# Conserved co-abundance modules: cell line and cervix_uterine

## Module 0

**Tissue pair**: cell line and cervix_uterine  
**Genes (20)**: SFN, ACADM, ACOX3, CDH1, CARHSP1, C3, CYBB, DAAM1, DSC3, DSG3, GALNT7, SERPING1, KRT4, KRT6A, LY6D, RRBP1, SCEL, WARS1, TRIM29, VAC14

### Function

The module most plausibly reflects an epithelial barrier, adhesion, and differentiation program coupled to complement and innate-inflammatory biology. Its strongest network position is occupied by CYBB, which connects epithelial-associated genes including DSG3, DSC3, CDH1, KRT6A, and SFN with complement-associated C3 and SERPING1. The epithelial interpretation is supported by HPA enrichment for esophageal, skin, vaginal, cervical, and suprabasal epithelial populations, together with the known roles of desmosomal cadherins, E-cadherin, keratins, and sciellin in epithelial junctions, intermediate filaments, and differentiation. The complement interpretation is supported by the established functions of C3 and SERPING1 and by the STRING C3-SERPING1 relationship. No GO/KEGG term passed global correction, so GO/KEGG provides no globally significant enrichment for this module. STRING terms (STRING DISEASES Skin disease; within-query FDR = 0.0036), (STRING SMART Cadherin repeats.; within-query FDR = 0.0153), and (STRING Keyword Cleavage on pair of basic residues; within-query FDR = 0.0387) are supplementary evidence only and point toward skin disease, cadherin repeats, and cleavage-related annotation rather than independently establishing module function.

**Cell composition.** This is predominantly an epithelial-associated module rather than a broadly expressed housekeeping module. HPA links many members to esophageal apical, basal, or suprabasal cells, suprabasal keratinocytes, skin, vagina, and cervix. DSG3, DSC3, CDH1, KRT6A, KRT4, LY6D, TRIM29, SFN, and SCEL support epithelial structure, differentiation, or barrier biology. The module also contains an immune and secreted-protein component: CYBB is associated with monocytes and macrophage-lineage cells, while C3 and SERPING1 are secreted to blood and associated with liver or immune-cell contexts. Thus, the shared signal may reflect epithelial cell state together with complement-rich extracellular material, immune-cell admixture, or a common epithelial–innate immune interface. It is not best characterized as a plasma-protein-only or housekeeping module, although the secreted complement component warrants caution about sample composition.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING reports a small set of high-confidence pairwise relationships. The C3-SERPING1 relationship (STRING DISEASES Skin disease; within-query FDR = 0.0036) is consistent with complement regulation, and the DSC3-DSG3 relationship (STRING SMART Cadherin repeats.; within-query FDR = 0.0153) is consistent with desmosomal cadherin biology. ACADM-ACOX3 is a metabolic relationship linking mitochondrial and peroxisomal fatty-acid oxidation. STRING functional annotations connect C3, SERPING1, DSG3, DSC3, CDH1, CYBB, KRT6A, and KRT4 to skin disease (STRING DISEASES Skin disease; within-query FDR = 0.0036), DSG3, CDH1, and DSC3 to cadherin repeats (STRING SMART Cadherin repeats.; within-query FDR = 0.0153), and C3, DSG3, CDH1, and DSC3 to cleavage on pairs of basic residues (STRING Keyword Cleavage on pair of basic residues; within-query FDR = 0.0387). These are supportive annotations and are not globally corrected enrichment results. hu.MAP independently places C3 and SERPING1 together in several complexes (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), and (hu.MAP huMAP3_15040.1), and places C3, SERPING1, and TRIM29 together in (hu.MAP huMAP3_10678.1). The repeated C3-SERPING1 overlap indicates known complement-associated protein context, whereas most epithelial genes lack corresponding hu.MAP complex support. Overall, the network combines a few established molecular relationships with many co-abundance edges that may represent shared cell state, tissue composition, or indirect regulation rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 3 of 190 gene pairs: ACADM–ACOX3 (0.735); C3–SERPING1 (0.954); DSC3–DSG3 (0.934)
**STRING functional enrichment (supplementary, within-query FDR)**: DISEASES Skin disease (FDR = 0.0036, 8 genes); SMART Cadherin repeats. (FDR = 0.0153, 3 genes); Keyword Cleavage on pair of basic residues (FDR = 0.0387, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10678.1 (C3, SERPING1, TRIM29; 3/71); huMAP3_09531.1 (C3, SERPING1; 2/47); huMAP3_10101.1 (C3, SERPING1; 2/49); huMAP3_15040.1 (C3, SERPING1; 2/64)

### Novelty

The module should not be called a wholly new molecular complex or a newly discovered pathway. C3-SERPING1, DSC3-DSG3, and ACADM-ACOX3 are already supported by STRING, and C3-SERPING1 is repeatedly represented in hu.MAP. The epithelial roles of DSG3, DSC3, CDH1, KRT4, KRT6A, TRIM29, SFN, and SCEL are also established. A potentially novel aspect is the reproducible co-abundance of this particular epithelial, complement, metabolic, and intracellular-protein combination across the cell line and cervix_uterine tissue pair. However, database absence for many edges does not prove novelty, and the sparse direct-interaction support means that this claim requires validation in independent cohorts, cell-type-resolved data, and perturbation experiments.

**Hypothesis.** Hypothesis: a differentiated epithelial barrier state in the shared cell line and cervix_uterine context is accompanied by local or sample-level innate immune activity. Epithelial junction and differentiation genes may define the cellular state, while complement proteins and CYBB may report extracellular inflammatory exposure, immune-cell admixture, or epithelial–immune crosstalk. SERPING1 could restrain complement activation while C3 provides the central complement substrate, and CYBB could connect inflammatory or phagocyte-associated redox biology to the epithelial state. The metabolic pair ACADM-ACOX3 may reflect a linked energy or lipid-oxidation state, but its connection to the epithelial–complement program remains speculative. This hypothesis is not established by the co-abundance graph alone and should be tested with cell deconvolution, spatial or single-cell measurements, complement-activation assays, and perturbation of epithelial junction or innate-immune pathways.

### Important genes

#### CYBB

- **Related proteins** (co-abundance neighbors): DSG3 (0.96), TRIM29 (0.96), DSC3 (0.94), SFN (0.92), CDH1 (0.91), ACADM (0.90), CARHSP1 (0.89), C3 (0.88), KRT6A (0.85), SCEL (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome b-245 beta chain. Cytochrome b (-245) is composed of cytochrome b alpha (CYBA) and beta (CYBB) chain. It has been proposed as a primary component of the microbicidal oxidase system of phagocytes. CYBB deficiency is one of five described biochemical defects associated with chronic granulomatous disease (CGD). In this disorder, there is decreased activity of phagocyte NADPH oxidase; neutrophils are able to phagocytiz…
- **Diseases (Open Targets)**: chronic granulomatous disease (0.864); neurodegenerative disease (0.352); hereditary disease (0.191); discoid lupus erythematosus (0.185); Kartagener Syndrome (0.118)
- **Europe PMC papers**: 6704
- **Why important**: CYBB is the highest-positioned network gene in the module and connects epithelial-associated members, complement genes, and metabolic or stress-related genes. Its established function in the phagocyte NADPH oxidase and defense or inflammatory responses provides a plausible bridge between epithelial state and innate immunity. HPA associates it with monocyte and macrophage-lineage cells, while its disease association with chronic granulomatous disease is well established and its literature volume is substantial.
- **Conclusion**: Established evidence supports CYBB as a network bridge and an innate-defense marker associated with myeloid biology. It is not established that CYBB is produced by the epithelial cells represented in this module. The most cautious interpretation is that CYBB may mark immune-cell admixture or epithelial–immune crosstalk; direct epithelial involvement is a hypothesis.

#### C3

- **Related proteins** (co-abundance neighbors): CYBB (0.88); STRING partners: SERPING1 (0.954)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a central complement component, is secreted to blood, has liver and immune-cell associations in HPA, and has a very strong STRING relationship with SERPING1. It recurs with SERPING1 across several hu.MAP complexes (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), and (hu.MAP huMAP3_15040.1). Its broad disease relevance and extensive literature make it the clearest functional anchor for the extracellular innate-immune arm of the module.
- **Conclusion**: Established evidence supports C3 as a complement-related extracellular component and as part of a known C3-SERPING1 protein context. The module does not establish local complement activation in cervix_uterine or prove that C3 originates from the epithelial compartment.

#### SERPING1

- **Related proteins** (co-abundance neighbors): DSC3 (0.99), ACOX3 (0.91), WARS1 (0.87), VAC14 (0.87), RRBP1 (0.84), GALNT7 (0.84), DAAM1 (0.82); STRING partners: C3 (0.954)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1
- **Function (MyGene.info)**: serpin family G member 1. This gene encodes a highly glycosylated plasma protein involved in the regulation of the complement cascade. Its encoded protein, C1 inhibitor, inhibits activated C1r and C1s of the first complement component and thus regulates complement activation. It is synthesized in the liver, and its deficiency is associated with hereditary angioneurotic oedema (HANE). Alternative splicing results in multipl…
- **Diseases (Open Targets)**: hereditary angioedema with C1Inh deficiency (0.828); hereditary angioedema type 1 (0.750); hereditary angioedema (0.728); angioedema (0.616); hereditary angioedema type 2 (0.614)
- **Europe PMC papers**: 4203
- **Why important**: SERPING1 is a relatively central module gene and the principal complement-regulatory partner of C3 in the available STRING evidence. It is a secreted liver-associated plasma protein that inhibits activated C1r and C1s, has repeated hu.MAP membership with C3, and has strong disease associations involving hereditary angioedema. Its network placement also links it to genes involved in glycosylation, vesicles, endoplasmic-reticulum organization, and morphogenesis.
- **Conclusion**: Established evidence supports SERPING1 as a complement regulator and as part of a known extracellular protein context with C3. Its co-abundance with epithelial genes may reflect shared inflammatory milieu, secretion, or tissue composition; a direct regulatory role in the epithelial program remains a hypothesis.

#### CDH1

- **Related proteins** (co-abundance neighbors): CYBB (0.91); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cadherin 1. This gene encodes a classical cadherin of the cadherin superfamily. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature glycoprotein. This calcium-dependent cell-cell adhesion protein is comprised of five extracellular cadherin repeats, a transmembrane region and a highly conserved cyto…
- **Diseases (Open Targets)**: CDH1-related diffuse gastric and lobular breast cancer syndrome (0.833); blepharocheilodontic syndrome 1 (0.760); Familial gastric cancer (0.686); ovarian cancer (0.684); endometrial carcinoma (0.676)
- **Europe PMC papers**: 32214
- **Why important**: CDH1 is a canonical epithelial cell-junction gene with very extensive literature, cervix_uterine protein detection, and HPA associations with epithelial cell types. Its annotations include homophilic cell adhesion and junction assembly, and it contributes to the STRING cadherin-related supplementary signal (STRING SMART Cadherin repeats.; within-query FDR = 0.0153) and the skin-disease signal (STRING DISEASES Skin disease; within-query FDR = 0.0036). Its disease associations include hereditary diffuse gastric and lobular breast cancer syndrome and several epithelial cancers.
- **Conclusion**: Established evidence supports CDH1 as a marker and mediator of epithelial adhesion and junctional integrity. Its module membership is consistent with epithelial organization, but the graph does not demonstrate that CDH1 physically interacts with every co-abundant module member or that it drives the complement component.

#### DSG3

- **Related proteins** (co-abundance neighbors): CYBB (0.96); STRING partners: DSC3 (0.934)
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enriched; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: desmoglein 3. This gene encodes a member of the desmoglein family and cadherin cell adhesion molecule superfamily of proteins. Desmogleins are calcium-binding transmembrane glycoprotein components of desmosomes, cell-cell junctions between epithelial, myocardial, and other cell types. The encoded preproprotein is proteolytically processed to generate the mature glycoprotein. This gene is present in a gene clust…
- **Diseases (Open Targets)**: blistering, acantholytic, of oral and laryngeal mucosa (0.442); primary thrombocytopenia (0.280); pemphigus vulgaris (0.137); paraneoplastic pemphigus (0.108); neoplasm (0.107)
- **Europe PMC papers**: 1797
- **Why important**: DSG3 is an epithelial desmosomal cadherin with cervix, vagina, and esophageal HPA associations and localization in desmosomal cell-junction biology. It is linked to DSC3 by a high-confidence STRING relationship and contributes to the cadherin and cleavage-related supplementary terms (STRING SMART Cadherin repeats.; within-query FDR = 0.0153) and (STRING Keyword Cleavage on pair of basic residues; within-query FDR = 0.0387). Its disease associations include pemphigus vulgaris and other blistering or epithelial disorders, making it a strong structural and disease-relevant representative of the epithelial arm.
- **Conclusion**: Established evidence supports DSG3 as a desmosomal adhesion protein and supports a known DSG3-DSC3 relationship. Its co-abundance with complement and CYBB is consistent with epithelial barrier or inflammatory context, but a direct mechanistic link between desmosomes and complement is not demonstrated here.

#### KRT6A

- **Related proteins** (co-abundance neighbors): LY6D (0.90), CYBB (0.85); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Intermediate filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 6A. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. As many as six of this type II cytokeratin (KRT6) have been identified; the multiplicity of the genes is attributed to successi…
- **Diseases (Open Targets)**: pachyonychia congenita (0.825); pachyonychia congenita 1 (0.371); skin neoplasm (0.200); hereditary disease (0.194); skin cancer (0.167)
- **Europe PMC papers**: 2238
- **Why important**: KRT6A represents the epithelial differentiation and intermediate-filament component of the module. HPA associates it with cervix, esophagus, vagina, suprabasal keratinocytes, and epithelial populations, and it is detected in cervix_uterine. Its known role in epithelial morphogenesis, differentiation, keratinization, and cell behavior, together with its association with pachyonychia congenita, makes it informative despite its modest local network connectivity.
- **Conclusion**: Established evidence supports KRT6A as an epithelial structural and differentiation marker. Its presence strengthens the epithelial-state interpretation, but it does not by itself establish a causal connection to C3, SERPING1, or CYBB.

## Module 1

**Tissue pair**: cell line and cervix_uterine  
**Genes (41)**: PPP2R5D, BZW2, ACLY, AP3B1, ASCC3, ATXN10, CARM1, CLUH, NCAPD2, NCAPG, CYFIP1, DDX6, POLD1, DYNC1H1, FLII, HARS1, EIF4G1, LTA4H, MCM5, MOV10, MSH6, NAA15, NEMF, NUP93, PFKP, PIK3R4, PRPF31, CAD, ELAC2, DIS3, SEC24A, SMC4, SNX2, SUPT5H, EPRS1, IARS1, LARS1, MARS1, QARS1, TARS1, VPS45

### Function

The module is best interpreted as a cytosolic protein-biosynthesis and genome-maintenance program centered on aminoacyl-tRNA charging and translation. The primary globally corrected evidence supports catalytic activity on nucleic acids (GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.000402), aminoacyl-tRNA ligase activity and tRNA aminoacylation (5 globally significant GO/KEGG terms, q_global 0.00148–0.00189; see the table), aminoacyl-tRNA biosynthesis (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 0.00189), the aminoacyl-tRNA synthetase multienzyme complex (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.00484), tRNA catalysis (GO:MF catalytic activity, acting on a tRNA; q_global = 0.00513), translation and protein biosynthesis (GO:BP translation; q_global = 0.00667) (GO:BP protein biosynthetic process; q_global = 0.00667), RNA catalysis (GO:MF catalytic activity, acting on RNA; q_global = 0.0097), and tRNA metabolism (GO:BP tRNA metabolic process; q_global = 0.0247). Nucleic-acid binding and ATP binding (GO:MF nucleic acid binding; q_global = 0.0299) (GO:MF ATP binding; q_global = 0.0495) are broader supporting signals. The remaining genes connect this core to RNA processing, translation control, DNA replication and repair, chromosome condensation, metabolism, and intracellular transport.

**Cell composition.** The module is not a plasma or secreted-protein module: HPA reports no secreted genes. Most genes have low tissue specificity and low immune-cell specificity, consistent with a broadly expressed housekeeping-like program rather than a tissue-exclusive signature. Some genes are enhanced in erythrocyte progenitors, megakaryocyte progenitors, trophoblast populations, bone marrow, lymphoid tissue, and muscle, indicating a cell-state component. The evidence does not support interpreting the module primarily as blood contamination or a circulating-protein signal. Shared abundance in cell line and cervix_uterine may instead reflect broadly active biosynthesis, proliferation, or progenitor-like cellular states. Protein detection is widespread in cervix_uterine, while the cell-line comparison lacks a matching HPA tissue dataset, so the cross-context interpretation remains cautious.

**GO/KEGG enrichment**: 15 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF catalytic activity, acting on a nucleic acid | 0.000402 | ASCC3, DDX6, DIS3, ELAC2, EPRS1, HARS1, IARS1, LARS1, MARS1, MCM5, MOV10, MSH6, POLD1, QARS1, TARS1 |
| GO:MF aminoacyl-tRNA ligase activity | 0.00148 | EPRS1, HARS1, IARS1, LARS1, MARS1, QARS1, TARS1 |
| GO:BP tRNA aminoacylation for protein translation | 0.00148 | EPRS1, HARS1, IARS1, LARS1, MARS1, QARS1, TARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 0.00148 | EPRS1, HARS1, IARS1, LARS1, MARS1, QARS1, TARS1 |
| GO:BP amino acid activation | 0.00189 | EPRS1, HARS1, IARS1, LARS1, MARS1, QARS1, TARS1 |
| GO:BP tRNA aminoacylation | 0.00189 | EPRS1, HARS1, IARS1, LARS1, MARS1, QARS1, TARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 0.00189 | EPRS1, HARS1, IARS1, LARS1, MARS1, QARS1, TARS1 |
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 0.00484 | EPRS1, IARS1, LARS1, MARS1, QARS1 |
| GO:MF catalytic activity, acting on a tRNA | 0.00513 | ELAC2, EPRS1, HARS1, IARS1, LARS1, MARS1, QARS1, TARS1 |
| GO:BP translation | 0.00667 | ASCC3, BZW2, CYFIP1, DDX6, EIF4G1, EPRS1, HARS1, IARS1, LARS1, MARS1, NEMF, QARS1, TARS1 |
| GO:BP protein biosynthetic process | 0.00667 | ASCC3, BZW2, CYFIP1, DDX6, EIF4G1, EPRS1, HARS1, IARS1, LARS1, MARS1, NEMF, QARS1, TARS1 |
| GO:MF catalytic activity, acting on RNA | 0.0097 | DDX6, DIS3, ELAC2, EPRS1, HARS1, IARS1, LARS1, MARS1, MOV10, QARS1, TARS1 |
| GO:BP tRNA metabolic process | 0.0247 | ELAC2, EPRS1, HARS1, IARS1, LARS1, MARS1, QARS1, TARS1 |
| GO:MF nucleic acid binding | 0.0299 | ASCC3, CARM1, CLUH, CYFIP1, DDX6, DIS3, DYNC1H1, EIF4G1, ELAC2, EPRS1, HARS1, IARS1, LTA4H, MARS1, MCM5, MOV10, MSH6, NAA15, NEMF, POLD1, PRPF31, SMC4, SUPT5H, TARS1 |
| GO:MF ATP binding | 0.0495 | ACLY, ASCC3, CAD, DDX6, DYNC1H1, EIF4G1, EPRS1, HARS1, IARS1, LARS1, MARS1, MCM5, MOV10, MSH6, PFKP, PIK3R4, QARS1, SMC4, TARS1 |

### STRING and hu.MAP

STRING strongly supports a multisynthetase subnetwork involving EPRS1, IARS1, LARS1, MARS1, QARS1, TARS1, and HARS1. The same biology appears in the supplementary STRING enrichments for aminoacyl-tRNA biosynthesis and ligase activity (6 supplementary STRING terms; within-query FDR 0.00094–0.0125). STRING also supports DDX6-MOV10-EIF4G1 RNA and translation regulation, MCM5-MSH6-POLD1 DNA replication and repair, and NCAPD2-NCAPG-SMC4 condensin relationships. These STRING enrichments are supplementary and do not replace the globally corrected GO/KEGG evidence. hu.MAP independently places the synthetase genes in recurring multisynthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1) and places NCAPD2, NCAPG, and SMC4 in condensin-related complexes (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_14663.1). Other hu.MAP complexes connect MSH6 with NUP93 and ATXN10 and CAD (hu.MAP huMAP3_09042.1) (hu.MAP huMAP3_10665.1). Thus, much of the module reflects established molecular assemblies and neighboring cellular programs rather than one wholly unexplained complex.

**STRING interactions (score >= 0.7)**: 31 of 820 gene pairs: DDX6–EIF4G1 (0.857); DDX6–MOV10 (0.746); EPRS1–HARS1 (0.837); EPRS1–IARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–MARS1 (0.999); EPRS1–QARS1 (0.999); EPRS1–TARS1 (0.928); HARS1–IARS1 (0.849); HARS1–LARS1 (0.844); HARS1–MARS1 (0.878); HARS1–QARS1 (0.835); HARS1–TARS1 (0.865); IARS1–LARS1 (0.999); IARS1–MARS1 (0.999); IARS1–QARS1 (0.999); IARS1–TARS1 (0.913); LARS1–MARS1 (0.999); LARS1–QARS1 (0.999); LARS1–TARS1 (0.98); MARS1–QARS1 (0.999); MARS1–TARS1 (0.881); MCM5–MSH6 (0.749); MCM5–NCAPD2 (0.736); MCM5–POLD1 (0.969); MCM5–SMC4 (0.785); MSH6–POLD1 (0.995); NCAPD2–NCAPG (0.999); NCAPD2–SMC4 (0.999); NCAPG–SMC4 (0.999); QARS1–TARS1 (0.807)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Catalytic activity, acting on a nucleic acid (FDR = 6.42e-05, 15 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 0.00094, 7 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 0.001, 7 genes); Function aminoacyl-tRNA ligase activity (FDR = 0.0015, 7 genes); Function Catalytic activity, acting on RNA (FDR = 0.0015, 11 genes); Function Catalytic activity, acting on a tRNA (FDR = 0.0015, 8 genes); RCTM Cytosolic tRNA aminoacylation (FDR = 0.0021, 7 genes); NetworkNeighborAL tRNA Aminoacylation (FDR = 0.0023, 7 genes); Keyword Protein biosynthesis (FDR = 0.0045, 8 genes); Function ATP binding (FDR = 0.0099, 19 genes); Component Cytosol (FDR = 0.0125, 35 genes); Component aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.0125, 5 genes); Keyword ATP-binding (FDR = 0.0137, 18 genes); Keyword Ligase (FDR = 0.0137, 8 genes); Keyword Phosphoprotein (FDR = 0.0137, 39 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, TARS1, IARS1, QARS1, MARS1, LARS1; 6/14); huMAP3_13688.1 (EPRS1, TARS1, IARS1, QARS1, MARS1, LARS1; 6/14); huMAP3_03084.1 (NCAPD2, NCAPG, SMC4; 3/8); huMAP3_14385.1 (NCAPD2, NCAPG, SMC4; 3/9); huMAP3_09855.1 (NCAPD2, NCAPG, SMC4; 3/10); huMAP3_11457.1 (NCAPD2, NCAPG, SMC4; 3/10); huMAP3_14663.1 (NCAPD2, NCAPG, SMC4; 3/14); huMAP3_09042.1 (MSH6, NUP93, ATXN10; 3/26); huMAP3_10665.1 (CAD, MSH6; 2/42)

