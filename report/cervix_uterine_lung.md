# Conserved co-abundance modules: cervix_uterine and lung

## Module 0

**Tissue pair**: cervix_uterine and lung  
**Genes (45)**: SLC3A2, SLC1A5, ACADVL, ACO2, ACSL3, AGPS, AIFM1, ASPH, ATL3, MTHFD1L, CPD, CS, CKAP4, HSD17B4, GFM1, EMC1, GNAI3, IKBIP, ITGB1, TMPO, TMPO, NCSTN, DDOST, ALDH18A1, PCK2, PIGS, PNPT1, NUP210, UQCRC1, RAB18, RAB21, RTN1, RTN4, OXCT1, SDHA, SEC63, SFXN1, SUPV3L1, MARS1, TACSTD2, TIMM50, TMEM109, TMEM214, TNPO1, VDAC2

### Function

The module is best interpreted as a membrane-organelle homeostasis program centered on the endoplasmic reticulum, with links to mitochondrial metabolism, membrane trafficking, protein insertion, amino-acid transport, and organelle organization. The primary evidence is the globally corrected enrichment for organelle membrane (GO:CC organelle membrane; q_global = 1.26e-06), endoplasmic reticulum membrane and subcompartments (4 globally significant GO/KEGG terms, q_global 3.79e-06–5.99e-05; see the table), the endoplasmic reticulum (GO:CC endoplasmic reticulum; q_global = 0.00276), the tubular endoplasmic-reticulum network (GO:CC endoplasmic reticulum tubular network; q_global = 0.00518), membrane-protein complexes (GO:CC membrane protein complex; q_global = 0.018), membrane (GO:CC membrane; q_global = 0.0209), transmembrane transport (GO:BP transmembrane transport; q_global = 0.0232), amino-acid transmembrane transport (GO:BP amino acid transmembrane transport; q_global = 0.0235), and endoplasmic-reticulum organization (GO:BP endoplasmic reticulum tubular network organization; q_global = 0.0398) (GO:BP endoplasmic reticulum organization; q_global = 0.0477). The enrichment is therefore not adequately described as a generic membrane signature: it specifically points to ER architecture and ER–mitochondrial functional coupling, with transport and bioenergetic support. The mitochondrial interpretation is supported mainly by the gene annotations and supplementary STRING results rather than by a separate globally corrected GO term. No KEGG term is provided as globally significant.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It is also not dominated by a single tissue-restricted lineage. Most genes have low tissue specificity, and protein detection is generally present in both cervix_uterine and lung, supporting a broadly expressed intracellular program. The HPA data do show cell-type-enhanced representation in neutrophils and several epithelial, trophoblast-like, muscle, hepatic, and hematopoietic populations. Immune-cell specificity is usually low, although a subset is immune-cell enhanced and neutrophils are a recurrent enriched cell type. Consequently, shared abundance may reflect common intracellular demands or shared cell populations in the samples, including myeloid-cell contribution, rather than a cervix- or lung-specific pathway. The HPA protein evidence does not support a blood-plasma contamination explanation by itself.

**GO/KEGG enrichment**: 13 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC organelle membrane | 1.26e-06 | ACADVL, ACSL3, AGPS, AIFM1, ALDH18A1, ASPH, ATL3, CKAP4, DDOST, EMC1, GNAI3, HSD17B4, IKBIP, ITGB1, NCSTN, NUP210, PIGS, PNPT1, RAB18, RAB21, RTN1, RTN4, SDHA, SEC63, SFXN1, SLC3A2, TIMM50, TMEM109, TMEM214, TMPO, UQCRC1, VDAC2 |
| GO:CC endoplasmic reticulum membrane | 3.79e-06 | ACSL3, ASPH, ATL3, CKAP4, DDOST, EMC1, GNAI3, IKBIP, NCSTN, NUP210, PIGS, PNPT1, RAB18, RAB21, RTN1, RTN4, SEC63, TMEM109, TMEM214 |
| GO:CC endoplasmic reticulum subcompartment | 3.79e-06 | ACSL3, ASPH, ATL3, CKAP4, DDOST, EMC1, GNAI3, IKBIP, NCSTN, NUP210, PIGS, PNPT1, RAB18, RAB21, RTN1, RTN4, SEC63, TMEM109, TMEM214 |
| GO:CC nuclear outer membrane-endoplasmic reticulum membrane network | 5.59e-06 | ACSL3, ASPH, ATL3, CKAP4, DDOST, EMC1, GNAI3, IKBIP, NCSTN, NUP210, PIGS, PNPT1, RAB18, RAB21, RTN1, RTN4, SEC63, TMEM109, TMEM214 |
| GO:CC organelle subcompartment | 5.99e-05 | ACSL3, ASPH, ATL3, CKAP4, DDOST, EMC1, GNAI3, IKBIP, NCSTN, NUP210, PIGS, PNPT1, RAB18, RAB21, RTN1, RTN4, SEC63, TMEM109, TMEM214 |
| GO:CC endoplasmic reticulum | 0.00276 | ACSL3, ASPH, ATL3, CKAP4, DDOST, EMC1, GNAI3, IKBIP, NCSTN, NUP210, PIGS, PNPT1, RAB18, RAB21, RTN1, RTN4, SEC63, TIMM50, TMEM109, TMEM214 |
| GO:CC endoplasmic reticulum tubular network | 0.00518 | ASPH, ATL3, RAB18, RTN4 |
| GO:CC membrane protein complex | 0.018 | ASPH, DDOST, EMC1, GNAI3, ITGB1, NCSTN, PIGS, SDHA, SEC63, SLC3A2, TIMM50, TMEM109, UQCRC1, VDAC2 |
| GO:CC membrane | 0.0209 | ACADVL, ACSL3, AGPS, AIFM1, ALDH18A1, ASPH, ATL3, CKAP4, CPD, CS, DDOST, EMC1, GNAI3, HSD17B4, IKBIP, ITGB1, MARS1, MTHFD1L, NCSTN, NUP210, PIGS, PNPT1, RAB18, RAB21, RTN1, RTN4, SDHA, SEC63, SFXN1, SLC1A5, SLC3A2, TACSTD2, TIMM50, TMEM109, TMEM214, TMPO, UQCRC1, VDAC2 |
| GO:BP transmembrane transport | 0.0232 | AIFM1, ASPH, ITGB1, PNPT1, SEC63, SFXN1, SLC1A5, SLC3A2, TIMM50, TMEM109, UQCRC1, VDAC2 |
| GO:BP amino acid transmembrane transport | 0.0235 | ITGB1, SFXN1, SLC1A5, SLC3A2 |
| GO:BP endoplasmic reticulum tubular network organization | 0.0398 | ATL3, RAB18, RTN1, RTN4 |
| GO:BP endoplasmic reticulum organization | 0.0477 | ATL3, EMC1, RAB18, RTN1, RTN4 |

### STRING and hu.MAP

STRING supports a mixture of established substructures rather than one fully connected canonical complex. The strongest known relationships include the mitochondrial metabolic cluster involving ACO2, CS, SDHA, UQCRC1, OXCT1, and PCK2; the ER-shaping relationships among ATL3, RTN1, and RTN4; the SEC63–TMEM214 relationship; the DDOST–EMC1 relationship; the mitochondrial RNA-processing relationship between PNPT1 and SUPV3L1; and the amino-acid transporter pair SLC1A5–SLC3A2. ITGB1–RAB21 also links membrane adhesion to trafficking. STRING enrichment (15 supplementary STRING terms; within-query FDR 6.01e-08–0.0057) independently supports transmembrane, membrane, ER, mitochondrial, and membrane-protein-complex properties, but it is supplementary and its reported false-discovery values are not global module significance. hu.MAP provides established complex context for the mitochondrial and organelle-interface portions: ALDH18A1, PCK2, MTHFD1L, PNPT1, and GFM1 occur together in a mitochondrial-associated complex (hu.MAP huMAP3_13468.1); VDAC2, CKAP4, and TMEM109 recur in organelle-interface complexes (hu.MAP huMAP3_08403.1) (hu.MAP huMAP3_09822.1) (hu.MAP huMAP3_10525.1) (hu.MAP huMAP3_10725.1); ACSL3, VDAC2, and TNPO1 occur in another complex (hu.MAP huMAP3_09592.1); RTN1 and RTN4 recur across several reticulon-related complexes (hu.MAP huMAP3_08799.1) (hu.MAP huMAP3_05344.1) (hu.MAP huMAP3_10855.1) (hu.MAP huMAP3_09584.1) (hu.MAP huMAP3_10255.1) (hu.MAP huMAP3_14009.1); and SLC1A5 with SFXN1 appears in (hu.MAP huMAP3_10473.1). These observations indicate that parts of the module recapitulate known molecular systems, while the complete co-abundance arrangement is more heterogeneous.

