# Conserved co-abundance modules: bone_marrow and kidney

## Module 0

**Tissue pair**: bone_marrow and kidney  
**Genes (46)**: YWHAH, PGD, ABCF1, CACYBP, DCTN1, DDX5, DDX6, EIF2AK2, EIF3L, FAM120A, FDPS, HSPH1, EIF4G1, IL18R1, IMPDH2, NAMPT, OLA1, PAPSS2, PCNA, PDLIM1, PFKP, PTBP1, GART, PAICS, ATIC, CTPS1, RSL1D1, RPL3, RPL6, RUVBL2, SEPTIN7, SF3A1, STAT1, STT3A, DARS1, SYNPO, RARS1, SARS1, TARS1, YARS1, CCT5, CCT3, CCT7, CCT8, VPS35, XRCC6

### Function

The strongest interpretation is a conserved core of cellular biosynthetic capacity, protein quality control, RNA handling, and genome maintenance. The primary GO evidence links the module to Cajal-body and telomerase-RNA localization, ATP and purine-ribonucleotide binding, the CCT chaperonin complex, ATP-dependent protein folding, purine and GMP biosynthesis, DNA biosynthetic regulation, telomere maintenance, RNA binding, and general biosynthesis (54 globally significant GO/KEGG terms, q_global 4.17e-05–0.049; see the table). The CCT3-CCT5-CCT7-CCT8 group provides a coherent chaperone-centered component, while ATIC, GART, IMPDH2, and PAICS form a coherent purine-biosynthesis component. Aminoacyl-tRNA synthetases, ribosomal proteins, translation-initiation factors, RNA helicases, nucleotide enzymes, and DNA-repair proteins indicate that the module is associated with high demand for translation, RNA processing, nucleotide production, and proliferation-linked cellular maintenance. The telomerase and Cajal-body annotations are biologically plausible but should not be interpreted as proof that the complete module directly controls telomerase; much of that signal is concentrated in the CCT subunits. The broad ATP-, nucleotide-, cytosol-, and biosynthesis-related terms support a general cellular maintenance program rather than a narrowly tissue-specific pathway.

**Cell composition.** This is not primarily a plasma or secreted-protein module: nearly all members are intracellular, and NAMPT is the only gene annotated as secreted to blood. The HPA profile is dominated by low tissue specificity, with many proteins detected in both bone marrow and kidney, supporting a broadly expressed housekeeping-like component. There is nevertheless a possible sample-composition contribution from hematopoietic material. HPA supplementary evidence includes blood-associated and hematopoietic-system enrichment, with signals involving neutrophils, eosinophils, monocytes, B cells, megakaryocytes, and platelets, while most genes retain low immune-cell specificity. The module also contains cell-type-enhanced genes in reproductive, epithelial, vascular, muscle, and other cell types. Therefore, the shared bone-marrow-kidney pattern is more consistent with ubiquitous cellular machinery, potentially strengthened by shared proliferative or blood-derived cell populations, than with a kidney-specific or bone-marrow-specific secretory program.

**GO/KEGG enrichment**: 54 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA localization to Cajal body | 4.17e-05 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP telomerase RNA localization to Cajal body | 4.17e-05 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP telomerase RNA localization | 4.17e-05 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP RNA localization to nucleus | 4.17e-05 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:MF ATP binding | 5.02e-05 | ABCF1, CCT3, CCT5, CCT7, CCT8, CTPS1, DARS1, DDX5, DDX6, EIF2AK2, EIF4G1, GART, HSPH1, OLA1, PAICS, PAPSS2, PFKP, RARS1, RUVBL2, SARS1, TARS1, XRCC6, YARS1 |
| GO:MF adenyl nucleotide binding | 5.09e-05 | ABCF1, CCT3, CCT5, CCT7, CCT8, CTPS1, DARS1, DDX5, DDX6, EIF2AK2, EIF4G1, GART, HSPH1, OLA1, PAICS, PAPSS2, PFKP, PGD, RARS1, RUVBL2, SARS1, TARS1, XRCC6, YARS1 |
| GO:MF adenyl ribonucleotide binding | 5.16e-05 | ABCF1, CCT3, CCT5, CCT7, CCT8, CTPS1, DARS1, DDX5, DDX6, EIF2AK2, EIF4G1, GART, HSPH1, OLA1, PAICS, PAPSS2, PFKP, RARS1, RUVBL2, SARS1, TARS1, XRCC6, YARS1 |
| GO:MF purine nucleotide binding | 0.000225 | ABCF1, CCT3, CCT5, CCT7, CCT8, CTPS1, DARS1, DDX5, DDX6, EIF2AK2, EIF4G1, GART, HSPH1, OLA1, PAICS, PAPSS2, PFKP, PGD, RARS1, RUVBL2, SARS1, SEPTIN7, TARS1, XRCC6, YARS1 |
| GO:MF purine ribonucleoside triphosphate binding | 0.00024 | ABCF1, CCT3, CCT5, CCT7, CCT8, CTPS1, DARS1, DDX5, DDX6, EIF2AK2, EIF4G1, GART, HSPH1, OLA1, PAICS, PAPSS2, PFKP, RARS1, RUVBL2, SARS1, SEPTIN7, TARS1, XRCC6, YARS1 |
| GO:MF purine ribonucleotide binding | 0.000247 | ABCF1, CCT3, CCT5, CCT7, CCT8, CTPS1, DARS1, DDX5, DDX6, EIF2AK2, EIF4G1, GART, HSPH1, OLA1, PAICS, PAPSS2, PFKP, RARS1, RUVBL2, SARS1, SEPTIN7, TARS1, XRCC6, YARS1 |
| GO:MF nucleotide binding | 0.000272 | ABCF1, CCT3, CCT5, CCT7, CCT8, CTPS1, DARS1, DDX5, DDX6, EIF2AK2, EIF4G1, GART, HSPH1, IMPDH2, OLA1, PAICS, PAPSS2, PFKP, PGD, RARS1, RUVBL2, SARS1, SEPTIN7, TARS1, XRCC6, YARS1 |
| GO:CC chaperonin-containing T-complex | 0.000294 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 0.000294 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 0.000294 | CCT3, CCT5, CCT7, CCT8 |
| GO:MF ribonucleotide binding | 0.000294 | ABCF1, CCT3, CCT5, CCT7, CCT8, CTPS1, DARS1, DDX5, DDX6, EIF2AK2, EIF4G1, GART, HSPH1, OLA1, PAICS, PAPSS2, PFKP, RARS1, RUVBL2, SARS1, SEPTIN7, TARS1, XRCC6, YARS1 |

### STRING and hu.MAP

STRING supports several established molecular neighborhoods within the module. The CCT subunits have very strong mutual associations, and they connect to RUVBL2 and selected translation or ribosome-related proteins. ATIC, GART, IMPDH2, and PAICS form a recognized purine-biosynthesis neighborhood, with additional support from CTPS1. DARS1, RARS1, SARS1, TARS1, and YARS1 show the expected aminoacyl-tRNA-synthetase association pattern. EIF4G1 connects with EIF3L, DDX6, and VPS35, while PCNA connects with XRCC6, supporting translation-control and genome-maintenance substructures. The hu.MAP evidence independently supports the CCT complex (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), an aminoacyl-tRNA-synthetase complex containing DARS1, RARS1, and TARS1 (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), translation-initiation complexes containing EIF4G1 and EIF3L (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1), and a mixed metabolic or structural complex containing PDLIM1, ATIC, PGD, YARS1, and OLA1 (hu.MAP huMAP3_14442.1). These relationships show that the co-abundance module is not an arbitrary collection of genes: several of its internal edges correspond to established physical or functional assemblies. They also indicate that the module is composite, joining multiple related housekeeping systems rather than representing one single protein complex.

**STRING interactions (score >= 0.7)**: 49 of 1035 gene pairs: ABCF1–RPL6 (0.921); ATIC–CCT7 (0.881); ATIC–GART (0.999); ATIC–IMPDH2 (0.991); ATIC–PAICS (0.997); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT3–RUVBL2 (0.766); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT5–RPL3 (0.731); CCT5–RPL6 (0.708); CCT5–RUVBL2 (0.705); CCT5–TARS1 (0.727); CCT7–CCT8 (0.999); CCT7–IMPDH2 (0.758); CCT7–RPL3 (0.8); CCT7–RPL6 (0.793); CCT7–RUVBL2 (0.802); CCT8–RPL6 (0.78); CCT8–RUVBL2 (0.776); CTPS1–GART (0.734); CTPS1–IMPDH2 (0.927); CTPS1–RARS1 (0.739); DARS1–RARS1 (0.996); DARS1–YARS1 (0.859); DDX6–EIF4G1 (0.857); EIF2AK2–STAT1 (0.98); EIF3L–EIF4G1 (0.924); EIF3L–RPL6 (0.89); EIF4G1–VPS35 (0.899); GART–IMPDH2 (0.811); GART–PAICS (0.999); GART–RPL3 (0.805); IMPDH2–PAICS (0.744); OLA1–RARS1 (0.747); OLA1–YARS1 (0.824); PCNA–XRCC6 (0.819); RARS1–SARS1 (0.933); RARS1–TARS1 (0.806); RARS1–YARS1 (0.942); RPL3–RPL6 (0.999); RPL3–RSL1D1 (0.846); RPL6–RSL1D1 (0.919); RPL6–STT3A (0.8); SARS1–TARS1 (0.915); SARS1–YARS1 (0.941); TARS1–YARS1 (0.911)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Digestive gland (FDR = 9.2e-12, 40 genes); TISSUES Liver (FDR = 1.98e-11, 36 genes); TISSUES Lymphoblast (FDR = 1.27e-09, 15 genes); TISSUES Blood (FDR = 4.78e-09, 28 genes); TISSUES Lung (FDR = 3.77e-08, 24 genes); TISSUES Respiratory system (FDR = 4.68e-08, 26 genes); TISSUES Lymphocyte (FDR = 6.87e-08, 18 genes); TISSUES Gland (FDR = 3.4e-07, 45 genes); TISSUES Hematopoietic system (FDR = 5.27e-07, 30 genes); TISSUES Endocrine gland (FDR = 5.27e-07, 44 genes); TISSUES Testis (FDR = 1.64e-06, 25 genes); TISSUES Viscus (FDR = 3.41e-06, 40 genes); TISSUES Male reproductive system (FDR = 4.69e-06, 29 genes); TISSUES Female reproductive gland (FDR = 6.96e-06, 30 genes); TISSUES Male reproductive gland (FDR = 7.67e-06, 28 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (PDLIM1, ATIC, PGD, YARS1, OLA1; 5/57); huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_02637.1 (DARS1, TARS1, RARS1; 3/14); huMAP3_13688.1 (DARS1, TARS1, RARS1; 3/14); huMAP3_13175.1 (EIF4G1, EIF3L; 2/20); huMAP3_11246.1 (EIF4G1, EIF3L; 2/24)

### Novelty

The module should not be described as a wholly new molecular pathway. Its principal components and many internal relationships are already represented in STRING and hu.MAP, especially the CCT chaperonin, purine-biosynthesis, aminoacyl-tRNA-synthetase, and translation-initiation neighborhoods. What may be novel is the conserved co-abundance organization of these established systems across bone marrow and kidney, including their particular coupling to Cajal-body and telomere-related annotations. However, the fact sheet does not compare this module with prior tissue-pair co-abundance studies, so a claim of a new finding cannot be established from database absence or presence alone. The most defensible conclusion is that this is a potentially informative cross-tissue regulatory or abundance module assembled from largely known biology, with novelty residing in its tissue-pair co-abundance context rather than in the individual gene functions.

**Hypothesis.** Hypothesis: the shared module reflects a demand-coupled cellular maintenance state in which proliferative or metabolically active cells coordinate nucleotide production, aminoacyl-tRNA charging, translation, chaperone-mediated folding, RNA processing, and DNA or telomere maintenance. In this model, the CCT chaperonin supports folding of newly synthesized proteins; purine and pyrimidine metabolism supplies nucleotides for RNA and DNA synthesis; aminoacyl-tRNA synthetases and translation factors sustain protein production; and RUVBL2, PCNA, XRCC6, and the CCT-associated telomere annotations link this state to genome integrity and telomere maintenance. The shared signal could arise from common proliferative or hematopoietic cell populations in the two tissues, from a conserved response to cellular stress, or from both. This is a mechanistic hypothesis rather than a demonstrated causal pathway and should be tested with cell-resolved expression, protein abundance, perturbation, and telomere or replication readouts.

### Important genes

#### CCT7

- **Related proteins** (co-abundance neighbors): CCT8 (0.94), IMPDH2 (0.89), CCT3 (0.89), CTPS1 (0.87), TARS1 (0.87), CCT5 (0.87), HSPH1 (0.85), RUVBL2 (0.85), YARS1 (0.85), SEPTIN7 (0.84), PTBP1 (0.82), DARS1 (0.82), SARS1 (0.81), EIF4G1 (0.81); STRING partners: ATIC (0.881), CCT3 (0.999), CCT5 (0.999), CCT8 (0.999), IMPDH2 (0.758), RPL3 (0.8), RPL6 (0.793), RUVBL2 (0.802)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is a central network member and one of the strongest bridges in the module. It is part of the CCT chaperonin complex, has strong STRING connections to the other CCT subunits, and is present in the hu.MAP CCT complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). It contributes to the globally supported protein-folding, Cajal-body, telomerase-RNA-localization, and telomere-maintenance terms (4 globally significant GO/KEGG terms, q_global 4.17e-05–4.17e-05; see the table), (GO:CC chaperonin-containing T-complex; q_global = 0.000294) (GO:BP regulation of telomerase RNA localization to Cajal body; q_global = 0.000294) (GO:BP positive regulation of telomerase RNA localization to Cajal body; q_global = 0.000294), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.00267), (GO:CC protein folding chaperone complex; q_global = 0.00697), (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 0.00827), (GO:BP positive regulation of telomere maintenance via telomere lengthening; q_global = 0.0131), (7 globally significant GO/KEGG terms, q_global 0.0198–0.0457; see the table), (GO:BP regulation of telomere maintenance via telomere lengthening; q_global = 0.049). Its broad tissue profile and substantial literature make it a strong representative of the module’s core chaperone biology.
- **Conclusion**: Established evidence supports CCT7 as a structural and functional component of the CCT folding machinery and as a major network hub. Its co-abundance with nucleotide, translation, and genome-maintenance genes suggests that it may mark coordinated proteostasis in active cells. A direct causal role for CCT7 in the complete cross-tissue module or in telomere regulation remains a hypothesis.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): CTPS1 (0.89), DARS1 (0.86), CCT7 (0.85), DDX5 (0.85), RARS1 (0.84), YARS1 (0.84), RPL3 (0.83), PCNA (0.83), DDX6 (0.83), PAICS (0.82), GART (0.82), CCT8 (0.81), TARS1 (0.81), HSPH1 (0.81); STRING partners: CCT3 (0.766), CCT5 (0.705), CCT7 (0.802), CCT8 (0.776)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 has strong network connectivity and links the CCT-centered neighborhood to RNA, ribosome, nucleotide, replication, and DNA-repair genes. Its annotations include ATPase and DNA-helicase activity, DNA repair, DNA recombination, telomere maintenance, and regulation of DNA replication. It is included in globally supported RNA-localization, chaperone-complex, telomere, biosynthesis, and nucleotide-binding terms (4 globally significant GO/KEGG terms, q_global 4.17e-05–4.17e-05; see the table), (GO:CC chaperonin-containing T-complex; q_global = 0.000294), (4 globally significant GO/KEGG terms, q_global 0.000294–0.000358; see the table), (GO:CC cytosol; q_global = 0.00147), (GO:CC protein folding chaperone complex; q_global = 0.00697), (GO:BP biosynthetic process; q_global = 0.0174), (GO:BP telomere maintenance; q_global = 0.0198) (GO:BP telomere organization; q_global = 0.022), (GO:BP positive regulation of telomere maintenance; q_global = 0.0457). Its substantial literature and disease associations involving developmental, reproductive, and neoplastic biology further support its importance.
- **Conclusion**: Established evidence supports RUVBL2 as a multifunctional ATPase and DNA or RNA-associated factor that connects several module processes. It is a plausible integrator of proteostasis, RNA localization, replication, repair, and telomere-related biology. Whether RUVBL2 is the causal bridge between these processes in bone marrow and kidney is not established by co-abundance alone.

#### CTPS1

- **Related proteins** (co-abundance neighbors): RUVBL2 (0.89), TARS1 (0.88), RPL3 (0.88), CCT7 (0.87), SF3A1 (0.85), CCT8 (0.85), EIF4G1 (0.85), CCT5 (0.85), RARS1 (0.84), ABCF1 (0.84), IMPDH2 (0.83), HSPH1 (0.82); STRING partners: GART (0.734), IMPDH2 (0.927), RARS1 (0.739)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CTP synthase 1. This gene encodes an enzyme responsible for the catalytic conversion of UTP (uridine triphosphate) to CTP (cytidine triphospate). This reaction is an important step in the biosynthesis of phospholipids and nucleic acids. Activity of this proten is important in the immune system, and loss of function of this gene has been associated with immunodeficiency. Alternative splicing results in multiple tr…
- **Diseases (Open Targets)**: combined immunodeficiency due to CTPS1 deficiency (0.712); androgenetic alopecia (0.204); hyperpituitarism (0.195); urolithiasis (0.097); alcohol drinking (0.097)
- **Europe PMC papers**: 641
- **Why important**: CTPS1 occupies a central position among the module’s metabolic and translation-associated genes and connects to RUVBL2, TARS1, ribosomal proteins, CCT subunits, SF3A1, and EIF4G1. It catalyzes CTP production for nucleic-acid and phospholipid biosynthesis, and the fact sheet specifically links its loss of function to immunodeficiency. It is included in the globally supported nucleotide-binding and biosynthetic terms (7 globally significant GO/KEGG terms, q_global 5.02e-05–0.000272; see the table), (GO:MF ribonucleotide binding; q_global = 0.000294), (GO:MF nucleoside phosphate binding; q_global = 0.000348), (GO:MF heterocyclic compound binding; q_global = 0.000944), (GO:MF carbohydrate derivative binding; q_global = 0.00106) (GO:CC cytosol; q_global = 0.00147), (GO:MF anion binding; q_global = 0.0134) (GO:BP biosynthetic process; q_global = 0.0174). Its literature volume is substantial, and its immune disease association makes it especially relevant to a module shared with bone marrow.
- **Conclusion**: Established evidence supports CTPS1 as a nucleotide-biosynthetic enzyme with particular importance for immune-cell function. Its position suggests that nucleotide supply may couple the module’s metabolic and protein-production components. A specific contribution of CTPS1 to the kidney-bone-marrow conservation pattern remains a hypothesis.

#### IMPDH2

- **Related proteins** (co-abundance neighbors): CCT7 (0.89), CCT8 (0.87), CCT3 (0.85), CCT5 (0.83), TARS1 (0.83), CTPS1 (0.83), SEPTIN7 (0.80), DDX5 (0.80); STRING partners: ATIC (0.991), CCT7 (0.758), CTPS1 (0.927), GART (0.811), PAICS (0.744)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inosine monophosphate dehydrogenase 2. This gene encodes the rate-limiting enzyme in the de novo guanine nucleotide biosynthesis. It is thus involved in maintaining cellular guanine deoxy- and ribonucleotide pools needed for DNA and RNA synthesis. The encoded protein catalyzes the NAD-dependent oxidation of inosine-5'-monophosphate into xanthine-5'-monophosphate, which is then converted into guanosine-5'-monophosphate. This gene is up-…
- **Diseases (Open Targets)**: acute lymphoblastic leukemia (0.529); Crohn disease (0.447); acute myeloid leukemia (0.421); lupus nephritis (0.408); myelodysplastic syndrome (0.403)
- **Europe PMC papers**: 1438
- **Why important**: IMPDH2 is a network connector between the CCT proteins, CTPS1, TARS1, SEPTIN7, and the purine-biosynthesis enzymes. It catalyzes a rate-limiting step in guanine-nucleotide production and is directly represented in the globally supported XMP and GMP biosynthetic terms (GO:BP XMP metabolic process; q_global = 0.00479) (GO:BP XMP biosynthetic process; q_global = 0.00479) (GO:BP 'de novo' XMP biosynthetic process; q_global = 0.00479), (GO:BP GMP biosynthetic process; q_global = 0.0372). It also contributes to the broader nucleotide, cytosolic, extracellular-vesicle, and biosynthetic annotations (GO:MF nucleotide binding; q_global = 0.000272), (8 globally significant GO/KEGG terms, q_global 0.00032–0.000944; see the table), (GO:CC cytosol; q_global = 0.00147), (GO:BP biosynthetic process; q_global = 0.0174). Its disease associations include hematologic malignancies and lupus nephritis, making it relevant to both hematopoietic and kidney-related biology, while its literature base is substantial.
- **Conclusion**: Established evidence supports IMPDH2 as a key guanine-nucleotide supply enzyme and a plausible metabolic anchor of the module. Its connections to CCT and translation-related genes are consistent with coordinated support of biosynthesis in active cells. The module does not establish that IMPDH2 drives the observed co-abundance pattern or disease associations.

#### PCNA

- **Related proteins** (co-abundance neighbors): GART (0.83), RUVBL2 (0.83), YARS1 (0.80); STRING partners: XRCC6 (0.819)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proliferating cell nuclear antigen. The protein encoded by this gene is found in the nucleus and is a cofactor of DNA polymerase delta. The encoded protein acts as a homotrimer and helps increase the processivity of leading strand synthesis during DNA replication. In response to DNA damage, this protein is ubiquitinated and is involved in the RAD6-dependent DNA repair pathway. Two transcript variants encoding the same protein have b…
- **Diseases (Open Targets)**: ataxia-telangiectasia-like disorder (0.497); neurodegenerative disease (0.188); neoplasm (0.118); diabetes mellitus (0.116); hepatocellular carcinoma (0.113)
- **Europe PMC papers**: 61820
- **Why important**: PCNA provides a direct link to DNA replication, repair, and cell proliferation. It connects in the module to GART, RUVBL2, and YARS1, and STRING supports its relationship with XRCC6. It contributes to the globally supported regulation of DNA biosynthesis, telomere maintenance, telomere organization, and biosynthetic-process terms (7 globally significant GO/KEGG terms, q_global 0.00032–0.000584; see the table), (GO:CC cytosol; q_global = 0.00147), (GO:BP positive regulation of DNA biosynthetic process; q_global = 0.00518), (GO:BP biosynthetic process; q_global = 0.0174), (4 globally significant GO/KEGG terms, q_global 0.0198–0.0272; see the table). HPA identifies it as tissue-enhanced in bone marrow and cell-type-enhanced in proliferative or progenitor-associated populations. Its disease and cancer literature is extensive, making it a strong marker of the proliferative and genome-maintenance dimension of the module.
- **Conclusion**: Established evidence supports PCNA as a replication and DNA-repair factor and as a plausible indicator of proliferative cellular content. Its presence strengthens the interpretation that the module includes genome-maintenance demands in addition to housekeeping metabolism. It does not by itself prove that the entire module represents proliferation.

#### STAT1

- **Related proteins** (co-abundance neighbors): PFKP (0.87), YARS1 (0.81), XRCC6 (0.80); STRING partners: EIF2AK2 (0.98)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal transducer and activator of transcription 1. The protein encoded by this gene is a member of the STAT protein family. In response to cytokines and growth factors, STAT family members are phosphorylated by the receptor associated kinases, and then form homo- or heterodimers that translocate to the cell nucleus where they act as transcription activators. The protein encoded by this gene can be activated by various ligands including interferon-…
- **Diseases (Open Targets)**: immunodeficiency 31B (0.786); chronic mucocutaneous candidiasis (0.775); autoimmune enteropathy and endocrinopathy - susceptibility to chronic infections syndrome (0.772); cancer (0.554); immunodeficiency disease (0.482)
- **Europe PMC papers**: 66602
- **Why important**: STAT1 is less connected than the main metabolic and chaperone hubs but is biologically important because it links the module to cytokine and interferon-responsive signaling. It connects to PFKP, YARS1, and XRCC6 within the module and to EIF2AK2 in STRING. Its annotations include defense responses to viruses, cytokine-responsive transcription, and regulation of cell proliferation, while the module also contains immune-associated HPA signals and STRING blood or hematopoietic tissue enrichment (STRING TISSUES Blood; within-query FDR = 4.78e-09), (STRING TISSUES Hematopoietic system; within-query FDR = 5.27e-07). STAT1 has an exceptionally extensive literature and established associations with immunodeficiency and inflammatory disease.
- **Conclusion**: Established evidence supports STAT1 as an immune and cytokine-responsive transcription factor that may explain part of the module’s hematopoietic or stress-related context. Its relatively peripheral network position argues against treating it as the module’s central organizer. A plausible hypothesis is that immune signaling modulates the otherwise broadly expressed biosynthetic and proteostasis program, but this requires direct testing.

## Module 1

**Tissue pair**: bone_marrow and kidney  
**Genes (28)**: MPG, AFG2A, C2orf49, ATG9A, BRD8, CFAP298, DCAF13, DSN1, DUS3L, GON7, LUC7L2, MBD3, NAA20, NAA30, NUP43, PDCD2L, RAVER1, RCOR1, RIOX1, POLR1G, SGTB, TAF6, TFIP11, THOC3, TRIM24, FTSJ1, VIRMA, WDR74

### Function

The module most plausibly represents a broadly expressed nuclear and cytosolic gene-expression maintenance program, combining RNA processing, RNA modification, ribosome biogenesis, translation-related quality control, chromatin regulation, and protein homeostasis. This interpretation is supported by the functions of TRIM24, GON7, FTSJ1, WDR74, VIRMA, LUC7L2, THOC3, TFIP11, DCAF13, POLR1G, NAA20, NAA30, and related genes. The network also contains genes involved in autophagy, DNA repair, kinetochore function, nucleocytoplasmic transport, and ciliary biology, so it is not a narrowly defined pathway. No GO or KEGG term passed global correction; therefore, the functional interpretation is driven by convergent gene annotations and network structure rather than globally significant pathway enrichment. The relatively sparse co-abundance graph, with TRIM24 as the main connectivity hub, is consistent with a coordinated cellular maintenance program rather than a densely connected canonical complex.

**Cell composition.** The module is not composed of plasma proteins or secreted proteins: the HPA summary reports no secreted genes, and the individual proteins are predominantly nuclear, nucleolar, cytosolic, or vesicular. Most genes have low tissue specificity and low immune-cell specificity, arguing against a simple blood-cell or plasma-protein signature shared between bone marrow and kidney. HPA nevertheless shows cell-type-enhanced expression for most genes, with frequent associations to germ-cell states and additional associations to neural, epithelial, muscle, and selected immune-cell populations. A minority of genes are immune-cell enhanced or associated with bone marrow, but the overall pattern does not support a predominantly blood-cell module. The shared signal may therefore reflect broadly active cellular programs, with possible contributions from particular cell populations in each tissue. Protein detection is present for many genes in both tissues, although absence of detection for some genes and missing HPA data limit interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a small amount of direct high-confidence support within the module. The FTSJ1-WDR74 relationship connects RNA modification or ribosome-related biology, while the NAA20-NAA30 relationship supports a Nat acetyltransferase association. No STRING functional enrichment was reported, and no STRING enrichment should be treated as globally significant. hu.MAP provides additional complex-level context: VIRMA, THOC3, and LUC7L2 occur together in C1; VIRMA and LUC7L2 occur together in C3; NUP43 and GON7 occur together in C2; MPG and C2orf49 occur together in C4 and C5; and MBD3 and RCOR1 occur together in C6. These overlaps indicate that portions of the module intersect known RNA-processing, nuclear transport, translation-associated, and chromatin-regulatory complexes. However, each hu.MAP overlap contains only a subset of the respective complex, so the module should not be equated with any single complete complex. The combination of sparse STRING links and several partial hu.MAP overlaps suggests coordinated cellular machinery and shared regulation rather than one experimentally established physical assembly.

**STRING interactions (score >= 0.7)**: 2 of 378 gene pairs: FTSJ1–WDR74 (0.91); NAA20–NAA30 (0.954)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09943.1 (VIRMA, THOC3, LUC7L2; 3/78); huMAP3_11762.1 (NUP43, GON7; 2/10); huMAP3_10564.1 (VIRMA, LUC7L2; 2/37); huMAP3_14270.1 (MPG, C2orf49; 2/47); huMAP3_14559.1 (MPG, C2orf49; 2/47); huMAP3_15128.1 (MBD3, RCOR1; 2/96)

### Novelty

The module cannot be established as a wholly new biological pathway from the supplied evidence. Several relationships and functional groupings are already recognized through STRING and hu.MAP, including the FTSJ1-WDR74 and NAA20-NAA30 relationships and the partial complexes containing VIRMA, LUC7L2, THOC3, GON7, NUP43, MPG, C2orf49, MBD3, and RCOR1. At the same time, the particular bone-marrow–kidney co-abundance configuration, its sparse cross-functional topology, and the shared tissue context may represent a potentially novel systems-level observation. Lack of STRING or hu.MAP support for many module edges is not evidence of novelty, because co-abundance can reflect shared regulation, cell composition, or indirect biological coupling. The defensible conclusion is that the constituent biology is largely established, whereas the specific cross-tissue co-abundance module remains a hypothesis-generating finding requiring replication and comparison with published co-expression resources.

**Hypothesis.** Hypothesis: the module reflects a shared cellular stress or maintenance state in bone marrow and kidney in which nuclear gene expression, RNA maturation and modification, ribosome production, translation quality control, chromatin regulation, and selective protein or organelle homeostasis are coordinated. TRIM24, MBD3, and RCOR1 could provide regulatory links between chromatin state and transcriptional programs; VIRMA, LUC7L2, THOC3, and TFIP11 could coordinate RNA maturation and export; GON7, WDR74, FTSJ1, DCAF13, and POLR1G could support nucleolar or translational capacity; and ATG9A, SGTB, and AFG2A could connect this program to vesicle, autophagy, protein-targeting, or mitochondrial maintenance. This is a mechanistic hypothesis, not a demonstrated causal pathway. It should be tested by replication across independent samples, cell-composition adjustment, perturbation of hub genes, and measurement of RNA-processing, ribosome-biogenesis, chromatin, and autophagy phenotypes.

### Important genes

#### TRIM24

- **Related proteins** (co-abundance neighbors): THOC3 (0.85), WDR74 (0.85), NUP43 (0.85), MBD3 (0.84), RIOX1 (0.83), DUS3L (0.81), C2orf49 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tripartite motif containing 24. The protein encoded by this gene mediates transcriptional control by interaction with the activation function 2 (AF2) region of several nuclear receptors, including the estrogen, retinoic acid, and vitamin D3 receptors. The protein localizes to nuclear bodies and is thought to associate with chromatin and heterochromatin-associated factors. The protein is a member of the tripartite motif (TRIM) fa…
- **Diseases (Open Targets)**: cancer (0.609); neurodegenerative disease (0.540); leukemia (0.380); lung adenocarcinoma (0.374); acute lymphoblastic leukemia (0.372)
- **Europe PMC papers**: 2114
- **Why important**: TRIM24 is the principal network hub in the supplied graph, linking genes involved in transcriptional regulation, RNA and ribosome biology, nuclear transport, chromatin regulation, and DNA or RNA maintenance. Its established functions include nuclear-receptor-dependent transcriptional control, chromatin or heterochromatin association, protein ubiquitination, and regulation of transcription. It has substantial literature support and disease associations including cancer and leukemia. Its HPA profile is broadly expressed rather than secreted or strongly immune-cell specific, which fits a shared cellular maintenance program.
- **Conclusion**: Established evidence supports TRIM24 as a nuclear transcriptional and chromatin regulator with broad disease relevance and a central position in this module. The hypothesis that it coordinates the other module processes is plausible from its network position but is not demonstrated by the supplied data.

#### GON7

- **Related proteins** (co-abundance neighbors): ATG9A (0.87), MBD3 (0.87), TAF6 (0.85), CFAP298 (0.84), DCAF13 (0.83), TFIP11 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Nucleoli rim; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_11762.1
- **Function (MyGene.info)**: GON7 subunit of KEOPS complex. Located in cytosol; nucleolus; and nucleoplasm. Part of EKC/KEOPS complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Galloway-Mowat syndrome 9 (0.572); Galloway-Mowat syndrome (0.504); eye injury (0.053); systemic inflammatory response syndrome (0.037); corneal degeneration (0.031)
- **Europe PMC papers**: 134
- **Why important**: GON7 has a relatively central network position and connects ATG9A, MBD3, TAF6, CFAP298, DCAF13, and TFIP11. It is a subunit of the KEOPS complex and is annotated for tRNA threonylcarbamoyladenosine modification and maintenance of translational fidelity. It is also part of hu.MAP complex C2 with NUP43, providing complex-level support for a nuclear or translation-related context. Its disease associations include Galloway-Mowat syndrome, and its HPA profile includes bone marrow and kidney protein detection.
- **Conclusion**: Established evidence supports GON7 as a KEOPS-associated factor involved in tRNA modification and translational fidelity. Its position may make it a useful bridge between RNA quality control, nuclear biology, and cellular maintenance in this module, but a causal role in the bone-marrow–kidney co-abundance pattern remains hypothetical.

#### FTSJ1

- **Related proteins** (co-abundance neighbors): ATG9A (0.86), RAVER1 (0.84), MPG (0.83), LUC7L2 (0.83); STRING partners: WDR74 (0.91)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FtsJ RNA 2'-O-methyltransferase 1. This gene encodes a member of the methyltransferase superfamily. The encoded protein localizes to the nucleolus, binds to S-adenosylmethionine, and may be involved in the processing and modification of ribosomal RNA. Mutations in this gene are associated with cognitive disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013].
- **Diseases (Open Targets)**: non-syndromic X-linked intellectual disability (0.712); hereditary disease (0.499); Intellectual disability (0.393); X-linked complex neurodevelopmental disorder (0.370); autism spectrum disorder (0.118)
- **Europe PMC papers**: 365
- **Why important**: FTSJ1 links ATG9A, RAVER1, MPG, and LUC7L2 in the module and has a high-confidence STRING relationship with WDR74. It is an RNA methyltransferase involved in tRNA modification, tRNA processing, and cytoplasmic translation, with additional annotation for ribosomal RNA processing. It has established associations with intellectual disability and a substantial literature base. HPA detects the protein in kidney, while its cell-type-enhanced pattern includes spermatogenic states.
- **Conclusion**: Established evidence supports FTSJ1 as an RNA-modification and translation-related enzyme, and the STRING link to WDR74 reinforces a connection to RNA or ribosome biology. Its module-level connection to splicing and autophagy genes suggests coordinated cellular maintenance, but that broader integration is a hypothesis.

#### VIRMA

- **Related proteins** (co-abundance neighbors): NAA30 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_09943.1, huMAP3_10564.1
- **Function (MyGene.info)**: vir like m6A methyltransferase associated. Enables RNA binding activity. Involved in mRNA alternative polyadenylation and mRNA methylation. Located in cytosol and nuclear speck. Colocalizes with RNA N6-methyladenosine methyltransferase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: smoking initiation (0.355); Abnormality of the skeletal system (0.355); obesity disorder (0.344); orofacial cleft (0.256); cleft palate (0.221)
- **Europe PMC papers**: 1994
- **Why important**: VIRMA is a member of two hu.MAP complexes represented in the module, C1 and C3, with THOC3 and LUC7L2 in one complex context and LUC7L2 in another. It is a component of the RNA N-six-methyladenosine methyltransferase system and is involved in mRNA processing, alternative polyadenylation, and mRNA methylation. It has extensive literature support and disease or trait associations including skeletal abnormalities, obesity-related disease, and orofacial development. HPA detects the protein in both bone marrow and kidney.
- **Conclusion**: Established evidence supports VIRMA as an RNA-processing and mRNA-methylation regulator embedded in known RNA-associated complexes. Its co-abundance with splicing and transcription-export genes is biologically coherent, but the data do not establish that VIRMA drives the shared tissue module.

#### RCOR1

