# Conserved co-abundance modules: cervix_uterine and rectum

## Module 0

**Tissue pair**: cervix_uterine and rectum  
**Genes (39)**: BZW2, ACSL4, AIFM1, ALDH2, ATP5F1B, MTHFD1, CPSF3, DNAAF5, DDX5, DDX6, HSD17B4, HADHB, GFM1, EIF3F, ERO1A, HMGCS1, HNRNPH1, HNRNPL, LACTB, LAS1L, MRE11, NOP56, NRDC, PDLIM1, PLIN3, PNPT1, PRPF31, RBM26, RCC1, RPRD1B, PDCD11, SUPT16H, TIMM44, TIMM50, TMEM33, TOMM40, UMPS, XPO1, ZFR

### Function

The strongest primary interpretation is a broadly expressed mitochondrial and RNA–protein homeostasis module, with a particularly coherent mitochondrial-import core. The only GO/KEGG term surviving global correction is (GO:BP protein import into mitochondrial matrix; q_global = 0.0411), protein import into the mitochondrial matrix, represented by TIMM44, TIMM50, and TOMM40. This is biologically supported by the direct STRING links among TIMM44, TIMM50, and TOMM40, and by the presence of mitochondrial translation, mitochondrial RNA processing, oxidative metabolism, fatty-acid oxidation, and ATP-production genes elsewhere in the module. A secondary layer comprises RNA processing, ribosome biogenesis, RNA export, transcription, and cell-cycle or genome-maintenance functions, but these are functional interpretations from individual annotations and network structure rather than globally significant enrichment. The module therefore appears to capture coordinated cellular infrastructure, especially mitochondrial import and maintenance coupled to gene-expression and metabolic capacity.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: the HPA summary identifies only one secreted gene, while protein detection is broadly observed in both cervix_uterine and rectum. It is also not strongly blood-cell enriched: most genes have low immune-cell specificity, with only limited immune-cell-enhanced or group-enriched observations. Most genes have low tissue specificity, although subsets are enhanced in liver, skeletal muscle, tongue, heart muscle, or esophagus and several are enhanced in specialized cell types such as enterocytes, hepatocytes, neutrophils, trophoblasts, or spermatogenic cells. This pattern favors a broadly expressed intracellular program rather than a plasma-protein or blood-contamination explanation. Shared epithelial, metabolic, or other resident-cell composition could still contribute to the co-abundance signal, particularly because HPA shows cell-type enhancement for subsets of the genes.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP protein import into mitochondrial matrix | 0.0411 | TIMM44, TIMM50, TOMM40 |

### STRING and hu.MAP

STRING supports a structured mitochondrial-import component: TIMM44–TIMM50 and TIMM44–TOMM40 are very strong known relationships, with TIMM50–TOMM40 also supported, and ATP5F1B connects to TIMM50 and TOMM40. STRING also supports several other established relationships, including DDX5 with HNRNPH1, HNRNPH1 with HNRNPL, NOP56 with PDCD11, GFM1 with PNPT1, HADHB with HMGCS1 and HSD17B4, and RCC1 with XPO1. These links indicate that part of the module recapitulates known mitochondrial, RNA-processing, nucleolar, and lipid-metabolic biology rather than being an entirely undocumented interaction system. hu.MAP provides additional complex-level support: HNRNPL and ZFR occur together in RNA-binding complexes (hu.MAP huMAP3_07581.1) and (hu.MAP huMAP3_10625.1); PNPT1 and GFM1 occur together in a mitochondrial complex (hu.MAP huMAP3_13468.1); XPO1 and UMPS recur in complexes (hu.MAP huMAP3_07170.1) and (hu.MAP huMAP3_09042.1); ACSL4 and TMEM33 recur in membrane or lipid-associated complexes (hu.MAP huMAP3_09592.1) and (hu.MAP huMAP3_06247.1); XPO1 and ACSL4 occur together in (hu.MAP huMAP3_09592.1) and (hu.MAP huMAP3_06791.1); and PDLIM1 with HMGCS1 occurs in (hu.MAP huMAP3_14442.1). However, most hu.MAP complexes contain only a small subset of the module, so the module is better viewed as a co-abundance assembly of several connected cellular subsystems than as a single established physical complex.

**STRING interactions (score >= 0.7)**: 15 of 741 gene pairs: ATP5F1B–TIMM50 (0.73); ATP5F1B–TOMM40 (0.727); DDX5–HNRNPH1 (0.96); GFM1–PDCD11 (0.815); GFM1–PNPT1 (0.842); HADHB–HMGCS1 (0.993); HADHB–HSD17B4 (0.93); HNRNPH1–HNRNPL (0.982); LAS1L–PRPF31 (0.902); NOP56–PDCD11 (0.997); PDCD11–PNPT1 (0.745); RCC1–XPO1 (0.927); TIMM44–TIMM50 (0.985); TIMM44–TOMM40 (0.958); TIMM50–TOMM40 (0.971)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09592.1 (XPO1, ACSL4, TMEM33; 3/95); huMAP3_07170.1 (XPO1, UMPS; 2/14); huMAP3_07581.1 (HNRNPL, ZFR; 2/21); huMAP3_09042.1 (XPO1, UMPS; 2/26); huMAP3_06791.1 (XPO1, ACSL4; 2/31); huMAP3_14442.1 (PDLIM1, HMGCS1; 2/57); huMAP3_10625.1 (HNRNPL, ZFR; 2/57); huMAP3_06247.1 (ACSL4, TMEM33; 2/65); huMAP3_13468.1 (PNPT1, GFM1; 2/99)

### Novelty

This is not established as a wholly new molecular complex or a newly discovered pathway. The mitochondrial-import core and several RNA-processing, nucleolar, lipid-metabolic, and mitochondrial-translation relationships are already represented in STRING or hu.MAP, and the individual gene functions are well established. The potentially novel result is the conserved co-abundance pattern across cervix_uterine and rectum, especially the way mitochondrial import, RNA handling, lipid metabolism, and cellular infrastructure appear together in these tissues. That pattern should be described as a tissue-pair network observation rather than a new physical interaction or a newly proven mechanism. Absence of some module pairs from STRING or hu.MAP does not establish novelty, because those resources record different evidence types and are incomplete. The single globally corrected term (GO:BP protein import into mitochondrial matrix; q_global = 0.0411) gives focused statistical support but does not by itself prove that the entire module is a new biological entity.

**Hypothesis.** Hypothesis: in shared cervix_uterine and rectum cell populations, coordinated mitochondrial protein import may support mitochondrial translation, RNA surveillance, fatty-acid handling, and energy production, while nuclear and nucleolar RNA-processing factors maintain the gene-expression capacity needed for this metabolic state. The observed co-abundance could therefore reflect a common intracellular demand for mitochondrial maintenance and biosynthetic or epithelial-cell activity. ACSL4, HMGCS1, HADHB, and HSD17B4 suggest a lipid-metabolic interface, whereas DDX5, HNRNPL, NOP56, PDCD11, PNPT1, and GFM1 suggest RNA-processing and mitochondrial gene-expression interfaces. This remains a hypothesis: the co-abundance data do not establish directionality, physical binding among all module members, or causal regulation. Testing would require cell-type-resolved measurements, perturbation of the mitochondrial-import or lipid-metabolic components, and assessment of the predicted effects on mitochondrial function and RNA processing.

### Important genes

#### TIMM50

- **Related proteins** (co-abundance neighbors): DDX5 (0.91), HNRNPL (0.86), RCC1 (0.85), DDX6 (0.85), NOP56 (0.84), ACSL4 (0.83), LACTB (0.81), MRE11 (0.81), PDCD11 (0.81); STRING partners: ATP5F1B (0.73), TIMM44 (0.985), TOMM40 (0.971)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translocase of inner mitochondrial membrane 50. This gene encodes a subunit of the TIM23 inner mitochondrial membrane translocase complex. The encoded protein functions as the receptor subunit that recognizes the mitochondrial targeting signal, or presequence, on protein cargo that is destined for the mitochondrial inner membrane and matrix. This protein may also play a role in maintaining the membrane permeability barrier, and knockdown of thi…
- **Diseases (Open Targets)**: 3-methylglutaconic aciduria type 9 (0.773); neurodegenerative disease (0.519); Mitochondrial encephalopathy (0.425); hereditary disease (0.415); Epileptic encephalopathy (0.370)
- **Europe PMC papers**: 442
- **Why important**: TIMM50 is a high-connectivity module gene and is one of the three genes in the sole globally corrected term (GO:BP protein import into mitochondrial matrix; q_global = 0.0411). It is a receptor subunit of the TIM23 inner-membrane translocase and is linked in STRING to TIMM44 and TOMM40, while also connecting within the module to RNA, metabolic, and mitochondrial genes. Its HPA profile is broadly expressed and detected in both tissues, which fits a core cellular role rather than a tissue-restricted or secreted signal. Its disease associations include mitochondrial encephalopathy and related inherited disorders, and its literature volume is substantial enough to provide established mechanistic context.
- **Conclusion**: Established evidence supports TIMM50 as a central mitochondrial-import component and a strong anchor for interpreting the module. The hypothesis that it coordinates the module’s RNA and lipid-metabolic branches is plausible from network context but is not demonstrated by the fact sheet.

#### TOMM40

- **Related proteins** (co-abundance neighbors): HNRNPH1 (0.82), NOP56 (0.81); STRING partners: ATP5F1B (0.727), TIMM44 (0.958), TIMM50 (0.971)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translocase of outer mitochondrial membrane 40. The protein encoded by this gene is localized in the outer membrane of the mitochondria. It is the channel-forming subunit of the translocase of the mitochondrial outer membrane (TOM) complex that is essential for import of protein precursors into mitochondria. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Aug 2015].
- **Diseases (Open Targets)**: Alzheimer disease (0.325); dementia (0.269); metabolic syndrome (0.262); chronic kidney disease (0.224); Lewy body dementia (0.205)
- **Europe PMC papers**: 2387
- **Why important**: TOMM40 is part of (GO:BP protein import into mitochondrial matrix; q_global = 0.0411) and encodes the channel-forming component of the outer-mitochondrial-membrane import machinery. It has direct STRING relationships with TIMM44, TIMM50, and ATP5F1B, providing unusually clear support for a mitochondrial-import and energy-related subnetwork. It is detected in both tissues and has broad tissue specificity, arguing against a plasma or blood-cell explanation. Its disease associations include Alzheimer disease, dementia, metabolic syndrome, and kidney disease, and it has a substantial literature base.
- **Conclusion**: Established evidence makes TOMM40 a key structural anchor for the mitochondrial interpretation. Its co-abundance with nuclear RNA-processing and lipid genes may reflect shared cellular state or mitochondrial demand, but that cross-compartment coordination remains a hypothesis.

#### ACSL4

- **Related proteins** (co-abundance neighbors): HMGCS1 (0.88), GFM1 (0.84), TIMM50 (0.83), AIFM1 (0.83), PNPT1 (0.82), DDX5 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_09592.1, huMAP3_06791.1, huMAP3_06247.1
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 4. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme preferentially util…
- **Diseases (Open Targets)**: non-syndromic X-linked intellectual disability (0.734); neurodegenerative disease (0.545); Alport syndrome-intellectual disability-midface hypoplasia-elliptocytosis syndrome (0.509); Alzheimer disease (0.384); Parkinson disease (0.381)
- **Europe PMC papers**: 10097
- **Why important**: ACSL4 has meaningful connectivity to HMGCS1, GFM1, TIMM50, AIFM1, PNPT1, and DDX5, placing lipid handling near both mitochondrial and RNA-related portions of the network. It activates long-chain fatty acids and preferentially uses arachidonate, providing a plausible metabolic interface. It is represented in several hu.MAP complexes (hu.MAP huMAP3_09592.1), (hu.MAP huMAP3_06791.1), and (hu.MAP huMAP3_06247.1), although those complexes contain only a subset of module members. HPA shows cell-type enhancement in several epithelial and immune-associated cell types and protein detection in rectum, while disease associations include intellectual disability and neurodegenerative disease. Its literature volume is especially large.
- **Conclusion**: Established evidence supports ACSL4 as a lipid-metabolic connector within the module. A role in coupling lipid substrate handling to mitochondrial maintenance is a reasonable hypothesis, not a demonstrated causal function of this module.

#### HMGCS1

- **Related proteins** (co-abundance neighbors): MRE11 (0.88), ACSL4 (0.88), HADHB (0.88), PDLIM1 (0.87), ALDH2 (0.83), ERO1A (0.82), HNRNPH1 (0.82), ZFR (0.81); STRING partners: HADHB (0.993)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: 3-hydroxy-3-methylglutaryl-CoA synthase 1. Enables protein homodimerization activity. Predicted to be involved in acetyl-CoA metabolic process and farnesyl diphosphate biosynthetic process, mevalonate pathway. Predicted to be located in cytoplasm. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.556); rigid spine syndrome (0.500); mathematical ability (0.289); prostate carcinoma (0.232); Alzheimer disease (0.231)
- **Europe PMC papers**: 3616
- **Why important**: HMGCS1 is a highly connected metabolic gene linked to ACSL4, HADHB, PDLIM1, ALDH2, ERO1A, HNRNPH1, and ZFR. It is a key enzyme of the cytosolic mevalonate and cholesterol-biosynthetic pathway, and it occurs with PDLIM1 in hu.MAP complex (hu.MAP huMAP3_14442.1). HPA shows liver tissue enhancement and broad detection in both tissues, with low immune specificity. Its disease associations span neurodegenerative disease, rigid spine syndrome, and cancer-related indications, and it has a substantial literature volume.
- **Conclusion**: Established evidence supports HMGCS1 as a metabolic hub connecting lipid, mitochondrial, cytoskeletal, and RNA-associated module neighborhoods. The proposed metabolic coupling to mitochondrial import is consistent with the network but requires experimental validation.

#### DDX5

- **Related proteins** (co-abundance neighbors): TIMM50 (0.91), RCC1 (0.89), NOP56 (0.86), HNRNPL (0.85), DDX6 (0.85), HSD17B4 (0.84), SUPT16H (0.83), MRE11 (0.82), ACSL4 (0.80); STRING partners: HNRNPH1 (0.96)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 has among the strongest network centrality in the module and connects mitochondrial-import-associated TIMM50 with RCC1, NOP56, HNRNPL, DDX6, HSD17B4, SUPT16H, and MRE11. It is an RNA helicase involved in RNA structure alteration, transcriptional co-regulation, splicing, and small noncoding-RNA processing. STRING directly supports its relationship with HNRNPH1, while HPA shows low tissue and cell-type specificity and detection in both tissues. It has extensive literature and disease associations including colorectal and colon adenocarcinoma.
- **Conclusion**: Established evidence supports DDX5 as a central RNA-processing and transcriptional organizer within a broadly expressed intracellular module. Its position suggests it may help link gene-expression state to mitochondrial and metabolic programs, but the network does not establish that it regulates those branches here.

#### PNPT1

- **Related proteins** (co-abundance neighbors): RCC1 (0.85), GFM1 (0.82), ACSL4 (0.82), TIMM44 (0.81), DDX6 (0.81); STRING partners: GFM1 (0.842), PDCD11 (0.745)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: polyribonucleotide nucleotidyltransferase 1. The protein encoded by this gene belongs to the evolutionary conserved polynucleotide phosphorylase family comprised of phosphate dependent 3'-to-5' exoribonucleases implicated in RNA processing and degradation. This enzyme is predominantly localized in the mitochondrial intermembrane space and is involved in import of RNA to mitochondria. Mutations in this gene have been associated with combined …
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 13 (0.807); autosomal recessive nonsyndromic hearing loss 70 (0.740); spinocerebellar ataxia type 25 (0.709); deafness (0.676); hearing loss, autosomal recessive (0.634)
- **Europe PMC papers**: 839
- **Why important**: PNPT1 connects GFM1, RCC1, ACSL4, TIMM44, and DDX6, bridging mitochondrial RNA handling, mitochondrial import, metabolism, and cytoplasmic RNA turnover. It is a mitochondrial polynucleotide phosphorylase involved in RNA processing and degradation and is represented with GFM1 in hu.MAP complex (hu.MAP huMAP3_13468.1). STRING also supports its relationships with GFM1 and PDCD11. HPA shows low tissue and cell-type specificity with detection in both tissues. Its disease associations include combined oxidative phosphorylation deficiency, hearing loss, and spinocerebellar ataxia, supported by a substantive literature base.
- **Conclusion**: Established evidence supports PNPT1 as a biologically informative bridge between mitochondrial gene expression and the broader module. Its possible role in coordinating mitochondrial RNA quality control with import and lipid metabolism is a hypothesis derived from the network context.