**STRING interactions (score >= 0.7)**: 19 of 990 gene pairs: ACO2–CS (0.999); ACO2–SDHA (0.975); ACO2–TIMM50 (0.755); ACO2–UQCRC1 (0.855); ALDH18A1–CS (0.704); ATL3–RTN1 (0.865); ATL3–RTN4 (0.826); CS–PCK2 (0.958); CS–SDHA (0.984); CS–UQCRC1 (0.71); DDOST–EMC1 (0.818); GFM1–PNPT1 (0.842); ITGB1–RAB21 (0.815); OXCT1–SDHA (0.874); PNPT1–SUPV3L1 (0.999); RTN1–RTN4 (0.849); SDHA–UQCRC1 (0.968); SEC63–TMEM214 (0.723); SLC1A5–SLC3A2 (0.894)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transmembrane (FDR = 6.01e-08, 22 genes); Component Integral component of membrane (FDR = 1.1e-07, 26 genes); Component Organelle membrane (FDR = 1.1e-07, 32 genes); Keyword Transmembrane helix (FDR = 1.68e-07, 21 genes); Keyword Membrane (FDR = 2.96e-07, 32 genes); Component Endoplasmic reticulum membrane (FDR = 1.33e-06, 18 genes); COMPARTMENTS Organelle membrane (FDR = 7.41e-05, 25 genes); Keyword Transit peptide (FDR = 0.00047, 14 genes); Keyword Mitochondrion (FDR = 0.0011, 17 genes); COMPARTMENTS Membrane (FDR = 0.0013, 30 genes); Component Membrane (FDR = 0.0014, 38 genes); Component Endoplasmic reticulum tubular network (FDR = 0.0036, 4 genes); Keyword Endoplasmic reticulum (FDR = 0.0042, 13 genes); Component Mitochondrion (FDR = 0.0044, 19 genes); Component Membrane protein complex (FDR = 0.0057, 13 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (ALDH18A1, PCK2, MTHFD1L, PNPT1, GFM1; 5/99); huMAP3_08403.1 (VDAC2, CKAP4, TMEM109; 3/10); huMAP3_09822.1 (VDAC2, CKAP4, TMEM109; 3/28); huMAP3_10525.1 (ALDH18A1, MTHFD1L, GFM1; 3/33); huMAP3_10725.1 (VDAC2, CKAP4, TMEM109; 3/59); huMAP3_09592.1 (ACSL3, VDAC2, TNPO1; 3/95); huMAP3_08799.1 (RTN1, RTN4; 2/5); huMAP3_05344.1 (RTN1, RTN4; 2/7); huMAP3_10473.1 (SLC1A5, SFXN1; 2/24); huMAP3_10855.1 (RTN1, RTN4; 2/24); huMAP3_09584.1 (RTN1, RTN4; 2/28); huMAP3_10255.1 (RTN1, RTN4; 2/30); huMAP3_14009.1 (RTN1, RTN4; 2/42)

### Novelty

The module should not be called a wholly new molecular pathway. Many of its relationships and complexes are already represented in STRING and hu.MAP, especially ER shaping, mitochondrial metabolism, mitochondrial RNA handling, amino-acid transport, and organelle-interface assemblies. Nevertheless, the conserved co-abundance of these components across cervix_uterine and lung may represent a new tissue-pair observation or a new systems-level combination. The fact sheet does not establish whether this exact gene set or co-abundance module has appeared previously in published tissue-network studies. Absence of some edges from STRING or hu.MAP is not evidence of novelty, because those resources are incomplete and interaction evidence is context dependent. The defensible conclusion is conditional novelty at the module-organization or cross-tissue level, not discovery of previously unknown individual interactions.

**Hypothesis.** Hypothesis: the module coordinates ER membrane architecture and protein-handling capacity with mitochondrial import, RNA surveillance, respiration, lipid metabolism, and amino-acid supply. In cells sharing substantial secretory, barrier, metabolic, or stress-handling demands, ER-shaping proteins such as ATL3 and reticulons could maintain tubular ER structure, while SEC63 and EMC1 support membrane-protein insertion. Transporters and trafficking factors could supply substrates and route membrane cargo, and mitochondrial components could sustain energy production and mitochondrial gene expression. The conserved abundance pattern may therefore reflect coordinated organelle proteostasis and metabolic adaptation. This remains a hypothesis because co-abundance does not demonstrate physical interaction, directionality, or causal regulation.

### Important genes

#### SEC63

- **Related proteins** (co-abundance neighbors): EMC1 (0.84), ASPH (0.83), OXCT1 (0.82), PNPT1 (0.82), NUP210 (0.81), ALDH18A1 (0.81), ACSL3 (0.80), UQCRC1 (0.80); STRING partners: TMEM214 (0.723)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC63 protein translocation regulator. The Sec61 complex is the central component of the protein translocation apparatus of the endoplasmic reticulum (ER) membrane. The protein encoded by this gene and SEC62 protein are found to be associated with ribosome-free SEC61 complex. It is speculated that Sec61-Sec62-Sec63 may perform post-translational protein translocation into the ER. The Sec61-Sec62-Sec63 complex might also perform the bac…
- **Diseases (Open Targets)**: autosomal dominant polycystic liver disease (0.795); neurodegenerative disease (0.526); polycystic liver disease 1 (0.430); Biliary tract abnormality (0.346); placental abruption (0.232)
- **Europe PMC papers**: 1756
- **Why important**: SEC63 is among the highest-connectivity genes in the module and occupies a central position linking EMC1, ASPH, OXCT1, PNPT1, NUP210, ALDH18A1, UQCRC1, and ACSL3. It is an ER protein-translocation regulator, is included in many primary ER and membrane terms (9 globally significant GO/KEGG terms, q_global 1.26e-06–0.0232; see the table), and has a known STRING relationship with TMEM214. Its broad HPA profile and detection in both tissues are consistent with a shared intracellular program rather than a restricted cell type. Its disease associations include polycystic liver disease and neurodegenerative disease, and its literature support is substantial.
- **Conclusion**: Established evidence supports SEC63 as an ER translocation component and a network bridge between ER and mitochondrial-associated genes. The hypothesis that it organizes the entire conserved module is plausible from its network position but is not demonstrated by the co-abundance data.

#### ATL3

- **Related proteins** (co-abundance neighbors): ACADVL (0.81); STRING partners: RTN1 (0.865), RTN4 (0.826)
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: atlastin GTPase 3. This gene encodes a member of a family of dynamin-like, integral membrane GTPases. The encoded protein is required for the proper formation of the network of interconnected tubules of the endoplasmic reticulum. Mutations in this gene may be associated with hereditary sensory neuropathy type IF. Alternatively spliced transcript variants that encode distinct isoforms have been described. [provided b…
- **Diseases (Open Targets)**: neuropathy, hereditary sensory, type 1F (0.718); hereditary sensory and autonomic neuropathy type 1 (0.617); hereditary disease (0.193); Familial prostate cancer (0.112); prostate cancer (0.112)
- **Europe PMC papers**: 672
- **Why important**: ATL3 is a direct mechanistic anchor for ER morphology. It is part of the globally corrected tubular-ER and ER-organization terms (GO:CC endoplasmic reticulum tubular network; q_global = 0.00518) (GO:BP endoplasmic reticulum tubular network organization; q_global = 0.0398) (GO:BP endoplasmic reticulum organization; q_global = 0.0477), has STRING relationships with RTN1 and RTN4, and those reticulon genes recur in multiple hu.MAP complexes (hu.MAP huMAP3_08799.1) (hu.MAP huMAP3_05344.1) (hu.MAP huMAP3_10855.1) (hu.MAP huMAP3_09584.1) (hu.MAP huMAP3_10255.1) (hu.MAP huMAP3_14009.1). Its known role in ER membrane fusion and tubular-network formation gives biological specificity beyond a generic membrane annotation. It is associated with hereditary sensory neuropathy, while its literature volume is more modest than that of heavily studied housekeeping genes.
- **Conclusion**: Established evidence supports ATL3 as an ER-shaping component and explains the tubular-ER signal. It is a strong candidate for a structural driver of the module, but whether it drives the cross-tissue co-abundance pattern remains hypothetical.

#### TIMM50

- **Related proteins** (co-abundance neighbors): ACSL3 (0.88), SLC3A2 (0.86), MTHFD1L (0.85), UQCRC1 (0.82), EMC1 (0.82), SLC1A5 (0.81); STRING partners: ACO2 (0.755)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translocase of inner mitochondrial membrane 50. This gene encodes a subunit of the TIM23 inner mitochondrial membrane translocase complex. The encoded protein functions as the receptor subunit that recognizes the mitochondrial targeting signal, or presequence, on protein cargo that is destined for the mitochondrial inner membrane and matrix. This protein may also play a role in maintaining the membrane permeability barrier, and knockdown of thi…
- **Diseases (Open Targets)**: 3-methylglutaconic aciduria type 9 (0.773); neurodegenerative disease (0.519); Mitochondrial encephalopathy (0.425); hereditary disease (0.415); Epileptic encephalopathy (0.370)
- **Europe PMC papers**: 442
- **Why important**: TIMM50 connects the ER-associated portion of the network to mitochondrial protein import and apoptosis-related mitochondrial membrane control. It has high network connectivity, links ACSL3, SLC3A2, MTHFD1L, UQCRC1, EMC1, and SLC1A5, and is represented in primary membrane and transport terms (5 globally significant GO/KEGG terms, q_global 1.26e-06–0.0232; see the table). STRING links it to ACO2, while its annotated function places it in the TIM23 inner-membrane translocase. It is detected in both tissues, has a mitochondrial disease association, and has established but comparatively focused literature support.
- **Conclusion**: Established evidence supports TIMM50 as a mitochondrial import and membrane-integrity factor. Its position makes it a credible bridge between organelle proteostasis and mitochondrial function, but the module does not prove that TIMM50 mediates ER–mitochondrial coordination.

#### PNPT1

- **Related proteins** (co-abundance neighbors): TMEM214 (0.92), SUPV3L1 (0.88), GFM1 (0.85), ALDH18A1 (0.85), SEC63 (0.82); STRING partners: GFM1 (0.842), SUPV3L1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: polyribonucleotide nucleotidyltransferase 1. The protein encoded by this gene belongs to the evolutionary conserved polynucleotide phosphorylase family comprised of phosphate dependent 3'-to-5' exoribonucleases implicated in RNA processing and degradation. This enzyme is predominantly localized in the mitochondrial intermembrane space and is involved in import of RNA to mitochondria. Mutations in this gene have been associated with combined …
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 13 (0.807); autosomal recessive nonsyndromic hearing loss 70 (0.740); spinocerebellar ataxia type 25 (0.709); deafness (0.676); hearing loss, autosomal recessive (0.634)
- **Europe PMC papers**: 839
- **Why important**: PNPT1 links the ER-associated network to mitochondrial RNA metabolism. It connects TMEM214, SUPV3L1, GFM1, ALDH18A1, and SEC63, participates in the hu.MAP mitochondrial-associated complex (hu.MAP huMAP3_13468.1), and has strong STRING relationships with SUPV3L1 and GFM1. Its annotated function in mitochondrial RNA processing and degradation has direct disease relevance through combined oxidative-phosphorylation deficiency and inherited hearing loss. It is broadly detected in both tissues and has a substantial disease and literature record.
- **Conclusion**: Established evidence supports PNPT1 as a mitochondrial RNA-processing factor and as part of a known mitochondrial complex. Its network position supports a hypothesis of coordination between mitochondrial gene-expression quality control and ER membrane processes, but does not establish such coordination mechanistically.

#### SLC3A2

- **Related proteins** (co-abundance neighbors): TIMM50 (0.86), SLC1A5 (0.86), TMPO (0.84), PIGS (0.81), TMEM214 (0.81); STRING partners: SLC1A5 (0.894)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 3 member 2. This gene is a member of the solute carrier family and encodes a cell surface, transmembrane protein. The protein exists as the heavy chain of a heterodimer, covalently bound through di-sulfide bonds to one of several possible light chains. The encoded transporter plays a role in regulation of intracellular calcium levels and transports L-type amino acids. Alternatively spliced transcript variants…
- **Diseases (Open Targets)**: sensorineural hearing loss disorder (0.370); neurodegenerative disease (0.324); neoplasm (0.117); breast cancer (0.113); breast carcinoma (0.110)
- **Europe PMC papers**: 6815
- **Why important**: SLC3A2 is a membrane transporter component and a prominent link to the amino-acid transport signal (GO:BP transmembrane transport; q_global = 0.0232) (GO:BP amino acid transmembrane transport; q_global = 0.0235). It is connected to SLC1A5 by a strong STRING relationship and is also linked within the module to TIMM50, TMPO, PIGS, and TMEM214. Its known role as a heavy chain of heteromeric amino-acid transporters provides a functional route from membrane organization to nutrient supply. It is broadly expressed, with cell-type enhancement in several epithelial and trophoblast populations, and has a large literature base with transporter, disease, and cancer associations.
- **Conclusion**: Established evidence supports SLC3A2 as a cell-surface transporter component involved in amino-acid handling and membrane biology. It may connect nutrient availability to organelle maintenance in the module, but that metabolic coupling is a hypothesis rather than a demonstrated causal role.

## Module 1

**Tissue pair**: cervix_uterine and lung  
**Genes (24)**: ACLY, HSPA5, MTHFD1, CHD4, DAZAP1, TUFM, G6PD, HIBCH, HYOU1, MKI67, PKM, LMNB1, MATR3, MAT2A, MTA2, NKRF, NUCB1, PRKDC, RBBP7, SEH1L, SMARCC2, TKT, TRAP1, XRCC6

### Function

No GO/KEGG term passed global correction, so the module does not support a formally significant pathway assignment from the primary enrichment analysis. The most coherent interpretation is a composite cellular-maintenance program linking chromatin regulation, DNA repair, stress handling, and central carbon metabolism. The chromatin arm is supported by the coordinated presence of CHD4, MTA2, RBBP7 and SMARCC2, together with STRING evidence for NuRD-, CHD-type and SWI/SNF-related complexes (STRING COMPARTMENTS SWI/SNF superfamily-type complex; within-query FDR = 0.0275), (STRING COMPARTMENTS CHD-type complex; within-query FDR = 0.028), (STRING Component NuRD complex; within-query FDR = 0.0484), (STRING Component SWI/SNF superfamily-type complex; within-query FDR = 0.0484) and hu.MAP complexes (hu.MAP huMAP3_09499.1) (hu.MAP huMAP3_10472.1) (hu.MAP huMAP3_15128.1). The metabolic arm includes ACLY, G6PD, TKT, PKM and MTHFD1, with STRING-supported links among ACLY, G6PD, TKT and PKM. PRKDC and XRCC6 provide a DNA double-strand-break-repair connection, while HSPA5, HYOU1 and TRAP1 support proteostasis and cellular-stress biology. These are integrated functional clues rather than globally significant GO/KEGG enrichment. The module is therefore best viewed as a conserved, mixed intracellular program rather than a specific tissue pathway.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only NUCB1 is annotated as secreted to blood, and HSPA5 and HYOU1 have intracellular or membrane secretome annotations. Most genes are intracellular, broadly expressed and associated with nuclear, cytosolic, mitochondrial or organellar functions. HPA indicates low tissue specificity for most genes, with several tissue-enhanced or tissue-enriched signals involving bone marrow, lymphoid tissue, liver, skeletal muscle and tongue. Single-cell annotations are frequently cell-type enhanced, especially for erythrocyte progenitors, neutrophil-lineage cells and epithelial or reproductive cell types, but overall blood-cell specificity is low. TKT and G6PD show particularly notable myeloid or neutrophil-related HPA patterns, and LMNB1 and MKI67 show bone-marrow or lymphoid associations. Protein detection is broadly present in both cervix and lung. Thus, the shared signal is more consistent with broadly expressed cellular machinery, potentially influenced by shared cell-state or cellular-composition effects, than with a secreted tissue-specific program. A blood or proliferative-cell contribution remains plausible but is not established by these data.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides strong, internally coherent evidence for several relationships. CHD4–MTA2 and CHD4–RBBP7 are strongly supported, with CHD4 also linked to SMARCC2, matching chromatin-remodeling and NuRD-related interpretation (STRING COMPARTMENTS SWI/SNF superfamily-type complex; within-query FDR = 0.0275), (STRING COMPARTMENTS CHD-type complex; within-query FDR = 0.028), (STRING Component NuRD complex; within-query FDR = 0.0484), (STRING Component SWI/SNF superfamily-type complex; within-query FDR = 0.0484). PRKDC–XRCC6 supports the DNA-dependent protein kinase and non-homologous-end-joining axis. HSPA5–HYOU1 and HSPA5–TRAP1 support a chaperone and stress-response connection. ACLY–G6PD, ACLY–MTHFD1, G6PD–PKM, G6PD–TKT and PKM–TKT support a metabolic subnetwork involving glycolysis, the pentose-phosphate pathway, acetyl-CoA production and one-carbon metabolism. hu.MAP independently places MTA2, CHD4 and RBBP7 together in several complexes (hu.MAP huMAP3_09499.1) (hu.MAP huMAP3_10472.1) (hu.MAP huMAP3_15128.1), MTHFD1 with PKM in multiple complexes (hu.MAP huMAP3_14154.1), (hu.MAP huMAP3_13695.1), (hu.MAP huMAP3_12823.1), and HSPA5 with HYOU1 (hu.MAP huMAP3_07455.1). These results show that parts of the module recapitulate known protein complexes and functional neighborhoods. They support biological coherence, but they do not demonstrate that all co-abundance edges are direct physical interactions or that the full module is one molecular complex.

**STRING interactions (score >= 0.7)**: 12 of 276 gene pairs: ACLY–G6PD (0.785); ACLY–MTHFD1 (0.723); CHD4–MTA2 (0.999); CHD4–RBBP7 (0.999); CHD4–SMARCC2 (0.775); G6PD–PKM (0.941); G6PD–TKT (0.91); HSPA5–HYOU1 (0.999); HSPA5–TRAP1 (0.787); MTA2–RBBP7 (0.999); PKM–TKT (0.951); PRKDC–XRCC6 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Ubl conjugation (FDR = 0.0019, 15 genes); Keyword Isopeptide bond (FDR = 0.0019, 14 genes); COMPARTMENTS Chromosome, telomeric region (FDR = 0.0058, 5 genes); COMPARTMENTS Intracellular organelle lumen (FDR = 0.0058, 19 genes); Component Chromosomal region (FDR = 0.026, 7 genes); COMPARTMENTS SWI/SNF superfamily-type complex (FDR = 0.0275, 4 genes); COMPARTMENTS CHD-type complex (FDR = 0.028, 3 genes); Keyword DNA-binding (FDR = 0.0302, 7 genes); TISSUES Lymphocytic leukemia cell (FDR = 0.0322, 8 genes); TISSUES Leukemia cell (FDR = 0.0336, 12 genes); Component Chromosome, telomeric region (FDR = 0.0484, 5 genes); Component Transcription regulator complex (FDR = 0.0484, 5 genes); Component NuRD complex (FDR = 0.0484, 3 genes); Component SWI/SNF superfamily-type complex (FDR = 0.0484, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09499.1 (MTA2, CHD4, RBBP7; 3/33); huMAP3_10472.1 (MTA2, CHD4, RBBP7; 3/36); huMAP3_15128.1 (MTA2, CHD4, RBBP7; 3/96); huMAP3_14154.1 (MTHFD1, PKM; 2/2); huMAP3_07455.1 (HSPA5, HYOU1; 2/4); huMAP3_13695.1 (MTHFD1, PKM; 2/4); huMAP3_12823.1 (MTHFD1, PKM; 2/7); huMAP3_03905.1 (MTA2, CHD4; 2/10); huMAP3_05579.1 (MTA2, CHD4; 2/11); huMAP3_08738.1 (MTA2, CHD4; 2/17); huMAP3_14442.1 (PKM, TRAP1; 2/57)

### Novelty

The module should not be called a wholly new molecular complex or a newly discovered pathway. Several of its strongest relationships are already represented in STRING and hu.MAP, particularly the CHD4–MTA2–RBBP7 chromatin group, the PRKDC–XRCC6 repair pair, the HSPA5–HYOU1 stress pair and the glycolytic or pentose-phosphate relationships. Nevertheless, the conserved co-abundance of these distinct functional arms across cervix and lung may be a novel systems-level observation, especially if this exact tissue-pair module and its coordinated expression pattern have not previously been reported. Absence of an edge from STRING or hu.MAP is not evidence of novelty, because those resources emphasize known physical or curated associations and may miss context-specific co-regulation. The defensible conclusion is therefore partial novelty at the module and tissue-combination level, not novelty of the individual genes, complexes or biochemical functions.

**Hypothesis.** Hypothesis: the module reflects a shared stress-adaptation and proliferative or reparative state in cells present in both cervix and lung. Increased demand for chromatin organization and transcriptional control could coordinate with DNA-damage surveillance, protein folding and mitochondrial or ER stress management, while glycolysis, the pentose-phosphate pathway, acetyl-CoA production and folate metabolism provide energy, reducing power and biosynthetic substrates. HPA patterns raise the possibility that variation in epithelial, myeloid, erythroid-progenitor or other shared cellular contributions helps generate the signal. This hypothesis predicts that the module will vary with cell composition, proliferation, oxidative or ER stress, and tissue injury. It is not established by the co-abundance data alone.

### Important genes

#### CHD4

- **Related proteins** (co-abundance neighbors): NKRF (0.80); STRING partners: MTA2 (0.999), RBBP7 (0.999), SMARCC2 (0.775)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_09499.1, huMAP3_10472.1, huMAP3_15128.1, huMAP3_03905.1, huMAP3_05579.1, huMAP3_08738.1
- **Function (MyGene.info)**: chromodomain helicase DNA binding protein 4. The product of this gene belongs to the SNF2/RAD54 helicase family. It represents the main component of the nucleosome remodeling and deacetylase complex and plays an important role in epigenetic transcriptional repression. Patients with dermatomyositis develop antibodies against this protein. Somatic mutations in this gene are associated with serous endometrial tumors. Alternative splicing result…
- **Diseases (Open Targets)**: Sifrim-Hitz-Weiss syndrome (0.810); neurodegenerative disease (0.551); hereditary disease (0.505); endometrial cancer (0.470); uterine carcinosarcoma (0.439)
- **Europe PMC papers**: 3617
- **Why important**: CHD4 is a central anchor of the chromatin-regulatory part of the module. It has STRING links to MTA2, RBBP7 and SMARCC2, appears with MTA2 and RBBP7 across several hu.MAP complexes (hu.MAP huMAP3_09499.1) (hu.MAP huMAP3_10472.1) (hu.MAP huMAP3_15128.1), and is included in the CHD-type, NuRD and SWI/SNF-related supplementary annotations (STRING COMPARTMENTS SWI/SNF superfamily-type complex; within-query FDR = 0.0275), (STRING COMPARTMENTS CHD-type complex; within-query FDR = 0.028), (STRING Component NuRD complex; within-query FDR = 0.0484), (STRING Component SWI/SNF superfamily-type complex; within-query FDR = 0.0484). Its established functions include nucleosome remodeling, epigenetic transcriptional repression and DNA repair. It has substantial literature support and disease associations including Sifrim-Hitz-Weiss syndrome and endometrial cancer. Its network position and independent complex evidence make it more informative than a generic housekeeping marker.
- **Conclusion**: Established evidence supports CHD4 as a core chromatin-remodeling and transcriptional-regulatory component of the module. A role in coordinating the module's stress or repair response is a hypothesis, not a demonstrated causal function here.

#### MTA2

- **Related proteins** (co-abundance neighbors): NKRF (0.82), MKI67 (0.81); STRING partners: CHD4 (0.999), RBBP7 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_09499.1, huMAP3_10472.1, huMAP3_15128.1, huMAP3_03905.1, huMAP3_05579.1, huMAP3_08738.1
- **Function (MyGene.info)**: metastasis associated 1 family member 2. This gene encodes a protein that has been identified as a component of NuRD, a nucleosome remodeling deacetylase complex identified in the nucleus of human cells. It shows a very broad expression pattern and is strongly expressed in many tissues. It may represent one member of a small gene family that encode different but related proteins involved either directly or indirectly in transcriptional r…
- **Diseases (Open Targets)**: neoplasm (0.108); gastric cancer (0.108); Alzheimer disease (0.102); hepatocellular carcinoma (0.100); non-small cell lung carcinoma (0.098)
- **Europe PMC papers**: 1603
- **Why important**: MTA2 is tightly connected to CHD4 and RBBP7 in STRING and is present in multiple hu.MAP complexes (hu.MAP huMAP3_09499.1) (hu.MAP huMAP3_10472.1) (hu.MAP huMAP3_15128.1), (hu.MAP huMAP3_03905.1) (hu.MAP huMAP3_05579.1) (hu.MAP huMAP3_08738.1). It is a recognized NuRD component with broad expression and established roles in chromatin organization, transcriptional repression and cell-fate regulation. It has substantial literature volume and reported associations with neoplasm and several other diseases. Its repeated agreement across network, STRING and complex evidence makes it a strong representative of the module's chromatin arm.
- **Conclusion**: Established evidence supports MTA2 as a component of a known chromatin-remodeling and transcriptional-repression machinery represented in this module. Its contribution to the shared cervix–lung co-abundance pattern remains inferential.

#### RBBP7

- **Related proteins** (co-abundance neighbors): MATR3 (0.86), SMARCC2 (0.82), ACLY (0.81); STRING partners: CHD4 (0.999), MTA2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_09499.1, huMAP3_10472.1, huMAP3_15128.1
- **Function (MyGene.info)**: RB binding protein 7, chromatin remodeling factor. This protein is a ubiquitously expressed nuclear protein and belongs to a highly conserved subfamily of WD-repeat proteins. It is found among several proteins that binds directly to retinoblastoma protein, which regulates cell proliferation. The encoded protein is found in many histone deacetylase complexes, including mSin3 co-repressor complex. It is also present in protein complexes involved in …
- **Diseases (Open Targets)**: neurodegenerative disease (0.501); viral infectious disease (0.462); melanoma (0.408); breast carcinoma (0.380); cancer (0.378)
- **Europe PMC papers**: 1508
- **Why important**: RBBP7 is part of the dense CHD4–MTA2–RBBP7 STRING relationship and occurs with those genes in several hu.MAP complexes (hu.MAP huMAP3_09499.1) (hu.MAP huMAP3_10472.1) (hu.MAP huMAP3_15128.1). It is a conserved nuclear chromatin-remodeling factor found in histone deacetylase and chromatin-assembly complexes, with established links to transcriptional regulation, cell growth and migration. Its network position is less connected than the principal module anchors, but its complex membership is unusually consistent. It also has substantial literature and disease associations including cancer and neurodegenerative disease.
- **Conclusion**: Established evidence supports RBBP7 as a structural or regulatory partner in the chromatin-complex signal. The data do not establish that RBBP7 drives the tissue-shared module or disease-related variation.

#### ACLY

- **Related proteins** (co-abundance neighbors): G6PD (0.84), MTHFD1 (0.82), MATR3 (0.81), TKT (0.81), RBBP7 (0.81), PRKDC (0.81), PKM (0.80), DAZAP1 (0.80); STRING partners: G6PD (0.785), MTHFD1 (0.723)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP citrate lyase. ATP citrate lyase is the primary enzyme responsible for the synthesis of cytosolic acetyl-CoA in many tissues. The enzyme is a tetramer (relative molecular weight approximately 440,000) of apparently identical subunits. It catalyzes the formation of acetyl-CoA and oxaloacetate from citrate and CoA with a concomitant hydrolysis of ATP to ADP and phosphate. The product, acetyl-CoA, serves several im…
- **Diseases (Open Targets)**: familial hypercholesterolemia (0.532); Hypercholesterolemia (0.532); atherosclerosis (0.470); inherited lipid metabolism disorder (0.467); cardiovascular disorder (0.449)
- **Europe PMC papers**: 7957
- **Why important**: ACLY has the strongest network connectivity in the module and links the metabolic genes G6PD, MTHFD1, TKT and PKM while also connecting to nuclear and structural components. It produces cytosolic acetyl-CoA for lipid and cholesterol biosynthesis and is supported by STRING relationships with G6PD and MTHFD1. It has extensive literature and disease associations involving hypercholesterolemia, familial hypercholesterolemia and atherosclerosis. Its position makes it a plausible bridge between metabolism and chromatin biology because acetyl-CoA can support biosynthetic and regulatory processes, although that bridge is not directly demonstrated here.
- **Conclusion**: Established evidence supports ACLY as a central metabolic connector in the module. Its proposed role in coupling metabolic state to chromatin regulation is a mechanistic hypothesis rather than a finding proven by this analysis.

#### HSPA5

- **Related proteins** (co-abundance neighbors): HYOU1 (0.83), PRKDC (0.81); STRING partners: HYOU1 (0.999), TRAP1 (0.787)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_07455.1
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 represents the proteostasis and ER-stress arm of the module. It is strongly linked to HYOU1 in STRING and is linked to TRAP1, while hu.MAP places HSPA5 and HYOU1 in a shared complex (hu.MAP huMAP3_07455.1). HSPA5 is an ER HSP70 chaperone and regulator of ER homeostasis, with established roles in protein folding, unfolded-protein responses and stress-associated signaling. It has extensive literature and disease associations including dengue disease, neurodegenerative disease and neoplasm. Its presence alongside HYOU1 and TRAP1 gives the stress interpretation a coherent protein-level basis.
- **Conclusion**: Established evidence supports HSPA5 as a proteostasis and ER-stress component of the module. A coordinated stress response linking HSPA5 to the chromatin and metabolic arms is plausible but remains a hypothesis.

#### G6PD

- **Related proteins** (co-abundance neighbors): ACLY (0.84), TKT (0.82); STRING partners: ACLY (0.785), PKM (0.941), TKT (0.91)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glucose-6-phosphate dehydrogenase. This gene encodes glucose-6-phosphate dehydrogenase. This protein is a cytosolic enzyme encoded by a housekeeping X-linked gene whose main function is to produce NADPH, a key electron donor in the defense against oxidizing agents and in reductive biosynthetic reactions. G6PD is remarkable for its genetic diversity. Many variants of G6PD, mostly produced from missense mutations, have been described…
- **Diseases (Open Targets)**: anemia, nonspherocytic hemolytic, due to G6PD deficiency (0.851); anemia (phenotype) (0.776); G6PD deficiency (0.686); hereditary disease (0.535); infection (0.488)
- **Europe PMC papers**: 16994
- **Why important**: G6PD is part of the compact metabolic subnetwork with ACLY, TKT and PKM, including strong STRING relationships with PKM and TKT. It is a housekeeping X-linked enzyme that generates NADPH through the pentose-phosphate pathway, supporting antioxidant defense and reductive biosynthesis. HPA shows enhancement in neutrophil-related cell types and immune-cell enhancement for eosinophils, making it relevant both to redox metabolism and possible cellular-composition effects. It has very extensive literature and established disease associations with G6PD deficiency and hemolytic anemia.
- **Conclusion**: Established evidence supports G6PD as a redox and pentose-phosphate component and as a possible marker of myeloid or granulocytic contribution. Its role as a driver of the shared tissue module, rather than a correlated metabolic or compositional marker, is unproven.

## Module 2

**Tissue pair**: cervix_uterine and lung  
**Genes (32)**: AIMP1, ATXN2L, BCLAF1, DYNC1I2, DDX24, DHX9, DNM1L, DBN1, EPS15L1, FAM120A, HNRNPR, METAP2, PPP1R12A, NBN, NOP56, URB1, PLRG1, PRRC2A, PRRC2C, PSME4, PUM1, RBM22, SEC16A, SEPTIN7, PSAT1, SHTN1, SUPT16H, SUPT5H, TMOD3, TRIO, USP15, ZC3HAV1

### Function

The strongest functional interpretation is RNA-centered antiviral and post-transcriptional regulation. (GO:BP positive regulation of RIG-I signaling pathway; q_global = 0.0132) is the only GO or KEGG term passing global correction and links PUM1, USP15, and ZC3HAV1 to positive regulation of RIG-I signaling. This provides specific primary evidence for an innate antiviral RNA-response component. The remaining annotations support a broader RNA-processing context: PUM1 regulates mRNA stability and translation, ZC3HAV1 promotes antiviral RNA degradation, USP15 is a deubiquitinase involved in signaling and protein stability, DHX9 is an RNA helicase with interferon-related functions, and multiple members are involved in splicing, RNA transport, translation, ribosome biogenesis, or stress-granule biology. The module therefore appears heterogeneous but coherent around RNA handling, antiviral signaling, and nuclear or cytoplasmic gene-expression control. (STRING HPO Grip strength measurement; within-query FDR = 0.0088) is supplementary only and suggests that several module genes may also reflect cytoskeletal or cell-type-associated biology; it does not establish a primary module function.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: HPA identifies only AIMP1 as secreted to blood, while the other genes are intracellular. Most genes have low tissue specificity, and protein detection is broadly retained in both cervix and lung, which is consistent with a broadly expressed cellular program rather than a tissue-exclusive program. The module is also not globally immune-cell specific, although selected genes show enrichment in neutrophils, neutrophil progenitors, monocytes, dendritic cells, natural killer cells, or related blood-cell populations. The bone-marrow enhancement of BCLAF1, ZC3HAV1, and USP15 and the neutrophil-associated signal for several members raise the possibility that variable immune-cell content contributes to the shared co-abundance pattern. However, the predominance of low tissue and low immune specificity, together with widespread intracellular localization, argues against interpreting the entire module as a simple blood-contamination signature. The module may instead combine a broadly expressed housekeeping-like RNA-processing program with contributions from shared immune or epithelial cell populations.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP positive regulation of RIG-I signaling pathway | 0.0132 | PUM1, USP15, ZC3HAV1 |

### STRING and hu.MAP

STRING provides only a small set of high-confidence pairwise links. The best-supported relationships are DHX9 with HNRNPR, PLRG1 with RBM22, SUPT16H with SUPT5H, and DDX24 with URB1. These links independently support RNA processing, transcriptional elongation, and ribosome-biogenesis components, but they do not connect the entire module into a single established STRING interaction network. hu.MAP provides stronger structural context. (hu.MAP huMAP3_08887.1) supports a PRRC2A–PRRC2C complex, while (hu.MAP huMAP3_10625.1), (hu.MAP huMAP3_00582.1) through (hu.MAP huMAP3_10659.1), and (hu.MAP huMAP3_05807.1) place combinations of PUM1, HNRNPR, FAM120A, and ZC3HAV1 within larger RNA-binding or RNA-regulatory assemblies. (hu.MAP huMAP3_06726.1) through (hu.MAP huMAP3_09945.1) consistently place PLRG1 and RBM22 in spliceosome-related complexes. (hu.MAP huMAP3_13164.1) connects PUM1 and ATXN2L, and (hu.MAP huMAP3_10762.1), (hu.MAP huMAP3_12918.1), and (hu.MAP huMAP3_12394.1) place SEC16A and EPS15L1 in trafficking and endocytic assemblies. Thus, known interactions support several functional neighborhoods rather than a single molecular complex. The co-abundance module may reflect coordinated abundance of multiple interacting RNA-processing, trafficking, stress-response, and cell-structure subsystems.

**STRING interactions (score >= 0.7)**: 4 of 496 gene pairs: DDX24–URB1 (0.77); DHX9–HNRNPR (0.909); PLRG1–RBM22 (0.999); SUPT16H–SUPT5H (0.998)
**STRING functional enrichment (supplementary, within-query FDR)**: HPO Grip strength measurement (FDR = 0.0088, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10625.1 (HNRNPR, PUM1, FAM120A; 3/57); huMAP3_08887.1 (PRRC2A, PRRC2C; 2/2); huMAP3_00582.1 (PUM1, FAM120A; 2/3); huMAP3_07846.1 (PUM1, FAM120A; 2/6); huMAP3_07225.1 (HNRNPR, FAM120A; 2/7); huMAP3_13164.1 (PUM1, ATXN2L; 2/10); huMAP3_09654.1 (HNRNPR, FAM120A; 2/13); huMAP3_09281.1 (HNRNPR, FAM120A; 2/14); huMAP3_07115.1 (PUM1, FAM120A; 2/15); huMAP3_09223.1 (PUM1, FAM120A; 2/15); huMAP3_10659.1 (HNRNPR, FAM120A; 2/28); huMAP3_06726.1 (PLRG1, RBM22; 2/37); huMAP3_08501.1 (PLRG1, RBM22; 2/47); huMAP3_09504.1 (PLRG1, RBM22; 2/51); huMAP3_09945.1 (PLRG1, RBM22; 2/61); huMAP3_10762.1 (SEC16A, EPS15L1; 2/62); huMAP3_12918.1 (SEC16A, EPS15L1; 2/62); huMAP3_05807.1 (ZC3HAV1, FAM120A; 2/81); huMAP3_12394.1 (SEC16A, EPS15L1; 2/98)

### Novelty

This module should not be described as a wholly new molecular complex or as a newly discovered antiviral pathway. Its component functions, several pairwise interactions, and many complex memberships are already represented in STRING, hu.MAP, and established gene annotations. The potentially novel observation is the conserved co-abundance pattern linking these genes across cervix and lung, particularly the combination of the globally supported RIG-I-related genes with spliceosomal, stress-granule, transcriptional, and trafficking genes. Absence of some module pairs from STRING or hu.MAP does not demonstrate novelty, because database coverage is incomplete and co-abundance is not equivalent to physical interaction. A defensible claim is therefore that the cross-tissue co-abundance organization may be novel or under-characterized, whereas the underlying biological functions and many molecular relationships are established. Replication in independent cohorts, adjustment for cell composition, and comparison with previously published cross-tissue modules would be needed to establish novelty.

**Hypothesis.** Hypothesis: the conserved module represents a cell-state program in which antiviral RNA sensing and RNA-quality control are coordinated with post-transcriptional gene regulation. In this model, ZC3HAV1 and DHX9 participate in recognition or processing of aberrant or viral-associated RNA, PUM1 and stress-granule-associated proteins regulate transcript fate and translation, USP15 tunes signaling-protein stability, and spliceosomal and transcriptional components maintain expression of the responding cell. The trafficking and cytoskeletal members may reflect the cellular remodeling or shared cell populations associated with this state rather than a direct antiviral complex. This is a mechanistic hypothesis, not a demonstrated causal pathway: the co-abundance data do not establish physical binding, directionality, activation, or tissue-specific causation.

### Important genes

#### ZC3HAV1

- **Related proteins** (co-abundance neighbors): URB1 (0.82), SEC16A (0.81), DDX24 (0.81), DHX9 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_05807.1
- **Function (MyGene.info)**: zinc finger CCCH-type containing, antiviral 1. This gene encodes a CCCH-type zinc finger protein. This antiviral protein inhibits viral replication by recruiting cellular RNA degradation machineries to degrade viral mRNAs. The encoded protein plays an important role in the innate immune response against multiple DNA and RNA viruses, including Ebola virus, HIV and SARS-CoV-2 (which causes COVID-19). [provided by RefSeq, Sep 2021].
- **Diseases (Open Targets)**: cancer (0.549); hypothyroidism (0.429); neurodegenerative disease (0.358); autoimmune disease (0.308); Hashimoto thyroiditis (0.306)
- **Europe PMC papers**: 979
- **Why important**: ZC3HAV1 is one of the genes in the sole globally corrected term (GO:BP positive regulation of RIG-I signaling pathway; q_global = 0.0132), has a direct antiviral RNA-degradation function, and occupies a connecting position between the antiviral signal and RNA-helicase or ribosome-related neighbors. Its bone-marrow and multiple immune or endometrial cell-type enhancements make it relevant to possible immune-cell contributions. Its disease and literature record also directly includes viral infection and innate immune biology.
- **Conclusion**: Established evidence supports ZC3HAV1 as the clearest antiviral effector in the module. It is plausible, but not proven, that its co-abundance helps define the shared antiviral RNA-response state.

#### PUM1

- **Related proteins** (co-abundance neighbors): DDX24 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_00582.1, huMAP3_07846.1, huMAP3_13164.1, huMAP3_07115.1, huMAP3_09223.1
- **Function (MyGene.info)**: pumilio RNA binding family member 1. This gene encodes a member of the PUF family, evolutionarily conserved RNA-binding proteins related to the Pumilio proteins of Drosophila and the fem-3 mRNA binding factor proteins of C. elegans. The encoded protein contains a sequence-specific RNA binding domain comprised of eight repeats and N- and C-terminal flanking regions, and serves as a translational regulator of specific mRNAs by binding …
- **Diseases (Open Targets)**: spinocerebellar ataxia 47 (0.751); neurodevelopmental disorder with motor abnormalities, seizures, and facial dysmorphism (0.676); hereditary disease (0.504); neurodegenerative disease (0.487); hypertensive disorder (0.290)
- **Europe PMC papers**: 2316
- **Why important**: PUM1 is part of (GO:BP positive regulation of RIG-I signaling pathway; q_global = 0.0132) and is a sequence-specific RNA-binding and translational regulator. It appears repeatedly across hu.MAP assemblies (hu.MAP huMAP3_10625.1), (hu.MAP huMAP3_00582.1), (hu.MAP huMAP3_07846.1), (hu.MAP huMAP3_13164.1), (hu.MAP huMAP3_07115.1), and (hu.MAP huMAP3_09223.1), making it an important integrator of the RNA-regulatory neighborhood despite limited direct STRING support. Its established links to post-transcriptional control and neurological disease provide substantial biological context and literature depth.
- **Conclusion**: Established evidence supports PUM1 as a central RNA-fate regulator within the module. Its participation in antiviral signaling is supported through (GO:BP positive regulation of RIG-I signaling pathway; q_global = 0.0132) at the module annotation level, but a direct causal role for PUM1 in RIG-I activation remains a hypothesis.

#### USP15

- **Related proteins** (co-abundance neighbors): PLRG1 (0.85), SHTN1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin specific peptidase 15. This gene encodes a member of the ubiquitin specific protease (USP) family of deubiquitinating enzymes. USP enzymes play critical roles in ubiquitin-dependent processes through polyubiquitin chain disassembly and hydrolysis of ubiquitin-substrate bonds. The encoded protein associates with the COP9 signalosome, and also plays a role in transforming growth factor beta signalling through deubiquitina…
- **Diseases (Open Targets)**: neurodegenerative disease (0.548); alcohol drinking (0.294); post term pregnancy (0.272); smoking initiation (0.217); injury (0.162)
- **Europe PMC papers**: 1872
- **Why important**: USP15 is part of (GO:BP positive regulation of RIG-I signaling pathway; q_global = 0.0132) and encodes a deubiquitinase capable of regulating protein stability and transforming growth factor beta-related signaling. It connects the globally significant antiviral annotation to PLRG1 and to the supplementary cell-structure neighborhood. Its immune-cell and bone-marrow enhancement makes it useful for assessing whether the module includes an immune-state component, and it has a substantial disease literature.
- **Conclusion**: Established evidence supports USP15 as a signaling and protein-stability regulator associated with the module's antiviral annotation. Whether USP15 mechanistically drives the shared cervix–lung co-abundance pattern is unestablished.

#### DHX9

- **Related proteins** (co-abundance neighbors): SUPT16H (0.85), PPP1R12A (0.84), NOP56 (0.84), SEC16A (0.82), HNRNPR (0.81), ZC3HAV1 (0.81); STRING partners: HNRNPR (0.909)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 has a prominent network position and a high-confidence STRING relationship with HNRNPR. It is an RNA helicase involved in RNA and DNA–RNA unwinding, alternative splicing, transcriptional regulation, and interferon-related functions. Its large literature base and disease associations make it a biologically well-supported bridge between RNA metabolism and antiviral responses.
- **Conclusion**: Established evidence supports DHX9 as a plausible RNA-processing and antiviral-response hub in the module. The network supports coordination with neighboring genes, but does not prove that DHX9 is the causal upstream sensor.

#### PLRG1

- **Related proteins** (co-abundance neighbors): BCLAF1 (0.89), METAP2 (0.86), USP15 (0.85), PPP1R12A (0.83), RBM22 (0.82), ATXN2L (0.81); STRING partners: RBM22 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_06726.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: pleiotropic regulator 1. This gene encodes a core component of the cell division cycle 5-like (CDC5L) complex. The CDC5L complex is part of the spliceosome and is required for pre-mRNA splicing. The encoded protein plays a critical role in alternative splice site selection. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jan 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); Alzheimer disease (0.462); lysosomal storage disease (0.462); Parkinson disease (0.462); dengue disease (0.370)
- **Europe PMC papers**: 379
- **Why important**: PLRG1 has a strong network position, a high-confidence STRING relationship with RBM22, and repeated membership with RBM22 across spliceosome-related hu.MAP complexes (hu.MAP huMAP3_06726.1) through (hu.MAP huMAP3_09945.1). Its established role as a CDC5L-complex and pre-mRNA-splicing component provides a concrete explanation for the module's broad RNA-processing signal. Its disease associations and substantial literature support make it a strong representative of the spliceosomal neighborhood.
- **Conclusion**: Established evidence supports PLRG1 as a core spliceosomal organizer within the module. Its connection to the antiviral component is most securely interpreted as coordinated RNA processing rather than direct antiviral signaling.

## Module 3

**Tissue pair**: cervix_uterine and lung  
**Genes (8)**: ALB, HBA1, HBB, IGHM, IGKC, S100A8, S100A9, TF

### Function

The module most strongly represents a blood-associated oxygen-handling, extracellular detoxification, and inflammatory-defense signature. Globally corrected evidence supports oxygen binding (GO:MF oxygen binding; q_global = 0.004), antioxidant activity and cellular oxidant detoxification (GO:MF antioxidant activity; q_global = 0.0055)(GO:BP cellular oxidant detoxification; q_global = 0.0082), blood microparticles (GO:CC blood microparticle; q_global = 0.00902), fatty-acid binding (GO:MF fatty acid binding; q_global = 0.0125), responses to toxic substances (GO:BP cellular response to toxic substance; q_global = 0.0158)(GO:BP cellular detoxification; q_global = 0.0158)(GO:BP detoxification; q_global = 0.0175)(GO:BP response to toxic substance; q_global = 0.049), chronic inflammatory response (GO:BP chronic inflammatory response; q_global = 0.0333), nitric oxide transport (GO:BP nitric oxide transport; q_global = 0.0333), Toll-like-receptor binding and related signaling (GO:MF Toll-like receptor binding; q_global = 0.0333)(GO:BP autocrine signaling; q_global = 0.0333)(GO:MF Toll-like receptor 4 binding; q_global = 0.0333), icosanoid binding (GO:MF icosanoid binding; q_global = 0.0333)(GO:MF icosatetraenoic acid binding; q_global = 0.0333)(GO:MF arachidonate binding; q_global = 0.0333), neutrophil aggregation (GO:BP neutrophil aggregation; q_global = 0.0333), the calprotectin complex (GO:CC calprotectin complex; q_global = 0.0333), and bacterial defense (GO:BP defense response to bacterium; q_global = 0.0428). HBA1 and HBB represent the oxygen-related component, ALB and TF the extracellular carrier and detoxification component, and S100A8 with S100A9 the innate inflammatory component. The module is therefore better interpreted as a composite blood or inflammatory signal than as a single tissue-intrinsic pathway.

**Cell composition.** The composition strongly supports blood-derived material rather than a uniformly resident cervix or lung program. HPA identifies many secreted or immunoglobulin-related proteins and emphasizes blood-cell associations, especially neutrophils, with additional monocyte, plasmacytoid dendritic-cell, memory B-cell, naive B-cell, erythrocyte, plasma-cell, and hepatocyte signals. ALB and TF are liver-associated secreted proteins; HBA1 and HBB are erythrocyte markers; S100A8 and S100A9 are neutrophil and monocyte associated inflammatory proteins; and IGHM with IGKC indicates B-cell or immunoglobulin material. Only a minority of the module proteins are detected by HPA in each named tissue, whereas S100A8 and S100A9 are detected in the tissues. The shared co-abundance may therefore reflect blood contamination, vascular content, infiltrating immune cells, extracellular protein carryover, or shared cell types. It should not automatically be interpreted as coordinated expression by cervix and lung parenchymal cells.

**GO/KEGG enrichment**: 20 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF oxygen binding | 0.004 | ALB, HBA1, HBB |
| GO:MF antioxidant activity | 0.0055 | ALB, HBA1, HBB, S100A9 |
| GO:BP cellular oxidant detoxification | 0.0082 | ALB, HBA1, HBB, S100A9 |
| GO:CC blood microparticle | 0.00902 | ALB, HBA1, HBB, IGHM, TF |
| GO:MF fatty acid binding | 0.0125 | ALB, S100A8, S100A9 |
| GO:BP cellular response to toxic substance | 0.0158 | ALB, HBA1, HBB, S100A9 |
| GO:BP cellular detoxification | 0.0158 | ALB, HBA1, HBB, S100A9 |
| GO:BP detoxification | 0.0175 | ALB, HBA1, HBB, S100A9 |
| GO:BP chronic inflammatory response | 0.0333 | S100A8, S100A9 |
| GO:BP nitric oxide transport | 0.0333 | HBA1, HBB |
| GO:MF Toll-like receptor binding | 0.0333 | S100A8, S100A9 |
| GO:BP autocrine signaling | 0.0333 | S100A8, S100A9 |
| GO:MF Toll-like receptor 4 binding | 0.0333 | S100A8, S100A9 |
| GO:MF icosanoid binding | 0.0333 | S100A8, S100A9 |
| GO:MF icosatetraenoic acid binding | 0.0333 | S100A8, S100A9 |

### STRING and hu.MAP

STRING provides three high-confidence pairwise relationships: ALB with TF, HBA1 with HBB, and S100A8 with S100A9. These correspond to a plasma-protein association, the hemoglobin complex, and calprotectin, respectively. STRING tissue and extracellular-space enrichments and the proteomic-study associations are supplementary context, not global enrichment evidence. hu.MAP independently places ALB with TF in several large plasma or extracellular protein complexes, HBA1 with HBB in several hemoglobin-related complexes, and S100A8 with S100A9 in complexes associated with epithelial or inflammatory protein environments (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_04556.1) (hu.MAP huMAP3_06991.1) (hu.MAP huMAP3_10486.1) (hu.MAP huMAP3_13522.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09929.1). IGKC and IGHM have no listed STRING partners or hu.MAP complexes in this module. These resources validate recognizable substructures, but they also show that the module combines multiple familiar protein pools rather than constituting one established complete complex.

**STRING interactions (score >= 0.7)**: 3 of 28 gene pairs: ALB–TF (0.9); HBA1–HBB (0.999); S100A8–S100A9 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Left atrium (FDR = 0.00055, 4 genes); TISSUES Right atrium (FDR = 0.00055, 4 genes); TISSUES Left ventricle (FDR = 0.0009, 4 genes); COMPARTMENTS Hemoglobin complex (FDR = 0.0019, 3 genes); COMPARTMENTS Extracellular space (FDR = 0.0027, 6 genes); PMID (2022) Serum alpha-1-antitrypsin level in the severity prognosis of systemic lupus erythematosus patients: Systematic exploration of novel biomarker. (FDR = 0.0031, 5 genes); PMID (2023) Proteomic analysis of sialoliths from calcified, lipid and mixed groups as a source of potential biomarkers of deposit formation in the salivary glands. (FDR = 0.0035, 5 genes); PMID (2022) Paracrine Factors of Stressed Peripheral Blood Mononuclear Cells Activate Proangiogenic and Anti-Proteolytic Processes in Whole Blood Cells and Protect the Endothelial Barrier. (FDR = 0.0035, 4 genes); PMID (2022) Spatial intra-tumor heterogeneity is associated with survival of lung adenocarcinoma patients. (FDR = 0.0035, 4 genes); PMID (2021) The tryptic peptides of hemoglobin for diagnosis of type 2 diabetes mellitus using label-free and standard-free LC-ESI-DMRM. (FDR = 0.0035, 4 genes); PMID (2021) Effects of Cancer Presence and Therapy on the Platelet Proteome. (FDR = 0.0035, 4 genes); PMID (2019) Proteomics data of ovine mastitis associated with Mannheimia haemolytica. (FDR = 0.0035, 5 genes); PMID (2018) Standardization of a protocol for shotgun proteomic analysis of saliva. (FDR = 0.0035, 4 genes); PMID (2014) Quantitative gingival crevicular fluid proteome in health and periodontal disease using stable isotope chemistries and mass spectrometry. (FDR = 0.0035, 4 genes); PMID (2013) Proteomic analysis revealed the altered tear protein profile in a rabbit model of Sjoegrens syndrome-associated dry eye. (FDR = 0.0035, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (ALB, TF, HBB, HBA1; 4/64); huMAP3_04556.1 (HBB, HBA1; 2/3); huMAP3_06991.1 (HBB, HBA1; 2/4); huMAP3_10486.1 (HBB, HBA1; 2/4); huMAP3_13522.1 (HBB, HBA1; 2/10); huMAP3_07432.1 (ALB, TF; 2/18); huMAP3_07265.1 (ALB, TF; 2/20); huMAP3_09434.1 (ALB, TF; 2/33); huMAP3_08395.1 (ALB, TF; 2/43); huMAP3_09531.1 (ALB, TF; 2/47); huMAP3_10101.1 (ALB, TF; 2/49); huMAP3_09125.1 (S100A8, S100A9; 2/53); huMAP3_10678.1 (ALB, TF; 2/71); huMAP3_09929.1 (S100A8, S100A9; 2/75)

### Novelty

This should not be described as a new molecular complex or a newly discovered pathway. Its principal relationships and functional components are already established by STRING and hu.MAP, particularly the hemoglobin pair, the calprotectin pair, and the ALB-TF association. The potentially novel observation is the cross-tissue co-abundance pattern linking blood, erythrocyte, inflammatory, hepatic, and immunoglobulin signals in cervix and lung. That pattern may be useful as a sample-composition or systemic-inflammatory signature, but novelty remains provisional because shared blood content, cell-type mixture, and extracellular carryover provide simpler explanations. Tissue-cellular novelty would require cell-resolved or spatial validation and independent cohorts.

**Hypothesis.** Mechanistic hypothesis: variation in vascular or extravascular blood content, together with recruitment or activation of neutrophil and monocyte-lineage cells, produces the coordinated extracellular signal. Hemoglobin may contribute oxygen, nitric-oxide, and oxidant-related chemistry; ALB and TF may bind or transport metabolites, fatty acids, and iron; S100A8-S100A9 may promote Toll-like-receptor-linked inflammatory signaling and neutrophil aggregation; and immunoglobulin material may report B-cell or plasma-cell contribution. This is a hypothesis about the source and mechanism of co-abundance, not proof that the proteins act together within the same resident cells.

### Important genes

#### TF

- **Related proteins** (co-abundance neighbors): ALB (0.94), IGHM (0.86), IGKC (0.81), HBA1; HBA2 (0.81), S100A9 (0.80); STRING partners: ALB (0.9)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: transferrin. This gene encodes a glycoprotein with an approximate molecular weight of 76.5 kDa. It is thought to have been created as a result of an ancient gene duplication event that led to generation of homologous C and N-terminal domains each of which binds one ion of ferric iron. The function of this protein is to transport iron from the intestine, reticuloendothelial system, and liver parenchymal cells t…
- **Diseases (Open Targets)**: atransferrinemia (0.776); alcohol drinking (0.492); hemochromatosis type 1 (0.471); neurodegenerative disease (0.400); urolithiasis (0.329)
- **Europe PMC papers**: 143656
- **Why important**: TF is the strongest network bridge, connecting the albumin, immunoglobulin, hemoglobin, and S100A9 portions of the graph. It participates in blood-microparticle and bacterial-defense evidence (GO:CC blood microparticle; q_global = 0.00902)(GO:BP defense response to bacterium; q_global = 0.0428), is secreted to blood, and transports iron according to the supplied annotation. Its disease and literature annotations support importance for iron homeostasis and antibacterial humoral biology.
- **Conclusion**: Established: TF is a secreted iron-transport protein and a network bridge supported by ALB-TF STRING evidence and multiple hu.MAP associations. Hypothesis: TF may couple iron handling with extracellular antimicrobial conditions in this module, but co-abundance does not establish that it drives the inflammatory signal.

#### ALB

- **Related proteins** (co-abundance neighbors): TF (0.94), HBA1; HBA2 (0.92), IGKC (0.84); STRING partners: TF (0.9)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB is liver-enriched, secreted to blood, and connected to TF, hemoglobin-related material, and IGKC. It supports oxygen-binding, antioxidant, detoxification, fatty-acid-binding, toxic-substance, and blood-microparticle terms (8 globally significant GO/KEGG terms, q_global 0.004–0.0175; see the table)(GO:BP response to toxic substance; q_global = 0.049). Its annotation as a highly abundant blood protein and broad carrier of endogenous and exogenous molecules makes it especially informative for sample composition.
- **Conclusion**: Established: ALB is a circulating carrier and a known ALB-TF interaction partner, strongly supporting plasma contribution. Hypothesis: ALB may buffer or transport compounds associated with the oxidative and inflammatory state, but its presence does not demonstrate tissue-local synthesis in cervix or lung.

#### S100A9

- **Related proteins** (co-abundance neighbors): S100A8 (0.87), TF (0.80), IGKC (0.80); STRING partners: S100A8 (0.999)
- **HPA**: Group enriched; Cell type enriched; blood Group enriched; location Plasma membrane, Intermediate filaments, Cytosol; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: S100 calcium binding protein A9. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: inborn error of immunity (0.370); Sepsis (0.121); neoplasm (0.119); psoriasis (0.114); cancer (0.114)
- **Europe PMC papers**: 16393
- **Why important**: S100A9 is an inflammatory network connector linked to S100A8, TF, and IGKC, and HPA detects it in both named tissues. It is associated with neutrophils and classical monocytes, is secreted to blood, and contributes to inflammatory, Toll-like-receptor, icosanoid, neutrophil-aggregation, calprotectin, and bacterial-defense terms (GO:MF antioxidant activity; q_global = 0.0055)(GO:BP cellular oxidant detoxification; q_global = 0.0082)(16 globally significant GO/KEGG terms, q_global 0.0125–0.049; see the table). Its extensive disease and literature record supports its role as the most informative inflammatory marker in the module.
- **Conclusion**: Established: S100A9 is an inflammatory S100 protein, forms the known S100A8-S100A9 pair, and marks innate immune or myeloid-associated material. Hypothesis: it may indicate local or systemic inflammatory recruitment in both tissues, but the network cannot distinguish local activation from blood-derived carryover.

#### S100A8

- **Related proteins** (co-abundance neighbors): S100A9 (0.87); STRING partners: S100A9 (0.999)
- **HPA**: Tissue enhanced; Group enriched; blood Group enriched; location Intermediate filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: S100 calcium binding protein A8. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: inborn error of immunity (0.371); Sepsis (0.122); neoplasm (0.119); breast carcinoma (0.119); gastric cancer (0.119)
- **Europe PMC papers**: 18104
- **Why important**: S100A8 forms the calprotectin pair with S100A9 and provides a specific inflammatory interpretation, including chronic inflammation, Toll-like-receptor binding, icosanoid binding, neutrophil aggregation, calprotectin, and bacterial-defense terms (GO:MF fatty acid binding; q_global = 0.0125)(GO:BP chronic inflammatory response; q_global = 0.0333)(9 globally significant GO/KEGG terms, q_global 0.0333–0.0428; see the table). HPA associates it with neutrophils and classical monocytes and detects it in cervix, while STRING and hu.MAP support the inflammatory submodule.
- **Conclusion**: Established: S100A8 is a secreted myeloid-associated inflammatory protein and a validated component of calprotectin. Hypothesis: its presence may indicate neutrophil or monocyte recruitment into the cervix or lung environment, but it is not by itself evidence of tissue-resident expression.

#### HBB

- **Related proteins** (co-abundance neighbors): HBA1; HBA2 (0.92); STRING partners: HBA1 (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Group enriched; location None; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_04556.1, huMAP3_06991.1, huMAP3_10486.1, huMAP3_13522.1
- **Function (MyGene.info)**: hemoglobin subunit beta. The alpha (HBA) and beta (HBB) loci determine the structure of the 2 types of polypeptide chains in adult hemoglobin, Hb A. The normal adult hemoglobin tetramer consists of two alpha chains and two beta chains. Mutant beta globin causes sickle cell anemia. Absence of beta chain causes beta-zero-thalassemia. Reduced amounts of detectable beta globin causes beta-plus-thalassemia. The order of the ge…
- **Diseases (Open Targets)**: beta thalassemia (0.842); sickle cell disease (0.813); dominant beta-thalassemia (0.790); hemoglobin M disease (0.774); anemia (0.773)
- **Europe PMC papers**: 13411
- **Why important**: HBB identifies the erythrocyte and oxygen-handling component, pairs directly with HBA1 in STRING, and appears in hemoglobin-related hu.MAP complexes. It supports oxygen binding, oxidant detoxification, blood-microparticle, nitric-oxide transport, and toxic-substance terms (4 globally significant GO/KEGG terms, q_global 0.004–0.00902; see the table)(GO:BP cellular response to toxic substance; q_global = 0.0158) (GO:BP cellular detoxification; q_global = 0.0158) (GO:BP detoxification; q_global = 0.0175)(GO:BP nitric oxide transport; q_global = 0.0333)(GO:BP response to toxic substance; q_global = 0.049). Its disease associations with beta-thalassemia and sickle-cell disease are well established, and HPA assigns it to erythrocytes and detects it in lung.
- **Conclusion**: Established: HBB is a hemoglobin subunit and marker of erythrocyte-derived material, with a known HBA1 relationship. Hypothesis: hemoglobin-related chemistry may contribute to the oxidative and nitric-oxide signature, but HBB co-abundance more parsimoniously indicates blood content than a lung or cervix parenchymal mechanism.

## Module 4

**Tissue pair**: cervix_uterine and lung  
**Genes (25)**: AMPD2, FKBP4, FUS, GARS1, GMPS, HSPA8, IMPDH2, PCNA, PSMC4, PSMC2, PTBP1, GART, PAICS, UPF1, AARS1, EPRS1, KARS1, LARS1, SARS1, YARS1, CCT5, CCT3, CCT7, CCT8, TXNRD1

### Function

The module is best interpreted as a conserved intracellular biosynthetic and proteostasis program. Its strongest primary evidence is for nucleotide and ATP binding (9 globally significant GO/KEGG terms, q_global 3.26e-06–4.97e-05; see the table), catalytic and ligase activity (GO:MF ligase activity; q_global = 9.04e-05), (GO:MF ligase activity, forming carbon-oxygen bonds; q_global = 0.000123), (GO:MF anion binding; q_global = 0.000257), (GO:MF ion binding; q_global = 0.00286), (GO:MF small molecule binding; q_global = 0.00508), (GO:MF catalytic activity; q_global = 0.0138), aminoacyl-tRNA ligase activity and tRNA aminoacylation (7 globally significant GO/KEGG terms, q_global 0.000123–0.000159; see the table), (GO:MF catalytic activity, acting on a tRNA; q_global = 0.00289), (GO:BP tRNA metabolic process; q_global = 0.0123), (GO:MF catalytic activity, acting on RNA; q_global = 0.0429), and aminoacyl-tRNA biosynthesis (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 0.000159). A coordinated purine-nucleotide biosynthesis component is supported by AMPD2, GART, GMPS, IMPDH2 and PAICS in (GO:BP purine nucleoside monophosphate biosynthetic process; q_global = 0.00259), (GO:BP purine ribonucleoside monophosphate biosynthetic process; q_global = 0.00259), (GO:BP ribonucleoside monophosphate biosynthetic process; q_global = 0.0128), (GO:BP nucleotide biosynthetic process; q_global = 0.015) (GO:BP purine nucleoside monophosphate metabolic process; q_global = 0.0156) (GO:BP purine ribonucleoside monophosphate metabolic process; q_global = 0.0156), (GO:BP nucleoside monophosphate biosynthetic process; q_global = 0.0191), (GO:BP GMP biosynthetic process; q_global = 0.0211) and (GO:BP GMP metabolic process; q_global = 0.0488). A protein-folding component is supported by CCT3, CCT5, CCT7, CCT8 and HSPA8 in (GO:CC chaperonin-containing T-complex; q_global = 0.000228), (GO:CC protein folding chaperone complex; q_global = 0.00053), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.00126), (GO:MF protein folding chaperone; q_global = 0.0103) and (GO:MF unfolded protein binding; q_global = 0.0323). The CCT subunits also account for the globally corrected telomerase-RNA and Cajal-body localization terms (7 globally significant GO/KEGG terms, q_global 0.000228–0.000228; see the table), (4 globally significant GO/KEGG terms, q_global 0.000809–0.000809; see the table), (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 0.00367), (GO:BP regulation of telomere maintenance via telomerase; q_global = 0.00634), (GO:BP positive regulation of telomere maintenance via telomere lengthening; q_global = 0.00634), (GO:BP telomere maintenance; q_global = 0.00738) (GO:BP regulation of telomere maintenance via telomere lengthening; q_global = 0.01) (GO:BP telomere organization; q_global = 0.0101), (GO:BP regulation of telomere maintenance; q_global = 0.0156), (GO:BP RNA-templated DNA biosynthetic process; q_global = 0.0288), (GO:BP telomere maintenance via telomerase; q_global = 0.0288) and (GO:BP telomere maintenance via telomere lengthening; q_global = 0.038), although these terms should not be taken to mean that the entire module is a dedicated telomere module. Overall, the coherent interpretation is translation capacity and aminoacylation supported by nucleotide supply, chaperone-assisted folding, RNA handling and protein quality control. The broad ATP and nucleotide-binding signal partly reflects the abundance of these enzyme and chaperone classes, so it is less specific than the aminoacyl-tRNA, purine-biosynthesis and CCT-complex evidence.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the HPA summary reports only a small secreted component, and the genes described individually are overwhelmingly intracellular, with cytosolic, nucleoplasmic or complex-associated locations. It is also not convincingly a blood-cell module. Most genes have low immune-cell specificity, while AMPD2 is the main blood-cell-enriched exception and is associated with monocyte, dendritic-cell and neutrophil populations; it is not detected in cervix_uterine or lung by the supplied HPA evidence. The module is instead broadly expressed and housekeeping-like: most genes have low tissue specificity, and protein detection is reported for nearly all module genes in both cervix_uterine and lung. Cell-type-enhanced signals in reproductive, trophoblast, epithelial, cardiomyocyte and other cell types occur for subsets, but there is no single dominant shared cell type. Thus, shared abundance is more plausibly a conserved cellular program than a plasma carryover or a simple immune-infiltration signature, while sample composition and proliferative state could still influence its strength.

**GO/KEGG enrichment**: 68 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF ATP binding | 3.26e-06 | AARS1, CCT3, CCT5, CCT7, CCT8, EPRS1, FKBP4, GARS1, GART, GMPS, HSPA8, KARS1, LARS1, PAICS, PSMC2, PSMC4, SARS1, UPF1, YARS1 |
| GO:MF adenyl ribonucleotide binding | 3.44e-06 | AARS1, CCT3, CCT5, CCT7, CCT8, EPRS1, FKBP4, GARS1, GART, GMPS, HSPA8, KARS1, LARS1, PAICS, PSMC2, PSMC4, SARS1, UPF1, YARS1 |
| GO:MF nucleotide binding | 8.93e-06 | AARS1, CCT3, CCT5, CCT7, CCT8, EPRS1, FKBP4, GARS1, GART, GMPS, HSPA8, IMPDH2, KARS1, LARS1, PAICS, PSMC2, PSMC4, SARS1, TXNRD1, UPF1, YARS1 |
| GO:MF nucleoside phosphate binding | 1.2e-05 | AARS1, CCT3, CCT5, CCT7, CCT8, EPRS1, FKBP4, GARS1, GART, GMPS, HSPA8, IMPDH2, KARS1, LARS1, PAICS, PSMC2, PSMC4, SARS1, TXNRD1, UPF1, YARS1 |
| GO:MF adenyl nucleotide binding | 1.59e-05 | AARS1, CCT3, CCT5, CCT7, CCT8, EPRS1, FKBP4, GARS1, GART, GMPS, HSPA8, KARS1, LARS1, PAICS, PSMC2, PSMC4, SARS1, UPF1, YARS1 |
| GO:MF heterocyclic compound binding | 3.18e-05 | AARS1, CCT3, CCT5, CCT7, CCT8, EPRS1, FKBP4, GARS1, GART, GMPS, HSPA8, IMPDH2, KARS1, LARS1, PAICS, PSMC2, PSMC4, SARS1, TXNRD1, UPF1, YARS1 |
| GO:MF purine ribonucleoside triphosphate binding | 4.11e-05 | AARS1, CCT3, CCT5, CCT7, CCT8, EPRS1, FKBP4, GARS1, GART, GMPS, HSPA8, KARS1, LARS1, PAICS, PSMC2, PSMC4, SARS1, UPF1, YARS1 |
| GO:MF purine ribonucleotide binding | 4.27e-05 | AARS1, CCT3, CCT5, CCT7, CCT8, EPRS1, FKBP4, GARS1, GART, GMPS, HSPA8, KARS1, LARS1, PAICS, PSMC2, PSMC4, SARS1, UPF1, YARS1 |
| GO:MF ribonucleotide binding | 4.97e-05 | AARS1, CCT3, CCT5, CCT7, CCT8, EPRS1, FKBP4, GARS1, GART, GMPS, HSPA8, KARS1, LARS1, PAICS, PSMC2, PSMC4, SARS1, UPF1, YARS1 |
| GO:MF ligase activity | 9.04e-05 | AARS1, EPRS1, GARS1, GART, GMPS, KARS1, LARS1, PAICS, SARS1, YARS1 |
| GO:MF aminoacyl-tRNA ligase activity | 0.000123 | AARS1, EPRS1, GARS1, KARS1, LARS1, SARS1, YARS1 |
| GO:BP tRNA aminoacylation for protein translation | 0.000123 | AARS1, EPRS1, GARS1, KARS1, LARS1, SARS1, YARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 0.000123 | AARS1, EPRS1, GARS1, KARS1, LARS1, SARS1, YARS1 |
| GO:MF purine nucleotide binding | 0.000153 | AARS1, CCT3, CCT5, CCT7, CCT8, EPRS1, FKBP4, GARS1, GART, GMPS, HSPA8, KARS1, LARS1, PAICS, PSMC2, PSMC4, SARS1, UPF1, YARS1 |
| GO:BP amino acid activation | 0.000159 | AARS1, EPRS1, GARS1, KARS1, LARS1, SARS1, YARS1 |

### STRING and hu.MAP

STRING independently supports the same architecture through supplementary enrichment for ATP binding, nucleotide binding, ligase activity, aminoacyl-tRNA ligase activity, aminoacyl-tRNA synthetase, aminoacyl-tRNA biosynthesis and ATP-dependent protein folding (15 supplementary STRING terms; within-query FDR 4.75e-07–7.13e-05). The interaction map contains a known aminoacyl-tRNA synthetase neighborhood centered on AARS1, EPRS1, GARS1, KARS1, LARS1, SARS1 and YARS1, a purine-biosynthesis neighborhood involving AMPD2, GART, GMPS, IMPDH2 and PAICS, and a CCT-HSPA8 chaperone neighborhood involving CCT3, CCT5, CCT7, CCT8 and HSPA8. The proteasome ATPases PSMC2 and PSMC4, RNA-processing proteins such as FUS, PTBP1 and UPF1, and redox or protein-folding components provide additional links. hu.MAP independently identifies repeated CCT-containing complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1), (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), an aminoacyl-tRNA synthetase complex containing EPRS1, KARS1 and LARS1 (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), synthetase-associated complexes containing AARS1, GARS1 and YARS1 (hu.MAP huMAP3_14442.1), (hu.MAP huMAP3_04783.1) (hu.MAP huMAP3_11534.1) (hu.MAP huMAP3_10302.1) (hu.MAP huMAP3_10115.1), and proteasome complexes containing PSMC2 and PSMC4 (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). These are established relationships rather than newly demonstrated physical interactions. Their recurrence indicates that the co-abundance network captures several real cellular assemblies and pathway neighborhoods, while also showing that the module is a composite functional program rather than one single complex.

**STRING interactions (score >= 0.7)**: 47 of 300 gene pairs: AARS1–EPRS1 (0.976); AARS1–GARS1 (0.983); AARS1–KARS1 (0.992); AARS1–LARS1 (0.968); AARS1–SARS1 (0.881); AARS1–YARS1 (0.996); AMPD2–GMPS (0.722); AMPD2–IMPDH2 (0.966); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT3–HSPA8 (0.88); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT5–HSPA8 (0.948); CCT7–CCT8 (0.999); CCT7–HSPA8 (0.922); CCT7–IMPDH2 (0.758); CCT8–HSPA8 (0.905); CCT8–PSMC2 (0.733); EPRS1–GARS1 (0.973); EPRS1–GART (0.752); EPRS1–GMPS (0.912); EPRS1–KARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–SARS1 (0.86); EPRS1–YARS1 (0.999); FKBP4–HSPA8 (0.942); FUS–PTBP1 (0.852); GARS1–KARS1 (0.915); GARS1–LARS1 (0.895); GARS1–SARS1 (0.975); GARS1–YARS1 (0.989); GART–GMPS (0.937); GART–IMPDH2 (0.811); GART–PAICS (0.999); GMPS–IMPDH2 (0.998); GMPS–KARS1 (0.835); GMPS–PAICS (0.85); IMPDH2–PAICS (0.744); KARS1–LARS1 (0.999); KARS1–SARS1 (0.882); KARS1–YARS1 (0.988); LARS1–SARS1 (0.933); LARS1–YARS1 (0.98); PSMC2–PSMC4 (0.999); SARS1–YARS1 (0.941)
**STRING functional enrichment (supplementary, within-query FDR)**: Function ATP binding (FDR = 4.75e-07, 19 genes); Function Nucleotide binding (FDR = 6.55e-07, 21 genes); Keyword ATP-binding (FDR = 1.03e-06, 18 genes); Keyword Ligase (FDR = 3.11e-06, 10 genes); TISSUES Lymphoblast (FDR = 3.47e-06, 11 genes); Function Ligase activity (FDR = 4.44e-06, 10 genes); Function Anion binding (FDR = 4.44e-06, 20 genes); Function aminoacyl-tRNA ligase activity (FDR = 9.55e-06, 7 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 1.21e-05, 7 genes); Function Heterocyclic compound binding (FDR = 4.06e-05, 24 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 4.33e-05, 7 genes); TISSUES Embryonic structure (FDR = 5.05e-05, 20 genes); Function Organic cyclic compound binding (FDR = 5.29e-05, 24 genes); Function Ion binding (FDR = 6.16e-05, 23 genes); Function ATP-dependent protein folding chaperone (FDR = 7.13e-05, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14442.1 (GARS1, AARS1, GMPS, YARS1; 4/57); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_02637.1 (EPRS1, KARS1, LARS1; 3/14); huMAP3_13688.1 (EPRS1, KARS1, LARS1; 3/14); huMAP3_04783.1 (AARS1, YARS1; 2/4); huMAP3_11534.1 (GARS1, AARS1; 2/5); huMAP3_10302.1 (AARS1, YARS1; 2/9); huMAP3_10115.1 (AARS1, YARS1; 2/14); huMAP3_05064.1 (PSMC2, PSMC4; 2/31); huMAP3_09656.1 (PSMC2, PSMC4; 2/64); huMAP3_13725.1 (PSMC2, PSMC4; 2/69)

### Novelty

The module should not be called a wholly new molecular pathway. Most of its central relationships and assemblies are already represented in STRING and hu.MAP, especially the CCT chaperonin, aminoacyl-tRNA synthetase, purine-biosynthesis and proteasome components. Absence of some individual genes from a particular hu.MAP complex or absence of a STRING edge is not evidence of novelty, because those resources represent different interaction types and have incomplete coverage. The potentially novel finding is the conserved co-abundance configuration shared by cervix_uterine and lung: these established intracellular programs appear together across the two tissues, with a network that links translation charging, purine supply, chaperone folding, RNA surveillance and protein degradation. That cross-tissue abundance pattern is a systems-level observation, but it requires replication, adjustment for cell composition, disease state, proliferation and technical covariates before it can be considered tissue-specific biology. The strongest defensible conclusion is therefore a potentially novel cross-tissue module organization built from largely known biology, not discovery of new gene functions or new physical complexes.

**Hypothesis.** Hypothesis: in both cervix_uterine and lung, a shared demand for protein production and renewal coordinately raises aminoacyl-tRNA charging, purine-nucleotide production, ATP-dependent folding and quality control. Aminoacyl-tRNA synthetases may increase charged-tRNA availability, while GART, GMPS, IMPDH2, PAICS and AMPD2 help maintain nucleotide pools. The CCT chaperonin and HSPA8 may fold newly synthesized proteins, with PSMC2 and PSMC4 contributing to removal of damaged or misassembled proteins. RNA-processing factors and UPF1 may couple this state to transcript maturation and surveillance. The CCT-associated telomerase and Cajal-body annotations suggest a possible connection to proliferative or nuclear RNA-management demands, but the co-abundance data do not establish telomerase activity, causal regulation, or a disease mechanism. A useful test would be to determine whether module activity covaries with translation, nucleotide pools, proteostasis and proliferation within purified epithelial and stromal cell populations from both tissues.

### Important genes

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT5 (0.90), CCT8 (0.90), AARS1 (0.86), HSPA8 (0.86), GART (0.86), PSMC2 (0.85), KARS1 (0.85), CCT7 (0.81); STRING partners: CCT5 (0.999), CCT7 (0.999), CCT8 (0.999), HSPA8 (0.88)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a central member of the CCT chaperonin cluster, with strong module connectivity and repeated membership in the hu.MAP CCT complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1), (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It participates in the globally corrected chaperonin-containing T-complex, protein-folding, Cajal-body and telomerase-RNA localization terms (8 globally significant GO/KEGG terms, q_global 0.000228–0.000228; see the table), (5 globally significant GO/KEGG terms, q_global 0.00053–0.000809; see the table), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.00126), (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 0.00367), (GO:BP regulation of telomere maintenance via telomerase; q_global = 0.00634), (GO:BP positive regulation of telomere maintenance via telomere lengthening; q_global = 0.00634), (4 globally significant GO/KEGG terms, q_global 0.00738–0.0103; see the table), (GO:BP regulation of telomere maintenance; q_global = 0.0156), (4 globally significant GO/KEGG terms, q_global 0.0288–0.038; see the table). Its substantial literature supports a well-established chaperone role rather than a speculative annotation.
- **Conclusion**: Established evidence supports CCT3 as a structural and functional reporter of the module’s ATP-dependent protein-folding arm. It is a plausible marker of the module, but the supplied evidence does not show that CCT3 initiates the cross-tissue program or specifically regulates telomerase in these tissues.

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT3 (0.90), HSPA8 (0.90), KARS1 (0.88), AARS1 (0.88), GART (0.87), CCT7 (0.87), YARS1 (0.81), LARS1 (0.80); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999), HSPA8 (0.948)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is highly connected within the module and is repeatedly represented in STRING with the other CCT subunits and HSPA8, as well as in the hu.MAP CCT complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1), (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It has broad tissue expression, is detected in both tissues, and carries the same primary chaperonin, protein-folding and Cajal-body or telomerase-RNA annotations as the CCT cluster (8 globally significant GO/KEGG terms, q_global 0.000228–0.000228; see the table), (5 globally significant GO/KEGG terms, q_global 0.00053–0.000809; see the table), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.00126), (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 0.00367), (GO:BP regulation of telomere maintenance via telomerase; q_global = 0.00634), (GO:BP positive regulation of telomere maintenance via telomere lengthening; q_global = 0.00634), (4 globally significant GO/KEGG terms, q_global 0.00738–0.0103; see the table), (GO:BP regulation of telomere maintenance; q_global = 0.0156), (4 globally significant GO/KEGG terms, q_global 0.0288–0.038; see the table). Its disease associations and substantial literature make it biologically important beyond being a generic network node.
- **Conclusion**: Established evidence supports CCT5 as part of the conserved CCT folding machine represented in this module. Its co-abundance may report demand for folding and protein stabilization; it does not by itself establish a cervix_uterine- or lung-specific pathogenic role.

#### AARS1

- **Related proteins** (co-abundance neighbors): HSPA8 (0.90), GART (0.88), CCT5 (0.88), KARS1 (0.88), GARS1 (0.87), PAICS (0.87), CCT3 (0.86), IMPDH2 (0.85), PSMC2 (0.85); STRING partners: EPRS1 (0.976), GARS1 (0.983), KARS1 (0.992), LARS1 (0.968), SARS1 (0.881), YARS1 (0.996)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_14442.1, huMAP3_04783.1, huMAP3_11534.1, huMAP3_10302.1, huMAP3_10115.1
- **Function (MyGene.info)**: alanyl-tRNA synthetase 1. The human alanyl-tRNA synthetase (AARS) belongs to a family of tRNA synthases, of the class II enzymes.  Class II tRNA synthases evolved early in evolution and are highly conserved. This is reflected by the fact that 498 of the 968-residue polypeptide human AARS shares 41% identity witht the E.coli protein.  tRNA synthases are the enzymes that interpret the RNA code and attach specific aminoacids …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2N (0.762); developmental and epileptic encephalopathy, 29 (0.747); undetermined early-onset epileptic encephalopathy (0.678); trichothiodystrophy 8, nonphotosensitive (0.568); Charcot-Marie-Tooth disease type 2 (0.566)
- **Europe PMC papers**: 672
- **Why important**: AARS1 is among the more connected module genes and bridges the synthetase neighborhood with chaperone and purine-related genes. It is linked in STRING to several module aminoacyl-tRNA synthetases and appears in multiple hu.MAP complexes (hu.MAP huMAP3_14442.1), (hu.MAP huMAP3_04783.1) (hu.MAP huMAP3_11534.1) (hu.MAP huMAP3_10302.1) (hu.MAP huMAP3_10115.1). It is included in the globally corrected aminoacyl-tRNA and nucleotide-binding evidence (17 globally significant GO/KEGG terms, q_global 3.26e-06–0.000159; see the table), (GO:MF catalytic activity, acting on a tRNA; q_global = 0.00289), (GO:BP tRNA metabolic process; q_global = 0.0123), (GO:MF catalytic activity, acting on RNA; q_global = 0.0429), and its established function is charging alanine onto cognate tRNAs. Its disease associations and substantial literature provide strong external support for functional importance.
- **Conclusion**: Established evidence supports AARS1 as a core translation-capacity component and a connector between known synthetase assemblies. The module may reflect coordinated translational demand, but the data do not show that AARS1 is the causal driver of that demand or that its disease associations explain the shared tissue pattern.

#### KARS1

- **Related proteins** (co-abundance neighbors): CCT8 (0.90), CCT5 (0.88), AARS1 (0.88), EPRS1 (0.87), YARS1 (0.86), CCT3 (0.85), HSPA8 (0.83), PSMC4 (0.83); STRING partners: AARS1 (0.992), EPRS1 (0.999), GARS1 (0.915), GMPS (0.835), LARS1 (0.999), SARS1 (0.882), YARS1 (0.988)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: lysyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. Lysyl-tRNA synthetase is a homodimer localized to the cytoplasm which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Alternatively spliced transcript variants encoding different…
- **Diseases (Open Targets)**: leukoencephalopathy, progressive, infantile-onset, with or without deafness (0.753); deafness, congenital, and adult-onset progressive leukoencephalopathy (0.714); autosomal recessive nonsyndromic hearing loss 89 (0.685); Charcot-Marie-Tooth disease recessive intermediate B (0.670); deafness (0.534)
- **Europe PMC papers**: 232
- **Why important**: KARS1 has strong connectivity across the synthetase and CCT neighborhoods and is part of the hu.MAP synthetase complexes containing EPRS1 and LARS1 (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). It is included in the primary aminoacyl-tRNA biosynthesis and tRNA-aminoacylation evidence (8 globally significant GO/KEGG terms, q_global 9.04e-05–0.000159; see the table), (GO:MF catalytic activity, acting on a tRNA; q_global = 0.00289), (GO:BP tRNA metabolic process; q_global = 0.0123), (GO:MF catalytic activity, acting on RNA; q_global = 0.0429), while STRING supports its established relationships with multiple synthetases and chaperone-linked module genes (4 supplementary STRING terms; within-query FDR 4.75e-07–3.11e-06), (6 supplementary STRING terms; within-query FDR 4.44e-06–4.33e-05), (STRING Function Organic cyclic compound binding; within-query FDR = 5.29e-05) (STRING Function Ion binding; within-query FDR = 6.16e-05). It is detected in both tissues and has documented disease and autoimmune relevance.
- **Conclusion**: Established evidence supports KARS1 as a representative cytoplasmic tRNA-charging enzyme and an important bridge between translation and the broader module. A hypothesis is that its abundance tracks translational load or stress adaptation, but no causal tissue-specific mechanism is demonstrated.

#### GART

- **Related proteins** (co-abundance neighbors): AARS1 (0.88), HSPA8 (0.88), CCT5 (0.87), GARS1 (0.87), GMPS (0.86), CCT3 (0.86), PAICS (0.82), TXNRD1 (0.80); STRING partners: EPRS1 (0.752), GMPS (0.937), IMPDH2 (0.811), PAICS (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase. The protein encoded by this gene is a trifunctional polypeptide. It has phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase activity which is required for de novo purine biosynthesis. This enzyme is highly conserved in vertebrates. Alternative splicing of this gene results in two transcript variants encoding different isoforms.…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.606); mesothelioma (0.584); malignant pleural mesothelioma (0.557); adenocarcinoma (0.486); anaplastic lung carcinoma (0.462)
- **Europe PMC papers**: 1890
- **Why important**: GART connects the aminoacyl-tRNA and chaperone neighborhoods to the purine-biosynthesis cluster. Its STRING relationships with GMPS, IMPDH2 and PAICS and its inclusion in the globally corrected purine and GMP biosynthesis terms (GO:BP purine nucleoside monophosphate biosynthetic process; q_global = 0.00259) (GO:BP purine ribonucleoside monophosphate biosynthetic process; q_global = 0.00259) (GO:BP nucleobase-containing compound biosynthetic process; q_global = 0.00284), (GO:BP ribonucleoside monophosphate biosynthetic process; q_global = 0.0128), (GO:BP nucleotide biosynthetic process; q_global = 0.015) (GO:BP purine nucleoside monophosphate metabolic process; q_global = 0.0156) (GO:BP purine ribonucleoside monophosphate metabolic process; q_global = 0.0156), (GO:BP nucleoside monophosphate biosynthetic process; q_global = 0.0191), (GO:BP GMP biosynthetic process; q_global = 0.0211), (GO:BP GMP metabolic process; q_global = 0.0488) provide pathway-level support. GART is a trifunctional enzyme required for de novo purine synthesis, is detected in both tissues, and has extensive literature and disease associations including lung cancer relevance.
- **Conclusion**: Established evidence supports GART as a metabolic backbone of the module that can supply purine precursors needed for RNA, DNA and energy metabolism. Its connection to the translation and chaperone genes is a plausible systems-level coupling, but the module does not establish that purine synthesis is rate-limiting in either tissue.

## Module 5

**Tissue pair**: cervix_uterine and lung  
**Genes (28)**: PRMT5, CBS, COPB1, DCTN1, DDX5, DDX39B, EIF3L, PIGK, HNRNPH1, HNRNPF, HNRNPK, HSPH1, EIF4G1, IQGAP1, LAS1L, PDCD6IP, PSMD13, RBBP4, RBM39, RUVBL2, SF3B3, DARS1, IARS1, QARS1, SNRNP200, EFTUD2, VPS35, CSE1L

### Function

The module is best interpreted as a conserved nuclear RNA-processing and pre-mRNA-splicing module. The primary evidence is the globally corrected enrichment for RNA splicing and spliceosome processes (GO:BP RNA splicing, via transesterification reactions; q_global = 7.14e-05), (GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 7.14e-05), (GO:BP mRNA splicing, via spliceosome; q_global = 7.14e-05), (GO:CC catalytic step 2 spliceosome; q_global = 0.000188), (GO:CC spliceosomal complex; q_global = 0.000333), (GO:BP RNA splicing; q_global = 0.00126), (GO:BP regulation of RNA splicing; q_global = 0.00371), (GO:BP mRNA processing; q_global = 0.00436), (KEGG Spliceosome - Homo sapiens (human); q_global = 0.039), and (GO:BP RNA processing; q_global = 0.0485). The module also supports assembly and activity of protein–RNA complexes (GO:CC ribonucleoprotein complex; q_global = 0.00122), (GO:BP protein-RNA complex assembly; q_global = 0.049), gene expression (GO:BP gene expression; q_global = 0.0337), and a histone methyltransferase complex (GO:CC histone methyltransferase complex; q_global = 0.00929). Thus, its central function is spliceosome-associated RNA maturation, with linked contributions from RNA-protein complex assembly, translation-related machinery, chromatin regulation, and gene-expression control. The co-abundance pattern should be interpreted as coordinated abundance of a cellular machinery program, not as proof that every encoded protein directly binds every other member.

**Cell composition.** This is not primarily a plasma-protein, secreted-protein, or blood-cell module. HPA classifies nearly all members as having low tissue specificity, most as having low cell-type specificity, and nearly all as having low immune-cell specificity; only a small minority are secreted. Protein detection is concordant in cervix_uterine and lung for nearly all assessed members. The broad expression and nuclear or cytosolic localization of the principal genes favor a ubiquitous housekeeping-like RNA-processing program rather than a blood-contamination explanation. Some individual genes show enrichment in specialized cell types or tissues, including respiratory ciliated cells, esophageal apical cells, bone marrow, testis, and neutrophils, so cellular composition could modulate the signal, but the aggregate HPA evidence does not support a predominantly blood-cell or secreted-protein module.

**GO/KEGG enrichment**: 17 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA splicing, via transesterification reactions | 7.14e-05 | DDX39B, DDX5, EFTUD2, HNRNPF, HNRNPH1, HNRNPK, PRMT5, RBM39, SF3B3, SNRNP200 |
| GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile | 7.14e-05 | DDX39B, DDX5, EFTUD2, HNRNPF, HNRNPH1, HNRNPK, PRMT5, RBM39, SF3B3, SNRNP200 |
| GO:BP mRNA splicing, via spliceosome | 7.14e-05 | DDX39B, DDX5, EFTUD2, HNRNPF, HNRNPH1, HNRNPK, PRMT5, RBM39, SF3B3, SNRNP200 |
| GO:CC catalytic complex | 0.000184 | DARS1, DCTN1, DDX5, EFTUD2, HNRNPF, HNRNPH1, HNRNPK, IARS1, LAS1L, PIGK, PRMT5, PSMD13, QARS1, RBBP4, RUVBL2, SF3B3, SNRNP200 |
| GO:CC catalytic step 2 spliceosome | 0.000188 | DDX5, EFTUD2, HNRNPF, HNRNPH1, HNRNPK, SF3B3, SNRNP200 |
| GO:CC spliceosomal complex | 0.000333 | DDX39B, DDX5, EFTUD2, HNRNPF, HNRNPH1, HNRNPK, SF3B3, SNRNP200 |
| GO:CC protein-containing complex | 0.00115 | COPB1, DARS1, DCTN1, DDX39B, DDX5, EFTUD2, EIF3L, EIF4G1, HNRNPF, HNRNPH1, HNRNPK, HSPH1, IARS1, IQGAP1, LAS1L, PIGK, PRMT5, PSMD13, QARS1, RBBP4, RBM39, RUVBL2, SF3B3, SNRNP200, VPS35 |
| GO:CC ribonucleoprotein complex | 0.00122 | DDX39B, DDX5, EFTUD2, EIF3L, HNRNPF, HNRNPH1, HNRNPK, IQGAP1, RUVBL2, SF3B3, SNRNP200 |
| GO:BP RNA splicing | 0.00126 | DDX39B, DDX5, EFTUD2, HNRNPF, HNRNPH1, HNRNPK, PRMT5, RBM39, SF3B3, SNRNP200 |
| GO:BP regulation of RNA splicing | 0.00371 | DDX5, HNRNPF, HNRNPH1, HNRNPK, PRMT5, RBM39, SF3B3 |
| GO:BP mRNA processing | 0.00436 | DDX39B, DDX5, EFTUD2, HNRNPF, HNRNPH1, HNRNPK, PRMT5, RBM39, SF3B3, SNRNP200 |
| GO:CC histone methyltransferase complex | 0.00929 | LAS1L, PRMT5, RBBP4, RUVBL2 |
| GO:CC nuclear protein-containing complex | 0.0269 | DDX39B, DDX5, EFTUD2, HNRNPF, HNRNPH1, HNRNPK, LAS1L, PRMT5, RBBP4, RUVBL2, SF3B3, SNRNP200 |
| GO:BP gene expression | 0.0337 | DARS1, DDX39B, DDX5, EFTUD2, EIF3L, EIF4G1, HNRNPF, HNRNPH1, HNRNPK, HSPH1, IARS1, IQGAP1, LAS1L, PIGK, PRMT5, QARS1, RBBP4, RBM39, RUVBL2, SF3B3, SNRNP200, VPS35 |
| KEGG Spliceosome - Homo sapiens (human) | 0.039 | DDX39B, DDX5, EFTUD2, HNRNPK, SF3B3, SNRNP200 |

### STRING and hu.MAP

STRING independently supports a spliceosomal and ribonucleoprotein interpretation through the supplementary terms (STRING Component Ribonucleoprotein complex; within-query FDR = 1.85e-05), (STRING Keyword Spliceosome; within-query FDR = 3.03e-05), (STRING Keyword mRNA splicing; within-query FDR = 9.4e-05), (STRING COMPARTMENTS Spliceosomal complex; within-query FDR = 0.00012), (STRING COMPARTMENTS Catalytic step 2 spliceosome; within-query FDR = 0.00012), (STRING Component Spliceosomal complex; within-query FDR = 0.00012), (STRING Component Catalytic step 2 spliceosome; within-query FDR = 0.00012), (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.00014), (STRING RCTM Metabolism of RNA; within-query FDR = 0.0002), (STRING Process mRNA splicing, via spliceosome; within-query FDR = 0.00043), and (STRING Process RNA splicing; within-query FDR = 0.00043). High-confidence links connect DDX39B, DDX5, EFTUD2, HNRNPF, HNRNPH1, HNRNPK, RBM39, SF3B3, and SNRNP200, while a separate aminoacyl-tRNA synthetase cluster links DARS1, IARS1, and QARS1. The hu.MAP evidence identifies established complexes containing PRMT5, SNRNP200, EFTUD2, and SF3B3 (hu.MAP huMAP3_08980.1); DARS1, IARS1, and QARS1 (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1); HNRNPF, HNRNPH1, and HNRNPK (hu.MAP huMAP3_14523.1); SNRNP200 and EFTUD2 (hu.MAP huMAP3_00960.1), (hu.MAP huMAP3_07622.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), (hu.MAP huMAP3_09945.1); EIF4G1 and EIF3L (hu.MAP huMAP3_13175.1), (hu.MAP huMAP3_11246.1); and PRMT5 with SF3B3 (hu.MAP huMAP3_06511.1). These observations show that substantial portions of the module recapitulate known spliceosomal, heterogeneous nuclear ribonucleoprotein, translation, and aminoacyl-tRNA-synthetase relationships. They support biological coherence, but they do not establish that the complete co-abundance module is one physical complex.

**STRING interactions (score >= 0.7)**: 25 of 378 gene pairs: DARS1–IARS1 (0.996); DARS1–QARS1 (0.999); DDX39B–DDX5 (0.915); DDX39B–EFTUD2 (0.754); DDX39B–HNRNPF (0.736); DDX39B–HNRNPH1 (0.742); DDX39B–HNRNPK (0.808); DDX39B–RBM39 (0.922); DDX39B–SNRNP200 (0.709); DDX5–HNRNPF (0.807); DDX5–HNRNPH1 (0.96); DDX5–HNRNPK (0.935); DDX5–RBM39 (0.971); EFTUD2–RUVBL2 (0.793); EFTUD2–SF3B3 (0.999); EFTUD2–SNRNP200 (0.999); EIF3L–EIF4G1 (0.924); EIF4G1–VPS35 (0.899); HNRNPF–HNRNPH1 (0.994); HNRNPF–HNRNPK (0.971); HNRNPH1–HNRNPK (0.975); HNRNPK–SF3B3 (0.971); IARS1–QARS1 (0.999); LAS1L–RUVBL2 (0.906); SF3B3–SNRNP200 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Ribonucleoprotein complex (FDR = 1.85e-05, 13 genes); Keyword Spliceosome (FDR = 3.03e-05, 8 genes); Keyword mRNA splicing (FDR = 9.4e-05, 9 genes); COMPARTMENTS Spliceosomal complex (FDR = 0.00012, 8 genes); COMPARTMENTS Catalytic step 2 spliceosome (FDR = 0.00012, 7 genes); Component Spliceosomal complex (FDR = 0.00012, 8 genes); Component Protein-containing complex (FDR = 0.00012, 25 genes); Component Catalytic step 2 spliceosome (FDR = 0.00012, 7 genes); RCTM mRNA Splicing - Major Pathway (FDR = 0.00014, 9 genes); TISSUES Liver (FDR = 0.00017, 24 genes); TISSUES Lymphoblast (FDR = 0.00017, 10 genes); RCTM Metabolism of RNA (FDR = 0.0002, 13 genes); Process mRNA splicing, via spliceosome (FDR = 0.00043, 9 genes); Process RNA splicing (FDR = 0.00043, 10 genes); Component Catalytic complex (FDR = 0.00078, 14 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (PRMT5, SNRNP200, EFTUD2, SF3B3; 4/97); huMAP3_02637.1 (DARS1, IARS1, QARS1; 3/14); huMAP3_13688.1 (DARS1, IARS1, QARS1; 3/14); huMAP3_14523.1 (HNRNPH1, HNRNPF, HNRNPK; 3/33); huMAP3_07055.1 (HNRNPH1, HNRNPF; 2/3); huMAP3_06054.1 (HNRNPH1, HNRNPF; 2/4); huMAP3_11034.1 (HNRNPH1, HNRNPF; 2/5); huMAP3_00960.1 (SNRNP200, EFTUD2; 2/8); huMAP3_13511.1 (HNRNPH1, HNRNPF; 2/9); huMAP3_07622.1 (SNRNP200, EFTUD2; 2/9); huMAP3_13175.1 (EIF4G1, EIF3L; 2/20); huMAP3_11246.1 (EIF4G1, EIF3L; 2/24); huMAP3_08501.1 (SNRNP200, EFTUD2; 2/47); huMAP3_09504.1 (SNRNP200, EFTUD2; 2/51); huMAP3_09945.1 (SNRNP200, EFTUD2; 2/61); huMAP3_06511.1 (PRMT5, SF3B3; 2/79)

### Novelty

The module should not be described as a newly discovered molecular complex or as a wholly novel pathway. Its dominant signal is a well-established spliceosome and RNA-processing program, and many of its relationships are already represented in STRING and hu.MAP. A potentially novel aspect is the conserved co-abundance of this combination across cervix_uterine and lung, including the way spliceosomal, translation-associated, proteostasis, trafficking, and cytoskeletal genes are coordinated in these tissue groups. However, the supplied evidence does not compare this module with all prior tissue co-abundance studies or establish disease-specific causal novelty. Therefore, the defensible conclusion is that the module is a dataset-specific conserved co-abundance pattern built largely from known biology; novelty of the tissue-pair organization remains plausible but unproven. Lack of a STRING or hu.MAP record for some genes would not by itself demonstrate novelty.

**Hypothesis.** Mechanistic hypothesis: shared cellular demands in cervix_uterine and lung coordinate a nuclear RNA-processing program in which spliceosomal core components and RNA helicases maintain pre-mRNA maturation, while hnRNP proteins and RBM39 tune transcript selection and alternative splicing. PRMT5 and RBBP4 may connect RNA processing with chromatin and transcriptional regulation, whereas the aminoacyl-tRNA synthetase and translation-associated members may couple transcript maturation to protein-production capacity. The trafficking, proteostasis, and cytoskeletal genes may reflect downstream requirements of active, differentiated epithelial cells or shared cell-state composition rather than a single physical complex. This is a hypothesis generated from co-abundance and annotation evidence; it requires validation with transcript-level splicing measurements, perturbation experiments, and cell-composition-aware analyses.

### Important genes

#### DDX5

- **Related proteins** (co-abundance neighbors): IARS1 (0.87), RBM39 (0.86), EFTUD2 (0.85), EIF4G1 (0.84), HNRNPH1 (0.84), HSPH1 (0.83), EIF3L (0.82), HNRNPK (0.82), SF3B3 (0.81), DARS1 (0.80), COPB1 (0.80), SNRNP200 (0.80); STRING partners: DDX39B (0.915), HNRNPF (0.807), HNRNPH1 (0.96), HNRNPK (0.935), RBM39 (0.971)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 is the most network-central member in the supplied module and connects the principal spliceosomal and hnRNP groups with translation-associated and stress-related members. It is included in nearly all primary spliceosome and RNA-processing terms (GO:BP RNA splicing, via transesterification reactions; q_global = 7.14e-05), (GO:BP mRNA splicing, via spliceosome; q_global = 7.14e-05), (GO:CC catalytic step 2 spliceosome; q_global = 0.000188), (GO:CC spliceosomal complex; q_global = 0.000333), (GO:BP RNA splicing; q_global = 0.00126), (GO:BP regulation of RNA splicing; q_global = 0.00371), (GO:BP mRNA processing; q_global = 0.00436), (KEGG Spliceosome - Homo sapiens (human); q_global = 0.039), and (GO:BP RNA processing; q_global = 0.0485), and in all listed STRING supplementary categories. Its established DEAD-box helicase, splicing-regulator, transcriptional-coregulator, and small-noncoding-RNA functions make it a strong integrator of the module. It also has substantial literature volume and disease associations spanning infectious disease and cancer.
- **Conclusion**: Established evidence supports DDX5 as a central RNA-helicase and spliceosome-associated hub in this module. Its network position makes it a plausible coordinator of the co-abundance pattern, but co-abundance does not establish that DDX5 drives the module or causes the associated diseases.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.89), DDX5 (0.85), QARS1 (0.84), SF3B3 (0.81), DARS1 (0.81), RUVBL2 (0.80); STRING partners: DDX39B (0.754), RUVBL2 (0.793), SF3B3 (0.999), SNRNP200 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 is a core spliceosomal GTPase associated with spliceosomal assembly and conformational transitions. It appears in the primary splicing terms (GO:BP RNA splicing, via transesterification reactions; q_global = 7.14e-05), (GO:BP mRNA splicing, via spliceosome; q_global = 7.14e-05), (GO:CC catalytic step 2 spliceosome; q_global = 0.000188), (GO:CC spliceosomal complex; q_global = 0.000333), (GO:BP RNA splicing; q_global = 0.00126), (GO:BP mRNA processing; q_global = 0.00436), (KEGG Spliceosome - Homo sapiens (human); q_global = 0.039), and (GO:BP RNA processing; q_global = 0.0485), has strong STRING relationships with SF3B3 and SNRNP200, and is represented in several hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1), (hu.MAP huMAP3_00960.1), (hu.MAP huMAP3_07622.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), and (hu.MAP huMAP3_09945.1). Its disease association with mandibulofacial dysostosis with microcephaly provides evidence that disruption of this machinery can have organism-level consequences.
- **Conclusion**: Established evidence identifies EFTUD2 as a bona fide spliceosomal component and a major structural bridge within the module. The shared tissue signal is consistent with coordinated spliceosome demand, but it does not show that EFTUD2-specific variation explains the tissue-pair pattern.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.89), IARS1 (0.83), SF3B3 (0.83), EIF4G1 (0.81), HNRNPF (0.81), DDX5 (0.80); STRING partners: DDX39B (0.709), EFTUD2 (0.999), SF3B3 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is a U5 small nuclear ribonucleoprotein component and RNA helicase involved in spliceosome assembly and conformational remodeling. It contributes to the primary enrichment for spliceosome, RNA splicing, RNA processing, and protein–RNA complex assembly (GO:BP RNA splicing, via transesterification reactions; q_global = 7.14e-05), (GO:BP mRNA splicing, via spliceosome; q_global = 7.14e-05), (GO:CC catalytic step 2 spliceosome; q_global = 0.000188), (GO:CC spliceosomal complex; q_global = 0.000333), (GO:BP RNA splicing; q_global = 0.00126), (GO:BP mRNA processing; q_global = 0.00436), (KEGG Spliceosome - Homo sapiens (human); q_global = 0.039), (GO:BP RNA processing; q_global = 0.0485), and (GO:BP protein-RNA complex assembly; q_global = 0.049). Its strong links with EFTUD2 and SF3B3 and repeated representation in hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1), (hu.MAP huMAP3_00960.1), (hu.MAP huMAP3_13511.1), (hu.MAP huMAP3_07622.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), and (hu.MAP huMAP3_09945.1) provide unusually direct structural support. Its established association with retinal degeneration further highlights the functional importance of spliceosome integrity.
- **Conclusion**: Established evidence supports SNRNP200 as a core catalytic-stage spliceosomal component and a strong anchor for the module interpretation. A reasonable hypothesis is that its abundance tracks overall spliceosome capacity, but this requires functional testing rather than inference from co-abundance alone.

