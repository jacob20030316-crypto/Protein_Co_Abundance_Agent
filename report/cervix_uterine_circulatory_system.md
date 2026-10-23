# Conserved co-abundance modules: cervix_uterine and circulatory_system

## Module 0

**Tissue pair**: cervix_uterine and circulatory_system  
**Genes (50)**: PPP2R2A, AFDN, AKR1D1, ASRGL1, BPI, CRAT, CDO1, CHMP1A, CNOT12, CROCC, CTNND1, DCP1A, DGKA, EPS15, GRK5, H2AC21, HMOX1, HOOK1, HSPB1, HK3, IGHA1, INPP1, KRT19, LMO7, LSM7, PLBD1, MICU1, MMS19, MNDA, MYO6, NAA20, NCF2, NDRG2, LCN2, PCCA, PDZD8, PHPT1, PIP4K2C, PKP3, PLCD1, PNPT1, RBM27, RBM47, RNASET2, SERPINH1, SORL1, UBTF, WASHC4, XPO4, TJP1

### Function

No GO/KEGG term passed global correction, so the module has no statistically established GO/KEGG functional label. Its gene-level evidence instead indicates a mixed epithelial-junction, vesicle-trafficking, phosphoinositide-signaling, and innate-myeloid program. The strongest coherent structural signal is an epithelial adhesion network involving AFDN, CTNND1, TJP1, LMO7, PKP3, and related cytoskeletal proteins. A second signal involves neutrophil and monocyte biology, including BPI, NCF2, MNDA, HK3, HMOX1, LCN2, and PLBD1. Phosphoinositide and membrane-signaling genes, including PLCD1, DGKA, INPP1, and PIP4K2C, provide a possible signaling bridge between these components. These are biological interpretations of the gene annotations and network structure, not globally significant enrichment claims.

**Cell composition.** The module is compositionally mixed rather than a uniform housekeeping module. HPA indicates substantial representation of epithelial and mucosal cell types, especially esophageal apical cells, together with neutrophils, neutrophil progenitors, monocytes, macrophages, and other bone-marrow or lymphoid populations. Several genes are blood-cell associated, including BPI, NCF2, MNDA, HK3, LCN2, PLBD1, and RBM47. A minority of genes are secreted or blood-associated proteins, notably BPI, LCN2, SORL1, RNASET2, and IGHA1, while PLBD1 has intracellular and membrane localization. Many other genes are membrane, junctional, cytoskeletal, mitochondrial, or nuclear proteins. Cervix protein detection is present for many module genes, but the circulatory-system tissue has no matching HPA tissue entry. Therefore, the shared co-abundance pattern could partly reflect blood or infiltrating myeloid cells in the samples, alongside epithelial-cell content, rather than a single specialized cervix–circulation pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no supplementary functional-enrichment result. Its high-confidence interactions support a known epithelial-junction subnetwork: AFDN connects with CTNND1, LMO7, and TJP1, while CTNND1 connects with TJP1. STRING also supports a phosphoinositide-related neighborhood around PLCD1 involving DGKA, INPP1, and PIP4K2C, and a myeloid neighborhood involving HK3, MNDA, and NCF2. These relationships show that parts of the co-abundance module recapitulate established molecular associations, but most module pairs are not represented by high-confidence STRING interactions; co-abundance therefore adds an expression-level relationship that should not be interpreted as direct physical binding. hu.MAP supports several partially overlapping complexes. The most biologically informative are epithelial or mucosal complexes containing LCN2 with HMOX1 and NDRG2 (hu.MAP huMAP3_10678.1), LCN2 with PLBD1 and PKP3 (hu.MAP huMAP3_09929.1), AFDN with LMO7 (hu.MAP huMAP3_05977.1), BPI with MNDA (hu.MAP huMAP3_10260.1), and NCF2 with LCN2 or BPI (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_14295.1). hu.MAP also identifies mitochondrial or metabolic complexes containing PCCA, CRAT, and PNPT1 (hu.MAP huMAP3_13468.1) (hu.MAP huMAP3_10458.1), plus an endosomal or actin-associated complex containing WASHC4 and CNOT12 (hu.MAP huMAP3_12900.1). These complexes reinforce the view that the module combines epithelial organization, innate immunity, intracellular trafficking, and metabolism rather than representing one purified complex.

**STRING interactions (score >= 0.7)**: 9 of 1225 gene pairs: AFDN–CTNND1 (0.998); AFDN–LMO7 (0.983); AFDN–TJP1 (0.999); CTNND1–TJP1 (0.956); DGKA–PLCD1 (0.702); HK3–MNDA (0.78); INPP1–PLCD1 (0.915); MNDA–NCF2 (0.811); PIP4K2C–PLCD1 (0.78)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10678.1 (HMOX1, LCN2, NDRG2; 3/71); huMAP3_09929.1 (LCN2, PLBD1, PKP3; 3/75); huMAP3_13468.1 (PCCA, CRAT, PNPT1; 3/99); huMAP3_08328.1 (LCN2, NDRG2; 2/3); huMAP3_06637.1 (LCN2, NDRG2; 2/4); huMAP3_05977.1 (AFDN, LMO7; 2/12); huMAP3_10260.1 (BPI, MNDA; 2/14); huMAP3_09833.1 (HMOX1, NDRG2; 2/16); huMAP3_10458.1 (PCCA, PNPT1; 2/16); huMAP3_09434.1 (NCF2, LCN2; 2/33); huMAP3_14295.1 (BPI, NCF2; 2/38); huMAP3_12900.1 (WASHC4, CNOT12; 2/50); huMAP3_09125.1 (LCN2, PKP3; 2/53)

### Novelty

The module is unlikely to constitute a wholly new molecular pathway because its most interpretable components reproduce established junctional, myeloid, phosphoinositide, mitochondrial, and epithelial-complex relationships documented by STRING or hu.MAP. The shared co-abundance organization across cervix_uterine and circulatory_system could still be a new observation, especially because most module gene pairs lack curated high-confidence physical interactions and no GO/KEGG term passed global correction. However, the present evidence does not establish that the module is a new biological entity. Its apparent novelty is best described as a potentially distinctive tissue-pair co-abundance pattern whose reproducibility, cell-composition correction, and independence from blood contamination require validation.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of mucosal epithelial junction and barrier machinery together with a variable innate-myeloid or blood-cell component. In this model, AFDN, TJP1, CTNND1, LMO7, and PKP3 maintain epithelial adhesion and cytoskeletal organization; PLCD1 and related phosphoinositide regulators transmit membrane signals; and BPI, LCN2, NCF2, MNDA, and HMOX1 represent antimicrobial, oxidative-stress, and myeloid-defense activity. The shared signal between cervix_uterine and circulatory_system may therefore arise from epithelial–immune interface biology or from differing proportions of epithelial and circulating myeloid cells. This mechanism is a testable hypothesis, not a demonstrated causal pathway.

