# Conserved co-abundance modules: bone_marrow and ovary

## Module 0

**Tissue pair**: bone_marrow and ovary  
**Genes (9)**: ACO2, AIFM1, ATP1A1, ATP2A2, ATP5PB, CANX, IMMT, UQCRC2, SEC22B

### Function

The strongest interpretation is a conserved membrane and mitochondrial energy-and-ion-handling module. The primary evidence is the globally corrected enrichment for cardiac muscle contraction (KEGG Cardiac muscle contraction - Homo sapiens (human); q_global = 0.0204) and for transmembrane transporter complex and transporter complex (GO:CC transmembrane transporter complex; q_global = 0.0373)(GO:CC transporter complex; q_global = 0.0439), driven by ATP1A1, ATP2A2, ATP5PB and UQCRC2. These terms support coordinated abundance of ion transport machinery together with oxidative-phosphorylation components, rather than a narrowly cardiac-only function. The mitochondrial annotations of ACO2, IMMT, UQCRC2 and ATP5PB add support for respiratory metabolism, while CANX and SEC22B indicate ER protein-folding and vesicle-trafficking context. The muscle-related signal should therefore be interpreted as a transport, calcium-handling and bioenergetic program that may be shared by particular cell states in the two tissues. No GO or KEGG term beyond (KEGG Cardiac muscle contraction - Homo sapiens (human); q_global = 0.0204) (GO:CC transmembrane transporter complex; q_global = 0.0373) (GO:CC transporter complex; q_global = 0.0439) should be treated as globally corrected primary evidence; the STRING terms are supplementary.

**Cell composition.** This is not a plasma-protein or secreted-protein module: HPA reports no secreted genes. All genes have low immune-cell specificity, and no blood-cell type is reported as enriched, arguing against a module composed mainly of blood cells. The module is instead composed largely of broadly cellular membrane, ER and mitochondrial proteins, with several tissue-enhanced signals in muscle or tongue and cell-type signals including oocytes, cardiomyocytes, parietal cells, enterocytes, hepatocytes and neutrophils. HPA detects protein for only part of the module in each relevant tissue, with other genes not detected or lacking data. Thus the shared bone-marrow and ovary signal could reflect common metabolic or organelle-rich cell states, technical abundance coupling, or shared cell populations, rather than a tissue-specific secreted or hematopoietic program.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Cardiac muscle contraction - Homo sapiens (human) | 0.0204 | ATP1A1, ATP2A2, UQCRC2 |
| GO:CC transmembrane transporter complex | 0.0373 | ATP1A1, ATP2A2, ATP5PB, UQCRC2 |
| GO:CC transporter complex | 0.0439 | ATP1A1, ATP2A2, ATP5PB, UQCRC2 |

### STRING and hu.MAP

STRING provides a partially connected, biologically coherent core. ACO2 is linked to UQCRC2; UQCRC2 is linked to ATP5PB and IMMT; ATP1A1 is linked to ATP2A2; ATP2A2 is linked to CANX; and CANX is linked to SEC22B. The strongest known relationships particularly support respiratory-chain and ATP-synthase context, sodium and calcium transport, and ER quality-control connections. STRING supplementary enrichment also points to cardiac muscle contraction, cardiac tissues, membrane complexes, mitochondrial inner membrane and cation-transporting ATPase complexes (13 supplementary STRING terms; within-query FDR 0.006–0.049), but these are not global enrichment tests. hu.MAP independently places ATP2A2, UQCRC2 and ATP5PB in one low-confidence complex (hu.MAP huMAP3_06247.1), and ATP1A1 with ATP2A2 in another higher-confidence complex (hu.MAP huMAP3_10473.1). These results show that several module relationships are already known physical or functional associations, while the complete cross-organelle module is not established by these resources.

