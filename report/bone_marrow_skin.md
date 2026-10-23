# Conserved co-abundance modules: bone_marrow and skin

## Module 0

**Tissue pair**: bone_marrow and skin  
**Genes (41)**: BZW2, NUDT1, ADAM10, ALG6, ASPH, BABAM2, CADM1, CARMIL1, CNDP2, CUSTOS, DCTN5, DNM2, EHMT2, FN1, HDGFL3, KIF13B, KIF2C, LNPEP, LMCD1, MDC1, MED8, MMS19, IGF2R, NT5DC2, NUP93, OTUD7B, PHIP, PLEKHM2, RB1, REPS1, RIPK2, MRPL1, GINS4, SPTBN1, SPTAN1, CCDC59, TLN1, TRPT1, UBAC2, VPS37A, ZNF830

### Function

The best-supported function is cytoskeletal and membrane-remodelling activity, particularly microtubule and actin-associated protein turnover, cell adhesion, intracellular transport, and cell communication. The primary GO evidence is (GO:BP protein depolymerization; q_global = 0.034), protein depolymerization, supported by ASPH, CARMIL1, HDGFL3, KIF2C, SPTAN1, and SPTBN1. This term connects microtubule depolymerization through KIF2C and HDGFL3 with actin or membrane scaffolding through CARMIL1 and the spectrin pair. Supplementary STRING evidence supports cell communication and a TROP2 regulatory-signaling association (STRING WikiPathways TROP2 regulatory signaling; within-query FDR = 0.0048)(STRING Process Cell communication; within-query FDR = 0.0399), but these are not global enrichment evidence. Overall, the module is most consistent with a shared structural, trafficking, and signaling state rather than a narrowly defined pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins. FN1 is secreted to blood and provides an extracellular-matrix component, while ADAM10 and LNPEP have intracellular or membrane-associated secretome annotations. Most genes have low tissue specificity, indicating a substantial broadly expressed or housekeeping-like component. Immune-cell specificity is also low for most genes, although selected genes show enhancement in neutrophils, dendritic cells, lymphoid populations, or progenitor populations. HPA evidence therefore supports a mixed module rather than a pure blood-cell signature. The shared signal could nevertheless reflect common stromal, vascular, epithelial, or immune-associated cell types present in both bone marrow and skin. The stronger representation of protein detection in skin than bone marrow should also be considered when interpreting the cross-tissue association.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP protein depolymerization | 0.034 | ASPH, CARMIL1, HDGFL3, KIF2C, SPTAN1, SPTBN1 |

### STRING and hu.MAP

The strongest known STRING relationship is FN1-TLN1, linking extracellular matrix to integrin-associated cytoskeletal adhesion. The other high-confidence STRING relationship is SPTAN1-SPTBN1, an established alpha- and beta-spectrin scaffold pair. These relationships show that at least part of the module recovers known structural biology rather than being entirely unexplained. STRING also places ADAM10, IGF2R, RB1, FN1, and TLN1 in the supplementary TROP2 regulatory-signaling association (STRING WikiPathways TROP2 regulatory signaling; within-query FDR = 0.0048), and assigns a broader cell communication signal (STRING Process Cell communication; within-query FDR = 0.0399). The hu.MAP evidence provides partial complex support for the spectrin pair (hu.MAP huMAP3_07940.1)(hu.MAP huMAP3_05473.1)(hu.MAP huMAP3_09165.1), MDC1 with PHIP (hu.MAP huMAP3_12288.1)(hu.MAP huMAP3_14365.1), CARMIL1 with DCTN5 (hu.MAP huMAP3_12900.1), ADAM10 with IGF2R (hu.MAP huMAP3_06775.1), and DNM2 with BZW2 (hu.MAP huMAP3_11232.1). Because each hu.MAP complex contains many members outside the module, these results support biological compatibility but not a single complete complex encompassing the module.

**STRING interactions (score >= 0.7)**: 2 of 820 gene pairs: FN1–TLN1 (0.992); SPTAN1–SPTBN1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: WikiPathways TROP2 regulatory signaling (FDR = 0.0048, 5 genes); Process Cell communication (FDR = 0.0399, 22 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12288.1 (MDC1, PHIP; 2/3); huMAP3_07940.1 (SPTBN1, SPTAN1; 2/5); huMAP3_14365.1 (MDC1, PHIP; 2/7); huMAP3_05473.1 (SPTBN1, SPTAN1; 2/7); huMAP3_09042.1 (NUP93, MMS19; 2/26); huMAP3_09165.1 (SPTBN1, SPTAN1; 2/39); huMAP3_12900.1 (CARMIL1, DCTN5; 2/50); huMAP3_06775.1 (ADAM10, IGF2R; 2/60); huMAP3_11232.1 (DNM2, BZW2; 2/78)

### Novelty

This module should not be described as a wholly new molecular pathway. The FN1-TLN1 interaction, the SPTAN1-SPTBN1 spectrin pair, cytoskeletal roles of CARMIL1 and KIF2C, and signaling or trafficking functions of RIPK2, ADAM10, and IGF2R are established in the fact sheet. The potentially novel aspect is the cross-tissue co-abundance organization of these genes in bone marrow and skin, especially the way structural, trafficking, immune, and cell-cycle-related genes are combined. However, the available evidence does not establish that this exact module has not been reported elsewhere. Limited STRING connectivity and partial hu.MAP overlap make the module biologically plausible, but database absence cannot by itself demonstrate novelty. The appropriate conclusion is a potentially useful tissue-pair-specific co-abundance observation requiring independent replication.

**Hypothesis.** Hypothesis: the module represents a shared cell-state program in which cytoskeletal remodelling and membrane trafficking coordinate adhesion, migration, receptor processing, and stress or immune signaling in cells present in both bone marrow and skin. The SPTAN1-SPTBN1 scaffold and FN1-TLN1 adhesion axis could provide structural support, while KIF2C, CARMIL1, DNM2, PLEKHM2, and related trafficking genes could remodel microtubules, actin networks, and lysosome or vesicle positioning. RIPK2 and ADAM10 could connect this structural state to inflammatory or receptor-signaling inputs. This is a mechanistic hypothesis, not a demonstrated causal pathway; the co-abundance data do not establish physical interaction, directionality, or cell-type origin.

### Important genes

#### PLEKHM2

- **Related proteins** (co-abundance neighbors): DCTN5 (0.94), LMCD1 (0.88), CARMIL1 (0.85), MMS19 (0.83), NUDT1 (0.82), GINS4 (0.82), CNDP2 (0.81), BABAM2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pleckstrin homology and RUN domain containing M2. This gene encodes a protein that binds the plus-end directed microtubule motor protein kinesin, together with the lysosomal GTPase Arl8, and is required for lysosomes to distribute away from the microtubule-organizing center. The encoded protein belongs to the multisubunit BLOC-one-related complex that regulates lysosome positioning. It binds a Salmonella effector protein called Salmonella induced…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.388); dilated cardiomyopathy (0.194); autosomal recessive dilated cardiomyopathy (0.192); diabetes mellitus (0.172); aortic stenosis (0.166)
- **Europe PMC papers**: 280
- **Why important**: PLEKHM2 is the most central network gene in the supplied graph and connects trafficking, lysosome positioning, CARMIL1, MMS19, NUDT1, GINS4, and other module members. Its annotation links it to kinesin-dependent lysosome distribution, the BLOC-one-related complex, Golgi organization, and natural-killer-cell cytotoxicity. Its neutrophil-enhanced HPA profile and substantial literature support make it a strong candidate for coordinating the module's trafficking and immune-associated signals, despite lacking STRING or hu.MAP support here.
- **Conclusion**: Established evidence supports PLEKHM2 as a lysosome-positioning and intracellular transport regulator with a central position in this module. It is a plausible organizing candidate, but its role in the shared bone-marrow and skin co-abundance state remains a hypothesis.

#### RIPK2