## Module 1

**Tissue pair**: cervix_uterine and rectum  
**Genes (38)**: ACADVL, ACTL6A, ADGRE5, PRMT5, ATP1A1, CCAR1, CTNNA1, DNM1L, EDC4, EIF3L, GLS, GPD2, GRSF1, COLGALT1, GTPBP4, HSDL2, KRT18, KRT8, LMNB1, CHCHD3, IMMT, MISP, NSDHL, NUP155, NUP210, PRPF4, SEC23IP, SLC25A24, SFXN3, SMARCA4, SPTBN1, SRRT, DARS1, QARS1, THOP1, UGGT1, ZC3HAV1, ZW10

### Function

No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The gene composition and network instead suggest a broadly cellular maintenance program spanning nuclear transport, RNA processing and translation, mitochondrial architecture and metabolism, epithelial structure, membrane transport, and cell-cycle or chromatin regulation. The strongest network-position evidence comes from SRRT, NUP155, NUP210, DARS1, and PRPF4, which connect several of these processes. The module should therefore be interpreted as a coordinated cellular-state signature rather than a single demonstrated biochemical pathway. The presence of the KRT8-KRT18 pair, nuclear-pore genes, aminoacyl-tRNA synthetases, spliceosome-related genes, and mitochondrial genes is consistent with maintenance of epithelial cell integrity, gene-expression processing, protein synthesis, and organelle homeostasis. These functional interpretations are supported by the individual gene annotations, but not by globally significant enrichment.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the HPA summary identifies only a small secreted component, and most genes have low tissue specificity. Protein detection is broad in both cervix_uterine and rectum, supporting the interpretation that the module is present in resident tissue cells rather than being explained mainly by a circulating protein signal. The module is also not strongly blood-cell enriched overall, because most genes have low immune-cell specificity. Some components nevertheless show hematopoietic or immune-related patterns, including NUP210, LMNB1, ZC3HAV1, COLGALT1, GPD2, and ADGRE5, while several genes are enhanced in intestinal, esophageal, epithelial, or enterocyte-related cell types. Thus, shared epithelial or general cellular composition is more plausible as the principal explanation than a purely blood-derived signal, although contributions from stromal or hematopoietic cells cannot be excluded.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports several established relationships within the module. The KRT8-KRT18 pair is a known epithelial intermediate-filament relationship; NUP155-NUP210 supports a nuclear-pore connection; DARS1-QARS1 supports aminoacyl-tRNA synthetase organization; ACTL6A-SMARCA4 and PRMT5-SMARCA4 support chromatin-remodeling and transcriptional machinery; and CHCHD3-IMMT together with DNM1L supports mitochondrial cristae organization and mitochondrial dynamics. ACADVL-HSDL2 also links mitochondrial lipid or sterol-related functions. The remaining high-confidence module edges may represent functional association rather than direct physical binding. hu.MAP independently places NUP155 and NUP210 in a nuclear-pore complex (hu.MAP huMAP3_07645.1), CHCHD3 and SLC25A24 in a mitochondrial-associated complex (hu.MAP huMAP3_06505.1), DARS1 and QARS1 in aminoacyl-tRNA synthetase complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), ATP1A1 and LMNB1 in a larger cellular complex (hu.MAP huMAP3_10473.1), and PRMT5 with PRPF4 in spliceosome-related complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1). Because these complexes contain only subsets of the module members, the evidence supports several established molecular neighborhoods rather than one unified physical complex.

**STRING interactions (score >= 0.7)**: 11 of 703 gene pairs: ACADVL–HSDL2 (0.787); ACTL6A–PRMT5 (0.722); ACTL6A–SMARCA4 (0.999); CCAR1–SRRT (0.857); CHCHD3–DNM1L (0.736); CHCHD3–IMMT (0.999); DARS1–QARS1 (0.999); DNM1L–IMMT (0.798); KRT18–KRT8 (0.999); NUP155–NUP210 (0.991); PRMT5–SMARCA4 (0.977)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07645.1 (NUP155, NUP210; 2/7); huMAP3_06505.1 (SLC25A24, CHCHD3; 2/11); huMAP3_02637.1 (DARS1, QARS1; 2/14); huMAP3_13688.1 (DARS1, QARS1; 2/14); huMAP3_10473.1 (ATP1A1, LMNB1; 2/24); huMAP3_06511.1 (PRMT5, PRPF4; 2/79); huMAP3_08980.1 (PRMT5, PRPF4; 2/97)

### Novelty

The module may be a new tissue-pair co-abundance observation, but the biological relationships it contains are not themselves new. Several links and complexes are already represented in STRING or hu.MAP, including the nuclear-pore, keratin, mitochondrial, aminoacyl-tRNA synthetase, chromatin-remodeling, and spliceosome-related relationships. The absence of a STRING enrichment result and the lack of a single globally significant GO or KEGG term do not prove that the module is false or novel. A defensible novelty claim is therefore limited: the potentially novel aspect is the reproducible co-abundance of this particular combination across cervix_uterine and rectum, especially the way epithelial structure, nuclear transport, RNA processing, translation, and mitochondrial homeostasis appear together. This requires validation in independent cohorts, control for cell composition, and comparison with published tissue co-expression or proteomic modules before being called a new biological mechanism.

**Hypothesis.** Hypothesis: the shared module reflects a conserved epithelial tissue maintenance state in which nuclear transport and RNA maturation are coordinated with translation, mitochondrial quality and energy management, membrane transport, and cytoskeletal integrity. In this model, NUP155 and NUP210 support regulated nucleocytoplasmic exchange; SRRT, PRPF4, and PRMT5 support RNA-processing and gene-expression control; DARS1 and QARS1 support protein synthesis capacity; CHCHD3, IMMT, and DNM1L support mitochondrial architecture and dynamics; and KRT8 with KRT18 supports epithelial structural resilience. The hypothesis predicts that the module will track epithelial integrity and cellular metabolic demand, rather than a single specialized pathway. It also predicts that apparent variation in the module should be tested against epithelial abundance, stromal or immune admixture, tissue injury, and mitochondrial or proliferative state.

### Important genes

#### SRRT

- **Related proteins** (co-abundance neighbors): NUP210 (0.92), KRT8 (0.87), GPD2 (0.86), NUP155 (0.86), ZC3HAV1 (0.86), DARS1 (0.86), SMARCA4 (0.86), EDC4 (0.85), ATP1A1 (0.84), COLGALT1 (0.83), NSDHL (0.82), QARS1 (0.82), MISP (0.80), ACTL6A (0.80); STRING partners: CCAR1 (0.857)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serrate, RNA effector molecule. Enables mRNA cap binding complex binding activity and protein-macromolecule adaptor activity. Involved in primary miRNA processing. Located in nucleoplasm. Part of ribonucleoprotein complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dengue disease (0.370); myxedema (0.228); hypothyroidism (0.228); neurodegenerative disease (0.227); hair color (0.175)
- **Europe PMC papers**: 413
- **Why important**: SRRT is the highest-positioned network hub in the supplied module and connects nuclear-pore genes, keratin, metabolic genes, DARS1, SMARCA4, and EDC4. Its established functions include primary microRNA processing, transcriptional regulation, and RNA-protein complex activity. Its broad tissue specificity and detection in both tissues make it a plausible integrator of a shared cellular state. Its literature volume is substantial, although less extensive than that of the major chromatin or epithelial genes in the module.
- **Conclusion**: Established evidence supports SRRT as a central RNA-processing and regulatory component with strong network connectivity. It is reasonable to hypothesize that SRRT helps coordinate the module, but the co-abundance network does not establish that SRRT causally drives the other genes or that microRNA processing is the dominant module function.

#### NUP155

- **Related proteins** (co-abundance neighbors): NSDHL (0.89), SMARCA4 (0.87), MISP (0.87), EDC4 (0.87), SRRT (0.86), QARS1 (0.85), DNM1L (0.85), DARS1 (0.84), PRPF4 (0.84), UGGT1 (0.81), CTNNA1 (0.81), NUP210 (0.80); STRING partners: NUP210 (0.991)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07645.1
- **Function (MyGene.info)**: nucleoporin 155. Nucleoporins are proteins that play an important role in the assembly and functioning of the nuclear pore complex (NPC) which regulates the movement of macromolecules across the nuclear envelope (NE). The protein encoded by this gene plays a role in the fusion of NE vesicles and formation of the double membrane NE. The protein may also be involved in cardiac physiology and may be associated with t…
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); atrial fibrillation (0.470); familial atrial fibrillation (0.390)
- **Europe PMC papers**: 944
- **Why important**: NUP155 is a prominent network hub and is directly linked in STRING to NUP210. It is a nuclear-pore component involved in nucleocytoplasmic transport and nuclear-envelope organization, and it is represented with NUP210 in hu.MAP complex (hu.MAP huMAP3_07645.1). Its disease associations include familial atrial fibrillation and nuclear-envelope-related biology. Its network position makes it a strong structural anchor for the nuclear-transport interpretation.
- **Conclusion**: Established evidence supports NUP155 as a nuclear-pore and nuclear-envelope component that provides a coherent explanation for part of the module. Its lack of HPA detection in the two tissues weakens a direct protein-level localization claim in these samples, so its role as a module driver remains a hypothesis rather than a demonstrated tissue-specific mechanism.

#### NUP210

- **Related proteins** (co-abundance neighbors): SRRT (0.92), CTNNA1 (0.89), ATP1A1 (0.87), GPD2 (0.86), DARS1 (0.82), ZC3HAV1 (0.82), QARS1 (0.81), PRPF4 (0.81), IMMT (0.81), NUP155 (0.80); STRING partners: NUP155 (0.991)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: huMAP3_07645.1
- **Function (MyGene.info)**: nucleoporin 210. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. The protein encoded by this gene is a membrane-spanning glycoprotein that is a major component of the nuclear pore complex. M…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.536); COVID-19 (0.407); Histiocytosis (0.370)
- **Europe PMC papers**: 642
- **Why important**: NUP210 is a network hub paired with NUP155 by a very strong STRING relationship and by hu.MAP complex (hu.MAP huMAP3_07645.1). It is a membrane-spanning nuclear-pore glycoprotein involved in nucleocytoplasmic transport, and HPA shows enhancement in bone marrow and lymphoid tissue together with detection in both tissues. Its connections to SRRT, CTNNA1, ATP1A1, DARS1, QARS1, and PRPF4 place it at the interface of nuclear transport, epithelial organization, and gene-expression machinery.
- **Conclusion**: Established evidence supports NUP210 as an important nuclear-pore component and a plausible bridge between the module's structural and gene-expression features. The hematopoietic expression pattern means cell-composition effects should be tested before assigning the module exclusively to epithelial cells.

#### DARS1

- **Related proteins** (co-abundance neighbors): SRRT (0.86), EDC4 (0.85), NUP155 (0.84), ADGRE5 (0.83), GRSF1 (0.83), NUP210 (0.82), PRPF4 (0.82), NSDHL (0.81), COLGALT1 (0.81), ZC3HAV1 (0.81); STRING partners: QARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 1. This gene encodes a member of a multienzyme complex that functions in mediating the attachment of amino acids to their cognate tRNAs. The encoded protein ligates L-aspartate to tRNA(Asp). Mutations in this gene have been found in patients showing hypomyelination with brainstem and spinal cord involvement and leg spasticity. Alternative splicing results in multiple transcript variants. [provided by…
- **Diseases (Open Targets)**: hypomyelination with brain stem and spinal cord involvement and leg spasticity (0.773); atrial fibrillation (0.268); Abnormal brain morphology (0.266); tooth hard tissue disease (0.226); Pancreatic pseudocyst (0.225)
- **Europe PMC papers**: 238
- **Why important**: DARS1 is a highly connected module member linking SRRT, EDC4, NUP155, ADGRE5, GRSF1, NUP210, PRPF4, and NSDHL. Its established function is charging tRNA with aspartate, and STRING directly connects it to QARS1. It is present in hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), supporting a recognized aminoacyl-tRNA synthetase context. Its low tissue and immune specificity and detection in both tissues favor a general cellular role.
- **Conclusion**: Established evidence supports DARS1 as a translation-capacity and protein-synthesis component that may connect RNA processing with cellular maintenance. The network supports coordination with QARS1 and other module processes, but does not demonstrate altered translation or a causal role in the shared tissue signature.

#### PRPF4

- **Related proteins** (co-abundance neighbors): EDC4 (0.87), GPD2 (0.86), NUP155 (0.84), KRT8 (0.83), DARS1 (0.82), NUP210 (0.81), ATP1A1 (0.81), QARS1 (0.81), ZC3HAV1 (0.80), COLGALT1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: pre-mRNA splicing tri-snRNP complex factor PRPF4. The protein encoded by this gene is part of a heteromeric complex that binds U4, U5, and U6 small nuclear RNAs and is involved in pre-mRNA splicing. The encoded protein also is a mitotic checkpoint protein and a regulator of chemoresistance in human ovarian cancer. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: retinitis pigmentosa (0.634); retinitis pigmentosa 70 (0.578); inherited retinal dystrophy (0.377); neurodegenerative disease (0.203); refractive error (0.083)
- **Europe PMC papers**: 461
- **Why important**: PRPF4 is a central connector in the module and links EDC4, GPD2, NUP155, KRT8, DARS1, NUP210, ATP1A1, and QARS1. It is an established component of the U4, U5, and U6 small nuclear RNA-associated spliceosomal machinery and is represented with PRMT5 in hu.MAP complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1). Its detection in both tissues and its nuclear-speckle localization are consistent with a shared RNA-processing state.
- **Conclusion**: Established evidence supports PRPF4 as a spliceosome-related component and a plausible bridge between nuclear transport, RNA processing, and translation-related genes. The module does not establish a specific splicing program or disease mechanism, so those remain hypotheses.

#### KRT8

- **Related proteins** (co-abundance neighbors): SRRT (0.87), GLS (0.86), KRT18 (0.86), PRPF4 (0.83), GPD2 (0.82), EDC4 (0.81); STRING partners: KRT18 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Intermediate filaments; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 8. This gene is a member of the type II keratin family clustered on the long arm of chromosome 12. Type I and type II keratins heteropolymerize to form intermediate-sized filaments in the cytoplasm of epithelial cells. The product of this gene typically dimerizes with keratin 18 to form an intermediate filament in simple single-layered epithelial cells. This protein plays a role in maintaining cellul…
- **Diseases (Open Targets)**: cirrhosis of liver (0.596); cirrhosis, familial (0.401); neurodegenerative disease (0.371); prostate carcinoma (0.314); Abnormality of the liver (0.306)
- **Europe PMC papers**: 5942
- **Why important**: KRT8 is the principal epithelial structural marker among the selected genes and forms the known KRT8-KRT18 intermediate-filament pair in STRING. It is tissue enhanced in intestine and stomach, cell-type enhanced in colonocytes, enterocytes, and related epithelial populations, and detected in both tissues. Its extensive literature and disease associations make it an informative anchor for interpreting the shared module as at least partly epithelial.
- **Conclusion**: Established evidence supports KRT8 as an epithelial intermediate-filament component and a marker of epithelial structural state. Its presence does not prove that the entire module is epithelial, because several members have mitochondrial, nuclear, immune-associated, or broadly expressed profiles.

## Module 2

