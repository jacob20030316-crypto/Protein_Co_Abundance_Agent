# Conserved co-abundance modules: autonomic_nervous_system and brain

## Module 0

**Tissue pair**: autonomic_nervous_system and brain  
**Genes (47)**: PPP2R2A, HIBADH, ABHD10, ABHD14B, AIFM1, AP1S1, BOP1, CD276, COX7A2, DDX41, DECR1, HADHB, GCSH, GRK3, IDH3A, LYSMD2, ABCB1, MGME1, IMMT, MPDU1, NCEH1, NDUFC1, IVNS1ABP, PDHB, PLXNB2, PTCD3, PTK7, RAB21, MRPL13, MRPL45, MRPL55, RRP8, MRPS27, MRPS35, SDC2, SEC63, SMARCA4, HM13, SPR, SUCLG1, SUPV3L1, TRAPPC4, TRNT1, UBA5, VTA1, RP2, SLC30A7

### Function

The module is best interpreted as a mitochondrial maintenance and energy-production program, with a particularly strong mitochondrial translation component. The primary evidence is the enrichment of mitochondrial matrix (GO:CC mitochondrial matrix; q_global = 0.00102), mitochondrial protein-containing complex (GO:CC mitochondrial protein-containing complex; q_global = 0.00532), mitochondrion (GO:CC mitochondrion; q_global = 0.00661), Ribosome (KEGG Ribosome - Homo sapiens (human); q_global = 0.0237), organellar ribosome (GO:CC organellar ribosome; q_global = 0.0367), and mitochondrial ribosome (GO:CC mitochondrial ribosome; q_global = 0.0367). The genes span mitochondrial ribosomal proteins, mitochondrial RNA processing, oxidative phosphorylation, the tricarboxylic acid cycle, pyruvate entry into the cycle, amino-acid catabolism, and fatty-acid oxidation. Thus, the most coherent interpretation is coordinated abundance of mitochondrial protein synthesis machinery together with respiratory and intermediary-metabolism components. The module is not restricted to a single enzymatic pathway: its structure suggests a broader mitochondrial capacity or state program rather than a narrowly defined pathway. The presence of genes involved in mitochondrial inner-membrane organization, mitochondrial genome maintenance, RNA surveillance, and vesicle or membrane processes indicates that mitochondrial translation and respiratory metabolism are embedded in wider organelle homeostasis.

**Cell composition.** This does not resemble a plasma-protein or secreted-protein module: the HPA summary identifies only a small secreted component, and the individual proteins are predominantly intracellular, mitochondrial, membrane, cytosolic, or nuclear. It also does not look primarily blood-cell driven. Most genes have low immune-cell specificity, although selected genes show enrichment in myeloid or other immune populations. Tissue specificity is generally low, with some tissue-enhanced or group-enriched genes in brain, muscle, tongue, kidney, liver, heart muscle, and bone marrow. The diverse HPA single-cell enhancements, including epithelial, muscle, neuronal, hepatic, reproductive, and immune cell types, are more consistent with a broadly used metabolic program than with a single contaminating cell type. Protein detection throughout the sampled brain regions supports biological presence in brain, but the lack of matching autonomic-nervous-system HPA tissue data prevents a direct protein-level comparison there. The shared signal could therefore reflect conserved mitochondrial abundance across cell types in the two tissue groups, while sample composition and cell-type mixture remain possible contributors.

**GO/KEGG enrichment**: 6 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrial matrix | 0.00102 | ABHD10, DECR1, GCSH, HADHB, HIBADH, IDH3A, MRPL13, MRPL55, MRPS27, MRPS35, PDHB, PTCD3, SUCLG1, SUPV3L1, TRNT1 |
| GO:CC mitochondrial protein-containing complex | 0.00532 | HADHB, IMMT, MRPL13, MRPL55, MRPS27, MRPS35, PTCD3, SUPV3L1 |
| GO:CC mitochondrion | 0.00661 | ABHD10, AIFM1, COX7A2, DECR1, GCSH, HADHB, HIBADH, IDH3A, IMMT, MGME1, MRPL13, MRPL45, MRPL55, MRPS27, MRPS35, NDUFC1, PDHB, PTCD3, SLC30A7, SPR, SUCLG1, SUPV3L1, TRNT1 |
| KEGG Ribosome - Homo sapiens (human) | 0.0237 | MRPL13, MRPL45, MRPL55, MRPS27, MRPS35, PTCD3 |
| GO:CC organellar ribosome | 0.0367 | MRPL13, MRPL55, MRPS27, MRPS35, PTCD3 |
| GO:CC mitochondrial ribosome | 0.0367 | MRPL13, MRPL55, MRPS27, MRPS35, PTCD3 |

### STRING and hu.MAP

STRING provides strong support for a real mitochondrial subnetwork. The most prominent known relationships form a tightly connected group of MRPL13, MRPL45, MRPL55, MRPS27, MRPS35, and PTCD3, matching the mitochondrial-ribosome annotations (STRING COMPARTMENTS Mitochondrial ribosome; within-query FDR = 0.0022), (STRING Component Mitochondrial ribosome; within-query FDR = 0.0028), (STRING COMPARTMENTS Ribosomal subunit; within-query FDR = 0.0032), (STRING Keyword Ribosomal protein; within-query FDR = 0.0063), (STRING Component Ribosomal subunit; within-query FDR = 0.0081), and (STRING NetworkNeighborAL Organellar ribosome; within-query FDR = 0.0138). STRING also connects metabolic genes in biologically coherent pairs or groups, including IDH3A with PDHB and SUCLG1, HADHB with SUCLG1, DECR1 with HADHB, and respiratory-chain genes COX7A2 with NDUFC1. The SDC2–TRAPPC4 relationship is a separate high-confidence interaction and may represent a membrane-trafficking or cell-structural branch rather than the core mitochondrial signal. hu.MAP independently supports several partial complexes: mitochondrial large-ribosomal assemblies containing MRPL13 and MRPL55 (hu.MAP huMAP3_09113.1), (hu.MAP huMAP3_06589.1), (hu.MAP huMAP3_04652.1), (hu.MAP huMAP3_01856.1), (hu.MAP huMAP3_06439.1), (hu.MAP huMAP3_06550.1), (hu.MAP huMAP3_07939.1), (hu.MAP huMAP3_08458.1), (hu.MAP huMAP3_09483.1); small-ribosomal assemblies containing MRPS35, MRPS27, and PTCD3 (hu.MAP huMAP3_05807.1), (hu.MAP huMAP3_03554.1), (hu.MAP huMAP3_05954.1); and complexes linking DECR1 with TRNT1 (hu.MAP huMAP3_12301.1), (hu.MAP huMAP3_12727.1) or HADHB with SDC2 (hu.MAP huMAP3_11136.1), (hu.MAP huMAP3_13917.1). These resources show that many relationships are already established physical, functional, or database-supported associations. They strengthen the interpretation that the module contains genuine mitochondrial-ribosome and metabolic structure, but they do not demonstrate that all co-abundance edges are direct physical interactions or that the entire module is one purified complex.

**STRING interactions (score >= 0.7)**: 22 of 1081 gene pairs: COX7A2–NDUFC1 (0.725); DECR1–HADHB (0.736); HADHB–SUCLG1 (0.94); IDH3A–PDHB (0.856); IDH3A–SUCLG1 (0.902); MRPL13–MRPL45 (0.97); MRPL13–MRPL55 (0.97); MRPL13–MRPS27 (0.905); MRPL13–MRPS35 (0.995); MRPL13–PTCD3 (0.871); MRPL45–MRPL55 (0.841); MRPL45–MRPS27 (0.927); MRPL45–MRPS35 (0.898); MRPL45–PTCD3 (0.894); MRPL55–MRPS27 (0.876); MRPL55–MRPS35 (0.851); MRPL55–PTCD3 (0.824); MRPS27–MRPS35 (0.991); MRPS27–PTCD3 (0.996); MRPS35–PTCD3 (0.999); PDHB–SUCLG1 (0.821); SDC2–TRAPPC4 (0.972)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transit peptide (FDR = 1.62e-07, 19 genes); Component Mitochondrial protein-containing complex (FDR = 3.31e-06, 14 genes); COMPARTMENTS Mitochondrial protein complex (FDR = 1.15e-05, 14 genes); Keyword Mitochondrion (FDR = 1.56e-05, 21 genes); Component Mitochondrial matrix (FDR = 2.92e-05, 16 genes); COMPARTMENTS Mitochondrion (FDR = 0.00015, 21 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.00015, 14 genes); COMPARTMENTS Mitochondrial ribosome (FDR = 0.0022, 6 genes); Component Mitochondrion (FDR = 0.0028, 21 genes); Component Mitochondrial ribosome (FDR = 0.0028, 6 genes); COMPARTMENTS Ribosomal subunit (FDR = 0.0032, 6 genes); Component Mitochondrial inner membrane (FDR = 0.0032, 11 genes); Keyword Ribosomal protein (FDR = 0.0063, 6 genes); Component Ribosomal subunit (FDR = 0.0081, 6 genes); NetworkNeighborAL Organellar ribosome (FDR = 0.0138, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09113.1 (MRPL55, SUPV3L1, MRPL13; 3/72); huMAP3_06589.1 (MRPL55, SUPV3L1, MRPL13; 3/79); huMAP3_05807.1 (MRPS35, MRPS27, PTCD3; 3/81); huMAP3_03554.1 (MRPS35, PTCD3; 2/2); huMAP3_11136.1 (SDC2, HADHB; 2/16); huMAP3_12301.1 (DECR1, TRNT1; 2/26); huMAP3_05954.1 (MRPS35, PTCD3; 2/28); huMAP3_04652.1 (MRPL55, MRPL13; 2/30); huMAP3_01856.1 (MRPL55, MRPL13; 2/31); huMAP3_12727.1 (DECR1, TRNT1; 2/32); huMAP3_13917.1 (SDC2, HADHB; 2/33); huMAP3_07410.1 (SLC30A7, HM13; 2/35); huMAP3_06439.1 (MRPL55, MRPL13; 2/57); huMAP3_06550.1 (MRPL55, MRPL13; 2/62); huMAP3_06247.1 (SLC30A7, HM13; 2/65); huMAP3_07939.1 (MRPL55, MRPL13; 2/68); huMAP3_08458.1 (MRPL55, MRPL13; 2/70); huMAP3_09483.1 (MRPL55, MRPL13; 2/74)

### Novelty

The biological components are not a wholly new discovery. Mitochondrial ribosomes, mitochondrial translation, respiratory metabolism, and the represented metabolic enzymes are already well established, and many of the central relationships are present in STRING and hu.MAP. The potentially novel result is the conserved co-abundance organization of these genes across autonomic nervous system and brain, especially the way mitochondrial translation, matrix metabolism, membrane organization, and selected trafficking genes appear together. However, this should be described as a new systems-level association rather than a newly discovered molecular complex or mechanism. Absence of an edge from STRING or hu.MAP is not evidence of novelty, because database coverage, assay context, and complex incompleteness can all limit detection. Demonstrating novelty would require comparison with independent tissue cohorts, preservation testing, cell-type-aware analyses, and experimental validation of the module-level coordination.

**Hypothesis.** Hypothesis: the module represents a conserved mitochondrial resilience program in neural and autonomic tissues. Coordinated abundance of mitochondrial ribosomal proteins and PTCD3 may support mitochondrial translation, while GCSH, PDHB, IDH3A, SUCLG1, HADHB, DECR1, and respiratory-chain components provide substrates, reducing power, and energy flux for oxidative metabolism. IMMT may connect this program to inner-membrane and cristae organization, and SUPV3L1, TRNT1, and MGME1 may maintain mitochondrial RNA and genome quality. Under this model, the shared co-abundance signal reflects coordinated control of mitochondrial protein production, energy generation, and organelle quality rather than a single physical complex. The hypothesis predicts that module activity should track mitochondrial respiratory capacity and translation in relevant neural or autonomic cell populations, but the co-abundance data alone do not establish directionality or causation.

### Important genes

#### MRPL13

- **Related proteins** (co-abundance neighbors): RRP8 (0.87), BOP1 (0.86), IVNS1ABP (0.85), MRPL45 (0.82); STRING partners: MRPL45 (0.97), MRPL55 (0.97), MRPS27 (0.905), MRPS35 (0.995), PTCD3 (0.871)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_09113.1, huMAP3_06589.1, huMAP3_04652.1, huMAP3_01856.1, huMAP3_06439.1, huMAP3_06550.1, huMAP3_07939.1, huMAP3_08458.1, huMAP3_09483.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein L13. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.357); asthma (0.196); refractive error (0.178); pathological myopia (0.138); Abnormality of the immune system (0.133)
- **Europe PMC papers**: 478
- **Why important**: MRPL13 is a highly connected module member and a central component of the mitochondrial-ribosome cluster. It appears in every primary mitochondrial-ribosome and ribosome-related enrichment listed in the fact sheet, including (GO:CC mitochondrial matrix; q_global = 0.00102) through (GO:CC mitochondrial ribosome; q_global = 0.0367). It has strong STRING relationships with MRPL45, MRPL55, MRPS27, MRPS35, and PTCD3, and it recurs across many hu.MAP mitochondrial large-ribosomal complexes (hu.MAP huMAP3_09113.1), (hu.MAP huMAP3_06589.1), (hu.MAP huMAP3_04652.1), (hu.MAP huMAP3_01856.1), (hu.MAP huMAP3_06439.1), (hu.MAP huMAP3_06550.1), (hu.MAP huMAP3_07939.1), (hu.MAP huMAP3_08458.1), and (hu.MAP huMAP3_09483.1). Its established function is mitochondrial translation, and its disease-resource associations include neurodegenerative disease and immune-system abnormality. Its literature volume is substantial, supporting it as a well-characterized anchor rather than an obscure connector.
- **Conclusion**: Established evidence supports MRPL13 as a structural and functional anchor of the mitochondrial translation part of the module. The module-level data support coordinated mitoribosome abundance, but they do not show that MRPL13 drives the shared tissue program or that its disease associations explain the co-abundance pattern.

#### PTCD3

- **Related proteins** (co-abundance neighbors): RP2 (0.86), MRPS35 (0.85), HIBADH (0.84); STRING partners: MRPL13 (0.871), MRPL45 (0.894), MRPL55 (0.824), MRPS27 (0.996), MRPS35 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_05807.1, huMAP3_03554.1, huMAP3_05954.1
- **Function (MyGene.info)**: pentatricopeptide repeat domain 3. Enables rRNA binding activity and ribosomal small subunit binding activity. Involved in mitochondrial translation. Located in several cellular components, including cytosol; mitochondrion; and nucleoplasm. Implicated in combined oxidative phosphorylation deficiency 51. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: combined oxidative phosphorylation deficiency 51 (0.678); mixed connective tissue disease (0.230); hereditary disease (0.193); alcohol drinking (0.110); posterior cortical atrophy (0.074)
- **Europe PMC papers**: 308
- **Why important**: PTCD3 is represented in all primary enrichment terms (GO:CC mitochondrial matrix; q_global = 0.00102) through (GO:CC mitochondrial ribosome; q_global = 0.0367), has strong STRING relationships with the mitochondrial ribosomal proteins, and occurs in hu.MAP small-ribosomal complexes (hu.MAP huMAP3_05807.1), (hu.MAP huMAP3_03554.1), and (hu.MAP huMAP3_05954.1). Its established annotation includes rRNA binding, small-subunit binding, and mitochondrial translation, and it is implicated in combined oxidative phosphorylation deficiency. It therefore provides a mechanistic bridge between mitochondrial RNA handling and assembly or function of the mitoribosome. Its network position is less hub-like than the leading large-subunit genes, but its annotation is unusually direct for the core interpretation.
- **Conclusion**: Established evidence identifies PTCD3 as a mitochondrial translation and rRNA-associated component that reinforces the module's mitoribosomal interpretation. It is plausible, but not demonstrated, that PTCD3 coordinates RNA processing with respiratory capacity in the shared tissue state.

#### GCSH

- **Related proteins** (co-abundance neighbors): MRPL55 (0.87), MRPL45 (0.85), NCEH1 (0.83), COX7A2 (0.83), PDHB (0.83), GRK3 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycine cleavage system protein H. Degradation of glycine is brought about by the glycine cleavage system, which is composed of four mitochondrial protein components: P protein (a pyridoxal phosphate-dependent glycine decarboxylase), H protein (a lipoic acid-containing protein), T protein (a tetrahydrofolate-requiring enzyme), and L protein (a lipoamide dehydrogenase). The protein encoded by this gene is the H protein, which transf…
- **Diseases (Open Targets)**: multiple mitochondrial dysfunctions syndrome 7 (0.710); glycine encephalopathy (0.692); neurodegenerative disease (0.482); atypical glycine encephalopathy (0.370); neonatal glycine encephalopathy (0.370)
- **Europe PMC papers**: 1061
- **Why important**: GCSH is a well-connected metabolic member linking MRPL45, PDHB, COX7A2, and other module genes. It contributes to the primary mitochondrial matrix and mitochondrion enrichments (GO:CC mitochondrial matrix; q_global = 0.00102) and (GO:CC mitochondrion; q_global = 0.00661) and to several supplementary mitochondrial terms (STRING Keyword Transit peptide; within-query FDR = 1.62e-07), (STRING Keyword Mitochondrion; within-query FDR = 1.56e-05), (STRING Component Mitochondrial matrix; within-query FDR = 2.92e-05), (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.00015), (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.00015), and (STRING Component Mitochondrion; within-query FDR = 0.0028). Its established function in the glycine-cleavage system places it at the interface of amino-acid catabolism, one-carbon-related metabolism, and mitochondrial energy production. HPA reports tissue enhancement in brain, and disease resources associate it with mitochondrial dysfunction and glycine encephalopathy. Its literature volume is substantial.
- **Conclusion**: Established evidence supports GCSH as a metabolically informative bridge between mitochondrial matrix chemistry and the translation-heavy core. Its brain enhancement makes it relevant to the tissue pair, but the data do not establish brain-specific regulation or a causal role in the module.

#### SUCLG1

- **Related proteins** (co-abundance neighbors): IDH3A (0.87), IMMT (0.86), NDUFC1 (0.85), DECR1 (0.83), RP2 (0.83); STRING partners: HADHB (0.94), IDH3A (0.902), PDHB (0.821)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase GDP/ADP-forming subunit alpha. This gene encodes the alpha subunit of the heterodimeric enzyme succinate coenzyme A ligase. This enzyme is targeted to the mitochondria and catalyzes the conversion of succinyl CoA and ADP or GDP to succinate and ATP or GTP. Mutations in this gene are the cause of the metabolic disorder fatal infantile lactic acidosis and mitochondrial DNA depletion. [provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome 9 (0.811); neurodegenerative disease (0.520); mitochondrial DNA depletion syndrome (0.507); post term pregnancy (0.280); lysosomal storage disease (0.245)
- **Europe PMC papers**: 1277
- **Why important**: SUCLG1 occupies a central metabolic position in the module and connects IDH3A, HADHB, NDUFC1, DECR1, and IMMT in the co-abundance network. It contributes to (GO:CC mitochondrial matrix; q_global = 0.00102) and (GO:CC mitochondrion; q_global = 0.00661), and STRING supports relationships with HADHB, IDH3A, and PDHB. Its established function in succinate-CoA ligase links succinyl-CoA metabolism to nucleotide triphosphate production and the tricarboxylic acid cycle. It is associated with mitochondrial DNA depletion syndromes and neurodegenerative disease, and it has a substantial literature base.
- **Conclusion**: Established evidence supports SUCLG1 as a metabolic backbone connecting matrix energy metabolism with the mitochondrial structural and translational signal. The hypothesis that it couples mitochondrial nucleotide supply to mitoribosome activity is biologically plausible but not directly shown by this module.

#### IMMT

- **Related proteins** (co-abundance neighbors): RP2 (0.88), LYSMD2 (0.86), SUCLG1 (0.86), ABHD10 (0.85), PDHB (0.82), IDH3A (0.82), NCEH1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inner membrane mitochondrial protein. Enables RNA binding activity. Involved in cristae formation. Located in mitochondrial inner membrane. Part of MICOS complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); multinodular goiter (0.196); alcohol drinking (0.190); breast cancer (0.094); neoplasm (0.087)
- **Europe PMC papers**: 933
- **Why important**: IMMT has among the strongest network connectivity in the module and is linked to SUCLG1, ABHD10, PDHB, IDH3A, and other mitochondrial genes. It contributes to mitochondrial protein-containing complex and mitochondrion enrichment (GO:CC mitochondrial protein-containing complex; q_global = 0.00532) and (GO:CC mitochondrion; q_global = 0.00661), with additional support from the mitochondrial complex and inner-membrane STRING annotations (STRING Component Mitochondrial protein-containing complex; within-query FDR = 3.31e-06), (STRING COMPARTMENTS Mitochondrial protein complex; within-query FDR = 1.15e-05), (STRING Keyword Mitochondrion; within-query FDR = 1.56e-05), (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.00015), (STRING Component Mitochondrion; within-query FDR = 0.0028), and (STRING Component Mitochondrial inner membrane; within-query FDR = 0.0032). Its established role in MICOS, cristae formation, and inner-membrane organization gives the module a structural dimension beyond translation and metabolism. HPA reports mitochondrial localization and brain protein detection, while disease resources include neurodegenerative disease.
- **Conclusion**: Established evidence supports IMMT as a structural mitochondrial anchor that may help explain why membrane organization is co-abundant with matrix metabolism and mitochondrial translation. A role for IMMT in organizing the entire module is a hypothesis, not a demonstrated physical or regulatory relationship.

## Module 1

**Tissue pair**: autonomic_nervous_system and brain  
**Genes (45)**: BZW2, AKAP8, ARIH1, ASS1, ATRX, BCLAF1, BCS1L, DLG1, EDC4, EIPR1, EPS15, ESS2, FAM107B, FAF1, FEN1, GAPVD1, GDAP1L1, HMOX2, IDH1, EIF4G3, MSH2, MTMR2, NES, NUCB1, OSBPL3, DDOST, PIP4K2C, POGZ, PPIL3, ERC1, RBBP4, UPF2, RFC2, RFC3, RPL26L1, SF3A1, VIPAS39, SPIN1, EPRS1, TP53BP1, TSG101, UBE3A, VPS4B, XRN2, ZDHHC5