- **Related proteins** (co-abundance neighbors): HDGFL3 (0.90), ASPH (0.87), DCTN5 (0.86), EHMT2 (0.83), VPS37A (0.82), CUSTOS (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: receptor interacting serine/threonine kinase 2. This gene encodes a member of the receptor-interacting protein (RIP) family of serine/threonine protein kinases. The encoded protein contains a C-terminal caspase activation and recruitment domain (CARD), and is a component of signaling complexes in both the innate and adaptive immune pathways. It is a potent activator of NF-kappaB and inducer of apoptosis in response to various stimuli. [provided…
- **Diseases (Open Targets)**: leprosy (0.459); Abnormality of the skeletal system (0.364); Crohn disease (0.355); neurodegenerative disease (0.344); Precordial pain (0.294)
- **Europe PMC papers**: 3294
- **Why important**: RIPK2 has one of the stronger network positions and connects to HDGFL3, ASPH, DCTN5, EHMT2, VPS37A, and CUSTOS. It is a CARD-containing kinase involved in innate and adaptive immune signaling, NF-kappaB activation, cytokine production, inflammation, and apoptosis. It also contributes to the supplementary cell communication evidence (STRING Process Cell communication; within-query FDR = 0.0399) and has disease associations including leprosy and Crohn disease, with substantial literature volume.
- **Conclusion**: Established evidence supports RIPK2 as an immune and inflammatory signaling component. Its placement in this module suggests that immune signaling may be coupled to cytoskeletal or trafficking changes, but the co-abundance data do not prove that RIPK2 drives the module.

#### FN1

- **Related proteins** (co-abundance neighbors): EHMT2 (0.87), MED8 (0.86), MDC1 (0.83); STRING partners: TLN1 (0.992)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 is the clearest extracellular-matrix representative and is secreted to blood. It is involved in adhesion, migration, wound healing, coagulation, host defense, and integrin-mediated signaling. It has a direct high-confidence STRING relationship with TLN1 and appears in both supplementary STRING signals (STRING WikiPathways TROP2 regulatory signaling; within-query FDR = 0.0048)(STRING Process Cell communication; within-query FDR = 0.0399). Its HPA profile includes blood vessel, liver, placenta, fibroblast, and hepatic stellate-cell enrichment, and it is detected in both relevant tissues.
- **Conclusion**: Established evidence supports FN1 as an extracellular scaffold and adhesion component that can connect tissue matrix to cell signaling. In this module it may mark stromal or vascular contribution, but it could also reflect shared tissue composition rather than a cell-intrinsic module mechanism.

#### SPTAN1

- **Related proteins** (co-abundance neighbors): SPTBN1 (0.90), ALG6 (0.80); STRING partners: SPTBN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Microtubules; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: huMAP3_07940.1, huMAP3_05473.1, huMAP3_09165.1
- **Function (MyGene.info)**: spectrin alpha, non-erythrocytic 1. Spectrins are a family of filamentous cytoskeletal proteins that function as essential scaffold proteins that stabilize the plasma membrane and organize intracellular organelles. Spectrins are composed of alpha and beta dimers that associate to form tetramers linked in a head-to-head arrangement. This gene encodes an alpha spectrin that is specifically expressed in nonerythrocytic cells. The encod…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 5 (0.749); developmental delay with or without epilepsy (0.681); spastic paraplegia 91, autosomal dominant, with or without cerebellar ataxia (0.681); infantile spasms (0.651); genetic developmental and epileptic encephalopathy (0.651)
- **Europe PMC papers**: 1422
- **Why important**: SPTAN1 is part of the only spectrin pair in the module and forms a very strong STRING relationship with SPTBN1. Both genes contribute to the globally supported protein-depolymerization term (GO:BP protein depolymerization; q_global = 0.034), and both occur together in several hu.MAP complexes (hu.MAP huMAP3_07940.1)(hu.MAP huMAP3_05473.1)(hu.MAP huMAP3_09165.1). SPTAN1 is a non-erythrocytic membrane and organelle scaffold involved in actin-cytoskeleton organization, with disease associations including developmental epileptic encephalopathy and spastic paraplegia.
- **Conclusion**: Established evidence supports SPTAN1 as a structural cytoskeletal scaffold and supports its partnership with SPTBN1. This pair is one of the most convincing mechanistic anchors of the module, although the module-wide role still requires experimental validation.

#### KIF2C

- **Related proteins** (co-abundance neighbors): CCDC59 (0.81), EHMT2 (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Immune cell enhanced; location Nucleoplasm, Midbody, Centrosome; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 2C. This gene encodes a kinesin-like protein that functions as a microtubule-dependent molecular motor. The encoded protein can depolymerize microtubules at the plus end, thereby promoting mitotic chromosome segregation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.320); Abnormality of the skeletal system (0.165); placenta praevia (0.159); neuroendocrine neoplasm (0.159); placental retention (0.129)
- **Europe PMC papers**: 2214
- **Why important**: KIF2C is one of the genes contributing directly to (GO:BP protein depolymerization; q_global = 0.034). It is a microtubule motor and depolymerase that promotes chromosome segregation, metaphase alignment, and microtubule-cytoskeleton polarity. HPA places it in a bone-marrow, lymphoid, and testis-enriched tissue pattern and shows enhancement in a T-regulatory cell type. Its network position links it to CCDC59 and EHMT2, connecting the cytoskeletal signal to cell-cycle and chromatin-related components.
- **Conclusion**: Established evidence supports KIF2C as a microtubule-remodelling and mitotic regulator, with a particularly relevant bone-marrow association. Its presence could indicate proliferating hematopoietic cells or a broader cytoskeletal state; the data do not distinguish these possibilities.

## Module 1

**Tissue pair**: bone_marrow and skin  
**Genes (40)**: NT5E, AFDN, AHR, AKAP1, ARSA, BIN1, CACNG6, CDK13, CHMP1A, CASK, CSTF2T, PDF, ECE1, EHMT1, ERCC6L, ERLIN1, HMMR, IGF2BP1, KDM5C, PRKD2, RPS6KB1, MLST8, METTL16, MAP2K6, CDC42BPA, NEK7, NFXL1, NVL, CRYZL1, QTRT2, RBM7, SCD, SLC25A24, SRCAP, STK3, GTF2A2, THOC6, TPX2, TXNL4A, ZGPAT

### Function

The best-supported function is a coordinated protein-serine and protein-serine/threonine kinase program. Both globally corrected terms, (GO:MF protein serine kinase activity; q_global = 0.0142) and (GO:MF protein serine/threonine kinase activity; q_global = 0.0312), identify the same kinase-containing subset: CASK, CDC42BPA, CDK13, MAP2K6, NEK7, PRKD2, RPS6KB1, and STK3. The concordance between the primary GO evidence and the independent STRING annotations (STRING SMART Serine/Threonine protein kinases, catalytic domain; within-query FDR = 0.00035) through (STRING InterPro Protein kinase-like domain superfamily; within-query FDR = 0.029) makes kinase activity the most defensible module-level interpretation. The broader gene set also connects this signal to stress and inflammatory signaling through MAP2K6, nutrient-responsive growth signaling through RPS6KB1 and MLST8, cytoskeletal and migratory regulation through CDC42BPA and HMMR, mitotic spindle organization through NEK7, HMMR, and TPX2, and transcriptional or RNA-processing control through genes such as RBM7, TXNL4A, and METTL16. The two primary terms substantially overlap, so they should be treated as convergent evidence for one kinase-centered program rather than as separate biological functions.

**Cell composition.** This does not look like a plasma-protein or secreted-protein module: the HPA summary identifies only a minority of genes as secreted, and most proteins are intracellular or membrane-associated. Many genes have low tissue specificity, while others are enhanced in bone marrow, skeletal muscle, lymphoid tissue, or multiple unrelated tissues. Several genes show immune-cell enhancement or enrichment, including associations with neutrophils, T-reg cells, B cells, NK cells, basophils, and monocytes, but the module is not dominated by immune-cell-specific genes. Protein detection is broadly observed in both bone marrow and skin for the genes with available HPA evidence. Thus, the shared signal may reflect a conserved intracellular program present in overlapping stromal, epithelial, progenitor, or immune-associated cell populations rather than a circulating plasma signature. The mixed skeletal-muscle, reproductive, neural, liver, and immune HPA patterns also caution against assigning the module to one specific cell type without cell-resolved validation.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF protein serine kinase activity | 0.0142 | CASK, CDC42BPA, CDK13, MAP2K6, NEK7, PRKD2, RPS6KB1, STK3 |
| GO:MF protein serine/threonine kinase activity | 0.0312 | CASK, CDC42BPA, CDK13, MAP2K6, NEK7, PRKD2, RPS6KB1, STK3 |

### STRING and hu.MAP

The high-confidence STRING network provides only a sparse set of direct relationships within the module. HMMR–TPX2 supports a known connection between a mitotic or microtubule-associated factor and a spindle nucleation factor. MLST8–RPS6KB1 supports the established TOR-associated growth-signaling relationship. IGF2BP1–METTL16 links RNA regulation and RNA modification, although it is not a kinase interaction. STRING functional annotations (STRING SMART Serine/Threonine protein kinases, catalytic domain; within-query FDR = 0.00035) through (STRING InterPro Protein kinase-like domain superfamily; within-query FDR = 0.029) independently recognize the kinase-domain and serine/threonine-kinase subset, while (STRING Function Protein kinase activator activity; within-query FDR = 0.0438) additionally links TPX2, STK3, MLST8, and MAP2K6 to kinase activation. In hu.MAP, TXNL4A and ZGPAT occur together in the spliceosomal complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1), and ARSA and ECE1 occur together in (hu.MAP huMAP3_09327.1). These pairs are only small representations of much larger complexes, so they establish known complex membership more than a module-specific physical assembly. Overall, the co-abundance structure is much denser than the directly catalogued physical interaction structure, suggesting that shared regulation, cell state, or pathway activity may be driving the module.

**STRING interactions (score >= 0.7)**: 3 of 780 gene pairs: HMMR–TPX2 (0.979); IGF2BP1–METTL16 (0.729); MLST8–RPS6KB1 (0.991)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Serine/Threonine protein kinases, catalytic domain (FDR = 0.00035, 8 genes); Keyword Serine/threonine-protein kinase (FDR = 0.0067, 8 genes); Function Protein serine kinase activity (FDR = 0.0184, 8 genes); InterPro Protein kinase domain (FDR = 0.0229, 8 genes); InterPro Protein kinase, ATP binding site (FDR = 0.0229, 7 genes); Function Protein serine/threonine kinase activity (FDR = 0.0265, 8 genes); InterPro Protein kinase-like domain superfamily (FDR = 0.029, 8 genes); Function Protein kinase activator activity (FDR = 0.0438, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06511.1 (TXNL4A, ZGPAT; 2/79); huMAP3_09327.1 (ARSA, ECE1; 2/93); huMAP3_08980.1 (TXNL4A, ZGPAT; 2/97)

### Novelty

The module-level finding is plausibly novel, but it cannot be called a newly discovered molecular complex. The kinase enrichment is well established from GO and STRING, and several individual relationships and complex memberships are already known. What may be new is the conserved co-abundance combination across bone marrow and skin, especially the joint behavior of kinase, growth-control, mitotic, RNA-processing, metabolic, and membrane-associated genes. The sparse direct STRING connectivity and limited within-module representation in hu.MAP argue against the module being a previously documented physical complex. However, absence from those databases does not prove novelty, because co-abundance relationships can reflect shared regulation, context, cell composition, or interactions not yet curated. The appropriate conclusion is a potentially novel cross-tissue regulatory module built from partly known biological components.

**Hypothesis.** Hypothesis: this module represents a conserved cell-state program in which stress, inflammatory, and nutrient signals converge on serine/threonine kinases to coordinate growth, survival, cytoskeletal remodeling, RNA handling, and cell division in cells represented in both bone marrow and skin. MAP2K6 could transmit stress or inflammatory inputs through p38 signaling; RPS6KB1 and MLST8 could couple nutrient or TOR activity to protein synthesis and growth; CDC42BPA, CASK, and STK3 could organize membrane, adhesion, cytoskeletal, or apoptotic responses; and NEK7, HMMR, and TPX2 could support proliferative or spindle-associated states. The observed co-abundance may therefore reflect coordinated cell-state regulation rather than direct binding among all module members. This model should be tested by cell-type-resolved expression, perturbation of the kinase components, and measurement of pathway activity rather than transcript abundance alone.

### Important genes

#### MAP2K6

- **Related proteins** (co-abundance neighbors): METTL16 (0.89), PRKD2 (0.85), CACNG6 (0.84), CDK13 (0.83), NEK7 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitogen-activated protein kinase kinase 6. This gene encodes a member of the dual specificity protein kinase family, which functions as a mitogen-activated protein (MAP) kinase kinase. MAP kinases, also known as extracellular signal-regulated kinases (ERKs), act as an integration point for multiple biochemical signals. This protein phosphorylates and activates p38 MAP kinase in response to inflammatory cytokines or environmental stress. As…
- **Diseases (Open Targets)**: neurodegenerative disease (0.504); osteoarthritis, hip (0.493); osteoarthritis, knee (0.482); osteoarthritis (0.460); Abnormality of the skeletal system (0.425)
- **Europe PMC papers**: 1961
- **Why important**: MAP2K6 is a relatively central node in the co-abundance graph and is one of the genes present in both primary kinase terms (GO:MF protein serine kinase activity; q_global = 0.0142) and (GO:MF protein serine/threonine kinase activity; q_global = 0.0312) and in the broad STRING kinase evidence (STRING SMART Serine/Threonine protein kinases, catalytic domain; within-query FDR = 0.00035) through (STRING Function Protein kinase activator activity; within-query FDR = 0.0438). Its established function is a MAP kinase kinase that activates p38 in response to inflammatory cytokines and environmental stress. Its annotations include MAPK signaling, stress-activated signaling, osteoblast differentiation, and receptor-linked inflammatory signaling. HPA shows enhancement in intestine and skeletal muscle and cell-type enhancement in adipocytes, myonuclei, kidney cells, and neutrophil-related populations. Its disease associations include osteoarthritis and skeletal-system abnormalities, making it particularly relevant to a bone-marrow and skin comparison.
- **Conclusion**: Established conclusion: MAP2K6 is a strong mechanistic anchor for a stress-responsive kinase interpretation and connects the module to inflammatory and skeletal biology. Hypothesis: its activity may help synchronize tissue stress responses across marrow-associated and skin-associated cell states.

#### RPS6KB1

- **Related proteins** (co-abundance neighbors): AKAP1 (0.85), SLC25A24 (0.85), AHR (0.84); STRING partners: MLST8 (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein S6 kinase B1. This gene encodes a member of the ribosomal S6 kinase family of serine/threonine kinases. The encoded protein responds to mTOR (mammalian target of rapamycin) signaling to promote protein synthesis, cell growth, and cell proliferation. Activity of this gene has been associated with human cancer. Alternatively spliced transcript variants have been observed. The use of alternative translation start …
- **Diseases (Open Targets)**: neurodegenerative disease (0.514); autoimmune disorder of central nervous system (0.370); hypertensive disorder (0.230); hypertrophic cardiomyopathy (0.194); type 2 diabetes mellitus (0.178)
- **Europe PMC papers**: 13203
- **Why important**: RPS6KB1 is a confirmed serine/threonine kinase in (GO:MF protein serine kinase activity; q_global = 0.0142) and (GO:MF protein serine/threonine kinase activity; q_global = 0.0312), is repeatedly recognized by STRING kinase annotations (STRING SMART Serine/Threonine protein kinases, catalytic domain; within-query FDR = 0.00035) through (STRING InterPro Protein kinase-like domain superfamily; within-query FDR = 0.029), and has a direct high-confidence STRING relationship with MLST8. Its established role is downstream of mTOR signaling, promoting protein synthesis, cell growth, and cell proliferation. Its biological-process annotations include TOR signaling, nutrient response, peptidyl-serine phosphorylation, and cell-cycle transition. The direct MLST8 relationship provides the clearest physical link in the module to a recognized growth-control complex. RPS6KB1 also has a large literature base and disease associations spanning neurodegenerative, autoimmune, hypertrophic, and metabolic disorders.
- **Conclusion**: Established conclusion: RPS6KB1 identifies a nutrient- and growth-responsive arm of the module and has particularly strong support from both annotation and physical-interaction evidence. Hypothesis: TOR-linked translational control may be one mechanism coupling the module to tissue remodeling or cellular recovery.

#### CASK

- **Related proteins** (co-abundance neighbors): EHMT1 (0.92), NEK7 (0.89), IGF2BP1 (0.89), ERLIN1 (0.87), ZGPAT (0.85), AFDN (0.84), TXNL4A (0.83), CHMP1A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium/calmodulin dependent serine protein kinase. This gene encodes a calcium/calmodulin-dependent serine protein kinase. The encoded protein is a MAGUK (membrane-associated guanylate kinase) protein family member. These proteins are scaffold proteins and the encoded protein is located at synapses in the brain. Mutations in this gene are associated with FG syndrome 4, intellectual disability and microcephaly with pontine and cerebellar hypoplasia…
- **Diseases (Open Targets)**: syndromic X-linked intellectual disability Najm type (0.829); FG syndrome 4 (0.800); cask-related x-linked intellectual disability (0.667); FG syndrome (0.567); hereditary disease (0.531)
- **Europe PMC papers**: 3838
- **Why important**: CASK has the strongest network position in the module and belongs to both primary kinase terms (GO:MF protein serine kinase activity; q_global = 0.0142) and (GO:MF protein serine/threonine kinase activity; q_global = 0.0312) as well as the corresponding STRING kinase annotations. It encodes a calcium/calmodulin-dependent serine protein kinase and a MAGUK-family scaffold, providing a plausible bridge between enzymatic signaling, membrane organization, and intracellular localization. Its neighbors include NEK7, IGF2BP1, ERLIN1, ZGPAT, AFDN, TXNL4A, and CHMP1A, connecting the central network region to mitotic, RNA-processing, adhesion, endoplasmic-reticulum, and trafficking-related genes. Its disease associations include several forms of X-linked intellectual disability and microcephaly, and it has extensive literature support.
- **Conclusion**: Established conclusion: CASK is the principal network scaffold-like kinase candidate and supports a multi-process signaling interpretation rather than a narrowly defined kinase pathway. Hypothesis: CASK may help couple calcium-sensitive or membrane-proximal signals to the broader co-abundance program.

#### NEK7

- **Related proteins** (co-abundance neighbors): CASK (0.89), CDC42BPA (0.88), MAP2K6 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NIMA related kinase 7. NIMA-related kinases share high amino acid sequence identity with the gene product of the Aspergillus nidulans 'never in mitosis A' gene, which controls initiation of mitosis.[supplied by OMIM, Jul 2002].
- **Diseases (Open Targets)**: lymphatic system disorder (0.405); vein disorder (0.405); Varicose veins (0.387); refractive error (0.340); neurodegenerative disease (0.339)
- **Europe PMC papers**: 2199
- **Why important**: NEK7 is present in both globally corrected kinase terms (GO:MF protein serine kinase activity; q_global = 0.0142) and (GO:MF protein serine/threonine kinase activity; q_global = 0.0312) and in the STRING kinase evidence (STRING SMART Serine/Threonine protein kinases, catalytic domain; within-query FDR = 0.00035) through (STRING InterPro Protein kinase-like domain superfamily; within-query FDR = 0.029). It is connected in the module to CASK, CDC42BPA, and MAP2K6, placing it at the intersection of kinase signaling, cytoskeletal regulation, and stress signaling. Its established annotations include protein phosphorylation, mitotic-cell-cycle regulation, spindle assembly, and regulation of kinase activity. HPA reports enhancement in heart muscle and cell-type enhancement in adrenal and neutrophil populations. Its disease associations include lymphatic and vascular disorders.
- **Conclusion**: Established conclusion: NEK7 contributes a cell-division and spindle-regulatory dimension to the module and is consistent with a proliferative or progenitor-associated cell state. Hypothesis: NEK7 may coordinate stress-responsive kinase activity with cell-cycle progression in the shared tissues.

#### HMMR

- **Related proteins** (co-abundance neighbors): AKAP1 (0.84), ERCC6L (0.82), STK3 (0.81); STRING partners: TPX2 (0.979)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Microtubules; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hyaluronan mediated motility receptor. The protein encoded by this gene is involved in cell motility. It is expressed in breast tissue and together with other proteins, it forms a complex with BRCA1 and BRCA2, thus is potentially associated with higher risk of breast cancer. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene. [provided by RefSeq, Dec 2008].
- **Diseases (Open Targets)**: ovarian cancer (0.342); thyroid gland carcinoma (0.306); alcohol drinking (0.298); Alzheimer disease (0.279); Parkinson disease (0.279)
- **Europe PMC papers**: 2289
- **Why important**: HMMR is one of the more connected non-kinase genes and has the strongest direct STRING relationship in the module, with TPX2. Its established function concerns cell motility, hyaluronan-related processes, and receptor-mediated endocytosis, while its location is associated with microtubules. Its module neighbors include AKAP1, ERCC6L, and STK3, linking mitochondrial anchoring, chromosome or DNA-related cell-cycle processes, and kinase signaling. HPA shows tissue enhancement in bone marrow and lymphoid tissue and immune-cell enhancement in T-reg cells, which is especially relevant to the tissue pair. It also has substantial literature and cancer-related disease associations.
- **Conclusion**: Established conclusion: HMMR provides a biologically plausible bridge between the module's co-abundance pattern and microtubule, motility, marrow, and lymphoid biology. Hypothesis: the HMMR–TPX2 relationship may mark a proliferative or migratory subprogram embedded within the broader kinase module.

## Module 2

**Tissue pair**: bone_marrow and skin  
**Genes (36)**: A2M, PRKAG1, AP1S1, BTAF1, CAMSAP1, CCNB1, ESS2, MACROH2A2, EIF4E, INTS13, IPO4, PRKCI, LIN7C, LYRM4, MAP1A, EEF1E1, ATF7IP, MGME1, NEDD1, PAWR, PNKP, RANBP3, RBM15B, RNF25, POLR3A, POLR3D, MRPS33, SIRT5, SMARCD1, SNAP23, TASOR, TBC1D2B, GTF3C1, TPRKB, TTC38, ZC3HAV1

### Function

No GO or KEGG term passed global multiple-testing correction, so the module should not be assigned a significantly enriched pathway on that basis. Its gene-level evidence instead points to a heterogeneous cellular maintenance program involving RNA polymerase III transcription, chromatin and transcriptional regulation, mitochondrial genome and protein maintenance, cytoskeletal organization, vesicle trafficking, cell-cycle control, and innate antiviral signaling. The strongest coherent functional signal is a shared program of basic nuclear, mitochondrial, and cytoskeletal processes rather than a narrowly defined tissue-specific pathway. The high-connectivity genes MRPS33 and MAP1A link several of these functional areas in the co-abundance graph, while the POLR3A–POLR3D–GTF3C1 component provides a more specific transcriptional submodule.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: only A2M is annotated as secreted to blood. Most genes have low tissue specificity and low immune-cell specificity, and protein detection is common in both bone marrow and skin. The module therefore does not look like a simple blood-contamination signature or a conventional blood-cell module. Nevertheless, HPA shows cell-type-enhanced signals across diverse populations, including neutrophil progenitors, B-cell and dendritic-cell populations, megakaryocytes, platelets, and gdT cells, alongside epithelial, neural, reproductive, and hepatic cell types. The shared bone-marrow and skin signal may consequently reflect broadly expressed cellular machinery, shared proliferative or structural cell states, or mixtures of cell types rather than a single lineage. A2M could contribute a circulating or extracellular component, but it is not representative of the module as a whole.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a compact, internally coherent RNA polymerase III interaction component: GTF3C1 is connected to POLR3A and POLR3D, and POLR3A and POLR3D have a particularly strong known relationship. These are established protein relationships and support interpreting that part of the module as a genuine transcriptional complex-related signal rather than an arbitrary correlation. STRING reports no functional enrichment for the complete module. hu.MAP independently places POLR3A and POLR3D together in the complexes (hu.MAP huMAP3_00807.1), (hu.MAP huMAP3_09057.1), (hu.MAP huMAP3_08487.1), (hu.MAP huMAP3_06426.1), (hu.MAP huMAP3_14318.1), and (hu.MAP huMAP3_11092.1). However, each complex contributes only those two module members, while the remaining module genes are not represented in those complexes. Thus, known physical or complex-level evidence validates a small POLR3A–POLR3D-centered submodule, but does not establish one unified physical complex for the full co-abundance module. Most other module relationships are not supported by the supplied STRING or hu.MAP results and may represent co-regulation, indirect biology, or tissue-composition effects.

**STRING interactions (score >= 0.7)**: 3 of 630 gene pairs: GTF3C1–POLR3A (0.82); GTF3C1–POLR3D (0.803); POLR3A–POLR3D (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00807.1 (POLR3A, POLR3D; 2/30); huMAP3_09057.1 (POLR3A, POLR3D; 2/36); huMAP3_08487.1 (POLR3A, POLR3D; 2/37); huMAP3_06426.1 (POLR3A, POLR3D; 2/38); huMAP3_14318.1 (POLR3A, POLR3D; 2/58); huMAP3_11092.1 (POLR3A, POLR3D; 2/65)

### Novelty

The module may be a new co-abundance observation, but the available evidence does not justify claiming a newly discovered molecular complex or pathway. The POLR3A, POLR3D, and GTF3C1 relationships are already known, and the POLR3A–POLR3D pairing is repeatedly represented in hu.MAP complexes (hu.MAP huMAP3_00807.1) through (hu.MAP huMAP3_11092.1). The broader module is more distinctive because it combines that transcriptional component with genes involved in mitochondrial maintenance, chromatin regulation, cytoskeletal organization, vesicle trafficking, translation, and immune signaling, while lacking broad STRING or hu.MAP support as a single entity. Absence of additional STRING or hu.MAP relationships cannot by itself prove novelty. The defensible conclusion is that the tissue-pair co-abundance pattern is potentially novel, whereas its best-supported molecular submodule is established and the biological integration of the remaining genes remains unresolved.

**Hypothesis.** Hypothesis: the module represents a shared cell-state program coupling basal biosynthetic and genome-maintenance activity to cytoskeletal remodeling and stress or innate-immune readiness in cells present in both bone marrow and skin. In this model, RNA polymerase III activity through GTF3C1, POLR3A, and POLR3D supports production of small RNAs and may contribute to antiviral sensing; chromatin regulators such as ATF7IP, SMARCD1, MACROH2A2, and TASOR tune transcriptional state; mitochondrial and DNA-maintenance genes such as MRPS33, MGME1, LYRM4, and PNKP support energetic and genome stability demands; and MAP1A, CAMSAP1, PRKCI, NEDD1, and vesicle-associated genes support structural or trafficking adaptations. This is a mechanistic model rather than an enrichment result and should be tested by cell-type-resolved expression, perturbation of the POLR3A–POLR3D–GTF3C1 axis, and validation across independent bone-marrow and skin cohorts.

### Important genes

#### POLR3A

- **Related proteins** (co-abundance neighbors): MRPS33 (0.84); STRING partners: GTF3C1 (0.82), POLR3D (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_00807.1, huMAP3_09057.1, huMAP3_08487.1, huMAP3_06426.1, huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase III subunit A. The protein encoded by this gene is the catalytic component of RNA polymerase III, which synthesizes small RNAs. The encoded protein also acts as a sensor to detect foreign DNA and trigger an innate immune response. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: Wiedemann-Rautenstrauch syndrome (0.810); Leukoencephalopathy - ataxia - hypodontia - hypomyelination (0.796); hypomyelination-hypogonadotropic hypogonadism-hypodontia syndrome (0.763); tremor-ataxia-central hypomyelination syndrome (0.671); odontoleukodystrophy (0.671)
- **Europe PMC papers**: 879
- **Why important**: POLR3A is the catalytic RNA polymerase III subunit and occupies the most clearly annotated known interaction submodule with POLR3D and GTF3C1. It is present in every listed hu.MAP complex (hu.MAP huMAP3_00807.1) through (hu.MAP huMAP3_11092.1), and its gene-level annotations include RNA polymerase III transcription and positive regulation of interferon-beta production. Its disease associations include several severe inherited neurological and hypomyelination syndromes, giving it strong biological and clinical relevance. The literature volume is substantial, supporting established interpretation rather than a purely predictive assignment.
- **Conclusion**: Established evidence supports POLR3A as a central marker of the RNA polymerase III component of the module and as a plausible link between transcriptional output and innate immune signaling. It is not established that POLR3A drives the entire shared bone-marrow–skin module; that broader role remains a hypothesis.

#### POLR3D

- **Related proteins** (co-abundance neighbors): MRPS33 (0.82), RNF25 (0.81); STRING partners: GTF3C1 (0.803), POLR3A (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: huMAP3_00807.1, huMAP3_09057.1, huMAP3_08487.1, huMAP3_06426.1, huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase III subunit D. This gene complements a temperature-sensitive mutant isolated from the BHK-21 Syrian hamster cell line. It leads to a block in progression through the G1 phase of the cell cycle at nonpermissive temperatures. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: placental abruption (0.083); autosomal dominant macrothrombocytopenia (0.063); hyperlipoproteinemia type V (0.058); hypertriglyceridemia 2 (0.053); apolipoprotein c-III deficiency (0.052)
- **Europe PMC papers**: 287
- **Why important**: POLR3D is directly connected in STRING to GTF3C1 and POLR3A and is repeatedly included with POLR3A in hu.MAP complexes (hu.MAP huMAP3_00807.1) through (hu.MAP huMAP3_11092.1). Its annotations support RNA polymerase III transcription, tRNA transcription, and innate immune response regulation. It has a more peripheral position in the co-abundance graph than MRPS33 or MAP1A, but its complex membership gives it disproportionate interpretive importance because it anchors the best-supported physical submodule.
- **Conclusion**: Established evidence identifies POLR3D as a bona fide component of the module's RNA polymerase III-associated substructure. Its co-abundance with the rest of the module may reflect shared cellular state or regulation, but a direct physical association with most module genes is not established.

#### GTF3C1

- **Related proteins** (co-abundance neighbors): MAP1A (0.88); STRING partners: POLR3A (0.82), POLR3D (0.803)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Nucleoli; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: general transcription factor IIIC subunit 1. Predicted to contribute to DNA binding activity. Predicted to be involved in 5S class rRNA transcription by RNA polymerase III and transcription initiation from RNA polymerase III promoter. Located in nucleolus and nucleoplasm. Part of transcription factor TFIIIC complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.543); lysosomal storage disease (0.357); alopecia areata (0.352); Abnormal brain morphology (0.266); esophageal atresia/tracheoesophageal fistula (0.259)
- **Europe PMC papers**: 394
- **Why important**: GTF3C1 is a transcription factor for RNA polymerase III initiation and is the third member of the module's known STRING-supported transcriptional component. Its annotations include five-S class ribosomal RNA and tRNA transcription, and it is represented in STRING with both POLR3A and POLR3D. Its HPA profile is broadly distributed with an immune-cell-enhanced signal in gdT cells, which is relevant to interpreting the shared tissue pattern without reducing the module to a blood signature.
- **Conclusion**: Established evidence supports GTF3C1 as the initiation-factor side of the POLR3 transcriptional submodule. A reasonable hypothesis is that it helps connect basal transcriptional demand with antiviral readiness, but the co-abundance data do not demonstrate that it regulates the other module branches.

#### MRPS33

- **Related proteins** (co-abundance neighbors): SMARCD1 (0.88), SNAP23 (0.85), EEF1E1 (0.84), POLR3A (0.84), ATF7IP (0.82), NEDD1 (0.82), POLR3D (0.82), PAWR (0.82), EIF4E (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial ribosomal protein S33. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: bipolar disorder (0.336); ovarian neoplasm (0.253); alopecia areata (0.251); schizophrenia (0.235); obsessive-compulsive disorder (0.235)
- **Europe PMC papers**: 206
- **Why important**: MRPS33 has the strongest network connectivity in the supplied module graph and links genes from mitochondrial translation, chromatin regulation, vesicle biology, cytoskeletal biology, and RNA polymerase III-associated transcription. Its known function is as a mitochondrial ribosomal protein involved in mitochondrial protein synthesis. Although it has no supplied STRING partner or hu.MAP complex assignment, its network position makes it an important integrative marker of the co-abundance pattern. It also has a meaningful literature record and disease associations spanning neurological and ovarian conditions.
- **Conclusion**: Established evidence supports MRPS33 as a mitochondrial translation factor and as a network-level connector in this module. Its apparent bridging role is an observation from the co-abundance graph, not proof that MRPS33 physically coordinates the other branches. It is a strong candidate for testing whether mitochondrial state contributes to the shared tissue signal.

#### MAP1A

- **Related proteins** (co-abundance neighbors): PNKP (0.91), GTF3C1 (0.88), IPO4 (0.83), MGME1 (0.83), PRKAG1 (0.82), TASOR (0.82), ZC3HAV1 (0.81), RANBP3 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: microtubule associated protein 1A. This gene encodes a protein that belongs to the microtubule-associated protein family. The proteins of this family are thought to be involved in microtubule assembly, which is an essential step in neurogenesis. The product of this gene is a precursor polypeptide that presumably undergoes proteolytic processing to generate the final MAP1A heavy chain and LC2 light chain. Expression of this gene is …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.340); venous thromboembolism (0.238); hereditary disease (0.118); autism spectrum disorder (0.094); urinary bladder cancer (0.075)
- **Europe PMC papers**: 1240
- **Why important**: MAP1A is among the most highly connected genes in the module and links PNKP, GTF3C1, IPO4, MGME1, PRKAG1, TASOR, ZC3HAV1, and RANBP3. Its established function concerns microtubule organization and neuronal structural biology, and HPA describes tissue enrichment in brain with enhancement in several neural and ciliated cell types as well as plasmacytoid dendritic cells. It has a large literature base and disease associations involving neurodevelopment and thrombosis, making it a biologically informative but potentially context-sensitive marker.
- **Conclusion**: Established evidence supports MAP1A as a microtubule-associated protein with broad relevance to cell structure and intracellular organization. Its prominence here may indicate cytoskeletal or cell-state variation shared across sampled tissues, but the neural expression pattern and lack of direct STRING or hu.MAP support argue against assigning it a specific bone-marrow–skin mechanism without further validation.

#### A2M

- **Related proteins** (co-abundance neighbors): BTAF1 (0.84), MGME1 (0.81), INTS13 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alpha-2-macroglobulin. The protein encoded by this gene is a protease inhibitor and cytokine transporter. It uses a bait-and-trap mechanism to inhibit a broad spectrum of proteases, including trypsin, thrombin and collagenase. It can also inhibit inflammatory cytokines, and it thus disrupts inflammatory cascades. Mutations in this gene are a cause of alpha-2-macroglobulin deficiency. This gene is implicated in Alzheimer…
- **Diseases (Open Targets)**: myopia (0.206); refractive error (0.151); primary angle-closure glaucoma (0.148); Abnormality of refraction (0.144); Aganglionic megacolon (0.118)
- **Europe PMC papers**: 5133
- **Why important**: A2M is the clearest extracellular and blood-related component: HPA annotates it as secreted to blood and enriched in several stromal, hepatic, cardiac, and mast-cell contexts. Its established function is broad protease inhibition and cytokine transport, including negative regulation of complement activation. It occupies a connecting position to BTAF1, MGME1, and INTS13 in the module, and it has a large literature base. Its presence is important because it offers a plausible sample-level or extracellular explanation for part of the shared signal, even though the module is not generally secreted.
- **Conclusion**: Established evidence supports A2M as a circulating protease inhibitor and cytokine transporter rather than as a core intracellular member of the RNA polymerase III submodule. Its inclusion may reflect extracellular milieu, stromal contribution, or shared sample composition. It should therefore be treated as a potential contextual marker, not evidence that the full module is a plasma-protein program.

## Module 3

**Tissue pair**: bone_marrow and skin  
**Genes (41)**: AAK1, ALDH1L2, ALDH7A1, ATXN2, BRAP, CAVIN3, CD2AP, CDK12, HLA-DQA1, CLINT1, ERBIN, FERMT2, FHL1, GCFC2, HNRNPLL, INTS5, IPO11, KIFBP, LTA4H, LEMD3, MED30, NCOA2, NDC80, NSUN2, PAXX, PPWD1, PRPF4, RASA1, RMP64, POLRMT, RUNX3, SNRNP27, SRPK1, STAU2, WRAP53, GTF2H4, MELTF, TTC5, WFS1, YIPF5, ZC3H7A

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. The most defensible interpretation is therefore a mixed cellular maintenance and regulatory module rather than a single established pathway. Its genes collectively point toward RNA processing and transcriptional regulation, intracellular trafficking, mitochondrial and metabolic support, DNA damage and genome maintenance, cell adhesion, and immune or epithelial state. The module may capture a shared cellular-state program present in bone marrow and skin, but the co-abundance pattern alone does not establish that these processes act in one physical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only a small minority are secreted, and most proteins are intracellular or membrane-associated. Most genes have low tissue specificity, consistent with broadly expressed housekeeping or regulatory functions rather than a narrowly skin-specific program. HPA protein detection is broadly present in both tissues. There is a notable immune and hematopoietic component, including RUNX3, HLA-DQA1, CLINT1, LTA4H, SRPK1, HNRNPLL, and genes enhanced in neutrophil progenitors or other blood-cell populations. There is also a keratinocyte signal for MED30 and a mixture of bone-marrow, lymphoid, epithelial, stromal, and broadly expressed cell states. Consequently, the shared module could partly reflect blood or immune-cell representation in the tissue samples, shared cell types, or a general cellular maintenance program rather than a specialized bone-marrow–skin mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports only a small amount of direct, high-confidence physical connectivity within the module: GTF2H4–MED30 and PRPF4–SNRNP27. The latter relationship is consistent with spliceosomal biology, while the former links a general transcription and DNA-repair factor with a Mediator subunit. The absence of broader STRING functional enrichment means that the module is not independently supported as a coherent known interaction network by STRING. hu.MAP provides more structured support for subgroups. GCFC2 and PPWD1 recur together in multiple spliceosome-related complexes (hu.MAP huMAP3_00050.1), (hu.MAP huMAP3_06576.1), (hu.MAP huMAP3_03019.1), (hu.MAP huMAP3_06726.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), (hu.MAP huMAP3_09945.1). CLINT1 and AAK1 recur together in clathrin, AP-complex, and endocytic assemblies (hu.MAP huMAP3_05849.1), (hu.MAP huMAP3_08320.1), (hu.MAP huMAP3_09403.1), (hu.MAP huMAP3_10876.1), (hu.MAP huMAP3_10762.1), (hu.MAP huMAP3_12918.1), (hu.MAP huMAP3_12394.1). PRPF4 and SNRNP27 occur together in spliceosomal complexes (hu.MAP huMAP3_06511.1), (hu.MAP huMAP3_08980.1). These observations support recognizable spliceosomal and endocytic submodules, but each complex contains only a small subset of the module genes. Thus, the network is best viewed as co-abundance connecting several known cellular subsystems, not as a single experimentally established complex.

**STRING interactions (score >= 0.7)**: 2 of 820 gene pairs: GTF2H4–MED30 (0.818); PRPF4–SNRNP27 (0.945)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00050.1 (GCFC2, PPWD1; 2/8); huMAP3_06576.1 (GCFC2, PPWD1; 2/11); huMAP3_03019.1 (GCFC2, PPWD1; 2/20); huMAP3_05849.1 (CLINT1, AAK1; 2/21); huMAP3_08320.1 (CLINT1, AAK1; 2/24); huMAP3_09403.1 (CLINT1, AAK1; 2/26); huMAP3_06726.1 (GCFC2, PPWD1; 2/37); huMAP3_10876.1 (CLINT1, AAK1; 2/40); huMAP3_08501.1 (GCFC2, PPWD1; 2/47); huMAP3_09504.1 (GCFC2, PPWD1; 2/51); huMAP3_09945.1 (GCFC2, PPWD1; 2/61); huMAP3_10762.1 (CLINT1, AAK1; 2/62); huMAP3_12918.1 (CLINT1, AAK1; 2/62); huMAP3_06511.1 (PRPF4, SNRNP27; 2/79); huMAP3_08980.1 (PRPF4, SNRNP27; 2/97); huMAP3_12394.1 (CLINT1, AAK1; 2/98)

### Novelty

The shared co-abundance module may be a new tissue-pair-level observation, but the biological components are not individually novel. Several relationships and substructures correspond to known spliceosomal, transcriptional, mitochondrial, endocytic, immune, and adhesion biology, as shown by the STRING and hu.MAP evidence and by the gene annotations. The lack of a globally significant GO/KEGG term and the limited STRING connectivity make a claim of a newly discovered pathway especially unwarranted. Conversely, absence from STRING or hu.MAP does not prove novelty, because co-abundance can arise from coordinated regulation, shared cell composition, or context-specific biology not represented in those resources. The appropriate novelty claim is therefore modest: the cross-tissue co-abundance pattern may be novel and worth replication, whereas the underlying molecular functions are largely established and heterogeneous.

**Hypothesis.** Hypothesis: this module reflects a shared cell-state program in bone marrow and skin in which broadly expressed nuclear RNA-processing and transcriptional machinery is coordinated with endocytic trafficking, mitochondrial or metabolic capacity, DNA repair, and immune or epithelial signaling. In bone marrow, part of the signal may be contributed by hematopoietic or immune-cell composition; in skin, it may be contributed by resident epithelial, stromal, vascular, or immune cells. The apparent links among these processes could represent coordinated adaptation to proliferation, differentiation, stress, membrane remodeling, and inflammatory signaling rather than direct physical interaction. This hypothesis should be tested by cell-type-resolved expression, replication in independent cohorts, and perturbation or activity measurements for the implicated pathways.

### Important genes

#### WFS1

- **Related proteins** (co-abundance neighbors): ERBIN (0.90), ALDH1L2 (0.88), RASA1 (0.86), ALDH7A1 (0.85), CDK12 (0.85), INTS5 (0.85), POLRMT (0.84), ATXN2 (0.83), PRPF4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: wolframin ER transmembrane glycoprotein. This gene encodes a transmembrane protein, which is located primarily in the endoplasmic reticulum and ubiquitously expressed with highest levels in brain, pancreas, heart, and insulinoma beta-cell lines. Mutations in this gene are associated with Wolfram syndrome, also called DIDMOAD (Diabetes Insipidus, Diabetes Mellitus, Optic Atrophy, and Deafness), an autosomal recessive disorder. The disease…
- **Diseases (Open Targets)**: Wolfram syndrome (0.851); Wolfram-like syndrome (0.818); type 2 diabetes mellitus (0.764); autosomal dominant nonsyndromic hearing loss (0.749); cataract (0.703)
- **Europe PMC papers**: 3064
- **Why important**: WFS1 is the strongest network hub in the supplied subgraph and connects genes spanning ER biology, transcriptional regulation, mitochondrial function, and RNA-related processes. It is detected in both bone marrow and skin, has low tissue specificity, and encodes an ER transmembrane glycoprotein associated with ER overload response and Wolfram syndrome. Its large literature base and disease associations make it a useful anchor for distinguishing a general cellular-stress signal from a tissue-specific pathway.
- **Conclusion**: Established evidence supports WFS1 as a broadly expressed ER and disease-relevant gene with a central co-abundance position. It is not established that WFS1 mechanistically drives this module; its hub status may instead reflect coordinated cellular stress or shared cell composition.

#### TTC5

- **Related proteins** (co-abundance neighbors): BRAP (0.88), LTA4H (0.86), CD2AP (0.86), NSUN2 (0.85), ZC3H7A (0.85), SRPK1 (0.82), STAU2 (0.82), RMP64 (0.80), IPO11 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tetratricopeptide repeat domain 5. Predicted to enable DNA binding activity and chromatin binding activity. Predicted to be involved in DNA repair. Predicted to act upstream of or within positive regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder with cerebral atrophy and variable facial dysmorphism (0.739); autosomal recessive non-syndromic intellectual disability (0.370); neurodevelopmental disorder (0.370); Neurodevelopmental delay (0.118); autosomal recessive spondylocostal dysostosis (0.075)
- **Europe PMC papers**: 767
- **Why important**: TTC5 is also among the most connected genes in the module and links BRAP, LTA4H, CD2AP, NSUN2, ZC3H7A, SRPK1, STAU2, and RMP64. Its annotation involves DNA and chromatin binding, DNA damage response, transcriptional regulation, and RNA metabolism. The neighboring genes span inflammatory lipid metabolism, cytoskeletal signaling, RNA modification, splicing regulation, and RNA localization, making TTC5 a plausible integrative node. It is detected in both tissues and has disease associations involving neurodevelopment.
- **Conclusion**: Established evidence supports TTC5 as a highly connected nuclear regulatory candidate with links to genome maintenance and gene expression. Its role as an organizer of the cross-tissue module remains a hypothesis because no direct STRING or hu.MAP relationship was supplied.

#### RUNX3

- **Related proteins** (co-abundance neighbors): MED30 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Vesicles; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RUNX family transcription factor 3. This gene encodes a member of the runt domain-containing family of transcription factors. A heterodimer of this protein and a beta subunit forms a complex that binds to the core DNA sequence 5'-PYGPYGGT-3' found in a number of enhancers and promoters, and can either activate or suppress transcription. It also interacts with other transcription factors. It functions as a tumor suppressor, and the g…
- **Diseases (Open Targets)**: asthma (0.530); psoriasis (0.504); allergic rhinitis (0.499); atopic eczema (0.487); allergic disease (0.483)
- **Europe PMC papers**: 10344
- **Why important**: RUNX3 connects to MED30 and is tissue enhanced in bone marrow and lymphoid tissue. Its single-cell annotations include B cells, dendritic cells, innate lymphoid cells, macrophages, and mast cells. It regulates transcription, is involved in ossification and chondrocyte differentiation, and has substantial literature volume and disease associations with psoriasis, asthma, and allergic disease. It therefore provides a biologically informative link between hematopoietic composition, immune regulation, and tissue biology.
- **Conclusion**: Established evidence supports RUNX3 as an immune and developmental transcription factor that could explain part of the shared bone-marrow and skin signal. The module does not establish that RUNX3 coordinates the other submodules or that it mediates a direct bone-marrow–skin connection.

#### PRPF4

- **Related proteins** (co-abundance neighbors): WFS1 (0.81); STRING partners: SNRNP27 (0.945)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: pre-mRNA splicing tri-snRNP complex factor PRPF4. The protein encoded by this gene is part of a heteromeric complex that binds U4, U5, and U6 small nuclear RNAs and is involved in pre-mRNA splicing. The encoded protein also is a mitotic checkpoint protein and a regulator of chemoresistance in human ovarian cancer. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: retinitis pigmentosa (0.634); retinitis pigmentosa 70 (0.578); inherited retinal dystrophy (0.377); neurodegenerative disease (0.203); refractive error (0.083)
- **Europe PMC papers**: 461
- **Why important**: PRPF4 is directly connected to SNRNP27 in STRING and occurs with SNRNP27 in hu.MAP spliceosomal complexes (hu.MAP huMAP3_06511.1), (hu.MAP huMAP3_08980.1). Its annotation places it in the U4, U5, and U6 tri-snRNP and in spliceosomal assembly and RNA splicing. It is detected in both tissues and provides one of the clearest molecularly coherent anchors within the module.
- **Conclusion**: Established evidence supports PRPF4 as a spliceosomal component and supports the PRPF4–SNRNP27 relationship as a known interaction. It is plausible that coordinated RNA processing contributes to the module, but the absence of global enrichment means this cannot be generalized to the entire module without further testing.

#### AAK1

- **Related proteins** (co-abundance neighbors): NCOA2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05849.1, huMAP3_08320.1, huMAP3_09403.1, huMAP3_10876.1, huMAP3_10762.1, huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: AP2 associated kinase 1. This gene encodes a member of the SNF1 subfamily of serine/threonine protein kinases. Adaptor-related protein complex 2 (AP-2 complexes) functions during receptor-mediated endocytosis to trigger clathrin assembly, interact with membrane-bound receptors, and recruit encodytic accessory factors. The encoded protein interacts with and phosphorylates a subunit of the AP-2 complex, which promotes bindi…
- **Diseases (Open Targets)**: gout (0.466); Parkinson disease (0.265); Alzheimer disease (0.264); neurodegenerative disease (0.261); lysosomal storage disease (0.259)
- **Europe PMC papers**: 1532
- **Why important**: AAK1 is the representative module gene for a recurring hu.MAP endocytic subgroup with CLINT1 (hu.MAP huMAP3_05849.1), (hu.MAP huMAP3_08320.1), (hu.MAP huMAP3_09403.1), (hu.MAP huMAP3_10876.1), (hu.MAP huMAP3_10762.1), (hu.MAP huMAP3_12918.1), (hu.MAP huMAP3_12394.1). Its established function is phosphorylation associated with AP-two-dependent, clathrin-mediated endocytosis and membrane organization. Although HPA protein detection was not reported in either focal tissue, its complex-level evidence gives it strong interpretive value for the trafficking component of the module. It also has disease associations involving neurodegenerative and lysosomal disorders.
- **Conclusion**: Established evidence supports AAK1 as an endocytic regulatory kinase and supports its membership in known trafficking complexes. Its inclusion in this shared module may indicate coordinated membrane trafficking or may reflect a cell-type mixture; the module alone cannot distinguish these possibilities.

#### HLA-DQA1

- **Related proteins** (co-abundance neighbors): MED30 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location None; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: major histocompatibility complex, class II, DQ alpha 1. HLA-DQA1 belongs to the HLA class II alpha chain paralogues. The class II molecule is a heterodimer consisting of an alpha (DQA) and a beta chain (DQB), both anchored in the membrane. It plays a central role in the immune system by presenting peptides derived from extracellular proteins. Class II molecules are expressed in antigen presenting cells (APC: B Lymphocytes, dendritic cells, macrophages)…
- **Diseases (Open Targets)**: pleural mesothelioma (0.123); type 1 diabetes mellitus (0.108); hepatitis B virus infection (0.093); neoplasm (0.089); esophageal squamous cell carcinoma (0.083)
- **Europe PMC papers**: 14540
- **Why important**: HLA-DQA1 connects to MED30 and is tissue enhanced in lung and lymphoid tissue, with single-cell enrichment in antigen-presenting cell populations and immune-cell enhancement in myeloid dendritic cells. Its established function is presentation of extracellular peptides through MHC class two and regulation of immune responses. It has a very large literature base and disease associations involving immune and neoplastic conditions. It is therefore important for assessing whether the shared module partly reflects immune-cell abundance.
- **Conclusion**: Established evidence supports HLA-DQA1 as an antigen-presentation marker and a strong indicator of immune-cell contribution. It does not demonstrate that antigen presentation is the central function of the module, especially because no GO/KEGG term passed global correction.

## Module 4

**Tissue pair**: bone_marrow and skin  
**Genes (40)**: AGRN, ALG9, ANKRD17, ANAPC7, ATP12A, BABAM1, BOLA3, RNF40, CDC45, CHD1, SPECC1, DYNC1I2, LIG1, POLD1, DPYSL2, ESF1, EXOSC7, FAM107B, GNAI3, EIF4G3, IRGQ, KIF20A, MAD2L1, MIER1, MYO1E, NDUFA7, NSFL1C, PDCL, PRIM2, RNASEH2A, RRP15, SLAIN2, SMCHD1, SREK1, SRSF5, TATDN1, ACAA1, WDR74, ZMYND8, TJP2

### Function

The module is best interpreted as a mixed proliferative, genome-maintenance, and cell-organization program rather than a narrowly defined pathway. Its strongest biological signal comes from DNA replication and repair genes, mitotic checkpoint and cytokinesis genes, nucleolar ribosome-biogenesis genes, and additional genes involved in chromatin, cytoskeletal, membrane-junction, glycosylation, and mitochondrial functions. CDC45, POLD1, PRIM2, LIG1, and RNASEH2A form a coherent DNA-replication and DNA-repair theme, while MAD2L1, KIF20A, and ANAPC7 support spindle-checkpoint, cytokinesis, and cell-cycle control. ALG9 is the highest-connectivity node and links several otherwise diverse parts of the module, but its network centrality does not by itself establish a single biochemical pathway. No GO or KEGG term passed global correction; therefore, the functional interpretation is based on the concordance of individual gene annotations, network structure, STRING relationships, and cellular localization rather than on globally significant enrichment. The absence of a globally significant term does not make the module biologically false.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only a small minority are secreted, with AGRN identified as secreted to the extracellular matrix and the module-level HPA summary identifying only a small secreted component. Most genes are intracellular and broadly detected in both tissues, especially in the nucleus, nucleolus, cytosol, cytoskeleton, mitochondria, or membrane junctions. HPA describes most genes as having low tissue specificity, while a substantial subset is cell-type enhanced. Bone marrow, lymphoid tissue, erythrocyte progenitors, neutrophils, and other hematopoietic populations recur among the enriched tissue or cell-type annotations. This makes shared proliferating or lineage-related cell populations, and possibly blood-cell representation in tissue samples, plausible contributors to the shared signal. The module also contains genes enhanced in skin or epithelial contexts, including TJP2 and ATP12A, so it should not be reduced to a purely hematopoietic signature. Its broad detection in both tissues and mixture of lineage-specific annotations argue for a composite cellular-state module rather than a tissue-exclusive program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a concentrated set of established relationships within the replication and mitosis portion of the module. CDC45 is connected to LIG1, MAD2L1, POLD1, and PRIM2; POLD1 is connected to LIG1, PRIM2, and RNASEH2A; PRIM2 is connected to RNASEH2A; and KIF20A is connected to MAD2L1 and CDC45. ANAPC7 is connected to MAD2L1. These relationships support a real, known genome-replication and cell-division subnetwork rather than an interpretation based only on correlated expression. STRING also supports the nucleolar and ribosome-biogenesis part through ESF1–RRP15 and RRP15–WDR74. However, STRING reports no supplementary functional enrichment, and many module edges have no listed high-confidence STRING counterpart. hu.MAP gives partial support rather than a complete shared complex: CHD1 and WDR74 occur together in C1, KIF20A and MAD2L1 occur together in C2, and SPECC1 and TJP2 occur together in C3. The other members of each complex are largely outside the module. Thus, the module contains several known molecular substructures, but it is not itself equivalent to one established complex.

**STRING interactions (score >= 0.7)**: 13 of 780 gene pairs: ANAPC7–MAD2L1 (0.978); CDC45–KIF20A (0.797); CDC45–LIG1 (0.773); CDC45–MAD2L1 (0.862); CDC45–POLD1 (0.886); CDC45–PRIM2 (0.924); ESF1–RRP15 (0.828); KIF20A–MAD2L1 (0.913); LIG1–POLD1 (0.973); POLD1–PRIM2 (0.992); POLD1–RNASEH2A (0.713); PRIM2–RNASEH2A (0.848); RRP15–WDR74 (0.968)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01045.1 (CHD1, WDR74; 2/5); huMAP3_07733.1 (KIF20A, MAD2L1; 2/9); huMAP3_05613.1 (SPECC1, TJP2; 2/11)

### Novelty

This is not a wholly new molecular mechanism, because major parts of it recapitulate established DNA-replication, DNA-repair, spindle-checkpoint, cytokinesis, and nucleolar-processing biology supported by gene annotations, STRING, and hu.MAP. The potentially novel aspect is the cross-tissue co-abundance configuration linking these known processes with ALG9-centered glycosylation, epithelial-junction genes, cytoskeletal components, and lineage-associated genes in bone marrow and skin. That configuration should be described as a candidate tissue-shared module, not as a newly discovered pathway. The absence of a STRING or hu.MAP relationship for many pairs does not prove novelty; it may reflect indirect regulation, co-expression without physical interaction, incomplete database coverage, or cell-composition effects. Demonstrating novelty would require replication in independent cohorts, preservation after cell-composition adjustment, comparison with published co-expression modules, and ideally perturbation or longitudinal evidence.

**Hypothesis.** Hypothesis: the module reflects a shared abundance program generated by proliferating or renewing cell populations present in bone marrow and skin. In this model, DNA replication and repair machinery supports genome duplication and genome stability, MAD2L1 and KIF20A coordinate chromosome segregation and cytokinesis, and nucleolar factors support the increased RNA-processing and ribosome-production demand of proliferating cells. ALG9-centered connections may represent glycoprotein-processing or endoplasmic-reticulum activity associated with the same cellular state, while TJP2, ATP12A, AGRN, SPECC1, and cytoskeletal genes may reflect epithelial or junctional organization in skin and related structural cells in marrow-associated samples. The module could therefore arise from a shared regenerative or proliferative state combined with cell-type composition, rather than from one physical complex or one tissue-specific pathway. This hypothesis should be tested by single-cell deconvolution, cell-cycle scoring, replication in independent tissue datasets, and experimental assessment of whether perturbing selected replication or cytokinesis genes changes the broader co-abundance program.

### Important genes

#### ALG9

- **Related proteins** (co-abundance neighbors): RNASEH2A (0.95), DYNC1I2 (0.90), RNF40 (0.87), SREK1 (0.86), EXOSC7 (0.86), FAM107B (0.85), IRGQ (0.85), TJP2 (0.84), WDR74 (0.83), NDUFA7 (0.83), TATDN1 (0.82), ZMYND8 (0.82), RRP15 (0.82), ANKRD17 (0.81), ESF1 (0.81), SRSF5 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ALG9 alpha-1,2-mannosyltransferase. This gene encodes an alpha-1,2-mannosyltransferase enzyme that functions in lipid-linked oligosaccharide assembly. Mutations in this gene result in congenital disorder of glycosylation type Il. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2008].
- **Diseases (Open Targets)**: ALG9-congenital disorder of glycosylation (0.824); ALG9-associated autosomal dominant polycystic kidney disease (0.614); autosomal dominant polycystic kidney disease (0.575); congenital disorder of glycosylation type I (0.462); neurodegenerative disease (0.459)
- **Europe PMC papers**: 910
- **Why important**: ALG9 is the principal network hub by weighted degree and connects genes spanning DNA metabolism, RNA processing, cytoskeletal organization, vesicular or membrane-associated biology, and cellular quality-control functions. Its established function is alpha-mannosyltransferase activity in lipid-linked oligosaccharide assembly, and its disease associations include congenital disorders of glycosylation and polycystic kidney disease. It is broadly detected in bone marrow and skin, has low tissue specificity, and is located in the endoplasmic reticulum. Its large literature base makes it a well-characterized anchor, although its centrality may partly reflect correlation with multiple cellular states rather than direct physical interaction with all neighbors.
- **Conclusion**: Established evidence supports ALG9 as a highly connected glycosylation-related hub associated with the module. It is a plausible integrator of endoplasmic-reticulum and protein-processing state, but the data do not establish that ALG9 mechanistically drives the replication or mitotic subnetwork. The proposed cross-talk between glycosylation activity and the proliferative program remains a hypothesis.

#### CDC45

- **Related proteins** (co-abundance neighbors): MYO1E (0.87), LIG1 (0.87), GNAI3 (0.87), SMCHD1 (0.86), DPYSL2 (0.86), POLD1 (0.86), MAD2L1 (0.84), PRIM2 (0.84); STRING partners: KIF20A (0.797), LIG1 (0.773), MAD2L1 (0.862), POLD1 (0.886), PRIM2 (0.924)
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell division cycle 45. The protein encoded by this gene was identified by its strong similarity with Saccharomyces cerevisiae Cdc45, an essential protein required to the initiation of DNA replication. Cdc45 is a member of the highly conserved multiprotein complex including Cdc6/Cdc18, the minichromosome maintenance proteins (MCMs) and DNA polymerase, which is important for early steps of DNA replication in eukaryotes. T…
- **Diseases (Open Targets)**: Meier-Gorlin syndrome (0.805); hereditary disease (0.195); microcephaly (0.111); hepatocellular carcinoma (0.111); androgen insensitivity syndrome (0.111)
- **Europe PMC papers**: 3743
- **Why important**: CDC45 is a strong network connector and has several high-confidence STRING relationships with DNA-replication, ligation, polymerase, primase, and spindle-checkpoint genes. Its established role is in the replication-initiation machinery and replication-checkpoint biology. HPA reports enrichment in bone marrow and lymphoid tissue and enhancement in erythrocyte progenitors and germ-cell developmental populations, consistent with a proliferative-cell contribution. It has a substantial literature base and a disease association with Meier-Gorlin syndrome.
- **Conclusion**: Established evidence makes CDC45 one of the clearest functional anchors of the module and strongly supports a replication-associated component. Its abundance may mark cells undergoing DNA synthesis or replication stress, but the module does not prove that CDC45 activity is altered or causative in either tissue.

#### POLD1

- **Related proteins** (co-abundance neighbors): CDC45 (0.86), AGRN (0.84); STRING partners: CDC45 (0.886), LIG1 (0.973), PRIM2 (0.992), RNASEH2A (0.713)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA polymerase delta 1, catalytic subunit. This gene encodes the 125-kDa catalytic subunit of DNA polymerase delta. DNA polymerase delta possesses both polymerase and 3' to 5' exonuclease activity and plays a critical role in DNA replication and repair. Alternatively spliced transcript variants have been observed for this gene, and a pseudogene of this gene is located on the long arm of chromosome 6. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: mandibular hypoplasia-deafness-progeroid syndrome (0.768); non-small cell lung carcinoma (0.690); acute lymphoblastic leukemia (0.671); colorectal cancer (0.670); acute myeloid leukemia (0.659)
- **Europe PMC papers**: 3886
- **Why important**: POLD1 encodes the catalytic subunit of DNA polymerase delta and contributes to DNA replication, proofreading, and repair. It is embedded in a coherent STRING-supported subnetwork with CDC45, LIG1, PRIM2, and RNASEH2A. HPA shows detection in both tissues and enhancement in differentiating spermatogonia, erythrocyte progenitors, and tuft cells. Its disease associations include mandibular hypoplasia-deafness-progeroid syndrome and several hematologic and solid cancers, and it has a substantial literature base.
- **Conclusion**: Established evidence supports POLD1 as a central genome-maintenance component and a strong marker of the module's replication and repair axis. The module suggests coordinated abundance of replication machinery, but it cannot determine whether this reflects increased proliferation, altered repair demand, or changes in cell composition.

#### KIF20A

- **Related proteins** (co-abundance neighbors): MIER1 (0.84), ZMYND8 (0.81), SLAIN2 (0.81); STRING partners: CDC45 (0.797), MAD2L1 (0.913)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm, Cytokinetic bridge, Cleavage furrow, Mitotic spindle; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: huMAP3_07733.1
- **Function (MyGene.info)**: kinesin family member 20A. Enables protein kinase binding activity. Involved in microtubule bundle formation; midbody abscission; and regulation of cytokinesis. Located in several cellular components, including cleavage furrow; intercellular bridge; and midbody. Implicated in restrictive cardiomyopathy. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: cardiomyopathy, familial restrictive, 6 (0.586); familial isolated restrictive cardiomyopathy (0.370); hepatocellular carcinoma (0.123); central nervous system cancer (0.120); neoplasm (0.111)
- **Europe PMC papers**: 2386
- **Why important**: KIF20A represents the mitotic and cytokinetic arm of the module. Its annotated functions include microtubule-bundle formation, cytokinesis, and midbody abscission, and its localization includes the cytokinetic bridge, cleavage furrow, and mitotic spindle. STRING connects it to MAD2L1 and CDC45, while hu.MAP complex C2 contains KIF20A and MAD2L1. HPA reports enhancement in bone marrow and lymphoid tissue and in erythrocyte progenitors, with blood annotations including NK-cell and T-reg enrichment. It is associated with restrictive cardiomyopathy and has a substantial literature base.
- **Conclusion**: Established evidence supports KIF20A as a marker of active mitosis and cytokinesis within the module. Its presence strengthens the interpretation of a proliferative-cell program. A direct role for KIF20A in linking skin and marrow states is not established and remains inferential.

#### MAD2L1

- **Related proteins** (co-abundance neighbors): CDC45 (0.84); STRING partners: ANAPC7 (0.978), CDC45 (0.862), KIF20A (0.913)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07733.1
- **Function (MyGene.info)**: mitotic arrest deficient 2 like 1. MAD2L1 is a component of the mitotic spindle assembly checkpoint that prevents the onset of anaphase until all chromosomes are properly aligned at the metaphase plate.  MAD2L1 is related to the MAD2L2 gene located on chromosome 1.  A MAD2 pseudogene has been mapped to chromosome 14. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: alcohol drinking (0.433); cornea transplantation (0.342); connective tissue disorder (0.314); hypotensive disorder (0.294); Tietze syndrome (0.294)
- **Europe PMC papers**: 3856
- **Why important**: MAD2L1 is a spindle-assembly checkpoint component that delays anaphase until chromosome alignment is adequate. It has strong STRING relationships with ANAPC7, CDC45, and KIF20A, and it occurs with KIF20A in hu.MAP complex C2. HPA reports tissue enhancement in bone marrow and lymphoid tissue and cell-type enhancement in erythrocyte progenitors and several proliferative developmental populations. Its extensive literature and direct cell-cycle function make it an important complement to the DNA-replication genes.
- **Conclusion**: Established evidence supports MAD2L1 as a checkpoint component consistent with coordinated chromosome segregation and cell division. The module likely captures a cell-cycle state that includes both replication and mitotic surveillance. It does not show whether checkpoint activation is normal, stressed, or merely more abundant because of increased numbers of dividing cells.

#### TJP2

- **Related proteins** (co-abundance neighbors): ATP12A (0.88), ALG9 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cell Junctions; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: huMAP3_05613.1
- **Function (MyGene.info)**: tight junction protein 2. This gene encodes a zonula occluden that is a member of the membrane-associated guanylate kinase homolog family. The encoded protein functions as a component of the tight junction barrier in epithelial and endothelial cells and is necessary for proper assembly of tight junctions. Mutations in this gene have been identified in patients with hypercholanemia, and genomic duplication of a 270 kb regio…
- **Diseases (Open Targets)**: cholestasis, progressive familial intrahepatic, 4 (0.800); hypercholanemia, familial 1 (0.647); autosomal dominant nonsyndromic hearing loss (0.558); progressive familial intrahepatic cholestasis type 2 (0.527); deafness (0.467)
- **Europe PMC papers**: 1748
- **Why important**: TJP2 provides a structural and tissue-contextual counterpoint to the nuclear replication genes. It encodes a tight-junction component involved in cell-cell junction organization and barrier function, is localized at plasma-membrane cell junctions, and is detected in both bone marrow and skin. It is included in hu.MAP complex C3 with SPECC1, and HPA identifies enhancement in several epithelial or neural cell types as well as immune-cell enhancement in non-classical monocytes. Its disease associations include familial hypercholanemia, progressive familial intrahepatic cholestasis, and inherited hearing loss.
- **Conclusion**: Established evidence supports TJP2 as a marker of junctional or epithelial structural context within the shared module. Its connection to the replication program is not direct and may reflect co-occurring cell populations or tissue architecture. The hypothesis that junctional remodeling accompanies the shared regenerative state requires independent validation.

## Module 5

**Tissue pair**: bone_marrow and skin  
**Genes (45)**: ANKIB1, ANXA7, BCAR1, CDC50A, CCDC43, CEP43, CEP55, CLK3, NCAPG2, COMMD1, DHX8, POLD3, EXOC8, EZH2, FOXK2, GIT1, GOLGA7, H1-2, H1-5, HS2ST1, ILK, KIF3A, LARP7, LRCH1, MADD, MINK1, MTMR1, PCCB, PHF23, PPHLN1, RASA3, RPL22L1, RNASEH1, SLC20A1, SLC35F6, SCAF11, SHC1, SIL1, INIP, SPAST, SRFBP1, SZRD1, TFAP4, TFIP11, TRADD

### Function

This module does not support a single statistically established biological function from GO or KEGG: no GO or KEGG term passed global correction. Its gene content instead points to a heterogeneous, predominantly intracellular program combining RNA processing and spliceosome-associated biology, chromatin regulation, genome maintenance, cell-cycle and chromosome organization, and cell-adhesion or signal-transduction processes. The strongest functional anchors are the DHX8–TFIP11 spliceosome relationship, the FOXK2–EZH2 chromatin-regulatory relationship, and the BCAR1-centered adhesion and signaling branch. The co-abundance pattern is therefore better interpreted as a shared cellular-state or cell-composition signal than as proof of one unified pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a small minority as secreted, and the listed proteins are mainly intracellular or membrane-associated. Most genes have low tissue specificity, while many show cell-type-enhanced expression across epithelial, progenitor, reproductive, neural, or hematopoietic populations. Blood-cell specificity is generally low, although selected genes are enhanced in progenitors, megakaryocyte or platelet-related cells, granulocytes, basophils, or T-reg cells. The presence of bone-marrow and lymphoid enrichment for genes such as NCAPG2, EZH2, CEP55, and H1-5, together with broad detection in skin, means that the shared module could partly reflect common proliferative or progenitor-cell content in the samples. It does not resemble a simple blood-contamination signature, because the module also contains epithelial, neuronal, skeletal-muscle, and broadly expressed intracellular genes.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a few high-confidence relationships within the module. BCAR1 is connected to ILK and SHC1, supporting a known focal-adhesion and receptor-signaling branch. DHX8 is strongly connected to TFIP11, supporting a known spliceosome-associated RNA-processing relationship. H1-2 is connected to H1-5, consistent with linker-histone biology. hu.MAP independently places DHX8 and TFIP11 together in several spliceosome-related complexes, while FOXK2 and EZH2 co-occur in chromatin-regulatory complexes. These observations validate selected local edges and functional islands, but they do not establish that the full module is one physical complex. The sparse STRING connectivity and partial hu.MAP overlap indicate that much of the co-abundance structure is not explained by already catalogued direct protein interactions.

**STRING interactions (score >= 0.7)**: 4 of 990 gene pairs: BCAR1–ILK (0.886); BCAR1–SHC1 (0.865); DHX8–TFIP11 (0.954); H1-2–H1-5 (0.704)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03019.1 (DHX8, TFIP11; 2/20); huMAP3_06726.1 (DHX8, TFIP11; 2/37); huMAP3_08501.1 (DHX8, TFIP11; 2/47); huMAP3_13482.1 (FOXK2, EZH2; 2/50); huMAP3_09504.1 (DHX8, TFIP11; 2/51); huMAP3_09945.1 (DHX8, TFIP11; 2/61); huMAP3_15128.1 (FOXK2, EZH2; 2/96)

### Novelty

The module should not be called a wholly new molecular complex. Its DHX8–TFIP11, BCAR1–ILK, BCAR1–SHC1, H1-2–H1-5, and FOXK2–EZH2 relationships are already represented in STRING or hu.MAP. However, the cross-tissue co-abundance grouping of these genes, including genes with no listed STRING partners or hu.MAP membership, is not directly established by those resources. The absence of an interaction annotation is not evidence of novelty, and the lack of globally significant GO or KEGG enrichment limits claims of a newly discovered pathway. The defensible conclusion is that this is a potentially useful, but currently hypothesis-generating, conserved co-abundance module whose novelty lies in its tissue-pair association and integrated expression structure rather than in a demonstrated new complex.

**Hypothesis.** Hypothesis: the module reflects a shared proliferative and stress-adaptive cellular state present in selected bone-marrow and skin cell populations. In this model, chromatin and transcriptional regulators such as EZH2 and FOXK2 coordinate cell-state programs, DHX8 and TFIP11 support processing of transcripts needed during state transitions, NCAPG2 supports chromosome organization in proliferating progenitors, and BCAR1 with ILK or SHC1 couples adhesion and extracellular cues to intracellular signaling. The apparent conservation between tissues may therefore arise from common progenitor, epithelial, or remodeling-associated cellular states rather than from a tissue-specific secreted program. This hypothesis requires validation by cell-resolved expression, perturbation of the proposed hubs, and testing whether the module tracks proliferation, differentiation, adhesion, or stress independently of cell composition.

### Important genes

#### DHX8

- **Related proteins** (co-abundance neighbors): TFAP4 (0.82), NCAPG2 (0.81); STRING partners: TFIP11 (0.954)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: huMAP3_03019.1, huMAP3_06726.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: DEAH-box helicase 8. This gene is a member of the DEAH box polypeptide family. The encoded protein contains the DEAH (Asp-Glu-Ala-His) motif which is characteristic of all DEAH box proteins, and is thought to function as an ATP-dependent RNA helicase that regulates the release of spliced mRNAs from spliceosomes prior to their export from the nucleus. This protein may be required for the replication of human immunodefi…
- **Diseases (Open Targets)**: congenital anomaly of kidney and urinary tract (0.259); neurodegenerative disease (0.193); upper extremity fracture (0.118); lens disorder (0.064); exudative vitreoretinopathy (0.048)
- **Europe PMC papers**: 360
- **Why important**: DHX8 is a central functional anchor for the RNA-processing interpretation. It is connected to TFIP11 in STRING and co-occurs with TFIP11 across several hu.MAP spliceosome-related complexes. Its annotation identifies an ATP-dependent RNA helicase involved in release of spliced messenger RNA and spliceosomal RNA processing. It is detected in both tissues and has a substantial literature base, while its disease associations include congenital kidney and urinary tract abnormalities and other disorders.
- **Conclusion**: Established evidence supports DHX8 as a representative spliceosome-associated component and one of the most credible functional anchors of the module. It is plausible, but not established, that coordinated DHX8 abundance contributes to the conserved tissue-pair signal.

#### TFIP11

- **Related proteins** (co-abundance neighbors): RNASEH1 (0.92); STRING partners: DHX8 (0.954)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_03019.1, huMAP3_06726.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: tuftelin interacting protein 11. This gene encodes a protein component of the spliceosome that promotes the release of the lariat-intron during late-stage splicing through the recruitment of a pre-mRNA splicing factor called DEAH-box helicase 15. The encoded protein contains a G-patch domain, a hallmark of RNA-processing proteins, that binds DEAH-box helicase 15. This protein contains an atypical nuclear localization sequence as …
- **Diseases (Open Targets)**: neurodegenerative disease (0.487); skin cancer (0.329); malunion fracture (0.214); mathematical ability (0.117); neuroendocrine neoplasm (0.086)
- **Europe PMC papers**: 336
- **Why important**: TFIP11 provides an independent and highly specific RNA-processing anchor. It is the STRING partner of DHX8 and appears with DHX8 in several hu.MAP complexes. Its annotated role in late spliceosome disassembly and lariat-intron release directly complements the DHX8 function. Although its tissue protein evidence is limited, it is detected at the transcript or protein evidence level in the module context and has documented associations including skin cancer and fracture-related phenotypes.
- **Conclusion**: Established evidence supports TFIP11 as part of a known spliceosome-associated machinery represented in the module. A coordinated RNA-processing state is a reasonable interpretation, but the module does not prove that splicing is its dominant activity in either tissue.

#### BCAR1

- **Related proteins** (co-abundance neighbors): MINK1 (0.92), TFAP4 (0.85); STRING partners: ILK (0.886), SHC1 (0.865)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Focal adhesion sites; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BCAR1 scaffold protein, Cas family member. The protein encoded by this gene is a member of the Crk-associated substrate (CAS) family of scaffold proteins, characterized by the presence of multiple protein-protein interaction domains and many serine and tyrosine phosphorylation sites. The encoded protein contains a Src-homology 3 (SH3) domain, a proline-rich domain, a substrate domain which contains 15 repeat of the YxxP consensus phosphory…
- **Diseases (Open Targets)**: neurodegenerative disease (0.551); Abnormality of the skeletal system (0.525); exocrine pancreatic carcinoma (0.413); alcohol drinking (0.307); stroke disorder (0.289)
- **Europe PMC papers**: 1423
- **Why important**: BCAR1 is a network connector linking MINK1 and TFAP4 and is the module member with known STRING relationships to ILK and SHC1. Its scaffold architecture, phosphorylation sites, focal-adhesion localization, and annotations in cell adhesion, actin organization, growth, and receptor signaling make it a strong candidate for coupling extracellular or matrix signals to the intracellular portions of the module. It is detected in skin and has substantial literature and disease-association coverage, including skeletal abnormalities and cancer-related phenotypes.
- **Conclusion**: Established evidence supports BCAR1 as a signaling and adhesion scaffold that may explain part of the tissue-shared co-abundance pattern. Its role as a bridge between the RNA-processing and adhesion branches is a hypothesis based on network placement, not a demonstrated molecular interaction.

#### EZH2

- **Related proteins** (co-abundance neighbors): RASA3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: huMAP3_13482.1, huMAP3_15128.1
- **Function (MyGene.info)**: enhancer of zeste 2 polycomb repressive complex 2 subunit. This gene encodes a member of the Polycomb-group (PcG) family. PcG family members form multimeric protein complexes, which are involved in maintaining the transcriptional repressive state of genes over successive cell generations. This protein associates with the embryonic ectoderm development protein, the VAV1 oncoprotein, and the X-linked nuclear protein. This protein may play a role in the hema…
- **Diseases (Open Targets)**: Weaver syndrome (0.837); diffuse large B-cell lymphoma (0.615); neurodegenerative disease (0.525); follicular lymphoma (0.517); viral infectious disease (0.486)
- **Europe PMC papers**: 43112
- **Why important**: EZH2 is a tissue-enhanced gene in bone marrow and lymphoid tissue and is enhanced in several hematopoietic progenitor populations. It co-occurs with FOXK2 in hu.MAP chromatin-regulatory complexes and is a core Polycomb-associated transcriptional repressor involved in chromatin organization and cell-population proliferation. Its extensive literature and disease associations, including Weaver syndrome and lymphomas, make it biologically consequential even though it has no listed STRING partner within this module.
- **Conclusion**: Established evidence supports EZH2 as a chromatin and cell-state regulator that may be especially relevant to the bone-marrow component. Its contribution to conservation in skin remains a hypothesis and could reflect shared progenitor or proliferative states rather than a tissue-specific EZH2 mechanism.

#### NCAPG2

- **Related proteins** (co-abundance neighbors): CEP55 (0.92), CLK3 (0.87), HS2ST1 (0.81), DHX8 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: non-SMC condensin II complex subunit G2. This gene encodes a protein that belongs to the Condensin2nSMC family of proteins. The encoded protein is a regulatory subunit of the condensin II complex which, along with the condensin I complex, plays a role in chromosome assembly and segregation during mitosis. A similar protein in mouse is required for early development of the embryo. Alternate splicing results in multiple transcript variants…
- **Diseases (Open Targets)**: Khan-Khan-Katsanis syndrome (0.667); neurodegenerative disease (0.344); neoplasm (0.103); cancer (0.101); lung adenocarcinoma (0.098)
- **Europe PMC papers**: 554
- **Why important**: NCAPG2 is tissue-enhanced in bone marrow and lymphoid tissue and is associated with erythrocyte, megakaryocyte, and monocyte progenitor cell types. Its network position connects CEP55, CLK3, HS2ST1, and DHX8, linking chromosome organization to the RNA-processing branch. Its established function in condensin II, chromosome condensation, and sister-chromatid segregation makes it a marker of proliferative cell-state biology. It also has a documented association with a developmental syndrome and other disease categories.
- **Conclusion**: Established evidence supports NCAPG2 as a plausible indicator of proliferating or differentiating progenitor cells in the shared module. The proposed coupling of condensin activity to the DHX8–TFIP11 branch is speculative and should not be treated as a direct interaction.

## Module 6

**Tissue pair**: bone_marrow and skin  
**Genes (18)**: ASL, ARMC8, DCPH1, ASF1B, CEP131, DIAPH3, EP400, FOXRED1, GTPBP10, IFT27, KAT7, KIF22, LARP4, PPP1R3D, STEEP1, TBC1D13, TFB2M, TPM2

### Function

This module does not support a single statistically established GO or KEGG function: no globally significant GO/KEGG term passed global correction, and no supplementary STRING term was reported. Its gene content instead suggests a heterogeneous cellular-maintenance program spanning ciliary and centrosomal biology, chromatin regulation, mitochondrial function, cytoskeletal organization, intracellular transport, and metabolic regulation. IFT27 is the most connected network hub and links cilium-related biology with otherwise diverse genes. KAT7 and EP400 suggest chromatin acetylation and remodeling, FOXRED1 and TFB2M suggest mitochondrial maintenance, while DIAPH3 and TPM2 suggest cytoskeletal or actin-related biology. The lack of coherent enrichment means these annotations should be treated as interpretation of the member genes, not as module-level enrichment evidence.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity and low immune-cell specificity, while many show cell-type-enhanced expression in specialized populations, particularly germ-cell populations and some progenitor or epithelial populations. A smaller subset has immune-related HPA signals, including neutrophil, eosinophil, basophil, and plasmacytoid dendritic-cell associations, but the module is not broadly blood-cell enriched. Protein detection is present for many genes in both bone marrow and skin, although several genes are not detected in one or both tissues. Therefore, the shared module may partly reflect broadly expressed cellular programs or shared cell states, with possible contributions from particular cell populations, rather than a secreted blood-protein signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interactions were reported among the module genes, and no STRING functional-enrichment term was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance relationships are not supported here by previously catalogued high-confidence physical interactions or by a known multi-member complex. This does not disprove biological coordination: co-abundance can reflect shared regulation, cell composition, developmental state, or indirect pathway relationships. The network itself connects genes through co-abundance, but the absence of corresponding STRING and hu.MAP support argues against interpreting it as a known physical complex.

**STRING interactions (score >= 0.7)**: 0 of 153 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module can reasonably be described as a potentially novel co-abundance association, but not as a newly discovered molecular complex or a newly established pathway. Its novelty comes from the tissue-pair-specific co-abundance pattern and the unusual connection of ciliary, chromatin, mitochondrial, cytoskeletal, and metabolic genes. The absence of STRING or hu.MAP support is compatible with novelty but is not proof of it. Because there is no globally significant GO or KEGG term and no independent interaction or complex support, the module requires validation in additional cohorts, cell-composition analyses, perturbation experiments, or orthogonal molecular measurements before claiming a new biological mechanism.

**Hypothesis.** Mechanistic hypothesis: this module may represent a shared cellular-state program in bone marrow and skin in which proliferative or differentiating cells coordinate chromatin accessibility, mitochondrial activity, cytoskeletal remodeling, intracellular transport, and ciliary or centrosomal functions. IFT27 could act as a network-level organizing marker, while KAT7 and EP400 could regulate transcriptional or replication-associated chromatin states, FOXRED1 and TFB2M could support mitochondrial capacity, and DIAPH3 could connect the state to cytoskeletal remodeling. The HPA pattern raises the alternative possibility that the signal is generated by shared or changing cell populations, including progenitor or specialized differentiating cells, rather than by direct regulation among all module genes. This remains a hypothesis because the module lacks globally significant enrichment, known STRING links, and a shared hu.MAP complex.

### Important genes

#### IFT27

- **Related proteins** (co-abundance neighbors): FOXRED1 (0.88), TBC1D13 (0.86), LARP4 (0.84), DCPH1 (0.83), TPM2 (0.82), ARMC8 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: intraflagellar transport 27. This gene encodes a GTP-binding protein that is a core component of the intraflagellar transport complex B. Characterization of the similar Chlamydomonas protein indicates a function in cell cycle control. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: Bardet-Biedl syndrome (0.772); Jeune syndrome (0.432); ciliopathy (0.380); polydactyly (0.370); smoking initiation (0.278)
- **Europe PMC papers**: 552
- **Why important**: IFT27 is the strongest network hub in the module and connects to several otherwise diverse genes. Its established annotation places it in intraflagellar transport and cilium-related biology, with additional links to intracellular transport, smoothened signaling, keratinocyte development, and spermatogenesis. Its HPA profile is broadly low in tissue specificity but enhanced in multiple ciliated and germ-cell populations. Its disease associations include Bardet-Biedl syndrome, Jeune syndrome, ciliopathy, and polydactyly, and it has substantial literature support.
- **Conclusion**: Established evidence supports IFT27 as the best network entry point for a ciliary, transport, or cell-state interpretation. It is plausible that IFT27 marks a shared ciliary or differentiation-related component of the module, but the co-abundance network does not establish that IFT27 regulates the other members.

#### KAT7

- **Related proteins** (co-abundance neighbors): FOXRED1 (0.86), ASF1B (0.84), STEEP1 (0.81), CEP131 (0.80), ASL (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lysine acetyltransferase 7. The protein encoded by this gene is part of the multimeric HBO1 complex, which possesses histone H4-specific acetyltransferase activity. This activity is required for functional replication origins and is involved in transcriptional activation of some genes. In both cases, the acetylation of histone H4 helps unfold chromatin so that the DNA can be accessed and replicated or transcribed. [provided …
- **Diseases (Open Targets)**: neurodegenerative disease (0.521); Alzheimer disease (0.372); autoimmune disorder of central nervous system (0.370); Parkinson disease (0.353); lysosomal storage disease (0.352)
- **Europe PMC papers**: 1247
- **Why important**: KAT7 is a highly connected module member and encodes a histone acetyltransferase component of the HBO1 complex. Its established functions include histone H4 acetylation, regulation of DNA replication, and transcriptional regulation. It is detected in both bone marrow and skin, has nucleoplasmic localization, and has extensive literature support. Its disease associations include neurodegenerative and autoimmune disorders.
- **Conclusion**: Established evidence supports KAT7 as a chromatin and replication regulator that could explain coordinated expression of genes linked to cellular state. Its role as a direct driver of this tissue-pair module is unproven, because neither enrichment evidence nor interaction databases connect it to the module as a complex.

#### EP400

- **Related proteins** (co-abundance neighbors): FOXRED1 (0.93), KIF22 (0.89), GTPBP10 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: E1A binding protein p400. Predicted to enable several functions, including ATP binding activity; ATP-dependent chromatin remodeler activity; and protein antigen binding activity. Involved in histone H2A acetylation and histone H4 acetylation. Part of NuA4 histone acetyltransferase complex and Swr1 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); essential hypertension (0.318); hypertensive disorder (0.318); urolithiasis (0.273); alcohol drinking (0.273)
- **Europe PMC papers**: 1056
- **Why important**: EP400 is connected to FOXRED1, KIF22, and GTPBP10 and encodes an ATP-dependent chromatin remodeler associated with NuA4 and Swr1 complexes. Its established annotations include histone acetylation, transcriptional regulation, cell-cycle control, DNA repair, and homologous-recombination repair. It is detected in both bone marrow and skin and has extensive literature support, with disease associations including neurodegenerative disease and hypertension-related conditions.
- **Conclusion**: Established evidence supports EP400 as a plausible chromatin-state and genome-maintenance marker. It could contribute to a shared proliferative or differentiation state, but that mechanistic interpretation remains a hypothesis rather than a demonstrated property of this module.

#### FOXRED1

- **Related proteins** (co-abundance neighbors): EP400 (0.93), IFT27 (0.88), KAT7 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FAD dependent oxidoreductase domain containing 1. This gene encodes a protein that contains a FAD-dependent oxidoreductase domain. The encoded protein is localized to the mitochondria and may function as a chaperone protein required for the function of mitochondrial complex I. Mutations in this gene are associated with mitochondrial complex I deficiency. Alternatively spliced transcript variants have been observed for this gene. [provided by RefS…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.783); mitochondrial complex I deficiency, nuclear type 19 (0.741); Leigh syndrome (0.662); mitochondrial disease (0.646); mitochondrial complex I deficiency, nuclear type 1 (0.630)
- **Europe PMC papers**: 308
- **Why important**: FOXRED1 forms the strongest local co-abundance links with EP400, IFT27, and KAT7. Its established annotation describes a mitochondrial FAD-dependent oxidoreductase-domain protein that may act as a chaperone for mitochondrial complex I, and mutations are associated with mitochondrial complex I deficiency. Its disease associations include Leigh syndrome and mitochondrial disease. Although its literature volume is smaller than that of several other selected genes, its functional and disease annotations are relatively specific.
- **Conclusion**: Established evidence supports FOXRED1 as a mitochondrial respiratory-chain maintenance gene. Its position between chromatin-associated genes and IFT27 makes it an informative bridge in the module, but a direct chromatin-to-mitochondrial mechanism is not established by the available evidence.

#### DIAPH3

- **Related proteins** (co-abundance neighbors): TFB2M (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Microtubules; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: diaphanous related formin 3. This gene encodes a member of the diaphanous subfamily of the formin family. Members of this family are involved in actin remodeling and regulate cell movement and adhesion. Mutations in this gene are associated with autosomal dominant auditory neuropathy 1. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss (0.574); smoking initiation (0.376); insomnia (0.342); metabolic syndrome X (0.319); endometriosis (0.314)
- **Europe PMC papers**: 1094
- **Why important**: DIAPH3 is linked to TFB2M and encodes a diaphanous formin involved in actin remodeling, actin-filament polymerization, cell movement, and adhesion. HPA indicates tissue enhancement in bone marrow and testis and cell-type enhancement in germ-cell and erythrocyte-progenitor populations. Its established disease association is autosomal dominant auditory neuropathy, and it has substantial literature support.
- **Conclusion**: Established evidence supports DIAPH3 as a cytoskeletal and cell-morphology component that may connect the module to differentiation or adhesion. Its bone-marrow and specialized-cell expression makes it relevant to cell-composition interpretation, but its direct contribution to the shared bone-marrow–skin program is unresolved.

#### ASL

- **Related proteins** (co-abundance neighbors): PPP1R3D (0.85), KAT7 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: argininosuccinate lyase. This gene encodes a member of the lyase 1 family. The encoded protein forms a cytosolic homotetramer and primarily catalyzes the reversible hydrolytic cleavage of argininosuccinate into arginine and fumarate, an essential step in the liver in detoxifying ammonia via the urea cycle. Mutations in this gene result in the autosomal recessive disorder argininosuccinic aciduria, or argininosuccinic acid…
- **Diseases (Open Targets)**: argininosuccinic aciduria (0.866); hereditary disease (0.508); neurodevelopmental disorder (0.436); dystonic disorder (0.370); Tremor (0.370)
- **Europe PMC papers**: 13702
- **Why important**: ASL is connected to KAT7 through the module and encodes argininosuccinate lyase, a cytosolic tetrameric enzyme of the urea cycle and arginine metabolism. HPA identifies liver tissue enrichment and detection in skin but not bone marrow. Its disease association with argininosuccinic aciduria is well established, and it has extensive literature support. Its inclusion adds a metabolic dimension that is distinct from the chromatin, mitochondrial, and cytoskeletal annotations of other selected genes.
- **Conclusion**: Established evidence supports ASL as a metabolic enzyme rather than a module-specific structural component. Its presence may indicate shared metabolic state, indirect co-regulation, or cell-composition effects; a direct ASL role in the proposed module mechanism is currently only a hypothesis.

## Module 7

**Tissue pair**: bone_marrow and skin  
**Genes (23)**: ASCC2, NCAPD3, CTR9, CWC27, EIF2B2, AHCTF1, GAPVD1, GNL3L, HMGN5, HYPK, KIF11, KIF4A, TK1, OGFOD1, OSBPL9, PTPN2, RBM22, RALGAPB, SLC35F2, SENP3, SPDL1, USP15, ZNF346

### Function

The module is most consistent with a proliferative nuclear and cell-division program, especially mitotic spindle organization, chromosome segregation, chromosome condensation, cytokinesis, DNA synthesis, RNA processing, and nucleolar activity. SPDL1 is the principal network hub and is annotated with spindle assembly, kinetochore localization, chromosome alignment, and mitotic checkpoint functions. NCAPD3 links the module to condensin II and mitotic chromosome organization, while KIF11, KIF4A, and TK1 support spindle dynamics, cytokinesis, and DNA precursor production. Additional genes connect RNA splicing, ribosome biogenesis, transcriptional regulation, translation control, protein modification, and vesicle or lipid transport to this cell-cycle-related core. No GO/KEGG term passed global correction, so this functional interpretation is based on the individual gene annotations and network structure rather than significant enrichment. The absence of a globally significant term does not invalidate the module.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and most proteins are intracellular, particularly nuclear or cytosolic. It is also not uniformly immune-cell specific, since most genes have low immune-cell specificity and many have low tissue specificity. Nevertheless, the HPA pattern is strongly compatible with proliferating hematopoietic populations: erythrocyte progenitors, monocyte progenitors, neutrophils, and megakaryocyte progenitors recur among the enriched single-cell types, while lymphoid tissue and bone marrow recur among enriched tissues. Several genes are also detected in both bone marrow and skin. Thus, the shared module may reflect a conserved proliferative cell state present in both tissues, but it may also partly reflect shared or contaminating hematopoietic cell populations rather than a skin-specific biological program. The lack of broad immune specificity argues against interpreting it as a general mature immune-cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING evidence is limited but biologically coherent in places. KIF11 connects to KIF4A and TK1, forming a small spindle, cytokinesis, and DNA-replication-related cluster. CWC27 connects to RBM22, consistent with spliceosome-associated RNA processing. These are established protein associations and support parts of the proposed functional interpretation, but they do not demonstrate that every co-abundance edge represents a direct physical interaction. Most module relationships are absent from the high-confidence STRING set. No hu.MAP complex contains multiple module members, so there is no independent complex-level support for a shared canonical protein complex. Overall, the module appears to combine a cell-cycle core with several less well-connected nuclear and regulatory genes rather than representing one fully established physical complex.

**STRING interactions (score >= 0.7)**: 4 of 253 gene pairs: CWC27–RBM22 (0.943); KIF11–KIF4A (0.952); KIF11–TK1 (0.761); KIF4A–TK1 (0.718)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The co-abundance pattern could be a new tissue-pair observation, but novelty cannot be claimed as established from this fact sheet alone. The module has little high-confidence STRING support, no multi-member hu.MAP complex, and no globally significant GO/KEGG enrichment, which makes it less likely to be a direct recovery of a single well-characterized complex. However, absence from STRING or hu.MAP is not proof of novelty, because co-abundance relationships can reflect shared regulation, cell-state composition, indirect biology, or incomplete database coverage. The most defensible conclusion is that the module presents a potentially novel cross-tissue co-abundance pattern built around a plausible proliferative program, requiring replication and independent validation.

**Hypothesis.** Hypothesis: the module captures a conserved proliferative state shared between bone marrow and skin, particularly in cycling progenitor or transit-amplifying cells. In this model, SPDL1, KIF11, KIF4A, and NCAPD3 coordinate spindle assembly, chromosome organization, and chromosome segregation; TK1 supplies thymidine salvage for DNA replication; and the surrounding RNA-processing, nucleolar, transcriptional, and protein-modification genes support the biosynthetic and regulatory demands of proliferation. The enrichment of hematopoietic progenitor cell types suggests that shared blood-cell composition may contribute substantially to the signal. This hypothesis should be tested by cell-type deconvolution, cell-cycle scoring, and validation of coordinated expression within purified skin and bone-marrow populations.

### Important genes

#### SPDL1

- **Related proteins** (co-abundance neighbors): HYPK (0.86), GAPVD1 (0.86), TK1 (0.85), OSBPL9 (0.83), USP15 (0.82), GNL3L (0.82), CWC27 (0.81), HMGN5 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: spindle apparatus coiled-coil protein 1. This gene encodes a coiled-coil domain-containing protein that functions in mitotic spindle formation and chromosome segregation. The encoded protein plays a role in coordinating microtubule attachment by promoting recruitment of dynein proteins, and in mitotic checkpoint signaling. [provided by RefSeq, Jul 2016].
- **Diseases (Open Targets)**: idiopathic pulmonary fibrosis (0.513); hypothyroidism (0.510); interstitial lung disease (0.502); prostate carcinoma (0.494); renal carcinoma (0.457)
- **Europe PMC papers**: 346
- **Why important**: SPDL1 has the strongest hub-like position in the module and connects to genes involved in spindle control, nucleolar regulation, trafficking, sterol biology, deubiquitination, and splicing. Its supplied annotation directly supports mitotic spindle formation, kinetochore localization, chromosome alignment, spindle checkpoint signaling, and chromosome segregation. It is detected in both bone marrow and skin and is enriched in erythrocyte and megakaryocyte progenitor populations. Its literature record is substantial, although smaller than that of the best-studied mitotic genes. This combination of network centrality and direct cell-division annotation makes it the strongest module-level marker.
- **Conclusion**: Established evidence supports SPDL1 as a central mitotic-spindle and chromosome-segregation component whose abundance could mark proliferating progenitors. Its role as the organizing driver of this entire cross-tissue module remains a hypothesis because the module edges are co-abundance relationships rather than demonstrated physical interactions.

#### KIF11

- **Related proteins** (co-abundance neighbors): NCAPD3 (0.86), ZNF346 (0.81); STRING partners: KIF4A (0.952), TK1 (0.761)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Mid piece; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 11. This gene encodes a motor protein that belongs to the kinesin-like protein family. Members of this protein family are known to be involved in various kinds of spindle dynamics. The function of this gene product includes chromosome positioning, centrosome separation and establishing a bipolar spindle during cell mitosis. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: microcephaly with or without chorioretinopathy, lymphedema, or intellectual disability (0.821); hereditary disease (0.509); inherited retinal dystrophy (0.507); neurodegenerative disease (0.484); microcephaly (0.412)
- **Europe PMC papers**: 3618
- **Why important**: KIF11 is directly annotated for centrosome separation, bipolar spindle establishment, spindle assembly, and chromosome positioning. It is tissue enhanced in bone marrow and lymphoid tissue and is enriched in several dividing progenitor populations. It also participates in the strongest STRING-supported local cluster with KIF4A and TK1. Its extensive literature and disease associations involving developmental and microcephaly phenotypes provide strong independent biological context.
- **Conclusion**: Established evidence identifies KIF11 as a core mitotic motor and a credible anchor for the proliferative interpretation. Its contribution to the shared bone-marrow and skin signal is likely to reflect cycling-cell abundance, but the tissue-specific origin of that signal is not established.

#### KIF4A

- **Related proteins** (co-abundance neighbors): ZNF346 (0.81); STRING partners: KIF11 (0.952), TK1 (0.718)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm, Midbody; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 4A. This gene encodes a member of the kinesin 4 subfamily of kinesin related proteins. The encoded protein is an ATP dependent microtubule-based motor protein that is involved in the intracellular transport of membranous organelles. This protein also associates with condensed chromosome arms and may be involved in maintaining chromosome integrity during mitosis. This protein may also be involved in th…
- **Diseases (Open Targets)**: intellectual disability, X-linked 100 (0.624); neurodegenerative disease (0.541); taurodontism, microdontia, and dens invaginatus (0.483); Hydrocephalus (0.435); Agenesis of corpus callosum (0.259)
- **Europe PMC papers**: 1677
- **Why important**: KIF4A is an ATP-dependent microtubule motor involved in chromosome integrity, central-spindle organization, spindle elongation, and cytokinesis. It has STRING relationships with KIF11 and TK1, reinforcing the local division-related cluster. HPA places it in bone marrow and lymphoid tissue and in erythrocyte progenitors and other proliferative cell types. Its literature record is extensive and its disease associations provide additional evidence that it is a biologically important chromosome and cytokinesis regulator.
- **Conclusion**: Established evidence supports KIF4A as a second mitotic and cytokinetic anchor in the module. Its co-abundance with KIF11 is biologically plausible, whereas the broader module-wide coordination remains an inferred network property rather than a demonstrated common complex.

#### TK1

- **Related proteins** (co-abundance neighbors): SPDL1 (0.85); STRING partners: KIF11 (0.761), KIF4A (0.718)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thymidine kinase 1. The protein encoded by this gene is a cytosolic enzyme that catalyzes the addition of a gamma-phosphate group to thymidine. This creates dTMP and is the first step in the biosynthesis of dTTP, which is one component required for DNA replication. The encoded protein, whose levels fluctuate depending on the cell cycle stage, can act as a low activity dimer or a high activity tetramer. High levels of…
- **Diseases (Open Targets)**: COVID-19 (0.356); neurodegenerative disease (0.274); cancer (0.113); hepatocellular carcinoma (0.111); neoplasm (0.110)
- **Europe PMC papers**: 3410
- **Why important**: TK1 supplies the thymidine salvage step that produces dTMP for dTTP synthesis and DNA replication, with abundance that varies across the cell cycle. It is tissue enhanced in bone marrow and enriched in erythrocyte progenitors and other proliferative populations. STRING places it with KIF11 and KIF4A, connecting nucleotide supply to the mitotic machinery. Its literature record is extensive, including use of TK1 levels as a cancer proliferation biomarker.
- **Conclusion**: Established evidence supports TK1 as a proliferation and DNA-replication marker that complements the spindle genes. It likely reports the replication demand of cycling cells in the module, but it does not by itself establish that the module controls DNA synthesis.

#### NCAPD3

- **Related proteins** (co-abundance neighbors): AHCTF1 (0.87), KIF11 (0.86), PTPN2 (0.85), ASCC2 (0.83), SENP3 (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: non-SMC condensin II complex subunit D3. Condensin complexes I and II play essential roles in mitotic chromosome assembly and segregation. Both condensins contain 2 invariant structural maintenance of chromosome (SMC) subunits, SMC2 (MIM 605576) and SMC4 (MIM 605575), but they contain different sets of non-SMC subunits. NCAPD3 is 1 of 3 non-SMC subunits that define condensin II (Ono et al., 2003 [PubMed 14532007]).[supplied by OMIM, Mar …
- **Diseases (Open Targets)**: microcephaly 22, primary, autosomal recessive (0.615); autosomal recessive primary microcephaly (0.504); alcohol drinking (0.305); urolithiasis (0.276); bronchiectasis (0.233)
- **Europe PMC papers**: 458
- **Why important**: NCAPD3 is a defining non-SMC subunit of condensin II and is annotated for chromosome condensation and chromosome segregation. It has a comparatively central position in the network and connects to AHCTF1, KIF11, PTPN2, ASCC2, and SENP3, linking chromosome architecture to nuclear transport, signaling, DNA or ribosome quality control, and protein modification. HPA reports enrichment in lymphoid tissue and in several progenitor or dividing cell types. Its literature record is substantial, and its association with primary microcephaly provides disease relevance for chromosome segregation biology.
- **Conclusion**: Established evidence supports NCAPD3 as the module component most directly connecting mitotic chromosome architecture with the surrounding nuclear regulatory genes. Its role as a bridge between these processes in bone marrow and skin is a plausible but unproven module-level interpretation.

#### PTPN2

- **Related proteins** (co-abundance neighbors): NCAPD3 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein tyrosine phosphatase non-receptor type 2. The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. Members of the PTP family share a highly conserved catalytic motif, which is essential for the catalytic activity. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. Epidermal growth f…
- **Diseases (Open Targets)**: type 1 diabetes mellitus (0.510); Crohn disease (0.499); autoimmune disease (0.482); inflammatory bowel disease (0.476); rheumatoid arthritis (0.472)
- **Europe PMC papers**: 2852
- **Why important**: PTPN2 is a signaling phosphatase with supplied annotations covering negative regulation of proliferation, insulin-receptor signaling, tumor-necrosis-factor signaling, and B- and T-cell differentiation. It is tissue enhanced in lymphoid tissue and has strong disease associations with autoimmune and inflammatory disorders. In the module network it connects to NCAPD3, placing a signaling and differentiation regulator beside a chromosome-condensation component. Its literature record is extensive relative to most module genes.
- **Conclusion**: Established evidence supports PTPN2 as a regulator of immune-cell signaling and differentiation rather than as a canonical mitotic structural protein. Its presence may indicate coupling between proliferative state and hematopoietic signaling, but that coupling is a hypothesis and could also reflect shared cell-type composition.

## Module 8

**Tissue pair**: bone_marrow and skin  
**Genes (41)**: BLTP3A, BRI3BP, CARM1, CORO1A, GFM1, ERO1B, ETV6, GALK2, GEMIN8, GLMN, GNAS, GNAS, GOLT1B, H2AC21, H4C1, HAUS5, HERC2, KRT9, MAP7D3, MARF1, SLC16A1, MPI, MTRR, POR, NDUFB5, NUDT19, PDK3, PEX14, RABGGTA, PITRM1, PRUNE1, PTCD1, PTMS, RAB8B, SLC12A9, SLC27A4, SACM1L, SAMHD1, TKFC, UTP25, ZC3H14

### Function

No GO or KEGG term passed global correction, and STRING supplied no functional-enrichment term. Therefore, the module does not support a single statistically established pathway annotation. Its genes instead suggest a heterogeneous cellular program combining intracellular trafficking and membrane organization, mitochondrial translation and respiration, intermediary and lipid metabolism, chromatin or cell-cycle regulation, and selected hematopoietic or epithelial functions. The co-abundance structure is therefore more consistent with a shared cellular-state or cell-composition signal than with a discrete canonical pathway. The strongest interpretable network features include BLTP3A connections to histones, KRT9, GNAS, MPI, TKFC, and CARM1; a trafficking and fatty-acid-related branch involving SLC27A4, RABGGTA, and RAB proteins; and a mitochondrial branch involving PTCD1, GFM1, NDUFB5, and PDK3.

**Cell composition.** The module is not predominantly plasma or secreted: HPA identifies only one secreted gene, and nearly all genes have intracellular or membrane-associated descriptions. It is also not uniformly blood-cell enriched. Most genes have low immune-cell specificity, although selected members are enhanced in hematopoietic or immune populations, including CORO1A, ETV6, H2AC21, H4C1, RAB8B, and PDK3-associated cell contexts. The module is broadly expressed overall, with many genes having low tissue specificity and protein detection in both bone marrow and skin. Bone-marrow, lymphoid, neutrophil, monocyte-progenitor, megakaryocyte, and platelet signals coexist with epithelial, skeletal-muscle, liver, intestine, testis, and spermatid signals. This mixed profile makes shared cell types, sample cellular composition, or a broadly deployed cellular program plausible explanations for the cross-tissue conservation. The HPA signal does not support interpreting the module simply as a plasma-protein module or as a pure blood-cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only two high-confidence relationships within the module: H2AC21 with H4C1, and HERC2 with RABGGTA. These are useful anchors for a histone or chromatin branch and a protein-trafficking or ubiquitin-associated branch, respectively, but they do not establish a connected module-wide physical complex. hu.MAP supplies partial membership in several large complexes. RABGGTA and RAB8B occur together in the large Rab-associated complexes (hu.MAP huMAP3_11094.1) and (hu.MAP huMAP3_11860.1), NDUFB5 and GOLT1B occur together in (hu.MAP huMAP3_14018.1), and NUDT19 and GFM1 occur together in the broad mitochondrial and metabolic assembly (hu.MAP huMAP3_13468.1). In each case only a small subset of the complex is represented, so these results support known local relationships rather than a single shared complex. Most module edges have no corresponding STRING or hu.MAP relationship in the supplied evidence. The network consequently appears to combine several known biological neighborhoods with co-abundance links that are not currently supported as established physical interactions.

**STRING interactions (score >= 0.7)**: 2 of 820 gene pairs: H2AC21–H4C1 (0.961); HERC2–RABGGTA (0.768)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11094.1 (RABGGTA, RAB8B; 2/43); huMAP3_11860.1 (RABGGTA, RAB8B; 2/44); huMAP3_14018.1 (NDUFB5, GOLT1B; 2/48); huMAP3_13468.1 (NUDT19, GFM1; 2/99)

### Novelty

The conserved bone-marrow–skin co-abundance pattern may be a new systems-level observation, but the evidence does not justify calling the biological mechanism novel. The module contains well-established genes and several locally known relationships, including the H2AC21–H4C1 STRING interaction, the HERC2–RABGGTA STRING interaction, and the Rab, respiratory, and mitochondrial complex memberships in (hu.MAP huMAP3_11094.1) through (hu.MAP huMAP3_13468.1). At the same time, there is no globally significant GO or KEGG enrichment, no STRING functional-enrichment result, and limited interaction support for most module edges. Thus the cautious conclusion is that the particular cross-tissue co-abundance arrangement is potentially novel, whereas the component functions are not demonstrated to be novel. Absence from interaction databases cannot by itself establish discovery or biological novelty.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program present in selected bone-marrow and skin cell populations, in which intracellular trafficking and membrane lipid handling are coordinated with mitochondrial energy management, chromatin regulation, and lineage-specific functions. RABGGTA and RAB8B could mark a vesicle-trafficking component; SLC27A4 could connect membrane lipid transport to this component; PTCD1, GFM1, NDUFB5, and PDK3 could represent mitochondrial translation, respiratory-chain, and glucose-utilization demands; and histone genes together with CARM1, ETV6, and GNAS could reflect cell-state or differentiation regulation. This hypothesis predicts that the apparent module will vary with the abundance and activation state of epithelial, hematopoietic, and other metabolically active cells rather than behave as one universal biochemical complex. It requires validation with cell-resolved data, independent cohorts, perturbation, and protein-level interaction or localization assays.

### Important genes

#### BLTP3A

- **Related proteins** (co-abundance neighbors): H4C1; H4C2; H4C3; H4C4; H4C5; H4C6; H4C8; H4C9; H4C11; H4C12; H4C13; H4C14; H4C15; H4C16 (0.93), KRT9 (0.92), H2AC21 (0.91), GNAS (0.87), MPI (0.85), TKFC (0.84), GNAS (0.84), CARM1 (0.82), PTMS (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Nuclear membrane; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: bridge-like lipid transfer protein family member 3A. Enables histone deacetylase binding activity and identical protein binding activity. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: artificial cardiac pacemaker (0.340); coronary artery disorder (0.273); coronary atherosclerosis (0.261); obesity disorder (0.245); ulcerative colitis (0.235)
- **Europe PMC papers**: 24
- **Why important**: BLTP3A has the most central position in the supplied co-abundance structure and links otherwise different portions of the module, including histones, KRT9, GNAS, MPI, TKFC, and CARM1. Its annotation supports lipid-transfer biology and histone-deacetylase binding, while its HPA profile is broadly expressed and includes skin detection but not bone-marrow detection. The literature volume is modest, which makes BLTP3A a potentially informative, less-characterized network connector rather than a well-established pathway marker.
- **Conclusion**: Established evidence supports BLTP3A as a network connector with lipid-transfer and chromatin-associated annotations. It is a plausible organizing marker of the module, but a direct role in the shared bone-marrow–skin biology remains hypothetical.

#### GNAS

- **Related proteins** (co-abundance neighbors): GNAS (0.96), ERO1B (0.88), BLTP3A (0.84), PTCD1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GNAS complex locus. This locus has a highly complex imprinted expression pattern. It gives rise to maternally, paternally, and biallelically expressed transcripts that are derived from four alternative promoters and 5' exons. Some transcripts contain a differentially methylated region (DMR) at their 5' exons, and this DMR is commonly found in imprinted genes and correlates with transcript expression. An antisense tra…
- **Diseases (Open Targets)**: pseudohypoparathyroidism type 1A (0.839); pseudohypoparathyroidism type 1C (0.816); McCune-Albright syndrome (0.811); Albright hereditary osteodystrophy (0.798); pseudohypoparathyroidism type 1B (0.797)
- **Europe PMC papers**: 10304
- **Why important**: GNAS is a central connector near BLTP3A, ERO1B, and PTCD1 and has extensive literature and strong disease-association evidence. Its complex imprinted locus and roles in signal transduction, glucose homeostasis, inflammatory regulation, and water homeostasis make it capable of linking metabolic and signaling states. HPA detects it in both tissues and in several specialized cell contexts, including platelets and endocrine cells.
- **Conclusion**: Established evidence supports GNAS as a multifunctional signaling and metabolic regulator with substantial disease relevance. Its placement in this module may indicate a shared signaling state, but the co-abundance data do not establish that GNAS drives the other genes.

#### SLC27A4

- **Related proteins** (co-abundance neighbors): HERC2 (0.84), RABGGTA (0.83), GALK2 (0.82), GFM1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 27 member 4. This gene encodes a member of a family of fatty acid transport proteins, which are involved in translocation of long-chain fatty acids cross the plasma membrane. This protein is expressed at high levels on the apical side of mature enterocytes in the small intestine, and appears to be the principal fatty acid transporter in enterocytes. Clinical studies suggest this gene as a candidate gene for th…
- **Diseases (Open Targets)**: ichthyosis prematurity syndrome (0.805); neurodegenerative disease (0.485); hereditary disease (0.471); lamellar ichthyosis (0.414); autosomal recessive disease (0.370)
- **Europe PMC papers**: 947
- **Why important**: SLC27A4 occupies a bridge position between HERC2, RABGGTA, GALK2, and GFM1. It is a fatty-acid transporter involved in long-chain fatty-acid handling and is associated with ichthyosis prematurity syndrome and lamellar ichthyosis, making it especially relevant to skin biology. HPA detects it in both tissues, while its cell-type associations emphasize epithelial and absorptive populations rather than a specific immune lineage.
- **Conclusion**: Established evidence supports SLC27A4 as a membrane fatty-acid transport and skin-disease gene. Its module position supports a possible link between lipid handling and vesicle or mitochondrial biology, but that cross-tissue mechanism is a hypothesis.

#### ETV6

- **Related proteins** (co-abundance neighbors): ERO1B (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ETS variant transcription factor 6. This gene encodes an ETS family transcription factor. The product of this gene contains two functional domains: a N-terminal pointed (PNT) domain that is involved in protein-protein interactions with itself and other proteins, and a C-terminal DNA-binding domain. Gene knockout studies in mice suggest that it is required for hematopoiesis and maintenance of the developing vascular network. This gen…
- **Diseases (Open Targets)**: thrombocytopenia 5 (0.791); Thrombocytopenia (0.640); acute myeloid leukemia (0.632); cancer (0.602); hereditary disease (0.550)
- **Europe PMC papers**: 9689
- **Why important**: ETV6 connects the module to hematopoietic biology through its relationship with ERO1B and its HPA enhancement in hematopoietic stem cells, neutrophils, and thymocytes. It is an ETS-family transcription factor required for hematopoiesis and vascular development, and it has extensive literature and established associations with thrombocytopenia and leukemia.
- **Conclusion**: Established evidence supports ETV6 as a hematopoietic transcriptional regulator with major disease relevance. Its presence is compatible with a bone-marrow cell-state contribution, but it does not prove that the entire conserved module is hematopoietic in origin.

#### RABGGTA

- **Related proteins** (co-abundance neighbors): SLC27A4 (0.83); STRING partners: HERC2 (0.768)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: huMAP3_11094.1, huMAP3_11860.1
- **Function (MyGene.info)**: Rab geranylgeranyltransferase subunit alpha. Predicted to enable small GTPase binding activity. Predicted to contribute to Rab geranylgeranyltransferase activity. Predicted to be involved in protein geranylgeranylation. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.494); autoimmune disorder of central nervous system (0.319); primary familial polycythemia due to EPO receptor mutation (0.070); autosomal dominant severe congenital neutropenia (0.068); nonimmune chronic idiopathic neutropenia of adults (0.067)
- **Europe PMC papers**: 207
- **Why important**: RABGGTA is linked to SLC27A4 in the co-abundance graph, to HERC2 in STRING, and to RAB8B in the hu.MAP complexes (hu.MAP huMAP3_11094.1) and (hu.MAP huMAP3_11860.1). Its established function in Rab geranylgeranylation provides a mechanistic basis for membrane trafficking, while the complex evidence places it in known Rab-associated molecular neighborhoods. HPA shows detection in both tissues and epithelial cell-type associations.
- **Conclusion**: Established evidence supports RABGGTA as a component of Rab protein modification and vesicle-trafficking machinery. It is a strong candidate for the module's trafficking axis, although the module does not demonstrate a novel RABGGTA complex.

#### H2AC21

- **Related proteins** (co-abundance neighbors): BLTP3A (0.91); STRING partners: H4C1 (0.961)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: H2A clustered histone 21. Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Nucleosomes consist of approximately 146 bp of DNA wrapped around a histone octamer composed of pairs of each of the four core histones (H2A, H2B, H3, and H4). The chromatin fiber is further compacted through the interaction of a linker histone, H1, with the DNA between the…
- **Diseases (Open Targets)**: infectious disease (0.503); viral infectious disease (0.503); dengue disease (0.370); aortic stenosis (0.079); breast carcinoma (0.063)
- **Europe PMC papers**: 90
- **Why important**: H2AC21 is bone-marrow enriched by HPA and is associated with erythrocyte progenitors, megakaryocyte progenitors, monocyte progenitors, and neutrophil progenitors. It has a direct high-confidence STRING relationship with H4C1 and encodes a core histone involved in nucleosome structure and chromatin organization. Its connection to BLTP3A creates a chromatin-associated endpoint of the co-abundance structure.
- **Conclusion**: Established evidence supports H2AC21 as a histone associated with chromatin organization and hematopoietic progenitor contexts. Its module membership may report proliferative or lineage-composition effects in bone marrow, but it does not establish a specific chromatin mechanism shared with skin.

## Module 9

**Tissue pair**: bone_marrow and skin  
**Genes (5)**: FTH1, PIH1D1, UQCRC1, MRPL42, TIMCC

### Function

The module is most consistent with a weakly connected mitochondrial and cellular-maintenance program rather than a sharply defined pathway. MRPL42 is the network hub and is annotated for mitochondrial translation; UQCRC1 supports mitochondrial electron transport and oxidative phosphorylation; FTH1 supports intracellular iron storage and homeostasis; PIH1D1 supports snoRNP assembly, rRNA processing, protein stabilization, and cellular regulation; and TIMCC is a conserved mitochondrially localized chaperone. However, no GO or KEGG term passed global correction, and there was no supplementary STRING functional enrichment. Therefore, these annotations support a biological interpretation but do not establish a statistically enriched pathway. The star-like network centered on MRPL42 suggests coordinated abundance of genes related to mitochondrial protein production, respiration, and general cellular maintenance, while the absence of strong pathway enrichment argues against assigning a more specific canonical function.

**Cell composition.** The module is not dominated by secreted or plasma proteins: the HPA summary reports no secreted genes. All genes have low immune-cell specificity, and no blood-cell-enriched pattern was reported, which argues against a simple blood-cell contamination explanation. Most genes have low tissue specificity, with UQCRC1 showing tissue enhancement in heart muscle, skeletal muscle, and tongue. All genes show cell-type enhancement in at least one annotated cell type, including epithelial, germ-cell, immune dendritic, and intestinal cell types. Protein detection is present for most module genes in both bone marrow and skin, with one gene lacking tissue protein data in each tissue. The shared module may therefore reflect broadly present mitochondrial or cellular-maintenance biology, or shared cell-state composition, rather than a tissue-specific secreted or hematopoietic program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No pair among the module genes met the supplied STRING interaction threshold, and no STRING partners were reported for any member. No hu.MAP complex contained at least two module members. Thus, the co-abundance edges are not supported by the reported high-confidence physical-interaction resources. This does not disprove coordinated regulation or shared cellular context, but it means that the network should not be interpreted as a known physical complex. The apparent hub status of MRPL42 is a property of this co-abundance network, not an established STRING or hu.MAP interaction hub.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unrecognized co-abundance association in the bone-marrow and skin comparison, because its specific five-gene combination is not supported by the reported STRING or hu.MAP resources. Nevertheless, it cannot be called a new biological pathway or a confirmed novel mechanism. The absence of STRING and hu.MAP support alone does not prove novelty, and the lack of globally significant GO or KEGG enrichment limits functional specificity. A defensible conclusion is that the tissue-pair co-abundance pattern is potentially novel, whereas the individual gene functions are established and largely well studied.

**Hypothesis.** Hypothesis: variation in mitochondrial and cellular maintenance state across bone-marrow and skin samples produces coordinated abundance of MRPL42, UQCRC1, TIMCC, FTH1, and PIH1D1. MRPL42 may link mitochondrial protein synthesis to respiratory capacity through its co-abundance with UQCRC1, while FTH1 may reflect the iron and oxidative-stress environment accompanying mitochondrial activity. PIH1D1 may mark parallel demands for RNA processing and protein-complex assembly, and TIMCC may represent mitochondrial chaperone support. This hypothesis predicts that the module will track mitochondrial activity, respiratory demand, iron handling, or cellular stress more closely than a specific tissue lineage; it requires validation with independent cohorts, cell-composition adjustment, perturbation experiments, and direct measurements of respiration and mitochondrial translation.

### Important genes

#### MRPL42

- **Related proteins** (co-abundance neighbors): UQCRC1 (0.89), TIMCC (0.88), FTH1 (0.85), PIH1D1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial ribosomal protein L42. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.513); Parkinson disease (0.330); Alzheimer disease (0.329); lysosomal storage disease (0.329); Respiratory insufficiency (0.147)
- **Europe PMC papers**: 198
- **Why important**: MRPL42 is the central co-abundance node, connected to every other module member with the strongest aggregate network support in the supplied graph. It encodes a mitochondrial large-subunit ribosomal protein and is annotated for mitochondrial translation. Its broad tissue profile and detection in both bone marrow and skin fit a shared cellular-maintenance role. Its disease associations include neurodegenerative and lysosomal-storage disease categories, and its literature volume is substantial enough to support an established mitochondrial interpretation.
- **Conclusion**: Established evidence supports MRPL42 as the network hub and as a mitochondrial translation component. It is reasonable to hypothesize that MRPL42 helps organize the module's mitochondrial signal, but the co-abundance data do not establish that it causally regulates the other genes.

#### UQCRC1

- **Related proteins** (co-abundance neighbors): MRPL42 (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase core protein 1. Enables ubiquitin protein ligase binding activity. Predicted to be involved in oxidative phosphorylation. Predicted to act upstream of or within mitochondrial electron transport, ubiquinol to cytochrome c. Located in mitochondrion. Implicated in Alzheimer's disease. Biomarker of Alzheimer's disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: parkinsonism with polyneuropathy (0.642); neurodegenerative disease (0.569); Parkinson disease (0.521); Alzheimer disease (0.519); lysosomal storage disease (0.498)
- **Europe PMC papers**: 1860
- **Why important**: UQCRC1 is directly connected to MRPL42 and is the module member with the clearest respiratory annotation. It is a mitochondrial cytochrome-c-reductase core protein associated with oxidative phosphorylation, mitochondrial electron transport, aerobic respiration, and cellular respiration. Its tissue enhancement in muscle-related tissues is compatible with respiratory demand. It has extensive literature and disease associations involving neurodegenerative disorders.
- **Conclusion**: Established evidence supports UQCRC1 as a mitochondrial respiratory-chain component. Its presence strengthens a mitochondrial-energy interpretation of the module, but it does not prove that the module represents oxidative phosphorylation as a statistically enriched pathway.

#### FTH1

- **Related proteins** (co-abundance neighbors): MRPL42 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ferritin heavy chain 1. This gene encodes the heavy subunit of ferritin, the major intracellular iron storage protein in prokaryotes and eukaryotes. It is composed of 24 subunits of the heavy and light ferritin chains. Variation in ferritin subunit composition may affect the rates of iron uptake and release in different tissues. A major function of ferritin is the storage of iron in a soluble and nontoxic state. Defects …
- **Diseases (Open Targets)**: hemochromatosis type 5 (0.582); neurodegeneration with brain iron accumulation 9 (0.548); inherited retinal dystrophy (0.531); autosomal recessive bestrophinopathy (0.528); vitelliform macular dystrophy 2 (0.517)
- **Europe PMC papers**: 8350
- **Why important**: FTH1 is connected to the hub and encodes the heavy subunit of ferritin, the major intracellular iron-storage system. Its annotations include iron transport, intracellular iron homeostasis, autophagy, immune response, and erythrocyte differentiation. It is broadly detected in both tissues, has a broad cell-type profile, extensive literature, and multiple iron-related and retinal disease associations. FTH1 may connect mitochondrial activity with iron availability and oxidative-stress handling.
- **Conclusion**: Established evidence supports FTH1 as an intracellular iron-storage and homeostasis protein. Its inclusion supports an iron-related cellular-state interpretation, but the module does not demonstrate that iron regulation is its primary function or that FTH1 drives the co-abundance pattern.

#### PIH1D1

- **Related proteins** (co-abundance neighbors): MRPL42 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PIH1 domain containing 1. Enables several functions, including RNA polymerase I core promoter sequence-specific DNA binding activity; enzyme binding activity; and phosphoprotein binding activity. Involved in several processes, including box C/D snoRNP assembly; positive regulation of signal transduction; and regulation of cellular protein metabolic process. Located in cytoplasm and nucleolus. Part of R2TP complex and pre-s…
- **Diseases (Open Targets)**: neurodegenerative disease (0.437); mood disorder (0.059); depressive disorder (0.043); mental disorder (0.032); breast cancer (0.022)
- **Europe PMC papers**: 285
- **Why important**: PIH1D1 is connected to MRPL42 and encodes a protein involved in R2TP and pre-snoRNP complexes, box C/D snoRNP assembly, rRNA processing, protein stabilization, and cellular regulation. Its localization in cytosol and nucleolus provides a possible bridge between RNA and protein biogenesis and the mitochondrial-associated genes. It is detected in both tissues and has established disease-association annotations, although its literature volume is lower than that of FTH1 or UQCRC1.
- **Conclusion**: Established evidence supports PIH1D1 in RNA-processing and protein-complex assembly functions. Its connection to the module may reflect a broader biosynthetic or proteostasis state, but a direct mechanistic link to mitochondrial translation is only a hypothesis.

#### TIMCC

- **Related proteins** (co-abundance neighbors): MRPL42 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TIM double twin CX3C motif chaperone. This gene encodes a mitochondrially localized protein that is highly conserved across species. The gene is expressed in a variety of tissues including human lymphoblast cells and rat neurosensorial epithelium of the cristaampullaris. A mutation in this gene has been associated with familial Meniere's disease, a chronic disorder of the inner ear. Several pseudogenes of this gene are found on other …
- **Diseases (Open Targets)**: Meniere disease (0.356); Hypercholesterolemia (0.323); total hip arthroplasty (0.258); osteoarthritis, hip (0.258); ovarian dysfunction (0.232)
- **Europe PMC papers**: 14
- **Why important**: TIMCC is connected to MRPL42 and encodes a conserved mitochondrially localized protein described as a TIM double twin CX3C motif chaperone. It has a relatively small literature base compared with the other selected genes, but its mitochondrial localization and reported association with familial Meniere disease make it informative for interpreting the less-characterized edge of the module. Its cell-type enhancements include esophageal apical cells and oocytes, while its protein detection is unavailable in the supplied HPA summary.
- **Conclusion**: Established evidence supports TIMCC as a conserved mitochondrial protein with a disease association involving Meniere disease. Its role in this module is uncertain; the most plausible interpretation is that it marks mitochondrial proteostasis or chaperone activity, but this remains a hypothesis requiring independent validation.
