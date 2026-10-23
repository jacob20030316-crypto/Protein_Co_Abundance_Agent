# Conserved co-abundance modules: cervix_uterine and myometrium

## Module 0

**Tissue pair**: cervix_uterine and myometrium  
**Genes (7)**: ORM2, SERPINA1, LRG1, SERPINA3, ITIH4, MDH1, GC

### Function

The strongest interpretation is an acute inflammatory and acute-phase plasma protein module. The primary evidence is the globally corrected enrichment for acute-phase response (GO:BP acute-phase response; q_global = 0.00238) and acute inflammatory response (GO:BP acute inflammatory response; q_global = 0.00501), with ITIH4, ORM2, SERPINA1 and SERPINA3 contributing to both terms. The module is therefore more consistent with coordinated extracellular inflammatory transport, protease regulation and acute-phase biology than with a cervix- or myometrium-specific intracellular pathway. LRG1 may add an endothelial, epithelial, wound-healing or angiogenic signaling component, while GC contributes vitamin transport biology, but these interpretations are supplementary because those genes are not present in the primary globally significant GO/KEGG terms. MDH1 is an isolated metabolic gene in the module and does not establish a metabolic module-level function.

**Cell composition.** This module is dominated by secreted blood proteins and has a strong liver and hepatocyte signature in HPA. Most of the genes are secreted to blood, and HPA also links part of the module to neutrophils or monocytes. The tissue evidence argues against interpreting the module as a product of local cervix or myometrium cells: SERPINA1, LRG1, ORM2 and ITIH4 are not detected by HPA immunohistochemistry in those tissues, whereas GC is detected in both and SERPINA3 is detected in cervix. The shared signal may therefore reflect circulating plasma proteins, blood exposure, a shared vascular or immune component, or tissue-associated extracellular material. It should not automatically be treated as evidence that uterine cells synthesize the entire module.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP acute-phase response | 0.00238 | ITIH4, ORM2, SERPINA1, SERPINA3 |
| GO:BP acute inflammatory response | 0.00501 | ITIH4, ORM2, SERPINA1, SERPINA3 |

### STRING and hu.MAP

STRING supports a partially known interaction core. The strongest listed relationships connect ORM2 with SERPINA1 and SERPINA3, and additional links connect GC with SERPINA1 and ORM2 and LRG1 with SERPINA3. STRING provides no listed interaction for ITIH4 or MDH1, and the LRG1 evidence is comparatively limited within this module. The STRING enrichment for acute-phase, secreted and glycoprotein annotations is concordant with the primary GO interpretation but remains supplementary. hu.MAP independently places SERPINA1, SERPINA3, GC, ORM2 and ITIH4 together in several complexes, especially complexes C1 through C5. These complexes contain many other plasma, complement, coagulation and transport proteins, so they support a shared extracellular plasma-protein context rather than proving a dedicated cervix-myometrium complex. The hu.MAP results also show that several module relationships are embedded in broad plasma-protein assemblies.

**STRING interactions (score >= 0.7)**: 5 of 21 gene pairs: GC–ORM2 (0.726); GC–SERPINA1 (0.876); LRG1–SERPINA3 (0.711); ORM2–SERPINA1 (0.972); ORM2–SERPINA3 (0.903)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Acute phase (FDR = 0.00011, 4 genes); Keyword Secreted (FDR = 0.00044, 6 genes); PMID (2022) Effects of Omega-3 and Antioxidant Cocktail Supplement on Prolonged Bed Rest: Results from Serum Proteome and Sphingolipids Analysis. (FDR = 0.00048, 6 genes); PMID (2018) Serum sialylation changes in cancer. (FDR = 0.00048, 5 genes); PMID (2016) Glycoproteomic Analysis of Malignant Ovarian Cancer Ascites Fluid Identifies Unusual Glycopeptides. (FDR = 0.00048, 6 genes); Keyword Signal (FDR = 0.00091, 6 genes); Keyword Glycoprotein (FDR = 0.0012, 6 genes); PMID (2023) The brain reacting to COVID-19: analysis of the cerebrospinal fluid proteome, RNA and inflammation. (FDR = 0.0014, 5 genes); PMID (2015) Identification of serum proteome signatures of locally advanced and metastatic gastric cancer: a pilot study. (FDR = 0.0014, 5 genes); PMID (2014) Mapping and Identification of the Urine Proteome of Prostate Cancer Patients by 2D PAGEMS. (FDR = 0.0014, 5 genes); TISSUES Plasma cell (FDR = 0.002, 5 genes); PMID (2017) Plasma biomarker proteins for detection of human growth hormone administration in athletes. (FDR = 0.0021, 5 genes); PMID (2010) Plasma proteomic analysis of simian immunodeficiency virus infection of rhesus macaques. (FDR = 0.0021, 5 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 0.0024, 6 genes); PMID (2021) Exosome-Derived Mediators as Potential Biomarkers for Cardiovascular Diseases: A Network Approach. (FDR = 0.0024, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINA1, SERPINA3, GC, ORM2, ITIH4; 5/64); huMAP3_10678.1 (SERPINA1, SERPINA3, GC, ORM2, ITIH4; 5/71); huMAP3_09434.1 (SERPINA1, SERPINA3, GC, ITIH4; 4/33); huMAP3_09531.1 (SERPINA1, SERPINA3, ORM2, ITIH4; 4/47); huMAP3_10101.1 (SERPINA1, SERPINA3, ORM2, ITIH4; 4/49); huMAP3_07432.1 (SERPINA1, SERPINA3, ORM2; 3/18); huMAP3_07265.1 (SERPINA1, SERPINA3, ORM2; 3/20); huMAP3_08395.1 (SERPINA1, SERPINA3, ORM2; 3/43); huMAP3_08224.1 (SERPINA3, GC; 2/21)

### Novelty

The molecular function of this gene set is not a new biological discovery: acute-phase proteins, liver origin, secretion to blood and several of the protein relationships are already well established by GO, STRING, hu.MAP and the gene-level literature. The potentially novel observation is the co-abundance of this particular set across cervix_uterine and myometrium. However, the fact sheet does not establish that this tissue-pair module has not been reported elsewhere, and absence of a relationship from STRING or hu.MAP would not prove novelty. The most defensible conclusion is that the tissue-pair co-abundance pattern may be a new dataset-specific observation, while its biological interpretation is largely established and may primarily reflect shared blood, liver-derived plasma proteins or immune-associated material.

**Hypothesis.** Hypothesis: a shared vascular or inflammatory exposure in cervix_uterine and myometrium produces coordinated abundance of circulating acute-phase glycoproteins. Within this model, SERPINA1, SERPINA3 and ORM2 provide protease-inhibitory and acute-phase activity, ITIH4 participates in extracellular matrix or hyaluronan-associated inflammatory remodeling, LRG1 may connect the plasma signal to endothelial, epithelial, wound-healing or angiogenic responses, and GC may transport vitamin D-related metabolites. This hypothesis predicts that the module will track plasma leakage, vascularity, inflammatory state or immune-cell admixture more strongly than local smooth-muscle or cervical-cell identity. It requires validation using matched plasma measurements, cell-type-resolved expression, histology and independent tissue cohorts.

### Important genes

#### SERPINA1

- **Related proteins** (co-abundance neighbors): LRG1 (0.89), SERPINA3 (0.88), GC (0.87); STRING partners: GC (0.876), ORM2 (0.972)
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09434.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_08395.1
- **Function (MyGene.info)**: serpin family A member 1. The protein encoded by this gene is a serine protease inhibitor belonging to the serpin superfamily whose targets include elastase, plasmin, thrombin, trypsin, chymotrypsin, and plasminogen activator. This protein is produced in the liver, the bone marrow, by lymphocytic and monocytic cells in lymphoid tissue, and by the Paneth cells of the gut. Defects in this gene are associated with chronic obs…
- **Diseases (Open Targets)**: alpha 1-antitrypsin deficiency (0.768); chronic obstructive pulmonary disease (0.690); cirrhosis of liver (0.573); cholelithiasis (0.569); pulmonary emphysema (0.569)
- **Europe PMC papers**: 6526
- **Why important**: SERPINA1 is a central network gene with links to LRG1, SERPINA3 and GC, and it occurs in both primary acute-phase terms (GO:BP acute-phase response; q_global = 0.00238) and (GO:BP acute inflammatory response; q_global = 0.00501). It is a liver-derived secreted serpin whose established targets include several proteases. It is represented across many STRING supplementary annotations, appears in numerous hu.MAP complexes, has extensive literature, and has established disease associations including alpha one antitrypsin deficiency, chronic obstructive pulmonary disease and liver disease.
- **Conclusion**: Established conclusion: SERPINA1 is a major marker and plausible functional contributor to the module's circulating acute-phase and protease-regulatory character. Hypothesis: its network position makes it a useful sentinel for determining whether the module reflects plasma exposure or inflammation rather than local uterine synthesis.

#### SERPINA3

- **Related proteins** (co-abundance neighbors): SERPINA1 (0.88), MDH1 (0.82); STRING partners: LRG1 (0.711), ORM2 (0.903)
- **HPA**: Group enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09434.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_08395.1, huMAP3_08224.1
- **Function (MyGene.info)**: serpin family A member 3. The protein encoded by this gene is a member of the serpin family of proteins, a group of proteins that inhibit serine proteases. This gene is one in a cluster of serpin genes located on the q arm of chromosome 14. Polymorphisms in this protein appear to be tissue specific and influence protease targeting. Variations in this protein's sequence have been implicated in Alzheimer's disease, and defic…
- **Diseases (Open Targets)**: prostate carcinoma (0.359); chronic kidney disease (0.217); peripheral arterial occlusive disease 1 (0.118); central nervous system cancer (0.118); glioma (0.105)
- **Europe PMC papers**: 5458
- **Why important**: SERPINA3 is directly connected to SERPINA1 and MDH1 and occurs in both primary terms (GO:BP acute-phase response; q_global = 0.00238) and (GO:BP acute inflammatory response; q_global = 0.00501). It is a secreted serpin associated with inflammatory response and cytokine response, is detected in cervix but not myometrium by HPA, and appears in many hu.MAP complexes. It has substantial literature and reported associations with liver disease, Alzheimer disease and several cancers.
- **Conclusion**: Established conclusion: SERPINA3 reinforces the acute inflammatory and extracellular protease-regulatory interpretation. Hypothesis: its cervix detection may indicate a local contribution in cervix, although the broader liver and plasma evidence means that local production cannot be inferred from co-abundance alone.

#### ORM2

- **Related proteins** (co-abundance neighbors): LRG1 (0.83); STRING partners: GC (0.726), SERPINA1 (0.972), SERPINA3 (0.903)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_08395.1
- **Function (MyGene.info)**: orosomucoid 2. This gene encodes a key acute phase plasma protein. Because of its increase due to acute inflammation, this protein is classified as an acute-phase reactant.  The specific function of this protein has not yet been determined; however, it may be involved in aspects of immunosuppression. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: hemorrhage (0.262); complication (0.262); rheumatoid arthritis (0.095); neoplasm (0.088); nephronophthisis (0.088)
- **Europe PMC papers**: 1234
- **Why important**: ORM2 is part of both primary acute-phase terms (GO:BP acute-phase response; q_global = 0.00238) and (GO:BP acute inflammatory response; q_global = 0.00501) and has strong listed STRING relationships with SERPINA1 and SERPINA3, as well as a relationship with GC. It is a liver-derived secreted acute-phase plasma protein with immune-regulatory annotations, neutrophil enrichment and membership in several hu.MAP plasma-protein complexes. Its disease associations and literature support its value as an inflammation-linked circulating marker.
- **Conclusion**: Established conclusion: ORM2 is a core acute-phase component and a strong indicator that the module represents a circulating inflammatory protein program. Hypothesis: ORM2 may help couple the serpin-rich protein group to broader immune and cytokine-related changes in the tissue samples.

#### ITIH4

- **Related proteins** (co-abundance neighbors): LRG1 (0.86); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09434.1, huMAP3_09531.1, huMAP3_10101.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 4. The protein encoded by this gene is secreted into the blood, where it is cleaved by plasma kallikrein into two smaller forms. Expression of this gene has been detected only in liver, and it seems to be upregulated during surgical trauma. This gene is part of a cluster of similar genes on chromosome 3. Two transcript variants encoding different isoforms have been found for this gene. [provided by R…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.466); coronary artery disorder (0.417); type 2 diabetes mellitus (0.397); osteoarthritis (0.387); diabetes mellitus (0.363)
- **Europe PMC papers**: 1710
- **Why important**: ITIH4 is present in both primary terms (GO:BP acute-phase response; q_global = 0.00238) and (GO:BP acute inflammatory response; q_global = 0.00501), is secreted to blood, and is included with the main acute-phase proteins in several hu.MAP complexes. Its established annotations include acute-phase response, hyaluronan metabolism and cytokine response, while its documented expression is liver-associated and it is not detected in the two queried tissues by HPA immunohistochemistry. It has disease associations involving skeletal, coronary and metabolic disorders.
- **Conclusion**: Established conclusion: ITIH4 supports an extracellular acute-phase and matrix-associated inflammatory interpretation. Hypothesis: it may connect circulating inflammation to extracellular-matrix or hyaluronan remodeling near the sampled tissues, but the available evidence does not demonstrate local production.

#### LRG1

- **Related proteins** (co-abundance neighbors): SERPINA1 (0.89), ITIH4 (0.86), ORM2 (0.83); STRING partners: SERPINA3 (0.711)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: leucine rich alpha-2-glycoprotein 1. The leucine-rich repeat (LRR) family of proteins, including LRG1, have been shown to be involved in protein-protein interaction, signal transduction, and cell adhesion and development. LRG1 is expressed during granulocyte differentiation (O'Donnell et al., 2002 [PubMed 12223515]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: colorectal carcinoma (0.113); neoplasm (0.112); nonpapillary renal cell carcinoma (0.101); non-small cell lung carcinoma (0.099); esophageal squamous cell carcinoma (0.096)
- **Europe PMC papers**: 2461
- **Why important**: LRG1 has high network connectivity in the module, linking SERPINA1, ITIH4 and ORM2, and is associated in the supplied annotations with endothelial proliferation, epithelial-to-mesenchymal transition, keratinocyte proliferation, transforming growth factor beta receptor signaling, wound healing and angiogenesis. HPA places it in liver and neutrophil-associated contexts and identifies it as secreted to blood. Although it is absent from the listed hu.MAP complexes and has only a limited listed STRING relationship, its network position gives it importance as a possible signaling bridge.
- **Conclusion**: Established conclusion: LRG1 is a secreted, inflammation-associated network connector with plausible vascular and tissue-remodeling relevance. Hypothesis: LRG1 may link a circulating acute-phase signal to endothelial or epithelial responses in cervix and myometrium, but this mechanistic role is not established by the co-abundance data.

## Module 1

**Tissue pair**: cervix_uterine and myometrium  
**Genes (12)**: ACTL6A, DDX5, DDX39B, FASN, HNRNPK, HNRNPL, LMNB1, MAT2A, NRDC, NUP155, NUP93, SF3A1

### Function

The module is best interpreted as a nuclear RNA-processing and pre-mRNA-splicing module. The primary evidence is the globally corrected enrichment for nuclear protein-containing complexes (GO:CC nuclear protein-containing complex; q_global = 0.00314), multiple forms of spliceosomal RNA splicing (GO:BP RNA splicing, via transesterification reactions; q_global = 0.00875), (GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 0.00875), (GO:BP mRNA splicing, via spliceosome; q_global = 0.00875), RNA processing (GO:BP RNA processing; q_global = 0.0172), mRNA processing (GO:BP mRNA processing; q_global = 0.0264), RNA splicing (GO:BP RNA splicing; q_global = 0.0264), the KEGG spliceosome pathway (KEGG Spliceosome - Homo sapiens (human); q_global = 0.0314), and the spliceosomal complex (GO:CC spliceosomal complex; q_global = 0.039). The module therefore appears to capture coordinated abundance of spliceosomal and nuclear RNA-metabolism machinery, with additional nuclear-envelope and chromatin-associated components. The annotations support a role in spliceosome assembly or activity, RNA maturation, and movement of processed RNA between the nucleus and cytoplasm. The module should not be reduced to a single pathway, because its members also include nucleoporins, a nuclear-lamina protein, a chromatin-remodeling component, a metabolic enzyme, and a protease-related protein.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly intracellular, especially nuclear, nucleoplasmic, nuclear-speckle, nuclear-membrane, or nuclear-lamina proteins. Most genes have low tissue specificity, which is compatible with broadly used cellular machinery rather than a highly restricted tissue program. The module is also unlikely to be explained primarily by blood contamination or a blood-cell program: HPA reports low immune-cell specificity for nearly all genes, no recurring enriched blood-cell category, and only one gene not detected in immune cells. Several cell-type-enhanced annotations involve germ-cell or neural cell types, but these are dispersed rather than forming a coherent cervix or myometrium lineage signature. Protein detection in both tissues for many members supports presence in the sampled tissues, although absence of detection for some proteins means that tissue-level protein evidence is incomplete.

**GO/KEGG enrichment**: 9 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC nuclear protein-containing complex | 0.00314 | ACTL6A, DDX39B, DDX5, HNRNPK, NUP155, NUP93, SF3A1 |
| GO:BP RNA splicing, via transesterification reactions | 0.00875 | DDX39B, DDX5, HNRNPK, HNRNPL, SF3A1 |
| GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile | 0.00875 | DDX39B, DDX5, HNRNPK, HNRNPL, SF3A1 |
| GO:BP mRNA splicing, via spliceosome | 0.00875 | DDX39B, DDX5, HNRNPK, HNRNPL, SF3A1 |
| GO:BP RNA processing | 0.0172 | DDX39B, DDX5, HNRNPK, HNRNPL, NUP155, SF3A1 |
| GO:BP mRNA processing | 0.0264 | DDX39B, DDX5, HNRNPK, HNRNPL, SF3A1 |
| GO:BP RNA splicing | 0.0264 | DDX39B, DDX5, HNRNPK, HNRNPL, SF3A1 |
| KEGG Spliceosome - Homo sapiens (human) | 0.0314 | DDX39B, DDX5, HNRNPK, SF3A1 |
| GO:CC spliceosomal complex | 0.039 | DDX39B, DDX5, HNRNPK, SF3A1 |

### STRING and hu.MAP

STRING supports a coherent RNA-processing subnetwork through DDX39B with DDX5, HNRNPK, and HNRNPL, through DDX5 with HNRNPK, and through HNRNPK with HNRNPL. It separately supports a very strong nucleoporin relationship between NUP155 and NUP93. The STRING functional results are concordant with pre-mRNA processing, the major splicing pathway, nuclear protein complexes, nucleoplasmic and nuclear-lumen localization, RNA export, and SUMO-related processes (STRING RCTM Processing of Capped Intron-Containing Pre-mRNA; within-query FDR = 3.65e-05), (STRING Component Nuclear protein-containing complex; within-query FDR = 0.0013), (STRING RCTM SUMO E3 ligases SUMOylate target proteins; within-query FDR = 0.0017), (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0027), (STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.0038), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0038), (STRING RCTM SUMOylation of RNA binding proteins; within-query FDR = 0.0081), (STRING RCTM Transport of Mature mRNA derived from an Intron-Containing Transcript; within-query FDR = 0.0168). These STRING results are supplementary rather than globally corrected module-level evidence. hu.MAP provides orthogonal complex support for HNRNPK and HNRNPL occurring together in two larger heterogeneous nuclear ribonucleoprotein complexes (hu.MAP huMAP3_10659.1), (hu.MAP huMAP3_10625.1). The fact that these complexes contain many additional RNA-binding proteins indicates that the module samples parts of larger cellular assemblies rather than representing complete complexes. The lack of hu.MAP assignments for the other module members does not imply that they do not interact biologically.

