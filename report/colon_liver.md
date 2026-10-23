# Conserved co-abundance modules: colon and liver

## Module 0

**Tissue pair**: colon and liver  
**Genes (11)**: ABCF1, DDX46, DDX5, EIF3C, LUC7L2, NUP93, UPF1, RUVBL2, SF3A1, SRRT, XRN2

### Function

The module is strongly characterized as a nuclear RNA-processing and ribonucleoprotein module. The primary evidence is the enrichment of ribonucleoprotein complex (GO:CC ribonucleoprotein complex; q_global = 1.86e-05), mRNA processing (GO:BP mRNA processing; q_global = 8.13e-05), ribonucleoprotein complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.000314), mRNA metabolic process (GO:BP mRNA metabolic process; q_global = 0.000575), RNA processing (GO:BP RNA processing; q_global = 0.000815), protein-RNA complex assembly and organization (GO:BP protein-RNA complex assembly; q_global = 0.00094) (GO:BP protein-RNA complex organization; q_global = 0.0011), spliceosomal complex (GO:CC spliceosomal complex; q_global = 0.00175), RNA splicing (4 globally significant GO/KEGG terms, q_global 0.00672–0.0165; see the table), and spliceosomal complex assembly (GO:BP spliceosomal complex assembly; q_global = 0.0409). The module also shows global enrichment for RNA binding (GO:MF RNA binding; q_global = 0.00624), helicase activity (GO:MF helicase activity; q_global = 0.00507), ATP hydrolysis activity (GO:MF ATP hydrolysis activity; q_global = 0.0384), and nucleic acid binding (GO:MF nucleic acid binding; q_global = 0.00162). All genes contribute to the broad gene-expression annotation (GO:BP gene expression; q_global = 0.00421), but the more specific terms support RNA maturation, spliceosome function, ribonucleoprotein assembly, RNA surveillance, and related nuclear RNA metabolism. The pattern is coherent rather than dependent on a single annotation: DDX46, DDX5, LUC7L2, SF3A1, SRRT, UPF1, and XRN2 recur across RNA-processing terms, while EIF3C, RUVBL2, and ABCF1 add protein-RNA, ATPase, or translation-related context.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It is also not blood-cell enriched by the available HPA categories; nearly all genes have low immune-cell specificity, with one reported as not detected in immune cells. Most genes have low tissue specificity, and protein detection is broadly consistent with presence in colon and liver. This supports a broadly expressed intracellular housekeeping-like RNA-processing program rather than a tissue-specific secretory signal. Several genes show cell-type-enhanced annotations in germ cells or neural and glial populations, but those findings do not establish that such cells explain the colon-liver module. RUVBL2 is tissue-enhanced in testis and is not detected by HPA immunohistochemistry in colon or liver, so its contribution should be interpreted cautiously.

**GO/KEGG enrichment**: 24 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC ribonucleoprotein complex | 1.86e-05 | DDX46, DDX5, EIF3C, LUC7L2, RUVBL2, SF3A1, SRRT, UPF1 |
| GO:BP mRNA processing | 8.13e-05 | DDX46, DDX5, LUC7L2, SF3A1, SRRT, UPF1, XRN2 |
| GO:BP ribonucleoprotein complex biogenesis | 0.000314 | DDX46, EIF3C, LUC7L2, RUVBL2, SF3A1, XRN2 |
| GO:BP mRNA metabolic process | 0.000575 | DDX46, DDX5, LUC7L2, SF3A1, SRRT, UPF1, XRN2 |
| GO:BP RNA processing | 0.000815 | DDX46, DDX5, LUC7L2, SF3A1, SRRT, UPF1, XRN2 |
| GO:BP protein-RNA complex assembly | 0.00094 | DDX46, EIF3C, LUC7L2, RUVBL2, SF3A1 |
| GO:BP protein-RNA complex organization | 0.0011 | DDX46, EIF3C, LUC7L2, RUVBL2, SF3A1 |
| GO:CC nuclear protein-containing complex | 0.00149 | DDX46, DDX5, LUC7L2, NUP93, RUVBL2, SF3A1, UPF1 |
| GO:MF nucleic acid binding | 0.00162 | ABCF1, DDX46, DDX5, EIF3C, LUC7L2, RUVBL2, SF3A1, SRRT, UPF1, XRN2 |
| GO:CC spliceosomal complex | 0.00175 | DDX46, DDX5, LUC7L2, SF3A1, UPF1 |
| GO:BP gene expression | 0.00421 | ABCF1, DDX46, DDX5, EIF3C, LUC7L2, NUP93, RUVBL2, SF3A1, SRRT, UPF1, XRN2 |
| GO:MF helicase activity | 0.00507 | DDX46, DDX5, RUVBL2, UPF1 |
| GO:MF RNA binding | 0.00624 | ABCF1, DDX46, DDX5, EIF3C, LUC7L2, SF3A1, SRRT, UPF1, XRN2 |
| GO:BP RNA splicing, via transesterification reactions | 0.00672 | DDX46, DDX5, LUC7L2, SF3A1, UPF1 |
| GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile | 0.00672 | DDX46, DDX5, LUC7L2, SF3A1, UPF1 |

### STRING and hu.MAP

STRING supports a connected RNA-processing interpretation, but only selected relationships are already represented as high-confidence pairwise links. The strongest connections include DDX46 with SF3A1, DDX5 with SRRT, LUC7L2 with SF3A1, UPF1 with XRN2, and RUVBL2 with UPF1; DDX46 also links to LUC7L2. STRING functional categories independently point to ribonucleoprotein complexes, nuclear lumen, nucleoplasm, gene expression, mRNA metabolism, spliceosomal complexes, RNA metabolism, and helicase activity (15 supplementary STRING terms; within-query FDR 1.16e-07–0.00089). These STRING results are supplementary and do not replace the globally corrected GO evidence. hu.MAP provides additional complex-level context: SRRT and LUC7L2 co-occur in several splicing and RNA-processing complexes (hu.MAP huMAP3_09490.1) (hu.MAP huMAP3_09587.1) (hu.MAP huMAP3_10564.1) (hu.MAP huMAP3_09621.1) (hu.MAP huMAP3_11073.1) (hu.MAP huMAP3_09943.1), while SF3A1 and DDX46 co-occur in complexes related to spliceosomal and small nuclear ribonucleoprotein biology (hu.MAP huMAP3_04549.1) (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_08980.1). However, each hu.MAP complex contains many members outside the module, so the module is best viewed as a coordinated subset of larger established RNA-processing systems rather than a complete canonical complex.