**Tissue pair**: cervix_uterine and rectum  
**Genes (47)**: ACIN1, AFDN, ARHGEF1, CLIC1, CNOT12, CTNND1, DSP, DLG1, EFHD2, CLINT1, EPS8L2, H1-2, H1-5, MACROH2A1, HMGA1, HMGB3, EIF4E, KGD4, LGALS3BP, LMO7, IGF2R, MYH14, MYO1B, MYO6, PDCD10, PKP3, JUP, POF1B, PPP4C, PTPN6, PRXL2A, RPL12, RPL9, RPE, RRBP1, SH3BGRL2, SNRPD1, SNAP23, SSR1, STRN, TST, TMEM214, TM9SF2, TOM1, SLC25A1, XPO4, TJP2

### Function

The module is best interpreted as an epithelial cell-junction and barrier-organization module. The strongest primary evidence is enrichment for adherens junction (GO:CC adherens junction; q_global = 0.00153), cell-cell junction organization (GO:BP cell-cell junction organization; q_global = 0.00924), cell-cell junction (GO:CC cell-cell junction; q_global = 0.0125), and anchoring junction (GO:CC anchoring junction; q_global = 0.0278). The associated genes include afadin, catenin delta one, desmoplakin, junction plakoglobin, plakophilin three, POF1B, and tight-junction protein two, linking cadherin-associated adhesion, desmosomes, tight junctions, and actin-associated junctional architecture. The heterochromatin term (GO:CC heterochromatin; q_global = 0.0363) is also globally significant, but it is supported by a smaller chromatin-associated submodule involving CNOT12, H1-5, HMGA1, and MACROH2A1; it is better viewed as a secondary nuclear component rather than the dominant module function. The STRING results independently reinforce the junction interpretation through cell-junction, adherens-junction, apical-junction, and tight-junction annotations (12 supplementary STRING terms; within-query FDR 0.004–0.0483).

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the HPA summary identifies only a minority of secreted genes, while most proteins are intracellular, membrane-associated, or junctional. The composition is strongly compatible with epithelial material. Many genes are tissue-enhanced in esophagus, skin, intestine, or related epithelial compartments, and the most frequent cell-type signal is for esophageal apical cells, with additional enterocyte, colonocyte, and basal or suprabasal epithelial signals. This supports a shared epithelial-cell program in cervix and rectum rather than a generic plasma-protein signature. There is nevertheless a possible immune or blood-cell contribution: several genes have immune-cell-enhanced or blood-cell-enriched HPA patterns, particularly among monocyte, neutrophil, eosinophil, platelet, and lymphoid populations. Therefore, sample composition or epithelial-immune admixture should be considered when interpreting the conserved co-abundance pattern. Protein detection in both tissues is broad for the module, but detection does not by itself establish coordinated regulation or cell-type purity.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC adherens junction | 0.00153 | AFDN, CNOT12, CTNND1, DLG1, DSP, JUP, PKP3, POF1B, SNAP23, TJP2 |
| GO:BP cell-cell junction organization | 0.00924 | AFDN, DLG1, DSP, JUP, PKP3, POF1B, STRN, TJP2 |
| GO:CC cell-cell junction | 0.0125 | AFDN, CNOT12, CTNND1, DLG1, DSP, JUP, PKP3, POF1B, PTPN6, SNAP23, STRN, TJP2 |
| GO:CC anchoring junction | 0.0278 | AFDN, CNOT12, CTNND1, DLG1, DSP, HMGA1, IGF2R, JUP, LMO7, PKP3, POF1B, PTPN6, RPL12, RPL9, SNAP23, STRN, TJP2 |
| GO:CC heterochromatin | 0.0363 | CNOT12, H1-5, HMGA1, MACROH2A1 |

### STRING and hu.MAP

STRING provides a partially known physical and functional backbone. The strongest junctional relationships include AFDN with CTNND1 and TJP2, DSP with JUP and PKP3, and CTNND1 with JUP and PTPN6. These links agree with the junction annotations (12 supplementary STRING terms; within-query FDR 0.004–0.0483) and indicate that the central adhesion signal is not merely an artifact of one isolated annotation. Additional STRING links connect MYO6 with TOM1, STRN with PDCD10, and the linker histones with each other, suggesting vesicle-trafficking, STRIPAK-related signaling, and chromatin components around the junctional core. hu.MAP independently places JUP, DSP, POF1B, and PKP3 together in epithelial or desmosomal complexes (hu.MAP huMAP3_09125.1), (hu.MAP huMAP3_09929.1), (hu.MAP huMAP3_05845.1), and (hu.MAP huMAP3_08595.1). It also supports STRN, PPP4C, and PDCD10 in related phosphatase or STRIPAK-associated complexes (hu.MAP huMAP3_09709.1) (hu.MAP huMAP3_10333.1) (hu.MAP huMAP3_13510.1), AFDN with LMO7 (hu.MAP huMAP3_05977.1), and TJP2 with EFHD2 (hu.MAP huMAP3_06395.1) and (hu.MAP huMAP3_10673.1). Thus, several module relationships are already known, while the complete co-abundance organization is broader than the directly documented interaction subgraph.

**STRING interactions (score >= 0.7)**: 13 of 1081 gene pairs: AFDN–CTNND1 (0.998); AFDN–LMO7 (0.983); AFDN–TJP2 (0.999); CTNND1–DSP (0.808); CTNND1–JUP (0.901); CTNND1–PTPN6 (0.936); DSP–JUP (0.999); DSP–PKP3 (0.93); H1-2–H1-5 (0.704); JUP–PKP3 (0.851); MYO6–TOM1 (0.981); PDCD10–STRN (0.999); RPL12–RPL9 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Cell-cell junction (FDR = 0.004, 10 genes); COMPARTMENTS Adherens junction (FDR = 0.0054, 7 genes); Process Cell-cell junction organization (FDR = 0.0066, 9 genes); Component Cell-cell junction (FDR = 0.0091, 12 genes); Component Adherens junction (FDR = 0.0091, 9 genes); COMPARTMENTS Apical junction complex (FDR = 0.0149, 6 genes); Keyword Cell junction (FDR = 0.019, 11 genes); COMPARTMENTS Cell-cell contact zone (FDR = 0.0245, 5 genes); Process Cell-cell junction assembly (FDR = 0.0257, 7 genes); Component Apical junction complex (FDR = 0.0404, 6 genes); Component Anchoring junction (FDR = 0.0404, 16 genes); COMPARTMENTS Tight junction (FDR = 0.0483, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09125.1 (JUP, DSP, POF1B, PKP3; 4/53); huMAP3_09929.1 (JUP, DSP, POF1B, PKP3; 4/75); huMAP3_09709.1 (STRN, PPP4C, PDCD10; 3/57); huMAP3_10333.1 (STRN, PPP4C, PDCD10; 3/63); huMAP3_13510.1 (STRN, PPP4C, PDCD10; 3/85); huMAP3_06046.1 (POF1B, PKP3; 2/5); huMAP3_07972.1 (POF1B, PKP3; 2/7); huMAP3_06395.1 (EFHD2, TJP2; 2/8); huMAP3_05977.1 (AFDN, LMO7; 2/12); huMAP3_10673.1 (EFHD2, TJP2; 2/14); huMAP3_07620.1 (STRN, PDCD10; 2/15); huMAP3_07644.1 (STRN, PDCD10; 2/19); huMAP3_05845.1 (JUP, DSP; 2/24); huMAP3_08595.1 (JUP, DSP; 2/25); huMAP3_09542.1 (MYO1B, LMO7; 2/38)

### Novelty

The broad biological interpretation is not a new discovery: epithelial junctions, desmosomal proteins, and tight-junction proteins are already established, and many of the central pairwise relationships are present in STRING or hu.MAP. The potentially novel aspect is the conserved co-abundance module shared by cervix and rectum, including its particular combination of junctional, trafficking, cytoskeletal, chromatin, and immune-associated signals. However, the fact sheet does not provide an external catalogue comparison, replication cohort, perturbation experiment, or tissue-cell deconvolution that would establish module-level novelty. The appropriate conclusion is therefore that this is a potentially informative conserved tissue-pair pattern, not a proven new molecular complex or newly discovered pathway. Absence of some genes from STRING or hu.MAP should be treated as incomplete knowledge, not evidence of novelty.

**Hypothesis.** Mechanistic hypothesis: the module reflects coordinated abundance of epithelial junctional machinery that maintains apical-basal organization, intercellular adhesion, and barrier integrity in both cervix and rectum. A core formed by AFDN, CTNND1, DSP, JUP, PKP3, POF1B, and TJP2 could couple cadherin-associated adhesion, desmosomal anchoring, and tight-junction organization to actin and myosin-dependent remodeling. MYO6, MYO1B, LMO7, SNAP23, and trafficking-related proteins may support membrane delivery or turnover of this machinery. STRN, PDCD10, and PPP4C may connect junctional state to phosphatase and signaling control, while the chromatin genes in (GO:CC heterochromatin; q_global = 0.0363) may reflect epithelial differentiation or state-dependent transcriptional regulation. The immune signals may represent genuine epithelial-immune interaction or varying immune admixture; this distinction requires cell-resolved data and functional validation.

### Important genes

#### CTNND1

- **Related proteins** (co-abundance neighbors): DSP (0.92), JUP (0.91), MYH14 (0.90), MYO6 (0.88), LGALS3BP (0.88), XPO4 (0.86), PKP3 (0.85), TMEM214 (0.84), SH3BGRL2 (0.83), ACIN1 (0.82), EIF4E (0.82), ARHGEF1 (0.80); STRING partners: AFDN (0.998), DSP (0.808), JUP (0.901), PTPN6 (0.936)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin delta 1. This gene encodes a member of the Armadillo protein family, which function in adhesion between cells and signal transduction. Multiple translation initiation codons and alternative splicing result in many different isoforms being translated. Not all of the full-length natures of the described transcript variants have been determined. Read-through transcription also exists between this gene and the…
- **Diseases (Open Targets)**: blepharocheilodontic syndrome (0.724); listeriosis (0.526); cleft lip (0.510); hereditary disease (0.415); exudative vitreoretinopathy (0.376)
- **Europe PMC papers**: 3021
- **Why important**: CTNND1 is a central network hub and connects directly to DSP, JUP, PKP3, AFDN, and PTPN6 in STRING. It occurs in the primary junction terms (GO:CC adherens junction; q_global = 0.00153), (GO:CC cell-cell junction; q_global = 0.0125), and (GO:CC anchoring junction; q_global = 0.0278), and its known functions include cadherin-mediated cell-cell adhesion, adhesion-associated signaling, and cell migration. Its plasma-membrane localization, junction relevance, disease associations involving epithelial development, and substantial literature make it a strong integrative marker of the module rather than a peripheral correlate.
- **Conclusion**: Established evidence supports CTNND1 as a central adhesion and signaling component of the module. It is plausible, but not demonstrated here, that CTNND1 helps coordinate the co-abundance of the desmosomal and tight-junction components.

#### DSP

- **Related proteins** (co-abundance neighbors): JUP (0.95), CTNND1 (0.92), POF1B (0.91), XPO4 (0.88), MYH14 (0.87), SH3BGRL2 (0.86), EIF4E (0.86), PKP3 (0.85), LGALS3BP (0.84), TMEM214 (0.81); STRING partners: CTNND1 (0.808), JUP (0.999), PKP3 (0.93)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cell Junctions; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1, huMAP3_05845.1, huMAP3_08595.1
- **Function (MyGene.info)**: desmoplakin. This gene encodes a protein that anchors intermediate filaments to desmosomal plaques and forms an obligate component of functional desmosomes. Mutations in this gene are the cause of several cardiomyopathies and keratodermas, including skin fragility-woolly hair syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016].
- **Diseases (Open Targets)**: arrhythmogenic cardiomyopathy with wooly hair and keratoderma (0.841); arrhythmogenic right ventricular dysplasia 8 (0.812); arrhythmogenic right ventricular cardiomyopathy (0.760); lethal acantholytic epidermolysis bullosa (0.745); cardiomyopathy, dilated, with wooly hair, keratoderma, and tooth agenesis (0.741)
- **Europe PMC papers**: 17350
- **Why important**: DSP is among the strongest junctional network members and is connected in STRING to JUP, CTNND1, and PKP3. It appears across the primary junction terms (4 globally significant GO/KEGG terms, q_global 0.00153–0.0278; see the table), is located at cell junctions, and encodes the obligate desmosomal plaque component that anchors intermediate filaments. It is represented in multiple hu.MAP epithelial and desmosomal complexes (hu.MAP huMAP3_09125.1), (hu.MAP huMAP3_09929.1), (hu.MAP huMAP3_05845.1), and (hu.MAP huMAP3_08595.1), has extensive literature, and has well-established cardiomyopathy and skin-fragility disease associations.
- **Conclusion**: Established evidence identifies DSP as a structural desmosomal cornerstone of the module. Its co-abundance in both tissues is consistent with shared epithelial junctional integrity, although the data do not prove that DSP drives the module.

#### JUP

- **Related proteins** (co-abundance neighbors): DSP (0.95), CTNND1 (0.91), MYH14 (0.89), PKP3 (0.88), TJP2 (0.83); STRING partners: CTNND1 (0.901), DSP (0.999), PKP3 (0.851)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1, huMAP3_05845.1, huMAP3_08595.1
- **Function (MyGene.info)**: junction plakoglobin. This gene encodes a major cytoplasmic protein which is the only known constituent common to submembranous plaques of both desmosomes and intermediate junctions. This protein forms distinct complexes with cadherins and desmosomal cadherins and is a member of the catenin family since it contains a distinct repeating amino acid motif called the armadillo repeat. Mutation in this gene has been associa…
- **Diseases (Open Targets)**: Naxos disease (0.784); arrhythmogenic right ventricular dysplasia 12 (0.755); arrhythmogenic right ventricular cardiomyopathy (0.597); lethal acantholytic epidermolysis bullosa (0.383); familial isolated arrhythmogenic ventricular dysplasia, biventricular form (0.370)
- **Europe PMC papers**: 3429
- **Why important**: JUP occupies the junctional core through strong STRING relationships with DSP, CTNND1, PKP3, and TJP2. It is present in (4 globally significant GO/KEGG terms, q_global 0.00153–0.0278; see the table), localizes to the plasma membrane and cell junctions, and is a common plaque component of desmosomes and intermediate junctions. Its membership in several hu.MAP epithelial complexes (hu.MAP huMAP3_09125.1), (hu.MAP huMAP3_09929.1), (hu.MAP huMAP3_05845.1), and (hu.MAP huMAP3_08595.1), together with established desmosome, adhesion, migration, and arrhythmogenic disease biology, makes it an especially informative bridge between structural adhesion and signaling.
- **Conclusion**: Established evidence supports JUP as a core adaptor shared by desmosomal and other adhesion structures. A possible hypothesis is that JUP helps couple the module's structural junctional state to epithelial signaling, but that coupling is not directly tested by this co-abundance analysis.

#### TJP2

