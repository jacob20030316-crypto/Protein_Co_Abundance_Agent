# Conserved co-abundance modules: circulatory_system and lung

## Module 0

**Tissue pair**: circulatory_system and lung  
**Genes (34)**: A1BG, SERPINF2, A2M, APOA2, APOA4, LPA, APOC3, APOD, C4BPA, CA1, CP, CFB, CFH, CFI, C3, C5, C6, C7, C8A, C8B, C9, CPN2, FBN1, SERPING1, ITIH1, ITIH2, ITIH3, ITIH4, KNG1, PLG, RBP4, SAA4, GC, AZGP1

### Function

This is a circulating extracellular innate-immune and protease-regulatory module, with a strong complement and coagulation signature. The primary evidence is the globally corrected enrichment for blood microparticles (GO:CC blood microparticle; q_global = 1.33e-18), complement and coagulation cascades (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 1.01e-16), extracellular space and extracellular region (GO:CC extracellular space; q_global = 3.23e-15) (GO:CC extracellular region; q_global = 4.6e-14), complement activation (GO:BP complement activation; q_global = 1.07e-14), the alternative and classical complement pathways (GO:BP complement activation, alternative pathway; q_global = 6.18e-11) (GO:BP complement activation, classical pathway; q_global = 1.78e-10), humoral immune responses (GO:BP humoral immune response; q_global = 1.03e-10) (GO:BP humoral immune response mediated by circulating immunoglobulin; q_global = 7.02e-10), and the membrane attack complex (GO:CC membrane attack complex; q_global = 1.63e-07). The module also contains a substantial lipid-transport component, supported by plasma lipoprotein and protein-lipid complex terms (4 globally significant GO/KEGG terms, q_global 0.0014–0.0114; see the table), and an inter-alpha-trypsin-inhibitor and hyaluronan-associated component (GO:BP hyaluronan metabolic process; q_global = 0.00863) (GO:BP aminoglycan metabolic process; q_global = 0.0417) (GO:BP glycosaminoglycan metabolic process; q_global = 0.0417). Together, the evidence supports a plasma protein program linking complement surveillance, regulation of extracellular proteolysis, fibrinolysis and coagulation, lipid particles, and extracellular matrix or hyaluronan stabilization. The KEGG disease terms (KEGG Systemic lupus erythematosus - Homo sapiens (human); q_global = 9.55e-05) (KEGG Coronavirus disease - Homo sapiens (human); q_global = 0.000329) (KEGG Staphylococcus aureus infection - Homo sapiens (human); q_global = 0.00128) should be interpreted as pathway overlap rather than evidence that this module specifically causes those diseases.

**Cell composition.** The module is overwhelmingly composed of secreted or plasma-associated proteins. HPA classifies nearly all genes as secreted, and the module is strongly liver-enriched, with hepatocytes the dominant single-cell source. Most genes are not detected in immune cells, so the pattern is more consistent with circulating liver-derived proteins than with a blood-leukocyte transcriptional module. A smaller subset has immune-cell enrichment or enhancement, including C3, C4BPA, SERPING1, C8B, SERPINF2, APOD and A2M, while A2M and C4BPA have lung protein detection and several complement genes have alveolar or lung-associated single-cell annotations. The shared circulatory-system and lung signal therefore could reflect plasma protein abundance in tissue samples, vascular or blood content, and a limited contribution from lung cells, rather than a lung-specific resident program. The lipoprotein genes APOA2, APOA4, APOC3, APOD, LPA and SAA4 further support a plasma-lipoprotein component.

**GO/KEGG enrichment**: 83 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 1.33e-18 | A1BG, A2M, APOA2, APOA4, C3, C4BPA, C8A, C9, CFB, CFH, CP, CPN2, GC, ITIH1, ITIH2, ITIH4, KNG1, PLG, SERPINF2, SERPING1 |
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 1.01e-16 | A2M, C3, C4BPA, C5, C6, C7, C8A, C8B, C9, CFB, CFH, CFI, KNG1, PLG, SERPINF2, SERPING1 |
| GO:CC extracellular space | 3.23e-15 | A1BG, A2M, APOA2, APOA4, APOC3, APOD, AZGP1, C3, C4BPA, C5, C6, C7, C8A, C8B, C9, CA1, CFB, CFH, CFI, CP, CPN2, FBN1, GC, ITIH1, ITIH2, ITIH3, ITIH4, KNG1, LPA, PLG, RBP4, SAA4, SERPINF2, SERPING1 |
| GO:BP complement activation | 1.07e-14 | A2M, C3, C4BPA, C5, C6, C7, C8A, C8B, C9, CFB, CFH, CFI, SERPING1 |
| GO:CC extracellular region | 4.6e-14 | A1BG, A2M, APOA2, APOA4, APOC3, APOD, AZGP1, C3, C4BPA, C5, C6, C7, C8A, C8B, C9, CA1, CFB, CFH, CFI, CP, CPN2, FBN1, GC, ITIH1, ITIH2, ITIH3, ITIH4, KNG1, LPA, PLG, RBP4, SAA4, SERPINF2, SERPING1 |
| GO:CC extracellular exosome | 4.8e-12 | A1BG, A2M, APOA2, APOA4, APOC3, APOD, AZGP1, C3, C5, C6, C7, C8A, C8B, C9, CA1, CFB, CFH, CFI, CP, CPN2, GC, ITIH1, ITIH2, ITIH3, ITIH4, KNG1, PLG, RBP4, SAA4, SERPINF2, SERPING1 |
| GO:CC extracellular organelle | 5.47e-12 | A1BG, A2M, APOA2, APOA4, APOC3, APOD, AZGP1, C3, C5, C6, C7, C8A, C8B, C9, CA1, CFB, CFH, CFI, CP, CPN2, GC, ITIH1, ITIH2, ITIH3, ITIH4, KNG1, PLG, RBP4, SAA4, SERPINF2, SERPING1 |
| GO:CC extracellular membrane-bounded organelle | 5.47e-12 | A1BG, A2M, APOA2, APOA4, APOC3, APOD, AZGP1, C3, C5, C6, C7, C8A, C8B, C9, CA1, CFB, CFH, CFI, CP, CPN2, GC, ITIH1, ITIH2, ITIH3, ITIH4, KNG1, PLG, RBP4, SAA4, SERPINF2, SERPING1 |
| GO:CC extracellular vesicle | 5.47e-12 | A1BG, A2M, APOA2, APOA4, APOC3, APOD, AZGP1, C3, C5, C6, C7, C8A, C8B, C9, CA1, CFB, CFH, CFI, CP, CPN2, GC, ITIH1, ITIH2, ITIH3, ITIH4, KNG1, PLG, RBP4, SAA4, SERPINF2, SERPING1 |
| GO:BP complement activation, alternative pathway | 6.18e-11 | C3, C5, C7, C8A, C8B, C9, CFB, CFH |
| GO:BP humoral immune response | 1.03e-10 | A2M, C3, C4BPA, C5, C6, C7, C8A, C8B, C9, CFB, CFH, CFI, SERPING1 |
| GO:BP complement activation, classical pathway | 1.78e-10 | C3, C4BPA, C5, C6, C7, C8A, C8B, C9, CFI, SERPING1 |
| GO:BP humoral immune response mediated by circulating immunoglobulin | 7.02e-10 | C3, C4BPA, C5, C6, C7, C8A, C8B, C9, CFI, SERPING1 |
| GO:BP immune effector process | 1.62e-08 | A2M, APOA2, AZGP1, C3, C4BPA, C5, C6, C7, C8A, C8B, C9, CFB, CFH, CFI, RBP4, SERPING1 |
| GO:MF endopeptidase inhibitor activity | 2.9e-08 | A2M, C3, C5, ITIH1, ITIH2, ITIH3, ITIH4, KNG1, LPA, SERPINF2, SERPING1 |

### STRING and hu.MAP

STRING provides extensive known support for the module's internal organization. The complement arm is connected through C3, CFB, CFH, CFI, C5 and the terminal components C6, C7, C8A, C8B and C9. The inhibitor and fibrinolysis arm is connected through A2M, SERPING1, KNG1, PLG and SERPINF2, while the lipoprotein arm is connected through APOA2, APOA4, APOC3, APOD, LPA and SAA4. The STRING functional results are supplementary and concordant with this interpretation, especially the secreted, signal-peptide, extracellular, blood-microparticle and complement/coagulation annotations (9 supplementary STRING terms; within-query FDR 7.28e-33–2.4e-18). They are not being treated as globally corrected enrichment evidence. hu.MAP independently places many of the same proteins in recurring plasma-protein and complement-associated complexes, including complexes containing C3, CFB, C5, CP, PLG, A2M, KNG1, complement regulators, apolipoproteins and inter-alpha-trypsin-inhibitor proteins (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_00178.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_02236.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07119.1) (hu.MAP huMAP3_08700.1). Additional complexes connect terminal complement proteins with regulatory and fibrinolytic proteins (hu.MAP huMAP3_14445.1) (hu.MAP huMAP3_14656.1) (hu.MAP huMAP3_08889.1) (hu.MAP huMAP3_14295.1) (hu.MAP huMAP3_11660.1). Thus, much of the module reflects known physical or functional protein organization, although co-abundance edges do not by themselves prove direct binding or biochemical interaction.

**STRING interactions (score >= 0.7)**: 73 of 561 gene pairs: A2M–APOA2 (0.772); A2M–CFB (0.726); A2M–CP (0.889); A2M–KNG1 (0.927); A2M–PLG (0.779); A2M–SERPINF2 (0.968); A2M–SERPING1 (0.905); APOA2–APOA4 (0.994); APOA2–APOC3 (0.999); APOA2–APOD (0.993); APOA2–GC (0.765); APOA2–LPA (0.977); APOA2–SAA4 (0.816); APOA4–APOC3 (0.999); APOA4–APOD (0.864); APOA4–LPA (0.887); APOA4–SAA4 (0.757); APOC3–APOD (0.777); APOC3–LPA (0.957); APOC3–SAA4 (0.799); APOD–AZGP1 (0.707); AZGP1–GC (0.823); AZGP1–RBP4 (0.746); C3–C4BPA (0.817); C3–C5 (0.974); C3–C8A (0.816); C3–C8B (0.736); C3–CFB (0.999); C3–CFH (0.999); C3–CFI (0.999); C3–CP (0.751); C3–GC (0.768); C3–ITIH4 (0.745); C3–KNG1 (0.804); C3–PLG (0.978); C3–SERPING1 (0.954); C4BPA–CFI (0.816); C5–C6 (0.999); C5–C7 (0.999); C5–C8A (0.999); C5–C8B (0.999); C5–C9 (0.999); C5–CFB (0.774); C5–CFH (0.824); C5–KNG1 (0.701); C5–PLG (0.725); C6–C7 (0.995); C6–C8A (0.985); C6–C8B (0.984); C6–C9 (0.996); C7–C8A (0.984); C7–C8B (0.991); C7–C9 (0.986); C8A–C8B (0.999); C8A–C9 (0.997); C8B–C9 (0.989); C9–CFI (0.707); C9–PLG (0.757); CFB–CFH (0.961); CFB–CFI (0.97); CFB–SERPING1 (0.88); CFH–CFI (0.999); CFH–SERPING1 (0.722); GC–PLG (0.719); GC–RBP4 (0.749); ITIH1–ITIH2 (0.835); ITIH1–ITIH3 (0.724); ITIH2–ITIH3 (0.787); ITIH4–KNG1 (0.723); ITIH4–PLG (0.715); KNG1–PLG (0.898); KNG1–SERPING1 (0.964); PLG–SERPINF2 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 7.28e-33, 28 genes); Keyword Secreted (FDR = 3.88e-32, 32 genes); Keyword Signal (FDR = 3.38e-29, 33 genes); NetworkNeighborAL Complement and coagulation cascades, and Protein-lipid complex (FDR = 4.21e-28, 24 genes); COMPARTMENTS Extracellular region (FDR = 1.46e-24, 33 genes); Keyword Glycoprotein (FDR = 6.62e-23, 31 genes); Keyword Disulfide bond (FDR = 1.11e-21, 29 genes); NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization (FDR = 1.32e-21, 19 genes); COMPARTMENTS Blood microparticle (FDR = 4.32e-21, 20 genes); PMID (2022) The Aging Features of Thyrotoxicosis Mice: Malnutrition, Immunosenescence and Lipotoxicity. (FDR = 6.49e-21, 19 genes); Component Blood microparticle (FDR = 7.79e-21, 20 genes); COMPARTMENTS Extracellular space (FDR = 1.1e-20, 28 genes); NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization (FDR = 2.61e-20, 18 genes); PMID (2020) Revelation of Proteomic Indicators for Colorectal Cancer in Initial Stages of Development. (FDR = 7.23e-20, 19 genes); KEGG Complement and coagulation cascades (FDR = 2.4e-18, 16 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10678.1 (CP, PLG, CFB, A2M, C3, C5, KNG1, APOA2, APOC3, GC, C4BPA, A1BG, SERPING1, APOA4, CFH, ITIH2, ITIH1, ITIH4; 18/71); huMAP3_09531.1 (CP, PLG, CFB, A2M, C3, C5, KNG1, APOA2, APOC3, C4BPA, A1BG, SERPING1, APOA4, ITIH2, ITIH1, SAA4, ITIH4; 17/47); huMAP3_10101.1 (CP, PLG, CFB, A2M, C3, C5, KNG1, APOA2, APOC3, C4BPA, A1BG, SERPING1, APOA4, ITIH2, ITIH1, SAA4, ITIH4; 17/49); huMAP3_15040.1 (CP, PLG, CFB, A2M, C3, KNG1, APOA2, APOC3, GC, C4BPA, A1BG, SERPING1, APOA4, CFH, ITIH2, ITIH1, ITIH4; 17/64); huMAP3_08395.1 (CP, PLG, CFB, A2M, C3, C5, KNG1, APOA2, APOC3, C4BPA, A1BG, APOA4, ITIH2, ITIH1, SAA4; 15/43); huMAP3_09273.1 (CP, PLG, CFB, A2M, KNG1, APOA2, APOC3, C4BPA, SERPING1, ITIH2, ITIH1, SAA4; 12/28); huMAP3_08796.1 (PLG, CFB, C5, APOC3, RBP4, C4BPA, ITIH1, SAA4, ITIH4; 9/15); huMAP3_09832.1 (PLG, CFB, C5, APOC3, RBP4, C4BPA, ITIH1, SAA4, ITIH4; 9/18); huMAP3_07701.1 (PLG, CFB, A2M, KNG1, APOC3, C4BPA, ITIH2, ITIH1, SAA4; 9/22); huMAP3_07541.1 (A2M, C5, KNG1, APOC3, C4BPA, ITIH2, ITIH1, SAA4; 8/19); huMAP3_07265.1 (CP, A2M, KNG1, APOA2, A1BG, APOA4, ITIH2; 7/20); huMAP3_00178.1 (C5, APOC3, RBP4, SERPINF2, ITIH1, SAA4; 6/9); huMAP3_09434.1 (C3, C5, GC, A1BG, APOA4, ITIH4; 6/33); huMAP3_02236.1 (CP, KNG1, APOA2, A1BG, ITIH2; 5/7); huMAP3_07432.1 (CP, C3, APOA2, A1BG, APOA4; 5/18); huMAP3_07119.1 (C5, RBP4, SERPINF2, SAA4; 4/6); huMAP3_08700.1 (CP, APOA2, A1BG, APOA4; 4/11); huMAP3_14445.1 (CFI, C8A, SERPINF2, C6; 4/18); huMAP3_14656.1 (CFI, C8A, SERPINF2, C6; 4/21); huMAP3_05943.1 (RBP4, SERPINF2, SAA4; 3/6); huMAP3_06190.1 (PLG, APOC3, ITIH1; 3/6); huMAP3_06724.1 (CFB, APOC3, ITIH1; 3/6); huMAP3_02811.1 (C5, C4BPA, ITIH1; 3/8); huMAP3_08224.1 (C3, C5, GC; 3/21); huMAP3_08889.1 (SERPING1, SERPINF2; 2/3); huMAP3_00961.1 (APOC3, ITIH1; 2/4); huMAP3_07376.1 (C5, C4BPA; 2/4); huMAP3_09391.1 (APOC3, ITIH1; 2/5); huMAP3_06018.1 (APOC3, ITIH1; 2/6); huMAP3_07064.1 (APOC3, ITIH1; 2/6); huMAP3_07603.1 (APOC3, ITIH1; 2/6); huMAP3_10426.1 (APOC3, ITIH1; 2/6); huMAP3_02242.1 (C3, APOA4; 2/9); huMAP3_14295.1 (CFI, SAA4; 2/38); huMAP3_11660.1 (C8A, SERPINF2; 2/43)

### Novelty

This should not be claimed as a wholly new complement, coagulation or plasma-protein mechanism. The core relationships are already represented in STRING, hu.MAP, curated pathway annotations and extensive disease literature, particularly for C3, CFB, CFH, CFI, C5, the terminal complement components, A2M, PLG and SERPING1. The potentially novel result is the conserved co-abundance organization of this combined complement, protease-control, fibrinolytic, lipoprotein and extracellular-matrix program across circulatory_system and lung. That module-level conservation may be useful as a systems-level observation, but the fact sheet does not establish that it has not previously been reported in another cohort or analysis. Absence of a STRING interaction or hu.MAP membership for genes such as LPA, AZGP1, FBN1 or A1BG would not establish novelty, because co-abundance can arise from shared secretion, tissue composition, plasma carryover or coordinated regulation rather than a previously unrecognized physical interaction.

**Hypothesis.** Hypothesis: the module represents a liver-derived plasma program that is carried into, or sampled with, both circulation and lung tissue. In this model, complement components provide innate immune surveillance and membrane-attack capacity; CFB supports alternative-pathway amplification; CFH, CFI, C4BPA, SERPING1 and A2M restrain excessive activation; PLG, KNG1 and SERPINF2 couple the program to fibrinolysis, kinin biology and protease control; and apolipoproteins and LPA couple inflammatory surveillance to lipid particles. Inter-alpha-trypsin-inhibitor proteins may stabilize hyaluronan-rich extracellular matrices, potentially helping coordinate vascular or alveolar extracellular environments. This is a mechanistic hypothesis, not a demonstrated causal model. It should be tested by measuring plasma contamination, cell-type composition, protein abundance and activation fragments separately in paired circulation and lung samples.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): SERPING1 (0.87), CP (0.86), CFB (0.82); STRING partners: C4BPA (0.817), C5 (0.974), C8A (0.816), C8B (0.736), CFB (0.999), CFH (0.999), CFI (0.999), CP (0.751), GC (0.768), ITIH4 (0.745), KNG1 (0.804), PLG (0.978), SERPING1 (0.954)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_08395.1, huMAP3_09434.1, huMAP3_07432.1, huMAP3_08224.1, huMAP3_02242.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a central network bridge linking CFB, CFH, CFI, C5, SERPING1, PLG and other module proteins. It appears across the complement, humoral immunity, innate immunity, immune-effector and membrane-attack annotations (18 globally significant GO/KEGG terms, q_global 1.01e-16–0.000192; see the table). STRING supports its relationships with both activators and regulators, and hu.MAP places it in multiple high-confidence plasma and complement complexes (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_02242.1). Its established disease associations include complement deficiency, atypical hemolytic-uremic syndrome, age-related macular degeneration and complement-mediated glomerulopathy. It also has exceptionally extensive literature support.
- **Conclusion**: Established conclusion: C3 is the strongest functional anchor for the module's complement interpretation and a plausible abundance hub. Hypothesis: coordinated C3 abundance may mark the balance between complement activation and inhibition in the sampled circulation and lung environment; this requires direct measurement of activation products rather than total C3 alone.

#### CFB

- **Related proteins** (co-abundance neighbors): C3 (0.82), CFH (0.82), PLG (0.81), CP (0.80); STRING partners: A2M (0.726), C3 (0.999), C5 (0.774), CFH (0.961), CFI (0.97), SERPING1 (0.88)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_08395.1, huMAP3_09273.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07701.1, huMAP3_06724.1
- **Function (MyGene.info)**: complement factor B. This gene encodes complement factor B, a component of the alternative pathway of complement activation. Factor B circulates in the blood as a single chain polypeptide. Upon activation of the alternative pathway, it is cleaved by complement factor D yielding the noncatalytic chain Ba and the catalytic subunit Bb. The active subunit Bb is a serine protease which associates with C3b to form the alter…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with B factor anomaly (0.764); atypical hemolytic-uremic syndrome (0.705); Immunodeficiency due to a complement cascade protein anomaly (0.614); paroxysmal nocturnal hemoglobinuria (0.561); complement 3 glomerulopathy (0.546)
- **Europe PMC papers**: 7226
- **Why important**: CFB connects C3 with CFH, CFI, SERPING1 and PLG in the module and is annotated as a component of the alternative complement pathway (6 globally significant GO/KEGG terms, q_global 1.01e-16–0.000192; see the table). Its STRING relationships are especially coherent with the complement core, and it occurs in many hu.MAP plasma-protein complexes (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_06724.1) (hu.MAP huMAP3_14295.1). Established disease associations include atypical hemolytic-uremic syndrome, complement-mediated glomerulopathy, paroxysmal nocturnal hemoglobinuria and complement immunodeficiency. Its literature base is substantial.
- **Conclusion**: Established conclusion: CFB provides strong support for an alternative-pathway component rather than a generic inflammatory signal. Hypothesis: variation in the CFB-centered branch could influence the degree of complement amplification in lung-associated plasma, but the co-abundance data cannot determine pathway activity or direction.

#### CFH

- **Related proteins** (co-abundance neighbors): LPA (0.90), CFB (0.82), GC (0.82); STRING partners: C3 (0.999), C5 (0.824), CFB (0.961), CFI (0.999), SERPING1 (0.722)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_15040.1
- **Function (MyGene.info)**: complement factor H. This gene is a member of the Regulator of Complement Activation (RCA) gene cluster and encodes a protein with twenty short consensus repeat (SCR) domains. This protein is secreted into the bloodstream and has an essential role in the regulation of complement activation, restricting this innate defense mechanism to microbial infections. Mutations in this gene have been associated with hemolytic-ure…
- **Diseases (Open Targets)**: complement factor H deficiency (0.769); age-related macular degeneration (0.750); atypical hemolytic-uremic syndrome (0.729); age related macular degeneration 4 (0.711); Doyne honeycomb retinal dystrophy (0.688)
- **Europe PMC papers**: 9287
- **Why important**: CFH is a key regulator positioned with C3, CFB and CFI, and it is included in the alternative-pathway, complement-regulation and negative-regulation annotations (8 globally significant GO/KEGG terms, q_global 1.01e-16–0.0295; see the table). STRING shows strong relationships with the complement core, while hu.MAP places CFH in several plasma and complement complexes (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_15040.1). HPA supports a liver-derived secreted protein with fibroblast and hepatic-stellate-cell enhancement. Established disease associations include factor H deficiency, atypical hemolytic-uremic syndrome and age-related macular degeneration.
- **Conclusion**: Established conclusion: CFH is the principal counter-regulatory marker selected here and helps distinguish a regulated complement program from unrestrained activation. Hypothesis: the balance between CFH and alternative-pathway activators may be particularly relevant to whether this shared module reflects homeostatic plasma surveillance or lung-associated injury.

#### A2M

- **Related proteins** (co-abundance neighbors): APOC3 (0.86), CA1 (0.85), LPA (0.82), ITIH4 (0.81), CP (0.81), GC (0.81), RBP4 (0.80); STRING partners: APOA2 (0.772), CFB (0.726), CP (0.889), KNG1 (0.927), PLG (0.779), SERPINF2 (0.968), SERPING1 (0.905)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_08395.1, huMAP3_09273.1, huMAP3_07701.1, huMAP3_07541.1, huMAP3_07265.1
- **Function (MyGene.info)**: alpha-2-macroglobulin. The protein encoded by this gene is a protease inhibitor and cytokine transporter. It uses a bait-and-trap mechanism to inhibit a broad spectrum of proteases, including trypsin, thrombin and collagenase. It can also inhibit inflammatory cytokines, and it thus disrupts inflammatory cascades. Mutations in this gene are a cause of alpha-2-macroglobulin deficiency. This gene is implicated in Alzheimer…
- **Diseases (Open Targets)**: myopia (0.206); refractive error (0.151); primary angle-closure glaucoma (0.148); Abnormality of refraction (0.144); Aganglionic megacolon (0.118)
- **Europe PMC papers**: 5133
- **Why important**: A2M occupies a central position connecting protease inhibitors, complement regulators, kininogen, plasminogen, ceruloplasmin and lipoprotein-associated proteins. It supports globally corrected terms for complement regulation, immune effector processes, endopeptidase inhibition and extracellular or blood-microparticle localization (9 globally significant GO/KEGG terms, q_global 1.33e-18–0.0295; see the table). STRING and hu.MAP repeatedly connect it to the plasma-protein complexes (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_07265.1). It is secreted to blood, has lung tissue enhancement and lung protein detection, and is associated with protease inhibition, cytokine transport and regulation of inflammatory cascades. Its disease and biomedical literature support is broad.
- **Conclusion**: Established conclusion: A2M is the best candidate for linking complement control to broad extracellular protease and inflammatory regulation in this module. Hypothesis: its lung-associated signal could represent a local or vascular buffering response, but plasma origin and tissue carryover remain competing explanations.

#### PLG

- **Related proteins** (co-abundance neighbors): CFB (0.81), ITIH2 (0.81); STRING partners: A2M (0.779), C3 (0.978), C5 (0.725), C9 (0.757), GC (0.719), ITIH4 (0.715), KNG1 (0.898), SERPINF2 (0.999)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_08395.1, huMAP3_09273.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07701.1, huMAP3_06190.1
- **Function (MyGene.info)**: plasminogen. The plasminogen protein encoded by this gene is a serine protease that circulates in blood plasma as an inactive zymogen and is converted to the active protease, plasmin, by several plasminogen activators such as tissue plasminogen activator (tPA), urokinase plasminogen activator (uPA), kallikrein, and factor XII (Hageman factor). The conversion of plasminogen to plasmin involves the cleavage of t…
- **Diseases (Open Targets)**: hypoplasminogenemia (0.813); hereditary angioedema (0.737); hemorrhage (0.605); dysplasminogenemia (0.598); Menorrhagia (0.579)
- **Europe PMC papers**: 17740
- **Why important**: PLG links the complement network to fibrinolysis, extracellular-matrix disassembly and proteolysis. It connects with C3, CFB, C5, C9, KNG1, GC, A2M and SERPINF2 in STRING and appears in numerous hu.MAP plasma complexes (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_06190.1). It supports the complement/coagulation, blood-microparticle and extracellular terms (11 globally significant GO/KEGG terms, q_global 1.33e-18–0.00863; see the table). Its established functions include conversion to plasmin, fibrinolysis and extracellular-matrix remodeling, with disease associations including hypoplasminogenemia, hereditary angioedema, hemorrhage and dysplasminogenemia. It has a substantial literature base.
- **Conclusion**: Established conclusion: PLG provides the clearest bridge from complement and plasma immunity to clot remodeling and extracellular matrix turnover. Hypothesis: coordinated PLG and SERPINF2 abundance may tune proteolytic remodeling near lung vasculature, but activation state cannot be inferred from abundance alone.

## Module 1

**Tissue pair**: circulatory_system and lung  
**Genes (38)**: ACIN1, AFG2B, AMPD2, ANAPC5, ASCC2, ATRX, CLTB, CNOT3, CRIPT, EHMT1, ELP2, EPS15L1, ERCC1, EZH2, FIP1L1, GCC2, INTS13, KIF13B, KIF14, KNTC1, MAD1L1, CHCHD6, NAA35, NCOA3, NIT1, OSBPL11, PCF11, PELO, PPIG, PRRC2A, PRRC2C, PTPRJ, PYM1, RBBP6, SEC16A, TP53BP1, ZC3H13, ZMYND8

### Function

This module most plausibly represents a coordinated nuclear gene-expression and RNA-maturation program, with additional links to chromatin regulation, genome surveillance, cell-cycle control, and membrane trafficking. The strongest coherent signal is post-transcriptional RNA handling: FIP1L1 and PCF11 participate in messenger-RNA cleavage and polyadenylation, ACIN1 participates in RNA splicing and the exon-junction complex, PYM1 supports exon-junction-complex disassembly and messenger-RNA surveillance, and RBBP6 participates in messenger-RNA processing and co-transcriptional three-prime end processing. This interpretation is supported by the supplementary STRING term (STRING KEGG mRNA surveillance pathway; within-query FDR = 0.0156), but no GO or KEGG term passed global correction, so there is no globally significant GO/KEGG enrichment to report. The module also contains chromatin regulators and DNA-damage factors, including EHMT1, ATRX, EZH2, TP53BP1, and ERCC1, as well as vesicle and endocytic components such as SEC16A, CLTB, and EPS15L1. The network therefore appears functionally mixed but biologically connected through gene-expression control, stress or damage responses, and cellular transport.

**Cell composition.** The module is not dominated by plasma or secreted proteins: HPA identifies only PTPRJ as secreted to blood, while the other annotated proteins are intracellular or membrane-associated. Most genes have low tissue specificity, and most have low immune-cell specificity, which argues against interpreting the module primarily as a plasma-protein signature or a simple blood-cell contamination signal. Nevertheless, HPA shows cell-type-enhanced expression in many genes, with neutrophils and neutrophil progenitors recurring among the enriched cell types, alongside epithelial, reproductive, progenitor, and plasma-cell annotations. AMPD2 has group-enriched blood-cell expression, PTPRJ is immune-cell enhanced for neutrophils, and several genes are enhanced in hematopoietic or megakaryocytic populations. Thus, shared cell types or sample-composition effects cannot be excluded, particularly for the circulatory_system component. The broad tissue distribution and intracellular localization instead favor a general cellular program that may be modulated by the cell populations represented in both tissues. Lung protein detection is present for most genes, whereas the circulatory_system summary has no matching HPA tissue entry, so the tissue-level comparison should be interpreted cautiously.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a compact set of established relationships rather than dense coverage of the module. The clearest known RNA-processing relationships are the high-confidence links among FIP1L1, PCF11, and RBBP6, and these genes also support the supplementary mRNA-surveillance term (STRING KEGG mRNA surveillance pathway; within-query FDR = 0.0156) together with ACIN1 and PYM1. Other known STRING relationships connect ATRX with EZH2 and TP53BP1, ERCC1 with TP53BP1, MAD1L1 with ANAPC5, and CLTB with EPS15L1. hu.MAP independently places PPIG, FIP1L1, RBBP6, PYM1, and ACIN1 in a large RNA-processing and splicing-associated complex (hu.MAP huMAP3_11073.1), with overlapping complexes (hu.MAP huMAP3_09587.1), (hu.MAP huMAP3_10564.1), (hu.MAP huMAP3_09621.1), (hu.MAP huMAP3_09943.1), (hu.MAP huMAP3_06219.1), (hu.MAP huMAP3_09490.1), (hu.MAP huMAP3_09637.1), (hu.MAP huMAP3_06097.1), (hu.MAP huMAP3_08467.1), and (hu.MAP huMAP3_10789.1). SEC16A, CLTB, and EPS15L1 recur in vesicle-trafficking and endocytic complexes (hu.MAP huMAP3_10762.1) and (hu.MAP huMAP3_12394.1), while ATRX and EHMT1 occur in a chromatin-associated complex (hu.MAP huMAP3_11539.1), and EZH2 and EHMT1 in a chromatin-regulatory complex (hu.MAP huMAP3_15128.1). The module therefore contains several independently supported molecular neighborhoods, but many module edges are not represented by high-confidence STRING interactions or hu.MAP complexes. Co-abundance should consequently be treated as evidence of coordinated regulation or shared cellular context, not as proof of direct physical interaction.