**STRING interactions (score >= 0.7)**: 6 of 36 gene pairs: ACO2–UQCRC2 (0.879); ATP1A1–ATP2A2 (0.82); ATP2A2–CANX (0.849); ATP5PB–UQCRC2 (0.973); CANX–SEC22B (0.703); IMMT–UQCRC2 (0.811)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Cardiac muscle contraction (FDR = 0.006, 3 genes); TISSUES Left ventricle (FDR = 0.0067, 4 genes); TISSUES Right atrium (FDR = 0.0178, 3 genes); Component Membrane protein complex (FDR = 0.024, 6 genes); TISSUES Left atrium (FDR = 0.027, 3 genes); TISSUES Liver (FDR = 0.0279, 8 genes); Component Integral component of membrane (FDR = 0.0378, 7 genes); Component Organelle membrane (FDR = 0.0378, 8 genes); Component Melanosome (FDR = 0.0464, 3 genes); Component Cation-transporting ATPase complex (FDR = 0.0464, 2 genes); Component Inner mitochondrial membrane protein complex (FDR = 0.0464, 3 genes); Component Transmembrane transporter complex (FDR = 0.0464, 3 genes); Component Mitochondrial inner membrane (FDR = 0.049, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06247.1 (ATP2A2, UQCRC2, ATP5PB; 3/65); huMAP3_10473.1 (ATP1A1, ATP2A2; 2/24)

### Novelty

The module should not be called wholly novel: its central relationships and component functions are represented in STRING and hu.MAP, and the transporter, calcium-handling and mitochondrial biology is established. A potentially novel aspect is the coordinated co-abundance of this particular set across bone marrow and ovary, especially the combination of plasma-membrane transport, ER handling, mitochondrial respiration and vesicle trafficking. That claim remains a hypothesis rather than a demonstrated discovery because absence of a complete matching module from STRING or hu.MAP does not prove novelty, and co-abundance can arise from shared cell composition or organelle content. Independent replication, cell-type-resolved analysis and comparison with published cross-tissue co-abundance modules would be needed to establish whether the tissue-pair module is new.

**Hypothesis.** Hypothesis: in a shared bone-marrow and ovary cellular context, cells with elevated oxidative phosphorylation and mitochondrial structural capacity co-abundantly increase sodium and calcium transport machinery and ER quality-control or trafficking proteins. ATP1A1 and ATP2A2 could coordinate electrochemical and calcium gradients, while UQCRC2, ATP5PB, ACO2 and IMMT could support respiratory ATP production and mitochondrial organization; CANX and SEC22B could maintain folding and membrane traffic. This may reflect a metabolically demanding or differentiation-associated cell state, but it should not yet be interpreted as proof of cardiac tissue contamination or a direct regulatory pathway.

### Important genes

#### ATP2A2

- **Related proteins** (co-abundance neighbors): ATP1A1 (0.86); STRING partners: ATP1A1 (0.82), CANX (0.849)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_06247.1, huMAP3_10473.1
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darie…
- **Diseases (Open Targets)**: Darier disease (0.823); acrokeratosis verruciformis (0.663); neurodegenerative disease (0.507); hereditary disease (0.416); schizophrenia (0.406)
- **Europe PMC papers**: 9327
- **Why important**: ATP2A2 is a key annotated calcium pump and is one of the two module genes in the globally corrected transporter terms and cardiac-muscle term (KEGG Cardiac muscle contraction - Homo sapiens (human); q_global = 0.0204)(GO:CC transmembrane transporter complex; q_global = 0.0373)(GO:CC transporter complex; q_global = 0.0439). It connects by STRING to ATP1A1 and CANX and appears in both hu.MAP complexes (hu.MAP huMAP3_06247.1)(hu.MAP huMAP3_10473.1). Its HPA profile includes heart muscle, skeletal muscle, tongue and cardiomyocytes, and it has a substantial literature record plus a strong disease association with Darier disease.
- **Conclusion**: Established: ATP2A2 provides the clearest calcium-handling anchor and has direct network, complex and disease evidence. Hypothesis: its co-abundance with mitochondrial genes marks coordinated calcium demand and energy supply in the shared module.

#### ATP1A1

- **Related proteins** (co-abundance neighbors): ATP2A2 (0.86), ACO2 (0.82), CANX (0.82), ATP5PB (0.80); STRING partners: ATP2A2 (0.82)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10473.1
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 is the sodium-potassium pump alpha subunit and is centrally connected within the module to ATP2A2, ACO2, CANX and ATP5PB. It is present in all primary GO or KEGG terms (KEGG Cardiac muscle contraction - Homo sapiens (human); q_global = 0.0204)(GO:CC transmembrane transporter complex; q_global = 0.0373)(GO:CC transporter complex; q_global = 0.0439), in multiple supplementary membrane and transporter terms, and in hu.MAP complex (hu.MAP huMAP3_10473.1). Its broad cell-type profile and extensive literature and disease associations make it an important functional and interpretive anchor.
- **Conclusion**: Established: ATP1A1 supports a membrane electrochemical-gradient mechanism and is one of the best-supported module genes by annotations and network position. Hypothesis: its coordinated abundance with ATP2A2 may couple sodium gradients to calcium homeostasis in the shared cell state.

#### UQCRC2

- **Related proteins** (co-abundance neighbors): IMMT (0.82); STRING partners: ACO2 (0.879), ATP5PB (0.973), IMMT (0.811)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: huMAP3_06247.1
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase core protein 2. The protein encoded by this gene is located in the mitochondrion, where it is part of the ubiquinol-cytochrome c reductase complex (also known as complex III). This complex constitutes a part of the mitochondrial respiratory chain. Defects in this gene are a cause of mitochondrial complex III deficiency nuclear type 5. [provided by RefSeq, Jul 2015].
- **Diseases (Open Targets)**: mitochondrial complex III deficiency (0.732); neurodegenerative disease (0.423); mitochondrial disease (0.312); gastric cancer (0.085); adrenoleukodystrophy (0.075)
- **Europe PMC papers**: 3297
- **Why important**: UQCRC2 is a core component of mitochondrial respiratory complex III and participates in every primary term (KEGG Cardiac muscle contraction - Homo sapiens (human); q_global = 0.0204)(GO:CC transmembrane transporter complex; q_global = 0.0373)(GO:CC transporter complex; q_global = 0.0439). It connects in STRING to ACO2, ATP5PB and IMMT, has the strongest respiratory-chain support in the supplementary evidence, and is a member of hu.MAP complex (hu.MAP huMAP3_06247.1). Its mitochondrial disease association and extensive literature make it a strong bioenergetic representative.
- **Conclusion**: Established: UQCRC2 anchors the oxidative-phosphorylation interpretation and links the mitochondrial portion of the module to known respiratory and ATP-synthase relationships. Hypothesis: it supplies the respiratory capacity needed to sustain the module's ion-transport burden.

#### ACO2

- **Related proteins** (co-abundance neighbors): SEC22B (0.84), IMMT (0.84), ATP1A1 (0.82), CANX (0.81); STRING partners: UQCRC2 (0.879)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aconitase 2. The protein encoded by this gene belongs to the aconitase/IPM isomerase family. It is an enzyme that catalyzes the interconversion of citrate to isocitrate via cis-aconitate in the second step of the TCA cycle. This protein is encoded in the nucleus and functions in the mitochondrion. It was found to be one of the mitochondrial matrix proteins that are preferentially degraded by the serine proteas…
- **Diseases (Open Targets)**: infantile cerebellar-retinal degeneration (0.814); optic atrophy 9 (0.693); autosomal dominant optic atrophy, classic form (0.619); optic atrophy (0.601); mitochondrial disease (0.505)
- **Europe PMC papers**: 3559
- **Why important**: ACO2 is a mitochondrial TCA-cycle enzyme with a relatively central position in the co-abundance graph, connecting to SEC22B, IMMT, ATP1A1 and CANX. STRING links it to UQCRC2 and places it in cardiac and liver tissue-related supplementary signals (STRING TISSUES Left ventricle; within-query FDR = 0.0067)(STRING TISSUES Right atrium; within-query FDR = 0.0178)(STRING TISSUES Left atrium; within-query FDR = 0.027)(STRING TISSUES Liver; within-query FDR = 0.0279). It has a large literature record and notable mitochondrial and optic-atrophy disease associations.
- **Conclusion**: Established: ACO2 supports the interpretation of mitochondrial carbon metabolism and is a bridge between metabolic and membrane or ER-associated module members. Hypothesis: its abundance may report energetic substrate flux that is coordinated with ion-gradient maintenance.

#### CANX

- **Related proteins** (co-abundance neighbors): SEC22B (0.84), ATP1A1 (0.82), ACO2 (0.81); STRING partners: ATP2A2 (0.849), SEC22B (0.703)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is an ER calcium-binding chaperone involved in glycoprotein folding, assembly and ER quality control. It connects to SEC22B and ATP1A1 in the module and to ATP2A2 and SEC22B in STRING, while supplementary terms place it in membrane and organelle-membrane contexts (STRING Component Membrane protein complex; within-query FDR = 0.024)(STRING TISSUES Liver; within-query FDR = 0.0279)(STRING Component Integral component of membrane; within-query FDR = 0.0378)(STRING Component Organelle membrane; within-query FDR = 0.0378)(STRING Component Melanosome; within-query FDR = 0.0464). It is detected in both bone marrow and ovary by HPA and has a substantial literature and disease-association record.
- **Conclusion**: Established: CANX supplies the ER protein-quality-control and calcium-sensitive folding component of the module. Hypothesis: CANX may couple ER calcium handling and secretory quality control to the mitochondrial and plasma-membrane systems, although the co-abundance data do not establish direct regulation.

## Module 1

**Tissue pair**: bone_marrow and ovary  
**Genes (9)**: COPB1, DHX9, ADAR, HNRNPR, PSMD13, CAD, SUPT16H, SNRNP200, EFTUD2

### Function

The most coherent interpretation is a broadly expressed nuclear RNA-processing and pre-mRNA splicing module, with additional links to transcriptional regulation, pyrimidine biosynthesis, proteasomal turnover, and vesicle trafficking. The spliceosome interpretation is supported by the functions of SNRNP200, EFTUD2, HNRNPR, DHX9, and ADAR, and by the supplementary STRING terms for mRNA processing, spliceosomal complex, and mRNA splicing (STRING Keyword mRNA processing; within-query FDR = 0.0094)(STRING COMPARTMENTS Spliceosomal complex; within-query FDR = 0.0231)(STRING Keyword mRNA splicing; within-query FDR = 0.0446). The network also contains a connected transcription and nucleotide biosynthesis branch involving SUPT16H and CAD, plus a proteostasis and trafficking branch involving PSMD13 and COPB1. No GO/KEGG term passed global correction, so the functional interpretation should be treated as biologically coherent but not as globally validated by GO/KEGG enrichment.

**Cell composition.** This does not resemble a plasma-protein or secreted-protein module: the module has no secreted genes, and the proteins are predominantly intracellular, especially nuclear or nucleolar. HPA reports low tissue specificity for all genes, low immune-cell specificity for all genes, and no recurrent enriched blood-cell category. HPA detects the proteins in bone marrow broadly and detects most of them in ovary, while the absence of ovary detection for SNRNP200 and PSMD13 does not by itself establish tissue restriction. The cell-type-enhanced annotations for SUPT16H, PSMD13, and ADAR point respectively to erythrocyte progenitors, syncytiotrophoblasts, and neutrophils, but these are isolated signals rather than evidence that the whole module is blood-cell specific. Overall, the shared module is more consistent with broadly required cellular machinery, possibly influenced by shared proliferative or transcriptionally active cell populations, than with a secreted or specialized tissue program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a compact core centered on RNA metabolism. ADAR is strongly connected to DHX9, DHX9 connects to HNRNPR and SNRNP200, and EFTUD2 is very strongly connected to SNRNP200. These relationships are concordant with RNA editing, RNA helicase activity, heterogeneous nuclear ribonucleoprotein function, and spliceosomal activity. The remaining co-abundance edges, including CAD with SNRNP200, PSMD13, SUPT16H, and ADAR, and PSMD13 with COPB1, are not represented by high-confidence STRING partners in the fact sheet and may reflect co-regulation or shared cellular state rather than direct physical interaction. hu.MAP repeatedly places SNRNP200 and EFTUD2 together in spliceosomal or related complexes (hu.MAP huMAP3_00960.1)(hu.MAP huMAP3_07622.1)(hu.MAP huMAP3_08501.1)(hu.MAP huMAP3_09504.1)(hu.MAP huMAP3_09945.1)(hu.MAP huMAP3_08980.1). hu.MAP also places HNRNPR and ADAR together in an RNA-binding complex (hu.MAP huMAP3_10625.1). Thus, part of the module recapitulates known molecular machinery, while the complete co-abundance pattern is broader than the known physical-complex structure.

**STRING interactions (score >= 0.7)**: 4 of 36 gene pairs: ADAR–DHX9 (0.922); DHX9–HNRNPR (0.909); DHX9–SNRNP200 (0.784); EFTUD2–SNRNP200 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword mRNA processing (FDR = 0.0094, 5 genes); COMPARTMENTS Spliceosomal complex (FDR = 0.0231, 4 genes); Keyword mRNA splicing (FDR = 0.0446, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00960.1 (SNRNP200, EFTUD2; 2/8); huMAP3_07622.1 (SNRNP200, EFTUD2; 2/9); huMAP3_08501.1 (SNRNP200, EFTUD2; 2/47); huMAP3_09504.1 (SNRNP200, EFTUD2; 2/51); huMAP3_10625.1 (HNRNPR, ADAR; 2/57); huMAP3_09945.1 (SNRNP200, EFTUD2; 2/61); huMAP3_08980.1 (SNRNP200, EFTUD2; 2/97)

### Novelty

The exact shared bone-marrow and ovary co-abundance module may be a new observation, because the fact sheet does not identify a prior report of this tissue-pair module. However, it should not be presented as a newly discovered molecular complex or as a novel spliceosome mechanism. The central SNRNP200-EFTUD2 relationship, the association of DHX9 with ADAR and HNRNPR, and the participation of SNRNP200, EFTUD2, HNRNPR, and ADAR in hu.MAP or STRING-supported RNA-processing machinery are already established. The absence of some module edges from STRING or hu.MAP is compatible with co-abundance, context dependence, incomplete databases, or indirect regulation and is not evidence of novelty by itself. The defensible novelty claim is therefore the tissue-shared co-abundance pattern and its integration of spliceosomal, transcriptional, nucleotide biosynthetic, proteasomal, and trafficking genes.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in bone marrow and ovary in which active transcription and cell production require coordinated pre-mRNA processing, RNA helicase and editing activity, chromatin-compatible transcription, nucleotide supply, protein quality control, and intracellular trafficking. SNRNP200 and EFTUD2 could form the spliceosomal core, with DHX9, HNRNPR, and ADAR coordinating RNA remodeling, RNA binding, and editing. CAD and SUPT16H could support the biosynthetic and transcriptional demands of this state, while PSMD13 and COPB1 could represent linked proteostasis and membrane-trafficking requirements. This is a mechanistic model rather than a demonstrated causal pathway; it requires validation with cell-composition controls, perturbation experiments, and direct measurement of transcript processing.

### Important genes

#### SNRNP200

- **Related proteins** (co-abundance neighbors): CAD (0.88), EFTUD2 (0.84); STRING partners: DHX9 (0.784), EFTUD2 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is a central connector in the module and has direct STRING support with EFTUD2 and DHX9. It is a U5 snRNP helicase and is assigned spliceosomal assembly and conformational-change functions. It occurs with EFTUD2 across multiple hu.MAP complexes (hu.MAP huMAP3_00960.1)(hu.MAP huMAP3_07622.1)(hu.MAP huMAP3_08501.1)(hu.MAP huMAP3_09504.1)(hu.MAP huMAP3_09945.1)(hu.MAP huMAP3_08980.1), and its disease associations include retinitis pigmentosa and inherited retinal dystrophy. Its network position and direct spliceosome evidence make it a strong anchor for the module's core interpretation.
- **Conclusion**: Established evidence supports SNRNP200 as a core spliceosomal component and as one of the best-supported functional anchors of the module. The hypothesis that its co-abundance links spliceosome activity to the broader tissue-shared state remains to be tested.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.84); STRING partners: SNRNP200 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_08980.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 has a direct, very strong STRING relationship with SNRNP200 and appears with SNRNP200 in multiple hu.MAP complexes (hu.MAP huMAP3_00960.1)(hu.MAP huMAP3_07622.1)(hu.MAP huMAP3_08501.1)(hu.MAP huMAP3_09504.1)(hu.MAP huMAP3_09945.1)(hu.MAP huMAP3_08980.1). It is a spliceosomal GTPase involved in tri-snRNP assembly and spliceosome conformational change. Its association with mandibulofacial dysostosis with microcephaly and developmental disorders illustrates the biological importance of accurate spliceosome function, despite its limited local degree in the co-abundance graph.
- **Conclusion**: Established evidence identifies EFTUD2 as a spliceosome component that reinforces the SNRNP200-centered core. The module data do not establish that EFTUD2 drives the shared tissue pattern or that it has a tissue-specific role here.

#### DHX9

- **Related proteins** (co-abundance neighbors): HNRNPR (0.92), SUPT16H (0.90); STRING partners: ADAR (0.922), HNRNPR (0.909), SNRNP200 (0.784)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 connects to HNRNPR and SNRNP200 in STRING and to ADAR through a high-confidence RNA-metabolism relationship. It is an ATP-dependent RNA and DNA-RNA helicase with roles in alternative splicing, transcriptional regulation, and interferon-related processes. It is also annotated for osteoblast differentiation and has disease associations involving intellectual development and neurodegeneration. Its position bridges the spliceosomal core and the RNA-editing and RNA-binding branch.
- **Conclusion**: Established evidence supports DHX9 as a multifunctional RNA helicase linking splicing and broader RNA regulation. Its proposed role as the principal bridge between these processes in this tissue-shared module is a hypothesis, not a demonstrated causal relationship.

#### ADAR

- **Related proteins** (co-abundance neighbors): CAD (0.81); STRING partners: DHX9 (0.922)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: huMAP3_10625.1
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR is the module's RNA-editing enzyme and is connected to DHX9 in STRING. It participates in the hu.MAP RNA-binding complex containing HNRNPR (hu.MAP huMAP3_10625.1) and is associated with RNA processing, adenosine-to-inosine editing, antiviral responses, and Aicardi-Goutieres syndrome. Its cell-type-enhanced HPA signal in neutrophils is notable but does not establish immune specificity because the overall module has low immune-cell specificity.
- **Conclusion**: Established evidence supports ADAR as an RNA-editing and RNA-processing component that may connect splicing-related machinery with transcript surveillance or antiviral regulation. A coordinated editing role in the shared bone-marrow and ovary module remains hypothetical.

#### HNRNPR

- **Related proteins** (co-abundance neighbors): DHX9 (0.92); STRING partners: DHX9 (0.909)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR is directly connected to DHX9 and participates with ADAR in hu.MAP complex (hu.MAP huMAP3_10625.1). It is a heterogeneous nuclear ribonucleoprotein involved in spliceosomal mRNA processing and transcript transport, and it has disease associations involving neurodevelopment, skeletal abnormalities, intellectual disability, and seizures. Although it has a peripheral position in the graph, its molecular function provides an important RNA-binding link between the helicase and editing branches.
- **Conclusion**: Established evidence supports HNRNPR as an RNA-binding and pre-mRNA-processing factor that strengthens the module's RNA-regulatory interpretation. The data do not show that HNRNPR is a unique driver of the tissue-shared co-abundance pattern.

## Module 2

**Tissue pair**: bone_marrow and ovary  
**Genes (8)**: DDX5, MATR3, PSMC4, PSMC2, CCT5, CCT3, CCT7, CCT8

### Function

The strongest interpretation is a conserved intracellular proteostasis module centered on the CCT/TRiC chaperonin. The CCT subunits CCT3, CCT5, CCT7 and CCT8 form a coherent core supported by the global GO/KEGG evidence for the chaperonin-containing T-complex, ATP-dependent protein folding, unfolded-protein binding, protein stabilization and protein-folding chaperone activity (GO:CC chaperonin-containing T-complex; q_global = 9.93e-07), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.00018), (GO:CC protein folding chaperone complex; q_global = 0.000294), (GO:MF protein folding chaperone; q_global = 0.00127), (GO:MF unfolded protein binding; q_global = 0.00348), (GO:BP protein stabilization; q_global = 0.0297), (GO:BP protein folding; q_global = 0.0459). The broader module also contains the proteasome ATPases PSMC2 and PSMC4, the RNA helicase DDX5 and the nuclear RNA-associated protein MATR3. Thus, the network links protein folding, regulated protein turnover and RNA/nuclear functions. The telomerase, Cajal-body, DNA-biosynthetic and fertilization terms are globally significant (15 globally significant GO/KEGG terms, q_global 9.93e-07–2.93e-05; see the table), (GO:BP regulation of telomere maintenance via telomerase; q_global = 9.78e-05) (GO:BP regulation of telomere maintenance via telomere lengthening; q_global = 0.000134), (GO:BP positive regulation of DNA biosynthetic process; q_global = 0.00018), (GO:BP RNA-templated DNA biosynthetic process; q_global = 0.000294) (GO:BP telomere maintenance via telomerase; q_global = 0.000294), (GO:BP telomere maintenance via telomere lengthening; q_global = 0.000369), (GO:BP single fertilization; q_global = 0.00046), (GO:BP regulation of DNA biosynthetic process; q_global = 0.000812) (GO:BP positive regulation of telomere maintenance; q_global = 0.000943), (9 globally significant GO/KEGG terms, q_global 0.00192–0.011; see the table), but they are driven largely by the same CCT subunit subset and should not by themselves be interpreted as evidence that this entire module is a specialized telomerase or fertilization pathway. A parsimonious functional label is CCT-mediated proteostasis coupled to proteasomal maintenance and RNA-associated nuclear processes.

