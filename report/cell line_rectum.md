# Conserved co-abundance modules: cell line and rectum

## Module 0

**Tissue pair**: cell line and rectum  
**Genes (17)**: AAAS, BOP1, CLTC, DDX21, DHX9, ERMP1, MYBBP1A, NOP56, PRKDC, RSL1D1, RRP12, PDCD11, SEC63, SUPT16H, QARS1, TOP2A, XRN2

### Function

The module is best interpreted as a nucleolar RNA-processing and ribosome-biogenesis program. The strongest primary evidence is the broad RNA-binding signal (GO:MF RNA binding; q_global = 0.00026), nucleolar localization (GO:CC nucleolus; q_global = 0.000267), ribonucleoprotein-complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.000727), ribosome biogenesis (GO:BP ribosome biogenesis; q_global = 0.000985), rRNA processing (GO:BP rRNA processing; q_global = 0.0022), and rRNA metabolism (GO:BP rRNA metabolic process; q_global = 0.00462). The preribosome result (GO:CC preribosome; q_global = 0.0319) further supports a coordinated assembly pathway rather than an incidental collection of RNA-associated genes. The RNA-binding and nucleic-acid-binding terms (GO:MF RNA binding; q_global = 0.00026) (GO:MF nucleic acid binding; q_global = 0.00326) are broad, whereas the rRNA and preribosome terms provide the most specific functional interpretation. The osteoblast-differentiation term (GO:BP osteoblast differentiation; q_global = 0.0164) is secondary to the dominant nucleolar signature and may reflect shared regulatory or proliferative biology rather than a specialized osteoblast program. STRING independently supports nucleolar localization and rRNA or ribosome-biogenesis processes (8 supplementary STRING terms; within-query FDR 1.31e-06–0.0016). Overall, the module most plausibly represents active ribosomal RNA maturation, preribosome assembly, and associated nuclear RNA metabolism.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and the proteins detected in rectum are predominantly intracellular and nuclear or nucleolar. This favors a broadly expressed housekeeping or growth-associated program rather than a tissue-restricted rectal function. Some genes show enrichment in neutrophils, erythrocyte progenitors, spermatogenic cells, keratinocytes, or progenitor-like populations, and a small subset shows immune-cell or tissue enhancement. Thus, variation in shared cell types could contribute to the co-abundance pattern, especially in heterogeneous rectal material, but the absence of secretion and the strong nucleolar localization argue against a simple plasma-protein or blood-contamination explanation. The shared signal is more consistent with a conserved cellular RNA-production program that can be expressed across cell line and rectum.

**GO/KEGG enrichment**: 9 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF RNA binding | 0.00026 | BOP1, CLTC, DDX21, DHX9, MYBBP1A, NOP56, PDCD11, PRKDC, RRP12, RSL1D1, SEC63, SUPT16H, TOP2A, XRN2 |
| GO:CC nucleolus | 0.000267 | BOP1, DDX21, DHX9, MYBBP1A, NOP56, PDCD11, PRKDC, RRP12, RSL1D1, TOP2A, XRN2 |
| GO:BP ribonucleoprotein complex biogenesis | 0.000727 | BOP1, DDX21, DHX9, MYBBP1A, NOP56, PDCD11, PRKDC, XRN2 |
| GO:BP ribosome biogenesis | 0.000985 | BOP1, DDX21, MYBBP1A, NOP56, PDCD11, PRKDC, XRN2 |
| GO:BP rRNA processing | 0.0022 | BOP1, DDX21, NOP56, PDCD11, PRKDC, XRN2 |
| GO:MF nucleic acid binding | 0.00326 | BOP1, CLTC, DDX21, DHX9, MYBBP1A, NOP56, PDCD11, PRKDC, RRP12, RSL1D1, SEC63, SUPT16H, TOP2A, XRN2 |
| GO:BP rRNA metabolic process | 0.00462 | BOP1, DDX21, NOP56, PDCD11, PRKDC, XRN2 |
| GO:BP osteoblast differentiation | 0.0164 | CLTC, DDX21, DHX9, MYBBP1A, RSL1D1 |
| GO:CC preribosome | 0.0319 | BOP1, NOP56, PDCD11, PRKDC |

### STRING and hu.MAP

STRING shows a coherent known interaction core centered on BOP1, NOP56, PDCD11, RSL1D1, MYBBP1A, RRP12, and DDX21. The particularly dense relationships among BOP1, NOP56, PDCD11, RSL1D1, MYBBP1A, and RRP12 are consistent with established preribosome and rRNA-processing biology. Additional links connect DDX21 and DHX9 to this nucleolar core, while PRKDC connects the core to DHX9, TOP2A, and other module members. These relationships indicate that much of the co-abundance structure recapitulates known functional biology rather than being an entirely unexplained association. No hu.MAP complex contains at least two module members, so the module is not directly represented by a detected hu.MAP complex under the supplied criterion. That absence does not negate the STRING-supported relationships or the GO evidence; it may indicate that the signal spans several interacting nucleolar activities rather than a single catalogued complex.

