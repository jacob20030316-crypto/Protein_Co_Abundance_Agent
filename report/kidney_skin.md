# Conserved co-abundance modules: kidney and skin

## Module 0

**Tissue pair**: kidney and skin  
**Genes (48)**: AAAS, AKAP8, AKAP8L, ANKHD1, ANAPC1, MTHFD1L, CCDC86, DAXX, DDX46, DDX55, DDX56, POLD3, EXOSC5, EXOSC9, FBXO30, GIGYF2, HDAC3, LAS1L, LUC7L, METAP1, MTFR1, NBN, NLE1, NOL11, NOL8, NUP88, NUP98, PARG, PPAT, RBM22, RBM26, RCOR1, RAB11FIP1, RPP40, RRP1B, SNRNP40, SUZ12, TASOR, TGS1, TNRC6B, USP16, UTP15, UTP4, VIRMA, WAPL, WDR12, WDR36, WDR3

### Function

This is a conserved nuclear RNA biogenesis module, with the strongest primary evidence for ribonucleoprotein complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 6.43e-08), ribosome biogenesis (GO:BP ribosome biogenesis; q_global = 4.39e-07), rRNA processing (GO:BP rRNA processing; q_global = 6.52e-06), rRNA metabolism (GO:BP rRNA metabolic process; q_global = 2.99e-05), nucleolar localization (GO:CC nucleolus; q_global = 7.59e-06), and preribosome association (GO:CC preribosome; q_global = 0.0495). The convergence of the globally corrected GO terms, the nucleolar localizations, the STRING enrichments for rRNA processing and ribosome biogenesis (STRING Keyword rRNA processing; within-query FDR = 6.22e-08), (STRING Process Ribonucleoprotein complex biogenesis; within-query FDR = 1.73e-07), (STRING Process Ribosome biogenesis; within-query FDR = 8.71e-07), and the dense relationships among NOL11, UTP4, UTP15, WDR3, WDR12, WDR36, EXOSC5, EXOSC9, DDX56, and RRP1B supports a coordinated role in maturation, surveillance, and handling of ribosomal RNA. The module also contains a broader RNA-processing and nuclear gene-regulation layer, including spliceosome-associated proteins, RNA-binding proteins, nucleoporins, chromatin regulators, and RNA-modification machinery, supported by (GO:BP RNA processing; q_global = 7.74e-05), (GO:MF RNA binding; q_global = 0.00013), (GO:BP nucleic acid metabolic process; q_global = 0.00273), (GO:MF nucleic acid binding; q_global = 0.00355), (GO:BP gene expression; q_global = 0.0113), (GO:BP RNA metabolic process; q_global = 0.0168), (GO:BP RNA biosynthetic process; q_global = 0.0271), (STRING Component Nuclear protein-containing complex; within-query FDR = 4.4e-06), (STRING Function RNA binding; within-query FDR = 9.16e-06), and (STRING Process RNA processing; within-query FDR = 9.58e-06). Thus, the most defensible functional interpretation is a core nucleolar ribosome-biogenesis program embedded in broader nuclear RNA processing and gene-expression control, rather than a tissue-specific metabolic or extracellular pathway.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins: HPA reports no secreted genes. It is also not broadly blood-cell enriched; most genes have low immune-cell specificity and low tissue specificity. HPA protein detection in kidney and skin is widespread across the module, supporting the presence of the encoded proteins in both tissues. Some cell-type-enhanced signals occur in neutrophils, reproductive cell types, progenitors, cardiomyocytes, basal epithelial cells, and other cell populations, but these are heterogeneous rather than pointing to a single contaminating blood or immune population. The module therefore more plausibly reflects a shared intracellular program, such as nucleolar activity and RNA production, present across cells in kidney and skin. The few tissue-enhanced annotations, including parathyroid gland, bone marrow, and blood vessel, do not establish that the module is driven by those tissues.

**GO/KEGG enrichment**: 26 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP ribonucleoprotein complex biogenesis | 6.43e-08 | DDX46, DDX56, EXOSC5, EXOSC9, LAS1L, LUC7L, NLE1, NOL11, NOL8, NUP88, RPP40, RRP1B, TGS1, USP16, UTP15, UTP4, WDR12, WDR3, WDR36 |
| GO:BP ribosome biogenesis | 4.39e-07 | DDX56, EXOSC5, EXOSC9, LAS1L, NLE1, NOL11, NOL8, NUP88, RPP40, RRP1B, USP16, UTP15, UTP4, WDR12, WDR3, WDR36 |
| GO:BP rRNA processing | 6.52e-06 | DDX56, EXOSC5, EXOSC9, LAS1L, NOL11, NOL8, RPP40, RRP1B, UTP15, UTP4, WDR12, WDR3, WDR36 |
| GO:CC nucleolus | 7.59e-06 | AKAP8, CCDC86, DAXX, DDX46, DDX55, DDX56, EXOSC5, EXOSC9, LAS1L, NBN, NLE1, NOL11, NOL8, RPP40, RRP1B, SUZ12, TGS1, UTP15, UTP4, WDR12, WDR3, WDR36 |
| GO:CC nuclear protein-containing complex | 1.79e-05 | AAAS, ANAPC1, DDX46, EXOSC5, EXOSC9, HDAC3, LAS1L, LUC7L, NBN, NOL11, NUP88, NUP98, POLD3, RBM22, RCOR1, RPP40, SNRNP40, SUZ12, TGS1, UTP15, UTP4, WDR12, WDR3, WDR36 |
| GO:BP rRNA metabolic process | 2.99e-05 | DDX56, EXOSC5, EXOSC9, LAS1L, NOL11, NOL8, RPP40, RRP1B, UTP15, UTP4, WDR12, WDR3, WDR36 |
| GO:BP RNA processing | 7.74e-05 | AKAP8L, DDX46, DDX56, EXOSC5, EXOSC9, LAS1L, LUC7L, NOL11, NOL8, NUP98, RBM22, RPP40, RRP1B, SNRNP40, TGS1, UTP15, UTP4, VIRMA, WDR12, WDR3, WDR36 |
| GO:MF RNA binding | 0.00013 | AKAP8, AKAP8L, ANKHD1, CCDC86, DDX46, DDX55, DDX56, EXOSC5, EXOSC9, GIGYF2, LAS1L, LUC7L, NOL11, NOL8, NUP98, RBM22, RBM26, RPP40, RRP1B, SNRNP40, SUZ12, TASOR, TNRC6B, UTP15, UTP4, VIRMA, WDR3 |
| GO:CC nuclear lumen | 0.000188 | AAAS, AKAP8, AKAP8L, ANAPC1, CCDC86, DAXX, DDX46, DDX55, DDX56, EXOSC5, EXOSC9, HDAC3, LAS1L, NBN, NLE1, NOL11, NOL8, NUP88, NUP98, PARG, POLD3, RBM22, RCOR1, RPP40, RRP1B, SNRNP40, SUZ12, TASOR, TGS1, TNRC6B, USP16, UTP15, UTP4, VIRMA, WAPL, WDR12, WDR3, WDR36 |
| GO:CC ribonucleoprotein complex | 0.000982 | AKAP8L, DDX46, LUC7L, NUP98, RBM22, RPP40, RRP1B, SNRNP40, SUZ12, TGS1, UTP15, UTP4, WDR12, WDR3, WDR36 |
| GO:CC nucleoplasm | 0.00104 | AAAS, AKAP8, AKAP8L, ANAPC1, CCDC86, DAXX, DDX46, DDX55, EXOSC5, EXOSC9, HDAC3, LAS1L, NBN, NLE1, NOL11, NUP88, NUP98, PARG, POLD3, RBM22, RCOR1, RPP40, RRP1B, SNRNP40, SUZ12, TASOR, TGS1, TNRC6B, USP16, UTP15, UTP4, VIRMA, WAPL, WDR12, WDR3 |
| GO:BP nucleic acid metabolic process | 0.00273 | AKAP8L, DAXX, DDX46, DDX56, EXOSC5, EXOSC9, GIGYF2, HDAC3, LAS1L, LUC7L, NBN, NOL11, NOL8, NUP98, PARG, POLD3, RBM22, RCOR1, RPP40, RRP1B, SNRNP40, SUZ12, TGS1, TNRC6B, USP16, UTP15, UTP4, VIRMA, WAPL, WDR12, WDR3, WDR36 |
| GO:MF nucleic acid binding | 0.00355 | AKAP8, AKAP8L, ANKHD1, CCDC86, DDX46, DDX55, DDX56, EXOSC5, EXOSC9, GIGYF2, HDAC3, LAS1L, LUC7L, NBN, NOL11, NOL8, NUP98, RBM22, RBM26, RPP40, RRP1B, SNRNP40, SUZ12, TASOR, TNRC6B, UTP15, UTP4, VIRMA, WDR3 |
| GO:BP gene expression | 0.0113 | AKAP8, AKAP8L, DAXX, DDX46, DDX56, EXOSC5, EXOSC9, FBXO30, GIGYF2, HDAC3, LAS1L, LUC7L, METAP1, NBN, NOL11, NOL8, NUP88, NUP98, RBM22, RCOR1, RPP40, RRP1B, SNRNP40, SUZ12, TASOR, TGS1, TNRC6B, USP16, UTP15, UTP4, VIRMA, WDR12, WDR3, WDR36 |
| GO:BP macromolecule biosynthetic process | 0.0115 | AKAP8, AKAP8L, DAXX, DDX46, DDX56, EXOSC5, EXOSC9, FBXO30, GIGYF2, HDAC3, LAS1L, LUC7L, METAP1, NBN, NOL11, NOL8, NUP88, NUP98, POLD3, RBM22, RCOR1, RPP40, RRP1B, SNRNP40, SUZ12, TASOR, TGS1, TNRC6B, USP16, UTP15, UTP4, VIRMA, WDR12, WDR3, WDR36 |

### STRING and hu.MAP

STRING provides extensive support for a known ribosome-biogenesis and RNA-processing core. Particularly coherent relationships connect NOL11 with UTP4, UTP15, WDR3, WDR12, and WDR36; connect EXOSC5 with EXOSC9 and several processome-associated proteins; connect DDX56 with WDR12, WDR3, WDR36, NLE1, and RRP1B; and connect NUP88 with NUP98 and AAAS. STRING also supports known nuclear regulatory relationships involving HDAC3, RCOR1, and SUZ12, as well as spliceosomal relationships involving RBM22 and SNRNP40. The STRING functional enrichments (STRING Keyword rRNA processing; within-query FDR = 6.22e-08) through (STRING COMPARTMENTS Nucleolus; within-query FDR = 1.48e-05) are supplementary and reinforce the globally corrected GO interpretation, but they are not being treated as global significance. hu.MAP independently identifies a high-confidence exosome-related complex containing EXOSC5 and EXOSC9 with other module members (hu.MAP huMAP3_14264.1), small-subunit-processome complexes containing NOL11, UTP4, and UTP15 (hu.MAP huMAP3_01743.1), nuclear-pore complexes involving NUP98, NUP88, and AAAS (hu.MAP huMAP3_12581.1), and spliceosomal complexes involving DDX46, TGS1, SNRNP40, and RBM22 (hu.MAP huMAP3_08980.1), (hu.MAP huMAP3_06726.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), (hu.MAP huMAP3_04549.1), (hu.MAP huMAP3_09945.1), and (hu.MAP huMAP3_06511.1). Additional complexes support AKAP8 and AKAP8L (hu.MAP huMAP3_02863.1), NOL8 and WDR36 (hu.MAP huMAP3_08465.1), and SUZ12 with RCOR1 (hu.MAP huMAP3_15128.1). These observations indicate that the module contains real molecular assemblies and not merely unrelated genes that happen to share expression patterns. The network also includes cross-connections between these assemblies, although co-abundance does not by itself prove direct physical interaction.