**STRING interactions (score >= 0.7)**: 6 of 55 gene pairs: DDX46–LUC7L2 (0.74); DDX46–SF3A1 (0.999); DDX5–SRRT (0.855); LUC7L2–SF3A1 (0.835); RUVBL2–UPF1 (0.742); UPF1–XRN2 (0.812)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Ribonucleoprotein complex (FDR = 1.16e-07, 9 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 2.27e-06, 8 genes); COMPARTMENTS Nuclear lumen (FDR = 9.98e-06, 9 genes); COMPARTMENTS Nucleoplasm (FDR = 8.44e-05, 7 genes); Process Gene expression (FDR = 0.00014, 10 genes); Process mRNA metabolic process (FDR = 0.00014, 7 genes); COMPARTMENTS Spliceosomal complex (FDR = 0.00015, 5 genes); Component Nuclear protein-containing complex (FDR = 0.00015, 7 genes); Process Ribonucleoprotein complex biogenesis (FDR = 0.00032, 6 genes); Component Spliceosomal complex (FDR = 0.00034, 5 genes); COMPARTMENTS Nuclear body (FDR = 0.00039, 5 genes); Process mRNA processing (FDR = 0.0007, 6 genes); RCTM Metabolism of RNA (FDR = 0.00083, 7 genes); Function Nucleic acid binding (FDR = 0.00084, 10 genes); Keyword Helicase (FDR = 0.00089, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09490.1 (SRRT, LUC7L2; 2/9); huMAP3_09587.1 (SRRT, LUC7L2; 2/21); huMAP3_10564.1 (SRRT, LUC7L2; 2/37); huMAP3_04549.1 (SF3A1, DDX46; 2/52); huMAP3_09621.1 (SRRT, LUC7L2; 2/56); huMAP3_11073.1 (SRRT, LUC7L2; 2/67); huMAP3_09943.1 (SRRT, LUC7L2; 2/78); huMAP3_06511.1 (SF3A1, DDX46; 2/79); huMAP3_08980.1 (SF3A1, DDX46; 2/97)

### Novelty

The module should not be called a newly discovered molecular complex. Its central biology is well established through globally significant GO terms, STRING functional categories, known STRING pairwise relationships, and hu.MAP complexes. The co-abundance pattern may still be a new observation in the specific colon-liver comparison, especially because the module combines members from spliceosomal, RNA surveillance, nuclear transport, helicase, and translation-related systems. However, the available evidence does not establish that this particular gene grouping, its cross-tissue conservation, or its co-abundance organization has been reported previously. Absence of some genes from STRING or hu.MAP is not evidence of novelty; it may reflect incomplete interaction coverage, context dependence, or the fact that co-abundance is not equivalent to physical interaction. A cautious conclusion is that the conserved co-abundance module may be a potentially novel systems-level observation built from largely established RNA-processing machinery.

**Hypothesis.** Hypothesis: in colon and liver, this module reflects coordinated regulation of nuclear RNA maturation and quality control. A possible mechanism is that spliceosomal and splice-site recognition factors, represented by SF3A1 and LUC7L2, work with RNA helicases such as DDX46 and DDX5 to remodel or process precursor transcripts; SRRT may organize or connect RNA-effector activities; UPF1 and XRN2 may provide downstream RNA surveillance, degradation, export, or transcription-termination functions; and EIF3C, ABCF1, and RUVBL2 may connect RNA handling to translation or ATP-dependent remodeling. This is a mechanistic model consistent with the annotations and network, not a demonstrated physical pathway. Testing would require tissue-resolved perturbation, RNA-sequencing or isoform analysis, and direct interaction or co-complex experiments.

### Important genes

#### SRRT

- **Related proteins** (co-abundance neighbors): XRN2 (0.86), SF3A1 (0.83), LUC7L2 (0.82), DDX5 (0.82), EIF3C (0.82), RUVBL2 (0.80); STRING partners: DDX5 (0.855)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon, liver
- **hu.MAP 3.0**: huMAP3_09490.1, huMAP3_09587.1, huMAP3_10564.1, huMAP3_09621.1, huMAP3_11073.1, huMAP3_09943.1
- **Function (MyGene.info)**: serrate, RNA effector molecule. Enables mRNA cap binding complex binding activity and protein-macromolecule adaptor activity. Involved in primary miRNA processing. Located in nucleoplasm. Part of ribonucleoprotein complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dengue disease (0.370); myxedema (0.228); hypothyroidism (0.228); neurodegenerative disease (0.227); hair color (0.175)
- **Europe PMC papers**: 413
- **Why important**: SRRT has the strongest network centrality in the module and connects to several module branches, including XRN2, SF3A1, LUC7L2, DDX5, EIF3C, and RUVBL2. It is present in many globally significant RNA-processing and ribonucleoprotein terms (11 globally significant GO/KEGG terms, q_global 1.86e-05–0.0398; see the table). It is also repeatedly represented with LUC7L2 in hu.MAP splicing-related complexes (hu.MAP huMAP3_09490.1) (hu.MAP huMAP3_09587.1) (hu.MAP huMAP3_10564.1) (hu.MAP huMAP3_09621.1) (hu.MAP huMAP3_11073.1) (hu.MAP huMAP3_09943.1), and HPA places it in the nucleoplasm with detection in both tissues. Its literature base is substantial, while its annotations include RNA-effector and primary microRNA-processing functions.
- **Conclusion**: Established: SRRT is a central, nuclear, RNA-associated connector in this module and belongs to established splicing and RNA-effector systems. Hypothesis: its network position may allow it to coordinate spliceosomal or RNA-regulatory activities across the module, but co-abundance alone does not prove that it is the organizing scaffold.

#### DDX46

- **Related proteins** (co-abundance neighbors): UPF1 (0.82), LUC7L2 (0.82), ABCF1 (0.82); STRING partners: LUC7L2 (0.74), SF3A1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in colon, liver
- **hu.MAP 3.0**: huMAP3_04549.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: DEAD-box helicase 46. This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribu…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); dengue disease (0.370); Hypercholesterolemia (0.203); lung adenocarcinoma (0.074); osteosarcoma (0.053)
- **Europe PMC papers**: 592
- **Why important**: DDX46 is the most extensively annotated module member, appearing in every globally significant term listed in the fact sheet, including spliceosome assembly, mRNA processing, helicase activity, RNA binding, and ATP-dependent activities (24 globally significant GO/KEGG terms, q_global 1.86e-05–0.0409; see the table). It has high-confidence STRING links to SF3A1 and LUC7L2 and is included with SF3A1 in several hu.MAP spliceosomal complexes (hu.MAP huMAP3_04549.1) (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_08980.1). Its DEAD-box helicase function is directly relevant to RNA-structure remodeling, spliceosome assembly, and mRNA splicing. It is detected in both colon and liver and has a substantial literature base.
- **Conclusion**: Established: DDX46 is a strong molecular anchor for the module's spliceosomal and RNA-remodeling interpretation. Hypothesis: DDX46 may be a functional driver of the co-abundance program by coupling RNA helicase activity to spliceosome assembly, but the module does not demonstrate tissue-specific causality.

#### SF3A1

- **Related proteins** (co-abundance neighbors): SRRT (0.83); STRING partners: DDX46 (0.999), LUC7L2 (0.835)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in colon, liver
- **hu.MAP 3.0**: huMAP3_04549.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 is a core component of the SF3A complex and mature U2 small nuclear ribonucleoprotein, making it directly relevant to spliceosome assembly and pre-mRNA splicing. It contributes to many primary RNA-processing terms (21 globally significant GO/KEGG terms, q_global 1.86e-05–0.0409; see the table). Its STRING relationships with DDX46 and LUC7L2 are strong, and hu.MAP places it with DDX46 in spliceosomal complexes (hu.MAP huMAP3_04549.1) (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_08980.1). HPA detects it in both colon and liver, with nuclear or nuclear-speckle localization, and its literature base is substantial.
- **Conclusion**: Established: SF3A1 provides direct canonical spliceosomal support for the module interpretation. Hypothesis: it may represent the spliceosomal core that links the module's co-abundance to coordinated pre-mRNA processing, although this cannot be inferred as a physical module-specific assembly.

#### DDX5

- **Related proteins** (co-abundance neighbors): SRRT (0.82), NUP93 (0.80); STRING partners: SRRT (0.855)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in colon, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 is a well-studied DEAD-box RNA helicase and adaptor involved in RNA-structure remodeling, alternative splicing, transcriptional regulation, and small noncoding RNA processing. It appears across the primary mRNA-processing, splicing, helicase, RNA-binding, and ribonucleoprotein annotations (18 globally significant GO/KEGG terms, q_global 1.86e-05–0.0398; see the table). Its STRING relationship with SRRT is established, and HPA places it in the nucleoplasm and nucleoli with detection in both tissues. The gene has a large literature base and disease associations that include colon and colorectal adenocarcinoma annotations.
- **Conclusion**: Established: DDX5 is a multifunctional nuclear RNA helicase and splicing-associated factor with a known SRRT relationship and disease relevance in colon-related cancer annotations. Hypothesis: DDX5 may help couple RNA processing with transcriptional and alternative-splicing regulation in this conserved module, but the module does not demonstrate that mechanism.

#### UPF1

- **Related proteins** (co-abundance neighbors): DDX46 (0.82), ABCF1 (0.81); STRING partners: RUVBL2 (0.742), XRN2 (0.812)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in colon, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UPF1 RNA helicase and ATPase. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons.…
- **Diseases (Open Targets)**: Intellectual disability (0.437); Global developmental delay (0.426); High anterior hairline (0.425); Frontal bossing (0.425); Hypertelorism (0.425)
- **Europe PMC papers**: 4252
- **Why important**: UPF1 links RNA processing to post-splicing RNA export and nonsense-mediated decay. It appears in the ribonucleoprotein, mRNA-processing, RNA-splicing, helicase, ATPase, and nucleic-acid terms (18 globally significant GO/KEGG terms, q_global 1.86e-05–0.0398; see the table). STRING connects it to RUVBL2 and XRN2, providing a bridge between RNA surveillance, ATP-dependent remodeling, and RNA degradation. HPA detects it in both colon and liver, and its disease and developmental associations are supported by a large literature base.
- **Conclusion**: Established: UPF1 is a biologically important RNA-surveillance and helicase component that broadens the module beyond spliceosome assembly. Hypothesis: UPF1 may couple splicing quality control to nonsense-mediated decay or export in the shared tissue program, but the co-abundance data do not establish directionality or direct cooperation.

#### LUC7L2

- **Related proteins** (co-abundance neighbors): SRRT (0.82), DDX46 (0.82); STRING partners: DDX46 (0.74), SF3A1 (0.835)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon, liver
- **hu.MAP 3.0**: huMAP3_09490.1, huMAP3_09587.1, huMAP3_10564.1, huMAP3_09621.1, huMAP3_11073.1, huMAP3_09943.1
- **Function (MyGene.info)**: LUC7 like 2, pre-mRNA splicing factor. This gene encodes a protein that contains a C2H2-type zinc finger, coiled-coil region and arginine, serine-rich (RS) domain. A similar protein in mouse interacts with sodium channel modifier 1, and the encoded protein may be involved in the recognition of non-consensus splice donor sites in association with the U1 snRNP spliceosomal subunit. Alternatively spliced transcript variants encoding multi…
- **Diseases (Open Targets)**: Usher syndrome (0.266); chronic venous hypertension (0.202); neurodegenerative disease (0.182); nasopharyngeal carcinoma (0.074); acute myeloid leukemia (0.049)
- **Europe PMC papers**: 562
- **Why important**: LUC7L2 is a pre-mRNA splicing factor with a reported role in recognition of non-consensus splice donor sites. It is repeatedly present in the primary ribonucleoprotein, mRNA-processing, RNA-splicing, and protein-RNA organization terms (20 globally significant GO/KEGG terms, q_global 1.86e-05–0.0409; see the table). It connects to SRRT and DDX46 in the module, to SF3A1 in STRING, and recurs with SRRT across multiple hu.MAP splicing complexes (hu.MAP huMAP3_09490.1) (hu.MAP huMAP3_09587.1) (hu.MAP huMAP3_10564.1) (hu.MAP huMAP3_09621.1) (hu.MAP huMAP3_11073.1) (hu.MAP huMAP3_09943.1). HPA localizes it to the nucleoplasm and detects it in both tissues. Its cell-type-enhanced annotations in neural and glial populations warrant context awareness, while its literature base is substantial.
- **Conclusion**: Established: LUC7L2 is a plausible splice-site-recognition component embedded in known splicing complexes and connected to the module's central RNA-processing genes. Hypothesis: it may contribute to tissue-shared regulation of splice-site choice, but the module does not show which transcripts or splice events are affected.