- **Related proteins** (co-abundance neighbors): BRD8 (0.95), WDR74 (0.93), AFG2A (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_15128.1
- **Function (MyGene.info)**: REST corepressor 1. This gene encodes a protein that is well-conserved, downregulated at birth, and with a specific role in determining neural cell differentiation. The encoded protein binds to the C-terminal domain of REST (repressor element-1 silencing transcription factor). [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: secondary malignant neoplasm (0.269); adrenal gland hyperfunction (0.265); hyperaldosteronism (0.265); venous thromboembolism (0.259); Joubert syndrome (0.259)
- **Europe PMC papers**: 952
- **Why important**: RCOR1 connects BRD8, WDR74, and AFG2A and is represented with MBD3 in hu.MAP complex C6. It is a REST corepressor involved in transcriptional repression, erythrocyte differentiation, and positive regulation of megakaryocyte differentiation. These hematopoietic annotations are especially relevant to the bone-marrow component, while HPA detects the protein in both bone marrow and kidney. It has substantial literature support and reported disease associations including malignancy, thromboembolism, and developmental syndromes.
- **Conclusion**: Established evidence supports RCOR1 as a chromatin-associated transcriptional coregulator with direct relevance to hematopoietic differentiation. Its presence may help explain the bone-marrow connection, but the shared kidney association and its integration with RNA or ribosome-related genes remain hypotheses rather than demonstrated mechanisms.

## Module 2

**Tissue pair**: bone_marrow and kidney  
**Genes (34)**: NUDT1, ZNHIT6, BRIX1, CPSF3, CRTC2, LIG1, DNMT1, ECD, EP300, SIRAL1, GTPBP4, HAUS6, HDAC3, HMG20A, IGF2BP3, MCM4, MCM7, MTA3, NVL, PAXBP1, PDCD4, PSME4, RBM7, MRPL19, RNF25, POLR3D, RSRC1, SMC2, SRCAP, QTRT1, TRMT61A, UNC119B, USP13, XPO5

### Function

The strongest interpretation is a conserved nuclear gene-expression and genome-maintenance module. The primary evidence is broad and coherent: nucleic-acid metabolism (GO:BP nucleic acid metabolic process; q_global = 4.68e-05), nucleobase-containing compound metabolism (GO:BP nucleobase-containing compound metabolic process; q_global = 0.00177), nuclear localization (GO:CC nucleus; q_global = 0.00267), RNA metabolism (GO:BP RNA metabolic process; q_global = 0.00658), nucleic-acid biosynthesis (GO:BP nucleic acid biosynthetic process; q_global = 0.00996), and RNA biosynthesis (GO:BP RNA biosynthetic process; q_global = 0.0204) all pass global correction. The additional macromolecule-metabolism term (GO:BP macromolecule metabolic process; q_global = 0.0457) supports a general biosynthetic and information-processing role. The gene set combines DNA replication and repair, RNA processing and export, ribosome and RNA maturation, chromatin remodeling, transcriptional regulation, and regulated protein turnover. Thus, this is not best described as a single narrow pathway; it is a coordinated nuclear program associated with proliferating or transcriptionally active cells.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and many are nuclear or nucleolar housekeeping-type factors. There is nevertheless a strong cell-state signal. HPA annotations repeatedly point to erythrocyte progenitors, megakaryocyte progenitors, monocyte progenitors, lymphoid tissue, and bone marrow, while many genes are cell-type enhanced rather than immune-cell specific. This pattern is compatible with shared proliferative or progenitor-cell content in bone marrow and kidney samples, and possibly with blood or marrow-derived cells, but the low immune-cell specificity argues against interpreting the module as a simple mature immune-cell signature. The protein-detection pattern in both tissues supports biological presence, although detection is not evidence that every gene acts in one physical complex.

**GO/KEGG enrichment**: 7 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP nucleic acid metabolic process | 4.68e-05 | BRIX1, CPSF3, CRTC2, DNMT1, ECD, EP300, GTPBP4, HDAC3, HMG20A, IGF2BP3, LIG1, MCM4, MCM7, MTA3, NUDT1, NVL, PAXBP1, PDCD4, POLR3D, PSME4, QTRT1, RBM7, RSRC1, SRCAP, TRMT61A, USP13, XPO5, ZNHIT6 |
| GO:BP nucleobase-containing compound metabolic process | 0.00177 | BRIX1, CPSF3, CRTC2, DNMT1, ECD, EP300, GTPBP4, HDAC3, HMG20A, IGF2BP3, LIG1, MCM4, MCM7, MTA3, NUDT1, NVL, PAXBP1, PDCD4, POLR3D, PSME4, QTRT1, RBM7, RSRC1, SRCAP, TRMT61A, USP13, XPO5, ZNHIT6 |
| GO:CC nucleus | 0.00267 | BRIX1, CPSF3, CRTC2, DNMT1, ECD, EP300, GTPBP4, HDAC3, HMG20A, IGF2BP3, LIG1, MCM4, MCM7, MRPL19, MTA3, NUDT1, NVL, PAXBP1, PDCD4, POLR3D, PSME4, QTRT1, RBM7, RNF25, RSRC1, SIRAL1, SMC2, SRCAP, TRMT61A, USP13, XPO5, ZNHIT6 |
| GO:BP RNA metabolic process | 0.00658 | BRIX1, CPSF3, CRTC2, DNMT1, ECD, EP300, GTPBP4, HDAC3, HMG20A, IGF2BP3, MTA3, NVL, PAXBP1, PDCD4, POLR3D, QTRT1, RBM7, RSRC1, SRCAP, TRMT61A, USP13, XPO5, ZNHIT6 |
| GO:BP nucleic acid biosynthetic process | 0.00996 | BRIX1, CPSF3, CRTC2, DNMT1, ECD, EP300, GTPBP4, HDAC3, HMG20A, LIG1, MTA3, NVL, PAXBP1, PDCD4, POLR3D, QTRT1, RBM7, RSRC1, SRCAP, TRMT61A, USP13, ZNHIT6 |
| GO:BP RNA biosynthetic process | 0.0204 | BRIX1, CPSF3, CRTC2, DNMT1, ECD, EP300, GTPBP4, HDAC3, HMG20A, MTA3, NVL, PAXBP1, PDCD4, POLR3D, QTRT1, RBM7, RSRC1, SRCAP, TRMT61A, USP13, ZNHIT6 |
| GO:BP macromolecule metabolic process | 0.0457 | BRIX1, CPSF3, CRTC2, DNMT1, ECD, EP300, GTPBP4, HDAC3, HMG20A, IGF2BP3, LIG1, MCM4, MCM7, MRPL19, MTA3, NUDT1, NVL, PAXBP1, PDCD4, POLR3D, PSME4, QTRT1, RBM7, RNF25, RSRC1, SRCAP, TRMT61A, USP13, XPO5, ZNHIT6 |

### STRING and hu.MAP

STRING supports several established relationships within the module. The MCM4–MCM7 pair is strongly supported, with links from both proteins to LIG1 and SMC2. The chromatin-regulatory group is supported by EP300 links to HDAC3, CRTC2, and SRCAP. The nucleolar/ribosome-related group is supported by BRIX1–GTPBP4 and GTPBP4–NVL, while PAXBP1–RSRC1 supports an RNA-processing connection. STRING functional terms independently reinforce nuclear location, nucleic-acid metabolism, macromolecule metabolism, and ubiquitin-related regulation (5 supplementary STRING terms; within-query FDR 0.0011–0.0196). These STRING results are supplementary and do not replace the globally corrected GO evidence. hu.MAP provides especially strong contextual support for MCM4 and MCM7 recurring in replication-associated complexes (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_07113.1) and (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1). ECD, RSRC1, and PAXBP1 recur in spliceosomal or RNA-processing complexes (hu.MAP huMAP3_08980.1), (hu.MAP huMAP3_00424.1), and (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_09945.1). The partial membership of the module in these complexes suggests that the co-abundance module combines several related nuclear machines rather than representing one complete complex.

**STRING interactions (score >= 0.7)**: 11 of 561 gene pairs: BRIX1–GTPBP4 (0.998); CRTC2–EP300 (0.961); EP300–HDAC3 (0.958); EP300–SRCAP (0.911); GTPBP4–NVL (0.769); LIG1–MCM4 (0.843); LIG1–MCM7 (0.855); MCM4–MCM7 (0.999); MCM4–SMC2 (0.748); MCM7–SMC2 (0.7); PAXBP1–RSRC1 (0.844)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Nucleus (FDR = 0.0011, 26 genes); Component Nucleus (FDR = 0.0017, 31 genes); Keyword Ubl conjugation (FDR = 0.011, 17 genes); Process Macromolecule metabolic process (FDR = 0.0145, 28 genes); Process Nucleic acid metabolic process (FDR = 0.0196, 20 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (ECD, RSRC1, PAXBP1; 3/97); huMAP3_06061.1 (MCM4, MCM7; 2/5); huMAP3_05529.1 (MCM4, MCM7; 2/6); huMAP3_07113.1 (MCM4, MCM7; 2/6); huMAP3_00424.1 (ECD, RSRC1; 2/8); huMAP3_11119.1 (MCM4, MCM7; 2/14); huMAP3_14758.1 (MCM4, MCM7; 2/14); huMAP3_08554.1 (MCM4, MCM7; 2/15); huMAP3_11832.1 (MCM4, MCM7; 2/15); huMAP3_12180.1 (MCM4, MCM7; 2/17); huMAP3_08501.1 (ECD, PAXBP1; 2/47); huMAP3_09504.1 (ECD, PAXBP1; 2/51); huMAP3_14306.1 (MCM4, SRCAP; 2/55); huMAP3_09945.1 (ECD, PAXBP1; 2/61)

### Novelty

The biological functions represented here are not new: DNA replication, RNA processing, chromatin regulation, ribosome biogenesis, and nuclear organization are established processes. The presence of known STRING relationships and repeated hu.MAP memberships further argues that important components and interactions are already documented. However, the particular cross-tissue co-abundance pattern and its combination of replication, RNA, chromatin, and nucleolar genes could still be a useful systems-level observation. The fact sheet does not provide an external module catalogue, replication cohort, perturbation experiment, or independent validation, so it cannot establish that the module is a new biological discovery. Absence of some genes from STRING or hu.MAP should be interpreted as incomplete prior coverage, not as evidence of novelty.

**Hypothesis.** Hypothesis: the module reflects a shared demand for nuclear biosynthetic capacity in proliferating or progenitor-like cells present in bone marrow and kidney samples. MCM4 and MCM7 could mark replication licensing and fork-associated activity, LIG1 could support replication and repair, EP300, HDAC3, SRCAP, and MTA3 could coordinate chromatin accessibility and transcription, while CPSF3, RBM7, RSRC1, PAXBP1, XPO5, and related factors could process, export, and regulate RNA. Nucleolar factors such as BRIX1, GTPBP4, NVL, and ZNHIT6 could provide ribosome and small-nucleolar-RNA support. Under this model, co-abundance across the two tissues reflects shared cellular composition or a shared proliferative state rather than a single physical megacomplex. This hypothesis should be tested with cell-composition adjustment, cell-state markers, protein-level localization, and independent tissue cohorts.

### Important genes

#### MCM4

- **Related proteins** (co-abundance neighbors): SIRAL1 (0.88); STRING partners: LIG1 (0.843), MCM7 (0.999), SMC2 (0.748)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 4. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication rel…
- **Diseases (Open Targets)**: primary immunodeficiency with natural-killer cell deficiency and adrenal insufficiency (0.714); X-linked adrenal hypoplasia congenita (0.185); lung adenocarcinoma (0.112); microcephaly (0.111); neoplasm (0.102)
- **Europe PMC papers**: 4082
- **Why important**: MCM4 is a central representative of the replication arm of the module. It is linked in STRING to MCM7, LIG1, and SMC2, and it recurs with MCM7 across multiple hu.MAP replication-associated complexes (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_07113.1) and (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1). It contributes to the primary nucleic-acid and macromolecule terms (GO:BP nucleic acid metabolic process; q_global = 4.68e-05), (GO:BP nucleobase-containing compound metabolic process; q_global = 0.00177), (GO:CC nucleus; q_global = 0.00267), and (GO:BP macromolecule metabolic process; q_global = 0.0457). Its established function is replication initiation, DNA metabolism, strand elongation, and DNA-damage response. Its bone-marrow-enhanced HPA pattern and enrichment in erythrocyte and megakaryocyte progenitor cell types make it informative for a proliferative progenitor interpretation. The gene has substantial disease and literature support, including replication-related human disorders and cancer associations.
- **Conclusion**: Established evidence supports MCM4 as a replication and genome-maintenance marker within the module. It is plausible, but not proven, that its co-abundance helps identify proliferating progenitor cells shared between the sampled tissues.

#### MCM7

- **Related proteins** (co-abundance neighbors): ECD (0.84), SIRAL1 (0.80); STRING partners: LIG1 (0.855), MCM4 (0.999), SMC2 (0.7)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 provides a concordant replication signal with MCM4 and is connected to LIG1 and SMC2 in STRING. Its repeated hu.MAP membership with MCM4 across replication-associated complexes (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_07113.1) and (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) is stronger evidence than co-abundance alone. It contributes to (GO:BP nucleic acid metabolic process; q_global = 4.68e-05), (GO:BP nucleobase-containing compound metabolic process; q_global = 0.00177), (GO:CC nucleus; q_global = 0.00267), and (GO:BP macromolecule metabolic process; q_global = 0.0457), and its established functions include replication initiation, DNA strand elongation, and DNA-damage response. HPA identifies bone marrow enhancement and several progenitor cell types, supporting a cell-cycle or progenitor-cell component. MCM7 has extensive literature and disease-association coverage, making it a well-established anchor rather than a speculative module member.
- **Conclusion**: Established evidence identifies MCM7 as a replication-complex component and a robust marker of the module's genome-duplication arm. The shared MCM4–MCM7 signal is more consistent with conserved replication biology than with an uncharacterized interaction.

#### EP300

- **Related proteins** (co-abundance neighbors): HDAC3 (0.84); STRING partners: CRTC2 (0.961), HDAC3 (0.958), SRCAP (0.911)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EP300 lysine acetyltransferase. This gene encodes the adenovirus E1A-associated cellular p300 transcriptional co-activator protein. It functions as histone acetyltransferase that regulates transcription via chromatin remodeling and is important in the processes of cell proliferation and differentiation. It mediates cAMP-gene regulation by binding specifically to phosphorylated CREB protein. This gene has also been identified as …
- **Diseases (Open Targets)**: Rubinstein-Taybi syndrome due to EP300 haploinsufficiency (0.797); Menke-Hennekam syndrome 2 (0.677); cancer (0.601); Rubinstein-Taybi syndrome (0.585); hereditary disease (0.551)
- **Europe PMC papers**: 17204
- **Why important**: EP300 is the strongest representative of the transcriptional and chromatin-regulatory arm. STRING links it to CRTC2, HDAC3, and SRCAP, connecting signaling-responsive transcription with acetylation, deacetylation, and chromatin remodeling. It contributes to every primary term (7 globally significant GO/KEGG terms, q_global 4.68e-05–0.0457; see the table) and is included in the supplementary nuclear and nucleic-acid categories (5 supplementary STRING terms; within-query FDR 0.0011–0.0196). Its established functions include histone acetyltransferase activity, transcriptional coactivation, chromatin remodeling, cell proliferation, differentiation, and hypoxia-related regulation. It is detected in both tissues and has very extensive literature and disease-association support, including a defined hereditary syndrome.
- **Conclusion**: Established evidence supports EP300 as a regulatory bridge linking chromatin state to transcription and cellular state. Its placement in this module could indicate coordinated transcriptional adaptation, but the module does not demonstrate a direct EP300-dependent mechanism.

#### HDAC3

- **Related proteins** (co-abundance neighbors): EP300 (0.84), POLR3D (0.83), NVL (0.83), PAXBP1 (0.81); STRING partners: EP300 (0.958)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: histone deacetylase 3. Histones play a critical role in transcriptional regulation, cell cycle progression, and developmental events. Histone acetylation/deacetylation alters chromosome structure and affects transcription factor access to DNA. The protein encoded by this gene belongs to the histone deacetylase/acuc/apha family. It has histone deacetylase activity and represses transcription when tethered to a promoter. …
- **Diseases (Open Targets)**: plasma cell myeloma (0.573); neoplasm (0.573); primary cutaneous T-cell non-Hodgkin lymphoma (0.566); neurodegenerative disease (0.529); Duchenne muscular dystrophy (0.518)
- **Europe PMC papers**: 15136
- **Why important**: HDAC3 complements EP300 by representing transcriptional repression, histone deacetylation, and chromatin organization. It is connected to EP300 in STRING and is also linked within the module to POLR3D, NVL, and PAXBP1. It contributes to all primary terms (7 globally significant GO/KEGG terms, q_global 4.68e-05–0.0457; see the table) and to the supplementary nuclear and macromolecule categories (4 supplementary STRING terms; within-query FDR 0.0011–0.0145). Its established functions include transcriptional regulation, protein deacetylation, chromatin organization, and cell-cycle-related regulation. HPA detects it in both tissues, and it has extensive literature and disease-association support, including hematologic and neoplastic disease relevance.
- **Conclusion**: Established evidence supports HDAC3 as a chromatin-regulatory component that could balance EP300-associated activation. A coordinated EP300–HDAC3 regulatory axis is a reasonable interpretation, but co-abundance alone cannot establish their temporal or causal relationship.

#### ECD

- **Related proteins** (co-abundance neighbors): BRIX1 (0.86), MCM7 (0.84), GTPBP4 (0.83), XPO5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_00424.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: ecdysoneless cell cycle regulator. Enables histone acetyltransferase binding activity. Involved in positive regulation of transcription by RNA polymerase II. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); alcohol drinking (0.209); breast cancer (0.092); gastric cancer (0.082); breast carcinoma (0.074)
- **Europe PMC papers**: 16795
- **Why important**: ECD is a connective node between several module themes: in the co-abundance graph it links to BRIX1, MCM7, GTPBP4, and XPO5. It contributes to all primary terms (7 globally significant GO/KEGG terms, q_global 4.68e-05–0.0457; see the table). hu.MAP places ECD with RSRC1 and PAXBP1 in an RNA-processing complex (hu.MAP huMAP3_08980.1), and with RNA-splicing and transcript-processing assemblies (hu.MAP huMAP3_00424.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), and (hu.MAP huMAP3_09945.1). Its established annotation supports transcriptional regulation and histone-acetyltransferase binding, with localization in nucleoplasm and cytosol. ECD is detected in both tissues and has very extensive literature and disease-association coverage, making it a plausible integrator rather than merely a low-information housekeeping marker.
- **Conclusion**: Established evidence supports ECD as a bridge between transcriptional regulation, RNA processing, and the nucleolar or replication-associated portions of the module. Its network position suggests coordination across nuclear processes, but whether ECD is mechanistically central remains a hypothesis requiring perturbation or interaction experiments.

## Module 3

**Tissue pair**: bone_marrow and kidney  
**Genes (41)**: AAAS, AATF, AKAP8L, ASCC3, CCDC134, CEP43, CHD1L, CHD1, DDX46, DDX52, POLA2, DHFR, ERCC3, GPN1, IGF2BP1, EIF4G3, LRWD1, ATF7IP, NAA25, NECAP2, NOL11, NPM3, NUP155, NUP98, ORC4, PHAX, POU2F1, PUM1, POLR1A, POLR2D, RPP40, SETDB1, SRRT, STEEP1, SUZ12, TAF2, DNTTIP2, GTF3C5, TIGAR, WDR12, WDR3

### Function

This is a predominantly nuclear gene-expression and RNA-processing module. The strongest primary evidence is for nucleoplasm and nuclear lumen localization (GO:CC nucleoplasm; q_global = 0.00013) (GO:CC nuclear lumen; q_global = 0.00099), with additional global evidence for the nucleus and nuclear protein-containing complexes (GO:CC nuclear protein-containing complex; q_global = 0.00315) (GO:CC nucleus; q_global = 0.00461). The module is also enriched for nucleic-acid binding and nucleic-acid metabolic processes (GO:MF nucleic acid binding; q_global = 0.00053) (GO:BP nucleic acid metabolic process; q_global = 0.00302), chromatin binding (GO:MF chromatin binding; q_global = 0.018), ribosomal small-subunit biogenesis (GO:BP ribosomal small subunit biogenesis; q_global = 0.0207), and ribonucleoprotein complexes (GO:CC ribonucleoprotein complex; q_global = 0.0316). Together, these findings support a coordinated program involving transcriptional regulation, chromatin organization, RNA maturation and export, ribosome biogenesis, and nuclear transport rather than a narrowly tissue-specific pathway. The supplementary STRING results reinforce nuclear, transcriptional, RNA-metabolic, helicase, chromatin, and nucleolar themes (15 supplementary STRING terms; within-query FDR 7.53e-07–0.0262), but they are treated as supporting evidence rather than primary global enrichment evidence.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only one secreted gene, CCDC134. It is also not strongly blood-cell enriched: most genes have low immune-cell specificity, with only limited immune-cell enhancement or detection patterns. Most genes have low tissue specificity, which is consistent with broadly expressed housekeeping or core nuclear machinery. The HPA protein-detection patterns in both bone marrow and kidney are broadly compatible with a shared cellular machinery signal, although many genes show cell-type enhancement in renal tubular populations and other specialized cell types. The frequent testis-associated tissue or cell-type annotations likely reflect expression specificity of individual genes rather than evidence that this is a testis module. Thus, the shared bone-marrow–kidney signal is more plausibly related to conserved cellular processes and shared proliferative or metabolically active cell populations than to circulating plasma contamination.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC nucleoplasm | 0.00013 | AAAS, AATF, AKAP8L, ASCC3, ATF7IP, CHD1, CHD1L, DDX46, DDX52, DNTTIP2, ERCC3, GPN1, GTF3C5, IGF2BP1, LRWD1, NOL11, NPM3, NUP98, ORC4, PHAX, POLA2, POLR1A, POLR2D, POU2F1, PUM1, RPP40, SETDB1, SRRT, STEEP1, SUZ12, TAF2, WDR12, WDR3 |
| GO:MF nucleic acid binding | 0.00053 | AATF, AKAP8L, ASCC3, CHD1, DDX46, DDX52, DHFR, DNTTIP2, EIF4G3, ERCC3, GTF3C5, IGF2BP1, LRWD1, NOL11, NPM3, NUP98, ORC4, PHAX, POLA2, POLR1A, POU2F1, PUM1, RPP40, SETDB1, SRRT, SUZ12, TAF2, WDR3 |
| GO:CC nuclear lumen | 0.00099 | AAAS, AATF, AKAP8L, ASCC3, ATF7IP, CHD1, CHD1L, DDX46, DDX52, DNTTIP2, ERCC3, GPN1, GTF3C5, IGF2BP1, LRWD1, NOL11, NPM3, NUP98, ORC4, PHAX, POLA2, POLR1A, POLR2D, POU2F1, PUM1, RPP40, SETDB1, SRRT, STEEP1, SUZ12, TAF2, WDR12, WDR3 |
| GO:BP nucleic acid metabolic process | 0.00302 | AKAP8L, ASCC3, ATF7IP, CHD1L, DDX46, DDX52, DNTTIP2, ERCC3, GTF3C5, IGF2BP1, LRWD1, NOL11, NPM3, NUP155, NUP98, ORC4, PHAX, POLA2, POLR1A, POLR2D, POU2F1, PUM1, RPP40, SRRT, SUZ12, TAF2, TIGAR, WDR12, WDR3 |
| GO:CC nuclear protein-containing complex | 0.00315 | AAAS, AATF, DDX46, DNTTIP2, ERCC3, LRWD1, NOL11, NUP155, NUP98, ORC4, POLA2, POLR1A, POLR2D, POU2F1, RPP40, SUZ12, TAF2, WDR12, WDR3 |
| GO:CC nucleus | 0.00461 | AAAS, AATF, AKAP8L, ASCC3, ATF7IP, CCDC134, CEP43, CHD1, CHD1L, DDX46, DDX52, DNTTIP2, ERCC3, GPN1, GTF3C5, IGF2BP1, LRWD1, NOL11, NPM3, NUP155, NUP98, ORC4, PHAX, POLA2, POLR1A, POLR2D, POU2F1, PUM1, RPP40, SETDB1, SRRT, STEEP1, SUZ12, TAF2, TIGAR, WDR12, WDR3 |
| GO:CC membraneless organelle | 0.0144 | AAAS, AATF, AKAP8L, ASCC3, ATF7IP, CEP43, CHD1, CHD1L, DDX46, DDX52, DNTTIP2, EIF4G3, IGF2BP1, LRWD1, NOL11, NPM3, NUP98, ORC4, PHAX, POLA2, POLR1A, POLR2D, POU2F1, PUM1, RPP40, SETDB1, SRRT, STEEP1, SUZ12, TAF2, WDR12, WDR3 |
| GO:CC intracellular membraneless organelle | 0.0144 | AAAS, AATF, AKAP8L, ASCC3, ATF7IP, CEP43, CHD1, CHD1L, DDX46, DDX52, DNTTIP2, EIF4G3, IGF2BP1, LRWD1, NOL11, NPM3, NUP98, ORC4, PHAX, POLA2, POLR1A, POLR2D, POU2F1, PUM1, RPP40, SETDB1, SRRT, STEEP1, SUZ12, TAF2, WDR12, WDR3 |
| GO:MF chromatin binding | 0.018 | CHD1, CHD1L, ERCC3, LRWD1, NPM3, NUP98, POLR1A, SETDB1, SUZ12, TAF2 |
| GO:BP ribosomal small subunit biogenesis | 0.0207 | AATF, DDX52, DNTTIP2, NOL11, RPP40, WDR3 |
| GO:CC ribonucleoprotein complex | 0.0316 | AATF, AKAP8L, DDX46, DNTTIP2, IGF2BP1, NUP98, PHAX, RPP40, SRRT, SUZ12, WDR12, WDR3 |

### STRING and hu.MAP

STRING supports several established physical or functional relationships within the module. Examples include the nuclear-pore relationships involving AAAS, NUP155, and NUP98; the nucleolar and small-subunit biogenesis relationships involving AATF, DDX52, DNTTIP2, NOL11, WDR3, and WDR12; the SETDB1–ATF7IP and SETDB1–SUZ12 chromatin relationships; the transcription-related links among ERCC3, TAF2, and POLR2D; and the RNA-export or processing relationship between PHAX and SRRT. hu.MAP independently places module genes in nuclear-pore complexes (hu.MAP huMAP3_12581.1) (hu.MAP huMAP3_07705.1) (hu.MAP huMAP3_09710.1), RNA-polymerase-associated complexes (hu.MAP huMAP3_14318.1) (hu.MAP huMAP3_11092.1) (hu.MAP huMAP3_09057.1) (hu.MAP huMAP3_08487.1) (hu.MAP huMAP3_06426.1), and SETDB1–ATF7IP complexes (hu.MAP huMAP3_04847.1) (hu.MAP huMAP3_05859.1) (hu.MAP huMAP3_07263.1) (hu.MAP huMAP3_15236.1) (hu.MAP huMAP3_12714.1). These observations show that substantial parts of the module recapitulate known molecular machinery. They also indicate that the co-abundance module is not equivalent to one physical complex: it combines nuclear pores, transcriptional machinery, chromatin regulators, ribosome-biogenesis factors, and RNA-processing components. Module edges without corresponding STRING or hu.MAP support may therefore represent co-regulation, indirect functional coupling, shared cell-state dependence, or incompletely catalogued interactions.

**STRING interactions (score >= 0.7)**: 25 of 820 gene pairs: AAAS–NUP155 (0.989); AAAS–NUP98 (0.96); AATF–DDX52 (0.972); AATF–DNTTIP2 (0.997); AATF–NOL11 (0.811); AATF–WDR12 (0.829); AATF–WDR3 (0.998); ATF7IP–SETDB1 (0.999); DDX52–NOL11 (0.829); DDX52–WDR12 (0.933); DNTTIP2–NOL11 (0.866); DNTTIP2–WDR3 (0.99); ERCC3–POLR2D (0.984); ERCC3–TAF2 (0.984); GPN1–POLR2D (0.771); LRWD1–ORC4 (0.987); NOL11–WDR12 (0.78); NOL11–WDR3 (0.951); NUP155–NUP98 (0.999); ORC4–POLA2 (0.747); PHAX–SRRT (0.987); POLR1A–WDR3 (0.948); POLR2D–TAF2 (0.914); SETDB1–SUZ12 (0.763); WDR12–WDR3 (0.954)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Nucleus (FDR = 7.53e-07, 34 genes); COMPARTMENTS Nucleus (FDR = 2.74e-05, 34 genes); Component Nucleoplasm (FDR = 3.59e-05, 32 genes); COMPARTMENTS Nuclear lumen (FDR = 9.44e-05, 23 genes); Function Nucleic acid binding (FDR = 0.00015, 28 genes); Component Nucleus (FDR = 0.00085, 36 genes); Component Nuclear protein-containing complex (FDR = 0.00085, 18 genes); Keyword Transcription (FDR = 0.0018, 15 genes); COMPARTMENTS Nucleolus (FDR = 0.0154, 12 genes); Function Organic cyclic compound binding (FDR = 0.016, 31 genes); Function Heterocyclic compound binding (FDR = 0.016, 31 genes); SMART DEAD-like helicases superfamily (FDR = 0.0181, 6 genes); SMART Helicase superfamily c-terminal domain (FDR = 0.0181, 6 genes); RCTM Metabolism of RNA (FDR = 0.0196, 14 genes); Function Chromatin binding (FDR = 0.0262, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12581.1 (NUP155, NUP98, AAAS; 3/58); huMAP3_14318.1 (POLR2D, POLR1A, GPN1; 3/58); huMAP3_11092.1 (POLR2D, POLR1A, GPN1; 3/65); huMAP3_04847.1 (SETDB1, ATF7IP; 2/2); huMAP3_05859.1 (SETDB1, ATF7IP; 2/3); huMAP3_07263.1 (SETDB1, ATF7IP; 2/3); huMAP3_15236.1 (SETDB1, ATF7IP; 2/4); huMAP3_12714.1 (SETDB1, ATF7IP; 2/8); huMAP3_07705.1 (NUP98, AAAS; 2/9); huMAP3_09710.1 (NUP98, AAAS; 2/13); huMAP3_09057.1 (POLR1A, GPN1; 2/36); huMAP3_08487.1 (POLR1A, GPN1; 2/37); huMAP3_06426.1 (POLR1A, GPN1; 2/38)

### Novelty

The module should not be described as a newly discovered molecular complex. Several of its relationships and substructures are already represented in STRING and hu.MAP, and many member genes are well studied core nuclear factors. Nevertheless, the conserved co-abundance of this particular gene combination across bone marrow and kidney may still be a new systems-level observation, because database membership does not establish that these genes have previously been reported as a shared cross-tissue co-abundance module. The evidence supports cautious novelty at the level of module organization or tissue-pair reproducibility, not novelty of the individual interactions. Absence of a gene from STRING or hu.MAP is insufficient to establish a novel interaction or pathway.

**Hypothesis.** Hypothesis: the module reflects a conserved nuclear capacity program that couples transcription initiation, chromatin state, DNA replication or repair, RNA processing and export, and ribosome production. In bone marrow and kidney, this program may be co-abundant because cells with substantial biosynthetic demand or active proliferation require coordinated operation of nuclear pores, transcriptional machinery, chromatin regulators, and ribosome-biogenesis systems. TAF2 and POU2F1 may provide transcriptional coordination, SETDB1 and ATF7IP may connect transcriptional state to heterochromatin, POLR1A and the nucleolar factors may support ribosomal RNA production, and NUP98, NUP155, and AAAS may support nucleocytoplasmic exchange. This is a mechanistic model rather than proof of direct physical assembly or causal regulation; it should be tested with cell-composition adjustment, perturbation experiments, and measurements of transcription, chromatin state, RNA processing, and ribosome biogenesis.

### Important genes

#### TAF2

- **Related proteins** (co-abundance neighbors): GTF3C5 (0.92), PUM1 (0.90), POLR1A (0.90), ORC4 (0.90), DDX52 (0.89), NOL11 (0.89), WDR3 (0.88), TIGAR (0.88), ERCC3 (0.85), CHD1 (0.85), SRRT (0.84), AKAP8L (0.84), ASCC3 (0.84), NUP98 (0.83), POLA2 (0.82), PHAX (0.82), WDR12 (0.81); STRING partners: ERCC3 (0.984), POLR2D (0.914)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TATA-box binding protein associated factor 2. Initiation of transcription by RNA polymerase II requires the activities of more than 70 polypeptides. The protein that coordinates these activities is transcription factor IID (TFIID), which binds to the core promoter to position the polymerase properly, serves as the scaffold for assembly of the remainder of the transcription complex, and acts as a channel for regulatory signals. TFIID is compos…
- **Diseases (Open Targets)**: microcephaly-thin corpus callosum-intellectual disability syndrome (0.704); HIV infectious disease (0.579); neurodegenerative disease (0.462); myelodysplastic syndrome (0.230); placenta praevia (0.225)
- **Europe PMC papers**: 603
- **Why important**: TAF2 has the strongest module connectivity in the supplied network and links genes involved in transcription, replication, RNA processing, and nucleolar functions. It is present across most primary nuclear, nucleic-acid, chromatin, and complex-related enrichment terms (9 globally significant GO/KEGG terms, q_global 0.00013–0.018; see the table). Its annotation identifies it as a TFIID-associated transcription-initiation factor, and its established STRING relationships with ERCC3 and POLR2D connect transcription initiation with transcription-coupled repair and RNA polymerase activity. Its extensive literature supports a well-established role rather than an uncharacterized marker.
- **Conclusion**: Established evidence supports TAF2 as a central transcriptional scaffold and a plausible network organizer. The hypothesis that it coordinates the entire module is reasonable from its network position but is not demonstrated by the co-abundance data alone.

#### AATF

- **Related proteins** (co-abundance neighbors): POU2F1 (0.94), NAA25 (0.85), NUP155 (0.84), CEP43 (0.84); STRING partners: DDX52 (0.972), DNTTIP2 (0.997), NOL11 (0.811), WDR12 (0.829), WDR3 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apoptosis antagonizing transcription factor. The protein encoded by this gene was identified on the basis of its interaction with MAP3K12/DLK, a protein kinase known to be involved in the induction of cell apoptosis. This gene product contains a leucine zipper, which is a characteristic motif of transcription factors, and was shown to exhibit strong transactivation activity when fused to Gal4 DNA binding domain. Overexpression of this gene i…
- **Diseases (Open Targets)**: skin neoplasm (0.147); generalized dystonia (0.116); multinodular goiter (0.115); bone fracture (0.113); neoplasm (0.107)
- **Europe PMC papers**: 6349
- **Why important**: AATF connects POU2F1 with nucleolar and ribosome-biogenesis factors in the module. It appears in the primary evidence for nuclear localization, nuclear complexes, ribosomal small-subunit biogenesis, and ribonucleoprotein complexes (8 globally significant GO/KEGG terms, q_global 0.00013–0.0316; see the table). STRING supports relationships with DDX52, DNTTIP2, NOL11, WDR12, and WDR3, while its annotation includes RNA maturation, ribosome-biogenesis, transcriptional regulation, and apoptosis-related activity. It is detected in kidney and shows enhancement in several renal tubular cell types, providing a possible link to the kidney component without making the module kidney-specific.
- **Conclusion**: Established evidence supports AATF as a bridge between nucleolar RNA-production machinery and transcriptional or stress-related regulation. Its role as a cross-tissue driver of the module remains a hypothesis.

#### SETDB1

- **Related proteins** (co-abundance neighbors): NPM3 (0.86), DDX46 (0.81), POU2F1 (0.80); STRING partners: ATF7IP (0.999), SUZ12 (0.763)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_04847.1, huMAP3_05859.1, huMAP3_07263.1, huMAP3_15236.1, huMAP3_12714.1
- **Function (MyGene.info)**: SET domain bifurcated histone lysine methyltransferase 1. This gene encodes a histone methyltransferase which regulates histone methylation, gene silencing, and transcriptional repression. This gene has been identified as a target for treatment in Huntington Disease, given that gene silencing and transcription dysfunction likely play a role in the disease pathogenesis. Alternatively spliced transcript variants of this gene have been described.[provided b…
- **Diseases (Open Targets)**: acute myeloid leukemia (0.251); hepatocellular carcinoma (0.238); B-cell chronic lymphocytic leukemia (0.229); head and neck squamous cell carcinoma (0.226); pleural mesothelioma (0.217)
- **Europe PMC papers**: 5377
- **Why important**: SETDB1 is a chromatin-binding histone methyltransferase associated with gene silencing, heterochromatin, and transcriptional repression. It contributes to the primary chromatin-binding evidence (GO:MF chromatin binding; q_global = 0.018) and broader nuclear and nucleic-acid evidence (8 globally significant GO/KEGG terms, q_global 0.00013–0.0144; see the table). It is connected by STRING to ATF7IP and SUZ12, and it occurs with ATF7IP across several hu.MAP complexes (hu.MAP huMAP3_04847.1) (hu.MAP huMAP3_05859.1) (hu.MAP huMAP3_07263.1) (hu.MAP huMAP3_15236.1) (hu.MAP huMAP3_12714.1), giving this pair unusually direct complex-level support within the module. SETDB1 also has substantial literature and disease associations, including hematologic and cancer-related annotations.
- **Conclusion**: Established evidence supports SETDB1 as a chromatin-state regulator that could connect nuclear transcriptional activity with repression and genome organization. It is plausible that SETDB1 helps define the module's regulatory state, but the data do not establish that its enzymatic activity drives the observed co-abundance.

#### POLR1A

- **Related proteins** (co-abundance neighbors): TAF2 (0.90), CEP43 (0.85); STRING partners: WDR3 (0.948)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoli fibrillar center; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_14318.1, huMAP3_11092.1, huMAP3_09057.1, huMAP3_08487.1, huMAP3_06426.1
- **Function (MyGene.info)**: RNA polymerase I subunit A. The protein encoded by this gene is the largest subunit of the RNA polymerase I complex. The encoded protein represents the catalytic subunit of the complex, which transcribes DNA into ribosomal RNA precursors. Defects in this gene are a cause of the Cincinnati type of acrofacial dysostosis. [provided by RefSeq, May 2016].
- **Diseases (Open Targets)**: choanal atresia-hearing loss-cardiac defects-craniofacial dysmorphism syndrome (0.780); acrofacial dysostosis Cincinnati type (0.723); leukodystrophy, hypomyelinating, 27 (0.459); acrofacial dysostosis (0.372); microtia (0.370)
- **Europe PMC papers**: 555
- **Why important**: POLR1A is the catalytic subunit of RNA polymerase I and provides a direct mechanistic anchor for nucleolar large-ribosomal-RNA transcription. It participates in the primary nuclear, nucleic-acid, nuclear-complex, chromatin, and ribonucleoprotein evidence (10 globally significant GO/KEGG terms, q_global 0.00013–0.0316; see the table). It is represented with GPN1 and POLR2D in multiple hu.MAP polymerase-associated complexes (hu.MAP huMAP3_14318.1) (hu.MAP huMAP3_11092.1) (hu.MAP huMAP3_09057.1) (hu.MAP huMAP3_08487.1) (hu.MAP huMAP3_06426.1), while STRING links it to WDR3. Its disease associations include developmental and craniofacial disorders, and its literature supports a well-established transcriptional role.
- **Conclusion**: Established evidence supports POLR1A as a core nucleolar transcription component and a strong explanation for the module's ribosome-biogenesis signal. Its presence does not prove that every module gene participates directly in RNA polymerase I function.

#### NUP98

- **Related proteins** (co-abundance neighbors): TAF2 (0.83); STRING partners: AAAS (0.96), NUP155 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12581.1, huMAP3_07705.1, huMAP3_09710.1
- **Function (MyGene.info)**: nucleoporin 98 and 96 precursor. Nuclear pore complexes (NPCs) regulate the transport of macromolecules between the nucleus and cytoplasm, and are composed of many polypeptide subunits, many of which belong to the nucleoporin family. This gene belongs to the nucleoporin gene family and encodes a 186 kDa precursor protein that undergoes autoproteolytic cleavage to generate a 98 kDa nucleoporin and 96 kDa nucleoporin. The 98 kDa nu…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); acute myeloid leukemia (0.399); lung carcinoma (0.376)
- **Europe PMC papers**: 4839
- **Why important**: NUP98 represents the nuclear-pore and nucleocytoplasmic-transport arm of the module. It is included in primary evidence for nuclear localization, nuclear complexes, nucleic-acid metabolism, chromatin binding, and ribonucleoprotein complexes (10 globally significant GO/KEGG terms, q_global 0.00013–0.0316; see the table). STRING supports its relationships with AAAS and NUP155, and hu.MAP places it with AAAS in nuclear-pore complexes (hu.MAP huMAP3_12581.1) (hu.MAP huMAP3_07705.1) (hu.MAP huMAP3_09710.1). Its annotation includes RNA export, protein import, nuclear-pore organization, and peripheral tethering of transcriptional loci. It also has substantial literature and established associations with viral disease and leukemia-related biology.
- **Conclusion**: Established evidence supports NUP98 as a transport and nuclear-organization component that can connect RNA production with export. Its inclusion supports coordinated nuclear logistics, but it does not demonstrate that altered pore transport causes the shared tissue co-abundance pattern.

## Module 4

**Tissue pair**: bone_marrow and kidney  
**Genes (5)**: ABHD14B, SERPINC1, APOA1, CRYZ, S100A9

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established pathway assignment from enrichment. The most defensible functional interpretation comes from the individual gene annotations and the network. APOA1 and SERPINC1 connect the module to circulating lipid transport and regulation of blood coagulation, while S100A9 represents myeloid inflammatory biology. CRYZ provides a kidney- and liver-associated redox or quinone-reductase component, and ABHD14B is a less characterized nuclear or cytosolic gene linked to transcriptional regulation. APOA1 is the main network hub and connects to the other module components, whereas ABHD14B links APOA1 with S100A9. Overall, this is better interpreted as a mixed circulating-protein, inflammatory-cell, and kidney or liver-associated co-abundance pattern than as a coherent canonical pathway.

**Cell composition.** The module is strongly influenced by tissue and sample composition. APOA1, SERPINC1, and S100A9 are secreted to blood, making secreted or plasma-associated proteins a majority of the module. HPA tissue evidence points repeatedly to liver and hepatocytes, with APOA1 and SERPINC1 tissue-enriched in liver and CRYZ tissue-enhanced in kidney and liver. S100A9 is associated with bone marrow and with classical monocytes and neutrophils, while APOA1 has an immune-cell-enhanced association with plasmacytoid dendritic cells. Protein detection is present for some but not all genes in each target tissue. These observations make blood content, hepatic protein production, and shared or variable cell populations important alternative explanations for the cross-tissue module. The module is therefore not evidence that all of its proteins are produced by the same kidney or bone-marrow cell.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports one high-confidence relationship within the module, APOA1--SERPINC1, which is consistent with a known plasma, lipid-transport, and coagulation context. STRING reports no supplementary functional enrichment. hu.MAP places APOA1 and SERPINC1 together in complex C1, but they are only a small subset of a much larger complex annotation dominated by circulating proteins, complement-related proteins, coagulation proteins, apolipoproteins, and other serum-associated factors. This supports shared extracellular or plasma biology, but does not establish a physical complex containing all module genes. ABHD14B, S100A9, and CRYZ have no listed hu.MAP membership or STRING partner in the provided evidence. The co-abundance edges involving these genes may therefore reflect shared sample composition or correlated regulation rather than known direct molecular interactions.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: APOA1–SERPINC1 (0.708)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINC1, APOA1; 2/64)

### Novelty

The module should not be called a newly discovered biological pathway. Its APOA1--SERPINC1 relationship and the associated plasma, lipid, and coagulation context are already represented in external interaction and complex resources. At most, the joint co-abundance pattern across bone marrow and kidney, particularly the connection of APOA1 with ABHD14B, S100A9, and CRYZ, may be a potentially novel data-driven observation. However, the provided evidence does not establish that these associations are mechanistically new: absence from STRING or hu.MAP is not proof of novelty, the module is small, and its composition is compatible with blood carryover, hepatic plasma proteins, or shared cell populations. Replication, adjustment for cell composition and plasma abundance, and independent molecular validation would be required before claiming a novel mechanism.

**Hypothesis.** Hypothesis: variation in circulating hepatic proteins, especially APOA1 and SERPINC1, co-varies across bone-marrow and kidney samples with a myeloid inflammatory signal marked by S100A9 and with tissue-associated metabolic or redox biology represented by CRYZ. ABHD14B may participate in, or report, a transcriptional or cellular-state response that links the circulating and inflammatory components. Under this model, the shared module reflects an interaction between systemic plasma composition, marrow myeloid abundance, and kidney or liver-associated cellular state rather than a single intracellular pathway. This is a hypothesis rather than an established causal mechanism; testing would require cell-resolved data, plasma-aware analyses, and targeted validation of the non-canonical co-abundance relationships.

### Important genes

#### APOA1

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.87), ABHD14B (0.86), CRYZ (0.80); STRING partners: SERPINC1 (0.708)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 has the strongest network position and is the hub connecting the other module genes. It is the major HDL protein, promotes cholesterol efflux, and supports lecithin cholesterol acyltransferase activity. It is secreted to blood, tissue-enriched in liver, associated with enterocytes and hepatocytes, and linked to disorders of HDL biology and familial amyloidosis. Its extensive literature also makes it the best-established biological anchor for the module. Its STRING relationship with SERPINC1 and shared hu.MAP membership provide external support for the plasma-associated part of the module.
- **Conclusion**: Established evidence supports APOA1 as a circulating hepatic lipid-transport protein and as the central network anchor. It is plausible, but not established, that APOA1 is the biological driver of the cross-tissue module; sample plasma content could instead account for its centrality.

#### SERPINC1

- **Related proteins** (co-abundance neighbors): APOA1 (0.87); STRING partners: APOA1 (0.708)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 is directly connected to APOA1 and shares hu.MAP complex C1 with it. It encodes antithrombin, a plasma serpin that inhibits thrombin and other activated coagulation proteases. It is secreted to blood, enriched in liver and hepatocytes, and has well-established associations with hereditary antithrombin deficiency and venous thromboembolic disease. Its established coagulation function gives the module a clinically meaningful plasma component.
- **Conclusion**: Established evidence supports SERPINC1 as a hepatic plasma anticoagulant and as part of the known APOA1-associated extracellular signal. A coordinated coagulation mechanism spanning kidney and marrow remains a hypothesis, not a conclusion from this module alone.

#### S100A9

- **Related proteins** (co-abundance neighbors): ABHD14B (0.85); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Group enriched; location Plasma membrane, Intermediate filaments, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: S100 calcium binding protein A9. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: inborn error of immunity (0.370); Sepsis (0.121); neoplasm (0.119); psoriasis (0.114); cancer (0.114)
- **Europe PMC papers**: 16393
- **Why important**: S100A9 is the module's strongest marker of bone-marrow and myeloid biology. It is associated with bone marrow, classical monocytes, and neutrophils, is secreted to blood, and has extensive literature connecting it with leukocyte migration and inflammatory responses. Its edge to ABHD14B is not supported by a listed STRING partner or hu.MAP complex, which makes it important for assessing whether the module reflects cell composition or a less-characterized regulatory relationship. Its disease associations include immune disorders, sepsis, psoriasis, and cancer.
- **Conclusion**: Established evidence supports S100A9 as a myeloid and inflammatory marker that could report bone-marrow cell abundance or activation. It is not established that S100A9 mechanistically connects to APOA1, SERPINC1, or CRYZ in this module.

#### CRYZ

- **Related proteins** (co-abundance neighbors): APOA1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: crystallin zeta. Crystallins are separated into two classes: taxon-specific, or enzyme, and ubiquitous. The latter class constitutes the major proteins of vertebrate eye lens and maintains the transparency and refractive index of the lens. The former class is also called phylogenetically-restricted crystallins. This gene encodes a taxon-specific crystallin protein which has NADPH-dependent quinone reductase activi…
- **Diseases (Open Targets)**: response to paracetamol (0.249); amyotrophic lateral sclerosis (0.220); adolescent idiopathic scoliosis (0.205); ovarian neoplasm (0.170); Wheezing (0.125)
- **Europe PMC papers**: 864
- **Why important**: CRYZ is directly connected to the APOA1 hub and is tissue-enhanced in kidney and liver, with detection in both bone marrow and kidney. It encodes a taxon-specific crystallin with NADPH-dependent quinone reductase activity and annotations involving xenobiotic catabolism and mRNA stabilization. Its kidney association makes it important for interpreting why this module is shared with kidney, while its moderate literature volume and limited external interaction support argue for a careful, exploratory interpretation.
- **Conclusion**: Established evidence supports CRYZ as a kidney- and liver-associated cytosolic enzyme with redox or xenobiotic-related functions. Its connection to APOA1 may represent shared tissue state, metabolic regulation, or sample composition; a direct functional role in the module is hypothetical.

#### ABHD14B

- **Related proteins** (co-abundance neighbors): APOA1 (0.86), S100A9 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: abhydrolase domain containing 14B. Enables hydrolase activity. Involved in positive regulation of transcription by RNA polymerase II. Located in cytosol; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.432); immune system disorder (0.070); type 2 diabetes mellitus (0.015); gout (0.009); neoplasm (0.008)
- **Europe PMC papers**: 216
- **Why important**: ABHD14B is a bridge node between APOA1 and S100A9 in the co-abundance network, giving it importance despite limited annotation and a comparatively small literature base. HPA detects it in bone marrow and kidney, and its reported functions include hydrolase activity, positive regulation of transcription by RNA polymerase II, and a phosphoadenosine-phosphosulfate metabolic process. It has no listed STRING partner or hu.MAP complex membership, so its network position is not independently supported by the provided interaction resources.
- **Conclusion**: Established evidence supports ABHD14B as a detected intracellular protein with hydrolase and transcription-related annotations. Its bridge position may indicate a genuine regulatory link between inflammatory and circulating signals, but this is the most speculative interpretation and requires independent validation.