### Function

No GO/KEGG term passed global correction, and STRING reports no functional enrichment. The most coherent interpretation is a mixed intracellular maintenance module rather than a single established pathway. Its components span DNA replication and repair, chromatin and transcriptional regulation, RNA processing and translation, vesicle and endosomal trafficking, phosphoinositide metabolism, lipid handling, mitochondrial biology, and neuronal structural or synaptic functions. The strongest mechanistic thread is a DNA-replication and genome-surveillance branch involving MSH2, FEN1, RFC2, RFC3, TP53BP1, ATRX, and related chromatin factors. A second branch involves membrane trafficking, endosomal sorting, autophagy, and receptor or protein localization, including TSG101, VPS4B, EIF4G3, ZDHHC5, PIP4K2C, and related genes. The module should therefore be described as a co-abundance signature of general cellular maintenance with a possible neural-cell context, not as proof of one unified biological pathway.

**Cell composition.** The module is not dominated by secreted or plasma proteins: only NUCB1 is annotated as secreted to blood, while the remaining genes are intracellular or membrane-associated. It is also not strongly blood-cell specific. Most genes have low immune-cell specificity, only ASS1 is immune-cell enriched, and several genes show enhancement in neutrophils or other specialized cell types without establishing a blood origin. HPA tissue evidence is broadly distributed, with many genes having low tissue specificity and smaller subsets enhanced in brain, muscle, liver, heart, kidney, lymphoid tissue, or reproductive cell types. Protein detection in brain is widespread among the tested genes, although this does not establish brain-specific expression or neuronal causality. The shared autonomic-nervous-system and brain signal could therefore reflect broadly expressed housekeeping or stress-sensitive intracellular programs present in shared cell populations, with a possible contribution from neural cells rather than a secreted blood contaminant.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a connected DNA maintenance branch: MSH2 links to FEN1, RFC2, and RFC3; FEN1 links to RFC2, RFC3, and TP53BP1; and RFC2 and RFC3 are strongly linked. STRING also supports ATRX with BCLAF1, IDH1, and TP53BP1; TSG101 with VPS4B; UPF2 with XRN2; DLG1 with UBE3A; EPRS1 with RPL26L1; and MTMR2 with PIP4K2C. These relationships indicate that parts of the module recapitulate known molecular biology rather than being entirely arbitrary co-abundance associations. hu.MAP independently places RFC2 and RFC3 together across multiple replication-factor-complex assemblies (hu.MAP huMAP3_07313.1) through (hu.MAP huMAP3_10568.1) and (hu.MAP huMAP3_12727.1), and places ATRX and POGZ together in a chromatin-associated complex (hu.MAP huMAP3_11539.1). However, most complexes contribute only a pair of module members, so the data support embedded known subcomplexes rather than a single experimentally established complex containing the whole module.

**STRING interactions (score >= 0.7)**: 15 of 990 gene pairs: ATRX–BCLAF1 (0.769); ATRX–IDH1 (0.888); ATRX–TP53BP1 (0.742); DLG1–UBE3A (0.974); EPRS1–RPL26L1 (0.894); FEN1–MSH2 (0.948); FEN1–RFC2 (0.939); FEN1–RFC3 (0.947); FEN1–TP53BP1 (0.729); MSH2–RFC2 (0.884); MSH2–RFC3 (0.77); MTMR2–PIP4K2C (0.702); RFC2–RFC3 (0.999); TSG101–VPS4B (0.959); UPF2–XRN2 (0.784)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07313.1 (RFC2, RFC3; 2/9); huMAP3_02854.1 (RFC2, RFC3; 2/10); huMAP3_08854.1 (RFC2, RFC3; 2/10); huMAP3_14232.1 (RFC2, RFC3; 2/10); huMAP3_08879.1 (RFC2, RFC3; 2/11); huMAP3_12839.1 (RFC2, RFC3; 2/11); huMAP3_00703.1 (RFC2, RFC3; 2/12); huMAP3_10568.1 (RFC2, RFC3; 2/13); huMAP3_11539.1 (ATRX, POGZ; 2/32); huMAP3_12727.1 (RFC2, RFC3; 2/32)

### Novelty

The module is not established as a new molecular complex or pathway on the presented evidence. Several internal relationships are already known through STRING and hu.MAP, especially the RFC2–RFC3 replication-factor relationship, the MSH2–FEN1–RFC connections, the TSG101–VPS4B trafficking relationship, and the ATRX–POGZ complex membership. Its potentially novel aspect is the reproducible co-abundance of these otherwise distinct functional branches across autonomic nervous system and brain tissue groups. That observation is hypothesis-generating, but absence from STRING or hu.MAP cannot by itself demonstrate novelty. Independent replication, preservation across datasets, cell-type deconvolution, and perturbation or protein-level validation would be needed before claiming a new biological module.

**Hypothesis.** Hypothesis: the shared module reflects a coordinated cellular resilience program in neural or shared tissue cell populations. In this model, genome surveillance and repair involving MSH2, FEN1, RFC2, RFC3, TP53BP1, and ATRX is coupled through transcriptional, RNA-processing, translational, ubiquitin, and membrane-trafficking machinery to maintain cell survival and proteostasis. TSG101, VPS4B, ZDHHC5, PIP4K2C, and EIF4G3 could connect protein or membrane turnover with signaling and translation, while GDAP1L1, MTMR2, ERC1, DLG1, and UBE3A could provide a neural structural or synaptic context. This is a mechanistic hypothesis, not a demonstrated causal pathway; the lack of globally significant GO/KEGG enrichment argues for cautious interpretation.

### Important genes

#### GDAP1L1

- **Related proteins** (co-abundance neighbors): OSBPL3 (0.88), FAM107B (0.88), MSH2 (0.86), TSG101 (0.85), TP53BP1 (0.83), EDC4 (0.82), DDOST (0.81), NUCB1 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ganglioside induced differentiation associated protein 1 like 1. The ganglioside GD3 synthase causes cell differentiation with neurite sprouting when transfected into the mouse neuroblastoma cell line Neuro2a. After differentiation, the expression of several genes is upregulated, including one that encodes a protein termed ganglioside-induced differentiation-associated protein 1 (Gdap1). A similar gene was found in humans, and mutations in the human gene are as…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.427); ulcerative colitis (0.089); cervical carcinoma (0.020); diabetes mellitus (0.020); ataxia telangiectasia (0.018)
- **Europe PMC papers**: 148
- **Why important**: GDAP1L1 is the principal network hub by weighted connectivity in the supplied subgraph and links genes from several otherwise separate branches, including MSH2, TP53BP1, TSG101, OSBPL3, EDC4, DDOST, and NUCB1. HPA places it in the endoplasmic reticulum, with group enrichment in brain and pituitary gland and detection in brain. Its name and supplied annotation connect it to ganglioside-associated neuronal differentiation biology, and its disease context includes Charcot-Marie-Tooth disease through similarity to GDAP1-related biology. Its literature volume is modest relative to the major DNA-repair genes, making it a useful candidate for module-specific follow-up.
- **Conclusion**: Established evidence supports GDAP1L1 as a highly connected, brain-associated intracellular candidate that bridges membrane or endoplasmic-reticulum biology with DNA-maintenance and trafficking-related genes. It is plausible that GDAP1L1 helps define the neural context of the module, but the supplied data do not establish that it mechanistically regulates the connected genes.

#### MSH2

- **Related proteins** (co-abundance neighbors): GDAP1L1 (0.86), FEN1 (0.86), NES (0.82), SF3A1 (0.81), BZW2 (0.81); STRING partners: FEN1 (0.948), RFC2 (0.884), RFC3 (0.77)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutS homolog 2. This locus is frequently mutated in hereditary nonpolyposis colon cancer (HNPCC). When cloned, it was discovered to be a human homolog of the E. coli mismatch repair gene mutS, consistent with the characteristic alterations in microsatellite sequences (RER+ phenotype) found in HNPCC. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: Lynch syndrome (0.891); colorectal cancer (0.776); mismatch repair cancer syndrome (0.775); Muir-Torre syndrome (0.752); mismatch repair cancer syndrome 1 (0.740)
- **Europe PMC papers**: 22581
- **Why important**: MSH2 is a central member of the DNA surveillance branch and connects within the module to GDAP1L1, FEN1, NES, SF3A1, and BZW2. STRING independently supports its relationships with FEN1, RFC2, and RFC3. Its established function is mismatch repair and DNA damage tolerance, and its disease associations strongly include Lynch syndrome and colorectal cancer. It also has a very large literature base, making its biology particularly well established.
- **Conclusion**: Established evidence supports MSH2 as an anchor of a genuine DNA-repair subnetwork within the module. Its presence does not prove that the whole module is a DNA-repair module; instead, it identifies one well-supported component that may reflect genome maintenance or cell-state composition.

#### RFC2

- **Related proteins** (co-abundance neighbors): RFC3 (0.85), FAF1 (0.83); STRING partners: FEN1 (0.939), MSH2 (0.884), RFC3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_07313.1, huMAP3_02854.1, huMAP3_08854.1, huMAP3_14232.1, huMAP3_08879.1, huMAP3_12839.1, huMAP3_00703.1, huMAP3_10568.1, huMAP3_12727.1
- **Function (MyGene.info)**: replication factor C subunit 2. This gene encodes a member of the activator 1 small subunits family. The elongation of primed DNA templates by DNA polymerase delta and epsilon requires the action of the accessory proteins, proliferating cell nuclear antigen (PCNA) and replication factor C (RFC). Replication factor C, also called activator 1, is a protein complex consisting of five distinct subunits. This gene encodes the 40 kD s…
- **Diseases (Open Targets)**: neurodegenerative disease (0.509); ovarian dysfunction (0.202); hypotensive disorder (0.170); hepatocellular carcinoma (0.087); colorectal carcinoma (0.085)
- **Europe PMC papers**: 1272
- **Why important**: RFC2 is part of the replication factor C complex and is connected to RFC3 within the module. STRING supports RFC2 with RFC3, FEN1, and MSH2, while hu.MAP repeatedly places RFC2 and RFC3 in replication-factor-complex assemblies (hu.MAP huMAP3_07313.1) through (hu.MAP huMAP3_10568.1) and (hu.MAP huMAP3_12727.1). Its supplied function includes DNA replication, replication-checkpoint signaling, DNA repair, and stimulation of DNA polymerase activity. Its disease associations include neurodegenerative disease and several cancers, with a substantial literature base.
- **Conclusion**: Established evidence supports RFC2 as a core representative of the module's replication and repair branch, strengthened by agreement between the co-abundance network, STRING, and hu.MAP. The data support a shared DNA-maintenance signal but do not show that RFC2 drives the cross-tissue module.

#### TSG101

- **Related proteins** (co-abundance neighbors): GDAP1L1 (0.85), EIF4G3 (0.84), VIPAS39 (0.81), ARIH1 (0.80); STRING partners: VPS4B (0.959)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tumor susceptibility 101. The protein encoded by this gene belongs to a group of apparently inactive homologs of ubiquitin-conjugating enzymes. The gene product contains a coiled-coil domain that interacts with stathmin, a cytosolic phosphoprotein implicated in tumorigenesis. The protein may play a role in cell growth and differentiation and act as a negative growth regulator. In vitro steady-state expression of this tumor…
- **Diseases (Open Targets)**: HIV infectious disease (0.528); viral infectious disease (0.467); dengue disease (0.370); neurodegenerative disease (0.337); Alkalosis (0.144)
- **Europe PMC papers**: 14220
- **Why important**: TSG101 connects GDAP1L1, EIF4G3, VIPAS39, and ARIH1 in the module and has a strong STRING relationship with VPS4B. Its supplied functions include protein transport, vesicle-mediated transport, autophagy, and regulation of growth-related signaling. HPA detects it in brain, and its large literature volume makes it a well-characterized trafficking and proteostasis component. Its position provides a plausible bridge between the module's neuronal or membrane-associated genes and its intracellular maintenance genes.
- **Conclusion**: Established evidence supports TSG101 as an anchor of the module's vesicle-trafficking and proteostasis branch. It may connect endosomal turnover with cellular stress responses, but a specific role in the shared autonomic-nervous-system and brain co-abundance pattern remains a hypothesis.

#### UBE3A

- **Related proteins** (co-abundance neighbors): UPF2 (0.80); STRING partners: DLG1 (0.974)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin protein ligase E3A. This gene encodes an E3 ubiquitin-protein ligase, part of the ubiquitin protein degradation system. This imprinted gene is maternally expressed in brain and biallelically expressed in other tissues. Maternally inherited deletion of this gene causes Angelman Syndrome, characterized by severe motor and intellectual retardation, ataxia, hypotonia, epilepsy, absence of speech, and characteristic facie…
- **Diseases (Open Targets)**: Angelman syndrome (0.843); hereditary disease (0.545); Intellectual disability (0.514); Global developmental delay (0.400); neurodevelopmental disorder (0.346)
- **Europe PMC papers**: 4879
- **Why important**: UBE3A is connected to UPF2 in the module and has a strong STRING relationship with DLG1, a brain-associated scaffold gene. Its established function is E3 ubiquitin ligase activity, and the supplied annotation emphasizes maternal expression in brain and the association of maternal loss with Angelman syndrome. It has a substantial literature base and a strong neurodevelopmental disease association, making it especially relevant to a brain-shared module despite its limited local degree.
- **Conclusion**: Established evidence supports UBE3A as a biologically important neural ubiquitin-system gene whose module connection may relate to protein turnover, RNA surveillance, or synaptic scaffolding. Its low local connectivity means it should not be treated as a topological hub, and the data do not establish that this module mediates Angelman-related biology.

## Module 2

**Tissue pair**: autonomic_nervous_system and brain  
**Genes (30)**: PGD, SLC1A5, ABLIM1, CANX, CD47, CLASP1, DDX39B, ECHS1, GDAP1, GNAI3, HIBCH, PPA2, ME2, MYL6B, NDUFA10, NDUFS1, NFS1, NPY, BCKDHA, ATIC, PZP, RMDN3, SCARB2, SDHA, SFXN1, HARS2, IARS2, SYN1, TAF5, TIMM50

### Function

The strongest supported interpretation is a mitochondrial energy and biosynthetic maintenance module. (GO:CC mitochondrial matrix; q_global = 0.00623) identifies mitochondrial matrix localization through BCKDHA, ECHS1, HARS2, HIBCH, IARS2, ME2, NDUFA10, NDUFS1, NFS1, PPA2 and SDHA, while (GO:CC mitochondrion; q_global = 0.0382) extends the signal to the mitochondrion and includes CANX, GDAP1, RMDN3, SFXN1 and TIMM50. These globally corrected terms support a coherent mitochondrial rather than a narrowly neuronal annotation. The constituent functions cover respiratory electron transfer through NDUFA10, NDUFS1 and SDHA; iron-sulfur cluster production through NFS1; branched-chain amino-acid and fatty-acid related metabolism through BCKDHA, HIBCH and ECHS1; mitochondrial translation through HARS2 and IARS2; pyrophosphate and membrane-potential regulation through PPA2; metabolite and serine transport through SFXN1; and mitochondrial protein import through TIMM50. GDAP1 and SYN1 provide a neuronal and mitochondrial-dynamics or synaptic context, whereas NPY provides a neuropeptide signaling context. Thus the module is best described as a conserved mitochondrial proteostasis, respiration and substrate-utilization program with particular relevance to energetically demanding neural cells. The STRING enrichments (STRING Keyword Mitochondrion; within-query FDR = 0.00027), (STRING Keyword Transit peptide; within-query FDR = 0.00027), (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0024), (STRING DISEASES Mitochondrial metabolism disease; within-query FDR = 0.0033), (STRING Component Mitochondrial matrix; within-query FDR = 0.0192), (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.0203) and (STRING Component Mitochondrion; within-query FDR = 0.022) are concordant supplementary evidence, but they are not additional globally corrected GO or KEGG evidence.

**Cell composition.** The module does not appear to be dominated by plasma or secreted proteins: only NPY and PZP are annotated as secreted to blood, and PZP is not detected in brain by HPA. It is also not predominantly blood-cell specific. Most genes have low immune-cell specificity, although several show immune-cell enhancement or blood-cell enrichment, especially PGD and SCARB2. The HPA profile instead supports a broadly distributed cellular program with many tissue-enhanced or cell-type-enhanced genes. Brain neuronal populations are repeatedly represented, and brain protein detection is present for nearly all module genes, while SYN1 is brain tissue enriched and GDAP1 is brain tissue enhanced. The presence of genes enriched in liver, muscle, tongue, esophagus and selected immune populations means that the module is not exclusively neural. The shared signal could therefore reflect conserved mitochondrial abundance across neurons and other oxidative cell types, with some contribution from cellular composition or sample admixture. The HPA summary does not support interpreting this primarily as a blood-contamination module, but the secreted PZP-NPY branch and blood-associated PGD-SCARB2 branch warrant caution.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrial matrix | 0.00623 | BCKDHA, ECHS1, HARS2, HIBCH, IARS2, ME2, NDUFA10, NDUFS1, NFS1, PPA2, SDHA |
| GO:CC mitochondrion | 0.0382 | BCKDHA, CANX, ECHS1, GDAP1, HARS2, HIBCH, IARS2, ME2, NDUFA10, NDUFS1, NFS1, PPA2, RMDN3, SDHA, SFXN1, TIMM50 |

### STRING and hu.MAP

STRING provides a small set of high-confidence known relationships within the module. The strongest links include the CD47-SCARB2 relationship, the ECHS1-HIBCH relationship, the HARS2-IARS2 relationship, and the respiratory relationships among NDUFA10, NDUFS1 and SDHA. These links independently support several biological substructures: branched-chain or related mitochondrial metabolism, mitochondrial translation, and respiratory-chain activity. STRING functional categories (STRING Keyword Mitochondrion; within-query FDR = 0.00027), (STRING Keyword Transit peptide; within-query FDR = 0.00027), (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0024), (STRING DISEASES Mitochondrial metabolism disease; within-query FDR = 0.0033), (STRING Component Mitochondrial matrix; within-query FDR = 0.0192), (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.0203) and (STRING Component Mitochondrion; within-query FDR = 0.022) are concordant with the mitochondrial interpretation, while (STRING DISEASES Leigh disease; within-query FDR = 0.0033) links part of the module to Leigh disease in supplementary analysis. hu.MAP adds known complex context. NDUFA10 and NDUFS1 co-occur across several complex-I-related complexes (hu.MAP huMAP3_07653.1) and (hu.MAP huMAP3_02819.1) through (hu.MAP huMAP3_14878.1). HARS2 and IARS2 co-occur in (hu.MAP huMAP3_13468.1), and PPA2 also appears in (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1). ME2 and PPA2 occur in (hu.MAP huMAP3_14442.1), while ME2 and SCARB2 recur in (hu.MAP huMAP3_05184.1) and (hu.MAP huMAP3_08042.1). SLC1A5 and SFXN1 occur together in (hu.MAP huMAP3_10473.1), and ABLIM1 with MYL6B occurs in (hu.MAP huMAP3_08205.1). These observations show that parts of the co-abundance module recapitulate established molecular complexes, especially respiratory chain, mitochondrial translation and metabolic assemblies. They do not establish that every co-abundance edge is a direct physical interaction, nor that the entire module is one molecular complex.

