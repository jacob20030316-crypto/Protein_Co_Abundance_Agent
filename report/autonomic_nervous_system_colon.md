# Conserved co-abundance modules: autonomic_nervous_system and colon

## Module 0

**Tissue pair**: autonomic_nervous_system and colon  
**Genes (25)**: AATF, CPSF2, CWC22, GABPA, KIF14, LEO1, MAD1L1, NOL11, NSMCE3, NUP205, NUP93, PAXBP1, PSPC1, RSL1D1, RNPC3, RRS1, SETDB1, SMARCAD1, SRRT, TCERG1, UTP15, UTP4, VAMP4, VPS13C, WDR33

### Function

The strongest interpretation is a nuclear RNA-processing module with a particularly coherent ribosomal small-subunit biogenesis component. The globally corrected evidence supports ribosomal small-subunit biogenesis (GO:BP ribosomal small subunit biogenesis; q_global = 0.0217) and RNA processing (GO:BP RNA processing; q_global = 0.0232). The module therefore appears to couple nucleolar ribosome production with broader processing of pre-messenger RNA, including splicing and messenger-RNA maturation. Supplementary STRING evidence independently points to nuclear and nucleolar localization, RNA processing, transcription regulation, capped intron-containing pre-messenger-RNA processing, and the t-UTP complex (10 supplementary STRING terms; within-query FDR 3.73e-05–0.0407). The network is not a single uniform complex: it contains a nucleolar t-UTP/ribosome-biogenesis group, an RNA-splicing and three-prime-end-processing group, a nuclear-pore pair, and additional chromatin, mitotic, and vesicle-associated links. Thus, the most defensible function is coordinated nuclear RNA maturation and ribosome biogenesis, rather than a tissue-specific autonomic or colonic pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It is also not strongly blood-cell enriched: most genes have low immune-cell specificity, several are not detected in immune cells, and no enriched blood-cell category is reported. Most genes have low tissue specificity, while a smaller subset is tissue enhanced in bone marrow or lymphoid tissue and several show cell-type enhancement in renal, reproductive, cardiac, intestinal proliferative, or related cell types. Protein detection in colon is reported for most assessed genes, whereas there is no matching HPA tissue for autonomic nervous system. The shared signal is therefore more consistent with broadly expressed nuclear machinery, with possible contributions from proliferative or cell-type composition differences, than with a blood or secreted-protein artifact. HPA expression alone does not establish that the module is specific to either tissue.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP ribosomal small subunit biogenesis | 0.0217 | AATF, NOL11, RRS1, UTP15, UTP4 |
| GO:BP RNA processing | 0.0232 | CPSF2, CWC22, LEO1, NOL11, PAXBP1, RNPC3, RRS1, SRRT, TCERG1, UTP15, UTP4, WDR33 |

### STRING and hu.MAP

STRING provides direct high-confidence support for several internal relationships. The strongest coherent group links AATF, NOL11, UTP15, UTP4, RSL1D1, and RRS1 around nucleolar and ribosome-biogenesis functions; CPSF2 connects with WDR33 in messenger-RNA three-prime-end processing; CWC22 connects with SRRT and SRRT connects with TCERG1 in RNA processing; and NUP93 connects with NUP205 in the nuclear pore. RNPC3 is a highly connected bridge in the module subgraph, but it has no listed STRING partner in this result, so its module connectivity should not be equated with a known direct physical interaction. hu.MAP independently recovers UTP15, UTP4, and NOL11 in small-subunit-processome or exosome-associated complexes (hu.MAP huMAP3_01743.1), (hu.MAP huMAP3_14264.1), and (hu.MAP huMAP3_14364.1); NUP93 and NUP205 in nuclear-pore-related complexes (hu.MAP huMAP3_07789.1), (hu.MAP huMAP3_05673.1), and (hu.MAP huMAP3_09042.1); WDR33 and CPSF2 in cleavage and polyadenylation complexes (hu.MAP huMAP3_00102.1) (hu.MAP huMAP3_15022.1) (hu.MAP huMAP3_09096.1) (hu.MAP huMAP3_11757.1); RNPC3 and PAXBP1 in spliceosomal complexes (hu.MAP huMAP3_04549.1), (hu.MAP huMAP3_06511.1), and (hu.MAP huMAP3_08980.1); and SRRT with CWC22 in a broad RNA-processing complex (hu.MAP huMAP3_09943.1). These results show that important portions of the module recapitulate known molecular machinery. They support biological coherence, but they do not prove that all module edges are physical interactions or that the entire module is one stable complex.

**STRING interactions (score >= 0.7)**: 15 of 300 gene pairs: AATF–NOL11 (0.811); AATF–RSL1D1 (0.986); AATF–UTP15 (0.994); AATF–UTP4 (0.997); CPSF2–WDR33 (0.999); CWC22–SRRT (0.855); NOL11–UTP15 (0.986); NOL11–UTP4 (0.999); NUP205–NUP93 (0.999); RRS1–RSL1D1 (0.992); RRS1–UTP4 (0.739); RSL1D1–UTP15 (0.924); RSL1D1–UTP4 (0.996); SRRT–TCERG1 (0.839); UTP15–UTP4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Nucleus (FDR = 3.73e-05, 23 genes); COMPARTMENTS Nuclear lumen (FDR = 0.00056, 17 genes); Process RNA processing (FDR = 0.0076, 13 genes); Keyword Transcription regulation (FDR = 0.0116, 10 genes); COMPARTMENTS t-UTP complex (FDR = 0.0272, 3 genes); COMPARTMENTS Fibrillar center (FDR = 0.0356, 5 genes); RCTM Processing of Capped Intron-Containing Pre-mRNA (FDR = 0.038, 8 genes); RCTM Metabolism of RNA (FDR = 0.038, 11 genes); COMPARTMENTS Nucleus (FDR = 0.0407, 20 genes); COMPARTMENTS Nucleolus (FDR = 0.0407, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01743.1 (UTP15, UTP4, NOL11; 3/6); huMAP3_14264.1 (UTP15, UTP4, NOL11; 3/20); huMAP3_14364.1 (UTP4, NOL11; 2/4); huMAP3_07789.1 (NUP93, NUP205; 2/7); huMAP3_05673.1 (NUP93, NUP205; 2/11); huMAP3_00102.1 (WDR33, CPSF2; 2/12); huMAP3_15022.1 (WDR33, CPSF2; 2/12); huMAP3_09096.1 (WDR33, CPSF2; 2/15); huMAP3_11757.1 (WDR33, CPSF2; 2/16); huMAP3_09042.1 (NUP93, NUP205; 2/26); huMAP3_04549.1 (RNPC3, PAXBP1; 2/52); huMAP3_09943.1 (SRRT, CWC22; 2/78); huMAP3_06511.1 (RNPC3, PAXBP1; 2/79); huMAP3_08980.1 (RNPC3, PAXBP1; 2/97)

### Novelty

The module should not be claimed as a wholly new molecular pathway. Its central components and several relationships are already represented in STRING and hu.MAP, and the globally significant annotations correspond to established ribosome-biogenesis and RNA-processing biology. The potentially novel finding is the tissue-pair co-abundance organization: known nucleolar, spliceosomal, nuclear-pore, and transcript-processing components appear together as a conserved module across autonomic nervous system and colon. Whether that cross-tissue co-abundance pattern is new cannot be established from the fact sheet alone. Absence of some genes or edges from STRING or hu.MAP is not evidence of novelty. A defensible novelty claim would require comparison with published co-abundance modules, tissue-specific expression studies, and independent cohorts, followed by replication of the cross-tissue association.

**Hypothesis.** Hypothesis: variation in a shared nuclear RNA-production state coordinates nucleolar ribosome assembly with pre-messenger-RNA splicing, transcript three-prime-end processing, and nuclear transport in autonomic nervous system and colon samples. The t-UTP and small-subunit-processome components could represent the nucleolar core, while spliceosomal, cleavage-and-polyadenylation, nuclear-pore, and chromatin-associated genes could reflect coupled downstream demands for transcription and RNA maturation. Differences in proliferative activity, cellular composition, or tissue stress may drive the shared co-abundance pattern. This hypothesis predicts coordinated changes in nascent ribosomal RNA processing, pre-messenger-RNA splicing, transcript-end formation, and nuclear export; it requires experimental validation and should not be treated as established causality.

### Important genes

#### RNPC3

- **Related proteins** (co-abundance neighbors): WDR33 (0.91), AATF (0.88), PSPC1 (0.87), CWC22 (0.86), PAXBP1 (0.84), GABPA (0.83), NSMCE3 (0.83), RRS1 (0.83), CPSF2 (0.82), LEO1 (0.81), NUP93 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_04549.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: RNA binding region (RNP1, RRM) containing 3. Two types of spliceosomes catalyze splicing of pre-mRNAs. The major U2-type spliceosome is found in all eukaryotes and removes U2-type introns, which represent more than 99% of pre-mRNA introns. The minor U12-type spliceosome is found in some eukaryotes and removes U12-type introns, which are rare and have distinct splice consensus signals. The U12-type spliceosome consists of several small nuclea…
- **Diseases (Open Targets)**: isolated growth hormone deficiency, type 5 (0.710); neurodegenerative disease (0.527); Decreased response to growth hormone stimulation test (0.453); dentures (0.409); isolated growth hormone deficiency type IA (0.370)
- **Europe PMC papers**: 297
- **Why important**: RNPC3 has the strongest module connectivity and acts as the principal network bridge among RNA-processing, nucleolar, transcription-associated, and other module components. It is annotated as an RNA-binding component of the U twelve-type spliceosome and contributes to messenger-RNA splicing (GO:BP RNA processing; q_global = 0.0232), (STRING Keyword Nucleus; within-query FDR = 3.73e-05), (STRING Process RNA processing; within-query FDR = 0.0076), (STRING RCTM Processing of Capped Intron-Containing Pre-mRNA; within-query FDR = 0.038) (STRING RCTM Metabolism of RNA; within-query FDR = 0.038) (STRING COMPARTMENTS Nucleus; within-query FDR = 0.0407). It is also represented in several hu.MAP spliceosomal complexes (hu.MAP huMAP3_04549.1), (hu.MAP huMAP3_06511.1), (hu.MAP huMAP3_08980.1). Its disease associations include isolated growth hormone deficiency and neurodegenerative disease, and its literature volume is substantial.
- **Conclusion**: Established evidence supports RNPC3 as a central RNA-processing bridge and a component of the minor spliceosome. The module data support its importance as a coordinator or marker of RNA-processing activity. It remains a hypothesis that RNPC3 mechanistically links the nucleolar and splicing portions of this specific cross-tissue module.

#### UTP4

- **Related proteins** (co-abundance neighbors): UTP15 (0.84), RRS1 (0.83); STRING partners: AATF (0.997), NOL11 (0.999), RRS1 (0.739), RSL1D1 (0.996), UTP15 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: huMAP3_01743.1, huMAP3_14264.1, huMAP3_14364.1
- **Function (MyGene.info)**: UTP4 small subunit processome component. This gene encodes a WD40-repeat-containing protein that is localized to the nucleolus. Mutation of this gene causes North American Indian childhood cirrhosis, a severe intrahepatic cholestasis that results in transient neonatal jaundice, and progresses to periportal fibrosis and cirrhosis in childhood and adolescence. Alternative splicing results in multiple transcript variants. [provided by RefSe…
- **Diseases (Open Targets)**: hereditary North American Indian childhood cirrhosis (0.420); cardiovascular disorder (0.101); basal cell carcinoma (0.079); hypertensive disorder (0.064); osteosarcoma (0.052)
- **Europe PMC papers**: 214
- **Why important**: UTP4 is a core member of the nucleolar small-subunit biogenesis signal (GO:BP ribosomal small subunit biogenesis; q_global = 0.0217), (GO:BP RNA processing; q_global = 0.0232). It has strong STRING relationships with the other nucleolar components and is represented in multiple hu.MAP complexes with UTP15 and NOL11 (hu.MAP huMAP3_01743.1) (hu.MAP huMAP3_14264.1) (hu.MAP huMAP3_14364.1). Its annotated function includes maturation of small-subunit ribosomal RNA and ribosomal small-subunit biogenesis. It is associated with North American Indian childhood cirrhosis and other reported disorders, providing disease relevance despite a comparatively modest literature volume.
- **Conclusion**: Established evidence identifies UTP4 as a nucleolar small-subunit-processome component and a structural anchor of the module. Its co-abundance with UTP15 and NOL11 is consistent with shared ribosome-biogenesis activity. The data do not establish that UTP4 is the tissue-specific driver of the module.

#### NOL11

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.86), UTP15 (0.83); STRING partners: AATF (0.811), UTP15 (0.986), UTP4 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_01743.1, huMAP3_14264.1, huMAP3_14364.1
- **Function (MyGene.info)**: nucleolar protein 11. Enables RNA binding activity. Involved in maturation of SSU-rRNA and positive regulation of transcription of nucleolar large rRNA by RNA polymerase I. Located in nucleolus. Part of t-UTP complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: diabetes mellitus (0.100); type 2 diabetes mellitus (0.100); atrial fibrillation (0.087); ulcerative colitis (0.011); cancer (0.011)
- **Europe PMC papers**: 240
- **Why important**: NOL11 is one of the few genes in both globally corrected terms, linking small-subunit biogenesis with RNA processing (GO:BP ribosomal small subunit biogenesis; q_global = 0.0217), (GO:BP RNA processing; q_global = 0.0232). It is located in the nucleolus, belongs to the t-UTP complex, and participates in small-subunit ribosomal RNA maturation. STRING and hu.MAP support its relationships with UTP4 and UTP15 and place it in several complexes (hu.MAP huMAP3_01743.1) (hu.MAP huMAP3_14264.1) (hu.MAP huMAP3_14364.1). It also has reported associations with diabetes, atrial fibrillation, ulcerative colitis, and cancer, although the disease evidence is not specific to this module.
- **Conclusion**: Established evidence supports NOL11 as a nucleolar ribosome-biogenesis component and a connector within the module's core. Its presence in the autonomic nervous system and colon module may indicate a shared demand for ribosome production. A direct role in autonomic or colonic physiology is not demonstrated.

#### CPSF2

- **Related proteins** (co-abundance neighbors): RNPC3 (0.82), SMARCAD1 (0.80); STRING partners: WDR33 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_00102.1, huMAP3_15022.1, huMAP3_09096.1, huMAP3_11757.1
- **Function (MyGene.info)**: cleavage and polyadenylation specific factor 2. Predicted to enable RNA binding activity. Involved in mRNA 3'-end processing by stem-loop binding activity and cleavage. Located in membrane. Part of mRNA cleavage and polyadenylation specificity factor complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); refractive error (0.436); dengue disease (0.370); primary angle-closure glaucoma (0.301); Abnormality of refraction (0.300)
- **Europe PMC papers**: 453
- **Why important**: CPSF2 represents the messenger-RNA three-prime-end-processing arm of the module and is included in the globally corrected RNA-processing term (GO:BP RNA processing; q_global = 0.0232). It has a high-confidence STRING relationship with WDR33 and is present with WDR33 in several hu.MAP cleavage-and-polyadenylation complexes (hu.MAP huMAP3_00102.1) (hu.MAP huMAP3_15022.1) (hu.MAP huMAP3_09096.1) (hu.MAP huMAP3_11757.1). Its annotated function is RNA binding and messenger-RNA three-prime-end processing by stem-loop binding and cleavage. It has reported associations with neurodegenerative disease, refractive error, dengue disease, and glaucoma, and has a substantial literature base.
- **Conclusion**: Established evidence supports CPSF2 as a component of messenger-RNA three-prime-end processing and as the best-defined bridge from the module's general RNA-processing signal to transcript maturation. The module supports coordinated activity with WDR33, but does not show that CPSF2 changes the processing of particular tissue-specific transcripts.

#### NUP93

- **Related proteins** (co-abundance neighbors): TCERG1 (0.83), NUP205 (0.81), SMARCAD1 (0.81), RNPC3 (0.80); STRING partners: NUP205 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_07789.1, huMAP3_05673.1, huMAP3_09042.1
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 provides the clearest nuclear-transport component. It connects in the module to NUP205 and to RNA-processing and chromatin-associated genes, while STRING and hu.MAP support its participation in nuclear-pore-related machinery (STRING Keyword Nucleus; within-query FDR = 3.73e-05), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.00056), (STRING RCTM Processing of Capped Intron-Containing Pre-mRNA; within-query FDR = 0.038) (STRING RCTM Metabolism of RNA; within-query FDR = 0.038) (STRING COMPARTMENTS Nucleus; within-query FDR = 0.0407), (hu.MAP huMAP3_07789.1), (hu.MAP huMAP3_05673.1), (hu.MAP huMAP3_09042.1). Its established functions include nuclear pore complex assembly and nucleocytoplasmic transport, including transport of proteins and RNA. It has a large literature base and disease associations including steroid-resistant nephrotic syndrome and viral infection-related annotations.
- **Conclusion**: Established evidence supports NUP93 as a nuclear-pore component that could connect RNA maturation with nucleocytoplasmic transport. Its position in this module is compatible with coordinated export of processed RNA, but the co-abundance data do not establish altered transport or a causal role in either tissue.

## Module 1

**Tissue pair**: autonomic_nervous_system and colon  
**Genes (12)**: ABT1, BCL7A, NCAPH2, CUX1, ADAR, KMT2A, ODF2, RBM12B, RBM6, SYMPK, TASOR2, ZC3H7B

### Function

The module does not have a formally established GO or KEGG function: no GO/KEGG term passed global correction. Its strongest interpretable signal is a broadly nuclear gene-regulatory and RNA-processing theme. RBM6 and RBM12B are RNA-binding proteins associated with splicing and ribonucleoprotein complexes; SYMPK is a scaffold for polyadenylation and histone-mRNA processing; ADAR performs adenosine-to-inosine RNA editing; CUX1, BCL7A, KMT2A, and TASOR2 contribute transcriptional or epigenetic regulation. The supplementary STRING keywords for isopeptide bonding and Ubl conjugation (STRING Keyword Isopeptide bond; within-query FDR = 0.0153) (STRING Keyword Ubl conjugation; within-query FDR = 0.0273) are compatible with post-translational regulation, but they do not establish the module's primary function. Overall, the safest interpretation is coordinated expression of nuclear RNA-processing, transcriptional, chromatin, and regulatory proteins rather than a demonstrated canonical pathway.