## Module 5

**Tissue pair**: bone_marrow and kidney  
**Genes (15)**: ABI2, ASH2L, DCAF7, SHMT2, MACROH2A1, KRI1, METAP1, ALDH18A1, PHC2, PRAF2, PRDX4, QKI, RNF2, SCRN3, UBA5

### Function

The strongest functional interpretation is a chromatin and transcriptional-regulation module with a Polycomb-centered core. The only globally significant GO/KEGG result is enrichment of the PRC1 complex (GO:CC PRC1 complex; q_global = 0.0394), contributed by PHC2 and RNF2. PHC2 is a central network hub and RNF2 is a core Polycomb protein involved in transcriptional repression, chromatin remodeling, heterochromatin formation, and epigenetic regulation. ASH2L provides a second chromatin-related connection through its role in histone H3-K4 methylation and the MLL3/4 and Set1C/COMPASS complexes. The module also contains a metabolically coherent mitochondrial branch involving SHMT2 and ALDH18A1, but that branch is not supported by a globally significant GO/KEGG term. Thus, the primary interpretation is Polycomb-associated chromatin regulation, with linked metabolic and cellular-stress components rather than a uniformly single-process module. The absence of STRING functional enrichment does not invalidate the module, particularly because the module is small and contains several poorly characterized or indirectly connected genes.

**Cell composition.** This is not a module dominated by plasma or secreted proteins: the HPA summary identifies only a single secreted gene, and the listed proteins are predominantly intracellular, with many localized to the nucleus, mitochondria, cytosol, endoplasmic reticulum, or vesicles. Most genes have low tissue specificity, while many show cell-type enhancement across diverse cell types, including neural, reproductive, epithelial, hepatic, and stromal populations. Blood-cell specificity is generally low, with PHC2 showing neutrophil enrichment and UBA5 having annotations related to erythrocyte and megakaryocyte differentiation. Protein detection is broad in kidney and present for most genes in bone marrow, so the shared signal is not convincingly explained by a plasma-protein contribution or by a strongly blood-cell-specific module. Shared cellular programs, ubiquitous expression, or variation in cellular composition remain plausible contributors.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC PRC1 complex | 0.0394 | PHC2, RNF2 |

### STRING and hu.MAP

The known interaction structure is concentrated in a few relationships. PHC2-RNF2 is a very strong STRING-supported interaction and is represented in all three hu.MAP complexes (hu.MAP huMAP3_02464.1), (hu.MAP huMAP3_10162.1), and (hu.MAP huMAP3_14051.1). ASH2L-RNF2 is also supported by STRING, linking the Polycomb-associated signal to a histone-methylation-associated factor. ALDH18A1-SHMT2 is supported by STRING and provides evidence for a mitochondrial metabolic submodule. There is no STRING functional-enrichment result. The hu.MAP results are especially informative because PHC2 and RNF2 occur together in complexes whose other members include CBX proteins, BMI1, RING1, PCGF proteins, BCOR-family proteins, PHC-family proteins, and other Polycomb-associated factors. These observations establish that part of the module recapitulates known molecular machinery, while most module genes are not assigned to the listed hu.MAP complexes and are not connected by high-confidence STRING relationships.

**STRING interactions (score >= 0.7)**: 3 of 105 gene pairs: ALDH18A1–SHMT2 (0.804); ASH2L–RNF2 (0.794); PHC2–RNF2 (0.997)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02464.1 (PHC2, RNF2; 2/7); huMAP3_10162.1 (PHC2, RNF2; 2/37); huMAP3_14051.1 (PHC2, RNF2; 2/50)

### Novelty

The module should not be described as a newly discovered Polycomb complex. The PHC2-RNF2 relationship is already strongly supported by STRING and is present in multiple hu.MAP complexes (hu.MAP huMAP3_02464.1), (hu.MAP huMAP3_10162.1), and (hu.MAP huMAP3_14051.1), while the broader Polycomb interpretation is already established by the functions of PHC2 and RNF2. The SHMT2-ALDH18A1 relationship is also already represented in STRING. A potentially novel aspect is the co-abundance of this particular mixture of Polycomb, metabolic, RNA-processing, redox, and protein-homeostasis genes across bone marrow and kidney, but the fact sheet does not establish that this cross-tissue arrangement is biologically novel. The lack of STRING or hu.MAP support for several peripheral genes cannot by itself demonstrate novelty; it may reflect incomplete interaction coverage, indirect regulation, or tissue-dependent co-abundance.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in which Polycomb-associated chromatin control is coordinated with mitochondrial amino-acid metabolism and proteostatic or redox demands. In this model, PHC2 and RNF2 form the chromatin-regulatory anchor, ASH2L represents an opposing or complementary histone-methylation context, and SHMT2 with ALDH18A1 represents metabolic support for cells requiring mitochondrial one-carbon, glycine, and amino-acid metabolism. The remaining genes may capture connected effects on RNA processing, ubiquitin-like modification, protein maturation, oxidative-stress handling, vesicular function, and membrane transport. This is a mechanistic hypothesis rather than a demonstrated causal pathway; the co-abundance data and annotations do not show direct regulation between these components.

### Important genes

#### PHC2

- **Related proteins** (co-abundance neighbors): SHMT2 (0.92), UBA5 (0.89), KRI1 (0.88), DCAF7 (0.88), PRDX4 (0.87), METAP1 (0.84), ASH2L (0.84); STRING partners: RNF2 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_02464.1, huMAP3_10162.1, huMAP3_14051.1
- **Function (MyGene.info)**: polyhomeotic homolog 2. In Drosophila melanogaster, the 'Polycomb' group (PcG) of genes are part of a cellular memory system that is responsible for the stable inheritance of gene activity. PcG proteins form a large multimeric, chromatin-associated protein complex. The protein encoded by this gene has homology to the Drosophila PcG protein 'polyhomeotic' (Ph) and is known to heterodimerize with EDR1 and colocalize with B…
- **Diseases (Open Targets)**: neurodegenerative disease (0.341); Abnormality of the skeletal system (0.233); smoking initiation (0.227); breast cancer (0.170); risk-taking behaviour (0.161)
- **Europe PMC papers**: 586
- **Why important**: PHC2 is the most central network gene in the module and connects the chromatin-related signal to several otherwise weakly connected genes. It is one of the two genes in the globally significant PRC1-complex term (GO:CC PRC1 complex; q_global = 0.0394), has the strongest STRING relationship in the module with RNF2, and occurs in all three hu.MAP complexes (hu.MAP huMAP3_02464.1), (hu.MAP huMAP3_10162.1), and (hu.MAP huMAP3_14051.1). Its Polycomb-related function, nuclear localization, detection in both tissues, and substantial literature support make it the clearest organizational anchor.
- **Conclusion**: Established evidence supports PHC2 as a Polycomb-associated chromatin regulator and as the principal network hub. It is reasonable to conclude that PHC2 is central to the module's primary functional interpretation. It remains unestablished whether PHC2 drives the cross-tissue co-abundance pattern or merely marks a shared chromatin-regulatory state.

#### RNF2

- **Related proteins** (co-abundance neighbors): QKI (0.84), SHMT2 (0.81); STRING partners: ASH2L (0.794), PHC2 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_02464.1, huMAP3_10162.1, huMAP3_14051.1
- **Function (MyGene.info)**: ring finger protein 2. Polycomb group (PcG) of proteins form the multiprotein complexes that are important for the transcription repression of various genes involved in development and cell proliferation. The protein encoded by this gene is one of the PcG proteins. It has been shown to interact with, and suppress the activity of, transcription factor CP2 (TFCP2/CP2). Studies of the mouse counterpart suggested the involv…
- **Diseases (Open Targets)**: Luo-Schoch-Yamamoto syndrome (0.616); complex neurodevelopmental disorder (0.370); neurodegenerative disease (0.352); body weight gain (0.278); glomerulonephritis (0.220)
- **Europe PMC papers**: 1811
- **Why important**: RNF2 is the second member of the globally significant PRC1-complex term (GO:CC PRC1 complex; q_global = 0.0394) and has a high-confidence STRING interaction with PHC2. It is present with PHC2 in all three hu.MAP complexes (hu.MAP huMAP3_02464.1), (hu.MAP huMAP3_10162.1), and (hu.MAP huMAP3_14051.1). Its established roles in Polycomb-mediated transcriptional repression, chromatin remodeling, heterochromatin formation, epigenetic regulation, and cell proliferation directly support the module's principal interpretation. It also has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence identifies RNF2 as a core Polycomb and chromatin-regulatory component of the module. Its relationship with PHC2 is supported by both interaction resources and the enrichment result. The module does not establish whether altered RNF2 activity is responsible for the associated metabolic and cellular-state genes.

#### SHMT2

- **Related proteins** (co-abundance neighbors): PHC2 (0.92), ABI2 (0.86), ALDH18A1 (0.82), RNF2 (0.81), PRAF2 (0.80); STRING partners: ALDH18A1 (0.804)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine hydroxymethyltransferase 2. This gene encodes the mitochondrial form of a pyridoxal phosphate-dependent enzyme that catalyzes the reversible reaction of serine and tetrahydrofolate to glycine and 5,10-methylene tetrahydrofolate. The encoded product is primarily responsible for glycine synthesis. The activity of the encoded protein has been suggested to be the primary source of intracellular glycine. The gene which encodes th…
- **Diseases (Open Targets)**: neurodevelopmental disorder with cardiomyopathy, spasticity, and brain abnormalities (0.771); microcephaly (0.370); polymicrogyria (0.370); neurodevelopmental disorder (0.336); hereditary disease (0.192)
- **Europe PMC papers**: 2579
- **Why important**: SHMT2 is a major network connector outside the Polycomb pair, linking PHC2 to ALDH18A1 and several other module genes. STRING supports its relationship with ALDH18A1, and its mitochondrial enzyme function connects the module to glycine synthesis, serine metabolism, and one-carbon metabolism. It is detected in both tissues, has strong tissue and disease literature coverage, and provides a biologically plausible metabolic component even though it is absent from the primary GO/KEGG result.
- **Conclusion**: Established evidence supports SHMT2 as a mitochondrial metabolic enzyme and as the anchor of a secondary metabolic branch. Its inclusion strengthens the interpretation of a mixed chromatin-metabolic state, but the co-abundance data do not prove that SHMT2 metabolism is mechanistically coupled to PRC1 activity.

#### ASH2L

- **Related proteins** (co-abundance neighbors): PHC2 (0.84); STRING partners: RNF2 (0.794)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ASH2 like, histone lysine methyltransferase complex subunit. Enables beta-catenin binding activity and transcription cis-regulatory region binding activity. Contributes to histone methyltransferase activity (H3-K4 specific). Involved in histone H3-K4 methylation; positive regulation of cell population proliferation; and response to estrogen. Acts upstream of or within cellular response to DNA damage stimulus. Located in nucleus. Part of MLL3/4 complex and S…
- **Diseases (Open Targets)**: neurodegenerative disease (0.502); venous thromboembolism (0.351); Intellectual disability (0.266); Global developmental delay (0.266); preeclampsia (0.200)
- **Europe PMC papers**: 1621
- **Why important**: ASH2L is a chromatin-associated factor connected to PHC2 in the co-abundance network and to RNF2 through STRING. It participates in histone H3-K4 methylation, transcription-coupled chromatin remodeling, DNA-damage response, and hematopoietic processes. Although it is not part of the primary enriched term (GO:CC PRC1 complex; q_global = 0.0394), it supplies independent functional context for interpreting the module as a coordinated chromatin-regulatory program. Its substantial literature and disease-association coverage further support its importance.
- **Conclusion**: Established evidence supports ASH2L as a histone-methylation and transcriptional-regulation factor that is plausibly related to the module's chromatin signal. Its direct functional integration with PHC2 and RNF2 within this cross-tissue module remains a hypothesis rather than a demonstrated molecular interaction pattern.

#### ALDH18A1

- **Related proteins** (co-abundance neighbors): MACROH2A1 (0.83), SHMT2 (0.82); STRING partners: SHMT2 (0.804)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 18 family member A1. This gene is a member of the aldehyde dehydrogenase family and encodes a bifunctional ATP- and NADPH-dependent mitochondrial enzyme with both gamma-glutamyl kinase and gamma-glutamyl phosphate reductase activities. The encoded protein catalyzes the reduction of glutamate to delta1-pyrroline-5-carboxylate, a critical step in the de novo biosynthesis of proline, ornithine and arginine. Mutations in …
- **Diseases (Open Targets)**: ALDH18A1-related de Barsy syndrome (0.832); cutis laxa, autosomal dominant 3 (0.816); autosomal recessive complex spastic paraplegia type 9B (0.814); de Barsy syndrome (0.731); autosomal dominant spastic paraplegia type 9 (0.706)
- **Europe PMC papers**: 1168
- **Why important**: ALDH18A1 is linked to SHMT2 by STRING and occupies the metabolic branch connected to the module's chromatin-centered hub through SHMT2. Its mitochondrial enzyme activity supplies a defined role in proline, ornithine, arginine, and citrulline biosynthesis. It is detected in both tissues, has substantial literature, and has well-established associations with inherited metabolic and connective-tissue disorders.
- **Conclusion**: Established evidence supports ALDH18A1 as a mitochondrial amino-acid biosynthesis enzyme and supports its known relationship with SHMT2. Its presence suggests that amino-acid metabolism may accompany the shared module state, but there is no primary enrichment result demonstrating that this metabolic pathway defines the module.

## Module 6

**Tissue pair**: bone_marrow and kidney  
**Genes (23)**: ACADM, ACSF2, SLC25A4, BPHL, CMBL, SORD, FH, GALM, HBA1, ALAD, IDH2, AK4, ALDH6A1, NQO2, DBT, PCCA, PCCB, PCK2, ACAT1, ACAA2, TST, TMT1A, TTC38

### Function

This is a mitochondrial metabolic co-abundance module centered on small-molecule, organic-acid, carboxylic-acid, fatty-acid and branched-chain amino-acid catabolism. The primary evidence is the concordant set of globally corrected GO and KEGG terms (GO:BP small molecule catabolic process; q_global = 3.37e-07) through (GO:BP lipid catabolic process; q_global = 0.03), including mitochondrial matrix localization (GO:CC mitochondrial matrix; q_global = 8.39e-06), broad metabolic pathways (GO:BP small molecule metabolic process; q_global = 8.68e-05) (KEGG Metabolic pathways - Homo sapiens (human); q_global = 0.000375), branched-chain amino-acid degradation (KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 3.07e-05) (GO:BP branched-chain amino acid metabolic process; q_global = 0.000841), fatty-acid catabolism (GO:BP fatty acid catabolic process; q_global = 0.00131) (GO:BP fatty acid metabolic process; q_global = 0.0131) (GO:BP lipid catabolic process; q_global = 0.03), carbon metabolism (KEGG Carbon metabolism - Homo sapiens (human); q_global = 0.00679), and propanoate metabolism (KEGG Propanoate metabolism - Homo sapiens (human); q_global = 0.0229). The module therefore most plausibly represents coordinated mitochondrial substrate oxidation and conversion of carbon substrates into central metabolic intermediates. The heme-related signal from ALAD and the nucleotide-energy contribution from SLC25A4 are compatible secondary components rather than the dominant module function. The catalytic-activity term (GO:MF catalytic activity; q_global = 0.00827) is broad but supports the enzyme-rich character of the module.

**Cell composition.** The module is not composed of plasma or secreted proteins: HPA reports no secreted genes. It is instead dominated by intracellular enzymes, particularly mitochondrial proteins, with many genes enriched in liver, kidney, hepatocytes and proximal tubule cells. This pattern argues against a generic blood-protein module and favors a tissue metabolic program shared by kidney and bone marrow samples. Most genes have low immune-cell specificity, although selected genes show immune-cell enrichment and HBA1 is strongly associated with bone marrow, erythrocytes and lymphoid tissue. The presence of HBA1 may reflect erythroid material or marrow cellular composition, but it is isolated in the network and does not explain the main mitochondrial metabolic signal. Detection of many proteins in both tissues supports technical observability, while the HPA cell-type patterns suggest that shared metabolic cell populations or common mitochondrial activity could contribute to the cross-tissue module.

**GO/KEGG enrichment**: 24 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP small molecule catabolic process | 3.37e-07 | ACAA2, ACADM, ACAT1, ALDH6A1, DBT, GALM, NQO2, PCCA, PCCB, PCK2, SORD, TST |
| GO:BP organic acid catabolic process | 3.25e-06 | ACAA2, ACADM, ACAT1, ALDH6A1, DBT, PCCA, PCCB, PCK2, SORD, TST |
| GO:BP carboxylic acid catabolic process | 3.25e-06 | ACAA2, ACADM, ACAT1, ALDH6A1, DBT, PCCA, PCCB, PCK2, SORD, TST |
| GO:CC mitochondrial matrix | 8.39e-06 | ACAA2, ACADM, ACAT1, ACSF2, AK4, ALDH6A1, DBT, FH, IDH2, PCCA, PCCB, PCK2, TST |
| GO:BP carboxylic acid metabolic process | 2.58e-05 | ACAA2, ACADM, ACAT1, ACSF2, ALDH6A1, DBT, FH, IDH2, PCCA, PCCB, PCK2, SORD, TST |
| KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human) | 3.07e-05 | ACAA2, ACADM, ACAT1, ALDH6A1, DBT, PCCA, PCCB |
| GO:BP oxoacid metabolic process | 3.15e-05 | ACAA2, ACADM, ACAT1, ACSF2, ALDH6A1, DBT, FH, IDH2, PCCA, PCCB, PCK2, SORD, TST |
| GO:BP organic acid metabolic process | 3.27e-05 | ACAA2, ACADM, ACAT1, ACSF2, ALDH6A1, DBT, FH, IDH2, PCCA, PCCB, PCK2, SORD, TST |
| GO:BP small molecule metabolic process | 8.68e-05 | ACAA2, ACADM, ACAT1, ACSF2, AK4, ALDH6A1, DBT, FH, GALM, IDH2, NQO2, PCCA, PCCB, PCK2, SORD, TST |
| GO:BP monocarboxylic acid catabolic process | 0.0002 | ACAA2, ACADM, ACAT1, PCCA, PCCB, PCK2, SORD |
| KEGG Metabolic pathways - Homo sapiens (human) | 0.000375 | ACAA2, ACADM, ACAT1, AK4, ALAD, ALDH6A1, DBT, FH, GALM, IDH2, PCCA, PCCB, PCK2, SORD, TST |
| GO:BP branched-chain amino acid metabolic process | 0.000841 | ACAT1, ALDH6A1, DBT, PCCA, PCCB |
| GO:BP fatty acid catabolic process | 0.00131 | ACAA2, ACADM, ACAT1, PCCA, PCCB, PCK2 |
| GO:CC mitochondrion | 0.00151 | ACAA2, ACADM, ACAT1, ACSF2, AK4, ALDH6A1, BPHL, DBT, FH, IDH2, PCCA, PCCB, PCK2, SLC25A4, SORD, TST |
| GO:BP monocarboxylic acid metabolic process | 0.00257 | ACAA2, ACADM, ACAT1, ACSF2, IDH2, PCCA, PCCB, PCK2, SORD |

### STRING and hu.MAP

STRING supports a biologically coherent branched-chain and organic-acid catabolic core. Established high-confidence relationships include PCCA with PCCB, DBT, ALDH6A1 and ACAA2; PCCB with DBT, ALDH6A1 and ACAA2; ACAT1 with ACAA2 and ALDH6A1; and ACAA2 with ACADM. FH and IDH2 also form a connected tricarboxylic-acid-cycle pair. These relationships indicate that the module is not merely a set of statistically co-abundant genes: part of it recapitulates known metabolic pathway relationships. STRING enrichment (STRING Process Small molecule catabolic process; within-query FDR = 7.34e-08) through (STRING Keyword Transit peptide; within-query FDR = 6.52e-05) independently supports mitochondrial matrix localization, small-molecule catabolism, branched-chain amino-acid degradation and inherited metabolic disorders, but these are supplementary rather than globally corrected module-wide evidence. hu.MAP provides additional complex-level support. PCCA, PCCB and ACAA2 recur together in (hu.MAP huMAP3_13468.1), (hu.MAP huMAP3_10458.1) and (hu.MAP huMAP3_07028.1), while PCCA and ACSF2 recur in (hu.MAP huMAP3_13468.1), (hu.MAP huMAP3_08696.1) and (hu.MAP huMAP3_09437.1), and ACADM with TST recurs in (hu.MAP huMAP3_15255.1) and (hu.MAP huMAP3_03498.1). The partial overlap of module genes with larger complexes is consistent with a pathway-centered module containing several established enzyme assemblies rather than one single physical complex.