**STRING interactions (score >= 0.7)**: 8 of 703 gene pairs: ANAPC5–MAD1L1 (0.753); ATRX–EZH2 (0.933); ATRX–TP53BP1 (0.742); CLTB–EPS15L1 (0.721); ERCC1–TP53BP1 (0.835); FIP1L1–PCF11 (0.976); FIP1L1–RBBP6 (0.978); PCF11–RBBP6 (0.917)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG mRNA surveillance pathway (FDR = 0.0156, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11073.1 (PPIG, FIP1L1, RBBP6, PYM1, ACIN1; 5/67); huMAP3_09587.1 (PPIG, FIP1L1, RBBP6; 3/21); huMAP3_10564.1 (PPIG, RBBP6, ACIN1; 3/37); huMAP3_09621.1 (PPIG, RBBP6, ACIN1; 3/56); huMAP3_10762.1 (SEC16A, CLTB, EPS15L1; 3/62); huMAP3_09943.1 (PPIG, RBBP6, ACIN1; 3/78); huMAP3_12394.1 (SEC16A, CLTB, EPS15L1; 3/98); huMAP3_08887.1 (PRRC2A, PRRC2C; 2/2); huMAP3_07405.1 (SEC16A, CLTB; 2/3); huMAP3_05708.1 (PYM1, MAD1L1; 2/6); huMAP3_06219.1 (PPIG, ACIN1; 2/7); huMAP3_09490.1 (FIP1L1, RBBP6; 2/9); huMAP3_07733.1 (PYM1, MAD1L1; 2/9); huMAP3_08744.1 (SEC16A, CLTB; 2/20); huMAP3_09637.1 (PPIG, ACIN1; 2/21); huMAP3_06097.1 (PPIG, ACIN1; 2/22); huMAP3_08467.1 (PPIG, RBBP6; 2/22); huMAP3_11539.1 (ATRX, EHMT1; 2/32); huMAP3_10789.1 (PPIG, PYM1; 2/37); huMAP3_12918.1 (SEC16A, EPS15L1; 2/62); huMAP3_15128.1 (EZH2, EHMT1; 2/96)

### Novelty

The module should not be called a wholly new molecular system. Its component processes and several relationships are already established by STRING, hu.MAP, and gene-level functional annotations, especially RNA processing, mRNA surveillance, chromatin regulation, DNA damage response, and endocytic trafficking. At the same time, the particular co-abundance configuration shared by circulatory_system and lung may be novel or under-described, because the supplied evidence does not identify a previously named module with this exact cross-tissue membership and organization. The absence of a STRING or hu.MAP relationship for many edges does not establish novelty; it may reflect incomplete interaction coverage, indirect regulation, shared cell composition, or co-expression driven by a common state. A defensible conclusion is that this is a potentially novel cross-tissue co-abundance pattern assembled from largely known cellular programs, requiring replication in independent cohorts and cell-resolved data before being claimed as a new biological mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared state of transcriptional and post-transcriptional quality control in cells represented in both circulation and lung. Coordinated activity of FIP1L1, PCF11, RBBP6, ACIN1, and PYM1 could couple messenger-RNA cleavage, splicing, exon-junction-complex turnover, and surveillance, while EHMT1, ATRX, and EZH2 could regulate the chromatin environment in which these transcriptional programs operate. SEC16A, CLTB, and EPS15L1 may connect this nuclear program to secretory or endocytic trafficking, perhaps during cellular stress, differentiation, or turnover. The neutrophil and progenitor-associated HPA pattern raises the alternative possibility that the signal is partly driven by shared hematopoietic or immune-cell composition rather than by a universal tissue-cell mechanism. This hypothesis predicts that the module will track RNA-processing and stress-response states within matched cell types, and that its apparent cross-tissue conservation will weaken after strict cell-composition adjustment if the signal is mainly compositional.

### Important genes

#### EHMT1

- **Related proteins** (co-abundance neighbors): PPIG (0.89), SEC16A (0.89), ACIN1 (0.86), FIP1L1 (0.84), EPS15L1 (0.83), NIT1 (0.83), PRRC2C (0.81), CNOT3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_11539.1, huMAP3_15128.1
- **Function (MyGene.info)**: euchromatic histone lysine methyltransferase 1. The protein encoded by this gene is a histone methyltransferase that methylates the lysine-9 position of histone H3. This action marks the genomic region packaged with these methylated histones for transcriptional repression. This protein may be involved in the silencing of MYC- and E2F-responsive genes and therefore could play a role in the G0/G1 cell cycle transition. Defects in this gene are a …
- **Diseases (Open Targets)**: Kleefstra syndrome 1 (0.748); Kleefstra syndrome (0.677); hereditary disease (0.547); Intellectual disability (0.514); Kleefstra syndrome due to 9q34 microdeletion (0.462)
- **Europe PMC papers**: 2274
- **Why important**: EHMT1 has the strongest weighted network position in the supplied module and connects RNA-processing-associated genes, SEC16A, EPS15L1, NIT1, PRRC2C, and CNOT3. Its established function is histone H3 lysine-nine methylation and transcriptional repression, with roles in chromatin organization and epigenetic regulation. It is represented in hu.MAP chromatin-related complexes (hu.MAP huMAP3_11539.1) and (hu.MAP huMAP3_15128.1), but lacks a STRING partner in this module. Its disease associations include Kleefstra syndrome and intellectual disability, and the literature volume is substantial.
- **Conclusion**: Established evidence supports EHMT1 as a central chromatin regulator and a network bridge between otherwise distinct module neighborhoods. Its high co-abundance connectivity suggests coordinated regulation, but does not establish direct physical coupling to the RNA-processing or trafficking proteins. A plausible interpretation is that EHMT1 marks a transcriptional-state component of the module rather than the sole driver of its function.

#### FIP1L1

- **Related proteins** (co-abundance neighbors): EHMT1 (0.84); STRING partners: PCF11 (0.976), RBBP6 (0.978)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_11073.1, huMAP3_09587.1, huMAP3_09490.1
- **Function (MyGene.info)**: factor interacting with PAPOLA and CPSF1. This gene encodes a subunit of the CPSF (cleavage and polyadenylation specificity factor) complex that polyadenylates the 3' end of mRNA precursors. This gene, the homolog of yeast Fip1 (factor interacting with PAP), binds to U-rich sequences of pre-mRNA and stimulates poly(A) polymerase activity. Its N-terminus contains a PAP-binding site and its C-terminus an RNA-binding domain. An interstitial …
- **Diseases (Open Targets)**: cancer (0.465); Abnormality of the skeletal system (0.406); dengue disease (0.370); benign neoplasm of pituitary gland (0.206); response to stimulus (0.198)
- **Europe PMC papers**: 1832
- **Why important**: FIP1L1 is a core RNA-processing candidate: it is a component of the cleavage and polyadenylation machinery, binds RNA, and supports messenger-RNA three-prime end processing. It has strong established STRING relationships with PCF11 and RBBP6 and occurs in hu.MAP complexes (hu.MAP huMAP3_11073.1), (hu.MAP huMAP3_09587.1), and (hu.MAP huMAP3_09490.1). It is also one of the genes in the supplementary mRNA-surveillance term (STRING KEGG mRNA surveillance pathway; within-query FDR = 0.0156). Its disease relevance includes the FIP1L1-PDGFRA fusion and cancer associations, and it has a substantial literature base.
- **Conclusion**: Established evidence makes FIP1L1 one of the best-supported functional anchors of the module, especially for messenger-RNA maturation. The co-abundance pattern may reflect coordinated regulation of RNA three-prime end formation and surveillance, but the module does not by itself show that the encoded proteins assemble into one tissue-specific complex.

#### RBBP6

- **Related proteins** (co-abundance neighbors): PRRC2C (0.85), MAD1L1 (0.81); STRING partners: FIP1L1 (0.978), PCF11 (0.917)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_11073.1, huMAP3_09587.1, huMAP3_10564.1, huMAP3_09621.1, huMAP3_09943.1, huMAP3_09490.1, huMAP3_08467.1
- **Function (MyGene.info)**: RB binding protein 6, ubiquitin ligase. The retinoblastoma tumor suppressor (pRB) protein binds with many other proteins. In various human cancers, pRB suppresses cellular proliferation and is inactivated. Cell cycle-dependent phosphorylation regulates the activity of pRB. This gene encodes a protein which binds to underphosphorylated but not phosphorylated pRB. Multiple alternatively spliced transcript variants that encode different is…
- **Diseases (Open Targets)**: neurodegenerative disease (0.556); Abnormality of the skeletal system (0.555); placental abruption (0.357); retinoschisis (0.230); retinal disorder (0.230)
- **Europe PMC papers**: 748
- **Why important**: RBBP6 occupies a strategically informative position linking PRRC2C and MAD1L1 in the module and has strong STRING links to FIP1L1 and PCF11. It recurs across many hu.MAP RNA-processing complexes, including (hu.MAP huMAP3_11073.1), (hu.MAP huMAP3_09587.1), (hu.MAP huMAP3_10564.1), (hu.MAP huMAP3_09621.1), (hu.MAP huMAP3_09943.1), (hu.MAP huMAP3_09490.1), and (hu.MAP huMAP3_08467.1). Its annotated functions include messenger-RNA processing, co-transcriptional cleavage and polyadenylation, DNA-damage response, ubiquitination, and regulation of DNA replication. It is enhanced in bone marrow and platelets by HPA, and its disease associations include skeletal abnormalities and neurodegenerative disease.
- **Conclusion**: Established evidence supports RBBP6 as a bridge between RNA three-prime end processing and broader genome-maintenance functions. Its repeated complex membership and STRING support make it a strong integrator gene. The platelet and bone-marrow associations raise a composition-related possibility in circulatory samples, but HPA does not support a simple blood-specific interpretation for the entire module.

#### ACIN1

- **Related proteins** (co-abundance neighbors): SEC16A (0.87), EHMT1 (0.86), ANAPC5 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_11073.1, huMAP3_10564.1, huMAP3_09621.1, huMAP3_09943.1, huMAP3_06219.1, huMAP3_09637.1, huMAP3_06097.1
- **Function (MyGene.info)**: apoptotic chromatin condensation inducer 1. Apoptosis is defined by several morphologic nuclear changes, including chromatin condensation and nuclear fragmentation. This gene encodes a nuclear protein that induces apoptotic chromatin condensation after activation by caspase-3, without inducing DNA fragmentation. This protein has also been shown to be a component of a splicing-dependent multiprotein exon junction complex (EJC) that is deposi…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); adolescent idiopathic scoliosis (0.090); hepatocellular carcinoma (0.076); acute lymphoblastic leukemia (0.074); pancreatic neoplasm (0.045)
- **Europe PMC papers**: 894
- **Why important**: ACIN1 connects EHMT1, SEC16A, and ANAPC5 and is repeatedly represented in the large hu.MAP RNA-processing complexes (hu.MAP huMAP3_11073.1), (hu.MAP huMAP3_10564.1), (hu.MAP huMAP3_09621.1), (hu.MAP huMAP3_09943.1), (hu.MAP huMAP3_06219.1), (hu.MAP huMAP3_09637.1), and (hu.MAP huMAP3_06097.1). It has established roles in RNA splicing, the exon-junction complex, apoptotic chromatin condensation, and regulation of apoptosis. It also contributes to the supplementary mRNA-surveillance term (STRING KEGG mRNA surveillance pathway; within-query FDR = 0.0156). Its disease associations include neurodegenerative and neoplastic conditions, and its literature base is substantial.
- **Conclusion**: Established evidence places ACIN1 at the intersection of RNA processing and apoptotic nuclear remodeling. In this module it is more likely to report a shared RNA-quality-control or cell-state program than a tissue-specific secreted function. The apparent link to SEC16A is a co-abundance relationship and should not be interpreted as a direct ACIN1 role in vesicle transport without experimental validation.

#### SEC16A

- **Related proteins** (co-abundance neighbors): EHMT1 (0.89), ACIN1 (0.87), PYM1 (0.84), CLTB (0.82), PRRC2A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_10762.1, huMAP3_12394.1, huMAP3_07405.1, huMAP3_08744.1, huMAP3_12918.1
- **Function (MyGene.info)**: SEC16 homolog A, endoplasmic reticulum export factor. This gene encodes a protein that forms part of the Sec16 complex. This protein has a role in protein transport from the endoplasmic reticulum (ER) to the Golgi and mediates COPII vesicle formation at the transitional ER. Alternative splicing results in multiple transcript variants that encode different protein isoforms. [provided by RefSeq, Feb 2013].
- **Diseases (Open Targets)**: squamous cell carcinoma (0.288); Crohn disease (0.277); bladder calculus (0.241); nephrolithiasis (0.235); actinic keratosis (0.215)
- **Europe PMC papers**: 595
- **Why important**: SEC16A has a high network position and connects EHMT1, ACIN1, PYM1, CLTB, and PRRC2A. Its established function is organization of endoplasmic-reticulum export sites, COPII vesicle formation, ER-to-Golgi transport, and endocytic recycling. It appears in multiple hu.MAP trafficking complexes (hu.MAP huMAP3_10762.1), (hu.MAP huMAP3_12394.1), (hu.MAP huMAP3_07405.1), (hu.MAP huMAP3_08744.1), and (hu.MAP huMAP3_12918.1). HPA indicates low tissue specificity and low cell-type specificity, with lung protein detection, making it a plausible broadly expressed transport component rather than a blood-specific marker. Its disease associations include Crohn disease and epithelial cancer-related conditions.
- **Conclusion**: Established evidence supports SEC16A as the principal membrane-trafficking anchor of the module. Its connection to RNA-processing genes may indicate coordinated cellular logistics during stress, differentiation, or high biosynthetic demand, but this remains a hypothesis. The broad HPA profile favors a general cellular contribution over a specialized circulatory or lung function.

## Module 2

**Tissue pair**: circulatory_system and lung  
**Genes (18)**: AKAP9, CARMIL1, CDK12, CHAMP1, COA7, COG1, CPSF1, CSTF2T, DCTN5, EEF2K, GCC1, LRSAM1, BCKDHB, PCNT, PHACTR4, SVIL, UBA5, ZNF451

### Function

No GO or KEGG term passed global correction, so the module does not have a statistically established pathway annotation from the primary enrichment analysis. Its gene content nevertheless points to a mixed intracellular maintenance program involving cytoskeletal and membrane organization, centrosome and microtubule biology, Golgi trafficking, mitochondrial respiratory-chain assembly, RNA three-prime-end processing, translational control, and protein modification. The co-abundance structure is therefore better interpreted as a coordinated cellular-state module than as evidence for one narrowly defined pathway. The strongest functional themes suggested by individual annotations are cytoskeletal organization and trafficking, with additional links to RNA processing and cellular energy management.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and nearly all have low immune-cell specificity. SVIL is tissue enhanced in skeletal muscle and tongue and immune-cell enriched in neutrophils, while PCNT is tissue enriched in skeletal muscle; other cell-type associations include cardiomyocytes, myonuclei, spermatogenic cells, glial cells, and epithelial populations. Thus, the shared circulatory-system and lung signal is unlikely to be explained simply by a circulating secretome or a broadly blood-cell-enriched program. It may instead reflect conserved intracellular programs present in several structural, contractile, epithelial, or parenchymal cell populations, with a possible contribution from neutrophil-related expression. Lung protein detection is available for most genes, whereas evidence is unavailable or negative for a small subset.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides sparse but informative support. AKAP9 and PCNT have a high-confidence known interaction, consistent with their shared centrosome and microtubule-related functions. CPSF1 and CSTF2T also have a high-confidence known interaction, matching their established roles in the cleavage and polyadenylation machinery. No STRING functional-enrichment result was reported. hu.MAP independently places CPSF1 and CSTF2T together in complexes (hu.MAP huMAP3_09096.1) and (hu.MAP huMAP3_11757.1), strengthening the interpretation that this part of the module captures a known RNA three-prime-end-processing assembly. CARMIL1 and DCTN5 co-occur in hu.MAP complex (hu.MAP huMAP3_12900.1), although only a small portion of that large complex is represented in the module. The remaining module edges and genes lack corresponding high-confidence STRING or multi-member hu.MAP support in the fact sheet. Overall, the network contains several established molecular relationships embedded in a broader co-abundance pattern, rather than a single experimentally confirmed complex.

**STRING interactions (score >= 0.7)**: 2 of 153 gene pairs: AKAP9–PCNT (0.827); CPSF1–CSTF2T (0.964)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09096.1 (CPSF1, CSTF2T; 2/15); huMAP3_11757.1 (CPSF1, CSTF2T; 2/16); huMAP3_12900.1 (CARMIL1, DCTN5; 2/50)

### Novelty

The module should not be presented as a newly discovered molecular complex or as a newly established pathway. Several of its strongest relationships are already known through STRING and hu.MAP, especially the AKAP9–PCNT pair and the CPSF1–CSTF2T RNA-processing pair. At the same time, the particular cross-tissue co-abundance arrangement may be a potentially novel observation because most module edges are not represented by the listed databases. Database absence alone cannot establish novelty, and the lack of globally significant GO or KEGG enrichment limits claims about biological distinctiveness. The defensible conclusion is that the conserved tissue-pair co-abundance pattern is hypothesis-generating and may organize known cellular processes in a previously unreported tissue context, but requires independent replication and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a conserved intracellular homeostasis state that couples cytoskeletal and centrosomal organization with membrane and Golgi trafficking, RNA three-prime-end processing, and metabolic or translational adaptation. In this model, the AKAP9–PCNT axis could coordinate centrosomal and microtubule organization, the CPSF1–CSTF2T pair could represent a linked RNA-processing component, and actin-associated genes such as SVIL and CARMIL1 could connect these processes to cell shape, adhesion, and movement. COA7, BCKDHB, EEF2K, and UBA5 suggest possible contributions from mitochondrial function, nutrient-responsive translation, and protein-modification stress responses. This is a mechanistic hypothesis rather than an established causal pathway; the co-abundance data do not demonstrate physical interaction or directionality among all module members.

### Important genes

#### PCNT

- **Related proteins** (co-abundance neighbors): ZNF451 (0.86), AKAP9 (0.82), COG1 (0.82), CDK12 (0.82); STRING partners: AKAP9 (0.827)
- **HPA**: Tissue enriched; Group enriched; blood Low immune cell specificity; location Centrosome; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pericentrin. The protein encoded by this gene binds to calmodulin and is expressed in the centrosome. It is an integral component of the pericentriolar material (PCM). The protein contains a series of coiled-coil domains and a highly conserved PCM targeting motif called the PACT domain near its C-terminus. The protein interacts with the microtubule nucleation component gamma-tubulin and is likely important to …
- **Diseases (Open Targets)**: microcephalic osteodysplastic primordial dwarfism type II (0.808); hereditary disease (0.526); Insulin resistance (0.469); microcephalic primordial dwarfism (0.380); microcephalic osteodysplastic primordial dwarfism (0.371)
- **Europe PMC papers**: 1285
- **Why important**: PCNT is one of the strongest network-connected genes in the module and links directly to AKAP9, with that relationship supported by STRING. Its established centrosomal localization and roles in microtubule nucleation, mitotic spindle organization, cilium assembly, and intracellular transport make it a plausible structural anchor for the cytoskeletal aspect of the module. HPA identifies skeletal muscle enrichment and myonuclear or thymic myoid associations, and its disease associations include primordial dwarfism and insulin resistance. Its substantial literature supports a well-established biological role.
- **Conclusion**: Established evidence supports PCNT as a centrosome and microtubule organizer and as a known partner of AKAP9. Its position in the module makes it a strong candidate for coordinating the cytoskeletal component, but the module does not establish that PCNT regulates the other genes in this tissue context.

#### AKAP9

- **Related proteins** (co-abundance neighbors): PCNT (0.82), CSTF2T (0.82); STRING partners: PCNT (0.827)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: A-kinase anchoring protein 9. The A-kinase anchor proteins (AKAPs) are a group of structurally diverse proteins which have the common function of binding to the regulatory subunit of protein kinase A (PKA) and confining the holoenzyme to discrete locations within the cell. This gene encodes a member of the AKAP family. Alternate splicing of this gene results in at least two isoforms that localize to the centrosome and the Golg…
- **Diseases (Open Targets)**: cancer (0.547); long QT syndrome 11 (0.501); Prolonged QT interval (0.399); lymphangioma (0.243); hemangioma (0.243)
- **Europe PMC papers**: 1761
- **Why important**: AKAP9 is a highly studied scaffold with a central position linking PCNT and CSTF2T. It localizes to the centrosome and Golgi apparatus and organizes PKA and other signaling proteins. Its annotated roles in microtubule nucleation, centrosome maintenance, protein-complex localization, and signal transduction provide a plausible bridge between cytoskeletal organization and intracellular trafficking. The STRING relationship with PCNT is established, and disease associations include long QT syndrome and prolonged QT interval.
- **Conclusion**: Established evidence supports AKAP9 as a signaling and organelle-localization scaffold, especially for centrosomal and Golgi processes. Its bridge-like placement suggests a possible integrative role in the module, but any connection to RNA processing through CSTF2T remains a hypothesis based on co-abundance rather than demonstrated molecular coupling.

#### CPSF1