**Cell composition.** This is not a secreted-protein module, and the HPA profile does not support a plasma-protein explanation. Most genes have low tissue specificity and low immune-cell specificity, which is consistent with broadly expressed cellular machinery rather than a strongly tissue-restricted program. There are, however, cell-type-enhanced signals in late spermatids, trophoblast populations, and selected myeloid or B-cell populations. ODF2 is tissue-enriched in testis and cell-type-enriched in late spermatids, while BCL7A, CUX1, and ADAR have blood or immune-cell-associated signals. Thus, a contribution from shared cell types or sample composition cannot be excluded, but the evidence does not indicate that the module is primarily blood-cell enriched. Protein detection in colon is common among the annotated genes, whereas there is no matching HPA tissue for autonomic nervous system, so the cross-tissue interpretation should be treated cautiously.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no high-confidence interaction among the tested module gene pairs. This means the co-abundance edges are not simply a recovery of established STRING physical or functional links. The supplementary STRING enrichment for isopeptide bonding and Ubl conjugation (STRING Keyword Isopeptide bond; within-query FDR = 0.0153) (STRING Keyword Ubl conjugation; within-query FDR = 0.0273) is driven by a subset containing SYMPK, RBM6, TASOR2, CUX1, ADAR, RBM12B, ODF2, KMT2A, and BCL7A, but it is within-query supplementary evidence and is not global enrichment. hu.MAP supplies partial complex support: RBM6 and RBM12B recur together across many complexes, and TASOR2 occurs with them in (hu.MAP huMAP3_12158.1). These recurring pairs suggest that part of the module may reflect RNA-associated or nuclear regulatory complex membership. However, most hu.MAP complexes contain only a subset of the module, so they support local relationships rather than one unified physical complex.