### Important genes

#### AFDN

- **Related proteins** (co-abundance neighbors): PLBD1 (0.96), HK3 (0.96), MNDA (0.92), IGHA1 (0.92), NCF2 (0.91), HOOK1 (0.91), CTNND1 (0.91), PLCD1 (0.89), BPI (0.86), PKP3 (0.84), CRAT (0.83); STRING partners: CTNND1 (0.998), LMO7 (0.983), TJP1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_05977.1
- **Function (MyGene.info)**: afadin, adherens junction formation factor. This gene encodes a multi-domain protein involved in signaling and organization of cell junctions during embryogenesis. It has also been identified as the fusion partner of acute lymphoblastic leukemia (ALL-1) gene, involved in acute myeloid leukemias with t(6;11)(q27;q23) translocation. Alternatively spliced transcript variants encoding different isoforms have been described for this gene, howeve…
- **Diseases (Open Targets)**: colorectal adenocarcinoma (0.401); lung carcinoma (0.371); gastric carcinoma (0.371); carcinoma of liver and intrahepatic biliary tract (0.370); melanoma (0.370)
- **Europe PMC papers**: 633
- **Why important**: AFDN is a central connector in the module's epithelial-adhesion neighborhood and links several module components, including CTNND1, LMO7, TJP1, PLBD1, HK3, MNDA, NCF2, and PLCD1. Its HPA localization at the plasma membrane and cell junctions, cervical detection, epithelial cell-type associations, STRING links to CTNND1, LMO7, and TJP1, and hu.MAP membership with LMO7 (hu.MAP huMAP3_05977.1) make it a strong structural anchor. Its disease associations include several carcinomas, while its literature volume is substantial.
- **Conclusion**: Established evidence supports AFDN as an adherens-junction and cell-adhesion factor that connects the epithelial structural part of the module to immune-associated and signaling genes. It is plausible, but not established, that AFDN helps coordinate epithelial barrier state with the co-abundant myeloid program.

#### TJP1

- **Related proteins** (co-abundance neighbors): EPS15 (0.91), CTNND1 (0.88), WASHC4 (0.87), MMS19 (0.86), RBM27 (0.82); STRING partners: AFDN (0.999), CTNND1 (0.956)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cell Junctions; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tight junction protein 1. This gene encodes a member of the membrane-associated guanylate kinase (MAGUK) family of proteins, and acts as a tight junction adaptor protein that also regulates adherens junctions. Tight junctions regulate the movement of ions and macromolecules between endothelial and epithelial cells. The multidomain structure of this scaffold protein, including a postsynaptic density 95/disc-large/zona occlu…
- **Diseases (Open Targets)**: dengue disease (0.476); COVID-19 (0.373); skin disorder (0.312); Hypocalcemia (0.264); cataract (0.256)
- **Europe PMC papers**: 6421
- **Why important**: TJP1 is a key tight-junction adaptor with a prominent position in the junctional subnetwork. It is detected in the cervix, localizes to cell junctions, and has strong STRING relationships with AFDN and CTNND1. Its established functions include tight-junction assembly, adherens-junction maintenance, actin organization, and regulation of epithelial permeability and migration. It also has a large literature base and disease associations involving epithelial and vascular-relevant disorders.
- **Conclusion**: Established evidence identifies TJP1 as a core epithelial barrier and junctional scaffold represented coherently in this module. The hypothesis that its co-abundance marks altered epithelial permeability or tissue-interface remodeling remains unproven in these data.

#### BPI

- **Related proteins** (co-abundance neighbors): HOOK1 (0.97), CROCC (0.92), LMO7 (0.90), AFDN (0.86), PLCD1 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10260.1, huMAP3_14295.1
- **Function (MyGene.info)**: bactericidal permeability increasing protein. This gene encodes a lipopolysaccharide binding protein. It is associated with human neutrophil granules and has antimicrobial activity against gram-negative organisms. [provided by RefSeq, Nov 2014].
- **Diseases (Open Targets)**: retinal degeneration (0.297); alcohol drinking (0.266); asthma (0.251); acute tonsillitis (0.243); infection (0.091)
- **Europe PMC papers**: 241427
- **Why important**: BPI provides the clearest secreted and blood-cell-associated innate-defense signal. It is enriched in bone marrow, associated with neutrophils and classical monocytes, secreted to blood, and participates in hu.MAP myeloid complexes with MNDA and NCF2 (hu.MAP huMAP3_10260.1) (hu.MAP huMAP3_14295.1). It is also connected within the module to HOOK1, LMO7, AFDN, and PLCD1. BPI has extensive literature and established antimicrobial and lipopolysaccharide-binding functions.
- **Conclusion**: Established evidence supports BPI as a neutrophil-granule antimicrobial protein and a likely marker of myeloid or blood contribution to the module. Its co-abundance with epithelial-junction genes does not establish direct epithelial regulation; it may instead reflect shared sample composition or mucosal immune surveillance.

#### NCF2