#### SF3B3

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.83), HNRNPF (0.82), EFTUD2 (0.81), DDX5 (0.81), HNRNPK (0.80); STRING partners: EFTUD2 (0.999), HNRNPK (0.971), SNRNP200 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Nucleoli rim; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_06511.1
- **Function (MyGene.info)**: splicing factor 3b subunit 3. This gene encodes subunit 3 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); dengue disease (0.370); cervical cancer (0.189); cervical carcinoma (0.189); prostate cancer (0.111)
- **Europe PMC papers**: 965
- **Why important**: SF3B3 is a component of the SF3B complex and U2 small nuclear ribonucleoprotein, which helps anchor the spliceosome near the intron branch site. It is present across the primary splicing and RNA-processing terms (GO:BP RNA splicing, via transesterification reactions; q_global = 7.14e-05), (GO:BP mRNA splicing, via spliceosome; q_global = 7.14e-05), (GO:CC catalytic step 2 spliceosome; q_global = 0.000188), (GO:CC spliceosomal complex; q_global = 0.000333), (GO:BP RNA splicing; q_global = 0.00126), (GO:BP regulation of RNA splicing; q_global = 0.00371), (GO:BP mRNA processing; q_global = 0.00436), (KEGG Spliceosome - Homo sapiens (human); q_global = 0.039), (GO:BP RNA processing; q_global = 0.0485), and (GO:BP protein-RNA complex assembly; q_global = 0.049). Its strong STRING relationships with EFTUD2, SNRNP200, HNRNPK, and DDX5, together with hu.MAP support in (hu.MAP huMAP3_08980.1) and (hu.MAP huMAP3_06511.1), place it at the interface between spliceosome structure and regulatory RNA-binding proteins. The module also contains a disease association with cervical cancer and cervical carcinoma for this gene.
- **Conclusion**: Established evidence supports SF3B3 as a central U2 and spliceosomal scaffold within the module. Its cancer associations make it biologically relevant to cervix_uterine research, but the supplied data do not establish a cancer-specific mechanism or causal role.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): HNRNPH1 (0.90), HSPH1 (0.85), HNRNPF (0.84), DDX39B (0.82), DDX5 (0.82), RBBP4 (0.81), SF3B3 (0.80); STRING partners: DDX39B (0.808), DDX5 (0.935), HNRNPF (0.971), HNRNPH1 (0.975), SF3B3 (0.971)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_14523.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is a highly connected hnRNP member linking DDX5, DDX39B, HNRNPF, HNRNPH1, SF3B3, and RBBP4. It appears in the primary terms for splicing, regulation of splicing, RNA processing, gene expression, and the KEGG spliceosome pathway (GO:BP RNA splicing, via transesterification reactions; q_global = 7.14e-05), (GO:BP mRNA splicing, via spliceosome; q_global = 7.14e-05), (GO:CC catalytic step 2 spliceosome; q_global = 0.000188), (GO:CC spliceosomal complex; q_global = 0.000333), (GO:BP RNA splicing; q_global = 0.00126), (GO:BP regulation of RNA splicing; q_global = 0.00371), (GO:BP mRNA processing; q_global = 0.00436), (GO:CC nuclear protein-containing complex; q_global = 0.0269), (GO:BP gene expression; q_global = 0.0337), (KEGG Spliceosome - Homo sapiens (human); q_global = 0.039), and (GO:BP RNA processing; q_global = 0.0485). Its established roles in pre-mRNA processing, transcriptional regulation, and signal-related gene control, plus its extensive literature and developmental disease associations, make it a plausible regulatory connector rather than merely a structural spliceosome part. It is also represented in the hnRNP complex (hu.MAP huMAP3_14523.1).
- **Conclusion**: Established evidence supports HNRNPK as a multifunctional RNA-binding and transcriptional regulator that may connect spliceosomal activity to broader gene-expression programs. Its position supports a regulatory-bridge hypothesis, but the module does not identify which transcripts or splicing decisions are affected.