**STRING interactions (score >= 0.7)**: 22 of 136 gene pairs: BOP1–DDX21 (0.838); BOP1–MYBBP1A (0.915); BOP1–NOP56 (0.974); BOP1–PDCD11 (0.97); BOP1–RRP12 (0.901); BOP1–RSL1D1 (0.998); DDX21–DHX9 (0.908); DDX21–MYBBP1A (0.963); DDX21–NOP56 (0.811); DDX21–RSL1D1 (0.81); DHX9–PRKDC (0.74); MYBBP1A–NOP56 (0.737); MYBBP1A–PDCD11 (0.949); MYBBP1A–RRP12 (0.846); MYBBP1A–RSL1D1 (0.831); NOP56–PDCD11 (0.997); NOP56–RRP12 (0.938); NOP56–RSL1D1 (0.991); PDCD11–RRP12 (0.984); PDCD11–RSL1D1 (0.978); PRKDC–TOP2A (0.793); RRP12–RSL1D1 (0.97)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Nucleolus (FDR = 1.31e-06, 11 genes); Process rRNA processing (FDR = 4.62e-06, 8 genes); Process Ribonucleoprotein complex biogenesis (FDR = 4.62e-06, 10 genes); Process Ribosome biogenesis (FDR = 4.62e-06, 9 genes); PMID (2017) Nol12 is a multifunctional RNA binding protein at the nexus of RNA and DNA metabolism. (FDR = 2.07e-05, 8 genes); Component Nucleolus (FDR = 4.06e-05, 11 genes); Process ncRNA metabolic process (FDR = 7.41e-05, 9 genes); Function RNA binding (FDR = 8.56e-05, 14 genes); COMPARTMENTS Nuclear lumen (FDR = 0.00028, 12 genes); COMPARTMENTS Preribosome (FDR = 0.00035, 5 genes); Process RNA metabolic process (FDR = 0.00052, 11 genes); Component Preribosome (FDR = 0.0006, 5 genes); Process Nucleic acid metabolic process (FDR = 0.00088, 12 genes); Process RNA processing (FDR = 0.0013, 9 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 0.0016, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The underlying processes are established, and many of the internal relationships are already supported by STRING and by gene-specific functional annotations. Therefore, this should not be claimed as discovery of a new ribosome-biogenesis mechanism. The potentially novel observation is the conserved co-abundance of this particular gene combination across cell line and rectum, especially because no hu.MAP complex captures the module as a unit. However, the fact sheet does not establish whether this exact cross-tissue module has been reported previously, and absence from STRING or hu.MAP alone cannot demonstrate novelty. The defensible conclusion is that the module may represent a new systems-level co-abundance pattern built from largely established nucleolar biology, pending comparison with published co-expression modules and independent datasets.

**Hypothesis.** Hypothesis: the module reflects coordinated control of nucleolar ribosome production coupled to nuclear RNA surveillance and cell-cycle or genome-maintenance demands. A core containing BOP1, NOP56, PDCD11, RSL1D1, MYBBP1A, and RRP12 could support preribosome assembly and rRNA maturation, while DDX21, DHX9, and XRN2 could coordinate RNA remodeling, processing, and turnover. PRKDC and TOP2A may connect this nucleolar activity to DNA damage responses, chromatin or chromosome dynamics, and proliferative state. In rectum, the signal could arise from proliferating or progenitor-like epithelial cells together with other cell types; in cell line, it may reflect a comparable growth-associated demand for ribosome production. This is a mechanistic model, not a demonstrated causal pathway.

### Important genes

#### PRKDC

- **Related proteins** (co-abundance neighbors): DHX9 (0.88), RSL1D1 (0.88), NOP56 (0.86), TOP2A (0.86), DDX21 (0.85), CLTC (0.84), SUPT16H (0.84), PDCD11 (0.84), XRN2 (0.82), RRP12 (0.80); STRING partners: DHX9 (0.74), TOP2A (0.793)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase, DNA-activated, catalytic subunit. This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to DNA-PKcs deficiency (0.752); neurodegenerative disease (0.548); severe combined immunodeficiency (0.470); combined immunodeficiency (0.464); ovarian neoplasm (0.210)
- **Europe PMC papers**: 12461
- **Why important**: PRKDC is a central connector in the module and is linked within the co-abundance graph to both the nucleolar RNA-processing group and DNA or chromosome-associated genes. It appears in nearly all of the primary GO evidence, including nucleolar, ribosome-biogenesis, and rRNA-processing terms (8 globally significant GO/KEGG terms, q_global 0.00026–0.0319; see the table). Its established DNA-PK catalytic function provides a biologically meaningful connection to double-strand-break repair, while the supplied annotation also links it to rRNA maturation. It has extensive literature and disease associations including DNA-PKcs-related immunodeficiency and neoplastic disease.
- **Conclusion**: Established evidence supports PRKDC as a central network component with roles in DNA repair and RNA or nucleolar biology. My conclusion is that it is a strong candidate for coupling ribosome-production state to genome-maintenance state in this module. Its precise causal role in the cross-tissue co-abundance pattern remains a hypothesis.

#### BOP1

- **Related proteins** (co-abundance neighbors): PDCD11 (0.81); STRING partners: DDX21 (0.838), MYBBP1A (0.915), NOP56 (0.974), PDCD11 (0.97), RRP12 (0.901), RSL1D1 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BOP1 ribosomal biogenesis factor. Enables RNA binding activity. Involved in regulation of cell cycle; regulation of signal transduction by p53 class mediator; and ribosomal large subunit biogenesis. Located in chromosome; nucleolus; and nucleoplasm. Part of PeBoW complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.318); cancer (0.090); neoplasm (0.087); polycystic ovary syndrome (0.082); colorectal carcinoma (0.078)
- **Europe PMC papers**: 1064
- **Why important**: BOP1 is a core STRING-connected member of the preribosome group and is linked to NOP56, PDCD11, RSL1D1, MYBBP1A, and RRP12. It contributes to every primary ribosome-biogenesis and rRNA-processing signal in which the corresponding genes are represented (7 globally significant GO/KEGG terms, q_global 0.00026–0.0319; see the table). Its annotation identifies it as a ribosomal-biogenesis factor and a component of the PeBoW complex, with roles in large-subunit assembly and rRNA maturation. It also has established links to cell-cycle regulation, p53-mediated signaling, cancer, and colorectal carcinoma.
- **Conclusion**: Established evidence makes BOP1 one of the clearest functional anchors of the module. My conclusion is that BOP1 likely marks the ribosome-assembly component of the shared program, although the co-abundance data do not prove that it drives the other genes.

#### PDCD11

- **Related proteins** (co-abundance neighbors): NOP56 (0.89), PRKDC (0.84), MYBBP1A (0.84), BOP1 (0.81), RSL1D1 (0.80); STRING partners: BOP1 (0.97), MYBBP1A (0.949), NOP56 (0.997), RRP12 (0.984), RSL1D1 (0.978)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 11. PDCD11 is a NF-kappa-B (NFKB1; 164011)-binding protein that colocalizes with U3 RNA (MIM 180710) in the nucleolus and is required for rRNA maturation and generation of 18S rRNA (Sweet et al., 2003 [PubMed 14624448]; Sweet et al., 2008 [PubMed 17654514]).[supplied by OMIM, Oct 2008].
- **Diseases (Open Targets)**: Back pain (0.277); insomnia (0.216); systemic lupus erythematosus (0.170); neoplasm (0.095); colorectal carcinoma (0.093)
- **Europe PMC papers**: 334
- **Why important**: PDCD11 is embedded in the dense nucleolar interaction core and connects strongly with NOP56, BOP1, MYBBP1A, RRP12, and RSL1D1. It is represented across the primary RNA-binding, nucleolar, ribonucleoprotein-biogenesis, ribosome-biogenesis, and rRNA-processing evidence (8 globally significant GO/KEGG terms, q_global 0.00026–0.0319; see the table). The supplied literature annotation specifically states that PDCD11 binds or colocalizes with U3 RNA and is required for rRNA maturation and generation of the small-subunit rRNA. It also has disease associations including systemic lupus erythematosus and colorectal carcinoma.
- **Conclusion**: Established evidence supports PDCD11 as a direct rRNA-maturation factor and a structural or functional core member. My conclusion is that PDCD11 provides particularly strong support for interpreting the module as an active preribosome and rRNA-processing program rather than generic RNA binding.

#### NOP56