- **Related proteins** (co-abundance neighbors): PHACTR4 (0.87); STRING partners: CSTF2T (0.964)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09096.1, huMAP3_11757.1
- **Function (MyGene.info)**: cleavage and polyadenylation specific factor 1. Cleavage and polyadenylation specificity factor (CPSF) is a multisubunit complex that plays a central role in 3-prime processing of pre-mRNAs. CPSF recognizes the AAUAAA signal in the pre-mRNA and interacts with other proteins to facilitate both RNA cleavage and poly(A) synthesis. CPSF1 is the largest subunit of the CPSF complex (Murthy and Manley, 1995 [PubMed 7590244]).[supplied by OMIM, Mar 200…
- **Diseases (Open Targets)**: myopia 27 (0.639); neurodegenerative disease (0.384); dengue disease (0.370); ventricular septal defect (0.298); Alzheimer disease (0.262)
- **Europe PMC papers**: 863
- **Why important**: CPSF1 is a core subunit of the cleavage and polyadenylation specificity factor and is directly paired with CSTF2T in STRING and in hu.MAP complexes (hu.MAP huMAP3_09096.1) and (hu.MAP huMAP3_11757.1). Its established role in recognizing and processing the three-prime ends of pre-mRNAs gives the module a clear RNA-processing component. It also has substantial literature and disease associations including myopia, neurodegenerative disease, dengue disease, ventricular septal defect, and Alzheimer disease.
- **Conclusion**: Established evidence identifies CPSF1 as a core pre-mRNA three-prime-end-processing factor and confirms its molecular association with CSTF2T. Its inclusion indicates that RNA maturation is represented in the module, but there is no evidence that this RNA-processing pair is a globally enriched module function.

#### CSTF2T

- **Related proteins** (co-abundance neighbors): AKAP9 (0.82), UBA5 (0.81); STRING partners: CPSF1 (0.964)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_09096.1, huMAP3_11757.1
- **Function (MyGene.info)**: cleavage stimulation factor subunit 2 tau variant. Enables RNA binding activity. Predicted to be involved in pre-mRNA cleavage required for polyadenylation. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dengue disease (0.370); smoking initiation (0.347); Abnormality of the skeletal system (0.307); laryngeal carcinoma (0.287); breast cancer (0.268)
- **Europe PMC papers**: 341
- **Why important**: CSTF2T is a nuclear RNA-binding factor involved in pre-mRNA cleavage and polyadenylation. It has a strong STRING relationship with CPSF1 and appears with CPSF1 in hu.MAP complexes (hu.MAP huMAP3_09096.1) and (hu.MAP huMAP3_11757.1), making this pair the clearest experimentally supported substructure beyond the AKAP9–PCNT relationship. Its cardiomyocyte cell-type association may also be relevant to the shared circulatory-system and lung context.
- **Conclusion**: Established evidence supports CSTF2T as part of the mRNA three-prime-end-processing machinery and as a partner of CPSF1. Its co-abundance with centrosomal and cytoskeletal genes may reflect a shared cellular state or coordinated regulation, but a direct mechanistic connection to those systems is not established.

#### SVIL

- **Related proteins** (co-abundance neighbors): COA7 (0.83), CARMIL1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: supervillin. This gene encodes a bipartite protein with distinct amino- and carboxy-terminal domains. The amino-terminus contains nuclear localization signals and the carboxy-terminus contains numerous consecutive sequences with extensive similarity to proteins in the gelsolin family of actin-binding proteins, which cap, nucleate, and/or sever actin filaments. The gene product is tightly associated with both a…
- **Diseases (Open Targets)**: myofibrillar myopathy 10 (0.634); neurodegenerative disease (0.402); aortic stenosis (0.376); sialolithiasis (0.323); biliary tract disorder (0.322)
- **Europe PMC papers**: 839
- **Why important**: SVIL has a network connection to both COA7 and CARMIL1 and is the clearest HPA-supported marker of a contractile or cytoskeletal and possible blood-cell contribution. It is tissue enhanced in skeletal muscle and tongue, cell-type enhanced in myonuclei, smooth muscle cells, neutrophils, and related populations, and immune-cell enriched in neutrophils. Its established functions include actin organization, membrane association, actin filament severing and capping, cytokinesis, and skeletal muscle development. It also has disease associations including myofibrillar myopathy and aortic stenosis.
- **Conclusion**: Established evidence supports SVIL as an actin–membrane and muscle-associated cytoskeletal regulator, with a possible neutrophil contribution in tissue samples. It is a plausible contributor to the module's structural component, but the data do not distinguish a shared cell-composition signal from coordinated regulation within cells.

#### COG1

- **Related proteins** (co-abundance neighbors): PHACTR4 (0.83), PCNT (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: component of oligomeric golgi complex 1. The protein encoded by this gene is one of eight proteins (Cog1-8) which form a Golgi-localized complex (COG) required for normal Golgi morphology and function. It is thought that this protein is required for steps in the normal medial and trans Golgi-associated processing of glycoconjugates and plays a role in the organization of the Golgi-localized complex. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: COG1-congenital disorder of glycosylation (0.789); congenital disorder of glycosylation (0.371); dengue disease (0.370); neurodegenerative disease (0.369); hereditary disease (0.194)
- **Europe PMC papers**: 535
- **Why important**: COG1 connects PHACTR4 and PCNT in the module and encodes a component of the oligomeric Golgi complex. Its established functions include Golgi organization, intra-Golgi vesicle transport, and retrograde vesicle recycling, providing a trafficking interpretation for part of the network. Its disease associations include COG1-related congenital disorder of glycosylation and broader congenital glycosylation disorders. Its literature support is substantial relative to many of the less characterized module members.
- **Conclusion**: Established evidence supports COG1 as a Golgi trafficking and glycosylation-related factor. Its network placement suggests that organelle trafficking may connect the cytoskeletal and centrosomal portions of the module, but this proposed connection is inferential and not demonstrated by the available interaction databases.

## Module 3

**Tissue pair**: circulatory_system and lung  
**Genes (20)**: ALB, SERPINC1, APOA1, APOE, CLU, COL1A1, COL1A2, COL4A2, COL6A1, COL6A3, COL18A1, FBLN1, EFEMP1, HBA1, HBB, LAMB2, LUM, NID1, HSPG2, VTN

### Function

This is an extracellular-matrix and basement-membrane module, with the strongest primary evidence from (GO:CC external encapsulating structure; q_global = 2.04e-16), (GO:CC extracellular matrix; q_global = 2.04e-16), (GO:MF extracellular matrix structural constituent; q_global = 3.49e-15), (GO:CC basement membrane; q_global = 2.36e-08), (GO:CC collagen trimer; q_global = 2.67e-08), (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 3.14e-08), and (GO:BP extracellular matrix organization; q_global = 4e-07) (GO:BP extracellular structure organization; q_global = 4e-07) (GO:BP external encapsulating structure organization; q_global = 4e-07). Its genes encode fibrillar and non-fibrillar collagens, laminin-associated proteins, proteoglycans, nidogen, fibulins, and matrix-associated adhesive proteins. The collagen-trimer and tensile-strength annotations in (GO:MF extracellular matrix structural constituent; q_global = 3.49e-15), (GO:MF extracellular matrix structural constituent conferring tensile strength; q_global = 8.93e-09), (GO:CC complex of collagen trimers; q_global = 8.93e-09), and (GO:CC collagen trimer; q_global = 2.67e-08), together with ECM-receptor interaction, integrin signaling, PI3K-Akt signaling, and focal adhesion in (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 3.14e-08), (KEGG Integrin signaling - Homo sapiens (human); q_global = 6.22e-05) (KEGG PI3K-Akt signaling pathway - Homo sapiens (human); q_global = 8.67e-05) (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.000118), support a structural and cell–matrix signaling function. The module also contains a circulating protein and lipoprotein component, supported by (GO:MF lipoprotein particle receptor binding; q_global = 0.00192), (GO:MF amyloid-beta binding; q_global = 0.00251), (GO:BP reverse cholesterol transport; q_global = 0.0181), (GO:MF low-density lipoprotein particle receptor binding; q_global = 0.0247), (GO:BP regulation of phospholipid efflux; q_global = 0.0486), and (GO:BP positive regulation of phospholipid efflux; q_global = 0.0486). Thus, the most conservative interpretation is a vascular and pulmonary extracellular-matrix module with links to basement-membrane integrity, adhesion, lipid transport, coagulation, and tissue remodeling. The visual-perception terms should not be treated as evidence for a visual function; they are plausibly driven by shared matrix genes such as COL18A1, LAMB2, EFEMP1, and LUM.

**Cell composition.** The module is dominated by secreted or extracellular-matrix proteins rather than intracellular housekeeping proteins. HPA classifies most of the genes as secreted, with many directed to the extracellular matrix or blood. The matrix component is enriched in fibroblast-like, hepatic stellate, vascular, alveolar, and other stromal cell contexts, while several soluble proteins are liver-enriched or hepatocyte-associated. APOA1, ALB, VTN, CLU, and SERPINC1 are consistent with plasma or secreted protein carryover, and HBA1 and HBB indicate an erythrocyte or blood-microparticle contribution, also supported by (GO:CC blood microparticle; q_global = 4.2e-05), (GO:CC endocytic vesicle lumen; q_global = 0.00251), (GO:MF oxygen binding; q_global = 0.0181), (GO:BP nitric oxide transport; q_global = 0.0486), and (GO:MF antioxidant activity; q_global = 0.0493). HPA reports that most genes are not detected in immune cells, arguing against a primarily leukocyte-derived module, although selected immune-cell associations remain. Therefore, conservation between circulatory_system and lung may reflect a genuine vascular or stromal ECM program, but it may also be amplified by blood exposure, plasma proteins, or shared stromal cell types. The limited protein detection in lung for several genes further argues against assuming that every module member is produced by lung parenchymal cells.

**GO/KEGG enrichment**: 73 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC external encapsulating structure | 2.04e-16 | APOE, COL18A1, COL1A1, COL1A2, COL4A2, COL6A1, COL6A3, EFEMP1, FBLN1, HSPG2, LAMB2, LUM, NID1, VTN |
| GO:CC extracellular matrix | 2.04e-16 | APOE, COL18A1, COL1A1, COL1A2, COL4A2, COL6A1, COL6A3, EFEMP1, FBLN1, HSPG2, LAMB2, LUM, NID1, VTN |
| GO:MF extracellular matrix structural constituent | 3.49e-15 | COL18A1, COL1A1, COL1A2, COL4A2, COL6A1, COL6A3, EFEMP1, FBLN1, HSPG2, LAMB2, LUM, NID1, VTN |
| GO:CC endoplasmic reticulum lumen | 3.96e-11 | ALB, APOA1, APOE, CLU, COL18A1, COL1A1, COL1A2, COL4A2, COL6A1, COL6A3, LAMB2, SERPINC1, VTN |
| GO:MF structural molecule activity | 8.65e-09 | APOE, COL18A1, COL1A1, COL1A2, COL4A2, COL6A1, COL6A3, EFEMP1, FBLN1, HSPG2, LAMB2, LUM, NID1, VTN |
| GO:MF extracellular matrix structural constituent conferring tensile strength | 8.93e-09 | COL18A1, COL1A1, COL1A2, COL4A2, COL6A1, COL6A3 |
| GO:CC complex of collagen trimers | 8.93e-09 | COL1A1, COL1A2, COL4A2, COL6A1, COL6A3, LUM |
| GO:CC basement membrane | 2.36e-08 | COL18A1, COL4A2, COL6A1, FBLN1, HSPG2, LAMB2, NID1, VTN |
| GO:CC collagen trimer | 2.67e-08 | COL18A1, COL1A1, COL1A2, COL4A2, COL6A1, COL6A3, LUM |
| KEGG ECM-receptor interaction - Homo sapiens (human) | 3.14e-08 | COL1A1, COL1A2, COL4A2, COL6A1, COL6A3, HSPG2, LAMB2, VTN |
| GO:CC extracellular space | 5.97e-08 | ALB, APOA1, APOE, CLU, COL18A1, COL1A1, COL1A2, COL4A2, COL6A1, COL6A3, EFEMP1, FBLN1, HBA1, HBB, HSPG2, LAMB2, LUM, NID1, SERPINC1, VTN |
| GO:CC extracellular region | 2.54e-07 | ALB, APOA1, APOE, CLU, COL18A1, COL1A1, COL1A2, COL4A2, COL6A1, COL6A3, EFEMP1, FBLN1, HBA1, HBB, HSPG2, LAMB2, LUM, NID1, SERPINC1, VTN |
| GO:CC extracellular exosome | 2.67e-07 | ALB, APOA1, APOE, CLU, COL18A1, COL1A2, COL4A2, COL6A1, COL6A3, EFEMP1, FBLN1, HBA1, HBB, HSPG2, LAMB2, LUM, NID1, SERPINC1, VTN |
| GO:CC extracellular organelle | 2.97e-07 | ALB, APOA1, APOE, CLU, COL18A1, COL1A2, COL4A2, COL6A1, COL6A3, EFEMP1, FBLN1, HBA1, HBB, HSPG2, LAMB2, LUM, NID1, SERPINC1, VTN |
| GO:CC extracellular membrane-bounded organelle | 2.97e-07 | ALB, APOA1, APOE, CLU, COL18A1, COL1A2, COL4A2, COL6A1, COL6A3, EFEMP1, FBLN1, HBA1, HBB, HSPG2, LAMB2, LUM, NID1, SERPINC1, VTN |

### STRING and hu.MAP

STRING supports two connected biological neighborhoods. One contains collagen and basement-membrane relationships, including COL1A1–COL1A2, collagen-VI associations, HSPG2–NID1, NID1–VTN, and links among LAMB2, COL4A2, COL18A1, FBLN1, EFEMP1, and LUM. The other contains established plasma and lipoprotein relationships, including ALB, APOA1, APOE, CLU, VTN, and SERPINC1, with the hemoglobin pair HBA1–HBB providing an additional blood-derived edge. These are known molecular relationships, so the module is not merely a statistically unconnected gene list. However, STRING evidence is supplementary here: (15 supplementary STRING terms; within-query FDR 2.63e-21–5.41e-13) corroborate the biological interpretation but are not global GO/KEGG significance tests. hu.MAP independently supports collagen assemblies involving COL1A1 and COL1A2, collagen-IV, collagen-VI, and collagen-XVIII groupings, as well as plasma-protein assemblies containing ALB, APOA1, SERPINC1, HBA1, and HBB. The repeated collagen and plasma complexes indicate that substantial parts of the module recapitulate known extracellular assemblies. Several module members, including HSPG2, NID1, VTN, EFEMP1, FBLN1, and LUM, lack hu.MAP complex assignments in the fact sheet; their co-abundance therefore adds network-level evidence but does not establish a new physical complex.

**STRING interactions (score >= 0.7)**: 46 of 190 gene pairs: ALB–APOA1 (0.998); ALB–APOE (0.953); ALB–CLU (0.831); ALB–LUM (0.737); ALB–SERPINC1 (0.933); ALB–VTN (0.988); APOA1–APOE (0.999); APOA1–CLU (0.998); APOA1–HBB (0.839); APOA1–SERPINC1 (0.708); APOA1–VTN (0.755); APOE–CLU (0.999); APOE–HSPG2 (0.954); APOE–VTN (0.989); CLU–VTN (0.962); COL18A1–COL1A1 (0.724); COL18A1–COL4A2 (0.733); COL18A1–COL6A1 (0.848); COL18A1–HSPG2 (0.894); COL18A1–VTN (0.752); COL1A1–COL1A2 (0.999); COL1A1–COL6A1 (0.969); COL1A1–COL6A3 (0.974); COL1A1–LUM (0.981); COL1A1–NID1 (0.739); COL1A2–COL4A2 (0.786); COL1A2–COL6A1 (0.875); COL1A2–COL6A3 (0.968); COL1A2–LUM (0.999); COL4A2–COL6A1 (0.81); COL4A2–COL6A3 (0.792); COL4A2–NID1 (0.823); COL6A1–COL6A3 (0.994); COL6A1–FBLN1 (0.738); COL6A1–NID1 (0.709); COL6A3–LUM (0.853); EFEMP1–FBLN1 (0.754); FBLN1–HSPG2 (0.904); FBLN1–NID1 (0.835); HBA1–HBB (0.999); HSPG2–LUM (0.78); HSPG2–NID1 (0.999); HSPG2–VTN (0.797); LAMB2–NID1 (0.734); NID1–VTN (0.996); SERPINC1–VTN (0.949)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS External encapsulating structure (FDR = 2.63e-21, 16 genes); COMPARTMENTS Extracellular matrix (FDR = 1.9e-19, 15 genes); Component Collagen-containing extracellular matrix (FDR = 1.1e-18, 17 genes); Keyword Extracellular matrix (FDR = 2.09e-17, 13 genes); Keyword Secreted (FDR = 5.24e-17, 18 genes); NetworkNeighborAL Extracellular matrix organization (FDR = 5.52e-16, 13 genes); COMPARTMENTS Collagen-containing extracellular matrix (FDR = 6.12e-16, 13 genes); Function Extracellular matrix structural constituent (FDR = 8.01e-16, 12 genes); COMPARTMENTS Extracellular region (FDR = 1.56e-15, 20 genes); Keyword Glycoprotein (FDR = 1.62e-14, 19 genes); Keyword Signal (FDR = 3.16e-14, 18 genes); NetworkNeighborAL Collagen formation, and Protein complex involved in cell adhesion (FDR = 2.08e-13, 11 genes); RCTM Extracellular matrix organization (FDR = 2.36e-13, 13 genes); Component Endoplasmic reticulum lumen (FDR = 2.63e-13, 13 genes); PMID (2023) Data-independent acquisition and quantification of extracellular matrix from human lung in chronic inflammation-associated carcinomas. (FDR = 5.41e-13, 12 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINC1, APOA1, ALB, HBB, HBA1; 5/64); huMAP3_06555.1 (COL4A2, COL6A1, COL18A1; 3/14); huMAP3_13038.1 (COL4A2, COL6A3, COL18A1; 3/40); huMAP3_02141.1 (COL1A1, COL1A2; 2/3); huMAP3_06460.1 (COL1A1, COL1A2; 2/3); huMAP3_07562.1 (COL1A1, COL1A2; 2/3); huMAP3_04556.1 (HBB, HBA1; 2/3); huMAP3_02069.1 (COL1A1, COL1A2; 2/4); huMAP3_06991.1 (HBB, HBA1; 2/4); huMAP3_10486.1 (HBB, HBA1; 2/4); huMAP3_10780.1 (COL1A1, COL1A2; 2/5); huMAP3_09231.1 (COL1A1, COL1A2; 2/6); huMAP3_09523.1 (COL1A1, COL1A2; 2/6); huMAP3_09606.1 (COL1A1, COL1A2; 2/6); huMAP3_10652.1 (COL1A1, COL1A2; 2/6); huMAP3_14070.1 (COL1A1, COL1A2; 2/8); huMAP3_07149.1 (COL4A2, COL18A1; 2/10); huMAP3_13522.1 (HBB, HBA1; 2/10); huMAP3_02991.1 (COL4A2, COL18A1; 2/14); huMAP3_08295.1 (COL4A2, COL18A1; 2/17); huMAP3_07432.1 (APOA1, ALB; 2/18); huMAP3_09435.1 (COL4A2, COL18A1; 2/18); huMAP3_07265.1 (APOA1, ALB; 2/20); huMAP3_10984.1 (COL4A2, COL18A1; 2/21); huMAP3_10699.1 (COL4A2, COL18A1; 2/28); huMAP3_09434.1 (APOA1, ALB; 2/33); huMAP3_08395.1 (APOA1, ALB; 2/43); huMAP3_09531.1 (APOA1, ALB; 2/47); huMAP3_10101.1 (APOA1, ALB; 2/49); huMAP3_10678.1 (APOA1, ALB; 2/71)

### Novelty

This module should not be presented as a newly discovered molecular complex or as proof of a novel pathway. Its central biology is well established: collagen, basement-membrane, laminin-associated, nidogen, proteoglycan, lipoprotein, albumin, and coagulation relationships are represented in STRING, hu.MAP, and extensive literature. The potentially novel aspect is the conserved co-abundance pattern across circulatory_system and lung, particularly the way a stromal ECM neighborhood is connected to a plasma and erythrocyte-associated neighborhood. That observation is hypothesis-generating rather than a claim of molecular novelty. Absence of a gene pair from STRING or hu.MAP cannot establish novelty, because those resources capture known interactions and complexes incompletely and do not directly test this tissue-pair co-abundance pattern.

**Hypothesis.** Hypothesis: this conserved module reflects a vascular–stromal extracellular-matrix program shared by the lung and the circulation. A collagen and basement-membrane scaffold formed around COL1A1, COL1A2, COL4A2, COL6A1, COL6A3, HSPG2, LAMB2, NID1, and related matrix proteins could regulate endothelial or stromal adhesion, barrier organization, and tissue remodeling through integrin-linked signaling. Secreted lipoprotein and plasma proteins may bind or traffic through this matrix, while albumin, hemoglobin, and other blood-associated proteins may partly reflect vascular content or blood microparticles. The hypothesis predicts that the matrix subnetwork will track vascular or fibroblast abundance and remodeling, whereas the plasma and hemoglobin component will track blood exposure. These alternatives should be separated using cell-resolved measurements, vascular-depletion controls, and independent validation of protein localization.

### Important genes

#### COL6A1

- **Related proteins** (co-abundance neighbors): EFEMP1 (0.88), COL1A2 (0.88), NID1 (0.86), APOA1 (0.85), ALB (0.83), HBA1; HBA2 (0.82), LAMB2 (0.81); STRING partners: COL18A1 (0.848), COL1A1 (0.969), COL1A2 (0.875), COL4A2 (0.81), COL6A3 (0.994), FBLN1 (0.738), NID1 (0.709)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06555.1
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is the most connected matrix-centered gene in the module and links collagen, nidogen, fibulin, laminin-associated, and plasma-associated neighbors. It participates in the collagen-VI trimer and ECM structural terms (GO:CC external encapsulating structure; q_global = 2.04e-16) (GO:CC extracellular matrix; q_global = 2.04e-16) (GO:MF extracellular matrix structural constituent; q_global = 3.49e-15), (5 globally significant GO/KEGG terms, q_global 8.93e-09–3.14e-08; see the table), and (5 globally significant GO/KEGG terms, q_global 0.0486–0.0486; see the table). HPA associates it with fibroblast and stromal cell contexts and secretion to the extracellular matrix. Its established collagen-VI function and disease links to Bethlem and Ullrich myopathies make it a strong structural anchor, while its substantial literature supports a mature evidence base.
- **Conclusion**: Established conclusion: COL6A1 is a credible structural hub of the matrix arm of this module. Hypothesis: its central co-abundance position may mark coordinated collagen-VI remodeling in vascular or pulmonary stroma, but the network alone does not establish that COL6A1 regulates the other genes.

#### HSPG2

- **Related proteins** (co-abundance neighbors): NID1 (0.91), COL6A3 (0.86), VTN (0.85), EFEMP1 (0.84), CLU (0.83), LAMB2 (0.82), COL18A1 (0.80); STRING partners: APOE (0.954), COL18A1 (0.894), FBLN1 (0.904), LUM (0.78), NID1 (0.999), VTN (0.797)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 is highly connected to NID1, COL18A1, VTN, EFEMP1, CLU, and LAMB2 and is a central bridge within the basement-membrane neighborhood. The primary terms (GO:CC external encapsulating structure; q_global = 2.04e-16), (GO:CC extracellular matrix; q_global = 2.04e-16), (GO:CC basement membrane; q_global = 2.36e-08), (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 3.14e-08), (GO:MF lipoprotein particle receptor binding; q_global = 0.00192), (GO:MF amyloid-beta binding; q_global = 0.00251), and (GO:MF low-density lipoprotein particle receptor binding; q_global = 0.0247) support extracellular structural, receptor-binding, and lipoprotein-associated roles. HPA identifies blood-vessel enhancement, alveolar-cell and hepatic-stellate contexts, extracellular-matrix secretion, and lung protein detection. Its annotated ability to cross-link matrix and cell-surface molecules gives it a plausible organizing role.
- **Conclusion**: Established conclusion: HSPG2 is a biologically plausible basement-membrane organizer and a network bridge between matrix and soluble-protein neighborhoods. Hypothesis: HSPG2 may help present or retain circulating ligands at the vascular or alveolar interface, an idea requiring direct binding and localization experiments.

#### COL1A1

- **Related proteins** (co-abundance neighbors): COL1A2 (0.92); STRING partners: COL18A1 (0.724), COL1A2 (0.999), COL6A1 (0.969), COL6A3 (0.974), LUM (0.981), NID1 (0.739)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_02141.1, huMAP3_06460.1, huMAP3_07562.1, huMAP3_02069.1, huMAP3_10780.1, huMAP3_09231.1, huMAP3_09523.1, huMAP3_09606.1, huMAP3_10652.1, huMAP3_14070.1
- **Function (MyGene.info)**: collagen type I alpha 1 chain. This gene encodes the pro-alpha1 chains of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIA, Ehlers-Danlos syndrome Classical type,…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 2 (0.847); osteogenesis imperfecta type 4 (0.837); osteogenesis imperfecta type 3 (0.835); osteogenesis imperfecta type 1 (0.834); osteogenesis imperfecta (0.808)
- **Europe PMC papers**: 45548
- **Why important**: COL1A1 is part of the strongly supported type-I collagen unit with COL1A2, with primary evidence from (GO:MF extracellular matrix structural constituent; q_global = 3.49e-15), (GO:MF extracellular matrix structural constituent conferring tensile strength; q_global = 8.93e-09), (GO:CC complex of collagen trimers; q_global = 8.93e-09), (GO:CC collagen trimer; q_global = 2.67e-08), (GO:BP extracellular matrix organization; q_global = 4e-07) (GO:BP extracellular structure organization; q_global = 4e-07) (GO:BP external encapsulating structure organization; q_global = 4e-07), (GO:CC fibrillar collagen trimer; q_global = 0.00222), (GO:CC fibrillar collagen complex; q_global = 0.00222), (GO:CC collagenous component of interstitial matrix; q_global = 0.00222), (GO:BP collagen fibril organization; q_global = 0.00612), and (GO:CC collagen type I trimer; q_global = 0.0486). It is connected in STRING to COL1A2, COL6A1, COL6A3, LUM, NID1, and COL18A1, and appears in multiple hu.MAP collagen-related complexes. HPA associates it with fibroblasts, hepatic stellate cells, and stromal contexts, and its extensive disease literature includes osteogenesis imperfecta and Ehlers-Danlos syndromes.
- **Conclusion**: Established conclusion: COL1A1 is a core fibrillar-collagen component and a reliable marker of the structural ECM arm. Hypothesis: coordinated COL1A1 and COL1A2 abundance may indicate active matrix deposition or remodeling in the shared vascular–lung environment, but co-abundance cannot distinguish synthesis from altered matrix retention.

#### APOA1

- **Related proteins** (co-abundance neighbors): COL6A1 (0.85), SERPINC1 (0.82), VTN (0.81), CLU (0.81), APOE (0.80); STRING partners: ALB (0.998), APOE (0.999), CLU (0.998), HBB (0.839), SERPINC1 (0.708), VTN (0.755)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is the most prominent bridge into the soluble plasma neighborhood, connecting to ALB, APOE, CLU, SERPINC1, VTN, HBB, and COL6A1. It supports lipid transport, phospholipid efflux, lipoprotein receptor binding, extracellular-vesicle, and blood-microparticle terms including (GO:CC blood microparticle; q_global = 4.2e-05), (GO:MF lipoprotein particle receptor binding; q_global = 0.00192), (GO:MF amyloid-beta binding; q_global = 0.00251), (GO:BP reverse cholesterol transport; q_global = 0.0181), (GO:MF low-density lipoprotein particle receptor binding; q_global = 0.0247), (GO:BP regulation of phospholipid efflux; q_global = 0.0486), and (GO:BP positive regulation of phospholipid efflux; q_global = 0.0486). HPA identifies liver and hepatocyte enrichment and secretion to blood. Its very large literature base and established associations with apolipoprotein deficiency, dyslipidemia, and vascular disease make it an important interpretive marker.
- **Conclusion**: Established conclusion: APOA1 most likely represents a circulating lipoprotein component rather than a lung-produced ECM component. Hypothesis: its connection to COL6A1 may reflect binding, vesicle transport, or shared vascular abundance, but it could also be a blood-content effect.

#### NID1

- **Related proteins** (co-abundance neighbors): HSPG2 (0.91), COL4A2 (0.87), COL6A1 (0.86), LAMB2 (0.83); STRING partners: COL1A1 (0.739), COL4A2 (0.823), COL6A1 (0.709), FBLN1 (0.835), HSPG2 (0.999), LAMB2 (0.734), VTN (0.996)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nidogen 1. This gene encodes a member of the nidogen family of basement membrane glycoproteins. The protein interacts with several other components of basement membranes, and may play a role in cell interactions with the extracellular matrix. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.425); focal epilepsy (0.259); Hemiparesis (0.259); Hydrocephalus (0.259); placental retention (0.233)
- **Europe PMC papers**: 1838
- **Why important**: NID1 is a central basement-membrane connector, linking HSPG2, COL4A2, COL6A1, and LAMB2, with additional STRING relationships to FBLN1 and VTN. It is represented in primary basement-membrane, cell–matrix adhesion, and ECM-organization terms (GO:CC basement membrane; q_global = 2.36e-08), (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 3.14e-08), (GO:BP extracellular matrix organization; q_global = 4e-07) (GO:BP extracellular structure organization; q_global = 4e-07) (GO:BP external encapsulating structure organization; q_global = 4e-07), (GO:MF collagen binding; q_global = 0.0236), (GO:CC protein complex involved in cell-matrix adhesion; q_global = 0.0247), (GO:BP basement membrane organization; q_global = 0.0326), and (GO:BP regulation of cell-substrate adhesion; q_global = 0.0484). HPA places it in stromal and fibroblast-like contexts and identifies secretion to the extracellular matrix. Its established role as a basement-membrane glycoprotein makes it a useful structural interface gene even though it lacks a hu.MAP assignment in the fact sheet.
- **Conclusion**: Established conclusion: NID1 is a credible matrix-interface component that supports the basement-membrane interpretation. Hypothesis: NID1 may be the physical or functional interface through which collagen, laminin-associated proteins, and proteoglycans coordinate in this shared module, but this requires tissue-specific interaction validation.

## Module 4

**Tissue pair**: circulatory_system and lung  
**Genes (23)**: ANKHD1, ARID4B, BPTF, CC2D1A, CNOT12, DENND4C, DIDO1, AHCTF1, HTATIP2, INTS7, LPP, MED12, NIPBL, PARD3, PEX5, PRRC2B, RBM22, RALGAPB, MRPL2, SRCAP, WDR44, ZC3H7B, ZNF638

### Function

The module is most consistent with a broad intracellular regulatory program centered on chromatin remodeling, transcriptional control, RNA processing, and maintenance of cellular architecture. SRCAP, ARID4B, BPTF, NIPBL, MED12, RBM22, ZNF638, CNOT12, INTS7 and related genes provide established links to chromatin remodeling, transcription by RNA polymerase II, mediator or integrator functions, RNA splicing, and post-transcriptional regulation. PARD3, LPP, DENND4C and RALGAPB add cell polarity, adhesion, membrane localization, and small-GTPase-related functions. No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The functional interpretation therefore comes from the coherent gene functions and network structure rather than from enrichment significance.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the fact sheet reports no secreted genes, and the proteins are predominantly intracellular, with many localized to the nucleus, cytosol, mitochondria, Golgi, or cell junctions. Most genes have low tissue specificity, which is compatible with a broadly expressed housekeeping or regulatory program rather than a lung-specific program. HPA nevertheless shows repeated cell-type associations, especially with neutrophils, together with additional associations involving glial, epithelial, progenitor, vascular, smooth-muscle, platelet, and other cell types. Most genes have low immune-cell specificity, but a smaller subset is immune-cell enhanced or enriched. Lung protein detection is present for most assessed genes, whereas the circulatory-system protein summary has no matching tissue data. The shared signal could therefore reflect a broadly expressed intracellular program, shared cellular composition, or blood and immune-cell contribution in the sampled tissues; it should not be interpreted as evidence that the module consists of circulating secreted proteins.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a concentrated, not module-wide, interaction structure. The known high-confidence relationships form a NIPBL-centered set linking NIPBL with ARID4B, BPTF, INTS7, MED12 and ZNF638. This supports a real connection among chromatin, transcriptional, and RNA-processing regulators, but it does not establish that every co-abundance edge represents direct physical binding. There is no STRING functional-enrichment result. hu.MAP independently places BPTF and ARID4B together in two high-confidence complexes, (hu.MAP huMAP3_13482.1) and (hu.MAP huMAP3_15128.1), although they represent only a small subset of the much larger complexes. The overlap between the STRING NIPBL-centered relationships and the hu.MAP BPTF-ARID4B complexes strengthens the interpretation that part of the module captures known nuclear regulatory machinery. The remaining genes are connected mainly by co-abundance and have no supplied STRING or hu.MAP support, so the module is broader than a single established complex.

**STRING interactions (score >= 0.7)**: 5 of 253 gene pairs: ARID4B–NIPBL (0.714); BPTF–NIPBL (0.806); INTS7–NIPBL (0.723); MED12–NIPBL (0.746); NIPBL–ZNF638 (0.745)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13482.1 (BPTF, ARID4B; 2/50); huMAP3_15128.1 (BPTF, ARID4B; 2/96)

### Novelty

The module should not be called a newly discovered molecular complex. Its most interpretable core contains previously documented relationships involving NIPBL, BPTF and ARID4B, and BPTF-ARID4B also occur together in hu.MAP complexes (hu.MAP huMAP3_13482.1) and (hu.MAP huMAP3_15128.1). The potentially novel aspect is the shared co-abundance pattern across circulatory_system and lung, particularly the way known chromatin and transcriptional regulators are coordinated with RNA processing, polarity, vesicle, mitochondrial, and adhesion genes. However, the absence of STRING or hu.MAP support for many edges is not evidence of novelty; it may reflect incomplete databases, indirect regulation, tissue composition, or correlated expression. A claim of a new biological mechanism would require independent replication, cell-type-aware analysis, and perturbation or physical-interaction experiments.

**Hypothesis.** Hypothesis: the module reflects a shared cell-state or cell-composition program in which a broadly expressed nuclear regulatory system coordinates transcriptional and chromatin states with RNA processing and structural maintenance in cells present in both tissues. NIPBL, BPTF and ARID4B may form the best-supported regulatory core, while SRCAP could connect chromatin remodeling to the wider co-abundance pattern. RBM22 and ZNF638 may represent RNA-processing links, and PARD3 and LPP may connect the intracellular regulatory state to polarity, adhesion, vascular, or immune-cell features. The recurrent neutrophil associations make a blood or immune-cell contribution plausible, but this remains a hypothesis rather than proof of the module's cellular origin.

### Important genes

#### SRCAP

- **Related proteins** (co-abundance neighbors): ARID4B (0.90), BPTF (0.89), PRRC2B (0.85), DIDO1 (0.83), PARD3 (0.82), CNOT12 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Snf2 related CREBBP activator protein. This gene encodes the core catalytic component of the multiprotein chromatin-remodeling SRCAP complex. The encoded protein is an ATPase that is necessary for the incorporation of the histone variant H2A.Z into nucleosomes. It can function as a transcriptional activator in Notch-mediated, CREB-mediated and steroid receptor-mediated transcription. Mutations in this gene cause Floating-Harbor syndrom…
- **Diseases (Open Targets)**: Floating-Harbor syndrome (0.799); hereditary disease (0.539); neurodevelopmental disorder (0.512); developmental delay, hypotonia, musculoskeletal defects, and behavioral abnormalities (0.462); neurodevelopmental disorder with hypotonia and variable intellectual and behavioral abnormalities (0.462)
- **Europe PMC papers**: 1276
- **Why important**: SRCAP is the strongest network hub in the supplied subgraph and connects several otherwise distinct branches, including ARID4B, BPTF, PRRC2B, DIDO1, PARD3 and CNOT12. Its established role as the catalytic component of the SRCAP chromatin-remodeling complex, including H2A.Z incorporation and transcriptional regulation, gives the module a plausible chromatin-centered anchor. It has a substantial literature and a documented association with Floating-Harbor syndrome. HPA describes broad tissue distribution and lung detection, rather than a secreted or tissue-restricted protein.
- **Conclusion**: Established evidence supports SRCAP as a central chromatin-remodeling and transcriptional regulator in the module. It is a strong candidate for organizing the module's regulatory axis, but the co-abundance data do not establish that SRCAP directly controls the other module genes in circulatory_system or lung.

#### NIPBL

- **Related proteins** (co-abundance neighbors): BPTF (0.83), ARID4B (0.81); STRING partners: ARID4B (0.714), BPTF (0.806), INTS7 (0.723), MED12 (0.746), ZNF638 (0.745)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NIPBL cohesin loading factor. This gene encodes the homolog of the Drosophila melanogaster Nipped-B gene product and fungal Scc2-type sister chromatid cohesion proteins. The Drosophila protein facilitates enhancer-promoter communication of remote enhancers and plays a role in developmental regulation. It is also homologous to a family of chromosomal adherins with broad roles in sister chromatid cohesion, chromosome condensatio…
- **Diseases (Open Targets)**: Cornelia de Lange syndrome (0.864); hereditary disease (0.544); Dislocated radial head (0.462); Intellectual disability (0.384); low grade glioma (0.370)
- **Europe PMC papers**: 2494
- **Why important**: NIPBL is the clearest known-interaction hub: STRING links it to ARID4B, BPTF, INTS7, MED12 and ZNF638. Its established functions include cohesin loading, enhancer-promoter communication, chromatin remodeling, chromosome cohesion, DNA repair, and developmental regulation. It has extensive literature and strong disease evidence for Cornelia de Lange syndrome and related developmental phenotypes. Its HPA profile is broadly distributed with a neutrophil cell-type association and lung detection.
- **Conclusion**: Established evidence makes NIPBL a credible bridge between chromatin organization, transcriptional regulation and the known STRING-supported core. Its presence does not by itself prove cohesin activity in the sampled tissues, so that interpretation remains mechanistic context rather than demonstrated module function.

#### ARID4B

- **Related proteins** (co-abundance neighbors): SRCAP (0.90), PRRC2B (0.86), ZNF638 (0.86), NIPBL (0.81), CC2D1A (0.80); STRING partners: NIPBL (0.714)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13482.1, huMAP3_15128.1
- **Function (MyGene.info)**: AT-rich interaction domain 4B. This gene encodes a protein with sequence similarity to retinoblastoma-binding protein-1. The encoded protein is a subunit of the histone deacetylase-dependant SIN3A transcriptional corepressor complex, which functions in diverse cellular processes including proliferation, differentiation, apoptosis, oncogenesis, and cell fate determination. The gene product is recognized by IgG antibody isolated …
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.375); glomerulonephritis (0.227); thyroiditis (0.210); asthma (0.200); femur fracture (0.190)
- **Europe PMC papers**: 634
- **Why important**: ARID4B occupies a highly connected position near SRCAP, PRRC2B, ZNF638, NIPBL and CC2D1A. It is a component of the SIN3A histone deacetylase-dependent transcriptional corepressor complex and is represented with BPTF in both hu.MAP complexes (hu.MAP huMAP3_13482.1) and (hu.MAP huMAP3_15128.1). Its annotations implicate transcriptional repression, cell fate, proliferation, differentiation and transforming-growth-factor-beta-related regulation. It has substantial literature and disease associations including skeletal, renal, thyroid and airway-related conditions.
- **Conclusion**: Established evidence supports ARID4B as a transcriptional-coregulator component that reinforces the chromatin and repression interpretation. Its role as a tissue-specific driver of this shared module is unproven, and the neutrophil association could reflect cellular composition rather than ARID4B activity within neutrophils.

#### BPTF

- **Related proteins** (co-abundance neighbors): SRCAP (0.89), NIPBL (0.83), INTS7 (0.82); STRING partners: NIPBL (0.806)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_13482.1, huMAP3_15128.1
- **Function (MyGene.info)**: bromodomain PHD finger transcription factor. This gene was identified by the reactivity of its encoded protein to a monoclonal antibody prepared against brain homogenates from patients with Alzheimer's disease. Analysis of the original protein (fetal Alz-50 reactive clone 1, or FAC1), identified as an 810 aa protein containing a DNA-binding domain and a zinc finger motif, suggested it might play a role in the regulation of transcription. Hig…
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and distal limb anomalies (0.788); Intellectual disability (0.539); hereditary disease (0.538); neurodegenerative disease (0.536); Global developmental delay (0.507)
- **Europe PMC papers**: 1741
- **Why important**: BPTF connects SRCAP, NIPBL and INTS7 and is the second member of the module represented in both hu.MAP complexes (hu.MAP huMAP3_13482.1) and (hu.MAP huMAP3_15128.1) with ARID4B. It is annotated for chromatin remodeling and regulation of transcription by RNA polymerase II, with additional relevance to brain development and neurodevelopmental disease. It has extensive literature and strong disease associations involving developmental delay, intellectual disability and dysmorphic-facies syndromes. HPA shows broad tissue specificity and lung detection.
- **Conclusion**: Established evidence identifies BPTF as a plausible chromatin-remodeling and transcriptional component of the known nuclear core. The module does not demonstrate that BPTF is acting through the same complex in both tissues, so the tissue-level mechanism remains to be tested.

#### PARD3

- **Related proteins** (co-abundance neighbors): SRCAP (0.82), CNOT12 (0.81), DENND4C (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Cell Junctions; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: par-3 family cell polarity regulator. This gene encodes a member of the PARD protein family. PARD family members interact with other PARD family members and other proteins; they affect asymmetrical cell division and direct polarized cell growth. Multiple alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Oct 2011].
- **Diseases (Open Targets)**: spina bifida (0.596); neurodegenerative disease (0.526); Abnormality of the skeletal system (0.515); neural tube defect (0.484); alcohol drinking (0.419)
- **Europe PMC papers**: 1607
- **Why important**: PARD3 links the central SRCAP-CNOT12 branch to DENND4C and is the clearest structural-cellular component among the selected genes. Its established functions include cell polarity, adhesion, microtubule organization and protein targeting to membranes. HPA places it at plasma-membrane and cell-junction locations, with associations to podocytes, esophageal apical cells and basophils. It has extensive literature and disease associations involving neural-tube and skeletal abnormalities.
- **Conclusion**: Established evidence supports PARD3 as a polarity and junctional component that may connect nuclear regulation to tissue architecture. Its inclusion in the module is compatible with shared epithelial, vascular or immune-cell composition, but a direct regulatory link from the chromatin core to PARD3 is only a hypothesis.

## Module 5

**Tissue pair**: circulatory_system and lung  
**Genes (6)**: APMAP, CKAP4, ITGAV, NME6, NCSTN, VKORC1L1

### Function

The module does not have a globally significant GO or KEGG enrichment term, and STRING reports no supplementary enrichment. Its strongest interpretation therefore comes from the gene annotations and the co-abundance topology rather than from pathway over-representation. The genes collectively point to a membrane-associated cellular program involving cell adhesion and integrin signaling through ITGAV, membrane-protein processing through NCSTN, endoplasmic-reticulum and oxidative-stress biology through VKORC1L1 and CKAP4, nucleotide metabolism through NME6, and plasma-membrane biology through APMAP. ITGAV is the most connected node, but the network should be interpreted as a correlated expression module rather than as a demonstrated physical pathway.

**Cell composition.** The module is not composed of secreted or plasma proteins. Most genes have low tissue specificity, while all have some cell-type-enhanced annotation. The recurring cell-type annotations include neutrophils or neutrophil progenitors, trophoblast populations, and cardiomyocytes; CKAP4 also has immune-cell enhancement for basophils. APMAP is tissue-enhanced in liver. This pattern is compatible with a broadly expressed cellular program, shared cell types, or sample-composition effects rather than a lung- and circulation-specific secreted-protein system. Protein detection in lung supports expression of part of the module, but the absence of matching circulatory-system HPA tissue data limits tissue-level interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and STRING provides no functional-enrichment support. No hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not corroborated here as established protein-protein interactions or as membership in a known multiprotein complex. The pair involving ITGAV and CKAP4, and the links involving ITGAV, NCSTN, VKORC1L1, and APMAP, may reflect coordinated regulation, shared cell-type composition, membrane or organelle biology, or indirect biology; they should not be described as physical interactions without independent evidence.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel co-abundance association in the specific circulatory-system and lung comparison, because the module lacks high-confidence STRING interactions, lacks a hu.MAP complex, and lacks a globally significant GO or KEGG term. However, those absences do not establish biological novelty. The individual genes and their functions are already established, and the module could arise from broad expression, shared cell types, or technical and compositional effects. The defensible conclusion is that the coordinated expression pattern is a potentially novel observation requiring replication and orthogonal validation, not that it is a newly discovered molecular complex or pathway.

**Hypothesis.** Hypothesis: the module represents a shared membrane and intracellular-stress state present in related cellular populations across circulation and lung. Integrin-associated adhesion through ITGAV may be coordinated with membrane or endoplasmic-reticulum functions involving CKAP4, VKORC1L1, and APMAP, while NCSTN and NME6 may reflect concurrent membrane-protein processing and nucleotide-metabolic demands. This hypothesis is biologically plausible from the annotations and topology, but it is not established by enrichment, STRING, hu.MAP, or the co-abundance data alone. Testing should include cell-composition adjustment, replication in independent cohorts, protein-level validation, and perturbation or localization experiments.

### Important genes

#### ITGAV

- **Related proteins** (co-abundance neighbors): CKAP4 (0.82), NCSTN (0.81), APMAP (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha V. The product of this gene belongs to the integrin alpha chain family. Integrins are heterodimeric integral membrane proteins composed of an alpha subunit and a beta subunit that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha V subunit. This subunit associates with beta 1, beta 3, beta…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); myocardial infarction (0.396); angina pectoris (0.371); Recurrent thrombophlebitis (0.370); intermediate coronary syndrome (0.370)
- **Europe PMC papers**: 5475
- **Why important**: ITGAV is the most connected and strongest node in the module. Its established role as an integrin alpha subunit links it to heterodimeric cell-surface adhesion and signaling, including angiogenesis, vasculogenesis, cell-matrix adhesion, and calcium signaling. It also has extensive literature and disease associations involving cardiovascular and thrombotic conditions.
- **Conclusion**: Established evidence supports ITGAV as the best anchor for an adhesion- and membrane-signaling interpretation. The hypothesis that it organizes the other module genes is not established, because STRING and hu.MAP provide no corroborating interaction evidence.

#### NCSTN

