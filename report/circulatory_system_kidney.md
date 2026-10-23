# Conserved co-abundance modules: circulatory_system and kidney

## Module 0

**Tissue pair**: circulatory_system and kidney  
**Genes (33)**: MPG, ADNP, BRD2, CPSF1, DDX31, DDX41, DHX8, MCAT, GRSF1, HAUS5, HMG20A, INTS1, INTS4, INTS9, KIF23, MTA2, MTA3, PCNT, PTCD3, RBM15B, UPF3B, RIOX1, RIOX2, MRPS22, MRPS27, MRPS35, TAF2, TAF6, GTF3C2, GTF3C4, TLE3, TOP2A, FYTTD1

### Function

The module is best interpreted as a nuclear gene-expression and RNA-processing program with a linked mitochondrial translation component. The primary evidence is the globally corrected enrichment for transcription-regulator complexes (GO:CC transcription regulator complex; q_global = 0.000849), gene expression (GO:BP gene expression; q_global = 0.0015), RNA biosynthetic processes (GO:BP RNA biosynthetic process; q_global = 0.00179) (GO:BP nucleic acid biosynthetic process; q_global = 0.00326), macromolecule biosynthesis (GO:BP macromolecule biosynthetic process; q_global = 0.00408), RNA metabolism (GO:BP RNA metabolic process; q_global = 0.00832), regulation of RNA metabolism (GO:BP regulation of RNA metabolic process; q_global = 0.0168), nucleic-acid metabolism (GO:BP nucleic acid metabolic process; q_global = 0.0192), general transcription initiation factor activity (GO:MF general transcription initiation factor activity; q_global = 0.031), and DNA-templated transcription (GO:BP DNA-templated transcription; q_global = 0.0316). The mitochondrial small-ribosomal-subunit terms (GO:CC organellar small ribosomal subunit; q_global = 0.00471) (GO:CC mitochondrial small ribosomal subunit; q_global = 0.00471) (GO:CC small ribosomal subunit; q_global = 0.0159) identify a coherent secondary arm involving MRPS22, MRPS27, MRPS35, and PTCD3. The module therefore appears to combine transcriptional regulation, RNA maturation and surveillance, chromatin control, and mitochondrial protein synthesis rather than representing a tissue-specific secreted pathway. The presence of TOP2A, KIF23, HAUS5, and PCNT also suggests that a proliferative or cell-cycle-associated component may contribute to the co-abundance pattern, although this is not the dominant enrichment signal.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the annotated proteins are predominantly nuclear, nucleolar, mitochondrial, or centrosomal. Most genes have low tissue specificity, which is compatible with a broadly expressed housekeeping-type program. The module is not strongly blood-cell specific overall, because most genes have low immune-cell specificity. Nevertheless, selected genes show enrichment or enhancement in lymphoid tissue, bone marrow, neutrophils, eosinophils, T-reg cells, erythrocyte progenitors, and other proliferative or specialized cell types. Kidney protein detection is present for many genes, whereas the circulatory-system protein comparison has no matching HPA tissue data. Thus, the shared module may partly reflect broadly expressed cellular machinery and shared cell-state composition in the sampled tissues; the evidence does not support interpreting it as a circulating secretome.

**GO/KEGG enrichment**: 21 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC transcription regulator complex | 0.000849 | ADNP, GTF3C2, GTF3C4, MTA2, MTA3, RIOX2, TAF2, TAF6, TLE3 |
| GO:BP gene expression | 0.0015 | ADNP, BRD2, CPSF1, DDX41, DHX8, FYTTD1, GRSF1, GTF3C2, GTF3C4, HMG20A, INTS1, INTS4, INTS9, MRPS22, MRPS27, MRPS35, MTA2, MTA3, PTCD3, RBM15B, RIOX1, RIOX2, TAF2, TAF6, TLE3, TOP2A, UPF3B |
| GO:BP RNA biosynthetic process | 0.00179 | ADNP, BRD2, CPSF1, DDX41, DHX8, GRSF1, GTF3C2, GTF3C4, HMG20A, INTS1, INTS4, INTS9, MTA2, MTA3, RBM15B, RIOX1, RIOX2, TAF2, TAF6, TLE3, TOP2A, UPF3B |
| GO:BP nucleic acid biosynthetic process | 0.00326 | ADNP, BRD2, CPSF1, DDX41, DHX8, GRSF1, GTF3C2, GTF3C4, HMG20A, INTS1, INTS4, INTS9, MTA2, MTA3, RBM15B, RIOX1, RIOX2, TAF2, TAF6, TLE3, TOP2A, UPF3B |
| GO:BP macromolecule biosynthetic process | 0.00408 | ADNP, BRD2, CPSF1, DDX41, DHX8, FYTTD1, GRSF1, GTF3C2, GTF3C4, HMG20A, INTS1, INTS4, INTS9, MRPS22, MRPS27, MRPS35, MTA2, MTA3, PTCD3, RBM15B, RIOX1, RIOX2, TAF2, TAF6, TLE3, TOP2A, UPF3B |
| GO:CC organellar small ribosomal subunit | 0.00471 | MRPS22, MRPS27, MRPS35, PTCD3 |
| GO:CC mitochondrial small ribosomal subunit | 0.00471 | MRPS22, MRPS27, MRPS35, PTCD3 |
| GO:MF nucleic acid binding | 0.00472 | ADNP, CPSF1, DDX31, DDX41, DHX8, FYTTD1, GRSF1, GTF3C2, GTF3C4, HMG20A, MCAT, MPG, MRPS27, MRPS35, MTA2, MTA3, PTCD3, RBM15B, TAF2, TAF6, TOP2A, UPF3B |
| GO:BP RNA metabolic process | 0.00832 | ADNP, BRD2, CPSF1, DDX41, DHX8, GRSF1, GTF3C2, GTF3C4, HMG20A, INTS1, INTS4, INTS9, MTA2, MTA3, RBM15B, RIOX1, RIOX2, TAF2, TAF6, TLE3, TOP2A, UPF3B |
| GO:CC nuclear lumen | 0.00972 | BRD2, CPSF1, DDX31, DDX41, DHX8, FYTTD1, GRSF1, GTF3C2, GTF3C4, INTS1, INTS4, INTS9, KIF23, MPG, MRPS27, MTA2, MTA3, PTCD3, RBM15B, RIOX1, RIOX2, TAF2, TAF6, TLE3, TOP2A, UPF3B |
| GO:CC small ribosomal subunit | 0.0159 | MRPS22, MRPS27, MRPS35, PTCD3 |
| GO:BP regulation of RNA metabolic process | 0.0168 | ADNP, BRD2, GRSF1, HMG20A, INTS1, INTS4, INTS9, MTA2, MTA3, RBM15B, RIOX1, RIOX2, TAF2, TAF6, TLE3, TOP2A, UPF3B |
| GO:BP nucleic acid metabolic process | 0.0192 | ADNP, BRD2, CPSF1, DDX41, DHX8, GRSF1, GTF3C2, GTF3C4, HMG20A, INTS1, INTS4, INTS9, MPG, MTA2, MTA3, RBM15B, RIOX1, RIOX2, TAF2, TAF6, TLE3, TOP2A, UPF3B |
| GO:CC membrane-enclosed lumen | 0.0194 | BRD2, CPSF1, DDX31, DDX41, DHX8, FYTTD1, GRSF1, GTF3C2, GTF3C4, INTS1, INTS4, INTS9, KIF23, MCAT, MPG, MRPS22, MRPS27, MRPS35, MTA2, MTA3, PTCD3, RBM15B, RIOX1, RIOX2, TAF2, TAF6, TLE3, TOP2A, UPF3B |
| GO:CC organelle lumen | 0.0194 | BRD2, CPSF1, DDX31, DDX41, DHX8, FYTTD1, GRSF1, GTF3C2, GTF3C4, INTS1, INTS4, INTS9, KIF23, MCAT, MPG, MRPS22, MRPS27, MRPS35, MTA2, MTA3, PTCD3, RBM15B, RIOX1, RIOX2, TAF2, TAF6, TLE3, TOP2A, UPF3B |

### STRING and hu.MAP

STRING supports established molecular relationships rather than an entirely disconnected co-abundance cluster. The strongest known links include the TFIIIC pair GTF3C2–GTF3C4, the TFIID pair TAF2–TAF6, the Integrator links among INTS1, INTS4, and INTS9, the MTA2–MTA3 chromatin-regulatory pair, and the mitochondrial small-ribosomal-subunit links among MRPS22, MRPS27, MRPS35, and PTCD3. STRING also connects KIF23 with TOP2A, CPSF1 with INTS9, and RNA-processing factors including DDX41, DHX8, and UPF3B. These relationships are supplementary network support and should not be treated as globally corrected enrichment. hu.MAP independently recovers partial Integrator complexes containing INTS1, INTS4, and INTS9; mitochondrial ribosomal assemblies containing MRPS22, MRPS27, MRPS35, PTCD3, and MCAT; MTA-containing chromatin-remodeling complexes; TFIIIC complexes containing GTF3C2 and GTF3C4; and TAF complexes containing TAF2 and TAF6. Thus, several module edges correspond to known complexes, while other co-abundance connections likely reflect shared regulation, cell state, or indirect functional coupling.

**STRING interactions (score >= 0.7)**: 21 of 528 gene pairs: BRD2–TAF6 (0.789); CPSF1–INTS9 (0.758); DDX41–UPF3B (0.811); DHX8–UPF3B (0.828); GTF3C2–GTF3C4 (0.993); INTS1–INTS4 (0.999); INTS1–INTS9 (0.999); INTS4–INTS9 (0.999); KIF23–TOP2A (0.927); MCAT–MRPS22 (0.888); MCAT–MRPS27 (0.871); MCAT–MRPS35 (0.855); MCAT–PTCD3 (0.862); MRPS22–MRPS27 (0.999); MRPS22–MRPS35 (0.998); MRPS22–PTCD3 (0.999); MRPS27–MRPS35 (0.991); MRPS27–PTCD3 (0.996); MRPS35–PTCD3 (0.999); MTA2–MTA3 (0.966); TAF2–TAF6 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Transcription regulator complex (FDR = 0.00069, 9 genes); NetworkNeighborAL Organellar small ribosomal subunit (FDR = 0.0021, 4 genes); Keyword Nucleus (FDR = 0.0032, 25 genes); Component Mitochondrial small ribosomal subunit (FDR = 0.0042, 4 genes); Component Nuclear lumen (FDR = 0.0045, 25 genes); COMPARTMENTS Mitochondrial small ribosomal subunit (FDR = 0.0067, 4 genes); Component Nucleoplasm (FDR = 0.0075, 23 genes); Component Intracellular organelle lumen (FDR = 0.0075, 28 genes); COMPARTMENTS Nucleus (FDR = 0.0103, 25 genes); Component Nuclear protein-containing complex (FDR = 0.0136, 13 genes); Component Nucleus (FDR = 0.017, 28 genes); Component Protein-containing complex (FDR = 0.017, 25 genes); RCTM Gene expression (Transcription) (FDR = 0.0177, 13 genes); Function Nucleic acid binding (FDR = 0.0218, 21 genes); Function General transcription initiation factor activity (FDR = 0.0218, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05807.1 (MRPS35, MCAT, MRPS27, PTCD3; 4/81); huMAP3_09363.1 (INTS1, INTS4, INTS9; 3/6); huMAP3_09230.1 (INTS1, INTS4, INTS9; 3/9); huMAP3_10641.1 (INTS1, INTS4, INTS9; 3/11); huMAP3_05954.1 (MRPS22, MRPS35, PTCD3; 3/28); huMAP3_03554.1 (MRPS35, PTCD3; 2/2); huMAP3_08985.1 (INTS4, INTS9; 2/4); huMAP3_06382.1 (INTS1, INTS4; 2/5); huMAP3_08278.1 (INTS1, INTS4; 2/6); huMAP3_05606.1 (MCAT, MRPS27; 2/7); huMAP3_06989.1 (INTS1, INTS4; 2/8); huMAP3_03905.1 (MTA2, MTA3; 2/10); huMAP3_05579.1 (MTA2, MTA3; 2/11); huMAP3_15286.1 (INTS4, INTS9; 2/12); huMAP3_12564.1 (INTS4, INTS9; 2/14); huMAP3_04798.1 (TAF6, TAF2; 2/14); huMAP3_10875.1 (GTF3C2, GTF3C4; 2/14); huMAP3_08738.1 (MTA2, MTA3; 2/17); huMAP3_00288.1 (TAF6, TAF2; 2/17); huMAP3_14957.1 (TAF6, TAF2; 2/19); huMAP3_08438.1 (TAF6, TAF2; 2/23); huMAP3_14501.1 (TAF6, TAF2; 2/24); huMAP3_09451.1 (TAF6, TAF2; 2/25); huMAP3_09499.1 (MTA2, MTA3; 2/33); huMAP3_10472.1 (MTA2, MTA3; 2/36); huMAP3_10385.1 (TAF6, TAF2; 2/40); huMAP3_09943.1 (FYTTD1, DDX41; 2/78); huMAP3_13510.1 (INTS4, INTS9; 2/85); huMAP3_15128.1 (MTA2, MTA3; 2/96)

### Novelty

The module should not be claimed as a newly discovered molecular complex. Several of its dense portions are already represented by known STRING relationships and hu.MAP complexes, especially the Integrator, mitochondrial small-ribosomal-subunit, TFIIIC, TFIID, and MTA-associated chromatin assemblies. Its potentially novel aspect is the coordinated co-abundance of these established machinery components across circulatory_system and kidney. That cross-tissue organization may be a new systems-level observation, but the fact sheet alone does not establish tissue specificity, causality, or biological novelty. Absence of an edge from STRING or hu.MAP would not prove novelty, because these resources are incomplete and represent physical or curated relationships rather than every shared regulatory or abundance relationship. Replication in independent cohorts, cell-composition adjustment, and comparison with previously reported cross-tissue modules would be needed to support a novelty claim.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular maintenance and proliferative-state program in which chromatin and transcription regulators coordinate RNA synthesis, processing, surveillance, and export, while a linked mitochondrial ribosomal arm supports mitochondrial translation and energy-demanding cellular activity. In kidney and circulatory-system samples, this program may be observed because both tissues contain broadly expressing cells and variable proportions of proliferative or immune-associated cell types. The hypothesis predicts coordinated changes between the nuclear transcription/RNA-processing arm and the mitochondrial translation arm, but the co-abundance data do not by themselves demonstrate direct regulation or physical assembly between these arms.

### Important genes

#### GTF3C2

- **Related proteins** (co-abundance neighbors): DHX8 (0.88), CPSF1 (0.86), TAF6 (0.86), RIOX1 (0.84), MTA3 (0.84), ADNP (0.83), GTF3C4 (0.82); STRING partners: GTF3C4 (0.993)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_10875.1
- **Function (MyGene.info)**: general transcription factor IIIC subunit 2. Contributes to DNA binding activity. Involved in transcription by RNA polymerase III. Located in nucleoplasm. Part of transcription factor TFIIIC complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.534); diverticular disease (0.195); hepatocellular carcinoma (0.076); essential tremor (0.067); neoplasm (0.048)
- **Europe PMC papers**: 239
- **Why important**: GTF3C2 is a leading network connector in the module and links multiple RNA-processing, transcriptional, and chromatin-associated genes. It is part of TFIIIC and is annotated for RNA polymerase III transcription, including tRNA and five-S rRNA transcription. It participates in the globally significant transcription-regulator-complex and gene-expression evidence (5 globally significant GO/KEGG terms, q_global 0.000849–0.0316; see the table). Its relationship with GTF3C4 is strongly supported by STRING and by hu.MAP (hu.MAP huMAP3_10875.1). The literature volume is substantial, and disease associations include neurodegenerative disease and several other conditions.
- **Conclusion**: Established evidence supports GTF3C2 as a transcriptional hub and TFIIIC component within this module. It is a plausible anchor for the nuclear gene-expression interpretation. It remains a hypothesis that its abundance specifically coordinates the kidney–circulatory shared module or drives the mitochondrial arm.

#### MTA3

- **Related proteins** (co-abundance neighbors): UPF3B (0.91), MTA2 (0.85), PCNT (0.85), GTF3C2 (0.84), HMG20A (0.81), FYTTD1 (0.81), RIOX2 (0.80); STRING partners: MTA2 (0.966)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_03905.1, huMAP3_05579.1, huMAP3_08738.1, huMAP3_09499.1, huMAP3_10472.1, huMAP3_15128.1
- **Function (MyGene.info)**: metastasis associated 1 family member 3. Predicted to enable histone deacetylase binding activity; transcription coactivator activity; and transcription corepressor activity. Involved in negative regulation of transcription, DNA-templated. Located in nucleoplasm. Part of NuRD complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.336); Short stature (0.259); urolithiasis (0.252); alcohol drinking (0.252); neurodegenerative disease (0.226)
- **Europe PMC papers**: 1053
- **Why important**: MTA3 has high network connectivity and connects the MTA2 chromatin-regulatory pair with transcription, RNA-processing, and chromatin-associated genes. It is annotated as a NuRD-complex component with transcriptional corepressor and chromatin-remodeling functions and contributes to the globally significant transcription-regulator-complex and transcriptional-process terms (5 globally significant GO/KEGG terms, q_global 0.000849–0.0316; see the table). STRING supports its relationship with MTA2, while hu.MAP repeatedly places the pair in MTA-containing complexes (hu.MAP huMAP3_03905.1) (hu.MAP huMAP3_05579.1) (hu.MAP huMAP3_08738.1) (hu.MAP huMAP3_09499.1) (hu.MAP huMAP3_10472.1) (hu.MAP huMAP3_15128.1). It has a substantial literature base and reported associations with skeletal abnormalities, short stature, urolithiasis, and neurodegenerative disease.
- **Conclusion**: Established evidence supports MTA3 as a chromatin and transcriptional regulatory component that helps explain the module's nuclear regulatory character. Its tissue enhancement in lymphoid tissue may also make it sensitive to cell-composition differences. A direct role in coordinating the shared tissue module is a hypothesis rather than an established finding.

#### INTS1

- **Related proteins** (co-abundance neighbors): INTS9 (0.81); STRING partners: INTS4 (0.999), INTS9 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_09363.1, huMAP3_09230.1, huMAP3_10641.1, huMAP3_06382.1, huMAP3_08278.1, huMAP3_06989.1
- **Function (MyGene.info)**: integrator complex subunit 1. INTS1 is a subunit of the Integrator complex, which associates with the C-terminal domain of RNA polymerase II large subunit (POLR2A; MIM 180660) and mediates 3-prime end processing of small nuclear RNAs U1 (RNU1; MIM 180680) and U2 (RNU2; MIM 180690) (Baillat et al., 2005 [PubMed 16239144]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: neurodevelopmental disorder with cataracts, poor growth, and dysmorphic facies (0.763); hereditary disease (0.488); placental abruption (0.340); Neurodevelopmental delay (0.335); neurodegenerative disease (0.267)
- **Europe PMC papers**: 642
- **Why important**: INTS1 is a member of the Integrator complex and is connected in the module to INTS4 and INTS9. The Integrator triad is supported by near-complete STRING relationships and by multiple hu.MAP complexes (hu.MAP huMAP3_09363.1) (hu.MAP huMAP3_09230.1) (hu.MAP huMAP3_10641.1) (hu.MAP huMAP3_06382.1) (hu.MAP huMAP3_08278.1) (hu.MAP huMAP3_06989.1). INTS1 contributes to the globally significant gene-expression, RNA-biosynthetic, RNA-metabolic, and transcriptional terms (5 globally significant GO/KEGG terms, q_global 0.0015–0.0316; see the table). Its established function in small nuclear RNA processing and transcription surveillance provides a mechanistic bridge between transcription and RNA maturation. It also has disease associations involving neurodevelopmental disorders and placental or hereditary conditions.
- **Conclusion**: Established evidence supports INTS1 as a core RNA-processing and transcription-surveillance component of the module. The coordinated abundance of INTS1, INTS4, and INTS9 is consistent with Integrator-complex biology. It is not established that this Integrator signal is specific to kidney or circulatory biology.

#### PTCD3

- **Related proteins** (co-abundance neighbors): MRPS22 (0.86), MRPS27 (0.82), MCAT (0.80); STRING partners: MCAT (0.862), MRPS22 (0.999), MRPS27 (0.996), MRPS35 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_05807.1, huMAP3_05954.1, huMAP3_03554.1
- **Function (MyGene.info)**: pentatricopeptide repeat domain 3. Enables rRNA binding activity and ribosomal small subunit binding activity. Involved in mitochondrial translation. Located in several cellular components, including cytosol; mitochondrion; and nucleoplasm. Implicated in combined oxidative phosphorylation deficiency 51. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: combined oxidative phosphorylation deficiency 51 (0.678); mixed connective tissue disease (0.230); hereditary disease (0.193); alcohol drinking (0.110); posterior cortical atrophy (0.074)
- **Europe PMC papers**: 308
- **Why important**: PTCD3 is part of the tightly connected mitochondrial small-ribosomal-subunit cluster with MRPS22, MRPS27, and MRPS35. This cluster is supported by the globally significant mitochondrial ribosomal terms (GO:CC organellar small ribosomal subunit; q_global = 0.00471) (GO:CC mitochondrial small ribosomal subunit; q_global = 0.00471) (GO:CC small ribosomal subunit; q_global = 0.0159), STRING relationships (STRING NetworkNeighborAL Organellar small ribosomal subunit; within-query FDR = 0.0021) (STRING Component Mitochondrial small ribosomal subunit; within-query FDR = 0.0042) (STRING COMPARTMENTS Mitochondrial small ribosomal subunit; within-query FDR = 0.0067), and hu.MAP complexes (hu.MAP huMAP3_05807.1) (hu.MAP huMAP3_05954.1) (hu.MAP huMAP3_03554.1). PTCD3 is annotated for rRNA binding, small-subunit binding, and mitochondrial translation, and it is associated with combined oxidative phosphorylation deficiency. Its module position makes it a representative connector for the mitochondrial arm, while its kidney protein detection supports biological presence in kidney samples.
- **Conclusion**: Established evidence supports PTCD3 as a mitochondrial translation component and a strong indicator that the module is not purely nuclear. The hypothesis that this mitochondrial arm is functionally coupled to the transcription and RNA-processing arm through cellular energy demand is plausible but not demonstrated by the supplied data.

#### TAF6

- **Related proteins** (co-abundance neighbors): GTF3C2 (0.86), DHX8 (0.84), HMG20A (0.82); STRING partners: BRD2 (0.789), TAF2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_04798.1, huMAP3_00288.1, huMAP3_14957.1, huMAP3_08438.1, huMAP3_14501.1, huMAP3_09451.1, huMAP3_10385.1
- **Function (MyGene.info)**: TATA-box binding protein associated factor 6. Initiation of transcription by RNA polymerase II requires the activities of more than 70 polypeptides. The protein that coordinates these activities is transcription factor IID (TFIID), which binds to the core promoter to position the polymerase properly, serves as the scaffold for assembly of the remainder of the transcription complex, and acts as a channel for regulatory signals. TFIID is compos…
- **Diseases (Open Targets)**: Alazami-Yuan syndrome (0.681); HIV infectious disease (0.578); hereditary disease (0.470); neurodegenerative disease (0.420); Intellectual disability (0.407)
- **Europe PMC papers**: 773
- **Why important**: TAF6 is a component of TFIID and supports transcription initiation by RNA polymerase II. It participates in the transcription-regulator-complex, gene-expression, RNA-biosynthetic, general-transcription-initiation, and DNA-templated-transcription evidence (5 globally significant GO/KEGG terms, q_global 0.000849–0.0316; see the table). Its relationship with TAF2 is strongly supported by STRING, and hu.MAP repeatedly places TAF2 and TAF6 in TFIID and related transcription complexes (hu.MAP huMAP3_04798.1) (hu.MAP huMAP3_00288.1) (hu.MAP huMAP3_14957.1) (hu.MAP huMAP3_08438.1) (hu.MAP huMAP3_14501.1) (hu.MAP huMAP3_09451.1) (hu.MAP huMAP3_10385.1). It has a substantial literature base and disease associations including Alazami-Yuan syndrome, hereditary disease, neurodegenerative disease, and intellectual disability.
- **Conclusion**: Established evidence supports TAF6 as a transcription-initiation scaffold that reinforces the module's core gene-expression interpretation. Its module connectivity is more consistent with participation in known transcription machinery than with a novel tissue-specific function. Any role in linking transcription initiation to mitochondrial translation remains hypothetical.

## Module 1

**Tissue pair**: circulatory_system and kidney  
**Genes (33)**: NT5C3B, AIMP1, CCAR1, CHAMP1, COG6, CEP131, DIDO1, ADAR, EHMT2, ERCC5, INTS7, KAT7, LIMD1, ATF7IP, MTMR1, NBN, NCOR1, NECAP2, PI4KB, PRPF31, PRP4K, PRPF4, RBM10, RBM22, RBMS1, RTCA, TNRC6B, UIMC1, UNK, WDR33, XRN1, XRN2, RCHY1

### Function

The module is best interpreted as a broadly expressed nuclear gene-expression and RNA-metabolism module. The primary evidence is the global enrichment for nucleic acid metabolic process (GO:BP nucleic acid metabolic process; q_global = 0.00118), nucleic acid binding (GO:MF nucleic acid binding; q_global = 0.00472), gene expression (GO:BP gene expression; q_global = 0.00673), RNA metabolic process (GO:BP RNA metabolic process; q_global = 0.00832), nucleic acid biosynthetic process (GO:BP nucleic acid biosynthetic process; q_global = 0.0127), macromolecule biosynthetic process (GO:BP macromolecule biosynthetic process; q_global = 0.0169), nucleobase-containing compound metabolic process (GO:BP nucleobase-containing compound metabolic process; q_global = 0.0271), nuclear body (GO:CC nuclear body; q_global = 0.0332), and biosynthetic process (GO:BP biosynthetic process; q_global = 0.0474). The genes span pre-mRNA splicing and spliceosomal assembly, RNA editing, RNA degradation, RNA processing, transcriptional regulation, chromatin modification, DNA repair, and nuclear surveillance. The enrichment therefore supports a coordinated housekeeping-like nuclear program rather than a narrowly specialized circulatory or kidney pathway. The STRING results are concordant but supplementary: they point to nucleic acid metabolism, RNA binding, mRNA processing, nuclear bodies, and the major spliceosome (10 supplementary STRING terms; within-query FDR 0.0023–0.0474).

**Cell composition.** This is not primarily a plasma or secreted-protein module: only AIMP1 is annotated as secreted to blood, while the remainder are intracellular proteins. All module genes have low tissue specificity in HPA, arguing against a kidney-specific or circulatory-system-specific molecular program. Most genes also have low immune-cell specificity, so the module is not strongly blood-cell restricted. Nevertheless, several genes show cell-type enhancement in neutrophils or other hematopoietic cells, including UIMC1, ADAR, RBM22, XRN2, NBN, RBMS1, and TNRC6B, and UIMC1 and TNRC6B are immune-cell enhanced in the blood-cell summary. AIMP1 may contribute a blood-associated extracellular signal, but it is a minority component. The shared signal could therefore partly reflect ubiquitous cellular machinery present in both tissues and, in some samples, shared leukocyte or neutrophil content. Detection of most proteins in kidney is compatible with the module being present in kidney cells, but HPA does not establish that the co-abundance relationship originates from renal cells rather than mixed tissue composition.

**GO/KEGG enrichment**: 9 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP nucleic acid metabolic process | 0.00118 | ADAR, ATF7IP, CCAR1, DIDO1, EHMT2, ERCC5, INTS7, KAT7, LIMD1, NBN, NCOR1, NT5C3B, PRP4K, PRPF31, PRPF4, RBM10, RBM22, RBMS1, RCHY1, RTCA, TNRC6B, UIMC1, WDR33, XRN1, XRN2 |
| GO:MF nucleic acid binding | 0.00472 | ADAR, AIMP1, CCAR1, DIDO1, EHMT2, ERCC5, KAT7, NBN, NCOR1, PRP4K, PRPF31, PRPF4, RBM10, RBM22, RBMS1, RTCA, TNRC6B, UIMC1, UNK, WDR33, XRN1, XRN2 |
| GO:BP gene expression | 0.00673 | ADAR, AIMP1, ATF7IP, CCAR1, DIDO1, EHMT2, INTS7, KAT7, LIMD1, NBN, NCOR1, NT5C3B, PRP4K, PRPF31, PRPF4, RBM10, RBM22, RBMS1, RCHY1, RTCA, TNRC6B, UIMC1, UNK, WDR33, XRN1, XRN2 |
| GO:BP RNA metabolic process | 0.00832 | ADAR, ATF7IP, CCAR1, DIDO1, EHMT2, INTS7, KAT7, LIMD1, NCOR1, NT5C3B, PRP4K, PRPF31, PRPF4, RBM10, RBM22, RBMS1, RTCA, TNRC6B, UIMC1, WDR33, XRN1, XRN2 |
| GO:BP nucleic acid biosynthetic process | 0.0127 | ADAR, ATF7IP, CCAR1, DIDO1, EHMT2, INTS7, KAT7, LIMD1, NCOR1, PRP4K, PRPF31, PRPF4, RBM10, RBM22, RBMS1, RCHY1, RTCA, UIMC1, WDR33, XRN1, XRN2 |
| GO:BP macromolecule biosynthetic process | 0.0169 | ADAR, AIMP1, ATF7IP, CCAR1, DIDO1, EHMT2, INTS7, KAT7, LIMD1, NBN, NCOR1, NT5C3B, PRP4K, PRPF31, PRPF4, RBM10, RBM22, RBMS1, RCHY1, RTCA, TNRC6B, UIMC1, UNK, WDR33, XRN1, XRN2 |
| GO:BP nucleobase-containing compound metabolic process | 0.0271 | ADAR, ATF7IP, CCAR1, DIDO1, EHMT2, ERCC5, INTS7, KAT7, LIMD1, NBN, NCOR1, NT5C3B, PRP4K, PRPF31, PRPF4, RBM10, RBM22, RBMS1, RCHY1, RTCA, TNRC6B, UIMC1, WDR33, XRN1, XRN2 |
| GO:CC nuclear body | 0.0332 | ATF7IP, CHAMP1, EHMT2, INTS7, NBN, PRP4K, PRPF31, PRPF4, RBM10, RCHY1, UIMC1 |
| GO:BP biosynthetic process | 0.0474 | ADAR, AIMP1, ATF7IP, CCAR1, DIDO1, EHMT2, INTS7, KAT7, LIMD1, MTMR1, NBN, NCOR1, NT5C3B, PI4KB, PRP4K, PRPF31, PRPF4, RBM10, RBM22, RBMS1, RCHY1, RTCA, TNRC6B, UIMC1, UNK, WDR33, XRN1, XRN2 |

### STRING and hu.MAP

STRING provides several established relationships within the module. PRPF4, PRPF31, and PRP4K form a strongly supported spliceosomal interaction group, CCAR1 connects to RBM10 and PRP4K, XRN1 connects to XRN2, NBN connects to UIMC1, and MTMR1 connects to PI4KB. These relationships support real molecular substructures rather than a purely statistical association. The STRING functional results additionally support major-spliceosome and mRNA-processing involvement (STRING Keyword mRNA processing; within-query FDR = 0.0155) and (STRING NetworkNeighborAL U2-type spliceosomal complex, and mRNA Splicing - Major Pathway; within-query FDR = 0.0319), but they remain supplementary rather than globally corrected enrichment evidence. hu.MAP independently places module members in known or candidate assemblies: RBM10 with CCAR1 and UIMC1 (hu.MAP huMAP3_11912.1), RBM10 with CCAR1 in another RNA-associated complex (hu.MAP huMAP3_10359.1), CHAMP1 with EHMT2 in a chromatin-associated complex (hu.MAP huMAP3_11539.1), RBMS1 with ADAR in an RNA-binding complex (hu.MAP huMAP3_10625.1), NECAP2 with TNRC6B in endocytic complexes (hu.MAP huMAP3_10762.1) and (hu.MAP huMAP3_12394.1), and PRPF4 with PRPF31 in spliceosomal complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1). These complexes explain parts of the module, especially RNA processing, chromatin regulation, and vesicle-associated signaling, but the module does not correspond to one complete known complex.

**STRING interactions (score >= 0.7)**: 8 of 528 gene pairs: CCAR1–PRP4K (0.763); CCAR1–RBM10 (0.743); MTMR1–PI4KB (0.742); NBN–UIMC1 (0.768); PRP4K–PRPF31 (0.965); PRP4K–PRPF4 (0.959); PRPF31–PRPF4 (0.999); XRN1–XRN2 (0.985)
**STRING functional enrichment (supplementary, within-query FDR)**: Process Nucleic acid metabolic process (FDR = 0.0023, 21 genes); Function Nucleic acid binding (FDR = 0.0044, 22 genes); Keyword mRNA processing (FDR = 0.0155, 8 genes); Keyword Nucleus (FDR = 0.0155, 23 genes); Keyword Ubl conjugation (FDR = 0.0155, 17 genes); Keyword Zinc (FDR = 0.0155, 12 genes); Keyword Isopeptide bond (FDR = 0.0155, 15 genes); Component Nuclear body (FDR = 0.0185, 11 genes); NetworkNeighborAL U2-type spliceosomal complex, and mRNA Splicing - Major Pathway (FDR = 0.0319, 6 genes); COMPARTMENTS Nuclear body (FDR = 0.0474, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11912.1 (RBM10, CCAR1, UIMC1; 3/16); huMAP3_10359.1 (RBM10, CCAR1; 2/27); huMAP3_11539.1 (CHAMP1, EHMT2; 2/32); huMAP3_10625.1 (RBMS1, ADAR; 2/57); huMAP3_10762.1 (NECAP2, TNRC6B; 2/62); huMAP3_06511.1 (PRPF4, PRPF31; 2/79); huMAP3_08980.1 (PRPF4, PRPF31; 2/97); huMAP3_12394.1 (NECAP2, TNRC6B; 2/98)

### Novelty

The module should not be described as a wholly new molecular pathway. Its central biology is already established through canonical RNA-processing, spliceosomal, chromatin, DNA-repair, and RNA-decay functions, and several internal relationships are supported by STRING and hu.MAP. However, the particular cross-tissue co-abundance organization may still be a new observation. The network is relatively sparse and combines multiple known molecular neighborhoods that are not represented by one single hu.MAP complex. Many module pairs lack high-confidence STRING support and many genes have no matching hu.MAP entry in this module. That pattern suggests a potentially novel tissue-level co-abundance configuration, but absence from interaction databases is not evidence of biological novelty by itself. The appropriate conclusion is that the module provides a new systems-level association hypothesis built from largely known gene functions, rather than discovering an entirely new pathway or interaction complex.

**Hypothesis.** Mechanistic hypothesis: the shared circulatory-system and kidney signal reflects coordinated abundance of a broadly active nuclear RNA and genome-maintenance program. Core RNA-processing components such as PRPF4, PRPF31, RBM10, RBM22, ADAR, XRN1, and XRN2 could coordinate spliceosome activity, RNA editing, transcript maturation, and RNA decay, while EHMT2, ATF7IP, KAT7, NCOR1, and UIMC1 could couple this program to chromatin state, transcriptional repression or activation, and DNA-damage surveillance. The association with neutrophil-enhanced genes may indicate that part of the signal is contributed by shared blood or immune-cell content, whereas the broad HPA tissue distribution supports a general cellular maintenance program. This is a hypothesis generated by the integrated network and annotation evidence; the co-abundance data do not demonstrate physical assembly, causal regulation, or a tissue-specific mechanism.

### Important genes

#### PRPF4

- **Related proteins** (co-abundance neighbors): RBM10 (0.88), ATF7IP (0.80); STRING partners: PRP4K (0.959), PRPF31 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: pre-mRNA splicing tri-snRNP complex factor PRPF4. The protein encoded by this gene is part of a heteromeric complex that binds U4, U5, and U6 small nuclear RNAs and is involved in pre-mRNA splicing. The encoded protein also is a mitotic checkpoint protein and a regulator of chemoresistance in human ovarian cancer. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: retinitis pigmentosa (0.634); retinitis pigmentosa 70 (0.578); inherited retinal dystrophy (0.377); neurodegenerative disease (0.203); refractive error (0.083)
- **Europe PMC papers**: 461
- **Why important**: PRPF4 is a central representative of the spliceosomal component of the module. It is linked in the module to RBM10 and ATF7IP, has very strong STRING support with PRP4K and PRPF31, and is present with PRPF31 in two hu.MAP spliceosomal complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1). Its globally significant annotations cover nucleic acid metabolism, RNA metabolism, gene expression, and nuclear bodies (9 globally significant GO/KEGG terms, q_global 0.00118–0.0474; see the table). Its established disease associations include retinitis pigmentosa and inherited retinal dystrophy, and its literature supports a well-characterized role in spliceosomal assembly.
- **Conclusion**: Established evidence identifies PRPF4 as a spliceosomal scaffold or assembly factor that anchors the RNA-processing interpretation. The module data support its participation in a shared RNA-processing program, but do not establish that altered PRPF4 drives the cross-tissue co-abundance pattern.