**Cell composition.** This is not a plasma or secreted-protein module: HPA reports no secreted genes, and all module proteins are detected in both bone marrow and ovary. All genes have low tissue specificity, and the module has low immune-cell specificity, arguing against a simple blood-cell marker interpretation. Several genes are cell-type enhanced in reproductive or placental populations, including spermatocytes, spermatids, oocytes and syncytiotrophoblasts, while MATR3 is enhanced in several epithelial, endocrine and progenitor populations. The overall pattern is therefore more consistent with broadly expressed, intracellular housekeeping and proteostasis machinery that can be prominent in particular proliferative or specialized cell states. Shared detection in bone marrow and ovary may reflect common cellular demands, such as protein quality control and macromolecular turnover, rather than a tissue-specific secretory program.

**GO/KEGG enrichment**: 56 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chaperonin-containing T-complex | 9.93e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 9.93e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 9.93e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to Cajal body | 3.53e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 3.53e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 3.53e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 3.53e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 3.53e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 3.53e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 3.53e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 3.53e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 3.53e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP binding of sperm to zona pellucida | 8.44e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 1.66e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP sperm-egg recognition | 1.66e-05 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING provides strong prior support for a CCT subnetwork: the pairwise relationships among CCT3, CCT5, CCT7 and CCT8 are very strong (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 1.1e-06) (STRING Component Chaperonin-containing T-complex; within-query FDR = 2.67e-06) (STRING COMPARTMENTS Chaperonin-containing T-complex; within-query FDR = 2.84e-06), (6 supplementary STRING terms; within-query FDR 4.4e-06–4.4e-06), and the STRING functional results identify the TCP-1 chaperonin family, CCT-mediated actin folding, cellular proteostasis and biosynthetic target folding (14 supplementary STRING terms; within-query FDR 1.1e-06–1.32e-05). STRING also supports the PSMC2–PSMC4 proteasome relationship and links CCT8 with PSMC2, while the DDX5–MATR3 relationship is independently supported. hu.MAP identifies multiple complexes containing the four CCT subunits (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1) and multiple proteasome assemblies containing PSMC2 and PSMC4 (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). These results indicate that the module contains known molecular complexes rather than an arbitrary set of correlated genes. The co-abundance edges involving CCT proteins, proteasome ATPases, DDX5 and MATR3 may therefore represent coordinated activity of established complexes, cross-complex coupling, or shared abundance regulation; they should not automatically be interpreted as direct physical binding.

