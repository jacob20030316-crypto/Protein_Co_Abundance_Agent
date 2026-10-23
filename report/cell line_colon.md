# Conserved co-abundance modules: cell line and colon

## Module 0

**Tissue pair**: cell line and colon  
**Genes (44)**: APOBEC3B, ABCB6, BNIP2, CLDND1, CPSF1, SPECC1L, MEAF6, ESCO1, EXOC4, GTPBP2, GTPBP4, HEATR1, KAZN, KIFBP, KNOP1, LIN9, MBTD1, MOSPD1, NOL10, NOM1, NOP56, MT-ND2, PAPOLG, PHB2, PIK3CB, POT1, PTCD1, RBM28, RSL1D1, RRP12, PDCD11, SNRK, SNX2, TMEM161B, TAF1D, CCT7, TGM1, SNRNP200, UTP15, UTP6, VDR, ATP6V0A2, WDR3, ZC3H10

### Function

The module is best interpreted as a nucleolar RNA-processing and ribosome-biogenesis module, particularly the small-subunit processome and maturation of small-subunit ribosomal RNA. This conclusion is supported by the globally corrected terms for small-subunit processome (GO:CC small-subunit processome; q_global = 6.18e-06), nucleolus (GO:CC nucleolus; q_global = 3.39e-05), eukaryotic ribosome biogenesis (KEGG Ribosome biogenesis in eukaryotes - Homo sapiens (human); q_global = 6.88e-05), ribosomal small-subunit biogenesis (GO:BP ribosomal small subunit biogenesis; q_global = 8.86e-05), preribosome (GO:CC preribosome; q_global = 0.000113), RNA processing (GO:BP RNA processing; q_global = 0.000345), rRNA processing (GO:BP rRNA processing; q_global = 0.00297), ribosome biogenesis (GO:BP ribosome biogenesis; q_global = 0.00317), ribonucleoprotein-complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.00381), rRNA metabolism (GO:BP rRNA metabolic process; q_global = 0.00776), snoRNA binding (GO:MF snoRNA binding; q_global = 0.0128), and maturation of small-subunit rRNA (GO:BP maturation of SSU-rRNA; q_global = 0.0479). RNA binding and nucleic-acid binding (GO:MF RNA binding; q_global = 0.000267) (GO:MF nucleic acid binding; q_global = 0.00311) are consistent molecular features of this function. The network contains a compact, highly interconnected nucleolar core centered on HEATR1, NOP56, UTP6, UTP15, WDR3, PDCD11, GTPBP4, NOL10, RBM28, RRP12, and RSL1D1, with more peripheral genes connected to RNA processing, chromatin regulation, mitochondrial activity, membrane trafficking, and cell-surface biology. Thus, the module likely captures coordinated abundance of a ribosome-production program rather than a single isolated molecular interaction.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the HPA summary identifies only a single secreted gene, and the module is dominated by intracellular nucleolar, nuclear, mitochondrial, and cytosolic proteins. Most genes have low tissue specificity, consistent with a broadly used cellular program rather than a tissue-exclusive signature. Several genes show immune or blood-cell enhancement, especially among neutrophil, neutrophil-progenitor, basophil, monocyte, eosinophil, or B-cell populations, so a contribution from shared immune-cell content cannot be excluded in colon samples. However, the strongest functional core is composed of broadly expressed nucleolar ribosome-biogenesis genes rather than blood-cell markers. HPA also shows protein detection for most assessed genes in colon, whereas the cell-line comparison has no matching HPA tissue-protein assessment. Tissue-enhanced genes such as APOBEC3B, TGM1, VDR, and MT-ND2 may represent secondary cellular or tissue-context signals rather than the central module function.

**GO/KEGG enrichment**: 14 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC small-subunit processome | 6.18e-06 | HEATR1, NOL10, NOP56, PDCD11, UTP15, UTP6, WDR3 |
| GO:CC nucleolus | 3.39e-05 | BNIP2, GTPBP4, HEATR1, KNOP1, MEAF6, NOL10, NOM1, NOP56, PDCD11, PHB2, PIK3CB, RBM28, RRP12, RSL1D1, TAF1D, UTP15, UTP6, WDR3 |
| KEGG Ribosome biogenesis in eukaryotes - Homo sapiens (human) | 6.88e-05 | GTPBP4, HEATR1, NOP56, RBM28, UTP15, UTP6, WDR3 |
| GO:BP ribosomal small subunit biogenesis | 8.86e-05 | HEATR1, NOL10, NOM1, NOP56, UTP15, UTP6, WDR3 |
| GO:CC preribosome | 0.000113 | HEATR1, NOL10, NOP56, PDCD11, UTP15, UTP6, WDR3 |
| GO:MF RNA binding | 0.000267 | APOBEC3B, CPSF1, GTPBP2, GTPBP4, HEATR1, KNOP1, NOL10, NOM1, NOP56, PAPOLG, PDCD11, PTCD1, RBM28, RRP12, RSL1D1, SNRNP200, UTP15, UTP6, WDR3, ZC3H10 |
| GO:BP RNA processing | 0.000345 | CPSF1, GTPBP4, HEATR1, NOL10, NOP56, PAPOLG, PDCD11, PHB2, PTCD1, RBM28, SNRNP200, TAF1D, UTP15, UTP6, WDR3, ZC3H10 |
| GO:BP rRNA processing | 0.00297 | GTPBP4, HEATR1, NOL10, NOP56, PDCD11, UTP15, UTP6, WDR3 |
| GO:MF nucleic acid binding | 0.00311 | APOBEC3B, CPSF1, GTPBP2, GTPBP4, HEATR1, KNOP1, LIN9, NOL10, NOM1, NOP56, PAPOLG, PDCD11, POT1, PTCD1, RBM28, RRP12, RSL1D1, SNRNP200, TAF1D, TMEM161B, UTP15, UTP6, VDR, WDR3, ZC3H10 |
| GO:BP ribosome biogenesis | 0.00317 | GTPBP4, HEATR1, NOL10, NOM1, NOP56, PDCD11, UTP15, UTP6, WDR3 |
| GO:BP ribonucleoprotein complex biogenesis | 0.00381 | GTPBP4, HEATR1, NOL10, NOM1, NOP56, PDCD11, SNRNP200, UTP15, UTP6, WDR3 |
| GO:BP rRNA metabolic process | 0.00776 | GTPBP4, HEATR1, NOL10, NOP56, PDCD11, UTP15, UTP6, WDR3 |
| GO:MF snoRNA binding | 0.0128 | HEATR1, NOP56, UTP6, WDR3 |
| GO:BP maturation of SSU-rRNA | 0.0479 | HEATR1, NOL10, UTP6, WDR3 |

### STRING and hu.MAP

STRING provides substantial prior support for the nucleolar interpretation. The strongest known relationships form a coherent interaction neighborhood among HEATR1, NOP56, NOL10, PDCD11, UTP6, UTP15, WDR3, GTPBP4, RBM28, RRP12, RSL1D1, and NOM1. These relationships are represented across STRING functional terms for the preribosome, small-subunit processome, rRNA processing, ribosome biogenesis, and nucleolar localization (15 supplementary STRING terms; within-query FDR 2.56e-10–0.00016). Additional established STRING links include CPSF1 with PAPOLG, MBTD1 with MEAF6, and a weaker link between CCT7 and NOP56. The STRING evidence indicates that much of the central subnetwork is already known and that the co-abundance pattern recapitulates a real molecular neighborhood rather than an arbitrary gene grouping. hu.MAP independently identifies recurring complexes containing MBTD1 and MEAF6 (hu.MAP huMAP3_04039.1) (hu.MAP huMAP3_06087.1) (hu.MAP huMAP3_07843.1) (hu.MAP huMAP3_09291.1) (hu.MAP huMAP3_10481.1) (hu.MAP huMAP3_14306.1), and complexes containing VDR and ATP6V0A2 (hu.MAP huMAP3_09873.1) (hu.MAP huMAP3_10511.1). These complexes cover only subsets of the module, so they support selected side branches rather than the whole module. The absence of hu.MAP assignments for most nucleolar genes does not contradict their established STRING relationships.

**STRING interactions (score >= 0.7)**: 62 of 946 gene pairs: CCT7–NOP56 (0.728); CPSF1–PAPOLG (0.961); GTPBP4–HEATR1 (0.933); GTPBP4–NOL10 (0.877); GTPBP4–NOP56 (0.941); GTPBP4–PDCD11 (0.928); GTPBP4–RBM28 (0.975); GTPBP4–RRP12 (0.981); GTPBP4–RSL1D1 (0.996); GTPBP4–UTP15 (0.832); GTPBP4–UTP6 (0.876); GTPBP4–WDR3 (0.951); HEATR1–NOL10 (0.998); HEATR1–NOP56 (0.999); HEATR1–PDCD11 (0.999); HEATR1–RBM28 (0.793); HEATR1–RRP12 (0.951); HEATR1–RSL1D1 (0.982); HEATR1–UTP15 (0.999); HEATR1–UTP6 (0.999); HEATR1–WDR3 (0.999); MBTD1–MEAF6 (0.995); NOL10–NOP56 (0.996); NOL10–PDCD11 (0.997); NOL10–RBM28 (0.892); NOL10–RRP12 (0.923); NOL10–RSL1D1 (0.984); NOL10–UTP15 (0.996); NOL10–UTP6 (0.999); NOL10–WDR3 (0.998); NOM1–PDCD11 (0.705); NOM1–RBM28 (0.848); NOM1–RSL1D1 (0.897); NOM1–UTP6 (0.971); NOM1–WDR3 (0.986); NOP56–PDCD11 (0.997); NOP56–RBM28 (0.945); NOP56–RRP12 (0.938); NOP56–RSL1D1 (0.991); NOP56–UTP15 (0.999); NOP56–UTP6 (0.998); NOP56–WDR3 (0.999); PDCD11–RBM28 (0.976); PDCD11–RRP12 (0.984); PDCD11–RSL1D1 (0.978); PDCD11–UTP15 (0.987); PDCD11–UTP6 (0.994); PDCD11–WDR3 (0.997); RBM28–RRP12 (0.977); RBM28–RSL1D1 (0.953); RBM28–UTP6 (0.958); RBM28–WDR3 (0.913); RRP12–RSL1D1 (0.97); RRP12–UTP15 (0.724); RRP12–UTP6 (0.742); RRP12–WDR3 (0.878); RSL1D1–UTP15 (0.924); RSL1D1–UTP6 (0.993); RSL1D1–WDR3 (0.993); UTP15–UTP6 (0.999); UTP15–WDR3 (0.999); UTP6–WDR3 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 2.56e-10, 12 genes); NetworkNeighborAL rRNA modification in the nucleus and cytosol, and Maturation of SSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA) (FDR = 2.71e-06, 7 genes); NetworkNeighborAL Small-subunit processome, and Positive regulation of rRNA processing (FDR = 5.55e-06, 6 genes); KEGG Ribosome biogenesis in eukaryotes (FDR = 6.51e-06, 7 genes); COMPARTMENTS Small-subunit processome (FDR = 8.12e-06, 6 genes); NetworkNeighborAL Small-subunit processome, and Positive regulation of rRNA processing (FDR = 9.9e-06, 5 genes); COMPARTMENTS Preribosome (FDR = 1.43e-05, 7 genes); Component Nucleolus (FDR = 2.34e-05, 17 genes); Component Preribosome (FDR = 2.34e-05, 7 genes); Component Small-subunit processome (FDR = 2.34e-05, 6 genes); Process rRNA processing (FDR = 5.32e-05, 10 genes); Process Ribonucleoprotein complex biogenesis (FDR = 5.32e-05, 12 genes); Process Ribosome biogenesis (FDR = 5.32e-05, 11 genes); RCTM rRNA modification in the nucleus and cytosol (FDR = 9.09e-05, 6 genes); COMPARTMENTS Nucleolus (FDR = 0.00016, 13 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04039.1 (MBTD1, MEAF6; 2/9); huMAP3_06087.1 (MBTD1, MEAF6; 2/14); huMAP3_07843.1 (MBTD1, MEAF6; 2/23); huMAP3_09873.1 (VDR, ATP6V0A2; 2/24); huMAP3_09291.1 (MBTD1, MEAF6; 2/27); huMAP3_10511.1 (VDR, ATP6V0A2; 2/35); huMAP3_10481.1 (MBTD1, MEAF6; 2/40); huMAP3_14306.1 (MBTD1, MEAF6; 2/55)

### Novelty

The module should not be claimed as a newly discovered ribosome-biogenesis complex. Its dominant biological function and many of its central pairwise relationships are already represented in STRING, and the core genes are established nucleolar or small-subunit-processome components. The potentially novel observation is the reproducible co-abundance of this known machinery as one conserved module across cell line and colon, together with peripheral links to genes involved in epithelial differentiation, immune-cell biology, mitochondrial function, membrane trafficking, chromatin regulation, and RNA three-prime-end processing. That cross-context organization may be biologically informative, but the fact sheet does not establish whether it is absent from prior co-expression studies, whether it is causal, or whether it reflects cell composition. Therefore the appropriate conclusion is a conserved data-derived module built around known biology, with possible novelty in its sample-context organization rather than in the underlying molecular functions.

**Hypothesis.** Hypothesis: coordinated abundance of the nucleolar small-subunit-processome machinery reflects a shared demand for ribosome production and RNA maturation in both the cell-line and colon contexts. The peripheral genes may connect this core to cell proliferation, epithelial differentiation, immune-cell state, mitochondrial activity, membrane trafficking, and post-transcriptional RNA control. In colon, the pattern could arise from a combination of epithelial growth or renewal and variable immune-cell representation; in the cell line, it may reflect a broadly conserved biosynthetic state. This hypothesis predicts that module activity should track nucleolar transcription and small-subunit rRNA maturation, while perturbation of core genes such as HEATR1, UTP6, PDCD11, NOP56, or WDR3 should disrupt ribosome production and possibly alter growth or stress responses. The proposed links to immune composition, epithelial state, and mitochondrial or membrane biology remain hypotheses and are not established by the enrichment results alone.

### Important genes

#### HEATR1

- **Related proteins** (co-abundance neighbors): WDR3 (0.84), PDCD11 (0.82), UTP6 (0.80); STRING partners: GTPBP4 (0.933), NOL10 (0.998), NOP56 (0.999), PDCD11 (0.999), RBM28 (0.793), RRP12 (0.951), RSL1D1 (0.982), UTP15 (0.999), UTP6 (0.999), WDR3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HEAT repeat containing 1. Enables RNA binding activity. Involved in positive regulation of rRNA processing and positive regulation of transcription by RNA polymerase I. Located in fibrillar center and mitochondrion. Implicated in pancreatic ductal carcinoma. Biomarker of glioblastoma. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.475); Alzheimer disease (0.463); Parkinson disease (0.462); lysosomal storage disease (0.462); musculoskeletal system disorder (0.168)
- **Europe PMC papers**: 342
- **Why important**: HEATR1 is a central anchor of the nucleolar subnetwork, with strong STRING relationships to nearly all major ribosome-biogenesis genes in the module. It appears in every primary enrichment layer spanning the small-subunit processome, preribosome, rRNA processing, ribosome biogenesis, snoRNA binding, and small-subunit-rRNA maturation (14 globally significant GO/KEGG terms, q_global 6.18e-06–0.0479; see the table). HPA places it in the nucleolar fibrillar center and detects it in colon. Its curated functions include positive regulation of rRNA processing, RNA polymerase I transcription, and maturation of small-subunit rRNA. The fact sheet also links it to pancreatic ductal carcinoma and glioblastoma biomarker status, giving it disease relevance beyond basic ribosome biology.
- **Conclusion**: Established evidence supports HEATR1 as a core component or regulator of the module's nucleolar ribosome-biogenesis program. Its central network position and broad primary annotation support make it one of the strongest candidate drivers of the module. Whether its coordinated abundance directly controls the cross-tissue module, rather than simply marking nucleolar activity, remains to be tested.