- **Related proteins** (co-abundance neighbors): VKORC1L1 (0.82), ITGAV (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nicastrin. This gene encodes a type I transmembrane glycoprotein that is an integral component of the multimeric gamma-secretase complex. The encoded protein cleaves integral membrane proteins, including Notch receptors and beta-amyloid precursor protein, and may be a stabilizing cofactor required for gamma-secretase complex assembly. The cleavage of beta-amyloid precursor protein yields amyloid beta peptide…
- **Diseases (Open Targets)**: acne inversa, familial, 1 (0.724); neurodegenerative disease (0.525); desmoid tumor (0.503); Alzheimer disease (0.406); hidradenitis suppurativa (0.389)
- **Europe PMC papers**: 2357
- **Why important**: NCSTN is a network bridge connecting ITGAV with VKORC1L1. It is an established component and stabilizing cofactor of the gamma-secretase complex and participates in membrane-protein ectodomain processing and Notch receptor processing. It has substantial literature and disease associations, including neurodegenerative and inflammatory disorders. Its lung protein detection also provides tissue-level support.
- **Conclusion**: Established evidence supports NCSTN as a biologically informative membrane-processing gene within the module. A coordinated relationship between gamma-secretase-related processing and integrin biology is a hypothesis, not a demonstrated mechanism here.

#### VKORC1L1

- **Related proteins** (co-abundance neighbors): NME6 (0.87), NCSTN (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vitamin K epoxide reductase complex subunit 1L1. This gene encodes an enzyme important in the vitamin K cycle, which is involved in the carboxylation of glutamate residues present in vitamin K-dependent proteins. The encoded enzyme catalyzes the de-epoxidation of vitamin K 2,3-epoxide. Oxidative stress may upregulate expression of this gene and the encoded protein may protect cells and membrane proteins form oxidative damage. This gene and a rel…
- **Diseases (Open Targets)**: preeclampsia (0.271); Lower limb asymmetry (0.201); pulmonary embolism (0.140); prostate cancer (0.111); Familial prostate cancer (0.111)
- **Europe PMC papers**: 291
- **Why important**: VKORC1L1 connects NME6 and NCSTN in the module topology. Its established function in vitamin K metabolism and glutamate carboxylation, together with a reported role in cellular oxidative-stress responses, gives it a distinctive redox and biosynthetic interpretation. It has more limited literature than ITGAV or NCSTN but has disease associations including pulmonary embolism and preeclampsia.
- **Conclusion**: Established evidence supports VKORC1L1 as a plausible redox and vitamin-K-related component. Its placement in this module may indicate coordinated stress or membrane biology, but that connection remains a hypothesis because no pathway enrichment or physical-complex evidence supports it.

#### CKAP4

- **Related proteins** (co-abundance neighbors): ITGAV (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytoskeleton associated protein 4. Enables RNA binding activity. Located in several cellular components, including lipid droplet; nuclear speck; and rough endoplasmic reticulum. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: smoking initiation (0.357); arthropathy (0.216); asthma (0.200); adolescent idiopathic scoliosis (0.141); spinal cord injury (0.128)
- **Europe PMC papers**: 2103
- **Why important**: CKAP4 is directly connected to ITGAV and is localized to the endoplasmic reticulum according to the supplied annotation. It has cell-type-enhanced annotations spanning cardiomyocytes, neutrophils, and neutrophil progenitors, as well as immune-cell enhancement for basophils. It has substantial literature and disease associations that include asthma and smoking initiation.
- **Conclusion**: Established evidence supports CKAP4 as a candidate link between membrane adhesion, endoplasmic-reticulum biology, and cell-composition signals. A role in coordinating the module across lung and circulatory samples is plausible but unproven.

#### APMAP

- **Related proteins** (co-abundance neighbors): ITGAV (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adipocyte plasma membrane associated protein. Enables arylesterase activity. Predicted to be involved in biosynthetic process. Located in cell surface and membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: smoking initiation (0.243); obesity disorder (0.196); Alzheimer disease (0.078); infection (0.077); cervical carcinoma (0.076)
- **Europe PMC papers**: 444
- **Why important**: APMAP is connected to ITGAV and is annotated as a plasma-membrane protein with arylesterase activity. It is tissue-enhanced in liver and has cell-type-enhanced annotations in hepatocytes, trophoblast populations, neutrophils, and neutrophil progenitors. Its literature is more limited than that of the other leading candidates, making it useful as a potentially informative but less established module component.
- **Conclusion**: Established evidence supports APMAP as a membrane-associated gene that may contribute to the module's shared cellular or metabolic signal. Its specific relationship to ITGAV or to lung and circulation biology is a hypothesis requiring validation.

## Module 6

**Tissue pair**: circulatory_system and lung  
**Genes (6)**: ARFIP2, EXOC6, PRPF39, TCP11L1, GTF3C1, XIAP

### Function

The module does not have any GO or KEGG term that passes global multiple-testing correction, so no pathway-level function can be assigned from enrichment evidence. Its sparse co-abundance structure links intracellular processes rather than defining a coherent canonical pathway: XIAP contributes anti-apoptotic and inflammatory-signaling functions; ARFIP2 contributes membrane curvature sensing, intracellular trafficking, and actin organization; EXOC6 contributes exocytosis and Golgi-to-cell-surface transport; GTF3C1 contributes RNA polymerase three transcription; PRPF39 contributes pre-mRNA processing; and TCP11L1 has a predicted role in signal transduction and microtubule biology. The module is therefore best interpreted as a possible shared intracellular homeostasis or stress-response signal, not as an established functional pathway. The absence of significant GO or KEGG enrichment does not invalidate the module.

**Cell composition.** This is not a plasma or secreted-protein module: none of the genes is annotated as secreted. Most genes have low tissue specificity, and all module proteins are detected in lung, while the supplied circulatory-system HPA comparison has no matching tissue data. The module is not strongly blood-cell dominated overall, because most genes have low immune-cell specificity, although GTF3C1 is immune-cell enhanced in gdT cells and EXOC6 is immune-cell enhanced in neutrophils. Cell-type enhancement is present for most genes, with signals involving esophageal apical cells, goblet cells, syncytiotrophoblasts, myonuclei, pituitary stem cells, photoreceptor cells, and neutrophil-lineage cells. EXOC6 is tissue enriched in retina. These observations raise the possibility that the shared signal partly reflects cell-type composition or broadly shared epithelial, immune, or structural cell states in the sampled tissues rather than a circulatory-system–lung-specific molecular program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and no hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not supported by the supplied known physical-interaction resources. The genes nevertheless represent biologically plausible intracellular processes: apoptosis and inflammatory signaling through XIAP, membrane and actin organization through ARFIP2, vesicular trafficking through EXOC6, transcription through GTF3C1, and RNA processing through PRPF39. Their lack of STRING and hu.MAP support means the network should be treated as a co-abundance association rather than a demonstrated protein complex or direct molecular interaction network.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported cross-tissue co-abundance pattern, because it has no reported high-confidence STRING links, no supported hu.MAP multi-member complex, and no globally significant GO or KEGG annotation. However, these absences do not establish biological novelty. The sparse network, mixed functional annotations, broad tissue expression, and cell-type enhancement suggest that the pattern could arise from shared cellular composition, coordinated general cell-state regulation, or technical and sampling effects. A claim of a new biological module would require replication in independent cohorts, adjustment for cell composition, and preferably orthogonal molecular or perturbation evidence.

**Hypothesis.** Hypothesis: the module captures a shared intracellular adaptation state present in lung and circulatory-system samples, in which survival signaling, membrane remodeling, exocytosis, transcriptional capacity, and RNA processing vary together. XIAP may support survival during inflammatory or oxidative stress, ARFIP2 and EXOC6 may coordinate membrane and vesicle behavior, and GTF3C1 and PRPF39 may reflect accompanying changes in transcription and RNA maturation. An alternative hypothesis is that the association is driven mainly by mixtures of epithelial, immune, and other cell types rather than by a single pathway operating within one cell type. This should be tested by cell-resolved expression analysis and perturbation of the proposed trafficking or survival components.

### Important genes

#### XIAP

- **Related proteins** (co-abundance neighbors): PRPF39 (0.88), ARFIP2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: X-linked inhibitor of apoptosis. This gene encodes a protein that belongs to a family of apoptotic suppressor proteins. Members of this family share a conserved motif termed, baculovirus IAP repeat, which is necessary for their anti-apoptotic function. This protein functions through binding to tumor necrosis factor receptor-associated factors TRAF1 and TRAF2 and inhibits apoptosis induced by menadione, a potent inducer of free ra…
- **Diseases (Open Targets)**: X-linked lymphoproliferative syndrome (0.814); neurodegenerative disease (0.556); inflammatory bowel disease (0.478); hereditary disease (0.469); Splenomegaly (0.464)
- **Europe PMC papers**: 16708
- **Why important**: XIAP is among the most connected genes in the module and links to ARFIP2 and PRPF39. Its established anti-apoptotic role, interactions with tumor-necrosis-factor receptor-associated factors, and reported involvement in inflammatory, DNA-damage, ubiquitination, and interferon-related processes make it the strongest candidate for a survival or stress-response interpretation. It also has substantial literature and disease-association coverage, including X-linked lymphoproliferative syndrome and inflammatory bowel disease.
- **Conclusion**: Established evidence supports XIAP as an anti-apoptotic and inflammation-related regulator with a central network position. It is plausible, but not demonstrated, that XIAP helps organize the cross-tissue module or links cellular stress to the other module processes.

#### ARFIP2

- **Related proteins** (co-abundance neighbors): XIAP (0.85), TCP11L1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ARF interacting protein 2. Enables several functions, including GTP-dependent protein binding activity; membrane curvature sensor activity; and phosphatidylinositol-4-phosphate binding activity. Involved in actin cytoskeleton organization. Located in cell cortex; ruffle; and trans-Golgi network membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.081); familial idiopathic steroid-resistant nephrotic syndrome (0.071); early-onset non-syndromic cataract (0.068); retinitis pigmentosa (0.065); focal segmental glomerulosclerosis (0.065)
- **Europe PMC papers**: 226
- **Why important**: ARFIP2 is among the most connected genes and bridges XIAP with TCP11L1. Its annotated membrane-curvature sensing, phosphatidylinositol-phosphate binding, small-GTPase signaling, intracellular transport, mitophagy, lamellipodium assembly, and actin-cytoskeleton functions provide a mechanistic connection between signaling, membrane remodeling, and trafficking. Its cell-type enhancement in epithelial and syncytial populations is relevant to the mixed tissue context.
- **Conclusion**: Established evidence supports ARFIP2 as a membrane and cytoskeletal trafficking regulator. Its bridging position makes it a plausible coordinator of the module, but the module does not establish that its protein interactions or functions are co-regulated across the two tissues.

#### EXOC6

- **Related proteins** (co-abundance neighbors): PRPF39 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Centrosome, Basal body, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exocyst complex component 6. The protein encoded by this gene is highly similar to the Saccharomyces cerevisiae SEC15 gene product, which is essential for vesicular traffic from the Golgi apparatus to the cell surface in yeast. It is one of the components of a multiprotein complex required for exocytosis. The 5' portion of this gene and two neighboring cytochrome p450 genes are included in a deletion that results in an autoso…
- **Diseases (Open Targets)**: pituitary gland disorder (0.358); metabolic syndrome (0.323); type 2 diabetes mellitus (0.317); Abnormality of the skeletal system (0.313); open-angle glaucoma (0.299)
- **Europe PMC papers**: 344
- **Why important**: EXOC6 is a peripheral network member connected to PRPF39 and is a component of the exocyst machinery required for exocytosis and Golgi-to-cell-surface transport. It is tissue enriched in retina and enhanced in several cell types, including neutrophils, making it informative for evaluating cell-composition effects. Its disease associations include pituitary disorders, metabolic syndrome, type two diabetes, skeletal abnormalities, and glaucoma.
- **Conclusion**: Established evidence supports EXOC6 as a vesicular-trafficking and exocytosis component. Its module membership could reflect secretory or membrane-transport activity, but because the module contains no secreted proteins and EXOC6 is cell-type enhanced, a cell-composition explanation remains at least as plausible as a shared tissue-wide trafficking program.

#### GTF3C1

- **Related proteins** (co-abundance neighbors): TCP11L1 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: general transcription factor IIIC subunit 1. Predicted to contribute to DNA binding activity. Predicted to be involved in 5S class rRNA transcription by RNA polymerase III and transcription initiation from RNA polymerase III promoter. Located in nucleolus and nucleoplasm. Part of transcription factor TFIIIC complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.543); lysosomal storage disease (0.357); alopecia areata (0.352); Abnormal brain morphology (0.266); esophageal atresia/tracheoesophageal fistula (0.259)
- **Europe PMC papers**: 394
- **Why important**: GTF3C1 is connected to TCP11L1 and supplies a transcriptional dimension to an otherwise mixed module. It is a component of the TFIIIC complex and is involved in transcription of transfer RNA, ribosomal RNA, and other RNA polymerase three products. Its enhancement in cone photoreceptor, esophageal apical, and prostatic glandular cells, together with immune-cell enhancement in gdT cells, makes it relevant to the possibility of cell-state or cell-mixture effects.
- **Conclusion**: Established evidence supports GTF3C1 as a core transcription-initiation factor for RNA polymerase three. Its presence does not demonstrate a transcriptional module because no enrichment term passed global correction; it may instead mark a shared biosynthetic state or the abundance of particular cell populations.

#### PRPF39

- **Related proteins** (co-abundance neighbors): XIAP (0.88), EXOC6 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pre-mRNA processing factor 39. Predicted to be involved in mRNA 5'-splice site recognition. Predicted to be part of U1 snRNP; U2-type prespliceosome; and commitment complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); inborn disorder of amino acid metabolism (0.174); early-onset non-syndromic cataract (0.070); influenza A (H1N1) (0.069); early-onset zonular cataract (0.065)
- **Europe PMC papers**: 208
- **Why important**: PRPF39 is among the more connected genes and links XIAP with EXOC6. It is predicted to participate in splice-site recognition and spliceosomal prespliceosome or commitment-complex functions, thereby connecting RNA maturation with the survival and trafficking-related genes. It has a smaller literature base than XIAP but direct relevance to RNA processing.
- **Conclusion**: Established evidence supports PRPF39 as a predicted pre-mRNA-processing factor. Its module position suggests coordinated RNA-processing activity may accompany the observed co-abundance pattern, but this is a hypothesis rather than a demonstrated module function.

## Module 7

**Tissue pair**: circulatory_system and lung  
**Genes (7)**: ARFRP1, FAM3C, HSDL2, KNL1, MBLAC2, SIRT1, UXS1

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established shared pathway or biological process at the module level. The genes nevertheless suggest a heterogeneous cellular program spanning intracellular trafficking, Golgi and secretory biology, glycosaminoglycan precursor production, mitochondrial or lipid-related metabolism, signaling, genome maintenance, and cell division. FAM3C provides a secreted signaling component, ARFRP1 supports Golgi-to-endosome and Golgi-to-plasma-membrane trafficking, and UXS1 supplies UDP-xylose for glycosaminoglycan synthesis. SIRT1 and KNL1 represent regulatory and proliferative biology, respectively. The most defensible interpretation is therefore a weakly connected co-abundance pattern that may reflect shared cellular composition or coordinated cellular state rather than a single established pathway.

**Cell composition.** The module is not dominated by secreted or plasma proteins. FAM3C is explicitly secreted in other tissues, whereas UXS1 is intracellular and membrane-associated and the remaining genes are not secreted according to the HPA summary. Most genes have low tissue specificity, and most have low immune-cell specificity, arguing against a uniformly blood-cell-specific module. However, HPA single-cell annotations are diverse, including enterocytes, parietal cells, adipocytes, myonuclei, neutrophils, spermatids, platelets, photoreceptor cells, corticotrophs, and progenitor populations. KNL1 is group-enriched in bone marrow, lymphoid tissue, and testis, while FAM3C is enriched in memory and naive B-cell annotations. Lung protein detection is present for most genes but absent for SIRT1 and KNL1. Overall, the composition is heterogeneous and compatible with shared cell types, proliferative cells, or sample-composition effects rather than a uniform circulatory-system or lung tissue program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes, no STRING functional-enrichment result, and no hu.MAP complex containing multiple module members. Therefore, the co-abundance edges are not corroborated by the supplied curated interaction or complex resources. The absence of such evidence means the module may capture co-regulation, shared cell composition, or indirect biology rather than direct physical interaction. Gene-level annotations still provide established functions: ARFRP1 is a Golgi trafficking GTPase, UXS1 is a UDP-xylose biosynthetic enzyme, SIRT1 is an intracellular regulatory protein associated with DNA repair and transcriptional regulation, KNL1 is a kinetochore scaffold, and FAM3C is a secreted signaling molecule.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially under-characterized co-abundance pattern, but it cannot be called a new biological discovery solely because STRING and hu.MAP contain no matching relationships. The lack of globally significant GO/KEGG enrichment, STRING enrichment, and multi-member hu.MAP complexes weakens the case for a previously unrecognized molecular complex or pathway. A cautious novelty claim is that this particular cross-tissue co-abundance association may be new in the analyzed dataset and warrants replication, while the individual gene functions and disease links are not themselves novel.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state or sample-composition signal in which Golgi and membrane trafficking, secretory signaling, glycosaminoglycan precursor production, lipid-related metabolism, and cell-cycle or DNA-regulatory activity vary together across circulatory-system and lung samples. FAM3C and UXS1 could connect secretory or extracellular-matrix biology to Golgi function, while ARFRP1 could support the trafficking component. SIRT1 and KNL1 may mark regulatory or proliferative state rather than directly participate in the same physical pathway. This hypothesis predicts that the association should be tested against cell-type proportions, proliferative-state markers, and independent cohorts before assigning it a unified mechanism.

### Important genes

#### FAM3C

- **Related proteins** (co-abundance neighbors): ARFRP1 (0.85), UXS1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FAM3 metabolism regulating signaling molecule C. This gene is a member of the family with sequence similarity 3 (FAM3) family and encodes a secreted protein with a GG domain. A change in expression of this protein has been noted in pancreatic cancer-derived cells. [provided by RefSeq, Mar 2010].
- **Diseases (Open Targets)**: osteoporosis (0.469); Abnormality of the skeletal system (0.406); bone disorder (0.405); upper extremity fracture (0.353); bone fracture (0.338)
- **Europe PMC papers**: 816
- **Why important**: FAM3C is the clearest extracellular and signaling-facing member: it is annotated as a secreted protein with a signaling role, has enterocyte and parietal-cell single-cell enrichment, and is enriched in memory and naive B-cell annotations. It links the module to possible intercellular communication and sample-composition effects. Its position is intermediate in the co-abundance subgraph, connecting ARFRP1 with UXS1. It also has substantial literature and disease associations involving skeletal and bone-related traits.
- **Conclusion**: Established evidence supports FAM3C as a secreted signaling molecule and a plausible indicator of cell-type or extracellular signaling variation. It is not established that FAM3C mechanistically drives the whole module; that role remains a hypothesis.

#### ARFRP1

- **Related proteins** (co-abundance neighbors): HSDL2 (0.87), FAM3C (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ARF related protein 1. The protein encoded by this gene is a membrane-associated GTP-ase which localizes to the plasma membrane and is related to the ADP-ribosylation factor (ARF) and ARF-like (ARL) proteins. This gene plays a role in membrane trafficking between the trans-Golgi network and endosomes. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, May 201…
- **Diseases (Open Targets)**: atopic eczema (0.283); inflammatory bowel disease (0.208); metabolic syndrome (0.205); prostate carcinoma (0.202); dermatitis (0.196)
- **Europe PMC papers**: 406
- **Why important**: ARFRP1 has a central position in the co-abundance subgraph and is annotated as a membrane-associated GTPase involved in retrograde endosome-to-Golgi transport and Golgi-to-plasma-membrane transport. Its Golgi localization provides a plausible intracellular counterpart to FAM3C secretion and UXS1-related Golgi biology. Its low tissue and cell-type specificity makes it useful for a broadly expressed cellular-state interpretation.
- **Conclusion**: Established evidence supports ARFRP1 as a Golgi trafficking regulator. Its network position makes it a useful connector in this module, but no supplied interaction resource establishes direct physical links to the other module genes.

#### UXS1

- **Related proteins** (co-abundance neighbors): FAM3C (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UDP-glucuronate decarboxylase 1. This gene encodes an enzyme found in the perinuclear Golgi which catalyzes the synthesis of UDP-xylose used in glycosaminoglycan (GAG) synthesis on proteoglycans. The GAG chains are covalently attached to proteoglycans which participate in signaling pathways during development. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); aortic disorder (0.271); alcohol drinking (0.262); placental retention (0.259); Shock (0.259)
- **Europe PMC papers**: 436
- **Why important**: UXS1 has the most direct connection to extracellular-matrix precursor production: it catalyzes UDP-xylose synthesis for glycosaminoglycan chains on proteoglycans. It is connected to FAM3C in the co-abundance subgraph and is annotated as intracellular and membrane-associated, fitting a biosynthetic or Golgi-related interpretation. Its platelet-enriched single-cell annotation also makes blood or cellular-composition effects relevant.
- **Conclusion**: Established evidence supports UXS1 in UDP-xylose and glycosaminoglycan biosynthesis. Its possible role in a shared lung-circulatory extracellular-matrix program is a hypothesis, not a demonstrated module-level function.

#### SIRT1

- **Related proteins** (co-abundance neighbors): KNL1 (0.85), MBLAC2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sirtuin 1. This gene encodes a member of the sirtuin family of proteins, homologs to the yeast Sir2 protein. Members of the sirtuin family are characterized by a sirtuin core domain and grouped into four classes. The functions of human sirtuins have not yet been determined; however, yeast sirtuin proteins are known to regulate epigenetic gene silencing and suppress recombination of rDNA. Studies suggest that…
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); atrial fibrillation (0.336); hypertensive disorder (0.204); tooth disorder (0.200); type 2 diabetes mellitus (0.140)
- **Europe PMC papers**: 55588
- **Why important**: SIRT1 is the most extensively studied gene in the module and has annotations involving DNA repair, transcriptional regulation, chromatin-related biology, and angiogenesis. It forms a co-abundance branch with KNL1 and MBLAC2, giving it a potentially important regulatory position despite the absence of curated STRING or hu.MAP support. Its disease associations span neurodegenerative, cardiovascular, hypertensive, and metabolic contexts, making it relevant to circulatory and lung research.
- **Conclusion**: Established evidence supports SIRT1 as an intracellular regulatory protein with roles in repair and transcriptional control. Linking it directly to the trafficking, secretion, or glycosaminoglycan branch is speculative and should not be inferred from co-abundance alone.

#### KNL1

- **Related proteins** (co-abundance neighbors): SIRT1 (0.85); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinetochore scaffold 1. The protein encoded by this gene is a component of the multiprotein assembly that is required for creation of kinetochore-microtubule attachments and chromosome segregation. The encoded protein functions as a scaffold for proteins that influence the spindle assembly checkpoint during the eukaryotic cell cycle and it interacts with at least five different kinetochore proteins and two checkpoint kin…
- **Diseases (Open Targets)**: autosomal recessive primary microcephaly (0.739); hereditary disease (0.414); Primary microcephaly (0.373); endometrial endometrioid adenocarcinoma (0.371); colorectal adenocarcinoma (0.371)
- **Europe PMC papers**: 1055
- **Why important**: KNL1 is a kinetochore scaffold required for kinetochore-microtubule attachment, spindle-checkpoint activity, and chromosome segregation. Its HPA profile is enriched in bone marrow, lymphoid tissue, testis, and several germ-cell or progenitor populations, making it a strong marker of proliferative or progenitor-cell composition. It is connected to SIRT1 in the module and has disease associations including primary microcephaly and several cancers.
- **Conclusion**: Established evidence supports KNL1 as a mitotic and kinetochore protein and supports its association with proliferative progenitor contexts. Its presence does not establish that mitosis is the function of the whole module; it may instead report a cell-composition or proliferation component.

## Module 8

**Tissue pair**: circulatory_system and lung  
**Genes (5)**: ATG9A, CHD1, INCENP, NF2, TRMT5

### Function

The module does not have a globally significant GO or KEGG annotation: no GO or KEGG term passed global correction. Its genes instead suggest several connected cellular processes rather than one established pathway. CHD1 and TRMT5 support chromatin, nucleosome, transcriptional and RNA-modification biology; INCENP supports chromosome segregation and mitotic cytokinesis; NF2 supports membrane–cytoskeleton coupling, cell adhesion, contact-dependent growth control and cell-shape regulation; and ATG9A supports vesicle trafficking and autophagosome assembly. The co-abundance graph is sparse and links CHD1 with INCENP and TRMT5, while INCENP links with NF2 and NF2 links with ATG9A. Thus, the most defensible interpretation is a possible coordinated program involving cell proliferation or progenitor-state biology together with chromatin regulation, membrane organization and cellular quality control. These are functional interpretations from individual gene annotations, not globally significant enrichment claims.

**Cell composition.** This is not a plasma-protein or secreted-protein module: none of the genes is annotated as secreted. The HPA evidence also does not support a uniform lung tissue program. Most genes have low tissue specificity, while the tissue-enhanced signals point separately to bone marrow and skeletal muscle. Every gene has some cell-type-enhanced annotation, including hematopoietic progenitor or myeloid populations for CHD1 and INCENP, neural or germ-cell populations for ATG9A and TRMT5, and late spermatids for NF2. Blood-cell specificity is low for most genes, with a group-enriched signal for INCENP and enriched basophil and NK-cell annotations. Protein detection in lung is mixed: NF2 and TRMT5 are detected, whereas CHD1, INCENP and ATG9A are not detected. The shared module may therefore reflect shared cellular composition, progenitor or proliferative states, or sample-level covariation rather than a lung-specific extracellular program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship is reported among the module genes, and no STRING functional-enrichment result is available. No hu.MAP complex contains multiple module members. The co-abundance links are therefore not corroborated by the supplied physical-interaction or complex resources. This does not disprove coordinated regulation: co-abundance can arise from shared cell states, transcriptional programs, localization, or indirect regulation. It does mean that the module is not supported here as a known physical protein complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The cross-tissue co-abundance association appears potentially novel because the supplied resources contain neither high-confidence STRING links nor a shared hu.MAP complex, and no globally significant GO or KEGG term defines the module. However, it should not be called a newly discovered biological mechanism. Absence from STRING and hu.MAP is not proof of novelty, and the sparse network plus heterogeneous HPA cell-type signals provide plausible alternative explanations involving cell composition or coordinated abundance of unrelated cellular programs. Novelty should therefore be stated as a candidate observation requiring replication in independent cohorts, adjustment for cellular composition, and experimental testing.

**Hypothesis.** Hypothesis: in shared circulatory-system and lung samples, a cell-state or progenitor-associated program may coordinately increase chromatin accessibility and transcriptional capacity through CHD1, maintain mitotic chromosome and cytokinesis machinery through INCENP, regulate membrane–cytoskeleton organization through NF2, support vesicle and autophagy processes through ATG9A, and sustain RNA modification through TRMT5. A simpler alternative hypothesis is that the apparent module is generated by correlated mixtures of proliferative or hematopoietic cells and other cell types rather than by direct mechanistic coupling among all five proteins.

Web sources: https://en.wikipedia.org/wiki/CHD1; https://www.genecards.org/card/CHD1; https://www.genecards.org/card/TRMT5

### Important genes

#### CHD1

- **Related proteins** (co-abundance neighbors): INCENP (0.87), TRMT5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromodomain helicase DNA binding protein 1. The CHD family of proteins is characterized by the presence of chromo (chromatin organization modifier) domains and SNF2-related helicase/ATPase domains.  CHD genes alter gene expression possibly by modification of chromatin structure thus altering access of the transcriptional apparatus to its chromosomal DNA template. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: intellectual disability with language impairment (0.714); gestational diabetes (0.363); breast carcinoma (0.349); developmental and epileptic encephalopathy (0.340); nervous system disorder (0.255)
- **Europe PMC papers**: 4137
- **Why important**: CHD1 is highly connected within the module, linking to INCENP and TRMT5, and is a chromatin remodeler with chromodomains and an SNF2-related helicase or ATPase domain. Its supplied annotations implicate chromatin remodeling and nucleosome organization. It also has substantial literature coverage and disease associations including intellectual disability with language impairment and developmental epileptic encephalopathy. Its HPA annotation in monocytes and neutrophils makes it relevant to a possible blood or cell-state explanation.
- **Conclusion**: Established evidence supports CHD1 as a chromatin and transcriptional regulator and as a central network connector. The module data do not establish that CHD1 drives the shared circulatory-system and lung signal; its involvement in a common progenitor or immune-cell state is a hypothesis.

#### INCENP

- **Related proteins** (co-abundance neighbors): CHD1 (0.87), NF2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nuclear bodies, Kinetochore; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inner centromere protein. In mammalian cells, 2 broad groups of centromere-interacting proteins have been described: constitutively binding centromere proteins and 'passenger,' or transiently interacting, proteins (reviewed by Choo, 1997). The constitutive proteins include CENPA (centromere protein A; MIM 117139), CENPB (MIM 117140), CENPC1 (MIM 117141), and CENPD (MIM 117142). The term 'passenger proteins' encompasses a b…
- **Diseases (Open Targets)**: prostate carcinoma (0.527); clear cell renal carcinoma (0.438); renal carcinoma (0.438); nephronophthisis (0.259); Lyme disease (0.237)
- **Europe PMC papers**: 9760
- **Why important**: INCENP is highly connected, linking CHD1 and NF2, and has a well-defined role in the mitotic passenger machinery, chromosome segregation, spindle midzone assembly and cytokinesis. It has the largest supplied literature volume among the module genes and shows tissue enhancement in bone marrow, with annotations in erythrocyte, megakaryocyte, monocyte and neutrophil progenitors as well as basophils and NK cells. These features make it especially informative for interpreting a possible proliferative or hematopoietic component.
- **Conclusion**: Established evidence supports INCENP as a mitotic and progenitor-associated gene. Its network position and bone-marrow-related HPA pattern support a possible cell-composition contribution, but they do not prove that mitosis is the function of the entire module.

#### NF2

- **Related proteins** (co-abundance neighbors): ATG9A (0.84), INCENP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NF2, moesin-ezrin-radixin like (MERLIN) tumor suppressor. This gene encodes a protein that is similar to some members of the ERM (ezrin, radixin, moesin) family of proteins that link cytoskeletal components with proteins in the cell membrane. The encoded protein is involved in regulation of contact-dependent inhibition of cell proliferation and functions in cell-cell adhesion and transmembrane signaling. The encoded protein has been shown to interact wit…
- **Diseases (Open Targets)**: NF2-related schwannomatosis (0.851); schwannomatosis (0.680); SMARCB1-related schwannomatosis (0.651); familial meningioma (0.628); acoustic neuroma (0.623)
- **Europe PMC papers**: 12172
- **Why important**: NF2 connects the mitotic-associated INCENP side of the graph to ATG9A, placing it at the interface between cell division or adhesion-related biology and vesicle or autophagy biology. It encodes merlin, a membrane-associated cytoskeletal regulator involved in cell shape, cell adhesion, contact-dependent inhibition of proliferation and transmembrane signaling. It has strong disease relevance for NF2-related schwannomatosis, schwannomatosis, familial meningioma and acoustic neuroma, and it is detected in lung by HPA immunohistochemistry.
- **Conclusion**: Established evidence supports NF2 as a membrane–cytoskeleton and growth-control regulator with direct relevance to lung protein detection. Its bridging position suggests a possible coordinating role, but the supplied data cannot distinguish direct regulation from correlated abundance or shared cell-type composition.

#### ATG9A

- **Related proteins** (co-abundance neighbors): NF2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: autophagy related 9A. Acts upstream of or within autophagosome assembly. Located in endosome; phagophore assembly site; and trans-Golgi network. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); lysosomal storage disease (0.370); cancer (0.094); neoplasm (0.091); triple-negative breast carcinoma (0.076)
- **Europe PMC papers**: 2152
- **Why important**: ATG9A is the terminal network member connected to NF2 and is the module's clearest autophagy and vesicle-biology representative. Its supplied annotations include autophagosome assembly, mitophagy, autophagy, membrane phospholipid scrambling and localization to the phagophore assembly site. HPA associates it with skeletal muscle and several neural cell types, while disease associations include neurodegenerative and lysosomal storage disease categories.
- **Conclusion**: Established evidence supports ATG9A as a membrane-trafficking and autophagy regulator. Its connection to NF2 motivates a hypothesis about coupling membrane organization to quality-control pathways, but there is no supplied physical-interaction or enrichment evidence establishing that mechanism in this module.

#### TRMT5

- **Related proteins** (co-abundance neighbors): CHD1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tRNA methyltransferase 5. tRNAs contain as many as 13 or 14 nucleotides that are modified posttranscriptionally by enzymes that are highly specific for particular nucleotides in the tRNA structure. TRMT5 methylates the N1 position of guanosine-37 (G37) in selected tRNAs using S-adenosyl methionine (Brule et al., 2004 [PubMed 15248782]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Combined oxidative phosphorylation defect type 26 (0.765); neurodegenerative disease (0.503); mitochondrial disease (0.372); hereditary disease (0.193); Intellectual disability (0.118)
- **Europe PMC papers**: 275
- **Why important**: TRMT5 is connected to CHD1 and provides a distinct RNA and mitochondrial dimension. It methylates guanosine in selected tRNAs and is annotated for tRNA and mitochondrial tRNA methylation. Its disease associations include combined oxidative phosphorylation defect type twenty-six, neurodegenerative disease and mitochondrial disease. HPA places it in the nucleoplasm and nucleoli and associates it with spermatid and spermatocyte cell types.
- **Conclusion**: Established evidence supports TRMT5 as a tRNA-modification enzyme with mitochondrial disease relevance. Its co-abundance with CHD1 may reflect a shared transcriptional or cellular-state program, but the module does not establish a mechanistic link between tRNA methylation and the other module processes.

## Module 9

**Tissue pair**: circulatory_system and lung  
**Genes (10)**: BAZ1A, CWC22, ERCC3, HAUS6, KLC2, MED24, PDXDC1, RBM15B, UPF2, XPO6

### Function

The module does not have a statistically supported GO or KEGG enrichment term: no term passed global correction. Its gene annotations instead point to a broad intracellular gene-expression and RNA-processing program, including transcriptional regulation, chromatin remodeling, RNA splicing, RNA export, nonsense-mediated decay, and nuclear transport. The network also includes microtubule and vesicle-related functions through HAUS6, KLC2, XPO6, and PDXDC1. Because the module is sparse and lacks coherent pathway enrichment, this should be interpreted as a functional neighborhood rather than a demonstrated single biochemical pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module; the HPA summary reports no secreted genes. Most genes have low tissue specificity and low immune-cell specificity, consistent with broadly expressed intracellular proteins rather than a tissue-exclusive program. Nevertheless, several cell-type-enhanced genes and the enrichment of BAZ1A and XPO6 in neutrophil-related HPA categories raise the possibility that part of the shared signal reflects cellular composition, particularly myeloid or progenitor-cell contributions. Brain and germ-cell-associated HPA patterns are also present, so the module is not specifically attributable to blood cells. Lung protein detection is common among the genes with available lung measurements, but this does not establish lung-specific function.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The co-abundance graph is sparse and does not show a dense established interaction complex. The only high-confidence STRING relationship is ERCC3–MED24, indicating that at least this pair has prior interaction support. No additional STRING functional-enrichment result is available, and no hu.MAP complex contains multiple module members. The remaining co-abundance links therefore should not be treated as experimentally established physical interactions. Instead, they may reflect shared expression, indirect regulation, common cell-type composition, or unrepresented interactions. The graph has several short links joining transcriptional, chromatin, RNA-processing, transport, and microtubule-related genes, but its structure does not demonstrate one unified molecular machine.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: ERCC3–MED24 (0.918)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a new co-abundance association in the circulatory-system and lung comparison, but the evidence is insufficient to call it a newly discovered biological complex or pathway. The presence of the known ERCC3–MED24 STRING relationship provides prior biological support for part of the signal, while the lack of hu.MAP support and the absence of broader STRING evidence leave most edges unvalidated. The lack of globally significant GO or KEGG enrichment further argues against claiming a novel, coherent pathway. A cautious interpretation is that the module is a potentially novel expression-level grouping of mostly intracellular genes whose biological reproducibility and tissue specificity require independent validation.

**Hypothesis.** Hypothesis: the module may reflect coordinated variation in general nuclear gene regulation and RNA quality control, coupled indirectly to intracellular transport and microtubule organization. ERCC3, MED24, BAZ1A, RBM15B, CWC22, and UPF2 could represent a transcriptional, chromatin, splicing, export, and RNA-surveillance axis, while KLC2, HAUS6, XPO6, and PDXDC1 could capture transport, cytoskeletal, or vesicular consequences of that state. In shared circulatory-system and lung samples, the observed co-abundance may be generated by a mixture of broadly expressed cellular programs and variable representation of neutrophil-related or other cell populations. This is a testable hypothesis, not an established pathway assignment.

### Important genes

#### ERCC3

- **Related proteins** (co-abundance neighbors): RBM15B (0.86), HAUS6 (0.82), UPF2 (0.81); STRING partners: MED24 (0.918)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ERCC excision repair 3, TFIIH core complex helicase subunit. This gene encodes an ATP-dependent DNA helicase that functions in nucleotide excision repair. The encoded protein is a subunit of basal transcription factor 2 (TFIIH) and, therefore, also functions in class II transcription. Mutations in this gene are associated with Xeroderma pigmentosum B, Cockayne's syndrome, and trichothiodystrophy. Alternative splicing results in multiple transcript variants.…
- **Diseases (Open Targets)**: xeroderma pigmentosum group B (0.790); trichothiodystrophy 2, photosensitive (0.707); xeroderma pigmentosum-Cockayne syndrome complex (0.683); trichothiodystrophy (0.677); xeroderma pigmentosum (0.673)
- **Europe PMC papers**: 2032
- **Why important**: ERCC3 is a central node in the module and connects to RBM15B, HAUS6, and UPF2. Its established function in nucleotide-excision repair and RNA polymerase II transcription gives the module a strong nuclear gene-regulation anchor. It also has substantial disease and literature support, including associations with xeroderma pigmentosum, Cockayne syndrome, and trichothiodystrophy. The ERCC3–MED24 relationship is the only high-confidence STRING interaction in the module.
- **Conclusion**: Established evidence supports ERCC3 as a DNA-repair and basal-transcription gene that may anchor part of the module. It is reasonable to hypothesize that its co-abundance with RNA-processing and chromatin genes reflects a shared nuclear regulatory state, but the module does not establish a new ERCC3 complex.

#### BAZ1A

- **Related proteins** (co-abundance neighbors): MED24 (0.82), HAUS6 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: bromodomain adjacent to zinc finger domain 1A. The BAZ1A gene encodes the accessory subunit of the ATP-dependent chromatin assembly factor (ACF), a member of the ISWI ('imitation switch') family of chromatin remodeling complexes (summarized by Racki et al., 2009 [PubMed 20033039]).[supplied by OMIM, Apr 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); non-small cell lung carcinoma (0.405); lung adenocarcinoma (0.395); hypothyroidism (0.391); psoriasis (0.346)
- **Europe PMC papers**: 666
- **Why important**: BAZ1A links MED24 and HAUS6 and therefore occupies a position between transcriptional regulation and chromosome or microtubule-related biology. Its established role in the ATP-dependent ACF chromatin-remodeling complex and nucleosome assembly makes it a plausible regulatory coordinator. HPA evidence shows bone-marrow enhancement and neutrophil-related cell-type enhancement, which is relevant to possible sample-composition effects. Its disease associations include lung cancer-related entries and other disorders, with a substantial literature record.
- **Conclusion**: Established evidence supports BAZ1A as a chromatin-remodeling factor with possible relevance to the cellular composition of the samples. Its bridge-like network position makes it a useful candidate for follow-up, but linking it mechanistically to the other module genes remains a hypothesis.

#### MED24

- **Related proteins** (co-abundance neighbors): BAZ1A (0.82), KLC2 (0.81); STRING partners: ERCC3 (0.918)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mediator complex subunit 24. This gene encodes a component of the mediator complex (also known as TRAP, SMCC, DRIP, or ARC), a transcriptional coactivator complex thought to be required for the expression of almost all genes. The mediator complex is recruited by transcriptional activators or nuclear receptors to induce gene expression, possibly by interacting with RNA polymerase II and promoting the formation of a transcripti…
- **Diseases (Open Targets)**: Short stature (0.323); chronic obstructive pulmonary disease (0.281); functional neutrophil defect (0.171); major depressive disorder (0.170); allergic rhinitis (0.149)
- **Europe PMC papers**: 610
- **Why important**: MED24 connects BAZ1A and KLC2 and is also linked to ERCC3 by the high-confidence STRING relationship. As a Mediator subunit, it is established as a transcriptional coactivator involved in RNA polymerase II initiation and elongation. Its disease associations include chronic obstructive pulmonary disease, functional neutrophil defect, and allergic rhinitis, which gives the gene contextual relevance to lung and circulatory biology. The gene also has substantial literature support.
- **Conclusion**: Established evidence supports MED24 as a transcriptional regulatory component and the best-supported interaction bridge in this module. A coordinated transcriptional state involving MED24, ERCC3, and BAZ1A is plausible, but the co-abundance data do not prove that all three operate in one physical complex.

#### KLC2

- **Related proteins** (co-abundance neighbors): CWC22 (0.82), MED24 (0.81), PDXDC1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin light chain 2. The protein encoded by this gene is a light chain of kinesin, a molecular motor responsible for moving vesicles and organelles along microtubules. Defects in this gene are a cause of spastic paraplegia, optic atrophy, and neuropathy (SPOAN) syndrome. [provided by RefSeq, Mar 2016].
- **Diseases (Open Targets)**: spastic paraplegia, optic atropy, and neuropathy (0.503); neurodegenerative disease (0.335); gout (0.204); Anal fistula (0.092); Anal fissure (0.092)
- **Europe PMC papers**: 481
- **Why important**: KLC2 is a network connector between CWC22, MED24, and PDXDC1. Its established function as a kinesin light chain places it in microtubule-dependent transport of vesicles and organelles, providing a cellular-transport counterpart to the module's nuclear and RNA-related genes. HPA shows brain tissue enhancement and enhancement in excitatory neurons, while the gene is associated with spastic paraplegia, optic atrophy, and neuropathy syndrome. Its position and function make it informative for testing whether the module reflects transport or cell-state differences rather than a single nuclear pathway.
- **Conclusion**: Established evidence supports KLC2 as a microtubule-based transport gene with neuronal relevance. Its connection to transcriptional and RNA-processing genes is currently an association in the co-abundance graph, so any mechanistic coupling is hypothetical.

#### XPO6

- **Related proteins** (co-abundance neighbors): HAUS6 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enriched; location Nucleoplasm, Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exportin 6. The protein encoded by this gene is a member of the importin-beta family. Members of this family are regulated by the GTPase Ran to mediate transport of cargo across the nuclear envelope. This protein has been shown to mediate nuclear export of profilin-actin complexes. A pseudogene of this gene is located on the long arm of chromosome 14. Alternative splicing results in multiple transcript varian…
- **Diseases (Open Targets)**: neurodegenerative disease (0.500); myocardial infarction (0.187); male reproductive system disorder (0.187); mathematical ability (0.187); intelligence (0.173)
- **Europe PMC papers**: 321
- **Why important**: XPO6 connects HAUS6 to the module and has an established role in Ran-regulated nuclear export, including export of profilin-actin complexes. HPA classifies it as enriched in neutrophils, making it particularly relevant to the possibility that cellular composition contributes to the shared signal. Its disease associations include neurodegenerative disease and myocardial infarction, while its network placement links nuclear transport to the HAUS6 microtubule and chromosome-segregation annotation.
- **Conclusion**: Established evidence supports XPO6 as a nuclear-export factor and identifies a plausible cell-composition clue through neutrophil enrichment. The proposed connection between XPO6, HAUS6, and the wider module is a hypothesis rather than a demonstrated physical or functional complex.

## Module 10

**Tissue pair**: circulatory_system and lung  
**Genes (21)**: BOD1L1, ARFGEF1, CLIP2, COG4, COQ9, FKBP15, GLYR1, ITSN2, ATF7IP, MED22, MINK1, MTMR1, NCOR1, NF1, RABEP2, SMARCA2, STRN, SYNRG, TASOR, TMF1, TRAPPC8

### Function

No GO/KEGG term passed global correction, so there is no statistically established pathway-level annotation from the primary enrichment analysis. Gene functions instead suggest a mixed intracellular regulatory module involving chromatin and transcriptional control, vesicle trafficking, Golgi and endosomal organization, and signaling. ATF7IP, NCOR1, SMARCA2, TASOR, MED22, and GLYR1 support a nuclear regulatory component. COG4, TMF1, TRAPPC8, ARFGEF1, SYNRG, ITSN2, and RABEP2 support intracellular trafficking. MINK1, STRN, NF1, and MTMR1 support kinase, phosphatase, Ras, MAPK, adhesion, and phosphoinositide-related processes. Because the network is sparse and STRING reports no functional enrichment, this is an integrated functional interpretation rather than a formally enriched pathway assignment.

**Cell composition.** The module contains no secreted genes, so it is not a plasma-protein or secretome module. Most genes have low tissue specificity, and most have low immune-cell specificity, arguing against a module defined simply by a circulating blood-cell signature. HPA does show cell-type enhancement for many genes, including recurring signals in neutrophils, neutrophil progenitors, microglia, and esophageal apical cells. BOD1L1, TRAPPC8, and FKBP15 show immune-cell enhancement in neutrophils, basophils, and non-classical monocytes, respectively. Shared cell types or sample-composition effects therefore remain plausible in the circulatory-system and lung comparison, although the module is not predominantly blood-cell-specific. Frequent protein detection in lung supports detectability there but does not establish lung-specific function.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supplies two high-confidence within-module relationships: MINK1--STRN and NCOR1--SMARCA2. These support a STRN-associated signaling scaffold and a chromatin-coregulator relationship. hu.MAP independently places STRN and MINK1 together in complexes (hu.MAP huMAP3_00935.1), (hu.MAP huMAP3_07620.1), (hu.MAP huMAP3_07644.1), (hu.MAP huMAP3_09709.1), and (hu.MAP huMAP3_10333.1), consistent with a STRIPAK-like or phosphatase-associated signaling context. ITSN2 and SYNRG repeatedly occur together in complexes (hu.MAP huMAP3_12376.1), (hu.MAP huMAP3_10876.1), (hu.MAP huMAP3_10762.1), (hu.MAP huMAP3_12918.1), and (hu.MAP huMAP3_12394.1), supporting clathrin, adaptor-complex, endosomal, and intracellular trafficking biology. Because these complexes contain many proteins absent from the module, they validate local relationships rather than showing that the complete module is one physical complex. The limited STRING connectivity and absence of STRING enrichment indicate that most co-abundance edges are not already represented as high-confidence physical or functional interactions.

**STRING interactions (score >= 0.7)**: 2 of 210 gene pairs: MINK1–STRN (0.95); NCOR1–SMARCA2 (0.782)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00935.1 (STRN, MINK1; 2/12); huMAP3_07620.1 (STRN, MINK1; 2/15); huMAP3_07644.1 (STRN, MINK1; 2/19); huMAP3_12376.1 (ITSN2, SYNRG; 2/32); huMAP3_10876.1 (ITSN2, SYNRG; 2/40); huMAP3_09709.1 (STRN, MINK1; 2/57); huMAP3_10762.1 (ITSN2, SYNRG; 2/62); huMAP3_12918.1 (ITSN2, SYNRG; 2/62); huMAP3_10333.1 (STRN, MINK1; 2/63); huMAP3_12394.1 (ITSN2, SYNRG; 2/98)

### Novelty

This module is not demonstrably a wholly new molecular mechanism. Several components recapitulate known biology: MINK1 and STRN have a high-confidence STRING relationship; STRN and MINK1 recur together in hu.MAP complexes; ITSN2 and SYNRG recur in vesicle-trafficking complexes; and NCOR1 and SMARCA2 have a STRING relationship. The potentially novel observation is the shared co-abundance of otherwise distinct regulatory, trafficking, and signaling components across circulatory_system and lung. That interpretation remains provisional because no GO/KEGG term passed global correction, STRING reports no functional enrichment, direct interaction support is sparse, and cell-composition effects are possible. Absence from STRING or hu.MAP alone does not establish novelty.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of intracellular trafficking and cell-state signaling coupled to chromatin-mediated transcriptional control. STRN and MINK1 may form a signaling or phosphatase-associated scaffold, while ITSN2 and SYNRG may organize endocytic and adaptor-linked trafficking. ATF7IP, NCOR1, SMARCA2, TASOR, and MED22 could connect cytoplasmic or membrane-associated state changes to transcriptional and chromatin responses. COG4, TMF1, TRAPPC8, and ARFGEF1 could support the Golgi and vesicular infrastructure involved in this coordination. The shared signal may instead arise from a common epithelial or immune-cell state in lung and circulatory-system samples rather than from one universal pathway. This hypothesis requires cell-resolved, perturbational, and physical-interaction validation.

### Important genes

#### ATF7IP

- **Related proteins** (co-abundance neighbors): NCOR1 (0.91), SYNRG (0.86), MINK1 (0.84), SMARCA2 (0.84), COG4 (0.83), TRAPPC8 (0.82), TASOR (0.81), RABEP2 (0.81), GLYR1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: activating transcription factor 7 interacting protein. ATF7IP is a multifunctional nuclear protein that associates with heterochromatin. It can act as a transcriptional coactivator or corepressor depending upon its binding partners (summary by Liu et al., 2009 [PubMed 19106100]).[supplied by OMIM, Nov 2010].
- **Diseases (Open Targets)**: breast carcinoma (0.389); alcohol drinking (0.375); neurodegenerative disease (0.370); schizophrenia (0.355); prostate carcinoma (0.293)
- **Europe PMC papers**: 675
- **Why important**: ATF7IP is the strongest network connector and links NCOR1, SYNRG, MINK1, SMARCA2, COG4, TRAPPC8, TASOR, and RABEP2. It is a multifunctional nuclear protein associated with heterochromatin and can act as a transcriptional coactivator or corepressor depending on binding partners. It therefore connects the module's nuclear regulatory genes to trafficking and signaling genes. HPA shows broad tissue distribution with cell-type enhancement in B-cells and neutrophil progenitors, and its literature base is substantial.
- **Conclusion**: Established evidence supports ATF7IP as a network hub and chromatin-associated transcriptional regulator. It is a strong candidate for the nuclear arm of the module, but co-abundance does not establish that it mechanistically controls the other genes.

#### STRN

- **Related proteins** (co-abundance neighbors): SMARCA2 (0.83), ITSN2 (0.82), FKBP15 (0.82); STRING partners: MINK1 (0.95)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_00935.1, huMAP3_07620.1, huMAP3_07644.1, huMAP3_09709.1, huMAP3_10333.1
- **Function (MyGene.info)**: striatin. Enables armadillo repeat domain binding activity; estrogen receptor binding activity; and protein phosphatase 2A binding activity. Involved in Wnt signaling pathway and negative regulation of cell population proliferation. Located in bicellular tight junction. Part of FAR/SIN/STRIPAK complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: cancer (0.619); heart failure (0.457); atrial fibrillation (0.439); hypertrophic cardiomyopathy (0.404); thyroid gland papillary carcinoma (0.380)
- **Europe PMC papers**: 1350
- **Why important**: STRN has a high-confidence STRING relationship with MINK1 and occurs with MINK1 in hu.MAP complexes (hu.MAP huMAP3_00935.1), (hu.MAP huMAP3_07620.1), (hu.MAP huMAP3_07644.1), (hu.MAP huMAP3_09709.1), and (hu.MAP huMAP3_10333.1). It binds protein phosphatase two A, participates in the FAR/SIN/STRIPAK complex, and is associated with Wnt, Hippo, signal-transduction, cell-proliferation, and tight-junction biology. Its disease associations include cancer, heart failure, atrial fibrillation, and cardiomyopathy, with a substantial literature.
- **Conclusion**: Established evidence identifies STRN as the best-supported signaling-scaffold anchor of the module. Its cardiovascular disease associations are relevant to the tissue pair, but it is unproven whether STRN drives the shared co-abundance pattern or marks a common cell state.

#### MINK1

- **Related proteins** (co-abundance neighbors): SYNRG (0.86), ATF7IP (0.84), COQ9 (0.82); STRING partners: STRN (0.95)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_00935.1, huMAP3_07620.1, huMAP3_07644.1, huMAP3_09709.1, huMAP3_10333.1
- **Function (MyGene.info)**: misshapen like kinase 1. This gene encodes a serine/threonine kinase belonging to the germinal center kinase (GCK) family. The protein is structurally similar to the kinases that are related to NIK and may belong to a distinct subfamily of NIK-related kinases within the GCK family. Studies of the mouse homolog indicate an up-regulation of expression in the course of postnatal mouse cerebral development and activation of t…
- **Diseases (Open Targets)**: Alzheimer disease (0.326); neurodegenerative disease (0.318); Parkinson disease (0.316); lysosomal storage disease (0.316); obesity disorder (0.301)
- **Europe PMC papers**: 621
- **Why important**: MINK1 has a high-confidence STRING relationship with STRN, appears with STRN in hu.MAP complexes (hu.MAP huMAP3_00935.1), (hu.MAP huMAP3_07620.1), (hu.MAP huMAP3_07644.1), (hu.MAP huMAP3_09709.1), and (hu.MAP huMAP3_10333.1), and connects to SYNRG, ATF7IP, and COQ9 in the network. It is a serine/threonine kinase associated with MAPK, JNK, p38, cell-matrix adhesion, phosphorylation, synaptic signaling, and brain development. Its disease associations include neurodegenerative and lysosomal-storage disorders, Parkinson disease, Alzheimer disease, and obesity.
- **Conclusion**: Established evidence supports MINK1 as a plausible signaling effector in the STRN-associated portion of the module. Its involvement in stress, adhesion, or differentiation in these tissues remains a hypothesis.

#### ITSN2

- **Related proteins** (co-abundance neighbors): STRN (0.82), FKBP15 (0.82), TMF1 (0.81), SMARCA2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12376.1, huMAP3_10876.1, huMAP3_10762.1, huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: intersectin 2. This gene encodes a cytoplasmic protein which contains SH3 domains. This protein is a member of a family of proteins involved in clathrin-mediated endocytosis. Intersectin 2 is thought to regulate the formation of clathrin-coated vesicles and also may function in the induction of T cell antigen receptor (TCR) endocytosis. [provided by RefSeq, Jan 2017].
- **Diseases (Open Targets)**: urinary system disorder (0.243); muscular disease (0.198); schizophrenia (0.194); respiratory tract infectious disorder (0.159); B-cell non-Hodgkin lymphoma (0.153)
- **Europe PMC papers**: 469
- **Why important**: ITSN2 links STRN, FKBP15, TMF1, and SMARCA2 in the co-abundance network and repeatedly occurs with SYNRG in hu.MAP trafficking complexes (hu.MAP huMAP3_12376.1), (hu.MAP huMAP3_10876.1), (hu.MAP huMAP3_10762.1), (hu.MAP huMAP3_12918.1), and (hu.MAP huMAP3_12394.1). It is an SH3-domain protein involved in clathrin-mediated endocytosis, endosomal transport, and T-cell-receptor endocytosis. HPA shows enhancement in esophageal apical cells and neutrophils, and its disease associations include respiratory tract infectious disorder and B-cell non-Hodgkin lymphoma.
- **Conclusion**: Established evidence supports ITSN2 as an endocytic and trafficking component that may connect membrane events to the broader module. Its lung and immune-cell relevance is compatible with the tissue-pair signal, but the module does not establish that ITSN2-specific endocytosis is dominant.

#### SMARCA2

- **Related proteins** (co-abundance neighbors): ATF7IP (0.84), STRN (0.83), ITSN2 (0.81); STRING partners: NCOR1 (0.782)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SWI/SNF related BAF chromatin remodeling complex subunit ATPase 2. The protein encoded by this gene is a member of the SWI/SNF family of proteins and is highly similar to the brahma protein of Drosophila. Members of this family have helicase and ATPase activities and are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/…
- **Diseases (Open Targets)**: intellectual disability-sparse hair-brachydactyly syndrome (0.854); blepharophimosis-impaired intellectual development syndrome (0.694); hereditary disease (0.527); Intellectual disability (0.501); blepharophimosis - intellectual disability syndrome (0.434)
- **Europe PMC papers**: 3654
- **Why important**: SMARCA2 connects ATF7IP, STRN, and ITSN2 and has a STRING relationship with NCOR1. It is an ATP-dependent SWI/SNF chromatin-remodeling ATPase involved in regulation of DNA-templated transcription and cell proliferation. HPA shows low tissue specificity with enhancement in innate lymphoid cells. Its disease associations include intellectual-disability syndromes and hereditary disease, and it has a particularly extensive literature.
- **Conclusion**: Established evidence supports SMARCA2 as a chromatin-remodeling effector and independently supports the NCOR1--SMARCA2 regulatory link. Its proximity to trafficking genes suggests possible cross-compartment coupling, but that coupling is not established by the available evidence.

## Module 11

**Tissue pair**: circulatory_system and lung  
**Genes (24)**: CDKN2AIP, DNAJC10, ADAR, FASTKD2, GTPBP10, LACTB, NOL6, PPIL1, PRPF31, CRYZ, MRPL10, RNF213, PDCD11, MRPS27, MRPS35, SIPA1L3, SUN1, LARS1, TACO1, GTF3C2, GTF3C4, SNRNP200, EFTUD2, UBTF

### Function

The strongest interpretation is a conserved intracellular RNA-handling and translation-support module. The primary evidence is global enrichment for ribonucleoprotein complex (GO:CC ribonucleoprotein complex; q_global = 0.00332), RNA binding (GO:MF RNA binding; q_global = 0.00676), nucleic acid binding (GO:MF nucleic acid binding; q_global = 0.0121), and mitochondrial translation (GO:BP mitochondrial translation; q_global = 0.0398). The genes represent several connected processes: nucleolar ribosome biogenesis through NOL6, PDCD11 and UBTF; spliceosomal RNA processing through SNRNP200, EFTUD2, PRPF31, PPIL1 and ADAR; mitochondrial RNA processing and translation through MRPL10, MRPS27, MRPS35, FASTKD2, GTPBP10 and TACO1; and RNA polymerase III transcription through GTF3C2 and GTF3C4. Thus, the module is better viewed as a coordinated RNA-processing, ribosome-production and mitochondrial protein-synthesis program than as a tissue-specific signaling pathway. The STRING results independently support ribonucleoprotein and RNA-binding organization (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.00063) (STRING Component Ribonucleoprotein complex; within-query FDR = 0.0024) (STRING Function RNA binding; within-query FDR = 0.0053) and also connect mitochondrial ribosome and mitochondrial gene-expression functions (STRING NetworkNeighborAL Organellar ribosome, and Regulation of mitochondrial gene expression; within-query FDR = 0.0158). The absence of a more specific biological-process term does not invalidate the module; it suggests that the shared signal spans related RNA and translation systems.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and protein detection is common in lung, which is consistent with a broadly expressed intracellular program rather than a lung-exclusive function. The module also does not show a blood-cell-enriched composition: immune-cell specificity is generally low, no enriched blood-cell category is reported, and one gene is not detected in immune cells. Cell-type-enhanced annotations are nevertheless frequent, including early spermatids, neutrophils, trophoblasts, epithelial populations and other specialized cells. These annotations may reflect shared cellular states or differences in cell composition across samples, but they do not support interpreting the module primarily as circulating blood or immune-cell contamination. The shared circulatory-system and lung signal therefore most plausibly reflects a conserved housekeeping-like RNA and mitochondrial program present in relevant cells of both tissues.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC ribonucleoprotein complex | 0.00332 | ADAR, EFTUD2, MRPL10, MRPS27, MRPS35, NOL6, PDCD11, PPIL1, PRPF31, SNRNP200 |
| GO:MF RNA binding | 0.00676 | ADAR, CDKN2AIP, CRYZ, EFTUD2, FASTKD2, GTPBP10, MRPL10, MRPS27, MRPS35, NOL6, PDCD11, PRPF31, SNRNP200, TACO1, UBTF |
| GO:MF nucleic acid binding | 0.0121 | ADAR, CDKN2AIP, CRYZ, EFTUD2, FASTKD2, GTF3C2, GTF3C4, GTPBP10, MRPL10, MRPS27, MRPS35, NOL6, PDCD11, PRPF31, SNRNP200, TACO1, UBTF |
| GO:BP mitochondrial translation | 0.0398 | FASTKD2, MRPL10, MRPS27, MRPS35, TACO1 |

### STRING and hu.MAP

STRING contains established relationships within three recognizable parts of the module. SNRNP200, EFTUD2, PRPF31 and PPIL1 form a strongly supported spliceosomal interaction group, with EFTUD2 also connected to PDCD11. MRPL10, MRPS27 and MRPS35 form a mitochondrial ribosomal group, with links to GTPBP10, while FASTKD2 is linked to TACO1. GTF3C2 and GTF3C4 are also a strongly supported transcription-factor pair. These relationships are consistent with the functional enrichments (8 supplementary STRING terms; within-query FDR 0.00063–0.0427) and show that part of the co-abundance structure recapitulates known molecular machinery. hu.MAP independently identifies spliceosomal complexes containing SNRNP200, EFTUD2, PRPF31 and PPIL1 (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1), (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_00960.1) (hu.MAP huMAP3_07622.1) (hu.MAP huMAP3_10875.1) (hu.MAP huMAP3_06726.1), mitochondrial-ribosome or mitochondrial-RNA complexes containing MRPL10, FASTKD2 and CDKN2AIP (hu.MAP huMAP3_08458.1) (hu.MAP huMAP3_09113.1) (hu.MAP huMAP3_09483.1) (hu.MAP huMAP3_06589.1), (hu.MAP huMAP3_06439.1), (hu.MAP huMAP3_07939.1), and a mitochondrial ribosomal complex containing MRPS27 and MRPS35 (hu.MAP huMAP3_05807.1). However, many module genes have no listed STRING partner or hu.MAP complex assignment, and the resources do not establish one physical complex containing the entire module. The network therefore appears to combine several known RNA and translation subsystems whose expression is coordinated, rather than representing a single experimentally defined protein complex.

**STRING interactions (score >= 0.7)**: 13 of 276 gene pairs: EFTUD2–PDCD11 (0.828); EFTUD2–PPIL1 (0.999); EFTUD2–PRPF31 (0.999); EFTUD2–SNRNP200 (0.999); FASTKD2–TACO1 (0.769); GTF3C2–GTF3C4 (0.993); GTPBP10–MRPL10 (0.824); MRPL10–MRPS27 (0.932); MRPL10–MRPS35 (0.969); MRPS27–MRPS35 (0.991); NOL6–PDCD11 (0.999); PPIL1–SNRNP200 (0.959); PRPF31–SNRNP200 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Ribonucleoprotein complex (FDR = 0.00063, 10 genes); Component Ribonucleoprotein complex (FDR = 0.0024, 10 genes); Function RNA binding (FDR = 0.0053, 15 genes); NetworkNeighborAL Organellar ribosome, and Regulation of mitochondrial gene expression (FDR = 0.0158, 5 genes); COMPARTMENTS Spliceosomal complex (FDR = 0.0227, 5 genes); Function Nucleic acid binding (FDR = 0.0384, 16 genes); COMPARTMENTS U2-type spliceosomal complex (FDR = 0.0427, 4 genes); COMPARTMENTS U4/U6 x U5 tri-snRNP complex (FDR = 0.0427, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08501.1 (SNRNP200, EFTUD2, PPIL1; 3/47); huMAP3_09504.1 (SNRNP200, EFTUD2, PPIL1; 3/51); huMAP3_09945.1 (SNRNP200, EFTUD2, PPIL1; 3/61); huMAP3_08458.1 (MRPL10, CDKN2AIP, FASTKD2; 3/70); huMAP3_09113.1 (MRPL10, CDKN2AIP, FASTKD2; 3/72); huMAP3_09483.1 (MRPL10, CDKN2AIP, FASTKD2; 3/74); huMAP3_06589.1 (MRPL10, CDKN2AIP, FASTKD2; 3/79); huMAP3_08980.1 (SNRNP200, EFTUD2, PRPF31; 3/97); huMAP3_00960.1 (SNRNP200, EFTUD2; 2/8); huMAP3_07622.1 (SNRNP200, EFTUD2; 2/9); huMAP3_10875.1 (GTF3C2, GTF3C4; 2/14); huMAP3_06726.1 (SNRNP200, PPIL1; 2/37); huMAP3_06439.1 (MRPL10, FASTKD2; 2/57); huMAP3_07939.1 (MRPL10, FASTKD2; 2/68); huMAP3_05807.1 (MRPS35, MRPS27; 2/81)

### Novelty

The module-level finding should not be called a wholly new molecular mechanism. Its principal components and several of its internal relationships are already established by STRING and hu.MAP, and the enriched functions are canonical cellular processes. At the same time, the specific co-abundance module shared by circulatory_system and lung may be a new systems-level observation if this tissue-pair module has not previously been reported. The evidence supports cautious novelty at the level of cross-tissue coordination, not novelty of the individual genes, complexes or pathways. Absence of STRING or hu.MAP support for some edges is not evidence that those relationships are novel; it may reflect incomplete interaction coverage or co-regulation without direct physical binding. Independent validation across cohorts, cell compositions and perturbation experiments would be needed before claiming a new biological mechanism.

**Hypothesis.** Hypothesis: the shared module reflects a cell-intrinsic quality-control and biosynthetic state in which nucleolar RNA production and ribosome assembly, spliceosome activity, and mitochondrial RNA translation are coordinately maintained. In this model, increased demand for RNA maturation and protein synthesis couples nuclear RNA processing through the spliceosomal genes with mitochondrial gene expression through the mitoribosomal and mitochondrial RNA regulators. SUN1, SIPA1L3 and RNF213 may provide context-dependent links to nuclear architecture, cell polarity or vascular and epithelial state, but the present data establish co-abundance rather than causal regulation. A testable prediction is that perturbing the spliceosomal or mitochondrial translation components would alter the abundance or activity of the other subsystem in relevant lung and circulatory-system cell types.

### Important genes

#### SNRNP200

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.86), SUN1 (0.83); STRING partners: EFTUD2 (0.999), PPIL1 (0.959), PRPF31 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_08980.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_06726.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is a central spliceosomal helicase and a prominent connector of the module's spliceosome-related genes. It participates in multiple hu.MAP spliceosomal complexes (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1), (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_00960.1) (hu.MAP huMAP3_07622.1), (hu.MAP huMAP3_06726.1) and has established STRING links to EFTUD2, PRPF31 and PPIL1. It contributes to all three primary RNA and nucleic-acid enrichment themes (GO:CC ribonucleoprotein complex; q_global = 0.00332) (GO:MF RNA binding; q_global = 0.00676) (GO:MF nucleic acid binding; q_global = 0.0121). Its disease associations include retinitis pigmentosa and inherited retinal dystrophy, and it has substantial literature support.
- **Conclusion**: Established evidence supports SNRNP200 as a core component of pre-mRNA splicing and a major anchor of the module's spliceosomal substructure. It is a strong candidate for coordinating the RNA-processing arm, but the module does not establish that SNRNP200 drives the cross-tissue co-abundance pattern.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.86); STRING partners: PDCD11 (0.828), PPIL1 (0.999), PRPF31 (0.999), SNRNP200 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_08980.1, huMAP3_00960.1, huMAP3_07622.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 connects directly to the spliceosomal genes in STRING and appears in several hu.MAP spliceosomal complexes (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1), (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_00960.1) (hu.MAP huMAP3_07622.1). It is represented in the primary ribonucleoprotein, RNA-binding and nucleic-acid-binding enrichments (GO:CC ribonucleoprotein complex; q_global = 0.00332) (GO:MF RNA binding; q_global = 0.00676) (GO:MF nucleic acid binding; q_global = 0.0121). Its established role in spliceosomal assembly and conformational change, together with the association of pathogenic variation with mandibulofacial dysostosis with microcephaly, makes it biologically important. Its literature volume is substantial.
- **Conclusion**: Established evidence identifies EFTUD2 as a spliceosome component that reinforces the module's RNA-processing interpretation. Its position in the module is consistent with a conserved splicing program, while any role in coupling splicing to mitochondrial translation remains a hypothesis.

#### NOL6

- **Related proteins** (co-abundance neighbors): SIPA1L3 (0.83), MRPS27 (0.82), PDCD11 (0.81), GTF3C2 (0.80); STRING partners: PDCD11 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleolar protein 6. The nucleolus is a dense subnuclear membraneless organelle that assembles around clusters of rRNA genes and functions in ribosome biogenesis. This gene encodes a nucleolar RNA-associated protein that is highly conserved between species. RNase treatment of permeabilized cells indicates that the nucleolar localization is RNA dependent. Further studies suggest that the protein is associated with ribo…
- **Diseases (Open Targets)**: neurodegenerative disease (0.119); hepatocellular carcinoma (0.054); hidradenitis (0.052); response to xenobiotic stimulus (0.045); gastric cancer (0.036)
- **Europe PMC papers**: 335
- **Why important**: NOL6 is a nucleolar RNA-associated protein involved in rRNA processing and small-subunit biogenesis. It is included in all three primary RNA and nucleic-acid enrichment terms (GO:CC ribonucleoprotein complex; q_global = 0.00332) (GO:MF RNA binding; q_global = 0.00676) (GO:MF nucleic acid binding; q_global = 0.0121), connects to PDCD11 in STRING, and links the nucleolar branch to MRPS27 and GTF3C2 within the co-abundance network. Its nucleolar localization and disease literature support make it an important bridge between RNA metabolism and ribosome production.
- **Conclusion**: Established evidence supports NOL6 as a core nucleolar ribosome-biogenesis factor and a plausible representative of the module's ribonucleoprotein arm. The network suggests coordination with mitochondrial and transcriptional genes, but does not prove direct biochemical coupling.

#### MRPL10

- **Related proteins** (co-abundance neighbors): MRPS35 (0.84); STRING partners: GTPBP10 (0.824), MRPS27 (0.932), MRPS35 (0.969)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_08458.1, huMAP3_09113.1, huMAP3_09483.1, huMAP3_06589.1, huMAP3_06439.1, huMAP3_07939.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein L10. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.532); Alzheimer disease (0.270); Parkinson disease (0.268); lysosomal storage disease (0.268); atrial fibrillation (0.079)
- **Europe PMC papers**: 327
- **Why important**: MRPL10 is a mitochondrial ribosomal protein and one of the clearest representatives of the mitochondrial translation branch. It contributes to every primary enrichment term, including mitochondrial translation (4 globally significant GO/KEGG terms, q_global 0.00332–0.0398; see the table), and has STRING links to MRPS27, MRPS35 and GTPBP10. It is present in multiple hu.MAP mitochondrial complexes (hu.MAP huMAP3_08458.1) (hu.MAP huMAP3_09113.1) (hu.MAP huMAP3_09483.1) (hu.MAP huMAP3_06589.1), (hu.MAP huMAP3_06439.1), (hu.MAP huMAP3_07939.1). Its disease associations include neurodegenerative and mitochondrial-relevant conditions, and its literature supports a recognized role in mitochondrial protein synthesis.
- **Conclusion**: Established evidence supports MRPL10 as an anchor of mitochondrial translation within the module. Its co-abundance with spliceosomal and nucleolar genes supports a coordinated biosynthetic state, but does not establish that mitochondrial translation is the primary driver.

#### FASTKD2

- **Related proteins** (co-abundance neighbors): PDCD11 (0.83), GTPBP10 (0.83); STRING partners: TACO1 (0.769)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08458.1, huMAP3_09113.1, huMAP3_09483.1, huMAP3_06589.1, huMAP3_06439.1, huMAP3_07939.1
- **Function (MyGene.info)**: FASTK mitochondrial RNA regulator 2. This gene encodes a protein that is localized in the mitochondrial inner compartment and that may play a role in mitochondrial apoptosis. Nonsense mutations have been reported to result in cytochrome c oxidase deficiency. [provided by RefSeq, Oct 2008].
- **Diseases (Open Targets)**: combined oxidative phosphorylation deficiency 44 (0.777); leigh syndrome due to mitochondrial complex iv deficiency (0.487); mitochondrial complex IV deficiency, nuclear-type (0.487); Leigh syndrome (0.453); mitochondrial disease (0.373)
- **Europe PMC papers**: 335
- **Why important**: FASTKD2 links mitochondrial RNA regulation with mitochondrial translation and apoptosis-related biology. It appears in the primary RNA-binding, nucleic-acid-binding and mitochondrial-translation enrichments (GO:MF RNA binding; q_global = 0.00676) (GO:MF nucleic acid binding; q_global = 0.0121) (GO:BP mitochondrial translation; q_global = 0.0398), connects to TACO1 in STRING, and is repeatedly represented in hu.MAP mitochondrial complexes (hu.MAP huMAP3_08458.1) (hu.MAP huMAP3_09113.1) (hu.MAP huMAP3_09483.1) (hu.MAP huMAP3_06589.1), (hu.MAP huMAP3_06439.1), (hu.MAP huMAP3_07939.1). Its established disease associations include combined oxidative-phosphorylation deficiency and Leigh syndrome, giving it strong functional and clinical relevance despite more limited literature volume than the major spliceosomal genes.
- **Conclusion**: Established evidence supports FASTKD2 as a mitochondrial RNA-processing factor that helps define the mitochondrial arm of the module. Its linkage to the nuclear RNA-processing branch is a plausible systems-level hypothesis rather than a demonstrated direct mechanism.

#### ADAR

- **Related proteins** (co-abundance neighbors): SUN1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR is an RNA-editing enzyme included in the primary ribonucleoprotein, RNA-binding and nucleic-acid-binding enrichments (GO:CC ribonucleoprotein complex; q_global = 0.00332) (GO:MF RNA binding; q_global = 0.00676) (GO:MF nucleic acid binding; q_global = 0.0121). It provides a functional connection between RNA processing and RNA quality control, and its HPA annotation includes neutrophils while retaining low overall immune-cell specificity. ADAR has very extensive literature support and established associations with Aicardi–Goutieres syndrome, dyschromatosis symmetrica hereditaria and ADAR-related interferonopathy.
- **Conclusion**: Established evidence supports ADAR as an RNA-editing and RNA-processing component of the module, with disease links demonstrating the importance of altered RNA surveillance. Its presence does not show that inflammation or neutrophils generate the module, and any immune-related interpretation should remain secondary to the broader intracellular RNA-processing explanation.

## Module 12

**Tissue pair**: circulatory_system and lung  
**Genes (7)**: CUX1, CUX1, DCAF13, GNL3L, KIF11, SLC12A7, USP36

### Function

The module does not have a globally significant GO or KEGG enrichment term, so its function should be inferred cautiously from its gene-level biology and network structure. The genes collectively point to intracellular maintenance and proliferative processes, including nucleolar ribosomal RNA processing, chromatin and transcriptional regulation, ubiquitin-dependent protein control, mitotic spindle organization, and ionic homeostasis. The strongest biological coherence is therefore a possible relationship between nuclear or nucleolar regulation, cell-cycle activity, and cellular homeostasis rather than a single established pathway. The sparse co-abundance structure and lack of STRING functional enrichment provide limited support for a unified canonical function. No GO or KEGG term passed global correction.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, while many show cell-type-enhanced expression. HPA points to neutrophils, monocytes, cardiomyocytes, progenitor populations, and germ-cell populations rather than a consistent lung or circulatory tissue lineage. Protein detection is reported for nearly all module genes in lung, whereas matching circulatory-system tissue detection is unavailable. The module may therefore reflect shared cellular composition, proliferative state, or broadly distributed intracellular programs in the sampled tissues. The HPA evidence does not support a specifically blood-cell-enriched module overall, although CUX1 has immune-cell-enhanced evidence and several genes are associated with hematopoietic or progenitor cell types.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was detected among the module genes, and STRING supplied no functional enrichment. This argues against a densely documented physical interaction network and makes the co-abundance relationships less likely to be explained by a well-known STRING-defined complex. The main external complex evidence is huMAP complex C1, which contains GNL3L and USP36 from the module together with RFC3, SKIC2, SKIC3, EME1, and DIDO1. Thus, the GNL3L–USP36 relationship has support from a curated complex context, but only a partial representation of that complex is present in the module. The remaining co-abundance links are not independently supported by the reported STRING or huMAP evidence.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09525.1 (GNL3L, USP36; 2/7)

### Novelty

The shared co-abundance pattern may represent a previously unreported association, because the module combines genes from nuclear regulation, nucleolar processing, mitosis, and ion transport without a globally significant pathway annotation or a matching STRING interaction network. However, it cannot be called a definitively new biological module from these data alone. The absence of STRING interactions or broad complex coverage is evidence of limited prior annotation, not proof of novelty. A more defensible conclusion is that this is a potentially novel tissue-pair co-abundance association requiring replication, cell-composition adjustment, and experimental or independent cohort validation.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular state in lung and circulatory-system samples in which proliferative or progenitor-like cells coordinate nucleolar and ribosomal processing with ubiquitin-dependent protein regulation, chromatin or transcriptional control, mitotic machinery, and ion or volume homeostasis. GNL3L and USP36 may provide a nucleolar and protein-stability axis supported by huMAP complex C1, while DCAF13 and KIF11 could connect regulatory protein turnover with spindle-related cell-cycle activity. CUX1 and SLC12A7 may mark transcriptional and ion-homeostatic components of the same cellular state. This hypothesis is not established by enrichment, because no GO or KEGG term passed global correction and the STRING network is empty.

### Important genes

#### GNL3L

- **Related proteins** (co-abundance neighbors): USP36 (0.82), DCAF13 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_09525.1
- **Function (MyGene.info)**: G protein nucleolar 3 like. The protein encoded by this gene appears to be a nucleolar GTPase that is essential for ribosomal pre-rRNA processing and cell proliferation. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, May 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.126); esophageal squamous cell carcinoma (0.092); alopecia (0.091); esophageal cancer (0.085); cancer (0.082)
- **Europe PMC papers**: 301
- **Why important**: GNL3L occupies a central position in the module's connected structure and is linked to USP36 and DCAF13. Its established annotation as a nucleolar GTPase involved in ribosomal pre-RNA processing and cell proliferation gives the module a plausible nucleolar and growth-related anchor. It is also one of the two module genes in huMAP complex C1. The literature volume is moderate, so its biological interpretation is more specific but less extensively established than that of heavily studied cell-cycle genes.
- **Conclusion**: Established evidence supports a nucleolar ribosome-processing and proliferation role, plus participation in huMAP complex C1 with USP36. The hypothesis that GNL3L organizes the shared module's broader co-abundance state remains unproven.