**STRING interactions (score >= 0.7)**: 6 of 66 gene pairs: DDX39B–DDX5 (0.915); DDX39B–HNRNPK (0.808); DDX39B–HNRNPL (0.807); DDX5–HNRNPK (0.935); HNRNPK–HNRNPL (0.99); NUP155–NUP93 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Processing of Capped Intron-Containing Pre-mRNA (FDR = 3.65e-05, 7 genes); Keyword Isopeptide bond (FDR = 3.82e-05, 10 genes); Keyword Ubl conjugation (FDR = 0.0001, 10 genes); Component Nuclear protein-containing complex (FDR = 0.0013, 7 genes); RCTM SUMO E3 ligases SUMOylate target proteins (FDR = 0.0017, 4 genes); RCTM mRNA Splicing - Major Pathway (FDR = 0.0027, 5 genes); COMPARTMENTS Nucleoplasm (FDR = 0.0038, 7 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0038, 8 genes); Keyword Spliceosome (FDR = 0.0061, 4 genes); RCTM SUMOylation of RNA binding proteins (FDR = 0.0081, 3 genes); COMPARTMENTS Spliceosomal complex (FDR = 0.0116, 4 genes); RCTM Transport of Mature mRNA derived from an Intron-Containing Transcript (FDR = 0.0168, 3 genes); RCTM Nuclear Envelope Breakdown (FDR = 0.0168, 3 genes); KEGG Spliceosome (FDR = 0.0177, 4 genes); RCTM HCMV Late Events (FDR = 0.019, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10659.1 (HNRNPL, HNRNPK; 2/28); huMAP3_10625.1 (HNRNPL, HNRNPK; 2/57)

### Novelty

The broad biological interpretation is not a new discovery: spliceosomal activity, heterogeneous nuclear ribonucleoprotein assemblies, and nucleoporin relationships are already established by the globally corrected annotations, STRING relationships, hu.MAP complexes, and gene descriptions. The module may nevertheless represent a potentially novel co-abundance pattern shared by cervix_uterine and myometrium, particularly because it combines a spliceosome-associated subnetwork with a nucleoporin pair, nuclear-lamina and chromatin components, and metabolic or protease-related genes. However, the supplied evidence does not establish that this tissue-shared combination has never been reported. Absence of a hu.MAP or STRING relationship for several module pairs cannot prove novelty, because those resources emphasize experimentally supported or curated interactions and do not directly test this tissue-pair co-abundance pattern. The most defensible conclusion is that the molecular functions are established, whereas the specific cross-tissue co-abundance organization remains a candidate observation requiring replication and comparison with existing tissue-network studies.

**Hypothesis.** Hypothesis: the shared module reflects coordinated regulation of nuclear RNA handling in cervix_uterine and myometrium. A spliceosomal core represented by DDX39B, DDX5, HNRNPK, HNRNPL, and SF3A1 may process selected pre-mRNAs, while NUP93 and NUP155 support nucleocytoplasmic transport and nuclear-envelope organization. ACTL6A and LMNB1 may connect this RNA-processing state to chromatin or nuclear architecture, and MAT2A may provide a methyl-donor-related metabolic context that influences RNA or protein regulation. NRDC and FASN may represent tissue-state or metabolic coupling rather than core spliceosome components. This model predicts coordinated changes in RNA splicing, RNA export, and nuclear organization across the two tissues, but it does not establish direct physical interaction or causal regulation among every module member.

### Important genes

#### DDX5

- **Related proteins** (co-abundance neighbors): MAT2A (0.84), HNRNPL (0.82); STRING partners: DDX39B (0.915), HNRNPK (0.935)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 is a central connector within the spliceosome-associated portion of the network and participates in every primary enrichment term (GO:CC nuclear protein-containing complex; q_global = 0.00314) through (GO:CC spliceosomal complex; q_global = 0.039). Its established functions include RNA-structure remodeling, transcriptional co-regulation, alternative splicing, and small noncoding RNA processing. It has substantial literature support and STRING relationships with DDX39B and HNRNPK, while the supplementary STRING results connect it to spliceosomal, nuclear-complex, and SUMO-related processes (STRING RCTM Processing of Capped Intron-Containing Pre-mRNA; within-query FDR = 3.65e-05), (STRING Component Nuclear protein-containing complex; within-query FDR = 0.0013), (STRING RCTM SUMO E3 ligases SUMOylate target proteins; within-query FDR = 0.0017), (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0027), (STRING Keyword Spliceosome; within-query FDR = 0.0061).
- **Conclusion**: Established evidence supports DDX5 as a major RNA-processing and splicing component of the module. It is reasonable to regard DDX5 as a functional anchor. It remains a hypothesis that its abundance specifically drives tissue-shared alternative-splicing changes in cervix_uterine and myometrium.

#### DDX39B

- **Related proteins** (co-abundance neighbors): MAT2A (0.84), NRDC (0.83), HNRNPK (0.82); STRING partners: DDX5 (0.915), HNRNPK (0.808), HNRNPL (0.807)
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nuclear speckles; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 39B. This gene encodes a member of the DEAD box family of RNA-dependent ATPases that mediate ATP hydrolysis during pre-mRNA splicing. The encoded protein is an essential splicing factor required for association of U2 small nuclear ribonucleoprotein with pre-mRNA, and it also plays an important role in mRNA export from the nucleus to the cytoplasm. This gene belongs to a cluster of genes localized in th…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); Alzheimer disease (0.522); Parkinson disease (0.503); lysosomal storage disease (0.503); neurodevelopmental disorder (0.413)
- **Europe PMC papers**: 1037
- **Why important**: DDX39B links the spliceosomal subnetwork to other module components and participates in every primary enrichment term (GO:CC nuclear protein-containing complex; q_global = 0.00314) through (GO:CC spliceosomal complex; q_global = 0.039). Its established functions include ATP-dependent pre-mRNA splicing, U2 small nuclear ribonucleoprotein association, and mRNA export. It has several strong STRING relationships within the module and is represented in the supplementary processing, spliceosome, nuclear-complex, and RNA-export terms (STRING RCTM Processing of Capped Intron-Containing Pre-mRNA; within-query FDR = 3.65e-05), (STRING Component Nuclear protein-containing complex; within-query FDR = 0.0013), (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0027), (STRING Keyword Spliceosome; within-query FDR = 0.0061), (STRING RCTM Transport of Mature mRNA derived from an Intron-Containing Transcript; within-query FDR = 0.0168).
- **Conclusion**: Established evidence identifies DDX39B as a plausible bridge between pre-mRNA splicing and nuclear export within the module. The hypothesis that it coordinates the shared tissue program, rather than merely marking general nuclear RNA metabolism, requires direct expression, isoform, and perturbation evidence.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): DDX39B (0.82); STRING partners: DDX39B (0.808), DDX5 (0.935), HNRNPL (0.99)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK participates in every primary enrichment term (GO:CC nuclear protein-containing complex; q_global = 0.00314) through (GO:CC spliceosomal complex; q_global = 0.039), connects to DDX39B and DDX5 in STRING, and has the strongest STRING relationship with HNRNPL. It is a nuclear RNA-binding protein involved in pre-mRNA processing, RNA metabolism, transcriptional regulation, and signal transduction. It is also the only selected gene represented in both hu.MAP heterogeneous nuclear ribonucleoprotein complexes (hu.MAP huMAP3_10659.1), (hu.MAP huMAP3_10625.1), together with HNRNPL. Its disease associations and extensive literature support make it an important interpretive anchor.
- **Conclusion**: Established evidence supports HNRNPK as a multifunctional RNA-binding and transcriptional regulator embedded in the module’s spliceosomal network and larger hnRNP assemblies. A tissue-specific role in selecting transcripts or coupling splicing to transcription is a hypothesis, not demonstrated by co-abundance alone.

#### SF3A1

- **Related proteins** (co-abundance neighbors): MAT2A (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 participates in every primary enrichment term (GO:CC nuclear protein-containing complex; q_global = 0.00314) through (GO:CC spliceosomal complex; q_global = 0.039). It is an established component of the SF3A complex and mature U2 small nuclear ribonucleoprotein, with roles in spliceosome assembly, splice-site recognition, and mRNA processing. Its connection to DDX5-related network structure and its repeated representation in the supplementary spliceosome terms (STRING RCTM Processing of Capped Intron-Containing Pre-mRNA; within-query FDR = 3.65e-05), (STRING Component Nuclear protein-containing complex; within-query FDR = 0.0013), (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0027), (STRING Keyword Spliceosome; within-query FDR = 0.0061), (STRING COMPARTMENTS Spliceosomal complex; within-query FDR = 0.0116), (STRING KEGG Spliceosome; within-query FDR = 0.0177) strengthen its interpretation as a core spliceosomal component.
- **Conclusion**: Established evidence supports SF3A1 as a direct molecular representative of the module’s core spliceosome function. The hypothesis that SF3A1 abundance limits or alters specific splicing programs in either tissue requires transcript-isoform or functional validation.

#### NUP93

- **Related proteins** (co-abundance neighbors): NRDC (0.86); STRING partners: NUP155 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 provides a nuclear-pore and nuclear-envelope component that broadens the module beyond spliceosome proteins. It participates in the nuclear protein-containing complex enrichment (GO:CC nuclear protein-containing complex; q_global = 0.00314) and is associated with nucleocytoplasmic transport, nuclear-pore assembly, nuclear-envelope organization, and polyadenylated RNA export. Its very strong STRING relationship with NUP155 and its representation in supplementary nuclear-complex, RNA-export, and SUMO-related terms (STRING RCTM Processing of Capped Intron-Containing Pre-mRNA; within-query FDR = 3.65e-05), (STRING Component Nuclear protein-containing complex; within-query FDR = 0.0013), (STRING RCTM SUMO E3 ligases SUMOylate target proteins; within-query FDR = 0.0017), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0038), (STRING RCTM SUMOylation of RNA binding proteins; within-query FDR = 0.0081), (STRING RCTM Transport of Mature mRNA derived from an Intron-Containing Transcript; within-query FDR = 0.0168), (STRING RCTM Nuclear Envelope Breakdown; within-query FDR = 0.0168), (STRING RCTM HCMV Late Events; within-query FDR = 0.019) support a transport-related substructure.
- **Conclusion**: Established evidence supports NUP93 as a nuclear-pore component that may connect RNA processing with export and nuclear architecture. It is a hypothesis that the NUP93-NUP155 pair is functionally coordinated with the spliceosomal subnetwork in these tissues rather than simply co-abundant because of shared nuclear content.

## Module 2

**Tissue pair**: cervix_uterine and myometrium  
**Genes (19)**: ACO1, ACO2, CANX, CAPN1, CAPN2, DNM1L, FERMT2, GARS1, HSP90AA1, HSPA8, KATNAL2, PGM2, PLCD1, CTPS1, SEC23A, SEPTIN9, STAT1, TARS1, VPS35

### Function

The strongest primary evidence supports protein processing in the endoplasmic reticulum through (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0218), which includes CANX, CAPN1, CAPN2, HSP90AA1, HSPA8, and SEC23A. CANX and the heat-shock proteins support folding and quality control of newly synthesized proteins, while SEC23A supports COPII-dependent export from the endoplasmic reticulum toward the Golgi. CAPN1 and CAPN2 add calcium-regulated intracellular proteolysis. The supplementary STRING results reinforce an endoplasmic-reticulum processing theme (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0114) and also suggest links to necroptosis (STRING KEGG Necroptosis; within-query FDR = 0.0123), perinuclear organization (STRING Component Perinuclear region of cytoplasm; within-query FDR = 0.0473), and antigen processing and presentation (STRING KEGG Antigen processing and presentation; within-query FDR = 0.0481). These supplementary signals should not be interpreted as globally corrected enrichment. The remaining genes connect this core to mitochondrial and peroxisomal fission, endosomal recycling, cytoskeletal organization, phospholipid signaling, central metabolism, and translation. Thus, the module is best interpreted as a cellular proteostasis and trafficking program with connections to stress response, organelle remodeling, and calcium-dependent proteolysis, rather than as a narrowly tissue-specific pathway.

**Cell composition.** The module is predominantly composed of intracellular, broadly expressed proteins with low tissue specificity in HPA. Many genes encode housekeeping-type functions such as chaperoning, translation, nucleotide or carbohydrate metabolism, organelle maintenance, and vesicle transport. The HPA profile argues against a plasma-protein or secreted-protein module: only one gene is classified as secreted, and the genes generally have low immune-cell specificity, with no enriched blood-cell category reported. Protein detection is broad in cervix_uterine and present for a substantial subset in myometrium, while several genes are not detected in myometrium. Cell-type annotations are heterogeneous, including smooth muscle cells, adipocytes, hepatocytes, epithelial populations, and other specialized cell types. Therefore, the shared signal is more plausibly a conserved intracellular program or a common cellular-composition feature than contamination by blood. The broad expression of several chaperones and metabolic proteins also means that co-abundance may partly reflect general cellular abundance or tissue quality.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human) | 0.0218 | CANX, CAPN1, CAPN2, HSP90AA1, HSPA8, SEC23A |

### STRING and hu.MAP

STRING supports several established relationships within the module: CAPN1 with CAPN2, HSP90AA1 with HSPA8, HSP90AA1 with CANX, HSP90AA1 with STAT1, DNM1L with VPS35, ACO1 with ACO2, and GARS1 with TARS1. These interactions show that parts of the module recapitulate known protein relationships, particularly the calpain pair, chaperone network, mitochondrial or endosomal connection, aconitase pair, and aminoacyl-tRNA synthetase pair. The STRING functional results independently highlight the endoplasmic-reticulum processing group (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0114), but the necroptosis and antigen-presentation signals (STRING KEGG Necroptosis; within-query FDR = 0.0123) (STRING KEGG Antigen processing and presentation; within-query FDR = 0.0481) remain supplementary. hu.MAP repeatedly identifies CAPN1 and CAPN2 together in complexes containing CAPNS1, and in some complexes also CAPN8, CAST, FNTB, LIX1L, KDM8, SPDL1, WNT8B, or CAPNS2 (hu.MAP huMAP3_03767.1) through (hu.MAP huMAP3_12926.1). This is strong evidence that the CAPN1-CAPN2 portion reflects established calpain-complex biology. In contrast, hu.MAP does not provide a complex containing the module as a whole, and most other module genes lack a reported hu.MAP complex in the supplied evidence. The network therefore combines known local interaction neighborhoods with co-abundance links that may reflect shared regulation, compartmental proximity, or cellular state rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 7 of 171 gene pairs: ACO1–ACO2 (0.943); CANX–HSP90AA1 (0.848); CAPN1–CAPN2 (0.978); DNM1L–VPS35 (0.9); GARS1–TARS1 (0.909); HSP90AA1–HSPA8 (0.999); HSP90AA1–STAT1 (0.868)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Protein processing in endoplasmic reticulum (FDR = 0.0114, 6 genes); KEGG Necroptosis (FDR = 0.0123, 5 genes); Component Perinuclear region of cytoplasm (FDR = 0.0473, 8 genes); KEGG Antigen processing and presentation (FDR = 0.0481, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03767.1 (CAPN1, CAPN2; 2/3); huMAP3_08670.1 (CAPN1, CAPN2; 2/4); huMAP3_09127.1 (CAPN1, CAPN2; 2/5); huMAP3_09328.1 (CAPN1, CAPN2; 2/6); huMAP3_10242.1 (CAPN1, CAPN2; 2/6); huMAP3_13615.1 (CAPN1, CAPN2; 2/7); huMAP3_14229.1 (CAPN1, CAPN2; 2/7); huMAP3_11557.1 (CAPN1, CAPN2; 2/8); huMAP3_12716.1 (CAPN1, CAPN2; 2/8); huMAP3_12926.1 (CAPN1, CAPN2; 2/8)

### Novelty

The module-level observation may be a new finding because the supplied evidence describes a conserved co-abundance pattern shared by cervix_uterine and myometrium, whereas STRING and hu.MAP mainly document selected pairwise interactions or partial complexes. The endoplasmic-reticulum processing theme is already established by (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0218) and (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0114), and the calpain and chaperone relationships are clearly known. Consequently, the biological components are not individually novel, and the module should not be claimed as a newly discovered molecular complex. A defensible novelty claim is instead that these established processes co-vary as a cross-tissue module in this tissue pair. That claim requires validation in independent cohorts, replication across platforms, cell-composition adjustment, and comparison with published co-expression or proteomic modules. Absence of a complete module from STRING or hu.MAP is not evidence that the module itself is novel.

**Hypothesis.** Hypothesis: a shared intracellular proteostasis state in cervix_uterine and myometrium coordinates endoplasmic-reticulum folding and COPII export with chaperone activity, calcium-dependent calpain proteolysis, organelle remodeling, and vesicle recycling. In this model, increased demand for protein folding or trafficking could co-vary with HSP90AA1, HSPA8, CANX, and SEC23A, while calcium-sensitive proteolysis through CAPN1 and CAPN2 and mitochondrial or endosomal remodeling through DNM1L and VPS35 adapt the cell to mechanical, metabolic, or stress-related demands. STAT1 and the supplementary necroptosis and antigen-processing associations suggest possible stress or inflammatory coupling, but the supplied data do not establish cytokine activation, cell death, or antigen presentation as the primary module function. This hypothesis should be tested with perturbation of ER proteostasis or calpain activity, followed by measurement of cargo trafficking, organelle morphology, and tissue-specific contractile or stromal phenotypes.

### Important genes

#### SEC23A

- **Related proteins** (co-abundance neighbors): ACO2 (0.89), DNM1L (0.87), CAPN2 (0.87), KATNAL2 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A is a central network connector and is one of the genes in the globally supported primary term (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0218). Its established role in COPII-coated vesicle budding, cargo loading, and ER-to-Golgi transport provides a direct mechanistic anchor for the module's strongest functional interpretation. It connects in the module to DNM1L, ACO2, CAPN2, and KATNAL2, although STRING does not report a supplied high-confidence partner for SEC23A. HPA places it in the endoplasmic reticulum and cytosol, with detection in cervix_uterine but not myometrium. Its disease and literature annotations show that it is biologically established but not among the most extensively studied genes in the module.
- **Conclusion**: Established evidence supports SEC23A as a trafficking component and as an important module anchor through (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0218). The hypothesis that its co-abundance marks altered secretory or ER export demand in both tissues is plausible but unproven.

#### CANX

- **Related proteins** (co-abundance neighbors): TARS1 (0.88), HSPA8 (0.85), CTPS1 (0.85), HSP90AA1 (0.84); STRING partners: HSP90AA1 (0.848)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is a network connector and a member of (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0218). It is an ER calcium-binding chaperone that assists folding and assembly of newly synthesized glycoproteins and participates in ER quality control and ER-associated degradation. Its STRING relationship with HSP90AA1 and module links to HSPA8, TARS1, and CTPS1 place it at the interface of folding, translation, and cellular biosynthetic activity. HPA detects it in both tissues and assigns it to the ER. Its substantial literature volume and disease associations involving infectious and neurodegenerative conditions reflect well-established, broad chaperone biology rather than tissue-specific novelty.
- **Conclusion**: Established evidence makes CANX a strong indicator of ER folding and quality control within the module. It could report proteostatic demand in the shared tissues, but co-abundance alone cannot determine whether it is causal or merely a marker of cellular protein synthesis.

#### CAPN1

- **Related proteins** (co-abundance neighbors): FERMT2 (0.92), ACO1 (0.84), PLCD1 (0.83), VPS35 (0.82); STRING partners: CAPN2 (0.978)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: huMAP3_03767.1, huMAP3_08670.1, huMAP3_09127.1, huMAP3_09328.1, huMAP3_10242.1, huMAP3_13615.1, huMAP3_14229.1, huMAP3_11557.1, huMAP3_12716.1, huMAP3_12926.1
- **Function (MyGene.info)**: calpain 1. The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpa…
- **Diseases (Open Targets)**: Autosomal recessive spastic paraplegia type 76 (0.781); Alzheimer disease (0.383); neurodegenerative disease (0.326); hereditary spastic paraplegia 11 (0.266); hereditary disease (0.193)
- **Europe PMC papers**: 1869
- **Why important**: CAPN1 has a relatively connected position in the module and links to FERMT2, ACO1, PLCD1, and VPS35. It is part of (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0218), has a very strong STRING relationship with CAPN2, and is present with CAPN2 across the hu.MAP calpain complexes (hu.MAP huMAP3_03767.1) through (hu.MAP huMAP3_12926.1). Its established function as a calcium-activated intracellular cysteine protease provides a mechanism connecting calcium signaling, cytoskeletal or adhesion remodeling, and proteolysis. HPA detects it in both tissues and reports enhancement in esophageal and selected cell populations, including smooth muscle-related annotations. It has extensive literature and disease associations involving neurological and hereditary disorders.
- **Conclusion**: Established evidence identifies CAPN1 as a major calpain-complex component and a plausible effector of calcium-dependent remodeling. Its participation in ER proteostasis or tissue-specific mechanical adaptation is a hypothesis derived from the module context, not a demonstrated function of this module.

#### CAPN2

- **Related proteins** (co-abundance neighbors): SEC23A (0.87), DNM1L (0.82); STRING partners: CAPN1 (0.978)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Connecting piece, Mid piece; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_03767.1, huMAP3_08670.1, huMAP3_09127.1, huMAP3_09328.1, huMAP3_10242.1, huMAP3_13615.1, huMAP3_14229.1, huMAP3_11557.1, huMAP3_12716.1, huMAP3_12926.1
- **Function (MyGene.info)**: calpain 2. The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpa…
- **Diseases (Open Targets)**: Alzheimer disease (0.389); urolithiasis (0.288); alcohol drinking (0.288); aortic stenosis (0.141); neoplasm (0.105)
- **Europe PMC papers**: 1796
- **Why important**: CAPN2 is included in (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0218), connects to SEC23A and DNM1L, and forms the strongest supplied STRING pair with CAPN1. Its repeated co-membership with CAPN1 in hu.MAP complexes (hu.MAP huMAP3_03767.1) through (hu.MAP huMAP3_12926.1) provides unusually consistent complex-level support. CAPN2 is a calcium-regulated intracellular protease associated in the supplied annotations with proteolysis, hypoxia response, mechanical stimulus, and pregnancy-related biology. HPA detects it in cervix_uterine but not myometrium and reports enhancement in selected epithelial cell populations. Its disease and literature evidence is substantial.
- **Conclusion**: Established evidence supports CAPN2 as the second core calpain component and as a bridge between proteolysis, trafficking, and organelle-remodeling signals. A role in adapting shared uterine tissues to mechanical or ER stress is a reasonable hypothesis, but it requires direct functional testing.

#### HSP90AA1

- **Related proteins** (co-abundance neighbors): HSPA8 (0.87), CANX (0.84); STRING partners: CANX (0.848), HSPA8 (0.999), STAT1 (0.868)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein 90 alpha family class A member 1. The protein encoded by this gene is an inducible molecular chaperone that functions as a homodimer. The encoded protein aids in the proper folding of specific target proteins by use of an ATPase activity that is modulated by co-chaperones. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: cancer (0.643); plasma cell myeloma (0.404); non-small cell lung carcinoma (0.394); dengue disease (0.375); Orthomyxoviridae infectious disease (0.375)
- **Europe PMC papers**: 8215
- **Why important**: HSP90AA1 is part of (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0218) and appears in every supplementary STRING category supplied for this module (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0114) through (STRING KEGG Antigen processing and presentation; within-query FDR = 0.0481). It has established high-confidence STRING relationships with HSPA8, CANX, and STAT1, placing it at the center of the chaperone and stress-associated part of the network despite a modest direct degree in the co-abundance graph. It is an inducible molecular chaperone that supports folding of specific client proteins and is linked in the annotations to defense responses and muscle contraction. HPA detects it in cervix_uterine but not myometrium. It has the largest literature volume among the highlighted genes and broad disease associations, so it is biologically important but not a novel marker by itself.
- **Conclusion**: Established evidence supports HSP90AA1 as a proteostasis hub connecting ER chaperoning, cytosolic chaperoning, and STAT1-associated signaling. The hypothesis that it coordinates a stress-responsive state across the two tissues is consistent with the evidence, but the module does not prove activation of an inflammatory or cell-death program.

#### DNM1L

- **Related proteins** (co-abundance neighbors): SEC23A (0.87), TARS1 (0.86), STAT1 (0.84), VPS35 (0.82), CAPN2 (0.82); STRING partners: VPS35 (0.9)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 1L. This gene encodes a member of the dynamin superfamily of GTPases. The encoded protein mediates mitochondrial and peroxisomal division, and is involved in developmentally regulated apoptosis and programmed necrosis. Dysfunction of this gene is implicated in several neurological disorders, including Alzheimer's disease. Mutations in this gene are associated with the autosomal dominant disorder, ence…
- **Diseases (Open Targets)**: encephalopathy, lethal, due to defective mitochondrial peroxisomal fission 1 (0.815); autosomal dominant optic atrophy, classic form (0.721); neurodegenerative disease (0.531); encephalopathy due to mitochondrial and peroxisomal fission defect (0.455); hereditary disease (0.451)
- **Europe PMC papers**: 3015
- **Why important**: DNM1L has the highest weighted connectivity in the supplied module and links SEC23A, TARS1, STAT1, VPS35, and CAPN2. Its STRING relationship with VPS35 connects mitochondrial or peroxisomal division with endosomal trafficking, while its supplementary membership in necroptosis and perinuclear-region terms (STRING KEGG Necroptosis; within-query FDR = 0.0123) (STRING Component Perinuclear region of cytoplasm; within-query FDR = 0.0473) provides context for organelle remodeling and stress responses. The gene is established as a dynamin-family GTPase involved in mitochondrial and peroxisomal fission, apoptosis-related processes, and endoplasmic-reticulum organization. HPA detects it in both tissues, and its disease associations include mitochondrial fission disorders and neurodegenerative conditions.
- **Conclusion**: Established evidence supports DNM1L as an organelle-remodeling and trafficking connector in the module. Its position makes it a strong candidate for coupling proteostasis with mitochondrial adaptation, but the proposed coupling in cervix_uterine and myometrium remains a hypothesis rather than a demonstrated mechanism.

## Module 3

**Tissue pair**: cervix_uterine and myometrium  
**Genes (12)**: ALB, APOA1, C9, FBLN1, IGHA1, IGHG1, IGHG2, IGHG3, IGKC, LUM, F2, TF

### Function

The strongest interpretation is a circulating humoral-defense and blood-associated extracellular module. The primary evidence is the globally corrected enrichment for blood microparticle (GO:CC blood microparticle; q_global = 0.000698), antimicrobial humoral response (GO:BP antimicrobial humoral response; q_global = 0.00132), humoral immune response (GO:BP humoral immune response; q_global = 0.00196), bacterial defense (GO:BP defense response to bacterium; q_global = 0.00875), antibacterial humoral response (GO:BP antibacterial humoral response; q_global = 0.0105), classical complement activation (GO:BP complement activation, classical pathway; q_global = 0.0191), IgG immunoglobulin complex (GO:CC IgG immunoglobulin complex; q_global = 0.0272), and circulating-immunoglobulin-mediated humoral response (GO:BP humoral immune response mediated by circulating immunoglobulin; q_global = 0.0314). Together, these terms support coordinated abundance of immunoglobulin, complement, coagulation, iron-transport, and plasma-carrier proteins rather than a cervix- or myometrium-specific intracellular pathway. FBLN1 and LUM add an extracellular-matrix component, but neither has a globally corrected GO/KEGG annotation in this module. The co-abundance structure is therefore most plausibly a shared extracellular or blood-derived protein signal, with a possible contribution from local immune and stromal cells.

**Cell composition.** The module is strongly dominated by secreted proteins and immunoglobulin genes. HPA classifies every module gene as secreted, with liver and hepatocyte enrichment prominent for ALB, APOA1, F2, C9, and TF, and lymphoid tissue, plasma-cell, and B-cell enrichment prominent for IGHA1, IGHG1, IGHG2, IGHG3, and IGKC. The HPA blood-cell evidence particularly supports a plasma-cell or B-cell contribution. Protein detection is limited or absent for most module proteins in both cervix_uterine and myometrium, while FBLN1 is detected in both tissues and selected immunoglobulins are detected in cervix_uterine or myometrium. This pattern cautions that the shared module may reflect plasma leakage, blood microparticles, vascular content, or shared immune-cell content rather than production by the principal uterine tissue cells. It is not a housekeeping module.

**GO/KEGG enrichment**: 8 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 0.000698 | ALB, APOA1, C9, F2, IGHA1, IGHG1, IGHG2, TF |
| GO:BP antimicrobial humoral response | 0.00132 | F2, IGHA1, IGHG1, IGHG2, TF |
| GO:BP humoral immune response | 0.00196 | C9, F2, IGHA1, IGHG1, IGHG2, TF |
| GO:BP defense response to bacterium | 0.00875 | F2, IGHA1, IGHG1, IGHG2, TF |
| GO:BP antibacterial humoral response | 0.0105 | IGHA1, IGHG1, IGHG2, TF |
| GO:BP complement activation, classical pathway | 0.0191 | C9, IGHA1, IGHG1, IGHG2 |
| GO:CC IgG immunoglobulin complex | 0.0272 | IGHA1, IGHG1, IGHG2 |
| GO:BP humoral immune response mediated by circulating immunoglobulin | 0.0314 | C9, IGHA1, IGHG1, IGHG2 |

### STRING and hu.MAP

STRING supports a known plasma-protein interaction neighborhood among ALB, APOA1, F2, and TF, including the ALB–APOA1, ALB–F2, ALB–TF, APOA1–F2, APOA1–TF, and F2–TF relationships. STRING also connects ALB with LUM, while the supplementary annotations associate the network with secretion, extracellular space, blood microparticles, complement and coagulation, and protein-lipid complexes (15 supplementary STRING terms; within-query FDR 0.0001–0.0329). These are supplementary annotations and do not replace the globally corrected GO/KEGG evidence. hu.MAP independently places F2, APOA1, ALB, and TF together in several plasma-protein complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_15040.1), and APOA1 with TF in another complex (hu.MAP huMAP3_08224.1). Thus, part of the module is a known plasma-protein assembly or interaction neighborhood. The immunoglobulin genes have no recorded STRING partners or hu.MAP complexes here, so their co-abundance is better interpreted as a coordinated immune-cell or immunoglobulin signal than as demonstrated physical binding within this dataset.