#### UTP6

- **Related proteins** (co-abundance neighbors): PDCD11 (0.81), HEATR1 (0.80); STRING partners: GTPBP4 (0.876), HEATR1 (0.999), NOL10 (0.999), NOM1 (0.971), NOP56 (0.998), PDCD11 (0.994), RBM28 (0.958), RRP12 (0.742), RSL1D1 (0.993), UTP15 (0.999), WDR3 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UTP6 small subunit processome component. Predicted to enable snoRNA binding activity. Predicted to be involved in maturation of SSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: post-traumatic stress disorder (0.069); colorectal carcinoma (0.067); type 1 diabetes mellitus (0.057); ovarian neoplasm (0.057); prostate carcinoma (0.040)
- **Europe PMC papers**: 283
- **Why important**: UTP6 is a canonical small-subunit-processome component with extensive STRING connectivity to the nucleolar core and repeated membership across all primary enrichment themes, including small-subunit processome, eukaryotic ribosome biogenesis, rRNA processing, snoRNA binding, and small-subunit-rRNA maturation (14 globally significant GO/KEGG terms, q_global 6.18e-06–0.0479; see the table). HPA localizes it to nucleoli and detects it in colon. Its curated function specifically includes snoRNA binding and maturation of small-subunit rRNA. It therefore provides a direct molecular bridge between the module's network structure and its inferred biochemical activity.
- **Conclusion**: Established evidence identifies UTP6 as a core small-subunit-processome gene and a strong marker of the module's principal function. Its disease associations in the fact sheet are comparatively limited, so its importance here is primarily mechanistic and network-based rather than disease-specific. A causal role in the conserved co-abundance pattern is plausible but not demonstrated.

#### PDCD11

- **Related proteins** (co-abundance neighbors): NOL10 (0.83), HEATR1 (0.82), UTP15 (0.82), NOP56 (0.81), UTP6 (0.81), RSL1D1 (0.80); STRING partners: GTPBP4 (0.928), HEATR1 (0.999), NOL10 (0.997), NOM1 (0.705), NOP56 (0.997), RBM28 (0.976), RRP12 (0.984), RSL1D1 (0.978), UTP15 (0.987), UTP6 (0.994), WDR3 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 11. PDCD11 is a NF-kappa-B (NFKB1; 164011)-binding protein that colocalizes with U3 RNA (MIM 180710) in the nucleolus and is required for rRNA maturation and generation of 18S rRNA (Sweet et al., 2003 [PubMed 14624448]; Sweet et al., 2008 [PubMed 17654514]).[supplied by OMIM, Oct 2008].
- **Diseases (Open Targets)**: Back pain (0.277); insomnia (0.216); systemic lupus erythematosus (0.170); neoplasm (0.095); colorectal carcinoma (0.093)
- **Europe PMC papers**: 334
- **Why important**: PDCD11 has a prominent position within the nucleolar core and many high-confidence STRING relationships to the principal ribosome-biogenesis genes. It participates in nearly all primary functional annotations for the module, including small-subunit processome, preribosome, RNA processing, rRNA processing, ribosome biogenesis, and rRNA metabolism (12 globally significant GO/KEGG terms, q_global 6.18e-06–0.00776; see the table). HPA places it at the nucleolar rim and detects it in colon. Curated evidence states that PDCD11 colocalizes with U3 RNA, is required for rRNA maturation and generation of the eighteen-S rRNA product, and participates in cleavage of the external transcribed spacer. The fact sheet also records associations with systemic lupus erythematosus and colorectal carcinoma, although these associations do not establish a role in this module.
- **Conclusion**: Established evidence makes PDCD11 a particularly informative functional representative of the module because its known activity directly concerns rRNA maturation. It is likely to report the active nucleolar core more specifically than peripheral genes. The disease associations are supportive context only; they do not show that this module mediates those diseases.

#### NOP56

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.81), PDCD11 (0.81); STRING partners: CCT7 (0.728), GTPBP4 (0.941), HEATR1 (0.999), NOL10 (0.996), PDCD11 (0.997), RBM28 (0.945), RRP12 (0.938), RSL1D1 (0.991), UTP15 (0.999), UTP6 (0.998), WDR3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP56 ribonucleoprotein. Nop56p is a yeast nucleolar protein that is part of a complex with the nucleolar proteins Nop58p and fibrillarin. Nop56p is required for assembly of the 60S ribosomal subunit and is involved in pre-rRNA processing. The protein encoded by this gene is similar in sequence to Nop56p and is also found in the nucleolus. Expansion of a GGCCTG repeat from 3-8 copies to 1500-2500 copies in an intron of th…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 36 (0.586); neurodegenerative disease (0.495); ovarian neoplasm (0.272); hereditary disease (0.193); cerebellar ataxia (0.121)
- **Europe PMC papers**: 1517
- **Why important**: NOP56 is deeply embedded in the STRING-supported nucleolar interaction neighborhood and appears across the primary processome, nucleolus, preribosome, ribosome-biogenesis, RNA-processing, rRNA-processing, snoRNA-binding, and small-subunit-maturation terms (14 globally significant GO/KEGG terms, q_global 6.18e-06–0.0479; see the table). HPA places it in the nucleolar fibrillar center and detects it in colon. Its established function includes rRNA processing, rRNA two-prime-O-methylation, maturation of small-subunit rRNA, and small-subunit biogenesis. It also has substantial literature and a well-established disease association with spinocerebellar ataxia type thirty-six.
- **Conclusion**: Established evidence supports NOP56 as a core ribosome-biogenesis and rRNA-modification component of the module. Its disease connection shows that disruption of this biology can have organismal consequences, but it does not imply that the observed module is pathogenic or disease-specific. NOP56 is best viewed as a mechanistic anchor and disease-relevant context gene.

#### WDR3

- **Related proteins** (co-abundance neighbors): HEATR1 (0.84), RRP12 (0.82), SNRNP200 (0.80); STRING partners: GTPBP4 (0.951), HEATR1 (0.999), NOL10 (0.998), NOM1 (0.986), NOP56 (0.999), PDCD11 (0.997), RBM28 (0.913), RRP12 (0.878), RSL1D1 (0.993), UTP15 (0.999), UTP6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 3. This gene encodes a nuclear protein containing 10 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, which usually include a trp-asp at the C-terminal end. Proteins belonging to the WD repeat family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. [provid…
- **Diseases (Open Targets)**: presbycusis (0.335); respiratory tract infectious disorder (0.184); neurodegenerative disease (0.143); preeclampsia (0.120); alcohol drinking (0.098)
- **Europe PMC papers**: 280
- **Why important**: WDR3 is a nucleolar WD-repeat protein with strong STRING relationships to the central processome neighborhood and membership across all primary enrichment terms for small-subunit processome, rRNA processing, ribosome biogenesis, snoRNA binding, and small-subunit-rRNA maturation (14 globally significant GO/KEGG terms, q_global 6.18e-06–0.0479; see the table). HPA localizes it to nucleoli. Its curated annotation directly identifies roles in maturation of small-subunit rRNA and ribosomal small-subunit biogenesis. Although its direct literature and disease-association profile is less extensive than that of some module members, its repeated primary annotation and placement within the conserved core make it important for interpreting the module.
- **Conclusion**: Established evidence supports WDR3 as a core nucleolar small-subunit-biogenesis component and a useful corroborating marker for the inferred function. Its lower apparent network connectivity within the co-abundance graph does not diminish the strength of its functional annotation. Whether WDR3 helps organize the observed cross-context abundance pattern is a testable hypothesis rather than an established conclusion.

## Module 1

**Tissue pair**: cell line and colon  
**Genes (5)**: ACE, ASB9, FAR2, H1-3, QPCT

### Function

This is a sparse co-abundance module without a statistically supported common GO or KEGG function: no globally significant GO/KEGG GO/KEGG term passed global correction. The genes represent biologically diverse processes, including peptide hormone processing and vascular physiology through ACE, peptide maturation through QPCT, ubiquitin-dependent protein turnover through ASB9, fatty-acyl metabolism through FAR2, and chromatin organization through H1-3. The absence of enriched terms does not invalidate the module, but it argues against interpreting it as a canonical biochemical pathway. The network is better viewed as a reproducible expression or abundance association among genes with distinct cellular functions.

**Cell composition.** The module is compositionally mixed rather than a clearly coherent secreted-protein module or a broadly expressed housekeeping module. ACE and QPCT are secreted to blood, but the remaining genes are not annotated as secreted. HPA tissue annotations point toward intestine, testis, epididymis, kidney, liver, adrenal gland, bone marrow, and choroid plexus. Cell-type annotations include enterocytes, neutrophils and neutrophil progenitors, melanocytes, spermatogenic cells, renal and parietal cells, and hematopoietic progenitors. Immune-cell associations are present for most of the module, particularly involving neutrophil-related, eosinophil, dendritic-cell, and memory B-cell populations. Colon protein detection is mixed, while there is no matching HPA protein-detection evidence for the cell-line context. These observations raise the possibility that the shared module reflects cell-type composition, immune or epithelial admixture, or tissue-state composition rather than a single process operating in every member gene.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no STRING functional-enrichment result was reported. No hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not supported here as established physical interactions or as membership in a known multiprotein complex. The ACE–ASB9–QPCT portion forms the central co-abundance connection pattern, with FAR2 linked to ACE and H1-3 linked to QPCT, but these relationships should be interpreted as abundance associations rather than demonstrated molecular binding or direct regulation.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unrecognized co-abundance pattern because its internal associations lack corresponding high-confidence STRING interactions, hu.MAP complexes, or STRING enrichment. However, that absence alone does not establish biological novelty. Several members are well studied, especially ACE and H1-3, and their individual functions and disease links are established. The potentially novel element is therefore the cross-process association of these genes in the shared cell-line and colon module, not the discovery of new functions for the individual genes. The mixed HPA tissue and immune-cell signatures provide an alternative explanation in which the pattern reflects shared sample composition or cellular state.

**Hypothesis.** Hypothesis: the module reflects a shared epithelial or immune-associated abundance state that couples peptide-related proteins with cellular remodeling, lipid handling, protein turnover, and chromatin changes. In this model, ACE and QPCT may mark extracellular or secretory activity, FAR2 may mark lipid and membrane-related metabolic state, ASB9 may reflect altered ubiquitin-mediated substrate handling, and H1-3 may reflect changes in chromatin organization or proliferative composition. The sparse network and lack of known physical complexes favor a model of coordinated cell-state composition or co-regulation rather than a single protein complex. This hypothesis requires validation with cell deconvolution, independent cohorts, perturbation experiments, and expression-level analyses within purified cell populations.

### Important genes

#### ACE

- **Related proteins** (co-abundance neighbors): FAR2 (0.87), ASB9 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: angiotensin I converting enzyme. This gene encodes an enzyme involved in blood pressure regulation and electrolyte balance. It catalyzes the conversion of angiotensin I into a physiologically active peptide angiotensin II. Angiotensin II is a potent vasopressor and aldosterone-stimulating peptide that controls blood pressure and fluid-electrolyte balance. This angiotensin converting enzyme (ACE) also inactivates the vasodilator p…
- **Diseases (Open Targets)**: hypertensive disorder (0.750); renal tubular dysgenesis of genetic origin (0.729); renal tubular dysgenesis (0.724); cardiovascular disorder (0.704); diabetic kidney disease (0.689)
- **Europe PMC papers**: 95248
- **Why important**: ACE is a central node in the module, connected to both ASB9 and FAR2, and has a well-established enzymatic role in angiotensin maturation, bradykinin inactivation, blood-pressure regulation, electrolyte balance, vascular remodeling, and renal physiology. Its HPA profile links it to intestine, testis, enterocytes, late spermatids, and a memory B-cell population. It has extensive literature support and strong disease relevance for hypertensive, cardiovascular, renal, and diabetic kidney disorders.
- **Conclusion**: Established evidence supports ACE as the most biologically interpretable anchor of the module and as a plausible marker of vascular, renal, epithelial, or secretory state. It is not established that ACE directly regulates the other module genes. Its module role may therefore be contextual or compositional rather than mechanistic.

#### QPCT

- **Related proteins** (co-abundance neighbors): H1-3 (0.87), ASB9 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enriched; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutaminyl-peptide cyclotransferase. This gene encodes human pituitary glutaminyl cyclase, which is responsible for the presence of pyroglutamyl residues in many neuroendocrine peptides. The amino acid sequence of this enzyme is 86% identical to that of bovine glutaminyl cyclase. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.424); Alzheimer disease (0.407); Parkinson disease (0.399); lysosomal storage disease (0.396); schizophrenia (0.285)
- **Europe PMC papers**: 1244
- **Why important**: QPCT occupies a central connecting position between H1-3 and ASB9 and encodes glutaminyl-peptide cyclotransferase, an enzyme that generates pyroglutamyl residues in peptide hormones and other neuroendocrine peptides. It is secreted to blood and is associated in HPA with adrenal gland, epididymis, melanocytes, neutrophils, pancreatic islet cells, and neutrophil-related blood-cell profiles. Its disease literature includes neurodegenerative and lysosomal disorders.
- **Conclusion**: Established evidence supports QPCT as a peptide-processing and secretory-state marker. Its association with ACE could indicate coordinated peptide-related biology, but the absence of STRING and complex evidence means that a direct molecular relationship is unproven. The immune and tissue annotations also make cell composition a credible explanation.