#### USP36

- **Related proteins** (co-abundance neighbors): CUX1 (0.82), GNL3L (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09525.1
- **Function (MyGene.info)**: ubiquitin specific peptidase 36. This gene encodes a member of the peptidase C19 or ubiquitin-specific protease family of cysteine proteases. Members of this family remove ubiquitin molecules from polyubiquitinated proteins. The encoded protein may deubiquitinate and stabilize the transcription factor c-Myc, also known as MYC, an important oncoprotein known to be upregulated in most human cancers. The encoded protease may also re…
- **Diseases (Open Targets)**: neurodegenerative disease (0.346); atrial fibrillation (0.344); Sjogren syndrome (0.218); liver cancer (0.216); myocardial ischemia (0.202)
- **Europe PMC papers**: 798
- **Why important**: USP36 is centrally connected with GNL3L and CUX1 and is the second module member in huMAP complex C1. Its established deubiquitinase activity, nucleolar localization, roles in chromatin or nucleolus organization, protein stability, and autophagy regulation make it a plausible regulatory counterpart to GNL3L. Its reported relationship with MYC stability and lung-related expression provides disease and tissue relevance, while its literature volume is substantial.
- **Conclusion**: Established evidence supports a nucleolar deubiquitination and protein-stability function and a relationship with GNL3L in C1. It is plausible, but not demonstrated, that USP36 helps couple nucleolar regulation to the shared tissue-pair co-abundance pattern.

#### CUX1

- **Related proteins** (co-abundance neighbors): CUX1 (0.93), SLC12A7 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cut like homeobox 1. The protein encoded by this gene is a member of the homeodomain family of DNA binding proteins. It may regulate gene expression, morphogenesis, and differentiation and it may also play a role in the cell cycle progession. Several alternatively spliced transcript variants encoding different isoforms have been identified.[provided by RefSeq, Feb 2011].
- **Diseases (Open Targets)**: global developmental delay with or without impaired intellectual development (0.754); cancer (0.588); myelodysplastic syndrome (0.536); hereditary disease (0.519); acute lymphoblastic leukemia (0.509)
- **Europe PMC papers**: 3914
- **Why important**: CUX1 has among the strongest apparent connectivity in the module and links to SLC12A7 and USP36. It is an established homeobox DNA-binding regulator involved in transcription, morphogenesis, differentiation, and cell-cycle progression. HPA associates it with neutrophils and non-classical monocytes, which is relevant to possible cellular-composition effects. Its extensive literature and disease associations, including developmental disorders, cancer, myelodysplastic syndrome, and acute lymphoblastic leukemia, make it an important interpretive marker.
- **Conclusion**: Established evidence supports transcriptional regulation and disease relevance, with HPA support for immune-cell-associated expression. The hypothesis that CUX1 coordinates the module's transcriptional component or explains its presence in shared samples is not established.

#### DCAF13

- **Related proteins** (co-abundance neighbors): KIF11 (0.90), GNL3L (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DDB1 and CUL4 associated factor 13. Enables estrogen receptor binding activity. Predicted to be involved in maturation of SSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Located in several cellular components, including centrosome; cytosol; and nuclear lumen. Part of Cul4-RING E3 ubiquitin ligase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.285); acute tonsillitis (0.133); breast cancer (0.105); breast carcinoma (0.099); hepatocellular carcinoma (0.087)
- **Europe PMC papers**: 311
- **Why important**: DCAF13 connects KIF11 with GNL3L, placing it at a bridge between spindle-related biology and the nucleolar component. Its established role as a DDB1 and CUL4-associated factor connects the module to ubiquitin-ligase activity, rRNA processing, oocyte growth, and meiotic spindle assembly. HPA shows cell-type-enhanced expression in cardiomyocytes and germ-cell populations, supporting a context-dependent cellular rather than secreted role. The literature volume is limited compared with CUX1 or KIF11, which makes it a potentially informative but less established module component.
- **Conclusion**: Established evidence supports ubiquitin-ligase-associated regulation and roles in rRNA processing and spindle-related processes. Its bridging role in this module and any functional connection between these processes remain hypotheses.

#### KIF11

- **Related proteins** (co-abundance neighbors): DCAF13 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Mid piece; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 11. This gene encodes a motor protein that belongs to the kinesin-like protein family. Members of this protein family are known to be involved in various kinds of spindle dynamics. The function of this gene product includes chromosome positioning, centrosome separation and establishing a bipolar spindle during cell mitosis. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: microcephaly with or without chorioretinopathy, lymphedema, or intellectual disability (0.821); hereditary disease (0.509); inherited retinal dystrophy (0.507); neurodegenerative disease (0.484); microcephaly (0.412)
- **Europe PMC papers**: 3618
- **Why important**: KIF11 is the module's spindle-motor component and is linked to DCAF13. Its established function in chromosome positioning, centrosome separation, bipolar spindle formation, and mitotic spindle organization provides a strong cell-cycle interpretation. HPA shows tissue enhancement in bone marrow and lymphoid tissue and cell-type enhancement in several progenitor populations, making it relevant to proliferative or hematopoietic cellular composition. Its literature volume is extensive and includes developmental disease associations.
- **Conclusion**: Established evidence supports a mitotic spindle and progenitor-cell biology role. The conclusion that KIF11 drives or mechanistically links the whole shared module is not justified by the sparse network and should remain a hypothesis.

#### SLC12A7

- **Related proteins** (co-abundance neighbors): CUX1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 12 member 7. Enables protein kinase binding activity. Predicted to be involved in several processes, including cell volume homeostasis; inorganic ion homeostasis; and inorganic ion transmembrane transport. Part of protein-containing complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: clonal hematopoiesis (0.462); myasthenia gravis (0.342); edema (0.233); brain compression (0.233); preeclampsia (0.198)
- **Europe PMC papers**: 577
- **Why important**: SLC12A7 is connected to CUX1 and contributes a distinct membrane-transport and homeostasis component. Its established annotations include chloride and potassium transport, inorganic ion homeostasis, cell-volume regulation, and protein-kinase binding. HPA shows tissue enhancement in heart muscle and cell-type enhancement in cardiomyocytes and several epithelial or renal cell types, which may help explain a shared cellular-state signal rather than a secreted-protein signal. Its literature volume is moderate, with disease associations including clonal hematopoiesis, edema, and preeclampsia.
- **Conclusion**: Established evidence supports ion transport and cell-volume homeostasis. Its relationship to the module's nuclear, nucleolar, and mitotic genes is not established and may reflect shared cell-state or sample-composition effects.

## Module 13

**Tissue pair**: circulatory_system and lung  
**Genes (6)**: CHD8, NCAPD3, COG8, MED23, ARHGAP5, ERCC4

### Function

The module does not have a statistically supported GO or KEGG functional enrichment signal: no term passed global correction. Its observed structure is a hub-and-spoke pattern centered on NCAPD3, with links to MED23, COG8, ERCC4, ARHGAP5 and CHD8. The member annotations span chromosome condensation and chromatin organization through NCAPD3, transcriptional regulation through MED23, Golgi trafficking and glycoprotein modification through COG8, DNA repair through ERCC4, Rho-GTPase regulation through ARHGAP5, and chromatin remodeling and transcriptional regulation through CHD8. Taken together, the most defensible interpretation is a cross-tissue co-abundance pattern involving broadly distributed intracellular maintenance processes, especially nuclear genome regulation, rather than a single established pathway. The functional interpretation remains hypothesis-generating because the module lacks globally significant GO or KEGG support globally significant GO/KEGG and has a sparse network.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins: all members are intracellular and the secreted-protein annotation is absent. HPA indicates low immune-cell specificity for every member and no enriched blood-cell category, arguing against a straightforward blood-cell-enrichment explanation. Most members have low tissue specificity, while one is tissue group-enriched and one is tissue-enhanced; the reported single-cell enrichments include cardiomyocytes, epicardial cells, erythrocyte progenitors, monocyte progenitors, Sertoli cells and early or late spermatids. These scattered cell-type associations do not define a coherent circulatory or lung cell population. The shared signal may therefore reflect broadly expressed intracellular programs, compositional variation among multiple cell types, or coordinated regulation in a subset of cells rather than a secreted or blood-cell module. Protein-level evidence in lung is incomplete and mixed, with detection for some members, non-detection for another, and no data for the remainder; there is no matching HPA tissue evidence for circulatory_system.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the specified high-confidence threshold, no STRING functional enrichment was reported, and no hu.MAP complex contained at least two module members. Thus the co-abundance edges are not corroborated by the supplied high-confidence protein-interaction or complex resources. The links may represent coordinated expression, indirect biology, shared cellular composition, technical covariance, or interactions that are absent from or below the coverage and confidence thresholds of these databases. The only clear network feature is the computational hub position of NCAPD3, which connects to every other member in the supplied subgraph; this is a network observation, not evidence that NCAPD3 physically binds all of them.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module is a potentially interesting co-abundance observation, but it cannot be called a new biological mechanism on the current evidence. Its lack of high-confidence STRING interactions and hu.MAP complexes supports that the particular combination is not represented in those resources, but database absence does not establish novelty. The absence of globally significant GO or KEGG enrichment, the lack of STRING enrichment, the sparse network, and the heterogeneous member annotations all limit mechanistic specificity. A cautious novelty claim is that this tissue-pair co-abundance pattern may be an under-characterized association requiring replication and external validation, rather than a newly discovered conserved complex or pathway.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of intracellular genome-maintenance and cell-state regulators in shared or variable cell populations across circulatory_system and lung. NCAPD3 may mark a chromatin and chromosome-organization component, while MED23 and CHD8 represent transcriptional and chromatin-regulatory state, ERCC4 represents DNA-repair capacity, COG8 represents secretory-pathway and Golgi maintenance, and ARHGAP5 represents cytoskeletal signaling control. The apparent coordination could arise from a common proliferative, stress-response, differentiation, or cell-composition program rather than direct physical interaction. This hypothesis should be tested by replication in independent tissue cohorts, cell-type-resolved analyses, protein-level measurements, and experimental examination of whether the co-abundance relationships persist within matched cell populations.

### Important genes

#### NCAPD3

- **Related proteins** (co-abundance neighbors): MED23 (0.85), COG8 (0.85), ERCC4 (0.84), ARHGAP5 (0.81), CHD8 (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: non-SMC condensin II complex subunit D3. Condensin complexes I and II play essential roles in mitotic chromosome assembly and segregation. Both condensins contain 2 invariant structural maintenance of chromosome (SMC) subunits, SMC2 (MIM 605576) and SMC4 (MIM 605575), but they contain different sets of non-SMC subunits. NCAPD3 is 1 of 3 non-SMC subunits that define condensin II (Ono et al., 2003 [PubMed 14532007]).[supplied by OMIM, Mar …
- **Diseases (Open Targets)**: microcephaly 22, primary, autosomal recessive (0.615); autosomal recessive primary microcephaly (0.504); alcohol drinking (0.305); urolithiasis (0.276); bronchiectasis (0.233)
- **Europe PMC papers**: 458
- **Why important**: NCAPD3 is the central network node, connected to every other module member and having the greatest supplied weighted degree. Its established function is as a non-SMC condensin II subunit involved in mitotic and meiotic chromosome condensation and chromatin organization. It therefore provides the strongest organizing signal for interpreting the module as potentially related to nuclear genome organization. Its disease associations include primary microcephaly and related neurodevelopmental disease, and its literature volume is substantial.
- **Conclusion**: Established evidence supports NCAPD3 as the computational hub and a condensin-II chromatin factor. It is a plausible module anchor, but the network does not establish direct binding to the other members or prove that condensin biology drives the tissue-pair association.

#### CHD8

- **Related proteins** (co-abundance neighbors): NCAPD3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromodomain helicase DNA binding protein 8. This gene encodes a member of the chromodomain-helicase-DNA binding protein family, which is characterized by a SNF2-like domain and two chromatin organization modifier domains. The encoded protein also contains brahma and kismet domains, which are common to the subfamily of chromodomain-helicase-DNA binding proteins to which this protein belongs. This gene has been shown to function in several pr…
- **Diseases (Open Targets)**: autism (0.679); hereditary disease (0.550); autism spectrum disorder (0.547); Intellectual disability (0.515); neurodevelopmental disorder (0.497)
- **Europe PMC papers**: 2541
- **Why important**: CHD8 is a nuclear chromatin-remodeling and transcriptional regulator connected directly to NCAPD3. Its annotated functions include chromatin remodeling, transcriptional regulation, messenger RNA processing and developmental processes. It has extensive literature and strong disease relevance to autism, intellectual disability and neurodevelopmental disorders. Its inclusion makes a shared genome-regulatory state more plausible than an interpretation based only on a single condensin gene.
- **Conclusion**: Established evidence supports CHD8 as a biologically important chromatin and transcription regulator. Its module association may indicate coordinated nuclear regulation, but a direct functional partnership with NCAPD3 in these tissues remains a hypothesis.

#### ERCC4

- **Related proteins** (co-abundance neighbors): NCAPD3 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ERCC excision repair 4, endonuclease catalytic subunit. The protein encoded by this gene forms a complex with ERCC1 and is involved in the 5' incision made during nucleotide excision repair. This complex is a structure specific DNA repair endonuclease that interacts with EME1. Defects in this gene are a cause of xeroderma pigmentosum complementation group F (XP-F), or xeroderma pigmentosum VI (XP6).[provided by RefSeq, Mar 2009].
- **Diseases (Open Targets)**: xeroderma pigmentosum group F (0.837); Fanconi anemia complementation group Q (0.808); xeroderma pigmentosum (0.780); xeroderma pigmentosum-Cockayne syndrome complex (0.731); XFE progeroid syndrome (0.730)
- **Europe PMC papers**: 2223
- **Why important**: ERCC4 is directly connected to the network hub and encodes the catalytic subunit of the ERCC1-ERCC4 nucleotide-excision-repair endonuclease. Its established roles include DNA repair, telomere maintenance, homologous-recombination repair and repair of other forms of genomic damage. It has extensive literature and strong disease associations with xeroderma pigmentosum, Fanconi anemia complementation group Q and XFE progeroid syndrome. It adds a genome-integrity dimension to the nuclear-regulatory interpretation.
- **Conclusion**: Established evidence supports ERCC4 as a DNA-repair factor with major human disease relevance. Its co-abundance with chromatin regulators could reflect coordinated genome-maintenance capacity, but the module does not demonstrate a shared DNA-repair pathway.

#### MED23

- **Related proteins** (co-abundance neighbors): NCAPD3 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mediator complex subunit 23. The activation of gene transcription is a multistep process that is triggered by factors that recognize transcriptional enhancer sites in DNA. These factors work with co-activators to direct transcriptional initiation by the RNA polymerase II apparatus. The protein encoded by this gene is a subunit of the CRSP (cofactor required for SP1 activation) complex, which, along with TFIID, is required for…
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.631); arginase deficiency (0.575); hereditary disease (0.471); type 2 diabetes mellitus (0.465); neurodegenerative disease (0.460)
- **Europe PMC papers**: 872
- **Why important**: MED23 is the direct neighbor of NCAPD3 and is a subunit of the mediator-related transcriptional coactivator machinery. Its annotations include regulation of RNA-polymerase-II transcription, transcription initiation, transcriptional elongation and positive regulation of gene expression. It has a substantial literature base and disease associations including autosomal-recessive intellectual disability and metabolic disease. It provides an independent transcriptional-regulation axis within the otherwise sparse module.
- **Conclusion**: Established evidence supports MED23 as a transcriptional co-regulatory factor. Its association with NCAPD3 is consistent with coordinated regulation of gene expression, but no direct interaction or shared tissue-specific mechanism is established here.

#### COG8

- **Related proteins** (co-abundance neighbors): NCAPD3 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: component of oligomeric golgi complex 8. This gene encodes a protein that is a component of the conserved oligomeric Golgi (COG) complex, a multiprotein complex that plays a structural role in the Golgi apparatus, and is involved in intracellular membrane trafficking and glycoprotein modification. Mutations in this gene cause congenital disorder of glycosylation, type IIh, a disease that is characterized by under-glycosylated serum prote…
- **Diseases (Open Targets)**: COG8-congenital disorder of glycosylation (0.788); neurodegenerative disease (0.430); Alzheimer disease (0.387); Parkinson disease (0.387); lysosomal storage disease (0.387)
- **Europe PMC papers**: 359
- **Why important**: COG8 is directly connected to NCAPD3 and is the only member with supplied lung immunohistochemistry detection without a corresponding non-detection entry. It is a component of the conserved oligomeric Golgi complex involved in Golgi organization, retrograde transport, vesicle recycling and glycoprotein modification. Its disease association with congenital disorder of glycosylation provides strong functional and clinical support, while its cardiomyocyte and epicardial-cell enrichments may be relevant to tissue composition. It broadens the module beyond nuclear biology and is useful for testing whether the signal reflects general intracellular homeostasis.
- **Conclusion**: Established evidence supports COG8 as a Golgi-trafficking and glycoprotein-processing factor with lung protein detection and disease relevance. Its presence may indicate a broader cellular-maintenance program or cell-composition effect, but connecting it mechanistically to the nuclear genes is currently speculative.

## Module 14

**Tissue pair**: circulatory_system and lung  
**Genes (5)**: COMMD10, HIKESHI, OSBPL1A, STK11IP, VPS53

### Function

The module does not have a GO or KEGG term passing global multiple-testing correction, so no GO or KEGG functional enrichment can be claimed as primary evidence. Its internal structure is consistent with a cellular infrastructure program rather than a narrowly defined pathway. OSBPL1A connects most of the module and is annotated with intracellular cholesterol transport, cholesterol homeostasis, lysosome-to-ER cholesterol transport, and vesicle-mediated transport. VPS53 supports a vesicle-trafficking interpretation through GARP-complex membership, retrograde transport, endocytic recycling, and lysosomal transport. COMMD10 is annotated for endocytic recycling, while STK11IP is involved in intracellular protein localization. HIKESHI adds a cellular-stress and nuclear-protein-transport component through heat-shock-induced HSP seventy nuclear import. Taken together, the best-supported interpretation is coordinated intracellular membrane trafficking, lipid handling, protein localization, and stress-responsive transport, with no evidence that this is a formally enriched canonical pathway.

**Cell composition.** All module genes have low tissue specificity in HPA, and none is annotated as secreted. This argues against a plasma-protein module. Most genes also have low immune-cell specificity; only OSBPL1A is immune-cell enriched in basophils and STK11IP is immune-cell enhanced in plasmacytoid dendritic cells. Cell-type enhancement is distributed across neural or epithelial populations and germ-cell populations rather than concentrated in a single shared tissue lineage. Four genes are detected by HPA immunohistochemistry in lung, whereas STK11IP is not detected there. The composition therefore looks more like a broadly expressed intracellular, housekeeping-adjacent program that may reflect shared cellular machinery in the sampled tissues than a blood-cell or secreted-protein signal. The cell-type annotations also warrant caution because some enhanced cell types are not obviously common to circulatory system and lung.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction among the module gene pairs reaches the supplied high-confidence threshold, and STRING functional enrichment is absent. No hu.MAP complex contains multiple module members. Thus, the co-abundance relationships are not corroborated here by high-confidence curated or experimentally supported physical interactions, nor by a shared known complex. The absence of these relationships does not invalidate co-abundance, but it favors a model of coordinated cellular state, compartmental activity, or indirect regulation rather than a stable physical complex. The individual annotations still provide biologically coherent themes involving vesicles, endocytic recycling, lipid transport, and protein trafficking.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is potentially a new tissue-pair co-abundance observation, but it cannot be called a newly discovered molecular pathway. The module has no globally significant GO or KEGG term, no STRING functional enrichment, no high-confidence STRING pair, and no multi-member hu.MAP complex. Those negative database results support novelty of the observed cross-tissue co-abundance pattern, but absence from STRING or hu.MAP alone does not prove biological novelty. Several component genes have established functions and disease associations, so the defensible claim is that the co-abundance combination and its relevance to circulatory system and lung may be under-characterized, not that the genes or their individual functions are new.

**Hypothesis.** Hypothesis: the shared module reflects a conserved intracellular maintenance state in which OSBPL1A-dependent sterol handling is coordinated with VPS53-mediated retrograde and lysosomal trafficking, COMMD10-linked endocytic recycling, STK11IP-associated protein localization, and HIKESHI-mediated stress-responsive nuclear import. In circulatory system and lung samples, this could arise from shared activation or abundance of cells requiring membrane turnover and protein quality control, rather than from direct protein-protein binding among all module members. This hypothesis should be tested with cell-resolved expression, perturbation of trafficking or sterol handling, and independent tissue cohorts.

### Important genes

#### OSBPL1A

- **Related proteins** (co-abundance neighbors): COMMD10 (0.89), HIKESHI (0.84), VPS53 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: oxysterol binding protein like 1A. This gene encodes a member of the oxysterol-binding protein (OSBP) family, a group of intracellular lipid receptors. Most members contain an N-terminal pleckstrin homology domain and a highly conserved C-terminal OSBP-like sterol-binding domain, although some members contain only the sterol-binding domain. Transcript variants derived from alternative promoter usage and/or alternative splicing exis…
- **Diseases (Open Targets)**: Paraproteinemia (0.244); otitis externa (0.219); secondary malignant neoplasm (0.206); Abnormality of the skeletal system (0.109); obesity disorder (0.077)
- **Europe PMC papers**: 404
- **Why important**: OSBPL1A is the central network connector, linking COMMD10, HIKESHI, and VPS53. Its established OSBP-family function in intracellular sterol sensing and transport provides the strongest mechanistic bridge between lipid homeostasis and the module's vesicle-related annotations. It is also detected in lung, has broad tissue distribution, multiple cell-type enhancements, an immune-cell enrichment annotation, disease associations including paraproteinemia and obesity disorder, and substantial literature support.
- **Conclusion**: Established evidence supports OSBPL1A as the module's principal organizational and lipid-trafficking candidate. It is a plausible driver or marker of the shared state, but the co-abundance data do not establish that it physically regulates the other module genes.

#### VPS53

- **Related proteins** (co-abundance neighbors): STK11IP (0.83), OSBPL1A (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS53 subunit of GARP complex. This gene encodes a protein with sequence similarity to the yeast Vps53p protein. Vps53p is involved in retrograde vesicle trafficking in late Golgi. [provided by RefSeq, Jul 2008]
- **Diseases (Open Targets)**: pontocerebellar hypoplasia type 2E (0.732); progressive cerebello-cerebral atrophy (0.656); prostate carcinoma (0.539); neurodegenerative disease (0.528); prostate cancer (0.480)
- **Europe PMC papers**: 504
- **Why important**: VPS53 is a network bridge between OSBPL1A and STK11IP and is an annotated subunit of the GARP complex. Its established roles in retrograde Golgi trafficking, lysosomal transport, endocytic recycling, and protein targeting connect the module to intracellular membrane logistics. It is detected in lung, shows enhancement across several neural cell types, and has disease associations with pontocerebellar hypoplasia type two E and progressive cerebello-cerebral atrophy, alongside substantial literature support.
- **Conclusion**: Established evidence makes VPS53 the strongest trafficking anchor in the module. Its position supports a shared vesicle-maintenance interpretation, while the module does not show direct database-supported physical interaction with the other members.

#### HIKESHI

- **Related proteins** (co-abundance neighbors): OSBPL1A (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein nuclear import factor hikeshi. This gene encodes an evolutionarily conserved nuclear transport receptor that mediates heat-shock-induced nuclear import of 70 kDa heat-shock proteins (Hsp70s) through interactions with FG-nucleoporins. The protein mediates transport of the ATP form but not the ADP form of Hsp70 proteins under conditions of heat shock stress. Structural analyses demonstrate that the protein forms an asymmetric hom…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 13 (0.720); POLR-related leukodystrophy (0.619); hypothyroidism (0.463); hereditary disease (0.358); ocular hypotension (0.211)
- **Europe PMC papers**: 136
- **Why important**: HIKESHI connects directly to OSBPL1A and contributes a distinct stress-response mechanism. Its established function is nuclear import of ATP-bound HSP seventy proteins during heat shock, through interactions with nuclear-pore components. It is detected in lung and has disease associations including hypomyelinating leukodystrophy and POLR-related leukodystrophy. Its literature base is smaller than that of the best-characterized trafficking genes, which makes its inclusion especially informative for a stress-adaptation interpretation.
- **Conclusion**: Established evidence supports HIKESHI as a stress-responsive protein-transport component. Its relationship to sterol and vesicle genes is a hypothesis from the co-abundance pattern, not an established shared molecular pathway.

#### STK11IP

- **Related proteins** (co-abundance neighbors): VPS53 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine/threonine kinase 11 interacting protein. Enables protein kinase binding activity. Involved in protein localization. Located in cytoplasm and intracellular membrane-bounded organelle. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: atrial fibrillation (0.333); neurodegenerative disease (0.255); Alzheimer disease (0.254); Parkinson disease (0.254); lysosomal storage disease (0.254)
- **Europe PMC papers**: 168
- **Why important**: STK11IP is connected to VPS53 and is annotated for protein kinase binding, intracellular protein localization, and localization to intracellular membrane-bounded organelles. Its vesicular localization and enhancement in late spermatids and Sertoli cells, together with immune-cell enhancement in plasmacytoid dendritic cells, indicate cell-context dependence. It also has associations with atrial fibrillation, neurodegenerative disease, and lysosomal storage disease.
- **Conclusion**: Established evidence supports STK11IP as a protein-localization and vesicle-associated contextual component. Its contribution to the shared circulatory-system and lung module may reflect cell-state composition or intracellular trafficking demand, but causality is not demonstrated.

#### COMMD10

- **Related proteins** (co-abundance neighbors): OSBPL1A (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: COMM domain containing 10. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.406); bone benign neoplasm (0.237); sensory perception of smell (0.212); sialolithiasis (0.181); tricuspid valve disorder (0.147)
- **Europe PMC papers**: 361
- **Why important**: COMMD10 is directly connected to the central OSBPL1A node and is annotated for endocytic recycling, providing a focused link to membrane trafficking. It is broadly expressed, has low cell-type specificity, is detected in lung, and has associations with neurodegenerative disease, bone benign neoplasm, sensory perception of smell, sialolithiasis, and tricuspid valve disorder. Its literature support is substantial despite the lack of STRING or hu.MAP support within this module.
- **Conclusion**: Established evidence supports COMMD10 as a plausible endocytic-recycling marker that reinforces the trafficking interpretation. Its peripheral network position and lack of database-supported module interactions make it less suitable as a claimed master regulator.

## Module 15

**Tissue pair**: circulatory_system and lung  
**Genes (18)**: CACYBP, DDX5, FKBP4, GMPS, MCM2, MCM4, MCM5, MCM6, MCM7, PCNA, GART, PFAS, ATIC, RRM1, CCT5, CCT3, CCT7, CCT8

### Function

The module is best interpreted as a coordinated proliferative, genome-maintenance program centered on DNA replication and replication-fork biology. The strongest primary evidence is the coherent enrichment of the MCM complex and CMG-related replication machinery (GO:CC MCM complex; q_global = 1.03e-07), (GO:CC CMG complex; q_global = 4.42e-06), together with DNA replication initiation and regulation (GO:BP regulation of DNA-templated DNA replication initiation; q_global = 4.42e-06), (GO:CC DNA replication preinitiation complex; q_global = 7.55e-06), (KEGG DNA replication - Homo sapiens (human); q_global = 1.57e-05), (GO:BP regulation of DNA-templated DNA replication; q_global = 3.92e-05), (GO:BP regulation of DNA replication; q_global = 0.000103), (GO:BP DNA-templated DNA replication; q_global = 0.000124), (GO:BP DNA replication initiation; q_global = 0.000241), (GO:BP DNA replication; q_global = 0.00159). The MCM2, MCM4, MCM5, MCM6 and MCM7 group supports licensing and helicase activity, while PCNA and RRM1 support replication-associated DNA synthesis and repair (KEGG DNA replication - Homo sapiens (human); q_global = 1.57e-05), (GO:BP DNA-templated DNA replication; q_global = 0.000124), (GO:BP DNA biosynthetic process; q_global = 0.000521), (GO:BP DNA replication; q_global = 0.00159), (GO:BP DNA repair; q_global = 0.0414). A second component is ATP-dependent protein folding through CCT3, CCT5, CCT7 and CCT8 (GO:CC chaperonin-containing T-complex; q_global = 7.63e-06), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.00134), (GO:CC protein folding chaperone complex; q_global = 0.00348), (GO:MF protein folding chaperone; q_global = 0.00843), (GO:BP protein folding; q_global = 0.0313), with related Cajal-body and telomerase-localization annotations (GO:BP regulation of telomerase RNA localization to Cajal body; q_global = 7.63e-06), (GO:BP regulation of protein localization to Cajal body; q_global = 2.82e-05), (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 0.000346), (GO:BP telomere maintenance via telomerase; q_global = 0.0051). A third component is purine nucleotide production through ATIC, GART, GMPS and PFAS (GO:BP GMP biosynthetic process; q_global = 0.00101), (GO:BP purine ribonucleoside monophosphate biosynthetic process; q_global = 0.00223), (GO:BP purine nucleoside monophosphate biosynthetic process; q_global = 0.00348), (KEGG Purine metabolism - Homo sapiens (human); q_global = 0.00477), (GO:BP 'de novo' IMP biosynthetic process; q_global = 0.00618), (GO:BP ribonucleoside monophosphate biosynthetic process; q_global = 0.0112). Thus, the most parsimonious established interpretation is a cell-cycle and genome-replication module accompanied by chaperoning and nucleotide-supply functions. The ATP- and nucleotide-binding enrichments (GO:MF ATP binding; q_global = 1.2e-06), (GO:MF adenyl ribonucleotide binding; q_global = 1.28e-06), (GO:MF adenyl nucleotide binding; q_global = 3.96e-06), (GO:MF purine ribonucleoside triphosphate binding; q_global = 1.17e-05), (GO:MF ribonucleotide binding; q_global = 1.4e-05), (GO:MF purine nucleotide binding; q_global = 3.24e-05) are broad molecular-function signals and should not be treated as the principal biological interpretation.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. Most genes are intracellular, with nuclear, nucleoplasmic or cytosolic localization, and protein detection in lung is reported for nearly all of the module where data are available. The module has a strong proliferative or progenitor-associated composition. HPA links many genes to erythrocyte progenitors, megakaryocyte progenitors, monocyte progenitors, trophoblast populations and germ-cell populations; tissue-enhanced signals most often involve bone marrow and lymphoid tissue. However, the blood-cell specificity summary is predominantly low, with only PFAS showing immune-cell enhancement toward neutrophils. Therefore, the shared circulatory-system and lung signal may reflect proliferating or progenitor-like cells present in the sampled tissues, or a broadly shared cell-cycle state, rather than a lung-specific or vascular-secreted program. The HPA evidence does not establish that the module is caused by blood contamination.

**GO/KEGG enrichment**: 117 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC MCM complex | 1.03e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP double-strand break repair via break-induced replication | 1.08e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF ATP binding | 1.2e-06 | CCT3, CCT5, CCT7, CCT8, DDX5, FKBP4, GART, GMPS, MCM2, MCM4, MCM5, MCM6, MCM7, PFAS, RRM1 |
| GO:MF adenyl ribonucleotide binding | 1.28e-06 | CCT3, CCT5, CCT7, CCT8, DDX5, FKBP4, GART, GMPS, MCM2, MCM4, MCM5, MCM6, MCM7, PFAS, RRM1 |
| GO:MF adenyl nucleotide binding | 3.96e-06 | CCT3, CCT5, CCT7, CCT8, DDX5, FKBP4, GART, GMPS, MCM2, MCM4, MCM5, MCM6, MCM7, PFAS, RRM1 |
| GO:BP regulation of DNA-templated DNA replication initiation | 4.42e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC CMG complex | 4.42e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA metabolic process | 7.14e-06 | CCT3, CCT5, CCT7, CCT8, MCM2, MCM4, MCM5, MCM6, MCM7, PCNA |
| GO:CC DNA replication preinitiation complex | 7.55e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC chaperonin-containing T-complex | 7.63e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 7.63e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 7.63e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:MF purine ribonucleoside triphosphate binding | 1.17e-05 | CCT3, CCT5, CCT7, CCT8, DDX5, FKBP4, GART, GMPS, MCM2, MCM4, MCM5, MCM6, MCM7, PFAS, RRM1 |
| GO:MF purine ribonucleotide binding | 1.24e-05 | CCT3, CCT5, CCT7, CCT8, DDX5, FKBP4, GART, GMPS, MCM2, MCM4, MCM5, MCM6, MCM7, PFAS, RRM1 |
| GO:MF ribonucleotide binding | 1.4e-05 | CCT3, CCT5, CCT7, CCT8, DDX5, FKBP4, GART, GMPS, MCM2, MCM4, MCM5, MCM6, MCM7, PFAS, RRM1 |

### STRING and hu.MAP

STRING independently recovers the MCM group as a dense, high-confidence interaction structure, including MCM2, MCM4, MCM5, MCM6 and MCM7, with links to PCNA and RRM1. STRING also recovers the CCT3, CCT5, CCT7 and CCT8 chaperonin group and the purine-biosynthesis links involving ATIC, GART, GMPS and PFAS. These relationships are consistent with known physical or functional organization rather than isolated co-abundance. The supplementary STRING enrichments (STRING Function ATP binding; within-query FDR = 1.02e-07) through (STRING WikiPathways G1 to S cell cycle control; within-query FDR = 2.1e-06) support ATP-related activity, the MCM complex, DNA replication and cell-cycle control, but their within-query FDR values are not global module significance. hu.MAP provides convergent complex-level support: (hu.MAP huMAP3_05529.1) through (hu.MAP huMAP3_11119.1) connect the MCM proteins to MCM3, MCMBP, CDC45, GINS proteins and fork-protection factors; (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_14584.1) connect the CCT proteins to the broader CCT or associated chaperone machinery; and (hu.MAP huMAP3_03291.1) through (hu.MAP huMAP3_12823.1) connect purine-pathway members to related metabolic assemblies. PCNA, RRM1, FKBP4, DDX5 and CACYBP have no hu.MAP complex listed in the fact sheet, so their module membership should not be overstated as established complex membership.

**STRING interactions (score >= 0.7)**: 34 of 153 gene pairs: ATIC–CCT7 (0.881); ATIC–GART (0.999); ATIC–GMPS (0.921); ATIC–PFAS (0.819); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999); GART–GMPS (0.937); GART–PFAS (0.999); GMPS–RRM1 (0.748); MCM2–MCM4 (0.999); MCM2–MCM5 (0.999); MCM2–MCM6 (0.999); MCM2–MCM7 (0.999); MCM2–PCNA (0.939); MCM2–RRM1 (0.914); MCM4–MCM5 (0.999); MCM4–MCM6 (0.999); MCM4–MCM7 (0.999); MCM4–PCNA (0.965); MCM4–RRM1 (0.952); MCM5–MCM6 (0.999); MCM5–MCM7 (0.999); MCM5–PCNA (0.918); MCM5–RRM1 (0.957); MCM6–MCM7 (0.999); MCM6–PCNA (0.912); MCM6–RRM1 (0.953); MCM7–PCNA (0.985); MCM7–RRM1 (0.921); PCNA–RRM1 (0.933)
**STRING functional enrichment (supplementary, within-query FDR)**: Function ATP binding (FDR = 1.02e-07, 15 genes); Function ATP hydrolysis activity (FDR = 2.11e-07, 10 genes); Keyword ATP-binding (FDR = 3.81e-07, 14 genes); Component MCM complex (FDR = 5.72e-07, 5 genes); COMPARTMENTS MCM complex (FDR = 6.34e-07, 5 genes); Function Pyrophosphatase activity (FDR = 8.88e-07, 11 genes); InterPro MCM domain (FDR = 1.08e-06, 5 genes); InterPro Mini-chromosome maintenance, conserved site (FDR = 1.08e-06, 5 genes); InterPro MCM N-terminal domain (FDR = 1.08e-06, 5 genes); InterPro Mini-chromosome maintenance protein (FDR = 1.08e-06, 5 genes); InterPro MCM OB domain (FDR = 1.08e-06, 5 genes); InterPro MCM, AAA-lid domain (FDR = 1.08e-06, 5 genes); KEGG DNA replication (FDR = 1.59e-06, 6 genes); Keyword DNA replication (FDR = 2.09e-06, 7 genes); WikiPathways G1 to S cell cycle control (FDR = 2.1e-06, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05529.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/6); huMAP3_14758.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/14); huMAP3_08554.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_11832.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_12180.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/17); huMAP3_06061.1 (MCM4, MCM7, MCM2, MCM6; 4/5); huMAP3_07113.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_11119.1 (MCM4, MCM5, MCM7, MCM6; 4/14); huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_09860.1 (MCM4, MCM2, MCM6; 3/4); huMAP3_00154.1 (MCM4, MCM2, MCM6; 3/5); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_09466.1 (MCM4, MCM2, MCM6; 3/23); huMAP3_10862.1 (MCM4, MCM2, MCM6; 3/33); huMAP3_14306.1 (MCM4, MCM2, MCM6; 3/55); huMAP3_02602.1 (MCM4, MCM6; 2/2); huMAP3_03291.1 (PFAS, GART; 2/3); huMAP3_00676.1 (PFAS, GART; 2/4); huMAP3_12823.1 (ATIC, GMPS; 2/7); huMAP3_09238.1 (MCM5, MCM7; 2/11); huMAP3_08848.1 (MCM4, MCM6; 2/15); huMAP3_14442.1 (ATIC, GMPS; 2/57)