**STRING interactions (score >= 0.7)**: 9 of 28 gene pairs: CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999); CCT8–PSMC2 (0.733); DDX5–MATR3 (0.894); PSMC2–PSMC4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam TCP-1/cpn60 chaperonin family (FDR = 1.1e-06, 4 genes); Component Chaperonin-containing T-complex (FDR = 2.67e-06, 4 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 2.84e-06, 4 genes); Function ATP hydrolysis activity (FDR = 3.21e-06, 7 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 4.4e-06, 4 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 4.4e-06, 4 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 4.4e-06, 4 genes); InterPro GroEL-like apical domain superfamily (FDR = 4.4e-06, 4 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 4.4e-06, 4 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 4.4e-06, 4 genes); RCTM Folding of actin by CCT/TriC (FDR = 7e-06, 4 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis (FDR = 8.44e-06, 4 genes); RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding (FDR = 9.14e-06, 4 genes); RCTM Association of TriC/CCT with target proteins during biosynthesis (FDR = 1.32e-05, 4 genes); Process Binding of sperm to zona pellucida (FDR = 1.68e-05, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_05064.1 (PSMC2, PSMC4; 2/31); huMAP3_09656.1 (PSMC2, PSMC4; 2/64); huMAP3_13725.1 (PSMC2, PSMC4; 2/69)

### Novelty

The molecular components are not novel as complexes: the CCT core, the PSMC2–PSMC4 proteasome pair and the DDX5–MATR3 relationship are already represented by STRING or hu.MAP evidence. The potentially novel observation is the conservation of this particular co-abundance configuration across bone marrow and ovary, especially the coordinated placement of CCT, proteasome and RNA-associated genes. However, the fact sheet does not establish that this cross-tissue module has not been reported previously, and absence of a complete matching module from STRING or hu.MAP would not prove novelty because those resources describe physical interactions and complexes rather than every tissue-specific co-abundance pattern. The appropriate conclusion is that the module may provide a useful cross-tissue co-abundance observation, but a claim of a new biological mechanism requires comparison with published coexpression, proteomic and tissue-network studies.

**Hypothesis.** Hypothesis: in both bone marrow and ovary, a shared cellular state increases demand for CCT/TRiC-mediated folding of newly synthesized proteins and for proteasomal removal of damaged or obsolete proteins. Coordinated RNA handling by DDX5 and MATR3 may regulate production, processing or stabilization of transcripts encoding proteins that enter this proteostasis system. The CCT-associated annotations involving telomerase RNA and Cajal-body localization suggest a possible connection to nuclear RNA organization and telomere maintenance, but this is a mechanistic hypothesis rather than a demonstrated direct activity of the full module. The reproductive-cell enrichment in HPA may indicate that this proteostasis–RNA axis is particularly important during highly specialized or proliferative cell states, while the lack of tissue and immune specificity supports a general cellular maintenance program.

### Important genes

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT8 (0.92), CCT3 (0.88), CCT7 (0.87), PSMC2 (0.86), DDX5 (0.84); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is the highest-connectivity and highest-strength node in the module. It is part of the strongly supported CCT3–CCT5–CCT7–CCT8 chaperonin core, appears in the global enrichment terms spanning chaperonin assembly, protein folding, protein stabilization, ATP-dependent activity and telomerase/Cajal-body annotations (56 globally significant GO/KEGG terms, q_global 9.93e-07–0.0483; see the table), and is present in several hu.MAP CCT complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). Its established function is ATP-dependent folding of proteins including actin and tubulin. The fact sheet also associates it with hereditary sensory and autonomic neuropathy with spastic paraplegia and neurodegenerative disease, and it has substantial literature coverage.
- **Conclusion**: Established evidence supports CCT5 as a central structural and functional component of the module's proteostasis core. Its network position makes it a strong candidate for coordinating the module, but the data do not establish that CCT5 specifically drives the cross-tissue conservation or directly regulates telomerase.

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT5 (0.88), CCT8 (0.84), PSMC2 (0.83); STRING partners: CCT5 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a core CCT subunit with strong STRING relationships to CCT5, CCT7 and CCT8 and membership in the same hu.MAP CCT complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It contributes to nearly all of the globally significant CCT-associated terms, including chaperonin-containing T-complex, protein folding, protein stabilization, Cajal-body localization and telomere-maintenance annotations (56 globally significant GO/KEGG terms, q_global 9.93e-07–0.0483; see the table). It is broadly detected in both tissues and has substantial literature coverage. The fact sheet links it to neurodevelopmental, neurodegenerative, osteoarthritis and autoimmune disease associations.
- **Conclusion**: Established evidence identifies CCT3 as a core component of the chaperonin interpretation and a highly plausible contributor to shared proteostasis demand. Disease associations are supportive of biological importance but do not demonstrate a disease mechanism for this module. Any direct role in telomere maintenance remains inferential from the enrichment annotations.

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT5 (0.92), CCT7 (0.85), CCT3 (0.84), MATR3 (0.81); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999), PSMC2 (0.733)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is a core CCT subunit with strong STRING links to the other CCT members and an additional relationship to PSMC2. It is represented in the global CCT, protein-folding, Cajal-body, telomere-maintenance, cell-recognition and zona-pellucida-related terms (20 globally significant GO/KEGG terms, q_global 9.93e-07–0.000134; see the table), (5 globally significant GO/KEGG terms, q_global 0.000294–0.000369; see the table), (GO:BP single fertilization; q_global = 0.00046), (11 globally significant GO/KEGG terms, q_global 0.000943–0.011; see the table), (4 globally significant GO/KEGG terms, q_global 0.0174–0.0297; see the table), (GO:BP protein folding; q_global = 0.0459). HPA shows enhancement in oocytes, which is notable for an ovary-sharing module, although its overall tissue specificity is low. It has substantial literature coverage and reported associations with several cancers.
- **Conclusion**: Established evidence supports CCT8 as a core chaperonin component and a possible bridge between the CCT subnetwork and proteasomal machinery through its network relationship with PSMC2. The oocyte signal is biologically suggestive but does not prove ovary-specific function. The reproductive and telomerase interpretations should remain hypotheses beyond the established folding role.