**STRING interactions (score >= 0.7)**: 7 of 66 gene pairs: ALB–APOA1 (0.998); ALB–F2 (0.99); ALB–LUM (0.737); ALB–TF (0.9); APOA1–F2 (0.927); APOA1–TF (0.919); F2–TF (0.725)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Secreted (FDR = 0.0001, 7 genes); Keyword Signal (FDR = 0.0002, 7 genes); Keyword Glycoprotein (FDR = 0.00025, 7 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 0.0017, 7 genes); NetworkNeighborAL Complement and coagulation cascades, and Protein-lipid complex (FDR = 0.0039, 5 genes); Keyword Disulfide bond (FDR = 0.0042, 6 genes); PMID (2014) Proteomic analysis of human plasma in chronic rheumatic mitral stenosis reveals proteins involved in the complement and coagulation cascade. (FDR = 0.0052, 6 genes); COMPARTMENTS Extracellular space (FDR = 0.0065, 7 genes); COMPARTMENTS Blood microparticle (FDR = 0.0072, 5 genes); NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization (FDR = 0.0093, 4 genes); Component Blood microparticle (FDR = 0.0142, 5 genes); RCTM Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) (FDR = 0.0292, 4 genes); PMID (2023) Dysregulation of metalloproteins in ischemic heart disease patients with systolic dysfunction. (FDR = 0.0329, 4 genes); PMID (2023) Characterization of the Protein Corona of Three Chairside Hemoderivatives on Melt Electrowritten Polycaprolactone Scaffolds. (FDR = 0.0329, 4 genes); PMID (2022) Comparative Proteomic Assessment of Normal vs. Polyhydramnios Amniotic Fluid Based on Computational Analysis. (FDR = 0.0329, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08395.1 (F2, APOA1, ALB, TF; 4/43); huMAP3_09531.1 (F2, APOA1, ALB, TF; 4/47); huMAP3_10101.1 (F2, APOA1, ALB, TF; 4/49); huMAP3_10678.1 (F2, APOA1, ALB, TF; 4/71); huMAP3_07432.1 (APOA1, ALB, TF; 3/18); huMAP3_07265.1 (APOA1, ALB, TF; 3/20); huMAP3_09434.1 (APOA1, ALB, TF; 3/33); huMAP3_15040.1 (APOA1, ALB, TF; 3/64); huMAP3_08224.1 (APOA1, TF; 2/21)

### Novelty

A new tissue-pair co-abundance observation may be present, but the module should not be claimed as a newly discovered molecular complex or pathway. Its central relationships and functional themes are already represented by STRING, hu.MAP, and established protein functions, while the immunoglobulin component is a familiar plasma-cell signature. The potentially distinctive aspect is the recurrence of this mixed plasma, humoral-defense, coagulation, and extracellular-matrix signal across cervix_uterine and myometrium. That recurrence could be biologically meaningful, but it could also arise from shared vascular or immune-cell content, sample handling, or plasma carryover. Demonstrating novelty would require independent tissue-level replication, cell-type-aware measurements, and comparison with existing uterine proteomic or transcriptomic modules.

**Hypothesis.** Hypothesis: the shared module represents a vascular or extracellular-fluid interface in which liver-derived plasma proteins and immunoglobulins enter, or are sampled together with, cervix_uterine and myometrium tissue. The immunoglobulin component may reflect local or infiltrating plasma cells, while F2, C9, TF, ALB, and APOA1 may provide coagulation, complement, iron-transport, and lipid-carrier functions in the same extracellular milieu. FBLN1 and LUM could couple this blood-associated signal to the local extracellular matrix. This model predicts that the module will track vascularity, plasma exposure, immune-cell abundance, or tissue injury more strongly than the abundance of uterine contractile-cell markers. It remains a hypothesis because co-abundance does not establish secretion by the tissue, physical interaction, or causal activity in either tissue.

### Important genes

#### ALB

- **Related proteins** (co-abundance neighbors): IGHG1 (0.86), LUM (0.81), FBLN1 (0.81), TF (0.80); STRING partners: APOA1 (0.998), F2 (0.99), LUM (0.737), TF (0.9)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_15040.1
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB is a highly connected bridge in the module and links the immunoglobulin-associated side of the network with LUM, FBLN1, and TF. HPA identifies it as liver-enriched, hepatocyte-enriched, and secreted to blood, and MyGene.info describes its role as the most abundant blood protein and a carrier of diverse endogenous and exogenous molecules. It is present in the strongest STRING plasma-protein relationships and in many hu.MAP plasma complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_15040.1), while also contributing to the primary blood-microparticle evidence (GO:CC blood microparticle; q_global = 0.000698). Its large literature base and disease associations make it an informative marker of systemic plasma contribution.
- **Conclusion**: Established evidence supports ALB as a central plasma-carrier and extracellular marker, not as evidence that cervix_uterine or myometrium synthesizes ALB. In this module, ALB most likely reports blood or extracellular-fluid content and helps connect otherwise distinct protein groups.

#### F2

- **Related proteins** (co-abundance neighbors): TF (0.84); STRING partners: ALB (0.99), APOA1 (0.927), TF (0.725)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: coagulation factor II, thrombin. This gene encodes the prothrombin protein (also known as coagulation factor II). This protein is proteolytically cleaved in multiple steps to form the activated serine protease thrombin. The activated thrombin enzyme plays an important role in thrombosis and hemostasis by converting fibrinogen to fibrin during blood clot formation, by stimulating platelet aggregation, and by activating additional …
- **Diseases (Open Targets)**: congenital prothrombin deficiency (0.827); thrombophilia due to thrombin defect (0.738); venous thromboembolism (0.727); deep vein thrombosis (0.690); blood coagulation disease (0.670)
- **Europe PMC papers**: 109299
- **Why important**: F2 occupies a network bridge between TF and the ALB–APOA1 plasma-protein neighborhood and occurs in the primary humoral and bacterial-defense terms (6 globally significant GO/KEGG terms, q_global 0.000698–0.0191; see the table). It is liver- and hepatocyte-enriched, secreted to blood, and encodes prothrombin, whose activated product participates in coagulation, platelet activation, tissue repair, and angiogenesis. It has strong STRING relationships with ALB, APOA1, and TF and appears in several hu.MAP plasma complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1). Its extensive literature and coagulation-related disease associations make it a strong indicator of vascular or hemostatic context.
- **Conclusion**: Established evidence supports F2 as a circulating coagulation protein embedded in a known plasma-protein neighborhood. A possible local role in uterine tissue repair or vascular remodeling is biologically plausible, but it is not demonstrated by this co-abundance module.

#### TF

- **Related proteins** (co-abundance neighbors): F2 (0.84), FBLN1 (0.81), ALB (0.80); STRING partners: ALB (0.9), APOA1 (0.919), F2 (0.725)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_15040.1, huMAP3_08224.1
- **Function (MyGene.info)**: transferrin. This gene encodes a glycoprotein with an approximate molecular weight of 76.5 kDa. It is thought to have been created as a result of an ancient gene duplication event that led to generation of homologous C and N-terminal domains each of which binds one ion of ferric iron. The function of this protein is to transport iron from the intestine, reticuloendothelial system, and liver parenchymal cells t…
- **Diseases (Open Targets)**: atransferrinemia (0.776); alcohol drinking (0.492); hemochromatosis type 1 (0.471); neurodegenerative disease (0.400); urolithiasis (0.329)
- **Europe PMC papers**: 143656
- **Why important**: TF is a network bridge connecting F2, FBLN1, and ALB and contributes to the primary blood-microparticle and humoral-defense evidence (5 globally significant GO/KEGG terms, q_global 0.000698–0.0105; see the table). HPA supports liver and hepatocyte enrichment and secretion to blood. MyGene.info identifies transferrin as an iron-transport glycoprotein, and its STRING relationships with ALB, APOA1, and F2, together with repeated hu.MAP membership (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08224.1), place it at the core of the known plasma-protein organization. It also has a very large literature base and disease associations involving iron handling.
- **Conclusion**: Established evidence supports TF as a circulating iron-transport protein and structural marker of the plasma component. Its presence does not establish iron-starvation or altered iron metabolism in either uterine tissue; those would require independent functional measurements.

#### IGHA1

- **Related proteins** (co-abundance neighbors): IGHG2 (0.92), IGHG1 (0.90), IGHG3 (0.86), IGKC (0.84); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Group enriched; location None; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: immunoglobulin heavy constant alpha 1
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 1712
- **Why important**: IGHA1 is one of the most connected immunoglobulin genes in the module and links IGHG2, IGHG1, IGHG3, and IGKC. It contributes to every primary GO/KEGG term (8 globally significant GO/KEGG terms, q_global 0.000698–0.0314; see the table). HPA identifies plasma-cell enrichment and association with memory and naive B-cell populations, with detection in myometrium but not cervix_uterine. Its substantial literature base supports a well-established immunoglobulin role, although it has no recorded STRING partner or hu.MAP complex in this dataset.
- **Conclusion**: Established evidence supports IGHA1 as a marker of immunoglobulin and plasma-cell abundance contributing to humoral defense. The module does not show that IGHA1 physically interacts with the other module proteins or that local uterine plasma cells are the source; circulating or infiltrating immunoglobulin remain alternatives.

#### C9

- **Related proteins** (co-abundance neighbors): FBLN1 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C9. This gene encodes the final component of the complement system. It participates in the formation of the Membrane Attack Complex (MAC). The MAC assembles on bacterial membranes to form a pore, permitting disruption of bacterial membrane organization. Mutations in this gene cause component C9 deficiency. [provided by RefSeq, Feb 2009].
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.747); age-related macular degeneration (0.584); complement component 9 deficiency (0.548); macular degeneration (0.541); complement deficiency (0.463)
- **Europe PMC papers**: 28081
- **Why important**: C9 contributes to the primary blood-microparticle, humoral-immune, complement, and circulating-immunoglobulin terms (GO:CC blood microparticle; q_global = 0.000698), (GO:BP humoral immune response; q_global = 0.00196), (GO:BP complement activation, classical pathway; q_global = 0.0191), and (GO:BP humoral immune response mediated by circulating immunoglobulin; q_global = 0.0314). HPA identifies liver and hepatocyte enrichment and secretion to blood. MyGene.info describes C9 as the terminal complement component that forms the membrane attack complex, and its disease associations include complement C9 deficiency and immunodeficiency. Although it lacks a recorded STRING partner or hu.MAP complex here, its functional annotation gives the module a direct complement-effector component.
- **Conclusion**: Established evidence supports C9 as a circulating terminal complement effector and a meaningful indicator of humoral-defense potential. Whether complement is actively engaged in cervix_uterine or myometrium cannot be inferred from its co-abundance alone.

#### FBLN1

- **Related proteins** (co-abundance neighbors): C9 (0.82), TF (0.81), ALB (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibulin 1. Fibulin 1 is a secreted glycoprotein that becomes incorporated into a fibrillar extracellular matrix. Calcium-binding is apparently required to mediate its binding to laminin and nidogen. It mediates platelet adhesion via binding fibrinogen. Four splice variants which differ in the 3' end have been identified. Each variant encodes a different isoform, but no functional distinctions have been ident…
- **Diseases (Open Targets)**: synpolydactyly type 2 (0.447); FBLN1-related developmental delay-central nervous system anomaly-syndactyly syndrome (0.377); synpolydactyly (0.371); adolescent idiopathic scoliosis (0.306); alcohol drinking (0.219)
- **Europe PMC papers**: 2655
- **Why important**: FBLN1 connects C9 and TF to ALB in the co-abundance graph and is the clearest tissue-matrix-facing member of the module. HPA identifies extracellular-matrix secretion and detection in both cervix_uterine and myometrium, with enrichment or enhancement in decidual, endometrial, and related stromal cell types. MyGene.info describes incorporation into fibrillar extracellular matrix, binding to laminin and nidogen, platelet adhesion, and roles in cell adhesion and matrix organization. It has no STRING partner or hu.MAP complex recorded here, but it provides a biologically plausible interface between plasma-associated proteins and uterine stroma.
- **Conclusion**: Established evidence supports FBLN1 as a secreted extracellular-matrix protein with relevance to the tissues represented in the module. Its co-abundance with plasma proteins may indicate matrix–vascular coupling, but direct binding or causal coordination with C9, TF, or ALB remains a hypothesis.

## Module 4

**Tissue pair**: cervix_uterine and myometrium  
**Genes (6)**: SERPINC1, AHSG, FGG, KNG1, SELENBP1, VTN

### Function

The module is most strongly characterized by regulation of coagulation and hemostasis, wound response, and complement/coagulation biology, supported by the globally corrected terms (GO:BP regulation of blood coagulation; q_global = 0.00318), (GO:BP regulation of hemostasis; q_global = 0.00318), (GO:BP regulation of coagulation; q_global = 0.00467), (GO:BP regulation of wound healing; q_global = 0.0104), (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.0104), and (GO:BP regulation of response to wounding; q_global = 0.0119). The endoplasmic-reticulum-lumen and blood-microparticle terms (GO:CC endoplasmic reticulum lumen; q_global = 0.00604) and (GO:CC blood microparticle; q_global = 0.0168) indicate that the proteins are predominantly secreted or circulating rather than components of a cervix or myometrium intracellular pathway. FGG, KNG1, SERPINC1, and VTN drive the coagulation-related enrichment, while AHSG contributes to the secreted protein and blood-microparticle pattern. SELENBP1 is connected in the co-abundance subgraph but has no GO or KEGG term in the fact sheet, so its specific role in this module remains uncertain.

**Cell composition.** This is predominantly a plasma and secreted-protein module. HPA annotates five module genes as secreted to blood or otherwise secreted, and all genes show liver tissue enrichment or enhancement, with hepatocytes the recurring enriched cell type. The proteins were not detected by IHC in either cervix_uterine or myometrium. Most module genes were not detected in immune cells, so the evidence does not support a blood-cell-enriched module. These observations strongly suggest that the shared tissue association may reflect circulating plasma proteins, sample blood content, or a shared vascular or extracellular component rather than expression by uterine or cervical cells. SELENBP1 differs from the other genes: it is tissue-enhanced in intestine, has nucleolar localization, lacks a secreted annotation, and is associated with an immune-cell-enhanced pattern involving myeloid dendritic cells.

**GO/KEGG enrichment**: 8 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulation of blood coagulation | 0.00318 | FGG, KNG1, SERPINC1, VTN |
| GO:BP regulation of hemostasis | 0.00318 | FGG, KNG1, SERPINC1, VTN |
| GO:BP regulation of coagulation | 0.00467 | FGG, KNG1, SERPINC1, VTN |
| GO:CC endoplasmic reticulum lumen | 0.00604 | AHSG, FGG, KNG1, SERPINC1, VTN |
| GO:BP regulation of wound healing | 0.0104 | FGG, KNG1, SERPINC1, VTN |
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 0.0104 | FGG, KNG1, SERPINC1, VTN |
| GO:BP regulation of response to wounding | 0.0119 | FGG, KNG1, SERPINC1, VTN |
| GO:CC blood microparticle | 0.0168 | AHSG, FGG, KNG1, SERPINC1, VTN |

### STRING and hu.MAP

STRING supports a coherent, already known interaction neighborhood among AHSG, FGG, KNG1, SERPINC1, and VTN. The strongest reported relationships include AHSG with FGG, AHSG with KNG1, FGG with SERPINC1, and SERPINC1 with VTN, with additional links connecting the same proteins. STRING enrichment independently recovers complement and coagulation cascades, blood coagulation, fibrin-clot formation, secreted proteins, endoplasmic-reticulum lumen, blood microparticles, and collagen-containing extracellular matrix (5 supplementary STRING terms; within-query FDR 0.0025–0.0044), (STRING Process Regulation of blood coagulation; within-query FDR = 0.0097), (STRING RCTM Formation of Fibrin Clot (Clotting Cascade); within-query FDR = 0.0182), and (STRING Keyword Secreted; within-query FDR = 0.0226). These are supplementary confirmations rather than globally corrected enrichment evidence. hu.MAP places SERPINC1, KNG1, FGG, and AHSG together in a higher-confidence complex (hu.MAP huMAP3_15040.1), and repeatedly places subsets of KNG1, FGG, and AHSG in related plasma-protein complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1). Thus, much of the module reflects a known extracellular and plasma-protein interaction environment. SELENBP1 has no listed STRING partner and no hu.MAP complex, making its co-abundance links less supported by prior molecular-interaction resources.

**STRING interactions (score >= 0.7)**: 10 of 15 gene pairs: AHSG–FGG (0.97); AHSG–KNG1 (0.936); AHSG–SERPINC1 (0.838); AHSG–VTN (0.782); FGG–KNG1 (0.917); FGG–SERPINC1 (0.921); FGG–VTN (0.721); KNG1–SERPINC1 (0.758); KNG1–VTN (0.803); SERPINC1–VTN (0.949)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Complement and coagulation cascades (FDR = 0.0025, 4 genes); Component Endoplasmic reticulum lumen (FDR = 0.0026, 5 genes); Component Blood microparticle (FDR = 0.0026, 5 genes); Component Collagen-containing extracellular matrix (FDR = 0.0032, 5 genes); COMPARTMENTS Blood microparticle (FDR = 0.0044, 5 genes); RCTM Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) (FDR = 0.0096, 4 genes); RCTM Post-translational protein phosphorylation (FDR = 0.0096, 4 genes); Process Regulation of blood coagulation (FDR = 0.0097, 4 genes); RCTM Formation of Fibrin Clot (Clotting Cascade) (FDR = 0.0182, 3 genes); Process Regulation of response to external stimulus (FDR = 0.0208, 5 genes); PMID (2019) The Critical Role of Codon Composition on the Translation Efficiency Robustness of the Hepatitis A Virus Capsid. (FDR = 0.022, 4 genes); PMID (2016) Human plasma protein N-glycosylation. (FDR = 0.022, 5 genes); Keyword Blood coagulation (FDR = 0.0226, 3 genes); Keyword Secreted (FDR = 0.0226, 5 genes); Keyword Signal (FDR = 0.0254, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINC1, KNG1, FGG, AHSG; 4/64); huMAP3_08395.1 (KNG1, FGG, AHSG; 3/43); huMAP3_09531.1 (KNG1, FGG, AHSG; 3/47); huMAP3_10101.1 (KNG1, FGG, AHSG; 3/49); huMAP3_10678.1 (KNG1, FGG, AHSG; 3/71); huMAP3_02242.1 (FGG, AHSG; 2/9); huMAP3_07541.1 (KNG1, FGG; 2/19); huMAP3_07265.1 (KNG1, AHSG; 2/20); huMAP3_09434.1 (FGG, AHSG; 2/33)