- **Related proteins** (co-abundance neighbors): PDCD11 (0.89), PRKDC (0.86), RSL1D1 (0.81), MYBBP1A (0.81); STRING partners: BOP1 (0.974), DDX21 (0.811), MYBBP1A (0.737), PDCD11 (0.997), RRP12 (0.938), RSL1D1 (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP56 ribonucleoprotein. Nop56p is a yeast nucleolar protein that is part of a complex with the nucleolar proteins Nop58p and fibrillarin. Nop56p is required for assembly of the 60S ribosomal subunit and is involved in pre-rRNA processing. The protein encoded by this gene is similar in sequence to Nop56p and is also found in the nucleolus. Expansion of a GGCCTG repeat from 3-8 copies to 1500-2500 copies in an intron of th…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 36 (0.586); neurodegenerative disease (0.495); ovarian neoplasm (0.272); hereditary disease (0.193); cerebellar ataxia (0.121)
- **Europe PMC papers**: 1517
- **Why important**: NOP56 occupies the nucleolar core and has strong STRING relationships with BOP1, PDCD11, RRP12, RSL1D1, MYBBP1A, and DDX21. It appears in the primary RNA-binding, nucleolar, ribonucleoprotein-biogenesis, ribosome-biogenesis, rRNA-processing, and preribosome evidence (8 globally significant GO/KEGG terms, q_global 0.00026–0.0319; see the table). Its established annotation places it in nucleolar ribonucleoprotein biology, rRNA modification, and small-subunit biogenesis. It also has a substantial literature base and a well-established association with spinocerebellar ataxia type thirty-six.
- **Conclusion**: Established evidence supports NOP56 as a core nucleolar ribonucleoprotein and rRNA-processing factor. My conclusion is that NOP56 is a strong marker of the conserved ribosome-biogenesis component, while its disease association shows that perturbing this biology can have specialized neurological consequences.

#### DDX21

- **Related proteins** (co-abundance neighbors): DHX9 (0.86), PRKDC (0.85), AAAS (0.83); STRING partners: BOP1 (0.838), DHX9 (0.908), MYBBP1A (0.963), NOP56 (0.811), RSL1D1 (0.81)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 links the nucleolar core to DHX9 and other module members and is supported by primary evidence for RNA binding, nucleolar localization, ribonucleoprotein biogenesis, ribosome biogenesis, rRNA processing, and rRNA metabolism (8 globally significant GO/KEGG terms, q_global 0.00026–0.0164; see the table). Its RNA-helicase annotation provides a plausible molecular activity for remodeling RNA structures during ribosome or RNA processing, and its broader functions include chromatin remodeling and transcriptional regulation. It has substantial literature and associations with colorectal, gastric, hepatic, and other cancers as well as neurodegenerative disease.
- **Conclusion**: Established evidence supports DDX21 as an RNA-remodeling and nucleolar regulatory factor with links beyond ribosome assembly. My conclusion is that DDX21 may help coordinate RNA processing with transcriptional or chromatin state, but that integrative role is a hypothesis rather than a direct inference from co-abundance alone.

## Module 1

**Tissue pair**: cell line and rectum  
**Genes (14)**: ABCD3, DHX36, MSH6, NUP160, NUP85, NUP93, NUP210, TBL2, TEX10, THOC2, TMEM214, TM9SF4, SNRNP200, UGGT1

### Function

The strongest interpretation is a nuclear RNA-handling module centered on nuclear pore function, nucleocytoplasmic transport, and export of mature mRNA. The primary evidence is the globally corrected enrichment for RNA localization (GO:BP RNA localization; q_global = 0.00248), nucleocytoplasmic transport (KEGG Nucleocytoplasmic transport - Homo sapiens (human); q_global = 0.00696), mRNA transport (GO:BP mRNA transport; q_global = 0.00775), mRNA export from the nucleus (GO:BP mRNA export from nucleus; q_global = 0.0098), broader nucleic-acid and RNA transport (GO:BP nucleic acid transport; q_global = 0.0167), (GO:BP RNA transport; q_global = 0.0167), and establishment of RNA localization (GO:BP establishment of RNA localization; q_global = 0.0167). The repeated presence of NUP160, NUP210, NUP85, NUP93, and THOC2 across these terms provides a coherent core rather than an isolated annotation. The nuclear pore and nuclear protein-complex terms (GO:CC nuclear protein-containing complex; q_global = 0.0318) and (GO:CC nuclear pore; q_global = 0.047) further support a structural nuclear-transport interpretation. DHX36 adds an RNA helicase and RNA-localization component (GO:BP RNA localization; q_global = 0.00248), while SNRNP200 contributes a spliceosomal RNA-processing connection (GO:CC nuclear protein-containing complex; q_global = 0.0318). The STRING pathway results are concordant supplementary evidence, especially for mature mRNA transport (STRING NetworkNeighborAL Transport of Mature mRNA derived from an Intron-Containing Transcript; within-query FDR = 0.0017), (STRING Keyword mRNA transport; within-query FDR = 0.0018), and (STRING RCTM Transport of Mature mRNA derived from an Intron-Containing Transcript; within-query FDR = 0.0018), but the primary significance claim rests on (GO:BP RNA localization; q_global = 0.00248) through (GO:CC nuclear pore; q_global = 0.047).

**Cell composition.** This is not a plasma-protein or secreted-protein-dominated module. HPA reports low tissue specificity for most members, low immune-cell specificity for every member, and no enriched blood-cell category. Thus, the module does not resemble a blood-cell contamination signature on the available evidence. It also does not appear to be driven by a single shared tissue lineage: the tissue-enhanced genes point separately to bone marrow and lymphoid tissue, testis, and liver, while cell-type-enhanced annotations span neural, germ-cell, cardiac, trophoblast, and erythroid-related populations. One secreted-gene annotation is present in the HPA summary, but the annotated protein is described as intracellular and membrane-associated, so the overall composition remains predominantly intracellular. Protein detection in rectum is available for most members, whereas cell-line protein detection has no matching HPA tissue record; this limits direct protein-level comparison between the two sample groups.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA localization | 0.00248 | DHX36, NUP160, NUP210, NUP85, NUP93, THOC2 |
| KEGG Nucleocytoplasmic transport - Homo sapiens (human) | 0.00696 | NUP160, NUP210, NUP85, NUP93, THOC2 |
| GO:BP mRNA transport | 0.00775 | NUP160, NUP210, NUP85, NUP93, THOC2 |
| GO:BP mRNA export from nucleus | 0.0098 | NUP160, NUP85, NUP93, THOC2 |
| GO:BP nucleic acid transport | 0.0167 | NUP160, NUP210, NUP85, NUP93, THOC2 |
| GO:BP RNA transport | 0.0167 | NUP160, NUP210, NUP85, NUP93, THOC2 |
| GO:BP establishment of RNA localization | 0.0167 | NUP160, NUP210, NUP85, NUP93, THOC2 |
| GO:BP nucleobase-containing compound transport | 0.0233 | NUP160, NUP210, NUP85, NUP93, THOC2 |
| GO:CC nuclear protein-containing complex | 0.0318 | MSH6, NUP160, NUP210, NUP85, NUP93, SNRNP200, TEX10, THOC2 |
| GO:BP RNA export from nucleus | 0.0331 | NUP160, NUP85, NUP93, THOC2 |
| GO:CC nuclear pore | 0.047 | NUP160, NUP210, NUP85, NUP93 |

### STRING and hu.MAP

STRING identifies a tightly connected known nucleoporin core: NUP160, NUP210, NUP85, and NUP93 have high-confidence pairwise relationships with one another. STRING also independently places this core in mRNA transport, RNA transport, and mature mRNA export pathways (STRING NetworkNeighborAL Transport of Mature mRNA derived from an Intron-Containing Transcript; within-query FDR = 0.0017) through (STRING KEGG RNA transport; within-query FDR = 0.0038). The additional viral and host-export terms (STRING NetworkNeighborAL NEP/NS2 Interacts with the Cellular Export Machinery; within-query FDR = 0.0046) through (STRING RCTM NEP/NS2 Interacts with the Cellular Export Machinery; within-query FDR = 0.0056) should be interpreted as contextual reuse of the cellular export machinery, not as evidence that this module is a viral-response module. The glucokinase-related STRING term (STRING RCTM Regulation of Glucokinase by Glucokinase Regulatory Protein; within-query FDR = 0.0056) is not supported by the primary GO/KEGG interpretation and should not drive functional annotation. hu.MAP independently places NUP160, NUP85, and NUP210 in complexes containing other nuclear pore components (hu.MAP huMAP3_04548.1) through (hu.MAP huMAP3_08298.1) and (hu.MAP huMAP3_09825.1) through (hu.MAP huMAP3_11232.1). NUP93 and MSH6 occur together in a broader complex context (hu.MAP huMAP3_09042.1). These results show that the central nucleoporin relationships are already known, whereas the co-abundance links from the nucleoporin core to SNRNP200, THOC2, DHX36, TBL2, TM9SF4, TMEM214, UGGT1, ABCD3, and MSH6 are not generally established by the supplied STRING or hu.MAP records.

**STRING interactions (score >= 0.7)**: 6 of 91 gene pairs: NUP160–NUP210 (0.983); NUP160–NUP85 (0.999); NUP160–NUP93 (0.991); NUP210–NUP85 (0.988); NUP210–NUP93 (0.993); NUP85–NUP93 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Transport of Mature mRNA derived from an Intron-Containing Transcript (FDR = 0.0017, 5 genes); Keyword mRNA transport (FDR = 0.0018, 5 genes); RCTM Transport of Mature mRNA derived from an Intron-Containing Transcript (FDR = 0.0018, 5 genes); KEGG RNA transport (FDR = 0.0038, 5 genes); NetworkNeighborAL NEP/NS2 Interacts with the Cellular Export Machinery (FDR = 0.0046, 4 genes); RCTM ISG15 antiviral mechanism (FDR = 0.0056, 4 genes); RCTM Transport of the SLBP independent Mature mRNA (FDR = 0.0056, 4 genes); RCTM Transport of the SLBP Dependant Mature mRNA (FDR = 0.0056, 4 genes); RCTM Transport of Mature mRNA Derived from an Intronless Transcript (FDR = 0.0056, 4 genes); RCTM Rev-mediated nuclear export of HIV RNA (FDR = 0.0056, 4 genes); RCTM Transport of Ribonucleoproteins into the Host Nucleus (FDR = 0.0056, 4 genes); RCTM NS1 Mediated Effects on Host Pathways (FDR = 0.0056, 4 genes); RCTM Viral Messenger RNA Synthesis (FDR = 0.0056, 4 genes); RCTM NEP/NS2 Interacts with the Cellular Export Machinery (FDR = 0.0056, 4 genes); RCTM Regulation of Glucokinase by Glucokinase Regulatory Protein (FDR = 0.0056, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04548.1 (NUP160, NUP85; 2/2); huMAP3_08489.1 (NUP160, NUP85; 2/10); huMAP3_09710.1 (NUP160, NUP210; 2/13); huMAP3_08298.1 (NUP160, NUP85; 2/24); huMAP3_09042.1 (MSH6, NUP93; 2/26); huMAP3_09825.1 (NUP160, NUP85; 2/27); huMAP3_09114.1 (NUP160, NUP85; 2/30); huMAP3_10202.1 (NUP160, NUP85; 2/52); huMAP3_12581.1 (NUP160, NUP85; 2/58); huMAP3_11232.1 (NUP160, NUP85; 2/78)

### Novelty

The biological mechanism represented by the central portion is not a new discovery: nuclear pores, nucleocytoplasmic transport, mRNA export, and the relationships among NUP160, NUP210, NUP85, and NUP93 are established. The module may nevertheless be a new or useful systems-level observation if its conservation between cell line and rectum is reproducible, because the supplied records do not establish this exact cross-context co-abundance grouping or its peripheral links. That claim should remain modest. The absence of STRING or hu.MAP support for several peripheral genes is evidence of limited prior curated coverage, not proof of novelty. The most defensible conclusion is established core biology combined with a potentially novel co-abundance configuration and tissue-pair conservation.

**Hypothesis.** Hypothesis: the shared module reflects coordinated regulation of nuclear pore capacity and RNA quality control. A nucleoporin scaffold formed around NUP160, NUP85, NUP93, and NUP210 may co-vary with TREX-linked mRNA export through THOC2, RNA remodeling through DHX36, and spliceosomal processing through SNRNP200. The peripheral associations with ER, Golgi, peroxisomal, and DNA-repair proteins may indicate coupling of RNA export to broader proteostasis, organelle function, or genome maintenance, but those connections are hypotheses rather than demonstrated physical interactions in this module. A useful test would be whether the peripheral genes change with experimentally measured nuclear-pore abundance, mature-mRNA export, and splicing activity in both sample contexts.

### Important genes

#### NUP160

- **Related proteins** (co-abundance neighbors): THOC2 (0.84), TBL2 (0.81), SNRNP200 (0.81); STRING partners: NUP210 (0.983), NUP85 (0.999), NUP93 (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_04548.1, huMAP3_08489.1, huMAP3_09710.1, huMAP3_08298.1, huMAP3_09825.1, huMAP3_09114.1, huMAP3_10202.1, huMAP3_12581.1, huMAP3_11232.1
- **Function (MyGene.info)**: nucleoporin 160. NUP160 is 1 of up to 60 proteins that make up the 120-MD nuclear pore complex, which mediates nucleoplasmic transport.[supplied by OMIM, Apr 2004]
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.527); neurodegenerative disease (0.469); Alzheimer disease (0.429)
- **Europe PMC papers**: 812
- **Why important**: NUP160 is a central member of the nucleoporin core and connects directly within the module to NUP210, NUP85, and NUP93. It appears in every primary enrichment category from RNA localization through nuclear-pore annotation (GO:BP RNA localization; q_global = 0.00248) through (GO:CC nuclear pore; q_global = 0.047), in all listed STRING supplementary terms, and in many hu.MAP complexes (hu.MAP huMAP3_04548.1) through (hu.MAP huMAP3_08298.1) and (hu.MAP huMAP3_09825.1) through (hu.MAP huMAP3_11232.1). Its established function in the nuclear pore and nucleocytoplasmic transport makes it the clearest structural anchor. It also has substantial literature and disease links involving infectious disease and neurodegenerative disease.
- **Conclusion**: Established conclusion: NUP160 is a principal structural and functional marker of the module's nuclear-pore and RNA-transport program. Hypothesis: its co-abundance may report variation in the amount or activity of nuclear-pore machinery across the two tissue contexts.

#### NUP85

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.82); STRING partners: NUP160 (0.999), NUP210 (0.988), NUP93 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_04548.1, huMAP3_08489.1, huMAP3_08298.1, huMAP3_09825.1, huMAP3_09114.1, huMAP3_10202.1, huMAP3_12581.1, huMAP3_11232.1
- **Function (MyGene.info)**: nucleoporin 85. This gene encodes a protein component of the Nup107-160 subunit of the nuclear pore complex. Nuclear pore complexes are embedded in the nuclear envelope and promote bidirectional transport of macromolecules between the cytoplasm and nucleus. The encoded protein can also bind to the C-terminus of chemokine (C-C motif) receptor 2 (CCR2) and promote chemotaxis of monocytes, thereby participating in t…
- **Diseases (Open Targets)**: nephrotic syndrome (0.596); Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.527); Seckel syndrome (0.371)
- **Europe PMC papers**: 872
- **Why important**: NUP85 is a member of the NUP107-160 nuclear-pore subunit and has direct STRING relationships with NUP160, NUP210, and NUP93. It is present throughout the primary RNA-transport and nuclear-pore evidence (GO:BP RNA localization; q_global = 0.00248) through (GO:CC nuclear pore; q_global = 0.047), recurs in the STRING transport terms (STRING NetworkNeighborAL Transport of Mature mRNA derived from an Intron-Containing Transcript; within-query FDR = 0.0017) through (STRING KEGG RNA transport; within-query FDR = 0.0038), and appears in numerous hu.MAP pore-related complexes (hu.MAP huMAP3_04548.1), (hu.MAP huMAP3_08489.1), and (hu.MAP huMAP3_08298.1) through (hu.MAP huMAP3_11232.1). It also has a documented connection to CCR2-associated chemotaxis and disease associations including nephrotic syndrome, viral infection, and Seckel syndrome.
- **Conclusion**: Established conclusion: NUP85 is a well-supported pore-complex component that reinforces the module's core interpretation. Hypothesis: the module could link general nuclear transport with cellular inflammatory or chemotactic state, but the co-abundance data alone do not establish that connection.