#### PSMC2

- **Related proteins** (co-abundance neighbors): CCT5 (0.86), PSMC4 (0.86), CCT3 (0.83), DDX5 (0.80); STRING partners: CCT8 (0.733), PSMC4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is a central connector between the CCT-rich portion of the module and the proteasome portion. It is linked in the co-abundance network to CCT5, CCT3, DDX5 and PSMC4, has STRING support with PSMC4 and CCT8, and is present in hu.MAP proteasome complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). Its global GO evidence supports ATP-dependent activity, proteasome-activating activity and nucleotide-binding functions (GO:MF ATP hydrolysis activity; q_global = 4.26e-05), (GO:MF ATP-dependent activity; q_global = 0.000255), (GO:MF ribonucleoside triphosphate phosphatase activity; q_global = 0.000438), (GO:MF pyrophosphatase activity; q_global = 0.000747) (GO:MF hydrolase activity, acting on acid anhydrides; q_global = 0.000766) (GO:MF hydrolase activity, acting on acid anhydrides, in phosphorus-containing anhydrides; q_global = 0.000766), (5 globally significant GO/KEGG terms, q_global 0.016–0.028; see the table), (5 globally significant GO/KEGG terms, q_global 0.0409–0.0483; see the table). The fact sheet associates it with plasma cell myeloma, mantle cell lymphoma, neoplasm, HIV-related disease and amyloidosis.
- **Conclusion**: Established evidence supports PSMC2 as the module's proteasomal remodeling and degradation component, providing a credible functional link between protein folding and protein disposal. Its disease associations are consistent with importance in proteostasis and hematologic biology, but the module does not establish a specific role in any listed disease.