### Novelty

The molecular function represented by the module is not new: coagulation, fibrinogen biology, kininogen biology, antithrombin activity, vitronectin biology, and plasma-protein complexes are well established. The co-abundance observation shared by cervix_uterine and myometrium could still be a new tissue-pair-specific finding, but the fact sheet does not provide a direct comparison with previously published co-abundance modules or datasets. Absence of SELENBP1 from STRING and hu.MAP does not establish novelty, because database coverage and evidence types are incomplete. The most defensible conclusion is that the module-level tissue observation may be novel, whereas its dominant biological content is established and is plausibly driven by circulating-protein carryover or shared extracellular material.

**Hypothesis.** Hypothesis: the shared module mainly reflects a common plasma or vascular signal present in both tissue sample types, rather than a locally synthesized uterine or cervical program. Liver-derived secreted proteins may enter the sampled tissue material through blood or extracellular fluid and co-vary as a group. Within this signal, FGG could represent clot-forming potential, SERPINC1 an inhibitory counterweight to coagulation, KNG1 a link to the kallikrein–kinin and coagulation systems, and VTN an adhesive extracellular-matrix interface. AHSG may accompany this circulating glycoprotein environment, while SELENBP1 may reflect an additional sample-composition or tissue-associated covariation signal. This hypothesis should be tested with blood-contamination markers, matched plasma measurements, cell-type deconvolution, and validation of local transcript or protein production.

### Important genes

#### SERPINC1

- **Related proteins** (co-abundance neighbors): KNG1 (0.92), VTN (0.85), AHSG (0.82); STRING partners: AHSG (0.838), FGG (0.921), KNG1 (0.758), VTN (0.949)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 has the strongest weighted network position in the module and connects to KNG1, VTN, and AHSG. It appears in every globally corrected term (8 globally significant GO/KEGG terms, q_global 0.00318–0.0168; see the table), is central to the STRING coagulation neighborhood (15 supplementary STRING terms; within-query FDR 0.0025–0.0254), and belongs to the higher-confidence hu.MAP complex (hu.MAP huMAP3_15040.1). Its encoded antithrombin is an established plasma inhibitor of thrombin and other activated coagulation proteases. The disease associations in the fact sheet include hereditary antithrombin deficiency and venous thromboembolism, and its extensive literature supports a well-established role.
- **Conclusion**: Established evidence identifies SERPINC1 as a central circulating regulator of coagulation and a major anchor of the module. The module data do not establish local SERPINC1 production in cervix_uterine or myometrium; the absent tissue IHC signal favors a circulating or sample-composition explanation.

#### KNG1

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.92), SELENBP1 (0.83); STRING partners: AHSG (0.936), FGG (0.917), SERPINC1 (0.758), VTN (0.803)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07541.1, huMAP3_07265.1
- **Function (MyGene.info)**: kininogen 1. This gene uses alternative splicing to generate two different proteins- high molecular weight kininogen (HMWK) and low molecular weight kininogen (LMWK). HMWK is essential for blood coagulation and assembly of the kallikrein-kinin system. Also, bradykinin, a peptide causing numerous physiological effects, is released from HMWK. Bradykinin also functions as an antimicrobial peptide with antibacteri…
- **Diseases (Open Targets)**: congenital high-molecular-weight kininogen deficiency (0.733); venous thromboembolism (0.547); hereditary angioedema (0.458); serum lipopolysaccharide activity (0.367); ischemic stroke (0.363)
- **Europe PMC papers**: 2325
- **Why important**: KNG1 has a strong network position, connects to SERPINC1 and SELENBP1 in the co-abundance subgraph, appears in every globally corrected term (8 globally significant GO/KEGG terms, q_global 0.00318–0.0168; see the table), and occurs across multiple hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_07541.1), and (hu.MAP huMAP3_07265.1). Its high-molecular-weight product is established as a component of coagulation and the kallikrein–kinin system, while cleavage releases bradykinin with vasodilatory and other physiological effects. The fact sheet links it to congenital high-molecular-weight kininogen deficiency, hereditary angioedema, and thromboembolic disease, with substantial literature support.
- **Conclusion**: Established evidence places KNG1 at the interface of coagulation, kinin signaling, and vascular physiology. Its joint abundance with the plasma-protein genes is consistent with a circulating hemostatic signal, but the data do not show that KNG1 is produced locally by either target tissue.

#### FGG

- **Related proteins** (co-abundance neighbors): SELENBP1 (0.84); STRING partners: AHSG (0.97), KNG1 (0.917), SERPINC1 (0.921), VTN (0.721)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_02242.1, huMAP3_07541.1, huMAP3_09434.1
- **Function (MyGene.info)**: fibrinogen gamma chain. The protein encoded by this gene is the gamma component of fibrinogen, a blood-borne glycoprotein comprised of three pairs of nonidentical polypeptide chains. Following vascular injury, fibrinogen is cleaved by thrombin to form fibrin which is the most abundant component of blood clots. In addition, various cleavage products of fibrinogen and fibrin regulate cell adhesion and spreading, display va…
- **Diseases (Open Targets)**: familial dysfibrinogenemia (0.787); congenital afibrinogenemia (0.753); congenital fibrinogen deficiency (0.617); familial hypodysfibrinogenemia (0.597); cancer (0.596)
- **Europe PMC papers**: 4006
- **Why important**: FGG is present in every globally corrected term (8 globally significant GO/KEGG terms, q_global 0.00318–0.0168; see the table), has strong STRING relationships with AHSG, KNG1, SERPINC1, and VTN, and recurs in the hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_07541.1) and (hu.MAP huMAP3_09434.1). It encodes the gamma chain of fibrinogen, an established blood-borne glycoprotein whose thrombin-cleaved product forms fibrin and whose fragments influence adhesion, spreading, vascular tone, chemotaxis, and cell proliferation. The fact sheet associates it with familial dysfibrinogenemia and congenital fibrinogen deficiencies and reports extensive literature.
- **Conclusion**: Established evidence identifies FGG as a core clotting and extracellular-response component that explains much of the module’s enrichment. Its abundance is more readily interpreted as plasma or blood-microparticle carryover than as evidence for fibrinogen synthesis by cervix_uterine or myometrium.

#### VTN

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.85); STRING partners: AHSG (0.782), FGG (0.721), KNG1 (0.803), SERPINC1 (0.949)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vitronectin. The protein encoded by this gene functions in part as an adhesive glycoprotein. Differential expression of this protein can promote either cell adhesion or migration as it links cells to the extracellular matrix through a variety of ligands. These ligands include integrins, plasminogen activator inhibitor-1, and urokinase plasminogen activator receptor. This secreted protein can be present in the …
- **Diseases (Open Targets)**: hypertensive disorder (0.421); dengue disease (0.376); neurodegenerative disease (0.343); temporal arteritis (0.338); age-related macular degeneration (0.313)
- **Europe PMC papers**: 3940
- **Why important**: VTN connects to SERPINC1 in the co-abundance subgraph and has STRING links to all of the principal plasma-protein members. It contributes to every globally corrected term (8 globally significant GO/KEGG terms, q_global 0.00318–0.0168; see the table). Vitronectin is an established secreted adhesive glycoprotein that links integrins, plasminogen-activator-related ligands, and extracellular matrix, and the fact sheet specifically notes roles in cell adhesion, cell-matrix adhesion, integrin signaling, and smooth-muscle-cell migration. Its liver enrichment, blood secretion, vesicular or endoplasmic-reticulum localization, and absence of target-tissue IHC detection are especially informative for interpreting the module.
- **Conclusion**: Established evidence supports VTN as the module’s extracellular-adhesion and matrix-interface component. Its co-abundance could influence how circulating material interacts with uterine or cervical extracellular matrix, but a local mechanistic role remains a hypothesis because tissue protein was not detected.

#### AHSG

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.82); STRING partners: FGG (0.97), KNG1 (0.936), SERPINC1 (0.838), VTN (0.782)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_02242.1, huMAP3_07265.1, huMAP3_09434.1
- **Function (MyGene.info)**: alpha 2-HS glycoprotein. The protein encoded by this gene is a negatively-charged serum glycoprotein that is synthesized by hepatocytes. The encoded protein consists of two polypeptide chains, which are both cleaved from a proprotein encoded from a single mRNA. It is involved in several processes, including endocytosis, brain development, and the formation of bone tissue. Defects in this gene are a cause of susceptibility…
- **Diseases (Open Targets)**: alopecia - intellectual disability syndrome (0.476); otosclerosis (0.465); nephrolithiasis, calcium oxalate (0.417); calcium oxalate urolithiasis (0.416); neurodegenerative disease (0.204)
- **Europe PMC papers**: 2310
- **Why important**: AHSG has a direct co-abundance connection to SERPINC1 and strong STRING relationships with FGG, KNG1, SERPINC1, and VTN. It contributes to the endoplasmic-reticulum-lumen and blood-microparticle terms (GO:CC endoplasmic reticulum lumen; q_global = 0.00604) and (GO:CC blood microparticle; q_global = 0.0168) and recurs in many hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_02242.1), (hu.MAP huMAP3_07265.1), and (hu.MAP huMAP3_09434.1). It is an established hepatocyte-derived serum glycoprotein involved in endocytosis, acute-phase biology, and regulation of mineralization and insulin-receptor signaling. Its liver and hepatocyte enrichment and lack of target-tissue IHC detection make it useful for identifying the module as a circulating-protein signal.
- **Conclusion**: Established evidence supports AHSG as a plasma glycoprotein that reinforces the module’s sample-composition interpretation. Its precise contribution to the shared cervix_uterine–myometrium co-abundance pattern is not established by the available data.

## Module 5

**Tissue pair**: cervix_uterine and myometrium  
**Genes (7)**: AP2B1, C3, COPB1, FGA, GANAB, ITIH1, ITIH2

### Function

No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The most coherent interpretation comes from the gene identities, supplementary STRING evidence, and hu.MAP complexes. The module contains an extracellular plasma-protein branch involving complement component C3, fibrinogen alpha chain FGA, and the inter-alpha-trypsin inhibitor heavy chains ITIH1 and ITIH2. This points toward complement-associated inflammation, coagulation or fibrin organization, and extracellular-matrix or hyaluronan stabilization. The STRING terms support serum association and complement/coagulation biology only as supplementary evidence (STRING TISSUES Serum; within-query FDR = 0.0459) (STRING NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization; within-query FDR = 0.0467) (STRING NetworkNeighborAL Mixed, incl. COVID-19, thrombosis and anticoagulation, and Inter-alpha-trypsin inhibitor heavy chain C-terminus; within-query FDR = 0.0467), not as globally corrected enrichment. A second branch contains GANAB, AP2B1, and COPB1, which are intracellular protein-folding, vesicle-trafficking, and Golgi or endoplasmic-reticulum transport proteins. Thus, the module may combine a dominant circulating-protein signal with a smaller intracellular processing or trafficking signal rather than representing one sharply defined canonical pathway.

**Cell composition.** The module is strongly compatible with a circulating-protein or sample-content signal. Most of its genes encode secreted proteins, and HPA assigns liver enrichment to several genes, with hepatocyte enrichment recurring across the module. C3, FGA, ITIH1, and ITIH2 are not detected in cervix or myometrium by the reported immunohistochemistry evidence, while the intracellular trafficking genes are detected in the tissues. This pattern makes blood or extracellular-fluid carryover, vascular content, or shared stromal and extracellular material plausible explanations for the conserved co-abundance. The HPA evidence does not support a broad immune-cell module: most genes have low immune-cell specificity or are not detected in immune cells, with only limited enrichment for a non-classical monocyte population. The module should therefore not be interpreted as tissue-resident uterine biology without orthogonal validation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides two high-confidence pairwise relationships within the module: FGA with ITIH2 and ITIH1 with ITIH2. ITIH2 is consequently the principal connector of the experimentally or computationally supported extracellular branch, while C3 is linked to FGA in the co-abundance network but has no reported STRING partner within the module. The supplementary STRING neighborhoods connect C3, ITIH1, ITIH2, and FGA to serum, complement, coagulation, opsonization, thrombosis, and inter-alpha-trypsin-inhibitor biology (STRING TISSUES Serum; within-query FDR = 0.0459) (STRING NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization; within-query FDR = 0.0467) (STRING NetworkNeighborAL Mixed, incl. COVID-19, thrombosis and anticoagulation, and Inter-alpha-trypsin inhibitor heavy chain C-terminus; within-query FDR = 0.0467). hu.MAP repeatedly places C3, FGA, ITIH1, and ITIH2 together in broad plasma-protein complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1), with additional complexes linking the C3–FGA pair or the ITIH1–ITIH2 pair (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07541.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_09434.1). These repeated complexes show that the extracellular branch is consistent with known protein-community organization, but they do not establish that all module proteins form one physical complex. GANAB, AP2B1, and COPB1 have no reported STRING or hu.MAP support in this module, so their co-abundance relationship is more plausibly regulatory, cellular-compositional, or technical than a demonstrated physical interaction.

**STRING interactions (score >= 0.7)**: 2 of 21 gene pairs: FGA–ITIH2 (0.811); ITIH1–ITIH2 (0.835)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Serum (FDR = 0.0459, 3 genes); NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization (FDR = 0.0467, 4 genes); NetworkNeighborAL Mixed, incl. COVID-19, thrombosis and anticoagulation, and Inter-alpha-trypsin inhibitor heavy chain C-terminus (FDR = 0.0467, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08395.1 (C3, FGA, ITIH2, ITIH1; 4/43); huMAP3_09531.1 (C3, FGA, ITIH2, ITIH1; 4/47); huMAP3_10101.1 (C3, FGA, ITIH2, ITIH1; 4/49); huMAP3_15040.1 (C3, FGA, ITIH2, ITIH1; 4/64); huMAP3_10678.1 (C3, FGA, ITIH2, ITIH1; 4/71); huMAP3_02242.1 (C3, FGA; 2/9); huMAP3_07432.1 (C3, FGA; 2/18); huMAP3_07541.1 (ITIH2, ITIH1; 2/19); huMAP3_08224.1 (C3, FGA; 2/21); huMAP3_07701.1 (ITIH2, ITIH1; 2/22); huMAP3_09273.1 (ITIH2, ITIH1; 2/28); huMAP3_09434.1 (C3, FGA; 2/33)

### Novelty

The exact conserved co-abundance module may be a new observation, but the underlying biology is not new. Complement C3, fibrinogen FGA, and the inter-alpha-trypsin inhibitor proteins have established roles in circulating inflammation, coagulation, extracellular-matrix organization, and hyaluronan biology, and their joint appearance is supported by existing STRING neighborhoods and repeated hu.MAP plasma-protein complexes. The lack of a complete match in STRING or hu.MAP would not prove novelty, especially because those resources describe physical interactions or curated complexes rather than tissue-pair co-abundance modules. The most defensible novelty claim is therefore that this particular cross-tissue co-abundance pattern, including its association with cervix and myometrium samples and its intracellular branch, requires validation as a dataset-specific observation. It should not be presented as a newly discovered molecular pathway.

**Hypothesis.** Hypothesis: the conserved module reflects a shared extracellular-fluid or vascular-content program in cervix and myometrium, dominated by liver-derived plasma proteins. In this model, C3 contributes complement and inflammatory signaling, FGA contributes clotting and provisional matrix formation, and ITIH1 together with ITIH2 contributes stabilization of hyaluronan-rich extracellular structures and modulation of proteolysis. The GANAB, AP2B1, and COPB1 branch may reflect intracellular handling, secretion, or vesicle trafficking in cells contributing to the samples, but this connection is not established by the supplied interaction databases. A practical test would be to compare the module with plasma or vascular markers, cell-type deconvolution, and independent tissue-level protein measurements before assigning it a uterus-specific mechanism.

### Important genes

#### ITIH2

- **Related proteins** (co-abundance neighbors): ITIH1 (0.85), GANAB (0.83), C3 (0.81); STRING partners: FGA (0.811), ITIH1 (0.835)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07541.1, huMAP3_07701.1, huMAP3_09273.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 2. The inter-alpha-trypsin inhibitors (ITI) are a family of structurally related plasma serine protease inhibitors involved in extracellular matrix stabilization and in prevention of tumor metastasis. The ITI family contains multiple proteins made up of a light chain (see MIM 176870) and a variable number of heavy chains (Salier et al., 1987 [PubMed 2446322]; Himmelfarb et al., 2004 [PubMed 14744536]…
- **Diseases (Open Targets)**: acute tonsillitis (0.357); neurodegenerative disease (0.332); type 2 diabetes mellitus (0.231); non-alcoholic fatty liver (0.231); adverse effect (0.213)
- **Europe PMC papers**: 1020
- **Why important**: ITIH2 has the strongest network connectivity in the module and links ITIH1, GANAB, and C3 in the co-abundance graph. It is secreted to blood, enriched in liver and hepatocytes, and repeatedly appears in STRING-supported terms (STRING TISSUES Serum; within-query FDR = 0.0459) (STRING NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization; within-query FDR = 0.0467) (STRING NetworkNeighborAL Mixed, incl. COVID-19, thrombosis and anticoagulation, and Inter-alpha-trypsin inhibitor heavy chain C-terminus; within-query FDR = 0.0467) and hu.MAP complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) and (hu.MAP huMAP3_07541.1), (hu.MAP huMAP3_07701.1), (hu.MAP huMAP3_09273.1). Its annotation connects the inter-alpha-trypsin inhibitor family with extracellular-matrix stabilization, protease inhibition, and hyaluronan metabolism. It therefore provides the clearest bridge between the circulating-protein interpretation and the smaller intracellular branch.
- **Conclusion**: Established evidence supports ITIH2 as a liver-derived secreted extracellular-matrix and hyaluronan-associated protein that is central to this module’s network structure. It is plausible, but not established, that ITIH2 mediates the association between the plasma-protein branch and intracellular protein-processing signals.

#### C3

- **Related proteins** (co-abundance neighbors): FGA (0.88), ITIH2 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_02242.1, huMAP3_07432.1, huMAP3_08224.1, huMAP3_09434.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a central complement component with extensive disease and literature support, is secreted to blood, and is enriched in liver. It participates in the module’s co-abundance links with FGA and ITIH2 and recurs across many hu.MAP plasma-protein complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_02242.1), (hu.MAP huMAP3_07432.1), (hu.MAP huMAP3_08224.1), and (hu.MAP huMAP3_09434.1). Supplementary STRING evidence associates it with serum, complement, coagulation, and opsonization (STRING TISSUES Serum; within-query FDR = 0.0459), (STRING NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization; within-query FDR = 0.0467). Its immune-cell specificity is limited overall, although a non-classical monocyte enrichment is reported.
- **Conclusion**: Established evidence supports C3 as a biologically important marker of circulating complement and inflammatory potential. In this module, C3 is more safely interpreted as evidence for extracellular or vascular content than as proof of active complement production by cervix or myometrium.

#### FGA

- **Related proteins** (co-abundance neighbors): C3 (0.88); STRING partners: ITIH2 (0.811)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_02242.1, huMAP3_07432.1, huMAP3_08224.1, huMAP3_09434.1
- **Function (MyGene.info)**: fibrinogen alpha chain. This gene encodes the alpha subunit of the coagulation factor fibrinogen, which is a component of the blood clot. Following vascular injury, the encoded preproprotein is proteolytically processed by thrombin during the conversion of fibrinogen to fibrin. Mutations in this gene lead to several disorders, including dysfibrinogenemia, hypofibrinogenemia, afibrinogenemia and renal amyloidosis. Alterna…
- **Diseases (Open Targets)**: familial dysfibrinogenemia (0.789); familial visceral amyloidosis (0.765); congenital afibrinogenemia (0.757); familial hypodysfibrinogenemia (0.659); congenital fibrinogen deficiency (0.619)
- **Europe PMC papers**: 7516
- **Why important**: FGA encodes the fibrinogen alpha chain and is a secreted liver-enriched plasma protein involved in clot formation, platelet activation, cell–matrix adhesion, fibrinolysis, and plasminogen activation. It connects to C3 in the co-abundance graph, to ITIH2 in STRING, and repeatedly occurs with C3 in hu.MAP complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_07432.1), (hu.MAP huMAP3_08224.1), and (hu.MAP huMAP3_09434.1). Its extensive disease and literature record makes it a strong biological anchor for interpreting the module’s coagulation and provisional-matrix component.
- **Conclusion**: Established evidence supports FGA as a circulating coagulation and extracellular-matrix marker. The module does not establish local fibrinogen synthesis or active clot formation in either uterine tissue; those would remain hypotheses requiring tissue-specific validation.

#### ITIH1

- **Related proteins** (co-abundance neighbors): ITIH2 (0.85); STRING partners: ITIH2 (0.835)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07541.1, huMAP3_07701.1, huMAP3_09273.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 1. This gene encodes a member of the inter-alpha-trypsin inhibitor family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the heavy chain of the inter-alpha-trypsin inhibitor complex, which is secreted by hepatocytes into the blood. The heavy chain also interacts with hyaluronan, and…
- **Diseases (Open Targets)**: osteoarthritis, hip (0.305); osteoarthritis (0.188); schizophrenia (0.185); major depressive disorder (0.183); psychiatric disorder (0.171)
- **Europe PMC papers**: 963
- **Why important**: ITIH1 is a liver- and hepatocyte-enriched secreted protein with a direct STRING relationship to ITIH2 and repeated co-occurrence with ITIH2 in hu.MAP complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) and (hu.MAP huMAP3_07541.1), (hu.MAP huMAP3_07701.1), (hu.MAP huMAP3_09273.1). Its known association with hyaluronan and the inter-alpha-trypsin inhibitor family gives it a complementary role to ITIH2 in extracellular-matrix organization. Its literature base is substantial enough to support interpretation without relying only on the network.
- **Conclusion**: Established evidence supports ITIH1 as part of a circulating inter-alpha-trypsin inhibitor system involved in hyaluronan-associated extracellular organization. Its co-abundance with ITIH2 is biologically coherent, but the data do not demonstrate that this pair is produced locally by cervix or myometrium.

#### GANAB

