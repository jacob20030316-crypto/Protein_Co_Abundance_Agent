# Conserved co-abundance modules: cell line and circulatory_system

## Module 0

**Tissue pair**: cell line and circulatory_system  
**Genes (49)**: PGD, ACLY, ANKRD12, APMAP, ASL, BROX, CBLB, CCDC88B, CCDC92, CACNG6, CFAP20, CHST11, DAAM1, POLD3, EML2, EPPK1, FES, FHL1, FPGT, FYN, GNB5, GSAP, H1-5, H3-3A, IMUP, KSR1, MAN2C1, MCTP2, NCBP3, NDUFB5, NOP16, OGFRL1, SLC25A15, PDE7A, PLCB2, PLD6, PPP1R3D, RAB10, RBM15, RNF34, SFT2D2, SLCO3A1, SPTLC1, STOM, TSC22D3, UQCC3, VKORC1L1, VMA12, XPO5

### Function

No GO or KEGG term passed global correction, so there is no statistically established pathway-level function for this module. The gene annotations instead indicate a heterogeneous combination of cellular signaling, vesicle and membrane trafficking, metabolism, cytoskeletal organization, chromatin regulation, and hematopoietic biology. The network is sparse and organized around GSAP, with smaller branches involving metabolic genes, immune signaling genes, membrane transporters, and structural or regulatory proteins. The strongest functional interpretation is therefore a conserved co-abundance program reflecting shared cellular composition or broad cellular state rather than a single validated biochemical pathway. The known STRING links ACLY–ASL, ACLY–PGD, CBLB–FYN, and GNB5–PLCB2 support limited local functional coherence, but they do not establish a unified module function. The supplementary STRING and gene-level annotations are supportive context only, not globally significant enrichment evidence.

**Cell composition.** The module contains no secreted genes, so it is not a plasma-protein or secretome module. HPA evidence shows a mixture of broadly expressed genes and genes enhanced in particular tissues or cell types. Bone marrow and lymphoid tissue recur among enriched tissues, while neutrophils, neutrophil progenitors, eosinophils, basophils, NK cells, megakaryocytes, and macrophage-lineage cells recur among enriched cell types. Several genes are also associated with epithelial, neural, hepatic, muscular, or reproductive cell types. Thus, the module is not uniformly blood-cell specific, but its shared signal could plausibly be influenced by hematopoietic or circulatory cell composition, especially granulocyte-related populations. The broad HPA distribution and absence of secreted proteins argue against interpreting it as a coherent circulating protein program. Cell-composition adjustment and single-cell deconvolution would be important before assigning intrinsic biology to every member.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING contains only a small set of high-confidence relationships within the module: ACLY–ASL and ACLY–PGD connect metabolic genes; CBLB–FYN connects immune receptor regulation with tyrosine-kinase signaling; and GNB5–PLCB2 connects G-protein regulation with phospholipase signaling. These known links provide local support for several functional neighborhoods but leave most co-abundance edges without established physical or functional interaction evidence. hu.MAP provides partial support for two related complexes containing CHST11 and SLC25A15, with additional members outside the module, as recorded in (hu.MAP huMAP3_00587.1) and (hu.MAP huMAP3_06650.1). A separate hu.MAP complex links STOM and VMA12, with many non-module members, in (hu.MAP huMAP3_12042.1). Because each complex captures only a small subset of the module, the hu.MAP evidence supports local context rather than a single module-wide complex. Overall, co-abundance is substantially broader than currently curated interaction evidence.

**STRING interactions (score >= 0.7)**: 4 of 1176 gene pairs: ACLY–ASL (0.864); ACLY–PGD (0.717); CBLB–FYN (0.938); GNB5–PLCB2 (0.875)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00587.1 (CHST11, SLC25A15; 2/5); huMAP3_06650.1 (CHST11, SLC25A15; 2/6); huMAP3_12042.1 (STOM, VMA12; 2/56)

### Novelty

This should not be called a newly discovered biological pathway or complex. No GO or KEGG term passed global correction, STRING functional enrichment was absent, and only a minority of within-module relationships are represented by high-confidence STRING or hu.MAP evidence. The observation may still be novel as a cross-tissue co-abundance pattern, particularly because the full combination of genes and its conservation between cell line and circulatory_system is not directly represented by the available interaction resources. However, absence from STRING or hu.MAP does not demonstrate novelty: it may reflect incomplete curation, context-specific regulation, indirect associations, or cell-mixture effects. Replication in independent datasets, adjustment for blood-cell proportions, preservation testing, and experimental validation would be needed before claiming a novel biological module.

**Hypothesis.** Hypothesis: this module reflects a shared cellular-state and composition signal in which hematopoietic or circulatory cell representation contributes strongly, while a set of conserved housekeeping, metabolic, membrane-trafficking, and signaling genes provides the common transcriptional background. A possible mechanistic axis is coordinated regulation of membrane and vesicle processes together with immune-cell signal transduction, supported locally by the GNB5–PLCB2 and CBLB–FYN relationships, and coupled to metabolic activity through ACLY, ASL, and PGD. GSAP may act as a network-level abundance hub rather than a proven master regulator. This remains a hypothesis because the module has no globally significant pathway enrichment and the network edges are co-abundance relationships, not demonstrated causal interactions.

### Important genes

#### GSAP

- **Related proteins** (co-abundance neighbors): H1-5 (0.92), STOM (0.91), APMAP (0.90), DAAM1 (0.89), SLC25A15 (0.87), BROX (0.87), ASL (0.86), FHL1 (0.86), EPPK1 (0.83), H3-3A; H3-3B (0.82), VKORC1L1 (0.81), RAB10 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gamma-secretase activating protein. Accumulation of neurotoxic amyloid-beta is a major hallmark of Alzheimer disease (AD; MIM 104300). Formation of amyloid-beta is catalyzed by gamma-secretase (see PSEN1; MIM 104311), a protease with numerous substrates. PION, or GSAP, selectively increases amyloid-beta production through a mechanism involving its interaction with both gamma-secretase and its substrate, the amyloid-beta precursor pr…
- **Diseases (Open Targets)**: allergic rhinitis (0.453); atopic eczema (0.435); asthma (0.433); obesity disorder (0.411); allergic disease (0.393)
- **Europe PMC papers**: 263
- **Why important**: GSAP is the principal network hub in the supplied graph and connects genes spanning membrane vesicles, metabolism, cytoskeletal organization, and cellular transport. It is broadly expressed by HPA, with cell-type enhancement in B cells, Kupffer cells, and NK cells, and is localized to vesicles. Its established annotation links it to gamma-secretase regulation and amyloid-beta formation, while its disease and literature records are substantial. Its central network position makes it important for interpreting the module, although centrality alone does not establish a causal role.
- **Conclusion**: Established evidence: GSAP is a highly connected co-abundance hub with vesicular localization and a documented role in regulating amyloid-beta formation. Hypothesis: GSAP may coordinate a vesicle-associated cellular state represented across the two tissue groups, but this requires perturbation or longitudinal evidence.

#### FES

- **Related proteins** (co-abundance neighbors): VMA12 (0.83), TSC22D3 (0.83), OGFRL1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FES proto-oncogene, tyrosine kinase. This gene encodes the human cellular counterpart of a feline sarcoma retrovirus protein with transforming capabilities. The gene product has tyrosine-specific protein kinase activity and that activity is required for maintenance of cellular transformation. Its chromosomal location has linked it to a specific translocation event identified in patients with acute promyelocytic leukemia but it is als…
- **Diseases (Open Targets)**: hypertensive disorder (0.624); coronary artery disorder (0.592); essential hypertension (0.583); myocardial infarction (0.556); angina pectoris (0.551)
- **Europe PMC papers**: 11786
- **Why important**: FES links the module to hematopoietic and immune biology. HPA shows tissue enhancement in bone marrow and lymphoid tissue and cell-type enhancement in dendritic, macrophage, innate lymphoid, Hofbauer, and Kupffer cells. FES is a tyrosine kinase involved in normal hematopoiesis and growth factor or cytokine receptor signaling, and it has a large literature record. Its association with TSC22D3 and OGFRL1 places it in a signaling branch, while its disease associations include cardiovascular disorders and leukemia-related biology.
- **Conclusion**: Established evidence: FES is a hematopoietic signaling kinase with relevant HPA localization and substantial biological literature. Hypothesis: FES may mark or help transmit an immune-cell state shared by the sampled systems, but the co-abundance data do not show that FES drives the module.

#### PLCB2

- **Related proteins** (co-abundance neighbors): OGFRL1 (0.86), MAN2C1 (0.80); STRING partners: GNB5 (0.875)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phospholipase C beta 2. The protein encoded by this gene is a phosphodiesterase that catalyzes the hydrolysis of phosphatidylinositol 4,5-bisphosphate to the second messengers inositol 1,4,5-trisphosphate (IP3) and diacylglycerol. The encoded protein is activated by G proteins and has been shown to be involved in the type 2 taste receptor signal transduction pathway. In addition, nuclear factor kappa B can regulate the t…
- **Diseases (Open Targets)**: schizophrenia (0.345); myocardial infarction (0.330); coronary artery disorder (0.328); neurodegenerative disease (0.327); ischemic stroke (0.324)
- **Europe PMC papers**: 1756
- **Why important**: PLCB2 provides a mechanistic bridge between receptor signaling and second-messenger production. It hydrolyzes phosphatidylinositol bisphosphate to generate IP3 and diacylglycerol, is activated by G proteins, and is implicated in platelet responses. HPA shows enhancement in bone marrow and lymphoid tissue and in antigen-presenting or macrophage-lineage cell types. It has a direct STRING relationship with GNB5 and a substantial literature and disease-association record, including cardiovascular and cerebrovascular conditions.
- **Conclusion**: Established evidence: PLCB2 is a signaling enzyme with immune, platelet, and G-protein-related functions, supported locally by the GNB5–PLCB2 STRING relationship. Hypothesis: PLCB2 may represent a functional signaling node within a blood-cell-associated branch of the module, pending cell-type resolved validation.

#### CBLB

- **Related proteins** (co-abundance neighbors): GNB5 (0.86); STRING partners: FYN (0.938)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Cbl proto-oncogene B. This gene encodes an E3 ubiquitin-protein ligase which promotes proteosome-mediated protein degradation by transferring ubiquitin from an E2 ubiquitin-conjugating enzyme to a substrate. The encoded protein is involved in the regulation of immune response by limiting T-cell receptor, B-cell receptor, and high affinity immunoglobulin epsilon receptor activation. Studies in mouse suggest that this ge…
- **Diseases (Open Targets)**: hypothyroidism (0.547); urticaria (0.488); myxedema (0.463); Hashimoto thyroiditis (0.429); thyroid gland disorder (0.420)
- **Europe PMC papers**: 2144
- **Why important**: CBLB is an E3 ubiquitin ligase that limits T-cell receptor, B-cell receptor, and high-affinity immunoglobulin receptor activation. It has cell-type enhancement in NK cells and several immune or vascular-associated populations, and it forms a high-confidence STRING relationship with FYN. Its disease associations include thyroid and immune disorders, and its literature record is broad. Although it has only a peripheral co-abundance position in this module, its known regulatory function makes it biologically informative.
- **Conclusion**: Established evidence: CBLB is a negative regulator of immune receptor signaling and is linked to FYN by STRING evidence. Hypothesis: the CBLB–FYN neighborhood may reflect coordinated tuning of immune activation in the shared module, but this cannot be separated from changes in immune-cell abundance using the supplied data alone.

#### CHST11