#### DDX5

- **Related proteins** (co-abundance neighbors): CCT5 (0.84), CCT7 (0.83), PSMC2 (0.80); STRING partners: MATR3 (0.894)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 has a bridging position connecting CCT5, CCT7 and PSMC2, while STRING independently supports its relationship with MATR3. Its established function is that of a DEAD-box RNA helicase and adaptor involved in RNA structure remodeling, transcriptional co-regulation, splicing and small noncoding RNA processing. It contributes to the globally significant ATP-dependent activity and nucleotide-binding terms (GO:MF ATP hydrolysis activity; q_global = 4.26e-05), (GO:MF ATP-dependent activity; q_global = 0.000255), (GO:MF ribonucleoside triphosphate phosphatase activity; q_global = 0.000438), (GO:MF pyrophosphatase activity; q_global = 0.000747) (GO:MF hydrolase activity, acting on acid anhydrides; q_global = 0.000766) (GO:MF hydrolase activity, acting on acid anhydrides, in phosphorus-containing anhydrides; q_global = 0.000766), (GO:MF ATP binding; q_global = 0.016) (GO:MF adenyl ribonucleotide binding; q_global = 0.0163), (GO:MF adenyl nucleotide binding; q_global = 0.028), (4 globally significant GO/KEGG terms, q_global 0.045–0.0483; see the table). It has the largest literature volume among the listed genes and is associated with viral disease and colorectal malignancy in the fact sheet.
- **Conclusion**: Established evidence supports DDX5 as the module's RNA-processing and nuclear regulatory component rather than as a CCT subunit. Its position suggests coupling between RNA handling and proteostasis, but whether DDX5 functionally regulates the CCT or proteasome components in these tissues is an untested hypothesis.