- **Related proteins** (co-abundance neighbors): CNOT12 (0.93), AFDN (0.91), HMOX1 (0.88), MNDA (0.81); STRING partners: MNDA (0.811)
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09434.1, huMAP3_14295.1
- **Function (MyGene.info)**: neutrophil cytosolic factor 2. This gene encodes neutrophil cytosolic factor 2, the 67-kilodalton cytosolic subunit of the multi-protein NADPH oxidase complex found in neutrophils. This oxidase produces a burst of superoxide which is delivered to the lumen of the neutrophil phagosome. Mutations in this gene, as well as in other NADPH oxidase subunits, can result in chronic granulomatous disease, a disease that causes recurrent …
- **Diseases (Open Targets)**: chronic granulomatous disease (0.734); systemic lupus erythematosus (0.548); celiac disease (0.525); rheumatoid arthritis (0.442); autoimmune disorder of musculoskeletal system (0.434)
- **Europe PMC papers**: 2695
- **Why important**: NCF2 is a module connector linking AFDN, CNOT12, HMOX1, and MNDA. HPA associates it with bone marrow, lung, lymphoid tissue, neutrophils, and eosinophils. It is a component of the neutrophil NADPH oxidase and has STRING support with MNDA, as well as hu.MAP support with BPI and LCN2-associated complexes (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_14295.1). Its chronic granulomatous disease association and substantial literature make it biologically informative.
- **Conclusion**: Established evidence supports NCF2 as an innate-defense and respiratory-burst component, strengthening the interpretation that the module contains a myeloid signal. A coordinated oxidative-stress circuit linking NCF2 with HMOX1 and epithelial junction genes is a hypothesis rather than a demonstrated mechanism.

#### LCN2

- **Related proteins** (co-abundance neighbors): PLCD1 (0.98); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Endoplasmic reticulum; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09929.1, huMAP3_08328.1, huMAP3_06637.1, huMAP3_09434.1, huMAP3_09125.1
- **Function (MyGene.info)**: lipocalin 2. This gene encodes a protein that belongs to the lipocalin family. Members of this family transport small hydrophobic molecules such as lipids, steroid hormones and retinoids. The protein encoded by this gene is a neutrophil gelatinase-associated lipocalin and plays a role in innate immunity by limiting bacterial growth as a result of sequestering iron-containing siderophores. The presence of this …
- **Diseases (Open Targets)**: psoriasis (0.124); type 2 diabetes mellitus (0.122); acute kidney injury (0.121); coronary artery disorder (0.121); neoplasm (0.120)
- **Europe PMC papers**: 11549
- **Why important**: LCN2 is a secreted or extracellularly detected innate-defense protein associated with bone marrow, gallbladder, salivary gland, neutrophil progenitors, neutrophils, basophils, and monocytes. It participates in several hu.MAP complexes spanning epithelial, myeloid, and blood-protein contexts (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09929.1) (hu.MAP huMAP3_08328.1) (hu.MAP huMAP3_06637.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_09125.1). Its established role in siderophore sequestration and antibacterial defense, cervical protein detection, and substantial literature make it a useful bridge between mucosal epithelium and innate immunity.
- **Conclusion**: Established evidence supports LCN2 as an antimicrobial and inflammatory-interface marker that can occur in both epithelial and myeloid contexts. Its module position is consistent with a shared mucosal–circulatory defense state, but cannot distinguish true cross-tissue regulation from cell-mixture effects.

#### PKP3

- **Related proteins** (co-abundance neighbors): PLCD1 (0.93), CHMP1A (0.85), AFDN (0.84), SERPINH1 (0.83), CTNND1 (0.82), XPO4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cell Junctions; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09929.1, huMAP3_09125.1
- **Function (MyGene.info)**: plakophilin 3. This gene encodes a member of the arm-repeat (armadillo) and plakophilin gene families. Plakophilin proteins contain numerous armadillo repeats, localize to cell desmosomes and nuclei, and participate in linking cadherins to intermediate filaments in the cytoskeleton. This protein may act in cellular desmosome-dependent adhesion and signaling pathways. Two transcript variants encoding different is…
- **Diseases (Open Targets)**: anorectal malformation (0.295); neurodegenerative disease (0.292); lymphopenia (0.111); neutropenia (0.111); hypertensive disorder (0.106)
- **Europe PMC papers**: 747
- **Why important**: PKP3 is a cervical-detected cell-junction protein with strong epithelial cell-type associations, especially esophageal and other barrier epithelia. Its known roles include desmosome assembly, epithelial structure maintenance, and cytokine-related regulation. It connects in the module to AFDN, CTNND1, PLCD1, and other structural or signaling genes, and appears in hu.MAP epithelial complexes with LCN2 and PLBD1 (hu.MAP huMAP3_09929.1) (hu.MAP huMAP3_09125.1). Its disease associations and literature support relevance to epithelial integrity and pathology.
- **Conclusion**: Established evidence supports PKP3 as an epithelial desmosomal and barrier-maintenance component, making it an important counterpoint to the module's myeloid genes. The possibility that PKP3-mediated barrier changes influence co-abundant innate-defense proteins is a mechanistic hypothesis, not a conclusion from the network alone.

## Module 1

**Tissue pair**: cervix_uterine and circulatory_system  
**Genes (37)**: BZW2, ORM1, AKAP13, APOA2, RNF40, CAPZB, CTSG, CD5L, TRIP10, SPECC1, DPP4, EFHD2, FGA, FMNL1, GALE, GALNT7, IFI30, HDGF, IDE, ITPRID2, LYZ, IGF2R, NUCB1, PCK2, HPGD, PLEC, NAPRT, PODXL, PSMA4, PRXL2A, RAB27A, SNRPA1, SAMHD1, SH3BGRL3, SPTBN2, TUBA4A, VASP

### Function

The strongest supported interpretation is an extracellular, blood-associated module with contributions from plasma protein biology, acute-phase and innate immune defense, coagulation, proteolysis, and cell-surface or cytoskeletal organization. The only globally corrected GO/KEGG result is the extracellular-region term (GO:CC extracellular region; q_global = 0.016), which covers most of the module and is therefore the primary functional evidence. The module is not a single canonical intracellular pathway: it combines secreted plasma proteins such as APOA2, FGA, ORM1, CD5L, DPP4, and LYZ with membrane, vesicle, protease, and cytoskeletal genes. FGA supports coagulation, platelet activation, cell-matrix adhesion, and fibrinolysis; ORM1 marks acute-phase and inflammatory regulation; LYZ and CTSG support antimicrobial and myeloid defense; DPP4 supports extracellular peptide processing and immune or metabolic regulation; and HPGD links the module to prostaglandin metabolism and inflammatory physiology. These observations support an extracellular inflammatory and hemostatic interface rather than a narrowly defined biochemical pathway. No GO/KEGG biological-process or KEGG term passed global correction beyond the extracellular-region cellular-component term (GO:CC extracellular region; q_global = 0.016).