### Novelty

The biochemical functions represented here are established: aminoacyl-tRNA synthetase complexes, RNA surveillance, translation control, DNA replication and repair, and condensin are already known systems. The potentially novel observation is their coordinated co-abundance as one conserved module across cell line and cervix_uterine. The fact sheet does not provide an external matched-tissue comparison, perturbation experiment, or prior co-abundance benchmark sufficient to establish that this module-level organization is new. Therefore, this is best described as a biologically coherent cross-context association with potentially novel organization, not as a newly discovered molecular complex or pathway. Absence of an individual relationship from STRING or hu.MAP would not by itself prove novelty.

**Hypothesis.** Hypothesis: a shared biosynthetically active or proliferative cell state coordinates amino acid charging, translation initiation and quality control, RNA processing, nucleotide production, DNA replication and repair, and chromosome organization. The synthetase core may provide translational capacity and fidelity; DDX6, MOV10, EIF4G1, and NEMF may regulate RNA fate and stalled-ribosome quality control; CAD and ACLY may support nucleotide and acetyl-CoA supply; and MCM5, POLD1, MSH6, NCAPD2, NCAPG, and SMC4 may support genome duplication and segregation. This could represent coordinated cellular resource allocation rather than direct physical interaction among every module member. It is a testable hypothesis, not a demonstrated causal mechanism.

### Important genes

#### EPRS1

- **Related proteins** (co-abundance neighbors): NEMF (0.87), LARS1 (0.85), NAA15 (0.84), CLUH (0.82), MCM5 (0.81), MSH6 (0.80); STRING partners: HARS1 (0.837), IARS1 (0.999), LARS1 (0.999), MARS1 (0.999), QARS1 (0.999), TARS1 (0.928)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is a central bridge in the synthetase core, has strong links to other module synthetases in STRING, and occurs in both hu.MAP multisynthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). It appears across the primary translation, tRNA, RNA, and ATP-related terms (15 globally significant GO/KEGG terms, q_global 0.000402–0.0495; see the table). Its established function is glutamyl- and prolyl-tRNA charging, and it has disease associations involving hypomyelinating leukodystrophy and developmental phenotypes.
- **Conclusion**: Established: EPRS1 is a strong molecular anchor for the aminoacyl-tRNA and translation interpretation. Hypothesis: EPRS1 abundance may report translational capacity in the shared state, but the data do not show that EPRS1 controls the whole module.

#### LARS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.90), NAA15 (0.85), EPRS1 (0.85), ACLY (0.83), CAD (0.82), SEC24A (0.81), DYNC1H1 (0.81), NCAPG (0.80); STRING partners: EPRS1 (0.999), HARS1 (0.844), IARS1 (0.999), MARS1 (0.999), QARS1 (0.999), TARS1 (0.98)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: leucyl-tRNA synthetase 1. This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals w…
- **Diseases (Open Targets)**: infantile liver failure syndrome 1 (0.670); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.510); Global developmental delay (0.119); sensorineural hearing loss disorder (0.119); Generalized-onset seizure (0.118)
- **Europe PMC papers**: 267
- **Why important**: LARS1 has strong module connectivity, belongs to both hu.MAP multisynthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), and is strongly connected to the synthetase group in STRING. It contributes to the primary aminoacylation, translation, RNA, and ATP-related evidence (15 globally significant GO/KEGG terms, q_global 0.000402–0.0495; see the table). Its established function is cytosolic leucine-tRNA charging, with disease associations including infantile liver failure and developmental or neurological phenotypes.
- **Conclusion**: Established: LARS1 is a core leucine-tRNA synthetase linking amino acid charging to translational fidelity. Hypothesis: it may couple nutrient-sensitive translation to the broader biosynthetic state, but that coupling is not demonstrated by co-abundance alone.

#### DDX6

- **Related proteins** (co-abundance neighbors): ELAC2 (0.84), VPS45 (0.84), IARS1 (0.81), ACLY (0.81), MOV10 (0.80); STRING partners: EIF4G1 (0.857), MOV10 (0.746)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytoplasmic bodies; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 6. This gene encodes a member of the DEAD box protein family. The protein is an RNA helicase found in P-bodies and stress granules, and functions in translation suppression and mRNA degradation. It is required for microRNA-induced gene silencing. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: intellectual developmental disorder with impaired language and dysmorphic facies (0.650); Intellectual disability (0.555); neurodegenerative disease (0.459); lung carcinoma (0.371); Global developmental delay (0.371)
- **Europe PMC papers**: 3002
- **Why important**: DDX6 connects RNA-processing and translation-related neighbors, including ELAC2, MOV10, and EIF4G1, and has strong STRING relationships with EIF4G1 and MOV10. It contributes to primary RNA-catalysis and translation evidence (5 globally significant GO/KEGG terms, q_global 0.000402–0.0495; see the table). Its established function is an RNA helicase involved in P-bodies, stress granules, mRNA decay, translation suppression, and microRNA-mediated silencing. It has substantial literature and disease associations involving neurodevelopment and neurodegeneration.
- **Conclusion**: Established: DDX6 provides a post-transcriptional regulatory arm distinct from the synthetase complex. Hypothesis: DDX6 may balance increased translational demand with selective mRNA repression and RNA quality control.

#### MCM5

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.87), NAA15 (0.85), NEMF (0.83), EPRS1 (0.81), NCAPG (0.80); STRING partners: MSH6 (0.749), NCAPD2 (0.736), POLD1 (0.969), SMC4 (0.785)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: minichromosome maintenance complex component 5. The protein encoded by this gene is structurally very similar to the CDC46 protein from S. cerevisiae, a protein involved in the initiation of DNA replication. The encoded protein is a member of the MCM family of chromatin-binding proteins and can interact with at least two other members of this family. The encoded protein is upregulated in the transition from the G0 to G1/S phase of the cell cycl…
- **Diseases (Open Targets)**: Meier-Gorlin syndrome (0.563); neurodegenerative disease (0.397); lysosomal storage disease (0.362); kidney transplant (0.198); diabetic ketoacidosis (0.129)
- **Europe PMC papers**: 4143
- **Why important**: MCM5 links the module to DNA replication and cell-cycle activity and is connected in STRING with MSH6, POLD1, NCAPD2, and SMC4. HPA associates it with bone marrow and several progenitor populations. It contributes to nucleic-acid catalytic and ATP-binding evidence (GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.000402) (GO:MF nucleic acid binding; q_global = 0.0299) (GO:MF ATP binding; q_global = 0.0495), while its established function is replication initiation and regulation of DNA replication. It has a well-established disease association with Meier-Gorlin syndrome.
- **Conclusion**: Established: MCM5 supports a proliferative and genome-maintenance interpretation in addition to translation. Hypothesis: its co-abundance with the synthetase core may mark coordinated preparation for cell division, but it is not shown to regulate aminoacylation.

#### NEMF

- **Related proteins** (co-abundance neighbors): EPRS1 (0.87), SMC4 (0.87), MCM5 (0.83), NCAPD2 (0.82), DYNC1H1 (0.82), TARS1 (0.81), POLD1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nuclear export mediator factor. This gene encodes a component of the ribosome quality control complex. The encoded protein facilitates the recognition and ubiquitination of stalled 60S subunits by the ubiquitin ligase listerin. A similar protein in fly functions as a tumor suppressor. [provided by RefSeq, Jul 2016].
- **Diseases (Open Targets)**: intellectual developmental disorder with speech delay and axonal peripheral neuropathy (0.708); hereditary disease (0.471); Global developmental delay (0.374); Intellectual disability (0.371); cerebellar ataxia (0.370)
- **Europe PMC papers**: 2061
- **Why important**: NEMF has strong module connectivity and links the synthetase neighborhood to chromosome-associated genes and DYNC1H1. It contributes to translation, protein biosynthesis, and nucleic-acid-binding evidence (GO:BP translation; q_global = 0.00667) (GO:BP protein biosynthetic process; q_global = 0.00667) (GO:MF nucleic acid binding; q_global = 0.0299). Its established function is in ribosome quality control, including recognition and ubiquitination of stalled translation products. Its disease associations include developmental delay, intellectual disability, and axonal neuropathy.
- **Conclusion**: Established: NEMF supplies a ribosome-quality-control component connecting protein synthesis with proteostasis. Hypothesis: NEMF may help explain coordinated variation of translation and genome-maintenance genes by supporting cells under high biosynthetic and proliferative demand.

## Module 2

**Tissue pair**: cell line and cervix_uterine  
**Genes (29)**: ACBD5, ALB, ASRGL1, CALML5, CTSV, CFH, CSTA, DCP1A, ENDOD1, FABP5, GFUS, GSTM1, H2AX, HSPA2, EIF4A2, KIAA0825, KRT19, KRT72, KRT78, CKMT1A, LYZ, MACO1, MYADM, SDR16C5, TIMP1, TUFT1, TWF1, VASP, ZNF462

### Function

The module is most consistent with an epithelial differentiation and barrier-associated program, with contributions from keratin structure, epidermal lipid handling, calcium-linked differentiation, cysteine-protease regulation, and extracellular protease control. This interpretation is supported by the tissue and single-cell annotations for CALML5, KRT78, KRT72, KRT19, FABP5, CSTA, CTSV, and related genes, together with the partial hu.MAP epithelial complexes (hu.MAP huMAP3_09929.1) and (hu.MAP huMAP3_09125.1). The network is sparse and appears organized around CALML5, with a separate keratin-associated branch involving KRT78 and a protease-regulatory branch involving CSTA and CTSV. However, no GO or KEGG term passed global correction, so the pathway interpretation is annotation-led rather than enrichment-proven. The absence of a globally significant term does not invalidate the module.

**Cell composition.** This is not primarily a plasma or secreted-protein module, although plasma-associated genes are present. ALB and CFH are liver-enriched and secreted to blood, and LYZ and TIMP1 are also secreted or extracellularly associated. Thus, blood, plasma carryover, or tissue-fluid exposure could contribute to part of the signal, especially in cervix samples. HPA evidence nevertheless points more strongly toward epithelial and keratinizing cell states: many genes are enhanced in esophageal apical or suprabasal cells, suprabasal keratinocytes, cervix, vagina, or skin. Several genes are not detected in immune cells, while a smaller subset shows myeloid or neutrophil association. The module therefore appears to reflect epithelial cell composition and differentiation, with possible admixture from circulating proteins and limited immune-cell content, rather than a predominantly blood-cell module or a generic housekeeping program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING contains only a small set of high-confidence relationships: ALB with CALML5 and TIMP1, CSTA with CTSV, and CTSV with TIMP1. These relationships support a protease and extracellular-regulation component, but STRING reports no functional enrichment for the module. hu.MAP provides stronger structural context. (hu.MAP huMAP3_09929.1) links CTSV, CSTA, FABP5, and CALML5 within an epithelial-associated complex, while (hu.MAP huMAP3_09125.1) again links CTSV, CSTA, and CALML5. (hu.MAP huMAP3_15040.1) and (hu.MAP huMAP3_10678.1) place ALB and CFH in complexes dominated by circulating plasma and complement-related proteins. Because only a subset of members from each large complex occurs in this module, these results support shared molecular context rather than demonstrating that the complete complexes are assembled in the sampled tissues. The combination of a strong CALML5-centered co-abundance structure, limited STRING support, and partial hu.MAP overlap suggests coordinated abundance without implying direct physical interaction for every module edge.

**STRING interactions (score >= 0.7)**: 4 of 406 gene pairs: ALB–CALML5 (0.794); ALB–TIMP1 (0.737); CSTA–CTSV (0.96); CTSV–TIMP1 (0.705)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09929.1 (CTSV, CSTA, FABP5, CALML5; 4/75); huMAP3_09125.1 (CTSV, CSTA, CALML5; 3/53); huMAP3_15040.1 (ALB, CFH; 2/64); huMAP3_10678.1 (ALB, CFH; 2/71)

### Novelty

The module should not be described as a newly discovered biological complex or pathway. Its component signals are largely interpretable through established epithelial differentiation, keratin, lipid-binding, cysteine-protease, complement, and plasma-protein biology. Several relationships are already represented by STRING or hu.MAP, particularly the CSTA–CTSV relationship and the epithelial complexes (hu.MAP huMAP3_09929.1) and (hu.MAP huMAP3_09125.1). The potentially novel result is the reproducible co-abundance pattern shared by cell line and cervix_uterine, especially the way CALML5, keratin-associated genes, protease regulators, and blood-associated proteins co-vary. That claim remains provisional because the module has no globally significant GO/KEGG enrichment, STRING gives no module-level enrichment, and tissue composition or plasma carryover could generate part of the pattern. Absence from interaction databases would not by itself establish novelty.

**Hypothesis.** Hypothesis: the shared module reflects a conserved epithelial differentiation state in which CALML5-linked calcium sensing or calcium-dependent conformational change accompanies keratin cytoskeletal remodeling, epidermal lipid handling, and regulation of cysteine-protease activity. CSTA may restrain proteolysis while CTSV contributes lysosomal or extracellular protein turnover, and FABP5 may connect differentiation with lipid signaling. ALB, CFH, LYZ, and TIMP1 may represent extracellular exposure, plasma contribution, or injury-associated remodeling rather than the core intracellular program. This hypothesis predicts that the module will be strongest in differentiated epithelial cells and will weaken after controlling for plasma content, immune admixture, and epithelial cell proportion.

### Important genes

#### CALML5

- **Related proteins** (co-abundance neighbors): MACO1 (0.94), DCP1A (0.93), GSTM1 (0.89), ASRGL1 (0.89), LYZ (0.87), EIF4A2 (0.87), ALB (0.87), CFH (0.87), FABP5 (0.86), MYADM (0.85), CSTA (0.84), TIMP1 (0.84), GFUS (0.83), HSPA2 (0.81), VASP (0.81), TUFT1 (0.81); STRING partners: ALB (0.794)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09929.1, huMAP3_09125.1
- **Function (MyGene.info)**: calmodulin like 5. This gene encodes a novel calcium binding protein expressed in the epidermis and related to the calmodulin family of calcium binding proteins. Functional studies with recombinant protein demonstrate it does bind calcium and undergoes a conformational change when it does so. Abundant expression is detected only in reconstructed epidermis and is restricted to differentiating keratinocytes. In additi…
- **Diseases (Open Targets)**: alcohol drinking (0.095); Alzheimer disease (0.093); thymic carcinoma (0.074); breast cancer (0.066); breast carcinoma (0.066)
- **Europe PMC papers**: 604
- **Why important**: CALML5 is the central network hub and has the strongest weighted connectivity in the module. HPA places it in skin and in apical or suprabasal epithelial cell states, with protein detected in cervix_uterine. Its annotated calcium binding, epidermal expression, and association with terminal keratinocyte differentiation provide the clearest biological anchor for the module. It also occurs in hu.MAP complexes (hu.MAP huMAP3_09929.1) and (hu.MAP huMAP3_09125.1) and has substantial literature support.
- **Conclusion**: Established evidence supports CALML5 as a marker and possible organizer of differentiated epithelial state. It is reasonable to treat CALML5 as the module's principal abundance-linked anchor. It remains a hypothesis that CALML5 causally coordinates the other module genes; the co-abundance network alone does not establish that mechanism.

#### KRT78