## Module 3

**Tissue pair**: bone_marrow and ovary  
**Genes (11)**: FASN, HSPH1, EIF4G1, PAICS, CTPS1, RPL3, RUVBL2, SF3A1, SRP68, SRP72, QARS1

### Function

The primary evidence is (GO:MF signal recognition particle binding; q_global = 0.0295), where SRP68 and SRP72 support signal recognition particle binding. Together with the supplementary translation and SRP-dependent cotranslational targeting terms (STRING RCTM Translation; within-query FDR = 0.0222) and (STRING RCTM SRP-dependent cotranslational protein targeting to membrane; within-query FDR = 0.0232), the module is most consistent with coordinated translation, RNA-associated processing, and delivery of selected nascent proteins to the endoplasmic reticulum. EIF4G1 supports translation initiation, RPL3 supports ribosome function, QARS1 supports aminoacyl-tRNA charging, SF3A1 supports pre-mRNA splicing, PAICS and CTPS1 support nucleotide production, FASN supports lipid synthesis, and HSPH1 supports protein quality control. RUVBL2 may connect the program to ATP-dependent genome-maintenance functions. The module therefore appears to represent a broad biosynthetic and proteostasis state rather than a narrowly tissue-specific pathway. (GO:MF signal recognition particle binding; q_global = 0.0295) is the strongest functional evidence; the remaining pathway interpretations are supplementary.

**Cell composition.** The module contains no secreted genes and is composed predominantly of intracellular proteins. Most genes have low tissue specificity, and most have low immune-cell specificity; one is not detected in immune cells. This favors a broadly expressed, housekeeping-like biosynthetic program rather than a dedicated blood-cell signature. The blood, lymphocyte, and lymphoblast signals (STRING TISSUES Blood; within-query FDR = 0.005), (STRING TISSUES Lymphocyte; within-query FDR = 0.0166), and (STRING TISSUES Lymphoblast; within-query FDR = 0.0236) may reflect general translational and metabolic machinery in those samples. Reproductive-gland signals (STRING TISSUES Male reproductive gland; within-query FDR = 0.02), (STRING TISSUES Female reproductive gland; within-query FDR = 0.0297), and (STRING TISSUES Internal male genital organ; within-query FDR = 0.0315) and cell-type enrichments involving spermatids, epithelial cells, and trophoblasts do not establish reproductive-tissue specificity. HPA protein detection is broadly compatible with the shared tissues, although FASN and HSPH1 show weaker or asymmetric tissue detection.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF signal recognition particle binding | 0.0295 | SRP68, SRP72 |

### STRING and hu.MAP

STRING supports a compact SRP and ribosome-centered core. SRP68–SRP72 is strongly supported, and both SRP subunits connect to RPL3; QARS1 also connects to RPL3. These known relationships reinforce the translation and cotranslational-targeting interpretation, especially with (STRING RCTM Translation; within-query FDR = 0.0222) and (STRING RCTM SRP-dependent cotranslational protein targeting to membrane; within-query FDR = 0.0232). The other co-abundance edges are not among the reported high-confidence STRING links, so co-abundance should not be interpreted as physical binding. No hu.MAP complex contains multiple module members. The module therefore has a known mechanistic core but a broader, partly unresolved co-regulated neighborhood.

