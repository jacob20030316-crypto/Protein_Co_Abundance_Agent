# Conserved co-abundance modules: bone_marrow and circulatory_system

## Module 0

**Tissue pair**: bone_marrow and circulatory_system  
**Genes (38)**: AFTPH, GFER, C2CD5, ELMOD2, FGFR1OP2, GALM, MCM3AP, HACD3, HNRNPF, BPNT2, MIER1, MIOS, MYH10, NAA10, NDUFS7, NF1, PDLIM2, PHF8, NAPRT, CTPS2, CHM, RCC1L, RCOR1, RCOR3, RFXAP, RNASEH2C, GFM2, SLC25A42, SAP30BP, SCRN3, SMARCE1, QTRT1, TRIM24, TMEM209, TOMM40L, FTSJ1, TSPAN31, UIMC1

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established pathway-level function from those analyses. Its organization instead suggests a mixed cellular program. TSPAN31 is the principal co-abundance hub and connects genes involved in membrane trafficking, nucleotide metabolism, chromatin regulation, mitochondrial activity, and cytoskeletal function. A more coherent substructure is formed by RCOR1 and RCOR3, which are linked by STRING and recur together in multiple hu.MAP complexes; these genes support a transcriptional corepressor and chromatin-regulatory component. A separate mitochondrial branch includes NDUFS7 and GFM2, while RFXAP contributes a plausible immune-transcriptional context through regulation of MHC class II transcription. These interpretations are hypothesis-generating rather than globally enriched functional assignments. The supplementary STRING ELM2-domain signal (STRING SMART The ELM2 (Egl-27 and MTA1 homology 2) domain is a small domain of unknown function. It is found in the MTA1 protein that is part of the NuRD complex PUBMED:10226007. The domain is usually found to the N terminus of a myb-like DNA binding domain SANT ...; within-query FDR = 0.0375) is consistent with the RCOR1–RCOR3–MIER1 chromatin-related substructure but is not global enrichment evidence.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only a small subset is annotated as secreted, with GFER being the clearest example. Most genes have low tissue specificity, and many are intracellular or nuclear rather than extracellular. HPA indicates broad protein detection in bone marrow for much of the module, while there is no matching HPA tissue assessment for the circulatory-system label. Blood-cell specificity is generally low, although selected genes show enhancement in neutrophils, neutrophil progenitors, platelets, megakaryocytes, or lymphocyte populations. This pattern is more compatible with broadly expressed cellular machinery, mixed marrow cell composition, or shared cell states than with a specialized circulating plasma-protein program. The presence of genes enhanced in non-blood cell types, including muscle, liver, epithelial, and reproductive cell types, further argues against assigning the module exclusively to one blood lineage.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

Known physical or functional relationships are limited within the module. STRING reports RCOR1–RCOR3 and RCOR1–SMARCE1 as high-confidence relationships, plus FGFR1OP2–TRIM24; these links provide direct support for a chromatin-regulatory connection and a smaller signaling or regulatory connection, but most module pairs are not represented by high-confidence STRING edges. hu.MAP repeatedly places RCOR1 and RCOR3 together in several corepressor and chromatin-remodeling complexes (hu.MAP huMAP3_09692.1) (hu.MAP huMAP3_10258.1) (hu.MAP huMAP3_09232.1) (hu.MAP huMAP3_10311.1) (hu.MAP huMAP3_08800.1) (hu.MAP huMAP3_09031.1) (hu.MAP huMAP3_15128.1), although the module contains only a small subset of the members of each large complex. NDUFS7 and GFM2 co-occur in a hu.MAP mitochondrial translation or respiratory-function complex (hu.MAP huMAP3_13468.1). Thus, the network contains recognizable molecular substructures, but it is not itself a complete known protein complex. The sparse STRING connectivity and partial hu.MAP membership favor interpreting the module as a co-abundance association that combines several cellular programs rather than as one established physical complex.