#### NUP93

- **Related proteins** (co-abundance neighbors): TM9SF4 (0.81); STRING partners: NUP160 (0.991), NUP210 (0.993), NUP85 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_09042.1
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 is a nuclear-pore component with a particularly strong known relationship to NUP160, NUP210, and NUP85 in STRING. It is included in all primary enrichment terms (GO:BP RNA localization; q_global = 0.00248) through (GO:CC nuclear pore; q_global = 0.047) and in the module's direct nuclear-pore evidence. hu.MAP places it with MSH6 in a broader complex context (hu.MAP huMAP3_09042.1). NUP93 has extensive literature, including strong disease associations with nephrotic syndromes, and its annotations include nuclear-pore assembly, mRNA export, and SMAD signaling.
- **Conclusion**: Established conclusion: NUP93 is both a mechanistically relevant pore component and a highly informative disease-linked member of the module. Hypothesis: variation involving NUP93 could couple transport architecture to signaling or epithelial homeostasis, but this requires direct testing.

#### NUP210

- **Related proteins** (co-abundance neighbors): DHX36 (0.82), SNRNP200 (0.82); STRING partners: NUP160 (0.983), NUP85 (0.988), NUP93 (0.993)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_09710.1
- **Function (MyGene.info)**: nucleoporin 210. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. The protein encoded by this gene is a membrane-spanning glycoprotein that is a major component of the nuclear pore complex. M…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.536); COVID-19 (0.407); Histiocytosis (0.370)
- **Europe PMC papers**: 642
- **Why important**: NUP210 is a membrane-spanning nuclear-pore glycoprotein and is directly connected by STRING to NUP160, NUP85, and NUP93. It contributes to the primary RNA-localization and nucleocytoplasmic transport evidence (GO:BP RNA localization; q_global = 0.00248), (KEGG Nucleocytoplasmic transport - Homo sapiens (human); q_global = 0.00696), (GO:BP mRNA transport; q_global = 0.00775), and (GO:BP nucleic acid transport; q_global = 0.0167) through (GO:CC nuclear pore; q_global = 0.047), as well as the STRING transport terms (STRING NetworkNeighborAL Transport of Mature mRNA derived from an Intron-Containing Transcript; within-query FDR = 0.0017) through (STRING RCTM Regulation of Glucokinase by Glucokinase Regulatory Protein; within-query FDR = 0.0056). Its HPA tissue enhancement in bone marrow and lymphoid tissue and cell-type enhancement in progenitor and B-cell categories provide a possible context-sensitive dimension, although HPA does not classify the module as blood-cell specific.
- **Conclusion**: Established conclusion: NUP210 is a structural nuclear-pore component that supports the module's transport interpretation. Hypothesis: its tissue-associated expression may modulate how the shared transport program is manifested in rectum or cell-line samples, without implying blood contamination.