## Module 6

**Tissue pair**: cervix_uterine and lung  
**Genes (5)**: AP3D1, BRIX1, PGP, RSL1D1, YBX3

### Function

The module does not support a single, statistically established GO or KEGG function: no GO or KEGG term passed global correction. Its genes instead span several cellular processes. BRIX1 is associated with ribosomal large-subunit assembly and rRNA processing, while RSL1D1 is associated with RNA binding, protein localization, apoptosis regulation, and cellular senescence. AP3D1 represents Golgi, vesicle-coat, lysosomal, and intracellular trafficking functions. PGP represents glycerol and glycerophospholipid metabolism and toxic-metabolite repair. YBX3 represents RNA binding, mRNA stabilization, stress responses, tumor-necrosis-factor responses, and negative regulation of cell death. The co-abundance pattern therefore appears more consistent with a shared cellular state involving nucleolar and RNA-related activity, intracellular trafficking, metabolism, and stress regulation than with a narrowly defined pathway. The lack of significant enrichment does not invalidate the module, but it limits functional interpretation.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity and low immune-cell specificity, arguing against a predominantly blood-cell or plasma-protein explanation. One gene is tissue enhanced in brain, one is group enriched in skeletal muscle and tongue, and the remaining genes are broadly distributed or low-specificity. YBX3 has enhanced association with naive B cells, but the other genes do not show strong blood-cell specificity. Protein detection is present for several genes in cervix and for fewer genes in lung, with some genes lacking tissue data. Overall, the composition is compatible with broadly expressed intracellular proteins, with limited evidence for a shared immune-cell contribution and no evidence for a secreted-protein module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known relationship is the high-confidence STRING association between BRIX1 and RSL1D1. The network also places BRIX1 at the central position connecting RSL1D1, AP3D1, and YBX3, while RSL1D1 connects to PGP. However, the other observed co-abundance relationships are not supported by the reported high-confidence STRING interactions. No hu.MAP complex contains multiple module members. Thus, the module contains one well-supported known nucleolar relationship embedded in a broader co-abundance pattern that is not currently explained by a documented common complex. STRING and hu.MAP support part of the module but do not establish that all members form a physical or functional complex.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: BRIX1–RSL1D1 (0.997)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is plausibly a novel tissue-shared co-abundance association, but it cannot be called a definitively new biological mechanism. The pattern is unusual because a nucleolar pair is linked by co-abundance to vesicle trafficking, phosphoglycerate-related metabolism, and RNA or stress regulation, while only the BRIX1–RSL1D1 relationship is already strongly represented in STRING and no shared hu.MAP complex is reported. The absence of broader STRING or hu.MAP support is evidence that the complete grouping is not an established complex, not proof that it is novel. The absence of globally significant GO or KEGG enrichment further indicates that the novelty claim rests on the cross-tissue network pattern rather than on a newly identified pathway. A plausible explanation is coordinated expression of broadly expressed intracellular programs or shared sample-composition effects, which should be tested before assigning mechanistic novelty.

