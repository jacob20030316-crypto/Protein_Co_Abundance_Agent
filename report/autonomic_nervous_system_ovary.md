# Conserved co-abundance modules: autonomic_nervous_system and ovary

## Module 0

**Tissue pair**: autonomic_nervous_system and ovary  
**Genes (14)**: ACIN1, ADNP, PRMT5, CHD4, DDX46, PUM1, RBM33, RFC2, RRS1, SF3A1, SMC4, SNRNP40, SYMPK, QARS1

### Function

The module is best interpreted as a conserved nuclear RNA-processing and gene-expression module. The primary evidence is the globally corrected enrichment for nucleic acid metabolic process (GO:BP nucleic acid metabolic process; q_global = 0.0204), nucleic acid biosynthetic process (GO:BP nucleic acid biosynthetic process; q_global = 0.0224), mRNA metabolic process (GO:BP mRNA metabolic process; q_global = 0.032), and RNA metabolic process (GO:BP RNA metabolic process; q_global = 0.0394). The broad overlap with these terms, together with the presence of spliceosome-related genes such as SNRNP40, DDX46, SF3A1, PRMT5, ACIN1, and SYMPK, supports coordinated pre-mRNA processing, spliceosome assembly or function, RNA maturation, and post-transcriptional regulation. Additional genes connect this core to chromatin regulation, transcriptional control, ribosome biogenesis, DNA replication, chromosome organization, translation, and mRNA stability. The absence of STRING functional enrichment does not negate the module, because the GO evidence and the gene functions support a coherent biological interpretation.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly nuclear, nucleolar, nuclear-speckle, nucleoplasmic, or cytosolic. Most genes have low tissue specificity and low immune-cell specificity, which is consistent with broadly expressed housekeeping or core gene-expression machinery rather than a specialized autonomic or ovarian secretory program. All module genes have detected protein expression in ovary, whereas matching HPA tissue data are unavailable for autonomic nervous system. Several genes show cell-type-enhanced expression in reproductive, epithelial, progenitor, or neural-related cell types, so some co-abundance could reflect shared proliferative or RNA-processing demands across cell populations. The HPA evidence does not strongly support blood contamination as the main explanation, although the enhanced expression of SMC4 in lymphoid and hematopoietic cell types warrants attention when interpreting tissue mixtures.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP nucleic acid metabolic process | 0.0204 | ACIN1, ADNP, CHD4, DDX46, PRMT5, PUM1, QARS1, RBM33, RFC2, RRS1, SF3A1, SNRNP40, SYMPK |
| GO:BP nucleic acid biosynthetic process | 0.0224 | ACIN1, ADNP, CHD4, DDX46, PRMT5, PUM1, QARS1, RFC2, RRS1, SF3A1, SNRNP40, SYMPK |
| GO:BP mRNA metabolic process | 0.032 | ACIN1, DDX46, PRMT5, PUM1, RBM33, SF3A1, SNRNP40, SYMPK |
| GO:BP RNA metabolic process | 0.0394 | ACIN1, ADNP, CHD4, DDX46, PRMT5, PUM1, QARS1, RBM33, RRS1, SF3A1, SNRNP40, SYMPK |

### STRING and hu.MAP

The STRING evidence indicates a small set of established or strongly supported relationships within the module: ACIN1 with CHD4, ADNP with CHD4, DDX46 with SF3A1, and SF3A1 with SNRNP40. These links provide direct support for parts of the chromatin-regulatory and spliceosomal interpretation, but the lack of STRING functional enrichment and the limited number of high-confidence links mean that the co-abundance network should not be treated as a fully validated physical complex. hu.MAP provides stronger complex-level support for a spliceosome-related assembly. PRMT5, SF3A1, DDX46, and SNRNP40 occur together in (hu.MAP huMAP3_08980.1), while PRMT5, SF3A1, and DDX46 recur in (hu.MAP huMAP3_06511.1), and SF3A1 with DDX46 recur in (hu.MAP huMAP3_04549.1). The overlap across these complexes particularly supports a spliceosome or snRNP-associated core. Genes connected to this core by co-abundance, including PUM1, RBM33, SYMPK, QARS1, RFC2, RRS1, and SMC4, may represent linked RNA regulation, translation, ribosome production, replication, or cell-cycle state rather than members of the same physical complex.

**STRING interactions (score >= 0.7)**: 4 of 91 gene pairs: ACIN1–CHD4 (0.82); ADNP–CHD4 (0.991); DDX46–SF3A1 (0.999); SF3A1–SNRNP40 (0.94)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (PRMT5, SF3A1, DDX46, SNRNP40; 4/97); huMAP3_06511.1 (PRMT5, SF3A1, DDX46; 3/79); huMAP3_04549.1 (SF3A1, DDX46; 2/52)

### Novelty

The biological mechanism represented by the module is not, by itself, a new molecular process: spliceosome function, RNA processing, chromatin regulation, and core gene-expression machinery are established biology, and several relationships are already represented in STRING and hu.MAP. A potentially novel aspect is the reproducible co-abundance of this particular gene combination across autonomic nervous system and ovary. However, the fact sheet does not establish that this tissue-pair module has not been reported previously, and absence of a relationship from STRING or hu.MAP would not prove novelty. The scientifically defensible conclusion is that the shared co-abundance configuration may be a new observation, while the underlying molecular functions are established and should not be claimed as newly discovered.

**Hypothesis.** Hypothesis: the conserved module reflects a shared demand for coordinated nuclear RNA handling in autonomic nervous system and ovary cells, with a spliceosome-associated core centered on SNRNP40, DDX46, SF3A1, and PRMT5. This core may be coupled to chromatin remodeling through CHD4 and ADNP, RNA stability and translation control through PUM1 and RBM33, and proliferative or chromosome-associated processes through RFC2, SMC4, and RRS1. In ovary, the signal may be especially visible because these processes support oocyte or follicular-cell gene-expression programs; in autonomic nervous system, it may reflect the general maintenance and differentiation requirements of neural or neural-associated cells. This is a mechanistic proposal, not evidence that the genes physically act as one complex or that the module is specific to either tissue.

### Important genes

#### SNRNP40

- **Related proteins** (co-abundance neighbors): ACIN1 (0.87), PRMT5 (0.86), DDX46 (0.85), QARS1 (0.85), CHD4 (0.84), SYMPK (0.82), SMC4 (0.80); STRING partners: SF3A1 (0.94)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 40. This gene encodes a component of the U5 small nuclear ribonucleoprotein (snRNP) particle. The U5 snRNP is part of the spliceosome, a multiprotein complex that catalyzes the removal of introns from pre-messenger RNAs. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.530); dengue disease (0.377); X-linked lymphoproliferative syndrome (0.058); autoimmune lymphoproliferative syndrome (0.055); Familial hemophagocytic lymphohistiocytosis (0.053)
- **Europe PMC papers**: 235
- **Why important**: SNRNP40 has the strongest network position in the module and connects the spliceosome-associated core to multiple other module genes, including DDX46, SF3A1, PRMT5, ACIN1, CHD4, QARS1, SYMPK, and SMC4. It is a U snRNP component involved in spliceosomal assembly, conformational change, and mRNA splicing. It is present in the high-confidence hu.MAP spliceosome-related complex (hu.MAP huMAP3_08980.1), and it has a STRING relationship with SF3A1. Its nuclear-speckle localization and ovarian protein detection are consistent with the inferred function. The gene has substantial literature coverage and reported associations with neurodegenerative and immune-related diseases.
- **Conclusion**: Established evidence supports SNRNP40 as a central spliceosome-related hub and a strong marker of the module's RNA-processing function. The hypothesis that it organizes the broader tissue-shared co-abundance program remains unproven because co-abundance and network centrality do not demonstrate causal control.

#### DDX46

- **Related proteins** (co-abundance neighbors): SNRNP40 (0.85), SF3A1 (0.84), SMC4 (0.82), PUM1 (0.81), RBM33 (0.81); STRING partners: SF3A1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_06511.1, huMAP3_04549.1
- **Function (MyGene.info)**: DEAD-box helicase 46. This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribu…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); dengue disease (0.370); Hypercholesterolemia (0.203); lung adenocarcinoma (0.074); osteosarcoma (0.053)
- **Europe PMC papers**: 592
- **Why important**: DDX46 is a high-connectivity module gene and links SNRNP40, SF3A1, SMC4, PUM1, and RBM33. It is a DEAD-box RNA helicase implicated in RNA secondary-structure remodeling, spliceosome assembly, and U two-type prespliceosome assembly. It participates in all reported hu.MAP complexes (hu.MAP huMAP3_08980.1), (hu.MAP huMAP3_06511.1), and (hu.MAP huMAP3_04549.1), and has a very strong STRING relationship with SF3A1. Its nuclear-speckle localization and ovarian detection reinforce the RNA-processing interpretation. Its disease associations include neurodegenerative disease and several other disorders, and its literature coverage is substantial.
- **Conclusion**: Established evidence identifies DDX46 as a plausible connector between spliceosome assembly and broader RNA regulation within the module. A tissue-specific role in coordinating autonomic or ovarian cell-state programs is a hypothesis rather than an established conclusion.

#### SF3A1

- **Related proteins** (co-abundance neighbors): DDX46 (0.84); STRING partners: DDX46 (0.999), SNRNP40 (0.94)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_06511.1, huMAP3_04549.1
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 is a core U two snRNP and spliceosome component involved in splice-site recognition, snRNP assembly, and mRNA splicing. Although its co-abundance degree is modest, it has strong support from STRING relationships with DDX46 and SNRNP40 and appears in all three hu.MAP complexes (hu.MAP huMAP3_08980.1), (hu.MAP huMAP3_06511.1), and (hu.MAP huMAP3_04549.1). It therefore provides some of the clearest independent evidence that the module contains a spliceosome-associated physical component. It is localized to the nucleoplasm and nuclear speckles, detected in ovary, and has disease associations spanning neurological, malignant, metabolic, and infectious conditions.
- **Conclusion**: Established evidence supports SF3A1 as a physically and functionally anchored spliceosomal component of the module. Its contribution to the shared tissue-pair signal is likely to be core RNA processing, but any special role in autonomic-ovarian biology remains hypothetical.