### Novelty

The module is unlikely to represent a wholly new molecular mechanism, because its principal structures are canonical and independently supported: the MCM replication machinery, PCNA-associated replication biology, the CCT chaperonin, and purine biosynthesis are already represented in STRING, hu.MAP, GO and KEGG. What may be novel is the tissue-pair-specific co-abundance configuration in which these established cellular programs appear together across circulatory system and lung. The module therefore supports a potentially useful cross-tissue signature, but the fact sheet alone cannot establish disease specificity, causal regulation, or discovery of a new protein complex. Absence of hu.MAP or STRING entries for individual genes such as CACYBP, DDX5, FKBP4, PCNA or RRM1 does not by itself demonstrate novelty.

**Hypothesis.** Hypothesis: the shared module reflects a proliferative progenitor or regenerating-cell state in which replication licensing and fork progression are coordinated with nucleotide supply and proteostasis. Increased demand for DNA synthesis could couple the MCM helicase machinery and PCNA to RRM1-dependent deoxyribonucleotide production, while ATIC, GART, GMPS and PFAS support purine availability. CCT chaperonin activity could maintain folding of replication and cell-cycle proteins, with the Cajal-body and telomerase annotations suggesting a possible link to nuclear RNA and telomere-related processes. This is a mechanistic model rather than proof of active replication in every contributing cell; bulk co-abundance can also arise from changing proportions of progenitor-like cell types.