**STRING interactions (score >= 0.7)**: 51 of 1128 gene pairs: AAAS–NUP88 (0.994); AAAS–NUP98 (0.96); DDX55–DDX56 (0.942); DDX55–WDR12 (0.977); DDX56–NLE1 (0.745); DDX56–RRP1B (0.829); DDX56–UTP4 (0.82); DDX56–WDR12 (0.917); DDX56–WDR3 (0.893); DDX56–WDR36 (0.923); EXOSC5–EXOSC9 (0.999); EXOSC5–UTP15 (0.823); EXOSC5–UTP4 (0.839); EXOSC5–WDR3 (0.851); EXOSC5–WDR36 (0.735); EXOSC9–UTP15 (0.772); EXOSC9–UTP4 (0.823); EXOSC9–WDR3 (0.742); EXOSC9–WDR36 (0.77); GIGYF2–TNRC6B (0.749); HDAC3–RCOR1 (0.812); HDAC3–SUZ12 (0.733); LAS1L–RRP1B (0.785); LAS1L–WDR3 (0.737); MTHFD1L–PPAT (0.845); NLE1–RRP1B (0.799); NLE1–WDR12 (0.859); NLE1–WDR36 (0.857); NOL11–UTP15 (0.986); NOL11–UTP4 (0.999); NOL11–WDR12 (0.78); NOL11–WDR3 (0.951); NOL11–WDR36 (0.936); NUP88–NUP98 (0.999); RBM22–SNRNP40 (0.997); RCOR1–SUZ12 (0.892); RRP1B–UTP15 (0.734); RRP1B–UTP4 (0.734); RRP1B–WDR12 (0.979); RRP1B–WDR3 (0.796); RRP1B–WDR36 (0.824); UTP15–UTP4 (0.999); UTP15–WDR12 (0.869); UTP15–WDR3 (0.999); UTP15–WDR36 (0.999); UTP4–WDR12 (0.939); UTP4–WDR3 (0.999); UTP4–WDR36 (0.999); WDR12–WDR3 (0.954); WDR12–WDR36 (0.948); WDR3–WDR36 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword rRNA processing (FDR = 6.22e-08, 11 genes); Process Ribonucleoprotein complex biogenesis (FDR = 1.73e-07, 18 genes); COMPARTMENTS Nuclear lumen (FDR = 2.23e-07, 29 genes); NetworkNeighborAL rRNA processing, and RNA helicase activity (FDR = 5.76e-07, 14 genes); Component Nucleolus (FDR = 7.32e-07, 22 genes); Process Ribosome biogenesis (FDR = 8.71e-07, 15 genes); NetworkNeighborAL rRNA processing, and Ribosomal large subunit biogenesis (FDR = 2.3e-06, 13 genes); Process rRNA processing (FDR = 2.84e-06, 13 genes); Component Nuclear protein-containing complex (FDR = 4.4e-06, 23 genes); COMPARTMENTS Nucleus (FDR = 5.69e-06, 39 genes); Component Nuclear lumen (FDR = 7.66e-06, 38 genes); Function RNA binding (FDR = 9.16e-06, 28 genes); Process RNA processing (FDR = 9.58e-06, 21 genes); Component Nucleoplasm (FDR = 1.12e-05, 36 genes); COMPARTMENTS Nucleolus (FDR = 1.48e-05, 17 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14264.1 (EXOSC9, UTP15, UTP4, NOL11, EXOSC5; 5/20); huMAP3_01743.1 (UTP15, UTP4, NOL11; 3/6); huMAP3_12581.1 (NUP98, NUP88, AAAS; 3/58); huMAP3_08980.1 (DDX46, SNRNP40, TGS1; 3/97); huMAP3_02863.1 (AKAP8, AKAP8L; 2/3); huMAP3_14364.1 (UTP4, NOL11; 2/4); huMAP3_05948.1 (NUP98, NUP88; 2/5); huMAP3_07705.1 (NUP98, AAAS; 2/9); huMAP3_06369.1 (NUP98, NUP88; 2/12); huMAP3_09710.1 (NUP98, AAAS; 2/13); huMAP3_08465.1 (NOL8, WDR36; 2/17); huMAP3_05382.1 (EXOSC9, EXOSC5; 2/18); huMAP3_06726.1 (SNRNP40, RBM22; 2/37); huMAP3_10000.1 (NUP98, NUP88; 2/44); huMAP3_08501.1 (SNRNP40, RBM22; 2/47); huMAP3_09504.1 (SNRNP40, RBM22; 2/51); huMAP3_04549.1 (DDX46, TGS1; 2/52); huMAP3_09945.1 (SNRNP40, RBM22; 2/61); huMAP3_06511.1 (DDX46, TGS1; 2/79); huMAP3_15128.1 (SUZ12, RCOR1; 2/96)

### Novelty

This should not be described as a wholly new molecular pathway. The central ribosome-biogenesis and RNA-processing relationships are already represented in STRING and hu.MAP, including known small-subunit-processome, exosome, spliceosome, and nuclear-pore assemblies. The module is therefore a new co-abundance observation or tissue-pair organization of largely established biology, rather than a discovery of an unknown ribosome-biogenesis complex. Its potentially novel aspect is the conservation of this coordinated nuclear program across kidney and skin and the way the co-abundance network links several established assemblies in those tissues. That interpretation remains provisional because the fact sheet does not establish causality, directionality, cell-state specificity, or whether the same cells account for the signal in both tissues. Lack of a STRING or hu.MAP annotation for individual genes is not evidence that their participation is novel.

**Hypothesis.** Hypothesis: a shared requirement for high-quality nuclear RNA production in kidney and skin coordinates nucleolar ribosome assembly with RNA surveillance, splicing, nuclear transport, and chromatin regulation. In this model, the NOL11–UTP4–UTP15–WDR3–WDR12–WDR36 axis supports ribosomal RNA maturation, EXOSC5 and EXOSC9 provide RNA processing or surveillance capacity, and NUP98–NUP88–AAAS connect nuclear transport with the movement of RNA and ribosomal subunits. Regulatory proteins such as SUZ12, RCOR1, HDAC3, USP16, and DAXX could tune this program according to proliferation, differentiation, stress, or DNA-damage state. The cross-tissue conservation could therefore reflect a shared nucleolar and nuclear maintenance program rather than a kidney-specific or skin-specific pathway. This hypothesis should be tested with cell-resolved measurements, perturbation of the processome or exosome components, and direct assessment of ribosomal RNA maturation and nuclear RNA export.

### Important genes

#### NOL11

- **Related proteins** (co-abundance neighbors): UTP4 (0.87), WDR3 (0.87), WDR12 (0.86), ANAPC1 (0.83), LAS1L (0.82), AKAP8L (0.82), ANKHD1 (0.81), NLE1 (0.81), AKAP8 (0.81), RPP40 (0.80), SNRNP40 (0.80), LUC7L (0.80); STRING partners: UTP15 (0.986), UTP4 (0.999), WDR12 (0.78), WDR3 (0.951), WDR36 (0.936)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_14264.1, huMAP3_01743.1, huMAP3_14364.1
- **Function (MyGene.info)**: nucleolar protein 11. Enables RNA binding activity. Involved in maturation of SSU-rRNA and positive regulation of transcription of nucleolar large rRNA by RNA polymerase I. Located in nucleolus. Part of t-UTP complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: diabetes mellitus (0.100); type 2 diabetes mellitus (0.100); atrial fibrillation (0.087); ulcerative colitis (0.011); cancer (0.011)
- **Europe PMC papers**: 240
- **Why important**: NOL11 is a high-connectivity module hub and is linked to many of the primary terms for ribonucleoprotein biogenesis, ribosome biogenesis, rRNA processing, the nucleolus, and RNA binding (GO:BP ribonucleoprotein complex biogenesis; q_global = 6.43e-08) through (GO:CC intracellular membraneless organelle; q_global = 0.0445). It is a nucleolar RNA-binding component of the t-UTP complex and is present in several hu.MAP processome complexes (hu.MAP huMAP3_14264.1), (hu.MAP huMAP3_01743.1), and (hu.MAP huMAP3_14364.1). Its strong STRING relationships with UTP4, UTP15, WDR3, WDR12, and WDR36 place it at the center of the module's most coherent subnetwork. HPA detects the protein in both kidney and skin, and its literature and disease-association record is substantial enough to support established biological relevance without implying a disease mechanism here.
- **Conclusion**: Established evidence supports NOL11 as a central component of the module's nucleolar ribosome-biogenesis core. It is a plausible organizing marker of the conserved module. It remains a hypothesis that NOL11 is a causal driver of the cross-tissue co-abundance pattern or that it coordinates the peripheral RNA-processing and chromatin components.

#### UTP4

- **Related proteins** (co-abundance neighbors): UTP15 (0.88), NOL11 (0.87), ANAPC1 (0.86), RPP40 (0.85), WDR3 (0.83); STRING partners: DDX56 (0.82), EXOSC5 (0.839), EXOSC9 (0.823), NOL11 (0.999), RRP1B (0.734), UTP15 (0.999), WDR12 (0.939), WDR3 (0.999), WDR36 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_14264.1, huMAP3_01743.1, huMAP3_14364.1
- **Function (MyGene.info)**: UTP4 small subunit processome component. This gene encodes a WD40-repeat-containing protein that is localized to the nucleolus. Mutation of this gene causes North American Indian childhood cirrhosis, a severe intrahepatic cholestasis that results in transient neonatal jaundice, and progresses to periportal fibrosis and cirrhosis in childhood and adolescence. Alternative splicing results in multiple transcript variants. [provided by RefSe…
- **Diseases (Open Targets)**: hereditary North American Indian childhood cirrhosis (0.420); cardiovascular disorder (0.101); basal cell carcinoma (0.079); hypertensive disorder (0.064); osteosarcoma (0.052)
- **Europe PMC papers**: 214
- **Why important**: UTP4 is a core processome gene with high connectivity to UTP15, NOL11, RPP40, WDR3, and related ribosome-biogenesis proteins. It appears across essentially the full set of primary terms, including ribonucleoprotein complex biogenesis, ribosome biogenesis, rRNA processing, the nucleolus, and preribosome (GO:BP ribonucleoprotein complex biogenesis; q_global = 6.43e-08) through (GO:CC preribosome; q_global = 0.0495). It is represented in multiple hu.MAP complexes (hu.MAP huMAP3_14264.1), (hu.MAP huMAP3_01743.1), and (hu.MAP huMAP3_14364.1), and STRING supports strong relationships with the principal processome and exosome-associated genes. HPA detects it in kidney and skin, with cell-type enhancement in proximal tubule cells and oocytes. Its established disease association with North American Indian childhood cirrhosis further demonstrates that disruption of this conserved machinery can have organismal consequences.
- **Conclusion**: Established evidence identifies UTP4 as a core small-subunit-processome component and a strong functional anchor for the module. The kidney and skin co-abundance is consistent with shared cellular dependence on ribosome production. It is not established that UTP4 specifically explains tissue conservation or disease susceptibility in these samples.

#### WDR3

- **Related proteins** (co-abundance neighbors): NOL11 (0.87), RRP1B (0.83), UTP4 (0.83), NOL8 (0.82), LAS1L (0.82), NUP98 (0.81); STRING partners: DDX56 (0.893), EXOSC5 (0.851), EXOSC9 (0.742), LAS1L (0.737), NOL11 (0.951), RRP1B (0.796), UTP15 (0.999), UTP4 (0.999), WDR12 (0.954), WDR36 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 3. This gene encodes a nuclear protein containing 10 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, which usually include a trp-asp at the C-terminal end. Proteins belonging to the WD repeat family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. [provid…
- **Diseases (Open Targets)**: presbycusis (0.335); respiratory tract infectious disorder (0.184); neurodegenerative disease (0.143); preeclampsia (0.120); alcohol drinking (0.098)
- **Europe PMC papers**: 280
- **Why important**: WDR3 is a nucleolar WD-repeat protein with a high module position and broad coverage of the primary enrichment terms, including every primary term listed for the module (GO:BP ribonucleoprotein complex biogenesis; q_global = 6.43e-08) through (GO:CC preribosome; q_global = 0.0495). It has extensive STRING support with NOL11, UTP15, UTP4, WDR12, WDR36, DDX56, EXOSC5, EXOSC9, RRP1B, and LAS1L. Its established annotation in small-subunit rRNA maturation and ribosomal biogenesis, together with its membership in the module's densest known interaction neighborhood, makes it an informative representative of the ribosome-biogenesis core. HPA places it in the nucleoli and reports low tissue specificity, which fits a conserved housekeeping-like nuclear function rather than a secreted or tissue-exclusive role.
- **Conclusion**: Established evidence supports WDR3 as a central structural or assembly-associated component of the nucleolar subnetwork. Its position makes it useful for validating the module experimentally. A direct role for WDR3 in coordinating the broader spliceosome, nuclear-pore, or chromatin branches remains hypothetical.

#### EXOSC5

- **Related proteins** (co-abundance neighbors): RPP40 (0.80); STRING partners: EXOSC9 (0.999), UTP15 (0.823), UTP4 (0.839), WDR3 (0.851), WDR36 (0.735)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14264.1, huMAP3_05382.1
- **Function (MyGene.info)**: exosome component 5. Predicted to enable RNA binding activity. Involved in DNA deamination and exonucleolytic catabolism of deadenylated mRNA. Acts upstream of or within defense response to virus. Located in nucleolus; nucleoplasm; and transcriptionally active chromatin. Part of exosome (RNase complex). [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: cerebellar ataxia, brain abnormalities, and cardiac conduction defects (0.728); neurodegenerative disease (0.497); Global developmental delay (0.372); cerebellar ataxia (0.371); Short stature (0.370)
- **Europe PMC papers**: 405
- **Why important**: EXOSC5 links the module's ribosome-biogenesis signal to RNA surveillance. It is a member of the nuclear exosome, has strong STRING support with EXOSC9 and several processome-associated proteins, and occurs in high-confidence hu.MAP exosome complexes (hu.MAP huMAP3_14264.1) and (hu.MAP huMAP3_05382.1). It contributes to the primary terms for ribonucleoprotein complex biogenesis, ribosome biogenesis, rRNA processing, RNA processing, and rRNA metabolism (GO:BP ribonucleoprotein complex biogenesis; q_global = 6.43e-08) through (GO:BP RNA processing; q_global = 7.74e-05). Its annotated functions include rRNA processing and RNA catabolism, while HPA places it in the nucleolus and reports protein detection in kidney and skin. The absence of detected protein in the HPA samples should be considered a measurement result rather than evidence that the gene is irrelevant, because the module-level HPA summary shows broad detection across the tissues.
- **Conclusion**: Established evidence supports EXOSC5 as a bridge between RNA degradation or surveillance and nucleolar ribosome production. It strengthens the interpretation that the module involves RNA quality control as well as synthesis. Whether this bridge is functionally active in both tissues, rather than reflecting coordinated abundance of housekeeping machinery, remains a hypothesis.

#### NUP98

- **Related proteins** (co-abundance neighbors): TNRC6B (0.85), NOL8 (0.83), WDR3 (0.81); STRING partners: AAAS (0.96), NUP88 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12581.1, huMAP3_05948.1, huMAP3_07705.1, huMAP3_06369.1, huMAP3_09710.1, huMAP3_10000.1
- **Function (MyGene.info)**: nucleoporin 98 and 96 precursor. Nuclear pore complexes (NPCs) regulate the transport of macromolecules between the nucleus and cytoplasm, and are composed of many polypeptide subunits, many of which belong to the nucleoporin family. This gene belongs to the nucleoporin gene family and encodes a 186 kDa precursor protein that undergoes autoproteolytic cleavage to generate a 98 kDa nucleoporin and 96 kDa nucleoporin. The 98 kDa nu…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); acute myeloid leukemia (0.399); lung carcinoma (0.376)
- **Europe PMC papers**: 4839
- **Why important**: NUP98 represents the nuclear-transport branch of the module. It is connected in STRING to NUP88 and AAAS, occurs in several hu.MAP nuclear-pore complexes (hu.MAP huMAP3_12581.1), (hu.MAP huMAP3_05948.1), (hu.MAP huMAP3_07705.1), (hu.MAP huMAP3_06369.1), (hu.MAP huMAP3_09710.1), and (hu.MAP huMAP3_10000.1), and contributes to primary terms for nuclear protein-containing complexes, nuclear lumen, RNA processing, RNA binding, and gene expression (GO:CC nuclear protein-containing complex; q_global = 1.79e-05), (GO:BP RNA processing; q_global = 7.74e-05) through (GO:BP RNA biosynthetic process; q_global = 0.0271). Its established function includes nucleocytoplasmic transport and RNA export, providing a mechanistic link between nuclear RNA production and movement of RNA or ribosomal subunits. HPA reports a neutrophil-enriched single-cell pattern but low immune-cell specificity overall, so the module should not be interpreted as a neutrophil module on this basis alone. NUP98 also has a substantial literature and disease-association record, including viral disease and leukemia contexts.
- **Conclusion**: Established evidence supports NUP98 as a nuclear-pore component that may connect the nucleolar RNA program to nuclear export. Its presence does not demonstrate that transport is the primary function of the module; the dominant evidence still favors ribosome biogenesis. A coordinated transport role in the kidney–skin module is therefore a plausible hypothesis rather than a demonstrated mechanism.

## Module 1

**Tissue pair**: kidney and skin  
**Genes (10)**: ABLIM1, MTHFD1, CTNND1, HK1, PDCD6IP, PITRM1, RAI14, SLC12A7, TJP1, TJP2

### Function

The strongest integrated interpretation is an epithelial and endothelial cell-junction module, centered on tight-junction organization and regulation of barrier permeability. The primary, globally corrected evidence is protein localization to cell-cell junction (GO:BP protein localization to cell-cell junction; q_global = 0.0111), regulation and positive regulation of blood-brain barrier permeability (GO:BP regulation of blood-brain barrier permeability; q_global = 0.0182) (GO:BP positive regulation of blood-brain barrier permeability; q_global = 0.0182), and positive regulation of vascular permeability (GO:BP positive regulation of vascular permeability; q_global = 0.0428). These terms converge on junctional barrier biology rather than a general metabolic or immune function. The STRING annotations independently support apical-junction, tight-junction, cell-junction, and cell-cell-junction organization themes (STRING Component Apical junction complex; within-query FDR = 0.0027) (STRING Keyword Tight junction; within-query FDR = 0.0133) (STRING Keyword Cell junction; within-query FDR = 0.0168) (STRING Component Bicellular tight junction; within-query FDR = 0.035) (STRING Process Cell-cell junction organization; within-query FDR = 0.0441), while the barrier-related literature annotation (STRING PMID (2011) Molecular biology of the blood-brain and the blood-cerebrospinal fluid barriers: similarities and differences.; within-query FDR = 0.0195) is consistent supplementary evidence. The module also contains genes with plausible supporting roles in cytoskeletal attachment, ion transport, membrane trafficking, mitochondrial proteolysis, and intermediary metabolism, but those functions are not globally enriched module functions.

**Cell composition.** This does not look like a plasma-protein or secreted-protein module: the HPA summary identifies only one secreted gene, and the genes are detected in both kidney and skin. Most genes have low tissue specificity, so the shared signal is more consistent with broadly present cellular machinery than with a narrowly tissue-restricted program. HPA single-cell annotations are heterogeneous, including epithelial, podocyte, glial, cardiac, and germ-cell contexts. Several genes have immune-cell enhancement or group enrichment, but the module is not dominated by immune-cell-specific genes, and one junctional gene is not detected in immune cells. Thus, blood contamination or a shared blood-cell population is not the leading explanation, although cellular composition and junction-rich epithelial or endothelial populations could contribute to the co-abundance pattern.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP protein localization to cell-cell junction | 0.0111 | CTNND1, TJP1, TJP2 |
| GO:BP regulation of blood-brain barrier permeability | 0.0182 | TJP1, TJP2 |
| GO:BP positive regulation of blood-brain barrier permeability | 0.0182 | TJP1, TJP2 |
| GO:BP positive regulation of vascular permeability | 0.0428 | TJP1, TJP2 |

### STRING and hu.MAP

Known protein relationships provide a focused core rather than explaining the entire module. STRING supports a very strong CTNND1–TJP1 relationship and an especially strong TJP1–TJP2 relationship. TJP1, TJP2, and CTNND1 also recur in the STRING junction and barrier annotations (STRING Component Apical junction complex; within-query FDR = 0.0027) (STRING Keyword Tight junction; within-query FDR = 0.0133) (STRING Keyword Cell junction; within-query FDR = 0.0168) (STRING PMID (2011) Molecular biology of the blood-brain and the blood-cerebrospinal fluid barriers: similarities and differences.; within-query FDR = 0.0195) (STRING Component Bicellular tight junction; within-query FDR = 0.035) (STRING Process Cell-cell junction organization; within-query FDR = 0.0441). hu.MAP independently places TJP1 and TJP2 together in multiple complexes (hu.MAP huMAP3_06395.1) (hu.MAP huMAP3_10673.1), TJP2 with RAI14 (hu.MAP huMAP3_05613.1), and ABLIM1 with RAI14 (hu.MAP huMAP3_08205.1) (hu.MAP huMAP3_09542.1). These complexes connect tight-junction scaffolds to actin-associated and signaling machinery, but the partial membership of the module in each complex means that the co-abundance module is not identical to any one physical complex. The lack of recorded STRING partners or hu.MAP complexes for several genes indicates that network co-abundance adds information beyond established physical interaction maps.

**STRING interactions (score >= 0.7)**: 2 of 45 gene pairs: CTNND1–TJP1 (0.956); TJP1–TJP2 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Apical junction complex (FDR = 0.0027, 4 genes); Keyword Tight junction (FDR = 0.0133, 3 genes); Keyword Cell junction (FDR = 0.0168, 5 genes); PMID (2011) Molecular biology of the blood-brain and the blood-cerebrospinal fluid barriers: similarities and differences. (FDR = 0.0195, 5 genes); Component Bicellular tight junction (FDR = 0.035, 3 genes); Process Cell-cell junction organization (FDR = 0.0441, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06395.1 (TJP1, TJP2; 2/8); huMAP3_05613.1 (RAI14, TJP2; 2/11); huMAP3_10673.1 (TJP1, TJP2; 2/14); huMAP3_08205.1 (ABLIM1, RAI14; 2/17); huMAP3_09542.1 (ABLIM1, RAI14; 2/38)

### Novelty

The module should not be called a newly discovered tight-junction complex. Its central interpretation is already strongly supported by established biology for TJP1, TJP2, and CTNND1, and the relevant interactions and complexes are represented in STRING and hu.MAP. A more defensible novelty claim is that this particular cross-tissue co-abundance configuration may reveal a conserved kidney–skin expression program that combines junctional scaffolding with ion handling, cytoskeletal regulation, vesicle biology, mitochondrial processing, and folate or glucose metabolism. That is a hypothesis-generating systems-level observation, not proof of a new molecular interaction or a kidney–skin-specific mechanism. Absence of some genes from interaction databases cannot establish novelty, especially because co-abundance does not require direct physical binding.

**Hypothesis.** Hypothesis: the shared module represents a conserved barrier-maintenance state in junction-forming epithelial or endothelial populations. TJP1 and TJP2 may provide the principal junctional scaffold, with CTNND1 linking adhesion complexes to signaling and the actin cytoskeleton. ABLIM1 and RAI14 may help organize actin-associated architecture, while SLC12A7 may couple junctional state to ion and cell-volume homeostasis. PDCD6IP could connect membrane trafficking and junction turnover, and the metabolic or mitochondrial genes may reflect the energetic and proteostatic requirements of maintaining polarized barrier cells. This model predicts coordinated changes in junction integrity, permeability, cytoskeletal organization, and ion homeostasis, but it requires experimental testing and should not be treated as established causation.

### Important genes

#### TJP1

- **Related proteins** (co-abundance neighbors): SLC12A7 (0.86); STRING partners: CTNND1 (0.956), TJP2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cell Junctions; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_06395.1, huMAP3_10673.1
- **Function (MyGene.info)**: tight junction protein 1. This gene encodes a member of the membrane-associated guanylate kinase (MAGUK) family of proteins, and acts as a tight junction adaptor protein that also regulates adherens junctions. Tight junctions regulate the movement of ions and macromolecules between endothelial and epithelial cells. The multidomain structure of this scaffold protein, including a postsynaptic density 95/disc-large/zona occlu…
- **Diseases (Open Targets)**: dengue disease (0.476); COVID-19 (0.373); skin disorder (0.312); Hypocalcemia (0.264); cataract (0.256)
- **Europe PMC papers**: 6421
- **Why important**: TJP1 is a central anchor of the interpretation. It is a junction-localized MAGUK scaffold with established roles in tight-junction and adherens-junction organization, and it participates in all globally corrected terms (GO:BP protein localization to cell-cell junction; q_global = 0.0111) (GO:BP regulation of blood-brain barrier permeability; q_global = 0.0182) (GO:BP positive regulation of blood-brain barrier permeability; q_global = 0.0182) (GO:BP positive regulation of vascular permeability; q_global = 0.0428). It has the strongest literature support among the module genes, direct STRING relationships with CTNND1 and TJP2, and hu.MAP support with TJP2 (hu.MAP huMAP3_06395.1) (hu.MAP huMAP3_10673.1). Its HPA localization to cell junctions and detection in both tissues fit the shared module particularly well.
- **Conclusion**: Established evidence supports TJP1 as a core junctional scaffold and a major interpretive driver of the module. It is reasonable to hypothesize that TJP1 helps organize the shared barrier-related state, but the co-abundance data alone do not demonstrate that TJP1 regulates the other module genes.

#### TJP2

- **Related proteins** (co-abundance neighbors): SLC12A7 (0.86), ABLIM1 (0.84); STRING partners: TJP1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cell Junctions; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_06395.1, huMAP3_05613.1, huMAP3_10673.1
- **Function (MyGene.info)**: tight junction protein 2. This gene encodes a zonula occluden that is a member of the membrane-associated guanylate kinase homolog family. The encoded protein functions as a component of the tight junction barrier in epithelial and endothelial cells and is necessary for proper assembly of tight junctions. Mutations in this gene have been identified in patients with hypercholanemia, and genomic duplication of a 270 kb regio…
- **Diseases (Open Targets)**: cholestasis, progressive familial intrahepatic, 4 (0.800); hypercholanemia, familial 1 (0.647); autosomal dominant nonsyndromic hearing loss (0.558); progressive familial intrahepatic cholestasis type 2 (0.527); deafness (0.467)
- **Europe PMC papers**: 1748
- **Why important**: TJP2 is the clearest complementary core gene. It is a zonula occludens protein required for tight-junction barrier assembly, participates in every globally corrected term (GO:BP protein localization to cell-cell junction; q_global = 0.0111) (GO:BP regulation of blood-brain barrier permeability; q_global = 0.0182) (GO:BP positive regulation of blood-brain barrier permeability; q_global = 0.0182) (GO:BP positive regulation of vascular permeability; q_global = 0.0428), and is present in every listed STRING enrichment theme (STRING Component Apical junction complex; within-query FDR = 0.0027) (STRING Keyword Tight junction; within-query FDR = 0.0133) (STRING Keyword Cell junction; within-query FDR = 0.0168) (STRING PMID (2011) Molecular biology of the blood-brain and the blood-cerebrospinal fluid barriers: similarities and differences.; within-query FDR = 0.0195) (STRING Component Bicellular tight junction; within-query FDR = 0.035) (STRING Process Cell-cell junction organization; within-query FDR = 0.0441). It has a very strong STRING relationship with TJP1 and appears with TJP1 in several hu.MAP complexes (hu.MAP huMAP3_06395.1) (hu.MAP huMAP3_10673.1), while its disease associations include cholestatic and hearing-related disorders consistent with epithelial barrier biology.
- **Conclusion**: Established evidence identifies TJP2 as a core barrier and junction component. Its co-abundance with TJP1 is compatible with coordinated junction assembly or maintenance, but whether it is functionally causal in the kidney–skin module remains untested.

#### CTNND1

- **Related proteins** (co-abundance neighbors): SLC12A7 (0.87), ABLIM1 (0.80); STRING partners: TJP1 (0.956)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin delta 1. This gene encodes a member of the Armadillo protein family, which function in adhesion between cells and signal transduction. Multiple translation initiation codons and alternative splicing result in many different isoforms being translated. Not all of the full-length natures of the described transcript variants have been determined. Read-through transcription also exists between this gene and the…
- **Diseases (Open Targets)**: blepharocheilodontic syndrome (0.724); listeriosis (0.526); cleft lip (0.510); hereditary disease (0.415); exudative vitreoretinopathy (0.376)
- **Europe PMC papers**: 3021
- **Why important**: CTNND1 links the module to adhesion and signaling beyond the tight-junction scaffold itself. It participates in the globally corrected cell-cell-junction localization term (GO:BP protein localization to cell-cell junction; q_global = 0.0111), has a strong STRING relationship with TJP1, and contributes to the STRING apical-junction and cell-junction themes (STRING Component Apical junction complex; within-query FDR = 0.0027) (STRING Keyword Cell junction; within-query FDR = 0.0168) (STRING PMID (2011) Molecular biology of the blood-brain and the blood-cerebrospinal fluid barriers: similarities and differences.; within-query FDR = 0.0195) (STRING Process Cell-cell junction organization; within-query FDR = 0.0441). Its annotated roles in cadherin-mediated adhesion, protein stabilization, migration, and sprouting angiogenesis make it a plausible bridge between junction structure and barrier-associated remodeling. It also has substantial literature and disease-association support.
- **Conclusion**: Established evidence supports CTNND1 as an adhesion-associated junctional linker. A plausible but unproven conclusion is that it couples the TJP scaffold to tissue remodeling or vascular behavior in the shared module.

#### SLC12A7

- **Related proteins** (co-abundance neighbors): PITRM1 (0.87), CTNND1 (0.87), TJP2 (0.86), TJP1 (0.86), HK1 (0.84), PDCD6IP (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 12 member 7. Enables protein kinase binding activity. Predicted to be involved in several processes, including cell volume homeostasis; inorganic ion homeostasis; and inorganic ion transmembrane transport. Part of protein-containing complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: clonal hematopoiesis (0.462); myasthenia gravis (0.342); edema (0.233); brain compression (0.233); preeclampsia (0.198)
- **Europe PMC papers**: 577
- **Why important**: SLC12A7 is the principal network-connected gene that broadens the module beyond junctional scaffolding. It has the strongest weighted network position in the supplied subgraph and connects to TJP1, TJP2, CTNND1, HK1, PITRM1, and PDCD6IP. Its known roles include chloride and potassium transport, ion and cell-volume homeostasis, and protein-kinase binding. HPA places it in cell types relevant to kidney epithelia and barrier-associated tissues, while STRING supplementary evidence links it to the blood-brain and blood-cerebrospinal-fluid barrier literature (STRING PMID (2011) Molecular biology of the blood-brain and the blood-cerebrospinal fluid barriers: similarities and differences.; within-query FDR = 0.0195).
- **Conclusion**: Established evidence supports SLC12A7 as an ion-homeostasis and transport component that is co-abundant with the junctional core. It is reasonable to hypothesize that ion or volume regulation supports barrier integrity, but the module does not establish a direct SLC12A7 interaction with the junction proteins.

## Module 2

**Tissue pair**: kidney and skin  
**Genes (36)**: ACIN1, BABAM1, BAG2, CDK13, DDX21, DHX9, ADAR, CLINT1, FAM120A, GTPBP3, MACROH2A1, HNRNPL, HNRNPR, IGF2BP3, TMPO, TMPO, LMNB1, LYAR, MYBBP1A, NASP, NOL6, NOP2, NOP56, PAAF1, PHC2, PPM1G, PSMC6, PSMB10, PSIP1, RBM33, RCC1, RPL12, RNF25, RRP12, SUPT16H, UTP14A

### Function

The module is most convincingly a conserved nuclear RNA and chromatin regulatory module. Primary evidence comes from globally corrected enrichment for nucleic acid binding (GO:MF nucleic acid binding; q_global = 0.000309), RNA binding (GO:MF RNA binding; q_global = 0.00302), chromatin (GO:CC chromatin; q_global = 0.00343), nucleic acid metabolism (GO:BP nucleic acid metabolic process; q_global = 0.00547), RNA metabolism (GO:BP RNA metabolic process; q_global = 0.0079), gene expression (GO:BP gene expression; q_global = 0.0084), ribonucleoprotein complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0203), RNA processing (GO:BP RNA processing; q_global = 0.0209), RNA biosynthesis (GO:BP RNA biosynthetic process; q_global = 0.0232), nucleoplasm (GO:CC nucleoplasm; q_global = 0.0407), and regulation of transcription by RNA polymerase I (GO:BP regulation of transcription by RNA polymerase I; q_global = 0.0415). The coherent biological interpretation is coordinated RNA processing, ribosome biogenesis, nucleolar function, transcriptional regulation, and chromatin organization. The module also contains supporting components for nuclear architecture, proteasomal regulation, RNA editing, RNA export, DNA repair, and mitochondrial RNA modification. The enrichment therefore supports a broad nuclear gene-expression maintenance program rather than a narrowly defined pathway.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity and low immune-cell specificity, and nearly all assessed proteins are detected in both kidney and skin. This argues against the module being primarily a blood-cell or sample-plasma signature. Nevertheless, HPA shows selected enhancement in lymphoid tissue, bone marrow, monocyte progenitors, neutrophils, erythroid progenitors, and germ-cell populations. These signals could contribute to co-abundance in particular specimens, but they do not dominate the module. The shared kidney-skin signal is therefore more consistent with a broadly expressed nuclear housekeeping and cellular-state program, with possible contributions from shared proliferative or resident cell populations.

**GO/KEGG enrichment**: 14 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleic acid binding | 0.000309 | ACIN1, ADAR, CDK13, DDX21, DHX9, FAM120A, HNRNPL, HNRNPR, IGF2BP3, LMNB1, LYAR, MACROH2A1, MYBBP1A, NOL6, NOP2, NOP56, PHC2, PSIP1, RBM33, RCC1, RPL12, RRP12, SUPT16H, TMPO, UTP14A |
| GO:CC nucleus | 0.00103 | ACIN1, ADAR, BABAM1, CDK13, CLINT1, DDX21, DHX9, FAM120A, GTPBP3, HNRNPL, HNRNPR, IGF2BP3, LMNB1, LYAR, MACROH2A1, MYBBP1A, NASP, NOL6, NOP2, NOP56, PAAF1, PHC2, PPM1G, PSIP1, PSMB10, PSMC6, RBM33, RCC1, RNF25, RRP12, SUPT16H, TMPO, UTP14A |
| GO:MF RNA binding | 0.00302 | ACIN1, ADAR, CDK13, DDX21, DHX9, FAM120A, HNRNPL, HNRNPR, IGF2BP3, LYAR, MYBBP1A, NOL6, NOP2, NOP56, PSIP1, RBM33, RPL12, RRP12, SUPT16H, UTP14A |
| GO:CC chromatin | 0.00343 | DDX21, DHX9, HNRNPL, MACROH2A1, MYBBP1A, NASP, PAAF1, PHC2, PSIP1, RCC1, SUPT16H, TMPO |
| GO:BP nucleic acid metabolic process | 0.00547 | ACIN1, ADAR, BABAM1, CDK13, DDX21, DHX9, GTPBP3, HNRNPL, HNRNPR, IGF2BP3, LYAR, MACROH2A1, MYBBP1A, NASP, NOL6, NOP2, NOP56, PAAF1, PHC2, PPM1G, PSIP1, PSMC6, RBM33, SUPT16H, UTP14A |
| GO:BP RNA metabolic process | 0.0079 | ACIN1, ADAR, CDK13, DDX21, DHX9, GTPBP3, HNRNPL, HNRNPR, IGF2BP3, LYAR, MACROH2A1, MYBBP1A, NOL6, NOP2, NOP56, PAAF1, PHC2, PPM1G, PSIP1, PSMC6, RBM33, SUPT16H, UTP14A |
| GO:BP gene expression | 0.0084 | ACIN1, ADAR, BAG2, CDK13, DDX21, DHX9, GTPBP3, HNRNPL, HNRNPR, IGF2BP3, LMNB1, LYAR, MACROH2A1, MYBBP1A, NOL6, NOP2, NOP56, PAAF1, PHC2, PPM1G, PSIP1, PSMC6, RBM33, RNF25, RPL12, SUPT16H, UTP14A |
| GO:BP ribonucleoprotein complex biogenesis | 0.0203 | ADAR, DDX21, DHX9, LYAR, MYBBP1A, NOL6, NOP2, NOP56, PSIP1, UTP14A |
| GO:BP RNA processing | 0.0209 | ACIN1, ADAR, CDK13, DDX21, DHX9, GTPBP3, HNRNPL, HNRNPR, LYAR, NOL6, NOP2, NOP56, PSIP1, UTP14A |
| GO:BP macromolecule biosynthetic process | 0.0216 | ACIN1, ADAR, BAG2, CDK13, DDX21, DHX9, GTPBP3, HNRNPL, HNRNPR, IGF2BP3, LMNB1, LYAR, MACROH2A1, MYBBP1A, NOL6, NOP2, NOP56, PAAF1, PHC2, PPM1G, PSIP1, PSMC6, RBM33, RNF25, RPL12, SUPT16H, UTP14A |
| GO:BP RNA biosynthetic process | 0.0232 | ACIN1, ADAR, CDK13, DDX21, DHX9, GTPBP3, HNRNPL, HNRNPR, LYAR, MACROH2A1, MYBBP1A, NOL6, NOP2, NOP56, PAAF1, PHC2, PPM1G, PSIP1, PSMC6, SUPT16H, UTP14A |
| GO:BP nucleic acid biosynthetic process | 0.0389 | ACIN1, ADAR, CDK13, DDX21, DHX9, GTPBP3, HNRNPL, HNRNPR, LYAR, MACROH2A1, MYBBP1A, NOL6, NOP2, NOP56, PAAF1, PHC2, PPM1G, PSIP1, PSMC6, SUPT16H, UTP14A |
| GO:CC nucleoplasm | 0.0407 | ACIN1, ADAR, BABAM1, CDK13, CLINT1, DDX21, DHX9, HNRNPL, HNRNPR, LMNB1, LYAR, MACROH2A1, MYBBP1A, NASP, NOL6, NOP2, NOP56, PAAF1, PHC2, PPM1G, PSIP1, PSMC6, RCC1, SUPT16H, UTP14A |
| GO:BP regulation of transcription by RNA polymerase I | 0.0415 | DDX21, LYAR, MACROH2A1, MYBBP1A |

### STRING and hu.MAP

STRING supports a dense, biologically coherent core centered on RNA helicases, heterogeneous nuclear ribonucleoproteins, and nucleolar ribosome-biogenesis proteins. Established high-confidence relationships include ADAR with DHX9, DDX21 with DHX9, MYBBP1A, NOP2, and NOP56, the HNRNPL-HNRNPR relationship, and the tightly connected NOL6-NOP56-UTP14A-NOP2-RRP12 group. LMNB1 and TMPO form a nuclear-envelope pair, while PSMB10, PSMC6, and PAAF1 connect a proteasome-related branch. The hu.MAP evidence independently identifies hnRNP-associated complexes containing HNRNPR, HNRNPL, ADAR, and FAM120A (hu.MAP huMAP3_10625.1), additional hnRNP assemblies (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09281.1) (hu.MAP huMAP3_07581.1), a chromatin or histone-associated complex containing PPM1G, MACROH2A1, and SUPT16H (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_10592.1), proteasome-associated complexes containing PSMB10, PSMC6, and PAAF1 (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1) (hu.MAP huMAP3_05064.1), and a lamin-associated complex containing LMNB1 and TMPO (hu.MAP huMAP3_09748.1). Thus, much of the module reflects known molecular relationships, while the co-abundance organization links these established nuclear subsystems in kidney and skin.

**STRING interactions (score >= 0.7)**: 30 of 630 gene pairs: ADAR–DHX9 (0.922); DDX21–DHX9 (0.908); DDX21–HNRNPR (0.73); DDX21–MYBBP1A (0.963); DDX21–NOP2 (0.761); DDX21–NOP56 (0.811); DHX9–HNRNPL (0.901); DHX9–HNRNPR (0.909); HNRNPL–HNRNPR (0.961); LMNB1–TMPO (0.981); LYAR–MYBBP1A (0.711); LYAR–NOP56 (0.749); LYAR–RPL12 (0.806); MYBBP1A–NOL6 (0.97); MYBBP1A–NOP2 (0.864); MYBBP1A–NOP56 (0.737); MYBBP1A–RRP12 (0.846); NASP–SUPT16H (0.727); NOL6–NOP2 (0.881); NOL6–NOP56 (0.998); NOL6–RRP12 (0.863); NOL6–UTP14A (0.997); NOP2–NOP56 (0.969); NOP2–RRP12 (0.844); NOP2–UTP14A (0.866); NOP56–RRP12 (0.938); NOP56–UTP14A (0.998); PAAF1–PSMC6 (0.705); PSMB10–PSMC6 (0.918); RRP12–UTP14A (0.978)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Isopeptide bond (FDR = 2.99e-07, 22 genes); Keyword Ubl conjugation (FDR = 8.71e-07, 23 genes); Function Nucleic acid binding (FDR = 0.00016, 25 genes); RCTM Metabolism of RNA (FDR = 0.00021, 15 genes); Function RNA binding (FDR = 0.001, 20 genes); Keyword Nucleus (FDR = 0.0013, 26 genes); Keyword RNA-binding (FDR = 0.0013, 12 genes); COMPARTMENTS Chromatin (FDR = 0.0014, 10 genes); COMPARTMENTS Nucleus (FDR = 0.0014, 28 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0014, 19 genes); Component Chromatin (FDR = 0.0025, 11 genes); Component Nucleus (FDR = 0.0025, 32 genes); Component Nuclear lumen (FDR = 0.0025, 27 genes); Keyword Methylation (FDR = 0.0033, 12 genes); Component Nucleoplasm (FDR = 0.0055, 25 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10625.1 (HNRNPR, HNRNPL, ADAR, FAM120A; 4/57); huMAP3_07225.1 (HNRNPR, HNRNPL, FAM120A; 3/7); huMAP3_09654.1 (HNRNPR, HNRNPL, FAM120A; 3/13); huMAP3_10659.1 (HNRNPR, HNRNPL, FAM120A; 3/28); huMAP3_10862.1 (PPM1G, MACROH2A1, SUPT16H; 3/33); huMAP3_09656.1 (PSMB10, PSMC6, PAAF1; 3/64); huMAP3_13725.1 (PSMB10, PSMC6, PAAF1; 3/69); huMAP3_09748.1 (LMNB1, TMPO; 2/3); huMAP3_10592.1 (PPM1G, MACROH2A1; 2/5); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09281.1 (HNRNPR, FAM120A; 2/14); huMAP3_07581.1 (HNRNPR, HNRNPL; 2/21); huMAP3_05064.1 (PSMC6, PAAF1; 2/31)

### Novelty

The module should not be described as a newly discovered molecular complex. Many of its relationships and subsystems are already established by STRING and hu.MAP, especially hnRNP assemblies, nucleolar ribosome biogenesis, chromatin organization, the nuclear lamina, and the proteasome. Its potentially novel aspect is the conserved co-abundance configuration across kidney and skin and the way these known components are coordinated in this tissue pair. That observation is hypothesis-generating rather than proof of a new physical complex or pathway. Absence of a gene from STRING or hu.MAP does not establish novelty, and the presence of globally enriched terms does not by itself establish a new mechanism.

**Hypothesis.** Mechanistic hypothesis: this module represents a shared nuclear homeostasis program that coordinates transcription, chromatin access, RNA editing and splicing, nucleolar ribosome production, and selective protein turnover in kidney and skin cells. In this model, DDX21, DHX9, HNRNPL, HNRNPR, and ADAR regulate RNA structure, processing, and editing; NOL6, NOP56, NOP2, RRP12, and UTP14A support ribosome biogenesis; LMNB1, TMPO, MACROH2A1, SUPT16H, and related factors couple nuclear architecture to chromatin state; and proteasome-associated genes buffer damaged or misassembled proteins. The shared co-abundance could therefore reflect coordinated demand for gene-expression quality control rather than a single tissue-specific function. This is a testable hypothesis, not an established causal model.

### Important genes

#### DDX21

- **Related proteins** (co-abundance neighbors): NOL6 (0.87), NOP2 (0.87), IGF2BP3 (0.83), HNRNPR (0.82), NOP56 (0.82), LMNB1 (0.81), MYBBP1A (0.81); STRING partners: DHX9 (0.908), HNRNPR (0.73), MYBBP1A (0.963), NOP2 (0.761), NOP56 (0.811)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 is a central connector between the nucleolar and RNA-processing portions of the module. It is present in every primary enrichment category from nucleic acid binding through RNA processing, ribonucleoprotein biogenesis, chromatin, and RNA polymerase I transcription (6 globally significant GO/KEGG terms, q_global 0.000309–0.0415; see the table). Its STRING relationships with DHX9, DDX21-associated nucleolar factors, HNRNPR, and MYBBP1A support known links between RNA helicase activity, ribosome biogenesis, and transcriptional regulation. HPA additionally identifies DDX21 in basal and suprabasal keratinocytes, directly relevant to the skin component.
- **Conclusion**: Established conclusion: DDX21 is a strong integrative marker of the module's RNA, nucleolar, and transcriptional functions. Hypothesis: it may help couple ribosome production and RNA processing to the differentiated or proliferative state of kidney and skin cells.

#### NOL6

- **Related proteins** (co-abundance neighbors): DDX21 (0.87), MYBBP1A (0.87), TMPO (0.85), LYAR (0.85), LMNB1 (0.84), NOP56 (0.84), PSIP1 (0.83), ADAR (0.82), PSMB10 (0.81); STRING partners: MYBBP1A (0.97), NOP2 (0.881), NOP56 (0.998), RRP12 (0.863), UTP14A (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleolar protein 6. The nucleolus is a dense subnuclear membraneless organelle that assembles around clusters of rRNA genes and functions in ribosome biogenesis. This gene encodes a nucleolar RNA-associated protein that is highly conserved between species. RNase treatment of permeabilized cells indicates that the nucleolar localization is RNA dependent. Further studies suggest that the protein is associated with ribo…
- **Diseases (Open Targets)**: neurodegenerative disease (0.119); hepatocellular carcinoma (0.054); hidradenitis (0.052); response to xenobiotic stimulus (0.045); gastric cancer (0.036)
- **Europe PMC papers**: 335
- **Why important**: NOL6 is a highly integrated nucleolar component with extensive module connectivity and broad support across the primary RNA-processing and ribonucleoprotein-biogenesis terms (8 globally significant GO/KEGG terms, q_global 0.000309–0.0389; see the table). Its STRING relationships with MYBBP1A, NOP2, NOP56, RRP12, and UTP14A form a coherent ribosome-biogenesis cluster. The supplied annotation describes RNA-dependent nucleolar localization, pre-rRNA association, small-subunit maturation, and ribosome biogenesis. NOL6 is detected in both kidney and skin, while its cell-type enhancement in spermatids suggests that its expression can also track high RNA-production states.
- **Conclusion**: Established conclusion: NOL6 is a core nucleolar and ribosome-biogenesis representative of the module. Hypothesis: coordinated NOL6 abundance may report cellular demand for nucleolar RNA processing rather than a kidney- or skin-specific biochemical activity.

#### NOP56

- **Related proteins** (co-abundance neighbors): HNRNPR (0.88), FAM120A (0.87), ADAR (0.86), SUPT16H (0.86), NOL6 (0.84), LMNB1 (0.84), DDX21 (0.82), ACIN1 (0.82), LYAR (0.81); STRING partners: DDX21 (0.811), LYAR (0.749), MYBBP1A (0.737), NOL6 (0.998), NOP2 (0.969), RRP12 (0.938), UTP14A (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP56 ribonucleoprotein. Nop56p is a yeast nucleolar protein that is part of a complex with the nucleolar proteins Nop58p and fibrillarin. Nop56p is required for assembly of the 60S ribosomal subunit and is involved in pre-rRNA processing. The protein encoded by this gene is similar in sequence to Nop56p and is also found in the nucleolus. Expansion of a GGCCTG repeat from 3-8 copies to 1500-2500 copies in an intron of th…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 36 (0.586); neurodegenerative disease (0.495); ovarian neoplasm (0.272); hereditary disease (0.193); cerebellar ataxia (0.121)
- **Europe PMC papers**: 1517
- **Why important**: NOP56 is a central member of the nucleolar interaction cluster and is represented across nearly all primary RNA, nucleic-acid, gene-expression, and nucleoplasm enrichments (9 globally significant GO/KEGG terms, q_global 0.000309–0.0407; see the table). STRING supports its established relationships with NOL6, NOP2, RRP12, UTP14A, DDX21, and MYBBP1A. Its annotation identifies roles in rRNA processing, rRNA modification, and ribosomal-subunit biogenesis. The disease association with spinocerebellar ataxia type thirty-six demonstrates clinically important consequences of perturbing this conserved nucleolar machinery.
- **Conclusion**: Established conclusion: NOP56 is a core ribosome-biogenesis and rRNA-processing component, not merely a generic nuclear marker. Hypothesis: its co-abundance with the module may reflect coordinated control of ribosome production and RNA quality in both tissues.

#### ADAR

- **Related proteins** (co-abundance neighbors): FAM120A (0.87), NOP56 (0.86), PSMC6 (0.85), NOL6 (0.82), MYBBP1A (0.82), HNRNPR (0.82), RRP12 (0.81), LMNB1 (0.81), RCC1 (0.80); STRING partners: DHX9 (0.922)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_10625.1
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR provides a distinctive enzymatic function within the module: site-specific adenosine-to-inosine RNA editing and destabilization of double-stranded RNA. It is highly integrated in the module and appears throughout the primary RNA, nucleic-acid, gene-expression, RNA-processing, and nucleoplasm evidence (10 globally significant GO/KEGG terms, q_global 0.000309–0.0407; see the table). Its established STRING relationship with DHX9 and its hu.MAP membership in an hnRNP-associated complex (hu.MAP huMAP3_10625.1) connect RNA editing with RNA structure and processing. ADAR is associated with Aicardi-Goutieres syndrome and dyschromatosis symmetrica hereditaria, and it is detected in kidney and skin.
- **Conclusion**: Established conclusion: ADAR adds RNA-editing and double-stranded-RNA handling to the module's core nuclear RNA function. Hypothesis: ADAR may connect ordinary RNA-processing demand with tissue responses to endogenous nucleic-acid stress or antiviral-like signaling.

#### HNRNPR

- **Related proteins** (co-abundance neighbors): SUPT16H (0.93), RPL12 (0.93), NOP56 (0.88), FAM120A (0.88), NOP2 (0.86), DHX9 (0.84), RRP12 (0.83), DDX21 (0.82), HNRNPL (0.82), ADAR (0.82), LMNB1 (0.80); STRING partners: DDX21 (0.73), DHX9 (0.909), HNRNPL (0.961)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_07225.1, huMAP3_09654.1, huMAP3_10659.1, huMAP3_06093.1, huMAP3_09281.1, huMAP3_07581.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR is the strongest network hub in the supplied module and occupies the intersection of RNA binding, RNA processing, gene expression, nucleoplasm, and nucleic-acid metabolism (10 globally significant GO/KEGG terms, q_global 0.000309–0.0407; see the table). Its known function in spliceosome-associated pre-mRNA processing and transport is directly concordant with the enrichment profile. STRING supports relationships with HNRNPL, DHX9, and DDX21, while hu.MAP places it in several hnRNP assemblies with HNRNPL, ADAR, and FAM120A (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09281.1) (hu.MAP huMAP3_07581.1). Its developmental and neurodevelopmental disease associations and substantial literature support make it a biologically informative hub rather than a purely technical connector.
- **Conclusion**: Established conclusion: HNRNPR is a central RNA-binding and pre-mRNA-processing organizer of the module. Hypothesis: variation in this hub could redistribute RNA-processing activity across several module branches and thereby influence tissue cell-state programs.

#### LMNB1

- **Related proteins** (co-abundance neighbors): NOP2 (0.89), FAM120A (0.86), HNRNPL (0.85), NOL6 (0.84), NOP56 (0.84), DDX21 (0.81), MACROH2A1 (0.81), ADAR (0.81), HNRNPR (0.80), MYBBP1A (0.80); STRING partners: TMPO (0.981)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_09748.1
- **Function (MyGene.info)**: lamin B1. This gene encodes one of the two B-type lamin proteins and is a component of the nuclear lamina. A duplication of this gene is associated with autosomal dominant adult-onset leukodystrophy (ADLD). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: microcephaly 26, primary, autosomal dominant (0.723); autosomal dominant primary microcephaly (0.675); adult-onset autosomal dominant demyelinating leukodystrophy (0.670); hereditary disease (0.488); Syndrome with microcephaly as major feature (0.487)
- **Europe PMC papers**: 3851
- **Why important**: LMNB1 links the RNA-rich nuclear network to nuclear architecture. It is a high-connectivity module member, appears in nucleic-acid binding, nucleus, gene-expression, macromolecule biosynthesis, and nucleoplasm enrichments (5 globally significant GO/KEGG terms, q_global 0.000309–0.0407; see the table), and is annotated as a nuclear-lamina component involved in nuclear-envelope organization, heterochromatin formation, nuclear-pore localization, and nuclear migration. Its strong STRING relationship with TMPO and hu.MAP association with the LMNB1-TMPO complex (hu.MAP huMAP3_09748.1) provide direct support for the nuclear-envelope branch. LMNB1 is detected in kidney and skin and is associated with adult-onset autosomal dominant demyelinating leukodystrophy and primary microcephaly.
- **Conclusion**: Established conclusion: LMNB1 anchors the module's RNA and chromatin program to nuclear structure. Hypothesis: coordinated LMNB1 abundance may influence how nuclear architecture constrains transcription and RNA processing in shared kidney and skin cell states.

## Module 3

**Tissue pair**: kidney and skin  
**Genes (34)**: ACLY, EIF3C, FASN, HDAC1, HSPH1, IMPDH2, MATR3, PSMC4, PSMC2, PFAS, ATIC, CAD, RPL3, RPL6, RPL9, RUVBL2, SF3A1, SF3B3, AARS1, EPRS1, IARS1, KARS1, LARS1, MARS1, RARS1, CCT5, CCT3, CCT7, CCT8, TNPO1, EFTUD2, USP5, XPO1, XRCC6

### Function

The module is best interpreted as a conserved intracellular protein-production and proteostasis program. The strongest primary evidence is the aminoacyl-tRNA synthetase multienzyme complex and aminoacyl-tRNA biosynthesis (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 6.48e-06), (10 globally significant GO/KEGG terms, q_global 0.000185–0.000261; see the table), together with translation and protein biosynthesis (GO:BP translation; q_global = 0.0143) (GO:BP protein biosynthetic process; q_global = 0.0143). A second coherent component is the CCT chaperonin complex (GO:CC chaperonin-containing T-complex; q_global = 8.84e-05), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.000595), (GO:CC protein folding chaperone complex; q_global = 0.00255), (GO:MF protein folding chaperone; q_global = 0.00617), with globally corrected terms linking CCT3, CCT5, CCT7, CCT8 and RUVBL2 to RNA and telomerase-RNA localization to Cajal bodies (4 globally significant GO/KEGG terms, q_global 8.9e-06–8.9e-06; see the table), (GO:BP regulation of telomerase RNA localization to Cajal body; q_global = 8.84e-05) (GO:BP positive regulation of telomerase RNA localization to Cajal body; q_global = 8.84e-05), (GO:BP regulation of protein localization to Cajal body; q_global = 0.000309) (GO:BP positive regulation of protein localization to Cajal body; q_global = 0.000309), (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 0.00243), (GO:BP positive regulation of telomere maintenance; q_global = 0.00893) (GO:BP regulation of telomere maintenance via telomerase; q_global = 0.0113), (GO:BP telomere maintenance; q_global = 0.02), (GO:BP telomere organization; q_global = 0.022), (GO:BP regulation of telomere maintenance; q_global = 0.0368), (GO:BP RNA-templated DNA biosynthetic process; q_global = 0.0379) (GO:BP telomere maintenance via telomerase; q_global = 0.0379) (GO:BP telomere maintenance via telomere lengthening; q_global = 0.0457). The module also contains ribosomal proteins, translation initiation, spliceosomal factors, proteasome ATPases, nucleotide-biosynthesis enzymes, nuclear transport factors and lipid-biosynthesis enzymes. Thus, the most defensible functional interpretation is coordinated translational capacity, folding of newly synthesized proteins, RNA processing and nuclear quality-control or maintenance functions. The Cajal-body and telomere annotations are biologically coherent but are concentrated in the CCT subgroup and should not be taken to mean that every module member directly regulates telomerase.

**Cell composition.** This is predominantly an intracellular, broadly expressed housekeeping-type module rather than a plasma-protein or secreted-protein module. HPA reports low tissue specificity for most genes, low immune-cell specificity for nearly all genes, and protein detection in both kidney and skin for most members. The module contains only a single gene annotated as secreted, so contamination by a plasma secretome is not the leading interpretation. HPA cell-type annotations do show enrichment in germ-cell, trophoblast, epithelial, neuronal and other specialized cell populations, and STRING supplementary tissue results include blood and lymphoid categories (STRING TISSUES Lymphoblast; within-query FDR = 1.44e-09), (STRING TISSUES Lymphocyte; within-query FDR = 1.44e-09), (STRING TISSUES Blood; within-query FDR = 2.41e-07), (STRING TISSUES Lymphoid tissue; within-query FDR = 2.82e-07), (STRING TISSUES Hematopoietic system; within-query FDR = 4.28e-06). These observations could reflect shared cellular composition or general proliferative and biosynthetic activity in the samples, but they do not support a primarily blood-cell-derived module. The HPA pattern is therefore more consistent with a ubiquitous intracellular program modulated by cell-type mixture than with a kidney- or skin-specific secreted program.

**GO/KEGG enrichment**: 70 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 6.48e-06 | EPRS1, IARS1, KARS1, LARS1, MARS1, RARS1 |
| GO:BP RNA localization to Cajal body | 8.9e-06 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP telomerase RNA localization to Cajal body | 8.9e-06 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP telomerase RNA localization | 8.9e-06 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP RNA localization to nucleus | 8.9e-06 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:MF ATP binding | 8.11e-05 | AARS1, ACLY, CAD, CCT3, CCT5, CCT7, CCT8, EPRS1, HSPH1, IARS1, KARS1, LARS1, MARS1, PFAS, PSMC2, PSMC4, RARS1, RUVBL2, XRCC6 |
| GO:MF adenyl ribonucleotide binding | 8.66e-05 | AARS1, ACLY, CAD, CCT3, CCT5, CCT7, CCT8, EPRS1, HSPH1, IARS1, KARS1, LARS1, MARS1, PFAS, PSMC2, PSMC4, RARS1, RUVBL2, XRCC6 |
| GO:CC chaperonin-containing T-complex | 8.84e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 8.84e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 8.84e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:MF aminoacyl-tRNA ligase activity | 0.000185 | AARS1, EPRS1, IARS1, KARS1, LARS1, MARS1, RARS1 |
| GO:BP tRNA aminoacylation for protein translation | 0.000185 | AARS1, EPRS1, IARS1, KARS1, LARS1, MARS1, RARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 0.000185 | AARS1, EPRS1, IARS1, KARS1, LARS1, MARS1, RARS1 |
| GO:CC intracellular protein-containing complex | 0.000189 | CCT3, CCT5, CCT7, CCT8, EPRS1, IARS1, KARS1, LARS1, MARS1, PSMC2, PSMC4, RARS1, RUVBL2, SF3B3, XRCC6 |
| GO:MF purine ribonucleoside triphosphate binding | 0.000203 | AARS1, ACLY, CAD, CCT3, CCT5, CCT7, CCT8, EFTUD2, EPRS1, HSPH1, IARS1, KARS1, LARS1, MARS1, PFAS, PSMC2, PSMC4, RARS1, RUVBL2, XRCC6 |

### STRING and hu.MAP

STRING provides strong prior support for several substructures. The aminoacyl-tRNA synthetases form a tightly connected group corresponding to the multisynthetase complex, also supported by (STRING COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex; within-query FDR = 4.27e-07) and (STRING RCTM Cytosolic tRNA aminoacylation; within-query FDR = 5.34e-06). CCT3, CCT5, CCT7 and CCT8 form a highly connected chaperonin cluster, with additional links to RUVBL2, ribosomal proteins and proteostasis factors. RPL3, RPL6 and RPL9 form a ribosomal subgroup; PSMC2 and PSMC4 form a proteasome-ATPase subgroup; SF3A1, SF3B3 and EFTUD2 support spliceosomal organization; and ACLY with FASN supports lipid biosynthesis. The hu.MAP results independently recover the aminoacyl-tRNA synthetase complex (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1) and several CCT-containing complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). They also support spliceosomal (hu.MAP huMAP3_08980.1), metabolic (hu.MAP huMAP3_03291.1) (hu.MAP huMAP3_00676.1) (hu.MAP huMAP3_10103.1), proteasomal (hu.MAP huMAP3_05064.1), chaperone (hu.MAP huMAP3_13774.1), nuclear transport (hu.MAP huMAP3_09592.1) and other assemblies. Consequently, much of the module reflects known molecular machinery rather than previously unknown pairwise biology. STRING and hu.MAP support biological coherence, but they do not by themselves establish that all relationships are direct physical interactions or that the entire module is one stable complex.

**STRING interactions (score >= 0.7)**: 66 of 561 gene pairs: AARS1–EPRS1 (0.976); AARS1–IARS1 (0.98); AARS1–KARS1 (0.992); AARS1–LARS1 (0.968); AARS1–MARS1 (0.913); AARS1–RARS1 (0.85); ACLY–FASN (0.994); ATIC–CCT7 (0.881); ATIC–IMPDH2 (0.991); ATIC–PFAS (0.819); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT3–RUVBL2 (0.766); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT5–RPL3 (0.731); CCT5–RPL6 (0.708); CCT5–RUVBL2 (0.705); CCT7–CCT8 (0.999); CCT7–EIF3C (0.728); CCT7–IMPDH2 (0.758); CCT7–RPL3 (0.8); CCT7–RPL6 (0.793); CCT7–RPL9 (0.723); CCT7–RUVBL2 (0.802); CCT8–PSMC2 (0.733); CCT8–RPL6 (0.78); CCT8–RPL9 (0.752); CCT8–RUVBL2 (0.776); EFTUD2–EPRS1 (0.744); EFTUD2–KARS1 (0.704); EFTUD2–RPL3 (0.837); EFTUD2–RPL6 (0.706); EFTUD2–RPL9 (0.864); EFTUD2–RUVBL2 (0.793); EFTUD2–SF3A1 (0.999); EFTUD2–SF3B3 (0.999); EIF3C–EPRS1 (0.755); EPRS1–IARS1 (0.999); EPRS1–KARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–MARS1 (0.999); EPRS1–RARS1 (0.999); EPRS1–RPL3 (0.855); EPRS1–RPL6 (0.711); EPRS1–RPL9 (0.832); HDAC1–RUVBL2 (0.946); IARS1–KARS1 (0.999); IARS1–LARS1 (0.999); IARS1–MARS1 (0.999); IARS1–RARS1 (0.999); KARS1–LARS1 (0.999); KARS1–MARS1 (0.999); KARS1–RARS1 (0.999); KARS1–RPL3 (0.705); LARS1–MARS1 (0.999); LARS1–RARS1 (0.999); MARS1–RARS1 (0.999); PSMC2–PSMC4 (0.999); PSMC2–RPL3 (0.705); RPL3–RPL6 (0.999); RPL3–RPL9 (0.999); RPL6–RPL9 (0.999); SF3A1–SF3B3 (0.999); TNPO1–XPO1 (0.868)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Liver (FDR = 1.21e-10, 29 genes); TISSUES Lymphoblast (FDR = 1.44e-09, 13 genes); TISSUES Lymphocyte (FDR = 1.44e-09, 17 genes); RCTM Selenoamino acid metabolism (FDR = 8.31e-08, 9 genes); TISSUES Blood (FDR = 2.41e-07, 21 genes); TISSUES Lymphoid tissue (FDR = 2.82e-07, 19 genes); COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex (FDR = 4.27e-07, 7 genes); COMPARTMENTS Cytosol (FDR = 4.73e-07, 29 genes); Function Organic cyclic compound binding (FDR = 7.59e-07, 32 genes); Function Heterocyclic compound binding (FDR = 7.59e-07, 32 genes); TISSUES Viscus (FDR = 8.76e-07, 32 genes); Keyword ATP-binding (FDR = 2.96e-06, 19 genes); RCTM Translation (FDR = 3.13e-06, 11 genes); TISSUES Hematopoietic system (FDR = 4.28e-06, 23 genes); RCTM Cytosolic tRNA aminoacylation (FDR = 5.34e-06, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, IARS1, RARS1, MARS1, KARS1, LARS1; 6/14); huMAP3_13688.1 (EPRS1, IARS1, RARS1, MARS1, KARS1, LARS1; 6/14); huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_08980.1 (EFTUD2, SF3B3, SF3A1; 3/97); huMAP3_03291.1 (PFAS, FASN; 2/3); huMAP3_00676.1 (PFAS, FASN; 2/4); huMAP3_10103.1 (CAD, FASN; 2/4); huMAP3_05064.1 (PSMC2, PSMC4; 2/31); huMAP3_13774.1 (PFAS, HSPH1; 2/33); huMAP3_04549.1 (SF3B3, SF3A1; 2/52); huMAP3_14442.1 (ATIC, AARS1; 2/57); huMAP3_09656.1 (PSMC2, PSMC4; 2/64); huMAP3_13725.1 (PSMC2, PSMC4; 2/69); huMAP3_06511.1 (SF3B3, SF3A1; 2/79); huMAP3_09592.1 (XPO1, TNPO1; 2/95)

### Novelty

The individual components and most internal relationships are established: aminoacyl-tRNA synthetase assembly, CCT chaperonin function, ribosomal translation, spliceosomal processing, proteasomal degradation and nucleotide or lipid biosynthesis are all represented by known annotations and complexes. The potentially new observation is their coordinated co-abundance as one conserved module shared by kidney and skin. The supplied resources do not identify an existing kidney-skin co-abundance module with this exact composition, but absence from STRING or hu.MAP would not prove novelty because those resources catalogue physical or functional knowledge rather than tissue-pair co-abundance patterns. I therefore regard this as a potentially novel cross-tissue systems-level association, not as a newly discovered molecular complex. Replication in independent kidney and skin cohorts, adjustment for cell composition, and comparison with previously published tissue coexpression modules would be required before calling it a new finding.

**Hypothesis.** Hypothesis: the module represents a shared cellular demand program in kidney and skin in which aminoacyl-tRNA synthetase activity sustains translation, CCT chaperonins fold newly synthesized proteins, ribosomal and initiation factors support protein production, and proteasome and RNA-processing components maintain quality control. RUVBL2, XRCC6 and the CCT subgroup may connect this biosynthetic state to nuclear RNA localization, telomere maintenance and DNA-repair-related functions, while ACLY and FASN may reflect accompanying metabolic support. The cross-tissue signal could arise because both tissues contain viable, metabolically active epithelial or stromal cells that require these functions, or because shared cell-type composition drives the co-abundance. This is a mechanistic model rather than proof of direct regulation among all members.

### Important genes

#### EPRS1

- **Related proteins** (co-abundance neighbors): MARS1 (0.86), LARS1 (0.86), IARS1 (0.80), CAD (0.80); STRING partners: AARS1 (0.976), EFTUD2 (0.744), EIF3C (0.755), IARS1 (0.999), KARS1 (0.999), LARS1 (0.999), MARS1 (0.999), RARS1 (0.999), RPL3 (0.855), RPL6 (0.711), RPL9 (0.832)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is a central member of the aminoacyl-tRNA synthetase cluster, has strong module connectivity to several synthetases and ribosomal proteins, belongs to the hu.MAP multisynthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), and is included in the primary aminoacylation and translation terms (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 6.48e-06), (10 globally significant GO/KEGG terms, q_global 0.000185–0.000261; see the table), (GO:BP translation; q_global = 0.0143) (GO:BP protein biosynthetic process; q_global = 0.0143). Its established function is charging glutamyl and prolyl tRNAs, and its literature and disease annotation provide substantial biological context.
- **Conclusion**: Established evidence supports EPRS1 as a core translational component and a strong anchor for the module's aminoacylation interpretation. It is plausible, but not demonstrated, that EPRS1 helps couple translational demand to the neighboring chaperone and ribosomal submodules.

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT7 (0.87), RPL3 (0.86), CCT3 (0.84), PSMC4 (0.83), CCT8 (0.83), HSPH1 (0.83); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999), RPL3 (0.731), RPL6 (0.708), RUVBL2 (0.705)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is a member of the tightly connected CCT3-CCT5-CCT7-CCT8 subgroup, participates in multiple hu.MAP CCT complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), and contributes to the globally corrected chaperone, Cajal-body and telomere-maintenance terms (9 globally significant GO/KEGG terms, q_global 8.9e-06–8.84e-05; see the table), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.000595), (6 globally significant GO/KEGG terms, q_global 0.00243–0.00617; see the table), (GO:BP positive regulation of telomere maintenance; q_global = 0.00893) (GO:BP regulation of telomere maintenance via telomerase; q_global = 0.0113), (GO:BP telomere maintenance; q_global = 0.02), (GO:BP telomere organization; q_global = 0.022), (GO:BP regulation of telomere maintenance; q_global = 0.0368), (GO:BP RNA-templated DNA biosynthetic process; q_global = 0.0379) (GO:BP telomere maintenance via telomerase; q_global = 0.0379) (GO:BP telomere maintenance via telomere lengthening; q_global = 0.0457). Its established function is ATP-dependent folding of proteins such as actin and tubulin. It has a substantial disease and literature record and is detected in both kidney and skin by HPA.
- **Conclusion**: Established evidence supports CCT5 as a core proteostasis and chaperonin marker of the module. The annotations make a role in RNA or telomere-related nuclear maintenance plausible, but the co-abundance data do not establish that CCT5 directly controls telomerase.

#### RPL3

- **Related proteins** (co-abundance neighbors): RPL6 (0.88), CCT5 (0.86), CCT3 (0.85), IARS1 (0.84), EIF3C (0.84), XRCC6 (0.83), RUVBL2 (0.83), ATIC (0.82), XPO1 (0.82), RARS1 (0.82), FASN (0.81), HDAC1 (0.81), EFTUD2 (0.80), KARS1 (0.80); STRING partners: CCT5 (0.731), CCT7 (0.8), EFTUD2 (0.837), EPRS1 (0.855), KARS1 (0.705), PSMC2 (0.705), RPL6 (0.999), RPL9 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Cytosol; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein L3. Ribosomes, the complexes that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L3P family of ribosomal proteins and it is located in the cytoplasm. The p…
- **Diseases (Open Targets)**: Duchenne muscular dystrophy (0.506); Orthomyxoviridae infectious disease (0.463); cystic fibrosis (0.389); neuromuscular disease caused by qualitative or quantitative defects of dystrophin (0.323); inflammatory bowel disease (0.308)
- **Europe PMC papers**: 2316
- **Why important**: RPL3 has the strongest network position in the supplied module ranking and connects the ribosomal subgroup to CCT proteins, synthetases, EIF3C, RUVBL2 and DNA-repair-associated components. It is part of the cytosolic large ribosomal subunit (GO:CC cytosolic large ribosomal subunit; q_global = 0.0212) and the primary translation and protein-biosynthesis terms (GO:BP protein metabolic process; q_global = 0.000353), (GO:BP translation; q_global = 0.0143) (GO:BP protein biosynthetic process; q_global = 0.0143). Its broad expression, detection in kidney and skin, and extensive literature make it a useful indicator of general translational capacity.
- **Conclusion**: Established evidence supports RPL3 as a structural translation component and network bridge rather than a tissue-specific regulator. Its central position may help explain module coherence, but it does not by itself demonstrate a specialized kidney-skin mechanism.

#### LARS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.88), EPRS1 (0.86), MARS1 (0.85), USP5 (0.82), RPL6 (0.80); STRING partners: AARS1 (0.968), EPRS1 (0.999), IARS1 (0.999), KARS1 (0.999), MARS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: leucyl-tRNA synthetase 1. This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals w…
- **Diseases (Open Targets)**: infantile liver failure syndrome 1 (0.670); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.510); Global developmental delay (0.119); sensorineural hearing loss disorder (0.119); Generalized-onset seizure (0.118)
- **Europe PMC papers**: 267
- **Why important**: LARS1 is a highly connected member of the multisynthetase complex, is recovered in hu.MAP complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), and contributes to the primary aminoacylation, tRNA-biosynthesis and translation evidence (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 6.48e-06), (10 globally significant GO/KEGG terms, q_global 0.000185–0.000261; see the table), (GO:MF catalytic activity, acting on a tRNA; q_global = 0.0138) (GO:BP translation; q_global = 0.0143) (GO:BP protein biosynthetic process; q_global = 0.0143). Its established enzyme activity charges tRNA with leucine and it is linked to infantile liver failure syndrome. Its position also links the synthetase cluster to USP5 and ribosomal proteins.
- **Conclusion**: Established evidence supports LARS1 as a core enzymatic component of the translational arm. Its disease association demonstrates biological importance, while any role in coordinating the broader module remains a hypothesis.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): CCT7 (0.83), RPL3 (0.83), CCT8 (0.82); STRING partners: CCT3 (0.766), CCT5 (0.705), CCT7 (0.802), CCT8 (0.776), EFTUD2 (0.793), HDAC1 (0.946)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 connects the CCT subgroup with RPL3 and has a strong STRING relationship with HDAC1, while contributing to primary terms for Cajal-body localization, chaperone complexes, telomere maintenance and nucleic-acid-associated functions (4 globally significant GO/KEGG terms, q_global 8.9e-06–8.9e-06; see the table), (GO:CC intracellular protein-containing complex; q_global = 0.000189), (GO:CC protein folding chaperone complex; q_global = 0.00255), (GO:BP positive regulation of telomere maintenance; q_global = 0.00893), (GO:BP telomere maintenance; q_global = 0.02), (GO:BP telomere organization; q_global = 0.022), (GO:MF unfolded protein binding; q_global = 0.029), (GO:BP regulation of telomere maintenance; q_global = 0.0368). Its established annotations include ATPase and DNA-helicase activity, DNA repair, recombination, snoRNP assembly and telomere maintenance. It is broadly detected and has a substantial disease and literature record.
- **Conclusion**: Established evidence supports RUVBL2 as a plausible bridge between proteostasis, RNA-related nuclear organization and genome maintenance. The module suggests coordinated activity across these processes, but does not establish that RUVBL2 mechanistically links the CCT and synthetase submodules in kidney or skin.