#### PRPF31

- **Related proteins** (co-abundance neighbors): ATF7IP (0.85), KAT7 (0.80); STRING partners: PRP4K (0.965), PRPF4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: pre-mRNA processing factor 31. This gene encodes a component of the spliceosome complex and is one of several retinitis pigmentosa-causing genes. When the gene product is added to the spliceosome complex, activation occurs.[provided by RefSeq, Jan 2009].
- **Diseases (Open Targets)**: retinitis pigmentosa (0.798); inherited retinal dystrophy (0.576); autosomal dominant retinitis pigmentosa (0.376); eye disorder (0.371); cone-rod dystrophy (0.365)
- **Europe PMC papers**: 1184
- **Why important**: PRPF31 is one of the strongest molecularly supported spliceosomal genes in the module. It is connected to PRP4K and PRPF4 by STRING, with the PRPF4 relationship also represented in hu.MAP complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1). It occurs in every globally significant enrichment category (9 globally significant GO/KEGG terms, q_global 0.00118–0.0474; see the table), directly linking the gene to RNA processing, gene expression, nucleic acid metabolism, and nuclear bodies. It has established associations with retinitis pigmentosa and inherited retinal dystrophy and a substantial literature base.
- **Conclusion**: Established evidence supports PRPF31 as a core spliceosome-related component and a strong marker of the module's RNA-processing function. A module-specific role in circulatory-system or kidney biology remains hypothetical.

#### RBM10

- **Related proteins** (co-abundance neighbors): PRPF4 (0.88), RBMS1 (0.84); STRING partners: CCAR1 (0.743)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_11912.1, huMAP3_10359.1
- **Function (MyGene.info)**: RNA binding motif protein 10. This gene encodes a nuclear protein that belongs to a family proteins that contain an RNA-binding motif. The encoded protein associates with hnRNP proteins and may be involved in regulating alternative splicing. Defects in this gene are the cause of the X-linked recessive disorder, TARP syndrome. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Mar 2011].
- **Diseases (Open Targets)**: TARP syndrome (0.787); lung adenocarcinoma (0.629); neurodegenerative disease (0.526); pancreatic adenocarcinoma (0.513); non-small cell lung carcinoma (0.510)
- **Europe PMC papers**: 1601
- **Why important**: RBM10 connects the spliceosomal and RNA-binding portions of the module. It is linked to PRPF4 and RBMS1 in the co-abundance graph, has STRING support with CCAR1, and occurs in two hu.MAP RNA-associated complexes (hu.MAP huMAP3_11912.1) and (hu.MAP huMAP3_10359.1). It is included in all globally significant enrichment categories (9 globally significant GO/KEGG terms, q_global 0.00118–0.0474; see the table) and in STRING's mRNA-processing and major-spliceosome results (STRING Keyword mRNA processing; within-query FDR = 0.0155) and (STRING NetworkNeighborAL U2-type spliceosomal complex, and mRNA Splicing - Major Pathway; within-query FDR = 0.0319). Its established disease association with TARP syndrome and its substantial literature support the biological importance of regulated alternative splicing.
- **Conclusion**: Established evidence identifies RBM10 as an RNA-binding alternative-splicing regulator that may connect general transcript processing to regulatory gene expression. The module supports coordinated activity with spliceosomal partners, but does not show whether RBM10 is a driver or merely a co-abundant marker.

#### ADAR

- **Related proteins** (co-abundance neighbors): XRN2 (0.87), EHMT2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_10625.1
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR supplies a distinct RNA-editing function within the module. It is globally enriched across the nucleic-acid, RNA, gene-expression, and biosynthetic categories (7 globally significant GO/KEGG terms, q_global 0.00118–0.0271; see the table) and (GO:BP biosynthetic process; q_global = 0.0474), appears in STRING's nucleic-acid and mRNA-processing terms (4 supplementary STRING terms; within-query FDR 0.0023–0.0155), and occurs with RBMS1 in an RNA-binding hu.MAP complex (hu.MAP huMAP3_10625.1). Its neutrophil cell-type enhancement provides a possible link to the blood-associated aspect of the module. ADAR has extensive literature and established associations with Aicardi-Goutieres syndrome, dyschromatosis symmetrica hereditaria, and ADAR-related interferonopathy.
- **Conclusion**: Established evidence supports ADAR as an RNA-editing and RNA-processing component with plausible relevance to immune-cell biology. It could help explain why a general nuclear module is shared between kidney and circulatory-system samples, but the present data do not demonstrate an interferon-driven mechanism.

#### UIMC1

- **Related proteins** (co-abundance neighbors): ATF7IP (0.85), RCHY1 (0.82), NCOR1 (0.81), EHMT2 (0.80); STRING partners: NBN (0.768)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nuclear bodies; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_11912.1
- **Function (MyGene.info)**: ubiquitin interaction motif containing 1. This gene encodes a nuclear protein that interacts with Brca1 (breast cancer 1) in a complex to recognize and repair DNA lesions. This protein binds ubiquitinated lysine 63 of histone H2A and H2AX. This protein may also function as a repressor of transcription. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: menopause (0.283); insomnia (0.236); uterine corpus leiomyoma (0.216); jaw disease (0.187); pituitary gland disorder (0.143)
- **Europe PMC papers**: 404
- **Why important**: UIMC1 is a high-connectivity nuclear-body component linking ATF7IP, RCHY1, NCOR1, and EHMT2 in the module. It has a STRING relationship with NBN and is represented with RBM10, CCAR1, and UIMC1 in hu.MAP complex (hu.MAP huMAP3_11912.1). UIMC1 occurs in every globally significant enrichment category (9 globally significant GO/KEGG terms, q_global 0.00118–0.0474; see the table) and in the STRING nuclear-body and ubiquitin-related terms (7 supplementary STRING terms; within-query FDR 0.0155–0.0474). HPA identifies enhancement in neutrophils and platelets, making it informative for evaluating a possible blood-cell contribution. Its established function involves recognition of ubiquitinated chromatin lesions and DNA-damage repair, with disease associations including breast cancer and Nijmegen breakage syndrome-related biology through the repair network.
- **Conclusion**: Established evidence supports UIMC1 as a bridge between chromatin-associated DNA repair, nuclear bodies, and the possible blood-cell component of the module. The hypothesis that it couples RNA metabolism to tissue or immune-cell composition is plausible but unproven.

## Module 2

**Tissue pair**: circulatory_system and kidney  
**Genes (25)**: A2M, ACY1, ANPEP, SERPINC1, APOA1, APOH, ASL, CRAT, CLU, C3, COL6A1, COL18A1, EHHADH, GGACT, GPD1L, HNMT, MSRA, NIT1, HSPG2, PTGR1, SIAE, SIRT3, TTC38, GC, VTN

### Function

The module is best interpreted as an extracellular, plasma-associated homeostasis module integrating complement and coagulation regulation, lipoprotein transport, extracellular-matrix organization, and vesicle-associated proteins. The strongest primary evidence is the coordinated enrichment for extracellular exosome, extracellular organelle, extracellular membrane-bounded organelle, extracellular vesicle, extracellular space, and extracellular region (6 globally significant GO/KEGG terms, q_global 3.79e-07–7.69e-06; see the table), together with blood microparticles (GO:CC blood microparticle; q_global = 2.42e-05). Complement and coagulation cascades (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.000144), basement membrane and extracellular-matrix structural constituent (GO:CC basement membrane; q_global = 0.0218) (GO:MF extracellular matrix structural constituent; q_global = 0.0298), complement activation (GO:BP complement activation; q_global = 0.0245), and lipoprotein particles (GO:CC high-density lipoprotein particle; q_global = 0.0158) (GO:CC plasma lipoprotein particle; q_global = 0.0354) (GO:CC lipoprotein particle; q_global = 0.0354) refine this interpretation. C3, A2M, CLU, SERPINC1, and VTN support complement or coagulation control; APOA1, APOH, and CLU support lipoprotein biology; and COL18A1, COL6A1, HSPG2, and VTN support vascular or basement-membrane organization. The module therefore appears to represent a coordinated extracellular protein milieu rather than a single intracellular biochemical pathway.

**Cell composition.** The module is strongly dominated by secreted or extracellular proteins and by proteins commonly found in plasma, extracellular vesicles, or blood microparticles. HPA identifies secreted-to-blood proteins including C3, SERPINC1, CLU, GC, APOA1, APOH, VTN, and A2M, while COL18A1, COL6A1, and HSPG2 are secreted to the extracellular matrix. HPA also shows frequent liver and hepatocyte enrichment, with additional intestine, enterocyte, kidney, proximal-tubule, vascular, and fibroblast signals. Kidney protein detection is common for the module, whereas several canonical plasma proteins are not detected in kidney tissue by immunohistochemistry. This pattern makes a circulating plasma contribution, blood contamination, vascular content, or shared extracellular material a substantial alternative explanation for the cross-tissue conservation. The module is not primarily a blood-cell transcriptional module: blood-cell specificity is mixed, and several genes are not detected in immune cells. A smaller intracellular metabolic component includes ACY1, ASL, EHHADH, MSRA, CRAT, SIRT3, HNMT, and related genes, so the module is not compositionally uniform.

**GO/KEGG enrichment**: 16 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC extracellular exosome | 3.79e-07 | A2M, ACY1, ANPEP, APOA1, APOH, ASL, C3, CLU, COL18A1, COL6A1, GC, GGACT, GPD1L, HNMT, HSPG2, MSRA, PTGR1, SERPINC1, SIAE, TTC38, VTN |
| GO:CC extracellular organelle | 4.3e-07 | A2M, ACY1, ANPEP, APOA1, APOH, ASL, C3, CLU, COL18A1, COL6A1, GC, GGACT, GPD1L, HNMT, HSPG2, MSRA, PTGR1, SERPINC1, SIAE, TTC38, VTN |
| GO:CC extracellular membrane-bounded organelle | 4.3e-07 | A2M, ACY1, ANPEP, APOA1, APOH, ASL, C3, CLU, COL18A1, COL6A1, GC, GGACT, GPD1L, HNMT, HSPG2, MSRA, PTGR1, SERPINC1, SIAE, TTC38, VTN |
| GO:CC extracellular vesicle | 4.3e-07 | A2M, ACY1, ANPEP, APOA1, APOH, ASL, C3, CLU, COL18A1, COL6A1, GC, GGACT, GPD1L, HNMT, HSPG2, MSRA, PTGR1, SERPINC1, SIAE, TTC38, VTN |
| GO:CC extracellular space | 2.04e-06 | A2M, ACY1, ANPEP, APOA1, APOH, ASL, C3, CLU, COL18A1, COL6A1, GC, GGACT, GPD1L, HNMT, HSPG2, MSRA, PTGR1, SERPINC1, SIAE, TTC38, VTN |
| GO:CC extracellular region | 7.69e-06 | A2M, ACY1, ANPEP, APOA1, APOH, ASL, C3, CLU, COL18A1, COL6A1, GC, GGACT, GPD1L, HNMT, HSPG2, MSRA, PTGR1, SERPINC1, SIAE, TTC38, VTN |
| GO:CC blood microparticle | 2.42e-05 | A2M, APOA1, C3, CLU, GC, SERPINC1, VTN |
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 0.000144 | A2M, C3, CLU, SERPINC1, VTN |
| GO:CC vesicle | 0.000251 | A2M, ACY1, ANPEP, APOA1, APOH, ASL, C3, CLU, COL18A1, COL6A1, GC, GGACT, GPD1L, HNMT, HSPG2, MSRA, PTGR1, SERPINC1, SIAE, TTC38, VTN |
| GO:CC endoplasmic reticulum lumen | 0.00623 | APOA1, C3, CLU, COL18A1, COL6A1, SERPINC1, VTN |
| GO:CC high-density lipoprotein particle | 0.0158 | APOA1, APOH, CLU |
| GO:CC basement membrane | 0.0218 | COL18A1, COL6A1, HSPG2, VTN |
| GO:BP complement activation | 0.0245 | A2M, C3, CLU |
| GO:MF extracellular matrix structural constituent | 0.0298 | COL18A1, COL6A1, HSPG2, VTN |
| GO:CC plasma lipoprotein particle | 0.0354 | APOA1, APOH, CLU |

### STRING and hu.MAP

STRING supports a pre-existing extracellular plasma network rather than isolated co-abundance links. Strong relationships connect APOA1 with A2M, APOH, C3, CLU, SERPINC1, and VTN; connect complement or coagulation-associated proteins such as C3, SERPINC1, and VTN; and connect COL18A1 with COL6A1 and HSPG2. These relationships are concordant with the globally corrected GO/KEGG interpretation, although the STRING enrichment results are supplementary and their FDR values are not global module significance. hu.MAP provides additional evidence for known shared protein-complex or plasma-protein assemblies. The complexes represented by (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) repeatedly contain A2M, C3, APOA1, APOH, GC, or SERPINC1, while (hu.MAP huMAP3_06555.1) supports a collagen-associated assembly involving COL18A1 and COL6A1. CRAT and SIRT3 occur together in mitochondrial complexes (hu.MAP huMAP3_10525.1) (hu.MAP huMAP3_13468.1). Thus, part of the module recapitulates known extracellular and plasma assemblies, with a smaller metabolic substructure. CLU, PTGR1, HSPG2, and several other module genes lack hu.MAP complex assignments in the supplied evidence, which does not imply that their co-abundance is artifactual.

**STRING interactions (score >= 0.7)**: 24 of 300 gene pairs: A2M–APOA1 (0.998); A2M–APOH (0.752); A2M–CLU (0.896); A2M–SERPINC1 (0.927); APOA1–APOH (0.985); APOA1–C3 (0.957); APOA1–CLU (0.998); APOA1–SERPINC1 (0.708); APOA1–VTN (0.755); APOH–CLU (0.911); APOH–GC (0.766); APOH–SERPINC1 (0.944); APOH–VTN (0.787); C3–CLU (0.803); C3–GC (0.768); C3–VTN (0.79); CLU–GC (0.745); CLU–VTN (0.962); COL18A1–COL6A1 (0.848); COL18A1–HSPG2 (0.894); COL18A1–VTN (0.752); GC–SERPINC1 (0.84); HSPG2–VTN (0.797); SERPINC1–VTN (0.949)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Extracellular exosome (FDR = 2.03e-08, 21 genes); Keyword Secreted (FDR = 2.24e-08, 12 genes); Component Collagen-containing extracellular matrix (FDR = 4.56e-07, 9 genes); Component Blood microparticle (FDR = 9.69e-07, 7 genes); COMPARTMENTS Extracellular membrane-bounded organelle (FDR = 2.06e-06, 12 genes); COMPARTMENTS Extracellular vesicle (FDR = 2.06e-06, 12 genes); TISSUES Plasma cell (FDR = 2.11e-06, 8 genes); COMPARTMENTS Blood microparticle (FDR = 2.66e-06, 7 genes); COMPARTMENTS Extracellular region (FDR = 4.45e-06, 14 genes); COMPARTMENTS Extracellular space (FDR = 4.68e-06, 12 genes); PMID (2017) Characterization of Vitreous and Aqueous Proteome in Humans With Proliferative Diabetic Retinopathy and Its Clinical Correlation. (FDR = 5.63e-06, 7 genes); Keyword Signal (FDR = 7.52e-06, 12 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 7.76e-06, 8 genes); PMID (2020) Significant correlation between plasma proteome profile and pain intensity, sensitivity, and psychological distress in women with fibromyalgia. (FDR = 7.76e-06, 7 genes); Keyword Glycoprotein (FDR = 9.32e-06, 13 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINC1, A2M, C3, APOA1, APOH, GC; 6/64); huMAP3_10678.1 (A2M, C3, APOA1, GC; 4/71); huMAP3_08224.1 (C3, APOA1, GC; 3/21); huMAP3_09434.1 (C3, APOA1, GC; 3/33); huMAP3_08395.1 (A2M, C3, APOA1; 3/43); huMAP3_09531.1 (A2M, C3, APOA1; 3/47); huMAP3_10101.1 (A2M, C3, APOA1; 3/49); huMAP3_06555.1 (COL6A1, COL18A1; 2/14); huMAP3_07432.1 (C3, APOA1; 2/18); huMAP3_07265.1 (A2M, APOA1; 2/20); huMAP3_10525.1 (CRAT, SIRT3; 2/33); huMAP3_13468.1 (CRAT, SIRT3; 2/99)

### Novelty

The module should not be claimed as a wholly new molecular network. Many of its central relationships and functional groupings are already represented in STRING and hu.MAP, and the dominant biology is recognizable as a plasma, complement, coagulation, lipoprotein, and extracellular-matrix signature. The potentially novel aspect is the tissue-pair-level conservation of this particular combination across circulatory_system and kidney, especially the linking of a known circulating-protein network with kidney-associated extracellular-matrix and metabolic signals. However, the supplied evidence does not establish that this exact module has not previously been reported. Demonstrating novelty would require comparison with published tissue co-abundance modules, independent cohorts, and experimentally validated tissue-origin or physical-interaction data. Its reproducibility and tissue-pair context are therefore more defensible claims than molecular discovery of a new complex.

**Hypothesis.** Hypothesis: the module reflects a shared vascular or extracellular-fluid interface between circulation and kidney. Liver-derived plasma proteins may enter or associate with renal and vascular extracellular compartments, where complement, coagulation inhibitors, lipoprotein carriers, extracellular-matrix components, and vesicles jointly regulate protease activity, inflammatory activation, lipid handling, endothelial or basement-membrane interactions, and tissue injury responses. C3 and A2M could provide complement and protease surveillance, SERPINC1 could constrain coagulation proteases, APOA1 and APOH could couple lipid transport to inflammatory or coagulation state, and COL18A1, COL6A1, HSPG2, and VTN could provide an extracellular scaffold. The kidney-associated metabolic genes may reflect a parallel epithelial or proximal-tubule component, or shared sample composition, rather than a direct physical connection to the plasma proteins. This hypothesis requires validation with cell-type-resolved measurements, plasma-depletion controls, tissue localization, and perturbation experiments.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): APOH (0.95), COL18A1 (0.87), A2M (0.85), SERPINC1 (0.84), GGACT (0.83); STRING partners: APOA1 (0.957), CLU (0.803), GC (0.768), VTN (0.79)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_08224.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_07432.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is the most connected gene in the supplied module network and links complement biology to APOH, COL18A1, A2M, SERPINC1, and GGACT. It appears across the principal extracellular and blood-microparticle terms (9 globally significant GO/KEGG terms, q_global 3.79e-07–0.000251; see the table), complement activation (GO:BP complement activation; q_global = 0.0245), and the complement/coagulation pathway (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 0.000144). HPA supports liver enrichment, secretion to blood, kidney protein detection, and an immune-cell association with non-classical monocytes. Its disease associations include complement deficiency, complement glomerulopathy, and atypical hemolytic-uremic syndrome, making it especially relevant to a circulatory-kidney interpretation. The large literature volume indicates that its role is well established.
- **Conclusion**: Established evidence supports C3 as a central complement component and a major anchor of the extracellular plasma signal. Its network position is consistent with integration of complement, coagulation, and matrix-associated proteins. A module-specific role in coordinating renal extracellular responses remains a hypothesis rather than a demonstrated mechanism.

#### APOA1

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.91), CLU (0.87), COL18A1 (0.85); STRING partners: A2M (0.998), APOH (0.985), C3 (0.957), CLU (0.998), SERPINC1 (0.708), VTN (0.755)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_08224.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_07432.1, huMAP3_07265.1
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is a highly connected module gene with STRING relationships to A2M, APOH, C3, CLU, SERPINC1, and VTN, and it occurs in numerous hu.MAP plasma-protein complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1). It is the major protein component of HDL and promotes cholesterol efflux, while the globally corrected terms identify HDL, plasma lipoprotein, and lipoprotein particles (GO:CC high-density lipoprotein particle; q_global = 0.0158) (GO:CC plasma lipoprotein particle; q_global = 0.0354) (GO:CC lipoprotein particle; q_global = 0.0354). HPA shows liver enrichment, enterocyte and hepatocyte association, secretion to blood, and vesicle localization. Its disease associations include apolipoprotein A-I deficiency and low-HDL disorders, and it has substantial literature support.
- **Conclusion**: Established evidence identifies APOA1 as the lipid-transport anchor of the module and a plausible bridge between plasma composition and renal or vascular extracellular biology. Whether its co-abundance here reflects active kidney-relevant lipid handling or simply circulating HDL abundance is unresolved.

#### SERPINC1

- **Related proteins** (co-abundance neighbors): APOA1 (0.91), COL18A1 (0.85), CLU (0.85), C3 (0.84); STRING partners: A2M (0.927), APOA1 (0.708), APOH (0.944), GC (0.84), VTN (0.949)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 is a central network gene connected to APOA1, COL18A1, CLU, and C3, with strong STRING relationships to A2M, APOH, GC, and VTN. It is represented in the extracellular, blood-microparticle, endoplasmic-reticulum-lumen, and complement/coagulation terms (10 globally significant GO/KEGG terms, q_global 3.79e-07–0.00623; see the table). HPA identifies liver and hepatocyte enrichment, secretion to blood, and absence from immune cells. Its encoded antithrombin regulates blood coagulation, and its disease associations include hereditary antithrombin deficiency and venous thromboembolism. It also participates in the principal hu.MAP plasma complex (hu.MAP huMAP3_15040.1).
- **Conclusion**: Established evidence supports SERPINC1 as the coagulation-control anchor of the module and shows that its relationships with the other central proteins are already known. A renal protective or injury-linked role for this particular module is plausible but not established by co-abundance alone.

#### COL18A1

- **Related proteins** (co-abundance neighbors): VTN (0.90), C3 (0.87), SERPINC1 (0.85), APOA1 (0.85); STRING partners: COL6A1 (0.848), HSPG2 (0.894), VTN (0.752)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_06555.1
- **Function (MyGene.info)**: collagen type XVIII alpha 1 chain. This gene encodes the alpha chain of type XVIII collagen. This collagen is one of the multiplexins, extracellular matrix proteins that contain multiple triple-helix domains (collagenous domains) interrupted by non-collagenous domains. A long isoform of the protein has an N-terminal domain that is homologous to the extracellular part of frizzled receptors. Proteolytic processing at several endogeno…
- **Diseases (Open Targets)**: Knobloch syndrome 1 (0.778); Knobloch syndrome (0.700); hereditary glaucoma, primary closed-angle (0.593); Dupuytren Contracture (0.587); severe early-childhood-onset retinal dystrophy (0.501)
- **Europe PMC papers**: 5223
- **Why important**: COL18A1 occupies a well-connected position and links VTN, C3, SERPINC1, and APOA1 in the module network. It contributes to extracellular vesicle and space terms (7 globally significant GO/KEGG terms, q_global 3.79e-07–0.000251; see the table), basement membrane and extracellular-matrix structural constituent terms (GO:CC endoplasmic reticulum lumen; q_global = 0.00623) (GO:CC basement membrane; q_global = 0.0218) (GO:MF extracellular matrix structural constituent; q_global = 0.0298), and the collagen-associated hu.MAP complex (hu.MAP huMAP3_06555.1). HPA identifies blood-vessel and liver enrichment, hepatocyte association, secretion to extracellular matrix, and kidney protein detection. Its product is a type XVIII collagen chain, and its processing can produce endostatin; disease associations include Knobloch syndrome and related ocular disorders.
- **Conclusion**: Established evidence supports COL18A1 as the vascular and basement-membrane scaffold component of the module. Its links to plasma proteins suggest extracellular coupling, but the direction of interaction and whether the module changes matrix biology in kidney are hypotheses requiring tissue-level validation.

#### CLU

- **Related proteins** (co-abundance neighbors): GC (0.89), APOA1 (0.87), SERPINC1 (0.85), HSPG2 (0.84); STRING partners: A2M (0.896), APOA1 (0.998), APOH (0.911), C3 (0.803), GC (0.745), VTN (0.962)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: clusterin. The protein encoded by this gene is a secreted chaperone that can under some stress conditions also be found in the cell cytosol. It has been suggested to be involved in several basic biological events such as cell death, tumor progression, and neurodegenerative disorders. Alternate splicing results in both coding and non-coding variants.[provided by RefSeq, May 2011].
- **Diseases (Open Targets)**: Alzheimer disease (0.583); dementia (0.525); refractive error (0.444); late-onset Alzheimers disease (0.406); prostate cancer (0.376)
- **Europe PMC papers**: 10677
- **Why important**: CLU is a strongly connected extracellular gene linked by STRING to A2M, APOA1, APOH, C3, GC, VTN, and SERPINC1. It appears in nearly all major extracellular, lipoprotein, and complement-related primary terms (12 globally significant GO/KEGG terms, q_global 3.79e-07–0.0354; see the table). HPA shows liver enrichment and secretion to blood. Its annotated functions include secreted chaperone activity, immune-complex clearance, negative regulation of membrane-attack-complex activation, and protein folding. Disease associations include Alzheimer disease and dementia, and the literature support is substantial. No hu.MAP complex assignment is supplied, despite extensive STRING connectivity.
- **Conclusion**: Established evidence supports CLU as an extracellular chaperone and complement-regulatory connector between the lipoprotein and immune parts of the module. Its absence from the supplied hu.MAP complexes highlights a distinction between network-level association and experimentally supported complex membership. A role as a soluble stabilizer of the broader module is a hypothesis.

## Module 3

**Tissue pair**: circulatory_system and kidney  
**Genes (29)**: ACIN1, PRMT5, BCLAF1, DAZAP1, DHX9, DYNC1H1, EIF3C, FAM120A, HNRNPR, ISYNA1, MOCS2, NSFL1C, PAPSS2, PYM1, RPL12, RPL3, RPL6, POLR1G, RPS26, SEC16A, SPART, AARS1, MARS1, ALYREF, TRIM25, TRIP6, TTK, SNRNP200, EFTUD2

### Function

The strongest interpretation is a constitutive intracellular RNA-processing and protein-synthesis module. The globally corrected terms establish RNA binding and nucleic-acid binding (GO:MF RNA binding; q_global = 1.06e-05)(GO:MF nucleic acid binding; q_global = 0.00026), cytoplasmic translation and protein biosynthesis (GO:BP cytoplasmic translation; q_global = 0.000908)(GO:BP translation; q_global = 0.0184)(GO:BP protein biosynthetic process; q_global = 0.0184), cytosolic ribosome and large ribosomal-subunit components (GO:CC cytosolic large ribosomal subunit; q_global = 0.0133)(GO:CC cytosolic ribosome; q_global = 0.0352), RNA splicing (GO:BP RNA splicing; q_global = 0.0134), ribonucleoprotein complexes (GO:CC ribonucleoprotein complex; q_global = 0.0184), and exon-exon junction-complex association (GO:CC exon-exon junction complex; q_global = 0.0228). The genes therefore represent coordinated RNA maturation, transport or surveillance, translation initiation and elongation, and ribosome function rather than a specialized circulatory or kidney pathway. The presence of both spliceosomal and ribosomal components suggests coupling between pre-mRNA processing and downstream protein production. The interpretation is supported by the STRING enrichment for RNA and nucleic-acid binding (STRING Function RNA binding; within-query FDR = 1.82e-06)(STRING Function Nucleic acid binding; within-query FDR = 5.91e-05), but the STRING pathway results are supplementary rather than additional global enrichment evidence.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the encoded proteins are predominantly intracellular. Most genes have low tissue specificity, with kidney protein detection for nearly all annotated genes, which is consistent with a broadly expressed housekeeping-like program. The blood-cell specificity is also generally low, although isolated genes show enrichment in bone-marrow, erythroid, megakaryocytic, monocyte, dendritic-cell, neutrophil, basophil, or related populations. Consequently, the shared circulatory_system and kidney signal is more plausibly a ubiquitous RNA-processing and translation program, or a shared cellular-composition signal, than a module of circulating secreted factors. The heterogeneous cell-type-enhanced HPA annotations do not identify one coherent blood-cell population, so blood contamination or a single shared cell type should remain possibilities rather than conclusions.

**GO/KEGG enrichment**: 10 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF RNA binding | 1.06e-05 | AARS1, ACIN1, ALYREF, BCLAF1, DAZAP1, DHX9, DYNC1H1, EFTUD2, EIF3C, FAM120A, HNRNPR, MARS1, POLR1G, PYM1, RPL12, RPL3, RPL6, RPS26, SNRNP200, TRIM25, TRIP6 |
| GO:MF nucleic acid binding | 0.00026 | AARS1, ACIN1, ALYREF, BCLAF1, DAZAP1, DHX9, DYNC1H1, EFTUD2, EIF3C, FAM120A, HNRNPR, MARS1, POLR1G, PRMT5, PYM1, RPL12, RPL3, RPL6, RPS26, SNRNP200, TRIM25, TRIP6 |
| GO:BP cytoplasmic translation | 0.000908 | AARS1, DHX9, EIF3C, RPL12, RPL3, RPL6, RPS26 |
| GO:CC cytosolic large ribosomal subunit | 0.0133 | RPL12, RPL3, RPL6 |
| GO:BP RNA splicing | 0.0134 | ACIN1, BCLAF1, DAZAP1, DHX9, EFTUD2, HNRNPR, PRMT5, RPS26, SNRNP200 |
| GO:BP translation | 0.0184 | AARS1, BCLAF1, DHX9, EIF3C, MARS1, PYM1, RPL12, RPL3, RPL6, RPS26 |
| GO:BP protein biosynthetic process | 0.0184 | AARS1, BCLAF1, DHX9, EIF3C, MARS1, PYM1, RPL12, RPL3, RPL6, RPS26 |
| GO:CC ribonucleoprotein complex | 0.0184 | DAZAP1, DHX9, EFTUD2, EIF3C, HNRNPR, RPL12, RPL3, RPL6, RPS26, SNRNP200 |
| GO:CC exon-exon junction complex | 0.0228 | ACIN1, BCLAF1, PYM1 |
| GO:CC cytosolic ribosome | 0.0352 | RPL12, RPL3, RPL6, RPS26 |

### STRING and hu.MAP

STRING confirms a connected core of established relationships. The ribosomal proteins RPL3, RPL6, RPL12, and RPS26 form a particularly coherent translation-related group, with links to EIF3C, EFTUD2, and DHX9. DHX9 is connected to ALYREF, HNRNPR, SNRNP200, and ribosomal proteins, while SNRNP200 and EFTUD2 are strongly connected within the spliceosomal machinery. AARS1 and MARS1 also have a known aminoacyl-tRNA-synthetase relationship. These observations indicate that the co-abundance structure is substantially grounded in known molecular biology, although STRING coverage does not account for every module edge. hu.MAP provides independent complex-level support for an exon-junction and splicing-associated group containing ACIN1, BCLAF1, ALYREF, and PYM1 (hu.MAP huMAP3_11073.1)(hu.MAP huMAP3_09943.1), and for spliceosomal groups containing PRMT5, SNRNP200, and EFTUD2 (hu.MAP huMAP3_08980.1), with additional support for SNRNP200-EFTUD2 complexes (hu.MAP huMAP3_00960.1)(hu.MAP huMAP3_07622.1)(hu.MAP huMAP3_08501.1)(hu.MAP huMAP3_09504.1)(hu.MAP huMAP3_09945.1). The hu.MAP overlaps are partial rather than complete complexes, so they support several embedded molecular assemblies rather than one experimentally defined complex containing the entire module.

**STRING interactions (score >= 0.7)**: 21 of 406 gene pairs: AARS1–MARS1 (0.913); ACIN1–ALYREF (0.92); ALYREF–DHX9 (0.953); ALYREF–EFTUD2 (0.89); ALYREF–HNRNPR (0.851); DHX9–HNRNPR (0.909); DHX9–RPL6 (0.958); DHX9–RPS26 (0.923); DHX9–SNRNP200 (0.784); EFTUD2–RPL12 (0.752); EFTUD2–RPL3 (0.837); EFTUD2–RPL6 (0.706); EFTUD2–RPS26 (0.823); EFTUD2–SNRNP200 (0.999); EIF3C–RPS26 (0.987); RPL12–RPL3 (0.999); RPL12–RPL6 (0.999); RPL12–RPS26 (0.999); RPL3–RPL6 (0.999); RPL3–RPS26 (0.999); RPL6–RPS26 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function RNA binding (FDR = 1.82e-06, 21 genes); Function Nucleic acid binding (FDR = 5.91e-05, 22 genes); RCTM Formation of a pool of free 40S subunits (FDR = 0.00016, 5 genes); RCTM L13a-mediated translational silencing of Ceruloplasmin expression (FDR = 0.00019, 5 genes); RCTM Selenoamino acid metabolism (FDR = 0.00019, 6 genes); RCTM GTP hydrolysis and joining of the 60S ribosomal subunit (FDR = 0.00019, 5 genes); RCTM Peptide chain elongation (FDR = 0.00034, 4 genes); RCTM Viral mRNA Translation (FDR = 0.00045, 4 genes); RCTM Eukaryotic Translation Termination (FDR = 0.00045, 4 genes); RCTM Selenocysteine synthesis (FDR = 0.00047, 4 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 0.00053, 11 genes); RCTM Response of EIF2AK4 (GCN2) to amino acid deficiency (FDR = 0.0006, 4 genes); RCTM Nonsense Mediated Decay (NMD) independent of the Exon Junction Complex (EJC) (FDR = 0.0006, 4 genes); COMPARTMENTS Cytosolic ribosome (FDR = 0.00092, 4 genes); Function Organic cyclic compound binding (FDR = 0.0011, 25 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11073.1 (PYM1, BCLAF1, ACIN1; 3/67); huMAP3_09943.1 (ALYREF, BCLAF1, ACIN1; 3/78); huMAP3_08980.1 (PRMT5, SNRNP200, EFTUD2; 3/97); huMAP3_07225.1 (HNRNPR, FAM120A; 2/7); huMAP3_00960.1 (SNRNP200, EFTUD2; 2/8); huMAP3_07622.1 (SNRNP200, EFTUD2; 2/9); huMAP3_09654.1 (HNRNPR, FAM120A; 2/13); huMAP3_09281.1 (HNRNPR, FAM120A; 2/14); huMAP3_06097.1 (BCLAF1, ACIN1; 2/22); huMAP3_10659.1 (HNRNPR, FAM120A; 2/28); huMAP3_10564.1 (BCLAF1, ACIN1; 2/37); huMAP3_10789.1 (ALYREF, PYM1; 2/37); huMAP3_08501.1 (SNRNP200, EFTUD2; 2/47); huMAP3_09504.1 (SNRNP200, EFTUD2; 2/51); huMAP3_10625.1 (HNRNPR, FAM120A; 2/57); huMAP3_09945.1 (SNRNP200, EFTUD2; 2/61)

### Novelty

The module should not be claimed as a newly discovered molecular complex or pathway. Its central biology is already well established by the ribosome, spliceosome, exon-junction, RNA-binding, and translation annotations, by STRING relationships, and by hu.MAP complexes. What may be new is the reproducible co-abundance of these genes across the circulatory_system and kidney tissue groups, but the fact sheet does not compare this module with previously reported tissue-pair modules or independent cohorts. Therefore, the tissue-pair co-abundance observation is potentially novel but presently unproven as a new finding. The absence of some module relationships from STRING or hu.MAP would not establish novelty, because database coverage, assay context, and complex membership can be incomplete. A defensible novelty claim would require replication and comparison with existing co-expression or co-abundance modules.

**Hypothesis.** Hypothesis: this conserved module reflects a shared cellular demand for coordinated RNA handling and protein production in kidney and circulatory-system samples. A core ribosomal and translation-initiation program may be coupled to spliceosomal processing, RNA export, exon-junction-complex turnover, and RNA surveillance so that transcript maturation is matched to translational capacity. The observed tissue sharing may therefore arise from broadly active nucleated cells present in both sample groups, with additional variation contributed by bone-marrow or immune-related cell populations. This mechanism is a hypothesis, not a demonstrated tissue-specific pathway; it should be tested by cell-resolved expression, perturbation of the RNA-processing hubs, and replication in independent tissue datasets.

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): RPS26 (0.83), ALYREF (0.82), RPL12 (0.82), RPL6 (0.80); STRING partners: ALYREF (0.953), HNRNPR (0.909), RPL6 (0.958), RPS26 (0.923), SNRNP200 (0.784)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is a central network connector linking ribosomal proteins, ALYREF, HNRNPR, and SNRNP200. It appears in the globally corrected RNA-binding, nucleic-acid-binding, translation, splicing, and ribonucleoprotein terms (GO:MF RNA binding; q_global = 1.06e-05)(GO:MF nucleic acid binding; q_global = 0.00026)(GO:BP cytoplasmic translation; q_global = 0.000908)(GO:BP RNA splicing; q_global = 0.0134)(GO:BP translation; q_global = 0.0184)(GO:BP protein biosynthetic process; q_global = 0.0184)(GO:CC ribonucleoprotein complex; q_global = 0.0184), and STRING supports several of these relationships (STRING Function RNA binding; within-query FDR = 1.82e-06)(STRING Function Nucleic acid binding; within-query FDR = 5.91e-05)(STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.00053). Its established function as an ATP-dependent RNA helicase with roles in RNA processing, transcriptional regulation, RNA export, and interferon-related regulation makes it a plausible integrator of the module. It also has a substantial literature and disease associations involving neurodevelopmental and neurodegenerative phenotypes.
- **Conclusion**: Established: DHX9 is a multifunctional RNA helicase and a network bridge between splicing and translation-related genes. Hypothesis: its bridge position may help couple transcript processing with translation in the shared tissue program, but the co-abundance data do not demonstrate that DHX9 regulates the other module genes.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): TTK (0.83), EIF3C (0.82), EFTUD2 (0.81), RPL3 (0.80); STRING partners: DHX9 (0.784), EFTUD2 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is a network hub connected to EFTUD2, DHX9, EIF3C, and TTK. It is present in the globally corrected RNA-binding, nucleic-acid-binding, RNA-splicing, and ribonucleoprotein terms (GO:MF RNA binding; q_global = 1.06e-05)(GO:MF nucleic acid binding; q_global = 0.00026)(GO:BP RNA splicing; q_global = 0.0134)(GO:CC ribonucleoprotein complex; q_global = 0.0184), and it participates in multiple hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1)(hu.MAP huMAP3_00960.1)(hu.MAP huMAP3_07622.1)(hu.MAP huMAP3_08501.1)(hu.MAP huMAP3_09504.1)(hu.MAP huMAP3_09945.1). Its established role as a U5 small nuclear ribonucleoprotein component and RNA helicase directly explains the spliceosomal part of the module. Its strong disease literature includes retinitis pigmentosa and inherited retinal dystrophy associations.
- **Conclusion**: Established: SNRNP200 is a core spliceosomal factor and one of the best-supported mechanistic anchors of the RNA-processing component. Hypothesis: coordinated SNRNP200 abundance may mark increased spliceosome demand in the shared samples, but it does not by itself establish altered splicing activity.