**Hypothesis.** Hypothesis: the conserved module reflects a shared intracellular maintenance or stress state in cervix and lung samples. BRIX1 and RSL1D1 may mark coordinated nucleolar and ribosome-related activity, with BRIX1 acting as the network bridge to AP3D1-dependent intracellular trafficking and YBX3-dependent RNA or stress regulation; PGP may reflect accompanying lipid or metabolite handling. This could arise from coordinated cell-state regulation, differences in cellular composition, or a common proliferative or stress-related condition rather than a stable multiprotein complex. The hypothesis predicts that module activity should covary with nucleolar or ribosome biogenesis markers, RNA-stability or stress-response markers, vesicle or lysosomal trafficking markers, and metabolic-state markers in independent cervix and lung datasets. These predictions are hypotheses, not established consequences of the current evidence.

### Important genes

#### BRIX1

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.87), AP3D1 (0.83), YBX3 (0.81); STRING partners: RSL1D1 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Mitotic chromosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biogenesis of ribosomes BRX1. Enables RNA binding activity. Predicted to be involved in ribosomal large subunit assembly. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: colorectal cancer (0.077); cancer (0.077); colorectal carcinoma (0.074); deficiency anemia (0.065); sialolithiasis (0.060)
- **Europe PMC papers**: 251
- **Why important**: BRIX1 is the most connected gene in the module and bridges the nucleolar pair to AP3D1 and YBX3. Its established roles in ribosomal large-subunit assembly and rRNA processing provide the clearest organizing biological theme in the network. It also has a high-confidence STRING relationship with RSL1D1. Its literature is substantial, and its disease associations include cancer and deficiency anemia in Open Targets.
- **Conclusion**: Established evidence supports BRIX1 as the network hub and as a ribosome-biogenesis or nucleolar gene. It is the strongest candidate for organizing the module's shared cellular-state signal. It remains a hypothesis that BRIX1 mechanistically drives the links to vesicle trafficking, metabolism, or stress regulation.

#### RSL1D1

- **Related proteins** (co-abundance neighbors): BRIX1 (0.87), PGP (0.82); STRING partners: BRIX1 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal L1 domain containing 1. Enables mRNA 3'-UTR binding activity and mRNA 5'-UTR binding activity. Involved in regulation of apoptotic process and regulation of cellular senescence. Acts upstream of or within regulation of protein localization. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: adolescent idiopathic scoliosis (0.219); hepatocellular carcinoma (0.099); neoplasm (0.099); colorectal carcinoma (0.096); insomnia (0.078)
- **Europe PMC papers**: 381
- **Why important**: RSL1D1 is directly connected to BRIX1 through the module's strongest known STRING relationship and occupies a bridge position toward PGP. Its nucleolar localization and reported links to RNA binding, apoptosis regulation, senescence, and protein localization make it relevant to a possible growth, stress, or cell-survival state. It has a substantial literature and disease associations involving neoplasm, hepatocellular carcinoma, and adolescent idiopathic scoliosis.
- **Conclusion**: Established evidence supports RSL1D1 as a nucleolar and RNA-associated partner of BRIX1 with additional links to cell survival and senescence. It may help explain why the module is conserved across tissues. The proposed role as a coordinator between nucleolar activity and PGP-associated metabolism is speculative.

#### AP3D1

- **Related proteins** (co-abundance neighbors): BRIX1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor related protein complex 3 subunit delta 1. The protein encoded by this gene is a subunit of the AP3 adaptor-like complex, which is not clathrin-associated, but is associated with the golgi region, as well as more peripheral structures. The AP-3 complex facilitates the budding of vesicles from the golgi membrane, and may be directly involved in trafficking to lysosomes. This subunit is implicated in intracellular biogenesis and trafficking …
- **Diseases (Open Targets)**: Hermansky-Pudlak syndrome 10 (0.584); Hermansky-Pudlak syndrome 2 (0.455); Hermansky-Pudlak syndrome (0.432); Alzheimer disease (0.421); lysosomal storage disease (0.417)
- **Europe PMC papers**: 637
- **Why important**: AP3D1 is connected directly to the central BRIX1 node and contributes a distinct intracellular-trafficking dimension. Its annotated functions include AP-three adaptor-complex activity, vesicle budding, lysosomal transport, and Golgi-associated trafficking. It has a substantial literature and disease associations with Hermansky-Pudlak syndrome and lysosomal storage disease.
- **Conclusion**: Established evidence supports AP3D1 as an intracellular vesicle and lysosomal-trafficking component. Its connection to BRIX1 is a co-abundance observation rather than a documented physical interaction in the supplied STRING or hu.MAP evidence. A role in coupling nucleolar state to organelle trafficking is therefore only a hypothesis.

#### PGP

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Nuclear bodies; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglycolate phosphatase. Enables glycerol-3-phosphatase activity and phosphoglycolate phosphatase activity. Involved in glycerol biosynthetic process; glycerophospholipid metabolic process; and negative regulation of gluconeogenesis. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.499); Abnormality of the skeletal system (0.356); lysosomal storage disease (0.347); neoplasm (0.118); cancer (0.117)
- **Europe PMC papers**: 16025
- **Why important**: PGP is connected to RSL1D1 and contributes metabolic context through glycerol biosynthesis, glycerophospholipid metabolism, gluconeogenesis regulation, and toxic-metabolite repair. It has the largest literature volume among the module genes and disease associations involving neurodegenerative disease, skeletal abnormalities, lysosomal storage disease, and neoplasm. Its tissue-enhanced brain pattern and detection in both sampled tissues make it relevant to interpreting the shared signal.
- **Conclusion**: Established evidence supports PGP as a metabolic and metabolite-repair enzyme with broad disease relevance. Its co-abundance with RSL1D1 may indicate a shared cellular state, but there is no supplied evidence that PGP forms a physical complex with RSL1D1 or the other module members. Its participation in a coordinated nucleolar-metabolic program remains hypothetical.

#### YBX3

- **Related proteins** (co-abundance neighbors): BRIX1 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Y-box binding protein 3. Enables RNA binding activity. Involved in cellular hyperosmotic response; cellular response to tumor necrosis factor; and negative regulation of programmed cell death. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: coronary artery disorder (0.429); refractive error (0.381); neurodegenerative disease (0.312); Abnormality of refraction (0.289); menopause (0.226)
- **Europe PMC papers**: 873
- **Why important**: YBX3 is directly connected to BRIX1 and contributes RNA-binding, mRNA-stabilization, osmotic-stress, tumor-necrosis-factor, and cell-death-regulatory functions. It is group enriched in skeletal muscle and tongue, shows enhanced association with several specialized cell types, and is immune-cell enhanced in naive B cells. Its literature is substantial, and Open Targets links it to coronary artery disorder, neurodegenerative disease, refractive traits, and menopause.
- **Conclusion**: Established evidence supports YBX3 as an RNA-regulatory and stress-response gene with context-dependent tissue and cell-type patterns. Its lack of HPA detection in lung but detection in cervix cautions against treating it as a uniform lung marker. Its connection to BRIX1 may reflect coordinated RNA or stress regulation, but a direct mechanistic bridge is not established.

## Module 7

**Tissue pair**: cervix_uterine and lung  
**Genes (5)**: APMAP, ITGB5, PRKCD, TAP2, VWA5A

### Function

The module is most consistent with a weakly supported interface between intracellular signaling, antigen transport, cell adhesion, and membrane-associated biology. Its co-abundance topology forms a chain-like pattern linking PRKCD with VWA5A and TAP2, while VWA5A links to APMAP and APMAP links to ITGB5. PRKCD provides established kinase, stress-response, apoptotic, and cell-cycle functions; TAP2 provides established antigen-processing and peptide-transport functions; and ITGB5 provides established integrin-mediated adhesion, migration, and cell-surface signaling functions. APMAP is a membrane-associated protein with a reported arylesterase activity, whereas VWA5A has comparatively sparse functional annotation. No GO or KEGG term passed global correction, and there was no supplementary STRING functional enrichment. Therefore, the functional interpretation is driven by gene-level biology and the co-abundance pattern rather than pathway-enrichment evidence.

**Cell composition.** This is not a secreted-protein module: none of its members is annotated as secreted. Most members have low tissue specificity in HPA, while APMAP is tissue-enhanced in liver and ITGB5 is tissue-enhanced in blood vessel. HPA assigns cell-type specificity to nearly all members, including associations with neutrophils, platelets, mast cells, basophils, hepatocytes, and cytotrophoblast-related cells. The module therefore may partly reflect shared cellular composition, vascular or immune-associated material, or tissue-specific cell mixtures rather than a single conserved intracellular pathway. The largely low immune-cell specificity argues against treating it as a dedicated blood-cell module. Protein detection is broad across the two tissues, although TAP2 is not detected in cervix_uterine by the supplied HPA evidence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair has a high-confidence STRING interaction in the supplied results, and no STRING functional enrichment was reported. No hu.MAP complex contains multiple module members. Thus, the co-abundance edges should not be interpreted as established physical interactions or membership in a known multiprotein complex. The absence of STRING and hu.MAP support is informative: the module appears to be a coordinated expression pattern without corroboration from the queried interaction and complex resources. It may reflect co-regulation, shared cell composition, indirect biological coupling, or context-specific associations.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact conserved co-abundance pattern may be a potentially novel tissue-pair observation because it is not represented by high-confidence STRING interactions or a shared hu.MAP complex. However, this does not establish that the module is a new biological mechanism. The lack of global GO or KEGG enrichment, the absence of STRING support, the limited annotation of VWA5A, and the possibility of cell-composition effects all make a strong novelty claim premature. The defensible conclusion is that the co-abundance observation is potentially novel as a tissue-pair pattern and requires replication, cell-composition adjustment, and experimental or independent-cohort validation before being called a new pathway.

**Hypothesis.** Hypothesis: in cervix_uterine and lung samples, a shared cellular or tissue-state program may coordinate PRKCD-linked stress and immune signaling with TAP2-dependent antigen transport and an APMAP–ITGB5 membrane-adhesion axis, with VWA5A acting as a transcriptionally associated bridge rather than a proven physical adaptor. This could arise from coordinated responses in vascular, epithelial, immune-associated, or mixed-cell populations. The hypothesis predicts that the module relationships should weaken after adjustment for relevant cell-type composition if they are primarily compositional, but should persist and correlate with signaling, antigen-presentation, or adhesion states if they represent a conserved regulatory program.

### Important genes

#### PRKCD

- **Related proteins** (co-abundance neighbors): VWA5A (0.88), TAP2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase C delta. The protein encoded by this gene is a member of the protein kinase C family of serine- and threonine-specific protein kinases. The encoded protein is activated by diacylglycerol and is both a tumor suppressor and a positive regulator of cell cycle progression. Also, this protein can positively or negatively regulate apoptosis. Defects in this gene are a cause of autoimmune lymphoproliferative synd…
- **Diseases (Open Targets)**: autoimmune lymphoproliferative syndrome (0.685); acute myeloid leukemia (0.556); mast cell leukemia (0.475); systemic mastocytosis (0.471); mastocytosis (0.464)
- **Europe PMC papers**: 3335
- **Why important**: PRKCD is the most connected member of the module and links the VWA5A–APMAP side of the pattern to TAP2. Its established kinase, stress-response, apoptosis, DNA-damage, and immune-related biology gives the module a plausible signaling anchor. It also has extensive literature and disease associations involving immune dysregulation and hematologic disease.
- **Conclusion**: Established evidence supports PRKCD as a central signaling gene with roles in stress, apoptosis, cell-cycle regulation, and immune biology. It is a plausible module organizer by network position, but the supplied data do not establish that it directly regulates the other module genes. Its role as the mechanistic driver remains a hypothesis.

#### TAP2

- **Related proteins** (co-abundance neighbors): PRKCD (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transporter 2, ATP binding cassette subfamily B member. The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily ar…
- **Diseases (Open Targets)**: MHC class I deficiency (0.729); MHC class I deficiency 2 (0.477); hereditary disease (0.193); neoplasm (0.107); cancer (0.097)
- **Europe PMC papers**: 4557
- **Why important**: TAP2 is the module member with the clearest antigen-processing annotation and is connected to PRKCD in the co-abundance graph. It encodes an ER transporter involved in peptide transport and MHC class I antigen presentation, with strong disease relevance to MHC class I deficiency and extensive literature.
- **Conclusion**: Established evidence supports TAP2 as an antigen-processing and peptide-transport component. Its terminal position suggests that it may report a specialized branch of the module rather than act as a central connector. A link between TAP2 and PRKCD is supported here only as co-abundance, not as a demonstrated physical or regulatory interaction.

#### APMAP

- **Related proteins** (co-abundance neighbors): VWA5A (0.80), ITGB5 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adipocyte plasma membrane associated protein. Enables arylesterase activity. Predicted to be involved in biosynthetic process. Located in cell surface and membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: smoking initiation (0.243); obesity disorder (0.196); Alzheimer disease (0.078); infection (0.077); cervical carcinoma (0.076)
- **Europe PMC papers**: 444
- **Why important**: APMAP occupies an internal position between VWA5A and ITGB5, making it a structural bridge toward the membrane-adhesion arm of the module. HPA places it in a liver-enhanced context and associates it with hepatocytes, cytotrophoblast-related cells, neutrophil-lineage cells, and the plasma membrane. Its disease and trait associations include obesity-related, infection-related, and cervical-carcinoma-related entries, although its literature base is more limited than that of PRKCD or TAP2.
- **Conclusion**: Established evidence supports APMAP as a membrane-associated protein with reported arylesterase activity and cell-type-sensitive expression. Its bridge position makes it important for interpreting the module as a membrane or cell-composition signal. Whether it mechanistically connects signaling to adhesion is unproven and remains a hypothesis.

#### ITGB5

- **Related proteins** (co-abundance neighbors): APMAP (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Mitochondria; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 5. This gene encodes a beta subunit of integrin, which can combine with different alpha chains to form a variety of integrin heterodimers. Integrins are integral cell-surface receptors that participate in cell adhesion as well as cell-surface mediated signaling. The alphav beta5 integrin is involved in adhesion to vitronectin. [provided by RefSeq, Aug 2017].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.569); coronary artery disorder (0.567); carpal tunnel syndrome (0.490); migraine disorder (0.452); open-angle glaucoma (0.451)
- **Europe PMC papers**: 2960
- **Why important**: ITGB5 is the membrane receptor component at one end of the co-abundance pattern and is connected to APMAP. Its established integrin biology directly supports cell-matrix adhesion, vitronectin binding through alphav beta five integrin, migration, and surface-mediated signaling. HPA associates it with blood vessel tissue and several cell types including platelets and podocytes, and it has a substantial literature base.
- **Conclusion**: Established evidence supports ITGB5 as an adhesion and signaling receptor subunit with vascular and cell-interface relevance. Its network position is compatible with a membrane-facing module arm, but the supplied data do not show that it physically interacts with APMAP or that it explains the shared tissue pattern.

#### VWA5A

- **Related proteins** (co-abundance neighbors): PRKCD (0.88), APMAP (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enriched; location Nucleoplasm; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: von Willebrand factor A domain containing 5A. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.089); posterior polymorphous corneal dystrophy (0.073); Fuchs' endothelial dystrophy (0.071); retinitis pigmentosa (0.070); breast cancer (0.070)
- **Europe PMC papers**: 260
- **Why important**: VWA5A is an internal bridge between PRKCD and APMAP, so it is important for the topology even though its molecular annotation is sparse. HPA associates it with mast cells and basophils, which raises the possibility that this part of the module reflects an immune-associated cellular context. Its disease associations are tentative and its literature volume is limited relative to the better-characterized genes.
- **Conclusion**: Established evidence supports VWA5A as a nucleoplasmic protein with limited functional characterization and cell-type-associated expression. Its network position makes it a useful candidate marker of the co-abundance pattern, but there is insufficient evidence to assign it a specific mechanistic role. Any adaptor or regulatory interpretation is hypothetical.

## Module 8

**Tissue pair**: cervix_uterine and lung  
**Genes (9)**: APOD, BID, CP, CFB, CLU, C3, SERPING1, TRIM16, VTN

### Function

The module is most convincingly associated with complement and coagulation biology, supported by the globally corrected KEGG complement and coagulation term (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.000258) and the globally corrected GO complement-activation term (GO:BP complement activation; q_global = 0.00469). The blood-microparticle term (GO:CC blood microparticle; q_global = 0.000876) and endoplasmic-reticulum-lumen term (GO:CC endoplasmic reticulum lumen; q_global = 0.0114) indicate that the signal is strongly compatible with circulating or secreted proteins. Positive regulation of receptor-mediated endocytosis (GO:BP positive regulation of receptor-mediated endocytosis; q_global = 0.0172) and smooth-muscle cell–matrix adhesion (GO:BP smooth muscle cell-matrix adhesion; q_global = 0.0405) suggest additional roles in uptake, extracellular-matrix interaction, and vascular or stromal biology. The STRING supplementary results reinforce complement regulation and plasma-protein biology, but they are supplementary rather than globally corrected evidence.

**Cell composition.** This is predominantly a secreted, liver-associated plasma-protein module rather than a clear epithelial or organ-specific intracellular program. Most module genes are annotated as secreted to blood, and HPA evidence repeatedly links the genes to liver or hepatocytes. Several genes are associated with secretory, stromal, or endothelial-adjacent cell types, while some show immune-cell enrichment. Protein detection in cervix and lung is limited, and several genes are not detected by immunohistochemistry in either tissue. Therefore, the shared cervix–lung signal may reflect blood microparticles, vascular leakage, plasma content, or shared stromal and immune exposure rather than coordinated production by the dominant parenchymal cells of both organs. The blood-cell annotations do not establish that the module is generated by blood cells, especially because several proteins are not detected in immune cells.

**GO/KEGG enrichment**: 6 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 0.000258 | C3, CFB, CLU, SERPING1, VTN |
| GO:CC blood microparticle | 0.000876 | C3, CFB, CLU, CP, SERPING1, VTN |
| GO:BP complement activation | 0.00469 | C3, CFB, CLU, SERPING1 |
| GO:CC endoplasmic reticulum lumen | 0.0114 | C3, CLU, CP, SERPING1, VTN |
| GO:BP positive regulation of receptor-mediated endocytosis | 0.0172 | C3, CLU, VTN |
| GO:BP smooth muscle cell-matrix adhesion | 0.0405 | APOD, VTN |

### STRING and hu.MAP

STRING contains established relationships among the complement components C3 and CFB, the inhibitor SERPING1, and associated extracellular proteins including CLU and VTN. C3 is connected to several module members, while CLU connects the lipocalin-like or extracellular portion of the network and VTN links complement-associated biology with cell adhesion. CP is also connected to C3 and CLU. These relationships indicate that the network is not an arbitrary co-abundance pattern; much of it recapitulates known plasma protein biology. Repeated hu.MAP complexes contain CP, CFB, C3, and SERPING1 together, alongside broader complement, coagulation, acute-phase, and plasma-protein components. This supports a recognized complement-containing extracellular complex context. CLU, VTN, APOD, TRIM16, and BID do not have corresponding multi-member hu.MAP representation in the listed complexes, so their placement may reflect interactions, shared abundance, or functional coupling rather than membership in a single experimentally defined complex.

**STRING interactions (score >= 0.7)**: 11 of 36 gene pairs: APOD–CLU (0.939); C3–CFB (0.999); C3–CLU (0.803); C3–CP (0.751); C3–SERPING1 (0.954); C3–VTN (0.79); CFB–SERPING1 (0.88); CLU–CP (0.794); CLU–SERPING1 (0.721); CLU–VTN (0.962); SERPING1–VTN (0.719)
**STRING functional enrichment (supplementary, within-query FDR)**: WikiPathways Complement system in neuronal development and plasticity (FDR = 2.38e-07, 6 genes); TISSUES Plasma cell (FDR = 2.24e-06, 7 genes); RCTM Regulation of Complement cascade (FDR = 1.21e-05, 5 genes); PMID (2019) Complement C5b-9 and Cancer: Mechanisms of Cell Damage, Cancer Counteractions, and Approaches for Intervention. (FDR = 2.3e-05, 6 genes); KEGG Complement and coagulation cascades (FDR = 3.58e-05, 5 genes); PMID (2020) Longitudinal Stroke Recovery Associated With Dysregulation of Complement System-A Proteomics Pathway Analysis. (FDR = 4.32e-05, 6 genes); PMID (2014) Proteomic analysis of human plasma in chronic rheumatic mitral stenosis reveals proteins involved in the complement and coagulation cascade. (FDR = 4.32e-05, 7 genes); PMID (2023) The Sertoli Cell Complement Signature: A Suspected Mechanism in Xenograft Survival. (FDR = 0.00016, 5 genes); PMID (2023) Complement System Proteins in the Human Aqueous Humor and Their Association with Primary Open-Angle Glaucoma. (FDR = 0.00016, 5 genes); PMID (2022) Dysregulation of complement and coagulation pathways: emerging mechanisms in the development of psychosis. (FDR = 0.00016, 5 genes); PMID (2022) Complement System and Alarmin HMGB1 Crosstalk: For Better or Worse. (FDR = 0.00016, 5 genes); PMID (2022) Proprotein Convertases and the Complement System. (FDR = 0.00016, 5 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 0.00016, 7 genes); PMID (2021) Gain-of-Function Mutations R249C and S250C in Complement C2 Protein Increase C3 Deposition in the Presence of C-Reactive Protein. (FDR = 0.00016, 5 genes); PMID (2020) Quantitative multiplex profiling of the complement system to diagnose complement-mediated diseases. (FDR = 0.00016, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09531.1 (CP, CFB, C3, SERPING1; 4/47); huMAP3_10101.1 (CP, CFB, C3, SERPING1; 4/49); huMAP3_15040.1 (CP, CFB, C3, SERPING1; 4/64); huMAP3_10678.1 (CP, CFB, C3, SERPING1; 4/71); huMAP3_09273.1 (CP, CFB, SERPING1; 3/28); huMAP3_08395.1 (CP, CFB, C3; 3/43); huMAP3_07432.1 (CP, C3; 2/18)

### Novelty

The complement and plasma-protein biology is established rather than a new biological pathway discovery: it is supported by globally corrected enrichment, STRING relationships, and recurring hu.MAP complexes. The potentially novel aspect is the observation that these genes form a conserved co-abundance module across cervix and lung in this dataset. That claim should remain provisional because the module is small, is dominated by secreted liver-associated proteins, and may be driven by shared blood or extracellular-fluid content. Absence of a complete matching module in STRING or hu.MAP would not prove novelty, and the available evidence does not establish tissue-specific production, causality, or a previously unknown molecular complex.

**Hypothesis.** Hypothesis: the shared module reflects a circulating extracellular complement-regulatory state that becomes co-abundant in cervix and lung samples through common exposure to plasma, blood microparticles, or vascular and stromal compartments. In this model, C3 and CFB provide alternative-pathway activity, SERPING1 constrains complement activation, CLU protects against complement-associated damage, and VTN and APOD connect the extracellular immune environment to matrix adhesion, lipid handling, and tissue repair. CP may contribute metal-dependent oxidative and iron-handling functions. The hypothesis predicts that module abundance will track vascular or extracellular-fluid content and complement activity more closely than the identity of the organ parenchymal cell. It requires testing with cell-resolved data, plasma contamination markers, complement activation products, and independent cervix and lung cohorts.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): SERPING1 (0.87), CP (0.86), CFB (0.82); STRING partners: CFB (0.999), CLU (0.803), CP (0.751), SERPING1 (0.954), VTN (0.79)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_08395.1, huMAP3_07432.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a central network connector and appears in the complement/coagulation, blood microparticle, complement-activation, endoplasmic-reticulum-lumen, and endocytosis terms (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.000258), (GO:CC blood microparticle; q_global = 0.000876), (GO:BP complement activation; q_global = 0.00469), (GO:CC endoplasmic reticulum lumen; q_global = 0.0114), and (GO:BP positive regulation of receptor-mediated endocytosis; q_global = 0.0172). Its established function is central to both classical and alternative complement activation, and its products can promote inflammation and antimicrobial activity. It has extensive literature and strong disease associations involving complement deficiency, complement dysregulation, kidney disease, and macular degeneration. HPA supports liver and hepatocyte association and secretion to blood.
- **Conclusion**: Established conclusion: C3 is the principal functional anchor of the module and strongly supports a complement interpretation. Hypothesis: its co-abundance may report local complement exposure or activation, but abundance alone does not show that C3 is activated in either tissue.

#### CFB

- **Related proteins** (co-abundance neighbors): C3 (0.82); STRING partners: C3 (0.999), SERPING1 (0.88)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_09273.1, huMAP3_08395.1
- **Function (MyGene.info)**: complement factor B. This gene encodes complement factor B, a component of the alternative pathway of complement activation. Factor B circulates in the blood as a single chain polypeptide. Upon activation of the alternative pathway, it is cleaved by complement factor D yielding the noncatalytic chain Ba and the catalytic subunit Bb. The active subunit Bb is a serine protease which associates with C3b to form the alter…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with B factor anomaly (0.764); atypical hemolytic-uremic syndrome (0.705); Immunodeficiency due to a complement cascade protein anomaly (0.614); paroxysmal nocturnal hemoglobinuria (0.561); complement 3 glomerulopathy (0.546)
- **Europe PMC papers**: 7226
- **Why important**: CFB is directly connected to C3 and occurs with C3 and SERPING1 in the recurring hu.MAP complexes. It is present in the globally corrected complement/coagulation, blood-microparticle, and complement-activation terms (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.000258), (GO:CC blood microparticle; q_global = 0.000876), and (GO:BP complement activation; q_global = 0.00469). Its established function is as the alternative-pathway factor that is cleaved to form the catalytic component of the C3 convertase. It has substantial literature and disease associations involving alternative-pathway abnormalities and complement glomerulopathy. HPA links it to liver and secretory compartments.
- **Conclusion**: Established conclusion: CFB gives the module a specific alternative-complement mechanistic component rather than a generic inflammation label. Hypothesis: co-abundance of CFB with C3 could indicate coordinated alternative-pathway capacity, although functional convertase formation must be demonstrated directly.

#### SERPING1

- **Related proteins** (co-abundance neighbors): C3 (0.87), APOD (0.80); STRING partners: C3 (0.954), CFB (0.88), CLU (0.721), VTN (0.719)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_09273.1
- **Function (MyGene.info)**: serpin family G member 1. This gene encodes a highly glycosylated plasma protein involved in the regulation of the complement cascade. Its encoded protein, C1 inhibitor, inhibits activated C1r and C1s of the first complement component and thus regulates complement activation. It is synthesized in the liver, and its deficiency is associated with hereditary angioneurotic oedema (HANE). Alternative splicing results in multipl…
- **Diseases (Open Targets)**: hereditary angioedema with C1Inh deficiency (0.828); hereditary angioedema type 1 (0.750); hereditary angioedema (0.728); angioedema (0.616); hereditary angioedema type 2 (0.614)
- **Europe PMC papers**: 4203
- **Why important**: SERPING1 connects to C3, CFB, CLU, and VTN and is included in the complement and coagulation, blood-microparticle, complement-activation, and endoplasmic-reticulum-lumen terms (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.000258), (GO:CC blood microparticle; q_global = 0.000876), (GO:BP complement activation; q_global = 0.00469), and (GO:CC endoplasmic reticulum lumen; q_global = 0.0114). It encodes the plasma C1 inhibitor and is an established negative regulator of complement activation. Its disease associations with hereditary angioedema and C1-inhibitor deficiency make it a clinically informative counter-regulatory gene. HPA supports liver, hepatocyte, stromal, and blood-secreted biology.
- **Conclusion**: Established conclusion: SERPING1 provides evidence that the module includes complement control as well as complement activation. Hypothesis: coordinated SERPING1 abundance may represent a compensatory response intended to limit complement injury, but the direction of pathway activity cannot be inferred from its abundance alone.

#### CLU

- **Related proteins** (co-abundance neighbors): VTN (0.87), TRIM16 (0.85), CP (0.80); STRING partners: APOD (0.939), C3 (0.803), CP (0.794), SERPING1 (0.721), VTN (0.962)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: clusterin. The protein encoded by this gene is a secreted chaperone that can under some stress conditions also be found in the cell cytosol. It has been suggested to be involved in several basic biological events such as cell death, tumor progression, and neurodegenerative disorders. Alternate splicing results in both coding and non-coding variants.[provided by RefSeq, May 2011].
- **Diseases (Open Targets)**: Alzheimer disease (0.583); dementia (0.525); refractive error (0.444); late-onset Alzheimers disease (0.406); prostate cancer (0.376)
- **Europe PMC papers**: 10677
- **Why important**: CLU is a network connector linking APOD, C3, CP, SERPING1, and VTN in STRING and is present across the globally corrected complement-related and extracellular terms (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.000258) through (GO:BP positive regulation of receptor-mediated endocytosis; q_global = 0.0172). It is an established secreted chaperone with roles in protein handling, immune-complex clearance, inhibition of membrane-attack-complex activation, stress responses, and cell-death biology. It has broad literature and disease associations including neurodegenerative disorders and cancer. HPA supports liver enrichment, secreted-to-blood localization, and cervix detection.
- **Conclusion**: Established conclusion: CLU plausibly connects complement regulation with extracellular proteostasis and tissue stress. Hypothesis: CLU may buffer complement-associated damage or stabilize extracellular protein assemblies in the shared tissue environment; this protective interpretation requires functional testing.

#### VTN

- **Related proteins** (co-abundance neighbors): CLU (0.87); STRING partners: C3 (0.79), CLU (0.962), SERPING1 (0.719)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vitronectin. The protein encoded by this gene functions in part as an adhesive glycoprotein. Differential expression of this protein can promote either cell adhesion or migration as it links cells to the extracellular matrix through a variety of ligands. These ligands include integrins, plasminogen activator inhibitor-1, and urokinase plasminogen activator receptor. This secreted protein can be present in the …
- **Diseases (Open Targets)**: hypertensive disorder (0.421); dengue disease (0.376); neurodegenerative disease (0.343); temporal arteritis (0.338); age-related macular degeneration (0.313)
- **Europe PMC papers**: 3940
- **Why important**: VTN is linked in STRING to CLU, C3, and SERPING1 and is the strongest annotation anchor for the globally corrected cell-matrix adhesion term (GO:BP smooth muscle cell-matrix adhesion; q_global = 0.0405). It also appears in the complement/coagulation, blood-microparticle, endoplasmic-reticulum-lumen, and endocytosis terms (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.000258), (GO:CC blood microparticle; q_global = 0.000876), (GO:CC endoplasmic reticulum lumen; q_global = 0.0114), and (GO:BP positive regulation of receptor-mediated endocytosis; q_global = 0.0172). Its established function is as a secreted adhesive glycoprotein that binds extracellular-matrix and integrin-related ligands and can influence cell adhesion and migration. HPA links it to liver and hepatocytes and to secretion into blood.
- **Conclusion**: Established conclusion: VTN broadens the module from complement into extracellular matrix and adhesion biology. Hypothesis: VTN could connect complement-associated vascular or inflammatory signals to stromal remodeling in cervix and lung, but the module does not establish tissue remodeling causality.

#### APOD

- **Related proteins** (co-abundance neighbors): SERPING1 (0.80); STRING partners: CLU (0.939)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein D. This gene encodes a component of high density lipoprotein that has no marked similarity to other apolipoprotein sequences. It has a high degree of homology to plasma retinol-binding protein and other members of the alpha 2 microglobulin protein superfamily of carrier proteins, also known as lipocalins. This glycoprotein is closely associated with the enzyme lecithin:cholesterol acyltransferase - a…
- **Diseases (Open Targets)**: gastric cancer (0.099); Alzheimer disease (0.098); Parkinson disease (0.098); neoplasm (0.091); cancer (0.088)
- **Europe PMC papers**: 5533
- **Why important**: APOD occupies a peripheral but informative position, connecting to SERPING1 in the module and to CLU in STRING. It is the other gene supporting the globally corrected smooth-muscle cell–matrix adhesion term (GO:BP smooth muscle cell-matrix adhesion; q_global = 0.0405). Its established biology includes lipid transport, association with high-density lipoprotein, oxidative-stress response, and stress-related tissue processes. It has substantial literature, and HPA links it to lung detection, stromal and fibroblast-associated cell types, and secretion to blood.
- **Conclusion**: Established conclusion: APOD suggests that lipid transport and oxidative-stress handling accompany the complement and matrix signal. Hypothesis: APOD may mark a protective stromal or vascular response coupled to complement regulation, but its peripheral network position makes that interpretation less secure than the complement-core interpretation.

## Module 9

**Tissue pair**: cervix_uterine and lung  
**Genes (7)**: ATP2A3, IST1, STXBP2, TLN2, TOM1, TRADD, UTRN

### Function

No GO/KEGG term passed global correction, and there was no supplementary STRING enrichment. Therefore, the module should not be assigned a single statistically established pathway. Its gene annotations and co-abundance structure instead suggest several connected cellular themes: cytoskeletal anchoring and cell adhesion through TLN2 and UTRN; endosomal, vesicular, and autophagy-related trafficking through TOM1 and IST1; intracellular calcium handling through ATP2A3; death-receptor and inflammatory signaling through TRADD; and regulated vesicle fusion and cytotoxic-granule release through STXBP2. The module is therefore best interpreted as a coordinated membrane–cytoskeleton, trafficking, calcium, and inflammatory-response program rather than as a demonstrated canonical pathway.

**Cell composition.** None of the module genes is annotated as secreted, so this is not a plasma-protein or secretome module. The HPA profile shows cell-type enhancement for every member, with repeated associations to neutrophils, neutrophil progenitors, monocytes, and platelets, while STXBP2 is enhanced in lymphoid tissue. This raises the possibility that the shared signal partly reflects immune or blood-related cellular composition in cervix_uterine and lung samples. However, the profile is not uniformly immune: several genes have low immune-cell specificity, one is not detected in immune cells, and the genes also show tissue or cell associations involving epithelial, muscle, adipose, endothelial-related, and alveolar contexts. The module therefore may combine a blood-cell or inflammatory component with structural and intracellular trafficking biology. HPA protein detection in both tissues for most members supports the possibility that the signal is biologically present in both tissues, although the absence of protein detection for TLN2 in cervix_uterine and for STXBP2 in both listed tissues makes protein-level interpretation uneven.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the specified high-confidence threshold, and no hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not supported here as established high-confidence physical interactions or as membership in a known multiprotein complex. The absence of STRING and hu.MAP support does not invalidate the co-abundance module: co-regulation, shared cell-type composition, indirect signaling, or tissue-specific biology can produce correlated abundance without direct binding. The annotated functions nevertheless provide biologically plausible links among adhesion, trafficking, calcium handling, inflammatory signaling, and regulated secretion.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module can reasonably be described as a potentially under-characterized co-abundance pattern, but not as a proven new biological mechanism. Its particular cross-tissue co-abundance combination is not represented by a corresponding high-confidence STRING network or hu.MAP complex in the supplied evidence. That lack of database representation is compatible with novelty, but it does not establish novelty because the signal could arise from shared cell populations, coordinated regulation, indirect functional relationships, or technical and sampling effects. The strongest novelty claim is therefore that this specific conserved module association merits validation, not that its constituent biology is previously unknown.

**Hypothesis.** Hypothesis: a shared structural and inflammatory cell-state program in cervix_uterine and lung coordinates membrane adhesion with intracellular trafficking and stress-responsive signaling. TLN2 and UTRN may organize cytoskeletal or membrane-associated structures; TOM1 and IST1 may support endosomal sorting and membrane-remodeling processes; ATP2A3 may influence calcium-dependent cellular state; TRADD may connect inflammatory or death-receptor signaling; and STXBP2 may reflect regulated vesicle fusion in immune or secretory cells. A blood-cell or immune-cell contribution, particularly involving neutrophil-lineage or monocyte-related cells, may be responsible for part of the cross-tissue conservation. This hypothesis requires validation with cell-resolved expression, deconvolution, independent cohorts, and perturbation or interaction assays.

### Important genes

#### TLN2

- **Related proteins** (co-abundance neighbors): UTRN (0.88), TOM1 (0.81), STXBP2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Focal adhesion sites, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 2. This gene encodes a protein related to talin 1, a cytoskeletal protein that plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. This protein has a different pattern of expression compared to talin 1 but, like talin 1, is thought to associate with unique transmembrane receptors to form novel linkage…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.511); renal carcinoma (0.425); Insulin resistance (0.405); renal cell carcinoma (0.344); placenta praevia (0.343)
- **Europe PMC papers**: 792
- **Why important**: TLN2 has a central position in the module and connects to UTRN, TOM1, and STXBP2. Its established annotation concerns actin organization, cell adhesion, cell-cell junction assembly, and focal-adhesion biology. It is tissue enhanced in kidney and is not detected in immune cells by the supplied HPA summary, making it a useful candidate for a structural or non-blood component of the shared signal. Its literature base is substantial, and its disease associations include skeletal abnormality, renal disease, insulin resistance, and placenta praevia.
- **Conclusion**: Established evidence supports TLN2 as a cytoskeletal and adhesion-related anchor of the module. It is plausible, but not demonstrated, that TLN2 links structural cell state to the trafficking-associated genes. The co-abundance relation should not be interpreted as a direct physical interaction without experimental confirmation.