- **Related proteins** (co-abundance neighbors): ITIH2 (0.83), AP2B1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glucosidase II alpha subunit. This gene encodes the alpha subunit of glucosidase II and a member of the glycosyl hydrolase 31 family of proteins. The heterodimeric enzyme glucosidase II plays a role in protein folding and quality control by cleaving glucose residues from immature glycoproteins in the endoplasmic reticulum. Expression of the encoded protein is elevated in lung tumor tissue and in response to UV irradiation. Mut…
- **Diseases (Open Targets)**: polycystic kidney disease 3 with or without polycystic liver disease (0.792); autosomal dominant polycystic liver disease (0.515); autosomal dominant polycystic kidney disease (0.470); Biliary tract abnormality (0.438); COVID-19 (0.370)
- **Europe PMC papers**: 1240
- **Why important**: GANAB occupies a connecting position between ITIH2 and AP2B1 in the module graph and is one of the tissue-detected intracellular genes. It encodes the alpha subunit of glucosidase II, which participates in endoplasmic-reticulum glycoprotein folding and quality control. Unlike the plasma-protein branch, GANAB has no reported STRING or hu.MAP support in this module, making it important as a contrasting signal that may represent intracellular handling or cellular composition rather than a shared extracellular complex.
- **Conclusion**: Established evidence supports GANAB as an intracellular glycoprotein-processing factor with tissue detection in both reported uterine tissue types. Its connection to the secreted-protein branch is a hypothesis based on co-abundance and network placement, not a demonstrated molecular interaction.

## Module 6

**Tissue pair**: cervix_uterine and myometrium  
**Genes (9)**: ARPC5, CLIC1, EFHD2, IMPA1, LYPLA1, NUDT5, PITPNA, PSMA1, PSMA4

### Function

This is a small, heterogeneous intracellular co-abundance module rather than a functionally coherent pathway established by enrichment. No GO/KEGG term passed global correction, and STRING supplied no functional enrichment, so no pathway-level function can be claimed from enrichment. The most plausible biological themes suggested by the individual annotations and network are proteasome-associated protein turnover, membrane-lipid and inositol signaling, actin remodeling, redox or stress handling, and intracellular trafficking. The strongest direct structural evidence is the proteasome alpha-subunit relationship between PSMA1 and PSMA4, supported by the shared hu.MAP complexes (hu.MAP huMAP3_00356.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1). The remaining co-abundance links may reflect coordinated cellular state, shared cell composition, or indirect regulation rather than physical interactions.

**Cell composition.** All module proteins are non-secreted and have low tissue specificity in HPA, arguing against a plasma-protein or secreted-protein module. Most genes have cell-type-enhanced expression, with recurring HPA signals in neutrophils, trophoblast populations, megakaryocytes, platelets, and esophageal apical cells. Blood-cell specificity is generally low, with only EFHD2 showing immune-cell enhancement for neutrophils. The module is therefore not a clean tissue-specific smooth-muscle or cervical program. It may partly reflect shared cell populations, including immune, vascular-associated, trophoblast-like, or other contaminating cell states, although the available HPA evidence does not establish which explanation is correct. Protein detection also differs between the tissues: several proteins are detected in cervix but not myometrium, while CLIC1 is detected in both and ARPC5 is detected in myometrium but not cervix. PITPNA and NUDT5 are not detected in either listed tissue, so their co-abundance may reflect abundance below detection, cell-mixture effects, or technical factors.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports one high-confidence relationship within the module, PSMA1–PSMA4. This agrees with their shared membership in the proteasome-related hu.MAP complexes (hu.MAP huMAP3_00356.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1), where they are only a subset of much larger complexes. Thus, the proteasome component is independently supported as a known molecular assembly, but the hu.MAP evidence does not show that all module genes form one complex. EFHD2, LYPLA1, CLIC1, PITPNA, NUDT5, ARPC5, and IMPA1 have no listed STRING partners or hu.MAP complexes within the supplied evidence. The other co-abundance edges should therefore be interpreted as statistical relationships in the tissue data, not as established direct protein interactions.

**STRING interactions (score >= 0.7)**: 1 of 36 gene pairs: PSMA1–PSMA4 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00356.1 (PSMA1, PSMA4; 2/33); huMAP3_09656.1 (PSMA1, PSMA4; 2/64); huMAP3_13725.1 (PSMA1, PSMA4; 2/69)

### Novelty

The module cannot be called a new molecular complex or a newly discovered pathway. Its PSMA1–PSMA4 relationship and proteasome membership are already known, and the pair is represented in STRING and hu.MAP. The broader co-abundance arrangement may be novel as a tissue-pair observation because most of its cross-functional links are not represented in the supplied interaction resources, but absence from STRING or hu.MAP alone does not prove novelty. The lack of globally corrected GO/KEGG enrichment also prevents a claim that this is a newly defined biological pathway. A defensible conclusion is that this may be a novel tissue-level co-abundance pattern built around a known proteasome relationship, requiring replication and targeted validation.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular stress or remodeling state present across cervix and myometrium samples. In this model, PSMA1 and PSMA4 mark proteasome activity, EFHD2 links the module to membrane-associated calcium or adhesion-related organization, LYPLA1 and PITPNA connect lipid handling to membrane signaling, CLIC1 and IMPA1 connect ion, inositol, and signal-transduction processes, and ARPC5 represents actin-network remodeling. NUDT5 could contribute to nucleotide or oxidative-damage handling. A second, nonexclusive hypothesis is that the pattern is driven partly by shared infiltrating or admixed cell populations, especially neutrophil- or platelet-associated cells. These hypotheses are not established by enrichment because no GO/KEGG term achieved global significance and should be tested with cell-resolved data, independent cohorts, and protein-level or perturbation experiments.

### Important genes

#### EFHD2

- **Related proteins** (co-abundance neighbors): PITPNA (0.86), LYPLA1 (0.85), CLIC1 (0.82), PSMA1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EF-hand domain family member D2. Enables cadherin binding activity. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: alcoholic pancreatitis (0.133); cancer (0.099); neoplasm (0.085); melanoma (0.079); lung cancer (0.078)
- **Europe PMC papers**: 542
- **Why important**: EFHD2 is the principal network bridge, connecting PITPNA, LYPLA1, CLIC1, and PSMA1. Its annotation supports cadherin binding and actin crosslink formation, while HPA links it to neutrophils and several specialized cell types. It is detected in cervix but not myometrium, making it potentially informative for tissue or cell-composition differences. Its literature volume is moderate relative to the better studied module members.
- **Conclusion**: Established evidence supports EFHD2 as a central co-abundance connector with cytoskeletal or adhesion-related annotation and neutrophil-associated HPA expression. It is plausible, but not proven, that EFHD2 coordinates the lipid, membrane, and proteasome-associated signals in this module. Its role as a driver of the shared tissue program remains a hypothesis.

#### PSMA1

- **Related proteins** (co-abundance neighbors): PSMA4 (0.83), EFHD2 (0.80); STRING partners: PSMA4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: huMAP3_00356.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 20S subunit alpha 1. The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent proc…
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.535); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1417
- **Why important**: PSMA1 participates in the only high-confidence STRING interaction in the module, with PSMA4, and is present with PSMA4 in all listed hu.MAP complexes (hu.MAP huMAP3_00356.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1). Its proteasome annotation connects the module to ubiquitin-dependent protein catabolism, DNA damage responses, apoptosis, and immune-system processes. It also has substantial literature and disease-association support.
- **Conclusion**: Established evidence identifies PSMA1 as a proteasome core subunit and validates its relationship with PSMA4. It is the strongest anchor for a protein-turnover interpretation. It does not establish that proteasome activity explains the entire module or that PSMA1 drives the tissue co-abundance pattern.

#### PSMA4

- **Related proteins** (co-abundance neighbors): NUDT5 (0.86), PSMA1 (0.83); STRING partners: PSMA1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_00356.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 20S subunit alpha 4. This gene encodes a core alpha subunit of the 20S proteosome, which is a highly ordered ring-shaped structure composed of four rings of 28 non-identical subunits. Proteasomes cleave peptides in an ATP- and ubiquitin-dependent manner. [provided by RefSeq, Aug 2016].
- **Diseases (Open Targets)**: plasma cell myeloma (0.616); mantle cell lymphoma (0.542); neoplasm (0.513); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1240
- **Why important**: PSMA4 is the partner of PSMA1 in the only listed high-confidence STRING interaction and occurs with PSMA1 in the three hu.MAP proteasome-related complexes (hu.MAP huMAP3_00356.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1). Its annotations include proteasomal protein catabolism, DNA repair, apoptosis, DNA-damage response, and oxidative-stress response. It has substantial literature and disease-association support.
- **Conclusion**: Established evidence supports PSMA4 as a proteasome core component and confirms a known molecular relationship with PSMA1. Its presence gives the module a credible protein-quality-control or stress-response anchor. Any proposed connection from PSMA4 to the other module genes is presently a co-abundance hypothesis rather than a demonstrated interaction.

#### CLIC1

- **Related proteins** (co-abundance neighbors): EFHD2 (0.82), IMPA1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CLIC family member 1. Chloride channels are a diverse group of proteins that regulate fundamental cellular processes including stabilization of cell membrane potential, transepithelial transport, maintenance of intracellular pH, and regulation of cell volume. Chloride intracellular channel 1  is a member of the p64 family; the protein localizes principally to the cell nucleus and exhibits both nuclear and plasma membra…
- **Diseases (Open Targets)**: spermatogenic failure 74 (0.333); neoplasm (0.115); glioblastoma (0.114); gastric cancer (0.102); central nervous system cancer (0.099)
- **Europe PMC papers**: 4339
- **Why important**: CLIC1 links EFHD2 to IMPA1 in the co-abundance graph and is detected in both listed tissues, unlike several other module proteins. Its annotation covers intracellular chloride-channel activity, signal transduction, oxidant detoxification, and platelet aggregation. It has the largest literature volume among the module genes and shows HPA enhancement in megakaryocytes and platelets as well as other cell types.
- **Conclusion**: Established evidence supports CLIC1 as a broadly studied intracellular channel or redox-associated protein with cytoskeletal and signaling relevance. Its bilateral tissue detection makes it a plausible shared-state marker. The proposed role as a bridge between ion or redox handling and inositol signaling in this module remains unproven.

#### LYPLA1