**STRING interactions (score >= 0.7)**: 3 of 703 gene pairs: FGFR1OP2–TRIM24 (0.707); RCOR1–RCOR3 (0.796); RCOR1–SMARCE1 (0.775)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART The ELM2 (Egl-27 and MTA1 homology 2) domain is a small domain of unknown function. It is found in the MTA1 protein that is part of the NuRD complex PUBMED:10226007. The domain is usually found to the N terminus of a myb-like DNA binding domain SANT ... (FDR = 0.0375, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09692.1 (RCOR3, RCOR1; 2/6); huMAP3_10258.1 (RCOR3, RCOR1; 2/19); huMAP3_09232.1 (RCOR3, RCOR1; 2/27); huMAP3_10311.1 (RCOR3, RCOR1; 2/32); huMAP3_08800.1 (RCOR3, RCOR1; 2/48); huMAP3_09031.1 (RCOR3, RCOR1; 2/49); huMAP3_15128.1 (RCOR3, RCOR1; 2/96); huMAP3_13468.1 (NDUFS7, GFM2; 2/99)

### Novelty

The shared co-abundance pattern may be a new observation, but the evidence does not establish a completely new biological mechanism. RCOR1–RCOR3, RCOR1–SMARCE1, the RCOR-containing corepressor complexes, and the NDUFS7–GFM2 complex context are already represented in established resources. Conversely, most module genes have no reported STRING or hu.MAP relationship within this module, which may indicate a novel tissue-level co-abundance arrangement, indirect regulation, shared cell composition, or technical and sampling effects. Absence from those resources is not proof of novelty. The most defensible conclusion is that the module is potentially novel as a cross-tissue co-abundance pattern, while its component functions and several internal relationships are already known.

**Hypothesis.** Hypothesis: the module reflects a shared marrow–circulatory cellular state in which broadly expressed structural and trafficking machinery is co-regulated with chromatin-mediated transcriptional control and mitochondrial maintenance. TSPAN31 may mark or help organize the dominant cellular state, while the RCOR1–RCOR3 corepressor axis could influence lineage or activation-related transcription, including programs relevant to hematopoietic cells. In parallel, NDUFS7 and GFM2 may represent mitochondrial respiratory and translation requirements of the same cells. RFXAP, UIMC1, and selected HPA blood-cell annotations raise the possibility that immune or myeloid composition contributes to the signal, but this is not established by enrichment. This hypothesis should be tested with cell-type-resolved expression, independent cohorts, perturbation of the RCOR1–RCOR3 axis, and validation of whether the co-abundance pattern persists after controlling for cellular composition.

### Important genes

#### TSPAN31

- **Related proteins** (co-abundance neighbors): MCM3AP (1.00), C2CD5 (0.98), CTPS2 (0.95), AFTPH (0.94), RNASEH2C (0.92), PHF8 (0.91), MYH10 (0.86), GFER (0.86), QTRT1 (0.85), MIOS (0.85), NDUFS7 (0.83), HACD3 (0.82), SAP30BP (0.82), NAA10 (0.82), SMARCE1 (0.81), NAPRT (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tetraspanin 31. The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. This encoded protein is thou…
- **Diseases (Open Targets)**: gastric cancer (0.356); neurodegenerative disease (0.344); familial melanoma (0.208); hereditary neoplastic syndrome (0.208); melanoma, cutaneous malignant, susceptibility to, 3 (0.208)
- **Europe PMC papers**: 849
- **Why important**: TSPAN31 is the central network hub, with the greatest connectivity and weighted network strength in the module. It is a broadly expressed tetraspanin-family membrane protein associated with cell-surface signaling, development, growth, and motility. Its hub position makes it important for interpreting the module, although it has no STRING or hu.MAP support here and no globally corrected GO/KEGG assignment. Its disease and cancer associations and substantial literature volume make it biologically notable, but they do not prove that it drives this module.
- **Conclusion**: Established evidence supports TSPAN31 as the network-organizing hub and as a membrane-associated signaling protein. It is a plausible marker of the shared cellular state, but whether it is mechanistically causal or merely tracks the dominant cell population remains a hypothesis.

#### RCOR1

- **Related proteins** (co-abundance neighbors): RCOR3 (0.83); STRING partners: RCOR3 (0.796), SMARCE1 (0.775)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_09692.1, huMAP3_10258.1, huMAP3_09232.1, huMAP3_10311.1, huMAP3_08800.1, huMAP3_09031.1, huMAP3_15128.1
- **Function (MyGene.info)**: REST corepressor 1. This gene encodes a protein that is well-conserved, downregulated at birth, and with a specific role in determining neural cell differentiation. The encoded protein binds to the C-terminal domain of REST (repressor element-1 silencing transcription factor). [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: secondary malignant neoplasm (0.269); adrenal gland hyperfunction (0.265); hyperaldosteronism (0.265); venous thromboembolism (0.259); Joubert syndrome (0.259)
- **Europe PMC papers**: 952
- **Why important**: RCOR1 is one of the clearest molecular anchors of the module. It has a STRING relationship with RCOR3 and SMARCE1, appears with RCOR3 in multiple hu.MAP corepressor and chromatin-remodeling complexes (hu.MAP huMAP3_09692.1) (hu.MAP huMAP3_10258.1) (hu.MAP huMAP3_09232.1) (hu.MAP huMAP3_10311.1) (hu.MAP huMAP3_08800.1) (hu.MAP huMAP3_09031.1) (hu.MAP huMAP3_15128.1), and is linked to transcriptional repression, erythrocyte differentiation, and megakaryocyte differentiation in the supplied annotations. HPA also places it in neutrophils and neutrophil progenitors, which is relevant to the marrow context. Its substantial literature volume and disease associations provide strong prior biological support.
- **Conclusion**: Established evidence supports RCOR1 as a transcriptional coregulator with known chromatin-complex relationships and relevance to hematopoietic differentiation. Its participation in this co-abundance module may reflect a genuine regulatory submodule, but the module does not establish a new RCOR1 target program.

#### RCOR3

- **Related proteins** (co-abundance neighbors): BPNT2 (0.91), UIMC1 (0.88), SCRN3 (0.87), GFM2 (0.86), MIER1 (0.85), RCOR1 (0.83); STRING partners: RCOR1 (0.796)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_09692.1, huMAP3_10258.1, huMAP3_09232.1, huMAP3_10311.1, huMAP3_08800.1, huMAP3_09031.1, huMAP3_15128.1
- **Function (MyGene.info)**: REST corepressor 3. Predicted to enable enzyme binding activity and transcription corepressor activity. Predicted to be involved in histone deacetylation; negative regulation of transcription, DNA-templated; and regulation of transcription by RNA polymerase II. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: smoking initiation (0.233); skin disorder (0.188); neurodegenerative disease (0.184); polyarteritis nodosa (0.072); ovarian neoplasm (0.067)
- **Europe PMC papers**: 231
- **Why important**: RCOR3 forms the strongest coherent partner relationship with RCOR1 in the module and is present with RCOR1 across several hu.MAP complexes (hu.MAP huMAP3_09692.1) (hu.MAP huMAP3_10258.1) (hu.MAP huMAP3_09232.1) (hu.MAP huMAP3_10311.1) (hu.MAP huMAP3_08800.1) (hu.MAP huMAP3_09031.1) (hu.MAP huMAP3_15128.1). Its annotation supports transcriptional corepressor activity, histone deacetylation, and negative regulation of transcription. It also contributes to the supplementary STRING ELM2-domain signal (STRING SMART The ELM2 (Egl-27 and MTA1 homology 2) domain is a small domain of unknown function. It is found in the MTA1 protein that is part of the NuRD complex PUBMED:10226007. The domain is usually found to the N terminus of a myb-like DNA binding domain SANT ...; within-query FDR = 0.0375) with RCOR1 and MIER1. Its network position is more connected than most genes, and its nucleoplasmic localization fits the inferred chromatin-regulatory substructure.
- **Conclusion**: Established evidence supports RCOR3 as part of a known transcriptional corepressor context shared with RCOR1. Its co-abundance with RCOR1 is biologically plausible, but the specific role of RCOR3 in the cross-tissue module remains inferential.

#### NDUFS7

- **Related proteins** (co-abundance neighbors): SLC25A42 (0.84), TSPAN31 (0.83), FTSJ1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S7. This gene encodes a protein that is a subunit of one of the complexes that forms the mitochondrial respiratory chain. This protein is one of over 40 subunits found in complex I, the nicotinamide adenine dinucleotide (NADH):ubiquinone oxidoreductase. This complex functions in the transfer of electrons from NADH to the respiratory chain, and ubiquinone is believed to be the immediate electron accept…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.765); mitochondrial complex I deficiency, nuclear type 3 (0.699); Leigh syndrome (0.691); mitochondrial disease (0.609); type 2 diabetes mellitus (0.608)
- **Europe PMC papers**: 1206
- **Why important**: NDUFS7 connects the module to mitochondrial respiratory-chain complex I and is annotated for electron transport, aerobic respiration, proton transport, and complex I assembly. It is also paired with GFM2 in hu.MAP complex (hu.MAP huMAP3_13468.1), providing complex-level support for a mitochondrial component. Its tissue enhancement in skeletal muscle and disease associations with mitochondrial complex I deficiency and Leigh syndrome make it an informative indicator of energetic and respiratory biology, despite its limited local connectivity.
- **Conclusion**: Established evidence supports NDUFS7 as a mitochondrial complex I component and supports a mitochondrial branch within the module. It is not evidence that the entire module is a mitochondrial pathway; the broader interpretation remains a hypothesis about shared cellular energy demand.

#### UIMC1

- **Related proteins** (co-abundance neighbors): RCOR3 (0.88), PDLIM2 (0.83), FGFR1OP2 (0.82), NF1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nuclear bodies; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin interaction motif containing 1. This gene encodes a nuclear protein that interacts with Brca1 (breast cancer 1) in a complex to recognize and repair DNA lesions. This protein binds ubiquitinated lysine 63 of histone H2A and H2AX. This protein may also function as a repressor of transcription. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: menopause (0.283); insomnia (0.236); uterine corpus leiomyoma (0.216); jaw disease (0.187); pituitary gland disorder (0.143)
- **Europe PMC papers**: 404
- **Why important**: UIMC1 occupies a bridge-like position between RCOR3, PDLIM2, FGFR1OP2, and NF1 in the co-abundance graph. Its established annotation concerns recognition of ubiquitinated histone lesions, DNA repair, and DNA-damage checkpoints. HPA specifically reports enhancement in neutrophils and platelets, making it relevant to the hematopoietic and circulatory comparison. It has no STRING or hu.MAP relationship in the supplied evidence, so its importance comes primarily from network position and cell-type context rather than established complex membership.
- **Conclusion**: Established evidence supports UIMC1 as a DNA-repair and nuclear surveillance protein with enrichment in selected blood-associated cell types. Its connection to the chromatin branch and blood-cell context is plausible, but a direct mechanistic link to RCOR3 or to the module-level phenotype is unproven.

#### RFXAP

- **Related proteins** (co-abundance neighbors): CTPS2 (0.88), TOMM40L (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: regulatory factor X associated protein. Major histocompatibility (MHC) class II molecules are transmembrane proteins that have a central role in development and control of the immune system. The protein encoded by this gene, along with regulatory factor X-associated ankyrin-containing protein and regulatory factor-5, forms a complex that binds to the X box motif of certain MHC class II gene promoters and activates their transcription. O…
- **Diseases (Open Targets)**: MHC class II deficiency (0.738); MHC class II deficiency 4 (0.527); neurodegenerative disease (0.274); oral mucosa leukoplakia (0.158); pancreatic ductal adenocarcinoma (0.076)
- **Europe PMC papers**: 692
- **Why important**: RFXAP provides a biologically relevant immune-transcriptional interpretation. It is a component of the regulatory factor X complex that activates MHC class II gene transcription and is associated with MHC class II deficiency. In the module it connects CTPS2 and TOMM40L, linking transcriptional regulation with nucleotide synthesis and mitochondrial import. Although HPA does not detect it in immune cells and it lacks STRING or hu.MAP support here, its function is directly relevant to potential immune-cell composition or activation effects.
- **Conclusion**: Established evidence supports RFXAP as an MHC class II transcriptional regulator. Its presence does not demonstrate that the module is an antigen-presentation module; it is better treated as a plausible immune-context marker whose module-level role requires cell-resolved validation.

## Module 1

**Tissue pair**: bone_marrow and circulatory_system  
**Genes (22)**: ASCC3, BABAM2, BAHD1, CWF19L1, CD79A, CDCA5, CNOT2, EIPR1, GALNT2, LUC7L2, LIN7C, LUC7L, MFF, NCF2, PALS2, PPHLN1, MRPS11, SREK1, GTF2E1, TIAL1, ZNF280C, ZBBX

### Function

No GO/KEGG term passed global correction, so the module does not support a single statistically established pathway-level function from enrichment. The gene-level evidence instead points to a composite program involving nuclear RNA processing and splicing, transcriptional and chromatin regulation, cell-cycle and DNA-damage processes, mitochondrial maintenance, and immune-cell functions. The strongest network hub is CDCA5, which connects genes associated with cell-cycle control, DNA repair, RNA regulation, and several lineage-related signals. The presence of NCF2 and CD79A adds specific neutrophil and B-cell biology, respectively, whereas LUC7L, LUC7L2, and SREK1 support an RNA-splicing component. Thus, the most cautious interpretation is a co-abundance module reflecting shared cellular composition and coordinated regulation in hematopoietic samples rather than a single coherent molecular pathway.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: HPA identifies only one secreted gene, while most genes are intracellular and many are nuclear. Most genes have low tissue specificity and low immune-cell specificity, consistent with broadly expressed housekeeping or regulatory functions. Nevertheless, several genes show enrichment in bone marrow, lymphoid tissue, B-cell populations, NK cells, T-reg cells, neutrophils, eosinophils, or megakaryocytes. CD79A is associated with B cells and plasma cells, and NCF2 with neutrophils and eosinophils. HPA detects protein for most annotated genes in bone marrow, but there is no matching HPA tissue entry for the circulatory-system comparison. The module may therefore partly reflect hematopoietic cell mixtures or shared blood-related cell types, superimposed on broadly expressed intracellular machinery. Testis and spermatogenic enrichment also occurs for several genes, so some tissue associations may reflect shared proliferative or RNA-processing programs rather than a blood-specific mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only two high-confidence relationships within the module: LIN7C with PALS2 and LUC7L with LUC7L2. These are established pairwise connections, but STRING reports no functional enrichment for the module. The hu.MAP evidence is more informative for partial complex membership. SREK1, LUC7L, and LUC7L2 recur in a large set of spliceosome- and RNA-processing-related complexes, including (hu.MAP huMAP3_11073.1), (hu.MAP huMAP3_05807.1), (hu.MAP huMAP3_09621.1), and (hu.MAP huMAP3_09943.1). LIN7C and PALS2 recur together in several membrane-polarity and MAGUK-associated complexes, including (hu.MAP huMAP3_08198.1) through (hu.MAP huMAP3_14575.1). MRPS11 appears with SREK1 and LUC7L in (hu.MAP huMAP3_05807.1). These observations show that parts of the module overlap known molecular systems, especially RNA splicing and cell-junction or polarity scaffolds, but the module as a whole is not represented as one known complex. The sparse STRING connectivity and partial hu.MAP overlap argue against interpreting every co-abundance edge as a direct physical interaction.

**STRING interactions (score >= 0.7)**: 2 of 231 gene pairs: LIN7C–PALS2 (0.924); LUC7L–LUC7L2 (0.935)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11073.1 (SREK1, LUC7L, LUC7L2; 3/67); huMAP3_05807.1 (MRPS11, SREK1, LUC7L; 3/81); huMAP3_08198.1 (LIN7C, PALS2; 2/15); huMAP3_11195.1 (LIN7C, PALS2; 2/19); huMAP3_08481.1 (LIN7C, PALS2; 2/21); huMAP3_09519.1 (LIN7C, PALS2; 2/23); huMAP3_14575.1 (LIN7C, PALS2; 2/31); huMAP3_09621.1 (SREK1, LUC7L2; 2/56); huMAP3_09943.1 (SREK1, LUC7L2; 2/78)

### Novelty

This module may be a new tissue-pair co-abundance pattern, but the available evidence does not establish it as a newly discovered molecular complex or pathway. Its novelty is supported by the lack of a single globally significant GO/KEGG annotation, the absence of STRING functional enrichment, and the fact that known hu.MAP complexes account for only subsets of the genes. However, several relationships are already known, including the LIN7C–PALS2 interaction, the LUC7L–LUC7L2 interaction, and repeated membership of splicing and polarity complexes. Therefore, absence from STRING or hu.MAP alone cannot prove novelty. The defensible claim is that the cross-tissue co-abundance assembly appears distinctive, while its underlying biology is likely a mixture of known processes and sample-composition effects that requires replication and perturbation testing.

**Hypothesis.** Hypothesis: the shared module reflects coordinated abundance of hematopoietic cells together with a conserved intracellular maintenance program. In this model, proliferative or progenitor-associated cells contribute CDCA5 and related DNA-repair and cell-cycle signals; B-cell and myeloid populations contribute CD79A and NCF2; and broadly expressed RNA-processing factors contribute LUC7L, LUC7L2, and SREK1. The co-abundance pattern could therefore arise because related bone-marrow and circulating cell populations share transcriptional, splicing, and stress-response states, rather than because all module genes operate in one physical complex. A secondary mechanistic possibility is that RNA-processing and chromatin-regulatory activity helps coordinate lineage-specific programs in these cells. This hypothesis should be tested by cell-resolved expression, sorting or deconvolution, and perturbation of candidate regulatory genes.

### Important genes

#### CDCA5

- **Related proteins** (co-abundance neighbors): TIAL1 (0.91), BABAM2 (0.88), CNOT2 (0.85), PPHLN1 (0.84), GTF2E1 (0.83), LIN7C (0.82), SREK1 (0.81), MFF (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell division cycle associated 5. Predicted to enable chromatin binding activity. Involved in double-strand break repair; mitotic sister chromatid segregation; and regulation of cell cycle process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.306); hepatocellular carcinoma (0.121); breast cancer (0.113); neoplasm (0.112); breast carcinoma (0.111)
- **Europe PMC papers**: 1491
- **Why important**: CDCA5 is the central network hub and links genes involved in RNA regulation, transcriptional control, mitochondrial organization, and cell-cycle or DNA-damage biology. HPA associates it with bone marrow, lymphoid tissue, erythrocyte progenitors, NK cells, and T-reg cells. Its annotated functions include sister-chromatid cohesion and double-strand break repair, and it has a substantial literature and disease-association record involving cancer and neurodegenerative disease.
- **Conclusion**: Established evidence supports CDCA5 as the principal network-organizing marker of a proliferative or genome-maintenance component. It is a plausible biological driver of part of the module, but the co-abundance data do not demonstrate that CDCA5 regulates the other genes directly.

#### NCF2

- **Related proteins** (co-abundance neighbors): BAHD1 (0.99); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enhanced; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neutrophil cytosolic factor 2. This gene encodes neutrophil cytosolic factor 2, the 67-kilodalton cytosolic subunit of the multi-protein NADPH oxidase complex found in neutrophils. This oxidase produces a burst of superoxide which is delivered to the lumen of the neutrophil phagosome. Mutations in this gene, as well as in other NADPH oxidase subunits, can result in chronic granulomatous disease, a disease that causes recurrent …
- **Diseases (Open Targets)**: chronic granulomatous disease (0.734); systemic lupus erythematosus (0.548); celiac disease (0.525); rheumatoid arthritis (0.442); autoimmune disorder of musculoskeletal system (0.434)
- **Europe PMC papers**: 2695
- **Why important**: NCF2 is a lineage-informative terminal node connected to BAHD1 and is strongly associated with bone marrow, lymphoid tissue, neutrophils, and eosinophils in HPA. It is a component of the neutrophil NADPH oxidase system and is annotated for respiratory burst, superoxide generation, phagocytosis, and innate immune defense. It has extensive literature and established disease relevance through chronic granulomatous disease and inflammatory disorders.
- **Conclusion**: Established evidence supports NCF2 as evidence that myeloid-cell composition or innate immune activity contributes to the module. It should not be used alone to infer that the entire module is an oxidative-burst pathway, because the global enrichment analysis is negative and NCF2 has limited direct network connectivity here.

#### CD79A

- **Related proteins** (co-abundance neighbors): ZNF280C (0.86); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Group enriched; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD79a molecule. The B lymphocyte antigen receptor is a multimeric complex that includes the antigen-specific component, surface immunoglobulin (Ig). Surface Ig non-covalently associates with two other proteins, Ig-alpha and Ig-beta, which are necessary for expression and function of the B-cell antigen receptor. This gene encodes the Ig-alpha protein of the B-cell antigen component. Alternatively spliced transcrip…
- **Diseases (Open Targets)**: isolated agammaglobulinemia (0.663); agammaglobulinemia (0.472); autosomal agammaglobulinemia (0.470); diffuse large B-cell lymphoma (0.376); colorectal adenocarcinoma (0.372)
- **Europe PMC papers**: 13538
- **Why important**: CD79A is a B-cell-specific marker within the module and connects to ZNF280C. HPA associates it with lymphoid tissue, B cells, plasma cells, and both naive and memory B-cell populations. Its established role is as a signaling component of the B-cell antigen receptor, with functions in B-cell activation, differentiation, and proliferation. It has a very substantial literature and disease relevance in agammaglobulinemia and B-cell malignancy.
- **Conclusion**: Established evidence supports CD79A as a strong indicator of B-cell contribution to the shared module. The module may therefore partly reflect variation in B-cell abundance or state; the data do not show that CD79A mechanistically controls the broadly expressed nuclear genes.

#### LUC7L2

- **Related proteins** (co-abundance neighbors): ZNF280C (0.85); STRING partners: LUC7L (0.935)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_11073.1, huMAP3_09621.1, huMAP3_09943.1
- **Function (MyGene.info)**: LUC7 like 2, pre-mRNA splicing factor. This gene encodes a protein that contains a C2H2-type zinc finger, coiled-coil region and arginine, serine-rich (RS) domain. A similar protein in mouse interacts with sodium channel modifier 1, and the encoded protein may be involved in the recognition of non-consensus splice donor sites in association with the U1 snRNP spliceosomal subunit. Alternatively spliced transcript variants encoding multi…
- **Diseases (Open Targets)**: Usher syndrome (0.266); chronic venous hypertension (0.202); neurodegenerative disease (0.182); nasopharyngeal carcinoma (0.074); acute myeloid leukemia (0.049)
- **Europe PMC papers**: 562
- **Why important**: LUC7L2 is part of the recurring hu.MAP splicing complexes (hu.MAP huMAP3_11073.1), (hu.MAP huMAP3_09621.1), and (hu.MAP huMAP3_09943.1), and it has a high-confidence STRING relationship with LUC7L. Its annotation supports recognition of non-consensus splice sites, and HPA places it mainly in the nucleoplasm with low overall tissue specificity. Its network connectivity within this module is limited, but its repeated complex membership makes it a useful representative of the RNA-splicing component.
- **Conclusion**: Established evidence supports LUC7L2 as a marker of spliceosomal and RNA-processing machinery represented in the module. The module may coordinate alternative splicing in hematopoietic cells, but this remains a hypothesis because no globally significant GO/KEGG term or module-wide STRING enrichment supports it.

#### SREK1

- **Related proteins** (co-abundance neighbors): CDCA5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_11073.1, huMAP3_05807.1, huMAP3_09621.1, huMAP3_09943.1
- **Function (MyGene.info)**: splicing regulatory glutamic acid and lysine rich protein 1. This gene encodes a member of a family of serine/arginine-rich (SR) splicing proteins containing RNA recognition motif (RRM) domains. The encoded protein interacts with other SR proteins to modulate splice site selection. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jul 2012].
- **Diseases (Open Targets)**: neurodegenerative disease (0.530); lysosomal storage disease (0.361); alcohol drinking (0.347); tongue cancer (0.281); spondylolisthesis (0.244)
- **Europe PMC papers**: 197
- **Why important**: SREK1 connects to the central CDCA5 hub and recurs with LUC7L and LUC7L2 in hu.MAP complexes (hu.MAP huMAP3_11073.1), (hu.MAP huMAP3_05807.1), (hu.MAP huMAP3_09621.1), and (hu.MAP huMAP3_09943.1). It is an SR-family splicing regulator that interacts with other splicing factors to influence splice-site selection. HPA places it in nuclear speckles and detects it in bone marrow, making it a plausible bridge between the hematopoietic context and the RNA-processing component.
- **Conclusion**: Established evidence supports SREK1 as a connector between the module’s central co-abundance structure and known splicing machinery. Its possible role in coordinating lineage-associated transcript processing is a reasonable hypothesis, not an established function of this module.