## Module 1

**Tissue pair**: colon and liver  
**Genes (5)**: SERPINA6, CP, CFB, C3, TNC

### Function

The module is best interpreted as a liver-associated circulating secreted-protein module with a complement-centered core. C3 is the network hub and a central complement component, while CFB is an alternative-pathway component that contributes to the alternative-pathway C3 convertase. CP is a circulating copper-binding protein involved in iron handling and oxidant detoxification. SERPINA6 is a blood corticosteroid carrier, and TNC is an extracellular-matrix protein linked to cell adhesion, growth, epithelial morphogenesis, and wound response. The strongest biological theme is therefore complement and extracellular plasma biology, with associated redox, hormone-transport, and matrix-remodeling functions. No GO or KEGG term passed global correction. The interpretation therefore relies on individual gene annotations, the network structure, STRING supplementary terms such as (STRING Keyword Secreted; within-query FDR = 0.0051), (STRING Keyword Signal; within-query FDR = 0.0117), (STRING Keyword Glycoprotein; within-query FDR = 0.0159), (STRING Keyword Complement alternate pathway; within-query FDR = 0.0178), and (STRING TISSUES Skeletal system; within-query FDR = 0.0431), and the hu.MAP evidence.

**Cell composition.** All genes are secreted according to HPA. The module is predominantly liver-associated at the tissue level, while selected genes also show enhancement in vascular, smooth-muscle, epithelial, stromal, or ductal cell types. Most genes are not detected in immune cells, with only C3 showing immune-cell enrichment in non-classical monocytes. The proteins were not detected by HPA immunohistochemistry in either colon or liver, despite transcript-level tissue enrichment. This composition strongly suggests a plasma or extracellular-protein module rather than a conventional tissue-resident blood-cell module. The shared colon-liver signal could therefore reflect circulating proteins, hepatic production, vascular or extracellular contributions, or shared sample composition. Plasma carryover and cellular composition should be considered before interpreting the module as coordinated expression by colon and liver cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports two high-confidence pairwise relationships: C3 with CFB and C3 with CP. These relationships establish a known complement and plasma-protein core. The supplementary STRING terms support secretion, signaling, glycoprotein biology, complement alternative-pathway biology, and related disease associations, but they are not globally corrected GO or KEGG results. hu.MAP repeatedly places C3, CFB, and CP together in larger complexes, as shown by (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1), and (hu.MAP huMAP3_10678.1). CFB and SERPINA6 co-occur in additional hu.MAP complexes, including (hu.MAP huMAP3_08796.1) and (hu.MAP huMAP3_09832.1), while CP and C3 co-occur in (hu.MAP huMAP3_07432.1) and CFB and CP in (hu.MAP huMAP3_09273.1). These findings support known biochemical or co-complex context for the complement and circulating-protein core. They do not establish that every module edge is a direct physical interaction, because the listed complexes contain many other plasma proteins. TNC has no listed STRING partner or hu.MAP complex, and SERPINA6 has no listed STRING partner, although SERPINA6 has hu.MAP context with CFB.

**STRING interactions (score >= 0.7)**: 2 of 10 gene pairs: C3–CFB (0.999); C3–CP (0.751)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Secreted (FDR = 0.0051, 5 genes); Keyword Signal (FDR = 0.0117, 5 genes); Keyword Glycoprotein (FDR = 0.0159, 5 genes); Keyword Hemolytic uremic syndrome (FDR = 0.0159, 2 genes); Keyword Complement alternate pathway (FDR = 0.0178, 2 genes); Keyword Age-related macular degeneration (FDR = 0.0178, 2 genes); TISSUES Bone marrow cell (FDR = 0.018, 4 genes); TISSUES Skeletal system (FDR = 0.0431, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08395.1 (CP, CFB, C3; 3/43); huMAP3_09531.1 (CP, CFB, C3; 3/47); huMAP3_10101.1 (CP, CFB, C3; 3/49); huMAP3_15040.1 (CP, CFB, C3; 3/64); huMAP3_10678.1 (CP, CFB, C3; 3/71); huMAP3_08796.1 (CFB, SERPINA6; 2/15); huMAP3_09832.1 (CFB, SERPINA6; 2/18); huMAP3_07432.1 (CP, C3; 2/18); huMAP3_09273.1 (CP, CFB; 2/28)

### Novelty

The module should not be described as a wholly new molecular pathway. C3, CFB, and CP have established relationships in STRING and recurring hu.MAP co-complex membership, and their complement or plasma functions are well documented. A potentially novel aspect is the conserved co-abundance pattern across colon and liver and the inclusion of TNC and SERPINA6 in this particular module. However, absence from STRING or hu.MAP alone does not demonstrate novelty, because database coverage, co-abundance, direct interaction, and tissue context are different kinds of evidence. A defensible novelty claim would require replication in independent colon and liver cohorts, adjustment for plasma contamination and cellular composition, and comparison with published tissue co-abundance modules.

**Hypothesis.** Hypothesis: hepatic and vascularly accessible secretion creates a shared extracellular protein milieu in colon and liver samples. C3 and CFB may form the functional complement core, CP may participate in metal and oxidative-state handling, SERPINA6 may report or influence corticosteroid transport, and TNC may connect inflammatory or injury-associated matrix remodeling with the circulating complement context. This model explains the secreted composition, the C3-centered network, the STRING complement terms, and the repeated hu.MAP plasma-protein complexes. It remains a hypothesis rather than demonstrated causality and should be tested by controlling for plasma abundance, measuring protein rather than transcript abundance, and examining complement activation and matrix-remodeling markers experimentally.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): CFB (0.90), CP (0.83), TNC (0.80); STRING partners: CFB (0.999), CP (0.751)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is the network hub with links to CFB, CP, and TNC. It is central to classical and alternative complement activation, generates inflammatory peptide products, and is supported by STRING relationships with CFB and CP plus repeated hu.MAP complex membership. Its disease associations include complement deficiency, atypical hemolytic-uremic syndrome, complement-mediated kidney disease, and age-related macular degeneration. Its literature volume is extensive, making it the best-established anchor for the module.
- **Conclusion**: Established evidence supports C3 as the principal complement and network hub of the module. The hypothesis that C3 links circulating complement activity to TNC-associated matrix remodeling in the shared colon-liver signal is plausible but not demonstrated.

#### CFB

- **Related proteins** (co-abundance neighbors): C3 (0.90); STRING partners: C3 (0.999)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_09273.1
- **Function (MyGene.info)**: complement factor B. This gene encodes complement factor B, a component of the alternative pathway of complement activation. Factor B circulates in the blood as a single chain polypeptide. Upon activation of the alternative pathway, it is cleaved by complement factor D yielding the noncatalytic chain Ba and the catalytic subunit Bb. The active subunit Bb is a serine protease which associates with C3b to form the alter…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with B factor anomaly (0.764); atypical hemolytic-uremic syndrome (0.705); Immunodeficiency due to a complement cascade protein anomaly (0.614); paroxysmal nocturnal hemoglobinuria (0.561); complement 3 glomerulopathy (0.546)
- **Europe PMC papers**: 7226
- **Why important**: CFB is directly connected to C3 with very high STRING confidence and is repeatedly represented with C3 and CP in hu.MAP complexes. It is a defined component of the alternative complement pathway and supplies the catalytic subunit of the alternative-pathway C3 convertase. Its disease associations include atypical hemolytic-uremic syndrome, complement cascade disorders, paroxysmal nocturnal hemoglobinuria, and complement-mediated kidney disease.
- **Conclusion**: Established evidence supports CFB as the clearest alternative-pathway partner of C3 in the module. The hypothesis that CFB activity contributes to the conserved cross-tissue co-abundance pattern requires direct measurement of pathway activation and cannot be inferred from co-abundance alone.

#### CP

- **Related proteins** (co-abundance neighbors): C3 (0.83), SERPINA6 (0.80); STRING partners: C3 (0.751)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_09273.1
- **Function (MyGene.info)**: ceruloplasmin. The protein encoded by this gene is a metalloprotein that binds most of the copper in plasma and is involved in the peroxidation of Fe(II)transferrin to Fe(III) transferrin. Mutations in this gene cause aceruloplasminemia, which results in iron accumulation and tissue damage, and is associated with diabetes and neurologic abnormalities. Two transcript variants, one protein-coding and the other not…
- **Diseases (Open Targets)**: aceruloplasminemia (0.827); cerebellar ataxia (0.572); Hermansky-Pudlak syndrome 3 (0.564); Hermansky-Pudlak syndrome (0.543); neurodegeneration with brain iron accumulation (0.510)
- **Europe PMC papers**: 171928
- **Why important**: CP is connected to the hub C3 and to SERPINA6, appears with C3 and CFB in many hu.MAP complexes, and is a secreted liver-enriched plasma protein. Its established roles include copper binding, iron handling, and cellular oxidant detoxification. Its disease associations include aceruloplasminemia, neurological iron-accumulation disorders, and related neurological or metabolic phenotypes. It also has an extensive literature base.
- **Conclusion**: Established evidence supports CP as a plasma transport and metal-redox component associated with the complement core. The hypothesis that CP modifies the oxidative environment in which complement operates is biologically reasonable but is not proven by the module.