#### TOM1

- **Related proteins** (co-abundance neighbors): ATP2A3 (0.82), TRADD (0.81), TLN2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: target of myb1 membrane trafficking protein. This gene was identified as a target of the v-myb oncogene. The encoded protein shares its N-terminal domain in common with proteins associated with vesicular trafficking at the endosome. It is recruited to the endosomes by its interaction with endofin. Several alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.418); immunodeficiency 85 and autoimmunity (0.396); type 2 diabetes mellitus (0.368); COVID-19 (0.216); inflammatory bowel disease (0.152)
- **Europe PMC papers**: 1563
- **Why important**: TOM1 has a central position and connects to ATP2A3, TRADD, and TLN2. Its established functions include endocytosis, endosomal transport, protein transport, substrate localization to autophagosomes, and autophagosome-lysosome fusion. It is detected by immunohistochemistry in both tissues and has cell-type enhancement in monocytes and neutrophils, making it a candidate bridge between intracellular trafficking and the possible immune-cell component. Its literature volume is substantial, with disease associations involving neurodegenerative disease, immunodeficiency and autoimmunity, diabetes, COVID-19, and inflammatory bowel disease.
- **Conclusion**: Established evidence supports TOM1 as a trafficking and endolysosomal regulator that could connect several module themes. Its position makes it a strong integrative candidate, but the module does not establish that TOM1 directly mediates the observed tissue-pair conservation.

#### ATP2A3

- **Related proteins** (co-abundance neighbors): IST1 (0.84), TOM1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 3. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of muscle cells. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol to the sarcoplasmic reticulum lumen, and is involved in calcium sequestration associated with muscular excitation and contraction. Alternative spli…
- **Diseases (Open Targets)**: diabetes mellitus (0.411); type 2 diabetes mellitus (0.376); gastroesophageal reflux disease (0.276); esophageal disorder (0.240); alcohol drinking (0.222)
- **Europe PMC papers**: 1271
- **Why important**: ATP2A3 connects TOM1 and IST1 and encodes an intracellular calcium pump involved in calcium transport and calcium homeostasis. It is detected in both tissues and has cell-type enhancement involving neutrophil progenitors, megakaryocyte progenitors, B-cells, goblet cells, and foveolar cells. Its disease associations include diabetes and disorders involving the esophagus, while its literature base is substantial. Calcium handling offers a plausible regulatory interface between cellular stress, membrane trafficking, secretion, and inflammatory responses.
- **Conclusion**: Established evidence supports ATP2A3 as the module's calcium-homeostasis component. A role for ATP2A3 in coordinating trafficking or inflammatory state is a reasonable hypothesis from its function and network placement, but it is not proven by the enrichment or interaction evidence.

#### TRADD

- **Related proteins** (co-abundance neighbors): TOM1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TNFRSF1A associated via death domain. The protein encoded by this gene is a death domain containing adaptor molecule that interacts with TNFRSF1A/TNFR1 and mediates programmed cell death signaling and NF-kappaB activation. This protein binds adaptor protein TRAF2, reduces the recruitment of inhibitor-of-apoptosis proteins (IAPs) by TRAF2, and thus suppresses TRAF2 mediated apoptosis. This protein can also interact with receptor TNFRSF…
- **Diseases (Open Targets)**: hereditary disease (0.370); Abnormality of the skeletal system (0.222); cataract 5 multiple types (0.181); androgenetic alopecia (0.091); non-small cell lung carcinoma (0.085)
- **Europe PMC papers**: 6284
- **Why important**: TRADD connects to TOM1 and is a death-domain adaptor associated with TNFR1 and Fas signaling. Its established annotations include apoptosis, inflammatory response, canonical NF-kappaB signaling, and extrinsic death-receptor signaling. It is detected in both tissues and has cell-type enhancement in esophageal epithelial populations, which supports a possible epithelial or barrier-associated context rather than a purely circulating-cell interpretation. It has the largest literature volume among the module genes and disease associations that include hereditary disease and non-small cell lung carcinoma.
- **Conclusion**: Established evidence supports TRADD as an inflammatory and cell-death signaling component. Its connection to TOM1 suggests a possible interface between receptor signaling and trafficking, but that mechanistic link remains a hypothesis because no high-confidence STRING or hu.MAP relationship was supplied.

#### STXBP2

- **Related proteins** (co-abundance neighbors): TLN2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntaxin binding protein 2. This gene encodes a member of the STXBP/unc-18/SEC1 family. The encoded protein is involved in intracellular trafficking, control of SNARE (soluble NSF attachment protein receptor) complex assembly, and the release of cytotoxic granules by natural killer cells. Mutations in this gene are associated with familial hemophagocytic lymphohistiocytosis. Alternatively spliced transcript variants encoding…
- **Diseases (Open Targets)**: Familial hemophagocytic lymphohistiocytosis (0.823); autoinflammatory syndrome (0.466); hereditary hemophagocytic lymphohistiocytosis (0.372); hereditary disease (0.342); Thrombocytopenia (0.153)
- **Europe PMC papers**: 1259
- **Why important**: STXBP2 connects to TLN2 and encodes a syntaxin-binding protein involved in SNARE assembly, intracellular transport, cytotoxic-granule release, mast-cell degranulation, and neutrophil degranulation. It is tissue enhanced in lymphoid tissue and has cell-type enhancement in neutrophils, neutrophil progenitors, monocytes, and megakaryocytes. Its association with familial hemophagocytic lymphohistiocytosis and thrombocytopenia gives it strong disease relevance, while its literature base is substantial. It is therefore an important marker of a possible regulated immune-vesicle component.
- **Conclusion**: Established evidence supports STXBP2 as a regulated secretion and immune-vesicle gene. Its presence strengthens the interpretation that blood-cell composition or immune activation may contribute to the module. A direct role in the shared cervix_uterine–lung mechanism is not established, particularly because HPA protein detection was not reported in the listed tissues.

## Module 10

**Tissue pair**: cervix_uterine and lung  
**Genes (10)**: ATP5F1C, ECHS1, PRDX3, RAB10, RAB5C, RAB8A, RDH11, SEC22B, TMEM33, TMX1

### Function

The most coherent interpretation is intracellular membrane trafficking, centered on Rab-family small GTPases and endosomal or exocytic transport. RAB5C, RAB10, and RAB8A are the clearest functional core: their annotations support endocytosis, endosomal transport, exocytosis, Golgi-to-plasma-membrane transport, and endocytic recycling. SEC22B adds ER-to-Golgi trafficking and vesicle fusion, while TMX1 and TMEM33 connect the module to ER protein-folding and ER-stress biology. ECHS1, PRDX3, and ATP5F1C indicate mitochondrial fatty-acid metabolism, antioxidant protection, and oxidative phosphorylation, respectively, suggesting that the module also captures cellular energetic or stress state. No GO/KEGG term passed global correction, so no GO/KEGG enrichment is presented as statistically significant. The STRING results provide supplementary support for a Rab-trafficking interpretation through (STRING SMART Rab subfamily of small GTPases; within-query FDR = 0.0096), (STRING RCTM RAB geranylgeranylation; within-query FDR = 0.0433), and (STRING RCTM RAB GEFs exchange GTP for GDP on RABs; within-query FDR = 0.0433), but they are not globally corrected evidence.

**Cell composition.** This does not look like a predominantly plasma-protein or blood-cell module. HPA reports low immune-cell specificity for every gene and no enriched blood-cell category, arguing against a simple blood contamination explanation. The module includes two secreted genes in the HPA summary, but the individually described proteins are predominantly intracellular, membrane-associated, ER, endosomal, or mitochondrial rather than circulating proteins. Most genes have low tissue specificity, whereas a smaller subset is tissue enhanced in liver, prostate, or tongue. All genes are cell-type enhanced, with recurring signals in epithelial, parietal, trophoblast, hepatocyte, platelet, or related cell types. Protein detection is present for most genes in both cervix_uterine and lung, although some genes lack detection in one or both tissues. Thus, the shared module may reflect a broadly deployed vesicle, ER, and metabolic program, while variation in epithelial or other shared cell populations could contribute to its cross-tissue co-abundance.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest direct STRING relationship is the RAB10–RAB8A edge. STRING also groups RAB10, RAB8A, and RAB5C in the supplementary Rab-subfamily, Rab-geranylgeranylation, and Rab GEF terms (STRING SMART Rab subfamily of small GTPases; within-query FDR = 0.0096), (STRING RCTM RAB geranylgeranylation; within-query FDR = 0.0433), and (STRING RCTM RAB GEFs exchange GTP for GDP on RABs; within-query FDR = 0.0433). This is biologically coherent with the three genes' established roles in Rab-dependent vesicle transport, but the STRING enrichment is supplementary rather than globally corrected evidence. The module contains a sparse network in which RAB5C connects to RAB10, SEC22B, and PRDX3; TMX1 connects to RAB10, RDH11, and TMEM33; and ECHS1 connects to PRDX3 and ATP5F1C. hu.MAP independently places RAB5C, RAB8A, and RAB10 together in several complexes (hu.MAP huMAP3_08941.1), (hu.MAP huMAP3_09217.1), (hu.MAP huMAP3_11094.1), and (hu.MAP huMAP3_11860.1), while RAB8A and RAB10 recur in additional complexes (hu.MAP huMAP3_07302.1), (hu.MAP huMAP3_06607.1), (hu.MAP huMAP3_01895.1), and (hu.MAP huMAP3_06994.1). These complexes contain many other Rab proteins, Rab regulators, and membrane-trafficking factors. The overlap therefore supports a known Rab-centered trafficking neighborhood, but it does not establish that all module genes form one physical complex.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: RAB10–RAB8A (0.831)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Rab subfamily of small GTPases (FDR = 0.0096, 3 genes); RCTM RAB geranylgeranylation (FDR = 0.0433, 3 genes); RCTM RAB GEFs exchange GTP for GDP on RABs (FDR = 0.0433, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08941.1 (RAB5C, RAB8A, RAB10; 3/28); huMAP3_09217.1 (RAB5C, RAB8A, RAB10; 3/29); huMAP3_11094.1 (RAB5C, RAB8A, RAB10; 3/43); huMAP3_11860.1 (RAB5C, RAB8A, RAB10; 3/44); huMAP3_07302.1 (RAB8A, RAB10; 2/13); huMAP3_06607.1 (RAB8A, RAB10; 2/16); huMAP3_01895.1 (RAB8A, RAB10; 2/19); huMAP3_06994.1 (RAB8A, RAB10; 2/24)

### Novelty

The module should not be claimed as a wholly new molecular mechanism. The Rab relationships are already represented in STRING and hu.MAP, and the functions of the individual genes are established. What may be distinctive is the coordinated co-abundance of this Rab, ER, mitochondrial, and redox set across cervix_uterine and lung. The fact sheet does not provide an external cross-tissue module catalogue or prior report of this exact gene combination, so novelty of the tissue-pair association remains unresolved rather than demonstrated. Absence of STRING or hu.MAP support for several non-Rab edges cannot by itself establish novelty, because those resources emphasize physical interactions or curated complexes rather than tissue-specific co-abundance. The lack of globally significant GO/KEGG enrichment also neither proves nor disproves novelty; it mainly limits claims of pathway-level enrichment.

**Hypothesis.** Hypothesis: in shared epithelial or other common cell populations of cervix_uterine and lung, a coordinated vesicle-trafficking program couples Rab-dependent endosomal recycling and exocytosis with ER cargo handling and mitochondrial stress management. RAB5C, RAB10, and RAB8A may organize the trafficking arm; SEC22B and TMX1 may connect cargo flow to ER membrane and protein-folding processes; TMEM33 may reflect ER-stress regulation; and PRDX3, ECHS1, and ATP5F1C may reflect the energetic and oxidative demands of that state. This is a mechanistic model, not a demonstrated causal pathway. It should be tested with cell-type-resolved data, perturbation of the Rab or ER components, and direct measurements of trafficking, ER stress, mitochondrial activity, and oxidative stress.

### Important genes

#### RAB10

- **Related proteins** (co-abundance neighbors): RAB5C (0.85), RAB8A (0.81), TMX1 (0.80); STRING partners: RAB8A (0.831)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_08941.1, huMAP3_09217.1, huMAP3_11094.1, huMAP3_11860.1, huMAP3_07302.1, huMAP3_06607.1, huMAP3_01895.1, huMAP3_06994.1
- **Function (MyGene.info)**: RAB10, member RAS oncogene family. RAB10 belongs to the RAS (see HRAS; MIM 190020) superfamily of small GTPases. RAB proteins localize to exocytic and endocytic compartments and regulate intracellular vesicle trafficking (Bao et al., 1998 [PubMed 9918381]).[supplied by OMIM, Mar 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.549); digestive system disorder (0.242); cervical carcinoma (0.215); lobular capilliary hemangioma (0.165); hepatocellular carcinoma (0.109)
- **Europe PMC papers**: 2856
- **Why important**: RAB10 is a high-centrality module member connected to RAB5C, RAB8A, and TMX1. It is the sole direct STRING partner of RAB8A and occurs in all listed hu.MAP complexes (hu.MAP huMAP3_08941.1) through (hu.MAP huMAP3_06994.1). Its annotations support exocytosis, Golgi-to-plasma-membrane transport, endosomal transport, and antigen processing and presentation. It also has the largest literature volume among the selected genes and disease associations that include cervical carcinoma and neurodegenerative disease.
- **Conclusion**: Established evidence supports RAB10 as a central trafficking component and a strong marker of the module's Rab-centered architecture. It is plausible, but not proven, that RAB10 helps coordinate the shared cervix_uterine and lung co-abundance program.

#### RAB5C

- **Related proteins** (co-abundance neighbors): RAB10 (0.85), SEC22B (0.83), PRDX3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endosomes; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_08941.1, huMAP3_09217.1, huMAP3_11094.1, huMAP3_11860.1
- **Function (MyGene.info)**: RAB5C, member RAS oncogene family. Members of the Rab protein family are small GTPases of the Ras superfamily that are thought to ensure fidelity in the process of docking and/or fusion of vesicles with their correct acceptor compartment (Han et al., 1996 [PubMed 8646882]).[supplied by OMIM, Nov 2010].
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.508); hypothyroidism (0.391); hereditary disease (0.336); autoimmune thyroid disease (0.264); myxedema (0.213)
- **Europe PMC papers**: 1368
- **Why important**: RAB5C has high network centrality and connects the Rab arm to SEC22B and PRDX3, thereby linking vesicle trafficking with ER-Golgi transport and mitochondrial redox biology. Its location is reported at endosomes, and its annotations include intracellular protein transport, endocytosis, endosomal transport, and plasma-membrane-to-endosome transport. It participates with RAB8A and RAB10 in the recurring hu.MAP complexes (hu.MAP huMAP3_08941.1) through (hu.MAP huMAP3_11860.1) and in the supplementary STRING Rab terms (STRING SMART Rab subfamily of small GTPases; within-query FDR = 0.0096) through (STRING RCTM RAB GEFs exchange GTP for GDP on RABs; within-query FDR = 0.0433).
- **Conclusion**: Established evidence supports RAB5C as an endosomal trafficking anchor and a bridge between the module's functional neighborhoods. Its bridge position suggests a coordinating role, but co-abundance alone does not demonstrate that it regulates the other module genes.

#### RAB8A

- **Related proteins** (co-abundance neighbors): RAB10 (0.81); STRING partners: RAB10 (0.831)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08941.1, huMAP3_09217.1, huMAP3_11094.1, huMAP3_11860.1, huMAP3_07302.1, huMAP3_06607.1, huMAP3_01895.1, huMAP3_06994.1
- **Function (MyGene.info)**: RAB8A, member RAS oncogene family. The protein encoded by this gene is a member of the RAS superfamily which are small GTP/GDP-binding proteins with an average size of 200 amino acids. The RAS-related proteins of the RAB/YPT family may play a role in the transport of proteins from the endoplasmic reticulum to the Golgi and the plasma membrane. This protein shares 97%, 96%, and 51% similarity with the dog RAB8, mouse MEL, and mouse …
- **Diseases (Open Targets)**: acute respiratory distress syndrome (0.077); non-small cell lung carcinoma (0.076); esophageal cancer (0.076); congenital diarrhea 5 with tufting enteropathy (0.068); inflammatory bowel disease 30 (0.067)
- **Europe PMC papers**: 2105
- **Why important**: RAB8A is part of the recurring RAB5C–RAB8A–RAB10 hu.MAP membership and has the direct STRING relationship with RAB10. Its annotations support exocytosis, Golgi organization, endocytic recycling, autophagy regulation, and cellular response to insulin stimulus. Although its direct module connectivity is limited, its repeated complex membership makes it an important functional representative of the Rab trafficking core, and it has substantial literature support.
- **Conclusion**: Established evidence supports RAB8A as a known exocytic and recycling component of the Rab core. Its repeated complex membership strengthens the trafficking interpretation, but does not show that RAB8A is the driver of the tissue-pair module.

#### TMX1

- **Related proteins** (co-abundance neighbors): RDH11 (0.85), TMEM33 (0.82), RAB10 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin related transmembrane protein 1. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, a catalytically active thioredoxin domain, and one transmembrane domain. Unlike most members of this gene family, it lacks a C-terminal ER-retention sequence. The …
- **Diseases (Open Targets)**: adolescent idiopathic scoliosis (0.247); Alkalosis (0.193); cutaneous lupus erythematosus (0.180); cleft lip (0.137); cleft palate (0.106)
- **Europe PMC papers**: 415
- **Why important**: TMX1 has high network centrality and is the principal connection between RAB10 and the RDH11–TMEM33 branch. It is an ER transmembrane thioredoxin-related protein involved in disulfide-bond handling, ER stress, calcium transport, ER-associated degradation, and regulation of platelet aggregation. Its HPA localization is intracellular and membrane-associated in the ER, and its literature and disease-association support are substantial enough to make it more than a generic connector.
- **Conclusion**: Established evidence supports TMX1 as an ER proteostasis and membrane component that could connect trafficking to folding or stress responses. Its proposed role as the molecular bridge between Rab trafficking and ER stress in this module remains a hypothesis.

#### PRDX3