#### PRMT5

- **Related proteins** (co-abundance neighbors): SNRNP40 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_06511.1
- **Function (MyGene.info)**: protein arginine methyltransferase 5. This gene encodes an enzyme that belongs to the methyltransferase family. The encoded protein catalyzes the transfer of methyl groups to the amino acid arginine, in target proteins that include histones, transcriptional elongation factors and the tumor suppressor p53. This gene plays a role in several cellular processes, including transcriptional regulation, and the assembly of small nuclear ribon…
- **Diseases (Open Targets)**: neurodegenerative disease (0.207); breast cancer (0.140); neoplasm (0.119); hepatocellular carcinoma (0.117); colorectal carcinoma (0.116)
- **Europe PMC papers**: 6035
- **Why important**: PRMT5 is an enzyme that methylates arginine residues in proteins including histones, transcriptional factors, and p53, and it contributes to snRNP assembly, chromatin remodeling, transcriptional regulation, and mitotic control. It occurs in hu.MAP complexes (hu.MAP huMAP3_08980.1) and (hu.MAP huMAP3_06511.1) with the spliceosome-associated genes. Its ovarian and oocyte-enhanced HPA expression is particularly relevant to the tissue pair, while its broad disease literature includes neurodegenerative disease and multiple cancers. Its network degree is limited, so its importance comes more from biochemical function and complex membership than from graph centrality.
- **Conclusion**: Established evidence supports PRMT5 as a regulatory bridge between RNA processing, chromatin state, and transcription. It is plausible that PRMT5 helps tune the module according to cell state, including ovarian germ-cell state, but the co-abundance data do not establish that it drives the module.

#### CHD4

