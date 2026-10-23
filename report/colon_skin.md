# Conserved co-abundance modules: colon and skin

## Module 0

**Tissue pair**: colon and skin  
**Genes (26)**: AATF, ANAPC4, BYSL, CAMSAP2, CEP170, DDX55, ERICH1, EZH2, GSDME, KIF1B, KRI1, LRCH3, MICAL3, MICALL1, PRRC2B, RBM15, RINT1, SASH1, SP110, SRFBP1, SRPK2, TRAPPC8, TTC27, VIRMA, ZC3H7B, ZFYVE1

### Function

The most defensible interpretation is a broad intracellular gene-expression and RNA-processing module, with a prominent nucleolar and ribosome-biogenesis component. This interpretation is supported by the annotations of SRFBP1, KRI1, AATF, BYSL and DDX55, together with their nucleolar locations and the STRING-connected subnetwork involving these genes. Additional module members indicate RNA modification, alternative RNA processing, transcriptional regulation, cytoskeletal organization, vesicle trafficking and cell-cycle control, so the module is not functionally homogeneous. No GO or KEGG term passed global correction, and STRING reported no functional enrichment; therefore the functional interpretation is based on convergent individual-gene annotations and network structure rather than enrichment significance.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and nearly all are detected at the protein level in both colon and skin. The module is therefore compatible with broadly expressed intracellular biology rather than a tissue-specific secretory program. HPA also shows cell-type enhancement for many genes, with recurring signals in late spermatids, neutrophils, oocytes and syncytiotrophoblasts, while several genes show bone-marrow, lymphoid or immune-cell associations. This raises the possibility that part of the shared colon-skin signal reflects common cellular constituents or variable immune and hematopoietic contributions, although the overall profile does not support a simple blood-cell module because many genes have low immune-cell specificity and some are not detected in immune cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known relationships form a nucleolar and ribosome-biogenesis cluster around AATF, BYSL, DDX55, KRI1 and SRFBP1. STRING also links VIRMA with RBM15, providing an established connection between RNA modification and RNA-binding regulation. These relationships support the biological plausibility of the co-abundance module, but STRING evidence is supplementary and does not establish enrichment of the whole module. The remaining co-abundance edges are not represented by high-confidence STRING relationships in the fact sheet, so the network extends beyond already catalogued protein associations. No hu.MAP complex contains multiple module members, which argues against identifying the module as a known canonical physical complex.