## Module 4

**Tissue pair**: kidney and skin  
**Genes (19)**: ACSL3, ATP2A2, ATL3, CANX, C5orf22, CENPV, CKAP4, DHFR, GALNT7, SHMT2, GPD2, HMOX2, ITGB1, ITGB3, NCSTN, PRKDC, SEC22B, TARS2, TRAP1

### Function

The strongest interpretation is a membrane and organelle-trafficking module centered on the endoplasmic reticulum and related organelle membranes. The primary evidence is enrichment for organelle membrane (GO:CC organelle membrane; q_global = 0.00348), melanosome (GO:CC melanosome; q_global = 0.00575), pigment granule (GO:CC pigment granule; q_global = 0.00575), endoplasmic reticulum membrane (GO:CC endoplasmic reticulum membrane; q_global = 0.0398), an endoplasmic reticulum subcompartment (GO:CC endoplasmic reticulum subcompartment; q_global = 0.0398), and the nuclear outer membrane–endoplasmic reticulum membrane network (GO:CC nuclear outer membrane-endoplasmic reticulum membrane network; q_global = 0.045). The melanosome and pigment-granule signals are driven by CANX, ITGB1, ITGB3, NCSTN, and SEC22B, whereas the endoplasmic-reticulum signals include ACSL3, ATL3, ATP2A2, CANX, CKAP4, HMOX2, NCSTN, and SEC22B. Functionally, the module combines protein folding and quality control, calcium handling, membrane organization, lipid metabolism, glycosylation, vesicle transport, adhesion, and cellular stress responses. The co-abundance graph is sparse but has convergence around CKAP4, GPD2, and NCSTN, with CANX linking several membrane and secretory components. Thus, the module is better viewed as a coordinated membrane-homeostasis and trafficking program than as a single linear pathway.

**Cell composition.** The module is not dominated by secreted proteins: HPA identifies only one secreted gene, and most genes are intracellular or membrane-associated. It is also not uniformly tissue-specific; most genes have low tissue specificity, and protein detection is broadly compatible with both kidney and skin. HPA nevertheless shows strong cell-type structure, including recurrent enrichment in neutrophils and additional signals in granulocytes, platelets, monocytes, mast cells, and other specialized cell types. ITGB3 is especially compatible with platelet and blood-cell biology, while several genes show neutrophil or progenitor enrichment. Therefore, the shared kidney–skin module may reflect a conserved epithelial or stromal membrane program, but a contribution from common immune, vascular, or blood-derived cell populations should be considered. The melanosome and pigment-granule evidence may also reflect pigment-cell or pigment-associated biology rather than a universal property of all kidney and skin cells.

**GO/KEGG enrichment**: 6 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC organelle membrane | 0.00348 | ACSL3, ATL3, ATP2A2, CANX, CENPV, CKAP4, GALNT7, GPD2, HMOX2, ITGB1, ITGB3, NCSTN, SEC22B, SHMT2, TRAP1 |
| GO:CC melanosome | 0.00575 | CANX, ITGB1, ITGB3, NCSTN, SEC22B |
| GO:CC pigment granule | 0.00575 | CANX, ITGB1, ITGB3, NCSTN, SEC22B |
| GO:CC endoplasmic reticulum membrane | 0.0398 | ACSL3, ATL3, ATP2A2, CANX, CKAP4, HMOX2, NCSTN, SEC22B |
| GO:CC endoplasmic reticulum subcompartment | 0.0398 | ACSL3, ATL3, ATP2A2, CANX, CKAP4, HMOX2, NCSTN, SEC22B |
| GO:CC nuclear outer membrane-endoplasmic reticulum membrane network | 0.045 | ACSL3, ATL3, ATP2A2, CANX, CKAP4, HMOX2, NCSTN, SEC22B |

### STRING and hu.MAP

STRING provides a small set of high-confidence relationships rather than a densely connected known interaction network. The strongest supported pairs include ITGB1–ITGB3, ATP2A2–CANX, CANX–NCSTN, CANX–SEC22B, and DHFR–SHMT2. These relationships support coherent substructures involving integrin adhesion, endoplasmic-reticulum calcium and folding biology, gamma-secretase-associated membrane biology, vesicle trafficking, and mitochondrial or folate-linked metabolism. STRING supplementary terms reinforce organelle membrane, endoplasmic-reticulum membrane, melanosome, membrane topology, phagosome, and adhesion-related interpretations, but they are not global enrichment evidence. hu.MAP contributes one partially overlapping, moderate-confidence complex containing ACSL3, ATP2A2, and PRKDC among many other proteins. This supports a possible broader membrane-associated complex context, but the limited overlap and confidence mean that it should not be treated as proof that the entire module is one physical complex. Overall, the network contains a mixture of established interactions and co-abundance links that may connect proteins through shared cell state or compartment rather than direct binding.