#### ASB9

- **Related proteins** (co-abundance neighbors): ACE (0.81), QPCT (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ankyrin repeat and SOCS box containing 9. This gene encodes a member of the ankyrin repeat and suppressor of cytokine signaling (SOCS) box protein family. Members of this family can interact with the elongin B-C adapter complex via their SOCS box domain and further complex with the cullin and ring box proteins to form E3 ubiquitin ligase complexes. They may function to mediate the substrate-recognition of the E3 ubiquitin ligases. A trans…
- **Diseases (Open Targets)**: Alzheimer disease (0.021); colorectal carcinoma (0.017); hepatocellular carcinoma (0.016); clear cell renal carcinoma (0.015); hypertensive disorder (0.015)
- **Europe PMC papers**: 293
- **Why important**: ASB9 is part of the central ACE–ASB9–QPCT co-abundance pattern. Its SOCS-box and ankyrin-repeat architecture is consistent with substrate recognition in cullin-associated E3 ubiquitin ligase complexes, and its annotations include protein ubiquitination, proteasome-mediated catabolism, and intracellular signal transduction. HPA links it to kidney, liver, testis, melanocytes, renal collecting-duct intercalated cells, Sertoli cells, and myeloid dendritic cells. It also has disease associations involving colorectal, hepatic, renal, hypertensive, and neurodegenerative contexts.
- **Conclusion**: Established evidence supports ASB9 as a candidate regulator of protein turnover and signaling state. Its position makes it a potentially informative bridge between peptide-associated genes and intracellular regulation, but no physical interaction or shared complex with ACE or QPCT is established. Its relatively limited literature base makes the module association particularly suitable for follow-up.

#### FAR2

- **Related proteins** (co-abundance neighbors): ACE (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fatty acyl-CoA reductase 2. This gene belongs to the short chain dehydrogenase/reductase superfamily. It encodes a reductase enzyme involved in the first step of wax biosynthesis wherein fatty acids are converted to fatty alcohols. The encoded peroxisomal protein utilizes saturated fatty acids of 16 or 18 carbons as preferred substrates. Alternatively spliced transcript variants have been observed for this gene. Related pseu…
- **Diseases (Open Targets)**: osteoarthritis, hip (0.434); spinal stenosis (0.432); androgenetic alopecia (0.355); total hip arthroplasty (0.349); refractive error (0.342)
- **Europe PMC papers**: 593
- **Why important**: FAR2 is connected to ACE and encodes a fatty-acyl-CoA reductase involved in fatty-acid-to-fatty-alcohol conversion and wax biosynthesis, using long saturated fatty-acid substrates. It is localized to the Golgi apparatus and has HPA associations with epididymis, intestine, cardiomyocytes, microglia, neutrophils, neutrophil progenitors, and eosinophils. Its disease-linked literature includes skeletal and refractive disorders.
- **Conclusion**: Established evidence supports FAR2 as a lipid-metabolism and membrane-associated marker. Its connection with ACE may identify a shared epithelial, secretory, or tissue-composition state, but there is no evidence here that ACE directly controls FAR2 or that the two proteins form a complex. FAR2 is a plausible mechanistic follow-up gene because lipid handling could influence secretory and cellular-state phenotypes.

#### H1-3

- **Related proteins** (co-abundance neighbors): QPCT (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: H1.3 linker histone, cluster member. Histones are basic nuclear proteins responsible for nucleosome structure of the chromosomal fiber in eukaryotes. Two molecules of each of the four core histones (H2A, H2B, H3, and H4) form an octamer, around which approximately 146 bp of DNA is wrapped in repeating units, called nucleosomes. The linker histone, H1, interacts with linker DNA between nucleosomes and functions in the compaction of ch…
- **Diseases (Open Targets)**: breast carcinoma (0.080); actinic keratosis (0.066); sebaceous of Jadassohn nevus (0.057); squamous cell carcinoma (0.045); non-small cell lung carcinoma (0.036)
- **Europe PMC papers**: 118293
- **Why important**: H1-3 is connected to QPCT and encodes a linker histone involved in nucleosome organization, chromatin compaction, chromosome condensation, DNA recombination control, and regulation of mRNA splicing. It has a very large literature base relative to the other module members. HPA associates it with bone marrow and choroid plexus and with erythrocyte, hematopoietic stem, innate lymphoid, and megakaryocyte progenitor populations.
- **Conclusion**: Established evidence supports H1-3 as a chromatin and hematopoietic-state marker. Its co-abundance with QPCT does not demonstrate a direct regulatory connection. The association may instead reflect differences in cellular composition, proliferation, chromatin state, or sample handling. H1-3 is important because it links the module to nuclear state while also reinforcing the possibility of hematopoietic or mixed-cell contributions.

## Module 2

**Tissue pair**: cell line and colon  
**Genes (33)**: ADGRG6, APPBP2, AURKB, BLMH, CDAN1, C8orf33, CLK4, DNAJC30, E2F8, GIPC2, HNRNPLL, HOXB7, KLF4, MSANTD4, N4BP3, NANP, OAF, PCGF6, AGPAT2, RAB8B, HRAS, RAB11FIP3, RFWD3, MRPL55, POLR1C, RPS26, RTEL1, SLC35A3, SACK1D, SPI1, TCEAL3, VCF1, ZFAND5

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING enrichment; therefore, the module should not be assigned a statistically established pathway label. Its genes nevertheless suggest a mixed regulatory module involving nuclear genome maintenance and cell-cycle control, epithelial and developmental transcription, intracellular trafficking, glycosylation-related transport, and selected myeloid or erythroid programs. The co-abundance structure is sparse and distributed across several local connections rather than forming a known pathway-level complex. These gene-level annotations support biological interpretation, but they do not replace enrichment evidence.

**Cell composition.** The module is not dominated by secreted or plasma proteins: only a small minority are annotated as secreted, and most proteins detected in colon are intracellular. It is also not uniformly blood-cell specific. Most genes have low immune-cell specificity, although several show enhancement in bone marrow, lymphoid tissue, erythrocyte progenitors, neutrophil progenitors, monocyte-related cells, or other hematopoietic populations. Many genes are broadly expressed or associated with epithelial, reproductive, hepatic, muscle, or developmental cell types. The shared signal between cell line and colon may therefore reflect a combination of broadly expressed intracellular programs and shared proliferative, epithelial, or hematopoietic-related cell states rather than a plasma-protein signal. HPA protein detection in colon supports expression of much of the module there, whereas the cell-line protein summary provides no discriminating evidence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was detected among module members, and no hu.MAP complex contained multiple module members. Thus, the co-abundance relationships are not corroborated as established physical interactions or membership in a known complex by these resources. The strongest module links are consequently co-abundance associations, not demonstrated protein binding. Some individual functions are nevertheless biologically coherent: RFWD3 is linked to DNA-damage repair, AURKB to mitosis, RAB8B and RAB11FIP3 to vesicle trafficking, SPI1 to myeloid and lymphoid development, and KLF4 and HOXB7 to transcriptional regulation. These annotations support interpretation of functional neighborhoods but do not establish direct molecular connectivity.

**STRING interactions (score >= 0.7)**: 0 of 528 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel co-abundance pattern, but it cannot be called a newly discovered biological complex or pathway. The absence of STRING and hu.MAP support increases the possibility that the coordinated signal is under-characterized, context-dependent, indirect, or driven by cell composition. It does not by itself prove novelty. The lack of globally significant GO or KEGG enrichment also argues for caution: the module appears heterogeneous, and its reproducibility across cell line and colon is more consistent with a shared expression or cell-state signal than with a previously defined molecular complex. Demonstrating novelty would require independent replication, comparison with published tissue and cell-line modules, and testing whether the signal persists after adjustment for cell-type composition and proliferation.

**Hypothesis.** Hypothesis: this module captures a cross-context cell-state program in which proliferative or differentiating cells coordinate genome maintenance, mitotic progression, transcriptional remodeling, vesicle and membrane trafficking, and lineage-associated regulation. RFWD3, AURKB, and E2F8 may represent a genome-integrity and cell-cycle branch; SPI1 and selected hematopoietic-associated genes may reflect myeloid or progenitor cell contribution; KLF4 and HOXB7 may represent epithelial or developmental transcriptional state; and RAB8B, SLC35A3, and RAB11FIP3 may connect that state to membrane trafficking and glycan handling. This is a mechanistic model, not an established pathway assignment, and it should be tested by cell-type deconvolution, perturbation of selected regulators, and replication in independent colon and cell-line datasets.

### Important genes

#### RFWD3

- **Related proteins** (co-abundance neighbors): CDAN1 (0.96), E2F8 (0.87), HOXB7 (0.87), PCGF6 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ring finger and WD repeat domain 3. Enables MDM2/MDM4 family protein binding activity; p53 binding activity; and ubiquitin protein ligase activity. Involved in several processes, including DNA metabolic process; regulation of cell cycle phase transition; and response to ionizing radiation. Located in nucleoplasm and site of DNA damage. Colocalizes with site of double-strand break. Implicated in Fanconi anemia. [provided by Alliance …
- **Diseases (Open Targets)**: Fanconi anemia, complementation group W (0.585); Fanconi anemia (0.445); plasma cell myeloma (0.384); testicular germ cell tumor (0.384); neurodegenerative disease (0.370)
- **Europe PMC papers**: 512
- **Why important**: RFWD3 is one of the better-connected genes in the module and links directly to CDAN1, E2F8, HOXB7, and PCGF6 in the co-abundance graph. Its established functions include p53 and MDM-family binding, ubiquitin ligase activity, DNA-damage response, homologous-recombination repair, replication-fork processing, and ionizing-radiation response. HPA places it in bone marrow and in progenitor populations, while the disease annotations connect it to Fanconi anemia. Its literature volume is substantial enough to provide stronger biological grounding than the poorly characterized module members.
- **Conclusion**: Established evidence supports RFWD3 as a DNA-damage and genome-maintenance factor with hematopoietic relevance. Its position suggests that it may anchor one regulatory neighborhood of the module. It is not established that RFWD3 physically interacts with the neighboring module genes or that it drives the shared co-abundance pattern.

#### SPI1

- **Related proteins** (co-abundance neighbors): POLR1C (0.83), HNRNPLL (0.82), BLMH (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Spi-1 proto-oncogene. This gene encodes an ETS-domain transcription factor that activates gene expression during myeloid and B-lymphoid cell development. The nuclear protein binds to a purine-rich sequence known as the PU-box found near the promoters of target genes, and regulates their expression in coordination with other transcription factors and cofactors. The protein can also regulate alternative splicing of targe…
- **Diseases (Open Targets)**: agammaglobulinemia 10, autosomal dominant (0.726); agammaglobulinemia (0.538); neurodegenerative disease (0.528); Alzheimer disease (0.410); autosomal agammaglobulinemia (0.384)
- **Europe PMC papers**: 10689
- **Why important**: SPI1 is a biologically prominent transcription factor with a strong literature base and a central lineage interpretation. It is associated with myeloid and B-lymphoid development, is enhanced in bone marrow, lung, and lymphoid tissue, and is enriched in dendritic, macrophage, Kupffer-cell, and monocyte-progenitor populations. In the module it connects POLR1C, HNRNPLL, and BLMH. Its disease annotations include inherited agammaglobulinemia and neurodegenerative or Alzheimer disease associations.
- **Conclusion**: Established evidence supports SPI1 as a regulator of hematopoietic lineage development and immune-cell transcription. It makes a blood or progenitor contribution to the shared module plausible, but the HPA summary does not show that the whole module is immune-cell specific. SPI1 should therefore be treated as a marker of one possible cellular component, not as proof of an immune pathway.

#### RAB8B

- **Related proteins** (co-abundance neighbors): CLK4 (0.94), HOXB7 (0.87), VCF1 (0.81), SLC35A3 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB8B, member RAS oncogene family. RAB proteins, like RAB8B, are low molecular mass monomeric GTPases that localize on the cytoplasmic surfaces of distinct membrane-bound organelles. RAB proteins function in intracellular vesicle transport by aiding in the docking and/or fusion of vesicles with their target membranes (summary by Chen et al., 1997 [PubMed 9030196]).[supplied by OMIM, Nov 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.287); placenta praevia (0.192); tooth disorder (0.126); osteoarthritis, hip (0.095); infection (0.072)
- **Europe PMC papers**: 871
- **Why important**: RAB8B is a network connector linking CLK4, HOXB7, VCF1, and SLC35A3. Its established function is as a small GTPase involved in vesicle docking and fusion, exocytosis, endocytic recycling, cell-projection organization, and related transport processes. It is enhanced in bone marrow and in several hematopoietic or spermatid populations. The gene has a substantial literature base and provides a plausible trafficking component that connects otherwise diverse regulatory signals.
- **Conclusion**: Established evidence supports RAB8B as an intracellular membrane-trafficking regulator. Its module position supports a trafficking-related interpretation of part of the signal. A direct RAB8B-mediated mechanism linking the module to colon biology remains a hypothesis because STRING and hu.MAP provide no corroboration here.

#### KLF4

- **Related proteins** (co-abundance neighbors): SACK1D (0.82), HRAS (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: KLF transcription factor 4. This gene encodes a protein that belongs to the Kruppel family of transcription factors. The encoded zinc finger protein is required for normal development of the barrier function of skin. The encoded protein is thought to control the G1-to-S transition of the cell cycle following DNA damage by mediating the tumor suppressor gene p53. Mice lacking this gene have a normal appearance but lose weight…
- **Diseases (Open Targets)**: breast carcinoma (0.533); cutaneous melanoma (0.518); prostate carcinoma (0.504); neurodegenerative disease (0.489); osteoarthritis (0.413)
- **Europe PMC papers**: 33464
- **Why important**: KLF4 is a highly studied transcription factor with one of the strongest literature bases in the module. It connects SACK1D and HRAS, is enhanced in skin and in colonocytes, goblet cells, and esophageal epithelial populations, and is also enhanced in selected monocyte populations. Its established functions include epithelial barrier development, regulation of the cell-cycle transition after DNA damage, transcriptional control, and negative regulation of cell proliferation. Its disease associations include several carcinomas and melanoma.
- **Conclusion**: Established evidence supports KLF4 as an epithelial and cell-state transcriptional regulator with relevance to barrier biology, damage responses, and cancer. Its presence is consistent with a colon epithelial component in the shared module. The co-abundance data do not establish whether KLF4 regulates the other module genes or merely tracks a shared epithelial state.

#### AURKB

- **Related proteins** (co-abundance neighbors): CLK4 (0.92), RTEL1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aurora kinase B. This gene encodes a member of the aurora kinase subfamily of serine/threonine kinases. The genes encoding the other two members of this subfamily are located on chromosomes 19 and 20. These kinases participate in the regulation of alignment and segregation of chromosomes during mitosis and meiosis through association with microtubules. A pseudogene of this gene is located on chromosome 8. Alternat…
- **Diseases (Open Targets)**: neurodegenerative disease (0.562); Alzheimer disease (0.529); Parkinson disease (0.527); lysosomal storage disease (0.526); autoimmune disorder of central nervous system (0.445)
- **Europe PMC papers**: 5817
- **Why important**: AURKB connects CLK4 and RTEL1 and represents the clearest mitotic component of the selected genes. It is an established serine-threonine kinase involved in chromosome alignment and segregation, spindle organization, cytokinesis, and mitotic control. HPA associates it with bone marrow, lymphoid tissue, erythrocyte progenitors, enteric transient amplifying cells, and several proliferative developmental populations. Its disease literature is extensive and includes neurodegenerative and other disease associations.
- **Conclusion**: Established evidence supports AURKB as a mitotic and chromosome-segregation regulator. Its presence supports the possibility that the module reflects proliferative or differentiating cells in both contexts. It does not establish that the entire module is a cell-cycle module, because the enrichment analyses were globally negative and the network lacks known complex support.

## Module 3

**Tissue pair**: cell line and colon  
**Genes (9)**: APBA1, FGA, FGG, FTH1, HSPB7, MXRA5, PARVA, PLIN4, TNS1

### Function

The strongest interpretation is a fibrinogen-linked extracellular adhesion module with a secondary cell-adhesion and cytoskeletal component. The primary globally corrected evidence identifies heterotypic cell-cell adhesion (GO:BP heterotypic cell-cell adhesion; q_global = 0.021), the fibrinogen complex (GO:CC fibrinogen complex; q_global = 0.0363), and positive regulation of heterotypic cell-cell adhesion (GO:BP positive regulation of heterotypic cell-cell adhesion; q_global = 0.0472). FGA and FGG provide the clearest biochemical core, while PARVA connects the module to actin binding, focal adhesions, cell adhesion, motility, polarity, and survival. HSPB7, TNS1, and MXRA5 support a broader structural or matrix-associated context, whereas PLIN4, APBA1, and FTH1 may reflect tissue, cellular, or sample-state associations rather than a single unified biochemical pathway. The enrichment evidence supports an adhesion and fibrinogen-related interpretation, but does not establish that every module member participates in one molecular complex or pathway.

**Cell composition.** The module has a mixed composition rather than being a uniformly expressed housekeeping set. FGA and FGG are liver-enriched, hepatocyte-enriched proteins secreted to blood, making a circulating plasma or vascular contribution highly plausible. MXRA5 is secreted to extracellular matrix. The remaining genes are predominantly intracellular or membrane-associated, with HSPB7 associated with muscle cells, TNS1 with focal adhesions and vascular or stromal cell types, PLIN4 with adipocytes and lipid droplets, APBA1 with neuronal cells, PARVA with focal-adhesion and stromal-related cell types, and FTH1 with colonocytes, enterocytes, and other cells. Most genes are not detected in immune cells, so the module is not best explained as a blood-cell transcriptional program. The combination of liver-derived secreted proteins and adhesion or structural proteins raises the possibility that the shared signal reflects circulating protein carryover, vascular or stromal material, or shared cell-type composition in the samples. The absence of colon protein detection for FGA and FGG is consistent with, but does not prove, a non-colon-local source.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP heterotypic cell-cell adhesion | 0.021 | FGA, FGG, PARVA |
| GO:CC fibrinogen complex | 0.0363 | FGA, FGG |
| GO:BP positive regulation of heterotypic cell-cell adhesion | 0.0472 | FGA, FGG |

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module: the direct FGA-FGG interaction. This is expected because the two proteins are fibrinogen chains and strongly supports the fibrinogen core. STRING supplementary terms independently point to fibrinogen alpha or beta chain families, fibrinogen-related domains, thrombosis and anticoagulation, and congenital afibrinogenemia (4 supplementary STRING terms; within-query FDR 0.0082–0.0342); these are supportive annotations, not additional globally corrected enrichment results. The absence of STRING partners for the other module genes means that their co-abundance relationships are not established by the supplied STRING network, rather than disproving biological association. hu.MAP repeatedly places FGA and FGG together in broader protein-complex or plasma-protein assemblies (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1). Those complexes contain many other coagulation, complement, transport, acute-phase, and plasma proteins, so they support a known fibrinogen-centered extracellular context but do not establish a specific complex containing all module genes. Overall, known physical or curated relationships are concentrated in the FGA-FGG pair; the remaining edges are primarily co-abundance observations requiring independent validation.

**STRING interactions (score >= 0.7)**: 1 of 36 gene pairs: FGA–FGG (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Fibrinogen alpha/beta chain family (FDR = 0.0082, 2 genes); SMART Fibrinogen-related domains (FReDs) (FDR = 0.0148, 2 genes); WikiPathways COVID-19, thrombosis and anticoagulation (FDR = 0.0296, 2 genes); DISEASES Congenital afibrinogenemia (FDR = 0.0342, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02242.1 (FGA, FGG; 2/9); huMAP3_08224.1 (FGA, FGG; 2/21); huMAP3_09434.1 (FGA, FGG; 2/33); huMAP3_08395.1 (FGA, FGG; 2/43); huMAP3_09531.1 (FGA, FGG; 2/47); huMAP3_10101.1 (FGA, FGG; 2/49); huMAP3_15040.1 (FGA, FGG; 2/64); huMAP3_10678.1 (FGA, FGG; 2/71)

### Novelty

The fibrinogen-centered part of the module is not a new biological finding: FGA and FGG have a known direct relationship, established coagulation and adhesion functions, and repeated representation in hu.MAP plasma-protein assemblies. The potentially novel aspect is the particular cross-tissue co-abundance configuration linking this fibrinogen pair with HSPB7, PARVA, TNS1, PLIN4, MXRA5, APBA1, and FTH1. However, absence of those links from STRING or hu.MAP is insufficient to claim novelty, because database coverage, tissue context, assay effects, and indirect associations can all limit detection. The most defensible conclusion is that this is a potentially context-specific module configuration built around a known fibrinogen signal, not a demonstrably new molecular complex or pathway.

**Hypothesis.** Hypothesis: the shared module reflects a coordinated extracellular-interface state in which circulating fibrinogen contributes to adhesion and vascular or matrix interactions, while focal-adhesion and cytoskeletal proteins such as PARVA and TNS1 represent the responding structural cell compartment. HSPB7 may mark a muscle-like or contractile structural context, MXRA5 may represent matrix remodeling, and PLIN4 may indicate adipocyte or lipid-storage composition. In cell line and colon samples, the observed conservation could therefore arise from a combination of extracellular fibrinogen exposure or carryover and shared stromal, vascular, smooth-muscle, adipocyte, or epithelial composition. This hypothesis predicts that the FGA-FGG signal should track extracellular or plasma abundance, whereas the structural genes should track the relevant cell populations and adhesion or matrix state; it should not be treated as proof that all genes directly interact.

### Important genes

#### FGA

- **Related proteins** (co-abundance neighbors): FGG (0.89); STRING partners: FGG (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02242.1, huMAP3_08224.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: fibrinogen alpha chain. This gene encodes the alpha subunit of the coagulation factor fibrinogen, which is a component of the blood clot. Following vascular injury, the encoded preproprotein is proteolytically processed by thrombin during the conversion of fibrinogen to fibrin. Mutations in this gene lead to several disorders, including dysfibrinogenemia, hypofibrinogenemia, afibrinogenemia and renal amyloidosis. Alterna…
- **Diseases (Open Targets)**: familial dysfibrinogenemia (0.789); familial visceral amyloidosis (0.765); congenital afibrinogenemia (0.757); familial hypodysfibrinogenemia (0.659); congenital fibrinogen deficiency (0.619)
- **Europe PMC papers**: 7516
- **Why important**: FGA is a central biological anchor because it is one half of the only direct STRING relationship in the module, is present with FGG in every listed hu.MAP assembly, and contributes to all primary globally corrected terms (GO:BP heterotypic cell-cell adhesion; q_global = 0.021) (GO:CC fibrinogen complex; q_global = 0.0363) (GO:BP positive regulation of heterotypic cell-cell adhesion; q_global = 0.0472). It encodes a fibrinogen chain involved in blood coagulation, platelet activation, plasminogen activation, fibrinolysis, cell-matrix adhesion, and heterotypic cell-cell adhesion. Its liver and hepatocyte enrichment, secretion to blood, strong disease annotation for inherited fibrinogen disorders, and extensive literature make it the most established functional entry point.
- **Conclusion**: Established evidence supports FGA as a liver-derived, blood-secreted fibrinogen component that explains the module's adhesion and fibrinogen enrichment. The module data do not establish local production by colon cells or a direct interaction between FGA and the non-fibrinogen genes; those interpretations remain hypotheses.

#### FGG

- **Related proteins** (co-abundance neighbors): FGA (0.89), PLIN4 (0.83); STRING partners: FGA (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02242.1, huMAP3_08224.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: fibrinogen gamma chain. The protein encoded by this gene is the gamma component of fibrinogen, a blood-borne glycoprotein comprised of three pairs of nonidentical polypeptide chains. Following vascular injury, fibrinogen is cleaved by thrombin to form fibrin which is the most abundant component of blood clots. In addition, various cleavage products of fibrinogen and fibrin regulate cell adhesion and spreading, display va…
- **Diseases (Open Targets)**: familial dysfibrinogenemia (0.787); congenital afibrinogenemia (0.753); congenital fibrinogen deficiency (0.617); familial hypodysfibrinogenemia (0.597); cancer (0.596)
- **Europe PMC papers**: 4006
- **Why important**: FGG is the partner of FGA in the only supplied high-confidence STRING interaction and is present in all listed hu.MAP assemblies. It contributes to every primary enrichment term (GO:BP heterotypic cell-cell adhesion; q_global = 0.021) (GO:CC fibrinogen complex; q_global = 0.0363) (GO:BP positive regulation of heterotypic cell-cell adhesion; q_global = 0.0472) and every supplementary STRING term (4 supplementary STRING terms; within-query FDR 0.0082–0.0342). Its annotated roles include coagulation, platelet activation, plasminogen activation, cell-matrix adhesion, protein secretion, and positive regulation of heterotypic cell-cell adhesion. It is liver- and hepatocyte-enriched, secreted to blood, and strongly associated with inherited fibrinogen disorders.
- **Conclusion**: Established evidence identifies FGG as a core fibrinogen and extracellular-adhesion component, most plausibly representing a circulating or plasma-associated contribution. Its co-abundance with the other module genes does not by itself show that those genes form a shared fibrinogen complex.

#### PARVA

- **Related proteins** (co-abundance neighbors): HSPB7 (0.88), APBA1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Actin filaments, Focal adhesion sites; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: parvin alpha. This gene encodes a member of the parvin family of actin-binding proteins. Parvins are associated with focal contacts and contain calponin homology domains that bind to actin filaments. The encoded protein is part of the integrin-linked kinase signaling complex and plays a role in cell adhesion, motility and survival. [provided by RefSeq, Dec 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.487); osteoarthritis, hip (0.339); total hip arthroplasty (0.339); open-angle glaucoma (0.337); Pancreatic pseudocyst (0.331)
- **Europe PMC papers**: 3949
- **Why important**: PARVA is the only non-fibrinogen gene included in the primary heterotypic cell-cell adhesion overlap (GO:BP heterotypic cell-cell adhesion; q_global = 0.021). It is connected in the module to HSPB7 and APBA1 and is located at actin filaments and focal adhesion sites. Its established functions include actin binding, integrin-linked kinase signaling, cell adhesion, motility, survival, polarity, angiogenesis, and cytoskeletal organization. Its literature volume is substantial, and its cell-type profile includes adipocytes, podocytes, and smooth-muscle-related cells.
- **Conclusion**: Established evidence supports PARVA as the best intracellular bridge from the fibrinogen-centered extracellular signal to adhesion and cytoskeletal biology. A mechanistic role linking fibrinogen exposure to the module's cellular adhesion state is plausible, but the supplied network does not prove such signaling.

#### TNS1

- **Related proteins** (co-abundance neighbors): HSPB7 (0.84), PLIN4 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Focal adhesion sites; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tensin 1. The protein encoded by this gene localizes to focal adhesions, regions of the plasma membrane where the cell attaches to the extracellular matrix. This protein crosslinks actin filaments and contains a Src homology 2 (SH2) domain, which is often found in molecules involved in signal transduction. This protein is a substrate of calpain II. Alternative splicing results in multiple transcript variant…
- **Diseases (Open Targets)**: coronary artery disorder (0.555); chronic obstructive pulmonary disease (0.550); myocardial infarction (0.513); aortic stenosis (0.462); breast cancer (0.443)
- **Europe PMC papers**: 1434
- **Why important**: TNS1 is a focal-adhesion protein that crosslinks actin and contains a signaling-associated SH two domain. It is connected to HSPB7 and PLIN4, has a blood-vessel-enhanced tissue profile, and is associated with adipocytes, pericytes, and related stromal or contractile cell types. Its established annotations include cell-matrix adhesion and fibroblast migration, while disease associations include cardiovascular, pulmonary, and cancer-related conditions.
- **Conclusion**: Established evidence supports TNS1 as a structural and matrix-adhesion marker that could represent the cellular side of the module. Its participation in a fibrinogen-triggered mechanism is a hypothesis, not a demonstrated interaction, because it has no supplied STRING or hu.MAP relationship within this module.

#### HSPB7

- **Related proteins** (co-abundance neighbors): MXRA5 (0.91), PARVA (0.88), TNS1 (0.84), FTH1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family B (small) member 7. This gene encodes a small heat shock family B member that can heterodimerize with similar heat shock proteins. Defects in this gene are associated with advanced heart failure. In addition, the encoded protein may be a tumor suppressor in the p53 pathway, with defects in this gene being associated with renal cell carcinoma. [provided by RefSeq, Mar 2017].
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy (0.489); cardiomyopathy (0.337); systolic heart failure (0.290); cardioverter defibrillator (0.245); heart failure (0.233)
- **Europe PMC papers**: 866
- **Why important**: HSPB7 has the highest network connectivity and weighted strength in the module and links MXRA5, PARVA, TNS1, and FTH1. It is enriched in heart and skeletal muscle contexts and in several contractile or myoid cell types. Its established functions include response to unfolded protein, heart development, and regulation of heart contraction, and it has disease associations with cardiomyopathy and heart failure. It also has substantial literature support.
- **Conclusion**: Established evidence supports HSPB7 as a highly connected structural or muscle-associated module marker rather than as a fibrinogen component. Its position suggests that it may organize the non-fibrinogen co-abundance pattern, but the supplied data do not establish a physical mechanism connecting HSPB7 to FGA or FGG.

## Module 4

**Tissue pair**: cell line and colon  
**Genes (9)**: CCDC32, COL8A1, AMT, GDAP1, GRHL1, PICK1, RMP24, STX1A, TMEM87B

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING functional enrichment. The gene set is therefore not assigned a statistically supported pathway function. Its annotations nevertheless point to a heterogeneous cellular-trafficking and organelle-associated theme: PICK1 supports membrane-protein organization and receptor internalization; AMT participates in glycine cleavage; GDAP1 is associated with mitochondrial dynamics and neuronal development; STX1A mediates vesicle docking, fusion, exocytosis, and neurotransmitter secretion; TMEM87B is linked to endosome-to-Golgi retrograde transport; and the remaining genes include extracellular-matrix, epithelial-transcriptional, ciliary, and RNA-processing functions. The co-abundance pattern is best interpreted as a candidate shared expression program involving intracellular trafficking, neuronal or secretory biology, and epithelial or structural context rather than as an established biochemical pathway.

**Cell composition.** The module is not dominated by plasma or broadly secreted proteins. COL8A1 is secreted to the extracellular matrix, while the other entries are mainly intracellular, membrane, vesicular, mitochondrial, nucleolar, or nuclear proteins. HPA tissue specificity is mixed: several genes have low tissue specificity, whereas others show enhancement in brain, liver, blood vessel, esophagus, skin, or reproductive tissues. Cell-type annotations are especially prominent for neural and glial populations, but this does not establish that the module represents neural contamination in colon or cell-line samples. Immune-cell specificity is generally low, with isolated enhancement in NK cells or eosinophils, so a blood-cell explanation is not strongly supported. Protein detection in colon is broad among the genes with available data, whereas matching HPA protein data are unavailable for the cell-line context. The shared module could therefore reflect a conserved cell-state or epithelial-associated expression program, but sample composition and shared cell types remain alternative explanations.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

None of the possible gene-pair relationships reached the stated STRING interaction threshold, and no STRING functional enrichment was reported. No hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not corroborated by the supplied high-confidence physical-interaction or complex resources. This suggests that the network may represent coordinated expression, indirect regulation, shared cellular context, or technical and compositional effects rather than a known protein complex. It does not disprove biological coordination, because absence from these resources is not evidence that the proteins never interact.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a novel co-abundance association because its specific gene combination is not represented by a high-confidence STRING interaction network or a multi-member hu.MAP complex, and no established enriched pathway was recovered. However, these absences do not prove novelty. Several individual genes and functions are well established, including PICK1 in membrane organization, AMT in glycine cleavage, GDAP1 in mitochondrial and neuropathy biology, STX1A in vesicle fusion, COL8A1 in basement membrane biology, and GRHL1 in epithelial transcription. The potentially novel aspect is therefore the shared abundance pattern across cell line and colon, not the discovery of unknown functions for the individual genes. Independent replication, adjustment for cell composition, and validation at RNA and protein levels would be needed to support a new biological module.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of membrane and vesicle trafficking together with mitochondrial, epithelial, and extracellular-matrix states. PICK1 may provide a central expression-associated hub linking membrane organization to COL8A1, CCDC32, RMP24, and AMT, while the AMT–GDAP1–STX1A branch may couple mitochondrial or metabolic state with vesicle biology. GRHL1 and COL8A1 may capture epithelial or structural context in colon, whereas the neural and glial HPA annotations may reflect shared differentiation programs or expression in a particular cellular subpopulation. This is a mechanistic hypothesis rather than a demonstrated physical pathway, because global enrichment, STRING support, and hu.MAP support are absent.

### Important genes

#### PICK1

- **Related proteins** (co-abundance neighbors): COL8A1 (0.85), RMP24 (0.84), CCDC32 (0.83), AMT (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein interacting with PRKCA 1. The protein encoded by this gene contains a PDZ domain, through which it interacts with protein kinase C, alpha (PRKCA). This protein may function as an adaptor that binds to and organizes the subcellular localization of a variety of membrane proteins. It has been shown to interact with multiple glutamate receptor subtypes, monoamine plasma membrane transporters, as well as non-voltage gated sodiu…
- **Diseases (Open Targets)**: male infertility due to globozoospermia (0.370); Alzheimer disease (0.369); neurodegenerative disease (0.359); Parkinson disease (0.358); lysosomal storage disease (0.356)
- **Europe PMC papers**: 1566
- **Why important**: PICK1 is the most connected node in the module and links membrane-associated, mitochondrial-associated, and less characterized proteins. Its PDZ-domain adaptor function, interactions with membrane receptors and transporters, and roles in receptor internalization and intracellular transport provide a plausible organizing point for the observed co-abundance pattern. It also has substantial literature and disease associations spanning infertility and neurodegenerative disorders.
- **Conclusion**: Established evidence supports PICK1 as a membrane-trafficking and adaptor protein with a prominent position in this module. It is a strong candidate hub for follow-up. It remains unproven that PICK1 directly regulates the other module members or that it explains the shared abundance pattern.

#### AMT

- **Related proteins** (co-abundance neighbors): TMEM87B (0.87), GDAP1 (0.84), PICK1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aminomethyltransferase. This gene encodes one of four critical components of the glycine cleavage system. Mutations in this gene have been associated with glycine encephalopathy. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2011].
- **Diseases (Open Targets)**: glycine encephalopathy (0.830); glycine encephalopathy 1 (0.691); hereditary disease (0.495); Neurodevelopmental delay (0.425); infantile glycine encephalopathy (0.370)
- **Europe PMC papers**: 14866
- **Why important**: AMT is a highly connected intermediary joining PICK1, TMEM87B, and GDAP1. Its established role as a component of the glycine cleavage system and its strong association with glycine encephalopathy connect the module to mitochondrial metabolism and neural biology. HPA also places it in liver and several neural or glial cell types, making it informative for interpreting the mixed tissue context.
- **Conclusion**: Established evidence supports AMT as a mitochondrial glycine-metabolism protein with important neurological disease relevance. Its network position makes it a useful bridge candidate. The hypothesis that it couples metabolic state to membrane or vesicle trafficking in this module requires experimental testing.

#### GDAP1

- **Related proteins** (co-abundance neighbors): STX1A (0.87), AMT (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ganglioside induced differentiation associated protein 1. This gene encodes a member of the ganglioside-induced differentiation-associated protein family, which may play a role in a signal transduction pathway during neuronal development. Mutations in this gene have been associated with various forms of Charcot-Marie-Tooth Disease and neuropathy. Two transcript variants encoding different isoforms and a noncoding variant have been identified for this gen…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2K (0.833); Charcot-Marie-Tooth disease type 4A (0.803); Charcot-Marie-Tooth disease recessive intermediate A (0.784); autosomal dominant Charcot-Marie-Tooth disease type 2K (0.664); Charcot-Marie-Tooth disease (0.631)
- **Europe PMC papers**: 1052
- **Why important**: GDAP1 connects AMT with STX1A and is annotated for mitochondrial fission and fusion, neuronal development, and inherited neuropathies. Its brain-enhanced and neural-cell-associated HPA profile provides biological context for the neuronal features in the module, while its connection to a vesicle-fusion gene suggests a possible relationship between mitochondrial dynamics and secretion.
- **Conclusion**: Established evidence supports GDAP1 as a mitochondrial-dynamics and neuropathy-associated protein. Its placement between AMT and STX1A makes it a valuable mechanistic candidate. A direct role for GDAP1 in coordinating the complete module is only a hypothesis.

#### STX1A

- **Related proteins** (co-abundance neighbors): GDAP1 (0.87); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntaxin 1A. This gene encodes a member of the syntaxin superfamily. Syntaxins are nervous system-specific proteins implicated in the docking of synaptic vesicles with the presynaptic plasma membrane. Syntaxins possess a single C-terminal transmembrane domain, a SNARE [Soluble NSF (N-ethylmaleimide-sensitive fusion protein)-Attachment protein REceptor] domain (known as H3), and an N-terminal regulatory domain …
- **Diseases (Open Targets)**: Intellectual disability (0.568); autism (0.442); neurodevelopmental disorder (0.377); cystic fibrosis (0.374); botulism (0.370)
- **Europe PMC papers**: 3039
- **Why important**: STX1A is connected to GDAP1 and has a well-established role in synaptic-vesicle docking, vesicle fusion, exocytosis, and neurotransmitter secretion. Its brain and neuroendocrine cell-type associations and substantial literature make it the clearest vesicle-secretion marker in the module. Its presence may indicate a secretory or neuronal-like cellular state rather than a conventional colon-specific pathway.
- **Conclusion**: Established evidence supports STX1A as a vesicle-fusion and secretion protein with strong neural relevance. It is important for testing whether the module reflects a secretory cell state. The module data do not establish neuronal identity or direct interaction between STX1A and GDAP1.

#### COL8A1

- **Related proteins** (co-abundance neighbors): PICK1 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VIII alpha 1 chain. This gene encodes one of the two alpha chains of type VIII collagen. The gene product is a short chain collagen and a major component of the basement membrane of the corneal endothelium. The type VIII collagen fibril can be either a homo- or a heterotrimer. Alternatively spliced transcript variants encoding the same protein have been observed. [provided by RefSeq, Dec 2011].
- **Diseases (Open Targets)**: Inguinal hernia (0.444); open-angle glaucoma (0.412); glaucoma (0.403); Hernia (0.383); Hernia of the abdominal wall (0.382)
- **Europe PMC papers**: 2630
- **Why important**: COL8A1 is directly connected to the central PICK1 node and is the clearest extracellular-matrix and basement-membrane component in the module. Its blood-vessel tissue enrichment, extracellular-matrix secretion, colon protein detection, and associations with hernia and glaucoma provide a structural and tissue-interface perspective that contrasts with the intracellular neural annotations.
- **Conclusion**: Established evidence supports COL8A1 as a short-chain collagen involved in basement-membrane and extracellular-matrix biology. It may report epithelial, vascular, or stromal context in the shared module. A functional connection between COL8A1 and PICK1 is not established by the supplied interaction resources.

#### GRHL1

- **Related proteins** (co-abundance neighbors): RMP24 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: grainyhead like transcription factor 1. This gene encodes a member of the grainyhead family of transcription factors. The encoded protein can exist as a homodimer or can form heterodimers with sister-of-mammalian grainyhead or brother-of-mammalian grainyhead. This protein functions as a transcription factor during development. [provided by RefSeq, Jun 2009].
- **Diseases (Open Targets)**: prostate carcinoma (0.493); breast carcinoma (0.403); prostate cancer (0.397); basal cell carcinoma (0.371); skin cancer (0.306)
- **Europe PMC papers**: 721
- **Why important**: GRHL1 is connected to RMP24 and contributes an epithelial transcriptional interpretation through epidermis development and regulation of transcription. Its enrichment in esophagus, skin, and vagina and its association with epithelial cell types are relevant to interpreting the colon component. Its cancer associations also make it biologically consequential despite its peripheral network position.
- **Conclusion**: Established evidence supports GRHL1 as a developmental and epithelial transcription factor. It may indicate epithelial differentiation or barrier-state biology within the module. The fact sheet does not demonstrate that GRHL1 transcriptionally controls the other module genes.

## Module 5

**Tissue pair**: cell line and colon  
**Genes (7)**: C11orf96, GBP1, LPP, PCCB, PPP3CA, SELENBP1, MPST

### Function

No GO or KEGG term passed global correction, so there is no primary enrichment-based functional assignment for this module. The gene set is heterogeneous but suggests coordinated biology involving vascular or stromal cell features, cell adhesion and motility, interferon-associated host defense, calcium-regulated signaling, sulfur handling, and mitochondrial organic-acid metabolism. The strongest network organization is a hub-and-spoke pattern centered on C11orf96, while the only independently supported protein interaction is the MPST–SELENBP1 relationship (STRING KEGG Sulfur metabolism; within-query FDR = 0.0183). The module should therefore be interpreted as a tissue-associated co-abundance program rather than as an established single biochemical pathway.

**Cell composition.** All module genes have HPA tissue-enhanced annotations and all are detected by immunohistochemistry in colon. The enriched-tissue pattern spans blood vessel, liver, intestine, lymphoid tissue, and brain, indicating mixed tissue and cellular contributions rather than a narrowly colon-specific signature. Single-cell annotations include vascular smooth muscle cells, smooth muscle cells, colonocytes, enteric stem or transit-amplifying populations, and germ-cell populations. Most genes have low immune-cell specificity, although GBP1 and SELENBP1 have immune-cell-enhanced annotations and LPP is associated with neutrophils. One gene is annotated as secreted, whereas the remainder are not classified as secreted. The data do not support describing the module as predominantly plasma-protein or blood-cell derived, but shared vascular, stromal, epithelial, and limited immune composition could contribute to its conservation between cell line and colon.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports one high-confidence pair within the module: MPST with SELENBP1. These genes also jointly appear in the supplementary STRING sulfur-metabolism term (STRING KEGG Sulfur metabolism; within-query FDR = 0.0183), which is useful contextual evidence but is not global enrichment evidence. No other module pair is supported at the supplied STRING threshold. No hu.MAP complex contains multiple module members. Thus, the module has a small known sulfur-related interaction core embedded in a largely unconnected co-abundance network; the remaining edges may reflect correlated abundance, indirect regulation, shared cell composition, or interactions not represented in the queried resources.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: MPST–SELENBP1 (0.854)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Sulfur metabolism (FDR = 0.0183, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The conserved co-abundance pattern may be a new observation in this tissue-pair analysis, particularly because most module relationships are absent from the supplied STRING and hu.MAP evidence. However, absence from those resources does not establish novelty. The lack of globally significant GO or KEGG enrichment, the absence of a multi-member hu.MAP complex, and the presence of only one supported STRING interaction make a claim of a newly discovered molecular complex or pathway premature. The defensible novelty claim is limited to the reproducible association of these genes in the present cell-line and colon co-abundance context, pending replication and experimental testing.

**Hypothesis.** Hypothesis: the module reflects a shared abundance program linking a vascular or stromal structural state, epithelial or intestinal metabolic activity, and context-dependent host-defense signaling. C11orf96 may act as the abundance-level hub connecting LPP-associated adhesion biology, GBP1-associated interferon-responsive defense, PPP3CA-associated calcium and dephosphorylation signaling, and the SELENBP1–MPST sulfur-handling pair, with PCCB representing mitochondrial propionyl-CoA and short-chain metabolic activity. This is a co-regulation or shared-cell-state hypothesis, not evidence that C11orf96 physically binds all neighboring proteins or that the module constitutes one biochemical complex.

### Important genes

#### C11orf96

- **Related proteins** (co-abundance neighbors): LPP (0.94), GBP1 (0.88), PPP3CA (0.86), SELENBP1 (0.85), MPST (0.83), PCCB (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Nucleoplasm, Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromosome 11 open reading frame 96
- **Diseases (Open Targets)**: neurodegenerative disease (0.415); gram-negative bacterial infections (0.301); head injury (0.160); hearing loss, autosomal recessive (0.092); deafness (0.092)
- **Europe PMC papers**: 483
- **Why important**: C11orf96 is the central network hub, connecting every other module member with the strongest overall network integration in the supplied graph. HPA places it in blood-vessel-associated tissue and pericyte or smooth-muscle-related cell populations, with nucleoplasmic and cytosolic localization. Its disease associations include neurodegenerative disease, gram-negative bacterial infection, head injury, and inherited hearing disorders, but its functional annotation and literature base are more limited than those of several neighboring genes.
- **Conclusion**: Established evidence supports C11orf96 as the organizational hub of this co-abundance module and as a marker associated with vascular or mural-cell biology. Its causal molecular function in the module remains unresolved. The possibility that it coordinates the other abundance patterns is a hypothesis requiring perturbation, localization, and interaction experiments.

#### LPP

- **Related proteins** (co-abundance neighbors): C11orf96 (0.94); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Focal adhesion sites, Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LIM domain containing preferred translocation partner in lipoma. This gene encodes a member of a subfamily of LIM domain proteins that are characterized by an N-terminal proline-rich region and three C-terminal LIM domains. The encoded protein localizes to the cell periphery in focal adhesions and may be involved in cell-cell adhesion and cell motility. This protein also shuttles through the nucleus and may function as a transcriptional co-activator. This gene …
- **Diseases (Open Targets)**: asthma (0.569); basal cell carcinoma (0.569); hypothyroidism (0.538); respiratory system disorder (0.522); open-angle glaucoma (0.517)
- **Europe PMC papers**: 6712
- **Why important**: LPP is the module member most directly associated with focal-adhesion sites, cell periphery localization, cell-cell adhesion, and cell motility. It is linked to vascular and smooth-muscle populations and is the only direct peripheral structural partner of the C11orf96 hub in the supplied graph. Its extensive literature and disease associations involving asthma, basal-cell carcinoma, hypothyroidism, respiratory disorders, and glaucoma make it a strong biological anchor for the adhesion or stromal interpretation.
- **Conclusion**: Established evidence supports LPP as an adhesion and motility-related component that could report vascular or stromal cell state. Its co-abundance with C11orf96 does not demonstrate direct physical binding or prove that adhesion drives the whole module. A role for LPP in transmitting a structural-cell state to the other genes is therefore a hypothesis.

#### GBP1

- **Related proteins** (co-abundance neighbors): C11orf96 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: guanylate binding protein 1. Guanylate binding protein expression is induced by interferon. Guanylate binding proteins are characterized by their ability to specifically bind guanine nucleotides (GMP, GDP, and GTP) and are distinguished from the GTP-binding proteins by the presence of 2 binding motifs rather than 3. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: bacterial infectious disease (0.528); Orthomyxoviridae infectious disease (0.374); neurodegenerative disease (0.302); muscular disease (0.195); neoplasm (0.116)
- **Europe PMC papers**: 3935
- **Why important**: GBP1 provides the clearest host-defense component of the module. It is interferon-induced, binds guanine nucleotides, and is annotated for innate defense, responses to bacteria and protozoa, interleukin signaling, calcium-mediated signaling, and T-cell receptor regulation. It has liver and lymphoid tissue enhancement, is detected in colon, and has disease associations led by bacterial and viral infectious disease. Its substantial literature makes its biological interpretation comparatively well established.
- **Conclusion**: Established evidence supports GBP1 as an intracellular or membrane-associated defense and interferon-responsive marker. The module does not establish active infection or an immune mechanism, especially given GBP1's low overall immune-cell specificity in HPA. Its coordinated abundance with vascular, epithelial, and metabolic genes may reflect inflammatory signaling or shared cellular composition; this remains a hypothesis.

#### SELENBP1

- **Related proteins** (co-abundance neighbors): C11orf96 (0.85); STRING partners: MPST (0.854)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoli; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: selenium binding protein 1. This gene encodes a member of the selenium-binding protein family. Selenium is an essential nutrient that exhibits potent anticarcinogenic properties, and deficiency of selenium may cause certain neurologic diseases. The effects of selenium in preventing cancer and neurologic diseases may be mediated by selenium-binding proteins, and decreased expression of this gene may be associated with several…
- **Diseases (Open Targets)**: extraoral halitosis due to methanethiol oxidase deficiency (0.694); type 2 diabetes mellitus (0.265); neoplasm (0.114); colorectal carcinoma (0.103); lung adenocarcinoma (0.103)
- **Europe PMC papers**: 1503
- **Why important**: SELENBP1 is one half of the only supported STRING interaction in the module and is paired with MPST in the supplementary sulfur-metabolism signal (STRING KEGG Sulfur metabolism; within-query FDR = 0.0183). It is intestine-enhanced, associated with colonocytes and enteric progenitor populations, localized to nucleoli, and linked to selenium biology, ubiquitination or deubiquitination-related mechanisms, cancer-related expression changes, methanethiol oxidase deficiency, type two diabetes, and colorectal carcinoma.
- **Conclusion**: Established evidence supports SELENBP1 as an intestinally relevant component with a known network relationship to MPST and a plausible sulfur-related context. The supplied data do not establish that SELENBP1 controls sulfur metabolism in this module, nor that its cancer associations explain the co-abundance pattern. Its role as an intestinal metabolic or stress-state marker is a reasonable hypothesis.

#### MPST

- **Related proteins** (co-abundance neighbors): C11orf96 (0.83); STRING partners: SELENBP1 (0.854)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mercaptopyruvate sulfurtransferase. This protein encoded by this gene catalyzes the transfer of a sulfur ion from 3-mercaptopyruvate to cyanide or other thiol compounds. It may be involved in cysteine degradation and cyanide detoxification. There is confusion in literature between this protein (mercaptopyruvate sulfurtransferase, MPST), which appears to be cytoplasmic, and thiosulfate sulfurtransferase (rhodanese, TST, GeneID:7263),…
- **Diseases (Open Targets)**: neurodegenerative disease (0.261); COVID-19 (0.164); severe acute respiratory syndrome (0.163); colitis (0.080); non-alcoholic fatty liver (0.078)
- **Europe PMC papers**: 1532
- **Why important**: MPST is the other member of the supported STRING pair with SELENBP1 and has the same supplementary sulfur-metabolism context (STRING KEGG Sulfur metabolism; within-query FDR = 0.0183). It catalyzes sulfur transfer from mercaptopyruvate to cyanide or other thiol compounds and is linked to cysteine degradation, cyanide detoxification, sulfur-amino-acid catabolism, toxic-substance response, and liver development. HPA identifies liver enhancement and enrichment across colonocyte and enteric populations, while disease associations include neurodegenerative disease, viral respiratory disease, colitis, and fatty-liver disease.
- **Conclusion**: Established evidence supports MPST as a sulfur-transfer and detoxification enzyme with intestinal and hepatic relevance, and supports its network relationship with SELENBP1. The module does not prove that sulfur flux is the organizing mechanism for all seven genes. A sulfur-redox or epithelial metabolic state linking MPST and SELENBP1 to the wider module is a hypothesis.

#### PPP3CA

- **Related proteins** (co-abundance neighbors): C11orf96 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase 3 catalytic subunit alpha. Enables several functions, including ATPase binding activity; calmodulin binding activity; and calmodulin-dependent protein phosphatase activity. Involved in several processes, including calcineurin-NFAT signaling cascade; peptidyl-serine dephosphorylation; and response to calcium ion. Located in several cellular components, including cytosol; dendritic spine; and nucleoplasm. Part of calcineurin …
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy 91 (0.796); arthrogryposis, cleft palate, craniosynostosis, and impaired intellectual development (0.706); lupus nephritis (0.561); type 2 diabetes mellitus (0.483); infantile epileptic encephalopathy (0.462)
- **Europe PMC papers**: 2097
- **Why important**: PPP3CA connects the module to calcineurin-related calcium signaling, calmodulin-dependent phosphatase activity, protein dephosphorylation, signaling regulation, epidermal differentiation, and cell migration. It is brain-enhanced, detected in colon, and annotated in neuronal and neutrophil-related cell populations. Its disease associations include developmental and epileptic encephalopathy, syndromic developmental disorders, lupus nephritis, type two diabetes, and infantile epileptic encephalopathy. In the network it is a peripheral member linked to the C11orf96 hub.
- **Conclusion**: Established evidence supports PPP3CA as a calcium-responsive signaling and dephosphorylation component with important disease relevance. Its presence does not establish neuronal biology in the colon module, because HPA also reports non-neuronal cell associations. A calcium-dependent signaling bridge between structural-cell state and host-defense or epithelial responses is a hypothesis.

## Module 6

**Tissue pair**: cell line and colon  
**Genes (7)**: RCSD1, ELMOD2, ARHGDIB, GMFG, HCLS1, ITGAL, SLC1A4

### Function

The module most plausibly reflects a leukocyte-associated cytoskeletal, adhesion, and signaling program rather than a narrowly defined biochemical pathway. ITGAL is the most connected node and encodes the alpha chain of LFA-1, a leukocyte integrin involved in intercellular adhesion. ARHGDIB links the module to Rho-family signaling and cytoskeletal organization, HCLS1 to hematopoietic-cell signaling and actin organization, and GMFG to Arp2/3-associated actin remodeling. RCSD1 is annotated for actin filament binding, while SLC1A4 contributes neutral amino-acid transport. The supplementary STRING results support an immune-tissue association (STRING TISSUES Lymph; within-query FDR = 0.00087) and actin-cytoskeleton reorganization (STRING Process Regulation of actin cytoskeleton reorganization; within-query FDR = 0.019). However, no GO or KEGG term passed global correction, so these annotations should be interpreted as functional context rather than statistically confirmed enrichment. The network therefore supports a broad leukocyte adhesion and motility hypothesis, with cytoskeletal regulation as a central theme.

**Cell composition.** The module is strongly characterized by hematopoietic and lymphoid expression patterns rather than by plasma or secreted proteins. HPA tissue annotations frequently point to lymphoid tissue and bone marrow, and single-cell annotations commonly include monocytes, neutrophil-lineage cells, Kupffer cells, macrophages, and related hematopoietic populations. The module contains no secreted genes. Most genes are labelled with low immune-cell specificity in the HPA summary, so the evidence does not establish a uniform blood-cell signature; nevertheless, the repeated lymphoid, myeloid, and bone-marrow associations make shared immune-cell composition or a shared leukocyte state a plausible explanation for conservation between cell line and colon. Colon protein detection is mixed, and the cell-line comparison has no matching HPA tissue protein data, so the module should not be interpreted as a colon epithelial program without further cell-composition controls.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes, and no hu.MAP complex contains multiple module members. Thus, the co-abundance relationships are not simply recapitulating a documented physical interaction network or a known multiprotein complex. STRING nevertheless provides supplementary functional context: ARHGDIB, SLC1A4, HCLS1, and ITGAL occur in the lymphoid-tissue result (STRING TISSUES Lymph; within-query FDR = 0.00087), while ARHGDIB, HCLS1, and GMFG occur in the actin-cytoskeleton-reorganization result (STRING Process Regulation of actin cytoskeleton reorganization; within-query FDR = 0.019). These results are consistent with the proposed immune adhesion and cytoskeletal interpretation, but they do not establish direct molecular interactions or globally significant enrichment.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Lymph (FDR = 0.00087, 4 genes); Process Regulation of actin cytoskeleton reorganization (FDR = 0.019, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be called a newly discovered molecular complex or pathway. Its component functions, immune associations, adhesion biology, Rho signaling, and actin-regulatory roles are already established to varying degrees, and the absence of STRING or hu.MAP support does not by itself demonstrate novelty. The potentially novel observation is the reproducible co-abundance configuration shared by cell line and colon, particularly the association of ITGAL and RCSD1 with actin- and hematopoietic-related genes despite the lack of a known shared complex. This is best regarded as a novel systems-level association that generates a testable hypothesis, not as proof of a new mechanism.

**Hypothesis.** Hypothesis: the module represents a shared leukocyte-associated state in which integrin-mediated adhesion and cell-cell contact are coordinated with Rho-family regulation and actin-network remodeling. ITGAL may mark the adhesion component, ARHGDIB and HCLS1 may connect signaling to cytoskeletal organization, and GMFG and RCSD1 may influence actin architecture or motility. SLC1A4 may reflect the metabolic or amino-acid transport requirements of the associated cell state, while ELMOD2 may contribute a broader stress or defense-response context. In colon samples, the module could therefore arise from immune-cell abundance or immune-cell activity, and in the cell-line context it could reflect a related hematopoietic-like state or shared sample composition. This hypothesis requires validation with cell deconvolution, independent cohorts, protein-level measurements, and perturbation of adhesion or actin-regulatory pathways.

### Important genes

#### ITGAL

- **Related proteins** (co-abundance neighbors): ELMOD2 (0.85), SLC1A4 (0.85), GMFG (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha L. ITGAL encodes the integrin alpha L chain. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain. This I-domain containing alpha integrin combines with the beta 2 chain (ITGB2) to form the integrin lymphocyte function-associated antigen-1 (LFA-1), which is expressed on all leukocytes. LFA-1 plays a central role in leukocyte intercellular adhesion through…
- **Diseases (Open Targets)**: psoriasis vulgaris (0.585); dry eye syndrome (0.568); psoriasis (0.473); eye disorder (0.371); ulcerative colitis (0.336)
- **Europe PMC papers**: 2930
- **Why important**: ITGAL is the most network-connected gene in the module and links to ELMOD2, SLC1A4, and GMFG. It encodes the alpha chain of LFA-1, a leukocyte integrin central to leukocyte adhesion and interactions with ICAM ligands. HPA links it to bone marrow, lymphoid tissue, B-cells, microglia, monocytes, and neutrophil progenitors, while Open Targets associates it with inflammatory and immune-related disorders including ulcerative colitis. Its extensive literature base makes it the strongest established biological anchor for the module.
- **Conclusion**: Established evidence supports ITGAL as an immune-cell adhesion marker and a plausible organizing signal for the module. Hypothesis: its co-abundance with actin-regulatory genes reflects coordinated leukocyte adhesion or motility rather than a direct physical complex.

#### ARHGDIB

- **Related proteins** (co-abundance neighbors): RCSD1 (0.85); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho GDP dissociation inhibitor beta. Members of the Rho (or ARH) protein family (see MIM 165390) and other Ras-related small GTP-binding proteins (see MIM 179520) are involved in diverse cellular events, including cell signaling, proliferation, cytoskeletal organization, and secretion. The GTP-binding proteins are active only in the GTP-bound state. At least 3 classes of proteins tightly regulate cycling between the GTP-bound and GDP…
- **Diseases (Open Targets)**: placental abruption (0.122); gastric cancer (0.109); diabetes mellitus (0.105); breast cancer (0.099); neoplasm (0.095)
- **Europe PMC papers**: 1089
- **Why important**: ARHGDIB connects to RCSD1 and appears in both supplementary STRING contexts (STRING TISSUES Lymph; within-query FDR = 0.00087) and (STRING Process Regulation of actin cytoskeleton reorganization; within-query FDR = 0.019). It regulates Rho-family signaling, a major control point for cytoskeletal organization, cell shape, migration, and signaling. HPA associates it with bone marrow and lymphoid tissue and with several hematopoietic and tissue-macrophage populations. Its disease associations include placental, metabolic, and neoplastic conditions, and it has a substantial literature base.
- **Conclusion**: Established evidence supports ARHGDIB as a cytoskeletal-signaling regulator with hematopoietic relevance. Hypothesis: ARHGDIB may connect integrin-associated adhesion to the actin remodeling state represented by this module.

#### HCLS1

- **Related proteins** (co-abundance neighbors): RCSD1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hematopoietic cell-specific Lyn substrate 1. Enables RNA polymerase II-specific DNA-binding transcription factor binding activity and protein kinase binding activity. Involved in several processes, including positive regulation of intracellular signal transduction; positive regulation of protein phosphorylation; and regulation of transcription, DNA-templated. Located in cytosol; nucleus; and plasma membrane. Part of transcription regulator c…
- **Diseases (Open Targets)**: duodenitis (0.191); atrial fibrillation (0.120); colorectal carcinoma (0.067); neoplasm (0.062); systemic lupus erythematosus (0.052)
- **Europe PMC papers**: 1012
- **Why important**: HCLS1 is connected to RCSD1 and is included in both supplementary STRING results (STRING TISSUES Lymph; within-query FDR = 0.00087) and (STRING Process Regulation of actin cytoskeleton reorganization; within-query FDR = 0.019). It is a hematopoietic-cell-associated signaling protein annotated for protein-kinase binding, intracellular signal transduction, actin organization, and transcriptional regulation. HPA links it to bone marrow, lymphoid tissue, monocytes, macrophages, Kupffer cells, and monocyte progenitors. Its literature and disease-association records are comparatively extensive, including inflammatory and colorectal disease relevance.
- **Conclusion**: Established evidence supports HCLS1 as a hematopoietic signaling and actin-organization component. Hypothesis: HCLS1 may act as a signaling-to-cytoskeleton relay within the shared co-abundance state.

#### GMFG

- **Related proteins** (co-abundance neighbors): RCSD1 (0.82), ITGAL (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glia maturation factor gamma. Predicted to enable Arp2/3 complex binding activity. Predicted to be involved in actin filament debranching and negative regulation of Arp2/3 complex-mediated actin nucleation. Predicted to be located in extracellular region; ficolin-1-rich granule lumen; and secretory granule lumen. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: breast cancer (0.098); breast carcinoma (0.097); cancer (0.083); glioblastoma (0.083); lung carcinoma (0.082)
- **Europe PMC papers**: 425
- **Why important**: GMFG occupies a bridging position between RCSD1 and ITGAL and is the module member most directly annotated for Arp2/3-related actin regulation. It is associated with actin filament debranching and negative regulation of Arp2/3-mediated actin nucleation, and it appears in the supplementary actin-cytoskeleton result (STRING Process Regulation of actin cytoskeleton reorganization; within-query FDR = 0.019). HPA links it to bone marrow, lymphoid tissue, dendritic cells, hematopoietic progenitors, and tissue macrophages. Its disease literature is smaller than that of ITGAL or HCLS1, but it provides a mechanistically specific actin-remodeling link.
- **Conclusion**: Established evidence supports GMFG as an actin-network regulator in hematopoietic contexts. Hypothesis: GMFG may tune the actin architecture required for integrin-dependent adhesion or migration in the module-associated cells.

#### RCSD1

- **Related proteins** (co-abundance neighbors): ARHGDIB (0.85), HCLS1 (0.82), GMFG (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RCSD domain containing 1. Enables actin filament binding activity. Involved in cellular hyperosmotic response. Predicted to be located in actin filament. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Bicuspid aortic valve (0.291); lobular capilliary hemangioma (0.230); alcohol drinking (0.229); stroke disorder (0.229); venous thromboembolism (0.219)
- **Europe PMC papers**: 321
- **Why important**: RCSD1 is among the most connected nodes and links ARHGDIB, HCLS1, and GMFG, placing it at the intersection of the module’s Rho-signaling and actin-regulatory components. It is annotated for actin filament binding, endosomal protein localization, and cellular hyperosmotic response. HPA associates it with lymphoid tissue, skeletal muscle, B-cells, hematopoietic stem cells, innate lymphoid cells, Kupffer cells, and macrophages. Its literature volume is more limited, which makes its repeated network position especially useful for prioritizing follow-up.
- **Conclusion**: Established evidence supports RCSD1 as an actin-associated protein with hematopoietic and lymphoid expression context. Hypothesis: RCSD1 may be an under-characterized scaffold or regulator that helps couple Rho-related signaling to actin remodeling in this conserved module.

## Module 7

**Tissue pair**: cell line and colon  
**Genes (5)**: HOXB9, OTULIN, SERAC1, TXNDC16, WDR81

### Function

The module has no single established function from enrichment analysis: no GO or KEGG term passed global correction, and there was no supplementary STRING enrichment. Its co-abundance structure links TXNDC16 most centrally with SERAC1, WDR81, and OTULIN, while WDR81 links to HOXB9. The annotations suggest a mixed biology involving organelle and membrane homeostasis, lipid and cholesterol handling, endolysosomal trafficking, ubiquitin-dependent inflammatory regulation, and transcriptional control of differentiation. These annotations support biological plausibility but do not establish that the module is a unified pathway.

**Cell composition.** This is not predominantly a plasma-protein, secreted-protein, or blood-cell module. Only TXNDC16 is annotated as secreted to blood, while the other genes are not secreted; the HPA summary reports low immune-cell specificity for most genes and no enriched blood-cell group. Most genes have low tissue specificity, with cell-type enhancement or group enrichment concentrated in epithelial, reproductive, renal, hepatic, neural, and related cell types. HOXB9 shows tissue enhancement in intestine among other tissues, and several module proteins are detected in colon, but the pattern does not by itself demonstrate a colon-specific cellular source. The module could therefore reflect a broadly distributed cellular program or shared cell-state composition rather than a specialized blood signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported for any module pair, and no hu.MAP complex contains multiple module members. Thus, the co-abundance edges should not be interpreted as established physical interactions or as a known protein complex. Established biology instead comes from individual gene annotations: SERAC1 participates in phospholipid remodeling and intracellular cholesterol transport; WDR81 is associated with endolysosomal trafficking and protein quality control; OTULIN removes linear ubiquitin chains and regulates inflammatory signaling; HOXB9 is a transcription factor involved in proliferation and differentiation; and TXNDC16 is associated with an organelle-localized thioredoxin-domain protein. The network may capture coordinated abundance without direct molecular binding.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The particular co-abundance combination may be an under-described association, because it is not represented as a supported STRING interaction set or a shared hu.MAP complex. However, that absence does not prove novelty: the module has no globally significant GO or KEGG annotation, no STRING enrichment, and no independent experimental validation in the fact sheet. The most defensible conclusion is that it is a potentially novel co-abundance pattern whose biological interpretation remains provisional rather than a confirmed new molecular complex or pathway.

**Hypothesis.** Mechanistic hypothesis: the module reflects coordinated regulation of organelle and membrane homeostasis together with cellular stress and inflammatory control. In this model, TXNDC16 may provide an organelle-associated connection between SERAC1-dependent lipid remodeling and WDR81-dependent trafficking or protein quality control, while OTULIN tunes ubiquitin-linked inflammatory signaling and HOXB9 represents a transcriptional state associated with differentiation or tissue context. This is a hypothesis based on co-abundance and individual annotations, not an established physical mechanism.

### Important genes

#### TXNDC16

- **Related proteins** (co-abundance neighbors): SERAC1 (0.89), WDR81 (0.86), OTULIN (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin domain containing 16. Located in endoplasmic reticulum lumen. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: obesity due to melanocortin 4 receptor deficiency (0.044); Obesity due to MC3R deficiency (0.044); eye disorder (0.041); hemorrhage (0.025); gastric ulcer (0.025)
- **Europe PMC papers**: 113
- **Why important**: TXNDC16 is the most connected node in the module and links SERAC1, WDR81, and OTULIN. Its annotation places it in an organelle-associated context, and it is secreted to blood according to HPA, although its immune-cell specificity is low. It has disease associations involving metabolic, ocular, hemorrhagic, and gastrointestinal phenotypes and a meaningful literature record. Its central network position makes it the strongest candidate for coordinating the module, while its precise molecular role remains incompletely defined.
- **Conclusion**: Established evidence supports TXNDC16 as the network hub and as an organelle-associated protein with reported disease links. It is a plausible candidate coordinator of the module, but the proposed coordinating role is hypothetical because no STRING or hu.MAP relationship supports direct interaction.

#### WDR81

- **Related proteins** (co-abundance neighbors): TXNDC16 (0.86), HOXB9 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 81. This gene encodes a multi-domain transmembrane protein which is predominantly expressed in the brain and is thought to play a role in endolysosomal trafficking. Mutations in this gene are associated with an autosomal recessive form of a syndrome exhibiting cerebellar ataxia, cognitive disability, and disequilibrium (CAMRQ2). Alternatively spliced transcript variants encoding different isoforms hav…
- **Diseases (Open Targets)**: cerebellar ataxia, intellectual disability, and dysequilibrium (0.784); cerebellar ataxia, intellectual disability, and dysequilibrium syndrome 2 (0.769); hydrocephalus, congenital, 3, with brain anomalies (0.711); hereditary ataxia (0.561); hereditary disease (0.471)
- **Europe PMC papers**: 348
- **Why important**: WDR81 connects TXNDC16 with HOXB9 and has the clearest annotation for intracellular trafficking and protein quality control, including early endosome to late endosome transport, aggrephagy, protein stabilization, and mitochondrial organization. It is associated with a defined recessive neurodevelopmental syndrome and has a substantial literature record. Its broad cell-type enhancement is compatible with a general cellular maintenance role rather than a blood-specific signal.
- **Conclusion**: Established evidence supports WDR81 as an endolysosomal and cellular quality-control protein with disease relevance. Its position between TXNDC16 and HOXB9 makes it a plausible bridge between organelle homeostasis and tissue-state regulation, but that bridge is a hypothesis rather than a demonstrated interaction.

#### SERAC1

- **Related proteins** (co-abundance neighbors): TXNDC16 (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine active site containing 1. The protein encoded by this gene is a phosphatidylglycerol remodeling protein found at the interface of mitochondria and endoplasmic reticula, where it mediates phospholipid exchange. The encoded protein plays a major role in mitochondrial function and intracellular cholesterol trafficking. Defects in this gene are a cause of 3-methylglutaconic aciduria with deafness, encephalopathy, and Leigh-lik…
- **Diseases (Open Targets)**: 3-methylglutaconic aciduria with deafness, encephalopathy, and Leigh-like syndrome (0.832); hereditary disease (0.470); Leigh syndrome (0.405); dystonic disorder (0.374); Hypoglycemia (0.370)
- **Europe PMC papers**: 365
- **Why important**: SERAC1 is directly connected to TXNDC16 and has a well-defined role in phosphatidylglycerol remodeling, mitochondrial function, and intracellular cholesterol trafficking. Its pathogenic variants cause a severe mitochondrial and metabolic disorder, giving it strong functional and disease relevance. HPA detects it in colon, while its cell-type enhancement is concentrated in spermatid populations, indicating that its abundance may be sensitive to cellular composition.
- **Conclusion**: Established evidence supports SERAC1 as a mitochondrial and membrane-lipid homeostasis factor with major disease importance. It is a credible contributor to an organelle and lipid-related module, but the co-abundance data do not establish that it acts directly with TXNDC16.

#### OTULIN

- **Related proteins** (co-abundance neighbors): TXNDC16 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OTU deubiquitinase with linear linkage specificity. This gene encodes a member of the peptidase C65 family of ubiquitin isopeptidases. Members of this family remove ubiquitin from proteins. The encoded enzyme specifically recognizes and removes M1(Met1)-linked, or linear, ubiquitin chains from protein substrates. Linear ubiquitin chains are known to regulate the NF-kappa B signaling pathway in the context of immunity and inflammation. Mutations in …
- **Diseases (Open Targets)**: autoinflammation, panniculitis, and dermatosis syndrome, autosomal recessive (0.808); immunodeficiency 107, susceptibility to invasive staphylococcus aureus infection (0.682); autoinflammation, panniculitis, and dermatosis syndrome (0.559); craniometaphyseal dysplasia (0.508); Alzheimer disease (0.409)
- **Europe PMC papers**: 1229
- **Why important**: OTULIN is connected to TXNDC16 and has the strongest literature and disease relevance among the module genes. It specifically regulates linear ubiquitin chains and is annotated in innate immunity, inflammatory regulation, tumor necrosis factor signaling, angiogenesis, and Wnt regulation. Its association with severe autoinflammatory and immunodeficiency phenotypes makes it biologically important even though HPA indicates low immune-cell specificity in this module.
- **Conclusion**: Established evidence supports OTULIN as a regulator of linear-ubiquitin signaling and inflammatory control with substantial human disease relevance. Its inclusion suggests that inflammatory or stress signaling could influence the module, but a direct mechanistic connection to the organelle-associated genes remains hypothetical.

#### HOXB9

- **Related proteins** (co-abundance neighbors): WDR81 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: homeobox B9. This gene is a member of the Abd-B homeobox family and encodes a protein with a homeobox DNA-binding domain. It is included in a cluster of homeobox B genes located on chromosome 17. The encoded nuclear protein functions as a sequence-specific transcription factor that is involved in cell proliferation and differentiation. Increased expression of this gene is associated with some cases of leukemia…
- **Diseases (Open Targets)**: neurodegenerative disease (0.536); movement disorder (0.354); restless legs syndrome (0.336); Parkinson disease (0.286); Alzheimer disease (0.284)
- **Europe PMC papers**: 1639
- **Why important**: HOXB9 is the transcriptional endpoint of the WDR81 branch and encodes a sequence-specific homeobox transcription factor involved in proliferation, differentiation, and developmental patterning. It shows tissue enhancement in intestine as well as other tissues and is not detected in immune cells, which may be relevant to the shared cell-line and colon context. It has extensive literature and reported associations with leukemia and several cancers.
- **Conclusion**: Established evidence supports HOXB9 as a developmental and differentiation-related transcription factor with cancer relevance. Its network placement may indicate a tissue or cell-state component of the module, but the data do not show that HOXB9 transcriptionally regulates the other module genes.