**STRING interactions (score >= 0.7)**: 8 of 325 gene pairs: AATF–BYSL (0.998); AATF–DDX55 (0.73); AATF–KRI1 (0.732); BYSL–DDX55 (0.727); BYSL–KRI1 (0.742); BYSL–SRFBP1 (0.971); KRI1–SRFBP1 (0.727); RBM15–VIRMA (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be called a newly discovered molecular complex or a proven new pathway. Its central biological themes are established: nucleolar RNA processing, ribosome biogenesis, RNA methylation and post-transcriptional regulation are represented by known genes and some known STRING relationships. The potentially novel observation is the cross-tissue co-abundance configuration linking this nucleolar RNA-processing cluster with genes involved in cytoskeletal organization, trafficking, chromatin regulation, cell-cycle control and immune-associated cell types in colon and skin. That configuration is not recapitulated by a hu.MAP multi-member complex and is only partly represented in STRING. Its novelty therefore concerns the tissue-shared co-abundance pattern and its biological context, not the individual gene functions. Independent replication, control for cell composition and comparison with published colon-skin coexpression modules would be needed before claiming a new finding.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in colon and skin in which nucleolar ribosome production and RNA maturation are coordinated with growth, differentiation, intracellular trafficking and stress-responsive programs. The co-abundance signal may arise from broadly expressed epithelial or stromal cells together with variable contributions from immune or hematopoietic cells, rather than from one stable physical complex. A testable prediction is that the nucleolar subnetwork and the cell-composition-associated genes will separate when analyses are repeated within purified cell populations or after adjustment for cellular composition.

### Important genes

#### SRFBP1

- **Related proteins** (co-abundance neighbors): ZC3H7B (0.83), ERICH1 (0.83), RINT1 (0.81), TRAPPC8 (0.81), VIRMA (0.81), GSDME (0.80), AATF (0.80); STRING partners: BYSL (0.971), KRI1 (0.727)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serum response factor binding protein 1. Enables RNA binding activity. Predicted to be involved in maturation of SSU-rRNA. Predicted to be located in perinuclear region of cytoplasm. Predicted to be part of 90S preribosome. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: familial thoracic aortic aneurysm and aortic dissection (0.547); Aortic dissection (0.474); marfan syndrome/loeys-dietz syndrome/familial thoracic aortic aneurysms and dissections (0.474); Abnormality of the cardiovascular system (0.470); Familial hemophagocytic lymphohistiocytosis (0.266)
- **Europe PMC papers**: 150
- **Why important**: SRFBP1 is a central connector in the annotated co-abundance network and links several module branches. It is detected in both colon and skin, localizes to the nucleolar rim, and is annotated for SSU-rRNA maturation and the ninety-S preribosome. Its high-confidence STRING links to BYSL and KRI1 reinforce the interpretation of a nucleolar RNA-processing core. Its disease associations include aortic and cardiovascular disorders and familial hemophagocytic lymphohistiocytosis, while its literature volume is substantial enough to support a well-established but still context-dependent interpretation.
- **Conclusion**: Established evidence supports SRFBP1 as an important marker of the module's nucleolar and ribosome-biogenesis component. Hypothesis: SRFBP1 may act as a bridge coordinating this core with trafficking, cytoskeletal and stress-related module branches. The co-abundance data do not prove that it directly regulates those branches.

#### AATF

- **Related proteins** (co-abundance neighbors): ERICH1 (0.83), SRFBP1 (0.80); STRING partners: BYSL (0.998), DDX55 (0.73), KRI1 (0.732)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apoptosis antagonizing transcription factor. The protein encoded by this gene was identified on the basis of its interaction with MAP3K12/DLK, a protein kinase known to be involved in the induction of cell apoptosis. This gene product contains a leucine zipper, which is a characteristic motif of transcription factors, and was shown to exhibit strong transactivation activity when fused to Gal4 DNA binding domain. Overexpression of this gene i…
- **Diseases (Open Targets)**: skin neoplasm (0.147); generalized dystonia (0.116); multinodular goiter (0.115); bone fracture (0.113); neoplasm (0.107)
- **Europe PMC papers**: 6349
- **Why important**: AATF connects the module's high-confidence STRING ribosome-biogenesis relationships with the co-abundance network. It is detected in both tissues, localizes to nucleoli, and has annotations for SSU-rRNA maturation, small-subunit biogenesis, the unfolded-protein response and transcriptional regulation. It has a large literature base and disease associations including skin neoplasm and neurological or developmental phenotypes, making it a biologically informative anchor rather than an uncharacterized connector.
- **Conclusion**: Established evidence supports AATF as a nucleolar RNA-biogenesis and stress-response regulator within the module. Hypothesis: its position may indicate coordination between ribosome production and survival or proteostasis programs in shared colon and skin cells. The network does not establish causality.

#### VIRMA

- **Related proteins** (co-abundance neighbors): ERICH1 (0.88), SP110 (0.82), SRFBP1 (0.81); STRING partners: RBM15 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vir like m6A methyltransferase associated. Enables RNA binding activity. Involved in mRNA alternative polyadenylation and mRNA methylation. Located in cytosol and nuclear speck. Colocalizes with RNA N6-methyladenosine methyltransferase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: smoking initiation (0.355); Abnormality of the skeletal system (0.355); obesity disorder (0.344); orofacial cleft (0.256); cleft palate (0.221)
- **Europe PMC papers**: 1994
- **Why important**: VIRMA is a well-studied RNA-regulatory factor with a large literature base. It is annotated for mRNA methylation and alternative polyadenylation, is detected in both tissues, and connects in the module to ERICH1, SP110 and SRFBP1. Its very strong STRING relationship with RBM15 provides established external support for an RNA-modification and RNA-processing axis. Its disease and trait associations include skeletal abnormalities, obesity-related disease and craniofacial phenotypes.
- **Conclusion**: Established evidence supports VIRMA as the module's strongest marker of post-transcriptional RNA regulation and mRNA modification. Hypothesis: VIRMA may connect nucleolar or ribosome-related activity with broader RNA fate control in the shared tissue state. The module alone cannot determine whether RNA methylation drives the co-abundance pattern.

#### KRI1

- **Related proteins** (co-abundance neighbors): ERICH1 (0.84), SP110 (0.82); STRING partners: AATF (0.732), BYSL (0.742), SRFBP1 (0.727)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: KRI1 homolog. This gene overlaps with the gene for cysteine endopeptidase AUT-like 4 in a head-to-tail orientation. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: metabolic disease (0.293); neurodegenerative disease (0.220); osteoarthritis (0.044); Knee pain (0.028); arthropathy (0.027)
- **Europe PMC papers**: 172
- **Why important**: KRI1 is a focused nucleolar component with an annotation for endonucleolytic processing that separates ribosomal RNA products. It is detected in both colon and skin and participates in the STRING-supported cluster involving AATF, BYSL and SRFBP1. Although its literature volume and disease evidence are more limited than those of several other candidates, its specific function and network placement make it useful for defining the module's mechanistic core.
- **Conclusion**: Established evidence supports KRI1 as a ribosomal RNA-processing component within the module. Hypothesis: KRI1 may help explain why the module preserves a nucleolar signal across distinct tissues. Its low network connectivity means that it should be treated as a focused marker rather than as a demonstrated master regulator.

#### SP110

- **Related proteins** (co-abundance neighbors): KRI1 (0.82), VIRMA (0.82), RBM15 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SP110 nuclear body protein. The nuclear body is a multiprotein complex that may have a role in the regulation of gene transcription. This gene is a member of the SP100/SP140 family of nuclear body proteins and encodes a leukocyte-specific nuclear body component. The protein can function as an activator of gene transcription and may serve as a nuclear hormone receptor coactivator. In addition, it has been suggested that the p…
- **Diseases (Open Targets)**: hepatic veno-occlusive disease-immunodeficiency syndrome (0.763); lymphoid neoplasm (0.359); B-cell chronic lymphocytic leukemia (0.358); Crohn disease (0.348); leukemia (0.272)
- **Europe PMC papers**: 1706
- **Why important**: SP110 links the VIRMA-RBM15 RNA-regulatory branch to a gene with leukocyte-associated biology. It is annotated as a nuclear-body protein involved in transcriptional regulation, with suggested roles in ribosome biogenesis and myeloid differentiation. HPA shows cell-type enhancement in B cells, neutrophils and plasmacytoid dendritic cells, and its disease associations include immunodeficiency, lymphoid neoplasm, chronic lymphocytic leukemia and Crohn disease. Its substantial literature volume makes it important for interpreting possible immune or cell-composition contributions.
- **Conclusion**: Established evidence supports SP110 as a nuclear regulatory protein with immune-cell relevance and a STRING-supported link to VIRMA and RBM15. Hypothesis: SP110 may mark an immune-associated contribution to the shared module or connect immune-state regulation with RNA processing. The data do not establish that the module is immune-cell driven.

## Module 1

**Tissue pair**: colon and skin  
**Genes (45)**: ABCF1, ATXN2, ZNHIT6, BIRC5, BRD2, CHAF1B, CDK12, CWC27, DSCC1, DHX16, DSN1, ERF, HIRIP3, HPS6, JUNB, LARP4, LARP7, LEO1, MAP7D1, MAP7D3, MAD1L1, MMTAG2, MPHOSPH6, MYO9B, RASAL2, PHIP, MOB4, PPP4R1, PPHLN1, PTPN2, QSER1, RAD18, RBM6, RMC1, SDE2, SNIP1, SUZ12, GTF2A2, GTF3C2, TGS1, TJAP1, TRIM32, UHRF1, WDR70, ZFC3H1

### Function

The strongest functional interpretation is a nuclear gene-expression and genome-maintenance module. The only globally corrected GO/KEGG evidence is (GO:BP nucleic acid metabolic process; q_global = 0.0488), nucleic acid metabolic process, with broad overlap across the module. This umbrella annotation is consistent with the module's concentration of DNA-damage and replication factors, chromatin regulators, transcription machinery, RNA-processing proteins, and cell-cycle components. RAD18, UHRF1, CHAF1B, DSCC1, and SUZ12 support DNA repair, chromatin maintenance, replication, and epigenetic regulation; CDK12, LEO1, LARP7, ERF, GTF2A2, and GTF3C2 support transcription; and RBM6, CWC27, DHX16, SNIP1, TGS1, MPHOSPH6, and ZFC3H1 support RNA processing, splicing, or ribonucleoprotein maturation. The STRING supplementary terms (STRING Keyword Ubl conjugation; within-query FDR = 0.001) and (STRING Keyword Isopeptide bond; within-query FDR = 0.0011) suggest enrichment for ubiquitin-like or isopeptide-bond biology, while (STRING Keyword Nucleus; within-query FDR = 0.0246) supports a nuclear localization theme, but these are supplementary rather than globally corrected evidence. The module therefore appears to represent coordinated nuclear information processing, linking transcription and RNA maturation with chromatin, DNA-damage tolerance, and proliferative control. The absence of additional globally corrected terms does not invalidate this interpretation; it indicates that the evidence is distributed across related nuclear processes rather than concentrated in a narrowly defined pathway.

**Cell composition.** This is not a plasma or secreted-protein module: HPA reports no secreted genes, and nearly all members are detected at the protein level in both colon and skin. Most genes have low tissue specificity and low immune-cell specificity, which argues against the module being explained primarily by blood contamination or a narrowly restricted blood-cell population. Nevertheless, the module contains some context-sensitive markers. PTPN2 and MYO9B are tissue enhanced in lymphoid tissue, BIRC5 and UHRF1 are enriched in bone marrow or lymphoid-associated contexts, and several genes show immune-cell enhancement, especially in neutrophils or T-reg cells. Many members are also enhanced in proliferative, germ-cell, epithelial, or progenitor-like cell types. The shared colon-skin signal is therefore most plausibly a broadly expressed nuclear program, potentially strengthened by shared epithelial or proliferative cell states, rather than a secreted or predominantly blood-derived signature.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP nucleic acid metabolic process | 0.0488 | ATXN2, BIRC5, BRD2, CDK12, CHAF1B, CWC27, DHX16, DSCC1, ERF, GTF2A2, GTF3C2, JUNB, LARP7, LEO1, MPHOSPH6, PHIP, PPHLN1, PTPN2, RAD18, RBM6, SDE2, SNIP1, SUZ12, TGS1, TRIM32, UHRF1, ZFC3H1, ZNHIT6 |

### STRING and hu.MAP

The high-confidence STRING network is selective rather than comprehensive. Established relationships include the very strong CWC27-DHX16 and CWC27-SNIP1 connections, the strong DHX16-SNIP1 connection, MPHOSPH6-ZFC3H1, CDK12-LEO1, and lower-confidence links involving BIRC5-UHRF1 and SUZ12-UHRF1. These relationships independently support spliceosome or RNA-processing biology, RNA surveillance or ribonucleoprotein maturation, transcriptional regulation, and chromatin or cell-cycle control. hu.MAP provides additional complex-level support: ERF and TRIM32 occur together in (hu.MAP huMAP3_08608.1); RBM6 and PPHLN1 recur together across the related complexes (hu.MAP huMAP3_08625.1) through (hu.MAP huMAP3_10098.1) and (hu.MAP huMAP3_14523.1); BRD2 and CWC27 occur together in (hu.MAP huMAP3_11931.1); SNIP1 and CDK12 occur together in (hu.MAP huMAP3_09621.1); PPP4R1 and MOB4 recur in (hu.MAP huMAP3_09709.1), (hu.MAP huMAP3_10333.1), and (hu.MAP huMAP3_13510.1); and LARP7 with MMTAG2 occurs in (hu.MAP huMAP3_05807.1). These are partial complex overlaps, often involving only a small subset of the annotated complex, so they support shared molecular neighborhoods rather than proving that the entire module is one physical complex. Overall, known interactions validate several local substructures, while the full co-abundance organization extends beyond currently catalogued physical interactions.

**STRING interactions (score >= 0.7)**: 7 of 990 gene pairs: BIRC5–UHRF1 (0.707); CDK12–LEO1 (0.788); CWC27–DHX16 (0.998); CWC27–SNIP1 (0.997); DHX16–SNIP1 (0.997); MPHOSPH6–ZFC3H1 (0.954); SUZ12–UHRF1 (0.704)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Ubl conjugation (FDR = 0.001, 23 genes); Keyword Isopeptide bond (FDR = 0.0011, 20 genes); Keyword Nucleus (FDR = 0.0246, 29 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08608.1 (ERF, TRIM32; 2/5); huMAP3_08625.1 (RBM6, PPHLN1; 2/6); huMAP3_01533.1 (RBM6, PPHLN1; 2/7); huMAP3_09463.1 (RBM6, PPHLN1; 2/7); huMAP3_09569.1 (RBM6, PPHLN1; 2/9); huMAP3_07030.1 (RBM6, PPHLN1; 2/10); huMAP3_08950.1 (RBM6, PPHLN1; 2/10); huMAP3_09973.1 (RBM6, PPHLN1; 2/10); huMAP3_10643.1 (RBM6, PPHLN1; 2/13); huMAP3_09895.1 (RBM6, PPHLN1; 2/14); huMAP3_09778.1 (RBM6, PPHLN1; 2/16); huMAP3_10098.1 (RBM6, PPHLN1; 2/17); huMAP3_11931.1 (BRD2, CWC27; 2/19); huMAP3_14523.1 (RBM6, PPHLN1; 2/33); huMAP3_09621.1 (SNIP1, CDK12; 2/56); huMAP3_09709.1 (PPP4R1, MOB4; 2/57); huMAP3_10333.1 (PPP4R1, MOB4; 2/63); huMAP3_05807.1 (LARP7, MMTAG2; 2/81); huMAP3_13510.1 (PPP4R1, MOB4; 2/85)

### Novelty

The module should not be described as a wholly new molecular pathway. Its component biology is largely established: DNA repair, chromatin regulation, transcription, RNA splicing, ribosome or snoRNP maturation, and mitotic control are well documented, and several local relationships are already represented in STRING or hu.MAP. The potentially novel result is the reproducible co-abundance organization of these otherwise distinct nuclear functions across colon and skin. The sparse direct STRING connectivity and partial hu.MAP overlaps suggest that the tissue-shared module is not simply a known canonical complex. However, absence from STRING or hu.MAP cannot establish novelty because those resources emphasize physical interactions and curated complexes, whereas co-abundance can arise from coordinated regulation, shared cell state, or indirect functional coupling. The appropriate conclusion is that this is a potentially novel cross-tissue co-abundance signature built from largely established molecular functions, requiring validation in independent cohorts and cell-composition-aware analyses.

**Hypothesis.** Hypothesis: the module is a coordinated nuclear stress-and-proliferation program that maintains transcriptional output and RNA maturation while protecting chromosome integrity. In this model, RAD18 and UHRF1 connect DNA-damage tolerance, ubiquitin-linked regulation, chromatin maintenance, and replication-associated control; CDK12, LEO1, LARP7, and ERF tune RNA polymerase transcription; and CWC27, DHX16, SNIP1, RBM6, MPHOSPH6, and ZFC3H1 maintain splicing, RNA surveillance, and ribonucleoprotein maturation. BIRC5, DSCC1, and MAD1L1 could reflect the proliferative and chromosome-segregation component, whereas PPHLN1 and epithelial-associated HPA patterns may reflect shared barrier-cell differentiation. This model predicts that the module will be strongest in proliferating or stressed epithelial compartments and will track coordinated DNA-repair, chromatin, transcription, and RNA-processing activity rather than secretion. It remains a hypothesis because co-abundance alone does not establish directionality, physical interaction, or causal regulation.

### Important genes

#### RAD18

- **Related proteins** (co-abundance neighbors): LEO1 (0.90), DHX16 (0.87), MAD1L1 (0.85), CHAF1B (0.85), PTPN2 (0.85), TRIM32 (0.84), UHRF1 (0.83), WDR70 (0.83), PPHLN1 (0.82), SUZ12 (0.82), MMTAG2 (0.82), LARP4 (0.82), MYO9B (0.82), ATXN2 (0.81), DSCC1 (0.81), MPHOSPH6 (0.81), HIRIP3 (0.80), LARP7 (0.80), GTF3C2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAD18 E3 ubiquitin protein ligase. The protein encoded by this gene is highly similar to S. cerevisiae DNA damage repair protein Rad18. Yeast Rad18 functions through its interaction with Rad6, which is an ubiquitin-conjugating enzyme required for post-replication repair of damaged DNA. Similar to its yeast counterpart, this protein is able to interact with the human homolog of yeast Rad6 protein through a conserved ring-finger moti…
- **Diseases (Open Targets)**: neurodegenerative disease (0.434); cervical carcinoma (0.283); myocardial ischemia (0.269); lysosomal storage disease (0.258); generalized dystonia (0.205)
- **Europe PMC papers**: 2815
- **Why important**: RAD18 is the highest-connectivity hub in the supplied module and links many of its nuclear neighborhoods, including LEO1, DHX16, MAD1L1, CHAF1B, PTPN2, TRIM32, UHRF1, and WDR70. Its established E3 ubiquitin-ligase function, DNA-damage tolerance, DNA-damage response, and protein monoubiquitination directly anchor the module's genome-maintenance interpretation. It is present in the primary term (GO:BP nucleic acid metabolic process; q_global = 0.0488) and all supplementary STRING themes (STRING Keyword Ubl conjugation; within-query FDR = 0.001) through (STRING Keyword Nucleus; within-query FDR = 0.0246), has nuclear localization, and has substantial literature support and disease-relevance evidence.
- **Conclusion**: Established evidence supports RAD18 as a central genome-maintenance and ubiquitin-linked regulator within the module. Its hub position makes it an important organizing candidate, but the co-abundance data do not establish that RAD18 regulates the other module members or that all of its apparent connections are physical.

#### ERF

- **Related proteins** (co-abundance neighbors): PHIP (0.88), QSER1 (0.85), ABCF1 (0.85), LEO1 (0.83), PTPN2 (0.82), MAP7D1 (0.82), RASAL2 (0.81), JUNB (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in colon, skin
- **hu.MAP 3.0**: huMAP3_08608.1
- **Function (MyGene.info)**: ETS2 repressor factor. ETS2 is a transcription factor and protooncogene involved in development, apoptosis, and the regulation of telomerase. The protein encoded by this gene binds to the ETS2 promoter and is a strong repressor of ETS2 transcription. Several transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Aug 2015].
- **Diseases (Open Targets)**: craniosynostosis 4 (0.709); Chitayat syndrome (0.708); craniosynostosis (0.619); Lambdoidal craniosynostosis (0.559); TWIST1-related craniosynostosis (0.548)
- **Europe PMC papers**: 17324
- **Why important**: ERF is a transcriptional repressor with extensive literature support and the strongest supplied literature volume among the module's transcriptional regulators. It occupies a connected position linking PHIP, QSER1, ABCF1, LEO1, PTPN2, MAP7D1, RASAL2, and JUNB, and it participates in (GO:BP nucleic acid metabolic process; q_global = 0.0488) and the supplementary nuclear and ubiquitin-related themes (STRING Keyword Ubl conjugation; within-query FDR = 0.001) through (STRING Keyword Nucleus; within-query FDR = 0.0246). Its hu.MAP support with TRIM32 in (hu.MAP huMAP3_08608.1) adds a complex-level connection, while its disease associations include craniosynostosis-related conditions.
- **Conclusion**: Established evidence supports ERF as a transcriptional-control component that may help connect general nuclear regulation with cell differentiation and signaling. Its position supports a coordinating role, but a specific ERF-driven mechanism for the colon-skin module remains hypothetical.

#### CDK12

- **Related proteins** (co-abundance neighbors): ZNHIT6 (0.85), RBM6 (0.83); STRING partners: LEO1 (0.788)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in colon, skin
- **hu.MAP 3.0**: huMAP3_09621.1
- **Function (MyGene.info)**: cyclin dependent kinase 12. Enables RNA polymerase II CTD heptapeptide repeat kinase activity and cyclin binding activity. Involved in phosphorylation of RNA polymerase II C-terminal domain; protein autophosphorylation; and regulation of MAP kinase activity. Located in nuclear speck. Part of cyclin K-CDK12 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: prostate adenocarcinoma (0.638); neurodegenerative disease (0.565); Alzheimer disease (0.502); lysosomal storage disease (0.501); Parkinson disease (0.501)
- **Europe PMC papers**: 4245
- **Why important**: CDK12 provides a direct mechanistic bridge between transcription and RNA processing. It phosphorylates the RNA polymerase transcriptional machinery, regulates transcription elongation and RNA splicing, appears in (GO:BP nucleic acid metabolic process; q_global = 0.0488) and (STRING Keyword Ubl conjugation; within-query FDR = 0.001) through (STRING Keyword Nucleus; within-query FDR = 0.0246), has a STRING relationship with LEO1, and shares the hu.MAP complex (hu.MAP huMAP3_09621.1) with SNIP1. It also has extensive literature support and established associations with prostate cancer and several neurological or lysosomal disease contexts.
- **Conclusion**: Established evidence supports CDK12 as a plausible transcriptional-elongation and RNA-processing anchor of the module. The network supports coordinated activity with LEO1 and SNIP1, but does not demonstrate that CDK12 is the causal driver of the shared tissue pattern.

#### CWC27

- **Related proteins** (co-abundance neighbors): TGS1 (0.83), ZNHIT6 (0.82), QSER1 (0.81); STRING partners: DHX16 (0.998), SNIP1 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon, skin
- **hu.MAP 3.0**: huMAP3_11931.1
- **Function (MyGene.info)**: CWC27 spliceosome associated cyclophilin. Predicted to enable peptidyl-prolyl cis-trans isomerase activity. Predicted to be involved in protein peptidyl-prolyl isomerization. Located in nucleoplasm. Part of U2-type precatalytic spliceosome and catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: metaphyseal chondrodysplasia-retinitis pigmentosa syndrome (0.764); retinitis pigmentosa (0.450); inherited retinal dystrophy (0.433); Abnormality of the skeletal system (0.421); diverticular disease (0.394)
- **Europe PMC papers**: 282
- **Why important**: CWC27 is a spliceosome-associated cyclophilin involved in catalytic-stage splicing and protein peptidyl-prolyl isomerization. It forms one of the clearest local STRING structures in the module with DHX16 and SNIP1, is included in (GO:BP nucleic acid metabolic process; q_global = 0.0488) and (STRING Keyword Nucleus; within-query FDR = 0.0246), and also occurs with BRD2 in hu.MAP complex (hu.MAP huMAP3_11931.1). Its disease associations include inherited skeletal and retinal disorders, giving it strong functional and clinical relevance despite a more localized network position than RAD18.
- **Conclusion**: Established evidence supports CWC27 as a concrete RNA-splicing component and a key local anchor for the module's RNA-processing arm. Its relationship to the broader DNA-repair and chromatin program is supported mainly by co-abundance and network context, so that broader integration remains a hypothesis.

#### UHRF1

- **Related proteins** (co-abundance neighbors): RAD18 (0.83); STRING partners: BIRC5 (0.707), SUZ12 (0.704)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin like with PHD and ring finger domains 1. This gene encodes a member of a subfamily of RING-finger type E3 ubiquitin ligases. The protein binds to specific DNA sequences, and recruits a histone deacetylase to regulate gene expression. Its expression peaks at late G1 phase and continues during G2 and M phases of the cell cycle. It plays a major role in the G1/S transition by regulating topoisomerase IIalpha and retinoblastoma gene expressi…
- **Diseases (Open Targets)**: hypertensive disorder (0.450); type 2 diabetes mellitus (0.424); immunodeficiency-centromeric instability-facial anomalies syndrome (0.371); neurodegenerative disease (0.367); coronary artery disorder (0.362)
- **Europe PMC papers**: 4824
- **Why important**: UHRF1 links DNA methylation or chromatin-associated regulation, ubiquitin-ligase activity, DNA-damage response, and cell-cycle control. It connects to RAD18 and has STRING relationships with BIRC5 and SUZ12, thereby joining genome maintenance, proliferation, and epigenetic repression. It is included in (GO:BP nucleic acid metabolic process; q_global = 0.0488) and (STRING Keyword Ubl conjugation; within-query FDR = 0.001) through (STRING Keyword Nucleus; within-query FDR = 0.0246), has group-enriched HPA expression in bone marrow and lymphoid tissue, and has extensive literature and disease-association support.
- **Conclusion**: Established evidence supports UHRF1 as an epigenetic and genome-maintenance component, with a possible proliferative or progenitor-state contribution to the module. Its HPA pattern warrants attention to cell-state composition, but does not by itself show that blood or lymphoid cells generated the shared colon-skin signal.

#### PPHLN1

- **Related proteins** (co-abundance neighbors): RAD18 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon, skin
- **hu.MAP 3.0**: huMAP3_08625.1, huMAP3_01533.1, huMAP3_09463.1, huMAP3_09569.1, huMAP3_07030.1, huMAP3_08950.1, huMAP3_09973.1, huMAP3_10643.1, huMAP3_09895.1, huMAP3_09778.1, huMAP3_10098.1, huMAP3_14523.1
- **Function (MyGene.info)**: periphilin 1. The protein encoded by this gene is one of the several proteins that become sequentially incorporated into the cornified cell envelope during the terminal differentiation of keratinocyte at the outer layers of epidermis. This protein interacts with periplakin, which is known as a precursor of the cornified cell envelope. The cellular localization pattern and insolubility of this protein suggest th…
- **Diseases (Open Targets)**: alcohol drinking (0.252); actinic keratosis (0.247); stroke disorder (0.224); hypothyroidism (0.224); systemic lupus erythematosus (0.211)
- **Europe PMC papers**: 360
- **Why important**: PPHLN1 is especially informative for the cross-tissue interpretation because it is associated with terminal keratinocyte differentiation and epidermal barrier integrity, while also appearing in the primary nucleic-acid term (GO:BP nucleic acid metabolic process; q_global = 0.0488). It has a strong module connection to RAD18 and repeatedly co-occurs with RBM6 across many hu.MAP complexes (hu.MAP huMAP3_08625.1) through (hu.MAP huMAP3_10098.1) and (hu.MAP huMAP3_14523.1). Its literature volume is moderate, and its disease associations include actinic keratosis and systemic lupus erythematosus, which are relevant to epithelial and immune contexts.
- **Conclusion**: Established evidence supports PPHLN1 as an epithelial-differentiation and chromatin-associated component that may help explain why the module is shared by colon and skin. Its inclusion in a broad nuclear module could reflect coordinated epithelial state rather than a direct PPHLN1-centered complex, so the proposed barrier-linked role remains partly hypothetical.

## Module 2

**Tissue pair**: colon and skin  
**Genes (25)**: ACACA, C5orf22, CHD1, COPB1, DDX21, EPHB6, EXOSC1, GFPT1, GNAI3, NOL6, NOL9, RDX, RFX1, PDCD11, SMARCA4, SMN1, XAB2, TBL3, TCEA1, THUMPD1, TMEM222, TTI1, UTP15, UTP4, ZC3H14

### Function

The module is best interpreted as a conserved nucleolar RNA-processing and ribosome-biogenesis module. The primary evidence is the concordant set of globally corrected terms for rRNA metabolic process (GO:BP rRNA metabolic process; q_global = 0.000247), ribonucleoprotein complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.000877), nucleolus (GO:CC nucleolus; q_global = 0.000973), rRNA processing (GO:BP rRNA processing; q_global = 0.00104), small-subunit processome (GO:CC small-subunit processome; q_global = 0.00232), ribosome biogenesis (GO:BP ribosome biogenesis; q_global = 0.00623), RNA processing (GO:BP RNA processing; q_global = 0.00726), and preribosome (GO:CC preribosome; q_global = 0.0179). These terms implicate maturation and assembly of ribosomal RNA, especially the small ribosomal subunit. The module contains a functionally coherent core formed by PDCD11, NOL6, NOL9, TBL3, UTP15, UTP4, EXOSC1, and DDX21. The sparse co-abundance graph appears to have a broad connector, EPHB6, linking this core to genes involved in transcription, chromatin, vesicle biology, metabolism, and membrane or cytoskeletal functions. Those peripheral links should not be interpreted as proof that all module members execute the same biochemical reaction.

**Cell composition.** This is not primarily a plasma-protein, secreted-protein, or blood-cell module. HPA identifies only one secreted gene, and the module shows generally low immune-cell specificity, so a blood-contamination explanation is not favored. Most genes have low tissue specificity and protein detection is reported in both colon and skin for most assessed genes, consistent with a broadly expressed intracellular program. There is nevertheless substantial cell-type variation, including enrichment or enhancement in keratinocytes, esophageal apical cells, spermatogenic cells, neurons, and selected epithelial or stromal populations. The shared colon-skin signal could therefore reflect a conserved housekeeping-like nucleolar program across resident cells, with additional contributions from shared epithelial or proliferative states rather than a secreted or circulating component.

**GO/KEGG enrichment**: 8 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP rRNA metabolic process | 0.000247 | DDX21, EXOSC1, NOL6, NOL9, PDCD11, SMARCA4, TBL3, UTP15, UTP4 |
| GO:BP ribonucleoprotein complex biogenesis | 0.000877 | DDX21, EXOSC1, NOL6, NOL9, PDCD11, SMN1, TBL3, UTP15, UTP4, XAB2 |
| GO:CC nucleolus | 0.000973 | ACACA, DDX21, EXOSC1, GNAI3, NOL6, NOL9, PDCD11, SMARCA4, TBL3, TCEA1, UTP15, UTP4, ZC3H14 |
| GO:BP rRNA processing | 0.00104 | DDX21, EXOSC1, NOL6, NOL9, PDCD11, TBL3, UTP15, UTP4 |
| GO:CC small-subunit processome | 0.00232 | NOL6, PDCD11, TBL3, UTP15, UTP4 |
| GO:BP ribosome biogenesis | 0.00623 | DDX21, EXOSC1, NOL6, NOL9, PDCD11, TBL3, UTP15, UTP4 |
| GO:BP RNA processing | 0.00726 | DDX21, EXOSC1, NOL6, NOL9, PDCD11, SMN1, TBL3, THUMPD1, UTP15, UTP4, XAB2, ZC3H14 |
| GO:CC preribosome | 0.0179 | NOL6, PDCD11, TBL3, UTP15, UTP4 |

### STRING and hu.MAP

STRING supports a known rRNA-processing and nucleolar interaction core. The strongest and most repeated relationships connect NOL6, PDCD11, TBL3, UTP15, UTP4, and EXOSC1, while NOL9 and DDX21 provide additional links within the rRNA-processing neighborhood. TCEA1 and XAB2 form a separate known relationship associated with transcription and RNA processing. The STRING functional results (STRING RCTM rRNA processing in the nucleus and cytosol; within-query FDR = 1.23e-06) through (STRING NetworkNeighborAL Small-subunit processome; within-query FDR = 0.0068) independently converge on rRNA processing, rRNA modification, preribosome, nucleolus, and RNA metabolism, but these are supplementary and not global enrichment evidence. hu.MAP provides direct complex support through a complex containing UTP15, UTP4, and EXOSC1 (hu.MAP huMAP3_14264.1), and another containing UTP15 and UTP4 (hu.MAP huMAP3_01743.1). Thus, the module contains a recognizable molecular core rather than being supported only by co-abundance. Conversely, several highly connected co-abundance links, especially those involving EPHB6, have no corresponding STRING partner or hu.MAP complex in the fact sheet and should be treated as associations requiring validation.

**STRING interactions (score >= 0.7)**: 18 of 300 gene pairs: EXOSC1–NOL6 (0.791); EXOSC1–PDCD11 (0.757); EXOSC1–TBL3 (0.912); EXOSC1–UTP15 (0.848); EXOSC1–UTP4 (0.887); NOL6–PDCD11 (0.999); NOL6–TBL3 (0.999); NOL6–UTP15 (0.998); NOL6–UTP4 (0.999); NOL9–PDCD11 (0.819); NOL9–UTP15 (0.732); PDCD11–TBL3 (0.996); PDCD11–UTP15 (0.987); PDCD11–UTP4 (0.999); TBL3–UTP15 (0.999); TBL3–UTP4 (0.999); TCEA1–XAB2 (0.898); UTP15–UTP4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM rRNA processing in the nucleus and cytosol (FDR = 1.23e-06, 9 genes); RCTM Major pathway of rRNA processing in the nucleolus and cytosol (FDR = 7.51e-06, 8 genes); RCTM rRNA modification in the nucleus and cytosol (FDR = 2.02e-05, 6 genes); COMPARTMENTS Nucleolus (FDR = 3.97e-05, 12 genes); Keyword rRNA processing (FDR = 0.00058, 6 genes); RCTM Metabolism of RNA (FDR = 0.00064, 11 genes); NetworkNeighborAL rRNA processing, and Ribosomal large subunit biogenesis (FDR = 0.00074, 8 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 0.0011, 7 genes); Process rRNA processing (FDR = 0.0015, 8 genes); Process Ribonucleoprotein complex biogenesis (FDR = 0.0015, 10 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0017, 15 genes); Component Nucleolus (FDR = 0.0021, 12 genes); Process ncRNA processing (FDR = 0.0047, 9 genes); COMPARTMENTS 90S preribosome (FDR = 0.006, 4 genes); NetworkNeighborAL Small-subunit processome (FDR = 0.0068, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14264.1 (UTP15, UTP4, EXOSC1; 3/20); huMAP3_01743.1 (UTP15, UTP4; 2/6)

### Novelty

The central biological interpretation is not a wholly new ribosome-biogenesis discovery: the principal genes, interactions, and complexes are already represented in STRING, hu.MAP, and the literature. The potentially novel aspect is the coordinated co-abundance of this established nucleolar machinery with EPHB6 and a set of transcriptional, chromatin, metabolic, vesicular, and membrane-associated genes across colon and skin. That cross-tissue conservation may indicate a shared cellular-state program or a previously underappreciated regulatory context, but it cannot be called a new molecular complex from the present evidence. Absence of some genes from STRING or hu.MAP is not evidence of novelty, because database coverage and assay context are incomplete. The finding is therefore best described as a potentially novel tissue-pair co-abundance pattern built around a known RNA-processing program.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of nucleolar output in shared colon and skin epithelial states. A change in cellular growth, differentiation, stress, or tissue repair could increase the demand for rRNA maturation and ribosome assembly, producing synchronized abundance of the PDCD11-NOL6-TBL3-UTP15-UTP4-EXOSC1 core. EPHB6 may act as a cell-state or adhesion-associated correlate that connects this nucleolar program to epithelial organization, migration, or differentiation, but its role in the module is not established by the available interaction databases. The hypothesis predicts that module activity should track nucleolar transcription and ribosome-biogenesis measurements within matched colon and skin cell populations, and that the EPHB6 association should be tested separately from the established rRNA-processing core.

### Important genes

#### PDCD11

- **Related proteins** (co-abundance neighbors): NOL6 (0.84), EPHB6 (0.84), TMEM222 (0.81); STRING partners: EXOSC1 (0.757), NOL6 (0.999), NOL9 (0.819), TBL3 (0.996), UTP15 (0.987), UTP4 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 11. PDCD11 is a NF-kappa-B (NFKB1; 164011)-binding protein that colocalizes with U3 RNA (MIM 180710) in the nucleolus and is required for rRNA maturation and generation of 18S rRNA (Sweet et al., 2003 [PubMed 14624448]; Sweet et al., 2008 [PubMed 17654514]).[supplied by OMIM, Oct 2008].
- **Diseases (Open Targets)**: Back pain (0.277); insomnia (0.216); systemic lupus erythematosus (0.170); neoplasm (0.095); colorectal carcinoma (0.093)
- **Europe PMC papers**: 334
- **Why important**: PDCD11 is a central biological anchor despite modest local graph connectivity. It appears in every globally corrected term (GO:BP rRNA metabolic process; q_global = 0.000247) through (GO:CC preribosome; q_global = 0.0179), is localized at the nucleolar rim, and is detected in both colon and skin. Its established function includes association with U3 RNA, rRNA maturation, and generation of mature small-subunit rRNA. STRING places it in the dense interaction core with NOL6, TBL3, UTP15, UTP4, EXOSC1, and NOL9. Its disease associations include systemic lupus erythematosus and colorectal carcinoma, and its literature provides direct mechanistic support.
- **Conclusion**: Established conclusion: PDCD11 is a core rRNA-processing component and a strong marker of the module's nucleolar function. Hypothesis: variation in PDCD11 abundance may help tune ribosome production in shared colon and skin cellular states, but the co-abundance data do not establish that it drives the state.

#### UTP15

- **Related proteins** (co-abundance neighbors): EPHB6 (0.84), UTP4 (0.84); STRING partners: EXOSC1 (0.848), NOL6 (0.998), NOL9 (0.732), PDCD11 (0.987), TBL3 (0.999), UTP4 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14264.1, huMAP3_01743.1
- **Function (MyGene.info)**: UTP15 small subunit processome component. Enables RNA binding activity. Involved in positive regulation of rRNA processing and positive regulation of transcription by RNA polymerase I. Located in endoplasmic reticulum and fibrillar center. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.354); Parkinson disease (0.251); Alzheimer disease (0.251); lysosomal storage disease (0.251); male reproductive organ cancer (0.114)
- **Europe PMC papers**: 234
- **Why important**: UTP15 is present in every globally corrected term (GO:BP rRNA metabolic process; q_global = 0.000247) through (GO:CC preribosome; q_global = 0.0179) and in nearly all relevant STRING functional categories. It is a small-subunit processome component with established roles in rRNA processing, small-subunit maturation, and regulation of RNA polymerase I transcription. It participates in both hu.MAP complexes (hu.MAP huMAP3_14264.1) and (hu.MAP huMAP3_01743.1) and has strong STRING relationships with the principal nucleolar core. Its HPA localization is nucleolar, and its disease-oriented literature includes neurodegenerative conditions and male reproductive cancer.
- **Conclusion**: Established conclusion: UTP15 is a molecularly supported component of the small-subunit processome and one of the most informative functional markers of this module. Hypothesis: UTP15 abundance may coordinate the module with changes in RNA polymerase I output, although causal regulation is not demonstrated.

#### UTP4

- **Related proteins** (co-abundance neighbors): UTP15 (0.84); STRING partners: EXOSC1 (0.887), NOL6 (0.999), PDCD11 (0.999), TBL3 (0.999), UTP15 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_14264.1, huMAP3_01743.1
- **Function (MyGene.info)**: UTP4 small subunit processome component. This gene encodes a WD40-repeat-containing protein that is localized to the nucleolus. Mutation of this gene causes North American Indian childhood cirrhosis, a severe intrahepatic cholestasis that results in transient neonatal jaundice, and progresses to periportal fibrosis and cirrhosis in childhood and adolescence. Alternative splicing results in multiple transcript variants. [provided by RefSe…
- **Diseases (Open Targets)**: hereditary North American Indian childhood cirrhosis (0.420); cardiovascular disorder (0.101); basal cell carcinoma (0.079); hypertensive disorder (0.064); osteosarcoma (0.052)
- **Europe PMC papers**: 214
- **Why important**: UTP4 is present in every globally corrected term (GO:BP rRNA metabolic process; q_global = 0.000247) through (GO:CC preribosome; q_global = 0.0179), has strong STRING relationships throughout the nucleolar core, and occurs in both hu.MAP complexes (hu.MAP huMAP3_14264.1) and (hu.MAP huMAP3_01743.1). It is a nucleolar WD-repeat protein involved in maturation of small-subunit rRNA and ribosome biogenesis. Its disease association with North American Indian childhood cirrhosis gives the gene an established clinical link to tissue and cellular consequences of disrupted ribosome production. HPA detects the protein in skin, while the transcript-level module association extends across the colon-skin pair.
- **Conclusion**: Established conclusion: UTP4 is a core small-subunit processome component and a strong bridge between the co-abundance module and known ribosome-biogenesis complexes. Hypothesis: UTP4 may be particularly informative for testing whether the conserved module represents altered small-subunit assembly rather than generic RNA abundance.

#### NOL6

- **Related proteins** (co-abundance neighbors): PDCD11 (0.84), DDX21 (0.81); STRING partners: EXOSC1 (0.791), PDCD11 (0.999), TBL3 (0.999), UTP15 (0.998), UTP4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleolar protein 6. The nucleolus is a dense subnuclear membraneless organelle that assembles around clusters of rRNA genes and functions in ribosome biogenesis. This gene encodes a nucleolar RNA-associated protein that is highly conserved between species. RNase treatment of permeabilized cells indicates that the nucleolar localization is RNA dependent. Further studies suggest that the protein is associated with ribo…
- **Diseases (Open Targets)**: neurodegenerative disease (0.119); hepatocellular carcinoma (0.054); hidradenitis (0.052); response to xenobiotic stimulus (0.045); gastric cancer (0.036)
- **Europe PMC papers**: 335
- **Why important**: NOL6 is present in every globally corrected term (GO:BP rRNA metabolic process; q_global = 0.000247) through (GO:CC preribosome; q_global = 0.0179) and has exceptionally coherent STRING relationships with PDCD11, TBL3, UTP15, UTP4, and EXOSC1. It is a conserved nucleolar RNA-associated protein that binds primary pre-rRNA transcripts and contributes to small-subunit rRNA maturation. HPA places it in the nucleolus and detects it in both colon and skin. Its annotations and literature support a direct role in the biological process rather than an indirect correlation.
- **Conclusion**: Established conclusion: NOL6 is a core nucleolar rRNA-processing component and a reliable indicator that the module represents a real ribosome-biogenesis program. Hypothesis: NOL6 may help couple pre-rRNA handling to the broader co-abundance state, but no module-specific regulatory direction can be inferred.

#### DDX21

- **Related proteins** (co-abundance neighbors): NOL6 (0.81), EPHB6 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 contributes to the globally corrected rRNA and RNA-processing terms (GO:BP rRNA metabolic process; q_global = 0.000247), (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.000877), (GO:CC nucleolus; q_global = 0.000973), (GO:BP rRNA processing; q_global = 0.00104), (GO:BP ribosome biogenesis; q_global = 0.00623), and (GO:BP RNA processing; q_global = 0.00726). It is a DEAD-box RNA helicase localized at the nucleolar rim and is detected in both colon and skin. Its established molecular class supports RNA remodeling during ribosome and RNA-complex assembly, while its literature is substantial and includes colorectal carcinoma and other cancer-related associations. Although its direct STRING partner list is absent in the supplied record, it connects in the co-abundance graph to NOL6 and EPHB6.
- **Conclusion**: Established conclusion: DDX21 provides an RNA-remodeling function compatible with the module's nucleolar interpretation. Hypothesis: DDX21 could be a regulatory interface between rRNA processing and cell-state transcriptional programs, but the available network evidence is insufficient to establish that role here.

#### EPHB6

- **Related proteins** (co-abundance neighbors): RFX1 (0.91), COPB1 (0.91), TCEA1 (0.88), GFPT1 (0.86), RDX (0.85), SMARCA4 (0.85), ACACA (0.85), PDCD11 (0.84), UTP15 (0.84), CHD1 (0.84), TTI1 (0.83), SMN1; SMN2 (0.83), GNAI3 (0.82), C5orf22 (0.82), EXOSC1 (0.82), TBL3 (0.81), ZC3H14 (0.80), THUMPD1 (0.80), DDX21 (0.80), XAB2 (0.80), NOL9 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EPH receptor B6. This gene encodes a member of a family of transmembrane proteins that function as receptors for ephrin-B family proteins. Unlike other members of this family, the encoded protein does not contain a functional kinase domain. Activity of this protein can influence cell adhesion and migration. Expression of this gene is downregulated during tumor progression, suggesting that the protein may suppress …
- **Diseases (Open Targets)**: myoepithelial tumor (0.111); neoplasm (0.106); triple-negative breast carcinoma (0.101); non-syndromic male infertility due to sperm motility disorder (0.081); autism (0.081)
- **Europe PMC papers**: 2774
- **Why important**: EPHB6 is the dominant structural connector in the supplied co-abundance graph, linking many otherwise weakly connected module members. It encodes a kinase-deficient ephrin receptor whose established functions include effects on cell adhesion and migration. HPA reports tissue enhancement in skin and cell-type enhancement in basal keratinocytes, among other cell types, making it relevant to the colon-skin context. It has substantial literature and cancer-related associations, but it is absent from the supplied STRING partner and hu.MAP records and does not occur in the globally corrected GO terms.
- **Conclusion**: Established conclusion: EPHB6 is an important co-abundance connector and a plausible epithelial cell-state marker, not an established component of the nucleolar machinery. Hypothesis: EPHB6 may link epithelial adhesion or differentiation state to ribosome-biogenesis demand, but this proposed bridge requires independent validation and may instead reflect coordinated expression without physical or regulatory interaction.

## Module 3

**Tissue pair**: colon and skin  
**Genes (18)**: PGM3, CAPN2, CHD4, CYFIP1, POLE, EIF3L, HELLS, MED23, MSH2, MSH6, NRDC, NUP93, PSMG1, RRM1, SRP72, SRRT, TCERG1, TLCD1

### Function

The strongest interpretation is a DNA replication surveillance and repair module centered on the MutSalpha mismatch-repair complex. (GO:MF single thymine insertion binding; q_global = 0.0358) identifies single thymine insertion binding through MSH2 and MSH6, while (GO:CC MutSalpha complex; q_global = 0.0358) identifies the MutSalpha complex through the same gene pair. These are the only GO/KEGG terms passing global correction and therefore provide the primary functional evidence. The known STRING links among MSH2, MSH6, and POLE support coordination between mismatch recognition and DNA replication or repair. Additional module genes suggest connected regulatory processes involving chromatin remodeling, DNA methylation, transcription, RNA processing, translation, proteasome assembly, membrane organization, and lipid homeostasis, but these are contextual annotations rather than globally enriched module functions. The STRING endometrial-cancer signal (STRING DISEASES Endometrial cancer; within-query FDR = 0.0143) is supplementary and is consistent with the presence of DNA-repair and cancer-associated genes, but it is not global enrichment evidence.

**Cell composition.** The module contains no secreted genes, so it does not resemble a plasma-protein or secreted-protein module. Most genes have low tissue specificity, and protein detection is generally present in both colon and skin, supporting a broadly shared cellular program rather than a tissue-exclusive program. Several genes have enhanced expression in particular cell types, with recurring signals in erythrocyte progenitors and additional signals in germ-cell, megakaryocyte, myeloid, microglial, bone-marrow, lymphoid, and skeletal-muscle contexts. This pattern does not establish blood contamination, especially because immune-cell specificity is generally low, but it raises the possibility that shared cell populations, progenitor-like states, or sample composition contribute to the conserved co-abundance pattern. The module is therefore not best described as a simple housekeeping module, although its broad tissue distribution and multiple basic nuclear and metabolic functions indicate a substantial ubiquitous-cellular component.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF single thymine insertion binding | 0.0358 | MSH2, MSH6 |
| GO:CC MutSalpha complex | 0.0358 | MSH2, MSH6 |

### STRING and hu.MAP

The most informative known relationships are MSH2 with MSH6, MSH2 with POLE, and MSH6 with POLE, forming a coherent DNA mismatch-repair and replication-associated neighborhood. STRING also supports SRRT with TCERG1 and CHD4 with SRRT, providing a smaller RNA-processing and chromatin-regulatory chain. The remaining co-abundance relationships do not have corresponding high-confidence STRING support in the supplied results. hu.MAP provides partial complex support rather than a complete module explanation: (hu.MAP huMAP3_10240.1) connects MSH6 with PGM3 in a larger complex, and (hu.MAP huMAP3_09042.1) connects MSH6 with NUP93 in a larger complex. These observations indicate that part of the module recapitulates established molecular relationships, especially the MSH2–MSH6–POLE core, while much of the module may reflect coordinated abundance, indirect regulation, shared cell state, or technical and biological context rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 5 of 153 gene pairs: CHD4–SRRT (0.76); MSH2–MSH6 (0.999); MSH2–POLE (0.947); MSH6–POLE (0.957); SRRT–TCERG1 (0.839)
**STRING functional enrichment (supplementary, within-query FDR)**: DISEASES Endometrial cancer (FDR = 0.0143, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10240.1 (PGM3, MSH6; 2/12); huMAP3_09042.1 (MSH6, NUP93; 2/26)

### Novelty

The module as a whole should not be claimed as a newly discovered molecular complex. Its central MSH2–MSH6 mismatch-repair relationship and the links to POLE are already established by STRING, and partial relationships are represented in hu.MAP. At the same time, the complete colon–skin co-abundance pattern, including TLCD1 as the principal network hub and the peripheral combination of membrane, nuclear, chromatin, RNA, and metabolic genes, is not explained by the supplied interaction resources. This makes the conserved co-abundance module potentially novel as a cross-tissue systems-level pattern, but not proof of a new biochemical pathway or complex. Absence of additional STRING or hu.MAP relationships cannot by itself establish novelty; independent replication, control for cell composition, and testing in matched colon and skin datasets would be needed.

**Hypothesis.** Hypothesis: the module reflects a conserved proliferative or stress-responsive cellular state in which mismatch surveillance and replication-associated repair are coordinated with chromatin regulation, transcriptional processing, and membrane or metabolic remodeling. MSH2 and MSH6 may define the repair-recognition core, with POLE representing replication-coupled DNA synthesis and repair. HELLS and CHD4 could contribute chromatin accessibility or methylation-dependent regulation, while SRRT and TCERG1 could couple the state to RNA processing and transcription. TLCD1 may act as a co-abundance hub associated with membrane lipid organization rather than as a demonstrated physical connector. An alternative hypothesis is that the pattern partly reflects shared progenitor or proliferative cell populations across the sampled tissues. These mechanisms are hypotheses and are not directly established by the enrichment or interaction evidence.

### Important genes

#### MSH6

- **Related proteins** (co-abundance neighbors): TLCD1 (0.85), MSH2 (0.85), HELLS (0.80); STRING partners: MSH2 (0.999), POLE (0.957)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus, Vesicles; IHC detected in colon, skin
- **hu.MAP 3.0**: huMAP3_10240.1, huMAP3_09042.1
- **Function (MyGene.info)**: mutS homolog 6. This gene encodes a member of the DNA mismatch repair MutS family. In E. coli, the MutS protein helps in the recognition of mismatched nucleotides prior to their repair. A highly conserved region of approximately 150 aa, called the Walker-A adenine nucleotide binding motif, exists in MutS homologs. The encoded protein heterodimerizes with MSH2 to form a mismatch recognition complex that functions …
- **Diseases (Open Targets)**: Lynch syndrome (0.878); colorectal cancer (0.832); endometrial cancer (0.819); mismatch repair cancer syndrome (0.799); mismatch repair cancer syndrome 1 (0.737)
- **Europe PMC papers**: 17901
- **Why important**: MSH6 is a core member of both globally significant terms, (GO:MF single thymine insertion binding; q_global = 0.0358) and (GO:CC MutSalpha complex; q_global = 0.0358), and is directly linked in STRING to MSH2 and POLE. Its annotation establishes a role in mismatch repair, DNA repair, chromatin organization, and spermatogenesis. It also has strong disease associations with Lynch syndrome, colorectal cancer, endometrial cancer, and mismatch-repair cancer syndromes, together with extensive literature.
- **Conclusion**: Established evidence supports MSH6 as a central mismatch-recognition component and a biologically meaningful anchor of the module. Its role as a driver of the entire co-abundance pattern, or as a direct regulator of the non-repair genes, remains hypothetical.

#### MSH2

- **Related proteins** (co-abundance neighbors): MSH6 (0.85); STRING partners: MSH6 (0.999), POLE (0.947)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutS homolog 2. This locus is frequently mutated in hereditary nonpolyposis colon cancer (HNPCC). When cloned, it was discovered to be a human homolog of the E. coli mismatch repair gene mutS, consistent with the characteristic alterations in microsatellite sequences (RER+ phenotype) found in HNPCC. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: Lynch syndrome (0.891); colorectal cancer (0.776); mismatch repair cancer syndrome (0.775); Muir-Torre syndrome (0.752); mismatch repair cancer syndrome 1 (0.740)
- **Europe PMC papers**: 22581
- **Why important**: MSH2 is the partner of MSH6 in both globally significant terms, (GO:MF single thymine insertion binding; q_global = 0.0358) and (GO:CC MutSalpha complex; q_global = 0.0358), and has established STRING relationships with MSH6 and POLE. Its annotation describes mismatch repair and DNA damage tolerance, and it is strongly associated with Lynch syndrome, colorectal cancer, Muir-Torre syndrome, and mismatch-repair cancer syndromes. It has extensive literature and is particularly relevant to the colon component of the tissue pair.
- **Conclusion**: Established evidence identifies MSH2 as a core functional member of the module and supports a mismatch-repair interpretation. The conserved co-abundance of MSH2 with the broader module does not demonstrate that MSH2 mechanistically coordinates every peripheral gene.

#### POLE

- **Related proteins** (co-abundance neighbors): MED23 (0.80), HELLS (0.80); STRING partners: MSH2 (0.947), MSH6 (0.957)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA polymerase epsilon, catalytic subunit. This gene encodes the catalytic subunit of DNA polymerase epsilon. The enzyme is involved in DNA repair and chromosomal DNA replication. Mutations in this gene have been associated with colorectal cancer 12 and facial dysmorphism, immunodeficiency, livedo, and short stature. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal cancer, susceptibility to, 12 (0.739); intrauterine growth retardation, metaphyseal dysplasia, adrenal hypoplasia congenita, genital anomalies, and immunodeficiency (0.735); facial dysmorphism-immunodeficiency-livedo-short stature syndrome (0.732); non-small cell lung carcinoma (0.668); B-cell chronic lymphocytic leukemia (0.660)
- **Europe PMC papers**: 71098
- **Why important**: POLE connects to both MSH2 and MSH6 in STRING and encodes the catalytic subunit of DNA polymerase epsilon, which participates in chromosomal DNA replication and repair. It has a strong literature base and disease associations including colorectal-cancer susceptibility and inherited immunodeficiency-related syndromes. Its tissue enhancement in bone marrow and cell-type enhancement in progenitor populations also makes it relevant to the possibility of a proliferative or progenitor-associated module state.
- **Conclusion**: Established evidence supports POLE as the replication and repair counterpart of the MSH2–MSH6 recognition pair. The proposition that POLE-driven replication activity explains the entire colon–skin conservation is a hypothesis requiring cell-cycle and cell-composition controls.

#### TLCD1

- **Related proteins** (co-abundance neighbors): NUP93 (0.92), RRM1 (0.90), EIF3L (0.88), MSH6 (0.85), PSMG1 (0.85), CAPN2 (0.84), PGM3 (0.83), SRP72 (0.81), CYFIP1 (0.81), NRDC (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TLC domain containing 1. Involved in several processes, including membrane assembly; phospholipid homeostasis; and regulation of membrane lipid distribution. Located in plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: cancer (0.082); neoplasm (0.067); liver cancer (0.057); gout (0.045); metabolic dysfunction-associated steatohepatitis (0.041)
- **Europe PMC papers**: 134
- **Why important**: TLCD1 is the principal network hub by weighted connectivity and links genes from several functional areas, including MSH6, NUP93, RRM1, EIF3L, PSMG1, CAPN2, PGM3, and SRP72. Its annotation supports roles in membrane assembly, phospholipid homeostasis, and membrane-lipid distribution. It is detected in both colon and skin and has substantial literature, although it has no supplied STRING partners, no hu.MAP assignment, and no enriched-term membership.
- **Conclusion**: Established evidence supports TLCD1 as a prominent co-abundance hub associated with membrane-lipid biology. Its possible role as a coordinator linking membrane state to DNA repair or proliferation is a hypothesis, not an established molecular interaction.

#### CHD4

- **Related proteins** (co-abundance neighbors): SRRT (0.82); STRING partners: SRRT (0.76)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromodomain helicase DNA binding protein 4. The product of this gene belongs to the SNF2/RAD54 helicase family. It represents the main component of the nucleosome remodeling and deacetylase complex and plays an important role in epigenetic transcriptional repression. Patients with dermatomyositis develop antibodies against this protein. Somatic mutations in this gene are associated with serous endometrial tumors. Alternative splicing result…
- **Diseases (Open Targets)**: Sifrim-Hitz-Weiss syndrome (0.810); neurodegenerative disease (0.551); hereditary disease (0.505); endometrial cancer (0.470); uterine carcinosarcoma (0.439)
- **Europe PMC papers**: 3617
- **Why important**: CHD4 provides a chromatin-regulatory connection through its STRING relationship with SRRT and is annotated as a principal component of the nucleosome remodeling and deacetylase complex. Its functions include chromatin remodeling, transcriptional repression, and double-strand-break repair. It is associated with endometrial cancer and other disease contexts and has substantial literature, making it relevant to the repair, epigenetic, and cancer-related interpretation.
- **Conclusion**: Established evidence supports CHD4 as a chromatin and DNA-repair regulator that could contextualize the MSH2–MSH6–POLE core. A direct CHD4-mediated mechanism for the complete module is not demonstrated by the supplied network evidence.

#### HELLS

- **Related proteins** (co-abundance neighbors): POLE (0.80), MSH6 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: helicase, lymphoid specific. This gene encodes a lymphoid-specific helicase. Other helicases function in processes involving DNA strand separation, including replication, repair, recombination, and transcription. This protein is thought to be involved with cellular proliferation and may play a role in leukemogenesis. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSe…
- **Diseases (Open Targets)**: immunodeficiency-centromeric instability-facial anomalies syndrome (0.724); neurodegenerative disease (0.319); hereditary disease (0.195); hepatocellular carcinoma (0.102); cancer (0.102)
- **Europe PMC papers**: 1652
- **Why important**: HELLS is connected within the module to POLE and MSH6 and is annotated for DNA double-strand-break repair, DNA methylation-dependent heterochromatin formation, and regulation of gene expression. It is enhanced in lymphoid and several progenitor or germ-cell populations, which is relevant to the possible proliferative or cell-state component of the module. Its disease associations include immunodeficiency-centromeric instability-facial anomalies syndrome and cancer, with a substantial literature base.
- **Conclusion**: Established evidence supports HELLS as a plausible chromatin and genome-stability component associated with the repair-centered module. Its apparent bridging role between MSH6 and POLE is based on co-abundance topology rather than supplied STRING or hu.MAP evidence, so causal coordination remains hypothetical.

## Module 4

**Tissue pair**: colon and skin  
**Genes (32)**: AGO2, ANAPC1, CDC73, CDCA5, DNAAF5, DLGAP5, DPH5, HMMR, HOMER1, KIFBP, KIF15, KIF22, KIF23, KIF2C, LLGL1, LUZP1, NUF2, PIK3R4, PLEKHM2, PKN1, PPM1B, RPAP1, POLR2B, POLR3G, SMG1, SWAP70, TRAPPC2L, TPX2, TTF2, UNC119B, UXT, ZNF638

### Function

The module is most strongly associated with mitotic chromosome segregation and microtubule-dependent cell division. Globally corrected GO evidence supports sister chromatid segregation (GO:BP sister chromatid segregation; q_global = 0.000993), spindle localization (GO:CC spindle; q_global = 0.00199), microtubule-based movement (GO:BP microtubule-based movement; q_global = 0.00226), mitotic chromosome segregation (GO:BP mitotic sister chromatid segregation; q_global = 0.00241), nuclear chromosome segregation (GO:BP nuclear chromosome segregation; q_global = 0.00252), microtubule binding (GO:MF microtubule binding; q_global = 0.00397), cell-cycle processes (GO:BP cell cycle process; q_global = 0.00684), mitotic nuclear division (GO:BP mitotic nuclear division; q_global = 0.00816), microtubule-cytoskeleton organization (GO:BP microtubule cytoskeleton organization; q_global = 0.0125), chromosome organization (GO:BP chromosome organization; q_global = 0.0138), tubulin binding (GO:MF tubulin binding; q_global = 0.0146), chromosome segregation (GO:BP chromosome segregation; q_global = 0.0153), microtubule-based processes (GO:BP microtubule-based process; q_global = 0.0155), organelle localization (GO:BP organelle localization; q_global = 0.0167), nuclear division (GO:BP nuclear division; q_global = 0.0256), microtubule motor activity (GO:MF microtubule motor activity; q_global = 0.0309), kinesin complex membership (GO:CC kinesin complex; q_global = 0.0422), and the cell cycle (GO:BP cell cycle; q_global = 0.0441). The coherent convergence of these terms, together with the concentration of kinesins, spindle-associated proteins, kinetochore components, and chromosome-segregation regulators, indicates a cell-division and mitotic-spindle module rather than a general housekeeping signal. The globally significant GO/KEGG terms are the primary enrichment evidence; STRING terms (STRING PMID (2021) Transcriptome-based stemness indices analysis reveals platinum-based chemo-theraputic response indicators in advanced-stage serous ovarian cancer.; within-query FDR = 0.0043) through (STRING Process Organelle localization; within-query FDR = 0.0278) provide concordant supplementary support but are not additional global enrichment claims.

**Cell composition.** The module is not composed of plasma or secreted proteins: HPA reports no secreted genes, and most proteins are intracellular. Many genes have low tissue specificity, but the tissue-enhanced pattern is prominent in bone marrow, lymphoid tissue, and testis, with additional enrichment in proliferative germ-cell and blood-cell populations. Immune-cell enhancement is also present, especially for T-reg-associated expression, although most genes have low immune-cell specificity. Protein detection is broadly concordant between colon and skin for most genes, but the absence of protein detection for some mitotic kinesins in one or both tissues cautions against interpreting the module as uniformly active in every cell. The shared colon-skin signal may therefore reflect proliferating epithelial or progenitor populations, and could also partly reflect shared hematopoietic or immune-cell content. It is unlikely to be explained by circulating secreted proteins.

**GO/KEGG enrichment**: 18 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP sister chromatid segregation | 0.000993 | ANAPC1, CDCA5, DLGAP5, KIF15, KIF22, KIF23, KIF2C, NUF2, TPX2 |
| GO:CC spindle | 0.00199 | DLGAP5, DNAAF5, HMMR, KIF15, KIF22, KIF23, KIF2C, LUZP1, TPX2, UXT |
| GO:BP microtubule-based movement | 0.00226 | DLGAP5, DNAAF5, KIF15, KIF22, KIF23, KIF2C, KIFBP, UXT |
| GO:BP mitotic sister chromatid segregation | 0.00241 | CDCA5, DLGAP5, KIF15, KIF22, KIF23, KIF2C, NUF2, TPX2 |
| GO:BP nuclear chromosome segregation | 0.00252 | ANAPC1, CDCA5, DLGAP5, KIF15, KIF22, KIF23, KIF2C, NUF2, TPX2 |
| GO:MF microtubule binding | 0.00397 | DLGAP5, KIF15, KIF22, KIF23, KIF2C, LUZP1, NUF2, UXT |
| GO:BP cell cycle process | 0.00684 | ANAPC1, CDC73, CDCA5, DLGAP5, KIF15, KIF22, KIF23, KIF2C, LLGL1, LUZP1, NUF2, PIK3R4, TPX2, UXT |
| GO:BP mitotic nuclear division | 0.00816 | CDCA5, DLGAP5, KIF15, KIF22, KIF23, KIF2C, NUF2, TPX2 |
| GO:BP microtubule cytoskeleton organization | 0.0125 | DLGAP5, DNAAF5, KIF15, KIF23, KIF2C, KIFBP, LLGL1, NUF2, TPX2, UXT |
| GO:BP chromosome organization | 0.0138 | ANAPC1, CDCA5, DLGAP5, KIF15, KIF22, KIF23, KIF2C, NUF2, SMG1, TPX2 |
| GO:MF tubulin binding | 0.0146 | DLGAP5, KIF15, KIF22, KIF23, KIF2C, LUZP1, NUF2, UXT |
| GO:BP chromosome segregation | 0.0153 | ANAPC1, CDCA5, DLGAP5, KIF15, KIF22, KIF23, KIF2C, NUF2, TPX2 |
| GO:BP microtubule-based process | 0.0155 | DLGAP5, DNAAF5, KIF15, KIF22, KIF23, KIF2C, KIFBP, LLGL1, NUF2, TPX2, UXT |
| GO:BP organelle localization | 0.0167 | CDCA5, DLGAP5, KIF22, KIF2C, KIFBP, LLGL1, NUF2, PLEKHM2, TRAPPC2L, UXT |
| GO:BP nuclear division | 0.0256 | CDCA5, DLGAP5, KIF15, KIF22, KIF23, KIF2C, NUF2, TPX2 |

### STRING and hu.MAP

STRING provides substantial support for a known mitotic-spindle core. DLGAP5, HMMR, KIF15, KIF23, KIF2C, NUF2, and TPX2 are connected by numerous high-confidence relationships, with CDCA5 and KIF22 contributing further links. These relationships agree with spindle organization, kinetochore attachment, spindle elongation, chromosome segregation, and kinesin motor biology described by (STRING NetworkNeighborAL Mixed, incl. Mitotic Spindle Checkpoint, and Mitotic sister chromatid segregation; within-query FDR = 0.008), (STRING NetworkNeighborAL Mixed, incl. Amplification of signal from the kinetochores, and Condensin complex; within-query FDR = 0.008), (STRING NetworkNeighborAL Mixed, incl. Spindle elongation, and Polo-like kinase mediated events; within-query FDR = 0.008), (STRING SMART Kinesin motor, catalytic domain. ATPase.; within-query FDR = 0.0087), (STRING NetworkNeighborAL Mixed, incl. Spindle elongation, and Outer kinetochore; within-query FDR = 0.0106), and (STRING NetworkNeighborAL Mixed, incl. Mitotic centrosome separation, and Nuclear microtubule; within-query FDR = 0.0123) through (STRING Process Organelle localization; within-query FDR = 0.0278). hu.MAP independently identifies KIFBP with KIF15 in several kinesin-related complexes (hu.MAP huMAP3_07678.1) through (hu.MAP huMAP3_04725.1). It also places POLR3G, RPAP1, and UXT in recurring RNA-polymerase-associated assemblies (hu.MAP huMAP3_11092.1) through (hu.MAP huMAP3_06426.1) and (hu.MAP huMAP3_00807.1), while POLR2B and CDC73 occur in transcription-related complexes (hu.MAP huMAP3_07454.1) through (hu.MAP huMAP3_09843.1). Thus, the module contains a strongly established mitotic machinery component plus a smaller transcriptional and trafficking-associated component. The co-abundance network extends beyond the relationships already represented in STRING and hu.MAP, but known interactions account for much of its central spindle-associated structure.

**STRING interactions (score >= 0.7)**: 35 of 496 gene pairs: CDC73–POLR2B (0.98); CDC73–TTF2 (0.746); CDCA5–DLGAP5 (0.921); CDCA5–HMMR (0.831); CDCA5–KIF23 (0.799); CDCA5–KIF2C (0.893); CDCA5–NUF2 (0.931); CDCA5–TPX2 (0.883); DLGAP5–HMMR (0.999); DLGAP5–KIF15 (0.937); DLGAP5–KIF23 (0.951); DLGAP5–KIF2C (0.975); DLGAP5–NUF2 (0.964); DLGAP5–TPX2 (0.978); HMMR–KIF15 (0.901); HMMR–KIF23 (0.889); HMMR–KIF2C (0.868); HMMR–NUF2 (0.886); HMMR–TPX2 (0.979); KIF15–KIF22 (0.718); KIF15–KIF23 (0.893); KIF15–KIF2C (0.945); KIF15–KIFBP (0.981); KIF15–NUF2 (0.936); KIF15–TPX2 (0.948); KIF22–KIF23 (0.745); KIF22–KIF2C (0.916); KIF22–TPX2 (0.749); KIF23–KIF2C (0.917); KIF23–NUF2 (0.912); KIF23–TPX2 (0.906); KIF2C–NUF2 (0.935); KIF2C–TPX2 (0.999); NUF2–TPX2 (0.947); POLR2B–RPAP1 (0.746)
**STRING functional enrichment (supplementary, within-query FDR)**: PMID (2021) Transcriptome-based stemness indices analysis reveals platinum-based chemo-theraputic response indicators in advanced-stage serous ovarian cancer. (FDR = 0.0043, 7 genes); NetworkNeighborAL Mixed, incl. Mitotic Spindle Checkpoint, and Mitotic sister chromatid segregation (FDR = 0.008, 7 genes); NetworkNeighborAL Mixed, incl. Amplification of signal from the kinetochores, and Condensin complex (FDR = 0.008, 6 genes); NetworkNeighborAL Mixed, incl. Spindle elongation, and Polo-like kinase mediated events (FDR = 0.008, 5 genes); SMART Kinesin motor, catalytic domain. ATPase. (FDR = 0.0087, 4 genes); NetworkNeighborAL Mixed, incl. Spindle elongation, and Outer kinetochore (FDR = 0.0106, 4 genes); PMID (2013) Intrinsic Disorder in the Kinesin Superfamily. (FDR = 0.0114, 7 genes); Process Microtubule-based process (FDR = 0.0123, 11 genes); NetworkNeighborAL Mixed, incl. Mitotic centrosome separation, and Nuclear microtubule (FDR = 0.0123, 3 genes); Process Microtubule-based movement (FDR = 0.0241, 7 genes); Process Microtubule cytoskeleton organization (FDR = 0.0248, 9 genes); Process Mitotic nuclear division (FDR = 0.0248, 7 genes); Process Mitotic sister chromatid segregation (FDR = 0.0278, 6 genes); Process Chromosome localization (FDR = 0.0278, 5 genes); Process Organelle localization (FDR = 0.0278, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11092.1 (POLR3G, POLR2B, CDC73, RPAP1, UXT; 5/65); huMAP3_14318.1 (POLR3G, POLR2B, RPAP1, UXT; 4/58); huMAP3_09057.1 (POLR3G, RPAP1, UXT; 3/36); huMAP3_08487.1 (POLR3G, RPAP1, UXT; 3/37); huMAP3_06426.1 (POLR3G, RPAP1, UXT; 3/38); huMAP3_07678.1 (KIFBP, KIF15; 2/4); huMAP3_14950.1 (KIFBP, KIF15; 2/4); huMAP3_06422.1 (KIFBP, KIF15; 2/5); huMAP3_06916.1 (KIFBP, KIF15; 2/5); huMAP3_04725.1 (KIFBP, KIF15; 2/8); huMAP3_07454.1 (POLR2B, CDC73; 2/27); huMAP3_07749.1 (POLR2B, CDC73; 2/28); huMAP3_09843.1 (POLR2B, CDC73; 2/29); huMAP3_00807.1 (POLR3G, UXT; 2/30)

### Novelty

The core biology is not a new discovery: the functions of the principal kinesins, spindle proteins, kinetochore components, and chromosome-segregation factors are already well established, and many of their relationships are represented in STRING. The module may nevertheless be a new tissue-pair co-abundance observation because it identifies a coordinated pattern conserved between colon and skin and links the mitotic core with genes involved in lysosome positioning, vesicle trafficking, transcription, and cytoskeletal organization. However, the available evidence does not establish that the complete module, its tissue conservation, or its cross-process organization is novel. Absence of a gene or relationship from STRING or hu.MAP would not by itself demonstrate novelty. The most defensible conclusion is that this is a potentially novel co-abundance configuration built largely from well-known mitotic biology.

**Hypothesis.** Hypothesis: the module reflects a shared proliferative-cell program in colon and skin in which spindle assembly, kinetochore attachment, chromosome movement, and cytokinesis are coordinated with intracellular trafficking and organelle positioning. DLGAP5, TPX2, HMMR, NUF2, KIF15, KIF23, and KIF2C could form the functional mitotic-spindle axis, while PLEKHM2, PIK3R4, TRAPPC2L, and UXT could connect that axis to lysosome, vesicle, centrosomal, and microtubule-associated organization. The HPA pattern raises an alternative or additional explanation in which shared proliferating immune or blood-cell populations contribute to the signal. This mechanism is a hypothesis from the integrated network and annotation evidence, not a demonstrated causal pathway.

### Important genes

#### DLGAP5

- **Related proteins** (co-abundance neighbors): POLR3G (0.88), KIF23 (0.85), ZNF638 (0.83), LLGL1 (0.82), POLR2B (0.82), KIFBP (0.82), LUZP1 (0.81), PKN1 (0.81), HMMR (0.81), NUF2 (0.80); STRING partners: CDCA5 (0.921), HMMR (0.999), KIF15 (0.937), KIF23 (0.951), KIF2C (0.975), NUF2 (0.964), TPX2 (0.978)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DLG associated protein 5. Predicted to enable microtubule binding activity. Predicted to be involved in several processes, including centrosome localization; kinetochore assembly; and mitotic spindle organization. Located in several cellular components, including centrosome; cytosol; and mitochondrion. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.485); placenta praevia (0.228); alcohol drinking (0.223); placental retention (0.151); male infertility (0.149)
- **Europe PMC papers**: 1514
- **Why important**: DLGAP5 is the strongest network hub among the mitotic genes in the listed subgraph and connects directly to KIF23, KIF2C, KIF15, NUF2, TPX2, HMMR, and CDCA5 in STRING. It appears across nearly all of the relevant globally corrected terms, including spindle, microtubule, chromosome-segregation, and cell-cycle categories (GO:BP sister chromatid segregation; q_global = 0.000993) through (GO:BP nuclear division; q_global = 0.0256) and (GO:BP cell cycle; q_global = 0.0441). Its annotation supports kinetochore assembly, spindle organization, chromosome movement, and mitotic-cell-cycle regulation. It also has substantial literature and disease links that include neurodegenerative disease and male infertility.
- **Conclusion**: Established evidence identifies DLGAP5 as a central spindle and chromosome-segregation component and as a major connector in the known STRING mitotic core. Its high co-abundance connectivity makes it an important module marker. The module does not establish that DLGAP5 drives the shared colon-skin signal or that its disease associations are relevant to these tissues.

#### NUF2

- **Related proteins** (co-abundance neighbors): KIF23 (0.86), KIF2C (0.83), KIF15 (0.83), SMG1 (0.81), DLGAP5 (0.80); STRING partners: CDCA5 (0.931), DLGAP5 (0.964), HMMR (0.886), KIF15 (0.936), KIF23 (0.912), KIF2C (0.935), TPX2 (0.947)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NUF2 component of NDC80 kinetochore complex. This gene encodes a protein that is highly similar to yeast Nuf2, a component of a conserved protein complex associated with the centromere. Yeast Nuf2 disappears from the centromere during meiotic prophase when centromeres lose their connection to the spindle pole body, and plays a regulatory role in chromosome segregation. The encoded protein is found to be associated with centromeres of mitotic…
- **Diseases (Open Targets)**: gout (0.458); irritable bowel syndrome (0.438); bipolar disorder (0.426); mathematical ability (0.401); prostate carcinoma (0.400)
- **Europe PMC papers**: 1971
- **Why important**: NUF2 is a component of the conserved NDC80 kinetochore complex and is annotated for spindle organization, chromosome segregation, spindle-checkpoint signaling, and attachment of spindle microtubules to kinetochores. It participates in the globally corrected segregation and microtubule terms (GO:BP sister chromatid segregation; q_global = 0.000993), (GO:BP mitotic sister chromatid segregation; q_global = 0.00241) through (GO:BP nuclear division; q_global = 0.0256), and (GO:BP cell cycle; q_global = 0.0441). It is connected in STRING to the major mitotic genes, including DLGAP5, KIF15, KIF23, KIF2C, TPX2, and CDCA5. Its HPA pattern is enriched in bone marrow, lymphoid tissue, testis, and several progenitor populations.
- **Conclusion**: Established evidence supports NUF2 as a kinetochore-centered indicator of active or abundant proliferative cell populations. Its presence strengthens the interpretation that the module represents coordinated chromosome-spindle function. The tissue-pair data alone cannot distinguish epithelial proliferation from contribution by blood or germ-cell-like populations.

#### KIF2C

- **Related proteins** (co-abundance neighbors): NUF2 (0.83), KIF23 (0.80), PLEKHM2 (0.80); STRING partners: CDCA5 (0.893), DLGAP5 (0.975), HMMR (0.868), KIF15 (0.945), KIF22 (0.916), KIF23 (0.917), NUF2 (0.935), TPX2 (0.999)
- **HPA**: Group enriched; Cell type enriched; blood Immune cell enhanced; location Nucleoplasm, Midbody, Centrosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 2C. This gene encodes a kinesin-like protein that functions as a microtubule-dependent molecular motor. The encoded protein can depolymerize microtubules at the plus end, thereby promoting mitotic chromosome segregation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.320); Abnormality of the skeletal system (0.165); placenta praevia (0.159); neuroendocrine neoplasm (0.159); placental retention (0.129)
- **Europe PMC papers**: 2214
- **Why important**: KIF2C has the broadest direct annotation coverage within the module, appearing in all globally corrected terms listed from (GO:BP sister chromatid segregation; q_global = 0.000993) through (GO:BP cell cycle; q_global = 0.0441). It is a microtubule-dependent motor that depolymerizes microtubules at their plus ends and promotes mitotic chromosome segregation, metaphase alignment, and microtubule polarity. It is strongly connected in STRING to DLGAP5, TPX2, NUF2, KIF15, KIF23, HMMR, CDCA5, and KIF22. It also has extensive literature and disease associations including neurodegenerative disease and neuroendocrine neoplasm.
- **Conclusion**: Established evidence makes KIF2C a strong functional representative of the module's mitotic-motor axis. Its network relationships and annotations support a role in chromosome alignment and microtubule turnover. The lack of HPA protein detection in colon and skin cautions that the co-abundance signal may arise from a restricted or low-abundance proliferative population rather than from the bulk tissue.

#### TPX2

- **Related proteins** (co-abundance neighbors): KIF22 (0.80), CDCA5 (0.80); STRING partners: CDCA5 (0.883), DLGAP5 (0.978), HMMR (0.979), KIF15 (0.948), KIF22 (0.749), KIF23 (0.906), KIF2C (0.999), NUF2 (0.947)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TPX2 microtubule nucleation factor. Enables importin-alpha family protein binding activity and protein kinase binding activity. Involved in activation of protein kinase activity; microtubule cytoskeleton organization; and negative regulation of microtubule depolymerization. Located in intercellular bridge; mitotic spindle; and nucleoplasm. Colocalizes with spindle pole. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.124); neoplasm (0.117); breast carcinoma (0.116); non-small cell lung carcinoma (0.112); breast cancer (0.110)
- **Europe PMC papers**: 4216
- **Why important**: TPX2 is a microtubule-nucleation and spindle-organization factor located in the mitotic spindle and nucleoplasm. It occurs in the globally corrected spindle, chromosome-segregation, microtubule, organelle-localization, and cell-cycle terms (GO:BP sister chromatid segregation; q_global = 0.000993), (GO:CC spindle; q_global = 0.00199), (GO:BP mitotic sister chromatid segregation; q_global = 0.00241), (GO:BP nuclear chromosome segregation; q_global = 0.00252), (GO:BP cell cycle process; q_global = 0.00684) through (GO:BP chromosome organization; q_global = 0.0138), (GO:BP chromosome segregation; q_global = 0.0153), (GO:BP microtubule-based process; q_global = 0.0155), (GO:BP nuclear division; q_global = 0.0256), and (GO:BP cell cycle; q_global = 0.0441). STRING places it in a dense, high-confidence network with DLGAP5, HMMR, KIF2C, KIF15, NUF2, KIF23, CDCA5, and KIF22. It has the largest literature volume among the selected genes and established cancer-related associations.
- **Conclusion**: Established evidence supports TPX2 as a key organizer of spindle microtubule nucleation and mitotic progression, making it a biologically important module component despite its limited direct degree in the co-abundance subgraph. Its enrichment in progenitor and lymphoid-associated HPA categories is consistent with a proliferative-cell explanation. A causal role in colon-skin conservation remains untested.

#### KIF23

- **Related proteins** (co-abundance neighbors): NUF2 (0.86), DLGAP5 (0.85), CDCA5 (0.82), KIF2C (0.80); STRING partners: CDCA5 (0.799), DLGAP5 (0.951), HMMR (0.889), KIF15 (0.893), KIF22 (0.745), KIF2C (0.917), NUF2 (0.912), TPX2 (0.906)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 23. The protein encoded by this gene is a member of kinesin-like protein family. This family includes microtubule-dependent molecular motors that transport organelles within cells and move chromosomes during cell division. This protein has been shown to cross-bridge antiparallel microtubules and drive microtubule movement in vitro. Alternate splicing of this gene results in multiple transcript variant…
- **Diseases (Open Targets)**: congenital dyserythropoietic anemia type 3 (0.735); hypertensive disorder (0.436); neurodegenerative disease (0.370); cardiovascular disorder (0.302); essential hypertension (0.302)
- **Europe PMC papers**: 2136
- **Why important**: KIF23 is a kinesin motor that cross-bridges antiparallel microtubules and contributes to spindle elongation, midzone assembly, cytokinesis, and microtubule-based movement. It appears in the globally corrected segregation, spindle, microtubule, motor, kinesin-complex, and cell-cycle terms (GO:BP sister chromatid segregation; q_global = 0.000993) through (GO:BP cell cycle; q_global = 0.0441). It is connected in STRING to DLGAP5, NUF2, KIF2C, TPX2, CDCA5, KIF15, KIF22, and HMMR. Its disease associations include congenital dyserythropoietic anemia and cardiovascular disorders, and it is detected by HPA in both colon and skin.
- **Conclusion**: Established evidence identifies KIF23 as a central motor linking spindle dynamics to the late stages of cell division, especially spindle midzone function and cytokinesis. Its detection in both tissues makes it a plausible shared-tissue marker. The module does not show whether KIF23 abundance is functionally active or merely reflects the abundance of dividing cells.

#### PLEKHM2

- **Related proteins** (co-abundance neighbors): PIK3R4 (0.89), ANAPC1 (0.86), DPH5 (0.85), PPM1B (0.84), CDC73 (0.84), SWAP70 (0.84), POLR2B (0.83), POLR3G (0.83), UNC119B (0.82), PKN1 (0.82), TRAPPC2L (0.81), RPAP1 (0.81), DNAAF5 (0.80), KIF2C (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pleckstrin homology and RUN domain containing M2. This gene encodes a protein that binds the plus-end directed microtubule motor protein kinesin, together with the lysosomal GTPase Arl8, and is required for lysosomes to distribute away from the microtubule-organizing center. The encoded protein belongs to the multisubunit BLOC-one-related complex that regulates lysosome positioning. It binds a Salmonella effector protein called Salmonella induced…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.388); dilated cardiomyopathy (0.194); autosomal recessive dilated cardiomyopathy (0.192); diabetes mellitus (0.172); aortic stenosis (0.166)
- **Europe PMC papers**: 280
- **Why important**: PLEKHM2 has the highest weighted network position in the listed co-abundance subgraph and connects the mitotic-associated portion with PIK3R4, ANAPC1, DPH5, PPM1B, CDC73, SWAP70, POLR2B, and POLR3G. It is annotated for lysosome positioning, protein localization, Golgi organization, and interaction with a plus-end-directed kinesin together with Arl8. It contributes to organelle localization (GO:BP organelle localization; q_global = 0.0167) and appears in the supplementary STRING organelle-localization category (STRING Process Organelle localization; within-query FDR = 0.0278), although it has no listed STRING partners or hu.MAP complex.
- **Conclusion**: Established evidence supports PLEKHM2 as a lysosome-positioning and intracellular-localization factor with a prominent co-abundance position. Its absence from the listed STRING and hu.MAP relationships means that its connection to the mitotic core is not independently established here. It is therefore an important candidate for the module's trafficking and organelle-positioning arm, but its proposed bridge to mitosis remains a hypothesis.

## Module 5

**Tissue pair**: colon and skin  
**Genes (49)**: AKAP17A, ARAP3, TP53BP2, BPTF, CBX8, CCDC137, CDK13, CSTF2T, DMAP1, EP400, GNL3L, HAUS4, HMG20B, IMP4, INTS9, ISY1, KAT7, KCTD3, MKI67, MED22, MED24, NAV1, NFXL1, NSL1, PRPF39, RBM22, UPF2, RFC1, POLR1G, RRAS2, SAP30BP, P3H4, SCOC, SETDB1, SMC5, SMARCA1, SMARCAD1, SPDL1, SPIN1, SUN1, TCP11L1, TAF4, TLK2, TOP2A, TRIM27, TTF1, UHRF2, UIMC1, ZNF346

### Function

The module is best interpreted as a conserved nuclear gene-regulatory and genome-maintenance program. The strongest primary evidence is for chromosome and nuclear organization, nuclear protein-containing complexes, chromatin organization, lysine modification, protein sumoylation, nucleic-acid binding, transcription, and RNA biosynthetic and metabolic processes (19 globally significant GO/KEGG terms, q_global 8.48e-06–0.0441; see the table). The breadth of the significant GO terms suggests coordinated activity across chromatin remodeling, transcriptional control, RNA processing, DNA replication or repair, and mitotic chromosome management rather than a narrowly specialized pathway. The presence of MKI67, TOP2A, NSL1, SPDL1, HAUS4, and RFC1 is consistent with a proliferative or cell-cycle-associated component, while SETDB1, SMARCA1, BPTF, KAT7, SMARCAD1, EP400, DMAP1, CBX8, and UHRF2 support chromatin regulation and epigenetic maintenance. No KEGG term is reported as having passed global correction.

**Cell composition.** This is not primarily a plasma or secreted-protein module: the HPA summary identifies only a single secreted gene, and nearly all genes have low tissue specificity. Protein detection is reported for most genes in both colon and skin, with many proteins localized to the nucleus, nucleoplasm, nuclear speckles, nucleoli, or chromatin-related compartments. The composition therefore resembles a broadly expressed housekeeping and nuclear regulatory program rather than a tissue-specific secretory program. Blood contamination is not the simplest explanation because most genes have low immune-cell specificity, although a minority show immune-cell enhancement or enrichment, including neutrophil-associated signals. The module may consequently reflect shared proliferative, progenitor, epithelial, or other common cell states present in both tissues, with a possible smaller contribution from immune-cell composition.

**GO/KEGG enrichment**: 19 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chromosome | 8.48e-06 | BPTF, CBX8, CCDC137, DMAP1, EP400, HMG20B, KAT7, MKI67, NFXL1, NSL1, P3H4, POLR1G, RFC1, SETDB1, SMARCA1, SMARCAD1, SMC5, SPDL1, SPIN1, SUN1, TAF4, TOP2A, UHRF2, UIMC1 |
| GO:CC nucleoplasm | 8.73e-05 | AKAP17A, BPTF, CBX8, CCDC137, CDK13, CSTF2T, DMAP1, EP400, GNL3L, HMG20B, IMP4, INTS9, ISY1, KAT7, MED22, MED24, MKI67, NSL1, POLR1G, RBM22, RFC1, SAP30BP, SCOC, SETDB1, SMARCA1, SMARCAD1, SMC5, SPIN1, TAF4, TLK2, TOP2A, TP53BP2, TRIM27, TTF1, UHRF2, UIMC1, ZNF346 |
| GO:CC nuclear lumen | 0.000246 | AKAP17A, BPTF, CBX8, CCDC137, CDK13, CSTF2T, DMAP1, EP400, GNL3L, HMG20B, IMP4, INTS9, ISY1, KAT7, MED22, MED24, MKI67, NSL1, P3H4, POLR1G, RBM22, RFC1, SAP30BP, SCOC, SETDB1, SMARCA1, SMARCAD1, SMC5, SPIN1, TAF4, TLK2, TOP2A, TP53BP2, TRIM27, TTF1, UHRF2, UIMC1, ZNF346 |
| GO:CC nuclear protein-containing complex | 0.000323 | AKAP17A, BPTF, CBX8, CDK13, CSTF2T, DMAP1, EP400, GNL3L, IMP4, INTS9, ISY1, KAT7, MED22, MED24, POLR1G, PRPF39, RBM22, SMARCA1, SUN1, TAF4, UIMC1, UPF2 |
| GO:BP chromatin organization | 0.000615 | BPTF, CBX8, DMAP1, EP400, HMG20B, KAT7, MKI67, SETDB1, SMARCA1, SMARCAD1, SMC5, SPIN1, TLK2, TOP2A, TRIM27, UHRF2, UIMC1 |
| GO:BP peptidyl-lysine modification | 0.00111 | GNL3L, HMG20B, KAT7, P3H4, SMC5, TRIM27, UHRF2 |
| GO:CC nucleus | 0.00115 | AKAP17A, BPTF, CBX8, CCDC137, CDK13, CSTF2T, DMAP1, EP400, GNL3L, HMG20B, IMP4, INTS9, ISY1, KAT7, MED22, MED24, MKI67, NFXL1, NSL1, P3H4, POLR1G, PRPF39, RBM22, RFC1, SAP30BP, SCOC, SETDB1, SMARCA1, SMARCAD1, SMC5, SPDL1, SPIN1, SUN1, TAF4, TLK2, TOP2A, TP53BP2, TRIM27, TTF1, UHRF2, UIMC1, UPF2, ZNF346 |
| GO:MF nucleic acid binding | 0.00116 | AKAP17A, BPTF, CBX8, CCDC137, CDK13, CSTF2T, EP400, GNL3L, HMG20B, IMP4, ISY1, KAT7, MKI67, NFXL1, POLR1G, PRPF39, RBM22, RFC1, SETDB1, SMARCA1, SMARCAD1, SMC5, TAF4, TOP2A, TRIM27, TTF1, UHRF2, UIMC1, UPF2, ZNF346 |
| GO:BP protein sumoylation | 0.00182 | GNL3L, HMG20B, SMC5, TRIM27, UHRF2 |
| GO:CC membraneless organelle | 0.00191 | AKAP17A, ARAP3, BPTF, CBX8, CCDC137, CDK13, DMAP1, EP400, GNL3L, HAUS4, HMG20B, IMP4, KAT7, MKI67, NAV1, NFXL1, NSL1, P3H4, POLR1G, RFC1, SAP30BP, SETDB1, SMARCA1, SMARCAD1, SMC5, SPDL1, SPIN1, SUN1, TAF4, TCP11L1, TLK2, TOP2A, TRIM27, TTF1, UHRF2, UIMC1, UPF2, ZNF346 |
| GO:CC intracellular membraneless organelle | 0.00191 | AKAP17A, ARAP3, BPTF, CBX8, CCDC137, CDK13, DMAP1, EP400, GNL3L, HAUS4, HMG20B, IMP4, KAT7, MKI67, NAV1, NFXL1, NSL1, P3H4, POLR1G, RFC1, SAP30BP, SETDB1, SMARCA1, SMARCAD1, SMC5, SPDL1, SPIN1, SUN1, TAF4, TCP11L1, TLK2, TOP2A, TRIM27, TTF1, UHRF2, UIMC1, UPF2, ZNF346 |
| GO:MF DNA binding | 0.00356 | BPTF, EP400, HMG20B, KAT7, MKI67, NFXL1, RFC1, SETDB1, SMARCA1, SMARCAD1, SMC5, TAF4, TOP2A, TRIM27, TTF1, UHRF2, UIMC1, UPF2 |
| GO:BP nucleic acid biosynthetic process | 0.0127 | AKAP17A, BPTF, CBX8, CDK13, CSTF2T, DMAP1, EP400, GNL3L, IMP4, INTS9, ISY1, KAT7, MED22, MED24, NFXL1, POLR1G, PRPF39, RBM22, RFC1, SAP30BP, SMARCA1, SMARCAD1, SPIN1, TAF4, TOP2A, TRIM27, TTF1, UIMC1 |
| GO:BP DNA-templated transcription | 0.0144 | AKAP17A, BPTF, CBX8, CDK13, DMAP1, EP400, INTS9, KAT7, MED22, MED24, NFXL1, POLR1G, RFC1, SAP30BP, SMARCA1, SMARCAD1, SPIN1, TAF4, TOP2A, TRIM27, TTF1, UIMC1 |
| GO:BP RNA biosynthetic process | 0.0192 | AKAP17A, BPTF, CBX8, CDK13, CSTF2T, DMAP1, EP400, IMP4, INTS9, ISY1, KAT7, MED22, MED24, NFXL1, POLR1G, PRPF39, RBM22, RFC1, SAP30BP, SMARCA1, SMARCAD1, SPIN1, TAF4, TOP2A, TRIM27, TTF1, UIMC1 |

### STRING and hu.MAP

STRING provides direct high-confidence support for several established relationships: SMARCA1 with BPTF, DMAP1 with EP400, ISY1 with RBM22, MED22 with MED24 and TAF4, MKI67 with TOP2A, GNL3L with IMP4, and SMC5 with TOP2A (15 supplementary STRING terms; within-query FDR 3.45e-07–0.00028). These links connect chromatin remodeling, transcriptional coactivation, spliceosome or RNA processing, nucleolar biology, and proliferation. The STRING enrichment results independently point to nuclear, chromosomal, chromatin-regulatory, and non-membrane-bounded compartments, but they are supplementary evidence rather than globally corrected module-level significance. hu.MAP further shows repeated partial membership of SMARCA1 with BPTF in chromatin-related complexes, EP400 with DMAP1 in EP400-associated complexes, RBM22 with ISY1 in spliceosomal complexes, MED22 with MED24 in Mediator, and NFXL1 with TCP11L1 in several reported complexes (hu.MAP huMAP3_15128.1) (hu.MAP huMAP3_00746.1) (hu.MAP huMAP3_08262.1) (hu.MAP huMAP3_00206.1) (hu.MAP huMAP3_07625.1) (hu.MAP huMAP3_09198.1) (hu.MAP huMAP3_14567.1) (hu.MAP huMAP3_06728.1) (hu.MAP huMAP3_07299.1) (hu.MAP huMAP3_08906.1) (hu.MAP huMAP3_06087.1) (hu.MAP huMAP3_15095.1) (hu.MAP huMAP3_03019.1) (hu.MAP huMAP3_07843.1) (hu.MAP huMAP3_09291.1) (hu.MAP huMAP3_09499.1) (hu.MAP huMAP3_02730.1) (hu.MAP huMAP3_09233.1) (hu.MAP huMAP3_10472.1) (hu.MAP huMAP3_06726.1) (hu.MAP huMAP3_10475.1) (hu.MAP huMAP3_10481.1) (hu.MAP huMAP3_10665.1) (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_13482.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_09945.1). These observations indicate that parts of the module recapitulate known molecular machinery. They do not demonstrate that all module genes form one physical complex or that the co-abundance edges are direct biochemical interactions.

**STRING interactions (score >= 0.7)**: 9 of 1176 gene pairs: BPTF–SMARCA1 (0.999); DMAP1–EP400 (0.999); GNL3L–IMP4 (0.81); ISY1–RBM22 (0.993); MED22–MED24 (0.997); MED22–TAF4 (0.826); MED24–TAF4 (0.807); MKI67–TOP2A (0.993); SMC5–TOP2A (0.706)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Nucleus (FDR = 3.45e-07, 41 genes); COMPARTMENTS Nuclear lumen (FDR = 4.42e-07, 28 genes); COMPARTMENTS Chromosome (FDR = 8.32e-07, 20 genes); Keyword Chromatin regulator (FDR = 4.36e-06, 12 genes); Keyword Nucleus (FDR = 9.94e-06, 37 genes); Process Chromosome organization (FDR = 1.18e-05, 20 genes); Component Chromosome (FDR = 4.59e-05, 21 genes); Component Nuclear protein-containing complex (FDR = 4.59e-05, 22 genes); Process Peptidyl-lysine modification (FDR = 6.26e-05, 11 genes); COMPARTMENTS Intracellular non-membrane-bounded organelle (FDR = 6.92e-05, 32 genes); Component Nucleus (FDR = 0.00011, 43 genes); Component Nuclear lumen (FDR = 0.00018, 36 genes); Component Nucleoplasm (FDR = 0.00021, 34 genes); Keyword Isopeptide bond (FDR = 0.00021, 22 genes); COMPARTMENTS Nucleoplasm (FDR = 0.00028, 18 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15128.1 (SMARCA1, BPTF, HMG20B; 3/96); huMAP3_00746.1 (SMARCA1, BPTF; 2/4); huMAP3_08262.1 (NFXL1, TCP11L1; 2/4); huMAP3_00206.1 (SMARCA1, BPTF; 2/5); huMAP3_07625.1 (NFXL1, TCP11L1; 2/5); huMAP3_09198.1 (SMARCA1, BPTF; 2/6); huMAP3_14567.1 (SMARCA1, BPTF; 2/8); huMAP3_06728.1 (SMARCA1, BPTF; 2/10); huMAP3_07299.1 (SMARCA1, BPTF; 2/12); huMAP3_08906.1 (SMARCA1, BPTF; 2/12); huMAP3_06087.1 (EP400, DMAP1; 2/14); huMAP3_15095.1 (SMARCA1, BPTF; 2/17); huMAP3_03019.1 (RBM22, ISY1; 2/20); huMAP3_07843.1 (EP400, DMAP1; 2/23); huMAP3_09291.1 (EP400, DMAP1; 2/27); huMAP3_09499.1 (SMARCA1, BPTF; 2/33); huMAP3_02730.1 (MED24, MED22; 2/34); huMAP3_09233.1 (NFXL1, TCP11L1; 2/34); huMAP3_10472.1 (SMARCA1, BPTF; 2/36); huMAP3_06726.1 (RBM22, ISY1; 2/37); huMAP3_10475.1 (NFXL1, TCP11L1; 2/39); huMAP3_10481.1 (EP400, DMAP1; 2/40); huMAP3_10665.1 (NFXL1, TCP11L1; 2/42); huMAP3_08501.1 (RBM22, ISY1; 2/47); huMAP3_13482.1 (SMARCA1, BPTF; 2/50); huMAP3_09504.1 (RBM22, ISY1; 2/51); huMAP3_14306.1 (EP400, DMAP1; 2/55); huMAP3_09945.1 (RBM22, ISY1; 2/61)

### Novelty

The broad biological interpretation is not a wholly new discovery: chromatin remodeling, transcription, RNA processing, DNA maintenance, and proliferation are established functions of several module genes, and multiple within-module relationships are already represented in STRING and hu.MAP. Nevertheless, the conserved co-abundance organization across colon and skin may represent a useful systems-level observation, especially because the module combines several nuclear processes and includes genes with sparse interaction or annotation coverage. Absence of a relationship from STRING or hu.MAP is not evidence of novelty, and the partial complex coverage argues against claiming a new physical complex. The defensible conclusion is that this is a potentially novel cross-tissue co-abundance pattern built largely from established nuclear biology. Replication in independent cohorts, adjustment for proliferation and cell-type composition, and perturbation or activity assays would be needed to establish biological novelty.

**Hypothesis.** Hypothesis: the module captures a shared proliferative nuclear state in colon and skin in which chromatin remodeling and histone modification are coordinated with transcription, RNA maturation, DNA replication or repair, and chromosome segregation. In this model, SMARCA1 and BPTF remodel chromatin, SETDB1, KAT7, SMARCAD1, and associated factors establish or interpret epigenetic states, EP400 and Mediator-related proteins support transcriptional output, spliceosomal factors support RNA processing, and TOP2A, MKI67, NSL1, and RFC1 reflect replication or mitotic demand. The observed co-abundance could therefore arise from a common cycling or regenerative cell state shared by both tissues rather than from a single stable complex. This is a testable hypothesis, not a demonstrated causal mechanism.

### Important genes

#### SETDB1

- **Related proteins** (co-abundance neighbors): RFC1 (0.86), CCDC137 (0.85), RRAS2 (0.85), TCP11L1 (0.83), ISY1 (0.83), MKI67 (0.82), NFXL1 (0.82), UHRF2 (0.82), TOP2A (0.82), POLR1G (0.81), IMP4 (0.81), SAP30BP (0.81), EP400 (0.80), SPIN1 (0.80), KAT7 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SET domain bifurcated histone lysine methyltransferase 1. This gene encodes a histone methyltransferase which regulates histone methylation, gene silencing, and transcriptional repression. This gene has been identified as a target for treatment in Huntington Disease, given that gene silencing and transcription dysfunction likely play a role in the disease pathogenesis. Alternatively spliced transcript variants of this gene have been described.[provided b…
- **Diseases (Open Targets)**: acute myeloid leukemia (0.251); hepatocellular carcinoma (0.238); B-cell chronic lymphocytic leukemia (0.229); head and neck squamous cell carcinoma (0.226); pleural mesothelioma (0.217)
- **Europe PMC papers**: 5377
- **Why important**: SETDB1 is among the most central genes in the module by weighted network position and connects to multiple module neighborhoods. It is a histone methyltransferase involved in gene silencing, heterochromatin organization, and transcriptional repression, and it appears across many primary chromosome, nucleus, chromatin, DNA-binding, and nucleic-acid terms (12 globally significant GO/KEGG terms, q_global 8.48e-06–0.00356; see the table). Its disease associations include several malignancies, and its literature is extensive.
- **Conclusion**: Established evidence supports SETDB1 as a major chromatin-state regulator and a plausible organizing hub for the module. It is reasonable to infer that SETDB1 contributes to the chromatin-regulatory signature. It is not established that SETDB1 drives the cross-tissue co-abundance pattern.

#### SMARCA1

- **Related proteins** (co-abundance neighbors): KCTD3 (0.85), TTF1 (0.82), UIMC1 (0.82), EP400 (0.81), NFXL1 (0.80), CDK13 (0.80), BPTF (0.80), UPF2 (0.80); STRING partners: BPTF (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_15128.1, huMAP3_00746.1, huMAP3_00206.1, huMAP3_09198.1, huMAP3_14567.1, huMAP3_06728.1, huMAP3_07299.1, huMAP3_08906.1, huMAP3_15095.1, huMAP3_09499.1, huMAP3_10472.1, huMAP3_13482.1
- **Function (MyGene.info)**: SNF2 related chromatin remodeling ATPase 1. This gene encodes a member of the SWI/SNF family of proteins. The encoded protein is an ATPase which is expressed in diverse tissues and contributes to the chromatin remodeling complex that is involved in transcription. The protein may also play a role in DNA damage, growth inhibition and apoptosis of cancer cells. Alternative splicing results in multiple transcript variants. [provided by RefSeq, …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.423); X-linked intellectual disability (0.401); non-syndromic X-linked intellectual disability (0.333); Abnormal brain morphology (0.266); cancer (0.211)
- **Europe PMC papers**: 924
- **Why important**: SMARCA1 has a prominent network position and is the module member with the clearest repeated support from both STRING and hu.MAP. It is a SWI/SNF-family ATPase involved in chromatin remodeling and transcription, appears in essentially all primary GO themes reported for the module (19 globally significant GO/KEGG terms, q_global 8.48e-06–0.0441; see the table), and recurs with BPTF across many hu.MAP complexes (hu.MAP huMAP3_15128.1), (hu.MAP huMAP3_00746.1), (hu.MAP huMAP3_00206.1), (hu.MAP huMAP3_09198.1) (hu.MAP huMAP3_14567.1) (hu.MAP huMAP3_06728.1) (hu.MAP huMAP3_07299.1) (hu.MAP huMAP3_08906.1), (hu.MAP huMAP3_15095.1), (hu.MAP huMAP3_09499.1), (hu.MAP huMAP3_10472.1), (hu.MAP huMAP3_13482.1). It also has substantial literature and disease associations involving neurodevelopment and cancer.
- **Conclusion**: Established evidence makes SMARCA1 a strong mechanistic anchor for the chromatin-remodeling component of the module. Its repeated complex membership supports known molecular context, but the co-abundance data alone do not show that every module gene is recruited by SMARCA1.

#### BPTF

- **Related proteins** (co-abundance neighbors): TOP2A (0.81), MKI67 (0.81), KCTD3 (0.80), SMARCA1 (0.80); STRING partners: SMARCA1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon, skin
- **hu.MAP 3.0**: huMAP3_15128.1, huMAP3_00746.1, huMAP3_00206.1, huMAP3_09198.1, huMAP3_14567.1, huMAP3_06728.1, huMAP3_07299.1, huMAP3_08906.1, huMAP3_15095.1, huMAP3_09499.1, huMAP3_10472.1, huMAP3_13482.1
- **Function (MyGene.info)**: bromodomain PHD finger transcription factor. This gene was identified by the reactivity of its encoded protein to a monoclonal antibody prepared against brain homogenates from patients with Alzheimer's disease. Analysis of the original protein (fetal Alz-50 reactive clone 1, or FAC1), identified as an 810 aa protein containing a DNA-binding domain and a zinc finger motif, suggested it might play a role in the regulation of transcription. Hig…
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and distal limb anomalies (0.788); Intellectual disability (0.539); hereditary disease (0.538); neurodegenerative disease (0.536); Global developmental delay (0.507)
- **Europe PMC papers**: 1741
- **Why important**: BPTF is a network-connected chromatin regulator and forms a very strong known STRING relationship with SMARCA1. It is included in the primary chromosome, nuclear-complex, chromatin, DNA-binding, transcription, and RNA-related terms (19 globally significant GO/KEGG terms, q_global 8.48e-06–0.0441; see the table), and it repeatedly co-occurs with SMARCA1 in hu.MAP complexes. BPTF has extensive literature and established links to neurodevelopmental disorders and developmental phenotypes.
- **Conclusion**: Established evidence supports BPTF as a complementary chromatin-remodeling component and as one of the best-supported known interaction pairs in the module. Its role as a cross-tissue module organizer remains a hypothesis.

#### KAT7

- **Related proteins** (co-abundance neighbors): SPIN1 (0.85), RBM22 (0.82), SMARCAD1 (0.80), SETDB1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lysine acetyltransferase 7. The protein encoded by this gene is part of the multimeric HBO1 complex, which possesses histone H4-specific acetyltransferase activity. This activity is required for functional replication origins and is involved in transcriptional activation of some genes. In both cases, the acetylation of histone H4 helps unfold chromatin so that the DNA can be accessed and replicated or transcribed. [provided …
- **Diseases (Open Targets)**: neurodegenerative disease (0.521); Alzheimer disease (0.372); autoimmune disorder of central nervous system (0.370); Parkinson disease (0.353); lysosomal storage disease (0.352)
- **Europe PMC papers**: 1247
- **Why important**: KAT7 is connected to several central module genes and is represented throughout the primary enrichment profile (19 globally significant GO/KEGG terms, q_global 8.48e-06–0.0441; see the table). It is a histone acetyltransferase component of the HBO1 complex, supports histone acetylation, replication-origin function, transcriptional activation, and regulation of DNA replication. It also has substantial literature and disease associations involving neurodegenerative and other neurological disorders.
- **Conclusion**: Established evidence identifies KAT7 as a plausible enzymatic link between chromatin modification, replication, and transcription in this module. The data support involvement of KAT7-related biology, but do not establish that its enzymatic activity is altered in either tissue.

#### TOP2A

- **Related proteins** (co-abundance neighbors): SETDB1 (0.82), BPTF (0.81), SUN1 (0.80); STRING partners: MKI67 (0.993), SMC5 (0.706)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA topoisomerase II alpha. This gene encodes a DNA topoisomerase, an enzyme that controls and alters the topologic states of DNA during transcription. This nuclear enzyme is involved in processes such as chromosome condensation, chromatid separation, and the relief of torsional stress that occurs during DNA transcription and replication. It catalyzes the transient breaking and rejoining of two strands of duplex DNA which al…
- **Diseases (Open Targets)**: neoplasm (0.618); breast cancer (0.616); acute myeloid leukemia (0.606); plasma cell myeloma (0.594); small cell lung carcinoma (0.580)
- **Europe PMC papers**: 11752
- **Why important**: TOP2A connects the module to DNA topology, chromosome condensation, chromatid separation, transcription, replication, and DNA damage responses. It has known STRING relationships with MKI67 and SMC5, appears across the primary chromosome, chromatin, DNA-binding, transcription, and nucleic-acid terms (19 globally significant GO/KEGG terms, q_global 8.48e-06–0.0441; see the table), and has very extensive literature and strong cancer associations. HPA describes tissue and cell-type enhancement in proliferative and progenitor-related populations.
- **Conclusion**: Established evidence supports TOP2A as a marker and functional participant of cell proliferation and chromosome management. Its presence strengthens the interpretation of a cycling or regenerative state, but it does not by itself distinguish active proliferation from shared cell-composition effects.

## Module 6

**Tissue pair**: colon and skin  
**Genes (7)**: AKAP11, BLOC1S3, GIGYF2, HEXIM2, PINX1, WRAP53, USP10

### Function

This is a small intracellular co-abundance module without a statistically supported GO or KEGG functional enrichment term, and without supplementary STRING enrichment. Its genes point to several related but not unified regulatory themes: ubiquitin-dependent protein regulation and DNA-damage responses through USP10; transcriptional elongation control through HEXIM2; telomere and Cajal-body biology through WRAP53 and PINX1; and organelle or melanosome-related trafficking through BLOC1S3. GIGYF2 additionally links the module to post-transcriptional regulation and translational control, while AKAP11 is a signaling-scaffold protein. The network therefore appears more consistent with a shared intracellular regulatory or cell-state program than with a single established biochemical pathway. No GO or KEGG term passed global correction.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and every member has protein detection in both colon and skin. Most genes have low tissue specificity, arguing against a module restricted to one tissue. Several members show reproductive-cell associations, especially spermatid or spermatocyte enrichment, and HEXIM2 is enhanced in skeletal muscle and testis and in several specialized cell types. USP10 is immune-cell enriched in neutrophils, while WRAP53 is immune-cell enhanced in basophils, but the module as a whole is not predominantly blood-cell specific. These findings make a shared intracellular program or shared cell-state contribution more plausible than a plasma-protein signal, although sample-cell composition could still contribute.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair in the module reaches the supplied STRING interaction threshold, and STRING provides no supplementary functional enrichment. Thus, the co-abundance edges should not be interpreted as established physical interactions. hu.MAP supplies the main prior complex evidence: USP10 and GIGYF2 co-occur as module members in complexes C1, C2, and C3, but each complex contains many additional proteins and only a minority of its members are in this module. This supports a possible connection to shared translation, RNA-associated, or protein-regulatory assemblies, but does not establish that all module genes form one complex. The remaining co-abundance relationships lack corresponding STRING or hu.MAP support in the supplied evidence.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10976.1 (USP10, GIGYF2; 2/12); huMAP3_14270.1 (USP10, GIGYF2; 2/47); huMAP3_14559.1 (USP10, GIGYF2; 2/47)

### Novelty

The module should not be claimed as a newly discovered biological complex or pathway. Its absence from STRING and the limited overlap with hu.MAP do not prove novelty, because co-abundance can capture condition, cell-state, localization, or indirect regulatory relationships that interaction databases do not record. The potentially interesting observation is the cross-tissue recurrence of a mixed intracellular pattern involving USP10, GIGYF2, HEXIM2, BLOC1S3, WRAP53, PINX1, and AKAP11 in colon and skin. However, there is no globally significant enrichment term and no direct interaction support linking all members. The appropriate novelty claim is therefore a candidate conserved co-abundance signature requiring replication and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a conserved intracellular stress, differentiation, or proliferative-state program in which ubiquitin and protein-stability control through USP10 is coordinated with translational regulation involving GIGYF2, transcriptional restraint involving HEXIM2, and nuclear genome-maintenance processes involving WRAP53 and PINX1. BLOC1S3 may represent a parallel organelle-trafficking or lysosome-related component, while AKAP11 may provide signaling-context dependence through PKA-associated scaffolding. The apparent reproductive-cell associations in HPA could indicate that the program is favored in highly specialized or differentiating cells, but they do not demonstrate that colon or skin samples contain germ cells. This hypothesis predicts that the module will track cellular state or composition more strongly than a single canonical pathway and should be tested with cell-resolved data, perturbation of USP10 or HEXIM2, and direct assays of RNA regulation, telomere biology, and organelle trafficking.

### Important genes

#### USP10

- **Related proteins** (co-abundance neighbors): WRAP53 (0.81), AKAP11 (0.81), PINX1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in colon, skin
- **hu.MAP 3.0**: huMAP3_10976.1, huMAP3_14270.1, huMAP3_14559.1
- **Function (MyGene.info)**: ubiquitin specific peptidase 10. Ubiquitin is a highly conserved protein that is covalently linked to other proteins to regulate their function and degradation. This gene encodes a member of the ubiquitin-specific protease family of cysteine proteases. The enzyme specifically cleaves ubiquitin from ubiquitin-conjugated protein substrates. The protein is found in the nucleus and cytoplasm. It functions as a co-factor of the DNA-bo…
- **Diseases (Open Targets)**: tricuspid valve disorder (0.254); Abnormality of the skeletal system (0.221); metabolic disease (0.207); alcohol drinking (0.198); neoplasm (0.117)
- **Europe PMC papers**: 2531
- **Why important**: USP10 is the most connected and strongest network member in the supplied subgraph, linking WRAP53, AKAP11, and PINX1. Established annotations place it in protein deubiquitination, regulation of protein stability, autophagy, DNA-damage response, and p53-related signaling. It is also the module member with neutrophil-enriched HPA evidence and has the largest literature volume among the selected genes. Its hu.MAP co-membership with GIGYF2 in C1, C2, and C3 makes it a useful anchor for interpreting the otherwise weakly connected module.
- **Conclusion**: Established evidence: USP10 is a plausible central regulator of protein stability and stress-responsive intracellular biology, and its network position makes it the strongest module anchor. Hypothesis: USP10 may coordinate the module by coupling ubiquitin-dependent regulation to nuclear maintenance and signaling processes. The co-abundance data do not establish that USP10 directly regulates the other module genes.

#### GIGYF2

- **Related proteins** (co-abundance neighbors): AKAP11 (0.86), HEXIM2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in colon, skin
- **hu.MAP 3.0**: huMAP3_10976.1, huMAP3_14270.1, huMAP3_14559.1
- **Function (MyGene.info)**: GRB10 interacting GYF protein 2. This gene contains CAG trinucleotide repeats and encodes a protein containing several stretches of polyglutamine residues. The encoded protein may be involved in the regulation of tyrosine kinase receptor signaling. This gene is located in a chromosomal region that was genetically linked to Parkinson disease type 11, and mutations in this gene were thought to be causative for this disease. However…
- **Diseases (Open Targets)**: neurodegenerative disease (0.528); Leber congenital amaurosis 16 (0.525); schizophrenia (0.397); Parkinson disease (0.390); snowflake vitreoretinal degeneration (0.375)
- **Europe PMC papers**: 832
- **Why important**: GIGYF2 is connected to AKAP11 and HEXIM2 and shares hu.MAP complex membership with USP10 in C1, C2, and C3. Its established annotations include negative regulation of translation and translational initiation, mRNA destabilization, post-transcriptional gene silencing, and regulation of insulin-like growth factor receptor signaling. HPA places it in a late-spermatid-enhanced cell context, while disease databases associate it with neurodegenerative and retinal disorders as well as reported Parkinson disease links of uncertain replication.
- **Conclusion**: Established evidence: GIGYF2 is a biologically credible post-transcriptional and translation-control component and is one of the two genes with repeated hu.MAP support. Hypothesis: it may connect protein-quality or signaling responses to selective translational repression within the module. The module does not prove a direct USP10–GIGYF2 functional interaction in colon or skin.

#### HEXIM2

- **Related proteins** (co-abundance neighbors): BLOC1S3 (0.82), GIGYF2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HEXIM P-TEFb complex subunit 2. This gene encodes a member of the HEXIM family of proteins. This protein is a component of the 7SK small nuclear ribonucleoprotein. This protein has been found to negatively regulate the kinase activity of the cyclin-dependent kinase P-TEFb, which phosphorylates multiple target proteins to promote transcriptional elongation. This gene is located approximately 7 kb downstream from related family me…
- **Diseases (Open Targets)**: neurodegenerative disease (0.240); aortic stenosis (0.229); intelligence (0.179); femur fracture (0.095); essential hypertension (0.071)
- **Europe PMC papers**: 256
- **Why important**: HEXIM2 connects GIGYF2 to BLOC1S3 and is the strongest tissue-context marker in the module, with HPA enhancement in skeletal muscle and testis and cell-type enhancement across cardiomyocytes, oocytes, spermatocytes, and spermatids. It is an established component of the seven-SK small nuclear ribonucleoprotein system and negatively regulates P-TEFb kinase activity, RNA polymerase transcriptional elongation, and cell-cycle progression. Its position may therefore connect translational regulation with transcriptional restraint.
- **Conclusion**: Established evidence: HEXIM2 is a transcriptional-elongation regulator with a specialized-cell expression pattern and a bridging position between GIGYF2 and BLOC1S3. Hypothesis: its presence may indicate a differentiation or controlled-proliferation state in which transcriptional output is actively restrained. The cross-tissue module does not establish that HEXIM2 is causally responsible for the observed co-abundance.

#### BLOC1S3

- **Related proteins** (co-abundance neighbors): HEXIM2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Golgi apparatus; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biogenesis of lysosomal organelles complex 1 subunit 3. This gene encodes a protein that is a component of the BLOC1 multi-subunit protein complex. This complex is necessary for the biogenesis of specialized organelles of the endosomal-lysosomal system, including platelet dense granules and melanosomes. Mutations in this gene cause Hermansky-Pudlak syndrome 8, a disease characterized by lysosomal storage defects, bleeding due to platelet storage pool d…
- **Diseases (Open Targets)**: Hermansky-Pudlak syndrome 8 (0.685); Hermansky-Pudlak syndrome (0.626); skin sensitivity to sun (0.445); Hermansky-Pudlak syndrome 7 (0.370); neurodegenerative disease (0.321)
- **Europe PMC papers**: 382
- **Why important**: BLOC1S3 is the endpoint connected to HEXIM2 and contributes a distinct organelle-trafficking interpretation. It is a component of the BLOC1 complex, which supports specialized endosomal-lysosomal organelles, platelet dense granules, and melanosomes. Its established disease association with Hermansky-Pudlak syndrome and its HPA enrichment in late spermatids make it informative for interpreting the module's cell-state and organelle component, despite its peripheral network position.
- **Conclusion**: Established evidence: BLOC1S3 supports lysosome-related organelle and pigment-organelle biology and is associated with Hermansky-Pudlak syndrome. Hypothesis: it may mark a trafficking or organelle-maturation aspect of the module rather than participate in the same nuclear regulatory process as USP10 or WRAP53. The available network evidence is insufficient to infer a direct connection beyond co-abundance with HEXIM2.

#### WRAP53

- **Related proteins** (co-abundance neighbors): USP10 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nuclear bodies; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat containing antisense to TP53. This gene encodes an essential component of the telomerase holoenzyme complex, a ribonucleoprotein complex required for telomere synthesis. This protein is enriched in Cajal bodies, nuclear sites of RNP processing that are important for telomerase function. It interacts with dyskerin, TERT and TERC, other components of active telomerase, and with small Cajal body RNAs (scaRNAs), which are involved…
- **Diseases (Open Targets)**: dyskeratosis congenita (0.778); neurodegenerative disease (0.550); hereditary neoplastic syndrome (0.466); acute myeloid leukemia with minimal differentiation (0.462); Alzheimer disease (0.444)
- **Europe PMC papers**: 847
- **Why important**: WRAP53 is connected to USP10 and represents the nuclear genome-maintenance arm of the module. Established annotations identify it as a telomerase-holoenzyme and Cajal-body component involved in telomere maintenance, RNA folding, and DNA-repair regulation, with disease associations including dyskeratosis congenita and hereditary neoplastic syndromes. Its HPA profile includes specialized ciliated and progenitor cell contexts and basophil enhancement, while its network link to USP10 places it beside the module's central regulatory gene.
- **Conclusion**: Established evidence: WRAP53 is a telomere, Cajal-body, and RNA-processing factor with substantial disease relevance. Hypothesis: its co-abundance with USP10 may reflect coordinated management of proteostasis and genome or RNP integrity during cellular stress or differentiation. No direct STRING or hu.MAP support was supplied for the WRAP53–USP10 relationship.

#### PINX1

- **Related proteins** (co-abundance neighbors): USP10 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PIN2 (TERF1) interacting telomerase inhibitor 1. Enables telomerase RNA binding activity and telomerase inhibitor activity. Involved in several processes, including negative regulation of DNA biosynthetic process; positive regulation of protein localization to nucleolus; and protein localization to organelle. Acts upstream of or within telomere maintenance via telomerase. Located in several cellular components, including chromosomal region; nucl…
- **Diseases (Open Targets)**: osteoarthritis (0.461); Increased blood pressure (0.398); osteoarthritis, hip (0.351); risk-taking behaviour (0.347); osteoarthritis, knee (0.346)
- **Europe PMC papers**: 610
- **Why important**: PINX1 is connected to USP10 and provides a second telomere-related interpretation. It has established telomerase-inhibitory and telomere-maintenance functions, as well as roles in nucleolar localization, chromosome alignment, cell-cycle control, protein stability, and regulation of ubiquitination. HPA associates it with early spermatids, primary spermatocytes, and late spermatids. Its combination of a direct link to the module hub and complementary telomere biology makes it useful for testing whether the module reflects nuclear maintenance.
- **Conclusion**: Established evidence: PINX1 is a telomere and cell-cycle regulator that is directly co-abundant with USP10 in this subgraph. Hypothesis: PINX1 and WRAP53 may jointly indicate a genome-maintenance state linked to proteostasis regulation. The data do not demonstrate a physical USP10–PINX1 complex or a unified telomere pathway for the entire module.

## Module 7

**Tissue pair**: colon and skin  
**Genes (31)**: ALDH1L2, ARGLU1, BAZ2A, BOP1, SDHC, CHAF1A, CIZ1, CIT, EHMT2, ESF1, MCM3AP, HERC2, KIF14, KIN, KMT2A, PRORP, NAA40, NCBP3, NKTR, NSD2, RBM19, POLR1A, POLR2A, RSF1, SCAF8, SNRNP27, SRBD1, WDR33, ZC3H13, ZFR, ZMYM4

### Function

The module is best interpreted as a conserved nuclear gene-expression and RNA-processing module, with a strong chromatin and ribosome-biogenesis component. The primary evidence is the global enrichment for nucleic acid binding (GO:MF nucleic acid binding; q_global = 0.00486), zinc ion binding (GO:MF zinc ion binding; q_global = 0.00706), nucleobase-containing compound metabolic process (GO:BP nucleobase-containing compound metabolic process; q_global = 0.0188), nucleoplasm (GO:CC nucleoplasm; q_global = 0.023), and transition metal ion binding (GO:MF transition metal ion binding; q_global = 0.0333). Its genes include chromatin regulators and histone-modifying proteins such as BAZ2A, EHMT2, KMT2A, NSD2, RSF1, and ZMYM4; transcriptional machinery such as POLR1A and POLR2A; RNA-processing factors such as ZC3H13, SCAF8, WDR33, NCBP3, SNRNP27, and ARGLU1; and nucleolar or ribosome-biogenesis factors such as BOP1, RBM19, and ESF1. Thus, the most defensible functional description is coordinated regulation of chromatin state, transcription, RNA maturation, and nucleolar RNA production. The STRING supplementary terms support nuclear localization, ubiquitin-related processes, zinc-associated domains, and nucleic-acid metabolism (15 supplementary STRING terms; within-query FDR 0.0023–0.0145), but they are not primary global enrichment evidence.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and the proteins detected in both colon and skin are predominantly nuclear or nucleoplasmic. Therefore, the shared signal is more consistent with a broadly expressed intracellular program than with a tissue-specific secretome. HPA does show enrichment for several progenitor or precursor cell populations, including erythrocyte progenitors, megakaryocyte progenitors, monocyte progenitors, and germ-cell populations, while immune-cell specificity is generally low and only a minority of genes are immune-cell enhanced. This raises a possible contribution from shared proliferative or progenitor-like cell states, but the available evidence does not establish that the module is caused by blood contamination or a particular shared cell type.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleic acid binding | 0.00486 | ARGLU1, BAZ2A, BOP1, CIZ1, EHMT2, ESF1, KIN, KMT2A, MCM3AP, NCBP3, NSD2, POLR1A, POLR2A, RBM19, SCAF8, SNRNP27, SRBD1, WDR33, ZC3H13, ZFR, ZMYM4 |
| GO:MF zinc ion binding | 0.00706 | BAZ2A, CIT, CIZ1, EHMT2, HERC2, KIN, KMT2A, NSD2, POLR1A, RSF1, ZC3H13, ZFR, ZMYM4 |
| GO:BP nucleobase-containing compound metabolic process | 0.0188 | ALDH1L2, ARGLU1, BAZ2A, BOP1, CHAF1A, CIZ1, EHMT2, ESF1, HERC2, KIN, KMT2A, NCBP3, NKTR, NSD2, POLR1A, POLR2A, PRORP, RSF1, SCAF8, SDHC, SNRNP27, SRBD1, WDR33, ZC3H13 |
| GO:CC nucleoplasm | 0.023 | ALDH1L2, ARGLU1, BAZ2A, BOP1, CIZ1, EHMT2, ESF1, HERC2, KIN, KMT2A, MCM3AP, NAA40, NCBP3, NSD2, POLR1A, POLR2A, PRORP, RBM19, RSF1, SCAF8, SNRNP27, WDR33, ZC3H13 |
| GO:MF transition metal ion binding | 0.0333 | BAZ2A, CIT, CIZ1, EHMT2, HERC2, KIN, KMT2A, NSD2, POLR1A, RSF1, ZC3H13, ZFR, ZMYM4 |

### STRING and hu.MAP

Only a limited subset of module relationships are high-confidence STRING interactions. Established examples include BOP1 with POLR1A and RBM19, POLR2A with SCAF8 and ZC3H13, SCAF8 with WDR33, ESF1 with POLR1A, and CIT with KIF14. These links support real connections among ribosome biogenesis, transcription, RNA processing, and cytokinesis-related machinery, but they do not explain the entire co-abundance module. hu.MAP provides additional complex-level support. CHAF1A, ZMYM4, EHMT2, and RSF1 occur together in a chromatin-associated complex (hu.MAP huMAP3_11539.1); NKTR, NCBP3, and ARGLU1 occur in RNA-processing complexes (hu.MAP huMAP3_09943.1); CHAF1A and RSF1 recur in chromatin-assembly complexes (hu.MAP huMAP3_11491.1) (hu.MAP huMAP3_12711.1); NKTR and NCBP3 recur in another RNA-processing complex (hu.MAP huMAP3_10789.1); POLR1A and POLR2A recur in polymerase-associated complexes (hu.MAP huMAP3_08487.1) (hu.MAP huMAP3_06426.1) (hu.MAP huMAP3_14318.1) (hu.MAP huMAP3_11092.1); and NKTR with ARGLU1 recur in additional RNA-processing complexes (hu.MAP huMAP3_09621.1) (hu.MAP huMAP3_11073.1). The combination of sparse direct STRING links and several partially overlapping hu.MAP complexes suggests a composite regulatory neighborhood rather than one single physical complex.

**STRING interactions (score >= 0.7)**: 7 of 465 gene pairs: BOP1–POLR1A (0.933); BOP1–RBM19 (0.914); CIT–KIF14 (0.97); ESF1–POLR1A (0.819); POLR2A–SCAF8 (0.897); POLR2A–ZC3H13 (0.996); SCAF8–WDR33 (0.769)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Nucleus (FDR = 0.0023, 24 genes); Keyword Ubl conjugation (FDR = 0.0032, 17 genes); Keyword Zinc (FDR = 0.0032, 13 genes); Keyword Isopeptide bond (FDR = 0.0032, 15 genes); Keyword Zinc-finger (FDR = 0.0043, 10 genes); Process Nucleobase-containing compound metabolic process (FDR = 0.0071, 21 genes); Process Cellular aromatic compound metabolic process (FDR = 0.0071, 22 genes); Process Heterocycle metabolic process (FDR = 0.0071, 22 genes); Process Nucleic acid metabolic process (FDR = 0.0071, 19 genes); Process Organic cyclic compound metabolic process (FDR = 0.0071, 22 genes); Component Nucleus (FDR = 0.0106, 28 genes); Component Nucleoplasm (FDR = 0.0106, 23 genes); SMART Cysteine-rich motif following a subset of SET domains (FDR = 0.0106, 3 genes); Process Cellular nitrogen compound metabolic process (FDR = 0.0114, 22 genes); SMART PHD zinc finger (FDR = 0.0145, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11539.1 (CHAF1A, ZMYM4, EHMT2, RSF1; 4/32); huMAP3_09943.1 (NKTR, NCBP3, ARGLU1; 3/78); huMAP3_11491.1 (CHAF1A, RSF1; 2/4); huMAP3_12711.1 (CHAF1A, RSF1; 2/35); huMAP3_10789.1 (NKTR, NCBP3; 2/37); huMAP3_08487.1 (POLR1A, POLR2A; 2/37); huMAP3_06426.1 (POLR1A, POLR2A; 2/38); huMAP3_09621.1 (NKTR, ARGLU1; 2/56); huMAP3_14318.1 (POLR1A, POLR2A; 2/58); huMAP3_11092.1 (POLR1A, POLR2A; 2/65); huMAP3_11073.1 (NKTR, ARGLU1; 2/67)

### Novelty

The module may represent a new tissue-pair co-abundance pattern, but the biological functions themselves are not new. Its genes map onto established chromatin, transcription, RNA-processing, nucleolar, and cell-cycle biology, and several subsets are supported by known STRING interactions and hu.MAP complexes. Conversely, the limited direct STRING connectivity means that the full thirty-one-gene co-abundance arrangement is not simply a previously catalogued protein complex. Absence from STRING or hu.MAP cannot establish novelty, because those resources emphasize curated or experimentally supported physical and functional relationships rather than tissue-pair co-abundance. The appropriate conclusion is that the conserved colon-skin co-abundance organization is potentially novel, while its component processes and many of its subassemblies are established.

**Hypothesis.** Hypothesis: the module reflects a shared proliferative and biosynthetic cell state in colon and skin in which chromatin remodeling and histone modification coordinate transcriptional output, RNA polymerase activity, RNA processing, and nucleolar ribosome production. BAZ2A, EHMT2, KMT2A, NSD2, RSF1, and related factors could establish or read chromatin states; POLR1A and POLR2A could couple those states to ribosomal and messenger-RNA transcription; and ZC3H13, SCAF8, WDR33, NCBP3, and other RNA factors could couple transcription to RNA maturation. The HPA precursor-cell signal makes a proliferative or progenitor-associated state plausible, but this remains a hypothesis because co-abundance does not demonstrate physical interaction, causal regulation, or a common cell of origin.

### Important genes

#### BAZ2A

- **Related proteins** (co-abundance neighbors): CIT (0.84), ZC3H13 (0.83), HERC2 (0.83), MCM3AP (0.83), CHAF1A (0.82), ZMYM4 (0.82), POLR1A (0.82), KMT2A (0.81), BOP1 (0.81), SCAF8 (0.81), SDHC (0.81), PRORP (0.81), POLR2A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: bromodomain adjacent to zinc finger domain 2A. Enables histone binding activity. Contributes to RNA polymerase I core promoter sequence-specific DNA binding activity. Predicted to be involved in DNA methylation; histone deacetylation; and negative regulation of macromolecule metabolic process. Predicted to act upstream of or within chromatin organization and histone modification. Located in cytosol and nuclear speck. [provided by Alliance of G…
- **Diseases (Open Targets)**: neurodegenerative disease (0.508); premature birth (0.347); hypothyroidism (0.176); posterior cortical atrophy (0.103); Graves disease (0.098)
- **Europe PMC papers**: 649
- **Why important**: BAZ2A is the strongest network hub in the supplied module and participates in every globally enriched GO term (5 globally significant GO/KEGG terms, q_global 0.00486–0.0333; see the table). It is a nuclear-speckle protein with histone-binding activity and reported roles in chromatin organization, histone modification, and RNA polymerase I regulation. It also connects in the module to chromatin, transcription, RNA, and cell-cycle-associated genes, while the STRING supplementary annotations repeatedly place it in the same nuclear and zinc-related themes (15 supplementary STRING terms; within-query FDR 0.0023–0.0145). Its substantial literature volume makes it a well-characterized anchor for interpreting the module.
- **Conclusion**: Established evidence supports BAZ2A as a central chromatin and transcription-related component of the module. Its hub position makes it a plausible organizer of the co-abundance pattern, but the network does not prove that BAZ2A causally regulates the other module genes.

#### CHAF1A

- **Related proteins** (co-abundance neighbors): POLR2A (0.88), KIF14 (0.84), MCM3AP (0.84), NAA40 (0.84), CIZ1 (0.83), RBM19 (0.83), BAZ2A (0.82), ZMYM4 (0.82), NCBP3 (0.82), ESF1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in colon, skin
- **hu.MAP 3.0**: huMAP3_11539.1, huMAP3_11491.1, huMAP3_12711.1
- **Function (MyGene.info)**: chromatin assembly factor 1 subunit A. Chromatin assembly factor I (CAF1) is a nuclear complex consisting of p50, p60 (CHAF1B; MIM 601245), and p150 (CHAF1A) subunits that assembles histone octamers onto replicating DNA in vitro (Kaufman et al., 1995 [PubMed 7600578]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: craniofacial microsomia (0.446); neurodegenerative disease (0.441); Abnormality of the skeletal system (0.116); neoplasm (0.105); gastric cancer (0.098)
- **Europe PMC papers**: 845
- **Why important**: CHAF1A has a prominent module position and is detected in both colon and skin. It is the large subunit of chromatin assembly factor, which assembles histone octamers onto replicating DNA, and its annotations include nucleosome assembly and replication-dependent chromatin assembly. It is present in several hu.MAP chromatin and histone-associated complexes (hu.MAP huMAP3_11539.1) (hu.MAP huMAP3_11491.1) (hu.MAP huMAP3_12711.1), providing complex-level support beyond co-abundance. HPA also shows enhancement in bone marrow and several progenitor populations, which is relevant to a possible proliferative-state interpretation.
- **Conclusion**: Established evidence identifies CHAF1A as a chromatin-assembly factor that links the module to DNA replication and nucleosome organization. Its progenitor-associated HPA pattern supports, but does not establish, a contribution from proliferating or precursor cells.

#### POLR2A

- **Related proteins** (co-abundance neighbors): CHAF1A (0.88), KIF14 (0.83), MCM3AP (0.80), BAZ2A (0.80); STRING partners: SCAF8 (0.897), ZC3H13 (0.996)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08487.1, huMAP3_06426.1, huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase II subunit A. This gene encodes the largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene contains a carboxy terminal domain composed of heptapeptide repeats that are essential for polymerase activity. These repeats contain serine and threonine residues that are phosphorylated in actively transcribing RNA polymerase. In addition, …
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and variable intellectual and behavioral abnormalities (0.738); HIV infectious disease (0.600); hereditary disease (0.479); syndromic intellectual disability (0.462); Orthomyxoviridae infectious disease (0.374)
- **Europe PMC papers**: 4546
- **Why important**: POLR2A encodes the largest subunit of RNA polymerase II and is the core transcriptional machinery representative in the module. It is included in the globally significant nucleic-acid-binding, nucleobase-metabolism, and nucleoplasm terms (GO:MF nucleic acid binding; q_global = 0.00486) (GO:BP nucleobase-containing compound metabolic process; q_global = 0.0188) (GO:CC nucleoplasm; q_global = 0.023). It has STRING links to SCAF8 and ZC3H13, connecting transcription to RNA elongation and RNA methylation-related machinery, and it recurs with polymerase-associated hu.MAP complexes (hu.MAP huMAP3_08487.1) (hu.MAP huMAP3_06426.1) (hu.MAP huMAP3_14318.1) (hu.MAP huMAP3_11092.1). It also has a substantial literature base and disease associations involving neurodevelopmental and hereditary disorders.
- **Conclusion**: Established evidence supports POLR2A as a transcriptional backbone of the module and as a bridge between chromatin-associated genes and RNA-processing genes. Its presence indicates transcriptional activity, but does not identify which transcripts or tissue-specific programs are involved.

#### EHMT2

- **Related proteins** (co-abundance neighbors): ZMYM4 (0.84), MCM3AP (0.81), NAA40 (0.81), NSD2 (0.80), NKTR (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm, Nuclear speckles; IHC detected in colon, skin
- **hu.MAP 3.0**: huMAP3_11539.1
- **Function (MyGene.info)**: euchromatic histone lysine methyltransferase 2. This gene encodes a methyltransferase that methylates lysine residues of histone H3. Methylation of H3 at lysine 9 by this protein results in recruitment of additional epigenetic regulators and repression of transcription. This gene was initially thought to be two different genes, NG36 and G9a, adjacent to each other in the HLA locus. Alternative splicing results in multiple transcript variants. […
- **Diseases (Open Targets)**: neurodegenerative disease (0.405); Kleefstra syndrome (0.192); neoplasm (0.118); hepatocellular carcinoma (0.115); breast cancer (0.113)
- **Europe PMC papers**: 3105
- **Why important**: EHMT2 is a histone lysine methyltransferase with extensive literature support and is included in every globally enriched GO term (5 globally significant GO/KEGG terms, q_global 0.00486–0.0333; see the table). Its reported functions include histone H3 lysine methylation, transcriptional repression, DNA methylation-dependent heterochromatin formation, and regulation of DNA replication. It is part of the hu.MAP chromatin-associated complex with CHAF1A, ZMYM4, and RSF1 (hu.MAP huMAP3_11539.1), and it connects within the module to other chromatin regulators and nuclear factors.
- **Conclusion**: Established evidence supports EHMT2 as an epigenetic regulator that gives the module a mechanistically meaningful chromatin-repression component. Its co-abundance with other chromatin factors is consistent with coordinated epigenetic control, but the data do not establish a specific target locus or direction of regulation.

#### ZC3H13

- **Related proteins** (co-abundance neighbors): MCM3AP (0.85), BAZ2A (0.83), ALDH1L2 (0.83), ZFR (0.80); STRING partners: POLR2A (0.996)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger CCCH-type containing 13. Enables RNA binding activity. Involved in mRNA methylation. Located in nuclear speck. Part of RNA N6-methyladenosine methyltransferase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); type 2 diabetes mellitus (0.332); liver disorder (0.332); renal dialysis (0.290); poisoning (0.213)
- **Europe PMC papers**: 2616
- **Why important**: ZC3H13 is a high-connectivity module member included in every globally enriched GO term (5 globally significant GO/KEGG terms, q_global 0.00486–0.0333; see the table). It is an RNA-binding factor involved in mRNA methylation and is part of an RNA N six methyladenosine methyltransferase complex. Its very strong STRING relationship with POLR2A and its links to several module genes connect RNA modification with transcriptional machinery. HPA places it in the nucleoplasm and shows colon and skin protein detection, while its broad tissue profile argues against a secreted or narrowly tissue-specific role.
- **Conclusion**: Established evidence supports ZC3H13 as an RNA-processing and RNA-modification component that may connect transcription to post-transcriptional regulation. The module is compatible with such coupling, but it does not prove that RNA methylation mediates the shared colon-skin co-abundance pattern.

## Module 8

**Tissue pair**: colon and skin  
**Genes (11)**: ANKZF1, BCAT1, INTS5, PEX5, PHAF1, PSMG4, RBPMS, SUOX, VPS37A, WDR62, XIAP

### Function

This is a heterogeneous, sparse co-abundance module rather than a clearly defined pathway module. Its genes span branched-chain amino-acid metabolism through BCAT1, RNA processing through RBPMS and INTS5, endosomal sorting and autophagy through VPS37A, peroxisomal import through PEX5, proteasome assembly through PSMG4, sulfur metabolism through SUOX, apoptosis and inflammatory signaling through XIAP, and cell-cycle or developmental functions through WDR62. The network therefore does not support a single established biochemical function. No GO/KEGG term passed global correction, and there were no supplementary STRING functional-enrichment terms. The most defensible interpretation is a shared expression or co-abundance state involving general cellular maintenance, protein and organelle homeostasis, RNA regulation, stress responses, and survival, rather than a demonstrated pathway.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins: none of its genes is annotated as secreted. Most genes have low tissue specificity and low immune-cell specificity, while a subset has enhanced expression in diverse tissues or cell types, including pancreas, liver, blood vessel, skeletal muscle, testis, hepatocytes, spermatids, and renal cell types. A small subset has immune-cell associations involving non-classical monocytes, plasmacytoid dendritic cells, or conventional dendritic cells, but the overall HPA profile does not indicate a strong blood-cell signature. Protein detection in both colon and skin for many members supports that the module is not simply an artifact of complete protein absence in either tissue. The scattered tissue and cell-type preferences instead suggest mixed cellular composition, shared housekeeping or stress-related expression, or a context-dependent co-abundance pattern.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair in the module meets the specified high-confidence STRING interaction threshold, and no STRING partners are reported for the individual genes. No hu.MAP complex contains multiple module members. Thus, the co-abundance links are not corroborated here by established high-confidence physical or functional interaction evidence. Known biology exists for individual genes, including ESCRT-I activity for VPS37A, peroxisomal import for PEX5, anti-apoptotic signaling for XIAP, RNA processing for RBPMS and INTS5, and proteasome assembly for PSMG4, but these annotations do not establish a shared molecular complex or pathway for the module.

**STRING interactions (score >= 0.7)**: 0 of 55 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a previously unreported tissue-pair co-abundance pattern, but it cannot be called a new biological mechanism on the present evidence. The absence of STRING and hu.MAP support argues against an already recognized physical module, yet absence from those resources alone does not prove novelty. The lack of globally significant GO/KEGG enrichment, the heterogeneous annotations, and the scattered HPA cell-type associations make a technical, cell-composition, or general cellular-state explanation plausible. A novelty claim would require independent validation in separate colon and skin cohorts, preservation of the gene-gene relationships, and testing against cell-type composition, batch, donor, and tissue-quality covariates.

**Hypothesis.** Hypothesis: the module reflects a shared cellular maintenance and stress state present in subsets of colon and skin samples. In this model, BCAT1-linked metabolic activity is co-regulated with RNA processing, proteasome and peroxisome maintenance, endosomal or autophagic trafficking, sulfur metabolism, and XIAP-mediated survival. The pattern could arise from coordinated adaptation to oxidative, proteotoxic, or inflammatory stress, or from a shared mixture of cell types rather than direct molecular cooperation among all members. This is a hypothesis only; the current module has no enrichment or interaction evidence sufficient to establish the mechanism.

### Important genes

#### BCAT1

- **Related proteins** (co-abundance neighbors): RBPMS (0.85), ANKZF1 (0.83), PEX5 (0.83), XIAP (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: branched chain amino acid transaminase 1. This gene encodes the cytosolic form of the enzyme branched-chain amino acid transaminase. This enzyme catalyzes the reversible transamination of branched-chain alpha-keto acids to branched-chain L-amino acids essential for cell growth. Two different clinical disorders have been attributed to a defect of branched-chain amino acid transamination: hypervalinemia and hyperleucine-isoleucinemia. As th…
- **Diseases (Open Targets)**: aortic stenosis (0.375); alcohol drinking (0.328); atrial fibrillation (0.315); type 1 diabetes mellitus (0.300); male reproductive system disorder (0.258)
- **Europe PMC papers**: 2600
- **Why important**: BCAT1 is the most connected and strongest-associated node in the module and links to RBPMS, ANKZF1, PEX5, and XIAP. Its established function in branched-chain amino-acid transamination provides a plausible metabolic anchor, while its annotations include amino-acid metabolism, cell-cycle transition, and oxidative-stress-relevant biology. It also has substantial literature and disease-association support compared with several less studied module members.
- **Conclusion**: Established: BCAT1 is a cytosolic branched-chain amino-acid enzyme and a central co-abundance node. Hypothesis: it may mark a metabolic component of the shared colon-skin state and could connect nutrient handling with survival or stress responses. The module does not establish that BCAT1 directly regulates the other genes.

#### VPS37A

- **Related proteins** (co-abundance neighbors): INTS5 (0.82), PHAF1 (0.81), WDR62 (0.80), RBPMS (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles, Centrosome, Acrosome, Flagellar centriole; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS37A subunit of ESCRT-I. This gene belongs to the VPS37 family, and encodes a component of the ESCRT-I (endosomal sorting complex required for transport I) protein complex, required for the sorting of ubiquitinated transmembrane proteins into internal vesicles of multivesicular bodies. Expression of this gene is downregulated in hepatocellular carcinoma, and mutations in this gene are associated with autosomal recessive s…
- **Diseases (Open Targets)**: hereditary spastic paraplegia 53 (0.578); HIV infectious disease (0.526); viral infectious disease (0.463); neurodegenerative disease (0.221); Paralysis (0.207)
- **Europe PMC papers**: 430
- **Why important**: VPS37A is among the most connected nodes and links INTS5, PHAF1, WDR62, and RBPMS. Its established role as an ESCRT-I component connects the module to ubiquitin-dependent membrane-protein sorting, multivesicular-body assembly, autophagy, and viral budding-related host machinery. It is detected in both colon and skin and has substantial disease relevance through hereditary spastic paraplegia.
- **Conclusion**: Established: VPS37A participates in endosomal sorting and membrane-trafficking machinery. Hypothesis: it may represent an organelle and membrane-quality-control arm of the module. There is no high-confidence interaction evidence showing that its co-abundance links are physical ESCRT interactions.

#### XIAP

- **Related proteins** (co-abundance neighbors): BCAT1 (0.83), SUOX (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: X-linked inhibitor of apoptosis. This gene encodes a protein that belongs to a family of apoptotic suppressor proteins. Members of this family share a conserved motif termed, baculovirus IAP repeat, which is necessary for their anti-apoptotic function. This protein functions through binding to tumor necrosis factor receptor-associated factors TRAF1 and TRAF2 and inhibits apoptosis induced by menadione, a potent inducer of free ra…
- **Diseases (Open Targets)**: X-linked lymphoproliferative syndrome (0.814); neurodegenerative disease (0.556); inflammatory bowel disease (0.478); hereditary disease (0.469); Splenomegaly (0.464)
- **Europe PMC papers**: 16708
- **Why important**: XIAP is a bridge between BCAT1 and SUOX and is the most extensively studied gene in the module by literature volume. Its established functions include inhibition of apoptosis, regulation of tumor-necrosis-factor signaling, DNA-damage responses, ubiquitination, and type-I interferon production. Its detection in both colon and skin and its inflammatory-bowel-disease association make it especially relevant to a shared tissue stress or survival state.
- **Conclusion**: Established: XIAP is an anti-apoptotic and inflammatory-signaling regulator. Hypothesis: XIAP may help explain why this module is preserved across tissues exposed to epithelial injury, oxidative stress, or inflammatory signaling. The co-abundance network does not prove that XIAP is causally driving the module.

#### PEX5

- **Related proteins** (co-abundance neighbors): BCAT1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peroxisomal biogenesis factor 5. The product of this gene binds to the C-terminal PTS1-type tripeptide peroxisomal targeting signal (SKL-type) and plays an essential role in peroxisomal protein import. Peroxins (PEXs) are proteins that are essential for the assembly of functional peroxisomes. The peroxisome biogenesis disorders (PBDs) are a group of genetically heterogeneous autosomal recessive, lethal diseases characterized by m…
- **Diseases (Open Targets)**: Zellweger spectrum disorders (0.806); peroxisome biogenesis disorder 2A (Zellweger) (0.780); peroxisome biogenesis disorder 2B (0.750); rhizomelic chondrodysplasia punctata type 5 (0.716); peroxisome biogenesis disorder (0.716)
- **Europe PMC papers**: 1958
- **Why important**: PEX5 connects directly to BCAT1 and is the essential receptor for import of proteins bearing the peroxisomal targeting signal. Its established functions include peroxisomal matrix import, receptor recycling, and pexophagy, and its disease associations include Zellweger-spectrum and related peroxisome-biogenesis disorders. It is detected in both colon and skin, making it a useful candidate for a conserved organelle-maintenance component.
- **Conclusion**: Established: PEX5 is required for peroxisomal protein import and peroxisome maintenance. Hypothesis: its association with BCAT1 may reflect coordinated regulation of amino-acid metabolism and peroxisomal quality control. The module does not demonstrate a direct PEX5-BCAT1 mechanism.

#### RBPMS

- **Related proteins** (co-abundance neighbors): BCAT1 (0.85), VPS37A (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding protein, mRNA processing factor. This gene encodes a member of the RNA recognition motif family of RNA-binding proteins. The RNA recognition motif is between 80-100 amino acids in length and family members contain one to four copies of the motif. The RNA recognition motif consists of two short stretches of conserved sequence, as well as a few highly conserved hydrophobic residues. The encoded protein has a single, putative RNA re…
- **Diseases (Open Targets)**: uterine corpus leiomyoma (0.420); renal carcinoma (0.416); atrial fibrillation (0.412); preeclampsia (0.338); chronic kidney disease (0.318)
- **Europe PMC papers**: 1929
- **Why important**: RBPMS has fewer network links than the principal hubs but connects BCAT1 and VPS37A, thereby bridging metabolic and trafficking-related portions of the module. It is an RNA-binding protein associated with alternative splicing, RNA processing, oxidative-stress response, transcriptional regulation, and SMAD signaling. Its blood-vessel and renal-cell annotations, together with detection in colon but not skin, make it informative for assessing cell-type composition and tissue-specific contribution.
- **Conclusion**: Established: RBPMS is an RNA-processing regulator with vascular, renal, and stress-related expression associations. Hypothesis: it may coordinate post-transcriptional adaptation within the co-abundance state or may act as a marker of a shared stromal or vascular cell contribution. The available evidence cannot distinguish regulation from correlated cell composition.

## Module 9

**Tissue pair**: colon and skin  
**Genes (11)**: ANKRD17, ARIH1, BRAP, ECD, GEMIN4, HYCC1, INTS4, TIMELESS, TIPIN, TMED8, URGCP

### Function

The strongest interpretation is a DNA-replication stress module centered on replication-fork protection and fork arrest. TIMELESS and TIPIN are the only genes supported by globally significant GO evidence, specifically the replication fork protection complex and replication fork arrest terms (GO:CC replication fork protection complex; q_global = 0.016) and (GO:BP replication fork arrest; q_global = 0.016). Their established roles in the replisome, DNA-replication checkpoint signaling, DNA-damage response, and protection from replication-associated stress provide a coherent functional core. The remaining genes do not have globally significant GO/KEGG annotations in this module, so they should not be assigned the replication-fork function solely from co-abundance. Their annotations instead suggest additional links to ubiquitination and signaling, transcription and RNA processing, vesicle trafficking, membrane-associated functions, and cell proliferation. Thus, this is best viewed as a replication-stress core embedded in a broader regulatory co-abundance neighborhood rather than as a uniformly annotated pathway module.

**Cell composition.** This module does not resemble a plasma-protein or secreted-protein module: none of its genes are classified as secreted, and all are detected at the protein level in both colon and skin. All genes have low immune-cell specificity, with no enriched blood-cell category, arguing against a straightforward blood-cell contamination or circulating-protein explanation. Most genes have low tissue specificity, which is compatible with broadly distributed cellular functions. Several genes show cell-type-enhanced expression, particularly in spermatogenic populations, while other enhancements involve neutrophils, muscle, epithelial, neuronal, retinal, or progenitor populations. These patterns suggest that the shared colon-skin signal may reflect conserved cellular programs or proliferative-state composition rather than a tissue-specific secretory program. The spermatogenic enrichments should be treated as HPA expression-context clues, not evidence that germ cells are present in the colon or skin samples.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC replication fork protection complex | 0.016 | TIMELESS, TIPIN |
| GO:BP replication fork arrest | 0.016 | TIMELESS, TIPIN |

### STRING and hu.MAP

STRING provides one particularly strong known relationship, TIMELESS-TIPIN, supporting the replication-fork core. STRING reports no functional enrichment for the module, so the network-level interpretation should rely primarily on (GO:CC replication fork protection complex; q_global = 0.016) and (GO:BP replication fork arrest; q_global = 0.016) rather than on STRING enrichment. hu.MAP independently places TIMELESS and TIPIN together in multiple replisome or replication-fork-related complexes (hu.MAP huMAP3_06417.1) through (hu.MAP huMAP3_12180.1), alongside proteins such as MCM, GINS, CDC45, and CLSPN. This repeated complex evidence strengthens the conclusion that the pair represents a genuine known molecular unit. hu.MAP also places ECD and GEMIN4 together in a large spliceosomal complex (hu.MAP huMAP3_08980.1), consistent with RNA-processing biology. The other co-abundance relationships are not represented by the supplied high-confidence STRING or hu.MAP evidence. Consequently, the resources validate selected cores of the module but do not establish one complete physical complex containing all module genes.

**STRING interactions (score >= 0.7)**: 1 of 55 gene pairs: TIMELESS–TIPIN (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06417.1 (TIPIN, TIMELESS; 2/8); huMAP3_06136.1 (TIPIN, TIMELESS; 2/9); huMAP3_08399.1 (TIPIN, TIMELESS; 2/10); huMAP3_09238.1 (TIPIN, TIMELESS; 2/11); huMAP3_11119.1 (TIPIN, TIMELESS; 2/14); huMAP3_14758.1 (TIPIN, TIMELESS; 2/14); huMAP3_08554.1 (TIPIN, TIMELESS; 2/15); huMAP3_11832.1 (TIPIN, TIMELESS; 2/15); huMAP3_12180.1 (TIPIN, TIMELESS; 2/17); huMAP3_08980.1 (ECD, GEMIN4; 2/97)

### Novelty

The module should not be claimed as a wholly new molecular complex. The TIMELESS-TIPIN relationship is already strongly established by STRING and repeated hu.MAP complexes (hu.MAP huMAP3_06417.1) through (hu.MAP huMAP3_12180.1), while the ECD-GEMIN4 association is represented in hu.MAP (hu.MAP huMAP3_08980.1). A potentially novel aspect is the conserved co-abundance configuration linking this replication-fork core with BRAP, ANKRD17, ECD, GEMIN4, and the other regulatory genes across colon and skin. However, absence of the remaining relationships from STRING or hu.MAP does not prove that they are biologically new; it may reflect incomplete interaction catalogs, context dependence, indirect regulation, or co-expression rather than physical binding. The defensible conclusion is that this is a potentially novel tissue-shared co-abundance module built around a known replication-stress pair, requiring experimental validation before being described as a new mechanism.

**Hypothesis.** Hypothesis: in shared epithelial or proliferative cellular states of colon and skin, replication stress may increase coordinated expression of the TIMELESS-TIPIN fork-protection system together with regulatory proteins that influence ubiquitination, transcription, RNA maturation, signaling, and membrane or vesicle biology. BRAP may act as a network-level connector linking several of these regulatory components, while ECD and GEMIN4 may connect replication-associated state changes to transcriptional and spliceosomal capacity. ANKRD17 could provide an additional link between cell-cycle control and innate or stress-responsive signaling. This hypothesis predicts that the module should be strongest in cells undergoing replication or repair stress and that perturbing TIMELESS or TIPIN should alter the co-abundance of selected neighboring genes. The prediction is not established by the enrichment or interaction evidence alone.

### Important genes

#### TIMELESS

- **Related proteins** (co-abundance neighbors): ECD (0.82); STRING partners: TIPIN (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon, skin
- **hu.MAP 3.0**: huMAP3_06417.1, huMAP3_06136.1, huMAP3_08399.1, huMAP3_09238.1, huMAP3_11119.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1
- **Function (MyGene.info)**: timeless circadian regulator. The protein encoded by this gene is highly conserved and is involved in cell survival after damage or stress, increase in DNA polymerase epsilon activity, maintenance of telomere length, and epithelial cell morphogenesis. The encoded protein also plays a role in the circadian rhythm autoregulatory loop, interacting with the PERIOD genes (PER1, PER2, and PER3) and others to downregulate activation …
- **Diseases (Open Targets)**: advanced sleep phase syndrome (0.503); ocular hypertension (0.310); neurodegenerative disease (0.209); breast carcinoma (0.111); breast cancer (0.108)
- **Europe PMC papers**: 3998
- **Why important**: TIMELESS is one of the two genes in both globally significant terms (GO:CC replication fork protection complex; q_global = 0.016) and (GO:BP replication fork arrest; q_global = 0.016). It has the strongest direct network support through the high-confidence STRING interaction with TIPIN and appears with TIPIN across the replication-related hu.MAP complexes (hu.MAP huMAP3_06417.1) through (hu.MAP huMAP3_12180.1). Its documented roles include replication-checkpoint signaling, DNA repair, damage response, telomere maintenance, epithelial morphogenesis, and circadian regulation. Its substantial literature volume and disease links make it the best-established anchor for the module.
- **Conclusion**: Established evidence supports TIMELESS as a central replication-fork protection and DNA-damage-response component of the module. Its association with the broader co-abundance neighborhood is supported by the network but does not establish direct binding to the other module genes. A role in coordinating epithelial stress or proliferation is a plausible hypothesis, not a demonstrated property of this module.

#### TIPIN

- **Related proteins** (co-abundance neighbors): ANKRD17 (0.80); STRING partners: TIMELESS (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in colon, skin
- **hu.MAP 3.0**: huMAP3_06417.1, huMAP3_06136.1, huMAP3_08399.1, huMAP3_09238.1, huMAP3_11119.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1
- **Function (MyGene.info)**: TIMELESS interacting protein. The protein encoded by this gene is part of the replisome complex, a group of proteins that support DNA replication. It binds TIM, which is involved in circadian rhythm regulation, and aids in protecting cells against DNA damage and stress. Two pseudogenes and two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: renal carcinoma (0.348); clear cell renal carcinoma (0.320); smoking initiation (0.314); ovarian dysfunction (0.230); melanoma (0.074)
- **Europe PMC papers**: 751
- **Why important**: TIPIN is the second gene in both globally significant terms (GO:CC replication fork protection complex; q_global = 0.016) and (GO:BP replication fork arrest; q_global = 0.016). It forms the strongest known STRING pair with TIMELESS and is repeatedly represented with TIMELESS in hu.MAP replication complexes (hu.MAP huMAP3_06417.1) through (hu.MAP huMAP3_12180.1). Its annotations directly implicate the replisome, replication-fork processing, replication checkpoints, DNA-damage response, and regulation of nuclear DNA replication. It therefore provides highly specific functional support rather than merely generic cell-cycle association.
- **Conclusion**: Established evidence identifies TIPIN as a core replication-fork protection and replication-stress gene in this module. Its co-abundance with the other genes may reflect a shared proliferative or damage-response state, but the supplied evidence does not show that TIPIN physically interacts with those other neighbors.

#### BRAP

- **Related proteins** (co-abundance neighbors): ARIH1 (0.82), URGCP (0.82), GEMIN4 (0.81), ANKRD17 (0.81), TMED8 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BRCA1 associated protein. The protein encoded by this gene was identified by its ability to bind to the nuclear localization signal of BRCA1 and other proteins. It is a cytoplasmic protein which may regulate nuclear targeting by retaining proteins with a nuclear localization signal in the cytoplasm. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: gout (0.234); colorectal cancer (0.202); age-related macular degeneration (0.186); COVID-19 (0.179); heart failure (0.158)
- **Europe PMC papers**: 6455
- **Why important**: BRAP has the highest network connectivity in the supplied module and links several otherwise weakly connected branches, including ARIH1, URGCP, GEMIN4, ANKRD17, and TMED8. Its documented functions involve nuclear-targeting regulation, ubiquitination-related signaling, MAPK and RAS signaling, and negative regulation of signal transduction. It is protein-detected in both tissues and has substantially more literature than most of the less characterized module genes. Its position makes it important for interpreting the module as broader than a compact replisome fragment.
- **Conclusion**: Established evidence supports BRAP as a regulatory and network-connecting gene with roles in signaling and protein handling. Its hub-like co-abundance position suggests that it may organize the broader module signal, but neither STRING nor hu.MAP supplies a known physical complex connecting BRAP to the replication-fork core. Any mechanistic bridge between BRAP and TIMELESS-TIPIN remains hypothetical.

#### ECD

- **Related proteins** (co-abundance neighbors): TIMELESS (0.82), ANKRD17 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in colon, skin
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: ecdysoneless cell cycle regulator. Enables histone acetyltransferase binding activity. Involved in positive regulation of transcription by RNA polymerase II. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); alcohol drinking (0.209); breast cancer (0.092); gastric cancer (0.082); breast carcinoma (0.074)
- **Europe PMC papers**: 16795
- **Why important**: ECD connects the module network to TIMELESS and ANKRD17 and is paired with GEMIN4 in the hu.MAP spliceosomal complex (hu.MAP huMAP3_08980.1). Its annotation supports transcriptional regulation, and its localization spans the nucleoplasm and cytosol. ECD also has a very large literature base and disease associations, making it a well-studied candidate for linking cellular stress, transcription, and RNA-processing capacity to the replication-related core.
- **Conclusion**: Established evidence supports ECD as a transcription-associated regulator and as a member of the hu.MAP complex represented by (hu.MAP huMAP3_08980.1). Its connection to TIMELESS in the co-abundance network may indicate coordinated regulation between replication stress and gene-expression machinery, but a direct functional bridge is not established.

#### ANKRD17

- **Related proteins** (co-abundance neighbors): BRAP (0.81), TIPIN (0.80), ECD (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ankyrin repeat domain 17. The protein encoded by this gene belongs to the family of ankyrin repeat-containing proteins, and contains two distinct arrays of ankyrin repeats in its amino-terminal region, one with 15 ankyrin repeats, and the other with 10 ankyrin repeats. It also contains a nuclear export signal, nuclear localization signal, and a cyclin-binding RXL motif. Localization of this protein to the nucleus has been …
- **Diseases (Open Targets)**: Chopra-Amiel-Gordon syndrome (0.782); neurodegenerative disease (0.555); hereditary disease (0.523); neurodevelopmental disorder (0.371); syndromic complex neurodevelopmental disorder (0.370)
- **Europe PMC papers**: 469
- **Why important**: ANKRD17 occupies a connecting position between BRAP, TIPIN, and ECD. Its annotations include regulation of DNA replication, positive regulation of cell-cycle progression, innate immune response, and NF-kappaB signaling. It is detected in both tissues and has disease associations involving neurodevelopmental and hereditary disorders. The combination of a bridge position and annotations spanning replication, proliferation, and stress-responsive signaling makes it a useful candidate for explaining why the module extends beyond the TIMELESS-TIPIN pair.
- **Conclusion**: Established evidence supports ANKRD17 as a nuclear ankyrin-repeat protein associated with replication, cell-cycle, and innate-response biology. Its network placement is consistent with a coordinating role, but the module data do not prove that ANKRD17 regulates TIPIN or physically joins the replication-fork complex. That coordinating role remains a hypothesis.

## Module 10

**Tissue pair**: colon and skin  
**Genes (17)**: ASL, ASCC3, CNOT1, DIAPH1, DOCK1, PTK2, KATNAL1, WDR77, NAA15, NEMF, PKD1, SDAD1, TEX10, THOP1, TXLNG, UBE3A, WDR26

### Function

The strongest functional interpretation is a proteostasis and cellular-quality-control module, with a globally corrected enrichment for ubiquitin-dependent protein catabolic process (GO:BP ubiquitin-dependent protein catabolic process; q_global = 0.049). The enriched genes ASCC3, NEMF, PTK2, UBE3A, WDR26 and WDR77 connect ubiquitin-related degradation with ribosome rescue, protein quality control, signaling and cytoskeletal or cell-matrix biology. NEMF and ASCC3 provide particularly coherent links to stalled-ribosome rescue and ribosome-associated ubiquitin-dependent catabolism, while UBE3A, WDR26 and WDR77 support ubiquitin-mediated protein handling. PTK2, DOCK1, PKD1, KATNAL1 and DIAPH1 suggest an accompanying axis involving cell adhesion, small-GTPase signaling, actin or microtubule organization and membrane-associated signaling. The module therefore appears to combine a core protein-surveillance program with structural and signaling processes rather than represent a single narrowly defined pathway. No STRING functional-enrichment term was reported. The absence of additional enriched terms does not invalidate the module, particularly because the network contains several broadly expressed cellular genes and may integrate processes that are related mechanistically without sharing many annotation terms.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module: only PKD1 is annotated as secreted with unknown location, and the remaining genes are intracellular or membrane-associated. The HPA profile is dominated by low tissue specificity, with only limited tissue enhancement and one tissue-enriched gene, ASL. Protein detection is broadly supported in both colon and skin. Blood-cell specificity is generally low, with no recurrent enriched blood-cell category and two genes not detected in immune cells, so the module is not strongly suggestive of a blood-cell contamination signal. Several cell-type-enhanced annotations occur across epithelial, neuronal, reproductive, hepatic, neutrophil and other cell types. The repeated colonocyte, enterocyte and tuft-cell annotations, together with ASL and THOP1 in digestive epithelial cell types, support a possible epithelial contribution, but the broad HPA profile means that shared cell states or general cellular processes remain plausible alternatives.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP ubiquitin-dependent protein catabolic process | 0.049 | ASCC3, NEMF, PTK2, UBE3A, WDR26, WDR77 |

### STRING and hu.MAP

STRING supports only a small set of high-confidence pairwise relationships within the module: DOCK1 with PTK2, PKD1 with PTK2, and SDAD1 with TEX10. These relationships provide established anchors for focal adhesion or signaling and for nucleolar or ribosome-related biology. The fact sheet reports no STRING functional-enrichment result. hu.MAP reports no complex containing multiple module members. Thus, the co-abundance module is not reproduced as a recognized dense protein complex. Its structure is more consistent with coordinated activity across partially connected cellular systems than with one pre-existing stable complex. The co-abundance edges that lack STRING support should be treated as expression-level associations rather than established physical interactions.

**STRING interactions (score >= 0.7)**: 3 of 136 gene pairs: DOCK1–PTK2 (0.979); PKD1–PTK2 (0.73); SDAD1–TEX10 (0.882)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a new tissue-pair co-abundance pattern, but the fact sheet does not establish that it is a newly discovered biological mechanism. Its novelty lies most plausibly in the coordinated association of proteostasis, ribosome quality control, adhesion, cytoskeletal regulation and epithelial cell-state signals across colon and skin. Several component functions and three internal relationships are already supported by prior databases, and the absence of a hu.MAP complex or additional STRING relationships does not prove novelty. A defensible conclusion is that the cross-tissue co-abundance configuration is potentially novel and merits validation, whereas the individual gene functions and some pairwise relationships are established.

**Hypothesis.** Hypothesis: the module reflects a conserved epithelial cellular-maintenance state shared by colon and skin. In this state, protein synthesis or translation stress could increase ribosome-quality-control and ubiquitin-dependent disposal through NEMF, ASCC3, UBE3A, WDR26 and WDR77, while PKD1, PTK2 and DOCK1 coordinate cell-matrix or membrane signaling and KATNAL1 and DIAPH1 adjust microtubule and actin architecture. ASL and THOP1 may mark the epithelial metabolic and peptide-processing context in which this response occurs. This is a mechanistic proposal, not a demonstrated causal pathway; the co-abundance data and database annotations do not establish directionality, physical complex formation or a shared stress trigger.

### Important genes

#### PTK2

- **Related proteins** (co-abundance neighbors): PKD1 (0.83); STRING partners: DOCK1 (0.979), PKD1 (0.73)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein tyrosine kinase 2. This gene encodes a cytoplasmic protein tyrosine kinase which is found concentrated in the focal adhesions that form between cells growing in the presence of extracellular matrix constituents. The encoded protein is a member of the FAK subfamily of protein tyrosine kinases but lacks significant sequence similarity to kinases from other subfamilies. Activation of this gene may be an important early…
- **Diseases (Open Targets)**: neurodegenerative disease (0.551); Abnormality of the skeletal system (0.450); atrial fibrillation (0.396); Dupuytren Contracture (0.390); non-small cell lung carcinoma (0.327)
- **Europe PMC papers**: 7056
- **Why important**: PTK2 is a central signaling anchor in the module because it is linked by STRING to DOCK1 and PKD1. Its established focal-adhesion localization and roles in cell-matrix adhesion, signal-complex assembly and growth-related signaling connect the module to tissue architecture. It is also one of the genes in the globally corrected ubiquitin-dependent protein-catabolic term (GO:BP ubiquitin-dependent protein catabolic process; q_global = 0.049), although that enrichment does not by itself establish a direct ubiquitin function for PTK2. Its substantial literature volume and disease-linked associations make it a biologically informative entry point.
- **Conclusion**: Established evidence supports PTK2 as a focal-adhesion and signaling component and as a STRING anchor. The conclusion that it coordinates the proteostasis and epithelial-structure arms is a hypothesis inferred from its co-abundance position and annotations, not a demonstrated mechanism.

#### PKD1

- **Related proteins** (co-abundance neighbors): WDR77 (0.84), PTK2 (0.83), ASCC3 (0.82), SDAD1 (0.82), TEX10 (0.82), TXLNG (0.81), WDR26 (0.80); STRING partners: PTK2 (0.73)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polycystin 1, transient receptor potential channel interacting. This gene encodes a member of the polycystin protein family. The encoded glycoprotein contains a large N-terminal extracellular region, multiple transmembrane domains and a cytoplasmic C-tail. It is an integral membrane protein that functions as a regulator of calcium permeable cation channels and intracellular calcium homoeostasis. It is also involved in cell-cell/matrix interactions and may modu…
- **Diseases (Open Targets)**: autosomal dominant polycystic kidney disease (0.860); hypertensive disorder (0.782); polycystic kidney disease (0.781); cystic kidney disease (0.743); kidney failure (0.688)
- **Europe PMC papers**: 8084
- **Why important**: PKD1 has one of the strongest network positions in the module and connects to PTK2, DOCK1-related signaling context, ASCC3, SDAD1, TEX10, TXLNG and WDR26 through the co-abundance network. Its established functions include membrane and cell-cell or cell-matrix interactions, calcium-permeable cation-channel regulation and intracellular calcium homeostasis. It is detected in both colon and skin, is tissue-enhanced in brain, and has extensive disease literature, particularly involving polycystic kidney disease.
- **Conclusion**: Established evidence supports PKD1 as a membrane-associated signaling and adhesion regulator with major disease relevance. Its position suggests that it may bridge signaling, structural and quality-control signals in this module, but a direct role in the ubiquitin-dependent process is not established by the fact sheet.

#### NEMF

- **Related proteins** (co-abundance neighbors): CNOT1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nuclear export mediator factor. This gene encodes a component of the ribosome quality control complex. The encoded protein facilitates the recognition and ubiquitination of stalled 60S subunits by the ubiquitin ligase listerin. A similar protein in fly functions as a tumor suppressor. [provided by RefSeq, Jul 2016].
- **Diseases (Open Targets)**: intellectual developmental disorder with speech delay and axonal peripheral neuropathy (0.708); hereditary disease (0.471); Global developmental delay (0.374); Intellectual disability (0.371); cerebellar ataxia (0.370)
- **Europe PMC papers**: 2061
- **Why important**: NEMF is a direct member of the globally corrected ubiquitin-dependent protein-catabolic term (GO:BP ubiquitin-dependent protein catabolic process; q_global = 0.049). Its established role in the ribosome-quality-control complex, recognition of stalled sixty-subunit ribosomes and facilitation of their ubiquitination gives the module a mechanistically specific proteostasis component. It is connected to CNOT1 in the module, linking quality control with mRNA metabolism, and it has substantial disease and developmental literature.
- **Conclusion**: Established evidence supports NEMF as a ribosome-surveillance and stalled-translation quality control factor. It is a strong candidate for the module's proteostasis core. Whether its co-abundance with adhesion and cytoskeletal genes reflects a shared stress response or merely correlated cell composition remains unresolved.

#### UBE3A

- **Related proteins** (co-abundance neighbors): KATNAL1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin protein ligase E3A. This gene encodes an E3 ubiquitin-protein ligase, part of the ubiquitin protein degradation system. This imprinted gene is maternally expressed in brain and biallelically expressed in other tissues. Maternally inherited deletion of this gene causes Angelman Syndrome, characterized by severe motor and intellectual retardation, ataxia, hypotonia, epilepsy, absence of speech, and characteristic facie…
- **Diseases (Open Targets)**: Angelman syndrome (0.843); hereditary disease (0.545); Intellectual disability (0.514); Global developmental delay (0.400); neurodevelopmental disorder (0.346)
- **Europe PMC papers**: 4879
- **Why important**: UBE3A is an established ubiquitin-protein ligase and a member of the globally corrected term (GO:BP ubiquitin-dependent protein catabolic process; q_global = 0.049). Its connection to KATNAL1 places an E3 ligase within the central portion of the co-abundance subgraph, and its broad detection in colon and skin supports relevance to both tissues. UBE3A has extensive literature and strong disease associations, especially Angelman syndrome and related neurodevelopmental phenotypes.
- **Conclusion**: Established evidence supports UBE3A as a ubiquitin-mediated protein-degradation regulator. It may help define the proteostasis arm of the module, but the fact sheet does not demonstrate that UBE3A acts on NEMF, PTK2 or any other module member.

#### KATNAL1

- **Related proteins** (co-abundance neighbors): TXLNG (0.85), NAA15 (0.83), DOCK1 (0.83), DIAPH1 (0.83), ASL (0.82), UBE3A (0.82), THOP1 (0.82), CNOT1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Centrosome, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: katanin catalytic subunit A1 like 1. Enables identical protein binding activity and microtubule-severing ATPase activity. Involved in microtubule severing. Located in cytoplasm; microtubule; and spindle pole. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: refractive error (0.390); Abnormality of refraction (0.313); androgenetic alopecia (0.299); cirrhosis of liver (0.284); conduction system disorder (0.253)
- **Europe PMC papers**: 256
- **Why important**: KATNAL1 has the most prominent network connectivity in the module and links TXLNG, NAA15, DOCK1, DIAPH1, ASL, UBE3A, THOP1 and CNOT1. Its established microtubule-severing ATPase function and centrosomal or cytosolic localization provide a structural explanation for its central network position. It also connects structural organization to ubiquitin-related and RNA or protein handling genes, although it is not itself in the primary enriched term (GO:BP ubiquitin-dependent protein catabolic process; q_global = 0.049).
- **Conclusion**: Established evidence supports KATNAL1 as a microtubule-organization factor. Its centrality makes it an important candidate for linking cell architecture to the proteostasis-associated genes. That bridging role is a hypothesis based on network structure and should not be treated as a demonstrated biochemical interaction.

## Module 11

**Tissue pair**: colon and skin  
**Genes (43)**: ACTR8, ATR, CPSF1, CPSF2, CRNKL1, DCAF13, DDX52, DHX33, DHX37, ERCC3, ESS2, SMG6, HEATR1, KLHL7, MDN1, NOL11, NOL8, NOM1, URB1, NUP107, NUP98, TENT4B, PLK1, PSPC1, PUM3, RCL1, RIF1, RMP64, POLR3A, RRP1B, SMARCD1, SP3, SRCAP, GTF3C1, THOC1, THOC2, THOC5, USP36, UTP11, UTP20, WDR36, WDR3, XPO6

### Function

The module is most strongly characterized as a nuclear RNA-production and ribosome-biogenesis program. The globally corrected GO evidence identifies nuclear and nucleolar localization, nucleic-acid and RNA biosynthesis, RNA processing, ribonucleoprotein-complex biogenesis, ribosome biogenesis, rRNA metabolism and rRNA processing (7 globally significant GO/KEGG terms, q_global 3.2e-11–1.56e-08; see the table), (11 globally significant GO/KEGG terms, q_global 1.85e-08–4.73e-07; see the table). The same interpretation is supported by the enrichment of preribosome and small-subunit processome terms (GO:CC preribosome; q_global = 8.37e-07), (GO:BP maturation of SSU-rRNA; q_global = 5.49e-06), (GO:CC small-subunit processome; q_global = 5.49e-06), together with RNA export and nucleocytoplasmic transport (GO:BP nuclear export; q_global = 0.00256), (GO:BP RNA export from nucleus; q_global = 0.012), (GO:BP mRNA export from nucleus; q_global = 0.0371), (KEGG Nucleocytoplasmic transport - Homo sapiens (human); q_global = 0.0387). The module therefore represents coordinated expression of machinery for producing, processing, exporting and quality-controlling nuclear RNAs, with a particularly strong nucleolar and ribosome-biogenesis component. Additional genes connect this core to transcription, chromatin regulation, DNA repair, cell-cycle control, mRNA processing and surveillance. These latter features broaden the module but do not outweigh the dominant rRNA-processing and nuclear RNA-metabolism signal.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and the proteins are predominantly nuclear, nucleoplasmic or nucleolar. Protein detection is broadly compatible with both colon and skin, supporting a conserved intracellular program rather than a tissue-specific secreted signal. The module is also not strongly blood-cell enriched overall: most genes have low immune-cell specificity, with only limited immune-cell enhancement or enrichment. Some cell-type signals occur in reproductive cells, neutrophils and other specialized populations, and several genes have enhanced expression in particular tissues, but these scattered signals do not establish that the module is driven by blood contamination or a shared immune-cell population. A shared housekeeping-like nuclear RNA program remains a plausible contributor to its conservation across colon and skin.

**GO/KEGG enrichment**: 44 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC nuclear lumen | 3.2e-11 | ACTR8, ATR, CPSF1, CPSF2, CRNKL1, DCAF13, DDX52, DHX33, DHX37, ERCC3, GTF3C1, HEATR1, KLHL7, MDN1, NOL11, NOL8, NOM1, NUP107, NUP98, PLK1, POLR3A, PSPC1, PUM3, RCL1, RIF1, RMP64, RRP1B, SMARCD1, SMG6, SP3, SRCAP, TENT4B, THOC1, THOC2, THOC5, URB1, USP36, UTP11, UTP20, WDR3, WDR36, XPO6 |
| GO:BP nucleic acid biosynthetic process | 7.81e-10 | ACTR8, ATR, CPSF1, CPSF2, CRNKL1, DCAF13, DDX52, DHX33, DHX37, ERCC3, ESS2, GTF3C1, HEATR1, NOL11, NOL8, NUP98, PLK1, POLR3A, PSPC1, RCL1, RIF1, RRP1B, SMARCD1, SMG6, SP3, SRCAP, TENT4B, THOC1, THOC2, THOC5, URB1, USP36, UTP11, UTP20, WDR3, WDR36 |
| GO:CC nucleolus | 1.69e-09 | DCAF13, DDX52, DHX33, DHX37, GTF3C1, HEATR1, KLHL7, MDN1, NOL11, NOL8, NOM1, PSPC1, PUM3, RCL1, RMP64, RRP1B, SMG6, TENT4B, URB1, USP36, UTP11, UTP20, WDR3, WDR36, XPO6 |
| GO:BP ribonucleoprotein complex biogenesis | 4.61e-09 | ATR, CRNKL1, DCAF13, DDX52, DHX37, HEATR1, MDN1, NOL11, NOL8, NOM1, RCL1, RRP1B, TENT4B, URB1, USP36, UTP11, UTP20, WDR3, WDR36 |
| GO:BP ribosome biogenesis | 5.12e-09 | DCAF13, DDX52, DHX37, HEATR1, MDN1, NOL11, NOL8, NOM1, RCL1, RRP1B, TENT4B, URB1, USP36, UTP11, UTP20, WDR3, WDR36 |
| GO:BP rRNA metabolic process | 6.31e-09 | DCAF13, DDX52, DHX37, GTF3C1, HEATR1, NOL11, NOL8, RCL1, RRP1B, TENT4B, URB1, USP36, UTP11, UTP20, WDR3, WDR36 |
| GO:BP rRNA processing | 1.56e-08 | DCAF13, DDX52, DHX37, HEATR1, NOL11, NOL8, RCL1, RRP1B, TENT4B, URB1, USP36, UTP11, UTP20, WDR3, WDR36 |
| GO:BP RNA biosynthetic process | 1.85e-08 | ACTR8, CPSF1, CPSF2, CRNKL1, DCAF13, DDX52, DHX33, DHX37, ERCC3, ESS2, GTF3C1, HEATR1, NOL11, NOL8, NUP98, PLK1, POLR3A, PSPC1, RCL1, RIF1, RRP1B, SMARCD1, SP3, SRCAP, TENT4B, THOC1, THOC2, THOC5, URB1, USP36, UTP11, UTP20, WDR3, WDR36 |
| GO:BP nucleobase-containing compound biosynthetic process | 2.53e-08 | ACTR8, ATR, CPSF1, CPSF2, CRNKL1, DCAF13, DDX52, DHX33, DHX37, ERCC3, ESS2, GTF3C1, HEATR1, NOL11, NOL8, NUP98, PLK1, POLR3A, PSPC1, RCL1, RIF1, RRP1B, SMARCD1, SMG6, SP3, SRCAP, TENT4B, THOC1, THOC2, THOC5, URB1, USP36, UTP11, UTP20, WDR3, WDR36 |
| GO:BP RNA metabolic process | 2.71e-08 | ACTR8, CPSF1, CPSF2, CRNKL1, DCAF13, DDX52, DHX33, DHX37, ERCC3, ESS2, GTF3C1, HEATR1, NOL11, NOL8, NUP98, PLK1, POLR3A, PSPC1, RCL1, RIF1, RRP1B, SMARCD1, SMG6, SP3, SRCAP, TENT4B, THOC1, THOC2, THOC5, URB1, USP36, UTP11, UTP20, WDR3, WDR36 |
| GO:CC nuclear protein-containing complex | 3.19e-08 | ACTR8, ATR, CPSF1, CPSF2, CRNKL1, DCAF13, DHX37, ERCC3, ESS2, HEATR1, NOL11, NUP107, NUP98, POLR3A, RCL1, SMARCD1, SMG6, SRCAP, TENT4B, THOC1, THOC2, THOC5, UTP11, UTP20, WDR3, WDR36 |
| GO:CC nucleus | 8.57e-08 | ACTR8, ATR, CPSF1, CPSF2, CRNKL1, DCAF13, DDX52, DHX33, DHX37, ERCC3, ESS2, GTF3C1, HEATR1, KLHL7, MDN1, NOL11, NOL8, NOM1, NUP107, NUP98, PLK1, POLR3A, PSPC1, PUM3, RCL1, RIF1, RMP64, RRP1B, SMARCD1, SMG6, SP3, SRCAP, TENT4B, THOC1, THOC2, THOC5, URB1, USP36, UTP11, UTP20, WDR3, WDR36, XPO6 |
| GO:CC membrane-enclosed lumen | 1.43e-07 | ACTR8, ATR, CPSF1, CPSF2, CRNKL1, DCAF13, DDX52, DHX33, DHX37, ERCC3, GTF3C1, HEATR1, KLHL7, MDN1, NOL11, NOL8, NOM1, NUP107, NUP98, PLK1, POLR3A, PSPC1, PUM3, RCL1, RIF1, RMP64, RRP1B, SMARCD1, SMG6, SP3, SRCAP, TENT4B, THOC1, THOC2, THOC5, URB1, USP36, UTP11, UTP20, WDR3, WDR36, XPO6 |
| GO:CC organelle lumen | 1.43e-07 | ACTR8, ATR, CPSF1, CPSF2, CRNKL1, DCAF13, DDX52, DHX33, DHX37, ERCC3, GTF3C1, HEATR1, KLHL7, MDN1, NOL11, NOL8, NOM1, NUP107, NUP98, PLK1, POLR3A, PSPC1, PUM3, RCL1, RIF1, RMP64, RRP1B, SMARCD1, SMG6, SP3, SRCAP, TENT4B, THOC1, THOC2, THOC5, URB1, USP36, UTP11, UTP20, WDR3, WDR36, XPO6 |
| GO:CC intracellular organelle lumen | 1.43e-07 | ACTR8, ATR, CPSF1, CPSF2, CRNKL1, DCAF13, DDX52, DHX33, DHX37, ERCC3, GTF3C1, HEATR1, KLHL7, MDN1, NOL11, NOL8, NOM1, NUP107, NUP98, PLK1, POLR3A, PSPC1, PUM3, RCL1, RIF1, RMP64, RRP1B, SMARCD1, SMG6, SP3, SRCAP, TENT4B, THOC1, THOC2, THOC5, URB1, USP36, UTP11, UTP20, WDR3, WDR36, XPO6 |

### STRING and hu.MAP

STRING provides extensive, coherent prior support for the nucleolar and ribosome-biogenesis interpretation. The supplementary STRING enrichments identify nuclear lumen, nucleus, nucleolus, rRNA processing and ribosome biogenesis (15 supplementary STRING terms; within-query FDR 5.43e-17–2.89e-09). Many of the strongest within-module STRING relationships connect DCAF13, DDX52, DHX37, HEATR1, NOL11, RCL1, UTP11, UTP20, WDR3 and WDR36, indicating that a substantial part of the co-abundance structure recapitulates known functional relationships rather than an arbitrary correlation pattern. Other established links include the CPSF1–CPSF2 pair, the THOC1–THOC2–THOC5 group, the NUP107–NUP98 pair, and links involving RNA polymerase and nucleocytoplasmic transport machinery. hu.MAP independently identifies the THOC1–THOC2–THOC5 transcription-export complex in multiple complexes (hu.MAP huMAP3_04932.1), (hu.MAP huMAP3_12548.1) (hu.MAP huMAP3_09101.1) (hu.MAP huMAP3_10299.1) (hu.MAP huMAP3_10789.1) (hu.MAP huMAP3_11232.1) (hu.MAP huMAP3_09943.1) (hu.MAP huMAP3_08963.1) (hu.MAP huMAP3_02771.1) (hu.MAP huMAP3_09583.1) (hu.MAP huMAP3_02553.1) (hu.MAP huMAP3_07273.1) (hu.MAP huMAP3_08233.1), the CPSF1–CPSF2 complex (hu.MAP huMAP3_00102.1), (hu.MAP huMAP3_09096.1), (hu.MAP huMAP3_11757.1), the NUP98–NUP107 nuclear-pore complexes (hu.MAP huMAP3_07705.1), (hu.MAP huMAP3_09710.1), (hu.MAP huMAP3_12581.1), and smaller complexes containing rRNA-processing or transport proteins (hu.MAP huMAP3_08465.1), (hu.MAP huMAP3_11232.1). Thus, the module contains several recognizable molecular subassemblies linked by shared nuclear RNA biology. STRING and hu.MAP support biological coherence, but they do not by themselves demonstrate that all proteins physically form one complex or that co-abundance implies direct binding.

**STRING interactions (score >= 0.7)**: 80 of 903 gene pairs: ACTR8–SRCAP (0.801); CPSF1–CPSF2 (0.999); CPSF2–THOC5 (0.939); DCAF13–DDX52 (0.946); DCAF13–DHX37 (0.971); DCAF13–HEATR1 (0.997); DCAF13–NOL11 (0.968); DCAF13–PUM3 (0.865); DCAF13–RCL1 (0.993); DCAF13–UTP11 (0.998); DCAF13–UTP20 (0.998); DCAF13–WDR3 (0.999); DCAF13–WDR36 (0.999); DDX52–DHX37 (0.923); DDX52–HEATR1 (0.886); DDX52–NOL11 (0.829); DDX52–PUM3 (0.848); DDX52–RCL1 (0.753); DDX52–RRP1B (0.776); DDX52–UTP11 (0.936); DDX52–UTP20 (0.954); DDX52–WDR36 (0.814); DHX33–NOM1 (0.712); DHX33–USP36 (0.849); DHX33–WDR36 (0.77); DHX37–HEATR1 (0.943); DHX37–NOL11 (0.96); DHX37–RCL1 (0.922); DHX37–UTP11 (0.974); DHX37–UTP20 (0.975); DHX37–WDR3 (0.892); DHX37–WDR36 (0.929); GTF3C1–POLR3A (0.82); HEATR1–NOL11 (0.983); HEATR1–POLR3A (0.775); HEATR1–PUM3 (0.837); HEATR1–RCL1 (0.998); HEATR1–URB1 (0.914); HEATR1–UTP11 (0.997); HEATR1–UTP20 (0.999); HEATR1–WDR3 (0.999); HEATR1–WDR36 (0.999); MDN1–RRP1B (0.8); MDN1–UTP20 (0.802); NOL11–RCL1 (0.928); NOL11–UTP11 (0.967); NOL11–UTP20 (0.979); NOL11–WDR3 (0.951); NOL11–WDR36 (0.936); NOL8–URB1 (0.838); NOM1–PUM3 (0.741); NOM1–WDR3 (0.986); NUP107–NUP98 (0.999); POLR3A–URB1 (0.75); POLR3A–WDR3 (0.78); POLR3A–WDR36 (0.715); PUM3–RRP1B (0.79); PUM3–UTP20 (0.812); PUM3–WDR3 (0.905); PUM3–WDR36 (0.955); RCL1–RRP1B (0.783); RCL1–UTP11 (0.993); RCL1–UTP20 (0.998); RCL1–WDR3 (0.998); RCL1–WDR36 (0.998); RRP1B–UTP11 (0.763); RRP1B–UTP20 (0.731); RRP1B–WDR3 (0.796); RRP1B–WDR36 (0.824); THOC1–THOC2 (0.999); THOC1–THOC5 (0.999); THOC2–THOC5 (0.999); URB1–UTP20 (0.915); URB1–WDR36 (0.878); UTP11–UTP20 (0.998); UTP11–WDR3 (0.996); UTP11–WDR36 (0.998); UTP20–WDR3 (0.999); UTP20–WDR36 (0.999); WDR3–WDR36 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Nuclear lumen (FDR = 5.43e-17, 35 genes); COMPARTMENTS Nucleus (FDR = 7.73e-15, 42 genes); Keyword Nucleus (FDR = 2.35e-14, 41 genes); Component Nuclear lumen (FDR = 2.82e-13, 41 genes); COMPARTMENTS Nucleolus (FDR = 3.01e-12, 22 genes); NetworkNeighborAL rRNA processing, and RNA helicase activity (FDR = 6.22e-12, 17 genes); Component Nucleolus (FDR = 6.26e-11, 24 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 1.11e-10, 14 genes); NetworkNeighborAL rRNA modification in the nucleus and cytosol, and Maturation of SSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA) (FDR = 2.84e-10, 11 genes); NetworkNeighborAL rRNA processing, and Ribosomal large subunit biogenesis (FDR = 2.84e-10, 15 genes); NetworkNeighborAL rRNA modification in the nucleus and cytosol (FDR = 8.29e-10, 10 genes); Component Nucleus (FDR = 1.24e-09, 42 genes); Process rRNA metabolic process (FDR = 1.33e-09, 16 genes); Process rRNA processing (FDR = 2.37e-09, 15 genes); Process Ribosome biogenesis (FDR = 2.89e-09, 16 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04932.1 (THOC5, THOC2, THOC1; 3/14); huMAP3_08465.1 (NOL8, WDR36, DDX52; 3/17); huMAP3_12548.1 (THOC5, THOC2, THOC1; 3/21); huMAP3_09101.1 (THOC5, THOC2, THOC1; 3/22); huMAP3_10299.1 (THOC5, THOC2, THOC1; 3/22); huMAP3_10789.1 (THOC5, THOC2, THOC1; 3/37); huMAP3_11232.1 (UTP20, ATR, XPO6; 3/78); huMAP3_09943.1 (THOC5, THOC2, THOC1; 3/78); huMAP3_08963.1 (THOC5, THOC1; 2/5); huMAP3_02771.1 (THOC5, THOC1; 2/6); huMAP3_09583.1 (THOC5, THOC1; 2/7); huMAP3_02553.1 (THOC5, THOC1; 2/8); huMAP3_07273.1 (THOC5, THOC1; 2/8); huMAP3_08233.1 (THOC5, THOC1; 2/8); huMAP3_07705.1 (NUP98, NUP107; 2/9); huMAP3_08111.1 (THOC5, THOC1; 2/9); huMAP3_00102.1 (CPSF1, CPSF2; 2/12); huMAP3_09710.1 (NUP98, NUP107; 2/13); huMAP3_09096.1 (CPSF1, CPSF2; 2/15); huMAP3_11757.1 (CPSF1, CPSF2; 2/16); huMAP3_09226.1 (THOC5, THOC2; 2/17); huMAP3_06429.1 (ESS2, CRNKL1; 2/18); huMAP3_08703.1 (ESS2, CRNKL1; 2/21); huMAP3_08501.1 (ESS2, CRNKL1; 2/47); huMAP3_09504.1 (ESS2, CRNKL1; 2/51); huMAP3_12581.1 (NUP98, NUP107; 2/58); huMAP3_09945.1 (ESS2, CRNKL1; 2/61)

### Novelty

The molecular function is not a new biological discovery: nucleolar ribosome biogenesis, RNA processing, THO-mediated mRNA export, cleavage and polyadenylation, and nuclear transport are already established functions, and many of the relationships are represented in STRING and hu.MAP. The potentially new aspect is the observation that these known machineries form a conserved co-abundance module across colon and skin, including coordinated links between a strong rRNA-processing core and RNA export, RNA surveillance, chromatin and cell-cycle components. That cross-tissue co-abundance organization should be treated as a dataset-specific finding requiring replication in independent cohorts and control for cellular composition. Lack of a complete matching STRING or hu.MAP complex would not prove novelty, because co-abundance modules can reflect conditionally coordinated pathways, shared transcriptional regulation or indirect cellular programs.

**Hypothesis.** Hypothesis: in colon and skin, variation in proliferative or biosynthetic demand coordinately regulates a nuclear RNA-production axis. A nucleolar ribosome-biogenesis core involving DCAF13, UTP11, WDR3, DHX37 and related factors could increase or decrease with rRNA maturation and ribosomal assembly demand, while THOC1–THOC2–THOC5, NUP98–NUP107, CPSF proteins and XPO6 couple that state to mRNA processing and nuclear export. ATR, PLK1, SMG6, chromatin regulators and RNA surveillance factors may connect the transcriptional and RNA-processing state to replication stress, cell-cycle state and transcript quality control. This is a mechanistic model rather than proof of physical coupling; testing it would require perturbation of selected nucleolar and export components followed by measurement of rRNA maturation, mRNA export, proliferation and cell-state composition in colon and skin models.

### Important genes

#### DCAF13

- **Related proteins** (co-abundance neighbors): UTP11 (0.87), ACTR8 (0.85), WDR3 (0.81), RMP64 (0.81), WDR36 (0.80), USP36 (0.80), DDX52 (0.80); STRING partners: DDX52 (0.946), DHX37 (0.971), HEATR1 (0.997), NOL11 (0.968), PUM3 (0.865), RCL1 (0.993), UTP11 (0.998), UTP20 (0.998), WDR3 (0.999), WDR36 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DDB1 and CUL4 associated factor 13. Enables estrogen receptor binding activity. Predicted to be involved in maturation of SSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Located in several cellular components, including centrosome; cytosol; and nuclear lumen. Part of Cul4-RING E3 ubiquitin ligase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.285); acute tonsillitis (0.133); breast cancer (0.105); breast carcinoma (0.099); hepatocellular carcinoma (0.087)
- **Europe PMC papers**: 311
- **Why important**: DCAF13 is a central connector of the nucleolar core in the module and has strong STRING relationships with DDX52, DHX37, HEATR1, NOL11, RCL1, UTP11, UTP20, WDR3 and WDR36. It appears across the core global terms for rRNA processing, ribosome biogenesis, preribosome and small-subunit maturation (5 globally significant GO/KEGG terms, q_global 1.69e-09–1.56e-08; see the table), (GO:BP ribosomal small subunit biogenesis; q_global = 4.73e-07), (GO:CC preribosome; q_global = 8.37e-07), (GO:BP maturation of SSU-rRNA; q_global = 5.49e-06), (GO:CC small-subunit processome; q_global = 5.49e-06). Its annotation places it in the CUL4-associated ubiquitin-ligase system and in SSU-rRNA maturation, providing a possible regulatory bridge between protein turnover and nucleolar assembly. It has a substantial literature and disease-oriented associations including neurodegenerative and cancer-related entries.
- **Conclusion**: Established evidence supports DCAF13 as a core nucleolar ribosome-biogenesis component and a high-confidence network connector. It is plausible, but not established here, that its ubiquitin-ligase association regulates the abundance or assembly of other module proteins.

#### UTP11

- **Related proteins** (co-abundance neighbors): DCAF13 (0.87), RCL1 (0.87), THOC2 (0.85), PUM3 (0.83), CPSF1 (0.83), UTP20 (0.83), THOC1 (0.83), CPSF2 (0.82), ACTR8 (0.81); STRING partners: DCAF13 (0.998), DDX52 (0.936), DHX37 (0.974), HEATR1 (0.997), NOL11 (0.967), RCL1 (0.993), RRP1B (0.763), UTP20 (0.998), WDR3 (0.996), WDR36 (0.998)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UTP11 small subunit processome component. Enables RNA binding activity. Involved in nervous system development and positive regulation of apoptotic process. Located in cytoplasm; extracellular space; and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: alcohol drinking (0.160); stroke disorder (0.135); ocular hypotension (0.096); neoplasm (0.083); coronary artery disorder (0.080)
- **Europe PMC papers**: 109
- **Why important**: UTP11 is among the more connected genes in the co-abundance network and is linked by STRING to much of the nucleolar processing machinery, including DCAF13, DDX52, DHX37, HEATR1, NOL11, RCL1, RRP1B, UTP20, WDR3 and WDR36. It is represented across nearly all central global terms, including ribonucleoprotein-complex biogenesis, ribosome biogenesis, rRNA processing, SSU maturation and the nucleolus (5 globally significant GO/KEGG terms, q_global 1.69e-09–1.56e-08; see the table), (GO:BP ribosomal small subunit biogenesis; q_global = 4.73e-07), (GO:BP maturation of SSU-rRNA; q_global = 5.49e-06), (GO:CC small-subunit processome; q_global = 5.49e-06). Its annotation identifies it as a small-subunit processome component and RNA-binding protein, while its expression is detected in both colon and skin.
- **Conclusion**: Established evidence makes UTP11 a strong marker of the module's small-subunit processome and nucleolar identity. The co-abundance data support coordinated regulation with the processome, but do not establish that UTP11 is the causal driver of the cross-tissue module.

#### WDR3

- **Related proteins** (co-abundance neighbors): USP36 (0.83), NOL11 (0.82), DCAF13 (0.81), RCL1 (0.80); STRING partners: DCAF13 (0.999), DHX37 (0.892), HEATR1 (0.999), NOL11 (0.951), NOM1 (0.986), POLR3A (0.78), PUM3 (0.905), RCL1 (0.998), RRP1B (0.796), UTP11 (0.996), UTP20 (0.999), WDR36 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 3. This gene encodes a nuclear protein containing 10 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, which usually include a trp-asp at the C-terminal end. Proteins belonging to the WD repeat family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. [provid…
- **Diseases (Open Targets)**: presbycusis (0.335); respiratory tract infectious disorder (0.184); neurodegenerative disease (0.143); preeclampsia (0.120); alcohol drinking (0.098)
- **Europe PMC papers**: 280
- **Why important**: WDR3 is a nucleolar WD-repeat protein with strong STRING connectivity to DCAF13, DHX37, HEATR1, NOL11, NOM1, RCL1, UTP11, UTP20, WDR36 and related factors. It is included in the global evidence for rRNA metabolism, rRNA processing, ribosome biogenesis, preribosome and small-subunit processome functions (5 globally significant GO/KEGG terms, q_global 1.69e-09–1.56e-08; see the table), (GO:BP ribosomal small subunit biogenesis; q_global = 4.73e-07), (GO:CC preribosome; q_global = 8.37e-07), (GO:CC small-subunit processome; q_global = 5.49e-06). Its WD-repeat architecture is consistent with assembly of multiprotein complexes, and its HPA localization is nucleolar. It also has disease associations including open-angle glaucoma and respiratory or neurodegenerative disease categories.
- **Conclusion**: Established evidence supports WDR3 as a nucleolar assembly factor within the known rRNA-processing network. Its position makes it a useful candidate for testing whether perturbing processome organization changes the shared colon–skin co-abundance state.

#### THOC1

- **Related proteins** (co-abundance neighbors): UTP11 (0.83), ACTR8 (0.82), KLHL7 (0.81), NOL11 (0.81); STRING partners: THOC2 (0.999), THOC5 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in colon, skin
- **hu.MAP 3.0**: huMAP3_04932.1, huMAP3_12548.1, huMAP3_09101.1, huMAP3_10299.1, huMAP3_10789.1, huMAP3_09943.1, huMAP3_08963.1, huMAP3_02771.1, huMAP3_09583.1, huMAP3_02553.1, huMAP3_07273.1, huMAP3_08233.1, huMAP3_08111.1
- **Function (MyGene.info)**: THO complex subunit 1. HPR1 is part of the TREX (transcription/export) complex, which includes TEX1 (MIM 606929), THO2 (MIM 300395), ALY (MIM 604171), and UAP56 (MIM 142560).[supplied by OMIM, Nov 2010]
- **Diseases (Open Targets)**: neurodegenerative disease (0.409); hearing loss, autosomal dominant 86 (0.362); alcohol drinking (0.231); urolithiasis (0.231); immune system disorder (0.226)
- **Europe PMC papers**: 804
- **Why important**: THOC1 links the module's RNA-processing core to transcript export. It belongs to the THO/TREX transcription-export machinery, is connected in STRING to THOC2 and THOC5, and is repeatedly represented in hu.MAP THO complexes (hu.MAP huMAP3_04932.1), (hu.MAP huMAP3_12548.1) (hu.MAP huMAP3_09101.1) (hu.MAP huMAP3_10299.1) (hu.MAP huMAP3_10789.1) (hu.MAP huMAP3_11232.1) (hu.MAP huMAP3_09943.1) (hu.MAP huMAP3_08963.1) (hu.MAP huMAP3_02771.1) (hu.MAP huMAP3_09583.1) (hu.MAP huMAP3_02553.1) (hu.MAP huMAP3_07273.1) (hu.MAP huMAP3_08233.1). It contributes to the globally corrected terms for RNA processing, nuclear export, mRNA export, RNA localization and the transcription-export complex (GO:BP RNA processing; q_global = 1.56e-07), (GO:BP nuclear export; q_global = 0.00256), (GO:BP RNA export from nucleus; q_global = 0.012), (6 globally significant GO/KEGG terms, q_global 0.0244–0.0416; see the table). Its protein is detected in both colon and skin, and it has a substantial literature with associations including neurodegenerative, hearing and immune-system disorders.
- **Conclusion**: Established evidence supports THOC1 as a bona fide mRNA-export and transcription-export component that explains the module's connection beyond the nucleolus. Its co-abundance with ribosome-biogenesis genes is consistent with coordinated RNA supply and use, but the direction of regulation is unresolved.

#### NUP98

- **Related proteins** (co-abundance neighbors): USP36 (0.85), KLHL7 (0.83), RRP1B (0.81); STRING partners: NUP107 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07705.1, huMAP3_09710.1, huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 98 and 96 precursor. Nuclear pore complexes (NPCs) regulate the transport of macromolecules between the nucleus and cytoplasm, and are composed of many polypeptide subunits, many of which belong to the nucleoporin family. This gene belongs to the nucleoporin gene family and encodes a 186 kDa precursor protein that undergoes autoproteolytic cleavage to generate a 98 kDa nucleoporin and 96 kDa nucleoporin. The 98 kDa nu…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); acute myeloid leukemia (0.399); lung carcinoma (0.376)
- **Europe PMC papers**: 4839
- **Why important**: NUP98 represents the nuclear-pore and nucleocytoplasmic-transport arm of the module. It pairs strongly with NUP107 in STRING and occurs in hu.MAP nuclear-pore complexes (hu.MAP huMAP3_07705.1), (hu.MAP huMAP3_09710.1), (hu.MAP huMAP3_12581.1). It contributes to the globally corrected evidence for nuclear export, mRNA export, RNA localization and nucleocytoplasmic transport (GO:BP nuclear export; q_global = 0.00256), (GO:BP RNA export from nucleus; q_global = 0.012), (GO:BP establishment of RNA localization; q_global = 0.0269) (GO:BP mRNA export from nucleus; q_global = 0.0371) (KEGG Nucleocytoplasmic transport - Homo sapiens (human); q_global = 0.0387). Its established functions include RNA export, protein import, nuclear-pore organization and peripheral gene tethering. NUP98 also has a very substantial literature and disease associations involving viral infection and leukemia.
- **Conclusion**: Established evidence supports NUP98 as the module's nuclear-pore transport representative and as a mechanistic link between nuclear RNA production and cytoplasmic delivery. The module does not establish whether altered transport is primary or simply tracks broader nuclear activity.

## Module 12

**Tissue pair**: colon and skin  
**Genes (9)**: CEP250, ITPR2, PHF3, RBM28, RBM34, RNF5, POLR3E, SUGP1, TRPS1

### Function

No GO or KEGG term passed global correction, so there is no statistically supported pathway-level functional assignment from enrichment analysis. The module is instead a sparse co-abundance network centered on TRPS1, a transcriptional repressor, with connections to genes involved in RNA biology, centrosome organization, calcium signaling, RNA polymerase III function, and ER-associated ubiquitination. The mixed annotation profile does not support treating the module as a single established biochemical pathway. A cautious interpretation is a coordinated cellular-state module involving transcriptional regulation and RNA or protein homeostasis, with possible contributions from intracellular calcium signaling and cell-structure regulation. These are functional interpretations of the constituent genes, not globally significant enrichment claims.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of the genes is annotated as secreted. Most genes have low tissue specificity, while the tissue-enhanced annotations are distributed across liver, skeletal muscle, and breast rather than being concentrated in colon or skin. Most genes show cell-type-enhanced expression, including several neural or glial cell types, but the module is not strongly blood-cell enriched because most genes have low immune-cell specificity and only a minority show immune-cell enhancement. Protein detection is widespread in both colon and skin, although TRPS1 is detected in skin and not detected in colon. Overall, the shared module could reflect broadly present cellular programs or shared cell-type composition rather than a colon-skin-specific secreted or blood-derived program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship among module members is the RBM28–RBM34 pair. This supports a known connection between two nucleolar or RNA-associated proteins, but it does not establish a physical interaction network for the whole module. The remaining co-abundance edges, including the central connections of TRPS1, are not supported by the reported high-confidence STRING partner data. No hu.MAP complex contains multiple module members. Thus, the network appears to combine one known RNA-related relationship with tissue-level co-abundance associations that may arise from shared regulation, cell composition, or indirect biology rather than one canonical protein complex.

**STRING interactions (score >= 0.7)**: 1 of 36 gene pairs: RBM28–RBM34 (0.975)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be called a definitively new biological discovery. Its sparse STRING support and lack of a shared hu.MAP complex indicate that it is not an obvious reconstruction of a known multiprotein complex, but database absence alone cannot demonstrate novelty. The strongest defensible claim is that this particular conserved colon-skin co-abundance configuration, especially the centrality of TRPS1 and its links to otherwise diverse genes, may represent a hypothesis-generating association that requires independent validation. Replication in additional cohorts, control for cell composition, and experimental or orthogonal molecular interaction evidence would be needed before assigning novelty or a new mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program in which TRPS1-associated transcriptional regulation is co-varying with RNA maturation or processing, RNA polymerase activity, centrosome or cilium biology, ER protein quality control, and intracellular calcium signaling. The RBM28–RBM34 relationship may represent a nucleolar RNA-processing component, while the other edges may be indirect or driven by coordinated expression in particular cell populations. ITPR2-mediated calcium signaling and RNF5-mediated ER ubiquitination could provide links between cellular signaling, protein homeostasis, and changes in transcriptional or RNA-processing state. This hypothesis is not established by global enrichment, because no GO or KEGG term passed global correction.

### Important genes

#### TRPS1

- **Related proteins** (co-abundance neighbors): RNF5 (0.85), RBM28 (0.83), RBM34 (0.82), ITPR2 (0.82), POLR3E (0.81), SUGP1 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transcriptional repressor GATA binding 1. This gene encodes a transcription factor that represses GATA-regulated genes and binds to a dynein light chain protein. Binding of the encoded protein to the dynein light chain protein affects binding to GATA consensus sequences and suppresses its transcriptional activity. Defects in this gene are a cause of tricho-rhino-phalangeal syndrome (TRPS) types I-III. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: trichorhinophalangeal syndrome type I or III (0.825); Treacher-Collins syndrome (0.561); hereditary disease (0.538); Abnormality of the skeletal system (0.537); trichorhinophalangeal syndrome type II (0.525)
- **Europe PMC papers**: 2072
- **Why important**: TRPS1 is the network hub, connecting to the greatest number of module members and having the strongest weighted position in the subgraph. It is a transcriptional repressor with annotations for regulation of RNA polymerase II transcription, skeletal development, and chondrocyte differentiation. It also has the largest literature volume among the selected genes and strong disease associations with trichorhinophalangeal syndromes and skeletal abnormalities. Its breast-enriched HPA annotation and detection in skin, but not colon, make it especially relevant to interpreting tissue and cell-composition effects.
- **Conclusion**: Established evidence supports TRPS1 as the principal network-organizing gene and a transcriptional regulator with skeletal and developmental disease relevance. It is reasonable to hypothesize that TRPS1-related regulation contributes to the module, but the co-abundance network does not prove that TRPS1 regulates the other module genes or explains the shared colon-skin signal.

#### RBM28

- **Related proteins** (co-abundance neighbors): TRPS1 (0.83); STRING partners: RBM34 (0.975)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 28. The protein encoded by this gene is a specific nucleolar component of the spliceosomal small nuclear ribonucleoprotein (snRNP)complexes . It specifically associates with U1, U2, U4, U5, and U6 small nuclear RNAs (snRNAs), possibly coordinating their transition through the nucleolus. Mutation in this gene causes alopecia, progressive neurological defects, and endocrinopathy (ANE syndrome), a pleiot…
- **Diseases (Open Targets)**: ANE syndrome (0.643); neurodegenerative disease (0.472); microcephaly (0.111); cancer (0.076); colorectal carcinoma (0.075)
- **Europe PMC papers**: 337
- **Why important**: RBM28 is part of the only high-confidence STRING relationship reported within the module, pairing with RBM34. It is a nucleolar spliceosomal small nuclear RNA-associated protein and is linked to ANE syndrome, progressive neurological disease, and endocrinopathy. Its protein is detected in both colon and skin, and its nucleolar localization provides a plausible RNA-processing component to the module.
- **Conclusion**: Established evidence supports RBM28 as a nucleolar RNA-processing factor and as a known interaction partner of RBM34. Its participation in the broader module mechanism remains a hypothesis because the other module connections are co-abundance relationships rather than demonstrated physical interactions.

#### RBM34

- **Related proteins** (co-abundance neighbors): TRPS1 (0.82), CEP250 (0.80); STRING partners: RBM28 (0.975)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 34. This gene encodes a member of the RNA-binding motif family of RNA recognition motif proteins. The encoded protein contains an RNA-binding domain made up of two RNA recognition motif subdomains referred to as RNA recognition motif-1 and RNA recognition motif-2. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2016].
- **Diseases (Open Targets)**: neurodegenerative disease (0.334); hepatocellular carcinoma (0.076); neoplasm (0.075); nervous system benign neoplasm (0.069); alcohol drinking (0.067)
- **Europe PMC papers**: 154
- **Why important**: RBM34 is the other member of the sole high-confidence STRING pair and is annotated as an RNA-binding protein involved in maturation of large-subunit ribosomal RNA. It is detected in both colon and skin and occupies a nucleolar location. Its co-abundance connections to TRPS1 and CEP250 may connect RNA biology to transcriptional or centrosomal cellular state, although those relationships are not independently established as physical interactions.
- **Conclusion**: Established evidence supports RBM34 as an RNA-binding and nucleolar rRNA-maturation factor that is connected to RBM28 in STRING. A role linking RNA maturation to the TRPS1-centered module is plausible but remains unproven and should not be presented as a demonstrated pathway.

#### ITPR2

- **Related proteins** (co-abundance neighbors): TRPS1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum, Mid piece; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inositol 1,4,5-trisphosphate receptor type 2. The protein encoded by this gene belongs to the inositol 1,4,5-triphosphate receptor family, whose members are second messenger intracellular calcium release channels. These proteins mediate a rise in cytoplasmic calcium in response to receptor activated production of inositol triphosphate. Inositol triphosphate receptor-mediated signaling is involved in many processes including cell migration, ce…
- **Diseases (Open Targets)**: isolated anhidrosis with normal sweat glands (0.547); alcohol drinking (0.428); atrial fibrillation (0.394); open-angle glaucoma (0.365); familial hypercholesterolemia (0.333)
- **Europe PMC papers**: 1988
- **Why important**: ITPR2 encodes an intracellular calcium-release channel and is annotated for calcium transport, calcium-mediated signaling, signal transduction, and responses to hypoxia. It is tissue-enhanced in liver and cell-type-enhanced in several specialized epithelial or immune-associated cell types, while its protein is detected in both colon and skin. Its connection to the TRPS1 hub gives the module a signaling component distinct from the nucleolar genes.
- **Conclusion**: Established evidence supports ITPR2 as a calcium-signaling component with broad cellular roles and relevant cell-type variation. Its relationship to TRPS1 and the shared tissue module is an association only; the hypothesis that calcium signaling helps coordinate the module requires validation.

#### RNF5

- **Related proteins** (co-abundance neighbors): TRPS1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ring finger protein 5. The protein encoded by this gene contains a RING finger, which is a motif known to be involved in protein-protein interactions. This protein is a membrane-bound ubiquitin ligase. It can regulate cell motility by targeting paxillin ubiquitination and altering the distribution and localization of paxillin in cytoplasm and cell focal adhesions. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: cystic fibrosis (0.481); neoplasm (0.105); breast cancer (0.084); breast carcinoma (0.084); melanoma (0.082)
- **Europe PMC papers**: 1109
- **Why important**: RNF5 is an ER membrane-bound ubiquitin ligase annotated for protein ubiquitination, ER-associated degradation, transmembrane transport, and regulation of cell motility through paxillin ubiquitination. It is detected in both colon and skin and connects directly to the TRPS1 hub in the module. Its substantial literature volume and disease associations involving cystic fibrosis and cancer make it an informative candidate for protein-homeostasis and cell-behavior interpretations.
- **Conclusion**: Established evidence supports RNF5 as an ER ubiquitination and protein-quality-control regulator with effects on cell motility. Its placement next to TRPS1 suggests coordinated cellular-state biology, but there is no evidence here that RNF5 physically interacts with TRPS1 or mechanistically drives the module.

## Module 13

**Tissue pair**: colon and skin  
**Genes (9)**: CWC22, GULP1, INTS13, METTL16, POLR3B, ATP6V0A1, ZCCHC3, ZNF106, ZNF598

### Function

The strongest functional interpretation is RNA biogenesis and processing, centered on snRNA metabolism (GO:BP snRNA metabolic process; q_global = 0.0451). The globally supported term (GO:BP snRNA metabolic process; q_global = 0.0451) includes INTS13, METTL16, and POLR3B. This is biologically coherent with POLR3B-mediated transcription of small RNAs, METTL16-mediated RNA modification and processing, CWC22 participation in spliceosome-associated mRNA splicing, and ZNF106 RNA-binding activity. Additional functions represented by individual genes include translation quality control through ZNF598, antiviral RNA sensing through ZCCHC3, intracellular organelle acidification through ATP6V0A1, apoptotic-cell engulfment through GULP1, and cell-cycle or spindle regulation through INTS13. These individual annotations should be treated as supporting context rather than evidence for additional module-level enrichment. The module is therefore best described as a small RNA-processing and nuclear RNA-homeostasis module with links to vesicular and quality-control biology.

**Cell composition.** This does not appear to be a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. The genes are predominantly broadly expressed or low in tissue specificity, and the proteins are detected in both colon and skin for most genes with available data. The HPA evidence does not support a strong blood-cell explanation: most genes have low immune-cell specificity, some are not detected in immune cells, and only ZNF106 is immune-cell enhanced, with neutrophil enrichment. Tissue or cell-type enhancements are scattered across diverse cell types and tissues rather than concentrated in one shared lineage. Thus, blood contamination or a shared secreted compartment is not the leading explanation, although cellular composition and broadly expressed housekeeping-like RNA-processing activity may contribute to the conserved co-abundance pattern.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP snRNA metabolic process | 0.0451 | INTS13, METTL16, POLR3B |

### STRING and hu.MAP

No high-confidence STRING interactions are reported among the module genes, and STRING functional enrichment is absent. Consequently, the co-abundance edges should not be presented as established physical interactions. Two hu.MAP complexes, (hu.MAP huMAP3_12918.1) and (hu.MAP huMAP3_12394.1), independently contain the pair GULP1 and ZNF106, while the remaining complex members are largely proteins involved in endocytosis, vesicle trafficking, and adaptor-mediated membrane transport. This provides limited external support for a relationship between GULP1 and ZNF106 in large multifunctional complexes, but the low representation of the module within those complexes means it does not establish a complete module complex. The network itself is sparse and structured around GULP1 and ZNF106: GULP1 has the strongest connectivity, ZNF106 is the next most connected node, and the other genes form short links to these hubs or to each other. The absence of STRING support contrasts with the hu.MAP pair evidence and argues for cautious interpretation of the network as a co-abundance structure rather than a validated protein complex.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12918.1 (ZNF106, GULP1; 2/62); huMAP3_12394.1 (ZNF106, GULP1; 2/98)

### Novelty

The module may be a novel tissue-conserved co-abundance pattern, but the available evidence is insufficient to call it a newly discovered molecular complex or pathway. Its novelty is supported by the specific combination of genes and by the absence of high-confidence STRING connectivity, while the globally significant snRNA-metabolism signal gives the pattern a coherent biological interpretation. However, lack of STRING annotation alone does not prove novelty, because sparse modules can contain indirect, condition-dependent, tissue-dependent, or poorly characterized relationships. The overlap of GULP1 and ZNF106 with hu.MAP complexes (hu.MAP huMAP3_12918.1) and (hu.MAP huMAP3_12394.1) also indicates that at least part of the biology is already represented in existing interaction resources. The defensible conclusion is that this is a potentially novel conserved co-abundance arrangement, not proof of a novel molecular mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated RNA and protein homeostasis in colon and skin cells. A nuclear RNA-processing arm may couple POLR3B, METTL16, CWC22, INTS13, and ZNF106 to production, modification, splicing, and regulation of small or other cellular RNAs. GULP1, ATP6V0A1, ZCCHC3, and ZNF598 may connect this core to vesicular trafficking, organelle acidification, innate RNA surveillance, and ribosome-quality control. The co-abundance pattern could therefore arise from a shared cellular state requiring enhanced RNA processing together with endolysosomal and proteostasis capacity. This is a mechanistic hypothesis, not an experimentally established interaction map.

### Important genes

#### GULP1

- **Related proteins** (co-abundance neighbors): POLR3B (0.87), ZCCHC3 (0.84), ATP6V0A1 (0.81), METTL16 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in colon, skin
- **hu.MAP 3.0**: huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: GULP PTB domain containing engulfment adaptor 1. The protein encoded by this gene is an adapter protein necessary for the engulfment of apoptotic cells by phagocytes. Several transcript variants, some protein coding and some thought not to be protein coding, have been found for this gene. [provided by RefSeq, Nov 2011].
- **Diseases (Open Targets)**: smoking initiation (0.419); intracranial hemorrhage (0.308); ovarian dysfunction (0.270); alcohol drinking (0.250); urolithiasis (0.250)
- **Europe PMC papers**: 573
- **Why important**: GULP1 is the principal network hub, connecting to POLR3B, ZCCHC3, ATP6V0A1, and METTL16. It is detected in colon and skin, is localized to vesicles, and has an established role as an adaptor for apoptotic-cell engulfment by phagocytes. It is also the only module hub shared by both hu.MAP complexes (hu.MAP huMAP3_12918.1) and (hu.MAP huMAP3_12394.1), although those complexes are broad and multifunctional. Its literature base is substantial relative to most genes in the module.
- **Conclusion**: Established evidence supports GULP1 as the structural center of the co-abundance network and as a vesicular engulfment adaptor. Its connection to the RNA-processing genes is a module-level association rather than a demonstrated physical mechanism. A possible role linking vesicle-mediated clearance to RNA or proteostasis responses remains hypothetical.

#### POLR3B

- **Related proteins** (co-abundance neighbors): GULP1 (0.87), CWC22 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase III subunit B. This gene encodes the second largest subunit of RNA polymerase III, the polymerase responsible for synthesizing transfer and small ribosomal RNAs in eukaryotes. The largest subunit and the encoded protein form the catalytic center of RNA polymerase III. Mutations in this gene are a cause of hypomyelinating leukodystrophy. Alternatively spliced transcript variants encoding multiple isoforms have be…
- **Diseases (Open Targets)**: hypomyelination-hypogonadotropic hypogonadism-hypodontia syndrome (0.796); leukodystrophy, hypomyelinating, 8, with or without oligodontia and/or hypogonadotropic hypogonadism (0.747); Charcot-Marie-Tooth disease, demyelinating, IIA 1I (0.729); POLR-related leukodystrophy (0.707); POLR3B-related disorder (0.575)
- **Europe PMC papers**: 587
- **Why important**: POLR3B is one of the three genes in the only globally supported enrichment term, snRNA metabolic process (GO:BP snRNA metabolic process; q_global = 0.0451). It encodes a catalytic-center subunit of RNA polymerase III and is connected in the module to GULP1 and CWC22. It has substantial literature and well-established disease associations involving hypomyelinating leukodystrophy and related POLR3B disorders, making it an informative anchor for the module's RNA-biology interpretation.
- **Conclusion**: Established evidence identifies POLR3B as a core small-RNA transcription component and a direct contributor to the module-level (GO:BP snRNA metabolic process; q_global = 0.0451) signal. Its network links do not establish a physical interaction with GULP1 or CWC22, and any proposed coupling of polymerase activity to vesicular biology is hypothetical.

#### METTL16

- **Related proteins** (co-abundance neighbors): GULP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methyltransferase 16, RNA N6-adenosine. Enables RNA binding activity and RNA methyltransferase activity. Involved in RNA modification and regulation of mRNA metabolic process. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.352); vitiligo (0.160); hepatocellular carcinoma (0.112); colorectal carcinoma (0.108); neoplasm (0.107)
- **Europe PMC papers**: 2452
- **Why important**: METTL16 is also part of the globally supported snRNA-metabolism term (GO:BP snRNA metabolic process; q_global = 0.0451) and is connected to the hub GULP1. It is an RNA-binding methyltransferase involved in RNA modification and mRNA processing, with a large literature base and disease-oriented associations including colorectal carcinoma and vitiligo. Its functional annotation provides a mechanistic bridge from RNA production to post-transcriptional RNA regulation.
- **Conclusion**: Established evidence supports METTL16 as a major functional contributor to the RNA-processing interpretation and to (GO:BP snRNA metabolic process; q_global = 0.0451). The network places it next to GULP1, but no STRING relationship is reported; therefore, a direct METTL16–GULP1 pathway in colon or skin is a hypothesis rather than an established finding.

#### ZNF106

- **Related proteins** (co-abundance neighbors): INTS13 (0.86), ZNF598 (0.82), CWC22 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoli; IHC detected in colon, skin
- **hu.MAP 3.0**: huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: zinc finger protein 106. Enables RNA binding activity. Predicted to be involved in insulin receptor signaling pathway. Predicted to be located in nuclear speck and nucleolus. Predicted to be active in cytosol and membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: urethritis (0.352); hyperaldosteronism (0.191); benign neoplasm of eye (0.179); preeclampsia (0.179); Complete right bundle branch block (0.178)
- **Europe PMC papers**: 130
- **Why important**: ZNF106 is the second major network hub, linked to INTS13, ZNF598, and CWC22, and it shares hu.MAP complexes (hu.MAP huMAP3_12918.1) and (hu.MAP huMAP3_12394.1) with GULP1. It has RNA-binding annotation, nucleolar localization, and tissue or cell-type enrichment that includes muscle-related tissues, melanocytes, myonuclei, choroid plexus epithelial cells, and neutrophils. Its literature volume is more limited than that of METTL16 or POLR3B, so it may be especially informative as a potentially undercharacterized connector.
- **Conclusion**: Established evidence supports ZNF106 as a central co-abundance node with RNA-related annotation and membership in two hu.MAP complexes. The scattered HPA enrichments do not establish a shared cell type for colon and skin, and its proposed role as the bridge between RNA processing and vesicular-complex biology remains hypothetical.

#### CWC22

- **Related proteins** (co-abundance neighbors): ZNF106 (0.81), POLR3B (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in colon, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CWC22 spliceosome associated protein. Enables RNA binding activity. Involved in mRNA splicing, via spliceosome. Located in cytosol and nuclear speck. Part of U2-type catalytic step 1 spliceosome; U2-type catalytic step 2 spliceosome; and U2-type precatalytic spliceosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.507); dengue disease (0.370); prostate carcinoma (0.330); mathematical ability (0.328); lagophthalmos (0.321)
- **Europe PMC papers**: 406
- **Why important**: CWC22 links ZNF106 and POLR3B in the network and has established spliceosome-associated mRNA-splicing functions, including participation in spliceosomal complexes. It is detected in both colon and skin, has low tissue and cell-type specificity, and provides a focused mechanistic connection between the module's RNA-processing genes. Its literature volume is substantial, supporting a well-established molecular function even though it lacks STRING or hu.MAP representation within this module.
- **Conclusion**: Established evidence supports CWC22 as a spliceosome-associated RNA-processing factor and as a plausible connector between the ZNF106 and POLR3B portions of the network. Its module edges are co-abundance relationships rather than validated physical interactions, so any coordinated pathway involving CWC22 and the other module genes remains a hypothesis.