**STRING interactions (score >= 0.7)**: 5 of 171 gene pairs: ATP2A2–CANX (0.849); CANX–NCSTN (0.754); CANX–SEC22B (0.703); DHFR–SHMT2 (0.992); ITGB1–ITGB3 (0.987)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Organelle membrane (FDR = 0.00017, 14 genes); Component Organelle membrane (FDR = 0.00093, 15 genes); Component Integral component of synaptic membrane (FDR = 0.00093, 4 genes); Component Melanosome (FDR = 0.0011, 5 genes); Component Endoplasmic reticulum membrane (FDR = 0.0035, 8 genes); Component Integral component of membrane (FDR = 0.0047, 11 genes); Keyword Transmembrane helix (FDR = 0.0077, 10 genes); Component Integral component of plasma membrane (FDR = 0.0201, 5 genes); Component Bounding membrane of organelle (FDR = 0.0337, 9 genes); Component Secretory granule membrane (FDR = 0.042, 4 genes); KEGG Phagosome (FDR = 0.045, 4 genes); KEGG Hypertrophic cardiomyopathy (FDR = 0.045, 3 genes); KEGG Arrhythmogenic right ventricular cardiomyopathy (FDR = 0.045, 3 genes); KEGG Dilated cardiomyopathy (FDR = 0.045, 3 genes); Component Integral component of presynaptic membrane (FDR = 0.0458, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09592.1 (ACSL3, ATP2A2, PRKDC; 3/95)

### Novelty

This appears to be a potentially novel tissue-pair co-abundance module, but the evidence does not justify claiming a newly discovered molecular complex or pathway. The globally corrected enrichment establishes a reproducible shared compartmental signature, while the limited STRING connectivity and partial hu.MAP overlap indicate that much of the module is not represented as one established interaction unit in those resources. That pattern is compatible with a new cross-tissue co-abundance relationship assembled from known membrane, trafficking, metabolic, adhesion, and stress proteins. However, absence or weak representation in STRING or hu.MAP alone cannot establish novelty. A stronger novelty claim would require replication in independent kidney and skin cohorts, control for cell-type composition and blood contamination, comparison with published tissue co-expression modules, and experimental testing of the predicted coordinated regulation.

**Hypothesis.** Hypothesis: the module reflects a conserved membrane-homeostasis state shared by kidney and skin in which endoplasmic-reticulum architecture, calcium handling, glycoprotein folding, lipid activation, and ER-to-Golgi trafficking are coordinated with cell-surface adhesion and pigment- or granule-associated membrane organization. ATL3 and CKAP4 could help maintain the ER membrane framework, CANX and ATP2A2 could couple protein quality control to calcium balance, and SEC22B could connect the ER to vesicle transport. NCSTN may mark a membrane-proteolysis and receptor-processing component, while ITGB1 and ITGB3 may report adhesion or vascular, platelet, and immune-cell contributions. The observed module could therefore represent either a genuine conserved epithelial membrane program or a mixture of this program with shared immune and blood-associated cell states; separating these possibilities requires cell-resolved validation.

### Important genes

#### CANX

- **Related proteins** (co-abundance neighbors): GPD2 (0.84), NCSTN (0.81); STRING partners: ATP2A2 (0.849), NCSTN (0.754), SEC22B (0.703)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is a central connector of the membrane-related subnetwork and is linked by STRING to ATP2A2, NCSTN, and SEC22B. It is present in every primary compartmental term involving the endoplasmic reticulum and pigment-associated organelles (GO:CC organelle membrane; q_global = 0.00348), (GO:CC melanosome; q_global = 0.00575), (GO:CC pigment granule; q_global = 0.00575), (GO:CC endoplasmic reticulum membrane; q_global = 0.0398), (GO:CC endoplasmic reticulum subcompartment; q_global = 0.0398), (GO:CC nuclear outer membrane-endoplasmic reticulum membrane network; q_global = 0.045). Its established function as an endoplasmic-reticulum chaperone and quality-control factor provides a direct mechanistic bridge between protein folding, calcium-associated ER function, and vesicle biology. It also has substantial literature support and is detected in both kidney and skin by HPA.
- **Conclusion**: Established evidence supports CANX as a core ER quality-control and membrane-trafficking component of the module. It is a strong candidate for an organizing marker, but the co-abundance data do not establish that CANX directly regulates the other module genes.

#### NCSTN

- **Related proteins** (co-abundance neighbors): ACSL3 (0.82), CANX (0.81), GPD2 (0.81), CKAP4 (0.81); STRING partners: CANX (0.754)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nicastrin. This gene encodes a type I transmembrane glycoprotein that is an integral component of the multimeric gamma-secretase complex. The encoded protein cleaves integral membrane proteins, including Notch receptors and beta-amyloid precursor protein, and may be a stabilizing cofactor required for gamma-secretase complex assembly. The cleavage of beta-amyloid precursor protein yields amyloid beta peptide…
- **Diseases (Open Targets)**: acne inversa, familial, 1 (0.724); neurodegenerative disease (0.525); desmoid tumor (0.503); Alzheimer disease (0.406); hidradenitis suppurativa (0.389)
- **Europe PMC papers**: 2357
- **Why important**: NCSTN has high network connectivity and is the only module gene with a STRING relationship to CANX among the gamma-secretase-associated component candidates. It appears in all primary enrichment terms (GO:CC organelle membrane; q_global = 0.00348), (GO:CC melanosome; q_global = 0.00575), (GO:CC pigment granule; q_global = 0.00575), (GO:CC endoplasmic reticulum membrane; q_global = 0.0398), (GO:CC endoplasmic reticulum subcompartment; q_global = 0.0398), (GO:CC nuclear outer membrane-endoplasmic reticulum membrane network; q_global = 0.045) and across a broad range of supplementary membrane, ER, melanosome, secretory-granule, and synaptic-membrane terms. Its established role as an integral gamma-secretase component connects the module to membrane-protein processing and Notch-related biology. It also has substantial literature and disease-association support.
- **Conclusion**: Established evidence supports NCSTN as a membrane-proteolysis and organelle-membrane marker within the module. A role in coordinating the kidney–skin co-abundance state is plausible but remains a hypothesis because the data show association rather than regulatory causality.

#### CKAP4

- **Related proteins** (co-abundance neighbors): ITGB3 (0.83), HMOX2 (0.82), NCSTN (0.81), ITGB1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytoskeleton associated protein 4. Enables RNA binding activity. Located in several cellular components, including lipid droplet; nuclear speck; and rough endoplasmic reticulum. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: smoking initiation (0.357); arthropathy (0.216); asthma (0.200); adolescent idiopathic scoliosis (0.141); spinal cord injury (0.128)
- **Europe PMC papers**: 2103
- **Why important**: CKAP4 is one of the most connected genes in the module and links ITGB1, ITGB3, HMOX2, and NCSTN. It is represented in the organelle-membrane and ER primary terms (GO:CC organelle membrane; q_global = 0.00348), (GO:CC endoplasmic reticulum membrane; q_global = 0.0398), (GO:CC endoplasmic reticulum subcompartment; q_global = 0.0398), (GO:CC nuclear outer membrane-endoplasmic reticulum membrane network; q_global = 0.045), and HPA places it in the ER with detection in kidney and skin. Its established ER and membrane-associated biology makes it a useful candidate for coupling intracellular membrane organization with cell-surface adhesion. It also has a substantial literature base.
- **Conclusion**: Established evidence supports CKAP4 as a plausible structural bridge between ER-associated membrane biology and integrin-linked surface processes. The specific bridging role inferred from this module is a hypothesis requiring perturbation or spatial validation.

#### ATP2A2

- **Related proteins** (co-abundance neighbors): SHMT2 (0.83); STRING partners: CANX (0.849)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darie…
- **Diseases (Open Targets)**: Darier disease (0.823); acrokeratosis verruciformis (0.663); neurodegenerative disease (0.507); hereditary disease (0.416); schizophrenia (0.406)
- **Europe PMC papers**: 9327
- **Why important**: ATP2A2 is included in the primary organelle-membrane and ER terms (GO:CC organelle membrane; q_global = 0.00348), (GO:CC endoplasmic reticulum membrane; q_global = 0.0398), (GO:CC endoplasmic reticulum subcompartment; q_global = 0.0398), (GO:CC nuclear outer membrane-endoplasmic reticulum membrane network; q_global = 0.045) and has a high-confidence STRING relationship with CANX. Its established role as an ER or sarcoplasmic-reticulum calcium pump gives the module a direct calcium-homeostasis component. It is detected in kidney and skin, has strong disease evidence for Darier disease, and has a substantial literature base. Its HPA enrichment in muscle-associated tissues also provides a possible context for cell-type or tissue-state effects.
- **Conclusion**: Established evidence supports ATP2A2 as a functionally important calcium-handling component and a plausible link between ER physiology and tissue integrity. The module does not establish that altered ATP2A2 activity drives the shared kidney–skin pattern.

#### ITGB1

- **Related proteins** (co-abundance neighbors): ATL3 (0.87), CKAP4 (0.80); STRING partners: ITGB3 (0.987)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is part of the primary organelle-membrane and pigment-associated terms (GO:CC organelle membrane; q_global = 0.00348), (GO:CC melanosome; q_global = 0.00575), (GO:CC pigment granule; q_global = 0.00575), and has a very strong STRING relationship with ITGB3. Its established role in integrin-mediated adhesion, cell-matrix interactions, tissue repair, phagocytosis, and immune responses provides a surface-receptor counterpart to the intracellular membrane machinery. HPA places it at the plasma membrane and focal adhesions with detection in kidney and skin, and it has extensive literature and disease-association support.
- **Conclusion**: Established evidence supports ITGB1 as a cell-adhesion and membrane-signaling component that may connect the module to tissue architecture. Its presence may also reflect shared stromal, vascular, or immune cell composition, so a kidney–skin-specific mechanistic interpretation remains provisional.

#### SEC22B

- **Related proteins** (co-abundance neighbors): GPD2 (0.80); STRING partners: CANX (0.703)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC22 homolog B, vesicle trafficking protein. The protein encoded by this gene is a member of the SEC22 family of vesicle trafficking proteins. It seems to complex with SNARE and it is thought to play a role in the ER-Golgi protein trafficking. This protein has strong similarity to Mus musculus and Cricetulus griseus proteins.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: inflammatory bowel disease (0.285); luminal A breast carcinoma (0.271); colitis (0.238); enteritis (0.238); Crohn disease (0.233)
- **Europe PMC papers**: 1006
- **Why important**: SEC22B is present in every primary enrichment term (GO:CC organelle membrane; q_global = 0.00348), (GO:CC melanosome; q_global = 0.00575), (GO:CC pigment granule; q_global = 0.00575), (GO:CC endoplasmic reticulum membrane; q_global = 0.0398), (GO:CC endoplasmic reticulum subcompartment; q_global = 0.0398), (GO:CC nuclear outer membrane-endoplasmic reticulum membrane network; q_global = 0.045), and STRING links it to CANX. Its established function in ER-to-Golgi and retrograde vesicle trafficking provides a direct transport mechanism consistent with the module's compartmental signature. HPA reports neutrophil cell-type enhancement and no secreted classification, making it relevant both to intracellular trafficking and to the possibility of immune-cell contributions. It has a meaningful literature base and disease associations involving inflammatory intestinal disorders.
- **Conclusion**: Established evidence supports SEC22B as a vesicle-trafficking component that strengthens the ER and secretory-pathway interpretation. Its neutrophil-associated expression means that immune-cell composition remains an important alternative explanation for part of the shared signal.

## Module 5

**Tissue pair**: kidney and skin  
**Genes (47)**: ADNP, ACTR5, ATXN2L, BCL9L, BRD8, DCAF13, DCAF7, ECD, SIRAL1, GNA13, GOPC, IPO11, KATNAL1, KIF2C, LTN1, RNGTT, MCM2, MCM4, MCM6, MCM7, MKLN1, MSH2, MSH6, PPP1R12A, NAA25, NRDC, NUP188, NUP214, NUP93, NVL, ORC2, PRRC2C, GINS2, PUM1, RBM10, RBM7, SEH1L, SGTB, SMC2, SMARCAD1, SNIP1, SRPK1, STK26, STRBP, THOP1, USP28, ZFR

### Function

The module is best interpreted as a nuclear DNA-replication and genome-maintenance program. The primary evidence is the coordinated presence of the MCM and GINS2 core in the CMG complex, the DNA-replication preinitiation complex, the MCM complex, and replication-initiation processes (GO:CC CMG complex; q_global = 0.000367), (GO:CC DNA replication preinitiation complex; q_global = 0.000636), (GO:CC MCM complex; q_global = 0.000894), (GO:BP regulation of DNA-templated DNA replication initiation; q_global = 0.0112), (GO:BP DNA replication initiation; q_global = 0.0187). The same core is associated with helicase activities and with double-strand-break repair via break-induced replication (GO:BP double-strand break repair via break-induced replication; q_global = 9.22e-05), (GO:MF four-way junction helicase activity; q_global = 0.0152), (GO:MF forked DNA-dependent helicase activity; q_global = 0.0152), (GO:MF double-stranded DNA helicase activity; q_global = 0.0187), (GO:MF 3'-5' DNA helicase activity; q_global = 0.0187), (GO:MF single-stranded 3'-5' DNA helicase activity; q_global = 0.0187), (GO:MF single-stranded DNA helicase activity; q_global = 0.0382). Additional module members support a broader genome-integrity interpretation through DNA recombination, double-strand-break repair, mismatch repair, chromatin remodeling, chromosome organization, and cell-cycle annotations (GO:BP DNA recombination; q_global = 0.00176), (GO:MF single-stranded DNA binding; q_global = 0.0111), (GO:BP cell cycle; q_global = 0.0128), (GO:BP double-strand break repair; q_global = 0.0137), (GO:MF ATP-dependent activity, acting on DNA; q_global = 0.0139), (GO:CC chromosome; q_global = 0.0149), (GO:BP regulation of DNA metabolic process; q_global = 0.0343). The nuclear-chromosome and nuclear-complex terms (GO:CC nuclear chromosome; q_global = 0.000888), (GO:CC nuclear protein-containing complex; q_global = 0.0109) reinforce that this is a coordinated nuclear machinery signal rather than a generic tissue-expression signature. STRING results are consistent with this interpretation, but are supplementary rather than globally corrected enrichment evidence.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes, and most proteins are detected in both kidney and skin. The composition is largely intracellular and broadly expressed, with many genes showing low tissue specificity and nuclear or nucleoplasmic localization. The HPA pattern nevertheless points toward proliferative or hematopoietic contributions: enriched tissue and cell-type annotations repeatedly include bone marrow, lymphoid tissue, neutrophils, neutrophil progenitors, erythrocyte progenitors, and related progenitor populations. This does not establish blood contamination, but it makes shared blood cells, resident immune cells, or proliferating cells plausible contributors to the kidney-skin co-abundance pattern. The module should therefore not be interpreted as a kidney-specific or skin-specific program without cell-composition adjustment.

**GO/KEGG enrichment**: 22 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP double-strand break repair via break-induced replication | 9.22e-05 | GINS2, MCM2, MCM4, MCM6, MCM7 |
| GO:CC CMG complex | 0.000367 | GINS2, MCM2, MCM4, MCM6, MCM7 |
| GO:CC DNA replication preinitiation complex | 0.000636 | GINS2, MCM2, MCM4, MCM6, MCM7 |
| GO:CC nuclear chromosome | 0.000888 | ACTR5, BRD8, GINS2, MCM2, MCM4, MCM6, MCM7, ORC2, SMARCAD1, SMC2 |
| GO:CC MCM complex | 0.000894 | MCM2, MCM4, MCM6, MCM7 |
| GO:BP DNA recombination | 0.00176 | ACTR5, BRD8, GINS2, MCM2, MCM4, MCM6, MCM7, MSH2, MSH6, SMARCAD1 |
| GO:CC nuclear protein-containing complex | 0.0109 | ACTR5, ADNP, BCL9L, BRD8, DCAF13, GINS2, MCM2, MCM4, MCM6, MCM7, MSH2, MSH6, NUP188, NUP214, NUP93, NVL, ORC2, SEH1L, SNIP1 |
| GO:MF single-stranded DNA binding | 0.0111 | MCM2, MCM4, MCM6, MCM7, MSH2, SMC2 |
| GO:BP regulation of DNA-templated DNA replication initiation | 0.0112 | MCM2, MCM4, MCM6, MCM7 |
| GO:BP cell cycle | 0.0128 | ACTR5, BRD8, DCAF13, ECD, KIF2C, MCM2, MCM4, MCM6, MSH2, MSH6, NUP214, PPP1R12A, PUM1, RBM7, SEH1L, SMARCAD1, SMC2, SRPK1, USP28 |
| GO:BP double-strand break repair | 0.0137 | ACTR5, BRD8, GINS2, MCM2, MCM4, MCM6, MCM7, MSH2, SMARCAD1 |
| GO:MF ATP-dependent activity, acting on DNA | 0.0139 | MCM2, MCM4, MCM6, MCM7, MSH2, MSH6, SMARCAD1 |
| GO:CC chromosome | 0.0149 | ACTR5, ADNP, BRD8, GINS2, KIF2C, MCM2, MCM4, MCM6, MCM7, MSH2, MSH6, ORC2, PPP1R12A, SEH1L, SMARCAD1, SMC2, SRPK1, ZFR |
| GO:MF four-way junction helicase activity | 0.0152 | MCM2, MCM4, MCM6, MCM7, SMARCAD1 |
| GO:MF forked DNA-dependent helicase activity | 0.0152 | MCM2, MCM4, MCM6, MCM7, SMARCAD1 |

### STRING and hu.MAP

STRING provides strong, internally coherent support for a replication complex: GINS2 is linked to MCM2, MCM4, MCM6, and MCM7, while those MCM proteins are linked to ORC2 and to one another (STRING Component CMG complex; within-query FDR = 0.00048), (STRING NetworkNeighborAL Activation of the pre-replicative complex, and GINS complex; within-query FDR = 0.00057), (STRING Component MCM complex; within-query FDR = 0.00097), (STRING RCTM Unwinding of DNA; within-query FDR = 0.0014). A second established interaction group contains MSH2 and MSH6, with links from the mismatch-repair pair to MCM proteins and SMARCAD1. Other recognizable subnetworks include the nuclear-pore group NUP188, NUP214, NUP93, and SEH1L, the ACTR5-BRD8 pair, and the DCAF13-DCAF7 pair. hu.MAP independently recovers repeated CMG or replisome-related complexes containing the MCM and GINS2 genes (hu.MAP huMAP3_14758.1), (hu.MAP huMAP3_08554.1), (hu.MAP huMAP3_11832.1), (hu.MAP huMAP3_12180.1), (hu.MAP huMAP3_11119.1), (hu.MAP huMAP3_09238.1), together with additional complexes involving chromatin, nuclear-pore, RNA-binding, and other cellular machinery. Thus, part of the module reflects already known physical or functional complexes, especially the replication core. The remaining co-abundance links are more heterogeneous and should not automatically be treated as direct physical interactions.

**STRING interactions (score >= 0.7)**: 30 of 1081 gene pairs: ACTR5–BRD8 (0.901); DCAF13–DCAF7 (0.9); GINS2–MCM2 (0.998); GINS2–MCM4 (0.999); GINS2–MCM6 (0.998); GINS2–MCM7 (0.999); MCM2–MCM4 (0.999); MCM2–MCM6 (0.999); MCM2–MCM7 (0.999); MCM2–ORC2 (0.999); MCM4–MCM6 (0.999); MCM4–MCM7 (0.999); MCM4–MSH6 (0.735); MCM4–ORC2 (0.988); MCM4–SMC2 (0.748); MCM6–MCM7 (0.999); MCM6–MSH6 (0.802); MCM6–ORC2 (0.986); MCM6–SMC2 (0.75); MCM7–MSH2 (0.71); MCM7–ORC2 (0.997); MCM7–SMC2 (0.7); MSH2–MSH6 (0.999); MSH2–SMARCAD1 (0.944); NUP188–NUP214 (0.992); NUP188–NUP93 (0.999); NUP188–SEH1L (0.991); NUP214–NUP93 (0.999); NUP214–SEH1L (0.998); NUP93–SEH1L (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Nucleus (FDR = 0.00028, 34 genes); Component Nuclear chromosome (FDR = 0.00041, 10 genes); Component Chromosome (FDR = 0.00048, 18 genes); Component CMG complex (FDR = 0.00048, 5 genes); NetworkNeighborAL Activation of the pre-replicative complex, and GINS complex (FDR = 0.00057, 6 genes); Component MCM complex (FDR = 0.00097, 4 genes); COMPARTMENTS Nuclear chromosome (FDR = 0.001, 10 genes); COMPARTMENTS Nuclear lumen (FDR = 0.001, 23 genes); COMPARTMENTS CMG complex (FDR = 0.001, 5 genes); COMPARTMENTS Nucleus (FDR = 0.0011, 34 genes); COMPARTMENTS MCM complex (FDR = 0.0011, 4 genes); RCTM Unwinding of DNA (FDR = 0.0014, 5 genes); Component Nuclear protein-containing complex (FDR = 0.0021, 18 genes); Process Double-strand break repair via break-induced replication (FDR = 0.0024, 5 genes); RCTM Cell Cycle, Mitotic (FDR = 0.0028, 13 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14758.1 (MCM4, MCM7, MCM2, MCM6, GINS2; 5/14); huMAP3_08554.1 (MCM4, MCM7, MCM2, MCM6, GINS2; 5/15); huMAP3_11832.1 (MCM4, MCM7, MCM2, MCM6, GINS2; 5/15); huMAP3_12180.1 (MCM4, MCM7, MCM2, MCM6, GINS2; 5/17); huMAP3_06061.1 (MCM4, MCM7, MCM2, MCM6; 4/5); huMAP3_05529.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_07113.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_11119.1 (MCM4, MCM7, MCM6, GINS2; 4/14); huMAP3_14306.1 (MCM4, MCM2, MCM6, BRD8; 4/55); huMAP3_09860.1 (MCM4, MCM2, MCM6; 3/4); huMAP3_00154.1 (MCM4, MCM2, MCM6; 3/5); huMAP3_09466.1 (MCM4, MCM2, MCM6; 3/23); huMAP3_10862.1 (MCM4, MCM2, MCM6; 3/33); huMAP3_10625.1 (PUM1, ZFR, STRBP; 3/57); huMAP3_02602.1 (MCM4, MCM6; 2/2); huMAP3_11693.1 (ATXN2L, KATNAL1; 2/8); huMAP3_13164.1 (PUM1, ATXN2L; 2/10); huMAP3_07492.1 (NUP188, SEH1L; 2/10); huMAP3_08489.1 (NUP188, SEH1L; 2/10); huMAP3_09238.1 (MCM7, GINS2; 2/11); huMAP3_05673.1 (NUP188, NUP93; 2/11); huMAP3_09707.1 (THOP1, ADNP; 2/12); huMAP3_09710.1 (NUP188, SEH1L; 2/13); huMAP3_08848.1 (MCM4, MCM6; 2/15); huMAP3_07115.1 (PUM1, ZFR; 2/15); huMAP3_09223.1 (PUM1, ZFR; 2/15); huMAP3_09042.1 (MSH6, NUP93; 2/26); huMAP3_11084.1 (MSH2, SIRAL1; 2/27); huMAP3_09825.1 (NUP188, SEH1L; 2/27); huMAP3_12581.1 (NUP214, SEH1L; 2/58); huMAP3_06589.1 (ZFR, STRBP; 2/79)

### Novelty

The module is unlikely to represent a newly discovered replication or DNA-repair mechanism: the MCM-GINS2 machinery, mismatch-repair pair, nuclear-pore components, and several associated functions are already well established by GO, STRING, hu.MAP, and the literature. What may be novel is the reproducible co-abundance organization of these known components in a conserved kidney-skin module, particularly the way a replication core is accompanied by repair, chromatin, nuclear-transport, RNA-processing, and cell-cycle genes. That claim remains provisional because co-abundance can arise from shared cell states, proliferation, or cell mixture. The absence of hu.MAP or STRING support for some peripheral genes does not demonstrate novelty; it may instead reflect incomplete interaction coverage, indirect regulation, or tissue-specific co-expression. A stronger novelty claim would require replication in independent cohorts, cell-type-resolved data, and comparison with previously reported tissue modules.

**Hypothesis.** Hypothesis: this conserved kidney-skin module reflects a shared proliferative genome-maintenance state in which the MCM-GINS2 helicase machinery licenses and supports replication, while MSH2-MSH6, SMARCAD1, ACTR5-BRD8, and chromosome-associated proteins help protect, repair, and reorganize replicating chromatin. Nuclear-pore and RNA-processing members may coordinate transport and gene-expression demands of that state. The hematopoietic and progenitor-heavy HPA pattern raises the alternative hypothesis that the signal is partly driven by shared immune or blood-cell content rather than by mature kidney and skin parenchymal cells. These alternatives should be tested by cell-type deconvolution, proliferation-state adjustment, and perturbation or replication-fork assays.

### Important genes

#### MCM6

- **Related proteins** (co-abundance neighbors): MCM4 (0.89), MCM2 (0.88), NVL (0.84), MKLN1 (0.83), MSH2 (0.83), KATNAL1 (0.82); STRING partners: GINS2 (0.998), MCM2 (0.999), MCM4 (0.999), MCM7 (0.999), MSH6 (0.802), ORC2 (0.986), SMC2 (0.75)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_14306.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 6. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: lactose intolerance (0.246); neurodegenerative disease (0.225); obesity disorder (0.166); nervous system disorder (0.141); systemic lupus erythematosus (0.140)
- **Europe PMC papers**: 3766
- **Why important**: MCM6 is a core member of the MCM helicase and CMG assemblies, appears across the full set of primary replication, helicase, chromosome, cell-cycle, and DNA-repair annotations (GO:BP double-strand break repair via break-induced replication; q_global = 9.22e-05) through (GO:MF single-stranded DNA helicase activity; q_global = 0.0382), and has connections to the other MCM proteins, GINS2, ORC2, MSH6, and SMC2 in STRING. It has substantial literature support and is detected in kidney and skin, while its HPA annotations also connect it to lymphoid and hematopoietic progenitor states. Its module position and broad annotation coverage make it a strong representative of the module's principal biological axis.
- **Conclusion**: Established: MCM6 is a replication-initiation and helicase-complex component, and its associations with DNA replication and repair are strongly supported (GO:BP double-strand break repair via break-induced replication; q_global = 9.22e-05), (GO:CC CMG complex; q_global = 0.000367), (GO:CC DNA replication preinitiation complex; q_global = 0.000636), (GO:CC MCM complex; q_global = 0.000894), (GO:BP regulation of DNA-templated DNA replication initiation; q_global = 0.0112), (GO:BP DNA replication initiation; q_global = 0.0187), (GO:MF double-stranded DNA helicase activity; q_global = 0.0187), (GO:MF 3'-5' DNA helicase activity; q_global = 0.0187), (GO:MF single-stranded 3'-5' DNA helicase activity; q_global = 0.0187), (GO:MF single-stranded DNA helicase activity; q_global = 0.0382). Hypothesis: its co-abundance in kidney and skin marks a shared replication-capable or progenitor-like cell state.

#### MCM2

- **Related proteins** (co-abundance neighbors): MCM6 (0.88), MCM7 (0.84); STRING partners: GINS2 (0.998), MCM4 (0.999), MCM6 (0.999), MCM7 (0.999), ORC2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14306.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a canonical MCM-complex component and a highly connected member of the STRING replication core, linking with GINS2, MCM4, MCM6, MCM7, and ORC2. It contributes to every primary MCM and replication-initiation signal and is also implicated in break-induced replication and broader DNA repair (GO:BP double-strand break repair via break-induced replication; q_global = 9.22e-05), (GO:CC CMG complex; q_global = 0.000367), (GO:CC DNA replication preinitiation complex; q_global = 0.000636), (GO:CC MCM complex; q_global = 0.000894), (GO:BP regulation of DNA-templated DNA replication initiation; q_global = 0.0112), (GO:BP double-strand break repair; q_global = 0.0137), (GO:BP DNA replication initiation; q_global = 0.0187). Its extensive literature base and disease associations, including hearing-related disorders, make it an informative marker of replication competence and genome stability.
- **Conclusion**: Established: MCM2 participates in the conserved pre-replication and replication-fork machinery represented by this module. Hypothesis: variation in the MCM2-associated signal could report differences in proliferative demand or replication stress between the contributing kidney and skin cell populations.

#### MCM4

- **Related proteins** (co-abundance neighbors): MCM6 (0.89), MCM7 (0.82); STRING partners: GINS2 (0.999), MCM2 (0.999), MCM6 (0.999), MCM7 (0.999), MSH6 (0.735), ORC2 (0.988), SMC2 (0.748)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_14306.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 4. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication rel…
- **Diseases (Open Targets)**: primary immunodeficiency with natural-killer cell deficiency and adrenal insufficiency (0.714); X-linked adrenal hypoplasia congenita (0.185); lung adenocarcinoma (0.112); microcephaly (0.111); neoplasm (0.102)
- **Europe PMC papers**: 4082
- **Why important**: MCM4 is part of the same experimentally supported MCM-GINS2 core and connects in STRING to the MCM proteins, GINS2, ORC2, MSH6, and SMC2. It is present throughout the primary replication and helicase annotations (GO:BP double-strand break repair via break-induced replication; q_global = 9.22e-05) through (GO:MF single-stranded DNA helicase activity; q_global = 0.0382) and has established links to replication initiation, strand elongation, and DNA repair. Its disease associations include immunodeficiency with adrenal insufficiency, giving it additional relevance to tissue and immune-cell interpretation.
- **Conclusion**: Established: MCM4 is a central enzymatic-complex component of DNA replication and a plausible contributor to the repair-associated module signal. Hypothesis: the MCM4 signal may couple replication activity with tissue or immune progenitor renewal in the shared module.

#### MCM7

- **Related proteins** (co-abundance neighbors): MCM2 (0.84), MCM4 (0.82); STRING partners: GINS2 (0.999), MCM2 (0.999), MCM4 (0.999), MCM6 (0.999), MSH2 (0.71), ORC2 (0.997), SMC2 (0.7)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 completes the recurring MCM-GINS2 replication core and has strong STRING links to GINS2, MCM2, MCM4, MCM6, and ORC2, with additional links to MSH2 and SMC2. It contributes to nearly all primary replication and helicase terms, including break-induced replication (GO:BP double-strand break repair via break-induced replication; q_global = 9.22e-05), (GO:CC CMG complex; q_global = 0.000367), (GO:CC DNA replication preinitiation complex; q_global = 0.000636), (GO:CC MCM complex; q_global = 0.000894), (GO:BP regulation of DNA-templated DNA replication initiation; q_global = 0.0112), (GO:BP double-strand break repair; q_global = 0.0137), (GO:MF four-way junction helicase activity; q_global = 0.0152), (GO:MF forked DNA-dependent helicase activity; q_global = 0.0152), (GO:BP DNA replication initiation; q_global = 0.0187), (GO:MF double-stranded DNA helicase activity; q_global = 0.0187), (GO:MF 3'-5' DNA helicase activity; q_global = 0.0187), (GO:MF single-stranded 3'-5' DNA helicase activity; q_global = 0.0187), (GO:BP regulation of DNA-templated DNA replication; q_global = 0.0321), (GO:MF single-stranded DNA helicase activity; q_global = 0.0382). Its substantial literature volume and associations with replication-linked developmental and neurological syndromes support its value as a biologically interpretable core gene.
- **Conclusion**: Established: MCM7 is part of the conserved replicative helicase machinery captured by this module. Hypothesis: coordinated MCM7 abundance may reflect the amount of licensed replication machinery in shared proliferating or progenitor cells.

#### SMARCAD1

- **Related proteins** (co-abundance neighbors): ORC2 (0.88), DCAF13 (0.85), NVL (0.84), GINS2 (0.82), MKLN1 (0.81); STRING partners: MSH2 (0.944)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SNF2 related chromatin remodeling ATPase with DExD box 1. This gene encodes a member of the SNF subfamily of helicase proteins. The encoded protein plays a critical role in the restoration of heterochromatin organization and propagation of epigenetic patterns following DNA replication by mediating histone H3/H4 deacetylation. Mutations in this gene are associated with adermatoglyphia. Alternatively spliced transcript variants encoding multiple isoforms h…
- **Diseases (Open Targets)**: palmoplantar keratoderma-sclerodactyly syndrome (0.600); absence of fingerprints-congenital milia syndrome (0.580); Adermatoglyphia (0.568); type 2 diabetes mellitus (0.396); isolated congenital adermatoglyphia (0.373)
- **Europe PMC papers**: 708
- **Why important**: SMARCAD1 connects the replication core to chromatin and repair biology. It is linked to MSH2 in STRING, is connected within the module to ORC2, NVL, GINS2, DCAF13, and MKLN1, and contributes to double-strand-break repair, DNA recombination, ATP-dependent DNA activity, helicase-related terms, chromatin organization, and heterochromatin formation (GO:CC nuclear chromosome; q_global = 0.000888), (GO:BP DNA recombination; q_global = 0.00176), (GO:BP double-strand break repair; q_global = 0.0137), (GO:MF ATP-dependent activity, acting on DNA; q_global = 0.0139), (GO:MF four-way junction helicase activity; q_global = 0.0152), (GO:MF forked DNA-dependent helicase activity; q_global = 0.0152), (GO:MF double-stranded DNA helicase activity; q_global = 0.0187), (GO:MF 3'-5' DNA helicase activity; q_global = 0.0187), (GO:MF single-stranded 3'-5' DNA helicase activity; q_global = 0.0187), (GO:BP regulation of DNA metabolic process; q_global = 0.0343), (GO:MF single-stranded DNA helicase activity; q_global = 0.0382). Its established role in restoring heterochromatin after replication and its association with adermatoglyphia are especially relevant to a skin-containing tissue pair.
- **Conclusion**: Established: SMARCAD1 provides a plausible chromatin-remodeling and repair component that complements the MCM-GINS2 replication core. Hypothesis: SMARCAD1 may help couple replication completion to chromatin restoration in shared kidney and skin cell states, although the co-abundance data do not establish direct regulation.

## Module 6

**Tissue pair**: kidney and skin  
**Genes (33)**: AFDN, ALG2, DSG2, EP300, EPHA2, EXOC1, EXOC8, GRSF1, INTS4, INTS9, MLST8, MGME1, PHACTR4, PHF3, PHF6, PPM1B, RAB23, RCC1L, RCL1, RHOG, RIF1, MRPS12, SCAF8, SIN3A, THYN1, TM9SF4, TRMT5, TRUB1, TTC19, UBA5, UNK, UTP6, VPS18

### Function

No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The gene composition nevertheless points to a heterogeneous cellular-maintenance program rather than a single established pathway. Relevant established functions include RNA processing and ribosome biogenesis through INTS4, INTS9, RCL1 and UTP6; mitochondrial RNA, translation and genome-maintenance functions through TRMT5, MRPS12, GRSF1, MGME1 and TTC19; vesicle trafficking and exocytosis through EXOC1, EXOC8, VPS18, RAB23 and TM9SF4; cell junction, adhesion and cytoskeletal signaling through DSG2, AFDN, EPHA2, RHOG and PHACTR4; and transcriptional or chromatin regulation through EP300, SIN3A, PHF3, PHF6 and SCAF8. These annotations support a broad cellular homeostasis interpretation, but they do not establish one unified biological process. There were no supplementary STRING functional-enrichment terms either, so the interpretation should remain provisional.

**Cell composition.** The module is not composed mainly of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and protein detection is reported in both kidney and skin for nearly all genes with available data. The module is therefore compatible with broadly expressed intracellular housekeeping or maintenance biology rather than a kidney-specific or skin-specific secretory program. The HPA cell-type signals are diverse, including neutrophil-associated, epithelial, reproductive, muscle and other cell types. Most genes have low immune-cell specificity, with only a small subset showing immune enrichment or enhancement. Thus, blood contamination or a shared blood-cell population is not the leading explanation, although sample cellular composition could still contribute to the co-abundance pattern. The epithelial signals for DSG2 and EPHA2, and the kidney and skin protein detection, are consistent with a shared epithelial or tissue-structural component.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a sparse but informative set of high-confidence relationships. The EXOC1–EXOC8 relationship supports a known exocyst connection, while INTS4–INTS9 supports a known Integrator-complex connection. RCL1–UTP6 supports a known ribosome-biogenesis relationship, and MRPS12–UTP6 links mitochondrial translation biology with the nucleolar RNA-processing neighborhood. EP300–SIN3A supports a known transcriptional-regulatory relationship, and EPHA2–RHOG supports a signaling connection involving the plasma membrane and cytoskeletal regulation. The hu.MAP results independently reinforce the EXOC1–EXOC8 and INTS4–INTS9 pairings across several complexes, with additional complex membership outside the module. These findings show that parts of the module contain established molecular machinery, but most module genes lack a reported STRING or hu.MAP relationship within the supplied evidence. Accordingly, the network is not evidence that all genes form one physical complex; it is more consistent with several connected functional neighborhoods embedded in a co-abundance module.

**STRING interactions (score >= 0.7)**: 6 of 528 gene pairs: EP300–SIN3A (0.816); EPHA2–RHOG (0.732); EXOC1–EXOC8 (0.999); INTS4–INTS9 (0.999); MRPS12–UTP6 (0.823); RCL1–UTP6 (0.998)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08985.1 (INTS4, INTS9; 2/4); huMAP3_09363.1 (INTS4, INTS9; 2/6); huMAP3_09230.1 (INTS4, INTS9; 2/9); huMAP3_04054.1 (EXOC8, EXOC1; 2/10); huMAP3_07009.1 (EXOC8, EXOC1; 2/10); huMAP3_10641.1 (INTS4, INTS9; 2/11); huMAP3_09839.1 (EXOC8, EXOC1; 2/12); huMAP3_15286.1 (INTS4, INTS9; 2/12); huMAP3_12587.1 (EXOC8, EXOC1; 2/14); huMAP3_12564.1 (INTS4, INTS9; 2/14); huMAP3_13510.1 (INTS4, INTS9; 2/85)

### Novelty

This module should not be called a wholly new molecular complex or a newly discovered pathway. Several of its strongest relationships are already known through STRING or hu.MAP, especially the Integrator, exocyst, ribosome-biogenesis, transcriptional-regulatory and EPHA2–RHOG connections. The potentially novel observation is the coordinated co-abundance of these otherwise distinct cellular systems across kidney and skin. However, absence of a relationship from STRING or hu.MAP does not prove novelty, because those resources are incomplete and the module was defined by abundance correlation rather than direct physical interaction. A defensible conclusion is that the cross-tissue co-abundance pattern may be a new systems-level observation, but its novelty requires replication in independent cohorts, control for cell composition, and comparison with published kidney–skin co-expression modules.

**Hypothesis.** Hypothesis: the conserved kidney–skin module reflects a shared intracellular state in epithelial or tissue-resident cells that coordinates RNA maturation and translation capacity with vesicle delivery, cell-junction maintenance, cytoskeletal signaling and stress-responsive transcription. In this model, Integrator and ribosome-biogenesis components support gene-expression output, EXOC1 and EXOC8 support membrane delivery, DSG2, AFDN, EPHA2 and RHOG support tissue architecture and signaling, and EP300 with SIN3A modulates transcriptional adaptation. The mitochondrial genes may indicate an accompanying requirement for organelle quality and energy production. This is a mechanistic hypothesis, not an enrichment result: the absence of globally significant GO or KEGG terms means that the proposed coordination must be tested experimentally and statistically rather than treated as established module function.

### Important genes

#### EP300

- **Related proteins** (co-abundance neighbors): UBA5 (0.82), SIN3A (0.80), PHF6 (0.80); STRING partners: SIN3A (0.816)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EP300 lysine acetyltransferase. This gene encodes the adenovirus E1A-associated cellular p300 transcriptional co-activator protein. It functions as histone acetyltransferase that regulates transcription via chromatin remodeling and is important in the processes of cell proliferation and differentiation. It mediates cAMP-gene regulation by binding specifically to phosphorylated CREB protein. This gene has also been identified as …
- **Diseases (Open Targets)**: Rubinstein-Taybi syndrome due to EP300 haploinsufficiency (0.797); Menke-Hennekam syndrome 2 (0.677); cancer (0.601); Rubinstein-Taybi syndrome (0.585); hereditary disease (0.551)
- **Europe PMC papers**: 17204
- **Why important**: EP300 is a transcriptional co-activator and lysine acetyltransferase with a central regulatory role in chromatin, differentiation, proliferation and hypoxia responses. It connects in the module to SIN3A, UBA5 and PHF6, and its STRING relationship with SIN3A is high-confidence. It has strong disease and literature support, including established association with Rubinstein-Taybi syndrome and cancer-related biology. Its HPA profile is broadly expressed with enrichment in neutrophil-related cell types, so it is a plausible regulatory anchor but not a tissue-specific marker.
- **Conclusion**: Established: EP300 can regulate transcription and chromatin-dependent cellular responses, and its relationship with SIN3A is supported by STRING. Hypothesis: EP300 may help coordinate the diverse transcriptional, trafficking and stress-related processes represented in the module. The module alone does not establish that EP300 drives the kidney–skin co-abundance pattern.

#### EXOC1

- **Related proteins** (co-abundance neighbors): RCC1L (0.81), UNK (0.80); STRING partners: EXOC8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Plasma membrane, Microtubules; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_04054.1, huMAP3_07009.1, huMAP3_09839.1, huMAP3_12587.1
- **Function (MyGene.info)**: exocyst complex component 1. The protein encoded by this gene is a component of the exocyst complex, a multiple protein complex essential for targeting exocytic vesicles to specific docking sites on the plasma membrane. Though best characterized in yeast, the component proteins and functions of the exocyst complex have been demonstrated to be highly conserved in higher eukaryotes. At least eight components of the exocyst comp…
- **Diseases (Open Targets)**: neurodegenerative disease (0.475); dengue disease (0.370); sialolithiasis (0.188); cervical carcinoma (0.167); hyperaldosteronism (0.166)
- **Europe PMC papers**: 318
- **Why important**: EXOC1 is a core exocyst component involved in vesicle docking, exocytosis and Golgi-to-plasma-membrane transport. It has a direct high-confidence STRING relationship with EXOC8 and appears in several hu.MAP complexes containing other exocyst components. It is detected at the protein level in kidney and skin and is located at the plasma membrane and microtubules. Its network position connects it to RCC1L and UNK, placing vesicle trafficking within the broader co-abundance structure.
- **Conclusion**: Established: EXOC1 represents a known vesicle-trafficking process, supported by its function, STRING relationship and hu.MAP context. Hypothesis: exocyst activity may couple intracellular biosynthetic capacity to delivery of membrane or junctional components in both tissues. The co-abundance data do not prove increased exocytosis or a direct interaction with the rest of the module.

#### INTS4

- **Related proteins** (co-abundance neighbors): MLST8 (0.81); STRING partners: INTS9 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_08985.1, huMAP3_09363.1, huMAP3_09230.1, huMAP3_10641.1, huMAP3_15286.1, huMAP3_12564.1, huMAP3_13510.1
- **Function (MyGene.info)**: integrator complex subunit 4. INTS4 is a subunit of the Integrator complex, which associates with the C-terminal domain of RNA polymerase II large subunit (POLR2A; MIM 180660) and mediates 3-prime end processing of small nuclear RNAs U1 (RNU1; MIM 180680) and U2 (RNU2; MIM 180690) (Baillat et al., 2005 [PubMed 16239144]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: preeclampsia (0.186); systemic lupus erythematosus (0.173); prostate carcinoma (0.160); celiac disease (0.139); hepatocellular carcinoma (0.072)
- **Europe PMC papers**: 223
- **Why important**: INTS4 is an Integrator-complex subunit involved in small nuclear RNA processing and RNA polymerase transcription surveillance. It is paired with INTS9 by a high-confidence STRING relationship and occurs with INTS9 across multiple hu.MAP complexes containing additional Integrator subunits. Its nucleolar-rim localization and detection in kidney and skin support a broadly relevant RNA-processing role. Its disease associations are more limited than those of EP300, but the complex-level evidence makes it an informative structural marker of the module's RNA-processing neighborhood.
- **Conclusion**: Established: INTS4 and INTS9 belong to a known Integrator-associated machinery, with support from both STRING and hu.MAP. Hypothesis: coordinated Integrator activity could reflect a shared requirement for RNA maturation or transcriptional quality control in kidney and skin cells. No globally significant GO or KEGG term confirms that interpretation for the module as a whole.

#### DSG2

- **Related proteins** (co-abundance neighbors): RCC1L (0.85), EPHA2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cell Junctions; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: desmoglein 2. This gene encodes a member of the desmoglein family and cadherin cell adhesion molecule superfamily of proteins. Desmogleins are calcium-binding transmembrane glycoprotein components of desmosomes, cell-cell junctions between epithelial, myocardial, and other cell types. The encoded preproprotein is proteolytically processed to generate the mature glycoprotein. This gene is present in a gene clust…
- **Diseases (Open Targets)**: arrhythmogenic right ventricular dysplasia 10 (0.812); arrhythmogenic right ventricular cardiomyopathy (0.781); dilated cardiomyopathy 1BB (0.714); familial isolated dilated cardiomyopathy (0.615); Abnormality of the cardiovascular system (0.552)
- **Europe PMC papers**: 3811
- **Why important**: DSG2 is a desmosomal cadherin that mediates calcium-dependent cell adhesion and desmosome organization. It is located at cell junctions, is detected in kidney and skin, and shows epithelial and urothelial cell-type associations in HPA. Its module links to RCC1L and EPHA2, connecting junctional structure with signaling and the broader co-abundance network. DSG2 has substantial literature and established disease associations with arrhythmogenic and dilated cardiomyopathies, demonstrating the biological importance of junctional integrity.
- **Conclusion**: Established: DSG2 is a tissue-structural adhesion gene with relevant kidney and skin protein detection and epithelial cell-type evidence. Hypothesis: DSG2 may mark the epithelial or junction-maintenance component that helps explain conservation of the module across the two tissues. The data do not show that DSG2 physically connects the entire module or that cardiac disease mechanisms apply directly here.

#### RCL1

- **Related proteins** (co-abundance neighbors): UNK (0.89), TRMT5 (0.87), ALG2 (0.85); STRING partners: UTP6 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA terminal phosphate cyclase like 1. Predicted to enable endoribonuclease activity. Predicted to be involved in endonucleolytic cleavage of tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Predicted to act upstream of or within endonucleolytic cleavage in 5'-ETS of tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA) and endonucleolytic cleavage in ITS1 to separate SSU-rRNA from 5.8S rRNA and LSU-rRNA from tricis…
- **Diseases (Open Targets)**: Thrombocytopenia (0.388); psychotic disorder (0.334); hemorrhagic disease (0.328); thrombocytopenia 4 (0.328); Abnormal male internal genitalia morphology (0.136)
- **Europe PMC papers**: 441
- **Why important**: RCL1 is implicated in endonucleolytic processing of ribosomal RNA and small-subunit ribosome biogenesis. It connects to ALG2 and TRMT5 in the co-abundance graph and to UTP6 through a near-maximal STRING relationship. Its tissue-enhanced HPA signal in liver and its cell-type signals in hepatocytes, erythrocyte progenitors and other cells indicate that it is not kidney- or skin-specific. Its disease associations include thrombocytopenia and related hematologic phenotypes, while its literature volume provides stronger support than many lesser-characterized module genes.
- **Conclusion**: Established: RCL1 and UTP6 participate in a known ribosome-biogenesis neighborhood supported by STRING and compatible annotations. Hypothesis: this neighborhood may represent the biosynthetic-demand component of the shared module, enabling tissue cells to maintain protein production and turnover. The lack of global enrichment means this remains a gene-level interpretation rather than a demonstrated module-wide ribosome-biogenesis program.

## Module 7

**Tissue pair**: kidney and skin  
**Genes (24)**: AKAP17A, ATG4B, LIG3, ERCC2, TBRG4, GTPBP10, HAUS4, NDUFS2, NDUFV1, PDHB, PCK2, PDS5B, PTCD3, RAD50, MRPL2, MRPL4, MRPS27, MRPS33, MRPS35, SPTLC2, SUPV3L1, YARS2, TOP2B, ATP6V0A1

### Function

The module represents mitochondrial gene expression and protein production, centered on mitochondrial ribosome structure and mitochondrial translation. The primary evidence is the globally corrected enrichment for mitochondrial gene expression (GO:BP mitochondrial gene expression; q_global = 6.94e-06), organellar and mitochondrial ribosomes (GO:CC organellar ribosome; q_global = 4.47e-05) (GO:CC mitochondrial ribosome; q_global = 4.47e-05), mitochondrial translation (GO:BP mitochondrial translation; q_global = 0.000228), ribosome and ribosomal-subunit terms (5 globally significant GO/KEGG terms, q_global 0.000283–0.0384; see the table), mitochondrial protein-containing complexes (GO:CC mitochondrial protein-containing complex; q_global = 0.000388), and the mitochondrion and its inner membrane (GO:CC mitochondrion; q_global = 0.00204) (GO:CC mitochondrial inner membrane; q_global = 0.011) (GO:CC organelle inner membrane; q_global = 0.0179). NDUFS2 and NDUFV1 support a respiratory-chain component, while PDHB and PCK2 support mitochondrial carbon metabolism. The module therefore reflects coordinated mitochondrial protein synthesis linked to oxidative metabolism rather than a narrowly kidney- or skin-specific pathway. STRING enrichment (15 supplementary STRING terms; within-query FDR 1.62e-06–3.91e-05) is concordant supplementary evidence and is not treated as global significance.

**Cell composition.** This is not a plasma-protein or secreted-protein module: HPA reports no secreted genes. It is unlikely to be explained primarily by blood contamination or blood-cell abundance because nearly all genes have low immune-cell specificity and only AKAP17A is immune-cell enhanced in basophils. Most genes have low tissue specificity, and HPA detects protein for nearly all tested genes in both kidney and skin. The pattern is broadly expressed and compatible with a shared housekeeping mitochondrial program or shared metabolically active cell populations. HPA single-cell enhancement across reproductive, neural, epithelial, and other cell types cautions against assigning the module to one specific kidney or skin cell type.

**GO/KEGG enrichment**: 16 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP mitochondrial gene expression | 6.94e-06 | FASTKD4, MRPL2, MRPL4, MRPS27, MRPS33, MRPS35, PTCD3, SUPV3L1, YARS2 |
| GO:CC organellar ribosome | 4.47e-05 | MRPL2, MRPL4, MRPS27, MRPS33, MRPS35, PTCD3 |
| GO:CC mitochondrial ribosome | 4.47e-05 | MRPL2, MRPL4, MRPS27, MRPS33, MRPS35, PTCD3 |
| GO:CC mitochondrial matrix | 7.7e-05 | FASTKD4, MRPL2, MRPL4, MRPS27, MRPS33, MRPS35, NDUFS2, PCK2, PDHB, PTCD3, SUPV3L1, YARS2 |
| GO:BP mitochondrial translation | 0.000228 | MRPL2, MRPL4, MRPS27, MRPS33, MRPS35, PTCD3, YARS2 |
| KEGG Ribosome - Homo sapiens (human) | 0.000283 | MRPL2, MRPL4, MRPS27, MRPS33, MRPS35, PTCD3 |
| GO:CC ribosomal subunit | 0.000332 | MRPL2, MRPL4, MRPS27, MRPS33, MRPS35, PTCD3 |
| GO:CC mitochondrial protein-containing complex | 0.000388 | MRPL2, MRPL4, MRPS27, MRPS33, MRPS35, PTCD3, SUPV3L1 |
| GO:CC organellar small ribosomal subunit | 0.0018 | MRPS27, MRPS33, MRPS35, PTCD3 |
| GO:CC mitochondrial small ribosomal subunit | 0.0018 | MRPS27, MRPS33, MRPS35, PTCD3 |
| GO:CC mitochondrion | 0.00204 | ATG4B, FASTKD4, GTPBP10, LIG3, MRPL2, MRPL4, MRPS27, MRPS33, MRPS35, NDUFS2, NDUFV1, PCK2, PDHB, PTCD3, SUPV3L1, YARS2 |
| GO:CC ribosome | 0.0051 | MRPL2, MRPL4, MRPS27, MRPS33, MRPS35, PTCD3 |
| GO:CC small ribosomal subunit | 0.00623 | MRPS27, MRPS33, MRPS35, PTCD3 |
| GO:CC mitochondrial inner membrane | 0.011 | MRPL2, MRPL4, MRPS27, MRPS33, MRPS35, NDUFS2, NDUFV1, PTCD3 |
| GO:CC organelle inner membrane | 0.0179 | MRPL2, MRPL4, MRPS27, MRPS33, MRPS35, NDUFS2, NDUFV1, PTCD3 |

### STRING and hu.MAP

STRING supports a coherent known mitochondrial-ribosome subnetwork involving MRPL2, MRPL4, MRPS27, MRPS33, MRPS35, and PTCD3, with GTPBP10 connected to large-subunit proteins. STRING also links NDUFS2 with NDUFV1, PCK2 with PDHB, and LIG3 with ERCC2 and RAD50. These relationships indicate that much of the module recapitulates established biology. hu.MAP places MRPL2, MRPL4, SUPV3L1, and YARS2 in mitochondrial large-ribosome or mitochondrial RNA-related complexes (hu.MAP huMAP3_09113.1) (hu.MAP huMAP3_06589.1) (hu.MAP huMAP3_06550.1) (hu.MAP huMAP3_07939.1) (hu.MAP huMAP3_08458.1) (hu.MAP huMAP3_09483.1) (hu.MAP huMAP3_00983.1) (hu.MAP huMAP3_04652.1) (hu.MAP huMAP3_06439.1); MRPS35, PTCD3, and MRPS33 in small-subunit complexes (hu.MAP huMAP3_05954.1) (hu.MAP huMAP3_05807.1) (hu.MAP huMAP3_03554.1); and NDUFS2 with NDUFV1 in complex-I assemblies (hu.MAP huMAP3_08132.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1). TBRG4 and PDS5B occur together in (hu.MAP huMAP3_11232.1). Partial overlap with larger complexes supports biological coherence while showing that the module is a co-abundance representation of larger systems rather than a complete purified complex.

**STRING interactions (score >= 0.7)**: 22 of 276 gene pairs: ERCC2–LIG3 (0.803); GTPBP10–MRPL2 (0.888); GTPBP10–MRPL4 (0.872); LIG3–RAD50 (0.809); MRPL2–MRPL4 (0.999); MRPL2–MRPS27 (0.876); MRPL2–MRPS33 (0.871); MRPL2–MRPS35 (0.98); MRPL2–PTCD3 (0.846); MRPL4–MRPS27 (0.895); MRPL4–MRPS33 (0.883); MRPL4–MRPS35 (0.994); MRPL4–PTCD3 (0.887); MRPS27–MRPS33 (0.996); MRPS27–MRPS35 (0.991); MRPS27–PTCD3 (0.996); MRPS33–MRPS35 (0.992); MRPS33–PTCD3 (0.987); MRPS35–PTCD3 (0.999); NDUFS2–NDUFV1 (0.999); NDUFV1–PDHB (0.738); PCK2–PDHB (0.89)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Mitochondrial protein-containing complex (FDR = 1.62e-06, 10 genes); COMPARTMENTS Mitochondrial matrix (FDR = 2.14e-06, 12 genes); COMPARTMENTS Mitochondrial protein complex (FDR = 2.17e-06, 10 genes); Process Mitochondrial gene expression (FDR = 2.33e-06, 9 genes); Component Mitochondrial matrix (FDR = 6.97e-06, 12 genes); NetworkNeighborAL Organellar ribosome, and Regulation of mitochondrial gene expression (FDR = 1.14e-05, 7 genes); Component Mitochondrial ribosome (FDR = 1.41e-05, 6 genes); COMPARTMENTS Mitochondrial ribosome (FDR = 1.54e-05, 6 genes); COMPARTMENTS Ribosomal subunit (FDR = 1.54e-05, 6 genes); Keyword Transit peptide (FDR = 1.68e-05, 12 genes); Keyword Ribosomal protein (FDR = 2.9e-05, 6 genes); Component Mitochondrion (FDR = 3.12e-05, 16 genes); NetworkNeighborAL Organellar ribosome (FDR = 3.15e-05, 6 genes); Keyword Mitochondrion (FDR = 3.55e-05, 14 genes); Component Ribosomal subunit (FDR = 3.91e-05, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09113.1 (MRPL2, SUPV3L1, MRPL4, YARS2; 4/72); huMAP3_06589.1 (MRPL2, SUPV3L1, MRPL4, YARS2; 4/79); huMAP3_05954.1 (MRPS35, PTCD3, MRPS33; 3/28); huMAP3_06550.1 (MRPL2, MRPL4, YARS2; 3/62); huMAP3_07939.1 (MRPL2, MRPL4, YARS2; 3/68); huMAP3_08458.1 (MRPL2, MRPL4, YARS2; 3/70); huMAP3_09483.1 (MRPL2, MRPL4, YARS2; 3/74); huMAP3_05807.1 (MRPS35, MRPS27, PTCD3; 3/81); huMAP3_03554.1 (MRPS35, PTCD3; 2/2); huMAP3_00983.1 (MRPL2, MRPL4; 2/22); huMAP3_08132.1 (NDUFS2, NDUFV1; 2/24); huMAP3_04652.1 (MRPL4, YARS2; 2/30); huMAP3_14018.1 (NDUFS2, NDUFV1; 2/48); huMAP3_06397.1 (NDUFS2, NDUFV1; 2/49); huMAP3_09982.1 (NDUFS2, NDUFV1; 2/49); huMAP3_09567.1 (NDUFS2, NDUFV1; 2/52); huMAP3_14878.1 (NDUFS2, NDUFV1; 2/53); huMAP3_06439.1 (MRPL2, MRPL4; 2/57); huMAP3_11232.1 (TBRG4, PDS5B; 2/78)

### Novelty

The broad biological interpretation is not new: mitochondrial translation, mitoribosome, complex-I, DNA-repair, and metabolic relationships are already represented in STRING and hu.MAP. What may be new is the conserved kidney-skin co-abundance configuration, including the linkage among mitochondrial ribosome genes, mitochondrial metabolism, DNA maintenance, autophagy, and cell-division-related genes. That claim remains provisional because the fact sheet does not provide an external catalogue of prior kidney-skin modules, replication cohorts, or independent validation. Absence of hu.MAP or STRING entries for HAUS4, TOP2B, PDS5B, or TBRG4 does not establish novelty; it may reflect incomplete interaction coverage or indirect, regulatory, or context-dependent association.

**Hypothesis.** Mechanistic hypothesis: in shared kidney and skin cell populations, variation in mitochondrial translation capacity is coordinated with respiratory-chain activity and mitochondrial metabolic flux. The dense mitoribosome core may support production of mitochondrially encoded respiratory-chain components, while NDUFS2 and NDUFV1 reflect complex-I activity, PDHB and PCK2 reflect carbon-flow state, and SUPV3L1, YARS2, and PTCD3 support mitochondrial RNA processing and translation. GTPBP10 may bridge mitoribosome assembly with metabolic and genome-maintenance signals. Links to LIG3, RAD50, ATG4B, TOP2B, and PDS5B suggest a possible coupling between mitochondrial activity, nucleic-acid maintenance, autophagy, and proliferative state. This is a hypothesis generated by the co-abundance structure; the enrichment and interaction data do not demonstrate causality, directionality, or direct physical interaction for every module edge.

### Important genes

#### MRPS35

- **Related proteins** (co-abundance neighbors): MRPS33 (0.86), TOP2B (0.83), MRPL2 (0.82), HAUS4 (0.82); STRING partners: MRPL2 (0.98), MRPL4 (0.994), MRPS27 (0.991), MRPS33 (0.992), PTCD3 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_05954.1, huMAP3_05807.1, huMAP3_03554.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein S35. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: alcohol drinking (0.365); urolithiasis (0.350); type 2 diabetes mellitus (0.236); keratoconus (0.218); tic disorder (0.217)
- **Europe PMC papers**: 294
- **Why important**: MRPS35 is a mitochondrial small-subunit ribosomal protein and is included in all listed primary GO and KEGG evidence classes for the mitochondrial ribosome and mitochondrial translation core (16 globally significant GO/KEGG terms, q_global 6.94e-06–0.0384; see the table). It is a highly connected member of the STRING mitoribosome cluster and appears in hu.MAP small-subunit complexes (hu.MAP huMAP3_05954.1) (hu.MAP huMAP3_05807.1) (hu.MAP huMAP3_03554.1). It is detected in both kidney and skin, has mitochondrial localization in HPA, and has substantial literature and disease-linked evidence in the supplied resources.
- **Conclusion**: Established: MRPS35 is a strong structural anchor of the module's mitochondrial-translation interpretation. Hypothesis: its central co-abundance position may make it a useful readout of coordinated mitoribosome activity in kidney and skin, but the data do not show that it controls the module.

#### MRPL2

- **Related proteins** (co-abundance neighbors): MRPS35 (0.82), YARS2 (0.82), ATP6V0A1 (0.81); STRING partners: GTPBP10 (0.888), MRPL4 (0.999), MRPS27 (0.876), MRPS33 (0.871), MRPS35 (0.98), PTCD3 (0.846)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_09113.1, huMAP3_06589.1, huMAP3_06550.1, huMAP3_07939.1, huMAP3_08458.1, huMAP3_09483.1, huMAP3_00983.1, huMAP3_06439.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein L2. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.383); systemic lupus erythematosus (0.133); chronic obstructive pulmonary disease (0.074); non-small cell lung carcinoma (0.030); refractive error (0.028)
- **Europe PMC papers**: 234
- **Why important**: MRPL2 is a mitochondrial large-subunit ribosomal protein with broad coverage across the primary mitochondrial gene-expression, ribosome, mitochondrial-translation, and inner-membrane terms (13 globally significant GO/KEGG terms, q_global 6.94e-06–0.0384; see the table). It has strong STRING links to the mitochondrial-ribosome cluster and occurs across multiple hu.MAP mitochondrial complexes (hu.MAP huMAP3_09113.1) (hu.MAP huMAP3_06589.1) (hu.MAP huMAP3_06550.1) (hu.MAP huMAP3_07939.1) (hu.MAP huMAP3_08458.1) (hu.MAP huMAP3_09483.1) (hu.MAP huMAP3_00983.1) (hu.MAP huMAP3_06439.1). Its network links connect the ribosomal core to YARS2 and ATP6V0A1, and HPA detects it in both tissues.
- **Conclusion**: Established: MRPL2 is a large-subunit anchor connecting several known mitochondrial complexes. Hypothesis: it may help couple mitochondrial translation state to organelle protein quality or trafficking, but the ATP6V0A1 association is not sufficient to establish that mechanism.

#### PTCD3

- **Related proteins** (co-abundance neighbors): HAUS4 (0.84), MRPS33 (0.82); STRING partners: MRPL2 (0.846), MRPL4 (0.887), MRPS27 (0.996), MRPS33 (0.987), MRPS35 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_05954.1, huMAP3_05807.1, huMAP3_03554.1
- **Function (MyGene.info)**: pentatricopeptide repeat domain 3. Enables rRNA binding activity and ribosomal small subunit binding activity. Involved in mitochondrial translation. Located in several cellular components, including cytosol; mitochondrion; and nucleoplasm. Implicated in combined oxidative phosphorylation deficiency 51. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: combined oxidative phosphorylation deficiency 51 (0.678); mixed connective tissue disease (0.230); hereditary disease (0.193); alcohol drinking (0.110); posterior cortical atrophy (0.074)
- **Europe PMC papers**: 308
- **Why important**: PTCD3 has annotations for rRNA binding, small-subunit binding, and mitochondrial translation, and it is represented across the mitochondrial-translation and mitoribosome primary terms (15 globally significant GO/KEGG terms, q_global 6.94e-06–0.0179; see the table). It is part of the dense STRING core with MRPL2, MRPL4, MRPS27, MRPS33, and MRPS35, and appears in hu.MAP small-subunit complexes (hu.MAP huMAP3_05954.1) (hu.MAP huMAP3_05807.1) (hu.MAP huMAP3_03554.1). Its supplied disease association with combined oxidative phosphorylation deficiency gives it particular biological relevance.
- **Conclusion**: Established: PTCD3 is an RNA-handling and small-subunit component of the module. Hypothesis: its presence may connect mitochondrial RNA maturation with respiratory competence, but the co-abundance data do not establish that it is the causal link to oxidative-phosphorylation deficiency.

#### NDUFS2

- **Related proteins** (co-abundance neighbors): GTPBP10 (0.87); STRING partners: NDUFV1 (0.999)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_08132.1, huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S2. The protein encoded by this gene is a core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (complex I). Mammalian mitochondrial complex I is composed of at least 43 different subunits, 7 of which are encoded by the mitochondrial genome, and the rest are the products of nuclear genes. The iron-sulfur protein fraction of complex I is made up of 7 subunits, including this g…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.758); mitochondrial complex I deficiency, nuclear type 6 (0.665); type 2 diabetes mellitus (0.608); mitochondrial disease (0.596); Parkinson disease (0.588)
- **Europe PMC papers**: 1723
- **Why important**: NDUFS2 is a core subunit of mitochondrial respiratory-chain complex I and is annotated for mitochondrial electron transport and complex-I assembly. It connects in STRING to NDUFV1, and both genes recur together in hu.MAP complex-I assemblies (hu.MAP huMAP3_08132.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1). NDUFS2 is also represented in the primary mitochondrial-matrix, mitochondrion, and inner-membrane terms (4 globally significant GO/KEGG terms, q_global 7.7e-05–0.0179; see the table), has tissue enhancement in skeletal muscle and tongue, and has strong supplied disease associations with complex-I deficiency and mitochondrial disease.
- **Conclusion**: Established: NDUFS2 provides a respiratory-chain link to the mitochondrial-translation core. Hypothesis: its co-abundance with mitoribosome genes may reflect coordinated demand for respiratory-chain biogenesis or energy production, but it does not prove that translation changes drive complex-I activity.

#### GTPBP10

- **Related proteins** (co-abundance neighbors): PDS5B (0.91), SUPV3L1 (0.89), RAD50 (0.87), TOP2B (0.87), NDUFS2 (0.87), PCK2 (0.86), MRPS27 (0.86), MRPL4 (0.85), ERCC2 (0.81), LIG3 (0.81), TBRG4 (0.81); STRING partners: MRPL2 (0.888), MRPL4 (0.872)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GTP binding protein 10. Small G proteins, such as GTPBP10, act as molecular switches that play crucial roles in the regulation of fundamental cellular processes such as protein synthesis, nuclear transport, membrane trafficking, and signal transduction (Hirano et al., 2006 [PubMed 17054726]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); Abnormality of the skeletal system (0.266); bone Paget disease (0.178); type 2 diabetes mellitus (0.097); placenta praevia (0.075)
- **Europe PMC papers**: 153
- **Why important**: GTPBP10 has the highest weighted network position in the supplied module and connects mitochondrial-ribosome genes with SUPV3L1, NDUFS2, PCK2, RAD50, TOP2B, PDS5B, and other module members. It is linked by STRING to MRPL2 and MRPL4 and is included in mitochondrial gene-expression and organellar-ribosome supplementary evidence (STRING Process Mitochondrial gene expression; within-query FDR = 2.33e-06) (STRING NetworkNeighborAL Organellar ribosome, and Regulation of mitochondrial gene expression; within-query FDR = 1.14e-05) (STRING Component Mitochondrion; within-query FDR = 3.12e-05). Its supplied annotation identifies a role in mitochondrial large-ribosomal-subunit assembly, and HPA detects it in both kidney and skin.
- **Conclusion**: Established: GTPBP10 is a network bridge with an annotation consistent with mitochondrial large-subunit assembly. Hypothesis: it may coordinate mitochondrial ribosome assembly with metabolic and genome-maintenance states represented by neighboring genes; this requires experimental validation because most of its module connections are co-abundance edges rather than established STRING partnerships.

## Module 8

**Tissue pair**: kidney and skin  
**Genes (10)**: ALDH4A1, ALDH2, ASS1, ETFDH, ABAT, MME, PCCA, CRYZ, ACAA1, ACAA2

### Function

This is a mitochondrial and peroxisomal organic-substrate catabolism module. The strongest primary evidence is enrichment for small-molecule catabolism (GO:BP small molecule catabolic process; q_global = 0.00016), branched-chain amino-acid degradation (KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 0.000214), organic and carboxylic-acid catabolism (GO:BP organic acid catabolic process; q_global = 0.000644)(GO:BP carboxylic acid catabolic process; q_global = 0.000644), and broad small-molecule metabolism (GO:BP small molecule metabolic process; q_global = 0.00192). The module also supports fatty-acid catabolism (GO:BP fatty acid catabolic process; q_global = 0.0145), xenobiotic response (GO:BP response to xenobiotic stimulus; q_global = 0.00692), and alanine, aspartate and glutamate metabolism (KEGG Alanine, aspartate and glutamate metabolism - Homo sapiens (human); q_global = 0.04). The gene composition indicates coordinated handling of branched-chain amino acids, fatty acids, aldehydes, proline-derived intermediates, and related organic acids. The network is centered on ABAT, with ACAA1, ACAA2, ALDH2, ALDH4A1 and PCCA providing interconnected enzymatic links. Thus, the most defensible interpretation is a conserved tissue metabolic program for mitochondrial and peroxisomal substrate oxidation, detoxification and carbon-nitrogen balance.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and the individual proteins are intracellular enzymes except for the membrane-associated MME. It is also not primarily a blood-cell module. Most genes have low immune-cell specificity, although ALDH2 is immune-cell enhanced and ASS1 and MME show immune-cell enrichment in particular cell types. The strongest HPA pattern is tissue and cell-type specialization toward liver, kidney and hepatocytes, with additional signals in enterocytes, colonocytes and proximal tubule cells. Protein detection is complete in kidney and somewhat less complete in skin, with ACAA1 and MME not detected in skin. Therefore, the shared kidney-skin signal is more plausibly a conserved metabolic or shared epithelial-cell program than a blood-contamination signature, although tissue composition and cell-type abundance could contribute.

**GO/KEGG enrichment**: 13 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP small molecule catabolic process | 0.00016 | ABAT, ACAA1, ACAA2, ALDH2, ALDH4A1, ETFDH, PCCA |
| KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human) | 0.000214 | ABAT, ACAA1, ACAA2, ALDH2, PCCA |
| GO:BP organic acid catabolic process | 0.000644 | ABAT, ACAA1, ACAA2, ALDH4A1, ETFDH, PCCA |
| GO:BP carboxylic acid catabolic process | 0.000644 | ABAT, ACAA1, ACAA2, ALDH4A1, ETFDH, PCCA |
| GO:BP small molecule metabolic process | 0.00192 | ABAT, ACAA1, ACAA2, ALDH2, ALDH4A1, ASS1, ETFDH, MME, PCCA |
| GO:BP carboxylic acid metabolic process | 0.00611 | ABAT, ACAA1, ACAA2, ALDH4A1, ASS1, ETFDH, PCCA |
| GO:BP oxoacid metabolic process | 0.0069 | ABAT, ACAA1, ACAA2, ALDH4A1, ASS1, ETFDH, PCCA |
| GO:BP response to xenobiotic stimulus | 0.00692 | ABAT, ACAA1, ALDH2, ASS1, CRYZ |
| GO:BP organic acid metabolic process | 0.00704 | ABAT, ACAA1, ACAA2, ALDH4A1, ASS1, ETFDH, PCCA |
| GO:BP fatty acid catabolic process | 0.0145 | ACAA1, ACAA2, ETFDH, PCCA |
| GO:BP catabolic process | 0.0153 | ABAT, ACAA1, ACAA2, ALDH2, ALDH4A1, CRYZ, ETFDH, MME, PCCA |
| GO:BP monocarboxylic acid catabolic process | 0.0244 | ACAA1, ACAA2, ETFDH, PCCA |
| KEGG Alanine, aspartate and glutamate metabolism - Homo sapiens (human) | 0.04 | ABAT, ALDH4A1, ASS1 |

### STRING and hu.MAP

STRING supports a metabolically coherent core. Strong relationships include ACAA1 with ACAA2 and PCCA, ACAA2 with PCCA and ETFDH, ABAT with ALDH2 and PCCA, and ALDH2 with ALDH4A1 and PCCA. STRING supplementary enrichment independently points to branched-chain amino-acid degradation, fatty-acid beta-oxidation, small-molecule catabolism and amino acid metabolic disorders (STRING KEGG Valine, leucine and isoleucine degradation; within-query FDR = 1.54e-05)(STRING DISEASES Amino acid metabolic disorder; within-query FDR = 1.87e-05)(STRING Process Small molecule catabolic process; within-query FDR = 0.00022)(STRING NetworkNeighborAL Fatty acid beta-oxidation, and Valine catabolic process; within-query FDR = 0.0027)(STRING NetworkNeighborAL Glutamine family amino acid biosynthetic process, and Arginine and proline metabolism; within-query FDR = 0.0053). These results indicate that much of the module reflects established biochemical relationships rather than arbitrary co-abundance. hu.MAP also places PCCA, ACAA2, ALDH4A1 and CRYZ in a shared metabolic complex context (hu.MAP huMAP3_13468.1), while PCCA and ACAA2 occur together in another complex (hu.MAP huMAP3_10458.1). ASS1, CRYZ, MME and several other module genes lack corresponding high-confidence STRING pairings or hu.MAP multi-member complex support. Consequently, the module combines a well-supported catabolic core with additional co-abundance relationships that may reflect pathway coordination, tissue regulation or indirect coupling.

**STRING interactions (score >= 0.7)**: 9 of 45 gene pairs: ABAT–ALDH2 (0.945); ABAT–PCCA (0.821); ACAA1–ACAA2 (0.935); ACAA1–ALDH2 (0.711); ACAA1–PCCA (0.948); ACAA2–ETFDH (0.81); ACAA2–PCCA (0.955); ALDH2–ALDH4A1 (0.85); ALDH2–PCCA (0.844)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Valine, leucine and isoleucine degradation (FDR = 1.54e-05, 5 genes); DISEASES Amino acid metabolic disorder (FDR = 1.87e-05, 6 genes); Process Small molecule catabolic process (FDR = 0.00022, 7 genes); Process Cellular catabolic process (FDR = 0.0004, 9 genes); Process Carboxylic acid catabolic process (FDR = 0.0004, 6 genes); TISSUES Liver (FDR = 0.00056, 10 genes); Keyword Transit peptide (FDR = 0.00058, 7 genes); Process Small molecule metabolic process (FDR = 0.00086, 9 genes); NetworkNeighborAL Fatty acid beta-oxidation, and Valine catabolic process (FDR = 0.0027, 4 genes); Process Carboxylic acid metabolic process (FDR = 0.0039, 7 genes); Process Organic substance catabolic process (FDR = 0.0041, 8 genes); Process Fatty acid catabolic process (FDR = 0.0044, 4 genes); NetworkNeighborAL Fatty acid beta-oxidation (FDR = 0.0053, 3 genes); NetworkNeighborAL Glutamine family amino acid biosynthetic process, and Arginine and proline metabolism (FDR = 0.0053, 3 genes); KEGG Fatty acid degradation (FDR = 0.0059, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (PCCA, ALDH4A1, ACAA2, CRYZ; 4/99); huMAP3_10458.1 (PCCA, ACAA2; 2/16)

### Novelty

The biochemical activities represented here are not new: the STRING relationships, hu.MAP complexes, gene annotations and disease associations establish prior knowledge for much of the metabolic core. Absence of a relationship from STRING or hu.MAP would not by itself establish novelty. The potentially new aspect is the coordinated co-abundance of this particular metabolic gene set as a conserved module shared by kidney and skin, especially the inclusion of genes connected across mitochondrial, peroxisomal and cytosolic compartments. This should be described as a potentially novel tissue-pair network context rather than a newly discovered pathway. Independent replication, comparison with existing kidney and skin co-expression studies, and experimental testing would be required before claiming a new finding.

**Hypothesis.** Hypothesis: the module represents a shared epithelial metabolic adaptation that coordinates mitochondrial oxidation of branched-chain and short-chain substrates with peroxisomal fatty-acid beta-oxidation, aldehyde detoxification and nitrogen handling. ABAT, ALDH4A1 and ASS1 may connect amino-acid-derived carbon and nitrogen flux to central metabolism; PCCA, ACAA2 and ETFDH may support mitochondrial propionate, branched-chain and fatty-acid oxidation; ACAA1 may extend this program into peroxisomal lipid catabolism; and ALDH2 and CRYZ may limit reactive aldehyde or quinone stress. The conserved kidney-skin co-abundance could therefore reflect a shared requirement for metabolic detoxification and redox resilience in epithelial tissues. This mechanistic interpretation is a hypothesis inferred from co-abundance, annotations and known interactions, not proof of physical co-complex formation or causal regulation.

### Important genes

#### ABAT

- **Related proteins** (co-abundance neighbors): ALDH4A1 (0.89), ACAA2 (0.86), ALDH2 (0.86), ACAA1 (0.81); STRING partners: ALDH2 (0.945), PCCA (0.821)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 4-aminobutyrate aminotransferase. 4-aminobutyrate aminotransferase (ABAT) is responsible for catabolism of gamma-aminobutyric acid (GABA), an important, mostly inhibitory neurotransmitter in the central nervous system, into succinic semialdehyde. The active enzyme is a homodimer of 50-kD subunits complexed to pyridoxal-5-phosphate. The protein sequence is over 95% similar to the pig protein. GABA is estimated to be present in near…
- **Diseases (Open Targets)**: GABA aminotransaminase deficiency (0.795); infantile spasms (0.568); mitochondrial DNA depletion syndrome (0.542); epilepsy (0.468); Focal impaired awareness seizure (0.466)
- **Europe PMC papers**: 1783
- **Why important**: ABAT is the strongest network-centered gene in the module and connects to ALDH4A1, ACAA2, ALDH2 and ACAA1. It appears across most of the primary enrichment terms, including small-molecule catabolism, branched-chain amino-acid degradation, organic-acid metabolism and xenobiotic response (GO:BP small molecule catabolic process; q_global = 0.00016)(KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 0.000214)(GO:BP response to xenobiotic stimulus; q_global = 0.00692). Its mitochondrial localization and established role in GABA catabolism make it a plausible bridge between amino-acid metabolism and mitochondrial carbon flux. It also has extensive literature and disease links involving GABA-aminotransferase deficiency, seizures and mitochondrial disease.
- **Conclusion**: Established: ABAT is a mitochondrial aminotransferase with a central network position and broad pathway support. Hypothesis: its centrality may help couple amino-acid catabolism to the broader epithelial oxidative program.

#### ACAA1

- **Related proteins** (co-abundance neighbors): ABAT (0.81); STRING partners: ACAA2 (0.935), ALDH2 (0.711), PCCA (0.948)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Peroxisomes; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA acyltransferase 1. This gene encodes an enzyme operative in the beta-oxidation system of the peroxisomes. Deficiency of this enzyme leads to pseudo-Zellweger syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: hyperpituitarism (0.348); Follicular Cyst (0.127); Sepsis (0.103); neoplasm (0.098); Alzheimer disease (0.082)
- **Europe PMC papers**: 1153
- **Why important**: ACAA1 is the peroxisomal beta-oxidation component of the module and is present in nearly all of the primary metabolic enrichment themes, including fatty-acid catabolism (GO:BP fatty acid catabolic process; q_global = 0.0145). It has strong STRING relationships with ACAA2 and PCCA and links the peroxisomal compartment to the mitochondrial catabolic core. Its established role in very-long-chain fatty-acid and bile-acid metabolism, along with disease association with pseudo-Zellweger syndrome, gives it direct functional and pathological relevance.
- **Conclusion**: Established: ACAA1 supports peroxisomal fatty-acid degradation and is strongly connected to the module's metabolic core. Hypothesis: its inclusion may indicate cross-compartment coordination between peroxisomal lipid processing and mitochondrial oxidation in kidney and skin.

#### ACAA2

- **Related proteins** (co-abundance neighbors): ASS1 (0.88), ABAT (0.86), ETFDH (0.82); STRING partners: ACAA1 (0.935), ETFDH (0.81), PCCA (0.955)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10458.1
- **Function (MyGene.info)**: acetyl-CoA acyltransferase 2. The encoded protein catalyzes the last step of the mitochondrial fatty acid beta-oxidation spiral. Unlike most mitochondrial matrix proteins, it contains a non-cleavable amino-terminal targeting signal. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: bone remodeling disease (0.270); sinusitis (0.260); refractive error (0.190); kidney disorder (0.151); myopia (0.141)
- **Europe PMC papers**: 3056
- **Why important**: ACAA2 is a mitochondrial thiolase involved in the final step of the mitochondrial fatty-acid beta-oxidation spiral. It is connected to ABAT, ASS1 and ETFDH in the module and has strong STRING links to ACAA1 and PCCA. It contributes to the primary evidence for small-molecule, organic-acid, branched-chain and fatty-acid catabolism (GO:BP small molecule catabolic process; q_global = 0.00016)(KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 0.000214)(GO:BP fatty acid catabolic process; q_global = 0.0145), and it is represented in hu.MAP complexes (hu.MAP huMAP3_13468.1)(hu.MAP huMAP3_10458.1). Its liver and hepatocyte enrichment and substantial literature support make it a key marker of oxidative metabolic specialization.
- **Conclusion**: Established: ACAA2 is a mitochondrial fatty-acid oxidation enzyme with both network and complex-level support. Hypothesis: it may act as a principal mitochondrial execution point for the shared kidney-skin catabolic state.

#### ALDH2

- **Related proteins** (co-abundance neighbors): ABAT (0.86), ALDH4A1 (0.83), PCCA (0.81); STRING partners: ABAT (0.945), ACAA1 (0.711), ALDH4A1 (0.85), PCCA (0.844)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 2 family member. This protein belongs to the aldehyde dehydrogenase family of proteins. Aldehyde dehydrogenase is the second enzyme of the major oxidative pathway of alcohol metabolism. Two major liver isoforms of aldehyde dehydrogenase, cytosolic and mitochondrial, can be distinguished by their electrophoretic mobilities, kinetic properties, and subcellular localizations. Most Caucasians have two major isozymes, …
- **Diseases (Open Targets)**: alcohol dependence (0.654); alcohol drinking (0.549); AMED syndrome, digenic (0.503); gout (0.501); atrial fibrillation (0.469)
- **Europe PMC papers**: 7978
- **Why important**: ALDH2 is a highly connected aldehyde-processing enzyme linked to ABAT, ACAA1, ALDH4A1 and PCCA. It contributes to the primary small-molecule catabolism and xenobiotic-response evidence (GO:BP small molecule catabolic process; q_global = 0.00016)(KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 0.000214)(GO:BP response to xenobiotic stimulus; q_global = 0.00692), and its established functions include aldehyde detoxification and ethanol catabolism. It has particularly extensive literature and disease associations, including alcohol-related disorders, gout and cardiovascular disease. Its immune-cell-enhanced HPA pattern also makes it a useful gene for assessing whether local immune composition contributes to the module.
- **Conclusion**: Established: ALDH2 is a well-studied aldehyde-detoxification enzyme and a well-connected member of the metabolic core. Hypothesis: ALDH2 may protect the shared tissue program from reactive aldehydes generated during intensified oxidative metabolism.

#### PCCA

- **Related proteins** (co-abundance neighbors): ALDH2 (0.81); STRING partners: ABAT (0.821), ACAA1 (0.948), ACAA2 (0.955), ALDH2 (0.844)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10458.1
- **Function (MyGene.info)**: propionyl-CoA carboxylase subunit alpha. The protein encoded by this gene is the alpha subunit of the heterodimeric mitochondrial enzyme Propionyl-CoA carboxylase. PCCA encodes the biotin-binding region of this enzyme. Mutations in either PCCA or PCCB (encoding the beta subunit) lead to an enzyme deficiency resulting in propionic acidemia. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by…
- **Diseases (Open Targets)**: propionic acidemia (0.853); hereditary disease (0.487); dilated cardiomyopathy (0.370); neurodegenerative disease (0.357); pontocerebellar hypoplasia type 2D (0.340)
- **Europe PMC papers**: 2633
- **Why important**: PCCA is the biotin-binding alpha subunit of mitochondrial propionyl-CoA carboxylase. It participates in the primary evidence for branched-chain amino-acid degradation and multiple organic-acid and fatty-acid catabolic terms (GO:BP small molecule catabolic process; q_global = 0.00016)(KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 0.000214)(GO:BP fatty acid catabolic process; q_global = 0.0145). It has strong STRING links to ABAT, ACAA1, ACAA2 and ALDH2 and is present in both hu.MAP complex contexts (hu.MAP huMAP3_13468.1)(hu.MAP huMAP3_10458.1). Its established association with propionic acidemia and other metabolic disease gives the module a direct connection to clinically important mitochondrial carbon handling.
- **Conclusion**: Established: PCCA is a central biochemical and interaction-supported component of propionyl-CoA and branched-chain substrate metabolism. Hypothesis: it may coordinate incoming propionyl-CoA flux with the fatty-acid and amino-acid catabolic reactions represented by neighboring genes.

#### ALDH4A1

- **Related proteins** (co-abundance neighbors): ABAT (0.89), ALDH2 (0.83), MME (0.82); STRING partners: ALDH2 (0.85)
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: aldehyde dehydrogenase 4 family member A1. This protein belongs to the aldehyde dehydrogenase family of proteins. This enzyme is a mitochondrial matrix NAD-dependent dehydrogenase which catalyzes the second step of the proline degradation pathway, converting pyrroline-5-carboxylate to glutamate. Deficiency of this enzyme is associated with type II hyperprolinemia, an autosomal recessive disorder characterized by accumulation of delta-1-pyr…
- **Diseases (Open Targets)**: hyperprolinemia type 2 (0.788); Intellectual disability (0.497); hyperprolinemia (0.372); spermatocele (0.255); alcohol drinking (0.150)
- **Europe PMC papers**: 1283
- **Why important**: ALDH4A1 is a mitochondrial matrix enzyme in proline degradation and is connected to ABAT, ALDH2 and MME. It contributes to the primary organic-acid, carboxylic-acid and small-molecule catabolic evidence (GO:BP small molecule catabolic process; q_global = 0.00016)(GO:BP organic acid catabolic process; q_global = 0.000644)(GO:BP carboxylic acid catabolic process; q_global = 0.000644), and it is included in the hu.MAP metabolic complex context (hu.MAP huMAP3_13468.1). Its established disease association with type two hyperprolinemia provides a clear link between the module and disturbed proline-derived carbon metabolism.
- **Conclusion**: Established: ALDH4A1 provides a mitochondrial proline-catabolism branch within the module and has supporting network and complex evidence. Hypothesis: it may help connect proline turnover with aldehyde handling and broader organic-acid clearance in the shared tissue state.

## Module 9

**Tissue pair**: kidney and skin  
**Genes (12)**: ANKRD13A, CCNH, DHX57, POLD1, GEMIN4, GEMIN5, HEATR3, MLH1, ORC3, PGM2L1, TBL3, WDR44

### Function

No GO or KEGG term passed global correction, so the module does not support a formally enriched pathway assignment. Its structure instead suggests a mixed intracellular gene-expression and genome-maintenance module centered on DHX57, with a spliceosomal snRNP-related branch involving GEMIN4 and GEMIN5, a DNA-replication and repair branch involving POLD1, MLH1 and ORC3, and additional links to ribosome biogenesis, vesicle trafficking, cell-cycle transcriptional control and carbohydrate metabolism. These are functional interpretations from the individual gene annotations and network structure, not globally significant enrichment claims.

**Cell composition.** The module is predominantly composed of broadly expressed, non-secreted intracellular proteins. HPA classifies most genes as having low tissue specificity, and the module contains no secreted genes. Most genes have low immune-cell specificity, with no enriched blood-cell category reported, arguing against a straightforward plasma-protein or blood-contamination explanation. Nevertheless, several genes show cell-type associations with spermatids, progenitor or specialized cell populations, so shared cellular composition or correlated cellular activity could contribute to the kidney-skin co-abundance pattern. Protein detection is strong in kidney and present for many genes in skin, but absence of global tissue specificity means the module should not be interpreted as kidney- or skin-specific.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides two high-confidence pairwise relationships: GEMIN4 with GEMIN5 and MLH1 with POLD1. These agree with established spliceosomal snRNP assembly and DNA replication or repair biology, respectively. hu.MAP independently places GEMIN4 and GEMIN5 together in several complexes, including C1, C3 and C4, and places GEMIN4 with HEATR3 in C2. Thus, the strongest external support concerns a GEMIN4-GEMIN5 spliceosome-related unit, while the MLH1-POLD1 relationship is supported by STRING but not by a listed hu.MAP complex. Most module edges lack listed STRING or hu.MAP support, so the co-abundance network extends beyond currently catalogued physical complexes and should not be treated as a single experimentally established multiprotein complex.

**STRING interactions (score >= 0.7)**: 2 of 66 gene pairs: GEMIN4–GEMIN5 (0.999); MLH1–POLD1 (0.944)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04549.1 (GEMIN4, GEMIN5; 2/52); huMAP3_11232.1 (GEMIN4, HEATR3; 2/78); huMAP3_06511.1 (GEMIN4, GEMIN5; 2/79); huMAP3_08980.1 (GEMIN4, GEMIN5; 2/97)

### Novelty

This is not established as a wholly new biological complex or pathway. The GEMIN4-GEMIN5 relationship and their placement in spliceosome-related complexes are already known, as is the MLH1-POLD1 relationship. The potentially novel aspect is the coordinated co-abundance of these established functional components with DHX57, HEATR3, WDR44, TBL3, CCNH, PGM2L1, ORC3 and ANKRD13A across kidney and skin. However, absence of additional STRING or hu.MAP links does not prove novelty, and the lack of globally significant GO or KEGG enrichment prevents a strong claim that this is a newly defined biological program. Independent replication, tissue deconvolution, perturbation experiments and comparison with existing co-expression resources would be needed.

**Hypothesis.** Hypothesis: the module may reflect a shared intracellular maintenance state in kidney and skin that couples RNA processing and translation-related machinery with genome replication or repair, while also incorporating cell-cycle, ribosome-biogenesis, trafficking and metabolic functions. DHX57 may act as the principal abundance-coordinating hub, with a spliceosomal arm involving GEMIN4 and GEMIN5 and a genome-integrity arm involving POLD1, MLH1 and ORC3. The co-abundance may arise from coordinated demand for RNA processing and DNA maintenance in particular cell states rather than from direct physical interaction among all module members. Cell-type composition and shared non-immune cellular programs remain alternative explanations.

### Important genes

#### DHX57

- **Related proteins** (co-abundance neighbors): GEMIN5 (0.89), WDR44 (0.87), TBL3 (0.86), CCNH (0.85), GEMIN4 (0.83), POLD1 (0.82), HEATR3 (0.81), ORC3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 57. Enables RNA binding activity. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.301); sensory perception of smell (0.197); smoking initiation (0.174); alcohol drinking (0.048); acquired thrombocytopenia (0.042)
- **Europe PMC papers**: 170
- **Why important**: DHX57 is the network hub, connecting most of the module's genes with comparatively strong weighted relationships. Its annotation supports RNA binding and positive regulation of translation, which provides a plausible organizing role for links to GEMIN4, GEMIN5 and TBL3, while its disease and sensory associations indicate biological relevance beyond a purely structural network position. Its literature volume is substantial enough to support investigation, but its direct role in this module is not established.
- **Conclusion**: Established: DHX57 is the central network connector and is annotated as an RNA-binding DExH-box helicase associated with translation regulation. Hypothesis: it may coordinate RNA-handling or translational demand with the other module branches. Direct physical or regulatory control over the module is unproven.

#### GEMIN4

- **Related proteins** (co-abundance neighbors): DHX57 (0.83); STRING partners: GEMIN5 (0.999)
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_04549.1, huMAP3_11232.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: gem nuclear organelle associated protein 4. The product of this gene is part of a large complex localized to the cytoplasm, nucleoli, and to discrete nuclear bodies called Gemini bodies (gems). The complex functions in spliceosomal snRNP assembly in the cytoplasm, and regenerates spliceosomes required for pre-mRNA splicing in the nucleus. The encoded protein directly interacts with a DEAD box protein and several spliceosome core proteins. A…
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, cataracts, and renal abnormalities (0.738); neurodegenerative disease (0.527); microcephaly (0.262); Global developmental delay (0.259); Developmental cataract (0.259)
- **Europe PMC papers**: 647
- **Why important**: GEMIN4 is supported by both network context and external molecular-complex evidence. It is paired with GEMIN5 in STRING and appears with GEMIN5 across several hu.MAP complexes, while its annotation places it in SMN-complex and spliceosomal snRNP assembly. It also connects to DHX57 and has a substantial disease-literature record, including developmental and renal abnormalities.
- **Conclusion**: Established: GEMIN4 is a spliceosomal snRNP-assembly component with known complex relationships to GEMIN5 and related spliceosome machinery. Hypothesis: its co-abundance with DHX57 may indicate coordinated RNA processing in the shared kidney-skin cellular state. The module does not establish a new GEMIN4 complex.

#### GEMIN5

- **Related proteins** (co-abundance neighbors): DHX57 (0.89); STRING partners: GEMIN4 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_04549.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: gem nuclear organelle associated protein 5. This gene encodes a WD repeat protein that is a component of the survival of motor neurons (SMN) complex. The SMN complex plays a critical role in mRNA splicing through the assembly of spliceosomal small nuclear ribonucleoproteins (snRNPs), and may also mediate the assembly and transport of other classes of ribonucleoproteins. The encoded protein is the snRNA-binding component of the SMN complex. …
- **Diseases (Open Targets)**: neurodevelopmental disorder with cerebellar atrophy and motor dysfunction (0.819); hereditary disease (0.505); neurodegenerative disease (0.463); alcohol drinking (0.374); autosomal recessive non-syndromic intellectual disability (0.370)
- **Europe PMC papers**: 608
- **Why important**: GEMIN5 is the strongest STRING-supported pair partner in the module through its relationship with GEMIN4, and it is represented with GEMIN4 in multiple hu.MAP complexes. Its established function as an snRNA-binding component of the SMN complex and its role in spliceosomal snRNP assembly make it a key marker of the RNA-processing branch. Its disease associations and literature volume provide additional biological context.
- **Conclusion**: Established: GEMIN5 participates in SMN-complex and spliceosomal snRNP assembly and has a known relationship with GEMIN4. Hypothesis: GEMIN5 may mark coordinated spliceosome-related activity within the module. The kidney-skin co-abundance pattern itself remains a new, unvalidated observation.

#### POLD1

- **Related proteins** (co-abundance neighbors): DHX57 (0.82), PGM2L1 (0.82); STRING partners: MLH1 (0.944)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA polymerase delta 1, catalytic subunit. This gene encodes the 125-kDa catalytic subunit of DNA polymerase delta. DNA polymerase delta possesses both polymerase and 3' to 5' exonuclease activity and plays a critical role in DNA replication and repair. Alternatively spliced transcript variants have been observed for this gene, and a pseudogene of this gene is located on the long arm of chromosome 6. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: mandibular hypoplasia-deafness-progeroid syndrome (0.768); non-small cell lung carcinoma (0.690); acute lymphoblastic leukemia (0.671); colorectal cancer (0.670); acute myeloid leukemia (0.659)
- **Europe PMC papers**: 3886
- **Why important**: POLD1 represents the genome-maintenance branch and is connected to DHX57 and PGM2L1 in the co-abundance network. It is the catalytic subunit of DNA polymerase delta, with established roles in DNA replication and repair, and it has a high-confidence STRING relationship with MLH1. Its extensive literature and associations with inherited syndromes and cancers make it an important biological and disease-relevant module member.
- **Conclusion**: Established: POLD1 performs core DNA replication and repair functions and is linked to MLH1 in STRING. Hypothesis: its co-abundance with RNA-processing genes may reflect a shared proliferative or genome-maintenance state. The network does not demonstrate direct regulation by DHX57 or a physical POLD1 complex containing all module genes.

#### MLH1

- **Related proteins** (co-abundance neighbors): HEATR3 (0.80); STRING partners: POLD1 (0.944)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutL homolog 1. The protein encoded by this gene can heterodimerize with mismatch repair endonuclease PMS2 to form MutL alpha, part of the DNA mismatch repair system. When MutL alpha is bound by MutS beta and some accessory proteins, the PMS2 subunit of MutL alpha introduces a single-strand break near DNA mismatches, providing an entry point for exonuclease degradation. The encoded protein is also involved in DNA…
- **Diseases (Open Targets)**: Lynch syndrome (0.848); colorectal cancer (0.820); mismatch repair cancer syndrome 1 (0.806); Muir-Torre syndrome (0.758); colon carcinoma (0.744)
- **Europe PMC papers**: 25031
- **Why important**: MLH1 is a central DNA mismatch-repair factor with very extensive literature and strong disease associations, particularly Lynch syndrome and colorectal cancer. Its high-confidence STRING relationship with POLD1 provides the clearest external support for the module's genome-integrity branch, while its network connection to HEATR3 may link that branch to ribosome-related biology.
- **Conclusion**: Established: MLH1 functions in mismatch repair and forms a known STRING-supported relationship with POLD1. Hypothesis: its co-abundance with HEATR3 and the RNA-processing branch may reflect coordinated DNA maintenance during specific cellular states. The module does not establish a novel MLH1 interaction.

## Module 10

**Tissue pair**: kidney and skin  
**Genes (36)**: ANKZF1, ANKRD17, ARID1B, ARMC8, ASCC3, ASH2L, C1orf52, CHAF1A, DDX54, DICER1, EPB41, ESF1, MCM3AP, HMGN5, KIF23, KLC1, MIB1, MOV10, IGF2R, MTA2, NAA30, GATAD2A, POLDIP3, PES1, PRRC2A, QSER1, RBM15, RBM27, POLR1A, POLR1B, POLR2D, TFRC, TOP2A, USP13, ZC3H13, ZC3HAV1

### Function

The strongest functional interpretation is a nuclear nucleic-acid metabolism and gene-expression module. (GO:MF nucleic acid binding; q_global = 0.00252) is the sole GO/KEGG term passing global correction and identifies nucleic acid binding, with broad representation across the module. The gene annotations support several connected processes: RNA polymerase activity and ribosomal RNA production through POLR1A and POLR1B; ribosome biogenesis and rRNA processing through PES1, DDX54 and ESF1; RNA processing, methylation and post-transcriptional regulation through ZC3H13, RBM15, RBM27, DICER1 and MOV10; and chromatin organization or transcriptional regulation through ARID1B, MTA2, GATAD2A, CHAF1A, HMGN5 and ASH2L. DNA replication, repair, chromosome organization and cell division are additional supported themes in the gene annotations. The STRING supplementary results reinforce a predominantly nuclear or nucleoplasmic interpretation (STRING Keyword Nucleus; within-query FDR = 0.0025)(STRING Component Nucleus; within-query FDR = 0.0115)(STRING Component Nucleoplasm; within-query FDR = 0.0238)(STRING COMPARTMENTS Nucleus; within-query FDR = 0.0333), while the zinc-finger and chromosome signals are supplementary rather than globally corrected evidence (STRING Keyword Zinc-finger; within-query FDR = 0.0139)(STRING Component Chromosome; within-query FDR = 0.0446).

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary identifies only TFRC as secreted to blood, and most genes are intracellular nuclear, nucleolar or cytosolic proteins. The module is broadly expressed rather than strongly tissue restricted, with many genes showing low tissue specificity and most proteins detected in both kidney and skin. It is therefore unlikely to represent a specialized kidney or skin program. However, HPA indicates enrichment of several genes in bone marrow, lymphoid tissue, erythrocyte progenitors, neutrophils, megakaryocyte progenitors and other blood-associated or proliferative cell types. This raises the possibility that part of the shared co-abundance signal reflects common cellular composition, proliferative cells, or blood-cell contribution in the samples. The erythrocyte-associated EPB41 and the blood-associated TFRC, KIF23, TOP2A, ZC3HAV1 and RBM15 should therefore be interpreted cautiously as possible composition-sensitive signals.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleic acid binding | 0.00252 | ANKRD17, ARID1B, ASCC3, ASH2L, C1orf52, DDX54, DICER1, ESF1, GATAD2A, HMGN5, MCM3AP, MOV10, MTA2, PES1, POLDIP3, POLR1A, POLR1B, PRRC2A, RBM15, RBM27, TFRC, TOP2A, ZC3H13, ZC3HAV1 |

### STRING and hu.MAP

STRING supports a mixture of established molecular relationships and functional neighborhood structure. Strong relationships include the DICER1–MOV10 RNA-regulatory pair, RBM15–ZC3H13, GATAD2A–MTA2, KIF23–TOP2A, and the RNA polymerase relationships involving POLR1A, POLR1B and POLR2D. DDX54 connects to PES1 and both major RNA polymerase I subunits, while PES1 connects to the polymerase I machinery. These relationships are consistent with RNA processing, ribosome biogenesis, transcription and cell-cycle functions, but they also show that the module is not a single uniformly connected complex. hu.MAP provides established complex context for the POLR2D–POLR1A–POLR1B group (hu.MAP huMAP3_14318.1)(hu.MAP huMAP3_11092.1), POLDIP3–RBM27 RNA-processing complexes (hu.MAP huMAP3_02553.1)(hu.MAP huMAP3_07273.1)(hu.MAP huMAP3_10299.1), the MTA2–GATAD2A NuRD-related complexes (hu.MAP huMAP3_03905.1)(hu.MAP huMAP3_08738.1)(hu.MAP huMAP3_09499.1)(hu.MAP huMAP3_10472.1)(hu.MAP huMAP3_15128.1), and POLR1A–POLR1B assemblies (hu.MAP huMAP3_00807.1)(hu.MAP huMAP3_09057.1)(hu.MAP huMAP3_08487.1)(hu.MAP huMAP3_06426.1). The partial membership of these larger complexes indicates that the co-abundance module brings together several known nuclear machineries rather than demonstrating one novel physical complex. The ZC3HAV1–DDX54 hu.MAP association (hu.MAP huMAP3_05807.1) adds further RNA-related context.

**STRING interactions (score >= 0.7)**: 14 of 630 gene pairs: CHAF1A–POLDIP3 (0.702); DDX54–PES1 (0.959); DDX54–POLR1A (0.788); DDX54–POLR1B (0.854); DICER1–MOV10 (0.991); ESF1–PES1 (0.709); ESF1–POLR1A (0.819); GATAD2A–MTA2 (0.999); KIF23–TOP2A (0.927); PES1–POLR1A (0.91); PES1–POLR1B (0.798); POLR1A–POLR1B (0.999); POLR1B–POLR2D (0.917); RBM15–ZC3H13 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Nucleic acid binding (FDR = 0.0021, 24 genes); Keyword Nucleus (FDR = 0.0025, 27 genes); Component Nucleus (FDR = 0.0115, 32 genes); Keyword Zinc-finger (FDR = 0.0139, 10 genes); Component Nucleoplasm (FDR = 0.0238, 25 genes); COMPARTMENTS Nucleus (FDR = 0.0333, 27 genes); Component Chromosome (FDR = 0.0446, 13 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14318.1 (POLR2D, POLR1A, POLR1B; 3/58); huMAP3_11092.1 (POLR2D, POLR1A, POLR1B; 3/65); huMAP3_02553.1 (POLDIP3, RBM27; 2/8); huMAP3_07273.1 (POLDIP3, RBM27; 2/8); huMAP3_03905.1 (MTA2, GATAD2A; 2/10); huMAP3_08738.1 (MTA2, GATAD2A; 2/17); huMAP3_10299.1 (POLDIP3, RBM27; 2/22); huMAP3_00807.1 (POLR1A, POLR1B; 2/30); huMAP3_09499.1 (MTA2, GATAD2A; 2/33); huMAP3_10472.1 (MTA2, GATAD2A; 2/36); huMAP3_09057.1 (POLR1A, POLR1B; 2/36); huMAP3_08487.1 (POLR1A, POLR1B; 2/37); huMAP3_06426.1 (POLR1A, POLR1B; 2/38); huMAP3_05807.1 (ZC3HAV1, DDX54; 2/81); huMAP3_15128.1 (MTA2, GATAD2A; 2/96)

### Novelty

The module should not be claimed as a newly discovered molecular complex or as a wholly new pathway. Many of its central relationships and functions are already established by STRING and hu.MAP, especially RNA polymerase, RNA processing, NuRD-related chromatin regulation and RNA surveillance. Its potentially novel aspect is the reproducible co-abundance behavior of this combination across kidney and skin, including the way transcriptional, ribosome-biogenesis, RNA-processing, chromatin and cell-cycle genes covary in these tissue groups. That is a systems-level observation rather than proof of a new direct interaction. Absence of a particular edge from STRING or hu.MAP cannot establish novelty, because those resources are incomplete and the co-abundance relationship may reflect shared regulation, cell composition or indirect biology. Independent replication, adjustment for cell composition, and perturbation or biochemical testing would be needed to support a genuinely new mechanism.

**Hypothesis.** Hypothesis: the shared kidney–skin module represents a broadly deployed nuclear growth and stress-response program that coordinates RNA production, rRNA maturation, RNA processing and chromatin accessibility with DNA replication and cell division. A core transcription and ribosome-biogenesis axis may be formed by POLR1A, POLR1B, PES1, DDX54 and ESF1, while ARID1B, MTA2, GATAD2A, CHAF1A and HMGN5 could couple this activity to chromatin state. The RBM15–ZC3H13 axis, together with DICER1 and MOV10, could connect transcriptional output to RNA modification, processing and surveillance. The blood-cell and proliferative HPA patterns suggest an alternative or contributing explanation: the module may partly reflect shared abundance of hematopoietic or cycling cells in kidney and skin samples. This is a hypothesis, not an established causal model.

### Important genes

#### POLR1A

- **Related proteins** (co-abundance neighbors): POLR1B (0.87), NAA30 (0.87), CHAF1A (0.85), ASCC3 (0.82); STRING partners: DDX54 (0.788), ESF1 (0.819), PES1 (0.91), POLR1B (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoli fibrillar center; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_14318.1, huMAP3_11092.1, huMAP3_00807.1, huMAP3_09057.1, huMAP3_08487.1, huMAP3_06426.1
- **Function (MyGene.info)**: RNA polymerase I subunit A. The protein encoded by this gene is the largest subunit of the RNA polymerase I complex. The encoded protein represents the catalytic subunit of the complex, which transcribes DNA into ribosomal RNA precursors. Defects in this gene are a cause of the Cincinnati type of acrofacial dysostosis. [provided by RefSeq, May 2016].
- **Diseases (Open Targets)**: choanal atresia-hearing loss-cardiac defects-craniofacial dysmorphism syndrome (0.780); acrofacial dysostosis Cincinnati type (0.723); leukodystrophy, hypomyelinating, 27 (0.459); acrofacial dysostosis (0.372); microtia (0.370)
- **Europe PMC papers**: 555
- **Why important**: POLR1A is a high-position module gene and is directly connected in STRING to POLR1B, PES1, DDX54 and ESF1. It is the largest catalytic subunit of RNA polymerase I, and its annotation directly supports transcription of ribosomal RNA. It belongs to the globally significant nucleic-acid-binding term (GO:MF nucleic acid binding; q_global = 0.00252), appears in several hu.MAP polymerase complexes (hu.MAP huMAP3_14318.1)(hu.MAP huMAP3_11092.1)(hu.MAP huMAP3_00807.1)(hu.MAP huMAP3_09057.1)(hu.MAP huMAP3_08487.1)(hu.MAP huMAP3_06426.1), and has disease associations involving craniofacial and developmental disorders. Its substantial literature supports an established biological role.
- **Conclusion**: Established evidence supports POLR1A as a central transcriptional and ribosome-biogenesis anchor of the module. It is plausible, but not proven, that its co-abundance with the surrounding genes reflects coordinated regulation of ribosomal RNA production in kidney and skin.

#### ARID1B

- **Related proteins** (co-abundance neighbors): IGF2R (0.85), POLDIP3 (0.82), ANKRD17 (0.80), ESF1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: AT-rich interaction domain 1B. This locus encodes an AT-rich DNA interacting domain-containing protein. The encoded protein is a component of the SWI/SNF chromatin remodeling complex and may play a role in cell-cycle activation. The protein encoded by this locus is similar to AT-rich interactive domain-containing protein 1A. These two proteins function as alternative, mutually exclusive ARID-subunits of the SWI/SNF complex. The…
- **Diseases (Open Targets)**: Coffin-Siris syndrome (0.778); Coffin-Siris syndrome 1 (0.778); hereditary disease (0.557); arid1b-related disorder (0.536); Intellectual disability (0.533)
- **Europe PMC papers**: 4099
- **Why important**: ARID1B is among the stronger module connectors and links to IGF2R, POLDIP3, ANKRD17 and ESF1. It is a SWI/SNF chromatin-remodeling component with annotations for chromatin remodeling, transcriptional regulation, cell-cycle transition and differentiation. It contributes to (GO:MF nucleic acid binding; q_global = 0.00252) and to the nuclear supplementary STRING terms (STRING Function Nucleic acid binding; within-query FDR = 0.0021)(STRING Keyword Nucleus; within-query FDR = 0.0025)(STRING Component Nucleus; within-query FDR = 0.0115)(STRING Component Nucleoplasm; within-query FDR = 0.0238)(STRING COMPARTMENTS Nucleus; within-query FDR = 0.0333)(STRING Component Chromosome; within-query FDR = 0.0446). Its Coffin-Siris syndrome and intellectual-disability associations, together with extensive literature, make it an important chromatin and disease-relevant gene.
- **Conclusion**: Established evidence supports ARID1B as a chromatin-regulatory bridge between the module's transcriptional and proliferative signals. A role in coupling chromatin state to the kidney–skin co-abundance pattern remains a hypothesis.

#### CHAF1A

- **Related proteins** (co-abundance neighbors): ASCC3 (0.87), POLR1A (0.85), QSER1 (0.84), POLDIP3 (0.83), USP13 (0.83), C1orf52 (0.83), GATAD2A (0.82), ZC3HAV1 (0.82), DDX54 (0.81), ANKRD17 (0.81), PRRC2A (0.80); STRING partners: POLDIP3 (0.702)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromatin assembly factor 1 subunit A. Chromatin assembly factor I (CAF1) is a nuclear complex consisting of p50, p60 (CHAF1B; MIM 601245), and p150 (CHAF1A) subunits that assembles histone octamers onto replicating DNA in vitro (Kaufman et al., 1995 [PubMed 7600578]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: craniofacial microsomia (0.446); neurodegenerative disease (0.441); Abnormality of the skeletal system (0.116); neoplasm (0.105); gastric cancer (0.098)
- **Europe PMC papers**: 845
- **Why important**: CHAF1A has the strongest network position in the supplied module graph and connects to several otherwise distinct parts of the module, including ASCC3, POLR1A, QSER1, POLDIP3, USP13, C1orf52, GATAD2A and ZC3HAV1. It is the p150 subunit of chromatin assembly factor one and supports nucleosome assembly and DNA replication-dependent chromatin assembly. It is supported by the nuclear and chromosome STRING themes (STRING Keyword Nucleus; within-query FDR = 0.0025)(STRING Component Nucleus; within-query FDR = 0.0115)(STRING Component Chromosome; within-query FDR = 0.0446), has bone-marrow and progenitor-cell enrichment in HPA, and has disease associations involving craniofacial and skeletal abnormalities.
- **Conclusion**: Established evidence supports CHAF1A as a network-level chromatin assembly and replication connector. Its progenitor-cell pattern means that cell proliferation or sample composition may contribute to its shared abundance, so a tissue-specific regulatory role is not established.

#### ZC3H13

- **Related proteins** (co-abundance neighbors): MCM3AP (0.85), MIB1 (0.82), RBM15 (0.80); STRING partners: RBM15 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger CCCH-type containing 13. Enables RNA binding activity. Involved in mRNA methylation. Located in nuclear speck. Part of RNA N6-methyladenosine methyltransferase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); type 2 diabetes mellitus (0.332); liver disorder (0.332); renal dialysis (0.290); poisoning (0.213)
- **Europe PMC papers**: 2616
- **Why important**: ZC3H13 links MCM3AP, MIB1 and RBM15 and has a strong STRING relationship with RBM15. It is an RNA-binding component of the RNA N6-methyladenosine methyltransferase complex and is annotated for mRNA processing and stem-cell population maintenance. It contributes to (GO:MF nucleic acid binding; q_global = 0.00252) and to the broad nuclear and zinc-finger supplementary signals (STRING Function Nucleic acid binding; within-query FDR = 0.0021)(STRING Keyword Nucleus; within-query FDR = 0.0025)(STRING Component Nucleus; within-query FDR = 0.0115)(STRING Keyword Zinc-finger; within-query FDR = 0.0139)(STRING Component Nucleoplasm; within-query FDR = 0.0238)(STRING COMPARTMENTS Nucleus; within-query FDR = 0.0333). Its disease associations include neurodegenerative and metabolic disorders, and its literature record is substantial.
- **Conclusion**: Established evidence supports ZC3H13 as an RNA-processing and RNA-modification component that may connect post-transcriptional regulation to the module. Its specific contribution to the kidney–skin module is a hypothesis rather than a demonstrated tissue mechanism.

#### DICER1

- **Related proteins** (co-abundance neighbors): ASCC3 (0.84); STRING partners: MOV10 (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dicer 1, ribonuclease III. This gene encodes a protein possessing an RNA helicase motif containing a DEXH box in its amino terminus and an RNA motif in the carboxy terminus. The encoded protein functions as a ribonuclease and is required by the RNA interference and small temporal RNA (stRNA) pathways to produce the active small RNA component that represses gene expression. This protein also acts as a strong antiviral agent …
- **Diseases (Open Targets)**: DICER1-related tumor predisposition (0.834); pleuropulmonary blastoma (0.765); goiter, multinodular 1, with or without Sertoli-Leydig cell tumors (0.761); global developmental delay - lung cysts - overgrowth - Wilms tumor syndrome (0.732); rhabdomyosarcoma, embryonal, 2 (0.687)
- **Europe PMC papers**: 7894
- **Why important**: DICER1 connects to ASCC3 in the module and has a very strong STRING relationship with MOV10. It produces regulatory small RNAs and is annotated for RNA processing, microRNA metabolism, gene-expression repression and antiviral activity. It contributes to (GO:MF nucleic acid binding; q_global = 0.00252) and to supplementary RNA-related STRING evidence (STRING Function Nucleic acid binding; within-query FDR = 0.0021)(STRING Component Nucleus; within-query FDR = 0.0115)(STRING COMPARTMENTS Nucleus; within-query FDR = 0.0333). DICER1 has extensive literature and strong disease associations, including DICER1-related tumor predisposition and developmental tumor syndromes.
- **Conclusion**: Established evidence supports DICER1 as a post-transcriptional regulatory and antiviral component. It could mediate consequences of the module for gene-expression stability or innate defense, but the co-abundance data do not establish that it drives the module.

## Module 11

**Tissue pair**: kidney and skin  
**Genes (42)**: ASF1A, BAZ1A, BRD2, CBS, CHD8, NCAPG2, CNOT1, DAZAP1, DCAF1, DDX52, DHX37, DHX8, POLA1, GEMIN6, HELLS, HMGCS1, HOMER1, IMP4, ISY1, KAT7, KNTC1, MCM5, MAD2L1, MDN1, NBAS, ORC4, PHAX, PRIM2, CDC40, PYM1, RNF2, RNASEH2B, POLR1C, POLR3E, SPIN1, TRIM24, TLK2, TTK, TTLL12, TXLNG, UNG, ZNF598

### Function

This is a conserved nuclear gene module centered on nucleic-acid metabolism and genome maintenance. The strongest primary evidence is the globally corrected enrichment for nucleic-acid metabolic process (GO:BP nucleic acid metabolic process; q_global = 0.000206), nucleobase-containing compound metabolic process (GO:BP nucleobase-containing compound metabolic process; q_global = 0.00271), macromolecule metabolism (GO:BP macromolecule metabolic process; q_global = 0.00437), RNA metabolism (GO:BP RNA metabolic process; q_global = 0.00909), DNA-replication-origin binding (GO:MF DNA replication origin binding; q_global = 0.0116), DNA-replication initiation (GO:BP DNA replication initiation; q_global = 0.0119), and DNA-templated DNA replication (GO:BP DNA-templated DNA replication; q_global = 0.0217). Nuclear and nucleoplasmic localization are also supported by (GO:CC nucleus; q_global = 0.00174), (GO:CC nucleoplasm; q_global = 0.00918), and (GO:CC nuclear lumen; q_global = 0.0166). The gene composition indicates coordinated chromatin regulation, DNA replication, chromosome organization, RNA processing, ribosome biogenesis, and cell-cycle control rather than a tissue-specific extracellular function. The replication core includes KAT7, MCM5, ORC4, POLA1, and PRIM2 (GO:MF DNA replication origin binding; q_global = 0.0116) (GO:BP DNA replication initiation; q_global = 0.0119) (GO:BP DNA-templated DNA replication; q_global = 0.0217). Chromatin and transcriptional regulation are represented by CHD8, TRIM24, RNF2, BAZ1A, BRD2, HELLS, ASF1A, and SPIN1. RNA processing and ribosome-biogenesis functions include CDC40, DHX8, ISY1, GEMIN6, IMP4, DHX37, DDX52, PHAX, and POLR3E. Thus, the most defensible interpretation is a nuclear genome-expression maintenance module that is especially relevant in proliferating or differentiating cells.

**Cell composition.** The module is not composed of plasma or secreted proteins: HPA reports no secreted genes. Most genes have low tissue specificity, and the module is detected at the protein level in both kidney and skin for many members. HPA shows limited immune-cell specificity overall, so a simple blood-cell explanation is not supported. Nevertheless, the tissue and single-cell annotations show enrichment patterns involving bone marrow, lymphoid tissue, erythrocyte progenitors, megakaryocyte progenitors, monocyte progenitors, and differentiating germ cells. This suggests that part of the shared kidney-skin signal could reflect broadly distributed proliferative or progenitor-cell programs, or shared cell types, rather than a kidney-and-skin-specific biological pathway. The presence of broadly expressed nuclear housekeeping and replication genes makes this interpretation more plausible than a specialized secretory tissue program. HPA protein detection is present in both tissues for many members, but detection alone does not establish that every gene is active in the same cell type.

**GO/KEGG enrichment**: 14 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP nucleic acid metabolic process | 0.000206 | ASF1A, BAZ1A, BRD2, CBS, CDC40, CHD8, CNOT1, DAZAP1, DCAF1, DDX52, DHX37, DHX8, GEMIN6, IMP4, ISY1, KAT7, MCM5, NBAS, NCAPG2, ORC4, PHAX, POLA1, POLR1C, POLR3E, PRIM2, PYM1, RNASEH2B, RNF2, SPIN1, TRIM24, UNG |
| GO:CC nucleus | 0.00174 | ASF1A, BAZ1A, BRD2, CBS, CDC40, CHD8, CNOT1, DAZAP1, DCAF1, DDX52, DHX37, DHX8, GEMIN6, HELLS, IMP4, ISY1, KAT7, KNTC1, MAD2L1, MCM5, MDN1, NCAPG2, ORC4, PHAX, POLA1, POLR1C, POLR3E, PRIM2, PYM1, RNASEH2B, RNF2, SPIN1, TLK2, TRIM24, TTK, TTLL12, TXLNG, UNG |
| GO:BP nucleobase-containing compound metabolic process | 0.00271 | ASF1A, BAZ1A, BRD2, CBS, CDC40, CHD8, CNOT1, DAZAP1, DCAF1, DDX52, DHX37, DHX8, GEMIN6, HMGCS1, IMP4, ISY1, KAT7, MCM5, NBAS, NCAPG2, ORC4, PHAX, POLA1, POLR1C, POLR3E, PRIM2, PYM1, RNASEH2B, RNF2, SPIN1, TRIM24, UNG |
| GO:BP macromolecule metabolic process | 0.00437 | ASF1A, BAZ1A, BRD2, CBS, CDC40, CHD8, CNOT1, DAZAP1, DCAF1, DDX52, DHX37, DHX8, GEMIN6, HELLS, IMP4, ISY1, KAT7, MAD2L1, MCM5, NBAS, NCAPG2, ORC4, PHAX, POLA1, POLR1C, POLR3E, PRIM2, PYM1, RNASEH2B, RNF2, SPIN1, TLK2, TRIM24, TTK, TTLL12, UNG, ZNF598 |
| GO:CC nuclear protein-containing complex | 0.00779 | BAZ1A, CDC40, CHD8, DCAF1, DHX37, DHX8, IMP4, ISY1, KAT7, MAD2L1, MCM5, ORC4, POLA1, POLR1C, POLR3E, PRIM2, PYM1, RNF2 |
| GO:BP RNA metabolic process | 0.00909 | BAZ1A, BRD2, CDC40, CHD8, CNOT1, DAZAP1, DCAF1, DDX52, DHX37, DHX8, GEMIN6, IMP4, ISY1, KAT7, NBAS, NCAPG2, PHAX, POLA1, POLR1C, POLR3E, PRIM2, PYM1, RNASEH2B, RNF2, SPIN1, TRIM24 |
| GO:CC nucleoplasm | 0.00918 | ASF1A, BRD2, CDC40, CHD8, DAZAP1, DCAF1, DDX52, DHX37, DHX8, GEMIN6, IMP4, ISY1, KAT7, MAD2L1, MCM5, MDN1, NCAPG2, ORC4, PHAX, POLA1, POLR1C, POLR3E, PRIM2, PYM1, RNASEH2B, RNF2, SPIN1, TLK2, TRIM24, UNG |
| GO:MF DNA replication origin binding | 0.0116 | KAT7, MCM5, ORC4, POLA1 |
| GO:CC chromosome | 0.0119 | ASF1A, BAZ1A, BRD2, CHD8, HELLS, KAT7, KNTC1, MAD2L1, MCM5, NCAPG2, ORC4, POLA1, PRIM2, RNF2, SPIN1, TRIM24, TTK |
| GO:BP DNA replication initiation | 0.0119 | KAT7, MCM5, ORC4, POLA1, PRIM2 |
| GO:CC nuclear lumen | 0.0166 | ASF1A, BAZ1A, BRD2, CDC40, CHD8, DAZAP1, DCAF1, DDX52, DHX37, DHX8, GEMIN6, IMP4, ISY1, KAT7, MAD2L1, MCM5, MDN1, NCAPG2, ORC4, PHAX, POLA1, POLR1C, POLR3E, PRIM2, PYM1, RNASEH2B, RNF2, SPIN1, TLK2, TRIM24, UNG |
| GO:BP DNA-templated DNA replication | 0.0217 | ASF1A, BAZ1A, KAT7, MCM5, ORC4, POLA1, PRIM2 |
| GO:CC membraneless organelle | 0.0256 | ASF1A, BAZ1A, BRD2, CDC40, CHD8, CNOT1, DCAF1, DDX52, DHX37, DHX8, GEMIN6, HELLS, HOMER1, IMP4, KAT7, KNTC1, MAD2L1, MCM5, MDN1, NCAPG2, ORC4, PHAX, POLA1, POLR1C, PRIM2, PYM1, RNF2, SPIN1, TLK2, TRIM24, TTK, TTLL12 |
| GO:CC intracellular membraneless organelle | 0.0256 | ASF1A, BAZ1A, BRD2, CDC40, CHD8, CNOT1, DCAF1, DDX52, DHX37, DHX8, GEMIN6, HELLS, HOMER1, IMP4, KAT7, KNTC1, MAD2L1, MCM5, MDN1, NCAPG2, ORC4, PHAX, POLA1, POLR1C, PRIM2, PYM1, RNF2, SPIN1, TLK2, TRIM24, TTK, TTLL12 |

### STRING and hu.MAP

STRING supports several coherent known substructures. The replication machinery is represented by MCM5 with ORC4, POLA1, and PRIM2, while POLA1 and PRIM2 are strongly connected. The mitotic checkpoint and chromosome-segregation group includes MAD2L1, KNTC1, TTK, and NCAPG2. The spliceosomal group is supported by CDC40, DHX8, and ISY1, and by the corresponding hu.MAP complexes (hu.MAP huMAP3_06726.1) (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1). RNA polymerase I and III components POLR1C and POLR3E form a STRING pair and occur together in hu.MAP complexes (hu.MAP huMAP3_09057.1) (hu.MAP huMAP3_08487.1) (hu.MAP huMAP3_06426.1) (hu.MAP huMAP3_14318.1) (hu.MAP huMAP3_11092.1). ASF1A and TLK2 have a strong STRING relationship and recur in hu.MAP chromatin-assembly complexes (hu.MAP huMAP3_09289.1) (hu.MAP huMAP3_11834.1) (hu.MAP huMAP3_12963.1) (hu.MAP huMAP3_12711.1). DCAF1 and UNG, CHD8 and RNF2, and DDX52 with DHX37 and IMP4 are also supported by STRING. The hu.MAP results are generally partial-complex signals: the module contains selected members of larger spliceosomal, replication, chromatin, polymerase, and checkpoint assemblies, rather than complete complexes. These concordant known relationships argue that the co-abundance structure captures real cellular machinery, while the remaining edges may reflect shared regulation, cell-cycle state, or indirect coordination.

**STRING interactions (score >= 0.7)**: 24 of 861 gene pairs: ASF1A–TLK2 (0.997); BRD2–KAT7 (0.753); CDC40–DHX8 (0.999); CDC40–ISY1 (0.993); CHD8–RNF2 (0.916); DCAF1–UNG (0.979); DDX52–DHX37 (0.923); DDX52–IMP4 (0.805); DHX37–IMP4 (0.925); DHX8–ISY1 (0.876); GEMIN6–PHAX (0.832); KNTC1–MAD2L1 (0.873); KNTC1–MCM5 (0.728); KNTC1–NCAPG2 (0.742); KNTC1–TTK (0.847); MAD2L1–MCM5 (0.845); MAD2L1–NCAPG2 (0.741); MAD2L1–TTK (0.995); MCM5–ORC4 (0.976); MCM5–POLA1 (0.958); MCM5–PRIM2 (0.948); ORC4–PRIM2 (0.791); POLA1–PRIM2 (0.999); POLR1C–POLR3E (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Nucleus (FDR = 5.25e-06, 34 genes); Process Nucleic acid metabolic process (FDR = 6.43e-06, 28 genes); Process Nucleobase-containing compound metabolic process (FDR = 0.00017, 29 genes); Component Nucleus (FDR = 0.00056, 38 genes); COMPARTMENTS Nucleus (FDR = 0.00068, 33 genes); Process Cellular nitrogen compound metabolic process (FDR = 0.00081, 30 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0024, 21 genes); Process Macromolecule metabolic process (FDR = 0.0026, 33 genes); Component Nucleoplasm (FDR = 0.0053, 29 genes); Component Chromosome (FDR = 0.0053, 16 genes); Component Nuclear lumen (FDR = 0.0066, 30 genes); Process RNA metabolic process (FDR = 0.0107, 19 genes); Component Intracellular non-membrane-bounded organelle (FDR = 0.0109, 29 genes); Component Nuclear protein-containing complex (FDR = 0.0109, 16 genes); Function Histone binding (FDR = 0.0123, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06726.1 (CDC40, DHX8, ISY1; 3/37); huMAP3_08501.1 (CDC40, DHX8, ISY1; 3/47); huMAP3_09504.1 (CDC40, DHX8, ISY1; 3/51); huMAP3_09945.1 (CDC40, DHX8, ISY1; 3/61); huMAP3_02598.1 (MAD2L1, PYM1; 2/2); huMAP3_05779.1 (POLA1, MAD2L1; 2/4); huMAP3_08654.1 (POLA1, PRIM2; 2/5); huMAP3_08676.1 (POLA1, PRIM2; 2/5); huMAP3_02748.1 (POLA1, PRIM2; 2/6); huMAP3_07961.1 (POLA1, PRIM2; 2/6); huMAP3_09716.1 (POLA1, PRIM2; 2/7); huMAP3_06980.1 (POLA1, PRIM2; 2/8); huMAP3_07733.1 (MAD2L1, PYM1; 2/9); huMAP3_09289.1 (TLK2, ASF1A; 2/14); huMAP3_11834.1 (TLK2, ASF1A; 2/14); huMAP3_12963.1 (TLK2, ASF1A; 2/15); huMAP3_03019.1 (DHX8, ISY1; 2/20); huMAP3_12711.1 (TLK2, ASF1A; 2/35); huMAP3_09057.1 (POLR1C, POLR3E; 2/36); huMAP3_08487.1 (POLR1C, POLR3E; 2/37); huMAP3_06426.1 (POLR1C, POLR3E; 2/38); huMAP3_14318.1 (POLR1C, POLR3E; 2/58); huMAP3_11092.1 (POLR1C, POLR3E; 2/65)

### Novelty

The module is unlikely to be a wholly new molecular function because its principal components belong to well-established replication, chromatin, spliceosome, RNA-polymerase, ribosome-biogenesis, and mitotic-checkpoint systems. Its novelty is more plausibly at the level of cross-tissue organization: a kidney-skin co-abundance module that brings together several established nuclear processes. The module has a coherent network and multiple STRING and hu.MAP-supported substructures, which argues against an arbitrary gene set. Conversely, many module members lack direct hu.MAP representation or STRING links within the module, so the complete module as a unified biological unit is not already established by those resources. Absence from either database cannot by itself demonstrate novelty. A cautious conclusion is that the module may be a new tissue-pair co-abundance pattern assembled from largely known molecular machinery, requiring replication in independent cohorts and cell-type-resolved data before being called a novel biological mechanism.

**Hypothesis.** Hypothesis: the shared kidney-skin module reflects a conserved proliferative and genome-maintenance state in selected epithelial, progenitor, or differentiating cells. In this model, KAT7 and chromatin regulators such as CHD8, TRIM24, RNF2, BAZ1A, ASF1A, and HELLS establish or remodel chromatin; MCM5, ORC4, POLA1, and PRIM2 support replication initiation and primer synthesis; CDC40, DHX8, and ISY1 coordinate removal and processing of introns; and POLR1C with POLR3E supports nuclear RNA production. The co-abundance pattern could therefore arise when DNA replication, chromatin assembly, RNA processing, and chromosome surveillance are jointly increased. HPA progenitor and differentiating-cell patterns make this biologically plausible, but the fact sheet does not establish causality, cell-type colocalization, or directionality. This hypothesis should be tested using single-cell co-expression, cell-cycle markers, spatial measurements, and perturbation of the replication or chromatin components.

### Important genes

#### CHD8

- **Related proteins** (co-abundance neighbors): TXLNG (0.91), HELLS (0.87), MDN1 (0.86), ORC4 (0.85), MCM5 (0.84), DHX37 (0.82), BRD2 (0.82), POLA1 (0.81); STRING partners: RNF2 (0.916)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromodomain helicase DNA binding protein 8. This gene encodes a member of the chromodomain-helicase-DNA binding protein family, which is characterized by a SNF2-like domain and two chromatin organization modifier domains. The encoded protein also contains brahma and kismet domains, which are common to the subfamily of chromodomain-helicase-DNA binding proteins to which this protein belongs. This gene has been shown to function in several pr…
- **Diseases (Open Targets)**: autism (0.679); hereditary disease (0.550); autism spectrum disorder (0.547); Intellectual disability (0.515); neurodevelopmental disorder (0.497)
- **Europe PMC papers**: 2541
- **Why important**: CHD8 is one of the highest-connectivity genes in the module and links the network to HELLS, MDN1, ORC4, MCM5, DHX37, BRD2, and POLA1. It is present across many primary nuclear, nucleic-acid, chromosome, and membraneless-organelle terms (11 globally significant GO/KEGG terms, q_global 0.000206–0.0256; see the table). Its established function includes chromatin remodeling and transcriptional regulation, and its STRING relationship with RNF2 supports a chromatin-regulatory connection. It also has substantial literature and disease associations involving neurodevelopmental disorders.
- **Conclusion**: Established evidence supports CHD8 as a central chromatin and transcriptional regulator within the module. Its network position makes it a plausible coordinator, but the data do not establish that CHD8 drives the kidney-skin co-abundance pattern or directly controls the other module members.

#### KAT7

- **Related proteins** (co-abundance neighbors): CBS (0.91), MAD2L1 (0.81); STRING partners: BRD2 (0.753)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lysine acetyltransferase 7. The protein encoded by this gene is part of the multimeric HBO1 complex, which possesses histone H4-specific acetyltransferase activity. This activity is required for functional replication origins and is involved in transcriptional activation of some genes. In both cases, the acetylation of histone H4 helps unfold chromatin so that the DNA can be accessed and replicated or transcribed. [provided …
- **Diseases (Open Targets)**: neurodegenerative disease (0.521); Alzheimer disease (0.372); autoimmune disorder of central nervous system (0.370); Parkinson disease (0.353); lysosomal storage disease (0.352)
- **Europe PMC papers**: 1247
- **Why important**: KAT7 is a direct member of the origin-binding and replication-initiation evidence (GO:MF DNA replication origin binding; q_global = 0.0116) (GO:BP DNA replication initiation; q_global = 0.0119) (GO:BP DNA-templated DNA replication; q_global = 0.0217) and appears in every globally corrected term listed for the replication-focused subset. Its established HBO1-complex function links histone acetylation with functional replication origins and transcriptional activation. It is detected by HPA in both kidney and skin, and it connects in STRING to BRD2 while also linking to replication and chromatin genes in the module.
- **Conclusion**: Established evidence supports KAT7 as a mechanistic bridge between chromatin accessibility and DNA-replication initiation. It is a strong candidate for coordinating the module's replication and chromatin arms, although co-abundance alone cannot show that its acetyltransferase activity is altered.

#### POLA1

- **Related proteins** (co-abundance neighbors): MAD2L1 (0.82), HELLS (0.82), CHD8 (0.81); STRING partners: MCM5 (0.958), PRIM2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_05779.1, huMAP3_08654.1, huMAP3_08676.1, huMAP3_02748.1, huMAP3_07961.1, huMAP3_09716.1, huMAP3_06980.1
- **Function (MyGene.info)**: DNA polymerase alpha 1, catalytic subunit. This gene encodes the catalytic subunit of DNA polymerase, which together with a regulatory and two primase subunits, forms the DNA polymerase alpha complex. The catalytic subunit plays an essential role in the initiation of DNA replication. [provided by RefSeq, Mar 2010].
- **Diseases (Open Targets)**: X-linked reticulate pigmentary disorder (0.747); X-linked intellectual disability, van Esch type (0.731); acute lymphoblastic leukemia (0.598); non-small cell lung carcinoma (0.593); B-cell chronic lymphocytic leukemia (0.590)
- **Europe PMC papers**: 1674
- **Why important**: POLA1 is a core DNA-replication enzyme and occurs in the primary replication terms (GO:MF DNA replication origin binding; q_global = 0.0116) (GO:BP DNA replication initiation; q_global = 0.0119) (GO:BP DNA-templated DNA replication; q_global = 0.0217). It has strong STRING relationships with MCM5 and PRIM2, and hu.MAP repeatedly places it with PRIM2 and other replication-complex components (hu.MAP huMAP3_05779.1) (hu.MAP huMAP3_08654.1) (hu.MAP huMAP3_08676.1) (hu.MAP huMAP3_02748.1) (hu.MAP huMAP3_07961.1) (hu.MAP huMAP3_09716.1) (hu.MAP huMAP3_06980.1). Its disease associations include X-linked reticulate pigmentary disorder and intellectual disability, while its network position connects the replication machinery to HELLS, CHD8, and MAD2L1.
- **Conclusion**: Established evidence identifies POLA1 as a functional anchor of the module's DNA-replication arm. Its presence supports a genuine replication-associated program rather than a generic nuclear annotation, but it does not prove that all module genes operate in one physical complex.

#### CDC40

- **Related proteins** (co-abundance neighbors): TXLNG (0.80), MDN1 (0.80); STRING partners: DHX8 (0.999), ISY1 (0.993)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06726.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: cell division cycle 40. Pre-mRNA splicing occurs in two sequential transesterification steps. The protein encoded by this gene is found to be essential for the catalytic step II in pre-mRNA splicing process. It is found in the spliceosome, and contains seven WD repeats, which function in protein-protein interactions. This protein has a sequence similarity to yeast Prp17 protein, which functions in two different cellular …
- **Diseases (Open Targets)**: neurodegenerative disease (0.464); pontocerebellar hypoplasia, type 15 (0.409); dengue disease (0.370); pontocerebellar hypoplasia (0.261); respiratory tract infectious disorder (0.202)
- **Europe PMC papers**: 396
- **Why important**: CDC40 represents the RNA-processing arm and is included in the hu.MAP spliceosomal complexes (hu.MAP huMAP3_06726.1) (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1). STRING shows strong relationships with DHX8 and ISY1, exactly matching the recurring hu.MAP subcomplex. It is broadly represented in the primary nucleic-acid and RNA-metabolism terms (8 globally significant GO/KEGG terms, q_global 0.000206–0.0256; see the table). Its established function is catalytic step two of pre-mRNA splicing, and it has disease associations involving pontocerebellar hypoplasia.
- **Conclusion**: Established evidence supports CDC40 as a credible marker of coordinated spliceosome activity within the module. Its connection to the replication and chromatin genes is an association in this network, not proof of a direct mechanistic coupling.

#### CBS

- **Related proteins** (co-abundance neighbors): KAT7 (0.91), PHAX (0.88), TXLNG (0.87), TRIM24 (0.86), ORC4 (0.85), DDX52 (0.84), ZNF598 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cystathionine beta-synthase. The protein encoded by this gene acts as a homotetramer to catalyze the conversion of homocysteine to cystathionine, the first step in the transsulfuration pathway. The encoded protein is allosterically activated by adenosyl-methionine and uses pyridoxal phosphate as a cofactor. Defects in this gene can cause cystathionine beta-synthase deficiency (CBSD), which can lead to homocystinuria. This gen…
- **Diseases (Open Targets)**: classic homocystinuria (0.867); homocystinuria (0.583); hyperhomocysteinemia, thrombotic, cbs-related (0.558); familial thoracic aortic aneurysm and aortic dissection (0.549); Marfan syndrome (0.418)
- **Europe PMC papers**: 30545
- **Why important**: CBS is a high-connectivity module member that connects KAT7, PHAX, TXLNG, TRIM24, ORC4, DDX52, and ZNF598. It is included in the globally corrected nucleic-acid and macromolecule terms (4 globally significant GO/KEGG terms, q_global 0.000206–0.00437; see the table), although those broad terms do not establish a specific CBS pathway. Its established enzyme function is transsulfuration, including conversion of homocysteine to cystathionine and contribution to cellular hydrogen-sulfide production. It has extensive literature and strong disease associations with cystathionine beta-synthase deficiency and homocystinuria. HPA shows liver and pancreas tissue enhancement and immune-cell enrichment in neutrophils, making it a potentially informative marker of metabolic or compositional influence.
- **Conclusion**: Established evidence supports CBS as a metabolic outlier or bridge within an otherwise predominantly nuclear module. Its connections may reflect shared regulation or cellular composition rather than a direct biochemical partnership with replication factors. CBS therefore deserves validation before being assigned a central role in the proposed genome-maintenance mechanism.

## Module 12

**Tissue pair**: kidney and skin  
**Genes (5)**: ATP2C1, CETN2, GLYR1, ITSN1, RPP30

### Function

No GO or KEGG term passed global correction, so the module does not support a globally significant pathway assignment. The gene annotations instead indicate a heterogeneous combination of processes: ITSN1 is associated with endocytic membrane traffic, actin-linked signaling, and vesicle recycling; ATP2C1 with intracellular calcium and manganese transport, epidermis development, and calcium-dependent cell adhesion; RPP30 with tRNA processing through the RNase P and RNase MRP complexes; CETN2 with centrosome, centriole, microtubule, ciliary, and spermatogenesis-related functions; and GLYR1 with nucleosome binding and transcription-associated chromatin remodeling. The co-abundance structure is star-like, with ITSN1 connected to every other member, but this pattern alone does not establish a shared biochemical pathway.STRING functional enrichment was absent.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. All members are detected at the protein level in both kidney and skin, while the tissue profile is predominantly of low tissue specificity. CETN2 is tissue enhanced in ciliated-tissue contexts, whereas the other genes are broadly distributed. The single-cell profile is mixed, including cell-type-enhanced or group-enriched patterns for several genes and low cell-type specificity for GLYR1. Most members have low immune-cell specificity, although ITSN1 is immune-cell enhanced in eosinophil and non-classical-monocyte contexts. Thus, the module does not resemble a coherent secreted or blood-cell program, but shared cellular composition, epithelial or ciliated-cell representation, and broadly expressed housekeeping-related activity could contribute to the kidney-skin co-abundance pattern.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

None of the possible within-module gene pairs reaches the stated high-confidence STRING threshold, and no hu.MAP complex contains multiple module members. Therefore the edges in the co-abundance network are not corroborated as established physical or functional interactions by these resources. Known biology remains gene-specific: ITSN1 has reported interactions with several endocytic and actin-regulatory proteins, ATP2C1 is a calcium pump, RPP30 is an RNase P/MRP subunit, CETN2 is a centriole and calcium-binding protein, and GLYR1 is associated with nucleosome and chromatin functions. None of those established relationships directly validates the observed module edges.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The kidney-skin co-abundance pattern appears potentially novel as a network-level observation because it is not represented by a corresponding high-confidence STRING interaction set or a shared hu.MAP complex. However, that absence does not prove biological novelty: the pattern could reflect correlated expression, shared cell composition, technical or sampling effects, or an indirect cellular state. The individual genes and their disease and molecular functions are already established, so the defensible novelty claim is limited to the particular cross-tissue co-abundance configuration, which requires independent replication and perturbational testing.

**Hypothesis.** Hypothesis: this module may represent a coordinated cellular-state signal centered on ITSN1-linked membrane trafficking and signaling, accompanied by calcium handling through ATP2C1, ciliary or centrosomal organization through CETN2, RNA maturation through RPP30, and chromatin regulation through GLYR1. In kidney and skin, the correlation could arise when epithelial, ciliated, or other shared cell populations undergo a common change in membrane dynamics, adhesion, intracellular calcium handling, and biosynthetic activity. This is a mechanistic hypothesis rather than an established pathway interpretation; the lack of global GO/KEGG enrichment, STRING support, and hu.MAP support makes direct physical coupling uncertain.

### Important genes

#### ITSN1

- **Related proteins** (co-abundance neighbors): GLYR1 (0.85), ATP2C1 (0.84), RPP30 (0.82), CETN2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: intersectin 1. The protein encoded by this gene is a cytoplasmic membrane-associated protein that indirectly coordinates endocytic membrane traffic with the actin assembly machinery. In addition, the encoded protein may regulate the formation of clathrin-coated vesicles and could be involved in synaptic vesicle recycling. This protein has been shown to interact with dynamin, CDC42, SNAP23, SNAP25, SPIN90, EPS15,…
- **Diseases (Open Targets)**: hereditary disease (0.531); neurodevelopmental disorder (0.451); Autistic behavior (0.404); Intellectual disability (0.378); autosomal dominant non-syndromic intellectual disability (0.371)
- **Europe PMC papers**: 1094
- **Why important**: ITSN1 is the central network member, connected to every other gene in the module and having the strongest weighted connectivity. Its established function in endocytic membrane traffic, clathrin-coated vesicles, actin assembly, and signaling provides the most plausible organizing biology for the network. It also has substantial literature and reported associations with hereditary and neurodevelopmental disorders.
- **Conclusion**: Established: ITSN1 is a membrane-associated endocytic and signaling regulator with the dominant network position. Hypothesis: it may be the principal correlational hub linking membrane trafficking to the other module processes, but the absence of STRING support means a direct role in this module is not demonstrated.

#### ATP2C1

- **Related proteins** (co-abundance neighbors): ITSN1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase secretory pathway Ca2+ transporting 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases. This magnesium-dependent enzyme catalyzes the hydrolysis of ATP coupled with the transport of calcium ions. Defects in this gene cause Hailey-Hailey disease, an autosomal dominant disorder. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Aug 20…
- **Diseases (Open Targets)**: Hailey-Hailey disease (0.801); restless legs syndrome (0.326); movement disorder (0.265); cutaneous lupus erythematosus (0.231); systemic lupus erythematosus (0.225)
- **Europe PMC papers**: 1369
- **Why important**: ATP2C1 is directly relevant to skin biology through calcium transport, calcium-dependent cell adhesion, and epidermis development. Its established disease association with Hailey-Hailey disease gives it strong biological and clinical importance, and it has substantial literature. Its connection to the central ITSN1 node makes it a plausible functional partner in the co-abundance pattern.
- **Conclusion**: Established: ATP2C1 maintains secretory-pathway calcium and manganese homeostasis and is important for epidermal integrity. Hypothesis: its co-abundance with ITSN1 may reflect coordinated regulation of calcium-dependent membrane trafficking or adhesion, but this relationship is not established by the available interaction resources.

#### CETN2

- **Related proteins** (co-abundance neighbors): ITSN1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Nucleoplasm, Flagellar centriole; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: centrin 2. Caltractin belongs to a family of calcium-binding proteins and is a structural component of the centrosome.  The high level of conservation from algae to humans and its association with the centrosome suggested that caltractin plays a fundamental role in the structure and function of the microtubule-organizing center, possibly required for the proper duplication and segregation of the centrosome. …
- **Diseases (Open Targets)**: neurodegenerative disease (0.144); esophageal squamous cell carcinoma (0.077); glioblastoma (0.060); megalencephaly-polymicrogyria-postaxial polydactyly-hydrocephalus syndrome (0.059); non-syndromic X-linked intellectual disability (0.057)
- **Europe PMC papers**: 783
- **Why important**: CETN2 is the only tissue-enhanced member and has a distinctive HPA profile in ciliated-cell contexts. Its established roles in centrosome structure, centriole replication, microtubule organization, and ciliary biology give the module a possible epithelial or ciliary dimension. It also has a substantial literature and recognized disease associations involving neurodevelopmental and tumor-related conditions.
- **Conclusion**: Established: CETN2 is a calcium-binding centrosomal protein associated with centriole and ciliary functions. Hypothesis: CETN2 may mark the cellular composition or structural state that makes the kidney-skin module visible, rather than being a direct molecular partner of ITSN1.

#### RPP30

- **Related proteins** (co-abundance neighbors): ITSN1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribonuclease P/MRP subunit p30. Enables ribonuclease P RNA binding activity. Contributes to ribonuclease P activity. Involved in tRNA 5'-leader removal. Part of multimeric ribonuclease P complex and ribonuclease MRP complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); alcohol drinking (0.297); ovarian dysfunction (0.260); Chest pain (0.230); hyperpituitarism (0.205)
- **Europe PMC papers**: 1572
- **Why important**: RPP30 is a core component of RNase P and RNase MRP and is required for tRNA five-prime leader removal and RNA processing. It has extensive literature and multiple disease-related associations. Its presence introduces a fundamental RNA-maturation function into an otherwise membrane, calcium, and centrosome-oriented module, making it important for judging whether the module reflects a unified pathway or correlated cellular activity.
- **Conclusion**: Established: RPP30 contributes to essential tRNA and RNA processing as part of multimeric ribonucleoprotein complexes. Hypothesis: its co-abundance may reflect a general increase in biosynthetic or proliferative activity rather than a specific physical connection to the other module members.

#### GLYR1

- **Related proteins** (co-abundance neighbors): ITSN1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glyoxylate reductase 1 homolog. Enables DNA binding activity; methylated histone binding activity; and nucleosome binding activity. Involved in positive regulation of histone acetylation and positive regulation of transcription by RNA polymerase II. Located in cytosol and nucleoplasm. Part of nucleosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.321); facial pain (0.127); ocular hypotension (0.093); neoplasm (0.076); colorectal carcinoma (0.076)
- **Europe PMC papers**: 300
- **Why important**: GLYR1 is the only module member with low cell-type specificity and is annotated for nucleosome binding, histone-related activity, and transcription-associated chromatin remodeling. It has a smaller literature base than the more intensively studied central and disease-linked members, but its chromatin role could connect the module to broader changes in cellular state. Its network link to ITSN1 is the only observed module connection for GLYR1.
- **Conclusion**: Established: GLYR1 has annotated chromatin and transcription-related functions. Hypothesis: GLYR1 may represent a regulatory-state component whose abundance changes alongside membrane and structural programs, but there is no evidence here for a direct GLYR1-ITSN1 mechanism.

## Module 13

**Tissue pair**: kidney and skin  
**Genes (16)**: ZNHIT6, BCLAF1, NCAPH, CRNKL1, ERCC5, KRI1, LRWD1, MRE11, NELFE, RBM39, RRP15, SRRT, STEEP1, TCERG1, TXNL4A, ZNF207

### Function

(GO:BP RNA processing; q_global = 0.0275) provides the primary functional interpretation: RNA processing, supported by broad overlap across the module. The participating genes include spliceosomal and mRNA-processing factors such as SRRT, TCERG1, TXNL4A, CRNKL1, RBM39 and BCLAF1, together with nucleolar RNA-processing factors such as KRI1, RRP15 and ZNHIT6. The supplementary STRING results reinforce RNA processing (STRING Process RNA processing; within-query FDR = 0.0218), nucleic-acid metabolism (STRING Process Nucleic acid metabolic process; within-query FDR = 0.0218) and major-pathway mRNA splicing (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0384), but these are not independent globally corrected enrichment claims. The module therefore most plausibly represents a nuclear RNA maturation and splicing program, with additional links to transcriptional regulation, ribosome biogenesis, DNA repair and chromosome biology. The absence of additional globally corrected terms does not invalidate this interpretation.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly nuclear or nucleolar. Most genes have low tissue specificity and low immune-cell specificity, arguing against a module driven primarily by blood contamination or a strongly restricted immune population. Protein detection is broadly compatible with both kidney and skin, although some genes show specialized HPA patterns, including bone-marrow enrichment for RBM39 and BCLAF1, testis enrichment for LRWD1, and blood-cell or progenitor-associated patterns for NCAPH. These specialized signals may reflect proliferative or cell-state contributions rather than a kidney- or skin-specific pathway. The module is therefore more consistent with a broadly expressed housekeeping or cell-state program that is conserved across the two tissues, with possible contributions from proliferating, differentiating or specialized cells.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA processing | 0.0275 | BCLAF1, CRNKL1, KRI1, RBM39, RRP15, SRRT, TCERG1, TXNL4A, ZNHIT6 |

### STRING and hu.MAP

STRING contains a coherent interaction core involving SRRT, TCERG1, TXNL4A, RBM39, CRNKL1 and BCLAF1. Particularly strong support connects CRNKL1 with TCERG1, RBM39 with SRRT and TCERG1, and SRRT with TCERG1 and TXNL4A. The ERCC5–MRE11 relationship provides a separate DNA-repair link, while the remaining module connections are not represented as high-confidence STRING interactions. The supplementary STRING terms for RNA processing, splicing, nucleic-acid metabolism and ubiquitin-related keywords (5 supplementary STRING terms; within-query FDR 0.0218–0.0422) are concordant but remain supplementary evidence. hu.MAP independently places SRRT with BCLAF1 in several spliceosome- and RNA-processing-related complexes (hu.MAP huMAP3_06391.1) (hu.MAP huMAP3_07267.1) (hu.MAP huMAP3_10564.1) and places TXNL4A with CRNKL1 in several spliceosomal complexes (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1). These complexes contain many additional proteins that are not in the module, so they support known molecular neighborhoods rather than membership of the entire co-abundance module in one physical complex. Overall, STRING and hu.MAP indicate that part of the module recapitulates established RNA-processing machinery, while the full tissue-shared co-abundance structure extends beyond the currently catalogued pairwise and complex relationships.

**STRING interactions (score >= 0.7)**: 8 of 120 gene pairs: BCLAF1–RBM39 (0.75); CRNKL1–TCERG1 (0.926); ERCC5–MRE11 (0.765); RBM39–SRRT (0.936); RBM39–TCERG1 (0.887); SRRT–TCERG1 (0.839); SRRT–TXNL4A (0.812); TCERG1–TXNL4A (0.803)
**STRING functional enrichment (supplementary, within-query FDR)**: Process RNA processing (FDR = 0.0218, 9 genes); Process Nucleic acid metabolic process (FDR = 0.0218, 12 genes); RCTM mRNA Splicing - Major Pathway (FDR = 0.0384, 5 genes); Keyword Ubl conjugation (FDR = 0.0422, 10 genes); Keyword Isopeptide bond (FDR = 0.0422, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06391.1 (SRRT, BCLAF1; 2/16); huMAP3_07267.1 (SRRT, BCLAF1; 2/16); huMAP3_10564.1 (SRRT, BCLAF1; 2/37); huMAP3_08501.1 (TXNL4A, CRNKL1; 2/47); huMAP3_09504.1 (TXNL4A, CRNKL1; 2/51); huMAP3_09945.1 (TXNL4A, CRNKL1; 2/61); huMAP3_11073.1 (SRRT, BCLAF1; 2/67); huMAP3_09943.1 (SRRT, BCLAF1; 2/78)

### Novelty

The underlying functions and several relationships are established, so the module should not be described as a newly discovered RNA-splicing or DNA-repair mechanism. However, the fact sheet provides no evidence that this particular conserved kidney–skin co-abundance configuration has previously been reported. Its potentially novel aspect is therefore the cross-tissue co-abundance organization and the way RNA-processing, nucleolar, transcriptional, DNA-repair and chromosome-associated genes are coordinated in this dataset. This is a qualified module-level novelty claim, not a claim that the genes or their interactions are novel. Absence from STRING or hu.MAP alone does not establish novelty, and the partial coverage by those resources argues for caution.

**Hypothesis.** Hypothesis: the module reflects a shared nuclear maintenance state in kidney and skin in which RNA processing and spliceosome activity are coordinated with transcriptional control, ribosome biogenesis and genome surveillance. The central SRRT–TCERG1–TXNL4A–RBM39–CRNKL1 network could organize or report active pre-mRNA maturation, while KRI1 and RRP15 connect the state to nucleolar RNA maturation. ERCC5 and MRE11 could couple this transcriptional and RNA-processing state to repair of endogenous or environmentally induced DNA damage, which is biologically plausible in skin but is not established by the co-abundance result. Alternative explanations include a broadly expressed housekeeping program or shared proliferative and differentiating cell states. Testing this hypothesis would require independent tissue cohorts, cell-composition adjustment, perturbation experiments and measurement of coordinated RNA-processing and DNA-repair activity.

### Important genes

#### SRRT

- **Related proteins** (co-abundance neighbors): TCERG1 (0.85), STEEP1 (0.85), TXNL4A (0.84); STRING partners: RBM39 (0.936), TCERG1 (0.839), TXNL4A (0.812)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_06391.1, huMAP3_07267.1, huMAP3_10564.1, huMAP3_11073.1, huMAP3_09943.1
- **Function (MyGene.info)**: serrate, RNA effector molecule. Enables mRNA cap binding complex binding activity and protein-macromolecule adaptor activity. Involved in primary miRNA processing. Located in nucleoplasm. Part of ribonucleoprotein complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dengue disease (0.370); myxedema (0.228); hypothyroidism (0.228); neurodegenerative disease (0.227); hair color (0.175)
- **Europe PMC papers**: 413
- **Why important**: SRRT is a central connector in the high-confidence STRING-supported RNA-processing core, linking TCERG1 and TXNL4A and also connecting with RBM39. It appears with BCLAF1 in multiple hu.MAP complexes (hu.MAP huMAP3_06391.1) (hu.MAP huMAP3_07267.1) (hu.MAP huMAP3_10564.1) and (hu.MAP huMAP3_11073.1) (hu.MAP huMAP3_09943.1). Its established functions include primary microRNA processing, mRNA-cap-complex binding and participation in ribonucleoprotein complexes. It is detected in kidney and skin, while its literature record is substantial.
- **Conclusion**: Established evidence supports SRRT as a core RNA-processing and RNA-regulatory component of the module. Hypothesis: its network position makes it a plausible coordinator or reporter of the shared tissue state, but co-abundance alone does not demonstrate that SRRT controls the other module genes.

#### TCERG1

- **Related proteins** (co-abundance neighbors): SRRT (0.85), STEEP1 (0.84), ZNHIT6 (0.80); STRING partners: CRNKL1 (0.926), RBM39 (0.887), SRRT (0.839), TXNL4A (0.803)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transcription elongation regulator 1. This gene encodes a nuclear protein that regulates transcriptional elongation and pre-mRNA splicing. The encoded protein interacts with the hyperphosphorylated C-terminal domain of RNA polymerase II via multiple FF domains, and with the pre-mRNA splicing factor SF1 via a WW domain. Alternative splicing results in multiple transcripts variants encoding different isoforms. [provided by RefSeq, Jul 2…
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); colorectal cancer (0.336); smoking initiation (0.302); sleep apnea syndrome (0.293); chronic venous hypertension (0.257)
- **Europe PMC papers**: 505
- **Why important**: TCERG1 is a key connector in the STRING-supported core, linking SRRT, RBM39, CRNKL1, TXNL4A and the broader RNA-processing signal. Its established molecular roles directly include transcriptional elongation regulation and pre-mRNA splicing, matching (GO:BP RNA processing; q_global = 0.0275) and the supplementary splicing signal (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0384). It is detected in kidney and skin and has a substantial literature base with disease associations including neurodegenerative disease and colorectal cancer.
- **Conclusion**: Established evidence strongly supports TCERG1 as an informative marker of coordinated transcriptional elongation and mRNA splicing in this module. Hypothesis: TCERG1 may bridge transcription and RNA maturation in the shared program, but the module does not establish causal direction.

#### TXNL4A

- **Related proteins** (co-abundance neighbors): SRRT (0.84), NELFE (0.83); STRING partners: SRRT (0.812), TCERG1 (0.803)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: thioredoxin like 4A. The protein encoded by this gene is a member of the U5 small ribonucleoprotein particle (snRNP), and is involved in pre-mRNA splicing. This protein contains a thioredoxin-like fold and it is expected to interact with multiple proteins. Protein-protein interactions have been observed with the polyglutamine tract-binding protein 1 (PQBP1). Mutations in both the coding region and promoter region of t…
- **Diseases (Open Targets)**: choanal atresia-hearing loss-cardiac defects-craniofacial dysmorphism syndrome (0.765); cleft palate (0.370); dengue disease (0.370); hereditary disease (0.176); neurodegenerative disease (0.167)
- **Europe PMC papers**: 292
- **Why important**: TXNL4A is part of the STRING-supported SRRT–TCERG1 core and connects to the spliceosomal branch represented by CRNKL1 in hu.MAP complexes (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1). Its established functions include spliceosomal complex assembly, snRNP assembly and mRNA splicing, directly supporting (GO:BP RNA processing; q_global = 0.0275) and (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0384). It is detected in kidney and skin and has disease associations involving craniofacial developmental syndromes.
- **Conclusion**: Established evidence identifies TXNL4A as a spliceosome-associated component that helps anchor the module's RNA-processing interpretation. Hypothesis: coordinated TXNL4A abundance may indicate altered spliceosome assembly or demand, but it does not prove altered splicing output.

#### RBM39

- **Related proteins** (co-abundance neighbors): ZNHIT6 (0.84); STRING partners: BCLAF1 (0.75), SRRT (0.936), TCERG1 (0.887)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 39. This gene encodes a member of the U2AF65 family of proteins. The encoded protein is found in the nucleus, where it co-localizes with core spliceosomal proteins. It has been shown to play a role in both steroid hormone receptor-mediated transcription and alternative splicing, and it is also a transcriptional coregulator of the viral oncoprotein v-Rel. Multiple transcript variants have been observed…
- **Diseases (Open Targets)**: neurodegenerative disease (0.401); endometrial cancer (0.220); skin neoplasm (0.217); skin cancer (0.217); actinic keratosis (0.217)
- **Europe PMC papers**: 1169
- **Why important**: RBM39 is an RNA-binding and splice-associated factor with strong STRING links to SRRT and TCERG1 and a supplementary association with RNA processing and major-pathway splicing (STRING Process RNA processing; within-query FDR = 0.0218) (STRING Process Nucleic acid metabolic process; within-query FDR = 0.0218) (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0384). It is tissue enhanced in bone marrow, is detected in kidney and skin, and has a substantial literature record. Its disease associations include skin neoplasm and actinic keratosis, which are relevant to interpreting a skin-containing tissue pair without implying disease causation.
- **Conclusion**: Established evidence supports RBM39 as an important RNA-processing and transcriptional co-regulatory member of the module. Hypothesis: RBM39 could help connect the shared nuclear program to tissue stress or proliferative states, but the co-abundance data cannot distinguish normal tissue biology from cellular-composition effects.

#### ERCC5

- **Related proteins** (co-abundance neighbors): NELFE (0.81), KRI1 (0.81); STRING partners: MRE11 (0.765)
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ERCC excision repair 5, endonuclease. This gene encodes a single-strand specific DNA endonuclease that makes the 3' incision in DNA excision repair following UV-induced damage. The protein may also function in other cellular processes, including RNA polymerase II transcription, and transcription-coupled DNA repair. Mutations in this gene cause xeroderma pigmentosum complementation group G (XP-G), which is also referred to as xeroderma…
- **Diseases (Open Targets)**: xeroderma pigmentosum group G (0.814); xeroderma pigmentosum-Cockayne syndrome complex (0.761); COFS syndrome (0.712); xeroderma pigmentosum (0.679); hereditary disease (0.414)
- **Europe PMC papers**: 1863
- **Why important**: ERCC5 occupies the module branch connected to MRE11 in STRING (STRING Process Nucleic acid metabolic process; within-query FDR = 0.0218) and has a direct, established role in transcription-coupled nucleotide-excision repair, UV-response biology and DNA damage processing. Its disease associations include xeroderma pigmentosum group G and related repair syndromes, making it especially relevant to skin biology. It is detected in kidney and skin and has a very substantial literature base.
- **Conclusion**: Established evidence supports ERCC5 as a DNA-repair component that broadens the module beyond RNA processing. Hypothesis: the module may coordinate RNA maturation with genome surveillance, potentially including protection from transcription-blocking damage in skin, but this coupling is not demonstrated by the enrichment or network data.

## Module 14

**Tissue pair**: kidney and skin  
**Genes (7)**: DDX10, DNMT1, EED, IRGQ, NUP205, RBMS1, SIRT1

### Function

The module is most consistent with a nuclear gene-regulatory and RNA or genome-maintenance program. EED, SIRT1, and DNMT1 connect the module to transcriptional repression, chromatin state, DNA methylation maintenance, and heterochromatin, while DDX10 and RBMS1 support RNA processing, ribosome-related biology, and post-transcriptional regulation. NUP205 contributes nuclear pore organization and nucleocytoplasmic transport, and IRGQ contributes protein quality control and autophagy-related biology. These annotations support a coherent intracellular regulatory interpretation, but no GO or KEGG term passed global correction. Therefore, the functional interpretation is gene-based and network-based rather than a claim of globally significant pathway enrichment.

**Cell composition.** The module is not dominated by secreted or plasma proteins, and all genes have low immune-cell specificity. This argues against a simple blood or plasma contamination explanation. The genes are broadly distributed across tissues, with low tissue specificity, while several show enhancement in specialized cell types including Sertoli cells, germ-cell populations, trophoblast populations, podocytes, neutrophils, retinal cells, and tuft cells. This mixed pattern is more compatible with a shared intracellular program or shared cellular state than with a tissue-specific secretory module. Protein detection is present for most genes in both kidney and skin where data are available, although NUP205 and RBMS1 lack tissue immunohistochemistry detection in the supplied summary and some genes have no data.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known interaction evidence is a connected EED-SIRT1-DNMT1 relationship: DNMT1 is linked to EED and SIRT1, and EED is linked to SIRT1. These known links support an epigenetic regulatory core within the co-abundance module. The remaining co-abundance edges, including EED with NUP205, DDX10, and IRGQ and IRGQ with RBMS1, are not supported by listed STRING interactions and should be treated as module-level associations rather than established physical interactions. No hu.MAP complex contains multiple module members. Thus, the module is not a documented single complex, but it contains a known regulatory interaction core embedded in a broader co-abundance pattern.

**STRING interactions (score >= 0.7)**: 3 of 21 gene pairs: DNMT1–EED (0.921); DNMT1–SIRT1 (0.922); EED–SIRT1 (0.716)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The result should not be called a wholly new molecular complex or a newly discovered pathway. The EED-SIRT1-DNMT1 relationships are already represented in STRING, so the central epigenetic connection has prior support. Conversely, the kidney-skin co-abundance organization that places this known core alongside NUP205, DDX10, IRGQ, and RBMS1 is not explained by a listed hu.MAP complex, and several module edges lack listed STRING support. This makes the tissue-shared co-abundance configuration potentially novel or at least insufficiently characterized, but absence from STRING or hu.MAP alone does not establish novelty. Independent validation would be needed.

**Hypothesis.** Hypothesis: the module reflects a conserved intracellular state in which chromatin regulation and DNA methylation maintenance are coordinated with nuclear transport, RNA maturation, and proteostasis. EED, SIRT1, and DNMT1 may form the regulatory core, while NUP205 and DDX10 could connect that state to nuclear transport and nucleolar RNA processing, and IRGQ with RBMS1 could connect it to protein quality control and RNA regulation. In kidney and skin, the shared signal may arise from cells requiring stable transcriptional programs during differentiation, renewal, or stress adaptation. This is a mechanistic hypothesis, not a demonstrated physical complex or causal pathway.

### Important genes

#### EED

- **Related proteins** (co-abundance neighbors): NUP205 (0.86), DDX10 (0.84), IRGQ (0.84); STRING partners: DNMT1 (0.921), SIRT1 (0.716)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: embryonic ectoderm development. This gene encodes a member of the Polycomb-group (PcG) family. PcG family members form multimeric protein complexes, which are involved in maintaining the transcriptional repressive state of genes over successive cell generations. This protein interacts with enhancer of zeste 2, the cytoplasmic tail of integrin beta7, immunodeficiency virus type 1 (HIV-1) MA protein, and histone deacetylase protei…
- **Diseases (Open Targets)**: Cohen-Gibson syndrome (0.786); viral infectious disease (0.463); smoking initiation (0.428); melanoma (0.418); breast carcinoma (0.417)
- **Europe PMC papers**: 7571
- **Why important**: EED has the highest network connectivity in the module and links the known STRING-supported epigenetic core to NUP205, DDX10, and IRGQ through co-abundance. Its established roles include Polycomb-mediated transcriptional repression and heterochromatin formation. It also has a substantial literature base and disease associations including Cohen-Gibson syndrome and melanoma.
- **Conclusion**: Established evidence supports EED as the principal network bridge and an epigenetic transcriptional regulator. The hypothesis that it organizes the broader kidney-skin module beyond its known partners remains unproven.

#### SIRT1

- **Related proteins** (co-abundance neighbors): NUP205 (0.83), DNMT1 (0.83); STRING partners: DNMT1 (0.922), EED (0.716)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sirtuin 1. This gene encodes a member of the sirtuin family of proteins, homologs to the yeast Sir2 protein. Members of the sirtuin family are characterized by a sirtuin core domain and grouped into four classes. The functions of human sirtuins have not yet been determined; however, yeast sirtuin proteins are known to regulate epigenetic gene silencing and suppress recombination of rDNA. Studies suggest that…
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); atrial fibrillation (0.336); hypertensive disorder (0.204); tooth disorder (0.200); type 2 diabetes mellitus (0.140)
- **Europe PMC papers**: 55588
- **Why important**: SIRT1 connects NUP205 to DNMT1 in the module and participates in the known STRING-supported EED-SIRT1-DNMT1 core. Its supplied annotations involve transcriptional regulation, heterochromatin, DNA repair, and genome maintenance. It has the largest literature volume among the listed genes and broad disease associations.
- **Conclusion**: Established evidence supports SIRT1 as a heavily studied nuclear regulatory factor and member of the known epigenetic interaction core. Its proposed role in coordinating nuclear transport or tissue-shared co-abundance is a hypothesis.

#### DNMT1

- **Related proteins** (co-abundance neighbors): SIRT1 (0.83); STRING partners: EED (0.921), SIRT1 (0.922)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA methyltransferase 1. This gene encodes an enzyme that transfers methyl groups to cytosine nucleotides of genomic DNA. This protein is the major enzyme responsible for maintaining methylation patterns following DNA replication and shows a preference for hemi-methylated DNA. Methylation of DNA is an important component of mammalian epigenetic gene regulation. Aberrant methylation patterns are found in human tumors and a…
- **Diseases (Open Targets)**: autosomal dominant cerebellar ataxia, deafness and narcolepsy (0.806); hereditary sensory neuropathy-deafness-dementia syndrome (0.777); acute myeloid leukemia (0.623); myelodysplastic syndrome (0.615); cancer (0.612)
- **Europe PMC papers**: 30754
- **Why important**: DNMT1 is part of the known STRING-supported triad with EED and SIRT1 and is the canonical maintenance DNA methyltransferase. Its network placement connects it to the epigenetic core, while its annotations and disease associations implicate methylation-dependent gene regulation, developmental abnormalities, and hematologic malignancy. It is also extensively studied.
- **Conclusion**: Established evidence supports DNMT1 as a central maintenance-methylation enzyme within the known regulatory core. The module does not establish that DNMT1 causes the kidney-skin co-abundance pattern or directly regulates its other members.

#### NUP205

- **Related proteins** (co-abundance neighbors): EED (0.86), SIRT1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 205. This gene encodes a nucleoporin, which is a subunit of the nuclear pore complex that functions in active transport of proteins, RNAs and ribonucleoprotein particles between the nucleus and cytoplasm. Mutations in this gene are associated with steroid-resistant nephrotic syndrome. [provided by RefSeq, Jul 2016].
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); familial idiopathic steroid-resistant nephrotic syndrome (0.528); viral infectious disease (0.527); lysosomal storage disease (0.462)
- **Europe PMC papers**: 729
- **Why important**: NUP205 links SIRT1 and EED-related network structure to nuclear pore biology and nucleocytoplasmic transport. Its established function is as a nuclear pore complex component, and mutations are associated with steroid-resistant nephrotic syndrome, directly relevant to kidney biology. It has a meaningful literature base despite lacking listed STRING partners or a hu.MAP multi-member complex here.
- **Conclusion**: Established evidence supports NUP205 as a nuclear transport component with kidney disease relevance. Its connection to the epigenetic core is supported by co-abundance but not by a listed physical interaction, so any mechanistic bridge is provisional.

#### DDX10

- **Related proteins** (co-abundance neighbors): EED (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 10. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.494); pancreatic ductal adenocarcinoma (0.376); lymphoid neoplasm (0.370); breast ductal adenocarcinoma (0.370); prostate adenocarcinoma (0.370)
- **Europe PMC papers**: 534
- **Why important**: DDX10 is connected to EED in the module and contributes a nucleolar RNA-processing dimension. Its established annotation as a DEAD-box helicase includes rRNA processing and broader roles in RNA structural remodeling, ribosome or spliceosome assembly, development, and cell growth. Its disease literature is more limited than that of the epigenetic core genes, making it useful as a less-characterized module component.
- **Conclusion**: Established evidence supports DDX10 as an RNA-processing and nucleolar factor. Its co-abundance with EED may indicate coordination between chromatin regulation and RNA maturation, but that coordination is a hypothesis.

#### IRGQ

- **Related proteins** (co-abundance neighbors): RBMS1 (0.86), EED (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: immunity related GTPase Q. Predicted to enable GTP binding activity. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Familial prostate cancer (0.111); prostate cancer (0.111); familial long QT syndrome (0.063); primary familial polycythemia due to EPO receptor mutation (0.062); autosomal dominant secondary polycythemia (0.060)
- **Europe PMC papers**: 136
- **Why important**: IRGQ connects EED to RBMS1 and contributes a distinct proteostasis-related signal. Its supplied annotations support GTP binding, protein quality control for misfolded or incompletely synthesized proteins, autophagy regulation, and substrate localization to autophagosomes. It has relatively limited literature compared with the core epigenetic genes, which makes the association potentially informative for follow-up.
- **Conclusion**: Established evidence supports IRGQ as a protein-quality-control and autophagy-related factor. Its position in the module does not demonstrate that it links proteostasis causally to chromatin regulation; that interpretation remains a hypothesis.

## Module 15

**Tissue pair**: kidney and skin  
**Genes (5)**: ERO1A, GANAB, HYOU1, PDIA4, SIRPA

### Function

The strongest interpretation is an endoplasmic-reticulum protein folding, quality-control, redox, and glycoprotein-processing module. The primary evidence is the globally significant KEGG term for protein processing in the endoplasmic reticulum (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00123) and the globally significant GO cellular-component term for the endoplasmic-reticulum lumen (GO:CC endoplasmic reticulum lumen; q_global = 0.00567). Both terms contain ERO1A, GANAB, HYOU1, and PDIA4, indicating that the module is organized around ER-lumen proteostasis. The supplementary STRING results independently support ER localization, disulfide-bond formation, glycoprotein handling, ER stress, and protein-disulfide-isomerase-related activity (11 supplementary STRING terms; within-query FDR 0.00015–0.0347). SIRPA is not present in the primary GO/KEGG terms, so its role is better interpreted as a cell-surface or immune-associated connection to the ER proteostasis core rather than as evidence that the entire module has one uniform biochemical function.

**Cell composition.** The module is not composed predominantly of classical secreted proteins: HPA classifies the four ER-associated members as intracellular and membrane or as ER-localized, while SIRPA has no secretome annotation in the fact sheet. Nevertheless, HPA reports secreted-gene status for most module genes, so the dataset may reflect proteins entering or supporting the secretory pathway rather than freely circulating plasma proteins. Tissue specificity is generally low, with only two tissue-enhanced genes, and immune-cell specificity is low for most genes. One gene is blood-cell group enriched and SIRPA is associated with monocytes, eosinophils, myeloid dendritic cells, and neutrophils. Several genes are cell-type enhanced in plasma cells or trophoblasts. Thus, a blood-cell or shared-cell-type contribution cannot be excluded, but the coherent ER annotations and detection of most proteins in both kidney and skin support a broader secretory-cell or tissue-stress program rather than a purely blood-derived signal. HYOU1 is not detected by kidney or skin immunohistochemistry in the supplied HPA summary, so its co-abundance may reflect transcript-level regulation, cell composition, or protein detection limitations.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human) | 0.00123 | ERO1A, GANAB, HYOU1, PDIA4 |
| GO:CC endoplasmic reticulum lumen | 0.00567 | ERO1A, GANAB, HYOU1, PDIA4 |

### STRING and hu.MAP

STRING provides high-confidence support for a connected ER-centered subnetwork. The strongest relationships include ERO1A with PDIA4, HYOU1 with PDIA4, and GANAB with HYOU1; GANAB also connects with PDIA4. These are known or database-supported relationships and therefore show that the co-abundance pattern recapitulates established molecular associations rather than being an isolated statistical grouping. STRING enrichment independently recovers ER protein processing and ER-lumen localization (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.00015), (STRING COMPARTMENTS Endoplasmic reticulum lumen; within-query FDR = 0.00079), and (STRING Component Endoplasmic reticulum lumen; within-query FDR = 0.0026), together with disulfide, glycoprotein, redox, and stress-related annotations (6 supplementary STRING terms; within-query FDR 0.028–0.0487). The infection-related STRING term (STRING KEGG Vibrio cholerae infection; within-query FDR = 0.0412) is supplementary and should not be treated as a primary module function. hu.MAP identifies PDIA4, GANAB, and HYOU1 together in two larger complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). These complexes contain many additional ER, glycosylation, trafficking, and proteostasis proteins, so the module appears to capture a conserved subnetwork or functional slice of larger assemblies, not a complete isolated complex. SIRPA and ERO1A have no listed hu.MAP complex membership, and SIRPA has no listed STRING partner in the supplied evidence.

**STRING interactions (score >= 0.7)**: 4 of 10 gene pairs: ERO1A–PDIA4 (0.984); GANAB–HYOU1 (0.83); GANAB–PDIA4 (0.717); HYOU1–PDIA4 (0.997)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Protein processing in endoplasmic reticulum (FDR = 0.00015, 4 genes); Keyword Signal (FDR = 0.00069, 5 genes); COMPARTMENTS Endoplasmic reticulum lumen (FDR = 0.00079, 4 genes); NetworkNeighborAL Mixed, incl. Photodynamic therapy-induced unfolded protein response, and Protein disulfide isomerase activity (FDR = 0.0014, 3 genes); Component Endoplasmic reticulum lumen (FDR = 0.0026, 4 genes); PMID (2021) The cytoprotective protein MANF promotes neuronal survival independently from its role as a GRP78 cofactor. (FDR = 0.0042, 4 genes); NetworkNeighborAL Endoplasmic reticulum chaperone complex, and ARMET-like (FDR = 0.0125, 2 genes); Keyword Endoplasmic reticulum (FDR = 0.028, 4 genes); Keyword Disulfide bond (FDR = 0.028, 4 genes); Keyword Glycoprotein (FDR = 0.0324, 4 genes); Keyword Redox-active center (FDR = 0.0347, 2 genes); KEGG Vibrio cholerae infection (FDR = 0.0412, 2 genes); PMID (2020) RNA-Seq analysis of European sea bass (Dicentrarchus labrax L.) infected with nodavirus reveals powerful modulation of the stress response. (FDR = 0.0487, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (PDIA4, GANAB, HYOU1; 3/60); huMAP3_09327.1 (PDIA4, GANAB, HYOU1; 3/93)

### Novelty

This is not a wholly new molecular pathway: the ER-proteostasis interpretation is strongly supported by established STRING relationships, two hu.MAP complexes, and concordant gene annotations. The co-abundance module may nevertheless be a potentially novel observation at the level of shared kidney-skin tissue organization, because the fact sheet does not establish that this exact five-gene co-abundance pattern or tissue-pair module has previously been reported. Absence of SIRPA or ERO1A from the listed hu.MAP or STRING relationships does not prove novelty; it may reflect incomplete databases, context-specific regulation, or the difference between co-abundance and direct physical interaction. The appropriate conclusion is therefore contextual novelty as a kidney-skin co-abundance module, not discovery of a new ER pathway or new protein complex.

**Hypothesis.** Hypothesis: in cell populations shared by kidney and skin, or in cells experiencing secretory or environmental stress, increased demand for maturation of disulfide-bonded and glycosylated proteins coordinately engages GANAB-mediated N-glycan processing, ERO1A-linked oxidative folding, PDIA4-mediated disulfide rearrangement, and HYOU1-mediated ER chaperoning and stress adaptation. SIRPA may connect this proteostasis state to immune or myeloid-associated cell composition or receptor signaling. This hypothesis is consistent with the primary terms (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00123) and (GO:CC endoplasmic reticulum lumen; q_global = 0.00567), the STRING network, and the HPA cell-type observations, but the fact sheet does not demonstrate causality, direct regulation by SIRPA, or a specific kidney-skin disease mechanism.

### Important genes

#### PDIA4

- **Related proteins** (co-abundance neighbors): SIRPA (0.82), HYOU1 (0.81); STRING partners: ERO1A (0.984), GANAB (0.717), HYOU1 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 is the central connector in the supplied interaction evidence: it links ERO1A, GANAB, and HYOU1 in STRING and is present in both hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). It belongs to both globally significant terms (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00123) and (GO:CC endoplasmic reticulum lumen; q_global = 0.00567), has ER localization in HPA, and its established function includes protein folding, thiol-disulfide interchange, protein secretion, and ER-stress response. Its disease-association evidence includes neurodegenerative disease and neoplastic or liver-related associations, while its literature volume is substantial.
- **Conclusion**: Established conclusion: PDIA4 is the best molecular anchor for the module's ER proteostasis interpretation. Hypothesis: its network-central position may make it a useful readout of coordinated secretory-pathway stress in kidney and skin, but the fact sheet does not establish that PDIA4 drives the co-abundance pattern.

#### HYOU1

- **Related proteins** (co-abundance neighbors): GANAB (0.82), PDIA4 (0.81); STRING partners: GANAB (0.83), PDIA4 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 is included in both primary terms (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00123) and (GO:CC endoplasmic reticulum lumen; q_global = 0.00567), connects strongly to PDIA4 and GANAB in STRING, and occurs in both hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Its annotation supports ER protein folding, secretion, hypoxia response, ER-stress response, stress adaptation, and suppression of apoptosis. HPA reports cell-type enhancement including plasma cells, and disease associations include granulocytopenia with immunoglobulin abnormality, neurodegenerative disease, dengue disease, coronary artery disorder, and type two diabetes. Its literature volume is substantial.
- **Conclusion**: Established conclusion: HYOU1 is a stress-responsive ER chaperone component that supports the module's folding and stress-adaptation interpretation. Hypothesis: it may report local hypoxia or secretory burden in the shared tissues, although lack of HPA immunohistochemical detection in kidney and skin cautions against assuming abundant local protein.

#### ERO1A

- **Related proteins** (co-abundance neighbors): SIRPA (0.92); STRING partners: PDIA4 (0.984)
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: endoplasmic reticulum oxidoreductase 1 alpha. Enables oxidoreductase activity. Involved in chaperone cofactor-dependent protein refolding. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: DNA methylation (0.155); neoplasm (0.117); cancer (0.107); non-small cell lung carcinoma (0.104); lung adenocarcinoma (0.103)
- **Europe PMC papers**: 698
- **Why important**: ERO1A is present in both primary terms (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00123) and (GO:CC endoplasmic reticulum lumen; q_global = 0.00567) and is linked to PDIA4 by a high-confidence STRING relationship. Its established function is ER oxidoreductase activity, chaperone-cofactor-dependent refolding, ER unfolded-protein response, protein folding, and redox homeostasis. HPA identifies esophageal tissue enhancement and esophageal apical-cell enrichment, while the supplied disease associations include neoplasm and lung cancer-related associations. Its literature volume is lower than that of SIRPA but still substantial.
- **Conclusion**: Established conclusion: ERO1A supplies the redox and oxidative-folding arm of the module. Hypothesis: coordinated ERO1A and PDIA4 activity could indicate increased disulfide-bonded protein maturation, but the co-abundance data do not prove a direct functional dependency in kidney or skin.

#### GANAB

- **Related proteins** (co-abundance neighbors): HYOU1 (0.82); STRING partners: HYOU1 (0.83), PDIA4 (0.717)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in kidney, skin
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: glucosidase II alpha subunit. This gene encodes the alpha subunit of glucosidase II and a member of the glycosyl hydrolase 31 family of proteins. The heterodimeric enzyme glucosidase II plays a role in protein folding and quality control by cleaving glucose residues from immature glycoproteins in the endoplasmic reticulum. Expression of the encoded protein is elevated in lung tumor tissue and in response to UV irradiation. Mut…
- **Diseases (Open Targets)**: polycystic kidney disease 3 with or without polycystic liver disease (0.792); autosomal dominant polycystic liver disease (0.515); autosomal dominant polycystic kidney disease (0.470); Biliary tract abnormality (0.438); COVID-19 (0.370)
- **Europe PMC papers**: 1240
- **Why important**: GANAB is present in both primary terms (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00123) and (GO:CC endoplasmic reticulum lumen; q_global = 0.00567), connects with HYOU1 and PDIA4 in STRING, and is included in both hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Its established role is the alpha subunit of glucosidase II, supporting N-glycan processing and ER quality control. It is detected in both kidney and skin by HPA and has strong disease associations with autosomal-dominant polycystic kidney and liver disease and related polycystic disease. Its literature volume is substantial.
- **Conclusion**: Established conclusion: GANAB adds glycan maturation and quality control to the ER proteostasis interpretation and gives the module a particularly relevant kidney disease connection. Hypothesis: GANAB variation or regulation could influence the tissue-pair signal through altered maturation of glycoproteins, but this module does not establish such a causal route.

#### SIRPA

- **Related proteins** (co-abundance neighbors): ERO1A (0.92), PDIA4 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal regulatory protein alpha. The protein encoded by this gene is a member of the signal-regulatory-protein (SIRP) family, and also belongs to the immunoglobulin superfamily. SIRP family members are receptor-type transmembrane glycoproteins known to be involved in the negative regulation of receptor tyrosine kinase-coupled signaling processes. This protein can be phosphorylated by tyrosine kinases. The phospho-tyrosine residue…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.376); thrombocytopenia 4 (0.364); neurodegenerative disease (0.361); hemorrhagic disease (0.351); diabetes mellitus (0.324)
- **Europe PMC papers**: 3860
- **Why important**: SIRPA has a meaningful network position through its links to ERO1A and PDIA4, although it is absent from the primary GO/KEGG terms and has no listed STRING partner or hu.MAP complex in the supplied evidence. Its established biology is that of a signal-regulatory immunoglobulin-superfamily receptor involved in cell adhesion, migration, negative regulation of receptor tyrosine-kinase-coupled signaling, and regulation of inflammatory responses. HPA associates it with brain tissue enhancement and multiple myeloid or monocyte-related cell types. It has the largest literature volume among the module genes and disease associations including type two diabetes, thrombocytopenia, hemorrhagic disease, and neurodegenerative disease.
- **Conclusion**: Established conclusion: SIRPA is an immune or cell-composition-associated peripheral member rather than a demonstrated ER-lumen component. Hypothesis: its co-abundance with the ER core may reflect myeloid-cell admixture or coordinated inflammatory and proteostasis states; a direct biochemical SIRPA-to-ER interaction is not supported by the supplied interaction databases.

## Module 16

**Tissue pair**: kidney and skin  
**Genes (5)**: NUCB1, PDIA5, PDLIM7, RFTN1, VPS4B

### Function

The module does not have a GO or KEGG term that passes global correction. Therefore, no pathway-level function can be claimed as statistically enriched. Its structure is nevertheless suggestive of a heterogeneous cellular-process module: RFTN1 is the central co-abundance connector, while NUCB1, VPS4B, PDLIM7, and PDIA5 each connect primarily through RFTN1. The gene annotations point to membrane-raft and immune signaling through RFTN1, Golgi calcium homeostasis through NUCB1, vesicle, lysosome, autophagy, and plasma-membrane-repair processes through VPS4B, actin and focal-adhesion organization through PDLIM7, and endoplasmic-reticulum protein folding through PDIA5. These are functional interpretations of individual genes, not evidence of a globally enriched common pathway. STRING provides no supplementary enrichment.

**Cell composition.** The module is not dominated by secreted proteins: NUCB1 is secreted to blood, while PDIA5 is annotated as intracellular and membrane-associated, and the remaining genes are not annotated as secreted. The module is also not uniformly blood-cell specific. HPA assigns low immune-cell specificity to several genes, with immune-cell enhancement or group enrichment for only a subset, including plasmacytoid dendritic cells, basophils, eosinophils, and neutrophils. All genes are cell-type enhanced in the HPA summary, with recurring signals in stromal, epithelial, and neutrophil-related cell types, so shared cellular composition could contribute to the kidney-skin association. Tissue specificity is mixed: some genes are enhanced in lymphoid tissue, blood vessel, intestine, skeletal muscle, or liver, whereas others have low tissue specificity. Protein detection is broader in kidney than skin, with every module protein detected in kidney but only a subset detected in skin. Thus, the module may reflect shared cell populations or general cellular states in the sampled tissues rather than a kidney-skin-specific biochemical pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair reaches the supplied STRING interaction threshold, and no hu.MAP complex contains multiple module members. The observed co-abundance relationships are therefore not corroborated by the supplied high-confidence physical or functional interaction resources. RFTN1 is the network hub by co-abundance, linking each of the other module genes, but this hub status is a property of the module network rather than established molecular interaction evidence. The absence of STRING and hu.MAP support means that the module should be interpreted as a coordinated expression or abundance pattern, not as a demonstrated protein complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel tissue-pair co-abundance pattern, because the module contains a compact RFTN1-centered structure that is absent from the supplied high-confidence STRING and hu.MAP relationships. However, it cannot be called a new biological mechanism on that basis alone. The lack of globally corrected GO or KEGG enrichment, the lack of STRING enrichment, the mixed HPA tissue and cell-type profile, and the absence of known complexes all make a strong mechanistic novelty claim premature. A more defensible conclusion is that the kidney-skin co-abundance association is potentially novel at the network-observation level, while its biological specificity and reproducibility remain to be established with independent cohorts, cell-composition adjustment, and experimental validation.

**Hypothesis.** Mechanistic hypothesis: the module may represent coordinated regulation of membrane-associated trafficking and cellular remodeling across shared kidney and skin cell populations. In this model, RFTN1-associated membrane-raft and immune-signaling biology is co-regulated with NUCB1-linked Golgi calcium handling, VPS4B-linked vesicle and membrane-repair machinery, PDLIM7-linked actin and focal-adhesion organization, and PDIA5-linked endoplasmic-reticulum folding. This is a hypothesis rather than an established pathway. The mixed HPA cell-type signals and the absence of high-confidence STRING or hu.MAP support make shared cell composition, stress, tissue injury, or remodeling equally plausible explanations that require testing.

### Important genes

#### RFTN1

- **Related proteins** (co-abundance neighbors): NUCB1 (0.84), VPS4B (0.84), PDLIM7 (0.81), PDIA5 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: raftlin, lipid raft linker 1. Enables double-stranded RNA binding activity. Involved in B cell receptor signaling pathway; membrane raft assembly; and positive regulation of growth rate. Acts upstream of or within dsRNA transport; response to exogenous dsRNA; and toll-like receptor 3 signaling pathway. Located in endosome; membrane raft; and plasma membrane. Part of protein-containing complex. [provided by Alliance of Genome R…
- **Diseases (Open Targets)**: neurodegenerative disease (0.486); COVID-19 (0.299); lysosomal storage disease (0.288); digestive system disorder (0.282); bone Paget disease (0.230)
- **Europe PMC papers**: 444
- **Why important**: RFTN1 is the co-abundance hub, connecting every other module member. Its annotations link it to membrane-raft assembly, B-cell-receptor signaling, antigen processing, interleukin-related regulation, double-stranded-RNA transport, and toll-like-receptor signaling. HPA indicates lymphoid-tissue enhancement and cell-type enhancement across several immune and nonimmune cell types, while Open Targets links it to neurodegenerative disease, COVID-related disease, lysosomal storage disease, digestive-system disorder, and Paget bone disease. Its literature volume is substantial, making it the best organizing candidate for interpreting the module.
- **Conclusion**: Established: RFTN1 is the central network connector and has annotations consistent with membrane-raft and immune or innate-sensing biology. Hypothesis: its hub position may mark coordinated membrane signaling in shared kidney and skin cell populations, but the module does not establish direct RFTN1-mediated interactions with the other genes.

#### VPS4B

- **Related proteins** (co-abundance neighbors): RFTN1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vacuolar protein sorting 4 homolog B. The protein encoded by this gene is a member of the AAA protein family (ATPases associated with diverse cellular activities), and is the homolog of the yeast Vps4 protein. In humans, two paralogs of the yeast protein have been identified. The former share a high degree of aa sequence similarity with each other, and also with yeast Vps4 and mouse Skd1 proteins. Mouse Skd1 (suppressor of K+ transpor…
- **Diseases (Open Targets)**: HIV infectious disease (0.462); dentin dysplasia type I (0.375); atypical dentin dysplasia due to SMOC2 deficiency (0.372); cystic kidney disease (0.194); enteritis (0.191)
- **Europe PMC papers**: 868
- **Why important**: VPS4B is one of the peripheral genes directly connected to RFTN1. Its established annotations include plasma-membrane repair, autophagy, vacuole organization, lysosomal transport, and chromosome-related cellular functions. HPA detects the protein in both kidney and skin and highlights esophageal epithelial, neutrophil, and ocular epithelial cell types. Open Targets associates it with HIV infectious disease, dentin dysplasia, cystic kidney disease, and enteritis. Its substantial literature supports its importance for interpreting membrane and vesicle biology.
- **Conclusion**: Established: VPS4B is a membrane-trafficking and repair gene detected in both tissues and connected to the module hub. Hypothesis: it could link the observed co-abundance pattern to epithelial or injury-associated membrane remodeling, but this cannot be inferred as a shared complex.

#### PDIA5

- **Related proteins** (co-abundance neighbors): RFTN1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein disulfide isomerase family A member 5. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, a TRX-like domain, and a C-terminal ER-retention sequence. The N-terminal TRX-like domain is the primary bind…
- **Diseases (Open Targets)**: spinal stenosis (0.273); blood coagulation disease (0.269); temporomandibular joint disorder (0.262); placenta praevia (0.144); glioblastoma (0.100)
- **Europe PMC papers**: 501
- **Why important**: PDIA5 is directly connected to RFTN1 and provides the module's clearest endoplasmic-reticulum protein-folding component. It encodes an ER disulfide-isomerase-family protein with thioredoxin domains and annotations for protein folding and electron transport. HPA detects it in both kidney and skin, places it in the ER, and identifies enhancement in liver-related and trophoblast-related cell types as well as plasmacytoid dendritic cells. Open Targets links it to spinal stenosis, blood coagulation disease, temporomandibular joint disorder, placenta praevia, and glioblastoma. Its literature base is substantial.
- **Conclusion**: Established: PDIA5 contributes an ER folding and proteostasis interpretation and is detected in both tissues. Hypothesis: its co-abundance with membrane and trafficking genes may indicate a shared secretory or cellular-stress state, but the absence of pathway enrichment prevents treating this as a demonstrated ER-to-membrane mechanism.

#### PDLIM7

- **Related proteins** (co-abundance neighbors): RFTN1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Actin filaments, Focal adhesion sites; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 7. The protein encoded by this gene is representative of a family of proteins composed of conserved PDZ and LIM domains. LIM domains are proposed to function in protein-protein recognition in a variety of contexts including gene transcription and development and in cytoskeletal interaction. The LIM domains of this protein bind to protein kinases, whereas the PDZ domain binds to actin filaments. The g…
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); nasopharyngeal carcinoma (0.121); neoplasm (0.120); lymphoma (0.115); Hodgkins lymphoma (0.105)
- **Europe PMC papers**: 808
- **Why important**: PDLIM7 is directly connected to RFTN1 and contributes a structural cytoskeletal dimension through PDZ and LIM domains, actin-filament binding, receptor-mediated endocytosis, and muscle-structure development. HPA shows tissue enhancement in blood vessel, intestine, and skeletal muscle and group enrichment in basophils, eosinophils, and neutrophils; its protein is detected in kidney but not skin. Open Targets associates it with neurodegenerative disease, nasopharyngeal carcinoma, neoplasm, lymphoma, and Hodgkin lymphoma. Its substantial literature and focal-adhesion or actin localization make it useful for assessing whether the module reflects tissue architecture or immune-cell composition.
- **Conclusion**: Established: PDLIM7 is a cytoskeletal and adhesion-associated module member with vascular, intestinal, muscular, and granulocyte-related HPA signals. Hypothesis: it may indicate coordinated structural remodeling or an infiltrating-cell signal in the shared tissues, but its absence of skin protein detection argues against assuming uniform tissue-level activity.

#### NUCB1

- **Related proteins** (co-abundance neighbors): RFTN1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in kidney, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleobindin 1. This gene encodes a member of a small calcium-binding EF-hand protein family. The encoded protein is thought to have a key role in Golgi calcium homeostasis and Ca(2+)-regulated signal transduction events. [provided by RefSeq, Jun 2010].
- **Diseases (Open Targets)**: neoplasm (0.099); breast cancer (0.083); breast carcinoma (0.082); diffuse large B-cell lymphoma (0.074); pancreatic ductal adenocarcinoma (0.066)
- **Europe PMC papers**: 626
- **Why important**: NUCB1 is directly connected to RFTN1 and adds a Golgi and calcium-regulation interpretation to the module. It is annotated as a calcium-binding EF-hand protein involved in Golgi calcium homeostasis and calcium-regulated signaling, with a small-GTPase-related biological-process annotation. HPA detects it in both kidney and skin, identifies secretion to blood, and highlights decidual stromal, enterocyte, and esophageal apical cell types. Open Targets links it to neoplasm, breast cancer, breast carcinoma, diffuse large B-cell lymphoma, and pancreatic ductal adenocarcinoma. Its literature base is substantial.
- **Conclusion**: Established: NUCB1 is a broadly detected, blood-secreted, Golgi-associated calcium-regulatory protein connected to the module hub. Hypothesis: it could reflect secretory-pathway or calcium-handling coordination with RFTN1 and VPS4B, although the module does not demonstrate direct molecular coupling.