**Cell composition.** The module has a strong extracellular and blood-plasma component, but it is not composed predominantly of secreted proteins: the HPA summary identifies a substantial secreted fraction alongside many intracellular, membrane, cytoskeletal, Golgi, and vesicular proteins. APOA2, FGA, ORM1, CD5L, DPP4, LYZ, NUCB1, and HDGF are reported as secreted to blood or secreted in other tissues, while CTSG and IFI30 are intracellular or membrane-associated and several genes encode structural or trafficking proteins. HPA tissue and single-cell profiles are heterogeneous, with liver, stomach, skeletal muscle, bone marrow, lymphoid tissue, neutrophils, epithelial populations, trophoblasts, and enterocytes recurring among enriched contexts. Most genes have low immune-cell specificity, although a subset is associated with neutrophils, monocytes, myeloid dendritic cells, basophils, or related myeloid populations. This mixture makes blood or plasma carryover, vascular material, shared myeloid cells, epithelial interfaces, or other shared cell types plausible contributors to the conserved signal. Detection of many proteins in cervix_uterine does not establish that the module is produced by cervical tissue itself, and there is no matching HPA tissue entry for circulatory_system.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC extracellular region | 0.016 | APOA2, CAPZB, CD5L, CTSG, DPP4, FGA, FMNL1, GALNT7, HDGF, HPGD, IDE, IFI30, IGF2R, LYZ, NAPRT, NUCB1, ORM1, PLEC, PODXL, PRXL2A, PSMA4, RAB27A, SH3BGRL3, SPTBN2, TRIP10, TUBA4A, VASP |

### STRING and hu.MAP

STRING provides a small but coherent set of high-confidence known relationships. The strongest connections include DPP4 with IGF2R, CTSG with LYZ, FGA with LYZ, APOA2 with FGA, APOA2 with ORM1, and FGA with ORM1. These links reinforce the interpretation of a connected extracellular, plasma, protease, and immune-defense component rather than proving that every module edge is a physical protein interaction. hu.MAP shows repeated co-membership of APOA2, FGA, and ORM1 in several plasma-protein and acute-phase-related complexes (hu.MAP huMAP3_07432.1) through (hu.MAP huMAP3_08700.1) and (hu.MAP huMAP3_07265.1) through (hu.MAP huMAP3_09434.1). CTSG and LYZ co-occur in a myeloid or secretory complex (hu.MAP huMAP3_11343.1), while ITPRID2 with SPECC1 (hu.MAP huMAP3_05613.1) and TUBA4A with SAMHD1 (hu.MAP huMAP3_10665.1) provide more limited structural or intracellular complex support. The repeated hu.MAP representation of APOA2, FGA, and ORM1 is the clearest known-complex signal. Many remaining module relationships are absent from the supplied STRING and hu.MAP evidence, so the co-abundance network should not be interpreted as a map of direct physical interactions.