### Important genes

#### MCM5

- **Related proteins** (co-abundance neighbors): MCM7 (0.87), MCM6 (0.84), PCNA (0.82), MCM4 (0.81); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM6 (0.999), MCM7 (0.999), PCNA (0.918), RRM1 (0.957)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 5. The protein encoded by this gene is structurally very similar to the CDC46 protein from S. cerevisiae, a protein involved in the initiation of DNA replication. The encoded protein is a member of the MCM family of chromatin-binding proteins and can interact with at least two other members of this family. The encoded protein is upregulated in the transition from the G0 to G1/S phase of the cell cycl…
- **Diseases (Open Targets)**: Meier-Gorlin syndrome (0.563); neurodegenerative disease (0.397); lysosomal storage disease (0.362); kidney transplant (0.198); diabetic ketoacidosis (0.129)
- **Europe PMC papers**: 4143
- **Why important**: MCM5 is a central network member with connections to MCM4, MCM6, MCM7 and PCNA. It belongs to the MCM complex and is represented across the primary replication, helicase, replication-repair and cell-cycle terms (GO:CC MCM complex; q_global = 1.03e-07), (GO:BP double-strand break repair via break-induced replication; q_global = 1.08e-06), (GO:BP regulation of DNA-templated DNA replication initiation; q_global = 4.42e-06), (KEGG DNA replication - Homo sapiens (human); q_global = 1.57e-05), (GO:BP DNA-templated DNA replication; q_global = 0.000124), (GO:BP DNA replication; q_global = 0.00159). The supplied annotation describes a chromatin-binding replication-initiation protein induced during the G0-to-G1/S transition. It also has strong hu.MAP support (hu.MAP huMAP3_05529.1) through (hu.MAP huMAP3_11119.1), disease associations including Meier-Gorlin syndrome, and substantial literature support.
- **Conclusion**: Established: MCM5 is a strong marker and likely structural contributor of the replication-centered part of the module. Hypothesis: its co-abundance may report the abundance or activation state of replication-competent progenitor-like cells in both tissues, but the data do not prove that MCM5 initiates the tissue-level program.

#### MCM6

- **Related proteins** (co-abundance neighbors): MCM4 (0.90), MCM5 (0.84), RRM1 (0.82); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM7 (0.999), PCNA (0.912), RRM1 (0.953)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 6. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: lactose intolerance (0.246); neurodegenerative disease (0.225); obesity disorder (0.166); nervous system disorder (0.141); systemic lupus erythematosus (0.140)
- **Europe PMC papers**: 3766
- **Why important**: MCM6 is embedded in the MCM interaction core and connects to MCM4, MCM5 and RRM1 in the module. It is present in the primary MCM, replication-initiation, helicase, DNA-repair and cell-cycle evidence (GO:CC MCM complex; q_global = 1.03e-07), (GO:BP double-strand break repair via break-induced replication; q_global = 1.08e-06), (GO:BP regulation of DNA-templated DNA replication initiation; q_global = 4.42e-06), (KEGG DNA replication - Homo sapiens (human); q_global = 1.57e-05), (GO:BP DNA replication initiation; q_global = 0.000241), (GO:BP DNA replication; q_global = 0.00159), (GO:BP double-strand break repair via homologous recombination; q_global = 0.0129), (GO:BP DNA repair; q_global = 0.0414). Its supplied annotation identifies it as an essential MCM-family replication factor, and hu.MAP repeatedly places it in MCM and replisome-related complexes (hu.MAP huMAP3_05529.1) through (hu.MAP huMAP3_11119.1), (hu.MAP huMAP3_09860.1), (hu.MAP huMAP3_00154.1), (hu.MAP huMAP3_09466.1) through (hu.MAP huMAP3_02602.1).
- **Conclusion**: Established: MCM6 provides particularly strong evidence that the module contains authentic replication machinery rather than a nonspecific ATP-binding cluster. Hypothesis: its association with RRM1 may reflect coordinated demand for replication substrates, although co-abundance cannot establish direct regulation.

#### MCM7

- **Related proteins** (co-abundance neighbors): MCM5 (0.87), GMPS (0.85), MCM2 (0.82); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM6 (0.999), PCNA (0.985), RRM1 (0.921)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 is a network bridge between the MCM group and GMPS, and it connects strongly to PCNA. It is included in the primary MCM, CMG, DNA-replication, helicase, homologous-recombination and DNA-damage-response evidence (GO:CC MCM complex; q_global = 1.03e-07), (GO:CC CMG complex; q_global = 4.42e-06), (KEGG DNA replication - Homo sapiens (human); q_global = 1.57e-05), (GO:MF four-way junction helicase activity; q_global = 0.000241), (KEGG Homologous recombination - Homo sapiens (human); q_global = 0.00576), (GO:BP double-strand break repair via homologous recombination; q_global = 0.0129), (GO:BP DNA damage response; q_global = 0.0486). It has repeated hu.MAP support for MCM and replisome assemblies (hu.MAP huMAP3_05529.1) through (hu.MAP huMAP3_11119.1), a large literature base, and disease associations including Meier-Gorlin syndrome and spastic paraplegia.
- **Conclusion**: Established: MCM7 is a high-value representative of the replication-fork interpretation and links that interpretation to the metabolic side of the module. Hypothesis: the MCM7-GMPS co-abundance relationship may indicate coordination between fork progression and guanine-nucleotide supply, but it is not evidence of a direct physical interaction beyond the supplied STRING relationship.

#### PCNA

- **Related proteins** (co-abundance neighbors): FKBP4 (0.83), MCM5 (0.82), DDX5 (0.81); STRING partners: MCM2 (0.939), MCM4 (0.965), MCM5 (0.918), MCM6 (0.912), MCM7 (0.985), RRM1 (0.933)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proliferating cell nuclear antigen. The protein encoded by this gene is found in the nucleus and is a cofactor of DNA polymerase delta. The encoded protein acts as a homotrimer and helps increase the processivity of leading strand synthesis during DNA replication. In response to DNA damage, this protein is ubiquitinated and is involved in the RAD6-dependent DNA repair pathway. Two transcript variants encoding the same protein have b…
- **Diseases (Open Targets)**: ataxia-telangiectasia-like disorder (0.497); neurodegenerative disease (0.188); neoplasm (0.118); diabetes mellitus (0.116); hepatocellular carcinoma (0.113)
- **Europe PMC papers**: 61820
- **Why important**: PCNA connects the module's MCM replication machinery with FKBP4 and DDX5 and has STRING links to the MCM group and RRM1. It is present in primary DNA replication, replication regulation, DNA biosynthesis, cell-cycle, telomere and DNA-repair terms (GO:BP regulation of DNA metabolic process; q_global = 7.14e-06), (KEGG DNA replication - Homo sapiens (human); q_global = 1.57e-05), (GO:BP regulation of DNA replication; q_global = 0.000103), (GO:BP DNA-templated DNA replication; q_global = 0.000124), (GO:BP DNA biosynthetic process; q_global = 0.000521), (KEGG Cell cycle - Homo sapiens (human); q_global = 0.000574), (GO:BP DNA replication; q_global = 0.00159), (GO:BP telomere maintenance; q_global = 0.0148), (GO:BP DNA repair; q_global = 0.0414), (GO:BP DNA damage response; q_global = 0.0486). The supplied annotation identifies it as the processivity cofactor for DNA polymerase delta and as a DNA-damage-response factor. It has the largest literature volume among the listed genes and disease associations including ataxia-telangiectasia-like disorder and neoplasm.
- **Conclusion**: Established: PCNA is the strongest functional bridge from MCM licensing to DNA synthesis and repair. Hypothesis: PCNA may help explain why the shared module is detectable in both tissues as a general proliferative or repair-state signal, but its network position does not prove that it is the module's regulator.

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT8 (0.89), CCT7 (0.83), CCT3 (0.82); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is a core member of the module's tightly connected CCT3-CCT5-CCT7-CCT8 group and is represented in the primary chaperonin, protein-folding, Cajal-body and telomerase-related terms (GO:CC chaperonin-containing T-complex; q_global = 7.63e-06), (GO:BP regulation of telomerase RNA localization to Cajal body; q_global = 7.63e-06), (GO:BP regulation of protein localization to Cajal body; q_global = 2.82e-05), (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 0.000346), (GO:CC protein folding chaperone complex; q_global = 0.00348), (GO:MF protein folding chaperone; q_global = 0.00843), (GO:BP protein folding; q_global = 0.0313). The supplied annotation describes ATP-dependent folding of proteins including actin and tubulin. hu.MAP supports repeated CCT-associated assemblies (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_14584.1), and CCT5 has a disease association with hereditary sensory and autonomic neuropathy with spastic paraplegia.
- **Conclusion**: Established: CCT5 supports a genuine proteostasis submodule that is distinct from, but co-abundant with, the replication machinery. Hypothesis: CCT5 may buffer the increased folding burden of proliferating cells or help maintain replication-related proteins; the module does not demonstrate a direct CCT5-to-replication mechanism.

#### ATIC

- **Related proteins** (co-abundance neighbors): CCT3 (0.87), CCT8 (0.81), CACYBP (0.81); STRING partners: CCT7 (0.881), GART (0.999), GMPS (0.921), PFAS (0.819)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_12823.1, huMAP3_14442.1
- **Function (MyGene.info)**: 5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase. This gene encodes a bifunctional protein that catalyzes the last two steps of the de novo purine biosynthetic pathway. The N-terminal domain has phosphoribosylaminoimidazolecarboxamide formyltransferase activity, and the C-terminal domain has IMP cyclohydrolase activity. A mutation in this gene results in AICA-ribosiduria. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: AICA-ribosiduria (0.708); cancer (0.571); Intellectual disability (0.463); lung adenocarcinoma (0.390); anaplastic large cell lymphoma (0.374)
- **Europe PMC papers**: 5200
- **Why important**: ATIC is a network connector between the CCT-related side and the purine-biosynthesis group, with STRING links to GART, GMPS and PFAS and hu.MAP support in (hu.MAP huMAP3_12823.1) and (hu.MAP huMAP3_14442.1). It is represented in the primary purine-biosynthesis and nucleotide-metabolism evidence (GO:BP GMP biosynthetic process; q_global = 0.00101), (GO:BP purine ribonucleoside monophosphate biosynthetic process; q_global = 0.00223), (GO:BP purine nucleoside monophosphate biosynthetic process; q_global = 0.00348), (KEGG Purine metabolism - Homo sapiens (human); q_global = 0.00477), (GO:BP 'de novo' IMP biosynthetic process; q_global = 0.00618), (GO:BP ribonucleoside monophosphate biosynthetic process; q_global = 0.0112), and its supplied annotation identifies the bifunctional enzyme catalyzing the final steps of de novo IMP production. It has extensive literature support and disease associations including AICA-ribosiduria and lung adenocarcinoma.
- **Conclusion**: Established: ATIC marks the nucleotide-supply component that can support DNA synthesis and links this component to the rest of the module. Hypothesis: ATIC may be a metabolic coupling point between proliferative demand and purine production in the shared tissue state, but the co-abundance data do not establish metabolic flux or causality.

## Module 16

**Tissue pair**: circulatory_system and lung  
**Genes (5)**: DSG2, GMPR2, HECTD3, LRRFIP2, UEVLD

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING functional enrichment. The module therefore does not support a statistically established pathway-level functional assignment. Its structure is compatible with a mixed epithelial, intracellular metabolic, ubiquitin-regulatory, and innate immune-related signal. DSG2 provides an epithelial junction and desmosome connection; HECTD3 provides ubiquitin-ligase biology; GMPR2 provides purine metabolism; LRRFIP2 provides links to TLR4–NF-kappa-B signaling and inflammasome regulation; and UEVLD is connected to protein transport, vesicle-mediated transport, transcriptional regulation, and predicted oxidoreductase activity. These annotations support biological plausibility but not a unified enriched function.

**Cell composition.** All module genes have lung protein detection, whereas matching circulatory-system tissue protein data are unavailable. Most genes have low tissue specificity and low immune-cell specificity, and none is annotated as secreted. The module is therefore not consistent with a plasma-protein module or a strongly blood-cell-enriched module. HECTD3, GMPR2, and DSG2 show cell-type-enhanced patterns, with repeated epithelial associations for HECTD3 and DSG2 and neural or glial associations for GMPR2. DSG2 is tissue-enhanced in intestine and parathyroid gland and is immune-cell-enriched in basophils. The shared signal may therefore reflect lung epithelial or other shared cell-type composition rather than a circulating molecular program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair reaches the supplied STRING interaction threshold, no STRING functional enrichment is present, and no hu.MAP complex contains multiple module members. The co-abundance edges are consequently not corroborated by the supplied curated interaction or complex resources. This suggests that the module is an expression-covariation group rather than a known physical complex or a STRING-supported interaction neighborhood. The absence of database support does not invalidate the co-abundance pattern, but it limits mechanistic certainty.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously under-characterized co-abundance relationship because none of its internal relationships is represented in the supplied STRING or hu.MAP evidence. However, that database absence alone cannot establish a new biological mechanism. Several individual genes and functions are already established, especially DSG2 desmosome biology, GMPR2 purine metabolism, HECTD3 ubiquitin ligase activity, and LRRFIP2 innate immune regulation. The defensible conclusion is that the shared tissue-pair module is potentially novel as a coordinated expression pattern, while its component biology is not uniformly novel.

**Hypothesis.** Hypothesis: the module reflects a lung epithelial cell-state program that combines epithelial junction maintenance through DSG2 with intracellular protein turnover through HECTD3, purine metabolic support through GMPR2, and conditional innate immune or inflammasome regulation through LRRFIP2, with UEVLD acting as a covarying intracellular transport or metabolic-associated component. The epithelial HPA patterns and lung detection support this cell-state interpretation, but the lack of globally significant GO or KEGG enrichment and the lack of STRING or hu.MAP support mean that this remains a mechanistic hypothesis rather than an established pathway.

### Important genes

#### DSG2

- **Related proteins** (co-abundance neighbors): HECTD3 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cell Junctions; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: desmoglein 2. This gene encodes a member of the desmoglein family and cadherin cell adhesion molecule superfamily of proteins. Desmogleins are calcium-binding transmembrane glycoprotein components of desmosomes, cell-cell junctions between epithelial, myocardial, and other cell types. The encoded preproprotein is proteolytically processed to generate the mature glycoprotein. This gene is present in a gene clust…
- **Diseases (Open Targets)**: arrhythmogenic right ventricular dysplasia 10 (0.812); arrhythmogenic right ventricular cardiomyopathy (0.781); dilated cardiomyopathy 1BB (0.714); familial isolated dilated cardiomyopathy (0.615); Abnormality of the cardiovascular system (0.552)
- **Europe PMC papers**: 3811
- **Why important**: DSG2 is the strongest biological anchor for the module because it is a cell-junction protein located at desmosomes and has annotations for desmosome assembly, cell adhesion, and epithelial organization. It has the largest literature volume among the module genes and disease associations with arrhythmogenic and dilated cardiomyopathy. Its tissue and cell-type patterns are strongly epithelial, and it connects the module to HECTD3 in the co-abundance graph.
- **Conclusion**: Established evidence supports DSG2 as an epithelial adhesion and desmosome gene with cardiovascular disease relevance. Its presence supports an epithelial structural component in the module. It is not established that DSG2 physically or functionally regulates the other module genes, because the supplied STRING and hu.MAP evidence is negative.

#### LRRFIP2