#### THOC2

- **Related proteins** (co-abundance neighbors): NUP160 (0.84), SNRNP200 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: THO complex subunit 2. The TREX multiprotein complex binds specifically to spliced mRNAs to facilitate mRNA export. The protein encoded by this gene is a member of the THO complex, a subset of the TREX complex. The encoded protein interacts with the THOC1 protein.[provided by RefSeq, Jun 2010].
- **Diseases (Open Targets)**: non-syndromic X-linked intellectual disability (0.753); neurodegenerative disease (0.500); hereditary disease (0.452); X-linked complex neurodevelopmental disorder (0.370); rheumatoid arthritis (0.302)
- **Europe PMC papers**: 680
- **Why important**: THOC2 is the strongest bridge between the pore core and the mature-mRNA export machinery: it links within the module to NUP160 and SNRNP200 and appears in the primary RNA-localization, mRNA-transport, and mRNA-export terms (GO:BP RNA localization; q_global = 0.00248) through (GO:BP RNA export from nucleus; q_global = 0.0331). It is also independently supported by STRING transport terms (STRING NetworkNeighborAL Transport of Mature mRNA derived from an Intron-Containing Transcript; within-query FDR = 0.0017) through (STRING KEGG RNA transport; within-query FDR = 0.0038). Its established role in the THO/TREX complex and polyadenylated mRNA export makes it more mechanistically specific than a generic nuclear structural marker. It has substantial literature and disease associations involving X-linked intellectual disability and neurodevelopmental disorders.
- **Conclusion**: Established conclusion: THOC2 supports a functional RNA-export process coupled to the nuclear pore, rather than merely reflecting nuclear localization. Hypothesis: THOC2 may be the key regulatory interface through which the module coordinates transcript processing with pore passage.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): TEX10 (0.85), TMEM214 (0.84), THOC2 (0.82), NUP210 (0.82), NUP85 (0.82), UGGT1 (0.81), NUP160 (0.81), ABCD3 (0.81), MSH6 (0.80), TM9SF4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is the highest-connectivity node in the supplied module and links the nucleoporin core to multiple peripheral genes. It is the U5 small nuclear ribonucleoprotein helicase and an established spliceosome component, while the primary nuclear-complex evidence includes it (GO:CC nuclear protein-containing complex; q_global = 0.0318). Its large literature base and disease associations with retinitis pigmentosa and inherited retinal dystrophy make it an important functional and clinical anchor. Unlike the nucleoporins, it has no supplied STRING partner or hu.MAP complex assignment here, so its module relationship is especially relevant as a co-abundance observation rather than a confirmed curated interaction.
- **Conclusion**: Established conclusion: SNRNP200 brings pre-mRNA splicing and RNA remodeling into a module otherwise dominated by nuclear pores. Hypothesis: the shared module may represent coordinated coupling of spliceosome output to export demand, but the direct molecular bridge remains to be demonstrated.

## Module 2

**Tissue pair**: cell line and rectum  
**Genes (11)**: ACLY, COPG2, EIF4G1, PDS5B, CAD, SEC24C, EPRS1, IARS1, LARS1, RARS1, VARS1

### Function

The module is best interpreted as a cytosolic protein-translation and translational-fidelity program centered on aminoacyl-tRNA charging. The primary evidence is the globally corrected enrichment for aminoacyl-tRNA ligase activity, tRNA aminoacylation, amino acid activation, aminoacyl-tRNA biosynthesis, and the aminoacyl-tRNA synthetase multienzyme complex (7 globally significant GO/KEGG terms, q_global 0.000706–0.000719; see the table). Additional globally corrected terms connect the module to tRNA metabolism, aminoacyl-tRNA deacylation, translational fidelity, ATP binding, and amino acid metabolism (9 globally significant GO/KEGG terms, q_global 0.00284–0.0322; see the table). The synthetase genes EPRS1, IARS1, LARS1, RARS1, and VARS1 form the functional core, while EIF4G1 supports translation initiation and CAD and ACLY connect the module to nucleotide and acetyl-CoA or lipid-related metabolism. The network therefore reflects coordinated protein synthesis capacity rather than a narrowly tissue-specific pathway.