**STRING interactions (score >= 0.7)**: 6 of 666 gene pairs: APOA2–FGA (0.893); APOA2–ORM1 (0.772); CTSG–LYZ (0.836); DPP4–IGF2R (0.945); FGA–LYZ (0.861); FGA–ORM1 (0.747)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Extracellular region (FDR = 0.0129, 27 genes); Component Extracellular space (FDR = 0.0311, 25 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07432.1 (APOA2, FGA, ORM1; 3/18); huMAP3_08395.1 (APOA2, FGA, ORM1; 3/43); huMAP3_09531.1 (APOA2, FGA, ORM1; 3/47); huMAP3_10101.1 (APOA2, FGA, ORM1; 3/49); huMAP3_15040.1 (APOA2, FGA, ORM1; 3/64); huMAP3_10678.1 (APOA2, FGA, ORM1; 3/71); huMAP3_02242.1 (FGA, ORM1; 2/9); huMAP3_08700.1 (APOA2, ORM1; 2/11); huMAP3_05613.1 (ITPRID2, SPECC1; 2/11); huMAP3_07265.1 (APOA2, ORM1; 2/20); huMAP3_09434.1 (FGA, ORM1; 2/33); huMAP3_10665.1 (TUBA4A, SAMHD1; 2/42); huMAP3_11343.1 (CTSG, LYZ; 2/54)

### Novelty

The module may be a novel tissue-pair co-abundance observation, but the biological components are not novel in isolation. Its extracellular-region enrichment is supported by established annotations, its plasma-protein core is represented in hu.MAP, and several STRING relationships are already known. The potentially new aspect is the conservation of this mixed plasma, innate-immune, epithelial-interface, and cytoskeletal expression pattern between cervix_uterine and circulatory_system. However, the module could reflect shared blood content, secreted proteins, or shared cell types rather than a newly discovered cervix-specific mechanism. Absence of a relationship from STRING or hu.MAP cannot establish novelty, because co-abundance can arise from co-expression, shared cellular origin, extracellular carryover, coordinated regulation, or context-specific interactions. A claim of a new biological mechanism would require independent validation, cell-composition adjustment, replication in separate cohorts, and experimental testing.

**Hypothesis.** Hypothesis: the conserved module represents a blood-exposed extracellular inflammatory and hemostatic interface that is captured in both cervix_uterine and circulatory_system. In this model, liver-derived APOA2, FGA, and ORM1 enter or accompany the tissue environment, while CD5L, LYZ, and CTSG reflect innate immune or myeloid defense. DPP4, IGF2R, RAB27A, and the cytoskeletal genes may connect extracellular or vesicular material with cell-surface processing, trafficking, adhesion, and remodeling. HPGD could modulate the local prostaglandin environment and thereby influence inflammatory or reproductive-tissue physiology. The hypothesis predicts that the module will weaken after correction for plasma abundance and blood-cell composition, while the tissue-intrinsic component should be most evident in samples with endothelial, epithelial, myeloid, or vascular-interface representation. This is a mechanistic proposal, not an established causal pathway.

### Important genes

#### APOA2

- **Related proteins** (co-abundance neighbors): PRXL2A (0.97), SPTBN2 (0.93), BZW2 (0.90), DPP4 (0.89), GALE (0.87), ITPRID2 (0.85), IDE (0.85), SNRPA1 (0.82); STRING partners: FGA (0.893), ORM1 (0.772)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07432.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_08700.1, huMAP3_07265.1
- **Function (MyGene.info)**: apolipoprotein A2. This gene encodes apolipoprotein (apo-) A-II, which is the second most abundant protein of the high density lipoprotein particles. The protein is found in plasma as a monomer, homodimer, or heterodimer with apolipoprotein D. Defects in this gene may result in apolipoprotein A-II deficiency or hypercholesterolemia. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: apolipoprotein A-II amyloidosis (0.400); amyloidosis (0.382); hypercholesterolemia, familial, 1 (0.341); pancreatic neoplasm (0.096); familial pancreatic carcinoma (0.096)
- **Europe PMC papers**: 8528
- **Why important**: APOA2 is among the most connected genes in the module and links to FGA and ORM1 in STRING. It is liver-enriched, hepatocyte-enriched, and secreted to blood, while its annotations include lipid transport, triglyceride metabolism, phospholipid biology, and negative regulation of cytokine production. Its repeated presence in hu.MAP plasma-protein complexes (hu.MAP huMAP3_07432.1) through (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_08700.1), and (hu.MAP huMAP3_07265.1) makes it a strong marker of the circulating extracellular component. Its large literature base and disease associations with lipid disorders and amyloidosis also make it an experimentally tractable anchor.
- **Conclusion**: Established evidence supports APOA2 as a prominent circulating plasma-protein contributor and a central marker of the module's blood-associated component. It should not be concluded that APOA2 drives the cervical module; its presence may primarily report plasma exposure or shared liver-derived material.

#### FGA

- **Related proteins** (co-abundance neighbors): CD5L (0.90), PODXL (0.87), NAPRT (0.80); STRING partners: APOA2 (0.893), LYZ (0.861), ORM1 (0.747)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07432.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_02242.1, huMAP3_09434.1
- **Function (MyGene.info)**: fibrinogen alpha chain. This gene encodes the alpha subunit of the coagulation factor fibrinogen, which is a component of the blood clot. Following vascular injury, the encoded preproprotein is proteolytically processed by thrombin during the conversion of fibrinogen to fibrin. Mutations in this gene lead to several disorders, including dysfibrinogenemia, hypofibrinogenemia, afibrinogenemia and renal amyloidosis. Alterna…
- **Diseases (Open Targets)**: familial dysfibrinogenemia (0.789); familial visceral amyloidosis (0.765); congenital afibrinogenemia (0.757); familial hypodysfibrinogenemia (0.659); congenital fibrinogen deficiency (0.619)
- **Europe PMC papers**: 7516
- **Why important**: FGA is a major network connector among the annotated plasma proteins and has known STRING relationships with APOA2, ORM1, and LYZ. It is liver- and hepatocyte-enriched, secreted to blood, and encodes the fibrinogen alpha chain, with established roles in coagulation, platelet activation, cell-matrix adhesion, plasminogen activation, and fibrinolysis. It recurs with APOA2 and ORM1 across many hu.MAP complexes (hu.MAP huMAP3_07432.1) through (hu.MAP huMAP3_02242.1) and (hu.MAP huMAP3_09434.1), providing the strongest complex-level support for a plasma and hemostatic submodule. Its extensive disease literature includes inherited fibrinogen disorders and amyloidosis.
- **Conclusion**: Established evidence supports FGA as a key plasma, coagulation, and extracellular-matrix marker within the module. A role in local cervical coagulation or remodeling is plausible but remains a hypothesis because the data do not distinguish locally produced FGA from circulating blood-derived protein.

#### ORM1

- **Related proteins** (co-abundance neighbors): SPTBN2 (0.95), ITPRID2 (0.93); STRING partners: APOA2 (0.772), FGA (0.747)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07432.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_02242.1, huMAP3_08700.1, huMAP3_07265.1, huMAP3_09434.1
- **Function (MyGene.info)**: orosomucoid 1. This gene encodes a key acute phase plasma protein. Because of its increase due to acute inflammation, this protein is classified as an acute-phase reactant.  The specific function of this protein has not yet been determined; however, it may be involved in aspects of immunosuppression. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.102); nephronophthisis (0.088); familial idiopathic steroid-resistant nephrotic syndrome (0.087); colorectal carcinoma (0.083); breast cancer (0.083)
- **Europe PMC papers**: 2436
- **Why important**: ORM1 is liver- and hepatocyte-enriched, secreted to blood, and annotated as an acute-phase plasma protein involved in inflammatory and immune regulation. It connects to APOA2 and FGA in STRING and repeatedly co-occurs with them in hu.MAP plasma-protein complexes (hu.MAP huMAP3_07432.1) through (hu.MAP huMAP3_08700.1), (hu.MAP huMAP3_07265.1), and (hu.MAP huMAP3_09434.1). Its position links the circulating protein component to inflammation, including regulation of interleukin and tumor-necrosis-factor production. The gene has substantial literature and disease associations across inflammatory and systemic disorders.
- **Conclusion**: Established evidence supports ORM1 as an acute-phase and circulating inflammatory marker that helps explain conservation between the two tissue groups. It is not sufficient evidence for an active local inflammatory process in the cervix, because circulating acute-phase protein abundance can generate the same pattern.

#### DPP4

- **Related proteins** (co-abundance neighbors): CD5L (0.99), PODXL (0.92), APOA2 (0.89); STRING partners: IGF2R (0.945)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dipeptidyl peptidase 4. The DPP4 gene encodes dipeptidyl peptidase 4, which is identical to adenosine deaminase complexing protein-2, and to the T-cell activation antigen CD26. It is an intrinsic type II transmembrane glycoprotein and a serine exopeptidase that cleaves X-proline dipeptides from the N-terminus of polypeptides. Dipeptidyl peptidase 4 is highly involved in glucose and insulin metabolism, as well as in immun…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.641); diabetes mellitus (0.621); chronic kidney disease (0.462); myocardial infarction (0.449); neurodegenerative disease (0.438)
- **Europe PMC papers**: 10882
- **Why important**: DPP4 connects CD5L, PODXL, and APOA2 in the co-abundance graph and has a very strong STRING relationship with IGF2R. It is secreted to blood as well as membrane-associated in biology, and its established functions include serine exopeptidase activity, peptide-hormone processing, glucose and insulin metabolism, immune regulation, and receptor-mediated processes. Its HPA profile spans intestinal, placental, and immune-associated cell contexts, including endometrial glandular cells and cytotrophoblasts, which is relevant to a reproductive-tissue and circulation interface. It also has a large literature base and broad metabolic and cardiovascular disease associations.
- **Conclusion**: Established evidence supports DPP4 as a multifunctional extracellular or cell-surface bridge between metabolic, immune, and reproductive-interface biology. Its contribution may be biologically meaningful, but the network does not establish that DPP4 enzymatic activity causes the shared module.