**STRING interactions (score >= 0.7)**: 6 of 435 gene pairs: CD47–SCARB2 (0.994); ECHS1–HIBCH (0.984); HARS2–IARS2 (0.854); NDUFA10–NDUFS1 (0.999); NDUFA10–SDHA (0.793); NDUFS1–SDHA (0.995)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Mitochondrion (FDR = 0.00027, 15 genes); Keyword Transit peptide (FDR = 0.00027, 12 genes); COMPARTMENTS Mitochondrion (FDR = 0.0024, 15 genes); DISEASES Leigh disease (FDR = 0.0033, 6 genes); DISEASES Mitochondrial metabolism disease (FDR = 0.0033, 8 genes); Component Mitochondrial matrix (FDR = 0.0192, 10 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.0203, 9 genes); Component Mitochondrion (FDR = 0.022, 15 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (ME2, ATIC, PGD, PPA2; 4/57); huMAP3_13468.1 (HARS2, PPA2, IARS2; 3/99); huMAP3_07653.1 (NDUFA10, NDUFS1; 2/7); huMAP3_05184.1 (ME2, SCARB2; 2/9); huMAP3_08042.1 (ME2, SCARB2; 2/13); huMAP3_08205.1 (ABLIM1, MYL6B; 2/17); huMAP3_10473.1 (SLC1A5, SFXN1; 2/24); huMAP3_10525.1 (PPA2, IARS2; 2/33); huMAP3_02819.1 (NDUFA10, NDUFS1; 2/34); huMAP3_14018.1 (NDUFA10, NDUFS1; 2/48); huMAP3_06397.1 (NDUFA10, NDUFS1; 2/49); huMAP3_09982.1 (NDUFA10, NDUFS1; 2/49); huMAP3_09567.1 (NDUFA10, NDUFS1; 2/52); huMAP3_14878.1 (NDUFA10, NDUFS1; 2/53)

### Novelty

The module should not be claimed as a wholly new molecular pathway. Several of its relationships and functional groupings are already represented in STRING and hu.MAP, particularly respiratory-chain components, ECHS1-HIBCH, HARS2-IARS2, and the metabolic complexes containing ME2 or PPA2. The potentially novel aspect is the coordinated co-abundance of these mitochondrial, metabolic, translational, transport, neuronal and signaling genes across autonomic nervous system and brain tissue groups. That cross-tissue organization may be a new systems-level observation, but novelty cannot be inferred merely because some module edges are absent from the reference networks. Demonstrating novelty would require comparison with prior co-expression or co-abundance studies, tissue-specific mitochondrial modules, and independent datasets, followed by replication and robustness testing. The current evidence supports a biologically credible conserved module, not proof of a new molecular complex or disease mechanism.

**Hypothesis.** Hypothesis: in autonomic and central neural tissues, high energetic demand coordinates mitochondrial respiration, iron-sulfur cluster supply, amino-acid and fatty-acid substrate handling, mitochondrial translation, pyrophosphate control, metabolite import and protein quality control. This coordinated state could help sustain neuronal ion gradients, synaptic vesicle function and axonal or mitochondrial dynamics, with NPY and membrane or lysosomal genes representing tissue-specific signaling and trafficking interfaces. The hypothesis predicts that module abundance should track mitochondrial respiratory capacity and neuronal activity more strongly than blood-cell abundance, and that perturbing respiratory or mitochondrial translation components should alter the broader module. These predictions require experimental testing; the co-abundance data alone do not demonstrate causal regulation or direct biochemical coupling.

### Important genes

#### NFS1

- **Related proteins** (co-abundance neighbors): MYL6B (0.86), NDUFA10 (0.86), CD47 (0.85), HIBCH (0.81), BCKDHA (0.81), CLASP1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NFS1 cysteine desulfurase. Iron-sulfur clusters are required for the function of many cellular enzymes. The proteins encoded by this gene supply inorganic sulfur to these clusters by removing the sulfur from cysteine, creating alanine in the process. This gene uses alternate in-frame translation initiation sites to generate mitochondrial forms and cytoplasmic/nuclear forms. Selection of the alternative initiation sites is d…
- **Diseases (Open Targets)**: combined oxidative phosphorylation deficiency 52 (0.543); neurodegenerative disease (0.469); severe neonatal lactic acidosis due to NFS1-ISD11 complex deficiency (0.370); placenta praevia (0.151); coronary artery disorder (0.132)
- **Europe PMC papers**: 1560
- **Why important**: NFS1 has the highest weighted network position and connects respiratory, metabolic and structural parts of the module. It is present in the globally corrected mitochondrial terms (GO:CC mitochondrial matrix; q_global = 0.00623) and (GO:CC mitochondrion; q_global = 0.0382), and STRING supplementary terms (STRING Keyword Mitochondrion; within-query FDR = 0.00027), (STRING Keyword Transit peptide; within-query FDR = 0.00027), (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0024), (STRING DISEASES Mitochondrial metabolism disease; within-query FDR = 0.0033), (STRING Component Mitochondrial matrix; within-query FDR = 0.0192), (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.0203) and (STRING Component Mitochondrion; within-query FDR = 0.022). Its established function is cysteine desulfurase activity supplying sulfur for iron-sulfur cluster assembly, which is relevant to many mitochondrial enzymes. HPA shows brain detection and low immune-cell specificity. Its disease associations include combined oxidative phosphorylation deficiency and severe neonatal lactic acidosis linked to NFS1-ISD11 deficiency, and its literature volume is substantial.
- **Conclusion**: Established: NFS1 is a strong network anchor for mitochondrial iron-sulfur and respiratory capacity. Hypothesis: variation in NFS1 abundance may help coordinate the module by coupling iron-sulfur assembly to respiratory and metabolic demand; the module does not by itself establish that NFS1 regulates the other genes.

#### SDHA

- **Related proteins** (co-abundance neighbors): ME2 (0.86), HIBCH (0.84), SFXN1 (0.81), ECHS1 (0.81), IARS2 (0.81); STRING partners: NDUFA10 (0.793), NDUFS1 (0.995)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate dehydrogenase complex flavoprotein subunit A. This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identi…
- **Diseases (Open Targets)**: mitochondrial complex II deficiency, nuclear type 1 (0.813); pheochromocytoma/paraganglioma syndrome 5 (0.790); dilated cardiomyopathy 1GG (0.768); neurodegeneration with ataxia and late-onset optic atrophy (0.761); gastrointestinal stromal tumor (0.743)
- **Europe PMC papers**: 12756
- **Why important**: SDHA is highly connected and links ME2, HIBCH, SFXN1, ECHS1 and IARS2 in the module. It is present in (GO:CC mitochondrial matrix; q_global = 0.00623) and (GO:CC mitochondrion; q_global = 0.0382), and STRING directly connects it with NDUFA10 and NDUFS1 while also placing it in the supplementary mitochondrial and Leigh-disease categories (STRING Keyword Mitochondrion; within-query FDR = 0.00027), (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0024), (STRING DISEASES Leigh disease; within-query FDR = 0.0033), (STRING DISEASES Mitochondrial metabolism disease; within-query FDR = 0.0033) and (STRING Component Mitochondrion; within-query FDR = 0.022). Its established role is the catalytic flavoprotein subunit of succinate dehydrogenase, connecting the tricarboxylic acid cycle with respiratory electron transfer. HPA shows enhancement in heart and skeletal muscle and multiple brain cell populations. Disease associations include mitochondrial complex-II deficiency, paraganglioma-related disease, cardiomyopathy and neurodegeneration, with a very large literature.
- **Conclusion**: Established: SDHA is a biologically central bridge between mitochondrial metabolism and electron transport. Hypothesis: its co-abundance with substrate-utilization genes may reflect coordinated adjustment of oxidative phosphorylation to fuel availability in neural tissue.

#### NDUFS1

- **Related proteins** (co-abundance neighbors): CD47 (0.88), HIBCH (0.82); STRING partners: NDUFA10 (0.999), SDHA (0.995)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_07653.1, huMAP3_02819.1, huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S1. The protein encoded by this gene belongs to the complex I 75 kDa subunit family. Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Thi…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 5 (0.810); mitochondrial complex I deficiency (0.647); type 2 diabetes mellitus (0.608); Parkinson disease (0.603); diabetes mellitus (0.580)
- **Europe PMC papers**: 2567
- **Why important**: NDUFS1 is a core respiratory-complex-I subunit and is represented in both globally corrected terms (GO:CC mitochondrial matrix; q_global = 0.00623) and (GO:CC mitochondrion; q_global = 0.0382). It participates in several hu.MAP complex-I assemblies (hu.MAP huMAP3_07653.1) and (hu.MAP huMAP3_02819.1) through (hu.MAP huMAP3_14878.1), and has very strong STRING relationships with NDUFA10 and SDHA. Its established function is transfer of electrons from NADH toward ubiquinone as part of complex I. HPA shows enhancement in heart and skeletal muscle and enhancement in excitatory neurons, inhibitory neurons and choroid plexus cells. Its disease associations include nuclear complex-I deficiency and Parkinson disease, and it has a substantial literature.
- **Conclusion**: Established: NDUFS1 provides strong evidence that the module contains a respiratory-chain core. Hypothesis: its coordinated abundance with NDUFA10 and SDHA may mark preserved respiratory-chain assembly or activity across the two neural tissue groups.

#### HIBCH

- **Related proteins** (co-abundance neighbors): ECHS1 (0.86), SDHA (0.84), NDUFS1 (0.82), ME2 (0.82), NFS1 (0.81); STRING partners: ECHS1 (0.984)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3-hydroxyisobutyryl-CoA hydrolase. This gene encodes the enzyme responsible for hydrolysis of both HIBYL-CoA and beta-hydroxypropionyl-CoA. Mutations in this gene have been associated with 3-hyroxyisobutyryl-CoA hydrolase deficiency. Alternative splicing results in multiple transcript variants.[provided by RefSeq, May 2010].
- **Diseases (Open Targets)**: 3-hydroxyisobutyryl-CoA hydrolase deficiency (0.821); hereditary disease (0.476); neurodegenerative disease (0.463); Leigh syndrome (0.373); liver disorder (0.264)
- **Europe PMC papers**: 850
- **Why important**: HIBCH is highly connected and links ECHS1, SDHA, NDUFS1, ME2 and NFS1. It occurs in (GO:CC mitochondrial matrix; q_global = 0.00623) and (GO:CC mitochondrion; q_global = 0.0382) and in all listed STRING supplementary mitochondrial categories, including Leigh disease (STRING DISEASES Leigh disease; within-query FDR = 0.0033) and mitochondrial metabolism disease (STRING DISEASES Mitochondrial metabolism disease; within-query FDR = 0.0033). Its established function is hydrolysis of HIBYL-CoA and beta-hydroxypropionyl-CoA, with roles in valine and branched-chain amino-acid catabolism. The ECHS1-HIBCH relationship is a high-confidence STRING interaction. HPA detects the protein in brain, and disease associations include HIBCH deficiency, Leigh syndrome and neurodegenerative disease.
- **Conclusion**: Established: HIBCH supports a mitochondrial substrate-catabolism branch that is physically linked to ECHS1 and embedded in the broader respiratory module. Hypothesis: coordinated HIBCH and ECHS1 abundance may indicate regulation of branched-chain carbon entry into oxidative metabolism in energetically demanding neural cells.

#### GDAP1

- **Related proteins** (co-abundance neighbors): SYN1 (0.82), CD47 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ganglioside induced differentiation associated protein 1. This gene encodes a member of the ganglioside-induced differentiation-associated protein family, which may play a role in a signal transduction pathway during neuronal development. Mutations in this gene have been associated with various forms of Charcot-Marie-Tooth Disease and neuropathy. Two transcript variants encoding different isoforms and a noncoding variant have been identified for this gen…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2K (0.833); Charcot-Marie-Tooth disease type 4A (0.803); Charcot-Marie-Tooth disease recessive intermediate A (0.784); autosomal dominant Charcot-Marie-Tooth disease type 2K (0.664); Charcot-Marie-Tooth disease (0.631)
- **Europe PMC papers**: 1052
- **Why important**: GDAP1 connects the module to SYN1 and CD47 and is present in the globally corrected mitochondrial term (GO:CC mitochondrion; q_global = 0.0382) and STRING mitochondrial categories (STRING Keyword Mitochondrion; within-query FDR = 0.00027), (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0024) and (STRING Component Mitochondrion; within-query FDR = 0.022). Its established annotation includes mitochondrial fission and fusion, and it is associated with Charcot-Marie-Tooth disease and peripheral neuropathy. HPA shows brain tissue enhancement and enhancement in Bergmann glia, excitatory neurons, inhibitory neurons and cone photoreceptors. Its position is not the strongest by network connectivity, but it is important because it supplies a direct neuronal mitochondrial-dynamics interpretation and connects to the synaptic gene SYN1.
- **Conclusion**: Established: GDAP1 is a neural mitochondrial-dynamics marker that broadens the module beyond generic respiration. Hypothesis: the conserved module may coordinate mitochondrial energy production with organelle remodeling and synaptic maintenance; the network does not prove that GDAP1 mediates this coordination.

## Module 3

**Tissue pair**: autonomic_nervous_system and brain  
**Genes (6)**: GOT1, ACE, APOA1, PTPA, S100A9, TPGS1

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING enrichment. The gene set therefore does not support a specific established pathway-level annotation. Its members instead span lipid transport, inflammatory signaling, blood-pressure and peptide regulation, amino-acid metabolism, phosphatase regulation, and microtubule biology. The network is a sparse co-abundance pattern rather than a recognized functional complex. The strongest bridge is TPGS1, which co-abunds with APOA1, S100A9, GOT1, and PTPA, while GOT1 links to ACE. This supports a mixed systemic, vascular, metabolic, and cellular-composition signal more strongly than a dedicated neuronal mechanism.

**Cell composition.** The module is not predominantly a broadly expressed housekeeping set. Three genes are secreted to blood according to HPA: APOA1, S100A9, and ACE. APOA1 is liver-enriched and associated with enterocytes and hepatocytes; S100A9 is associated with classical monocytes and neutrophils; and ACE is enriched in intestine and testis and associated with enterocytes and late spermatids. HPA also identifies immune-cell enhancement or group enrichment for several members, although other members have low immune-cell specificity. In brain protein data, GOT1 and PTPA are detected, whereas APOA1, S100A9, and ACE are not detected; there is no matching autonomic-nervous-system HPA tissue result. The module could therefore reflect vascular, blood-derived, immune, or other shared cellular components in the tissue samples rather than a brain-intrinsic neuronal program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the reported high-confidence threshold, and no STRING functional enrichment was present. No hu.MAP complex contained at least two module members. Thus, the co-abundance edges are not corroborated here as known physical interactions or shared complexes. This does not invalidate the module: co-abundance can arise from coordinated expression, shared cell composition, tissue transport, or indirect regulation. It does mean that the network should not be described as a molecular complex or direct interaction pathway.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The specific cross-tissue co-abundance pattern may be a new observation because it is not represented by a detected STRING interaction network or a hu.MAP complex. However, those absences alone do not establish novelty. The individual biology is not novel: APOA1, S100A9, ACE, GOT1, PTPA, and TPGS1 are independently annotated genes with established functions and disease or physiological associations. The most defensible conclusion is that the module-level arrangement is potentially novel but presently weakly mechanistically validated and may be driven partly by sample composition.

**Hypothesis.** Hypothesis: the shared module reflects a systemic vascular and cellular-composition axis present in both tissue groups. Circulating or locally represented APOA1, S100A9, and ACE could mark blood, endothelial, epithelial, or immune contributions, while GOT1 represents metabolic activity and TPGS1 and PTPA represent intracellular structural or regulatory state. Co-abundance may therefore arise from coordinated variation in vascular or immune-associated material and metabolically active cells, rather than from direct signaling among all module members. A testable prediction is that the module will track blood or vascular-cell markers and sample-composition measures more closely than neuronal identity markers.

### Important genes

#### TPGS1

- **Related proteins** (co-abundance neighbors): APOA1 (0.90), S100A9 (0.88), GOT1 (0.86), PTPA (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tubulin polyglutamylase complex subunit 1. Predicted to enable microtubule binding activity. Predicted to be involved in protein polyglutamylation. Predicted to act upstream of or within several processes, including adult behavior; chemical synaptic transmission; and sperm axoneme assembly. Located in centrosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: sialadenitis (0.089); type 1 diabetes mellitus (0.020); cystic fibrosis (0.011); leprosy (0.011); neoplasm (0.004)
- **Europe PMC papers**: 86
- **Why important**: TPGS1 has the central network position, connecting to APOA1, S100A9, GOT1, and PTPA. MyGene.info describes it as a tubulin polyglutamylase complex subunit involved in microtubule organization and sperm axoneme assembly, with predicted links to synaptic transmission and adult behavior. Its relatively limited literature compared with the other selected genes makes its centrality especially informative, although the function remains less established.
- **Conclusion**: Established evidence supports TPGS1 as the network bridge and as a microtubule-associated protein. Hypothesis: it may coordinate a cellular-state signal linking metabolic, inflammatory, and structural variation, but the co-abundance data do not demonstrate that TPGS1 directly regulates the other genes.

#### GOT1

- **Related proteins** (co-abundance neighbors): TPGS1 (0.86), ACE (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamic-oxaloacetic transaminase 1. Glutamic-oxaloacetic transaminase is a pyridoxal phosphate-dependent enzyme which exists in cytoplasmic and mitochondrial forms, GOT1 and GOT2, respectively.  GOT plays a role in amino acid metabolism and the urea and tricarboxylic acid cycles. The two enzymes are homodimeric and show close homology. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); Parkinson disease (0.375); Alzheimer disease (0.367); lysosomal storage disease (0.356); obesity disorder (0.172)
- **Europe PMC papers**: 3793
- **Why important**: GOT1 is an internal connector between TPGS1 and ACE and has a well-established role in amino-acid, aspartate, oxaloacetate, gluconeogenic, and related metabolic processes. It is tissue-enhanced in heart muscle, skeletal muscle, and tongue, is associated with selected retinal and germ-cell populations, is detected in brain by HPA, and has extensive literature and disease links including neurodegenerative disease, Parkinson disease, and Alzheimer disease.
- **Conclusion**: Established evidence supports GOT1 as the strongest metabolic interpretation of the module and as a plausible bridge between intracellular metabolism and ACE-associated physiology. Hypothesis: its presence may reflect metabolically active or vascular-associated cells shared across the tissue samples, not necessarily a disease-specific brain mechanism.

#### APOA1

- **Related proteins** (co-abundance neighbors): TPGS1 (0.90); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is a secreted blood protein, the major protein component of HDL, with roles in cholesterol efflux, lipid transport, and lecithin cholesterol acyltransferase activity. It is liver-enriched and associated with enterocytes and hepatocytes, has very extensive literature, and is connected in the module to the central TPGS1 node. HPA reports it as not detected in brain tissue protein measurements.
- **Conclusion**: Established evidence strongly supports APOA1 as a circulating lipid-transport and sample-composition marker rather than a brain-intrinsic module effector. Hypothesis: APOA1 may contribute to the shared module through vascular or blood-derived material, and its co-abundance with TPGS1 may be indirect.

#### S100A9

- **Related proteins** (co-abundance neighbors): TPGS1 (0.88); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Group enriched; location Plasma membrane, Intermediate filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: S100 calcium binding protein A9. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: inborn error of immunity (0.370); Sepsis (0.121); neoplasm (0.119); psoriasis (0.114); cancer (0.114)
- **Europe PMC papers**: 16393
- **Why important**: S100A9 is a secreted-to-blood inflammatory protein associated with classical monocytes and neutrophils. Its annotated functions include leukocyte migration, inflammatory responses, autophagy, cell-cell signaling, and neuron projection development. It has extensive literature and disease associations involving immunity, sepsis, psoriasis, and cancer, and it connects to TPGS1 in the module.
- **Conclusion**: Established evidence supports S100A9 as an inflammatory and myeloid-associated marker. Hypothesis: its co-abundance may indicate immune-cell or blood contribution to both tissue groups; the data do not show that S100A9 directly drives the module or neuronal biology.

#### ACE

- **Related proteins** (co-abundance neighbors): GOT1 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: angiotensin I converting enzyme. This gene encodes an enzyme involved in blood pressure regulation and electrolyte balance. It catalyzes the conversion of angiotensin I into a physiologically active peptide angiotensin II. Angiotensin II is a potent vasopressor and aldosterone-stimulating peptide that controls blood pressure and fluid-electrolyte balance. This angiotensin converting enzyme (ACE) also inactivates the vasodilator p…
- **Diseases (Open Targets)**: hypertensive disorder (0.750); renal tubular dysgenesis of genetic origin (0.729); renal tubular dysgenesis (0.724); cardiovascular disorder (0.704); diabetic kidney disease (0.689)
- **Europe PMC papers**: 95248
- **Why important**: ACE is a secreted-to-blood enzyme with a central role in angiotensin maturation, blood-pressure regulation, electrolyte balance, vascular remodeling, and bradykinin inactivation. It is tissue-enhanced in intestine and testis, associated with enterocytes and late spermatids, has exceptionally extensive literature, and links to GOT1 in the network. It is not detected in brain tissue protein measurements in the supplied HPA summary.
- **Conclusion**: Established evidence supports ACE as a systemic cardiovascular and epithelial-associated component rather than a specific neuronal marker. Hypothesis: ACE may report vascular or circulating physiology shared across samples and may couple indirectly to metabolic variation represented by GOT1.

## Module 4

**Tissue pair**: autonomic_nervous_system and brain  
**Genes (42)**: AATF, HCCS, CHD4, CHERP, COIL, DDX19B, DDX46, AHCTF1, MLLT1, GAK, GRWD1, GMPS, KPNA2, IMPDH1, DTYMK, LEMD3, MCM2, MCM5, MDC1, MGMT, NHERF1, NOL10, NSUN2, NUP93, PDIA4, PLIN3, PPP4R2, PTBP1, RBM28, PDCD11, RRS1, SMC4, SNRNP40, SUPT5H, SRP72, SRRT, STAG2, TCERG1, UBR5, UFD1, UTP25, UTP4

### Function

This is a predominantly nuclear RNA and chromatin-associated module. The primary enrichment signal is nucleic-acid binding (GO:MF nucleic acid binding; q_global = 0.000422), nuclear lumen (GO:CC nuclear lumen; q_global = 0.007), RNA binding (GO:MF RNA binding; q_global = 0.0235), and nucleoplasm (GO:CC nucleoplasm; q_global = 0.0371). Together with the gene annotations, the module is most consistent with coordinated RNA processing, spliceosome and small-nuclear-ribonucleoprotein biology, nucleolar ribosomal-RNA maturation, transcriptional regulation, and genome-maintenance functions. The signal is not limited to one pathway: ribosome biogenesis and RNA splicing are prominent, while DNA replication, DNA-damage response, chromatin remodeling, nuclear transport, and transcription elongation form connected secondary themes. The module therefore appears to represent a general nuclear gene-expression and genome-integrity program rather than a tissue-specific neuronal pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only a small minority are annotated as secreted, and most proteins are intracellular. HPA indicates broadly distributed expression for most genes, with many showing low tissue specificity and strong representation of cell-type-enhanced rather than tissue-exclusive patterns. Brain protein detection is widespread among the measured genes, whereas autonomic-nervous-system protein evidence is unavailable in the supplied HPA summary. Several genes show enrichment in reproductive, erythroid, myeloid, renal, or other proliferative cell types, including erythrocyte progenitors and myeloid cells, but the module overall has low immune-cell specificity. Thus, blood contamination is not the leading interpretation, although shared proliferative or broadly expressed cell populations could contribute. The module should not be interpreted as a neuron-specific program solely because it is shared by autonomic nervous system and brain.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleic acid binding | 0.000422 | AATF, AHCTF1, CHD4, CHERP, COIL, DDX19B, DDX46, GRWD1, IMPDH1, KPNA2, LEMD3, MCM2, MCM5, MGMT, NOL10, NSUN2, PDCD11, PDIA4, PTBP1, RBM28, RRS1, SMC4, SNRNP40, SRP72, SRRT, SUPT5H, TCERG1, UBR5, UTP25, UTP4 |
| GO:CC nuclear lumen | 0.007 | AATF, AHCTF1, CHD4, CHERP, COIL, DDX19B, DDX46, GRWD1, KPNA2, MCM2, MCM5, MDC1, MGMT, MLLT1, NOL10, NSUN2, NUP93, PDCD11, PPP4R2, PTBP1, RBM28, RRS1, SMC4, SNRNP40, SRRT, STAG2, SUPT5H, TCERG1, UBR5, UFD1, UTP25, UTP4 |
| GO:MF RNA binding | 0.0235 | AATF, CHERP, COIL, DDX19B, DDX46, GRWD1, IMPDH1, KPNA2, NOL10, NSUN2, PDCD11, PDIA4, PTBP1, RBM28, RRS1, SNRNP40, SRP72, SRRT, SUPT5H, TCERG1, UBR5, UTP25, UTP4 |
| GO:CC nucleoplasm | 0.0371 | AATF, AHCTF1, CHD4, CHERP, COIL, DDX19B, DDX46, GRWD1, KPNA2, MCM2, MCM5, MDC1, MGMT, MLLT1, NSUN2, PDCD11, PPP4R2, PTBP1, RRS1, SMC4, SNRNP40, SRRT, STAG2, SUPT5H, TCERG1, UBR5, UFD1, UTP25, UTP4 |

### STRING and hu.MAP

STRING supports a structured but incomplete molecular network. Strong known relationships connect AATF, NOL10, PDCD11, UTP4, UTP25, RBM28, RRS1, and GRWD1, consistent with nucleolar and ribosomal-RNA maturation machinery. MCM2 and MCM5 form a known replication-associated pair, while SNRNP40 connects with TCERG1 and the module contains additional established links involving splicing, transcription, chromatin, and nuclear-pore proteins. hu.MAP independently identifies spliceosomal complexes containing COIL, DDX46, and SNRNP40, and several replication complexes containing MCM2 and MCM5. A separate hu.MAP complex contains NHERF1 and GMPS. These observations show that parts of the module recapitulate known molecular assemblies, especially spliceosome-related, nucleolar, and replication-associated machinery. However, many co-abundance edges lack a corresponding high-confidence STRING or hu.MAP relationship. The network therefore combines established physical or functional submodules with tissue-level coordination that may reflect shared regulation, shared cellular state, or indirect dependencies.

**STRING interactions (score >= 0.7)**: 39 of 861 gene pairs: AATF–GRWD1 (0.727); AATF–NOL10 (0.999); AATF–PDCD11 (0.989); AATF–RBM28 (0.722); AATF–UTP25 (0.724); AATF–UTP4 (0.997); AHCTF1–NUP93 (0.989); CHD4–SRRT (0.76); CHERP–DDX46 (0.859); DDX46–TCERG1 (0.927); GMPS–IMPDH1 (0.999); GRWD1–NOL10 (0.916); GRWD1–NSUN2 (0.71); GRWD1–PDCD11 (0.929); GRWD1–RBM28 (0.873); GRWD1–RRS1 (0.926); GRWD1–UTP4 (0.917); MCM2–MCM5 (0.999); MCM5–SMC4 (0.785); MLLT1–SUPT5H (0.936); NOL10–PDCD11 (0.997); NOL10–RBM28 (0.892); NOL10–RRS1 (0.763); NOL10–UTP25 (0.79); NOL10–UTP4 (0.999); PDCD11–RBM28 (0.976); PDCD11–RRS1 (0.786); PDCD11–UTP25 (0.973); PDCD11–UTP4 (0.999); PPP4R2–SUPT5H (0.814); PTBP1–SRRT (0.78); RBM28–RRS1 (0.915); RBM28–UTP25 (0.757); RBM28–UTP4 (0.937); RRS1–UTP4 (0.739); SMC4–STAG2 (0.772); SNRNP40–TCERG1 (0.973); SRRT–TCERG1 (0.839); UTP25–UTP4 (0.886)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Nucleus (FDR = 0.00021, 34 genes); COMPARTMENTS Nuclear lumen (FDR = 0.00021, 24 genes); Function Nucleic acid binding (FDR = 0.00028, 30 genes); Keyword Nucleus (FDR = 0.00057, 32 genes); Component Nuclear lumen (FDR = 0.0023, 32 genes); COMPARTMENTS Nucleolus (FDR = 0.0027, 14 genes); Component Nucleoplasm (FDR = 0.0099, 29 genes); Function RNA binding (FDR = 0.0103, 23 genes); Function Organic cyclic compound binding (FDR = 0.0103, 34 genes); Function Heterocyclic compound binding (FDR = 0.0103, 34 genes); Keyword Isopeptide bond (FDR = 0.0154, 19 genes); COMPARTMENTS Intracellular organelle lumen (FDR = 0.0167, 26 genes); Component Intracellular organelle lumen (FDR = 0.02, 34 genes); COMPARTMENTS Intracellular membrane-bounded organelle (FDR = 0.0269, 39 genes); Component Nucleus (FDR = 0.0304, 35 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (COIL, DDX46, SNRNP40; 3/97); huMAP3_05529.1 (MCM5, MCM2; 2/6); huMAP3_14758.1 (MCM5, MCM2; 2/14); huMAP3_08554.1 (MCM5, MCM2; 2/15); huMAP3_11832.1 (MCM5, MCM2; 2/15); huMAP3_12180.1 (MCM5, MCM2; 2/17); huMAP3_14442.1 (NHERF1, GMPS; 2/57); huMAP3_06511.1 (COIL, DDX46; 2/79)

### Novelty

The module is unlikely to constitute a wholly new molecular complex because several of its relationships and subgroups are already represented in STRING and hu.MAP, particularly the nucleolar RNA-processing group, the spliceosomal group, and the MCM replication group. Its potentially novel aspect is the coordinated co-abundance of these established nuclear processes across autonomic nervous system and brain tissue. That cross-tissue organization is not demonstrated to be novel by absence from interaction databases, because those databases primarily capture physical interactions or curated functional links rather than tissue-pair co-abundance modules. The appropriate conclusion is that the module is a potentially novel systems-level tissue association built from largely established molecular components, requiring replication in independent cohorts and tests against cell-composition and proliferation-related confounding.

**Hypothesis.** Hypothesis: the shared module reflects a conserved nuclear maintenance state in autonomic nervous system and brain samples, coupling nucleolar ribosomal-RNA production and spliceosome activity with transcriptional elongation, nuclear transport, chromatin remodeling, DNA replication, and DNA-damage surveillance. A plausible mechanism is that cells with elevated RNA-production and proteostasis demands coordinately increase these nuclear machineries, while a subset of proliferative or repair-competent cells contributes the MCM, cohesin, chromatin, and checkpoint components. This hypothesis predicts coordinated changes in nascent RNA processing, ribosome biogenesis, DNA-damage response, and cell-state composition, but the co-abundance data alone do not establish causal regulation or a neuronal mechanism.

### Important genes

#### SNRNP40

- **Related proteins** (co-abundance neighbors): PTBP1 (0.83), PLIN3 (0.82), UTP4 (0.82), PPP4R2 (0.81), IMPDH1 (0.81), MGMT (0.81), MLLT1 (0.81), CHD4 (0.80); STRING partners: TCERG1 (0.973)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 40. This gene encodes a component of the U5 small nuclear ribonucleoprotein (snRNP) particle. The U5 snRNP is part of the spliceosome, a multiprotein complex that catalyzes the removal of introns from pre-messenger RNAs. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.530); dengue disease (0.377); X-linked lymphoproliferative syndrome (0.058); autoimmune lymphoproliferative syndrome (0.055); Familial hemophagocytic lymphohistiocytosis (0.053)
- **Europe PMC papers**: 235
- **Why important**: SNRNP40 has the strongest network position in the supplied module and connects to genes spanning RNA processing, chromatin, transcription, and nuclear functions. It is a U5 snRNP component with established roles in spliceosome assembly and pre-mRNA splicing. It is present in all primary enrichment categories (GO:MF nucleic acid binding; q_global = 0.000422), (GO:CC nuclear lumen; q_global = 0.007), (GO:MF RNA binding; q_global = 0.0235), and (GO:CC nucleoplasm; q_global = 0.0371), is supported by broad STRING nuclear and RNA-binding annotations (STRING COMPARTMENTS Nucleus; within-query FDR = 0.00021) through (STRING Component Nucleus; within-query FDR = 0.0304), and participates in a hu.MAP spliceosomal complex (hu.MAP huMAP3_08980.1). Its substantial literature base and neurodegenerative-disease association make it a strong anchor for the module's RNA-processing interpretation.
- **Conclusion**: Established evidence supports SNRNP40 as a central spliceosomal and nuclear RNA-processing component that helps explain the module. It is not established that SNRNP40 drives the cross-tissue co-abundance pattern or that it has a specific autonomic-neural role in this module.

#### AATF

- **Related proteins** (co-abundance neighbors): CHERP (0.84), UTP25 (0.83), RRS1 (0.82), GRWD1 (0.81), RBM28 (0.80); STRING partners: GRWD1 (0.727), NOL10 (0.999), PDCD11 (0.989), RBM28 (0.722), UTP25 (0.724), UTP4 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apoptosis antagonizing transcription factor. The protein encoded by this gene was identified on the basis of its interaction with MAP3K12/DLK, a protein kinase known to be involved in the induction of cell apoptosis. This gene product contains a leucine zipper, which is a characteristic motif of transcription factors, and was shown to exhibit strong transactivation activity when fused to Gal4 DNA binding domain. Overexpression of this gene i…
- **Diseases (Open Targets)**: skin neoplasm (0.147); generalized dystonia (0.116); multinodular goiter (0.115); bone fracture (0.113); neoplasm (0.107)
- **Europe PMC papers**: 6349
- **Why important**: AATF is a high-connectivity module gene and is linked to several nucleolar and RNA-processing proteins, including GRWD1, NOL10, PDCD11, RBM28, UTP25, and UTP4 in STRING. It appears in every primary GO category (GO:MF nucleic acid binding; q_global = 0.000422), (GO:CC nuclear lumen; q_global = 0.007), (GO:MF RNA binding; q_global = 0.0235), and (GO:CC nucleoplasm; q_global = 0.0371), and its nucleolar localization and annotations include small-subunit ribosomal-RNA maturation, ribosome biogenesis, unfolded-protein response, and transcriptional regulation. It also has a large literature base and disease associations involving neurodegenerative disease and dystonia-related phenotypes.
- **Conclusion**: Established evidence supports AATF as a connector between nucleolar RNA maturation and broader transcriptional or stress-related nuclear functions. Its role as a module-level regulator in brain or autonomic nervous system tissue remains a hypothesis rather than a demonstrated causal conclusion.

#### PDCD11

- **Related proteins** (co-abundance neighbors): STAG2 (0.85), DDX46 (0.82), MDC1 (0.81), GMPS (0.80); STRING partners: AATF (0.989), GRWD1 (0.929), NOL10 (0.997), RBM28 (0.976), RRS1 (0.786), UTP25 (0.973), UTP4 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 11. PDCD11 is a NF-kappa-B (NFKB1; 164011)-binding protein that colocalizes with U3 RNA (MIM 180710) in the nucleolus and is required for rRNA maturation and generation of 18S rRNA (Sweet et al., 2003 [PubMed 14624448]; Sweet et al., 2008 [PubMed 17654514]).[supplied by OMIM, Oct 2008].
- **Diseases (Open Targets)**: Back pain (0.277); insomnia (0.216); systemic lupus erythematosus (0.170); neoplasm (0.095); colorectal carcinoma (0.093)
- **Europe PMC papers**: 334
- **Why important**: PDCD11 is embedded in the strongest STRING-supported nucleolar cluster, with relationships to AATF, GRWD1, NOL10, RBM28, RRS1, UTP25, and UTP4. It occurs in all primary enrichment categories (GO:MF nucleic acid binding; q_global = 0.000422), (GO:CC nuclear lumen; q_global = 0.007), (GO:MF RNA binding; q_global = 0.0235), and (GO:CC nucleoplasm; q_global = 0.0371). Its established function in U3 RNA-associated nucleolar activity, rRNA processing, and generation of mature small-subunit rRNA provides a direct mechanistic explanation for the nucleolar and RNA-binding signal. It also links the nucleolar group to STAG2, DDX46, MDC1, and GMPS in the co-abundance graph.
- **Conclusion**: Established evidence supports PDCD11 as a core rRNA-processing component and a plausible representative of the module's nucleolar arm. The observed network does not establish that PDCD11 coordinates DNA repair, splicing, or tissue-specific physiology; those are integrative hypotheses.

#### CHD4

- **Related proteins** (co-abundance neighbors): DDX46 (0.88), NSUN2 (0.85), SNRNP40 (0.80), SUPT5H (0.80); STRING partners: SRRT (0.76)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromodomain helicase DNA binding protein 4. The product of this gene belongs to the SNF2/RAD54 helicase family. It represents the main component of the nucleosome remodeling and deacetylase complex and plays an important role in epigenetic transcriptional repression. Patients with dermatomyositis develop antibodies against this protein. Somatic mutations in this gene are associated with serous endometrial tumors. Alternative splicing result…
- **Diseases (Open Targets)**: Sifrim-Hitz-Weiss syndrome (0.810); neurodegenerative disease (0.551); hereditary disease (0.505); endometrial cancer (0.470); uterine carcinosarcoma (0.439)
- **Europe PMC papers**: 3617
- **Why important**: CHD4 connects RNA helicase and RNA-processing genes in the module and is represented in the primary nucleic-acid-binding, nuclear-lumen, and nucleoplasm terms (GO:MF nucleic acid binding; q_global = 0.000422), (GO:CC nuclear lumen; q_global = 0.007), and (GO:CC nucleoplasm; q_global = 0.0371). It is the principal component of the nucleosome-remodeling and deacetylase complex and has established functions in chromatin remodeling, transcriptional repression, and DNA repair. STRING supports links to SRRT, while the module network connects CHD4 with DDX46, NSUN2, SNRNP40, and SUPT5H. It has extensive literature and disease associations involving developmental and neurodegenerative phenotypes.
- **Conclusion**: Established evidence supports CHD4 as the module's strongest chromatin-remodeling and transcriptional-repression representative, providing a bridge between RNA metabolism and genome regulation. Its brain detection and disease associations do not prove that CHD4 explains the shared tissue module or that the module represents neuronal chromatin remodeling.

#### NSUN2

- **Related proteins** (co-abundance neighbors): CHD4 (0.85), MCM2 (0.81), NOL10 (0.81); STRING partners: GRWD1 (0.71)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP2/Sun RNA methyltransferase 2. This gene encodes a methyltransferase that catalyzes the methylation of cytosine to 5-methylcytosine (m5C) at position 34 of intron-containing tRNA(Leu)(CAA) precursors. This modification is necessary to stabilize the anticodon-codon pairing and correctly translate the mRNA. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Mar…
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.694); hereditary disease (0.518); Intellectual disability (0.489); phenylketonuria (0.470); neurodegenerative disease (0.462)
- **Europe PMC papers**: 2458
- **Why important**: NSUN2 is a nucleic-acid-binding and nuclear gene present in all primary terms (GO:MF nucleic acid binding; q_global = 0.000422), (GO:CC nuclear lumen; q_global = 0.007), (GO:MF RNA binding; q_global = 0.0235), and (GO:CC nucleoplasm; q_global = 0.0371). It catalyzes RNA cytosine methylation, contributes to tRNA modification, and is annotated in rRNA and mRNA processing and nuclear mRNA export. In the module network it connects CHD4, MCM2, and NOL10, thereby linking RNA modification with chromatin and nucleolar processes. It has substantial literature and disease associations involving intellectual disability and neurodegenerative disease.
- **Conclusion**: Established evidence supports NSUN2 as a mechanistically informative RNA-modification node that could couple RNA maturation and translation capacity to nuclear gene regulation. A direct contribution to the tissue-pair co-abundance pattern or to autonomic-neural function remains unproven.

## Module 5

**Tissue pair**: autonomic_nervous_system and brain  
**Genes (15)**: ABRACL, BRIX1, CLIC1, CYP51A1, DDX55, ERI1, EXOSC9, WDR77, PSMD13, PUS7, RFC4, RPRD1B, TCOF1, TRIM33, UAP1

### Function

The module is most consistent with a broadly expressed intracellular RNA and nucleolar maintenance program, with contributions from ribosome biogenesis, rRNA processing, RNA modification, RNA degradation, transcriptional regulation, and proteostasis. ERI1 occupies the most central position in the co-abundance graph and connects genes involved in RNA processing, ribosome assembly, proteasomal function, transcription, and metabolic processes. TCOF1, BRIX1, DDX55, and EXOSC9 provide convergent evidence for nucleolar and ribosome-related biology, while PUS7 supports RNA modification. RFC4 and RPRD1B indicate possible links to DNA replication or repair and RNA-polymerase-II regulation, respectively. CYP51A1 and UAP1 add lipid and nucleotide-sugar metabolism, so the module is not a narrowly defined single pathway. No GO or KEGG term passed global correction; therefore the functional interpretation is based on the coherent annotations of individual genes and the network structure, not on a globally significant enrichment result.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and protein detection is common in the sampled brain regions, supporting a general intracellular program that can occur in neural tissue. The cell-type annotations are heterogeneous, including reproductive, epithelial, stromal, neural-associated, and blood-related cell types, rather than identifying one consistent cellular population. Blood-cell specificity is generally low, with only an isolated immune-cell enhancement, so the module does not strongly suggest blood contamination or a plasma-protein signal. The liver and fallopian-tube tissue enhancements may reflect contributions from broadly expressed or mixed-cell programs rather than a brain-specific mechanism. Absence of matching autonomic-nervous-system HPA tissue data limits direct protein-level comparison for that tissue.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The high-confidence STRING evidence is restricted to BRIX1 with DDX55 and BRIX1 with PUS7. These relationships are biologically compatible with a nucleolar RNA-processing or ribosome-related subnetwork, but they account for only a small part of the co-abundance graph. STRING reports no functional enrichment, and hu.MAP reports no complex containing multiple module members. Thus, the module contains a small known interaction-supported core embedded in a larger set of co-abundant genes. The remaining edges should be treated as expression-level relationships, not established physical interactions or a single validated protein complex.

**STRING interactions (score >= 0.7)**: 2 of 105 gene pairs: BRIX1–DDX55 (0.931); BRIX1–PUS7 (0.713)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is plausibly a new tissue-pair co-abundance observation, but it is not evidence for a newly discovered molecular pathway. The module has a coherent but diffuse theme centered on RNA and nucleolar biology, while only the BRIX1-associated relationships are supported by the supplied STRING network and no multi-member hu.MAP complex is present. The lack of STRING or hu.MAP support for most edges does not establish novelty; it may reflect incomplete interaction knowledge or co-regulation rather than physical association. A firm claim that the module is a new finding would require comparison with prior autonomic-nervous-system and brain co-expression or co-abundance studies, independent cohorts, and experimental validation.

**Hypothesis.** Hypothesis: the shared module reflects coordinated demand for RNA maturation and ribosome-related quality control in cells represented in both autonomic nervous system and brain samples. ERI1-centered co-abundance may link rRNA maturation and RNA turnover with nucleolar assembly factors such as TCOF1, BRIX1, DDX55, and EXOSC9, while PUS7 may modulate RNA modification and translation. The association may be reinforced by common cellular stress, growth, or protein-homeostasis states, with additional genes representing transcriptional, proteasomal, sterol, and nucleotide-sugar support processes. This remains a mechanistic hypothesis because global GO/KEGG enrichment was not significant, most network edges lack interaction support, and the HPA cell-type signals are heterogeneous.

### Important genes

#### ERI1

- **Related proteins** (co-abundance neighbors): ABRACL (0.93), WDR77 (0.88), PSMD13 (0.87), TCOF1 (0.86), CLIC1 (0.86), EXOSC9 (0.83), PUS7 (0.82), UAP1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exoribonuclease 1. Enables 3'-5' exonuclease activity. Predicted to be involved in exonucleolytic trimming to generate mature 3'-end of 5.8S rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Located in cytoplasm and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: spondyloepimetaphyseal dysplasia, Guo-Campeau type (0.660); Hoxha-Aliu syndrome (0.586); neurodegenerative disease (0.478); hypertensive disorder (0.476); Abnormality of the skeletal system (0.453)
- **Europe PMC papers**: 561
- **Why important**: ERI1 is the central network gene by weighted connectivity and links most of the module's RNA-processing, nucleolar, proteasomal, and metabolic branches. Its established function is a three-prime-to-five-prime exoribonuclease involved in maturation of five-point-eight-S rRNA, rRNA processing, and histone-mRNA catabolism. It is detected in brain by HPA, has broad tissue distribution, and has substantial literature and disease associations including skeletal, developmental, and neurodegenerative contexts.
- **Conclusion**: Established evidence supports ERI1 as the strongest organizing candidate for an RNA-processing component of the module. It is plausible that ERI1 helps explain the shared co-abundance pattern, but the network does not establish that ERI1 directly regulates every connected gene or that it drives the tissue-pair association.

#### TCOF1

- **Related proteins** (co-abundance neighbors): ERI1 (0.86), RFC4 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: treacle ribosome biogenesis factor 1. This gene encodes a nucleolar protein with a LIS1 homology domain. The protein is involved in ribosomal DNA gene transcription through its interaction with upstream binding factor (UBF). Mutations in this gene have been associated with Treacher Collins syndrome, a disorder which includes abnormal craniofacial development. Multiple transcript variants encoding different isoforms have been found for…
- **Diseases (Open Targets)**: Treacher Collins syndrome 1 (0.761); Treacher-Collins syndrome (0.713); hereditary disease (0.472); neurodegenerative disease (0.459); Emery-Dreifuss muscular dystrophy 4, autosomal dominant (0.266)
- **Europe PMC papers**: 1248
- **Why important**: TCOF1 connects the central ERI1 branch to RFC4 and encodes a nucleolar factor involved in ribosome biogenesis, rRNA transcription, and neural-crest development. Its established disease association with Treacher Collins syndrome gives it strong biological and clinical relevance, and its protein is detected in brain. It also has extensive literature compared with many less characterized module members.
- **Conclusion**: Established evidence supports TCOF1 as a biologically meaningful nucleolar and ribosome-biogenesis component. Its presence supports a ribosome-related interpretation, but the module does not demonstrate that craniofacial-development mechanisms or Treacher Collins pathology are active in these tissue samples.

#### PUS7

- **Related proteins** (co-abundance neighbors): BRIX1 (0.83), ERI1 (0.82); STRING partners: BRIX1 (0.713)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pseudouridine synthase 7. Enables enzyme binding activity and pseudouridine synthase activity. Involved in several processes, including pseudouridine synthesis; regulation of hematopoietic stem cell differentiation; and regulation of mesoderm development. Located in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: intellectual developmental disorder with abnormal behavior, microcephaly, and short stature (0.784); hereditary disease (0.452); microcephaly (0.374); Intellectual disability (0.374); Atypical behavior (0.370)
- **Europe PMC papers**: 767
- **Why important**: PUS7 is connected to ERI1 and is one of the few module genes with direct STRING support through its relationship with BRIX1. It encodes a pseudouridine synthase involved in RNA modification, including tRNA and mRNA pseudouridine synthesis, and is associated with regulation of hematopoietic stem-cell differentiation. Its disease associations include developmental and intellectual-disability phenotypes, and it is detected in brain.
- **Conclusion**: Established evidence supports PUS7 as an RNA-modification component that could complement the module's rRNA-processing and ribosome-related biology. The BRIX1 connection strengthens this interpretation, but the co-abundance data do not show whether PUS7-dependent RNA modification is functionally altered.

#### BRIX1

- **Related proteins** (co-abundance neighbors): PUS7 (0.83); STRING partners: DDX55 (0.931), PUS7 (0.713)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Mitotic chromosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biogenesis of ribosomes BRX1. Enables RNA binding activity. Predicted to be involved in ribosomal large subunit assembly. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: colorectal cancer (0.077); cancer (0.077); colorectal carcinoma (0.074); deficiency anemia (0.065); sialolithiasis (0.060)
- **Europe PMC papers**: 251
- **Why important**: BRIX1 is a nucleolar ribosome large-subunit assembly factor and forms the module's most evident STRING-supported bridge, with relationships to DDX55 and PUS7. Its annotations directly connect it to rRNA processing and ribosome assembly. Although its literature volume and disease evidence are more limited than those of several other candidates, its network position is informative because it links two known RNA-related relationships.
- **Conclusion**: Established evidence supports BRIX1 as a plausible local anchor for a nucleolar RNA-processing submodule. Its apparent bridging role is compatible with the co-abundance pattern, but the absence of a hu.MAP multi-member complex means that a unified physical BRIX1 complex should not be inferred.

#### EXOSC9

- **Related proteins** (co-abundance neighbors): ERI1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exosome component 9. This gene encodes a component of the human exosome, a exoribonuclease complex which processes and degrades RNA in the nucleus and cytoplasm. This component may play a role in mRNA degradation and the polymyositis/scleroderma autoantigen complex. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: pontocerebellar hypoplasia, type 1D (0.691); neurodegenerative disease (0.510); pontocerebellar hypoplasia type 1 (0.370); pontocerebellar hypoplasia (0.341); Kabuki syndrome 2 (0.340)
- **Europe PMC papers**: 663
- **Why important**: EXOSC9 connects directly to ERI1 and encodes a component of the RNA exosome involved in nuclear and cytoplasmic RNA processing and degradation, including maturation of the three-prime end of five-point-eight-S rRNA. It is detected in brain and has established associations with pontocerebellar hypoplasia and other neurodevelopmental or neurodegenerative conditions. Its function provides an independent RNA-surveillance link to the central ERI1 signal.
- **Conclusion**: Established evidence supports EXOSC9 as a strong candidate for the RNA-processing and RNA-quality-control interpretation. Its neurological disease associations make it especially relevant to the tissue pair, but the module alone cannot establish a disease mechanism or prove that exosome activity is altered.

## Module 6

**Tissue pair**: autonomic_nervous_system and brain  
**Genes (18)**: ACLY, CLPB, COA7, CUL4A, TSFM, GMFB, INPP1, CHCHD4, PDCD4, PLCH1, PLXNA4, PAICS, PHGDH, SPTBN1, CCT5, CCT7, UBA3, XPNPEP3

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent. The module therefore does not support a single statistically established pathway-level annotation. Its gene-level evidence instead suggests a mixed intracellular program linking neuronal guidance and cytoskeletal organization with mitochondrial protein handling, mitochondrial translation and respiratory-chain assembly, phosphoinositide signaling, purine and serine metabolism, protein folding, and ubiquitin-related protein modification. PLXNA4 is the dominant co-abundance hub and is annotated for semaphorin receptor activity, axon guidance, axonogenesis, synapse assembly, and nervous-system development. The strongest directly known molecular relationships are the CCT chaperonin pairing, the CHCHD4–COA7 mitochondrial association, and the CUL4A–UBA3 association. Overall, the module is better interpreted as a coordinated cellular-maintenance and neuronal-structure signal than as evidence for a single canonical pathway.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: the HPA summary identifies only a single secreted gene, while the listed proteins are generally intracellular, mitochondrial, cytosolic, nucleoplasmic, vesicular, or membrane-associated. Most genes have low tissue specificity, with several showing cell-type enhancement across diverse tissues and cell types. Brain protein detection is widespread among the genes with available brain data, whereas autonomic-nervous-system protein data are unavailable in the supplied HPA comparison. Immune-cell specificity is low for most genes, and the module is not strongly blood-cell enriched. Enrichment for spermatid-related cell types and the presence of tissue-enhanced genes from testis, skeletal muscle, pancreas, lymphoid tissue, retina, and brain indicate a heterogeneous cellular program rather than a clean brain-specific signature. The shared module could therefore reflect broadly expressed intracellular biology present in relevant neural cells, although sample cellular composition cannot be excluded.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports three high-confidence pairwise relationships: CCT5 with CCT7, CHCHD4 with COA7, and CUL4A with UBA3. The CCT5–CCT7 relationship is especially strongly established and is reinforced by six hu.MAP complexes, (hu.MAP huMAP3_01951.1) through (hu.MAP huMAP3_14584.1), all containing both CCT subunits. Those complexes place the pair within broader CCT or TRiC chaperonin-associated assemblies containing other CCT subunits and several folding, cytoskeletal, and regulatory proteins. CHCHD4 and COA7 have a STRING relationship consistent with their mitochondrial roles in protein import and cytochrome-c-oxidase assembly. CUL4A and UBA3 have a STRING relationship consistent with ubiquitin-like protein activation and ubiquitin-ligase-associated regulation. No other module genes have reported hu.MAP complexes or STRING partners in the supplied evidence. Thus, the network contains a small core of externally supported molecular relationships, while much of the co-abundance structure, including the central position of PLXNA4, is not directly represented by these interaction resources.

**STRING interactions (score >= 0.7)**: 3 of 153 gene pairs: CCT5–CCT7 (0.999); CHCHD4–COA7 (0.739); CUL4A–UBA3 (0.853)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01951.1 (CCT5, CCT7; 2/8); huMAP3_07938.1 (CCT5, CCT7; 2/23); huMAP3_06559.1 (CCT5, CCT7; 2/25); huMAP3_09191.1 (CCT5, CCT7; 2/32); huMAP3_10656.1 (CCT5, CCT7; 2/36); huMAP3_14584.1 (CCT5, CCT7; 2/61)

### Novelty

The module-level co-abundance finding may be new because the specific cross-tissue association among these genes, particularly the central placement of PLXNA4 alongside mitochondrial, metabolic, chaperone, signaling, and cytoskeletal genes, is not established by the supplied interaction resources. However, the underlying biology is not wholly novel: CCT5–CCT7, CHCHD4–COA7, and CUL4A–UBA3 are already supported relationships, and individual genes have established functions and disease associations. Absence of STRING or hu.MAP support for the remaining edges does not demonstrate novelty, because those databases capture physical or curated molecular relationships rather than every co-abundance association. The defensible conclusion is that this is a potentially novel tissue-pair co-abundance configuration built from partly established molecular components, requiring independent replication and cell-type-aware validation.

**Hypothesis.** Hypothesis: in neural and autonomic tissues, a shared cellular state may couple semaphorin-receptor and cytoskeletal organization centered on PLXNA4 with mitochondrial proteostasis and respiratory competence represented by CHCHD4, COA7, TSFM, XPNPEP3, and CLPB. CCT-mediated folding could help maintain proteins required for neuronal structure and signaling, while phosphoinositide enzymes, metabolic enzymes, and ubiquitin-related regulators could support membrane signaling, biosynthetic demand, and quality control. This hypothesis is consistent with the co-abundance topology and gene functions, but it is not established as a unified pathway because no GO or KEGG term passed global correction and most network edges lack external interaction support.

### Important genes

#### PLXNA4

- **Related proteins** (co-abundance neighbors): ACLY (0.93), CCT5 (0.89), TSFM (0.85), CUL4A (0.83), PDCD4 (0.83), PHGDH (0.83), SPTBN1 (0.83), GMFB (0.83), PAICS (0.82), INPP1 (0.80), COA7 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plexin A4. Predicted to enable semaphorin receptor activity. Predicted to be involved in several processes, including axon guidance; positive regulation of axonogenesis; and regulation of GTPase activity. Predicted to act upstream of or within several processes, including nervous system development; regulation of axon extension involved in axon guidance; and regulation of negative chemotaxis. Predicted to be…
- **Diseases (Open Targets)**: neurodegenerative disease (0.518); mathematical ability (0.385); type 1 diabetes mellitus (0.337); attention deficit-hyperactivity disorder (0.333); substance abuse (0.332)
- **Europe PMC papers**: 1002
- **Why important**: PLXNA4 has the strongest network position in the module and connects to genes spanning chaperoning, metabolism, mitochondrial biology, cytoskeletal organization, and signaling. HPA supports enhancement in brain excitatory and inhibitory neurons as well as adrenal medulla cells, and protein is detected in brain. Its annotations include semaphorin receptor activity, axon guidance, axonogenesis, synapse assembly, and nervous-system development. It also has substantial literature coverage and disease links involving neurodegenerative and neurodevelopmental traits.
- **Conclusion**: Established evidence supports PLXNA4 as a neuronal membrane receptor involved in semaphorin-related guidance and neural development, and as the module's central co-abundance gene. The hypothesis that it coordinates the module's mitochondrial and proteostasis components is plausible from the network pattern but is not demonstrated by STRING, hu.MAP, or globally corrected enrichment.

#### CCT5

- **Related proteins** (co-abundance neighbors): PLXNA4 (0.89); STRING partners: CCT7 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_01951.1, huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is directly connected to CCT7 by STRING and occurs with CCT7 in all supplied hu.MAP complexes, making the pair the clearest externally supported molecular core. CCT5 encodes a subunit of the CCT or TRiC chaperonin, which folds proteins including actin and tubulin. It has brain protein detection, substantial literature coverage, and an association with hereditary sensory and autonomic neuropathy with spastic paraplegia.
- **Conclusion**: Established evidence supports CCT5 as a protein-folding component relevant to cytoskeletal-protein maturation and autonomic or sensory neural disease. Its co-abundance with PLXNA4 may indicate shared neuronal proteostasis or structural demand, but a direct functional link between CCT5 and PLXNA4 remains a hypothesis.

#### CCT7

- **Related proteins** (co-abundance neighbors): PAICS (0.82); STRING partners: CCT5 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_01951.1, huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 forms the strongest supported pair in the module with CCT5 and is present with CCT5 across the hu.MAP complex records. It is another CCT or TRiC chaperonin subunit involved in protein folding and stabilization, with brain protein detection and a substantial literature base. Its network placement also connects the chaperone signal to PAICS and therefore to biosynthetic metabolism.
- **Conclusion**: Established evidence supports CCT7 as part of the CCT chaperonin machinery that folds cellular proteins. Its inclusion strengthens interpretation of a proteostasis component in the module. Any proposed role in coordinating neuronal guidance or mitochondrial maintenance is inferential rather than directly established here.

#### CHCHD4

- **Related proteins** (co-abundance neighbors): COA7 (0.82), XPNPEP3 (0.81), PLCH1 (0.81); STRING partners: COA7 (0.739)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coiled-coil-helix-coiled-coil-helix domain containing 4. CHCHD4, a component of human mitochondria, belongs to a protein family whose members share 6 highly conserved cysteine residues constituting a -CXC-CX(9)C-CX(9)C- motif in the C terminus (Hofmann et al., 2005 [PubMed 16185709]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: lactic acidosis (0.333); Abnormal brain morphology (0.333); fetal growth restriction (0.333); Encephalopathy (0.333); Decreased liver function (0.333)
- **Europe PMC papers**: 351
- **Why important**: CHCHD4 is linked by STRING to COA7, and both genes form a coherent mitochondrial submodule. CHCHD4 is annotated for mitochondrial intermembrane-space protein import through the disulfide relay system, protein maturation, and respiratory-chain assembly. It has brain protein detection and disease associations involving lactic acidosis, abnormal brain morphology, fetal growth restriction, and encephalopathy.
- **Conclusion**: Established evidence supports CHCHD4 as a mitochondrial import and maturation factor relevant to respiratory-chain function. Its co-abundance with COA7 supports a mitochondrial component within the module. Whether this mitochondrial component is mechanistically coupled to PLXNA4-dependent neural signaling is a hypothesis requiring experimental testing.

#### COA7

- **Related proteins** (co-abundance neighbors): CHCHD4 (0.82), TSFM (0.81), PLXNA4 (0.80); STRING partners: CHCHD4 (0.739)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome c oxidase assembly factor 7. Located in mitochondrial intermembrane space and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: spinocerebellar ataxia, autosomal recessive, with axonal neuropathy 3 (0.799); mitochondrial disease (0.371); hereditary disease (0.187); chronic musculoskeletal pain (0.027); cerebellar ataxia (0.023)
- **Europe PMC papers**: 180
- **Why important**: COA7 is directly connected to CHCHD4 in STRING and is annotated as a cytochrome-c-oxidase assembly factor located in the mitochondrial intermembrane space and nucleoplasm. It has brain protein detection and a strong disease association with autosomal-recessive spinocerebellar ataxia with axonal neuropathy, along with broader mitochondrial-disease links.
- **Conclusion**: Established evidence supports COA7 as a mitochondrial respiratory-chain complex assembly factor with particular relevance to cerebellar and axonal disease. Its pairing with CHCHD4 makes it an important marker of the module's mitochondrial-maintenance component. A broader role in the shared autonomic and brain co-abundance pattern remains a hypothesis.

#### GMFB

- **Related proteins** (co-abundance neighbors): PLXNA4 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glia maturation factor beta. Predicted to enable Arp2/3 complex binding activity. Predicted to be involved in actin filament debranching and negative regulation of Arp2/3 complex-mediated actin nucleation. Predicted to act upstream of or within learning and locomotory behavior. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.381); neoplasm (0.081); hepatocellular carcinoma (0.078); glioma (0.077); central nervous system cancer (0.077)
- **Europe PMC papers**: 449
- **Why important**: GMFB is connected directly to the central PLXNA4 node and is tissue enhanced in brain according to HPA. It is annotated for Arp2/3-related actin regulation, actin-filament debranching, nervous-system development, learning, and locomotory behavior. Its disease-resource links include neurodegenerative disease, and its literature provides support for a neural and cytoskeletal interpretation.
- **Conclusion**: Established evidence supports GMFB as a brain-associated regulator of actin-network behavior and nervous-system biology. Its direct co-abundance relationship with PLXNA4 is consistent with a neuronal structural or guidance-related component. The possibility that GMFB connects this structural component to the module's mitochondrial and chaperone signals is a hypothesis rather than an established mechanism.

## Module 7

**Tissue pair**: autonomic_nervous_system and brain  
**Genes (18)**: ACO2, ADAM10, ALG3, NUDT2, ATP5PB, ATP5F1C, CPNE4, GLUD1, FERMT2, HDGFL3, HSPH1, LLPH, MAK16, RASA1, SFXN3, SPTAN1, AARS1, UCK2

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent, so the module should not be assigned a single statistically established pathway. Its gene annotations nevertheless suggest a mixed cellular program centered on mitochondrial energy and substrate metabolism, with contributions from amino-acid handling, oxidative metabolism, nucleotide and protein synthesis, membrane signaling, adhesion, cytoskeletal organization, and proteostasis. The strongest coherent functional thread is mitochondrial: SFXN3 supports serine import into mitochondria, GLUD1 catalyzes glutamate oxidation, ACO2 participates in the TCA cycle, and ATP5PB and ATP5F1C are ATP-synthase subunits. The remaining genes suggest that the co-abundance signal may combine energetic demand with neuronal or tissue-structural functions rather than represent a narrowly defined pathway.

**Cell composition.** The module does not look like a plasma-protein, secreted-protein, or blood-cell module. Only one gene is annotated in the secretome, most genes have low tissue specificity, and most have low immune-cell specificity. HPA protein detection is present for most genes in brain, whereas autonomic-nervous-system protein data are unavailable. Several genes show enhanced expression in muscle, tongue, kidney, liver, or brain, and many show cell-type enhancement across diverse nonimmune cell types. This breadth is compatible with a shared cellular program, such as mitochondrial activity or general neuronal and tissue maintenance, but it also means that the module could partly reflect shared cell composition or broad cellular state rather than a specialized autonomic-neural mechanism. The HPA evidence does not support a blood contamination explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The direct STRING evidence is highly limited: the only high-confidence pair is ATP5PB with ATP5F1C. Those same genes co-occur in every listed hu.MAP complex, (hu.MAP huMAP3_08716.1) through (hu.MAP huMAP3_11095.1), providing independent support that they belong to the mitochondrial ATP-synthase machinery. The other module genes have no listed STRING partners and no listed hu.MAP complex membership. Thus, ATP5PB and ATP5F1C form a known molecular anchor, while the remaining edges are primarily co-abundance relationships rather than established physical interactions. The network may therefore capture coordinated expression or shared cellular context, but it does not establish a single protein complex spanning the module.

**STRING interactions (score >= 0.7)**: 1 of 153 gene pairs: ATP5F1C–ATP5PB (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08716.1 (ATP5PB, ATP5F1C; 2/15); huMAP3_07476.1 (ATP5PB, ATP5F1C; 2/18); huMAP3_05994.1 (ATP5PB, ATP5F1C; 2/19); huMAP3_08393.1 (ATP5PB, ATP5F1C; 2/19); huMAP3_09775.1 (ATP5PB, ATP5F1C; 2/21); huMAP3_09307.1 (ATP5PB, ATP5F1C; 2/35); huMAP3_11095.1 (ATP5PB, ATP5F1C; 2/45)

### Novelty

The module may be a novel cross-tissue co-abundance pattern, but the fact sheet does not establish it as a new biological mechanism. The ATP5PB–ATP5F1C relationship and their repeated hu.MAP membership are already known, and the individual functions and disease associations of many genes are established. Conversely, the sparse STRING connectivity, absence of a shared hu.MAP complex containing most module members, lack of globally corrected GO/KEGG enrichment, and mixed functional composition leave open the possibility that the particular cross-tissue combination is under-described. Absence from STRING or hu.MAP is not evidence of novelty by itself. A novelty claim would require comparison with published co-abundance modules, tissue-specific networks, and independent datasets.

**Hypothesis.** Hypothesis: this shared module reflects coordinated mitochondrial and cellular-maintenance demand in brain and autonomic nervous system samples. Mitochondrial substrate handling through SFXN3 and GLUD1, TCA-cycle activity through ACO2, and ATP production through the ATP5PB–ATP5F1C machinery could form the energetic core. This state may be coupled to membrane signaling and neuronal or tissue architecture through ADAM10, RASA1, CPNE4, HDGFL3, FERMT2, and SPTAN1, with HSPH1 buffering proteotoxic stress. The hypothesis predicts that the module will track mitochondrial respiratory activity and cellular stress or structural remodeling, rather than a specific secreted or immune process. It remains a hypothesis because the enrichment results provide no globally corrected pathway support and most module relationships are not known physical interactions.

### Important genes

#### ATP5F1C

- **Related proteins** (co-abundance neighbors): ACO2 (0.83), SFXN3 (0.83); STRING partners: ATP5PB (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_08716.1, huMAP3_07476.1, huMAP3_05994.1, huMAP3_08393.1, huMAP3_09775.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit gamma. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: late-onset Alzheimers disease (0.350); scleritis (0.189); diaphragm disorder (0.082); glioblastoma (0.044); external ear disorder (0.042)
- **Europe PMC papers**: 306
- **Why important**: ATP5F1C is a mitochondrial ATP-synthase F1 gamma subunit and is directly connected to ATP5PB in STRING. It is also the shared module member in all listed hu.MAP complexes, making it a central molecular anchor despite its modest co-abundance connectivity. Its brain protein detection and association with late-onset Alzheimer disease provide additional relevance to the brain-containing tissue pair.
- **Conclusion**: Established evidence supports ATP5F1C as a component of oxidative phosphorylation and ATP synthesis and as part of a known ATP-synthase relationship with ATP5PB. It is reasonable to hypothesize that its module co-abundance reflects energetic demand, but the fact sheet does not show that the module represents a complete ATP-synthase complex or that ATP5F1C drives the wider network.

#### ATP5PB

- **Related proteins** (co-abundance neighbors): SFXN3 (0.86), RASA1 (0.80); STRING partners: ATP5F1C (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_08716.1, huMAP3_07476.1, huMAP3_05994.1, huMAP3_08393.1, huMAP3_09775.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase peripheral stalk-membrane subunit b. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: deficiency anemia (0.178); ocular hypotension (0.038); myasthenia gravis (0.022); ulcerative colitis (0.016); nonpapillary renal cell carcinoma (0.012)
- **Europe PMC papers**: 302
- **Why important**: ATP5PB is a mitochondrial ATP-synthase peripheral-stalk subunit and forms the module's only STRING-supported pair with ATP5F1C. Its inclusion with ATP5F1C across all listed hu.MAP complexes gives the module a well-supported oxidative-phosphorylation anchor. Its tissue-enhanced HPA pattern in skeletal muscle and tongue, together with brain protein detection, is consistent with participation in energetically demanding cells.
- **Conclusion**: Established evidence supports ATP5PB in proton-motive-force-driven mitochondrial ATP synthesis and confirms its known relationship with ATP5F1C. A broader role as the energetic hub of this cross-tissue module is a hypothesis, because the other module edges are not independently established protein interactions.

#### SFXN3

- **Related proteins** (co-abundance neighbors): ALG3 (0.86), ATP5PB (0.86), RASA1 (0.85), GLUD1 (0.83), ATP5F1C (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sideroflexin 3. Enables serine transmembrane transporter activity. Involved in serine import into mitochondrion. Located in mitochondrion. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.118); acute myeloid leukemia (0.096); hyperinsulinism due to INSR deficiency (0.081); cancer (0.077); hyperproinsulinemia (0.070)
- **Europe PMC papers**: 289
- **Why important**: SFXN3 has the strongest co-abundance connectivity in the module and links the ATP-synthase genes with ALG3, RASA1, and GLUD1. Its annotated mitochondrial serine-import function provides a plausible substrate-supply connection to energy metabolism. It is detected in brain and has substantial literature coverage, while its disease associations include neurodevelopmental disorder and metabolic conditions.
- **Conclusion**: Established evidence supports SFXN3 as a mitochondrial serine transporter and supports its prominent network position. It is plausible, but not demonstrated, that SFXN3 couples mitochondrial amino-acid import to the ATP-production and glutamate-metabolism signals in this module.

#### GLUD1

- **Related proteins** (co-abundance neighbors): ADAM10 (0.84), SFXN3 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamate dehydrogenase 1. This gene encodes glutamate dehydrogenase, which is a mitochondrial matrix enzyme that catalyzes the oxidative deamination of glutamate to alpha-ketoglutarate and ammonia. This enzyme has an important role in regulating amino acid-induced insulin secretion. It is allosterically activated by ADP and inhibited by GTP and ATP. Activating mutations in this gene are a common cause of congenital hyperin…
- **Diseases (Open Targets)**: hyperinsulinism-hyperammonemia syndrome (0.834); epilepsy (0.373); hyperinsulinemic hypoglycemia, familial, 2 (0.370); gout (0.345); familial hyperinsulinism (0.341)
- **Europe PMC papers**: 3159
- **Why important**: GLUD1 is a mitochondrial glutamate dehydrogenase connected to ADAM10 and SFXN3, placing amino-acid catabolism near both the module's mitochondrial and signaling portions. Its functions include glutamate oxidation, TCA-cycle input, and regulation of insulin secretion. It is detected in brain and has well-established links to hyperinsulinism, epilepsy, and related metabolic disease.
- **Conclusion**: Established evidence supports GLUD1 as a mitochondrial enzyme connecting glutamate metabolism with energy production. Its position supports an energetic-substrate interpretation of the module, but the co-abundance data do not prove altered glutamate flux or a causal role in autonomic or brain physiology.

#### ADAM10

- **Related proteins** (co-abundance neighbors): GLUD1 (0.84), RASA1 (0.82), HSPH1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ADAM metallopeptidase domain 10. Members of the ADAM family are cell surface proteins with a unique structure possessing both potential adhesion and protease domains. This gene encodes and ADAM family member that cleaves many proteins including TNF-alpha and E-cadherin. Alternate splicing results in multiple transcript variants encoding different proteins that may undergo similar processing. [provided by RefSeq, Feb 2016].
- **Diseases (Open Targets)**: reticulate acropigmentation of Kitamura (0.679); Alzheimer disease 18 (0.621); Alzheimer disease (0.522); dementia (0.415); schizophrenia (0.354)
- **Europe PMC papers**: 11139
- **Why important**: ADAM10 connects GLUD1 and RASA1 with HSPH1 and is the most extensively studied gene among the selected candidates. It is a membrane-associated metalloprotease involved in ectodomain cleavage, including TNF-alpha and E-cadherin, and is annotated in Notch signaling, adhesion, and proteolysis. It is detected in brain and has disease associations including Alzheimer disease and schizophrenia.
- **Conclusion**: Established evidence supports ADAM10 as a membrane protease and signaling regulator with important brain and disease relevance. Its placement beside mitochondrial genes suggests a possible link between energetic state and membrane or adhesion remodeling, but that linkage is a hypothesis rather than a demonstrated mechanism of this module.

## Module 8

**Tissue pair**: autonomic_nervous_system and brain  
**Genes (7)**: BRAF, GLOD4, HSPA13, IGFBP5, MTIF2, MAIP1, MRPL1

### Function

The module is most consistent with a mitochondrial protein-maintenance and translation-related program, with additional links to mitochondrial calcium handling, protein insertion, stress-protein processing, MAPK signaling, and extracellular growth-factor regulation. The strongest direct functional interpretation comes from the annotations of MTIF2, MRPL1, and MAIP1, which collectively implicate mitochondrial translation, ribosome function, mitochondrial membrane protein insertion, and calcium homeostasis. However, this interpretation is inferential rather than enrichment-confirmed: no GO or KEGG term passed global correction, and there are no STRING functional-enrichment terms. The module should therefore be treated as a co-abundance pattern that may connect mitochondrial proteostasis with signaling and extracellular regulation, rather than as proof of a single canonical pathway.

**Cell composition.** The module does not appear to be dominated by plasma proteins, secreted proteins, or blood-cell-enriched genes. Only IGFBP5 is annotated as secreted to blood, while HSPA13 has intracellular and membrane localization; the remaining genes are not secreted according to the supplied HPA summary. HPA indicates generally low tissue specificity for most genes, brain protein detection for most genes with available measurements, and low immune-cell specificity for nearly all members. Several isolated cell-type associations occur across diverse cell types, including T-cells, parietal cells, neutrophils, oocytes, corticotrophs, plasma cells, syncytiotrophoblasts, stromal cells, fibroblasts, Leydig cells, medullary thymic epithelial cells, and Müller glia. This diversity argues against a simple blood-cell contamination explanation, although broad expression and mixed cell-type contributions could contribute to the shared autonomic-nervous-system and brain signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence known relationship within the module, between MRPL1 and MTIF2. This is biologically coherent because MRPL1 is a mitochondrial ribosomal protein and MTIF2 is a mitochondrial translation-initiation factor. The other module relationships are not supported by high-confidence STRING interactions in the supplied results. No hu.MAP complex contains multiple module members. Thus, the network contains a plausible mitochondrial translation anchor, but most of the co-abundance structure is not presently explained by established physical interaction or shared hu.MAP complex membership. The remaining edges may reflect co-regulation, indirect biology, cell composition, or associations not captured by these resources.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: MRPL1–MTIF2 (0.939)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a potentially under-described cross-tissue co-abundance pattern, but it cannot be called a new biological mechanism from these data alone. Its novelty is supported only in the limited sense that most within-module relationships are absent from the supplied STRING and hu.MAP evidence, while the MRPL1–MTIF2 relationship is already known and biologically expected. Absence from interaction databases does not establish novelty, because database coverage, detection thresholds, tissue context, and indirect regulation can all hide real relationships. The cautious conclusion is that the shared module is a candidate novel network-level association requiring replication and experimental validation, not a demonstrated novel complex or pathway.

**Hypothesis.** Hypothesis: in cells contributing to both autonomic nervous system and brain samples, mitochondrial translation and mitochondrial protein handling may be co-regulated with cellular stress responses and growth-factor or MAPK signaling. MTIF2 and MRPL1 could form the core mitochondrial translation axis, MAIP1 could connect this axis to mitochondrial membrane insertion and calcium homeostasis, HSPA13 could reflect protein-folding or stress handling, and IGFBP5 or BRAF could represent extracellular or intracellular signaling inputs. This model predicts coordinated changes in mitochondrial protein synthesis, mitochondrial calcium or membrane-protein handling, and stress or growth signaling, but the current module does not establish directionality, causality, or a single shared cell type.

### Important genes

#### MTIF2

- **Related proteins** (co-abundance neighbors): MRPL1 (0.88), IGFBP5 (0.83), MAIP1 (0.80); STRING partners: MRPL1 (0.939)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial translational initiation factor 2. During the initiation of protein biosynthesis, initiation factor-2 (IF-2) promotes the binding of the initiator tRNA to the small subunit of the ribosome in a GTP-dependent manner. Prokaryotic IF-2 is a single polypeptide, while eukaryotic cytoplasmic IF-2 (eIF-2) is a trimeric protein. Bovine liver mitochondria contain IF-2(mt), an 85-kD monomeric protein that is equivalent to prokaryotic IF-2. T…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); hereditary disease (0.425); hypertensive disorder (0.215); preeclampsia (0.195); biliary tract disorder (0.184)
- **Europe PMC papers**: 301
- **Why important**: MTIF2 has the strongest network position in the module and connects to MRPL1, IGFBP5, and MAIP1. Its established function in mitochondrial translation initiation makes it a central candidate for explaining the module's mitochondrial interpretation. It is detected in brain, has an association with neurodegenerative disease in Open Targets, and has substantial literature support.
- **Conclusion**: Established evidence supports MTIF2 as a mitochondrial translation-initiation factor and as the principal network hub. Its contribution to this shared module is therefore plausible and biologically coherent. A role linking mitochondrial translation to the other module branches remains a hypothesis rather than an established mechanism.

#### MRPL1

- **Related proteins** (co-abundance neighbors): MTIF2 (0.88), GLOD4 (0.83); STRING partners: MTIF2 (0.939)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial ribosomal protein L1. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: preeclampsia (0.256); hair color (0.074); tongue cancer (0.043); stricture (0.028); COVID-19 (0.025)
- **Europe PMC papers**: 297
- **Why important**: MRPL1 is directly connected to MTIF2 by the only high-confidence STRING relationship reported for the module. Its established role as a mitochondrial large-subunit ribosomal protein provides an independent component of the mitochondrial translation interpretation. It is detected in brain and has substantial literature support.
- **Conclusion**: Established evidence supports MRPL1 as part of the mitochondrial ribosomal machinery and supports the MTIF2–MRPL1 relationship as a known interaction. Whether their co-abundance in this module reflects altered mitochondrial translation in the sampled tissues is a testable hypothesis.

#### MAIP1

- **Related proteins** (co-abundance neighbors): HSPA13 (0.81), MTIF2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: matrix AAA peptidase interacting protein 1. Predicted to enable ribosome binding activity. Involved in calcium import into the mitochondrion; mitochondrial calcium ion homeostasis; and protein insertion into mitochondrial membrane. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: schizophrenia (0.251); Abnormality of the skeletal system (0.197); autism spectrum disorder (0.171); metabolic disease (0.162); bipolar disorder (0.157)
- **Europe PMC papers**: 75
- **Why important**: MAIP1 links to MTIF2 in the module and is annotated with mitochondrial matrix localization, ribosome binding, mitochondrial calcium import, calcium homeostasis, and mitochondrial membrane protein insertion. It also has disease associations involving schizophrenia and autism spectrum disorder, which are relevant to nervous-system biology, although these associations do not establish the module mechanism. Its literature base is smaller than that of the major signaling genes, making it a potentially informative but less characterized component.
- **Conclusion**: Established annotations support MAIP1 as a mitochondrial protein-handling and calcium-homeostasis factor. Its network connection to MTIF2 supports a candidate bridge between mitochondrial translation and membrane or calcium biology. The specific role of that bridge in brain and autonomic nervous system co-abundance is a hypothesis.

#### BRAF

- **Related proteins** (co-abundance neighbors): GLOD4 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: B-Raf proto-oncogene, serine/threonine kinase. This gene encodes a protein belonging to the RAF family of serine/threonine protein kinases. This protein plays a role in regulating the MAP kinase/ERK signaling pathway, which affects cell division, differentiation, and secretion. Mutations in this gene, most commonly the V600E mutation, are the most frequently identified cancer-causing mutations in melanoma, and have been identified in various o…
- **Diseases (Open Targets)**: cardiofaciocutaneous syndrome (0.877); Noonan syndrome (0.838); melanoma (0.820); cardiofaciocutaneous syndrome 1 (0.764); Noonan syndrome 7 (0.759)
- **Europe PMC papers**: 71168
- **Why important**: BRAF is the module's signaling-associated gene and is connected to GLOD4. Its established kinase function in the MAPK or ERK pathway, together with extensive literature and strong disease associations including melanoma and RASopathy-related disorders, gives it major interpretive importance despite its peripheral network position. Its HPA profile shows brain protein detection and a cell-type association with neutrophils, but the supplied HPA evidence does not support a broad blood-cell explanation.
- **Conclusion**: Established evidence supports BRAF as a MAPK signaling kinase with major disease relevance. Its inclusion suggests that the module may combine mitochondrial state with signaling regulation, but the available network and enrichment evidence do not establish a direct BRAF connection to mitochondrial translation. That connection remains a hypothesis.

#### IGFBP5

- **Related proteins** (co-abundance neighbors): MTIF2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor binding protein 5. Enables insulin-like growth factor I binding activity. Involved in several processes, including cellular response to cAMP; regulation of smooth muscle cell migration; and regulation of smooth muscle cell proliferation. Part of insulin-like growth factor ternary complex. Biomarker of pulmonary fibrosis. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypothyroidism (0.394); nodular goiter (0.347); hyperthyroidism (0.342); thyroid gland disorder (0.288); Incisional hernia (0.283)
- **Europe PMC papers**: 6548
- **Why important**: IGFBP5 is connected to MTIF2 and is the module member with tissue-enhanced expression in cervix and secretion to blood. Its established functions include insulin-like growth-factor binding, regulation of smooth-muscle migration and proliferation, and links to fibrosis and cell signaling. It has a substantial literature base and may represent an extracellular or stromal signaling component rather than a mitochondrial component.
- **Conclusion**: Established evidence supports IGFBP5 as a secreted growth-factor-binding regulator with tissue and stromal associations. Its connection to MTIF2 could reflect coordinated signaling and mitochondrial state, but it could also arise from indirect regulation or sample composition. A functional bridge between IGFBP5 signaling and mitochondrial translation is therefore hypothetical.

## Module 9

**Tissue pair**: autonomic_nervous_system and brain  
**Genes (5)**: CKAP4, FUT8, GALNT2, SIGMAR1, SSR1

### Function

The strongest interpretation is a conserved endoplasmic-reticulum and Golgi membrane-processing module. All member genes support the globally corrected cellular-component term for an organelle subcompartment (GO:CC organelle subcompartment; q_global = 0.0233). SSR1 supports cotranslational protein targeting and translocation at the ER; CKAP4 is an ER-associated cytoskeletal protein; GALNT2 initiates mucin-type O-linked glycosylation in the Golgi; and FUT8 performs N-linked glycan fucosylation in the Golgi. SIGMAR1 is an ER-associated chaperone implicated in nervous-system development and regulation of neuronal survival. The supplementary STRING keywords for signal anchors, transmembrane helices, and organelle subcompartment (STRING Keyword Signal-anchor; within-query FDR = 0.0103)(STRING Keyword Transmembrane helix; within-query FDR = 0.0103)(STRING Component Organelle subcompartment; within-query FDR = 0.0116) are concordant, but they are not additional globally corrected enrichment evidence. Overall, the module is most consistent with coordinated membrane-protein insertion, ER handling, and glycan maturation, with a possible neuronal-protective component through SIGMAR1.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: only one member is annotated in the secretome, while the genes are mainly intracellular or membrane-associated ER and Golgi proteins. The HPA data indicate generally low tissue specificity for most members, with one liver-enhanced gene, and brain protein detection for every member. Cell-type annotations are heterogeneous, including neural, glial, epithelial, secretory, cardiac, trophoblast, and selected blood-cell populations. Most genes have low immune-cell specificity, so the module does not strongly resemble a blood-cell module, although sample cell composition could contribute to the shared signal. The absence of matching autonomic-nervous-system HPA tissue data limits direct tissue-specific interpretation.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC organelle subcompartment | 0.0233 | CKAP4, FUT8, GALNT2, SIGMAR1, SSR1 |

### STRING and hu.MAP

No member pair meets the reported high-confidence STRING interaction threshold, and no hu.MAP complex contains multiple module members. Thus, the co-abundance structure is not supported by established physical interactions or a recognized multi-member protein complex in these resources. The supplementary STRING keyword enrichments (STRING Keyword Signal-anchor; within-query FDR = 0.0103)(STRING Keyword Transmembrane helix; within-query FDR = 0.0103)(STRING Component Organelle subcompartment; within-query FDR = 0.0116) describe compatible cellular properties rather than documented pairwise relationships. The pattern may therefore reflect coordinated expression of proteins operating in the same membrane-trafficking and glycosylation environment, rather than a stable canonical complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Signal-anchor (FDR = 0.0103, 3 genes); Keyword Transmembrane helix (FDR = 0.0103, 5 genes); Component Organelle subcompartment (FDR = 0.0116, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared co-abundance pattern may represent a new systems-level observation because it is not reproduced as a known STRING interaction network or hu.MAP complex. However, it would be incorrect to claim that the underlying biology is novel: ER translocation, Golgi glycosylation, fucosylation, and SIGMAR1-associated neuronal functions are established individually. Absence from STRING or hu.MAP alone cannot establish discovery. The defensible novelty claim is that these genes form a conserved cross-tissue co-abundance module in the stated tissue pair, with an interpretable but previously unvalidated relationship between membrane-protein handling, glycan processing, and neuronal context.

**Hypothesis.** Hypothesis: in autonomic nervous system and brain samples, variation in a shared ER-to-Golgi proteostasis program coordinately alters membrane-protein insertion, ER organization, and glycan maturation. CKAP4 and SSR1 may provide the ER structural and translocation context; GALNT2 and FUT8 may modify the glycan state of newly processed proteins; and SIGMAR1 may connect this proteostasis state to neuronal stress responses and survival. This is a mechanistic hypothesis generated from co-abundance and functional coherence, not evidence of direct physical interaction or causal regulation.

### Important genes

#### CKAP4

- **Related proteins** (co-abundance neighbors): SSR1 (0.83), SIGMAR1 (0.80), GALNT2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytoskeleton associated protein 4. Enables RNA binding activity. Located in several cellular components, including lipid droplet; nuclear speck; and rough endoplasmic reticulum. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: smoking initiation (0.357); arthropathy (0.216); asthma (0.200); adolescent idiopathic scoliosis (0.141); spinal cord injury (0.128)
- **Europe PMC papers**: 2103
- **Why important**: CKAP4 is the central network connector, linking SSR1, SIGMAR1, and GALNT2, and it is present in the primary organelle-subcompartment evidence (GO:CC organelle subcompartment; q_global = 0.0233) and all supplementary STRING categories (STRING Keyword Signal-anchor; within-query FDR = 0.0103)(STRING Keyword Transmembrane helix; within-query FDR = 0.0103)(STRING Component Organelle subcompartment; within-query FDR = 0.0116). Its ER localization and extensive literature support make it a strong organizing candidate for the module.
- **Conclusion**: Established evidence supports CKAP4 as an ER-associated structural and membrane-processing component with broad tissue distribution and brain protein detection. Its central position supports a coordinating role in the module, but the co-abundance data do not establish that CKAP4 regulates the other genes.

#### GALNT2

- **Related proteins** (co-abundance neighbors): FUT8 (0.85), CKAP4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypeptide N-acetylgalactosaminyltransferase 2. This gene encodes a member of the glycosyltransferase 2 protein family. Members of this family initiate mucin-type O-glycoslation of peptides in the Golgi apparatus. The encoded protein may be involved in O-linked glycosylation of the immunoglobulin A1 hinge region. This gene may influence triglyceride levels, and may be involved Type 2 diabetes, as well as several types of cancer. Alternative spl…
- **Diseases (Open Targets)**: congenital disorder of glycosylation, type iit (0.777); metabolic syndrome (0.546); familial lipoprotein lipase deficiency (0.486); alcohol drinking (0.450); familial hyperlipidemia (0.444)
- **Europe PMC papers**: 1178
- **Why important**: GALNT2 connects the central ER-associated CKAP4 branch to FUT8 and provides a direct biochemical link to Golgi glycosylation. It is included in (GO:CC organelle subcompartment; q_global = 0.0233), (STRING Keyword Signal-anchor; within-query FDR = 0.0103), (STRING Keyword Transmembrane helix; within-query FDR = 0.0103), and (STRING Component Organelle subcompartment; within-query FDR = 0.0116), and its annotations connect protein maturation and O-linked glycosylation with metabolic and glycosylation-related disease associations.
- **Conclusion**: Established evidence supports GALNT2 as a Golgi glycosyltransferase involved in initiation of mucin-type O-linked glycosylation and protein maturation. Its role as the bridge between ER-associated co-abundance and Golgi processing is a plausible interpretation, but substrate-specific effects in these tissues remain a hypothesis.

#### FUT8

- **Related proteins** (co-abundance neighbors): GALNT2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fucosyltransferase 8. This gene encodes an enzyme belonging to the family of fucosyltransferases. The product of this gene catalyzes the transfer of fucose from GDP-fucose to N-linked type complex glycopeptides. This enzyme is distinct from other fucosyltransferases which catalyze alpha1-2, alpha1-3, and alpha1-4 fucose addition. The expression of this gene may contribute to the malignancy of cancer cells and to their …
- **Diseases (Open Targets)**: congenital disorder of glycosylation with defective fucosylation (0.784); hereditary disease (0.415); COVID-19 (0.404); gout (0.400); Abnormality of the skeletal system (0.380)
- **Europe PMC papers**: 3371
- **Why important**: FUT8 is the partner of GALNT2 in the module and contributes enzymatic specificity for N-linked glycan fucosylation. It appears in the primary organelle-subcompartment term (GO:CC organelle subcompartment; q_global = 0.0233) and the compatible signal-anchor, transmembrane, and organelle annotations (STRING Keyword Signal-anchor; within-query FDR = 0.0103)(STRING Keyword Transmembrane helix; within-query FDR = 0.0103)(STRING Component Organelle subcompartment; within-query FDR = 0.0116). Its congenital glycosylation disease association gives the module a clinically relevant glycan-processing anchor.
- **Conclusion**: Established evidence supports FUT8 as a Golgi fucosyltransferase involved in N-glycan processing and glycoprotein biosynthesis. Its co-abundance with GALNT2 suggests coordinated glycan remodeling, but it is not established that the two enzymes act on shared substrates in this module.

#### SSR1

- **Related proteins** (co-abundance neighbors): CKAP4 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal sequence receptor subunit 1. The signal sequence receptor (SSR) is a glycosylated endoplasmic reticulum (ER) membrane receptor associated with protein translocation across the ER membrane. The SSR consists of 2 subunits, a 34-kD glycoprotein encoded by this gene and a 22-kD glycoprotein. This gene generates several mRNA species as a result of complex alternative polyadenylation. This gene is unusual in that it utilizes arrays…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.470); diabetes mellitus (0.344); neurodegenerative disease (0.329); Inguinal hernia (0.322); refractive error (0.315)
- **Europe PMC papers**: 938
- **Why important**: SSR1 supplies the clearest direct link to ER protein translocation and is connected to CKAP4, the module's central connector. It contributes to (GO:CC organelle subcompartment; q_global = 0.0233), (STRING Keyword Transmembrane helix; within-query FDR = 0.0103), and (STRING Component Organelle subcompartment; within-query FDR = 0.0116), and its signal-sequence-receptor function is mechanistically relevant to the proposed ER proteostasis program.
- **Conclusion**: Established evidence supports SSR1 as a subunit of the ER signal-sequence receptor involved in cotranslational and post-translational membrane targeting. Its inclusion supports an ER-entry interpretation, while its specific contribution to the shared brain and autonomic nervous system co-abundance pattern remains unresolved.

#### SIGMAR1

- **Related proteins** (co-abundance neighbors): CKAP4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sigma receptor chaperone 1. This gene encodes a receptor protein that interacts with a variety of psychotomimetic drugs, including cocaine and amphetamines. The receptor is believed to play an important role in the cellular functions of various tissues associated with the endocrine, immune, and nervous systems. As indicated by its previous name, opioid receptor sigma 1 (OPRS1), the product of this gene was erroneously though…
- **Diseases (Open Targets)**: autosomal recessive distal spinal muscular atrophy 2 (0.703); juvenile amyotrophic lateral sclerosis (0.683); Cough (0.605); Headache (0.605); Nasal congestion (0.604)
- **Europe PMC papers**: 1220
- **Why important**: SIGMAR1 is connected to CKAP4 and adds nervous-system relevance to an otherwise largely general membrane-processing module. It is present in (GO:CC organelle subcompartment; q_global = 0.0233), (STRING Keyword Transmembrane helix; within-query FDR = 0.0103), and (STRING Component Organelle subcompartment; within-query FDR = 0.0116), has brain protein detection, and has disease associations involving motor-neuron disorders and neuronal function. Its tissue-enhanced liver annotation also cautions against assuming the module is exclusively neural.
- **Conclusion**: Established evidence supports SIGMAR1 as a non-opioid sigma receptor chaperone with roles in nervous-system development and regulation of neuronal apoptosis. A link between SIGMAR1-associated neuronal stress handling and the ER-to-Golgi processing program is a reasonable hypothesis, not a demonstrated causal mechanism.

## Module 10

**Tissue pair**: autonomic_nervous_system and brain  
**Genes (5)**: DIDO1, MTMR14, SNAP23, SUCLG2, TOP2B

### Function

No GO or KEGG term passed global correction, and there were no supplementary STRING enrichment terms. The module therefore does not support a narrowly defined pathway annotation. Its genes span phosphoinositide regulation and autophagy through MTMR14, DNA topology and transcriptional control through TOP2B, apoptosis and transcription through DIDO1, mitochondrial succinyl-CoA metabolism through SUCLG2, and vesicle fusion and exocytosis through SNAP23. The sparse co-abundance structure may reflect coordinated variation across cellular compartments rather than a single established biochemical pathway. The strongest biologically plausible themes are cellular maintenance, intracellular trafficking, energy metabolism, and regulation of DNA or cell-state responses, but these remain an interpretation rather than a globally supported enrichment result.

**Cell composition.** The module is not dominated by secreted or plasma proteins, since none of its genes is classified as secreted. Most genes have low tissue specificity and low immune-cell specificity, which is compatible with broadly expressed cellular machinery rather than a highly restricted tissue program. Nevertheless, several genes have cell-type-enhanced HPA annotations: MTMR14 is associated with neutrophils, SUCLG2 with hepatocytes and parietal cells, and SNAP23 with late spermatids, megakaryocytes, platelets, and eosinophils. SUCLG2 is tissue-enhanced in liver. These annotations raise the possibility that part of the shared signal reflects cell composition or broadly distributed cellular programs rather than a neuron-specific mechanism. All genes were detected by brain immunohistochemistry, while the autonomic-nervous-system comparison lacks a matching HPA tissue entry, so the protein evidence does not independently establish autonomic-neural specificity.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no hu.MAP complex contained multiple module members. Thus the co-abundance edges are not corroborated here as established physical or functional interactions. The absence of STRING and hu.MAP support argues against interpreting the module as a known protein complex. It does not exclude context-dependent interactions, transient associations, shared regulation, or indirect coordination. The observed links should therefore be treated primarily as dataset-derived co-abundance relationships.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a new co-abundance observation, but it cannot be called a new biological mechanism on the available evidence. The module has no globally significant GO or KEGG term, no supplementary STRING enrichment, no high-confidence STRING pair, and no multi-member hu.MAP complex. Those absences make the module difficult to connect to an established network, but they do not prove novelty because databases are incomplete and co-abundance can capture regulation or cell-mixture effects that interaction resources do not represent. A defensible claim is that the specific cross-tissue co-abundance configuration is potentially novel and requires independent replication, cell-composition assessment, and experimental or orthogonal network validation.

**Hypothesis.** Hypothesis: the module represents a cross-tissue cellular-maintenance program assembled from broadly expressed proteins, in which MTMR14-related phosphoinositide regulation and membrane trafficking covary with SNAP23-mediated vesicle fusion, SUCLG2-linked mitochondrial metabolism, and TOP2B or DIDO1-linked nuclear responses. The shared signal may arise from coordinated changes in cellular state, organelle function, and vesicle handling across autonomic-nervous-system and brain samples, potentially amplified by contributions from non-neuronal or blood-associated cell types. This is a hypothesis only; the lack of globally enriched terms and the absence of known interaction support prevent assigning it as an established module mechanism.

### Important genes

#### MTMR14

- **Related proteins** (co-abundance neighbors): TOP2B (0.85), SUCLG2 (0.83), SNAP23 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myotubularin related protein 14. This gene encodes a myotubularin-related protein. The encoded protein is a phosphoinositide phosphatase that specifically dephosphorylates phosphatidylinositol 3,5-biphosphate and phosphatidylinositol 3-phosphate. Mutations in this gene are correlated with autosomal dominant centronuclear myopathy. Alternate splicing results in multiple transcript variants. A pseudogene of this gene is found on ch…
- **Diseases (Open Targets)**: neurodegenerative disease (0.480); Alzheimer disease (0.464); Parkinson disease (0.463); lysosomal storage disease (0.462); autosomal dominant centronuclear myopathy (0.446)
- **Europe PMC papers**: 388
- **Why important**: MTMR14 is the central connector in the module, linking TOP2B, SUCLG2, and SNAP23 in the co-abundance subgraph. Its annotated phosphoinositide-phosphatase activity, roles in phosphoinositide-mediated signaling and macroautophagy, brain protein detection, and association with centronuclear myopathy and neurodegenerative disease make it the strongest candidate for connecting membrane signaling, organelle quality control, and disease biology. Its literature base is moderate relative to the other leading candidates, so its network position is especially informative.
- **Conclusion**: Established evidence supports MTMR14 as a phosphoinositide-regulating protein involved in autophagy and as a gene associated with centronuclear myopathy. The module supports a possible coordinating role for MTMR14, but the proposed connection to the other module genes is a hypothesis because no STRING or hu.MAP relationship is reported.

#### SNAP23

- **Related proteins** (co-abundance neighbors): MTMR14 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: synaptosome associated protein 23. Specificity of vesicular transport is regulated, in part, by the interaction of a vesicle-associated membrane protein termed synaptobrevin/VAMP with a target compartment membrane protein termed syntaxin. These proteins, together with SNAP25 (synaptosome-associated protein of 25 kDa), form a complex which serves as a binding site for the general membrane fusion machinery. Synaptobrevin/VAMP and syn…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); hyperaldosteronism (0.187); hepatocellular carcinoma (0.186); neoplasm (0.095); colorectal carcinoma (0.094)
- **Europe PMC papers**: 2202
- **Why important**: SNAP23 is the module member most directly linked to membrane fusion, exocytosis, vesicle transport, and synaptic vesicle-related processes. It is connected to MTMR14 in the module and has brain protein detection, while its HPA cell-type associations include megakaryocytes, platelets, and eosinophils. Its large literature base and disease associations involving neurodegenerative disease make it important for distinguishing a neuronal vesicle interpretation from a broader secretory or blood-cell-composition interpretation.
- **Conclusion**: Established evidence supports SNAP23 as a broadly used vesicle-fusion component with roles in exocytosis and degranulation. The module does not establish a neuron-specific SNAP23 mechanism; the blood-associated HPA pattern means that altered cell composition is an important alternative explanation.

#### TOP2B

- **Related proteins** (co-abundance neighbors): MTMR14 (0.85), DIDO1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA topoisomerase II beta. This gene encodes a DNA topoisomerase, an enzyme that controls and alters the topologic states of DNA during transcription. This nuclear enzyme is involved in processes such as chromosome condensation, chromatid separation, and the relief of torsional stress that occurs during DNA transcription and replication. It catalyzes the transient breaking and rejoining of two strands of duplex DNA which al…
- **Diseases (Open Targets)**: B-cell immunodeficiency, distal limb anomalies, and urogenital malformations (0.720); neoplasm (0.597); small cell lung carcinoma (0.561); breast cancer (0.552); small cell carcinoma (0.486)
- **Europe PMC papers**: 1781
- **Why important**: TOP2B occupies a bridging position between MTMR14 and DIDO1 and encodes a nuclear enzyme that changes DNA topology during transcription and other DNA processes. It has brain protein detection, a substantial literature base, and disease associations that include developmental abnormalities and cancer. Its presence broadens the module beyond membrane trafficking and suggests that cellular state or transcriptional demand could contribute to the shared co-abundance pattern.
- **Conclusion**: Established evidence supports TOP2B as a DNA-topology enzyme involved in transcription-related and chromosome-related processes. Its module relationship with MTMR14 and DIDO1 is not independently confirmed by interaction databases, so any role as a nuclear arm of the proposed program remains hypothetical.

#### SUCLG2

- **Related proteins** (co-abundance neighbors): MTMR14 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase GDP-forming subunit beta. This gene encodes a GTP-specific beta subunit of succinyl-CoA synthetase. Succinyl-CoA synthetase catalyzes the reversible reaction involving the formation of succinyl-CoA and succinate. Alternate splicing results in multiple transcript variants. Pseudogenes of this gene are found on chromosomes 5 and 12. [provided by RefSeq, Apr 2010].
- **Diseases (Open Targets)**: smoking initiation (0.377); breast disorder (0.325); vitamin B deficiency (0.318); alcohol drinking (0.314); duodenal ulcer (0.270)
- **Europe PMC papers**: 1184
- **Why important**: SUCLG2 is linked to MTMR14 in the module and encodes the beta subunit of a GTP-forming succinyl-CoA ligase involved in the tricarboxylic-acid cycle and succinyl-CoA metabolism. Its mitochondrial localization, liver tissue enhancement, hepatocyte association, brain protein detection, and substantial literature base make it important for evaluating whether the module includes an energetic or metabolic component rather than only neural signaling.
- **Conclusion**: Established evidence supports SUCLG2 as a mitochondrial metabolic enzyme component. The module is consistent with a possible relationship between metabolic state and phosphoinositide or vesicle biology, but it does not demonstrate that such coupling is causal or neural-specific.

## Module 11

**Tissue pair**: autonomic_nervous_system and brain  
**Genes (6)**: ADAR, NOL11, RSL1D1, RPF2, SRA1, WDR36

### Function

No GO or KEGG term passed global correction, so those resources provide no globally significant enrichment for this module. The supplementary STRING evidence converges on nucleolar RNA metabolism, ribonucleoprotein-complex biogenesis, rRNA processing, preribosome organization, and ribosome biogenesis (8 supplementary STRING terms; within-query FDR 0.0142–0.0347). The strongest biological interpretation is a conserved nucleolar RNA-processing and ribosome-production program, with ADAR adding an RNA-editing component and SRA1 adding a transcriptional and nuclear-regulatory component. Established evidence comes from the gene annotations and the coherent STRING neighborhood; the precise coordinated activity of the entire module remains inferential.

**Cell composition.** All module genes have low tissue specificity, and all have low immune-cell specificity in HPA. None is secreted. HPA detects the proteins in brain regions represented in the fact sheet, while autonomic-nervous-system protein data are unavailable. The module therefore does not resemble a plasma-protein or blood-cell-enriched signature. Its broadly expressed, nucleolar and nuclear composition is more consistent with a shared cellular program, plausibly reflecting common RNA-processing and biosynthetic demands, rather than a tissue-specific secreted signal or an obvious blood contamination effect. Cell-type-enhanced annotations for SRA1, RPF2, and ADAR should be treated as context clues rather than proof of a dominant cell population.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a connected core involving NOL11, RPF2, RSL1D1, and WDR36, with especially strong links among RPF2, RSL1D1, and WDR36, and an additional NOL11–WDR36 relationship. STRING also places most of the genes in nucleolar, preribosomal, ribonucleoprotein, rRNA-processing, and ribosome-biogenesis contexts (8 supplementary STRING terms; within-query FDR 0.0142–0.0347). SRA1 and ADAR have limited direct STRING support within this module, although both appear in supplementary functional groupings. No hu.MAP complex contains at least two module members. Thus, the module contains a known interaction-supported nucleolar core, but the complete six-gene co-abundance structure is not represented as a previously catalogued hu.MAP complex.

**STRING interactions (score >= 0.7)**: 4 of 15 gene pairs: NOL11–WDR36 (0.936); RPF2–RSL1D1 (0.996); RPF2–WDR36 (0.941); RSL1D1–WDR36 (0.992)
**STRING functional enrichment (supplementary, within-query FDR)**: Process ncRNA processing (FDR = 0.0142, 5 genes); COMPARTMENTS Nucleolus (FDR = 0.0154, 5 genes); COMPARTMENTS 90S preribosome (FDR = 0.0154, 3 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 0.0154, 5 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 0.0164, 4 genes); Process Ribonucleoprotein complex biogenesis (FDR = 0.0205, 5 genes); Process rRNA processing (FDR = 0.0318, 4 genes); Keyword Ribosome biogenesis (FDR = 0.0347, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is not established as a wholly new molecular pathway: several constituent genes, their nucleolar locations, and multiple pairwise STRING relationships are already known. The potentially novel result is the conserved co-abundance of this particular gene set across autonomic nervous system and brain, including the association of a ribosome-biogenesis core with ADAR and SRA1. That claim should remain cautious because absence from hu.MAP or incomplete STRING connectivity does not prove novelty, and no globally significant GO or KEGG enrichment supports a uniquely defined pathway. The finding is best described as a potentially novel tissue-pair co-abundance configuration built around known nucleolar biology.

**Hypothesis.** Hypothesis: in autonomic nervous system and brain samples, a shared cellular state coordinates nucleolar ribosome production and RNA quality control with broader nuclear RNA regulation. NOL11, RPF2, RSL1D1, and WDR36 may form the core of this state through rRNA maturation, preribosome handling, and ribonucleoprotein organization, while ADAR may couple it to double-stranded-RNA editing and SRA1 may couple it to transcriptional or chromatin-related regulation. This hypothesis is consistent with the annotations and STRING structure, but direct physical cooperation among all module members and causal relevance to neural function are not established by the fact sheet.

### Important genes

#### RPF2

- **Related proteins** (co-abundance neighbors): NOL11 (0.84), RSL1D1 (0.82); STRING partners: RSL1D1 (0.996), WDR36 (0.941)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosome production factor 2 homolog. Enables 5S rRNA binding activity. Involved in protein localization to nucleolus; regulation of signal transduction by p53 class mediator; and ribosomal large subunit biogenesis. Located in chromosome; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.479); Hypercholesterolemia (0.196); colorectal carcinoma (0.079); Helicobacter pylori infectious disease (0.048); asthma (0.047)
- **Europe PMC papers**: 424
- **Why important**: RPF2 is a central member of the nucleolar interpretation: it is linked within the module to NOL11 and RSL1D1 and is included across the broad STRING RNA-processing and ribosome-biogenesis groupings (8 supplementary STRING terms; within-query FDR 0.0142–0.0347). Its established functions include five-S rRNA binding, large-subunit assembly, rRNA maturation, and nucleolar localization. Its disease-oriented evidence includes an Open Targets association with neurodegenerative disease, and its literature volume is substantial enough to support a comparatively well-established role.
- **Conclusion**: Established evidence supports RPF2 as a core ribosome-production and rRNA-processing component. It is a strong anchor for the module function. A specific role in the autonomic nervous system–brain co-abundance pattern remains a hypothesis.

#### WDR36

- **Related proteins** (co-abundance neighbors): SRA1 (0.83); STRING partners: NOL11 (0.936), RPF2 (0.941), RSL1D1 (0.992)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 36. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: open-angle glaucoma (0.705); asthma (0.510); nasal cavity polyp (0.423); Wheezing (0.401); eosinophilic esophagitis (0.393)
- **Europe PMC papers**: 744
- **Why important**: WDR36 has the broadest STRING connectivity in the module, linking to NOL11, RPF2, and RSL1D1, and it appears in every listed STRING supplementary grouping (8 supplementary STRING terms; within-query FDR 0.0142–0.0347). Its annotations place it in the nucleolus and in small-subunit biogenesis and rRNA processing. It also has a relatively large literature base and a strong disease association with open-angle glaucoma, which is relevant to the nervous-system context without proving a role in this module.
- **Conclusion**: Established evidence identifies WDR36 as a highly connected nucleolar rRNA-processing component and a plausible structural bridge within the module. Its disease links support biological importance, but they do not establish that this module causes or modifies glaucoma or another neural phenotype.

#### RSL1D1

- **Related proteins** (co-abundance neighbors): SRA1 (0.91), RPF2 (0.82), NOL11 (0.82), ADAR (0.81); STRING partners: RPF2 (0.996), WDR36 (0.992)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal L1 domain containing 1. Enables mRNA 3'-UTR binding activity and mRNA 5'-UTR binding activity. Involved in regulation of apoptotic process and regulation of cellular senescence. Acts upstream of or within regulation of protein localization. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: adolescent idiopathic scoliosis (0.219); hepatocellular carcinoma (0.099); neoplasm (0.099); colorectal carcinoma (0.096); insomnia (0.078)
- **Europe PMC papers**: 381
- **Why important**: RSL1D1 has the highest network degree in the module and connects to SRA1, RPF2, NOL11, and ADAR. It has strong STRING links to RPF2 and WDR36 and participates in the nucleolar, preribosome, ribonucleoprotein, and RNA-processing groupings (7 supplementary STRING terms; within-query FDR 0.0142–0.0318). Its nucleolar and chromosome-associated localization, annotations involving protein localization, apoptosis, and cellular senescence, and substantial literature volume make it a plausible interface between ribosome-related activity and broader cell-state regulation.
- **Conclusion**: Established evidence supports RSL1D1 as the principal network connector and a nucleolar regulatory component. Its position suggests a possible coordinating role in the module, but that coordinating role is a hypothesis rather than a demonstrated mechanism.

#### NOL11

- **Related proteins** (co-abundance neighbors): RPF2 (0.84), RSL1D1 (0.82); STRING partners: WDR36 (0.936)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleolar protein 11. Enables RNA binding activity. Involved in maturation of SSU-rRNA and positive regulation of transcription of nucleolar large rRNA by RNA polymerase I. Located in nucleolus. Part of t-UTP complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: diabetes mellitus (0.100); type 2 diabetes mellitus (0.100); atrial fibrillation (0.087); ulcerative colitis (0.011); cancer (0.011)
- **Europe PMC papers**: 240
- **Why important**: NOL11 links directly to RPF2 and RSL1D1 in the module and to WDR36 in STRING. It is a nucleolar RNA-binding protein involved in small-subunit rRNA maturation and transcription of nucleolar large rRNA, and it contributes to the STRING RNA-processing and ribosome-biogenesis groupings (STRING Process ncRNA processing; within-query FDR = 0.0142), (STRING COMPARTMENTS Nucleolus; within-query FDR = 0.0154), (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 0.0164), (STRING Process Ribonucleoprotein complex biogenesis; within-query FDR = 0.0205), (STRING Process rRNA processing; within-query FDR = 0.0318), and (STRING Keyword Ribosome biogenesis; within-query FDR = 0.0347). Its disease-oriented annotations include diabetes mellitus, type two diabetes mellitus, and atrial fibrillation, while its literature volume is more limited than that of ADAR or SRA1.
- **Conclusion**: Established evidence places NOL11 in nucleolar rRNA maturation and transcriptional control. It is a biologically coherent core member, but any connection between its disease associations and the shared neural-tissue module remains unproven.

#### ADAR

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR is the most extensively studied gene in the module and provides a distinct RNA-editing dimension. It catalyzes adenosine-to-inosine editing, destabilizes double-stranded RNA, and is involved in RNA processing and antiviral responses. It connects to RSL1D1 in the module and appears in the STRING RNA-processing, nucleolar, ribonucleoprotein, and ribonucleoprotein-biogenesis groupings (STRING Process ncRNA processing; within-query FDR = 0.0142), (STRING COMPARTMENTS Nucleolus; within-query FDR = 0.0154), (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.0154), and (STRING Process Ribonucleoprotein complex biogenesis; within-query FDR = 0.0205). Its strong disease associations include Aicardi–Goutieres syndrome, dyschromatosis symmetrica hereditaria, and ADAR-related interferonopathy.
- **Conclusion**: Established evidence supports ADAR as an RNA-editing and RNA-surveillance component with major disease relevance. Its inclusion may indicate coupling between nucleolar RNA handling and broader RNA quality control, but that coupling is a hypothesis and is not demonstrated by the co-abundance data alone.

## Module 12

**Tissue pair**: autonomic_nervous_system and brain  
**Genes (28)**: DHFR, EXOSC2, FOXRED1, GEMIN4, HNRNPH1, HNRNPL, KRI1, LARP4, NSFL1C, NUP43, PPHLN1, PPIE, PRIM1, PSMC4, PSMC2, PSMA1, POLR1B, SMAP, SUPT16H, SMNDC1, TACC3, ALYREF, TMOD3, TOMM40, EFTUD2, UBTF, ZNF207, ZNRD2

### Function

The module is best interpreted as a broadly expressed intracellular gene-expression and proteostasis program, with contributions from pre-mRNA splicing and RNA processing, ribosomal RNA transcription and processing, nucleocytoplasmic transport, proteasomal protein degradation, mitochondrial protein handling, and cell-cycle or cytoskeletal regulation. This interpretation is supported by the functions of HNRNPL, HNRNPH1, EFTUD2, PPIE, GEMIN4, EXOSC2, ALYREF, POLR1B, UBTF, PSMA1, PSMC2, PSMC4, TOMM40, TACC3, ZNF207, and related genes. No GO or KEGG term passed global correction, so there is no globally significant GO or KEGG annotation for this module. The STRING results are supplementary: (STRING RCTM Metabolism of RNA; within-query FDR = 0.0286) points toward RNA metabolism, while (STRING RCTM Negative regulation of NOTCH4 signaling; within-query FDR = 0.0286) links a subset of proteasome and spindle-associated genes to negative regulation of NOTCH4 signaling. These findings support a composite housekeeping and gene-expression interpretation rather than a narrowly defined autonomic nervous system or brain-specific pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not strongly immune-cell specific, with most genes having low immune-cell specificity, so a simple blood contamination explanation is not supported by the HPA summary. However, the module is predominantly broadly expressed, with most genes having low tissue specificity. HPA nevertheless shows recurrent enrichment in erythrocyte progenitors and, for some genes, spermatogenic cell types; several genes also show cell-type enhancement in microglia or glial populations. This pattern could partly reflect shared proliferative, RNA-processing, or cellular-maintenance programs across tissues and cell types rather than a specialized neuronal function. Protein detection in brain is broad, whereas autonomic nervous system protein data are unavailable, so the cross-tissue interpretation should not be based on protein evidence for the autonomic nervous system.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a coherent but incomplete interaction backbone. The strongest known relationships include the proteasome links among PSMA1, PSMC2, and PSMC4; the RNA-binding links among HNRNPL, HNRNPH1, and ALYREF; and the spliceosome-associated link between EFTUD2 and PPIE. POLR1B also connects to UBTF and SUPT16H in STRING. These relationships indicate that parts of the module recover established proteasomal, RNA-processing, and ribosomal transcription machinery rather than an entirely novel physical complex. The hu.MAP results reinforce this conclusion: (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1), and (hu.MAP huMAP3_05064.1) place PSMA1, PSMC2, and PSMC4 in known proteasome assemblies; (hu.MAP huMAP3_07581.1) and (hu.MAP huMAP3_14523.1) place HNRNPL, HNRNPH1, and PPHLN1 in heterogeneous nuclear ribonucleoprotein-related assemblies; (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), and (hu.MAP huMAP3_09945.1) place EFTUD2 and PPIE in spliceosome-related assemblies; and (hu.MAP huMAP3_08980.1) connects GEMIN4 and EFTUD2 to an snRNP or spliceosomal assembly. The module therefore appears to combine several known machinery fragments linked by co-abundance, with many module edges not represented by high-confidence STRING interactions.

**STRING interactions (score >= 0.7)**: 10 of 378 gene pairs: ALYREF–EFTUD2 (0.89); ALYREF–HNRNPH1 (0.914); ALYREF–HNRNPL (0.844); EFTUD2–PPIE (0.992); HNRNPH1–HNRNPL (0.982); POLR1B–SUPT16H (0.748); POLR1B–UBTF (0.863); PSMA1–PSMC2 (0.999); PSMA1–PSMC4 (0.999); PSMC2–PSMC4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Metabolism of RNA (FDR = 0.0286, 12 genes); RCTM Negative regulation of NOTCH4 signaling (FDR = 0.0286, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09656.1 (PSMA1, PSMC2, PSMC4; 3/64); huMAP3_13725.1 (PSMA1, PSMC2, PSMC4; 3/69); huMAP3_07581.1 (HNRNPL, PPHLN1; 2/21); huMAP3_05064.1 (PSMC2, PSMC4; 2/31); huMAP3_14523.1 (HNRNPH1, PPHLN1; 2/33); huMAP3_08501.1 (EFTUD2, PPIE; 2/47); huMAP3_09504.1 (EFTUD2, PPIE; 2/51); huMAP3_09945.1 (EFTUD2, PPIE; 2/61); huMAP3_08980.1 (GEMIN4, EFTUD2; 2/97)

### Novelty

This module should not be claimed as a newly discovered molecular complex or as a new disease pathway. Several of its most interpretable components belong to well-established proteasome, spliceosome, heterogeneous nuclear ribonucleoprotein, ribosomal transcription, and RNA-processing systems, as shown by STRING and hu.MAP. The potentially new aspect is the reproducible co-abundance of these machinery fragments across autonomic nervous system and brain samples. That cross-tissue organization may be biologically informative, but it could also arise from shared cellular composition, broad housekeeping demands, proliferative cell states, or technical covariance. The absence of some genes from STRING or hu.MAP does not establish novelty. Stronger novelty claims would require replication in independent cohorts, preservation after cell-composition adjustment, comparison with existing tissue co-expression modules, and experimental testing of whether the genes are coordinately regulated.

**Hypothesis.** Hypothesis: the module represents a coordinated cellular-maintenance state in which RNA maturation and export, ribosomal transcription, proteasomal turnover, mitochondrial import, and cytoskeletal or spindle-related processes are jointly elevated or reduced across shared cell populations in brain and autonomic nervous system samples. One possible biological explanation is that cells with high demands for transcriptional remodeling and proteostasis co-vary across the two tissues, with RNA-processing genes forming one functional arm and proteasome or cell-cycle genes forming another. This is a hypothesis, not an established mechanism; the current enrichment evidence does not demonstrate direct regulation between these components or prove a neuron-specific role.

### Important genes

#### TACC3

- **Related proteins** (co-abundance neighbors): PSMC2 (0.90), LARP4 (0.89), PPIE (0.87), POLR1B (0.87), EXOSC2 (0.84), HNRNPL (0.84), HNRNPH1 (0.83), NUP43 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Centriolar satellite, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transforming acidic coiled-coil containing protein 3. This gene encodes a member of the transforming acidic colied-coil protein family. The encoded protein is a motor spindle protein that may play a role in stabilization of the mitotic spindle. This protein may also play a role in growth a differentiation of certain cancer cells. [provided by RefSeq, Nov 2011].
- **Diseases (Open Targets)**: osteoarthritis, hip (0.465); osteoarthritis, knee (0.465); total knee arthroplasty (0.425); osteoarthritis (0.421); medical procedure (0.360)
- **Europe PMC papers**: 2879
- **Why important**: TACC3 has the most central network position in the supplied subgraph, linking RNA-processing, proteasome, nucleoporin, and spindle-associated genes. Its established functions include mitotic spindle organization, chromosome segregation, and neurogenesis. It is tissue-enhanced in bone marrow, lymphoid tissue, and testis, and HPA detects it in brain. It is also the most extensively studied gene among the selected network hubs, with disease associations including osteoarthritis. It appears in the supplementary STRING NOTCH4-related set (STRING RCTM Negative regulation of NOTCH4 signaling; within-query FDR = 0.0286), although that annotation is not globally corrected enrichment.
- **Conclusion**: Established evidence supports TACC3 as a network connector and spindle-associated regulator with relevance to cell division and possibly neurogenesis. The hypothesis that TACC3 organizes the entire shared module or mediates the brain-autonomic connection is not established by these data.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): UBTF (0.84), TACC3 (0.84), SMNDC1 (0.83), SUPT16H (0.82); STRING partners: ALYREF (0.844), HNRNPH1 (0.982)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_07581.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is a central RNA-processing node in the module and has high-confidence STRING relationships with HNRNPH1 and ALYREF. It belongs to the hu.MAP heterogeneous nuclear ribonucleoprotein assembly (hu.MAP huMAP3_07581.1) and appears in the supplementary RNA-metabolism set (STRING RCTM Metabolism of RNA; within-query FDR = 0.0286). Its established functions include RNA processing and regulation of alternative mRNA splicing. HPA shows enhancement in astrocytes, Bergmann glia, microglia, and oligodendrocyte progenitor cells, with protein detected in brain. It also has substantial literature and associations with neuromuscular and cancer-related conditions.
- **Conclusion**: Established evidence supports HNRNPL as a plausible RNA-processing hub contributing to the module's shared gene-expression signal, particularly in glial or other brain cell populations. A brain-autonomic-specific splicing mechanism remains a hypothesis.

#### PSMC2

- **Related proteins** (co-abundance neighbors): TACC3 (0.90), DHFR (0.88); STRING partners: PSMA1 (0.999), PSMC4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1, huMAP3_05064.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is a proteasome regulatory ATPase and is directly connected in STRING to PSMA1 and PSMC4. All three genes occur together in the proteasome-related hu.MAP assemblies (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1), and (hu.MAP huMAP3_05064.1). PSMC2 also appears in both supplementary STRING sets (STRING RCTM Metabolism of RNA; within-query FDR = 0.0286) and (STRING RCTM Negative regulation of NOTCH4 signaling; within-query FDR = 0.0286). Its established functions include ubiquitin-dependent proteasomal degradation and response to oxidative stress. HPA detects the protein in brain, and disease associations include plasma cell myeloma, mantle cell lymphoma, neoplasm, HIV infection, and amyloidosis.
- **Conclusion**: Established evidence supports PSMC2 as a representative proteasome component and a marker of protein-quality control within the module. Its co-abundance does not establish altered proteasome activity, a NOTCH4 mechanism, or a tissue-specific disease process.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): SUPT16H (0.88), ALYREF (0.80); STRING partners: ALYREF (0.89), PPIE (0.992)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_08980.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 connects the module to the spliceosome through a very strong STRING relationship with PPIE and through the spliceosome-related hu.MAP assemblies (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), and (hu.MAP huMAP3_09945.1). It also occurs in (hu.MAP huMAP3_08980.1) with GEMIN4 and in the supplementary RNA-metabolism set (STRING RCTM Metabolism of RNA; within-query FDR = 0.0286). Its established role is in spliceosomal snRNP assembly, spliceosome conformational change, and mRNA splicing. HPA detects it in brain. EFTUD2 has a substantial literature and established disease associations with mandibulofacial dysostosis with microcephaly, hereditary disease, neurodegenerative disease, and developmental delay.
- **Conclusion**: Established evidence supports EFTUD2 as a key spliceosomal representative that helps explain the RNA-processing arm of the module. A causal role for EFTUD2 in coordinating proteasome, transcription, and mitochondrial genes is not established.

#### POLR1B

- **Related proteins** (co-abundance neighbors): TACC3 (0.87), GEMIN4 (0.85), NSFL1C (0.85), PSMC4 (0.82), PSMA1 (0.82); STRING partners: SUPT16H (0.748), UBTF (0.863)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase I subunit B. Eukaryotic RNA polymerase I (pol I) is responsible for the transcription of ribosomal RNA (rRNA) genes and production of rRNA, the primary component of ribosomes. Pol I is a multisubunit enzyme composed of 6 to 14 polypeptides, depending on the species. Most of the mass of the pol I complex derives from the 2 largest subunits, Rpa1 and Rpa2 in yeast. POLR1B is homologous to Rpa2 (Seither and Grumm…
- **Diseases (Open Targets)**: Treacher Collins syndrome 4 (0.751); Treacher-Collins syndrome (0.383); arthropathy (0.212); Chronic Obstructive Asthma (0.188); lower respiratory tract disorder (0.124)
- **Europe PMC papers**: 521
- **Why important**: POLR1B has a relatively central position and connects TACC3, GEMIN4, NSFL1C, PSMC4, and PSMA1 in the module. It is the RNA polymerase I subunit responsible for ribosomal RNA transcription as part of the polymerase I machinery, and it connects in STRING to UBTF and SUPT16H. Its established annotations include ribosomal RNA transcription, transcription initiation and elongation, neural crest formation, and nucleolar function. Its disease associations include Treacher Collins syndrome and related craniofacial disorders. The available literature is smaller than for several other selected genes, but its molecular function is highly specific.
- **Conclusion**: Established evidence supports POLR1B as a marker of nucleolar and ribosome-biogenesis activity within the module. The connection to autonomic nervous system or brain biology is plausible through cellular biosynthetic demand, but is not demonstrated as a tissue-specific mechanism.

## Module 13

**Tissue pair**: autonomic_nervous_system and brain  
**Genes (7)**: LIMA1, MYO9B, PDXDC1, PRP4K, RBBP7, UBE2T, UCHL3

### Function

This module does not support a narrowly defined, statistically established pathway. No GO or KEGG term passed global correction, and there was no supplementary STRING functional enrichment. The gene annotations are heterogeneous: MYO9B and LIMA1 support actin-based movement, Rho signaling, actin filament organization and cell migration; PRP4K supports pre-mRNA splicing; RBBP7 supports chromatin remodeling and transcriptional regulation; UCHL3 and UBE2T support ubiquitin-dependent proteostasis and DNA-damage-related processes; and PDXDC1 is associated with cadherin binding, Golgi localization and predicted carboxylic-acid metabolism. Thus, the most defensible interpretation is a weakly integrated co-abundance pattern spanning cytoskeletal organization, nuclear RNA and chromatin regulation, protein modification and vesicle-associated biology, rather than a validated common molecular function.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of the genes is annotated as secreted. It is also not blood-cell enriched according to HPA; most genes have low immune-cell specificity, with one not detected in immune cells. Most genes have low tissue specificity, while a smaller subset is tissue enhanced. At the single-cell level, most genes are cell-type enhanced, with recurring annotations in trophoblast, spermatogenic, oocyte, epithelial, neuronal and myeloid populations. This mixture, together with the absence of a coherent neural-cell signature and the lack of matching autonomic-nervous-system protein data, means that shared sample cell composition or a broadly distributed cellular state could contribute substantially to the module. Brain protein detection is mixed rather than uniform, so the module should not automatically be interpreted as a brain-specific neuronal program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

None of the within-module gene pairs reached the supplied high-confidence STRING interaction threshold, and no STRING functional enrichment was reported. No hu.MAP complex contains multiple module members. Therefore, the co-abundance edges are not corroborated here as established physical protein interactions or as membership in a known multiprotein complex. The lack of STRING and hu.MAP support weakens a direct-complex interpretation, but it does not invalidate a transcriptional, cell-compositional or indirect regulatory relationship. Known biology remains present at the individual-gene level: MYO9B is an unconventional actin motor with Rho-related activity; LIMA1 is an actin-bundling and membrane-associated protein; PRP4K is linked to spliceosomal regulation; RBBP7 occurs in chromatin-remodeling and histone-deacetylase complexes; UCHL3 is a deubiquitinating enzyme; and UBE2T is a ubiquitin-conjugating enzyme involved in Fanconi-anemia-related DNA repair.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The conserved co-abundance pattern in this autonomic-nervous-system and brain tissue pair may be a new dataset-level observation, because the supplied resources provide no matching STRING interactions, no shared hu.MAP complex and no globally significant GO or KEGG term. However, it would be inappropriate to call the underlying biology a new pathway. Each selected gene has established molecular functions and disease or literature associations, and the module is heterogeneous. The most cautious conclusion is that the specific cross-tissue co-abundance configuration is potentially novel, whereas its biological interpretation remains provisional. Absence from STRING or hu.MAP alone is not evidence of novelty; replication in independent cohorts, preservation of the same edges, control for cell composition and targeted functional testing would be needed.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state or cell-composition signal that couples actin and membrane organization with nuclear RNA processing, chromatin regulation, ubiquitin-mediated protein control and vesicle biology. MYO9B and LIMA1 could represent the cytoskeletal component, PRP4K and RBBP7 a nuclear regulatory component, and UCHL3 with UBE2T a proteostasis or genome-maintenance component, while PDXDC1 may connect the pattern to Golgi or cadherin-associated biology. This is a mechanistic hypothesis rather than an established pathway. The alternative explanation that the pattern arises from mixed cell populations or shared technical and abundance effects should be treated as equally important until tested.

### Important genes

#### MYO9B

- **Related proteins** (co-abundance neighbors): UCHL3 (0.91), LIMA1 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin IXB. This gene encodes a member of the myosin family of actin-based molecular motor heavy chain proteins. The protein represents an unconventional myosin; it should not be confused with the conventional non-muscle myosin-9 (MYH9). The protein has four IQ motifs located in the neck domain that bind calmodulin, which serves as a light chain. The protein complex has a single-headed structure and exhibits …
- **Diseases (Open Targets)**: neurodegenerative disease (0.522); Abnormality of the skeletal system (0.470); hypertensive disorder (0.448); coronary artery disorder (0.406); essential hypertension (0.378)
- **Europe PMC papers**: 722
- **Why important**: MYO9B is a central network node connected to both LIMA1 and UCHL3, placing it at the interface between the actin-associated branch and ubiquitin-related biology. Its established function as an unconventional actin motor with Rho-GTPase-related activity gives the module a plausible cytoskeletal and signaling anchor. HPA detects the protein in brain, while its cell annotations include neuronal and myeloid populations. It also has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports MYO9B as the strongest cytoskeletal and signaling candidate in the module. It may help explain the co-abundance pattern, but its network position does not establish a physical interaction with the neighboring proteins. A role as a cross-tissue coordinator is therefore a hypothesis.

#### LIMA1

- **Related proteins** (co-abundance neighbors): MYO9B (0.90), RBBP7 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LIM domain and actin binding 1. This gene encodes a cytoskeleton-associated protein that inhibits actin filament depolymerization and cross-links filaments in bundles. It is downregulated in some cancer cell lines. Alternatively spliced transcript variants encoding different isoforms have been described for this gene, and expression of some of the variants maybe independently regulated. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.327); hypertensive disorder (0.276); malunion fracture (0.189); nephrotic syndrome (0.169); Abnormality of the skeletal system (0.157)
- **Europe PMC papers**: 1156
- **Why important**: LIMA1 is a network connector between MYO9B and RBBP7 and encodes an actin-associated protein that stabilizes and bundles actin filaments. Its plasma-membrane and actin-filament localization, together with annotations involving migration and ruffle organization, makes it an informative link between cytoskeletal state and broader cellular regulation. It has substantial literature coverage and HPA detects the protein in brain.
- **Conclusion**: Established evidence supports LIMA1 as a cytoskeletal and membrane-associated component. Its position suggests a possible bridge from actin organization toward nuclear or transcriptional state, but that bridge is inferred from co-abundance and is not demonstrated as a molecular mechanism.

#### RBBP7

- **Related proteins** (co-abundance neighbors): PDXDC1 (0.83), LIMA1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RB binding protein 7, chromatin remodeling factor. This protein is a ubiquitously expressed nuclear protein and belongs to a highly conserved subfamily of WD-repeat proteins. It is found among several proteins that binds directly to retinoblastoma protein, which regulates cell proliferation. The encoded protein is found in many histone deacetylase complexes, including mSin3 co-repressor complex. It is also present in protein complexes involved in …
- **Diseases (Open Targets)**: neurodegenerative disease (0.501); viral infectious disease (0.462); melanoma (0.408); breast carcinoma (0.380); cancer (0.378)
- **Europe PMC papers**: 1508
- **Why important**: RBBP7 connects LIMA1 with PDXDC1 and is a conserved nuclear chromatin-remodeling factor found in histone-deacetylase and chromatin-assembly complexes. Its annotations include transcriptional regulation, brain development and cell-growth control, and it has extensive literature and disease-association coverage. HPA detects the protein in brain.
- **Conclusion**: Established evidence supports RBBP7 as the principal chromatin and transcriptional-regulatory candidate. Its inclusion suggests that the module could reflect a cellular-state program rather than only cytoskeletal abundance. A direct functional connection to MYO9B or LIMA1 remains unproven.

#### PRP4K

- **Related proteins** (co-abundance neighbors): UBE2T (0.88), PDXDC1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pre-mRNA processing factor kinase PRP4K. Pre-mRNA splicing occurs in two sequential transesterification steps, and the protein encoded by this gene is thought to be involved in pre-mRNA splicing and in signal transduction. This protein belongs to a kinase family that includes serine/arginine-rich protein-specific kinases and cyclin-dependent kinases (CDKs). This protein is regarded as a CDK-like kinase (Clk) with homology to mitogen-acti…
- **Diseases (Open Targets)**: skin neoplasm (0.235); cardiomyopathy (0.227); placenta praevia (0.225); ovarian dysfunction (0.194); glomerulonephritis (0.096)
- **Europe PMC papers**: 126
- **Why important**: PRP4K is a connector between UBE2T and PDXDC1 and is annotated as a kinase involved in spliceosomal assembly, spliceosome conformational change and mRNA splicing. This gives the module a distinct RNA-processing axis that is not explained by the actin genes. Its literature volume is more limited than that of several other candidates, making it especially useful as a testable but less established component.
- **Conclusion**: Established evidence supports PRP4K as an RNA-splicing and signaling-related protein. Its co-abundance with ubiquitin and Golgi-associated candidates may indicate a shared cellular state, but there is no supplied evidence for a common complex or direct pathway.

#### UBE2T

- **Related proteins** (co-abundance neighbors): PRP4K (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin conjugating enzyme E2 T. The protein encoded by this gene catalyzes the covalent attachment of ubiquitin to protein substrates. Defects in this gene have been associated with Fanconi anemia of complementation group T. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2015].
- **Diseases (Open Targets)**: Fanconi anemia (0.792); myelodysplastic syndrome (0.482); acute myeloid leukemia (0.463); hepatocellular carcinoma (0.125); lung adenocarcinoma (0.117)
- **Europe PMC papers**: 1818
- **Why important**: UBE2T is a terminal network node linked to PRP4K and is an established ubiquitin-conjugating enzyme involved in DNA-damage response, protein ubiquitination and Fanconi-anemia biology. It has strong disease relevance and extensive literature coverage. Its HPA annotations include tissue enhancement and several proliferative or developmental cell types.
- **Conclusion**: Established evidence supports UBE2T as the module's clearest genome-maintenance and ubiquitin-system marker. Its association with PRP4K could reflect coordinated stress, proliferation or DNA-repair state, but this interpretation is hypothetical because the interaction is not supported by the supplied STRING or hu.MAP evidence.