**Cell composition.** The module does not appear to be driven by plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not blood-cell enriched, because the genes show low immune-cell specificity or are not detected in immune cells. All genes have low tissue specificity, and the HPA single-cell annotations are dispersed across several cell types rather than concentrated in a coherent rectal or blood-cell population. Most module proteins are detected in rectum, consistent with expression in rectal tissue, but this does not establish a rectum-specific function. The shared cell-line and rectum signal is therefore more consistent with a broadly expressed housekeeping-like translation and biosynthetic program, potentially reflecting common cellular activity, than with contamination by plasma or blood cells.

**GO/KEGG enrichment**: 16 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF aminoacyl-tRNA ligase activity | 0.000706 | EPRS1, IARS1, LARS1, RARS1, VARS1 |
| GO:BP tRNA aminoacylation for protein translation | 0.000706 | EPRS1, IARS1, LARS1, RARS1, VARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 0.000706 | EPRS1, IARS1, LARS1, RARS1, VARS1 |
| GO:BP amino acid activation | 0.000706 | EPRS1, IARS1, LARS1, RARS1, VARS1 |
| GO:BP tRNA aminoacylation | 0.000706 | EPRS1, IARS1, LARS1, RARS1, VARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 0.000706 | EPRS1, IARS1, LARS1, RARS1, VARS1 |
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 0.000719 | EPRS1, IARS1, LARS1, RARS1 |
| GO:MF ligase activity | 0.00284 | CAD, EPRS1, IARS1, LARS1, RARS1, VARS1 |
| GO:MF catalytic activity, acting on a tRNA | 0.00451 | EPRS1, IARS1, LARS1, RARS1, VARS1 |
| GO:BP amino acid metabolic process | 0.00713 | CAD, EPRS1, IARS1, LARS1, RARS1, VARS1 |
| GO:BP tRNA metabolic process | 0.00899 | EPRS1, IARS1, LARS1, RARS1, VARS1 |
| GO:MF aminoacyl-tRNA deacylase activity | 0.0142 | IARS1, LARS1, VARS1 |
| GO:BP aminoacyl-tRNA metabolism involved in translational fidelity | 0.0142 | IARS1, LARS1, VARS1 |
| GO:BP regulation of translational fidelity | 0.0195 | IARS1, LARS1, VARS1 |
| GO:MF ATP binding | 0.0297 | ACLY, CAD, EIF4G1, EPRS1, IARS1, LARS1, RARS1, VARS1 |

### STRING and hu.MAP

STRING provides strong, mutually reinforcing relationships among EPRS1, IARS1, LARS1, RARS1, and VARS1 (STRING InterPro Aminoacyl-tRNA synthetase, class I, conserved site; within-query FDR = 1.04e-05), (STRING Keyword Aminoacyl-tRNA synthetase; within-query FDR = 8.02e-05), (STRING KEGG Aminoacyl-tRNA biosynthesis; within-query FDR = 0.00011), (4 supplementary STRING terms; within-query FDR 0.00018–0.00059), (STRING NetworkNeighborAL tRNA Aminoacylation, and glutamyl-tRNA(Gln) amidotransferase complex; within-query FDR = 0.00078), (STRING COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex; within-query FDR = 0.00084). These relationships and the STRING annotations support a known aminoacyl-tRNA synthetase network, not an isolated statistical grouping. hu.MAP independently places EPRS1, IARS1, LARS1, and RARS1 together in two multisynthetase-complex models (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1). Thus, the central synthetase cluster has established biochemical and complex-level support. The module also contains co-abundance links involving ACLY, CAD, EIF4G1, SEC24C, PDS5B, and COPG2, but these peripheral relationships are not represented by the reported STRING or hu.MAP evidence. They should be treated as module-level associations requiring validation rather than as established physical interactions.

**STRING interactions (score >= 0.7)**: 10 of 55 gene pairs: EPRS1–IARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–RARS1 (0.999); EPRS1–VARS1 (0.97); IARS1–LARS1 (0.999); IARS1–RARS1 (0.999); IARS1–VARS1 (0.9); LARS1–RARS1 (0.999); LARS1–VARS1 (0.968); RARS1–VARS1 (0.905)
**STRING functional enrichment (supplementary, within-query FDR)**: InterPro Aminoacyl-tRNA synthetase, class I, conserved site (FDR = 1.04e-05, 5 genes); Keyword Protein biosynthesis (FDR = 6.24e-05, 6 genes); WikiPathways Amino acid metabolism (FDR = 6.51e-05, 6 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 8.02e-05, 5 genes); Keyword Ligase (FDR = 9.67e-05, 6 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 0.00011, 5 genes); InterPro Rossmann-like alpha/beta/alpha sandwich fold (FDR = 0.00014, 5 genes); RCTM Cytosolic tRNA aminoacylation (FDR = 0.00018, 5 genes); InterPro Aminoacyl-tRNA synthetase, class Ia, anticodon-binding (FDR = 0.00023, 4 genes); Function aminoacyl-tRNA ligase activity (FDR = 0.00046, 5 genes); Component aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.00059, 4 genes); Function Ligase activity (FDR = 0.00061, 6 genes); NetworkNeighborAL tRNA Aminoacylation, and glutamyl-tRNA(Gln) amidotransferase complex (FDR = 0.00078, 5 genes); RCTM Translation (FDR = 0.00079, 6 genes); COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.00084, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, IARS1, RARS1, LARS1; 4/14); huMAP3_13688.1 (EPRS1, IARS1, RARS1, LARS1; 4/14)

### Novelty

This module should not be described as a newly discovered aminoacyl-tRNA synthetase complex or pathway, because its central relationships and functional annotations are already well established by STRING, hu.MAP, and the primary GO/KEGG results. A potentially useful new observation is the coordinated co-abundance of this known translation core with metabolic, translation-initiation, and vesicle-trafficking genes in a module shared by cell line and rectum. However, the fact sheet does not establish whether that cross-context co-abundance is reproducible, causal, or absent from prior co-expression studies. The most defensible conclusion is that the module represents a biologically coherent replication of a known core program with a potentially novel context-specific network perimeter, rather than a proven new molecular mechanism.

**Hypothesis.** Hypothesis: shared cellular demand for protein synthesis coordinates aminoacyl-tRNA charging with translation initiation and supporting nucleotide or carbon metabolism in both cell line and rectum. The synthetase core may set translational capacity and fidelity, while EIF4G1, CAD, and ACLY couple that capacity to mRNA recruitment, pyrimidine production, and cytosolic acetyl-CoA supply. The associations with SEC24C, COPG2, and PDS5B may reflect broader coupling to intracellular transport and proliferative or cell-cycle state, but this peripheral extension is provisional and should be tested by independent expression datasets, perturbation experiments, and physical-interaction assays.

### Important genes

#### IARS1