#### LYZ

- **Related proteins** (co-abundance neighbors): SPTBN2 (0.83); STRING partners: CTSG (0.836), FGA (0.861)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Golgi apparatus, Actin filaments; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11343.1
- **Function (MyGene.info)**: lysozyme. This gene encodes human lysozyme, whose natural substrate is the bacterial cell wall peptidoglycan (cleaving the beta[1-4]glycosidic linkages between N-acetylmuramic acid and N-acetylglucosamine). Lysozyme is one of the antimicrobial agents found in human milk, and is also present in spleen, lung, kidney, white blood cells, plasma, saliva, and tears. The protein has antibacterial activity against …
- **Diseases (Open Targets)**: familial visceral amyloidosis (0.619); amyloidosis, hereditary systemic 5 (0.550); Oral ulcer (0.483); AL amyloidosis (0.466); Renal amyloidosis (0.466)
- **Europe PMC papers**: 7506
- **Why important**: LYZ is a canonical secreted antimicrobial and myeloid-associated protein with HPA enrichment in bone marrow and several secretory tissues. It has known STRING relationships with CTSG and FGA and participates with CTSG in hu.MAP complex (hu.MAP huMAP3_11343.1). Its annotations support antimicrobial humoral defense, inflammatory response, and killing of other organisms. The combination of LYZ with CTSG, neutrophil-associated HPA signals, and plasma-linked FGA provides a biologically coherent innate-defense component. Its extensive literature and associations with systemic amyloidosis and inflammatory disease further increase its interpretive importance.
- **Conclusion**: Established evidence supports LYZ as a marker of innate antimicrobial and myeloid or secretory contribution. The module may therefore contain a blood-cell or myeloid-cell signal, but LYZ abundance alone does not prove active infection or inflammation in the cervix.

#### HPGD