#### TNC

- **Related proteins** (co-abundance neighbors): C3 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tenascin C. This gene encodes an extracellular matrix protein with a spatially and temporally restricted tissue distribution. This protein is homohexameric with disulfide-linked subunits, and contains multiple EGF-like and fibronectin type-III domains. It is implicated in guidance of migrating neurons as well as axons during development, synaptic plasticity, and neuronal regeneration. [provided by RefSeq, Jul…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss (0.619); deafness (0.552); osteoarthritis, hip (0.551); total hip arthroplasty (0.468); Varicose veins (0.460)
- **Europe PMC papers**: 12274
- **Why important**: TNC is directly connected to C3 in the module and is the only member characterized primarily as a secreted extracellular-matrix protein rather than a circulating complement or transport protein. Its annotations implicate cell adhesion, epithelial morphogenesis, growth regulation, and response to wounding. It is associated with vascular and smooth-muscle tissue enhancement and with disorders including hearing loss, deafness, hip osteoarthritis, and varicose veins. Its literature volume is substantial, although the module-specific interaction evidence is limited.
- **Conclusion**: Established evidence supports TNC as an extracellular-matrix and injury-response component linked to the C3 hub by co-abundance. The hypothesis that TNC supplies a tissue-remodeling bridge between complement and the shared colon-liver environment remains speculative because TNC lacks listed STRING and hu.MAP support here.

#### SERPINA6

- **Related proteins** (co-abundance neighbors): CP (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08796.1, huMAP3_09832.1
- **Function (MyGene.info)**: serpin family A member 6. This gene encodes an alpha-globulin protein with corticosteroid-binding properties. This is the major transport protein for glucorticoids and progestins in the blood of most vertebrates. The gene localizes to a chromosomal region containing several closely related serine protease inhibitors which may have evolved by duplication events. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: corticosteroid-binding globulin deficiency (0.638); hereditary disease (0.193); plasma protein metabolism disease (0.192); femur fracture (0.172); liver disorder (0.144)
- **Europe PMC papers**: 799
- **Why important**: SERPINA6 is liver-enriched, secreted to blood, and connected to CP in the module. It is the principal corticosteroid-binding protein in blood and is annotated with glucocorticoid biosynthetic biology. It has hu.MAP context with CFB and disease associations involving corticosteroid-binding globulin deficiency and plasma-protein metabolism. Its literature volume is smaller than that of C3 or CP, but its functional specificity makes it informative.
- **Conclusion**: Established evidence supports SERPINA6 as a corticosteroid-transport component that may help characterize the endocrine and hepatic context of the module. The hypothesis that corticosteroid transport coordinates with complement or matrix remodeling in this module is unproven and needs endocrine measurements and independent replication.

## Module 2

**Tissue pair**: colon and liver  
**Genes (10)**: CNOT1, CACYBP, FKBP4, GMPS, IPO4, NAA15, NSUN2, AARS1, TARS1, YARS1

### Function

The strongest interpretation is a conserved intracellular RNA-handling and translation-support module. The primary evidence is the convergence of (GO:MF tRNA binding; q_global = 0.00773), (GO:MF catalytic activity, acting on RNA; q_global = 0.0313), and (GO:MF catalytic activity, acting on a tRNA; q_global = 0.0441), which identify tRNA binding, catalytic activity acting on RNA, and catalytic activity acting on a tRNA. AARS1, TARS1, and YARS1 are aminoacyl-tRNA synthetases, while NSUN2 modifies tRNA and supports correct decoding. CNOT1 adds a broader post-transcriptional RNA-regulatory component. The network therefore most plausibly reflects coordinated control of tRNA modification, tRNA aminoacylation, translation competence, and RNA processing rather than a tissue-specific metabolic pathway. The network is sparse, so the enrichment supports a functional theme but does not establish that all genes form one physical complex.

**Cell composition.** This is predominantly a broadly expressed, intracellular protein module. HPA classifies most genes as having low tissue specificity and low cell-type specificity, with cytosolic or nucleoplasmic locations. Protein detection is reported in both colon and liver for most genes with available data, consistent with a shared cellular program rather than a protein secretion signature. Only one gene is annotated as secreted, and all genes have low immune-cell specificity; therefore, the module is not strongly suggestive of plasma proteins, blood-cell contamination, or a shared blood-cell population. GMPS and IPO4 show testis-enhanced or reproductive-cell-associated HPA patterns, but these isolated features do not define the module as reproductive or tissue-specific. The shared colon-liver signal is more consistent with a ubiquitous housekeeping-like RNA and protein-production program.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF tRNA binding | 0.00773 | AARS1, NSUN2, TARS1, YARS1 |
| GO:MF catalytic activity, acting on RNA | 0.0313 | AARS1, CNOT1, NSUN2, TARS1, YARS1 |
| GO:MF catalytic activity, acting on a tRNA | 0.0441 | AARS1, NSUN2, TARS1, YARS1 |

### STRING and hu.MAP

STRING independently supports the aminoacyl-tRNA-synthetase core: AARS1 is linked to TARS1 and YARS1, and TARS1 is linked to YARS1. These are concordant with (STRING Keyword tRNA-binding; within-query FDR = 0.00014), (STRING Function tRNA binding; within-query FDR = 0.0079), and (STRING Function Catalytic activity, acting on a tRNA; within-query FDR = 0.0189) and with the primary terms (GO:MF tRNA binding; q_global = 0.00773) and (GO:MF catalytic activity, acting on a tRNA; q_global = 0.0441). STRING also links GMPS with IPO4, while the broader cytoplasmic keyword (STRING Keyword Cytoplasm; within-query FDR = 0.0294) covers the module. hu.MAP provides additional evidence that AARS1 and YARS1 recur together in several complexes, including (hu.MAP huMAP3_04783.1), (hu.MAP huMAP3_10302.1), and (hu.MAP huMAP3_10115.1), and that AARS1, GMPS, and YARS1 occur together in (hu.MAP huMAP3_14442.1). The repeated AARS1-YARS1 association is the best-supported known structural relationship. In contrast, NSUN2, TARS1, NAA15, CNOT1, IPO4, FKBP4, and CACYBP lack corresponding hu.MAP or STRING pair evidence in this fact sheet. Thus, the co-abundance module combines a known tRNA-synthetase interaction core with additional genes connected primarily by correlated abundance rather than established physical interaction.

**STRING interactions (score >= 0.7)**: 4 of 45 gene pairs: AARS1–TARS1 (0.929); AARS1–YARS1 (0.996); GMPS–IPO4 (0.861); TARS1–YARS1 (0.911)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword tRNA-binding (FDR = 0.00014, 4 genes); Function tRNA binding (FDR = 0.0079, 4 genes); Function Catalytic activity, acting on a tRNA (FDR = 0.0189, 4 genes); Keyword Cytoplasm (FDR = 0.0294, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (AARS1, GMPS, YARS1; 3/57); huMAP3_04783.1 (AARS1, YARS1; 2/4); huMAP3_10302.1 (AARS1, YARS1; 2/9); huMAP3_10115.1 (AARS1, YARS1; 2/14)

### Novelty

The underlying functions are not new: aminoacyl-tRNA synthetases, NSUN2-mediated tRNA modification, GMP synthesis, protein folding, nuclear import, N-terminal acetylation, and CCR4-NOT RNA regulation are established biology. The AARS1-YARS1-TARS1 relationship is also represented in STRING and several hu.MAP complexes. What may be novel is the conserved colon-liver co-abundance configuration that places this known translation-related core together with NSUN2, NAA15, CNOT1, IPO4, FKBP4, GMPS, and CACYBP. That claim should remain cautious because correlation does not demonstrate physical interaction or causal coordination, and absence from STRING or hu.MAP cannot by itself establish novelty. The defensible conclusion is that this is a potentially new tissue-pair co-abundance pattern built around a largely known molecular program, rather than a newly discovered molecular complex.

**Hypothesis.** Hypothesis: the module reflects a shared cellular demand in colon and liver for maintaining accurate translation during routine protein production and cellular stress. In this model, AARS1, TARS1, and YARS1 supply charged tRNAs; NSUN2 stabilizes or improves tRNA decoding through cytosine methylation; CNOT1 coordinates mRNA turnover and translational regulation; and NAA15 supports maturation of newly synthesized proteins. GMPS may supply guanine nucleotides needed for RNA and protein synthesis, while IPO4, FKBP4, and CACYBP could connect the program to nuclear transport, protein folding, and regulated protein turnover. The network correlations may therefore arise from coordinated proteome maintenance rather than a single physical complex. This hypothesis requires experimental testing through perturbation, interaction assays, and validation across independent colon and liver cohorts.

### Important genes

#### YARS1

- **Related proteins** (co-abundance neighbors): FKBP4 (0.83), NSUN2 (0.81), GMPS (0.81); STRING partners: AARS1 (0.996), TARS1 (0.911)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in colon, liver
- **hu.MAP 3.0**: huMAP3_14442.1, huMAP3_04783.1, huMAP3_10302.1, huMAP3_10115.1
- **Function (MyGene.info)**: tyrosyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Tyrosyl-tRNA synthetase belongs to the class I tRNA synthetase family. Cytokine activities have also been observ…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease dominant intermediate C (0.739); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset 2 (0.707); hereditary disease (0.509); Charcot-Marie-Tooth disease (0.418); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset (0.333)
- **Europe PMC papers**: 215
- **Why important**: YARS1 has one of the strongest network positions, connecting FKBP4, NSUN2, and GMPS, and it is directly supported by (GO:MF tRNA binding; q_global = 0.00773), (GO:MF catalytic activity, acting on RNA; q_global = 0.0313), (GO:MF catalytic activity, acting on a tRNA; q_global = 0.0441), (STRING Keyword tRNA-binding; within-query FDR = 0.00014), (STRING Function tRNA binding; within-query FDR = 0.0079), and (STRING Function Catalytic activity, acting on a tRNA; within-query FDR = 0.0189). It is a tyrosyl-tRNA synthetase with an established role in tyrosine charging for translation, and it recurs with AARS1 in multiple hu.MAP complexes (hu.MAP huMAP3_14442.1) through (hu.MAP huMAP3_10115.1). Its disease associations include Charcot-Marie-Tooth disease and other multisystem or neurologic disorders, and the literature support is substantial. It is therefore both a functional anchor and a bridge between the aminoacylation core and the rest of the module.
- **Conclusion**: Established evidence supports YARS1 as a central translation-related component and a repeatedly observed molecular association partner of AARS1. It is plausible, but not established, that YARS1 helps coordinate the broader module in colon and liver.

#### AARS1

- **Related proteins** (co-abundance neighbors): TARS1 (0.82); STRING partners: TARS1 (0.929), YARS1 (0.996)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in colon, liver
- **hu.MAP 3.0**: huMAP3_14442.1, huMAP3_04783.1, huMAP3_10302.1, huMAP3_10115.1
- **Function (MyGene.info)**: alanyl-tRNA synthetase 1. The human alanyl-tRNA synthetase (AARS) belongs to a family of tRNA synthases, of the class II enzymes.  Class II tRNA synthases evolved early in evolution and are highly conserved. This is reflected by the fact that 498 of the 968-residue polypeptide human AARS shares 41% identity witht the E.coli protein.  tRNA synthases are the enzymes that interpret the RNA code and attach specific aminoacids …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2N (0.762); developmental and epileptic encephalopathy, 29 (0.747); undetermined early-onset epileptic encephalopathy (0.678); trichothiodystrophy 8, nonphotosensitive (0.568); Charcot-Marie-Tooth disease type 2 (0.566)
- **Europe PMC papers**: 672
- **Why important**: AARS1 is a core aminoacyl-tRNA synthetase and is included in all three primary enrichment terms (GO:MF tRNA binding; q_global = 0.00773), (GO:MF catalytic activity, acting on RNA; q_global = 0.0313), and (GO:MF catalytic activity, acting on a tRNA; q_global = 0.0441) as well as the concordant STRING terms (STRING Keyword tRNA-binding; within-query FDR = 0.00014), (STRING Function tRNA binding; within-query FDR = 0.0079), and (STRING Function Catalytic activity, acting on a tRNA; within-query FDR = 0.0189). It connects directly to TARS1 and YARS1 in STRING and appears in every hu.MAP complex listed in the fact sheet (hu.MAP huMAP3_14442.1) through (hu.MAP huMAP3_10115.1). Its network and complex evidence make it the strongest structural anchor of the module. Its disease associations include Charcot-Marie-Tooth disease and developmental or epileptic encephalopathy, with a substantial literature base.
- **Conclusion**: Established evidence identifies AARS1 as a central aminoacylation component with reproducible interaction and complex support. The data support its importance to the module, but do not show that its disease associations explain the colon-liver co-abundance pattern.

#### NSUN2

- **Related proteins** (co-abundance neighbors): YARS1 (0.81), TARS1 (0.81), NAA15 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP2/Sun RNA methyltransferase 2. This gene encodes a methyltransferase that catalyzes the methylation of cytosine to 5-methylcytosine (m5C) at position 34 of intron-containing tRNA(Leu)(CAA) precursors. This modification is necessary to stabilize the anticodon-codon pairing and correctly translate the mRNA. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Mar…
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.694); hereditary disease (0.518); Intellectual disability (0.489); phenylketonuria (0.470); neurodegenerative disease (0.462)
- **Europe PMC papers**: 2458
- **Why important**: NSUN2 is connected to YARS1, TARS1, and NAA15 and participates in every primary enrichment term (GO:MF tRNA binding; q_global = 0.00773), (GO:MF catalytic activity, acting on RNA; q_global = 0.0313), and (GO:MF catalytic activity, acting on a tRNA; q_global = 0.0441). Its established function is methylation of tRNA cytosine residues, with additional roles in RNA processing and RNA export. It has the largest literature volume among the genes selected here and is associated with intellectual disability and neurodegenerative disease. Its position links the aminoacyl-tRNA-synthetase signal to RNA modification, making it important for interpreting the module as an RNA quality-control program rather than simple translation alone.
- **Conclusion**: Established evidence supports NSUN2 as a tRNA-modification and RNA-processing component that complements the aminoacylation core. Its direct physical integration into this module is not established by the reported STRING or hu.MAP evidence; that integration is a hypothesis based on co-abundance and shared functional enrichment.

#### TARS1

- **Related proteins** (co-abundance neighbors): AARS1 (0.82), NSUN2 (0.81); STRING partners: AARS1 (0.929), YARS1 (0.911)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in colon, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: threonyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Threonyl-tRNA synthetase belongs to the class-II aminoacyl-tRNA synthetase family [provided by RefSeq, Jul 2008]…
- **Diseases (Open Targets)**: trichothiodystrophy 7, nonphotosensitive (0.520); trichothiodystrophy (0.430); actinic keratosis (0.356); dyshidrosis (0.315); placental abruption (0.307)
- **Europe PMC papers**: 147
- **Why important**: TARS1 is one of the genes contributing to all primary enrichment terms (GO:MF tRNA binding; q_global = 0.00773), (GO:MF catalytic activity, acting on RNA; q_global = 0.0313), and (GO:MF catalytic activity, acting on a tRNA; q_global = 0.0441) and to the corresponding STRING terms (STRING Keyword tRNA-binding; within-query FDR = 0.00014), (STRING Function tRNA binding; within-query FDR = 0.0079), and (STRING Function Catalytic activity, acting on a tRNA; within-query FDR = 0.0189). It encodes threonyl-tRNA synthetase and directly connects to AARS1 and YARS1 in STRING, placing it inside the best-supported aminoacylation subnetwork. Its disease associations include trichothiodystrophy and other disorders, and its literature base is established though smaller than that of several other selected genes.
- **Conclusion**: Established evidence supports TARS1 as a genuine member of the aminoacyl-tRNA-synthetase core and as a likely contributor to the module's translation-related function. The co-abundance data do not establish a tissue-specific role or a causal role in the associated diseases.

#### CNOT1

- **Related proteins** (co-abundance neighbors): NAA15 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in colon, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CCR4-NOT transcription complex subunit 1. Enables armadillo repeat domain binding activity; molecular adaptor activity; and nuclear receptor binding activity. Contributes to poly(A)-specific ribonuclease activity. Involved in several processes, including negative regulation of signal transduction; positive regulation of cytoplasmic mRNA processing body assembly; and regulation of gene expression. Located in P-body and cytosol. Part of CCR…
- **Diseases (Open Targets)**: holoprosencephaly 12 with or without pancreatic agenesis (0.749); Vissers-Bodmer syndrome (0.697); hereditary disease (0.515); complex neurodevelopmental disorder (0.474); neurodegenerative disease (0.471)
- **Europe PMC papers**: 1262
- **Why important**: CNOT1 is the central scaffold subunit of the CCR4-NOT complex and is connected in the module to NAA15. It contributes to (GO:MF catalytic activity, acting on RNA; q_global = 0.0313), linking the module's RNA-catalytic signal to mRNA deadenylation, transcript turnover, P-body biology, and regulation of translation. It is also represented in the cytoplasmic STRING term (STRING Keyword Cytoplasm; within-query FDR = 0.0294). Its association with holoprosencephaly and neurodevelopmental disorders provides disease relevance, while its substantial literature supports a well-established role in post-transcriptional regulation.
- **Conclusion**: Established evidence supports CNOT1 as an RNA-regulatory component that could broaden the module beyond tRNA metabolism. Its inclusion in the same conserved co-abundance program is suggestive, but a direct mechanistic connection to the aminoacyl-tRNA-synthetase core remains unproven.

## Module 3

**Tissue pair**: colon and liver  
**Genes (5)**: COL4A2, COL6A1, COL6A2, COL6A3, HSPG2

### Function

This is a strongly coherent extracellular-matrix structural module. The primary evidence is the globally corrected enrichment for ECM-receptor interaction (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 5.4e-06), extracellular-matrix structural constituents (GO:MF extracellular matrix structural constituent conferring tensile strength; q_global = 1.45e-05) (GO:MF extracellular matrix structural constituent; q_global = 3.3e-05), external encapsulating structure and extracellular matrix (GO:CC external encapsulating structure; q_global = 5.09e-05) (GO:CC extracellular matrix; q_global = 5.09e-05), collagen trimers (GO:CC collagen trimer; q_global = 0.00012), basement membrane/interstitial matrix (GO:CC basement membrane/interstitial matrix interface; q_global = 0.0155) (GO:CC basement membrane; q_global = 0.0339), collagen VI trimer and beaded filament (GO:CC collagen type VI trimer; q_global = 0.0155) (GO:CC collagen beaded filament; q_global = 0.0155), and integrin and focal-adhesion signaling (KEGG Integrin signaling - Homo sapiens (human); q_global = 0.00292) (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.00321). All module genes are represented in the ECM-receptor interaction term (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 5.4e-06). The collagen genes indicate collagen assembly and tensile structural support, while HSPG2 adds proteoglycan-mediated matrix organization and cell-surface interaction. The protein-digestion and absorption terms (KEGG Protein digestion and absorption - Homo sapiens (human); q_global = 6.85e-05) and the cytoskeleton-related terms (KEGG Cytoskeleton in muscle cells - Homo sapiens (human); q_global = 0.000342) are consistent with matrix-associated tissue architecture, but the dominant interpretation is basement-membrane and interstitial-matrix organization.

**Cell composition.** The module is composed entirely of secreted extracellular-matrix proteins: COL4A2, COL6A1, COL6A2, COL6A3, and HSPG2. HPA assigns all of them to extracellular secretion or matrix deposition. The single-cell evidence points consistently to stromal, fibroblast-like, fibro-adipogenic progenitor, hepatic stellate, and smooth-muscle-associated populations rather than immune cells. Four genes are not detected in immune cells, and only COL6A2 has group-enriched blood-cell evidence involving T-cell populations. Thus, this module is unlikely to represent a blood-cell program. It more plausibly reflects stromal or vascular matrix content shared by colon and liver, although shared stromal-cell composition or extracellular matrix abundance in the samples could contribute to the cross-tissue co-abundance pattern. The tissue-level HPA pattern is mixed, with tissue enhancement in placenta, smooth muscle, or blood vessel contexts and low tissue specificity for some collagen genes; protein detection is also stronger in colon than liver for several genes. These observations warrant caution when interpreting the module as a liver- or colon-specific regulatory program.

**GO/KEGG enrichment**: 20 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG ECM-receptor interaction - Homo sapiens (human) | 5.4e-06 | COL4A2, COL6A1, COL6A2, COL6A3, HSPG2 |
| GO:MF extracellular matrix structural constituent conferring tensile strength | 1.45e-05 | COL4A2, COL6A1, COL6A2, COL6A3 |
| GO:MF extracellular matrix structural constituent | 3.3e-05 | COL4A2, COL6A1, COL6A2, COL6A3, HSPG2 |
| GO:CC external encapsulating structure | 5.09e-05 | COL4A2, COL6A1, COL6A2, COL6A3, HSPG2 |
| GO:CC extracellular matrix | 5.09e-05 | COL4A2, COL6A1, COL6A2, COL6A3, HSPG2 |
| KEGG Protein digestion and absorption - Homo sapiens (human) | 6.85e-05 | COL4A2, COL6A1, COL6A2, COL6A3 |
| GO:CC collagen trimer | 0.00012 | COL4A2, COL6A1, COL6A2, COL6A3 |
| KEGG Cytoskeleton in muscle cells - Homo sapiens (human) | 0.000342 | COL4A2, COL6A1, COL6A2, COL6A3, HSPG2 |
| KEGG PI3K-Akt signaling pathway - Homo sapiens (human) | 0.00126 | COL4A2, COL6A1, COL6A2, COL6A3 |
| GO:CC complex of collagen trimers | 0.0017 | COL4A2, COL6A1, COL6A3 |
| KEGG Integrin signaling - Homo sapiens (human) | 0.00292 | COL4A2, COL6A1, COL6A2, COL6A3 |
| KEGG Focal adhesion - Homo sapiens (human) | 0.00321 | COL4A2, COL6A1, COL6A2, COL6A3 |
| KEGG Human papillomavirus infection - Homo sapiens (human) | 0.00383 | COL4A2, COL6A1, COL6A2, COL6A3 |
| GO:MF structural molecule activity | 0.0086 | COL4A2, COL6A1, COL6A2, COL6A3, HSPG2 |
| GO:CC collagen type VI trimer | 0.0155 | COL6A1, COL6A3 |

### STRING and hu.MAP

STRING supports the biological coherence of the module: the collagen genes have high-confidence connections, especially among the three collagen VI chains, and COL4A2 connects to each collagen VI member. HSPG2 has a high-confidence connection to COL6A3 in the module graph, although it has no listed STRING partner in the separate STRING interaction summary. STRING functional enrichment independently supports ECM-receptor interaction, integrin cell-surface interactions, ECM proteoglycans, collagen trimerization, collagen assembly, and matrix degradation (7 supplementary STRING terms; within-query FDR 2.88e-07–4.52e-06). These are supplementary because their FDR is not corrected across all modules. hu.MAP provides complex-level support rather than a complete module match: COL4A2 and COL6A1 co-occur in one matrix-related complex (hu.MAP huMAP3_06555.1), while COL4A2 and COL6A3 co-occur in another (hu.MAP huMAP3_13038.1). The complexes contain additional collagen-processing, collagen, matrix, and remodeling proteins. COL6A2 and HSPG2 lack a listed hu.MAP complex with another module member. Together, STRING and hu.MAP indicate that the module recapitulates known extracellular-matrix relationships, while also suggesting that the co-abundance module is broader than any single experimentally catalogued complex.

**STRING interactions (score >= 0.7)**: 6 of 10 gene pairs: COL4A2–COL6A1 (0.81); COL4A2–COL6A2 (0.813); COL4A2–COL6A3 (0.792); COL6A1–COL6A2 (0.998); COL6A1–COL6A3 (0.994); COL6A2–COL6A3 (0.994)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG ECM-receptor interaction (FDR = 2.88e-07, 5 genes); RCTM Integrin cell surface interactions (FDR = 7.92e-07, 5 genes); RCTM ECM proteoglycans (FDR = 7.92e-07, 5 genes); RCTM Degradation of the extracellular matrix (FDR = 8.37e-07, 5 genes); RCTM NCAM1 interactions (FDR = 8.37e-07, 4 genes); RCTM Signaling by PDGF (FDR = 1.31e-06, 4 genes); RCTM Collagen chain trimerization (FDR = 1.64e-06, 4 genes); Pfam Collagen triple helix repeat (20 copies) (FDR = 3.42e-06, 4 genes); Keyword Extracellular matrix (FDR = 4.04e-06, 5 genes); KEGG Protein digestion and absorption (FDR = 4.4e-06, 4 genes); RCTM Collagen degradation (FDR = 4.52e-06, 4 genes); RCTM Assembly of collagen fibrils and other multimeric structures (FDR = 4.52e-06, 4 genes); Keyword Collagen (FDR = 4.72e-06, 4 genes); Function Extracellular matrix structural constituent (FDR = 4.99e-06, 5 genes); Function Extracellular matrix structural constituent conferring tensile strength (FDR = 4.99e-06, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06555.1 (COL4A2, COL6A1; 2/14); huMAP3_13038.1 (COL4A2, COL6A3; 2/40)

### Novelty

The module should not be claimed as a wholly new molecular interaction network. Its central biology is well established: collagen VI chains form a known structural unit, COL4A2 is a basement-membrane collagen, and HSPG2 is a matrix proteoglycan that cross-links matrix and cell-surface components. The high-confidence STRING connections, the STRING pathway enrichments, and the hu.MAP complexes further show that several relationships are already documented. A potentially novel aspect is the conserved co-abundance of this particular five-gene combination across colon and liver and its specific tissue-pair network context. However, absence from a particular STRING or hu.MAP entry cannot establish novelty, and the shared pattern may arise from common stromal or vascular cell composition. Novelty therefore requires independent validation, such as replication in additional colon and liver cohorts, cell-composition adjustment, spatial or single-cell confirmation, and testing whether the module varies with fibrosis, tissue remodeling, or disease state.

**Hypothesis.** Hypothesis: a shared stromal or vascular extracellular-matrix program in colon and liver coordinates collagen VI microfibril assembly with collagen IV basement-membrane organization and perlecan-mediated matrix signaling. COL6A1, COL6A2, and COL6A3 may assemble into collagen VI structures, COL4A2 may contribute to basement-membrane architecture and signaling-related matrix functions, and HSPG2 may organize matrix components and influence integrin- or growth-factor-associated signaling. The resulting matrix state could generate the observed co-abundance through common fibroblast-like or hepatic-stellate-associated cells, shared tissue remodeling, or both. This is a mechanistic hypothesis rather than a demonstrated causal pathway; it should be tested by perturbing the collagen VI or perlecan axis and measuring matrix assembly, cell adhesion, focal-adhesion signaling, and tissue remodeling.

### Important genes

#### COL6A3

- **Related proteins** (co-abundance neighbors): COL6A2 (0.89), COL6A1 (0.88), HSPG2 (0.81); STRING partners: COL4A2 (0.792), COL6A1 (0.994), COL6A2 (0.994)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13038.1
- **Function (MyGene.info)**: collagen type VI alpha 3 chain. This gene encodes the alpha-3 chain, one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The alpha-3 chain of type VI collagen is much larger than the alpha-1 and -2 chains. This difference in size is largely due to an increase in the number of subdomains, similar to von Willebrand Factor type A domains, that are found in the amino termin…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy (0.766); dystonia 27 (0.764); Bethlem myopathy (0.758); Bethlem myopathy 1C (0.747); Bethlem myopathy 1A (0.718)
- **Europe PMC papers**: 5386
- **Why important**: COL6A3 is the most connected and highest-strength node in the module, linking the collagen VI members with HSPG2. It appears in nearly all primary ECM, collagen, basement-membrane, and signaling terms (10 globally significant GO/KEGG terms, q_global 5.4e-06–0.0339; see the table) and in every listed STRING enrichment (15 supplementary STRING terms; within-query FDR 2.88e-07–4.99e-06). HPA supports stromal, fibroblast-like, fibro-adipogenic progenitor, and hepatic-stellate associations, while MyGene.info identifies it as the alpha-three chain of collagen VI. Its disease associations include Ullrich congenital muscular dystrophy, Bethlem myopathy, and dystonia, and it has substantial literature coverage.
- **Conclusion**: Established: COL6A3 is a central collagen VI extracellular-matrix component with strong network, annotation, STRING, HPA, and disease support. Hypothesis: its central position may make it an important organizer or readout of the shared stromal matrix state, but causality in colon and liver is not established.

#### COL6A1

- **Related proteins** (co-abundance neighbors): COL6A3 (0.88), COL4A2 (0.85); STRING partners: COL4A2 (0.81), COL6A2 (0.998), COL6A3 (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_06555.1
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is a core collagen VI chain and a highly connected collagen node, with especially strong STRING links to COL6A2 and COL6A3. It participates in the full set of major ECM and collagen annotations, including collagen VI trimer and beaded filament terms [E1-E20 except terms whose overlap excludes it only where applicable]. HPA places it in fibroblast-like stromal populations and detects it in colon. MyGene.info describes collagen VI as a heterotrimer requiring COL6A1, COL6A2, and COL6A3. Its disease associations include Bethlem myopathy and Ullrich congenital muscular dystrophy, with substantial literature coverage.
- **Conclusion**: Established: COL6A1 is a core structural component of collagen VI and is strongly supported as part of this ECM module. Hypothesis: coordinated COL6A1 abundance may report collagen VI assembly capacity in shared colon and liver stromal populations; direct tissue-specific regulation remains unproven.

#### COL6A2

- **Related proteins** (co-abundance neighbors): COL6A3 (0.89), COL4A2 (0.80); STRING partners: COL4A2 (0.813), COL6A1 (0.998), COL6A3 (0.994)
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 2 chain. This gene encodes one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The product of this gene contains several domains similar to von Willebrand Factor type A domains. These domains have been shown to bind extracellular matrix proteins, an interaction that explains the importance of this collagen in organizing matrix components. Mutation…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy 1B (0.770); Bethlem myopathy (0.755); Ullrich congenital muscular dystrophy (0.743); Bethlem myopathy 1B (0.723); Bethlem myopathy 1A (0.713)
- **Europe PMC papers**: 4115
- **Why important**: COL6A2 is a core collagen VI chain with strong STRING links to COL6A1 and COL6A3 and a direct connection to COL4A2 in the module graph. It contributes to the major ECM, collagen, integrin, focal-adhesion, and structural-constituent enrichments (15 globally significant GO/KEGG terms, q_global 5.4e-06–0.0332; see the table). Its HPA profile supports fibroblast-like, fibro-adipogenic progenitor, and hepatic-stellate associations, with additional group-enriched T-cell evidence that should be interpreted cautiously. MyGene.info links its von-Willebrand-factor-like domains to matrix organization and associates mutations with Bethlem myopathy and Ullrich muscular dystrophy. It has substantial literature coverage.
- **Conclusion**: Established: COL6A2 is a bona fide collagen VI matrix component and a coherent member of the module. Hypothesis: its co-abundance may reflect matrix assembly by stromal cells rather than immune-cell biology, because the dominant HPA evidence is stromal and the immune signal is limited.

#### COL4A2

- **Related proteins** (co-abundance neighbors): COL6A1 (0.85), COL6A2 (0.80); STRING partners: COL6A1 (0.81), COL6A2 (0.813), COL6A3 (0.792)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06555.1, huMAP3_13038.1
- **Function (MyGene.info)**: collagen type IV alpha 2 chain. This gene encodes one of the six subunits of type IV collagen, the major structural component of basement membranes. The C-terminal portion of the protein, known as canstatin, is an inhibitor of angiogenesis and tumor growth. Like the other members of the type IV collagen gene family, this gene is organized in a head-to-head conformation with another type IV collagen gene so that each gene pair sh…
- **Diseases (Open Targets)**: brain small vessel disease 2A, autosomal dominant (0.728); porencephaly (0.612); Dupuytren Contracture (0.587); coronary artery disorder (0.548); hemorrhage, intracerebral, susceptibility to (0.541)
- **Europe PMC papers**: 5290
- **Why important**: COL4A2 connects the collagen VI group in the module and participates in both hu.MAP matrix complexes (hu.MAP huMAP3_06555.1) (hu.MAP huMAP3_13038.1). It is represented across the primary ECM, basement-membrane, collagen, integrin, focal-adhesion, and structural terms (15 globally significant GO/KEGG terms, q_global 5.4e-06–0.0339; see the table). MyGene.info identifies it as a type IV collagen subunit and notes that its canstatin-containing C-terminal region has anti-angiogenic and tumor-growth-inhibitory activity. HPA associates it with stromal and vascular-related cell contexts. Its disease associations include brain small-vessel disease, porencephaly, Dupuytren contracture, coronary artery disorder, and susceptibility to intracerebral hemorrhage, with substantial literature coverage.
- **Conclusion**: Established: COL4A2 supplies basement-membrane biology and bridges the collagen VI-rich module to broader matrix complexes. Hypothesis: COL4A2 may connect structural matrix assembly with vascular or signaling consequences in the shared tissue program, but this functional coupling was not directly tested.

#### HSPG2

- **Related proteins** (co-abundance neighbors): COL6A3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in colon, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 is the module's perlecan proteoglycan component and the only node that links to COL6A3 without additional listed STRING partners. It is present in the primary ECM-receptor, structural, external-encapsulating-structure, and basement-membrane terms (7 globally significant GO/KEGG terms, q_global 5.4e-06–0.0339; see the table). HPA detects it in both colon and liver and associates it with blood-vessel, fibro-adipogenic progenitor, and hepatic-stellate contexts. MyGene.info describes perlecan as a multidomain proteoglycan that binds and cross-links matrix and cell-surface molecules, including collagen IV and other matrix proteins. Its disease associations include Schwartz-Jampel syndrome, Silverman-Handmaker dyssegmental dysplasia, atrial fibrillation, COVID-19, and dengue disease, with substantial literature coverage.
- **Conclusion**: Established: HSPG2 is a matrix-organizing proteoglycan that complements the collagen components and is directly detected in both tissues. Hypothesis: HSPG2 may stabilize or signal through the collagen-rich matrix state and could help explain conservation across colon and liver, although the module data do not demonstrate that mechanism.

## Module 5

**Tissue pair**: colon and liver  
**Genes (5)**: DHX9, HNRNPR, NOP56, RSL1D1, PDCD11

### Function

The strongest interpretation is a conserved nucleolar and nuclear RNA-management module. (GO:CC ribonucleoprotein complex; q_global = 0.0305) identifies a ribonucleoprotein-complex signal carried by DHX9, HNRNPR, NOP56 and PDCD11, while (GO:BP RNA processing; q_global = 0.0454) identifies RNA processing involving the same four genes. The supplementary STRING signals refine this interpretation toward preribosome assembly, rRNA processing, ribonucleoprotein complex biogenesis and the nucleolus (15 supplementary STRING terms; within-query FDR 0.00015–0.0156). NOP56 and PDCD11 provide especially direct evidence for pre-rRNA maturation and ribosome biogenesis; HNRNPR supports pre-mRNA processing and spliceosomal function; DHX9 supplies RNA and RNA–DNA duplex unwinding and broader nuclear RNA regulation. RSL1D1 is consistent with the nucleolar component of this program through its STRING context and nucleolar localization, although it is not part of either globally significant GO term.

**Cell composition.** This is not a plasma-protein or secreted-protein module: none of the genes is secreted, and all are detected at the protein level in both colon and liver. HPA reports low tissue specificity for all genes, low immune-cell specificity for all genes, and no recurring enriched blood-cell type. Thus the shared signal is unlikely to be explained primarily by circulating proteins, blood-cell contamination or a restricted immune population. Its broad tissue distribution is more compatible with a generally used nuclear and nucleolar RNA-processing program. NOP56 has cell-type-enhanced HPA expression in differentiating spermatogonia and oocytes, but this does not establish that those cell types explain the colon–liver module.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC ribonucleoprotein complex | 0.0305 | DHX9, HNRNPR, NOP56, PDCD11 |
| GO:BP RNA processing | 0.0454 | DHX9, HNRNPR, NOP56, PDCD11 |

### STRING and hu.MAP

STRING supports a structured biological neighborhood rather than an arbitrary gene grouping. The observed links include DHX9 with HNRNPR and a tightly connected NOP56–PDCD11–RSL1D1 subnetwork, with high confidence for each reported interaction. STRING enrichment independently points to ribonucleoprotein complexes, preribosome, nucleolus, rRNA processing and RNA processing (15 supplementary STRING terms; within-query FDR 0.00015–0.0156). These relationships are already known functional or physical associations and therefore strengthen the interpretation that the co-abundance module tracks a real RNA-processing program. No hu.MAP complex contains at least two module members, so the present data do not identify a replicated hu.MAP-defined complex. The co-abundance pattern should therefore be viewed as coordinated activity across related RNA-processing machinery, not as proof that all genes form one physical complex.

**STRING interactions (score >= 0.7)**: 4 of 10 gene pairs: DHX9–HNRNPR (0.909); NOP56–PDCD11 (0.997); NOP56–RSL1D1 (0.991); PDCD11–RSL1D1 (0.978)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Ribonucleoprotein complex (FDR = 0.00015, 5 genes); Component Ribonucleoprotein complex (FDR = 0.00028, 5 genes); Component Preribosome (FDR = 0.00062, 3 genes); COMPARTMENTS Preribosome (FDR = 0.00068, 3 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 0.00098, 3 genes); Process RNA processing (FDR = 0.0015, 5 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0019, 5 genes); COMPARTMENTS Nucleolus (FDR = 0.0029, 4 genes); Keyword Isopeptide bond (FDR = 0.0059, 5 genes); Process Ribonucleoprotein complex biogenesis (FDR = 0.0071, 4 genes); COMPARTMENTS 90S preribosome (FDR = 0.0075, 2 genes); Keyword Ubl conjugation (FDR = 0.0078, 5 genes); Process rRNA processing (FDR = 0.0083, 3 genes); NetworkNeighborAL Mixed, incl. Preribosome, large subunit precursor, and Maturation of LSU-rRNA (FDR = 0.0083, 2 genes); COMPARTMENTS Small-subunit processome (FDR = 0.0156, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is unlikely to represent a wholly new molecular function: its genes have established roles in RNA processing, preribosome biology, nucleolar organization and RNA helicase activity, and most reported STRING relationships are already known. Its potentially novel aspect is the conserved co-abundance pattern shared by colon and liver, especially the way the DHX9–HNRNPR branch is linked with the NOP56–PDCD11–RSL1D1 nucleolar branch. However, the fact that no hu.MAP complex contains multiple members does not establish novelty, because absence from a resource can reflect coverage, detection or complex-boundary limitations. A claim of a new module-specific mechanism would require independent validation in additional cohorts, perturbation experiments or direct measurements of the proposed RNA-processing outputs.

**Hypothesis.** Hypothesis: in both colon and liver, coordinated demand for RNA maturation couples a nuclear RNA surveillance and processing arm with a nucleolar ribosome-biogenesis arm. DHX9 and HNRNPR could coordinate handling of structured RNA, RNA–DNA hybrids and pre-mRNA-associated complexes, while NOP56, PDCD11 and RSL1D1 could support nucleolar pre-rRNA maturation and preribosome assembly. Their shared abundance may therefore reflect a common requirement for maintaining transcriptional throughput, RNA quality and ribosome production in metabolically active tissues. This is a mechanistic hypothesis, not a demonstrated physical assembly or causal pathway; the reported STRING links and globally significant enrichment establish association and function, not directionality.

Web sources: https://www.nature.com/articles/s41467-024-47235-2

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): HNRNPR (0.80); STRING partners: HNRNPR (0.909)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is the most prominent RNA-remodeling candidate in the module. It is an ATP-dependent RNA and DNA–RNA duplex helicase, participates in alternative mRNA splicing and transcriptional regulation, and links to HNRNPR in STRING. It also contributes to the globally significant RNA-processing terms (GO:CC ribonucleoprotein complex; q_global = 0.0305) and (GO:BP RNA processing; q_global = 0.0454). Its large literature base and the web-reported evidence that DHX9 helps preserve intestinal stem-cell epithelial homeostasis by restraining harmful R-loops make it particularly relevant to a colon–liver RNA-maintenance interpretation.
- **Conclusion**: Established: DHX9 is a broadly expressed nuclear RNA helicase associated with RNA processing and with HNRNPR in this network. Hypothesis: DHX9 may act as a regulatory bridge between nuclear RNA surveillance and the nucleolar arm of the module, but that bridge is not directly demonstrated by the supplied data.

#### HNRNPR

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.86), DHX9 (0.80); STRING partners: DHX9 (0.909)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR is a nuclear heterogeneous nuclear ribonucleoprotein and a spliceosome-associated pre-mRNA processing factor. It is one of the four genes in both primary globally significant terms (GO:CC ribonucleoprotein complex; q_global = 0.0305) and (GO:BP RNA processing; q_global = 0.0454), and its STRING connection to DHX9 gives the module a coherent nuclear RNA-processing branch. Its disease associations include neurodevelopmental disorders, and its substantial literature supports an established role rather than a speculative annotation.
- **Conclusion**: Established: HNRNPR contributes to spliceosomal and mRNA processing functions and is central to the significant module annotations. Hypothesis: its co-abundance with DHX9 may report coordinated processing of structured or transcription-associated RNA in both tissues.

#### NOP56

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.81), PDCD11 (0.81); STRING partners: PDCD11 (0.997), RSL1D1 (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in colon, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP56 ribonucleoprotein. Nop56p is a yeast nucleolar protein that is part of a complex with the nucleolar proteins Nop58p and fibrillarin. Nop56p is required for assembly of the 60S ribosomal subunit and is involved in pre-rRNA processing. The protein encoded by this gene is similar in sequence to Nop56p and is also found in the nucleolus. Expansion of a GGCCTG repeat from 3-8 copies to 1500-2500 copies in an intron of th…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 36 (0.586); neurodegenerative disease (0.495); ovarian neoplasm (0.272); hereditary disease (0.193); cerebellar ataxia (0.121)
- **Europe PMC papers**: 1517
- **Why important**: NOP56 is a highly connected member of the nucleolar subnetwork and has strong STRING links to PDCD11 and RSL1D1. It belongs to both primary terms (GO:CC ribonucleoprotein complex; q_global = 0.0305) and (GO:BP RNA processing; q_global = 0.0454) and has supplementary support for preribosome formation, rRNA processing, small-subunit maturation and ribonucleoprotein complex biogenesis (STRING Component Preribosome; within-query FDR = 0.00062) (STRING COMPARTMENTS Preribosome; within-query FDR = 0.00068) (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 0.00098), (STRING COMPARTMENTS Nucleolus; within-query FDR = 0.0029), (STRING Process Ribonucleoprotein complex biogenesis; within-query FDR = 0.0071), (STRING Process rRNA processing; within-query FDR = 0.0083) and (STRING COMPARTMENTS Small-subunit processome; within-query FDR = 0.0156). Its established role in pre-rRNA processing and ribosomal-subunit assembly, together with its association with spinocerebellar ataxia type thirty-six, gives it strong functional and disease relevance.
- **Conclusion**: Established: NOP56 is a core nucleolar ribosome-biogenesis and rRNA-processing factor that anchors the module's preribosome interpretation. Hypothesis: NOP56 may be a principal abundance-sensitive driver of the shared colon–liver nucleolar signal.

#### PDCD11

- **Related proteins** (co-abundance neighbors): NOP56 (0.81); STRING partners: NOP56 (0.997), RSL1D1 (0.978)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim; IHC detected in colon, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 11. PDCD11 is a NF-kappa-B (NFKB1; 164011)-binding protein that colocalizes with U3 RNA (MIM 180710) in the nucleolus and is required for rRNA maturation and generation of 18S rRNA (Sweet et al., 2003 [PubMed 14624448]; Sweet et al., 2008 [PubMed 17654514]).[supplied by OMIM, Oct 2008].
- **Diseases (Open Targets)**: Back pain (0.277); insomnia (0.216); systemic lupus erythematosus (0.170); neoplasm (0.095); colorectal carcinoma (0.093)
- **Europe PMC papers**: 334
- **Why important**: PDCD11 is connected to NOP56 with very high STRING confidence and is part of both primary terms (GO:CC ribonucleoprotein complex; q_global = 0.0305) and (GO:BP RNA processing; q_global = 0.0454). The supplied annotation directly links it to U3 RNA, rRNA maturation and generation of mature small-subunit rRNA, while STRING places it in the preribosome and ninety-S preribosome context (STRING Component Preribosome; within-query FDR = 0.00062) (STRING COMPARTMENTS Preribosome; within-query FDR = 0.00068) (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 0.00098) and (5 supplementary STRING terms; within-query FDR 0.0071–0.0083). Its nucleolar-rim localization and reported association with colorectal carcinoma make it important for connecting core ribosome biogenesis with tissue-relevant disease biology.
- **Conclusion**: Established: PDCD11 is a nucleolar rRNA-maturation factor and a strong connector within the NOP56-centered subnetwork. Hypothesis: PDCD11 may help couple pre-rRNA maturation demand to the broader RNA-processing state represented by the module.

#### RSL1D1

- **Related proteins** (co-abundance neighbors): HNRNPR (0.86), NOP56 (0.81); STRING partners: NOP56 (0.991), PDCD11 (0.978)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in colon, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal L1 domain containing 1. Enables mRNA 3'-UTR binding activity and mRNA 5'-UTR binding activity. Involved in regulation of apoptotic process and regulation of cellular senescence. Acts upstream of or within regulation of protein localization. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: adolescent idiopathic scoliosis (0.219); hepatocellular carcinoma (0.099); neoplasm (0.099); colorectal carcinoma (0.096); insomnia (0.078)
- **Europe PMC papers**: 381
- **Why important**: RSL1D1 occupies a bridging position between HNRNPR and NOP56 in the co-abundance graph and has strong STRING links to NOP56 and PDCD11. It is included in the STRING-supported ribonucleoprotein, preribosome, nucleolar and rRNA-processing signals (15 supplementary STRING terms; within-query FDR 0.00015–0.0156), and its nucleolar-rim localization is consistent with that context. Its annotations include regulation of apoptosis, cellular senescence and protein localization, with reported associations including hepatocellular carcinoma and colorectal carcinoma.
- **Conclusion**: Established: RSL1D1 is a broadly detected nucleolar-associated gene embedded in the NOP56–PDCD11 STRING neighborhood. Hypothesis: it may serve as a coordination point linking nucleolar ribosome-biogenesis activity to cell-state programs, but the supplied evidence does not establish that it regulates the other module members.