- **Related proteins** (co-abundance neighbors): LARS1 (0.90), RARS1 (0.86), EPRS1 (0.85), ACLY (0.84), CAD (0.84), VARS1 (0.84), EIF4G1 (0.83), SEC24C (0.81); STRING partners: EPRS1 (0.999), LARS1 (0.999), RARS1 (0.999), VARS1 (0.9)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Isoleucine-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family and has been identified as a …
- **Diseases (Open Targets)**: growth retardation, intellectual developmental disorder, hypotonia, and hepatopathy (0.733); Abnormality of the skeletal system (0.332); microcephaly (0.289); Global developmental delay (0.289); Hallux valgus (0.184)
- **Europe PMC papers**: 184
- **Why important**: IARS1 is the most connected node in the reported module and is present in every primary GO/KEGG enrichment (16 globally significant GO/KEGG terms, q_global 0.000706–0.0322; see the table). It encodes isoleucyl-tRNA synthetase, directly supporting aminoacylation and translational fidelity. It is present in both hu.MAP complexes (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1) and has strong STRING relationships with the other core synthetases. Its disease evidence includes developmental, skeletal, neurologic, and hepatopathy associations, and its literature is substantial.
- **Conclusion**: Established evidence supports IARS1 as a central structural and functional anchor of the module. Its network position and annotations make it a strong marker of the module's translation-related function. It is plausible, but not established, that variation in IARS1 abundance could influence the translational capacity represented by this module.

#### EPRS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.85), RARS1 (0.85), LARS1 (0.85), VARS1 (0.83), PDS5B (0.81), COPG2 (0.80); STRING partners: IARS1 (0.999), LARS1 (0.999), RARS1 (0.999), VARS1 (0.97)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 has high module connectivity and encodes a multifunctional synthetase that charges glutamyl and prolyl tRNAs. It is a member of both hu.MAP complexes (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1) and participates in nearly all primary enrichment terms, including the aminoacyl-tRNA synthetase complex (11 globally significant GO/KEGG terms, q_global 0.000706–0.00899; see the table), (GO:MF ATP binding; q_global = 0.0297), (GO:MF adenyl ribonucleotide binding; q_global = 0.0322). It also has strong disease associations involving hypomyelinating leukodystrophy and developmental delay, together with substantial literature support.
- **Conclusion**: Established evidence identifies EPRS1 as a core multisynthetase-complex component and a major contributor to the module's functional interpretation. Its additional links to PDS5B and COPG2 are module associations, not established physical mechanisms. A regulatory role connecting translation to cellular stress or insulin response is a hypothesis supported by its annotations but not demonstrated by this module alone.

#### LARS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.90), EPRS1 (0.85), SEC24C (0.83), RARS1 (0.82), ACLY (0.82); STRING partners: EPRS1 (0.999), IARS1 (0.999), RARS1 (0.999), VARS1 (0.968)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: leucyl-tRNA synthetase 1. This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals w…
- **Diseases (Open Targets)**: infantile liver failure syndrome 1 (0.670); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.510); Global developmental delay (0.119); sensorineural hearing loss disorder (0.119); Generalized-onset seizure (0.118)
- **Europe PMC papers**: 267
- **Why important**: LARS1 is a highly connected core node, belongs to both hu.MAP complexes (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1), and has strong STRING relationships with the other synthetases. It catalyzes leucine-tRNA aminoacylation and is associated with amino-acid sensing and response annotations, making it a plausible bridge between nutrient state and translational activity. It has extensive literature and disease associations including infantile liver failure and other developmental or neurologic phenotypes.
- **Conclusion**: Established evidence supports LARS1 as both a translation enzyme and a component of the known multisynthetase complex. Its co-abundance with ACLY may indicate coordination between nutrient-linked translation and carbon metabolism, but that interpretation remains a hypothesis because the fact sheet does not establish direct regulation between them.

#### RARS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.86), EPRS1 (0.85), LARS1 (0.82); STRING partners: EPRS1 (0.999), IARS1 (0.999), LARS1 (0.999), VARS1 (0.905)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 is a core synthetase node with strong STRING support and membership in both hu.MAP complexes (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1). It contributes to the primary aminoacyl-tRNA charging and translation terms (11 globally significant GO/KEGG terms, q_global 0.000706–0.00899; see the table), (GO:MF ATP binding; q_global = 0.0297), (GO:MF adenyl ribonucleotide binding; q_global = 0.0322) and encodes arginyl-tRNA synthetase. Its disease associations include hypomyelinating and other leukodystrophy phenotypes, while its literature base is substantial.
- **Conclusion**: Established evidence supports RARS1 as part of the conserved multisynthetase machinery represented by the module. Its presence strengthens the interpretation that the module reflects coordinated charging of multiple tRNA species rather than a generic ATP-dependent process. The module does not establish a disease-specific role for RARS1 in rectum or cell line.

## Module 3

**Tissue pair**: cell line and rectum  
**Genes (7)**: COPB1, GARS1, NUP155, POLR1A, SLC25A13, SEC24A, DARS2

### Function

This is a heterogeneous intracellular co-abundance module rather than a clearly defined pathway module. Its genes span mitochondrial metabolism and transport (DARS2 and SLC25A13), nuclear pore and nucleocytoplasmic transport functions (NUP155), ribosomal RNA transcription (POLR1A), and endoplasmic-reticulum–Golgi vesicle trafficking (COPB1 and SEC24A). GARS1 adds cytosolic aminoacyl-tRNA charging. DARS2 is the network hub, linking the mitochondrial translation-related gene GARS1 with NUP155, POLR1A, and COPB1, while the remaining structure consists of two peripheral connections. No GO or KEGG term passed global correction. STRING functional enrichment was also absent. Therefore, the most defensible interpretation is coordinated expression of broadly required cellular maintenance processes, with possible contributions from mitochondrial, nuclear, and secretory-pathway activity rather than evidence for one established biological pathway.

**Cell composition.** The module is not dominated by plasma proteins, secreted proteins, or blood-cell-enriched genes. HPA reports low immune-cell specificity for nearly all members, no enriched blood-cell category, and only one gene as not detected in immune cells. Only GARS1 has a secretome annotation, described as intracellular and membrane, rather than a classical secreted protein. Most genes have low tissue specificity, although NUP155 is tissue-enriched in testis and SLC25A13 is tissue-enriched in liver. Cell-type-enhanced annotations are distributed across adipocytes, cardiomyocytes, epicardial cells, late spermatids, choroid plexus epithelial cells, neutrophils, oligodendrocytes, and endometrial glandular cells, without a coherent shared cell type. Protein detection in rectum is reported for most members, whereas the cell-line protein comparison has no informative HPA result. Overall, the module does not strongly suggest blood contamination or a plasma-protein signature; it is more consistent with broadly expressed intracellular biology, possibly modulated by tissue or cellular composition.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship is COPB1–SEC24A. This is biologically coherent: COPB1 is a COPI coatomer subunit involved in Golgi-to-endoplasmic-reticulum and intra-Golgi trafficking, while SEC24A is a COPII cargo-loading component involved in endoplasmic-reticulum-to-Golgi transport. The remaining co-abundance relationships are not represented as high-confidence STRING interactions in the fact sheet. No hu.MAP complex contains multiple module members. Thus, the module contains one externally supported trafficking relationship, but most of its network structure is not explained by established physical complexes. Co-abundance should therefore not be equated with direct protein interaction; it may reflect coordinated regulation, shared cellular state, or indirect functional coupling.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: COPB1–SEC24A (0.724)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unrecognized co-abundance association, because most of its edges are absent from the supplied STRING and hu.MAP evidence and no established multiprotein complex accounts for the module. However, this is not sufficient to claim a new biological mechanism. The genes are individually well characterized, and their functions are distributed across common cellular processes. The absence of a globally significant GO or KEGG term and the lack of STRING functional enrichment further weaken a pathway-level novelty claim. The strongest cautious conclusion is that the co-abundance pattern may be novel as a cross-context network observation, while its biological mechanism remains unresolved and requires independent replication and perturbational validation.