- **Related proteins** (co-abundance neighbors): ECHS1 (0.83), RAB5C (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Mitochondria; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peroxiredoxin 3. This gene encodes a mitochondrial protein with antioxidant function. The protein is similar to the C22 subunit of Salmonella typhimurium alkylhydroperoxide reductase, and it can rescue bacterial resistance to alkylhydroperoxide in E. coli that lack the C22 subunit. The human and mouse genes are highly conserved, and they map to the regions syntenic between mouse and human chromosomes. Sequence com…
- **Diseases (Open Targets)**: spinocerebellar ataxia, autosomal recessive 32 (0.653); corneal dystrophy, punctiform and polychromatic pre-descemet (0.571); autosomal recessive cerebellar ataxia (0.268); neurodegenerative disease (0.257); hereditary disease (0.191)
- **Europe PMC papers**: 2613
- **Why important**: PRDX3 connects RAB5C with ECHS1 and therefore links the trafficking-centered portion of the module to mitochondrial metabolism. It is a mitochondrial antioxidant protein annotated for oxidative-stress response and mitochondrion organization. It is detected in both tissues, is cell-type enhanced across several metabolically active or secretory cell types, and has extensive literature and disease-association support.
- **Conclusion**: Established evidence supports PRDX3 as a mitochondrial redox component and a plausible indicator of oxidative or energetic state. Its position suggests that redox control may be coordinated with trafficking in the module, but the causal direction and biological coupling are unproven.

## Module 11

**Tissue pair**: cervix_uterine and lung  
**Genes (38)**: ATXN10, CLTC, CLUH, CPSF3, DIAPH1, ADAR, FLII, FLNB, GANAB, GNL3, SLC2A1, HNRNPL, INF2, NUP214, NUP50, NUP98, OSBPL9, PPM1G, PRPF31, CAD, RAB3GAP2, RBM10, RBM12, PDCD11, SEC23IP, SEPTIN9, SIN3A, SMARCA4, SNW1, SPTBN1, SPTAN1, SRP68, CARS1, VARS1, UBR5, XPO7, ZFR, ZNF326

### Function

The best-supported function is RNA-centered nuclear information processing. The primary globally corrected terms are RNA binding (GO:MF RNA binding; q_global = 0.000293) and nucleic acid binding (GO:MF nucleic acid binding; q_global = 0.0144), with the same genes driving both signals. The module includes established components of RNA splicing and processing, including HNRNPL, RBM10, PRPF31, CPSF3, RBM12, SNW1, and ZFR; RNA editing through ADAR; ribosomal RNA maturation through PDCD11; RNA export and nucleocytoplasmic transport through NUP98, NUP214, NUP50, and XPO7; and transcriptional or chromatin regulation through SMARCA4, SIN3A, and ZNF326. Thus, the module most plausibly represents coordinated expression of RNA-binding, RNA-processing, nuclear-transport, and gene-regulatory machinery rather than a single narrow biochemical pathway. The STRING RNA-binding enrichment (STRING Function RNA binding; within-query FDR = 0.00015) is concordant supplementary evidence, while the phosphoprotein keyword (STRING Keyword Phosphoprotein; within-query FDR = 0.0014) is less specific and should not be treated as primary functional evidence. The absence of additional globally corrected GO or KEGG terms does not invalidate the module.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary identifies only a single secreted gene, and most annotated proteins are intracellular, with nuclear, nucleolar, cytosolic, vesicular, endoplasmic-reticulum, or cytoskeletal locations. The genes are generally broadly expressed, with low tissue specificity for most of the module and low immune-cell specificity for nearly all genes. HPA does show cell-type-enhanced signals in several epithelial, reproductive, neural, and structural cell populations, including neutrophils, but the module is not broadly blood-cell enriched. Therefore, a simple plasma contamination explanation is unlikely. Shared abundance may instead reflect common expression of conserved housekeeping and RNA-processing machinery, with contributions from shared epithelial or stromal cell states. HPA protein detection in both cervix_uterine and lung for many genes supports biological detectability in both tissues, while tissue-specific absences for some genes argue against interpreting every member as a universal component of both tissues.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF RNA binding | 0.000293 | ADAR, CARS1, CLTC, CLUH, CPSF3, DIAPH1, FLNB, GANAB, GNL3, HNRNPL, NUP98, PDCD11, PRPF31, RBM10, RBM12, SEC23IP, SIN3A, SMARCA4, SNW1, SPTBN1, SRP68, UBR5, ZFR, ZNF326 |
| GO:MF nucleic acid binding | 0.0144 | ADAR, CARS1, CLTC, CLUH, CPSF3, DIAPH1, FLNB, GANAB, GNL3, HNRNPL, NUP98, PDCD11, PRPF31, RBM10, RBM12, SEC23IP, SIN3A, SMARCA4, SNW1, SPTBN1, SRP68, UBR5, ZFR, ZNF326 |

### STRING and hu.MAP

STRING provides a connected but partial molecular framework. The strongest known relationships include the nucleoporin links NUP214–NUP98 and NUP214–NUP50, the chromatin-regulatory link SIN3A–SMARCA4, the GNL3–SMARCA4 and GNL3–PDCD11 links, the aminoacyl-tRNA synthetase link CARS1–VARS1, the PDCD11–VARS1 link, and the spectrin pair SPTAN1–SPTBN1. These relationships support genuine molecular organization within parts of the module, but most co-abundance edges are not represented by high-confidence STRING interactions. hu.MAP independently supports several substructures: HNRNPL, ADAR, ZNF326, and ZFR occur together in an RNA-associated complex (hu.MAP huMAP3_10625.1), with related hnRNP composition in (hu.MAP huMAP3_07581.1), while NUP214, NUP98, and NUP50 recur in nuclear-pore complexes (hu.MAP huMAP3_10000.1) and (hu.MAP huMAP3_12581.1). CARS1 and VARS1 recur in translation-related complexes (hu.MAP huMAP3_06945.1), (hu.MAP huMAP3_04189.1), (hu.MAP huMAP3_00469.1), and (hu.MAP huMAP3_12041.1); SPTAN1 and SPTBN1 recur in spectrin-associated complexes (hu.MAP huMAP3_07940.1), (hu.MAP huMAP3_05473.1), and (hu.MAP huMAP3_09165.1); and OSBPL9 with RAB3GAP2 occurs in membrane-trafficking complexes (hu.MAP huMAP3_11506.1) and (hu.MAP huMAP3_11485.1). Together, these results indicate that the module contains several known molecular neighborhoods connected by coordinated abundance, rather than being one experimentally established protein complex.

**STRING interactions (score >= 0.7)**: 9 of 703 gene pairs: CARS1–VARS1 (0.872); GNL3–PDCD11 (0.778); GNL3–SMARCA4 (0.878); NUP214–NUP50 (0.966); NUP214–NUP98 (0.999); NUP50–NUP98 (0.949); PDCD11–VARS1 (0.805); SIN3A–SMARCA4 (0.948); SPTAN1–SPTBN1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function RNA binding (FDR = 0.00015, 24 genes); Keyword Phosphoprotein (FDR = 0.0014, 38 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10625.1 (HNRNPL, ADAR, ZNF326, ZFR; 4/57); huMAP3_07581.1 (HNRNPL, ZNF326, ZFR; 3/21); huMAP3_10000.1 (NUP214, NUP98, NUP50; 3/44); huMAP3_12581.1 (NUP214, NUP98, NUP50; 3/58); huMAP3_06945.1 (VARS1, CARS1; 2/4); huMAP3_05948.1 (NUP214, NUP98; 2/5); huMAP3_07940.1 (SPTBN1, SPTAN1; 2/5); huMAP3_04189.1 (VARS1, CARS1; 2/6); huMAP3_05473.1 (SPTBN1, SPTAN1; 2/7); huMAP3_06671.1 (HNRNPL, ZNF326; 2/8); huMAP3_06369.1 (NUP214, NUP98; 2/12); huMAP3_00469.1 (VARS1, CARS1; 2/12); huMAP3_09654.1 (HNRNPL, ZNF326; 2/13); huMAP3_12041.1 (VARS1, CARS1; 2/16); huMAP3_11506.1 (OSBPL9, RAB3GAP2; 2/17); huMAP3_11485.1 (OSBPL9, RAB3GAP2; 2/26); huMAP3_10659.1 (HNRNPL, ZNF326; 2/28); huMAP3_09165.1 (SPTBN1, SPTAN1; 2/39)

### Novelty

The module should not be described as a newly discovered molecular complex. Several of its internal relationships and subassemblies are already represented in STRING and hu.MAP, especially the RNA-binding, nuclear-pore, spectrin, and aminoacyl-tRNA-synthetase neighborhoods. At the same time, the particular conserved co-abundance organization shared by cervix_uterine and lung is not established by these resources. Its potential novelty is therefore at the level of tissue-pair co-abundance and cross-subsystem coordination, not at the level of individual protein interactions. Absence of an edge from STRING or hu.MAP is not evidence of novelty, because those databases are incomplete and measure physical or curated interactions rather than tissue co-abundance. The finding should be considered a biologically coherent, potentially novel expression module requiring independent replication and perturbation-based testing.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular program that couples RNA handling to the demands of maintaining differentiated epithelial or stromal cells in cervix_uterine and lung. In this model, ZFR, HNRNPL, ZNF326, RBM10, ADAR, CPSF3, and PRPF31 coordinate RNA binding, editing, splicing, and transcript maturation; NUP98, NUP214, and NUP50 regulate exchange of RNA and regulatory proteins across the nuclear pore; SMARCA4 and SIN3A connect RNA output to chromatin and transcriptional state; and cytoskeletal or trafficking components provide cell-structural and membrane-transport support. The coordinated abundance may therefore mark a shared requirement for RNA quality control and gene-expression plasticity rather than a tissue-specific pathway. This remains a hypothesis: the co-abundance data do not establish physical interaction, directionality, or causal regulation.

### Important genes

#### ZFR

- **Related proteins** (co-abundance neighbors): CPSF3 (0.93), ZNF326 (0.91), RAB3GAP2 (0.85), SEC23IP (0.84), NUP98 (0.84), CARS1 (0.84), CLUH (0.83), SPTAN1 (0.82), VARS1 (0.81), OSBPL9 (0.81), PDCD11 (0.81), SIN3A (0.81), ADAR (0.81), SNW1 (0.81), PRPF31 (0.81), FLII (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_07581.1
- **Function (MyGene.info)**: zinc finger RNA binding protein. This gene encodes an RNA-binding protein characterized by its DZF (domain associated with zinc fingers) domain. The encoded protein may play a role in the nucleocytoplasmic shuttling of another RNA-binding protein, Staufen homolog 2, in neurons. Expression of this gene is regulated through alternative polyadenylation that mediates differential microRNA targeting. Elevated expression of this gene h…
- **Diseases (Open Targets)**: neurodegenerative disease (0.483); autosomal recessive spastic paraplegia type 71 (0.370); hyperaldosteronism (0.320); placental abruption (0.311); hearing loss disorder (0.242)
- **Europe PMC papers**: 793
- **Why important**: ZFR is the strongest network hub in the module and connects RNA-processing genes with nucleoporins, translation-related genes, vesicle-associated genes, and cytoskeletal genes. It is annotated as a zinc-finger RNA-binding protein, is present in the primary terms (GO:MF RNA binding; q_global = 0.000293) and (GO:MF nucleic acid binding; q_global = 0.0144) and the supplementary STRING terms (STRING Function RNA binding; within-query FDR = 0.00015) and (STRING Keyword Phosphoprotein; within-query FDR = 0.0014), and participates in the hu.MAP RNA-associated assemblies (hu.MAP huMAP3_10625.1) and (hu.MAP huMAP3_07581.1). Its broad HPA profile and detection in both tissues make it a strong candidate for the shared module backbone. The gene has substantial literature and disease links including neurodegenerative disease and spastic paraplegia.
- **Conclusion**: Established evidence supports ZFR as a central RNA-associated hub and a plausible coordinator of several module neighborhoods. It is reasonable to prioritize ZFR as a module marker. It is not established that ZFR drives the shared tissue pattern or directly links all of the observed subsystems.

#### ZNF326

- **Related proteins** (co-abundance neighbors): ZFR (0.91), XPO7 (0.87), NUP98 (0.85), VARS1 (0.82), ADAR (0.81), NUP50 (0.81), HNRNPL (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_07581.1, huMAP3_06671.1, huMAP3_09654.1, huMAP3_10659.1
- **Function (MyGene.info)**: zinc finger protein 326. Enables RNA polymerase II complex binding activity. Involved in regulation of DNA-templated transcription, elongation and regulation of RNA splicing. Located in nucleoplasm. Part of DBIRD complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: ocular hypotension (0.227); insomnia (0.222); adolescent idiopathic scoliosis (0.207); juvenile dermatomyositis (0.205); major depressive disorder (0.205)
- **Europe PMC papers**: 258
- **Why important**: ZNF326 has a prominent network position and connects ZFR to XPO7, NUP98, VARS1, ADAR, NUP50, and HNRNPL. It is present in (GO:MF RNA binding; q_global = 0.000293), (GO:MF nucleic acid binding; q_global = 0.0144), (STRING Function RNA binding; within-query FDR = 0.00015), and (STRING Keyword Phosphoprotein; within-query FDR = 0.0014), occurs in multiple hu.MAP RNA-associated complexes (hu.MAP huMAP3_10625.1), (hu.MAP huMAP3_07581.1), (hu.MAP huMAP3_06671.1), (hu.MAP huMAP3_09654.1), and (hu.MAP huMAP3_10659.1), and is annotated as a regulator of transcription elongation and RNA splicing. Its tissue-enhanced retinal and cell-type-enhanced photoreceptor expression suggest regulated cell-state specialization, although its overall module context is broader.
- **Conclusion**: Established evidence supports ZNF326 as a bridge between RNA-associated complexes, nuclear transport, and transcriptional regulation. It is a plausible integrator of the module's nuclear functions. A direct role in the cervix_uterine–lung shared state remains hypothetical.

#### SMARCA4

- **Related proteins** (co-abundance neighbors): SPTAN1 (0.89), FLII (0.85), RBM10 (0.85), NUP214 (0.82), SEPTIN9 (0.81), SPTBN1 (0.81); STRING partners: GNL3 (0.878), SIN3A (0.948)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center, Nucleoli rim; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SWI/SNF related BAF chromatin remodeling complex subunit ATPase 4. The protein encoded by this gene is a member of the SWI/SNF family of proteins and is similar to the brahma protein of Drosophila. Members of this family have helicase and ATPase activities and are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI, wh…
- **Diseases (Open Targets)**: intellectual disability, autosomal dominant 16 (0.796); rhabdoid tumor predisposition syndrome 2 (0.788); familial rhabdoid tumor (0.685); rhabdoid tumor (0.627); medulloblastoma (0.586)
- **Europe PMC papers**: 9906
- **Why important**: SMARCA4 links the RNA-centered portion of the module to chromatin remodeling and structural proteins. It is present in (GO:MF RNA binding; q_global = 0.000293), (GO:MF nucleic acid binding; q_global = 0.0144), (STRING Function RNA binding; within-query FDR = 0.00015), and (STRING Keyword Phosphoprotein; within-query FDR = 0.0014), connects in STRING to GNL3 and SIN3A, and is annotated as the ATPase subunit of the SWI/SNF-related BAF chromatin-remodeling complex. Its disease associations include rhabdoid tumor predisposition and intellectual disability, and it has extensive literature. HPA detects the protein in both tissues and places it in the nucleoplasm and nucleolar compartments.
- **Conclusion**: Established evidence supports SMARCA4 as a transcriptional and chromatin-regulatory anchor within the module. Its network links to RNA and cytoskeletal genes support a broad gene-expression program. The data do not show that chromatin remodeling is the initiating cause of the co-abundance pattern.

#### NUP98

- **Related proteins** (co-abundance neighbors): ZNF326 (0.85), RBM10 (0.85), ZFR (0.84), RBM12 (0.83); STRING partners: NUP214 (0.999), NUP50 (0.949)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10000.1, huMAP3_12581.1, huMAP3_05948.1, huMAP3_06369.1
- **Function (MyGene.info)**: nucleoporin 98 and 96 precursor. Nuclear pore complexes (NPCs) regulate the transport of macromolecules between the nucleus and cytoplasm, and are composed of many polypeptide subunits, many of which belong to the nucleoporin family. This gene belongs to the nucleoporin gene family and encodes a 186 kDa precursor protein that undergoes autoproteolytic cleavage to generate a 98 kDa nucleoporin and 96 kDa nucleoporin. The 98 kDa nu…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); acute myeloid leukemia (0.399); lung carcinoma (0.376)
- **Europe PMC papers**: 4839
- **Why important**: NUP98 is a nucleoporin with links to ZNF326, RBM10, ZFR, and RBM12 in the module. It forms high-confidence STRING relationships with NUP214 and NUP50 and recurs in the hu.MAP nuclear-pore assemblies (hu.MAP huMAP3_10000.1), (hu.MAP huMAP3_12581.1), (hu.MAP huMAP3_05948.1), and (hu.MAP huMAP3_06369.1). Its established functions include RNA export, protein import and export, nucleocytoplasmic transport, and nuclear-pore organization. It also has extensive literature and disease associations involving viral infection and acute myeloid leukemia.
- **Conclusion**: Established evidence supports NUP98 as the clearest nuclear-transport anchor and as part of a known nucleoporin subassembly inside the module. Its presence makes coordinated control of nuclear–cytoplasmic exchange plausible. It does not establish that altered transport is responsible for the tissue-pair conservation.

#### ADAR

- **Related proteins** (co-abundance neighbors): PDCD11 (0.86), ZFR (0.81), ZNF326 (0.81), UBR5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_10625.1
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR provides a distinctive functional capability within the module: site-specific adenosine-to-inosine RNA editing and response to viral stimuli. It is included in (GO:MF RNA binding; q_global = 0.000293), (GO:MF nucleic acid binding; q_global = 0.0144), (STRING Function RNA binding; within-query FDR = 0.00015), and (STRING Keyword Phosphoprotein; within-query FDR = 0.0014), connects to ZFR, ZNF326, PDCD11, and UBR5, and appears with ZFR and ZNF326 in hu.MAP complex (hu.MAP huMAP3_10625.1). HPA places it in the nucleolus, detects it in both tissues, and shows cell-type enhancement in neutrophils. Its extensive literature and strong disease associations with Aicardi–Goutières syndrome and ADAR-related interferonopathy make it biologically important.
- **Conclusion**: Established evidence supports ADAR as an RNA-editing and innate-response component that may connect RNA metabolism with cellular stress or antiviral biology. Its co-abundance with RNA-binding and transport genes is consistent with coordinated RNA surveillance. Activation of an antiviral program in these tissues is only a hypothesis and is not demonstrated by the module alone.

## Module 12

**Tissue pair**: cervix_uterine and lung  
**Genes (37)**: CCAR1, CHERP, CPSF6, GPS1, DDX42, DDX46, FEN1, GTF2I, HARS1, HLTF, EIF5, KPNA2, IPO4, MCM2, MCM4, MCM5, MCM7, MRE11, MSH2, MSH6, NAA15, NASP, NSUN2, NUP155, NUP205, NUP88, NUP93, PFAS, CTPS1, RAD50, SF3A1, SRRT, TARS1, TCERG1, TNPO3, XPO1, XPO5

### Function

This is a nuclear genome-maintenance and gene-expression module. The strongest primary evidence supports nuclear protein-containing complexes and nucleic-acid-directed catalytic activity (5 globally significant GO/KEGG terms, q_global 6.64e-05–0.000158; see the table). A prominent functional axis is DNA replication and replication initiation, centered on the MCM genes, together with DNA recombination and repair (19 globally significant GO/KEGG terms, q_global 0.000331–0.0195; see the table). A second axis is nucleocytoplasmic transport, including nuclear pore components, importins, and exportins (13 globally significant GO/KEGG terms, q_global 0.000189–0.0279; see the table). RNA processing, RNA localization, and RNA export are also represented, consistent with the presence of spliceosome-associated and RNA-processing proteins (9 globally significant GO/KEGG terms, q_global 0.000238–0.0279; see the table). The STRING supplementary results independently show the same broad organization around the nucleus, nucleic-acid metabolism, DNA repair, and capped pre-mRNA processing (15 supplementary STRING terms; within-query FDR 6.96e-06–0.00044). Overall, the module is best interpreted as a coordinated nuclear infrastructure program linking DNA replication and repair with RNA processing and regulated traffic through the nuclear envelope.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: the HPA summary identifies only a single secreted gene, while the proteins represented here are mainly nuclear, nucleoplasmic, nuclear membrane, or cytosolic components of intracellular processes. Protein detection is broadly concordant in cervix_uterine and lung, although selected genes lack detection in one or both tissues. Most genes have low tissue specificity and almost all have low immune-cell specificity, arguing against a simple plasma-protein or blood-leukocyte module. Nevertheless, many genes are cell-type enhanced in erythrocyte progenitors, megakaryocyte progenitors, or other developing cell populations, and several are enhanced in germ-cell populations. The pattern is therefore compatible with broadly expressed housekeeping and proliferative nuclear machinery, with possible contributions from shared cycling or progenitor-like cell states in the tissue samples. It should not be interpreted as evidence that the module is specific to cervix_uterine or lung parenchymal cells without cell-composition and spatial validation.

**GO/KEGG enrichment**: 47 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC nuclear protein-containing complex | 6.64e-05 | CPSF6, DDX42, DDX46, GPS1, HLTF, MCM2, MCM4, MCM5, MCM7, MRE11, MSH2, MSH6, NUP155, NUP205, NUP88, NUP93, RAD50, SF3A1 |
| GO:MF ATP-dependent activity, acting on DNA | 7.85e-05 | HLTF, MCM2, MCM4, MCM5, MCM7, MRE11, MSH2, MSH6, RAD50 |
| GO:MF nucleic acid binding | 0.000125 | CCAR1, CHERP, CPSF6, DDX42, DDX46, EIF5, FEN1, GTF2I, HARS1, HLTF, KPNA2, MCM2, MCM4, MCM5, MCM7, MRE11, MSH2, MSH6, NAA15, NSUN2, RAD50, SF3A1, SRRT, TARS1, TCERG1, XPO1, XPO5 |
| GO:MF catalytic activity, acting on DNA | 0.000126 | FEN1, HLTF, MCM2, MCM4, MCM5, MCM7, MRE11, MSH2, MSH6, RAD50 |
| GO:MF catalytic activity, acting on a nucleic acid | 0.000158 | DDX42, DDX46, FEN1, HARS1, HLTF, MCM2, MCM4, MCM5, MCM7, MRE11, MSH2, MSH6, NSUN2, RAD50, TARS1 |
| KEGG Nucleocytoplasmic transport - Homo sapiens (human) | 0.000189 | IPO4, KPNA2, NUP155, NUP205, NUP88, NUP93, TNPO3, XPO1, XPO5 |
| GO:BP nucleic acid metabolic process | 0.000238 | CCAR1, CHERP, CPSF6, DDX42, DDX46, FEN1, GTF2I, HARS1, HLTF, KPNA2, MCM2, MCM4, MCM5, MCM7, MRE11, MSH2, MSH6, NAA15, NASP, NSUN2, NUP155, RAD50, SF3A1, SRRT, TARS1, TCERG1, XPO5 |
| GO:CC nuclear lumen | 0.000265 | CCAR1, CHERP, CPSF6, DDX42, DDX46, FEN1, GPS1, GTF2I, HLTF, KPNA2, MCM2, MCM4, MCM5, MCM7, MRE11, MSH2, MSH6, NAA15, NASP, NSUN2, NUP205, NUP88, NUP93, RAD50, SF3A1, SRRT, TCERG1, TNPO3, XPO1, XPO5 |
| GO:BP DNA recombination | 0.000331 | FEN1, KPNA2, MCM2, MCM4, MCM5, MCM7, MRE11, MSH2, MSH6, RAD50 |
| GO:MF helicase activity | 0.000491 | DDX42, DDX46, HLTF, MCM2, MCM4, MCM5, MCM7, MRE11, RAD50 |
| GO:CC nucleoplasm | 0.000515 | CCAR1, CHERP, CPSF6, DDX42, DDX46, FEN1, GPS1, GTF2I, HLTF, KPNA2, MCM2, MCM4, MCM5, MCM7, MRE11, MSH2, MSH6, NAA15, NASP, NSUN2, NUP88, RAD50, SF3A1, SRRT, TCERG1, TNPO3, XPO1, XPO5 |
| GO:BP nucleocytoplasmic transport | 0.000562 | CPSF6, IPO4, KPNA2, NSUN2, NUP155, NUP205, NUP88, NUP93, TNPO3, XPO1, XPO5 |
| GO:BP nuclear transport | 0.000562 | CPSF6, IPO4, KPNA2, NSUN2, NUP155, NUP205, NUP88, NUP93, TNPO3, XPO1, XPO5 |
| GO:MF nucleic acid conformation isomerase activity | 0.000582 | DDX42, DDX46, HLTF, MCM2, MCM4, MCM5, MCM7, MRE11, RAD50 |
| GO:BP RNA export from nucleus | 0.000963 | CPSF6, NSUN2, NUP155, NUP88, NUP93, XPO1, XPO5 |

### STRING and hu.MAP

STRING contains many high-confidence relationships that are already expected from established molecular systems. The MCM2–MCM4–MCM5–MCM7 group is tightly connected, and FEN1, MSH2, MSH6, MRE11, and RAD50 connect this replication machinery to DNA repair. The nucleoporin group NUP155, NUP205, NUP88, and NUP93 is strongly interconnected and linked to XPO1 and XPO5, while IPO4, KPNA2, and TNPO3 represent import or transport connections. SF3A1, DDX42, DDX46, TCERG1, CHERP, CCAR1, SRRT, and CPSF6 provide established RNA-processing and splicing relationships (STRING Component Nuclear protein-containing complex; within-query FDR = 7.03e-05) (STRING RCTM Processing of Capped Intron-Containing Pre-mRNA; within-query FDR = 8.04e-05). hu.MAP independently recovers multiple MCM-containing replication complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1), the MRE11–RAD50 complex (hu.MAP huMAP3_11272.1) (hu.MAP huMAP3_14612.1), nucleoporin and transport assemblies (hu.MAP huMAP3_09042.1) (hu.MAP huMAP3_12581.1) (hu.MAP huMAP3_08764.1) (hu.MAP huMAP3_07789.1), and spliceosomal or RNA-processing assemblies (hu.MAP huMAP3_10359.1) (hu.MAP huMAP3_04549.1) (hu.MAP huMAP3_12581.1) (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_06511.1). These overlaps show that the co-abundance structure is strongly anchored in known protein complexes and pathways. They support biological coherence, but they also mean that much of the module's molecular connectivity is not newly discovered by this network.

**STRING interactions (score >= 0.7)**: 52 of 666 gene pairs: CCAR1–SRRT (0.857); CCAR1–TCERG1 (0.92); CHERP–DDX46 (0.859); CHERP–SF3A1 (0.818); CPSF6–SRRT (0.732); CPSF6–TNPO3 (0.87); DDX42–SF3A1 (0.903); DDX46–SF3A1 (0.999); DDX46–TCERG1 (0.927); FEN1–KPNA2 (0.858); FEN1–MCM2 (0.912); FEN1–MCM4 (0.941); FEN1–MCM5 (0.942); FEN1–MCM7 (0.903); FEN1–MRE11 (0.984); FEN1–MSH2 (0.948); FEN1–MSH6 (0.95); FEN1–RAD50 (0.844); HARS1–TARS1 (0.865); IPO4–NASP (0.775); IPO4–XPO1 (0.714); IPO4–XPO5 (0.713); KPNA2–XPO1 (0.832); KPNA2–XPO5 (0.708); MCM2–MCM4 (0.999); MCM2–MCM5 (0.999); MCM2–MCM7 (0.999); MCM4–MCM5 (0.999); MCM4–MCM7 (0.999); MCM4–MSH6 (0.735); MCM5–MCM7 (0.999); MCM5–MSH6 (0.749); MCM7–MSH2 (0.71); MCM7–NASP (0.81); MRE11–MSH2 (0.847); MRE11–MSH6 (0.862); MRE11–RAD50 (0.999); MSH2–MSH6 (0.999); NUP155–NUP205 (0.999); NUP155–NUP88 (0.995); NUP155–NUP93 (0.999); NUP155–XPO1 (0.769); NUP205–NUP88 (0.995); NUP205–NUP93 (0.999); NUP205–XPO5 (0.755); NUP88–NUP93 (0.995); NUP88–XPO1 (0.997); NUP93–XPO1 (0.712); SF3A1–TCERG1 (0.992); SRRT–TCERG1 (0.839); TNPO3–XPO1 (0.764); XPO1–XPO5 (0.752)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Nucleus (FDR = 6.96e-06, 30 genes); Function Catalytic activity, acting on a nucleic acid (FDR = 1.9e-05, 15 genes); Function Catalytic activity, acting on DNA (FDR = 2.61e-05, 10 genes); Process Nucleic acid metabolic process (FDR = 2.73e-05, 24 genes); COMPARTMENTS Nucleus (FDR = 6.7e-05, 31 genes); Component Nuclear protein-containing complex (FDR = 7.03e-05, 17 genes); RCTM Processing of Capped Intron-Containing Pre-mRNA (FDR = 8.04e-05, 12 genes); Function Nucleic acid binding (FDR = 0.00015, 26 genes); Function ATP-dependent activity, acting on DNA (FDR = 0.00015, 8 genes); Component Nuclear lumen (FDR = 0.00017, 29 genes); Component Chromosome, telomeric region (FDR = 0.00022, 8 genes); Component Nucleoplasm (FDR = 0.00022, 27 genes); Process Nucleobase-containing compound metabolic process (FDR = 0.00025, 26 genes); Process DNA recombination (FDR = 0.00026, 9 genes); Process Double-strand break repair (FDR = 0.00044, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05529.1 (MCM4, MCM5, MCM7, MCM2; 4/6); huMAP3_14758.1 (MCM4, MCM5, MCM7, MCM2; 4/14); huMAP3_08554.1 (MCM4, MCM5, MCM7, MCM2; 4/15); huMAP3_11832.1 (MCM4, MCM5, MCM7, MCM2; 4/15); huMAP3_12180.1 (MCM4, MCM5, MCM7, MCM2; 4/17); huMAP3_09042.1 (XPO1, MSH6, NUP93, NUP205; 4/26); huMAP3_06061.1 (MCM4, MCM7, MCM2; 3/5); huMAP3_07113.1 (MCM4, MCM7, MCM2; 3/6); huMAP3_11119.1 (MCM4, MCM5, MCM7; 3/14); huMAP3_13998.1 (TCERG1, FEN1, EIF5; 3/23); huMAP3_10747.1 (NASP, MCM2, IPO4; 3/25); huMAP3_10359.1 (SF3A1, CHERP, CCAR1; 3/27); huMAP3_04549.1 (SF3A1, DDX46, DDX42; 3/52); huMAP3_12581.1 (NUP155, KPNA2, NUP88; 3/58); huMAP3_08980.1 (SF3A1, DDX46, DDX42; 3/97); huMAP3_09860.1 (MCM4, MCM2; 2/4); huMAP3_11272.1 (MRE11, RAD50; 2/4); huMAP3_00154.1 (MCM4, MCM2; 2/5); huMAP3_08764.1 (XPO1, MSH6; 2/7); huMAP3_07789.1 (NUP93, NUP205; 2/7); huMAP3_14612.1 (MRE11, RAD50; 2/8); huMAP3_09238.1 (MCM5, MCM7; 2/11); huMAP3_05673.1 (NUP93, NUP205; 2/11); huMAP3_05517.1 (NASP, IPO4; 2/13); huMAP3_06020.1 (NASP, IPO4; 2/13); huMAP3_07170.1 (XPO1, MSH6; 2/14); huMAP3_05832.1 (XPO5, TNPO3; 2/14); huMAP3_06077.1 (XPO5, TNPO3; 2/15); huMAP3_08143.1 (NASP, IPO4; 2/21); huMAP3_09466.1 (MCM4, MCM2; 2/23); huMAP3_09859.1 (NASP, IPO4; 2/24); huMAP3_08298.1 (XPO5, TNPO3; 2/24); huMAP3_09053.1 (XPO5, TNPO3; 2/25); huMAP3_14982.1 (FEN1, EIF5; 2/28); huMAP3_09114.1 (XPO5, TNPO3; 2/30); huMAP3_06791.1 (XPO1, NUP205; 2/31); huMAP3_10862.1 (MCM4, MCM2; 2/33); huMAP3_12711.1 (NASP, IPO4; 2/35); huMAP3_10000.1 (KPNA2, NUP88; 2/44); huMAP3_10202.1 (XPO5, TNPO3; 2/52); huMAP3_10287.1 (XPO5, TNPO3; 2/53); huMAP3_14306.1 (MCM4, MCM2; 2/55); huMAP3_06511.1 (SF3A1, DDX46; 2/79)

### Novelty

The conserved co-abundance module may be a useful new observation at the level of tissue-pair organization, because it brings replication, repair, RNA processing, and nucleocytoplasmic transport into one shared cervix_uterine–lung expression pattern. However, the underlying biology is not a new molecular mechanism: the principal submodules, including the MCM complex, MRE11–RAD50 repair machinery, nuclear pore components, exportins, and spliceosomal proteins, are supported by established STRING relationships, hu.MAP complexes, and gene annotations. Absence of some module pairs from STRING or hu.MAP would not establish novelty, since co-abundance is not equivalent to physical interaction and database coverage is incomplete. The defensible claim is therefore a potentially novel cross-tissue co-abundance configuration of largely known machinery, not discovery of a new complex or pathway. Independent cohorts, cell-type-aware analyses, perturbation, and protein-level validation would be needed to establish whether the shared module reflects a reproducible biological state rather than common proliferation or sample composition.

**Hypothesis.** Hypothesis: the module reflects a shared state of nuclear activity in which cycling or progenitor-like cells coordinate genome duplication, replication-associated damage surveillance, repair, RNA maturation, and nucleocytoplasmic exchange. The MCM replication apparatus and FEN1–MSH2–MSH6–MRE11–RAD50 repair axis could support replication-fork progression and lesion resolution, while NUP93 and its nucleoporin partners, together with XPO1, XPO5, and import receptors, could regulate delivery and export of the required factors and RNA products. Splicing and RNA-processing components could couple transcriptional output to this nuclear state. This is a mechanistic model rather than proof of direct coordination; the co-abundance data cannot by itself establish physical interaction, causal direction, cell-cycle phase, or tissue-specific activity.

### Important genes

#### MCM7

- **Related proteins** (co-abundance neighbors): MCM2 (0.91), NUP93 (0.88), MCM5 (0.87), PFAS (0.85), NASP (0.85), NUP155 (0.83), KPNA2 (0.83), MSH2 (0.83); STRING partners: FEN1 (0.903), MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MSH2 (0.71), NASP (0.81)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 is a prominent network hub and a central member of the MCM replication group. It participates in a large set of globally supported terms covering DNA replication, helicase activity, replication initiation, recombinational repair, and the MCM, preinitiation, and CMG complexes (29 globally significant GO/KEGG terms, q_global 6.64e-05–0.0339; see the table). Its strong STRING links to MCM2, MCM4, MCM5, FEN1, MSH2, and NASP and its repeated hu.MAP membership make it a structural and functional anchor. It also has substantial disease and literature support, including replication-associated developmental and genomic-stability disorders.
- **Conclusion**: Established evidence identifies MCM7 as a replication-fork and DNA-maintenance component that helps explain the module's core function. The module data support coordinated abundance of MCM7 with repair and transport machinery, but do not show that MCM7 directly regulates the tissue phenotype.

#### NUP93

- **Related proteins** (co-abundance neighbors): SF3A1 (0.90), MCM7 (0.88), TARS1 (0.84), MCM5 (0.84), NUP205 (0.83), DDX42 (0.83), GPS1 (0.83), TCERG1 (0.83), RAD50 (0.82), NASP (0.82), FEN1 (0.81); STRING partners: NUP155 (0.999), NUP205 (0.999), NUP88 (0.995), XPO1 (0.712)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_09042.1, huMAP3_07789.1, huMAP3_05673.1
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 is among the most connected genes in the co-abundance graph and links the nuclear pore branch to MCM, RNA-processing, and other nuclear proteins. It appears across the globally supported nuclear lumen, nuclear transport, RNA export, and nucleocytoplasmic transport terms (16 globally significant GO/KEGG terms, q_global 6.64e-05–0.0495; see the table). Its strong STRING relationships with NUP155, NUP205, NUP88, and XPO1 and its hu.MAP transport memberships (hu.MAP huMAP3_09042.1) (hu.MAP huMAP3_07789.1) (hu.MAP huMAP3_05673.1) provide established molecular support. Its disease associations and substantial literature make it an informative representative of the nuclear-envelope component.
- **Conclusion**: Established evidence supports NUP93 as a nuclear pore constituent involved in regulated exchange between nucleus and cytoplasm. Its network position suggests that transport may couple the module's replication, repair, and RNA-processing branches, but that coupling remains an inference from co-abundance rather than a demonstrated causal mechanism.

#### MSH2

- **Related proteins** (co-abundance neighbors): MCM5 (0.84), NAA15 (0.84), MCM7 (0.83), MSH6 (0.81); STRING partners: FEN1 (0.948), MCM7 (0.71), MRE11 (0.847), MSH6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutS homolog 2. This locus is frequently mutated in hereditary nonpolyposis colon cancer (HNPCC). When cloned, it was discovered to be a human homolog of the E. coli mismatch repair gene mutS, consistent with the characteristic alterations in microsatellite sequences (RER+ phenotype) found in HNPCC. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: Lynch syndrome (0.891); colorectal cancer (0.776); mismatch repair cancer syndrome (0.775); Muir-Torre syndrome (0.752); mismatch repair cancer syndrome 1 (0.740)
- **Europe PMC papers**: 22581
- **Why important**: MSH2 represents mismatch repair within the module and is tightly connected to MSH6, while also linking to MCM proteins, FEN1, and MRE11. It occurs in globally supported DNA repair, recombination, DNA binding, and nucleic-acid catalytic terms (19 globally significant GO/KEGG terms, q_global 6.64e-05–0.0339; see the table). Its established MSH2–MSH6 relationship is supported by STRING, and its major disease associations with Lynch syndrome and mismatch-repair cancer syndromes give it strong clinical relevance and extensive literature support.
- **Conclusion**: Established evidence identifies MSH2 as a mismatch-repair factor and a clinically important genome-stability gene. In this module it is best viewed as a repair-state marker that connects replication activity to correction of DNA lesions, not as evidence that the shared tissue module causes mismatch-repair disease.

#### FEN1

- **Related proteins** (co-abundance neighbors): NUP93 (0.81); STRING partners: KPNA2 (0.858), MCM2 (0.912), MCM4 (0.941), MCM5 (0.942), MCM7 (0.903), MRE11 (0.984), MSH2 (0.948), MSH6 (0.95), RAD50 (0.844)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_13998.1, huMAP3_14982.1
- **Function (MyGene.info)**: flap structure-specific endonuclease 1. The protein encoded by this gene removes 5' overhanging flaps in DNA repair and processes the 5' ends of Okazaki fragments in lagging strand DNA synthesis. Direct physical interaction between this protein and AP endonuclease 1 during long-patch base excision repair provides coordinated loading of the proteins onto the substrate, thus passing the substrate from one enzyme to another. The protein is…
- **Diseases (Open Targets)**: neurodegenerative disease (0.496); HIV infectious disease (0.370); hepatocellular carcinoma (0.213); breast carcinoma (0.213); oral cavity squamous cell carcinoma (0.208)
- **Europe PMC papers**: 5275
- **Why important**: FEN1 is a multifunctional DNA-processing enzyme with a prominent repair and replication annotation profile. It is present in globally supported terms for DNA catalysis, DNA replication, homologous recombination, double-strand-break repair, and DNA binding (15 globally significant GO/KEGG terms, q_global 0.000125–0.0339; see the table). STRING places it at the interface of MCM proteins, MSH2, MSH6, MRE11, RAD50, and KPNA2, while hu.MAP includes FEN1-containing assemblies (hu.MAP huMAP3_13998.1) (hu.MAP huMAP3_14982.1). Its replication, repair, cancer, and neurodegenerative-disease literature is substantial.
- **Conclusion**: Established evidence supports FEN1 as a plausible biochemical bridge between DNA synthesis and repair in the module. Its connections make it a useful candidate for testing replication-associated stress, but the co-abundance pattern alone cannot determine whether FEN1 activity is altered.

#### XPO1

- **Related proteins** (co-abundance neighbors): XPO5 (0.85), NAA15 (0.82), SRRT (0.81), MCM2 (0.80); STRING partners: IPO4 (0.714), KPNA2 (0.832), NUP155 (0.769), NUP88 (0.997), NUP93 (0.712), TNPO3 (0.764), XPO5 (0.752)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: huMAP3_09042.1, huMAP3_08764.1, huMAP3_07170.1, huMAP3_06791.1
- **Function (MyGene.info)**: exportin 1. This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSe…
- **Diseases (Open Targets)**: plasma cell myeloma (0.642); B-cell chronic lymphocytic leukemia (0.626); diffuse large B-cell lymphoma (0.602); HIV infectious disease (0.561); neurodegenerative disease (0.522)
- **Europe PMC papers**: 5357
- **Why important**: XPO1 represents the export arm of the transport branch. It is included in globally supported nucleocytoplasmic transport, RNA export, nuclear export, and carrier-activity terms (18 globally significant GO/KEGG terms, q_global 0.000125–0.0495; see the table). It connects through STRING to the nucleoporin group, KPNA2, IPO4, TNPO3, and XPO5, and appears in multiple hu.MAP transport complexes (hu.MAP huMAP3_09042.1) (hu.MAP huMAP3_08764.1) (hu.MAP huMAP3_07170.1) (hu.MAP huMAP3_06791.1). Its extensive literature and associations with hematologic malignancy and viral infection make it a biologically consequential transport node.
- **Conclusion**: Established evidence identifies XPO1 as a major nuclear-export factor that could connect RNA and protein trafficking to the broader nuclear program. A role for altered export in the shared module is a reasonable interpretation, but it remains a hypothesis until cargo transport or XPO1 activity is measured directly.

## Module 13

**Tissue pair**: cervix_uterine and lung  
**Genes (5)**: DDX21, MYBBP1A, NOP2, PES1, RRP1B

### Function

This is a highly coherent nucleolar ribosome-biogenesis module. All module genes support ribosome biogenesis and ribonucleoprotein-complex biogenesis (GO:BP ribosome biogenesis; q_global = 0.000189) (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0012), with most members also supporting rRNA processing and rRNA metabolism (GO:BP rRNA processing; q_global = 0.00266) (GO:BP rRNA metabolic process; q_global = 0.00518). The shared localization evidence is the nucleolus (GO:CC nucleolus; q_global = 0.0248). DDX21 and MYBBP1A additionally connect the module to RNA polymerase III transcription and the B-WICH complex (GO:BP positive regulation of transcription by RNA polymerase III; q_global = 0.0352) (GO:CC B-WICH complex; q_global = 0.0352). Together, the evidence supports coordinated control of preribosome assembly, rRNA maturation, and ribosomal-subunit production rather than a tissue-specific extracellular function.

**Cell composition.** The module is composed of intracellular nucleolar proteins, not plasma proteins or secreted proteins. HPA reports no secreted genes and low immune-cell specificity for every member, arguing against a blood-cell or plasma-contamination explanation. All members have low tissue specificity, and protein detection is present for the module in cervix_uterine and for nearly all members in lung. Some genes show enhancement in particular cell types, including keratinocytes, glial or neuronal populations, and germ-cell or photoreceptor populations, but there is no recurrent blood-cell enrichment. The shared signal is therefore most consistent with a broadly expressed cellular program, potentially influenced by differences in proliferative or biosynthetic activity among sampled cells.

**GO/KEGG enrichment**: 7 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP ribosome biogenesis | 0.000189 | DDX21, MYBBP1A, NOP2, PES1, RRP1B |
| GO:BP ribonucleoprotein complex biogenesis | 0.0012 | DDX21, MYBBP1A, NOP2, PES1, RRP1B |
| GO:BP rRNA processing | 0.00266 | DDX21, NOP2, PES1, RRP1B |
| GO:BP rRNA metabolic process | 0.00518 | DDX21, NOP2, PES1, RRP1B |
| GO:CC nucleolus | 0.0248 | DDX21, MYBBP1A, NOP2, PES1, RRP1B |
| GO:BP positive regulation of transcription by RNA polymerase III | 0.0352 | DDX21, MYBBP1A |
| GO:CC B-WICH complex | 0.0352 | DDX21, MYBBP1A |

### STRING and hu.MAP

STRING provides strong functional and pairwise support: the module contains nearly all possible high-confidence pair relationships, including a dense network centered on DDX21 and strong links among NOP2, PES1, and RRP1B. STRING enrichment independently supports ribosome biogenesis, preribosome organization, nucleolar localization, rRNA processing, and the B-WICH complex (12 supplementary STRING terms; within-query FDR 0.00027–0.0482). These are largely concordant with the primary GO evidence, strengthening the interpretation that the co-abundance pattern reflects a real biological program. The citrullination keyword (STRING Keyword Citrullination; within-query FDR = 0.0035) is supplementary and does not establish a central module function. No hu.MAP complex contains multiple module members, so the evidence supports a functionally connected network without demonstrating that these proteins form one experimentally defined hu.MAP complex. PES1 is described as part of the PeBoW complex with BOP1 and WDR12, but that complex is not represented as a multi-member hu.MAP hit here.

**STRING interactions (score >= 0.7)**: 9 of 10 gene pairs: DDX21–MYBBP1A (0.963); DDX21–NOP2 (0.761); DDX21–PES1 (0.975); DDX21–RRP1B (0.806); MYBBP1A–NOP2 (0.864); MYBBP1A–PES1 (0.948); NOP2–PES1 (0.983); NOP2–RRP1B (0.937); PES1–RRP1B (0.984)
**STRING functional enrichment (supplementary, within-query FDR)**: Process Ribosome biogenesis (FDR = 0.00027, 5 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 0.0017, 4 genes); COMPARTMENTS Nucleolus (FDR = 0.0018, 5 genes); NetworkNeighborAL Mixed, incl. Preribosome, large subunit precursor, and Maturation of LSU-rRNA (FDR = 0.002, 3 genes); Process rRNA processing (FDR = 0.0031, 4 genes); Keyword Citrullination (FDR = 0.0035, 3 genes); Keyword Ribosome biogenesis (FDR = 0.0035, 3 genes); Keyword rRNA processing (FDR = 0.0035, 3 genes); Component Nucleolus (FDR = 0.0123, 5 genes); Component B-WICH complex (FDR = 0.0308, 2 genes); COMPARTMENTS B-WICH complex (FDR = 0.0322, 2 genes); NetworkNeighborAL Preribosome, large subunit precursor, and Circularly permuted (CP)-type guanine nucleotide-binding (G) domain (FDR = 0.0364, 2 genes); COMPARTMENTS Preribosome, large subunit precursor (FDR = 0.0482, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is unlikely to represent a newly discovered molecular function: its genes, nucleolar locations, ribosome-biogenesis annotations, STRING relationships, and known complexes are already strongly established. What may be novel is the observation that this coherent program is conserved as a co-abundance module across cervix_uterine and lung. That cross-tissue co-abundance organization, and its quantitative behavior in the underlying dataset, cannot be judged as previously reported from the supplied evidence alone. The absence of a hu.MAP multi-member complex does not prove novelty, because functional cooperation and context-dependent co-abundance need not correspond to inclusion in that resource.

**Hypothesis.** Hypothesis: the shared module reflects coordinated adjustment of ribosome production to cellular growth, proliferation, or biosynthetic demand in both tissues. DDX21 may help remodel RNA and organize ribosome-assembly processes, MYBBP1A may connect nucleolar stress and transcriptional regulation with ribosomal-DNA activity, NOP2 may support RNA modification and large-subunit maturation, and the PES1-RRP1B arm may contribute to preribosome maturation and associated transcriptional responses. This hypothesis is consistent with the annotations and network, but the co-abundance data alone do not establish causal direction, physical assembly of all five proteins, or the specific cellular stimulus responsible.

### Important genes

#### DDX21

- **Related proteins** (co-abundance neighbors): RRP1B (0.83), MYBBP1A (0.83), NOP2 (0.83), PES1 (0.82); STRING partners: MYBBP1A (0.963), NOP2 (0.761), PES1 (0.975), RRP1B (0.806)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 is the most connected member of the module in the supplied network and links to every other gene. It appears in every primary GO category, including ribosome biogenesis, rRNA processing, the nucleolus, RNA polymerase III transcription, and B-WICH (7 globally significant GO/KEGG terms, q_global 0.000189–0.0352; see the table). STRING independently connects it to all other members and to the same ribosome-related processes (9 supplementary STRING terms; within-query FDR 0.00027–0.0322). Its DEAD-box helicase family description provides a plausible RNA-remodeling role, and it has substantial literature coverage and disease associations involving cancer and neurodegenerative disease.
- **Conclusion**: Established evidence identifies DDX21 as a central, nucleolar RNA and ribosome-biogenesis factor and as the principal network connector. It is a strong candidate for coordinating the module, but the network does not prove that DDX21 drives the cross-tissue co-abundance pattern.

#### NOP2

- **Related proteins** (co-abundance neighbors): MYBBP1A (0.87), DDX21 (0.83); STRING partners: DDX21 (0.761), MYBBP1A (0.864), PES1 (0.983), RRP1B (0.937)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP2 nucleolar protein. Enables RNA binding activity. Involved in positive regulation of cell population proliferation; regulation of signal transduction by p53 class mediator; and ribosomal large subunit assembly. Located in nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.273); nonpapillary renal cell carcinoma (0.097); neoplasm (0.097); cancer (0.091); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 2120
- **Why important**: NOP2 is present in the core ribosome-biogenesis, ribonucleoprotein-complex, rRNA-processing, rRNA-metabolism, and nucleolar terms (5 globally significant GO/KEGG terms, q_global 0.000189–0.0248; see the table). Its annotation directly supports RNA binding, large-subunit assembly, LSU-rRNA maturation, and ribosome biogenesis. It has strong STRING relationships with every other module member and the largest literature volume among the listed genes. Its associations with proliferation and neoplasia make it biologically important when ribosomal production and growth are coupled.
- **Conclusion**: Established evidence supports NOP2 as a nucleolar RNA-processing and large-subunit maturation factor embedded in the module core. Its disease and proliferation associations make it a plausible activity marker, but they do not show that this module is cancer-specific or that NOP2 is causal in either tissue.

#### PES1

- **Related proteins** (co-abundance neighbors): DDX21 (0.82); STRING partners: DDX21 (0.975), MYBBP1A (0.948), NOP2 (0.983), RRP1B (0.984)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli, Nucleoli rim, Mitotic chromosome; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pescadillo ribosomal biogenesis factor 1. This gene encodes a nuclear protein that contains a breast cancer associated gene 1 (BRCA1) C-terminal interaction domain. The encoded protein interacts with BOP1 and WDR12 to form the PeBoW complex, which plays a critical role in cell proliferation via pre-rRNA processing and 60S ribosomal subunit maturation. Expression of this gene may play an important role in breast cancer proliferation and tu…
- **Diseases (Open Targets)**: aortic stenosis (0.137); neoplasm (0.104); head and neck squamous cell carcinoma (0.097); schizophrenia (0.091); neuroblastoma (0.081)
- **Europe PMC papers**: 1080
- **Why important**: PES1 is annotated as a ribosomal-biogenesis factor and as a component of the PeBoW complex, with roles in preribosomal RNA processing and large-subunit maturation. It appears in the principal ribosome-biogenesis and rRNA-processing terms (5 globally significant GO/KEGG terms, q_global 0.000189–0.0248; see the table) and in many STRING preribosome and nucleolar terms (10 supplementary STRING terms; within-query FDR 0.00027–0.0482). It has strong STRING links across the module, including particularly strong links with NOP2 and RRP1B, and it has substantial literature coverage. Its reported relationship to cell proliferation and tumorigenicity gives the module a possible growth-regulatory context.
- **Conclusion**: Established evidence supports PES1 as a key ribosome-maturation component and a bridge between the module and known preribosome biology. A role in explaining tissue-shared co-abundance is plausible, but the supplied data do not establish that PES1 controls proliferation in cervix_uterine or lung.

#### MYBBP1A

- **Related proteins** (co-abundance neighbors): NOP2 (0.87), DDX21 (0.83); STRING partners: DDX21 (0.963), NOP2 (0.864), PES1 (0.948)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MYB binding protein 1a. This gene encodes a nucleolar transcriptional regulator that was first identified by its ability to bind specifically to the Myb proto-oncogene protein. The encoded protein is thought to play a role in many cellular processes including response to nucleolar stress, tumor suppression and synthesis of ribosomal DNA. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep…
- **Diseases (Open Targets)**: neurodegenerative disease (0.507); Non-immune hydrops fetalis (0.370); ventricular septal defect (0.245); lysosomal storage disease (0.191); Meniere disease (0.162)
- **Europe PMC papers**: 763
- **Why important**: MYBBP1A is a nucleolar transcriptional regulator associated with nucleolar stress, tumor suppression, ribosomal-DNA synthesis, and chromatin remodeling. It contributes to the globally corrected ribosome-biogenesis and nucleolar terms (GO:BP ribosome biogenesis; q_global = 0.000189) (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0012) (GO:CC nucleolus; q_global = 0.0248) and to the RNA polymerase III and B-WICH terms (GO:BP positive regulation of transcription by RNA polymerase III; q_global = 0.0352) (GO:CC B-WICH complex; q_global = 0.0352). Its STRING links to DDX21, NOP2, and PES1 support a regulatory connection to the module, although its direct module degree is more limited than DDX21. Its disease associations and literature volume support relevance beyond a purely structural annotation.
- **Conclusion**: Established evidence places MYBBP1A at the interface of nucleolar regulation, transcription, and ribosome production. It is a reasonable candidate for linking ribosome biogenesis to cellular stress or transcriptional state, but that regulatory interpretation remains a hypothesis for this cross-tissue module.

#### RRP1B

- **Related proteins** (co-abundance neighbors): DDX21 (0.83); STRING partners: DDX21 (0.806), NOP2 (0.937), PES1 (0.984)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim, Mitotic chromosome; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal RNA processing 1B. Enables transcription coactivator activity. Involved in several processes, including cellular response to virus; positive regulation by host of viral transcription; and positive regulation of transcription by RNA polymerase II. Located in chromosome; granular component; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypertensive disorder (0.184); cardiovascular disorder (0.149); response to xenobiotic stimulus (0.111); essential hypertension (0.108); retinitis pigmentosa (0.107)
- **Europe PMC papers**: 387
- **Why important**: RRP1B is included in the primary ribosome-biogenesis, rRNA-processing, rRNA-metabolism, and nucleolar terms (5 globally significant GO/KEGG terms, q_global 0.000189–0.0248; see the table). Its annotations include rRNA processing and transcriptional regulation, and STRING places it in preribosome, large-subunit precursor, and rRNA-maturation neighborhoods (8 supplementary STRING terms; within-query FDR 0.00027–0.0482). Although it has the most limited direct connectivity in the supplied module graph, its strong STRING links to NOP2 and PES1 connect it to the presumed large-subunit maturation arm. It also has reported links to antiviral transcriptional responses, apoptosis, and transcriptional regulation.
- **Conclusion**: Established evidence supports RRP1B as a functionally relevant rRNA-processing and preribosome-associated member. Its peripheral position in the co-abundance graph may indicate a specialized or less tightly coordinated role, but the data do not establish whether it is an upstream regulator, downstream readout, or structural participant.

## Module 14

**Tissue pair**: cervix_uterine and lung  
**Genes (8)**: DNAJB1, EPS8, AGL, GMDS, ITPRID2, TRIP11, WDR18, WDR26

### Function

No GO or KEGG term passed global multiple-testing correction, so the module cannot be assigned a statistically supported pathway function from enrichment alone. The gene annotations instead suggest a heterogeneous intracellular program involving protein-complex organization and proteostasis through WDR26, WDR18 and DNAJB1; Golgi organization and trafficking through TRIP11; actin and growth-factor signaling through EPS8 and ITPRID2; carbohydrate and glycogen metabolism through GMDS and AGL; and possible glycan-related signaling through GMDS. The network is sparse but connected, with WDR26 as the main connector and EPS8 and GMDS forming a small bridge between several functional themes. These observations support a tentative interpretation as a shared epithelial or tissue-cell state involving intracellular organization, surface signaling, secretory-pathway organization and metabolic readiness, rather than a single established pathway. All functional interpretations beyond the absence of globally significant enrichment are hypotheses based on gene annotations and network structure.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins: none of its genes is annotated as secreted. Most genes have low tissue specificity, while several show cell-type-enhanced expression in epithelial, glandular, absorptive or related cells. The HPA evidence indicates low immune-cell specificity for most genes, with EPS8 as the exception showing immune-cell enhancement in non-classical monocytes. This makes a blood-cell explanation less compelling than a shared epithelial or epithelial-adjacent cell-state explanation, although sample composition cannot be excluded. Tissue-enhanced signals occur in digestive and glandular tissues, and AGL is group-enriched in skeletal muscle and tongue. Protein detection is broad in cervix_uterine and more limited in lung, while AGL, WDR18 and ITPRID2 have absence or non-detection in one or both tissues. Thus, the shared module may reflect conserved cell-state biology, variable cellular composition, or both; it does not resemble a secreted-plasma signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no STRING functional-enrichment result. No hu.MAP complex contains multiple module members. Therefore, the co-abundance edges are not corroborated as established physical or functional interactions by these resources. The absence of STRING and hu.MAP support argues against describing this as a validated protein complex. It may instead represent coordinated regulation, shared cell-type abundance, indirect pathway coupling, or correlations that are context-specific or not represented in current interaction databases. The strongest internal network position belongs to WDR26, which connects to TRIP11, EPS8, WDR18 and DNAJB1; this is a network observation, not evidence that WDR26 physically binds all of them.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The co-abundance pattern appears potentially novel in this tissue-pair analysis because none of its relationships is supported by the queried high-confidence STRING interactions or by a shared hu.MAP complex. However, that is not sufficient to establish biological novelty: database coverage is incomplete, co-abundance does not imply physical interaction, and the module may reflect known biology assembled in a new tissue context. The mixed annotations, sparse structure and lack of globally significant enrichment make a strong claim of a new molecular pathway unwarranted. A defensible conclusion is that this is a potentially novel cross-tissue co-abundance signature requiring replication, cell-composition adjustment, independent cohorts and targeted validation.

**Hypothesis.** Hypothesis: the module reflects a conserved epithelial or glandular cell state in cervix_uterine and lung in which intracellular scaffolding and proteostasis are coordinated with Golgi organization, actin-linked surface signaling and carbohydrate handling. WDR26 may act as the network-level integrator, while TRIP11 supports Golgi and microtubule organization, EPS8 links growth-factor signaling to actin remodeling, GMDS supplies GDP-fucose biosynthetic capacity, and DNAJB1 buffers protein-folding stress. This model predicts that the module will track epithelial differentiation, secretory-pathway demand or cellular stress more strongly than circulating immune-cell abundance. It remains a hypothesis because no GO or KEGG term passed global correction, STRING found no supported interactions, and hu.MAP found no shared complex.

### Important genes

#### WDR26

- **Related proteins** (co-abundance neighbors): TRIP11 (0.83), EPS8 (0.82), WDR18 (0.82), DNAJB1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 26. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: Skraban-Deardorff syndrome (0.798); neurodegenerative disease (0.539); hereditary disease (0.529); Intellectual disability (0.501); gastritis (0.207)
- **Europe PMC papers**: 416
- **Why important**: WDR26 is the central network connector, linking TRIP11, EPS8, WDR18 and DNAJB1. Its WD-repeat architecture is consistent with assembly of multiprotein complexes, and its annotation includes proteasome-mediated ubiquitin-dependent protein catabolism. It is detected in both tissues, has low tissue specificity, and has comparatively substantial literature and disease-association support, including Skraban-Deardorff syndrome and neurodegenerative disease.
- **Conclusion**: Established evidence supports WDR26 as the principal network organizer and a plausible contributor to intracellular complex assembly and proteostasis. It should be treated as a candidate coordinator of the module, not as a proven physical hub, because STRING and hu.MAP provide no corroboration and no globally significant enrichment implicates its functions.

#### EPS8

- **Related proteins** (co-abundance neighbors): WDR26 (0.82), GMDS (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EGFR pathway substrate 8, signaling adaptor. This gene encodes a member of the EPS8 family. This protein contains one PH domain and one SH3 domain. It functions as part of the EGFR pathway, though its exact role has not been determined. Highly similar proteins in other organisms are involved in the transduction of signals from Ras to Rac and growth factor-mediated actin remodeling. Alternate transcriptional splice variants of this gene have …
- **Diseases (Open Targets)**: autosomal recessive nonsyndromic hearing loss 102 (0.636); deafness (0.531); hearing loss, autosomal recessive (0.455); infectious meningitis (0.270); alcohol drinking (0.212)
- **Europe PMC papers**: 1754
- **Why important**: EPS8 occupies a bridging position between WDR26 and GMDS and is the most direct link in the module to plasma-membrane signaling and cytoskeletal remodeling. Its documented roles include EGFR-pathway signaling, Rac and Rho regulation, cell-shape control and actin-filament regulation. It is detected in both tissues and shows cell-type-enhanced expression in colonocytes, endometrial glandular cells and pericytes, with an immune-cell-enhanced signal in non-classical monocytes. It also has the largest literature volume among the module genes.
- **Conclusion**: Established evidence supports EPS8 as a plausible marker of epithelial growth-factor responsiveness and actin organization. Its position makes it a candidate interface between cell-surface signaling and the rest of the module, but the module does not establish that EPS8 drives the shared tissue signature or that its relationships are direct protein interactions.

#### GMDS

- **Related proteins** (co-abundance neighbors): AGL (0.87), EPS8 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GDP-mannose 4,6-dehydratase. GDP-mannose 4,6-dehydratase (GMD; EC 4.2.1.47) catalyzes the conversion of GDP-mannose to GDP-4-keto-6-deoxymannose, the first step in the synthesis of GDP-fucose from GDP-mannose, using NADP+ as a cofactor. The second and third steps of the pathway are catalyzed by a single enzyme, GDP-keto-6-deoxymannose 3,5-epimerase, 4-reductase, designated FX in humans (MIM 137020).[supplied by OMIM, Aug 2009…
- **Diseases (Open Targets)**: open-angle glaucoma (0.497); glaucoma (0.475); Abnormality of the skeletal system (0.474); gastroesophageal reflux disease (0.390); coronary artery disorder (0.373)
- **Europe PMC papers**: 1256
- **Why important**: GMDS is the metabolic bridge connecting AGL and EPS8. It catalyzes the first step of de novo GDP-fucose biosynthesis and is annotated in GDP-mannose metabolism and Notch signaling. HPA shows tissue enhancement in intestine, salivary gland and stomach-related tissue and cell-type enhancement in several mucous, glandular and epithelial populations. It is detected in both tissues and has a substantial literature and disease-association record.
- **Conclusion**: Established evidence supports GMDS as a glycan-biosynthesis enzyme with relevance to epithelial and glandular biology. In this module it may connect metabolic state with glycosylation-dependent signaling, but that connection is a mechanistic hypothesis rather than an enriched-pathway result or a demonstrated interaction.

#### TRIP11

- **Related proteins** (co-abundance neighbors): WDR26 (0.83), ITPRID2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thyroid hormone receptor interactor 11. This gene was identified based on the interaction of its protein product with thyroid hormone receptor beta. This protein is associated with the Golgi apparatus. The N-terminal region of the protein binds Golgi membranes and the C-terminal region binds the minus ends of microtubules; thus, the protein is thought to play a role in assembly and maintenance of the Golgi ribbon structure around the ce…
- **Diseases (Open Targets)**: achondrogenesis type IA (0.796); odontochondrodysplasia 1 (0.749); cancer (0.578); achondrogenesis (0.469); connective tissue disorder (0.462)
- **Europe PMC papers**: 503
- **Why important**: TRIP11 connects WDR26 with ITPRID2 and is annotated as a Golgi-associated protein involved in Golgi organization, Golgi-ribbon formation and endoplasmic-reticulum-to-Golgi vesicle transport. It is detected in both tissues, has low tissue specificity and low immune-cell specificity, and has established disease associations involving skeletal and connective-tissue disorders.
- **Conclusion**: Established evidence supports TRIP11 as a structural and trafficking component of the Golgi apparatus. Its network placement makes it a plausible indicator of secretory-pathway organization within the shared cell state, but there is no evidence that it forms a complex with the other module members or that Golgi biology is globally enriched in the module.

#### DNAJB1

- **Related proteins** (co-abundance neighbors): WDR26 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DnaJ heat shock protein family (Hsp40) member B1. This gene encodes a member of the DnaJ or Hsp40 (heat shock protein 40 kD) family of proteins. DNAJ family members are characterized by a highly conserved amino acid stretch called the 'J-domain' and function as one of the two major classes of molecular chaperones involved in a wide range of cellular events, such as protein folding and oligomeric protein complex assembly. The encoded protein is a …
- **Diseases (Open Targets)**: fibrolamellar hepatocellular carcinoma (0.377); hepatocellular adenoma (0.370); bile duct adenocarcinoma (0.370); hepatocellular carcinoma (0.290); hepatoblastoma (0.281)
- **Europe PMC papers**: 2924
- **Why important**: DNAJB1 is connected to WDR26 and encodes an Hsp40-family molecular chaperone that stimulates Hsp70 activity and participates in protein folding, unfolded-protein responses and suppression of inclusion-body assembly. It is detected in both tissues, has low tissue specificity and low immune-cell specificity, and has a substantial literature base with disease associations in liver tumors.
- **Conclusion**: Established evidence supports DNAJB1 as a proteostasis and cellular-stress component. Its connection to WDR26 is consistent with a possible protein-quality-control aspect of the module, but this remains a hypothesis because the network edge is co-abundance evidence and lacks STRING or hu.MAP support.