**STRING interactions (score >= 0.7)**: 0 of 66 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Isopeptide bond (FDR = 0.0153, 9 genes); Keyword Ubl conjugation (FDR = 0.0273, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12158.1 (RBM6, TASOR2, RBM12B; 3/16); huMAP3_04693.1 (RBM6, RBM12B; 2/5); huMAP3_08869.1 (RBM6, RBM12B; 2/5); huMAP3_08625.1 (RBM6, RBM12B; 2/6); huMAP3_09539.1 (RBM6, RBM12B; 2/6); huMAP3_01533.1 (RBM6, RBM12B; 2/7); huMAP3_06354.1 (RBM6, RBM12B; 2/7); huMAP3_09463.1 (RBM6, RBM12B; 2/7); huMAP3_08096.1 (RBM6, RBM12B; 2/9); huMAP3_09569.1 (RBM6, RBM12B; 2/9); huMAP3_07030.1 (RBM6, RBM12B; 2/10); huMAP3_08950.1 (RBM6, RBM12B; 2/10); huMAP3_09973.1 (RBM6, RBM12B; 2/10); huMAP3_10643.1 (RBM6, RBM12B; 2/13); huMAP3_09895.1 (RBM6, RBM12B; 2/14); huMAP3_09778.1 (RBM6, RBM12B; 2/16); huMAP3_10098.1 (RBM6, RBM12B; 2/17); huMAP3_14523.1 (RBM6, RBM12B; 2/33)

### Novelty

The module may represent a previously unreported cross-tissue co-abundance pattern, because its edges are absent from the supplied high-confidence STRING network and its hu.MAP support is partial rather than module-wide. Nevertheless, absence from STRING or hu.MAP alone does not establish novelty. The module lacks globally significant GO/KEGG enrichment, has a mixed set of nuclear, chromatin, RNA-processing, and ciliary or sperm-associated genes, and may partly reflect shared expression state, cell composition, or technical covariation. A claim of a new biological complex or pathway would therefore require replication in independent cohorts, preservation testing, cell-composition adjustment, and direct interaction or perturbation experiments.

**Hypothesis.** Hypothesis: the module reflects a conserved nuclear gene-expression state in which RNA processing and transcript maturation are coordinated with transcriptional and chromatin regulation. RBM6 and RBM12B may provide an RNA-associated organizational core, SYMPK may connect transcript three-prime-end processing, ADAR may couple the state to RNA editing and antiviral response, and KMT2A, BCL7A, CUX1, or TASOR2 may shape transcriptional or epigenetic output. ODF2 and the spermatid-associated signals may indicate a context-dependent ciliary or specialized differentiation component rather than a universal part of the mechanism. This remains a hypothesis because global pathway enrichment is absent and the module has no high-confidence STRING interactions.

### Important genes

#### RBM6

- **Related proteins** (co-abundance neighbors): SYMPK (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_12158.1, huMAP3_04693.1, huMAP3_08869.1, huMAP3_08625.1, huMAP3_09539.1, huMAP3_01533.1, huMAP3_06354.1, huMAP3_09463.1, huMAP3_08096.1, huMAP3_09569.1, huMAP3_07030.1, huMAP3_08950.1, huMAP3_09973.1, huMAP3_10643.1, huMAP3_09895.1, huMAP3_09778.1, huMAP3_10098.1, huMAP3_14523.1
- **Function (MyGene.info)**: RNA binding motif protein 6. Enables RNA binding activity. Predicted to be involved in mRNA splicing, via spliceosome. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: intelligence (0.273); type 2 diabetes mellitus (0.267); osteoarthritis (0.234); non-alcoholic fatty liver (0.217); Abnormality of the skeletal system (0.217)
- **Europe PMC papers**: 611
- **Why important**: RBM6 is among the more connected genes in the module and links directly to SYMPK. It is a nuclear-speckle RNA-binding protein with annotations for spliceosomal mRNA splicing and RNA processing. It is also one of the two recurring module members across the hu.MAP complexes (hu.MAP huMAP3_12158.1) through (hu.MAP huMAP3_14523.1). Its literature is substantial relative to the less characterized module members, making it a useful anchor for the RNA-processing interpretation.
- **Conclusion**: Established evidence supports RBM6 as a plausible RNA-processing component and a structural anchor of the module's partial complex signal. It is not established that RBM6 organizes this cross-tissue module or that the co-abundance relationship reflects direct physical interaction.

#### RBM12B

- **Related proteins** (co-abundance neighbors): ODF2 (0.83), TASOR2 (0.83), KMT2A (0.82), ABT1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_12158.1, huMAP3_04693.1, huMAP3_08869.1, huMAP3_08625.1, huMAP3_09539.1, huMAP3_01533.1, huMAP3_06354.1, huMAP3_09463.1, huMAP3_08096.1, huMAP3_09569.1, huMAP3_07030.1, huMAP3_08950.1, huMAP3_09973.1, huMAP3_10643.1, huMAP3_09895.1, huMAP3_09778.1, huMAP3_10098.1, huMAP3_14523.1
- **Function (MyGene.info)**: RNA binding motif protein 12B. Enables RNA binding activity. Predicted to be involved in regulation of RNA splicing. Predicted to be part of ribonucleoprotein complex. Predicted to be active in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: placental retention (0.353); connective tissue disorder (0.342); neurodegenerative disease (0.289); alcohol drinking (0.170); myoepithelial tumor (0.111)
- **Europe PMC papers**: 126
- **Why important**: RBM12B has strong local connectivity, linking ODF2, TASOR2, KMT2A, and ABT1, and it recurs with RBM6 across the hu.MAP complex set (hu.MAP huMAP3_12158.1) through (hu.MAP huMAP3_14523.1). Its annotation supports RNA binding, regulation of RNA splicing, and ribonucleoprotein-complex participation. Although its literature is limited, its repeated complex placement and central network position make it important for interpreting the module.
- **Conclusion**: Established evidence supports RBM12B as a candidate RNA-associated connector between several module branches. Its role as a functional driver of the shared autonomic-nervous-system and colon pattern is a hypothesis, not a demonstrated conclusion.

#### KMT2A

- **Related proteins** (co-abundance neighbors): RBM12B (0.82), ABT1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lysine methyltransferase 2A. This gene encodes a transcriptional coactivator that plays an essential role in regulating gene expression during early development and hematopoiesis. The encoded protein contains multiple conserved functional domains. One of these domains, the SET domain, is responsible for its histone H3 lysine 4 (H3K4) methyltransferase activity which mediates chromatin modifications associated with epigenetic …
- **Diseases (Open Targets)**: Wiedemann-Steiner syndrome (0.799); hereditary disease (0.556); Intellectual disability (0.538); acute myeloid leukemia (0.461); acute lymphoblastic leukemia (0.435)
- **Europe PMC papers**: 9049
- **Why important**: KMT2A connects to RBM12B and ABT1 and provides a strong functional bridge from RNA-associated proteins to chromatin and transcriptional regulation. It is a histone H3 lysine methyltransferase and transcriptional coactivator with roles in development and hematopoiesis. It has extensive literature and important disease associations, including developmental disorders and acute leukemias.
- **Conclusion**: Established evidence supports KMT2A as a biologically important chromatin regulator that could influence the transcriptional state represented by the module. The data do not show that KMT2A mechanistically controls the other module genes or explains the tissue sharing.

#### ADAR

- **Related proteins** (co-abundance neighbors): BCL7A (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR is connected to BCL7A and adds a distinct, well-established RNA-editing function. It catalyzes adenosine-to-inosine editing, affects double-stranded RNA stability, and is linked to RNA processing, antiviral response, and interferonopathy-related disease. Its literature is extensive, so it provides strong biological context even though its network degree is limited.
- **Conclusion**: Established evidence supports ADAR as an RNA-processing and innate-response regulator that is compatible with the module's nuclear regulatory theme. A specific role for RNA editing in generating this co-abundance module is not demonstrated.

#### BCL7A

- **Related proteins** (co-abundance neighbors): ZC3H7B (0.85), CUX1 (0.82), ADAR (0.82), NCAPH2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Group enriched; location Nucleoplasm, Vesicles; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BAF chromatin remodeling complex subunit BCL7A. This gene is directly involved, with Myc and IgH, in a three-way gene translocation in a Burkitt lymphoma cell line. As a result of the gene translocation, the N-terminal region of the gene product is disrupted, which is thought to be related to the pathogenesis of a subset of high-grade B cell non-Hodgkin lymphoma. The N-terminal segment involved in the translocation includes the region that shar…
- **Diseases (Open Targets)**: neurodegenerative disease (0.503); Burkitt lymphoma (0.385); plasma cell myeloma (0.301); diffuse large B-cell lymphoma (0.214); acute myeloid leukemia (0.206)
- **Europe PMC papers**: 692
- **Why important**: BCL7A is a highly connected local node linking ZC3H7B, CUX1, ADAR, and NCAPH2. It is a subunit of the BAF chromatin-remodeling complex and has transcriptional and differentiation-related functions. Its HPA profile includes enrichment in selected B-cell and plasmacytoid dendritic-cell populations, and it has established links to Burkitt lymphoma, plasma-cell myeloma, and other hematologic disease. Its literature is substantial.
- **Conclusion**: Established evidence supports BCL7A as a chromatin-regulatory node and raises the possibility that immune-cell composition contributes to part of the module. The available evidence does not distinguish a true shared regulatory program from correlated abundance of immune or other cell populations.

## Module 2

**Tissue pair**: autonomic_nervous_system and colon  
**Genes (21)**: ACIN1, BASP1, CPSF1, DCAF13, DDX54, LIG3, DST, AHCTF1, LIMCH1, LRWD1, MDC1, MDN1, RBM28, RBM34, SETMAR, SF3A1, SMARCA1, GTF3C1, TOP2A, VHL, ZFR

### Function

The strongest interpretation is a conserved nuclear information-processing module. The primary evidence is the broad membership of the module in nuclear lumen (GO:CC nuclear lumen; q_global = 0.00948), nucleic acid binding (GO:MF nucleic acid binding; q_global = 0.0477), and membraneless nuclear organelles (GO:CC membraneless organelle; q_global = 0.0483) and (GO:CC intracellular membraneless organelle; q_global = 0.0483). The gene annotations refine this into coordinated RNA handling, ribosome and nucleolar biogenesis, chromatin regulation, DNA replication and repair, and cell-cycle control. RBM34, RBM28, DDX54, DCAF13, GTF3C1, MDN1, CPSF1, SF3A1, and ZFR support RNA processing, ribosome-related maturation, transcription, splicing, or RNA binding; SMARCA1, SETMAR, LRWD1, MDC1, LIG3, and TOP2A support chromatin remodeling, DNA replication, DNA repair, or chromosome dynamics; AHCTF1 supports nuclear-pore assembly and cytokinesis. Thus, the module is better viewed as a coordinated nuclear maintenance and proliferative-state program than as a pathway dedicated to autonomic or colonic physiology. The membraneless-organelle terms should be interpreted as localization and molecular-process evidence, not as proof of one physical complex.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the secretome contains no module members. Most genes have low tissue specificity, and the proteins are predominantly nuclear, nucleolar, nucleoplasmic, or associated with nuclear bodies, with the main cytoskeletal exceptions being BASP1, DST, and LIMCH1. HPA does not indicate a uniformly autonomic-nervous-system or colon-specific program. Instead, cell-type-enhanced signals include oligodendrocytes, neurons, neutrophils, germ-cell populations, and several epithelial or muscle-related cell types. Several genes have immune-cell-enhanced or immune-cell-enriched patterns, particularly involving neutrophils and other leukocyte populations, so shared cellular composition or proliferative and stress-related cell states could contribute to the cross-tissue signal. Colon protein detection is widespread among the measured members, whereas the autonomic-nervous-system tissue lacks a matching HPA tissue measurement. The module therefore does not resemble a blood-protein signature, but blood or immune-cell admixture cannot be excluded as a contributor to some genes.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC nuclear lumen | 0.00948 | ACIN1, AHCTF1, BASP1, CPSF1, DCAF13, DDX54, DST, GTF3C1, LIG3, LRWD1, MDC1, MDN1, RBM28, RBM34, SETMAR, SF3A1, SMARCA1, TOP2A, VHL |
| GO:MF nucleic acid binding | 0.0477 | ACIN1, AHCTF1, BASP1, CPSF1, DCAF13, DDX54, GTF3C1, LIG3, LRWD1, RBM28, RBM34, SETMAR, SF3A1, SMARCA1, TOP2A, ZFR |
| GO:CC membraneless organelle | 0.0483 | ACIN1, AHCTF1, BASP1, DCAF13, DDX54, DST, GTF3C1, LIMCH1, LRWD1, MDC1, MDN1, RBM28, RBM34, SETMAR, SF3A1, SMARCA1, TOP2A, VHL, ZFR |
| GO:CC intracellular membraneless organelle | 0.0483 | ACIN1, AHCTF1, BASP1, DCAF13, DDX54, DST, GTF3C1, LIMCH1, LRWD1, MDC1, MDN1, RBM28, RBM34, SETMAR, SF3A1, SMARCA1, TOP2A, VHL, ZFR |

### STRING and hu.MAP

STRING provides a concentrated, biologically coherent RNA and nucleolar interaction core: RBM28 connects strongly with DCAF13, DDX54, and RBM34, while DDX54 also connects with RBM34. These are already known relationships and support the RNA-processing and nucleolar interpretation. STRING additionally places many members in nuclear and nuclear-lumen categories, but these are supplementary within-query enrichments rather than global module-level evidence. The module has only a small set of high-confidence STRING gene-pair relationships relative to all possible pairs, so most co-abundance edges are not directly supported as physical interactions. hu.MAP supplies one low-confidence partial complex overlap, involving BASP1 and DST in a complex otherwise containing cytoskeletal and signaling proteins. This supports a possible cytoskeletal or membrane-associated bridge but does not establish a central complex for the module. Overall, known molecular relationships validate a compact RNA and nucleolar core, while the larger module likely combines several related nuclear processes and state-dependent co-expression rather than representing one experimentally defined complex.

**STRING interactions (score >= 0.7)**: 4 of 210 gene pairs: DCAF13–RBM28 (0.896); DDX54–RBM28 (0.899); DDX54–RBM34 (0.92); RBM28–RBM34 (0.975)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Nuclear lumen (FDR = 0.00099, 15 genes); Keyword Nucleus (FDR = 0.00099, 19 genes); Component Nuclear lumen (FDR = 0.0031, 19 genes); COMPARTMENTS Nucleus (FDR = 0.0036, 19 genes); COMPARTMENTS Nucleolus (FDR = 0.0122, 9 genes); Component Nucleoplasm (FDR = 0.0244, 17 genes); Component Nucleolus (FDR = 0.025, 10 genes); Component Nucleus (FDR = 0.0283, 20 genes); Component Intracellular non-membrane-bounded organelle (FDR = 0.0359, 17 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05473.1 (BASP1, DST; 2/7)

### Novelty

The shared autonomic-nervous-system and colon co-abundance observation may be a new systems-level finding, especially because the module combines a tightly coherent nuclear and RNA-processing signature with a small number of known physical interactions. However, the underlying biology is not wholly new: the functions of its members, the RBM28–DDX54–RBM34 interaction core, and many nuclear processes are established. Absence of most module pairs from STRING or hu.MAP cannot by itself demonstrate novelty, because those resources are incomplete and physical interaction coverage is uneven. The defensible conclusion is that the cross-tissue co-abundance organization and its precise module boundary may be novel, whereas the component functions and part of the interaction core are established. Independent replication, preservation testing, cell-composition adjustment, and perturbation or interaction experiments would be needed to establish biological novelty.

**Hypothesis.** Hypothesis: in both autonomic-nervous-system and colon samples, a shared cellular state coordinates nucleolar RNA maturation, pre-mRNA processing, chromatin accessibility, DNA surveillance, and cell-cycle or replication demands. The RBM34–RBM28–DDX54–DCAF13 interaction core could organize RNA and nucleolar functions, while SMARCA1, SETMAR, MDC1, LIG3, LRWD1, TOP2A, and AHCTF1 connect that state to chromatin remodeling, DNA repair, replication licensing, chromosome topology, nuclear-envelope organization, and cytokinesis. BASP1, DST, and LIMCH1 may reflect a structural or cell-state interface between nuclear programs and the cytoskeleton. This is a mechanistic model generated from co-abundance and annotations, not a demonstrated causal pathway; it should be tested by cell-type-resolved analysis and perturbation of the RNA-processing and chromatin components.

### Important genes

#### RBM34

- **Related proteins** (co-abundance neighbors): SMARCA1 (0.87), TOP2A (0.83), RBM28 (0.82), AHCTF1 (0.81), DDX54 (0.80), GTF3C1 (0.80); STRING partners: DDX54 (0.92), RBM28 (0.975)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 34. This gene encodes a member of the RNA-binding motif family of RNA recognition motif proteins. The encoded protein contains an RNA-binding domain made up of two RNA recognition motif subdomains referred to as RNA recognition motif-1 and RNA recognition motif-2. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2016].
- **Diseases (Open Targets)**: neurodegenerative disease (0.334); hepatocellular carcinoma (0.076); neoplasm (0.075); nervous system benign neoplasm (0.069); alcohol drinking (0.067)
- **Europe PMC papers**: 154
- **Why important**: RBM34 is the highest-connectivity member of the module and links to SMARCA1, TOP2A, RBM28, AHCTF1, DDX54, and GTF3C1. It is present in every primary GO term (GO:CC nuclear lumen; q_global = 0.00948) through (GO:CC intracellular membraneless organelle; q_global = 0.0483) and every listed STRING enrichment, is localized to nucleoli, and is annotated as an RNA-binding protein involved in large-subunit ribosomal RNA maturation. Its direct STRING relationships with DDX54 and RBM28 place it at the center of the best-supported molecular core. The disease and literature evidence is substantial enough to make it biologically informative without implying a disease-specific role here.
- **Conclusion**: Established evidence supports RBM34 as a central nucleolar and RNA-processing component of the module. It is a strong candidate for organizing the conserved nuclear co-abundance signal. The hypothesis that it functionally couples RNA maturation to chromatin or cell-cycle components remains unproven.

#### SMARCA1

- **Related proteins** (co-abundance neighbors): RBM34 (0.87), AHCTF1 (0.82), GTF3C1 (0.82), MDN1 (0.82), TOP2A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SNF2 related chromatin remodeling ATPase 1. This gene encodes a member of the SWI/SNF family of proteins. The encoded protein is an ATPase which is expressed in diverse tissues and contributes to the chromatin remodeling complex that is involved in transcription. The protein may also play a role in DNA damage, growth inhibition and apoptosis of cancer cells. Alternative splicing results in multiple transcript variants. [provided by RefSeq, …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.423); X-linked intellectual disability (0.401); non-syndromic X-linked intellectual disability (0.333); Abnormal brain morphology (0.266); cancer (0.211)
- **Europe PMC papers**: 924
- **Why important**: SMARCA1 has a high network degree and connects the RBM34-centered core with AHCTF1, GTF3C1, MDN1, and TOP2A. It appears in all primary GO terms (GO:CC nuclear lumen; q_global = 0.00948) through (GO:CC intracellular membraneless organelle; q_global = 0.0483). Its established function as a SWI/SNF-family chromatin-remodeling ATPase provides a mechanistic route from nuclear organization to transcription, heterochromatin, DNA damage responses, and neuronal development. It also has substantial disease and literature representation, including neurodevelopmental associations.
- **Conclusion**: Established evidence supports SMARCA1 as the principal chromatin-remodeling representative in the module. Its co-abundance with RNA and nucleolar genes suggests coordinated nuclear regulation, but whether SMARCA1 directly drives the shared tissue signal is a hypothesis.

#### TOP2A

- **Related proteins** (co-abundance neighbors): RBM34 (0.83), DCAF13 (0.83), SMARCA1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA topoisomerase II alpha. This gene encodes a DNA topoisomerase, an enzyme that controls and alters the topologic states of DNA during transcription. This nuclear enzyme is involved in processes such as chromosome condensation, chromatid separation, and the relief of torsional stress that occurs during DNA transcription and replication. It catalyzes the transient breaking and rejoining of two strands of duplex DNA which al…
- **Diseases (Open Targets)**: neoplasm (0.618); breast cancer (0.616); acute myeloid leukemia (0.606); plasma cell myeloma (0.594); small cell lung carcinoma (0.580)
- **Europe PMC papers**: 11752
- **Why important**: TOP2A is connected to RBM34, DCAF13, and SMARCA1 and occurs in all primary GO terms (GO:CC nuclear lumen; q_global = 0.00948) through (GO:CC intracellular membraneless organelle; q_global = 0.0483) and all listed STRING enrichments. It controls DNA topology and is involved in chromosome condensation, chromatid separation, replication-related processes, and DNA damage responses. Its tissue and cell-type pattern includes proliferative and germ-cell populations as well as colon, and its disease and literature record is exceptionally extensive. These features make it a useful marker of a proliferative or genome-maintenance component within the module.
- **Conclusion**: Established evidence supports TOP2A as the module's clearest cell-cycle and chromosome-dynamics component. Its presence may indicate proliferative-state variation shared across samples, but the co-abundance data do not establish that proliferation is the sole cause of the module.

#### SETMAR

- **Related proteins** (co-abundance neighbors): CPSF1 (0.82), SF3A1 (0.82), AHCTF1 (0.82), ACIN1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SET and mariner transposase domain methyltransferase. This gene encodes a fusion protein that contains an N-terminal histone-lysine N-methyltransferase domain and a C-terminal mariner transposase domain. The encoded protein binds DNA and functions in DNA repair activities including non-homologous end joining and double strand break repair. The SET domain portion of this protein specifically methylates histone H3 lysines 4 and 36. This gene exists as …
- **Diseases (Open Targets)**: spinocerebellar ataxia type 15/16 (0.351); male reproductive organ cancer (0.314); schizophrenia (0.277); refractive error (0.251); secondary malignant neoplasm (0.243)
- **Europe PMC papers**: 633
- **Why important**: SETMAR has a central bridging position among CPSF1, SF3A1, AHCTF1, and ACIN1 and is present in all primary GO terms (GO:CC nuclear lumen; q_global = 0.00948) through (GO:CC intracellular membraneless organelle; q_global = 0.0483). Its fusion protein combines a histone methyltransferase domain with a mariner transposase domain and is annotated in DNA double-strand-break processing, nonhomologous-end joining, chromatin remodeling, and DNA integration. It therefore links the module's RNA-processing neighborhood to chromatin and DNA-repair biology. It also has broad disease associations and substantial literature coverage.
- **Conclusion**: Established evidence supports SETMAR as a plausible bridge between nuclear RNA-related organization and genome maintenance. Its exact contribution to this conserved co-abundance module, and whether it acts together with the neighboring splicing factors in these tissues, remains a hypothesis.

#### AHCTF1

- **Related proteins** (co-abundance neighbors): SMARCA1 (0.82), SETMAR (0.82), MDC1 (0.81), RBM34 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Nuclear membrane, Nuclear bodies; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: AT-hook containing transcription factor 1. Predicted to enable DNA binding activity. Involved in nuclear pore complex assembly and regulation of cytokinesis. Located in nuclear membrane. Colocalizes with chromatin; kinetochore; and nuclear pore outer ring. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.519); lysosomal storage disease (0.306); stricture (0.223); premature birth (0.182); Intellectual disability (0.111)
- **Europe PMC papers**: 392
- **Why important**: AHCTF1 has a relatively central position, connecting SMARCA1, SETMAR, MDC1, and RBM34, and appears in all primary GO terms (GO:CC nuclear lumen; q_global = 0.00948) through (GO:CC intracellular membraneless organelle; q_global = 0.0483). It is localized to the nuclear membrane, nuclear bodies, and nucleoplasm and is annotated in nuclear pore complex assembly, nucleocytoplasmic transport, and cytokinesis. Its colon protein detection and neutrophil-associated HPA pattern make it relevant to both the tissue setting and the possibility of cell-state or cellular-composition effects. Its disease associations include neurodegenerative and intellectual-disability categories.
- **Conclusion**: Established evidence supports AHCTF1 as a nuclear-envelope and transport-related connector between the RNA, chromatin, and cell-division portions of the module. Its role as a cross-tissue coordinator is a hypothesis rather than a demonstrated mechanism.

## Module 3

**Tissue pair**: autonomic_nervous_system and colon  
**Genes (21)**: AFG2A, AKAP12, PPP3R1, CARMIL2, DIAPH3, DNMT1, ELP1, GSE1, IQGAP3, KIFBP, KHDRBS3, KIF23, NME7, NUF2, PANX1, PKN1, PLK1, PLRG1, SHCBP1, SLAIN2, ZNF512

### Function

The module is most consistent with a proliferative cell-division and cytoskeletal-remodelling program, especially involving mitotic spindle function, chromosome segregation, cytokinesis, microtubule organisation, and associated signalling. This interpretation is based on the annotations of PLK1, KIF23, NUF2, SHCBP1, SLAIN2, IQGAP3, PKN1, DIAPH3 and related genes, together with the dense internal connections among PLK1, KIF23, NUF2 and SHCBP1. KHDRBS3 and PLRG1 add an RNA-processing component, while CARMIL2, PKN1, DIAPH3, PANX1 and PPP3R1 support cytoskeletal, polarity, migration or cell-signalling links. No GO or KEGG term passed global correction, so these annotations are interpretive evidence rather than globally significant enrichment. The lack of a globally significant term does not invalidate the module.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not a uniformly expressed housekeeping module. Many genes show tissue or cell-type enhancement in bone marrow, lymphoid tissue, testis, erythrocyte progenitors, monocyte progenitors, megakaryocyte progenitors or spermatogenic cells, and several genes have immune-cell enrichment or enhancement. This pattern raises the possibility that the shared signal reflects proliferating progenitor or immune-associated cells present in both tissue datasets, rather than a specialised function of autonomic nervous system and colon cells. The HPA pattern also includes brain, intestine and neural cell types, so a neural or epithelial contribution remains possible. Protein detection in colon is broad for the module, whereas the autonomic nervous system comparison has no matching HPA tissue.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a connected mitotic core rather than a uniformly interconnected module. The strongest relationships include KIF23 with PLK1 and SHCBP1, KIF23 with NUF2, and NUF2 with PLK1; KIF23 also connects to NME7. These are established database-supported relationships and are concordant with chromosome segregation, spindle and cytokinesis functions. The remaining module genes have few or no high-confidence STRING partners in the supplied results, so the full co-abundance structure should not be treated as a single experimentally established complex. hu.MAP independently places KIF23 and SHCBP1 together in every listed qualifying complex, with RACGAP1, CD2AP, USP8 and other proteins completing context-dependent complexes (hu.MAP huMAP3_07024.1) through (hu.MAP huMAP3_13310.1). Thus, KIF23–SHCBP1 is supported by repeated complex evidence, while the broader module likely combines a mitotic core with neighbouring regulatory, cytoskeletal, RNA-processing and cell-context signals.

**STRING interactions (score >= 0.7)**: 6 of 210 gene pairs: KIF23–NME7 (0.762); KIF23–NUF2 (0.912); KIF23–PLK1 (0.988); KIF23–SHCBP1 (0.965); NUF2–PLK1 (0.865); NUF2–SHCBP1 (0.701)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07024.1 (KIF23, SHCBP1; 2/3); huMAP3_07667.1 (KIF23, SHCBP1; 2/3); huMAP3_00688.1 (KIF23, SHCBP1; 2/4); huMAP3_11326.1 (KIF23, SHCBP1; 2/8); huMAP3_14449.1 (KIF23, SHCBP1; 2/9); huMAP3_13310.1 (KIF23, SHCBP1; 2/11)

### Novelty

The module should not be claimed as a wholly new molecular complex. Several of its central relationships are already represented in STRING, and the KIF23–SHCBP1 pairing recurs in hu.MAP complexes (hu.MAP huMAP3_07024.1) through (hu.MAP huMAP3_13310.1). The potentially novel result is instead the conserved co-abundance pattern across autonomic nervous system and colon, particularly the way mitotic, cytoskeletal, RNA-processing and immune or progenitor-associated genes are linked in these tissue groups. Absence of many module pairs from STRING or hu.MAP is not proof of novelty, because co-abundance can reflect shared cell composition, regulation, or condition-specific coordination rather than direct physical interaction. Independent replication, cell-composition adjustment, and comparison with existing tissue co-expression resources would be needed before calling the tissue-pair module a new biological mechanism.

**Hypothesis.** Hypothesis: the shared module reflects a proliferative or regenerative cell population present in both tissue groups, in which PLK1, KIF23, NUF2 and SHCBP1 coordinate mitotic progression, spindle or midbody behaviour and cytokinesis, while PKN1, DIAPH3, IQGAP3, CARMIL2 and PANX1 connect this program to actin organisation, polarity, migration or membrane signalling. KHDRBS3 and PLRG1 may couple the proliferative state to regulated RNA processing. The HPA enrichment of marrow, lymphoid and germ-cell progenitor populations makes a shared cellular-composition explanation especially plausible; a direct autonomic-neural mechanism remains a secondary possibility rather than an established conclusion.

### Important genes

#### PLK1

- **Related proteins** (co-abundance neighbors): KIFBP (0.83), NUF2 (0.82), KHDRBS3 (0.81), SHCBP1 (0.81), CARMIL2 (0.80); STRING partners: KIF23 (0.988), NUF2 (0.865)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polo like kinase 1. The Ser/Thr protein kinase encoded by this gene belongs to the CDC5/Polo subfamily. It is highly expressed during mitosis and elevated levels are found in many different types of cancer. Depletion of this protein in cancer cells dramatically inhibited cell proliferation and induced apoptosis; hence, it is a target for cancer therapy. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.545); Alzheimer disease (0.543); Parkinson disease (0.528); lysosomal storage disease (0.526); microcephaly (0.371)
- **Europe PMC papers**: 16075
- **Why important**: PLK1 is a highly connected module gene and links directly to KIF23, NUF2 and SHCBP1 in STRING. Its supplied annotations cover mitotic progression, spindle-related events, chromosome segregation and cytokinesis. HPA places it in bone marrow, lymphoid tissue, testis and proliferative intestinal or hematopoietic cell types. It also has extensive literature and disease relevance, making it the strongest established marker of the module's proliferative interpretation.
- **Conclusion**: Established evidence supports PLK1 as a central mitotic kinase and a major anchor of the module. The hypothesis that its abundance explains the shared tissue signal through proliferating progenitor or regenerative cells is plausible, but the fact sheet does not establish the responsible cell population or causal activity.

#### KIF23

- **Related proteins** (co-abundance neighbors): PANX1 (0.81), PLRG1 (0.80), SHCBP1 (0.80); STRING partners: NME7 (0.762), NUF2 (0.912), PLK1 (0.988), SHCBP1 (0.965)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_07024.1, huMAP3_07667.1, huMAP3_00688.1, huMAP3_11326.1, huMAP3_14449.1, huMAP3_13310.1
- **Function (MyGene.info)**: kinesin family member 23. The protein encoded by this gene is a member of kinesin-like protein family. This family includes microtubule-dependent molecular motors that transport organelles within cells and move chromosomes during cell division. This protein has been shown to cross-bridge antiparallel microtubules and drive microtubule movement in vitro. Alternate splicing of this gene results in multiple transcript variant…
- **Diseases (Open Targets)**: congenital dyserythropoietic anemia type 3 (0.735); hypertensive disorder (0.436); neurodegenerative disease (0.370); cardiovascular disorder (0.302); essential hypertension (0.302)
- **Europe PMC papers**: 2136
- **Why important**: KIF23 is a connected module hub with STRING links to PLK1, NUF2, SHCBP1 and NME7. Its annotations directly describe microtubule movement, spindle midzone assembly and cytokinesis. It is also present with SHCBP1 in all supplied hu.MAP complexes (hu.MAP huMAP3_07024.1) through (hu.MAP huMAP3_13310.1), giving it unusually strong support as a structural bridge between the module and known cell-division complexes. HPA enhancement in marrow, lymphoid tissue and proliferative cell types fits the same interpretation.
- **Conclusion**: Established evidence supports KIF23 as a core cytokinesis and spindle-associated component of the module. Its role as the principal bridge connecting the mitotic core to the wider co-abundance pattern is a reasonable network hypothesis, not proof of direct physical interaction with every module member.

#### SHCBP1

- **Related proteins** (co-abundance neighbors): KHDRBS3 (0.85), PANX1 (0.81), PLK1 (0.81), KIF23 (0.80); STRING partners: KIF23 (0.965), NUF2 (0.701)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nuclear bodies; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07024.1, huMAP3_07667.1, huMAP3_00688.1, huMAP3_11326.1, huMAP3_14449.1, huMAP3_13310.1
- **Function (MyGene.info)**: SHC binding and spindle associated 1. Predicted to enable SH2 domain binding activity. Predicted to be involved in fibroblast growth factor receptor signaling pathway and regulation of neural precursor cell proliferation. Predicted to be located in cytoplasm; midbody; and spindle. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Alzheimer disease (0.145); neoplasm (0.111); cancer (0.109); gastric cancer (0.098); breast cancer (0.098)
- **Europe PMC papers**: 1502
- **Why important**: SHCBP1 has strong connections to KHDRBS3, PANX1, PLK1 and KIF23 and is the repeated shared member of the hu.MAP complexes (hu.MAP huMAP3_07024.1) through (hu.MAP huMAP3_13310.1). Its annotations place it at the spindle and midbody and link it to neural precursor proliferation and fibroblast growth factor signalling. HPA associates it with marrow, lymphoid tissue, erythrocyte progenitors, spermatogenic cells and monocyte-related immune context.
- **Conclusion**: Established evidence supports SHCBP1 as a connector between mitotic structures and broader signalling or cell-context networks. The hypothesis that it helps couple cytokinesis to tissue regeneration or progenitor-cell behaviour is compatible with the supplied data, but its precise role in the conserved tissue-pair module remains unresolved.

#### NUF2

- **Related proteins** (co-abundance neighbors): DNMT1 (0.84), PLK1 (0.82), PKN1 (0.82); STRING partners: KIF23 (0.912), PLK1 (0.865), SHCBP1 (0.701)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NUF2 component of NDC80 kinetochore complex. This gene encodes a protein that is highly similar to yeast Nuf2, a component of a conserved protein complex associated with the centromere. Yeast Nuf2 disappears from the centromere during meiotic prophase when centromeres lose their connection to the spindle pole body, and plays a regulatory role in chromosome segregation. The encoded protein is found to be associated with centromeres of mitotic…
- **Diseases (Open Targets)**: gout (0.458); irritable bowel syndrome (0.438); bipolar disorder (0.426); mathematical ability (0.401); prostate carcinoma (0.400)
- **Europe PMC papers**: 1971
- **Why important**: NUF2 is directly connected to PLK1, KIF23 and SHCBP1 in STRING and is annotated as a component of the NDC80 kinetochore complex involved in spindle attachment, checkpoint signalling and chromosome segregation. Its HPA pattern is group-enriched in marrow, lymphoid tissue and testis, with enhancement in differentiating spermatogonia and erythrocyte progenitors. These features make it a strong indicator that the module contains a genuine chromosome-segregation signal rather than only generic tissue expression.
- **Conclusion**: Established evidence supports NUF2 as a kinetochore and mitotic component reinforcing the module's cell-division interpretation. Its association with the shared tissue signal may reflect proliferating cells, but the fact sheet cannot determine whether NUF2 is altered within cells or simply tracks their abundance.

#### ELP1

- **Related proteins** (co-abundance neighbors): KIFBP (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: elongator acetyltransferase complex subunit 1. The protein encoded by this gene is a scaffold protein and a regulator for three different kinases involved in proinflammatory signaling. The encoded protein can bind NF-kappa-B-inducing kinase and I-kappa-B kinases through separate domains and assemble them into an active kinase complex. Mutations in this gene have been associated with familial dysautonomia. Alternative splicing results in multip…
- **Diseases (Open Targets)**: Riley-Day syndrome (0.807); medulloblastoma (0.721); primary dysautonomia (0.407); hereditary sensory and autonomic neuropathy (0.374); mathematical ability (0.361)
- **Europe PMC papers**: 960
- **Why important**: ELP1 is less central in the network than the mitotic genes, but it provides important biological context for the autonomic nervous system comparison. It is a scaffold for kinase complexes involved in proinflammatory signalling, participates in tRNA modification and translation, and is associated with familial dysautonomia, primary dysautonomia and hereditary sensory and autonomic neuropathy in the supplied disease evidence. Its HPA profile includes a basophil-associated immune signal, while colon protein detection is reported.
- **Conclusion**: Established evidence supports ELP1 as a biologically relevant autonomic and translational or inflammatory-context gene, but not as a core physical component of the mitotic STRING or hu.MAP evidence. The hypothesis that ELP1 connects autonomic disease relevance to the broader proliferative or immune-associated module is suggestive and requires independent validation.

## Module 4

**Tissue pair**: autonomic_nervous_system and colon  
**Genes (16)**: PGM3, FARP1, HEATR1, KRT2, MAP7D1, NOL8, PDCL, PRRC2B, RNF214, POLR3D, SESN1, SNX24, GTF3C4, TRMT5, USP15, ERCC4

### Function

The module does not support a single strongly established biological function because no GO or KEGG globally significant GO/KEGG term passed global correction, and there was no supplementary STRING supplementary STRING enrichment. The co-abundance structure is centered on SESN1, with a set of weaker peripheral connections linking stress and metabolic regulation, protein deubiquitination, cytoskeletal organization, epithelial differentiation, RNA and ribosome-related processes, DNA repair, vesicle biology, and neuronal cytoskeletal signaling. SESN1 provides the most plausible functional anchor because it participates in cellular responses to oxidative stress and nutrient limitation, activates energy-stress signaling, inhibits growth-promoting signaling, supports antioxidant defense, and promotes macroautophagy. The overall interpretation is therefore a mixed cellular-stress and maintenance module rather than a narrowly defined pathway. The epithelial and cytoskeletal genes may also reflect the cellular composition of the sampled tissues.

**Cell composition.** The module is not composed of plasma or secreted proteins: HPA reports no secreted genes. Most genes have low tissue specificity, while many show cell-type-enhanced expression rather than a uniform autonomic-nervous-system or colon signature. KRT2 is tissue-enriched in skin and cell-type-enriched in suprabasal keratinocytes, making it a conspicuous epithelial or sample-composition marker rather than evidence for a core shared function of the two tissues. MAP7D1 and ERCC4 are tissue-enhanced in skeletal muscle, and USP15 is tissue-enhanced in bone marrow and associated with neutrophil-lineage cells. Several genes have immune-cell-enhanced signals, including neutrophil, monocyte, and T-cell annotations, but the module is not uniformly blood-cell specific. The pattern is most consistent with a mixture of broadly expressed cellular maintenance genes and signals from shared or variable epithelial, stromal, muscle, and immune cell populations. Colon protein detection is reported for many module members, whereas matched autonomic-nervous-system protein data are unavailable, so the apparent sharing should not be interpreted as protein-level confirmation in the autonomic nervous system.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no hu.MAP complex containing multiple module members. Thus, the co-abundance edges are not supported here as established direct physical interactions or as membership in a known multiprotein complex. The module may represent coordinated regulation, shared cell composition, indirect signaling, or technical and biological covariation rather than a stable molecular complex. Known functional relationships are available from individual gene annotations: SESN1 is linked to stress and growth control, USP15 to ubiquitin-dependent regulation and transforming-growth-factor signaling, FARP1 to neuronal cytoskeletal signaling, ERCC4 to nucleotide-excision and other DNA-repair processes, and HEATR1, NOL8, GTF3C4, and POLR3D to nucleolar or RNA-transcription processes. These annotations do not establish interactions within this module.

**STRING interactions (score >= 0.7)**: 0 of 120 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel tissue-pair co-abundance pattern, because the supplied databases do not place the genes in a shared high-confidence STRING interaction network or hu.MAP complex and no globally significant GO or KEGG signal defines the group. However, that absence does not prove novelty: co-abundance modules can capture indirect regulation, shared cell types, tissue composition, or poorly characterized biology that is not represented in interaction databases. The strongest defensible claim is that the particular cross-tissue co-abundance pattern is not explained by an already recognized physical complex or canonical enriched pathway in the supplied evidence. A claim of a new biological mechanism would require independent replication, cell-composition adjustment, and experimental or external-cohort validation.

**Hypothesis.** Hypothesis: the module reflects a coordinated cellular-maintenance state in which SESN1-associated stress and nutrient sensing covaries with protein-quality control, transcriptional and ribosomal maintenance, cytoskeletal remodeling, epithelial differentiation, and DNA repair. In colon, this signal may be contributed by epithelial cells together with variable immune or stromal content; in autonomic nervous system samples, it may reflect broadly expressed maintenance programs or shared non-neuronal cell populations. KRT2 and the HPA cell-type signals make a composition-driven component especially plausible. This hypothesis predicts that the module will weaken after adjustment for epithelial, immune, and muscle-cell proportions, while any residual SESN1-centered signal should track oxidative stress, nutrient limitation, autophagy, or growth-control states.

### Important genes

#### SESN1

- **Related proteins** (co-abundance neighbors): TRMT5 (0.85), HEATR1 (0.85), MAP7D1 (0.85), KRT2 (0.84), USP15 (0.83), PGM3 (0.82), PDCL (0.82), GTF3C4 (0.81), FARP1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sestrin 1. This gene encodes a member of the sestrin family. Sestrins are induced by the p53 tumor suppressor protein and play a role in the cellular response to DNA damage and oxidative stress. The encoded protein mediates p53 inhibition of cell growth by activating AMP-activated protein kinase, which results in the inhibition of the mammalian target of rapamycin protein. The encoded protein also plays a cr…
- **Diseases (Open Targets)**: uterine corpus leiomyoma (0.323); prostate carcinoma (0.278); hypothyroidism (0.271); neurodegenerative disease (0.264); preeclampsia (0.258)
- **Europe PMC papers**: 1461
- **Why important**: SESN1 is the central network hub, connecting the largest set of module members and therefore providing the strongest organizing position in the co-abundance graph. Its established functions include induction by p53, response to DNA damage and oxidative stress, AMP-activated kinase activation, inhibition of mammalian-target-of-rapamycin signaling, antioxidant defense, and promotion of macroautophagy. It also has a substantial literature and disease links spanning cancer, neurodegeneration, and other disorders.
- **Conclusion**: Established evidence supports SESN1 as the best candidate anchor for a cellular-stress and metabolic-maintenance interpretation. It is only a hypothesis that SESN1 drives the observed cross-tissue module; the co-abundance data do not establish causality.

#### KRT2

- **Related proteins** (co-abundance neighbors): SESN1 (0.84), POLR3D (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location Intermediate filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 2. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is expressed largely in the upper spinous layer of epidermal keratinocytes and mutations in this gene …
- **Diseases (Open Targets)**: superficial epidermolytic ichthyosis (0.815); exfoliative ichthyosis (0.358); Palmoplantar hyperkeratosis (0.267); hereditary disease (0.193); Vertigo (0.145)
- **Europe PMC papers**: 7459
- **Why important**: KRT2 is a conspicuous epithelial marker with tissue-enriched skin expression and cell-type-enriched suprabasal-keratinocyte expression. It is connected to SESN1 and POLR3D in the module and has a large disease and literature record, including inherited keratinization disorders. Its presence is important because it can identify epithelial or sample-composition effects rather than a shared autonomic-nervous-system and colon mechanism.
- **Conclusion**: Established evidence supports KRT2 as a marker of epithelial differentiation and keratinocyte biology. The interpretation that it represents epithelial contamination or variable epithelial abundance in this module is a plausible hypothesis, not a demonstrated cause of the module.

#### USP15

- **Related proteins** (co-abundance neighbors): SESN1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin specific peptidase 15. This gene encodes a member of the ubiquitin specific protease (USP) family of deubiquitinating enzymes. USP enzymes play critical roles in ubiquitin-dependent processes through polyubiquitin chain disassembly and hydrolysis of ubiquitin-substrate bonds. The encoded protein associates with the COP9 signalosome, and also plays a role in transforming growth factor beta signalling through deubiquitina…
- **Diseases (Open Targets)**: neurodegenerative disease (0.548); alcohol drinking (0.294); post term pregnancy (0.272); smoking initiation (0.217); injury (0.162)
- **Europe PMC papers**: 1872
- **Why important**: USP15 is directly connected to the SESN1 hub and encodes a deubiquitinating enzyme involved in protein stability, transforming-growth-factor signaling, and BMP signaling. HPA associates it with bone marrow and neutrophil-lineage cells, making it relevant both to cellular protein control and to possible immune-cell composition. It has a substantial literature and disease-association record.
- **Conclusion**: Established evidence supports USP15 as a regulator of ubiquitin-dependent signaling and protein stability with a notable hematopoietic expression context. Its contribution to a shared tissue stress program, or its role as an immune-composition indicator, remains hypothetical.

#### FARP1

- **Related proteins** (co-abundance neighbors): SESN1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FERM, ARH/RhoGEF and pleckstrin domain protein 1. This gene encodes a protein containing a FERM (4.2, exrin, radixin, moesin) domain, a Dbl homology domain, and two pleckstrin homology domains. These domains are found in guanine nucleotide exchange factors and proteins that link the cytoskeleton to the cell membrane. The encoded protein functions in neurons to promote dendritic growth. Alternative splicing results in multiple transcript variants.…
- **Diseases (Open Targets)**: neurodegenerative disease (0.361); Alzheimer disease (0.309); mathematical ability (0.286); aortic stenosis (0.278); alcohol drinking (0.267)
- **Europe PMC papers**: 556
- **Why important**: FARP1 is a module peripheral gene connected to SESN1 and encodes a membrane-associated guanine-nucleotide exchange factor with FERM, Dbl-homology, and pleckstrin-homology domains. Its established functions include neuronal dendritic growth, Rac signaling, synapse assembly, and postsynaptic actin-cytoskeleton organization. It has disease links involving neurodegeneration and cognition, making it particularly relevant to the autonomic-nervous-system side of the tissue pair.
- **Conclusion**: Established evidence supports FARP1 as a neuronal and cytoskeletal signaling protein. Its covariation with SESN1 in this module may indicate neuronal structural maintenance or indirect cell-composition effects, but the module does not establish either explanation.

#### ERCC4

- **Related proteins** (co-abundance neighbors): MAP7D1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ERCC excision repair 4, endonuclease catalytic subunit. The protein encoded by this gene forms a complex with ERCC1 and is involved in the 5' incision made during nucleotide excision repair. This complex is a structure specific DNA repair endonuclease that interacts with EME1. Defects in this gene are a cause of xeroderma pigmentosum complementation group F (XP-F), or xeroderma pigmentosum VI (XP6).[provided by RefSeq, Mar 2009].
- **Diseases (Open Targets)**: xeroderma pigmentosum group F (0.837); Fanconi anemia complementation group Q (0.808); xeroderma pigmentosum (0.780); xeroderma pigmentosum-Cockayne syndrome complex (0.731); XFE progeroid syndrome (0.730)
- **Europe PMC papers**: 2223
- **Why important**: ERCC4 is connected to MAP7D1 and encodes the catalytic component of a DNA-repair endonuclease complex with ERCC1 and EME1. It has established roles in nucleotide-excision repair, double-strand-break repair, homologous recombination, telomere maintenance, and xeroderma-pigmentosum-related disease. Its skeletal-muscle tissue enhancement and germ-cell-associated cell-type signals provide additional evidence that the module contains broad cellular-maintenance or composition-related features.
- **Conclusion**: Established evidence supports ERCC4 as a DNA-repair factor with strong disease relevance. Its participation in a shared stress or maintenance module is plausible, but a direct mechanistic connection to SESN1 or the colon-autonomic-nervous-system pairing is not established.

#### HEATR1

- **Related proteins** (co-abundance neighbors): SNX24 (0.85), SESN1 (0.85), NOL8 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HEAT repeat containing 1. Enables RNA binding activity. Involved in positive regulation of rRNA processing and positive regulation of transcription by RNA polymerase I. Located in fibrillar center and mitochondrion. Implicated in pancreatic ductal carcinoma. Biomarker of glioblastoma. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.475); Alzheimer disease (0.463); Parkinson disease (0.462); lysosomal storage disease (0.462); musculoskeletal system disorder (0.168)
- **Europe PMC papers**: 342
- **Why important**: HEATR1 occupies an internal position linking SESN1 with SNX24 and NOL8. It is associated with RNA binding, rRNA processing, small ribosomal-subunit biogenesis, and regulation of transcription by RNA polymerase. Its nucleolar localization, colon detection, and links to neurodegenerative disease and cancer make it a useful representative of the module's nucleolar and biosynthetic component.
- **Conclusion**: Established evidence supports HEATR1 as a nucleolar RNA-processing and ribosome-biogenesis factor. Its co-abundance with SESN1 may reflect coordinated growth and stress adaptation, but that relationship is a hypothesis rather than a demonstrated molecular pathway.

## Module 5

**Tissue pair**: autonomic_nervous_system and colon  
**Genes (11)**: AP3D1, CHRAC1, COPB1, DOHH, FEN1, GAB1, KATNAL1, LYSMD2, MYCBP, GAP43, THOP1

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING enrichment. Therefore, the module does not support a single statistically established pathway-level function. Its internal structure is organized around KATNAL1, which is connected to proteins involved in microtubule severing, intracellular trafficking, chromatin organization, DNA replication and repair, translation-factor maturation, and transcriptional regulation. A second smaller connection centered on GAP43 links neuronal growth or plasticity biology with GAB1 signaling and LYSMD2. The most defensible interpretation is therefore a mixed cellular-state module rather than a coherent pathway module. Established annotations suggest contributions from cytoskeletal remodeling, membrane and vesicle trafficking, genome maintenance, and neural growth or plasticity. These are biological interpretations of individual genes, not globally significant enrichment results.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of the genes is annotated as secreted. It is also not strongly blood-cell enriched. Most genes have low tissue specificity, while several show cell-type enhancement in specialized populations, particularly germ-cell populations; other signals include brain, colonocyte or enterocyte, esophageal, neuroendocrine, oligodendrocyte, cardiomyocyte, plasma-cell, and NK-cell contexts. HPA protein detection is available for most genes in colon, whereas no matching autonomic-nervous-system HPA tissue is available. GAP43 and DOHH have brain tissue associations, FEN1 has lymphoid-tissue enhancement, and GAB1 is immune-cell enhanced for NK cells, but the overall profile does not support a simple blood-contamination explanation. The shared module may instead reflect a mixture of broadly expressed intracellular proteins together with cell-state or cell-composition signals that differ between the two tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, no supplementary STRING functional enrichment was reported, and no hu.MAP complex contained at least two module members. Thus, the co-abundance relationships are not supported here by a dense set of previously catalogued physical or functional interactions. The strong co-abundance links, especially those involving KATNAL1 and the GAP43-centered branch, may represent coordinated expression, shared cellular state, tissue composition, indirect regulation, or context-dependent biology rather than direct protein binding. The absence of STRING or hu.MAP support is informative about current database coverage but does not demonstrate that the correlations are artifactual.

**STRING interactions (score >= 0.7)**: 0 of 55 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is potentially novel as a cross-tissue co-abundance pattern because its member combination is not represented by reported high-confidence STRING interactions or a shared hu.MAP complex, and because no coherent globally significant GO or KEGG signal defines it. However, it cannot be called a newly discovered biological mechanism from these facts alone. Several individual genes and their functions are well established, and the module contains recognizable cellular processes such as microtubule severing, vesicle trafficking, DNA repair, and neuronal growth responses. The defensible claim is that the particular coordinated pattern across autonomic nervous system and colon is not explained by the supplied interaction databases and merits validation, rather than that every relationship or the underlying biology is new.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular cell-state program that couples cytoskeletal remodeling and membrane trafficking with selective signaling and biosynthetic capacity. KATNAL1 may mark the central co-abundance axis, while GAP43 and GAB1 may represent a neural or regenerative signaling branch; AP3D1 and COPB1 could indicate vesicle trafficking, and FEN1, CHRAC1, DOHH, and MYCBP could reflect proliferation, genome maintenance, chromatin activity, or translational demand in the co-abundant cell state. THOP1 may connect this state to cytosolic peptide and neuropeptide processing. This is a hypothesis only: the lack of globally significant enrichment, STRING links, and hu.MAP complexes means that direct molecular coupling has not been established.

### Important genes

#### KATNAL1

- **Related proteins** (co-abundance neighbors): THOP1 (0.87), AP3D1 (0.85), CHRAC1 (0.84), GAP43 (0.83), FEN1 (0.83), COPB1 (0.81), DOHH (0.80), MYCBP (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Centrosome, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: katanin catalytic subunit A1 like 1. Enables identical protein binding activity and microtubule-severing ATPase activity. Involved in microtubule severing. Located in cytoplasm; microtubule; and spindle pole. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: refractive error (0.390); Abnormality of refraction (0.313); androgenetic alopecia (0.299); cirrhosis of liver (0.284); conduction system disorder (0.253)
- **Europe PMC papers**: 256
- **Why important**: KATNAL1 is the central network hub, connecting most of the other module members. Its established function is microtubule-severing ATPase activity, with roles in cytoplasmic microtubule organization and spermatogenesis. Its central position makes it the strongest candidate for organizing the module's co-abundance structure, although the network does not establish direct physical interactions. It has a moderate literature volume and disease associations including refractive error, androgenetic alopecia, cirrhosis, and conduction-system disorder.
- **Conclusion**: Established evidence supports KATNAL1 as the network-structuring marker and a microtubule-remodeling protein. It is plausible, but unproven, that variation in cytoskeletal or cell-state programs involving KATNAL1 helps generate the shared module.

#### GAP43

- **Related proteins** (co-abundance neighbors): KATNAL1 (0.83), LYSMD2 (0.83), GAB1 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: growth associated protein 43. The protein encoded by this gene has been termed a 'growth' or 'plasticity' protein because it is expressed at high levels in neuronal growth cones during development and axonal regeneration. This protein is considered a crucial component of an effective regenerative response in the nervous system. Alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. …
- **Diseases (Open Targets)**: neurodegenerative disease (0.429); DNA methylation (0.330); cholelithiasis (0.327); bone remodeling disease (0.321); skin infection (0.312)
- **Europe PMC papers**: 6590
- **Why important**: GAP43 forms the second visible network branch, connecting KATNAL1 with LYSMD2 and GAB1. It is tissue-enriched in brain, enhanced in several neuronal populations, detected in colon, and known as a growth or plasticity protein expressed during neuronal growth-cone formation and axonal regeneration. Its neuronal and regenerative biology gives it particular relevance to the autonomic-nervous-system side of the comparison. It also has substantial literature coverage and disease associations involving neurodegenerative disease and other conditions.
- **Conclusion**: Established evidence supports GAP43 as a neuronal growth and plasticity marker with a module-level bridging position. A role in linking autonomic neuronal signals to a colon cell-state program is a hypothesis, not a demonstrated mechanism.

#### GAB1

- **Related proteins** (co-abundance neighbors): GAP43 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GRB2 associated binding protein 1. The protein encoded by this gene is a member of the IRS1-like multisubstrate docking protein family. It is an important mediator of branching tubulogenesis and plays a central role in cellular growth response, transformation and apoptosis. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2008].
- **Diseases (Open Targets)**: cancer (0.595); bone development disease (0.565); hearing loss, autosomal recessive (0.383); Abnormality of the skeletal system (0.283); 15q14 microdeletion syndrome (0.278)
- **Europe PMC papers**: 12382
- **Why important**: GAB1 is connected to GAP43 and is an established multisubstrate docking protein involved in growth responses, transformation, apoptosis, angiogenesis, and receptor signaling. It is detected in colon and shows cell-type enhancement in cardiomyocytes, oligodendrocytes, plasma cells, and NK cells. Its signaling role and very large literature volume make it a useful candidate for interpreting the module as a context-dependent growth or response state rather than as a single metabolic pathway.
- **Conclusion**: Established evidence supports GAB1 as a signaling adaptor capable of integrating receptor-driven growth and survival signals. Its participation in this shared co-abundance module may indicate coordinated signaling-state variation, but the supplied data do not show that GAB1 directly regulates the other module genes.

#### FEN1

- **Related proteins** (co-abundance neighbors): KATNAL1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: flap structure-specific endonuclease 1. The protein encoded by this gene removes 5' overhanging flaps in DNA repair and processes the 5' ends of Okazaki fragments in lagging strand DNA synthesis. Direct physical interaction between this protein and AP endonuclease 1 during long-patch base excision repair provides coordinated loading of the proteins onto the substrate, thus passing the substrate from one enzyme to another. The protein is…
- **Diseases (Open Targets)**: neurodegenerative disease (0.496); HIV infectious disease (0.370); hepatocellular carcinoma (0.213); breast carcinoma (0.213); oral cavity squamous cell carcinoma (0.208)
- **Europe PMC papers**: 5275
- **Why important**: FEN1 is a well-characterized DNA replication and repair nuclease, including roles in Okazaki-fragment processing, base-excision repair, and homologous-recombination-associated double-strand-break repair. It is detected in colon and shows enhancement in lymphoid tissue and several germ-cell populations. Its strong literature base and cancer-related disease associations make it informative for assessing whether the module includes a proliferative or genome-maintenance component.
- **Conclusion**: Established evidence supports FEN1 as a genome-maintenance protein and a possible marker of replication or repair demand. It should not be interpreted as proof that the entire module is a DNA-repair module, because no GO or KEGG term passed global correction.

#### THOP1

- **Related proteins** (co-abundance neighbors): KATNAL1 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thimet oligopeptidase 1. The protein encoded by this gene is a kininase that uses zinc as a cofactor. The encoded oligopeptidase cleaves cytosolic peptides, making them unavailable for display on antigen-presenting cells. This protein also cleaves neuropeptides under 20 aa in length and can degrade beta-amyloid precursor protein to amyloidogenic peptides. [provided by RefSeq, Nov 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.371); Hypercholesterolemia (0.325); atrial fibrillation (0.246); asthma (0.245); neuroendocrine neoplasm (0.144)
- **Europe PMC papers**: 460
- **Why important**: THOP1 is directly connected to the KATNAL1 hub and is detected in colon, with cell-type enhancement in colonocytes, enterocytes, and hepatocytes. It is a cytosolic zinc-dependent oligopeptidase that processes short cytosolic peptides and neuropeptides. This provides a biologically relevant link between peptide handling in colon-associated cells and neuropeptide biology relevant to autonomic tissues. Its disease associations include neurodegenerative disease, hypercholesterolemia, atrial fibrillation, asthma, and neuroendocrine neoplasm.
- **Conclusion**: Established evidence supports THOP1 as a cytosolic peptide-processing enzyme with relevance to both intestinal and neural contexts. Its connection to the module's cross-tissue interpretation is plausible, but whether it mediates the co-abundance pattern is unresolved.

## Module 6

**Tissue pair**: autonomic_nervous_system and colon  
**Genes (5)**: APOA1, HBA1, KCTD12, GC, VTN

### Function

(GO:CC blood microparticle; q_global = 0.000208) supports a blood-microparticle and circulating-plasma-associated module, driven by APOA1, GC, HBA1, and VTN. APOA1 contributes lipid transport and cholesterol efflux, GC contributes vitamin D transport, VTN contributes cell-matrix adhesion and integrin-related signaling, and HBA1 contributes oxygen, carbon-dioxide, and nitric-oxide transport. The most cautious interpretation is therefore a circulating blood or extracellular-particle signature rather than a tissue-intrinsic autonomic-nervous-system or colon pathway. The co-abundance of KCTD12 with VTN is compatible with a possible link to receptor and G-protein-coupled signaling, but KCTD12 has no primary GO/KEGG enrichment support in this module. Established evidence is strongest for the blood-microparticle interpretation; a direct shared biological pathway across the two tissues remains a hypothesis.

**Cell composition.** The module is strongly dominated by secreted or blood-associated proteins. APOA1, GC, and VTN are secreted to blood and are tissue-enriched in liver, while HBA1 is enriched in erythrocytes and hematopoietic tissues. HPA evidence also links parts of the module to immune-cell populations, including myeloid and plasmacytoid dendritic-cell contexts. This composition raises an important sampling explanation: the conserved signal may reflect plasma, blood microparticles, erythrocyte material, or shared vascular and immune components present in both tissue datasets, rather than comparable expression by autonomic-nervous-system and colon parenchymal cells. GC is detected in colon, whereas several other module proteins are not detected there by immunohistochemistry, which further favors a circulating or extracellular contribution.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 0.000208 | APOA1, GC, HBA1, VTN |

### STRING and hu.MAP

STRING provides one high-confidence pair, APOA1–VTN, supporting a known relationship between two central extracellular proteins. The absence of STRING partners for GC, HBA1, and KCTD12 in this module means that their co-abundance should not be treated as established direct physical interaction. STRING supplementary enrichment (STRING Component Blood microparticle; within-query FDR = 6.85e-05) and (STRING COMPARTMENTS Blood microparticle; within-query FDR = 7.3e-05) independently place APOA1, GC, HBA1, and VTN in the blood-microparticle compartment, while (STRING PMID (2020) Revelation of Proteomic Indicators for Colorectal Cancer in Initial Stages of Development.; within-query FDR = 0.0104) and (STRING PMID (2014) Validation of semaphorin 7A and ala-beta-his-dipeptidase as biomarkers associated with the conversion from clinically isolated syndrome to multiple sclerosis.; within-query FDR = 0.0456) show disease- or biomarker-context associations but are not primary global enrichment evidence. hu.MAP provides additional support for shared complex or proteomic-context membership: APOA1, GC, and HBA1 co-occur in (hu.MAP huMAP3_15040.1), and APOA1 with GC co-occur in (hu.MAP huMAP3_08224.1), (hu.MAP huMAP3_09434.1), and (hu.MAP huMAP3_10678.1). These complexes contain many plasma, complement, coagulation, and transport proteins, so they support a shared circulating-protein context more strongly than a unique tissue-specific complex. KCTD12 has no STRING or hu.MAP support here.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: APOA1–VTN (0.755)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Blood microparticle (FDR = 6.85e-05, 4 genes); COMPARTMENTS Blood microparticle (FDR = 7.3e-05, 4 genes); PMID (2020) Revelation of Proteomic Indicators for Colorectal Cancer in Initial Stages of Development. (FDR = 0.0104, 4 genes); PMID (2014) Validation of semaphorin 7A and ala-beta-his-dipeptidase as biomarkers associated with the conversion from clinically isolated syndrome to multiple sclerosis. (FDR = 0.0456, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (APOA1, GC, HBA1; 3/64); huMAP3_08224.1 (APOA1, GC; 2/21); huMAP3_09434.1 (APOA1, GC; 2/33); huMAP3_10678.1 (APOA1, GC; 2/71)

### Novelty

This should not be presented as a wholly new molecular function. The individual proteins have established plasma, lipid-transport, vitamin-transport, extracellular-matrix, or erythrocyte-related roles, and the blood-microparticle association is supported by both (GO:CC blood microparticle; q_global = 0.000208) and the supplementary STRING results. A conserved co-abundance pattern across autonomic nervous system and colon could still be a useful dataset-level observation, especially because KCTD12 does not fit the otherwise strongly circulating composition, but the fact sheet does not establish that this is a new biological complex or a new mechanism. Lack of STRING or hu.MAP support alone cannot establish novelty. The most defensible conclusion is that the module-level cross-tissue observation may be under-characterized, while its dominant molecular content and broad biological context are already well established.

**Hypothesis.** Hypothesis: the conserved module reflects coordinated abundance of circulating extracellular material, including lipoprotein-associated proteins, vitamin-D transport protein, vitronectin-containing extracellular particles, and erythrocyte-derived hemoglobin, that is captured in both tissue proteomes. APOA1 and VTN may provide the most plausible extracellular interaction axis, GC may represent linked plasma transport biology, and HBA1 may indicate blood or microparticle carryover. KCTD12 may mark a tissue or immune-cell-associated regulatory connection to the extracellular signal, but this proposed bridge is not established by the available interaction or enrichment evidence. This hypothesis should be tested with cell-type-resolved measurements, plasma-depletion or blood-contamination controls, and independent validation of the cross-tissue co-abundance pattern.

### Important genes

#### APOA1

- **Related proteins** (co-abundance neighbors): HBA1; HBA2 (0.86), GC (0.81), VTN (0.81); STRING partners: VTN (0.755)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08224.1, huMAP3_09434.1, huMAP3_10678.1
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 has the strongest network centrality in the module and connects to VTN, GC, and hemoglobin-related module neighbors. It is a major HDL protein, promotes cholesterol efflux, and is secreted to blood. It is present in the primary term (GO:CC blood microparticle; q_global = 0.000208), all listed STRING supplementary terms, and the hu.MAP contexts (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_10678.1). Its extensive literature and disease-association record make it the clearest anchor for interpreting the module as circulating lipid and extracellular biology.
- **Conclusion**: Established: APOA1 is a central, secreted plasma protein with lipid-transport and cholesterol-efflux functions and a supported association with VTN. Conclusion: it is the principal biological anchor of the module. Hypothesis: its abundance may help capture circulating lipoprotein or blood-microparticle material shared across the tissue datasets.

#### GC

- **Related proteins** (co-abundance neighbors): APOA1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08224.1, huMAP3_09434.1, huMAP3_10678.1
- **Function (MyGene.info)**: GC vitamin D binding protein. The protein encoded by this gene belongs to the albumin gene family. It is a multifunctional protein found in plasma, ascitic fluid, cerebrospinal fluid and on the surface of many cell types. It binds to vitamin D and its plasma metabolites and transports them to target tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq,…
- **Diseases (Open Targets)**: vitamin D deficiency (0.574); vitamin deficiency (0.552); chronic obstructive pulmonary disease (0.499); squamous cell carcinoma (0.339); central nervous system cancer (0.334)
- **Europe PMC papers**: 363974
- **Why important**: GC is connected to APOA1 and appears in the primary blood-microparticle term (GO:CC blood microparticle; q_global = 0.000208), all listed STRING supplementary terms, and the hu.MAP contexts (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_10678.1). It is liver-enriched, secreted to blood, and transports vitamin D and its metabolites. Its very large literature base and disease associations provide strong independent biological context for a plasma transport interpretation.
- **Conclusion**: Established: GC is a multifunctional circulating vitamin-D transport protein that co-occurs with APOA1 in several plasma-associated hu.MAP contexts. Conclusion: it strengthens the interpretation of the module as a blood or extracellular transport signature. Hypothesis: variation in GC abundance could reflect systemic transport or plasma composition rather than local activity in both tissues.

#### VTN

- **Related proteins** (co-abundance neighbors): KCTD12 (0.81), APOA1 (0.81); STRING partners: APOA1 (0.755)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vitronectin. The protein encoded by this gene functions in part as an adhesive glycoprotein. Differential expression of this protein can promote either cell adhesion or migration as it links cells to the extracellular matrix through a variety of ligands. These ligands include integrins, plasminogen activator inhibitor-1, and urokinase plasminogen activator receptor. This secreted protein can be present in the …
- **Diseases (Open Targets)**: hypertensive disorder (0.421); dengue disease (0.376); neurodegenerative disease (0.343); temporal arteritis (0.338); age-related macular degeneration (0.313)
- **Europe PMC papers**: 3940
- **Why important**: VTN is connected to APOA1 and KCTD12 and is present in (GO:CC blood microparticle; q_global = 0.000208) and all listed STRING supplementary terms. It is a secreted blood protein with extracellular-matrix, adhesion, migration, and integrin-related functions. Its STRING relationship with APOA1 is the only high-confidence pairwise interaction reported for the module, making VTN important for linking the circulating signature to extracellular adhesion biology.
- **Conclusion**: Established: VTN is a secreted extracellular adhesion protein and has a supported high-confidence STRING relationship with APOA1. Conclusion: it is the strongest candidate for an extracellular-matrix or particle-associated interaction component. Hypothesis: VTN may provide a mechanistic bridge between circulating protein abundance and cell-adhesion or vascular-interface processes, but this is not demonstrated in the two tissues.

#### HBA1

- **Related proteins** (co-abundance neighbors): none; STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: hemoglobin subunit alpha 1. The human alpha globin gene cluster located on chromosome 16 spans about 30 kb and includes seven loci: 5'- zeta - pseudozeta - mu - pseudoalpha-1 - alpha-2 - alpha-1 - theta - 3'. The alpha-2 (HBA2) and alpha-1 (HBA1) coding sequences are identical. These genes differ slightly over the 5' untranslated regions and the introns, but they differ significantly over the 3' untranslated regions. Two alp…
- **Diseases (Open Targets)**: alpha thalassemia spectrum (0.758); hemoglobin H disease (0.755); hemoglobin M disease (0.735); Heinz body anemia (0.698); primary familial polycythemia due to EPO receptor mutation (0.689)
- **Europe PMC papers**: 4551
- **Why important**: HBA1 is part of the primary blood-microparticle term (GO:CC blood microparticle; q_global = 0.000208) and the supplementary STRING terms (STRING Component Blood microparticle; within-query FDR = 6.85e-05), (STRING COMPARTMENTS Blood microparticle; within-query FDR = 7.3e-05), and (STRING PMID (2020) Revelation of Proteomic Indicators for Colorectal Cancer in Initial Stages of Development.; within-query FDR = 0.0104). It is enriched in erythrocytes and hematopoietic tissues and has established roles in oxygen, carbon-dioxide, nitric-oxide, and oxidative-stress-related biology. Its presence in the hu.MAP plasma-associated context (hu.MAP huMAP3_15040.1) makes it a useful indicator of erythrocyte or blood-derived material, despite having no reported STRING partner in this module.
- **Conclusion**: Established: HBA1 is an erythrocyte-associated hemoglobin subunit and contributes to the blood-microparticle signal. Conclusion: it is more informative as a composition or sample-origin marker than as evidence for a specific intracellular module mechanism. Hypothesis: HBA1 abundance may indicate erythrocyte-derived particles or blood carryover shared between the tissue preparations.

#### KCTD12

- **Related proteins** (co-abundance neighbors): VTN (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: potassium channel tetramerization domain containing 12. Enables identical protein binding activity. Predicted to be involved in protein homooligomerization. Predicted to act upstream of or within regulation of G protein-coupled receptor signaling pathway. Predicted to be located in cell projection. Predicted to be part of receptor complex. Predicted to be active in postsynaptic membrane and presynaptic membrane. [provided by Alliance of Genome Resource…
- **Diseases (Open Targets)**: adolescent idiopathic scoliosis (0.315); alcohol drinking (0.313); stroke disorder (0.296); sialolithiasis (0.251); Tietze syndrome (0.239)
- **Europe PMC papers**: 741
- **Why important**: KCTD12 is the least connected and least externally supported member, linking only to VTN in the reported module network and lacking STRING partners, hu.MAP complexes, and enriched GO/KEGG or STRING terms. It is nevertheless biologically distinctive because its annotations involve protein oligomerization, receptor complexes, G-protein-coupled signaling, and nervous-system development. Its immune-cell and macrophage-related HPA patterns make it a potentially informative outlier against the otherwise plasma-dominated composition.
- **Conclusion**: Established: KCTD12 has annotations compatible with receptor and G-protein-coupled signaling and shows immune-cell-associated HPA patterns, but the module provides no independent interaction or enrichment support for a specific role. Conclusion: it should be treated as a provisional contextual marker, not as proof of a neuronal mechanism. Hypothesis: KCTD12 may connect a cell-associated signaling state to the extracellular VTN signal, a possibility requiring targeted validation.

## Module 7

**Tissue pair**: autonomic_nervous_system and colon  
**Genes (19)**: ACTR8, RNF40, CCDC117, CHD1, CRACD, CWC27, HMG20A, ISY1, MKI67, NELFE, SAP30BP, SEZ6L2, SPATS2, SPIN1, SUPT7L, UBR5, ATP6V0A1, WDHD1, ZNF318

### Function

No GO or KEGG term passed global correction, and STRING reported no functional enrichment. The gene annotations nevertheless suggest a broad nuclear regulatory program involving pre-mRNA splicing, chromatin remodeling, transcriptional regulation, DNA replication and repair, ubiquitin-mediated regulation, and cellular proliferation. A smaller subset points to neuronal or vesicular functions and gastrointestinal epithelial structure. The best-supported interpretation is therefore a broadly regulated cell-state module rather than one established pathway.

**Cell composition.** None of the genes is annotated as secreted, so this is not a plasma-protein or secreted-protein module. Most genes have low tissue specificity, while the remaining genes show diverse enrichment in brain, intestine, lymphoid tissue, testis, bone marrow, germ-cell populations, erythroid progenitors, megakaryocyte progenitors, and neural cell types. Overall immune-cell specificity is low, although some genes have immune or hematopoietic associations. Colon protein detection is broad among genes with available data, while matching autonomic-nervous-system protein data are unavailable. The shared signal may therefore reflect broadly expressed nuclear machinery, mixed cell populations, or a shared proliferative or epithelial state rather than a tissue-specific autonomic-colon function.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no STRING functional-enrichment result was available. No hu.MAP complex contained multiple module members. Thus, the co-abundance relationships are not supported by established physical-interaction or complex annotations in these resources. This does not exclude indirect biological coordination, shared transcriptional regulation, or cell-composition effects.

**STRING interactions (score >= 0.7)**: 0 of 171 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The particular cross-tissue co-abundance pattern may be novel because it is not represented by high-confidence STRING interactions or a shared hu.MAP complex. However, absence from those resources does not prove novelty. The individual functions are not novel: CWC27 and ISY1 have spliceosomal annotations; CHD1, ACTR8, SUPT7L, HMG20A, and NELFE have chromatin or transcriptional roles; MKI67 is associated with proliferation; CRACD has epithelial and actin-related annotations; and ATP6V0A1 mediates vesicular acidification. The defensible novelty claim concerns the observed combination and its reproducibility, not a newly established molecular complex.

**Hypothesis.** Hypothesis: the module reflects a shared cell-state program in which RNA processing, chromatin regulation, DNA maintenance, and proliferation-related processes covary with epithelial or neuronal cellular features. In colon, the signal could involve epithelial or proliferative cells; in autonomic nervous system samples, it could involve neural or glial cell states together with broadly expressed nuclear genes. The association may be indirect and partly driven by cell-type composition. Cell-resolved profiling, independent cohorts, and perturbation experiments would be needed to test this hypothesis.

### Important genes

#### CWC27

- **Related proteins** (co-abundance neighbors): CCDC117 (0.86), SUPT7L (0.83), SPIN1 (0.82), SAP30BP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CWC27 spliceosome associated cyclophilin. Predicted to enable peptidyl-prolyl cis-trans isomerase activity. Predicted to be involved in protein peptidyl-prolyl isomerization. Located in nucleoplasm. Part of U2-type precatalytic spliceosome and catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: metaphyseal chondrodysplasia-retinitis pigmentosa syndrome (0.764); retinitis pigmentosa (0.450); inherited retinal dystrophy (0.433); Abnormality of the skeletal system (0.421); diverticular disease (0.394)
- **Europe PMC papers**: 282
- **Why important**: CWC27 is among the more connected genes in the module and links to several other nuclear regulatory genes. It is annotated as a spliceosome-associated cyclophilin involved in pre-mRNA splicing and protein peptidyl-prolyl isomerization. It has disease associations involving skeletal, retinal, and diverticular disorders and has a substantive literature base.
- **Conclusion**: Established evidence supports CWC27 as a spliceosome-associated nuclear regulator. Its network position is compatible with coordination of RNA processing in the module, but the co-abundance pattern does not establish a new physical interaction or show that altered splicing causes the shared tissue signal.

#### CHD1

- **Related proteins** (co-abundance neighbors): SAP30BP (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromodomain helicase DNA binding protein 1. The CHD family of proteins is characterized by the presence of chromo (chromatin organization modifier) domains and SNF2-related helicase/ATPase domains.  CHD genes alter gene expression possibly by modification of chromatin structure thus altering access of the transcriptional apparatus to its chromosomal DNA template. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: intellectual disability with language impairment (0.714); gestational diabetes (0.363); breast carcinoma (0.349); developmental and epileptic encephalopathy (0.340); nervous system disorder (0.255)
- **Europe PMC papers**: 4137
- **Why important**: CHD1 is a chromatin-remodeling helicase with a very extensive literature base and established roles in nucleosome organization and chromatin remodeling. It is connected to SAP30BP in the module and has disease associations involving intellectual-developmental and neurological disorders.
- **Conclusion**: Established evidence supports CHD1 as a regulator of chromatin accessibility and transcription. Its presence supports a chromatin-related interpretation, but the module does not demonstrate that CHD1 forms a new complex with the other genes.

#### MKI67

- **Related proteins** (co-abundance neighbors): SAP30BP (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Nucleoli rim; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: marker of proliferation Ki-67. This gene encodes a nuclear protein that is associated with and may be necessary for cellular proliferation. Alternatively spliced transcript variants have been described. A related pseudogene exists on chromosome X. [provided by RefSeq, Mar 2009]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.461); neurodegenerative disease (0.370); type 1 diabetes mellitus (0.324); urolithiasis (0.293); alcohol drinking (0.293)
- **Europe PMC papers**: 14932
- **Why important**: MKI67 is a well-established nuclear proliferation marker associated with chromosome segregation, mitotic regulation, and cell population proliferation. It is connected to SAP30BP and has a very large literature base. HPA links it to bone marrow, lymphoid tissue, and several proliferative progenitor populations.
- **Conclusion**: Established evidence supports MKI67 as a marker of proliferative cell states rather than as a specific autonomic-colon pathway component. Its presence makes cell-state or cell-composition effects an important alternative explanation. A causal organizing role for MKI67 in the module is not established.

#### SEZ6L2

- **Related proteins** (co-abundance neighbors): WDHD1 (0.91), CCDC117 (0.86), NELFE (0.85), UBR5 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: seizure related 6 homolog like 2. This gene encodes a seizure-related protein that is localized on the cell surface. The gene is located in a region of chromosome 16p11.2 that is thought to contain candidate genes for autism spectrum disorders (ASD), though there is no evidence directly implicating this gene in ASD. Increased expression of this gene has been found in lung cancers, and the protein is therefore considered to be a no…
- **Diseases (Open Targets)**: neurodegenerative disease (0.274); colorectal carcinoma (0.077); hepatocellular carcinoma (0.075); intrahepatic cholangiocarcinoma (0.074); neoplasm (0.065)
- **Europe PMC papers**: 559
- **Why important**: SEZ6L2 is one of the more connected module genes and links to WDHD1, CCDC117, NELFE, and UBR5. HPA shows tissue enhancement in brain and cell-type enhancement in neuronal and pituitary populations. Its annotations include synapse maturation and locomotory behavior, and it has substantial literature and neurological and cancer disease associations.
- **Conclusion**: Established evidence supports SEZ6L2 as a cell-surface seizure-related protein with neural expression and synaptic-development associations. It could connect the module to autonomic or neural biology, but the absence of STRING and hu.MAP support means that a shared neural mechanism remains hypothetical.

#### CRACD

- **Related proteins** (co-abundance neighbors): SPIN1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: capping protein inhibiting regulator of actin dynamics. Involved in negative regulation of barbed-end actin filament capping. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: esophageal disorder (0.337); response to selective serotonin reuptake inhibitor (0.302); urolithiasis (0.267); alcohol drinking (0.267); hematologic disorder (0.251)
- **Europe PMC papers**: 159
- **Why important**: CRACD is connected to SPIN1 and is tissue-enhanced in intestine and testis. Its cell-type associations include enterocytes and several progenitor populations. Its annotations include maintenance of gastrointestinal epithelium and regulation of actin filament dynamics, making it particularly relevant to the colon component.
- **Conclusion**: Established evidence supports CRACD as an epithelial-structure and actin-regulatory gene with intestinal relevance. Its module association is compatible with a colon epithelial contribution, but its joint occurrence with neural and nuclear-regulatory genes may reflect shared cell-state regulation or sample composition rather than one established pathway.

## Module 8

**Tissue pair**: autonomic_nervous_system and colon  
**Genes (9)**: ASCC1, DRG2, GAL, MAPK9, PIK3CA, SEPTIN5, TRAPPC11, TTC5, ZFAND5

### Function

The module does not have a globally significant GO or KEGG enrichment, and there is no supplementary STRING functional enrichment. Its structure is centered on GAL, with connections to genes involved in signaling, transcriptional regulation, vesicle trafficking, and cellular stress responses; a smaller TTC5–SEPTIN5 branch is also present. The strongest biological interpretation is therefore a possible neuroendocrine and secretory-signaling program rather than a demonstrated single pathway. GAL is an established neuropeptide precursor expressed in nervous and gastrointestinal tissues and associated with neuropeptide signaling, feeding, nociception, and energy regulation. TRAPPC11 supports intracellular secretory trafficking, while PIK3CA and MAPK9 represent signaling kinases and ASCC1 represents transcriptional coactivation. These annotations are compatible with coordinated regulation of peptide secretion and stimulus-responsive cellular programs, but the absence of globally significant enrichment means this interpretation remains gene-based rather than pathway-level proof.

**Cell composition.** The module is not dominated by secreted or plasma proteins: GAL is the sole secreted gene identified by HPA. Most genes have low tissue specificity and low immune-cell specificity, and the HPA profile does not support a broadly blood-cell-derived module. There are isolated tissue or cell-type associations with pituitary endocrine cells, brain, skeletal muscle, cardiomyocytes, neutrophils, basophils, eosinophils, and astrocytes, but these are distributed across different genes rather than forming a coherent cell-type signature. Colon protein detection is common among the annotated genes, whereas autonomic-nervous-system protein data are unavailable in the supplied HPA summary. Thus, shared cell composition or general expression could contribute to the cross-tissue module, but a simple plasma-protein or blood-contamination explanation is not supported.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction meets the supplied high-confidence threshold, and no STRING functional enrichment is reported. No hu.MAP complex contains multiple module members. Consequently, the co-abundance relationships are not corroborated as known physical interactions or a known multiprotein complex by these resources. The network may reflect coordinated expression, indirect regulation, shared cellular state, or tissue composition rather than direct protein binding. The GAL-centered topology is especially notable as a co-abundance pattern, but it should not be interpreted as evidence that GAL physically interacts with its connected genes.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module is potentially novel as a cross-tissue co-abundance pattern because its membership and connectivity are not represented by high-confidence STRING interactions or a shared hu.MAP complex. However, absence from those resources does not establish biological novelty: the individual genes and many of their functions are already well characterized, and co-abundance can arise from shared regulation or cell composition. The defensible conclusion is that the specific autonomic-nervous-system and colon module is a candidate new systems-level association requiring independent replication, perturbation, and validation in matched cell types.

**Hypothesis.** Hypothesis: the module represents a coordinated neuroendocrine secretory-response state shared by autonomic nervous system and colon samples. In this model, GAL marks the peptide-signaling component; TRAPPC11 supports secretory-pathway trafficking; PIK3CA and MAPK9 transmit extracellular or cellular stimuli; and ASCC1, TTC5, and related nuclear proteins shape transcriptional or stress-responsive output. SEPTIN5 may connect this state to cytoskeletal organization and regulated vesicle exocytosis. This hypothesis predicts that module activity will track GAL production or release and will covary with secretory, signaling, and vesicle-trafficking measurements, but it is not established by the supplied co-abundance data.

### Important genes

#### GAL

- **Related proteins** (co-abundance neighbors): ZFAND5 (0.95), PIK3CA (0.88), DRG2 (0.87), MAPK9 (0.87), ASCC1 (0.84), TTC5 (0.84), TRAPPC11 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Golgi apparatus; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galanin and GMAP prepropeptide. This gene encodes a neuroendocrine peptide that is widely expressed in the central and peripheral nervous systems and also the gastrointestinal tract, pancreas, adrenal gland and urogenital tract. The encoded protein is a precursor that is proteolytically processed to generate two mature peptides: galanin and galanin message-associated peptide (GMAP). Galanin has diverse physiological functions in…
- **Diseases (Open Targets)**: temporal lobe epilepsy (0.467); neurodegenerative disease (0.458); autosomal dominant epilepsy with auditory features (0.418); ankylosing spondylitis (0.213); Abnormality of the skeletal system (0.144)
- **Europe PMC papers**: 127064
- **Why important**: GAL is the hub-like gene in the module and has the strongest network connectivity. It encodes a neuroendocrine precursor processed into galanin and GMAP, with established roles in neuropeptide signaling, nociception, feeding, energy homeostasis, and gastrointestinal biology. Its pituitary enrichment, endocrine-cell associations, secretion to blood, colon detection, disease links involving epilepsy and neurodegeneration, and very large literature base make it the clearest biological anchor.
- **Conclusion**: Established evidence supports GAL as a neuroendocrine and gastrointestinal signaling marker and as the central co-abundance feature of this module. It is plausible, but not demonstrated, that GAL organizes the shared module or drives the other genes.

#### PIK3CA

- **Related proteins** (co-abundance neighbors): GAL (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Primary cilium, Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit alpha. Phosphatidylinositol 3-kinase is composed of an 85 kDa regulatory subunit and a 110 kDa catalytic subunit. The protein encoded by this gene represents the catalytic subunit, which uses ATP to phosphorylate PtdIns, PtdIns4P and PtdIns(4,5)P2. This gene has been found to be oncogenic and has been implicated in cervical cancers. A pseudogene of this gene has been defined on chromosome 22. [provided b…
- **Diseases (Open Targets)**: megalencephaly-capillary malformation-polymicrogyria syndrome (0.849); CLOVES syndrome (0.795); PIK3CA-related overgrowth spectrum (0.770); breast cancer (0.754); Cowden syndrome 5 (0.754)
- **Europe PMC papers**: 45816
- **Why important**: PIK3CA is a catalytic subunit of phosphatidylinositol three-kinase and is connected directly to GAL in the module. Its established signaling functions include growth-factor and insulin-receptor pathways, and it has strong disease associations involving developmental overgrowth syndromes and cancer. Its broad literature base makes it a useful candidate for linking neuroendocrine or extracellular signals to intracellular growth and survival responses.
- **Conclusion**: Established evidence supports PIK3CA as a major signal-transduction component with disease relevance. The module does not establish a GAL–PIK3CA molecular interaction or show that this pathway is enriched in the shared tissues.

#### MAPK9

- **Related proteins** (co-abundance neighbors): GAL (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Immune cell enriched; location Plasma membrane, Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitogen-activated protein kinase 9. The protein encoded by this gene is a member of the MAP kinase family. MAP kinases act as an integration point for multiple biochemical signals, and are involved in a wide variety of cellular processes such as proliferation, differentiation, transcription regulation and development. This kinase targets specific transcription factors, and thus mediates immediate-early gene expression in response to…
- **Diseases (Open Targets)**: cancer (0.561); neoplasm (0.105); discoid lupus erythematosus (0.095); hepatocellular carcinoma (0.095); Abnormal central motor function (0.092)
- **Europe PMC papers**: 2501
- **Why important**: MAPK9 is directly connected to GAL and encodes a JNK-family mitogen-activated protein kinase that integrates cellular stimuli and regulates transcription factors. Its annotations include MAPK and JNK cascades, protein phosphorylation, and stimulus-responsive gene regulation. Its immune-cell association and disease literature, including cancer-related associations, make it a plausible indicator of context-dependent cellular signaling.
- **Conclusion**: Established evidence supports MAPK9 as a stimulus-responsive signaling kinase. Its participation in a GAL-linked secretory program is a hypothesis from the co-abundance pattern, not a demonstrated biochemical relationship.

#### TRAPPC11

- **Related proteins** (co-abundance neighbors): GAL (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: trafficking protein particle complex subunit 11. The protein encoded by this gene is a subunit of the TRAPP (transport protein particle) tethering complex, which functions in intracellular vesicle trafficking. This subunit is involved in early stage endoplasmic reticulum-to-Golgi vesicle transport. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jan 2013].
- **Diseases (Open Targets)**: autosomal recessive limb-girdle muscular dystrophy type R18 (0.805); autosomal recessive limb-girdle muscular dystrophy (0.554); neurodegenerative disease (0.485); hereditary disease (0.471); limb-girdle muscular dystrophy (0.458)
- **Europe PMC papers**: 377
- **Why important**: TRAPPC11 is directly connected to GAL and is a subunit of the TRAPP tethering complex involved in endoplasmic-reticulum-to-Golgi transport, Golgi organization, and the constitutive secretory pathway. This function provides a mechanistic bridge between a secreted neuroendocrine product and intracellular trafficking. Its established associations with limb-girdle muscular dystrophy and neurodegenerative disease add disease relevance despite a more modest literature base.
- **Conclusion**: Established evidence supports TRAPPC11 as a vesicle-trafficking and secretory-pathway component. It may support coordinated GAL handling or secretion, but the module does not prove such a causal connection.

#### SEPTIN5

- **Related proteins** (co-abundance neighbors): TTC5 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm, Actin filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: septin 5. This gene is a member of the septin gene family of nucleotide binding proteins, originally described in yeast as cell division cycle regulatory proteins. Septins are highly conserved in yeast, Drosophila, and mouse and appear to regulate cytoskeletal organization. Disruption of septin function disturbs cytokinesis and results in large multinucleate or polyploid cells. This gene is mapped to 22q11,…
- **Diseases (Open Targets)**: Bernard-Soulier syndrome (0.582); Thrombocytopenia (0.491); Macrothrombocytopenia (0.484); autosomal dominant macrothrombocytopenia (0.359); hair color (0.313)
- **Europe PMC papers**: 159
- **Why important**: SEPTIN5 is the exact module gene forming the second small network branch through TTC5. It is associated with cytoskeletal organization, intracellular protein localization, and regulation of synaptic-vesicle exocytosis. Its brain and neuronal cell-type associations, blood-cell group enrichment, and links to platelet disorders provide biological context for a vesicle and membrane-remodeling interpretation.
- **Conclusion**: Established evidence supports SEPTIN5 as a cytoskeletal and exocytosis-related protein with neural and platelet-relevant biology. Its connection to the GAL-centered branch may indicate coordinated vesicle biology, but it is not evidence of a known physical complex.

## Module 9

**Tissue pair**: autonomic_nervous_system and colon  
**Genes (19)**: BRAP, CDC7, CENPE, CEP97, CHURC1, CLASP1, HMGXB4, KRT9, LARP4, MANEAL, MOCS2, MSTO1, NAA16, NAA20, PTS, SCOC, TCP11L1, UBE2S, UXT

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent; therefore the module should not be assigned a statistically established pathway function. Its gene-level biology is heterogeneous but converges on cellular proliferation and structural maintenance. CDC7, CENPE and CLASP1 support DNA-replication initiation, mitotic progression, chromosome movement and microtubule organization. UBE2S contributes ubiquitin-dependent cell-cycle protein turnover, while UXT, CEP97 and related genes connect to centrosome, cilium and microtubule biology. NAA16 and NAA20 support co-translational protein acetylation, PTS supports tetrahydrobiopterin biosynthesis, and MSTO1 supports mitochondrial organization. The most defensible interpretation is a co-abundance signature combining cell-cycle and cytoskeletal state with protein maturation and metabolic functions, rather than a single well-defined biochemical pathway. These annotations are gene-level evidence and do not establish that all functions operate together in this module.

**Cell composition.** The module is predominantly intracellular rather than plasma or secreted: only MANEAL carries a secretome annotation, and the remaining genes are annotated to compartments such as nucleoplasm, cytosol, Golgi, centrosome, microtubules or mitochondria. The HPA profile is mixed, with many genes showing low tissue specificity and many showing cell-type enhancement. Enrichment patterns include testis, bone marrow, lymphoid tissue, brain and pancreas, with prominent germ-cell and epithelial cell-type annotations. Most genes have low immune-cell specificity, so this is not strongly characteristic of a blood-cell module, although CENPE and CLASP1 have particular blood or immune-cell annotations. Protein detection in colon is common among the genes with available data, whereas there is no matching HPA tissue for autonomic nervous system. Thus, the shared signal is more consistent with a broadly distributed intracellular or cell-state program, potentially influenced by shared proliferative, epithelial, neuronal or germ-cell-like features, than with circulating plasma proteins or a simple blood-contamination signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

Only two high-confidence STRING relationships are present within the module: CENPE with CLASP1 and NAA16 with NAA20. These provide established support for a microtubule-associated relationship and an N-terminal acetylation relationship, respectively. The remaining co-abundance links are not supported by the reported high-confidence STRING interaction set, so they should be interpreted as expression covariation rather than established physical interactions. No STRING functional enrichment was detected. No hu.MAP complex contains multiple module members. Overall, the module has limited support from known physical interaction or complex databases and appears more like a coordinated expression neighborhood than a previously recognized protein complex.

**STRING interactions (score >= 0.7)**: 2 of 171 gene pairs: CENPE–CLASP1 (0.793); NAA16–NAA20 (0.83)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a new cross-tissue co-abundance pattern, but the available evidence is insufficient to call it a new biological mechanism. Reasons supporting possible novelty are the absence of a globally significant GO or KEGG term, the absence of STRING functional enrichment, the lack of a multi-member hu.MAP complex, and the fact that most module links are not represented among the reported high-confidence STRING interactions. Reasons for caution are that CENPE–CLASP1 and NAA16–NAA20 are already known relationships, and the individual genes have established functions. Absence from STRING or hu.MAP cannot prove novelty; the appropriate claim is a potentially novel cross-tissue co-abundance configuration built from largely known cellular components.

**Hypothesis.** Hypothesis: the shared module reflects a conserved intracellular cell-state program that couples entry into or progression through proliferation with microtubule and centrosome remodeling, ubiquitin-mediated cell-cycle turnover, and production or stabilization of newly synthesized proteins. PTS could add a tetrahydrobiopterin-dependent metabolic or redox component, while MSTO1 and Golgi-associated genes could support organelle and trafficking demands. In autonomic nervous system and colon, this program might arise in different cell populations that share proliferative, regenerative or structural requirements rather than from a common tissue-specific pathway. This is a testable hypothesis, not an enrichment result: it would require replication with cell-resolved data and perturbation or protein-level validation.

### Important genes

#### CDC7

- **Related proteins** (co-abundance neighbors): UXT (0.88), MOCS2 (0.84), PTS (0.84), LARP4 (0.82), BRAP (0.81), UBE2S (0.81), NAA16 (0.81), NAA20 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell division cycle 7. This gene encodes a cell division cycle protein with kinase activity that is critical for the G1/S transition. The yeast homolog is also essential for initiation of DNA replication as cell division occurs. Overexpression of this gene product may be associated with neoplastic transformation for some tumors. Multiple alternatively spliced transcript variants that encode the same protein have been de…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); pathological myopia (0.325); liver disorder (0.265); Cachexia (0.253); glaucoma (0.249)
- **Europe PMC papers**: 3619
- **Why important**: CDC7 has the strongest network centrality in the reported module and connects to several otherwise weakly connected genes. Its established function is a kinase required for the G1/S transition and DNA-replication initiation, with additional links to cell-cycle progression and break-induced repair. It has extensive literature and disease or cancer relevance. Its HPA annotation is testis-enhanced with nucleoplasmic localization and colon protein detection.
- **Conclusion**: Established evidence supports CDC7 as the main cell-cycle and replication anchor of the module. It is plausible that its central co-abundance position reflects a proliferative state, but the module data do not show that CDC7 physically regulates every neighboring gene.

#### CENPE

- **Related proteins** (co-abundance neighbors): BRAP (0.81); STRING partners: CLASP1 (0.793)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Microtubules; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: centromere protein E. Centrosome-associated protein E (CENPE) is a kinesin-like motor protein that accumulates in the G2 phase of the cell cycle. Unlike other centrosome-associated proteins, it is not present during interphase and first appears at the centromere region of chromosomes during prometaphase. This protein is required for stable spindle microtubule capture at kinetochores which is a necessary step in chromos…
- **Diseases (Open Targets)**: Seckel syndrome (0.688); microcephalic primordial dwarfism (0.372); autosomal recessive primary microcephaly (0.371); Abnormality of the skeletal system (0.361); cervical carcinoma (0.354)
- **Europe PMC papers**: 2983
- **Why important**: CENPE is a mitotic kinesin-like motor required for stable spindle-microtubule capture at kinetochores, chromosome alignment and segregation. It has a strong mitotic annotation, substantial literature and disease associations involving developmental chromosome or cell-division defects. Its HPA profile is enhanced in bone marrow and lymphoid tissue and in progenitor populations, and it forms the module's reported high-confidence STRING relationship with CLASP1.
- **Conclusion**: Established evidence identifies CENPE as a compelling marker of mitotic and chromosome-segregation biology in the module. The co-abundance with CLASP1 supports a cytoskeletal interpretation, while the absence of broader known complex support limits claims about a complete mitotic machinery.

#### CLASP1

- **Related proteins** (co-abundance neighbors): CHURC1 (0.82); STRING partners: CENPE (0.793)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytoplasmic linker associated protein 1. CLASPs, such as CLASP1, are nonmotor microtubule-associated proteins that interact with CLIPs (e.g., CLIP170; MIM 179838). CLASP1 is involved in the regulation of microtubule dynamics at the kinetochore and throughout the spindle (Maiato et al., 2003 [PubMed 12837247]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: RNU4ATAC spectrum disorder (0.561); Roifman syndrome (0.560); microcephalic osteodysplastic primordial dwarfism type I (0.559); Lowry-Wood syndrome (0.551); neurodegenerative disease (0.521)
- **Europe PMC papers**: 738
- **Why important**: CLASP1 is a microtubule-associated protein that regulates microtubule dynamics, spindle organization, kinetochore-associated microtubules, microtubule nucleation and Golgi organization. It is directly linked to CENPE by the reported high-confidence STRING relationship and occupies a connection involving CHURC1 in the co-abundance graph. Its literature and disease annotations are substantial relative to several of the less characterized module genes.
- **Conclusion**: Established evidence supports CLASP1 as the clearest structural and microtubule component of the module, especially together with CENPE. It supports, but does not by itself prove, a coordinated mitotic or cytoskeletal program across both tissues.

#### PTS

- **Related proteins** (co-abundance neighbors): CDC7 (0.84), SCOC (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 6-pyruvoyltetrahydropterin synthase. The enzyme encoded by this gene catalyzes the elimination of inorganic triphosphate from dihydroneopterin triphosphate, which is the second and irreversible step in the biosynthesis of tetrahydrobiopterin from GTP. Tetrahydrobiopterin, also known as BH(4), is an essential cofactor and regulator of various enzyme activities, including enzymes involved in serotonin biosynthesis and NO synthase activ…
- **Diseases (Open Targets)**: BH4-deficient hyperphenylalaninemia A (0.857); hyperphenylalaninemia due to tetrahydrobiopterin deficiency (0.838); Intellectual disability (0.462); dystonic disorder (0.425); GTP cyclohydrolase I deficiency with hyperphenylalaninemia (0.420)
- **Europe PMC papers**: 27104
- **Why important**: PTS is an enzyme in tetrahydrobiopterin biosynthesis, producing a cofactor required for serotonin biosynthesis and nitric-oxide synthase activity. It is connected to CDC7 and SCOC in the module and has extensive literature plus strong disease associations with tetrahydrobiopterin-deficient hyperphenylalaninemia and neurological disorders. Its inclusion gives the module a potentially important metabolic and nervous-system-relevant component despite the lack of global pathway enrichment.
- **Conclusion**: Established evidence supports PTS as a bona fide metabolic enzyme with neural and vascular-relevant cofactor functions. Its relationship to the module's cell-cycle and microtubule genes is currently a hypothesis based on co-abundance, not an established shared pathway.

#### NAA16

- **Related proteins** (co-abundance neighbors): CDC7 (0.81); STRING partners: NAA20 (0.83)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-alpha-acetyltransferase 16, NatA auxiliary subunit. Enables ribosome binding activity. Involved in N-terminal protein amino acid acetylation; negative regulation of apoptotic process; and protein stabilization. Located in cytosol. Part of NatA complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: smoking cessation (0.290); hypertensive disorder (0.242); gallbladder disorder (0.238); essential hypertension (0.238); COVID-19 (0.236)
- **Europe PMC papers**: 127
- **Why important**: NAA16 is an auxiliary subunit of the NatA N-terminal acetyltransferase complex and contributes to protein maturation, stabilization and ribosome-associated activity. It is connected to CDC7 in the module and has a reported high-confidence STRING relationship with NAA20, providing the strongest evidence for a protein-modification submodule. Its HPA profile is enhanced in bone marrow and pancreas, with colon protein detection.
- **Conclusion**: Established evidence supports NAA16 as a protein-maturation and translational-quality-control component. The module may couple cell-cycle demand to protein processing, but this coupling remains an inference rather than a demonstrated mechanism.

#### NAA20

- **Related proteins** (co-abundance neighbors): CDC7 (0.80); STRING partners: NAA16 (0.83)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-alpha-acetyltransferase 20, NatB catalytic subunit. NAT5 is a component of N-acetyltransferase complex B (NatB). Human NatB performs cotranslational N(alpha)-terminal acetylation of methionine residues when they are followed by asparagine (Starheim et al., 2008 [PubMed 18570629]).[supplied by OMIM, Apr 2009].
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal recessive 73 (0.520); neurodegenerative disease (0.380); autosomal recessive non-syndromic intellectual disability (0.370); liver disorder (0.190); syndromic intellectual disability (0.185)
- **Europe PMC papers**: 236
- **Why important**: NAA20 is the catalytic subunit of the NatB complex and performs co-translational N-terminal acetylation. It is connected to CDC7 in the co-abundance graph and to NAA16 by the reported high-confidence STRING relationship, making it important for interpreting the module's protein acetylation signal. It has established links to intellectual-developmental and neurodegenerative disease and a growing literature base.
- **Conclusion**: Established evidence supports NAA20 as the catalytic counterpart to NAA16 and as evidence for a protein-maturation component within the module. The NAA16–NAA20 relationship is known, but whether their co-abundance is functionally coupled to CDC7 or the microtubule genes is unresolved.

## Module 10

**Tissue pair**: autonomic_nervous_system and colon  
**Genes (15)**: BYSL, CXXC1, DDX24, DDX42, MAP2, NOM1, NUP107, NUP88, RBM15, RSF1, SMARCA4, PPAN, TP53BP1, XRN2, ZMYM4

### Function

The module most plausibly represents a nuclear gene-expression and RNA-processing program, with linked components of ribosome biogenesis, RNA maturation, chromatin regulation, DNA-damage responses, and nucleocytoplasmic transport. PPAN, BYSL, NOM1 and DDX24 support a nucleolar and ribosome/RNA-processing interpretation; SMARCA4, RSF1, ZMYM4 and CXXC1 support chromatin and transcriptional regulation; and NUP107 with NUP88 supports nuclear-pore transport. MAP2 introduces a neuronal cytoskeletal component, which may reflect the autonomic nervous system context or a shared neuronal cell population. No GO/KEGG term passed global correction, so this functional interpretation is based on the convergence of individual gene annotations, network structure, STRING evidence and hu.MAP evidence rather than on globally significant enrichment.

**Cell composition.** The module is not dominated by secreted proteins, and the HPA evidence does not support a plasma-protein signature. Most genes have low tissue specificity and low immune-cell specificity, arguing against a blood-cell or broadly immune-driven explanation. Protein detection in colon is widespread across the module, whereas there is no matching HPA tissue for the autonomic nervous system. Several genes show cell-type enhancement in neuronal populations, including MAP2 and DDX24, while RBM15 is tissue enhanced in bone marrow and DDX24 is immune-cell enhanced in basophils. The composition therefore appears primarily intracellular and broadly expressed, with possible contributions from neuronal or other shared cell types rather than from circulating blood or secretion.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING network contains a limited set of high-confidence relationships. BYSL is linked to NOM1 and PPAN, DDX24 is linked to PPAN, and NUP107 is very strongly linked to NUP88. STRING supplementary compartment evidence places many module genes in the nuclear lumen (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.02), consistent with the nuclear and nucleolar interpretation, but this is supplementary evidence and is not a globally corrected GO/KEGG result. hu.MAP independently places ZMYM4 with RSF1 in a chromatin-associated complex (hu.MAP huMAP3_11539.1) and NUP107 with NUP88 in a nuclear-pore complex (hu.MAP huMAP3_12581.1). These known relationships show that parts of the module recapitulate established molecular assemblies. The remaining co-abundance links are not necessarily direct physical interactions and may reflect shared regulation, cell composition or coordinated cellular state.

**STRING interactions (score >= 0.7)**: 4 of 105 gene pairs: BYSL–NOM1 (0.748); BYSL–PPAN (0.819); DDX24–PPAN (0.719); NUP107–NUP88 (0.994)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Nuclear lumen (FDR = 0.02, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11539.1 (ZMYM4, RSF1; 2/32); huMAP3_12581.1 (NUP107, NUP88; 2/58)

### Novelty

This should not be called a wholly new molecular complex or a definitively novel biological pathway. Several internal relationships are already supported by STRING or hu.MAP, especially the BYSL–PPAN and BYSL–NOM1 relationships, the NUP107–NUP88 relationship, and the chromatin and nuclear-pore complex memberships (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.02) (hu.MAP huMAP3_11539.1) (hu.MAP huMAP3_12581.1). The potentially novel observation is the conserved co-abundance combination across autonomic nervous system and colon, particularly the connection of nucleolar, chromatin, nuclear-pore and neuronal-cytoskeletal genes in one module. That claim remains a candidate finding because absence from interaction databases does not establish novelty, and the module may reflect shared cell types or coordinated expression rather than a previously unknown physical complex. Independent replication, cell-resolved analysis and comparison with published co-expression modules would be needed to support a novelty claim.

**Hypothesis.** Hypothesis: the module reflects a conserved intracellular state in which RNA production and processing, ribosome assembly, chromatin accessibility, DNA-damage surveillance and nuclear transport are coordinated, with MAP2 marking a neuronal or neuron-associated component in the autonomic nervous system and possibly a shared cell population or structural program in colon. PPAN may organize the co-abundance pattern around RNA and ribosome-related processes, while the NUP107–NUP88 pair provides a nuclear-transport arm and the SMARCA4–RSF1–ZMYM4–CXXC1 group provides a chromatin-regulatory arm. This hypothesis predicts coordinated changes in RNA-processing, nucleolar, chromatin and nuclear-pore activity, but it does not establish direct physical cooperation among all module members.

### Important genes

#### PPAN

- **Related proteins** (co-abundance neighbors): ZMYM4 (0.86), RSF1 (0.83), MAP2 (0.82), NOM1 (0.81), SMARCA4 (0.81), BYSL (0.80); STRING partners: BYSL (0.819), DDX24 (0.719)
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peter pan homolog. The protein encoded by this gene is an evolutionarily conserved protein similar to yeast SSF1 as well as to the gene product of the Drosophila gene peter pan (ppan). SSF1 is known to be involved in the second step of mRNA splicing. Both SSF1 and ppan are essential for cell growth and proliferation. Exogenous expression of this gene was reported to reduce the anchorage-independent growth of some tu…
- **Diseases (Open Targets)**: Parkinson disease (0.462); Alzheimer disease (0.462); neurodegenerative disease (0.462); lysosomal storage disease (0.462); narcolepsy-cataplexy syndrome (0.435)
- **Europe PMC papers**: 417
- **Why important**: PPAN is the most connected gene in the module and links ZMYM4, RSF1, MAP2, NOM1, SMARCA4 and BYSL. Its annotation connects conserved cell growth and proliferation functions with rRNA processing and maturation of the large ribosomal subunit. It also has established STRING links to BYSL and DDX24, while its disease associations include neurodegenerative and lysosomal-storage disease categories. Its relatively substantial literature provides more context than for several less studied module members.
- **Conclusion**: Established evidence supports PPAN as a central co-abundance hub connecting ribosome-related, chromatin-related and neuronal components. The stronger claim that PPAN mechanistically coordinates the whole module is a hypothesis, not demonstrated by the supplied data.

#### MAP2

- **Related proteins** (co-abundance neighbors): PPAN (0.82), ZMYM4 (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: microtubule associated protein 2. This gene encodes a protein that belongs to the microtubule-associated protein family. The proteins of this family are thought to be involved in microtubule assembly, which is an essential step in neurogenesis. The products of similar genes in rat and mouse are neuron-specific cytoskeletal proteins that are enriched in dentrites, implicating a role in determining and stabilizing dentritic shape du…
- **Diseases (Open Targets)**: functional laterality (0.468); handedness (0.400); risk-taking behaviour (0.368); placenta praevia (0.345); septic shock (0.337)
- **Europe PMC papers**: 21514
- **Why important**: MAP2 is group enriched in brain and retina and is enhanced in several neuronal cell types. Its established function in microtubule organization, dendrite development and neuronal morphogenesis provides the clearest neuronal signal in the module. It connects to PPAN and ZMYM4, placing the neuronal cytoskeletal component near the module hub. MAP2 also has a very large literature base and disease or trait associations involving brain-related phenotypes.
- **Conclusion**: Established evidence supports MAP2 as a neuronal cytoskeletal marker and a plausible indicator of neuronal contribution to the shared module. Whether MAP2 participates in the same regulatory process as the nuclear and nucleolar genes remains unresolved and could instead reflect cell-type composition.

#### SMARCA4

- **Related proteins** (co-abundance neighbors): DDX24 (0.81), PPAN (0.81), XRN2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center, Nucleoli rim; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SWI/SNF related BAF chromatin remodeling complex subunit ATPase 4. The protein encoded by this gene is a member of the SWI/SNF family of proteins and is similar to the brahma protein of Drosophila. Members of this family have helicase and ATPase activities and are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI, wh…
- **Diseases (Open Targets)**: intellectual disability, autosomal dominant 16 (0.796); rhabdoid tumor predisposition syndrome 2 (0.788); familial rhabdoid tumor (0.685); rhabdoid tumor (0.627); medulloblastoma (0.586)
- **Europe PMC papers**: 9906
- **Why important**: SMARCA4 is a core ATPase of the SWI/SNF chromatin-remodeling system and is annotated in transcriptional regulation, chromatin remodeling and neural retina development. It links DDX24, PPAN and XRN2 in the module and is supported by a substantial literature base. Its disease associations include dominant intellectual disability and rhabdoid tumor predisposition, emphasizing the biological importance of altered chromatin regulation.
- **Conclusion**: Established evidence supports SMARCA4 as a major chromatin and transcriptional-regulatory component. Its connection to the RNA-processing genes is compatible with coordinated gene-expression control, but a direct SMARCA4-driven mechanism for this module is a hypothesis.

#### NUP107

- **Related proteins** (co-abundance neighbors): XRN2 (0.83), DDX42 (0.83); STRING partners: NUP88 (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 107. This gene encodes a member of the nucleoporin family. The protein is localized to the nuclear rim and is an essential component of the nuclear pore complex (NPC). All molecules entering or leaving the nucleus either diffuse through or are actively transported by the NPC. Alternate transcriptional splice variants of this gene have been observed but have not been thoroughly characterized. [provided …
- **Diseases (Open Targets)**: Galloway-Mowat syndrome (0.665); nephrotic syndrome, type 11 (0.622); 46 XX gonadal dysgenesis (0.577); familial idiopathic steroid-resistant nephrotic syndrome (0.554); HIV infectious disease (0.541)
- **Europe PMC papers**: 1487
- **Why important**: NUP107 is a nuclear-pore component involved in nucleocytoplasmic transport, nuclear-pore assembly and mRNA export. It connects XRN2 and DDX42 in the co-abundance network and has a strong STRING relationship with NUP88, with both genes appearing together in the hu.MAP nuclear-pore complex (hu.MAP huMAP3_12581.1). Its disease associations include Galloway-Mowat syndrome, nephrotic syndrome and gonadal dysgenesis, and it has a substantial literature base.
- **Conclusion**: Established evidence supports NUP107 as the principal nuclear-pore representative of the module and validates a transport-related substructure through NUP88 (hu.MAP huMAP3_12581.1). Its role as a bridge between RNA processing and the rest of the module is mechanistically plausible but not proven.

#### RSF1

- **Related proteins** (co-abundance neighbors): PPAN (0.83), RBM15 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_11539.1
- **Function (MyGene.info)**: remodeling and spacing factor 1. This gene encodes a nuclear protein that interacts with hepatitis B virus X protein (HBX) and facilitates transcription of hepatitis B virus genes by the HBX transcription activator, suggesting a role for this interaction in the virus life cycle. This protein also interacts with SNF2H protein to form the RSF chromatin-remodeling complex, where the SNF2H subunit functions as the nucleosome-dependen…
- **Diseases (Open Targets)**: myopathy (0.313); neurodevelopmental disorder (0.187); infection (0.172); handedness (0.156); neoplasm (0.101)
- **Europe PMC papers**: 783
- **Why important**: RSF1 is a nuclear chromatin-remodeling and histone-chaperone component that connects PPAN and RBM15. It is colocated with ZMYM4 in a hu.MAP chromatin-associated complex (hu.MAP huMAP3_11539.1) and is included in the supplementary nuclear-lumen signal (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.02). Its annotations cover chromatin organization, nucleosome assembly, transcription initiation and heterochromatin formation, while its disease associations include myopathy and neurodevelopmental disorder.
- **Conclusion**: Established evidence supports RSF1 as a chromatin-regulatory member that independently reinforces the nuclear interpretation. Its connection to PPAN and RBM15 may indicate coordinated regulation of chromatin and RNA metabolism, but this integrated role remains a hypothesis.

## Module 11

**Tissue pair**: autonomic_nervous_system and colon  
**Genes (20)**: CCNH, DIAPH1, DNAJC2, FRAS1, GAK, GPRIN1, HARS1, CAMK4, KIF15, KIF22, KIF5C, LNPK, PLCH1, PRPF39, PSME4, VIPAS39, TBCEL, TRAPPC5, UBR1, VPS41

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent. Therefore, the module does not support a statistically established single pathway-level function. Its gene content nevertheless points to a composite intracellular program involving neuronal and neuroendocrine signaling, microtubule-dependent transport, vesicle and endolysosomal trafficking, cytoskeletal organization, transcriptional or RNA-related processes, and protein quality control. CAMK4 is the principal network hub and connects signaling, cytoskeletal, trafficking, translation, and protein-degradation-related genes. KIF5C, GPRIN1, TBCEL, and several trafficking genes provide a coherent neuronal or neurite-associated aspect, whereas KIF15, KIF22, and cell-cycle-related annotations indicate a separate microtubule and chromosome-associated aspect. These observations are biological interpretation rather than globally significant enrichment.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module: only a single member is annotated in the secretome, and most proteins are intracellular, nuclear, cytosolic, vesicular, membrane, or endoplasmic-reticulum associated. The module is not strongly blood-cell specific. Most genes have low immune-cell specificity or are not detected in immune cells, although a small subset has immune, lymphoid, platelet, or progenitor-related annotations. HPA instead shows recurring associations with brain neurons, retina, lymphoid tissue, testis, and spermatogenic cell types, with many genes having enhanced rather than ubiquitous cell-type patterns. Protein detection in colon is widespread among the members, while direct autonomic-nervous-system protein evidence is unavailable in the supplied HPA summary. Thus, the shared signal is more consistent with a mixture of broadly expressed intracellular proteins and tissue or cell-type contributions than with a plasma-protein signature. Shared neural, epithelial, stromal, or other cell-composition effects remain possible and cannot be resolved from co-abundance alone.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING evidence is very limited: the only high-confidence reported relationship within the module is the KIF15-KIF22 pair. No other module-member relationships were reported at the supplied STRING threshold, and no STRING functional-enrichment result was present. No hu.MAP complex contained at least two module members. The KIF15-KIF22 relationship supports a real connection between two microtubule or mitotic proteins, but it does not establish the entire module as one physical complex. The remaining co-abundance edges may reflect co-expression, shared cell composition, indirect regulation, condition-specific biology, or incomplete interaction-database coverage. The apparent hub role of CAMK4 is a property of this co-abundance graph, not evidence that CAMK4 physically binds all of its neighbors.

**STRING interactions (score >= 0.7)**: 1 of 190 gene pairs: KIF15–KIF22 (0.718)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module can be considered a potentially interesting co-abundance observation, but it cannot be called a newly discovered biological complex or pathway. Its novelty is supported only in the limited sense that this particular cross-tissue co-abundance configuration is not represented by a corresponding hu.MAP multi-member complex and has very little high-confidence STRING support. That database absence does not prove novelty: the module combines well-established proteins and functions, includes broadly expressed genes, and may arise from shared cell types, tissue composition, or correlated technical or biological regulation. The lack of globally significant GO or KEGG enrichment further argues against claiming a previously unrecognized canonical pathway. A genuine new finding would require independent replication, cell-type-aware analysis, perturbation or mechanistic experiments, and validation of the cross-tissue association.

**Hypothesis.** Hypothesis: the module represents a context-dependent intracellular coordination program in which CAMK4-linked signaling is coupled to neuronal or neurite-associated cytoskeletal organization and microtubule-based cargo transport, with contributions from vesicle trafficking, endolysosomal sorting, endoplasmic-reticulum organization, and protein quality control. In colon, the signal may reflect neural, epithelial, stromal, or other shared cellular components rather than a colon-specific pathway. The KIF15-KIF22 relationship may mark a microtubule or chromosome-associated subcomponent, while the CAMK4-centered edges may represent correlated regulation rather than direct physical interactions. This hypothesis predicts that cell-type-resolved measurements and perturbation of CAMK4-associated signaling or microtubule and trafficking processes should separate the proposed biological program from a cell-composition or technical co-abundance effect.

### Important genes

#### CAMK4

- **Related proteins** (co-abundance neighbors): CCNH (0.90), PLCH1 (0.89), DIAPH1 (0.88), HARS1 (0.86), LNPK (0.85), TRAPPC5 (0.83), TBCEL (0.81), PSME4 (0.81), KIF5C (0.80), UBR1 (0.80), GAK (0.80), KIF22 (0.80), GPRIN1 (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium/calmodulin dependent protein kinase IV. The product of this gene belongs to the serine/threonine protein kinase family, and to the Ca(2+)/calmodulin-dependent protein kinase subfamily. This enzyme is a multifunctional serine/threonine protein kinase with limited tissue distribution, that has been implicated in transcriptional regulation in lymphocytes, neurons and male germ cells. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: Intellectual disability (0.528); hypothyroidism (0.497); autism (0.467); dystonic disorder (0.463); cerebellar ataxia (0.463)
- **Europe PMC papers**: 1893
- **Why important**: CAMK4 has the strongest hub position in the module and connects many otherwise weakly connected members. Its established function is a calcium and calmodulin-dependent serine/threonine kinase implicated in transcriptional regulation, lymphocytes, neurons, and male germ cells. Its HPA profile links it to brain and lymphoid tissue and to neuronal and adrenal-medulla cell types. Its disease associations include neurodevelopmental and neurological conditions, and it has a large literature base. It is therefore the best candidate for a regulatory anchor, although the co-abundance graph does not prove direct control of its neighbors.
- **Conclusion**: Established evidence: CAMK4 is a multifunctional kinase with neural and lymphoid relevance and is the central connector in this module. Hypothesis: CAMK4-related signaling may coordinate the module's trafficking and cytoskeletal components. This regulatory interpretation requires perturbation and cell-type-resolved validation.

#### KIF5C

- **Related proteins** (co-abundance neighbors): CCNH (0.88), GPRIN1 (0.87), DNAJC2 (0.84), VIPAS39 (0.82), FRAS1 (0.81), CAMK4 (0.80), VPS41 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Cytosol, Equatorial segment, Connecting piece; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 5C. The protein encoded by this gene is a kinesin heavy chain subunit involved in the transport of cargo within the central nervous system. The encoded protein, which acts as a tetramer by associating with another heavy chain and two light chains, interacts with protein kinase CK2. Mutations in this gene have been associated with complex cortical dysplasia with other brain malformations-2. Two transcr…
- **Diseases (Open Targets)**: Genetic central nervous system malformation (0.754); neurodegenerative disease (0.435); complex cortical dysplasia with other brain malformations (0.370); cerebral cortical dysplasia (0.271); disturbances of sensation of smell and taste (0.262)
- **Europe PMC papers**: 1225
- **Why important**: KIF5C is a highly connected member and is linked to CAMK4, GPRIN1, DNAJC2, VIPAS39, FRAS1, and VPS41 in the co-abundance graph. It is an established kinesin heavy-chain subunit involved in central-nervous-system cargo transport, microtubule movement, axon guidance, and synaptic vesicle transport. HPA shows tissue enrichment in brain and enhancement in several neuronal cell types, while its disease associations include cortical malformation and other neurological conditions. Its literature base is substantial.
- **Conclusion**: Established evidence: KIF5C supports a neuronal microtubule and intracellular-transport interpretation. Hypothesis: it may connect CAMK4-associated signaling to vesicle and organelle movement in the shared module. The cross-tissue role remains unproven.

#### GPRIN1

- **Related proteins** (co-abundance neighbors): KIF5C (0.87), TBCEL (0.85), CCNH (0.83), CAMK4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein regulated inducer of neurite outgrowth 1. Predicted to enable phosphoprotein binding activity. Predicted to be involved in neuron projection development. Predicted to be located in growth cone. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: gastric cancer (0.077); lung adenocarcinoma (0.074); non-small cell lung carcinoma (0.057); hemochromatosis type 5 (0.038); neoplasm (0.034)
- **Europe PMC papers**: 409
- **Why important**: GPRIN1 is connected to CAMK4 and KIF5C and is specifically associated with brain, pituitary gland, retina, and multiple neuronal cell types in HPA. Its annotated function concerns neurite outgrowth, neuron projection development, phosphoprotein binding, and the growth cone. Although its literature volume and disease evidence are more limited than those of CAMK4 or KIF5C, its position at the intersection of the neural signaling and transport portion of the graph makes it informative.
- **Conclusion**: Established evidence: GPRIN1 is a neuron-associated neurite-development protein with a neural HPA pattern and links to the module's signaling and transport genes. Hypothesis: it may mark a neuronal or neurite-related subcomponent of the shared co-abundance signal rather than a general colon mechanism.

#### PLCH1

- **Related proteins** (co-abundance neighbors): CAMK4 (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phospholipase C eta 1. PLCH1 is a member of the PLC-eta family of the phosphoinositide-specific phospholipase C (PLC) superfamily of enzymes that cleave phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2) to generate second messengers inositol 1,4,5-trisphosphate (IP3) and diacylglycerol (DAG) (Hwang et al., 2005 [PubMed 15702972]).[supplied by OMIM, Jun 2009].
- **Diseases (Open Targets)**: holoprosencephaly 14 (0.577); alobar holoprosencephaly (0.370); neurodegenerative disease (0.369); insomnia (0.364); adolescent idiopathic scoliosis (0.313)
- **Europe PMC papers**: 367
- **Why important**: PLCH1 is directly connected to CAMK4 and supplies a plausible second-messenger signaling link. Its established enzymatic activity cleaves phosphatidylinositol bisphosphate to generate IP3 and DAG, supporting intracellular calcium and phosphoinositide signaling. HPA associates it with lymphoid tissue, retina, and testis and with several ciliated, glial, epithelial, and germ-cell types. Its disease associations include developmental and neurological conditions.
- **Conclusion**: Established evidence: PLCH1 can transmit phosphoinositide and calcium-related signals and is linked to CAMK4 in the module. Hypothesis: PLCH1 may provide an upstream or parallel signaling input that helps explain CAMK4-centered co-abundance. Direct pathway coupling within this module has not been demonstrated.

#### FRAS1

- **Related proteins** (co-abundance neighbors): PRPF39 (0.88), KIF5C (0.81), KIF15 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Fraser extracellular matrix complex subunit 1. This gene encodes an extracellular matrix protein that appears to function in the regulation of epidermal-basement membrane adhesion and organogenesis during development. Mutations in this gene cause Fraser syndrome, a multisystem malformation that can include craniofacial, urogenital and respiratory system abnormalities. Alternative splicing results in multiple transcript variants. [provided by R…
- **Diseases (Open Targets)**: Fraser syndrome (0.809); renal agenesis (0.564); congenital anomaly of kidney and urinary tract (0.472); hereditary disease (0.417); renal agenesis, unilateral (0.370)
- **Europe PMC papers**: 1305
- **Why important**: FRAS1 links the graph's structural and transport components, connecting PRPF39, KIF5C, and KIF15. It is an extracellular-matrix-associated protein involved in cell-matrix adhesion and epithelial structure maintenance, with HPA enhancement in thyroid tissue and several epithelial, mesothelial, and developmental cell types. Its established disease association with Fraser syndrome and congenital renal and multisystem abnormalities supports a role in tissue organization. It is also one of the few members with an explicitly membrane or extracellular structural aspect, despite the module being predominantly intracellular.
- **Conclusion**: Established evidence: FRAS1 contributes to extracellular-matrix adhesion and epithelial organization and bridges structural and microtubule-associated members in the graph. Hypothesis: it may reflect shared epithelial or tissue-architecture composition in colon rather than a direct mechanistic component of a neural signaling pathway.

#### KIF15

- **Related proteins** (co-abundance neighbors): FRAS1 (0.80); STRING partners: KIF22 (0.718)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 15. Predicted to enable microtubule binding activity and microtubule motor activity. Predicted to be involved in microtubule-based movement. Located in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: braddock-carey syndrome 2 (0.503); 21q22.11q22.12 microdeletion syndrome (0.370); interstitial lung disease (0.210); pulmonary fibrosis (0.176); nasopharyngeal carcinoma (0.104)
- **Europe PMC papers**: 1270
- **Why important**: KIF15 is important because it is the module member participating in the only reported high-confidence STRING relationship, the KIF15-KIF22 pair. Its established functions include microtubule motor activity, mitotic spindle assembly, centrosome separation, and chromosome-related cell-cycle processes. HPA associates it with bone marrow, lymphoid tissue, testis, and spermatogenic or progenitor cell types. Its disease associations include developmental and pulmonary conditions. The external interaction evidence gives this part of the module more support than an edge based solely on co-abundance.
- **Conclusion**: Established evidence: KIF15 is a microtubule motor and has a reported STRING relationship with KIF22. Hypothesis: the pair may represent a proliferative, germ-cell, or progenitor-associated submodule embedded within the broader co-abundance pattern. It does not establish a unified module mechanism.