- **Related proteins** (co-abundance neighbors): RAB27A (0.95), NAPRT (0.94), CAPZB (0.82), EFHD2 (0.81), HDGF (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 15-hydroxyprostaglandin dehydrogenase. This gene encodes a member of the short-chain nonmetalloenzyme alcohol dehydrogenase protein family. The encoded enzyme is responsible for the metabolism of prostaglandins, which function in a variety of physiologic and cellular processes such as inflammation. Mutations in this gene result in primary autosomal recessive hypertrophic osteoarthropathy and cranioosteoarthropathy. Multiple transcript …
- **Diseases (Open Targets)**: hypertrophic osteoarthropathy, primary, autosomal recessive, 1 (0.756); cranio-osteoarthropathy (0.707); isolated congenital digital clubbing (0.695); primary hypertrophic osteoarthropathy (0.561); hereditary disease (0.193)
- **Europe PMC papers**: 1939
- **Why important**: HPGD is a distinctive non-secreted enzymatic component that connects RAB27A, NAPRT, CAPZB, EFHD2, and HDGF in the module. It is enriched in stomach and urinary bladder tissue contexts and appears in enterocyte, epithelial, trophoblast, and mast-cell contexts. Its established function is prostaglandin metabolism, with links to inflammation, pregnancy, and parturition, making it particularly relevant to a cervix-associated tissue pair. It has disease associations with primary hypertrophic osteoarthropathy and related disorders and a substantial literature base.
- **Conclusion**: Established evidence supports HPGD as a plausible tissue-regulatory and prostaglandin-metabolism component that is less readily explained by simple plasma carryover than APOA2, FGA, or ORM1. Its connection to the shared module may indicate coordinated epithelial, trophoblast, mast-cell, or inflammatory physiology, but a causal role in cervical or circulatory regulation remains hypothetical.

## Module 2

**Tissue pair**: cervix_uterine and circulatory_system  
**Genes (48)**: ACBD5, ARPC1B, ARHGEF1, BOLA2, CTSC, CCDC138, CCDC6, CHMP1B, CGN, CPNE3, CYTH1, DDAH2, DENND2D, DHRS7, DIP2B, DLG1, DNAJB1, ENOPH1, FABP5, FKBP15, FKBP5, GFPT1, GIPC1, GLRX, GNAS, GNAS, EIF4E, IMPA1, KGD4, LTA4H, MACO1, MYO18A, NIT2, NUP35, PACSIN3, PKD1, PLEKHA7, PSMF1, ARHGAP12, ARHGAP27, SNX5, SUCLG2, TAP1, TMOD3, UBAP1, VPS35, WDR26, ZW10

### Function

The strongest interpretation is a heterogeneous intracellular trafficking, epithelial-junction, cytoskeletal-signalling module rather than a single canonical pathway. The only primary GO/KEGG evidence that passed global correction is (GO:MF D1 dopamine receptor binding; q_global = 0.0315), dopamine receptor binding, represented by GNAS, SNX5 and VPS35. This is a narrow molecular-function signal and should not be expanded into a general dopamine pathway claim. Independently, the gene descriptions and network connections support several coherent themes: GNAS and ARHGEF1 connect extracellular or G-protein-coupled signals to small-GTPase regulation; CGN, PLEKHA7, ARHGAP12 and ARHGAP27 support epithelial junction, adhesion, polarity and Rho-regulated cytoskeletal organization; SNX5, VPS35, FKBP15, CHMP1B and UBAP1 support endosomal sorting, retromer function, multivesicular-body biology and membrane trafficking. Other members contribute protein folding, proteostasis, mitochondrial or lipid metabolism. Thus, the module is best viewed as a co-abundance state linking cell-surface organisation and signalling with intracellular trafficking, with dopamine-receptor binding as the only globally corrected functional annotation. No other GO/KEGG term passed global correction; the absence of additional enriched terms does not invalidate the module.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the HPA summary identifies only a small secreted subset, while most annotated proteins are intracellular, membrane-associated or junctional. Most genes have low tissue specificity, and many are cell-type enhanced across epithelial, neural, muscle and myeloid populations. Esophageal apical cells are the most frequent single-cell association, with additional representation of neutrophils, Kupffer cells and microglia. Blood-cell specificity is generally low, although a few genes show immune-cell or lymphoid associations. This argues against interpreting the shared signal simply as a plasma or blood-cell module. It may instead reflect broadly used cellular machinery, epithelial or junctional cell content, and possibly shared contaminating or infiltrating cell states. Protein detection in cervix is widespread among the tested genes, whereas there is no matching HPA tissue for the circulatory-system group, so the HPA comparison cannot establish equivalent protein abundance across the two tissue groups.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF D1 dopamine receptor binding | 0.0315 | GNAS, SNX5, VPS35 |

### STRING and hu.MAP

STRING provides a small set of high-confidence pairwise links rather than broad functional enrichment. The established relationships are CGN–PLEKHA7, CHMP1B–UBAP1, DNAJB1–FKBP5, FKBP15–VPS35 and SNX5–VPS35. These links independently reinforce epithelial junction biology, ESCRT or multivesicular-body processes, chaperone or folding biology, and endosomal-retromer trafficking. hu.MAP also places ARHGAP27 with ARHGAP12 across several related complexes (hu.MAP huMAP3_15300.1) (hu.MAP huMAP3_13005.1) (hu.MAP huMAP3_00279.1) (hu.MAP huMAP3_06265.1) (hu.MAP huMAP3_08948.1) (hu.MAP huMAP3_10120.1), with SHANK3 and, in some complexes, NKX2-5, ASAP proteins or PRR12; and places FKBP15 with VPS35 in a retromer-related complex (hu.MAP huMAP3_13244.1). CHMP1B and UBAP1 occur together in an ESCRT-associated complex (hu.MAP huMAP3_13805.1). These are known molecular relationships embedded within the module, not evidence that every module gene forms one physical complex. The limited number of STRING links and the partial overlap of hu.MAP complexes suggest a modular architecture with several connected functional neighborhoods rather than a single stable macromolecular assembly.

**STRING interactions (score >= 0.7)**: 5 of 1128 gene pairs: CGN–PLEKHA7 (0.884); CHMP1B–UBAP1 (0.938); DNAJB1–FKBP5 (0.936); FKBP15–VPS35 (0.793); SNX5–VPS35 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15300.1 (ARHGAP27, ARHGAP12; 2/3); huMAP3_13005.1 (ARHGAP27, ARHGAP12; 2/4); huMAP3_00279.1 (ARHGAP27, ARHGAP12; 2/5); huMAP3_06265.1 (ARHGAP27, ARHGAP12; 2/6); huMAP3_08948.1 (ARHGAP27, ARHGAP12; 2/6); huMAP3_10120.1 (ARHGAP27, ARHGAP12; 2/7); huMAP3_13244.1 (FKBP15, VPS35; 2/10); huMAP3_13805.1 (CHMP1B, UBAP1; 2/30)

### Novelty

The co-abundance module may be a new tissue-pair-level observation, but the fact sheet does not establish that it is a new biological complex or a previously unknown pathway. Several component relationships and functions are already known from STRING, hu.MAP and curated gene annotations, including junctional scaffolding, Rho regulation, ESCRT biology and retromer trafficking. Conversely, the absence of a STRING enrichment result or the absence of a hu.MAP complex containing most genes cannot prove novelty. The potentially novel result is therefore the reproducible co-abundance coordination of these otherwise partly separate processes across cervix_uterine and circulatory_system. Demonstrating novelty would require replication in independent cohorts, comparison with published tissue co-expression modules, preservation testing, and assessment of cell-composition effects.

**Hypothesis.** Hypothesis: the shared module marks a cell-state program in which epithelial or vascular-interface cells coordinate junctional integrity and actin remodelling with receptor signalling and membrane cargo traffic. GNAS-dependent signalling could influence Rho-family regulators and junctional scaffolds, while SNX5–VPS35, FKBP15, CHMP1B and UBAP1 maintain endosomal recycling, retromer retrieval and multivesicular-body sorting. In this model, the dopamine-receptor-binding signal reflects a receptor-trafficking or signalling component of the state rather than proof that dopamine is the dominant tissue stimulus. The module could also be partly driven by shared epithelial cell content or low-level myeloid admixture. This hypothesis should be tested by cell-type-resolved expression, protein localisation, perturbation of trafficking or junctional genes, and measurement of receptor recycling, barrier integrity and Rho-dependent cytoskeletal responses.

### Important genes

#### CCDC138

- **Related proteins** (co-abundance neighbors): GFPT1 (0.95), SNX5 (0.95), DDAH2 (0.94), GIPC1 (0.93), UBAP1 (0.92), DHRS7 (0.91), DIP2B (0.91), FKBP15 (0.89), LTA4H (0.89), DLG1 (0.88), PSMF1 (0.88), TMOD3 (0.86), MYO18A (0.85), ARPC1B (0.85), ENOPH1 (0.84), GNAS (0.84), GNAS (0.82), GLRX (0.82), ARHGEF1 (0.82), NIT2 (0.82), IMPA1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coiled-coil domain containing 138
- **Diseases (Open Targets)**: Hirsutism (0.316); placental abruption (0.262); benign urinary system neoplasm (0.173); disturbance of skin sensation (0.097); acne (0.069)
- **Europe PMC papers**: 72
- **Why important**: CCDC138 is the principal network hub by weighted connectivity in the supplied graph and links genes from several otherwise distinct neighborhoods, including SNX5, UBAP1, CGN, DDAH2, GIPC1 and metabolic or cytoskeletal genes. It has no assigned globally corrected GO term, no STRING partner and no hu.MAP complex in the fact sheet, so its central position is a co-abundance observation rather than established molecular interaction evidence. Its coiled-coil identity and broad HPA cell-type associations make it a plausible organisational or scaffold-like marker, while its disease and literature support are more limited than those of the established trafficking genes.
- **Conclusion**: Established: CCDC138 is the graph hub and is detected in cervix, with tissue enhancement reported in testis and several cell-type associations. Hypothesis: it may coordinate the module's otherwise disconnected trafficking, junctional and metabolic signals. Its causal role is unproven and requires physical-interaction and perturbation studies.

#### CGN

- **Related proteins** (co-abundance neighbors): GIPC1 (0.91), KGD4 (0.90), ARHGAP27 (0.89), CHMP1B (0.86), CTSC (0.84), UBAP1 (0.83), DIP2B (0.83), LTA4H (0.83), TAP1 (0.82), ARHGEF1 (0.82), EIF4E (0.82), PSMF1 (0.82), DNAJB1 (0.81); STRING partners: PLEKHA7 (0.884)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cingulin. Enables cadherin binding activity. Predicted to act upstream of or within bicellular tight junction assembly; epithelial cell morphogenesis; and microtubule cytoskeleton organization. Located in bicellular tight junction and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.359); nonsyndromic deafness (0.118); skin disorder (0.094); colorectal carcinoma (0.086); ovarian carcinoma (0.065)
- **Europe PMC papers**: 3593
- **Why important**: CGN is a relatively central connector and has a direct high-confidence STRING relationship with PLEKHA7. Its annotated functions include cadherin binding, bicellular tight-junction assembly, epithelial morphogenesis and microtubule organisation, while its HPA localisation includes plasma membrane and cell junctions. It is tissue enhanced in intestine and appears in several epithelial cell types, fitting the epithelial-interface interpretation. CGN also has substantial literature support and disease links involving skeletal, auditory and epithelial or neoplastic phenotypes.
- **Conclusion**: Established: CGN is a junction-associated epithelial scaffold with a known PLEKHA7 relationship and strong support for adhesion and cytoskeletal functions. Hypothesis: it may anchor the shared module at epithelial junctions and couple junctional state to trafficking and Rho signalling. The module does not establish that CGN drives the cross-tissue pattern.

