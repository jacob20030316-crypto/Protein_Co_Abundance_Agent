# Conserved co-abundance modules: circulatory_system and testis

## Module 0

**Tissue pair**: circulatory_system and testis  
**Genes (36)**: ALDH16A1, AMPD2, CA2, CALD1, CORO1B, DCTN1, DNM1L, APPL2, EPS15L1, FGA, FGB, FGG, GBP2, GPD2, GRIPAP1, ITGB1, CAMK1, KLC1, PRKCA, PRKCD, LPP, LRBA, MICAL1, MYLK, NCKAP1, NHLRC2, NSF, NUCB1, PDIA5, PYGB, CTTN, STXBP2, LARS1, TF, USP13, XPNPEP1

### Function

The strongest interpretation is a blood-interface and cell-surface trafficking module. The globally corrected GO evidence supports regulation of transport and localization (GO:BP regulation of transport; q_global = 0.0015) (GO:BP positive regulation of transport; q_global = 0.00307) (GO:BP regulation of localization; q_global = 0.0114), vesicle-mediated transport and exocytosis (5 globally significant GO/KEGG terms, q_global 0.00576–0.0354; see the table), and plasma-membrane and cell-periphery biology (GO:CC plasma membrane; q_global = 0.0371) (GO:CC cell periphery; q_global = 0.042). The fibrinogen genes additionally connect the module to endothelial-cell survival, wound healing, vasoconstriction, heterotypic cell adhesion, and response to wounding (6 globally significant GO/KEGG terms, q_global 0.0149–0.0494; see the table). Together, the genes suggest coordinated control of secretion, adhesion, cytoskeletal remodeling, and vascular or platelet-associated responses, rather than a single narrowly defined intracellular pathway.

**Cell composition.** The module is strongly influenced by circulating proteins and blood-associated cellular composition. FGA, FGB, and FGG are liver-enriched hepatocyte-associated proteins secreted to blood, and TF is also secreted to blood. The fibrinogen chains are prominent contributors to the globally significant wound-healing, vasoconstriction, adhesion, and hemostasis interpretation (6 globally significant GO/KEGG terms, q_global 0.0149–0.0494; see the table). HPA also points to platelets, neutrophils, monocytes, and smooth-muscle cells among the recurring enriched cell types. Most genes are not tissue-restricted, while many are detected in testis; this makes a shared blood, vascular, platelet, immune, or stromal signal plausible. The module should therefore not be treated as evidence that the entire program is produced by testicular cells. The secreted-protein component and the absence of matching circulatory-system HPA tissue protein data particularly warrant caution about plasma carryover or shared blood components.

**GO/KEGG enrichment**: 16 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulation of transport | 0.0015 | APPL2, CA2, CAMK1, DNM1L, FGA, FGB, FGG, GRIPAP1, ITGB1, MICAL1, MYLK, NSF, PRKCA, PRKCD, STXBP2, TF |
| GO:BP positive regulation of transport | 0.00307 | APPL2, CA2, CAMK1, DNM1L, FGA, FGB, FGG, ITGB1, MYLK, PRKCA, PRKCD, TF |
| GO:BP regulation of vesicle-mediated transport | 0.00576 | APPL2, FGA, FGB, FGG, GRIPAP1, MICAL1, MYLK, NSF, STXBP2, TF |
| GO:BP regulation of localization | 0.0114 | APPL2, CA2, CAMK1, DNM1L, FGA, FGB, FGG, GRIPAP1, ITGB1, MICAL1, MYLK, NSF, PRKCA, PRKCD, STXBP2, TF |
| GO:BP regulation of exocytosis | 0.0136 | FGA, FGB, FGG, MICAL1, NSF, STXBP2 |
| GO:BP vesicle-mediated transport | 0.0141 | APPL2, CTTN, DCTN1, DNM1L, EPS15L1, FGA, FGB, FGG, GRIPAP1, ITGB1, MICAL1, MYLK, NSF, PRKCD, STXBP2, TF |
| GO:BP negative regulation of endothelial cell apoptotic process | 0.0149 | FGA, FGB, FGG |
| GO:BP regulation of wound healing | 0.0233 | FGA, FGB, FGG, ITGB1, MYLK, PRKCD |
| GO:BP positive regulation of protein transport | 0.0314 | CAMK1, DNM1L, FGA, FGB, FGG, PRKCA, PRKCD |
| GO:BP regulation of secretion by cell | 0.0354 | DNM1L, FGA, FGB, FGG, MICAL1, NSF, PRKCA, STXBP2 |
| GO:CC plasma membrane | 0.0371 | APPL2, CA2, CALD1, CORO1B, CTTN, EPS15L1, FGA, FGB, FGG, GRIPAP1, ITGB1, LPP, LRBA, MICAL1, MYLK, NCKAP1, NSF, PRKCA, PRKCD, STXBP2, TF |
| GO:BP regulation of vasoconstriction | 0.0391 | FGA, FGB, FGG, ITGB1 |
| GO:CC cell periphery | 0.042 | APPL2, CA2, CALD1, CORO1B, CTTN, DCTN1, EPS15L1, FGA, FGB, FGG, GRIPAP1, ITGB1, LPP, LRBA, MICAL1, MYLK, NCKAP1, NSF, PRKCA, PRKCD, STXBP2, TF |
| GO:BP positive regulation of heterotypic cell-cell adhesion | 0.0436 | FGA, FGB, FGG |
| GO:BP positive regulation of vasoconstriction | 0.0436 | FGA, FGB, FGG |

### STRING and hu.MAP

STRING supports several established relationships: the fibrinogen chains form a tightly connected protein group; PRKCA and PRKCD are linked; CALD1 and MYLK connect contractile actin machinery; CORO1B and CTTN connect actin-remodeling proteins; DNM1L and NSF connect membrane or organelle trafficking; DCTN1 and KLC1 connect microtubule cargo transport; and ITGB1 is linked with PRKCA. These relationships are consistent with the co-abundance structure, but they cover only part of the module, so the network is not simply a recovered STRING complex. hu.MAP independently supports an actin and adhesion-associated complex containing CALD1, CTTN, MYLK, and CORO1B (hu.MAP huMAP3_10673.1) (hu.MAP huMAP3_06395.1) (hu.MAP huMAP3_03762.1) (hu.MAP huMAP3_11074.1). It also repeatedly places FGA, FGB, FGG, and TF within broad circulating-protein complexes (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_06675.1), and places NSF with STXBP2 in a vesicle-fusion complex (hu.MAP huMAP3_13160.1). Thus, some module structure reflects well-established protein assemblies, while the full cross-process combination is a co-abundance association rather than one validated physical complex.