**STRING interactions (score >= 0.7)**: 4 of 55 gene pairs: QARS1–RPL3 (0.749); RPL3–SRP68 (0.959); RPL3–SRP72 (0.936); SRP68–SRP72 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Blood (FDR = 0.005, 9 genes); TISSUES Lymphocyte (FDR = 0.0166, 6 genes); TISSUES Male reproductive gland (FDR = 0.02, 9 genes); RCTM Translation (FDR = 0.0222, 5 genes); RCTM SRP-dependent cotranslational protein targeting to membrane (FDR = 0.0232, 3 genes); TISSUES Lymphoblast (FDR = 0.0236, 4 genes); TISSUES Female reproductive gland (FDR = 0.0297, 9 genes); TISSUES Internal male genital organ (FDR = 0.0315, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is not a wholly new translation or SRP mechanism: the SRP68–SRP72 relationship and the RPL3 connections are already represented in STRING, and the functions of the component genes are established. A potentially novel aspect is the shared bone-marrow and ovary co-abundance configuration joining the SRP and ribosome core with translation initiation, RNA processing, nucleotide and lipid biosynthesis, chaperoning, and genome maintenance. That claim remains provisional because the fact sheet provides no independent replication, perturbation experiment, or comparison with other module architectures. Absence from hu.MAP or absence of a STRING edge does not prove novelty.

**Hypothesis.** Hypothesis: the module marks a demand-responsive intracellular biosynthetic state in which translational capacity and cotranslational ER targeting are coordinated with RNA processing, amino-acid charging, nucleotide and lipid production, and chaperone-mediated quality control. SRP68 and SRP72 may form the targeting anchor, RPL3 and EIF4G1 may represent ribosome recruitment and initiation, and HSPH1 may buffer folding stress. PAICS, CTPS1, and FASN may supply building blocks for nucleic-acid, membrane, and protein production. This model predicts coordinated changes in protein synthesis, ER targeting, and proteostasis, but co-abundance alone cannot establish direction or causality.

### Important genes

#### SRP68

- **Related proteins** (co-abundance neighbors): FASN (0.82), EIF4G1 (0.81), SRP72 (0.80); STRING partners: RPL3 (0.959), SRP72 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal recognition particle 68. This gene encodes a subunit of the signal recognition particle (SRP). The SRP is a ribonucleoprotein complex that transports secreted and membrane proteins to the endoplasmic reticulum for processing. The complex includes a 7S RNA and six protein subunits. The encoded protein is the 68kDa component of the SRP, and forms a heterodimer with the 72kDa subunit that is required for SRP function. Altern…
- **Diseases (Open Targets)**: neurodegenerative disease (0.347); neutropenia, severe congenital, 10, autosomal recessive (0.333); COVID-19 (0.155); metabolic syndrome (0.074); atrial septal defect (0.073)
- **Europe PMC papers**: 440
- **Why important**: SRP68 is a direct member of the only globally corrected GO term (GO:MF signal recognition particle binding; q_global = 0.0295), occupies a central position in the module, and has STRING links to SRP72 and RPL3. It is an SRP subunit involved in cotranslational targeting of secretory and membrane proteins. It is detected in both shared tissues and has low tissue and immune specificity.
- **Conclusion**: Established: SRP68 is the strongest functional anchor for an SRP and cotranslational-targeting interpretation, with independent support for its partnership with SRP72. Hypothesis: its co-abundance with the broader biosynthetic neighborhood reflects coordinated demand for ER-directed protein synthesis.

#### SRP72

- **Related proteins** (co-abundance neighbors): SRP68 (0.80); STRING partners: RPL3 (0.936), SRP68 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal recognition particle 72. This gene encodes the 72 kDa subunit of the signal recognition particle (SRP), a ribonucleoprotein complex that mediates the targeting of secretory proteins to the endoplasmic reticulum (ER). The SRP complex consists of a 7S RNA and 6 protein subunits: SRP9, SRP14, SRP19, SRP54, SRP68, and SRP72, that are bound to the 7S RNA as monomers or heterodimers. SRP has at least 3 distinct functions that c…
- **Diseases (Open Targets)**: autosomal dominant aplasia and myelodysplasia (0.641); neurodegenerative disease (0.416); intracranial subdural hematoma (0.280); type 2 diabetes mellitus (0.044); oropharynx cancer (0.032)
- **Europe PMC papers**: 696
- **Why important**: SRP72 is the other member of (GO:MF signal recognition particle binding; q_global = 0.0295) and forms the strongly supported SRP68–SRP72 pair. It is detected in both bone marrow and ovary and has low tissue specificity. It provides an independent molecular anchor for the SRP interpretation despite a more peripheral network position.
- **Conclusion**: Established: SRP72 is an SRP-associated component with direct STRING support for its partnership with SRP68 and its role in cotranslational ER targeting. Hypothesis: coordinated SRP68 and SRP72 abundance may indicate regulation at the level of functional SRP assembly or activity.

#### RPL3

- **Related proteins** (co-abundance neighbors): RUVBL2 (0.85); STRING partners: QARS1 (0.749), SRP68 (0.959), SRP72 (0.936)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Cytosol; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein L3. Ribosomes, the complexes that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L3P family of ribosomal proteins and it is located in the cytoplasm. The p…
- **Diseases (Open Targets)**: Duchenne muscular dystrophy (0.506); Orthomyxoviridae infectious disease (0.463); cystic fibrosis (0.389); neuromuscular disease caused by qualitative or quantitative defects of dystrophin (0.323); inflammatory bowel disease (0.308)
- **Europe PMC papers**: 2316
- **Why important**: RPL3 connects the SRP subunits to the ribosomal side of the module and is supported by STRING relationships with SRP68, SRP72, and QARS1. Its established role in the large ribosomal subunit and cytoplasmic translation connects the primary SRP evidence with the supplementary translation terms (STRING RCTM Translation; within-query FDR = 0.0222) and (STRING RCTM SRP-dependent cotranslational protein targeting to membrane; within-query FDR = 0.0232). It is detected in both tissues and is broadly expressed.
- **Conclusion**: Established: RPL3 provides a coherent ribosome connection to the SRP core. Hypothesis: its position may reflect coordination between ribosome availability and ER targeting, but the module does not prove a direct RPL3-mediated regulatory mechanism.

#### EIF4G1

- **Related proteins** (co-abundance neighbors): SF3A1 (0.84), HSPH1 (0.83), FASN (0.82), SRP68 (0.81), QARS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 has the greatest network connectivity in the module and links SRP68, FASN, HSPH1, QARS1, and SF3A1. Its established role as a scaffold in the EIF4F complex and in cap-dependent translation initiation makes it a plausible translation-initiation hub. It is detected in both tissues, broadly expressed, and has the largest reported literature volume among the selected genes.
- **Conclusion**: Established: EIF4G1 is a central co-abundance connector with a well-supported role in translation initiation. Hypothesis: it may coordinate translational throughput with metabolic and protein-quality-control capacity, although network centrality does not establish biochemical control.

#### CTPS1

- **Related proteins** (co-abundance neighbors): PAICS (0.84), HSPH1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CTP synthase 1. This gene encodes an enzyme responsible for the catalytic conversion of UTP (uridine triphosphate) to CTP (cytidine triphospate). This reaction is an important step in the biosynthesis of phospholipids and nucleic acids. Activity of this proten is important in the immune system, and loss of function of this gene has been associated with immunodeficiency. Alternative splicing results in multiple tr…
- **Diseases (Open Targets)**: combined immunodeficiency due to CTPS1 deficiency (0.712); androgenetic alopecia (0.204); hyperpituitarism (0.195); urolithiasis (0.097); alcohol drinking (0.097)
- **Europe PMC papers**: 641
- **Why important**: CTPS1 connects the HSPH1 stress branch to PAICS, linking protein production with nucleotide supply. Its established function in CTP production is relevant to nucleic-acid and phospholipid biosynthesis, and loss of function is associated with immunodeficiency. It is detected in both tissues and has low immune specificity.
- **Conclusion**: Established: CTPS1 supplies a plausible metabolic component and has a documented immunodeficiency association. Hypothesis: its co-abundance may help match nucleotide and membrane-precursor availability to biosynthetic and ER-targeted protein production; the module does not demonstrate causality.