#### GNAS

- **Related proteins** (co-abundance neighbors): GNAS (0.99), PKD1 (0.83), CCDC138 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GNAS complex locus. This locus has a highly complex imprinted expression pattern. It gives rise to maternally, paternally, and biallelically expressed transcripts that are derived from four alternative promoters and 5' exons. Some transcripts contain a differentially methylated region (DMR) at their 5' exons, and this DMR is commonly found in imprinted genes and correlates with transcript expression. An antisense tra…
- **Diseases (Open Targets)**: pseudohypoparathyroidism type 1A (0.839); pseudohypoparathyroidism type 1C (0.816); McCune-Albright syndrome (0.811); Albright hereditary osteodystrophy (0.798); pseudohypoparathyroidism type 1B (0.797)
- **Europe PMC papers**: 10304
- **Why important**: GNAS is one of the three genes in the only globally corrected term (GO:MF D1 dopamine receptor binding; q_global = 0.0315), dopamine receptor binding, and its annotation supports G-protein-coupled receptor signalling and intracellular homeostasis. It is connected in the module to PKD1 and CCDC138 and is associated in HPA with platelets and endocrine cell types, although its overall tissue specificity is low. GNAS has extensive literature and strong disease associations involving pseudohypoparathyroidism and McCune-Albright syndrome, making it the most established signalling regulator among the selected genes.
- **Conclusion**: Established: GNAS is a broadly important, imprinted signalling locus and contributes to (GO:MF D1 dopamine receptor binding; q_global = 0.0315). Hypothesis: GNAS-mediated receptor signalling may help couple extracellular cues to junctional remodelling or endosomal trafficking in this module. The enrichment does not demonstrate dopamine dependence in either tissue.

#### SNX5

- **Related proteins** (co-abundance neighbors): CCDC138 (0.95); STRING partners: VPS35 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sorting nexin 5. This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. This protein functions in endosomal sorting, the phosphoinositide-signaling pathway, and macropinocytosis. This gene may play a role in the tumorigenesis of papillary thyroid carcinoma. Alternative spli…
- **Diseases (Open Targets)**: drug allergy (0.201); Parkinson disease (0.095); hypothyroidism (0.093); nonpapillary renal cell carcinoma (0.078); head and neck squamous cell carcinoma (0.075)
- **Europe PMC papers**: 1362
- **Why important**: SNX5 is a member of (GO:MF D1 dopamine receptor binding; q_global = 0.0315) and has the strongest supplied STRING relationship, with VPS35. Its established sorting-nexin function in phosphoinositide-dependent endosomal sorting, intercellular transport and receptor or cargo handling gives the module a concrete trafficking mechanism. HPA places it in vesicles and cytosol and associates it with Hofbauer and Kupffer cells. Its literature volume and disease associations are more modest than those of GNAS or VPS35, but its network and annotation position is mechanistically specific.
- **Conclusion**: Established: SNX5 participates in endosomal sorting and is tightly linked to VPS35 in STRING; it also contributes to (GO:MF D1 dopamine receptor binding; q_global = 0.0315). Hypothesis: SNX5 may connect receptor handling, including dopamine-receptor-related cargo, to the broader shared module. Direct receptor-specific involvement is not demonstrated.

#### VPS35

- **Related proteins** (co-abundance neighbors): PKD1 (0.91); STRING partners: FKBP15 (0.793), SNX5 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_13244.1
- **Function (MyGene.info)**: VPS35 retromer complex component. This gene belongs to a group of vacuolar protein sorting (VPS) genes. The encoded protein is a component of a large multimeric complex, termed the retromer complex, involved in retrograde transport of proteins from endosomes to the trans-Golgi network. The close structural similarity between the yeast and human proteins that make up this complex suggests a similarity in function. Expression studie…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.743); neurodegenerative disease (0.553); young-onset Parkinson disease (0.503); Parkinson disease (0.482); Parkinson disease, dominant (0.370)
- **Europe PMC papers**: 3611
- **Why important**: VPS35 is a core retromer component and is included in (GO:MF D1 dopamine receptor binding; q_global = 0.0315). It is linked by STRING to SNX5 and FKBP15 and appears with FKBP15 in hu.MAP complex (hu.MAP huMAP3_13244.1). Its established roles in retrograde endosome-to-Golgi transport, lysosome organisation and signal regulation provide a strong mechanistic bridge between receptor trafficking and cellular homeostasis. VPS35 also has substantial literature and well-established associations with late-onset and dominant forms of Parkinson disease.
- **Conclusion**: Established: VPS35 is a retromer-associated trafficking protein supported by STRING, hu.MAP and (GO:MF D1 dopamine receptor binding; q_global = 0.0315). Hypothesis: retromer-dependent recycling may be a central process maintaining the shared tissue module and could couple receptor availability to junctional or cytoskeletal state. The co-abundance data alone do not show that VPS35 is the module's causal regulator.