- **Related proteins** (co-abundance neighbors): SNRNP40 (0.84); STRING partners: ACIN1 (0.82), ADNP (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromodomain helicase DNA binding protein 4. The product of this gene belongs to the SNF2/RAD54 helicase family. It represents the main component of the nucleosome remodeling and deacetylase complex and plays an important role in epigenetic transcriptional repression. Patients with dermatomyositis develop antibodies against this protein. Somatic mutations in this gene are associated with serous endometrial tumors. Alternative splicing result…
- **Diseases (Open Targets)**: Sifrim-Hitz-Weiss syndrome (0.810); neurodegenerative disease (0.551); hereditary disease (0.505); endometrial cancer (0.470); uterine carcinosarcoma (0.439)
- **Europe PMC papers**: 3617
- **Why important**: CHD4 is a major component of the nucleosome remodeling and deacetylase complex and participates in chromatin remodeling, transcriptional repression, DNA repair, and cell-fate regulation. It connects to SNRNP40 in the module and has STRING relationships with ACIN1 and ADNP, providing a chromatin-associated branch alongside the spliceosome core. Its neural and glial cell-type-enhanced HPA pattern is relevant to the autonomic nervous system context, while it is also detected in ovary. CHD4 has extensive literature and disease associations including developmental syndromes and endometrial cancer.
- **Conclusion**: Established evidence supports CHD4 as a chromatin-regulatory partner that could connect RNA processing with transcriptional and epigenetic control. Its tissue-pair relevance is a hypothesis, because the current evidence does not show whether the CHD4-associated branch is active in the same cells as the spliceosomal branch.

## Module 1

**Tissue pair**: autonomic_nervous_system and ovary  
**Genes (7)**: ACSL3, EGFR, EMC1, ITGB1, IMMT, SSR1, TFRC

### Function

This is a membrane-associated receptor and protein-trafficking module. The strongest primary evidence is the coordinated enrichment of receptor-complex components and exogenous-protein binding (GO:CC receptor complex; q_global = 0.0186)(GO:MF exogenous protein binding; q_global = 0.0186), driven by EGFR, ITGB1, and TFRC. The same genes support virus-receptor activity (GO:MF virus receptor activity; q_global = 0.0149), but this should be interpreted as a shared receptor property rather than evidence that the module specifically represents antiviral biology. ACSL3, EGFR, and ITGB1 support positive regulation of protein localization to the plasma membrane (GO:BP positive regulation of protein localization to plasma membrane; q_global = 0.0276)(GO:BP positive regulation of protein localization to membrane; q_global = 0.0447), while ACSL3, EGFR, EMC1, ITGB1, and SSR1 support membrane localization and establishment of protein localization to membranes (GO:BP localization within membrane; q_global = 0.0329)(GO:BP establishment of protein localization to membrane; q_global = 0.0338). Overall, the module is most consistent with coordinated cell-surface receptor organization, membrane delivery, endocytic handling, and associated lipid or organelle-membrane biology. No KEGG term is listed among the globally significant primary terms.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only EGFR and TFRC are annotated as secreted to blood, whereas the other genes are intracellular, endoplasmic-reticulum, mitochondrial, or membrane-associated proteins. HPA indicates generally low tissue specificity for much of the module, with tissue-enhanced signals involving parathyroid gland, placenta, and tongue. Cell-type enhancement is frequent, including trophoblast, oocyte, epithelial, stromal, and myeloid-related cell types. Blood-cell specificity is mostly low, although TFRC is immune-cell enhanced in non-classical monocytes. Thus, the module does not look like a simple blood-protein signature, but shared cell composition or membrane-rich cell populations could contribute to its conservation between autonomic nervous system and ovary. The ovary protein data support expression for much of the module, while IMMT and SSR1 lack ovary protein detection in the supplied HPA summary.

**GO/KEGG enrichment**: 7 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF virus receptor activity | 0.0149 | EGFR, ITGB1, TFRC |
| GO:CC receptor complex | 0.0186 | EGFR, ITGB1, TFRC |
| GO:MF exogenous protein binding | 0.0186 | EGFR, ITGB1, TFRC |
| GO:BP positive regulation of protein localization to plasma membrane | 0.0276 | ACSL3, EGFR, ITGB1 |
| GO:BP localization within membrane | 0.0329 | ACSL3, EGFR, EMC1, ITGB1, SSR1 |
| GO:BP establishment of protein localization to membrane | 0.0338 | ACSL3, EGFR, EMC1, SSR1 |
| GO:BP positive regulation of protein localization to membrane | 0.0447 | ACSL3, EGFR, ITGB1 |

### STRING and hu.MAP

The strongest known STRING relationships form a receptor-associated triangle among EGFR, ITGB1, and TFRC. STRING also independently assigns these genes to receptor complexes, virus-entry receptor functions, and membrane-protein categories (STRING Keyword Host cell receptor for virus entry; within-query FDR = 0.0012)(STRING Component Receptor complex; within-query FDR = 0.0036)(STRING COMPARTMENTS Receptor complex; within-query FDR = 0.0091)(STRING Function Virus receptor activity; within-query FDR = 0.0102)(STRING Component Membrane protein complex; within-query FDR = 0.0165). The broader STRING annotations support transmembrane, integral-membrane, organelle-membrane, glycoprotein, and signal-related properties across the module (STRING Keyword Transmembrane helix; within-query FDR = 5.15e-05)(STRING Component Integral component of membrane; within-query FDR = 0.002)(STRING Keyword Glycoprotein; within-query FDR = 0.0049)(STRING COMPARTMENTS Organelle membrane; within-query FDR = 0.007)(STRING Component Organelle membrane; within-query FDR = 0.0165)(STRING Keyword Signal; within-query FDR = 0.0271). These results provide external support for the receptor and membrane interpretation, but the STRING enrichments are supplementary rather than globally corrected primary evidence. ACSL3 is the most centrally connected gene in the co-abundance subgraph and links the receptor-associated genes with EMC1, suggesting a bridge between receptor biology and lipid or membrane organization. IMMT, EMC1, and SSR1 are peripheral connectors in the co-abundance structure. No hu.MAP complex contains multiple members of this module, so there is no independent curated human complex supporting the entire module.

**STRING interactions (score >= 0.7)**: 3 of 21 gene pairs: EGFR–ITGB1 (0.966); EGFR–TFRC (0.832); ITGB1–TFRC (0.838)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transmembrane helix (FDR = 5.15e-05, 7 genes); Keyword Host cell receptor for virus entry (FDR = 0.0012, 3 genes); Component Integral component of membrane (FDR = 0.002, 7 genes); Component Receptor complex (FDR = 0.0036, 3 genes); Keyword Glycoprotein (FDR = 0.0049, 5 genes); COMPARTMENTS Organelle membrane (FDR = 0.007, 7 genes); COMPARTMENTS Receptor complex (FDR = 0.0091, 3 genes); Function Virus receptor activity (FDR = 0.0102, 3 genes); Component Organelle membrane (FDR = 0.0165, 7 genes); Component Membrane protein complex (FDR = 0.0165, 5 genes); Keyword Signal (FDR = 0.0271, 4 genes); TISSUES Placenta (FDR = 0.0309, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module-level co-abundance pattern may be a new observation because the conserved association between autonomic nervous system and ovary, including the linkage of receptor genes with membrane-trafficking, lipid, ER, and mitochondrial genes, is not represented by a corresponding hu.MAP multi-member complex. However, the underlying biology is not wholly novel: EGFR, ITGB1, and TFRC already have strong known STRING relationships and well-established receptor or trafficking functions. Absence from hu.MAP or absence of additional STRING edges cannot by itself establish novelty. The defensible conclusion is that the potentially novel finding is the cross-tissue co-abundance organization and its particular combination of genes, not the existence or function of the individual proteins.

**Hypothesis.** Hypothesis: in both autonomic nervous system and ovary, a shared cell population or conserved physiological state coordinates plasma-membrane receptor abundance with membrane insertion, lipid handling, and receptor-mediated endocytosis. ACSL3 may help maintain the lipid environment needed for membrane organization, EMC1 and SSR1 may support ER insertion and cotranslational membrane targeting, and EGFR, ITGB1, and TFRC may form the functionally visible receptor and trafficking arm. This could couple adhesion and growth-factor signaling through EGFR and ITGB1 with iron uptake through TFRC. The data support this as a mechanistic model, but co-abundance and annotation evidence do not establish physical interaction, causal regulation, or a virus-specific role.

### Important genes

#### EGFR

- **Related proteins** (co-abundance neighbors): ACSL3 (0.82); STRING partners: ITGB1 (0.966), TFRC (0.832)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus, Plasma membrane; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: epidermal growth factor receptor. The protein encoded by this gene is a transmembrane glycoprotein that is a member of the protein kinase superfamily. This protein is a receptor for members of the epidermal growth factor family. EGFR is a cell surface protein that binds to epidermal growth factor, thus inducing receptor dimerization and tyrosine autophosphorylation leading to cell proliferation. Mutations in this gene are associat…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.850); lung adenocarcinoma (0.774); cancer (0.737); head and neck squamous cell carcinoma (0.725); lung cancer (0.717)
- **Europe PMC papers**: 223694
- **Why important**: EGFR is a membrane receptor tyrosine kinase and the most extensively studied gene in the module. It participates in the globally supported receptor-complex, exogenous-protein-binding, virus-receptor, and membrane-localization terms (GO:MF virus receptor activity; q_global = 0.0149)(GO:CC receptor complex; q_global = 0.0186)(GO:MF exogenous protein binding; q_global = 0.0186)(GO:BP positive regulation of protein localization to plasma membrane; q_global = 0.0276)(GO:BP localization within membrane; q_global = 0.0329)(GO:BP establishment of protein localization to membrane; q_global = 0.0338)(GO:BP positive regulation of protein localization to membrane; q_global = 0.0447). It has a direct STRING relationship with ITGB1 and TFRC and is annotated in the ovary and placenta-associated HPA patterns. Its extensive disease and literature associations make it the clearest signaling anchor.
- **Conclusion**: Established evidence supports EGFR as a cell-surface signaling and membrane-trafficking component of the module, with known relationships to ITGB1 and TFRC. It is plausible, but not established from these data, that EGFR signaling helps coordinate the conserved co-abundance pattern between the two tissues.

#### ITGB1

- **Related proteins** (co-abundance neighbors): IMMT (0.85), SSR1 (0.82), ACSL3 (0.82); STRING partners: EGFR (0.966), TFRC (0.838)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 has strong structural importance in the co-abundance network and is part of every primary receptor-related signal involving the EGFR-ITGB1-TFRC group (GO:MF virus receptor activity; q_global = 0.0149)(GO:CC receptor complex; q_global = 0.0186)(GO:MF exogenous protein binding; q_global = 0.0186)(GO:BP positive regulation of protein localization to plasma membrane; q_global = 0.0276)(GO:BP localization within membrane; q_global = 0.0329)(GO:BP positive regulation of protein localization to membrane; q_global = 0.0447). Its established integrin function connects cell adhesion, extracellular recognition, tissue repair, immune processes, and signaling. HPA places it at the plasma membrane and focal adhesions, with ovary protein detection, and STRING supports its relationships with EGFR and TFRC.
- **Conclusion**: Established evidence identifies ITGB1 as the adhesion and receptor-complex component linking membrane organization to cell-cell or cell-matrix interactions. A role in coordinating tissue-specific signaling or cell-state composition is a hypothesis rather than a demonstrated mechanism here.

#### TFRC

- **Related proteins** (co-abundance neighbors): ACSL3 (0.81); STRING partners: EGFR (0.832), ITGB1 (0.838)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes, Lysosomes; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transferrin receptor. This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: TFRC-related combined immunodeficiency (0.623); type 2 diabetes mellitus (0.518); mucopolysaccharidosis type 2 (0.490); diabetes mellitus (0.471); diabetic retinopathy (0.343)
- **Europe PMC papers**: 14164
- **Why important**: TFRC is a receptor for cellular iron uptake and is part of the known STRING receptor-associated group with EGFR and ITGB1. It contributes to the primary receptor-complex, exogenous-protein-binding, and virus-receptor terms (GO:MF virus receptor activity; q_global = 0.0149)(GO:CC receptor complex; q_global = 0.0186)(GO:MF exogenous protein binding; q_global = 0.0186). Its annotations connect the module to receptor-mediated endocytosis, iron homeostasis, hypoxia response, erythropoiesis, and neurologic development. HPA shows cell-type enhancement in erythroid, macrophage, monocyte, and trophoblast-related populations and secretion to blood.
- **Conclusion**: Established evidence supports TFRC as an endocytic and iron-homeostasis component that may explain part of the module's shared membrane-receptor signature. Its immune-cell enhancement raises a possible cell-composition contribution, but the supplied data do not show that blood contamination is the cause of the module.

#### ACSL3

- **Related proteins** (co-abundance neighbors): EMC1 (0.84), EGFR (0.82), ITGB1 (0.82), TFRC (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 3. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme is highly expressed…
- **Diseases (Open Targets)**: prostate adenocarcinoma (0.370); acute myeloid leukemia (0.313); neurodegenerative disease (0.300); ovarian dysfunction (0.253); Abnormality of the skeletal system (0.215)
- **Europe PMC papers**: 2930
- **Why important**: ACSL3 is the most centrally connected gene in the co-abundance subgraph and links receptor-associated genes with EMC1. It participates in all of the primary membrane-localization terms involving lipid or membrane positioning (GO:BP positive regulation of protein localization to plasma membrane; q_global = 0.0276)(GO:BP localization within membrane; q_global = 0.0329)(GO:BP establishment of protein localization to membrane; q_global = 0.0338)(GO:BP positive regulation of protein localization to membrane; q_global = 0.0447). Its established enzyme function converts long-chain fatty acids into fatty acyl-CoA esters, connecting the module to lipid biosynthesis, fatty-acid degradation, neuron differentiation, and membrane composition. It is highly expressed in brain according to the supplied annotation and has reported associations with neurodegenerative disease and ovarian dysfunction.
- **Conclusion**: Established evidence supports ACSL3 as a lipid-metabolism and membrane-organization bridge within the module. Its central network position makes it a strong candidate for coordinating the receptor-rich arm with membrane biology, but that regulatory role remains a hypothesis.

## Module 2

**Tissue pair**: autonomic_nervous_system and ovary  
**Genes (16)**: AIMP1, BCLAF1, EIF2A, FAM120A, FNTA, HMG20A, KIF2A, MMTAG2, PRRC2C, RBM15, RRP1B, SNW1, SRP54, DNTTIP2, XRN2, ZC3HAV1

### Function

The strongest interpretation is a broadly distributed nuclear and cytoplasmic RNA and nucleic-acid regulation module. (GO:MF RNA binding; q_global = 0.0112) identifies RNA binding as globally significant, with most module genes represented, and (GO:MF nucleic acid binding; q_global = 0.0227) identifies nucleic-acid binding as globally significant. The genes span RNA binding, RNA splicing, transcriptional regulation, RNA degradation, ribosomal RNA processing, translation initiation, stress-granule assembly, and signal-recognition-particle activity. This is therefore better described as an RNA-processing and gene-expression regulatory program than as a tissue-specific autonomic or ovarian pathway. The presence of XRN2, RRP1B, DNTTIP2, RBM15, SNW1, BCLAF1, and ZC3HAV1 supports coordinated control of RNA maturation, turnover, transcription, splicing, and antiviral RNA surveillance. The enrichment evidence supports the shared molecular function, but it does not establish that all genes form one physical complex or that the module has a single biochemical activity.

**Cell composition.** The module is predominantly composed of intracellular, broadly expressed proteins rather than plasma or secreted proteins. HPA classifies most genes as having low tissue specificity, and all module genes have low immune-cell specificity. Only AIMP1 is annotated as secreted to blood, so a plasma-protein explanation is unlikely. There is no broad blood-cell enrichment pattern, although ZC3HAV1 and XRN2 show cell-type enhancement involving neutrophils, and several genes show enhancement in reproductive or other specialized cell types. The module is detected at the protein level for most genes in ovary, whereas matching autonomic-nervous-system protein data are unavailable. Thus, the shared signal is more plausibly a conserved housekeeping-like RNA and gene-expression program, or a shared cellular-state signal, than simple blood contamination. The HPA data do not exclude contributions from particular cell populations, especially because several genes have cell-type-enhanced expression.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF RNA binding | 0.0112 | AIMP1, BCLAF1, C1orf35, DNTTIP2, EIF2A, FAM120A, PRRC2C, RBM15, RRP1B, SNW1, SRP54, XRN2, ZC3HAV1 |
| GO:MF nucleic acid binding | 0.0227 | AIMP1, BCLAF1, C1orf35, DNTTIP2, EIF2A, FAM120A, HMG20A, PRRC2C, RBM15, RRP1B, SNW1, SRP54, XRN2, ZC3HAV1 |

### STRING and hu.MAP

STRING provides direct high-confidence support for BCLAF1 relationships with RBM15 and SNW1. These links connect RNA-binding and transcriptional or splicing-related components and are consistent with the module's primary functional interpretation. The remaining co-abundance relationships are not broadly represented as high-confidence STRING pairwise interactions, so the co-abundance network extends beyond currently catalogued physical associations. hu.MAP identifies (hu.MAP huMAP3_05807.1), containing DNTTIP2, ZC3HAV1, MMTAG2, and FAM120A among a much larger complex annotation. That complex also contains RNA-processing, ribosomal, mitochondrial, chromatin, and splicing-related proteins, which is compatible with a gene-expression machinery context but does not prove that the entire module is one complex. Together, STRING and hu.MAP support selected known molecular relationships while indicating that much of the module's co-abundance structure may reflect shared regulation, cellular state, or indirect functional coupling.

**STRING interactions (score >= 0.7)**: 2 of 120 gene pairs: BCLAF1–RBM15 (0.72); BCLAF1–SNW1 (0.823)
**STRING functional enrichment (supplementary, within-query FDR)**: Function RNA binding (FDR = 0.0072, 13 genes); Function Nucleic acid binding (FDR = 0.0105, 14 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05807.1 (DNTTIP2, ZC3HAV1, MMTAG2, FAM120A; 4/81)

### Novelty

This module should be regarded as a potentially new cross-tissue co-abundance pattern, but not as a newly discovered molecular pathway. The RNA-binding and nucleic-acid-binding functions are established and supported independently by (GO:MF RNA binding; q_global = 0.0112), (GO:MF nucleic acid binding; q_global = 0.0227), (STRING Function RNA binding; within-query FDR = 0.0072), and (STRING Function Nucleic acid binding; within-query FDR = 0.0105). Some internal relationships are already known through STRING and (hu.MAP huMAP3_05807.1), while many module pairs lack catalogued STRING or hu.MAP support. Therefore, absence from those resources cannot establish novelty; it may reflect incomplete interaction coverage, indirect co-regulation, or context-specific biology. The more defensible novelty claim is that this particular coordinated expression pattern is shared by autonomic nervous system and ovary and may reveal a conserved tissue-pair molecular state. Validation would require replication in independent cohorts, preservation of the module across datasets, and testing whether the co-abundance relationships persist after controlling for cell composition and technical effects.

**Hypothesis.** Hypothesis: the shared module represents a conserved RNA-homeostasis and adaptive gene-expression state that coordinates transcriptional regulation, alternative splicing, RNA surveillance, ribosomal RNA processing, translation initiation, and stress responses in cells present in both tissues. SNW1, RBM15, and BCLAF1 may provide regulatory or splicing-related coordination, while XRN2, RRP1B, and DNTTIP2 may support RNA processing and turnover. ZC3HAV1 could connect this state to antiviral RNA degradation and innate immune signaling, and AIMP1 could provide a context-dependent link between translation machinery, inflammation, angiogenesis, and extracellular signaling. This remains a hypothesis because co-abundance does not establish directionality, physical binding, or causal regulation.

### Important genes

#### SNW1

- **Related proteins** (co-abundance neighbors): DNTTIP2 (0.91), HMG20A (0.87), BCLAF1 (0.86), FNTA (0.84), FAM120A (0.82); STRING partners: BCLAF1 (0.823)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SNW domain containing 1. This gene, a member of the SNW gene family, encodes a coactivator that enhances transcription from some Pol II promoters. This coactivator can bind to the ligand-binding domain of the vitamin D receptor and to retinoid receptors to enhance vitamin D-, retinoic acid-, estrogen-, and glucocorticoid-mediated gene expression. It can also function as a splicing factor by interacting with poly(A)-bindin…
- **Diseases (Open Targets)**: cancer (0.580); dengue disease (0.370); neurodegenerative disease (0.261); congenital lactic acidosis, Saguenay-Lac-Saint-Jean type (0.118); chondromalacia (0.052)
- **Europe PMC papers**: 653
- **Why important**: SNW1 has the strongest network connectivity in the module and links DNTTIP2, HMG20A, BCLAF1, FNTA, and FAM120A. It is represented in (GO:MF RNA binding; q_global = 0.0112), (GO:MF nucleic acid binding; q_global = 0.0227), (STRING Function RNA binding; within-query FDR = 0.0072), and (STRING Function Nucleic acid binding; within-query FDR = 0.0105). Its established functions include transcriptional coactivation, spliceosome-related activity, and modulation of vitamin D-, retinoic acid-, estrogen-, and glucocorticoid-mediated gene expression. Its substantial literature volume and association with cancer and neurodegenerative disease make it a strong candidate for coordinating the shared regulatory state.
- **Conclusion**: Established: SNW1 is a nuclear transcriptional coactivator and splicing-related protein positioned centrally in this co-abundance network. Hypothesis: SNW1 may act as a principal regulatory bridge connecting tissue-responsive transcription with RNA processing in the shared module.

#### RBM15

- **Related proteins** (co-abundance neighbors): ZC3HAV1 (0.88), AIMP1 (0.84); STRING partners: BCLAF1 (0.72)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 15. Members of the SPEN (Split-end) family of proteins, including RBM15, have repressor function in several signaling pathways and may bind to RNA through interaction with spliceosome components (Hiriart et al., 2005 [PubMed 16129689]).[supplied by OMIM, Feb 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); lung adenocarcinoma (0.219); esophageal squamous cell carcinoma (0.209); osteosarcoma (0.209); hepatocellular carcinoma (0.206)
- **Europe PMC papers**: 3897
- **Why important**: RBM15 is a core RNA-binding gene represented in (GO:MF RNA binding; q_global = 0.0112), (GO:MF nucleic acid binding; q_global = 0.0227), (STRING Function RNA binding; within-query FDR = 0.0072), and (STRING Function Nucleic acid binding; within-query FDR = 0.0105). It connects ZC3HAV1 and AIMP1 in the module and has a known STRING relationship with BCLAF1. Its established biology includes alternative mRNA splicing, RNA methylation, and regulation of myeloid and megakaryocyte differentiation. It has the largest literature volume among the selected genes and substantial disease associations involving neurodegeneration and cancer.
- **Conclusion**: Established: RBM15 is a multifunctional RNA regulator with links to splicing, RNA modification, and cell differentiation. Hypothesis: RBM15 may connect RNA processing to cell-state or lineage-related regulation in the shared autonomic-nervous-system and ovarian context.

#### ZC3HAV1

- **Related proteins** (co-abundance neighbors): MMTAG2 (0.91), RBM15 (0.88), SRP54 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_05807.1
- **Function (MyGene.info)**: zinc finger CCCH-type containing, antiviral 1. This gene encodes a CCCH-type zinc finger protein. This antiviral protein inhibits viral replication by recruiting cellular RNA degradation machineries to degrade viral mRNAs. The encoded protein plays an important role in the innate immune response against multiple DNA and RNA viruses, including Ebola virus, HIV and SARS-CoV-2 (which causes COVID-19). [provided by RefSeq, Sep 2021].
- **Diseases (Open Targets)**: cancer (0.549); hypothyroidism (0.429); neurodegenerative disease (0.358); autoimmune disease (0.308); Hashimoto thyroiditis (0.306)
- **Europe PMC papers**: 979
- **Why important**: ZC3HAV1 is represented in (GO:MF RNA binding; q_global = 0.0112), (GO:MF nucleic acid binding; q_global = 0.0227), (STRING Function RNA binding; within-query FDR = 0.0072), and (STRING Function Nucleic acid binding; within-query FDR = 0.0105), connects MMTAG2, RBM15, and SRP54, and is part of (hu.MAP huMAP3_05807.1). Its established function is antiviral RNA surveillance through recruitment of RNA-degradation machinery, with effects on interferon and NF-kappa-B signaling. HPA shows tissue enhancement in bone marrow and cell-type enhancement in endometrial cells, neutrophils, NK cells, and pDCs. Its disease associations include cancer, autoimmune disease, and neurodegenerative disease, supported by substantial literature.
- **Conclusion**: Established: ZC3HAV1 is an RNA-degradation and innate-immune regulator embedded in the module's RNA-binding core. Hypothesis: it may mark an inducible RNA-surveillance component of the shared module rather than indicating that the entire module is an immune-cell module.

#### BCLAF1

- **Related proteins** (co-abundance neighbors): SNW1 (0.86), KIF2A (0.83); STRING partners: RBM15 (0.72), SNW1 (0.823)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BCL2 associated transcription factor 1. This gene encodes a transcriptional repressor that interacts with several members of the BCL2 family of proteins. Overexpression of this protein induces apoptosis, which can be suppressed by co-expression of BCL2 proteins. The protein localizes to dot-like structures throughout the nucleus, and redistributes to a zone near the nuclear envelope in cells undergoing apoptosis. Multiple transcript var…
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); Pulmonary artery atresia (0.416); acute myeloid leukemia (0.357); bronchial disorder (0.288); Vertigo (0.253)
- **Europe PMC papers**: 1702
- **Why important**: BCLAF1 is represented in (GO:MF RNA binding; q_global = 0.0112), (GO:MF nucleic acid binding; q_global = 0.0227), (STRING Function RNA binding; within-query FDR = 0.0072), and (STRING Function Nucleic acid binding; within-query FDR = 0.0105) and has known STRING relationships with SNW1 and RBM15, giving it a direct bridge between the module's best-supported interaction groups. Its established functions include transcriptional repression, apoptosis, DNA-damage response, and mRNA stabilization. HPA shows bone-marrow tissue enhancement and nuclear-speckle localization. Its disease associations include neurodegenerative disease and acute myeloid leukemia, and it has a substantial literature base.
- **Conclusion**: Established: BCLAF1 is a nuclear transcriptional and RNA-regulatory factor with known connections to other important module members. Hypothesis: it may integrate RNA processing with apoptosis or DNA-damage-related state changes in the shared tissues.

#### AIMP1

- **Related proteins** (co-abundance neighbors): RBM15 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aminoacyl tRNA synthetase complex interacting multifunctional protein 1. The protein encoded by this gene is a cytokine that is specifically induced by apoptosis, and it is involved in the control of angiogenesis, inflammation, and wound healing. The release of this cytokine renders the tumor-associated vasculature sensitive to tumor necrosis factor. The precursor protein is identical to the p43 subunit, which is associated with the multi-tRNA synthetase complex, and i…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 3 (0.790); Pelizaeus-Merzbacher-like disease (0.657); POLR-related leukodystrophy (0.657); leukodystrophy (0.372); autosomal recessive non-syndromic intellectual disability (0.371)
- **Europe PMC papers**: 663
- **Why important**: AIMP1 is represented in (GO:MF RNA binding; q_global = 0.0112), (GO:MF nucleic acid binding; q_global = 0.0227), (STRING Function RNA binding; within-query FDR = 0.0072), and (STRING Function Nucleic acid binding; within-query FDR = 0.0105) and connects RBM15 in the module. It has a dual established identity as a component of the multi-tRNA synthetase complex and as a secreted cytokine involved in angiogenesis, inflammation, wound healing, and leukocyte migration. It is the only module gene annotated as secreted to blood, making it a useful bridge between intracellular translation machinery and extracellular signaling. Its disease associations include several leukodystrophy-related disorders, and it has a substantial literature volume.
- **Conclusion**: Established: AIMP1 links translation-related intracellular biology with extracellular inflammatory and vascular signaling. Hypothesis: AIMP1 may couple the module's RNA and translation program to tissue remodeling or paracrine signaling, although its single secreted annotation does not imply that the module is plasma-derived.

## Module 3

**Tissue pair**: autonomic_nervous_system and ovary  
**Genes (10)**: ATP1A1, ATP5PB, ATL3, CANX, GNA11, GNAI3, OPA1, PITRM1, RAB8A, RHOG

### Function

The module is most strongly characterized by guanyl-nucleotide and GTPase biology, supported by the globally corrected terms (GO:MF GTPase activity; q_global = 0.000519) through (GO:MF hydrolase activity, acting on acid anhydrides, in phosphorus-containing anhydrides; q_global = 0.0134). Its core is a coordinated set of nucleotide-binding and nucleotide-hydrolysis proteins, including heterotrimeric G-protein alpha subunits, small GTPases, dynamin-like GTPases, and ATPase-associated proteins. The gene annotations further connect this signal to membrane and organelle organization, receptor-linked signal transduction, cytoskeletal remodeling, vesicle trafficking, endoplasmic-reticulum organization, mitochondrial maintenance, and ion-gradient control. The supplementary STRING annotations (STRING Function GTPase activity; within-query FDR = 0.00012) through (STRING Component Organelle membrane; within-query FDR = 0.0336) are concordant with this interpretation, especially for GTPase activity, membrane association, organelle membranes, and nucleoside-triphosphatase-related functions. Because the module is based on co-abundance rather than demonstrated physical binding, the most defensible interpretation is a shared cellular program coupling membrane signaling and trafficking with organelle and energetic homeostasis.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It also does not appear to be predominantly blood-cell enriched, because most genes have low immune-cell specificity and only GNA11 is reported as immune-cell enhanced for neutrophils. Most genes have low tissue specificity, while the tissue-enhanced signals are scattered across bone marrow, parathyroid gland, skeletal muscle, and tongue rather than concentrated in one tissue. The single-cell annotations are heterogeneous, with recurring signals in spermatid populations and additional signals in enterocytes, esophageal cells, neutrophils, and other cell types. This argues against a simple blood-contamination explanation, although shared cell states or differences in cellular composition could still contribute to the conserved co-abundance pattern. HPA protein detection in ovary is present for only a subset of genes, and there is no matching HPA tissue dataset for the autonomic nervous system, so tissue-level protein validation is incomplete.

**GO/KEGG enrichment**: 8 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF GTPase activity | 0.000519 | ATL3, GNA11, GNAI3, OPA1, RAB8A, RHOG |
| GO:MF GTP binding | 0.00205 | ATL3, GNA11, GNAI3, OPA1, RAB8A, RHOG |
| GO:MF guanyl nucleotide binding | 0.00205 | ATL3, GNA11, GNAI3, OPA1, RAB8A, RHOG |
| GO:MF guanyl ribonucleotide binding | 0.00205 | ATL3, GNA11, GNAI3, OPA1, RAB8A, RHOG |
| GO:MF ribonucleoside triphosphate phosphatase activity | 0.00955 | ATL3, ATP1A1, GNA11, GNAI3, OPA1, RAB8A, RHOG |
| GO:MF pyrophosphatase activity | 0.013 | ATL3, ATP1A1, GNA11, GNAI3, OPA1, RAB8A, RHOG |
| GO:MF hydrolase activity, acting on acid anhydrides | 0.0134 | ATL3, ATP1A1, GNA11, GNAI3, OPA1, RAB8A, RHOG |
| GO:MF hydrolase activity, acting on acid anhydrides, in phosphorus-containing anhydrides | 0.0134 | ATL3, ATP1A1, GNA11, GNAI3, OPA1, RAB8A, RHOG |

### STRING and hu.MAP

There are no high-confidence STRING pairwise interactions among the module genes. Thus, the STRING enrichment results (STRING Function GTPase activity; within-query FDR = 0.00012) through (STRING Component Organelle membrane; within-query FDR = 0.0336) should be read as annotation-level support for a coherent functional theme, not as evidence that the module forms a known physical complex. hu.MAP provides partial complex-level support: both (hu.MAP huMAP3_13105.1) and (hu.MAP huMAP3_11173.1) contain GNAI3 and GNA11 among larger G-protein-related assemblies. The remaining module genes are not represented as shared members of those reported hu.MAP complexes. Together, these results suggest a biologically convergent module assembled from related signaling, membrane, ER, and mitochondrial programs rather than a single established multiprotein complex.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Function GTPase activity (FDR = 0.00012, 6 genes); Keyword GTP-binding (FDR = 0.00016, 6 genes); Function GTP binding (FDR = 0.00059, 6 genes); Function Nucleoside-triphosphatase activity (FDR = 0.00059, 7 genes); Keyword Lipoprotein (FDR = 0.0027, 5 genes); Function Hydrolase activity (FDR = 0.0085, 8 genes); Keyword Membrane (FDR = 0.009, 9 genes); Keyword ADP-ribosylation (FDR = 0.0156, 3 genes); Keyword Palmitate (FDR = 0.0193, 3 genes); Keyword Nucleotide-binding (FDR = 0.0322, 7 genes); Component Organelle membrane (FDR = 0.0336, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13105.1 (GNAI3, GNA11; 2/27); huMAP3_11173.1 (GNAI3, GNA11; 2/34)

### Novelty

The shared co-abundance module may represent a novel cross-tissue association, but the fact sheet does not establish that it is a new biological mechanism. Its novelty is supported only in a limited sense: the complete module has no high-confidence STRING pairwise network, and only the GNAI3–GNA11 subset has partial hu.MAP support. However, the individual genes, their functions, and several of their disease links are well established, and the globally enriched GTPase terms are canonical rather than newly discovered. Therefore, the appropriate conclusion is that the cross-tissue co-abundance configuration is potentially novel, while its molecular functions are largely established. Replication in independent autonomic-nervous-system and ovary cohorts, control for cell composition, and comparison with other tissue-pair modules would be needed to claim a new finding.

**Hypothesis.** Hypothesis: in both autonomic nervous system and ovary, a shared cellular state increases coordination between G-protein-mediated signaling, small-GTPase-dependent membrane remodeling, ER and Golgi trafficking, mitochondrial organization, and maintenance of ion gradients. RHOG, RAB8A, and ATL3 could link membrane or vesicle dynamics with ER architecture; GNAI3 and GNA11 could relay receptor-associated signals; OPA1, ATP5PB, PITRM1, and ATP1A1 could reflect mitochondrial, proteostatic, energetic, and electrochemical demands. The co-abundance pattern may therefore arise from coordinated regulation of signaling and organelle homeostasis in shared responsive cell populations, rather than from direct physical interaction among all module members. This remains a hypothesis because the module contains no high-confidence STRING pairwise interactions and the data are co-abundance data.

### Important genes

#### RHOG

- **Related proteins** (co-abundance neighbors): ATL3 (0.85), PITRM1 (0.82), RAB8A (0.81), ATP1A1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ras homolog family member G. This gene encodes a member of the Rho family of small GTPases, which cycle between inactive GDP-bound and active GTP-bound states and function as molecular switches in signal transduction cascades. Rho proteins promote reorganization of the actin cytoskeleton and regulate cell shape, attachment, and motility. The encoded protein facilitates translocation of a functional guanine nucleotide exchange…
- **Diseases (Open Targets)**: atrial fibrillation (0.428); cancer (0.373); kidney transplant (0.296); eosinophilic esophagitis (0.239); cardiac arrhythmia (0.128)
- **Europe PMC papers**: 1929
- **Why important**: RHOG is a central network member by weighted connectivity and links several parts of the module, including ATL3, PITRM1, RAB8A, and ATP1A1. It is present in every primary enrichment term (GO:MF GTPase activity; q_global = 0.000519) through (GO:MF hydrolase activity, acting on acid anhydrides, in phosphorus-containing anhydrides; q_global = 0.0134) and in nearly all concordant STRING annotations. Its established Rho-family function connects the module to actin organization, cell polarity, cell shape, motility, and membrane recruitment of signaling machinery. Its disease associations include atrial fibrillation, cancer, kidney transplant, and eosinophilic esophagitis, while its literature volume is substantial.
- **Conclusion**: Established evidence supports RHOG as a small-GTPase and cytoskeletal-signaling component with a prominent position in this module. The hypothesis that RHOG is a principal bridge between membrane remodeling and mitochondrial or proteostatic genes is plausible from the co-abundance topology, but it is not demonstrated as a direct molecular interaction here.

#### GNAI3

- **Related proteins** (co-abundance neighbors): GNA11 (0.82), ATP1A1 (0.81), CANX (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Centrosome, Principal piece; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13105.1, huMAP3_11173.1
- **Function (MyGene.info)**: G protein subunit alpha i3. Guanine nucleotide-binding proteins (G proteins) are involved as modulators or transducers in various transmembrane signaling pathways. G proteins are composed of 3 units: alpha, beta and gamma. This gene encodes an alpha subunit and belongs to the G-alpha family. Mutation in this gene, resulting in a gly40-to-arg substitution, is associated with auriculocondylar syndrome, and shown to affect down…
- **Diseases (Open Targets)**: auriculocondylar syndrome (0.764); agnathia-otocephaly complex (0.370); hereditary disease (0.191); Abnormality of the skeletal system (0.140); frozen shoulder (0.135)
- **Europe PMC papers**: 1172
- **Why important**: GNAI3 is a network connector between GNA11, ATP1A1, and CANX, appears in every primary enrichment term (GO:MF GTPase activity; q_global = 0.000519) through (GO:MF hydrolase activity, acting on acid anhydrides, in phosphorus-containing anhydrides; q_global = 0.0134), and appears throughout the STRING functional annotations. It is also the only module gene shared with both reported hu.MAP complexes (hu.MAP huMAP3_13105.1) and (hu.MAP huMAP3_11173.1), together with GNA11. Its established role is as an inhibitory G-protein alpha subunit in receptor-linked signal transduction and adenylate-cyclase regulation. It has a documented association with auriculocondylar syndrome and a substantial literature base.
- **Conclusion**: Established evidence makes GNAI3 a strong signaling anchor and a plausible explanation for the module's G-protein enrichment. Its co-abundance with ER, membrane, and ion-transport genes supports a coordinated signaling-state interpretation, but does not prove that GNAI3 directly regulates the other module members in these tissues.

#### GNA11

- **Related proteins** (co-abundance neighbors): GNAI3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_13105.1, huMAP3_11173.1
- **Function (MyGene.info)**: G protein subunit alpha 11. The protein encoded by this gene belongs to the family of guanine nucleotide-binding proteins (G proteins), which function as modulators or transducers in various transmembrane signaling systems. G proteins are composed of 3 units: alpha, beta and gamma. This gene encodes one of the alpha subunits (subunit alpha-11). Mutations in this gene have been associated with hypocalciuric hypercalcemia type…
- **Diseases (Open Targets)**: familial hypoparathyroidism (0.754); familial hypocalciuric hypercalcemia 2 (0.736); autosomal dominant hypocalcemia (0.611); congenital hemangioma (0.494); uveal melanoma (0.469)
- **Europe PMC papers**: 4418
- **Why important**: GNA11 is the second member of the G-protein pair represented in both hu.MAP complexes (hu.MAP huMAP3_13105.1) and (hu.MAP huMAP3_11173.1), and it is present in every primary enrichment term (GO:MF GTPase activity; q_global = 0.000519) through (GO:MF hydrolase activity, acting on acid anhydrides, in phosphorus-containing anhydrides; q_global = 0.0134) and across the STRING functional annotations. Its established functions include receptor-mediated signal transduction and phospholipase-C-activating pathways. It is detected in ovary by HPA and has strong disease associations involving calcium homeostasis, hypocalcemia, hypercalcemia, hypoparathyroidism, and congenital hemangioma, alongside a large literature base.
- **Conclusion**: Established evidence supports GNA11 as a receptor-proximal signaling component that may help explain conservation of the module across tissues with distinct functions. Its ovarian detection and disease links make it biologically important, but the module does not establish whether GNA11 activity, abundance, or cell-type composition drives the cross-tissue pattern.

#### OPA1

- **Related proteins** (co-abundance neighbors): ATP1A1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OPA1 mitochondrial dynamin like GTPase. The protein encoded by this gene is a nuclear-encoded mitochondrial protein with similarity to dynamin-related GTPases. The encoded protein localizes to the inner mitochondrial membrane and helps regulate mitochondrial stability and energy output. This protein also sequesters cytochrome c. Mutations in this gene have been associated with optic atrophy type 1, which is a dominantly inherited optic …
- **Diseases (Open Targets)**: autosomal dominant optic atrophy, classic form (0.846); Behr syndrome (0.812); optic atrophy with or without deafness, ophthalmoplegia, myopathy, ataxia, and neuropathy (0.766); mitochondrial DNA depletion syndrome 14B (cardioencephalomyopathic type) (0.745); optic atrophy (0.653)
- **Europe PMC papers**: 12169
- **Why important**: OPA1 is included in every primary GTPase and nucleotide-hydrolysis term (GO:MF GTPase activity; q_global = 0.000519) through (GO:MF hydrolase activity, acting on acid anhydrides, in phosphorus-containing anhydrides; q_global = 0.0134) and in the major supplementary STRING terms. It occupies a membrane- and mitochondrion-associated position adjacent to ATP1A1 in the module. Its established role in inner-mitochondrial-membrane organization, mitochondrial fusion, stability, and energy output gives the module a direct mitochondrial dimension. OPA1 has very extensive literature and strong disease associations with dominant optic atrophy, Behr syndrome, mitochondrial DNA depletion, and related optic-neuromuscular disorders. HPA detects OPA1 protein in ovary.
- **Conclusion**: Established evidence identifies OPA1 as the strongest mitochondrial component among the important genes. Its co-abundance with GTPase and membrane-signaling genes supports a hypothesis of coordinated energetic and signaling adaptation, but the enrichment analysis alone cannot establish a causal mitochondrial role in the shared tissue module.

#### ATL3

- **Related proteins** (co-abundance neighbors): RHOG (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: atlastin GTPase 3. This gene encodes a member of a family of dynamin-like, integral membrane GTPases. The encoded protein is required for the proper formation of the network of interconnected tubules of the endoplasmic reticulum. Mutations in this gene may be associated with hereditary sensory neuropathy type IF. Alternatively spliced transcript variants that encode distinct isoforms have been described. [provided b…
- **Diseases (Open Targets)**: neuropathy, hereditary sensory, type 1F (0.718); hereditary sensory and autonomic neuropathy type 1 (0.617); hereditary disease (0.193); Familial prostate cancer (0.112); prostate cancer (0.112)
- **Europe PMC papers**: 672
- **Why important**: ATL3 is a high-confidence functional member of all primary enrichment terms (GO:MF GTPase activity; q_global = 0.000519) through (GO:MF hydrolase activity, acting on acid anhydrides, in phosphorus-containing anhydrides; q_global = 0.0134) and is connected to RHOG in the module. Its established dynamin-like GTPase activity and role in ER membrane fusion and formation of the interconnected ER network provide a mechanistic link between GTPase biology and organelle architecture. ATL3 is associated with hereditary sensory neuropathy and hereditary sensory-autonomic neuropathy, making it especially relevant to the autonomic-nervous-system side of the tissue pair. Its literature volume is meaningful, though smaller than that of OPA1 or GNA11.
- **Conclusion**: Established evidence supports ATL3 as an ER-structural GTPase and a particularly relevant autonomic-neural candidate. Its network relationship with RHOG makes an ER-to-cytoskeleton coordination model plausible, but direct cooperation between these genes in ovary or autonomic nervous system remains hypothetical.

#### ATP1A1

- **Related proteins** (co-abundance neighbors): OPA1 (0.82), GNAI3 (0.81), PITRM1 (0.81), RHOG (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 is one of the more connected module members and links OPA1, GNAI3, PITRM1, and RHOG. It contributes to the broad nucleotide-hydrolysis and acid-anhydride terms (GO:MF ribonucleoside triphosphate phosphatase activity; q_global = 0.00955) through (GO:MF hydrolase activity, acting on acid anhydrides, in phosphorus-containing anhydrides; q_global = 0.0134) and to the corresponding STRING annotations. Its established Na-plus/K-plus pump function maintains electrochemical gradients required for transport, osmoregulation, and electrical excitability, providing a physiological bridge to autonomic tissues. It has substantial literature and disease associations including axonal Charcot-Marie-Tooth disease, hypomagnesemia with seizures and intellectual disability, heart failure, and atrial fibrillation.
- **Conclusion**: Established evidence supports ATP1A1 as an ion-homeostasis and excitability component that could connect signaling state to cellular energy and membrane physiology. Its module position supports a coordinating role, but the reported enrichment does not show whether ATP1A1 is functionally driving the shared pattern or simply co-varies with it.

## Module 4

**Tissue pair**: autonomic_nervous_system and ovary  
**Genes (15)**: ATXN2L, BYSL, CALU, CCDC6, CDC73, SPECC1L, DOHH, HSPH1, EIF4G1, NUP43, NUP62, PHAX, PSME3IP1, RCC1, SEC24A

### Function

No GO or KEGG term passed global correction, so the module should not be assigned a statistically established pathway from enrichment analysis. Its gene-level evidence instead points to a connected set of core cellular processes: endoplasmic-reticulum-to-Golgi cargo transport through SEC24A; nuclear-pore and nucleocytoplasmic transport through NUP62 and NUP43; RNA processing and export through PHAX and related factors; translation initiation through EIF4G1; protein folding and stress handling through CALU and HSPH1; and cell-cycle or chromosome-associated functions through RCC1 and CDC73. The co-abundance structure is therefore most consistent with a broadly used intracellular logistics and proteostasis program rather than a tissue-specific autonomic or ovarian pathway. This interpretation is provisional because the module has no globally significant globally significant GO/KEGG enrichment and STRING supplied no functional-enrichment result.

**Cell composition.** The module is not dominated by plasma or secreted proteins, and it is not blood-cell enriched: every member has low immune-cell specificity in HPA and no blood-cell enrichment is reported. Only CALU is annotated with an intracellular-and-membrane secretome location, while the remaining genes are non-secreted or lack a secretome annotation. Most genes have low tissue specificity, consistent with broadly expressed cellular machinery rather than a specialized tissue marker program. HPA does show cell-type-enhanced signals, particularly in reproductive-cell populations such as oocytes and spermatids, as well as several epithelial or stromal populations; these signals may reflect shared cellular composition or reproductive-tissue biology, but they do not establish a common autonomic-ovary mechanism. Protein detection is reported for many members in ovary, whereas no matching HPA tissue is available for autonomic nervous system, so the tissue-level protein comparison is limited.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known STRING relationship is the NUP62–NUP43 pair, supporting a genuine nuclear-pore connection rather than an entirely arbitrary co-abundance edge. hu.MAP independently places RCC1, NUP62, and NUP43 together in (hu.MAP huMAP3_12581.1), and RCC1 with NUP62 in (hu.MAP huMAP3_10000.1). These results support partial recovery of known nuclear-pore or nuclear-transport machinery. The other module edges are not represented by high-confidence STRING partners, and no other hu.MAP complex contains multiple module members according to the fact sheet. Thus, the network contains one well-supported nuclear-transport substructure embedded in a larger set of correlated genes whose direct physical relationships remain unestablished. STRING has no supplementary functional-enrichment result, so the interaction evidence should be interpreted as structural support, not pathway-level proof.

**STRING interactions (score >= 0.7)**: 1 of 105 gene pairs: NUP43–NUP62 (0.984)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12581.1 (RCC1, NUP62, NUP43; 3/58); huMAP3_10000.1 (RCC1, NUP62; 2/44)

### Novelty

The module-level observation may be new because this particular conserved co-abundance pattern across autonomic nervous system and ovary is not documented in the supplied evidence. However, the underlying biology is not wholly novel: SEC24A-mediated COPII transport, nucleoporins, RCC1-associated nuclear functions, translation initiation, RNA handling, ER calcium or folding functions, and stress chaperoning are established cellular themes. The known NUP62–NUP43 STRING relationship and the shared hu.MAP memberships further argue that at least part of the module recapitulates recognized molecular machinery. Conversely, the absence of STRING or hu.MAP support for most edges does not prove novelty; it may reflect incomplete interaction databases, indirect regulation, tissue-dependent associations, or co-regulation. The defensible conclusion is that the cross-tissue module configuration is potentially novel, while its component functions are largely established.

**Hypothesis.** Hypothesis: the shared module reflects coordinated maintenance of intracellular proteostasis and gene-expression logistics in a common cell population or cellular state present in both tissues. SEC24A could couple ER export and membrane-trafficking demand to CALU-dependent ER folding, while HSPH1 and EIF4G1 could support recovery of protein synthesis during proteotoxic or physiological stress. In parallel, NUP62 and NUP43, together with RCC1 and RNA-handling factors, could coordinate nucleocytoplasmic exchange, cell-cycle-associated nuclear organization, and selective RNA maturation. The reproductive-cell HPA signals raise the possibility that the pattern is influenced by germline or reproductive-cell representation, but this remains a hypothesis rather than an established tissue-specific mechanism. Testing would require cell-resolved expression, perturbation of the nuclear-pore and ER-transport components, and independent replication in autonomic and ovarian samples.

Web sources: https://en.wikipedia.org/wiki/Sec24a; https://www.genecards.org/card/SEC24A; https://pmc.ncbi.nlm.nih.gov/articles/PMC6962814/; https://pmc.ncbi.nlm.nih.gov/articles/PMC6299087/; https://journals.biologists.com/jcs/article/134/6/jcs249276/237867/SEC24A-facilitates-colocalization-and-Ca2-flux

### Important genes

#### SEC24A

- **Related proteins** (co-abundance neighbors): DOHH (0.92), NUP62 (0.91), PSME3IP1 (0.89), BYSL (0.87), CCDC6 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC24 homolog A, COPII component. The protein encoded by this gene belongs to a family of proteins that are homologous to yeast Sec24. This protein is a component of coat protein II (COPII)-coated vesicles that mediate protein transport from the endoplasmic reticulum. COPII acts in the cytoplasm to promote the transport of secretory, plasma membrane, and vacuolar proteins from the endoplasmic reticulum to the golgi complex. Altern…
- **Diseases (Open Targets)**: Graves disease (0.218); hyperlipoproteinemia type V (0.071); combined low LDL and fibrinogen (0.069); Hyperlipoproteinemia type 1 (0.062); apolipoprotein c-III deficiency (0.062)
- **Europe PMC papers**: 808
- **Why important**: SEC24A is the most connected node in the co-abundance subgraph and links several otherwise weakly connected portions of the module. Its established COPII function provides a mechanistic anchor for ER-to-Golgi cargo loading and secretory-pathway logistics. It has substantial literature support and reported disease associations, while the supplied web search also identifies studies connecting SEC24A with ER-stress-induced cell death, calcium handling, and cancer biology.
- **Conclusion**: Established evidence supports SEC24A as a central intracellular trafficking component and as the network hub of this module. It is reasonable to hypothesize that its abundance tracks cellular secretory or ER-stress demand, but the module does not establish that SEC24A drives the shared tissue association or any disease phenotype.

#### NUP62

- **Related proteins** (co-abundance neighbors): SEC24A (0.91), CDC73 (0.89); STRING partners: NUP43 (0.984)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_12581.1, huMAP3_10000.1
- **Function (MyGene.info)**: nucleoporin 62. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. The protein encoded by this gene is a member of the FG-repeat containing nucleoporins and is localized to the nuclear pore ce…
- **Diseases (Open Targets)**: infantile bilateral striatal necrosis (0.609); familial infantile bilateral striatal necrosis (0.590); HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.529)
- **Europe PMC papers**: 1582
- **Why important**: NUP62 is a nuclear-pore component with high network connectivity relative to most module members, a high-confidence STRING relationship with NUP43, and membership in both (hu.MAP huMAP3_12581.1) and (hu.MAP huMAP3_10000.1). Its annotated functions include nucleocytoplasmic transport, RNA export, nuclear import, and mitotic nuclear organization. It is also among the more literature-rich genes in the module and is detected in ovary by HPA.
- **Conclusion**: Established evidence strongly supports NUP62 as the clearest physical-complex anchor in the module. A role for altered nuclear transport or RNA trafficking in the shared co-abundance pattern is plausible, but whether NUP62 is functionally causal remains untested.

#### NUP43

- **Related proteins** (co-abundance neighbors): DOHH (0.86); STRING partners: NUP62 (0.984)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 43. Bidirectional transport of macromolecules between the cytoplasm and nucleus occurs through nuclear pore complexes (NPCs) embedded in the nuclear envelope. NPCs are composed of subcomplexes, and NUP43 is part of one such subcomplex, Nup107-160 (Loiodice et al., 2004 [PubMed 15146057]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); Histiocytosis (0.370); COVID-19 (0.370)
- **Europe PMC papers**: 494
- **Why important**: NUP43 is directly connected to NUP62 by the strongest reported STRING interaction and participates with NUP62 and RCC1 in (hu.MAP huMAP3_12581.1). Its established role in the Nup107–Nup160 subcomplex and nucleocytoplasmic transport gives the module a second, independent nuclear-pore marker. Its HPA profile includes ovary detection and a late-spermatid cell-type signal.
- **Conclusion**: Established evidence supports NUP43 as part of a real nuclear-pore substructure recovered by the module. The reproductive-cell signal is compatible with a cell-composition contribution, but it does not demonstrate a specialized ovarian or autonomic function.

#### RCC1

- **Related proteins** (co-abundance neighbors): HSPH1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_12581.1, huMAP3_10000.1
- **Function (MyGene.info)**: regulator of chromosome condensation 1. Enables several functions, including guanyl-nucleotide exchange factor activity; nucleosomal DNA binding activity; and protein heterodimerization activity. Involved in several processes, including G1/S transition of mitotic cell cycle; regulation of mitotic nuclear division; and spindle organization. Located in chromatin; cytoplasm; and nucleus. Part of protein-containing complex. [provided by All…
- **Diseases (Open Targets)**: injury (0.338); neurodegenerative disease (0.338); myasthenia gravis (0.329); neoplasm (0.104); cancer (0.091)
- **Europe PMC papers**: 3525
- **Why important**: RCC1 contributes a complementary nuclear dimension: it is associated with chromosome condensation, spindle organization, chromosome segregation, and mitotic nuclear reassembly. It is a member of both hu.MAP complexes identified in the module and connects to HSPH1 in the co-abundance graph. It also has substantial literature volume and a late-spermatid HPA enrichment.
- **Conclusion**: Established evidence supports RCC1 as a nuclear cell-cycle and chromosome-organization factor that reinforces the nuclear-transport interpretation. Its inclusion could reflect proliferative or germline-cell composition, but the available evidence does not distinguish that explanation from coordinated regulation within a shared cellular state.

#### EIF4G1

- **Related proteins** (co-abundance neighbors): PHAX (0.85), HSPH1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 supplies a translation-related component that is not redundant with the nucleoporin evidence. It is a core EIF4F scaffold for cap-dependent translation initiation, has a relatively connected position through PHAX and HSPH1, and has substantial literature and disease-association coverage. Its presence supports a broader interpretation involving RNA handling, translation, and stress-responsive protein production.
- **Conclusion**: Established evidence supports EIF4G1 as a translation-initiation scaffold and a plausible indicator of protein-production demand. Its connection to the nuclear and ER-related portions of the module is presently a co-abundance-based inference, not evidence of a demonstrated physical complex.

## Module 5

**Tissue pair**: autonomic_nervous_system and ovary  
**Genes (7)**: HNRNPH1, PSMC4, PSMC2, RAE1, CCT3, TP53BP1, SNRNP200

### Function

No GO or KEGG term passed global correction, so the module does not have a statistically confirmed pathway-level annotation from those analyses. Its gene content nevertheless points to a largely intracellular, nuclear–cytosolic maintenance program combining RNA metabolism, proteostasis, and genome-surveillance functions. SNRNP200 and HNRNPH1 support spliceosome assembly, pre-mRNA splicing, and RNA processing; RAE1 supports nuclear mRNA export and nucleocytoplasmic transport; TP53BP1 supports DNA-damage checkpoint signaling and double-strand break repair; and PSMC2 and PSMC4 support ATP-dependent proteasomal protein turnover. CCT3 adds ATP-dependent chaperone-mediated protein folding. The topology is sparse and crosses these functional areas rather than forming a single fully connected pathway, so the most defensible interpretation is a conserved cellular quality-control and macromolecule-handling module, not a narrowly defined tissue-specific process. The supplementary STRING signal (STRING SMART ATPases associated with a variety of cellular activities; within-query FDR = 0.0455) is consistent with an ATPase-related component involving PSMC2, PSMC4, and SNRNP200, but it is not global enrichment evidence.

**Cell composition.** The module is composed entirely of intracellular proteins, with no secreted genes and no indication that it is a plasma-protein module. HPA reports low immune-cell specificity for all module genes, so a blood-cell explanation is not supported by the supplied evidence. Most genes have low tissue specificity, which is compatible with broadly used cellular machinery rather than a specialized autonomic-nervous-system or ovarian product. Several genes show cell-type-enhanced patterns, including reproductive-cell, placental, microglial, and pituitary-cell annotations, but these are heterogeneous and do not define a single shared cell type. Protein detection is reported for most tested genes in ovary, whereas there is no matching HPA tissue for autonomic nervous system. Thus, the shared signal is more plausibly related to conserved intracellular machinery or shared cellular composition than to circulating proteins or blood contamination, although cell-composition effects cannot be excluded.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a high-confidence direct relationship between PSMC2 and PSMC4, while the other possible gene pairs do not meet the supplied interaction threshold. The supplementary STRING ATPase term (STRING SMART ATPases associated with a variety of cellular activities; within-query FDR = 0.0455) includes PSMC2, PSMC4, and SNRNP200, supporting a partial ATPase theme but not establishing a globally significant enrichment result. hu.MAP independently places PSMC2 and PSMC4 together in the proteasome-related complexes (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1). These complexes contain many additional proteasome subunits, so the module captures only a small proteasomal fragment rather than an entire complex. No hu.MAP or STRING relationship is supplied for the remaining module edges. Consequently, the proteasome connection is already known and biologically credible, whereas the broader co-abundance linkage among RNA-processing, DNA-repair, chaperone, and proteasome genes remains less directly supported by curated interaction resources.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: PSMC2–PSMC4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART ATPases associated with a variety of cellular activities (FDR = 0.0455, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05064.1 (PSMC2, PSMC4; 2/31); huMAP3_09656.1 (PSMC2, PSMC4; 2/64); huMAP3_13725.1 (PSMC2, PSMC4; 2/69)

### Novelty

The module should not be called a newly discovered molecular complex or pathway. The PSMC2–PSMC4 relationship and their shared proteasome-complex memberships are established by STRING and hu.MAP, respectively. At the same time, the particular cross-tissue co-abundance grouping is not reproduced by a listed STRING or hu.MAP interaction, which could make the module-level association interesting. However, absence from those resources does not prove novelty, because co-abundance relationships need not be physical interactions and database coverage is incomplete. The appropriate conclusion is that this may be a potentially novel tissue-pair co-abundance pattern built partly around known proteasome components, but the fact sheet does not establish that it is a new biological mechanism.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular stress-buffering program in which RNA processing and export, protein folding, proteasomal degradation, and DNA-damage surveillance are co-regulated to maintain proteome and transcriptome quality. In this model, SNRNP200, HNRNPH1, and RAE1 handle RNA maturation and transport; CCT3 supports folding of newly synthesized proteins; PSMC2 and PSMC4 provide proteasomal ATPase activity; and TP53BP1 coordinates responses to damaged DNA. The hypothesis is supported by the individual gene functions and the known PSMC2–PSMC4 proteasome connection, but the module’s sparse topology and lack of globally significant GO or KEGG enrichment mean that it requires independent replication, cell-composition analysis, and perturbation or time-resolved data.

### Important genes

#### SNRNP200

- **Related proteins** (co-abundance neighbors): TP53BP1 (0.83), CCT3 (0.82), RAE1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 has the strongest network position in the module and connects to TP53BP1, CCT3, and RAE1, thereby linking the RNA-processing side of the module to DNA-damage, protein-folding, and RNA-export signals. It is a core U5 snRNP component and an RNA-helicase-family protein involved in spliceosomal assembly and conformational change. It is also included in the supplementary STRING ATPase term (STRING SMART ATPases associated with a variety of cellular activities; within-query FDR = 0.0455). Its substantial literature base and associations with retinal and neurodegenerative disease make it a biologically informative anchor.
- **Conclusion**: Established: SNRNP200 is a spliceosome-associated RNA-processing factor with a central position in this sparse network and a supplementary ATPase annotation (STRING SMART ATPases associated with a variety of cellular activities; within-query FDR = 0.0455). Hypothesis: its centrality may help coordinate RNA quality control with broader cellular maintenance in the shared module, but the co-abundance data do not prove that it regulates the other genes.

#### PSMC2

- **Related proteins** (co-abundance neighbors): HNRNPH1 (0.86), CCT3 (0.83); STRING partners: PSMC4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is a proteasome regulatory ATPase and has a direct high-confidence STRING relationship with PSMC4. It occurs with PSMC4 in all listed hu.MAP complexes (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1), making it the clearest established complex-based component of the module. Its annotations include ubiquitin-dependent and proteasomal protein catabolism, and its disease associations include plasma-cell myeloma, mantle-cell lymphoma, neoplasm, HIV infectious disease, and amyloidosis. It also has a substantial literature base and is detected in ovary by HPA.
- **Conclusion**: Established: PSMC2 represents a proteasome regulatory ATPase and is supported by both STRING and hu.MAP evidence (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). Hypothesis: its co-abundance with RNA-processing and DNA-repair genes may indicate coordinated proteome-quality control rather than a physical interaction with every module member.

#### PSMC4

- **Related proteins** (co-abundance neighbors): TP53BP1 (0.81); STRING partners: PSMC2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 4. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.603); mantle cell lymphoma (0.542); neoplasm (0.519); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1065
- **Why important**: PSMC4 is the second proteasome regulatory ATPase and forms the module’s strongest known physical interaction with PSMC2. Its membership with PSMC2 across (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1) provides convergent complex evidence. Its annotations include proteasomal protein catabolism, oxidative-stress response, and cellular response to type I interferon. It has a substantial literature base, disease associations overlapping those of PSMC2, and HPA detection in ovary.
- **Conclusion**: Established: PSMC4 is a proteasome-associated ATPase supported by direct STRING evidence and multiple hu.MAP complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). Hypothesis: PSMC4 may mark a proteostasis component shared across the two tissues, but its presence does not establish a tissue-specific proteasomal mechanism.

#### TP53BP1

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.83), PSMC4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tumor protein p53 binding protein 1. This gene encodes a protein that functions in the DNA double-strand break repair pathway choice, promoting non-homologous end joining (NHEJ) pathways, and limiting homologous recombination. This protein plays multiple roles in the DNA damage response, including promoting checkpoint signaling following DNA damage, acting as a scaffold for recruitment of DNA damage response proteins to damaged chrom…
- **Diseases (Open Targets)**: neurodegenerative disease (0.367); microcephaly and chorioretinopathy 3 (0.353); alcohol drinking (0.269); urolithiasis (0.269); microcephaly and chorioretinopathy 1 (0.266)
- **Europe PMC papers**: 2200
- **Why important**: TP53BP1 connects the proteasome-linked side of the network to SNRNP200 and is the module’s clearest DNA-damage-response gene. It promotes non-homologous end joining, limits homologous-recombination pathway choice, and acts as a scaffold for damaged chromatin and checkpoint signaling. It has the largest literature base among the listed genes and disease associations including neurodegenerative disease and microcephaly with chorioretinopathy. HPA detects the protein in ovary.
- **Conclusion**: Established: TP53BP1 is a DNA double-strand-break response and repair factor with strong literature support. Hypothesis: its co-abundance with proteasome and RNA processing genes may reflect a general response to cellular stress or replication burden, but the module does not demonstrate direct physical or regulatory coupling.

#### RAE1

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribonucleic acid export 1. Mutations in the Schizosaccharomyces pombe Rae1 and Saccharomyces cerevisiae Gle2 genes have been shown to result in accumulation of poly(A)-containing mRNA in the nucleus, suggesting that the encoded proteins are involved in RNA export. The protein encoded by this gene is a homolog of yeast Rae1. It contains four WD40 motifs, and has been shown to localize to distinct foci in the nucleoplasm, to …
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); COVID-19 (0.370); Histiocytosis (0.370)
- **Europe PMC papers**: 1837
- **Why important**: RAE1 links SNRNP200 to the module’s RNA-export interpretation. It is involved in mRNA export, nucleocytoplasmic transport, transcription-dependent tethering at the nuclear periphery, and regulation of mitotic spindle organization. HPA reports tissue enhancement in testis and cell-type enhancement in early spermatids, late primary spermatocytes, and oocytes, making it especially relevant to the reproductive context of the ovary-containing tissue pair. Its literature includes RNA export, viral disease, and infectious-disease associations.
- **Conclusion**: Established: RAE1 is an RNA-export and nucleocytoplasmic-transport factor with reproductive-cell enrichment in HPA. Hypothesis: RAE1 may connect transcript export and cell-cycle organization to the broader quality-control program, but the single network edge and heterogeneous HPA pattern do not establish a shared reproductive-cell mechanism.