- **Related proteins** (co-abundance neighbors): EFHD2 (0.85), ARPC5 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lysophospholipase 1. This gene encodes a member of the alpha/beta hydrolase superfamily. The encoded protein functions as a homodimer, exhibiting both depalmitoylating as well as lysophospholipase activity, and may be involved in Ras localization and signaling. Alternate splicing results in multiple transcript variants. Pseudogenes of this gene have been defined on chromosomes 4, 6, and 7. [provided by RefSeq, Jul 201…
- **Diseases (Open Targets)**: ovarian neoplasm (0.205); obesity disorder (0.190); phlebitis (0.190); Thrombophlebitis (0.190); melanoma (0.093)
- **Europe PMC papers**: 1123
- **Why important**: LYPLA1 connects EFHD2 to ARPC5 and provides a biochemical link between lipid modification and cytoskeletal organization. It encodes a lysophospholipase and depalmitoylating enzyme with reported roles in Ras localization and signaling, protein depalmitoylation, fatty-acid transport, and membrane trafficking. It has substantial literature and is detected in cervix but not myometrium.
- **Conclusion**: Established evidence supports LYPLA1 as a lipid-processing and protein-depalmitoylation enzyme that could influence membrane signaling. Its network placement makes it a useful candidate for explaining the connection between EFHD2 and ARPC5. A direct mechanistic role in the shared cervix–myometrium module is a hypothesis requiring biochemical and tissue-resolved validation.

## Module 7

**Tissue pair**: cervix_uterine and myometrium  
**Genes (9)**: ATP5F1B, CS, CLTC, NME1, NNT, DDOST, PRDX4, XPO1, CSE1L

### Function

The module does not have any GO or KEGG term passing global correction, so no pathway-level enrichment can be claimed from those analyses. Its structure nevertheless suggests a composite cellular-maintenance program rather than a single specialized pathway. NNT, ATP5F1B, and CS connect mitochondrial redox capacity, oxidative metabolism, and energy production, while PRDX4 is consistent with peroxide control and endoplasmic-reticulum redox handling. CLTC and NME1 connect intracellular trafficking and nucleotide-related cellular processes, and XPO1 with CSE1L form a nuclear transport pair. NME1 is the principal network connector, linking the mitochondrial/metabolic side with CLTC, PRDX4, and the XPO1–CSE1L transport side. The most defensible interpretation is coordinated mitochondrial metabolism, redox protection, intracellular trafficking, and nucleocytoplasmic transport, rather than a validated single biological pathway. The absence of globally significant GO or KEGG enrichment does not invalidate the co-abundance module.

**Cell composition.** This is not a plasma-protein or blood-cell module. HPA assigns low immune-cell specificity to every member, identifies no enriched blood-cell population, and identifies only one module gene as secreted. Most members have low tissue specificity, indicating a substantial broadly expressed cellular component. The tissue-enhanced signal is most often associated with skeletal muscle and tongue, with an additional pancreas-associated signal, while cell-type enhancement is frequent and includes several distinct epithelial, trophoblast, germ-cell, hepatic, and muscle-related populations. Thus the module is unlikely to represent a uniform blood contamination signal. It may instead reflect shared cellular physiology, particularly mitochondrial and redox demands, across cervix and myometrium. Protein detection is complete in cervix and partial in myometrium, so the shared transcript or protein-abundance relationship should not be interpreted as uniform protein presence in every myometrial sample.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports two high-confidence pairwise relationships within the module: ATP5F1B with CS and XPO1 with CSE1L. These relationships independently support a mitochondrial energy or citrate-metabolism connection and a nuclear transport connection. STRING reports no functional enrichment for the module, so the pairwise evidence should not be generalized into a globally established pathway. hu.MAP places XPO1 and CSE1L together as the only module-member pair in each of the listed complexes (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_09592.1). Because those complexes contain many additional proteins and only this pair is represented from the module, the hu.MAP result supports a recurring association of the nuclear-export machinery with broad cellular complexes, but does not establish that all module genes form one physical complex. NME1, CLTC, NNT, CS, DDOST, and PRDX4 have no reported STRING partner or hu.MAP complex membership within the supplied evidence. Overall, known interactions explain local parts of the network, whereas the complete co-abundance structure is broader than the currently catalogued physical interactions.

**STRING interactions (score >= 0.7)**: 2 of 36 gene pairs: ATP5F1B–CS (0.917); CSE1L–XPO1 (0.976)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07170.1 (XPO1, CSE1L; 2/14); huMAP3_09042.1 (XPO1, CSE1L; 2/26); huMAP3_06791.1 (XPO1, CSE1L; 2/31); huMAP3_09592.1 (XPO1, CSE1L; 2/95)

### Novelty

The module may be a new cross-tissue co-abundance observation, but the supplied evidence is insufficient to call it a newly discovered molecular complex or pathway. Its novelty is supported by the limited overlap between the module and curated interaction resources: known STRING relationships account for only local edges, and hu.MAP repeatedly captures only the XPO1–CSE1L pair. The absence of STRING or hu.MAP representation for the remaining co-abundance relationships does not prove novelty, because co-abundance can arise from shared regulation, cell composition, organelle abundance, or indirect physiology rather than direct binding. A strong novelty claim would require comparison with published co-expression modules, independent cervix and myometrium cohorts, cell-composition estimates, and replication across platforms. The most cautious conclusion is that this is a potentially novel cross-tissue abundance pattern composed of several established cellular subsystems, not evidence for a previously unknown protein complex.

**Hypothesis.** Hypothesis: the shared module reflects a coordinated cellular state in which mitochondrial oxidative metabolism and NADPH-generating capacity support redox control and biosynthetic demands, while nuclear transport and endocytic trafficking maintain protein and signaling homeostasis. In this model, NNT, ATP5F1B, and CS represent the metabolic engine; PRDX4 buffers peroxide and endoplasmic-reticulum redox stress; CLTC supports trafficking; and XPO1 with CSE1L regulates nucleocytoplasmic transport. NME1 may couple these processes through its central co-abundance position and its links to both redox or stress-associated and transport-associated genes. This is a mechanistic proposal derived from network structure and known gene functions, not a demonstrated causal pathway. It should be tested by perturbing mitochondrial redox balance, nuclear export, or endocytic trafficking and measuring whether the other module members respond coherently in relevant cervical and myometrial cell types.

### Important genes

#### NME1

- **Related proteins** (co-abundance neighbors): CLTC (0.92), CS (0.83), PRDX4 (0.82), XPO1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NME/NM23 nucleoside diphosphate kinase 1. This gene (NME1) was identified because of its reduced mRNA transcript levels in highly metastatic cells. Nucleoside diphosphate kinase (NDK) exists as a hexamer composed of 'A' (encoded by this gene) and 'B' (encoded by NME2) isoforms. Mutations in this gene have been identified in aggressive neuroblastomas. Two transcript variants encoding different isoforms have been found for this gene. Co-tra…
- **Diseases (Open Targets)**: placenta praevia (0.211); Dermatochalasis (0.136); neoplasm (0.117); smoking initiation (0.113); melanoma (0.112)
- **Europe PMC papers**: 3306
- **Why important**: NME1 has the strongest network connectivity in the module and links CLTC, CS, PRDX4, and XPO1, making it the main bridge between trafficking, mitochondrial metabolism, redox handling, and nuclear transport. Its established function includes nucleoside diphosphate kinase activity and roles related to nucleotide biosynthesis, DNA processing, and apoptosis. It has extensive literature coverage and disease associations including aggressive neuroblastoma and neoplasm-related evidence. HPA detects it in cervix but not myometrium, which makes its cross-tissue co-abundance relationship especially informative but also demands replication.
- **Conclusion**: Established: NME1 is the module's central network connector and has broad nucleotide and cellular-stress relevance. Hypothesis: NME1 may coordinate the metabolic and transport components of the module. The data do not establish that NME1 drives the module or causes the shared tissue pattern.

#### NNT

- **Related proteins** (co-abundance neighbors): ATP5F1B (0.87), CLTC (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nicotinamide nucleotide transhydrogenase. This gene encodes an integral protein of the inner mitochondrial membrane. The enzyme couples hydride transfer between NAD(H) and NADP(+) to proton translocation across the inner mitochondrial membrane. Under most physiological conditions, the enzyme uses energy from the mitochondrial proton gradient to produce high concentrations of NADPH. The resulting NADPH is used for biosynthesis and in free …
- **Diseases (Open Targets)**: familial glucocorticoid deficiency (0.638); neurodegenerative disease (0.497); hereditary disease (0.453); atypical hemolytic-uremic syndrome with DGKE deficiency (0.416); Abnormality of the skeletal system (0.396)
- **Europe PMC papers**: 6111
- **Why important**: NNT connects to ATP5F1B and CLTC and encodes a mitochondrial inner-membrane enzyme that generates NADPH using the proton gradient. Its described functions include NADPH regeneration, reactive-oxygen-species metabolism, and support of biosynthesis and antioxidant defense. HPA shows tissue enhancement in skeletal muscle and tongue, cell-type enhancement in metabolically active cell populations, and protein detection in both tissues. Its disease associations include familial glucocorticoid deficiency and other hereditary or metabolic contexts.
- **Conclusion**: Established: NNT is a plausible marker of mitochondrial redox and biosynthetic capacity within this module. Hypothesis: NNT may help explain why the module is shared by tissues with substantial energetic or contractile demands. The module does not demonstrate that NNT controls redox state in cervix or myometrium.

#### ATP5F1B

- **Related proteins** (co-abundance neighbors): NNT (0.87), CLTC (0.82); STRING partners: CS (0.917)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP synthase F1 subunit beta. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: hypermetabolism due to uncoupled mitochondrial oxidative phosphorylation 2 (0.499); hypertrophic cardiomyopathy (0.212); Alzheimer disease (0.177); hypertensive disorder (0.117); response to xenobiotic stimulus (0.117)
- **Europe PMC papers**: 735
- **Why important**: ATP5F1B is connected to NNT and CLTC and has a high-confidence STRING relationship with CS, providing the clearest bridge to mitochondrial energy metabolism in the network. It encodes the catalytic beta subunit of mitochondrial ATP synthase and is associated with ATP production and proton-motive-force utilization. HPA shows tissue enhancement in skeletal muscle and tongue, detection in both tissues, and cell-type enhancement in several epithelial and trophoblast populations. Its disease associations include disorders involving uncoupled oxidative phosphorylation and cardiomyopathy-related evidence.
- **Conclusion**: Established: ATP5F1B and CS form a supported mitochondrial metabolic pair, and ATP5F1B is a core oxidative-phosphorylation component. Hypothesis: this pair represents a shared energetic-demand signal in the two uterine tissue groups. The evidence does not show that the module is specifically an ATP-synthesis module because global enrichment was not significant.

#### CS

- **Related proteins** (co-abundance neighbors): DDOST (0.84), NME1 (0.83); STRING partners: ATP5F1B (0.917)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS is connected to NME1 and DDOST and has a high-confidence STRING relationship with ATP5F1B. It encodes citrate synthase, a mitochondrial tricarboxylic-acid-cycle enzyme and a widely used indicator of oxidative metabolic capacity. HPA shows tissue enhancement in skeletal muscle and tongue, low cell-type specificity, and detection in both tissues. CS also has extensive literature coverage and disease associations spanning neurological and autoimmune contexts.
- **Conclusion**: Established: CS anchors the module's mitochondrial oxidative-metabolism interpretation and is supported by an interaction with ATP5F1B. Hypothesis: CS may report mitochondrial abundance or metabolic state that is co-regulated with redox and transport machinery. The data do not distinguish increased mitochondrial content from increased pathway activity.

#### XPO1

- **Related proteins** (co-abundance neighbors): NME1 (0.81), CSE1L (0.81); STRING partners: CSE1L (0.976)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: huMAP3_07170.1, huMAP3_09042.1, huMAP3_06791.1, huMAP3_09592.1
- **Function (MyGene.info)**: exportin 1. This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSe…
- **Diseases (Open Targets)**: plasma cell myeloma (0.642); B-cell chronic lymphocytic leukemia (0.626); diffuse large B-cell lymphoma (0.602); HIV infectious disease (0.561); neurodegenerative disease (0.522)
- **Europe PMC papers**: 5357
- **Why important**: XPO1 is connected to NME1 and CSE1L, has a high-confidence STRING relationship with CSE1L, and is present with CSE1L in every listed hu.MAP complex (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_09592.1). It encodes exportin one, a major mediator of nuclear export for RNA and nuclear proteins and a regulator of the localization of several signaling and cell-cycle factors. HPA detects it in both tissues and reports low tissue and cell-type specificity, consistent with a broadly required cellular process. Its disease associations include plasma-cell myeloma, chronic lymphocytic leukemia, diffuse large B-cell lymphoma, HIV-related disease, and neurodegenerative disease.
- **Conclusion**: Established: XPO1 with CSE1L is the best-supported transport submodule and the most consistently represented module pair in hu.MAP. Hypothesis: nuclear export capacity may be co-regulated with mitochondrial and redox capacity in the shared tissue state. The data do not establish a causal link between XPO1 transport and the metabolic genes.

#### PRDX4

- **Related proteins** (co-abundance neighbors): NME1 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peroxiredoxin 4. The protein encoded by this gene is an antioxidant enzyme and belongs to the peroxiredoxin family. The protein is localized to the cytoplasm. Peroxidases of the peroxiredoxin family reduce hydrogen peroxide and alkyl hydroperoxides to water and alcohol with the use of reducing equivalents derived from thiol-containing donor molecules. This protein has been found to play a regulatory role in the ac…
- **Diseases (Open Targets)**: Neurodevelopmental delay (0.118); neoplasm (0.113); cancer (0.097); lung adenocarcinoma (0.096); gastric cancer (0.095)
- **Europe PMC papers**: 1836
- **Why important**: PRDX4 is directly connected to NME1 and is the module member most specifically associated with peroxide detoxification and redox homeostasis in the supplied gene annotations. It encodes an antioxidant peroxiredoxin localized to the endoplasmic reticulum and is described as participating in hydrogen-peroxide reduction, cellular oxidant detoxification, and NF-kappaB regulation. HPA shows tissue enrichment in pancreas, cell-type enhancement in secretory, hepatic, germ-cell, and trophoblast populations, and detection in both tissues. Its disease associations include neurodevelopmental delay and several neoplasm-related contexts.
- **Conclusion**: Established: PRDX4 provides a biologically coherent redox and endoplasmic-reticulum component and is linked to NME1 in the module. Hypothesis: PRDX4 may buffer oxidative or protein-folding stress associated with the mitochondrial state represented by NNT, ATP5F1B, and CS. The module does not show that peroxide stress is the initiating event.

## Module 8

**Tissue pair**: cervix_uterine and myometrium  
**Genes (8)**: ATP5MK, BOLA2, COXFA4, ELOC, S100A10, S100A11, S100A16, TXN

### Function

The module does not have any GO or KEGG term that passes global correction, so no globally significant pathway-level function can be assigned. Its most coherent biological signal is a calcium-binding and S100-related subnetwork: S100A10, S100A11, and S100A16 are linked by high-confidence STRING relationships and share supplementary S100/calcium-binding domain annotations (STRING SMART S-100/ICaBP type calcium binding domain; within-query FDR = 0.0042), (STRING InterPro S100/Calcium binding protein 7/8-like, conserved site; within-query FDR = 0.0162), (STRING InterPro S100/CaBP-9k-type, calcium binding, subdomain; within-query FDR = 0.0162). The remaining genes connect this signal to intracellular redox homeostasis, transcriptional regulation, mitochondrial energy metabolism, and iron or iron-sulfur cluster biology. TXN is the main network hub and may connect redox regulation with the S100-associated component, while ATP5MK and COXFA4 form a small mitochondrial respiratory component. These annotations support a composite cellular-state module rather than a single established pathway.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only one gene is annotated as secreted, and the genes are generally intracellular or membrane-associated. HPA evidence argues against a blood-cell-driven interpretation: most genes have low immune-cell specificity, one is not detected in immune cells, and only S100A11 is immune-cell enhanced in neutrophils. Instead, the module has a strong epithelial-like tissue and cell-type signature, especially esophageal apical and suprabasal cells, with additional associations to gastric, hepatic, muscle, and neural cell types. This cross-tissue pattern suggests that the shared cervix_uterine and myometrium signal may reflect a conserved epithelial-like or differentiated cellular state, a broadly shared cellular program, or sample-composition effects rather than a uterus-specific process. Protein detection is more evident in cervix_uterine than in myometrium, so the module should not automatically be interpreted as a uniformly abundant smooth-muscle program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a known S100-associated core consisting of S100A10, S100A11, and S100A16: all three pairwise relationships are present at the specified high-confidence threshold. The same three genes receive the supplementary S100/calcium-binding annotations (STRING SMART S-100/ICaBP type calcium binding domain; within-query FDR = 0.0042), (STRING InterPro S100/Calcium binding protein 7/8-like, conserved site; within-query FDR = 0.0162), and (STRING InterPro S100/CaBP-9k-type, calcium binding, subdomain; within-query FDR = 0.0162). hu.MAP provides additional support for a known protein-complex context involving S100A11 and S100A16 in complexes (hu.MAP huMAP3_09125.1) and (hu.MAP huMAP3_09929.1), although each complex contains many proteins and only a small subset is represented in this module. The other module genes have no reported STRING partners or hu.MAP complexes in the fact sheet, so the network is partly composed of known physical or functional relationships and partly of co-abundance links without corresponding database support. Thus, the module is not equivalent to a single experimentally established complex.

**STRING interactions (score >= 0.7)**: 3 of 28 gene pairs: S100A10–S100A11 (0.716); S100A10–S100A16 (0.711); S100A11–S100A16 (0.738)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART S-100/ICaBP type calcium binding domain (FDR = 0.0042, 3 genes); InterPro S100/Calcium binding protein 7/8-like, conserved site (FDR = 0.0162, 3 genes); InterPro S100/CaBP-9k-type, calcium binding, subdomain (FDR = 0.0162, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09125.1 (S100A11, S100A16; 2/53); huMAP3_09929.1 (S100A11, S100A16; 2/75)

### Novelty

The module may be a new tissue-pair co-abundance observation, but the available evidence does not establish a wholly novel molecular mechanism. The S100A10-S100A11-S100A16 relationships and the S100A11-S100A16 complex memberships are already represented in STRING and hu.MAP, indicating that an important part of the module recapitulates known biology. Conversely, the particular combination with TXN, ELOC, ATP5MK, COXFA4, and BOLA2, and its conservation across cervix_uterine and myometrium, is not shown in the fact sheet as a previously defined complex or pathway. Database absence for several links is not proof of novelty. The strongest defensible conclusion is that the tissue-pair module is potentially novel as a co-abundance configuration, while its S100/calcium-associated core is not novel in isolation.

**Hypothesis.** Hypothesis: the module represents a conserved intracellular stress and differentiation state in which an S100/calcium-associated component is coordinated with redox control, transcriptional regulation, mitochondrial respiration, and iron-related homeostasis. TXN could help couple redox status to calcium-sensitive or cytoskeletal and adhesion-related processes associated with S100 proteins, while ATP5MK and COXFA4 could reflect accompanying mitochondrial energy demand. ELOC and BOLA2 may mark broader transcriptional, proteostasis, or iron-homeostasis support. This hypothesis is consistent with the network and annotations, but it is not demonstrated by a globally significant GO or KEGG enrichment result and requires validation by cell-resolved expression, protein measurements, and perturbation experiments in uterine tissues.

### Important genes

#### TXN

- **Related proteins** (co-abundance neighbors): BOLA2; BOLA2B (0.87), ATP5MK (0.82), ELOC (0.82), COXFA4 (0.81), S100A16 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin. The protein encoded by this gene acts as a homodimer and is involved in many redox reactions. The encoded protein is active in the reversible S-nitrosylation of cysteines in certain proteins, which is part of the response to intracellular nitric oxide. This protein is found in the cytoplasm. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct…
- **Diseases (Open Targets)**: neurodegenerative disease (0.530); smoking initiation (0.288); ovarian neoplasm (0.171); cancer (0.122); neoplasm (0.114)
- **Europe PMC papers**: 4080
- **Why important**: TXN is the principal network hub in the module and connects several otherwise weakly connected components, including S100A16, ELOC, BOLA2 or BOLA2B, ATP5MK, and COXFA4. Its annotated roles in redox reactions, cell redox homeostasis, hydrogen-peroxide detoxification, and nitric-oxide-related cysteine regulation make it a plausible integrator of cellular stress and metabolic state. It also has substantial literature support relative to most module genes.
- **Conclusion**: Established evidence supports TXN as a highly connected redox-homeostasis gene with broad cellular functions. It is reasonable to hypothesize that TXN helps organize the module-level stress state, but the co-abundance data do not prove that TXN regulates the S100 genes or drives the module.

#### S100A11

- **Related proteins** (co-abundance neighbors): BOLA2; BOLA2B (0.86), S100A16 (0.85), ELOC (0.80); STRING partners: S100A10 (0.716), S100A16 (0.738)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: S100 calcium binding protein A11. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: skin disorder (0.169); atopic eczema (0.127); skin cancer (0.122); neoplasm (0.115); hepatocellular carcinoma (0.111)
- **Europe PMC papers**: 2722
- **Why important**: S100A11 is part of the directly connected S100 triad with S100A10 and S100A16, appears in both hu.MAP complexes (hu.MAP huMAP3_09125.1) and (hu.MAP huMAP3_09929.1), and has annotations involving calcium binding, cell proliferation, cell-cell adhesion, and smooth-muscle-cell migration. HPA places it in the epithelial-like signature and also reports neutrophil enhancement. Its network position and literature support make it a strong biological marker of the module's calcium-associated component.
- **Conclusion**: Established evidence supports S100A11 as a calcium-binding S100-family protein with adhesion, proliferation, and migration-related annotations and known complex context. Its role as a mediator connecting this module to uterine smooth-muscle behavior remains a hypothesis rather than a demonstrated function here.

#### S100A16

- **Related proteins** (co-abundance neighbors): S100A11 (0.85), TXN (0.81); STRING partners: S100A10 (0.711), S100A11 (0.738)
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: S100 calcium binding protein A16. Enables calcium ion binding activity and protein homodimerization activity. Predicted to act upstream of or within response to calcium ion. Located in several cellular components, including cytosol; extracellular space; and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.490); neoplasm (0.107); lung adenocarcinoma (0.104); breast cancer (0.103); breast carcinoma (0.101)
- **Europe PMC papers**: 2006
- **Why important**: S100A16 is directly connected to S100A11 and TXN, participates with S100A11 in hu.MAP complexes (hu.MAP huMAP3_09125.1) and (hu.MAP huMAP3_09929.1), and contributes to all supplementary S100/calcium-binding signals (STRING SMART S-100/ICaBP type calcium binding domain; within-query FDR = 0.0042), (STRING InterPro S100/Calcium binding protein 7/8-like, conserved site; within-query FDR = 0.0162), and (STRING InterPro S100/CaBP-9k-type, calcium binding, subdomain; within-query FDR = 0.0162). Its annotation supports calcium binding and protein homodimerization, while HPA places it in the same epithelial-like tissue context as other S100 genes.
- **Conclusion**: Established evidence supports S100A16 as a calcium-associated S100-family component with known complex membership. Its position suggests that it may help stabilize the module's calcium-related core, but a specific mechanistic role in cervix_uterine or myometrium is not established by the fact sheet.

#### S100A10

- **Related proteins** (co-abundance neighbors): BOLA2; BOLA2B (0.85), ELOC (0.81); STRING partners: S100A11 (0.716), S100A16 (0.711)
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: S100 calcium binding protein A10. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: actinic keratosis (0.208); neurodegenerative disease (0.184); diverticular disease (0.183); neoplasm (0.115); hepatocellular carcinoma (0.111)
- **Europe PMC papers**: 10215
- **Why important**: S100A10 completes the directly connected S100 triad and is linked in STRING to both S100A11 and S100A16. Its annotations include vesicle budding, exocytosis, membrane-raft assembly, and plasminogen-activation regulation, providing a possible interface between calcium-associated proteins and membrane trafficking or extracellular-interaction processes. It is detected in both tissues by HPA and has extensive literature support.
- **Conclusion**: Established evidence supports S100A10 as a well-studied S100-family-associated regulator of membrane and vesicle-related processes and as a known partner of S100A11 and S100A16. Its possible role in coordinating secretion, adhesion, or tissue remodeling in this shared module is a hypothesis.

#### ELOC

- **Related proteins** (co-abundance neighbors): BOLA2; BOLA2B (0.93), TXN (0.82), S100A10 (0.81), S100A11 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: elongin C. This gene encodes the protein elongin C, which is a subunit of the transcription factor B (SIII) complex. The SIII complex is composed of elongins A/A2, B and C. It activates elongation by RNA polymerase II by suppressing transient pausing of the polymerase at many sites within transcription units. Elongin A functions as the transcriptionally active component of the SIII complex, whereas elongins …
- **Diseases (Open Targets)**: HIV infectious disease (0.588); metabolic disease (0.269); Hypercholesterolemia (0.180); renal cell carcinoma (0.104); neoplasm (0.085)
- **Europe PMC papers**: 817
- **Why important**: ELOC has a prominent network position beneath TXN and connects to S100A10 and S100A11. Its established annotation as a regulatory component of the RNA polymerase II elongation complex and its involvement in ubiquitin-dependent protein catabolism provide a plausible transcriptional and proteostasis context for the module. It has lower literature volume than the S100 genes but may represent a functionally informative bridge.
- **Conclusion**: Established evidence supports ELOC as a transcription-elongation and regulatory-complex component. Its co-abundance with the S100 and redox genes may indicate coordinated transcriptional or proteostatic adaptation, but that relationship is not directly demonstrated.

## Module 9

**Tissue pair**: cervix_uterine and myometrium  
**Genes (7)**: CASP3, CNN3, CYRIB, EIF6, SEC22B, TAGLN2, TPD52L2

### Function

No GO or KEGG term passed global correction, so the module does not support a formally established shared pathway. The co-abundance topology instead suggests a mixed intracellular program involving vesicle trafficking through SEC22B, cytoskeletal and actomyosin organization through TAGLN2 and CNN3, translational and ribosome-related functions through EIF6, regulation of actin and immune-associated signaling through CYRIB, and apoptotic execution through CASP3. These annotations are gene-level evidence rather than enrichment evidence. The module is therefore best interpreted as a potentially mixed cell-state or cellular-composition signal rather than a demonstrated coherent biochemical pathway. The central position of TPD52L2, with links to vesicle, cytoskeletal, and translation-associated genes, may indicate coordination among these processes, but this remains inferential.

**Cell composition.** The genes are not secreted proteins, so the module is not a plasma-protein or circulating-secretome module. Most genes have low tissue specificity in HPA, while every gene is marked as cell-type enhanced. HPA points to heterogeneous cellular associations, including platelets, neutrophils, megakaryocyte-erythroid progenitors, innate lymphoid cells, esophageal epithelial populations, and lymphocyte populations. CYRIB is tissue enhanced in bone marrow, and several genes have blood-cell or immune-cell associations. This pattern raises the possibility that the shared cervix_uterine and myometrium signal reflects variable representation of immune, blood-derived, or other shared cell types rather than a tissue-specific smooth-muscle program. Protein detection is also mixed across the two tissues: TPD52L2 and CNN3 are detected in both, EIF6 is detected in cervix_uterine, CYRIB in myometrium, while CASP3 and TAGLN2 are not detected in either tissue by the reported IHC summary. The lack of uniform tissue detection further argues for caution in assigning the module to a resident tissue mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

None of the possible module gene pairs met the supplied STRING interaction threshold, and no STRING functional-enrichment result was reported. No hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not corroborated as established physical or functional interactions by these resources. The strongest internal structure is centered on TPD52L2, with EIF6 providing a connection toward CYRIB and CYRIB connecting to CASP3; TPD52L2 also links to TAGLN2, SEC22B, and CNN3. This topology may reflect coordinated expression or shared cellular origin, but it should not be treated as a validated protein-interaction network.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared co-abundance pattern may be a new observation for the cervix_uterine and myometrium tissue pair, because it is not represented as a multi-member STRING interaction set or a hu.MAP complex. However, that absence does not establish biological novelty: co-expression can arise from cell composition, generic intracellular programs, technical effects, or context-specific regulation that is not captured by interaction databases. The lack of globally significant GO or KEGG enrichment also prevents claiming discovery of a new pathway. The defensible conclusion is that the tissue-pair co-abundance association is potentially novel as a dataset-level observation, while its mechanism and disease relevance remain unestablished.

**Hypothesis.** Hypothesis: the module reflects a shared, heterogeneous cellular state present in both tissues, combining vesicle and membrane-trafficking activity, cytoskeletal remodeling, translational support, and stress or apoptotic signaling. TPD52L2 may act as the expression-level hub linking SEC22B, TAGLN2, CNN3, and EIF6-associated processes, while CYRIB and CASP3 may capture an immune or stress-related component. An alternative hypothesis is that the apparent module is driven largely by varying contributions from blood-associated or immune-associated cells, especially platelets and neutrophil-lineage cells, rather than by a single resident cervix or myometrium cell program. This should be tested with cell deconvolution, independent cohorts, spatial data, and perturbation or protein-level validation.

### Important genes

#### TPD52L2

- **Related proteins** (co-abundance neighbors): TAGLN2 (0.85), EIF6 (0.83), SEC22B (0.82), CNN3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TPD52 like 2. This gene encodes a member of the tumor protein D52-like family. These proteins are characterized by an N-terminal coiled-coil motif that is used to form homo- and heteromeric complexes with other tumor protein D52-like proteins. Expression of this gene may be a marker for breast cancer and acute lymphoblastic leukemia. Alternatively spliced transcript variants encoding multiple isoforms have been…
- **Diseases (Open Targets)**: breast cancer (0.088); breast carcinoma (0.087); neoplasm (0.078); gastric cancer (0.078); posterior cortical atrophy (0.077)
- **Europe PMC papers**: 1316
- **Why important**: TPD52L2 is the most connected gene in the module and links the translation-associated EIF6 branch with SEC22B, TAGLN2, and CNN3. Its tumor-protein-D52-like coiled-coil family supports a role in protein complex formation, while its vesicular localization and detection in both tissues make it a plausible organizing marker for the observed co-abundance pattern. It also has a comparatively substantial literature and reported links to proliferation and cancer biology.
- **Conclusion**: Established evidence supports TPD52L2 as the network-centered marker of this module and as a protein capable of participating in coiled-coil complexes. It is not established that TPD52L2 mechanistically drives the shared tissue module. Its centrality is a hypothesis-generating observation, not proof of causation.

#### EIF6

- **Related proteins** (co-abundance neighbors): CYRIB (0.83), TPD52L2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 6. Hemidesmosomes are structures which link the basal lamina to the intermediate filament cytoskeleton. An important functional component of hemidesmosomes is the integrin beta-4 subunit (ITGB4), a protein containing two fibronectin type III domains. The protein encoded by this gene binds to the fibronectin type III domains of ITGB4 and may help link ITGB4 to the intermediate filament cytoskeleton. T…
- **Diseases (Open Targets)**: neurodegenerative disease (0.153); urolithiasis (0.135); alcohol drinking (0.135); exstrophy-epispadias complex (0.118); freckles (0.115)
- **Europe PMC papers**: 1420
- **Why important**: EIF6 is positioned between TPD52L2 and CYRIB, making it a bridge between the module's central structural branch and its immune or apoptotic-associated branch. Its curated functions include ribosomal subunit export, ribosomal RNA maturation, translational initiation, and regulation of glycolytic processes. It is detected in cervix_uterine but not myometrium and has a substantial literature, making it informative for testing whether the module reflects translational state or tissue-composition differences.
- **Conclusion**: Established evidence supports EIF6 as a translation and ribosome-related factor with a bridging network position. The data do not establish that altered translation is the cause of the module, and the asymmetric tissue detection favors validation before assigning it a shared resident-tissue role.

#### CYRIB

- **Related proteins** (co-abundance neighbors): CASP3 (0.85), EIF6 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CYFIP related Rac1 interactor B. Enables small GTPase binding activity. Involved in several processes, including cellular response to molecule of bacterial origin; negative regulation of small GTPase mediated signal transduction; and regulation of organelle organization. Located in mitochondrion. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: smoking initiation (0.336); bronchial disorder (0.286); mathematical ability (0.270); Alzheimer disease (0.250); rheumatoid arthritis (0.232)
- **Europe PMC papers**: 75
- **Why important**: CYRIB connects EIF6 to CASP3 and is tissue enhanced in bone marrow, with HPA associations to microglia, neutrophil progenitors, and neutrophils. Its reported functions include small-GTPase binding, regulation of actin polymerization, cell migration, and T-cell-associated responses. These properties make it a candidate link between cytoskeletal remodeling and immune-cell composition. Its literature is more limited than that of CASP3 or EIF6, which increases the value of the module as a context for hypothesis generation.
- **Conclusion**: Established evidence supports CYRIB as a regulator-associated protein connected to actin, migration, and immune signaling. The module does not establish whether CYRIB represents resident tissue biology or infiltrating blood-lineage cells. Its role as an immune-to-cytoskeletal bridge is therefore a hypothesis.

#### CASP3

- **Related proteins** (co-abundance neighbors): CYRIB (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caspase 3. The protein encoded by this gene is a cysteine-aspartic acid protease that plays a central role in the execution-phase of cell apoptosis. The encoded protein cleaves and inactivates poly(ADP-ribose) polymerase while it cleaves and activates sterol regulatory element binding proteins as well as caspases 6, 7, and 9. This protein itself is processed by caspases 8, 9, and 10. It is the predominant ca…
- **Diseases (Open Targets)**: neurodegenerative disease (0.537); Kawasaki disease (0.455); response to vaccine (0.422); response to water (0.315); response to stimulus (0.290)
- **Europe PMC papers**: 51611
- **Why important**: CASP3 is the terminal member of the CYRIB branch and is a canonical execution-phase apoptotic protease with extensive literature and broad disease relevance. HPA associates it with innate lymphoid cells, megakaryocyte-erythroid progenitors, plasma cells, platelets, basophils, and eosinophils, while it is not detected by IHC in either reported tissue. This combination makes CASP3 biologically important but also especially compatible with a blood-cell or cell-state explanation for the module.
- **Conclusion**: Established evidence supports CASP3 as an apoptosis effector and as a marker associated with several immune and blood-related cell populations. Its co-abundance with CYRIB does not demonstrate active apoptosis in the tissues; it may instead reflect cell composition or shared stress states.

#### CNN3

- **Related proteins** (co-abundance neighbors): TPD52L2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calponin 3. This gene encodes a protein with a markedly acidic C terminus; the basic N-terminus is highly homologous to the N-terminus of a related gene, CNN1. Members of the CNN gene family all contain similar tandemly repeated motifs. This encoded protein is associated with the cytoskeleton but is not involved in contraction. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.492); pleural empyema (0.256); pneumothorax (0.256); biliary tract disorder (0.247); tooth disorder (0.196)
- **Europe PMC papers**: 1628
- **Why important**: CNN3 is directly connected to TPD52L2 and is localized to actin filaments. Its curated functions include actin filament organization, actomyosin structure organization, epithelial differentiation, and cell-cell adhesion. It is detected in both tissues, giving it stronger direct tissue support than several other module members, although HPA also associates it with trophoblast, epithelial, Schwann, and lymphocyte populations. Its literature is substantial relative to the smaller module and supports its value as a cytoskeletal marker.
- **Conclusion**: Established evidence supports CNN3 as a cytoskeletal and adhesion-associated protein present in both tissues. It may contribute to a shared structural or epithelial-associated state, but the module does not establish a specific smooth-muscle mechanism, especially because CNN3 is also associated with diverse cell types.

## Module 10

**Tissue pair**: cervix_uterine and myometrium  
**Genes (16)**: CTSC, CNN2, CACYBP, CSTB, CZIB, FHL2, FKBP3, GLRX, GSTP1, LYRM7, SNU13, PFDN6, PRDX3, RAN, SH3BGRL3, TXNDC17

### Function

The module is best interpreted as a coordinated redox, protein-homeostasis, cytoskeletal, and cellular-maintenance program rather than as a narrowly defined pathway. The strongest internal structure places TXNDC17 near the center, connected to GLRX, GSTP1, PRDX3, CSTB, CNN2, CTSC, FKBP3, LYRM7, PFDN6, and other members. TXNDC17, GLRX, GSTP1, and PRDX3 support thiol redox control, antioxidant defense, glutathione metabolism, and detoxification; this interpretation is consistent with the supplementary STRING InterPro annotation for a thioredoxin-like superfamily (STRING InterPro Thioredoxin-like superfamily; within-query FDR = 0.0117). CNN2 and FHL2 provide a cytoskeletal and actin-associated component, while LYRM7 supports mitochondrial complex III assembly and cellular respiration. CTSC and CSTB indicate lysosomal protease activity and intracellular protease control. No GO/KEGG term passed global correction, so the functional interpretation is gene-based and network-based rather than enrichment-confirmed. The absence of a globally significant term does not invalidate the module.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only a single member is annotated as secreted, and CTSC is described as intracellular and membrane-associated. HPA indicates low immune-cell specificity for nearly all members, with only FHL2 showing immune-cell enhancement for basophils. This argues against a straightforward blood-cell or plasma-protein explanation. The genes are nevertheless broadly distributed across tissues and cell types, with repeated enhancement in esophageal, muscle, trophoblast, germ-cell, and other epithelial or specialized cell populations. Thus, the shared cervix_uterine and myometrium signal may reflect a conserved cellular state, tissue admixture, or a common structural and stress-response program rather than a uterus-specific lineage. Protein detection is broader in cervix_uterine than in myometrium, and several genes lack protein detection in one of the tissues, so transcript or co-abundance behavior should not be equated automatically with uniform protein abundance.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

At the supplied high-confidence STRING threshold, none of the possible gene pairs has a recorded interaction. No hu.MAP complex contains multiple module members. The only STRING functional signal is the supplementary thioredoxin-like superfamily annotation (STRING InterPro Thioredoxin-like superfamily; within-query FDR = 0.0117), involving TXNDC17, SH3BGRL3, PRDX3, GLRX, and GSTP1. Therefore, the module is not supported as a known physical protein complex or as a densely documented interaction network. Its edges represent coordinated abundance, not demonstrated direct binding. The absence of STRING and hu.MAP relationships may indicate tissue-contextual regulation, indirect coupling, shared cell-state regulation, or incomplete database coverage.

**STRING interactions (score >= 0.7)**: 0 of 120 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: InterPro Thioredoxin-like superfamily (FDR = 0.0117, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may represent a previously unreported co-abundance association because it has no high-confidence STRING interactions, no multi-member hu.MAP complex, and no globally significant GO/KEGG term that would identify it as a canonical pathway. However, those absences do not prove biological novelty. Several individual genes and functions are well established, especially GSTP1, GLRX, CTSC, CNN2, PRDX3, RAN, and FHL2. The defensible conclusion is that the specific cross-tissue co-abundance configuration is potentially novel, while its component biology is not. Demonstrating a new finding would require replication in independent cervix_uterine and myometrium cohorts, adjustment for cell composition and technical effects, and comparison with published uterine co-expression modules.

**Hypothesis.** Hypothesis: the module reflects a shared tissue-cell stress adaptation in which thiol redox buffering and detoxification are coordinated with mitochondrial maintenance, protease control, and actin-based structural remodeling. TXNDC17, GLRX, GSTP1, and PRDX3 could buffer oxidative or electrophilic stress; LYRM7 could support respiratory-chain integrity; CTSC and CSTB could regulate intracellular proteolysis; and CNN2 with FHL2 could couple the state to actin organization, adhesion, or smooth-muscle mechanics. This is a mechanistic hypothesis, not a demonstrated pathway: the co-abundance edges do not establish direct molecular interactions or causal regulation.

### Important genes

#### TXNDC17

- **Related proteins** (co-abundance neighbors): LYRM7 (0.89), PFDN6 (0.89), GLRX (0.88), GSTP1 (0.87), CNN2 (0.87), CSTB (0.86), FKBP3 (0.84), CTSC (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin domain containing 17. Enables peroxidase activity and protein-disulfide reductase (NAD(P)) activity. Involved in tumor necrosis factor-mediated signaling pathway. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.339); hypertensive disorder (0.134); response to xenobiotic stimulus (0.095); ovarian cancer (0.075); ovarian carcinoma (0.075)
- **Europe PMC papers**: 292
- **Why important**: TXNDC17 is the most central network member by weighted connectivity and links the redox-associated genes to cytoskeletal, protease, folding, and mitochondrial-related members. Its annotated peroxidase and protein-disulfide-reductase activities, involvement in tumor necrosis factor signaling, detection in both tissues, and supplementary membership in the thioredoxin-like superfamily (STRING InterPro Thioredoxin-like superfamily; within-query FDR = 0.0117) make it a strong candidate organizing signal. Its literature volume is substantial, although less extensive than that of the best-studied redox genes in this module.
- **Conclusion**: Established evidence supports TXNDC17 as a redox and protein-disulfide-handling protein and as a central co-abundance hub. It is plausible, but unproven, that TXNDC17 helps coordinate the module's redox and protein-homeostasis behavior.

#### GLRX

- **Related proteins** (co-abundance neighbors): CNN2 (0.92), TXNDC17 (0.88), SH3BGRL3 (0.86), CTSC (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutaredoxin. This gene encodes a member of the glutaredoxin family. The encoded protein is a cytoplasmic enzyme catalyzing the reversible reduction of glutathione-protein mixed disulfides. This enzyme highly contributes to the antioxidant defense system. It is crucial for several signalling pathways by controlling the S-glutathionylation status of signalling mediators. It is involved in beta-amyloid toxicity a…
- **Diseases (Open Targets)**: hemolysis (0.351); adolescent idiopathic scoliosis (0.289); liver disorder (0.232); vascular disorder (0.203); musculoskeletal system disorder (0.171)
- **Europe PMC papers**: 1222
- **Why important**: GLRX connects TXNDC17 with CNN2, CTSC, and SH3BGRL3 and is one of the module's principal internal connectors. It is a cytoplasmic glutaredoxin that reverses protein glutathionylation and contributes to antioxidant defense and signaling control. It is detected at the plasma membrane and in the cytosol, is tissue-enhanced in skeletal muscle, and has extensive literature coverage. It also belongs to the supplementary thioredoxin-like signal (STRING InterPro Thioredoxin-like superfamily; within-query FDR = 0.0117).
- **Conclusion**: Established evidence supports GLRX as a regulator of thiol redox state and protein glutathionylation. Its network position makes it a credible candidate for linking redox state to actin-associated and protease-related processes, but that cross-process coupling remains a hypothesis.

#### GSTP1

- **Related proteins** (co-abundance neighbors): TXNDC17 (0.87), CZIB (0.87), PRDX3 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutathione S-transferase pi 1. Glutathione S-transferases (GSTs) are a family of enzymes that play an important role in detoxification by catalyzing the conjugation of many hydrophobic and electrophilic compounds with reduced glutathione. Based on their biochemical, immunologic, and structural properties, the soluble GSTs are categorized into 4 main classes: alpha, mu, pi, and theta. This GST family member is a polymorphic gene…
- **Diseases (Open Targets)**: neurodegenerative disease (0.350); breast cancer (0.117); hepatocellular carcinoma (0.115); neoplasm (0.114); posterior cortical atrophy (0.113)
- **Europe PMC papers**: 12759
- **Why important**: GSTP1 is connected to TXNDC17, CZIB, and PRDX3 and forms part of the supplementary thioredoxin-like annotation (STRING InterPro Thioredoxin-like superfamily; within-query FDR = 0.0117). Its established functions include glutathione conjugation, xenobiotic metabolism, response to reactive oxygen species, prostaglandin metabolism, and negative regulation of acute inflammatory responses. It is detected in both tissues and has the largest literature volume among the selected genes, making it an informative and biologically well-characterized anchor.
- **Conclusion**: Established evidence supports GSTP1 as a detoxification and oxidative-stress response enzyme. Its co-abundance with mitochondrial and thiol-redox genes is consistent with a coordinated protective state, but the module does not demonstrate that GSTP1 drives that state.

#### CTSC

- **Related proteins** (co-abundance neighbors): FHL2 (0.91), CNN2 (0.87), GLRX (0.84), TXNDC17 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cathepsin C. This gene encodes a member of the peptidase C1 family and lysosomal cysteine proteinase that appears to be a central coordinator for activation of many serine proteinases in cells of the immune system. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate heavy and light chains that form a disulfide…
- **Diseases (Open Targets)**: Papillon-Lefevre disease (0.837); Haim-Munk syndrome (0.802); periodontitis, aggressive 1 (0.676); periodontitis, aggressive (0.573); periodontitis (0.560)
- **Europe PMC papers**: 4518
- **Why important**: CTSC is connected to FHL2, CNN2, GLRX, and TXNDC17 and is detected in both tissues. It is a lysosomal cysteine protease that activates serine proteases in immune cells and is annotated for proteolysis, apoptotic processes, immune response, and protein catabolism. Its vesicular and intracellular or membrane-associated localization provides a plausible connection between protease regulation and cellular remodeling. It also has extensive literature and strong disease associations involving Papillon-Lefevre disease and Haim-Munk syndrome.
- **Conclusion**: Established evidence supports CTSC as a proteolytic and lysosomal regulator with disease relevance. Its placement beside redox and cytoskeletal genes suggests a possible role in coordinated tissue remodeling, but a shared immune mechanism is not supported because the module is generally low in immune-cell specificity.

#### CNN2

- **Related proteins** (co-abundance neighbors): GLRX (0.92), CTSC (0.87), TXNDC17 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calponin 2. The protein encoded by this gene, which can bind actin, calmodulin, troponin C, and tropomyosin, may function in the structural organization of actin filaments. The encoded protein could play a role in smooth muscle contraction and cell adhesion. Several pseudogenes of this gene have been identified, and are present on chromosomes 1, 2, 3, 6, 9, 11, 13, 15, 16, 21 and 22. Alternative splicing resu…
- **Diseases (Open Targets)**: Pulmonary artery atresia (0.416); asthma (0.410); retinitis pigmentosa (0.370); Alzheimer disease (0.366); chronic rhinosinusitis (0.333)
- **Europe PMC papers**: 983
- **Why important**: CNN2 links GLRX, CTSC, and TXNDC17 and is annotated to actin-filament organization, actomyosin structure, cellular response to mechanical stimulus, smooth-muscle contraction, and cell adhesion. Its localization to actin filaments and detection in cervix_uterine make it particularly relevant to the anatomical tissues under study, even though it is not detected in myometrium by the supplied HPA protein evidence. Its literature volume is substantial.
- **Conclusion**: Established evidence supports CNN2 as a structural and contractile regulator. It provides the clearest mechanical interface for the module, but the discrepant tissue protein detection and lack of direct interaction evidence mean that its proposed coupling to the redox program remains provisional.

## Module 11

**Tissue pair**: cervix_uterine and myometrium  
**Genes (7)**: CORO1B, DPYSL2, PKM, LTA4H, PDXK, PGM1, WDR1

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established single pathway annotation. Its gene content instead suggests a mixed program involving intermediary metabolism, cytoskeletal organization, cell motility, and inflammatory lipid mediator biology. DPYSL2, PDXK, and PGM1 point toward metabolic and cytoskeletal functions, while WDR1 and CORO1B support actin remodeling and LTA4H supports leukotriene biosynthesis and peptide processing. These themes should be regarded as biological interpretation of the gene set rather than globally significant enrichment. The co-abundance edges indicate coordinated abundance in the two tissues, not direct biochemical interactions.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not predominantly blood-cell specific, because most genes have low immune-cell specificity, although LTA4H and CORO1B have immune or myeloid-associated single-cell annotations and several genes show monocyte or dendritic-cell enrichment. The module is heterogeneous at the tissue level, including brain, skeletal muscle, and tongue enrichment, while every gene has some cell-type-enhanced annotation. This pattern is more consistent with a mixture of broadly distributed intracellular proteins and shared cell-type or cellular-state signals than with a simple plasma-protein or blood-contamination signature. Protein detection in cervix and myometrium is substantial but incomplete, and the absence of DPYSL2 protein detection in both tissues cautions against assuming that every transcript-level co-abundance relationship reflects abundant local protein.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no high-confidence interaction among the module genes and no supplementary STRING enrichment. Therefore, the module is not supported as a known STRING interaction neighborhood. hu.MAP provides limited complex-level support. LTA4H and PKM co-occur in huMAP complexes (hu.MAP huMAP3_14973.1) and (hu.MAP huMAP3_14442.1), while WDR1 and CORO1B co-occur in (hu.MAP huMAP3_11076.1). In each case, only a small subset of the larger complex is represented in the module. These observations support isolated links to known multiprotein contexts, but they do not establish one unified physical complex containing the module. The module is therefore best interpreted as a coordinated abundance pattern spanning several cellular systems rather than as a canonical protein complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14973.1 (LTA4H, PKM; 2/6); huMAP3_11076.1 (WDR1, CORO1B; 2/10); huMAP3_14442.1 (LTA4H, PKM; 2/57)

### Novelty

This may be a novel tissue-shared co-abundance module, because the exact module-level pattern is not represented by a corresponding STRING network and has only partial huMAP coverage. However, absence from STRING or huMAP does not prove novelty: co-abundance relationships can arise from shared cell composition, regulation, localization, or cellular state without being catalogued as direct interactions. The individual genes and their biological functions are well established to varying degrees, so the potentially new result is the coordinated behavior of this particular gene combination across cervix_uterine and myometrium, not the discovery of previously unknown gene functions or interactions.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular state involving metabolic capacity and actin-based structural remodeling in cells present in both tissues, with a possible contribution from myeloid-like or other cell-type composition signals. PGM1, PDXK, and PKM could represent carbohydrate, vitamin-cofactor, and energy metabolism, while WDR1 and CORO1B could support actin turnover and motility; LTA4H could connect the state to inflammatory lipid mediator and peptide processing biology, and DPYSL2 could link cytoskeletal organization to signaling. This hypothesis is not established by enrichment or physical-interaction evidence and requires validation with cell-resolved expression, protein measurements, and perturbation experiments.

### Important genes

#### DPYSL2

- **Related proteins** (co-abundance neighbors): PGM1 (0.91), WDR1 (0.89), PDXK (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Microtubules, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dihydropyrimidinase like 2. This gene encodes a member of the collapsin response mediator protein family. Collapsin response mediator proteins form homo- and hetero-tetramers and facilitate neuron guidance, growth and polarity. The encoded protein promotes microtubule assembly and is required for Sema3A-mediated growth cone collapse, and also plays a role in synaptic signaling through interactions with calcium channels. This…
- **Diseases (Open Targets)**: hypertensive disorder (0.431); autosomal dominant non-syndromic intellectual disability (0.370); cardiovascular disorder (0.297); ovarian neoplasm (0.292); glomerulonephritis (0.269)
- **Europe PMC papers**: 1328
- **Why important**: DPYSL2 is the strongest network-connected member in the module and links the metabolic neighbors PGM1 and PDXK with the actin-associated gene WDR1. Its established role in microtubule assembly, neuronal guidance, polarity, and signaling makes it a plausible coordinator of cytoskeletal and signaling-related abundance. It also has substantial literature and disease-association support, although its HPA profile is brain-enriched and its protein was not detected in either listed tissue.
- **Conclusion**: Established evidence supports DPYSL2 as a cytoskeletal and signaling protein with broad disease relevance. In this module, its central position supports a hypothesis that it helps connect metabolic and structural signals, but the tissue-level mechanism remains unproven and could also reflect shared cell composition.

#### PDXK

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.85), PGM1 (0.83), PKM (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyridoxal kinase. The protein encoded by this gene phosphorylates vitamin B6, a step required for the conversion of vitamin B6 to pyridoxal-5-phosphate, an important cofactor in intermediary metabolism. The encoded protein is cytoplasmic and probably acts as a homodimer. Alternatively spliced transcript variants have been described, but their biological validity has not been determined. [provided by RefSeq, Jul 200…
- **Diseases (Open Targets)**: neuropathy, hereditary motor and sensory, type VIc, with optic atrophy (0.581); neurodegenerative disease (0.429); autoimmune disorder of central nervous system (0.370); hypertensive disorder (0.188); ovarian neoplasm (0.169)
- **Europe PMC papers**: 859
- **Why important**: PDXK is a highly connected metabolic bridge linking DPYSL2 and PGM1 to PKM. It catalyzes a required step in vitamin B six cofactor salvage, giving the module a plausible connection to intermediary metabolism. Its disease associations include hereditary neuropathy and neurodegenerative disease, and its protein is detected in cervix but not myometrium.
- **Conclusion**: Established evidence supports PDXK as a vitamin B six metabolic enzyme. Its network position suggests coordinated regulation with carbohydrate and glycolytic proteins, but there is no evidence here that PDXK drives the module or that the module represents a vitamin B six pathway.

#### PGM1

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.91), PDXK (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglucomutase 1. The protein encoded by this gene is an isozyme of phosphoglucomutase (PGM) and belongs to the phosphohexose mutase family. There are several PGM isozymes, which are encoded by different genes and catalyze the transfer of phosphate between the 1 and 6 positions of glucose. In most cell types, this PGM isozyme is predominant, representing about 90% of total PGM activity. In red cells, PGM2 is a majo…
- **Diseases (Open Targets)**: PGM1-congenital disorder of glycosylation (0.843); MPDU1-congenital disorder of glycosylation (0.551); developmental and epileptic encephalopathy, 36 (0.551); RFT1-congenital disorder of glycosylation (0.551); disorder of glycogen metabolism (0.506)
- **Europe PMC papers**: 3203
- **Why important**: PGM1 connects DPYSL2 and PDXK and is a major phosphohexose mutase involved in glucose, glycogen, glycolytic, and glycosylation-related metabolism. It has the strongest literature support among the selected metabolic genes and well-established disease associations involving congenital glycosylation and glycogen metabolism. HPA detects the protein in both tissues and reports enrichment in skeletal muscle and tongue.
- **Conclusion**: Established evidence supports PGM1 as a central carbohydrate-metabolism enzyme with disease relevance. Its co-abundance with PDXK and PKM is compatible with a metabolic component in the module, but no globally corrected enrichment demonstrates that interpretation.

#### WDR1

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.89), CORO1B (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions, Cytosol; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: huMAP3_11076.1
- **Function (MyGene.info)**: WD repeat domain 1. This gene encodes a protein containing 9 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, mostly including a trp-asp at the C-terminal end. WD domains are involved in protein-protein interactions. The encoded protein may help induce the disassembly of actin filaments. Two transcript variants encoding different isoforms have been found for…
- **Diseases (Open Targets)**: periodic fever, immunodeficiency, and thrombocytopenia syndrome (0.705); gout (0.528); neurodegenerative disease (0.526); atrial fibrillation (0.519); intellectual developmental disorder 61 (0.416)
- **Europe PMC papers**: 1861
- **Why important**: WDR1 is connected to DPYSL2 and CORO1B and is represented in huMAP complex (hu.MAP huMAP3_11076.1). It participates in actin filament depolymerization, cortical cytoskeleton organization, platelet formation, and immune-related biology. Its HPA single-cell annotations include megakaryocytes and platelets, while its broad tissue profile and detection in both tissues make it relevant to local cellular structure as well as possible cell-type composition.
- **Conclusion**: Established evidence supports WDR1 as an actin-remodeling protein with immune and platelet-associated functions. Its placement between DPYSL2 and CORO1B supports a structural-remodeling interpretation, but it does not establish platelet contamination or a direct physical interaction in this module.

#### CORO1B

- **Related proteins** (co-abundance neighbors): LTA4H (0.85), WDR1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: huMAP3_11076.1
- **Function (MyGene.info)**: coronin 1B. Members of the coronin family, such as CORO1B, are WD repeat-containing actin-binding proteins that regulate cell motility (Cai et al., 2005 [PubMed 16027158]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Abnormality of refraction (0.067); refractive error (0.049); alcohol drinking (0.027); asthma (0.025); diabetes mellitus (0.025)
- **Europe PMC papers**: 339
- **Why important**: CORO1B is connected to WDR1 and LTA4H and is also represented with WDR1 in huMAP complex (hu.MAP huMAP3_11076.1). It is an actin-binding regulator of cell motility, ruffle organization, and Arp2/3-associated actin nucleation. Its immune-cell-enhanced annotation in non-classical monocytes and its detection in both tissues make it a plausible marker of cell-state or cellular-composition effects.
- **Conclusion**: Established evidence supports CORO1B as an actin organization and motility regulator. Its position may connect cytoskeletal remodeling with the LTA4H-associated inflammatory axis, but that connection is a hypothesis rather than a demonstrated molecular interaction.

#### LTA4H

- **Related proteins** (co-abundance neighbors): CORO1B (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: huMAP3_14973.1, huMAP3_14442.1
- **Function (MyGene.info)**: leukotriene A4 hydrolase. The protein encoded by this gene is an enzyme that contains both hydrolase and aminopeptidase activities. The hydrolase activity is used in the final step of the biosynthesis of leukotriene B4, a proinflammatory mediator. The aminopeptidase activity has been shown to degrade proline-glycine-proline (PGP), a neutrophil chemoattractant and biomarker for chronic obstructive pulmonary disease (COPD). …
- **Diseases (Open Targets)**: hypotensive disorder (0.198); small intestine neuroendocrine neoplasm (0.150); cystic fibrosis (0.104); COVID-19 (0.096); hepatocellular carcinoma (0.086)
- **Europe PMC papers**: 1823
- **Why important**: LTA4H is the module member most directly associated with inflammatory mediator biology. It produces leukotriene B four and also degrades the neutrophil chemoattractant PGP. It is represented with PKM in huMAP complexes (hu.MAP huMAP3_14973.1) and (hu.MAP huMAP3_14442.1), although those complexes contain many additional proteins and do not establish a focused LTA4H-PKM complex. Its single-cell annotations include monocytes and neutrophil progenitors, and it is detected in both tissues.
- **Conclusion**: Established evidence supports LTA4H as an enzyme involved in leukotriene production and peptide catabolism. Its inclusion is compatible with an inflammatory or myeloid-associated component, but the module data do not show that leukotriene signaling is the dominant function or that LTA4H directly regulates the other module genes.

## Module 12

**Tissue pair**: cervix_uterine and myometrium  
**Genes (7)**: GPS1, OPA1, PLXNB2, PPP1CB, SEC23IP, DARS1, UGGT1

### Function

The module does not support a single statistically established GO or KEGG function, because no GO or KEGG term passed global correction. Its genes instead point to a mixed cellular-maintenance program involving translation, protein folding and quality control, ER-to-Golgi trafficking, phosphatase-regulated signaling, cell adhesion or migration, and mitochondrial organization. DARS1 is the most connected node and links genes with otherwise diverse annotations, so the network may represent coordinated cellular state rather than a canonical pathway. The functional interpretation is therefore exploratory rather than a demonstrated pathway assignment.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only one member is annotated as secreted, while the others are intracellular, membrane-associated, vesicular, or nuclear and mitochondrial proteins. All members have low tissue specificity. Most have low immune-cell specificity, although PLXNB2 shows enrichment across several myeloid and dendritic-cell populations and PPP1CB is enhanced in hematopoietic stem cells and neutrophils. The single-cell enrichments are heterogeneous rather than concentrated in one shared cell type. HPA protein detection is broader in cervix_uterine than in myometrium, with several members detected in both tissues. Overall, the composition does not strongly support a plasma-protein or blood-cell explanation, but a contribution from shared or variable cell populations cannot be excluded.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was identified among the module members, and no hu.MAP complex contains multiple members. The co-abundance edges therefore do not recapitulate an already documented physical interaction network in these resources. Established biology remains relevant at the individual-gene level: SEC23IP is associated with ER exit sites and COPII-related transport, UGGT1 performs ER glycoprotein quality control, and PPP1CB is a catalytic PP1 subunit. These annotations support cellular maintenance and trafficking themes, but they do not establish direct interaction between the module proteins. The absence of STRING or hu.MAP support weakens a complex-based interpretation.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a previously unreported tissue-pair co-abundance pattern, particularly because the observed combination is not represented as a supported STRING interaction set or a shared hu.MAP complex. However, that database absence is not proof of biological novelty: co-abundance modules can reflect indirect regulation, shared cellular state, sample composition, or technical covariance, and the component genes have established functions and substantial prior literature. The appropriate conclusion is that the module-level association is potentially novel but presently unvalidated, rather than that it represents a newly discovered molecular complex or pathway.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program in cervix_uterine and myometrium that coordinates protein synthesis, ER quality control and export, phosphatase-dependent signaling, mitochondrial maintenance, and cell-surface adhesion or migration. DARS1 may act as the co-abundance hub connecting these otherwise separate processes, while the SEC23IP–UGGT1 relationship may represent a coordinated ER trafficking and proteostasis component. PLXNB2 could connect this state to cell interaction or migration, and OPA1 could reflect the energetic or stress state of the same cells. This hypothesis should be tested with replication, cell-composition adjustment, perturbation experiments, and independent protein-level measurements.

### Important genes

#### DARS1

- **Related proteins** (co-abundance neighbors): GPS1 (0.85), PLXNB2 (0.84), PPP1CB (0.82), OPA1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 1. This gene encodes a member of a multienzyme complex that functions in mediating the attachment of amino acids to their cognate tRNAs. The encoded protein ligates L-aspartate to tRNA(Asp). Mutations in this gene have been found in patients showing hypomyelination with brainstem and spinal cord involvement and leg spasticity. Alternative splicing results in multiple transcript variants. [provided by…
- **Diseases (Open Targets)**: hypomyelination with brain stem and spinal cord involvement and leg spasticity (0.773); atrial fibrillation (0.268); Abnormal brain morphology (0.266); tooth hard tissue disease (0.226); Pancreatic pseudocyst (0.225)
- **Europe PMC papers**: 238
- **Why important**: DARS1 is the most connected node in the module and links GPS1, PLXNB2, PPP1CB, and OPA1. Its established function is aspartate-tRNA ligation within protein translation and protein-containing complex assembly. It has a disease association with hypomyelination involving the brainstem and spinal cord and has a substantial literature base.
- **Conclusion**: Established evidence supports DARS1 as a translation-related gene and as the central co-abundance connector in this module. It is reasonable to hypothesize that it reports a broad cellular biosynthetic or stress state, but the data do not show that DARS1 regulates the other module members or that it defines a specific tissue pathway.

#### PPP1CB

- **Related proteins** (co-abundance neighbors): DARS1 (0.82), SEC23IP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase 1 catalytic subunit beta. The protein encoded by this gene is one of the three catalytic subunits of protein phosphatase 1 (PP1). PP1 is a serine/threonine specific protein phosphatase known to be involved in the regulation of a variety of cellular processes, such as cell division, glycogen metabolism, muscle contractility, protein synthesis, and HIV-1 viral transcription. Mouse studies suggest that PP1 functions as a supp…
- **Diseases (Open Targets)**: Noonan syndrome-like disorder with loose anagen hair 2 (0.742); Noonan syndrome-like disorder with loose anagen hair (0.721); Noonan syndrome (0.577); neurodegenerative disease (0.558); RASopathy (0.522)
- **Europe PMC papers**: 1420
- **Why important**: PPP1CB connects DARS1 with SEC23IP and encodes a catalytic subunit of protein phosphatase one. Its established functions include protein dephosphorylation, MAPK-related regulation, cell adhesion, circadian regulation, and control of muscle contractility. It has extensive literature and multiple RASopathy-related disease associations.
- **Conclusion**: Established evidence supports PPP1CB as a broad signaling and dephosphorylation regulator with plausible relevance to smooth-muscle and adhesion-related cellular behavior. Its bridging position makes it an important interpretive candidate, but the module does not establish a specific PPP1CB-mediated mechanism.

#### SEC23IP

- **Related proteins** (co-abundance neighbors): UGGT1 (0.88), PPP1CB (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC23 interacting protein. This gene encodes a member of the phosphatidic acid preferring-phospholipase A1 family. The encoded protein is localized to endoplasmic reticulum exit sites and plays a critical role in ER-Golgi transport as part of the multimeric coat protein II complex. An orthologous gene in frogs is required for normal neural crest cell development, suggesting that this gene may play a role in Waardenburg synd…
- **Diseases (Open Targets)**: Parkinson disease (0.409); type 2 diabetes mellitus (0.372); cardiomyopathy (0.326); diabetes mellitus (0.294); Genu valgum (0.269)
- **Europe PMC papers**: 265
- **Why important**: SEC23IP is connected to PPP1CB and UGGT1 and is localized to ER exit sites. Its established functions involve ER-to-Golgi vesicle transport, Golgi organization, and endomembrane organization. It also has annotations related to spermatid development and disease associations including cardiomyopathy and diabetes-related conditions.
- **Conclusion**: Established evidence supports SEC23IP as an ER export and vesicle-trafficking factor. Its connection to UGGT1 makes coordinated proteostasis and secretory-pathway activity a plausible interpretation, but no direct interaction between these proteins is supported by the supplied STRING or hu.MAP results.

#### UGGT1

- **Related proteins** (co-abundance neighbors): SEC23IP (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UDP-glucose glycoprotein glucosyltransferase 1. UDP-glucose:glycoprotein glucosyltransferase (UGT) is a soluble protein of the endoplasmic reticulum (ER) that selectively reglucosylates unfolded glycoproteins, thus providing quality control for protein transport out of the ER.[supplied by OMIM, Oct 2009].
- **Diseases (Open Targets)**: congenital disorder of glycosylation (0.416); hypercholesterolemia, familial, 1 (0.333); connective tissue disorder (0.234); ovarian dysfunction (0.216); chronic laryngitis (0.147)
- **Europe PMC papers**: 507
- **Why important**: UGGT1 is the partner of SEC23IP in the co-abundance graph and performs ER glycoprotein quality control by reglucosylating incompletely folded glycoproteins. Its annotations include protein N-linked glycosylation, glycoprotein biosynthesis, post-translational folding, and ER mannose trimming. It is associated with congenital disorders of glycosylation and other disease areas.
- **Conclusion**: Established evidence supports UGGT1 as an ER proteostasis and glycoprotein-quality-control factor. Its co-abundance with SEC23IP is consistent with a secretory-pathway hypothesis, but the absence of STRING and complex evidence means that a direct functional partnership in this tissue module remains unproven.

#### OPA1

- **Related proteins** (co-abundance neighbors): DARS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OPA1 mitochondrial dynamin like GTPase. The protein encoded by this gene is a nuclear-encoded mitochondrial protein with similarity to dynamin-related GTPases. The encoded protein localizes to the inner mitochondrial membrane and helps regulate mitochondrial stability and energy output. This protein also sequesters cytochrome c. Mutations in this gene have been associated with optic atrophy type 1, which is a dominantly inherited optic …
- **Diseases (Open Targets)**: autosomal dominant optic atrophy, classic form (0.846); Behr syndrome (0.812); optic atrophy with or without deafness, ophthalmoplegia, myopathy, ataxia, and neuropathy (0.766); mitochondrial DNA depletion syndrome 14B (cardioencephalomyopathic type) (0.745); optic atrophy (0.653)
- **Europe PMC papers**: 12169
- **Why important**: OPA1 is linked to the central DARS1 node and encodes a mitochondrial inner-membrane dynamin-like GTPase involved in mitochondrial fusion, organization, stability, and energy output, including cytochrome c sequestration. It has a very large literature base and strong disease associations with dominant optic atrophy and related mitochondrial disorders.
- **Conclusion**: Established evidence supports OPA1 as a mitochondrial architecture and energy-maintenance gene. Its presence may indicate that mitochondrial state covaries with the module's biosynthetic and trafficking processes, but the module does not demonstrate that mitochondrial remodeling drives the shared tissue signal.

## Module 13

**Tissue pair**: cervix_uterine and myometrium  
**Genes (5)**: PSMC4, KARS1, CCT3, CCT7, CCT8

### Function

The strongest interpretation is an intracellular proteostasis and protein-folding module centered on the CCT/TRiC chaperonin. The primary evidence is the globally corrected enrichment of the chaperonin-containing T-complex and protein-folding chaperone complex (GO:CC chaperonin-containing T-complex; q_global = 0.00113), (GO:CC protein folding chaperone complex; q_global = 0.0128), together with ATP-dependent protein-folding and ATP-hydrolysis annotations (GO:MF ATP-dependent protein folding chaperone; q_global = 0.0218), (GO:MF ATP hydrolysis activity; q_global = 0.0302). CCT3, CCT7, and CCT8 account for the recurrent enrichment across terms involving protein localization to the nucleus and Cajal body, telomerase-RNA localization, telomere maintenance, chromosome organization, DNA biosynthesis, and fertilization-related recognition (14 globally significant GO/KEGG terms, q_global 0.00113–0.00234; see the table), (9 globally significant GO/KEGG terms, q_global 0.00409–0.00935; see the table), (GO:BP positive regulation of telomere maintenance; q_global = 0.0169) (GO:BP positive regulation of chromosome organization; q_global = 0.0169) (GO:BP regulation of telomere maintenance; q_global = 0.0218), (GO:BP single fertilization; q_global = 0.0272) (GO:BP cell recognition; q_global = 0.0272) (GO:BP DNA biosynthetic process; q_global = 0.0272), (4 globally significant GO/KEGG terms, q_global 0.0334–0.0477; see the table). The telomere, fertilization, and recognition annotations should be interpreted cautiously: they are driven by the same CCT genes and may reflect annotation structure or broad chaperone biology rather than a tissue-specific reproductive mechanism. The complete-module intracellular-complex annotation (GO:CC intracellular protein-containing complex; q_global = 0.00375) and the ATP-hydrolysis annotation (GO:MF ATP hydrolysis activity; q_global = 0.0302) support a broader interpretation in which chaperone activity is accompanied by proteasomal and translational proteostasis. The sparse co-abundance topology is consistent with a compact core: the CCT genes form the most strongly connected triangle, while PSMC4 and KARS1 are peripheral links.

**Cell composition.** This is not a plasma-protein or blood-cell module. HPA reports low immune-cell specificity for every member, no enriched blood-cell group, and no broad tissue-enriched pattern. All members have low tissue specificity, and the proteins are detected in cervix_uterine; nearly all are detected in myometrium. The composition is therefore consistent mainly with broadly expressed intracellular housekeeping and proteostasis machinery rather than a secreted tissue product. HPA reports one secreted gene at the module level, but KARS1 is specifically described as intracellular and membrane-associated, so this does not support a plasma or extracellular interpretation. The repeated enrichment of spermatocyte and spermatid cell types for several members, together with oocyte enhancement for CCT8, may indicate cell-state or germ-cell-related expression programs, but it is not evidence for blood contamination and does not by itself establish a reproductive function in these tissues.

**GO/KEGG enrichment**: 38 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chaperonin-containing T-complex | 0.00113 | CCT3, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 0.00113 | CCT3, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 0.00113 | CCT3, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 0.00113 | CCT3, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 0.00113 | CCT3, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 0.00113 | CCT3, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 0.00113 | CCT3, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 0.00113 | CCT3, CCT7, CCT8 |
| GO:BP binding of sperm to zona pellucida | 0.00234 | CCT3, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 0.00234 | CCT3, CCT7, CCT8 |
| GO:BP RNA localization to Cajal body | 0.00234 | CCT3, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 0.00234 | CCT3, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 0.00234 | CCT3, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 0.00234 | CCT3, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomere lengthening | 0.00234 | CCT3, CCT7, CCT8 |

### STRING and hu.MAP

STRING provides very strong known relationships among CCT3, CCT7, and CCT8: each pair is connected, forming the central CCT triangle. STRING supplementary enrichment identifies the TCP-1 chaperonin family, the chaperonin-containing T-complex, cellular proteostasis, and CCT-mediated folding of tubulin, actin, and G-protein beta (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 0.00037), (13 supplementary STRING terms; within-query FDR 0.0017–0.0043). The carcinoma-cell STRING annotation (STRING TISSUES Carcinoma cell; within-query FDR = 0.0015) is contextual and should not be treated as a tissue-specific functional conclusion. hu.MAP independently places CCT3, CCT7, and CCT8 together in several complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1), and in an additional lower-confidence complex containing CCT3 and CCT7 (hu.MAP huMAP3_01951.1). These complexes include other CCT subunits, TCP1, prefoldin-related proteins, tubulin-related proteins, and regulatory proteins. PSMC4 and KARS1 have no listed STRING partners and no listed hu.MAP complex membership in this module, so their co-abundance links are not independently established as direct physical interactions.

**STRING interactions (score >= 0.7)**: 3 of 10 gene pairs: CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT7–CCT8 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam TCP-1/cpn60 chaperonin family (FDR = 0.00037, 3 genes); TISSUES Carcinoma cell (FDR = 0.0015, 5 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 0.0017, 3 genes); Component Chaperonin-containing T-complex (FDR = 0.0017, 3 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 0.002, 3 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 0.002, 3 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 0.002, 3 genes); InterPro GroEL-like apical domain superfamily (FDR = 0.002, 3 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 0.002, 3 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 0.002, 3 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis (FDR = 0.0036, 3 genes); RCTM Formation of tubulin folding intermediates by CCT/TriC (FDR = 0.0043, 3 genes); RCTM Folding of actin by CCT/TriC (FDR = 0.0043, 3 genes); RCTM Association of TriC/CCT with target proteins during biosynthesis (FDR = 0.0043, 3 genes); RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding (FDR = 0.0043, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT3, CCT8, CCT7; 3/23); huMAP3_06559.1 (CCT3, CCT8, CCT7; 3/25); huMAP3_09191.1 (CCT3, CCT8, CCT7; 3/32); huMAP3_10656.1 (CCT3, CCT8, CCT7; 3/36); huMAP3_14584.1 (CCT3, CCT8, CCT7; 3/61); huMAP3_01951.1 (CCT3, CCT7; 2/8)

### Novelty

The module is unlikely to represent a newly discovered molecular complex: the central CCT3–CCT7–CCT8 relationships are already strongly supported by STRING, and their joint membership in multiple hu.MAP complexes is established (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). The chaperone, folding, proteostasis, actin, and tubulin interpretations are therefore confirmatory rather than novel. A potentially useful finding is the conserved co-abundance of this compact CCT-centered program across cervix_uterine and myometrium, with PSMC4 and KARS1 as peripheral co-abundant genes, but the fact sheet alone cannot establish that this tissue-pair pattern has not been reported previously. Absence of PSMC4 or KARS1 from the listed STRING and hu.MAP relationships does not prove novelty; it may reflect incomplete interaction coverage, indirect regulation, or co-abundance without physical binding. The reproductive and telomere-related annotations are hypothesis-generating, not evidence that this module constitutes a novel reproductive pathway.

**Hypothesis.** Hypothesis: in both tissues, a broadly expressed intracellular proteostasis program coordinates CCT/TRiC-mediated folding with protein turnover and aminoacylation capacity. CCT3, CCT7, and CCT8 may provide the chaperone core, PSMC4 may connect the program to ATP-dependent proteasomal degradation, and KARS1 may reflect the translation-supporting supply of charged lysine tRNA. This coordinated activity could help maintain cytoskeletal, nuclear, and other newly synthesized proteins in smooth-muscle and cervical cells. The Cajal-body, telomerase, and reproductive annotations suggest testable possibilities involving nuclear RNA handling or reproductive cell states, but these are hypotheses rather than established functions of this tissue-shared module.

### Important genes

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT8 (0.82), CCT7 (0.81); STRING partners: CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a central member of the highest-confidence functional core: it connects to both CCT7 and CCT8, participates in every listed globally corrected enrichment involving the CCT trio, and is present in all listed hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). Its annotation identifies it as a subunit of the ATP-dependent TRiC chaperonin that folds proteins including actin and tubulin. It also has the largest literature volume among the module genes in the fact sheet and has multiple disease associations in Open Targets.
- **Conclusion**: Established: CCT3 is a broadly expressed intracellular CCT/TRiC chaperone subunit and a central network component, with strong functional support from (15 globally significant GO/KEGG terms, q_global 0.00113–0.00234; see the table), (22 globally significant GO/KEGG terms, q_global 0.00409–0.0477; see the table), (15 supplementary STRING terms; within-query FDR 0.00037–0.0043), and (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). Hypothesis: its co-abundance may mark tissue-wide demand for cytoskeletal and general protein-folding capacity rather than a specialized cervical or myometrial pathway.

#### CCT7

- **Related proteins** (co-abundance neighbors): CCT3 (0.81); STRING partners: CCT3 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is part of the central CCT triangle with CCT3 and CCT8 and appears in the same globally corrected CCT, folding, telomere-related, nuclear-localization, and fertilization-related terms. It is included in all listed hu.MAP complexes and in the STRING chaperonin and proteostasis enrichments. Its annotation supports ATP-dependent folding of actin and tubulin, while its disease associations include myocardial infarction, preeclampsia, neurodegenerative disease, and hepatocellular carcinoma.
- **Conclusion**: Established: CCT7 is a core TRiC component with strong independent network and complex support. Hypothesis: its presence in the shared module may be relevant to maintaining contractile-cell proteostasis, but the available evidence does not demonstrate a direct role in myometrial contraction or cervical function.

#### CCT8

- **Related proteins** (co-abundance neighbors): PSMC4 (0.88), CCT3 (0.82); STRING partners: CCT3 (0.999), CCT7 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is a core network node connected to CCT3 and CCT7 and is represented in every globally corrected term and every listed STRING supplementary term. It is present in the higher-confidence hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). Its annotation describes a CCT/TRiC chaperone subunit involved in protein folding and protein stabilization, and HPA detects it in cervix_uterine. It has substantial literature coverage and cancer-related Open Targets associations.
- **Conclusion**: Established: CCT8 is a central, well-supported component of the chaperone core. Hypothesis: its cell-type enhancement in oocytes and its reproductive annotations may reflect a conserved protein-folding program shared with germ-cell states, but they do not establish an oocyte-like process in either tissue.

#### PSMC4

- **Related proteins** (co-abundance neighbors): CCT8 (0.88), KARS1 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 4. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.603); mantle cell lymphoma (0.542); neoplasm (0.519); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1065
- **Why important**: PSMC4 is a peripheral but mechanistically informative connector, linking CCT8 with KARS1 in the co-abundance graph. It contributes to the intracellular-complex and ATP-hydrolysis primary terms (GO:CC intracellular protein-containing complex; q_global = 0.00375), (GO:MF ATP hydrolysis activity; q_global = 0.0302), and its annotation identifies it as an ATPase subunit of the proteasome regulatory particle involved in proteasomal protein catabolism and responses to oxidative stress. It has a substantial literature volume and disease associations involving plasma-cell myeloma, lymphoma, neoplasm, HIV infection, and amyloidosis.
- **Conclusion**: Established: PSMC4 supports a proteostasis interpretation through proteasomal ATPase biology, although it has no listed STRING partner or hu.MAP complex in this module. Hypothesis: its co-abundance with the CCT core may indicate coupling between protein folding and selective protein turnover.

#### KARS1

- **Related proteins** (co-abundance neighbors): PSMC4 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lysyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. Lysyl-tRNA synthetase is a homodimer localized to the cytoplasm which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Alternatively spliced transcript variants encoding different…
- **Diseases (Open Targets)**: leukoencephalopathy, progressive, infantile-onset, with or without deafness (0.753); deafness, congenital, and adult-onset progressive leukoencephalopathy (0.714); autosomal recessive nonsyndromic hearing loss 89 (0.685); Charcot-Marie-Tooth disease recessive intermediate B (0.670); deafness (0.534)
- **Europe PMC papers**: 232
- **Why important**: KARS1 is the most peripheral module member, linked only to PSMC4, but it adds a distinct translation-related function. Its annotation identifies lysyl-tRNA synthetase as the enzyme that charges tRNA with lysine and supports protein translation and tRNA processing. It is detected in both tissues, has low tissue specificity, is enhanced in cardiomyocytes and germ-cell states, and has established associations with inherited neurological and hearing disorders.
- **Conclusion**: Established: KARS1 is a broadly expressed aminoacyl-tRNA synthetase whose co-abundance is consistent with protein-production capacity, but it has no listed STRING or hu.MAP relationship in this module. Hypothesis: KARS1 may be a peripheral readout of translational demand coupled to chaperone activity and proteasomal quality control, rather than a physical component of the CCT complex.