- **Related proteins** (co-abundance neighbors): UEVLD (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LRR binding FLII interacting protein 2. The protein encoded by this gene, along with MYD88, binds to the cytosolic tail of toll-like receptor 4 (TLR4), which results in activation of nuclear factor kappa B signaling. The ubiquitin-like protein FAT10 prevents the interaction of the encoded protein and TLR4, thereby inactivating the nuclear factor kappa B signaling pathway. In addition, this protein can downregulate the NLRP3 inflammasome…
- **Diseases (Open Targets)**: Lynch syndrome (0.720); hereditary neoplastic syndrome (0.572); hereditary nonpolyposis colorectal carcinoma (0.554); Muir-Torre syndrome (0.517); hereditary nonpolyposis colon cancer (0.507)
- **Europe PMC papers**: 425
- **Why important**: LRRFIP2 is important because its documented biology connects TLR4-associated signaling with NF-kappa-B activation and provides negative regulation of the NLRP3 inflammasome. It is linked to the module hub UEVLD and has substantial literature volume and strong hereditary colorectal cancer-related disease associations. Its plasma-membrane and actin-filament localization is compatible with a signaling or cell-interface role.
- **Conclusion**: Established evidence supports LRRFIP2 as an innate immune signaling and inflammasome-regulatory protein. Its inclusion makes immune-response coupling a plausible interpretation, but the low immune-cell specificity of the module and absence of STRING support argue against assigning the whole module to an immune pathway.

#### HECTD3

- **Related proteins** (co-abundance neighbors): UEVLD (0.84), DSG2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HECT domain E3 ubiquitin protein ligase 3. The protein encoded by this gene transfers ubiquitin from an E2 ubiquitin-conjugating enzyme to targeted substrates, leading to the degradation of those substrates. The encoded protein has been shown to transfer ubiquitin to TRIOBP to facilitate cell cycle progression, and to STX8. [provided by RefSeq, Dec 2012].
- **Diseases (Open Targets)**: neoplasm (0.088); breast carcinoma (0.081); experimental autoimmune encephalomyelitis (0.075); gastric cancer (0.074); metabolic syndrome (0.074)
- **Europe PMC papers**: 295
- **Why important**: HECTD3 is important because it encodes an E3 ubiquitin ligase and occupies an intermediate position connecting UEVLD with DSG2. Its established functions include protein ubiquitination and proteasome-mediated protein catabolism, with reported substrates including TRIOBP and STX8. It has more literature than the other intracellular regulatory genes and disease associations spanning neoplastic and metabolic conditions.
- **Conclusion**: Established evidence supports HECTD3 as a protein-turnover regulator. Its graph position and connection to DSG2 make it a plausible bridge between epithelial structure and intracellular quality-control biology. A direct role in coordinating the module has not been demonstrated by the supplied evidence.

#### GMPR2

- **Related proteins** (co-abundance neighbors): UEVLD (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: guanosine monophosphate reductase 2. This gene encodes an enzyme that catalyzes the irreversible and NADPH-dependent reductive deamination of guanosine monophosphate (GMP) to inosine monophosphate (IMP). The protein also functions in the re-utilization of free intracellular bases and purine nucleosides. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2017].
- **Diseases (Open Targets)**: refractive error (0.440); Abnormality of refraction (0.342); uterine corpus leiomyoma (0.055); prostate carcinoma (0.024); leukemia (0.023)
- **Europe PMC papers**: 193
- **Why important**: GMPR2 is important because it supplies a defined metabolic function: NADPH-dependent conversion of GMP to IMP and salvage of purine bases and nucleosides. It is connected to UEVLD and has disease associations involving refractive traits, uterine leiomyoma, prostate carcinoma, and leukemia. Its cell-type-enhanced pattern includes microglia, oligodendrocytes, and other brain neurons, indicating that its abundance may reflect cell composition rather than a lung-specific pathway.
- **Conclusion**: Established evidence supports GMPR2 as a purine-metabolism enzyme. It provides a metabolic dimension to the module, but there is no evidence that purine metabolism is globally enriched in this module or that GMPR2 is mechanistically linked to DSG2, HECTD3, or LRRFIP2.

#### UEVLD

- **Related proteins** (co-abundance neighbors): GMPR2 (0.86), LRRFIP2 (0.85), HECTD3 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UEV and lactate/malate dehyrogenase domains. Predicted to enable oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor. Predicted to be involved in several processes, including carbohydrate metabolic process; cellular protein modification process; and protein transport. Located in extracellular exosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hyperpituitarism (0.213); Dermatochalasis (0.172); benign chondrogenic neoplasm (0.076); epilepsy (0.038); smoking initiation (0.035)
- **Europe PMC papers**: 98
- **Why important**: UEVLD is important because it is the graph hub, connecting GMPR2, LRRFIP2, and HECTD3, and it has the greatest weighted network strength in the supplied subgraph. Its reported annotations include predicted oxidoreductase activity, carbohydrate metabolism, protein modification, protein transport, vesicle-mediated transport, and transcriptional regulation. It is broadly expressed by HPA and has lung protein detection, while its disease associations are comparatively weak and nonspecific.
- **Conclusion**: Established evidence supports UEVLD as the central covarying node and as a gene with broad predicted cellular functions. Its hub position makes it useful for describing module organization, but it does not prove that UEVLD drives the module or that its predicted functions explain the cross-tissue association.

## Module 17

**Tissue pair**: circulatory_system and lung  
**Genes (5)**: EIF2A, NOL10, SMC5, SPIN1, GTF3C5

### Function

No GO or KEGG term passed global correction. The module therefore does not support a statistically established pathway assignment from enrichment. Its structure is a hub-and-spoke co-abundance pattern centered on SPIN1, with links to SMC5, GTF3C5, EIF2A and NOL10. The gene annotations collectively point to nuclear and cytosolic gene-expression processes: chromatin and transcriptional regulation, genome maintenance, RNA polymerase III transcription, translation initiation and ribosome biogenesis. These are compatible with coordinated cellular maintenance or proliferation-related activity, but the module should not be assigned a single pathway as an established finding.

**Cell composition.** All module genes have low tissue specificity, and all are detected by immunohistochemistry in lung. None is annotated as secreted, and all have low immune-cell specificity. The module is therefore not plasma-protein dominated or blood-cell enriched. Its broadly expressed, intracellular, mostly nuclear or cytosolic composition is more consistent with a general cellular program than with a lung-specific secretory or immune-cell signature. Shared representation of common cell types or general cellular state in circulatory-system and lung samples remains a plausible explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was found among the module members, and no STRING functional-enrichment result was available. No hu.MAP complex contained multiple module members. Thus, the co-abundance relationships are not corroborated by the queried physical-interaction or complex resources. The absence of these relationships does not disprove coordinated regulation, but it argues against interpreting the module as a known multiprotein complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears to be a potentially novel co-abundance association rather than a rediscovery of a documented complex. The supporting pattern is the cross-tissue co-abundance network itself, while there is no high-confidence STRING support, no multi-member hu.MAP complex, and no globally significant GO or KEGG enrichment. These absences do not prove biological novelty: the module may reflect shared expression, cellular composition, technical or sampling effects, or interactions below database coverage. Novelty should therefore be stated as provisional until independently replicated and tested experimentally.

**Hypothesis.** Hypothesis: a broadly expressed intracellular state shared by circulatory-system and lung samples coordinates SPIN1 with transcriptional, genome-maintenance, translation-initiation and ribosome-biogenesis machinery. SPIN1 may act as the network-level marker of this state, while the other genes represent partially distinct cellular processes that covary because of common regulation or cell-state composition. This is a mechanistic hypothesis, not an established pathway assignment, and it requires replication, cell-resolved analysis and perturbation testing.

### Important genes

#### SPIN1

- **Related proteins** (co-abundance neighbors): SMC5 (0.83), GTF3C5 (0.82), EIF2A (0.81), NOL10 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: spindlin 1. Enables methylated histone binding activity. Involved in positive regulation of Wnt signaling pathway; positive regulation of transcription, DNA-templated; and rRNA transcription. Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.246); ovarian dysfunction (0.177); poisoning (0.124); non-small cell lung carcinoma (0.107); neoplasm (0.105)
- **Europe PMC papers**: 507
- **Why important**: SPIN1 is the central network node and is connected to every other module member. It binds methylated histone, is involved in transcriptional regulation, chromatin localization, rRNA transcription and positive regulation of Wnt signaling. It has disease links including neurodegenerative disease, ovarian dysfunction and non-small-cell lung carcinoma, and it has substantial literature support relative to the other module genes.
- **Conclusion**: Established evidence supports SPIN1 as the network hub and as a multifunctional chromatin and transcription-associated protein. Its centrality makes it the leading candidate marker of the module, but the data do not establish that SPIN1 causally drives the co-abundance pattern or that Wnt signaling is active in this module.

#### SMC5

- **Related proteins** (co-abundance neighbors): SPIN1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: structural maintenance of chromosomes 5. Predicted to enable ATP binding activity. Involved in several processes, including DNA recombination; cellular senescence; and positive regulation of maintenance of mitotic sister chromatid cohesion. Located in cell junction; chromosome; and nuclear body. Part of Smc5-Smc6 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Atelis syndrome 2 (0.695); Abnormality of the skeletal system (0.298); hereditary disease (0.194); neurodegenerative disease (0.188); developmental disability (0.185)
- **Europe PMC papers**: 1876
- **Why important**: SMC5 is linked directly to SPIN1 hu.MAP and encodes a component of the SMC five–SMC six complex. Its annotations include DNA recombination, homologous and nonhomologous double-strand-break repair, telomere maintenance, DNA-damage response and protein sumoylation. It has the strongest literature support among the module members and a disease association with Atelis syndrome two.
- **Conclusion**: Established evidence supports SMC5 as a genome-maintenance factor with a well-defined complex context. Its membership suggests that DNA repair or chromosome maintenance could accompany the shared cellular state, but the module does not demonstrate a functional SMC5 interaction with SPIN1.

#### EIF2A

- **Related proteins** (co-abundance neighbors): SPIN1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 2A. This gene encodes a eukaryotic translation initiation factor that catalyzes the formation of puromycin-sensitive 80 S preinitiation complexes and the poly(U)-directed synthesis of polyphenylalanine at low concentrations of Mg2+. This gene should not be confused with eIF2-alpha (EIF2S1, Gene ID: 1965), the alpha subunit of the eIF2 translation initiation complex. Although both of these proteins fun…
- **Diseases (Open Targets)**: aging (0.131); liver disorder (0.131); drug allergy (0.119); dystonia 33 (0.118); Marinesco-Sjogren syndrome (0.118)
- **Europe PMC papers**: 4315
- **Why important**: EIF2A is directly connected to SPIN1 hu.MAP and participates in translation initiation, regulation of translation, ribosome assembly and response to amino-acid starvation. It has the largest literature volume in the module and disease or trait associations including aging, liver disorder, drug allergy, dystonia and Marinesco–Sjogren syndrome.
- **Conclusion**: Established evidence supports EIF2A as a translation-related factor whose abundance may report cellular protein-synthesis state. Its connection to the hub is a co-abundance observation, not proof of a direct molecular interaction, and the module does not establish an integrated translational mechanism.

#### GTF3C5

- **Related proteins** (co-abundance neighbors): SPIN1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: general transcription factor IIIC subunit 5. Predicted to contribute to DNA binding activity. Predicted to be involved in 5S class rRNA transcription by RNA polymerase III and tRNA transcription by RNA polymerase III. Predicted to act upstream of or within skeletal muscle cell differentiation. Located in nucleoplasm. Part of transcription factor TFIIIC complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.501); complex neurodevelopmental disorder (0.416); neurodevelopmental disorder (0.370); Intellectual disability (0.370); hemorrhagic disease (0.252)
- **Europe PMC papers**: 200
- **Why important**: GTF3C5 is directly connected to SPIN1 hu.MAP and is a subunit of the TFIIIC complex involved in RNA polymerase three transcription of tRNA and five-S rRNA. It is cell-type enhanced in breast lactating cells and epididymal principal cells despite otherwise low tissue and cell-type specificity, and it has associations with neurodevelopmental and hemorrhagic disorders.
- **Conclusion**: Established evidence supports GTF3C5 as a transcription-factor-complex component involved in RNA polymerase three transcription. Its presence may indicate demand for core RNA production, but the cell-type observations do not establish that those specialized cell types explain this cross-tissue module.

#### NOL10

- **Related proteins** (co-abundance neighbors): SPIN1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleolar protein 10. Enables RNA binding activity. Predicted to be involved in maturation of SSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Located in nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.407); prostate carcinoma (0.392); prostate cancer (0.323); benign digestive system neoplasm (0.272); poisoning (0.238)
- **Europe PMC papers**: 249
- **Why important**: NOL10 is directly connected to SPIN1 hu.MAP and is a nucleolar RNA-binding protein involved in maturation of small-subunit ribosomal RNA. It provides a distinct ribosome-biogenesis perspective within the module and has disease associations including neurodegenerative disease and prostate carcinoma.
- **Conclusion**: Established evidence supports NOL10 as a nucleolar ribosome-biogenesis factor. Its co-abundance with SPIN1 may reflect coordinated RNA-production or growth-related cellular state, but no physical interaction, complex membership or globally significant enrichment supports that interpretation directly.

## Module 18

**Tissue pair**: circulatory_system and lung  
**Genes (6)**: EOGT, NUCB1, PIK3R2, PLXNB2, PUS1, RRBP1

### Function

This is a heterogeneous co-abundance module rather than a module supported by a single significantly enriched pathway. No GO or KEGG term passed global correction, and STRING reported no supplementary functional enrichment. The gene annotations nevertheless suggest a possible connection among endoplasmic-reticulum and Golgi protein handling, extracellular-targeted protein glycosylation, cell-surface receptor biology, intracellular signaling, and RNA modification. EOGT is the central network connector and is an ER glycosylation enzyme that modifies EGF-like proteins, including Notch. RRBP1 supports ER organization and secretory pathways, NUCB1 is associated with Golgi calcium handling and is secreted to blood, PLXNB2 is a semaphorin-responsive cell-surface receptor, PIK3R2 is a regulatory component of PI3K signaling, and PUS1 supports RNA pseudouridine synthesis. These annotations support a broad secretory, membrane-signaling, and cellular-maintenance interpretation, but not a single established pathway assignment.

**Cell composition.** The module does not appear to be dominated by broadly expressed housekeeping genes or by a uniform blood-cell program. HPA reports low tissue specificity for most genes, while cell-type annotations are diverse and include cardiomyocytes, smooth-muscle populations, epithelial populations, pancreatic and salivary acinar cells, astroglial and neuronal groups, and myeloid populations. A minority of module products are classified as secreted, including NUCB1, so blood-derived protein abundance could contribute in some sample contexts. However, most genes are intracellular or membrane-associated rather than clearly plasma proteins. All module proteins were detected by immunohistochemistry in lung, whereas no matching circulatory-system tissue result was available. The shared signal may therefore reflect common vascular, epithelial, smooth-muscle, or other constituent cell populations across the two tissues rather than a blood-only signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair met the reported STRING interaction threshold, and STRING listed no partners for the individual genes. Thus, the co-abundance relationships are not corroborated here by high-confidence STRING physical or functional links. The only listed hu.MAP relationship is (hu.MAP huMAP3_09327.1), which contains EOGT and PLXNB2 among a much broader complex membership. This provides limited support for a possible shared protein-complex context involving those genes, but it does not establish that the entire module is a physical complex. The remaining co-abundance edges may represent coordinated expression, shared cell-type origin, indirect regulation, or technical and tissue-composition effects.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09327.1 (PLXNB2, EOGT; 2/93)

### Novelty

This module is a potentially novel tissue-pair co-abundance pattern, but it cannot be called a newly discovered biological mechanism from the available evidence. Its genes span ER organization, glycosylation, Golgi calcium biology, RNA modification, PI3K signaling, and plexin-mediated receptor functions, with no globally significant GO or KEGG term and no STRING-supported interaction network. The limited overlap with hu.MAP through (hu.MAP huMAP3_09327.1) shows that at least part of the biology has prior complex-level context. Therefore, the defensible conclusion is that the shared expression pattern is a candidate context-specific association requiring independent replication and experimental validation, not proof of a new pathway or complex.

**Hypothesis.** Hypothesis: the module reflects coordinated activity of secretory and surface-signaling cells shared by lung and circulatory-system samples. In this model, RRBP1 marks ER organization and secretory capacity, EOGT supports glycosylation of extracellular-targeted EGF-like proteins, NUCB1 contributes to Golgi calcium handling and extracellular protein abundance, and PLXNB2 represents a cell-surface receptor component. PIK3R2 could connect membrane-associated signals to PI3K-dependent intracellular responses, while PUS1 may reflect a parallel RNA and mitochondrial maintenance state. This is a mechanistic hypothesis based on annotations and network structure; the co-abundance data do not demonstrate directionality, physical binding, or causal regulation.

### Important genes

#### EOGT

- **Related proteins** (co-abundance neighbors): PUS1 (0.91), RRBP1 (0.84), NUCB1 (0.83), PLXNB2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_09327.1
- **Function (MyGene.info)**: EGF domain specific O-linked N-acetylglucosamine transferase. This gene encodes an enzyme that acts in the lumen of the endoplasmic reticulum to catalyze the transfer of N-acetylglucosamine to serine or threonine residues of extracellular-targeted proteins. This enzyme modifies proteins containing eukaryotic growth factor (EGF)-like domains, including the Notch receptor, thereby regulating developmental signalling. Mutations in this gene have been observed i…
- **Diseases (Open Targets)**: Adams-Oliver syndrome (0.804); hereditary disease (0.193); retinitis pigmentosa (0.074); frozen shoulder (0.066); exudative vitreoretinopathy (0.066)
- **Europe PMC papers**: 413
- **Why important**: EOGT is the central connector in the module and links several otherwise weakly connected genes, including RRBP1, NUCB1, PUS1, and PLXNB2. Its established function is ER-lumen O-linked N-acetylglucosamine transfer to EGF-like domains, including Notch-related substrates. It is also the module gene with direct hu.MAP context through (hu.MAP huMAP3_09327.1). Its Adams-Oliver syndrome association and substantial literature support make it the strongest candidate for a biologically informative anchor.
- **Conclusion**: Established evidence supports EOGT as an ER glycosylation enzyme involved in extracellular-targeted protein maturation and developmental signaling. The hypothesis that its central co-abundance position coordinates glycosylation with plexin and secretory-cell programs is plausible but unproven.

#### RRBP1

- **Related proteins** (co-abundance neighbors): EOGT (0.84), PIK3R2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosome binding protein 1. This gene encodes a ribosome-binding protein of the endoplasmic reticulum (ER) membrane. Studies suggest that this gene plays a role in ER proliferation, secretory pathways and secretory cell differentiation, and mediation of ER-microtubule interactions. Alternative splicing has been observed and protein isoforms are characterized by regions of N-terminal decapeptide and C-terminal heptad repeats.…
- **Diseases (Open Targets)**: cancer (0.476); dengue disease (0.462); neurodegenerative disease (0.324); coronary artery disorder (0.292); placental abruption (0.279)
- **Europe PMC papers**: 1654
- **Why important**: RRBP1 occupies a bridging position between EOGT and PIK3R2. It is an ER membrane ribosome-binding protein associated with ER proliferation, secretory pathways, secretory-cell differentiation, and ER-microtubule interactions. Its tissue-enhanced and acinar-cell annotations make it particularly relevant to interpreting sample composition. It also has broad disease and literature associations, including links to cancer, neurodegenerative disease, and coronary artery disorder.
- **Conclusion**: Established evidence supports RRBP1 as an ER structural and secretory-pathway component. Its position suggests that ER capacity may help explain the module, but a direct role for RRBP1 in coordinating PIK3R2 or EOGT abundance remains a hypothesis.

#### PLXNB2

- **Related proteins** (co-abundance neighbors): EOGT (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location None; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_09327.1
- **Function (MyGene.info)**: plexin B2. Members of the B class of plexins, such as PLXNB2 are transmembrane receptors that participate in axon guidance and cell migration in response to semaphorins (Perrot et al. (2002) [PubMed 12183458]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Intellectual disability (0.519); amelogenesis imperfecta (0.518); sensorineural hearing loss disorder (0.516); cutaneous melanoma (0.486); neurodegenerative disease (0.455)
- **Europe PMC papers**: 2109
- **Why important**: PLXNB2 is the module's cell-surface receptor representative and is connected to EOGT in the co-abundance graph and in hu.MAP complex (hu.MAP huMAP3_09327.1). Plexin B2 is involved in semaphorin-responsive axon guidance and cell migration, with annotations also covering cell adhesion, receptor-mediated endocytosis, and developmental processes. Its lung-associated alveolar annotation and myeloid-cell enrichment make it informative for distinguishing a structural or epithelial signal from a purely intracellular program.
- **Conclusion**: Established evidence supports PLXNB2 as a membrane receptor involved in migration, adhesion, and developmental signaling. Its apparent association with EOGT may indicate shared cellular context or complex biology, but the available data do not establish direct glycosylation-dependent regulation.

#### PIK3R2

- **Related proteins** (co-abundance neighbors): RRBP1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Not detected in immune cells; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoinositide-3-kinase regulatory subunit 2. Phosphatidylinositol 3-kinase (PI3K) is a lipid kinase that phosphorylates phosphatidylinositol and similar compounds, creating second messengers important in growth signaling pathways. PI3K functions as a heterodimer of a regulatory and a catalytic subunit. The protein encoded by this gene is a regulatory component of PI3K. Three transcript variants, one protein coding and the other two non-prote…
- **Diseases (Open Targets)**: megalencephaly-polymicrogyria-postaxial polydactyly-hydrocephalus syndrome (0.803); megalencephaly-polymicrogyria-polydactyly-hydrocephalus syndrome 1 (0.766); cancer (0.588); overgrowth syndrome and/or cerebral malformations due to abnormalities in MTOR pathway genes (0.463); Seizure (0.445)
- **Europe PMC papers**: 5296
- **Why important**: PIK3R2 is the module's clearest signaling component and is connected to RRBP1. It encodes a regulatory subunit of PI3K, with established roles in signal transduction, insulin-receptor signaling, glucose homeostasis, autophagy regulation, and immune-related processes. Its disease associations include developmental overgrowth and brain malformation syndromes, cancer, and seizure, and it has extensive literature support.
- **Conclusion**: Established evidence supports PIK3R2 as a PI3K regulatory protein. Its inclusion is consistent with a signaling interpretation of the module, but the co-abundance relationship with an ER protein does not demonstrate that this module activates PI3K signaling.

#### NUCB1

- **Related proteins** (co-abundance neighbors): EOGT (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleobindin 1. This gene encodes a member of a small calcium-binding EF-hand protein family. The encoded protein is thought to have a key role in Golgi calcium homeostasis and Ca(2+)-regulated signal transduction events. [provided by RefSeq, Jun 2010].
- **Diseases (Open Targets)**: neoplasm (0.099); breast cancer (0.083); breast carcinoma (0.082); diffuse large B-cell lymphoma (0.074); pancreatic ductal adenocarcinoma (0.066)
- **Europe PMC papers**: 626
- **Why important**: NUCB1 is connected to EOGT and is relevant to sample-composition interpretation because HPA classifies it as secreted to blood. It is a Golgi-localized calcium-binding protein associated with Golgi calcium homeostasis and calcium-regulated signaling, and it shows epithelial and stromal cell-type annotations. These features make it a plausible link between intracellular secretory compartments and extracellular or blood-measurable protein abundance.
- **Conclusion**: Established evidence supports NUCB1 as a Golgi-associated calcium-binding and secreted protein. Its presence could reflect secretory-cell abundance or extracellular carryover in tissue samples; any proposed role in coordinating this module with EOGT is speculative.

## Module 19

**Tissue pair**: circulatory_system and lung  
**Genes (11)**: FASTKD1, HEXA, HSPA13, MAIP1, NDUFAF4, NFU1, P4HA1, PNPT1, SCAMP1, SUCLA2, TIMMDC1

### Function

No GO/KEGG term passed global correction, so there is no primary globally significant GO/KEGG functional enrichment for this module. The supplementary STRING results repeatedly point toward mitochondrial biology, including mitochondrial localization (STRING Component Mitochondrion; within-query FDR = 0.0063) (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0181) (STRING Keyword Mitochondrion; within-query FDR = 0.0292), mitochondrial disease associations (STRING Keyword Primary mitochondrial disease; within-query FDR = 0.0018) (STRING DISEASES Mitochondrial metabolism disease; within-query FDR = 0.0139), abnormal mitochondrial metabolism (STRING HPO Abnormality of mitochondrial metabolism; within-query FDR = 0.0092), reduced respiratory-chain activity (STRING HPO Decreased activity of mitochondrial respiratory chain; within-query FDR = 0.0099), and mitochondrial RNA-related membership through the annotated genes. The most coherent interpretation is a mitochondrial maintenance and energy-metabolism module, spanning complex I assembly, mitochondrial RNA handling, iron-sulfur cluster biogenesis, the tricarboxylic acid cycle, mitochondrial calcium and membrane-protein homeostasis, and quality control. Because the co-abundance graph is sparse and lacks broad primary enrichment, this should be treated as a biologically plausible functional theme rather than a formally established pathway enrichment.

**Cell composition.** The module does not resemble a blood-cell-enriched module: every gene has low immune-cell specificity in HPA, and no enriched blood-cell category is reported. Most genes have low tissue specificity, arguing against a sharply tissue-restricted program and allowing the shared signal in circulatory_system and lung to reflect broadly distributed cellular biology. HPA reports cell-type enhancement for most genes, with recurrent signals in syncytiotrophoblasts, choroid plexus epithelial cells, myonuclei, and oocytes, but these patterns do not identify a single shared cell type in the two sampled tissues. HPA reports three secreted genes at the module level, although the individual annotations predominantly place the proteins intracellularly, in mitochondria, vesicles, membranes, or the endoplasmic reticulum. Lung protein detection is widespread among the annotated genes, whereas matched circulatory-system tissue protein evidence is unavailable. Overall, sample composition or shared cell populations cannot be excluded, but a simple plasma-protein or blood-cell explanation is not supported by the HPA summary.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The known interaction structure is limited. STRING identifies a single high-confidence relationship, NDUFAF4–TIMMDC1, and both genes are independently annotated as mitochondrial complex I assembly factors. This pair provides direct support for one mechanistic submodule. The remaining co-abundance links are not represented by high-confidence STRING partnerships in the supplied results, so they may reflect co-regulation, shared cellular state, indirect biology, or tissue-composition effects rather than direct physical interaction. No hu.MAP complex contains at least two module members. Thus, the network is not a recovered canonical protein complex; it is a sparse co-abundance structure with one strongly supported known interaction and several functionally suggestive but unvalidated connections.

**STRING interactions (score >= 0.7)**: 1 of 55 gene pairs: NDUFAF4–TIMMDC1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Primary mitochondrial disease (FDR = 0.0018, 5 genes); Component Mitochondrion (FDR = 0.0063, 9 genes); HPO Abnormality of mitochondrial metabolism (FDR = 0.0092, 5 genes); HPO Decreased activity of mitochondrial respiratory chain (FDR = 0.0099, 4 genes); DISEASES Mitochondrial metabolism disease (FDR = 0.0139, 5 genes); COMPARTMENTS Mitochondrion (FDR = 0.0181, 8 genes); Keyword Mitochondrion (FDR = 0.0292, 7 genes); HPO Poor head control (FDR = 0.0367, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a new tissue-pair co-abundance observation, but the supplied evidence does not establish a new molecular mechanism. The mitochondrial theme is biologically established through gene annotations and the repeated supplementary STRING categories, and the NDUFAF4–TIMMDC1 relationship is already known. The absence of a hu.MAP complex and the limited STRING connectivity indicate that the particular cross-tissue co-abundance arrangement is not represented as a well-known complex, but absence from those resources alone cannot prove novelty. A defensible claim is therefore that the shared circulatory_system–lung co-abundance pattern is potentially novel as a tissue-level organization of partly known mitochondrial components, requiring replication and independent validation.

**Hypothesis.** Hypothesis: the module reflects coordinated mitochondrial maintenance in a shared cellular population or shared physiological state across circulatory_system and lung. In this model, FASTKD1 and PNPT1 support mitochondrial RNA processing and stability, NDUFAF4 and TIMMDC1 support complex I assembly, NFU1 supports iron-sulfur cluster delivery, SUCLA2 supports tricarboxylic-acid-cycle and mitochondrial nucleotide-energy metabolism, and MAIP1 may connect mitochondrial membrane-protein insertion with calcium homeostasis. The sparse graph and lack of a hu.MAP complex make it more likely that this is a coordinated state program than one physical multiprotein complex. This hypothesis predicts that module activity should track mitochondrial respiratory capacity, mitochondrial RNA integrity, or cellular energetic demand in the relevant lung and circulatory samples; it does not establish that the observed co-abundance links are causal.

### Important genes

#### FASTKD1

- **Related proteins** (co-abundance neighbors): NDUFAF4 (0.86), P4HA1 (0.86), PNPT1 (0.84), HEXA (0.84), MAIP1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FASTK mitochondrial RNA regulator 1. Enables RNA binding activity. Involved in mitochondrial RNA metabolic process and regulation of mitochondrial mRNA stability. Located in mitochondrion. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: secondary hypertrophic osteoarthropathy (0.190); stroke disorder (0.164); alcohol drinking (0.164); myocardial infarction (0.036); diabetes mellitus (0.036)
- **Europe PMC papers**: 155
- **Why important**: FASTKD1 has the strongest network position in the module, connecting mitochondrial and non-mitochondrial annotated genes across several co-abundance edges. Its annotation directly supports mitochondrial RNA metabolism, RNA processing, and mitochondrial messenger RNA stability. HPA places it in mitochondria and reports lung protein detection. Its disease associations include stroke disorder and myocardial infarction, which are relevant to the circulatory context, while its literature base is substantial.
- **Conclusion**: Established evidence supports FASTKD1 as a central mitochondrial RNA-regulatory component and the principal network connector in this module. It is a strong candidate for organizing the shared signal, but the network does not prove that FASTKD1 regulates the other module genes. Its role as a module driver remains a hypothesis.

#### NDUFAF4

- **Related proteins** (co-abundance neighbors): FASTKD1 (0.86), SCAMP1 (0.81), TIMMDC1 (0.80); STRING partners: TIMMDC1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase complex assembly factor 4. NADH:ubiquinone oxidoreductase (complex I) catalyzes the transfer of electrons from NADH to ubiquinone (coenzyme Q) in the first step of the mitochondrial respiratory chain, resulting in the translocation of protons across the inner mitochondrial membrane. This gene encodes a complex I assembly factor. Mutations in this gene are a cause of mitochondrial complex I deficiency. [provided by RefSeq, O…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.714); type 2 diabetes mellitus (0.607); mitochondrial disease (0.597); diabetes mellitus (0.578); mitochondrial complex I deficiency, nuclear type 15 (0.568)
- **Europe PMC papers**: 378
- **Why important**: NDUFAF4 is directly linked to TIMMDC1 by a high-confidence STRING interaction and is annotated as a mitochondrial complex I assembly factor. It participates in the broadest set of supplementary STRING signals in the module, including mitochondrial disease, mitochondrial metabolism, respiratory-chain activity, and poor head control (8 supplementary STRING terms; within-query FDR 0.0018–0.0367). It has a strong mitochondrial disease evidence profile and a substantial literature base.
- **Conclusion**: Established evidence identifies NDUFAF4 as a complex I assembly factor with disease relevance, and the NDUFAF4–TIMMDC1 relationship is known. It is likely an anchor of the mitochondrial interpretation. Whether its co-abundance with the other genes reflects coordinated respiratory-chain regulation in these tissues is not established.

#### TIMMDC1

- **Related proteins** (co-abundance neighbors): NDUFAF4 (0.80); STRING partners: NDUFAF4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translocase of inner mitochondrial membrane domain containing 1. Located in mitochondrion and nucleoplasm. Implicated in nuclear type mitochondrial complex I deficiency 31. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 31 (0.665); mitochondrial complex I deficiency (0.626); neurodegenerative disease (0.548); mitochondrial disease (0.371); primary biliary cholangitis (0.350)
- **Europe PMC papers**: 374
- **Why important**: TIMMDC1 forms the module's other known high-confidence STRING interaction with NDUFAF4 and is independently annotated in mitochondrial complex I assembly. It appears across the supplementary mitochondrial disease and respiratory-chain categories (8 supplementary STRING terms; within-query FDR 0.0018–0.0367). HPA places it in mitochondria, detects it in lung, and reports cell-type enhancement in syncytiotrophoblasts. Its disease associations include nuclear mitochondrial complex I deficiency.
- **Conclusion**: Established evidence supports TIMMDC1 as a mitochondrial complex I assembly component and as the best-supported interaction partner of NDUFAF4 in this module. It reinforces a respiratory-chain interpretation, but the tissue-pair co-abundance pattern and any functional connection to the peripheral module genes remain hypotheses.

#### PNPT1

- **Related proteins** (co-abundance neighbors): FASTKD1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polyribonucleotide nucleotidyltransferase 1. The protein encoded by this gene belongs to the evolutionary conserved polynucleotide phosphorylase family comprised of phosphate dependent 3'-to-5' exoribonucleases implicated in RNA processing and degradation. This enzyme is predominantly localized in the mitochondrial intermembrane space and is involved in import of RNA to mitochondria. Mutations in this gene have been associated with combined …
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 13 (0.807); autosomal recessive nonsyndromic hearing loss 70 (0.740); spinocerebellar ataxia type 25 (0.709); deafness (0.676); hearing loss, autosomal recessive (0.634)
- **Europe PMC papers**: 839
- **Why important**: PNPT1 is a mitochondrial RNA-processing and RNA-import factor with a strong disease literature, including combined oxidative phosphorylation deficiency, hereditary hearing loss, and spinocerebellar ataxia. It recurs in the supplementary mitochondrial disease, mitochondrial metabolism, respiratory-chain, and neurological phenotype categories (8 supplementary STRING terms; within-query FDR 0.0018–0.0367). Its annotated mitochondrial RNA catabolic and processing functions complement FASTKD1, although its direct network connection is limited to FASTKD1.
- **Conclusion**: Established evidence supports PNPT1 as a mitochondrial RNA-processing component with clinically important links to oxidative phosphorylation disorders. Its co-abundance with FASTKD1 is consistent with a shared mitochondrial RNA-maintenance program, but does not demonstrate direct physical interaction or a causal role in the tissue-pair module.

#### NFU1

- **Related proteins** (co-abundance neighbors): MAIP1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NFU1 iron-sulfur cluster scaffold. This gene encodes a protein that is localized to mitochondria and plays a critical role in iron-sulfur cluster biogenesis. The encoded protein assembles and transfers 4Fe-4S clusters to target apoproteins including succinate dehydrogenase and lipoic acid synthase. Mutations in this gene are a cause of multiple mitochondrial dysfunctions syndrome-1, and pseudogenes of this gene are located on the s…
- **Diseases (Open Targets)**: multiple mitochondrial dysfunctions syndrome 1 (0.813); spastic paraplegia 93, autosomal recessive (0.589); neurodegenerative disease (0.559); osteoarthritis, hip (0.377); multiple mitochondrial dysfunctions syndrome 2 (0.373)
- **Europe PMC papers**: 581
- **Why important**: NFU1 is a mitochondrial iron-sulfur cluster scaffold involved in maturation of respiratory and metabolic proteins, including succinate dehydrogenase and lipoic acid synthase. It appears repeatedly in the supplementary mitochondrial, mitochondrial-disease, metabolism, and respiratory-chain categories (7 supplementary STRING terms; within-query FDR 0.0018–0.0292). Its disease associations include multiple mitochondrial dysfunction syndromes and neurodegenerative disease. Within the network it connects to MAIP1, providing a possible bridge between mitochondrial assembly and membrane or calcium-related biology.
- **Conclusion**: Established evidence supports NFU1 as a core mitochondrial maturation factor whose dysfunction can impair several metabolic systems. Its presence strengthens the interpretation of broad mitochondrial functional capacity rather than a narrowly defined complex. The proposed bridge through MAIP1 is a hypothesis because no known interaction or hu.MAP complex is supplied.