**STRING interactions (score >= 0.7)**: 16 of 253 gene pairs: ACAA2–ACADM (0.937); ACAA2–ACAT1 (0.963); ACAA2–ALDH6A1 (0.957); ACAA2–DBT (0.865); ACAA2–PCCA (0.955); ACAA2–PCCB (0.962); ACADM–ACAT1 (0.717); ACADM–PCCB (0.726); ACAT1–ALDH6A1 (0.938); ALDH6A1–DBT (0.956); ALDH6A1–PCCA (0.96); ALDH6A1–PCCB (0.967); DBT–PCCA (0.961); DBT–PCCB (0.972); FH–IDH2 (0.934); PCCA–PCCB (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Process Small molecule catabolic process (FDR = 7.34e-08, 12 genes); Component Mitochondrial matrix (FDR = 4.22e-07, 13 genes); RCTM Metabolism (FDR = 1.15e-06, 18 genes); Process Small molecule metabolic process (FDR = 2.15e-06, 17 genes); Keyword Mitochondrion (FDR = 4.17e-06, 15 genes); KEGG Metabolic pathways (FDR = 5.76e-06, 15 genes); Process Organic acid catabolic process (FDR = 9.79e-06, 9 genes); Process Carboxylic acid metabolic process (FDR = 9.79e-06, 13 genes); COMPARTMENTS Mitochondrion (FDR = 1.4e-05, 15 genes); COMPARTMENTS Mitochondrial matrix (FDR = 1.4e-05, 11 genes); TISSUES Left ventricle (FDR = 1.71e-05, 7 genes); Component Mitochondrion (FDR = 2.65e-05, 16 genes); KEGG Valine, leucine and isoleucine degradation (FDR = 2.75e-05, 6 genes); DISEASES Inherited metabolic disorder (FDR = 5.2e-05, 13 genes); Keyword Transit peptide (FDR = 6.52e-05, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (PCCA, PCCB, ACAA2, PCK2, ACSF2; 5/99); huMAP3_10458.1 (PCCA, PCCB, ACAA2; 3/16); huMAP3_15255.1 (ACADM, TST; 2/3); huMAP3_08696.1 (PCCA, ACSF2; 2/3); huMAP3_03498.1 (ACADM, TST; 2/4); huMAP3_09437.1 (PCCA, ACSF2; 2/4); huMAP3_07028.1 (PCCA, PCCB; 2/4)

### Novelty

The biochemical functions represented here are established rather than novel: many central relationships are already captured by STRING, and several partial complexes are represented in hu.MAP. Consequently, the module should not be described as a newly discovered metabolic pathway or protein complex. Its potentially novel aspect is the coordinated co-abundance of this particular gene set across bone marrow and kidney, especially the integration of propionyl-CoA, branched-chain amino-acid, fatty-acid, carbohydrate and mitochondrial energy genes with tissue-specific expression patterns. The fact sheet does not provide an external catalogue of previously reported cross-tissue co-abundance modules, so genuine module-level novelty cannot be established from database absence or presence alone. The defensible conclusion is that the module is a potentially distinctive cross-tissue expression pattern built largely from known metabolic biology.

**Hypothesis.** Hypothesis: a shared mitochondrial substrate-oxidation state links bone marrow and kidney in these samples. Coordinated abundance of propionyl-CoA carboxylase subunits, branched-chain amino-acid catabolic enzymes, fatty-acid oxidation enzymes, tricarboxylic-acid-cycle enzymes and mitochondrial transport or redox components may support handling of amino-acid-, fatty-acid- and carbohydrate-derived carbon. In kidney, this could reflect proximal-tubule metabolic activity; in bone marrow, it could reflect metabolically active stromal or developing hematopoietic populations, with HBA1 indicating an additional erythroid contribution. This is a mechanistic interpretation of co-abundance, not proof that the proteins physically act together in every cell or that the module causes a disease phenotype.

### Important genes

#### PCCA

- **Related proteins** (co-abundance neighbors): ALAD (0.85), TTC38 (0.84); STRING partners: ACAA2 (0.955), ALDH6A1 (0.96), DBT (0.961), PCCB (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10458.1, huMAP3_08696.1, huMAP3_09437.1, huMAP3_07028.1
- **Function (MyGene.info)**: propionyl-CoA carboxylase subunit alpha. The protein encoded by this gene is the alpha subunit of the heterodimeric mitochondrial enzyme Propionyl-CoA carboxylase. PCCA encodes the biotin-binding region of this enzyme. Mutations in either PCCA or PCCB (encoding the beta subunit) lead to an enzyme deficiency resulting in propionic acidemia. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by…
- **Diseases (Open Targets)**: propionic acidemia (0.853); hereditary disease (0.487); dilated cardiomyopathy (0.370); neurodegenerative disease (0.357); pontocerebellar hypoplasia type 2D (0.340)
- **Europe PMC papers**: 2633
- **Why important**: PCCA is one of the most structurally supported genes in the module. It forms the propionyl-CoA carboxylase alpha subunit, is present in every globally significant GO/KEGG term listed for the module, connects to PCCB and several branched-chain and fatty-acid catabolic proteins in STRING, and recurs across multiple hu.MAP complexes (hu.MAP huMAP3_13468.1), (hu.MAP huMAP3_10458.1), (hu.MAP huMAP3_08696.1), (hu.MAP huMAP3_09437.1) and (hu.MAP huMAP3_07028.1). Its disease association with propionic acidemia gives the module a direct metabolic-disorder anchor, and its substantial literature supports an established biological role.
- **Conclusion**: Established evidence identifies PCCA as a central enzymatic component of propionyl-CoA and short-chain organic-acid metabolism. Its network and complex relationships make it a strong marker of the module's core mitochondrial catabolic program. The cross-tissue co-abundance may indicate coordinated regulation of this pathway, but it does not establish altered propionyl-CoA flux.

#### PCCB

- **Related proteins** (co-abundance neighbors): TTC38 (0.85); STRING partners: ACAA2 (0.962), ACADM (0.726), ALDH6A1 (0.967), DBT (0.972), PCCA (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10458.1, huMAP3_07028.1
- **Function (MyGene.info)**: propionyl-CoA carboxylase subunit beta. The protein encoded by this gene is a subunit of the propionyl-CoA carboxylase (PCC) enzyme, which is involved in the catabolism of propionyl-CoA. PCC is a mitochondrial enzyme that probably acts as a dodecamer of six alpha subunits and six beta subunits. This gene encodes the beta subunit of PCC. Defects in this gene are a cause of propionic acidemia type II (PA-2). Multiple transcript variants e…
- **Diseases (Open Targets)**: propionic acidemia (0.861); hereditary disease (0.517); hypertensive disorder (0.453); coronary artery disorder (0.438); coronary atherosclerosis (0.428)
- **Europe PMC papers**: 1404
- **Why important**: PCCB is the partner subunit of propionyl-CoA carboxylase and is present across the globally significant metabolic terms, including branched-chain amino-acid, short-chain fatty-acid and propanoate metabolism. It has strong STRING relationships with PCCA, DBT, ALDH6A1 and ACAA2 and appears in hu.MAP complexes (hu.MAP huMAP3_13468.1), (hu.MAP huMAP3_10458.1) and (hu.MAP huMAP3_07028.1). Its association with propionic acidemia type two provides a well-established disease connection.
- **Conclusion**: Established evidence supports PCCB as a core component of the module's organic-acid and branched-chain substrate metabolism. Its close partnership with PCCA strengthens the interpretation that the module captures a coordinated mitochondrial pathway rather than unrelated metabolic genes. A specific disease mechanism in either tissue remains a hypothesis.

#### ACAT1

- **Related proteins** (co-abundance neighbors): ACAA2 (0.89), ACADM (0.84), NQO2 (0.83); STRING partners: ACAA2 (0.963), ACADM (0.717), ALDH6A1 (0.938)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA acetyltransferase 1. This gene encodes a mitochondrially localized enzyme that catalyzes the reversible formation of acetoacetyl-CoA from two molecules of acetyl-CoA. Defects in this gene are associated with 3-ketothiolase deficiency, an inborn error of isoleucine catabolism characterized by urinary excretion of 2-methyl-3-hydroxybutyric acid, 2-methylacetoacetic acid, tiglylglycine, and butanone. [provided by RefSeq,…
- **Diseases (Open Targets)**: beta-ketothiolase deficiency (0.817); hereditary disease (0.470); Abnormality of the skeletal system (0.239); neoplasm (0.115); nonpapillary renal cell carcinoma (0.105)
- **Europe PMC papers**: 4147
- **Why important**: ACAT1 is among the most functionally connected genes in the module and participates in nearly all of the principal metabolic themes, including fatty-acid oxidation, branched-chain amino-acid degradation, organic-acid catabolism and mitochondrial localization (GO:BP small molecule catabolic process; q_global = 3.37e-07) through (GO:BP lipid catabolic process; q_global = 0.03) where listed. It has established STRING relationships with ACAA2, ACADM and ALDH6A1. Its known role in reversible acetoacetyl-CoA formation and its association with beta-ketothiolase deficiency provide strong biochemical and disease evidence, supported by extensive literature.
- **Conclusion**: Established evidence places ACAT1 at the intersection of ketone-related, fatty-acid and isoleucine catabolism. Its co-abundance with multiple mitochondrial catabolic enzymes is consistent with coordinated acetyl-CoA handling. The module does not by itself show whether ketogenesis, beta-oxidation or amino-acid oxidation is increased.

#### ALDH6A1

- **Related proteins** (co-abundance neighbors): TMT1A (0.93), NQO2 (0.83), GALM (0.82), TTC38 (0.81); STRING partners: ACAA2 (0.957), ACAT1 (0.938), DBT (0.956), PCCA (0.96), PCCB (0.967)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 6 family member A1. This gene encodes a member of the aldehyde dehydrogenase protein family. The encoded protein is a mitochondrial methylmalonate semialdehyde dehydrogenase that plays a role in the valine and pyrimidine catabolic pathways. This protein catalyzes the irreversible oxidative decarboxylation of malonate and methylmalonate semialdehydes to acetyl- and propionyl-CoA. Methylmalonate semialdehyde dehydrogen…
- **Diseases (Open Targets)**: methylmalonate semialdehyde dehydrogenase deficiency (0.706); hereditary disease (0.413); alcohol drinking (0.158); atrial fibrillation (0.089); gastric cancer (0.076)
- **Europe PMC papers**: 1031
- **Why important**: ALDH6A1 occupies a connective position linking ACAA2, ACAT1, DBT, PCCA and PCCB in STRING. It is present in the major globally significant catabolic and mitochondrial terms, including branched-chain amino-acid and propanoate metabolism. HPA places it in kidney and liver-related expression patterns and in proximal tubule and hepatocyte cell types. Its established function in methylmalonate semialdehyde oxidation and its association with methylmalonate semialdehyde dehydrogenase deficiency make it an informative bridge between amino-acid and organic-acid metabolism.
- **Conclusion**: Established evidence supports ALDH6A1 as a mitochondrial aldehyde-oxidation enzyme that helps connect branched-chain and propionyl-related catabolism. Its network position makes it a plausible integrator of the module. Any claim that it drives the shared bone-marrow and kidney phenotype would remain speculative.

#### ACAA2

- **Related proteins** (co-abundance neighbors): ACAT1 (0.89), NQO2 (0.88), BPHL (0.85), IDH2 (0.82), FH (0.82), ACADM (0.82); STRING partners: ACADM (0.937), ACAT1 (0.963), ALDH6A1 (0.957), DBT (0.865), PCCA (0.955), PCCB (0.962)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10458.1
- **Function (MyGene.info)**: acetyl-CoA acyltransferase 2. The encoded protein catalyzes the last step of the mitochondrial fatty acid beta-oxidation spiral. Unlike most mitochondrial matrix proteins, it contains a non-cleavable amino-terminal targeting signal. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: bone remodeling disease (0.270); sinusitis (0.260); refractive error (0.190); kidney disorder (0.151); myopia (0.141)
- **Europe PMC papers**: 3056
- **Why important**: ACAA2 has a prominent position in the module and connects to ACADM, ACAT1, ALDH6A1, DBT, PCCA and PCCB. It is represented across the principal globally significant terms for small-molecule, organic-acid and fatty-acid catabolism and mitochondrial matrix localization. It is also present in hu.MAP complexes (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10458.1). Its established role as the terminal enzyme of mitochondrial fatty-acid beta-oxidation, together with its kidney and metabolic disease associations, makes it a strong indicator of mitochondrial lipid oxidation.
- **Conclusion**: Established evidence identifies ACAA2 as a central fatty-acid beta-oxidation component and a connector between lipid and organic-acid catabolism. Its co-abundance supports a broad mitochondrial oxidation program. The data do not demonstrate that fatty acids are the dominant substrate in both tissues, because the module also contains substantial amino-acid and carbohydrate metabolism signals.

#### DBT

- **Related proteins** (co-abundance neighbors): GALM (0.84); STRING partners: ACAA2 (0.865), ALDH6A1 (0.956), PCCA (0.961), PCCB (0.972)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dihydrolipoamide branched chain transacylase E2. The branched-chain alpha-keto acid dehydrogenase complex (BCKD) is an inner-mitochondrial enzyme complex involved in the breakdown of the branched-chain amino acids isoleucine, leucine, and valine. The BCKD complex is thought to be composed of a core of 24 transacylase (E2) subunits, and associated decarboxylase (E1), dehydrogenase (E3), and regulatory subunits. This gene encodes the transacylase …
- **Diseases (Open Targets)**: maple syrup urine disease (0.710); maple syrup urine disease type 1A (0.695); maple syrup urine disease type 2 (0.659); intermittent maple syrup urine disease (0.370); classic maple syrup urine disease (0.370)
- **Europe PMC papers**: 15522
- **Why important**: DBT is a core enzyme of the branched-chain alpha-keto-acid dehydrogenase complex and is repeatedly represented in the globally significant branched-chain and organic-acid terms. STRING links DBT to ACAA2, ALDH6A1, PCCA and PCCB, placing it within the module's established catabolic core. Its association with maple syrup urine disease and its extensive literature provide strong disease and biochemical support.
- **Conclusion**: Established evidence supports DBT as a key entry point for branched-chain amino-acid oxidation and a major reason the module has a coherent amino-acid catabolic interpretation. Its coordinated abundance with propionyl-CoA and fatty-acid enzymes suggests shared regulation of mitochondrial carbon disposal, but does not prove direct physical interaction among all module members.

## Module 7

**Tissue pair**: bone_marrow and kidney  
**Genes (38)**: ACLY, ARHGEF2, ATP2A2, MTHFD1, COPB1, CYFIP1, DNM1L, DYNC1H1, EIF3C, EPS15L1, FASN, FLII, GANAB, HNRNPK, HPRT1, HK1, IQGAP1, RABIF, NCKAP1, PDCD6IP, CAD, POLR2B, SCFD1, SF3B3, SMIM40, AARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, VARS1, TNPO1, SNRNP200, EFTUD2, USP5, USO1, XPO1

### Function

The strongest interpretation is a conserved core of cytosolic protein production and translational quality control. The primary evidence is the coordinated presence of aminoacyl-tRNA ligases and tRNA aminoacylation genes in (GO:MF aminoacyl-tRNA ligase activity; q_global = 0.000519), (GO:BP tRNA aminoacylation for protein translation; q_global = 0.000519), (GO:BP amino acid activation; q_global = 0.00086), (GO:BP tRNA aminoacylation; q_global = 0.00086), (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 0.00086), (GO:MF aminoacyl-tRNA deacylase activity; q_global = 0.00704), (GO:BP aminoacyl-tRNA metabolism involved in translational fidelity; q_global = 0.00704), (GO:BP regulation of translational fidelity; q_global = 0.0203), and (GO:MF catalytic activity, acting on a tRNA; q_global = 0.0422). The aminoacyl-tRNA synthetase multienzyme complex is supported by (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.000563). The module also contains a broader cellular-support layer involving GTPase binding (GO:MF GTPase binding; q_global = 0.00305), amino-acid metabolism and ligase activity (GO:MF ligase activity; q_global = 0.00357) and (GO:BP amino acid metabolic process; q_global = 0.0121), RNA processing, vesicle trafficking, cytoskeletal regulation, lipid metabolism, and intracellular transport. Thus, the module is best viewed as a protein-biosynthesis and proteostasis-associated program rather than as a tissue-specific pathway. The GO and KEGG evidence does not establish that every module gene participates directly in aminoacylation; several genes probably reflect coupled translation, trafficking, RNA-processing, metabolic, or structural activity.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the HPA summary identifies only a small secreted component, while the listed proteins are mainly intracellular and localized to the cytosol, nucleus, Golgi, vesicles, or other intracellular compartments. Most genes have low tissue specificity, and the module is detected at the protein level in both bone marrow and kidney for nearly all genes with available data. The overall blood-cell specificity is low, with only limited cell-type enrichment involving neutrophils, monocytes, myeloid dendritic cells, erythrocyte progenitors, and other cell types. The broad expression pattern and strong representation of translation, metabolism, RNA processing, and transport genes therefore suggest a housekeeping or shared-cellular-state component rather than a module uniquely defining bone marrow or kidney. The tissue and cell-type enrichments in muscle, liver, nervous system, reproductive cells, and selected immune populations further argue against a simple blood-contamination explanation.

**GO/KEGG enrichment**: 14 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF aminoacyl-tRNA ligase activity | 0.000519 | AARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, VARS1 |
| GO:BP tRNA aminoacylation for protein translation | 0.000519 | AARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, VARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 0.000519 | AARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, VARS1 |
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 0.000563 | EPRS1, IARS1, LARS1, MARS1, QARS1 |
| GO:BP amino acid activation | 0.00086 | AARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, VARS1 |
| GO:BP tRNA aminoacylation | 0.00086 | AARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, VARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 0.00086 | AARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, VARS1 |
| GO:MF GTPase binding | 0.00305 | ARHGEF2, CYFIP1, DNM1L, EPRS1, IARS1, IQGAP1, NCKAP1, TNPO1, XPO1 |
| GO:MF ligase activity | 0.00357 | AARS1, CAD, EPRS1, IARS1, LARS1, MARS1, MTHFD1, QARS1, VARS1 |
| GO:MF aminoacyl-tRNA deacylase activity | 0.00704 | AARS1, IARS1, LARS1, VARS1 |
| GO:BP aminoacyl-tRNA metabolism involved in translational fidelity | 0.00704 | AARS1, IARS1, LARS1, VARS1 |
| GO:BP amino acid metabolic process | 0.0121 | AARS1, CAD, EPRS1, IARS1, LARS1, MARS1, MTHFD1, QARS1, VARS1 |
| GO:BP regulation of translational fidelity | 0.0203 | AARS1, IARS1, LARS1, VARS1 |
| GO:MF catalytic activity, acting on a tRNA | 0.0422 | AARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, VARS1 |

### STRING and hu.MAP

STRING provides established support for a coherent aminoacyl-tRNA synthetase network: AARS1, EPRS1, IARS1, LARS1, MARS1, QARS1, and VARS1 are densely interconnected, and the same genes recur in the supplementary aminoacylation and synthetase-complex terms (STRING COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex; within-query FDR = 5.19e-05), (STRING RCTM Cytosolic tRNA aminoacylation; within-query FDR = 5.77e-05), (STRING KEGG Aminoacyl-tRNA biosynthesis; within-query FDR = 0.00017), (STRING InterPro Aminoacyl-tRNA synthetase, class I, conserved site; within-query FDR = 0.00017), (STRING Keyword Aminoacyl-tRNA synthetase; within-query FDR = 0.00018), (STRING Function aminoacyl-tRNA ligase activity; within-query FDR = 0.0006), and (STRING Component aminoacyl-tRNA synthetase multienzyme complex; within-query FDR = 0.001). STRING also supports separate subnetworks involving ACLY with FASN, COPB1 with USO1 and SCFD1, CYFIP1 with NCKAP1, EFTUD2 with SF3B3 and SNRNP200, and TNPO1 with XPO1. These relationships indicate that the module combines a known multisynthetase-complex core with established RNA-splicing, vesicle-trafficking, cytoskeletal, lipid-metabolic, and nuclear-transport systems. hu.MAP independently confirms the multisynthetase complex in (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), with EPRS1, IARS1, QARS1, MARS1, and LARS1 recurring together. Additional hu.MAP complexes support spliceosomal organization through SNRNP200, EFTUD2, and SF3B3, actin or WAVE-associated organization through CYFIP1 and NCKAP1, metabolic association through CAD and FASN, and transport or membrane-associated assemblies involving XPO1, TNPO1, ATP2A2, USO1, and EPS15L1. Consequently, much of the module's molecular architecture is already known, although co-abundance links between these systems need not represent direct physical interactions.

**STRING interactions (score >= 0.7)**: 36 of 703 gene pairs: AARS1–EPRS1 (0.976); AARS1–IARS1 (0.98); AARS1–LARS1 (0.968); AARS1–MARS1 (0.913); AARS1–QARS1 (0.964); AARS1–VARS1 (0.938); ACLY–FASN (0.994); ACLY–MTHFD1 (0.723); ARHGEF2–RABIF (0.792); COPB1–SCFD1 (0.729); COPB1–USO1 (0.869); CYFIP1–NCKAP1 (0.999); EFTUD2–EPRS1 (0.744); EFTUD2–SF3B3 (0.999); EFTUD2–SNRNP200 (0.999); EIF3C–EPRS1 (0.755); EPRS1–IARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–MARS1 (0.999); EPRS1–QARS1 (0.999); EPRS1–VARS1 (0.97); HNRNPK–SF3B3 (0.971); IARS1–LARS1 (0.999); IARS1–MARS1 (0.999); IARS1–QARS1 (0.999); IARS1–VARS1 (0.9); LARS1–MARS1 (0.999); LARS1–QARS1 (0.999); LARS1–VARS1 (0.968); MARS1–QARS1 (0.999); MARS1–VARS1 (0.902); POLR2B–VARS1 (0.843); QARS1–VARS1 (0.91); SCFD1–USO1 (0.97); SF3B3–SNRNP200 (0.999); TNPO1–XPO1 (0.868)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Liver (FDR = 2.77e-07, 28 genes); TISSUES Digestive gland (FDR = 1e-06, 30 genes); COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex (FDR = 5.19e-05, 6 genes); RCTM Cytosolic tRNA aminoacylation (FDR = 5.77e-05, 7 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 0.00017, 7 genes); InterPro Aminoacyl-tRNA synthetase, class I, conserved site (FDR = 0.00017, 6 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 0.00018, 7 genes); Keyword Ligase (FDR = 0.00018, 9 genes); Keyword Protein biosynthesis (FDR = 0.00041, 8 genes); Function aminoacyl-tRNA ligase activity (FDR = 0.0006, 7 genes); Component aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.001, 5 genes); TISSUES Nervous system (FDR = 0.001, 32 genes); Function Ligase activity (FDR = 0.0011, 9 genes); TISSUES Viscus (FDR = 0.0012, 32 genes); TISSUES Brain (FDR = 0.0015, 31 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, IARS1, QARS1, MARS1, LARS1; 5/14); huMAP3_13688.1 (EPRS1, IARS1, QARS1, MARS1, LARS1; 5/14); huMAP3_09592.1 (XPO1, ATP2A2, TNPO1; 3/95); huMAP3_08980.1 (SNRNP200, EFTUD2, SF3B3; 3/97); huMAP3_10103.1 (CAD, FASN; 2/4); huMAP3_00960.1 (SNRNP200, EFTUD2; 2/8); huMAP3_07622.1 (SNRNP200, EFTUD2; 2/9); huMAP3_02474.1 (CYFIP1, NCKAP1; 2/13); huMAP3_07170.1 (XPO1, ATP2A2; 2/14); huMAP3_09598.1 (CYFIP1, NCKAP1; 2/23); huMAP3_13345.1 (CYFIP1, NCKAP1; 2/35); huMAP3_08501.1 (SNRNP200, EFTUD2; 2/47); huMAP3_09504.1 (SNRNP200, EFTUD2; 2/51); huMAP3_09945.1 (SNRNP200, EFTUD2; 2/61); huMAP3_06247.1 (ATP2A2, TNPO1; 2/65); huMAP3_12394.1 (USO1, EPS15L1; 2/98)

### Novelty

The module should not be claimed as a newly discovered aminoacyl-tRNA synthetase complex or as a new protein complex. The central synthetase relationships are already supported by STRING and hu.MAP, and the module also contains several established cellular assemblies. A potentially novel aspect is the reproducible co-abundance of this known translational core with trafficking, RNA-processing, cytoskeletal, metabolic, and calcium-handling genes across bone marrow and kidney. However, the fact sheet does not provide an external comparison with previously reported tissue co-abundance modules, so the novelty of that cross-tissue co-regulation remains unproven. Absence of a particular edge from STRING or hu.MAP would not establish novelty, because those resources describe physical or curated functional relationships rather than every abundance-level association.

**Hypothesis.** Hypothesis: the module represents a shared intracellular resource-allocation program active in cells that must maintain protein synthesis while coordinating RNA maturation, organelle transport, cytoskeletal organization, lipid and one-carbon metabolism, and membrane or calcium homeostasis. The aminoacyl-tRNA synthetase core may provide the primary signal, while EPRS1, NCKAP1, COPB1, MTHFD1, and related genes connect translational demand to cytoskeletal, trafficking, and biosynthetic support. In bone marrow, this could accompany proliferative or differentiating hematopoietic cells; in kidney, it could reflect broadly expressed epithelial or stromal cellular activity. This is a mechanistic model generated from co-abundance and annotation convergence, not proof of direct regulation or physical coupling among all module members.

### Important genes

#### EPRS1

- **Related proteins** (co-abundance neighbors): AARS1 (0.93), EFTUD2 (0.90), IARS1 (0.89), ATP2A2 (0.88), NCKAP1 (0.88), XPO1 (0.87), DYNC1H1 (0.87), MARS1 (0.86), CAD (0.86), COPB1 (0.86), LARS1 (0.86), FASN (0.86), MTHFD1 (0.85), EIF3C (0.81), SF3B3 (0.81); STRING partners: AARS1 (0.976), EFTUD2 (0.744), EIF3C (0.755), IARS1 (0.999), LARS1 (0.999), MARS1 (0.999), QARS1 (0.999), VARS1 (0.97)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is one of the most connected genes in the module and is linked to the core synthetase genes by STRING. It is present in nearly all of the primary aminoacylation-related terms, including the aminoacyl-tRNA synthetase multienzyme complex (GO:MF aminoacyl-tRNA ligase activity; q_global = 0.000519), (GO:BP tRNA aminoacylation for protein translation; q_global = 0.000519), (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.000563), (GO:BP amino acid activation; q_global = 0.00086), (GO:BP tRNA aminoacylation; q_global = 0.00086), (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 0.00086), (GO:MF ligase activity; q_global = 0.00357), (GO:BP amino acid metabolic process; q_global = 0.0121), and (GO:MF catalytic activity, acting on a tRNA; q_global = 0.0422). It is also a member of the multisynthetase assemblies (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), and its broad literature and disease annotation make it a well-supported anchor rather than an uncharacterized peripheral gene.
- **Conclusion**: Established evidence identifies EPRS1 as a central translational and multisynthetase-complex component. It is therefore a strong marker of the module's core function. Its high connectivity does not by itself show that EPRS1 organizes the entire cross-tissue module; that broader coordinating role remains a hypothesis.

#### IARS1

- **Related proteins** (co-abundance neighbors): EPRS1 (0.89), DYNC1H1 (0.86), XPO1 (0.85), VARS1 (0.84), ACLY (0.84), EFTUD2 (0.84), SF3B3 (0.84), EIF3C (0.84), FASN (0.82), RABIF (0.82), QARS1 (0.81), COPB1 (0.81), AARS1 (0.80); STRING partners: AARS1 (0.98), EPRS1 (0.999), LARS1 (0.999), MARS1 (0.999), QARS1 (0.999), VARS1 (0.9)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Isoleucine-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family and has been identified as a …
- **Diseases (Open Targets)**: growth retardation, intellectual developmental disorder, hypotonia, and hepatopathy (0.733); Abnormality of the skeletal system (0.332); microcephaly (0.289); Global developmental delay (0.289); Hallux valgus (0.184)
- **Europe PMC papers**: 184
- **Why important**: IARS1 combines high network connectivity with direct membership in the primary aminoacylation, translational-fidelity, and synthetase-complex terms (GO:MF aminoacyl-tRNA ligase activity; q_global = 0.000519) through (GO:MF catalytic activity, acting on a tRNA; q_global = 0.0422) where listed. It is repeatedly connected to the other synthetases in STRING and occurs in (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Its annotation as an isoleucyl-tRNA synthetase gives the translational interpretation a direct enzymatic basis, while its disease associations and literature support biological importance beyond a purely statistical module membership.
- **Conclusion**: Established evidence supports IARS1 as a core enzyme for accurate tRNA charging and translational fidelity within this module. The shared abundance of IARS1 with trafficking, metabolic, and RNA-processing genes suggests coordinated cellular demand, but does not establish that IARS1 directly regulates those systems.

#### NCKAP1

- **Related proteins** (co-abundance neighbors): COPB1 (0.89), EPRS1 (0.88), MARS1 (0.87), EIF3C (0.87), AARS1 (0.87), ATP2A2 (0.86), PDCD6IP (0.85), MTHFD1 (0.84), DYNC1H1 (0.84), VARS1 (0.83), CYFIP1 (0.82), ARHGEF2 (0.82), USP5 (0.81), USO1 (0.80), HK1 (0.80), ACLY (0.80), EPS15L1 (0.80); STRING partners: CYFIP1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_02474.1, huMAP3_09598.1, huMAP3_13345.1
- **Function (MyGene.info)**: NCK associated protein 1. Contributes to small GTPase binding activity. Involved in Rac protein signal transduction; positive regulation of Arp2/3 complex-mediated actin nucleation; and positive regulation of lamellipodium assembly. Located in extracellular exosome and focal adhesion. Part of SCAR complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.528); neurodevelopmental disorder (0.471); hereditary disease (0.451); complex neurodevelopmental disorder (0.443); Intellectual disability (0.437)
- **Europe PMC papers**: 1019
- **Why important**: NCKAP1 has among the strongest network positions and connects the translational core to the cytoskeletal branch. It is represented in the GTPase-binding term (GO:MF GTPase binding; q_global = 0.00305), is a known regulator of Rac signaling, Arp two slash three complex-mediated actin nucleation, lamellipodium assembly, and cell migration, and forms a STRING-supported pair with CYFIP1. Its membership in several hu.MAP assemblies (hu.MAP huMAP3_02474.1), (hu.MAP huMAP3_09598.1), and (hu.MAP huMAP3_13345.1) supports a recognized actin or WAVE-associated context. It is broadly expressed and is not detected as immune-cell-specific by HPA, making it a plausible general cellular bridge rather than a dedicated blood-cell marker.
- **Conclusion**: Established evidence supports NCKAP1 as a cytoskeletal and small-GTPase-associated connector within the module. Its position makes it a candidate link between protein-production demand and cell morphology or transport. Whether that link explains the conserved bone-marrow and kidney co-abundance pattern is a hypothesis.

#### MTHFD1

- **Related proteins** (co-abundance neighbors): VARS1 (0.89), ATP2A2 (0.88), DYNC1H1 (0.87), AARS1 (0.86), PDCD6IP (0.86), FASN (0.86), COPB1 (0.85), EPRS1 (0.85), NCKAP1 (0.84), EIF3C (0.83); STRING partners: ACLY (0.723)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methylenetetrahydrofolate dehydrogenase, cyclohydrolase and formyltetrahydrofolate synthetase 1. This gene encodes a protein that possesses three distinct enzymatic activities, 5,10-methylenetetrahydrofolate dehydrogenase, 5,10-methenyltetrahydrofolate cyclohydrolase and 10-formyltetrahydrofolate synthetase. Each of these activities catalyzes one of three sequential reactions in the interconversion of 1-carbon derivatives of tetrahydrofolate, which are substrates for methionine, thymidylate, …
- **Diseases (Open Targets)**: combined immunodeficiency and megaloblastic anemia with or without hyperhomocysteinemia (0.773); severe combined immunodeficiency (0.473); neural tube defects, folate-sensitive (0.414); isolated spina bifida (0.376); atrial fibrillation (0.332)
- **Europe PMC papers**: 1939
- **Why important**: MTHFD1 links the module to one-carbon and nucleotide-related metabolism and appears in the primary ligase and amino-acid-metabolism terms (GO:MF ligase activity; q_global = 0.00357) and (GO:BP amino acid metabolic process; q_global = 0.0121). Its network connections place it near the synthetase core, lipid metabolism, calcium handling, and transport-related genes. HPA reports enrichment in liver and cell-type enhancement in adipocytes, cardiomyocytes, epicardial cells, hepatocytes, and erythrocyte progenitors, with protein detection in both relevant tissues. Its disease associations include combined immunodeficiency and megaloblastic anemia, which are biologically relevant to a bone-marrow-associated module.
- **Conclusion**: Established evidence supports MTHFD1 as a metabolic support gene that can supply biosynthetic capacity for proliferating or protein-producing cells. Its association with the translational core is consistent with coordinated metabolic demand, but the data do not demonstrate that MTHFD1 drives the module.

#### COPB1

- **Related proteins** (co-abundance neighbors): ACLY (0.92), AARS1 (0.90), ATP2A2 (0.89), NCKAP1 (0.89), VARS1 (0.88), DYNC1H1 (0.87), EPRS1 (0.86), MTHFD1 (0.85), FASN (0.84), PDCD6IP (0.84), HK1 (0.83), FLII (0.82), EIF3C (0.81), MARS1 (0.81), IARS1 (0.81), LARS1 (0.80); STRING partners: SCFD1 (0.729), USO1 (0.869)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus, Vesicles, Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coat protein complex I subunit beta 1. This gene encodes a protein subunit of the coatomer complex associated with non-clathrin coated vesicles. The coatomer complex, also known as the coat protein complex 1, forms in the cytoplasm and is recruited to the Golgi by activated guanosine triphosphatases. Once at the Golgi membrane, the coatomer complex may assist in the movement of protein and lipid components back to the endoplasmic retic…
- **Diseases (Open Targets)**: Baralle-Macken syndrome (0.598); Alzheimer disease (0.463); Parkinson disease (0.462); neurodegenerative disease (0.462); lysosomal storage disease (0.462)
- **Europe PMC papers**: 565
- **Why important**: COPB1 is highly connected in the co-abundance network and links the module to Golgi and vesicle biology. Its established function is as a coatomer subunit involved in intracellular, retrograde, and ER-to-Golgi transport. STRING supports relationships with USO1 and SCFD1, while the module network connects COPB1 to several synthetases, metabolic genes, ATP2A2, and NCKAP1. HPA shows low tissue and cell-type specificity, with protein detection in both bone marrow and kidney. It is not itself part of a primary GO or KEGG term, which makes it useful as a non-enrichment-based network connector.
- **Conclusion**: Established evidence supports COPB1 as a trafficking component that may connect biosynthetic activity to intracellular transport. Its network position supports a bridging role in the module, but co-abundance does not prove that COPB1 physically associates with the aminoacyl-tRNA synthetase complex.

## Module 8

**Tissue pair**: bone_marrow and kidney  
**Genes (46)**: AKAP8, PRMT5, AP1M1, BAX, BRD2, BYSL, CNOT1, COPG2, CSTF3, POLD3, POLE, ELOC, FDFT1, FEN1, GEMIN2, GSKIP, HAUS5, HEATR1, HECTD3, IPO4, MCM2, MCM5, MED18, MSH6, MTA2, MYO9B, DR1, EMG1, PPAT, UQCRC2, RRM1, ELAC2, DIS3, PDCD11, SRP68, SRP72, SYMPK, SARS2, TARBP1, THOP1, TIPRL, TLK2, TRIM33, UNC45A, UTP4, YTHDF2

### Function

The module is best interpreted as a conserved nuclear gene-expression program coupling DNA replication and repair with broader nucleic-acid metabolism. The primary evidence is KEGG DNA replication (KEGG DNA replication - Homo sapiens (human); q_global = 0.0457), supported by FEN1, MCM2, MCM5, POLD3 and POLE, together with the globally significant GO term nucleic acid metabolic process (GO:BP nucleic acid metabolic process; q_global = 0.0486). STRING results independently reinforce DNA replication and nuclear localization (5 supplementary STRING terms; within-query FDR 0.0108–0.0339). The module also includes genes involved in ribosome biogenesis, RNA processing, transcriptional regulation, RNA degradation, chromatin regulation and nucleotide production. The most defensible interpretation is therefore a proliferative or progenitor-cell nuclear maintenance program rather than a single narrowly defined biochemical pathway. No GO/KEGG term passed within-module correction, although the two terms above passed the specified global correction; this does not invalidate the module.

**Cell composition.** The module contains no secreted genes according to HPA, so it is not a plasma-protein or secreted-protein module. Most genes have low tissue specificity and low immune-cell specificity, arguing against a simple blood-cell marker or immune-cell contamination explanation. Several genes are tissue-enhanced in bone marrow or lymphoid tissue, and many show cell-type-enhanced expression in erythrocyte progenitors or other progenitor and germ-cell populations. Protein detection is common in both bone marrow and kidney. The shared signal may therefore reflect broadly expressed nuclear housekeeping and proliferation-related machinery, with a possible contribution from proliferating progenitor cells present in both tissues. HPA does not support interpreting the module as a secreted or plasma-protein program.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG DNA replication - Homo sapiens (human) | 0.0457 | FEN1, MCM2, MCM5, POLD3, POLE |
| GO:BP nucleic acid metabolic process | 0.0486 | BAX, BRD2, BYSL, CNOT1, CSTF3, DIS3, DR1, ELAC2, ELOC, EMG1, FEN1, GEMIN2, HEATR1, MCM2, MCM5, MED18, MSH6, MTA2, PDCD11, POLD3, POLE, PRMT5, RRM1, SARS2, SYMPK, TARBP1, TRIM33, UTP4, YTHDF2 |

### STRING and hu.MAP

STRING contains established relationships within the DNA-replication component, including MCM2–MCM5, MCM2–POLE, MCM5–POLE, FEN1 links to MCM proteins, POLE, POLD3 and MSH6, and RRM1 links to MCM proteins (STRING Process Nucleic acid metabolic process; within-query FDR = 0.0108) (STRING KEGG DNA replication; within-query FDR = 0.0218) (STRING Keyword DNA replication; within-query FDR = 0.0339). It also contains coherent nucleolar and ribosome-biogenesis relationships among BYSL, EMG1, HEATR1, PDCD11 and UTP4, as well as RNA-processing pairs such as CSTF3–SYMPK and SRP68–SRP72. hu.MAP independently places MCM2 and MCM5 in replication-related complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1), CSTF3 and SYMPK in polyadenylation complexes (hu.MAP huMAP3_09096.1) (hu.MAP huMAP3_11757.1), PRMT5 and GEMIN2 in spliceosomal complexes (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_08980.1), and TLK2 with IPO4 in chromatin-assembly-related complexes (hu.MAP huMAP3_09289.1) (hu.MAP huMAP3_12711.1). These results validate local components and known relationships, but the complexes generally contain only subsets of the module and therefore do not show that the entire module is one physical complex.

**STRING interactions (score >= 0.7)**: 32 of 1035 gene pairs: BYSL–EMG1 (0.999); BYSL–HEATR1 (0.998); BYSL–PDCD11 (0.998); BYSL–UTP4 (0.999); CNOT1–YTHDF2 (0.986); CSTF3–SYMPK (0.999); ELOC–MCM2 (0.803); ELOC–MCM5 (0.811); ELOC–POLE (0.803); EMG1–HEATR1 (0.998); EMG1–PDCD11 (0.993); EMG1–UTP4 (0.998); FEN1–MCM2 (0.912); FEN1–MCM5 (0.942); FEN1–MSH6 (0.95); FEN1–POLD3 (0.983); FEN1–POLE (0.906); FEN1–RRM1 (0.766); HEATR1–PDCD11 (0.999); HEATR1–UTP4 (0.999); MCM2–MCM5 (0.999); MCM2–POLE (0.997); MCM2–RRM1 (0.914); MCM5–MSH6 (0.749); MCM5–POLE (0.997); MCM5–RRM1 (0.957); MSH6–POLE (0.957); PDCD11–TARBP1 (0.72); PDCD11–UTP4 (0.999); POLD3–POLE (0.963); SRP68–SRP72 (0.999); TARBP1–UTP4 (0.726)
**STRING functional enrichment (supplementary, within-query FDR)**: Process Nucleic acid metabolic process (FDR = 0.0108, 26 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0195, 22 genes); KEGG DNA replication (FDR = 0.0218, 5 genes); Keyword Nucleus (FDR = 0.0273, 31 genes); Keyword DNA replication (FDR = 0.0339, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05529.1 (MCM5, MCM2; 2/6); huMAP3_09289.1 (TLK2, IPO4; 2/14); huMAP3_14758.1 (MCM5, MCM2; 2/14); huMAP3_09096.1 (CSTF3, SYMPK; 2/15); huMAP3_08554.1 (MCM5, MCM2; 2/15); huMAP3_11832.1 (MCM5, MCM2; 2/15); huMAP3_11757.1 (CSTF3, SYMPK; 2/16); huMAP3_14135.1 (TARBP1, IPO4; 2/17); huMAP3_12180.1 (MCM5, MCM2; 2/17); huMAP3_14456.1 (TARBP1, IPO4; 2/18); huMAP3_10747.1 (MCM2, IPO4; 2/25); huMAP3_09042.1 (MSH6, UNC45A; 2/26); huMAP3_12711.1 (TLK2, IPO4; 2/35); huMAP3_06247.1 (UQCRC2, HEATR1; 2/65); huMAP3_06511.1 (PRMT5, GEMIN2; 2/79); huMAP3_08980.1 (PRMT5, GEMIN2; 2/97)

### Novelty

The constituent biology is established: DNA replication, mismatch repair, RNA processing, ribosome biogenesis, chromatin regulation and spliceosomal functions are already known, and several relationships are represented in STRING and hu.MAP. The potentially novel aspect is the conserved co-abundance organization linking these processes across bone marrow and kidney. The supplied evidence does not establish whether this exact tissue-pair module has been reported previously. Absence from STRING or hu.MAP would not prove novelty because those resources emphasize molecular interactions and complexes rather than tissue-pair co-abundance patterns. The appropriate conclusion is that this may be a new cross-tissue co-abundance configuration assembled from largely known biological components; independent replication and comparison with published co-expression modules are needed before claiming a new mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated activity of proliferating or repairing progenitor cells shared by bone marrow and kidney. A replication core involving MCM2, MCM5, POLE, POLD3, FEN1 and RRM1 could support genome duplication and repair, while MSH6 supports mismatch recognition. EMG1, HEATR1, BYSL, PDCD11 and UTP4 could support ribosome biogenesis, while RNA-processing and chromatin-associated genes maintain gene-expression capacity during cell-cycle progression. The co-abundance pattern may therefore arise because DNA synthesis, genome surveillance, ribosome production and RNA maturation are jointly increased in cells with high biosynthetic and proliferative demand. This is a mechanistic hypothesis, not evidence that all module members physically interact or that any one gene causes the module.

### Important genes

#### MCM2

- **Related proteins** (co-abundance neighbors): HAUS5 (0.89); STRING partners: ELOC (0.803), FEN1 (0.912), MCM5 (0.999), POLE (0.997), RRM1 (0.914)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_10747.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a core replication-initiation factor and appears in the primary DNA-replication and nucleic-acid-metabolism evidence (KEGG DNA replication - Homo sapiens (human); q_global = 0.0457) (GO:BP nucleic acid metabolic process; q_global = 0.0486). It has STRING links to MCM5, POLE, FEN1 and RRM1 and appears in several hu.MAP replication complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_10747.1). HPA reports enhancement in bone marrow and lymphoid tissue and in progenitor populations. Its established function, network position and substantial literature make it a strong anchor gene.
- **Conclusion**: Established evidence supports MCM2 as a replication-initiation component and a major biological anchor of the module. Its co-abundance is consistent with proliferating progenitor cells, but the data do not show that MCM2 mechanistically drives the cross-tissue module.

#### MCM5

- **Related proteins** (co-abundance neighbors): HAUS5 (0.89), POLE (0.85); STRING partners: ELOC (0.811), FEN1 (0.942), MCM2 (0.999), MSH6 (0.749), POLE (0.997), RRM1 (0.957)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 5. The protein encoded by this gene is structurally very similar to the CDC46 protein from S. cerevisiae, a protein involved in the initiation of DNA replication. The encoded protein is a member of the MCM family of chromatin-binding proteins and can interact with at least two other members of this family. The encoded protein is upregulated in the transition from the G0 to G1/S phase of the cell cycl…
- **Diseases (Open Targets)**: Meier-Gorlin syndrome (0.563); neurodegenerative disease (0.397); lysosomal storage disease (0.362); kidney transplant (0.198); diabetic ketoacidosis (0.129)
- **Europe PMC papers**: 4143
- **Why important**: MCM5 is included in the primary DNA-replication and nucleic-acid-metabolism evidence (KEGG DNA replication - Homo sapiens (human); q_global = 0.0457) (GO:BP nucleic acid metabolic process; q_global = 0.0486). It has strong STRING relationships with MCM2, POLE, FEN1, RRM1 and MSH6 and is represented in several hu.MAP replication assemblies (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1). HPA shows bone-marrow enhancement and enrichment in erythrocyte and megakaryocyte progenitor populations. Its established role in replication initiation and substantial literature support its importance for the proliferative interpretation.
- **Conclusion**: Established evidence identifies MCM5 as part of the replicative helicase machinery and supports a progenitor-cell proliferation interpretation. The cross-tissue conservation suggests shared cellular demand, but does not establish a kidney-specific or bone-marrow-specific function.

#### POLE

- **Related proteins** (co-abundance neighbors): EMG1 (0.95), BRD2 (0.90), UQCRC2 (0.90), HEATR1 (0.88), AP1M1 (0.87), MCM5 (0.85), SYMPK (0.84); STRING partners: ELOC (0.803), FEN1 (0.906), MCM2 (0.997), MCM5 (0.997), MSH6 (0.957), POLD3 (0.963)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA polymerase epsilon, catalytic subunit. This gene encodes the catalytic subunit of DNA polymerase epsilon. The enzyme is involved in DNA repair and chromosomal DNA replication. Mutations in this gene have been associated with colorectal cancer 12 and facial dysmorphism, immunodeficiency, livedo, and short stature. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal cancer, susceptibility to, 12 (0.739); intrauterine growth retardation, metaphyseal dysplasia, adrenal hypoplasia congenita, genital anomalies, and immunodeficiency (0.735); facial dysmorphism-immunodeficiency-livedo-short stature syndrome (0.732); non-small cell lung carcinoma (0.668); B-cell chronic lymphocytic leukemia (0.660)
- **Europe PMC papers**: 71098
- **Why important**: POLE is the catalytic subunit of DNA polymerase epsilon and is present in both primary terms (KEGG DNA replication - Homo sapiens (human); q_global = 0.0457) (GO:BP nucleic acid metabolic process; q_global = 0.0486). It connects the replication component to MCM2, MCM5, FEN1, POLD3 and MSH6 through STRING relationships (5 supplementary STRING terms; within-query FDR 0.0108–0.0339). HPA shows bone-marrow tissue enhancement and expression in erythrocyte and megakaryocyte progenitor populations. Its extensive literature and associations with colorectal cancer, immunodeficiency and related disease make it highly informative for both function and disease relevance.
- **Conclusion**: Established evidence supports POLE as an executor of chromosomal DNA replication and repair. Its presence strongly anchors the module in genome duplication and genome maintenance, while its disease associations show the consequences of replication failure. A causal role in formation of this co-abundance module remains hypothetical.

#### FEN1

- **Related proteins** (co-abundance neighbors): HAUS5 (0.86); STRING partners: MCM2 (0.912), MCM5 (0.942), MSH6 (0.95), POLD3 (0.983), POLE (0.906), RRM1 (0.766)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: flap structure-specific endonuclease 1. The protein encoded by this gene removes 5' overhanging flaps in DNA repair and processes the 5' ends of Okazaki fragments in lagging strand DNA synthesis. Direct physical interaction between this protein and AP endonuclease 1 during long-patch base excision repair provides coordinated loading of the proteins onto the substrate, thus passing the substrate from one enzyme to another. The protein is…
- **Diseases (Open Targets)**: neurodegenerative disease (0.496); HIV infectious disease (0.370); hepatocellular carcinoma (0.213); breast carcinoma (0.213); oral cavity squamous cell carcinoma (0.208)
- **Europe PMC papers**: 5275
- **Why important**: FEN1 is included in both primary terms (KEGG DNA replication - Homo sapiens (human); q_global = 0.0457) (GO:BP nucleic acid metabolic process; q_global = 0.0486) and is linked by STRING to MCM2, MCM5, POLE, POLD3, MSH6 and RRM1 (5 supplementary STRING terms; within-query FDR 0.0108–0.0339). Its documented role in processing Okazaki-fragment flaps and DNA-repair intermediates links replication with repair. HPA shows enhancement in lymphoid tissue and several progenitor populations. Its substantial literature and cancer associations further support its importance.
- **Conclusion**: Established evidence supports FEN1 as a replication-associated DNA-repair nuclease that reinforces the module's genome-maintenance interpretation. Its co-abundance with replication machinery is biologically coherent, but does not prove that it coordinates the RNA and nucleolar components.

#### EMG1

- **Related proteins** (co-abundance neighbors): POLE (0.95), TARBP1 (0.93), HAUS5 (0.90); STRING partners: BYSL (0.999), HEATR1 (0.998), PDCD11 (0.993), UTP4 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EMG1 N1-specific pseudouridine methyltransferase. This gene encodes an essential, conserved eukaryotic protein that methylates pseudouridine in 18S rRNA. The related protein in yeast is a component of the small subunit processome and is essential for biogenesis of the ribosomal 40S subunit. A mutation in this gene has been associated with Bowen-Conradi syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Fe…
- **Diseases (Open Targets)**: Bowen-Conradi syndrome (0.671); hereditary disease (0.181); neurodegenerative disease (0.088); retinitis pigmentosa (0.085); cone dystrophy (0.076)
- **Europe PMC papers**: 457
- **Why important**: EMG1 is part of the globally significant nucleic-acid metabolic process (GO:BP nucleic acid metabolic process; q_global = 0.0486) and connects POLE and TARBP1 with a nucleolar network. STRING shows strong relationships with BYSL, HEATR1, PDCD11 and UTP4, forming a coherent small-subunit ribosome-biogenesis component (STRING Process Nucleic acid metabolic process; within-query FDR = 0.0108) (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0195) (STRING Keyword Nucleus; within-query FDR = 0.0273). Its established role in eighteen-S rRNA modification and small-subunit maturation, together with its association with Bowen-Conradi syndrome, gives it distinctive mechanistic and disease relevance.
- **Conclusion**: Established evidence supports EMG1 as a nucleolar rRNA-processing factor, showing that the module extends beyond DNA replication into ribosome biogenesis. Its network position is consistent with coordinated biosynthetic demand, but whether it directly links replication and ribosome production is a hypothesis.

## Module 9

**Tissue pair**: bone_marrow and kidney  
**Genes (6)**: ALDH1A2, FNTA, GMPPB, EEF1E1, PSMA4, RO60

### Function

No GO or KEGG term passed global correction, and there are no supplementary STRING enrichment terms. The module therefore does not support a formally enriched pathway assignment. Its structure is a hub-and-spoke pattern centered on ALDH1A2, connected individually to EEF1E1, GMPPB, FNTA, PSMA4, and RO60. The gene annotations suggest a heterogeneous cellular-maintenance module that combines retinoic-acid biosynthesis, translation and DNA-damage response, glycoprotein biosynthesis, protein prenylation, proteasomal degradation, and RNA regulation. These annotations support biological plausibility for coordinated cellular state or abundance rather than a single established pathway.

**Cell composition.** All module proteins were detected in both bone marrow and kidney. None is secreted, so the module is not a plasma-protein or secreted-protein signature. Most genes have low tissue specificity and low immune-cell specificity, arguing against a strongly blood-cell-restricted program. The HPA single-cell evidence is nevertheless cell-type enriched or group enriched for every gene, with recurring signals in early spermatids and trophoblast populations and a smaller signal in stromal, epithelial, or plasma-cell populations. This pattern is more consistent with broadly expressed intracellular proteins whose abundance may vary with cellular composition or state than with a coherent bone-marrow or kidney-specific function. The neutrophil enrichment reported for ALDH1A2 should be treated as a limited cell-type association rather than evidence that the whole module is a neutrophil module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no STRING functional-enrichment result. No hu.MAP complex contains multiple module members. Thus, the observed co-abundance edges are not supported by the supplied reference interaction networks as known physical interactions or a shared canonical complex. The star-like topology, with ALDH1A2 connected to each other member and no peripheral-to-peripheral edges, is compatible with coordinated abundance without implying direct molecular binding. The absence of STRING or hu.MAP support also means that the network should be interpreted cautiously as a co-abundance pattern.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This exact shared co-abundance module appears potentially novel within the evidence supplied, because its gene combination has no reported STRING interaction support, no multi-member hu.MAP complex, and no globally significant GO or KEGG annotation. However, these absences do not establish biological novelty: they may reflect indirect regulation, shared cell composition, limited network coverage, or a dataset-specific abundance pattern. The defensible conclusion is that the module is a potentially new cross-tissue co-abundance observation, not a newly discovered molecular complex or pathway.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular cellular-state program present in both tissues, in which ALDH1A2-linked retinoic-acid metabolism covaries with general protein homeostasis, glycoprotein synthesis, protein prenylation, proteasome activity, and RNA regulation. ALDH1A2 may act as a transcriptomic or cellular-state hub rather than a physical binding hub. Variation in stromal, epithelial, progenitor, or other specialized cell contributions could generate the coordinated abundance pattern. This hypothesis requires validation with independent cohorts, cell-composition adjustment, expression-level replication, and perturbation or spatial experiments; it is not established by the enrichment or interaction evidence.

### Important genes

#### ALDH1A2

- **Related proteins** (co-abundance neighbors): EEF1E1 (0.90), GMPPB (0.84), FNTA (0.82), PSMA4 (0.81), RO60 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 1 family member A2. This protein belongs to the aldehyde dehydrogenase family of proteins. The product of this gene is an enzyme that catalyzes the synthesis of retinoic acid (RA) from retinaldehyde. Retinoic acid, the active derivative of vitamin A (retinol), is a hormonal signaling molecule that functions in developing and adult tissues. The studies of a similar mouse gene suggest that this enzyme and the cytochrom…
- **Diseases (Open Targets)**: diaphragmatic hernia 4, with cardiovascular defects (0.704); osteoarthritis, hand (0.464); osteoarthritis, knee (0.462); Knee pain (0.366); alcohol drinking (0.352)
- **Europe PMC papers**: 3482
- **Why important**: ALDH1A2 is the network hub, connected to every other module member with the strongest aggregate connectivity in the supplied subgraph. It catalyzes retinoic-acid synthesis and is annotated with retinoic-acid biosynthesis, vitamin A metabolism, kidney development, and regulation of cell proliferation. Its HPA pattern includes tissue enhancement in endometrium and fallopian tube, several stromal or mesothelial-related cell associations, and an immune-cell association with neutrophils. It also has the largest literature volume in the module and disease associations including diaphragmatic hernia with cardiovascular defects and osteoarthritis.
- **Conclusion**: Established evidence supports ALDH1A2 as the statistical hub and as an enzyme involved in retinoic-acid production and developmental or proliferative biology. It is the leading candidate for organizing the module at the level of coordinated abundance. It is not established that ALDH1A2 physically interacts with the other genes or mechanistically drives their abundance.

#### PSMA4

- **Related proteins** (co-abundance neighbors): ALDH1A2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 20S subunit alpha 4. This gene encodes a core alpha subunit of the 20S proteosome, which is a highly ordered ring-shaped structure composed of four rings of 28 non-identical subunits. Proteasomes cleave peptides in an ATP- and ubiquitin-dependent manner. [provided by RefSeq, Aug 2016].
- **Diseases (Open Targets)**: plasma cell myeloma (0.616); mantle cell lymphoma (0.542); neoplasm (0.513); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1240
- **Why important**: PSMA4 is a core proteasome subunit and is connected directly to ALDH1A2 in the module. Its annotations link it to ubiquitin-dependent protein degradation, DNA repair, apoptosis, DNA-damage response, oxidative-stress response, and immune processes. It is detected in both tissues, has cell-type-enriched associations involving trophoblasts and germ-cell populations, and has substantial literature and disease associations including plasma-cell myeloma, mantle-cell lymphoma, neoplasm, HIV infection, and amyloidosis.
- **Conclusion**: Established evidence supports PSMA4 as a component of constitutive proteasomal protein turnover and cellular stress responses. Its inclusion makes a protein-homeostasis or stress-state interpretation plausible. The module does not establish a specific connection between proteasomal activity and ALDH1A2 or demonstrate that PSMA4 is functionally regulated by retinoic acid.

#### RO60

- **Related proteins** (co-abundance neighbors): ALDH1A2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Primary cilium, Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Ro60, Y RNA binding protein. Enables RNA binding activity. Involved in cellular response to interferon-alpha and regulation of gene expression. Located in cytosol and nucleoplasm. Part of ribonucleoprotein complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: glomerulonephritis (0.180); gastrointestinal disease (0.180); laryngeal disorder (0.172); systemic sclerosis (0.107); systemic lupus erythematosus (0.103)
- **Europe PMC papers**: 1234
- **Why important**: RO60 is directly connected to ALDH1A2 and encodes an RNA-binding protein involved in ribonucleoprotein biology, gene-expression regulation, and cellular response to interferon-alpha. It is associated with the primary cilium and cytosol, has an early-spermatid cell-type signal, and has a substantial literature. Its disease associations include glomerulonephritis and systemic lupus erythematosus, which are relevant to immune-mediated kidney biology.
- **Conclusion**: Established evidence supports RO60 as an RNA-regulatory and interferon-responsive protein with disease relevance to immune and renal contexts. It could mark a regulatory or stress-responsive component of the module. A direct role in the shared bone-marrow–kidney co-abundance pattern remains hypothetical because there is no supplied STRING, hu.MAP, or enrichment support.

#### GMPPB

- **Related proteins** (co-abundance neighbors): ALDH1A2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GDP-mannose pyrophosphorylase B. This gene is thought to encode a GDP-mannose pyrophosphorylase. The encoded protein catalyzes the conversion of mannose-1-phosphate and GTP to GDP-mannose, a reaction involved in the production of N-linked oligosaccharides. Alternatively spliced transcript variants encoding distinct isoforms have been described. [provided by RefSeq, Jan 2009].
- **Diseases (Open Targets)**: autosomal recessive limb-girdle muscular dystrophy type 2T (0.833); muscular dystrophy-dystroglycanopathy (congenital with brain and eye anomalies), type A14 (0.800); muscular dystrophy-dystroglycanopathy (congenital with intellectual disability), type B14 (0.791); muscle-eye-brain disease (0.634); congenital muscular dystrophy with cerebellar involvement (0.619)
- **Europe PMC papers**: 773
- **Why important**: GMPPB is directly connected to ALDH1A2 and participates in GDP-mannose production, a prerequisite for glycoprotein biosynthesis. It is detected in both tissues and has cell-type-enriched associations spanning several epithelial or specialized cell types, including plasma cells and extravillous trophoblasts. Its disease associations are strong for muscular dystrophy and dystroglycanopathy, and its literature supports a well-established role in glycosylation biology.
- **Conclusion**: Established evidence supports GMPPB as a glycosylation-related metabolic enzyme with important inherited-disease associations. It may indicate biosynthetic or secretory-pathway demand within the cells contributing to the module, despite the module containing no secreted proteins. The data do not show that GMPPB and ALDH1A2 share a direct biochemical pathway.

#### EEF1E1

- **Related proteins** (co-abundance neighbors): ALDH1A2 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation elongation factor 1 epsilon 1. This gene encodes a multifunctional protein that localizes to both the cytoplasm and nucleus. In the cytoplasm, the encoded protein is an auxiliary component of the macromolecular aminoacyl-tRNA synthase complex. However, its mouse homolog has been shown to translocate to the nucleus in response to DNA damage, and it plays a positive role in ATM/ATR-mediated p53 activation. Alternative splicing re…
- **Diseases (Open Targets)**: respiratory tract infectious disorder (0.220); atrioventricular block (0.205); neoplasm (0.093); response to antihypertensive drug (0.092); hepatocellular carcinoma (0.087)
- **Europe PMC papers**: 1428
- **Why important**: EEF1E1 is directly connected to ALDH1A2 and is an auxiliary component of the aminoacyl-tRNA synthetase machinery. Its annotations also include DNA-damage response, p53 signaling, apoptosis, and cellular senescence. It is broadly detected in both tissues, has a group-enriched association with spermatids, has substantial literature, and has disease associations involving infection, cardiac conduction, neoplasm, and drug response.
- **Conclusion**: Established evidence supports EEF1E1 as a translation-associated and stress-response protein. It may represent general biosynthetic or nuclear stress-state activity within the module. Its module relationship to ALDH1A2 is a co-abundance observation, not evidence of a direct interaction or a shared established pathway.

## Module 10

**Tissue pair**: bone_marrow and kidney  
**Genes (20)**: AP2B1, CALU, CORO1C, DPYSL3, FLNA, FLNB, FLNC, FSCN1, G6PD, GARS1, HSPA8, HYOU1, PKM, NIBAN2, P4HA1, PDIA4, SEC23A, SEPTIN9, TFRC, TKT

### Function

The strongest interpretation is a vesicle-, membrane-trafficking-, and cytoskeleton-associated module. The primary evidence is the broad vesicle annotation (GO:CC vesicle; q_global = 0.00185), supported by cytoplasmic and intracellular vesicle terms (GO:CC cytoplasmic vesicle; q_global = 0.0397) and (GO:CC intracellular vesicle; q_global = 0.0416). The module also supports cell-junction organization (GO:CC cell junction; q_global = 0.0412) and cadherin-associated interactions (GO:MF cadherin binding; q_global = 0.031). Together, these findings indicate coordinated handling of membrane cargo, cell-surface organization, adhesion, and actin remodeling rather than a narrowly defined metabolic pathway. The module contains complementary subthemes: clathrin-associated trafficking through AP2B1 and TFRC, ER-to-Golgi handling through SEC23A and ER proteins, actin architecture through the filamin and fascin genes, and cellular energy or redox support through PKM, G6PD, and TKT. The vesicle and junction interpretation is supported by globally corrected terms (GO:CC vesicle; q_global = 0.00185), (GO:CC cytoplasmic vesicle; q_global = 0.0397), (GO:CC cell junction; q_global = 0.0412), and (GO:CC intracellular vesicle; q_global = 0.0416); the extracellular-region annotation (GO:CC extracellular region; q_global = 0.0342) is compatible with membrane-associated or exported proteins but does not by itself establish a secretory program.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. Several genes have intracellular or membrane-associated secretome annotations, while TFRC is annotated as secreted to blood and other proteins have intracellular-and-membrane annotations. The HPA profile is broadly distributed across tissues, with many genes showing low tissue specificity, so the module is not convincingly restricted to either bone marrow or kidney. There is nevertheless a substantial cell-type signal: platelet, monocyte, myeloid, neutrophil, megakaryocyte, and erythroid-related annotations occur among the genes, and the STRING tissue results include blood and blood platelet (STRING TISSUES Blood platelet; within-query FDR = 0.0021) and (STRING TISSUES Blood; within-query FDR = 0.005). Because most genes have low immune-cell specificity, this should not be described as a pure leukocyte module. The shared signal may instead reflect common vascular, stromal, epithelial, platelet, or other resident cell populations, with a possible contribution from blood contamination or hematopoietic cells in tissue samples. The HPA protein evidence shows broad detection in both tissues, although individual genes differ, so the conserved module is more consistent with a shared cellular process than with uniform protein expression by every cell in both organs.

**GO/KEGG enrichment**: 6 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC vesicle | 0.00185 | AP2B1, CALU, CORO1C, DPYSL3, FLNA, FLNB, FSCN1, G6PD, GARS1, HSPA8, HYOU1, NIBAN2, PDIA4, PKM, SEC23A, TFRC, TKT |
| GO:MF cadherin binding | 0.031 | FLNA, FLNB, FSCN1, HSPA8, NIBAN2, PKM, SEPTIN9 |
| GO:CC extracellular region | 0.0342 | CALU, DPYSL3, FLNA, FLNB, FSCN1, G6PD, GARS1, HSPA8, HYOU1, NIBAN2, PDIA4, PKM, TFRC, TKT |
| GO:CC cytoplasmic vesicle | 0.0397 | AP2B1, CALU, CORO1C, DPYSL3, FLNB, GARS1, HSPA8, HYOU1, PDIA4, PKM, SEC23A, TFRC |
| GO:CC cell junction | 0.0412 | AP2B1, CORO1C, DPYSL3, FLNA, FLNB, FLNC, FSCN1, HSPA8, HYOU1, NIBAN2, TFRC |
| GO:CC intracellular vesicle | 0.0416 | AP2B1, CALU, CORO1C, DPYSL3, FLNB, GARS1, HSPA8, HYOU1, PDIA4, PKM, SEC23A, TFRC |

### STRING and hu.MAP

STRING provides substantial prior support for a cytoskeletal and metabolic backbone. The filamin genes are linked to one another and to FSCN1, while G6PD, PKM, and TKT form a coherent metabolic association. HSPA8 is linked to TFRC, and HYOU1 is very strongly linked to PDIA4, supporting a chaperone, ER-stress, and trafficking component. AP2B1 is linked to TFRC, consistent with receptor-mediated endocytosis. The module therefore contains several already-known interaction neighborhoods rather than a uniformly novel network. hu.MAP independently supports an AP2B1–SEC23A trafficking complex (hu.MAP huMAP3_12394.1), a PKM–GARS1 complex (hu.MAP huMAP3_14442.1), and PDIA4–HYOU1 associations in ER or protein-processing complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). However, the hu.MAP support is partial: only a small subset of each large complex is represented in this module. The co-abundance module consequently integrates known physical or functional relationships, but its cross-process organization and tissue-pair conservation are not demonstrated by STRING or hu.MAP alone.

**STRING interactions (score >= 0.7)**: 15 of 190 gene pairs: AP2B1–TFRC (0.779); FLNA–FLNB (0.979); FLNA–FLNC (0.907); FLNA–FSCN1 (0.887); FLNA–SEPTIN9 (0.707); FLNB–FLNC (0.921); FLNB–FSCN1 (0.788); FLNC–FSCN1 (0.794); G6PD–PKM (0.941); G6PD–TKT (0.91); HSPA8–HYOU1 (0.746); HSPA8–TFRC (0.969); HYOU1–PDIA4 (0.997); P4HA1–PDIA4 (0.765); PKM–TKT (0.951)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Digestive gland (FDR = 3.12e-06, 19 genes); TISSUES Gonad (FDR = 0.00023, 14 genes); TISSUES Respiratory system (FDR = 0.00024, 13 genes); TISSUES Male reproductive gland (FDR = 0.00053, 15 genes); TISSUES Liver (FDR = 0.00053, 15 genes); Component Vesicle (FDR = 0.00063, 17 genes); TISSUES Lung (FDR = 0.00093, 11 genes); TISSUES Viscus (FDR = 0.0012, 19 genes); TISSUES Endocrine gland (FDR = 0.0014, 20 genes); TISSUES Blood platelet (FDR = 0.0021, 7 genes); COMPARTMENTS Cell periphery (FDR = 0.0023, 12 genes); SMART Filamin-type immunoglobulin domains (FDR = 0.003, 3 genes); TISSUES Atrium (FDR = 0.0044, 4 genes); TISSUES Muscle (FDR = 0.0047, 8 genes); TISSUES Blood (FDR = 0.005, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (PKM, GARS1; 2/57); huMAP3_06775.1 (PDIA4, HYOU1; 2/60); huMAP3_09327.1 (PDIA4, HYOU1; 2/93); huMAP3_12394.1 (AP2B1, SEC23A; 2/98)

### Novelty

This cannot be called a wholly new molecular interaction module. Many component relationships are already represented in STRING, and several pairs are supported by hu.MAP, especially the filamin network, the metabolic enzyme group, the AP2B1–SEC23A trafficking connection, and the PDIA4–HYOU1 ER association. Conversely, database support does not eliminate novelty at the systems level. The potentially new finding is the conserved co-abundance of these trafficking, actin, stress-folding, and metabolic genes across bone marrow and kidney, particularly the way they are assembled into one tissue-pair module. That claim remains provisional because the network is relatively sparse, the HPA profile suggests shared cell-type or sample-composition effects, and absence of a pair from STRING or hu.MAP is not evidence that the relationship is novel. Independent cohorts, cell-type deconvolution, and perturbation or localization experiments would be needed to establish novelty.

**Hypothesis.** Hypothesis: the module represents a shared membrane-remodeling and cargo-handling state in selected bone-marrow and kidney cell populations. Actin crosslinkers and bundlers may organize cortical structures and junctions, while AP2B1, TFRC, and SEC23A coordinate endocytic and ER-to-Golgi trafficking. PDIA4, HYOU1, and CALU may support folding and export of membrane or secretory cargo under ER stress, with HSPA8 assisting chaperoning and vesicle disassembly. PKM, G6PD, and TKT may provide glycolytic and redox capacity required for trafficking, cytoskeletal remodeling, and stress adaptation. The observed conservation could therefore reflect a common functional state of vascular, epithelial, stromal, platelet, or hematopoietic cells rather than a kidney-and-bone-marrow-specific pathway. This is a mechanistic model, not an experimentally established causal chain.

### Important genes

#### NIBAN2

- **Related proteins** (co-abundance neighbors): FLNC (0.87), SEPTIN9 (0.86), FLNB (0.85), P4HA1 (0.84), HSPA8 (0.81), GARS1 (0.81), TKT (0.81), G6PD (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: niban apoptosis regulator 2. Enables transcription coactivator activity. Involved in several processes, including gonadotropin secretion; positive regulation of transcription regulatory region DNA binding activity; and regulation of cellular macromolecule biosynthetic process. Located in several cellular components, including adherens junction; cytosol; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: asthma (0.281); prostate carcinoma (0.252); melanoma (0.081); neoplasm (0.080); osteoporosis (0.079)
- **Europe PMC papers**: 91
- **Why important**: NIBAN2 has the strongest weighted network position in the module and connects cytoskeletal, metabolic, and stress-associated genes. It contributes to the vesicle, cadherin-binding, extracellular-region, and junction terms (GO:CC vesicle; q_global = 0.00185), (GO:MF cadherin binding; q_global = 0.031), (GO:CC extracellular region; q_global = 0.0342), and (GO:CC cell junction; q_global = 0.0412). Its annotations include transcriptional coactivator activity and regulation of proliferation and apoptosis, while its HPA profile points toward an esophageal and classical-monocyte context rather than a kidney-specific role. It has no STRING partner or hu.MAP complex listed here, making its central co-abundance position especially informative but also less mechanistically established. Its literature volume is modest relative to the major cytoskeletal and metabolic genes.
- **Conclusion**: Established: NIBAN2 is a central module gene associated with transcriptional and survival-related functions and participates in several primary module annotations. Hypothesis: NIBAN2 may coordinate stress or cell-state signaling with the trafficking and cytoskeletal program. Its causal role and physical connectivity require direct validation.

#### PDIA4

- **Related proteins** (co-abundance neighbors): HYOU1 (0.85), SEPTIN9 (0.84), TFRC (0.80); STRING partners: HYOU1 (0.997), P4HA1 (0.765)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 is a direct component of the ER folding and secretion machinery, with annotations for protein folding, secretion, and ER stress. It participates in the vesicle and intracellular-vesicle terms (GO:CC vesicle; q_global = 0.00185), (GO:CC cytoplasmic vesicle; q_global = 0.0397), and (GO:CC intracellular vesicle; q_global = 0.0416), is detected in both tissues, and connects to HYOU1 in STRING and hu.MAP (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). The very strong PDIA4–HYOU1 relationship and the additional P4HA1 association provide a coherent ER-processing subnetwork. Its disease associations and substantial literature support make it a more established biological anchor than an uncharacterized connector.
- **Conclusion**: Established: PDIA4 is a plausible ER proteostasis and secretory-trafficking component of the module. Hypothesis: variation in this PDIA4-centered subnetwork may mark or help sustain an ER-stress-adapted state shared by relevant bone-marrow and kidney cell populations.

#### FLNA

- **Related proteins** (co-abundance neighbors): FLNC (0.82); STRING partners: FLNB (0.979), FLNC (0.907), FSCN1 (0.887), SEPTIN9 (0.707)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is a canonical actin crosslinker and membrane-interface organizer. It is linked by STRING to FLNB, FLNC, FSCN1, and SEPTIN9, and contributes to vesicle, cadherin-binding, extracellular-region, and junction terms (GO:CC vesicle; q_global = 0.00185), (GO:MF cadherin binding; q_global = 0.031), (GO:CC extracellular region; q_global = 0.0342), and (GO:CC cell junction; q_global = 0.0412). Its HPA annotations include vascular and megakaryocyte-related cell contexts, which are relevant to both tissue architecture and possible blood-derived signal. FLNA has extensive literature and multiple established disease associations, making it a strong functional representative of the module's cytoskeletal arm.
- **Conclusion**: Established: FLNA can connect actin architecture to membrane proteins, cell shape, migration, and platelet-related biology. Hypothesis: FLNA may provide the structural interface through which vesicle trafficking and cell-junction remodeling become coordinated in this conserved module.

#### FLNC

- **Related proteins** (co-abundance neighbors): NIBAN2 (0.87), FLNA (0.82), FLNB (0.82), CALU (0.81); STRING partners: FLNA (0.907), FLNB (0.921), FSCN1 (0.794)
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin C. This gene encodes one of three related filamin genes, specifically gamma filamin. These filamin proteins crosslink actin filaments into orthogonal networks in cortical cytoplasm and participate in the anchoring of membrane proteins for the actin cytoskeleton. Three functional domains exist in filamin: an N-terminal filamentous actin-binding domain, a C-terminal self-association domain, and a membr…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy 26 (0.833); myofibrillar myopathy 5 (0.791); distal myopathy with posterior leg and anterior hand involvement (0.742); dilated cardiomyopathy (0.714); familial restrictive cardiomyopathy (0.660)
- **Europe PMC papers**: 3861
- **Why important**: FLNC links the module's actin network to muscle and membrane architecture. It is connected in STRING to FLNA, FLNB, and FSCN1 and is the only gene in the primary junction term (GO:CC cell junction; q_global = 0.0412) among the selected filamin representatives. HPA shows tissue enhancement in heart muscle, skeletal muscle, and tongue, with group enrichment in cardiomyocytes, myonuclei, and smooth-muscle-related cells. Its established role in actin crosslinking, sarcomere organization, and cardiomyopathy, together with a large literature base, makes it informative for distinguishing a structural-cell contribution from a purely immune interpretation.
- **Conclusion**: Established: FLNC is a well-supported actin and muscle-architecture gene within a known filamin interaction neighborhood. Hypothesis: its presence may indicate vascular or smooth-muscle structural cells, or another contractile-cell contribution, rather than a kidney-specific signaling mechanism.

#### HSPA8

- **Related proteins** (co-abundance neighbors): NIBAN2 (0.81), DPYSL3 (0.80); STRING partners: HYOU1 (0.746), TFRC (0.969)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Flagellar centriole, Annulus; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 8. This gene encodes a member of the heat shock protein 70 family, which contains both heat-inducible and constitutively expressed members. This protein belongs to the latter group, which are also referred to as heat-shock cognate proteins. It functions as a chaperone, and binds to nascent polypeptides to facilitate correct folding. It also functions as an ATPase in the disassembly of clathrin-coated…
- **Diseases (Open Targets)**: dengue disease (0.505); systemic lupus erythematosus (0.375); smoking initiation (0.199); Lennox-Gastaut syndrome (0.118); neoplasm (0.105)
- **Europe PMC papers**: 6937
- **Why important**: HSPA8 is a constitutive chaperone and also participates in clathrin-coated-vesicle disassembly. It appears in every primary GO term listed for the module, including vesicles, cadherin binding, extracellular region, cytoplasmic and intracellular vesicles, and cell junctions (GO:CC vesicle; q_global = 0.00185) through (GO:CC intracellular vesicle; q_global = 0.0416). Its STRING links to HYOU1 and TFRC connect chaperoning with ER stress and receptor trafficking. HPA detects it in both tissues and shows broad cell-type distribution, consistent with a general cellular-state component rather than a tissue-restricted marker. Its extensive literature supports a well-established role in protein folding and membrane transport.
- **Conclusion**: Established: HSPA8 is a strong multifunctional bridge between proteostasis and vesicle traffic. Hypothesis: HSPA8 may help couple increased membrane turnover to folding or stress adaptation in the cell populations generating the shared module.

#### G6PD

- **Related proteins** (co-abundance neighbors): DPYSL3 (0.82), AP2B1 (0.81), NIBAN2 (0.81); STRING partners: PKM (0.941), TKT (0.91)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glucose-6-phosphate dehydrogenase. This gene encodes glucose-6-phosphate dehydrogenase. This protein is a cytosolic enzyme encoded by a housekeeping X-linked gene whose main function is to produce NADPH, a key electron donor in the defense against oxidizing agents and in reductive biosynthetic reactions. G6PD is remarkable for its genetic diversity. Many variants of G6PD, mostly produced from missense mutations, have been described…
- **Diseases (Open Targets)**: anemia, nonspherocytic hemolytic, due to G6PD deficiency (0.851); anemia (phenotype) (0.776); G6PD deficiency (0.686); hereditary disease (0.535); infection (0.488)
- **Europe PMC papers**: 16994
- **Why important**: G6PD represents the redox and metabolic arm of the module. It is linked by STRING to PKM and TKT and is annotated for the pentose-phosphate pathway, NADPH production, and defense against oxidizing agents. It contributes to the primary vesicle and extracellular-region terms (GO:CC vesicle; q_global = 0.00185) and (GO:CC extracellular region; q_global = 0.0342), while HPA places it in megakaryocyte, neutrophil-progenitor, neutrophil, and eosinophil-related contexts and detects it in both tissues. Its very large literature base and established deficiency-associated anemia make it biologically important, although its broad housekeeping character means that co-abundance may partly reflect general metabolic demand.
- **Conclusion**: Established: G6PD supplies a plausible redox-support function and is connected to the module's glycolytic and pentose-phosphate enzymes. Hypothesis: increased redox capacity may support actin remodeling, endocytic activity, and ER-stress handling, but the module alone cannot establish that this metabolic activity drives the structural program.

## Module 11

**Tissue pair**: bone_marrow and kidney  
**Genes (5)**: ANAPC7, CTTNBP2NL, MVP, PSMB8, WDR62

### Function

The strongest supported function is regulation of protein phosphorylation state, specifically protein phosphatase binding. The globally corrected terms (GO:MF protein phosphatase binding; q_global = 0.02) and (GO:MF phosphatase binding; q_global = 0.0391) converge on this interpretation and identify ANAPC7, CTTNBP2NL, and MVP. The module also contains genes linked to proteasomal protein turnover, cell-cycle control, intracellular signaling, and protein transport. These additional functions provide biological context but are not, by themselves, globally corrected enrichment results. The network is a connected chain-like subgraph, with MVP linking WDR62 to CTTNBP2NL and CTTNBP2NL linking MVP to PSMB8, while WDR62 links to ANAPC7. Because the module has no high-confidence STRING interactions among its gene pairs and no supported hu.MAP complex containing multiple members, the co-abundance structure should not be interpreted as a validated physical complex.

**Cell composition.** This is not a plasma or secreted-protein module: none of the genes is annotated as secreted. The HPA evidence instead indicates a mixed, broadly distributed cellular composition. Most genes have low tissue specificity, and all have some cell-type-enhanced annotation, including enterocytes, antigen-presenting or myeloid dendritic cells, microglia, megakaryocytes, platelets, and other differentiated cell types. A subset has enhanced immune-cell annotation, but the module is not uniformly blood-cell specific. Protein detection is present for most members in both bone marrow and kidney. Thus, the shared signal may reflect conserved intracellular programs or shared cellular populations rather than a tissue-specific secreted pathway. Possible contributions from blood or immune cells should nevertheless be considered, particularly for CTTNBP2NL and PSMB8.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF protein phosphatase binding | 0.02 | ANAPC7, CTTNBP2NL, MVP |
| GO:MF phosphatase binding | 0.0391 | ANAPC7, CTTNBP2NL, MVP |

### STRING and hu.MAP

STRING provides supplementary convergence on protein phosphatase binding through (STRING Function Protein phosphatase binding; within-query FDR = 0.0224), involving CTTNBP2NL, MVP, and ANAPC7. However, STRING reports no high-confidence interaction among any of the module gene pairs. hu.MAP likewise identifies no complex containing multiple module members. Therefore, the co-abundance relationships are not explained by an established physical complex in these resources. The shared abundance pattern may instead reflect co-regulation, common cellular state, indirect pathway coordination, or cell-composition effects.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Function Protein phosphatase binding (FDR = 0.0224, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is potentially novel as a cross-tissue co-abundance pattern because it is not recapitulated by a known STRING interaction network or a hu.MAP complex, while its members span phosphatase-binding, cell-cycle, proteasome, signaling, and transport-related biology. The globally corrected enrichment for protein phosphatase binding gives the pattern a coherent functional anchor. Nevertheless, absence from STRING or hu.MAP does not establish biological novelty: the genes and their individual functions are already known, and co-abundance can arise from shared regulation or cellular composition. The appropriate conclusion is that this is a novel or under-characterized module-level association requiring independent validation, not a newly discovered molecular complex.

**Hypothesis.** Hypothesis: in bone marrow and kidney, a shared cellular state coordinates phosphatase binding with protein quality control, intracellular signaling, and cell-cycle or cytoskeletal processes. CTTNBP2NL may provide a regulatory connection to protein dephosphorylation and transporter control, MVP may couple this state to intracellular signaling and protein transport, and ANAPC7, WDR62, and PSMB8 may reflect accompanying requirements for cell-cycle machinery, mitotic organization, and proteasome or immunoproteasome activity. The association could be driven by a mixture of conserved intracellular regulation and shared immune or hematopoietic cell representation. This is a mechanistic hypothesis, not a demonstrated physical interaction or causal pathway.

### Important genes

#### CTTNBP2NL

- **Related proteins** (co-abundance neighbors): PSMB8 (0.83), MVP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoli fibrillar center, Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CTTNBP2 N-terminal like. Enables protein phosphatase 2A binding activity. Acts upstream of or within negative regulation of transmembrane transport; negative regulation of transporter activity; and protein dephosphorylation. Located in actin cytoskeleton. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.226); Abnormality of the gastrointestinal tract (0.214); benign thyroid gland neoplasm (0.121); mathematical ability (0.118); alcohol drinking (0.104)
- **Europe PMC papers**: 172
- **Why important**: CTTNBP2NL is a central network connector with links to MVP and PSMB8 and is one of the genes in both globally corrected phosphatase-binding terms (GO:MF protein phosphatase binding; q_global = 0.02) and (GO:MF phosphatase binding; q_global = 0.0391), as well as the supplementary STRING term (STRING Function Protein phosphatase binding; within-query FDR = 0.0224). Its supplied annotation directly connects it to protein phosphatase binding, protein dephosphorylation, transporter regulation, and actin-cytoskeleton localization. HPA also links it to antigen-presenting and myeloid dendritic cell contexts, and its disease associations include skeletal and gastrointestinal abnormalities. Its literature volume is smaller than that of the better-established proteasome and vault genes, making it especially informative for the module's potentially under-characterized biology.
- **Conclusion**: Established evidence supports CTTNBP2NL as the most direct functional anchor for the phosphatase-binding interpretation and as a plausible bridge between regulatory and cellular-transport processes. It is a candidate module driver, but whether it causes the shared bone-marrow and kidney pattern remains untested.

#### MVP

- **Related proteins** (co-abundance neighbors): WDR62 (0.86), CTTNBP2NL (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: major vault protein. This gene encodes the major component of the vault complex. Vaults are multi-subunit ribonucleoprotein structures that may be involved in nucleo-cytoplasmic transport. The encoded protein may play a role in multiple cellular processes by regulating the MAP kinase, JAK/STAT and phosphoinositide 3-kinase/Akt signaling pathways. The encoded protein also plays a role in multidrug resistance, and expre…
- **Diseases (Open Targets)**: neurodegenerative disease (0.392); Alzheimer disease (0.349); Parkinson disease (0.332); lysosomal storage disease (0.331); glioblastoma (0.112)
- **Europe PMC papers**: 6545
- **Why important**: MVP is a network connector linking WDR62 and CTTNBP2NL and is present in (GO:MF protein phosphatase binding; q_global = 0.02), (GO:MF phosphatase binding; q_global = 0.0391), and (STRING Function Protein phosphatase binding; within-query FDR = 0.0224). It encodes the major component of the vault complex and has supplied annotations involving signal transduction, protein transport, MAP kinase, JAK/STAT, phosphoinositide signaling, and regulation of growth-factor signaling. It is detected in both tissues and has broad tissue distribution, while its disease literature is substantial and includes neurodegenerative and cancer-related associations.
- **Conclusion**: Established evidence supports MVP as a plausible integrator of phosphatase-associated regulation, intracellular transport, and signaling. Its broad expression makes it a credible contributor to a conserved cellular-state signal, but its network position does not prove that it physically binds the other module members.

#### ANAPC7

- **Related proteins** (co-abundance neighbors): WDR62 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules, Cytokinetic bridge, Mitotic spindle; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: anaphase promoting complex subunit 7. This gene encodes a tetratricopeptide repeat containing component of the anaphase promoting complex/cyclosome (APC/C), a large E3 ubiquitin ligase that controls cell cycle progression by targeting a number of cell cycle regulators such as B-type cyclins for 26S proteasome-mediated degradation through ubiquitination. The encoded protein is required for proper protein ubiquitination function of APC/…
- **Diseases (Open Targets)**: Ferguson-Bonni neurodevelopmental syndrome (0.475); neurodegenerative disease (0.233); obesity disorder (0.056); schizophrenia (0.040); Abnormality of the skeletal system (0.037)
- **Europe PMC papers**: 354
- **Why important**: ANAPC7 is present in both globally corrected phosphatase-binding terms (GO:MF protein phosphatase binding; q_global = 0.02) and (GO:MF phosphatase binding; q_global = 0.0391) and in the supplementary STRING term (STRING Function Protein phosphatase binding; within-query FDR = 0.0224). It is a component of the anaphase-promoting complex, an E3 ubiquitin ligase that controls cell-cycle progression and targets cell-cycle regulators for proteasomal degradation. Its localization to mitotic structures and its links to cell division and ubiquitination provide a strong cell-cycle explanation for part of the module. It is detected in both tissues and has associations with neurodevelopmental and other disease phenotypes.
- **Conclusion**: Established evidence supports ANAPC7 as the module member connecting phosphatase binding with cell-cycle and ubiquitin-dependent protein turnover. A coordinated proliferation or cellular-renewal state is plausible, but the co-abundance data alone cannot determine whether this reflects proliferating cells, regulation within cells, or both.

#### PSMB8

- **Related proteins** (co-abundance neighbors): CTTNBP2NL (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 20S subunit beta 8. The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent proc…
- **Diseases (Open Targets)**: proteosome-associated autoinflammatory syndrome (0.829); plasma cell myeloma (0.618); mantle cell lymphoma (0.542); neoplasm (0.536); amyloidosis (0.472)
- **Europe PMC papers**: 3589
- **Why important**: PSMB8 is the module's connection to proteasomal protein catabolism and the modified immunoproteasome. It is linked in the module to CTTNBP2NL and has annotations involving immune processes and cytokine regulation. HPA places it in cell types including enterocytes, megakaryocytes, and platelets, and it is detected in both tissues. Its disease associations include proteasome-associated autoinflammatory disease and hematologic malignancies, with substantial literature support.
- **Conclusion**: Established evidence supports PSMB8 as a protein-quality-control and immune-related component that may explain part of the shared bone-marrow and kidney signal. Its presence is compatible with an immune-cell or inflammatory contribution, but the module does not establish that immunoproteasome activity is the primary driver.

#### WDR62

- **Related proteins** (co-abundance neighbors): MVP (0.86), ANAPC7 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 62. This gene is proposed to play a role in cerebral cortical development. Mutations in this gene have been associated with microencephaly, cortical malformations, and cognitive disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2011].
- **Diseases (Open Targets)**: autosomal recessive primary microcephaly (0.815); hereditary disease (0.488); Intellectual disability (0.462); microcephaly (0.432); Skraban-Deardorff syndrome (0.358)
- **Europe PMC papers**: 820
- **Why important**: WDR62 has one of the stronger network positions in the module and connects MVP with ANAPC7. Its supplied annotations involve mitotic spindle organization, centriole replication, neurogenesis, and cerebral cortical development. It has tissue-enhanced expression in skeletal muscle, testis, and tongue, cell-type-enhanced annotations in germ-cell and photoreceptor contexts, and an immune-cell-enhanced annotation for non-classical monocytes. Its disease associations with primary microcephaly, cortical malformations, and cognitive disability are well established in the supplied evidence.
- **Conclusion**: Established evidence supports WDR62 as a cell-division and microtubule-related component that may connect ANAPC7-associated cell-cycle biology to the module's broader cellular state. Its tissue-enhanced profile is less obviously aligned with bone marrow or kidney, so its role here may reflect shared proliferative machinery, cell composition, or indirect co-regulation rather than a tissue-specific function.

## Module 12

**Tissue pair**: bone_marrow and kidney  
**Genes (23)**: ARFIP2, CCNH, DHX37, DHX8, EED, GIGYF2, LRRC20, MESD, NBN, NCOA2, NIPBL, PPP4R2, PRRC2B, RFC4, RNASEH2A, SIN3A, SMNDC1, SUPT5H, STRN, TASOR, GTF2H4, ZC3HAV1, ZNF598

### Function

The strongest supported interpretation is a nuclear gene-regulatory and genome-maintenance module. The only globally corrected GO/KEGG result is (GO:CC nuclear protein-containing complex; q_global = 0.0393), nuclear protein-containing complex, which includes CCNH, DHX37, DHX8, EED, GTF2H4, NBN, NCOA2, NIPBL, RFC4, SIN3A, SMNDC1 and SUPT5H. The gene annotations support several related processes: RNA splicing and processing through DHX8, DHX37 and SMNDC1; RNA polymerase transcription initiation or elongation through GTF2H4, CCNH and SUPT5H; chromatin repression and transcriptional regulation through EED, SIN3A, NIPBL and TASOR; and DNA replication, repair or checkpoint control through RFC4, RNASEH2A, NBN, PPP4R2 and GTF2H4. The module therefore appears to represent coordinated expression of nuclear complexes involved in RNA maturation, transcriptional control, chromatin regulation and genome integrity, rather than a narrowly defined pathway. There were no STRING functional-enrichment terms, so STRING does not provide an additional enriched biological process.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the genes are predominantly intracellular, with nuclear or cytosolic localizations and only one gene annotated in the secretome. HPA reports low tissue specificity for most genes, and low immune-cell specificity for nearly the entire module. Several genes are cell-type enhanced in neutrophils or progenitor populations, but the module is not specifically enriched for blood cells according to the supplied HPA summary. Protein detection is present for many genes in both bone marrow and kidney, while several genes are absent or lack data in one or both tissues. Thus, shared abundance may partly reflect broadly expressed housekeeping-like nuclear functions, general proliferative or biosynthetic state, and possibly shared cellular composition, rather than a tissue-specific bone-marrow or kidney function. The HPA evidence does not support interpreting it as a circulating or secreted protein signal.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC nuclear protein-containing complex | 0.0393 | CCNH, DHX37, DHX8, EED, GTF2H4, NBN, NCOA2, NIPBL, RFC4, SIN3A, SMNDC1, SUPT5H |

### STRING and hu.MAP

The high-confidence STRING evidence is limited but biologically coherent. Known relationships include CCNH with GTF2H4 and SUPT5H, GIGYF2 with ZNF598, NBN with RFC4, PPP4R2 with SUPT5H, and RFC4 with RNASEH2A. These links connect transcription initiation or elongation, translation surveillance, and DNA repair or replication. The supplied STRING functional-enrichment result is empty, so these interactions should be treated as supporting relationships rather than a globally enriched pathway. hu.MAP independently places CCNH and GTF2H4 together in several TFIIH-related complexes, GIGYF2 and ZNF598 together in translation- and RNA-associated complexes, and EED and SIN3A together in chromatin or transcriptional-repression complexes. Most of each hu.MAP complex lies outside the module, indicating that the module captures selected components of established larger complexes rather than complete complexes. The network is therefore partly anchored by known molecular machinery, with many co-abundance links not directly supported by the supplied STRING or hu.MAP records.

**STRING interactions (score >= 0.7)**: 6 of 253 gene pairs: CCNH–GTF2H4 (0.999); CCNH–SUPT5H (0.84); GIGYF2–ZNF598 (0.973); NBN–RFC4 (0.906); PPP4R2–SUPT5H (0.814); RFC4–RNASEH2A (0.728)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05174.1 (CCNH, GTF2H4; 2/11); huMAP3_09908.1 (CCNH, GTF2H4; 2/13); huMAP3_12429.1 (CCNH, GTF2H4; 2/13); huMAP3_10307.1 (GIGYF2, ZNF598; 2/20); huMAP3_14270.1 (GIGYF2, ZNF598; 2/47); huMAP3_14559.1 (GIGYF2, ZNF598; 2/47); huMAP3_13482.1 (EED, SIN3A; 2/50); huMAP3_15128.1 (EED, SIN3A; 2/96)

### Novelty

The module should not be called a newly discovered molecular complex. Several of its relationships and gene pairs are already represented in STRING or hu.MAP, especially the TFIIH-related CCNH–GTF2H4 relationship, the GIGYF2–ZNF598 translation-surveillance relationship, the EED–SIN3A chromatin relationship, and the NBN–RFC4 or RFC4–RNASEH2A genome-maintenance relationships. At the same time, the specific conserved co-abundance organization across bone marrow and kidney may be a new observation, because the fact sheet does not establish that this tissue-pair module has previously been reported. Absence of a relationship from STRING or hu.MAP is not evidence of novelty. The defensible conclusion is that the module may represent a novel cross-tissue co-abundance pattern assembled from largely established nuclear components, but its novelty requires comparison with published co-expression studies and independent cohorts.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular program that coordinates nuclear RNA processing with transcription, chromatin regulation and DNA replication or repair in cells present in both tissues. DHX8 may act as a network bridge linking RNA-processing state to multiple nuclear processes; CCNH and GTF2H4 may report TFIIH-linked transcription and nucleotide-excision-repair activity; EED and SIN3A may impose chromatin-level regulation; and RFC4, NBN and RNASEH2A may couple the program to replication-associated genome surveillance. The co-abundance signal could therefore arise when cellular demand for transcription, RNA maturation and genome maintenance changes together. This is a mechanistic model, not a demonstrated physical assembly or causal pathway, and it should be tested with cell-resolved data, perturbation experiments and replication in independent bone-marrow and kidney cohorts.

### Important genes

#### DHX8

- **Related proteins** (co-abundance neighbors): SMNDC1 (0.88), RFC4 (0.86), ZC3HAV1 (0.85), EED (0.83), RNASEH2A (0.83), GIGYF2 (0.82), TASOR (0.82), NBN (0.81), DHX37 (0.81), SIN3A (0.81), ZNF598 (0.81), SUPT5H (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAH-box helicase 8. This gene is a member of the DEAH box polypeptide family. The encoded protein contains the DEAH (Asp-Glu-Ala-His) motif which is characteristic of all DEAH box proteins, and is thought to function as an ATP-dependent RNA helicase that regulates the release of spliced mRNAs from spliceosomes prior to their export from the nucleus. This protein may be required for the replication of human immunodefi…
- **Diseases (Open Targets)**: congenital anomaly of kidney and urinary tract (0.259); neurodegenerative disease (0.193); upper extremity fracture (0.118); lens disorder (0.064); exudative vitreoretinopathy (0.048)
- **Europe PMC papers**: 360
- **Why important**: DHX8 has the strongest network position in the supplied module and connects to genes spanning RNA processing, chromatin, transcription and genome maintenance. Its annotation identifies an ATP-dependent DEAH-box RNA helicase involved in release of spliced mRNA from spliceosomes, and it is present in the only globally corrected term, (GO:CC nuclear protein-containing complex; q_global = 0.0393). It is detected by HPA in both tissues, has low tissue and cell-type specificity, and has a substantial literature base. Its disease associations include congenital anomaly of the kidney and urinary tract and neurodegenerative disease.
- **Conclusion**: Established: DHX8 is a broadly expressed nuclear RNA-processing factor and a central co-abundance connector in this module. Hypothesis: it may coordinate RNA maturation with the other nuclear programs represented here. The network position supports this as a priority candidate, but does not prove that DHX8 physically regulates the other module genes.

#### CCNH

- **Related proteins** (co-abundance neighbors): DHX37 (0.83); STRING partners: GTF2H4 (0.999), SUPT5H (0.84)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_05174.1, huMAP3_09908.1, huMAP3_12429.1
- **Function (MyGene.info)**: cyclin H. The protein encoded by this gene belongs to the highly conserved cyclin family, whose members are characterized by a dramatic periodicity in protein abundance through the cell cycle. Cyclins function as regulators of CDK kinases. Different cyclins exhibit distinct expression and degradation patterns which contribute to the temporal coordination of each mitotic event. This cyclin forms a complex wi…
- **Diseases (Open Targets)**: capillary malformation-arteriovenous malformation 1 (0.700); HIV infectious disease (0.593); capillary malformation-arteriovenous malformation syndrome (0.557); Abnormality of the cardiovascular system (0.543); angioosteohypertrophic syndrome (0.499)
- **Europe PMC papers**: 986
- **Why important**: CCNH is a component of the CDK7–MAT1-associated transcription and repair machinery and is included in (GO:CC nuclear protein-containing complex; q_global = 0.0393). Its STRING relationship with GTF2H4 is exceptionally strong in the supplied evidence, and CCNH and GTF2H4 recur together in several hu.MAP TFIIH-related complexes. CCNH also connects in STRING to SUPT5H. It is associated with transcription initiation, nucleotide-excision repair and cell-cycle regulation, and has a substantial literature base.
- **Conclusion**: Established: CCNH anchors a known TFIIH-related transcription and repair component of the module. Hypothesis: its co-abundance may mark coordinated transcriptional and genome-maintenance demand across the two tissues. The module data do not establish a tissue-specific role for CCNH.

#### NCOA2

- **Related proteins** (co-abundance neighbors): NIPBL (0.90), ARFIP2 (0.87), SIN3A (0.87), PRRC2B (0.86), MESD (0.85), PPP4R2 (0.84), STRN (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nuclear receptor coactivator 2. The protein encoded by this gene functions as a transcriptional coactivator for nuclear hormone receptors, including steroid, thyroid, retinoid, and vitamin D receptors. The encoded protein acts as an intermediary factor for the ligand-dependent activity of these nuclear receptors, which regulate their target genes upon binding of cognate response elements. This gene has been found to be involved …
- **Diseases (Open Targets)**: atrial fibrillation (0.491); uterine corpus leiomyoma (0.438); mesenchymal chondrosarcoma (0.381); pancreatic ductal adenocarcinoma (0.372); lung carcinoma (0.371)
- **Europe PMC papers**: 2860
- **Why important**: NCOA2 has a prominent network position and links to NIPBL, SIN3A, PPP4R2 and other module genes. It is a nuclear coactivator for steroid, thyroid, retinoid and vitamin D receptors, placing it at the interface of transcriptional regulation and hormone-responsive biology. It is cell-type enhanced in neutrophil progenitors and neutrophils, while HPA otherwise indicates low tissue specificity. Its disease associations include atrial fibrillation, uterine leiomyoma, mesenchymal chondrosarcoma and pancreatic ductal adenocarcinoma, and it has a large literature base.
- **Conclusion**: Established: NCOA2 is a transcriptional coactivator and a network connector linking regulatory and signaling-related components. Hypothesis: it may help explain why a broadly expressed nuclear module is conserved between bone marrow and kidney, potentially through shared hormone-responsive or differentiation-related states. This tissue-level interpretation remains unproven.

#### GIGYF2

- **Related proteins** (co-abundance neighbors): DHX8 (0.82); STRING partners: ZNF598 (0.973)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_10307.1, huMAP3_14270.1, huMAP3_14559.1
- **Function (MyGene.info)**: GRB10 interacting GYF protein 2. This gene contains CAG trinucleotide repeats and encodes a protein containing several stretches of polyglutamine residues. The encoded protein may be involved in the regulation of tyrosine kinase receptor signaling. This gene is located in a chromosomal region that was genetically linked to Parkinson disease type 11, and mutations in this gene were thought to be causative for this disease. However…
- **Diseases (Open Targets)**: neurodegenerative disease (0.528); Leber congenital amaurosis 16 (0.525); schizophrenia (0.397); Parkinson disease (0.390); snowflake vitreoretinal degeneration (0.375)
- **Europe PMC papers**: 832
- **Why important**: GIGYF2 links the module's central DHX8-associated neighborhood to ZNF598, with the pair supported by a strong STRING relationship and by several hu.MAP complexes. GIGYF2 is annotated in negative regulation of translation, mRNA destabilization and negative regulation of type I interferon signaling. It is detected in kidney, has low tissue specificity, and has disease associations including neurodegenerative disease, Leber congenital amaurosis and Parkinson disease. Its literature base is meaningful but smaller than that of the major chromatin and DNA-repair genes.
- **Conclusion**: Established: GIGYF2 participates in translation control and is paired with the ribosome-surveillance E3 ligase ZNF598 in the supplied interaction and complex data. Hypothesis: this pair may connect translational quality control to the nuclear RNA-processing state represented by the module. The co-abundance network alone cannot establish that this connection is mechanistic.

#### NBN

- **Related proteins** (co-abundance neighbors): DHX8 (0.81); STRING partners: RFC4 (0.906)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nibrin. Mutations in this gene are associated with Nijmegen breakage syndrome, an autosomal recessive chromosomal instability syndrome characterized by microcephaly, growth retardation, immunodeficiency, and cancer predisposition. The encoded protein is a member of the MRE11/RAD50 double-strand break repair complex which consists of 5 proteins. This gene product is thought to be involved in DNA double-str…
- **Diseases (Open Targets)**: Nijmegen breakage syndrome (0.822); aplastic anemia (0.720); acute lymphoblastic leukemia (0.676); breast cancer (0.611); hereditary neoplastic syndrome (0.577)
- **Europe PMC papers**: 5207
- **Why important**: NBN is a genome-integrity factor in the MRE11–RAD50 repair machinery, involved in double-strand-break repair and damage-induced checkpoint activation. It is included in (GO:CC nuclear protein-containing complex; q_global = 0.0393), connects to DHX8 in the co-abundance graph, and has a strong STRING relationship with RFC4. HPA detects it in both tissues and reports cell-type enhancement in neutrophils, adipocytes and cardiomyocytes. Its disease associations include Nijmegen breakage syndrome, aplastic anemia and acute lymphoblastic leukemia, and it has a large literature base.
- **Conclusion**: Established: NBN provides a well-supported genome-maintenance anchor and links the module to DNA-damage response. Hypothesis: its coordinated abundance with RNA-processing and transcription factors may reflect coupling between RNA production and genome surveillance in proliferative or stressed cells. The data do not show that NBN drives the cross-tissue module.

## Module 13

**Tissue pair**: bone_marrow and kidney  
**Genes (6)**: ATP1A1, ATP5PB, ETFA, PHB2, PRDX3, SDHA

### Function

The module is most consistent with mitochondrial energy metabolism, electron transfer, oxidative phosphorylation, and protection from mitochondrial oxidative stress, with ATP1A1 adding a plasma-membrane ion-gradient and epithelial transport component. SDHA links respiratory-chain metabolism with the central part of the co-abundance subgraph; PRDX3 links this region to mitochondrial antioxidant defense; ETFA connects electron transfer with fatty-acid and amino-acid catabolism; ATP5PB supports the oxidative-phosphorylation interpretation; PHB2 contributes mitochondrial membrane organization and quality-control biology. The module has a connected chain-like structure rather than a dense interaction cluster. No GO or KEGG term passed global correction, so this functional interpretation is based on the concordance of individual gene annotations and network organization rather than statistically significant enrichment.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the genes are intracellular or membrane-associated and none is annotated as secreted. It is also not blood-cell enriched according to HPA, because every member has low immune-cell specificity and no blood-cell enrichment is reported. All members show cell-type enhancement, while the tissue patterns include skeletal muscle, tongue, parathyroid gland, liver, and heart muscle, with some genes having low tissue specificity. Protein detection is present for nearly the entire module in bone marrow and for the entire module in kidney. The shared signal therefore does not specifically point to a blood-cell program or a kidney-specific program; it may reflect mitochondrial and transport activity shared by metabolically active cells or shared cellular components in the sampled tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports two high-confidence pairwise relationships within the module: SDHA with ATP5PB and SDHA with ETFA. These relationships provide external support for a respiratory-chain and mitochondrial-energy interpretation, especially around SDHA. STRING reports no functional-enrichment result for the module. hu.MAP reports no complex containing at least two module members, so the module is not independently supported as a known multi-protein complex by that resource. The absence of hu.MAP complexes does not negate co-abundance, but it indicates that the module is better viewed as a cross-process mitochondrial and membrane-transport association than as a single established complex.

**STRING interactions (score >= 0.7)**: 2 of 15 gene pairs: ATP5PB–SDHA (0.755); ETFA–SDHA (0.706)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The individual biology is established: SDHA, ETFA, ATP5PB, PRDX3, and PHB2 are recognized mitochondrial or mitochondrial-associated proteins, while ATP1A1 is a well-established ion transporter. The STRING-supported relationships are also known relationships, so the module is not a wholly novel molecular mechanism. The potentially new aspect is the tissue-pair co-abundance organization linking ion transport, respiratory metabolism, antioxidant defense, fatty-acid electron transfer, and prohibitin-associated mitochondrial biology in bone marrow and kidney. That observation should be treated as a candidate systems-level finding rather than a proven discovery, because there is no globally significant GO/KEGG enrichment, no hu.MAP complex support, and no evidence here that the exact module has been independently reproduced.

**Hypothesis.** Hypothesis: the module represents a shared cellular program in which mitochondrial respiratory capacity and substrate-derived electron transfer are coordinated with antioxidant protection and membrane ion-gradient maintenance. In this model, SDHA and ATP5PB mark respiratory-chain and ATP-synthesis capacity, ETFA supplies or transfers electrons from oxidative substrate metabolism, PRDX3 limits mitochondrial peroxide stress, PHB2 supports mitochondrial membrane organization and quality control, and ATP1A1 maintains the sodium and potassium gradients required for epithelial transport and cellular homeostasis. The co-abundance pattern could therefore arise from metabolically active kidney and bone-marrow-associated cells rather than from a secreted or immune-cell program. This remains a hypothesis and requires validation with cell-resolved expression, protein abundance, and perturbation data.

### Important genes

#### SDHA

- **Related proteins** (co-abundance neighbors): ATP1A1 (0.84), PRDX3 (0.81); STRING partners: ATP5PB (0.755), ETFA (0.706)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate dehydrogenase complex flavoprotein subunit A. This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identi…
- **Diseases (Open Targets)**: mitochondrial complex II deficiency, nuclear type 1 (0.813); pheochromocytoma/paraganglioma syndrome 5 (0.790); dilated cardiomyopathy 1GG (0.768); neurodegeneration with ataxia and late-onset optic atrophy (0.761); gastrointestinal stromal tumor (0.743)
- **Europe PMC papers**: 12756
- **Why important**: SDHA is a central connector in the module, linking ATP1A1 and PRDX3 in the co-abundance graph and also forming the two STRING-supported relationships with ATP5PB and ETFA. Its established role as a catalytic subunit of succinate dehydrogenase directly connects the module to the tricarboxylic acid cycle and respiratory electron transport. It has extensive literature support and disease associations involving mitochondrial complex deficiencies, cardiomyopathy, neurodegeneration, and tumor predisposition.
- **Conclusion**: Established evidence supports SDHA as the strongest metabolic anchor of the module. It is reasonable to interpret its co-abundance with the neighboring mitochondrial genes as evidence of coordinated respiratory biology, but the data do not establish that SDHA mechanistically regulates the other members.

#### PRDX3

- **Related proteins** (co-abundance neighbors): ETFA (0.83), SDHA (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Mitochondria; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peroxiredoxin 3. This gene encodes a mitochondrial protein with antioxidant function. The protein is similar to the C22 subunit of Salmonella typhimurium alkylhydroperoxide reductase, and it can rescue bacterial resistance to alkylhydroperoxide in E. coli that lack the C22 subunit. The human and mouse genes are highly conserved, and they map to the regions syntenic between mouse and human chromosomes. Sequence com…
- **Diseases (Open Targets)**: spinocerebellar ataxia, autosomal recessive 32 (0.653); corneal dystrophy, punctiform and polychromatic pre-descemet (0.571); autosomal recessive cerebellar ataxia (0.268); neurodegenerative disease (0.257); hereditary disease (0.191)
- **Europe PMC papers**: 2613
- **Why important**: PRDX3 occupies a bridging position between SDHA and ETFA and supplies a direct oxidative-stress interpretation. Its established mitochondrial antioxidant function and annotations involving response to oxidative stress, mitochondrion organization, and myeloid-cell differentiation make it relevant to both metabolic protection and the bone-marrow context. It also has substantial literature support and disease associations involving neurological and hereditary disorders.
- **Conclusion**: Established evidence supports PRDX3 as a mitochondrial redox-protection component. Its position suggests that oxidative-stress control may be coordinated with respiratory and substrate oxidation activity, but that coordination is a hypothesis rather than a demonstrated causal relationship.

#### ETFA

- **Related proteins** (co-abundance neighbors): PRDX3 (0.83), PHB2 (0.80); STRING partners: SDHA (0.706)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein subunit alpha. ETFA participates in catalyzing the initial step of the mitochondrial fatty acid beta-oxidation. It shuttles electrons between primary flavoprotein dehydrogenases and the membrane-bound electron transfer flavoprotein ubiquinone oxidoreductase. Defects in electron-transfer-flavoprotein have been implicated in type II glutaricaciduria in which multiple acyl-CoA dehydrogenase deficiencies result in l…
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.834); glutaric aciduria (0.756); hereditary disease (0.469); multiple acyl-CoA dehydrogenase deficiency, mild type (0.370); multiple acyl-CoA dehydrogenase deficiency, severe neonatal type (0.370)
- **Europe PMC papers**: 1433
- **Why important**: ETFA connects PRDX3 to PHB2 and is additionally supported by the STRING relationship with SDHA. Its established function in electron transfer from fatty-acid and other acyl-CoA dehydrogenases links the module to substrate oxidation beyond the tricarboxylic acid cycle. It has disease associations with multiple acyl-CoA dehydrogenase deficiency and glutaric aciduria, providing strong functional and clinical relevance.
- **Conclusion**: Established evidence supports ETFA as the module component connecting mitochondrial electron transfer with fatty-acid and amino-acid catabolism. The module may coordinate substrate oxidation with antioxidant defense, but the co-abundance data alone cannot determine whether ETFA activity drives the broader pattern.

#### ATP1A1

- **Related proteins** (co-abundance neighbors): SDHA (0.84), ATP5PB (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 is one of the most connected genes in the module and links SDHA with ATP5PB. Its established plasma-membrane Na/K-ATPase function provides the module with an ion-homeostasis and epithelial-transport dimension that complements the mitochondrial genes. HPA places it in kidney-relevant distal convoluted tubule cells and reports kidney protein detection, while disease associations include inherited neurological, electrolyte, and cardiac conditions. Its literature support is extensive.
- **Conclusion**: Established evidence supports ATP1A1 as the membrane-transport component of the module and makes a kidney-relevant transport interpretation plausible. Its connection to the mitochondrial genes may reflect shared energetic demand or coordinated cell-state regulation, but a direct molecular link is not established here.

#### ATP5PB

- **Related proteins** (co-abundance neighbors): ATP1A1 (0.82); STRING partners: SDHA (0.755)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP synthase peripheral stalk-membrane subunit b. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: deficiency anemia (0.178); ocular hypotension (0.038); myasthenia gravis (0.022); ulcerative colitis (0.016); nonpapillary renal cell carcinoma (0.012)
- **Europe PMC papers**: 302
- **Why important**: ATP5PB is connected to ATP1A1 and has the strongest external STRING-supported relationship with SDHA in the module. Its established role as a subunit of mitochondrial ATP synthase provides direct support for oxidative phosphorylation and proton-motive-force-driven ATP production. Although its literature volume and disease evidence are more limited than those of SDHA or ATP1A1, its functional placement is highly informative.
- **Conclusion**: Established evidence supports ATP5PB as an oxidative-phosphorylation marker within the module. Its co-abundance with ATP1A1 may reflect the energetic requirements of ion pumping, but this proposed coupling remains a hypothesis.

## Module 14

**Tissue pair**: bone_marrow and kidney  
**Genes (5)**: ATAD3A, GIT1, RAB34, SLX9, SPG21

### Function

This is a small, weakly connected co-abundance module without a demonstrated canonical pathway. No GO or KEGG term passed global correction, so there is no globally significant GO/KEGG functional enrichment to support a specific pathway assignment. There are also no supplementary supplementary STRING terms and no STRING functional enrichment. The network is organized around SPG21, which is co-abundant with SLX9, GIT1, and ATAD3A, while GIT1 is also co-abundant with RAB34. The gene annotations point to several intracellular processes rather than a single established function: SPG21 relates to CD4 and T-cell signaling, GIT1 to ARF regulation, microtubule nucleation and cytokinesis, SLX9 to ribosome biogenesis, RAB34 to Golgi, lysosome, cilium and macropinocytosis biology, and ATAD3A to mitochondrial organization and cellular growth. Taken together, the safest interpretation is a mixed intracellular cell-state module involving vesicular and cytoskeletal organization, organelle maintenance, and cellular biosynthetic activity, rather than a validated unified pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: every member is annotated as non-secreted and intracellular. Most members have low tissue specificity, while all have some cell-type-enhanced HPA expression. The enhanced cell types are heterogeneous and include reproductive, epithelial, stromal, neural-related, and immune-associated populations. RAB34 shows group-enriched expression across several myeloid and dendritic blood-cell populations, and SPG21 has immune-cell enhancement in neutrophils, but the module as a whole is not uniformly blood-cell specific. All proteins are detected in both bone marrow and kidney. Thus, the shared signal could reflect broadly expressed intracellular programs, shared cell types, or sample cellular composition rather than a tissue-specific biological mechanism. The HPA evidence does not support a secreted-protein or simple plasma-protein explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The co-abundance network contains edges among the module genes, with SPG21 as the most connected node and GIT1 linking toward RAB34. However, none of the possible within-module gene pairs is represented by a high-confidence STRING interaction, and no hu.MAP complex contains multiple module members. Therefore, the network edges should be interpreted as coordinated abundance patterns, not as established physical interactions or membership in a known multiprotein complex. The absence of STRING and hu.MAP support argues against claiming a pre-existing molecular complex, while it does not invalidate the reproducible co-abundance pattern.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a new tissue-pair co-abundance observation, but the data do not establish a new biological mechanism or molecular complex. Its novelty is supported only in the limited sense that the module is not represented as a shared high-confidence STRING interaction set or a multi-member hu.MAP complex. Those database absences cannot by themselves prove biological novelty, because the genes may be co-regulated without directly interacting and database coverage is incomplete. The lack of globally significant GO or KEGG enrichment and the heterogeneous annotations make a strong claim of pathway-level novelty premature. A genuine novel module would require replication, preservation testing, and experiments or orthogonal datasets linking its members mechanistically.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular state present in selected bone-marrow and kidney cell populations, in which organelle trafficking, cytoskeletal organization, mitochondrial maintenance, ribosome production, and immune-related signaling vary together. A possible organizing relationship is that SPG21-associated vesicular or receptor-signaling regulation covaries with GIT1-mediated cytoskeletal and ARF-related processes, while RAB34 contributes endolysosomal and ciliary trafficking and ATAD3A contributes mitochondrial organization. SLX9 may mark accompanying biosynthetic demand rather than a direct interaction with the other proteins. This is a hypothesis only: the lack of globally significant GO/KEGG terms, STRING interactions, and hu.MAP complexes prevents treating this proposed mechanism as established.

### Important genes

#### SPG21

- **Related proteins** (co-abundance neighbors): SLX9 (0.87), GIT1 (0.83), ATAD3A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SPG21 abhydrolase domain containing, maspardin. The protein encoded by this gene binds to the hydrophobic C-terminal amino acids of CD4 which are involved in repression of T cell activation. The interaction with CD4 is mediated by the noncatalytic alpha/beta hydrolase fold domain of this protein. It is thus proposed that this gene product modulates the stimulatory activity of CD4. Mutations in this gene are associated with autosomal recessive s…
- **Diseases (Open Targets)**: mast syndrome (0.746); hereditary sensory and autonomic neuropathy with spastic paraplegia (0.503); hereditary spastic paraplegia (0.494); hereditary spastic paraplegia 5A (0.370); alcohol drinking (0.228)
- **Europe PMC papers**: 263
- **Why important**: SPG21 is the central network node, connecting SLX9, GIT1, and ATAD3A. Its annotated CD4-binding and proposed modulation of T-cell activation provide the clearest immune-signaling link in the module, and it is associated with hereditary spastic paraplegia phenotypes. Its literature base is smaller than that of GIT1 but sufficient to support a disease-relevant, mechanistically interesting role.
- **Conclusion**: Established evidence supports SPG21 as the network anchor and as a regulator associated with CD4-related signaling and spastic paraplegia. It is plausible, but unproven, that SPG21 helps organize the shared intracellular state represented by this module.

#### GIT1

- **Related proteins** (co-abundance neighbors): RAB34 (0.86), SPG21 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GIT ArfGAP 1. Enables gamma-tubulin binding activity. Involved in positive regulation of microtubule nucleation and regulation of cytokinesis. Located in several cellular components, including focal adhesion; microtubule cytoskeleton; and mitochondrion. Implicated in attention deficit hyperactivity disorder. Biomarker of Huntington's disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.323); coronary artery disorder (0.237); hereditary disease (0.193); low tension glaucoma (0.173); venous thromboembolism (0.142)
- **Europe PMC papers**: 1678
- **Why important**: GIT1 is the second network connector, linking SPG21 with RAB34. Its functions in ARF signaling, gamma-tubulin binding, microtubule nucleation, cytokinesis, and focal-adhesion biology provide a plausible bridge between trafficking and cytoskeletal organization. It also has the largest literature volume in the module and disease associations extending into neurological and vascular phenotypes.
- **Conclusion**: Established evidence supports GIT1 as a multifunctional regulator of cytoskeletal, trafficking, and cell-division processes. Its position makes it a strong candidate for coordinating the module, but co-abundance alone does not show that it physically regulates the other members in these tissues.

#### RAB34

- **Related proteins** (co-abundance neighbors): GIT1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Nucleoplasm, Primary cilium; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB34, member RAS oncogene family. This gene encodes a protein belonging to the RAB family of proteins, which are small GTPases involved in protein transport. This family member is a Golgi-bound member of the secretory pathway that is involved in the repositioning of lysosomes and the activation of macropinocytosis. Alternative splicing of this gene results in multiple transcript variants. An alternatively spliced transcript varian…
- **Diseases (Open Targets)**: orofaciodigital syndrome 20 (0.605); Jeune syndrome (0.341); orofaciodigital syndrome (0.185); neurodegenerative disease (0.175); glioma (0.085)
- **Europe PMC papers**: 632
- **Why important**: RAB34 is the module's trafficking-related terminal node connected to GIT1. Its established annotation as a Golgi-associated small GTPase involved in lysosome positioning, macropinocytosis, cilium assembly, and antigen processing gives the module a concrete membrane-trafficking component. Its blood-cell pattern, especially across myeloid and dendritic populations, also makes it important for evaluating cell-composition effects.
- **Conclusion**: Established evidence supports RAB34 as a regulator of intracellular trafficking and as a marker potentially influenced by immune-cell composition. It may connect the module to endolysosomal or antigen-processing activity, but the module does not demonstrate that this activity is shared across all member genes.

#### ATAD3A

- **Related proteins** (co-abundance neighbors): SPG21 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase family AAA domain containing 3A. This gene encodes a ubiquitously expressed mitochondrial membrane protein that contributes to mitochondrial dynamics, nucleoid organization, protein translation, cell growth, and cholesterol metabolism. This gene is a member of the ATPase family AAA-domain containing 3 gene family which, in humans, includes two other paralogs. Naturally occurring mutations in this gene are associated with distinct…
- **Diseases (Open Targets)**: Harel-Yoon syndrome (0.824); pontocerebellar hypoplasia, hypotonia, and respiratory insufficiency syndrome, neonatal lethal (0.785); lactic acidosis (0.462); hereditary disease (0.418); isolated cerebellar hypoplasia/agenesis (0.342)
- **Europe PMC papers**: 879
- **Why important**: ATAD3A is connected directly to SPG21 and contributes a mitochondrial dimension absent from the other annotations. Its functions include mitochondrial dynamics, nucleoid organization, protein translation, cell growth, cholesterol metabolism, and apoptosis-related regulation. Its disease associations include severe neurological and mitochondrial phenotypes, making it biologically consequential despite its peripheral network position.
- **Conclusion**: Established evidence supports ATAD3A as a mitochondrial membrane protein important for organelle organization and cellular homeostasis. Its co-abundance with SPG21 may indicate coordinated organelle or stress-state regulation, but that relationship remains a hypothesis.

#### SLX9

- **Related proteins** (co-abundance neighbors): SPG21 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SLX9 ribosome biogenesis factor. Predicted to be involved in maturation of SSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Predicted to be located in nucleolus. Predicted to be part of 90S preribosome and preribosome, small subunit precursor. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: alcohol drinking (0.347); Vertigo (0.221); suppurative periapical periodontitis (0.217); spontaneous coronary artery dissection (0.176); amyotrophic lateral sclerosis (0.132)
- **Europe PMC papers**: 71
- **Why important**: SLX9 is directly connected to SPG21 and supplies the module's ribosome-biogenesis annotation. Its predicted role in small-subunit ribosomal RNA maturation and the nucleolar pre-ribosome makes it relevant to biosynthetic capacity and cell proliferation. Although its literature volume is limited and its network position is peripheral, it could distinguish a general cellular-state signal from a purely trafficking or immune module.
- **Conclusion**: Established evidence supports SLX9 as a predicted ribosome-biogenesis factor located in the nucleolus. Its inclusion may reflect coordinated biosynthetic demand, but its contribution to the shared bone-marrow and kidney module is uncertain and requires experimental validation.

## Module 15

**Tissue pair**: bone_marrow and kidney  
**Genes (36)**: BAG2, CAPRIN1, CBX5, CRBN, DDX21, DHX9, ADAR, EXOSC2, GMPS, HACL1, HNRNPL, HNRNPR, INTS14, LARP7, LMNB1, LMNB2, MATR3, NEK7, NHLRC2, NOP2, NOP56, PSMC4, PSMC2, PSIP1, PTCD3, ADSL, RCC1L, MRPS35, SETD2, SUPT16H, FARSB, TBC1D23, WRAP53, THOC1, TIAL1, ATP6V0A1

### Function

The best-supported function is coordinated RNA metabolism, centered on RNA binding and RNA-protein complex biology (GO:MF RNA binding; q_global = 0.00948). The module contains RNA helicases and RNA-binding proteins, spliceosome and mRNA-processing factors, nucleolar and ribosome-biogenesis proteins, RNA-editing machinery, mitochondrial RNA and translation components, and transcription or RNA-export regulators. The network supports a connected RNA-processing core: ADAR, DDX21, DHX9, HNRNPL, HNRNPR, MATR3, NOP2, NOP56, LARP7, CAPRIN1, EXOSC2, PTCD3, RCC1L, and related genes. The STRING results independently reinforce RNA binding (STRING Keyword RNA-binding; within-query FDR = 0.00022) (STRING Function RNA binding; within-query FDR = 0.0084), while the hu.MAP results support assemblies involving heterogeneous nuclear ribonucleoproteins (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1), mitochondrial RNA or ribosome-associated proteins (hu.MAP huMAP3_05807.1) (hu.MAP huMAP3_03554.1) (hu.MAP huMAP3_05954.1), and additional nuclear-envelope, proteasome, and purine-metabolism assemblies. Thus, this is most plausibly a broad RNA-processing and gene-expression module rather than a narrowly tissue-specific pathway. Transcriptional elongation and chromatin regulation are plausible subsidiary themes through SUPT16H, SETD2, PSIP1, THOC1, LARP7, and CBX5, but they are not independently established by a globally corrected GO/KEGG term. No other GO/KEGG term passed global correction; the STRING terms remain supplementary evidence.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most proteins have low tissue specificity, and the proteins are detected in both bone marrow and kidney, which supports a broadly expressed intracellular program rather than a secreted-tissue signature. Most genes also have low immune-cell specificity, so the module is not convincingly a blood-cell marker module. However, several genes show cell-type-enhanced patterns involving erythrocyte progenitors, megakaryocyte progenitors, neutrophils, basophils, platelets, or other hematopoietic-associated cells, and LMNB1 is tissue-enhanced in bone marrow and lymphoid tissue. Therefore, shared cellular composition or hematopoietic representation in the samples could contribute to the cross-tissue co-abundance. The kidney signal should not be interpreted as evidence that the module is kidney-specific, especially because several genes are not detected in bone marrow or kidney in HPA while the overall module is broadly intracellular.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF RNA binding | 0.00948 | ADAR, CAPRIN1, DDX21, DHX9, EXOSC2, FARSB, HNRNPL, HNRNPR, LARP7, MATR3, MRPS35, NOP2, NOP56, PSIP1, PTCD3, RCC1L, SUPT16H, THOC1, TIAL1, WRAP53 |

### STRING and hu.MAP

STRING provides established or database-supported relationships within the module, especially the ADAR-DHX9, DDX21-DHX9, DDX21-NOP2, DDX21-NOP56, DHX9-HNRNPL, DHX9-HNRNPR, HNRNPL-HNRNPR, HNRNPL-MATR3, and NOP2-NOP56 connections. It also supports the LMNB1-LMNB2 pair, the MRPS35-PTCD3 pair, the PSMC2-PSMC4 proteasome pair, the ADSL-GMPS metabolic pair, and links between SETD2, SUPT16H, and RNA-associated proteins. These relationships mean that much of the module recapitulates known molecular biology rather than representing unexplained pairings. hu.MAP independently supports a heterogeneous nuclear ribonucleoprotein and RNA-editing assembly containing HNRNPR, HNRNPL, MATR3, and ADAR (hu.MAP huMAP3_10625.1), with additional support for smaller hnRNP assemblies (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1). It also supports mitochondrial or ribosome-associated groupings involving MRPS35, PTCD3, and LARP7 (hu.MAP huMAP3_05807.1) (hu.MAP huMAP3_03554.1) (hu.MAP huMAP3_05954.1), the lamin pair (hu.MAP huMAP3_03501.1) (hu.MAP huMAP3_00325.1) (hu.MAP huMAP3_13519.1) (hu.MAP huMAP3_10433.1) (hu.MAP huMAP3_09259.1) (hu.MAP huMAP3_10492.1) (hu.MAP huMAP3_10614.1), proteasome assemblies involving PSMC2 and PSMC4 (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1), and the ADSL-GMPS pair (hu.MAP huMAP3_14442.1). Because the module combines several supported complexes rather than mapping to one complete complex, its structure is more consistent with coordinated abundance of interacting RNA and gene-expression machinery than with a single physical complex.

**STRING interactions (score >= 0.7)**: 28 of 630 gene pairs: ADAR–DHX9 (0.922); ADSL–GMPS (0.913); CAPRIN1–DHX9 (0.705); CAPRIN1–TIAL1 (0.861); DDX21–DHX9 (0.908); DDX21–HNRNPR (0.73); DDX21–LARP7 (0.866); DDX21–NOP2 (0.761); DDX21–NOP56 (0.811); DHX9–HNRNPL (0.901); DHX9–HNRNPR (0.909); DHX9–LARP7 (0.74); DHX9–MATR3 (0.786); EXOSC2–NOP56 (0.78); FARSB–GMPS (0.727); GMPS–NOP56 (0.823); HNRNPL–HNRNPR (0.961); HNRNPL–MATR3 (0.757); HNRNPL–SETD2 (0.935); HNRNPR–LARP7 (0.817); HNRNPR–MATR3 (0.714); LARP7–NOP56 (0.755); LMNB1–LMNB2 (0.999); MRPS35–PTCD3 (0.999); NEK7–RCC1L (0.73); NOP2–NOP56 (0.969); PSMC2–PSMC4 (0.999); SETD2–SUPT16H (0.754)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword RNA-binding (FDR = 0.00022, 14 genes); TISSUES Leukemia cell (FDR = 0.0016, 16 genes); Function RNA binding (FDR = 0.0084, 20 genes); Keyword Isopeptide bond (FDR = 0.0196, 16 genes); Keyword Ubl conjugation (FDR = 0.0291, 17 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10625.1 (HNRNPR, HNRNPL, MATR3, ADAR; 4/57); huMAP3_07581.1 (HNRNPR, HNRNPL, MATR3; 3/21); huMAP3_05807.1 (MRPS35, LARP7, PTCD3; 3/81); huMAP3_03501.1 (LMNB1, LMNB2; 2/2); huMAP3_03554.1 (MRPS35, PTCD3; 2/2); huMAP3_00325.1 (LMNB1, LMNB2; 2/3); huMAP3_13519.1 (LMNB1, LMNB2; 2/4); huMAP3_10433.1 (LMNB1, LMNB2; 2/5); huMAP3_05721.1 (HNRNPL, MATR3; 2/6); huMAP3_07225.1 (HNRNPR, HNRNPL; 2/7); huMAP3_09259.1 (LMNB1, LMNB2; 2/8); huMAP3_10492.1 (LMNB1, LMNB2; 2/9); huMAP3_10614.1 (LMNB1, LMNB2; 2/9); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09654.1 (HNRNPR, HNRNPL; 2/13); huMAP3_10659.1 (HNRNPR, HNRNPL; 2/28); huMAP3_05954.1 (MRPS35, PTCD3; 2/28); huMAP3_05064.1 (PSMC2, PSMC4; 2/31); huMAP3_14270.1 (PSIP1, CAPRIN1; 2/47); huMAP3_14442.1 (ADSL, GMPS; 2/57); huMAP3_09656.1 (PSMC2, PSMC4; 2/64); huMAP3_13725.1 (PSMC2, PSMC4; 2/69)

### Novelty

The molecular functions represented here are not, by themselves, a new discovery: RNA binding, RNA helicase activity, heterogeneous nuclear ribonucleoprotein associations, nucleolar RNA processing, mitochondrial translation, lamin biology, and proteasome organization are already supported by STRING, hu.MAP, and the gene annotations. The potentially novel aspect is the conserved co-abundance of this combined program across bone marrow and kidney. That observation may be useful as a cross-tissue systems-level finding, but the supplied evidence does not establish that it is a previously unknown biological mechanism. Absence of a complete matching entry in STRING or hu.MAP would not prove novelty, because those resources represent physical or curated associations and may not capture tissue-pair co-abundance. A defensible novelty claim would require comparison with prior co-expression or co-abundance studies, replication in independent cohorts, and tests showing that the signal is not driven by shared cell composition or broadly expressed housekeeping genes.

**Hypothesis.** Hypothesis: the module represents a conserved cellular infrastructure program that couples RNA binding, RNA remodeling, RNA editing, splicing, export, nucleolar RNA maturation, translation, and proteostasis. In both bone marrow and kidney, cells with active transcriptional and translational demands may coordinately regulate this machinery. The hnRNP and RNA-editing core could organize transcript processing, DDX21 and DHX9 could remodel RNA and support nucleolar or transcription-associated events, NOP2 and NOP56 could support ribosome biogenesis, SUPT16H and LARP7 could connect RNA output to transcriptional elongation, and proteasome and mitochondrial components could maintain protein and energetic homeostasis. This is a mechanistic model, not a demonstrated causal pathway. It should be tested by examining whether module activity tracks cell state, proliferation, erythroid or myeloid composition, and coordinated RNA-processing or ribosome-biogenesis measurements independently of tissue source.

### Important genes

#### ADAR

- **Related proteins** (co-abundance neighbors): DDX21 (0.88), SUPT16H (0.87), FARSB (0.84), PSMC2 (0.84), GMPS (0.82); STRING partners: DHX9 (0.922)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_10625.1
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR is a central RNA-editing enzyme and is part of the globally significant RNA-binding term (GO:MF RNA binding; q_global = 0.00948). It occupies a connective position with DDX21, SUPT16H, FARSB, PSMC2, and GMPS, has a strong STRING relationship with DHX9, and is included in the hu.MAP RNA-associated assembly with HNRNPR, HNRNPL, and MATR3 (hu.MAP huMAP3_10625.1). Its established disease associations include Aicardi-Goutieres syndrome and dyschromatosis symmetrica hereditaria, and it has substantial literature support.
- **Conclusion**: Established evidence supports ADAR as an RNA-editing and RNA-processing anchor that links the hnRNP core to RNA helicase activity. It is reasonable to hypothesize that ADAR contributes to the shared module's transcript-quality or innate RNA-response behavior, but the co-abundance data do not prove that ADAR editing activity changes in either tissue.

#### DDX21

- **Related proteins** (co-abundance neighbors): MATR3 (0.89), PSMC4 (0.89), ADAR (0.88), SUPT16H (0.86), HNRNPR (0.85), NOP2 (0.82), PSMC2 (0.81); STRING partners: DHX9 (0.908), HNRNPR (0.73), LARP7 (0.866), NOP2 (0.761), NOP56 (0.811)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 is highly connected within the module and links ADAR, DHX9, HNRNPR, SUPT16H, NOP2, NOP56, and proteasome-associated genes. It is supported by the primary RNA-binding term (GO:MF RNA binding; q_global = 0.00948) and by every listed STRING supplementary theme relevant to RNA binding, leukemia-cell annotation, and ubiquitin-associated keywords (5 supplementary STRING terms; within-query FDR 0.00022–0.0291). Its annotation supports RNA helicase activity, ribosome or nucleolar biology, transcriptional regulation, and osteoblast differentiation, while its disease literature includes cancer and neurodegenerative disease.
- **Conclusion**: Established evidence supports DDX21 as a major connector between RNA remodeling, nucleolar functions, and transcriptional regulation. It is a strong candidate for coordinating the module, but its network position does not establish that it is the causal driver of the cross-tissue signal.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): LMNB1 (0.82), MATR3 (0.81); STRING partners: DHX9 (0.901), HNRNPR (0.961), MATR3 (0.757), SETD2 (0.935)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_07581.1, huMAP3_05721.1, huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_10659.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is a nuclear RNA-binding and splicing regulator with a very strong STRING relationship to HNRNPR and additional relationships to DHX9, MATR3, and SETD2. It recurs across multiple hu.MAP hnRNP complexes (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1) and belongs to the primary RNA-binding term (GO:MF RNA binding; q_global = 0.00948). Its annotation supports mRNA processing and alternative splicing, and its disease associations include neuromuscular and cancer-related conditions.
- **Conclusion**: Established evidence supports HNRNPL as a scaffold-like component of the module's nuclear RNA-processing architecture. The module may reflect coordinated splicing control, but a specific transcript target or tissue-specific splicing consequence remains a hypothesis.

#### MATR3

- **Related proteins** (co-abundance neighbors): DDX21 (0.89), HNRNPR (0.83), PSMC4 (0.82), SUPT16H (0.82), BAG2 (0.81), HNRNPL (0.81), PSMC2 (0.81); STRING partners: DHX9 (0.786), HNRNPL (0.757), HNRNPR (0.714)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_07581.1, huMAP3_05721.1
- **Function (MyGene.info)**: matrin 3. This gene encodes a nuclear matrix protein, which is proposed to stabilize certain messenger RNA species. Mutations of this gene are associated with distal myopathy 2, which often includes vocal cord and pharyngeal weakness. Alternatively spliced transcript variants, including read-through transcripts composed of the upstream small nucleolar RNA host gene 4 (non-protein coding) and matrin 3 gene s…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.735); distal myopathy with vocal cord weakness (0.569); neurodegenerative disease (0.529); distal myopathy (0.384); hereditary disease (0.193)
- **Europe PMC papers**: 1756
- **Why important**: MATR3 is well positioned among DDX21, HNRNPR, HNRNPL, SUPT16H, and proteasome-associated genes. It is present in several hu.MAP hnRNP complexes (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_05721.1) and in the primary RNA-binding term (GO:MF RNA binding; q_global = 0.00948), with STRING support for interactions with DHX9, HNRNPL, and HNRNPR. Its established functions include nuclear matrix organization and post-transcriptional gene regulation, and its disease associations include distal myopathy and amyotrophic lateral sclerosis.
- **Conclusion**: Established evidence supports MATR3 as a nuclear RNA-protein organization factor connecting RNA processing with nuclear structure. Its inclusion suggests that spatial organization of RNA metabolism may be relevant, but the co-abundance pattern does not demonstrate a direct MATR3-dependent mechanism.

#### SUPT16H

- **Related proteins** (co-abundance neighbors): DHX9 (0.90), CRBN (0.87), ADAR (0.87), DDX21 (0.86), PSMC2 (0.83), MATR3 (0.82), CAPRIN1 (0.80); STRING partners: SETD2 (0.754)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SPT16 homolog, facilitates chromatin remodeling subunit. Transcription of protein-coding genes can be reconstituted on naked DNA with only the general transcription factors and RNA polymerase II. However, this minimal system cannot transcribe DNA packaged into chromatin, indicating that accessory factors may facilitate access to DNA. One such factor, FACT (facilitates chromatin transcription), interacts specifically with histones H2A/H2B to effect nucle…
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and thin corpus callosum (0.651); HIV infectious disease (0.584); Global developmental delay (0.372); Intellectual disability (0.372); Abnormal corpus callosum morphology (0.370)
- **Europe PMC papers**: 676
- **Why important**: SUPT16H connects the RNA-associated core to transcriptional chromatin regulation and has relationships with DHX9, ADAR, DDX21, MATR3, CAPRIN1, and proteasome-associated genes. It belongs to the primary RNA-binding term (GO:MF RNA binding; q_global = 0.00948) and to several supplementary STRING themes (4 supplementary STRING terms; within-query FDR 0.0016–0.0291). Its established function is as a component of FACT, which regulates nucleosome organization and transcription elongation. It is enhanced in erythrocyte progenitors, making it relevant to possible hematopoietic cell-state contributions.
- **Conclusion**: Established evidence supports SUPT16H as a bridge between RNA metabolism and chromatin-dependent transcription. A hematopoietic transcriptional-demand component is plausible, but the module does not establish whether this reflects erythroid composition, proliferation, or a shared regulatory state across tissues.

#### HNRNPR

- **Related proteins** (co-abundance neighbors): CRBN (0.90), DDX21 (0.85), DHX9 (0.84), MATR3 (0.83), LMNB1 (0.80); STRING partners: DDX21 (0.73), DHX9 (0.909), HNRNPL (0.961), LARP7 (0.817), MATR3 (0.714)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_07581.1, huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_10659.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR is a nuclear pre-mRNA-processing factor with connections to CRBN, DDX21, DHX9, MATR3, LMNB1, and HNRNPL. It is included in numerous hu.MAP hnRNP assemblies (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1), has multiple STRING relationships, and belongs to the primary RNA-binding term (GO:MF RNA binding; q_global = 0.00948). Its annotation supports spliceosome-associated mRNA processing, and its disease associations include developmental and neurodevelopmental disorders.
- **Conclusion**: Established evidence supports HNRNPR as a core component of the module's conserved nuclear RNA-processing network. Its broad expression and low immune-cell specificity favor a general intracellular program over a disease-specific interpretation; any tissue-pair-specific role remains hypothetical.

## Module 16

**Tissue pair**: bone_marrow and kidney  
**Genes (6)**: BOD1L1, MIB1, PPP1R12A, RBM26, TACC1, ZC3H13

### Function

The module has no GO or KEGG term passing global correction, so its function cannot be assigned from statistically significant pathway enrichment. Its network structure is organized around MIB1, which is connected to every other module member, while the remaining genes are peripheral and connected primarily to MIB1. The genes collectively point to a mixed cellular program involving ubiquitin-dependent regulation and endocytosis through MIB1, RNA processing and RNA regulation through ZC3H13 and RBM26, DNA-damage and replication-fork responses through BOD1L1, actomyosin and phosphatase regulation through PPP1R12A, and microtubule, spindle, and nuclear-migration biology through TACC1. These annotations are biologically suggestive but do not constitute a significantly enriched common function. The lack of STRING functional enrichment is consistent with a heterogeneous module rather than a clearly defined canonical pathway.

**Cell composition.** All module genes have low tissue specificity and all are detected at the protein level in both bone marrow and kidney. None is secreted, so the module is not a plasma-protein or secreted-protein signature. The HPA evidence also does not show a dominant tissue-enriched program. Cell-type annotations are heterogeneous: BOD1L1 is associated with neutrophils and neutrophil blood-cell enrichment, PPP1R12A with neutrophil-related and smooth-muscle populations, and the other genes with diverse cell types including podocytes, hepatocytes, cardiomyocytes, myonuclei, Sertoli cells, vascular cells, and kidney tubular cells. MIB1 is not detected in immune cells, whereas BOD1L1 is immune-cell enhanced. Thus, the shared signal is more compatible with broadly expressed intracellular proteins, potentially combined with shared or varying cell-composition effects, than with a uniform blood-cell or secreted-protein module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported for any pair in the module, and no hu.MAP complex contains multiple module members. The co-abundance edges therefore are not corroborated by the supplied physical-interaction or complex resources. MIB1 is a topological hub in the co-abundance graph, but this does not establish that it physically binds the other genes. The absence of STRING and hu.MAP support may reflect tissue-specific regulation, indirect co-expression, incomplete database coverage, or a statistical co-abundance relationship rather than a molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a previously unreported co-abundance association between these genes in the bone-marrow and kidney tissue pair, but it cannot be called a new biological mechanism from the supplied evidence alone. The absence of STRING interactions and hu.MAP complexes makes the pattern less likely to be a previously catalogued physical complex, yet database absence is not proof of novelty. The lack of globally significant GO or KEGG enrichment and the heterogeneous HPA cell-type annotations further argue for a cautious claim: the potentially novel result is the tissue-pair co-abundance pattern, not a newly established pathway or complex. Independent replication, cell-composition adjustment, and experimental interaction or perturbation studies would be needed.

**Hypothesis.** Hypothesis: the module may reflect coordinated regulation of intracellular processes in shared or changing cell populations across bone marrow and kidney. MIB1 could represent a central regulatory node linking protein turnover and endocytic signaling with RNA-processing factors, genome-stability machinery, cytoskeletal contractility, and microtubule organization. The observed pattern could therefore arise from a shared state involving cell maintenance, proliferation or repair, and cytoskeletal remodeling, potentially influenced by neutrophil-related composition in some samples. This is a hypothesis only; the absence of significant enrichment, STRING interactions, and hu.MAP complexes prevents treating it as an established mechanism.

### Important genes

#### MIB1

- **Related proteins** (co-abundance neighbors): ZC3H13 (0.89), RBM26 (0.89), BOD1L1 (0.84), PPP1R12A (0.84), TACC1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Microtubules, Primary cilium; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MIB E3 ubiquitin protein ligase 1. This gene encodes a protein containing multiple ankyrin repeats and RING finger domains that functions as an E3 ubiquitin ligase. The encoded protein positively regulates Notch signaling by ubiquitinating the Notch receptors, thereby facilitating their endocytosis. This protein may also promote the ubiquitination and degradation of death-associated protein kinase 1 (DAPK1). [provided by RefSeq, Ju…
- **Diseases (Open Targets)**: left ventricular noncompaction (0.625); hypercholesterolemia, familial, 1 (0.333); type 2 diabetes mellitus (0.268); Abnormality of the skeletal system (0.266); musculoskeletal system disorder (0.250)
- **Europe PMC papers**: 3711
- **Why important**: MIB1 is the central hub of the module, connected to all other members with the strongest overall network position. Its established E3 ubiquitin-ligase function, roles in Notch-receptor endocytosis and DAPK1 regulation, and localization to microtubules and the primary cilium make it the most plausible coordinating gene. It also has comparatively extensive literature support and disease associations including cardiac, metabolic, and skeletal phenotypes.
- **Conclusion**: Established evidence supports MIB1 as a ubiquitin-dependent regulator of endocytosis and Notch signaling and as the topological center of this co-abundance module. It is not established that MIB1 directly regulates the other module genes. Its proposed coordinating role is therefore a plausible interpretation, not a demonstrated molecular mechanism.

#### ZC3H13

- **Related proteins** (co-abundance neighbors): MIB1 (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger CCCH-type containing 13. Enables RNA binding activity. Involved in mRNA methylation. Located in nuclear speck. Part of RNA N6-methyladenosine methyltransferase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); type 2 diabetes mellitus (0.332); liver disorder (0.332); renal dialysis (0.290); poisoning (0.213)
- **Europe PMC papers**: 2616
- **Why important**: ZC3H13 is directly connected to the MIB1 hub and provides a distinct nuclear RNA-regulatory component. It has established RNA-binding and mRNA-methylation-related functions, involvement in RNA processing and stem-cell population maintenance, and substantial literature support. Its disease associations include neurodegenerative, metabolic, hepatic, and renal conditions.
- **Conclusion**: Established evidence supports ZC3H13 as an RNA-regulatory factor associated with mRNA processing and stem-cell maintenance. Its co-abundance with MIB1 may indicate coordinated regulation of nuclear RNA biology and protein-signaling machinery, but that connection remains hypothetical and is not supported by a reported physical interaction.

#### BOD1L1

- **Related proteins** (co-abundance neighbors): MIB1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biorientation of chromosomes in cell division 1 like 1. Predicted to enable protein phosphatase 2A binding activity and protein phosphatase inhibitor activity. Involved in cellular response to DNA damage stimulus and replication fork processing. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.515); luminal B breast carcinoma (0.321); sialolithiasis (0.292); Paralysis (0.284); hypopituitarism (0.236)
- **Europe PMC papers**: 151
- **Why important**: BOD1L1 is a peripheral member linked to MIB1 and contributes a genome-stability dimension through DNA-damage response and replication-fork processing. HPA associates it with neutrophils and shows immune-cell enhancement, making it especially relevant when interpreting a bone-marrow-containing tissue pair. Its literature is more limited than that of MIB1 or ZC3H13, but its functional annotation and disease associations provide a biologically meaningful anchor.
- **Conclusion**: Established evidence supports BOD1L1 in replication-fork and DNA-damage biology and supports a neutrophil-associated expression pattern. A role in linking genome maintenance to the wider module is a hypothesis; the data do not establish that the module is a DNA-damage program or a neutrophil-specific module.

#### PPP1R12A

- **Related proteins** (co-abundance neighbors): MIB1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments, Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase 1 regulatory subunit 12A. Myosin phosphatase target subunit 1, which is also called the myosin-binding subunit of myosin phosphatase, is one of the subunits of myosin phosphatase. Myosin phosphatase regulates the interaction of actin and myosin downstream of the guanosine triphosphatase Rho. The small guanosine triphosphatase Rho is implicated in myosin light chain (MLC) phosphorylation, which results in contraction of smo…
- **Diseases (Open Targets)**: genitourinary and/or brain malformation syndrome (0.777); neurodegenerative disease (0.572); hereditary disease (0.415); holoprosencephaly (0.371); Genetic 46,XY disorder of sex development (0.370)
- **Europe PMC papers**: 1121
- **Why important**: PPP1R12A is linked to the MIB1 hub and represents regulation of myosin phosphatase, Rho-dependent actomyosin behavior, adhesion, and cell-cycle-related processes. Its HPA annotations include neutrophil-related progenitor and smooth-muscle populations, while its disease associations include developmental and genitourinary phenotypes. Its literature support is substantial, making it a useful mechanistic bridge to cytoskeletal and cell-state regulation.
- **Conclusion**: Established evidence supports PPP1R12A as a regulator of myosin phosphatase and actomyosin behavior. Its presence may indicate cytoskeletal or adhesion-related coordination in the module, but a direct functional relationship with MIB1 or the other genes is not established.

#### TACC1

- **Related proteins** (co-abundance neighbors): MIB1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transforming acidic coiled-coil containing protein 1. This locus may represent a breast cancer candidate gene. It is located close to FGFR1 on a region of chromosome 8 that is amplified in some breast cancers. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2017].
- **Diseases (Open Targets)**: prostate carcinoma (0.325); nephritis (0.255); Nephropathy (0.255); ocular hypotension (0.255); hair color (0.201)
- **Europe PMC papers**: 1000
- **Why important**: TACC1 is connected to MIB1 and contributes microtubule, mitotic-spindle, nuclear-migration, and transcriptional functions. HPA places it in diverse vascular, pericyte, smooth-muscle, and kidney tubular cell contexts, which fits the absence of a single dominant tissue or immune signature. It has substantial literature support and disease associations including nephritis, nephropathy, and cancer-related phenotypes.
- **Conclusion**: Established evidence supports TACC1 in microtubule and mitotic-spindle organization and in nuclear migration. Its co-abundance with MIB1 could reflect coordinated cytoskeletal regulation, but this remains a hypothesis because neither STRING nor hu.MAP provides corroborating interaction or complex evidence.

## Module 17

**Tissue pair**: bone_marrow and kidney  
**Genes (9)**: CANX, CD151, ALCAM, CD44, ITGAV, ITGB1, MYOF, PLP2, SEC22B

### Function

The module is best interpreted as a cell-surface adhesion, extracellular-matrix interaction, and tissue-repair program. The strongest primary evidence is the coherent set of globally corrected terms for wound healing and spreading of cells (GO:BP wound healing, spreading of cells; q_global = 0.000101), epiboly and epiboly-associated wound healing (GO:BP epiboly; q_global = 0.000101) (GO:BP epiboly involved in wound healing; q_global = 0.000101), epithelial-sheet morphogenesis (GO:BP morphogenesis of an epithelial sheet; q_global = 0.000185), cell-surface and receptor-complex localization (GO:CC receptor complex; q_global = 0.00358) (GO:CC cell surface; q_global = 0.00585) (GO:CC plasma membrane signaling receptor complex; q_global = 0.0277), wound healing and response to wounding (GO:BP wound healing; q_global = 0.0067) (GO:BP response to wounding; q_global = 0.017), heterotypic cell-cell adhesion (GO:BP heterotypic cell-cell adhesion; q_global = 0.0122), integrin alpha-v-beta-one complex (GO:CC integrin alphav-beta1 complex; q_global = 0.017), ECM-receptor interaction (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0316), phagocytosis (KEGG Phagocytosis - Homo sapiens (human); q_global = 0.0337), vesicle membranes (GO:CC cytoplasmic vesicle membrane; q_global = 0.0377) (GO:CC vesicle membrane; q_global = 0.0418), focal adhesion (GO:CC focal adhesion; q_global = 0.0488), and epithelial morphogenesis (GO:BP morphogenesis of an epithelium; q_global = 0.049). Chemokine and cytokine binding (GO:MF chemokine binding; q_global = 0.000866) (GO:MF cytokine binding; q_global = 0.00792) (GO:MF C-X3-C chemokine binding; q_global = 0.017) suggests that the adhesion program may also participate in communicating with inflammatory ligands. Overall, the genes support coordinated cell attachment, migration, membrane organization, vesicle trafficking, and repair rather than a narrowly lineage-specific biosynthetic pathway.

**Cell composition.** The module is predominantly composed of membrane-associated or transmembrane proteins, consistent with the STRING membrane annotations (STRING Keyword Transmembrane helix; within-query FDR = 1.62e-06) (STRING Component Integral component of plasma membrane; within-query FDR = 1.93e-05) (STRING Component Integral component of membrane; within-query FDR = 2.26e-05). It is not dominated by secreted plasma proteins: only ALCAM and CD44 are annotated as secreted to blood, while the other genes are not secreted. Most genes have low tissue specificity in HPA, so the module is not strongly restricted to bone marrow or kidney. Several genes have enhanced profiles in epithelial, vascular, stromal, platelet, monocyte, neutrophil, or dendritic-cell populations, but the module as a whole has low immune-cell specificity. This makes a shared structural or cell-composition signal plausible, including contributions from common stromal, vascular, epithelial, or circulating-cell populations, rather than requiring a kidney-specific or marrow-specific mechanism. Protein detection is broadly compatible with the module in both tissues, although ITGB1 and ALCAM show tissue-specific detection differences in the supplied HPA evidence.

**GO/KEGG enrichment**: 22 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP wound healing, spreading of cells | 0.000101 | CD151, CD44, ITGAV, ITGB1 |
| GO:BP epiboly | 0.000101 | CD151, CD44, ITGAV, ITGB1 |
| GO:BP epiboly involved in wound healing | 0.000101 | CD151, CD44, ITGAV, ITGB1 |
| GO:BP morphogenesis of an epithelial sheet | 0.000185 | CD151, CD44, ITGAV, ITGB1 |
| GO:MF chemokine binding | 0.000866 | ITGAV, ITGB1, PLP2 |
| KEGG Cell adhesion molecule (CAM) interaction - Homo sapiens (human) | 0.00229 | ALCAM, ITGAV, ITGB1 |
| GO:CC receptor complex | 0.00358 | ALCAM, CD44, ITGAV, ITGB1 |
| GO:CC cell surface | 0.00585 | ALCAM, CD151, CD44, ITGAV, ITGB1 |
| GO:BP wound healing | 0.0067 | CD151, CD44, ITGAV, ITGB1, MYOF |
| GO:MF cytokine binding | 0.00792 | ITGAV, ITGB1, PLP2 |
| GO:BP heterotypic cell-cell adhesion | 0.0122 | CD44, ITGAV, ITGB1 |
| GO:BP response to wounding | 0.017 | CD151, CD44, ITGAV, ITGB1, MYOF |
| GO:MF C-X3-C chemokine binding | 0.017 | ITGAV, ITGB1 |
| GO:CC integrin alphav-beta1 complex | 0.017 | ITGAV, ITGB1 |
| GO:CC plasma membrane signaling receptor complex | 0.0277 | ALCAM, ITGAV, ITGB1 |

### STRING and hu.MAP

STRING supports a known adhesion-centered core involving ITGAV with ITGB1 and CD44, ITGB1 with CD44, CD151, and ALCAM, and CD151 with ALCAM. These relationships provide independent support that the co-abundance pattern contains established protein-association structure rather than being only a statistical grouping. STRING also links CANX with SEC22B, supporting an ER and vesicle-trafficking branch, while the broader membrane and transmembrane enrichments are supplementary evidence (STRING Keyword Transmembrane helix; within-query FDR = 1.62e-06) (STRING Component Integral component of plasma membrane; within-query FDR = 1.93e-05) (STRING Component Integral component of membrane; within-query FDR = 2.26e-05). hu.MAP identifies ITGB1 and ALCAM together in three larger complexes (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1). These complexes contain multiple adhesion, lectin, receptor, and membrane-trafficking proteins, but only a small subset of their members is present in this module. Thus, hu.MAP supports membership in known multi-protein contexts without demonstrating that the entire co-abundance module is one physical complex.

**STRING interactions (score >= 0.7)**: 8 of 36 gene pairs: ALCAM–CD44 (0.859); ALCAM–ITGB1 (0.824); CANX–SEC22B (0.703); CD151–CD44 (0.778); CD151–ITGB1 (0.949); CD44–ITGAV (0.85); CD44–ITGB1 (0.957); ITGAV–ITGB1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transmembrane helix (FDR = 1.62e-06, 9 genes); Component Integral component of plasma membrane (FDR = 1.93e-05, 6 genes); Component Integral component of membrane (FDR = 2.26e-05, 9 genes); PMID (1998) Phenotypic mapping of human mesothelial cells. (FDR = 4.38e-05, 5 genes); PMID (2023) The Upscale Manufacture of Chondrocytes for Allogeneic Cartilage Therapies. (FDR = 5.52e-05, 5 genes); PMID (2022) Meniscus Regeneration With Multipotent Stromal Cell Therapies. (FDR = 5.52e-05, 5 genes); PMID (2017) Mesenchymal stroma cells in peritoneal dialysis effluents from patients. (FDR = 5.52e-05, 5 genes); PMID (2003) Antigenic profile of human thymus in concurrence with Clusters of Thymic Epithelial Staining classification. (FDR = 5.52e-05, 5 genes); PMID (2019) A comprehensive characterisation of large-scale expanded human bone marrow and umbilical cord mesenchymal stem cells. (FDR = 5.67e-05, 5 genes); PMID (2014) Surface antigen profiles of leukocytes and melanoma cells in lymph node metastases are associated with survival in AJCC stage III melanoma patients. (FDR = 6.72e-05, 5 genes); PMID (2016) Extensive surface protein profiles of extracellular vesicles from cancer cells may provide diagnostic signatures from blood samples. (FDR = 0.00014, 5 genes); PMID (2015) Understanding nucleus pulposus cell phenotype: a prerequisite for stem cell based therapies to treat intervertebral disc degeneration. (FDR = 0.00014, 5 genes); PMID (2015) Label-free proteomic analysis of the hydrophobic membrane protein complement in articular chondrocytes: a technique for identification of membrane biomarkers. (FDR = 0.00014, 5 genes); PMID (2020) Perinatal Derivatives: Where Do We Stand? A Roadmap of the Human Placenta and Consensus for Tissue and Cell Nomenclature. (FDR = 0.00026, 5 genes); PMID (2008) Molecular trafficking mechanisms of multipotent mesenchymal stem cells derived from human bone marrow and placenta. (FDR = 0.00035, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10503.1 (ITGB1, ALCAM; 2/27); huMAP3_10980.1 (ITGB1, ALCAM; 2/44); huMAP3_09336.1 (ITGB1, ALCAM; 2/50)

### Novelty

The biological functions and much of the interaction core are not new: integrin-mediated adhesion, CD44-associated matrix interactions, CD151 associations, ALCAM-mediated cell adhesion, and vesicle trafficking are established areas of biology, and several module edges are already represented in STRING or hu.MAP. The potentially novel aspect is the reproducible co-abundance organization of these genes across bone marrow and kidney, particularly the combination of an integrin and adhesion core with a vesicle-trafficking branch. However, the supplied evidence does not establish that this cross-tissue module has never been reported. Absence of some genes or edges from STRING or hu.MAP cannot prove novelty, because those resources describe curated or experimentally supported relationships rather than every co-abundance relationship. The defensible conclusion is that the module may represent a new cross-tissue co-abundance pattern built from largely known biology, requiring comparison with published co-expression modules and independent cohorts before being called a new finding.

**Hypothesis.** Hypothesis: the module reflects a shared repair-competent membrane state in stromal, epithelial, vascular, or immune-adjacent cells present in both tissues. In this model, ITGAV-ITGB1 and CD44 organize matrix and cell-surface adhesion, CD151 stabilizes or coordinates membrane adhesion complexes, and ALCAM contributes heterotypic cell-cell contact. MYOF, SEC22B, and CANX could support membrane remodeling, vesicle delivery, and protein-folding or trafficking demands during migration and repair, while PLP2 may connect membrane organization with cytokine or chemokine responsiveness. The predicted consequence is coordinated adhesion, migration, matrix engagement, inflammatory-ligand sensing, phagocytic behavior, and wound repair. This is a mechanistic hypothesis rather than a demonstrated causal pathway; it should be tested with cell-type-resolved data, perturbation of the integrin or CD44 axis, and direct measurement of migration, adhesion, vesicle trafficking, and repair phenotypes.

### Important genes

#### ITGB1

- **Related proteins** (co-abundance neighbors): MYOF (0.91), ITGAV (0.84); STRING partners: ALCAM (0.824), CD151 (0.949), CD44 (0.957), ITGAV (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_10503.1, huMAP3_10980.1, huMAP3_09336.1
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is a central network component and is present in every primary globally corrected enrichment theme that defines the module's adhesion and repair interpretation, including wound healing, cell adhesion, integrin-complex, focal-adhesion, ECM-receptor, and phagocytosis terms (22 globally significant GO/KEGG terms, q_global 0.000101–0.049; see the table). It has strong STRING support with ITGAV, CD44, CD151, and ALCAM, and it is present in all three hu.MAP complexes (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1). Its established functions include cell adhesion, tissue repair, immune response, angiogenesis, and phagocytosis. It also has the largest literature volume among the module genes in the supplied evidence.
- **Conclusion**: Established evidence supports ITGB1 as a core adhesion and signaling hub of the module. It is the strongest candidate for the structural integrator of matrix attachment, cell-cell contact, and repair-related signaling. A causal role in the cross-tissue co-abundance pattern remains a hypothesis because the supplied data are observational.

#### ITGAV

- **Related proteins** (co-abundance neighbors): MYOF (0.85), ALCAM (0.85), ITGB1 (0.84), CD44 (0.84); STRING partners: CD44 (0.85), ITGB1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha V. The product of this gene belongs to the integrin alpha chain family. Integrins are heterodimeric integral membrane proteins composed of an alpha subunit and a beta subunit that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha V subunit. This subunit associates with beta 1, beta 3, beta…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); myocardial infarction (0.396); angina pectoris (0.371); Recurrent thrombophlebitis (0.370); intermediate coronary syndrome (0.370)
- **Europe PMC papers**: 5475
- **Why important**: ITGAV is the most connected module member in the supplied subgraph and connects the integrin core to MYOF, ALCAM, ITGB1, and CD44. It appears across the primary wound-healing, epithelial morphogenesis, chemokine-binding, cell-surface, ECM-receptor, focal-adhesion, and phagocytosis evidence (22 globally significant GO/KEGG terms, q_global 0.000101–0.049; see the table). Its established biology concerns integrin-mediated cell adhesion and signaling, with associations to angiogenesis, vasculogenesis, and cell-matrix adhesion. It is also supported by strong STRING association with ITGB1 and CD44 and has substantial literature support.
- **Conclusion**: Established evidence supports ITGAV as a principal receptor-side organizer of the adhesion and repair program. Its position suggests that it could couple matrix engagement to migration and inflammatory signaling, but that coupling is a mechanistic hypothesis rather than a direct demonstration in this module.

#### CD44

- **Related proteins** (co-abundance neighbors): MYOF (0.89), ITGAV (0.84); STRING partners: ALCAM (0.859), CD151 (0.778), ITGAV (0.85), ITGB1 (0.957)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD44 molecule (IN blood group). The protein encoded by this gene is a cell-surface glycoprotein involved in cell-cell interactions, cell adhesion and migration. It is a receptor for hyaluronic acid (HA) and can also interact with other ligands, such as osteopontin, collagens, and matrix metalloproteinases (MMPs). This protein participates in a wide variety of cellular functions including lymphocyte activation, recirculation and …
- **Diseases (Open Targets)**: nephrolithiasis, calcium oxalate (0.523); calcium oxalate urolithiasis (0.521); uterine corpus leiomyoma (0.480); systemic lupus erythematosus (0.467); autoimmune disease (0.330)
- **Europe PMC papers**: 102058
- **Why important**: CD44 is a highly connected surface receptor in the module and links MYOF and ITGAV with ITGB1 and ALCAM through STRING. It contributes to the globally corrected wound-healing, epithelial morphogenesis, cell-surface, heterotypic adhesion, ECM-receptor, and focal-adhesion terms (14 globally significant GO/KEGG terms, q_global 0.000101–0.049; see the table). Its established functions include hyaluronan-mediated cell interaction, cell adhesion, migration, inflammatory response, hematopoiesis, and vesicle-mediated transport. HPA places it in several epithelial and myeloid cell populations and detects it in both tissues. It also has by far the largest literature volume among the supplied genes.
- **Conclusion**: Established evidence supports CD44 as a multifunctional adhesion and migration receptor that could connect matrix sensing with inflammatory and repair responses. Its broad expression and extensive literature also make it a plausible marker of shared cell composition rather than proof of a tissue-specific mechanism.

#### CD151

- **Related proteins** (co-abundance neighbors): ALCAM (0.90), SEC22B (0.88), PLP2 (0.87); STRING partners: CD44 (0.778), ITGB1 (0.949)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD151 molecule (Raph blood group). The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. This encoded protein is a ce…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 7, with nephropathy and deafness (0.742); Abnormality of the skeletal system (0.463); hereditary disease (0.192); breast cancer (0.138); Fuchs' endothelial dystrophy (0.124)
- **Europe PMC papers**: 2989
- **Why important**: CD151 is a membrane tetraspanin with a central position in the module's surface-adhesion branch, connecting ALCAM, SEC22B, and PLP2 in the co-abundance network. It is included in the primary wound-healing, epithelial morphogenesis, cell-surface, and focal-adhesion evidence (9 globally significant GO/KEGG terms, q_global 0.000101–0.049; see the table). STRING supports its association with CD44 and ITGB1, while HPA shows enhancement in blood-vessel and platelet-related contexts. Its established functions include integrin complex formation, cell adhesion, migration, and wound healing.
- **Conclusion**: Established evidence supports CD151 as a membrane organizer that may stabilize or coordinate integrin-containing adhesion machinery. Its connection to the vesicle-associated branch is suggestive of membrane-trafficking coordination, but that specific role in this module remains a hypothesis.

#### ALCAM

- **Related proteins** (co-abundance neighbors): CD151 (0.90), ITGAV (0.85); STRING partners: CD44 (0.859), ITGB1 (0.824)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_10503.1, huMAP3_10980.1, huMAP3_09336.1
- **Function (MyGene.info)**: activated leukocyte cell adhesion molecule. This gene encodes activated leukocyte cell adhesion molecule (ALCAM), also known as CD166 (cluster of differentiation 166), which is a member of a subfamily of immunoglobulin receptors with five immunoglobulin-like domains (VVC2C2C2) in the extracellular domain. This protein binds to T-cell differentiation antigene CD6, and is implicated in the processes of cell adhesion and migration. Multiple al…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.458); mathematical ability (0.453); open-angle glaucoma (0.396); restless legs syndrome (0.379); ovarian dysfunction (0.362)
- **Europe PMC papers**: 4212
- **Why important**: ALCAM is a surface adhesion receptor connected to CD151 and ITGAV in the module and to CD44 and ITGB1 in STRING. It contributes to the primary CAM-interaction, receptor-complex, cell-surface, plasma-membrane receptor-complex, and focal-adhesion terms (5 globally significant GO/KEGG terms, q_global 0.00229–0.0488; see the table). It is represented with ITGB1 in all three hu.MAP complexes (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1). Its established functions include heterophilic cell-cell adhesion, leukocyte-related interactions, migration, and signal transduction. HPA annotates it as secreted to blood and enriched in parathyroid tissue or myeloid dendritic cells, which is relevant to interpreting possible circulating or cell-composition effects.
- **Conclusion**: Established evidence supports ALCAM as a cell-cell adhesion and receptor-complex component that helps define the module's intercellular-contact branch. Its blood secretion annotation means that extracellular or sample-composition effects should be considered, but it does not establish that circulating ALCAM drives the co-abundance module.

## Module 18

**Tissue pair**: bone_marrow and kidney  
**Genes (8)**: TTC4, HMGB3, NCK1, CBFB, PRRC2A, RBM4B, DPF2, UBE2S

### Function

The module does not support a single statistically established GO or KEGG function: no globally significant GO/KEGG term passed global correction, and there are no supplementary STRING terms. Its gene content instead suggests a mixed regulatory program involving RNA binding and post-transcriptional control through RBM4B and PRRC2A, transcriptional and chromatin regulation through CBFB, DPF2 and HMGB3, protein ubiquitination and cell-cycle-linked proteostasis through UBE2S, signalling and cytoskeletal organization through NCK1, and chaperone-associated protein handling through TTC4. The co-abundance network is organized around RBM4B, with the other genes forming sparse peripheral links, so the module is better interpreted as a coordinated expression pattern than as evidence for a defined physical pathway.

**Cell composition.** The module contains no secreted proteins. Most genes have low tissue specificity and low immune-cell specificity, while many show cell-type-enhanced expression in diverse cell types rather than a consistent bone-marrow or kidney lineage. HPA detects several proteins in both bone marrow and kidney, but detection is incomplete and HMGB3 and UBE2S are not detected in those tissues by the reported immunohistochemistry. The pattern therefore does not look like a plasma-protein module or a strongly blood-cell-enriched module. It is compatible with broadly expressed regulatory machinery, with possible contributions from differing cell composition or shared proliferative and progenitor-like cell states in the two tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and there is no supplementary STRING enrichment. No hu.MAP complex contains multiple module members. Thus, the co-abundance links are not corroborated here as established protein-protein interactions or a shared molecular complex. This does not disprove biological coordination, because co-abundance can arise from common regulation, cell-state composition, or indirect relationships; it does mean that the module should not be described as a known physical complex.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be novel as a tissue-pair co-abundance pattern, because its exact membership has no high-confidence STRING support, no multi-member hu.MAP complex support, and no globally significant GO or KEGG annotation. However, those absences alone do not establish novelty. The individual genes and several of their functions are already well studied, especially CBFB, HMGB3, DPF2 and UBE2S, and the sparse network could reflect a new combination of known regulatory genes rather than a newly discovered molecular mechanism. The strongest defensible claim is novelty of the cross-tissue co-abundance association, pending independent replication and comparison with published co-expression resources.

**Hypothesis.** Hypothesis: the module reflects a shared regulatory or progenitor-associated cell state present in bone marrow and kidney rather than a single biochemical pathway. RBM4B may mark or help coordinate RNA-processing and translation-related regulation, while CBFB and DPF2 could connect that state to transcriptional and chromatin control. HMGB3 may represent stem or progenitor maintenance and proliferative capacity, UBE2S may reflect regulated proteolysis during cell-cycle activity, and NCK1 or TTC4 may capture signalling and protein-homeostasis components. PRRC2A could contribute post-transcriptional mRNA stabilization and translation control. This model is provisional because the module lacks globally significant enrichment, STRING support and hu.MAP support.

### Important genes

#### RBM4B

- **Related proteins** (co-abundance neighbors): NCK1 (0.90), CBFB (0.88), DPF2 (0.83), HMGB3 (0.82), TTC4 (0.81), PRRC2A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 4B. Enables RNA binding activity. Predicted to be involved in entrainment of circadian clock by photoperiod; mRNA splicing, via spliceosome; and regulation of gene expression. Predicted to act upstream of or within positive regulation of gene expression. Located in cytosol and nucleoplasm. Part of protein-containing complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: maturity-onset diabetes of the young (0.077); maturity-onset diabetes of the young type 3 (0.060); familial idiopathic steroid-resistant nephrotic syndrome (0.052); hereditary xanthinuria (0.051); exercise-induced hyperinsulinism (0.046)
- **Europe PMC papers**: 148
- **Why important**: RBM4B is the central network node, connected to every other member in the supplied subgraph. Its annotation links it to RNA binding, alternative mRNA splicing, translation regulation and gene-expression control. It is detected in both bone marrow and kidney, has low tissue specificity, and has disease associations including maturity-onset diabetes and familial idiopathic steroid-resistant nephrotic syndrome. Its literature volume is modest relative to several other selected genes, but its network position makes it the most important candidate for explaining module connectivity.
- **Conclusion**: Established evidence supports RBM4B as a broadly expressed RNA-regulatory protein and as the network hub. It is a plausible coordinator of the module, but there is no direct evidence here that it physically binds the other module proteins or drives their co-abundance. Its hub role is therefore an association-based interpretation, not a demonstrated mechanism.

#### CBFB

- **Related proteins** (co-abundance neighbors): RBM4B (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: core-binding factor subunit beta. The protein encoded by this gene is the beta subunit of a heterodimeric core-binding transcription factor belonging to the PEBP2/CBF transcription factor family which master-regulates a host of genes specific to hematopoiesis (e.g., RUNX1) and osteogenesis (e.g., RUNX2). The beta subunit is a non-DNA binding regulatory subunit; it allosterically enhances DNA binding by alpha subunit as the complex…
- **Diseases (Open Targets)**: cleidocranial dysplasia 1 (0.711); breast adenocarcinoma (0.507); breast carcinoma (0.396); lymphoid neoplasm (0.372); breast lobular carcinoma (0.370)
- **Europe PMC papers**: 4109
- **Why important**: CBFB is a regulatory subunit of core-binding factor and is annotated as a master regulator of hematopoiesis and osteogenesis through RUNX-family transcription factors. It is connected to RBM4B and is relevant to both the bone-marrow context and skeletal biology. Its disease associations include cleidocranial dysplasia and lymphoid neoplasm, and it has the largest literature representation among the module genes in the fact sheet.
- **Conclusion**: Established evidence supports CBFB as a major transcriptional regulator with direct relevance to hematopoietic and osteogenic programs. Its presence is biologically credible in this tissue pair, but the module data do not establish that CBFB activity, rather than cell composition, explains the shared co-abundance pattern.

#### HMGB3

- **Related proteins** (co-abundance neighbors): RBM4B (0.82), UBE2S (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: high mobility group box 3. This gene encodes a member of a family of proteins containing one or more high mobility group DNA-binding motifs. The encoded protein plays an important role in maintaining stem cell populations, and may be aberrantly expressed in tumor cells. A mutation in this gene was associated with microphthalmia, syndromic 13. There are numerous pseudogenes of this gene on multiple chromosomes. Alternative s…
- **Diseases (Open Targets)**: X-linked colobomatous microphthalmia-microcephaly-intellectual disability-short stature syndrome (0.461); neurodegenerative disease (0.451); neoplasm (0.112); breast carcinoma (0.111); breast cancer (0.110)
- **Europe PMC papers**: 1454
- **Why important**: HMGB3 is linked to maintenance of stem-cell populations and is annotated for DNA recombination and DNA structural change. It is the second node in the small HMGB3–UBE2S branch and is associated with developmental disease, neurodegenerative disease and neoplasia. HPA shows tissue enhancement in placenta and cell-type enhancement in several developmental or specialized cell populations, including cytotrophoblasts, extravillous trophoblasts, migrating cytotrophs, oocytes and respiratory deuterosomal cells. It is not detected in bone marrow or kidney by the reported immunohistochemistry, which makes transcript co-abundance especially important to interpret cautiously.
- **Conclusion**: Established evidence supports HMGB3 as a nuclear DNA-associated protein connected to stem-cell and proliferative biology. Its tissue and cell-type pattern does not specifically identify a kidney or bone-marrow mechanism. A role in a shared progenitor-like state is a hypothesis, not a conclusion from the available module evidence.

#### DPF2

- **Related proteins** (co-abundance neighbors): RBM4B (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: double PHD fingers 2. The protein encoded by this gene is a member of the d4 domain family, characterized by a zinc finger-like structural motif. This protein functions as a transcription factor which is necessary for the apoptotic response following deprivation of survival factors. It likely serves a regulatory role in rapid hematopoietic cell growth and turnover. This gene is considered a candidate gene for multiple …
- **Diseases (Open Targets)**: Coffin-Siris syndrome (0.774); neurodegenerative disease (0.552); hereditary disease (0.468); Intellectual disability (0.371); lysosomal storage disease (0.370)
- **Europe PMC papers**: 835
- **Why important**: DPF2 is a chromatin-remodelling and transcriptional regulator annotated for apoptotic responses, hematopoietic growth and turnover, and cell-cycle transition control. It is connected to the RBM4B hub, is detected in both bone marrow and kidney, and shows cell-type enhancement in oocytes. Its disease associations include Coffin–Siris syndrome, intellectual disability and neurodegenerative disease. The literature record is substantial, supporting established biological relevance even though it is peripheral in this network.
- **Conclusion**: Established evidence supports DPF2 as a chromatin and transcriptional regulator with links to apoptosis and hematopoietic growth. Its module membership could indicate coordinated regulation of cell state with RBM4B, but the absence of enrichment and physical-interaction support prevents assigning it a specific module-level role.

#### UBE2S

- **Related proteins** (co-abundance neighbors): HMGB3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin conjugating enzyme E2 S. This gene encodes a member of the ubiquitin-conjugating enzyme family. The encoded protein is able to form a thiol ester linkage with ubiquitin in a ubiquitin activating enzyme-dependent manner, a characteristic property of ubiquitin carrier proteins. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.444); hepatocellular carcinoma (0.115); neoplasm (0.102); Female infertility due to fertilization defect (0.092); ovarian carcinoma (0.091)
- **Europe PMC papers**: 2306
- **Why important**: UBE2S is an ubiquitin-conjugating enzyme involved in ubiquitin-chain formation, protein catabolism, exit from mitosis and anaphase-promoting-complex-dependent degradation. It forms the only branch with HMGB3 in the supplied network and is tissue-enhanced in bone marrow and testis. Its disease associations include neurodegenerative disease, hepatocellular carcinoma and ovarian carcinoma, and its literature representation is extensive.
- **Conclusion**: Established evidence supports UBE2S as a cell-cycle and proteostasis enzyme. Its connection with HMGB3 is consistent with a possible proliferative or progenitor-associated state, but the relationship is co-abundance-based and is not validated as a protein complex or direct regulatory interaction in this dataset.

## Module 19

**Tissue pair**: bone_marrow and kidney  
**Genes (5)**: EPS8, BPNT2, CHCHD4, NDUFAF7, WFS1

### Function

The module does not support a single statistically established pathway-level function: no GO or KEGG term passed global multiple-testing correction, and therefore no globally significant GO/KEGG term can be used as primary functional evidence. The gene-level annotations nevertheless suggest a mixed cellular program involving mitochondrial respiratory-chain assembly and protein import through NDUFAF7 and CHCHD4, endoplasmic-reticulum homeostasis and renal water-related biology through WFS1, Golgi phosphatase activity and skeletal development through BPNT2, and plasma-membrane signaling, Rac/Rho regulation, cell shape, and actin remodeling through EPS8. The co-abundance pattern is therefore more consistent with a coordinated cellular-state or compartmental program than with a confidently defined canonical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of the genes is annotated as secreted. HPA detects the proteins in kidney for the module genes and in bone marrow for nearly all of them, while most genes have low tissue specificity and low immune-cell specificity. Several genes show cell-type-enhanced expression, but the enriched cell types are diverse, including renal collecting-duct intercalated cells, pericytes, colonocytes, endometrial glandular cells, spermatogenic cells, alveolar cells, trophoblasts, lymphatic endothelial cells, somatotrophs, and parietal cells. One gene is tissue-enhanced in testis and one is immune-cell enhanced in non-classical monocytes, but the module as a whole is not strongly blood-cell specific. These observations make a simple plasma-protein or shared blood-cell explanation unlikely, although variation in cellular composition or broadly expressed intracellular proteins could contribute to the cross-tissue co-abundance.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no supplementary functional enrichment and no high-confidence interaction among the module genes. hu.MAP contains no complex with at least two module members. The observed network therefore is not corroborated by the available curated interaction or complex resources. The strongest local connectivity is centered on EPS8, which connects to WFS1, BPNT2, and NDUFAF7. NDUFAF7 connects to CHCHD4, forming a mitochondrial submodule, whereas WFS1 and BPNT2 are peripheral partners of EPS8. These relationships describe the measured co-abundance structure, not established physical interactions.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel cross-tissue co-abundance association, but it cannot be called a newly discovered biological pathway on the present evidence. The combination lacks globally significant GO or KEGG enrichment, STRING enrichment, high-confidence STRING interactions, and a shared hu.MAP complex. The absence of database support does not prove novelty because databases are incomplete and co-abundance can capture regulation, cell composition, or shared technical behavior rather than physical binding. A defensible novelty claim is therefore limited to the observation that these genes co-vary in the conserved bone-marrow–kidney module; independent replication, tissue-cell deconvolution, and experimental testing would be needed to establish biological novelty.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular stress or differentiation state in bone marrow and kidney in which mitochondrial protein maturation and respiratory-chain assembly, endoplasmic-reticulum homeostasis, Golgi nucleotide metabolism, and growth-factor-responsive cytoskeletal remodeling vary together. EPS8 may act as the principal co-abundance hub linking signaling and cytoskeletal state to the mitochondrial and organelle-maintenance genes, while NDUFAF7 and CHCHD4 represent a linked mitochondrial arm. WFS1 and BPNT2 may contribute organelle-specific responses relevant to renal and skeletal biology. This is a mechanistic hypothesis rather than an established pathway assignment, because the enrichment and interaction resources do not independently support it.

### Important genes

#### EPS8

- **Related proteins** (co-abundance neighbors): WFS1 (0.85), BPNT2 (0.85), NDUFAF7 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EGFR pathway substrate 8, signaling adaptor. This gene encodes a member of the EPS8 family. This protein contains one PH domain and one SH3 domain. It functions as part of the EGFR pathway, though its exact role has not been determined. Highly similar proteins in other organisms are involved in the transduction of signals from Ras to Rac and growth factor-mediated actin remodeling. Alternate transcriptional splice variants of this gene have …
- **Diseases (Open Targets)**: autosomal recessive nonsyndromic hearing loss 102 (0.636); deafness (0.531); hearing loss, autosomal recessive (0.455); infectious meningitis (0.270); alcohol drinking (0.212)
- **Europe PMC papers**: 1754
- **Why important**: EPS8 is the network hub, connecting to WFS1, BPNT2, and NDUFAF7. Its established annotation as an EGFR-pathway signaling adaptor with PH and SH3 domains, together with roles in Rac/Rho signaling, cell shape, and actin-filament regulation, makes it the clearest candidate for linking signaling state to the rest of the module. It is detected in both tissues, has cell-type-enhanced expression across several epithelial, stromal, and immune-related populations, has disease associations involving hearing loss and deafness, and has a substantial literature base.
- **Conclusion**: Established evidence supports EPS8 as a signaling and cytoskeletal regulator and as the topological hub of this module. It is plausible, but not demonstrated, that EPS8 coordinates the other module genes; the network does not establish direct physical interaction.

#### NDUFAF7

- **Related proteins** (co-abundance neighbors): CHCHD4 (0.88), EPS8 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase complex assembly factor 7. This gene encodes an assembly factor protein which helps in the assembly and stabilization of Complex I, a large multi-subunit enzyme in the mitochondrial respiratory chain. Complex I is involved in several physiological activities in the cell, including metabolite transport and ATP synthesis. The encoded protein is a methyltransferase which methylates Arg85 of a subunit of Complex I in the early …
- **Diseases (Open Targets)**: hypertensive disorder (0.195); schizophrenia (0.103); response to xenobiotic stimulus (0.077); Increased blood pressure (0.076); essential hypertension (0.069)
- **Europe PMC papers**: 219
- **Why important**: NDUFAF7 occupies a bridge position between EPS8 and CHCHD4 and is annotated as a mitochondrial complex I assembly factor that methylates a complex I subunit during early assembly. Its tissue-enhanced testis profile and enrichment in spermatogenic cell types distinguish it from the broadly expressed members. It has disease and phenotype associations involving blood pressure, hypertension, schizophrenia, and xenobiotic response, while its literature base is more limited than that of EPS8 or WFS1.
- **Conclusion**: Established evidence supports a role in mitochondrial respiratory-chain complex I assembly. Its connection to EPS8 and CHCHD4 suggests a possible mitochondrial arm of the module, but any functional coupling to plasma-membrane signaling remains a hypothesis.

#### CHCHD4

- **Related proteins** (co-abundance neighbors): NDUFAF7 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coiled-coil-helix-coiled-coil-helix domain containing 4. CHCHD4, a component of human mitochondria, belongs to a protein family whose members share 6 highly conserved cysteine residues constituting a -CXC-CX(9)C-CX(9)C- motif in the C terminus (Hofmann et al., 2005 [PubMed 16185709]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: lactic acidosis (0.333); Abnormal brain morphology (0.333); fetal growth restriction (0.333); Encephalopathy (0.333); Decreased liver function (0.333)
- **Europe PMC papers**: 351
- **Why important**: CHCHD4 is the partner of NDUFAF7 in the module and is a mitochondrial intermembrane-space protein-import and disulfide-relay factor involved in protein maturation and respiratory-chain complex assembly. It is detected in kidney but not bone marrow by the stated HPA immunohistochemistry result, and it has cell-type-enhanced expression in differentiating spermatogonia, esophageal basal cells, and parietal cells. Its disease associations include lactic acidosis, abnormal brain morphology, fetal growth restriction, encephalopathy, and decreased liver function.
- **Conclusion**: Established evidence supports CHCHD4 as a mitochondrial import and maturation factor. Its co-abundance with NDUFAF7 is biologically coherent, but the lack of STRING and hu.MAP support means the module does not establish a novel complex involving these proteins.

#### WFS1

- **Related proteins** (co-abundance neighbors): EPS8 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: wolframin ER transmembrane glycoprotein. This gene encodes a transmembrane protein, which is located primarily in the endoplasmic reticulum and ubiquitously expressed with highest levels in brain, pancreas, heart, and insulinoma beta-cell lines. Mutations in this gene are associated with Wolfram syndrome, also called DIDMOAD (Diabetes Insipidus, Diabetes Mellitus, Optic Atrophy, and Deafness), an autosomal recessive disorder. The disease…
- **Diseases (Open Targets)**: Wolfram syndrome (0.851); Wolfram-like syndrome (0.818); type 2 diabetes mellitus (0.764); autosomal dominant nonsyndromic hearing loss (0.749); cataract (0.703)
- **Europe PMC papers**: 3064
- **Why important**: WFS1 is a peripheral partner of the EPS8 hub and encodes an endoplasmic-reticulum transmembrane glycoprotein associated with ER overload response, kidney development, renal water homeostasis, and sensory biology. Its disease associations include Wolfram syndrome, Wolfram-like syndrome, type two diabetes mellitus, autosomal dominant nonsyndromic hearing loss, and cataract. It is detected in both tissues and has the largest literature base among the module genes, making it an important biologically established anchor despite its limited network connectivity.
- **Conclusion**: Established evidence strongly supports WFS1 in ER and renal-related biology and in human disease. Its relationship with EPS8 in this module may indicate coordinated cellular stress or tissue-state regulation, but that connection is not established as a direct molecular mechanism.

#### BPNT2

- **Related proteins** (co-abundance neighbors): EPS8 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3'(2'), 5'-bisphosphate nucleotidase 2. This gene encodes a member of the inositol monophosphatase family. The encoded protein is localized to the Golgi apparatus and catalyzes the hydrolysis of phosphoadenosine phosphate (PAP) to adenosine monophosphate (AMP). Mutations in this gene are a cause of GRAPP type chondrodysplasia with joint dislocations, and a pseudogene of this gene is located on the long arm of chromosome 1. [provided by …
- **Diseases (Open Targets)**: chondrodysplasia with joint dislocations, gPAPP type (0.738); chronic kidney disease (0.316); breast disorder (0.294); liver disorder (0.288); ovarian neoplasm (0.288)
- **Europe PMC papers**: 63
- **Why important**: BPNT2 is connected to EPS8 and encodes a Golgi-localized phosphoadenosine-phosphate phosphatase involved in nucleotide-phosphate metabolism. Its annotations include skeletal-system development and phosphatidylinositol dephosphorylation, and its disease association with gPAPP-type chondrodysplasia with joint dislocations gives it a distinctive developmental and organelle-related significance. It is detected in both tissues, has low cell-type specificity, and has a smaller literature base than the other selected genes.
- **Conclusion**: Established evidence supports BPNT2 as a Golgi enzyme with skeletal-development relevance. Its position beside EPS8 is consistent with a possible link between signaling and Golgi or phosphoinositide biology, but the module does not establish that mechanism.

## Module 20

**Tissue pair**: bone_marrow and kidney  
**Genes (5)**: GALNT7, MBLAC2, MIPEP, MRPL11, AARS2

### Function

The module does not have a statistically supported GO or KEGG functional enrichment term: no term passed global correction. Its gene composition nevertheless suggests a mixed cellular maintenance program. MBLAC2 is associated with palmitoyl-CoA hydrolase activity and is annotated to the endoplasmic reticulum membrane and plasma membrane. MRPL11 is a mitochondrial ribosomal component involved in mitochondrial translation. AARS2 supports mitochondrial alanyl-tRNA aminoacylation and translational fidelity, while MIPEP processes selected mitochondrial proteins involved in oxidative phosphorylation. GALNT7 initiates mucin-type O-linked glycosylation in the Golgi. Thus, the most defensible interpretation is coordinated abundance of broadly distributed mitochondrial protein-production and processing genes together with genes involved in lipid handling and protein glycosylation, rather than a single established pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of the genes is annotated as secreted. All module proteins were detected in both bone marrow and kidney. Most genes have low tissue specificity, although GALNT7 is tissue enhanced in stomach. Most genes show cell-type enhancement, but the enhanced cell types are heterogeneous and include neutrophils, epithelial populations, photoreceptors, corticotrophs and related cell types. All genes have low immune-cell specificity and no enriched blood-cell category is reported. This profile does not support a simple blood-cell or plasma-protein explanation. It is more consistent with a broadly distributed cellular program, although shared cell composition or sample-state effects cannot be excluded.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The co-abundance network contains edges among all five genes, with MBLAC2 occupying the central network position and the other genes connected directly to it. However, none of the possible gene pairs reached the supplied STRING interaction threshold, STRING reports no functional enrichment, and no hu.MAP complex contains at least two module members. Accordingly, the network edges are co-abundance relationships rather than established physical interactions. Known molecular functions still provide biological context: MRPL11 is part of the mitochondrial ribosome, AARS2 charges mitochondrial tRNA, MIPEP participates in maturation of mitochondrial proteins, and GALNT7 catalyzes a defined glycosylation step. The available STRING and hu.MAP evidence does not support a pre-existing multiprotein complex containing this module.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a new cross-tissue co-abundance observation, but it cannot be called a newly discovered molecular complex or pathway. Its novelty is supported only in the limited sense that the specific co-abundance grouping is not supported by the supplied STRING or hu.MAP resources. That absence does not prove biological novelty, because co-abundance associations can reflect shared regulation, cell composition, organelle abundance, or technical effects and need not appear in interaction databases. The lack of globally significant GO or KEGG enrichment and the mixed mitochondrial, Golgi, membrane and metabolic annotations further argue for cautious interpretation and independent replication.

**Hypothesis.** Hypothesis: in bone marrow and kidney samples, a shared cellular state may coordinately increase abundance of proteins supporting mitochondrial translation and mitochondrial protein maturation, while also changing lipid handling and glycoprotein processing. MBLAC2 may act as the abundance-linked hub that best captures this state, with AARS2, MRPL11 and MIPEP representing the mitochondrial component and GALNT7 representing a secretory-pathway component. This is a regulatory or state-associated hypothesis, not evidence that these proteins form a physical complex. Testing should examine replication across independent cohorts, cell-composition adjustment, mitochondrial abundance measures, and experimental or perturbational relationships among the genes.

### Important genes

#### MBLAC2

- **Related proteins** (co-abundance neighbors): MRPL11 (0.90), GALNT7 (0.89), AARS2 (0.87), MIPEP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: metallo-beta-lactamase domain containing 2. Enables palmitoyl-CoA hydrolase activity. Located in endoplasmic reticulum membrane and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: intelligence (0.297); neurodegenerative disease (0.272); Dermatochalasis (0.239); attention deficit-hyperactivity disorder (0.216); autism spectrum disorder (0.216)
- **Europe PMC papers**: 132
- **Why important**: MBLAC2 is the network hub, directly connected to every other module member and having the strongest weighted connectivity. It has low tissue specificity, is detected in both tissues, and is annotated with palmitoyl-CoA hydrolase activity plus endoplasmic-reticulum and plasma-membrane localization. Its literature volume is comparatively limited within this module, making the central co-abundance position especially important for follow-up rather than proof of causality.
- **Conclusion**: Established: MBLAC2 is the central co-abundance marker and has a lipid-related membrane-associated annotation. Hypothesis: it may report or help coordinate the cellular state linking the mitochondrial and glycosylation-related genes. The current evidence does not establish that MBLAC2 regulates the other genes.

#### AARS2

- **Related proteins** (co-abundance neighbors): MBLAC2 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alanyl-tRNA synthetase 2, mitochondrial. The protein encoded by this gene belongs to the class-II aminoacyl-tRNA synthetase family. Aminoacyl-tRNA synthetases play critical roles in mRNA translation by charging tRNAs with their cognate amino acids. The encoded protein is a mitochondrial enzyme that specifically aminoacylates alanyl-tRNA. Mutations in this gene are a cause of combined oxidative phosphorylation deficiency 8. [provided by R…
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 8 (0.789); leukoencephalopathy, progressive, with ovarian failure (0.767); ovarioleukodystrophy (0.619); neurodegenerative disease (0.536); hereditary disease (0.503)
- **Europe PMC papers**: 789
- **Why important**: AARS2 links the module to mitochondrial translation through mitochondrial alanyl-tRNA charging and translational fidelity. It is connected to MBLAC2, detected in both tissues, and has low tissue and immune-cell specificity. Its disease associations include combined oxidative phosphorylation deficiency and related mitochondrial disorders, and it has substantial literature support.
- **Conclusion**: Established: AARS2 is a mitochondrial aminoacyl-tRNA synthetase with clinically relevant links to oxidative-phosphorylation deficiency. Hypothesis: its co-abundance with the module may indicate altered mitochondrial protein-production demand or mitochondrial state. The module does not demonstrate that the other members directly control AARS2.

#### MIPEP

- **Related proteins** (co-abundance neighbors): MBLAC2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial intermediate peptidase. The product of this gene performs the final step in processing a specific class of nuclear-encoded proteins targeted to the mitochondrial matrix or inner membrane. This protein is primarily involved in the maturation of oxidative phosphorylation (OXPHOS)-related proteins. This gene may contribute to the functional effects of frataxin deficiency and the clinical manifestations of Friedreich ataxia.…
- **Diseases (Open Targets)**: Mitochondrial disorder due to a defect in mitochondrial protein synthesis (0.769); neurodegenerative disease (0.522); cardiomyopathy (0.402); left ventricular noncompaction (0.400); Floppy infant (0.398)
- **Europe PMC papers**: 457
- **Why important**: MIPEP provides a second, functionally distinct link to mitochondrial protein biology. It processes selected nuclear-encoded proteins targeted to the mitochondrial matrix or inner membrane and is primarily involved in maturation of oxidative-phosphorylation-related proteins. It is connected to MBLAC2, detected in both tissues, associated with mitochondrial disorders and cardiomyopathy, and supported by substantial literature.
- **Conclusion**: Established: MIPEP participates in mitochondrial protein processing and has disease associations involving mitochondrial dysfunction. Hypothesis: coordinated MIPEP and AARS2 abundance could reflect a mitochondrial maintenance or respiratory-protein maturation state. The data do not show a direct MIPEP interaction with the other module genes.

#### GALNT7

- **Related proteins** (co-abundance neighbors): MBLAC2 (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypeptide N-acetylgalactosaminyltransferase 7. This gene encodes GalNAc transferase 7, a member of the GalNAc-transferase family. The enzyme encoded by this gene controls the initiation step of mucin-type O-linked protein glycosylation and transfer of N-acetylgalactosamine to serine and threonine amino acid residues. This enzyme is a type II transmembrane protein and shares common sequence motifs with other family members. Unlike other family …
- **Diseases (Open Targets)**: immune system disorder (0.291); color vision disorder (0.254); Hydrocephalus (0.252); Parkinson disease (0.228); alcohol drinking (0.209)
- **Europe PMC papers**: 758
- **Why important**: GALNT7 is the module member with tissue-enhanced expression, reported in stomach, and it is cell-type enhanced in neutrophils and prostatic glandular cells. It encodes a Golgi GalNAc transferase that initiates mucin-type O-linked glycosylation and is connected to MBLAC2 in the co-abundance network. It has the largest literature volume among the listed genes and disease associations spanning immune, neurological and other traits.
- **Conclusion**: Established: GALNT7 performs a defined Golgi glycosylation function and contributes a secretory-pathway dimension to the module. Hypothesis: its co-abundance may reflect coordinated changes in protein trafficking or cell-state composition rather than a shared physical complex. The present evidence does not establish a mechanistic link between GALNT7 glycosylation and mitochondrial function.

#### MRPL11

- **Related proteins** (co-abundance neighbors): MBLAC2 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial ribosomal protein L11. This nuclear gene encodes a 39S subunit component of the mitochondial ribosome. Alternative splicing results in multiple transcript variants. Pseudogenes for this gene are found on chromosomes 5 and 12. [provided by RefSeq, May 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.484); type 2 diabetes mellitus (0.300); diabetes mellitus (0.264); bipolar disorder (0.023); asthma (0.019)
- **Europe PMC papers**: 355
- **Why important**: MRPL11 is the module member directly annotated as a mitochondrial ribosomal subunit component involved in mitochondrial translation. Although it has only one module connection, that connection is to the central MBLAC2 node. It is detected in both tissues, has low tissue and immune-cell specificity, and has substantial literature support.
- **Conclusion**: Established: MRPL11 contributes to mitochondrial ribosome function and mitochondrial translation. Hypothesis: its co-abundance may mark the same mitochondrial translational state represented by AARS2 and MIPEP. The network does not establish a direct molecular interaction between MRPL11 and those mitochondrial proteins.

## Module 21

**Tissue pair**: bone_marrow and kidney  
**Genes (6)**: PHF6, STRIP1, TPRKB, UNG, WDR48, ZZEF1

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established pathway-level functional assignment from enrichment. Its gene annotations instead suggest a mixed intracellular maintenance program involving cytoskeletal and Hippo-signaling regulation through STRIP1, translational fidelity through TPRKB, DNA damage and homologous recombination responses through WDR48, base-excision DNA repair through UNG, and transcriptional regulation through PHF6. ZZEF1 has predicted ubiquitin-like ligase activity and predicted roles in signaling and synaptic processes, but these predictions do not establish a shared module function. The sparse network and absence of STRING enrichment or hu.MAP complexes indicate that the module is better interpreted as a weakly coherent co-abundance pattern than as a demonstrated single biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: all listed proteins are intracellular and the secretome annotation is absent for every gene. HPA reports low tissue specificity across the module and low immune-cell specificity across the module, arguing against a clear blood-cell or tissue-specific signature. Several genes are enhanced in distinct cell types, including erythrocyte progenitors, megakaryocytes, neutrophils, germ-cell populations, enterocytes, cytotrophoblasts, oocytes, granulosa cells, and parietal cells. This diversity suggests broadly distributed cellular machinery with cell-state-specific expression rather than a uniform bone-marrow or kidney identity. Protein detection is present for most genes in both tissues, while one gene lacks protein-detection data, so the shared signal could reflect common intracellular cell populations or general cellular state rather than a tissue-restricted process.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and STRING functional enrichment is absent. No hu.MAP complex contains multiple module members. The co-abundance edges therefore are not supported by the supplied physical-interaction or complex resources. This does not disprove coordinated regulation, but it means the network is not presently corroborated as a known protein complex or interaction neighborhood. The apparent central position of STRIP1 is a property of this co-abundance network, not evidence of a confirmed physical hub.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared co-abundance pattern may be a new observation because it is not represented by reported STRING interactions, STRING enrichment, or a shared hu.MAP complex. However, those database absences do not establish biological novelty: the genes have substantial prior annotation and literature, and the pattern could arise from broad expression, shared cell states, correlated technical or sampling effects, or indirect regulation. The defensible conclusion is that the cross-tissue co-abundance configuration is potentially novel and currently weakly mechanistically validated, not that the genes or their functions are novel.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of broadly expressed intracellular maintenance factors in a shared cellular state present in bone marrow and kidney. STRIP1 may provide a regulatory or structural organizing context, while TPRKB may mark translational quality control, WDR48 and UNG may support genome-integrity maintenance, and PHF6 may connect the state to transcriptional regulation. This could represent a general stress, proliferation, differentiation, or repair-associated program, but the fact sheet does not distinguish among these possibilities. Direct testing should examine cell composition, replication across cohorts, and whether the genes change together under DNA damage, altered translation, or differentiation conditions.

### Important genes

#### STRIP1

- **Related proteins** (co-abundance neighbors): ZZEF1 (0.88), WDR48 (0.86), TPRKB (0.82), PHF6 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: striatin interacting protein 1. This gene encodes a member of the striatin-interacting phosphatase and kinase complex, which is involved in localization of the Golgi body. The encoded protein participates in cytosketelal organization. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2012].
- **Diseases (Open Targets)**: neurodegenerative disease (0.489); ocular hypotension (0.192); mathematical ability (0.130); Abnormality of the skeletal system (0.128); smoking initiation (0.124)
- **Europe PMC papers**: 202
- **Why important**: STRIP1 is the most connected gene in the module and links to ZZEF1, WDR48, TPRKB, and PHF6, making it the network's central organizing feature. Its established annotations include cytoskeleton organization and regulation of Hippo signaling. It is detected at the protein level in both tissues, has low tissue specificity, and has a substantial literature footprint. Its disease and trait associations include neurodegenerative disease, ocular hypotension, mathematical ability, skeletal abnormality, and smoking initiation.
- **Conclusion**: Established evidence supports STRIP1 as a broadly expressed cytoskeletal and signaling regulator and as the co-abundance hub of this module. It is plausible that STRIP1 helps organize the shared expression state, but a causal hub role and physical interaction with the other module members remain hypotheses.

#### UNG

- **Related proteins** (co-abundance neighbors): TPRKB (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: uracil DNA glycosylase. This gene encodes one of several uracil-DNA glycosylases. One important function of uracil-DNA glycosylases is to prevent mutagenesis by eliminating uracil from DNA molecules by cleaving the N-glycosylic bond and initiating the base-excision repair (BER) pathway. Uracil bases occur from cytosine deamination or misincorporation of dUMP residues. Alternative promoter usage and splicing of this gene …
- **Diseases (Open Targets)**: hyper-IgM syndrome type 5 (0.748); food allergy (0.172); hereditary breast ovarian cancer syndrome (0.118); neoplasm (0.111); infection (0.098)
- **Europe PMC papers**: 13689
- **Why important**: UNG is connected to TPRKB and has a well-established role in removing uracil from DNA and initiating base-excision repair, with nuclear and mitochondrial isoforms described in the fact sheet. It has the strongest literature footprint among the module genes and is associated with hyper-IgM syndrome type five, food allergy, hereditary breast ovarian cancer syndrome, neoplasm, and infection. Protein detection is reported in both tissues.
- **Conclusion**: Established evidence identifies UNG as a DNA-repair factor with clinically relevant immune and cancer associations. Its inclusion supports a possible genome-integrity component of the module, but the co-abundance data do not demonstrate that DNA repair is the module's dominant function.

#### TPRKB

- **Related proteins** (co-abundance neighbors): UNG (0.83), STRIP1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TP53RK binding protein. Enables protein kinase binding activity. Involved in tRNA threonylcarbamoyladenosine modification. Located in cytosol and nucleus. Part of EKC/KEOPS complex. Implicated in Galloway-Mowat syndrome 5. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Galloway-Mowat syndrome (0.667); neurodegenerative disease (0.526); thyroiditis (0.154); nephrotic syndrome (0.112); vascular disorder (0.063)
- **Europe PMC papers**: 494
- **Why important**: TPRKB connects UNG with the central STRIP1 node. It is an established component of the KEOPS complex and participates in tRNA threonylcarbamoyladenosine modification and maintenance of translational fidelity. It is detected in both tissues and has disease associations including Galloway-Mowat syndrome, neurodegenerative disease, thyroiditis, nephrotic syndrome, and vascular disorder.
- **Conclusion**: Established evidence supports TPRKB as a translational-quality-control factor and gives the module a plausible proteostasis or cellular-fidelity dimension. Its role as a bridge between translation-related biology and UNG or STRIP1 in this module is hypothetical because no STRING or hu.MAP support is reported.

#### PHF6

- **Related proteins** (co-abundance neighbors): STRIP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in bone_marrow, kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PHD finger protein 6. This gene is a member of the plant homeodomain (PHD)-like finger (PHF) family. It encodes a protein with two PHD-type zinc finger domains, indicating a potential role in transcriptional regulation, that localizes to the nucleolus. Mutations affecting the coding region of this gene or the splicing of the transcript have been associated with Borjeson-Forssman-Lehmann syndrome (BFLS), a disorder char…
- **Diseases (Open Targets)**: Borjeson-Forssman-Lehmann syndrome (0.821); neurodegenerative disease (0.540); hereditary disease (0.521); acute myeloid leukemia (0.500); Intellectual disability (0.456)
- **Europe PMC papers**: 2392
- **Why important**: PHF6 connects to STRIP1 and is a nucleolar and nucleoplasmic PHD-family protein with annotated roles in transcriptional regulation. It is detected in both tissues and is enhanced in erythrocyte progenitors and granulosa cells. Its associations include Borjeson-Forssman-Lehmann syndrome, neurodegenerative disease, hereditary disease, acute myeloid leukemia, and intellectual disability. It also has a substantial literature footprint.
- **Conclusion**: Established evidence supports PHF6 as a transcriptional and nucleolar regulator with developmental and disease relevance. It could connect the co-abundance pattern to cell differentiation or gene-expression control, but that connection is a hypothesis rather than a demonstrated module mechanism.