#### EIF3C

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.89), RPL3 (0.84), MARS1 (0.84), SNRNP200 (0.82); STRING partners: RPS26 (0.987)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C has a prominent network position and connects DYNC1H1, RPL3, MARS1, and SNRNP200, while STRING links it strongly to RPS26. It appears across the globally corrected RNA-binding, nucleic-acid-binding, cytoplasmic-translation, translation, protein-biosynthesis, and ribonucleoprotein terms (GO:MF RNA binding; q_global = 1.06e-05)(GO:MF nucleic acid binding; q_global = 0.00026)(GO:BP cytoplasmic translation; q_global = 0.000908)(GO:BP translation; q_global = 0.0184)(GO:BP protein biosynthetic process; q_global = 0.0184)(GO:CC ribonucleoprotein complex; q_global = 0.0184). Its established function as a subunit of the eukaryotic translation-initiation factor complex gives the module a direct entry point from RNA handling into protein synthesis. It has extensive literature and reported associations with neoplastic disease and a developmental syndrome.
- **Conclusion**: Established: EIF3C is a translation-initiation component that connects the module's translation machinery to other RNA-associated proteins. Hypothesis: EIF3C may coordinate translational output with the RNA-processing state of the module, but this regulatory coupling is not proven by co-abundance alone.

#### RPS26

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.83), DHX9 (0.83), RPL3 (0.83), RPL12 (0.83); STRING partners: DHX9 (0.923), EFTUD2 (0.823), EIF3C (0.987), RPL12 (0.999), RPL3 (0.999), RPL6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein S26. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S26E family of ribosomal proteins. Mutations in this gene are found in Diamond-Blackfan anemia 10. There are multiple processed pseudogenes of this gene dispersed through the genome. [provided by RefSeq, Aug 2017].
- **Diseases (Open Targets)**: Diamond-Blackfan anemia (0.829); inherited bone marrow failure syndrome (0.503); Duchenne muscular dystrophy (0.503); asthma (0.486); Orthomyxoviridae infectious disease (0.463)
- **Europe PMC papers**: 1674
- **Why important**: RPS26 occupies the ribosomal hub of the module, connecting RPL3, RPL12, RPL6, EFTUD2, DHX9, and EIF3C. It is represented in the globally corrected RNA-binding, nucleic-acid-binding, cytoplasmic-translation, translation, protein-biosynthesis, ribonucleoprotein, and cytosolic-ribosome terms (GO:MF RNA binding; q_global = 1.06e-05)(GO:MF nucleic acid binding; q_global = 0.00026)(GO:BP cytoplasmic translation; q_global = 0.000908)(GO:BP translation; q_global = 0.0184)(GO:BP protein biosynthetic process; q_global = 0.0184)(GO:CC ribonucleoprotein complex; q_global = 0.0184)(GO:CC cytosolic ribosome; q_global = 0.0352). STRING independently supports its relationships with the ribosomal proteins, EIF3C, DHX9, and EFTUD2. Its established ribosomal function and association with Diamond-Blackfan anemia make it biologically and clinically informative, while its extensive literature supports interpretation as a core housekeeping component rather than a tissue-specific effector.
- **Conclusion**: Established: RPS26 is a small-subunit ribosomal protein embedded in the translation core and linked to a human bone-marrow-failure disorder. Hypothesis: its abundance may report translational capacity or cellular composition in the shared samples, but it is unlikely to explain tissue specificity by itself.

#### ALYREF

- **Related proteins** (co-abundance neighbors): DHX9 (0.82), POLR1G (0.80); STRING partners: ACIN1 (0.92), DHX9 (0.953), EFTUD2 (0.89), HNRNPR (0.851)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_09943.1, huMAP3_10789.1
- **Function (MyGene.info)**: Aly/REF export factor. The protein encoded by this gene is a heat stable, nuclear protein and functions as a molecular chaperone. It is thought to regulate dimerization, DNA binding, and transcriptional activity of basic region-leucine zipper (bZIP) proteins. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.542); dengue disease (0.370); neoplasm (0.103); non-small cell lung carcinoma (0.102); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 1636
- **Why important**: ALYREF connects DHX9 and POLR1G in the module and has STRING relationships with ACIN1, DHX9, EFTUD2, and HNRNPR. It is supported by the globally corrected RNA-binding and nucleic-acid-binding terms (GO:MF RNA binding; q_global = 1.06e-05)(GO:MF nucleic acid binding; q_global = 0.00026), by the RNA-binding and ribonucleoprotein STRING results (STRING Function RNA binding; within-query FDR = 1.82e-06)(STRING Function Nucleic acid binding; within-query FDR = 5.91e-05)(STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.00053), and by hu.MAP exon-junction and RNA-export-associated complexes (hu.MAP huMAP3_09943.1)(hu.MAP huMAP3_10789.1). Its established role in nuclear mRNA export and RNA metabolism provides a functional bridge between transcript processing and cytoplasmic translation. HPA tissue enhancement in bone marrow and cell-type enhancement in erythroid and megakaryocytic populations make it relevant to possible hematopoietic contributions, although its blood-cell specificity is not globally high.
- **Conclusion**: Established: ALYREF is an RNA-export and RNA-metabolism factor with experimentally supported complex relationships. Hypothesis: ALYREF may connect hematopoietic or other cell-composition effects to the shared RNA-processing program, but the module does not establish a blood-specific role.

## Module 4

**Tissue pair**: circulatory_system and kidney  
**Genes (5)**: ACSF2, ALDH4A1, ETFDH, HIBCH, MME

### Function

The module is best interpreted as a kidney-associated metabolic program spanning mitochondrial substrate metabolism and a membrane peptidase. ACSF2 supports fatty-acyl-CoA metabolism; HIBCH supports branched-chain amino-acid catabolism; ALDH4A1 supports proline and hydroxyproline catabolism; and ETFDH supports mitochondrial electron transfer, respiratory-chain input, and fatty-acid oxidation. MME is the central co-abundance hub and encodes a membrane neutral endopeptidase involved in peptide processing, including angiotensin maturation. These annotations suggest coordinated renal metabolic and peptide-processing biology, but not a single narrowly defined pathway. No GO/KEGG term passed global correction, so the functional interpretation is based on the individual gene annotations, network topology, HPA localization, and complex evidence rather than statistically significant enrichment.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of its members is annotated as secreted. HPA detects every member in kidney, and most members show kidney, liver, or other tissue-enhanced expression. The module is enriched for tissue and cell-type-restricted expression patterns, including proximal-tubule-associated, hepatocyte, enterocyte, adipocyte, myonuclear, adrenal, and Sertoli-cell patterns. Blood-cell specificity is generally low, although MME is immune-cell enriched in neutrophils. Thus, the shared circulatory_system–kidney signal is more consistent with renal or shared metabolic-cell biology than with a plasma-protein module, although the circulatory-system result could still reflect shared cell populations or sample composition. HPA provides no evidence here for a secreted-protein explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no high-confidence pairwise interactions among the module genes and no supplementary STRING functional-enrichment terms. This argues against interpreting the co-abundance edges as established physical interactions. hu.MAP identifies ACSF2 and ALDH4A1 together in complex (hu.MAP huMAP3_13468.1), whose broader membership is heavily mitochondrial and metabolic, but the module contains only a small subset of that complex. MME is the network hub yet has no hu.MAP or STRING partner in the supplied evidence. Overall, the network appears to capture coordinated expression across related metabolic and renal functions rather than a fully documented molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (ALDH4A1, ACSF2; 2/99)

### Novelty

The specific conserved co-abundance module appears potentially novel because its gene combination is not represented by a corresponding STRING interaction set, has only partial overlap with hu.MAP complex (hu.MAP huMAP3_13468.1), and has no globally significant GO/KEGG enrichment that would identify it as a canonical pathway module. However, these observations do not establish biological novelty: co-abundance can rediscover tissue or cell-state programs without physical interactions, and absence from STRING or hu.MAP reflects database coverage as well as true novelty. The defensible conclusion is that this is a potentially new renal metabolic co-expression pattern, not a proven new biochemical complex or pathway.

**Hypothesis.** Hypothesis: in kidney-related samples, coordinated expression of mitochondrial substrate-utilization genes reflects a shared metabolic state involving fatty-acyl-CoA handling, branched-chain amino-acid breakdown, proline catabolism, and respiratory electron transfer. MME may connect this intracellular metabolic state to extracellular peptide processing and renal signaling, potentially including angiotensin maturation. The apparent conservation in circulatory_system may arise from shared renal-like metabolic cell populations, systemic metabolic regulation, or sample-composition effects. This mechanism is provisional because the module has no globally significant enrichment and no supporting STRING interaction network.

### Important genes

#### MME