- **Related proteins** (co-abundance neighbors): ANKRD12 (0.89), KSR1 (0.87), NDUFB5 (0.83), CCDC88B (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_00587.1, huMAP3_06650.1
- **Function (MyGene.info)**: carbohydrate sulfotransferase 11. The protein encoded by this gene belongs to the sulfotransferase 2 family. It is localized to the golgi membrane, and catalyzes the transfer of sulfate to position 4 of the N-acetylgalactosamine (GalNAc) residue of chondroitin. Chondroitin sulfate constitutes the predominant proteoglycan present in cartilage, and is distributed on the surfaces of many cells and extracellular matrices. A chromosoma…
- **Diseases (Open Targets)**: osteochondrodysplasia, brachydactyly, and overlapping malformed digits (0.506); osteoarthritis (0.399); smoking initiation (0.340); keloid (0.318); neurodegenerative disease (0.279)
- **Europe PMC papers**: 968
- **Why important**: CHST11 is a Golgi carbohydrate sulfotransferase that modifies chondroitin and participates in proteoglycan biosynthesis. HPA shows enhancement in bone marrow and choroid plexus, with enrichment among hematopoietic progenitors, macrophages, microglia, and granulocyte-related cell types. It is one of the few genes supported by hu.MAP membership, appearing with SLC25A15 in (hu.MAP huMAP3_00587.1) and (hu.MAP huMAP3_06650.1). Its disease associations include osteoarthritis and skeletal developmental disorders, and its literature record is substantial.
- **Conclusion**: Established evidence: CHST11 has a defined Golgi glycosaminoglycan-related function, hematopoietic and bone-marrow HPA associations, and partial hu.MAP support. Hypothesis: CHST11 may indicate a cell-surface or extracellular-matrix remodeling component of the shared state, but the module does not establish a direct CHST11-centered complex.

## Module 1

**Tissue pair**: cell line and circulatory_system  
**Genes (43)**: ABHD15, ADA2, AKT3, B4GALT1, BLVRB, CTSF, BCHE, CD300A, CPEB4, CTDSPL, DCD, FCGRT, CBLL1, HLA-F, HPSE, HYPK, IDUA, JCHAIN, JAM3, KNG1, RPS6KC1, LRRC7, MLX, SLC16A3, NIPSNAP2, NOL8, NUDT16, PIK3R2, SERPINB2, PLD4, PRG2, PTPRZ1, RBP7, RIC1, RNF185, SERPINB8, SPPL2A, SWAP70, TRAF5, TREX1, TTC38, TXNIP, ZFYVE1

### Function

The strongest defensible interpretation is an extracellular and circulatory immune-associated module rather than a single well-defined intracellular pathway. The only globally corrected GO/KEGG evidence is (GO:CC extracellular region; q_global = 0.0364), enrichment for the extracellular region, with contributions from secreted proteins, membrane proteins, vesicular proteins, and proteins associated with immune or blood-cell biology. The supplementary STRING terms (STRING Keyword Signal; within-query FDR = 0.0001) through (STRING Component Extracellular space; within-query FDR = 0.0425) are concordant with signal peptides, disulfide-bonded or glycoprotein products, secretion, and extracellular localization, but they are not global enrichment evidence. Functionally, the module brings together extracellular proteolysis and matrix remodeling, humoral immunity, leukocyte signaling, glycosylation, blood coagulation and kinin biology, and intracellular trafficking. The co-abundance graph is sparse and chain-like, with a few relatively central connectors rather than a densely interconnected canonical complex. Thus, the module most likely captures a shared extracellular and immune-related abundance program, potentially influenced by circulating proteins and shared immune-cell content.

**Cell composition.** The module is compositionally biased toward extracellular and blood-associated biology. HPA annotations identify many secreted genes, including ADA2, KNG1, BCHE, ABHD15, JCHAIN, JAM3, HPSE, DCD and related products. Several genes are enriched in liver, consistent with plasma protein production, while others are enriched in lymphoid tissue, bone marrow, neutrophils, monocytes, basophils, plasmacytoid dendritic cells, memory B cells, plasma cells or other immune populations. The HPA summary also shows that many genes are cell-type enhanced, with neutrophil and Kupffer-cell signals recurring prominently. A smaller component has neural, epithelial, skin, placental or muscle-associated expression, and some genes are broadly expressed. Therefore, the shared module may partly reflect blood or immune-cell composition in the samples, or shared cell types, rather than coordinated regulation within a single cellular pathway. The absence of matching HPA protein-detection calls for the two named sample groups limits protein-level confirmation.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC extracellular region | 0.0364 | ABHD15, ADA2, B4GALT1, BCHE, BLVRB, CD300A, CTDSPL, CTSF, DCD, FCGRT, HLA-F, HPSE, IDUA, JAM3, JCHAIN, KNG1, PRG2, PTPRZ1, SERPINB2, SERPINB8, SPPL2A, TTC38 |

### STRING and hu.MAP

STRING provides only a small number of high-confidence pairwise relationships within the module. The best-supported relationships are AKT3 with PIK3R2, CBLL1 with SLC16A3, and CD300A with PRG2. The CD300A–PRG2 link is biologically compatible with leukocyte signaling and eosinophil or granule-associated biology; the AKT3–PIK3R2 link supports a PI3K-AKT signaling connection; and the CBLL1–SLC16A3 link connects adhesion or ubiquitin-related regulation with monocarboxylate transport. These links do not explain the entire module. hu.MAP identifies partial membership of ABHD15 and AKT3 in complexes also containing AKT family members (hu.MAP huMAP3_02055.1) and (hu.MAP huMAP3_10657.1), and partial membership of PTPRZ1 and SPPL2A in a much larger membrane-associated complex (hu.MAP huMAP3_11349.1). Because most module pairs lack corresponding STRING or hu.MAP support, the abundance network should be interpreted primarily as a co-abundance association, not as a demonstrated physical complex.

**STRING interactions (score >= 0.7)**: 3 of 903 gene pairs: AKT3–PIK3R2 (0.967); CBLL1–SLC16A3 (0.834); CD300A–PRG2 (0.759)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Signal (FDR = 0.0001, 17 genes); Keyword Disulfide bond (FDR = 0.0001, 17 genes); Keyword Glycoprotein (FDR = 0.00026, 18 genes); Keyword Secreted (FDR = 0.00034, 12 genes); Component Extracellular region (FDR = 0.014, 23 genes); Component Extracellular space (FDR = 0.0425, 20 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02055.1 (ABHD15, AKT3; 2/3); huMAP3_10657.1 (ABHD15, AKT3; 2/4); huMAP3_11349.1 (PTPRZ1, SPPL2A; 2/78)

### Novelty

The module may represent a novel cross-tissue co-abundance pattern, but the fact sheet does not establish a new molecular mechanism. Its strongest evidence is the coordinated abundance of extracellular, secreted, hepatic and immune-cell-associated genes across cell line and circulatory_system samples. The limited overlap with known STRING interactions and the partial hu.MAP matches suggest that the full module is not an established physical interaction network. However, absence from those resources cannot prove novelty because databases are incomplete, context-dependent and biased toward well-studied proteins. The extracellular theme, blood-cell composition signal, and known functions of several members are already well established. A genuinely new finding would therefore be the reproducible cross-tissue co-abundance organization or its context dependence, not the discovery of a wholly new extracellular or immune pathway. Independent replication, adjustment for cell composition, and validation at the protein level would be needed to support that claim.

**Hypothesis.** Hypothesis: this module reflects a circulating immune-extracellular interface in which hepatic and blood-derived secreted proteins are co-abundant with leukocyte receptors, granule proteins, extracellular-matrix remodeling enzymes and vesicular or lysosomal components. ADA2, HPSE, KNG1 and BCHE could link inflammatory-cell state, proteoglycan remodeling, kinin or coagulation biology and extracellular enzyme activity, while CD300A and PRG2 could represent a myeloid or granulocyte-associated branch. The module may thus report a mixture of circulating protein production and immune-cell abundance that is shared between the two tissue groups. This is a mechanistic hypothesis, not a demonstrated causal model; the sparse physical-interaction evidence and heterogeneous HPA localization argue for testing it with cell-composition correction, sorted-cell measurements, plasma proteomics and perturbation experiments.

### Important genes

#### ADA2

- **Related proteins** (co-abundance neighbors): CPEB4 (0.97), MLX (0.95), RPS6KC1 (0.91), ZFYVE1 (0.86), B4GALT1 (0.83), IDUA (0.82), FCGRT (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenosine deaminase 2. This gene encodes a member of a subfamily of the adenosine deaminase protein family. The encoded protein is one of two adenosine deaminases found in humans, which regulate levels of the signaling molecule, adenosine. The encoded protein is secreted from monocytes undergoing differentiation and may regulate cell proliferation and differentiation. This gene may be responsible for some of the phenoty…
- **Diseases (Open Targets)**: polyarteritis nodosa, childhoood-onset (0.819); Sneddon syndrome (0.771); Diamond-Blackfan anemia (0.597); autoinflammatory syndrome (0.507); Behcet disease (0.477)
- **Europe PMC papers**: 2846
- **Why important**: ADA2 is the strongest network hub in the supplied ranking and connects to several module branches, including B4GALT1, IDUA and FCGRT. It is globally represented in (GO:CC extracellular region; q_global = 0.0364) and in all listed STRING supplementary themes (STRING Keyword Signal; within-query FDR = 0.0001) through (STRING Component Extracellular space; within-query FDR = 0.0425). HPA places it in lymphoid tissue, monocyte-lineage cell types and the blood secretome. Its established function is a secreted adenosine deaminase associated with monocyte differentiation and regulation of adenosine-related signaling. It also has extensive literature and disease associations involving inflammatory and vascular disorders.
- **Conclusion**: Established evidence supports ADA2 as a central extracellular and immune-associated marker of the module. It is a plausible integrative biomarker, but the co-abundance data do not establish that ADA2 drives the other genes. A causal role in coordinating the module remains hypothetical.

#### KNG1

- **Related proteins** (co-abundance neighbors): BCHE (0.91), MLX (0.88), SERPINB2 (0.85), DCD (0.84); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kininogen 1. This gene uses alternative splicing to generate two different proteins- high molecular weight kininogen (HMWK) and low molecular weight kininogen (LMWK). HMWK is essential for blood coagulation and assembly of the kallikrein-kinin system. Also, bradykinin, a peptide causing numerous physiological effects, is released from HMWK. Bradykinin also functions as an antimicrobial peptide with antibacteri…
- **Diseases (Open Targets)**: congenital high-molecular-weight kininogen deficiency (0.733); venous thromboembolism (0.547); hereditary angioedema (0.458); serum lipopolysaccharide activity (0.367); ischemic stroke (0.363)
- **Europe PMC papers**: 2325
- **Why important**: KNG1 is a prominent connector among BCHE, MLX, SERPINB2 and DCD and is represented in (GO:CC extracellular region; q_global = 0.0364) and the full set of supplementary STRING themes (STRING Keyword Signal; within-query FDR = 0.0001) through (STRING Component Extracellular space; within-query FDR = 0.0425). HPA identifies it as liver-enriched and secreted to blood. Its established biology is especially relevant to the circulatory context: high-molecular-weight kininogen participates in coagulation and the kallikrein-kinin system, with bradykinin release and effects on vascular signaling. It has substantial literature and disease associations involving kininogen deficiency, thromboembolism, angioedema and stroke.
- **Conclusion**: Established evidence supports KNG1 as a plasma-derived vascular and proteolytic anchor for the module. It may help explain the circulatory component, but its co-abundance with immune and epithelial genes does not prove coordinated kinin-system activation.

#### CD300A

- **Related proteins** (co-abundance neighbors): NOL8 (0.86), CPEB4 (0.85), CBLL1 (0.83); STRING partners: PRG2 (0.759)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD300a molecule. This gene encodes a member of the CD300 glycoprotein family of cell surface proteins found on leukocytes involved in immune response signaling pathways. This gene is located on chromosome 17 in a cluster with all but one of the other family members. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2012].
- **Diseases (Open Targets)**: dengue disease (0.375); injury (0.255); neoplasm (0.104); acute myeloid leukemia (0.099); diffuse large B-cell lymphoma (0.078)
- **Europe PMC papers**: 982
- **Why important**: CD300A occupies a network position connecting CPEB4, NOL8 and CBLL1 and has the module's explicitly supported STRING relationship with PRG2. It is represented in (GO:CC extracellular region; q_global = 0.0364) and several supplementary extracellular and glycoprotein terms. HPA places it in lymphoid tissue and in dendritic, macrophage, Kupffer-cell and mast-cell populations, with intracellular and plasma-membrane localization. Its established function is leukocyte surface immune signaling, including negative regulation of mast-cell activation, degranulation, B-cell proliferation and innate receptor signaling.
- **Conclusion**: Established evidence supports CD300A as an immune-cell signaling component and as the clearest bridge to PRG2 in the known interaction data. It is a strong candidate for testing whether the module reflects myeloid or granulocyte composition, while any role in organizing the entire module remains hypothetical.

#### PRG2

- **Related proteins** (co-abundance neighbors): RBP7 (0.92), JCHAIN (0.88), ABHD15 (0.85), PTPRZ1 (0.81); STRING partners: CD300A (0.759)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteoglycan 2, pro eosinophil major basic protein. The protein encoded by this gene is the predominant constituent of the crystalline core of the eosinophil granule. High levels of the proform of this protein are also present in placenta and pregnancy serum, where it exists as a complex with several other proteins including pregnancy-associated plasma protein A (PAPPA), angiotensinogen (AGT), and C3dg. This protein may be involved in antiparasitic…
- **Diseases (Open Targets)**: hypothyroidism (0.118); prostate carcinoma (0.097); Familial prostate cancer (0.096); prostate cancer (0.096); retinitis pigmentosa (0.070)
- **Europe PMC papers**: 38412
- **Why important**: PRG2 links RBP7, JCHAIN, ABHD15 and PTPRZ1 in the co-abundance graph and forms the supported STRING pair with CD300A. It is present in (GO:CC extracellular region; q_global = 0.0364) and all listed supplementary STRING themes (STRING Keyword Signal; within-query FDR = 0.0001) through (STRING Component Extracellular space; within-query FDR = 0.0425). HPA identifies it as enriched in placenta, specific to extravillous trophoblasts and enriched in basophils, with secretion in the female reproductive system. Its established function is as the major basic protein precursor of eosinophil granules, with roles in antiparasitic defense and hypersensitivity reactions. It has a very extensive literature base.
- **Conclusion**: Established evidence supports PRG2 as a secretory granule and allergic or eosinophil-associated marker, and the CD300A link strengthens an immune-cell interpretation. Its presence may reflect granulocyte-related abundance or a context-specific secretory program; a direct functional role across all module members is not established.

#### HPSE

- **Related proteins** (co-abundance neighbors): TREX1 (0.91), CTSF (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparanase. Heparan sulfate proteoglycans are major components of the basement membrane and extracellular matrix. The protein encoded by this gene is an enzyme that cleaves heparan sulfate proteoglycans to permit cell movement through remodeling of the extracellular matrix. In addition, this cleavage can release bioactive molecules from the extracellular matrix. Several transcript variants encoding different …
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.385); liver cancer (0.262); vitiligo (0.225); hemangioma (0.174); lymphangioma (0.174)
- **Europe PMC papers**: 1953
- **Why important**: HPSE connects TREX1 and CTSF and is represented in (GO:CC extracellular region; q_global = 0.0364) and the supplementary signal, glycoprotein, secreted and extracellular terms (STRING Keyword Signal; within-query FDR = 0.0001) through (STRING Component Extracellular space; within-query FDR = 0.0425). HPA associates it with monocytes, neutrophils and Kupffer cells and with secretion to the extracellular matrix. Its established function is cleavage of heparan sulfate proteoglycans, allowing matrix remodeling and release of bioactive molecules; its annotated biology also includes inflammatory and cell-matrix processes. It has substantial literature and disease associations involving liver cancer, vascular lesions and inflammatory disease.
- **Conclusion**: Established evidence supports HPSE as a plausible extracellular-matrix and inflammation bridge between immune-cell state and circulating extracellular biology. It is a useful mechanistic candidate, but the module does not demonstrate that HPSE activity causes the observed co-abundance pattern.

## Module 2

**Tissue pair**: cell line and circulatory_system  
**Genes (38)**: ABLIM1, ANKRD28, ASRGL1, BLMH, CAPN7, CCNH, CDC6, CHD1L, CNOT4, CWC27, DCP1A, DHX36, DPCD, POLA1, EXOC3, GON7, HEATR6, HIP1R, INTS9, KDM8, KGD4, RNGTT, PARP16, PIAS1, PSMB3, CAD, RB1CC1, ARHGAP19, RNASEL, SCOC, SECISBP2, BNIP1, STAM, STXBP1, TRMT1L, TTI2, XPO6, ZCCHC9

### Function

The strongest statistically supported interpretation is a nuclear, broadly cellular module rather than a single narrowly defined pathway. The sole globally corrected GO term is nuclear localization (GO:CC nucleus; q_global = 0.0464), covering most module genes; the corresponding STRING nuclear component annotation (STRING Component Nucleus; within-query FDR = 0.011) is supplementary and consistent with it. The gene annotations suggest several connected processes: DNA replication initiation and checkpoint control through CDC6, POLA1 and TTI2; chromatin and DNA-damage responses through CHD1L, PIAS1 and RB1CC1; RNA processing and quality control through RNGTT, INTS9, CWC27, DCP1A, DHX36 and RNASEL; and intracellular transport or membrane-associated processes through XPO6, STXBP1, BNIP1 and EXOC3. Thus, the most defensible function is coordinated nuclear maintenance and proliferative or stress-response biology, with contributions from RNA handling, genome integrity, and intracellular trafficking. The enrichment does not establish that all genes act in one physical pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, which is compatible with broadly expressed housekeeping-type biology. At the same time, many genes are cell-type enhanced, especially in spermatogenic cells, neutrophils and erythrocyte progenitors, and several show immune-cell enhancement or enrichment, including genes associated with basophils, eosinophils, neutrophils and monocyte populations. The module therefore may partly reflect shared cell types or sample-composition effects in cell line and circulatory-system material, rather than a tissue-specific circulating program. The HPA evidence does not support assigning the module specifically to blood cells, because most genes have low immune-cell specificity and the cell-type signals are heterogeneous.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC nucleus | 0.0464 | ANKRD28, ARHGAP19, ASRGL1, BLMH, BNIP1, CAD, CAPN7, CCNH, CDC6, CHD1L, CNOT4, CWC27, DCP1A, DHX36, DPCD, GON7, INTS9, KDM8, PARP16, PIAS1, POLA1, PSMB3, RB1CC1, RNASEL, RNGTT, SCOC, SECISBP2, STXBP1, TRMT1L, TTI2, XPO6, ZCCHC9 |

### STRING and hu.MAP

The high-confidence STRING evidence is sparse but informative. CDC6 and POLA1 form a known-looking DNA-replication relationship that supports the genome-replication interpretation, while ASRGL1 and CAD form the other high-confidence pair and may reflect linked metabolic biology. The supplementary STRING nuclear-component annotation (STRING Component Nucleus; within-query FDR = 0.011) agrees with (GO:CC nucleus; q_global = 0.0464), but it is not independent global enrichment evidence. hu.MAP provides partial complex-level support: XPO6, TTI2 and HIP1R occur together in (hu.MAP huMAP3_11232.1); ANKRD28 and RNASEL occur together in (hu.MAP huMAP3_12079.1); and STXBP1 and BNIP1 occur together in (hu.MAP huMAP3_13160.1). These complexes connect nuclear transport, signaling or cell-cycle regulation, and vesicle trafficking, but only subsets of their members are present. Overall, the network contains a small number of recognizable relationships embedded in a much larger set of co-abundance links, so it should not be treated as a single experimentally established protein complex.

**STRING interactions (score >= 0.7)**: 2 of 703 gene pairs: ASRGL1–CAD (0.904); CDC6–POLA1 (0.907)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Nucleus (FDR = 0.011, 32 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11232.1 (HIP1R, TTI2, XPO6; 3/78); huMAP3_12079.1 (ANKRD28, RNASEL; 2/12); huMAP3_13160.1 (STXBP1, BNIP1; 2/49)

### Novelty

The conserved co-abundance pattern is plausibly a new systems-level observation, but the data do not prove that it is a new molecular pathway. The case for novelty is that the module combines genes from genome replication, RNA regulation, immune or antiviral response, nuclear transport, vesicle biology and cell-type-associated expression, while STRING supplies only limited direct pairwise support and hu.MAP supplies only partial complex overlap. Conversely, several component relationships and functions are already established, including CDC6 with POLA1, the Triple T damage-response role of TTI2, RNASEL antiviral biology, and XPO6 nuclear export. Therefore the novelty is best stated as a conserved cross-tissue co-abundance organization or regulatory state, not as discovery of previously unknown gene functions or a new physical complex. Absence from STRING or hu.MAP is treated as limited database support, not as proof of novelty.

**Hypothesis.** Hypothesis: the module represents a coordinated state of proliferative or stressed cells in which nuclear genome maintenance and RNA processing are coupled to transport, proteostasis and innate immune regulation. In this model, CDC6 and POLA1 mark replication competence, TTI2 and PIAS1 help constrain damage or signaling responses, RNASEL and related RNA-processing genes provide antiviral or RNA-quality control, and XPO6 links nuclear cargo handling to cytoskeletal or cell-type-specific programs. The heterogeneous HPA cell-type pattern raises the alternative possibility that the apparent conservation is driven partly by shared proliferating or immune-associated cell populations in the two sample groups. This hypothesis requires validation with cell-resolved measurements, perturbation of hub genes, and independent replication of the co-abundance pattern.

### Important genes

#### CDC6

- **Related proteins** (co-abundance neighbors): CCNH (0.97), CAPN7 (0.94), TTI2 (0.93), TRMT1L (0.92), RB1CC1 (0.89), HEATR6 (0.87), RNGTT (0.86), CHD1L (0.85), INTS9 (0.85), CAD (0.84), EXOC3 (0.83), STXBP1 (0.83), CWC27 (0.83), DHX36 (0.82), POLA1 (0.81); STRING partners: POLA1 (0.907)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell division cycle 6. The protein encoded by this gene is highly similar to Saccharomyces cerevisiae Cdc6, a protein essential for the initiation of DNA replication. This protein functions as a regulator at the early steps of DNA replication. It localizes in cell nucleus during cell cyle G1, but translocates to the cytoplasm at the start of S phase. The subcellular translocation of this protein during cell cyle is regu…
- **Diseases (Open Targets)**: Meier-Gorlin syndrome (0.718); neurodegenerative disease (0.462); neoplasm (0.113); hepatocellular carcinoma (0.112); microcephaly (0.112)
- **Europe PMC papers**: 7261
- **Why important**: CDC6 is the central network gene in the supplied subgraph, with the strongest connectivity and links to CCNH, CAPN7, TTI2, TRMT1L, RB1CC1, HEATR6, RNGTT and CHD1L. Its established role is initiation and regulation of DNA replication, and its relationship with POLA1 is supported by high-confidence STRING evidence. It is included in the globally corrected nuclear term (GO:CC nucleus; q_global = 0.0464) and is enhanced in bone marrow and lymphoid tissue, including erythrocyte progenitors and plasmacytoid dendritic cells. Its extensive literature and disease associations make it the best anchor for distinguishing a replication or cell-cycle component from a purely compositional signal.
- **Conclusion**: Established evidence supports CDC6 as a genome-replication and cell-cycle anchor of the module. It is plausible, but not established, that CDC6 organizes the broader co-abundance state or explains its conservation across the two tissue groups.

#### ARHGAP19

- **Related proteins** (co-abundance neighbors): GON7 (0.94), DPCD (0.89), PSMB3 (0.88), ANKRD28 (0.87), XPO6 (0.86), DCP1A (0.83), RNASEL (0.81), CWC27 (0.81), BLMH (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho GTPase activating protein 19. Members of the ARHGAP family, such as ARHGAP19, encode negative regulators of Rho GTPases (see RHOA; MIM 165390), which are involved in cell migration, proliferation, and differentiation, actin remodeling, and G1 cell cycle progression (Lv et al., 2007 [PubMed 17454002]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: motor peripheral neuropathy (0.462); Abnormality of the skeletal system (0.190); methicillin-resistant staphylococcus aureus infectious disease (0.177); Abnormal blistering of the skin (0.177); type 2 diabetes mellitus (0.137)
- **Europe PMC papers**: 279
- **Why important**: ARHGAP19 is one of the more connected genes and links GON7, DPCD, PSMB3, ANKRD28, XPO6, DCP1A, RNASEL and CWC27. Its established molecular role is negative regulation of Rho GTPases, which connects the module to signaling, migration, proliferation and actin remodeling. It is part of (GO:CC nucleus; q_global = 0.0464) and (STRING Component Nucleus; within-query FDR = 0.011), is enhanced in lymphoid tissue, and is enriched in several differentiating germ-cell and erythroid contexts. Despite its useful network position, it has much less literature than CDC6, making it a potentially informative but comparatively under-characterized bridge.
- **Conclusion**: Established evidence supports ARHGAP19 as a signaling and cytoskeletal regulator embedded in the nuclear-associated module. The hypothesis that it bridges cell-state signaling with the replication and RNA-control components is supported by network topology but remains untested.

#### RNASEL

- **Related proteins** (co-abundance neighbors): ARHGAP19 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12079.1
- **Function (MyGene.info)**: ribonuclease L. This gene encodes a component of the interferon-regulated 2-5A system that functions in the antiviral and antiproliferative roles of interferons. The protein is involved in innate immunity and is active against multiple RNA viruses, including the influenza and SARS-CoV-2 viruses. Mutations in this gene have been associated with predisposition to prostate cancer and this gene is a candidate for the…
- **Diseases (Open Targets)**: Familial prostate cancer (0.547); ovarian cancer (0.337); prostate cancer (0.285); circadian rhythm (0.168); type 2 diabetes mellitus (0.127)
- **Europe PMC papers**: 2008
- **Why important**: RNASEL connects to ARHGAP19 and is included in the nuclear annotation (GO:CC nucleus; q_global = 0.0464) and the supplementary STRING annotation (STRING Component Nucleus; within-query FDR = 0.011). Its established function is in the interferon-regulated two-five-A system, antiviral defense and antiproliferative responses, with additional roles in RNA processing and gene regulation. HPA places it among neutrophil-enhanced cell types, while disease resources associate it with hereditary and sporadic prostate cancer and other conditions. Its substantial literature makes it a strong candidate for an immune or stress-response contribution, even though its direct STRING support within this module is absent.
- **Conclusion**: Established evidence supports RNASEL as an antiviral, antiproliferative and RNA-control component. Its membership may indicate an interferon-related or immune-associated cell state, but the module data alone do not demonstrate interferon activation.

#### SECISBP2

- **Related proteins** (co-abundance neighbors): ASRGL1 (0.85), PSMB3 (0.83), XPO6 (0.82), SCOC (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SECIS binding protein 2. The protein encoded by this gene is one of the essential components of the machinery involved in co-translational insertion of selenocysteine (Sec) into selenoproteins. Sec is encoded by the UGA codon, which normally signals translation termination. The recoding of UGA as Sec codon requires a Sec insertion sequence (SECIS) element; present in the 3' untranslated regions of eukaryotic selenoprotein…
- **Diseases (Open Targets)**: thyroid hormone metabolism, abnormal 1 (0.795); thyroid hormone metabolism, abnormal (0.654); thoracic aortic aneurysm (0.370); poisoning (0.207); hereditary disease (0.194)
- **Europe PMC papers**: 673
- **Why important**: SECISBP2 forms a local network bridge to ASRGL1, PSMB3, XPO6 and SCOC and is included in (GO:CC nucleus; q_global = 0.0464) and (STRING Component Nucleus; within-query FDR = 0.011). Its established function is essential for co-translational selenocysteine insertion into selenoproteins, linking it to selenium-dependent protein homeostasis and thyroid-hormone biology. It is broadly expressed by HPA tissue classification but is enhanced in late primary spermatocytes and late spermatids, providing a possible cell-state context for part of the module. Its literature volume is moderate and its disease associations include abnormal thyroid-hormone metabolism and thoracic aortic aneurysm.
- **Conclusion**: Established evidence supports SECISBP2 as a translational and selenium-homeostasis component. Its network placement suggests a possible connection between protein-quality control and nuclear transport, but that connection is a hypothesis rather than a demonstrated mechanism.

#### XPO6

- **Related proteins** (co-abundance neighbors): ZCCHC9 (0.86), ARHGAP19 (0.86), SECISBP2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enriched; location Nucleoplasm, Nucleoli; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11232.1
- **Function (MyGene.info)**: exportin 6. The protein encoded by this gene is a member of the importin-beta family. Members of this family are regulated by the GTPase Ran to mediate transport of cargo across the nuclear envelope. This protein has been shown to mediate nuclear export of profilin-actin complexes. A pseudogene of this gene is located on the long arm of chromosome 14. Alternative splicing results in multiple transcript varian…
- **Diseases (Open Targets)**: neurodegenerative disease (0.500); myocardial infarction (0.187); male reproductive system disorder (0.187); mathematical ability (0.187); intelligence (0.173)
- **Europe PMC papers**: 321
- **Why important**: XPO6 connects ARHGAP19, SECISBP2 and ZCCHC9 and is one of the module members represented in hu.MAP complex (hu.MAP huMAP3_11232.1). Its established function is Ran-regulated nuclear export of profilin-actin complexes and intracellular protein transport. HPA identifies it as enriched in neutrophils and in immune cells, while the module-level GO and STRING evidence places it in a predominantly nuclear context. Its disease-resource associations include neurodegenerative disease, myocardial infarction and male reproductive-system disorders, although the literature is smaller than for the principal hub genes.
- **Conclusion**: Established evidence supports XPO6 as a nuclear-cargo and actin-transport regulator that could connect nuclear biology to cell morphology or immune-cell state. Its role as a mechanistic bridge within this module remains a hypothesis because direct STRING interactions with the other module genes were not supplied.

## Module 3

**Tissue pair**: cell line and circulatory_system  
**Genes (25)**: AFTPH, DNA2, ERICH1, ESCO2, FERRY3, GIPC3, GNL1, GOPC, GPSM1, MAP4K5, MAGEC2, MAP1A, NSFL1C, PKN1, CDC40, RNH1, POLR2G, RUBCN, RXRA, SIK3, SMG8, TNIP1, USP1, ZMYM1, ZPR1

### Function

No single biological function can be assigned with confidence. No GO/KEGG term passed global multiple-testing correction, and there were no supplementary STRING enrichment terms. The annotations instead span DNA replication and repair, sister-chromatid cohesion, RNA polymerase activity, mRNA surveillance and splicing, cytoskeletal organization, vesicle trafficking, kinase signaling, autophagy, and immune regulation. The module is therefore best described as a heterogeneous intracellular regulatory module rather than a validated pathway. The co-abundance structure may capture coordinated cellular state, shared expression context, or sample-composition effects, but the current evidence does not establish one unified mechanism.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes, and the proteins are predominantly intracellular or nuclear. Most genes have low tissue specificity, while many show cell-type-enhanced expression across diverse cell types, including neutrophils, platelets, oligodendrocytes, spermatogenic cells, and progenitor populations. Blood-cell associations are scattered rather than forming a dominant immune signature, with mostly low immune-cell specificity and only a minority showing immune enrichment or enhancement. The module therefore does not resemble a coherent circulating plasma-protein program. Its presence in the circulatory_system comparison could reflect shared cellular populations, especially blood or progenitor-related cells, rather than a secreted blood-borne function. The broad mixture of testis, brain, lymphoid, marrow, intestinal, retinal, and other cell-type associations also argues against a simple tissue-specific interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module gene pair met the supplied high-confidence STRING interaction threshold, and no STRING functional-enrichment terms were reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not supported here as established physical protein interactions or membership in a known multiprotein complex. This does not invalidate the co-abundance module, but it indicates that its network structure is presently an expression-level association rather than a protein-interaction network. Some genes have well-established molecular functions individually, such as DNA2 in genome maintenance, ESCO2 in sister-chromatid cohesion, USP1 in deubiquitination and DNA repair, MAP1A in microtubule biology, TNIP1 in inflammatory signaling, and RXRA in transcriptional regulation; those annotations should not be interpreted as evidence that all module members operate in one complex.

**STRING interactions (score >= 0.7)**: 0 of 300 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported co-abundance pattern, because neither STRING nor hu.MAP provides an established interaction or complex explanation for it. However, absence from those resources alone does not demonstrate biological novelty, and the lack of globally significant GO/KEGG or STRING enrichment makes a new pathway claim especially premature. A defensible conclusion is that the cross-tissue co-abundance pattern is potentially novel as a data-derived association, while its biological reproducibility, independence from cell composition, and mechanistic basis remain unproven. Replication in independent cohorts, adjustment for cell-type composition, and validation at the protein or perturbation level would be needed before calling it a new biological module.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular cell-state program involving genome maintenance, RNA handling, cytoskeletal or trafficking processes, and signaling regulation in a mixture of broadly expressing and cell-type-enhanced populations. ESCO2, DNA2, and USP1 could represent a genome-integrity component; MAP1A and related trafficking or cytoskeletal genes could represent structural or transport context; and TNIP1 or RXRA could connect the state to immune or transcriptional regulation. This is a mechanistic model, not an established conclusion: the lack of globally significant enrichment, STRING interactions, and hu.MAP complexes means that direct functional coupling has not been demonstrated.

### Important genes

#### ESCO2

- **Related proteins** (co-abundance neighbors): MAP1A (0.88), USP1 (0.85), ZMYM1 (0.81), RXRA (0.80), SMG8 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: establishment of sister chromatid cohesion N-acetyltransferase 2. This gene encodes a protein that may have acetyltransferase activity and may be required for the establishment of sister chromatid cohesion during the S phase of mitosis. Mutations in this gene have been associated with Roberts syndrome. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: Roberts-SC phocomelia syndrome (0.825); Juberg-Hayward syndrome (0.706); hereditary disease (0.487); Absent radius (0.462); hypercholesterolemia, familial, 1 (0.333)
- **Europe PMC papers**: 1280
- **Why important**: ESCO2 is among the more connected genes in the module and links to MAP1A, USP1, ZMYM1, RXRA, and SMG8. Its established function in sister-chromatid cohesion, DNA replication regulation, and protein acetylation provides one of the clearest mechanistic anchors in an otherwise heterogeneous module. Its HPA pattern includes marrow, lymphoid tissue, testis, erythrocyte progenitors, and megakaryocyte progenitors, which is relevant to the cell-line and circulatory_system comparison. Its association with Roberts syndrome adds strong disease relevance, and its literature base is substantial.
- **Conclusion**: Established evidence supports ESCO2 as a genome-maintenance and cohesion gene with expression in several progenitor-related populations. Its network position makes it a plausible module anchor, but there is no evidence here that the other module genes form an ESCO2-centered complex. The proposed role of ESCO2 as part of a shared cell-state program remains a hypothesis.

#### DNA2

- **Related proteins** (co-abundance neighbors): SMG8 (0.90), POLR2G (0.87), GOPC (0.83), CDC40 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA replication helicase/nuclease 2. This gene encodes a member of the DNA2/NAM7 helicase family. The encoded protein is a conserved helicase/nuclease involved in the maintenance of mitochondrial and nuclear DNA stability. Mutations in this gene are associated with autosomal dominant progressive external ophthalmoplegia-6 (PEOA6) and Seckel syndrome 8. Alternatively spliced transcript variants have been found for this gene. [provided…
- **Diseases (Open Targets)**: mitochondrial DNA deletion syndrome with progressive myopathy (0.799); Seckel syndrome 8 (0.668); Rothmund-Thomson syndrome type 4 (0.599); Seckel syndrome (0.556); cancer (0.550)
- **Europe PMC papers**: 3923
- **Why important**: DNA2 is a central connector in the module and links to SMG8, POLR2G, GOPC, and CDC40. It has established helicase and nuclease functions in nuclear and mitochondrial DNA stability, replication, repair, telomere maintenance, and double-strand-break processing. Its expression is enhanced in lymphoid tissue and in several hematopoietic progenitor populations, including erythrocyte, megakaryocyte, monocyte, and neutrophil progenitors. Its associations with progressive external ophthalmoplegia and Seckel syndrome, together with a large literature base, make it a biologically informative representative.
- **Conclusion**: Established evidence supports DNA2 as a genome-stability factor and shows relevant progenitor-associated expression. It could contribute to a proliferative or stress-related cellular state in the shared module, but the module data do not establish that DNA2-driven genome maintenance is the principal function.

#### MAP1A

- **Related proteins** (co-abundance neighbors): ESCO2 (0.88), MAGEC2 (0.87), TNIP1 (0.82), GPSM1 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: microtubule associated protein 1A. This gene encodes a protein that belongs to the microtubule-associated protein family. The proteins of this family are thought to be involved in microtubule assembly, which is an essential step in neurogenesis. The product of this gene is a precursor polypeptide that presumably undergoes proteolytic processing to generate the final MAP1A heavy chain and LC2 light chain. Expression of this gene is …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.340); venous thromboembolism (0.238); hereditary disease (0.118); autism spectrum disorder (0.094); urinary bladder cancer (0.075)
- **Europe PMC papers**: 1240
- **Why important**: MAP1A has a prominent network position and connects ESCO2, MAGEC2, TNIP1, and GPSM1. It is an established microtubule-associated protein involved in microtubule organization, axonogenesis, dendrite development, and neuronal structural processes. HPA identifies brain tissue enrichment and enhancement in oligodendrocytes, while also noting a plasmacytoid dendritic-cell association. Its disease associations include neurodevelopmental disorder and autism spectrum disorder, and it has a substantial literature base. It therefore provides a strong structural and cell-type-specific contrast to the genome-maintenance genes.
- **Conclusion**: Established evidence supports MAP1A as a neuronal and microtubule-related gene. Its inclusion may indicate cytoskeletal or cell-identity context in the co-abundance pattern, but it does not demonstrate a direct functional bridge to DNA2 or ESCO2. Any interpretation connecting MAP1A to a shared module mechanism is provisional.

#### MAGEC2

- **Related proteins** (co-abundance neighbors): PKN1 (0.88), MAP1A (0.87), ZPR1 (0.87), GNL1 (0.85), NSFL1C (0.82), RNH1 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MAGE family member C2. This gene is a member of the MAGEC gene family. It is not expressed in normal tissues, except for testis, and is expressed in tumors of various histological types. This gene and the other MAGEC genes are clustered on chromosome Xq26-q27. [provided by RefSeq, Oct 2009].
- **Diseases (Open Targets)**: anti-neutrophil antibody associated vasculitis (0.257); neoplasm (0.112); non-small cell lung carcinoma (0.093); hepatocellular carcinoma (0.093); melanoma (0.089)
- **Europe PMC papers**: 391
- **Why important**: MAGEC2 has the strongest network connectivity in the supplied subgraph and links to PKN1, MAP1A, ZPR1, GNL1, NSFL1C, and RNH1. It is a cancer-testis MAGE-family gene with highly restricted normal-tissue expression centered on testis and expression reported in tumors. HPA places it in differentiating and undifferentiated spermatogenic populations, and its disease associations include neoplasia and several tumor types. Its network prominence makes it important for interpreting the module even though its functional annotation is less directly connected to the other genes and its literature base is smaller than that of the major genome-maintenance genes.
- **Conclusion**: Established evidence supports MAGEC2 as a testis-restricted and cancer-associated MAGE-family member. Its network prominence may reflect a testis or tumor-related expression context rather than a conserved intracellular pathway. A direct mechanistic role for MAGEC2 in this cross-tissue module is not established.

#### TNIP1

- **Related proteins** (co-abundance neighbors): MAP1A (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TNFAIP3 interacting protein 1. This gene encodes an A20-binding protein which plays a role in autoimmunity and tissue homeostasis through the regulation of nuclear factor kappa-B activation. Mutations in this gene have been associated with psoriatic arthritis, rheumatoid arthritis, and systemic lupus erythematosus. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2…
- **Diseases (Open Targets)**: systemic lupus erythematosus (0.514); psoriasis (0.469); amyotrophic lateral sclerosis (0.458); systemic sclerosis (0.440); skin disorder (0.416)
- **Europe PMC papers**: 1698
- **Why important**: TNIP1 connects to MAP1A and has an established role in regulation of NF-kappa-B-related inflammatory signaling, tissue homeostasis, leukocyte adhesion, and defense responses. HPA shows enhancement in enterocytes, esophageal apical cells, and neutrophils. Its disease associations include systemic lupus erythematosus, psoriasis, systemic sclerosis, and other inflammatory conditions, and it has a substantial literature base. TNIP1 is therefore important because it supplies an immune-regulatory interpretation that could be relevant to circulatory-system samples without implying that the entire module is an immune module.
- **Conclusion**: Established evidence supports TNIP1 as an inflammatory and homeostatic regulator with relevant neutrophil-associated expression. It may mark immune or epithelial cellular context within the module, but the sparse network connection and absence of enrichment do not support TNIP1 as the central driver.

#### RXRA

- **Related proteins** (co-abundance neighbors): ESCO2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: retinoid X receptor alpha. Retinoid X receptors (RXRs) and retinoic acid receptors (RARs) are nuclear receptors that mediate the biological effects of retinoids by their involvement in retinoic acid-mediated gene activation. These receptors function as transcription factors by binding as homodimers or heterodimers to specific sequences in the promoters of target genes. The protein encoded by this gene is a member of the ste…
- **Diseases (Open Targets)**: psoriasis (0.583); primary cutaneous T-cell non-Hodgkin lymphoma (0.551); psoriasis vulgaris (0.517); urinary bladder cancer (0.507); neoplasm (0.480)
- **Europe PMC papers**: 5301
- **Why important**: RXRA is connected to ESCO2 and is an established nuclear receptor transcription factor that forms receptor partnerships and regulates retinoid-, thyroid-hormone-, and other hormone-responsive transcriptional programs. HPA shows enhancement in hepatocytes, Kupffer cells, monocytes, and neutrophils, as well as esophageal apical cells. Its disease associations include psoriasis, cutaneous lymphoma, and neoplasia, and it has a large literature base. RXRA is important as a plausible transcriptional-state regulator linking the module to differentiated and immune-associated cell contexts.
- **Conclusion**: Established evidence supports RXRA as a transcriptional regulator with broad physiological relevance and immune-associated expression. Its connection to ESCO2 suggests a possible regulatory-state relationship at the co-abundance level, but no direct interaction or shared complex is reported, so a causal role in the module remains hypothetical.

## Module 4

**Tissue pair**: cell line and circulatory_system  
**Genes (35)**: AGAP2, PRMT3, AP4B1, BAG3, CENATAC, TTC4, MT-CYB, DIAPH2, DLGAP5, DUSP12, ERCC6L, BRIP1, FLNB, TUBGCP5, GRWD1, HAUS6, KIF18B, KIF11, KIF3A, LUZP1, MAGED1, MYO7B, OGFOD2, TENT4B, PPP3CB, GINS2, ARHGAP17, RPL26L1, SBNO1, SMYD3, TTK, USP10, USP8, WDCP, WDR62

### Function

The primary interpretation is a microtubule- and spindle-centered cytoskeleton module. The globally corrected enrichment for cytoskeleton organization (GO:BP cytoskeleton organization; q_global = 0.00768), spindle (GO:CC spindle; q_global = 0.0177), and microtubule binding (GO:MF microtubule binding; q_global = 0.0436) supports coordinated regulation of microtubule architecture, centrosomes, spindle assembly, chromosome movement, and cell division. The strongest functional coherence is concentrated in DLGAP5, HAUS6, KIF11, KIF18B, KIF3A, LUZP1, TTK, TUBGCP5, and WDR62. Other module genes connect to actin organization, vesicle trafficking, DNA replication or repair, RNA processing, and protein quality control, suggesting that the module also captures broader properties of proliferating or structurally active cells. The enrichment is not evidence that every gene has a direct mitotic role.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, while nearly all show enhanced specificity for particular cell types. The recurrent HPA signals in bone marrow, lymphoid tissue, erythrocyte progenitors, neutrophil progenitors, monocyte progenitors, megakaryocyte progenitors, and spermatogenic cells are consistent with proliferative or progenitor-cell biology. The blood-cell specificity is mixed rather than uniformly immune, with many genes having low immune-cell specificity and a smaller subset enhanced or enriched in immune cells. Therefore, in circulatory_system samples, the module may partly reflect the abundance of circulating or blood-forming cell populations; in cell line samples, it may reflect shared proliferative state. The HPA protein-detection fields for the two specified sample groups provide no additional tissue-matched protein confirmation.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP cytoskeleton organization | 0.00768 | AGAP2, ARHGAP17, CENATAC, DIAPH2, DLGAP5, FLNB, HAUS6, KIF11, KIF18B, KIF3A, LUZP1, MYO7B, TTK, TUBGCP5, WDR62 |
| GO:CC spindle | 0.0177 | DLGAP5, HAUS6, KIF11, KIF18B, KIF3A, LUZP1, TTK, TUBGCP5, WDR62 |
| GO:MF microtubule binding | 0.0436 | DLGAP5, HAUS6, KIF11, KIF18B, KIF3A, LUZP1, TUBGCP5 |

### STRING and hu.MAP

STRING contains a coherent, high-confidence mitotic subnetwork involving DLGAP5, KIF11, KIF18B, TTK, KIF3A, GINS2, and ERCC6L. In particular, the links among DLGAP5, KIF11, KIF18B, and TTK independently support the spindle and chromosome-segregation interpretation. The STRING links are supplementary and do not constitute a globally corrected enrichment result; STRING reports no functional enrichment for this query. The co-abundance graph also places MYO7B as a major connectivity hub, but its direct STRING partners are absent from the supplied evidence. No hu.MAP complex contains at least two module members, so the module is not explained by a detected shared hu.MAP complex. Overall, known physical or functional relationships validate a central mitotic core, while much of the co-abundance structure remains unexplained by the supplied interaction resources.

**STRING interactions (score >= 0.7)**: 8 of 595 gene pairs: DLGAP5–GINS2 (0.72); DLGAP5–KIF11 (0.997); DLGAP5–KIF18B (0.818); DLGAP5–TTK (0.977); ERCC6L–TTK (0.805); KIF11–KIF18B (0.871); KIF11–KIF3A (0.776); KIF11–TTK (0.984)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be called a wholly new biological pathway: its central spindle biology is established by the globally corrected GO terms (GO:BP cytoskeleton organization; q_global = 0.00768), (GO:CC spindle; q_global = 0.0177), and (GO:MF microtubule binding; q_global = 0.0436), by the known STRING relationships, and by the documented functions of TTK, KIF11, DLGAP5, KIF18B, KIF3A, HAUS6, and TUBGCP5. It may nevertheless represent a potentially novel cross-context co-abundance pattern linking cell line and circulatory_system samples, especially because no hu.MAP complex was detected and STRING explains only a minority of the module relationships. Absence from STRING or hu.MAP is not proof of novelty. A claim of a new finding would require replication in independent datasets, assessment of cell-composition and proliferation confounding, and preferably experimental or perturbational validation.

**Hypothesis.** Hypothesis: the conserved module reflects a shared proliferative-cell program in which centrosome and microtubule organization, spindle assembly, chromosome segregation, and actin or membrane organization are coordinated. In cell lines this may represent the mitotic state of the culture; in circulatory_system samples it may arise from the relative abundance of dividing blood or hematopoietic progenitor populations. MYO7B may act as a co-abundance hub connecting cytoskeletal, membrane-trafficking, and mitotic signals, but this proposed bridging role is not established by the supplied physical-interaction evidence. The hypothesis predicts that module activity will track proliferation and progenitor-cell abundance and will diminish after adjustment for cellular composition.

### Important genes

#### MYO7B

- **Related proteins** (co-abundance neighbors): HAUS6 (0.92), ERCC6L (0.91), KIF11 (0.88), TTK (0.88), ARHGAP17 (0.87), PPP3CB (0.87), USP8 (0.86), FLNB (0.86), SBNO1 (0.86), USP10 (0.85), KIF18B (0.84), DUSP12 (0.83), DLGAP5 (0.83), PRMT3 (0.83), DIAPH2 (0.82), GRWD1 (0.81), SMYD3 (0.81), GINS2 (0.81), BAG3 (0.81), TTC4 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin VIIB. The protein encoded by this gene is found in brush border microvilli of epithelial cells in the intestines and kidneys. The encoded protein is involved in linking protocadherins to the actin cytoskeleton and is essential for proper microvilli function. This protein aids in the accumulation of intermicrovillar adhesion components such as harmonin and ANKS4B, and this accumulation is necessary for n…
- **Diseases (Open Targets)**: deep vein thrombosis (0.367); clear cell renal carcinoma (0.358); venous thromboembolism (0.333); Thromboembolism (0.332); neurodegenerative disease (0.302)
- **Europe PMC papers**: 284
- **Why important**: MYO7B is the principal network hub by weighted connectivity in the supplied module and connects genes involved in cytoskeleton, signaling, trafficking, and cellular organization. Its established function is myosin VIIB-mediated linkage of protocadherins to the actin cytoskeleton and maintenance of epithelial brush border microvilli. HPA supports intestine and epithelial-cell associations, while the disease-resource evidence includes thromboembolic and renal-cancer associations. Its literature volume is moderate. It is important because it may organize the cross-functional co-abundance structure even though it is not in the primary spindle terms (GO:BP cytoskeleton organization; q_global = 0.00768) and has no supplied STRING partner.
- **Conclusion**: Established: MYO7B is a highly connected module gene with actin-linked epithelial and trafficking functions. Hypothesis: its hub position may mark a cytoskeletal integration point rather than a direct spindle component. The thromboembolic association is relevant to circulatory-system interpretation but does not establish a causal role in this module.

#### TTK

- **Related proteins** (co-abundance neighbors): MYO7B (0.88), AGAP2 (0.80); STRING partners: DLGAP5 (0.977), ERCC6L (0.805), KIF11 (0.984)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TTK protein kinase. This gene encodes a dual specificity protein kinase with the ability to phosphorylate tyrosine, serine and threonine. Associated with cell proliferation, this protein is essential for chromosome alignment at the centromere during mitosis and is required for centrosome duplication. It has been found to be a critical mitotic checkpoint protein for accurate segregation of chromosomes during mitosis. …
- **Diseases (Open Targets)**: neurodegenerative disease (0.551); Alzheimer disease (0.380); Parkinson disease (0.375); lysosomal storage disease (0.375); ulna fracture (0.300)
- **Europe PMC papers**: 4437
- **Why important**: TTK is a mitotic checkpoint kinase required for chromosome alignment, centrosome duplication, spindle organization, and accurate chromosome segregation. It appears in cytoskeleton organization (GO:BP cytoskeleton organization; q_global = 0.00768) and spindle (GO:CC spindle; q_global = 0.0177), and has strong STRING relationships with DLGAP5, KIF11, and ERCC6L. HPA places it in bone marrow, lymphoid tissue, and testis, including erythrocyte and megakaryocyte progenitor states. It has a large literature base and broad disease-resource associations, although those associations do not by themselves define this module.
- **Conclusion**: Established: TTK is a strong mechanistic marker of the module's mitotic checkpoint and spindle component. Hypothesis: TTK-linked co-abundance may be especially sensitive to the fraction of actively cycling progenitor cells in circulatory_system samples.

#### KIF11

- **Related proteins** (co-abundance neighbors): MYO7B (0.88); STRING partners: DLGAP5 (0.997), KIF18B (0.871), KIF3A (0.776), TTK (0.984)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Mid piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 11. This gene encodes a motor protein that belongs to the kinesin-like protein family. Members of this protein family are known to be involved in various kinds of spindle dynamics. The function of this gene product includes chromosome positioning, centrosome separation and establishing a bipolar spindle during cell mitosis. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: microcephaly with or without chorioretinopathy, lymphedema, or intellectual disability (0.821); hereditary disease (0.509); inherited retinal dystrophy (0.507); neurodegenerative disease (0.484); microcephaly (0.412)
- **Europe PMC papers**: 3618
- **Why important**: KIF11 is a spindle motor that supports centrosome separation, bipolar spindle formation, chromosome positioning, and spindle dynamics. It is present in all three primary enrichment terms (GO:BP cytoskeleton organization; q_global = 0.00768), (GO:CC spindle; q_global = 0.0177), and (GO:MF microtubule binding; q_global = 0.0436), and forms a particularly well-supported STRING neighborhood with DLGAP5, KIF18B, KIF3A, and TTK. HPA associates it with bone marrow, lymphoid tissue, and several dividing progenitor populations. It has substantial literature and disease associations including microcephaly-related disorders and inherited retinal disease.
- **Conclusion**: Established: KIF11 is a central functional representative of the spindle and microtubule-binding core. Hypothesis: variation in KIF11-associated activity could provide a practical proxy for the proliferative component of this cross-tissue module.

#### DLGAP5

- **Related proteins** (co-abundance neighbors): MYO7B (0.83); STRING partners: GINS2 (0.72), KIF11 (0.997), KIF18B (0.818), TTK (0.977)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DLG associated protein 5. Predicted to enable microtubule binding activity. Predicted to be involved in several processes, including centrosome localization; kinetochore assembly; and mitotic spindle organization. Located in several cellular components, including centrosome; cytosol; and mitochondrion. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.485); placenta praevia (0.228); alcohol drinking (0.223); placental retention (0.151); male infertility (0.149)
- **Europe PMC papers**: 1514
- **Why important**: DLGAP5 is annotated for microtubule binding, kinetochore assembly, spindle organization, chromosome segregation, and mitotic progression. It occurs in (GO:BP cytoskeleton organization; q_global = 0.00768), (GO:CC spindle; q_global = 0.0177), and (GO:MF microtubule binding; q_global = 0.0436) and has several of the strongest supplied STRING relationships, including links to KIF11, TTK, KIF18B, and GINS2. HPA associates it with bone marrow, lymphoid tissue, testis, and erythrocyte or megakaryocyte progenitors. It has a substantial literature base and disease-resource links including male infertility.
- **Conclusion**: Established: DLGAP5 is a well-supported spindle and chromosome-segregation component and one of the best-supported anchors of the module. Hypothesis: its co-abundance with progenitor-associated genes reflects shared cell-cycle demand rather than a tissue-specific circulatory function.

#### KIF3A

- **Related proteins** (co-abundance neighbors): CENATAC (0.84), MAGED1 (0.81); STRING partners: KIF11 (0.776)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm, Primary cilium, Basal body, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 3A. Enables protein phosphatase binding activity; small GTPase binding activity; and spectrin binding activity. Involved in protein localization to cell junction and protein transport. Located in centriole and centrosome. Part of kinesin II complex. Colocalizes with spindle microtubule. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.541); ventricular septal defect (0.289); atopic eczema (0.283); alcohol drinking (0.234); asthma (0.225)
- **Europe PMC papers**: 2473
- **Why important**: KIF3A is a kinesin-II component involved in microtubule-based movement, organelle and protein localization, centriole organization, and transport. It appears in (GO:BP cytoskeleton organization; q_global = 0.00768), (GO:CC spindle; q_global = 0.0177), and (GO:MF microtubule binding; q_global = 0.0436), connects in the module to CENATAC and MAGED1, and has a high-confidence STRING relationship with KIF11. HPA supports brain and retinal tissue associations, primary-cilium and centrosomal localization, and enhanced signals in neuronal and ciliated cell types. It has a substantial literature base and disease-resource associations including neurodegenerative disease, atopic eczema, asthma, and ventricular septal defect.
- **Conclusion**: Established: KIF3A links the module's microtubule machinery to intracellular transport, centrosomes, and cilia. Hypothesis: KIF3A may broaden the module beyond canonical mitosis by coupling spindle-related co-abundance to ciliary or cell-polarity programs in particular cell populations.

## Module 5

**Tissue pair**: cell line and circulatory_system  
**Genes (13)**: ALKBH2, ANAPC5, BRD7, CARNMT1, CRACR2A, GSPT2, FHIP2B, FBXL15, NCOA2, TTC31, UBE2N, UBN2, ZNF639

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent. The module therefore does not support a narrowly defined pathway-level function from enrichment alone. Its gene composition instead suggests a mixed intracellular regulatory module linking ubiquitin-related protein control, chromatin and transcriptional regulation, DNA repair, translation termination, calcium entry, and cellular metabolism. FBXL15 is the central co-abundance node and is annotated as an F-box protein involved in an SCF ubiquitin ligase complex, BMP signaling, and cell-cycle regulation. CRACR2A contributes a calcium-entry and immune-cell activation connection, while GSPT2 contributes translation termination. These annotations support a broad cellular maintenance or regulatory program, but not a single established biological pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: no member is annotated as secreted. Most genes have low tissue specificity and low immune-cell specificity, arguing against a strongly blood-cell-restricted or tissue-restricted module. Some cell-type-enhanced signals occur in germ-cell populations, and CRACR2A is enhanced in mucosal secretory cell types and in basophils; UBN2 is also immune-cell enriched in basophils. These signals may reflect shared cell types or sample composition, but they are not sufficient to establish that the conserved module is a blood-derived program. The absence of matching HPA protein observations for the two queried tissue contexts further limits protein-level interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was observed among the module members, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance relationships are not corroborated here as known physical protein interactions or as membership in a known multiprotein complex. The strongest co-abundance connectivity is centered on FBXL15, with a smaller bridge involving CRACR2A, GSPT2, FHIP2B, and ZNF639. This structure may represent coordinated expression, shared regulation, cell-composition effects, or indirect biology rather than direct binding. Known molecular functions remain relevant: FBXL15 is linked to SCF ubiquitin-ligase activity, ANAPC5 to the anaphase-promoting complex, UBE2N to ubiquitin conjugation and DNA repair, BRD7 to chromatin remodeling, NCOA2 to nuclear-receptor coactivation, ALKBH2 to DNA alkylation repair, and CRACR2A to store-operated calcium entry.

**STRING interactions (score >= 0.7)**: 0 of 78 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This exact conserved co-abundance module appears potentially novel in the supplied resources because it has no reported STRING interactions, no multi-member hu.MAP complex, and no globally significant GO or KEGG enrichment. However, those absences do not prove biological novelty: the module may reflect co-regulation, shared cell composition, technical structure, or interactions not captured by the queried databases. The appropriate conclusion is that this is a novel candidate co-abundance pattern requiring replication, preservation testing, cell-composition adjustment, and orthogonal molecular validation, rather than a newly established molecular complex or pathway.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of intracellular proteostasis, chromatin and transcriptional state, genome maintenance, translation, and calcium-dependent signaling in cell-line and circulatory-system samples. FBXL15 may act as the expression-network hub linking ubiquitin-dependent regulation with chromatin, DNA-repair, and transcriptional regulators, while CRACR2A may connect the regulatory program to calcium handling and mucosal or immune-associated cell states. The germ-cell and basophil-associated HPA signals could indicate that part of the pattern is driven by shared cellular composition rather than a universal pathway. This hypothesis should be tested by controlling for cell mixture, examining independent cohorts, and measuring protein abundance and perturbational responses.

### Important genes

#### FBXL15

- **Related proteins** (co-abundance neighbors): ANAPC5 (0.89), FHIP2B (0.86), BRD7 (0.83), UBE2N (0.82), NCOA2 (0.82), UBN2 (0.81), ALKBH2 (0.81), CARNMT1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: F-box and leucine rich repeat protein 15. Involved in G2/M transition of mitotic cell cycle; cellular protein metabolic process; and positive regulation of BMP signaling pathway. Located in cytoplasm. Part of SCF ubiquitin ligase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: maturity-onset diabetes of the young (0.071); deafness (0.066); hearing loss, autosomal recessive (0.066); autosomal dominant nonsyndromic hearing loss (0.065); maturity-onset diabetes of the young type 3 (0.058)
- **Europe PMC papers**: 133
- **Why important**: FBXL15 is the central node of the co-abundance subgraph and has the strongest weighted connectivity in the module. It is annotated as an F-box and leucine-rich-repeat protein involved in an SCF ubiquitin-ligase complex, protein ubiquitination, cell-cycle transition, and BMP signaling. Its central network position makes it the leading candidate for coordinating the otherwise diverse functional signals. It also has disease associations involving diabetes and hearing disorders and a substantial literature base.
- **Conclusion**: Established: FBXL15 is the network hub and has documented ubiquitin-ligase, cell-cycle, and BMP-related functions. Hypothesis: its hub position marks it as a regulator of the shared co-abundance program, but the data do not establish that it physically interacts with the other module members.

#### CRACR2A

- **Related proteins** (co-abundance neighbors): GSPT2 (0.88), ZNF639 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium release activated channel regulator 2A. Enables GTPase activity and calcium ion binding activity. Involved in several processes, including activation of store-operated calcium channel activity; positive regulation of JNK cascade; and store-operated calcium entry. Located in several cellular components, including Golgi apparatus; Weibel-Palade body; and immunological synapse. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: alcohol drinking (0.417); ovarian dysfunction (0.271); kidney disorder (0.252); Respiratory insufficiency (0.240); ulcerative colitis (0.197)
- **Europe PMC papers**: 246
- **Why important**: CRACR2A is a bridge node connecting GSPT2 and ZNF639 and is the clearest cell-state-specific functional signal in the module. It is annotated for store-operated calcium entry, calcium binding, vesicle and endosomal transport, and leukocyte activation. HPA links it to mucosal secretory cell types and basophils, while its disease associations include intestinal and respiratory disorders. Its literature support is substantial relative to most of the module.
- **Conclusion**: Established: CRACR2A participates in calcium-entry regulation and immune-related cellular processes and shows enrichment in selected mucosal and immune cell types. Hypothesis: it may connect the co-abundance module to cell-state or calcium-dependent signaling, although this could also reflect cell composition.

#### GSPT2

- **Related proteins** (co-abundance neighbors): CRACR2A (0.88), FHIP2B (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G1 to S phase transition 2. This gene encodes a GTPase that belongs to the GTP-binding elongation factor family. The encoded protein is a polypeptide release factor that complexes with eukaryotic peptide chain release factor 1 to mediate translation termination. This protein may also be involved in mRNA stability.[provided by RefSeq, Mar 2010].
- **Diseases (Open Targets)**: autism (0.334); Seizure (0.333); Delayed speech and language development (0.333); cancer (0.064); hepatocellular carcinoma (0.041)
- **Europe PMC papers**: 221
- **Why important**: GSPT2 is positioned at the small bridge between CRACR2A and FHIP2B. It encodes a translation termination factor and is annotated for translation and translational termination. HPA shows enhancement in several germ-cell populations and Müller glia. Its established role in protein synthesis provides a plausible cellular-maintenance anchor, and it has a meaningful literature base and reported neurodevelopmental and seizure-related disease associations.
- **Conclusion**: Established: GSPT2 functions in translation termination and occupies a bridging position in the co-abundance graph. Hypothesis: it may indicate coordinated translational demand or cell-state regulation within the module, but the network does not demonstrate a direct mechanistic link to CRACR2A or FHIP2B.

#### BRD7

- **Related proteins** (co-abundance neighbors): FBXL15 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: bromodomain containing 7. This gene encodes a protein which is a member of the bromodomain-containing protein family. The product of this gene has been identified as a component of one form of the SWI/SNF chromatin remodeling complex, and as a protein which interacts with p53 and is required for p53-dependent oncogene-induced senescence which prevents tumor growth. Pseudogenes have been described on chromosomes 2, 3, 6, 13…
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.515); hypothyroidism (0.438); thyroid gland disorder (0.395); neurodegenerative disease (0.338); inflammatory bowel disease (0.336)
- **Europe PMC papers**: 1493
- **Why important**: BRD7 is a peripheral neighbor of the central FBXL15 node but is functionally important because it is a chromatin-remodeling and transcriptional regulator. It is annotated as a component of a SWI/SNF chromatin-remodeling form and as a regulator of differentiation, transcription, and the mitotic cell cycle. It has extensive literature coverage and disease associations involving hepatocellular carcinoma, thyroid disorders, neurodegeneration, and inflammatory bowel disease.
- **Conclusion**: Established: BRD7 has documented chromatin-remodeling and transcriptional functions and is linked to multiple disease contexts. Hypothesis: its co-abundance with FBXL15 may reflect shared control of cellular state or transcription, but the absence of STRING and hu.MAP support prevents claiming a known complex relationship.

#### UBE2N

- **Related proteins** (co-abundance neighbors): FBXL15 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin conjugating enzyme E2 N. The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. Studies …
- **Diseases (Open Targets)**: ovarian cancer (0.097); ovarian carcinoma (0.097); neoplasm (0.096); Alzheimer disease (0.095); lung adenocarcinoma (0.095)
- **Europe PMC papers**: 2131
- **Why important**: UBE2N is directly connected to FBXL15 and supplies a second ubiquitin-related functional anchor. It is annotated for ubiquitin conjugation, DNA damage tolerance, DNA repair, and homologous recombination-related processes. HPA identifies enhancement in late spermatids, and the gene has extensive literature coverage with associations spanning cancer and neurodegenerative disease.
- **Conclusion**: Established: UBE2N participates in ubiquitin-dependent regulation and DNA-damage responses. Hypothesis: its co-abundance with FBXL15 may represent coordinated proteostasis or genome-maintenance activity, but direct cooperation within this module is not demonstrated.

## Module 6

**Tissue pair**: cell line and circulatory_system  
**Genes (5)**: ANXA3, CYTH2, ZFPM1, SAMD9L, WDR44

### Function

The module has no GO or KEGG term passing global correction, so its function cannot be assigned from enrichment evidence. Its network structure is a star centered on CYTH2, with SAMD9L, ZFPM1, WDR44, and ANXA3 connected to it. The individual annotations point to membrane-associated signaling, endocytosis and vesicle trafficking, innate immune and myeloid biology, erythroid and megakaryocyte differentiation, and neutrophil-associated functions. These convergent annotations support a cautious interpretation as a cell-state or regulatory module linking membrane trafficking with hematopoietic and immune-related biology, rather than a demonstrated pathway.

**Cell composition.** The genes are not secreted proteins and are not uniformly blood-cell restricted. HPA indicates that most have enhanced specificity in particular cell types, including megakaryocytes, neutrophil progenitors, microglia, erythrocyte progenitors, and esophageal apical cells. Tissue-enhanced signals include lymphoid tissue for SAMD9L and bone marrow for ANXA3. ANXA3 is immune-cell enriched in neutrophils, whereas ZFPM1 is not detected in immune cells and is associated with erythroid and megakaryocyte progenitors. CYTH2, WDR44, and SAMD9L have low immune-cell specificity or broad tissue patterns. Thus, the shared module may partly reflect shared hematopoietic or other cell-type composition in the samples, but it is not simply a plasma-protein module or a uniformly blood-cell-specific signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair reaches the stated STRING interaction threshold, and there is no supplementary STRING functional enrichment. No hu.MAP complex contains multiple module members. Therefore, the observed co-abundance relationships are not supported here by high-confidence known physical or functional interactions or by a shared annotated complex. The star-like topology around CYTH2 is consequently a co-abundance pattern rather than evidence of a validated molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel co-abundance association because the module brings together genes with related but distinct annotations and has no detected high-confidence STRING interactions or shared hu.MAP complex. However, absence from STRING or hu.MAP does not establish biological novelty. The lack of globally significant GO or KEGG enrichment also prevents claiming a newly discovered pathway. The strongest defensible claim is that this particular cross-tissue co-abundance configuration is not explained by the provided interaction or complex databases and merits experimental and replication-based validation.

**Hypothesis.** Hypothesis: a shared cellular-state program may coordinate CYTH2-dependent ARF signaling and membrane trafficking with WDR44-linked endosome recycling, while co-varying with ANXA3 membrane and neutrophil functions, SAMD9L innate-immune or myeloid responses, and ZFPM1-dependent erythroid or megakaryocyte transcriptional regulation. In cell line and circulatory-system samples, this could arise from a common hematopoietic-related state or from variation in the abundance of related cell populations. This is a mechanistic hypothesis, not an established physical interaction model.

### Important genes

#### CYTH2

- **Related proteins** (co-abundance neighbors): SAMD9L (0.88), ZFPM1 (0.82), WDR44 (0.82), ANXA3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytohesin 2. The protein encoded by this gene is a member of the PSCD family. Members of this family have identical structural organization that consists of an N-terminal coiled-coil motif, a central Sec7 domain, and a C-terminal pleckstrin homology (PH) domain. The coiled-coil motif is involved in homodimerization, the Sec7 domain contains guanine-nucleotide exchange protein (GEP) activity, and the PH domain …
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); IgA glomerulonephritis (0.320); brain compression (0.107); edema (0.107); colorectal cancer (0.073)
- **Europe PMC papers**: 190
- **Why important**: CYTH2 is the central hub of the module, connected to every other member in the observed subgraph. Its Sec seven domain provides guanine-nucleotide exchange activity, its pleckstrin-homology domain supports membrane association, and its annotations include endocytosis, vesicle-mediated transport, actin organization, and ARF signaling. It also has substantial literature coverage and disease associations including neurodegenerative disease and IgA glomerulonephritis.
- **Conclusion**: Established evidence supports CYTH2 as the principal network anchor and as a regulator of membrane-associated ARF signaling and trafficking. It is a plausible organizing gene for the module, but the data do not establish that it regulates the other module members or causes their co-abundance.

#### SAMD9L

- **Related proteins** (co-abundance neighbors): CYTH2 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sterile alpha motif domain containing 9 like. This gene encodes a cytoplasmic protein that acts as a tumor suppressor but also plays a key role in cell proliferation and the innate immune response to viral infection. The encoded protein contains an N-terminal sterile alpha motif domain. Naturally occurring mutations in this gene are associated with myeloid disorders such as juvenile myelomonocytic leukemia, acute myeloid leukemia, and myelody…
- **Diseases (Open Targets)**: ataxia-pancytopenia syndrome (0.793); monosomy 7 myelodysplasia and leukemia syndrome 1 (0.690); spinocerebellar ataxia 49 (0.624); Bone marrow hypocellularity (0.464); acute myeloid leukemia with minimal differentiation (0.462)
- **Europe PMC papers**: 1155
- **Why important**: SAMD9L links to the central CYTH2 hub and has tissue enhancement in lymphoid tissue, with cell-type enhancement in microglia, neutrophil progenitors, and NK cells. It is annotated as a cytoplasmic tumor suppressor involved in cell proliferation and innate antiviral responses, and naturally occurring mutations are associated with myeloid disorders and ataxia-pancytopenia-related disease. Its literature coverage is extensive.
- **Conclusion**: Established evidence supports SAMD9L as a regulator relevant to innate immunity, myeloid biology, and hematologic disease. Its co-abundance with CYTH2 may reflect a shared cellular state, but a direct SAMD9L–CYTH2 mechanism is unproven.

#### ZFPM1

- **Related proteins** (co-abundance neighbors): CYTH2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger protein, FOG family member 1. Enables RNA polymerase II-specific DNA-binding transcription factor binding activity and transcription corepressor activity. Involved in platelet formation; regulation of definitive erythrocyte differentiation; and regulation of gene expression. Part of transcription repressor complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.524); hypothyroidism (0.411); nephrolithiasis (0.408); aortic stenosis (0.392); Thromboembolism (0.383)
- **Europe PMC papers**: 799
- **Why important**: ZFPM1 is a peripheral module member connected to CYTH2 and is specifically associated with erythrocyte progenitors, megakaryocyte progenitors, megakaryocyte-erythroid progenitors, and megakaryocytes. It encodes a transcriptional coregulator involved in erythroid differentiation, platelet formation, cytokine regulation, and leukocyte differentiation. It has substantial literature coverage and disease associations including thromboembolism and aortic stenosis.
- **Conclusion**: Established evidence supports ZFPM1 as a hematopoietic transcriptional regulator, especially in erythroid and megakaryocyte lineages. Its presence strengthens a blood-cell-state interpretation, while its connection to CYTH2 remains a co-abundance observation rather than a demonstrated regulatory interaction.

#### ANXA3

- **Related proteins** (co-abundance neighbors): CYTH2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A3. This gene encodes a member of the annexin family.  Members of this calcium-dependent phospholipid-binding protein family play a role in the regulation of cellular growth and in signal transduction pathways.  This protein functions in the inhibition of phopholipase A2 and cleavage of inositol 1,2-cyclic phosphate to form inositol 1-phosphate. This protein may also play a role in anti-coagulation. […
- **Diseases (Open Targets)**: rheumatoid arthritis (0.318); Meniere disease (0.276); insomnia (0.255); hair color (0.209); refractive error (0.176)
- **Europe PMC papers**: 2243
- **Why important**: ANXA3 is connected to CYTH2 and has tissue enhancement in bone marrow, cell-type enhancement in megakaryocytes and other epithelial or placental cell types, and immune-cell enrichment in neutrophils. Its established functions include calcium-dependent phospholipid binding, phospholipase A2 inhibition, phagocytosis, neutrophil degranulation, antibacterial defense, endothelial migration, and angiogenesis. It has the broadest literature representation among the module genes and multiple disease associations.
- **Conclusion**: Established evidence supports ANXA3 as a membrane-associated and neutrophil-relevant effector with links to inflammation and vascular biology. It is a strong marker candidate for hematopoietic or myeloid sample composition, but the module does not show that ANXA3 physically interacts with CYTH2.

#### WDR44

- **Related proteins** (co-abundance neighbors): CYTH2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 44. This gene encodes a protein that interacts with the small GTPase rab11. A similar protein in rat binds the GTP-containing active form of rab11. This protein may play a role in endosome recycling. Alternate splicing results in multiple transcript variants.[provided by RefSeq, May 2010].
- **Diseases (Open Targets)**: ciliopathy (0.551); neurodegenerative disease (0.503); Parkinson disease (0.021); infection (0.008); developmental disability (0.004)
- **Europe PMC papers**: 177
- **Why important**: WDR44 is connected to CYTH2 and is localized to the Golgi apparatus. Its annotation indicates interaction with the small GTPase RAB11 and a possible role in endosome recycling, with additional links to cilium assembly. It has a smaller literature base than the other selected genes but provides an important trafficking-related complement to the CYTH2 annotation and has disease associations involving ciliopathy and neurodegeneration.
- **Conclusion**: Established evidence supports WDR44 as a candidate component of intracellular recycling and trafficking biology. Its co-abundance with CYTH2 is consistent with a shared trafficking state, but the provided data do not demonstrate a direct interaction or establish its role in the hematopoietic signals.

## Module 7

**Tissue pair**: cell line and circulatory_system  
**Genes (36)**: ARHGEF3, ATP7B, CCL5, CDO1, CHKB, CHPF2, DICER1, HLA-DRB4, FRMD8, GALE, HAUS2, EIF4E3, KIFAP3, LAS1L, LRRC32, MOCS3, MTMR14, NADK, NOL10, OCRL, PAXBP1, PHF8, PNPLA8, PLXNB3, RINT1, MRPS12, MRPS21, ST3GAL1, SYTL4, TDRD7, TGFBR3, TTC7A, UBXN2B, FYTTD1, ATP6V1D, ZNF316

### Function

The module does not have a statistically supported GO or KEGG functional assignment: no GO/KEGG term passed global correction. Its structure instead suggests a mixed cellular program rather than a single coherent pathway. The strongest network position is occupied by LRRC32, which connects many otherwise weakly connected genes and is annotated as a regulator of transforming growth factor beta signaling. A smaller immune-related branch contains HLA-DRB4, CCL5, TGFBR3, ST3GAL1, FRMD8, ARHGEF3, and CHKB. Other branches involve mitochondrial translation, RNA processing, glycosylation, membrane trafficking, phosphoinositide metabolism, and cell structure. These annotations support a tentative interpretation involving immune-cell state, membrane and extracellular signaling, and general intracellular maintenance, but the lack of globally significant enrichment means this interpretation remains exploratory rather than an established module-level function.

**Cell composition.** The module is not dominated by secreted or plasma proteins: only CCL5 and TGFBR3 are annotated as secreted to blood, while the remaining annotated proteins are intracellular or membrane-associated. HPA indicates broadly distributed expression for many genes, with a substantial low-tissue-specificity component. Nevertheless, immune and blood-cell signals are present, especially neutrophil-associated genes and genes enhanced in T cells, NK cells, monocytes, or other blood-cell populations. CCL5 is enhanced in bone marrow and lymphoid tissue and in T-cell and NK-cell populations, while LRRC32 is enhanced in regulatory T cells. The occurrence of neutrophil-associated genes, together with the circulatory-system context, raises the possibility that the shared module partly reflects blood-cell composition or shared immune-cell types rather than a universal program of all cells. Tissue-enhanced signals in intestine, bone marrow, lymphoid tissue, liver, and other specialized tissues also indicate that the module is compositionally heterogeneous. HPA protein detection is unavailable for both sampled tissue groups, so protein-level confirmation in those groups is not possible.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a small amount of high-confidence support. MRPS12 is strongly connected to MRPS21 and also connected to NOL10, establishing a known relationship among mitochondrial ribosome and nucleolar RNA-processing components. No STRING functional-enrichment result was reported. hu.MAP identifies MRPS12 and MRPS21 together in two complexes, but each complex contains many additional proteins and only a small subset of its members occurs in this module. Thus, the mitochondrial-ribosome relationships are consistent with known complexes, but they explain only a limited branch of the co-abundance network. The absence of STRING or hu.MAP support for most other edges means that many module connections are co-abundance associations rather than established physical interactions. In particular, the prominent LRRC32-centered network and links involving CCL5, HLA-DRB4, ST3GAL1, and TGFBR3 are not independently validated here as physical molecular interactions.

**STRING interactions (score >= 0.7)**: 2 of 630 gene pairs: MRPS12–MRPS21 (0.992); MRPS12–NOL10 (0.761)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05954.1 (MRPS12, MRPS21; 2/28); huMAP3_05807.1 (MRPS12, MRPS21; 2/81)

### Novelty

This module should not be claimed as a newly discovered molecular complex or pathway. Its lack of globally significant GO/KEGG enrichment, sparse STRING support, and limited overlap with hu.MAP complexes argue against that conclusion. It may nevertheless represent a novel tissue-pair-specific co-abundance pattern, especially because the network joins an LRRC32-centered regulatory branch, immune and blood-cell markers, mitochondrial-ribosome genes, and several trafficking or metabolic genes. Novelty would require independent replication, control for cell composition, comparison with published co-expression modules, and validation in additional cell-line and circulatory-system datasets. Absence from STRING or hu.MAP is evidence of limited prior interaction annotation, not proof that the co-abundance pattern itself is novel.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state signal produced by variable immune-cell representation and coordinated regulation of extracellular signaling, vesicle or membrane trafficking, glycosylation, and cellular energy or translation capacity. In this model, LRRC32 could mark a transforming-growth-factor-beta-regulatory state, CCL5 could report lymphoid or platelet-associated secretory activity, and the MRPS12–MRPS21 branch could reflect mitochondrial translational demand. The proposed mechanism is that immune or stress-related signaling alters membrane and extracellular regulatory processes while cells adjust mitochondrial protein synthesis and intracellular trafficking. This is a hypothesis only; the available enrichment and interaction evidence does not establish causality or a single biochemical pathway.

Web sources: https://www.genecards.org/card/LRRC32; https://v18.proteinatlas.org/ENSG00000137507-LRRC32/cell; https://www.uniprot.org/uniprotkb/Q14392/entry; https://pmc.ncbi.nlm.nih.gov/articles/PMC11554709/

### Important genes

#### LRRC32

- **Related proteins** (co-abundance neighbors): NADK (0.95), DICER1 (0.95), MOCS3 (0.92), TTC7A (0.91), NOL10 (0.91), RINT1 (0.90), PAXBP1 (0.87), MRPS12 (0.85), MRPS21 (0.84), OCRL (0.83), HAUS2 (0.82), ST3GAL1 (0.82), GALE (0.82), ATP6V1D (0.82), MTMR14 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: leucine rich repeat containing 32. This gene encodes a type I membrane protein which contains 20 leucine-rich repeats. Alterations in the chromosomal region 11q13-11q14 are involved in several pathologies. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: cleft palate, proliferative retinopathy, and developmental delay (0.623); asthma (0.502); atopic eczema (0.408); dermatitis (0.381); Hepatitis (0.355)
- **Europe PMC papers**: 2406
- **Why important**: LRRC32 is the dominant network hub, connecting many module genes with high edge weights. It encodes a leucine-rich-repeat membrane protein linked to transforming growth factor beta receptor signaling and extracellular localization. HPA shows regulatory-T-cell enhancement and broad tissue distribution, making it a plausible bridge between immune-cell composition and extracellular signaling. It also has substantial literature coverage and disease associations involving developmental and inflammatory conditions.
- **Conclusion**: Established evidence supports LRRC32 as the principal network-organizing gene and as a regulator of transforming growth factor beta-related biology. The hypothesis that it drives the entire module is not established; its centrality may instead reflect correlated cell composition or shared regulation.

#### CCL5

- **Related proteins** (co-abundance neighbors): TGFBR3 (0.93), MRPS12 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: C-C motif chemokine ligand 5. This gene is one of several chemokine genes clustered on the q-arm of chromosome 17. Chemokines form a superfamily of secreted proteins involved in immunoregulatory and inflammatory processes. The superfamily is divided into four subfamilies based on the arrangement of the N-terminal cysteine residues of the mature peptide. This chemokine, a member of the CC subfamily, functions as a chemoattracta…
- **Diseases (Open Targets)**: neoplasm (0.121); breast cancer (0.118); breast carcinoma (0.117); hepatocellular carcinoma (0.115); cancer (0.115)
- **Europe PMC papers**: 46015
- **Why important**: CCL5 is a secreted chemokine with a direct role in attracting monocytes, memory T helper cells, and eosinophils. HPA places it in bone marrow and lymphoid tissue and associates it with NK-cell, platelet, and T-cell populations, including memory T-cell subsets. Its connection to TGFBR3 and MRPS12 links an immune-secretory signal to the broader module. CCL5 also has the largest literature volume among the selected genes and extensive cancer and inflammatory disease relevance.
- **Conclusion**: Established evidence supports CCL5 as an immune and secretory marker that could explain part of the circulatory-system signal. It is not established that CCL5 mechanistically controls the nonimmune branches of the module; it may primarily report the abundance or activation state of particular blood-cell populations.

#### MRPS12

- **Related proteins** (co-abundance neighbors): LRRC32 (0.85), EIF4E3 (0.85), CCL5 (0.80); STRING partners: MRPS21 (0.992), NOL10 (0.761)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05954.1, huMAP3_05807.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein S12. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.519); hyperuricemia-pulmonary hypertension-renal failure-alkalosis syndrome (0.118); familial isolated dilated cardiomyopathy (0.080); Rare familial disorder with hypertrophic cardiomyopathy (0.075); non-small cell lung carcinoma (0.074)
- **Europe PMC papers**: 385
- **Why important**: MRPS12 is a connector between the high-centrality LRRC32 branch, EIF4E3, and CCL5. It has direct high-confidence STRING support with MRPS21 and additional support with NOL10, and it occurs with MRPS21 in two hu.MAP complexes. Its established function in mitochondrial translation provides a coherent anchor for the module's mitochondrial branch. Disease associations include neurodegenerative and cardiac phenotypes, while the literature also describes links between mitochondrial ribosomal proteins and cancer biology.
- **Conclusion**: Established evidence supports MRPS12 as a mitochondrial translation component embedded in known molecular relationships. It is reasonable to regard the MRPS12–MRPS21 connection as a genuine biological submodule, but there is insufficient evidence that this mitochondrial branch explains the whole co-abundance module.

#### HLA-DRB4

- **Related proteins** (co-abundance neighbors): ST3GAL1 (0.95), UBXN2B (0.94), CHKB (0.87), PNPLA8 (0.86), FRMD8 (0.85); STRING partners: none
- **HPA**: no annotation
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: major histocompatibility complex, class II, DR beta 4. HLA-DRB4 belongs to the HLA class II beta chain paralogues. This class II molecule is a heterodimer consisting of an alpha (DRA) and a beta (DRB) chain, both anchored in the membrane. It plays a central role in the immune system by presenting peptides derived from extracellular proteins. Class II molecules are expressed in antigen presenting cells. The beta chain is approximately 26-28 kDa and its…
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 2422
- **Why important**: HLA-DRB4 encodes a class two major histocompatibility complex beta chain involved in presentation of extracellular peptides by antigen-presenting cells and in T-cell-related immune responses. It connects in the module to ST3GAL1, UBXN2B, CHKB, PNPLA8, and FRMD8, forming an immune and membrane-metabolic neighborhood. Although HPA annotation is unavailable for this gene in the fact sheet, its established molecular function makes it an informative immune-state marker.
- **Conclusion**: Established evidence supports HLA-DRB4 as an antigen-presentation gene and supports an immune interpretation of its local module neighborhood. Its module edges are not independently supported as physical interactions, so the network should not be interpreted as an HLA-DRB4 complex.

#### ST3GAL1

- **Related proteins** (co-abundance neighbors): HLA-DRB4 (0.95), LRRC32 (0.82), PHF8 (0.82), SYTL4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ST3 beta-galactoside alpha-2,3-sialyltransferase 1. The protein encoded by this gene is a type II membrane protein that catalyzes the transfer of sialic acid from CMP-sialic acid to galactose-containing substrates. The encoded protein is normally found in the Golgi but can be proteolytically processed to a soluble form. Correct glycosylation of the encoded protein may be critical to its sialyltransferase activity. This protein, which is a member of…
- **Diseases (Open Targets)**: COVID-19 (0.463); severe acute respiratory syndrome (0.370); bone fracture (0.344); cerebral atherosclerosis (0.337); prostate carcinoma (0.334)
- **Europe PMC papers**: 1214
- **Why important**: ST3GAL1 is a Golgi sialyltransferase that modifies glycoproteins and glycolipids and can be processed into a soluble form. It connects HLA-DRB4, LRRC32, PHF8, and SYTL4, thereby linking immune-associated genes to glycosylation, transcriptional, and vesicle-related branches. HPA shows enhancement in neutrophils and innate lymphoid cells, and its known functions are relevant to cell-surface glycosylation and immune-cell behavior.
- **Conclusion**: Established evidence supports ST3GAL1 as a glycosylation enzyme with immune-cell expression. A role for altered sialylation in coordinating this module is plausible, but the current data do not establish that ST3GAL1 mediates the observed co-abundance relationships.

## Module 8

**Tissue pair**: cell line and circulatory_system  
**Genes (13)**: BCAS3, CEP63, KDM1B, MARCHF7, PDLIM5, RAD51C, RLF, SCRN3, SPTA1, TEX2, TLK1, XPA, ZC3H7A

### Function

No GO/KEGG term passed global correction, and there are no STRING functional-enrichment terms. Therefore, the module does not support a statistically established common pathway. Its genes instead suggest a heterogeneous cellular-maintenance program: DNA damage recognition and repair through XPA and RAD51C, chromatin and transcriptional regulation through TLK1, KDM1B, RLF and ZC3H7A, centrosome and cell-cycle-related functions through CEP63, and cytoskeletal or structural functions through SPTA1 and PDLIM5. These annotations are compatible with shared variation in genome maintenance, proliferation state, and cell structure, but the co-abundance network alone does not establish a single biochemical mechanism.

**Cell composition.** The module is not dominated by secreted or plasma proteins, since no member is annotated as secreted. Most genes have low tissue specificity, consistent with broadly expressed intracellular proteins rather than a tissue-restricted secretome. However, many genes show cell-type enhancement, including neutrophils or neutrophil progenitors, while SPTA1 is associated with erythrocyte progenitors and bone marrow, and PDLIM5 is enriched in muscle-related tissues and cardiomyocytes. The module may therefore reflect shared cell-type composition or blood-derived cellular material in the circulatory samples, rather than a process occurring uniformly across all cells. HPA protein-level interpretation in the matched tissues is limited because the fact sheet reports no matching tissue-level protein detections.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported for any pair in the module, and no STRING functional-enrichment term was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated here as established physical interactions or membership in known multiprotein complexes. Several individual gene functions are well established, such as XPA in nucleotide-excision repair, RAD51C in homologous recombination, TLK1 in chromatin-related regulation, SPTA1 in erythrocyte membrane architecture, and PDLIM5 as a muscle-associated scaffold, but the available STRING and hu.MAP evidence does not connect these functions into one validated complex or pathway.

**STRING interactions (score >= 0.7)**: 0 of 78 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a new biological discovery solely because it is absent from STRING and hu.MAP. The lack of database support may reflect a co-abundance relationship, cell-composition effect, context specificity, incomplete database coverage, or a mixture of these explanations. Its potentially novel aspect is the coordinated abundance pattern across cell line and circulatory_system involving genes from genome maintenance, chromatin regulation, centrosomal biology, erythroid structure, and muscle scaffolding. That interpretation remains exploratory and would require replication in independent cohorts, adjustment for blood-cell composition, and experimental or perturbational validation.

**Hypothesis.** Hypothesis: the module represents a shared abundance program influenced by cellular composition and proliferative or stress state, in which genome-maintenance and chromatin-regulatory genes covary with lineage- and structure-associated transcripts. In circulatory samples, neutrophil, progenitor, erythroid, and platelet-related contributions may generate part of the signal; in cell-line samples, variation in cell cycle, DNA damage response, and cytoskeletal state may produce a related pattern. A stronger mechanistic claim that these proteins form one pathway is not supported by the enrichment, STRING, or hu.MAP evidence.

### Important genes

#### XPA

- **Related proteins** (co-abundance neighbors): CEP63 (0.88), TEX2 (0.82), RAD51C (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: XPA, DNA damage recognition and repair factor. This gene encodes a zinc finger protein plays a central role in nucleotide excision repair (NER), a specialized type of DNA repair. NER is responsible for repair of UV radiation-induced photoproducts and DNA adducts induced by chemical carcinogens and chemotherapeutic drugs. The encoded protein interacts with DNA and several NER proteins, acting as a scaffold to assemble the NER incision complex a…
- **Diseases (Open Targets)**: xeroderma pigmentosum group A (0.822); xeroderma pigmentosum (0.788); basal cell carcinoma (0.612); non-melanoma skin carcinoma (0.523); skin cancer (0.509)
- **Europe PMC papers**: 5087
- **Why important**: XPA is one of the more connected genes in the module and links the CEP63 branch with TEX2 and RAD51C. Its established function is central DNA damage recognition and nucleotide-excision repair. It also has substantial literature support and strong disease associations with xeroderma pigmentosum and skin cancer.
- **Conclusion**: Established evidence supports XPA as a DNA-repair anchor and an informative marker of genome-maintenance biology. The hypothesis that its co-abundance with CEP63, TEX2, and RAD51C reflects a coordinated repair or replication state is plausible but not demonstrated by the available interaction resources.

#### RAD51C

- **Related proteins** (co-abundance neighbors): XPA (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAD51 paralog C. This gene is a member of the RAD51 family. RAD51 family members are highly similar to bacterial RecA and Saccharomyces cerevisiae Rad51 and are known to be involved in the homologous recombination and repair of DNA. This protein can interact with other RAD51 paralogs and is reported to be important for Holliday junction resolution. Mutations in this gene are associated with Fanconi anemia-like syn…
- **Diseases (Open Targets)**: hereditary breast ovarian cancer syndrome (0.806); Fanconi anemia complementation group O (0.753); Fanconi anemia (0.697); ovarian cancer (0.661); RAD51C-related cancer predisposition (0.637)
- **Europe PMC papers**: 7128
- **Why important**: RAD51C is connected to XPA and has a central role in homologous recombination, double-strand-break repair, and recombination-dependent telomere maintenance. It has the largest literature base among the selected genes and strong associations with Fanconi-anemia-like disease and hereditary cancer predisposition.
- **Conclusion**: Established evidence makes RAD51C a compelling genome-stability marker in this module. Its relationship with XPA is a co-abundance association here, not evidence that the module contains a validated XPA–RAD51C complex or pathway.

#### TLK1

- **Related proteins** (co-abundance neighbors): TEX2 (0.83), RLF (0.82), ZC3H7A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tousled like kinase 1. The protein encoded by this gene is a serine/threonine kinase that may be involved in the regulation of chromatin assembly. The encoded protein is only active when it is phosphorylated, and this phosphorylation is cell cycle-dependent, with the maximal activity of this protein coming during S phase. The catalytic activity of this protein is diminished by DNA damage and by blockage of DNA replicati…
- **Diseases (Open Targets)**: neurodegenerative disease (0.508); cancer (0.295); mixed connective tissue disease (0.262); autoimmune disorder of central nervous system (0.184); oropharynx cancer (0.145)
- **Europe PMC papers**: 635
- **Why important**: TLK1 is a relatively central connector linking TEX2, RLF, and ZC3H7A. It is a cell-cycle-regulated kinase associated with chromatin assembly, chromosome segregation, and responses to replication or DNA damage stress. Its disease literature includes cancer and neurodegenerative or autoimmune associations.
- **Conclusion**: Established evidence supports TLK1 as a plausible regulator of replication-associated chromatin state. The hypothesis that TLK1 coordinates the repair-related genes in this module remains unproven because no global enrichment, STRING interaction, or hu.MAP complex supports that model.

#### ZC3H7A

- **Related proteins** (co-abundance neighbors): CEP63 (0.83), MARCHF7 (0.82), SPTA1 (0.82), TLK1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger CCCH-type containing 7A. Enables miRNA binding activity. Involved in production of miRNAs involved in gene silencing by miRNA. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.415); bilirubin metabolism disease (0.217); hereditary persistence of fetal hemoglobin-sickle cell disease syndrome (0.058); hereditary persistence of fetal hemoglobin-beta-thalassemia syndrome (0.058); Abnormality of the gastrointestinal tract (0.046)
- **Europe PMC papers**: 156
- **Why important**: ZC3H7A has the strongest network position in the module and connects CEP63, MARCHF7, SPTA1, and TLK1. It is annotated for miRNA binding and miRNA processing, making it a potential post-transcriptional regulator linking otherwise diverse gene groups. It also has disease associations involving neurodegeneration and bilirubin or hemoglobin-related disorders.
- **Conclusion**: Established evidence supports ZC3H7A as an RNA-regulatory protein and as the principal network connector in this module. Its central position suggests a possible regulatory role, but co-abundance and predicted function do not establish that it controls the other module genes.

#### SPTA1

- **Related proteins** (co-abundance neighbors): ZC3H7A (0.82), PDLIM5 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: spectrin alpha, erythrocytic 1. This gene encodes a member of a family of molecular scaffold proteins that link the plasma membrane to the actin cytoskeleton and functions in the determination of cell shape, arrangement of transmembrane proteins, and organization of organelles. The encoded protein is primarily composed of 22 spectrin repeats which are involved in dimer formation. It forms a component of the erythrocyte plasma me…
- **Diseases (Open Targets)**: elliptocytosis 2 (0.813); pyropoikilocytosis, hereditary (0.751); hereditary spherocytosis type 3 (0.734); hereditary elliptocytosis (0.610); hereditary spherocytosis (0.542)
- **Europe PMC papers**: 1547
- **Why important**: SPTA1 connects the central ZC3H7A branch to PDLIM5 and is specifically associated with erythrocyte membrane architecture, actin organization, and cell shape. HPA links it to bone marrow and erythrocyte progenitors, while disease associations include hereditary spherocytosis and elliptocytosis.
- **Conclusion**: Established evidence identifies SPTA1 as a strong indicator of erythroid or blood-cell composition rather than a general intracellular pathway marker. Its presence supports the possibility that the shared module is partly driven by circulating-cell composition. A direct mechanistic connection to ZC3H7A or PDLIM5 is only a hypothesis.

#### PDLIM5

- **Related proteins** (co-abundance neighbors): SPTA1 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 5. This gene encodes a member of a family of proteins that possess a 100-amino acid PDZ domain at the N terminus and one to three LIM domains at the C-terminus. This family member functions as a scaffold protein that tethers protein kinases to the Z-disk in striated muscles. It is thought to function in cardiomyocyte expansion and in restraining postsynaptic growth of excitatory synapses. Alternative…
- **Diseases (Open Targets)**: prostate carcinoma (0.515); uterine corpus leiomyoma (0.461); neurodegenerative disease (0.423); prostate cancer (0.391); Abnormality of the skeletal system (0.375)
- **Europe PMC papers**: 1238
- **Why important**: PDLIM5 is connected to SPTA1 and is the module member with the clearest muscle-associated tissue pattern. It encodes a PDZ and LIM domain scaffold involved in tethering protein kinases to the striated-muscle Z-disc and is annotated in cardiac and muscle development. It also has substantial literature and disease associations.
- **Conclusion**: Established evidence supports PDLIM5 as a muscle and cytoskeletal scaffold, and its HPA pattern suggests that tissue or cell-type composition may contribute to the module. The hypothesis that it participates in a shared structural program with SPTA1 is biologically suggestive but not validated as a physical or functional interaction here.

## Module 9

**Tissue pair**: cell line and circulatory_system  
**Genes (6)**: CDH1, CTSH, EGFR, HTRA1, HYOU1, PAPLN

### Function

The module is best interpreted as a mixed extracellular, epithelial-interface, and cellular-stress program rather than as a confidently established canonical pathway. PAPLN is the central co-abundance hub, connected to every other module gene, while the remaining genes occupy peripheral positions. PAPLN is annotated with extracellular-matrix organization and basement-membrane localization; HTRA1 is a secreted protease; CDH1 is a cell-cell adhesion molecule; EGFR is a cell-surface receptor tyrosine kinase; CTSH is a lysosomal protease; and HYOU1 is an endoplasmic-reticulum stress and protein-folding factor. Together, these annotations support an extracellular-matrix, adhesion, proteolysis, receptor-signaling, and secretory-stress interpretation. No GO or KEGG term passed global correction, so the module does not have globally significant pathway enrichment. STRING terms (STRING Keyword Signal; within-query FDR = 0.00042) and (STRING Keyword Disulfide bond; within-query FDR = 0.013) are supportive context only, not global enrichment evidence.

**Cell composition.** The module is compositionally dominated by secreted or extracellularly associated proteins. PAPLN is secreted with an unknown location, HTRA1 is secreted to blood, and EGFR is reported as secreted to blood; CTSH and HYOU1 are intracellular or membrane-associated, whereas CDH1 has no secretome annotation. HPA indicates cell-type enhancement for every module gene, with signals spanning epithelial, stromal, glial, trophoblast, and immune-related cell types. Several genes show blood-cell enrichment, while others are not detected in immune cells or have low immune-cell specificity. Therefore, the shared module may partly reflect differing cell-type composition, blood-associated material, or extracellular protein abundance in the samples rather than a single conserved intracellular mechanism. HPA reports no matching protein-detection result for either queried tissue group, so tissue-level protein validation is unavailable here.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship among module members is the CDH1-EGFR pair. This relationship is biologically coherent because CDH1 marks epithelial cell adhesion and EGFR mediates cell-surface growth-factor signaling. Their repeated appearance in STRING cancer-cell and literature-derived terms (STRING TISSUES MDA-MB-231 cell; within-query FDR = 0.01), (STRING TISSUES Colorectal cancer cell line; within-query FDR = 0.0218), (STRING KEGG Melanoma; within-query FDR = 0.0332), (STRING KEGG Bladder cancer; within-query FDR = 0.0332), (STRING PMID (2016) Targeting MDM2 for Treatment of Adenoid Cystic Carcinoma.; within-query FDR = 0.0387), (STRING PMID (2014) Alveolar progenitor and stem cells in lung development, renewal and cancer.; within-query FDR = 0.0387), (STRING PMID (2013) Characterization of tumorigenic cell lines from the recurrence and lymph node metastasis of a human salivary mucoepidermoid carcinoma.; within-query FDR = 0.0387), and (STRING KEGG Endometrial cancer; within-query FDR = 0.0396) indicates that this pair is already well represented in prior biological knowledge. The other module pairings are not supported by high-confidence STRING links in the supplied results, and no hu.MAP complex contains at least two module members. Thus, the co-abundance edges mostly do not establish physical interaction or membership in one known protein complex.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: CDH1–EGFR (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Signal (FDR = 0.00042, 6 genes); TISSUES MDA-MB-231 cell (FDR = 0.01, 2 genes); Keyword Disulfide bond (FDR = 0.013, 5 genes); TISSUES Colorectal cancer cell line (FDR = 0.0218, 2 genes); KEGG Melanoma (FDR = 0.0332, 2 genes); KEGG Bladder cancer (FDR = 0.0332, 2 genes); PMID (2016) Targeting MDM2 for Treatment of Adenoid Cystic Carcinoma. (FDR = 0.0387, 3 genes); PMID (2014) Alveolar progenitor and stem cells in lung development, renewal and cancer. (FDR = 0.0387, 3 genes); PMID (2013) Characterization of tumorigenic cell lines from the recurrence and lymph node metastasis of a human salivary mucoepidermoid carcinoma. (FDR = 0.0387, 3 genes); KEGG Endometrial cancer (FDR = 0.0396, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The individual gene functions and the CDH1-EGFR relationship are not novel. The potentially new observation is the coordinated co-abundance of PAPLN with CTSH, HYOU1, HTRA1, CDH1, and EGFR across the cell-line and circulatory-system tissue pair. This should be described as a candidate network-level finding rather than a demonstrated new mechanism. Its novelty is supported by the lack of a matching hu.MAP complex and by the absence of high-confidence STRING relationships for most of the module edges, but those absences alone do not prove novelty. The lack of globally corrected GO or KEGG enrichment also means that pathway-level novelty or specificity cannot be claimed from enrichment.

**Hypothesis.** Hypothesis: the module reflects a shared extracellular-interface state in which PAPLN-linked matrix organization is co-regulated with HTRA1-mediated proteolysis, CDH1-dependent adhesion, EGFR-associated receptor signaling, CTSH-associated proteolysis, and HYOU1-associated secretory or hypoxic stress. In cell-line and circulatory-system samples, this pattern may arise from coordinated abundance of epithelial or stromal material together with blood- or secretory-associated proteins. The hypothesis predicts that the module will track extracellular matrix remodeling and epithelial-interface state more reliably than a single intracellular complex. It requires experimental testing because co-abundance does not demonstrate direct molecular interaction or causal regulation.

### Important genes

#### PAPLN

- **Related proteins** (co-abundance neighbors): CTSH (0.98), HYOU1 (0.94), HTRA1 (0.91), CDH1 (0.87), EGFR (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: papilin, proteoglycan like sulfated glycoprotein. Predicted to enable metalloendopeptidase activity. Predicted to be involved in extracellular matrix organization. Predicted to be located in basement membrane. Predicted to be active in extracellular matrix. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.515); Genu valgum (0.355); Genu varum (0.355); obesity disorder (0.352); neurodegenerative disease (0.265)
- **Europe PMC papers**: 333
- **Why important**: PAPLN is the structural hub of the module, with co-abundance links to every other member. It is annotated as a secreted papilin-like proteoglycan involved in extracellular-matrix organization and associated with basement membrane. Its broad cell-type-enhanced HPA profile and secreted annotation make it a plausible indicator of extracellular material or stromal contribution. It has fewer literature reports than the major receptors and adhesion genes, so its central network position is especially informative.
- **Conclusion**: Established: PAPLN is the module's co-abundance hub and has extracellular-matrix-related annotations. Hypothesis: PAPLN may organize or mark the extracellular context that brings the other module signals together; a direct scaffolding or regulatory role is not established.

#### CDH1

- **Related proteins** (co-abundance neighbors): PAPLN (0.87); STRING partners: EGFR (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cadherin 1. This gene encodes a classical cadherin of the cadherin superfamily. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature glycoprotein. This calcium-dependent cell-cell adhesion protein is comprised of five extracellular cadherin repeats, a transmembrane region and a highly conserved cyto…
- **Diseases (Open Targets)**: CDH1-related diffuse gastric and lobular breast cancer syndrome (0.833); blepharocheilodontic syndrome 1 (0.760); Familial gastric cancer (0.686); ovarian cancer (0.684); endometrial carcinoma (0.676)
- **Europe PMC papers**: 32214
- **Why important**: CDH1 is a canonical epithelial cell-cell adhesion gene with plasma-membrane and junctional localization. It is linked to cell adhesion, desmosome assembly, and cell morphogenesis, has extensive disease literature, and is associated with familial gastric, breast, ovarian, and endometrial cancer annotations. It is also one of the two module genes forming the high-confidence STRING relationship with EGFR.
- **Conclusion**: Established: CDH1 provides strong evidence for an epithelial adhesion component and has a known relationship with EGFR in STRING. Hypothesis: its co-abundance with PAPLN may indicate coordinated epithelial-interface or matrix-remodeling state rather than a new CDH1 complex.

#### EGFR

- **Related proteins** (co-abundance neighbors): PAPLN (0.81); STRING partners: CDH1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: epidermal growth factor receptor. The protein encoded by this gene is a transmembrane glycoprotein that is a member of the protein kinase superfamily. This protein is a receptor for members of the epidermal growth factor family. EGFR is a cell surface protein that binds to epidermal growth factor, thus inducing receptor dimerization and tyrosine autophosphorylation leading to cell proliferation. Mutations in this gene are associat…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.850); lung adenocarcinoma (0.774); cancer (0.737); head and neck squamous cell carcinoma (0.725); lung cancer (0.717)
- **Europe PMC papers**: 223694
- **Why important**: EGFR is a cell-surface receptor tyrosine kinase that mediates growth-factor signaling and is annotated with MAPK and receptor-signaling functions. It has the largest literature volume in the module and strong disease associations, particularly involving lung and other cancers. Its high-confidence STRING relationship with CDH1 and repeated cancer-cell signals in (STRING TISSUES MDA-MB-231 cell; within-query FDR = 0.01), (STRING TISSUES Colorectal cancer cell line; within-query FDR = 0.0218), (STRING KEGG Melanoma; within-query FDR = 0.0332), (STRING KEGG Bladder cancer; within-query FDR = 0.0332), (STRING PMID (2014) Alveolar progenitor and stem cells in lung development, renewal and cancer.; within-query FDR = 0.0387), (STRING PMID (2013) Characterization of tumorigenic cell lines from the recurrence and lymph node metastasis of a human salivary mucoepidermoid carcinoma.; within-query FDR = 0.0387), and (STRING KEGG Endometrial cancer; within-query FDR = 0.0396) make it an important known signaling anchor.
- **Conclusion**: Established: EGFR represents a well-known receptor-signaling component and is connected to CDH1 by established STRING evidence. Hypothesis: EGFR may couple the module to growth or repair signaling at an epithelial or stromal interface; the module does not establish EGFR activation.

#### HTRA1

- **Related proteins** (co-abundance neighbors): PAPLN (0.91); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HtrA serine peptidase 1. This gene encodes a member of the trypsin family of serine proteases. This protein is a secreted enzyme that is proposed to regulate the availability of insulin-like growth factors (IGFs) by cleaving IGF-binding proteins. It has also been suggested to be a regulator of cell growth. Variations in the promoter region of this gene are the cause of susceptibility to age-related macular degeneration ty…
- **Diseases (Open Targets)**: cerebral arteriopathy, autosomal dominant, with subcortical infarcts and leukoencephalopathy, type 2 (0.760); CARASIL syndrome (0.755); age-related macular degeneration (0.656); macular degeneration (0.584); age related macular degeneration 7 (0.545)
- **Europe PMC papers**: 4032
- **Why important**: HTRA1 is a secreted serine protease with proposed roles in proteolysis, cell growth, programmed cell death, and regulation of insulin-like-growth-factor availability. It is tissue-enhanced in ovary, secreted to blood, and associated with vascular and macular disease annotations. Its strong connection to the PAPLN hub and participation in the supplementary disulfide-bond and signal terms (STRING Keyword Signal; within-query FDR = 0.00042) and (STRING Keyword Disulfide bond; within-query FDR = 0.013) support an extracellular remodeling interpretation.
- **Conclusion**: Established: HTRA1 is a secreted protease with disease-relevant extracellular functions and is co-abundant with the PAPLN-centered module. Hypothesis: HTRA1 may contribute to matrix or growth-factor remodeling within the shared state, but a direct interaction with PAPLN is not demonstrated.

#### CTSH

- **Related proteins** (co-abundance neighbors): PAPLN (0.98); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles, Cytosol, Cytoplasmic bodies; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cathepsin H. The protein encoded by this gene is a lysosomal cysteine proteinase important in the overall degradation of lysosomal proteins. It is composed of a dimer of disulfide-linked heavy and light chains, both produced from a single protein precursor. The encoded protein, which belongs to the peptidase C1 protein family, can act both as an aminopeptidase and as an endopeptidase. Increased expression of t…
- **Diseases (Open Targets)**: type 1 diabetes mellitus (0.558); Alzheimer disease (0.549); skin cancer (0.494); basal cell carcinoma (0.486); dementia (0.457)
- **Europe PMC papers**: 2242
- **Why important**: CTSH is a lysosomal cysteine proteinase that can act as both an aminopeptidase and an endopeptidase. It has immune-related and proteolysis annotations, tissue enhancement in lung, and HPA enrichment across multiple myeloid and lymphoid blood-cell categories. Its connection to PAPLN and recurrence in supplementary STRING literature terms (STRING Keyword Signal; within-query FDR = 0.00042), (STRING Keyword Disulfide bond; within-query FDR = 0.013), (STRING PMID (2016) Targeting MDM2 for Treatment of Adenoid Cystic Carcinoma.; within-query FDR = 0.0387), (STRING PMID (2014) Alveolar progenitor and stem cells in lung development, renewal and cancer.; within-query FDR = 0.0387), and (STRING PMID (2013) Characterization of tumorigenic cell lines from the recurrence and lymph node metastasis of a human salivary mucoepidermoid carcinoma.; within-query FDR = 0.0387) make it useful for distinguishing extracellular or epithelial signals from immune and lysosomal contributions.
- **Conclusion**: Established: CTSH contributes lysosomal proteolysis and has substantial immune-cell and lung-associated evidence. Hypothesis: CTSH may indicate immune-cell admixture or coordinated proteolytic remodeling in the samples, rather than being a physical partner of PAPLN.

## Module 10

**Tissue pair**: cell line and circulatory_system  
**Genes (6)**: DOCK5, MGAT4A, NMRAL1, SEC24A, TMEM214, TUT4

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. The module therefore does not support a statistically established pathway annotation. Its structure is centered on MGAT4A, with the other genes connected only to that hub. The gene annotations suggest a mixed cellular program involving Golgi N-glycan processing, ER-to-Golgi trafficking, intracellular transport, small-GTPase-associated migration, RNA processing, redox and antiviral regulation, and a possible apoptosis-related process. This is better interpreted as a co-abundance pattern spanning secretory-pathway and cell-regulatory functions than as a demonstrated single biochemical pathway.

**Cell composition.** The module is not dominated by broadly secreted plasma proteins: only MGAT4A is annotated as secreted to blood, while the other genes are not annotated as secreted. Most genes have low tissue specificity, arguing for broadly expressed or generally reusable cellular functions rather than a strongly tissue-restricted program. All genes have an HPA cell-type enhanced annotation, but these annotations are heterogeneous, including trophoblasts, neutrophils, oligodendrocytes, podocytes, thyrotrophs, plasma cells, endocrine cells, microglia, progenitors and myonuclei. DOCK5 is immune-cell enhanced in neutrophils, and MGAT4A is tissue enhanced in bone marrow. Thus, the shared signal could partly reflect shared cell types or blood-related material, but the HPA evidence does not identify a uniform blood-cell or plasma-protein module. HPA matched-tissue protein detection is unavailable for both sample groups, so protein-level confirmation is lacking.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and no STRING functional enrichment was present. No hu.MAP complex contained multiple module members. Consequently, the co-abundance edges are not supported here by established high-confidence physical interactions or a known multi-protein complex. The absence of these relationships does not disprove coordinated regulation, shared cell composition, indirect pathway coupling, or technical co-variation; it does mean that a direct molecular complex interpretation is unsupported by the supplied databases.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel tissue-pair co-abundance observation, because the module is not represented by a known STRING interaction network, a STRING enrichment result, or a multi-member hu.MAP complex. However, those absences alone do not establish biological novelty. The lack of globally corrected GO/KEGG enrichment, the heterogeneous cell-type annotations, and the absence of database-supported physical interactions make a new mechanism premature. The strongest defensible claim is that this is a potentially context-specific co-abundance pattern requiring replication, cell-composition adjustment, and orthogonal interaction or perturbation experiments.

**Hypothesis.** Hypothesis: coordinated abundance of MGAT4A with SEC24A, TMEM214, DOCK5, NMRAL1 and TUT4 may reflect a cell-state program linking secretory-pathway organization and glycoprotein processing to cytoskeletal or migration-related regulation, RNA maturation, and stress or antiviral control. MGAT4A could act as the most prominent network-level marker of this state, while the apparent association with the other genes may be indirect and mediated by shared cell type, secretory demand, or cellular stress. This hypothesis is not an enriched-pathway conclusion and should be tested experimentally.

### Important genes

#### MGAT4A

- **Related proteins** (co-abundance neighbors): NMRAL1 (0.84), DOCK5 (0.82), SEC24A (0.82), TMEM214 (0.81), TUT4 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminyltransferase A. This gene encodes a key glycosyltransferase that regulates the formation of tri- and multiantennary branching structures in the Golgi apparatus. The encoded protein, in addition to the related isoenzyme B, catalyzes the transfer of N-acetylglucosamine (GlcNAc) from UDP-GlcNAc in a beta-1,4 linkage to the Man-alpha-1,3-Man-beta-1,4-GlcNAc arm of R-Man-alpha-1,6(GlcNAc-beta-1,2-Man-alpha-1,3)Man-bet…
- **Diseases (Open Targets)**: COVID-19 (0.371); smoking initiation (0.280); placental abruption (0.233); obesity disorder (0.127); neoplasm (0.081)
- **Europe PMC papers**: 608
- **Why important**: MGAT4A is the central network hub, connected to every other module member and having the strongest supplied network support. Its established function is Golgi N-glycan branching and glycoprotein biosynthesis. HPA places it in a bone-marrow-enhanced context, in microglia, neutrophil progenitors and T-cells, and annotates it as secreted to blood. It also has substantial literature coverage and disease associations including COVID-19, smoking initiation, placental abruption, obesity disorder and neoplasm.
- **Conclusion**: Established evidence supports MGAT4A as the best marker of a glycoprotein-processing or Golgi-related component and as the network anchor. It is not established that MGAT4A directly regulates the other five proteins; that connection is a module-level hypothesis.

#### SEC24A

- **Related proteins** (co-abundance neighbors): MGAT4A (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC24 homolog A, COPII component. The protein encoded by this gene belongs to a family of proteins that are homologous to yeast Sec24. This protein is a component of coat protein II (COPII)-coated vesicles that mediate protein transport from the endoplasmic reticulum. COPII acts in the cytoplasm to promote the transport of secretory, plasma membrane, and vacuolar proteins from the endoplasmic reticulum to the golgi complex. Altern…
- **Diseases (Open Targets)**: Graves disease (0.218); hyperlipoproteinemia type V (0.071); combined low LDL and fibrinogen (0.069); Hyperlipoproteinemia type 1 (0.062); apolipoprotein c-III deficiency (0.062)
- **Europe PMC papers**: 808
- **Why important**: SEC24A is connected directly to the hub and has an established role in COPII cargo loading and ER-to-Golgi transport of secretory and membrane proteins. Its HPA single-cell enhancement in endometrial glandular cells and plasma cells is compatible with secretory-cell biology. It has the largest literature volume among the module genes and reported associations with Graves disease and several lipoprotein-related disorders.
- **Conclusion**: Established evidence supports SEC24A as a plausible secretory-trafficking component of the module. The data do not establish a direct SEC24A-MGAT4A interaction or prove that altered COPII transport causes the observed co-abundance.

#### DOCK5

- **Related proteins** (co-abundance neighbors): MGAT4A (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dedicator of cytokinesis 5. This gene encodes a member of the dedicator of cytokinesis protein family. Members of this family act as guanine nucleotide exchange factors for small Rho family G proteins. The protein encoded by this gene is thought to associate with adaptors CRK and CRKL, and function in regulation of intestinal epithelial cell spreading and migration on collagen IV. Similar proteins in mouse and zebrafish also…
- **Diseases (Open Targets)**: neurodegenerative disease (0.491); coronary artery disorder (0.411); coronary atherosclerosis (0.335); refractive error (0.332); glaucoma (0.323)
- **Europe PMC papers**: 706
- **Why important**: DOCK5 is directly connected to MGAT4A and encodes a guanine-nucleotide exchange factor family member involved in small-GTPase signaling, cell migration, adhesion-dependent spreading and myoblast fusion. HPA identifies neutrophil enhancement and immune-cell enhancement, providing a possible link to circulatory-system cellular composition. It has substantial literature coverage and associations with neurodegenerative disease, coronary artery disease, atherosclerosis, refractive error and glaucoma.
- **Conclusion**: Established evidence supports DOCK5 as a cell-migration and cytoskeletal-regulation marker, with a possible blood-cell relevance. Its connection to the Golgi and glycosylation component remains indirect and should be treated as a hypothesis.

#### NMRAL1

- **Related proteins** (co-abundance neighbors): MGAT4A (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NmrA like redox sensor 1. This gene encodes an NADPH sensor protein that preferentially binds to NADPH. The encoded protein also negatively regulates the activity of NF-kappaB in a ubiquitylation-dependent manner. It plays a key role in cellular antiviral response by negatively regulating the interferon response factor 3-mediated expression of interferon beta. Alternative splicing of this gene results in multiple transcrip…
- **Diseases (Open Targets)**: osteoarthritis, knee (0.163); hypertensive disorder (0.135); migraine disorder (0.096); schizophrenia (0.071); coronary artery disorder (0.071)
- **Europe PMC papers**: 174
- **Why important**: NMRAL1 is directly connected to the hub and encodes an NADPH sensor that negatively regulates NF-kappaB and interferon responses through a reported ubiquitylation-dependent mechanism. Its HPA annotation is broadly distributed, with enhancement in extravillous trophoblasts and gastric chief cells. It has disease associations including osteoarthritis, hypertension, migraine, schizophrenia and coronary artery disease.
- **Conclusion**: Established evidence supports NMRAL1 as a redox-sensitive antiviral and inflammatory regulator. Its presence could indicate shared cellular stress or immune signaling, but the module does not establish that NMRAL1 controls MGAT4A or secretory trafficking.

#### TUT4

- **Related proteins** (co-abundance neighbors): MGAT4A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: terminal uridylyl transferase 4. ZCCHC11 is an RNA uridyltransferase (EC 2.7.7.52) that uses UTP to add uridines to the 3-prime end of substrate RNA molecules (Jones et al., 2009 [PubMed 19701194]).[supplied by OMIM, Jan 2011]
- **Diseases (Open Targets)**: cataract (0.168); trauma complication (0.168); cancer (0.087); hepatocellular carcinoma (0.075); autosomal dominant macrothrombocytopenia (0.049)
- **Europe PMC papers**: 616
- **Why important**: TUT4 is directly connected to MGAT4A and is an RNA uridyltransferase involved in RNA three-prime-end processing, microRNA metabolism, pre-microRNA processing, oocyte maturation and stem-cell population maintenance. HPA identifies enhanced annotation in corticotrophs and myonuclei. It has substantial literature coverage and associations with cataract, trauma complications, cancer, hepatocellular carcinoma and autosomal dominant macrothrombocytopenia.
- **Conclusion**: Established evidence supports TUT4 as an RNA-processing regulator that may mark a cell-state or post-transcriptional program. Its co-abundance with the secretory and migration genes is not explained by a known complex and remains hypothetical.

#### TMEM214

- **Related proteins** (co-abundance neighbors): MGAT4A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Golgi apparatus, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transmembrane protein 214. Predicted to be involved in apoptotic process. Located in several cellular components, including Golgi apparatus; cytoplasmic microtubule; and endoplasmic reticulum. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: autism (0.111); Flexion contracture (0.111); osteoarthritis, knee (0.106); osteoarthritis, hip (0.106); risk-taking behaviour (0.074)
- **Europe PMC papers**: 203
- **Why important**: TMEM214 is directly connected to MGAT4A and is annotated as a predicted participant in apoptosis, with localization in the ER, Golgi apparatus and cytosol. HPA identifies enhancement in extravillous and syncytiotrophoblasts. It has fewer reported papers than the other selected genes but has associations with autism, joint contracture, osteoarthritis and risk-taking behaviour.
- **Conclusion**: Established evidence supports TMEM214 as a plausible ER-Golgi and cell-survival marker, although its functional annotation is comparatively limited. Its role in the module may reflect secretory or stress-state coordination, but this is a hypothesis rather than a demonstrated mechanism.