- **Related proteins** (co-abundance neighbors): ACBD5 (0.90), KRT72 (0.89), H2AX (0.87), ENDOD1 (0.87), ASRGL1 (0.85), CKMT1A; CKMT1B (0.82), SDR16C5 (0.81), CTSV (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 78. This gene is a member of the type II keratin gene family and encodes a protein with an intermediate filament domain. Keratins are the major structural proteins in epithelial cells, forming a cytoplasmic network of 10 to 12 nm wide intermediate filaments and creating a scaffold that gives cells the ability to withstand mechanical and non-mechanical stresses. The genes of the type II keratin family …
- **Diseases (Open Targets)**: neurodegenerative disease (0.398); preeclampsia (0.121); prostate carcinoma (0.086); head and neck squamous cell carcinoma (0.079); Abnormality of the liver (0.066)
- **Europe PMC papers**: 306
- **Why important**: KRT78 is a prominent structural node connected to genes associated with epithelial metabolism, nucleic-acid stress, and keratin biology. HPA places it in esophagus and esophageal apical cells, with protein detected in cervix_uterine. Its established role as a type II keratin and its links to keratinization and intermediate-filament organization make it a strong indicator of epithelial differentiation. It has a moderate literature base and no recorded STRING or hu.MAP relationship in this module.
- **Conclusion**: Established evidence supports KRT78 as a structural epithelial differentiation marker shared by the relevant tissue contexts. Its module connectivity may indicate coordinated cytoskeletal state, but a direct physical or regulatory connection to the other module genes is unproven.

#### CSTA

- **Related proteins** (co-abundance neighbors): CALML5 (0.84); STRING partners: CTSV (0.96)
- **HPA**: Tissue enhanced; Group enriched; blood Group enriched; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09929.1, huMAP3_09125.1
- **Function (MyGene.info)**: cystatin A. The cystatin superfamily encompasses proteins that contain multiple cystatin-like sequences. Some of the members are active cysteine protease inhibitors, while others have lost or perhaps never acquired this inhibitory activity. There are three inhibitory families in the superfamily, including the type 1 cystatins (stefins), type 2 cystatins, and kininogens. This gene encodes a stefin that functio…
- **Diseases (Open Targets)**: peeling skin syndrome 4 (0.707); exfoliative ichthyosis (0.640); acral peeling skin syndrome (0.387); Hyperkeratosis (0.372); Palmoplantar hyperkeratosis (0.371)
- **Europe PMC papers**: 1599
- **Why important**: CSTA is a tissue-enhanced cervix and esophagus gene with protein detected in cervix_uterine. It encodes a cysteine-protease inhibitor and is annotated for keratinocyte differentiation, negative regulation of proteolysis, and cell-cell adhesion. It is present in (hu.MAP huMAP3_09929.1) and (hu.MAP huMAP3_09125.1), and STRING gives a particularly strong known relationship with CTSV. Its disease associations include peeling skin and hyperkeratotic disorders, directly relevant to epithelial barrier biology.
- **Conclusion**: Established evidence supports CSTA as a mechanistically relevant link between epithelial differentiation, adhesion, and protease control. The module supports a coordinated CSTA–CTSV protease-regulatory state, although it does not show whether CSTA drives that state or simply marks the same cell population.

#### CTSV

- **Related proteins** (co-abundance neighbors): KRT78 (0.81); STRING partners: CSTA (0.96), TIMP1 (0.705)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location Nucleoli fibrillar center, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09929.1, huMAP3_09125.1
- **Function (MyGene.info)**: cathepsin V. The protein encoded by this gene, a member of the peptidase C1 family, is a lysosomal cysteine proteinase that may play an important role in corneal physiology. This gene is expressed in colorectal and breast carcinomas but not in normal colon, mammary gland, or peritumoral tissues, suggesting a possible role for this gene in tumor processes. Alternatively spliced variants, encoding the same prote…
- **Diseases (Open Targets)**: neurodegenerative disease (0.525); adolescent idiopathic scoliosis (0.146); dyshidrosis (0.130); alopecia universalis congenita (0.110); alopecia - intellectual disability syndrome (0.109)
- **Europe PMC papers**: 646
- **Why important**: CTSV occupies the protease-associated part of the network and is present in (hu.MAP huMAP3_09929.1) and (hu.MAP huMAP3_09125.1). It has known STRING relationships with CSTA and TIMP1. Its annotations include lysosomal cysteine proteolysis, antigen processing, and extracellular-matrix disassembly, while HPA detects it in epithelial and trophoblast-related cell states and in cervix_uterine. These features make it a plausible functional complement to CSTA.
- **Conclusion**: Established evidence supports CTSV as a proteolytic component of the module and strengthens the interpretation of a regulated epithelial remodeling program. Whether CTSV activity is actually altered in the shared module, rather than merely its abundance, remains a hypothesis requiring activity or substrate measurements.

#### CFH

- **Related proteins** (co-abundance neighbors): CALML5 (0.87), ZNF462 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: complement factor H. This gene is a member of the Regulator of Complement Activation (RCA) gene cluster and encodes a protein with twenty short consensus repeat (SCR) domains. This protein is secreted into the bloodstream and has an essential role in the regulation of complement activation, restricting this innate defense mechanism to microbial infections. Mutations in this gene have been associated with hemolytic-ure…
- **Diseases (Open Targets)**: complement factor H deficiency (0.769); age-related macular degeneration (0.750); atypical hemolytic-uremic syndrome (0.729); age related macular degeneration 4 (0.711); Doyne honeycomb retinal dystrophy (0.688)
- **Europe PMC papers**: 9287
- **Why important**: CFH is important because it represents a distinct extracellular and composition-related signal. It is liver-enriched, secreted to blood, associated with complement regulation, and linked to major complement and plasma complexes through (hu.MAP huMAP3_15040.1) and (hu.MAP huMAP3_10678.1). Its module position is peripheral rather than hub-like, but its extensive disease literature includes complement factor H deficiency and retinal vascular disease. HPA also associates it with hepatic and stromal cell states.
- **Conclusion**: Established evidence supports CFH as a complement-regulatory plasma protein and a likely indicator of extracellular or tissue-fluid contribution. It should not be interpreted as proof that complement activation is the core function of the module. Its co-abundance with epithelial genes may reflect local extracellular remodeling, plasma exposure, or sample composition; distinguishing these possibilities is a key validation step.

## Module 3

**Tissue pair**: cell line and cervix_uterine  
**Genes (5)**: ACSS2, PRKCD, MYO1B, PYGL, ATP6V1H

### Function

The module is most consistent with a metabolic and cellular-trafficking program rather than a narrowly defined canonical pathway. The primary enrichment evidence is AMP binding (GO:MF AMP binding; q_global = 0.0311), supported by ACSS2 and PYGL. ACSS2 is an acetate-activating enzyme that generates acetyl-CoA for lipid synthesis and energy generation, while PYGL mobilizes liver glycogen to release glucose-1-phosphate. The remaining genes broaden the interpretation: ATP6V1H supports V-ATPase-dependent organelle acidification, PRKCD participates in phosphorylation, stress responses and apoptosis, and MYO1B supports actin organization, endocytosis and post-Golgi vesicle transport. Because only the AMP-binding term passed global correction and there is no STRING functional enrichment, the metabolic interpretation is supported but should not be expanded into a claim of a fully established biochemical pathway. The sparse co-abundance structure may represent coordinated activity across metabolism, intracellular trafficking and signaling rather than a physical protein complex.

**Cell composition.** This is not a secreted-protein module, because none of the member genes is annotated as secreted. The HPA profile is heterogeneous: several genes are tissue enhanced, especially in liver or skeletal muscle, while others have low tissue specificity. Cell-type annotations include adipocytes, hepatocyte-related or epithelial populations, platelets, neutrophils and other specialized cells. The blood-related signal is mixed rather than uniformly blood-cell enriched: ACSS2, PYGL and PRKCD have some immune or blood-cell associations, whereas MYO1B is not detected in immune cells and ATP6V1H has low immune-cell specificity. Thus, the shared module could partly reflect common cell-type composition or metabolic state in the samples, rather than a cervix-specific program. Detection of most member proteins in cervix tissue supports tissue presence, but the lack of matching HPA protein data for the cell-line context limits direct comparison between the two tissues.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF AMP binding | 0.0311 | ACSS2, PYGL |

### STRING and hu.MAP

The co-abundance network places ACSS2 as the main connector, linking PYGL, ATP6V1H and PRKCD, while PYGL also links to MYO1B. However, none of the possible gene pairs reaches the supplied high-confidence STRING interaction threshold, and there is no STRING functional enrichment. No hu.MAP complex contains multiple module members. These results indicate that the observed relationships are not already supported as a known high-confidence physical interaction network or multiprotein complex. The network may instead capture coordinated expression, indirect regulation, shared cell composition or common physiological state. Known biology still provides plausible functional links: ACSS2 and PYGL are metabolic enzymes, ATP6V1H concerns organelle acidification, MYO1B concerns membrane trafficking, and PRKCD concerns signal transduction and stress responses.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module cannot be established as a new biological discovery from the supplied evidence alone. The individual genes and their functions are well characterized, and the AMP-binding association is supported by an established functional annotation (GO:MF AMP binding; q_global = 0.0311). The potentially novel aspect is the cross-context co-abundance of this particular combination in cell line and cervix_uterine, especially because it lacks a corresponding high-confidence STRING network or hu.MAP complex. Nevertheless, absence from STRING or hu.MAP does not prove novelty: the pattern could arise from indirect regulation, cell-type composition, technical covariance or a context-specific physiological state. The appropriate conclusion is that this is a potentially interesting association requiring independent replication and targeted mechanistic testing, not a demonstrated new pathway.

**Hypothesis.** Mechanistic hypothesis: the module may reflect a coordinated state in which acetate utilization and glycogen-derived carbohydrate availability are coupled to membrane and organelle remodeling. In this model, ACSS2 and PYGL represent metabolic inputs, ATP6V1H supports the acidic organelle environment needed for trafficking and degradation, MYO1B organizes actin-linked membrane transport, and PRKCD transduces stress or lipid-dependent signals that can influence survival and apoptosis. This is a hypothesis, not an established mechanism for the module. It predicts that the co-abundance pattern should track metabolic flux, organelle acidification, vesicle trafficking or stress-response measurements, and that perturbing ACSS2 or PYGL may alter the trafficking or signaling features associated with the other module members.

### Important genes

#### ACSS2

- **Related proteins** (co-abundance neighbors): PYGL (0.83), ATP6V1H (0.81), PRKCD (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase short chain family member 2. This gene encodes a cytosolic enzyme that catalyzes the activation of acetate for use in lipid synthesis and energy generation. The protein acts as a monomer and produces acetyl-CoA from acetate in a reaction that requires ATP. Expression of this gene is regulated by sterol regulatory element-binding proteins, transcription factors that activate genes required for the synthesis of cholesterol and …
- **Diseases (Open Targets)**: neurodegenerative disease (0.371); orofacial cleft (0.333); autoimmune disorder of central nervous system (0.261); coronary artery disorder (0.152); delusional disorder (0.142)
- **Europe PMC papers**: 2948
- **Why important**: ACSS2 is the central network connector and is one of the genes supporting the only globally corrected functional term, AMP binding (GO:MF AMP binding; q_global = 0.0311). Its established role is to activate acetate for acetyl-CoA production, linking carbon utilization to lipid synthesis and energy generation. It also has broad disease and literature support, including associations with neurodegenerative, autoimmune and coronary disorders, and substantial literature volume. Its tissue and cell annotations suggest metabolic relevance across adipocyte, muscle-associated and epithelial contexts.
- **Conclusion**: Established evidence supports ACSS2 as the strongest candidate metabolic anchor of the module. It is plausible that ACSS2 helps explain the shared co-abundance pattern, but its role as an upstream driver of the other genes remains a hypothesis because no direct STRING or hu.MAP relationship is supplied.

#### PYGL

- **Related proteins** (co-abundance neighbors): ACSS2 (0.83), MYO1B (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycogen phosphorylase L. This gene encodes a homodimeric protein that catalyses the cleavage of alpha-1,4-glucosidic bonds to release glucose-1-phosphate from liver glycogen stores. This protein switches from inactive phosphorylase B to active phosphorylase A by phosphorylation of serine residue 15. Activity of this enzyme is further regulated by multiple allosteric effectors and hormonal controls. Humans have three glyco…
- **Diseases (Open Targets)**: glycogen storage disease VI (0.821); disorder of glycogen metabolism (0.647); glycogen storage disease XV (0.596); neurodegenerative disease (0.370); Cholecystitis (0.357)
- **Europe PMC papers**: 1838
- **Why important**: PYGL is the other member of the globally corrected AMP-binding overlap (GO:MF AMP binding; q_global = 0.0311) and is a key glycogen-mobilizing enzyme. It occupies a bridging position between ACSS2 and MYO1B in the co-abundance network, connecting carbohydrate metabolism with a membrane-trafficking gene. Its liver enhancement and associations with glycogen storage disease and broader glycogen-metabolism disorders make it biologically informative for interpreting the module.
- **Conclusion**: Established evidence supports PYGL as a carbohydrate-metabolism component and an important network bridge. A coupling between glycogen mobilization and membrane trafficking is a reasonable hypothesis, but it is not demonstrated by the supplied interaction resources.

#### ATP6V1H

- **Related proteins** (co-abundance neighbors): ACSS2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase H+ transporting V1 subunit H. This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of intracellular organelles. V-ATPase-dependent organelle acidification is necessary for multiple processes including protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. The encoded protein is the regulatory H subunit of the…
- **Diseases (Open Targets)**: HIV infectious disease (0.551); neurodegenerative disease (0.539); tuberculosis (0.371); frozen shoulder (0.271); gastrointestinal disease (0.262)
- **Europe PMC papers**: 869
- **Why important**: ATP6V1H contributes a distinct organelle-physiology dimension to the module. It is a regulatory subunit of V-ATPase, which supports intracellular, endosomal and lysosomal acidification, endocytosis and macroautophagy. Its connection to ACSS2 makes it relevant to the proposed link between cellular metabolism and organelle handling, while its endometrial-glandular-cell annotation is pertinent to reproductive-tract tissue context.
- **Conclusion**: Established evidence supports ATP6V1H as a component of intracellular acidification and trafficking machinery. Its participation in a shared metabolic-trafficking state is plausible, but the module data do not establish direct regulation by ACSS2 or a causal role in the co-abundance pattern.

#### PRKCD

- **Related proteins** (co-abundance neighbors): ACSS2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase C delta. The protein encoded by this gene is a member of the protein kinase C family of serine- and threonine-specific protein kinases. The encoded protein is activated by diacylglycerol and is both a tumor suppressor and a positive regulator of cell cycle progression. Also, this protein can positively or negatively regulate apoptosis. Defects in this gene are a cause of autoimmune lymphoproliferative synd…
- **Diseases (Open Targets)**: autoimmune lymphoproliferative syndrome (0.685); acute myeloid leukemia (0.556); mast cell leukemia (0.475); systemic mastocytosis (0.471); mastocytosis (0.464)
- **Europe PMC papers**: 3335
- **Why important**: PRKCD adds a signaling and stress-response component and is connected directly to ACSS2 in the co-abundance network. Its established functions include protein phosphorylation, apoptosis, stress responses and DNA-damage signaling. It has substantial literature support and disease associations involving autoimmune lymphoproliferative syndrome, myeloid leukemia and mast-cell disorders. Its annotations in neutrophils and platelets also make it relevant when considering shared cellular composition.
- **Conclusion**: Established evidence supports PRKCD as a signaling regulator capable of connecting metabolic state with stress or survival responses. Its inclusion may indicate a stress-responsive context, but whether PRKCD mechanistically links the module members is unresolved.

#### MYO1B

- **Related proteins** (co-abundance neighbors): PYGL (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin IB. Enables ATP binding activity; actin filament binding activity; and microfilament motor activity. Involved in actin filament organization and post-Golgi vesicle-mediated transport. Located in several cellular components, including actin filament; endosome; and perinuclear region of cytoplasm. Colocalizes with trans-Golgi network membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: colorectal cancer (0.336); hair color (0.322); asthma (0.305); rectosigmoid junction neoplasm (0.269); cervical carcinoma (0.200)
- **Europe PMC papers**: 974
- **Why important**: MYO1B is the module's membrane-cytoskeletal and vesicle-transport representative. It supports actin filament binding, microfilament motor activity, endocytosis and post-Golgi vesicle transport, and it links to PYGL in the network. Its enrichment in liver and epithelial or vascular-associated cell types, together with an association with cervical carcinoma, gives it contextual relevance to the tissue pair despite a more limited literature volume than ACSS2 or PRKCD.
- **Conclusion**: Established evidence supports MYO1B as a membrane-trafficking and actin-organization factor. Its network connection to PYGL is compatible with a metabolism–trafficking relationship, but that relationship remains a co-abundance hypothesis rather than a demonstrated molecular interaction.

## Module 4

**Tissue pair**: cell line and cervix_uterine  
**Genes (22)**: ACSL3, CHD4, COPB1, DDX21, DDX56, DHX9, FASN, GTPBP4, MYBBP1A, RNMT, NOP56, URB1, NUP155, NUP160, PLRG1, NUP210, RAD50, PDCD11, SEC23A, SEC23B, VARS1, SNRNP200

### Function

The module is best interpreted as a conserved nuclear RNA-processing and ribosome-biogenesis program. The strongest primary evidence is the global enrichment for ribonucleoprotein complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.00115), nuclear protein-containing complexes (GO:CC nuclear protein-containing complex; q_global = 0.00134), RNA processing (GO:BP RNA processing; q_global = 0.00321), ribosome biogenesis (GO:BP ribosome biogenesis; q_global = 0.00624), and rRNA processing (GO:BP rRNA processing; q_global = 0.0073). The nucleolar localization signal (GO:CC nucleolus; q_global = 0.0402) and the rRNA metabolic-process term (GO:BP rRNA metabolic process; q_global = 0.0183) reinforce a nucleolus-centered interpretation. DEAD-box and related helicase activity (GO:MF helicase activity; q_global = 0.0133) and nucleic-acid conformation isomerase activity (GO:MF nucleic acid conformation isomerase activity; q_global = 0.0148) suggest active RNA remodeling. The module also contains nuclear-pore, spliceosomal, chromatin, DNA-repair, RNA-capping, translation-related, and vesicle-trafficking components, indicating coordination between RNA maturation, nucleocytoplasmic transport, and general nuclear gene expression. The osteoblast differentiation and ossification terms (GO:BP osteoblast differentiation; q_global = 0.0073) (GO:BP ossification; q_global = 0.0419) are globally significant but are less specific than the coherent RNA and nucleolar signal, so they should not be taken as proof of an osteoblast identity.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It is also not blood-cell enriched; most genes have low immune-cell specificity, and no blood-cell enrichment pattern is reported. Most genes have low tissue specificity, with protein detection in cervix_uterine for many members. The composition is therefore consistent with broadly expressed, housekeeping-like nuclear machinery rather than a tissue-restricted or blood-derived signature. The shared signal between cell line and cervix_uterine may consequently reflect a conserved cellular program, cellular proliferation or biosynthetic state, or shared nuclear components rather than shared tissue origin. A few genes show specialized HPA patterns, including NUP155 in testis, FASN in adipose tissue, breast and liver, NUP210 in bone marrow and lymphoid tissue, and several genes in neural or reproductive cell types, but these do not define the module as a whole.

**GO/KEGG enrichment**: 12 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP ribonucleoprotein complex biogenesis | 0.00115 | DDX21, DDX56, DHX9, GTPBP4, MYBBP1A, NOP56, PDCD11, SNRNP200, URB1 |
| GO:CC nuclear protein-containing complex | 0.00134 | CHD4, DDX21, MYBBP1A, NOP56, NUP155, NUP160, NUP210, PDCD11, PLRG1, RAD50, RNMT, SNRNP200 |
| GO:BP RNA processing | 0.00321 | DDX21, DDX56, DHX9, GTPBP4, NOP56, NUP155, PDCD11, PLRG1, RNMT, SNRNP200, URB1 |
| GO:BP ribosome biogenesis | 0.00624 | DDX21, DDX56, GTPBP4, MYBBP1A, NOP56, PDCD11, URB1 |
| GO:BP osteoblast differentiation | 0.0073 | DDX21, DHX9, FASN, GTPBP4, MYBBP1A, SNRNP200 |
| GO:BP rRNA processing | 0.0073 | DDX21, DDX56, GTPBP4, NOP56, PDCD11, URB1 |
| GO:MF helicase activity | 0.0133 | CHD4, DDX21, DDX56, DHX9, RAD50, SNRNP200 |
| GO:MF nucleic acid conformation isomerase activity | 0.0148 | CHD4, DDX21, DDX56, DHX9, RAD50, SNRNP200 |
| GO:BP rRNA metabolic process | 0.0183 | DDX21, DDX56, GTPBP4, NOP56, PDCD11, URB1 |
| GO:BP nucleobase-containing compound biosynthetic process | 0.0218 | ACSL3, CHD4, DDX21, DDX56, DHX9, FASN, GTPBP4, MYBBP1A, NOP56, NUP155, PDCD11, PLRG1, RAD50, RNMT, SNRNP200, URB1 |
| GO:CC nucleolus | 0.0402 | DDX21, DDX56, DHX9, GTPBP4, MYBBP1A, NOP56, PDCD11, PLRG1, RNMT, URB1 |
| GO:BP ossification | 0.0419 | DDX21, DHX9, FASN, GTPBP4, MYBBP1A, SNRNP200 |

### STRING and hu.MAP

STRING supports a dense, biologically coherent RNA and nucleolar subnetwork. Strong relationships connect DDX21, DDX56, GTPBP4, NOP56, PDCD11 and MYBBP1A, while DHX9 and SNRNP200 connect RNA helicase and spliceosomal functions. NUP155, NUP160 and NUP210 form a nuclear-pore subnetwork, SEC23A and SEC23B form a COPII pair, and ACSL3 and FASN form a lipid-metabolism pair. The STRING functional results (15 supplementary STRING terms; within-query FDR 0.00075–0.02) concordantly support nucleolar localization, RNA processing, ribosome biogenesis, rRNA processing and helicase-related biology, but they are supplementary and are not global multiple-testing evidence. hu.MAP independently identifies SEC23A-SEC23B complexes (hu.MAP huMAP3_00065.1) (hu.MAP huMAP3_00707.1) (hu.MAP huMAP3_07775.1) (hu.MAP huMAP3_06453.1) (hu.MAP huMAP3_09282.1) (hu.MAP huMAP3_11128.1) (hu.MAP huMAP3_11237.1) (hu.MAP huMAP3_09710.1) (hu.MAP huMAP3_13535.1) (hu.MAP huMAP3_12394.1), nuclear-pore complexes involving NUP155, NUP160 and NUP210 (hu.MAP huMAP3_07645.1) (hu.MAP huMAP3_09710.1) (hu.MAP huMAP3_12581.1), and spliceosomal complexes containing PLRG1 and SNRNP200 (hu.MAP huMAP3_06726.1) (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1). These resources therefore show that several module edges correspond to known physical or functional relationships, while other co-abundance links may represent indirect coordination or shared cellular state.

**STRING interactions (score >= 0.7)**: 23 of 231 gene pairs: ACSL3–FASN (0.964); DDX21–DHX9 (0.908); DDX21–GTPBP4 (0.813); DDX21–MYBBP1A (0.963); DDX21–NOP56 (0.811); DDX56–DHX9 (0.719); DDX56–GTPBP4 (0.978); DDX56–MYBBP1A (0.838); DDX56–NOP56 (0.884); DDX56–PDCD11 (0.853); DHX9–SNRNP200 (0.784); GTPBP4–NOP56 (0.941); GTPBP4–PDCD11 (0.928); MYBBP1A–NOP56 (0.737); MYBBP1A–PDCD11 (0.949); NOP56–PDCD11 (0.997); NUP155–NUP160 (0.994); NUP155–NUP210 (0.991); NUP160–NUP210 (0.983); PDCD11–URB1 (0.973); PDCD11–VARS1 (0.805); PLRG1–SNRNP200 (0.996); SEC23A–SEC23B (0.949)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Nucleolus (FDR = 0.00075, 10 genes); SMART DEAD-like helicases superfamily (FDR = 0.0037, 5 genes); SMART Helicase superfamily c-terminal domain (FDR = 0.0037, 5 genes); Process Osteoblast differentiation (FDR = 0.0038, 6 genes); Process RNA processing (FDR = 0.0038, 11 genes); Process Ribonucleoprotein complex biogenesis (FDR = 0.0038, 9 genes); Process Ribosome biogenesis (FDR = 0.0075, 7 genes); RCTM Metabolism of RNA (FDR = 0.009, 10 genes); Process rRNA processing (FDR = 0.0106, 6 genes); Process RNA metabolic process (FDR = 0.0113, 12 genes); Process ncRNA processing (FDR = 0.0156, 7 genes); Process ncRNA metabolic process (FDR = 0.0156, 8 genes); Process Gene expression (FDR = 0.0174, 13 genes); Process Nucleic acid metabolic process (FDR = 0.0187, 13 genes); NetworkNeighborAL rRNA processing, and RNA helicase activity (FDR = 0.02, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00065.1 (SEC23A, SEC23B; 2/4); huMAP3_00707.1 (SEC23A, SEC23B; 2/4); huMAP3_07775.1 (SEC23A, SEC23B; 2/5); huMAP3_06453.1 (SEC23A, SEC23B; 2/6); huMAP3_09282.1 (SEC23A, SEC23B; 2/6); huMAP3_07645.1 (NUP155, NUP210; 2/7); huMAP3_11128.1 (SEC23A, SEC23B; 2/8); huMAP3_11237.1 (SEC23A, SEC23B; 2/12); huMAP3_09710.1 (NUP160, NUP210; 2/13); huMAP3_13535.1 (SEC23A, SEC23B; 2/14); huMAP3_06726.1 (PLRG1, SNRNP200; 2/37); huMAP3_08501.1 (PLRG1, SNRNP200; 2/47); huMAP3_09504.1 (PLRG1, SNRNP200; 2/51); huMAP3_12581.1 (NUP155, NUP160; 2/58); huMAP3_09945.1 (PLRG1, SNRNP200; 2/61); huMAP3_12394.1 (SEC23A, SEC23B; 2/98)

### Novelty

The module should not be presented as a newly discovered molecular pathway. Its central biology—nucleolar rRNA maturation, ribosome biogenesis, RNA helicase activity, splicing, nuclear transport and COPII trafficking—is already well established, and many relationships are supported by STRING or hu.MAP. The potentially novel observation is the reproducible co-abundance configuration shared by cell line and cervix_uterine, especially the way the nucleolar, spliceosomal, nuclear-pore and trafficking components appear together. The fact sheet does not establish whether this exact module has previously been reported, and absence from STRING or hu.MAP would not prove novelty. A claim of novelty therefore requires comparison with prior co-abundance studies, matched tissue datasets and published module definitions.

**Hypothesis.** Mechanistic hypothesis: a conserved increase in nuclear biosynthetic demand induces coordinated production of nucleolar rRNA-processing machinery, RNA helicases, spliceosomal factors and nuclear-pore components. DDX21, DDX56, GTPBP4, NOP56, PDCD11 and URB1 could cooperate in rRNA maturation and ribonucleoprotein assembly, while SNRNP200, PLRG1 and DHX9 support pre-mRNA processing and RNA remodeling. Nuclear pores could couple RNA export with this synthesis program, and SEC23A or SEC23B could reflect the parallel secretory and membrane-trafficking demands of the same cellular state. The osteoblast-related annotations may reflect shared genes or growth-associated transcriptional programs rather than a direct osteogenic mechanism. This is a testable hypothesis, not evidence that the module itself causes proliferation, differentiation or disease.

### Important genes

#### DDX21

- **Related proteins** (co-abundance neighbors): GTPBP4 (0.87), DHX9 (0.86), URB1 (0.82), SNRNP200 (0.81); STRING partners: DHX9 (0.908), GTPBP4 (0.813), MYBBP1A (0.963), NOP56 (0.811)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 is a central connector in the module and participates in every globally significant GO term (12 globally significant GO/KEGG terms, q_global 0.00115–0.0419; see the table). It is localized at the nucleolar rim and is detected in cervix_uterine, while its curated functions include RNA helicase activity, ribosome and spliceosome assembly, chromatin remodeling and transcriptional regulation. It also has extensive literature support and disease associations involving neurodegenerative disease and cancer.
- **Conclusion**: Established evidence supports DDX21 as a multifunctional RNA-remodeling and nucleolar coordinator within this module. It is a strong candidate for an upstream integrator of the shared program. Whether its activity drives the observed co-abundance pattern remains a hypothesis.

#### PDCD11

- **Related proteins** (co-abundance neighbors): FASN (0.85), NOP56 (0.85), SNRNP200 (0.83), URB1 (0.82), ACSL3 (0.81), MYBBP1A (0.81), PLRG1 (0.81); STRING partners: DDX56 (0.853), GTPBP4 (0.928), MYBBP1A (0.949), NOP56 (0.997), URB1 (0.973), VARS1 (0.805)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 11. PDCD11 is a NF-kappa-B (NFKB1; 164011)-binding protein that colocalizes with U3 RNA (MIM 180710) in the nucleolus and is required for rRNA maturation and generation of 18S rRNA (Sweet et al., 2003 [PubMed 14624448]; Sweet et al., 2008 [PubMed 17654514]).[supplied by OMIM, Oct 2008].
- **Diseases (Open Targets)**: Back pain (0.277); insomnia (0.216); systemic lupus erythematosus (0.170); neoplasm (0.095); colorectal carcinoma (0.093)
- **Europe PMC papers**: 334
- **Why important**: PDCD11 is among the most connected module members and links the nucleolar cluster to FASN, ACSL3, MYBBP1A, NOP56, URB1, PLRG1 and SNRNP200. It is a nucleolar-rim protein required for rRNA maturation and generation of mature small-subunit rRNA, and it is represented across the primary ribonucleoprotein, RNA-processing, ribosome-biogenesis and nucleolar terms (8 globally significant GO/KEGG terms, q_global 0.00115–0.0402; see the table).
- **Conclusion**: Established evidence identifies PDCD11 as a strong structural and functional anchor for the nucleolar interpretation. Its connections to lipid-associated genes may indicate coordination with broader biosynthetic state, but a direct lipid-to-rRNA mechanism is not established here.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): GTPBP4 (0.86), CHD4 (0.86), NUP210 (0.85), PDCD11 (0.83), DHX9 (0.81), RNMT (0.81), NUP160 (0.81), DDX21 (0.81); STRING partners: DHX9 (0.784), PLRG1 (0.996)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_06726.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 has the highest network connectivity in the supplied module and connects the RNA-processing core to DHX9, CHD4, NUP160, NUP210, RNMT, GTPBP4, PDCD11 and DDX21. It is a U5 small nuclear ribonucleoprotein helicase and a core spliceosomal component, and it appears in the primary RNA, ribonucleoprotein, helicase, nuclear-complex and osteoblast-related terms (8 globally significant GO/KEGG terms, q_global 0.00115–0.0419; see the table). It is also represented in multiple hu.MAP spliceosomal complexes with PLRG1 (hu.MAP huMAP3_06726.1) (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1).
- **Conclusion**: Established evidence supports SNRNP200 as the principal bridge between spliceosomal RNA processing and the nucleolar-centered component of the module. Its high connectivity makes it important for module interpretation, although co-abundance does not demonstrate that it controls the other genes.

#### NOP56

- **Related proteins** (co-abundance neighbors): PDCD11 (0.85), NUP155 (0.85), DDX56 (0.83); STRING partners: DDX21 (0.811), DDX56 (0.884), GTPBP4 (0.941), MYBBP1A (0.737), PDCD11 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP56 ribonucleoprotein. Nop56p is a yeast nucleolar protein that is part of a complex with the nucleolar proteins Nop58p and fibrillarin. Nop56p is required for assembly of the 60S ribosomal subunit and is involved in pre-rRNA processing. The protein encoded by this gene is similar in sequence to Nop56p and is also found in the nucleolus. Expansion of a GGCCTG repeat from 3-8 copies to 1500-2500 copies in an intron of th…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 36 (0.586); neurodegenerative disease (0.495); ovarian neoplasm (0.272); hereditary disease (0.193); cerebellar ataxia (0.121)
- **Europe PMC papers**: 1517
- **Why important**: NOP56 is a nucleolar ribonucleoprotein associated with pre-rRNA processing, ribosomal subunit assembly and rRNA modification. It has strong STRING relationships with PDCD11, GTPBP4, DDX56, DDX21 and MYBBP1A, and it contributes to the primary ribonucleoprotein, RNA-processing, ribosome-biogenesis, rRNA-processing and nucleolar terms (8 globally significant GO/KEGG terms, q_global 0.00115–0.0402; see the table). Its disease relevance includes spinocerebellar ataxia type thirty-six and broader neurodegenerative disease associations.
- **Conclusion**: Established evidence makes NOP56 a core effector of the module's rRNA and nucleolar function. Its presence supports a genuine ribosome-biogenesis interpretation rather than a generic association with RNA abundance.

#### NUP155

- **Related proteins** (co-abundance neighbors): NOP56 (0.85), URB1 (0.84), GTPBP4 (0.82); STRING partners: NUP160 (0.994), NUP210 (0.991)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07645.1, huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 155. Nucleoporins are proteins that play an important role in the assembly and functioning of the nuclear pore complex (NPC) which regulates the movement of macromolecules across the nuclear envelope (NE). The protein encoded by this gene plays a role in the fusion of NE vesicles and formation of the double membrane NE. The protein may also be involved in cardiac physiology and may be associated with t…
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); atrial fibrillation (0.470); familial atrial fibrillation (0.390)
- **Europe PMC papers**: 944
- **Why important**: NUP155 provides a mechanistic link between the nucleolar RNA program and nuclear-envelope transport. It connects in the module to NOP56, URB1 and GTPBP4, while STRING and hu.MAP support its relationships with NUP160 and NUP210 (hu.MAP huMAP3_07645.1) (hu.MAP huMAP3_12581.1). Its curated functions include nuclear-pore assembly, nucleocytoplasmic transport and RNA export, and it has established associations with atrial fibrillation and viral disease.
- **Conclusion**: Established evidence supports NUP155 as a transport-interface component rather than a core rRNA processing factor. Its co-abundance with nucleolar genes suggests coordinated nuclear organization, but the direction and mechanism of that coupling are hypotheses.

## Module 5

**Tissue pair**: cell line and cervix_uterine  
**Genes (12)**: ADPRS, ALDOC, ANXA8L1, CTNND1, GLUL, GSTP1, EPHX1, RAB27A, STAT6, STX7, CLEC3B, TSTD1

### Function

The module does not have a statistically supported unified GO or KEGG function: no globally significant GO/KEGG term passed global correction. STRING functional enrichment is also absent, so the functional interpretation must remain gene- and network-based rather than pathway-based. The network has two apparent local neighborhoods. CLEC3B connects genes associated with extracellular or tissue-associated biology, xenobiotic metabolism, cytokine signaling, glycolysis, ADP-ribose regulation, and glutamine metabolism. ANXA8L1 connects vesicle, endosomal, membrane-adhesion, and immune-cell-associated genes. These neighborhoods are consistent with a mixed epithelial, extracellular, metabolic, and immune-cell state, but the sparse network does not establish a single biochemical pathway.

**Cell composition.** The module is not predominantly composed of secreted or plasma proteins; CLEC3B is the only gene annotated as secreted to blood. It is also not uniformly blood-cell enriched, because several genes have low immune-cell specificity or are not detected in immune cells. Nevertheless, HPA shows recurring enrichment in classical and other monocyte populations, myeloid dendritic cells, and neutrophils, while several genes are associated with esophageal epithelial cell types and other epithelial populations. This mixed pattern suggests that the shared co-abundance signal could partly reflect shared cell-type composition, immune or myeloid admixture, epithelial differentiation, or tissue-state effects rather than coordinated expression within a single cell type. The broad tissue distribution of several genes further argues against treating the module as a cervix-specific program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a particularly strong known association between EPHX1 and GSTP1. The co-abundance graph itself contains a CLEC3B-centered neighborhood and an ANXA8L1-centered neighborhood, but most of these edges lack high-confidence STRING support. No STRING functional-enrichment result is available. No hu.MAP complex contains multiple module members. Thus, the module contains one well-established detoxification-related protein relationship, while the broader co-abundance structure is not explained by a known protein complex and may represent co-regulation, shared cellular origin, or indirect tissue-level covariation.

**STRING interactions (score >= 0.7)**: 1 of 66 gene pairs: EPHX1–GSTP1 (0.989)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The underlying molecular functions of the member genes are established, including epoxide and glutathione metabolism, vesicle trafficking, cytokine signaling, cell adhesion, glycolysis, and extracellular matrix-associated biology. The module-level finding may therefore be novel as a cross-tissue co-abundance pattern, but the present evidence does not demonstrate that it is a new molecular mechanism. The absence of multiple STRING links, the absence of a hu.MAP complex, and the absence of globally significant GO or KEGG enrichment make a strong novelty claim premature. Replication in independent cell-line and cervix datasets, followed by cell-type-resolved testing, would be needed to distinguish a genuinely conserved regulatory module from shared sample composition or technical covariance.

**Hypothesis.**  The module may represent a composite epithelial or tissue-state program in which vesicle and endosomal trafficking through ANXA8L1, STX7, and RAB27A is coupled to epithelial adhesion through CTNND1, while CLEC3B-associated extracellular biology is co-abundant with cellular detoxification and stress handling through EPHX1 and GSTP1. The recurring myeloid and neutrophil HPA signals could indicate that this program is partly shaped by immune-cell admixture or inflammatory tissue remodeling. This is a testable hypothesis, not an established pathway: single-cell expression, purified-cell co-abundance, perturbation of vesicle trafficking or detoxification genes, and independent replication would be required.

### Important genes

#### CLEC3B

- **Related proteins** (co-abundance neighbors): TSTD1 (0.95), EPHX1 (0.93), STAT6 (0.87), ALDOC (0.87), ADPRS (0.86), GLUL (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: C-type lectin domain family 3 member B. Enables calcium ion binding activity; heparin binding activity; and kringle domain binding activity. Involved in bone mineralization and cellular response to transforming growth factor beta stimulus. Located in cytoplasm; extracellular space; and granular component. Part of collagen-containing extracellular matrix. Implicated in osteoarthritis. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: macular dystrophy, retinal, 4 (0.453); neurodegenerative disease (0.314); Parkinson disease (0.232); Alzheimer disease (0.223); lysosomal storage disease (0.221)
- **Europe PMC papers**: 1141
- **Why important**: CLEC3B is the central network node, connecting the largest local neighborhood in the module. It is secreted to blood, associated with the collagen-containing extracellular matrix, calcium and heparin binding, plasminogen activation, bone mineralization, and response to transforming growth factor beta. Its HPA profile is tissue enhanced in adipose tissue and cell-type enhanced in several epithelial or stromal populations, rather than immune cells. Its disease links include retinal macular dystrophy and neurodegenerative disease, and it has a substantial literature base.
- **Conclusion**: Established evidence supports CLEC3B as the best network-level marker of an extracellular or tissue-remodeling component. It may organize the module statistically through shared tissue state, but the data do not establish that CLEC3B mechanistically regulates the other module genes.

#### ANXA8L1

- **Related proteins** (co-abundance neighbors): GSTP1 (0.89), STX7 (0.84), RAB27A (0.83), CTNND1 (0.83), TSTD1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A8 like 1. This gene encodes a member of the annexin family of evolutionarily conserved Ca2+ and phospholipid binding proteins. The encoded protein may function as an an anticoagulant that indirectly inhibits the thromboplastin-specific complex. Overexpression of this gene has been associated with acute myelocytic leukemia. A highly similar duplicated copy of this gene is found in close proximity on the long…
- **Diseases (Open Targets)**: stroke disorder (0.283); renal cell carcinoma (0.036); esophageal adenocarcinoma (0.033); COVID-19 (0.025); severe acute respiratory syndrome (0.024)
- **Europe PMC papers**: 170
- **Why important**: ANXA8L1 is the second major network node and links genes involved in vesicles, endosomal transport, membrane adhesion, and immune-cell-associated expression. As an annexin-family protein, it is annotated for calcium and phospholipid binding and may have anticoagulant activity. It is tissue enhanced in esophagus and skin and is immune-cell enhanced in classical monocytes and myeloid dendritic cells. Its disease associations include stroke and several cancer-related conditions, although its literature base is more limited than that of the better-studied module genes.
- **Conclusion**: Established evidence supports ANXA8L1 as a plausible marker of vesicle or membrane-state variation and as a bridge between epithelial and myeloid signals. Its centrality makes it important for interpreting the module, but a direct regulatory role remains hypothetical.

#### EPHX1

- **Related proteins** (co-abundance neighbors): CLEC3B (0.93); STRING partners: GSTP1 (0.989)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: epoxide hydrolase 1. Epoxide hydrolase is a critical biotransformation enzyme that converts epoxides from the degradation of aromatic compounds to trans-dihydrodiols which can be conjugated and excreted from the body. Epoxide hydrolase functions in both the activation and detoxification of epoxides. Mutations in this gene cause preeclampsia, epoxide hydrolase deficiency or increased epoxide hydrolase activity. Alterna…
- **Diseases (Open Targets)**: hypercholanemia, familial 1 (0.399); Insulin resistance (0.372); lipodystrophy (0.370); hypercholanemia, familial (0.370); hereditary lipodystrophy (0.266)
- **Europe PMC papers**: 2198
- **Why important**: EPHX1 is connected to the central CLEC3B neighborhood and has the strongest known STRING relationship in the module through GSTP1. It encodes an epoxide hydrolase involved in xenobiotic and arachidonate metabolism and can participate in both detoxification and epoxide activation. HPA shows tissue enhancement in liver and adrenal gland and cell-type enhancement in hepatocytes, adrenal cortex, oocytes, ovarian stromal cells, and respiratory ciliated cells. It also has extensive literature and disease links involving lipid and metabolic traits.
- **Conclusion**: Established evidence supports EPHX1 as a detoxification and lipid-metabolism marker, with a known biochemical relationship to GSTP1. In this module it may report oxidative or xenobiotic stress, but the data do not show that it drives the co-abundance pattern.

#### GSTP1

- **Related proteins** (co-abundance neighbors): ANXA8L1 (0.89); STRING partners: EPHX1 (0.989)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutathione S-transferase pi 1. Glutathione S-transferases (GSTs) are a family of enzymes that play an important role in detoxification by catalyzing the conjugation of many hydrophobic and electrophilic compounds with reduced glutathione. Based on their biochemical, immunologic, and structural properties, the soluble GSTs are categorized into 4 main classes: alpha, mu, pi, and theta. This GST family member is a polymorphic gene…
- **Diseases (Open Targets)**: neurodegenerative disease (0.350); breast cancer (0.117); hepatocellular carcinoma (0.115); neoplasm (0.114); posterior cortical atrophy (0.113)
- **Europe PMC papers**: 12759
- **Why important**: GSTP1 is the partner of EPHX1 in the only high-confidence STRING interaction reported for the module and is also linked to ANXA8L1 in the co-abundance graph. It catalyzes glutathione conjugation and is annotated for glutathione, xenobiotic, prostaglandin, and reactive-oxygen biology. HPA shows tissue enhancement in esophagus and cell-type enhancement across esophageal and respiratory epithelial populations. It is the most extensively studied gene among the selected module members and has broad cancer and disease associations.
- **Conclusion**: Established evidence identifies GSTP1 as a strong candidate marker of epithelial detoxification and redox stress and as the best-supported molecular connection within the module. Its high literature volume increases interpretability, but the module does not prove that GSTP1-mediated detoxification causes the cross-tissue co-abundance.

#### STX7

- **Related proteins** (co-abundance neighbors): ANXA8L1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Lysosomes; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntaxin 7. The protein encoded by this gene is a syntaxin family membrane receptor involved in vesicle transport. The encoded protein binds alpha-SNAP, an important regulator of transport vesicle fusion. Along with syntaxin 13, this protein plays a role in the ordered fusion of endosomes and lysosomes with the phagosome. [provided by RefSeq, May 2016].
- **Diseases (Open Targets)**: neurodegenerative disease (0.489); Abnormality of neuronal migration (0.259); Raynaud disease (0.180); placental abruption (0.166); aortic stenosis (0.081)
- **Europe PMC papers**: 701
- **Why important**: STX7 connects to ANXA8L1 and encodes a syntaxin involved in intracellular vesicle transport, endosome and lysosome fusion, and phagosome-related trafficking. HPA places it in lysosomes and shows broad enrichment across immune populations, including monocytes, dendritic cells, B cells, and neutrophils, as well as selected other cell types. It has established links to intracellular transport and immune-cell function and a substantial literature base.
- **Conclusion**: Established evidence supports STX7 as a plausible indicator of vesicle and phagolysosomal activity and as a bridge between the ANXA8L1 neighborhood and immune-cell composition. Its inclusion supports a trafficking or admixture interpretation, but not a single-cell autonomous mechanism.

## Module 6

**Tissue pair**: cell line and cervix_uterine  
**Genes (17)**: AFDN, DENND2D, ELL2, FCHO2, FERRY3, H2AC21, HPX, ARHGAP45, HMOX1, ITIH4, PRKCB, MYH10, HSPG2, MRPL13, SH3BGRL2, UBAP1, ZNF185

### Function

No GO or KEGG term passed global correction, so the module does not have a statistically established pathway assignment from those analyses. Its strongest biological interpretation is a mixed extracellular heme and acute-phase response axis combined with immune-cell, epithelial, endocytic, junctional, and cytoskeletal signals. ITIH4 is the principal network connector, linking the plasma-associated HPX and HSPG2 branch with nuclear, membrane, and signaling genes. HPX and HMOX1 provide a biologically coherent heme-handling component, while ITIH4 is annotated for acute-phase response, hyaluronan metabolism, and cytokine response. The remaining links are more heterogeneous, so the module should not be assigned a single definitive pathway function.

**Cell composition.** The module is not dominated by secreted proteins, but it contains a conspicuous plasma-associated component: ITIH4 and HPX are secreted to blood, and HSPG2 is secreted to extracellular matrix. ITIH4 and HPX are liver-enriched, whereas HMOX1 is enriched in lymphoid tissue and monocytes. HPA profiles also point to lymphoid tissue, bone marrow, blood vessels, epithelial populations, platelets, neutrophils, and other immune-related cell types. Several genes are detected in cervix_uterine, while ITIH4, HPX, HMOX1, ARHGAP45, PRKCB, and MYH10 are not detected there by IHC. This mixture raises a substantial possibility that the shared signal reflects blood or immune-cell carryover, vascular or stromal material, and shared epithelial or immune cell types rather than a uniform cervix-specific program. Broadly expressed intracellular genes are also present, including mitochondrial translation, chromatin, trafficking, and transcription-related components.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING support is sparse but biologically informative. The established high-confidence links are HPX with HMOX1 and HPX with ITIH4. These relationships support a heme-scavenging and heme-response interpretation, but STRING supplied no functional-enrichment term. hu.MAP provides additional context: HPX, HMOX1, and ITIH4 co-occur in (hu.MAP huMAP3_10678.1), while HPX and ITIH4 recur together in (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), and (hu.MAP huMAP3_15040.1). ELL2 with DENND2D is represented in (hu.MAP huMAP3_12350.1), and PRKCB with FCHO2 in (hu.MAP huMAP3_12394.1). Because most module members are not connected by STRING or represented together in hu.MAP, the co-abundance structure is broader and more context-dependent than a single established protein complex. The hu.MAP overlaps also include many plasma and extracellular proteins, reinforcing the possibility of a circulating-protein or sample-composition contribution.

**STRING interactions (score >= 0.7)**: 2 of 136 gene pairs: HMOX1–HPX (0.753); HPX–ITIH4 (0.706)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10678.1 (HPX, HMOX1, ITIH4; 3/71); huMAP3_12350.1 (ELL2, DENND2D; 2/34); huMAP3_09531.1 (HPX, ITIH4; 2/47); huMAP3_10101.1 (HPX, ITIH4; 2/49); huMAP3_15040.1 (HPX, ITIH4; 2/64); huMAP3_12394.1 (PRKCB, FCHO2; 2/98)

### Novelty

The module should not be described as a newly discovered molecular complex. HPX, HMOX1, and ITIH4 have prior database support through STRING and recurring hu.MAP plasma-associated complexes, and the functions of the principal genes are already established. A potentially novel aspect is the co-abundance of this heme and acute-phase branch with the particular epithelial, immune, trafficking, and cytoskeletal genes in the shared cell line and cervix_uterine context. However, the available evidence cannot establish that this combination is novel: the module has no globally significant GO or KEGG term, STRING functional enrichment is absent, and several genes may reflect blood, immune, vascular, or epithelial composition. Novelty therefore remains a hypothesis requiring replication in independent cohorts, adjustment for cell composition, and comparison with existing co-expression modules.

**Hypothesis.** Hypothesis: the shared module reflects a tissue-interface stress state in which extracellular heme and acute-phase proteins are co-abundant with local immune, epithelial, vascular, and trafficking programs. In this model, HPX binds circulating heme, HMOX1 responds by catabolizing heme and may limit oxidative or inflammatory damage, and ITIH4 participates in the acute-phase extracellular matrix and hyaluronan environment. HSPG2, MYH10, AFDN, FCHO2, PRKCB, and ARHGAP45 could represent vascular, junctional, cytoskeletal, endocytic, and immune-cell context around that extracellular signal. The model is provisional: the network does not demonstrate physical interaction among all members, and sample admixture is an alternative explanation.

### Important genes

#### ITIH4

- **Related proteins** (co-abundance neighbors): HSPG2 (0.92), H2AC21 (0.90), UBAP1 (0.87), ELL2 (0.85), ARHGAP45 (0.82), ZNF185 (0.81); STRING partners: HPX (0.706)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 4. The protein encoded by this gene is secreted into the blood, where it is cleaved by plasma kallikrein into two smaller forms. Expression of this gene has been detected only in liver, and it seems to be upregulated during surgical trauma. This gene is part of a cluster of similar genes on chromosome 3. Two transcript variants encoding different isoforms have been found for this gene. [provided by R…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.466); coronary artery disorder (0.417); type 2 diabetes mellitus (0.397); osteoarthritis (0.387); diabetes mellitus (0.363)
- **Europe PMC papers**: 1710
- **Why important**: ITIH4 is the central network connector and has the strongest weighted network position. It is liver-enriched, secreted to blood, annotated for acute-phase response, hyaluronan metabolism, and cytokine response, and is repeatedly represented with HPX in hu.MAP (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), and (hu.MAP huMAP3_15040.1). Its disease associations include skeletal, coronary, metabolic, and osteoarthritic phenotypes, and it has an extensive literature base.
- **Conclusion**: Established evidence supports ITIH4 as a circulating acute-phase and extracellular-matrix component that anchors the module. It is a strong marker of the proposed plasma or tissue-interface signal, but its central co-abundance position does not prove that it regulates the other module genes.

#### HPX

- **Related proteins** (co-abundance neighbors): FCHO2 (0.91), H2AC21 (0.90), HMOX1 (0.89), MYH10 (0.80); STRING partners: HMOX1 (0.753), ITIH4 (0.706)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1
- **Function (MyGene.info)**: hemopexin. This gene encodes a plasma glycoprotein that binds heme with high affinity. The encoded protein is an acute phase protein that transports heme from the plasma to the liver and may be involved in protecting cells from oxidative stress. [provided by RefSeq, Apr 2009].
- **Diseases (Open Targets)**: panniculitis (0.116); neoplasm (0.107); familial idiopathic steroid-resistant nephrotic syndrome (0.101); hepatocellular carcinoma (0.101); focal segmental glomerulosclerosis (0.097)
- **Europe PMC papers**: 6894
- **Why important**: HPX is a network hub relative to most module members, is liver-enriched and secreted to blood, and encodes a heme-binding plasma glycoprotein involved in heme transport and protection from oxidative stress. It has STRING links to both HMOX1 and ITIH4 and appears in several hu.MAP complexes, including (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), and (hu.MAP huMAP3_15040.1). It also has a large literature base and disease associations involving renal disease and hepatocellular carcinoma.
- **Conclusion**: Established evidence identifies HPX as the most direct biochemical indicator of a plasma heme-scavenging component. Its co-abundance with HMOX1 is consistent with coordinated heme handling, but the data do not establish whether this reflects regulation, shared cellular sources, or extracellular protein carryover.

#### HMOX1

- **Related proteins** (co-abundance neighbors): HPX (0.89); STRING partners: HPX (0.753)
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location Golgi apparatus, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1
- **Function (MyGene.info)**: heme oxygenase 1. Heme oxygenase, an essential enzyme in heme catabolism, cleaves heme to form biliverdin, which is subsequently converted to bilirubin by biliverdin reductase, and carbon monoxide, a putative neurotransmitter. Heme oxygenase activity is induced by its substrate heme and by various nonheme substances. Heme oxygenase occurs as 2 isozymes, an inducible heme oxygenase-1 and a constitutive heme oxygenas…
- **Diseases (Open Targets)**: heme oxygenase 1 deficiency (0.686); amyloidosis (0.465); neurodegenerative disease (0.459); cystic fibrosis (0.392); chronic obstructive pulmonary disease (0.360)
- **Europe PMC papers**: 38190
- **Why important**: HMOX1 is the enzymatic counterpart to the HPX heme-binding signal and is directly linked to HPX by STRING. It is enriched in lymphoid tissue and monocyte populations, is present in hu.MAP complex (hu.MAP huMAP3_10678.1), and is annotated for heme oxidation, inflammatory wound healing, leukocyte migration, angiogenesis, and endothelial proliferation. It has the largest literature volume among the selected genes and multiple disease associations involving oxidative, inflammatory, pulmonary, and neurodegenerative biology.
- **Conclusion**: Established evidence supports HMOX1 as an inducible stress and heme-catabolism marker, particularly compatible with monocyte or macrophage involvement. The module supports a coordinated heme-response interpretation, but it does not prove that HMOX1 activation caused the shared co-abundance pattern.

#### HSPG2

- **Related proteins** (co-abundance neighbors): ITIH4 (0.92); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 connects the ITIH4-centered branch to extracellular matrix and vascular biology. It is tissue-enhanced in blood vessels, detected in cervix_uterine, secreted to extracellular matrix, and annotated for inflammatory response, receptor-mediated endocytosis, cell differentiation, and regulation of angiogenesis. It is linked to ITIH4 in the module and has substantial literature and disease evidence, including skeletal dysplasia, atrial fibrillation, and infectious disease associations.
- **Conclusion**: Established evidence supports HSPG2 as an extracellular vascular or stromal context marker that could connect circulating acute-phase proteins to the cervix tissue environment. Its role as a mechanistic bridge within this module remains a hypothesis because direct module-wide interaction evidence is absent.

#### PRKCB

- **Related proteins** (co-abundance neighbors): ARHGAP45 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: protein kinase C beta. Protein kinase C (PKC) is a family of serine- and threonine-specific protein kinases that can be activated by calcium and second messenger diacylglycerol. PKC family members phosphorylate a wide variety of protein targets and are known to be involved in diverse cellular signaling pathways. PKC family members also serve as major receptors for phorbol esters, a class of tumor promoters. Each member …
- **Diseases (Open Targets)**: acute myeloid leukemia (0.588); mast cell leukemia (0.475); systemic mastocytosis (0.471); ulcerative colitis (0.468); mastocytosis (0.462)
- **Europe PMC papers**: 3606
- **Why important**: PRKCB provides a signaling and immune-cell connection distinct from the plasma branch. It is tissue-enhanced in brain and lymphoid tissue, has cell-type enhancement in B cells, monocytes, Kupffer cells, and neutrophil progenitors, and is annotated for protein phosphorylation and signal transduction. It connects to ARHGAP45 in the co-abundance network and shares hu.MAP complex (hu.MAP huMAP3_12394.1) with FCHO2. Its literature is extensive and its disease associations include myeloid and mast-cell leukemias, mastocytosis, and ulcerative colitis.
- **Conclusion**: Established evidence supports PRKCB as an immune and signal-transduction marker that may identify the cellular context accompanying the extracellular heme and acute-phase signal. Its presence does not establish a direct biochemical pathway with HPX or ITIH4; that connection is a module-level hypothesis.

## Module 7

**Tissue pair**: cell line and cervix_uterine  
**Genes (36)**: AGR2, ANXA1, ACTR10, NAT1, ASTN2, CAPG, CTSG, CBR1, CNN2, HADHB, EIF3C, ERMP1, CES2, GALE, ITGB2, KNG1, MNDA, MYO1G, NSFL1C, NSF, SERPINB2, PDIA4, PDLIM2, PLG, PNP, PSMC4, PSMD13, ARHGAP32, ROCK1, S100A2, S100A13, SOD2, SERPINB8, SUN2, TMPRSS11E, UACA

### Function

No GO or KEGG term passed global correction, so the module does not have a globally validated pathway annotation from those analyses. Its biological signal is nevertheless coherent when the network, HPA profiles, gene annotations, and supplementary STRING evidence are considered. The strongest interpretation is a mixed inflammatory and tissue-interface program combining myeloid or neutrophil-associated activity, epithelial protease and stress responses, extracellular proteolysis, fibrinolysis or kinin-system biology, and intracellular protein quality control. STRING supplementary evidence supports leukocyte migration (STRING Process Leukocyte migration; within-query FDR = 0.0113) and a disulfide-bond or secretory-protein theme (STRING Keyword Disulfide bond; within-query FDR = 0.037), but these are not global enrichment results. The module should therefore be interpreted as a compositional or cell-state program rather than as a single definitive pathway.

**Cell composition.** The module is heterogeneous rather than a uniform housekeeping module. HPA indicates frequent association with bone marrow, lymphoid tissue, esophagus, intestine, and liver, and frequent association with esophageal apical cells, neutrophils, neutrophil progenitors, monocytes, and enterocytes. This supports contributions from myeloid or other blood-associated cells together with epithelial cells. Several members are secreted or plasma-associated proteins, especially PLG and KNG1, while ANXA1 and S100A13 can be secreted in relevant tissues. The module also contains epithelial and secretory-pathway genes such as TMPRSS11E, AGR2, PDIA4, SERPINB8, and S100A2, as well as broadly distributed intracellular genes. Thus, shared co-abundance between cell line and cervix_uterine may partly reflect shared epithelial or immune-cell content, inflammatory state, extracellular protein carryover, or sample composition rather than a dedicated cervix-specific mechanism. The HPA profile for cervix_uterine detects many module proteins, whereas the cell-line comparison has no matching HPA tissue protein data, limiting direct protein-level interpretation for the cell-line side.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides three high-confidence pairwise relationships within the module: the plasma-protein relationship between KNG1 and PLG, the relationship between PLG and SERPINB2, and the proteasome relationship between PSMC4 and PSMD13. These known links support extracellular coagulation or fibrinolysis biology and proteasome biology, but the sparse STRING connectivity indicates that most co-abundance edges are not established physical or functional interactions in STRING. Supplementary STRING annotations connect CTSG, MYO1G, PLG, ANXA1, ITGB2, ROCK1, and CNN2 with leukocyte migration (STRING Process Leukocyte migration; within-query FDR = 0.0113), and connect a broader set of secretory, extracellular, and intracellular proteins with a disulfide-bond keyword (STRING Keyword Disulfide bond; within-query FDR = 0.037). These findings are supportive rather than globally corrected enrichment evidence. hu.MAP independently places CTSG with MNDA in several immune or secretory-associated complexes (hu.MAP huMAP3_13546.1), (hu.MAP huMAP3_10260.1), and (hu.MAP huMAP3_11343.1); PLG with KNG1 in multiple plasma-protein or extracellular complexes (hu.MAP huMAP3_07701.1), (hu.MAP huMAP3_09273.1), (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1), and (hu.MAP huMAP3_10678.1); CES2 with AGR2 in (hu.MAP huMAP3_14537.1); and PSMC4 with PSMD13 in proteasome complexes (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1). Because each complex contains only a small subset of module members, hu.MAP supports recognizable submodules rather than one unified physical complex.

**STRING interactions (score >= 0.7)**: 3 of 630 gene pairs: KNG1–PLG (0.898); PLG–SERPINB2 (0.966); PSMC4–PSMD13 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Process Leukocyte migration (FDR = 0.0113, 7 genes); Keyword Disulfide bond (FDR = 0.037, 13 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13546.1 (CTSG, MNDA; 2/8); huMAP3_10260.1 (CTSG, MNDA; 2/14); huMAP3_07701.1 (PLG, KNG1; 2/22); huMAP3_14537.1 (CES2, AGR2; 2/24); huMAP3_09273.1 (PLG, KNG1; 2/28); huMAP3_05064.1 (PSMC4, PSMD13; 2/31); huMAP3_08395.1 (PLG, KNG1; 2/43); huMAP3_09531.1 (PLG, KNG1; 2/47); huMAP3_10101.1 (PLG, KNG1; 2/49); huMAP3_11343.1 (CTSG, MNDA; 2/54); huMAP3_15040.1 (PLG, KNG1; 2/64); huMAP3_09656.1 (PSMC4, PSMD13; 2/64); huMAP3_13725.1 (PSMC4, PSMD13; 2/69); huMAP3_10678.1 (PLG, KNG1; 2/71)

### Novelty

The underlying biology is not new: neutrophil and myeloid functions, plasminogen and kininogen biology, epithelial proteases, ER protein folding, and proteasome activity are established. The exact cross-tissue co-abundance module may still represent a new systems-level observation, because the module combines these signals across cell line and cervix_uterine and has limited direct STRING connectivity. However, sparse STRING support or absence from hu.MAP cannot by itself establish novelty. The most defensible conclusion is that this is a potentially novel co-abundance configuration assembled from largely known biological components, requiring replication, cell-composition adjustment, and independent validation before being called a new mechanism.

**Hypothesis.** Hypothesis: the shared module reflects an epithelial tissue-interface state with variable myeloid or neutrophil contribution. In this model, epithelial stress or secretory activity engages AGR2, PDIA4, and TMPRSS11E, while infiltrating or co-captured myeloid cells contribute MNDA, CTSG, ITGB2, MYO1G, and ANXA1. Extracellular PLG and KNG1 could connect local proteolysis, fibrinolysis, vascular permeability, and inflammatory signaling, with SERPINB2 providing protease regulation. Proteasome components and oxidative-stress-related genes could represent intracellular adaptation to inflammatory or secretory stress. This hypothesis predicts that the module will weaken after adjustment for epithelial and myeloid cell proportions and that its extracellular component will track plasma contamination or local tissue injury unless validated by spatial, protein, or perturbation experiments.

### Important genes

#### MNDA

- **Related proteins** (co-abundance neighbors): CBR1 (0.98), PSMD13 (0.97), MYO1G (0.95), EIF3C (0.92), PDIA4 (0.90), ERMP1 (0.90), ANXA1 (0.86), SUN2 (0.84), S100A13 (0.82), HADHB (0.82), UACA (0.82), CAPG (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13546.1, huMAP3_10260.1, huMAP3_11343.1
- **Function (MyGene.info)**: myeloid cell nuclear differentiation antigen. The myeloid cell nuclear differentiation antigen (MNDA) is detected only in nuclei of cells of the granulocyte-monocyte lineage. A 200-amino acid region of human MNDA is strikingly similar to a region in the proteins encoded by a family of interferon-inducible mouse genes, designated Ifi-201, Ifi-202, and Ifi-203, that are not regulated in a cell- or tissue-specific fashion. The 1.8-kb MNDA mRNA, …
- **Diseases (Open Targets)**: COVID-19 (0.221); type 1 diabetes mellitus (0.158); autosomal dominant macrothrombocytopenia (0.082); hereditary thrombocytopenia with normal platelets (0.075); Thrombocytopenia (0.072)
- **Europe PMC papers**: 1563
- **Why important**: MNDA is a central network node with the greatest connectivity in the supplied subgraph and links immune-associated genes with ER, cytoskeletal, translation, and proteasome-related members. HPA places it in bone marrow and lymphoid contexts and in monocyte and neutrophil lineages. It also anchors multiple hu.MAP complexes with CTSG (hu.MAP huMAP3_13546.1), (hu.MAP huMAP3_10260.1), and (hu.MAP huMAP3_11343.1). Its myeloid nuclear differentiation function and substantial literature support make it a strong indicator of immune-cell composition or myeloid state.
- **Conclusion**: Established evidence supports MNDA as a myeloid or granulocyte-monocyte-associated marker and as a major network organizer in this module. The module-level association does not establish that MNDA mechanistically drives the epithelial or extracellular components; it may instead report shared myeloid content or inflammatory state.

#### CTSG

- **Related proteins** (co-abundance neighbors): ASTN2 (0.94), SERPINB8 (0.93), UACA (0.92), CNN2 (0.86), ITGB2 (0.85), PSMC4 (0.84), PSMD13 (0.84), ACTR10 (0.83), CAPG (0.82), NSFL1C (0.81), GALE (0.81), S100A2 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13546.1, huMAP3_10260.1, huMAP3_11343.1
- **Function (MyGene.info)**: cathepsin G. The protein encoded by this gene, a member of the peptidase S1 protein family, is found in azurophil granules of neutrophilic polymorphonuclear leukocytes. The encoded protease has a specificity similar to that of chymotrypsin C, and may participate in the killing and digestion of engulfed pathogens, and in connective tissue remodeling at sites of inflammation. In addition, the encoded protein is …
- **Diseases (Open Targets)**: tuberculosis (0.374); ptosis (0.180); neoplasm (0.103); colorectal carcinoma (0.095); non-small cell lung carcinoma (0.093)
- **Europe PMC papers**: 4011
- **Why important**: CTSG is another highly connected module node and is linked to immune, cytoskeletal, proteasome, and epithelial-associated genes. It is a neutrophil azurophil-granule protease with antimicrobial and tissue-remodeling functions. It is represented in the supplementary leukocyte-migration and disulfide-bond annotations (STRING Process Leukocyte migration; within-query FDR = 0.0113), (STRING Keyword Disulfide bond; within-query FDR = 0.037), and occurs with MNDA in several hu.MAP complexes (hu.MAP huMAP3_13546.1), (hu.MAP huMAP3_10260.1), and (hu.MAP huMAP3_11343.1). Its disease and literature support are substantial.
- **Conclusion**: Established evidence supports CTSG as a plausible marker of neutrophil or myeloid contribution and of inflammatory proteolysis. Whether CTSG directly organizes the module is unproven; its high network position may reflect co-abundance with infiltrating cells and protease-rich extracellular material.

#### PLG

- **Related proteins** (co-abundance neighbors): TMPRSS11E (0.89); STRING partners: KNG1 (0.898), SERPINB2 (0.966)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07701.1, huMAP3_09273.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: plasminogen. The plasminogen protein encoded by this gene is a serine protease that circulates in blood plasma as an inactive zymogen and is converted to the active protease, plasmin, by several plasminogen activators such as tissue plasminogen activator (tPA), urokinase plasminogen activator (uPA), kallikrein, and factor XII (Hageman factor). The conversion of plasminogen to plasmin involves the cleavage of t…
- **Diseases (Open Targets)**: hypoplasminogenemia (0.813); hereditary angioedema (0.737); hemorrhage (0.605); dysplasminogenemia (0.598); Menorrhagia (0.579)
- **Europe PMC papers**: 17740
- **Why important**: PLG connects the module to a well-established extracellular proteolysis and fibrinolysis system. It is liver-enriched, secreted to blood, and has a direct STRING relationship with KNG1 and SERPINB2. It appears with KNG1 across many hu.MAP plasma-protein complexes (hu.MAP huMAP3_07701.1), (hu.MAP huMAP3_09273.1), (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1), and (hu.MAP huMAP3_10678.1), and it contributes to both supplementary STRING themes (STRING Process Leukocyte migration; within-query FDR = 0.0113), (STRING Keyword Disulfide bond; within-query FDR = 0.037). Its extensive literature and disease associations make it an important biochemical anchor.
- **Conclusion**: Established evidence supports PLG as a circulating extracellular protein involved in plasmin generation, fibrinolysis, matrix turnover, and related inflammatory processes. In this module, PLG may reflect blood or plasma contribution rather than local production by cervix or cell-line cells; a local mechanistic role remains a hypothesis.

#### KNG1

- **Related proteins** (co-abundance neighbors): PNP (0.92), SERPINB2 (0.91), CES2 (0.87), AGR2 (0.85), CAPG (0.80); STRING partners: PLG (0.898)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07701.1, huMAP3_09273.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: kininogen 1. This gene uses alternative splicing to generate two different proteins- high molecular weight kininogen (HMWK) and low molecular weight kininogen (LMWK). HMWK is essential for blood coagulation and assembly of the kallikrein-kinin system. Also, bradykinin, a peptide causing numerous physiological effects, is released from HMWK. Bradykinin also functions as an antimicrobial peptide with antibacteri…
- **Diseases (Open Targets)**: congenital high-molecular-weight kininogen deficiency (0.733); venous thromboembolism (0.547); hereditary angioedema (0.458); serum lipopolysaccharide activity (0.367); ischemic stroke (0.363)
- **Europe PMC papers**: 2325
- **Why important**: KNG1 is a secreted liver-enriched plasma protein that produces high- and low-molecular-weight kininogen products and participates in coagulation and the kallikrein-kinin system. It has a direct STRING relationship with PLG and appears with PLG in multiple hu.MAP extracellular and plasma-protein complexes. Its network links to SERPINB2, CES2, AGR2, and CAPG, giving it a bridge between extracellular biology and epithelial or intracellular module members.
- **Conclusion**: Established evidence supports KNG1 as an extracellular coagulation, kinin, and vascular-signaling component. Its presence is consistent with plasma contribution or tissue injury and does not prove that a local kinin mechanism operates in the shared module.

#### ITGB2

- **Related proteins** (co-abundance neighbors): CTSG (0.85), PDLIM2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 2. This gene encodes an integrin beta chain, which combines with multiple different alpha chains to form different integrin heterodimers. Integrins are integral cell-surface proteins that participate in cell adhesion as well as cell-surface mediated signalling. The encoded protein plays an important role in immune response and defects in this gene cause leukocyte adhesion deficiency. Alternative spli…
- **Diseases (Open Targets)**: leukocyte adhesion deficiency 1 (0.827); psoriasis vulgaris (0.585); leukocyte adhesion deficiency (0.559); dry eye syndrome (0.556); psoriasis (0.490)
- **Europe PMC papers**: 6754
- **Why important**: ITGB2 is a plasma-membrane integrin subunit with a well-established role in leukocyte adhesion, migration, phagocytosis, and immune signaling. HPA associates it with bone marrow, lymphoid tissue, dendritic cells, macrophages, and monocyte progenitors. It participates in the supplementary leukocyte-migration and disulfide-bond annotations (STRING Process Leukocyte migration; within-query FDR = 0.0113), (STRING Keyword Disulfide bond; within-query FDR = 0.037) and connects to CTSG and PDLIM2 in the module network. Its strong disease relevance to leukocyte adhesion deficiency further supports its biological importance.
- **Conclusion**: Established evidence supports ITGB2 as an immune-cell adhesion and trafficking marker that fits the leukocyte component of the module. The data do not show that ITGB2 is responsible for the co-abundance pattern or that it mediates a cervix-specific process.

#### AGR2

- **Related proteins** (co-abundance neighbors): KNG1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_14537.1
- **Function (MyGene.info)**: anterior gradient 2, protein disulphide isomerase family member. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, a catalytically active thioredoxin domain, and a C-terminal ER-retention sequence. This protein plays a role in cell migration, cellular transformation and metasta…
- **Diseases (Open Targets)**: respiratory infections, recurrent, and failure to thrive with or without diarrhea (0.670); chronic diarrheal disease (0.462); alcohol drinking (0.305); Epiphora (0.254); cutaneous melanoma (0.142)
- **Europe PMC papers**: 3105
- **Why important**: AGR2 is an ER protein-folding factor with tissue enhancement in cervix and gastrointestinal tissues and detection in cervix_uterine. It is associated with secretory and epithelial cell types, links to KNG1 in the module network, and occurs with CES2 in hu.MAP complex (hu.MAP huMAP3_14537.1). Its established role in ER protein folding, stress responses, cell migration, and cellular transformation provides a plausible epithelial counterpart to the immune and plasma-protein signals.
- **Conclusion**: Established evidence supports AGR2 as an epithelial secretory-pathway and ER-stress-associated protein that is particularly relevant to the cervix component. Its co-abundance with plasma and myeloid genes may indicate epithelial stress alongside immune or blood contribution, but a direct AGR2-mediated connection to KNG1 or the full module remains hypothetical.

## Module 8

**Tissue pair**: cell line and cervix_uterine  
**Genes (28)**: AKR1B10, AKR1D1, AQR, ATP1A1, ATP2A2, DSP, DHX36, FGA, GBP6, GPD2, MACROH2A1, KRT17, LLGL2, TMPO, PKP1, JUP, PLEC, POF1B, PRKDC, PTBP1, RPL6, RTTN, SACK1A, SUPT16H, SRP68, CCT7, TGM1, TMX1

### Function

The strongest interpretation is an epithelial structural and barrier module centered on desmosome organization, intermediate-filament anchoring, keratinocyte differentiation, and calcium-dependent epithelial integrity. The globally corrected GO evidence supports regulation of striated muscle contraction, regulation of blood circulation, regulation of muscle contraction, cardiac muscle action potential, cardiac conduction, and keratinocyte differentiation (6 globally significant GO/KEGG terms, q_global 0.0169–0.0434; see the table). The muscle and cardiac terms are driven largely by ATP1A1, ATP2A2, DSP, and JUP, whereas the keratinocyte term includes DSP, KRT17, MACROH2A1, PKP1, PLEC, and TGM1 (GO:BP keratinocyte differentiation; q_global = 0.0434). Taken together with the epithelial tissue and cell-type profiles, the most coherent biological interpretation is a keratinized epithelial junction and cytoskeletal program, with a secondary calcium-handling and excitable-tissue signal. The muscle and cardiac annotations may reflect shared structural and calcium-regulatory biology rather than a cardiac module in these tissues.

**Cell composition.** The module is strongly biased toward epithelial and keratinocyte-associated biology rather than being predominantly blood-cell or housekeeping derived. HPA profiles repeatedly point to esophagus, skin, suprabasal keratinocytes, basal keratinocytes, and ocular or other epithelial cell types. DSP, JUP, PKP1, KRT17, TGM1, PLEC, and POF1B support an epithelial junction, differentiation, or cytoskeletal interpretation. Most genes have low immune-cell specificity or are not detected in immune cells, although JUP, GPD2, and some other genes have blood-cell associations. The module is not dominated by secreted proteins, but FGA is a liver-enriched protein secreted to blood and is not detected in the cervix sample by HPA. This makes a contribution from blood or tissue fluid plausible for part of the signal, especially for FGA, but the broad epithelial pattern and cervix protein detection across many module genes argue against a purely blood-derived explanation. Several broadly expressed genes, including ribosomal, chromatin, RNA-processing, and chaperone-related genes, may represent general cellular support rather than the defining module function.

**GO/KEGG enrichment**: 6 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulation of striated muscle contraction | 0.0169 | ATP1A1, ATP2A2, DSP, JUP |
| GO:BP regulation of blood circulation | 0.0225 | ATP1A1, ATP2A2, DSP, FGA, JUP |
| GO:BP regulation of muscle contraction | 0.0326 | ATP1A1, ATP2A2, DSP, JUP |
| GO:BP cardiac muscle cell action potential | 0.0326 | ATP1A1, ATP2A2, DSP, JUP |
| GO:BP cardiac conduction | 0.043 | ATP1A1, ATP2A2, DSP, JUP |
| GO:BP keratinocyte differentiation | 0.0434 | DSP, KRT17, MACROH2A1, PKP1, PLEC, TGM1 |

### STRING and hu.MAP

STRING provides a compact known interaction core involving DSP, JUP, PKP1, PLEC, and TGM1, with particularly strong known links among DSP, JUP, and PKP1 and additional links from PKP1 to PLEC and TGM1. ATP2A2 is connected to ATP1A1 and DSP, supporting a bridge between calcium handling, membrane physiology, and epithelial junction biology. STRING also connects RPL6 with CCT7 and SRP68, indicating smaller translation, chaperone, or protein-targeting relationships. The supplementary phenotype enrichments for palmoplantar keratoderma, nail abnormalities, alopecia, fragile or blistering skin, and epidermal morphology (15 supplementary STRING terms; within-query FDR 0.00038–0.0178) are consistent with the desmosomal and keratinocyte interpretation, but they are not global GO or KEGG evidence. hu.MAP independently places JUP, DSP, TGM1, PKP1, and POF1B together in several epithelial complexes (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1) (hu.MAP huMAP3_05845.1) (hu.MAP huMAP3_08595.1), while ATP1A1 and ATP2A2 share a transport-related complex (hu.MAP huMAP3_10473.1). MACROH2A1 with SUPT16H (hu.MAP huMAP3_10862.1), AKR1B10 with FGA (hu.MAP huMAP3_10678.1), and ATP2A2 with PRKDC (hu.MAP huMAP3_09592.1) suggest additional chromatin, secreted or hepatic, and cellular stress or membrane-associated connections. Thus, the module contains a well-supported epithelial junction core plus peripheral genes connected through calcium handling, secretion, chromatin, translation, and cellular maintenance.

**STRING interactions (score >= 0.7)**: 9 of 378 gene pairs: ATP1A1–ATP2A2 (0.82); ATP2A2–DSP (0.704); CCT7–RPL6 (0.793); DSP–JUP (0.999); DSP–PKP1 (0.995); JUP–PKP1 (0.946); PKP1–PLEC (0.722); PKP1–TGM1 (0.734); RPL6–SRP68 (0.904)
**STRING functional enrichment (supplementary, within-query FDR)**: HPO Palmoplantar keratoderma (FDR = 0.00038, 8 genes); HPO Nail dystrophy (FDR = 0.00038, 7 genes); HPO Abnormality of the nail (FDR = 0.0041, 8 genes); HPO Alopecia (FDR = 0.0062, 6 genes); HPO Abnormal blistering of the skin (FDR = 0.0067, 5 genes); HPO Fragile skin (FDR = 0.0073, 4 genes); HPO Nail dysplasia (FDR = 0.0073, 5 genes); HPO Abnormal epidermal morphology (FDR = 0.0077, 5 genes); HPO Finger syndactyly (FDR = 0.0105, 5 genes); HPO 2-3 finger syndactyly (FDR = 0.0132, 3 genes); HPO Alopecia universalis (FDR = 0.0132, 3 genes); HPO 4-5 finger syndactyly (FDR = 0.0132, 3 genes); HPO Abnormal dermoepidermal hemidesmosome morphology (FDR = 0.0132, 3 genes); HPO Abnormality of the hand (FDR = 0.0133, 11 genes); HPO Epidermal acanthosis (FDR = 0.0178, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09125.1 (JUP, DSP, TGM1, PKP1, POF1B; 5/53); huMAP3_09929.1 (JUP, DSP, TGM1, PKP1, POF1B; 5/75); huMAP3_05845.1 (JUP, DSP, TGM1, PKP1; 4/24); huMAP3_08595.1 (JUP, DSP, TGM1, PKP1; 4/25); huMAP3_10473.1 (ATP1A1, ATP2A2; 2/24); huMAP3_10862.1 (MACROH2A1, SUPT16H; 2/33); huMAP3_10678.1 (AKR1B10, FGA; 2/71); huMAP3_09592.1 (ATP2A2, PRKDC; 2/95)

### Novelty

This is not a wholly new molecular program: the central DSP–JUP–PKP1 relationship is already well established in STRING, and the same proteins recur in multiple hu.MAP epithelial complexes (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1) (hu.MAP huMAP3_05845.1) (hu.MAP huMAP3_08595.1). The keratinocyte differentiation signal (GO:BP keratinocyte differentiation; q_global = 0.0434) and the skin and nail phenotypes (15 supplementary STRING terms; within-query FDR 0.00038–0.0178) also agree with established biology. The potentially novel result is the reproducible co-abundance of this epithelial junction program with ATP1A1, ATP2A2, GBP6, FGA, chromatin-related genes, and other peripheral genes across the cell line and cervix_uterine tissue pair. That cross-context organization could reflect a shared epithelial state, tissue composition, or sample-level biology, but the supplied evidence does not establish a new physical complex or a new disease mechanism. Absence of some edges from STRING or hu.MAP should be treated as missing prior knowledge rather than proof of novelty.

**Hypothesis.** Mechanistic hypothesis: the module represents a shared epithelial integrity state in which desmosomal components and intermediate-filament organizers maintain cell-cell adhesion and barrier resilience, while ATP2A2 and ATP1A1 coordinate intracellular calcium and membrane ion gradients that support junctional stability and epithelial differentiation. TGM1 may reinforce the differentiated epithelial envelope, and KRT17 may mark a basal or stress-responsive epithelial state. GBP6 could indicate interferon-responsive or inflammatory context, while FGA may reflect blood or tissue-fluid contribution rather than a core epithelial mechanism. This hypothesis predicts that module activity will track epithelial cell abundance or differentiation and will be associated with desmosome organization, calcium homeostasis, and tissue barrier phenotypes. It remains a hypothesis because co-abundance does not demonstrate physical interaction, directionality, or causal regulation.

### Important genes

#### DSP

- **Related proteins** (co-abundance neighbors): GBP6 (0.83), LLGL2 (0.80); STRING partners: ATP2A2 (0.704), JUP (0.999), PKP1 (0.995)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1, huMAP3_05845.1, huMAP3_08595.1
- **Function (MyGene.info)**: desmoplakin. This gene encodes a protein that anchors intermediate filaments to desmosomal plaques and forms an obligate component of functional desmosomes. Mutations in this gene are the cause of several cardiomyopathies and keratodermas, including skin fragility-woolly hair syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016].
- **Diseases (Open Targets)**: arrhythmogenic cardiomyopathy with wooly hair and keratoderma (0.841); arrhythmogenic right ventricular dysplasia 8 (0.812); arrhythmogenic right ventricular cardiomyopathy (0.760); lethal acantholytic epidermolysis bullosa (0.745); cardiomyopathy, dilated, with wooly hair, keratoderma, and tooth agenesis (0.741)
- **Europe PMC papers**: 17350
- **Why important**: DSP is the clearest structural anchor of the module. It has the strongest supplied literature support among the selected genes, is located at cell junctions, is enriched in esophageal and skin tissue and in multiple epithelial cell types, and participates in every globally corrected term (6 globally significant GO/KEGG terms, q_global 0.0169–0.0434; see the table). It is also connected in STRING to JUP, PKP1, and ATP2A2 and occurs in several hu.MAP epithelial complexes (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1) (hu.MAP huMAP3_05845.1) (hu.MAP huMAP3_08595.1). Its disease associations include cardiomyopathy, keratoderma, skin fragility, and epidermolysis bullosa.
- **Conclusion**: Established conclusion: DSP is a central epithelial desmosome and tissue-integrity gene and is the strongest candidate for defining the module. Hypothesis: variation in DSP abundance may organize much of the observed co-abundance pattern by marking epithelial junctional state.

#### JUP

- **Related proteins** (co-abundance neighbors): GBP6 (0.92); STRING partners: DSP (0.999), PKP1 (0.946)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1, huMAP3_05845.1, huMAP3_08595.1
- **Function (MyGene.info)**: junction plakoglobin. This gene encodes a major cytoplasmic protein which is the only known constituent common to submembranous plaques of both desmosomes and intermediate junctions. This protein forms distinct complexes with cadherins and desmosomal cadherins and is a member of the catenin family since it contains a distinct repeating amino acid motif called the armadillo repeat. Mutation in this gene has been associa…
- **Diseases (Open Targets)**: Naxos disease (0.784); arrhythmogenic right ventricular dysplasia 12 (0.755); arrhythmogenic right ventricular cardiomyopathy (0.597); lethal acantholytic epidermolysis bullosa (0.383); familial isolated arrhythmogenic ventricular dysplasia, biventricular form (0.370)
- **Europe PMC papers**: 3429
- **Why important**: JUP is a junctional plakoglobin shared by desmosomal and intermediate junction plaques. It is tissue enhanced in esophagus and skin, enriched across epithelial cell types, detected in cervix_uterine, and participates in the muscle, circulation, cardiac, and keratinocyte terms (6 globally significant GO/KEGG terms, q_global 0.0169–0.0434; see the table). Its nearly definitive STRING relationship with DSP and strong relationship with PKP1, together with repeated hu.MAP membership (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1) (hu.MAP huMAP3_05845.1) (hu.MAP huMAP3_08595.1), places it in the module's known adhesion core. Its disease associations include Naxos disease and arrhythmogenic cardiomyopathy.
- **Conclusion**: Established conclusion: JUP is a major molecular bridge between epithelial adhesion and cardiac structural phenotypes. Hypothesis: its co-abundance may couple epithelial junction remodeling with the cardiac and muscle annotations observed in the enrichment results.

#### PKP1

- **Related proteins** (co-abundance neighbors): GBP6 (0.88); STRING partners: DSP (0.995), JUP (0.946), PLEC (0.722), TGM1 (0.734)
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Nucleoplasm, Plasma membrane; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1, huMAP3_05845.1, huMAP3_08595.1
- **Function (MyGene.info)**: plakophilin 1. This gene encodes a member of the arm-repeat (armadillo) and plakophilin gene families. Plakophilin proteins contain numerous armadillo repeats, localize to cell desmosomes and nuclei, and participate in linking cadherins to intermediate filaments in the cytoskeleton. This protein may be involved in molecular recruitment and stabilization during desmosome formation. Mutations in this gene have bee…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex due to plakophilin deficiency (0.769); seborrheic keratosis (0.385); skin aging (0.334); skin disorder (0.252); congenital anomaly of cardiovascular system (0.241)
- **Europe PMC papers**: 1163
- **Why important**: PKP1 is a desmosomal armadillo-family protein involved in desmosome assembly, maintenance, and cell-cell adhesion. It is enriched in esophagus, skin, and vagina, appears in epithelial cell types, is detected in cervix_uterine, and contributes to the keratinocyte term (GO:BP keratinocyte differentiation; q_global = 0.0434). STRING links PKP1 strongly to DSP and JUP and additionally to PLEC and TGM1, while hu.MAP places it in several epithelial complexes (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1) (hu.MAP huMAP3_05845.1) (hu.MAP huMAP3_08595.1). Its disease associations include epidermolysis bullosa simplex and skin-fragility syndromes.
- **Conclusion**: Established conclusion: PKP1 is a core epithelial desmosome component that reinforces the structural interpretation. Hypothesis: PKP1 may be a sensitive marker of the differentiated or mechanically stressed epithelial state shared by the two tissue contexts.

#### ATP2A2

- **Related proteins** (co-abundance neighbors): GBP6 (0.92), PRKDC (0.80); STRING partners: ATP1A1 (0.82), DSP (0.704)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10473.1, huMAP3_09592.1
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darie…
- **Diseases (Open Targets)**: Darier disease (0.823); acrokeratosis verruciformis (0.663); neurodegenerative disease (0.507); hereditary disease (0.416); schizophrenia (0.406)
- **Europe PMC papers**: 9327
- **Why important**: ATP2A2 encodes a SERCA calcium pump and is the most prominent calcium-handling gene in the module. It participates in all of the globally corrected muscle, circulation, and cardiac terms (5 globally significant GO/KEGG terms, q_global 0.0169–0.043; see the table), is connected by STRING to ATP1A1 and DSP, and appears in hu.MAP complexes (hu.MAP huMAP3_10473.1) and (hu.MAP huMAP3_09592.1). HPA associates it with heart muscle, skeletal muscle, and tongue, while its annotations include calcium homeostasis, cell adhesion, epidermis development, and heart rate. Its disease association with Darier disease directly links calcium regulation to epithelial pathology.
- **Conclusion**: Established conclusion: ATP2A2 supplies a credible calcium-regulatory component that connects epithelial biology with the muscle and cardiac enrichment signal. Hypothesis: altered calcium sequestration could influence desmosome stability or epithelial differentiation within this module.

#### TGM1

- **Related proteins** (co-abundance neighbors): SACK1A (0.85), RPL6 (0.81), CCT7 (0.81); STRING partners: PKP1 (0.734)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles, Plasma membrane; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1, huMAP3_05845.1, huMAP3_08595.1
- **Function (MyGene.info)**: transglutaminase 1. The protein encoded by this gene is a membrane protein that catalyzes the addition of an alkyl group from an akylamine to a glutamine residue of a protein, forming an alkylglutamine in the protein. This protein alkylation leads to crosslinking of proteins and catenation of polyamines to proteins. This gene contains either one or two copies of a 22 nt repeat unit in its 3' UTR. Mutations in this ge…
- **Diseases (Open Targets)**: lamellar ichthyosis (0.721); autosomal recessive congenital ichthyosis (0.714); congenital reticular ichthyosiform erythroderma (0.504); Abnormality of the skin (0.482); ichthyosis (0.456)
- **Europe PMC papers**: 2060
- **Why important**: TGM1 is a membrane-associated transglutaminase involved in protein crosslinking, cell-envelope organization, and keratinocyte differentiation. It contributes to (GO:BP keratinocyte differentiation; q_global = 0.0434), is enriched in esophagus and several epithelial cell types, is detected in cervix_uterine, and is present in four hu.MAP epithelial complexes (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1) (hu.MAP huMAP3_05845.1) (hu.MAP huMAP3_08595.1). STRING links it to PKP1, and the supplementary phenotype terms repeatedly associate it with keratoderma, nail abnormalities, alopecia, and epidermal morphology (4 supplementary STRING terms; within-query FDR 0.00038–0.0062) and (9 supplementary STRING terms; within-query FDR 0.0073–0.0178). Its disease associations include lamellar ichthyosis and other congenital ichthyoses.
- **Conclusion**: Established conclusion: TGM1 is a strong marker of epithelial envelope maturation and keratinocyte differentiation. Hypothesis: TGM1 may act downstream of the junctional program to stabilize a differentiated, mechanically resilient surface barrier.

## Module 9

**Tissue pair**: cell line and cervix_uterine  
**Genes (34)**: LAP3, ARPC5L, CACNA1F, CTSH, CBR3, CCDC6, CLIC3, CNDP2, COTL1, CRYBG1, EZR, FHIT, GYG1, GNAS, GNAS, GPAT3, GPRC5B, SLC2A1, HSPA4L, CAST, IGHM, MARCKS, MGLL, ALDH6A1, MVP, NDUFS2, PDLIM5, RPL12, S100A11, SERPINB6, STOM, ACAA2, TKT, TRADD

### Function

This is a 34-gene, 35-edge co-abundance module, but no GO or KEGG term passed global correction (globally significant GO/KEGG terms: 0). Therefore, no pathway-level function should be claimed as statistically enriched. The gene annotations instead suggest a mixed program involving membrane and cytoskeletal organization, ion and glucose transport, mitochondrial and lipid metabolism, proteolysis, stress responses, and epithelial or immune-associated biology. CACNA1F is the dominant network hub, with degree 28 and weighted strength 25.61; its retinal calcium-channel biology does not by itself establish a calcium-signaling module in cervix or cell-line samples. The strongest biological interpretation is therefore a shared abundance state involving membrane-associated epithelial features, cellular metabolism, and variable immune or blood-cell contribution, rather than a single demonstrated molecular pathway.

**Cell composition.** HPA annotates 33 genes. The module is not predominantly a plasma or secreted-protein module: only 2 genes are classified as secreted, with IGHM representing an immunoglobulin component. Most genes are intracellular or membrane-associated. Expression specificity is mixed, including 14 genes with low tissue specificity, 12 tissue-enhanced genes, 4 group-enriched genes, and 3 tissue-enriched genes. The recurring single-cell signals for esophageal apical and suprabasal cells, together with epithelial-associated genes such as CLIC3, CRYBG1, EZR, CAST, S100A11, and MARCKS, support an epithelial or barrier-cell component. There is also a blood or immune contribution: HPA reports immune-cell enhancement, group enrichment, or enrichment across part of the module, with recurring monocyte, eosinophil, neutrophil, dendritic-cell, and B-cell signals. IGHM is especially consistent with B-cell or plasma-cell material, while CTSH, COTL1, TKT, MARCKS, and STOM are compatible with myeloid or blood-cell contributions. HPA protein detection in cervix is detected for 25 genes and not detected for 9; there is no matching cell-line tissue measurement. Thus, the shared module may partly reflect common epithelial cell states and partly shared sample composition or infiltrating blood cells. It should not be interpreted as a uniformly expressed housekeeping program, although several broadly expressed metabolic, translation, and signaling genes are present.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supplies only 3 high-confidence interactions among 561 possible pairs: ACAA2–ALDH6A1, MGLL–NDUFS2, and SLC2A1–STOM. These links provide limited support for local biochemical relationships involving mitochondrial or lipid metabolism and membrane glucose or ion-transport biology, but they do not connect most module members. There is no STRING functional-enrichment result. hu.MAP identifies one relevant complex, C1, containing CTSH and S100A11 among 75 listed complex members; only 2 module genes occur in that complex. This is evidence that those two proteins can participate in a known larger complex context, not evidence that the whole module is one physical complex. Overall, the external interaction resources support a few known relationships embedded in a largely weakly connected co-abundance structure.

**STRING interactions (score >= 0.7)**: 3 of 561 gene pairs: ACAA2–ALDH6A1 (0.957); MGLL–NDUFS2 (0.966); SLC2A1–STOM (0.88)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09929.1 (CTSH, S100A11; 2/75)

### Novelty

The module appears potentially novel as a cross-context co-abundance pattern because the supplied STRING and hu.MAP evidence does not define a previously recognized module containing most of these genes, and no globally significant GO or KEGG theme identifies an established pathway-level label. However, this is not proof of discovery: many individual genes and biological relationships are already well studied, and the observed pattern could arise from shared epithelial composition, blood-cell admixture, technical effects, or correlated abundance of otherwise unrelated proteins. The unusual inclusion of a retinal calcium-channel gene as the principal network hub alongside epithelial, metabolic, immune, and housekeeping-associated genes makes the module biologically interesting but also argues for validation. Novelty should therefore be described as a candidate new cross-tissue co-abundance association, not as a new molecular complex or newly discovered pathway.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular-state mixture in which epithelial membrane architecture and adhesion are coupled to altered nutrient, lipid, mitochondrial, and ion-transport demands, with variable contribution from blood or immune cells. In this model, CACNA1F may act as a statistical abundance anchor rather than a proven functional driver; membrane and cytoskeletal proteins such as EZR, STOM, and MARCKS could track changes in cell surface organization, while SLC2A1, MGLL, NDUFS2, ACAA2, and ALDH6A1 track energy and lipid handling. CTSH, S100A11, and IGHM may mark lysosomal, epithelial, and immune-cell composition components. This hypothesis predicts that cell-resolved measurements and independent cohorts will separate an epithelial core from blood-cell-associated genes and will determine whether CACNA1F is functionally active or merely correlated with the shared sample state.

### Important genes

#### CACNA1F

- **Related proteins** (co-abundance neighbors): HSPA4L (0.99), STOM (0.98), CCDC6 (0.97), ARPC5L (0.97), RPL12 (0.96), NDUFS2 (0.96), GYG1 (0.96), IGHM (0.96), CTSH (0.95), CRYBG1 (0.95), ACAA2 (0.94), MARCKS (0.93), ALDH6A1 (0.93), SLC2A1 (0.90), CNDP2 (0.90), TKT (0.90), SERPINB6 (0.90), CLIC3 (0.90), LAP3 (0.89), GNAS (0.89), GNAS (0.89), TRADD (0.88), MVP (0.88), CBR3 (0.87), CAST (0.87), PDLIM5 (0.86), EZR (0.85), S100A11 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium voltage-gated channel subunit alpha1 F. This gene encodes a multipass transmembrane protein that functions as an alpha-1 subunit of the voltage-dependent calcium channel, which mediates the influx of calcium ions into the cell. The encoded protein forms a complex of alpha-1, alpha-2/delta, beta, and gamma subunits in a 1:1:1:1 ratio. Mutations in this gene can cause X-linked eye disorders, including congenital stationary night blindness…
- **Diseases (Open Targets)**: congenital stationary night blindness 2A (0.803); Aland island eye disease (0.735); X-linked cone-rod dystrophy 3 (0.665); cone-rod dystrophy (0.646); congenital stationary night blindness (0.644)
- **Europe PMC papers**: 1115
- **Why important**: CACNA1F is the central network hub, with degree 28 and weighted strength 25.61, connecting to many otherwise sparsely connected genes. Its established function is as the alpha subunit of a voltage-dependent calcium channel involved in calcium influx and visual perception. HPA places it in retina and photoreceptor-related cell types, and its disease associations include inherited retinal disorders. It has substantial literature volume, but no STRING partner or hu.MAP complex support in this module.
- **Conclusion**: Established evidence supports CACNA1F as the module's strongest statistical connector and as a retinal calcium-channel gene. It does not establish a cervix-specific calcium-channel mechanism. The conclusion is that CACNA1F is important for network structure, but its mechanistic role in this module remains a hypothesis requiring replication and cell-type-resolved validation.

#### GPRC5B

- **Related proteins** (co-abundance neighbors): MGLL (0.95), GPAT3 (0.93), CAST (0.87), COTL1 (0.82), EZR (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein-coupled receptor class C group 5 member B. This gene encodes a member of the type 3 G protein-coupled receptor family. Members of this superfamily are characterized by a signature 7-transmembrane domain motif. The encoded protein may modulate insulin secretion and increased protein expression is associated with type 2 diabetes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2015].
- **Diseases (Open Targets)**: megalencephalic leukoencephalopathy with subcortical cysts 3 (0.436); Abnormality of the skeletal system (0.401); megalencephalic leukoencephalopathy with subcortical cysts (0.372); osteoarthritis, knee (0.318); osteoarthritis (0.312)
- **Europe PMC papers**: 727
- **Why important**: GPRC5B is a local connector linking MGLL, GPAT3, CAST, COTL1, and EZR. Its known biology includes class C G-protein-coupled receptor family membership, intracellular signaling, and cell-volume homeostasis, with reported association to insulin secretion and type two diabetes. Its neighbors span lipid synthesis, lipid hydrolysis, actin or membrane organization, and immune-associated biology, making it useful for interpreting the module's mixed signal.
- **Conclusion**: Established evidence supports GPRC5B as a network bridge between metabolic and membrane or cytoskeletal genes. A possible interpretation is that it links nutrient or lipid state to epithelial-cell surface organization, but the module does not prove that GPRC5B mediates this coupling.

#### EZR

- **Related proteins** (co-abundance neighbors): CACNA1F (0.85), GPRC5B (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ezrin. The cytoplasmic peripheral membrane protein encoded by this gene functions as a protein-tyrosine kinase substrate in microvilli. As a member of the ERM protein family, this protein serves as an intermediate between the plasma membrane and the actin cytoskeleton. This protein plays a key role in cell surface structure adhesion, migration and organization, and it has been implicated in various human…
- **Diseases (Open Targets)**: hair color (0.477); non-small cell lung carcinoma (0.397); lung adenocarcinoma (0.382); autosomal recessive non-syndromic intellectual disability (0.370); glaucoma (0.347)
- **Europe PMC papers**: 4982
- **Why important**: EZR connects the hub region to GPRC5B and is annotated as a plasma-membrane to actin-cytoskeleton linker involved in cell shape, adhesion, migration, and surface organization. HPA detects it in cervix and in several epithelial cell types, including esophageal apical and ocular epithelial cells. Its disease literature includes cancer and other tissue-organization phenotypes, giving it strong contextual relevance for epithelial samples.
- **Conclusion**: Established evidence supports EZR as a plausible epithelial structural component of the module. The module is consistent with coordinated membrane and cytoskeletal remodeling, but it does not demonstrate that EZR is upstream or causative.

#### MGLL

- **Related proteins** (co-abundance neighbors): GPRC5B (0.95); STRING partners: NDUFS2 (0.966)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: monoglyceride lipase. This gene encodes a serine hydrolase of the AB hydrolase superfamily that catalyzes the conversion of monoacylglycerides to free fatty acids and glycerol. The encoded protein plays a critical role in several physiological processes including pain and nociperception through hydrolysis of the endocannabinoid 2-arachidonoylglycerol. Expression of this gene may play a role in cancer tumorigenesis and …
- **Diseases (Open Targets)**: smoking initiation (0.348); prostate carcinoma (0.344); color vision disorder (0.278); Thrombophlebitis (0.236); phlebitis (0.236)
- **Europe PMC papers**: 3868
- **Why important**: MGLL connects to GPRC5B and has a high-confidence STRING relationship with NDUFS2. It hydrolyzes monoacylglycerides, participates in lipid and arachidonate metabolism, and can influence inflammatory signaling. HPA places it in several cell types, including alveolar cells, cardiomyocytes, esophageal apical cells, and platelets, with immune-cell enhancement in intermediate monocytes. Its disease and cancer literature provides substantial biological context.
- **Conclusion**: Established evidence supports MGLL as a metabolic and potentially inflammatory component, with an externally supported link to mitochondrial biology through NDUFS2. It is reasonable to hypothesize that lipid turnover contributes to the shared module state, but the co-abundance pattern does not establish a specific endocannabinoid or inflammatory mechanism.

#### SLC2A1

- **Related proteins** (co-abundance neighbors): CACNA1F (0.90); STRING partners: STOM (0.88)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 2 member 1. This gene encodes a major glucose transporter in the mammalian blood-brain barrier. The encoded protein is found primarily in the cell membrane and on the cell surface, where it can also function as a receptor for human T-cell leukemia virus (HTLV) I and II. Mutations in this gene have been found in a family with paroxysmal exertion-induced dyskinesia. [provided by RefSeq, Apr 2013].
- **Diseases (Open Targets)**: encephalopathy due to GLUT1 deficiency (0.852); childhood onset GLUT1 deficiency syndrome 2 (0.833); dystonia 9 (0.804); hereditary cryohydrocytosis with reduced stomatin (0.778); idiopathic generalized epilepsy (0.757)
- **Europe PMC papers**: 14405
- **Why important**: SLC2A1 is connected to the hub region and has a high-confidence STRING relationship with STOM. It encodes a major glucose transporter and is annotated for membrane transport and responses associated with hypoxia and energy demand. HPA highlights placenta and several trophoblast or epithelial-related cell types, while its disease associations include GLUT1 deficiency syndromes. Its strong literature base and direct transport function make it a useful metabolic anchor.
- **Conclusion**: Established evidence supports SLC2A1 as a glucose-transport component that could report cellular energetic state. The module is compatible with coordinated nutrient and membrane remodeling, but it does not show that glucose transport drives the co-abundance pattern.

#### CTSH

- **Related proteins** (co-abundance neighbors): CACNA1F (0.95); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles, Cytosol, Cytoplasmic bodies; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09929.1
- **Function (MyGene.info)**: cathepsin H. The protein encoded by this gene is a lysosomal cysteine proteinase important in the overall degradation of lysosomal proteins. It is composed of a dimer of disulfide-linked heavy and light chains, both produced from a single protein precursor. The encoded protein, which belongs to the peptidase C1 protein family, can act both as an aminopeptidase and as an endopeptidase. Increased expression of t…
- **Diseases (Open Targets)**: type 1 diabetes mellitus (0.558); Alzheimer disease (0.549); skin cancer (0.494); basal cell carcinoma (0.486); dementia (0.457)
- **Europe PMC papers**: 2242
- **Why important**: CTSH is connected to the hub region and is one of the two module members in the hu.MAP complex C1 with S100A11. It is a lysosomal cysteine protease with aminopeptidase and endopeptidase activity, and its annotations include proteolysis, adaptive immune response, and cytotoxicity-related biology. HPA detects it in cervix, multiple immune cell types, and several epithelial or stromal populations. Its position at the interface of lysosomal, epithelial, and immune contexts makes it important for composition-aware interpretation.
- **Conclusion**: Established evidence supports CTSH as a lysosomal and immune or epithelial-context marker, and hu.MAP provides limited complex-level support with S100A11. A plausible hypothesis is that CTSH reflects altered turnover or immune-cell admixture, but the module cannot distinguish those explanations.

## Module 10

**Tissue pair**: cell line and cervix_uterine  
**Genes (27)**: AP1B1, ATP5F1A, BAIAP2, CANX, CPM, CLTC, CNOT12, CRYAB, SORD, DNMT1, DPP3, H1-2, H1-4, KRT23, LDHA, LDHB, MDH1, NBEAL2, PAEP, PHPT1, PHGDH, SPTBN1, TMEM214, TNFSF13B, TNFAIP2, WDR26, XPO1

### Function

The strongest functional interpretation is coupled amino-acid and redox metabolism, centered on cysteine and methionine metabolism (KEGG Cysteine and methionine metabolism - Homo sapiens (human); q_global = 0.0194). The globally corrected KEGG term contains PHGDH, LDHA, LDHB, MDH1, and DNMT1, linking serine-associated biosynthesis, glycolytic lactate production, cytosolic malate metabolism, and DNA methylation maintenance. The module also contains proteins involved in vesicle trafficking and endocytosis, chromatin organization, protein folding, cytoskeletal organization, proteolysis, and immune signaling. Because only (KEGG Cysteine and methionine metabolism - Homo sapiens (human); q_global = 0.0194) passed global correction, these additional functions should be treated as biological context rather than equivalent enrichment conclusions. The network is sparse and is dominated by a highly connected TNFSF13B-centered co-abundance pattern, with smaller links involving XPO1, TMEM214, PHGDH, PAEP, and CNOT12. This architecture supports a composite module rather than a single compact molecular complex.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only TNFSF13B and PAEP are explicitly secreted, while most members are intracellular or membrane-associated. It is also not uniformly blood-cell specific, because many genes have low immune-cell specificity. Nevertheless, HPA evidence shows recurrent enrichment in neutrophils and other myeloid or blood-related populations, including TNFSF13B, NBEAL2, H1-2, H1-4, TNFAIP2, CPM, and PAEP. Several genes are enhanced in epithelial or reproductive tissues and cell types, including cervix, endometrial glandular cells, syncytiotrophoblasts, and trophoblast-related populations. The shared signal may therefore reflect a mixture of epithelial or reproductive-tissue biology with variable immune or blood-cell contribution. The broad tissue distribution of many genes also makes a housekeeping or general cellular-state component plausible. Protein detection in cervix is present for many members, whereas the cell-line protein-detection summary provides no discriminatory evidence.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Cysteine and methionine metabolism - Homo sapiens (human) | 0.0194 | DNMT1, LDHA, LDHB, MDH1, PHGDH |

### STRING and hu.MAP

STRING provides only a small set of high-confidence pairwise relationships within the module: AP1B1 with CLTC, H1-2 with H1-4, and PHGDH with XPO1. There is no STRING functional-enrichment result, so STRING does not independently support a shared pathway. hu.MAP provides stronger evidence for recurring subcomplexes: CPM with SORD occurs in a complex containing RALA (hu.MAP huMAP3_04177.1); LDHA with LDHB occurs in several lactate-dehydrogenase-related complexes containing ACADM and, in some complexes, LDHC, LDHAL6A, TMEM19, or SLC24A3 (hu.MAP huMAP3_06798.1) (hu.MAP huMAP3_09010.1) (hu.MAP huMAP3_14812.1) (hu.MAP huMAP3_12061.1); and CLTC with AP1B1 occurs in several large vesicle-trafficking complexes (hu.MAP huMAP3_10762.1) (hu.MAP huMAP3_12918.1) (hu.MAP huMAP3_12394.1). These observations support genuine metabolic and clathrin-adaptor components, but the repeated presence of only two module members in large complexes means they do not establish that the complete module is a single physical complex. The absence of hu.MAP or STRING support for many other co-abundant pairs indicates that co-abundance extends beyond previously catalogued physical interactions.

**STRING interactions (score >= 0.7)**: 3 of 351 gene pairs: AP1B1–CLTC (0.917); H1-2–H1-4 (0.826); PHGDH–XPO1 (0.786)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04177.1 (CPM, SORD; 2/3); huMAP3_06798.1 (LDHA, LDHB; 2/3); huMAP3_09010.1 (LDHA, LDHB; 2/5); huMAP3_14812.1 (LDHA, LDHB; 2/5); huMAP3_12061.1 (LDHA, LDHB; 2/6); huMAP3_10762.1 (CLTC, AP1B1; 2/62); huMAP3_12918.1 (CLTC, AP1B1; 2/62); huMAP3_12394.1 (CLTC, AP1B1; 2/98)

### Novelty

This module should not be called a newly discovered molecular complex. Parts of it recapitulate established biology: LDHA and LDHB are represented in known lactate-dehydrogenase-related complexes (hu.MAP huMAP3_06798.1) (hu.MAP huMAP3_09010.1) (hu.MAP huMAP3_14812.1) (hu.MAP huMAP3_12061.1), CLTC and AP1B1 are represented in known vesicle-trafficking complexes (hu.MAP huMAP3_10762.1) (hu.MAP huMAP3_12918.1) (hu.MAP huMAP3_12394.1), H1-2 and H1-4 have a known STRING relationship, and PHGDH with XPO1 has a known STRING relationship. The potentially novel aspect is the conserved co-abundance of the broader gene combination across cell line and cervix_uterine, particularly the association of a TNFSF13B-centered network with metabolic, trafficking, chromatin, epithelial, and reproductive-tissue markers. However, absence from STRING or hu.MAP is not proof of novelty. A defensible conclusion is that the cross-tissue co-abundance pattern is a candidate novel systems-level association, while its constituent molecular functions are largely established. Independent replication, perturbation, and cell-composition analyses would be needed to establish biological novelty.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program in which immune or epithelial reproductive-tissue signals coincide with altered metabolic and secretory demand. TNFSF13B may mark the immune-signaling component, while PHGDH, LDHA, LDHB, and MDH1 support carbon, redox, and amino-acid metabolism; CLTC and AP1B1 support receptor trafficking and endocytosis; and XPO1 and DNMT1 connect the state to nuclear transport and epigenetic maintenance. PAEP, CPM, TNFAIP2, and NBEAL2 may represent tissue- or cell-type-specific contributions from reproductive epithelium, myeloid cells, or platelet-related biology. This hypothesis predicts that the apparent module will weaken after controlling for immune and epithelial cell composition, but that a residual metabolic and trafficking program may remain in the relevant cells.

### Important genes

#### TNFSF13B

- **Related proteins** (co-abundance neighbors): NBEAL2 (1.00), H1-4 (1.00), CANX (0.99), PHPT1 (0.99), ATP5F1A (0.99), AP1B1 (0.97), LDHB (0.97), KRT23 (0.96), DPP3 (0.92), WDR26 (0.92), H1-2 (0.88), BAIAP2 (0.87), TNFAIP2 (0.87), CPM (0.85), MDH1 (0.85), XPO1 (0.84), SORD (0.83), PHGDH (0.81), LDHA (0.80), CRYAB (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TNF superfamily member 13b. The protein encoded by this gene is a cytokine that belongs to the tumor necrosis factor (TNF) ligand family. This cytokine is a ligand for receptors TNFRSF13B/TACI, TNFRSF17/BCMA, and TNFRSF13C/BAFFR. This cytokine is expressed in B cell lineage cells, and acts as a potent B cell activator. It has been also shown to play an important role in the proliferation and differentiation of B cells. Alter…
- **Diseases (Open Targets)**: systemic lupus erythematosus (0.622); lupus nephritis (0.545); IgA glomerulonephritis (0.382); interstitial lung disease (0.374); rheumatoid arthritis (0.357)
- **Europe PMC papers**: 3431
- **Why important**: TNFSF13B is the dominant network hub by weighted connectivity and links immune signaling to many otherwise weakly connected module members. It is a TNF-family cytokine ligand for TACI, BCMA, and BAFFR, is associated with B-cell activation and lymphocyte homeostasis, is secreted to blood, and is enhanced in immune-related cell types. Its disease associations include systemic lupus erythematosus, lupus nephritis, IgA glomerulonephritis, interstitial lung disease, and rheumatoid arthritis. The substantial literature volume supports a well-established biological role, although it has no STRING or hu.MAP relationship within this module.
- **Conclusion**: Established evidence supports TNFSF13B as an immune-signaling marker and the principal network organizer. It may explain part of the shared co-abundance pattern through immune-cell presence or cytokine-related state, but the data do not establish that TNFSF13B mechanistically regulates the other module genes.

#### PHGDH

- **Related proteins** (co-abundance neighbors): PAEP (0.92), TNFSF13B (0.81); STRING partners: XPO1 (0.786)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Plasma membrane, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglycerate dehydrogenase. This gene encodes the enzyme which is involved in the early steps of L-serine synthesis in animal cells. L-serine is required for D-serine and other amino acid synthesis. The enzyme requires NAD/NADH as a cofactor and forms homotetramers for activity. Mutations in this gene have been found in a family with congenital microcephaly, psychomotor retardation and other symptoms. Multiple alternatively …
- **Diseases (Open Targets)**: PHGDH deficiency (0.824); Neu-Laxova syndrome 1 (0.796); Neu-Laxova syndrome (0.617); neuropathy (0.516); osteomyelitis (0.494)
- **Europe PMC papers**: 5109
- **Why important**: PHGDH is one of the five genes in the sole globally significant KEGG term (KEGG Cysteine and methionine metabolism - Homo sapiens (human); q_global = 0.0194). It catalyzes an early step in L-serine biosynthesis and is directly connected to XPO1 in STRING while also connecting to PAEP in the co-abundance network. It has high literature volume and disease associations including PHGDH deficiency and Neu-Laxova syndrome. Its cervix protein detection and cell-type enhancements indicate that it may be relevant to the tissue context rather than functioning only as a generic metabolic marker.
- **Conclusion**: Established evidence supports PHGDH as a metabolic anchor of the module and as part of the globally significant cysteine-and-methionine-associated signal (KEGG Cysteine and methionine metabolism - Homo sapiens (human); q_global = 0.0194). A role in coordinating metabolic state with nuclear transport or reproductive-tissue biology is a hypothesis, not demonstrated by the supplied data.

#### LDHA

- **Related proteins** (co-abundance neighbors): TNFSF13B (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_06798.1, huMAP3_09010.1, huMAP3_14812.1, huMAP3_12061.1
- **Function (MyGene.info)**: lactate dehydrogenase A. This gene encodes the A subunit of lactate dehydrogenase enzyme which catalyzes the reversible conversion of pyruvate to lactate with the concomitant oxidation of NADH to NAD in anaerobic glycolysis. The protein is found predominantly in skeletal muscle and belongs to the lactate dehydrogenase family. Mutations in this gene have been linked to exertional myoglobinuria. The human genome contains se…
- **Diseases (Open Targets)**: glycogen storage disease due to lactate dehydrogenase M-subunit deficiency (0.755); disorder of glycogen metabolism (0.505); glycogen storage disease XV (0.505); primary hyperoxaluria (0.447); hereditary disease (0.190)
- **Europe PMC papers**: 20747
- **Why important**: LDHA is included in (KEGG Cysteine and methionine metabolism - Homo sapiens (human); q_global = 0.0194) and encodes the lactate-dehydrogenase A subunit, supporting pyruvate-to-lactate conversion and glycolytic redox balance. It is represented with LDHB in several hu.MAP complexes (hu.MAP huMAP3_06798.1) (hu.MAP huMAP3_09010.1) (hu.MAP huMAP3_14812.1) (hu.MAP huMAP3_12061.1), giving this part of the module established complex-level support. LDHA has extensive literature and disease associations involving glycogen-storage and glycolytic disorders, as well as cancer-related annotations.
- **Conclusion**: Established evidence supports LDHA as a core metabolic component and as part of known lactate-dehydrogenase-related complexes (hu.MAP huMAP3_06798.1) (hu.MAP huMAP3_09010.1) (hu.MAP huMAP3_14812.1) (hu.MAP huMAP3_12061.1). Its co-abundance with immune, trafficking, and reproductive-tissue markers may indicate shared metabolic demand, but does not demonstrate a direct regulatory connection.

#### LDHB

- **Related proteins** (co-abundance neighbors): TNFSF13B (0.97); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06798.1, huMAP3_09010.1, huMAP3_14812.1, huMAP3_12061.1
- **Function (MyGene.info)**: lactate dehydrogenase B. This gene encodes the B subunit of lactate dehydrogenase enzyme, which catalyzes the interconversion of pyruvate and lactate with concomitant interconversion of NADH and NAD+ in a post-glycolysis process. Alternatively spliced transcript variants have been found for this gene. Recent studies have shown that a C-terminally extended isoform is produced by use of an alternative in-frame translation t…
- **Diseases (Open Targets)**: glycogen storage disease due to lactate dehydrogenase H-subunit deficiency (0.724); type 2 diabetes mellitus (0.271); adverse effect (0.184); neoplasm (0.117); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 5204
- **Why important**: LDHB is included in (KEGG Cysteine and methionine metabolism - Homo sapiens (human); q_global = 0.0194), catalyzes reversible lactate and pyruvate interconversion, and is represented with LDHA in multiple hu.MAP complexes (hu.MAP huMAP3_06798.1) (hu.MAP huMAP3_09010.1) (hu.MAP huMAP3_14812.1) (hu.MAP huMAP3_12061.1). It is tissue-enhanced in heart muscle and kidney and has substantial literature volume, with disease associations involving lactate-dehydrogenase deficiency and metabolic disease. Its strong connection to the TNFSF13B-centered co-abundance pattern makes it an important bridge between the metabolic interpretation and the broader module.
- **Conclusion**: Established evidence supports LDHB as a metabolic component with known complex membership alongside LDHA (hu.MAP huMAP3_06798.1) (hu.MAP huMAP3_09010.1) (hu.MAP huMAP3_14812.1) (hu.MAP huMAP3_12061.1). The module suggests that lactate and redox metabolism may track with immune or epithelial state, but this remains an inference from co-abundance rather than proof of mechanism.

#### CLTC

- **Related proteins** (co-abundance neighbors): XPO1 (0.82), TMEM214 (0.81); STRING partners: AP1B1 (0.917)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_10762.1, huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: clathrin heavy chain. Clathrin is a major protein component of the cytoplasmic face of intracellular organelles, called coated vesicles and coated pits. These specialized organelles are involved in the intracellular trafficking of receptors and endocytosis of a variety of macromolecules.  The basic subunit of the clathrin coat is composed of three heavy chains and three light chains. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: intellectual disability, autosomal dominant 56 (0.787); cancer (0.576); hereditary disease (0.540); Alzheimer disease (0.466); neurodegenerative disease (0.465)
- **Europe PMC papers**: 2902
- **Why important**: CLTC encodes clathrin heavy chain and supports receptor-mediated endocytosis and intracellular protein transport. It is connected to XPO1 and TMEM214 in the module, has a high-confidence STRING interaction with AP1B1, and occurs with AP1B1 in several hu.MAP vesicle-trafficking complexes (hu.MAP huMAP3_10762.1) (hu.MAP huMAP3_12918.1) (hu.MAP huMAP3_12394.1). It has substantial literature and disease associations involving intellectual disability, cancer, and neurodegenerative disease. Its cervix detection and neutrophil cell-type enhancement make it relevant to both trafficking biology and possible cell-composition effects.
- **Conclusion**: Established evidence supports CLTC as the best-supported trafficking component of the module, with concordant STRING and hu.MAP evidence (hu.MAP huMAP3_10762.1) (hu.MAP huMAP3_12918.1) (hu.MAP huMAP3_12394.1). Its association with the metabolic and immune-centered portions of the module is a plausible systems-level coupling, but not an established direct interaction.

#### DNMT1

- **Related proteins** (co-abundance neighbors): XPO1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA methyltransferase 1. This gene encodes an enzyme that transfers methyl groups to cytosine nucleotides of genomic DNA. This protein is the major enzyme responsible for maintaining methylation patterns following DNA replication and shows a preference for hemi-methylated DNA. Methylation of DNA is an important component of mammalian epigenetic gene regulation. Aberrant methylation patterns are found in human tumors and a…
- **Diseases (Open Targets)**: autosomal dominant cerebellar ataxia, deafness and narcolepsy (0.806); hereditary sensory neuropathy-deafness-dementia syndrome (0.777); acute myeloid leukemia (0.623); myelodysplastic syndrome (0.615); cancer (0.612)
- **Europe PMC papers**: 30754
- **Why important**: DNMT1 is included in (KEGG Cysteine and methionine metabolism - Homo sapiens (human); q_global = 0.0194) and maintains DNA methylation after replication, providing an epigenetic dimension to the module's metabolic interpretation. It is connected to XPO1 in the co-abundance network and has extensive literature and disease associations involving hereditary neurological disease, acute myeloid leukemia, myelodysplastic syndrome, and cancer. Its cell-type enhancements include proliferative progenitor populations, making it relevant to cellular-state regulation.
- **Conclusion**: Established evidence supports DNMT1 as a DNA-methylation maintenance enzyme included in the globally significant term (KEGG Cysteine and methionine metabolism - Homo sapiens (human); q_global = 0.0194). Its co-abundance with metabolic and nuclear-transport genes may reflect coordinated proliferative or epigenetic state, but a causal metabolic-epigenetic mechanism is only a hypothesis.

## Module 11

**Tissue pair**: cell line and cervix_uterine  
**Genes (25)**: APOA1, C4BPA, CEACAM5, COL6A1, DLG1, EPHA2, EXOC7, FAM120A, FDFT1, GALNT10, GPD1L, LMO7, LYN, MVD, SERPINF1, PIP4K2C, PKP3, NAPRT, RIOK3, S100A8, S100A9, SCP2, STXBP2, TTN, TF

### Function

The module appears to combine a peripheral and epithelial structural program with inflammatory, lipid-handling, and circulating-protein biology. The primary evidence is (GO:MF long-chain fatty acid binding; q_global = 0.0177), where S100A8, S100A9, and SCP2 support long-chain fatty-acid binding, and (GO:CC cell periphery; q_global = 0.0412), where most module genes support cell-periphery localization. The network contains a C4BPA-centered set of associations, an S100A8–S100A9 pair, an APOA1–TF pair, a FDFT1–MVD cholesterol-biosynthesis pair, and an EPHA2–LYN signaling pair. These observations support a mixed module rather than a single narrowly defined pathway. STRING cell-periphery and plasma-membrane annotations (STRING Component Plasma membrane; within-query FDR = 0.0065) and (STRING Component Cell periphery; within-query FDR = 0.0065) are concordant but supplementary, not globally corrected primary evidence. The strongest biological interpretation is an epithelial or tissue-interface module influenced by inflammatory myeloid proteins and extracellular or plasma-protein carryover, with additional lipid and membrane-trafficking features.

**Cell composition.** The module is compositionally heterogeneous. It includes a substantial secreted-to-blood component, including APOA1, TF, C4BPA, SERPINF1, S100A8, and S100A9, together with extracellular-matrix protein COL6A1. HPA therefore raises the possibility that part of the shared signal reflects plasma or extracellular material rather than a single intracellular program. The blood-cell evidence is also meaningful: S100A8 and S100A9 are associated with neutrophils and monocytes, while C4BPA, LYN, and STXBP2 have immune or myeloid associations. However, the module is not predominantly a blood-cell signature. HPA instead shows strong representation of epithelial cell types, especially esophageal apical and suprabasal cells, alongside hepatocytes, enterocytes, colonocytes, and stromal or muscle-related populations. CEACAM5, PKP3, EPHA2, LMO7, and COL6A1 support epithelial junction, adhesion, or tissue-structure contributions. Cervix protein detection is present for many genes, including S100A8, S100A9, PKP3, CEACAM5, EPHA2, LYN, PIP4K2C, and several metabolic or trafficking genes, but the absence of detection for some circulating proteins cautions against treating the module as a uniform cervix-cell program. The shared cell-line and cervix signal may therefore reflect a combination of epithelial state, extracellular or plasma proteins, and variable myeloid material.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF long-chain fatty acid binding | 0.0177 | S100A8, S100A9, SCP2 |
| GO:CC cell periphery | 0.0412 | APOA1, C4BPA, CEACAM5, COL6A1, DLG1, EPHA2, EXOC7, FAM120A, GPD1L, LMO7, LYN, PIP4K2C, PKP3, S100A8, S100A9, SERPINF1, STXBP2, TF |

### STRING and hu.MAP

STRING provides only a limited set of high-confidence direct relationships within the module. The S100A8–S100A9 association is especially well established, while APOA1–TF, EPHA2–LYN, and FDFT1–MVD connect lipid transport, receptor signaling, and cholesterol synthesis. The broader STRING cell-periphery and plasma-membrane groupings (STRING Component Plasma membrane; within-query FDR = 0.0065) and (STRING Component Cell periphery; within-query FDR = 0.0065) support a common localization theme, but they do not establish that all module edges represent physical interactions. hu.MAP repeatedly places APOA1, TF, and C4BPA within large circulating-protein and complement-related complexes (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1), and (hu.MAP huMAP3_10678.1). It also places S100A8, S100A9, and PKP3 in epithelial or desmosomal complexes (hu.MAP huMAP3_09125.1) and (hu.MAP huMAP3_09929.1), while C4BPA and CEACAM5 occur together in smaller complexes (hu.MAP huMAP3_06454.1) and (hu.MAP huMAP3_02768.1). The repeated hu.MAP membership suggests that several module genes belong to known extracellular, plasma, complement, or epithelial protein environments. At the same time, many module genes lack STRING partners or hu.MAP complexes in the supplied evidence. Thus, the module is not a single experimentally established complex; it is a co-abundance structure containing several known biological neighborhoods.

**STRING interactions (score >= 0.7)**: 4 of 300 gene pairs: APOA1–TF (0.919); EPHA2–LYN (0.775); FDFT1–MVD (0.873); S100A8–S100A9 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Plasma membrane (FDR = 0.0065, 18 genes); Component Cell periphery (FDR = 0.0065, 19 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08395.1 (APOA1, TF, C4BPA; 3/43); huMAP3_09531.1 (APOA1, TF, C4BPA; 3/47); huMAP3_10101.1 (APOA1, TF, C4BPA; 3/49); huMAP3_09125.1 (S100A8, S100A9, PKP3; 3/53); huMAP3_15040.1 (APOA1, TF, C4BPA; 3/64); huMAP3_10678.1 (APOA1, TF, C4BPA; 3/71); huMAP3_09929.1 (S100A8, S100A9, PKP3; 3/75); huMAP3_06454.1 (C4BPA, CEACAM5; 2/6); huMAP3_02768.1 (C4BPA, CEACAM5; 2/7); huMAP3_07432.1 (APOA1, TF; 2/18); huMAP3_07265.1 (APOA1, TF; 2/20); huMAP3_08224.1 (APOA1, TF; 2/21); huMAP3_09434.1 (APOA1, TF; 2/33)

### Novelty

The underlying biology is not wholly new: S100A8–S100A9 inflammatory biology, APOA1–TF circulating-protein biology, complement regulation by C4BPA, epithelial adhesion involving PKP3 and CEACAM5, and cholesterol synthesis involving FDFT1 and MVD are all established. The module-level finding may nevertheless be novel because it identifies these signals as a conserved co-abundance pattern shared by a cell-line group and cervix_uterine. The supplied evidence does not provide an external module catalogue, independent cohort replication, perturbation experiment, or direct protein-interaction validation, so a claim of a completely new biological mechanism would be premature. The limited STRING connectivity and the absence of hu.MAP or STRING support for several edges suggest that some co-abundance relationships could be context-specific or driven by shared sample composition. Conversely, absence from those resources cannot prove novelty. The most defensible conclusion is that this is a potentially novel cross-context co-abundance configuration built from largely established component biology.

**Hypothesis.** Hypothesis: the conserved module reflects a tissue-interface state in which epithelial or junctional cells, extracellular matrix, circulating proteins, and recruited myeloid cells vary together. In this model, epithelial remodeling and membrane organization are represented by PKP3, CEACAM5, EPHA2, LMO7, and related peripheral genes; inflammatory or neutrophil-associated material is represented by the S100A8–S100A9 pair and parts of the LYN and STXBP2 signal; and plasma or hepatic material is represented by APOA1, TF, C4BPA, and SERPINF1. SCP2, FDFT1, and MVD could reflect coordinated lipid handling or membrane-lipid metabolism. This hypothesis predicts that the apparent conservation will weaken after controlling for epithelial content, plasma contamination, and myeloid-cell abundance, whereas a genuine tissue-interface program should remain associated with epithelial junction, inflammatory, and lipid-handling measurements in independent samples.

### Important genes

#### C4BPA

- **Related proteins** (co-abundance neighbors): RIOK3 (0.93), SERPINF1 (0.92), NAPRT (0.87), STXBP2 (0.85), PIP4K2C (0.85), GPD1L (0.84), LYN (0.83), SCP2 (0.83), FAM120A (0.83), EXOC7 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_06454.1, huMAP3_02768.1
- **Function (MyGene.info)**: complement component 4 binding protein alpha. This gene encodes a member of a superfamily of proteins composed predominantly of tandemly arrayed short consensus repeats of approximately 60 amino acids. Along with a single, unique beta-chain, seven identical alpha-chains encoded by this gene assemble into the predominant isoform of C4b-binding protein, a multimeric protein that controls activation of the complement cascade through the classica…
- **Diseases (Open Targets)**: venous thromboembolism (0.445); dengue disease (0.370); Thromboembolism (0.332); Alzheimer disease (0.246); Parkinson disease (0.243)
- **Europe PMC papers**: 1611
- **Why important**: C4BPA is the strongest network hub in the supplied graph and links inflammatory, metabolic, trafficking, and peripheral genes. It is a secreted blood protein that regulates classical complement activation, has liver and neutrophil HPA associations, and recurs with APOA1 and TF across many hu.MAP circulating-protein complexes (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1), and (hu.MAP huMAP3_10678.1). Its disease associations include thromboembolic and inflammatory conditions, and its literature base is substantial.
- **Conclusion**: Established evidence supports C4BPA as a central extracellular and complement-related component of the module. It is plausible that its network centrality reflects coordinated plasma or inflammatory material, but the co-abundance graph does not establish that C4BPA mechanistically regulates the intracellular genes connected to it.

#### S100A8

- **Related proteins** (co-abundance neighbors): PKP3 (0.96), S100A9 (0.91), DLG1 (0.90), LMO7 (0.86), GALNT10 (0.85), TF (0.84), TTN (0.82), EPHA2 (0.80), COL6A1 (0.80); STRING partners: S100A9 (0.999)
- **HPA**: Tissue enhanced; Group enriched; blood Group enriched; location Intermediate filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: S100 calcium binding protein A8. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: inborn error of immunity (0.371); Sepsis (0.122); neoplasm (0.119); breast carcinoma (0.119); gastric cancer (0.119)
- **Europe PMC papers**: 18104
- **Why important**: S100A8 is one of the most connected genes and is directly paired with S100A9 by STRING with very strong support. It is associated with neutrophils, classical monocytes, cervix, and esophageal epithelial cell types in HPA, passes both primary enrichment terms (GO:MF long-chain fatty acid binding; q_global = 0.0177) and (GO:CC cell periphery; q_global = 0.0412), and participates with S100A9 and PKP3 in hu.MAP epithelial complexes (hu.MAP huMAP3_09125.1) and (hu.MAP huMAP3_09929.1). It has extensive inflammatory literature and disease associations involving immunity, sepsis, and cancer.
- **Conclusion**: Established evidence identifies S100A8 as an inflammatory and tissue-interface marker with a known S100A8–S100A9 relationship. Its presence may indicate myeloid material, epithelial stress, or both. A direct causal role in organizing this complete module remains a hypothesis.

#### APOA1

- **Related proteins** (co-abundance neighbors): FDFT1 (0.89), TF (0.87), CEACAM5 (0.84), PIP4K2C (0.82), MVD (0.82); STRING partners: TF (0.919)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_08224.1, huMAP3_09434.1
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is a secreted HDL component and a key mediator of cholesterol efflux and plasma lipid transport. It connects to TF, FDFT1, MVD, CEACAM5, and PIP4K2C in the module, has STRING support with TF, and recurs across numerous hu.MAP circulating-protein complexes. HPA links it mainly to liver, enterocytes, hepatocytes, and blood-associated material. It has extensive literature and strong associations with lipid disorders and apolipoprotein deficiency.
- **Conclusion**: Established evidence supports APOA1 as a marker of circulating lipid transport and a bridge between plasma-protein and membrane-lipid signals. Its co-abundance with epithelial and inflammatory genes could reflect tissue exposure to plasma material or coordinated lipid handling; the data do not distinguish these explanations.

#### TF

- **Related proteins** (co-abundance neighbors): APOA1 (0.87), S100A8 (0.84); STRING partners: APOA1 (0.919)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_08224.1, huMAP3_09434.1
- **Function (MyGene.info)**: transferrin. This gene encodes a glycoprotein with an approximate molecular weight of 76.5 kDa. It is thought to have been created as a result of an ancient gene duplication event that led to generation of homologous C and N-terminal domains each of which binds one ion of ferric iron. The function of this protein is to transport iron from the intestine, reticuloendothelial system, and liver parenchymal cells t…
- **Diseases (Open Targets)**: atransferrinemia (0.776); alcohol drinking (0.492); hemochromatosis type 1 (0.471); neurodegenerative disease (0.400); urolithiasis (0.329)
- **Europe PMC papers**: 143656
- **Why important**: TF is a secreted iron-transport protein with a very large literature base and established roles in iron delivery, intracellular iron homeostasis, and antibacterial humoral defense. It connects to APOA1 and S100A8, has STRING support with APOA1, and repeatedly occurs with APOA1 and C4BPA in hu.MAP circulating-protein complexes. HPA supports a liver and hepatocyte origin while finding no immune-cell detection.
- **Conclusion**: Established evidence supports TF as a circulating hepatic protein and a plausible indicator of plasma contribution to the module. Its association with S100A8 may reflect shared sample composition or coordinated inflammatory iron biology, but a direct TF-mediated connection to S100A8 is not established here.

#### PKP3

- **Related proteins** (co-abundance neighbors): S100A8 (0.96); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cell Junctions; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: plakophilin 3. This gene encodes a member of the arm-repeat (armadillo) and plakophilin gene families. Plakophilin proteins contain numerous armadillo repeats, localize to cell desmosomes and nuclei, and participate in linking cadherins to intermediate filaments in the cytoskeleton. This protein may act in cellular desmosome-dependent adhesion and signaling pathways. Two transcript variants encoding different is…
- **Diseases (Open Targets)**: anorectal malformation (0.295); neurodegenerative disease (0.292); lymphopenia (0.111); neutropenia (0.111); hypertensive disorder (0.106)
- **Europe PMC papers**: 747
- **Why important**: PKP3 provides a strong epithelial interpretation despite having a relatively peripheral position in the graph. HPA places it in esophageal, skin, colonocyte, enterocyte, and cervix contexts and localizes it to cell junctions. Its known functions include desmosome assembly, epithelial structure maintenance, and regulation of cytokine production. It shares hu.MAP epithelial complexes with S100A8 and S100A9 (hu.MAP huMAP3_09125.1) and (hu.MAP huMAP3_09929.1), and it has disease associations involving lymphopenia, neutropenia, and developmental abnormalities.
- **Conclusion**: Established evidence supports PKP3 as an epithelial junction and desmosomal component that helps explain the cell-periphery signal (GO:CC cell periphery; q_global = 0.0412). Its connection to the inflammatory S100 proteins may indicate epithelial–myeloid co-variation, but the module does not prove direct molecular interaction.

#### STXBP2

- **Related proteins** (co-abundance neighbors): C4BPA (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntaxin binding protein 2. This gene encodes a member of the STXBP/unc-18/SEC1 family. The encoded protein is involved in intracellular trafficking, control of SNARE (soluble NSF attachment protein receptor) complex assembly, and the release of cytotoxic granules by natural killer cells. Mutations in this gene are associated with familial hemophagocytic lymphohistiocytosis. Alternatively spliced transcript variants encoding…
- **Diseases (Open Targets)**: Familial hemophagocytic lymphohistiocytosis (0.823); autoinflammatory syndrome (0.466); hereditary hemophagocytic lymphohistiocytosis (0.372); hereditary disease (0.342); Thrombocytopenia (0.153)
- **Europe PMC papers**: 1259
- **Why important**: STXBP2 links the module to regulated vesicle trafficking and immune-cell secretion. It is associated with cytotoxic-granule release, SNARE-complex assembly, neutrophil degranulation, monocyte and neutrophil-related cell types, and familial hemophagocytic lymphohistiocytosis. It is connected to the high-centrality C4BPA neighborhood and contributes to the STRING cell-periphery grouping (STRING Component Plasma membrane; within-query FDR = 0.0065) and (STRING Component Cell periphery; within-query FDR = 0.0065).
- **Conclusion**: Established evidence supports STXBP2 as a trafficking and immune-secretory component, consistent with a module containing extracellular material and myeloid signals. Its placement near C4BPA suggests coordinated abundance, not proof that STXBP2 controls complement or the wider module.

## Module 12

**Tissue pair**: cell line and cervix_uterine  
**Genes (14)**: DBNL, DSG1, EEA1, EPS15, FKBP15, EIF4E, KRT2, KRT1, ME1, NUCB2, PSPH, TUBA4A, TUBB4B, TPD52L1

### Function

The module is most consistent with a stratified epithelial differentiation and cell-junction program, accompanied by cytoskeletal, vesicular-trafficking, translation, and metabolic components. DSG1 is the central co-abundance hub, while KRT1 and KRT2 provide a coherent keratinization and intermediate-filament signal. TUBA4A and TUBB4B provide a microtubule component, and EEA1, EPS15, DBNL, and FKBP15 are compatible with membrane trafficking or cytoskeletal organization. No GO or KEGG term passed global correction, so these functional interpretations are inferred from gene annotations, tissue and cell-type evidence, and network structure rather than from globally significant GO or KEGG enrichment. The STRING ichthyosis-related result is supplementary only (STRING NetworkNeighborAL Mixed, incl. Ichthyosis vulgaris, and Bullous congenital ichthyosiform erythroderma; within-query FDR = 0.0291).

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only NUCB2 is annotated as secreted to blood. It is also not a broadly blood-cell-enriched module; most genes have low immune-cell specificity, although several have immune-cell-enhanced or immune-cell-enriched patterns. Instead, HPA evidence points toward epithelial and keratinocyte biology. Skin enrichment occurs repeatedly, and the most recurrent single-cell signals involve esophageal apical cells and suprabasal keratinocytes. Every module protein is detected by immunohistochemistry in cervix_uterine. Thus, the shared signal may reflect epithelial cell composition or epithelial differentiation in the samples, rather than a circulating plasma program or a blood-cell contaminant. The broad tissue distribution of several genes indicates that the module is not exclusively a skin program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a small number of established relationships within the module: DSG1 with KRT1, KRT1 with KRT2, and TUBA4A with TUBB4B. The keratin relationships and the DSG1 relationship are biologically coherent with desmosomal adhesion and epithelial intermediate-filament organization, while the tubulin relationship supports a microtubule component. The supplementary STRING enrichment for an ichthyosis-related network involves KRT1, DSG1, and KRT2 (STRING NetworkNeighborAL Mixed, incl. Ichthyosis vulgaris, and Bullous congenital ichthyosiform erythroderma; within-query FDR = 0.0291), but it is not global enrichment evidence. hu.MAP identifies TUBA4A and TUBB4B together in several related complexes (hu.MAP huMAP3_09233.1), (hu.MAP huMAP3_10475.1), and (hu.MAP huMAP3_10665.1). These complexes contain many proteins not present in the module, so they support known tubulin-complex membership rather than a complete complex being represented. Most co-abundance links lack high-confidence STRING or hu.MAP support. This suggests that the module is a coordinated expression or abundance state organized around DSG1, not a single experimentally established multiprotein complex.

**STRING interactions (score >= 0.7)**: 3 of 91 gene pairs: DSG1–KRT1 (0.915); KRT1–KRT2 (0.956); TUBA4A–TUBB4B (0.991)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Mixed, incl. Ichthyosis vulgaris, and Bullous congenital ichthyosiform erythroderma (FDR = 0.0291, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09233.1 (TUBA4A, TUBB4B; 2/34); huMAP3_10475.1 (TUBA4A, TUBB4B; 2/39); huMAP3_10665.1 (TUBA4A, TUBB4B; 2/42)

### Novelty

The module should not be called a completely new molecular pathway. Its strongest biological components are established: DSG1, KRT1, and KRT2 are known epithelial adhesion and keratinization proteins, and TUBA4A with TUBB4B belongs to known tubulin machinery. The potentially novel result is the reproducible co-abundance combination across cell line and cervix_uterine, especially the coupling of the DSG1-centered epithelial signal with trafficking, metabolic, translational, and microtubule genes. Lack of STRING or hu.MAP support for many edges does not by itself establish novelty, because co-abundance can reflect shared regulation, cell composition, or state rather than direct binding. Novelty would require validation in independent cohorts, comparison with existing epithelial differentiation signatures, and testing whether the module persists after adjustment for epithelial cell abundance.

**Hypothesis.** Hypothesis: the shared module reflects an epithelial differentiation state in which DSG1-associated cell-cell adhesion and keratinization are coordinated with cytoskeletal remodeling and membrane trafficking. In this model, DSG1 marks the principal epithelial structural state, KRT1 and KRT2 reinforce the differentiated intermediate-filament program, TUBA4A and TUBB4B support microtubule organization, and EEA1, EPS15, DBNL, and FKBP15 may accompany junctional turnover or membrane trafficking. NUCB2, ME1, PSPH, EIF4E, and TPD52L1 could reflect secretory, metabolic, translational, or growth-state features of the same cells. This is a mechanistic hypothesis rather than a demonstrated causal pathway; the co-abundance data do not establish directionality or direct molecular interactions.

### Important genes

#### DSG1

- **Related proteins** (co-abundance neighbors): DBNL (0.93), KRT1 (0.92), FKBP15 (0.92), EEA1 (0.90), PSPH (0.90), TUBA4A (0.88), NUCB2 (0.88), KRT2 (0.88), TPD52L1 (0.85), ME1 (0.84), EPS15 (0.83), TUBB4B (0.82), EIF4E (0.80); STRING partners: KRT1 (0.915)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: desmoglein 1. This gene encodes a member of the desmoglein protein subfamily. Desmogleins, along with desmocollins, are cadherin-like transmembrane glycoproteins that are major components of the desmosome. Desmosomes are cell-cell junctions that help resist shearing forces and are found in high concentrations in cells subject to mechanical stress. This gene is found in a cluster with other desmoglein family mem…
- **Diseases (Open Targets)**: palmoplantar keratoderma i, striate, focal, or diffuse (0.738); severe dermatitis-multiple allergies-metabolic wasting syndrome (0.732); striate palmoplantar keratoderma (0.464); hereditary palmoplantar keratoderma (0.455); epidermolytic palmoplantar keratoderma, 1 (0.375)
- **Europe PMC papers**: 3455
- **Why important**: DSG1 is the dominant network hub and connects the module's otherwise weakly connected components. It is a desmosomal cadherin involved in cell-cell adhesion and resistance to mechanical stress. HPA supports skin and keratinocyte-associated expression and detects the protein in cervix_uterine. It also has a direct high-confidence STRING relationship with KRT1 and extensive disease and literature support, including palmoplantar keratoderma and severe dermatitis-related disorders.
- **Conclusion**: Established evidence supports DSG1 as the principal epithelial adhesion marker and the best anchor for interpreting the module. It is plausible that DSG1-related epithelial state helps organize the observed co-abundance pattern, but the network does not prove that DSG1 regulates the other module genes.

#### KRT1

- **Related proteins** (co-abundance neighbors): DSG1 (0.92); STRING partners: DSG1 (0.915), KRT2 (0.956)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 is a highly studied type II keratin with strong skin and suprabasal-keratinocyte specificity. It is linked to keratinization and intermediate-filament organization, has direct STRING relationships with DSG1 and KRT2, and has well-established associations with epidermolytic and other ichthyosis phenotypes. Its position adjacent to the DSG1 hub makes it a key structural readout of epithelial differentiation.
- **Conclusion**: Established evidence identifies KRT1 as a differentiated stratified-epithelium and keratinization marker that reinforces the module's epithelial interpretation. Its co-abundance with DSG1 and KRT2 is biologically coherent, but it should not be interpreted as proof that the module represents a disease state.

#### KRT2

- **Related proteins** (co-abundance neighbors): DSG1 (0.88); STRING partners: KRT1 (0.956)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location Intermediate filaments, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 2. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is expressed largely in the upper spinous layer of epidermal keratinocytes and mutations in this gene …
- **Diseases (Open Targets)**: superficial epidermolytic ichthyosis (0.815); exfoliative ichthyosis (0.358); Palmoplantar hyperkeratosis (0.267); hereditary disease (0.193); Vertigo (0.145)
- **Europe PMC papers**: 7459
- **Why important**: KRT2 is another highly studied suprabasal keratin with tissue enrichment in skin and cell-type enrichment in suprabasal keratinocytes. It is annotated for epidermis development, keratinization, and intermediate-filament organization, connects to KRT1 and DSG1 through STRING, and is associated with superficial and exfoliative ichthyosis phenotypes. It therefore provides an independent epithelial differentiation signal alongside KRT1.
- **Conclusion**: Established evidence supports KRT2 as a structural marker of suprabasal epithelial differentiation and as part of the keratinization axis represented in the module. A hypothesis that KRT2 contributes functionally to the shared cervix and cell-line state remains untested because the present data show association rather than causation.

#### TUBA4A

- **Related proteins** (co-abundance neighbors): DSG1 (0.88); STRING partners: TUBB4B (0.991)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09233.1, huMAP3_10475.1, huMAP3_10665.1
- **Function (MyGene.info)**: tubulin alpha 4a. Microtubules of the eukaryotic cytoskeleton perform essential and diverse functions and are composed of a heterodimer of alpha and beta tubulin. The genes encoding these microtubule constituents are part of the tubulin superfamily, which is composed of six distinct families. Genes from the alpha, beta and gamma tubulin families are found in all eukaryotes. The alpha and beta tubulins represent the…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.778); amyotrophic lateral sclerosis type 22 (0.700); breast cancer (0.607); non-small cell lung carcinoma (0.607); breast carcinoma (0.598)
- **Europe PMC papers**: 1797
- **Why important**: TUBA4A is the alpha-tubulin member of the module's microtubule pair with TUBB4B. It has hu.MAP support in several complexes (hu.MAP huMAP3_09233.1), (hu.MAP huMAP3_10475.1), and (hu.MAP huMAP3_10665.1), a high-confidence STRING relationship with TUBB4B, and annotations involving microtubule organization and cell-cycle processes. HPA places it in microtubule structures and shows enhancement in several epithelial and reproductive cell types. It adds a cytoskeletal dimension beyond desmosomes and keratins.
- **Conclusion**: Established evidence supports TUBA4A as a marker of microtubule machinery represented in the module. Its coordinated abundance with TUBB4B is consistent with cytoskeletal remodeling, but the data do not establish that microtubule remodeling is downstream of DSG1.

#### TUBB4B

- **Related proteins** (co-abundance neighbors): DSG1 (0.82); STRING partners: TUBA4A (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09233.1, huMAP3_10475.1, huMAP3_10665.1
- **Function (MyGene.info)**: tubulin beta 4B class IVb. Enables double-stranded RNA binding activity. Predicted to be involved in microtubule cytoskeleton organization and mitotic cell cycle. Located in microtubule. Implicated in Leber congenital amaurosis with early-onset deafness. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Leber congenital amaurosis with early-onset deafness (0.651); non-small cell lung carcinoma (0.615); breast cancer (0.605); breast carcinoma (0.598); neoplasm (0.597)
- **Europe PMC papers**: 1308
- **Why important**: TUBB4B forms the complementary beta-tubulin pair with TUBA4A, is supported by the same hu.MAP complex evidence (hu.MAP huMAP3_09233.1), (hu.MAP huMAP3_10475.1), and (hu.MAP huMAP3_10665.1), and has a high-confidence STRING relationship with TUBA4A. It is annotated for microtubule organization and mitotic processes, has broad but cell-type-enhanced HPA expression, and has disease associations including a congenital retinal and hearing disorder and several neoplastic conditions.
- **Conclusion**: Established evidence supports TUBB4B as a component of the module's microtubule-associated signal and strengthens the interpretation that the module includes cytoskeletal organization. Its connection to epithelial differentiation is a hypothesis based on co-abundance and cell context, not a demonstrated direct role in DSG1-dependent adhesion.