- **Related proteins** (co-abundance neighbors): JUP (0.83), MYO6 (0.82), LMO7 (0.81); STRING partners: AFDN (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: huMAP3_06395.1, huMAP3_10673.1
- **Function (MyGene.info)**: tight junction protein 2. This gene encodes a zonula occluden that is a member of the membrane-associated guanylate kinase homolog family. The encoded protein functions as a component of the tight junction barrier in epithelial and endothelial cells and is necessary for proper assembly of tight junctions. Mutations in this gene have been identified in patients with hypercholanemia, and genomic duplication of a 270 kb regio…
- **Diseases (Open Targets)**: cholestasis, progressive familial intrahepatic, 4 (0.800); hypercholanemia, familial 1 (0.647); autosomal dominant nonsyndromic hearing loss (0.558); progressive familial intrahepatic cholestasis type 2 (0.527); deafness (0.467)
- **Europe PMC papers**: 1748
- **Why important**: TJP2 is a direct marker of the tight-junction side of the module. It is included in all primary junction terms (4 globally significant GO/KEGG terms, q_global 0.00153–0.0278; see the table), has strong STRING support with AFDN, and is represented in hu.MAP complexes with EFHD2 (hu.MAP huMAP3_06395.1) and (hu.MAP huMAP3_10673.1). Its plasma-membrane and cell-junction localization, role in epithelial and endothelial barrier assembly, intestinal relevance, and associations with cholestatic and hearing disorders provide clear functional and disease context.
- **Conclusion**: Established evidence supports TJP2 as a barrier-organization component that broadens the module beyond desmosomes. It is reasonable to hypothesize that variation in TJP2 abundance marks differences in epithelial barrier state, but the present data do not establish barrier permeability.

#### POF1B

- **Related proteins** (co-abundance neighbors): DSP (0.91), RPL9; RPL9P7; RPL9P8; RPL9P9 (0.90), MYO6 (0.86), H1-2 (0.81), H1-5 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Golgi apparatus; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1, huMAP3_06046.1, huMAP3_07972.1
- **Function (MyGene.info)**: POF1B actin binding protein. Premature ovarian failure (POF) is characterized by primary or secondary amenorrhea in women less than 40 years old. Two POF susceptibility regions called 'POF1' and 'POF2' have been identified by breakpoint mapping of X-autosome translocations. POF1 extends from Xq21-qter while POF2 extends from Xq13.3 to Xq21.1. This gene, POF1B, resides in the POF2 region. This gene is expressed at trace levels…
- **Diseases (Open Targets)**: primary ovarian failure (0.483); lymphatic system disorder (0.350); vein disorder (0.350); Varicose veins (0.341); premature ovarian failure 2B (0.231)
- **Europe PMC papers**: 329
- **Why important**: POF1B has a meaningful network position through DSP, MYO6, histone-associated neighbors, and the junctional module. It appears in every primary junction term (4 globally significant GO/KEGG terms, q_global 0.00153–0.0278; see the table) and in many supplementary STRING junction terms, while hu.MAP places it with JUP, DSP, and PKP3 in epithelial complexes (hu.MAP huMAP3_09125.1), (hu.MAP huMAP3_09929.1), (hu.MAP huMAP3_06046.1), and (hu.MAP huMAP3_07972.1). Its HPA pattern is enhanced in intestine, skin, colonocytes, enterocytes, and esophageal apical cells, and its annotated functions include actin organization and bicellular tight-junction assembly. Its disease association with primary ovarian failure and comparatively smaller literature base make it a potentially informative, less canonical component.
- **Conclusion**: Established evidence supports POF1B as an epithelial cytoskeletal or junction-associated component that fits the tissue and network context. Its precise mechanistic contribution to the shared cervix-rectum module remains a hypothesis and merits targeted functional testing.

## Module 3

**Tissue pair**: cervix_uterine and rectum  
**Genes (17)**: ACTN1, ANXA6, ATP2B4, CALD1, CAVIN1, CFL2, DPYSL2, FERMT2, FLNA, ITGB1, CKB, LPP, MCAM, PALLD, TES, TLN1, VCL

### Function


This module represents a contractile, actin-based cell-adhesion program centered on focal adhesions, cell-substrate junctions, integrin signaling, and actin organization. Primary evidence supports myofibril and contractile muscle fiber structures (GO:CC myofibril; q_global = 5.66e-05) (GO:CC contractile muscle fiber; q_global = 5.66e-05), focal adhesions and cell-substrate junctions (GO:CC focal adhesion; q_global = 7.31e-05) (GO:CC cell-substrate junction; q_global = 7.93e-05), plasma membrane and cell-periphery localization (GO:CC plasma membrane; q_global = 0.000213) (GO:CC cell periphery; q_global = 0.000498), actin binding (GO:MF actin binding; q_global = 0.00424), sarcomere-associated structures (GO:CC sarcomere; q_global = 0.00482), contractile actin bundles and actomyosin (4 globally significant GO/KEGG terms, q_global 0.0156–0.0295; see the table), focal-adhesion assembly (GO:BP focal adhesion assembly; q_global = 0.0324), cell-substrate adhesion (GO:BP cell-substrate adhesion; q_global = 0.0327), focal adhesion (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.034), and cell adhesion (GO:BP cell adhesion; q_global = 0.0432). The most coherent interpretation is a membrane-to-actin system that supports adhesion, cell shape, cytoskeletal organization, and mechanical or contractile behavior. The muscle annotations do not establish an origin in striated muscle, because the same genes are also associated with smooth muscle, vascular, stromal, epithelial, and platelet-related cell types.


**Cell composition.** 
The module contains no secreted genes, so it is not primarily a plasma or secreted-protein module. It is composed mainly of intracellular, plasma-membrane, focal-adhesion, and actin-associated proteins. HPA shows frequent association with smooth-muscle cells and vascular smooth-muscle cells, with additional associations involving platelets, myoepithelial cells, stromal cells, vascular cells, and selected myeloid populations. Several genes have low tissue specificity or broad cellular distributions. Therefore, the conserved signal may reflect shared structural cells, especially smooth-muscle or vascular-associated cells, in the two tissues. Platelet and myeloid annotations mean that blood or cellular admixture cannot be excluded, but the lack of secreted proteins and the strong focal-adhesion evidence argue against a circulating plasma explanation. Protein detection in both tissues for many members supports biological detectability, while genes not detected in one tissue should not be assumed to be uniformly expressed.


**GO/KEGG enrichment**: 24 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC myofibril | 5.66e-05 | ACTN1, ATP2B4, CALD1, CFL2, FERMT2, FLNA, PALLD, VCL |
| GO:CC contractile muscle fiber | 5.66e-05 | ACTN1, ATP2B4, CALD1, CFL2, FERMT2, FLNA, PALLD, VCL |
| GO:CC focal adhesion | 7.31e-05 | ACTN1, ANXA6, FERMT2, FLNA, ITGB1, LPP, MCAM, PALLD, TES, TLN1, VCL |
| GO:CC cell-substrate junction | 7.93e-05 | ACTN1, ANXA6, FERMT2, FLNA, ITGB1, LPP, MCAM, PALLD, TES, TLN1, VCL |
| GO:CC plasma membrane | 0.000213 | ACTN1, ANXA6, ATP2B4, CALD1, CAVIN1, CKB, DPYSL2, FERMT2, FLNA, ITGB1, LPP, MCAM, PALLD, TES, TLN1, VCL |
| GO:CC cell periphery | 0.000498 | ACTN1, ANXA6, ATP2B4, CALD1, CAVIN1, CKB, DPYSL2, FERMT2, FLNA, ITGB1, LPP, MCAM, PALLD, TES, TLN1, VCL |
| GO:CC I band | 0.00143 | ACTN1, ATP2B4, CFL2, FERMT2, FLNA, PALLD |
| GO:CC anchoring junction | 0.00173 | ACTN1, ANXA6, FERMT2, FLNA, ITGB1, LPP, MCAM, PALLD, TES, TLN1, VCL |
| KEGG Integrin signaling - Homo sapiens (human) | 0.0025 | ACTN1, FERMT2, FLNA, ITGB1, TLN1, VCL |
| GO:MF actin binding | 0.00424 | ACTN1, CALD1, CFL2, FERMT2, FLNA, ITGB1, PALLD, TLN1, VCL |
| GO:CC sarcomere | 0.00482 | ACTN1, ATP2B4, CFL2, FERMT2, FLNA, PALLD |
| GO:MF cell adhesion molecule binding | 0.00825 | ACTN1, CALD1, FERMT2, FLNA, ITGB1, MCAM, PALLD, TES, TLN1, VCL |
| GO:CC stress fiber | 0.0156 | ACTN1, CALD1, FERMT2, LPP, PALLD |
| GO:CC contractile actin filament bundle | 0.0156 | ACTN1, CALD1, FERMT2, LPP, PALLD |
| GO:CC cell junction | 0.0167 | ACTN1, ANXA6, ATP2B4, FERMT2, FLNA, ITGB1, LPP, MCAM, PALLD, TES, TLN1, VCL |

### STRING and hu.MAP


STRING provides prior support for a focal-adhesion and actin network. Known relationships connect ACTN1, FLNA, ITGB1, TLN1, and VCL, with additional links involving FERMT2, CFL2, and CALD1. These interactions agree with the primary GO and KEGG interpretation and indicate that much of the module reflects established integrin-cytoskeleton biology. STRING functional categories independently support focal adhesion, myofibril, cell periphery, actin binding, cell junction, and related structures (15 supplementary STRING terms; within-query FDR 2.07e-06–0.0015), but these are supplementary evidence rather than global enrichment evidence. hu.MAP places ITGB1 and ATP2B4 together in two larger complexes (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1). The partial overlap suggests that the module may represent a tissue-associated subnetwork or cellular context rather than a complete hu.MAP complex. The absence of hu.MAP entries for several members does not imply that they lack biological relationships.


**STRING interactions (score >= 0.7)**: 19 of 136 gene pairs: ACTN1–CFL2 (0.9); ACTN1–FLNA (0.716); ACTN1–ITGB1 (0.974); ACTN1–TLN1 (0.832); ACTN1–VCL (0.999); CALD1–VCL (0.771); CFL2–FLNA (0.888); CFL2–VCL (0.83); FERMT2–FLNA (0.852); FERMT2–ITGB1 (0.796); FERMT2–TLN1 (0.705); FERMT2–VCL (0.896); FLNA–ITGB1 (0.993); FLNA–TLN1 (0.998); FLNA–VCL (0.998); ITGB1–MCAM (0.82); ITGB1–TLN1 (0.999); ITGB1–VCL (0.966); TLN1–VCL (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Focal adhesion (FDR = 2.07e-06, 11 genes); Component Focal adhesion (FDR = 1.71e-05, 11 genes); Component Myofibril (FDR = 1.71e-05, 8 genes); COMPARTMENTS Myofibril (FDR = 6.19e-05, 6 genes); COMPARTMENTS Cell periphery (FDR = 0.00012, 13 genes); Component I band (FDR = 0.00019, 6 genes); COMPARTMENTS Z disc (FDR = 0.00022, 5 genes); Function Actin binding (FDR = 0.00025, 10 genes); Component Cell junction (FDR = 0.00047, 12 genes); Component Cell periphery (FDR = 0.00047, 15 genes); Component Plasma membrane (FDR = 0.00062, 14 genes); Keyword Cell junction (FDR = 0.00083, 8 genes); Function Cytoskeletal protein binding (FDR = 0.00089, 11 genes); COMPARTMENTS Cell-cell junction (FDR = 0.0014, 6 genes); Component Z disc (FDR = 0.0015, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10980.1 (ITGB1, ATP2B4; 2/44); huMAP3_09336.1 (ITGB1, ATP2B4; 2/50)

### Novelty


This is not a wholly new molecular pathway. The central functions of integrin adhesion, focal adhesions, actin anchoring, and contractile cytoskeletal organization are established by the known STRING relationships, gene annotations, and primary enrichment results. The potentially novel aspect is the conserved co-abundance of this particular combination across cervix_uterine and rectum. Its novelty is therefore best described as contextual or systems-level rather than discovery of an unknown pathway. The shared tissue-pair organization, relative gene composition, and reproducibility may provide new biological information. Absence from STRING or hu.MAP alone cannot establish novelty because database coverage and experimental context are incomplete.


**Hypothesis.** 
Mechanistic hypothesis: a shared population of smooth-muscle, vascular, stromal, epithelial, or other adherent cells in cervix_uterine and rectum produces this module through coordinated assembly of integrin-based focal adhesions and actin-associated contractile structures. ITGB1 may provide membrane linkage to extracellular matrix, while TLN1 and FERMT2 may couple integrin activation to the cytoskeleton. FLNA, ACTN1, VCL, PALLD, and LPP may organize and reinforce actin-linked junctions. CALD1, CFL2, ATP2B4, and CAVIN1 may contribute to contractility, actin dynamics, calcium handling, and membrane organization. This could support tissue architecture and mechanical responsiveness. This remains a hypothesis requiring cell-resolved, spatial, and perturbational validation.


### Important genes

#### FLNA

- **Related proteins** (co-abundance neighbors): FERMT2 (0.91), PALLD (0.90), CAVIN1 (0.90), LPP (0.86), CFL2 (0.84), ITGB1 (0.84); STRING partners: ACTN1 (0.716), CFL2 (0.888), FERMT2 (0.852), ITGB1 (0.993), TLN1 (0.998), VCL (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: 
FLNA is one of the most connected genes in the module and occurs across the primary adhesion, actin, membrane, and contractile annotations (19 globally significant GO/KEGG terms, q_global 5.66e-05–0.0432; see the table). Its established function is to crosslink actin and connect actin filaments to membrane glycoproteins, integrins, receptor complexes, and signaling components. STRING links it to ACTN1, CFL2, FERMT2, ITGB1, TLN1, and VCL. HPA associates it with blood vessels, intestine, myoepithelial cells, stromal cells, and megakaryocytes. Its disease associations and extensive literature support make it a strong mechanistic anchor.

- **Conclusion**: 
Established evidence supports FLNA as a central actin-to-membrane organizer and integrator of the module. Its role in coordinating the conserved tissue-pair co-abundance pattern is a plausible hypothesis, not a demonstrated causal conclusion.


#### FERMT2

- **Related proteins** (co-abundance neighbors): VCL (0.95), FLNA (0.91), PALLD (0.87), TES (0.86), LPP (0.83), DPYSL2 (0.80); STRING partners: FLNA (0.852), ITGB1 (0.796), TLN1 (0.705), VCL (0.896)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Focal adhesion sites; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FERM domain containing kindlin 2. Enables several functions, including actin binding activity; phosphatidylinositol-3,4,5-trisphosphate binding activity; and type I transforming growth factor beta receptor binding activity. Involved in several processes, including cell surface receptor signaling pathway; positive regulation of cell differentiation; and positive regulation of cellular component biogenesis. Acts upstream of or withi…
- **Diseases (Open Targets)**: open-angle glaucoma (0.501); prostate carcinoma (0.488); glaucoma (0.488); neurodegenerative disease (0.473); primary angle-closure glaucoma (0.407)
- **Europe PMC papers**: 1336
- **Why important**: 
FERMT2 is highly connected to VCL, FLNA, PALLD, TES, LPP, and DPYSL2. It occurs in the focal-adhesion, contractile, actin, adhesion, and integrin-related primary terms (21 globally significant GO/KEGG terms, q_global 5.66e-05–0.0432; see the table). Its established functions include actin binding, focal-adhesion localization, cell-matrix adhesion, integrin-mediated signaling, and receptor-associated signaling. HPA associates it with smooth-muscle cells and detects its protein in both tissues.

- **Conclusion**: 
Established evidence supports FERMT2 as an integrin-cytoskeleton coupling component. Its network position and detection in both tissues make it a strong candidate for maintaining the shared adhesion program, although causal importance remains unproven.


#### VCL

- **Related proteins** (co-abundance neighbors): FERMT2 (0.95), PALLD (0.93), CAVIN1 (0.86), LPP (0.84); STRING partners: ACTN1 (0.999), CALD1 (0.771), CFL2 (0.83), FERMT2 (0.896), FLNA (0.998), ITGB1 (0.966), TLN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vinculin. Vinculin is a cytoskeletal protein associated with cell-cell and cell-matrix junctions, where it is thought to function as one of several interacting proteins involved in anchoring F-actin to the membrane. Defects in VCL are the cause of cardiomyopathy dilated type 1W. Dilated cardiomyopathy is a disorder characterized by ventricular dilation and impaired systolic function, resulting in congestive…
- **Diseases (Open Targets)**: dilated cardiomyopathy 1W (0.692); hypertrophic cardiomyopathy 15 (0.660); hypertrophic cardiomyopathy (0.652); familial isolated dilated cardiomyopathy (0.642); cancer (0.605)
- **Europe PMC papers**: 10760
- **Why important**: 
VCL is a focal-adhesion protein connected within the module to FERMT2, PALLD, CAVIN1, and LPP. STRING links it to ACTN1, CALD1, CFL2, FERMT2, FLNA, ITGB1, and TLN1. It appears in the primary focal-adhesion, cell-substrate adhesion, actin-binding, integrin-signaling, and contractile terms (15 globally significant GO/KEGG terms, q_global 5.66e-05–0.0432; see the table). Its established role is anchoring actin to cell-cell and cell-matrix junctions. HPA detects it in both tissues and associates it with platelets.

- **Conclusion**: 
Established evidence supports VCL as a core mechanical linker. Its participation in transmitting information between integrin-associated membrane sites and actin is well supported, while the specific tissue-pair mechanism remains a hypothesis.


#### ITGB1

- **Related proteins** (co-abundance neighbors): ACTN1 (0.86), FLNA (0.84), TLN1 (0.84); STRING partners: ACTN1 (0.974), FERMT2 (0.796), FLNA (0.993), MCAM (0.82), TLN1 (0.999), VCL (0.966)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_10980.1, huMAP3_09336.1
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: 
ITGB1 is the principal membrane receptor component represented in the integrin-signaling and focal-adhesion KEGG terms (KEGG Integrin signaling - Homo sapiens (human); q_global = 0.0025) (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.034). It also occurs in multiple primary cell-adhesion and junction terms (10 globally significant GO/KEGG terms, q_global 7.31e-05–0.0432; see the table). STRING connects it to ACTN1, FERMT2, FLNA, MCAM, TLN1, and VCL. It is represented with ATP2B4 in the hu.MAP complexes (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1). Its established function is as an integrin beta subunit involved in adhesion, tissue repair, hemostasis, immune interactions, and matrix-linked signaling.

- **Conclusion**: 
Established evidence supports ITGB1 as a membrane-level entry point for the module. It is a compelling candidate regulator of the shared adhesion program, but the relevant alpha-integrin partner and extracellular ligand are not specified by the fact sheet.


#### PALLD

- **Related proteins** (co-abundance neighbors): VCL (0.93), FLNA (0.90), LPP (0.89), FERMT2 (0.87), CAVIN1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: palladin, cytoskeletal associated protein. This gene encodes a cytoskeletal protein that is required for organizing the actin cytoskeleton. The protein is a component of actin-containing microfilaments, and it is involved in the control of cell shape, adhesion, and contraction. Polymorphisms in this gene are associated with a susceptibility to pancreatic cancer type 1, and also with a risk for myocardial infarction. Alternative splicing re…
- **Diseases (Open Targets)**: coronary artery disorder (0.444); exocrine pancreatic carcinoma (0.372); coronary atherosclerosis (0.360); Bicuspid aortic valve (0.325); aortic stenosis (0.319)
- **Europe PMC papers**: 1170
- **Why important**: 
PALLD is connected to VCL, FLNA, LPP, FERMT2, and CAVIN1. It occurs in myofibril, focal-adhesion, actin-binding, stress-fiber, contractile-bundle, actomyosin, and cell-adhesion terms (18 globally significant GO/KEGG terms, q_global 5.66e-05–0.0432; see the table). Its established function is organizing the actin cytoskeleton and contributing to cell shape, adhesion, migration, and contraction. HPA associates it with cardiomyocytes, myonuclei, and smooth-muscle cells, with protein detected in both tissues. Its disease associations include cardiovascular and pancreatic conditions.

- **Conclusion**: 
Established evidence supports PALLD as an actin-architecture and contractile-adhesion organizer. Its position linking several structural proteins makes it a plausible module stabilizer, but a specific causal role in the conserved tissue-pair signal remains to be tested.


## Module 4

**Tissue pair**: cervix_uterine and rectum  
**Genes (45)**: AIMP2, AP3D1, HSPA5, CAPRIN1, CLUH, COPG2, DDX46, DNAJB1, EIF3C, FUS, GARS1, SHMT2, GMPS, HACL2, HYOU1, EIF5, ITGAM, LUC7L2, MCCC1, NSF, NSUN2, ALDH18A1, PRKDC, PSMC6, PSMC2, PTBP1, GART, UPF1, POLR2B, RUVBL2, SEC24A, SRPK1, EPRS1, KARS1, LARS1, RARS1, TUBA4A, CCT5, CCT3, CCT7, CCT8, TRAP1, TTLL12, TWF1, URB2

### Function

The module is best interpreted as a conserved intracellular proteostasis and biosynthetic-support program. The strongest primary evidence is broad enrichment for ATP, adenyl-ribonucleotide, purine-ribonucleotide, nucleotide, anion, and small-molecule binding (14 globally significant GO/KEGG terms, q_global 1.15e-06–0.0215; see the table), together with ATP-dependent protein folding and unfolded-protein binding (7 globally significant GO/KEGG terms, q_global 0.00015–0.0274; see the table). The CCT chaperonin signal is especially coherent: CCT3, CCT5, CCT7, and CCT8 support the chaperonin-containing T-complex and protein-folding-chaperone annotations (14 globally significant GO/KEGG terms, q_global 0.00015–0.018; see the table). A second layer involves aminoacyl-tRNA synthetase complex organization and translation support through EPRS1, KARS1, LARS1, RARS1, and AIMP2 (GO:CC intracellular protein-containing complex; q_global = 0.000401) (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.0284). Purine biosynthetic support is represented by GART and GMPS, while RNA handling is represented by CAPRIN1, NSUN2, DDX46, UPF1, and RUVBL2 (8 globally significant GO/KEGG terms, q_global 0.000251–0.0461; see the table). The telomere and Cajal-body terms (20 globally significant GO/KEGG terms, q_global 0.000251–0.0461; see the table) are biologically plausible but may partly reflect the concentrated contribution of the CCT subunits. Overall, the module most likely reflects coordinated protein folding, translation capacity, nucleotide supply, RNA processing, and stress-resilient maintenance of proliferative or metabolically active cells.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module. The HPA summary indicates mostly low tissue specificity, few secreted genes, and broad detection in both cervix_uterine and rectum for nearly all highlighted genes. It is also not strongly blood-cell enriched: immune-cell specificity is generally low, with only a limited signal involving ITGAM and SRPK1-associated basophil evidence. The module therefore does not look like a simple plasma contamination signature or a conventional leukocyte module. Its broadly expressed intracellular genes are consistent with a housekeeping-like cellular program, although the many cell-type-enhanced HPA annotations suggest that shared epithelial, germ-cell-like, secretory, or metabolically active cellular states could contribute. The differing detection of HYOU1, ITGAM, SEC24A, CLUH, and other genes between the two tissues also cautions against treating the module as a uniform tissue-specific program.

**GO/KEGG enrichment**: 44 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF ATP binding | 1.15e-06 | ALDH18A1, CAPRIN1, CCT3, CCT5, CCT7, CCT8, DDX46, EPRS1, GARS1, GART, GMPS, HSPA5, HYOU1, KARS1, LARS1, MCCC1, NSF, PRKDC, PSMC2, PSMC6, RARS1, RUVBL2, SRPK1, TRAP1, TTLL12, TWF1, UPF1 |
| GO:MF adenyl ribonucleotide binding | 1.26e-06 | ALDH18A1, CAPRIN1, CCT3, CCT5, CCT7, CCT8, DDX46, EPRS1, GARS1, GART, GMPS, HSPA5, HYOU1, KARS1, LARS1, MCCC1, NSF, PRKDC, PSMC2, PSMC6, RARS1, RUVBL2, SRPK1, TRAP1, TTLL12, TWF1, UPF1 |
| GO:MF purine ribonucleoside triphosphate binding | 2.77e-06 | ALDH18A1, CAPRIN1, CCT3, CCT5, CCT7, CCT8, DDX46, EIF5, EPRS1, GARS1, GART, GMPS, HSPA5, HYOU1, KARS1, LARS1, MCCC1, NSF, PRKDC, PSMC2, PSMC6, RARS1, RUVBL2, SRPK1, TRAP1, TTLL12, TUBA4A, TWF1, UPF1 |
| GO:MF purine ribonucleotide binding | 2.97e-06 | ALDH18A1, CAPRIN1, CCT3, CCT5, CCT7, CCT8, DDX46, EIF5, EPRS1, GARS1, GART, GMPS, HSPA5, HYOU1, KARS1, LARS1, MCCC1, NSF, PRKDC, PSMC2, PSMC6, RARS1, RUVBL2, SRPK1, TRAP1, TTLL12, TUBA4A, TWF1, UPF1 |
| GO:MF ribonucleotide binding | 3.23e-06 | ALDH18A1, CAPRIN1, CCT3, CCT5, CCT7, CCT8, DDX46, EIF5, EPRS1, GARS1, GART, GMPS, HSPA5, HYOU1, KARS1, LARS1, MCCC1, NSF, PRKDC, PSMC2, PSMC6, RARS1, RUVBL2, SRPK1, TRAP1, TTLL12, TUBA4A, TWF1, UPF1 |
| GO:MF heterocyclic compound binding | 5.5e-06 | ALDH18A1, CAPRIN1, CCT3, CCT5, CCT7, CCT8, DDX46, EIF5, EPRS1, GARS1, GART, GMPS, HACL2, HSPA5, HYOU1, KARS1, LARS1, MCCC1, NSF, POLR2B, PRKDC, PSMC2, PSMC6, RARS1, RUVBL2, SHMT2, SRPK1, TRAP1, TTLL12, TUBA4A, TWF1, UPF1 |
| GO:MF carbohydrate derivative binding | 1.04e-05 | ALDH18A1, CAPRIN1, CCT3, CCT5, CCT7, CCT8, DDX46, EIF5, EPRS1, GARS1, GART, GMPS, HSPA5, HYOU1, KARS1, LARS1, MCCC1, NSF, POLR2B, PRKDC, PSMC2, PSMC6, RARS1, RUVBL2, SRPK1, TRAP1, TTLL12, TUBA4A, TWF1, UPF1 |
| GO:MF adenyl nucleotide binding | 1.47e-05 | ALDH18A1, CAPRIN1, CCT3, CCT5, CCT7, CCT8, DDX46, EPRS1, GARS1, GART, GMPS, HSPA5, HYOU1, KARS1, LARS1, MCCC1, NSF, PRKDC, PSMC2, PSMC6, RARS1, RUVBL2, SRPK1, TRAP1, TTLL12, TWF1, UPF1 |
| GO:MF nucleotide binding | 2.19e-05 | ALDH18A1, CAPRIN1, CCT3, CCT5, CCT7, CCT8, DDX46, EIF5, EPRS1, GARS1, GART, GMPS, HACL2, HSPA5, HYOU1, KARS1, LARS1, MCCC1, NSF, PRKDC, PSMC2, PSMC6, RARS1, RUVBL2, SRPK1, TRAP1, TTLL12, TUBA4A, TWF1, UPF1 |
| GO:MF purine nucleotide binding | 2.61e-05 | ALDH18A1, CAPRIN1, CCT3, CCT5, CCT7, CCT8, DDX46, EIF5, EPRS1, GARS1, GART, GMPS, HSPA5, HYOU1, KARS1, LARS1, MCCC1, NSF, PRKDC, PSMC2, PSMC6, RARS1, RUVBL2, SRPK1, TRAP1, TTLL12, TUBA4A, TWF1, UPF1 |
| GO:MF nucleoside phosphate binding | 3.23e-05 | ALDH18A1, CAPRIN1, CCT3, CCT5, CCT7, CCT8, DDX46, EIF5, EPRS1, GARS1, GART, GMPS, HACL2, HSPA5, HYOU1, KARS1, LARS1, MCCC1, NSF, PRKDC, PSMC2, PSMC6, RARS1, RUVBL2, SRPK1, TRAP1, TTLL12, TUBA4A, TWF1, UPF1 |
| GO:MF anion binding | 3.95e-05 | ALDH18A1, CAPRIN1, CCT3, CCT5, CCT7, CCT8, DDX46, EIF5, EPRS1, GARS1, GART, GMPS, HACL2, HSPA5, HYOU1, KARS1, LARS1, MCCC1, NSF, PRKDC, PSMC2, PSMC6, RARS1, RUVBL2, SHMT2, SRPK1, TRAP1, TTLL12, TUBA4A, TWF1, UPF1 |
| GO:MF protein folding chaperone | 0.00015 | CCT3, CCT5, CCT7, CCT8, DNAJB1, HSPA5, HYOU1, TRAP1 |
| GO:MF ATP-dependent protein folding chaperone | 0.000177 | CCT3, CCT5, CCT7, CCT8, HSPA5, HYOU1, TRAP1 |
| GO:MF unfolded protein binding | 0.000185 | CCT3, CCT5, CCT7, CCT8, DNAJB1, HSPA5, HYOU1, RUVBL2, TRAP1 |

### STRING and hu.MAP

STRING provides strong known relationships within several coherent substructures. The CCT proteins form a tightly connected chaperonin group, with links to HSPA5 and RUVBL2. DNAJB1, HSPA5, HYOU1, and TRAP1 form a stress and protein-folding neighborhood. EPRS1, AIMP2, KARS1, LARS1, and RARS1 are connected both by STRING and by hu.MAP complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), supporting the aminoacyl-tRNA synthetase assembly interpretation. GART, GMPS, ALDH18A1, SHMT2, and related proteins provide known metabolic links, while PSMC2 and PSMC6 support a proteasome-associated ATPase component (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_10525.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). The hu.MAP results independently recover the CCT group (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), the stress-chaperone pair HSPA5-HYOU1 (hu.MAP huMAP3_07455.1), and metabolic or translation-associated complexes (hu.MAP huMAP3_14442.1) (hu.MAP huMAP3_13468.1) (hu.MAP huMAP3_10525.1). These known interactions show that much of the module is a coordinated collection of established cellular machines rather than an arbitrary set of correlated proteins. At the same time, several module edges and bridges, particularly those involving RNA processing, metabolism, and stress proteins, are not represented by reported STRING or hu.MAP relationships.

**STRING interactions (score >= 0.7)**: 57 of 990 gene pairs: AIMP2–EPRS1 (0.999); AIMP2–KARS1 (0.999); AIMP2–LARS1 (0.995); AIMP2–RARS1 (0.998); ALDH18A1–EPRS1 (0.723); ALDH18A1–GMPS (0.909); ALDH18A1–MCCC1 (0.732); ALDH18A1–SHMT2 (0.804); CAPRIN1–FUS (0.71); CAPRIN1–UPF1 (0.72); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT3–RUVBL2 (0.766); CCT3–TUBA4A (0.71); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT5–HSPA5 (0.727); CCT5–RUVBL2 (0.705); CCT7–CCT8 (0.999); CCT7–EIF3C (0.728); CCT7–HSPA5 (0.783); CCT7–RUVBL2 (0.802); CCT8–HSPA5 (0.701); CCT8–PSMC2 (0.733); CCT8–RUVBL2 (0.776); DDX46–LUC7L2 (0.74); DNAJB1–HSPA5 (0.95); DNAJB1–HYOU1 (0.765); DNAJB1–TRAP1 (0.704); DNAJB1–TTLL12 (0.797); EIF3C–EIF5 (0.998); EIF3C–EPRS1 (0.755); EPRS1–GARS1 (0.973); EPRS1–GART (0.752); EPRS1–GMPS (0.912); EPRS1–KARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–RARS1 (0.999); FUS–PTBP1 (0.852); GARS1–KARS1 (0.915); GARS1–LARS1 (0.895); GARS1–RARS1 (0.892); GART–GMPS (0.937); GART–SHMT2 (0.999); GMPS–KARS1 (0.835); GMPS–POLR2B (0.712); GMPS–RARS1 (0.872); HSPA5–HYOU1 (0.999); HSPA5–TRAP1 (0.787); KARS1–LARS1 (0.999); KARS1–RARS1 (0.999); LARS1–RARS1 (0.999); LUC7L2–SRPK1 (0.789); PRKDC–RUVBL2 (0.831); PSMC2–PSMC6 (0.999); RUVBL2–UPF1 (0.742)
**STRING functional enrichment (supplementary, within-query FDR)**: Function ATP binding (FDR = 1.25e-06, 26 genes); Keyword ATP-binding (FDR = 1.28e-06, 25 genes); Function Purine ribonucleotide binding (FDR = 1.43e-06, 28 genes); Function Purine ribonucleoside triphosphate binding (FDR = 1.43e-06, 28 genes); Function Carbohydrate derivative binding (FDR = 2.12e-06, 29 genes); Keyword Nucleotide-binding (FDR = 2.73e-06, 27 genes); Function Anion binding (FDR = 1.02e-05, 29 genes); Function Small molecule binding (FDR = 1.39e-05, 30 genes); Function Unfolded protein binding (FDR = 3.65e-05, 9 genes); Function ATP hydrolysis activity (FDR = 0.00014, 12 genes); Function Protein folding chaperone (FDR = 0.00016, 7 genes); Function Heterocyclic compound binding (FDR = 0.0002, 37 genes); Function Organic cyclic compound binding (FDR = 0.00028, 37 genes); Function ATP-dependent protein folding chaperone (FDR = 0.00034, 6 genes); Function ATP-dependent activity (FDR = 0.00054, 13 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, RARS1, AIMP2, KARS1, LARS1; 5/14); huMAP3_13688.1 (EPRS1, RARS1, AIMP2, KARS1, LARS1; 5/14); huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_14442.1 (GARS1, GMPS, TRAP1; 3/57); huMAP3_13468.1 (ALDH18A1, TRAP1, MCCC1; 3/99); huMAP3_07455.1 (HSPA5, HYOU1; 2/4); huMAP3_05064.1 (PSMC2, PSMC6; 2/31); huMAP3_10525.1 (ALDH18A1, MCCC1; 2/33); huMAP3_09656.1 (PSMC2, PSMC6; 2/64); huMAP3_13725.1 (PSMC2, PSMC6; 2/69)

### Novelty

The module should not be claimed as a wholly new molecular complex. Its central components recapitulate well-known CCT chaperonin, aminoacyl-tRNA synthetase, stress-chaperone, purine-metabolism, and proteasome relationships, as shown by STRING and hu.MAP (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_14442.1) (hu.MAP huMAP3_13468.1) (hu.MAP huMAP3_07455.1) (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_10525.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). The potentially novel finding is instead the conserved co-abundance organization of these established systems across cervix_uterine and rectum, including their specific cross-system wiring and shared tissue behavior. Absence of an edge from STRING or hu.MAP is not evidence of novelty, because those resources capture physical or curated relationships rather than tissue-specific co-abundance. Novelty therefore remains provisional and should be tested by replication in independent cohorts, preservation analysis, cell-composition adjustment, and orthogonal protein or transcript measurements.

**Hypothesis.** Hypothesis: the module represents a shared epithelial or metabolically active cellular state in which increased translation and RNA processing create demand for chaperone-assisted folding, nucleotide production, proteasomal quality control, and stress adaptation. EPRS1 and the associated synthetase complex could support aminoacylation and translational throughput; GART, GMPS, ALDH18A1, and SHMT2 could support nucleotide and mitochondrial metabolic capacity; CCT3, CCT5, CCT7, CCT8, HSPA5, HYOU1, and TRAP1 could buffer folding and organelle stress; and RUVBL2, PRKDC, UPF1, NSUN2, and related RNA or DNA maintenance factors could preserve genome and transcriptome integrity. The telomere and Cajal-body annotations suggest a possible link to proliferative maintenance, but this is a mechanistic hypothesis rather than proof that telomerase activity is altered in either tissue.

### Important genes

#### CCT8

- **Related proteins** (co-abundance neighbors): TRAP1 (0.89), CCT3 (0.88), EPRS1 (0.88), CCT7 (0.87), HYOU1 (0.85), SHMT2 (0.82), LARS1 (0.82), GMPS (0.81), KARS1 (0.80); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999), HSPA5 (0.701), PSMC2 (0.733), RUVBL2 (0.776)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is a high-centrality member of the module and sits within the densely connected CCT3-CCT5-CCT7-CCT8 subnetwork. It is present in essentially all of the module's chaperone, Cajal-body, telomere, ATPase, and protein-folding evidence (44 globally significant GO/KEGG terms, q_global 1.15e-06–0.0461; see the table), is supported by multiple hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), and has strong STRING links to the other CCT subunits, HSPA5, PSMC2, and RUVBL2. Its HPA profile is broadly expressed and detected in both tissues. It has substantial literature support and a disease-resource association with several neoplastic conditions.
- **Conclusion**: Established: CCT8 is a core component of the module's chaperonin and protein-folding signal, with extensive network and complex support. Hypothesis: CCT8 may act as a principal structural readout of increased proteostasis demand in the shared tissue state, but the co-abundance data do not establish causality or specific telomere regulation.

#### EPRS1

- **Related proteins** (co-abundance neighbors): LARS1 (0.89), ALDH18A1 (0.88), CCT8 (0.88), KARS1 (0.87), POLR2B (0.86), DDX46 (0.85), UPF1 (0.85), PRKDC (0.84), NSUN2 (0.83), TRAP1 (0.82), AP3D1 (0.80); STRING partners: AIMP2 (0.999), ALDH18A1 (0.723), EIF3C (0.755), GARS1 (0.973), GART (0.752), GMPS (0.912), KARS1 (0.999), LARS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is a highly connected bridge between the aminoacyl-tRNA synthetase complex, metabolic genes, RNA-related genes, and the CCT neighborhood. It participates in broad nucleotide-binding evidence and in the aminoacyl-tRNA synthetase multienzyme complex (16 globally significant GO/KEGG terms, q_global 1.15e-06–0.0284; see the table). STRING supports its relationships with AIMP2, KARS1, LARS1, RARS1, GARS1, GMPS, and EIF3C, while hu.MAP independently identifies the synthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). Its translation function and hereditary neurological disease associations make it biologically important, although its literature volume is more modest than that of the major chaperones.
- **Conclusion**: Established: EPRS1 anchors a known translation-support complex and connects that complex to the broader module. Hypothesis: coordinated EPRS1 abundance may couple translational throughput to chaperone capacity and metabolic supply in the shared tissue state.

#### HYOU1

- **Related proteins** (co-abundance neighbors): PRKDC (0.86), NSUN2 (0.86), CCT8 (0.85), CAPRIN1 (0.85), CCT5 (0.85), ALDH18A1 (0.84), UPF1 (0.82), PSMC6 (0.82), CCT7 (0.82), SHMT2 (0.80); STRING partners: DNAJB1 (0.765), HSPA5 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_07455.1
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 is a central stress-associated connector linking PRKDC, NSUN2, CCT proteins, CAPRIN1, UPF1, PSMC6, and ALDH18A1. It contributes to the globally corrected ATP-binding, protein-folding, unfolded-protein, ATP-dependent chaperone, and ATPase evidence (20 globally significant GO/KEGG terms, q_global 1.15e-06–0.0274; see the table). STRING and hu.MAP support its established relationships with HSPA5 and DNAJB1 (hu.MAP huMAP3_07455.1). Its annotated role in endoplasmic-reticulum protein folding, hypoxia, and stress responses, together with substantial literature, makes it a strong indicator of proteostasis and stress adaptation.
- **Conclusion**: Established: HYOU1 is part of a known stress and folding network and is detected in rectum. Hypothesis: its coordinated abundance may indicate an unfolded-protein or hypoxic burden shared by the two tissues, but the module alone cannot identify the initiating stress.

#### PRKDC

- **Related proteins** (co-abundance neighbors): HYOU1 (0.86), NSUN2 (0.85), EPRS1 (0.84), ALDH18A1 (0.82), KARS1 (0.81), CCT3 (0.81), CAPRIN1 (0.81), EIF3C (0.80), CCT5 (0.80); STRING partners: RUVBL2 (0.831)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase, DNA-activated, catalytic subunit. This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to DNA-PKcs deficiency (0.752); neurodegenerative disease (0.548); severe combined immunodeficiency (0.470); combined immunodeficiency (0.464); ovarian neoplasm (0.210)
- **Europe PMC papers**: 12461
- **Why important**: PRKDC has strong network connectivity to HYOU1, NSUN2, EPRS1, ALDH18A1, KARS1, CCT3, CAPRIN1, and EIF3C. It contributes to ATP-binding and telomere-maintenance annotations (18 globally significant GO/KEGG terms, q_global 1.15e-06–0.0215; see the table) and has a known STRING relationship with RUVBL2. Its established role in DNA-dependent protein kinase activity, double-strand-break repair, recombination, and telomere maintenance, plus extensive disease literature, gives it a plausible genome-integrity link within an otherwise largely proteostasis-focused module. HPA shows cell-type enhancement in erythrocyte progenitors and neutrophils but low overall immune-cell specificity.
- **Conclusion**: Established: PRKDC supplies a DNA-repair and genome-maintenance interpretation that is supported by the primary telomere terms and its known function. Hypothesis: PRKDC may connect stress-associated proteostasis to genome surveillance in the shared module, although cell-state composition could also explain part of its co-abundance.

#### ALDH18A1

- **Related proteins** (co-abundance neighbors): EPRS1 (0.88), RARS1 (0.88), SHMT2 (0.87), DDX46 (0.87), LARS1 (0.87), NSUN2 (0.87), PTBP1 (0.85), HYOU1 (0.84), COPG2 (0.82), UPF1 (0.82), PRKDC (0.82), RUVBL2 (0.80), AP3D1 (0.80), DNAJB1 (0.80), POLR2B (0.80), CCT7 (0.80); STRING partners: EPRS1 (0.723), GMPS (0.909), MCCC1 (0.732), SHMT2 (0.804)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1
- **Function (MyGene.info)**: aldehyde dehydrogenase 18 family member A1. This gene is a member of the aldehyde dehydrogenase family and encodes a bifunctional ATP- and NADPH-dependent mitochondrial enzyme with both gamma-glutamyl kinase and gamma-glutamyl phosphate reductase activities. The encoded protein catalyzes the reduction of glutamate to delta1-pyrroline-5-carboxylate, a critical step in the de novo biosynthesis of proline, ornithine and arginine. Mutations in …
- **Diseases (Open Targets)**: ALDH18A1-related de Barsy syndrome (0.832); cutis laxa, autosomal dominant 3 (0.816); autosomal recessive complex spastic paraplegia type 9B (0.814); de Barsy syndrome (0.731); autosomal dominant spastic paraplegia type 9 (0.706)
- **Europe PMC papers**: 1168
- **Why important**: ALDH18A1 is among the most connected genes and bridges EPRS1, RARS1, SHMT2, DDX46, LARS1, NSUN2, PTBP1, and HYOU1. It appears across the primary nucleotide-binding and small-molecule-binding terms (14 globally significant GO/KEGG terms, q_global 1.15e-06–0.0215; see the table) and is supported by STRING links to GMPS, MCCC1, SHMT2, and EPRS1 and by mitochondrial hu.MAP complexes (hu.MAP huMAP3_13468.1) (hu.MAP huMAP3_10525.1). Its established mitochondrial role in proline, ornithine, and arginine biosynthesis, together with disease associations involving connective tissue and neurological syndromes, makes it a useful metabolic anchor. Its literature support is substantial.
- **Conclusion**: Established: ALDH18A1 links mitochondrial amino-acid metabolism to the module's translation, nucleotide, and stress neighborhoods. Hypothesis: it may help supply metabolic capacity needed for the shared proteostasis state, but the data do not demonstrate altered flux through its pathway.

## Module 5

**Tissue pair**: cervix_uterine and rectum  
**Genes (9)**: BLVRB, CBR3, CPPED1, FCGBP, AHSG, JCHAIN, LUM, MARCKS, GC

### Function

The module is best interpreted as an extracellular and mucosal-interface co-abundance signature rather than as a validated single biochemical pathway. Its genes span secreted plasma proteins, mucosal epithelial and goblet-cell biology, immunoglobulin-associated secretion, extracellular-matrix biology, heme handling, xenobiotic or carbonyl metabolism, and cytoskeletal or membrane trafficking functions. FCGBP is the network hub and connects mucosal, extracellular, immune-associated, and metabolic signals. GC and AHSG indicate a liver-derived circulating-protein component, while JCHAIN points toward local or infiltrating antibody-secreting cells. LUM adds an extracellular-matrix component. No GO or KEGG term passed global correction; therefore, the annotations support biological interpretation but do not establish pathway enrichment. The absence of a globally significant term does not invalidate the module.

**Cell composition.** The module is compositionally heterogeneous and strongly compatible with mixed-source tissue signal. HPA annotates five genes as secreted, including GC, AHSG, JCHAIN, FCGBP, and LUM, and identifies GC and AHSG as liver-enriched or hepatocyte-associated circulating proteins. FCGBP is associated with goblet cells and intestine or salivary gland, JCHAIN with plasma cells and B-cell-related populations, LUM with extracellular matrix and stromal biology, and several genes with epithelial, neutrophil, monocyte, or erythroid-associated populations. HPA also reports immune-cell enhancement for part of the module and detection of most module proteins in rectum, with somewhat less detection in cervix. The shared signal may therefore reflect blood or plasma contribution, epithelial or goblet-cell material, stromal matrix, and immune-cell admixture rather than a uniform resident cell population. The presence of broadly distributed or low-specificity genes such as MARCKS and CPPED1 further weakens a narrowly tissue-specific interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides direct high-confidence support for the AHSG-GC relationship, while no other listed pair has a STRING interaction at the supplied threshold and STRING functional enrichment is absent. Thus, the observed co-abundance network is not equivalent to a densely documented protein-interaction complex. hu.MAP supplies convergent but partial context: AHSG and GC recur together in (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_09434.1), and (hu.MAP huMAP3_15040.1), and FCGBP joins them in (hu.MAP huMAP3_10678.1). These complexes are large, heterogeneous assemblies dominated by circulating, complement, coagulation, lipid-transport, and other extracellular proteins, so their partial overlap supports a shared extracellular or plasma-associated context but does not prove that all module members form one physical complex. The links involving FCGBP, MARCKS, LUM, JCHAIN, BLVRB, CPPED1, and CBR3 are primarily co-abundance observations here, not established physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 36 gene pairs: AHSG–GC (0.959)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10678.1 (AHSG, GC, FCGBP; 3/71); huMAP3_09434.1 (AHSG, GC; 2/33); huMAP3_15040.1 (AHSG, GC; 2/64)

### Novelty

This is not established as a new molecular complex or new pathway. The AHSG-GC relationship is already represented in STRING and in several hu.MAP complexes, and the component functions of FCGBP, JCHAIN, LUM, MARCKS, CBR3, BLVRB, and CPPED1 are individually known. What may be novel is the reproducible co-abundance pattern shared by cervix and rectum, especially the coupling of a mucosal hub with circulating liver proteins, antibody-associated secretion, matrix biology, and metabolic or heme-related genes. That tissue-pair association should be described as a potentially novel observation rather than a proven discovery, because the network is sparse, global enrichment is negative, and HPA indicates plausible variation in plasma content and cell composition. Absence of additional STRING or hu.MAP links cannot by itself establish novelty.

**Hypothesis.** Hypothesis: the module reflects a common mucosal-interface state in which epithelial or goblet-cell material, extracellular matrix, local humoral defense, and variable exposure to circulating liver-derived proteins are captured together in cervix and rectum samples. FCGBP may mark the mucosal epithelial component, JCHAIN may represent antibody-secreting-cell activity, LUM may represent stromal matrix context, and GC or AHSG may report plasma or hepatic-protein contribution. CPPED1 and CBR3 could be linked to local cellular stress or metabolic state, while BLVRB could reflect erythroid or heme-related material. This model predicts that the module will track epithelial, plasma, immune, and stromal composition more strongly than a single canonical pathway; it requires validation with cell deconvolution, plasma-contamination markers, spatial or single-cell data, and independent cohorts.

### Important genes

#### FCGBP

- **Related proteins** (co-abundance neighbors): MARCKS (0.92), LUM (0.89), GC (0.87), JCHAIN (0.84), BLVRB (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Plasma membrane; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: huMAP3_10678.1
- **Function (MyGene.info)**: Fc gamma binding protein. Located in extracellular exosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.307); Hodgkins lymphoma (0.220); alcohol drinking (0.214); ventricular septal defect (0.197); hereditary disease (0.118)
- **Europe PMC papers**: 1806
- **Why important**: FCGBP is the central network hub, linking MARCKS, LUM, GC, JCHAIN, and BLVRB. HPA associates it with intestine, salivary gland, and goblet cells, and identifies it as secreted or extracellular. It is therefore the strongest candidate marker of the mucosal epithelial component and the main bridge between epithelial, extracellular, immune-associated, and metabolic signals. Its literature base is substantial, and its Open Targets associations include several disease and phenotype categories.
- **Conclusion**: Established evidence supports FCGBP as the module’s topological hub and as a secreted, goblet-cell-associated mucosal protein. Hypothesis: FCGBP organizes or reports a shared mucosal-interface state in both tissues, but the co-abundance data do not prove that it physically regulates the other module genes.

#### GC

- **Related proteins** (co-abundance neighbors): FCGBP (0.87), CPPED1 (0.85); STRING partners: AHSG (0.959)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09434.1, huMAP3_15040.1
- **Function (MyGene.info)**: GC vitamin D binding protein. The protein encoded by this gene belongs to the albumin gene family. It is a multifunctional protein found in plasma, ascitic fluid, cerebrospinal fluid and on the surface of many cell types. It binds to vitamin D and its plasma metabolites and transports them to target tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq,…
- **Diseases (Open Targets)**: vitamin D deficiency (0.574); vitamin deficiency (0.552); chronic obstructive pulmonary disease (0.499); squamous cell carcinoma (0.339); central nervous system cancer (0.334)
- **Europe PMC papers**: 363974
- **Why important**: GC is directly connected to AHSG by the strongest supplied STRING relationship and is represented with AHSG in (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_09434.1), and (hu.MAP huMAP3_15040.1). HPA identifies it as liver-enriched, hepatocyte-associated, and secreted to blood. Its annotated roles in vitamin D binding and transport give it a plausible systemic-exposure interpretation, while its extensive literature and disease associations make it a well-characterized anchor for the circulating-protein component.
- **Conclusion**: Established evidence supports GC as a circulating, liver-derived vitamin-D-binding protein that is connected to AHSG in independent interaction or complex resources. Hypothesis: its presence in this shared mucosal module primarily reports plasma or extracellular-fluid contribution rather than a tissue-resident GC-centered pathway.

#### AHSG

- **Related proteins** (co-abundance neighbors): CPPED1 (0.85); STRING partners: GC (0.959)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09434.1, huMAP3_15040.1
- **Function (MyGene.info)**: alpha 2-HS glycoprotein. The protein encoded by this gene is a negatively-charged serum glycoprotein that is synthesized by hepatocytes. The encoded protein consists of two polypeptide chains, which are both cleaved from a proprotein encoded from a single mRNA. It is involved in several processes, including endocytosis, brain development, and the formation of bone tissue. Defects in this gene are a cause of susceptibility…
- **Diseases (Open Targets)**: alopecia - intellectual disability syndrome (0.476); otosclerosis (0.465); nephrolithiasis, calcium oxalate (0.417); calcium oxalate urolithiasis (0.416); neurodegenerative disease (0.204)
- **Europe PMC papers**: 2310
- **Why important**: AHSG is a liver-synthesized serum glycoprotein, is secreted to blood, and is connected to GC by STRING. It recurs with GC in (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_09434.1), and (hu.MAP huMAP3_15040.1), making it a key network and complex-context anchor despite its limited direct co-abundance connectivity. Its reported roles in endocytosis, acute-phase response, and mineralization provide biologically relevant links to extracellular regulation and systemic physiology.
- **Conclusion**: Established evidence supports AHSG as a circulating hepatic protein with known association to GC and repeated representation in hu.MAP contexts. Hypothesis: AHSG helps explain why this module is shared across tissues by marking a common plasma or acute-phase component, not necessarily a local cervix or rectum mechanism.

#### JCHAIN

- **Related proteins** (co-abundance neighbors): FCGBP (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Group enriched; location None; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: joining chain of multimeric IgA and IgM. Enables IgA binding activity and protein homodimerization activity. Contributes to several functions, including immunoglobulin receptor binding activity; peptidoglycan binding activity; and phosphatidylcholine binding activity. Involved in several processes, including defense response to other organism; glomerular filtration; and positive regulation of respiratory burst. Located in extracellular s…
- **Diseases (Open Targets)**: breast carcinoma (0.101); breast cancer (0.093); neoplasm (0.089); cancer (0.081); Barrett esophagus (0.062)
- **Europe PMC papers**: 2428
- **Why important**: JCHAIN connects to FCGBP and is secreted to blood. HPA associates it with plasma cells and memory or naive B-cell-related populations, and its known function is to join multimeric IgA and IgM and support humoral defense. It provides the clearest link between the mucosal epithelial signal and local or infiltrating antibody-associated immunity, despite having no STRING or hu.MAP relationship in the supplied evidence.
- **Conclusion**: Established evidence supports JCHAIN as an immunoglobulin-assembly and humoral-defense component associated with plasma-cell biology. Hypothesis: its co-abundance with FCGBP indicates coordinated mucosal barrier and antibody activity, or alternatively varying immune-cell abundance in the samples; the network alone cannot distinguish these possibilities.

#### LUM

- **Related proteins** (co-abundance neighbors): FCGBP (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lumican. This gene encodes a member of the small leucine-rich proteoglycan (SLRP) family that includes decorin, biglycan, fibromodulin, keratocan, epiphycan, and osteoglycin. In these bifunctional molecules, the protein moiety binds collagen fibrils and the highly charged hydrophilic glycosaminoglycans regulate interfibrillar spacings. Lumican is the major keratan sulfate proteoglycan of the cornea but is …
- **Diseases (Open Targets)**: lumbar disc herniation (0.359); Dupuytren Contracture (0.357); fibroblastic disorder (0.357); Hallux valgus (0.357); preeclampsia (0.154)
- **Europe PMC papers**: 14825
- **Why important**: LUM connects directly to FCGBP and is a secreted extracellular-matrix proteoglycan associated with collagen fibrils and matrix organization. HPA links it to gallbladder and placenta tissue and to decidual stromal cells, while its literature base is extensive. It contributes a stromal or matrix dimension that is not explained by the circulating proteins alone.
- **Conclusion**: Established evidence supports LUM as an extracellular-matrix and collagen-associated component of the module. Hypothesis: LUM marks stromal remodeling or matrix-rich mucosal context that is co-sampled with epithelial and plasma signals, rather than participating in a single molecular complex with FCGBP.

## Module 6

**Tissue pair**: cervix_uterine and rectum  
**Genes (14)**: BYSL, CANX, DDX21, SORD, MYBBP1A, NOP2, NUP107, PSMD13, PTDSS1, U2SURP, SRP72, TAP1, VDAC2, VPS35

### Function

No GO or KEGG term passed global correction, so there is no globally significant pathway assignment for this module. The gene annotations and network nevertheless suggest a broadly expressed intracellular maintenance module spanning nucleolar RNA and ribosome biology, RNA processing, proteostasis, membrane trafficking, endoplasmic-reticulum quality control, mitochondrial function, and antigen presentation. The strongest coherent functional signal is a nucleolar RNA-production and ribosome-biogenesis axis involving DDX21, MYBBP1A, NOP2 and BYSL, with additional links to protein quality control, transport, and cellular stress handling. This is an interpretation of the gene identities and network, not a claim of enrichment significance.

**Cell composition.** The module is not dominated by plasma or secreted proteins: every gene has no secretome annotation. Most genes have low tissue specificity, and the proteins are detected in both cervix_uterine and rectum for nearly all genes with available tissue data. HPA therefore supports a broadly expressed intracellular program rather than a tissue-exclusive secretory program. The module is also not broadly blood-cell enriched: most genes have low immune-cell specificity, although PTDSS1 is immune-cell enhanced and SORD is group enriched in basophils and eosinophils. Several genes show cell-type-enhanced annotations, including epithelial, neural, reproductive, and placental cell types, so shared cellular composition or common cellular activity could contribute to the cross-tissue co-abundance. The HPA evidence does not by itself establish blood contamination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a connected core involving DDX21, MYBBP1A, NOP2 and BYSL, with particularly strong reported links among DDX21, MYBBP1A and NOP2, and a further BYSL association with NOP2. STRING also reports CANX with TAP1. These are already known or database-supported relationships, so the module is not an entirely unconnected set of genes. The DDX21–MYBBP1A–NOP2–BYSL component is consistent with shared nucleolar RNA and ribosome-related biology, whereas the CANX–TAP1 link is consistent with endoplasmic-reticulum protein handling and antigen-processing machinery. The remaining module edges connect these functional neighborhoods through genes such as VPS35, VDAC2 and PSMD13. No hu.MAP complex contains at least two module members, so the data do not provide hu.MAP evidence for a shared experimentally defined complex. STRING relationships should be interpreted as prior knowledge supporting parts of the network, not as proof that all module genes form one physical complex.

**STRING interactions (score >= 0.7)**: 6 of 91 gene pairs: BYSL–MYBBP1A (0.73); BYSL–NOP2 (0.915); CANX–TAP1 (0.762); DDX21–MYBBP1A (0.963); DDX21–NOP2 (0.761); MYBBP1A–NOP2 (0.864)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be called a wholly new biological discovery. Several of its relationships and functions are already established in public knowledge, especially the nucleolar RNA and ribosome-related roles of DDX21, MYBBP1A, NOP2 and BYSL, and the cellular functions of the other annotated proteins. The absence of a qualifying hu.MAP complex and the lack of STRING support for some edges do not prove novelty. A potentially novel aspect is the reproducible co-abundance of this particular combination across cervix_uterine and rectum, especially the joint coupling of a nucleolar RNA-processing group with endoplasmic-reticulum, mitochondrial, trafficking, proteasomal and antigen-presentation genes. That cross-tissue module-level relationship is a hypothesis-generating observation and would require replication, covariate control, cell-composition analysis and independent functional testing before being considered a new mechanism.

**Hypothesis.** Hypothesis: the conserved module reflects a shared cellular state in which nucleolar RNA processing and ribosome production are coordinated with protein-folding quality control, proteasomal turnover, membrane trafficking, mitochondrial membrane function and antigen-presentation capacity. DDX21, MYBBP1A, NOP2 and BYSL may form the nucleolar regulatory core, while CANX, TAP1, VPS35, VDAC2 and PSMD13 represent connected downstream or parallel demands on protein maturation, transport, degradation and cellular stress adaptation. The cross-tissue signal may therefore arise from common epithelial or other shared cell populations, or from a general proliferative or stress-related state, rather than from a cervix- or rectum-specific pathway. This hypothesis is not established by the enrichment results, because no GO or KEGG term passed global correction.

### Important genes

#### DDX21

- **Related proteins** (co-abundance neighbors): MYBBP1A (0.92), VDAC2 (0.91), CANX (0.84), U2SURP (0.83), VPS35 (0.82), NOP2 (0.81), PSMD13 (0.80); STRING partners: MYBBP1A (0.963), NOP2 (0.761)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 is the most connected node in the module and links the nucleolar group to VDAC2, CANX, U2SURP, VPS35 and PSMD13. It is a DEAD-box RNA helicase with reported roles in RNA structural remodeling, ribosome and spliceosome assembly, gene regulation and chromatin-related processes. Its nucleoli-rim and mitotic-chromosome localization, detection in both tissues, substantial literature volume and disease associations make it a strong candidate for organizing the module's RNA-production and cellular-state signal.
- **Conclusion**: Established: DDX21 is a highly connected module node with nucleolar localization and documented RNA-related and regulatory functions. Conclusion: it is a plausible anchor of the module, but the co-abundance data do not establish that DDX21 causally controls the other genes.

#### MYBBP1A

- **Related proteins** (co-abundance neighbors): DDX21 (0.92), PTDSS1 (0.91), VDAC2 (0.87), NOP2 (0.84), CANX (0.81); STRING partners: BYSL (0.73), DDX21 (0.963), NOP2 (0.864)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MYB binding protein 1a. This gene encodes a nucleolar transcriptional regulator that was first identified by its ability to bind specifically to the Myb proto-oncogene protein. The encoded protein is thought to play a role in many cellular processes including response to nucleolar stress, tumor suppression and synthesis of ribosomal DNA. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep…
- **Diseases (Open Targets)**: neurodegenerative disease (0.507); Non-immune hydrops fetalis (0.370); ventricular septal defect (0.245); lysosomal storage disease (0.191); Meniere disease (0.162)
- **Europe PMC papers**: 763
- **Why important**: MYBBP1A has high network connectivity and bridges DDX21, NOP2, BYSL, PTDSS1, VDAC2 and CANX. It is a nucleolar transcriptional regulator associated with nucleolar stress, tumor suppression, chromatin remodeling and ribosomal DNA synthesis. Its position between the nucleolar genes and membrane or mitochondrial genes makes it informative for testing whether the module represents coordinated nucleolar stress and broader cellular adaptation.
- **Conclusion**: Established: MYBBP1A is a nucleolar regulator and has multiple strong STRING-supported relationships within the module. Conclusion: it is a credible integrative hub, while any proposed stress-signaling role in this tissue pair remains a hypothesis.

#### NOP2

- **Related proteins** (co-abundance neighbors): MYBBP1A (0.84), DDX21 (0.81); STRING partners: BYSL (0.915), DDX21 (0.761), MYBBP1A (0.864)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP2 nucleolar protein. Enables RNA binding activity. Involved in positive regulation of cell population proliferation; regulation of signal transduction by p53 class mediator; and ribosomal large subunit assembly. Located in nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.273); nonpapillary renal cell carcinoma (0.097); neoplasm (0.097); cancer (0.091); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 2120
- **Why important**: NOP2 is a nucleolar RNA-binding protein involved in ribosomal large-subunit assembly, ribosomal RNA maturation and RNA processing, and it is linked to positive regulation of cell-population proliferation. It connects directly in STRING to DDX21, MYBBP1A and BYSL, making it a compact marker of the module's most coherent functional neighborhood. Its substantial literature and cancer-related associations also make it biologically relevant when interpreting a possible growth or biosynthetic state.
- **Conclusion**: Established: NOP2 has direct nucleolar and ribosome-biogenesis functions and known relationships with other module members. Conclusion: NOP2 is a strong readout of the module's biosynthetic core, but proliferation or oncogenic activity cannot be inferred from this module alone.

#### TAP1

- **Related proteins** (co-abundance neighbors): VPS35 (0.83), SORD (0.80); STRING partners: CANX (0.762)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Centriolar satellite; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transporter 1, ATP binding cassette subfamily B member. The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily ar…
- **Diseases (Open Targets)**: MHC class I deficiency (0.760); MHC class II deficiency (0.371); autoimmune disorder of central nervous system (0.357); neurodegenerative disease (0.240); hereditary disease (0.193)
- **Europe PMC papers**: 7090
- **Why important**: TAP1 provides a functionally distinctive branch of the module. It transports cytosolic peptides into the endoplasmic reticulum for MHC class I antigen processing and presentation, is detected in both tissues, and has a direct STRING relationship with CANX. Its connection through VPS35 and SORD places antigen-processing capacity alongside trafficking and metabolic genes. Its disease associations and large literature base make it useful for evaluating whether immune-related cellular activity contributes to the shared module.
- **Conclusion**: Established: TAP1 is an ER-associated peptide transporter with an antigen-presentation function and a reported CANX relationship. Conclusion: TAP1 may mark an antigen-processing component of the module, but the HPA profile does not support interpreting the entire module as blood-cell derived.

#### VPS35

- **Related proteins** (co-abundance neighbors): SRP72 (0.83), TAP1 (0.83), DDX21 (0.82), VDAC2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in cervix_uterine, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS35 retromer complex component. This gene belongs to a group of vacuolar protein sorting (VPS) genes. The encoded protein is a component of a large multimeric complex, termed the retromer complex, involved in retrograde transport of proteins from endosomes to the trans-Golgi network. The close structural similarity between the yeast and human proteins that make up this complex suggests a similarity in function. Expression studie…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.743); neurodegenerative disease (0.553); young-onset Parkinson disease (0.503); Parkinson disease (0.482); Parkinson disease, dominant (0.370)
- **Europe PMC papers**: 3611
- **Why important**: VPS35 is a retromer component involved in endosome-to-trans-Golgi retrograde transport, lysosome organization and protein transport. It connects SRP72, TAP1, DDX21 and VDAC2, thereby linking secretory-pathway targeting, antigen processing, nucleolar-associated network structure and mitochondrial biology. Its strong disease literature, including Parkinson disease associations, makes it an informative candidate for the module's trafficking and cellular-maintenance interpretation.
- **Conclusion**: Established: VPS35 has retromer and intracellular trafficking functions and occupies a bridge position in the module. Conclusion: it is a plausible coordinator of the module's trafficking-related arm, but the data do not establish a disease mechanism or direct physical interaction with every connected gene.

## Module 7

**Tissue pair**: cervix_uterine and rectum  
**Genes (10)**: CTSG, CYBB, H1-3, H4C1, LYZ, MPO, RAB5C, RPL6, S100A8, S100A9

### Function

The module is best interpreted as a myeloid antimicrobial and phagocyte-effector program. The strongest primary evidence is defense against fungi (GO:BP defense response to fungus; q_global = 0.00096) (GO:BP response to fungus; q_global = 0.00143), defense against bacteria (GO:BP defense response to bacterium; q_global = 0.00814), phagocytosis (KEGG Phagocytosis - Homo sapiens (human); q_global = 0.0232), and respiratory burst (GO:BP respiratory burst; q_global = 0.0436). The constituent genes support complementary steps: LYZ provides antibacterial enzymatic activity; MPO and CTSG are granule effectors; S100A8 and S100A9 mark inflammatory myeloid cells and form a prominent paired signal; CYBB supports phagocyte oxidant production; and RAB5C is consistent with endosomal trafficking. The histone and ribosomal genes are not annotated by the primary enrichment terms and may reflect cellular state or sample composition rather than the core antimicrobial mechanism. The co-abundance structure therefore most plausibly represents coordinated abundance of infiltrating or resident myeloid cells, especially monocyte and neutrophil-lineage cells, rather than a tissue-specific epithelial program.

**Cell composition.** This is not primarily a housekeeping module, although H1-3, H4C1, and RPL6 are chromatin or ribosomal genes with broad cellular roles. Most of the biologically informative members are immune or antimicrobial genes. HPA links the module especially to bone marrow, monocyte progenitors, neutrophil progenitors, classical monocytes, and neutrophils, with additional associations to myeloid dendritic cells and related myeloid populations. HPA also reports secreted-to-blood proteins among the module members, notably S100A8, S100A9, and LYZ, while other effectors are intracellular or vesicular. The shared cervix and rectum signal may therefore reflect common myeloid-cell abundance, inflammatory infiltration, or blood exposure in the samples. Tissue protein detection is only partial in both tissues, and several canonical myeloid effectors are not detected by tissue immunohistochemistry, so the module should not be treated as evidence that every constituent protein is produced by the resident tissue cells.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP defense response to fungus | 0.00096 | CTSG, MPO, S100A8, S100A9 |
| GO:BP response to fungus | 0.00143 | CTSG, MPO, S100A8, S100A9 |
| GO:BP defense response to bacterium | 0.00814 | CTSG, LYZ, MPO, S100A8, S100A9 |
| KEGG Phagocytosis - Homo sapiens (human) | 0.0232 | CTSG, CYBB, LYZ, MPO, RAB5C |
| GO:BP respiratory burst | 0.0436 | CYBB, MPO, S100A9 |

### STRING and hu.MAP

STRING supports a biologically coherent antimicrobial network rather than a collection of unrelated genes. Known high-confidence relationships include the S100A8-S100A9 pair, CTSG-MPO, LYZ-MPO, CTSG-LYZ, CYBB-MPO, and CYBB-S100A9. The supplementary STRING results independently point to antimicrobial activity, bacterial and fungal defense, neutrophil degranulation, and NADPH-oxidase activation (8 supplementary STRING terms; within-query FDR 0.00051–0.0322), but these are supportive rather than globally corrected enrichment evidence. hu.MAP provides additional evidence that MPO and CTSG repeatedly occur in known myeloid granule or protease-associated complexes, and that MPO, CTSG, and LYZ occur together in a larger complex (hu.MAP huMAP3_11343.1) (hu.MAP huMAP3_03846.1) (hu.MAP huMAP3_13546.1) (hu.MAP huMAP3_10260.1). S100A8 and S100A9 also occur together in hu.MAP complexes (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1). By contrast, CYBB, RAB5C, H1-3, RPL6, and H4C1 lack hu.MAP support in this module, and H1-3, RPL6, and H4C1 lack STRING partner support here. Thus, the network contains a well-established antimicrobial core plus peripheral or composition-related genes whose co-abundance does not by itself establish physical interaction.

**STRING interactions (score >= 0.7)**: 6 of 45 gene pairs: CTSG–LYZ (0.836); CTSG–MPO (0.999); CYBB–MPO (0.767); CYBB–S100A9 (0.792); LYZ–MPO (0.918); S100A8–S100A9 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Antimicrobial (FDR = 0.00051, 4 genes); RCTM Antimicrobial peptides (FDR = 0.003, 4 genes); NetworkNeighborAL Mixed, incl. S100/CaBP-9k-type, calcium binding, subdomain, and Cystatin superfamily (FDR = 0.004, 5 genes); Process Defense response to bacterium (FDR = 0.0092, 5 genes); Process Defense response to fungus (FDR = 0.0092, 4 genes); RCTM Neutrophil degranulation (FDR = 0.0124, 7 genes); RCTM RHO GTPases Activate NADPH Oxidases (FDR = 0.0227, 3 genes); NetworkNeighborAL Mixed, incl. Neutrophil mediated cytotoxicity, and Mononeuritis multiplex (FDR = 0.0322, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11343.1 (MPO, CTSG, LYZ; 3/54); huMAP3_03846.1 (MPO, CTSG; 2/2); huMAP3_00649.1 (H1-3, RPL6; 2/2); huMAP3_13546.1 (MPO, CTSG; 2/8); huMAP3_10260.1 (MPO, CTSG; 2/14); huMAP3_09125.1 (S100A8, S100A9; 2/53); huMAP3_09929.1 (S100A8, S100A9; 2/75)

### Novelty

The module is unlikely to be a newly discovered molecular pathway because its central relationships and functions are already well established in STRING, hu.MAP, curated pathway annotations, and the literature. Its value may instead be contextual: it identifies a conserved cervix-rectum co-abundance pattern and shows that the same tissues share a myeloid antimicrobial signature. The specific tissue-pair module organization, including the association of the established antimicrobial core with RAB5C and histone or ribosomal genes, could be a dataset-specific observation, but it cannot be called a new biological mechanism from these data alone. Absence of support for some peripheral pairs in STRING or hu.MAP is evidence of limited prior interaction annotation, not proof of novelty.

**Hypothesis.** Hypothesis: the conserved module reflects variation in the abundance or activation state of infiltrating monocytes and neutrophil-lineage cells shared by cervix and rectum. In this model, S100A8 and S100A9 mark and potentially amplify inflammatory myeloid activity; LYZ, CTSG, and MPO provide antimicrobial and granule functions; CYBB supplies phagocyte oxidant-generating capacity; and RAB5C contributes endosomal trafficking during phagocytosis. The histone and ribosomal signals may arise from the abundance, maturation, or stress state of the same hematopoietic populations. This hypothesis should be tested with cell-deconvolution or single-cell data, matched blood-contamination measures, and protein or spatial assays; co-abundance alone does not establish activation, direct regulation, or physical interaction.

### Important genes

#### MPO

- **Related proteins** (co-abundance neighbors): LYZ (0.87), CTSG (0.82); STRING partners: CTSG (0.999), CYBB (0.767), LYZ (0.918)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11343.1, huMAP3_03846.1, huMAP3_13546.1, huMAP3_10260.1
- **Function (MyGene.info)**: myeloperoxidase. Myeloperoxidase (MPO) is a heme protein synthesized during myeloid differentiation that constitutes the major component of neutrophil azurophilic granules. Produced as a single chain precursor, myeloperoxidase is subsequently cleaved into a light and heavy chain. The mature myeloperoxidase is a tetramer composed of 2 light chains and 2 heavy chains. This enzyme produces hypohalous acids central to…
- **Diseases (Open Targets)**: myeloperoxidase deficiency (0.767); Alzheimer disease type 1 (0.485); multiple system atrophy (0.286); amyotrophic lateral sclerosis (0.242); Alzheimer disease (0.146)
- **Europe PMC papers**: 36383
- **Why important**: MPO is central to the module's primary evidence: it appears in every globally significant GO or KEGG term (5 globally significant GO/KEGG terms, q_global 0.00096–0.0436; see the table). It occupies the established antimicrobial core with CTSG and LYZ in STRING and multiple hu.MAP complexes (hu.MAP huMAP3_11343.1) (hu.MAP huMAP3_03846.1) (hu.MAP huMAP3_13546.1) (hu.MAP huMAP3_10260.1). HPA places it in bone marrow and monocyte or neutrophil progenitor populations, while its known role is production of microbicidal hypohalous acids in myeloid granules. It is extensively studied and has disease relevance including MPO deficiency and neurodegenerative disorders.
- **Conclusion**: Established evidence supports MPO as a defining myeloid granule and antimicrobial effector of this module. The module does not establish that MPO is enzymatically active in either tissue, but its co-abundance strongly supports a shared myeloid-effector interpretation.

#### S100A8

- **Related proteins** (co-abundance neighbors): S100A9 (0.96), LYZ (0.87), H1-3 (0.82); STRING partners: S100A9 (0.999)
- **HPA**: Tissue enhanced; Group enriched; blood Group enriched; location Intermediate filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: S100 calcium binding protein A8. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: inborn error of immunity (0.371); Sepsis (0.122); neoplasm (0.119); breast carcinoma (0.119); gastric cancer (0.119)
- **Europe PMC papers**: 18104
- **Why important**: S100A8 is among the most connected genes in the module and links the S100A8-S100A9 pair with LYZ and H1-3. It contributes to the fungal and bacterial defense terms (GO:BP defense response to fungus; q_global = 0.00096) (GO:BP response to fungus; q_global = 0.00143) (GO:BP defense response to bacterium; q_global = 0.00814) and to the supplementary antimicrobial, inflammatory, and neutrophil-related terms (7 supplementary STRING terms; within-query FDR 0.00051–0.0227). HPA associates it with bone marrow, classical monocytes, and neutrophils, and identifies it as secreted to blood. Its inflammatory biology, immune-disease associations, and extensive literature make it a strong marker of inflammatory myeloid abundance or state.
- **Conclusion**: Established evidence supports S100A8 as both a cellular marker and a potentially active inflammatory mediator in the module. A tissue-specific causal role remains a hypothesis because the data cannot distinguish local production from circulating or infiltrating myeloid cells.

#### S100A9

- **Related proteins** (co-abundance neighbors): S100A8 (0.96), LYZ (0.84); STRING partners: CYBB (0.792), S100A8 (0.999)
- **HPA**: Group enriched; Cell type enriched; blood Group enriched; location Plasma membrane, Intermediate filaments, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: S100 calcium binding protein A9. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: inborn error of immunity (0.370); Sepsis (0.121); neoplasm (0.119); psoriasis (0.114); cancer (0.114)
- **Europe PMC papers**: 16393
- **Why important**: S100A9 forms the strongest paired relationship with S100A8 in STRING and is connected to LYZ and CYBB. It appears in the fungal and bacterial defense terms and in respiratory burst (4 globally significant GO/KEGG terms, q_global 0.00096–0.0436; see the table), as well as the supplementary antimicrobial and NADPH-oxidase-related terms (7 supplementary STRING terms; within-query FDR 0.00051–0.0227). HPA links it to classical monocytes and neutrophils and to bone marrow and cervix-associated expression, with secretion to blood. It has extensive literature and disease associations involving immunity, sepsis, psoriasis, and cancer.
- **Conclusion**: Established evidence supports S100A9 as a prominent inflammatory myeloid component and a plausible readout of cell recruitment or activation. The module alone does not demonstrate that S100A9 drives the shared tissue phenotype rather than marking it.

#### LYZ

- **Related proteins** (co-abundance neighbors): S100A8 (0.87), MPO (0.87), S100A9 (0.84); STRING partners: CTSG (0.836), MPO (0.918)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Golgi apparatus, Actin filaments; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_11343.1
- **Function (MyGene.info)**: lysozyme. This gene encodes human lysozyme, whose natural substrate is the bacterial cell wall peptidoglycan (cleaving the beta[1-4]glycosidic linkages between N-acetylmuramic acid and N-acetylglucosamine). Lysozyme is one of the antimicrobial agents found in human milk, and is also present in spleen, lung, kidney, white blood cells, plasma, saliva, and tears. The protein has antibacterial activity against …
- **Diseases (Open Targets)**: familial visceral amyloidosis (0.619); amyloidosis, hereditary systemic 5 (0.550); Oral ulcer (0.483); AL amyloidosis (0.466); Renal amyloidosis (0.466)
- **Europe PMC papers**: 7506
- **Why important**: LYZ is a central connector among S100A8, S100A9, and MPO and contributes to bacterial defense and phagocytosis (GO:BP defense response to bacterium; q_global = 0.00814) (KEGG Phagocytosis - Homo sapiens (human); q_global = 0.0232). It is supported by STRING interactions with CTSG and MPO, appears in the hu.MAP complex containing MPO and CTSG (hu.MAP huMAP3_11343.1), and is linked by HPA to bone marrow, monocyte progenitors, classical monocytes, and myeloid dendritic cells. Its established enzymatic cleavage of bacterial cell-wall peptidoglycan gives a direct mechanistic basis for the antimicrobial interpretation, and it has substantial literature and disease associations including systemic amyloidosis.
- **Conclusion**: Established evidence supports LYZ as a secreted or granule-associated antibacterial effector and a marker of myeloid-cell content. Its presence does not by itself prove active bacterial infection in cervix or rectum.

#### CYBB

- **Related proteins** (co-abundance neighbors): CTSG (0.84); STRING partners: MPO (0.767), S100A9 (0.792)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome b-245 beta chain. Cytochrome b (-245) is composed of cytochrome b alpha (CYBA) and beta (CYBB) chain. It has been proposed as a primary component of the microbicidal oxidase system of phagocytes. CYBB deficiency is one of five described biochemical defects associated with chronic granulomatous disease (CGD). In this disorder, there is decreased activity of phagocyte NADPH oxidase; neutrophils are able to phagocytiz…
- **Diseases (Open Targets)**: chronic granulomatous disease (0.864); neurodegenerative disease (0.352); hereditary disease (0.191); discoid lupus erythematosus (0.185); Kartagener Syndrome (0.118)
- **Europe PMC papers**: 6704
- **Why important**: CYBB provides the clearest link to phagocyte oxidant production: it contributes to phagocytosis and respiratory burst (KEGG Phagocytosis - Homo sapiens (human); q_global = 0.0232) (GO:BP respiratory burst; q_global = 0.0436) and is connected in STRING to MPO and S100A9. HPA associates it with bone marrow, lymphoid tissue, macrophages, Kupffer cells, microglia, monocyte progenitors, and classical monocytes. Its established role in the phagocyte NADPH oxidase system and its association with chronic granulomatous disease give it strong mechanistic and clinical importance, despite its more peripheral position in the co-abundance graph.
- **Conclusion**: Established evidence supports CYBB as a functional phagocyte-effector component that complements the granule proteins. The module suggests coordinated presence of oxidant-capable myeloid cells, but does not prove that respiratory burst is occurring in the sampled tissues.