**STRING interactions (score >= 0.7)**: 10 of 630 gene pairs: CALD1–MYLK (0.832); CORO1B–CTTN (0.763); CTTN–MYLK (0.708); DCTN1–KLC1 (0.82); DNM1L–NSF (0.763); FGA–FGB (0.999); FGA–FGG (0.999); FGB–FGG (0.999); ITGB1–PRKCA (0.923); PRKCA–PRKCD (0.967)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Plasma membrane (FDR = 0.00023, 19 genes); COMPARTMENTS Cell periphery (FDR = 0.00032, 20 genes); COMPARTMENTS Membrane (FDR = 0.0022, 26 genes); TISSUES Blood platelet (FDR = 0.008, 12 genes); RCTM Hemostasis (FDR = 0.0272, 11 genes); Component Plasma membrane (FDR = 0.0275, 21 genes); SMART Fibrinogen alpha/beta chain family (FDR = 0.0312, 3 genes); Component Cell periphery (FDR = 0.0393, 22 genes); SMART Fibrinogen-related domains (FReDs) (FDR = 0.0425, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10673.1 (CALD1, CTTN, MYLK, CORO1B; 4/14); huMAP3_09434.1 (FGA, FGB, FGG, TF; 4/33); huMAP3_08395.1 (FGA, FGB, FGG, TF; 4/43); huMAP3_09531.1 (FGA, FGB, FGG, TF; 4/47); huMAP3_10101.1 (FGA, FGB, FGG, TF; 4/49); huMAP3_15040.1 (FGA, FGB, FGG, TF; 4/64); huMAP3_10678.1 (FGA, FGB, FGG, TF; 4/71); huMAP3_06395.1 (CALD1, CTTN, CORO1B; 3/8); huMAP3_02242.1 (FGA, FGG, TF; 3/9); huMAP3_07432.1 (FGA, FGB, TF; 3/18); huMAP3_08224.1 (FGA, FGG, TF; 3/21); huMAP3_06675.1 (FGA, FGB; 2/2); huMAP3_03762.1 (CALD1, CORO1B; 2/6); huMAP3_11074.1 (CALD1, MYLK; 2/6); huMAP3_13160.1 (NSF, STXBP2; 2/49)

### Novelty

This module should not be called a wholly new molecular pathway. Its fibrinogen, transferrin, platelet or hemostatic, actin-adhesion, kinase, and vesicle-trafficking components are established biology, and several pairwise relationships and complexes are already represented in STRING and hu.MAP. The potentially novel aspect is the conserved co-abundance combination across circulatory_system and testis, especially the joint appearance of circulating fibrinogen proteins with contractile, adhesion, cytoskeletal, and secretion machinery. However, the fact sheet does not provide an external replication cohort, perturbation experiment, cell-resolved validation, or a comparison with previously published cross-tissue modules. Therefore the finding is best described as a potentially informative cross-tissue module and a hypothesis-generating organization of known biology, not as a demonstrated novel mechanism.

**Hypothesis.** Hypothesis: the shared module reflects a coordinated blood-interface program in which circulating fibrinogen and transferrin provide extracellular or plasma-associated signals, integrin and actomyosin proteins organize adhesion and contractility, protein kinase C and calcium-dependent signaling tune those responses, and NSF, STXBP2, DNM1L, and associated trafficking proteins regulate secretion or vesicle recycling. In circulatory samples this could arise from plasma proteins, platelets, leukocytes, vascular smooth muscle, or endothelial-associated material. In testis it could reflect vascular and stromal cells, resident or contaminating blood cells, and shared vesicle or cytoskeletal machinery; the HPA observations do not establish that the liver-derived proteins are synthesized locally in testis. This hypothesis predicts that cell-resolved measurements and plasma-depletion or perfusion-aware sampling would reduce the apparent cross-tissue coupling of the secreted proteins, while vascular, platelet, or stromal compartments would retain much of the structural module.

### Important genes

#### FGA

- **Related proteins** (co-abundance neighbors): FGB (0.94), CA2 (0.87), CALD1 (0.81), PDIA5 (0.81); STRING partners: FGB (0.999), FGG (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_02242.1, huMAP3_07432.1, huMAP3_08224.1, huMAP3_06675.1
- **Function (MyGene.info)**: fibrinogen alpha chain. This gene encodes the alpha subunit of the coagulation factor fibrinogen, which is a component of the blood clot. Following vascular injury, the encoded preproprotein is proteolytically processed by thrombin during the conversion of fibrinogen to fibrin. Mutations in this gene lead to several disorders, including dysfibrinogenemia, hypofibrinogenemia, afibrinogenemia and renal amyloidosis. Alterna…
- **Diseases (Open Targets)**: familial dysfibrinogenemia (0.789); familial visceral amyloidosis (0.765); congenital afibrinogenemia (0.757); familial hypodysfibrinogenemia (0.659); congenital fibrinogen deficiency (0.619)
- **Europe PMC papers**: 7516
- **Why important**: FGA is a core member of the fibrinogen triad and is connected in STRING to FGB and FGG. It participates in every globally significant fibrinogen-linked process listed in the module, including transport, exocytosis, wound healing, vasoconstriction, adhesion, and response to wounding (16 globally significant GO/KEGG terms, q_global 0.0015–0.0494; see the table). HPA identifies it as liver-enriched, hepatocyte-associated, and secreted to blood. It has a high literature volume and established associations with dysfibrinogenemia, hypofibrinogenemia, afibrinogenemia, and renal amyloidosis.
- **Conclusion**: Established evidence: FGA is a circulating fibrinogen component with major relevance to coagulation, cell-matrix adhesion, platelet activation, and fibrinolysis. Its module membership most likely marks the blood or plasma-facing part of the signal. Hypothesis: FGA may help bridge the secreted-protein signal to integrin and cytoskeletal responses in the shared tissues, but the co-abundance data do not establish local production or direct action in testis.

#### FGB

- **Related proteins** (co-abundance neighbors): FGA (0.94), PDIA5 (0.84), FGG (0.84), CALD1 (0.83); STRING partners: FGA (0.999), FGG (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_06675.1
- **Function (MyGene.info)**: fibrinogen beta chain. The protein encoded by this gene is the beta component of fibrinogen, a blood-borne glycoprotein comprised of three pairs of nonidentical polypeptide chains. Following vascular injury, fibrinogen is cleaved by thrombin to form fibrin which is the most abundant component of blood clots. In addition, various cleavage products of fibrinogen and fibrin regulate cell adhesion and spreading, display vas…
- **Diseases (Open Targets)**: congenital afibrinogenemia (0.786); familial dysfibrinogenemia (0.705); congenital fibrinogen deficiency (0.622); familial hypodysfibrinogenemia (0.597); cancer (0.592)
- **Europe PMC papers**: 4215
- **Why important**: FGB is strongly connected to FGA and FGG in STRING and is the central fibrinogen-family signal in the STRING enrichment results (9 supplementary STRING terms; within-query FDR 0.00023–0.0425). It occurs in all globally significant module terms (16 globally significant GO/KEGG terms, q_global 0.0015–0.0494; see the table), linking the module to secretion, hemostasis-related biology, wound healing, vasoconstriction, cell adhesion, and endothelial-cell survival. HPA identifies liver and hepatocytes as enriched sources and blood as the secreted destination. Its extensive literature and associations with congenital fibrinogen deficiency and dysfibrinogenemia make it a particularly interpretable anchor.
- **Conclusion**: Established evidence: FGB is a circulating fibrinogen chain and a major explanation for the module's hemostatic and vascular annotations. Hypothesis: its co-abundance with actin and trafficking genes may reflect fibrinogen-dependent interactions with platelet, vascular, or stromal cells, but this cannot distinguish biology from sample composition.

#### FGG

- **Related proteins** (co-abundance neighbors): FGB (0.84); STRING partners: FGA (0.999), FGB (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_02242.1, huMAP3_08224.1
- **Function (MyGene.info)**: fibrinogen gamma chain. The protein encoded by this gene is the gamma component of fibrinogen, a blood-borne glycoprotein comprised of three pairs of nonidentical polypeptide chains. Following vascular injury, fibrinogen is cleaved by thrombin to form fibrin which is the most abundant component of blood clots. In addition, various cleavage products of fibrinogen and fibrin regulate cell adhesion and spreading, display va…
- **Diseases (Open Targets)**: familial dysfibrinogenemia (0.787); congenital afibrinogenemia (0.753); congenital fibrinogen deficiency (0.617); familial hypodysfibrinogenemia (0.597); cancer (0.596)
- **Europe PMC papers**: 4006
- **Why important**: FGG completes the fibrinogen triad with FGA and FGB and has the same broad global GO support across transport, secretion, wound healing, vasoconstriction, adhesion, and wounding responses (16 globally significant GO/KEGG terms, q_global 0.0015–0.0494; see the table). It is liver-enriched, hepatocyte-associated, and secreted to blood according to HPA. STRING and hu.MAP repeatedly support its association with the other fibrinogen chains and with broad circulating-protein assemblies (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_08224.1). Its disease associations include familial dysfibrinogenemia and congenital fibrinogen deficiency, with substantial literature support.
- **Conclusion**: Established evidence: FGG is a biologically indispensable part of the circulating fibrinogen signal and reinforces the interpretation of vascular, platelet, and wound-response biology. Hypothesis: FGG-containing fibrinogen may contribute to extracellular signaling toward integrin and cytoskeletal machinery, although the module alone does not demonstrate that mechanism.

#### MYLK

- **Related proteins** (co-abundance neighbors): APPL2 (0.87), CALD1 (0.82), ITGB1 (0.81), NHLRC2 (0.81); STRING partners: CALD1 (0.832), CTTN (0.708)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10673.1, huMAP3_11074.1
- **Function (MyGene.info)**: myosin light chain kinase. This gene, a muscle member of the immunoglobulin gene superfamily, encodes myosin light chain kinase which is a calcium/calmodulin dependent enzyme. This kinase phosphorylates myosin regulatory light chains to facilitate myosin interaction with actin filaments to produce contractile activity. This gene encodes both smooth muscle and nonmuscle isoforms. In addition, using a separate promoter in an …
- **Diseases (Open Targets)**: aortic aneurysm, familial thoracic 7 (0.767); familial thoracic aortic aneurysm and aortic dissection (0.710); megacystis-microcolon-intestinal hypoperistalsis syndrome 1 (0.617); megacystis-microcolon-intestinal hypoperistalsis syndrome (0.597); Rare genetic vascular disease (0.483)
- **Europe PMC papers**: 10503
- **Why important**: MYLK is a high-connectivity bridge between APPL2, CALD1, ITGB1, and NHLRC2 in the co-abundance network. It is represented in the globally significant transport, vesicle, localization, wound-healing, plasma-membrane, and wounding terms (9 globally significant GO/KEGG terms, q_global 0.0015–0.0494; see the table). STRING links it to CALD1 and CTTN, while hu.MAP supports complexes containing MYLK with CALD1 and an actin-associated group containing CALD1, CTTN, and CORO1B (hu.MAP huMAP3_10673.1) (hu.MAP huMAP3_06395.1) (hu.MAP huMAP3_11074.1). Its established function is calcium-calmodulin-dependent phosphorylation of myosin light chains, and its disease associations include familial thoracic aortic aneurysm and dissection. It also has substantial literature support.
- **Conclusion**: Established evidence: MYLK provides a mechanistic link between actomyosin contractility, adhesion, migration, and vascular remodeling. Hypothesis: MYLK may translate fibrinogen or integrin-associated signals into contractile responses in vascular smooth muscle, platelets, or testicular stromal cells, but cell identity and directionality remain unproven.

#### ITGB1

- **Related proteins** (co-abundance neighbors): GPD2 (0.90), CALD1 (0.84), AMPD2 (0.83), MYLK (0.81); STRING partners: PRKCA (0.923)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 connects GPD2, CALD1, AMPD2, and MYLK in the module and has a high-confidence STRING relationship with PRKCA. It appears in global terms for transport, localization, vesicle trafficking, wound healing, the plasma membrane, vasoconstriction, and response to wounding (9 globally significant GO/KEGG terms, q_global 0.0015–0.0494; see the table). HPA places it at the plasma membrane and focal adhesions and identifies platelet enrichment. Its established integrin function spans adhesion, hemostasis, tissue repair, immune response, phagocytosis, and angiogenesis, with extensive literature and disease associations including inflammatory disease.
- **Conclusion**: Established evidence: ITGB1 is a plausible membrane-level organizer connecting extracellular fibrinogen-related cues to adhesion and cytoskeletal signaling. Hypothesis: it could be the principal receptor-side conduit linking the circulating component to MYLK, PRKCA, and actin remodeling, but the specific integrin heterodimer and tissue compartment are not identified by the fact sheet.

#### STXBP2

- **Related proteins** (co-abundance neighbors): CAMK1 (0.89), PRKCD (0.82), PYGB (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13160.1
- **Function (MyGene.info)**: syntaxin binding protein 2. This gene encodes a member of the STXBP/unc-18/SEC1 family. The encoded protein is involved in intracellular trafficking, control of SNARE (soluble NSF attachment protein receptor) complex assembly, and the release of cytotoxic granules by natural killer cells. Mutations in this gene are associated with familial hemophagocytic lymphohistiocytosis. Alternatively spliced transcript variants encoding…
- **Diseases (Open Targets)**: Familial hemophagocytic lymphohistiocytosis (0.823); autoinflammatory syndrome (0.466); hereditary hemophagocytic lymphohistiocytosis (0.372); hereditary disease (0.342); Thrombocytopenia (0.153)
- **Europe PMC papers**: 1259
- **Why important**: STXBP2 is connected in the module to CAMK1, PRKCD, and PYGB and is part of the hu.MAP vesicle-fusion complex with NSF (hu.MAP huMAP3_13160.1). It appears in the globally significant transport, exocytosis, secretion, localization, and plasma-membrane terms (8 globally significant GO/KEGG terms, q_global 0.0015–0.042; see the table). HPA associates it with megakaryocytes, neutrophils, monocytes, and late spermatids. Its established role in SNARE-complex assembly and cytotoxic-granule release, together with the association of its mutations with familial hemophagocytic lymphohistiocytosis, gives it strong mechanistic and disease relevance.
- **Conclusion**: Established evidence: STXBP2 supports a regulated secretion and vesicle-fusion interpretation, especially in blood and immune-cell contexts. Hypothesis: STXBP2 may connect platelet or leukocyte degranulation with the broader adhesion and vascular-response program, and may also represent a shared vesicle mechanism in testis; the module does not establish which secretory cargo is involved.

## Module 1

**Tissue pair**: circulatory_system and testis  
**Genes (32)**: SERPINA1, CFH, DOCK7, EML3, EPDR1, FERMT2, FKBP5, GARS1, GFPT1, GYS1, HIBCH, IMPACT, IST1, ITSN1, ALDH6A1, NBAS, NSDHL, PPP4R3A, PPM1B, PITRM1, RECQL, SEC23IP, SH3GLB2, SNX6, STAT6, SYNE2, TES, UBA6, VPS11, VPS18, WASHC4, WASHC5

### Function

No GO or KEGG term passed global correction, and STRING reported no supplementary functional enrichment; therefore the module should not be assigned a statistically established pathway function. Its structure instead suggests a heterogeneous combination of intracellular membrane trafficking, endosomal and lysosomal organization, cytoskeletal or adhesion biology, mitochondrial metabolism, and circulating innate-defense proteins. The most coherent intracellular signal is vesicle trafficking: VPS11 and VPS18 are components of CORVET and HOPS complexes, while WASHC4 and WASHC5 participate in the WASH endosomal actin-remodelling system. Additional links involve mitochondrial branched-chain amino-acid metabolism through ALDH6A1 and HIBCH, and extracellular complement or protease regulation through CFH and SERPINA1. Thus, the safest interpretation is a mixed co-abundance module rather than a single proven biochemical pathway.

**Cell composition.** The module is not predominantly a uniform tissue-specific program. Most genes have low tissue specificity in HPA, and many are cell-type enhanced across disparate cell populations. Four genes are secreted or otherwise associated with extracellular protein compartments, with CFH and SERPINA1 especially indicating liver-derived or blood-borne protein contribution. CFH is secreted to blood and liver-enriched, whereas SERPINA1 is liver-enriched, secreted to blood, and associated with monocyte and neutrophil populations; SERPINA1 is not detected in testis by the supplied HPA evidence. The module also contains genes enriched in neutrophils, monocytes, eosinophils, podocytes, hepatocytes, muscle, and reproductive cell types. Most module proteins are detected in testis, but the lack of matching circulatory-system HPA tissue data prevents a direct tissue-protein comparison. The shared signal may therefore reflect plasma proteins, blood or immune-cell admixture, and broadly expressed cellular machinery rather than a specialized program shared by circulating tissue and testis.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports only a small set of high-confidence pairwise relationships in this module: ALDH6A1 with HIBCH, VPS11 with VPS18, and WASHC4 with WASHC5. The VPS11–VPS18 relationship is particularly interpretable because both proteins are established core components of vesicle-trafficking complexes. The WASHC4–WASHC5 relationship likewise agrees with their shared WASH-complex annotations. hu.MAP independently supports these same intracellular relationships: VPS11 and VPS18 co-occur in several CORVET or HOPS-related complexes, and WASHC4 and WASHC5 co-occur in several WASH and actin-remodelling complexes. hu.MAP also places CFH and SERPINA1 together in circulating-protein-rich complexes, while UBA6, GARS1, and TES occur together in a lower-resolution complex. These findings show that portions of the module recapitulate known molecular assemblies, but the module as a whole is not one established complex. Most co-abundance edges lack corresponding high-confidence STRING or hu.MAP support, so co-abundance should not be interpreted as direct physical interaction.

**STRING interactions (score >= 0.7)**: 3 of 496 gene pairs: ALDH6A1–HIBCH (0.811); VPS11–VPS18 (0.999); WASHC4–WASHC5 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (UBA6, GARS1, TES; 3/57); huMAP3_05454.1 (WASHC5, WASHC4; 2/2); huMAP3_08749.1 (VPS11, VPS18; 2/9); huMAP3_13822.1 (VPS11, VPS18; 2/9); huMAP3_12433.1 (VPS11, VPS18; 2/11); huMAP3_12945.1 (VPS11, VPS18; 2/12); huMAP3_06652.1 (WASHC5, WASHC4; 2/14); huMAP3_08077.1 (WASHC5, WASHC4; 2/16); huMAP3_10870.1 (WASHC5, WASHC4; 2/20); huMAP3_12900.1 (WASHC5, WASHC4; 2/50); huMAP3_15040.1 (SERPINA1, CFH; 2/64); huMAP3_10678.1 (SERPINA1, CFH; 2/71)

### Novelty

The exact cross-tissue co-abundance module may be a new systems-level observation, because the supplied evidence does not identify a previously described module with this precise membership and tissue pairing. However, it is not appropriate to call the biology wholly novel: the VPS, WASH, complement, serpin, and mitochondrial enzyme relationships are already established, and several genes have substantial disease and literature support. The absence of a complete module match in STRING or hu.MAP would not prove novelty, because those resources emphasize physical interactions and curated complexes rather than tissue-pair co-abundance. A defensible novelty claim is therefore limited to the observed shared co-abundance pattern, which requires replication in independent cohorts, control for plasma and cell-type composition, and testing of the module's preservation across datasets.

**Hypothesis.** Hypothesis: the shared signal reflects coordinated abundance of endosomal and lysosomal trafficking machinery in testicular cells and blood-associated or vascular-associated material, superimposed on circulating liver-derived proteins. VPS11, VPS18, WASHC4, and WASHC5 could mark vesicle maturation, endosomal sorting, and actin-dependent membrane remodeling, while TES and SEC23IP may connect this machinery to testicular structural or secretory biology. CFH and SERPINA1 may enter the shared module mainly through plasma exposure, liver-derived protein abundance, or immune-cell composition rather than through direct interaction with the intracellular trafficking proteins. The mitochondrial metabolic genes may represent a parallel metabolic state associated with the same cellular or sample-composition effects. This model predicts that the apparent module will weaken after adjustment for plasma proteins and immune-cell abundance, whereas the trafficking submodule should remain more reproducible in purified testicular or relevant vascular cell populations.

### Important genes

#### CFH

- **Related proteins** (co-abundance neighbors): PITRM1 (0.92), SYNE2 (0.90), EML3 (0.84), UBA6 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: complement factor H. This gene is a member of the Regulator of Complement Activation (RCA) gene cluster and encodes a protein with twenty short consensus repeat (SCR) domains. This protein is secreted into the bloodstream and has an essential role in the regulation of complement activation, restricting this innate defense mechanism to microbial infections. Mutations in this gene have been associated with hemolytic-ure…
- **Diseases (Open Targets)**: complement factor H deficiency (0.769); age-related macular degeneration (0.750); atypical hemolytic-uremic syndrome (0.729); age related macular degeneration 4 (0.711); Doyne honeycomb retinal dystrophy (0.688)
- **Europe PMC papers**: 9287
- **Why important**: CFH has relatively central network placement and connects to EML3, UBA6, PITRM1, and SYNE2. It is a liver-enriched, blood-secreted complement regulator, is associated with MAIT T-cell expression, and is present in hu.MAP circulating-protein complexes (hu.MAP huMAP3_15040.1) and (hu.MAP huMAP3_10678.1). It has extensive literature and strong disease associations involving complement deficiency, atypical hemolytic uremic syndrome, and age-related macular degeneration. Its position makes it useful for interpreting the module, but its plasma origin also makes it a potential composition marker.
- **Conclusion**: Established evidence supports CFH as a complement-regulatory, liver-derived circulating protein that is linked to the module through co-abundance and hu.MAP context, not through a STRING interaction. It is important for explaining the extracellular and blood-associated component. It is not established that CFH mechanistically drives the intracellular trafficking component.

#### VPS11

- **Related proteins** (co-abundance neighbors): IMPACT (0.84), VPS18 (0.82), WASHC5 (0.82), PPP4R3A (0.81); STRING partners: VPS18 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_08749.1, huMAP3_13822.1, huMAP3_12433.1, huMAP3_12945.1
- **Function (MyGene.info)**: VPS11 core subunit of CORVET and HOPS complexes. Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene encodes the human homolog of yeast class C Vps11 protein. The mammalian class C Vps proteins are predominantly associated with late…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 12 (0.723); neurodegenerative disease (0.527); POLR-related leukodystrophy (0.527); dystonia 32 (0.410); VPS11-related neurological disorder (0.370)
- **Europe PMC papers**: 849
- **Why important**: VPS11 is a network connector and forms the strongest STRING-supported pair in the module with VPS18. It is a core subunit of CORVET and HOPS, is represented with VPS18 across multiple hu.MAP complexes (hu.MAP huMAP3_08749.1), (hu.MAP huMAP3_13822.1), (hu.MAP huMAP3_12433.1), and (hu.MAP huMAP3_12945.1), and has annotations for endosome organization, lysosome organization, and vesicle-mediated transport. It is detected in testis and has disease associations involving leukodystrophy and VPS11-related neurological disorders.
- **Conclusion**: Established evidence supports VPS11 as a bona fide vesicle-trafficking component and one of the strongest mechanistic anchors of the module. The co-abundance pattern is consistent with coordinated endosomal or lysosomal machinery. Whether this machinery explains the shared circulatory-system and testis signal remains a hypothesis.

#### VPS18

- **Related proteins** (co-abundance neighbors): VPS11 (0.82), ALDH6A1 (0.82), PPM1B (0.80); STRING partners: VPS11 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_08749.1, huMAP3_13822.1, huMAP3_12433.1, huMAP3_12945.1
- **Function (MyGene.info)**: VPS18 core subunit of CORVET and HOPS complexes. Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene encodes the human homolog of yeast class C Vps18 protein. The mammalian class C Vps proteins are predominantly associated with late…
- **Diseases (Open Targets)**: neurodegenerative disease (0.541); COVID-19 (0.372); male infertility (0.190); neoplasm (0.091); ulcerative colitis (0.062)
- **Europe PMC papers**: 802
- **Why important**: VPS18 pairs with VPS11 in STRING and hu.MAP, and it is annotated as a core CORVET and HOPS subunit involved in endosome, lysosome, and vesicle organization. It connects in the module to VPS11, ALDH6A1, and PPM1B, linking trafficking with metabolic and regulatory genes. HPA detects it in testis and in neutrophil-related cell contexts, and its disease associations include neurodegenerative disease and male infertility.
- **Conclusion**: Established evidence supports VPS18 as a structural partner of VPS11 in conserved intracellular trafficking complexes. Its presence strengthens the interpretation of a trafficking submodule and provides a plausible bridge to testicular cell biology. The proposed connection to male reproductive phenotypes is suggestive rather than demonstrated for this module.

#### WASHC4

- **Related proteins** (co-abundance neighbors): NBAS (0.85); STRING partners: WASHC5 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_05454.1, huMAP3_06652.1, huMAP3_08077.1, huMAP3_10870.1, huMAP3_12900.1
- **Function (MyGene.info)**: WASH complex subunit 4. This gene encodes a component of the WASH complex, which functions in the intracellular transport of endosomes. Mutations in this gene have been detected in individuals with autosomal recessive cognitive disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014].
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.611); Intellectual disability (0.345); mathematical ability (0.322); Abnormality of the skeletal system (0.148); corneal ulcer (0.140)
- **Europe PMC papers**: 116
- **Why important**: WASHC4 has a direct high-confidence STRING relationship with WASHC5 and occurs with WASHC5 in several hu.MAP assemblies (hu.MAP huMAP3_05454.1), (hu.MAP huMAP3_06652.1), (hu.MAP huMAP3_08077.1), (hu.MAP huMAP3_10870.1), and (hu.MAP huMAP3_12900.1). Its established function is in WASH-complex control of endosomal transport and Arp2/3-dependent actin nucleation. It is detected in testis and has disease associations involving autosomal-recessive intellectual disability.
- **Conclusion**: Established evidence supports WASHC4 as an endosomal actin-remodelling component whose module membership is biologically concordant with the VPS trafficking signal. It is a stronger functional interpretation gene than a tissue-specific marker. A direct role in the shared tissue-pair phenotype is not established.

#### TES

- **Related proteins** (co-abundance neighbors): ALDH6A1 (0.85), SEC23IP (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: testin LIM domain protein. Cancer-associated chromosomal changes often involve regions containing fragile sites. This gene maps to a common fragile site on chromosome 7q31.2 designated FRA7G. This gene is similar to mouse Testin, a testosterone-responsive gene encoding a Sertoli cell secretory protein containing three LIM domains. LIM domains are double zinc-finger motifs that mediate protein-protein interactions between tr…
- **Diseases (Open Targets)**: open-angle glaucoma (0.490); glaucoma (0.440); placenta praevia (0.258); spinal cord injury (0.246); Joint stiffness (0.173)
- **Europe PMC papers**: 32609
- **Why important**: TES is connected to ALDH6A1 and SEC23IP and is represented with UBA6 and GARS1 in hu.MAP complex (hu.MAP huMAP3_14442.1). HPA identifies testis detection, seminal-vesicle tissue enhancement, and enrichment in early spermatids. Its LIM domains support protein-interaction and cytoskeletal functions, and its literature volume is substantial. These features make TES a useful reproductive and structural counterpart to the broadly expressed trafficking genes.
- **Conclusion**: Established evidence supports TES as a testis- and reproductive-system-associated cytoskeletal or interaction protein that may contextualize the module in testicular tissue. Its direct connection to the VPS or WASH machinery is not demonstrated by the supplied STRING or hu.MAP evidence. Its role as a tissue-pair bridge remains a hypothesis.

## Module 2

**Tissue pair**: circulatory_system and testis  
**Genes (21)**: SERPINF2, ACO1, ADK, APOB, SERPINA6, C6, C7, C9, FBLN1, FLNA, HP, ITIH4, LUM, MESD, PGM1, ATIC, TNXB, TFRC, TLN1, VIM, AZGP1

### Function

The strongest interpretation is an extracellular, circulating protein module with linked innate-defense, acute-phase, extracellular-matrix, and cell-adhesion features. The primary GO evidence supports extracellular exosomes, extracellular organelles, extracellular vesicles, extracellular space, and the cell periphery (6 globally significant GO/KEGG terms, q_global 0.000281–0.00216; see the table), (GO:CC cell periphery; q_global = 0.0119) (GO:CC vesicle; q_global = 0.0136). The complement membrane-attack-complex terms (GO:CC membrane attack complex; q_global = 0.0117), together with acute-phase response (GO:BP acute-phase response; q_global = 0.0173), indicate an immune and inflammatory component. Regulation of transforming-growth-factor-beta production (GO:BP regulation of transforming growth factor beta production; q_global = 0.041) adds a matrix-remodelling or stromal-signalling aspect. The intracellular enzymes and cytoskeletal proteins do not overturn this interpretation; they may represent vesicle cargo, associated cells, or correlated cellular states rather than a single biochemical pathway.

**Cell composition.** This module is dominated by secreted-to-blood or extracellular-matrix proteins, including ITIH4, C9, C6, C7, SERPINF2, HP, SERPINA6, APOB, AZGP1, FBLN1, LUM, and TNXB. HPA supports strong liver and hepatocyte representation, with additional vascular, fibroblast, hepatic-stellate, adrenal, and intestinal signals. The module therefore resembles a plasma or liver-derived extracellular-protein signature more than a testis-specific transcriptional program. The blood-cell evidence is mostly low or absent, although selected genes show monocyte, eosinophil, basophil, or plasmacytoid-dendritic-cell associations. TLN1, FLNA, VIM, TFRC, ACO1, PGM1, ATIC, ADK, MESD, and other intracellular or membrane-associated genes could reflect shared vascular, stromal, platelet-related, or testicular cell states. The cross-tissue observation may consequently reflect circulating proteins, extracellular vesicles, vascular or stromal cells, or sample composition, rather than secretion by testicular cells. HPA protein detection in testis is present for a subset of genes, but several major plasma proteins are not detected there.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC extracellular exosome | 0.000281 | ACO1, APOB, ATIC, AZGP1, C6, C7, C9, FBLN1, FLNA, HP, ITIH4, LUM, PGM1, SERPINA6, SERPINF2, TFRC, TLN1, TNXB, VIM |
| GO:CC extracellular organelle | 0.000301 | ACO1, APOB, ATIC, AZGP1, C6, C7, C9, FBLN1, FLNA, HP, ITIH4, LUM, PGM1, SERPINA6, SERPINF2, TFRC, TLN1, TNXB, VIM |
| GO:CC extracellular membrane-bounded organelle | 0.000301 | ACO1, APOB, ATIC, AZGP1, C6, C7, C9, FBLN1, FLNA, HP, ITIH4, LUM, PGM1, SERPINA6, SERPINF2, TFRC, TLN1, TNXB, VIM |
| GO:CC extracellular vesicle | 0.000301 | ACO1, APOB, ATIC, AZGP1, C6, C7, C9, FBLN1, FLNA, HP, ITIH4, LUM, PGM1, SERPINA6, SERPINF2, TFRC, TLN1, TNXB, VIM |
| GO:CC extracellular space | 0.000825 | ACO1, APOB, ATIC, AZGP1, C6, C7, C9, FBLN1, FLNA, HP, ITIH4, LUM, PGM1, SERPINA6, SERPINF2, TFRC, TLN1, TNXB, VIM |
| GO:CC extracellular region | 0.00216 | ACO1, APOB, ATIC, AZGP1, C6, C7, C9, FBLN1, FLNA, HP, ITIH4, LUM, PGM1, SERPINA6, SERPINF2, TFRC, TLN1, TNXB, VIM |
| GO:CC membrane attack complex | 0.0117 | C6, C7, C9 |
| GO:CC cell periphery | 0.0119 | ADK, APOB, ATIC, AZGP1, C6, C7, C9, FBLN1, FLNA, ITIH4, LUM, MESD, TFRC, TLN1, TNXB, VIM |
| GO:CC vesicle | 0.0136 | ACO1, APOB, ATIC, AZGP1, C6, C7, C9, FBLN1, FLNA, HP, ITIH4, LUM, PGM1, SERPINA6, SERPINF2, TFRC, TLN1, TNXB, VIM |
| GO:BP acute-phase response | 0.0173 | HP, ITIH4, SERPINF2, TFRC |
| GO:BP regulation of transforming growth factor beta production | 0.041 | FBLN1, LUM, SERPINF2 |

### STRING and hu.MAP

STRING provides particularly strong known relationships among the terminal complement proteins C6, C7, and C9, directly matching the membrane-attack-complex interpretation. It also supports the FLNA–TLN1 cytoskeletal pair, the ACO1–TFRC and APOB–TFRC connections, and the AZGP1–HP relationship. The supplementary STRING annotations independently reinforce secretion, extracellular location, vesicles, glycoproteins, plasma proteins, and cytolysis, but they are supportive rather than globally corrected GO evidence. hu.MAP shows recurrent co-membership of SERPINA6 with SERPINF2 or ITIH4, SERPINF2 with C6, MESD with TLN1, HP with ITIH4, and SERPINA6 with LUM in larger plasma, complement, coagulation, inflammatory, or intracellular complexes. These hu.MAP results generally involve only a small subset of module members within broad complexes, so they support biological coherence without demonstrating one physical complex containing the whole module.

**STRING interactions (score >= 0.7)**: 7 of 210 gene pairs: ACO1–TFRC (0.888); APOB–TFRC (0.813); AZGP1–HP (0.782); C6–C7 (0.995); C6–C9 (0.996); C7–C9 (0.986); FLNA–TLN1 (0.998)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Secreted (FDR = 1.52e-06, 13 genes); Keyword Glycoprotein (FDR = 2.71e-06, 15 genes); TISSUES Bone marrow cell (FDR = 4.63e-06, 10 genes); COMPARTMENTS Extracellular region (FDR = 5.32e-06, 16 genes); TISSUES Plasma cell (FDR = 2.3e-05, 9 genes); Keyword Signal (FDR = 4.96e-05, 13 genes); Component Extracellular exosome (FDR = 6.45e-05, 19 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 0.00014, 11 genes); Component Cell periphery (FDR = 0.00021, 17 genes); Keyword Disulfide bond (FDR = 0.00029, 12 genes); Keyword EGF-like domain (FDR = 0.00058, 5 genes); COMPARTMENTS Extracellular space (FDR = 0.00089, 12 genes); TISSUES Skeletal system (FDR = 0.0018, 12 genes); PMID (2016) Glycoproteomic Analysis of Malignant Ovarian Cancer Ascites Fluid Identifies Unusual Glycopeptides. (FDR = 0.0019, 8 genes); Keyword Cytolysis (FDR = 0.0032, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05943.1 (SERPINA6, SERPINF2; 2/6); huMAP3_00178.1 (SERPINA6, SERPINF2; 2/9); huMAP3_08796.1 (SERPINA6, ITIH4; 2/15); huMAP3_14445.1 (SERPINF2, C6; 2/18); huMAP3_09832.1 (SERPINA6, ITIH4; 2/18); huMAP3_14656.1 (SERPINF2, C6; 2/21); huMAP3_14982.1 (MESD, TLN1; 2/28); huMAP3_09434.1 (HP, ITIH4; 2/33); huMAP3_14295.1 (SERPINA6, LUM; 2/38); huMAP3_09531.1 (HP, ITIH4; 2/47); huMAP3_10101.1 (HP, ITIH4; 2/49); huMAP3_15040.1 (HP, ITIH4; 2/64); huMAP3_10678.1 (HP, ITIH4; 2/71)

### Novelty

The module should not be described as a newly discovered molecular complex. Several of its relationships and functional themes are already established: complement assembly, plasma transport and acute-phase proteins, extracellular matrix, and cytoskeletal adhesion. The supplied STRING and hu.MAP results therefore indicate substantial prior biological knowledge. A potentially novel aspect is the coordinated co-abundance of this particular combination across circulatory system and testis, especially the juxtaposition of liver-derived plasma proteins, complement components, matrix proteins, and testis-detected cellular proteins. However, the fact sheet does not provide a comparison against previously published tissue-pair modules or an independent co-abundance study. Absence of a complete module match in STRING or hu.MAP would not prove novelty, so the appropriate conclusion is that the cross-tissue module association is a candidate observation requiring replication and comparison with existing datasets.

**Hypothesis.** Hypothesis: circulating liver-derived proteins and extracellular vesicles form the principal shared signal, while vascular or stromal cells in the two sampled tissue groups contribute matrix and adhesion components. Within this environment, complement proteins C6, C7, and C9 could provide innate membrane-defense capacity; SERPINF2, ITIH4, HP, and SERPINA6 could couple protease, coagulation, acute-phase, and hormone-transport states; and LUM, FBLN1, TNXB, TLN1, FLNA, and VIM could report extracellular-matrix and cell-adhesion remodelling. The testis association may therefore reflect shared vascular or extracellular-vesicle biology, with a possible contribution from Leydig, Sertoli, fibroblast, or other stromal cells. This is a mechanistic model, not evidence that the complete module acts as one physical complex or that every protein is produced locally in testis.

### Important genes

#### ITIH4

- **Related proteins** (co-abundance neighbors): SERPINF2 (0.89), AZGP1 (0.89), HP (0.87), LUM (0.87), C9 (0.86), C6 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08796.1, huMAP3_09832.1, huMAP3_09434.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 4. The protein encoded by this gene is secreted into the blood, where it is cleaved by plasma kallikrein into two smaller forms. Expression of this gene has been detected only in liver, and it seems to be upregulated during surgical trauma. This gene is part of a cluster of similar genes on chromosome 3. Two transcript variants encoding different isoforms have been found for this gene. [provided by R…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.466); coronary artery disorder (0.417); type 2 diabetes mellitus (0.397); osteoarthritis (0.387); diabetes mellitus (0.363)
- **Europe PMC papers**: 1710
- **Why important**: ITIH4 is a central network hub and connects acute-phase, extracellular-vesicle, extracellular-space, and matrix-related evidence (6 globally significant GO/KEGG terms, q_global 0.000281–0.00216; see the table), (GO:CC cell periphery; q_global = 0.0119) (GO:CC vesicle; q_global = 0.0136) (GO:BP acute-phase response; q_global = 0.0173). HPA identifies it as a liver-enriched protein secreted to blood, and its annotation supports cytokine response and hyaluronan-related biology. Its extensive literature and disease associations involving vascular, metabolic, and skeletal traits make it a strong anchor for interpreting the module as a circulating inflammatory-matrix signature.
- **Conclusion**: Established evidence supports ITIH4 as a liver-derived extracellular acute-phase and matrix-associated hub. It is plausible, but not established, that ITIH4 helps link circulating inflammation to tissue matrix remodelling in the shared module.

#### C9

- **Related proteins** (co-abundance neighbors): MESD (0.86), ITIH4 (0.86), ACO1 (0.85), HP (0.85), ADK (0.82), VIM (0.81); STRING partners: C6 (0.996), C7 (0.986)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C9. This gene encodes the final component of the complement system. It participates in the formation of the Membrane Attack Complex (MAC). The MAC assembles on bacterial membranes to form a pore, permitting disruption of bacterial membrane organization. Mutations in this gene cause component C9 deficiency. [provided by RefSeq, Feb 2009].
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.747); age-related macular degeneration (0.584); complement component 9 deficiency (0.548); macular degeneration (0.541); complement deficiency (0.463)
- **Europe PMC papers**: 28081
- **Why important**: C9 is a network hub and is one of the three genes in the globally significant membrane-attack-complex term (GO:CC membrane attack complex; q_global = 0.0117). It is liver-enriched, secreted to blood, and has direct high-confidence STRING relationships with C6 and C7. Its function in the terminal complement pathway, disease associations with complement deficiency, and very extensive literature make it the clearest innate-immune effector in the module.
- **Conclusion**: Established evidence supports C9 as a terminal complement and membrane-attack-complex component that explains a specific part of the module. Its co-abundance with the other module proteins does not by itself establish complement activation in either tissue.

#### SERPINF2

- **Related proteins** (co-abundance neighbors): C6 (0.91), HP (0.90), ITIH4 (0.89); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enriched; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05943.1, huMAP3_00178.1, huMAP3_14445.1, huMAP3_14656.1
- **Function (MyGene.info)**: serpin family F member 2. This gene encodes a member of the serpin family of serine protease inhibitors. The protein is a major inhibitor of plasmin, which degrades fibrin and various other proteins. Consequently, the proper function of this gene has a major role in regulating the blood clotting pathway. Mutations in this gene result in alpha-2-plasmin inhibitor deficiency, which is characterized by severe hemorrhagic diat…
- **Diseases (Open Targets)**: alpha-2-plasmin inhibitor deficiency (0.666); chronic kidney disease (0.452); Alzheimer disease (0.413); dementia (0.402); Abnormal bleeding (0.371)
- **Europe PMC papers**: 1441
- **Why important**: SERPINF2 occupies a connected position beside C6, HP, and ITIH4 and contributes to extracellular, acute-phase, and transforming-growth-factor-beta-related evidence (6 globally significant GO/KEGG terms, q_global 0.000281–0.00216; see the table), (GO:CC vesicle; q_global = 0.0136) (GO:BP acute-phase response; q_global = 0.0173) (GO:BP regulation of transforming growth factor beta production; q_global = 0.041). It is secreted to blood, is liver-enriched, and is a major inhibitor of plasmin with established relevance to fibrinolysis and bleeding disorders. Repeated hu.MAP membership with SERPINA6, ITIH4, and C6 supports a plasma protease and coagulation context.
- **Conclusion**: Established evidence supports SERPINF2 as a circulating regulator of plasmin and fibrinolysis. A possible but unproven implication is that it coordinates protease balance with complement and matrix remodelling in this module.

#### LUM

- **Related proteins** (co-abundance neighbors): ITIH4 (0.87), FBLN1 (0.85), TLN1 (0.83), C7 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14295.1
- **Function (MyGene.info)**: lumican. This gene encodes a member of the small leucine-rich proteoglycan (SLRP) family that includes decorin, biglycan, fibromodulin, keratocan, epiphycan, and osteoglycin. In these bifunctional molecules, the protein moiety binds collagen fibrils and the highly charged hydrophilic glycosaminoglycans regulate interfibrillar spacings. Lumican is the major keratan sulfate proteoglycan of the cornea but is …
- **Diseases (Open Targets)**: lumbar disc herniation (0.359); Dupuytren Contracture (0.357); fibroblastic disorder (0.357); Hallux valgus (0.357); preeclampsia (0.154)
- **Europe PMC papers**: 14825
- **Why important**: LUM is a network connector between ITIH4, FBLN1, TLN1, and C7 and contributes to nearly all of the globally significant extracellular terms as well as transforming-growth-factor-beta production (6 globally significant GO/KEGG terms, q_global 0.000281–0.00216; see the table), (4 globally significant GO/KEGG terms, q_global 0.0119–0.041; see the table). It is an extracellular-matrix proteoglycan with collagen-fibril functions, has stromal and decidual-cell associations, and has extensive literature concerning matrix biology and disease. Its position links soluble plasma-associated proteins to structural extracellular matrix.
- **Conclusion**: Established evidence supports LUM as the matrix and growth-factor-regulatory component of the module. Its role as a bridge between circulating proteins and testicular or vascular stromal remodelling is a reasonable hypothesis, not a demonstrated mechanism.

#### TLN1

- **Related proteins** (co-abundance neighbors): SERPINA6 (0.88), TNXB (0.86), LUM (0.83), FLNA (0.82); STRING partners: FLNA (0.998)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_14982.1
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 connects SERPINA6, TNXB, LUM, and FLNA and is supported by extracellular or cell-periphery annotations (4 globally significant GO/KEGG terms, q_global 0.000281–0.000301; see the table), (GO:CC extracellular space; q_global = 0.000825) (GO:CC extracellular region; q_global = 0.00216), (GO:CC cell periphery; q_global = 0.0119) (GO:CC vesicle; q_global = 0.0136). Its established function in integrin activation, cell adhesion, actin organization, and focal adhesions gives the module a cellular-interface component that complements its secreted proteins. HPA links it to blood vessels, megakaryocytes, platelets, and testis, while STRING strongly supports its relationship with FLNA.
- **Conclusion**: Established evidence supports TLN1 as a vascular, platelet-associated, and adhesion-related cytoskeletal protein. It may mark the cellular source or recipient interface for extracellular proteins in the shared module, but the co-abundance data do not prove direct uptake or signalling.

## Module 3

**Tissue pair**: circulatory_system and testis  
**Genes (44)**: AAAS, ABHD17B, AP4B1, ASRGL1, BCAP29, CEP76, CISD1, CRLF3, SORD, DNAJB1, DPCD, FAF1, GGPS1, GLUL, HACL1, HEXA, HMOX1, MFGE8, CHCHD3, MTX1, NADSYN1, NDC1, NME7, NDRG3, NDUFA6, NDUFAF4, NUP155, NUP188, NUP88, ODF2, DLAT, PDHX, PFN3, PSMG1, RAE1, RNF123, SLC27A4, APCS, SCAMP4, LARS2, THTPA, TMEM38B, VPS13A, ZNRD2

### Function

The module does not have any GO or KEGG term that passed global correction. Its strongest interpretable signal is a composite cellular-maintenance program rather than a single established pathway. The network contains a coherent nuclear-pore and nucleocytoplasmic-transport component involving AAAS, NDC1, NUP155, NUP188, NUP88 and RAE1, supported by STRING relationships and by the supplementary STRING terms (15 supplementary STRING terms; within-query FDR 0.0085–0.0158). It also contains smaller mitochondrial, pyruvate-metabolism, ciliary or flagellar, lipid-handling and vesicle-trafficking components. Thus, the most defensible functional interpretation is coordinated abundance of nuclear transport machinery together with mitochondrial and structural programs, especially in testis-associated cells. The STRING viral and glucokinase terms should be interpreted as pathway-context annotations of the nuclear-pore proteins, not as evidence that the module is a viral or glucokinase module.

**Cell composition.** This is not predominantly a plasma or secreted-protein module. The secreted-to-blood genes include APCS and MFGE8, but most members are intracellular and HPA reports low immune-cell specificity for most genes. APCS is liver- and hepatocyte-enriched and secreted to blood, so it could contribute a circulating-protein signal in circulatory-system material. MFGE8 is blood-vessel-enriched and also secreted to blood. In contrast, the module has a strong testis and germ-cell signature: many genes are enhanced in early or late spermatids or primary spermatocytes, and several are testis-enriched or detected in testis. The HPA profile therefore supports a substantial shared-cell or tissue-composition contribution, particularly from spermatogenic, ciliated, centrosomal and mitochondrial biology, rather than a simple blood-cell module. The limited immune-cell enrichment, including HMOX1 and selected myeloid-associated signals, may reflect minor cellular admixture but does not dominate the composition.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING shows a well-supported known nucleoporin subnetwork: AAAS, NDC1, NUP155, NUP188, NUP88 and RAE1 are linked by high-confidence relationships. The same nuclear-pore group accounts for the repeated supplementary STRING annotations (15 supplementary STRING terms; within-query FDR 0.0085–0.0158), covering mRNA export, ribonucleoprotein transport, nuclear import and related host or viral transport contexts. Other known relationships include the PDHX–DLAT pyruvate-dehydrogenase connection, the NDUFA6–NDUFAF4 complex-I connection, and the CHCHD3–MTX1 mitochondrial relationship. hu.MAP independently supports several established complexes: (hu.MAP huMAP3_12581.1) (hu.MAP huMAP3_09111.1) (hu.MAP huMAP3_09497.1) (hu.MAP huMAP3_07645.1) and (hu.MAP huMAP3_08442.1), (hu.MAP huMAP3_07492.1) (hu.MAP huMAP3_08489.1), (hu.MAP huMAP3_09220.1) (hu.MAP huMAP3_06369.1), (hu.MAP huMAP3_09710.1), (hu.MAP huMAP3_09825.1) (hu.MAP huMAP3_10000.1) support nuclear-pore or RNA-export assemblies; (hu.MAP huMAP3_04919.1), (hu.MAP huMAP3_08216.1) (hu.MAP huMAP3_07514.1), (hu.MAP huMAP3_09761.1) (hu.MAP huMAP3_10899.1), (hu.MAP huMAP3_10412.1), (hu.MAP huMAP3_14339.1) (hu.MAP huMAP3_11877.1) (hu.MAP huMAP3_14864.1) (hu.MAP huMAP3_12248.1) support the pyruvate-dehydrogenase complex; and (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1) support complex-I assemblies. These observations indicate that part of the co-abundance structure recapitulates known physical or functional complexes. They do not establish that all module edges represent direct physical interactions, nor that the entire module is one biochemical complex.

**STRING interactions (score >= 0.7)**: 18 of 946 gene pairs: AAAS–NDC1 (0.994); AAAS–NUP155 (0.989); AAAS–NUP188 (0.981); AAAS–NUP88 (0.994); AAAS–RAE1 (0.924); CHCHD3–MTX1 (0.94); DLAT–PDHX (0.998); NDC1–NUP155 (0.992); NDC1–NUP188 (0.986); NDC1–NUP88 (0.979); NDC1–RAE1 (0.833); NDUFA6–NDUFAF4 (0.905); NUP155–NUP188 (0.999); NUP155–NUP88 (0.995); NUP155–RAE1 (0.934); NUP188–NUP88 (0.992); NUP188–RAE1 (0.878); NUP88–RAE1 (0.942)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM SLC transporter disorders (FDR = 0.0085, 7 genes); RCTM ISG15 antiviral mechanism (FDR = 0.0158, 6 genes); RCTM Transport of the SLBP independent Mature mRNA (FDR = 0.0158, 6 genes); RCTM Transport of the SLBP Dependant Mature mRNA (FDR = 0.0158, 6 genes); RCTM Transport of Mature mRNA Derived from an Intronless Transcript (FDR = 0.0158, 6 genes); RCTM Transport of Mature mRNA derived from an Intron-Containing Transcript (FDR = 0.0158, 6 genes); RCTM Rev-mediated nuclear export of HIV RNA (FDR = 0.0158, 6 genes); RCTM Transport of Ribonucleoproteins into the Host Nucleus (FDR = 0.0158, 6 genes); RCTM NS1 Mediated Effects on Host Pathways (FDR = 0.0158, 6 genes); RCTM Viral Messenger RNA Synthesis (FDR = 0.0158, 6 genes); RCTM NEP/NS2 Interacts with the Cellular Export Machinery (FDR = 0.0158, 6 genes); RCTM Regulation of Glucokinase by Glucokinase Regulatory Protein (FDR = 0.0158, 6 genes); RCTM Nuclear import of Rev protein (FDR = 0.0158, 6 genes); RCTM Vpr-mediated nuclear import of PICs (FDR = 0.0158, 6 genes); RCTM snRNP Assembly (FDR = 0.0158, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12581.1 (NUP155, RAE1, NUP88, AAAS; 4/58); huMAP3_09111.1 (NUP155, NDC1; 2/4); huMAP3_09497.1 (NUP155, NDC1; 2/6); huMAP3_07645.1 (NUP155, NDC1; 2/7); huMAP3_04919.1 (PDHX, DLAT; 2/7); huMAP3_08442.1 (RAE1, NUP88; 2/8); huMAP3_08216.1 (PDHX, DLAT; 2/8); huMAP3_07514.1 (PDHX, DLAT; 2/9); huMAP3_07492.1 (NUP188, AAAS; 2/10); huMAP3_08489.1 (NUP188, AAAS; 2/10); huMAP3_09761.1 (PDHX, DLAT; 2/10); huMAP3_10899.1 (PDHX, DLAT; 2/10); huMAP3_09220.1 (RAE1, NUP88; 2/11); huMAP3_06369.1 (RAE1, NUP88; 2/12); huMAP3_10412.1 (PDHX, DLAT; 2/12); huMAP3_09710.1 (NUP188, AAAS; 2/13); huMAP3_14339.1 (PDHX, DLAT; 2/13); huMAP3_11877.1 (PDHX, DLAT; 2/14); huMAP3_14864.1 (PDHX, DLAT; 2/14); huMAP3_12248.1 (PDHX, DLAT; 2/22); huMAP3_09825.1 (NUP188, AAAS; 2/27); huMAP3_10000.1 (RAE1, NUP88; 2/44); huMAP3_14018.1 (NDUFA6, NDUFAF4; 2/48); huMAP3_06397.1 (NDUFA6, NDUFAF4; 2/49); huMAP3_09982.1 (NDUFA6, NDUFAF4; 2/49); huMAP3_09567.1 (NDUFA6, NDUFAF4; 2/52); huMAP3_14878.1 (NDUFA6, NDUFAF4; 2/53)

### Novelty

The module should not be called a wholly new molecular pathway. Much of its strongest internal structure consists of already known nuclear-pore, pyruvate-dehydrogenase and complex-I relationships, as shown by STRING and hu.MAP. Conversely, the particular cross-tissue co-abundance association joining these established components with testis-associated ciliary, sperm-structural, lipid, vesicle and secreted proteins is not directly established by the fact sheet. It may be a novel systems-level observation, but novelty is provisional because shared tissue composition, spermatogenic cell abundance, circulating APCS or MFGE8, and correlated general cellular state could generate the association. Absence of a complete matching module in STRING or hu.MAP would not by itself prove novelty. Independent replication across cohorts, adjustment for cell composition, and testing of the cross-component relationships would be needed before claiming a new biological module.

**Hypothesis.** Hypothesis: in testis-associated cells, a high demand for nuclear transport and RNA handling during spermatogenic differentiation is coordinated with mitochondrial energy production, pyruvate utilization, ciliary or flagellar organization, lipid handling and proteostasis. In circulatory-system samples, the same apparent module may be observed partly through shared intracellular cell types and partly through circulating or vascular proteins such as APCS and MFGE8. The nucleoporin subnetwork may represent the mechanistic core, while the mitochondrial, ciliary and secreted-protein signals may be biologically coupled outputs or correlated tissue-composition signals. This hypothesis predicts that the nucleoporin genes will co-vary within purified germ-cell or relevant vascular-cell populations, whereas APCS and MFGE8 will weaken after removal of plasma or vascular-cell contributions.

### Important genes

#### NUP155

- **Related proteins** (co-abundance neighbors): MFGE8 (0.85), DPCD (0.82); STRING partners: AAAS (0.989), NDC1 (0.992), NUP188 (0.999), NUP88 (0.995), RAE1 (0.934)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_12581.1, huMAP3_09111.1, huMAP3_09497.1, huMAP3_07645.1
- **Function (MyGene.info)**: nucleoporin 155. Nucleoporins are proteins that play an important role in the assembly and functioning of the nuclear pore complex (NPC) which regulates the movement of macromolecules across the nuclear envelope (NE). The protein encoded by this gene plays a role in the fusion of NE vesicles and formation of the double membrane NE. The protein may also be involved in cardiac physiology and may be associated with t…
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); atrial fibrillation (0.470); familial atrial fibrillation (0.390)
- **Europe PMC papers**: 944
- **Why important**: NUP155 is a key member of the module's known nuclear-pore subnetwork. It connects to AAAS, NDC1, NUP188, NUP88 and RAE1 in STRING and appears across the hu.MAP assemblies (hu.MAP huMAP3_12581.1) (hu.MAP huMAP3_09111.1) (hu.MAP huMAP3_09497.1) (hu.MAP huMAP3_07645.1). HPA describes nuclear-membrane localization, testis enrichment and late-spermatid enhancement. Its disease associations include atrial-fibrillation-related conditions and viral-infection contexts, while its literature base is substantial.
- **Conclusion**: Established evidence supports NUP155 as a nuclear-pore and nucleocytoplasmic-transport component that is particularly relevant to the testis-associated part of this module. It is a plausible mechanistic anchor, but the co-abundance data do not show that NUP155 directly regulates spermatogenesis or that it links the secreted and mitochondrial branches.

#### NUP188

- **Related proteins** (co-abundance neighbors): ABHD17B (0.87), AAAS (0.82), DPCD (0.80), NME7 (0.80); STRING partners: AAAS (0.981), NDC1 (0.986), NUP155 (0.999), NUP88 (0.992), RAE1 (0.878)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07492.1, huMAP3_08489.1, huMAP3_09710.1, huMAP3_09825.1
- **Function (MyGene.info)**: nucleoporin 188. The nuclear pore complex (NPC) is found on the nuclear envelope and forms a gateway that regulates the flow of proteins and RNAs between the cytoplasm and nucleoplasm. The NPC is comprised of approximately 30 distinct proteins collectively known as nucleoporins. Nucleoporins are pore-complex-specific glycoproteins which often have cytoplasmically oriented O-linked N-acetylglucosamine residues and …
- **Diseases (Open Targets)**: sandestig-stefanova syndrome (0.799); HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.527); microcephaly (0.453)
- **Europe PMC papers**: 629
- **Why important**: NUP188 is embedded in the most coherent network region, with strong STRING relationships to AAAS, NDC1, NUP155, NUP88 and RAE1 and membership in several hu.MAP nuclear-pore assemblies, including (hu.MAP huMAP3_12581.1), (hu.MAP huMAP3_07492.1), (hu.MAP huMAP3_08489.1), (hu.MAP huMAP3_09710.1) and (hu.MAP huMAP3_09825.1). Its annotations support RNA export, protein import and nucleocytoplasmic transport. HPA places it in the nucleoplasm and reports testis detection, and its disease associations include Sandestig-Stefanova syndrome and viral-infection contexts.
- **Conclusion**: Established evidence identifies NUP188 as a nuclear-pore component and a central connector of the module's best-supported subnetwork. Its testis co-abundance is consistent with active nuclear transport in germ cells, but that tissue-specific role remains a hypothesis rather than a demonstrated consequence of this module.

#### RAE1

- **Related proteins** (co-abundance neighbors): APCS (0.90); STRING partners: AAAS (0.924), NDC1 (0.833), NUP155 (0.934), NUP188 (0.878), NUP88 (0.942)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12581.1, huMAP3_08442.1, huMAP3_09220.1, huMAP3_06369.1, huMAP3_10000.1
- **Function (MyGene.info)**: ribonucleic acid export 1. Mutations in the Schizosaccharomyces pombe Rae1 and Saccharomyces cerevisiae Gle2 genes have been shown to result in accumulation of poly(A)-containing mRNA in the nucleus, suggesting that the encoded proteins are involved in RNA export. The protein encoded by this gene is a homolog of yeast Rae1. It contains four WD40 motifs, and has been shown to localize to distinct foci in the nucleoplasm, to …
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); COVID-19 (0.370); Histiocytosis (0.370)
- **Europe PMC papers**: 1837
- **Why important**: RAE1 links the nuclear-pore region to mRNA export and mitotic-spindle biology. It has STRING relationships with the principal nucleoporins and occurs in hu.MAP assemblies (hu.MAP huMAP3_12581.1), (hu.MAP huMAP3_08442.1), (hu.MAP huMAP3_09220.1), (hu.MAP huMAP3_06369.1) and (hu.MAP huMAP3_10000.1). HPA reports testis enhancement and cell-type enhancement in early spermatids, late primary spermatocytes and oocytes. Its annotations and disease associations also connect it to RNA export, spindle organization and viral-infection biology.
- **Conclusion**: Established evidence supports RAE1 as an RNA-export and cell-division-related component of the known nuclear-transport subnetwork. Its germ-cell pattern makes it a strong candidate for a spermatogenic interpretation, but the module does not establish a causal role in germ-cell differentiation.

#### ODF2

- **Related proteins** (co-abundance neighbors): DPCD (0.85), PFN3 (0.84), PDHX (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location Primary cilium, Centrosome, Basal body, Connecting piece; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: outer dense fiber of sperm tails 2. The outer dense fibers are cytoskeletal structures that surround the axoneme in the middle piece and principal piece of the sperm tail. The fibers function in maintaining the elastic structure and recoil of the sperm tail as well as in protecting the tail from shear forces during epididymal transport and ejaculation. Defects in the outer dense fibers lead to abnormal sperm morphology and infertili…
- **Diseases (Open Targets)**: non-syndromic male infertility due to sperm motility disorder (0.074); spermatogenic failure 43 (0.067); spermatogenic failure 27 (0.067); spermatogenic failure 34 (0.067); spermatogenic failure 24 (0.066)
- **Europe PMC papers**: 861
- **Why important**: ODF2 provides a direct testis and sperm-structural anchor. It is testis-enriched, enhanced in late spermatids, and localized to the primary cilium, centrosome, basal body and sperm connecting piece. Its network links to DPCD, PFN3 and PDHX. The gene encodes an outer-dense-fiber protein, and its disease associations include male infertility and spermatogenic-failure phenotypes.
- **Conclusion**: Established evidence supports ODF2 as a sperm-tail and cilium-associated structural protein relevant to male fertility. Its presence argues that the module is not solely a generic housekeeping or nuclear-pore signature. A functional connection between ODF2 and the nucleoporin or metabolic branches is plausible but unproven.

#### APCS

- **Related proteins** (co-abundance neighbors): NUP88 (0.91), RAE1 (0.90), NDUFAF4 (0.86), MTX1 (0.85), PSMG1 (0.84), DLAT (0.83), NDUFA6 (0.81), CISD1 (0.81), NDRG3 (0.81), DNAJB1 (0.81), BCAP29 (0.80), LARS2 (0.80), CHCHD3 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: amyloid P component, serum. The protein encoded by this gene is a glycoprotein, belonging to the pentraxin family of proteins, which has a characteristic pentameric organization. These family members have considerable sequence homology which is thought to be the result of gene duplication. The binding of the encoded protein to proteins in the pathological amyloid cross-beta fold suggests its possible role as a chaperone. Thi…
- **Diseases (Open Targets)**: AL amyloidosis (0.370); aortic stenosis (0.274); restless legs syndrome (0.262); bacterial infectious disease (0.215); splenic disorder (0.210)
- **Europe PMC papers**: 49159
- **Why important**: APCS is one of the module's most connected members and is biologically distinctive because it is liver- and hepatocyte-enriched and secreted to blood. It connects in the module to NUP88, RAE1, NDUFAF4, MTX1, PSMG1, DLAT, NDUFA6 and CISD1, although STRING does not report established partners for it in this query. APCS has extensive literature and disease associations involving amyloidosis, aortic stenosis, infection and inflammatory biology.
- **Conclusion**: Established evidence supports APCS as a circulating pentraxin-family protein and a likely contributor to the circulatory-system signal. Its apparent connection to nuclear-pore and mitochondrial proteins should be treated cautiously: it may reflect co-abundance, plasma carryover or shared tissue state rather than direct molecular interaction.

#### PDHX

- **Related proteins** (co-abundance neighbors): MFGE8 (0.87), CEP76 (0.85), ODF2 (0.83), NDC1 (0.80); STRING partners: DLAT (0.998)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_04919.1, huMAP3_08216.1, huMAP3_07514.1, huMAP3_09761.1, huMAP3_10899.1, huMAP3_10412.1, huMAP3_14339.1, huMAP3_11877.1, huMAP3_14864.1, huMAP3_12248.1
- **Function (MyGene.info)**: pyruvate dehydrogenase complex component X. The pyruvate dehydrogenase (PDH) complex is located in the mitochondrial matrix and catalyzes the conversion of pyruvate to acetyl coenzyme A. The PDH complex thereby links glycolysis to Krebs cycle. The PDH complex contains three catalytic subunits, E1, E2, and E3, two regulatory subunits, E1 kinase and E1 phosphatase, and a non-catalytic subunit, E3 binding protein (E3BP). This gene encodes the …
- **Diseases (Open Targets)**: pyruvate dehydrogenase E3-binding protein deficiency (0.793); hereditary disease (0.453); mitochondrial disease (0.445); Leigh syndrome (0.371); ovarian dysfunction (0.269)
- **Europe PMC papers**: 976
- **Why important**: PDHX marks the module's mitochondrial pyruvate-utilization branch. It is connected to MFGE8, CEP76, ODF2 and NDC1 in the co-abundance graph, has a known STRING relationship with DLAT, and appears repeatedly in hu.MAP pyruvate-dehydrogenase assemblies (hu.MAP huMAP3_04919.1), (hu.MAP huMAP3_08216.1) (hu.MAP huMAP3_07514.1), (hu.MAP huMAP3_09761.1) (hu.MAP huMAP3_10899.1) and (hu.MAP huMAP3_10412.1), (hu.MAP huMAP3_14339.1) (hu.MAP huMAP3_11877.1) (hu.MAP huMAP3_14864.1) (hu.MAP huMAP3_12248.1). Its annotations identify it as the E3-binding component of the pyruvate-dehydrogenase complex, and its disease associations include PDH deficiency and mitochondrial disease.
- **Conclusion**: Established evidence supports PDHX as a pyruvate-dehydrogenase and mitochondrial-energy component. Its testis detection and connection to ODF2 make energy supply for sperm-related biology a reasonable hypothesis, but the module does not prove a direct metabolic-structural interaction.

## Module 4

**Tissue pair**: circulatory_system and testis  
**Genes (19)**: ACOT9, ALG2, AP1B1, CADM1, DHX9, DYNC1H1, EIF3C, EML2, GSN, HOOK1, NUDCD1, OXR1, PCCB, PEPD, IARS2, MARS1, SNRNP200, EFTUD2, VCL

### Function

The module does not have a GO or KEGG term that passes global correction, so no pathway-level enrichment can be claimed from the primary enrichment analysis. Its gene-level evidence instead points to several connected cellular processes: pre-mRNA splicing through EFTUD2, SNRNP200 and DHX9; cytoplasmic and mitochondrial protein synthesis through EIF3C, MARS1 and IARS2; cell adhesion and actin organization through CADM1, VCL and GSN; and intracellular trafficking, microtubule organization and metabolism through HOOK1, EML2, DYNC1H1, OXR1, ALG2, ACOT9 and PCCB. The co-abundance structure is therefore best interpreted as a mixed, broadly cellular module rather than a narrowly defined tissue-specific pathway. The strongest coherent substructure is the spliceosomal pair EFTUD2-SNRNP200, supported by STRING and multiple hu.MAP complexes (hu.MAP huMAP3_00960.1) through (hu.MAP huMAP3_08980.1).

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: GSN is the sole secreted gene identified by HPA, while the other genes are intracellular or membrane-associated. Most genes have low tissue specificity, and most have low immune-cell specificity, arguing against a simple blood-cell module. There are nevertheless cell-type signals involving neural and sensory cells, neutrophils, syncytiotrophoblasts, spermatogenic cells and other specialized populations. Testis protein detection is widespread across the module, whereas the circulatory-system HPA tissue comparison has no matching tissue-level protein result. Thus, shared abundance may partly reflect broadly expressed cellular machinery and shared cell-type composition rather than a dedicated circulatory-system-to-testis biological program. GSN, CADM1 and VCL also raise the possibility of vascular, platelet-associated or adhesion-related contributions, but the HPA evidence does not support calling the module blood-cell enriched overall.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited set of high-confidence relationships: EFTUD2-SNRNP200 is especially strong, DHX9-SNRNP200 is also supported, GSN-VCL supports an actin-related connection, and IARS2-MARS1 supports a translation-related connection. These links indicate that parts of the co-abundance module recapitulate known molecular relationships rather than defining an entirely disconnected gene set. hu.MAP independently places EFTUD2 and SNRNP200 together in several spliceosomal and snRNP-related complexes (hu.MAP huMAP3_00960.1), (hu.MAP huMAP3_07622.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), (hu.MAP huMAP3_09945.1) and (hu.MAP huMAP3_08980.1). PCCB and IARS2 occur together in a large metabolic and mitochondrial complex (hu.MAP huMAP3_13468.1). Because most module genes do not have listed STRING partners or hu.MAP membership, the full module is not a single experimentally established complex. The evidence instead supports a sparse co-abundance network containing a well-supported spliceosomal core, a translation-related pair, an actin-adhesion pair, and additional links that may reflect shared cellular state or tissue composition.

**STRING interactions (score >= 0.7)**: 4 of 171 gene pairs: DHX9–SNRNP200 (0.784); EFTUD2–SNRNP200 (0.999); GSN–VCL (0.918); IARS2–MARS1 (0.995)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00960.1 (SNRNP200, EFTUD2; 2/8); huMAP3_07622.1 (SNRNP200, EFTUD2; 2/9); huMAP3_08501.1 (SNRNP200, EFTUD2; 2/47); huMAP3_09504.1 (SNRNP200, EFTUD2; 2/51); huMAP3_09945.1 (SNRNP200, EFTUD2; 2/61); huMAP3_08980.1 (SNRNP200, EFTUD2; 2/97); huMAP3_13468.1 (PCCB, IARS2; 2/99)

### Novelty

The module-level finding may be novel as a conserved co-abundance pattern shared by circulatory_system and testis, because the fact sheet does not identify a previously named module or a complete known complex corresponding to all module genes. However, its component biology is not novel: spliceosomal, aminoacylation, cytoskeletal, adhesion, vesicle-trafficking and metabolic functions are established, and several pairwise relationships are already represented in STRING or hu.MAP. The absence of STRING or hu.MAP support for many edges cannot by itself establish novelty, because those databases do not measure this specific cross-tissue co-abundance relationship. The most defensible novelty claim is therefore a potentially new combination and cross-tissue abundance pattern, not discovery of a new molecular function or interaction.

**Hypothesis.** Hypothesis: the conserved module reflects a shared demand for basic cellular maintenance in cells represented in both tissues, combining RNA processing, protein synthesis, cytoskeletal and adhesion control, organelle trafficking, and intermediary metabolism. In testis, this state could be expressed during specialized germ-cell differentiation, where HPA signals implicate spermatids and spermatocytes and where rapid structural and translational remodeling is expected. In circulatory-system samples, the same abundance pattern could arise from broadly expressed cells or from vascular, platelet-associated or other tissue-associated cellular components rather than from circulating secreted proteins. The spliceosomal core and translation-related genes may coordinate transcript maturation and protein production, while CADM1, VCL, GSN, HOOK1 and EML2 could connect this state to adhesion, actin organization and microtubule-dependent trafficking. This is a mechanistic model requiring validation by cell-resolved expression, perturbation and protein-level interaction experiments; it is not established by the co-abundance result alone.

### Important genes

#### EFTUD2

- **Related proteins** (co-abundance neighbors): EIF3C (0.88), SNRNP200 (0.86), DHX9 (0.81); STRING partners: SNRNP200 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_08980.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 is a central bridge in the module, connecting EIF3C, SNRNP200 and DHX9. It has a direct high-confidence STRING relationship with SNRNP200 and appears with SNRNP200 in multiple hu.MAP spliceosomal complexes (hu.MAP huMAP3_00960.1) through (hu.MAP huMAP3_08980.1). Its established function is as a spliceosome-associated GTPase involved in snRNP assembly, spliceosome conformational change and pre-mRNA splicing. It also has a substantial literature base and a disease association with mandibulofacial dysostosis with microcephaly.
- **Conclusion**: Established conclusion: EFTUD2 is the strongest anchor for a spliceosome-related substructure within the module. Hypothesis: its co-abundance with translation and cytoskeletal genes may mark coordinated RNA-processing and cellular-remodeling demands shared by cells in the two tissues.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.86); STRING partners: DHX9 (0.784), EFTUD2 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is directly connected to EFTUD2 and DHX9 in STRING and is included with EFTUD2 across several hu.MAP complexes (hu.MAP huMAP3_00960.1) through (hu.MAP huMAP3_08980.1). It is a core U5 snRNP component and RNA helicase involved in spliceosome assembly and remodeling. Its network position is especially informative because the same pair is supported by both the co-abundance network and independent molecular-interaction resources. It also has established associations with retinitis pigmentosa and inherited retinal dystrophy.
- **Conclusion**: Established conclusion: SNRNP200 provides strong evidence that part of the module reflects conserved spliceosomal machinery. Hypothesis: coordinated SNRNP200 abundance may support transcript processing during the specialized differentiation state suggested by the testis observations, but the cross-tissue mechanism remains unproven.

#### MARS1

- **Related proteins** (co-abundance neighbors): EIF3C (0.86), HOOK1 (0.80), IARS2 (0.80); STRING partners: IARS2 (0.995)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionyl-tRNA synthetase 1. This gene encodes a member of the class I family of aminoacyl-tRNA synthetases. These enzymes play a critical role in protein biosynthesis by charging tRNAs with their cognate amino acids. The encoded protein is a component of the multi-tRNA synthetase complex and catalyzes the ligation of methionine to tRNA molecules. [provided by RefSeq, Jan 2011].
- **Diseases (Open Targets)**: severe early-onset pulmonary alveolar proteinosis due to MARS deficiency (0.745); Charcot-Marie-Tooth disease axonal type 2U (0.676); autosomal recessive spastic paraplegia type 70 (0.614); trichothiodystrophy 9, nonphotosensitive (0.428); pulmonary alveolar proteinosis (0.338)
- **Europe PMC papers**: 435
- **Why important**: MARS1 links EIF3C and IARS2 in the module and has a high-confidence STRING relationship with IARS2. It encodes methionyl-tRNA synthetase, an established enzyme required for charging tRNA and protein biosynthesis, and is part of the multi-tRNA synthetase context described in the fact sheet. Its disease associations include severe early-onset pulmonary alveolar proteinosis and several inherited neurological or neuromuscular disorders. Its network position connects cytosolic translation-related evidence to mitochondrial translation-related evidence through IARS2.
- **Conclusion**: Established conclusion: MARS1 marks a protein-production and aminoacylation component of the module. Hypothesis: the MARS1-IARS2 connection may indicate coordinated cytosolic and mitochondrial translational capacity, although the co-abundance data do not establish direct functional coupling in these tissues.

#### CADM1

- **Related proteins** (co-abundance neighbors): VCL (0.89), GSN (0.81), PEPD (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell adhesion molecule 1. Enables signaling receptor binding activity. Involved in several processes, including cell recognition; positive regulation of cytokine production; and susceptibility to natural killer cell mediated cytotoxicity. Located in plasma membrane. Implicated in breast carcinoma and prostate cancer. Biomarker of cervix uteri carcinoma in situ. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypothyroidism (0.505); Abnormality of the skeletal system (0.485); obesity disorder (0.420); restless legs syndrome (0.402); autoimmune thyroid disease (0.342)
- **Europe PMC papers**: 3471
- **Why important**: CADM1 connects VCL, GSN and PEPD and is the module's clearest membrane-associated adhesion regulator. It is involved in cell recognition, homophilic and heterophilic adhesion, cytokine regulation and susceptibility to natural-killer-cell-mediated cytotoxicity. HPA identifies tissue enhancement in retina and cell-type signals in epithelial, glial and photoreceptor populations, while the fact sheet also records immune-cell enhancement in selected blood cell types. CADM1 has a large literature base and disease associations including breast carcinoma and prostate cancer.
- **Conclusion**: Established conclusion: CADM1 supports a cell-contact and adhesion interpretation for one branch of the module. Hypothesis: CADM1 may couple tissue or cell-contact composition to the intracellular cytoskeletal branch, but it should not be treated as evidence that the entire module is an immune or vascular program.

#### GSN

- **Related proteins** (co-abundance neighbors): CADM1 (0.81); STRING partners: VCL (0.918)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gelsolin. The protein encoded by this gene binds to the 'plus' ends of actin monomers and filaments to prevent monomer exchange. The encoded calcium-regulated protein functions in both assembly and disassembly of actin filaments. Defects in this gene are a cause of familial amyloidosis Finnish type (FAF). Multiple transcript variants encoding several different isoforms have been found for this gene. [provid…
- **Diseases (Open Targets)**: Finnish type amyloidosis (0.805); AL amyloidosis (0.463); neuropathy (0.418); cardiomyopathy (0.418); cutis laxa (0.417)
- **Europe PMC papers**: 5062
- **Why important**: GSN is connected to CADM1 in the module and to VCL in STRING, forming the clearest actin-associated substructure. It is a calcium-regulated actin filament remodeling protein, is enriched in heart muscle in HPA, is detected in vascular endothelial cells and is secreted to blood. Its established disease associations include Finnish-type familial amyloidosis, amyloidosis, neuropathy and cardiomyopathy. Its substantial literature volume and unique secreted status make it important for interpreting whether the shared module partly reflects circulating or vascular material.
- **Conclusion**: Established conclusion: GSN provides evidence for actin remodeling and is the only module gene identified as secreted to blood. Hypothesis: GSN could contribute to a blood or vascular sampling component in circulatory-system data while also participating in adhesion-associated cytoskeletal remodeling, but the fact sheet does not demonstrate that this explains the conserved module.

## Module 5

**Tissue pair**: circulatory_system and testis  
**Genes (28)**: ACSS2, ADD3, AIFM1, DYNC1I2, DDX3Y, EML4, ETFDH, GDAP1, HACL2, ME1, NDUFS1, NEK9, NSFL1C, PAPSS2, PPP3CA, PRPF31, PPAT, SCRN2, SDHA, SMCHD1, SMARCC2, SRP72, FARSB, IARS1, KARS1, TOP2A, TRIM25, UBA3

### Function

No GO/KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The gene set instead suggests a heterogeneous cellular maintenance program combining mitochondrial energy metabolism, protein synthesis and modification, RNA handling, cytoskeletal or microtubule organization, cell-cycle control, and chromatin or DNA processes. The strongest direct network-supported themes are mitochondrial coupling through SDHA and NDUFS1, aminoacyl-tRNA synthetase connectivity through IARS1 and KARS1, and a microtubule-associated NEK9–EML4 relationship supported by STRING and hu.MAP. The STRING acetylation and isopeptide-bond keywords (STRING Keyword Acetylation; within-query FDR = 0.0439) (STRING Keyword Isopeptide bond; within-query FDR = 0.0439) are supplementary and should not be interpreted as globally corrected pathway enrichment.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary identifies only one secreted gene, while the listed proteins are predominantly intracellular and include mitochondrial, nuclear, cytosolic, cytoskeletal, and membrane-associated proteins. Most genes have low tissue specificity, although tissue-enhanced signals occur in muscle, brain, liver, bone marrow, adrenal gland, and testis. The strong representation of cell-type-enhanced genes, including neutrophils and neutrophil progenitors as well as cardiomyocytes, neurons, spermatogenic cells, and Sertoli cells, argues against a narrowly testis-specific program. The shared circulatory-system and testis signal could therefore reflect broadly distributed cellular machinery, shared cell states, or sample cellular composition rather than a circulating secretome. HPA protein detection is reported for nearly all module genes in testis, whereas the circulatory-system entry has no matching HPA tissue measurement.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a limited but coherent set of high-confidence relationships. EML4–NEK9, IARS1–KARS1, FARSB–IARS1, FARSB–KARS1, and NDUFS1–SDHA are consistent with microtubule or mitotic organization, aminoacyl-tRNA synthetase biology, and mitochondrial respiration. PAPSS2–SDHA links the most central co-abundance gene to mitochondrial metabolism, but co-abundance does not establish a direct physical interaction. hu.MAP independently supports repeated membership of NEK9 and EML4 in related microtubule-associated complexes (hu.MAP huMAP3_04397.1) (hu.MAP huMAP3_08321.1) (hu.MAP huMAP3_14043.1) (hu.MAP huMAP3_09835.1) (hu.MAP huMAP3_09233.1) (hu.MAP huMAP3_10475.1), and of IARS1 and KARS1 in aminoacyl-tRNA synthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). Most module genes have no recorded hu.MAP complex or high-confidence STRING partner in the supplied evidence. Thus, the network contains islands of established molecular association embedded in a broader co-abundance structure; it should not be treated as one experimentally established protein complex.

**STRING interactions (score >= 0.7)**: 6 of 378 gene pairs: EML4–NEK9 (0.811); FARSB–IARS1 (0.914); FARSB–KARS1 (0.813); IARS1–KARS1 (0.999); NDUFS1–SDHA (0.995); PAPSS2–SDHA (0.86)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Acetylation (FDR = 0.0439, 23 genes); Keyword Isopeptide bond (FDR = 0.0439, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04397.1 (NEK9, EML4; 2/4); huMAP3_08321.1 (NEK9, EML4; 2/5); huMAP3_14043.1 (NEK9, EML4; 2/5); huMAP3_09835.1 (NEK9, EML4; 2/6); huMAP3_02637.1 (IARS1, KARS1; 2/14); huMAP3_13688.1 (IARS1, KARS1; 2/14); huMAP3_09233.1 (NEK9, EML4; 2/34); huMAP3_10475.1 (NEK9, EML4; 2/39)

### Novelty

The co-abundance module may represent a new cross-tissue association because it combines genes from mitochondrial metabolism, translation, microtubule biology, RNA processing, chromatin regulation, and spermatogenesis in a pattern not reproduced as a single established STRING or hu.MAP complex. However, the individual processes and several gene relationships are already known, especially the NEK9–EML4, aminoacyl-tRNA synthetase, and respiratory-chain connections. The sparse STRING connectivity and partial hu.MAP overlap support possible novelty of the module-level organization, but absence from those resources alone does not prove a new biological mechanism. The appropriate conclusion is that this is a potentially novel co-abundance configuration requiring independent replication, cell-composition adjustment, and perturbation or biochemical validation.

**Hypothesis.** Hypothesis: the module reflects coordinated demand for energy production, translation, cytoskeletal remodeling, and quality-control processes in cells represented in both circulatory-system and testis samples. In testis, this could be especially relevant to proliferating or differentiating germ cells, where TOP2A, DDX3Y, NEK9, and EML4 support cell-cycle, RNA, and microtubule functions, while mitochondrial genes support energetic and redox requirements. In circulation, the same signal may arise from blood-cell or progenitor populations and from broadly expressed intracellular machinery rather than from plasma proteins. PAPSS2 may act as a high-connectivity metabolic bridge linking otherwise distinct functional neighborhoods, but this bridging role is a network hypothesis rather than an established molecular interaction.

### Important genes

#### PAPSS2

- **Related proteins** (co-abundance neighbors): HACL2 (0.90), PPAT (0.85), EML4 (0.85), PPP3CA (0.84), ADD3 (0.84), ACSS2 (0.84), SRP72 (0.83), FARSB (0.83), IARS1 (0.83), TRIM25 (0.82), NEK9 (0.80), SDHA (0.80); STRING partners: SDHA (0.86)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3'-phosphoadenosine 5'-phosphosulfate synthase 2. Sulfation is a common modification of endogenous (lipids, proteins, and carbohydrates) and exogenous (xenobiotics and drugs) compounds. In mammals, the sulfate source is 3'-phosphoadenosine 5'-phosphosulfate (PAPS), created from ATP and inorganic sulfate. Two different tissue isoforms encoded by different genes synthesize PAPS. This gene encodes one of the two PAPS synthetases. Defects in this gen…
- **Diseases (Open Targets)**: spondyloepimetaphyseal dysplasia, PAPSS2 type (0.799); hereditary disease (0.471); Spondyloepiphyseal dysplasia and spondyloepimetaphyseal dysplasia (0.462); autosomal recessive brachyolmia (0.455); skeletal dysplasia (0.343)
- **Europe PMC papers**: 1005
- **Why important**: PAPSS2 is the most central node in the supplied co-abundance graph and connects metabolic, cytoskeletal, signaling, translation-related, and mitochondrial neighbors. Its established function is production of PAPS for sulfation of endogenous and exogenous compounds. HPA describes adrenal and several cell-type-enhanced signals, with mitochondrial localization and testis protein detection. Its disease associations include PAPSS2-related skeletal dysplasia, and its literature base is substantial.
- **Conclusion**: Established evidence supports PAPSS2 as the network hub and as a sulfate-donor biosynthesis enzyme with skeletal-dysplasia relevance. It is a plausible integrator of the module, but the data do not establish that PAPSS2 mechanistically regulates the other module genes or that sulfation explains the cross-tissue co-abundance.

#### EML4

- **Related proteins** (co-abundance neighbors): PAPSS2 (0.85), DDX3Y (0.80); STRING partners: NEK9 (0.811)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules, Primary cilium, Annulus; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_04397.1, huMAP3_08321.1, huMAP3_14043.1, huMAP3_09835.1, huMAP3_09233.1, huMAP3_10475.1
- **Function (MyGene.info)**: EMAP like 4. This gene is a member of the echinoderm microtubule associated protein-like family. The encoded WD-repeat protein may be involved in microtubule formation. Abnormal fusion of parts of this gene with portions of the anaplastic lymphoma receptor tyrosine kinase gene, which generates EML4-ALK fusion transcripts, is one of the primary mutations associated with non-small cell lung cancer. Alternative s…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.704); cancer (0.668); Abnormality of the skeletal system (0.628); neoplasm (0.601); lung adenocarcinoma (0.453)
- **Europe PMC papers**: 7119
- **Why important**: EML4 is directly connected to NEK9 in STRING and repeatedly co-occurs with NEK9 in hu.MAP complexes (hu.MAP huMAP3_04397.1) (hu.MAP huMAP3_08321.1) (hu.MAP huMAP3_14043.1) (hu.MAP huMAP3_09835.1) (hu.MAP huMAP3_09233.1) (hu.MAP huMAP3_10475.1). Its established function concerns microtubule formation, mitotic progression, chromosome alignment, and kinetochore attachment. HPA places it in microtubules, the primary cilium, and the annulus, with cell-type-enhanced signals in immune and progenitor populations and protein detection in testis. It also has extensive literature and a well-known EML4–ALK cancer association.
- **Conclusion**: Established evidence makes EML4 the clearest cytoskeletal and mitotic anchor of the module. It supports a real microtubule-related component, but its co-abundance with the metabolic and translation genes remains a module-level association rather than proof of a unified EML4-centered pathway.

#### IARS1

- **Related proteins** (co-abundance neighbors): PAPSS2 (0.83); STRING partners: FARSB (0.914), KARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Isoleucine-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family and has been identified as a …
- **Diseases (Open Targets)**: growth retardation, intellectual developmental disorder, hypotonia, and hepatopathy (0.733); Abnormality of the skeletal system (0.332); microcephaly (0.289); Global developmental delay (0.289); Hallux valgus (0.184)
- **Europe PMC papers**: 184
- **Why important**: IARS1 participates in high-confidence STRING relationships with KARS1 and FARSB and in aminoacyl-tRNA synthetase complexes with KARS1 (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). Its established function is isoleucyl-tRNA aminoacylation and translational fidelity. HPA reports testis protein detection and broad low tissue specificity. It has disease and autoantibody relevance through developmental disorders and inflammatory myopathy-related biology, although its literature volume is lower than that of the major hub genes.
- **Conclusion**: Established evidence supports IARS1 as part of a translation and proteome-maintenance neighborhood. It strengthens the interpretation that the module includes biosynthetic housekeeping machinery, but there is no evidence that IARS1 explains the tissue pairing or directly links translation to the other module neighborhoods.

#### DDX3Y

- **Related proteins** (co-abundance neighbors): TOP2A (0.82), UBA3 (0.82), AIFM1 (0.81), EML4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 3 Y-linked. The protein encoded by this gene is a member of the DEAD-box RNA helicase family, characterized by nine conserved motifs, included the conserved Asp-Glu-Ala-Asp (DEAD) motif. These motifs are thought to be involved in ATP binding, hydrolysis, RNA binding, and in the formation of intramolecular interactions. This protein shares high similarity to DDX3X, on the X chromosome, but a deletion of this g…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.074); ataxia telangiectasia (0.062); breast carcinoma (0.055); Adams-Oliver syndrome (0.039); Azoospermia (0.034)
- **Europe PMC papers**: 1892
- **Why important**: DDX3Y is a Y-linked DEAD-box RNA helicase with cell-type-enhanced signals in early and late spermatids, hematopoietic stem cells, progenitors, and neutrophils. It connects in the co-abundance graph to TOP2A, UBA3, AIFM1, and EML4. Its established biology includes RNA binding and ATP-dependent RNA remodeling, gamete generation, and male infertility when disrupted. It has a substantial literature base and is especially informative for the testis component.
- **Conclusion**: Established evidence supports DDX3Y as a biologically meaningful testis and germ-cell-related member that may also reflect hematopoietic cell states. Its presence favors a shared proliferative or RNA-management program, but it does not demonstrate that the entire module is germ-cell-specific or that DDX3Y drives the network.

#### SDHA

- **Related proteins** (co-abundance neighbors): PAPSS2 (0.80); STRING partners: NDUFS1 (0.995), PAPSS2 (0.86)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate dehydrogenase complex flavoprotein subunit A. This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identi…
- **Diseases (Open Targets)**: mitochondrial complex II deficiency, nuclear type 1 (0.813); pheochromocytoma/paraganglioma syndrome 5 (0.790); dilated cardiomyopathy 1GG (0.768); neurodegeneration with ataxia and late-onset optic atrophy (0.761); gastrointestinal stromal tumor (0.743)
- **Europe PMC papers**: 12756
- **Why important**: SDHA is a catalytic component of mitochondrial complex II and is linked by STRING to NDUFS1 and PAPSS2. HPA shows enhancement in heart and skeletal muscle, neuronal cell-type signals, mitochondrial localization, and testis protein detection. Its established disease associations include mitochondrial complex deficiency, cardiomyopathy, and tumor-predisposition syndromes, and it has a large literature base.
- **Conclusion**: Established evidence supports SDHA as a mitochondrial respiration marker and a plausible energetic component of the module. The SDHA–NDUFS1 relationship is biologically coherent, but the module does not establish a complete respiratory-chain program or prove that altered mitochondrial activity causes the observed cross-tissue co-abundance.

## Module 6

**Tissue pair**: circulatory_system and testis  
**Genes (22)**: PGM3, CAND2, DIAPH2, GMPS, ISYNA1, IPO11, MCM2, MCM4, MCM6, MOV10, MYH10, OAT, ALDH18A1, PLCD1, PFAS, UPF1, RUSF1, SELENBP1, PSAT1, SMC2, SMC4, UBE3A

### Function

The strongest interpretation is a nuclear DNA-replication and chromosome-organization module, with an associated RNA-surveillance and nucleotide-metabolism component. The primary evidence is the globally corrected enrichment for nuclear DNA replication (GO:BP nuclear DNA replication; q_global = 0.000977), cell-cycle and mitotic DNA replication (GO:BP cell cycle DNA replication; q_global = 0.00189)(GO:BP mitotic DNA replication; q_global = 0.00438), DNA-helicase and double-stranded DNA-helicase activity (GO:MF double-stranded DNA helicase activity; q_global = 0.00782)(GO:MF helicase activity; q_global = 0.0172)(GO:MF DNA helicase activity; q_global = 0.0331), the DNA-replication preinitiation, MCM, and CMG complexes (GO:CC DNA replication preinitiation complex; q_global = 0.0132)(GO:CC MCM complex; q_global = 0.0132)(GO:CC CMG complex; q_global = 0.0132), and chromosome-associated functions (GO:CC nuclear chromosome; q_global = 0.0123). MCM2, MCM4, and MCM6 provide the clearest replication-core signal; SMC2 and SMC4 connect this signal to chromosome condensation and organization. UPF1 and MOV10 add helicase, ATP-dependent, RNA-processing, and surveillance biology. The evidence supports a proliferative, genome-maintenance program rather than a specialized secreted or circulating-protein function.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. The module is instead composed largely of intracellular nuclear, nucleoplasmic, cytosolic, mitochondrial, or structural proteins. Its HPA pattern is strongly cell-type associated, with recurring enrichment in Sertoli cells and hematopoietic progenitor populations, including erythrocyte, megakaryocyte, monocyte, and neutrophil progenitors. Several genes are enhanced in lymphoid tissue or bone marrow, while others are enhanced in testis or Sertoli cells. Protein detection is broadly reported in testis, whereas the circulatory-system comparison has no matching HPA tissue entry. Thus, the shared co-abundance signal may reflect proliferating or lineage-specific cells present in both tissue groups, and should not automatically be interpreted as a whole-organ program. The presence of testis and hematopoietic cell-type signatures makes shared cell composition a serious alternative explanation.

**GO/KEGG enrichment**: 21 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP nuclear DNA replication | 0.000977 | MCM2, MCM4, MCM6, UPF1 |
| GO:MF single-stranded DNA binding | 0.00114 | MCM2, MCM4, MCM6, SMC2, SMC4 |
| GO:BP cell cycle DNA replication | 0.00189 | MCM2, MCM4, MCM6, UPF1 |
| GO:BP mitotic DNA replication | 0.00438 | MCM2, MCM4, MCM6 |
| GO:MF double-stranded DNA helicase activity | 0.00782 | MCM2, MCM4, MCM6, UPF1 |
| GO:MF isomerase activity | 0.0115 | ISYNA1, MCM2, MCM4, MCM6, MOV10, MYH10, PGM3, UPF1 |
| GO:CC nuclear chromosome | 0.0123 | MCM2, MCM4, MCM6, SMC2, SMC4 |
| GO:BP double-strand break repair via break-induced replication | 0.0132 | MCM2, MCM4, MCM6 |
| GO:BP regulation of DNA-templated DNA replication initiation | 0.0132 | MCM2, MCM4, MCM6 |
| GO:CC DNA replication preinitiation complex | 0.0132 | MCM2, MCM4, MCM6 |
| GO:CC MCM complex | 0.0132 | MCM2, MCM4, MCM6 |
| GO:CC CMG complex | 0.0132 | MCM2, MCM4, MCM6 |
| GO:BP regulation of DNA-templated DNA replication | 0.0132 | MCM2, MCM4, MCM6 |
| GO:MF macromolecular conformation isomerase activity | 0.0154 | MCM2, MCM4, MCM6, MOV10, MYH10, UPF1 |
| GO:MF helicase activity | 0.0172 | MCM2, MCM4, MCM6, MOV10, UPF1 |

### STRING and hu.MAP

STRING supports a coherent replication and chromosome subnetwork: MCM2, MCM4, and MCM6 have very strong mutual relationships, SMC2 and SMC4 are strongly related, and the MCM proteins connect to the SMC proteins. STRING also supports the MOV10-UPF1 relationship and a separate metabolic group involving ALDH18A1, OAT, and PSAT1. These relationships are concordant with the primary GO evidence, but STRING enrichment is supplementary (15 supplementary STRING terms; within-query FDR 0.0019–0.023) and should not be treated as global enrichment significance. hu.MAP independently identifies many complexes containing MCM2, MCM4, and MCM6, including MCM assemblies and larger replisome or chromatin-associated assemblies (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1). SMC2-SMC4 complexes are also represented (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_14663.1), and MOV10-UPF1 occur in an RNA-processing complex (hu.MAP huMAP3_06975.1). The replication-core and condensin relationships are therefore already established molecular relationships, not newly discovered physical interactions. The weaker metabolic and signaling connections have much less direct complex support.

**STRING interactions (score >= 0.7)**: 12 of 231 gene pairs: ALDH18A1–GMPS (0.909); ALDH18A1–OAT (0.998); ALDH18A1–PSAT1 (0.842); MCM2–MCM4 (0.999); MCM2–MCM6 (0.999); MCM4–MCM6 (0.999); MCM4–SMC2 (0.748); MCM4–SMC4 (0.736); MCM6–SMC2 (0.75); MCM6–SMC4 (0.734); MOV10–UPF1 (0.912); SMC2–SMC4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Single-stranded DNA binding (FDR = 0.0019, 5 genes); Keyword Helicase (FDR = 0.0055, 5 genes); Function Helicase activity (FDR = 0.0062, 5 genes); Function ATP hydrolysis activity (FDR = 0.0062, 7 genes); Function ATP-dependent activity (FDR = 0.0062, 8 genes); Function DNA helicase activity (FDR = 0.0082, 4 genes); Keyword ATP-binding (FDR = 0.0114, 11 genes); Component Nuclear chromosome (FDR = 0.0126, 5 genes); Function ATP binding (FDR = 0.0166, 11 genes); Process Nuclear DNA replication (FDR = 0.0176, 4 genes); Function Anion binding (FDR = 0.0176, 14 genes); Function Pyrophosphatase activity (FDR = 0.0196, 8 genes); Component MCM complex (FDR = 0.0216, 3 genes); Component CMG complex (FDR = 0.0216, 3 genes); Component Chromosome, telomeric region (FDR = 0.023, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09860.1 (MCM4, MCM2, MCM6; 3/4); huMAP3_00154.1 (MCM4, MCM2, MCM6; 3/5); huMAP3_06061.1 (MCM4, MCM2, MCM6; 3/5); huMAP3_05529.1 (MCM4, MCM2, MCM6; 3/6); huMAP3_07113.1 (MCM4, MCM2, MCM6; 3/6); huMAP3_14758.1 (MCM4, MCM2, MCM6; 3/14); huMAP3_08554.1 (MCM4, MCM2, MCM6; 3/15); huMAP3_11832.1 (MCM4, MCM2, MCM6; 3/15); huMAP3_12180.1 (MCM4, MCM2, MCM6; 3/17); huMAP3_09466.1 (MCM4, MCM2, MCM6; 3/23); huMAP3_10862.1 (MCM4, MCM2, MCM6; 3/33); huMAP3_14306.1 (MCM4, MCM2, MCM6; 3/55); huMAP3_02602.1 (MCM4, MCM6; 2/2); huMAP3_02871.1 (PLCD1, SELENBP1; 2/6); huMAP3_06970.1 (PGM3, RUSF1; 2/8); huMAP3_03084.1 (SMC2, SMC4; 2/8); huMAP3_14385.1 (SMC2, SMC4; 2/9); huMAP3_09855.1 (SMC2, SMC4; 2/10); huMAP3_11457.1 (SMC2, SMC4; 2/10); huMAP3_11119.1 (MCM4, MCM6; 2/14); huMAP3_14663.1 (SMC2, SMC4; 2/14); huMAP3_08848.1 (MCM4, MCM6; 2/15); huMAP3_06162.1 (PLCD1, SELENBP1; 2/15); huMAP3_08862.1 (PLCD1, SELENBP1; 2/15); huMAP3_09842.1 (PLCD1, SELENBP1; 2/21); huMAP3_10061.1 (PLCD1, SELENBP1; 2/29); huMAP3_06975.1 (UPF1, MOV10; 2/31); huMAP3_12974.1 (PLCD1, SELENBP1; 2/49); huMAP3_10202.1 (CAND2, IPO11; 2/52); huMAP3_11232.1 (CAND2, IPO11; 2/78)

### Novelty

The core biology is not a new molecular function: MCM proteins, condensin components, UPF1, MOV10, and the supported complexes are already well established. The module may nevertheless represent a potentially useful cross-tissue co-abundance observation because it links a replication and chromosome-maintenance program with testis and circulatory-system samples. That observation is not sufficient to claim a new conserved mechanism. The HPA evidence raises the possibility that the apparent conservation is driven by shared proliferating or lineage-specific cell populations, particularly Sertoli and hematopoietic progenitor cells. Absence of some module edges from STRING or hu.MAP does not establish novelty, because those resources are incomplete and measure different kinds of evidence. A genuine novel module-level finding would require replication in independent cohorts, adjustment for cell composition, and preferably experimental or perturbational validation.

**Hypothesis.** Hypothesis: the shared module reflects a cell-state program in which proliferating or differentiating cells coordinate MCM-dependent replication initiation with condensin-mediated chromosome organization, while UPF1 and MOV10 maintain RNA quality and post-transcriptional control and metabolic enzymes provide supporting nucleotide, amino-acid, and phospholipid resources. In testis this could arise in Sertoli-associated or germ-cell developmental contexts; in circulatory-system samples it could arise from hematopoietic progenitor or other cellular admixture. The cross-tissue co-abundance may therefore reflect a conserved requirement for genome duplication and cell-state maintenance, rather than secretion into blood or a tissue-specific endocrine pathway. This remains a hypothesis because the co-abundance data do not demonstrate physical interaction, causality, or cellular origin.

### Important genes

#### MCM4

- **Related proteins** (co-abundance neighbors): MCM6 (0.90), SMC4 (0.81); STRING partners: MCM2 (0.999), MCM6 (0.999), SMC2 (0.748), SMC4 (0.736)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_09860.1, huMAP3_00154.1, huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_11119.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 4. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication rel…
- **Diseases (Open Targets)**: primary immunodeficiency with natural-killer cell deficiency and adrenal insufficiency (0.714); X-linked adrenal hypoplasia congenita (0.185); lung adenocarcinoma (0.112); microcephaly (0.111); neoplasm (0.102)
- **Europe PMC papers**: 4082
- **Why important**: MCM4 is part of the central MCM replication core and connects in the module to MCM6 and the condensin-associated SMC proteins. It appears across every primary replication and helicase-related enrichment listed for the MCM core (5 globally significant GO/KEGG terms, q_global 0.000977–0.00782; see the table)(15 globally significant GO/KEGG terms, q_global 0.0123–0.0431; see the table), is supported by strong STRING relationships, and is present in many hu.MAP replication and chromatin complexes (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1)(hu.MAP huMAP3_11119.1)(hu.MAP huMAP3_08848.1). Its HPA profile links it to bone marrow and spermatogenic cell populations, making it especially informative for the shared tissue context. It also has a substantial literature and established disease associations involving adrenal insufficiency, immunodeficiency, microcephaly, and neoplasia.
- **Conclusion**: Established evidence identifies MCM4 as a replication-initiation and genome-maintenance component, and the network and complex evidence make it a core anchor of this module. The tissue-sharing interpretation and any role for MCM4 in producing the cross-tissue co-abundance pattern remain hypotheses.

#### MCM6

- **Related proteins** (co-abundance neighbors): MCM4 (0.90), PSAT1 (0.83); STRING partners: MCM2 (0.999), MCM4 (0.999), SMC2 (0.75), SMC4 (0.734)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_09860.1, huMAP3_00154.1, huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_11119.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 6. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: lactose intolerance (0.246); neurodegenerative disease (0.225); obesity disorder (0.166); nervous system disorder (0.141); systemic lupus erythematosus (0.140)
- **Europe PMC papers**: 3766
- **Why important**: MCM6 is one of the most strongly connected members of the established MCM2-MCM4-MCM6 subnetwork and participates in the same primary replication, helicase, MCM, CMG, and chromosome terms (21 globally significant GO/KEGG terms, q_global 0.000977–0.0431; see the table). It has strong STRING support with MCM2, MCM4, SMC2, and SMC4 and extensive hu.MAP support across replication-associated complexes (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1)(hu.MAP huMAP3_11119.1)(hu.MAP huMAP3_08848.1). HPA links it to lymphoid tissue and multiple hematopoietic progenitor populations, while also detecting it in testis. Its established role in replication initiation and its substantial literature make it a strong representative of the module core.
- **Conclusion**: Established evidence supports MCM6 as a core replication licensing and replication-fork component whose presence is biologically coherent with the module. It is not evidence by itself that the module is specific to testis or circulation; the cell-type pattern remains a competing explanation.

#### MCM2

- **Related proteins** (co-abundance neighbors): PSAT1 (0.86); STRING partners: MCM4 (0.999), MCM6 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_09860.1, huMAP3_00154.1, huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a canonical member of the MCM replication complex and is directly connected to MCM4 and MCM6 in STRING. It contributes to every primary term associated with the MCM replication core (21 globally significant GO/KEGG terms, q_global 0.000977–0.0431; see the table) and is represented in numerous hu.MAP replication and chromatin complexes (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1). HPA associates it with bone marrow, lymphoid tissue, differentiating spermatogonia, and hematopoietic progenitors, providing a plausible explanation for its appearance in both tissue groups. It has the largest literature volume among the selected replication genes and established associations with hearing loss and developmental abnormalities.
- **Conclusion**: Established evidence makes MCM2 a highly informative marker of the module's replication program. Its broad progenitor and tissue distribution favors a cell-state or cell-composition interpretation over a narrowly organ-specific mechanism.

#### SMC2

- **Related proteins** (co-abundance neighbors): PSAT1 (0.84); STRING partners: MCM4 (0.748), MCM6 (0.75), SMC4 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_03084.1, huMAP3_14385.1, huMAP3_09855.1, huMAP3_11457.1, huMAP3_14663.1
- **Function (MyGene.info)**: structural maintenance of chromosomes 2. Predicted to enable ATP binding activity; chromatin binding activity; and single-stranded DNA binding activity. Involved in mitotic chromosome condensation. Located in condensed chromosome; cytoplasm; and nuclear lumen. Part of condensin complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: basal cell carcinoma (0.464); ovarian carcinoma (0.383); aortic stenosis (0.380); cancer (0.363); alcohol drinking (0.359)
- **Europe PMC papers**: 2065
- **Why important**: SMC2 provides the principal bridge from replication-associated proteins to chromosome architecture. It connects in STRING to MCM4, MCM6, and SMC4 and contributes to the globally significant single-stranded-DNA-binding and nuclear-chromosome terms (GO:MF single-stranded DNA binding; q_global = 0.00114)(GO:CC nuclear chromosome; q_global = 0.0123), as well as ATP-dependent activity (GO:MF ATP hydrolysis activity; q_global = 0.0324)(GO:MF ATP-dependent activity; q_global = 0.0431). hu.MAP supports SMC2-SMC4 condensin complexes (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_14663.1). Its established function includes mitotic chromosome condensation, chromosome organization, and chromosome segregation, while HPA links it to lymphoid tissue, spermatocytes, and hematopoietic progenitors. It also has disease associations involving cancer and aortic stenosis.
- **Conclusion**: Established evidence supports SMC2 as the chromosome-organization arm of the module and strengthens the interpretation that the module reflects active cell division or genome maintenance. Whether SMC2 is mechanistically coordinated with the MCM subnetwork in these tissues is a hypothesis rather than a demonstrated causal relationship.

#### UPF1

- **Related proteins** (co-abundance neighbors): PFAS (0.87), GMPS (0.82); STRING partners: MOV10 (0.912)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_06975.1
- **Function (MyGene.info)**: UPF1 RNA helicase and ATPase. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons.…
- **Diseases (Open Targets)**: Intellectual disability (0.437); Global developmental delay (0.426); High anterior hairline (0.425); Frontal bossing (0.425); Hypertelorism (0.425)
- **Europe PMC papers**: 4252
- **Why important**: UPF1 is a highly studied RNA helicase and ATPase involved in nonsense-mediated decay, mRNA export, and RNA surveillance, with established links to DNA replication and repair. It contributes to multiple primary helicase, ATP-dependent, DNA-replication, and repair terms (GO:BP nuclear DNA replication; q_global = 0.000977)(GO:BP cell cycle DNA replication; q_global = 0.00189)(GO:MF double-stranded DNA helicase activity; q_global = 0.00782)(GO:MF isomerase activity; q_global = 0.0115)(8 globally significant GO/KEGG terms, q_global 0.0154–0.0431; see the table). In the module it links to GMPS and PFAS, while STRING and hu.MAP support its relationship with MOV10 (hu.MAP huMAP3_06975.1). Its broad HPA profile contrasts with the lineage-enriched MCM genes, suggesting a more general cellular maintenance role. It has extensive literature and associations with intellectual disability and developmental phenotypes.
- **Conclusion**: Established evidence supports UPF1 as a multifunctional RNA-quality-control and genome-maintenance factor that may broaden the module beyond replication alone. Its inclusion does not prove that RNA surveillance drives the tissue-shared signal; that proposed coordination is hypothesis-level.

## Module 7

**Tissue pair**: circulatory_system and testis  
**Genes (27)**: AHNAK, ANXA6, AP3D1, ARFGEF1, CCAR1, CDK5RAP3, COG6, CORO7, GGA1, GIT1, DGLUCY, GMPPB, GMPR, GNAO1, CAST, EIF4G3, LMNB2, MAP1S, MVP, NECTIN2, PDCD4, PLEC, PPP1R21, PTPN23, SAMHD1, SUN2, USP5

### Function

The module does not support a globally significant GO or KEGG functional assignment: no GO/KEGG term passed global correction, and there are no supplementary STRING enrichment terms. Its structure instead suggests a heterogeneous intracellular organization and trafficking module. The genes include Golgi and endosomal trafficking factors, vesicle and membrane regulators, cytoskeletal scaffolds, nuclear-envelope components, translation and nucleotide-metabolism factors, and cell-adhesion proteins. The strongest biological interpretation is therefore coordinated cellular architecture, membrane trafficking, and compartmental organization rather than a narrowly defined pathway. The shared circulatory_system–testis signal may reflect common cellular programs present in both tissues, but the evidence does not establish a tissue-specific mechanism.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It is also not strongly blood-cell enriched. Most genes have low immune-cell specificity, while only a minority are immune-cell enhanced and the listed enhanced blood-cell types are neutrophils, basophils, and eosinophils. Most genes have low tissue specificity, with a smaller group showing tissue enhancement in brain, tongue, skeletal muscle, bone marrow, pancreas, or testis. Cell-type enhancement is widespread and includes epithelial, neural, muscle, reproductive, and immune-related cell types. Protein detection in testis is reported for nearly all module genes, whereas circulatory-system protein detection has no matching HPA tissue. This pattern is more consistent with shared cellular composition or broadly reused intracellular programs than with a circulating secretome or a blood-cell signature. The testis signal may also reflect the strong representation of testis-detected proteins and reproductive cell types in the available HPA evidence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The network has very limited support from established interaction resources. STRING identifies only the AHNAK–PLEC relationship at the stated confidence threshold. This supports a possible structural or membrane-cytoskeletal connection, but it does not validate the whole co-abundance module. hu.MAP identifies (hu.MAP huMAP3_09950.1), containing GGA1 and ARFGEF1 from this module together with other complex members outside the module. This provides limited support for a Golgi and vesicle-trafficking substructure. The absence of additional STRING or hu.MAP relationships means that most co-abundance edges are not already represented as high-confidence physical interactions or shared complex membership. Thus, the module is primarily an expression or co-abundance association, not a demonstrated protein complex.

**STRING interactions (score >= 0.7)**: 1 of 351 gene pairs: AHNAK–PLEC (0.73)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09950.1 (GGA1, ARFGEF1; 2/14)

### Novelty

The module should not be called a newly discovered molecular complex or pathway. Its lack of globally significant GO/KEGG enrichment, absence of STRING functional enrichment, sparse STRING connectivity, and limited hu.MAP representation make a strong novelty claim unjustified. It may still represent a novel tissue-pair co-abundance pattern, because co-abundance relationships can arise from shared cell states, coordinated regulation, or sample composition without appearing in interaction databases. The most defensible conclusion is that the tissue-pair association is potentially interesting but mechanistically unvalidated. Independent replication, cell-composition adjustment, and experimental testing would be needed before describing it as a new biological mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated maintenance of specialized cell architecture and intracellular trafficking in cells represented in both circulatory_system and testis. A possible axis is Golgi and endosomal sorting through GGA1, ARFGEF1, AP3D1, PTPN23, CORO7, and COG6, coupled to cytoskeletal and membrane organization through NECTIN2, PLEC, AHNAK, MVP, and ANXA6. Nuclear-envelope and regulatory components such as SUN2, LMNB2, PDCD4, and SAMHD1 could connect this structural state to nuclear organization, stress, or cell-cycle-related regulation. This is a hypothesis based on the mixed annotations and co-abundance structure; the fact sheet does not demonstrate that these proteins act in one physical pathway or that the module has a common causal driver.

### Important genes

#### NECTIN2

- **Related proteins** (co-abundance neighbors): USP5 (0.86), AHNAK (0.84), PPP1R21 (0.84), MVP (0.83), MAP1S (0.83), CORO7 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nectin cell adhesion molecule 2. This gene encodes a single-pass type I membrane glycoprotein with two Ig-like C2-type domains and an Ig-like V-type domain. This protein is one of the plasma membrane components of adherens junctions. It also serves as an entry for certain mutant strains of herpes simplex virus and pseudorabies virus, and it is involved in cell to cell spreading of these viruses. Variations in this gene have been …
- **Diseases (Open Targets)**: Alzheimer disease (0.460); atrial fibrillation (0.415); dementia (0.341); metabolic syndrome (0.309); Lewy body dementia (0.261)
- **Europe PMC papers**: 1219
- **Why important**: NECTIN2 is the most connected gene in the module and links USP5, AHNAK, PPP1R21, MVP, MAP1S, and CORO7. Established evidence supports a single-pass membrane adhesion role, homophilic cell-cell adhesion, signal transduction, and spermatid development. Its vesicular localization and detection in testis make it a plausible interface between cell adhesion, membrane organization, and the reproductive tissue context. It also has substantial literature and reported associations involving immune signaling, viral entry, and neurological disease.
- **Conclusion**: Established: NECTIN2 is a membrane adhesion and signaling protein with a prominent position in this co-abundance network and testis detection. Hypothesis: it may organize a membrane-associated branch that couples adhesion or cell contact to intracellular trafficking in the shared module. The module does not establish that NECTIN2 controls the other genes.

#### AP3D1

- **Related proteins** (co-abundance neighbors): PTPN23 (0.86), CDK5RAP3 (0.84), DGLUCY (0.84), CCAR1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor related protein complex 3 subunit delta 1. The protein encoded by this gene is a subunit of the AP3 adaptor-like complex, which is not clathrin-associated, but is associated with the golgi region, as well as more peripheral structures. The AP-3 complex facilitates the budding of vesicles from the golgi membrane, and may be directly involved in trafficking to lysosomes. This subunit is implicated in intracellular biogenesis and trafficking …
- **Diseases (Open Targets)**: Hermansky-Pudlak syndrome 10 (0.584); Hermansky-Pudlak syndrome 2 (0.455); Hermansky-Pudlak syndrome (0.432); Alzheimer disease (0.421); lysosomal storage disease (0.417)
- **Europe PMC papers**: 637
- **Why important**: AP3D1 is embedded in a trafficking-associated neighborhood with PTPN23, CDK5RAP3, DGLUCY, and CCAR1. Established evidence identifies it as a subunit of the AP-3 adaptor-like complex involved in Golgi budding and trafficking toward lysosomes, with possible roles in pigment granules, platelet dense granules, and neurotransmitter vesicles. Its disease associations include Hermansky-Pudlak syndrome and lysosomal storage disease, making it a biologically informative trafficking gene despite its intermediate network position.
- **Conclusion**: Established: AP3D1 participates in intracellular vesicle and lysosomal trafficking. Hypothesis: it may provide a trafficking backbone for part of the module and help explain co-abundance with endosomal, Golgi, and cytoskeletal genes. No direct module-wide physical interaction is demonstrated.

#### GGA1

- **Related proteins** (co-abundance neighbors): COG6 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_09950.1
- **Function (MyGene.info)**: golgi associated, gamma adaptin ear containing, ARF binding protein 1. This gene encodes a member of the Golgi-localized, gamma adaptin ear-containing, ARF-binding (GGA) protein family. Members of this family are ubiquitous coat proteins that regulate the trafficking of proteins between the trans-Golgi network and the lysosome. These proteins share an amino-terminal VHS domain which mediates sorting of the mannose 6-phosphate receptors at the trans-Golgi network. The…
- **Diseases (Open Targets)**: crush injury (0.057); nonsyndromic genetic hearing loss (0.036); Alzheimer disease (0.016); neoplasm (0.016); neuroblastoma (0.013)
- **Europe PMC papers**: 1079
- **Why important**: GGA1 is testis-enhanced, localized to the Golgi and vesicles, and annotated for intracellular protein sorting, Golgi-to-plasma-membrane transport, and endosome-to-Golgi transport. It is also one of the two module members in the hu.MAP complex represented by (hu.MAP huMAP3_09950.1), together with ARFGEF1. Although its direct co-abundance connectivity is limited, its annotation and complex membership give it high interpretive value for the trafficking theme. It has a substantial literature base and reported links to hearing loss, neuroblastoma, and Alzheimer disease.
- **Conclusion**: Established: GGA1 is a Golgi sorting factor and has limited complex-level support through (hu.MAP huMAP3_09950.1). Hypothesis: it may mark a reproductive-cell or testis-associated vesicle-sorting program within the module. The evidence does not show that the full module is a GGA1-containing complex.

#### PLEC

- **Related proteins** (co-abundance neighbors): MVP (0.84), GMPR (0.81); STRING partners: AHNAK (0.73)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plectin. Plectin is a prominent member of an important family of structurally and in part functionally related proteins, termed plakins or cytolinkers, that are capable of interlinking different elements of the cytoskeleton. Plakins, with their multi-domain structure and enormous size, not only play crucial roles in maintaining cell and tissue integrity and orchestrating dynamic changes in cytoarchitecture…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 5B, with muscular dystrophy (0.796); epidermolysis bullosa simplex 5A, Ogna type (0.775); autosomal recessive limb-girdle muscular dystrophy type 2Q (0.768); epidermolysis bullosa simplex 5C, with pyloric atresia (0.755); epidermolysis bullosa simplex with nail dystrophy (0.695)
- **Europe PMC papers**: 2578
- **Why important**: PLEC provides a structural counterpoint to the trafficking genes. It is a large cytoskeletal crosslinker and scaffold involved in cell shape, tissue integrity, and cytoskeletal organization. It connects to MVP and GMPR in the co-abundance network, and STRING independently supports the AHNAK–PLEC relationship. PLEC is skeletal-muscle enhanced, detected in testis, and strongly associated in the literature with epidermolysis bullosa and muscular dystrophy.
- **Conclusion**: Established: PLEC is a cytoskeletal scaffold with a supported AHNAK interaction and relevant structural disease associations. Hypothesis: PLEC may connect membrane trafficking or vesicle-associated proteins to the cytoskeleton in the shared module. This structural interpretation remains inferential because most module edges are not established physical interactions.

#### GMPR

- **Related proteins** (co-abundance neighbors): GNAO1 (0.97), GIT1 (0.84), EIF4G3 (0.83), ARFGEF1 (0.83), PLEC (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: guanosine monophosphate reductase. This gene encodes an enzyme that catalyzes the irreversible and NADPH-dependent reductive deamination of GMP to IMP. The protein also functions in the re-utilization of free intracellular bases and purine nucleosides.[provided by RefSeq, Oct 2009].
- **Diseases (Open Targets)**: chronic kidney disease (0.445); hypertrophic cardiomyopathy (0.333); Alzheimer disease (0.280); Abnormal blistering of the skin (0.273); disorder of appendix (0.258)
- **Europe PMC papers**: 740
- **Why important**: GMPR is a high-connectivity connector linking GNAO1, GIT1, EIF4G3, ARFGEF1, and PLEC. Established evidence identifies it as an NADPH-dependent enzyme in GMP-to-IMP conversion and purine recycling. Its cell-type annotations include differentiating spermatogonia, erythrocyte progenitors, megakaryocytes, and melanocytes, while its tissue annotation includes skeletal muscle and tongue. Its disease associations include chronic kidney disease and hypertrophic cardiomyopathy, and it has a substantial literature base.
- **Conclusion**: Established: GMPR is a purine-metabolism enzyme with broad cellular and disease relevance and a connector position between trafficking, cytoskeletal, signaling, and translation-related genes. Hypothesis: its co-abundance may reflect metabolic support for cells undergoing structural remodeling or differentiation. The fact sheet does not demonstrate a direct biochemical link between GMPR activity and the other module components.

## Module 8

**Tissue pair**: circulatory_system and testis  
**Genes (20)**: AIMP2, ANKRD28, ARMC8, SIRAL1, SHMT1, L2HGDH, LANCL2, MYL6B, NCK2, NFS1, C17orf75, NNT, OXSM, PPM1A, PTGR2, RAB28, TBL2, THNSL1, TM9SF4, TTC21B

### Function

No GO or KEGG term passed global correction, so no pathway-level enrichment can be claimed from the primary analysis. The network nevertheless contains genes involved in ciliary transport, intracellular trafficking, mitochondrial metabolism, lipid and prostaglandin metabolism, redox control, phosphorylation, and cytoskeletal or contractile functions. TTC21B is the clearest network hub and has an established role in ciliary retrograde transport. The module is therefore best interpreted as a mixed cellular-state signal rather than a single established pathway, with possible contributions from cilium biology, germ-cell differentiation, mitochondrial activity, metabolism, and intracellular transport.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly intracellular. It is not strongly blood-cell biased because most genes have low immune-cell specificity, although some show enhancement in basophils, plasmacytoid dendritic cells, platelets, or related populations. HPA shows low or broad tissue specificity for many genes, with additional enhancement in skeletal muscle, kidney, liver, tongue, and bone marrow. The strongest cell-level pattern is reproductive, with several genes enhanced in late primary spermatocytes, early spermatids, or late spermatids. The shared signal may therefore reflect common cellular programs or cell composition, especially germ-cell-associated, ciliary, metabolic, and contractile states, rather than circulating proteins.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No qualifying STRING interactions were identified among the module genes, and no hu.MAP complex contained multiple module members. The co-abundance edges are therefore not supported by high-confidence known physical interactions or by a recognized multiprotein complex. This does not exclude shared regulation, organelle-state effects, or cell-composition effects, but the module should not be described as an established physical complex or interaction network.

**STRING interactions (score >= 0.7)**: 0 of 190 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel co-abundance association, but it is not sufficient evidence for a newly discovered molecular pathway. The particular grouping lacks high-confidence STRING links, lacks a shared hu.MAP complex, and lacks globally significant GO or KEGG enrichment. However, absence from these resources does not prove novelty because database coverage, tissue context, cell composition, and detection thresholds can obscure real relationships. The appropriate conclusion is that this is a previously unvalidated candidate module requiring independent replication and targeted testing.

**Hypothesis.** Hypothesis: the module represents a shared cellular-state program combining ciliary or intracellular trafficking activity with mitochondrial and biosynthetic capacity during testicular germ-cell differentiation, with a related state detectable in circulatory-system samples through shared cell populations or systemic physiology. TTC21B may anchor the ciliary or transport component, while OXSM, NNT, SHMT1, and PTGR2 may reflect coordinated lipid, redox, one-carbon, and prostaglandin metabolism. This remains a hypothesis because the enrichment analysis is globally negative and neither STRING nor hu.MAP supports a shared physical complex.

### Important genes

#### TTC21B

- **Related proteins** (co-abundance neighbors): OXSM (0.86), LANCL2 (0.85), MYL6B (0.85), SIRAL1 (0.83), C17orf75 (0.83), ARMC8 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Primary cilium, Centriolar satellite, Basal body; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tetratricopeptide repeat domain 21B. This gene encodes a member of TTC21 family, containing several tetratricopeptide repeat (TPR) domains. This protein is localized to the cilium axoneme, and may play a role in retrograde intraflagellar transport in cilia. Mutations in this gene are associated with various ciliopathies, nephronophthisis 12, and asphyxiating thoracic dystrophy 4. [provided by RefSeq, Oct 2011].
- **Diseases (Open Targets)**: nephronophthisis (0.828); Jeune syndrome (0.754); nephronophthisis 2 (0.517); inherited retinal dystrophy (0.499); short-rib thoracic dysplasia 6 with or without polydactyly (0.454)
- **Europe PMC papers**: 628
- **Why important**: TTC21B is the central network hub, connecting the largest local set of module genes. HPA localizes it to the primary cilium, centriolar satellite, and basal body, and shows enhancement in several ciliated cell populations. Its established role in intraciliary retrograde transport and its associations with ciliopathies and nephronophthisis provide strong functional and disease support, alongside substantial literature.
- **Conclusion**: Established evidence supports TTC21B as the principal ciliary and transport-related anchor of the module and links it to ciliopathies. It is plausible but unproven that TTC21B helps define the shared tissue-pair state. The network does not establish direct physical interactions with its module neighbors.

#### PTGR2

- **Related proteins** (co-abundance neighbors): OXSM (0.87), PPM1A (0.85), L2HGDH (0.84), NFS1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prostaglandin reductase 2. This gene encodes an enzyme involved in the metabolism of prostaglandins. The encoded protein catalyzes the NADPH-dependent conversion of 15-keto-prostaglandin E2 to 15-keto-13,14-dihydro-prostaglandin E2. This protein may also be involved in regulating activation of the peroxisome proliferator-activated receptor. Alternative splicing results in multiple transcript variants. [provided by RefSeq, A…
- **Diseases (Open Targets)**: autoimmune disorder of central nervous system (0.274); retinitis pigmentosa (0.077); cone-rod dystrophy (0.076); nonpapillary renal cell carcinoma (0.074); Leber congenital amaurosis (0.068)
- **Europe PMC papers**: 238
- **Why important**: PTGR2 is relatively connected and links the hub region to PPM1A, L2HGDH, NFS1, and OXSM. It encodes a prostaglandin-metabolizing enzyme and may regulate peroxisome-proliferator-activated receptor activity, providing a plausible connection between lipid mediators, metabolism, and cellular state. HPA reports testis detection and enhancement in brain-associated cell types and basophils.
- **Conclusion**: Established evidence supports PTGR2 as a prostaglandin-metabolism enzyme. Its placement beside mitochondrial and signaling genes makes coordinated metabolic regulation plausible, but the module does not show that PTGR2 drives the co-abundance pattern or mechanistically connects the tissues.

#### OXSM

- **Related proteins** (co-abundance neighbors): PTGR2 (0.87), TTC21B (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3-oxoacyl-ACP synthase, mitochondrial. This gene encodes a beta-ketoacyl synthetase. The encoded enzyme is required for elongation of fatty acid chains in the mitochondria. Alternatively spliced transcript variants have been described.[provided by RefSeq, Feb 2009].
- **Diseases (Open Targets)**: congenital disorder of deglycosylation (0.522); hereditary disease (0.408); congenital disorder of deglycosylation 1 (0.395); hypercholesterolemia, familial, 1 (0.333); neurodegenerative disease (0.287)
- **Europe PMC papers**: 443
- **Why important**: OXSM bridges TTC21B and PTGR2 and encodes a mitochondrial beta-ketoacyl synthase required for fatty-acid-chain elongation. HPA places it in mitochondria and cytosol and reports a pattern spanning cardiomyocytes and multiple spermatogenic populations. This gives it relevance to the tissue pair and to a possible coupling of lipid metabolism with cell differentiation.
- **Conclusion**: Established evidence supports OXSM as a mitochondrial enzyme involved in fatty-acid biosynthesis. A coordinated mitochondrial lipid-metabolic component is plausible from its position and annotations, but a direct role in the shared tissue-pair program remains hypothetical.

#### NNT

- **Related proteins** (co-abundance neighbors): PPM1A (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nicotinamide nucleotide transhydrogenase. This gene encodes an integral protein of the inner mitochondrial membrane. The enzyme couples hydride transfer between NAD(H) and NADP(+) to proton translocation across the inner mitochondrial membrane. Under most physiological conditions, the enzyme uses energy from the mitochondrial proton gradient to produce high concentrations of NADPH. The resulting NADPH is used for biosynthesis and in free …
- **Diseases (Open Targets)**: familial glucocorticoid deficiency (0.638); neurodegenerative disease (0.497); hereditary disease (0.453); atypical hemolytic-uremic syndrome with DGKE deficiency (0.416); Abnormality of the skeletal system (0.396)
- **Europe PMC papers**: 6111
- **Why important**: NNT represents mitochondrial redox control within a module that also contains metabolic and stress-related genes. It produces NADPH through inner-mitochondrial-membrane hydride transfer and is annotated for reactive oxygen species metabolism. HPA shows enhancement in skeletal muscle and several metabolically active cell types, with testis protein detection. NNT also has extensive literature and disease-association support.
- **Conclusion**: Established evidence supports NNT as a mitochondrial source of reducing power relevant to biosynthesis and oxidative-stress control. It could help explain the module's occurrence across metabolically distinct tissues, but the co-abundance data do not establish redox regulation as the primary module function.

#### SHMT1

- **Related proteins** (co-abundance neighbors): RAB28 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine hydroxymethyltransferase 1. This gene encodes the cytosolic form of serine hydroxymethyltransferase, a pyridoxal phosphate-containing enzyme that catalyzes the reversible conversion of serine and tetrahydrofolate to glycine and 5,10-methylene tetrahydrofolate. This reaction provides one-carbon units for synthesis of methionine, thymidylate, and purines in the cytoplasm. This gene is located within the Smith-Magenis syndrome …
- **Diseases (Open Targets)**: neurodegenerative disease (0.458); Parkinson disease (0.351); Alzheimer disease (0.350); lysosomal storage disease (0.346); preeclampsia (0.314)
- **Europe PMC papers**: 2070
- **Why important**: SHMT1 provides a cytosolic one-carbon and amino-acid metabolic function and connects to RAB28. It supplies one-carbon units for nucleotide and related biosynthetic processes. HPA reports enhancement in kidney and liver, proximal tubule cells, and testis detection. Its established function, disease associations, and substantial literature make it an informative metabolic representative despite its limited network connectivity.
- **Conclusion**: Established evidence supports SHMT1 as a cytosolic serine and glycine metabolism enzyme contributing to nucleotide synthesis. Its presence is consistent with biosynthetic demands during germ-cell development or other metabolically active states, but that interpretation is hypothetical and is not demonstrated by global enrichment.

## Module 9

**Tissue pair**: circulatory_system and testis  
**Genes (8)**: ASPH, TRIP10, CNTN1, F13A1, MYO1C, NEO1, PLXNB2, SOD3

### Function

The module is most consistent with a mixed cell-surface, adhesion, migration, cytoskeletal, and extracellular-protective program rather than a single established biochemical pathway. Its topology links F13A1 to SOD3, NEO1, and TRIP10, while PLXNB2 connects to CNTN1, ASPH, and MYO1C and also links through MYO1C to TRIP10. The supplementary STRING terms support an immunoglobulin-like-fold component involving F13A1, NEO1, PLXNB2, and CNTN1 (STRING InterPro Immunoglobulin-like fold; within-query FDR = 0.0286), and a cell-periphery component involving TRIP10, NEO1, PLXNB2, ASPH, SOD3, CNTN1, and MYO1C (STRING COMPARTMENTS Cell periphery; within-query FDR = 0.0412). However, no GO/KEGG term passed global correction, so these annotations do not establish significant pathway enrichment. Established functions represented in the genes include coagulation and fibrin cross-linking through F13A1, extracellular antioxidant activity through SOD3, cell adhesion and axon guidance through CNTN1 and NEO1, semaphorin-related receptor signaling and cell migration through PLXNB2, and actin-based trafficking or endocytosis through MYO1C and TRIP10.

**Cell composition.** This is not a module dominated by classical plasma or secreted proteins. F13A1 and SOD3 are explicitly secreted to blood, while CNTN1 has an intracellular and membrane secretome annotation; the overall module therefore contains a mixture of extracellular, membrane, vesicular, and intracellular proteins. HPA shows protein detection for every module gene in testis, but the circulatory-system comparison has no matching HPA tissue protein result. Tissue and single-cell annotations are heterogeneous, including adipose tissue, skeletal muscle, brain, placenta, blood vessel, adipocytes, glial cells, epithelial cells, and vascular or placental cell types. Several genes have immune-cell enrichment or enhancement, especially in monocyte, dendritic-cell, plasmacytoid-dendritic-cell, basophil, and macrophage-related contexts, while other genes are not detected in immune cells. Thus, the shared signal could reflect common vascular, stromal, epithelial, immune, or other shared cell populations rather than a dedicated circulatory-system–testis pathway. The broad HPA distribution also argues against treating the module as a testis-specific program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair in the module reaches the supplied high-confidence STRING interaction threshold, and no hu.MAP complex contains multiple module members. Therefore, the co-abundance network is not corroborated as a known physical interaction network or a known multiprotein complex by these resources. The supplementary STRING fold and cell-periphery signals (STRING InterPro Immunoglobulin-like fold; within-query FDR = 0.0286) (STRING COMPARTMENTS Cell periphery; within-query FDR = 0.0412) are compatible with shared localization or domain architecture, but they do not demonstrate direct interaction. The network may therefore capture coordinated expression across related cell states, indirect signaling relationships, or sample-composition effects rather than a pre-existing molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: InterPro Immunoglobulin-like fold (FDR = 0.0286, 4 genes); COMPARTMENTS Cell periphery (FDR = 0.0412, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unrecognized cross-tissue co-abundance pattern, because its exact gene combination is not represented by a high-confidence STRING interaction set or a hu.MAP complex. Nevertheless, that absence alone does not prove novelty: the genes have established individual functions, several belong to well-studied adhesion, signaling, cytoskeletal, coagulation, or antioxidant biology, and the HPA profiles indicate multiple plausible shared cell sources. The defensible conclusion is that the cross-tissue co-abundance association is potentially novel, but its biological novelty and independence from cell-composition effects require validation in independent cohorts, cell-resolved data, and targeted molecular experiments.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of proteins expressed by vascular, stromal, epithelial, immune, or other shared cell populations present in circulatory-system and testis samples. Within such cells, PLXNB2, NEO1, and CNTN1 could organize adhesion or migration-related signaling; MYO1C and TRIP10 could connect receptor or membrane events to actin remodeling, vesicle traffic, and endocytosis; SOD3 could provide extracellular redox protection; and F13A1 could contribute coagulation-related or extracellular matrix-associated stabilization. This is a mechanistic model, not an established pathway, and the absence of STRING or hu.MAP support means that the proposed links may be indirect.

### Important genes

#### F13A1

- **Related proteins** (co-abundance neighbors): SOD3 (0.90), NEO1 (0.81), TRIP10 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coagulation factor XIII A chain. This gene encodes the coagulation factor XIII A subunit. Coagulation factor XIII is the last zymogen to become activated in the blood coagulation cascade. Plasma factor XIII is a heterotetramer composed of 2 A subunits and 2 B subunits. The A subunits have catalytic function, and the B subunits do not have enzymatic activity and may serve as plasma carrier molecules. Platelet factor XIII is compri…
- **Diseases (Open Targets)**: Factor XIII subunit A deficiency (0.808); factor XIII, A subunit, deficiency of (0.740); congenital factor XIII deficiency (0.527); thrombophilia due to thrombin defect (0.485); hemorrhage (0.463)
- **Europe PMC papers**: 2585
- **Why important**: F13A1 is among the most connected genes in the module and links the coagulation-related extracellular branch to SOD3, NEO1, and TRIP10. It encodes the catalytic A subunit of coagulation factor XIII and is associated with blood coagulation, fibrin-clot formation, and factor XIII deficiency. HPA identifies it as secreted to blood and associates it with Hofbauer cells, macrophages, megakaryocytes, platelets, classical monocytes, and myeloid dendritic cells. It also contributes to the supplementary immunoglobulin-like-fold signal (STRING InterPro Immunoglobulin-like fold; within-query FDR = 0.0286) and has extensive literature coverage.
- **Conclusion**: Established evidence supports F13A1 as a coagulation and extracellular factor with plausible vascular and blood-cell origins. Its central position makes it an important marker of the module, but the data do not establish that it directly interacts with the other module proteins or that coagulation is the module's primary function.

#### PLXNB2

- **Related proteins** (co-abundance neighbors): CNTN1 (0.87), ASPH (0.83), MYO1C (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plexin B2. Members of the B class of plexins, such as PLXNB2 are transmembrane receptors that participate in axon guidance and cell migration in response to semaphorins (Perrot et al. (2002) [PubMed 12183458]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Intellectual disability (0.519); amelogenesis imperfecta (0.518); sensorineural hearing loss disorder (0.516); cutaneous melanoma (0.486); neurodegenerative disease (0.455)
- **Europe PMC papers**: 2109
- **Why important**: PLXNB2 is one of the most connected genes and forms the central branch containing CNTN1, ASPH, and MYO1C. It is a transmembrane plexin receptor involved in semaphorin-responsive axon guidance and cell migration, with annotations also covering receptor-mediated endocytosis, cell adhesion, and neuroblast proliferation. HPA shows broad tissue behavior, enhanced expression in several epithelial cell types, and enrichment across multiple monocyte and dendritic-cell populations. It contributes to both supplementary STRING signals (STRING InterPro Immunoglobulin-like fold; within-query FDR = 0.0286) (STRING COMPARTMENTS Cell periphery; within-query FDR = 0.0412) and has substantial disease-oriented and literature evidence.
- **Conclusion**: Established evidence supports PLXNB2 as a cell-surface signaling and adhesion receptor expressed across several cell contexts. Its network position makes it a strong candidate for organizing the membrane-associated branch, but a specific PLXNB2-centered mechanism in the shared tissues remains hypothetical.

#### SOD3

- **Related proteins** (co-abundance neighbors): F13A1 (0.90); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: superoxide dismutase 3. This gene encodes a member of the superoxide dismutase (SOD) protein family. SODs are antioxidant enzymes that catalyze the conversion of superoxide radicals into hydrogen peroxide and oxygen, which may protect the brain, lungs, and other tissues from oxidative stress. Proteolytic processing of the encoded protein results in the formation of two distinct homotetramers that differ in their ability …
- **Diseases (Open Targets)**: alcohol drinking (0.286); transient ischemic attack (0.262); urolithiasis (0.257); aortic atherosclerosis (0.252); malunion fracture (0.251)
- **Europe PMC papers**: 5713
- **Why important**: SOD3 is directly connected to F13A1 and is the clearest extracellular redox-protection component. It encodes a secreted antioxidant enzyme that removes superoxide and participates in superoxide, nitric-oxide, and inflammatory processes. HPA places it in blood-vessel and choroid-plexus tissue groups, detects it in several epithelial, placental, stromal, and reproductive cell contexts, and reports it as not detected in immune cells. Its vascular relevance and disease associations make it informative despite its peripheral network position.
- **Conclusion**: Established evidence supports SOD3 as an extracellular antioxidant associated with vascular and tissue-protective biology. Its connection to F13A1 may indicate a shared extracellular or vascular context, but the network does not demonstrate a direct functional partnership.

#### NEO1

- **Related proteins** (co-abundance neighbors): F13A1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm, Plasma membrane; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neogenin 1. This gene encodes a cell surface protein that is a member of the immunoglobulin superfamily. The encoded protein consists of four N-terminal immunoglobulin-like domains, six fibronectin type III domains, a transmembrane domain and a C-terminal internal domain that shares homology with the tumor suppressor candidate gene DCC. This protein may be involved in cell growth and differentiation and in ce…
- **Diseases (Open Targets)**: dentures (0.456); dental caries (0.410); Varicose veins (0.344); atrial fibrillation (0.342); self-injurious ideation (0.277)
- **Europe PMC papers**: 1645
- **Why important**: NEO1 connects directly to F13A1 and contributes to both supplementary STRING terms (STRING InterPro Immunoglobulin-like fold; within-query FDR = 0.0286) (STRING COMPARTMENTS Cell periphery; within-query FDR = 0.0412). It is a cell-surface immunoglobulin-superfamily protein with fibronectin domains, involved in cell adhesion, axon guidance, neuron migration, and multicellular iron homeostasis. HPA shows expression in glial and myonuclear cell types and no detection in immune cells. Its domain architecture, membrane localization, network bridge, and associations with vascular and atrial-fibrillation-related disease make it a useful candidate for linking extracellular and cell-adhesion biology.
- **Conclusion**: Established evidence supports NEO1 as a multifunctional adhesion and guidance receptor. Its bridge to F13A1 is compatible with coordinated extracellular or cell-surface biology, but the proposed cross-talk with coagulation or testis biology remains unproven.

#### TRIP10

- **Related proteins** (co-abundance neighbors): MYO1C (0.81), F13A1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thyroid hormone receptor interactor 10. Enables identical protein binding activity. Predicted to be involved in actin cytoskeleton organization; endocytosis; and signal transduction. Located in nucleoplasm. Biomarker of Huntington's disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); auditory system disorder (0.219); neoplasm (0.105); colorectal carcinoma (0.084); nasopharyngeal carcinoma (0.076)
- **Europe PMC papers**: 516
- **Why important**: TRIP10 links the F13A1 branch to the PLXNB2-associated MYO1C branch and is annotated for actin-cytoskeleton organization, endocytosis, signal transduction, and plasma-membrane tubulation. HPA associates it with skeletal muscle, esophageal apical cells, and plasmacytoid dendritic cells, and places it in vesicles. Its position suggests a possible structural or trafficking role that could connect membrane receptors with cytoskeletal remodeling.
- **Conclusion**: Established evidence supports TRIP10 as a cytoskeletal and membrane-trafficking adaptor-like component. Its network position makes it a plausible coordinator of the module's membrane-associated behavior, but any physical or causal connection to F13A1, PLXNB2, or MYO1C is a hypothesis rather than a demonstrated interaction.

## Module 10

**Tissue pair**: circulatory_system and testis  
**Genes (9)**: CLTC, RNASET2, SEC63, SORT1, CCT5, CCT3, CCT7, CCT8, TNS1

### Function

The strongest interpretation is an ATP-dependent protein-folding and proteostasis module centered on the CCT/TRiC chaperonin. The globally corrected enrichment is driven by CCT3, CCT5, CCT7, and CCT8 across protein-folding, chaperonin-complex, protein-stabilization, and nuclear or Cajal-body localization terms (8 globally significant GO/KEGG terms, q_global 4.69e-06–1.69e-05; see the table), (GO:CC protein folding chaperone complex; q_global = 0.00046), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.00138), (GO:MF protein folding chaperone; q_global = 0.0061), (GO:MF unfolded protein binding; q_global = 0.0182), (GO:BP protein stabilization; q_global = 0.0243). The same CCT quartet is associated with telomerase-RNA localization and telomere maintenance (20 globally significant GO/KEGG terms, q_global 4.69e-06–0.00046; see the table), (GO:BP regulation of telomere maintenance; q_global = 0.000632), (GO:BP telomere maintenance; q_global = 0.00316), (GO:BP telomere organization; q_global = 0.00444). These annotations support a role in folding and stabilizing proteins that participate in nuclear RNA, DNA, and telomere processes, but they do not establish that this module directly regulates telomerase in either tissue. The fertilization and sperm-recognition terms (GO:BP binding of sperm to zona pellucida; q_global = 0.000136), (GO:BP sperm-egg recognition; q_global = 0.000217), (GO:BP cell-cell recognition; q_global = 0.000632), (GO:BP cell recognition; q_global = 0.0026), (GO:BP single fertilization; q_global = 0.00444), (GO:BP fertilization; q_global = 0.0104) may reflect the testis context or annotation overlap with the CCT genes; they are not sufficient by themselves to define a reproductive-specific mechanism. CLTC contributes to the microtubule term (GO:CC microtubule; q_global = 0.0135), while the remaining genes lack globally corrected GO or KEGG assignments.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: only RNASET2 is annotated as secreted to blood, and the other genes are intracellular or membrane-associated. The module is therefore more consistent with a mixture of broadly expressed housekeeping or structural functions and cell-type-associated signals than with a circulating secretome. HPA reports low tissue specificity for most genes, with testis protein detection for every module member. At the single-cell level, several genes are enhanced in neutrophils, vascular smooth muscle cells, or spermatogenic cells, and HPA also shows monocyte-associated blood-cell patterns. Thus, the shared circulatory-system and testis signal could partly reflect common cell types, vascular or stromal components, or blood-cell representation in tissue samples rather than a tissue-independent biological program. TNS1 is the clearest tissue-associated exception, with blood-vessel enhancement and enrichment in vascular, pericyte, Leydig, and peritubular myoid cell contexts.

**GO/KEGG enrichment**: 43 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP protein localization to nuclear body | 4.69e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 4.69e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 4.69e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 4.69e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 4.69e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 4.69e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 4.69e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:CC chaperonin-containing T-complex | 1.69e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomere maintenance via telomerase | 1.69e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 1.69e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to Cajal body | 1.69e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 1.69e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 1.69e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 1.69e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomere maintenance via telomere lengthening | 4.06e-05 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING independently supports a well-established CCT subnetwork: CCT3, CCT5, CCT7, and CCT8 form a densely connected high-confidence clique, and STRING supplementary annotations identify the TCP-1 chaperonin family, the chaperonin-containing T-complex, actin folding, biosynthetic target association, and cellular proteostasis (13 supplementary STRING terms; within-query FDR 1.04e-05–8.41e-05). The STRING sperm-recognition and telomerase annotations (STRING Process Binding of sperm to zona pellucida; within-query FDR = 0.00011), (STRING Process Positive regulation of telomere maintenance via telomerase; within-query FDR = 0.00011) agree with the GO results but remain supplementary rather than globally corrected evidence. hu.MAP identifies the same CCT quartet in several complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) and a closely related complex containing three of these genes (hu.MAP huMAP3_01951.1). These complexes include additional CCT subunits and associated folding, cytoskeletal, and regulatory proteins, showing that the core relationships are already known physical or complex-level biology. TNS1 connects the CCT component to SEC63, RNASET2, CLTC, and SORT1 in the co-abundance graph, but STRING and hu.MAP provide no recorded relationships for those peripheral module genes. Accordingly, the network is strongly anchored by a known chaperonin complex, while the links joining that complex to the other module members are less independently supported.

**STRING interactions (score >= 0.7)**: 6 of 36 gene pairs: CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam TCP-1/cpn60 chaperonin family (FDR = 1.04e-05, 4 genes); Component Chaperonin-containing T-complex (FDR = 2.9e-05, 4 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 3.04e-05, 4 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 4.62e-05, 4 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 4.62e-05, 4 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 4.62e-05, 4 genes); InterPro GroEL-like apical domain superfamily (FDR = 4.62e-05, 4 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 4.62e-05, 4 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 4.62e-05, 4 genes); RCTM Folding of actin by CCT/TriC (FDR = 7.17e-05, 4 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis (FDR = 8.34e-05, 4 genes); RCTM Association of TriC/CCT with target proteins during biosynthesis (FDR = 8.41e-05, 4 genes); RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding (FDR = 8.41e-05, 4 genes); Process Binding of sperm to zona pellucida (FDR = 0.00011, 4 genes); Process Positive regulation of telomere maintenance via telomerase (FDR = 0.00011, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8)

### Novelty

The module should not be presented as a discovery of a new CCT complex or a new CCT interaction: the core CCT3–CCT5–CCT7–CCT8 relationships are already supported by STRING, hu.MAP, and established gene annotations. A potentially novel aspect is the co-abundance coupling of this known chaperonin core with TNS1, SEC63, RNASET2, CLTC, and SORT1 across circulatory-system and testis samples. However, absence of those peripheral relationships from STRING or hu.MAP does not prove novelty, because database coverage, context dependence, tissue composition, and co-abundance are distinct from physical interaction evidence. The defensible conclusion is that this is a potentially novel tissue-pair co-abundance configuration built around a well-known proteostasis core, not a wholly new molecular complex.

**Hypothesis.** Hypothesis: the shared module reflects coordinated proteostasis and cytoskeletal or trafficking demand in vascular and testicular cell populations. The CCT quartet may maintain folding and stability of cytoskeletal or nuclear proteins, while TNS1 links focal-adhesion and actin-associated biology to this chaperone state. SEC63 could represent coupling to endoplasmic-reticulum protein targeting, CLTC and SORT1 could represent vesicle trafficking and endosomal routing, and RNASET2 could represent an extracellular or innate-immune component. In testis, the same program could support differentiating germ cells and their associated somatic cells; in circulatory-system samples, it could arise from vascular, stromal, or blood-cell populations. This is a mechanistic model generated from co-abundance and annotations, not evidence that these proteins form one physical pathway or that the CCT quartet directly controls telomerase.

### Important genes

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT8 (0.89), CCT7 (0.83), CCT3 (0.82); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is a central member of the module's known chaperonin core, connects directly to CCT3, CCT7, and CCT8, and appears in every hu.MAP complex listed for the module (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It participates in all globally corrected enrichment terms assigned to the CCT quartet, including chaperonin function, protein folding, telomerase-related localization, telomere maintenance, and protein stabilization (43 globally significant GO/KEGG terms, q_global 4.69e-06–0.0243; see the table). Its established disease associations include hereditary sensory and autonomic neuropathy with spastic paraplegia and neurodegenerative disease, and it has substantial literature support.
- **Conclusion**: Established: CCT5 is a CCT/TRiC folding-chaperone subunit and a core physical-complex marker. Established: its module association is strongly supported by GO, STRING, hu.MAP, and the network structure. Hypothesis: variation in CCT5 abundance may influence the capacity of vascular or testicular cells to maintain proteostasis during cytoskeletal or nuclear remodeling.

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT5 (0.82); STRING partners: CCT5 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is part of the high-confidence STRING CCT clique and is present in all listed hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It shares the complete set of globally corrected CCT-associated annotations (43 globally significant GO/KEGG terms, q_global 4.69e-06–0.0243; see the table), making it a strong contributor to the module's primary functional signal. Its documented functions include ATP-dependent folding of actin and tubulin, and its disease associations include neurodevelopmental, neurodegenerative, autoimmune, and cardiovascular conditions.
- **Conclusion**: Established: CCT3 is a core TRiC subunit with a direct known relationship to the other CCT genes in the module. Established: the enrichment evidence supports a broad folding and nuclear or telomere-associated interpretation. Hypothesis: CCT3 may help couple general proteostasis to cell-cycle or chromatin-related demands in the shared tissue context.

#### CCT7

- **Related proteins** (co-abundance neighbors): CCT5 (0.83), TNS1 (0.83), CCT8 (0.81); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is a core CCT component with direct STRING relationships to CCT3, CCT5, and CCT8 and membership in all hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It contributes to every globally corrected CCT-associated term (43 globally significant GO/KEGG terms, q_global 4.69e-06–0.0243; see the table). HPA places it in early and late spermatogenic cell contexts, while its disease associations include myocardial infarction, preeclampsia, neurodegenerative disease, and hepatocellular carcinoma. It also has substantial literature support.
- **Conclusion**: Established: CCT7 is a known chaperonin subunit and a major structural anchor of this module. Established: its testis cell-type associations are compatible with a germ-cell contribution, but do not prove a spermatogenesis-specific function. Hypothesis: CCT7 abundance may mark or support proteostatic requirements during spermatogenic differentiation and vascular-cell stress responses.

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT5 (0.89), CCT7 (0.81); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 completes the known CCT quartet, connects directly to CCT5 and CCT7 in the module and to CCT3 in STRING, and appears in the higher-confidence hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). It contributes to the globally corrected folding, nuclear-localization, telomerase-related, telomere, and protein-stabilization annotations (43 globally significant GO/KEGG terms, q_global 4.69e-06–0.0243; see the table). Its protein is detected in testis and localized to nucleoplasm and sperm-tail-associated compartments, while its disease associations include several cancers and neoplasm-related conditions.
- **Conclusion**: Established: CCT8 is a core TRiC subunit and a strong molecular explanation for the module's enrichment profile. Established: its localization and testis detection are compatible with roles in protein assembly in germ-cell-associated compartments. Hypothesis: CCT8 may help maintain the folding and transport of proteins needed for nuclear organization or sperm-cell structural maturation.

#### TNS1

- **Related proteins** (co-abundance neighbors): SEC63 (0.83), CCT7 (0.83), RNASET2 (0.82), CLTC (0.81), SORT1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Focal adhesion sites; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tensin 1. The protein encoded by this gene localizes to focal adhesions, regions of the plasma membrane where the cell attaches to the extracellular matrix. This protein crosslinks actin filaments and contains a Src homology 2 (SH2) domain, which is often found in molecules involved in signal transduction. This protein is a substrate of calpain II. Alternative splicing results in multiple transcript variant…
- **Diseases (Open Targets)**: coronary artery disorder (0.555); chronic obstructive pulmonary disease (0.550); myocardial infarction (0.513); aortic stenosis (0.462); breast cancer (0.443)
- **Europe PMC papers**: 1434
- **Why important**: TNS1 has the strongest network connectivity in the module and is the principal bridge between the CCT core and SEC63, RNASET2, CLTC, and SORT1. Its established function is focal-adhesion and actin-associated cell-matrix biology, with an SH2 domain and a role in fibroblast migration. HPA shows blood-vessel enhancement and cell contexts including pericytes, vascular cells, Leydig cells, and peritubular myoid cells. Its disease associations include coronary artery disorder, chronic obstructive pulmonary disease, myocardial infarction, aortic stenosis, and breast cancer, supported by substantial literature.
- **Conclusion**: Established: TNS1 is a focal-adhesion and cell-matrix protein and the most prominent network connector in this module. Established: its HPA pattern provides a plausible vascular and testicular somatic-cell source for the shared signal. Hypothesis: TNS1 may couple adhesion or cytoskeletal remodeling to the proteostasis demand represented by the CCT quartet, but this inferred coupling is not independently established by STRING or hu.MAP.

## Module 11

**Tissue pair**: circulatory_system and testis  
**Genes (6)**: COG1, HMGCL, KCTD12, MBOAT7, NAXD, RTCA

### Function

No GO/KEGG term passed global correction, and there was no supplementary STRING functional enrichment. The module therefore does not support a single statistically validated biological function. Its gene annotations instead suggest a loose combination of intracellular metabolic maintenance, RNA processing, Golgi organization, phospholipid remodeling, receptor-associated signaling, and ketone-body metabolism. The co-abundance structure is weakly organized around NAXD, which links to RTCA, KCTD12, and HMGCL, while RTCA links to COG1 and KCTD12 links to MBOAT7. This pattern is more consistent with a heterogeneous cellular program or shared abundance context than with a defined molecular complex or pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: the secretome annotation is absent for every member. Most genes have low tissue specificity, while the tissue-enhanced annotations point separately to adrenal gland and liver rather than to a common tissue program. Most genes have cell-type-enhanced annotations, including macrophage-lineage, endothelial, hepatocyte, esophageal, neuronal, and granulocyte contexts. Blood-cell specificity is generally low, although KCTD12 is immune-cell enhanced and MBOAT7 is group enriched in basophils, eosinophils, and neutrophils. Protein detection in testis is reported for most members, whereas the circulatory-system comparison lacks matching HPA tissue data. Thus, the shared module is unlikely to represent a secreted plasma program; it may partly reflect broadly expressed intracellular proteins, testis protein abundance, or variable shared cellular composition, with a possible contribution from myeloid or granulocyte-related signals.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair has a STRING interaction at the specified high-confidence cutoff, and no STRING functional enrichment was reported. No hu.MAP complex contains multiple module members. Consequently, the co-abundance edges are not corroborated as known physical interactions or as membership in a recognized multiprotein complex. The observed relationships should be interpreted as expression or abundance covariation rather than direct biochemical binding. Known functions of individual genes remain informative, but the module-level network does not currently establish a shared physical mechanism.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be an exploratory co-abundance pattern, but it cannot be called a new biological discovery from the present evidence. Its lack of STRING and hu.MAP support shows that the particular cross-tissue combination is not represented by the queried interaction resources, yet absence from those resources does not prove novelty. The absence of globally significant GO/KEGG enrichment, the lack of STRING enrichment, and the heterogeneous annotations argue for caution. A claim of novelty would require independent replication across cohorts or platforms, comparison with published co-expression modules, and testing whether the pattern persists after controlling for cell composition and tissue-specific abundance.

**Hypothesis.** Hypothesis: the shared circulatory-system and testis signal reflects coordinated abundance of broadly expressed intracellular proteins under common metabolic, RNA-processing, membrane-lipid, and organelle-maintenance conditions rather than a single pathway or complex. NAXD and HMGCL could mark linked metabolic state, while RTCA and COG1 could reflect RNA and Golgi-related cellular maintenance, and KCTD12 with MBOAT7 could reflect cell-state-dependent signaling and phospholipid remodeling. The apparent cross-tissue conservation may therefore arise from shared cellular stress, metabolic state, or cell-composition effects. This hypothesis requires validation by cell-type-adjusted analyses, independent datasets, and perturbation or biochemical experiments.

### Important genes

#### NAXD

- **Related proteins** (co-abundance neighbors): RTCA (0.84), KCTD12 (0.81), HMGCL (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NAD(P)HX dehydratase. Enables ATP-dependent NAD(P)H-hydrate dehydratase activity. Predicted to be involved in metabolite repair. Predicted to be located in cytosol; endoplasmic reticulum; and mitochondrion. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: NAD(P)HX dehydratase deficiency (0.747); encephalopathy, progressive, early-onset, with brain edema and/or leukoencephalopathy (0.554); mitochondrial disease (0.370); Combined oxidative phosphorylation defect type 27 (0.346); tympanic membrane perforation (0.277)
- **Europe PMC papers**: 167
- **Why important**: NAXD is the most connected apparent hub in the module and links the RTCA, KCTD12, and HMGCL branches. Its established annotation as NAD(P)HX dehydratase places it in metabolite repair and nicotinamide-nucleotide metabolism, with predicted cytosolic, endoplasmic-reticulum, and mitochondrial localization. It also has disease associations involving NAD(P)HX dehydratase deficiency and mitochondrial or neurological disease, supported by a substantial literature.
- **Conclusion**: Established evidence supports NAXD as a metabolite-repair enzyme and as the central network connector. It is an important candidate for explaining the module's metabolic component. It is not established that NAXD drives the cross-tissue module or directly interacts with its neighbors; that interpretation remains a hypothesis.

#### RTCA

- **Related proteins** (co-abundance neighbors): COG1 (0.87), NAXD (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA 3'-terminal phosphate cyclase. This gene encodes a member of the RNA 3'-phosphate cyclase family. The encoded protein plays a role in RNA metabolism by catalyzing the ATP-dependent conversion of the 3'-phosphate of RNA substrates to a 2',3'-cyclic phosphodiester. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Feb 2012].
- **Diseases (Open Targets)**: alcohol drinking (0.215); cardiomyopathy (0.022); neoplasm (0.017); ovarian carcinoma (0.011); breast cancer (0.008)
- **Europe PMC papers**: 5045
- **Why important**: RTCA connects the NAXD branch with COG1 and is the only apparent bridge to the Golgi-associated gene in the module. Its established function is ATP-dependent RNA three-prime-terminal phosphate cyclization, placing it in RNA metabolism and processing. It has the largest literature volume among the module genes and disease or phenotype associations including cardiomyopathy and neoplastic conditions.
- **Conclusion**: Established evidence supports RTCA as an RNA-processing enzyme and a network connector. Its position could indicate a cellular-maintenance component of the module, but there is no evidence that the module represents an RNA-processing pathway or that RTCA physically associates with COG1 or NAXD.

#### KCTD12

- **Related proteins** (co-abundance neighbors): MBOAT7 (0.83), NAXD (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: potassium channel tetramerization domain containing 12. Enables identical protein binding activity. Predicted to be involved in protein homooligomerization. Predicted to act upstream of or within regulation of G protein-coupled receptor signaling pathway. Predicted to be located in cell projection. Predicted to be part of receptor complex. Predicted to be active in postsynaptic membrane and presynaptic membrane. [provided by Alliance of Genome Resource…
- **Diseases (Open Targets)**: adolescent idiopathic scoliosis (0.315); alcohol drinking (0.313); stroke disorder (0.296); sialolithiasis (0.251); Tietze syndrome (0.239)
- **Europe PMC papers**: 741
- **Why important**: KCTD12 occupies an internal position connecting NAXD with MBOAT7. It is annotated for protein homooligomerization, receptor-complex activity, and regulation of G protein-coupled receptor signaling. HPA data show enhanced representation in Hofbauer cells, Kupffer cells, lymphatic endothelial cells, macrophages, and monocyte progenitors, together with immune-cell enhancement in classical monocytes and myeloid dendritic cells. Its disease associations include neurological and vascular-related phenotypes.
- **Conclusion**: Established evidence supports KCTD12 as a receptor-associated and cell-state-related protein with notable myeloid and endothelial context. It may contribute to the module's cell-composition sensitivity. A role as a mechanistic link between signaling and lipid remodeling is plausible but not demonstrated by the available network or enrichment evidence.

#### MBOAT7

- **Related proteins** (co-abundance neighbors): KCTD12 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: membrane bound acylglycerophosphatidylinositol O-acyltransferase MBOAT7. This gene encodes a member of the membrane-bound O-acyltransferases family of integral membrane proteins that have acyltransferase activity. The encoded protein is a lysophosphatidylinositol acyltransferase that has specificity for arachidonoyl-CoA as an acyl donor. This protein is involved in the reacylation of phospholipids as part of the phospholipid remodeling pathway known as the Land cycle. …
- **Diseases (Open Targets)**: intellectual disability, autosomal recessive 57 (0.754); hereditary disease (0.487); autosomal recessive non-syndromic intellectual disability (0.462); complex neurodevelopmental disorder (0.370); neurodegenerative disease (0.345)
- **Europe PMC papers**: 1344
- **Why important**: MBOAT7 is the module's annotated phospholipid-remodeling enzyme and is connected to KCTD12. It catalyzes lysophosphatidylinositol reacylation using arachidonoyl-CoA and participates in phospholipid and phosphatidylinositol remodeling. HPA annotations include adrenal-gland enrichment, neuronal and ependymal cell enhancement, and group enrichment in granulocytes. It has established associations with autosomal-recessive intellectual disability and broader neurodevelopmental disease, with a substantial literature.
- **Conclusion**: Established evidence supports MBOAT7 as a biologically important membrane-lipid remodeling enzyme and a plausible marker of cell-state or membrane composition. Its co-abundance with KCTD12 does not establish a direct interaction or prove that phospholipid remodeling defines the entire module.

#### COG1

- **Related proteins** (co-abundance neighbors): RTCA (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: component of oligomeric golgi complex 1. The protein encoded by this gene is one of eight proteins (Cog1-8) which form a Golgi-localized complex (COG) required for normal Golgi morphology and function. It is thought that this protein is required for steps in the normal medial and trans Golgi-associated processing of glycoconjugates and plays a role in the organization of the Golgi-localized complex. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: COG1-congenital disorder of glycosylation (0.789); congenital disorder of glycosylation (0.371); dengue disease (0.370); neurodegenerative disease (0.369); hereditary disease (0.194)
- **Europe PMC papers**: 535
- **Why important**: COG1 is the endpoint of the RTCA branch and encodes a component of the conserved oligomeric Golgi complex. Its established role is in Golgi morphology, retrograde transport, vesicle recycling, and glycoconjugate processing. It has a strong disease association with COG1-related congenital disorder of glycosylation and is detected in testis.
- **Conclusion**: Established evidence supports COG1 as a Golgi trafficking and glycosylation protein with clear disease relevance. Its isolated position in this small network makes it useful for identifying a possible organelle-maintenance signal, but the module does not establish a Golgi-centered mechanism.

#### HMGCL

- **Related proteins** (co-abundance neighbors): NAXD (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3-hydroxy-3-methylglutaryl-CoA lyase. The protein encoded by this gene belongs to the HMG-CoA lyase family. It is a mitochondrial enzyme that catalyzes the final step of leucine degradation and plays a key role in ketone body formation. Mutations in this gene are associated with HMG-CoA lyase deficiency. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2009].
- **Diseases (Open Targets)**: 3-hydroxy-3-methylglutaric aciduria (0.849); long chain 3-hydroxyacyl-CoA dehydrogenase deficiency (0.548); hereditary disease (0.494); Intellectual disability (0.370); neurodegenerative disease (0.215)
- **Europe PMC papers**: 1278
- **Why important**: HMGCL is connected to NAXD and encodes the mitochondrial enzyme catalyzing the final step of leucine degradation and ketone-body formation. HPA shows liver tissue enhancement and hepatocyte-related cell enhancement, while protein is detected in testis. HMGCL deficiency is an established inherited metabolic disease, and the gene has a substantial disease and biochemical literature.
- **Conclusion**: Established evidence supports HMGCL as a mitochondrial amino-acid-catabolic and ketogenesis enzyme, making it the clearest liver-metabolic component of the module. Its connection to NAXD may reflect shared metabolic-state regulation, but a direct relationship or shared pathway within this module is not established.

## Module 12

**Tissue pair**: circulatory_system and testis  
**Genes (5)**: DHRS11, ECI2, HSPA4L, MYG1, NSUN2

### Function

This is a small, internally connected co-abundance module with no GO or KEGG term passing global multiple-testing correction; therefore no pathway-level function can be claimed from enrichment. The gene annotations instead suggest a mixed biological signal: steroid biosynthesis through DHRS11, mitochondrial RNA and ribosome-related processing through MYG1, protein folding and stress response through HSPA4L, RNA modification and processing through NSUN2, and mitochondrial or peroxisomal unsaturated-fatty-acid beta-oxidation through ECI2. Taken together, the most defensible interpretation is a testis-associated module linking cellular proteostasis, RNA maturation, lipid metabolism, and steroid-related metabolism, rather than a single established pathway.

**Cell composition.** All module proteins were detected in testis, while the circulatory-system HPA tissue comparison had no matching tissue data. The module is not predominantly composed of plasma or secreted proteins: only DHRS11 is annotated as secreted to the digestive system, whereas the remaining proteins are intracellular or membrane-associated. The genes are not uniformly tissue-restricted. HPA annotations include testis enrichment for HSPA4L, liver enhancement for ECI2, intestine enrichment for DHRS11, and low tissue specificity for MYG1 and NSUN2. Most genes show cell-type enhancement, including several neural cell types, while blood-cell specificity is generally low; HSPA4L is immune-cell enhanced in eosinophils. This pattern argues against a simple blood-cell module, but shared testis cellular composition or coordinated testicular expression could contribute strongly to the cross-tissue association.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no STRING functional-enrichment result was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated by the supplied physical-interaction or complex databases. The network may represent coordinated expression, indirect biology, tissue or cell-state composition, or interactions below the database confidence threshold, rather than a documented protein complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a potentially novel co-abundance association, because its specific gene combination is not represented by reported high-confidence STRING interactions or a shared hu.MAP complex. However, absence from those resources does not establish novelty: the genes have established individual functions, substantial literature for several members, and the module has no globally significant GO or KEGG term. The appropriate conclusion is that this is a novel candidate network pattern requiring independent replication, not a proven new molecular complex or pathway.

**Hypothesis.** Hypothesis: in testicular cells, coordinated regulation of steroid-related metabolism and fatty-acid oxidation may occur alongside increased proteostasis and RNA-processing demands during germ-cell development. DHRS11 and ECI2 could represent metabolic components, HSPA4L could buffer protein-folding stress, and MYG1 together with NSUN2 could support mitochondrial or nuclear RNA maturation and translational competence. The observed cross-tissue module could therefore reflect a shared metabolic and proteostatic cell state rather than direct physical binding among all members. This hypothesis is not established by enrichment or interaction evidence and should be tested with independent expression cohorts, cell-resolved data, and protein-level or perturbation experiments.

### Important genes

#### DHRS11

- **Related proteins** (co-abundance neighbors): MYG1 (0.94), HSPA4L (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dehydrogenase/reductase 11. Enables 17-beta-hydroxysteroid dehydrogenase (NADP+) activity; 17-beta-ketosteroid reductase activity; and 3-keto sterol reductase activity. Involved in steroid biosynthetic process. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.428); intelligence (0.305); obesity disorder (0.257); mathematical ability (0.217); overnutrition (0.206)
- **Europe PMC papers**: 230
- **Why important**: DHRS11 is a network connector linking MYG1 and HSPA4L. Its annotated activities include steroid biosynthesis, estrogen biosynthesis, and ketosteroid reduction, making it the clearest link to testicular endocrine and metabolic biology. HPA places it in intestine-enriched tissue, with testis protein detection and no immune-cell detection; it is also the only module member annotated as secreted to the digestive system. Its literature volume is moderate relative to NSUN2 and HSPA4L, and the supplied disease associations are mainly computational or trait-oriented rather than a definitive disease mechanism.
- **Conclusion**: Established: DHRS11 is a metabolic enzyme candidate with steroid-related functions and a central position in this small co-abundance network. Hypothesis: it may help connect steroid metabolism with the proteostasis-associated portion of the module in testis. The module does not establish a direct interaction or a disease role for DHRS11.

#### MYG1

- **Related proteins** (co-abundance neighbors): DHRS11 (0.94), ECI2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MYG1 exonuclease. Predicted to enable nuclease activity. Predicted to be involved in nucleic acid phosphodiester bond hydrolysis. Predicted to act upstream of or within locomotory exploration behavior. Located in mitochondrion and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: triple-A syndrome (0.333); vitiligo (0.090); lung adenocarcinoma (0.074); breast carcinoma (0.037); breast cancer (0.037)
- **Europe PMC papers**: 183
- **Why important**: MYG1 is a network connector between DHRS11 and ECI2. Its annotated nuclease function and proposed roles in mitochondrial RNA metabolism, rRNA processing, and mRNA processing provide a possible RNA-biological bridge between metabolic genes. HPA reports low tissue specificity but enhancement across several neural cell types, with low immune-cell specificity and testis protein detection. Its literature volume is limited compared with NSUN2, and its disease associations are led by computational links rather than a well-established mechanism.
- **Conclusion**: Established: MYG1 is annotated as a nuclease-related gene with mitochondrial and nuclear RNA-processing roles and occupies a connector position. Hypothesis: it may coordinate RNA quality or processing with the metabolic state represented by DHRS11 and ECI2. This proposed bridge remains mechanistic speculation.

#### HSPA4L

- **Related proteins** (co-abundance neighbors): DHRS11 (0.84), NSUN2 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 4 like. The protein encoded by this gene is heat shock inducible and may act as a chaperone. The encoded protein can protect the heat-shocked cell against the harmful effects of aggregated proteins. This gene is highly expressed in leukemia cells and may be a good target for therapeutic intervention. Several transcripts encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 20…
- **Diseases (Open Targets)**: alcohol drinking (0.111); ovarian neoplasm (0.110); open-angle glaucoma (0.094); nasopharyngeal carcinoma (0.074); familial idiopathic steroid-resistant nephrotic syndrome (0.061)
- **Europe PMC papers**: 815
- **Why important**: HSPA4L connects DHRS11 with NSUN2 and is the strongest testis-specific biological marker in the module based on the supplied HPA description. It is enhanced in early spermatids, late primary spermatocytes, and late spermatids, and its annotated functions include chaperoning, protein folding, and response to unfolded protein. It has substantial literature volume and reported associations with several disease or therapeutic areas, although those associations do not prove relevance to this module. Its eosinophil enhancement is a reminder that tissue-associated signals can include cell-type contributions.
- **Conclusion**: Established: HSPA4L is a testis-associated, heat-shock-inducible chaperone candidate with a connector position and a strong germ-cell expression context. Hypothesis: it may protect developing germ cells from proteotoxic stress while the accompanying metabolic and RNA-processing programs are active. The supplied network does not show that HSPA4L physically binds the neighboring genes.

#### NSUN2

- **Related proteins** (co-abundance neighbors): HSPA4L (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP2/Sun RNA methyltransferase 2. This gene encodes a methyltransferase that catalyzes the methylation of cytosine to 5-methylcytosine (m5C) at position 34 of intron-containing tRNA(Leu)(CAA) precursors. This modification is necessary to stabilize the anticodon-codon pairing and correctly translate the mRNA. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Mar…
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.694); hereditary disease (0.518); Intellectual disability (0.489); phenylketonuria (0.470); neurodegenerative disease (0.462)
- **Europe PMC papers**: 2458
- **Why important**: NSUN2 is the module member with the largest literature volume and is annotated as an RNA cytosine methyltransferase involved in tRNA modification, rRNA processing, mRNA processing, and nuclear mRNA export. It is connected to HSPA4L, placing RNA modification adjacent to the module's proteostasis component. HPA reports low tissue and cell-type specificity, intracellular and membrane-associated localization, and testis protein detection. Its reported disease associations include intellectual disability and neurodegenerative disease, but these associations should not be transferred directly to the present module.
- **Conclusion**: Established: NSUN2 is a well-studied RNA-modification and RNA-processing gene with a terminal network position in this module. Hypothesis: NSUN2 may support translational fidelity or RNA maturation in the testicular cell state represented by the module. Its literature prominence makes it biologically important, but does not demonstrate that the module is an NSUN2-centered complex.

#### ECI2

- **Related proteins** (co-abundance neighbors): MYG1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Peroxisomes, Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: enoyl-CoA delta isomerase 2. This gene encodes a member of the hydratase/isomerase superfamily. The protein encoded is a key mitochondrial enzyme involved in beta-oxidation of unsaturated fatty acids. It catalyzes the transformation of 3-cis and 3-trans-enoyl-CoA esters arising during the stepwise degradation of cis-, mono-, and polyunsaturated fatty acids to the 2-trans-enoyl-CoA intermediates. Alternatively spliced transcri…
- **Diseases (Open Targets)**: thyroiditis (0.247); glomerulonephritis (0.161); nephritis (0.141); Abnormality of the skeletal system (0.140); brain aneurysm (0.138)
- **Europe PMC papers**: 516
- **Why important**: ECI2 is connected to MYG1 and supplies the clearest fatty-acid metabolic interpretation. It is annotated as a mitochondrial enzyme in unsaturated-fatty-acid beta-oxidation and is localized to peroxisomes and mitochondria. HPA reports liver enhancement, enhancement in hepatocytes and several other cell types, low immune-cell specificity, and testis protein detection. Its literature volume is substantial, while the listed disease associations are diverse and not specific to this module.
- **Conclusion**: Established: ECI2 is a mitochondrial or peroxisomal fatty-acid metabolism gene occupying a terminal position connected to MYG1. Hypothesis: it may provide energy or lipid intermediates that support spermatogenic activity and steroid-related metabolism. The module does not establish a direct ECI2 interaction with MYG1 or a causal role in testicular physiology.

## Module 13

**Tissue pair**: circulatory_system and testis  
**Genes (6)**: KRT10, KRT14, KRT9, KRT2, KRT1, KRT5

### Function

The module is a coherent epithelial keratin intermediate-filament program. All module genes support the globally corrected keratin-filament and intermediate-filament annotations (6 globally significant GO/KEGG terms, q_global 2.6e-10–1.21e-07; see the table). The globally corrected KEGG and GO evidence further supports cornified-envelope formation, epidermis and skin development, keratinocyte and epithelial differentiation, cytoskeletal organization, and structural molecule activity (21 globally significant GO/KEGG terms, q_global 2.77e-07–0.0132; see the table). The Staphylococcus aureus infection and estrogen-signaling annotations (KEGG Staphylococcus aureus infection - Homo sapiens (human); q_global = 0.0244) (GO:BP animal organ development; q_global = 0.0247) (KEGG Estrogen signaling pathway - Homo sapiens (human); q_global = 0.0364) are secondary pathway-context signals, not evidence that the module is primarily an infection or hormone-response module. Established interpretation: this is a structural and differentiation-associated keratin program rather than a circulatory or testis-specific biochemical pathway.

**Cell composition.** The module is strongly tissue- and cell-type-specific rather than a broadly expressed housekeeping module. HPA associates most genes with skin and suprabasal keratinocytes, with additional basal-epithelial and related epithelial signals. KRT five is group-enriched across cervix, esophagus, skin, and vagina, while KRT nine is tissue-enriched in lymphoid tissue and has enhanced expression in several specialized cell types. Only KRT ten is annotated as secreted in other tissues; the module is therefore not predominantly a plasma or secreted-protein module. Most genes are not detected in immune cells, although isolated immune-cell enhancement or enrichment is reported for some genes. All module proteins are reported as not detected in testis by HPA, despite the module being shared by the circulatory-system and testis datasets. This pattern makes epithelial-cell contribution, tissue contamination, sample carryover, or shared epithelial-like cell populations more plausible explanations than a blood-cell or generic housekeeping signature.

**GO/KEGG enrichment**: 31 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC keratin filament | 2.6e-10 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament organization | 1.11e-09 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament-based process | 5.3e-09 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament cytoskeleton organization | 5.3e-09 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:CC intermediate filament | 4.48e-08 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:CC intermediate filament cytoskeleton | 1.21e-07 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| KEGG Cornified envelope formation - Homo sapiens (human) | 2.77e-07 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP epidermis development | 6.2e-07 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP skin development | 7.29e-07 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:MF structural constituent of skin epidermis | 8.81e-07 | KRT1, KRT10, KRT2, KRT5 |
| KEGG Cadherin signaling - Homo sapiens (human) | 3.02e-06 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP keratinocyte differentiation | 3.94e-06 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| GO:BP epidermal cell differentiation | 1.01e-05 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| GO:BP epithelial cell differentiation | 3.4e-05 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:CC cornified envelope | 8.7e-05 | KRT1, KRT10, KRT14, KRT2 |

### STRING and hu.MAP

STRING independently supports a keratin filament, intermediate-filament, and cornified-envelope interpretation through the supplementary enrichments (8 supplementary STRING terms; within-query FDR 5.01e-11–1.03e-09). The reported high-confidence STRING relationships include the expected keratin pairings and interactions among KRT one, KRT two, KRT five, KRT ten, and KRT fourteen; KRT fourteen–KRT five is especially consistent with the established basal-epithelial keratin pair. KRT nine has no listed STRING partner in the supplied interaction summary, although it is connected to the other module genes in the co-abundance network. Thus, much of the module's structure recapitulates known keratin biology and likely reflects shared expression and established filament compatibility rather than a newly discovered protein complex. No hu.MAP complex contains at least two module members, so the data do not provide independent hu.MAP support for a defined multiprotein complex.

**STRING interactions (score >= 0.7)**: 7 of 15 gene pairs: KRT1–KRT10 (0.999); KRT1–KRT2 (0.956); KRT1–KRT5 (0.923); KRT10–KRT2 (0.904); KRT10–KRT5 (0.793); KRT14–KRT5 (0.999); KRT2–KRT5 (0.871)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Keratin filament (FDR = 5.01e-11, 6 genes); COMPARTMENTS Keratin filament (FDR = 5.25e-11, 6 genes); Keyword Keratin (FDR = 6.95e-11, 6 genes); SMART Intermediate filament protein (FDR = 1.82e-10, 6 genes); Keyword Intermediate filament (FDR = 2.35e-10, 6 genes); RCTM Formation of the cornified envelope (FDR = 6.73e-10, 6 genes); InterPro Intermediate filament protein, conserved site (FDR = 1.03e-09, 6 genes); InterPro Intermediate filament, rod domain (FDR = 1.03e-09, 6 genes); HPO Erythema (FDR = 3.77e-08, 6 genes); PMID (2025) Mass spectrometric detection of keratins in tear fluid. (FDR = 3.78e-08, 6 genes); PMID (2023) Key Factors in the Complex and Coordinated Network of Skin Keratinization: Their Significance and Involvement in Common Skin Conditions. (FDR = 3.78e-08, 6 genes); PMID (2022) A metatranscriptomic approach to explore longitudinal tissue specimens from non-healing diabetes related foot ulcers. (FDR = 3.78e-08, 6 genes); PMID (2022) Palmoplantar Keratoderma: A Molecular Genetic Analysis of Family Cases. (FDR = 3.78e-08, 6 genes); PMID (2021) Keratin Biomaterials in Skin Wound Healing, an Old Player in Modern Medicine: A Mini Review. (FDR = 3.78e-08, 6 genes); PMID (2019) Keratin 9 L164P mutation in a Chinese pedigree with epidermolytic palmoplantar keratoderma, cytokeratin analysis, and literature review. (FDR = 3.78e-08, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The biological function itself is not a new discovery: the genes are established keratins, their epithelial roles are extensively annotated, STRING contains several expected relationships, and the literature and disease associations are substantial. The potentially novel observation is the coordinated co-abundance of this keratin program across the circulatory-system and testis tissue groups. However, that cross-tissue observation should not be called a new mechanism without validation, because HPA places the genes mainly in skin and epithelial cell populations and reports no testis protein detection. The absence of a hu.MAP complex is not evidence of novelty, and the absence of a particular STRING relationship would not establish novelty either. Overall, this is best described as a potentially interesting cross-tissue network observation built from well-known keratin biology, not a newly established biological module.

**Hypothesis.** Hypothesis: the shared module reflects coordinated epithelial-cell or epithelial-material contribution to both tissue datasets, with co-abundance arising from the assembly and differentiation state of keratin intermediate filaments. A secondary possibility is that keratin-positive epithelial fragments, barrier cells, or sample carryover were represented in both tissue groups. The network and enrichment data support this structural interpretation, but they do not establish that these keratins perform a specialized function in testis or circulating blood. This hypothesis should be tested by examining cell-type-resolved expression, sample histology, contamination markers, and independent protein measurements.

### Important genes

#### KRT2

- **Related proteins** (co-abundance neighbors): KRT10 (0.91), KRT1 (0.87), KRT5 (0.85), KRT9 (0.83), KRT14 (0.81); STRING partners: KRT1 (0.956), KRT10 (0.904), KRT5 (0.871)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location Intermediate filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 2. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is expressed largely in the upper spinous layer of epidermal keratinocytes and mutations in this gene …
- **Diseases (Open Targets)**: superficial epidermolytic ichthyosis (0.815); exfoliative ichthyosis (0.358); Palmoplantar hyperkeratosis (0.267); hereditary disease (0.193); Vertigo (0.145)
- **Europe PMC papers**: 7459
- **Why important**: KRT2 is the strongest network hub in the supplied module and connects to every other module member. It is tissue-enriched in skin and cell-type-enriched in suprabasal keratinocytes, and it participates in nearly all relevant globally corrected keratin, epidermal differentiation, and cytoskeletal terms (27 globally significant GO/KEGG terms, q_global 2.6e-10–0.0132; see the table). Its established role is an upper-spinous epidermal type-two keratin, and disease associations include superficial epidermolytic ichthyosis and related hyperkeratotic disorders. Its literature volume is substantial, supporting a well-established biological interpretation.
- **Conclusion**: Established: KRT2 is a central suprabasal structural keratin and a major marker of the module's epidermal differentiation program. Hypothesis: its hub position may make it a useful indicator of the shared epithelial signal, but the network does not show that KRT2 drives the cross-tissue association.

#### KRT1

- **Related proteins** (co-abundance neighbors): KRT10 (0.95), KRT9 (0.93), KRT2 (0.87); STRING partners: KRT10 (0.999), KRT2 (0.956), KRT5 (0.923)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 is a highly connected module member with strong STRING support for interactions with KRT10, KRT2, and KRT5. It is skin-enriched and suprabasal-keratinocyte-enriched, and it appears throughout the globally corrected keratin-filament, epidermal development, cornification, and structural annotations (27 globally significant GO/KEGG terms, q_global 2.6e-10–0.0132; see the table). It is a major spinous and granular-layer keratin, and its disease associations include several epidermolytic and palmoplantar keratoderma conditions. Its literature volume is extensive.
- **Conclusion**: Established: KRT1 is a core structural component of differentiated epidermal keratin networks. Hypothesis: KRT1 may represent one of the most informative readouts of epithelial material underlying the shared module, rather than a testis-specific effector.

#### KRT10

- **Related proteins** (co-abundance neighbors): KRT1 (0.95), KRT2 (0.91), KRT9 (0.85); STRING partners: KRT1 (0.999), KRT2 (0.904), KRT5 (0.793)
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 10. This gene encodes a member of the type I (acidic) cytokeratin family, which belongs to the superfamily of intermediate filament (IF) proteins. Keratins are heteropolymeric structural proteins which form the intermediate filament. These filaments, along with actin microfilaments and microtubules, compose the cytoskeleton of epithelial cells. Mutations in this gene are associated with epidermolytic …
- **Diseases (Open Targets)**: epidermolytic hyperkeratosis 2A, autosomal dominant (0.787); epidermolytic ichthyosis (0.772); congenital reticular ichthyosiform erythroderma (0.727); ichthyosis, annular epidermolytic 1 (0.647); annular epidermolytic ichthyosis (0.642)
- **Europe PMC papers**: 2736
- **Why important**: KRT10 is a central differentiated-epithelium keratin with strong STRING links to KRT1, KRT2, and KRT5. It is skin-enriched and suprabasal-keratinocyte-enriched, contributes to the globally corrected keratin, cornified-envelope, epidermal differentiation, and cytoskeletal terms (27 globally significant GO/KEGG terms, q_global 2.6e-10–0.0132; see the table), and is also present in the supplementary infection and estrogen-signaling annotations (KEGG Staphylococcus aureus infection - Homo sapiens (human); q_global = 0.0244) (GO:BP animal organ development; q_global = 0.0247) (KEGG Estrogen signaling pathway - Homo sapiens (human); q_global = 0.0364). Its established role is as a type-one partner in epithelial intermediate filaments, and it is associated with epidermolytic hyperkeratosis and related ichthyoses. The fact sheet also identifies it as secreted in other tissues, which is relevant when considering sample carryover.
- **Conclusion**: Established: KRT10 is a differentiated epidermal keratin with strong network and annotation support. Hypothesis: its detection across the tissue pair could reflect epithelial material or tissue-associated protein carryover; the supplied data do not establish a specialized circulating or testicular role.

#### KRT14

- **Related proteins** (co-abundance neighbors): KRT5 (0.95), KRT9 (0.83), KRT2 (0.81); STRING partners: KRT5 (0.999)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 14. This gene encodes a member of the keratin family, the most diverse group of intermediate filaments. This gene product, a type I keratin, is usually found as a heterotetramer with two keratin 5 molecules, a type II keratin. Together they form the cytoskeleton of epithelial cells. Mutations in the genes for these keratins are associated with epidermolysis bullosa simplex. At least one pseudogene has…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 1A, generalized severe (0.823); epidermolysis bullosa simplex 1C, localized (0.818); epidermolysis bullosa simplex 1B, generalized intermediate (0.802); epidermolysis bullosa simplex 1D, generalized, intermediate or severe, autosomal recessive (0.759); Naegeli-Franceschetti-Jadassohn syndrome (0.759)
- **Europe PMC papers**: 6348
- **Why important**: KRT14 links the basal-epithelial component of the module to the differentiated keratin network and has a particularly strong STRING relationship with KRT5. HPA places it in skin and basal or suprabasal epithelial cell groups, while the globally corrected terms support intermediate filaments, epidermal development, epithelial differentiation, and keratinocyte differentiation (19 globally significant GO/KEGG terms, q_global 2.6e-10–0.000828; see the table) and (9 globally significant GO/KEGG terms, q_global 0.00112–0.0247; see the table). Its established function is formation of a heterotetramer with KRT5 in epithelial cytoskeleton, and its disease associations include multiple forms of epidermolysis bullosa simplex. Its literature volume is substantial.
- **Conclusion**: Established: KRT14 marks the basal epithelial keratin arm and provides a mechanistically meaningful link to KRT5. Hypothesis: its presence may indicate basal epithelial-cell contribution to the shared module, but it does not prove that basal cells are present in either tissue sample.

#### KRT5

- **Related proteins** (co-abundance neighbors): KRT14 (0.95), KRT2 (0.85); STRING partners: KRT1 (0.923), KRT10 (0.793), KRT14 (0.999), KRT2 (0.871)
- **HPA**: Group enriched; Group enriched; blood Immune cell enriched; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 5. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the basal layer of the epidermis with family member KRT14. Mutations in t…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 2C, localized (0.768); epidermolysis bullosa simplex 2A, generalized severe (0.761); epidermolysis bullosa simplex 2B, generalized intermediate (0.761); epidermolysis bullosa simplex 2F, with mottled pigmentation (0.729); Dowling-Degos disease 1 (0.697)
- **Europe PMC papers**: 7044
- **Why important**: KRT5 is the basal-epithelial counterpart of KRT14 and connects that pair to KRT1, KRT2, and KRT10 in STRING. It is group-enriched across several epithelial tissues and cell types, contributes to the globally corrected structural, epidermal, keratinization, and differentiation terms (19 globally significant GO/KEGG terms, q_global 2.6e-10–0.000828; see the table) and (9 globally significant GO/KEGG terms, q_global 0.00112–0.0247; see the table), and has established roles in basal-layer cytoskeleton, mechanical response, migration, and intermediate-filament polymerization. Its disease associations include multiple forms of epidermolysis bullosa simplex and Dowling-Degos disease. Its literature volume is extensive.
- **Conclusion**: Established: KRT5 identifies the basal epithelial structural program and forms a biologically established partnership with KRT14. Hypothesis: KRT5 may help explain the network bridge between basal and suprabasal keratin states, but this interpretation requires cell-resolved validation.