**Hypothesis.** Hypothesis: the module reflects a coordinated cellular maintenance state in which mitochondrial amino-acid handling and translation-related capacity are coupled indirectly to nuclear transport, ribosomal RNA production, and secretory-pathway trafficking. DARS2 may organize this expression pattern because it is the central network member and connects genes from several intracellular compartments. The COPB1–SEC24A relationship provides a plausible trafficking submodule, while the DARS2–GARS1 connection may indicate coordinated aminoacyl-tRNA charging capacity. The links to NUP155, POLR1A, and SLC25A13 are hypotheses based on co-abundance and known gene functions, not established physical interactions or demonstrated causal relationships.

### Important genes

#### DARS2

- **Related proteins** (co-abundance neighbors): NUP155 (0.84), POLR1A (0.83), COPB1 (0.80), GARS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 2, mitochondrial. The protein encoded by this gene belongs to the class-II aminoacyl-tRNA synthetase family. It is a mitochondrial enzyme that specifically aminoacylates aspartyl-tRNA. Mutations in this gene are associated with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation (LBSL). [provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: leukoencephalopathy with brain stem and spinal cord involvement-high lactate syndrome (0.843); neurodegenerative disease (0.527); hereditary disease (0.518); hypertensive disorder (0.425); Cerebral cortical atrophy (0.425)
- **Europe PMC papers**: 796
- **Why important**: DARS2 is the network hub, connecting NUP155, POLR1A, COPB1, and GARS1. Its established function is mitochondrial aspartyl-tRNA aminoacylation, and its mitochondrial localization provides a possible link between translational capacity and the other intracellular processes represented in the module. It is associated with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation, and it has substantial literature support.
- **Conclusion**: Established: DARS2 is the central co-abundance gene and a mitochondrial aminoacyl-tRNA synthetase with a documented neurological disease association. Hypothesis: its hub position may indicate coordinated mitochondrial and cellular maintenance regulation, but it does not establish that DARS2 drives the other module genes.

#### SLC25A13

- **Related proteins** (co-abundance neighbors): NUP155 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 25 member 13. This gene is a member of the mitochondrial carrier family. The encoded protein contains four EF-hand Ca(2+) binding motifs in the N-terminal domain, and localizes to mitochondria. The protein catalyzes the exchange of aspartate for glutamate and a proton across the inner mitochondrial membrane, and is stimulated by calcium on the external side of the inner mitochondrial membrane. Mutations in this…
- **Diseases (Open Targets)**: neonatal intrahepatic cholestasis due to citrin deficiency (0.804); citrullinemia type II (0.756); citrin deficiency (0.652); citrullinemia (0.649); citrullinemia type I (0.464)
- **Europe PMC papers**: 1421
- **Why important**: SLC25A13 is the module member connected to NUP155 and encodes a mitochondrial carrier that exchanges aspartate for glutamate and a proton. It is tissue-enriched in liver and has strong disease associations with citrin deficiency and citrullinemia type II. Its function is especially relevant to mitochondrial transport and metabolic state, although its single network connection limits claims about module-wide control.
- **Conclusion**: Established: SLC25A13 is a mitochondrial aspartate–glutamate transporter with a well-established metabolic and inherited-disease role. Hypothesis: its co-abundance with NUP155 may mark a broader metabolic or cellular-state program rather than a direct molecular interaction.

#### NUP155

- **Related proteins** (co-abundance neighbors): DARS2 (0.84), SLC25A13 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 155. Nucleoporins are proteins that play an important role in the assembly and functioning of the nuclear pore complex (NPC) which regulates the movement of macromolecules across the nuclear envelope (NE). The protein encoded by this gene plays a role in the fusion of NE vesicles and formation of the double membrane NE. The protein may also be involved in cardiac physiology and may be associated with t…
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); atrial fibrillation (0.470); familial atrial fibrillation (0.390)
- **Europe PMC papers**: 944
- **Why important**: NUP155 is connected to both DARS2 and SLC25A13 and encodes a nuclear pore component involved in nucleocytoplasmic transport and nuclear-envelope organization. It is tissue-enriched in testis and enhanced in late spermatids, and it has established associations with atrial fibrillation and familial atrial fibrillation. Its position provides a bridge between mitochondrial genes and nuclear transport biology.
- **Conclusion**: Established: NUP155 is a nuclear pore and nuclear-envelope protein with cardiac disease associations and distinctive testis-related HPA expression. Hypothesis: the NUP155 connections may reflect coordinated regulation of nuclear transport with mitochondrial metabolism, but no direct interaction with the neighboring module genes is established here.

#### COPB1

- **Related proteins** (co-abundance neighbors): SEC24A (0.82), DARS2 (0.80); STRING partners: SEC24A (0.724)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus, Vesicles, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coat protein complex I subunit beta 1. This gene encodes a protein subunit of the coatomer complex associated with non-clathrin coated vesicles. The coatomer complex, also known as the coat protein complex 1, forms in the cytoplasm and is recruited to the Golgi by activated guanosine triphosphatases. Once at the Golgi membrane, the coatomer complex may assist in the movement of protein and lipid components back to the endoplasmic retic…
- **Diseases (Open Targets)**: Baralle-Macken syndrome (0.598); Alzheimer disease (0.463); Parkinson disease (0.462); neurodegenerative disease (0.462); lysosomal storage disease (0.462)
- **Europe PMC papers**: 565
- **Why important**: COPB1 participates in the COPI coatomer complex and intracellular vesicle transport, including retrograde Golgi-to-endoplasmic-reticulum trafficking. It is one half of the only high-confidence STRING interaction in the module, pairing with SEC24A, and it also connects to the central gene DARS2. Its disease associations include Baralle-Macken syndrome and several neurodegenerative or lysosomal-storage disease categories.
- **Conclusion**: Established: COPB1 has a defined vesicle-trafficking function and an externally supported relationship with SEC24A. Hypothesis: COPB1 may define a secretory-pathway component of the module, but its connection to DARS2 is a co-abundance association rather than demonstrated physical coupling.

#### SEC24A

- **Related proteins** (co-abundance neighbors): COPB1 (0.82); STRING partners: COPB1 (0.724)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center, Vesicles; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC24 homolog A, COPII component. The protein encoded by this gene belongs to a family of proteins that are homologous to yeast Sec24. This protein is a component of coat protein II (COPII)-coated vesicles that mediate protein transport from the endoplasmic reticulum. COPII acts in the cytoplasm to promote the transport of secretory, plasma membrane, and vacuolar proteins from the endoplasmic reticulum to the golgi complex. Altern…
- **Diseases (Open Targets)**: Graves disease (0.218); hyperlipoproteinemia type V (0.071); combined low LDL and fibrinogen (0.069); Hyperlipoproteinemia type 1 (0.062); apolipoprotein c-III deficiency (0.062)
- **Europe PMC papers**: 808
- **Why important**: SEC24A is a COPII component involved in cargo loading and endoplasmic-reticulum-to-Golgi transport. Its direct STRING relationship with COPB1 is the clearest externally supported relationship in the module. It is also linked in the supplied disease evidence to lipid and lipoprotein-related disorders, which may connect vesicle trafficking to cellular metabolic state.
- **Conclusion**: Established: SEC24A is a secretory-pathway transport component and forms the module's only high-confidence STRING-supported pair with COPB1. Hypothesis: SEC24A and COPB1 may represent a real trafficking submodule embedded within a broader co-abundance program, but the rest of the module cannot be assigned to this pathway solely from the available evidence.