- **Related proteins** (co-abundance neighbors): ACSF2 (0.86), HIBCH (0.86), ALDH4A1 (0.86), ETFDH (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Centrosome, Basal body; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: membrane metalloendopeptidase. The protein encoded by this gene is a type II transmembrane glycoprotein and a common acute lymphocytic leukemia antigen that is an important cell surface marker in the diagnosis of human acute lymphocytic leukemia (ALL). The encoded protein is present on leukemic cells of pre-B phenotype, which represent 85% of cases of ALL. This protein is not restricted to leukemic cells, however, and is found …
- **Diseases (Open Targets)**: charcot-marie-tooth disease, axonal, type 2t (0.804); Spinocerebellar ataxia type 43 (0.692); heart failure (0.612); Alzheimer disease (0.552); congestive heart failure (0.534)
- **Europe PMC papers**: 7164
- **Why important**: MME is the central hub of the co-abundance subgraph, connecting every other module member. It is kidney-detected and intestine- and kidney-enhanced, is located at the plasma membrane, and has established roles in neutral endopeptidase activity, proteolysis, peptide metabolism, kidney development, and angiotensin maturation. It also has extensive literature and disease associations involving neuropathy, ataxia, and heart failure, making it the strongest bridge between renal biology, peptide signaling, and the module's mitochondrial metabolic genes.
- **Conclusion**: Established evidence supports MME as the network organizer and as a renal membrane peptidase with cardiovascularly relevant peptide-processing functions. It is not established that MME physically interacts with the metabolic enzymes here; its hub status represents co-abundance, not molecular binding. A signaling link between MME activity and the metabolic program is therefore a hypothesis.

#### ACSF2

- **Related proteins** (co-abundance neighbors): MME (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Microtubules, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: acyl-CoA synthetase family member 2. Enables medium-chain fatty acid-CoA ligase activity. Predicted to be involved in fatty acid metabolic process. Predicted to be located in mitochondrial matrix. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: response to antihypertensive drug (0.165); kidney transplant (0.134); liver dysplastic nodule (0.075); clear cell renal carcinoma (0.048); hepatocellular carcinoma (0.043)
- **Europe PMC papers**: 817
- **Why important**: ACSF2 is kidney-enhanced, kidney-detected, and annotated for medium-chain fatty-acid-CoA ligase activity and fatty-acid and acyl-CoA metabolism. It is also one of the two module members in hu.MAP complex (hu.MAP huMAP3_13468.1), placing it within a broader mitochondrial metabolic context. Its more limited literature and disease-association record makes it potentially informative for a tissue-specific metabolic signal rather than a well-established pathway marker.
- **Conclusion**: Established evidence supports ACSF2 as a kidney-associated fatty-acyl-CoA metabolic enzyme and as a partial member of (hu.MAP huMAP3_13468.1). Its co-abundance with MME and the other module genes may indicate coordinated metabolic state, but a direct functional relationship with MME or the other members is not established.

#### ALDH4A1

- **Related proteins** (co-abundance neighbors): MME (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: aldehyde dehydrogenase 4 family member A1. This protein belongs to the aldehyde dehydrogenase family of proteins. This enzyme is a mitochondrial matrix NAD-dependent dehydrogenase which catalyzes the second step of the proline degradation pathway, converting pyrroline-5-carboxylate to glutamate. Deficiency of this enzyme is associated with type II hyperprolinemia, an autosomal recessive disorder characterized by accumulation of delta-1-pyr…
- **Diseases (Open Targets)**: hyperprolinemia type 2 (0.788); Intellectual disability (0.497); hyperprolinemia (0.372); spermatocele (0.255); alcohol drinking (0.150)
- **Europe PMC papers**: 1283
- **Why important**: ALDH4A1 is a kidney- and liver-enhanced mitochondrial enzyme in (hu.MAP huMAP3_13468.1) that catalyzes a step in proline and hydroxyproline degradation. It has a defined inherited-disease association with type two hyperprolinemia and a substantial literature base. Its connection to the central MME hub links a specific amino-acid catabolic function to the broader renal co-abundance pattern.
- **Conclusion**: Established evidence supports ALDH4A1 as a mitochondrial proline-catabolism enzyme, kidney and liver associated, and a member of (hu.MAP huMAP3_13468.1). Its module relationship to MME and the other metabolic genes is a co-abundance observation; whether it marks altered proline flux in the shared tissue program remains a hypothesis.

#### ETFDH

- **Related proteins** (co-abundance neighbors): MME (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein dehydrogenase. This gene encodes a component of the electron-transfer system in mitochondria and is essential for electron transfer from a number of mitochondrial flavin-containing dehydrogenases to the main respiratory chain. Mutations in this gene are associated with glutaric acidemia. Alternatively spliced transcript variants that encode distinct isoforms have been observed. [provided by RefSeq, Aug 2013].
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.845); glutaric acidemia IIc (0.704); glutaric aciduria (0.670); hereditary disease (0.523); Abnormality of metabolism/homeostasis (0.407)
- **Europe PMC papers**: 1273
- **Why important**: ETFDH connects mitochondrial flavin-dependent dehydrogenases to the respiratory chain and is annotated for electron transport, oxidative-stress response, and fatty-acid beta-oxidation. It is kidney-detected and liver- and tongue-enhanced, with established associations to multiple acyl-CoA dehydrogenase deficiency and glutaric acidemia. Its role makes it a plausible energetic or redox component of the module despite having only a peripheral network position.
- **Conclusion**: Established evidence supports ETFDH as a mitochondrial electron-transfer and fatty-acid-oxidation component with clinically important metabolic-disease associations. Its co-abundance with MME, ACSF2, HIBCH, and ALDH4A1 may reflect coordinated oxidative metabolism, but the supplied data do not demonstrate a direct interaction or causal role in the module.

#### HIBCH

- **Related proteins** (co-abundance neighbors): MME (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3-hydroxyisobutyryl-CoA hydrolase. This gene encodes the enzyme responsible for hydrolysis of both HIBYL-CoA and beta-hydroxypropionyl-CoA. Mutations in this gene have been associated with 3-hyroxyisobutyryl-CoA hydrolase deficiency. Alternative splicing results in multiple transcript variants.[provided by RefSeq, May 2010].
- **Diseases (Open Targets)**: 3-hydroxyisobutyryl-CoA hydrolase deficiency (0.821); hereditary disease (0.476); neurodegenerative disease (0.463); Leigh syndrome (0.373); liver disorder (0.264)
- **Europe PMC papers**: 850
- **Why important**: HIBCH encodes a mitochondrial hydrolase involved in valine and branched-chain amino-acid catabolism and is kidney-detected. It has a defined association with HIBCH deficiency and broader links to hereditary and neurodegenerative disease. Although it is peripheral in the network and lacks STRING or hu.MAP support here, it adds a distinct amino-acid-catabolic axis to the module's metabolic interpretation.
- **Conclusion**: Established evidence supports HIBCH as a mitochondrial branched-chain amino-acid catabolic enzyme with a known deficiency phenotype. Its inclusion in this module is most plausibly interpreted as coordinated expression with renal metabolic genes, while any functional coupling to MME or the other enzymes remains hypothetical.

## Module 5

**Tissue pair**: circulatory_system and kidney  
**Genes (5)**: ACSL1, MFGE8, CHCHD3, STARD7, SUCLG2

### Function

No GO/KEGG term passed global correction, and there was no supplementary STRING functional enrichment; therefore the module should not be assigned a formally enriched pathway. The gene annotations nevertheless suggest a possible intersection of lipid handling, mitochondrial energy metabolism, mitochondrial membrane organization, and vascular apoptotic-cell clearance. ACSL1 supports long-chain fatty-acid activation; STARD7 is linked to phosphatidylcholine and ubiquinone biology; SUCLG2 supports succinyl-CoA metabolism in the tricarboxylic-acid cycle; CHCHD3 supports mitochondrial cristae organization; and MFGE8 supports clearance of apoptotic cells. These annotations support a biologically plausible theme, but it remains an interpretive hypothesis rather than a globally validated enrichment result.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: only MFGE8 is annotated as secreted to blood. The HPA profile instead points to tissue-associated biology, with enrichment or enhancement involving liver, skeletal muscle, blood vessel, adipose tissue, and tongue. Most genes have low immune-cell specificity, although ACSL1 is associated with neutrophils and MFGE8 with T-reg cells. All module proteins were detected in kidney, while the circulatory-system tissue-level comparison had no matching HPA tissue result. The shared signal may therefore reflect conserved kidney-associated expression together with metabolic, vascular, or shared stromal and parenchymal cell biology, rather than simply blood contamination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The module contains no high-confidence STRING interaction among its gene pairs and no hu.MAP complex containing multiple module members. Thus, the co-abundance edges are not corroborated by the supplied physical-interaction or curated-complex resources. The absence of these links does not invalidate co-regulation, but it argues against interpreting the module as a known stable protein complex. Its structure is more consistent with a small expression co-abundance association joining mitochondrial, lipid-metabolic, and vascular or clearance-related biology.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported cross-tissue co-abundance pattern, because its specific gene combination has no supporting high-confidence STRING links or shared hu.MAP complex in the supplied resources. However, this is not proof of a new biological mechanism: the component genes have established individual functions, and the small module has no globally significant GO/KEGG enrichment. The strongest defensible conclusion is that the cross-tissue co-abundance relationship is potentially novel, whereas the underlying gene functions are not.

**Hypothesis.** Hypothesis: in kidney and circulatory-system samples, a conserved metabolic and vascular cell program may couple fatty-acid activation and phospholipid handling with mitochondrial membrane and energy organization, while MFGE8 links that state to apoptotic-cell clearance and vascular remodeling. ACSL1 could provide lipid substrates, STARD7 could coordinate lipid and mitochondrial processes, SUCLG2 and CHCHD3 could reflect mitochondrial energetic and cristae requirements, and MFGE8 could mark the associated vascular or clearance response. This model is not established by enrichment or physical-interaction evidence and requires experimental validation.

### Important genes

#### ACSL1

- **Related proteins** (co-abundance neighbors): STARD7 (0.84), MFGE8 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 1. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. Several transcript variants enco…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.510); diabetes mellitus (0.501); diabetic neuropathy (0.404); neurodegenerative disease (0.368); menopause (0.334)
- **Europe PMC papers**: 4992
- **Why important**: ACSL1 is a central node in the module and connects STARD7 with MFGE8. Its established function is activation of long-chain fatty acids for lipid biosynthesis and fatty-acid degradation. It has tissue enhancement in adipose tissue, liver, and skeletal muscle, neutrophil-associated expression, links to diabetes and diabetic neuropathy, and extensive literature support.
- **Conclusion**: Established: ACSL1 is a long-chain fatty-acid metabolic enzyme with relevant metabolic disease associations. Hypothesis: its central co-abundance position may connect lipid metabolism to the mitochondrial and vascular features of this module.

#### STARD7

- **Related proteins** (co-abundance neighbors): ACSL1 (0.84), CHCHD3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: StAR related lipid transfer domain containing 7. Predicted to enable lipid binding activity. Predicted to act upstream of or within several processes, including establishment of skin barrier; mucociliary clearance; and myeloid dendritic cell activation. Predicted to be located in cytoplasm and extracellular region. Implicated in familial adult myoclonic epilepsy 2. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: benign adult familial myoclonic epilepsy (0.505); neurodegenerative disease (0.261); polycystic ovary syndrome (0.229); neoplasm (0.084); breast cancer (0.078)
- **Europe PMC papers**: 822
- **Why important**: STARD7 has the highest weighted network position and links ACSL1 to CHCHD3. Its annotations involve lipid binding, phosphatidylcholine biosynthesis, ubiquinone biosynthesis, mitochondrial membrane organization, and cellular respiration. It is detected in kidney, has a substantial literature base, and is associated with familial adult myoclonic epilepsy and broader neurodegenerative disease.
- **Conclusion**: Established: STARD7 is a plausible lipid and mitochondrial organizer with disease associations. Hypothesis: its network position may make it a bridge between fatty-acid handling and mitochondrial membrane function in the shared tissue program.

#### MFGE8

- **Related proteins** (co-abundance neighbors): SUCLG2 (0.84), ACSL1 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: milk fat globule EGF and factor V/VIII domain containing. This gene encodes a preproprotein that is proteolytically processed to form multiple protein products. The major encoded protein product, lactadherin, is a membrane glycoprotein that promotes phagocytosis of apoptotic cells. This protein has also been implicated in wound healing, autoimmune disease, and cancer. Lactadherin can be further processed to form a smaller cleavage product, medin, which c…
- **Diseases (Open Targets)**: AL amyloidosis (0.462); angina pectoris (0.339); myocardial ischemia (0.333); coronary artery bypass (0.314); coronary atherosclerosis (0.312)
- **Europe PMC papers**: 2623
- **Why important**: MFGE8 is a central connector between ACSL1 and SUCLG2, is tissue enriched in blood vessel, and is the only module member annotated as secreted to blood. Lactadherin promotes phagocytosis of apoptotic cells and has established links to wound healing, autoimmune disease, cancer, vascular disease, myocardial ischemia, and vascular amyloid biology. It also has extensive literature support.
- **Conclusion**: Established: MFGE8 links apoptotic-cell clearance with vascular and secreted-protein biology. Hypothesis: it may provide the extracellular or vascular component that couples the metabolic module to tissue repair or remodeling.

#### CHCHD3

- **Related proteins** (co-abundance neighbors): STARD7 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coiled-coil-helix-coiled-coil-helix domain containing 3. The protein encoded by this gene is an inner mitochondrial membrane scaffold protein. Absence of the encoded protein affects the structural integrity of mitochondrial cristae and leads to reductions in ATP production, cell growth, and oxygen consumption. This protein is part of the mitochondrial contact site and cristae organizing system (MICOS). Several transcript variants encoding different isof…
- **Diseases (Open Targets)**: neurodegenerative disease (0.537); smoking initiation (0.414); intelligence (0.385); insomnia (0.362); mathematical ability (0.312)
- **Europe PMC papers**: 549
- **Why important**: CHCHD3 is connected to STARD7 and is an inner mitochondrial membrane scaffold in the MICOS system. Its established functions include cristae formation, mitochondrial fusion, and preservation of mitochondrial structure, ATP production, growth, and oxygen consumption. It is enhanced in skeletal muscle and tongue, is detected in kidney, and has disease-relevant links to neurodegenerative disease.
- **Conclusion**: Established: CHCHD3 is a mitochondrial architecture gene. Hypothesis: its co-abundance with STARD7 may indicate coordinated maintenance of mitochondrial membranes in the shared kidney and circulatory-system context.

#### SUCLG2

- **Related proteins** (co-abundance neighbors): MFGE8 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase GDP-forming subunit beta. This gene encodes a GTP-specific beta subunit of succinyl-CoA synthetase. Succinyl-CoA synthetase catalyzes the reversible reaction involving the formation of succinyl-CoA and succinate. Alternate splicing results in multiple transcript variants. Pseudogenes of this gene are found on chromosomes 5 and 12. [provided by RefSeq, Apr 2010].
- **Diseases (Open Targets)**: smoking initiation (0.377); breast disorder (0.325); vitamin B deficiency (0.318); alcohol drinking (0.314); duodenal ulcer (0.270)
- **Europe PMC papers**: 1184
- **Why important**: SUCLG2 is connected to MFGE8 and represents the module's tricarboxylic-acid-cycle and succinyl-CoA metabolic component. It is tissue enhanced in liver, detected in kidney, and has a substantial literature base. Its disease and trait associations include smoking initiation, breast disorder, vitamin deficiency, alcohol drinking, and duodenal ulcer.
- **Conclusion**: Established: SUCLG2 is a GTP-forming succinyl-CoA-ligase subunit involved in mitochondrial intermediary metabolism. Hypothesis: its link to MFGE8 may reflect coupling between cellular energetic state and vascular or apoptotic-cell-clearance biology, but that connection is not directly demonstrated.

## Module 6

**Tissue pair**: circulatory_system and kidney  
**Genes (23)**: AFG2B, BOD1L1, EHBP1, EHMT1, EML3, ERBIN, FOXK1, GCC1, GRIPAP1, ITSN2, LACTB, MAD1L1, MED22, MIB1, IKBKG, NF1, NUP54, PMS2, PTPRK, INPPL1, TACC1, TMF1, ZGPAT

### Function

No GO or KEGG term passed global correction, so there is no globally supported pathway annotation for this module. The gene annotations instead suggest a heterogeneous combination of intracellular trafficking, membrane organization, receptor and Ras signaling, transcriptional and chromatin regulation, DNA repair, chromosome surveillance, and inflammatory signaling. TMF1, GCC1, GRIPAP1, ERBIN, PTPRK, ITSN2, EHBP1, and INPPL1 support a trafficking or membrane-associated component. NF1, IKBKG, EHMT1, FOXK1, MED22, and ZGPAT support signaling or transcriptional regulation, whereas BOD1L1, PMS2, MAD1L1, EML3, TACC1, and AFG2B support genome maintenance, cell-cycle, spindle, or proteostasis processes. The module is therefore best interpreted as a composite cellular-state or cell-composition signal rather than as one established biochemical pathway.

**Cell composition.** The module contains no secreted genes according to HPA, so it is not a plasma-protein or circulating-secretome module. Most genes have low tissue specificity, and kidney protein detection is broad among genes with available data. Single-cell annotations are diverse and include neutrophils, oligodendrocytes, distal convoluted tubule cells, cardiomyocytes, choroid plexus epithelial cells, and other cell types. Blood-cell specificity is generally low, although BOD1L1 is immune-cell enhanced in neutrophils and PTPRK has group-enriched memory and naive B-cell annotations. Several genes also have neutrophil-associated single-cell annotations. The circulatory-system protein evidence is unavailable in the supplied HPA summary. The shared signal may therefore reflect broadly expressed intracellular genes, mixed renal or vascular cell populations, or shared cellular states rather than a specialized blood-cell or secreted-protein program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports two high-confidence relationships within the module: GCC1 with TMF1 and NF1 with PMS2. These relationships support small established substructures but not a unified physical network. hu.MAP repeatedly places TMF1 and GRIPAP1 together in (hu.MAP huMAP3_11803.1), (hu.MAP huMAP3_11620.1), and (hu.MAP huMAP3_13576.1), within larger complexes that also contain proteins such as CALB1, RABEP1, and RABGEF1. This supports a possible trafficking or membrane-regulatory connection, although the complexes are incomplete in the module. FOXK1 and EHMT1 occur together in (hu.MAP huMAP3_15128.1), but that complex is very large and gives weaker evidence for a specific module-level complex. Most module edges lack corresponding high-confidence STRING or hu.MAP support. The module is therefore a co-abundance association containing several known relationships, not a validated physical complex.

**STRING interactions (score >= 0.7)**: 2 of 253 gene pairs: GCC1–TMF1 (0.729); NF1–PMS2 (0.745)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11803.1 (TMF1, GRIPAP1; 2/3); huMAP3_11620.1 (TMF1, GRIPAP1; 2/7); huMAP3_13576.1 (TMF1, GRIPAP1; 2/8); huMAP3_15128.1 (FOXK1, EHMT1; 2/96)

### Novelty

The tissue-pair co-abundance pattern may be a new systems-level observation, but the evidence does not establish a new molecular complex or pathway. The repeated TMF1–GRIPAP1 membership in (hu.MAP huMAP3_11803.1), (hu.MAP huMAP3_11620.1), and (hu.MAP huMAP3_13576.1), together with the STRING-supported GCC1–TMF1 and NF1–PMS2 relationships, shows that parts of the module recapitulate known biology. Most other associations are not represented by the supplied STRING or hu.MAP evidence, but absence from those resources cannot prove novelty because database coverage and context dependence are incomplete. The most defensible conclusion is that the cross-tissue co-abundance association may be novel, while its constituent molecular relationships are partly established and its integrated interpretation remains provisional.

**Hypothesis.** Hypothesis: the module reflects a shared renal–circulatory cellular state involving intracellular trafficking and membrane organization, with secondary coupling to signaling, chromatin regulation, cell-cycle surveillance, and inflammatory responsiveness. The TMF1–GRIPAP1–GCC1 signal could connect vesicle and Golgi organization with receptor or junctional regulation through ERBIN, PTPRK, ITSN2, EHBP1, and INPPL1. NF1, IKBKG, EHMT1, FOXK1, MED22, and ZGPAT could reflect associated signaling or transcriptional state, while the DNA-repair and spindle genes may reflect proliferation or cellular stress rather than one common pathway. Single-cell or spatial validation would be needed to distinguish intracellular co-regulation from variation in cell composition.

### Important genes

#### TMF1

- **Related proteins** (co-abundance neighbors): BOD1L1 (0.86), MIB1 (0.85), AFG2B (0.82), TACC1 (0.81), MED22 (0.81); STRING partners: GCC1 (0.729)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_11803.1, huMAP3_11620.1, huMAP3_13576.1
- **Function (MyGene.info)**: TATA element modulatory factor 1. Enables androgen receptor binding activity and nuclear receptor coactivator activity. Involved in androgen receptor signaling pathway and positive regulation of transcription by RNA polymerase II. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.166); infectious meningitis (0.100); non-syndromic male infertility due to sperm motility disorder (0.073); spermatogenic failure, X-linked, 7 (0.065); spermatogenic failure 85 (0.064)
- **Europe PMC papers**: 344
- **Why important**: TMF1 has the strongest network position in the module and connects to several module genes, including GCC1, with a STRING-supported relationship. It is localized to the Golgi and is annotated for retrograde Golgi and endosomal transport. It also appears with GRIPAP1 in (hu.MAP huMAP3_11803.1), (hu.MAP huMAP3_11620.1), and (hu.MAP huMAP3_13576.1). Its network position and trafficking annotations make it a central mechanistic anchor.
- **Conclusion**: Established evidence supports TMF1 as a Golgi and endosomal-trafficking protein and as part of known complex contexts with GRIPAP1. It is not established that TMF1 drives the shared circulatory-system and kidney co-abundance pattern. A trafficking-centered role is therefore a hypothesis rather than a demonstrated causal function.

#### GRIPAP1

- **Related proteins** (co-abundance neighbors): ZGPAT (0.84), BOD1L1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_11803.1, huMAP3_11620.1, huMAP3_13576.1
- **Function (MyGene.info)**: GRIP1 associated protein 1. This gene encodes a guanine nucleotide exchange factor for the Ras family of small G proteins (RasGEF). The encoded protein interacts in a complex with glutamate receptor interacting protein 1 (GRIP1) and plays a role in the regulation of AMPA receptor function. [provided by RefSeq, Aug 2013].
- **Diseases (Open Targets)**: neurodegenerative disease (0.286); type 2 diabetes mellitus (0.123); neurodevelopmental disorder (0.118); neoplasm (0.021); Alzheimer disease (0.014)
- **Europe PMC papers**: 210
- **Why important**: GRIPAP1 is one of the two recurring module members in (hu.MAP huMAP3_11803.1), (hu.MAP huMAP3_11620.1), and (hu.MAP huMAP3_13576.1), giving it the clearest hu.MAP-supported connection to the TMF1-associated signal. It is a Ras-family guanine nucleotide exchange factor associated with receptor transport, recycling endosome localization, and vesicles. Its repeated complex membership is important despite its modest network position.
- **Conclusion**: Established evidence supports GRIPAP1 as a vesicle- and receptor-trafficking regulator and as a repeated member of complexes containing TMF1. The module does not establish a specific role in kidney–circulatory coordination. Its proposed role as a connector between trafficking and signaling remains a hypothesis.

#### NF1

- **Related proteins** (co-abundance neighbors): MED22 (0.89), PMS2 (0.86), BOD1L1 (0.81); STRING partners: PMS2 (0.745)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neurofibromin 1. This gene product appears to function as a negative regulator of the ras signal transduction pathway. Mutations in this gene have been linked to neurofibromatosis type 1, juvenile myelomonocytic leukemia and Watson syndrome. The mRNA for this gene is subject to RNA editing (CGA>UGA->Arg1306Term) resulting in premature translation termination. Alternatively spliced transcript variants encoding diff…
- **Diseases (Open Targets)**: neurofibromatosis type 1 (0.886); neurofibromatosis-Noonan syndrome (0.841); neurofibromatosis (0.819); juvenile myelomonocytic leukemia (0.769); Watson syndrome (0.756)
- **Europe PMC papers**: 30450
- **Why important**: NF1 is a highly studied disease gene connected to MED22 and PMS2, with the NF1–PMS2 relationship supported by STRING. Neurofibromin negatively regulates Ras signaling and has annotations involving hypoxia, endothelial proliferation, and metanephros development, which are relevant to vascular and renal biology. Its extensive literature and disease associations increase its interpretive importance.
- **Conclusion**: Established evidence supports NF1 as a Ras-regulatory protein with hypoxia-, endothelial-, and kidney-development-related annotations, as well as a database relationship with PMS2. It is not established that NF1 links the whole module or explains the co-abundance pattern. A signaling-state contribution is plausible but unproven.

#### EHMT1

- **Related proteins** (co-abundance neighbors): FOXK1 (0.86), NUP54 (0.84), MIB1 (0.83), MAD1L1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_15128.1
- **Function (MyGene.info)**: euchromatic histone lysine methyltransferase 1. The protein encoded by this gene is a histone methyltransferase that methylates the lysine-9 position of histone H3. This action marks the genomic region packaged with these methylated histones for transcriptional repression. This protein may be involved in the silencing of MYC- and E2F-responsive genes and therefore could play a role in the G0/G1 cell cycle transition. Defects in this gene are a …
- **Diseases (Open Targets)**: Kleefstra syndrome 1 (0.748); Kleefstra syndrome (0.677); hereditary disease (0.547); Intellectual disability (0.514); Kleefstra syndrome due to 9q34 microdeletion (0.462)
- **Europe PMC papers**: 2274
- **Why important**: EHMT1 is a chromatin-modifying enzyme with a strong network position and a direct hu.MAP association with FOXK1 in (hu.MAP huMAP3_15128.1). It regulates repressive histone marks and transcriptional state and has substantial literature and established association with Kleefstra syndrome. Its connections to MIB1, NUP54, MAD1L1, and FOXK1 make it relevant to nuclear and cell-state interpretation.
- **Conclusion**: Established evidence supports EHMT1 as a transcriptional and chromatin regulator and supports its inclusion with FOXK1 in (hu.MAP huMAP3_15128.1). The module does not demonstrate that EHMT1-mediated repression causes the shared tissue-pair signal. Its role is best viewed as a possible cell-state or proliferation-related component.

#### MIB1

- **Related proteins** (co-abundance neighbors): TMF1 (0.85), EHMT1 (0.83), TACC1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Microtubules, Primary cilium; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MIB E3 ubiquitin protein ligase 1. This gene encodes a protein containing multiple ankyrin repeats and RING finger domains that functions as an E3 ubiquitin ligase. The encoded protein positively regulates Notch signaling by ubiquitinating the Notch receptors, thereby facilitating their endocytosis. This protein may also promote the ubiquitination and degradation of death-associated protein kinase 1 (DAPK1). [provided by RefSeq, Ju…
- **Diseases (Open Targets)**: left ventricular noncompaction (0.625); hypercholesterolemia, familial, 1 (0.333); type 2 diabetes mellitus (0.268); Abnormality of the skeletal system (0.266); musculoskeletal system disorder (0.250)
- **Europe PMC papers**: 3711
- **Why important**: MIB1 links TMF1, EHMT1, and TACC1 in the co-abundance network. It is an E3 ubiquitin ligase that promotes Notch receptor ubiquitination and endocytosis. HPA annotates it in cardiomyocytes, myonuclei, podocytes, microtubules, and primary cilia, making it relevant to membrane trafficking, developmental signaling, and renal or cardiovascular cell states. Its disease literature is substantial.
- **Conclusion**: Established evidence supports MIB1 as a Notch-regulating ubiquitin ligase involved in endocytosis and as a protein expressed in cell types relevant to the tissue pair. The module does not prove active Notch signaling or a direct MIB1-mediated connection among its neighbors. A Notch–trafficking interpretation is testable but unproven.

#### PMS2

- **Related proteins** (co-abundance neighbors): NF1 (0.86); STRING partners: NF1 (0.745)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PMS1 homolog 2, mismatch repair system component. The protein encoded by this gene is a key component of the mismatch repair system that functions to correct DNA mismatches and small insertions and deletions that can occur during DNA replication and homologous recombination. This protein forms heterodimers with the gene product of the mutL homolog 1 (MLH1) gene to form the MutL-alpha heterodimer. The MutL-alpha heterodimer possesses an endonucleo…
- **Diseases (Open Targets)**: Lynch syndrome (0.866); mismatch repair cancer syndrome (0.837); mismatch repair cancer syndrome 1 (0.740); endometrial carcinoma (0.654); Non-polyposis Turcot syndrome (0.648)
- **Europe PMC papers**: 14894
- **Why important**: PMS2 is the module member with a clear mismatch-repair function and a STRING-supported relationship with NF1. It is annotated in distal and proximal tubule cells and has extensive literature and strong disease associations involving Lynch syndrome and mismatch-repair cancer syndromes. Its peripheral network position is offset by its biological specificity and its connection to NF1.
- **Conclusion**: Established evidence supports PMS2 as a core mismatch-repair protein and supports its database relationship with NF1. The module does not show that mismatch-repair activity is a defining module function or that PMS2 is functionally coupled to the trafficking genes. A DNA-replication or cellular-stress contribution remains possible but is not demonstrated.

## Module 7

**Tissue pair**: circulatory_system and kidney  
**Genes (37)**: PRMT3, BAG2, ZNHIT6, CDK5RAP2, NCAPD2, CACYBP, DCAF13, DDX5, EIF2A, EIF3F, SIRAL1, FKBP4, GMPS, HSPH1, HK2, IGF2BP1, IGF2BP3, IMPDH2, MCM2, MCM4, MCM5, MCM6, MCM7, ORC2, OTUD6B, PCNA, PKP3, PPIE, GINS2, GART, PFAS, RRM1, RRP1B, SMC2, SMC4, SRPK1, UBE2V2

### Function

The module is most strongly characterized as a nuclear DNA-replication and chromosome-maintenance program. Primary evidence is provided by globally significant terms for break-induced replication (GO:BP double-strand break repair via break-induced replication; q_global = 3.28e-07), the CMG complex (GO:CC CMG complex; q_global = 2.24e-06), the MCM complex (GO:CC MCM complex; q_global = 2.72e-06), the DNA-replication preinitiation complex (GO:CC DNA replication preinitiation complex; q_global = 4.55e-06), DNA replication and its initiation (9 globally significant GO/KEGG terms, q_global 0.000122–0.00399; see the table), helicase activities (8 globally significant GO/KEGG terms, q_global 0.000251–0.0274; see the table), homologous-recombination and recombinational repair (KEGG Homologous recombination - Homo sapiens (human); q_global = 0.014) (GO:BP double-strand break repair via homologous recombination; q_global = 0.0365) (GO:BP recombinational repair; q_global = 0.0396), and the cell cycle (KEGG Cell cycle - Homo sapiens (human); q_global = 0.00301). The module also contains a purine-biosynthesis branch involving GART, PFAS, GMPS and IMPDH2 (4 globally significant GO/KEGG terms, q_global 0.0134–0.0445; see the table), consistent with nucleotide supply for DNA synthesis. SMC2, SMC4 and NCAPD2 connect the replication-associated genes to chromosome condensation and organization (GO:CC nuclear chromosome; q_global = 1.09e-05) (GO:CC chromosomal region; q_global = 0.0374) (GO:BP meiotic chromosome condensation; q_global = 0.0409). Thus, the most defensible interpretation is coordinated replication-fork activity, replication-associated repair, nucleotide provision and chromosome organization. The module should not be interpreted as proving that every gene operates in a single physical complex or that the tissue itself is undergoing active proliferation.

**Cell composition.** The module is composed predominantly of intracellular, nuclear or cytosolic proteins rather than plasma or secreted proteins: the HPA summary reports no secreted genes. Many genes are broadly expressed, while others are enhanced in bone marrow or lymphoid tissue and in progenitor populations, especially erythrocyte, megakaryocyte and monocyte progenitors. The HPA profile therefore supports a proliferative-cell or progenitor-cell signal rather than a plasma-protein signal. Its presence in circulatory-system and kidney data could reflect shared proliferating or progenitor-like cell populations, blood-cell contribution, or a conserved housekeeping replication program. This interpretation is strengthened by the frequent low immune-cell-specificity annotations, but the module is not simply an immune module. Kidney protein detection is common among the annotated genes, whereas circulatory-system protein evidence is unavailable in the supplied HPA summary; consequently, the shared tissue pattern should not be treated as proof of kidney-specific biology.

**GO/KEGG enrichment**: 37 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP double-strand break repair via break-induced replication | 3.28e-07 | GINS2, MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC CMG complex | 2.24e-06 | GINS2, MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC MCM complex | 2.72e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC DNA replication preinitiation complex | 4.55e-06 | GINS2, MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC nuclear chromosome | 1.09e-05 | GINS2, MCM2, MCM4, MCM5, MCM6, MCM7, NCAPD2, ORC2, PCNA, SMC2, SMC4 |
| GO:BP regulation of DNA-templated DNA replication initiation | 0.000122 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP DNA-templated DNA replication | 0.000124 | GINS2, MCM2, MCM4, MCM5, MCM6, MCM7, ORC2, PCNA, RRM1 |
| GO:MF single-stranded DNA binding | 0.000251 | MCM2, MCM4, MCM5, MCM6, MCM7, SMC2, SMC4 |
| GO:BP DNA replication initiation | 0.00034 | MCM2, MCM4, MCM5, MCM6, MCM7, ORC2 |
| GO:BP DNA replication | 0.000435 | GINS2, MCM2, MCM4, MCM5, MCM6, MCM7, ORC2, PCNA, RRM1, UBE2V2 |
| GO:BP regulation of DNA-templated DNA replication | 0.000744 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| KEGG DNA replication - Homo sapiens (human) | 0.00086 | MCM2, MCM4, MCM5, MCM6, MCM7, PCNA |
| KEGG Cell cycle - Homo sapiens (human) | 0.00301 | MCM2, MCM4, MCM5, MCM6, MCM7, ORC2, PCNA |
| GO:BP regulation of DNA replication | 0.00399 | MCM2, MCM4, MCM5, MCM6, MCM7, PCNA |
| GO:MF four-way junction helicase activity | 0.00503 | MCM2, MCM4, MCM5, MCM6, MCM7 |

### STRING and hu.MAP

STRING independently supports a highly coherent replication core: the MCM genes, GINS2, ORC2, PCNA and RRM1 form dense high-confidence relationships, with additional links to condensin components SMC2, SMC4 and NCAPD2 (15 supplementary STRING terms; within-query FDR 2.99e-06–4.88e-05). The strongest recurring structure is the MCM–GINS replication helicase and its association with origin recognition and PCNA. STRING also identifies a purine-biosynthesis group involving GART, GMPS, IMPDH2 and PFAS, plus smaller pairs such as BAG2–HSPH1 and IGF2BP1–IGF2BP3. These relationships are established interaction or functional-association evidence and are supplementary to the globally corrected GO/KEGG results. hu.MAP contains several replication complexes with the same MCM and GINS2 members, including complexes whose remaining members include MCM3, GINS1, GINS3, GINS4, CDC45, TIPIN, CLSPN and TIMELESS (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_06417.1) (hu.MAP huMAP3_08399.1). Separate hu.MAP complexes contain SMC2, SMC4 and NCAPD2, corresponding to condensin (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_14663.1). The module therefore recovers known molecular machinery, while also connecting these machinery-defined groups through the co-abundance network.

**STRING interactions (score >= 0.7)**: 56 of 666 gene pairs: BAG2–HSPH1 (0.995); GART–GMPS (0.937); GART–IMPDH2 (0.811); GART–PFAS (0.999); GINS2–MCM2 (0.998); GINS2–MCM4 (0.999); GINS2–MCM5 (0.999); GINS2–MCM6 (0.998); GINS2–MCM7 (0.999); GINS2–NCAPD2 (0.765); GINS2–SMC4 (0.735); GMPS–IMPDH2 (0.998); GMPS–RRM1 (0.748); IGF2BP1–IGF2BP3 (0.984); MCM2–MCM4 (0.999); MCM2–MCM5 (0.999); MCM2–MCM6 (0.999); MCM2–MCM7 (0.999); MCM2–NCAPD2 (0.713); MCM2–ORC2 (0.999); MCM2–PCNA (0.939); MCM2–RRM1 (0.914); MCM4–MCM5 (0.999); MCM4–MCM6 (0.999); MCM4–MCM7 (0.999); MCM4–NCAPD2 (0.732); MCM4–ORC2 (0.988); MCM4–PCNA (0.965); MCM4–RRM1 (0.952); MCM4–SMC2 (0.748); MCM4–SMC4 (0.736); MCM5–MCM6 (0.999); MCM5–MCM7 (0.999); MCM5–NCAPD2 (0.736); MCM5–ORC2 (0.999); MCM5–PCNA (0.918); MCM5–RRM1 (0.957); MCM5–SMC2 (0.754); MCM5–SMC4 (0.785); MCM6–MCM7 (0.999); MCM6–ORC2 (0.986); MCM6–PCNA (0.912); MCM6–RRM1 (0.953); MCM6–SMC2 (0.75); MCM6–SMC4 (0.734); MCM7–NCAPD2 (0.773); MCM7–ORC2 (0.997); MCM7–PCNA (0.985); MCM7–RRM1 (0.921); MCM7–SMC2 (0.7); MCM7–SMC4 (0.837); NCAPD2–SMC2 (0.999); NCAPD2–SMC4 (0.999); PCNA–RRM1 (0.933); PCNA–UBE2V2 (0.777); SMC2–SMC4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Activation of the pre-replicative complex, and GINS complex (FDR = 2.99e-06, 7 genes); Keyword DNA replication (FDR = 3.19e-06, 9 genes); NetworkNeighborAL DNA replication, and Regulation of DNA-directed DNA polymerase activity (FDR = 3.33e-06, 8 genes); Component CMG complex (FDR = 5.37e-06, 6 genes); COMPARTMENTS CMG complex (FDR = 5.89e-06, 6 genes); RCTM Unwinding of DNA (FDR = 7.73e-06, 6 genes); Component Nuclear chromosome (FDR = 9.01e-06, 10 genes); Component MCM complex (FDR = 9.01e-06, 5 genes); COMPARTMENTS MCM complex (FDR = 1.1e-05, 5 genes); Process Double-strand break repair via break-induced replication (FDR = 1.19e-05, 6 genes); WikiPathways G1 to S cell cycle control (FDR = 1.26e-05, 7 genes); WikiPathways DNA replication (FDR = 1.26e-05, 7 genes); RCTM DNA strand elongation (FDR = 1.63e-05, 7 genes); RCTM Activation of ATR in response to replication stress (FDR = 4.88e-05, 6 genes); RCTM Activation of the pre-replicative complex (FDR = 4.88e-05, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14758.1 (MCM4, MCM5, MCM7, MCM2, MCM6, GINS2; 6/14); huMAP3_08554.1 (MCM4, MCM5, MCM7, MCM2, MCM6, GINS2; 6/15); huMAP3_11832.1 (MCM4, MCM5, MCM7, MCM2, MCM6, GINS2; 6/15); huMAP3_12180.1 (MCM4, MCM5, MCM7, MCM2, MCM6, GINS2; 6/17); huMAP3_05529.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/6); huMAP3_11119.1 (MCM4, MCM5, MCM7, MCM6, GINS2; 5/14); huMAP3_06061.1 (MCM4, MCM7, MCM2, MCM6; 4/5); huMAP3_07113.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_09860.1 (MCM4, MCM2, MCM6; 3/4); huMAP3_00154.1 (MCM4, MCM2, MCM6; 3/5); huMAP3_03084.1 (SMC2, NCAPD2, SMC4; 3/8); huMAP3_14385.1 (SMC2, NCAPD2, SMC4; 3/9); huMAP3_09855.1 (SMC2, NCAPD2, SMC4; 3/10); huMAP3_11457.1 (SMC2, NCAPD2, SMC4; 3/10); huMAP3_09238.1 (MCM5, MCM7, GINS2; 3/11); huMAP3_14663.1 (SMC2, NCAPD2, SMC4; 3/14); huMAP3_09466.1 (MCM4, MCM2, MCM6; 3/23); huMAP3_13774.1 (PFAS, BAG2, HSPH1; 3/33); huMAP3_10862.1 (MCM4, MCM2, MCM6; 3/33); huMAP3_14306.1 (MCM4, MCM2, MCM6; 3/55); huMAP3_02602.1 (MCM4, MCM6; 2/2); huMAP3_03291.1 (PFAS, GART; 2/3); huMAP3_00676.1 (PFAS, GART; 2/4); huMAP3_06095.1 (GART, HK2; 2/5); huMAP3_10023.1 (GART, HK2; 2/7); huMAP3_06417.1 (MCM5, GINS2; 2/8); huMAP3_08399.1 (MCM5, GINS2; 2/10); huMAP3_08848.1 (MCM4, MCM6; 2/15); huMAP3_07919.1 (BAG2, HSPH1; 2/27); huMAP3_11049.1 (BAG2, HSPH1; 2/30); huMAP3_14723.1 (BAG2, HSPH1; 2/52)

### Novelty

The core biological interpretation is not a new molecular function: MCM–GINS replication machinery, ORC2, PCNA, condensin components and purine-biosynthesis enzymes are already represented in STRING and hu.MAP. The module may nevertheless be a new tissue-pair co-abundance observation because it identifies coordinated abundance across circulatory_system and kidney and links several established subsystems in this particular context. That contextual novelty cannot be established as a wholly new discovery from the fact sheet alone. Absence of some genes or pairs from STRING or hu.MAP is not evidence of biological novelty, especially because those resources represent curated or experimentally supported interactions rather than every co-abundance relationship. A stronger novelty claim would require comparison with published tissue-pair modules, matched datasets and independent replication.

**Hypothesis.** Hypothesis: the shared module reflects a conserved proliferative-cell state present in both tissue groups, in which MCM–GINS helicase activity and origin licensing support DNA replication, PCNA and RRM1 support synthesis and repair, purine-pathway enzymes supply nucleotide precursors, and condensin components organize replicated chromosomes. In circulatory-system samples, progenitor or other dividing blood-associated cells may contribute strongly to the signal; in kidney, dividing or regenerative cell populations may contribute. The cross-tissue co-abundance could therefore arise from shared cell-state composition rather than a tissue-specific secreted pathway. This hypothesis predicts that module abundance should track proliferation and progenitor-cell markers, and that cell-resolved or perturbation experiments should separate cell-composition effects from coordinated regulation within individual cells.

### Important genes

#### MCM5

- **Related proteins** (co-abundance neighbors): MCM7 (0.88), SMC2 (0.87), GINS2 (0.83), MCM2 (0.83), MCM4 (0.81), DCAF13 (0.80); STRING partners: GINS2 (0.999), MCM2 (0.999), MCM4 (0.999), MCM6 (0.999), MCM7 (0.999), NCAPD2 (0.736), ORC2 (0.999), PCNA (0.918), RRM1 (0.957), SMC2 (0.754), SMC4 (0.785)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_05529.1, huMAP3_11119.1, huMAP3_09238.1, huMAP3_06417.1, huMAP3_08399.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 5. The protein encoded by this gene is structurally very similar to the CDC46 protein from S. cerevisiae, a protein involved in the initiation of DNA replication. The encoded protein is a member of the MCM family of chromatin-binding proteins and can interact with at least two other members of this family. The encoded protein is upregulated in the transition from the G0 to G1/S phase of the cell cycl…
- **Diseases (Open Targets)**: Meier-Gorlin syndrome (0.563); neurodegenerative disease (0.397); lysosomal storage disease (0.362); kidney transplant (0.198); diabetic ketoacidosis (0.129)
- **Europe PMC papers**: 4143
- **Why important**: MCM5 is a central member of the replication core, connected in the module to MCM2, MCM4, MCM6, MCM7, GINS2, SMC2 and DCAF13. It appears across nearly all replication-related global terms and across the STRING replication annotations (GO:BP double-strand break repair via break-induced replication; q_global = 3.28e-07) (GO:CC CMG complex; q_global = 2.24e-06) (GO:CC MCM complex; q_global = 2.72e-06) (GO:CC DNA replication preinitiation complex; q_global = 4.55e-06) (GO:CC nuclear chromosome; q_global = 1.09e-05) (GO:BP regulation of DNA-templated DNA replication initiation; q_global = 0.000122) (GO:BP DNA-templated DNA replication; q_global = 0.000124) (GO:MF single-stranded DNA binding; q_global = 0.000251) (GO:BP DNA replication initiation; q_global = 0.00034) (GO:BP DNA replication; q_global = 0.000435) (GO:BP regulation of DNA-templated DNA replication; q_global = 0.000744) (KEGG DNA replication - Homo sapiens (human); q_global = 0.00086) (KEGG Cell cycle - Homo sapiens (human); q_global = 0.00301) (GO:BP regulation of DNA replication; q_global = 0.00399) (GO:MF four-way junction helicase activity; q_global = 0.00503) (GO:MF forked DNA-dependent helicase activity; q_global = 0.00503) (GO:CC protein-DNA complex; q_global = 0.00509) (GO:MF double-stranded DNA helicase activity; q_global = 0.00624) (GO:MF 3'-5' DNA helicase activity; q_global = 0.00624) (GO:MF single-stranded 3'-5' DNA helicase activity; q_global = 0.00624) (GO:CC chromosome, telomeric region; q_global = 0.0107) (GO:MF single-stranded DNA helicase activity; q_global = 0.013) (KEGG Homologous recombination - Homo sapiens (human); q_global = 0.014) (GO:MF ATP binding; q_global = 0.0254) (GO:MF adenyl ribonucleotide binding; q_global = 0.0271) (GO:MF DNA helicase activity; q_global = 0.0274) (GO:BP purine ribonucleoside monophosphate biosynthetic process; q_global = 0.0293) (GO:BP cell cycle DNA replication; q_global = 0.0293) (GO:BP nucleobase-containing compound metabolic process; q_global = 0.0362) (GO:BP double-strand break repair via homologous recombination; q_global = 0.0365) (GO:CC chromosomal region; q_global = 0.0374) (GO:BP recombinational repair; q_global = 0.0396) (STRING NetworkNeighborAL Activation of the pre-replicative complex, and GINS complex; within-query FDR = 2.99e-06) (STRING Keyword DNA replication; within-query FDR = 3.19e-06) (STRING NetworkNeighborAL DNA replication, and Regulation of DNA-directed DNA polymerase activity; within-query FDR = 3.33e-06) (STRING Component CMG complex; within-query FDR = 5.37e-06) (STRING COMPARTMENTS CMG complex; within-query FDR = 5.89e-06) (STRING RCTM Unwinding of DNA; within-query FDR = 7.73e-06) (STRING Component Nuclear chromosome; within-query FDR = 9.01e-06) (STRING Component MCM complex; within-query FDR = 9.01e-06) (STRING COMPARTMENTS MCM complex; within-query FDR = 1.1e-05) (STRING Process Double-strand break repair via break-induced replication; within-query FDR = 1.19e-05) (STRING WikiPathways G1 to S cell cycle control; within-query FDR = 1.26e-05) (STRING WikiPathways DNA replication; within-query FDR = 1.26e-05) (STRING RCTM DNA strand elongation; within-query FDR = 1.63e-05) (STRING RCTM Activation of ATR in response to replication stress; within-query FDR = 4.88e-05) (STRING RCTM Activation of the pre-replicative complex; within-query FDR = 4.88e-05). hu.MAP places it repeatedly in MCM–GINS and replication complexes (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_06417.1) (hu.MAP huMAP3_08399.1). It is tissue-enhanced in bone marrow and cell-type-enhanced in several progenitor populations. Its literature volume is substantial, and Open Targets links it to Meier–Gorlin syndrome and other disorders.
- **Conclusion**: Established evidence identifies MCM5 as a core replication-helicase component and a strong marker of the module's replication program. The co-abundance data support its importance as a module representative, but do not establish a tissue-specific role or a causal role in the shared tissue pattern.

#### MCM6

- **Related proteins** (co-abundance neighbors): MCM4 (0.90), SMC2 (0.82), NCAPD2 (0.82), RRM1 (0.81), PCNA (0.80); STRING partners: GINS2 (0.998), MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM7 (0.999), ORC2 (0.986), PCNA (0.912), RRM1 (0.953), SMC2 (0.75), SMC4 (0.734)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_05529.1, huMAP3_11119.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 6. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: lactose intolerance (0.246); neurodegenerative disease (0.225); obesity disorder (0.166); nervous system disorder (0.141); systemic lupus erythematosus (0.140)
- **Europe PMC papers**: 3766
- **Why important**: MCM6 is a core MCM component with module links to MCM4, SMC2, NCAPD2, RRM1 and PCNA. It is represented across the replication, helicase, repair and cell-cycle global terms (33 globally significant GO/KEGG terms, q_global 3.28e-07–0.0396; see the table) and in numerous hu.MAP replication complexes (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_08848.1). HPA places it in lymphoid tissue and in erythrocyte, megakaryocyte, monocyte and neutrophil progenitor populations. It has extensive literature and disease associations including Meier–Gorlin-related biology and systemic lupus erythematosus in Open Targets.
- **Conclusion**: Established evidence supports MCM6 as part of the MCM helicase and as a bridge between replication machinery and the chromosome-associated portion of the module. Its progenitor-enriched expression makes it compatible with a proliferative-cell explanation, but this remains an interpretation rather than proof of the source cell type.

#### MCM2

- **Related proteins** (co-abundance neighbors): MCM5 (0.83), MCM7 (0.82), DCAF13 (0.82), RRM1 (0.80); STRING partners: GINS2 (0.998), MCM4 (0.999), MCM5 (0.999), MCM6 (0.999), MCM7 (0.999), NCAPD2 (0.713), ORC2 (0.999), PCNA (0.939), RRM1 (0.914)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_05529.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a replication-core gene linked to MCM5, MCM7, DCAF13 and RRM1 in the module, with dense STRING relationships to GINS2, the other MCM proteins, ORC2, PCNA and RRM1. It contributes to the central global replication, helicase, repair and cell-cycle evidence (33 globally significant GO/KEGG terms, q_global 3.28e-07–0.0396; see the table) and recurs in many hu.MAP replication complexes (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_08848.1). It is enhanced in bone marrow and lymphoid tissue and in several progenitor populations. It has the largest literature volume among the selected replication genes and established disease associations including inherited hearing-loss and developmental phenotypes.
- **Conclusion**: Established evidence makes MCM2 a strong anchor for the interpretation that the module contains replication-initiation machinery. Its high literature volume means that its presence is biologically informative but not by itself novel. The module does not demonstrate that MCM2 drives the cross-tissue co-abundance.

#### PCNA

- **Related proteins** (co-abundance neighbors): FKBP4 (0.83), DDX5 (0.81), MCM6 (0.80); STRING partners: MCM2 (0.939), MCM4 (0.965), MCM5 (0.918), MCM6 (0.912), MCM7 (0.985), RRM1 (0.933), UBE2V2 (0.777)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proliferating cell nuclear antigen. The protein encoded by this gene is found in the nucleus and is a cofactor of DNA polymerase delta. The encoded protein acts as a homotrimer and helps increase the processivity of leading strand synthesis during DNA replication. In response to DNA damage, this protein is ubiquitinated and is involved in the RAD6-dependent DNA repair pathway. Two transcript variants encoding the same protein have b…
- **Diseases (Open Targets)**: ataxia-telangiectasia-like disorder (0.497); neurodegenerative disease (0.188); neoplasm (0.118); diabetes mellitus (0.116); hepatocellular carcinoma (0.113)
- **Europe PMC papers**: 61820
- **Why important**: PCNA links the MCM replication core to the broader module through its relationships with MCM2, MCM4, MCM5, MCM6, MCM7, RRM1, UBE2V2, FKBP4 and DDX5. It appears in global terms for DNA replication, the replication preinitiation complex, chromosome and telomeric regions, repair, cell cycle and DNA helicase-associated biology (12 globally significant GO/KEGG terms, q_global 1.09e-05–0.0374; see the table). STRING also supports its relationships with the MCM proteins and RRM1 (6 supplementary STRING terms; within-query FDR 3.19e-06–1.63e-05). HPA shows bone-marrow enhancement and progenitor-cell enhancement, and PCNA has extensive literature and disease associations.
- **Conclusion**: Established evidence identifies PCNA as a replication-processivity and DNA-repair factor that connects initiation machinery with synthesis and repair. Its position supports the module-level interpretation, while the shared tissue association remains compatible with either common proliferating cells or coordinated regulation.

#### SMC2

- **Related proteins** (co-abundance neighbors): MCM5 (0.87), MCM7 (0.83), MCM6 (0.82), MCM4 (0.82); STRING partners: MCM4 (0.748), MCM5 (0.754), MCM6 (0.75), MCM7 (0.7), NCAPD2 (0.999), SMC4 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_03084.1, huMAP3_14385.1, huMAP3_09855.1, huMAP3_11457.1, huMAP3_14663.1
- **Function (MyGene.info)**: structural maintenance of chromosomes 2. Predicted to enable ATP binding activity; chromatin binding activity; and single-stranded DNA binding activity. Involved in mitotic chromosome condensation. Located in condensed chromosome; cytoplasm; and nuclear lumen. Part of condensin complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: basal cell carcinoma (0.464); ovarian carcinoma (0.383); aortic stenosis (0.380); cancer (0.363); alcohol drinking (0.359)
- **Europe PMC papers**: 2065
- **Why important**: SMC2 forms a module bridge from the replication cluster to chromosome organization: it is connected to MCM5, MCM7, MCM6 and MCM4 and has a strong STRING relationship with SMC4 and NCAPD2. It contributes to the nuclear-chromosome, single-stranded-DNA-binding, ATP-binding and chromosome-condensation global terms (5 globally significant GO/KEGG terms, q_global 1.09e-05–0.0409; see the table). hu.MAP independently places SMC2 with SMC4 and NCAPD2 in condensin complexes (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_14663.1). It is enhanced in lymphoid tissue and in erythrocyte and megakaryocyte progenitor populations, with substantial literature and disease associations.
- **Conclusion**: Established evidence supports SMC2 as a condensin component and as the clearest connection between replication-associated genes and chromosome organization. Its network position suggests coordinated cell-cycle biology, but does not prove direct physical interaction with every replication gene in the module.

## Module 8

**Tissue pair**: circulatory_system and kidney  
**Genes (40)**: AP3D1, ATAD3A, BAG5, BAZ2A, CCDC86, CHD1, CSTF1, DCAF7, DDX20, DHFR, ESS2, GNL1, GOPC, HYPK, INTS3, ISY1, KDM5C, KTI12, MBD3, MOV10, NLE1, NUP43, NVL, CAD, URI1, RPP25L, POLR1F, RRP15, SCRN3, SEH1L, SMN1, STAM, TIA1, TRIM24, TRIM32, UBA5, UTP4, WDR74, ZC3H7A, ZC3HAV1

### Function

The primary functional inference is RNA metabolism, supported by the globally corrected GO term (GO:BP RNA metabolic process; q_global = 0.031), which covers many module genes. The gene annotations refine this broad signal toward coordinated nuclear RNA production and processing: rRNA transcription and maturation, ribosomal subunit biogenesis, spliceosome assembly and mRNA splicing, mRNA three-prime-end processing, RNA surveillance, and post-transcriptional regulation. Chromatin and transcriptional regulation are plausible supporting themes through TRIM24, KDM5C, MBD3, BAZ2A, CHD1, and INTS3, but these are not separate globally corrected GO or KEGG findings. The module therefore appears to represent a broadly shared nuclear RNA-metabolism and ribosome-production program rather than a tissue-specific pathway. The sparse network and mixed annotations argue against treating every gene as one physical complex.

**Cell composition.** This is not a plasma-protein or secreted-protein module: HPA reports no secreted genes. It is also not strongly blood-cell enriched. Most genes have low tissue specificity and low immune-cell specificity, while only limited genes show immune-cell enhancement or blood-related cell-type signals. HPA shows many cell-type-enhanced genes, especially in reproductive and neural cell types, with additional signals in kidney epithelial and other specialized cells. Kidney protein detection is common among the genes with available kidney data, but the module is not composed predominantly of kidney-specific genes. The shared circulatory-system and kidney signal is therefore more consistent with a broadly expressed intracellular housekeeping-like program, potentially influenced by shared cellular composition, than with circulating proteins or a blood-cell module. The reproductive and neural enrichment signals should be treated as contextual HPA expression patterns, not as proof that those tissues drive the co-abundance result.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA metabolic process | 0.031 | AP3D1, BAZ2A, CSTF1, DDX20, ESS2, INTS3, ISY1, KDM5C, KTI12, MBD3, MOV10, NVL, POLR1F, RPP25L, RRP15, SMN1, TIA1, TRIM24, TRIM32, URI1, UTP4, WDR74, ZC3H7A, ZC3HAV1 |

### STRING and hu.MAP

STRING provides a small set of strong or high-confidence relationships rather than dense external support for the whole module. Established relationships include DDX20 with SMN1, NUP43 with SEH1L, NVL with WDR74, RRP15 with WDR74, NLE1 with WDR74, and POLR1F with UTP4. These relationships independently support spliceosomal or RNA-processing biology, nucleocytoplasmic transport, and ribosome biogenesis. STRING supplementary keywords for nucleus and WD repeats (STRING Keyword Nucleus; within-query FDR = 0.011) (STRING Keyword WD repeat; within-query FDR = 0.0386) are consistent with this interpretation but are not globally corrected enrichment evidence. hu.MAP connects module genes to known assemblies: NUP43 and SEH1L occur in several Nup107-160 nuclear-pore complexes (hu.MAP huMAP3_07705.1) (hu.MAP huMAP3_08489.1) (hu.MAP huMAP3_09710.1) (hu.MAP huMAP3_09825.1) (hu.MAP huMAP3_12581.1); URI1 and POLR1F occur in RNA-polymerase-related assemblies (hu.MAP huMAP3_00807.1) (hu.MAP huMAP3_09057.1) (hu.MAP huMAP3_08487.1) (hu.MAP huMAP3_06426.1) (hu.MAP huMAP3_14318.1) (hu.MAP huMAP3_11092.1); ESS2 and ISY1 occur in spliceosome-associated assemblies (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1); SMN1 and DDX20 occur in spliceosomal and snRNP-related assemblies (hu.MAP huMAP3_04549.1) (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_08980.1); and CHD1 with WDR74, together with other complex members, appears in (hu.MAP huMAP3_01045.1). Because the hu.MAP overlaps generally contain only a small subset of each larger complex, the evidence supports reuse of known nuclear machinery but does not establish that the entire co-abundance module is one physical complex.

**STRING interactions (score >= 0.7)**: 6 of 780 gene pairs: DDX20–SMN1 (0.998); NLE1–WDR74 (0.74); NUP43–SEH1L (0.999); NVL–WDR74 (0.88); POLR1F–UTP4 (0.879); RRP15–WDR74 (0.968)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Nucleus (FDR = 0.011, 28 genes); Keyword WD repeat (FDR = 0.0386, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01045.1 (CHD1, WDR74; 2/5); huMAP3_07705.1 (NUP43, SEH1L; 2/9); huMAP3_08489.1 (NUP43, SEH1L; 2/10); huMAP3_09710.1 (NUP43, SEH1L; 2/13); huMAP3_09825.1 (NUP43, SEH1L; 2/27); huMAP3_00807.1 (URI1, POLR1F; 2/30); huMAP3_09057.1 (URI1, POLR1F; 2/36); huMAP3_08487.1 (URI1, POLR1F; 2/37); huMAP3_06426.1 (URI1, POLR1F; 2/38); huMAP3_08501.1 (ESS2, ISY1; 2/47); huMAP3_09504.1 (ESS2, ISY1; 2/51); huMAP3_04549.1 (SMN1, DDX20; 2/52); huMAP3_12581.1 (NUP43, SEH1L; 2/58); huMAP3_14318.1 (URI1, POLR1F; 2/58); huMAP3_09945.1 (ESS2, ISY1; 2/61); huMAP3_11092.1 (URI1, POLR1F; 2/65); huMAP3_06511.1 (SMN1, DDX20; 2/79); huMAP3_08980.1 (SMN1, DDX20; 2/97)

### Novelty

The module should not be called a wholly new biological pathway. Its strongest components are already anchored in established RNA-processing, ribosome-biogenesis, nuclear-pore, spliceosome, chromatin, and transcriptional machinery, as shown by the annotations, STRING relationships, and hu.MAP complexes. At the same time, the particular co-abundance organization across circulatory_system and kidney may be a new systems-level observation, because the external resources provide only sparse pairwise and partial-complex coverage and do not by themselves reproduce this exact module. Absence of a complete match in STRING or hu.MAP would not prove novelty. The defensible conclusion is that the module may offer a new cross-tissue co-abundance pattern assembled from largely known cellular functions, requiring replication, preservation testing, and comparison with independent cohorts before being described as a novel module.

**Hypothesis.** Hypothesis: the module reflects a shared demand for nuclear RNA production, processing, quality control, and ribosome assembly in cells represented in both tissues. A coordinated state involving RNA polymerase activity, rRNA maturation, spliceosome function, nuclear transport, chromatin regulation, and RNA surveillance could generate the observed co-abundance pattern. TRIM24 and chromatin regulators may help connect transcriptional state to RNA output; POLR1F, NVL, WDR74, and RRP15 may connect transcription to nucleolar ribosome production; and DDX20, SMN1, ESS2, and ISY1 may connect that state to spliceosomal processing. This is a mechanistic hypothesis, not a demonstrated causal pathway. The pattern could instead partly reflect shared abundance of broadly expressed intracellular proteins or shared cell states in the sampled tissues.

### Important genes

#### TRIM24

- **Related proteins** (co-abundance neighbors): KDM5C (0.84), NVL (0.84), MOV10 (0.84), ESS2 (0.84), ISY1 (0.82), GOPC (0.82), SMN1; SMN2 (0.81), ATAD3A (0.81), CAD (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tripartite motif containing 24. The protein encoded by this gene mediates transcriptional control by interaction with the activation function 2 (AF2) region of several nuclear receptors, including the estrogen, retinoic acid, and vitamin D3 receptors. The protein localizes to nuclear bodies and is thought to associate with chromatin and heterochromatin-associated factors. The protein is a member of the tripartite motif (TRIM) fa…
- **Diseases (Open Targets)**: cancer (0.609); neurodegenerative disease (0.540); leukemia (0.380); lung adenocarcinoma (0.374); acute lymphoblastic leukemia (0.372)
- **Europe PMC papers**: 2114
- **Why important**: TRIM24 is the most connected node in the module and links several RNA-related genes with chromatin and transcriptional regulators. It is annotated for transcriptional control, chromatin organization, protein ubiquitination, and nuclear-receptor interactions, and it has substantial disease and literature support. Its HPA profile is broadly expressed rather than tissue-specific, which fits a shared intracellular program.
- **Conclusion**: Established evidence supports TRIM24 as a network hub connecting transcriptional and chromatin regulation to the RNA-metabolism signal (GO:BP RNA metabolic process; q_global = 0.031). It is a strong candidate for coordinating module state, but the co-abundance data do not establish that TRIM24 regulates the other module genes in these tissues. Any causal role remains a hypothesis.

#### NVL

- **Related proteins** (co-abundance neighbors): TRIM24 (0.84), SCRN3 (0.84), CSTF1 (0.82), WDR74 (0.82), HYPK (0.81), POLR1F (0.80); STRING partners: WDR74 (0.88)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nuclear VCP like. This gene encodes a member of the AAA (ATPases associated with diverse cellular activities) superfamily. Multiple transcript variants encoding different isoforms have been found for this gene. Two encoded proteins, described as major and minor isoforms, have been localized to distinct regions of the nucleus. The largest encoded protein (major isoform) has been localized to the nucleolus and shown …
- **Diseases (Open Targets)**: neurodegenerative disease (0.459); Parkinson disease (0.370); lysosomal storage disease (0.370); Alzheimer disease (0.370); glioblastoma (0.263)
- **Europe PMC papers**: 717
- **Why important**: NVL is a relatively central module node and is connected to TRIM24, WDR74, CSTF1, POLR1F, and other RNA-associated genes. Its nucleolar localization and established roles in rRNA processing, ribosome biogenesis, and large-subunit biogenesis directly match (GO:BP RNA metabolic process; q_global = 0.031). Its STRING relationship with WDR74 provides external support, while its kidney detection and low tissue specificity are compatible with a shared cellular program.
- **Conclusion**: Established evidence identifies NVL as a plausible bridge between general RNA metabolism and nucleolar ribosome production. The network suggests that it may help organize the ribosome-biogenesis component, but co-abundance alone cannot demonstrate physical interaction or directionality.

#### WDR74

- **Related proteins** (co-abundance neighbors): DDX20 (0.83), CHD1 (0.82), NVL (0.82), NLE1 (0.81), RPP25L (0.81); STRING partners: NLE1 (0.74), NVL (0.88), RRP15 (0.968)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in none
- **hu.MAP 3.0**: huMAP3_01045.1
- **Function (MyGene.info)**: WD repeat domain 74. Involved in rRNA processing and ribosomal large subunit biogenesis. Located in nucleoplasm. Colocalizes with nuclear exosome (RNase complex) and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy 119 (0.470); neurodevelopmental disorder (0.401); neurodevelopmental disorder with seizures and brain abnormalities (0.340); colorectal carcinoma (0.074); cancer (0.062)
- **Europe PMC papers**: 312
- **Why important**: WDR74 connects DDX20, NVL, NLE1, CHD1, and RPP25L in the co-abundance graph. It is annotated for rRNA processing and ribosomal large-subunit biogenesis, is nucleolar or nucleoplasmic, and has several STRING relationships, including with NVL and RRP15. It also participates in a hu.MAP complex with CHD1 (hu.MAP huMAP3_01045.1). Its bone-marrow tissue enhancement is notable, but its overall blood-cell specificity is low.
- **Conclusion**: Established evidence supports WDR74 as a central ribosome-biogenesis and RNA-processing component and as one of the better externally supported module nodes. A hypothesis is that WDR74 helps couple nucleolar assembly with broader transcriptional or chromatin state, but this coupling is not directly demonstrated here.

#### DDX20

- **Related proteins** (co-abundance neighbors): ZC3H7A (0.86), WDR74 (0.83), RRP15 (0.82), UTP4 (0.81), MBD3 (0.80); STRING partners: SMN1 (0.998)
- **HPA**: Tissue enriched; Group enriched; blood Low immune cell specificity; location Nuclear bodies; IHC detected in none
- **hu.MAP 3.0**: huMAP3_04549.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: DEAD-box helicase 20. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.340); multisite chronic pain (0.287); hypertensive disorder (0.279); Abnormality of the skeletal system (0.275); essential hypertension (0.254)
- **Europe PMC papers**: 528
- **Why important**: DDX20 is connected to several module genes and has a very strong STRING relationship with SMN1. Its annotations include RNA processing, spliceosomal snRNP assembly, and spliceosomal tri-snRNP assembly, and hu.MAP places it with SMN1 in multiple snRNP-related complexes (hu.MAP huMAP3_04549.1) (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_08980.1). Its tissue-enriched and reproductive-cell HPA signals make it biologically distinctive within an otherwise broadly expressed module.
- **Conclusion**: Established evidence supports DDX20 as a spliceosome and snRNP-associated anchor that connects known complexes to this module (GO:BP RNA metabolic process; q_global = 0.031). The reproductive HPA pattern may indicate context dependence, but it does not show that reproductive cells explain the circulatory-system and kidney module. A broader coordinating role remains hypothetical.

#### NUP43

- **Related proteins** (co-abundance neighbors): DCAF7 (0.82); STRING partners: SEH1L (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_07705.1, huMAP3_08489.1, huMAP3_09710.1, huMAP3_09825.1, huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 43. Bidirectional transport of macromolecules between the cytoplasm and nucleus occurs through nuclear pore complexes (NPCs) embedded in the nuclear envelope. NPCs are composed of subcomplexes, and NUP43 is part of one such subcomplex, Nup107-160 (Loiodice et al., 2004 [PubMed 15146057]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); Histiocytosis (0.370); COVID-19 (0.370)
- **Europe PMC papers**: 494
- **Why important**: NUP43 is externally supported by a very strong STRING relationship with SEH1L and by repeated hu.MAP membership of Nup107-160 nuclear-pore assemblies (hu.MAP huMAP3_07705.1) (hu.MAP huMAP3_08489.1) (hu.MAP huMAP3_09710.1) (hu.MAP huMAP3_09825.1) (hu.MAP huMAP3_12581.1). Its annotation establishes a role in nucleocytoplasmic transport, and its module connection to DCAF7 links transport with protein-complex scaffolding. HPA places it in nuclear speckles or nucleoplasm and shows kidney detection.
- **Conclusion**: Established evidence supports NUP43 as the module's clearest nuclear-pore and transport representative. Its presence suggests that RNA metabolism may be coupled to nuclear import or export, but the module does not prove that transport is the primary driver or that NUP43 directly controls RNA processing.

## Module 9

**Tissue pair**: circulatory_system and kidney  
**Genes (21)**: ATRX, CETN2, HMGB3, CHUK, ITSN1, MAP7D3, CHCHD4, MRTFB, NAA50, NDUFA6, NDUFAF7, C17orf75, NUP37, OSBPL8, P3H1, PELO, RABEP1, RBM45, STAMBP, SUMF2, TRAPPC9

### Function

The most coherent interpretation is a membrane-trafficking and signaling-associated module, centered on endocytic, vesicular, and intracellular transport functions. ITSN1 is the most connected node and is annotated for endosomal transport, clathrin-coated vesicle formation, and coordination of membrane traffic with actin assembly. RABEP1 is an endocytic-vesicle and endosome-associated Rab effector, TRAPPC9 is associated with vesicle transport between the endoplasmic reticulum, Golgi, and early endosome, and C17orf75 is involved in vesicle tethering to the Golgi. Additional genes represent potentially connected cellular processes, including cytokine and NF-kappa-B signaling through CHUK, mitochondrial respiratory-chain biology through NDUFA6, NDUFAF7, and CHCHD4, nuclear transport through NUP37, RNA surveillance through PELO and RBM45, and chromatin regulation through ATRX. Thus, the module appears biologically heterogeneous but is most plausibly organized around intracellular trafficking and signaling interfaces rather than a single narrowly defined pathway. No GO/KEGG term passed global correction, so the functional interpretation is hypothesis-generating rather than an enrichment-based conclusion.

**Cell composition.** This is not a plasma-protein or secreted-protein-dominated module: the HPA summary identifies only a small secreted subset, while most genes have low tissue specificity. The module is also not strongly blood-cell enriched overall. Most genes have low immune-cell specificity, with only limited enrichment involving eosinophils or monocytes. Many genes are cell-type enhanced in specialized populations, including trophoblasts, germ-cell populations, ciliated cells, adipocytes, macrophages, endothelial cells, and muscle cells. This broad and mixed HPA pattern argues against interpreting the shared circulatory-system and kidney signal as a simple plasma-protein program or a uniform blood-cell contaminant. However, the wide distribution of cell-type-associated signals means that shared cell populations, cellular composition, or common stress and trafficking states could contribute to the co-abundance pattern. Protein detection is well supported in kidney for most of the module genes, whereas the circulatory-system HPA tissue comparison has no matching tissue data, limiting direct tissue-specific interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no high-confidence pairwise interactions among the module genes and no supplementary STRING enrichment. This means the co-abundance relationships are not reproduced as a dense, already-established physical or functional interaction network in STRING, and the module should not be described as a validated STRING complex. hu.MAP provides a more specific but limited result: STAMBP and ITSN1 occur together in the three listed hu.MAP complexes, (hu.MAP huMAP3_10762.1), (hu.MAP huMAP3_12918.1), and (hu.MAP huMAP3_12394.1). These complexes are broad trafficking and endocytic assemblies containing many proteins that are not in the module, so the repeated STAMBP–ITSN1 membership supports a known molecular connection but does not explain the entire module. The absence of additional hu.MAP overlap and the absence of STRING edges suggest that much of the co-abundance structure may reflect coordinated expression, shared cellular context, indirect regulation, or technical and compositional effects rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 0 of 210 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10762.1 (STAMBP, ITSN1; 2/62); huMAP3_12918.1 (STAMBP, ITSN1; 2/62); huMAP3_12394.1 (STAMBP, ITSN1; 2/98)

### Novelty

The module cannot be called a wholly new molecular complex. The STAMBP–ITSN1 relationship is already represented in hu.MAP (hu.MAP huMAP3_10762.1), (hu.MAP huMAP3_12918.1), and (hu.MAP huMAP3_12394.1), and the individual functions of several genes are well established. At the same time, the particular cross-tissue co-abundance configuration is not explained by the available interaction resources: STRING contains no high-confidence edges for the module, and the hu.MAP evidence covers only a repeated pair within large complexes. Therefore, the appropriate conclusion is that the module may represent a novel expression-level association or a context-dependent combination of known processes, but novelty remains unproven. Replication in independent circulatory-system and kidney cohorts, cell-composition adjustment, and experimental testing of the predicted trafficking and signaling relationships would be required before claiming a new biological mechanism.

**Hypothesis.** Hypothesis: in shared cellular populations present in circulatory-system and kidney samples, coordinated regulation of endocytic and vesicular trafficking genes may couple membrane cargo handling to cytokine signaling, organelle function, and transcriptional responses. ITSN1, RABEP1, TRAPPC9, and C17orf75 could define the trafficking component; STAMBP could connect trafficking to receptor and JAK-STAT-associated signaling; and CHUK could connect that state to NF-kappa-B activation. The mitochondrial and nuclear genes may reflect the energetic, RNA-processing, and transcriptional demands of this state rather than belonging to one physical complex. This remains a mechanistic hypothesis because the module has no globally significant GO/KEGG term, no STRING interaction support, and only limited hu.MAP overlap.

### Important genes

#### ITSN1

- **Related proteins** (co-abundance neighbors): CETN2 (0.88), TRAPPC9 (0.88), C17orf75 (0.82), OSBPL8 (0.80), CHCHD4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_10762.1, huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: intersectin 1. The protein encoded by this gene is a cytoplasmic membrane-associated protein that indirectly coordinates endocytic membrane traffic with the actin assembly machinery. In addition, the encoded protein may regulate the formation of clathrin-coated vesicles and could be involved in synaptic vesicle recycling. This protein has been shown to interact with dynamin, CDC42, SNAP23, SNAP25, SPIN90, EPS15,…
- **Diseases (Open Targets)**: hereditary disease (0.531); neurodevelopmental disorder (0.451); Autistic behavior (0.404); Intellectual disability (0.378); autosomal dominant non-syndromic intellectual disability (0.371)
- **Europe PMC papers**: 1094
- **Why important**: ITSN1 is the central network node by weighted connectivity and has the clearest functional link to the inferred module: it is a membrane-associated regulator of endosomal transport, clathrin-coated vesicles, actin assembly, and signaling. It is also the only selected gene with repeated hu.MAP membership together with STAMBP across (hu.MAP huMAP3_10762.1), (hu.MAP huMAP3_12918.1), and (hu.MAP huMAP3_12394.1). Its disease associations include hereditary and neurodevelopmental disorders, and its literature volume is substantial, making it the best-supported trafficking anchor.
- **Conclusion**: Established evidence supports ITSN1 as a membrane-trafficking and signaling scaffold. It is plausible, but not established, that ITSN1 helps organize the shared co-abundance state in circulatory-system and kidney samples.

#### STAMBP

- **Related proteins** (co-abundance neighbors): MRTFB (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_10762.1, huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: STAM binding protein. Cytokine-mediated signal transduction in the JAK-STAT cascade requires the involvement of adaptor molecules. One such signal-transducing adaptor molecule contains an SH3 domain that is required for induction of MYC and cell growth. The protein encoded by this gene binds to the SH3 domain of the signal-transducing adaptor molecule, and plays a critical role in cytokine-mediated signaling for MYC in…
- **Diseases (Open Targets)**: microcephaly-capillary malformation syndrome (0.799); neurodegenerative disease (0.433); stroke disorder (0.307); alcohol drinking (0.297); hereditary disease (0.194)
- **Europe PMC papers**: 563
- **Why important**: STAMBP is important because it is the second member of the repeated hu.MAP pair with ITSN1 in (hu.MAP huMAP3_10762.1), (hu.MAP huMAP3_12918.1), and (hu.MAP huMAP3_12394.1). Its annotation connects it to cytokine-mediated signaling, JAK-STAT-associated receptor signaling, protein deubiquitination, cell proliferation, and negative regulation of Ras and phosphatidylinositol three-kinase/protein kinase B signaling. It occupies a direct module edge and has a strong disease association with microcephaly-capillary malformation syndrome, while retaining a substantial literature base.
- **Conclusion**: Established evidence supports STAMBP as a signaling and deubiquitination regulator with known complex-level association with ITSN1. Its proposed role as the bridge between endocytic trafficking and cytokine signaling in this module is a hypothesis.

#### RABEP1

- **Related proteins** (co-abundance neighbors): MRTFB (0.83), ATRX (0.81), TRAPPC9 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: rabaptin, RAB GTPase binding effector protein 1. Enables protein domain specific binding activity and protein homodimerization activity. Involved in vesicle-mediated transport. Located in endocytic vesicle and endosome. Part of protein-containing complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Alzheimer disease (0.332); placenta praevia (0.228); dementia (0.188); breast carcinoma (0.187); pancreatic ductal adenocarcinoma (0.185)
- **Europe PMC papers**: 525
- **Why important**: RABEP1 is a vesicle and endosome-associated Rab effector annotated for endocytosis, membrane fusion, Golgi-to-plasma-membrane transport, and vesicle-mediated transport. It links the ITSN1-associated branch to TRAPPC9 and to MRTFB, giving it a potentially informative position at the interface of trafficking and other module processes. Its disease associations include Alzheimer disease, dementia, cancer, and placenta praevia, and it has a meaningful literature base.
- **Conclusion**: Established evidence supports RABEP1 as a vesicle-trafficking regulator. Its position suggests that it could transmit or stabilize the inferred trafficking signal, but a specific role in the shared tissue module is not demonstrated.

#### CHUK

- **Related proteins** (co-abundance neighbors): CETN2 (0.83), NDUFA6 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: component of inhibitor of nuclear factor kappa B kinase complex. This gene encodes a member of the serine/threonine protein kinase family. The encoded protein, a component of a cytokine-activated protein complex that is an inhibitor of the essential transcription factor NF-kappa-B complex, phosphorylates sites that trigger the degradation of the inhibitor via the ubiquination pathway, thereby activating the transcription factor. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: cocoon syndrome (0.635); COVID-19 (0.464); Bartsocas-Papas syndrome 1 (0.404); neurodegenerative disease (0.371); autoimmune disorder of central nervous system (0.370)
- **Europe PMC papers**: 3359
- **Why important**: CHUK is the module's clearest annotated inflammatory-signaling component. It encodes a kinase in the inhibitor of NF-kappa-B kinase complex and is associated with canonical NF-kappa-B signaling, pattern-recognition receptor signaling, inflammatory responses, and immune responses. It connects in the module to CETN2 and NDUFA6 and has the largest literature volume among the selected trafficking and signaling candidates, with disease associations including cocoon syndrome, COVID-19, and autoimmune disease.
- **Conclusion**: Established evidence supports CHUK as a regulator of NF-kappa-B-dependent inflammatory signaling. The idea that CHUK activity is coordinated with the module's vesicle-trafficking program is a hypothesis rather than a demonstrated physical or regulatory interaction.

#### NDUFA6

- **Related proteins** (co-abundance neighbors): CHUK (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, End piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit A6. This gene encodes a member of the LYR family of proteins that contain a highly conserved tripeptide (LYR) motif near the N-terminus. The encoded protein is an accessory subunit of NADH: ubiquinone oxidorerductase (Complex I), which is the largest enzyme of the mitochondrial membrane respiratory chain. Complex I functions in electron transfer from NADH to the respiratory chain. [provided by RefSeq,…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 33 (0.709); type 2 diabetes mellitus (0.609); mitochondrial complex I deficiency (0.601); diabetes mellitus (0.578); neurodegenerative disease (0.567)
- **Europe PMC papers**: 1085
- **Why important**: NDUFA6 provides a mechanistically relevant mitochondrial component. It is an accessory subunit of respiratory-chain complex I and is annotated for electron transport, aerobic respiration, proton motive force, ATP synthesis, and complex I assembly. It is connected in the module to CHUK and has disease associations with mitochondrial complex I deficiency and diabetes, supporting its relevance to cellular energetic state.
- **Conclusion**: Established evidence supports NDUFA6 as a complex I-associated mitochondrial protein with disease relevance. Its inclusion may indicate energetic coupling to the inferred trafficking and signaling state, but that coupling is a hypothesis and is not established by the available interaction evidence.

## Module 10

**Tissue pair**: circulatory_system and kidney  
**Genes (26)**: SLC4A2, CDH2, CALU, ALCAM, CD44, CEMIP2, SLC44A1, TBRG4, FAM3C, GPD2, IKBIP, ITGA5, ITGAV, ITGB3, KRT19, IGF2R, MCAM, NCEH1, NRP2, PON2, PVR, SCRIB, YARS2, TGOLN2, TM9SF2, AXL

### Function

The module is best interpreted as a cell-surface adhesion and receptor-signaling program. Primary evidence supports cell surface, plasma membrane, receptor complex, focal adhesion, cell-substrate junction, anchoring junction, cell-cell adhesion, integrin complex, vascular endothelial growth factor signaling, wound healing, tube development, blood-vessel morphogenesis, and ECM-receptor interaction (GO:CC cell surface; q_global = 4.82e-05)(GO:CC plasma membrane; q_global = 6.99e-05)(GO:MF signaling receptor activity; q_global = 8.11e-05)(GO:CC receptor complex; q_global = 0.00011)(GO:BP heterophilic cell-cell adhesion; q_global = 0.00053)(GO:BP cell adhesion; q_global = 0.00086)(GO:CC focal adhesion; q_global = 0.00137)(GO:CC cell-substrate junction; q_global = 0.00155)(GO:BP vascular endothelial growth factor signaling pathway; q_global = 0.00418)(GO:BP cell-cell adhesion; q_global = 0.00458)(GO:CC anchoring junction; q_global = 0.00676)(GO:BP wound healing, spreading of cells; q_global = 0.0073)(GO:BP tube development; q_global = 0.0127)(GO:BP cellular response to vascular endothelial growth factor stimulus; q_global = 0.0208)(GO:BP tube morphogenesis; q_global = 0.023)(GO:BP wound healing; q_global = 0.0233)(GO:CC integrin complex; q_global = 0.0271)(GO:CC plasma membrane signaling receptor complex; q_global = 0.0291)(GO:BP blood vessel morphogenesis; q_global = 0.0354)(KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0448). The coherent biological interpretation is coordinated regulation of cell-cell and cell-matrix contacts, receptor signaling, migration, vascular remodeling, and tissue repair. Virus-receptor, exogenous-protein-binding, and symbiont-entry terms (GO:MF virus receptor activity; q_global = 0.00356)(GO:MF exogenous protein binding; q_global = 0.00416)(KEGG Virion - Herpesvirus - Homo sapiens (human); q_global = 0.0102)(GO:BP symbiont entry into host cell; q_global = 0.0189)(GO:BP symbiont entry into host; q_global = 0.023) are secondary consequences of an abundance of exposed membrane receptors rather than the central physiological function. The module therefore represents a membrane adhesion and signaling system rather than a single linear pathway.

**Cell composition.** The module is predominantly composed of membrane-associated and cell-surface proteins, not mainly plasma or secreted proteins. HPA supports plasma-membrane, cell-surface, junctional, vesicular, Golgi, endoplasmic-reticulum, or related localization across the genes, consistent with (GO:CC cell surface; q_global = 4.82e-05)(GO:CC plasma membrane; q_global = 6.99e-05)(GO:CC cell periphery; q_global = 0.00017)(GO:CC focal adhesion; q_global = 0.00137)(GO:CC cell-substrate junction; q_global = 0.00155). Several genes are secreted to blood or have blood-associated detection, including CD44, ALCAM, FAM3C, PON2, NRP2, and PVR, but this is not the dominant module property. HPA shows heterogeneous cell associations involving vascular cells, pericytes, podocytes, epithelial cells, cardiomyocytes, platelets, stromal cells, neutrophils, and other myeloid populations. The shared circulatory-system and kidney signal may therefore reflect a conserved vascular or tissue-interface program, but shared blood, immune, stromal, epithelial, or platelet composition could also contribute. Broad kidney protein detection supports relevance to kidney tissue, while heterogeneous blood-cell specificity argues against interpreting the module as either a pure kidney-parenchymal program or a pure circulating-plasma signature.

**GO/KEGG enrichment**: 42 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC cell surface | 4.82e-05 | ALCAM, AXL, CD44, CDH2, IGF2R, ITGA5, ITGAV, ITGB3, MCAM, PVR |
| GO:CC plasma membrane | 6.99e-05 | ALCAM, AXL, CD44, CDH2, CEMIP2, IGF2R, ITGA5, ITGAV, ITGB3, KRT19, MCAM, NCEH1, NRP2, PON2, PVR, SCRIB, SLC44A1, SLC4A2, TGOLN2, TM9SF2 |
| GO:MF signaling receptor activity | 8.11e-05 | AXL, CD44, IGF2R, ITGA5, ITGAV, ITGB3, NRP2, PVR |
| GO:MF molecular transducer activity | 8.11e-05 | AXL, CD44, IGF2R, ITGA5, ITGAV, ITGB3, NRP2, PVR |
| GO:CC receptor complex | 0.00011 | ALCAM, AXL, CD44, ITGA5, ITGAV, ITGB3, NRP2 |
| GO:CC cell periphery | 0.00017 | ALCAM, AXL, CD44, CDH2, CEMIP2, IGF2R, ITGA5, ITGAV, ITGB3, KRT19, MCAM, NCEH1, NRP2, PON2, PVR, SCRIB, SLC44A1, SLC4A2, TGOLN2, TM9SF2 |
| GO:BP heterophilic cell-cell adhesion | 0.00053 | ALCAM, CDH2, ITGA5, PVR |
| GO:BP cell adhesion | 0.00086 | ALCAM, AXL, CD44, CDH2, ITGA5, ITGAV, ITGB3, MCAM, NRP2, PVR, SCRIB, SLC4A2 |
| GO:CC focal adhesion | 0.00137 | ALCAM, CD44, CDH2, IGF2R, ITGA5, ITGAV, ITGB3, MCAM, PVR, SLC4A2 |
| GO:CC cell-substrate junction | 0.00155 | ALCAM, CD44, CDH2, IGF2R, ITGA5, ITGAV, ITGB3, MCAM, PVR, SLC4A2 |
| GO:MF virus receptor activity | 0.00356 | AXL, ITGA5, ITGAV, ITGB3, PVR |
| GO:MF exogenous protein binding | 0.00416 | AXL, ITGA5, ITGAV, ITGB3, PVR |
| GO:BP vascular endothelial growth factor signaling pathway | 0.00418 | AXL, ITGA5, ITGB3, NRP2 |
| GO:BP cell-cell adhesion | 0.00458 | ALCAM, CD44, CDH2, ITGA5, ITGAV, ITGB3, PVR, SCRIB, SLC4A2 |
| GO:CC anchoring junction | 0.00676 | ALCAM, CD44, CDH2, IGF2R, ITGA5, ITGAV, ITGB3, MCAM, PVR, SCRIB, SLC4A2 |

### STRING and hu.MAP

STRING supports established relationships among the core adhesion machinery, including CD44 with ALCAM, CDH2, ITGA5, ITGAV, ITGB3, and MCAM; the integrin-related ITGA5, ITGAV, and ITGB3 group; and CDH2 with ITGA5 (STRING Keyword Receptor; within-query FDR = 6.86e-07)(STRING Keyword Cell adhesion; within-query FDR = 4.48e-06). STRING functional annotations support receptors, cell adhesion, glycoproteins, transmembrane helices, plasma membrane, and cell surface (STRING Keyword Signal; within-query FDR = 5.09e-10)(STRING Keyword Glycoprotein; within-query FDR = 8.44e-10)(STRING Keyword Transmembrane helix; within-query FDR = 4.55e-08)(STRING Component Integral component of plasma membrane; within-query FDR = 8.51e-08)(STRING Keyword Receptor; within-query FDR = 6.86e-07)(STRING COMPARTMENTS Plasma membrane; within-query FDR = 1.17e-06)(STRING Component Cell surface; within-query FDR = 1.33e-06)(STRING Component Plasma membrane; within-query FDR = 1.78e-06)(STRING Keyword Cell adhesion; within-query FDR = 4.48e-06)(STRING Keyword Membrane; within-query FDR = 2.3e-05)(STRING COMPARTMENTS Integral component of plasma membrane; within-query FDR = 2.4e-05). IGF2R-TGOLN2 is another known relationship. hu.MAP places ALCAM and ITGA5 together in several broader complexes (hu.MAP huMAP3_10503.1)(hu.MAP huMAP3_10980.1)(hu.MAP huMAP3_11349.1), but each complex contains many proteins outside the module, so this does not establish a single complete module-specific complex. The co-abundance network therefore recapitulates known adhesion biology in its core while also coordinating genes without matching high-confidence physical-interaction evidence. This may reflect shared cell states, tissue composition, or coordinated regulation in addition to direct molecular binding.

**STRING interactions (score >= 0.7)**: 11 of 325 gene pairs: ALCAM–CD44 (0.859); CD44–CDH2 (0.84); CD44–ITGA5 (0.785); CD44–ITGAV (0.85); CD44–ITGB3 (0.838); CD44–MCAM (0.7); CDH2–ITGA5 (0.712); IGF2R–TGOLN2 (0.891); ITGA5–ITGAV (0.946); ITGA5–ITGB3 (0.999); ITGAV–ITGB3 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Signal (FDR = 5.09e-10, 16 genes); Keyword Glycoprotein (FDR = 8.44e-10, 17 genes); Keyword Transmembrane helix (FDR = 4.55e-08, 17 genes); Component Integral component of plasma membrane (FDR = 8.51e-08, 11 genes); Component Integral component of membrane (FDR = 9.14e-08, 19 genes); Keyword Receptor (FDR = 6.86e-07, 8 genes); COMPARTMENTS Plasma membrane (FDR = 1.17e-06, 17 genes); COMPARTMENTS Cell periphery (FDR = 1.17e-06, 18 genes); Component Cell surface (FDR = 1.33e-06, 10 genes); Component Plasma membrane (FDR = 1.78e-06, 20 genes); COMPARTMENTS Cell surface (FDR = 2.43e-06, 9 genes); Keyword Cell adhesion (FDR = 4.48e-06, 8 genes); Keyword Disulfide bond (FDR = 6.77e-06, 12 genes); Keyword Membrane (FDR = 2.3e-05, 20 genes); COMPARTMENTS Integral component of plasma membrane (FDR = 2.4e-05, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10503.1 (ITGA5, ALCAM; 2/27); huMAP3_10980.1 (ITGA5, ALCAM; 2/44); huMAP3_11349.1 (ITGA5, ALCAM; 2/78)

### Novelty

The module should not be described as a wholly new molecular pathway. Its central functions and several core relationships are already established by GO, STRING, hu.MAP, and the extensive literature for CD44, CDH2, integrins, ALCAM, MCAM, AXL, and NRP2. Its potentially novel contribution is a conserved tissue-pair-specific co-abundance organization linking adhesion, vascular signaling, membrane trafficking, and tissue remodeling across circulatory system and kidney. Relationships absent from STRING or hu.MAP may indicate an undercatalogued co-expression relationship, but database absence alone does not demonstrate novelty. A strong novelty claim requires independent replication, adjustment for blood and vascular-cell abundance, and comparison with existing tissue co-expression modules.

**Hypothesis.** Hypothesis: the module is a conserved vascular and tissue-interface program in which integrin adhesion, cadherin and immunoglobulin-family contacts, hyaluronan-associated signaling, and receptor-kinase inputs coordinate cell attachment, migration, barrier remodeling, and repair in kidney and circulatory tissues. ITGA5, ITGAV, and ITGB3 may provide matrix adhesion and signaling; CDH2, CD44, ALCAM, and MCAM may organize cell-cell and cell-matrix contacts; AXL and NRP2 may connect the surface state to growth-factor, vascular, immune, or stromal signals; and trafficking or membrane-homeostasis genes may support receptor localization. An alternative hypothesis is that the module is partly driven by shared vascular, stromal, epithelial, platelet, or leukocyte abundance in the samples rather than by one mechanism operating in every cell.

### Important genes

#### CD44

- **Related proteins** (co-abundance neighbors): ALCAM (0.85), SLC4A2 (0.85), ITGAV (0.84), MCAM (0.82), AXL (0.81), CEMIP2 (0.81); STRING partners: ALCAM (0.859), CDH2 (0.84), ITGA5 (0.785), ITGAV (0.85), ITGB3 (0.838), MCAM (0.7)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD44 molecule (IN blood group). The protein encoded by this gene is a cell-surface glycoprotein involved in cell-cell interactions, cell adhesion and migration. It is a receptor for hyaluronic acid (HA) and can also interact with other ligands, such as osteopontin, collagens, and matrix metalloproteinases (MMPs). This protein participates in a wide variety of cellular functions including lymphocyte activation, recirculation and …
- **Diseases (Open Targets)**: nephrolithiasis, calcium oxalate (0.523); calcium oxalate urolithiasis (0.521); uterine corpus leiomyoma (0.480); systemic lupus erythematosus (0.467); autoimmune disease (0.330)
- **Europe PMC papers**: 102058
- **Why important**: CD44 is a central network hub connected to ALCAM, CDH2, ITGA5, ITGAV, ITGB3, MCAM, SLC4A2, AXL, and CEMIP2. It appears across primary adhesion, receptor, membrane, wound-healing, and ECM-related terms (GO:CC cell surface; q_global = 4.82e-05)(GO:CC plasma membrane; q_global = 6.99e-05)(GO:MF signaling receptor activity; q_global = 8.11e-05)(GO:CC receptor complex; q_global = 0.00011)(GO:BP cell adhesion; q_global = 0.00086)(GO:CC focal adhesion; q_global = 0.00137)(GO:CC cell-substrate junction; q_global = 0.00155)(GO:BP cell-cell adhesion; q_global = 0.00458)(GO:CC anchoring junction; q_global = 0.00676)(GO:BP wound healing, spreading of cells; q_global = 0.0073)(GO:BP wound healing; q_global = 0.0233)(KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0448). Established functions include hyaluronan binding, cell adhesion, migration, inflammatory responses, lymphocyte trafficking, and interactions with matrix-associated ligands. HPA detects it in kidney and associates it with monocytes, neutrophils, mast cells, and dendritic cells. Its extensive literature and disease associations further support its importance.
- **Conclusion**: Established evidence supports CD44 as a major organizing receptor for the adhesion and migration component of the module. It may bridge tissue-interface biology with blood-cell-associated signal, but co-abundance does not establish causality.

#### ITGAV

- **Related proteins** (co-abundance neighbors): NCEH1 (0.87), CD44 (0.84), SLC44A1 (0.83), IKBIP (0.83), ITGA5 (0.81); STRING partners: CD44 (0.85), ITGA5 (0.946), ITGB3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha V. The product of this gene belongs to the integrin alpha chain family. Integrins are heterodimeric integral membrane proteins composed of an alpha subunit and a beta subunit that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha V subunit. This subunit associates with beta 1, beta 3, beta…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); myocardial infarction (0.396); angina pectoris (0.371); Recurrent thrombophlebitis (0.370); intermediate coronary syndrome (0.370)
- **Europe PMC papers**: 5475
- **Why important**: ITGAV is a network-connected integrin component linked to CD44, ITGA5, NCEH1, SLC44A1, and IKBIP. It contributes to integrin-complex, adhesion, vascular, and ECM-receptor evidence (GO:MF signaling receptor activity; q_global = 8.11e-05)(GO:CC receptor complex; q_global = 0.00011)(GO:CC focal adhesion; q_global = 0.00137)(GO:CC cell-substrate junction; q_global = 0.00155)(GO:BP vascular endothelial growth factor signaling pathway; q_global = 0.00418)(GO:BP heterotypic cell-cell adhesion; q_global = 0.0073)(GO:BP wound healing, spreading of cells; q_global = 0.0073)(KEGG Cell adhesion molecule (CAM) interaction - Homo sapiens (human); q_global = 0.00934)(GO:CC integrin complex; q_global = 0.0271)(KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0448). Established functions include heterodimeric cell-surface adhesion and signaling, angiogenesis, vasculogenesis, cell-matrix adhesion, and regulation of intracellular calcium. HPA associates it with podocytes and urothelial cells and detects it in kidney. Its cardiovascular and thrombotic disease associations add biological relevance.
- **Conclusion**: Established evidence supports ITGAV as a matrix-contact and signaling anchor connecting kidney and vascular biology. The module does not identify which ITGAV heterodimer or ligand is responsible.

#### ITGB3

- **Related proteins** (co-abundance neighbors): CDH2 (0.88), MCAM (0.85), GPD2 (0.83); STRING partners: CD44 (0.838), ITGA5 (0.999), ITGAV (0.999)
- **HPA**: Tissue enhanced; Cell type enriched; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 3. The ITGB3 protein product is the integrin beta chain beta 3. Integrins are integral cell-surface proteins composed of an alpha chain and a beta chain. A given chain may combine with multiple partners resulting in different integrins. Integrin beta 3 is found along with the alpha IIb chain in platelets. Integrins are known to participate in cell adhesion as well as cell-surface mediated signalling.…
- **Diseases (Open Targets)**: Glanzmann thrombasthenia 1 (0.839); Glanzmann thrombasthenia (0.746); bleeding disorder, platelet-type, 24 (0.705); autosomal dominant macrothrombocytopenia (0.635); cancer (0.619)
- **Europe PMC papers**: 7392
- **Why important**: ITGB3 is part of the integrin machinery and has STRING relationships with CD44, ITGA5, and ITGAV. It recurs across primary membrane, receptor, adhesion, vascular, wound-healing, integrin-complex, and ECM-receptor terms (GO:CC cell surface; q_global = 4.82e-05)(GO:CC plasma membrane; q_global = 6.99e-05)(GO:MF signaling receptor activity; q_global = 8.11e-05)(GO:CC receptor complex; q_global = 0.00011)(GO:CC focal adhesion; q_global = 0.00137)(GO:BP vascular endothelial growth factor signaling pathway; q_global = 0.00418)(GO:BP wound healing, spreading of cells; q_global = 0.0073)(GO:BP cellular response to vascular endothelial growth factor stimulus; q_global = 0.0208)(GO:BP wound healing; q_global = 0.0233)(GO:CC integrin complex; q_global = 0.0271)(KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0448). Established functions include cell adhesion, cell-matrix adhesion, integrin signaling, angiogenesis, endothelial proliferation, and leukocyte migration. HPA links it to blood vessels and platelets as well as blood-cell populations, and its disease associations include platelet disorders.
- **Conclusion**: Established evidence supports ITGB3 as a key effector linking vascular adhesion, platelet biology, and tissue remodeling. Its blood and platelet associations make sample-composition effects especially important; cell-resolved data are needed to distinguish direct kidney biology from vascular or platelet contribution.

#### CDH2

- **Related proteins** (co-abundance neighbors): ALCAM (0.89), ITGB3 (0.88), MCAM (0.88), PVR (0.85), FAM3C (0.84), IGF2R (0.81); STRING partners: CD44 (0.84), ITGA5 (0.712)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cadherin 2. This gene encodes a classical cadherin and member of the cadherin superfamily. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein is proteolytically processed to generate a calcium-dependent cell adhesion molecule and glycoprotein. This protein plays a role in the establishment of left-right asymmetry, development of the nervous system and t…
- **Diseases (Open Targets)**: agenesis of corpus callosum, cardiac, ocular, and genital syndrome (0.809); arrhythmogenic right ventricular dysplasia, familial, 14 (0.583); Agenesis of corpus callosum (0.515); attention deficit-hyperactivity disorder 8 (0.505); aortic stenosis (0.481)
- **Europe PMC papers**: 35205
- **Why important**: CDH2 is a network hub connected to ALCAM, ITGB3, MCAM, PVR, FAM3C, and IGF2R. It appears in primary terms covering cell-cell adhesion, cell-substrate junctions, focal adhesion, tube development, cardiomyopathy-related annotation, and blood-vessel morphogenesis (GO:CC cell surface; q_global = 4.82e-05)(GO:BP heterophilic cell-cell adhesion; q_global = 0.00053)(GO:BP cell adhesion; q_global = 0.00086)(GO:CC focal adhesion; q_global = 0.00137)(GO:CC cell-substrate junction; q_global = 0.00155)(GO:BP cell-cell adhesion; q_global = 0.00458)(GO:CC anchoring junction; q_global = 0.00676)(KEGG Cell adhesion molecule (CAM) interaction - Homo sapiens (human); q_global = 0.00934)(GO:BP tube development; q_global = 0.0127)(KEGG Arrhythmogenic right ventricular cardiomyopathy - Homo sapiens (human); q_global = 0.0208)(GO:BP tube morphogenesis; q_global = 0.023)(GO:BP blood vessel morphogenesis; q_global = 0.0354). Its established function is calcium-dependent cell-cell adhesion and junction assembly. HPA shows heart-muscle enhancement, blood-cell group enrichment for basophils and neutrophils, and kidney protein detection. It has extensive literature and disease associations involving cardiac, ocular, genital, and neurodevelopmental disorders.
- **Conclusion**: Established evidence supports CDH2 as a cell-cell-junction component connecting tissue architecture with vascular, cardiac, and epithelial adhesion biology. Its cooperation with the integrin-centered program is a plausible hypothesis rather than a demonstrated mechanism.

#### AXL

- **Related proteins** (co-abundance neighbors): FAM3C (0.93), CALU (0.92), CD44 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: AXL receptor tyrosine kinase. The protein encoded by this gene is a member of the Tyro3-Axl-Mer (TAM) receptor tyrosine kinase subfamily. The encoded protein possesses an extracellular domain which is composed of two immunoglobulin-like motifs at the N-terminal, followed by two fibronectin type-III motifs. It transduces signals from the extracellular matrix into the cytoplasm by binding to the vitamin K-dependent protein growt…
- **Diseases (Open Targets)**: acute myeloid leukemia (0.596); neurodegenerative disease (0.567); Alzheimer disease (0.536); Parkinson disease (0.528); lysosomal storage disease (0.526)
- **Europe PMC papers**: 17119
- **Why important**: AXL is a membrane receptor tyrosine kinase connected to FAM3C, CALU, and CD44 in the co-abundance network. It contributes to primary receptor, molecular-transducer, vascular endothelial growth factor-response, wound-healing, and receptor-kinase terms (GO:CC cell surface; q_global = 4.82e-05)(GO:MF signaling receptor activity; q_global = 8.11e-05)(GO:MF molecular transducer activity; q_global = 8.11e-05)(GO:BP cell adhesion; q_global = 0.00086)(GO:BP vascular endothelial growth factor signaling pathway; q_global = 0.00418)(GO:BP cellular response to vascular endothelial growth factor stimulus; q_global = 0.0208)(GO:BP wound healing; q_global = 0.0233)(GO:MF transmembrane receptor protein tyrosine kinase activity; q_global = 0.0388)(GO:MF transmembrane receptor protein kinase activity; q_global = 0.0388). Established functions include TAM-family signaling, growth-arrest-specific-six binding, phagocytosis, cytokine regulation, and receptor-mediated signal transduction. HPA associates it with fibroblasts, stromal populations, natural-killer cells, and plasmacytoid dendritic cells and detects it in kidney. It has substantial literature and disease associations.
- **Conclusion**: Established evidence supports AXL as a signaling receptor that may connect adhesion and vascular remodeling to immune or stromal state. Its immune-stromal or repair-related role in this module is plausible but requires cell-type-resolved and perturbational validation.

## Module 11

**Tissue pair**: circulatory_system and kidney  
**Genes (7)**: BCL10, NR3C1, MYO1B, NCOR2, PARD3, RIPK2, SPATS2

### Function

The strongest functional interpretation is an immune and inflammatory signaling module centered on CARD-domain biology. The globally corrected enrichment (GO:MF CARD domain binding; q_global = 0.0224) identifies CARD domain binding through RIPK2 and BCL10, supporting an innate or adaptive immune signaling role involving NF-kappaB activation, cytokine production, apoptosis, and inflammatory responses. RIPK2 is the network hub and connects the CARD-associated genes with NR3C1, PARD3, and NCOR2. The supplementary STRING term (STRING KEGG Neuroactive ligand-receptor interaction; within-query FDR = 0.0337) links NR3C1 and PARD3 to neuroactive ligand-receptor interaction, but this is not global enrichment evidence and should not define the module. The remaining genes suggest additional regulatory layers involving glucocorticoid-responsive transcription, chromatin repression, cell polarity, actin organization, vesicle trafficking, and RNA binding. Because only the CARD-domain term passed global correction, the broader interpretation remains integrative rather than a claim that all these processes form one established pathway.

**Cell composition.** This is not a plasma or secreted-protein module: none of the genes is annotated as secreted. The genes are generally low in tissue specificity, so the shared circulatory-system and kidney signal is unlikely to represent a tightly tissue-restricted program. HPA single-cell evidence shows cell-type enhancement for most genes, but across diverse cell types including podocytes, basophils, myonuclei, endometrial cells, esophageal apical cells, plasma cells, and hepatocytes. Blood-cell evidence is mixed, with mostly low immune-cell specificity, one immune-cell-enhanced gene, one immune-cell-enriched gene, and one gene not detected in immune cells. Thus, the module may partly reflect shared immune or stromal cell populations in the samples, or a broadly distributed cellular stress and signaling state, rather than a uniform kidney-specific or blood-specific program. Protein detection in kidney is present for most genes, whereas there is no matching HPA tissue result for circulatory_system; this supports caution when assigning the module to a specific tissue compartment.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF CARD domain binding | 0.0224 | BCL10, RIPK2 |

### STRING and hu.MAP

The only high-confidence STRING relationship among module genes is NCOR2–NR3C1. This is biologically coherent because NCOR2 is a nuclear receptor corepressor and NR3C1 is the glucocorticoid receptor, so the pair supports a known transcriptional regulatory connection. No other module pair is reported as a high-confidence STRING interaction, including the CARD-related RIPK2–BCL10 association. Therefore, the co-abundance edges should not be interpreted as a pre-existing physical complex. No hu.MAP complex contains multiple module members. Overall, the module combines one established transcriptional interaction with a globally supported CARD-domain functional signal, but most of its network structure is not corroborated by the listed physical-interaction or complex resources.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: NCOR2–NR3C1 (0.907)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Neuroactive ligand-receptor interaction (FDR = 0.0337, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared co-abundance pattern may be a new systems-level observation, because the module connects CARD signaling, glucocorticoid transcriptional regulation, cell polarity, and cytoskeletal or vesicle processes without a matching hu.MAP complex and with only one reported high-confidence STRING pair. However, novelty cannot be established solely from the absence of STRING or hu.MAP support. The individual genes and several of their functions are well established, especially RIPK2, BCL10, NR3C1, and NCOR2. The defensible conclusion is that the cross-tissue co-abundance arrangement is potentially novel and hypothesis-generating, while the underlying molecular functions are not new discoveries.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of inflammatory signaling by tissue or circulating-cell composition together with glucocorticoid-dependent transcriptional control. In this model, RIPK2 and BCL10 provide CARD-associated immune signaling, NR3C1 and NCOR2 modulate the transcriptional response to glucocorticoids, and PARD3 with MYO1B links the response to polarized cell architecture, membrane organization, and vesicle movement. SPATS2 may represent a less characterized RNA-associated component of the same co-abundance state. This model predicts that the module will be strongest in samples containing relevant immune, epithelial, endothelial, or podocyte-associated cell populations and during inflammatory or glucocorticoid-responsive states. The prediction is a hypothesis; the fact sheet does not establish direct physical coupling among all members.

### Important genes

#### RIPK2

- **Related proteins** (co-abundance neighbors): NR3C1 (0.90), NCOR2 (0.84), PARD3 (0.84), BCL10 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: receptor interacting serine/threonine kinase 2. This gene encodes a member of the receptor-interacting protein (RIP) family of serine/threonine protein kinases. The encoded protein contains a C-terminal caspase activation and recruitment domain (CARD), and is a component of signaling complexes in both the innate and adaptive immune pathways. It is a potent activator of NF-kappaB and inducer of apoptosis in response to various stimuli. [provided…
- **Diseases (Open Targets)**: leprosy (0.459); Abnormality of the skeletal system (0.364); Crohn disease (0.355); neurodegenerative disease (0.344); Precordial pain (0.294)
- **Europe PMC papers**: 3294
- **Why important**: RIPK2 is the network hub, with the greatest connectivity and weighted strength in the module. It is one of the two genes in the globally corrected CARD domain binding term (GO:MF CARD domain binding; q_global = 0.0224), and its annotated functions include cytokine production, adaptive immune response, apoptosis, inflammatory response, and NF-kappaB activation. It also has substantial literature and disease associations including Crohn disease, leprosy, and neurodegenerative disease.
- **Conclusion**: Established evidence supports RIPK2 as the principal immune-signaling anchor of the module. Its hub position makes it the strongest candidate for organizing the co-abundance pattern, but the network does not prove that RIPK2 physically interacts with every connected gene. A role as the central driver of the entire cross-tissue module remains a hypothesis.

#### BCL10

- **Related proteins** (co-abundance neighbors): RIPK2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BCL10 immune signaling adaptor. This gene was identified by its translocation in a case of mucosa-associated lymphoid tissue (MALT) lymphoma. The protein encoded by this gene contains a caspase recruitment domain (CARD), and has been shown to induce apoptosis and to activate NF-kappaB. This protein is reported to interact with other CARD domain containing proteins including CARD9, 10, 11 and 14, which are thought to function as …
- **Diseases (Open Targets)**: immunodeficiency 37 (0.661); MALT lymphoma (0.562); testicular germ cell tumor (0.505); follicular lymphoma (0.498); diffuse large B-cell lymphoma (0.465)
- **Europe PMC papers**: 3836
- **Why important**: BCL10 is the other member of the globally corrected CARD domain binding term (GO:MF CARD domain binding; q_global = 0.0224). It is an immune signaling adaptor associated with NF-kappaB activation, cytokine production, adaptive immune response, apoptosis, and Toll-like receptor signaling. Its disease associations include immunodeficiency and MALT lymphoma, and it has substantial literature. Its direct module edge to RIPK2 gives it functional relevance despite limited network connectivity.
- **Conclusion**: Established evidence supports BCL10 as an immune and CARD-associated component that reinforces the interpretation anchored by RIPK2. The co-abundance relationship with RIPK2 is consistent with coordinated immune signaling, but the fact sheet does not establish a direct RIPK2–BCL10 physical interaction in this module.

#### NR3C1

- **Related proteins** (co-abundance neighbors): RIPK2 (0.90), SPATS2 (0.83); STRING partners: NCOR2 (0.907)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nuclear receptor subfamily 3 group C member 1. This gene encodes glucocorticoid receptor, which can function both as a transcription factor that binds to glucocorticoid response elements in the promoters of glucocorticoid responsive genes to activate their transcription, and as a regulator of other transcription factors. This receptor is typically found in the cytoplasm, but upon ligand binding, is transported into the nucleus. It is involved …
- **Diseases (Open Targets)**: glucocorticoid resistance (0.809); chronic obstructive pulmonary disease (0.711); rheumatoid arthritis (0.639); asthma (0.634); atopic eczema (0.626)
- **Europe PMC papers**: 35847
- **Why important**: NR3C1 encodes the glucocorticoid receptor and has the largest literature volume among the module genes. It occupies an internal network position, connects to RIPK2 and SPATS2, and has the high-confidence STRING relationship with NCOR2. Its functions include glucocorticoid-responsive transcription and regulation of inflammatory responses, with disease associations including glucocorticoid resistance, rheumatoid arthritis, asthma, and atopic eczema.
- **Conclusion**: Established evidence supports NR3C1 as a transcriptional and anti-inflammatory regulatory component, and the STRING relationship with NCOR2 is known evidence. Its connection to the CARD-centered portion suggests possible coordination between glucocorticoid regulation and immune signaling, but that cross-pathway coordination is a hypothesis rather than an established mechanism here.

#### PARD3

- **Related proteins** (co-abundance neighbors): RIPK2 (0.84), MYO1B (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Cell Junctions; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: par-3 family cell polarity regulator. This gene encodes a member of the PARD protein family. PARD family members interact with other PARD family members and other proteins; they affect asymmetrical cell division and direct polarized cell growth. Multiple alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Oct 2011].
- **Diseases (Open Targets)**: spina bifida (0.596); neurodegenerative disease (0.526); Abnormality of the skeletal system (0.515); neural tube defect (0.484); alcohol drinking (0.419)
- **Europe PMC papers**: 1607
- **Why important**: PARD3 connects the RIPK2-centered portion of the network to MYO1B and is localized at the plasma membrane and cell junctions. Its annotations support cell polarity, cell adhesion, membrane targeting, cytoskeletal organization, and axonogenesis. HPA data show enhancement in podocytes and esophageal apical cells, making it relevant to polarized epithelial or filtration-barrier biology. It is also included in the supplementary STRING enrichment (STRING KEGG Neuroactive ligand-receptor interaction; within-query FDR = 0.0337).
- **Conclusion**: Established evidence supports PARD3 as a polarity and junctional organizer that may explain why a signaling module is shared across tissue samples containing polarized cells. Its relationship to inflammatory signaling in this module is inferred from co-abundance and network placement, not demonstrated as a direct molecular mechanism.

#### NCOR2

- **Related proteins** (co-abundance neighbors): RIPK2 (0.84); STRING partners: NR3C1 (0.907)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Immune cell enhanced; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nuclear receptor corepressor 2. This gene encodes a nuclear receptor co-repressor that mediates transcriptional silencing of certain target genes. The encoded protein is a member of a family of thyroid hormone- and retinoic acid receptor-associated co-repressors. This protein acts as part of a multisubunit complex which includes histone deacetylases to modify chromatin structure that prevents basal transcriptional activity of ta…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.493); prostate adenocarcinoma (0.443); colorectal adenocarcinoma (0.412); smoking initiation (0.403); respiratory system disorder (0.398)
- **Europe PMC papers**: 3320
- **Why important**: NCOR2 is the partner of NR3C1 in the only high-confidence STRING interaction reported for the module. It is a nuclear receptor corepressor involved in transcriptional silencing and chromatin regulation, and it has disease associations including prostate adenocarcinoma, colorectal adenocarcinoma, and other disorders. Its position is peripheral in the co-abundance graph but mechanistically important because it can regulate the transcriptional output of glucocorticoid and other nuclear-receptor pathways.
- **Conclusion**: Established evidence supports NCOR2 as a transcriptional coregulator and as a known interaction partner of NR3C1. Its inclusion supports a glucocorticoid-responsive regulatory layer in the module, while any specific influence on RIPK2 or BCL10 signaling remains a hypothesis.

## Module 12

**Tissue pair**: circulatory_system and kidney  
**Genes (35)**: BCL9L, CAPRIN1, CBX5, CCDC9B, CDK13, CDK9, CEBPB, CIZ1, DPH5, POLD3, EDC4, EXOSC6, FBXO30, GRWD1, IGF2BP2, LARP4, MTCL2, NOLC1, NUP188, NUDCD3, OBI1, PAAF1, PUM3, RBM28, RBM34, RBM7, RNF25, RNASEH2A, RRS1, SUPT16H, SRA1, TCOF1, TPX2, TRIM27, VIRMA

### Function

The strongest interpretation is a conserved nuclear gene-expression and RNA-processing module. The globally corrected GO evidence supports macromolecule and nucleic-acid metabolism, RNA binding, membraneless-organellar biology, macromolecule biosynthesis, gene expression, and primary metabolism (9 globally significant GO/KEGG terms, q_global 0.0045–0.0475; see the table). The concentration of nucleolar, nuclear-speckle, nucleoplasmic, and cytosolic RNA regulators is consistent with coordinated control of transcription, RNA maturation, RNA surveillance, translation, and ribosome biogenesis. Specific components support transcriptional elongation and chromatin control, including CDK9, CDK13, SUPT16H, CBX5, and CEBPB; RNA processing and decay, including EXOSC6, RBM7, EDC4, VIRMA, CAPRIN1, and LARP4; and nucleolar or ribosome-related processes, including TCOF1, NOLC1, RRS1, RBM28, RBM34, PUM3, and GRWD1. The module is therefore better described as a broad nuclear RNA and biosynthetic-support program than as a narrowly specialized kidney or circulatory pathway. The enrichment does not by itself establish that every gene participates in one physical complex or that the module has a single biochemical reaction.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary identifies only MTCL2 as secreted to blood, while most members have intracellular nuclear, nucleolar, cytosolic, or related localizations. The module is broadly expressed according to HPA, with most genes showing low tissue specificity, and it has low immune-cell specificity for most members. Thus, a simple explanation based on plasma carryover or a dominant blood-cell signature is not supported. A minority of genes show tissue or cell-type enhancement in brain, bone marrow, skeletal muscle, cardiomyocytes, choroid plexus, myonuclei, erythrocyte progenitors, or selected immune cells, so shared cellular composition or common proliferative and biosynthetic states could contribute to the circulatory-system and kidney signal. Kidney protein detection is widespread among the listed genes, but this is compatible with a general intracellular housekeeping and RNA-biology program rather than a kidney-specific secretory program.

**GO/KEGG enrichment**: 9 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP macromolecule metabolic process | 0.0045 | BCL9L, CAPRIN1, CBX5, CDK13, CDK9, CEBPB, CIZ1, DPH5, EDC4, EXOSC6, FBXO30, GRWD1, IGF2BP2, LARP4, NOLC1, NUDCD3, OBI1, PAAF1, POLD3, PUM3, RBM28, RBM34, RBM7, RNASEH2A, RNF25, RRS1, SRA1, SUPT16H, TCOF1, TPX2, TRIM27, VIRMA |
| GO:BP nucleic acid metabolic process | 0.00524 | BCL9L, CAPRIN1, CBX5, CDK13, CDK9, CEBPB, CIZ1, EDC4, EXOSC6, GRWD1, IGF2BP2, NOLC1, OBI1, PAAF1, POLD3, RBM28, RBM34, RBM7, RNASEH2A, RRS1, SRA1, SUPT16H, TCOF1, TRIM27, VIRMA |
| GO:MF RNA binding | 0.00974 | CAPRIN1, CCDC9B, CDK13, CDK9, EXOSC6, GRWD1, IGF2BP2, LARP4, NOLC1, PUM3, RBM28, RBM34, RBM7, RNASEH2A, RRS1, SRA1, SUPT16H, TCOF1, VIRMA |
| GO:MF nucleic acid binding | 0.015 | CAPRIN1, CCDC9B, CDK13, CDK9, CEBPB, CIZ1, EXOSC6, GRWD1, IGF2BP2, LARP4, NOLC1, PUM3, RBM28, RBM34, RBM7, RNASEH2A, RRS1, SRA1, SUPT16H, TCOF1, TRIM27, VIRMA |
| GO:CC membraneless organelle | 0.0154 | BCL9L, CAPRIN1, CBX5, CDK13, CDK9, CEBPB, EDC4, EXOSC6, GRWD1, IGF2BP2, LARP4, MTCL2, NOLC1, NUDCD3, OBI1, PAAF1, POLD3, PUM3, RBM28, RBM34, RNF25, RRS1, SRA1, SUPT16H, TCOF1, TPX2, TRIM27, VIRMA |
| GO:CC intracellular membraneless organelle | 0.0154 | BCL9L, CAPRIN1, CBX5, CDK13, CDK9, CEBPB, EDC4, EXOSC6, GRWD1, IGF2BP2, LARP4, MTCL2, NOLC1, NUDCD3, OBI1, PAAF1, POLD3, PUM3, RBM28, RBM34, RNF25, RRS1, SRA1, SUPT16H, TCOF1, TPX2, TRIM27, VIRMA |
| GO:BP macromolecule biosynthetic process | 0.0215 | BCL9L, CAPRIN1, CBX5, CDK13, CDK9, CEBPB, CIZ1, EDC4, EXOSC6, FBXO30, IGF2BP2, LARP4, NOLC1, NUDCD3, PAAF1, POLD3, PUM3, RBM28, RBM34, RBM7, RNF25, RRS1, SRA1, SUPT16H, TCOF1, TRIM27, VIRMA |
| GO:BP gene expression | 0.0301 | BCL9L, CAPRIN1, CBX5, CDK13, CDK9, CEBPB, CIZ1, EDC4, EXOSC6, FBXO30, IGF2BP2, LARP4, NOLC1, NUDCD3, PAAF1, PUM3, RBM28, RBM34, RBM7, RNF25, RRS1, SRA1, SUPT16H, TCOF1, TRIM27, VIRMA |
| GO:BP primary metabolic process | 0.0475 | BCL9L, CAPRIN1, CBX5, CDK13, CDK9, CEBPB, CIZ1, DPH5, EDC4, EXOSC6, FBXO30, GRWD1, IGF2BP2, LARP4, MTCL2, NOLC1, NUDCD3, OBI1, PAAF1, POLD3, PUM3, RBM28, RBM34, RBM7, RNASEH2A, RNF25, RRS1, SRA1, SUPT16H, TCOF1, TPX2, TRIM27, VIRMA |

### STRING and hu.MAP

STRING provides supplementary functional convergence for nucleic-acid binding, RNA binding, nuclear or nucleolar localization, and ubiquitin-related biology (7 supplementary STRING terms; within-query FDR 0.0048–0.048). Its high-confidence pairwise evidence is concentrated in several coherent groups: the CDK13–CDK9 and CDK9–SUPT16H transcriptional cluster; the EXOSC6–RBM7 RNA-exosome relationship; and a nucleolar RNA-processing group involving GRWD1, PUM3, RBM28, RBM34, RRS1, and NOLC1. STRING also links IGF2BP2 with VIRMA, supporting an RNA-modification or RNA-regulatory connection. hu.MAP independently places EXOSC6 and RBM7 in an exosome-related complex (hu.MAP huMAP3_05382.1), TCOF1 and NOLC1 together in more than one complex (hu.MAP huMAP3_13072.1) (hu.MAP huMAP3_11931.1), and NOLC1 with VIRMA in a larger RNA-processing-associated complex (hu.MAP huMAP3_09943.1). FBXO30 and CIZ1 occur together in another complex (hu.MAP huMAP3_12566.1). These observations show that parts of the co-abundance module recover known molecular relationships, especially RNA surveillance, nucleolar organization, and transcriptional regulation. They do not demonstrate that the entire module is one physical complex, because many module members lack recorded STRING partners or hu.MAP complex assignments.

**STRING interactions (score >= 0.7)**: 16 of 595 gene pairs: CDK13–CDK9 (0.867); CDK9–SUPT16H (0.894); EXOSC6–RBM7 (0.824); GRWD1–PUM3 (0.914); GRWD1–RBM28 (0.873); GRWD1–RRS1 (0.926); IGF2BP2–VIRMA (0.865); NOLC1–RBM28 (0.729); NOLC1–RRS1 (0.806); NOLC1–TCOF1 (0.853); PUM3–RBM28 (0.972); PUM3–RBM34 (0.873); PUM3–RRS1 (0.962); RBM28–RBM34 (0.975); RBM28–RRS1 (0.915); RBM34–RRS1 (0.802)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Nucleic acid binding (FDR = 0.0048, 22 genes); Function RNA binding (FDR = 0.0048, 19 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0076, 18 genes); Keyword Nucleus (FDR = 0.0077, 25 genes); Keyword Ubl conjugation (FDR = 0.0127, 17 genes); COMPARTMENTS Nucleus (FDR = 0.048, 25 genes); COMPARTMENTS Nucleolus (FDR = 0.048, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13072.1 (TCOF1, NOLC1; 2/3); huMAP3_05382.1 (EXOSC6, RBM7; 2/18); huMAP3_11931.1 (TCOF1, NOLC1; 2/19); huMAP3_12566.1 (FBXO30, CIZ1; 2/51); huMAP3_09943.1 (NOLC1, VIRMA; 2/78)

### Novelty

The module should not be claimed as a wholly new molecular complex. Several of its internal relationships and functional groupings are already represented by STRING and hu.MAP, particularly the RNA exosome, nucleolar ribosome-biogenesis, transcriptional-elongation, and RNA-modification connections. Nevertheless, the conserved co-abundance configuration across circulatory_system and kidney may still be a potentially novel systems-level observation: the databases document many pairwise or complex relationships, but they do not by themselves establish this particular tissue-pair module, its connectivity pattern, or its coordinated abundance across the two tissues. Novelty is therefore best framed as a new cross-tissue network-level association requiring independent replication, rather than as discovery of previously unknown gene functions or physical interactions. Database absence for genes such as CCDC9B or RNF25 is evidence of limited prior annotation, not proof that their relationships in this module are novel.

**Hypothesis.** Hypothesis: the module represents a shared cellular state in which transcriptional output, RNA processing and degradation, nucleolar ribosome production, translation control, and proteostasis are coordinated. A plausible mechanism is that CDK9, CDK13, and SUPT16H support transcriptional elongation and chromatin access; VIRMA, IGF2BP2, CAPRIN1, LARP4, and EDC4 regulate RNA maturation, stability, translation, or decay; and the NOLC1–TCOF1–RRS1–RBM28–RBM34–PUM3 axis supports nucleolar RNA and ribosome-related activity. RNF25, TRIM27, OBI1, and FBXO30 could connect this program to ubiquitin-dependent regulation, while EXOSC6–RBM7 could provide RNA surveillance. In kidney and circulatory-system samples, coordinated abundance of these intracellular factors may reflect a shared biosynthetic, stress-response, or proliferative state, or shared cellular subpopulations, rather than a tissue-specific pathway. This remains a hypothesis and should be tested with cell-resolved expression, perturbation, and interaction assays.

### Important genes

#### RNF25

- **Related proteins** (co-abundance neighbors): PAAF1 (0.92), NUDCD3 (0.89), CDK13 (0.86), SRA1 (0.86), VIRMA (0.84), RBM7 (0.82), CAPRIN1 (0.82), EXOSC6 (0.81), POLD3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ring finger protein 25. The protein encoded by this gene contains a RING finger motif. The mouse counterpart of this protein has been shown to interact with Rela, the p65 subunit of NF-kappaB (NFKB), and modulate NFKB-mediated transcription activity. The mouse protein also binds ubiquitin-conjugating enzymes (E2s) and is a substrate for E2-dependent ubiquitination. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: Bjornstad syndrome (0.557); GRACILE syndrome (0.556); mitochondrial complex III deficiency nuclear type 1 (0.531); Joubert syndrome and related disorders (0.495); hereditary disease (0.464)
- **Europe PMC papers**: 207
- **Why important**: RNF25 is the strongest network-connected member in the supplied subgraph and links PAAF1, NUDCD3, CDK13, SRA1, VIRMA, RBM7, CAPRIN1, and EXOSC6. It is present in most globally corrected cellular and biosynthetic terms (GO:BP macromolecule metabolic process; q_global = 0.0045) (GO:CC membraneless organelle; q_global = 0.0154)–(GO:BP primary metabolic process; q_global = 0.0475) and in the supplementary ubiquitin and nuclear terms (STRING Keyword Ubl conjugation; within-query FDR = 0.0127) (STRING COMPARTMENTS Nucleus; within-query FDR = 0.048). Its annotated RING-finger activity, interaction with the NF-kappaB subunit Rela in mouse, and links to ubiquitin-conjugating enzymes provide a plausible regulatory bridge between RNA biology, transcription, and proteostasis. It also has a substantial literature and multiple disease associations, although these associations do not establish a role in this module.
- **Conclusion**: Established evidence supports RNF25 as a central co-abundance connector with ubiquitin-related and nuclear regulatory annotation. Its exact molecular role in this human tissue-pair module is unresolved. A testable hypothesis is that RNF25 helps couple RNA-processing or transcriptional factors to ubiquitin-dependent regulation.

#### CDK13

- **Related proteins** (co-abundance neighbors): PAAF1 (0.88), RNF25 (0.86); STRING partners: CDK9 (0.867)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cyclin dependent kinase 13. The protein encoded by this gene is a member of the cyclin-dependent serine/threonine protein kinase family. Members of this family are well known for their essential roles as master switches in cell cycle control. The exact function of this protein has not yet been determined, but it may play a role in mRNA processing and may be involved in regulation of hematopoiesis. Alternatively spliced trans…
- **Diseases (Open Targets)**: congenital heart defects, dysmorphic facial features, and intellectual developmental disorder (0.812); hereditary disease (0.546); neurodegenerative disease (0.526); Global developmental delay (0.458); syndromic intellectual disability (0.406)
- **Europe PMC papers**: 1167
- **Why important**: CDK13 is connected to RNF25 and PAAF1 in the module and has a high-confidence STRING relationship with CDK9. It appears in every globally corrected term (9 globally significant GO/KEGG terms, q_global 0.0045–0.0475; see the table) and in several supplementary nuclear and nucleic-acid categories (6 supplementary STRING terms; within-query FDR 0.0048–0.048). Its annotation supports RNA processing, transcriptional elongation, transcriptional regulation, hematopoiesis, and cell-cycle regulation, making it a mechanistically informative link between gene expression and cellular state. Its developmental and neurodevelopmental disease associations and substantial literature indicate that it is biologically consequential rather than merely a generic marker.
- **Conclusion**: Established evidence supports CDK13 as a transcriptional and RNA-processing regulator that fits the module function. The module data do not establish whether altered CDK13 activity drives the shared tissue signal or merely covaries with it.

#### RBM28

- **Related proteins** (co-abundance neighbors): CAPRIN1 (0.85), PUM3 (0.83), TPX2 (0.81); STRING partners: GRWD1 (0.873), NOLC1 (0.729), PUM3 (0.972), RBM34 (0.975), RRS1 (0.915)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 28. The protein encoded by this gene is a specific nucleolar component of the spliceosomal small nuclear ribonucleoprotein (snRNP)complexes . It specifically associates with U1, U2, U4, U5, and U6 small nuclear RNAs (snRNAs), possibly coordinating their transition through the nucleolus. Mutation in this gene causes alopecia, progressive neurological defects, and endocrinopathy (ANE syndrome), a pleiot…
- **Diseases (Open Targets)**: ANE syndrome (0.643); neurodegenerative disease (0.472); microcephaly (0.111); cancer (0.076); colorectal carcinoma (0.075)
- **Europe PMC papers**: 337
- **Why important**: RBM28 is embedded in the nucleolar RNA-processing core: STRING connects it strongly with PUM3, RBM34, RRS1, and GRWD1, while the module places it near CAPRIN1 and TPX2. It occurs in every globally corrected term (9 globally significant GO/KEGG terms, q_global 0.0045–0.0475; see the table) and every listed STRING functional category (7 supplementary STRING terms; within-query FDR 0.0048–0.048). Its annotated role in spliceosomal small nuclear ribonucleoprotein biology and its association with ANE syndrome provide direct functional and disease relevance. Its nucleolar localization and broad literature make it a strong representative of the module’s RNA-processing component.
- **Conclusion**: Established evidence supports RBM28 as a nucleolar RNA-processing component and a core connector within the known RNA-related subnetwork. The co-abundance data support coordinated regulation with neighboring factors but do not prove a new RBM28-containing complex.

#### TCOF1

- **Related proteins** (co-abundance neighbors): CCDC9B (0.86), CEBPB (0.82); STRING partners: NOLC1 (0.853)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_13072.1, huMAP3_11931.1
- **Function (MyGene.info)**: treacle ribosome biogenesis factor 1. This gene encodes a nucleolar protein with a LIS1 homology domain. The protein is involved in ribosomal DNA gene transcription through its interaction with upstream binding factor (UBF). Mutations in this gene have been associated with Treacher Collins syndrome, a disorder which includes abnormal craniofacial development. Multiple transcript variants encoding different isoforms have been found for…
- **Diseases (Open Targets)**: Treacher Collins syndrome 1 (0.761); Treacher-Collins syndrome (0.713); hereditary disease (0.472); neurodegenerative disease (0.459); Emery-Dreifuss muscular dystrophy 4, autosomal dominant (0.266)
- **Europe PMC papers**: 1248
- **Why important**: TCOF1 connects CCDC9B and CEBPB in the co-abundance graph, has a high-confidence STRING relationship with NOLC1, and occurs in two hu.MAP complexes with NOLC1 (hu.MAP huMAP3_13072.1) (hu.MAP huMAP3_11931.1). It is represented across all globally corrected terms (9 globally significant GO/KEGG terms, q_global 0.0045–0.0475; see the table) and all supplementary STRING categories (7 supplementary STRING terms; within-query FDR 0.0048–0.048). Its established functions in ribosome biogenesis, ribosomal DNA transcription, translation regulation, and neural crest development make it a strong mechanistic anchor for the nucleolar and biosynthetic interpretation. Its association with Treacher Collins syndrome and extensive literature further support its biological importance.
- **Conclusion**: Established evidence supports TCOF1 as a nucleolar ribosome-biogenesis and transcriptional regulator that helps explain the module’s biosynthetic signature. The module suggests coordinated activity with NOLC1 and CEBPB, but it does not establish tissue-specific causality.

#### NOLC1

- **Related proteins** (co-abundance neighbors): MTCL2 (0.81); STRING partners: RBM28 (0.729), RRS1 (0.806), TCOF1 (0.853)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13072.1, huMAP3_11931.1, huMAP3_09943.1
- **Function (MyGene.info)**: nucleolar and coiled-body phosphoprotein 1. Enables protein heterodimerization activity and protein-macromolecule adaptor activity. Involved in neural crest cell development; neural crest formation; and regulation of translation. Located in fibrillar center. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: uterine corpus leiomyoma (0.278); Menorrhagia (0.187); neoplasm (0.091); hepatocellular carcinoma (0.085); colorectal cancer (0.084)
- **Europe PMC papers**: 1092
- **Why important**: NOLC1 is a nucleolar component connected in STRING with RBM28, RRS1, and TCOF1, and it participates with TCOF1 in multiple hu.MAP complexes (hu.MAP huMAP3_13072.1) (hu.MAP huMAP3_11931.1) and with VIRMA in another (hu.MAP huMAP3_09943.1). It occurs in every globally corrected term (9 globally significant GO/KEGG terms, q_global 0.0045–0.0475; see the table) and all supplementary STRING categories (7 supplementary STRING terms; within-query FDR 0.0048–0.048). Its annotations in rRNA processing, regulation of translation, ribosome biogenesis, and nucleolar organization make it a direct bridge between the module’s enrichment signal and a concrete cellular process. Its disease and cancer associations and substantial literature add further evidence of functional relevance.
- **Conclusion**: Established evidence supports NOLC1 as a nucleolar and ribosome-biogenesis component that is central to the module’s interpretation. Its coordinated abundance with TCOF1, RRS1, and RNA-binding proteins is consistent with an integrated nucleolar program, but the module does not prove that NOLC1 is the driver.

#### CCDC9B

- **Related proteins** (co-abundance neighbors): SUPT16H (0.90), IGF2BP2 (0.89), CDK9 (0.88), POLD3 (0.87), BCL9L (0.87), TCOF1 (0.86), EDC4 (0.85), CBX5 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coiled-coil domain containing 9B. Enables RNA binding activity. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.338); diabetes mellitus (0.260); liver disorder (0.219); diverticular disease (0.058); intelligence (0.040)
- **Europe PMC papers**: 47
- **Why important**: CCDC9B has one of the strongest network positions in the supplied graph, connecting SUPT16H, IGF2BP2, CDK9, POLD3, BCL9L, TCOF1, EDC4, and CBX5. It is supported by the globally corrected RNA-binding terms (GO:MF RNA binding; q_global = 0.00974) (GO:MF nucleic acid binding; q_global = 0.015) and the corresponding STRING categories (STRING Function Nucleic acid binding; within-query FDR = 0.0048) (STRING Function RNA binding; within-query FDR = 0.0048). HPA describes skeletal-muscle enhancement and enhancement in cardiomyocytes, myonuclei, megakaryocytes, and other cell types, with kidney protein detection and no immune-cell detection. Its direct annotation is limited to RNA binding and its literature volume is comparatively small, so it is especially valuable as a network-level connector but should not be assigned a more specific function without experiments.
- **Conclusion**: Established evidence supports CCDC9B as a highly connected, intracellular RNA-associated member with tissue and cell-type context relevant to the shared module. Its precise biochemical role and whether it organizes the observed subnetwork remain hypotheses.

## Module 13

**Tissue pair**: circulatory_system and kidney  
**Genes (9)**: BIRC6, GAPVD1, GIGYF2, KIFAP3, POLR1B, THADA, FTSJ1, USP19, UTP25

### Function

The strongest functional interpretation is an intracellular RNA maturation and translation-quality module centered on tRNA ribose methylation. The only globally corrected GO/KEGG evidence is (GO:BP tRNA nucleoside ribose methylation; q_global = 0.0144), linking FTSJ1 and THADA to tRNA nucleoside ribose methylation. FTSJ1 is a tRNA methyltransferase, while THADA is associated with the same methylation process and with regulation of endoplasmic-reticulum calcium, lipid homeostasis, and adaptive thermogenesis. The module also contains genes related to nucleolar RNA production and processing, protein turnover, translation control, vesicle transport, microtubule organization, and apoptosis. These additional functions are biologically coherent possibilities but are not globally significant enrichment results. The strong FTSJ1–THADA relationship and the absence of STRING functional enrichment indicate that the clearest signal is a specific RNA-modification relationship rather than a broad pathway annotation.

**Cell composition.** This does not look like a plasma-protein or secreted-protein module: none of the genes is annotated as secreted, and the encoded proteins are intracellular. The HPA profile shows low tissue specificity across the module, with kidney protein detection for most genes that have kidney data, but without a tissue-enriched pattern. Several genes are cell-type enhanced in spermatids or primary spermatocytes, and some are associated with platelets or basophils; however, most genes have low cell-type and immune-cell specificity. Thus, the shared circulatory-system and kidney signal is more plausibly a broadly expressed intracellular program, or a signal influenced by shared cellular composition, than a blood-plasma signature. The spermatid and platelet associations should be treated as contextual HPA observations rather than evidence that the module is a reproductive or platelet-specific program in these tissues.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP tRNA nucleoside ribose methylation | 0.0144 | FTSJ1, THADA |

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, FTSJ1–THADA, and no STRING functional enrichment. This relationship is concordant with the globally corrected GO term (GO:BP tRNA nucleoside ribose methylation; q_global = 0.0144) and with external structural evidence that human FTSJ1 and THADA form a tRNA methyltransferase complex involved in anticodon-loop ribose methylation. The remaining co-abundance relationships do not have corresponding high-confidence STRING pair evidence in the fact sheet, so they may represent co-regulation, indirect biology, shared cellular context, or relationships not captured by STRING. No hu.MAP complex contains multiple module members. Consequently, the module has one well-supported molecular core rather than evidence for a fully established multiprotein complex spanning all genes.

**STRING interactions (score >= 0.7)**: 1 of 36 gene pairs: FTSJ1–THADA (0.977)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The FTSJ1–THADA functional core is not a new molecular association: it is supported by STRING, the globally corrected GO result (GO:BP tRNA nucleoside ribose methylation; q_global = 0.0144), and recent structural and biochemical literature. The broader nine-gene co-abundance pattern may still be a new tissue-pair observation, because the fact sheet does not identify a previously described co-abundance module or a hu.MAP complex containing these genes. However, novelty cannot be claimed solely because most edges are absent from STRING or hu.MAP. The defensible conclusion is that the module-level observation may be novel as a cross-tissue co-abundance pattern, while its central biochemical relationship is established and its peripheral connections remain unvalidated.

**Hypothesis.** Hypothesis: in both circulatory-system and kidney samples, variation in a broadly expressed intracellular RNA-processing and proteostasis state brings the FTSJ1–THADA tRNA-modification machinery into co-abundance with nucleolar transcription and RNA-processing genes, translation-regulatory machinery, protein-quality-control factors, vesicle and microtubule transport components, and apoptosis regulators. FTSJ1–THADA-dependent tRNA modification could influence codon-sensitive translation and thereby couple RNA maturation to cellular stress, trafficking, and survival programs. This is a mechanistic hypothesis, not an established causal explanation for the tissue-pair module; the co-abundance data do not demonstrate physical interaction or directionality.

Web sources: https://www.nature.com/articles/s42003-025-08278-3; https://pmc.ncbi.nlm.nih.gov/articles/PMC12145424/; https://www.uniprot.org/uniprotkb/A8C750/entry; https://www.rcsb.org/structure/8Y2O

### Important genes

#### FTSJ1

- **Related proteins** (co-abundance neighbors): THADA (0.86), UTP25 (0.82), POLR1B (0.81), GIGYF2 (0.80); STRING partners: THADA (0.977)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FtsJ RNA 2'-O-methyltransferase 1. This gene encodes a member of the methyltransferase superfamily. The encoded protein localizes to the nucleolus, binds to S-adenosylmethionine, and may be involved in the processing and modification of ribosomal RNA. Mutations in this gene are associated with cognitive disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013].
- **Diseases (Open Targets)**: non-syndromic X-linked intellectual disability (0.712); hereditary disease (0.499); Intellectual disability (0.393); X-linked complex neurodevelopmental disorder (0.370); autism spectrum disorder (0.118)
- **Europe PMC papers**: 365
- **Why important**: FTSJ1 is the central network gene and one half of the only globally supported functional pair (GO:BP tRNA nucleoside ribose methylation; q_global = 0.0144). It is a tRNA ribose methyltransferase involved in tRNA modification, tRNA processing, and cytoplasmic translation, and it connects to THADA, UTP25, POLR1B, and GIGYF2 in the module. Its association with non-syndromic X-linked intellectual disability and its substantial literature support make it the clearest functional anchor. External structural work directly supports an FTSJ1–THADA methyltransferase complex.
- **Conclusion**: Established: FTSJ1 is a tRNA-modification enzyme, is implicated in the (GO:BP tRNA nucleoside ribose methylation; q_global = 0.0144) process, and forms a supported relationship with THADA. Hypothesis: its central position reflects coupling of tRNA modification to the wider intracellular RNA-processing state represented by this module, rather than proving that FTSJ1 drives the co-abundance pattern.

#### THADA

- **Related proteins** (co-abundance neighbors): FTSJ1 (0.86); STRING partners: FTSJ1 (0.977)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Immune cell enhanced; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: THADA armadillo repeat containing. This gene is the target of 2p21 choromosomal aberrations in benign thyroid adenomas. Single nucleotide polymorphisms (SNPs) in this gene may be associated with type 2 diabetes and polycystic ovary syndrome. The encoded protein is likely involved in the death receptor pathway and apoptosis. [provided by RefSeq, Sep 2016].
- **Diseases (Open Targets)**: prostate carcinoma (0.455); diabetes mellitus (0.404); type 2 diabetes mellitus (0.386); polycystic ovary syndrome (0.384); hypertensive disorder (0.381)
- **Europe PMC papers**: 1260
- **Why important**: THADA is the partner of FTSJ1 in the only STRING relationship and the only other gene in (GO:BP tRNA nucleoside ribose methylation; q_global = 0.0144). It is annotated with tRNA methylation as well as endoplasmic-reticulum calcium regulation, lipid homeostasis, and adaptive thermogenesis. It has substantial literature volume and disease associations involving diabetes, polycystic ovary syndrome, and hypertensive disorders, which broaden the possible physiological relevance of the module.
- **Conclusion**: Established: THADA is associated with the FTSJ1-dependent tRNA methylation process and has reported metabolic and cellular-stress-related functions. Hypothesis: THADA may connect RNA-modification capacity with metabolic or endoplasmic-reticulum state in the shared tissue samples, but the co-abundance data do not establish that link.

#### KIFAP3

- **Related proteins** (co-abundance neighbors): USP19 (0.86), UTP25 (0.81), BIRC6 (0.81), GAPVD1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules, Basal body; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin associated protein 3. The small G protein GDP dissociation stimulator (smg GDS) is a regulator protein having two activities on a group of small G proteins including the Rho and Rap1 family members and Ki-Ras; one is to stimulate their GDP/GTP exchange reactions, and the other is to inhibit their interactions with membranes. The protein encoded by this gene contains 9 'Armadillo' repeats and interacts with the smg GDS …
- **Diseases (Open Targets)**: neurodegenerative disease (0.528); atrial fibrillation (0.456); Abnormality of the skeletal system (0.419); venous thromboembolism (0.388); deep vein thrombosis (0.338)
- **Europe PMC papers**: 605
- **Why important**: KIFAP3 is a highly connected module member and is annotated in microtubule-based movement, transport along microtubules, cilium organization, and protein-containing complex assembly. It is cell-type enhanced in late spermatids and platelets in HPA and has disease associations including atrial fibrillation and venous thromboembolism. It has no reported STRING partner or globally supported enrichment term in this module, making it an informative peripheral-to-core connection rather than an established component of the FTSJ1–THADA complex.
- **Conclusion**: Established: KIFAP3 is an intracellular microtubule-associated transport factor with relevant transport and cilium annotations. Hypothesis: its co-abundance with the RNA-processing core may reflect coordinated trafficking or cell-structural state, but there is no direct evidence here that KIFAP3 physically interacts with FTSJ1 or THADA.

#### POLR1B

- **Related proteins** (co-abundance neighbors): FTSJ1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase I subunit B. Eukaryotic RNA polymerase I (pol I) is responsible for the transcription of ribosomal RNA (rRNA) genes and production of rRNA, the primary component of ribosomes. Pol I is a multisubunit enzyme composed of 6 to 14 polypeptides, depending on the species. Most of the mass of the pol I complex derives from the 2 largest subunits, Rpa1 and Rpa2 in yeast. POLR1B is homologous to Rpa2 (Seither and Grumm…
- **Diseases (Open Targets)**: Treacher Collins syndrome 4 (0.751); Treacher-Collins syndrome (0.383); arthropathy (0.212); Chronic Obstructive Asthma (0.188); lower respiratory tract disorder (0.124)
- **Europe PMC papers**: 521
- **Why important**: POLR1B links the module to nucleolar ribosomal-RNA transcription. It encodes a subunit of RNA polymerase I and is cell-type enhanced in early spermatids and late primary spermatocytes. Its disease associations include Treacher Collins syndrome, and its literature support is substantial. Its connection to FTSJ1 is a co-abundance relationship without corresponding STRING or hu.MAP support in the fact sheet.
- **Conclusion**: Established: POLR1B participates in RNA polymerase I transcription and ribosomal-RNA production. Hypothesis: its relationship with FTSJ1 may indicate coordinated regulation of ribosome production and tRNA modification, consistent with a broader translational-capacity state, but this coupling is not demonstrated by the available evidence.

#### BIRC6

- **Related proteins** (co-abundance neighbors): KIFAP3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Immune cell enriched; location Golgi apparatus, Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: baculoviral IAP repeat containing 6. This gene encodes a protein with a BIR (baculoviral inhibition of apoptosis protein repeat) domain and a UBCc (ubiquitin-conjugating enzyme E2, catalytic) domain. This protein inhibits apoptosis by facilitating the degradation of apoptotic proteins by ubiquitination. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: cancer (0.528); neurodegenerative disease (0.512); autism spectrum disorder (0.333); diffuse large B-cell lymphoma (0.314); epilepsy (0.298)
- **Europe PMC papers**: 1390
- **Why important**: BIRC6 contributes a protein-quality-control and cell-survival dimension. It contains apoptosis-inhibitory and ubiquitin-conjugating domains and is annotated in protein ubiquitination, apoptotic processes, cytokinesis, and regulation of cell proliferation. It is immune-cell enriched in basophils in HPA and has substantial literature volume with disease associations involving cancer, neurodegeneration, autism spectrum disorder, and epilepsy. Its module connection is to KIFAP3, not directly to the FTSJ1–THADA pair.
- **Conclusion**: Established: BIRC6 is involved in ubiquitin-dependent regulation of apoptotic proteins and cellular survival. Hypothesis: its co-abundance may report a shared proteostasis or survival state that accompanies RNA-processing variation in the samples, but the module does not establish a direct BIRC6 role in tRNA methylation.

## Module 14

**Tissue pair**: circulatory_system and kidney  
**Genes (26)**: BRD8, CDK12, COIL, DDX55, HAUS7, HPS6, KLC2, NCBP3, NCOA2, NUP205, ORC4, PM20D2, PRRC2A, PRRC2B, PRRC2C, GINS3, RBBP6, RBM15, SIRT1, SMG8, SRCAP, TAF6L, ZC3H7B, ZMYND8, ZNF451, ZNF598

### Function

The strongest functional interpretation is a broadly expressed nuclear gene-regulatory and RNA-processing module. The only GO/KEGG term passing global correction is nuclear lumen (GO:CC nuclear lumen; q_global = 0.0317), covering most module genes and supporting a shared nuclear localization rather than a narrowly defined pathway. The member annotations indicate several coordinated activities: chromatin remodeling and transcriptional regulation through SRCAP, BRD8, NCOA2, TAF6L, ZMYND8 and ZNF451; RNA processing, RNA export and RNA surveillance through NCBP3, DDX55, CDK12, RBM15, COIL, RBBP6 and SMG8; DNA replication or cell-cycle control through ORC4, GINS3 and HAUS7; and cytoplasmic translation or stress-response regulation through the PRRC2 proteins and ZNF598. Thus, the module is best viewed as a coordinated nuclear gene-expression and genome-maintenance program with links to translation quality control, rather than as evidence for one specific biochemical pathway. The STRING compartment terms (STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.0093) and (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0093) are concordant supplementary evidence, not additional globally corrected enrichment.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. It is also not strongly blood-cell specific, because the module is mostly low in immune-cell specificity and has no enriched blood-cell category in the summary. Most genes have low tissue specificity, which is compatible with a housekeeping-like nuclear program expressed across tissues. Kidney protein detection is widespread among the genes with available HPA measurements, whereas circulatory-system protein evidence is unavailable in the provided tissue summary. A minority of genes show enrichment in bone marrow, blood vessel, brain or testis, and several show cell-type enhancement in germ-line, neural, vascular, podocyte or platelet-related cells. These observations make a shared cellular program more plausible than a circulating-protein signature, while also leaving open the possibility that sample cellular composition contributes to the co-abundance pattern.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC nuclear lumen | 0.0317 | BRD8, CDK12, COIL, DDX55, GINS3, HAUS7, HPS6, KLC2, NCBP3, NCOA2, NUP205, ORC4, PM20D2, PRRC2A, RBBP6, RBM15, SIRT1, SRCAP, TAF6L, ZMYND8, ZNF451 |

### STRING and hu.MAP

STRING provides one high-confidence pairwise relationship within the module, BRD8--SRCAP, supporting a specific chromatin-remodeling connection. STRING functional evidence also links subsets of genes to nucleoplasm, nuclear lumen and nuclear bodies (STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.0093), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0093) and (STRING COMPARTMENTS Nuclear body; within-query FDR = 0.0231), and identifies the shared BAT2 amino-terminal or PRRC2 features among PRRC2A, PRRC2B and PRRC2C (STRING Pfam BAT2 N-terminus; within-query FDR = 0.0046), (STRING InterPro BAT2, N-terminal; within-query FDR = 0.0177), (STRING InterPro Protein PRRC2; within-query FDR = 0.0177). These are supplementary within-query findings and should not be treated as globally corrected enrichment. hu.MAP independently places PRRC2A with PRRC2C in a small complex (hu.MAP huMAP3_08887.1), PRRC2A with ZNF598 in several translation or ribosome-quality-control-related complexes (hu.MAP huMAP3_10307.1), (hu.MAP huMAP3_11111.1), (hu.MAP huMAP3_14270.1), (hu.MAP huMAP3_14559.1), and BRD8 with SRCAP in multiple SRCAP-related chromatin complexes (hu.MAP huMAP3_09291.1), (hu.MAP huMAP3_10481.1), (hu.MAP huMAP3_14306.1). RBBP6 with CDK12 and NCBP3 with RBBP6 also overlap large RNA-processing complexes (hu.MAP huMAP3_09621.1), (hu.MAP huMAP3_09943.1). Together, these results show that parts of the module recapitulate known molecular systems, while the full module is not a single established physical complex.

**STRING interactions (score >= 0.7)**: 1 of 325 gene pairs: BRD8–SRCAP (0.826)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam BAT2 N-terminus (FDR = 0.0046, 3 genes); COMPARTMENTS Nucleoplasm (FDR = 0.0093, 12 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0093, 15 genes); InterPro BAT2, N-terminal (FDR = 0.0177, 3 genes); InterPro Protein PRRC2 (FDR = 0.0177, 3 genes); COMPARTMENTS Nuclear body (FDR = 0.0231, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08887.1 (PRRC2A, PRRC2C; 2/2); huMAP3_10307.1 (PRRC2A, ZNF598; 2/20); huMAP3_09291.1 (SRCAP, BRD8; 2/27); huMAP3_11111.1 (PRRC2A, ZNF598; 2/29); huMAP3_10481.1 (SRCAP, BRD8; 2/40); huMAP3_14270.1 (PRRC2A, ZNF598; 2/47); huMAP3_14559.1 (PRRC2A, ZNF598; 2/47); huMAP3_14306.1 (SRCAP, BRD8; 2/55); huMAP3_09621.1 (RBBP6, CDK12; 2/56); huMAP3_09943.1 (NCBP3, RBBP6; 2/78)

### Novelty

The module should not be called wholly novel. Its internal relationships include a known BRD8-SRCAP STRING association and multiple hu.MAP overlaps involving PRRC2A, PRRC2C, ZNF598, RBBP6, CDK12 and NCBP3. The annotations also independently support nuclear transcription, RNA handling, chromatin regulation and translation-quality control. Nevertheless, the shared co-abundance organization across circulatory_system and kidney appears more novel than the individual molecular interactions, because the module combines genes from several known systems and has sparse direct STRING connectivity. Absence of additional STRING or hu.MAP links does not establish novelty; it may reflect incomplete interaction coverage, tissue-dependent regulation or co-abundance relationships that are not physical interactions. The defensible conclusion is a potentially new cross-tissue co-abundance configuration built from partly established biology, requiring replication and perturbation-based validation.

**Hypothesis.** Hypothesis: this module represents a shared nuclear homeostasis program active in kidney and circulatory-system samples. A chromatin and transcriptional-control axis involving BRD8, SRCAP, NCOA2, TAF6L, ZMYND8 and ZNF451 could coordinate expression, while CDK12, RBBP6, NCBP3, RBM15, COIL and DDX55 could couple transcription to RNA processing, export and surveillance. In parallel, PRRC2A, PRRC2B, PRRC2C and ZNF598 could connect transcript handling to translational regulation, stress granules and ribosome quality control. SIRT1, ORC4, GINS3 and HAUS7 may reflect links to genome maintenance and cell-cycle state. This model predicts that the module will track nuclear stress, differentiation or proliferative state across relevant kidney and vascular cell populations, rather than represent a secreted blood-borne pathway. This is a hypothesis, not a demonstrated causal mechanism.

### Important genes

#### BRD8

- **Related proteins** (co-abundance neighbors): NCOA2 (0.88), COIL (0.85), HPS6 (0.85), PRRC2A (0.84), PRRC2B (0.82); STRING partners: SRCAP (0.826)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_09291.1, huMAP3_10481.1, huMAP3_14306.1
- **Function (MyGene.info)**: bromodomain containing 8. The protein encoded by this gene interacts with thyroid hormone receptor in a ligand-dependent manner and enhances thyroid hormone-dependent activation from thyroid response elements. This protein contains a bromodomain and is thought to be a nuclear receptor coactivator. Multiple alternatively spliced transcript variants that encode distinct isoforms have been identified. [provided by RefSeq, Jul…
- **Diseases (Open Targets)**: neurodegenerative disease (0.546); Parkinson disease (0.370); Alzheimer disease (0.370); lysosomal storage disease (0.370); mathematical ability (0.093)
- **Europe PMC papers**: 1733
- **Why important**: BRD8 is among the more connected genes in the module and links directly to SRCAP, the clearest STRING relationship in the network. It is part of the globally significant nuclear-lumen signal (GO:CC nuclear lumen; q_global = 0.0317), appears in the nucleoplasm and nuclear-lumen STRING terms (STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.0093), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0093), and overlaps several SRCAP-related hu.MAP complexes (hu.MAP huMAP3_09291.1), (hu.MAP huMAP3_10481.1), (hu.MAP huMAP3_14306.1). Its bromodomain and transcriptional-coactivator annotation provide a plausible bridge between chromatin state and transcription. It also has substantial literature and disease-oriented evidence compared with many less studied module members.
- **Conclusion**: Established evidence supports BRD8 as a nuclear transcriptional and chromatin-associated anchor of the module. It is plausible, but not proven, that BRD8 helps organize the cross-tissue co-abundance signal through its relationship with SRCAP and other transcriptional regulators.

#### SRCAP

- **Related proteins** (co-abundance neighbors): RBBP6 (0.85), NCBP3 (0.84); STRING partners: BRD8 (0.826)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_09291.1, huMAP3_10481.1, huMAP3_14306.1
- **Function (MyGene.info)**: Snf2 related CREBBP activator protein. This gene encodes the core catalytic component of the multiprotein chromatin-remodeling SRCAP complex. The encoded protein is an ATPase that is necessary for the incorporation of the histone variant H2A.Z into nucleosomes. It can function as a transcriptional activator in Notch-mediated, CREB-mediated and steroid receptor-mediated transcription. Mutations in this gene cause Floating-Harbor syndrom…
- **Diseases (Open Targets)**: Floating-Harbor syndrome (0.799); hereditary disease (0.539); neurodevelopmental disorder (0.512); developmental delay, hypotonia, musculoskeletal defects, and behavioral abnormalities (0.462); neurodevelopmental disorder with hypotonia and variable intellectual and behavioral abnormalities (0.462)
- **Europe PMC papers**: 1276
- **Why important**: SRCAP connects to BRD8 in STRING and repeatedly overlaps BRD8-containing hu.MAP complexes (hu.MAP huMAP3_09291.1), (hu.MAP huMAP3_10481.1), (hu.MAP huMAP3_14306.1). It is part of (GO:CC nuclear lumen; q_global = 0.0317) and (STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.0093), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0093), and encodes the catalytic component of a chromatin-remodeling complex that incorporates H2A.Z into nucleosomes. Its established role in transcriptional activation and its association with Floating-Harbor syndrome make it a strong mechanistic and disease-relevant anchor.
- **Conclusion**: Established evidence identifies SRCAP as a chromatin-remodeling and transcriptional regulator embedded in known complexes. The module data support its participation in a shared nuclear regulatory program, but do not establish that SRCAP drives the co-abundance pattern.

#### PRRC2A

- **Related proteins** (co-abundance neighbors): SIRT1 (0.87), PRRC2C (0.84), BRD8 (0.84), ZNF598 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_08887.1, huMAP3_10307.1, huMAP3_11111.1, huMAP3_14270.1, huMAP3_14559.1
- **Function (MyGene.info)**: proline rich coiled-coil 2A. A cluster of genes, BAT1-BAT5, has been localized in the vicinity of the genes for TNF alpha and TNF beta. These genes are all within the human major histocompatibility complex class III region. This gene has microsatellite repeats which are associated with the age-at-onset of insulin-dependent diabetes mellitus (IDDM) and possibly thought to be involved with the inflammatory process of pancreatic…
- **Diseases (Open Targets)**: neurodegenerative disease (0.477); neoplasm (0.085); hepatocellular carcinoma (0.079); colorectal carcinoma (0.074); type 1 diabetes mellitus (0.051)
- **Europe PMC papers**: 993
- **Why important**: PRRC2A is a highly connected member linking SIRT1, PRRC2C, BRD8 and ZNF598. It is present in (GO:CC nuclear lumen; q_global = 0.0317) and the PRRC2-related STRING terms (STRING Pfam BAT2 N-terminus; within-query FDR = 0.0046), (STRING InterPro BAT2, N-terminal; within-query FDR = 0.0177), (STRING InterPro Protein PRRC2; within-query FDR = 0.0177), and it occurs in the compact PRRC2A-PRRC2C complex (hu.MAP huMAP3_08887.1) as well as several larger translation-related complexes with ZNF598 (hu.MAP huMAP3_10307.1), (hu.MAP huMAP3_11111.1), (hu.MAP huMAP3_14270.1), (hu.MAP huMAP3_14559.1). Its annotations support mRNA stabilization and regulation of cytoplasmic translation, while its genomic context and disease associations provide additional biological relevance.
- **Conclusion**: Established evidence supports PRRC2A as a connector between the module's nuclear signal and its post-transcriptional or translational component. A role in coupling RNA stability to nuclear regulatory state is a reasonable hypothesis, but the co-abundance data do not demonstrate that coupling.

#### SIRT1

- **Related proteins** (co-abundance neighbors): ZNF598 (0.94), KLC2 (0.88), PRRC2A (0.87), NUP205 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sirtuin 1. This gene encodes a member of the sirtuin family of proteins, homologs to the yeast Sir2 protein. Members of the sirtuin family are characterized by a sirtuin core domain and grouped into four classes. The functions of human sirtuins have not yet been determined; however, yeast sirtuin proteins are known to regulate epigenetic gene silencing and suppress recombination of rDNA. Studies suggest that…
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); atrial fibrillation (0.336); hypertensive disorder (0.204); tooth disorder (0.200); type 2 diabetes mellitus (0.140)
- **Europe PMC papers**: 55588
- **Why important**: SIRT1 has strong network connectivity and links to ZNF598, KLC2, PRRC2A and NUP205. It is part of (GO:CC nuclear lumen; q_global = 0.0317) and the STRING nucleoplasm, nuclear-lumen and nuclear-body terms (STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.0093), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0093), (STRING COMPARTMENTS Nuclear body; within-query FDR = 0.0231). Its established annotations include transcriptional regulation, DNA repair, rDNA heterochromatin formation and angiogenesis, making it relevant to both nuclear homeostasis and vascular biology. It is also one of the most extensively studied genes in the module and has disease associations including atrial fibrillation and hypertensive disorder.
- **Conclusion**: Established evidence supports SIRT1 as a multifunctional nuclear regulator with plausible vascular relevance. Its position suggests that it may coordinate stress, chromatin and repair signals in the module, but that integrative role remains a hypothesis.

#### RBBP6

- **Related proteins** (co-abundance neighbors): ZMYND8 (0.88), SRCAP (0.85), ZC3H7B (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_09621.1, huMAP3_09943.1
- **Function (MyGene.info)**: RB binding protein 6, ubiquitin ligase. The retinoblastoma tumor suppressor (pRB) protein binds with many other proteins. In various human cancers, pRB suppresses cellular proliferation and is inactivated. Cell cycle-dependent phosphorylation regulates the activity of pRB. This gene encodes a protein which binds to underphosphorylated but not phosphorylated pRB. Multiple alternatively spliced transcript variants that encode different is…
- **Diseases (Open Targets)**: neurodegenerative disease (0.556); Abnormality of the skeletal system (0.555); placental abruption (0.357); retinoschisis (0.230); retinal disorder (0.230)
- **Europe PMC papers**: 748
- **Why important**: RBBP6 links ZMYND8 and SRCAP to ZC3H7B and overlaps RNA-processing complexes with CDK12 and NCBP3 (hu.MAP huMAP3_09621.1), (hu.MAP huMAP3_09943.1). It contributes to (GO:CC nuclear lumen; q_global = 0.0317) and the STRING nucleoplasm, nuclear-lumen and nuclear-body terms (STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.0093), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0093), (STRING COMPARTMENTS Nuclear body; within-query FDR = 0.0231). Its functions span transcription-associated RNA processing, DNA replication control, DNA-damage response and ubiquitin-dependent protein turnover. HPA indicates bone-marrow tissue enhancement and platelet cell-type enhancement, which may be relevant to circulatory-system sample composition despite the generally low immune specificity.
- **Conclusion**: Established evidence supports RBBP6 as a bridge between transcription, RNA processing, genome maintenance and protein turnover. Its platelet and bone-marrow pattern is compatible with a possible sample-composition contribution, but does not prove that interpretation.

## Module 15

**Tissue pair**: circulatory_system and kidney  
**Genes (7)**: C1orf122, EIF3L, ATIC, CCT5, CCT3, CCT7, CCT8

### Function

The strongest interpretation is a cytosolic protein-folding and proteostasis module centered on the chaperonin-containing TCP-complex. CCT3, CCT5, CCT7, and CCT8 jointly account for the globally corrected enrichment of the chaperonin-containing T-complex and ATP-dependent protein-folding functions (GO:CC chaperonin-containing T-complex; q_global = 2.78e-07), (GO:MF ATP-dependent protein folding chaperone; q_global = 4.84e-05), (GO:CC protein folding chaperone complex; q_global = 0.000125), (GO:MF protein folding chaperone; q_global = 0.000298), (GO:MF unfolded protein binding; q_global = 0.000855), (GO:BP protein stabilization; q_global = 0.0128), (GO:BP protein folding; q_global = 0.0134). The same subunits also support globally corrected terms involving RNA and protein localization to the Cajal body, nuclear localization, telomere maintenance, and DNA biosynthesis (GO:BP regulation of telomerase RNA localization to Cajal body; q_global = 2.78e-07) through (GO:BP positive regulation of protein localization to Cajal body; q_global = 9.5e-07), (GO:BP RNA localization to Cajal body; q_global = 2.27e-06) through (GO:BP regulation of telomere maintenance via telomerase; q_global = 4.84e-05), (GO:BP regulation of telomere maintenance via telomere lengthening; q_global = 6.27e-05) through (GO:BP telomere maintenance via telomere lengthening; q_global = 0.000183), and (GO:BP positive regulation of protein localization to nucleus; q_global = 0.00104) through (GO:BP telomere organization; q_global = 0.00581). These latter annotations are biologically compatible with reported CCT involvement in folding proteins required for nuclear and telomere-related processes, but they should not be interpreted as proof that this tissue module directly performs telomerase regulation. The sperm-recognition and fertilization terms (GO:BP binding of sperm to zona pellucida; q_global = 2.27e-06), (GO:BP sperm-egg recognition; q_global = 4.44e-06), (GO:BP single fertilization; q_global = 0.000219), (GO:BP fertilization; q_global = 0.000941) are likely annotation consequences of the same CCT-associated gene set rather than evidence that the circulatory-system and kidney module is a reproductive-tissue program. ATIC contributes a plausible metabolic link through de novo purine biosynthesis, while EIF3L contributes a translation-initiation link; C1orf122 has no functional annotation in the fact sheet. Overall, the module most defensibly represents coordinated abundance of a partial CCT chaperonin core with peripheral metabolic and translation-associated genes.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It is also not blood-cell enriched, because every gene has low immune-cell specificity and no enriched blood-cell population is reported. Most genes have low tissue specificity, consistent with broadly expressed intracellular housekeeping or proteostasis machinery rather than a specialized circulatory or kidney product. HPA protein detection in kidney supports presence of most of the measured module there, whereas the circulatory-system comparison has no matching HPA tissue. Several genes show cell-type-enhanced expression in reproductive or placental cell types, including spermatocytes, spermatids, oocytes, and trophoblasts, but this does not establish that those cells explain the shared circulatory-system and kidney signal. The composition therefore favors a shared intracellular cellular program, or common cell-composition effects, over a blood-contamination or secreted-protein explanation.

**GO/KEGG enrichment**: 47 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chaperonin-containing T-complex | 2.78e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 2.78e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 2.78e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 9.5e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 9.5e-07 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP binding of sperm to zona pellucida | 2.27e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to Cajal body | 2.27e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 2.27e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 2.27e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 2.27e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 2.27e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 2.27e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 2.27e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP sperm-egg recognition | 4.44e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 7.59e-06 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING strongly confirms the known CCT relationships among CCT3, CCT5, CCT7, and CCT8 (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 2.71e-07) through (STRING InterPro GroEL-like equatorial domain superfamily; within-query FDR = 1.04e-06) and shows their association with actin folding, CCT target-protein biosynthesis, cellular proteostasis, and telomere maintenance (STRING RCTM Folding of actin by CCT/TriC; within-query FDR = 1.44e-06) through (STRING Process Positive regulation of telomere maintenance via telomerase; within-query FDR = 6.4e-06). The high-confidence STRING edges among these four subunits are therefore expected physical or functional relationships and provide strong support that the central module signal reflects the CCT complex. STRING also reports an ATIC-CCT7 relationship, but no STRING relationship is reported for EIF3L or C1orf122 within this module. hu.MAP independently places CCT3, CCT5, CCT7, and CCT8 together in multiple complexes (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_14584.1), with a smaller related complex also containing CCT3, CCT5, and CCT7 (hu.MAP huMAP3_01951.1). These complexes include additional CCT subunits and cofactors, showing that the module contains a partial, not complete, representation of a known multisubunit chaperonin assembly. ATIC, EIF3L, and C1orf122 have no hu.MAP complex reported here. Thus, the network is anchored by a well-established complex, with the peripheral genes requiring more cautious interpretation.

**STRING interactions (score >= 0.7)**: 7 of 21 gene pairs: ATIC–CCT7 (0.881); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam TCP-1/cpn60 chaperonin family (FDR = 2.71e-07, 4 genes); Component Chaperonin-containing T-complex (FDR = 5.57e-07, 4 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 6.11e-07, 4 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 1.04e-06, 4 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 1.04e-06, 4 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 1.04e-06, 4 genes); InterPro GroEL-like apical domain superfamily (FDR = 1.04e-06, 4 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 1.04e-06, 4 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 1.04e-06, 4 genes); RCTM Folding of actin by CCT/TriC (FDR = 1.44e-06, 4 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis (FDR = 1.91e-06, 4 genes); RCTM Association of TriC/CCT with target proteins during biosynthesis (FDR = 5.71e-06, 4 genes); RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding (FDR = 5.71e-06, 4 genes); Process Binding of sperm to zona pellucida (FDR = 6.4e-06, 4 genes); Process Positive regulation of telomere maintenance via telomerase (FDR = 6.4e-06, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8)

### Novelty

The molecular function represented by the central part of this module is not a new discovery: the CCT chaperonin complex and its roles in ATP-dependent folding, actin and tubulin folding, and proteostasis are already established by STRING, hu.MAP, and the gene descriptions. The tissue-pair co-abundance pattern could still be a useful new observation, particularly because the module combines a partial CCT core with ATIC, EIF3L, and C1orf122, but the fact sheet does not establish that this exact cross-tissue module has been previously reported or experimentally validated. The absence of STRING or hu.MAP support for the peripheral genes is evidence of limited prior curated interaction coverage, not proof of novelty. The most defensible conclusion is therefore contextual novelty of the co-abundance pattern remains possible, whereas novelty of the underlying CCT biology is not supported.

**Hypothesis.** Hypothesis: shared abundance of CCT3, CCT5, CCT7, and CCT8 across circulatory-system and kidney samples reflects a conserved demand for CCT-mediated folding and stabilization of newly synthesized cytosolic proteins. ATIC may connect this proteostasis state to purine-nucleotide production, while EIF3L may connect it to translation initiation; C1orf122 may represent an uncharacterized or context-dependent association with the CCT3-centered neighborhood. A further hypothesis is that the CCT activity helps maintain proteins involved in nuclear-body, RNA-localization, or telomere processes, consistent with (GO:BP regulation of telomerase RNA localization to Cajal body; q_global = 2.78e-07) through (GO:BP positive regulation of protein localization to Cajal body; q_global = 9.5e-07) and (GO:BP RNA localization to Cajal body; q_global = 2.27e-06) through (GO:BP telomere maintenance via telomere lengthening; q_global = 0.000183), but this requires direct protein-interaction, perturbation, and cell-composition testing. The co-abundance may also reflect shared abundance of broadly expressed intracellular machinery rather than a kidney-specific or circulatory-specific pathway.

### Important genes

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT5 (0.82), C1orf122 (0.81), ATIC (0.81); STRING partners: CCT5 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a central network gene linking the CCT submodule to CCT5 and to the peripheral ATIC and C1orf122 branches. It participates in every globally corrected term assigned to the CCT core (GO:CC chaperonin-containing T-complex; q_global = 2.78e-07) through (GO:BP protein localization to nucleus; q_global = 0.045), is present in all reported hu.MAP complexes (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_01951.1), and has very strong STRING support with the other core subunits. Its protein is an ATP-dependent CCT chaperonin subunit that folds actin and tubulin. It also has substantial literature coverage and disease associations involving neurodevelopmental and neurodegenerative phenotypes.
- **Conclusion**: Established: CCT3 is a core component and strong network anchor of the module, supporting a chaperonin interpretation. Hypothesis: its connection to ATIC and C1orf122 may mark additional tissue-contextual partners, but those links are not independently established by STRING or hu.MAP in the fact sheet.

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT7 (0.83), CCT8 (0.83), CCT3 (0.82); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 has the strongest network position among the listed genes and connects all three other CCT subunits. It appears in every globally corrected CCT-associated term (GO:CC chaperonin-containing T-complex; q_global = 2.78e-07) through (GO:BP protein localization to nucleus; q_global = 0.045), every reported STRING functional category (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 2.71e-07) through (STRING Process Positive regulation of telomere maintenance via telomerase; within-query FDR = 6.4e-06), and every hu.MAP complex (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_01951.1). Its established function is ATP-dependent folding of proteins including actin and tubulin, and mutations are associated with hereditary sensory and autonomic neuropathy with spastic paraplegia and other disease categories. It also has extensive literature coverage.
- **Conclusion**: Established: CCT5 is a principal structural and functional representative of the conserved CCT signal. Hypothesis: variation in CCT5 abundance could influence the folding capacity of the shared cellular program, but the co-abundance data do not demonstrate causality.

#### CCT7

- **Related proteins** (co-abundance neighbors): CCT5 (0.83), CCT8 (0.81); STRING partners: ATIC (0.881), CCT3 (0.999), CCT5 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is part of the densely connected CCT core and is the only core subunit with the reported STRING link to ATIC. It participates in the globally corrected chaperonin, protein-folding, RNA-localization, and telomere-related terms (GO:CC chaperonin-containing T-complex; q_global = 2.78e-07) through (GO:BP protein localization to nucleus; q_global = 0.045), all reported STRING CCT categories (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 2.71e-07) through (STRING Process Positive regulation of telomere maintenance via telomerase; within-query FDR = 6.4e-06), and all hu.MAP complexes (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_01951.1). Its established role is as a CCT chaperonin subunit; disease associations include myocardial infarction, preeclampsia, neurodegenerative disease, and hepatocellular carcinoma, although these associations do not define the module function.
- **Conclusion**: Established: CCT7 reinforces the CCT-core interpretation and provides the best-supported bridge to ATIC. Hypothesis: the ATIC-CCT7 relationship may couple proteostasis to purine metabolism in this tissue context, but the module alone cannot distinguish direct binding from coordinated abundance.

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT5 (0.83), CCT7 (0.81); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is a core CCT subunit connected to CCT3, CCT5, and CCT7, and occurs in nearly all reported hu.MAP complexes, including the complexes with the highest confidence (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_14584.1). It participates in the globally corrected CCT, protein-folding, RNA-localization, telomere, and nuclear-localization terms (GO:CC chaperonin-containing T-complex; q_global = 2.78e-07) through (GO:BP protein localization to nucleus; q_global = 0.045), as well as the corresponding STRING categories (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 2.71e-07) through (STRING Process Positive regulation of telomere maintenance via telomerase; within-query FDR = 6.4e-06). Its established description identifies it as the theta subunit of the abundant eukaryotic cytosolic CCT complex involved in assembly and folding of newly synthesized proteins. It also has substantial literature coverage and cancer-related disease associations.
- **Conclusion**: Established: CCT8 is a core component supporting a conserved cytosolic folding module. Hypothesis: its nucleoplasmic and germ-cell-associated HPA localization may indicate context-dependent deployment of CCT, but it does not establish a reproductive or nuclear specialization in the tissues studied.

#### ATIC

- **Related proteins** (co-abundance neighbors): EIF3L (0.82), CCT3 (0.81); STRING partners: CCT7 (0.881)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase. This gene encodes a bifunctional protein that catalyzes the last two steps of the de novo purine biosynthetic pathway. The N-terminal domain has phosphoribosylaminoimidazolecarboxamide formyltransferase activity, and the C-terminal domain has IMP cyclohydrolase activity. A mutation in this gene results in AICA-ribosiduria. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: AICA-ribosiduria (0.708); cancer (0.571); Intellectual disability (0.463); lung adenocarcinoma (0.390); anaplastic large cell lymphoma (0.374)
- **Europe PMC papers**: 5200
- **Why important**: ATIC is the most informative peripheral gene because it links the CCT3-centered module to a distinct biochemical process: the final steps of de novo purine biosynthesis. It is connected in the module to CCT3 and EIF3L, and STRING reports a relationship with CCT7, but it has no globally corrected GO or KEGG term in this module and no hu.MAP complex reported here. Its disease and literature evidence is substantial, including AICA-ribosiduria, cancer, intellectual disability, and lung adenocarcinoma.
- **Conclusion**: Established: ATIC provides a plausible purine-metabolism component adjacent to the CCT core, but it is not itself evidence for the enriched chaperonin or telomere terms. Hypothesis: ATIC may connect nucleotide supply to protein synthesis or proteostasis in the shared cellular state; this requires targeted biochemical and interaction experiments.

## Module 16

**Tissue pair**: circulatory_system and kidney  
**Genes (5)**: CDKN2AIP, PPP1R12A, PPP1R9B, SH3GLB2, TNRC6A

### Function

The module is most consistent with a regulatory and structural cell-biology program involving actomyosin organization, phosphatase control, intracellular signaling, RNA silencing, DNA-damage response, and membrane organization. PPP1R12A provides the strongest network-centered interpretation: it regulates myosin phosphatase and links Rho-dependent signaling to actin–myosin behavior, smooth-muscle contraction, and nonmuscle-cell adhesion. PPP1R9B adds an actin-filament and protein-phosphatase scaffold connection, while TNRC6A contributes post-transcriptional and microRNA-mediated regulation. CDKN2AIP contributes DNA-damage and p53-related signaling, and SH3GLB2 contributes endocytosis and membrane organization. No GO/KEGG term passed global correction, as indicated by the absence of globally significant GO/KEGG terms; therefore, these annotations support a hypothesis about module function but do not establish statistically significant pathway enrichment.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not blood-cell enriched according to HPA, which assigns all module genes low immune-cell specificity and shows no enriched blood-cell category. Four genes have low tissue specificity, while PPP1R9B is tissue enhanced in brain. All genes have cell-type-enhanced annotations, but these are distributed across neutrophils, monocytes, Kupffer cells, neural cells, epithelial cells, smooth-muscle cells, trophoblasts, and reproductive cell types rather than forming a coherent blood-cell signature. All five proteins are detected in kidney, whereas matching circulatory-system protein data are unavailable. Thus, the shared signal is more plausibly related to broadly distributed cellular regulatory machinery or shared cell types than to circulating plasma proteins; a blood-derived sample-composition explanation is not supported by the HPA summary.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no qualifying pairwise interactions among the module genes and no supplementary functional enrichment. This means the co-abundance edges are not independently supported by the reported high-confidence STRING network and should not be treated as established physical interactions. hu.MAP provides one relevant complex association, (hu.MAP huMAP3_09542.1), containing PPP1R12A and PPP1R9B together. The complex contains many additional cytoskeletal, actin-regulatory, adhesion, and Rho-associated proteins, so (hu.MAP huMAP3_09542.1) supports a shared structural or regulatory context for those two genes. However, only a subset of that complex is represented in this module, and hu.MAP does not establish that TNRC6A, CDKN2AIP, or SH3GLB2 physically interact with the complex. Overall, the network is better interpreted as a co-abundance relationship with limited external interaction support rather than as a demonstrated multiprotein complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09542.1 (PPP1R12A, PPP1R9B; 2/38)

### Novelty

The module may represent a tissue-pair-specific co-abundance pattern, but it cannot be called a newly discovered molecular complex or pathway. The absence of STRING interactions and the limited hu.MAP overlap indicate that the exact module-level organization is not already strongly represented in those resources, yet absence from those databases does not prove novelty. Several component functions are established individually, and the PPP1R12A–PPP1R9B relationship is represented in (hu.MAP huMAP3_09542.1). The potentially novel aspect is therefore the coordinated abundance of this particular combination across circulatory_system and kidney, not the discovery of previously unknown functions for the genes. Independent replication, comparison with other tissue pairs, perturbation experiments, and direct protein-interaction testing would be needed to support a new biological mechanism.

**Hypothesis.** Hypothesis: in kidney and circulatory-system samples, a broadly distributed cell-regulatory state co-varies with an actomyosin and adhesion-control scaffold centered on PPP1R12A and PPP1R9B. That scaffold may be coordinated with TNRC6A-dependent post-transcriptional regulation, CDKN2AIP-linked DNA-damage signaling, and SH3GLB2-linked membrane remodeling. The shared abundance pattern could therefore reflect coupling between cytoskeletal state, RNA-mediated regulation, cellular stress responses, and vesicle or membrane organization. This is a mechanistic hypothesis derived from gene annotations, the co-abundance topology, and (hu.MAP huMAP3_09542.1); it is not established by GO/KEGG enrichment, STRING interactions, or the available HPA evidence.

### Important genes

#### PPP1R12A

- **Related proteins** (co-abundance neighbors): CDKN2AIP (0.80), PPP1R9B (0.80), SH3GLB2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments, Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_09542.1
- **Function (MyGene.info)**: protein phosphatase 1 regulatory subunit 12A. Myosin phosphatase target subunit 1, which is also called the myosin-binding subunit of myosin phosphatase, is one of the subunits of myosin phosphatase. Myosin phosphatase regulates the interaction of actin and myosin downstream of the guanosine triphosphatase Rho. The small guanosine triphosphatase Rho is implicated in myosin light chain (MLC) phosphorylation, which results in contraction of smo…
- **Diseases (Open Targets)**: genitourinary and/or brain malformation syndrome (0.777); neurodegenerative disease (0.572); hereditary disease (0.415); holoprosencephaly (0.371); Genetic 46,XY disorder of sex development (0.370)
- **Europe PMC papers**: 1121
- **Why important**: PPP1R12A is the central network gene, connecting the other module components through the reported co-abundance edges. It encodes the myosin phosphatase target subunit and links Rho signaling to actomyosin behavior, smooth-muscle contraction, and cell adhesion. It is also a member of the hu.MAP association (hu.MAP huMAP3_09542.1) and has the largest literature base among the module genes, making it the strongest anchor for interpreting the module. Its HPA annotations include kidney detection and cell-type enhancement in neutrophil-lineage and smooth-muscle cells.
- **Conclusion**: Established evidence supports PPP1R12A as the principal cytoskeletal and phosphatase-regulatory anchor of the module. It is reasonable to hypothesize that variation in its abundance contributes to the shared module signal, but the co-abundance data do not demonstrate that it drives the other genes or that the module performs a unified myosin-phosphatase function.

#### PPP1R9B

- **Related proteins** (co-abundance neighbors): TNRC6A (0.88), PPP1R12A (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_09542.1
- **Function (MyGene.info)**: protein phosphatase 1 regulatory subunit 9B. This gene encodes a scaffold protein that functions as a regulatory subunit of protein phosphatase 1a. Expression of this gene is particularly high in dendritic spines, suggesting that the encoded protein may play a role in receiving signals from the central nervous system. The encoded protein has putative tumor suppressor function and decreased expression has been observed in tumors. [provided by…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); Alzheimer disease (0.167); open-angle glaucoma (0.146); benign prostatic hyperplasia (0.119); glaucoma (0.100)
- **Europe PMC papers**: 405
- **Why important**: PPP1R9B directly connects to PPP1R12A in the module and is the second module member in hu.MAP complex (hu.MAP huMAP3_09542.1). It is a protein phosphatase scaffold with reported roles in actin-filament organization, developmental signaling, and neuronal signaling, and it is tissue enhanced in brain while showing cell-type enhancement in monocytes, Kupffer cells, and neutrophils. Its position provides the clearest bridge between the actomyosin interpretation and the module's broader regulatory character.
- **Conclusion**: Established evidence supports PPP1R9B as a scaffold associated with protein phosphatase regulation and actin organization, and (hu.MAP huMAP3_09542.1) supports a shared complex context with PPP1R12A. The proposed role of PPP1R9B in coordinating the entire module remains a hypothesis because STRING does not report qualifying interactions and no globally significant GO/KEGG term supports pathway-level enrichment.

#### TNRC6A

- **Related proteins** (co-abundance neighbors): PPP1R9B (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus, Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: trinucleotide repeat containing adaptor 6A. This gene encodes a member of the trinucleotide repeat containing 6 protein family. The protein functions in post-transcriptional gene silencing through the RNA interference (RNAi) and microRNA pathways. The protein associates with messenger RNAs and Argonaute proteins in cytoplasmic bodies known as GW-bodies or P-bodies. Inhibiting expression of this gene delocalizes other GW-body proteins and im…
- **Diseases (Open Targets)**: intelligence (0.468); smoking initiation (0.446); chronic obstructive pulmonary disease (0.395); shortness of breath (0.374); type 2 diabetes mellitus (0.373)
- **Europe PMC papers**: 1016
- **Why important**: TNRC6A is connected to PPP1R9B and contributes a distinct regulatory layer through Argonaute-associated RNA silencing, P-body biology, microRNA-mediated regulation, and messenger-RNA turnover. It has substantial literature coverage and broad cellular localization, including nucleoplasm, Golgi apparatus, and vesicles. Its presence prevents the module from being interpreted as purely structural and suggests possible coupling between cytoskeletal state and post-transcriptional control.
- **Conclusion**: Established evidence supports TNRC6A as a mediator of RNA-silencing and post-transcriptional regulation. Its inclusion in this module does not establish a physical or functional connection to the phosphatase scaffold; that linkage is a hypothesis based on co-abundance and network adjacency.

#### CDKN2AIP

- **Related proteins** (co-abundance neighbors): PPP1R12A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CDKN2A interacting protein. The protein encoded by this gene regulates the DNA damage response through several different signaling pathways. One such pathway is the p53-HDM2-p21(WAF1) pathway, which is critical to the DNA damage response. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.488); body weight gain (0.231); urolithiasis (0.194); alcohol drinking (0.194); major depressive disorder (0.165)
- **Europe PMC papers**: 412
- **Why important**: CDKN2AIP connects to the central PPP1R12A node and encodes a regulator of DNA-damage responses involving p53, HDM2, and p21-related signaling. It also has reported roles in regulation of cell growth and protein stability. HPA annotations place it in the nucleoplasm and show broad tissue distribution with cell-type enhancement across epithelial and reproductive cell types, supporting a general stress or growth-regulatory interpretation rather than a blood-specific one.
- **Conclusion**: Established evidence supports CDKN2AIP as a DNA-damage and cell-growth regulator. Its relationship to actomyosin regulation or the shared tissue-pair module is not established; a coordinated stress-and-cytoskeletal state is a plausible but untested hypothesis.

#### SH3GLB2

- **Related proteins** (co-abundance neighbors): PPP1R12A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SH3 domain containing GRB2 like, endophilin B2. Enables identical protein binding activity. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: sandestig-stefanova syndrome (0.500); Alzheimer disease (0.294); Parkinson disease (0.292); neurodegenerative disease (0.292); lysosomal storage disease (0.292)
- **Europe PMC papers**: 251
- **Why important**: SH3GLB2 connects to PPP1R12A and adds membrane-trafficking biology through endocytosis and membrane organization. It is localized to cytosol and nucleoplasm and has cell-type-enhanced annotations in trophoblast and esophageal epithelial populations. Its disease associations include neurodegenerative and lysosomal-storage categories, while its relatively smaller literature base makes it less established mechanistically than the phosphatase and RNA-regulatory genes. Nevertheless, it is important because it broadens the module toward vesicle and membrane remodeling.
- **Conclusion**: Established evidence supports SH3GLB2 as a protein involved in endocytosis and membrane organization. Its co-abundance with PPP1R12A may indicate coordinated membrane–cytoskeleton regulation, but this connection remains hypothetical because no qualifying STRING interaction or globally significant pathway term supports it.

## Module 17

**Tissue pair**: circulatory_system and kidney  
**Genes (19)**: CPSF6, DNMT1, IPO11, IRAK1, RPS6KB1, LSM5, MSH2, MSH6, NAA15, NAA25, NEFM, NPM3, NUP155, OSBPL9, PSMC6, POLR3D, DIS3, SLFN11, WDR12

### Function

The strongest and only globally corrected functional signal is DNA mismatch recognition and repair, supported by (GO:MF single thymine insertion binding; q_global = 0.0487) single thymine insertion binding and (GO:CC MutSalpha complex; q_global = 0.0487) the MutSalpha complex, both driven by MSH2 and MSH6. Their known biology establishes that MSH2 and MSH6 heterodimerize to recognize mismatched DNA and participate in mismatch repair. The remaining genes suggest a broader nuclear maintenance context, including DNA methylation through DNMT1, RNA processing through DIS3, CPSF6, LSM5 and POLR3D, nucleocytoplasmic transport through IPO11 and NUP155, proteostasis through PSMC6, ribosome biogenesis through WDR12 and NPM3, and signaling through IRAK1 and RPS6KB1. These additional themes are biological interpretation rather than globally corrected enrichment. The STRING colorectal-cancer term (STRING KEGG Colorectal cancer; within-query FDR = 0.0457) is supplementary and should not be treated as primary enrichment.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and most have enhanced rather than narrowly restricted single-cell expression. Immune-cell specificity is generally low, with only isolated immune-related or cell-associated signals. Kidney protein detection is reported for most genes, whereas circulatory-system protein detection has no matching HPA tissue result. The presence of NEFM, NUP155 and other genes with reproductive, neuronal, muscle, endothelial, platelet or progenitor-associated cell annotations indicates a mixed cellular composition rather than a clean blood-cell module. Thus, shared abundance may partly reflect broadly expressed intracellular housekeeping or nuclear programs, and possibly shared cell types in the sampled tissues, rather than a circulating secreted-protein program.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF single thymine insertion binding | 0.0487 | MSH2, MSH6 |
| GO:CC MutSalpha complex | 0.0487 | MSH2, MSH6 |

### STRING and hu.MAP

STRING provides a compact known interaction backbone. MSH2--MSH6 is the strongest listed relationship and is directly concordant with (GO:MF single thymine insertion binding; q_global = 0.0487) and (GO:CC MutSalpha complex; q_global = 0.0487). DNMT1 connects to both MSH2 and MSH6, supporting a known relationship between mismatch-repair machinery and DNA methylation-associated nuclear biology. NAA15--NAA25 is also a strong known pair, representing the NatA auxiliary and NatB auxiliary acetyltransferase components, although the module does not provide a globally corrected term for these complexes. The remaining module edges are not supported by the listed high-confidence STRING interactions. STRING nuclear localization (STRING Keyword Nucleus; within-query FDR = 0.0154) is consistent with the many nucleoplasmic and RNA-processing proteins, but is supplementary. hu.MAP identifies IRAK1 and MSH6 together in (hu.MAP huMAP3_10240.1) and (hu.MAP huMAP3_10665.1), but each complex contains only a small subset of the module members and has relatively low confidence. These complex results therefore suggest possible contextual convergence rather than evidence that the whole module is one established physical complex.

**STRING interactions (score >= 0.7)**: 4 of 171 gene pairs: DNMT1–MSH2 (0.718); DNMT1–MSH6 (0.781); MSH2–MSH6 (0.999); NAA15–NAA25 (0.993)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Nucleus (FDR = 0.0154, 16 genes); KEGG Colorectal cancer (FDR = 0.0457, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10240.1 (IRAK1, MSH6; 2/12); huMAP3_10665.1 (IRAK1, MSH6; 2/42)

### Novelty

The module is unlikely to represent a wholly new molecular mechanism because its clearest core, MSH2 with MSH6, is an established MutSalpha mismatch-repair complex and is directly present in STRING. The DNMT1 links to MSH2 and MSH6 and the NAA15--NAA25 pair are also already represented in STRING. Conversely, most module relationships are not listed in STRING, and hu.MAP supports only partial overlaps involving IRAK1 and MSH6. This may indicate a novel tissue-pair co-abundance configuration or a mixture of coordinated nuclear programs, but absence from interaction databases does not prove novelty. The appropriate conclusion is that the module-level co-abundance pattern may be novel or under-characterized, while its central mismatch-repair biology is established.

**Hypothesis.** Hypothesis: in shared circulatory-system and kidney samples, variation in a broadly expressed nuclear maintenance state co-varies across mismatch repair, DNA methylation, RNA processing, nucleocytoplasmic transport, proteostasis and growth or inflammatory signaling. MSH2--MSH6 may form the mechanistic anchor, with DNMT1 coupling genome maintenance to epigenetic state, while DIS3, CPSF6, LSM5 and POLR3D reflect coordinated RNA surveillance and transcriptional processing. IRAK1 and RPS6KB1 could connect this state to inflammatory or nutrient-responsive signaling. This is a testable hypothesis, not proof that these proteins physically assemble or that the shared signal is specific to kidney or blood biology.

### Important genes

#### MSH2

- **Related proteins** (co-abundance neighbors): NEFM (0.87), DIS3 (0.86), IRAK1 (0.85), NAA25 (0.82), MSH6 (0.81), CPSF6 (0.81); STRING partners: DNMT1 (0.718), MSH6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutS homolog 2. This locus is frequently mutated in hereditary nonpolyposis colon cancer (HNPCC). When cloned, it was discovered to be a human homolog of the E. coli mismatch repair gene mutS, consistent with the characteristic alterations in microsatellite sequences (RER+ phenotype) found in HNPCC. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: Lynch syndrome (0.891); colorectal cancer (0.776); mismatch repair cancer syndrome (0.775); Muir-Torre syndrome (0.752); mismatch repair cancer syndrome 1 (0.740)
- **Europe PMC papers**: 22581
- **Why important**: MSH2 is the most central gene in the co-abundance network and connects to MSH6, DNMT1 and several other module members. It is present in both globally corrected terms (GO:MF single thymine insertion binding; q_global = 0.0487) and (GO:CC MutSalpha complex; q_global = 0.0487), has established mismatch-repair and DNA-damage functions, and is strongly associated with Lynch syndrome, colorectal cancer and mismatch-repair cancer syndromes. Its extensive literature makes it the best-supported biological anchor.
- **Conclusion**: Established evidence supports MSH2 as a core mismatch-repair component and the principal interpretive anchor of this module. It is plausible, but not established here, that its co-abundance links the module to a broader genome-maintenance state in the two tissues.

#### MSH6

- **Related proteins** (co-abundance neighbors): MSH2 (0.81); STRING partners: DNMT1 (0.781), MSH2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus, Vesicles; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_10240.1, huMAP3_10665.1
- **Function (MyGene.info)**: mutS homolog 6. This gene encodes a member of the DNA mismatch repair MutS family. In E. coli, the MutS protein helps in the recognition of mismatched nucleotides prior to their repair. A highly conserved region of approximately 150 aa, called the Walker-A adenine nucleotide binding motif, exists in MutS homologs. The encoded protein heterodimerizes with MSH2 to form a mismatch recognition complex that functions …
- **Diseases (Open Targets)**: Lynch syndrome (0.878); colorectal cancer (0.832); endometrial cancer (0.819); mismatch repair cancer syndrome (0.799); mismatch repair cancer syndrome 1 (0.737)
- **Europe PMC papers**: 17901
- **Why important**: MSH6 forms the established MutSalpha mismatch-recognition heterodimer with MSH2, and it is present in both (GO:MF single thymine insertion binding; q_global = 0.0487) and (GO:CC MutSalpha complex; q_global = 0.0487). It has a strong STRING relationship with MSH2 and is also the only module member appearing with IRAK1 in both hu.MAP complexes (hu.MAP huMAP3_10240.1) and (hu.MAP huMAP3_10665.1). Its associations with Lynch syndrome, colorectal cancer and endometrial cancer add substantial disease relevance and literature support.
- **Conclusion**: Established evidence identifies MSH6 as the partner that gives the module its clearest functional interpretation: mismatch recognition and repair. The hu.MAP co-occurrence with IRAK1 is intriguing but insufficient to establish a physical or regulatory connection.

#### DNMT1

- **Related proteins** (co-abundance neighbors): SLFN11 (0.87); STRING partners: MSH2 (0.718), MSH6 (0.781)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA methyltransferase 1. This gene encodes an enzyme that transfers methyl groups to cytosine nucleotides of genomic DNA. This protein is the major enzyme responsible for maintaining methylation patterns following DNA replication and shows a preference for hemi-methylated DNA. Methylation of DNA is an important component of mammalian epigenetic gene regulation. Aberrant methylation patterns are found in human tumors and a…
- **Diseases (Open Targets)**: autosomal dominant cerebellar ataxia, deafness and narcolepsy (0.806); hereditary sensory neuropathy-deafness-dementia syndrome (0.777); acute myeloid leukemia (0.623); myelodysplastic syndrome (0.615); cancer (0.612)
- **Europe PMC papers**: 30754
- **Why important**: DNMT1 is connected in STRING to both MSH2 and MSH6, placing DNA methylation beside the module's mismatch-repair core. It maintains DNA methylation after replication and has extensive literature and disease associations including hereditary neurological disease, acute myeloid leukemia, myelodysplastic syndrome and cancer. Its network position is less central than MSH2, but its functional bridge is especially informative.
- **Conclusion**: Established evidence supports DNMT1 as a DNA-methylation maintenance enzyme linked by known interactions to the mismatch-repair pair. The hypothesis that it coordinates epigenetic state with the observed co-abundance module remains unproven.

#### IRAK1

- **Related proteins** (co-abundance neighbors): MSH2 (0.85), OSBPL9 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_10240.1, huMAP3_10665.1
- **Function (MyGene.info)**: interleukin 1 receptor associated kinase 1. This gene encodes the interleukin-1 receptor-associated kinase 1, one of two putative serine/threonine kinases that become associated with the interleukin-1 receptor (IL1R) upon stimulation. This gene is partially responsible for IL1-induced upregulation of the transcription factor NF-kappa B. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [pro…
- **Diseases (Open Targets)**: myelofibrosis (0.492); systemic lupus erythematosus (0.490); primary myelofibrosis (0.484); neoplasm (0.398); rheumatoid arthritis (0.393)
- **Europe PMC papers**: 10036
- **Why important**: IRAK1 provides the strongest immune-signaling interpretation in an otherwise largely nuclear and housekeeping-like module. It regulates interleukin and Toll-like-receptor signaling and canonical NF-kappa-B signaling, has substantial literature, and is associated with systemic lupus erythematosus, rheumatoid arthritis and myelofibrosis. It also appears with MSH6 in both hu.MAP complexes (hu.MAP huMAP3_10240.1) and (hu.MAP huMAP3_10665.1), although it has no listed high-confidence STRING partner.
- **Conclusion**: Established evidence supports IRAK1 as an inflammatory signaling kinase and a possible contextual marker of immune or stress-related state. Its apparent connection to MSH6 in hu.MAP is not enough to establish a direct mechanistic bridge, so any coupling to mismatch repair remains hypothetical.

#### DIS3

- **Related proteins** (co-abundance neighbors): MSH2 (0.86), RPS6KB1 (0.82), POLR3D (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DIS3 exosome endoribonuclease and 3'-5' exoribonuclease. Enables 3'-5'-exoribonuclease activity; endonuclease activity; and guanyl-nucleotide exchange factor activity. Involved in CUT catabolic process and rRNA catabolic process. Located in cytosol and nucleoplasm. Part of nuclear exosome (RNase complex). [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: plasma cell myeloma (0.438); self-injurious ideation (0.318); hyperpituitarism (0.237); restless legs syndrome (0.201); phototoxic dermatitis (0.137)
- **Europe PMC papers**: 2070
- **Why important**: DIS3 occupies a connecting position between MSH2, RPS6KB1 and POLR3D and is a catalytic component of the nuclear exosome involved in RNA degradation and rRNA processing. It contributes to the supplementary nuclear signal (STRING Keyword Nucleus; within-query FDR = 0.0154) and has disease associations including plasma-cell myeloma. Its literature is substantial, and it offers a coherent explanation for why RNA surveillance and processing genes co-vary with the mismatch-repair core.
- **Conclusion**: Established evidence supports DIS3 as an RNA surveillance and processing factor positioned near the module's DNA-repair and transcriptional machinery. A coordinated DNA-and-RNA quality-control state is a reasonable hypothesis, but the co-abundance data do not prove that DIS3 regulates MSH2 or MSH6.

## Module 18

**Tissue pair**: circulatory_system and kidney  
**Genes (6)**: IMPDH1, NUP214, ORC5, RPAP3, STEEP1, DNTTIP2

### Function

This module does not support a single established biological function from enrichment: no GO or KEGG term passed global correction. Its genes instead point to a mixed intracellular program involving endoplasmic-reticulum organization and vesicle trafficking through STEEP1, nuclear RNA processing and transport through DNTTIP2 and NUP214, DNA-replication initiation through ORC5, protein stabilization through RPAP3, and guanine-nucleotide biosynthesis through IMPDH1. The co-abundance structure is organized around STEEP1 and DNTTIP2: STEEP1 connects the replication-associated, nucleotide-metabolism, and DNTTIP2 branches, while DNTTIP2 connects to RPAP3 and NUP214. This topology suggests coordinated expression rather than a demonstrated shared biochemical pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: all members are annotated as non-secreted, intracellular proteins. Most members have low tissue specificity and low immune-cell specificity, consistent with broadly expressed intracellular or housekeeping-type biology. However, HPA evidence also points to cell-type-associated expression. IMPDH1 is associated with monocytes, neutrophils, and other myeloid populations, and NUP214 is associated with neutrophils and monocytes; STEEP1 and ORC5 have oocyte-associated expression, while IMPDH1 and NUP214 also show retinal or germ-cell-associated patterns. The shared circulatory-system and kidney signal could therefore reflect broadly expressed kidney cells, shared intracellular programs, or blood-cell contributions to samples rather than a specialized circulatory-kidney pathway. Kidney protein detection supports expression for most members, whereas no matching circulatory-system HPA tissue assessment is available.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module members and no hu.MAP complex containing multiple members. Thus, the co-abundance edges are not corroborated as established physical protein interactions or as a known multiprotein complex. The annotations nevertheless identify plausible cellular neighborhoods: ORC5 belongs to the origin-recognition replication complex, NUP214 is a nuclear-pore component, and the other genes have roles related to trafficking, RNA processing, protein stabilization, or nucleotide metabolism. These are established functions of individual genes, not evidence that all six proteins act together in one complex.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The conserved co-abundance pattern appears potentially novel as a cross-tissue module because it lacks corroborating STRING interactions, lacks a multi-member hu.MAP complex, and has no globally significant GO or KEGG enrichment. However, those absences do not prove biological novelty. The module may represent coordinated regulation of broadly expressed genes, shared cell-type composition, or a context-dependent transcriptional program that is not captured by curated interaction resources. The mixed annotations and absence of a common enriched pathway make a claim of a newly discovered molecular pathway premature.

**Hypothesis.** Hypothesis: this module reflects a shared intracellular stress, growth, or cell-state program in kidney and circulatory-system samples, in which STEEP1-linked membrane-trafficking or innate-signaling biology is co-regulated with nuclear transport, RNA processing, replication competence, and guanine-nucleotide supply. A contribution from myeloid cells is also plausible because HPA associates IMPDH1 and NUP214 with monocytes and neutrophils. This should be tested by cell-composition adjustment, cell-type-resolved expression analysis, and independent validation of the module in additional cohorts; it should not be interpreted as an established physical pathway.

Web sources: https://www.nature.com/articles/s41590-020-0730-5

### Important genes

#### STEEP1

- **Related proteins** (co-abundance neighbors): ORC5 (0.84), DNTTIP2 (0.84), IMPDH1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: STING1 ER exit protein 1. While this gene is well-supported by transcript data, no functional information on its protein products is currently available. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2009].
- **Diseases (Open Targets)**: non-syndromic X-linked intellectual disability (0.646); triple-negative breast carcinoma (0.074); breast cancer (0.071); breast carcinoma (0.067); microcephalic primordial dwarfism due to ZNF335 deficiency (0.046)
- **Europe PMC papers**: 20
- **Why important**: STEEP1 is the most connected module member and links ORC5, DNTTIP2, and IMPDH1, making it the principal network bridge. The fact sheet assigns it endoplasmic-reticulum to Golgi transport and endoplasmic-reticulum membrane organization, while the web search identified literature describing STEEP as a positive regulator of STING ER exit and signaling. It has relatively limited literature volume and no STRING or hu.MAP support within this module, so its centrality is more informative for hypothesis generation than proof of mechanism.
- **Conclusion**: Established: STEEP1 is a central co-abundance connector and has annotated roles in intracellular membrane organization and transport. Hypothesis: it may coordinate the module with ER or innate-signaling state. The module does not establish that STEEP1 physically interacts with the other members.

#### DNTTIP2

- **Related proteins** (co-abundance neighbors): STEEP1 (0.84), RPAP3 (0.83), NUP214 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: deoxynucleotidyltransferase terminal interacting protein 2. This gene is thought to be involved in chromatin remodeling and gene transcription. The encoded nuclear protein binds to and enhances the transcriptional activity of the estrogen receptor alpha, and also interacts with terminal deoxynucleotidyltransferase. The expression profile of this gene is a potential biomarker for chronic obstructive pulmonary disease. [provided by RefSeq, Dec 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.164); narcolepsy (0.117); Aphasia (0.113); alcohol drinking (0.068); device complication (0.046)
- **Europe PMC papers**: 1134
- **Why important**: DNTTIP2 is jointly central with STEEP1 and connects STEEP1 to RPAP3 and NUP214. Its annotations involve chromatin remodeling, transcriptional regulation, RNA processing, and ribosomal small-subunit biogenesis. Its substantial literature volume makes it one of the better-characterized members, although the module provides no enriched GO or KEGG term and no external interaction support.
- **Conclusion**: Established: DNTTIP2 occupies a central position and is linked by annotation to nuclear gene-expression and RNA-processing biology. Hypothesis: it may be a regulatory bridge between the membrane-trafficking-associated STEEP1 branch and the nuclear transport branch. This coordinating role remains unproven.

#### IMPDH1

- **Related proteins** (co-abundance neighbors): STEEP1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol, Rods & Rings; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inosine monophosphate dehydrogenase 1. The protein encoded by this gene acts as a homotetramer to regulate cell growth. The encoded protein is an enzyme that catalyzes the synthesis of xanthine monophosphate (XMP) from inosine-5'-monophosphate (IMP). This is the rate-limiting step in the de novo synthesis of guanine nucleotides. Defects in this gene are a cause of retinitis pigmentosa type 10 (RP10). Several transcript variants encodin…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.725); retinitis pigmentosa 10 (0.683); Leber congenital amaurosis (0.625); chronic hepatitis C virus infection (0.604); hepatitis C virus infection (0.602)
- **Europe PMC papers**: 1978
- **Why important**: IMPDH1 is a direct STEEP1 neighbor and catalyzes a rate-limiting step in de novo guanine-nucleotide production. It has strong disease relevance to inherited retinal degeneration and HPA associates it with retina, photoreceptor-related cell types, monocytes, and neutrophils. Its broad disease and literature record makes it biologically informative, while its blood-cell pattern is important for interpreting a circulatory-system module.
- **Conclusion**: Established: IMPDH1 supplies guanine-nucleotide biosynthesis and is associated with retinal disease and several myeloid cell types. Hypothesis: its co-abundance with STEEP1 may reflect cell growth, stress, immune activation, or sample-composition effects requiring nucleotide demand. The data do not distinguish these explanations.

#### NUP214

- **Related proteins** (co-abundance neighbors): DNTTIP2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 214. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene is a member of the FG-repeat-containing nucleoporins. The protein encoded by this gene is localized to the cytoplas…
- **Diseases (Open Targets)**: familial acute necrotizing encephalopathy (0.664); Orthomyxoviridae infectious disease (0.543); HIV infectious disease (0.542); viral infectious disease (0.527); Global developmental delay (0.435)
- **Europe PMC papers**: 2712
- **Why important**: NUP214 is a direct DNTTIP2 neighbor and represents the nuclear-transport arm of the module. It is a nucleoporin involved in RNA and protein transport across the nuclear envelope, has extensive literature and disease associations, and is HPA-associated with neutrophils and monocytes. Its inclusion therefore provides both a plausible nuclear-transport interpretation and a possible blood-cell-composition signal.
- **Conclusion**: Established: NUP214 is a nuclear-pore component with roles in nucleocytoplasmic transport and expression associations in myeloid cells. Hypothesis: its co-abundance with DNTTIP2 may reflect coordinated regulation of nuclear RNA handling in a shared cell state. No module-level physical complex or pathway is demonstrated.

#### ORC5

- **Related proteins** (co-abundance neighbors): STEEP1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: origin recognition complex subunit 5. The origin recognition complex (ORC) is a highly conserved six subunit protein complex essential for the initiation of the DNA replication in eukaryotic cells. Studies in yeast demonstrated that ORC binds specifically to origins of replication and serves as a platform for the assembly of additional initiation factors such as Cdc6 and Mcm proteins. The protein encoded by this gene is a subunit of t…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); response to antihypertensive drug (0.263); heart failure (0.263); schizophrenia (0.241); arthropathy (0.103)
- **Europe PMC papers**: 614
- **Why important**: ORC5 is the replication-associated member and is connected directly to the module hub STEEP1. It is a subunit of the conserved origin-recognition complex and is annotated for DNA-replication initiation and regulation of replication. Its network position gives it a defined but peripheral connection, and its HPA profile is broadly expressed with oocyte-associated cell-type enrichment.
- **Conclusion**: Established: ORC5 participates in the origin-recognition complex and replication initiation. Hypothesis: its co-abundance with STEEP1 may mark proliferative or cell-state variation rather than a direct STEEP1-linked replication mechanism. The module lacks evidence for a shared replication complex.
