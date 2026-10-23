# Conserved co-abundance modules: autonomic_nervous_system and heart

## Module 0

**Tissue pair**: autonomic_nervous_system and heart  
**Genes (21)**: YWHAH, BZW2, HSPA5, DDX39B, DNM2, EIF3L, EMILIN1, FKBP4, FLNA, HNRNPR, EIF4A2, MESD, NAGK, PGM2, PSMC6, PSMC4, SCARB2, SEPTIN2, KARS1, RARS1, TIMM50

### Function

The strongest functional interpretation is a broadly expressed macromolecule-processing and protein-homeostasis module. (GO:BP macromolecule metabolic process; q_global = 0.0405) is the only GO/KEGG term passing global correction and links nearly the entire module to macromolecule metabolic process. The gene-level annotations refine this broad result into several connected activities: translational initiation and aminoacyl-tRNA charging through EIF3L, EIF4A2, KARS1 and RARS1; pre-mRNA processing and export through DDX39B and HNRNPR; proteasome-mediated protein turnover through PSMC4 and PSMC6; protein folding and ER homeostasis through HSPA5 and MESD; and cytoskeletal, vesicle-trafficking and membrane-associated processes through SEPTIN2, FLNA and DNM2. The network therefore appears to represent coordinated cellular maintenance rather than a specialized autonomic-nervous-system or cardiac signaling pathway. There were no STRING functional-enrichment terms, so STRING does not provide an independent enriched-process interpretation.

**Cell composition.** The module is not dominated by secreted or plasma proteins, and it does not show a strong blood-cell signature. HPA describes most genes as having low tissue specificity, while blood-cell specificity is generally low; SCARB2 is the notable gene with a group-enriched blood-cell pattern, and YWHAH is enriched in megakaryocytes and platelets. Several genes have cell-type enhancement in trophoblast, esophageal, reproductive, glial or other cell types, but these patterns are heterogeneous rather than forming a coherent blood-cell population. BZW2 is tissue-enhanced in heart muscle, skeletal muscle and tongue, and YWHAH is group-enriched in blood vessel and brain, whereas EMILIN1 is an extracellular-matrix secreted protein. Heart protein detection is present for many module proteins, but absent for some members, including EIF3L, FLNA, RARS1, PGM2 and EMILIN1. Overall, the composition is most consistent with broadly expressed intracellular housekeeping and proteostasis machinery, with possible contributions from shared vascular, stromal or other cell types rather than a plasma-protein signal.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP macromolecule metabolic process | 0.0405 | BZW2, DDX39B, DNM2, EIF3L, EIF4A2, EMILIN1, FKBP4, FLNA, HNRNPR, HSPA5, KARS1, MESD, PGM2, PSMC4, PSMC6, RARS1, TIMM50, YWHAH |

### STRING and hu.MAP

The high-confidence STRING evidence is sparse but biologically coherent. The DDX39B–HNRNPR relationship supports a shared RNA-processing and splicing component; EIF3L–EIF4A2 supports translation initiation; KARS1–RARS1 links aminoacyl-tRNA synthetase machinery; and PSMC4–PSMC6 links proteasome ATPase subunits. The hu.MAP evidence independently recovers these same module pairs in larger complexes: KARS1 and RARS1 occur together in aminoacyl-tRNA synthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), EIF3L and EIF4A2 occur together in translation-initiation complexes (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1), and PSMC4 and PSMC6 occur together in proteasome assemblies (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). DNM2 and BZW2 are jointly represented in a larger hu.MAP assembly (hu.MAP huMAP3_11232.1). These observations show that parts of the co-abundance module correspond to established molecular complexes. At the same time, most module edges are not supported by the listed high-confidence STRING interactions or hu.MAP pair recovery, so the full network should not be interpreted as a single experimentally established physical complex.

**STRING interactions (score >= 0.7)**: 4 of 210 gene pairs: DDX39B–HNRNPR (0.74); EIF3L–EIF4A2 (0.762); KARS1–RARS1 (0.999); PSMC4–PSMC6 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (RARS1, KARS1; 2/14); huMAP3_13688.1 (RARS1, KARS1; 2/14); huMAP3_13175.1 (EIF4A2, EIF3L; 2/20); huMAP3_11246.1 (EIF4A2, EIF3L; 2/24); huMAP3_05064.1 (PSMC4, PSMC6; 2/31); huMAP3_09656.1 (PSMC4, PSMC6; 2/64); huMAP3_13725.1 (PSMC4, PSMC6; 2/69); huMAP3_11232.1 (DNM2, BZW2; 2/78)

### Novelty

This is not sufficient evidence for a newly discovered molecular pathway. Several central relationships reproduce well-known translation, RNA-processing and proteasome assemblies, and the module is enriched for broadly expressed core cellular machinery. The potentially novel aspect is the coordinated co-abundance of these otherwise distinct systems across autonomic nervous system and heart samples, possibly reflecting shared cellular state, protein-production demand or sample composition. That dataset-level organization could be new, but novelty cannot be established from this fact sheet alone. The absence of many module relationships from STRING or hu.MAP is not proof of novelty, because those resources emphasize curated or experimentally supported physical interactions and may not capture co-abundance relationships, tissue context or indirect regulation.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular maintenance program active in autonomic nervous system and heart tissue. In this model, translational initiation and aminoacyl-tRNA charging supply protein synthesis, DDX39B and HNRNPR regulate processing and export of transcripts, HSPA5 and MESD support folding and membrane-protein handling, the proteasome removes damaged or unneeded proteins, and DNM2, SEPTIN2 and FLNA coordinate membrane and cytoskeletal remodeling. The apparent co-abundance may therefore arise when cells in both tissues experience common requirements for proteome renewal, trafficking and structural maintenance. This remains a hypothesis: the available evidence does not demonstrate direct physical coupling among all these processes, nor does it distinguish a shared cell-state program from variation in tissue or cell-type composition.

### Important genes

#### EIF3L

- **Related proteins** (co-abundance neighbors): RARS1 (0.90), HNRNPR (0.89), KARS1 (0.89), SCARB2 (0.87), MESD (0.86), PSMC4 (0.86), SEPTIN2 (0.85), HSPA5 (0.84), DDX39B (0.82); STRING partners: EIF4A2 (0.762)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13175.1, huMAP3_11246.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit L. Enables RNA binding activity. Contributes to translation initiation factor activity. Involved in translational initiation and viral translational termination-reinitiation. Located in membrane. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.503); Hydrocephalus (0.064); open-angle glaucoma (0.042); severe acute respiratory syndrome (0.032); COVID-19 (0.032)
- **Europe PMC papers**: 558
- **Why important**: EIF3L is the strongest network hub by weighted connectivity and links RARS1, HNRNPR, KARS1, MESD, PSMC4 and HSPA5 within the module. It is part of the eukaryotic translation-initiation machinery, appears in the globally supported macromolecule-metabolism term (GO:BP macromolecule metabolic process; q_global = 0.0405), and is paired with EIF4A2 by STRING and hu.MAP (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1). Its broad tissue profile and substantial literature support a core cellular role rather than a tissue-restricted function.
- **Conclusion**: Established: EIF3L is a translation-initiation component and a central connector in this module. Hypothesis: it may help couple protein synthesis to proteostasis and RNA-processing demand in the shared tissue state.

#### PSMC4

- **Related proteins** (co-abundance neighbors): RARS1 (0.89), NAGK (0.89), HSPA5 (0.88), YWHAH (0.88), SEPTIN2 (0.87), PGM2 (0.86), EIF3L (0.86), DDX39B (0.85); STRING partners: PSMC6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 4. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.603); mantle cell lymphoma (0.542); neoplasm (0.519); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1065
- **Why important**: PSMC4 is a prominent network hub and is connected to HSPA5, YWHAH, PGM2, EIF3L and DDX39B. It is a proteasome regulatory ATPase, belongs to the globally supported term (GO:BP macromolecule metabolic process; q_global = 0.0405), has a very strong STRING relationship with PSMC6, and is recovered with PSMC6 in multiple hu.MAP proteasome assemblies (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). Its heart protein detection and disease links involving malignancy and amyloidosis emphasize the relevance of proteostasis, although they do not establish a disease mechanism here.
- **Conclusion**: Established: PSMC4 is a proteasome component embedded in a supported proteasome submodule. Hypothesis: its coordinated abundance with translation and ER-homeostasis genes may indicate enhanced protein quality-control demand.

#### DDX39B

- **Related proteins** (co-abundance neighbors): SEPTIN2 (0.92), HNRNPR (0.90), FLNA (0.87), NAGK (0.87), PSMC4 (0.85), EIF3L (0.82); STRING partners: HNRNPR (0.74)
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nuclear speckles; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 39B. This gene encodes a member of the DEAD box family of RNA-dependent ATPases that mediate ATP hydrolysis during pre-mRNA splicing. The encoded protein is an essential splicing factor required for association of U2 small nuclear ribonucleoprotein with pre-mRNA, and it also plays an important role in mRNA export from the nucleus to the cytoplasm. This gene belongs to a cluster of genes localized in th…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); Alzheimer disease (0.522); Parkinson disease (0.503); lysosomal storage disease (0.503); neurodevelopmental disorder (0.413)
- **Europe PMC papers**: 1037
- **Why important**: DDX39B occupies a well-connected position near SEPTIN2, HNRNPR, FLNA, NAGK, PSMC4 and EIF3L. It is an RNA-dependent ATPase required for pre-mRNA splicing and nuclear mRNA export, is included in (GO:BP macromolecule metabolic process; q_global = 0.0405), and has a STRING-supported relationship with HNRNPR. Its nuclear-speckle localization, neural and glial cell-type enrichment, and substantial literature record make it a useful indicator of transcript-processing activity.
- **Conclusion**: Established: DDX39B supplies a plausible RNA-processing and export component of the module. Hypothesis: it may connect transcript maturation to the translational and proteostatic systems represented by EIF3L and PSMC4.

#### DNM2

- **Related proteins** (co-abundance neighbors): MESD (0.87), EMILIN1 (0.86), FKBP4 (0.86), BZW2 (0.86), KARS1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_11232.1
- **Function (MyGene.info)**: dynamin 2. Dynamins represent one of the subfamilies of GTP-binding proteins. These proteins share considerable sequence similarity over the N-terminal portion of the molecule, which contains the GTPase domain. Dynamins are associated with microtubules. They have been implicated in cell processes such as endocytosis and cell motility, and in alterations of the membrane that accompany certain activities such …
- **Diseases (Open Targets)**: autosomal dominant centronuclear myopathy (0.844); Charcot-Marie-Tooth disease dominant intermediate B (0.830); fetal akinesia-cerebral and retinal hemorrhage syndrome (0.739); autosomal dominant Charcot-Marie-Tooth disease type 2M (0.715); centronuclear myopathy (0.692)
- **Europe PMC papers**: 2412
- **Why important**: DNM2 connects the module to MESD, EMILIN1, FKBP4, BZW2 and KARS1 and is the most extensively studied gene among the selected structural and trafficking candidates. Its established functions include endocytosis, post-Golgi vesicle transport and autophagy, and it is represented in the larger hu.MAP assembly (hu.MAP huMAP3_11232.1). Its strong disease associations with centronuclear myopathy and Charcot-Marie-Tooth disease are particularly relevant to muscle and neural biology, while its heart detection supports tissue relevance.
- **Conclusion**: Established: DNM2 is a membrane-trafficking and cytoskeletal GTPase with important neuromuscular disease associations. Hypothesis: DNM2 may connect proteome maintenance to vesicle trafficking and structural remodeling in the shared module.

#### HSPA5

- **Related proteins** (co-abundance neighbors): PSMC4 (0.88), PGM2 (0.87), RARS1 (0.84), EIF3L (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 connects PSMC4, PGM2, RARS1 and EIF3L and is a major ER chaperone and regulator of ER homeostasis. It is included in (GO:BP macromolecule metabolic process; q_global = 0.0405), has heart protein detection, and is cell-type enhanced in several secretory or trophoblast-related populations. Its large literature base and disease associations involving neurodegeneration and cancer make it an informative marker of cellular stress and protein-folding capacity.
- **Conclusion**: Established: HSPA5 supports ER protein folding and unfolded-protein-response biology. Hypothesis: its co-abundance with translation, aminoacylation and proteasome genes may reflect coordinated management of newly synthesized or damaged proteins.

## Module 1

**Tissue pair**: autonomic_nervous_system and heart  
**Genes (20)**: GOT2, ABHD10, ACADM, ACSL1, AIFM1, MAOA, ATP5F1C, CMBL, FHL1, HSDL2, L2HGDH, IMMT, NDUFS1, NDUFS2, NFS1, NNT, PDHB, SLC25A12, SDHA, SUCLA2

### Function

The strongest supported interpretation is a mitochondrial energy-metabolism module. (GO:CC mitochondrion; q_global = 0.0164) provides the only GO/KEGG term that passed global correction: mitochondrion, with nearly the entire module represented. The gene content spans respiratory electron transfer and ATP production through NDUFS1, NDUFS2, SDHA and ATP5F1C; pyruvate entry and the tricarboxylic-acid cycle through PDHB, SDHA, SUCLA2 and GOT2; fatty-acid activation and oxidation through ACSL1 and ACADM; redox and metabolite transport through NNT and SLC25A12; and mitochondrial structure, cofactor assembly and stress-linked functions through IMMT, NFS1 and AIFM1. The STRING enrichment for mitochondrial localization, mitochondrial membrane and transit peptides (6 supplementary STRING terms; within-query FDR 0.00062–0.0288) independently supports this interpretation, but those terms are supplementary rather than globally corrected evidence. The co-abundance pattern therefore most plausibly reflects coordinated mitochondrial oxidative capacity and metabolic integration in autonomic nervous system and heart samples, rather than a narrowly specialized signaling pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and all module proteins are detected in heart muscle. It is also not strongly blood-cell driven. Most genes have low immune-cell specificity or are not detected in immune cells, with only limited immune-cell enhancement involving ACSL1, L2HGDH and FHL1. The composition instead suggests metabolically active structural and parenchymal cells. HPA enrichment is frequent in skeletal muscle, tongue, heart muscle, liver and related metabolically active tissues, with cell-type signals including cardiomyocytes, myonuclei, hepatocytes and adipocytes. Consequently, the shared module may reflect common mitochondrial abundance or oxidative metabolic state across autonomic and cardiac tissues, while tissue or cell-composition effects remain possible. The lack of a matching HPA autonomic-nervous-system tissue limits direct tissue-specific interpretation.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrion | 0.0164 | ABHD10, ACADM, ACSL1, AIFM1, ATP5F1C, GOT2, HSDL2, IMMT, L2HGDH, MAOA, NDUFS1, NDUFS2, NFS1, NNT, PDHB, SDHA, SLC25A12, SUCLA2 |

### STRING and hu.MAP

STRING contains many high-confidence relationships among the module genes, especially the dense respiratory and central-metabolism connections involving NDUFS1, NDUFS2, SDHA, SUCLA2, ATP5F1C, PDHB and GOT2. The strongest pattern is therefore not an isolated co-abundance artifact: several module edges correspond to known physical or functional associations in mitochondrial respiration and metabolism. STRING also links ACADM with ACSL1 and HSDL2, connecting fatty-acid handling to the broader mitochondrial network. hu.MAP provides partial complex-level support. (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1) repeatedly place NDUFS1 and NDUFS2 within large complex-I-related assemblies, although only a small portion of each assembly is represented in this module. (hu.MAP huMAP3_12388.1) places ACADM and NNT together in a separate complex context, and (hu.MAP huMAP3_12412.1) links NDUFS1 with ABHD10. Thus, the module combines established respiratory-complex relationships with coordinated metabolic genes that are not all members of a single experimentally defined complex. The network is best viewed as a cross-complex mitochondrial functional neighborhood rather than one discrete protein complex.

**STRING interactions (score >= 0.7)**: 21 of 190 gene pairs: ACADM–ACSL1 (0.728); ACADM–HSDL2 (0.835); ACADM–SUCLA2 (0.755); ATP5F1C–NDUFS1 (0.959); ATP5F1C–NDUFS2 (0.95); ATP5F1C–PDHB (0.913); ATP5F1C–SDHA (0.75); ATP5F1C–SUCLA2 (0.751); GOT2–NDUFS2 (0.802); GOT2–SDHA (0.981); IMMT–NDUFS1 (0.901); IMMT–NDUFS2 (0.735); NDUFS1–NDUFS2 (0.999); NDUFS1–PDHB (0.809); NDUFS1–SDHA (0.995); NDUFS1–SUCLA2 (0.777); NDUFS2–SDHA (0.998); NDUFS2–SUCLA2 (0.837); PDHB–SDHA (0.731); PDHB–SUCLA2 (0.921); SDHA–SUCLA2 (0.998)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Mitochondrion (FDR = 0.00062, 18 genes); Keyword Mitochondrion (FDR = 0.00067, 17 genes); Keyword Transit peptide (FDR = 0.0011, 14 genes); Component Mitochondrion (FDR = 0.0022, 18 genes); COMPARTMENTS Mitochondrial membrane (FDR = 0.0187, 12 genes); Component Mitochondrial membrane (FDR = 0.0288, 12 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12412.1 (NDUFS1, ABHD10; 2/5); huMAP3_12388.1 (ACADM, NNT; 2/7); huMAP3_14018.1 (NDUFS2, NDUFS1; 2/48); huMAP3_06397.1 (NDUFS2, NDUFS1; 2/49); huMAP3_09982.1 (NDUFS2, NDUFS1; 2/49); huMAP3_09567.1 (NDUFS2, NDUFS1; 2/52); huMAP3_14878.1 (NDUFS2, NDUFS1; 2/53)

### Novelty

The mitochondrial interpretation itself is not a new biological concept, because the module contains well-characterized respiratory, tricarboxylic-acid-cycle, fatty-acid and mitochondrial-carrier genes, and many of its relationships are already represented in STRING or hu.MAP. What may be novel is the specific conserved co-abundance configuration shared by autonomic nervous system and heart, particularly the way respiratory-chain, substrate-oxidation, redox, transport and mitochondrial-structure genes covary across those tissue groups. The fact sheet does not establish that this exact module has been previously reported, and absence from STRING or hu.MAP would not by itself demonstrate novelty. A defensible conclusion is therefore that the biological components are established, while the tissue-pair-specific co-abundance organization is a potentially novel observation requiring comparison with published co-expression modules and independent cohorts.

**Hypothesis.** Hypothesis: the shared module represents a coordinated mitochondrial reserve program that couples substrate supply and oxidation to respiratory-chain electron transport, proton-gradient use and redox buffering in energetically demanding autonomic and cardiac cells. In this model, ACSL1 and ACADM support fatty-acid utilization, PDHB and SUCLA2 connect carbon flux to the tricarboxylic-acid cycle, GOT2 and SLC25A12 support amino-acid and malate-aspartate exchange, NDUFS1 and NDUFS2 support complex-I electron transfer, SDHA supports succinate-linked respiration, ATP5F1C supports ATP synthesis, and NNT supports NADPH-dependent redox control. IMMT, NFS1 and AIFM1 could couple mitochondrial architecture, iron-sulfur-dependent enzyme competence and stress or cell-survival responses to this metabolic state. This is a mechanistic hypothesis, not proof of physical co-regulation or causal interaction; it should be tested with independent expression cohorts, cell-resolved data, respiratory phenotyping and perturbation experiments.

### Important genes

#### SDHA

- **Related proteins** (co-abundance neighbors): MAOA (0.93), NDUFS1 (0.89), NNT (0.86), HSDL2 (0.85); STRING partners: ATP5F1C (0.75), GOT2 (0.981), NDUFS1 (0.995), NDUFS2 (0.998), PDHB (0.731), SUCLA2 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate dehydrogenase complex flavoprotein subunit A. This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identi…
- **Diseases (Open Targets)**: mitochondrial complex II deficiency, nuclear type 1 (0.813); pheochromocytoma/paraganglioma syndrome 5 (0.790); dilated cardiomyopathy 1GG (0.768); neurodegeneration with ataxia and late-onset optic atrophy (0.761); gastrointestinal stromal tumor (0.743)
- **Europe PMC papers**: 12756
- **Why important**: SDHA is a central network node with strong connections to NDUFS1, NDUFS2, SUCLA2, GOT2 and NNT. It is the catalytic subunit of succinate dehydrogenase, linking the tricarboxylic-acid cycle to respiratory electron transfer. It is heart- and skeletal-muscle enhanced by HPA, has extensive STRING support, appears in the global mitochondrial term (GO:CC mitochondrion; q_global = 0.0164) and all listed STRING mitochondrial enrichments, and has substantial disease and literature support including mitochondrial respiratory-chain deficiency and cardiomyopathy associations.
- **Conclusion**: Established: SDHA is a strong anchor for the module's integrated respiratory and tricarboxylic-acid-cycle interpretation, supported by network position, annotation, STRING relationships and disease biology. Hypothesis: variation in SDHA abundance may help explain coordinated module behavior across heart and autonomic samples, but this dataset does not establish that SDHA drives the module.

#### NDUFS1

- **Related proteins** (co-abundance neighbors): SDHA (0.89), MAOA (0.84); STRING partners: ATP5F1C (0.959), IMMT (0.901), NDUFS2 (0.999), PDHB (0.809), SDHA (0.995), SUCLA2 (0.777)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_12412.1, huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S1. The protein encoded by this gene belongs to the complex I 75 kDa subunit family. Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Thi…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 5 (0.810); mitochondrial complex I deficiency (0.647); type 2 diabetes mellitus (0.608); Parkinson disease (0.603); diabetes mellitus (0.580)
- **Europe PMC papers**: 2567
- **Why important**: NDUFS1 is a core complex-I subunit and one of the most strongly connected respiratory genes in the module, with STRING links to ATP5F1C, IMMT, NDUFS2, PDHB, SDHA and SUCLA2. It participates in multiple hu.MAP complex-I assemblies (hu.MAP huMAP3_12412.1), (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1), appears in (GO:CC mitochondrion; q_global = 0.0164) and every listed STRING mitochondrial enrichment, and is enhanced in heart muscle, skeletal muscle and tongue by HPA. Its disease associations include complex-I deficiency, Parkinson disease and metabolic disease, giving it both mechanistic and clinical relevance.
- **Conclusion**: Established: NDUFS1 provides direct support that the module includes complex-I-linked oxidative phosphorylation biology and is not merely a generic mitochondrial annotation. Hypothesis: its covariation with substrate-processing genes may indicate coordinated adjustment of electron input to respiratory capacity, but the co-abundance data do not prove regulatory coupling.

#### NNT

- **Related proteins** (co-abundance neighbors): SDHA (0.86), AIFM1 (0.83), SLC25A12 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_12388.1
- **Function (MyGene.info)**: nicotinamide nucleotide transhydrogenase. This gene encodes an integral protein of the inner mitochondrial membrane. The enzyme couples hydride transfer between NAD(H) and NADP(+) to proton translocation across the inner mitochondrial membrane. Under most physiological conditions, the enzyme uses energy from the mitochondrial proton gradient to produce high concentrations of NADPH. The resulting NADPH is used for biosynthesis and in free …
- **Diseases (Open Targets)**: familial glucocorticoid deficiency (0.638); neurodegenerative disease (0.497); hereditary disease (0.453); atypical hemolytic-uremic syndrome with DGKE deficiency (0.416); Abnormality of the skeletal system (0.396)
- **Europe PMC papers**: 6111
- **Why important**: NNT occupies a metabolically informative position connecting SDHA, AIFM1 and SLC25A12. Its inner-membrane enzyme couples proton-gradient use to NADPH generation, linking oxidative phosphorylation with antioxidant and biosynthetic redox control. It is supported by (GO:CC mitochondrion; q_global = 0.0164) and (6 supplementary STRING terms; within-query FDR 0.00062–0.0288), has cardiomyocyte and myonuclear cell-type enhancement, and is associated with familial glucocorticoid deficiency and neurodegenerative disease. The ACADM–NNT hu.MAP relationship (hu.MAP huMAP3_12388.1) further connects redox capacity with fatty-acid metabolism.
- **Conclusion**: Established: NNT is a plausible redox-control bridge within the mitochondrial metabolic program and strengthens the interpretation beyond ATP production alone. Hypothesis: NNT may help buffer oxidative stress generated when respiratory and fatty-acid oxidation increase in cardiac or autonomic cells; this proposed role requires functional testing.

#### SLC25A12

- **Related proteins** (co-abundance neighbors): IMMT (0.92), HSDL2 (0.83), ACSL1 (0.83), AIFM1 (0.82), NNT (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 25 member 12. This gene encodes a calcium-binding mitochondrial carrier protein. The encoded protein localizes to the mitochondria and is involved in the exchange of aspartate for glutamate across the inner mitochondrial membrane. Polymorphisms in this gene may be associated with autism, and mutations in this gene may also be a cause of global cerebral hypomyelination. Alternatively spliced transcript variants …
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 39 (0.799); hereditary disease (0.416); Global developmental delay (0.370); developmental and epileptic encephalopathy, 1 (0.274); X-linked spasticity-intellectual disability-epilepsy syndrome (0.266)
- **Europe PMC papers**: 992
- **Why important**: SLC25A12 has the highest weighted degree in the module and connects IMMT, HSDL2, ACSL1, AIFM1 and NNT. It is a mitochondrial aspartate–glutamate carrier involved in the malate-aspartate shuttle and calcium-responsive metabolism. It is supported by (GO:CC mitochondrion; q_global = 0.0164) and multiple STRING mitochondrial terms, is enhanced in skeletal muscle and tongue with relevant neuronal and myonuclear signals, and has substantial literature and disease associations involving developmental epileptic encephalopathy and cerebral hypomyelination.
- **Conclusion**: Established: SLC25A12 is a high-centrality metabolite-transport component that links redox shuttling, amino-acid exchange and calcium-related mitochondrial function to the rest of the module. Hypothesis: it may coordinate neuronal-autonomic and cardiac metabolic demands, but the shared module does not demonstrate calcium-dependent regulation.

#### ACADM

- **Related proteins** (co-abundance neighbors): PDHB (0.89), GOT2 (0.83); STRING partners: ACSL1 (0.728), HSDL2 (0.835), SUCLA2 (0.755)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_12388.1
- **Function (MyGene.info)**: acyl-CoA dehydrogenase medium chain. This gene encodes the medium-chain specific (C4 to C12 straight chain) acyl-Coenzyme A dehydrogenase. The homotetramer enzyme catalyzes the initial step of the mitochondrial fatty acid beta-oxidation pathway. Defects in this gene cause medium-chain acyl-CoA dehydrogenase deficiency, a disease characterized by hepatic dysfunction, fasting hypoglycemia, and encephalopathy, which can result in infant…
- **Diseases (Open Targets)**: medium chain acyl-CoA dehydrogenase deficiency (0.854); hereditary disease (0.516); rhabdomyolysis (0.370); short chain acyl-CoA dehydrogenase deficiency (0.349); Epileptic spasm (0.333)
- **Europe PMC papers**: 4795
- **Why important**: ACADM connects PDHB and GOT2 in the module and has known STRING relationships with ACSL1, HSDL2 and SUCLA2. It catalyzes the initial step of medium-chain fatty-acid beta-oxidation, placing lipid substrate use alongside respiratory and tricarboxylic-acid-cycle genes. It is enhanced in liver, skeletal muscle and tongue, appears in (GO:CC mitochondrion; q_global = 0.0164) and (6 supplementary STRING terms; within-query FDR 0.00062–0.0288), is represented with NNT in hu.MAP (hu.MAP huMAP3_12388.1), and has a well-established medium-chain acyl-CoA dehydrogenase deficiency association.
- **Conclusion**: Established: ACADM identifies substrate oxidation as an important component of the module and helps explain its relevance to energetically demanding tissues. Hypothesis: coordinated ACADM abundance may reflect flexible fatty-acid fuel use supporting cardiac and autonomic mitochondrial respiration, but the data do not establish altered flux.

## Module 2

**Tissue pair**: autonomic_nervous_system and heart  
**Genes (16)**: AHNAK, APMAP, ATP1A1, CAPN1, CBR1, EIF3C, FLNB, FNTA, GET3, LTA4H, OLA1, PARVA, PLS3, SNX6, TPD52L2, XPNPEP1

### Function

No GO or KEGG term passed global correction, and no supplementary STRING functional-enrichment term was reported. The module therefore does not support a statistically established pathway-level annotation. Its gene-level composition instead suggests a membrane–cytoskeleton and intracellular-processing program. XPNPEP1 is the strongest network hub and encodes a cytosolic aminopeptidase involved in peptide processing; AHNAK and PLS3 are membrane-associated or actin-associated structural proteins; CAPN1 is an intracellular calcium-activated protease; PARVA and FLNB contribute to actin organization, adhesion, and membrane linkage; ATP1A1 supports ion gradients and electrical excitability; and SNX6, GET3, EIF3C, and OLA1 represent trafficking, membrane-protein insertion, translation, or ATPase-related functions. This is best interpreted as a mixed structural, membrane-homeostatic, and intracellular protein-processing module rather than as a demonstrated single biochemical pathway.

**Cell composition.** The module is not dominated by secreted or plasma proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity but strong cell-type enhancement, with repeated enrichment for esophageal epithelial and suprabasal cell types and additional signals from neuronal, glial, vascular, muscle-associated, hepatic, and platelet-related cell types. Immune-cell specificity is generally low, although PLS3 has group enrichment in NK-cell and plasmacytoid-DC populations and several genes have isolated immune or myeloid associations. Thus, a blood-cell explanation is not strongly supported, but shared cellular composition or broadly distributed structural and housekeeping programs could contribute to the conserved co-abundance pattern. Heart protein detection is widespread for the module, whereas the autonomic-nervous-system tissue has no matching HPA protein-detection category, so the HPA evidence does not establish equivalent protein expression in both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, AHNAK–CAPN1, supporting a known connection between a structural scaffold and an intracellular protease. No STRING functional-enrichment term was reported. hu.MAP supplies additional complex-level evidence: (hu.MAP huMAP3_14442.1) contains LTA4H, PLS3, XPNPEP1, and OLA1 among its module members, while (hu.MAP huMAP3_05674.1) contains FLNB and AHNAK. These observations support partial participation of several module proteins in previously characterized multiprotein assemblies, but they do not show that the whole co-abundance module is one physical complex. Most module edges lack corresponding high-confidence STRING support, so the co-abundance structure extends beyond currently catalogued protein interactions.

**STRING interactions (score >= 0.7)**: 1 of 120 gene pairs: AHNAK–CAPN1 (0.813)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (LTA4H, PLS3, XPNPEP1, OLA1; 4/57); huMAP3_05674.1 (FLNB, AHNAK; 2/12)

### Novelty

The conserved co-abundance pattern across autonomic nervous system and heart may be a useful systems-level observation, but it cannot be claimed as a new biological mechanism from this dataset alone. The absence of most edges from STRING or hu.MAP is not evidence of novelty, because co-abundance relationships can reflect shared regulation, cell composition, indirect effects, or context-specific interactions rather than stable physical binding. The lack of globally significant GO or KEGG enrichment also argues against assigning the module to a previously established canonical pathway. A genuinely novel module claim would require independent replication, control for cell composition, and experimental or perturbational validation of the predicted relationships.

**Hypothesis.** Hypothesis: the module reflects a conserved cell-state program coupling cytoskeletal and membrane organization to intracellular proteolysis, peptide or metabolite processing, ion-gradient maintenance, and membrane-protein trafficking. AHNAK, PLS3, FLNB, and PARVA could provide structural or adhesion-related coordination; CAPN1 could connect calcium-dependent proteolysis to remodeling; ATP1A1 could couple the program to membrane excitability; and XPNPEP1, LTA4H, SNX6, GET3, EIF3C, and OLA1 could represent associated processing, trafficking, translation, or proteostasis demands. In the two tissues, this may arise from a shared structural or vascular-associated cell population rather than from a heart-specific or autonomic-neuron-specific pathway. This remains a testable hypothesis, not an established module mechanism.

### Important genes

#### XPNPEP1

- **Related proteins** (co-abundance neighbors): PLS3 (0.96), LTA4H (0.89), CAPN1 (0.88), OLA1 (0.87), EIF3C (0.87), SNX6 (0.85), TPD52L2 (0.84), PARVA (0.83), AHNAK (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: X-prolyl aminopeptidase 1. This gene encodes the cytosolic form of a metalloaminopeptidase that catalyzes the cleavage of the N-terminal amino acid adjacent to a proline residue. The gene product may play a role in degradation and maturation of tachykinins, neuropeptides, and peptide hormones. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: preeclampsia (0.281); Hypercholesterolemia (0.257); bipolar disorder (0.251); bipolar I disorder (0.240); mathematical ability (0.212)
- **Europe PMC papers**: 4691
- **Why important**: XPNPEP1 is the principal network hub, linking structural, metabolic, trafficking, and processing-related genes across the module. Its established cytosolic aminopeptidase activity is relevant to degradation or maturation of tachykinins, neuropeptides, and peptide hormones, which is especially pertinent to tissues with autonomic and cardiac physiology. It also has substantial literature coverage and disease or trait associations, making it a strong entry point for experimental follow-up.
- **Conclusion**: Established evidence supports XPNPEP1 as a central co-abundance connector and cytosolic peptide-processing enzyme. The hypothesis that it coordinates neuropeptide or peptide-hormone processing with the other module proteins in heart or autonomic nervous system remains unproven.

#### AHNAK

- **Related proteins** (co-abundance neighbors): FLNB (0.89), CBR1 (0.87), CAPN1 (0.84), OLA1 (0.84), XPNPEP1 (0.82), PLS3 (0.82); STRING partners: CAPN1 (0.813)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_05674.1
- **Function (MyGene.info)**: AHNAK nucleoprotein. The protein encoded by this gene is a large (700 kDa) structural scaffold protein consisting of a central domain with 128 aa repeats. The encoded protein may play a role in such diverse processes as blood-brain barrier formation, cell structure and migration, cardiac calcium channel regulation, and tumor metastasis. A much shorter variant encoding a 17 kDa isoform exists for this gene, and the sho…
- **Diseases (Open Targets)**: Aganglionic megacolon (0.266); neoplasm (0.108); hepatocellular carcinoma (0.093); cancer (0.085); melanoma (0.085)
- **Europe PMC papers**: 2886
- **Why important**: AHNAK occupies a central position among the structural subnetwork members and is the only module gene with a high-confidence STRING relationship, namely with CAPN1. It is a large membrane-associated and cytosolic scaffold implicated in cell structure, migration, plasma-membrane repair, blood-brain-barrier formation, and cardiac calcium-channel regulation. It also participates in (hu.MAP huMAP3_05674.1) with FLNB, giving independent complex-level support for a structural role.
- **Conclusion**: Established evidence supports AHNAK as a scaffold-like structural component with a known relationship to CAPN1 and a known complex association with FLNB. Its proposed role as the organizer that couples membrane repair or calcium-channel regulation to the broader module is a hypothesis.

#### PLS3

- **Related proteins** (co-abundance neighbors): XPNPEP1 (0.96), CAPN1 (0.89), OLA1 (0.84), AHNAK (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cytosol; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: plastin 3. Plastins are a family of actin-binding proteins that are conserved throughout eukaryote evolution and expressed in most tissues of higher eukaryotes. In humans, two ubiquitous plastin isoforms (L and T) have been identified. Plastin 1 (otherwise known as Fimbrin) is a third distinct plastin isoform which is specifically expressed at high levels in the small intestine. The L isoform is expressed on…
- **Diseases (Open Targets)**: X-linked osteoporosis with fractures (0.727); congenital diaphragmatic hernia (0.553); osteoporosis (0.477); hernia, anterior diaphragmatic (0.380); postmenopausal osteoporosis (0.341)
- **Europe PMC papers**: 1365
- **Why important**: PLS3 is directly connected to XPNPEP1, CAPN1, OLA1, and AHNAK and is included in (hu.MAP huMAP3_14442.1). Its established actin-bundling function, membrane and cytosolic localization, vascular-tissue enhancement, and associations with synaptic-vesicle and presynaptic actin organization make it relevant to both structural remodeling and excitable-tissue biology. Its disease associations include skeletal and connective-tissue phenotypes, while its literature base is substantial.
- **Conclusion**: Established evidence supports PLS3 as an actin-organizing and complex-associated component that could connect cell architecture to membrane processes. A specific role in coordinating the conserved heart–autonomic co-abundance program remains a hypothesis.

#### CAPN1

- **Related proteins** (co-abundance neighbors): PLS3 (0.89), XPNPEP1 (0.88), AHNAK (0.84); STRING partners: AHNAK (0.813)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calpain 1. The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpa…
- **Diseases (Open Targets)**: Autosomal recessive spastic paraplegia type 76 (0.781); Alzheimer disease (0.383); neurodegenerative disease (0.326); hereditary spastic paraplegia 11 (0.266); hereditary disease (0.193)
- **Europe PMC papers**: 1869
- **Why important**: CAPN1 is connected to the structural core formed by PLS3 and AHNAK and is the partner in the module's high-confidence STRING relationship with AHNAK. It is an established calcium-activated intracellular cysteine protease involved in proteolysis, autophagy regulation, and signaling. Its strong disease relevance includes hereditary spastic paraplegia and neurodegenerative associations, making it important for a module spanning cardiac and autonomic tissues.
- **Conclusion**: Established evidence supports CAPN1 as a calcium-responsive proteolytic component linked to AHNAK. The hypothesis that CAPN1-mediated remodeling helps couple calcium or membrane stress to the module's cytoskeletal state requires direct functional testing.

#### ATP1A1

- **Related proteins** (co-abundance neighbors): EIF3C (0.88), APMAP (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 provides a distinct physiological anchor because it maintains sodium and potassium gradients required for osmoregulation, membrane potential, and electrical excitability in nerve and muscle. It connects the module to EIF3C and APMAP and has established associations with axonal disease, seizures, atrial fibrillation, and heart failure. Although it is not a high-connectivity hub, its function is highly relevant to the tissue pair.
- **Conclusion**: Established evidence supports ATP1A1 as an ion-homeostasis and excitability component with cardiac and neurological disease relevance. Its placement in this module may indicate coupling between structural or proteostatic state and membrane excitability, but that coupling is a hypothesis.

## Module 3

**Tissue pair**: autonomic_nervous_system and heart  
**Genes (11)**: ANXA2, ASPH, HNRNPH1, HNRNPL, PKM, LDHA, PFKP, PLCXD3, PSMC2, PSMA1, SERPINH1

### Function

The module does not support a globally significant GO or KEGG functional annotation: no globally significant GO/KEGG term passed global correction. Its structure nevertheless suggests a composite intracellular program rather than a single established pathway. The strongest coherent signals are RNA processing through HNRNPH1 and HNRNPL, proteasome-related protein turnover through PSMA1 and PSMC2, and glycolytic metabolism through LDHA, PKM, and PFKP. SERPINH1 adds a protein-folding and collagen-biosynthesis connection, while PLCXD3 and ASPH suggest possible lipid-signaling and calcium-related links. These interpretations are based on the gene annotations and network structure, not on significant GO or KEGG enrichment.

**Cell composition.** The module is not predominantly composed of secreted or plasma proteins, and it is not broadly characterized as a blood-cell module. Most genes have low tissue specificity and low immune-cell specificity, although the HPA data include isolated immune-cell enrichments. ANXA2 is secreted to blood and has blood-cell enrichment, so some sample-level association with blood or myeloid components is possible, but this does not explain the entire module. The HPA patterns instead indicate a mixture of broadly expressed intracellular proteins with tissue-enhanced signals in heart muscle, brain, skeletal muscle, esophagus, adipose tissue, tongue, ovary, and retina. The single-cell annotations are diverse, including cardiomyocytes, neural and glial cells, epithelial cells, adipocytes, trophoblast-related cells, and selected immune cells. Heart protein detection is present for several members, whereas autonomic-nervous-system protein detection is unavailable in the supplied HPA comparison.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a small set of known relationships rather than a densely documented interaction network. HNRNPH1–HNRNPL is a strong known association consistent with an hnRNP RNA-processing pair. LDHA–PKM and LDHA–PFKP, together with PFKP–PKM, support a glycolytic subnetwork. PSMA1–PSMC2 is a very strong proteasome association. No STRING functional-enrichment result was reported. hu.MAP independently places PSMA1 and PSMC2 together in the proteasome-related complexes (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1). The fact that these complexes contain many additional proteasome components, while only these members occur in the module, supports a real proteasome connection but not a complete proteasome module. The remaining cross-links, especially those involving SERPINH1, ANXA2, PLCXD3, and PSMC2, are less directly established by the supplied STRING and hu.MAP evidence and may reflect co-abundance or shared cellular context rather than physical binding.

**STRING interactions (score >= 0.7)**: 5 of 55 gene pairs: HNRNPH1–HNRNPL (0.982); LDHA–PFKP (0.841); LDHA–PKM (0.997); PFKP–PKM (0.927); PSMA1–PSMC2 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09656.1 (PSMA1, PSMC2; 2/64); huMAP3_13725.1 (PSMA1, PSMC2; 2/69)

### Novelty

This should not be claimed as a newly discovered molecular complex or pathway. Several core relationships are already well established through STRING and hu.MAP, including the hnRNP pair, glycolytic enzyme relationships, and the proteasome association. The potentially interesting aspect is the tissue-pair co-abundance pattern connecting RNA processing, proteostasis, glycolysis, collagen-related folding, membrane or lipid signaling, and calcium-linked biology across autonomic nervous system and heart. That systems-level co-abundance configuration may be novel, but the supplied evidence does not establish biological novelty, causality, or a tissue-specific mechanism. Absence of STRING or hu.MAP support for some edges is insufficient to prove novelty.

**Hypothesis.** Hypothesis: the module reflects a shared cellular stress and metabolic-maintenance state present across autonomic nervous system and heart samples. In this model, glycolytic capacity from LDHA, PKM, and PFKP supplies rapid energy and redox support; proteasome components PSMA1 and PSMC2 remove damaged or unwanted proteins; hnRNP proteins coordinate RNA processing; and SERPINH1 helps manage endoplasmic-reticulum protein folding and collagen-related biosynthesis. ANXA2, PLCXD3, and ASPH could connect this maintenance state to membrane organization, lipid signaling, and calcium handling. This is a mechanistic hypothesis generated from co-abundance and annotations, not an established causal pathway.

### Important genes

#### SERPINH1

- **Related proteins** (co-abundance neighbors): HNRNPH1 (0.92), PLCXD3 (0.88), LDHA (0.87), HNRNPL (0.86), PSMC2 (0.86), ANXA2 (0.85), PKM (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family H member 1. This gene encodes a member of the serpin superfamily of serine proteinase inhibitors. The encoded protein is localized to the endoplasmic reticulum and plays a role in collagen biosynthesis as a collagen-specific molecular chaperone. Autoantibodies to the encoded protein have been found in patients with rheumatoid arthritis. Expression of this gene may be a marker for cancer, and nucleotide polymo…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 10 (0.714); preterm premature rupture of the membranes (0.559); coronary artery disorder (0.554); myocardial infarction (0.510); Abnormality of the skeletal system (0.474)
- **Europe PMC papers**: 2762
- **Why important**: SERPINH1 has the strongest network position in the module and links the RNA-associated, proteasome-associated, and glycolytic portions of the graph. Its established annotation as an endoplasmic-reticulum collagen-specific chaperone connects the module to protein folding and collagen biosynthesis. Its disease associations include osteogenesis imperfecta, preterm premature rupture of membranes, coronary artery disorder, and myocardial infarction, and it has substantial literature support.
- **Conclusion**: Established evidence supports SERPINH1 as a central co-abundance connector with a protein-folding and collagen-biosynthesis role. Its position makes it a plausible integrator of cellular proteostasis and tissue-structural biology. It is only a hypothesis that SERPINH1 drives the shared autonomic-nervous-system and heart module or directly links the other functional groups.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): ANXA2 (0.89), PSMC2 (0.89), PSMA1 (0.87), SERPINH1 (0.86), PLCXD3 (0.82), HNRNPH1 (0.82); STRING partners: HNRNPH1 (0.982)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is among the most connected genes and is linked to HNRNPH1 through a strong STRING association. Its established function in hnRNP complexes, RNA processing, and alternative splicing provides a coherent nuclear-RNA interpretation. It is detected in heart and has substantial literature support, with disease associations including dengue disease, neuromuscular disease, and cancer-related conditions.
- **Conclusion**: Established evidence supports HNRNPL as a representative RNA-processing component and as part of a known hnRNP relationship with HNRNPH1. Its broad tissue profile is compatible with a general cellular maintenance program. A heart or autonomic-neural specific splicing mechanism remains a hypothesis.

#### PSMC2

- **Related proteins** (co-abundance neighbors): HNRNPL (0.89), SERPINH1 (0.86), ASPH (0.86), PSMA1 (0.84), PLCXD3 (0.83); STRING partners: PSMA1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in heart
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 occupies a central position in the network and connects to HNRNPL, SERPINH1, ASPH, PSMA1, and PLCXD3. It is supported by the strongest supplied proteasome STRING relationship with PSMA1 and occurs with PSMA1 in the hu.MAP complexes (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1). Its established role as a proteasome ATPase links the module to ubiquitin-dependent protein catabolism and oxidative-stress responses. It is detected in heart and has disease associations involving plasma-cell myeloma, mantle-cell lymphoma, neoplasm, HIV infection, and amyloidosis.
- **Conclusion**: Established evidence supports PSMC2 as the clearest proteasome anchor in the module and confirms that part of the network corresponds to a known proteasome complex. It may mark proteostasis demand in the shared tissues, but the co-abundance data do not establish altered proteasome activity or a disease mechanism.

#### ANXA2

- **Related proteins** (co-abundance neighbors): HNRNPL (0.89), SERPINH1 (0.85), PSMA1 (0.85), PFKP (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A2. This gene encodes a member of the annexin family. Members of this calcium-dependent phospholipid-binding protein family play a role in the regulation of cellular growth and in signal transduction pathways. This protein functions as an autocrine factor which heightens osteoclast formation and bone resorption. This gene has three pseudogenes located on chromosomes 4, 9 and 10, respectively. Multiple…
- **Diseases (Open Targets)**: neurodegenerative disease (0.443); Alzheimer disease (0.312); Parkinson disease (0.298); lysosomal storage disease (0.289); benign urinary system neoplasm (0.270)
- **Europe PMC papers**: 12966
- **Why important**: ANXA2 has a strong central position linking HNRNPL, SERPINH1, PSMA1, and PFKP. Its established functions include calcium-dependent membrane association, angiogenesis, membrane-raft assembly, receptor recycling, vesicle budding, and cell adhesion. HPA identifies it as secreted to blood, tissue-enhanced in esophagus, and enriched in several blood and epithelial cell types. It has the largest literature volume among the module genes and disease associations involving neurodegenerative disease and Alzheimer disease.
- **Conclusion**: Established evidence supports ANXA2 as a membrane and trafficking-related connector that could also reflect epithelial or blood-derived material in samples. Its centrality makes it important for interpreting the module, but its presence does not prove that the module is vascular, immune, or secreted. A direct role in coupling glycolysis or proteostasis to autonomic-heart biology is hypothetical.

#### PLCXD3

- **Related proteins** (co-abundance neighbors): SERPINH1 (0.88), PSMA1 (0.85), PSMC2 (0.83), HNRNPL (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphatidylinositol specific phospholipase C X domain containing 3. Predicted to enable phosphoric diester hydrolase activity. Predicted to be involved in lipid catabolic process and signal transduction. Predicted to be located in cytoplasm. Predicted to be active in glutamatergic synapse. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: response to xenobiotic stimulus (0.308); alcohol drinking (0.299); Proptosis (0.294); Alzheimer disease (0.216); breast disorder (0.210)
- **Europe PMC papers**: 275
- **Why important**: PLCXD3 is connected to SERPINH1, PSMA1, PSMC2, and HNRNPL and is tissue-enhanced in brain, heart muscle, and ovary. Its established annotation is limited but supports phosphoric diester hydrolase activity, lipid catabolism, signal transduction, and possible glutamatergic-synapse localization. HPA also identifies enrichment in cardiomyocytes and brain neurons, making it particularly relevant to the tissue pair despite its relatively modest literature volume.
- **Conclusion**: Established evidence supports PLCXD3 as a heart- and nervous-system-relevant candidate with possible lipid-signaling functions. Its network placement suggests it may connect tissue-specific signaling to the broader maintenance module. The precise biochemical role and any direct contribution to autonomic or cardiac co-abundance remain hypotheses because its annotation is comparatively limited.

#### LDHA

- **Related proteins** (co-abundance neighbors): SERPINH1 (0.87), PKM (0.83); STRING partners: PFKP (0.841), PKM (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lactate dehydrogenase A. This gene encodes the A subunit of lactate dehydrogenase enzyme which catalyzes the reversible conversion of pyruvate to lactate with the concomitant oxidation of NADH to NAD in anaerobic glycolysis. The protein is found predominantly in skeletal muscle and belongs to the lactate dehydrogenase family. Mutations in this gene have been linked to exertional myoglobinuria. The human genome contains se…
- **Diseases (Open Targets)**: glycogen storage disease due to lactate dehydrogenase M-subunit deficiency (0.755); disorder of glycogen metabolism (0.505); glycogen storage disease XV (0.505); primary hyperoxaluria (0.447); hereditary disease (0.190)
- **Europe PMC papers**: 20747
- **Why important**: LDHA forms a coherent STRING-supported glycolytic cluster with PKM and PFKP and is connected in the module to SERPINH1. Its established role is reversible pyruvate-to-lactate conversion during glycolysis, with relevance to muscle metabolism. It has strong literature support and disease associations involving lactate-dehydrogenase deficiency and glycogen metabolism.
- **Conclusion**: Established evidence supports LDHA as a metabolic component of the module and, together with PKM and PFKP, as evidence for coordinated glycolytic capacity. The module does not demonstrate increased glycolytic flux, lactate production, or a specific cardiac or autonomic metabolic state; those are hypotheses requiring direct metabolic measurements.

## Module 4

**Tissue pair**: autonomic_nervous_system and heart  
**Genes (10)**: ANXA5, CLIC1, GANAB, SHMT2, ISOC1, PGK1, PSMD13, RAN, FARSB, CCT8

### Function

This is a heterogeneous cellular maintenance module rather than a clearly defined pathway module. Its genes span cytosolic chaperoning and protein folding through CCT8, nuclear transport and cell-cycle-related functions through RAN, glycolysis through PGK1, mitochondrial one-carbon and glycine metabolism through SHMT2, protein quality control through GANAB and PSMD13, translation through FARSB, and membrane, calcium, redox, or coagulation-related functions through CLIC1 and ANXA5. The co-abundance structure therefore most plausibly reflects coordinated general cellular state, protein homeostasis, energy or biosynthetic demand, rather than a single established biochemical pathway. No GO or KEGG term passed global correction, so there is no globally significant pathway annotation to use as primary functional evidence. The absence of a globally enriched term does not invalidate the module, but it limits confidence in assigning a specific function.

**Cell composition.** The module is not dominated by secreted proteins or blood-cell-enriched proteins. HPA reports low tissue specificity for nearly all members, low immune-cell specificity throughout, and only a single secretome annotation. The cell-type annotations are distributed across several epithelial, reproductive, hepatic, and other cell types rather than concentrated in blood cells. One member is tissue-enhanced in liver, while the remainder are broadly distributed. This profile is more consistent with a broadly expressed cellular program or shared cell-state signal than with a plasma-protein or blood-contamination module. Heart protein detection is present for several members, whereas matching autonomic-nervous-system protein evidence is unavailable. The cell-type enrichment patterns, including trophoblast, oocyte, and esophageal-cell annotations, should not be interpreted as evidence that those cell types are present in the two tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only reported high-confidence STRING relationship within the module is between CCT8 and RAN. This supports a specific connection between chaperone-related protein handling and nuclear transport, but it does not establish the entire module as a physical complex. There is no STRING functional-enrichment result and no hu.MAP complex containing multiple module members. Most co-abundance edges therefore lack corresponding database support in the supplied evidence. The network appears to contain a relatively central CLIC1 and CCT8 region, with RAN linking the CCT8 and CLIC1 portions, while other relationships connect metabolic, proteostasis, translation, and membrane-associated genes. These observations favor coordinated regulation or shared cellular state over a single experimentally established multiprotein assembly.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: CCT8–RAN (0.712)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unrecognized co-abundance pattern shared by autonomic nervous system and heart, but the evidence is insufficient to call it a new biological mechanism. Its constituent genes are individually well characterized, and the CCT8-RAN relationship is already represented in STRING. At the same time, the absence of a multi-member hu.MAP complex, the lack of STRING enrichment, and the lack of globally significant GO or KEGG enrichment indicate that the particular cross-tissue combination and its co-abundance organization are not explained by an established database pathway or complex. Thus, the defensible conclusion is novelty of the observed module-level association as a candidate finding, not proof of novelty of the genes, their functions, or their pairwise biology. Independent replication, cell-composition controls, and experimental testing would be required.

**Hypothesis.** Hypothesis: the module reflects a shared cellular stress and biosynthetic state in autonomic nervous system and heart cells. In this model, CCT8 supports folding of newly synthesized proteins, RAN supports nuclear transport and cell-cycle or nucleic-acid-related logistics, PGK1 and SHMT2 support glycolytic and mitochondrial one-carbon metabolism, while CLIC1, ANXA5, PSMD13, and GANAB contribute to membrane, redox, degradation, and endoplasmic-reticulum quality-control processes. The observed co-abundance could therefore arise when cells coordinate protein production, trafficking, energy metabolism, and quality control. This is a mechanistic proposal, not an established pathway assignment, because the enrichment analyses and complex databases do not independently support a unified pathway.

### Important genes

#### CLIC1

- **Related proteins** (co-abundance neighbors): RAN (0.92), ANXA5 (0.86), FARSB (0.83), CCT8 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CLIC family member 1. Chloride channels are a diverse group of proteins that regulate fundamental cellular processes including stabilization of cell membrane potential, transepithelial transport, maintenance of intracellular pH, and regulation of cell volume. Chloride intracellular channel 1  is a member of the p64 family; the protein localizes principally to the cell nucleus and exhibits both nuclear and plasma membra…
- **Diseases (Open Targets)**: spermatogenic failure 74 (0.333); neoplasm (0.115); glioblastoma (0.114); gastric cancer (0.102); central nervous system cancer (0.099)
- **Europe PMC papers**: 4339
- **Why important**: CLIC1 has a central position in the module and connects the RAN, ANXA5, FARSB, and CCT8 portions of the network. Its established functions include chloride transport, signal transduction, platelet aggregation, and cellular oxidant detoxification. It is detected in heart by HPA, is broadly tissue distributed, and has extensive literature and disease-linked associations including neoplastic and central-nervous-system conditions. Its network position makes it a useful candidate coordinator, although the module does not establish that it causally organizes the other genes.
- **Conclusion**: Established evidence supports CLIC1 as a broadly expressed membrane or cytosolic regulator with redox and signaling relevance and as a network-central member. The hypothesis that CLIC1 helps couple membrane or redox state to the rest of this module remains unproven.

#### CCT8

- **Related proteins** (co-abundance neighbors): RAN (0.89), PGK1 (0.84), CLIC1 (0.83), SHMT2 (0.81); STRING partners: RAN (0.712)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is among the most connected module members and links RAN, PGK1, CLIC1, and SHMT2. It is a subunit of the CCT chaperonin, which participates in folding and stabilization of newly synthesized proteins. The CCT8-RAN relationship is the sole reported high-confidence STRING interaction within the module, giving CCT8 the strongest direct database-supported bridge between network structure and molecular function. It is detected in heart and has substantial literature concerning protein folding and disease biology.
- **Conclusion**: Established evidence supports CCT8 as a plausible proteostasis anchor and as the best-supported physical-interaction entry point in the module. Whether its co-abundance with metabolic and membrane genes reflects a shared stress response or coordinated translation demand is a hypothesis.

#### RAN

- **Related proteins** (co-abundance neighbors): CLIC1 (0.92), CCT8 (0.89); STRING partners: CCT8 (0.712)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAN, member RAS oncogene family. RAN (ras-related nuclear protein) is a small GTP binding protein belonging to the RAS superfamily that is essential for the translocation of RNA and proteins through the nuclear pore complex. The RAN protein is also involved in control of DNA synthesis and cell cycle progression. Nuclear localization of RAN requires the presence of regulator of chromosome condensation 1 (RCC1). Mutations in RAN di…
- **Diseases (Open Targets)**: HIV infectious disease (0.565); Orthomyxoviridae infectious disease (0.376); pemphigus foliaceus (0.298); neurodegenerative disease (0.270); Genu valgum (0.136)
- **Europe PMC papers**: 133080
- **Why important**: RAN links the CCT8 and CLIC1 regions and is the second participant in the sole reported STRING interaction. Its established functions include nuclear import and export, ribosomal subunit export, DNA metabolism, and cell-cycle processes. It is one of the most extensively studied genes in the module and has broad disease associations, including neurodegenerative and infectious-disease contexts. Its position makes it informative for interpreting the module as involving intracellular logistics rather than only metabolism.
- **Conclusion**: Established evidence supports RAN as a central nuclear-transport and nucleic-acid-related regulator with strong database support for its connection to CCT8. A role for RAN in coupling nuclear transport to the cross-tissue co-abundance state is plausible but not demonstrated.

#### PGK1

- **Related proteins** (co-abundance neighbors): ANXA5 (0.86), CCT8 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece, Principal piece, End piece; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglycerate kinase 1. The protein encoded by this gene is a glycolytic enzyme that catalyzes the conversion of 1,3-diphosphoglycerate to 3-phosphoglycerate. The encoded protein may also act as a cofactor for polymerase alpha. Additionally, this protein is secreted by tumor cells where it participates in angiogenesis by functioning to reduce disulfide bonds in the serine protease, plasmin, which consequently leads to th…
- **Diseases (Open Targets)**: glycogen storage disease due to phosphoglycerate kinase 1 deficiency (0.823); Menkes disease (0.578); X-linked distal spinal muscular atrophy type 3 (0.556); occipital horn syndrome (0.556); hereditary disease (0.520)
- **Europe PMC papers**: 14784
- **Why important**: PGK1 connects CCT8 and ANXA5 and provides the clearest canonical energy-metabolism component of the module. It catalyzes a glycolytic reaction and also has described roles in angiogenesis and plasminogen activation. It is detected in heart, is broadly expressed, has extensive literature, and is associated with PGK1-deficiency disorders and other disease phenotypes. Its network placement supports a possible link between metabolic demand and the proteostasis or membrane-related portions of the module.
- **Conclusion**: Established evidence supports PGK1 as a glycolytic enzyme with additional context-dependent functions. The hypothesis that its co-abundance marks energetic support for protein handling in the shared tissues requires metabolic and cell-type validation.

#### SHMT2

- **Related proteins** (co-abundance neighbors): CCT8 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine hydroxymethyltransferase 2. This gene encodes the mitochondrial form of a pyridoxal phosphate-dependent enzyme that catalyzes the reversible reaction of serine and tetrahydrofolate to glycine and 5,10-methylene tetrahydrofolate. The encoded product is primarily responsible for glycine synthesis. The activity of the encoded protein has been suggested to be the primary source of intracellular glycine. The gene which encodes th…
- **Diseases (Open Targets)**: neurodevelopmental disorder with cardiomyopathy, spasticity, and brain abnormalities (0.771); microcephaly (0.370); polymicrogyria (0.370); neurodevelopmental disorder (0.336); hereditary disease (0.192)
- **Europe PMC papers**: 2579
- **Why important**: SHMT2 connects to CCT8 and supplies the module's clearest mitochondrial biosynthetic component. It supports glycine production and serine, folate, and one-carbon metabolism, with additional annotation related to oxidative phosphorylation. It is tissue-enhanced in liver, is associated with neurodevelopmental disorders involving cardiomyopathy, and has a substantial literature base. Although it has only a peripheral network position, its function complements PGK1 and could help explain coordinated metabolic co-abundance.
- **Conclusion**: Established evidence supports SHMT2 as a mitochondrial one-carbon and glycine-metabolism enzyme with disease relevance to neurodevelopment and cardiomyopathy. Its participation in a shared metabolic-proteostasis program in autonomic nervous system and heart is a hypothesis rather than a demonstrated mechanism.

#### ANXA5

- **Related proteins** (co-abundance neighbors): CLIC1 (0.86), PGK1 (0.86), PSMD13 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A5. The Annexin 5 gene spans 29 kb containing 13 exons, and encodes a single transcript of approximately 1.6 kb and a protein product with a molecular weight of about 35 kDa.The protein encoded by this gene belongs to the annexin family of calcium-dependent phospholipid binding proteins some of which have been implicated in membrane-related events along exocytotic and endocytotic pathways. Annexin 5 i…
- **Diseases (Open Targets)**: habitual spontaneous abortion (0.370); complication (0.124); herpes zoster (0.124); nervous system disorder (0.124); neoplasm (0.118)
- **Europe PMC papers**: 3276
- **Why important**: ANXA5 connects CLIC1, PGK1, and PSMD13, placing it at the interface of membrane-associated, metabolic, and proteostasis-related parts of the network. Its established functions include calcium-dependent phospholipid binding, membrane-related trafficking, signal transduction, inhibition of phospholipase A2 and protein kinase C, and negative regulation of coagulation and apoptosis. It has extensive literature and disease associations including reproductive and nervous-system disorders. Its lack of heart IHC detection in the supplied HPA summary cautions against assuming that its module signal represents abundant heart-muscle protein.
- **Conclusion**: Established evidence supports ANXA5 as a membrane and calcium-responsive regulator with coagulation and apoptotic relevance. Its role as a functional bridge between membrane state, metabolism, and proteostasis in this module remains speculative.

## Module 5

**Tissue pair**: autonomic_nervous_system and heart  
**Genes (7)**: BPNT1, HSP90AA1, DDOST, RAB18, SEC22B, SEPTIN9, QARS1

### Function

The module is most consistent with a cellular proteostasis and membrane-trafficking program, linking endoplasmic-reticulum protein processing, vesicle transport, cytoskeletal organization, translation, and intracellular signaling. HSP90AA1 connects to QARS1, SEPTIN9, and DDOST, while DDOST connects to BPNT1 and RAB18; SEPTIN9 also connects to SEC22B. These links suggest coordinated activity across protein folding, N-linked glycosylation, ER-to-Golgi trafficking, membrane organization, and cytosolic structural processes. However, no GO/KEGG term passed global correction, there are no supplementary STRING enrichment terms, and therefore the module function is an interpretation of the gene annotations and co-abundance structure rather than a statistically validated pathway assignment. The module should not be described as a canonical protein complex or a formally enriched pathway.

**Cell composition.** The module is not dominated by secreted proteins, plasma proteins, or blood-cell-enriched genes. HPA reports low tissue specificity and low immune-cell specificity for every member, with no secreted genes. The cell-type-enhanced annotations are dispersed across several epithelial, trophoblast, reproductive, and neutrophil categories rather than concentrated in a shared autonomic or cardiac cell type. Heart protein detection is mixed among the genes, whereas the autonomic-nervous-system comparison has no matching HPA tissue. This pattern is more compatible with broadly expressed intracellular proteins, shared cellular machinery, or sample-composition effects than with a blood-derived module. The scattered cell-type enhancements also caution against interpreting the module as specific to neurons or cardiomyocytes.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The fact sheet reports no high-confidence STRING interaction among the module pairs and no hu.MAP complex containing multiple module members. Thus, the co-abundance relationships are not supported here as previously established physical interactions or as membership in a known multiprotein complex. This does not disprove functional coordination: HSP90AA1 is a molecular chaperone, DDOST is an oligosaccharyltransferase component, SEC22B supports ER-Golgi vesicle trafficking, RAB18 regulates organelle and vesicle transport, SEPTIN9 organizes cytoskeletal structures, QARS1 supports translation, and BPNT1 participates in nucleotide and phosphoinositide-related metabolism. The lack of STRING and hu.MAP support means that the module is better regarded as a cross-process co-abundance pattern than as a known physical assembly.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

A shared co-abundance module spanning autonomic nervous system and heart may represent a potentially novel systems-level observation, particularly because the genes do not form a recognized high-confidence STRING neighborhood or hu.MAP complex. Nevertheless, absence from those resources alone cannot establish novelty, and the individual genes and their functions are well established to varying degrees. The strongest defensible conclusion is that the specific tissue-pair co-abundance organization appears under-characterized in the supplied evidence, while its component biology is not itself new. Independent replication, comparison with published tissue co-expression modules, and testing in additional cohorts would be needed before calling it a new biological mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated maintenance of intracellular protein quality and membrane traffic in cells shared between the sampled autonomic nervous system and heart material. HSP90AA1 may buffer folding stress; DDOST may support glycoprotein maturation in the ER; SEC22B and RAB18 may coordinate ER, Golgi, and organelle trafficking; SEPTIN9 may couple trafficking to cytoskeletal organization; QARS1 may sustain translation; and BPNT1 may connect the program to nucleotide or phosphoinositide metabolism. The observed co-abundance could therefore arise from a common demand for proteostasis and membrane transport rather than from direct binding among the proteins. This remains a hypothesis because there is no globally significant GO/KEGG enrichment, STRING enrichment, or hu.MAP complex evidence.

### Important genes

#### HSP90AA1

- **Related proteins** (co-abundance neighbors): QARS1 (0.92), SEPTIN9 (0.86), DDOST (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein 90 alpha family class A member 1. The protein encoded by this gene is an inducible molecular chaperone that functions as a homodimer. The encoded protein aids in the proper folding of specific target proteins by use of an ATPase activity that is modulated by co-chaperones. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: cancer (0.643); plasma cell myeloma (0.404); non-small cell lung carcinoma (0.394); dengue disease (0.375); Orthomyxoviridae infectious disease (0.375)
- **Europe PMC papers**: 8215
- **Why important**: HSP90AA1 has the most central network position in the supplied graph and connects the translation-related QARS1 branch, the cytoskeletal SEPTIN9 branch, and the ER-associated DDOST branch. Its established function as an inducible ATP-dependent molecular chaperone provides a plausible proteostasis anchor for the module. It also has substantial literature coverage and disease associations spanning cancer, plasma cell myeloma, lung carcinoma, and infectious disease, making it the best-supported integrative marker of the module.
- **Conclusion**: Established evidence supports HSP90AA1 as a broadly expressed chaperone with strong relevance to protein folding and stress responses. It is reasonable to treat it as a central hub of the observed co-abundance pattern. It is not established that HSP90AA1 drives the tissue-pair module or directly binds the other members in this module.

#### DDOST

- **Related proteins** (co-abundance neighbors): BPNT1 (0.85), RAB18 (0.82), HSP90AA1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dolichyl-diphosphooligosaccharide--protein glycosyltransferase non-catalytic subunit. This gene encodes a component of the oligosaccharyltransferase complex which catalyzes the transfer of high-mannose oligosaccharides to asparagine residues on nascent polypeptides in the lumen of the rough endoplasmic reticulum. The protein complex co-purifies with ribosomes. The product of this gene is also implicated in the processing of advanced glycation endproducts (AGEs), which form from non…
- **Diseases (Open Targets)**: DDOST-congenital disorder of glycosylation (0.734); young-onset Parkinson disease (0.561); neurodegenerative disease (0.539); dengue disease (0.505); congenital disorder of glycosylation (0.373)
- **Europe PMC papers**: 685
- **Why important**: DDOST is among the most connected genes and links HSP90AA1 to BPNT1 and RAB18, thereby joining the putative proteostasis, metabolic, and membrane-trafficking neighborhoods. Its established role as a non-catalytic component of the oligosaccharyltransferase complex places ER protein glycosylation at the center of a plausible secretory-pathway interpretation. It also has a disease association with congenital disorders of glycosylation and neurodegenerative disease.
- **Conclusion**: Established evidence supports DDOST as an ER oligosaccharyltransferase component involved in glycoprotein biosynthesis and protein stability. Its position makes ER protein maturation a plausible component of the module. A tissue-pair-specific role or causal coordination with RAB18 and BPNT1 remains hypothetical.

#### SEC22B

- **Related proteins** (co-abundance neighbors): SEPTIN9 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC22 homolog B, vesicle trafficking protein. The protein encoded by this gene is a member of the SEC22 family of vesicle trafficking proteins. It seems to complex with SNARE and it is thought to play a role in the ER-Golgi protein trafficking. This protein has strong similarity to Mus musculus and Cricetulus griseus proteins.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: inflammatory bowel disease (0.285); luminal A breast carcinoma (0.271); colitis (0.238); enteritis (0.238); Crohn disease (0.233)
- **Europe PMC papers**: 1006
- **Why important**: SEC22B is the module member that most directly represents vesicle trafficking and ER-Golgi transport. It connects to SEPTIN9, providing a route between membrane trafficking and cytoskeletal organization. Its annotations include vesicle fusion, retrograde transport, starvation response, and macroautophagy, while its disease associations include inflammatory bowel disease and related intestinal disorders.
- **Conclusion**: Established evidence supports SEC22B as a vesicle-trafficking protein involved in ER-Golgi transport and membrane fusion. Its placement supports a trafficking component in the module. A direct functional partnership with SEPTIN9 in autonomic nervous system or heart tissue is not established by the supplied interaction resources.

#### RAB18

- **Related proteins** (co-abundance neighbors): DDOST (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB18, member RAS oncogene family. The protein encoded by this gene is a member of a family of Ras-related small GTPases that regulate membrane trafficking in organelles and transport vesicles. Knockdown studies is zebrafish suggest that this protein may have a role in eye and brain development. Mutations in this gene are associated with Warburg micro syndrome type 3. Alternatively spliced transcript variants have been found for th…
- **Diseases (Open Targets)**: Warburg micro syndrome (0.815); neurodegenerative disease (0.496); cerebral atherosclerosis (0.275); malunion fracture (0.239); adolescent idiopathic scoliosis (0.229)
- **Europe PMC papers**: 2168
- **Why important**: RAB18 links directly to DDOST and represents small-GTPase control of intracellular transport, organelle dynamics, lipid-droplet organization, and sterol homeostasis. Its disease association with Warburg micro syndrome and neurodegenerative disease gives it particular relevance to nervous-system biology, while its network placement connects this biology to the ER-centered portion of the module.
- **Conclusion**: Established evidence supports RAB18 as a membrane-trafficking regulator with roles in intracellular transport and developmental biology. It is a strong candidate for the module's organelle- and vesicle-trafficking component. The idea that its co-abundance with DDOST marks a shared stress or secretory program in heart and autonomic tissue remains a hypothesis.

#### SEPTIN9

- **Related proteins** (co-abundance neighbors): HSP90AA1 (0.86), SEC22B (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: septin 9. This gene is a member of the septin family involved in cytokinesis and cell cycle control. This gene is a candidate for the ovarian tumor suppressor gene. Mutations in this gene cause hereditary neuralgic amyotrophy, also known as neuritis with brachial predilection. A chromosomal translocation involving this gene on chromosome 17 and the MLL gene on chromosome 11 results in acute myelomonocytic l…
- **Diseases (Open Targets)**: neuralgic amyotrophy (0.564); hypertensive disorder (0.496); cataract (0.437); essential hypertension (0.426); alcohol drinking (0.420)
- **Europe PMC papers**: 748
- **Why important**: SEPTIN9 bridges HSP90AA1 and SEC22B and is the clearest cytoskeletal element in the network. Its established functions include cytoskeleton organization, intracellular protein localization, cytokinesis, and cilium assembly. Its associations with hereditary neuralgic amyotrophy, hypertension-related traits, cataract, and acute myelomonocytic leukemia broaden its relevance to neural, vascular, and disease biology.
- **Conclusion**: Established evidence supports SEPTIN9 as a cytoskeletal and cell-organization protein. Its bridging position supports a possible interface between cytoskeletal architecture and vesicle transport. It is not established that SEPTIN9 physically links the chaperone and trafficking processes in this module or that it explains the tissue-pair sharing.

## Module 6

**Tissue pair**: autonomic_nervous_system and heart  
**Genes (7)**: CLTC, TSFM, HNRNPK, HK1, RO60, CCT7, MPST

### Function

The module is most consistent with a broadly expressed cellular-maintenance program spanning intracellular trafficking, glucose utilization, protein folding, RNA processing, sulfur metabolism, and mitochondrial translation. The strongest network organization is a central cluster around CLTC, HK1, and CCT7, with HNRNPK and MPST forming a smaller RNA-processing and sulfur-metabolism connection, and TSFM linking mitochondrial translation to the central cluster. These annotations suggest coordinated demands for energy production, proteostasis, macromolecular trafficking, and gene-expression maintenance rather than a narrowly specialized pathway. However, no GO or KEGG term passed global correction, and STRING functional enrichment was absent, so this functional interpretation is integrative and hypothesis-generating rather than evidence of a formally enriched pathway.

**Cell composition.** The module is not composed of secreted proteins and does not show blood-cell enrichment in the HPA summary. Most genes have low tissue specificity, consistent with a broadly expressed or housekeeping-like component that could reflect shared cellular state rather than a tissue-exclusive biological program. HPA reports cell-type enhancement for most genes, but the most frequent annotations involve early or late spermatids, which are not a direct explanation for the autonomic-nervous-system and heart comparison. TSFM has cardiomyocyte and epicardial-cell enhancement, while CLTC has neutrophil enhancement and MPST is liver-enhanced; these isolated annotations should not be overinterpreted as evidence for blood contamination or a single dominant cell type. Protein detection in heart supports presence of much of the module in heart, whereas the autonomic-nervous-system tissue comparison lacks matching HPA protein data.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair in the module met the supplied STRING interaction threshold, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance relationships are not supported here as established high-confidence physical interactions or as a known protein complex. The module may instead reflect coordinated expression across separate compartments: CLTC in endosomal and lysosomal trafficking, HK1 and MPST in mitochondrial-associated metabolism, CCT7 in cytosolic protein folding, HNRNPK in the nucleus, TSFM in mitochondrial translation, and RO60 in cytosolic or ciliary ribonucleoprotein biology. These established individual functions support biological coherence at the level of cellular state, but they do not establish direct binding among the module members.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact shared co-abundance module appears potentially novel as a cross-tissue grouping because it lacks high-confidence STRING pairwise support, lacks a multi-member hu.MAP complex, and has no globally significant GO or KEGG term. Nevertheless, this does not prove discovery of a new molecular pathway: the genes themselves and their individual functions are well established, and co-abundance can arise from shared regulation, cell composition, mitochondrial content, or general cellular stress. The defensible conclusion is that the module is a new or under-characterized co-abundance pattern, not a newly discovered protein complex or biochemical pathway.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular-capacity program that couples mitochondrial energy and translation requirements with cytosolic proteostasis, RNA handling, and vesicular trafficking. In heart, energetic and mitochondrial demands could coordinate HK1, TSFM, and CCT7 with the trafficking role of CLTC. HNRNPK, MPST, and RO60 may represent linked RNA-processing and redox or sulfur-response components. The association may be mediated by common transcriptional or cell-state regulation rather than direct protein-protein interaction. This hypothesis should be tested with replication across cohorts, adjustment for cell composition, perturbation or stress experiments, and independent measurements of mitochondrial function, glucose handling, protein folding, and RNA regulation.

### Important genes

#### CLTC

- **Related proteins** (co-abundance neighbors): HNRNPK (0.88), CCT7 (0.83), HK1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: clathrin heavy chain. Clathrin is a major protein component of the cytoplasmic face of intracellular organelles, called coated vesicles and coated pits. These specialized organelles are involved in the intracellular trafficking of receptors and endocytosis of a variety of macromolecules.  The basic subunit of the clathrin coat is composed of three heavy chains and three light chains. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: intellectual disability, autosomal dominant 56 (0.787); cancer (0.576); hereditary disease (0.540); Alzheimer disease (0.466); neurodegenerative disease (0.465)
- **Europe PMC papers**: 2902
- **Why important**: CLTC has the strongest network connectivity in the module and links the central cluster to HNRNPK, CCT7, and HK1. Its established role as clathrin heavy chain places it in receptor-mediated endocytosis and intracellular protein trafficking, processes relevant to membrane turnover and cellular communication. It is detected in heart and has extensive disease and literature annotation, including neurodevelopmental, cancer, Alzheimer disease, and neurodegenerative associations.
- **Conclusion**: Established evidence supports CLTC as the principal trafficking-related anchor of the module and as a broadly expressed cellular-maintenance gene. The hypothesis that its co-abundance with metabolic and chaperone genes reflects coordinated membrane and proteostasis demand in heart is plausible but not demonstrated by the supplied data.

#### HK1

- **Related proteins** (co-abundance neighbors): TSFM (0.86), CCT7 (0.85), CLTC (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hexokinase 1. Hexokinases phosphorylate glucose to produce glucose-6-phosphate, the first step in most glucose metabolism pathways. This gene encodes a ubiquitous form of hexokinase which localizes to the outer membrane of mitochondria. Mutations in this gene have been associated with hemolytic anemia due to hexokinase deficiency. Alternative splicing of this gene results in several transcript variants which en…
- **Diseases (Open Targets)**: neurodevelopmental disorder with visual defects and brain anomalies (0.757); non-spherocytic hemolytic anemia due to hexokinase deficiency (0.751); Charcot-Marie-Tooth disease type 4G (0.711); retinitis pigmentosa 79 (0.596); retinitis pigmentosa (0.496)
- **Europe PMC papers**: 51843
- **Why important**: HK1 is among the most connected genes and links CLTC and CCT7 with TSFM. It catalyzes the first step of glucose metabolism and is associated with the mitochondrial outer membrane, giving it a direct connection to energy supply. Its extensive literature and disease record includes hexokinase deficiency with hemolytic anemia, neurodevelopmental disease, Charcot-Marie-Tooth disease, and retinal disorders. It is detected in heart.
- **Conclusion**: Established evidence supports HK1 as the module's clearest metabolic component and a plausible contributor to energetic coordination in heart. The proposed coupling of HK1 abundance to mitochondrial translation and protein-folding capacity remains a hypothesis because the module has no globally enriched metabolic term globally significant GO/KEGG and no STRING support.

#### CCT7

- **Related proteins** (co-abundance neighbors): HK1 (0.85), TSFM (0.84), CLTC (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is highly connected to HK1, TSFM, and CLTC and encodes a subunit of the CCT or TRiC chaperonin complex. Its established function in ATP-dependent folding of proteins including actin and tubulin makes it relevant to cytoskeletal integrity, protein quality control, and cellular resilience. It is detected in heart and has disease links including myocardial infarction and neurodegenerative disease, with a substantial research literature.
- **Conclusion**: Established evidence supports CCT7 as the principal proteostasis-related member and a central connector between metabolic, mitochondrial, and trafficking signals. It may help explain why the module is shared across tissues as a general cellular-capacity program, but direct functional cooperation with the other module genes is not established.

#### TSFM

- **Related proteins** (co-abundance neighbors): HK1 (0.86), CCT7 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Ts translation elongation factor, mitochondrial. This gene encodes a mitochondrial translation elongation factor. The encoded protein is an enzyme that catalyzes the exchange of guanine nucleotides on the translation elongation factor Tu during the elongation step of mitchondrial protein translation. Mutations in this gene are associated with combined oxidative phosphorylation deficiency-3 syndrome. Alternate splicing results in multiple transcr…
- **Diseases (Open Targets)**: fatal mitochondrial disease due to combined oxidative phosphorylation defect type 3 (0.795); steroid-resistant nephrotic syndrome (0.474); hereditary disease (0.414); mitochondrial disease (0.372); neurodegenerative disease (0.370)
- **Europe PMC papers**: 484
- **Why important**: TSFM connects the central HK1 and CCT7 cluster and encodes a mitochondrial translation elongation factor. Its role in mitochondrial protein synthesis directly relates to production of respiratory-chain components and energetic capacity. It has a strong association with combined oxidative-phosphorylation deficiency and broader mitochondrial disease, and HPA reports cell-type enhancement in cardiomyocytes and epicardial cells.
- **Conclusion**: Established evidence supports TSFM as the most tissue-relevant mitochondrial translation component for interpreting the heart-shared module. Its co-abundance with HK1 and CCT7 supports a hypothesis of coordinated mitochondrial energy, translation, and proteostasis capacity, but the data do not establish causal regulation or a direct complex.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): CLTC (0.88), MPST (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK connects CLTC to MPST and represents the module's strongest explicit RNA-processing and transcriptional-regulation component. It is a broadly expressed RNA-binding protein involved in pre-mRNA processing, RNA transport, and regulation of transcription. Its disease associations include Au-Kline syndrome, craniofacial and cardiac developmental disease, and neurodevelopmental and neurodegenerative conditions. It is detected in heart.
- **Conclusion**: Established evidence supports HNRNPK as a plausible regulatory bridge linking cellular trafficking to RNA metabolism. A hypothesis that HNRNPK-mediated gene-expression control helps coordinate the module across autonomic nervous system and heart is reasonable, but no enrichment or physical-interaction evidence demonstrates that mechanism.

## Module 7

**Tissue pair**: autonomic_nervous_system and heart  
**Genes (6)**: EZR, FKBP3, MATR3, SEPTIN7, DARS1, CCT3

### Function

No GO or KEGG term passed global multiple-testing correction, and STRING functional enrichment was absent. Therefore, the module does not support a narrowly defined pathway-level function from enrichment alone. Its gene composition and network topology instead suggest a broadly expressed intracellular module linking RNA and protein regulation with cytoskeletal and membrane organization. MATR3 provides a nuclear and post-transcriptional regulatory component; DARS1 represents core translation-related activity; CCT3 represents ATP-dependent folding of actin, tubulin, and other proteins; SEPTIN7 and EZR connect cytoskeletal organization with cell shape and membrane architecture; and FKBP3 contributes protein-folding, trafficking, and regulatory interactions. The shared co-abundance pattern is therefore most consistent with a general cellular-architecture and proteostasis program rather than a specialized autonomic or cardiac pathway. This interpretation is a synthesis of annotations and network structure, not a globally significant enrichment result.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of the genes is annotated as secreted. All genes have low immune-cell specificity, with no enriched blood-cell category, arguing against a simple blood-cell or plasma contamination explanation. Most genes also have low tissue specificity, consistent with broadly expressed housekeeping-like intracellular proteins. There is nevertheless cell-type heterogeneity: SEPTIN7, FKBP3, and EZR have cell-type-enhanced annotations spanning neural, epithelial, reproductive, and other specialized cell types, while FKBP3 is tissue-enhanced in skeletal muscle and tongue. Heart protein detection is present for MATR3, CCT3, and FKBP3 but absent for SEPTIN7, DARS1, and EZR; there is no matching HPA tissue result for autonomic nervous system. Thus, the shared module may reflect common intracellular machinery across sampled cells, with possible contributions from muscle or epithelial cell composition, but the evidence does not establish a single source cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and no hu.MAP complex contains multiple module members. Consequently, the co-abundance edges are not simply recapitulating a documented physical interaction network in these resources. The absence of STRING and hu.MAP support weakens a claim that the entire module is a known molecular complex, but it does not invalidate coordinated expression or exclude interactions below the selected database confidence thresholds. The biological annotations still provide a plausible chain from MATR3 through SEPTIN7 and DARS1 to CCT3 and EZR, with FKBP3 connected to MATR3; this should be treated as a co-abundance relationship rather than demonstrated physical binding.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module appears potentially novel as a cross-tissue co-abundance configuration because its member combination is not represented by reported high-confidence STRING interactions or a shared hu.MAP complex. However, that observation alone cannot establish discovery of a new biological pathway: the genes themselves are well studied, several have established cellular functions, and the module may reflect broadly expressed cellular machinery or sample composition. The strongest defensible claim is that this particular coordinated pattern across autonomic nervous system and heart is a candidate novel network-level observation requiring replication, preservation testing, cell-composition analysis, and independent protein or transcriptomic validation.

**Hypothesis.** Hypothesis: the module reflects coordinated maintenance of intracellular proteostasis and cell architecture in autonomic nervous system and heart samples. In this model, CCT3 supports folding of cytoskeletal proteins, DARS1 supports translation capacity, FKBP3 contributes regulatory folding and trafficking functions, SEPTIN7 organizes cytoskeletal structures, EZR couples the plasma membrane to actin, and MATR3 links nuclear RNA regulation to cellular stress or structural-state programs. Their coordinated abundance could arise when cells adjust translation, protein quality control, and cytoskeletal or membrane organization together. This remains a mechanistic hypothesis, not a demonstrated pathway or physical complex.

### Important genes

#### MATR3

- **Related proteins** (co-abundance neighbors): FKBP3 (0.90), SEPTIN7 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: matrin 3. This gene encodes a nuclear matrix protein, which is proposed to stabilize certain messenger RNA species. Mutations of this gene are associated with distal myopathy 2, which often includes vocal cord and pharyngeal weakness. Alternatively spliced transcript variants, including read-through transcripts composed of the upstream small nucleolar RNA host gene 4 (non-protein coding) and matrin 3 gene s…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.735); distal myopathy with vocal cord weakness (0.569); neurodegenerative disease (0.529); distal myopathy (0.384); hereditary disease (0.193)
- **Europe PMC papers**: 1756
- **Why important**: MATR3 is a topological bridge in the module, connecting FKBP3 with SEPTIN7. It is a nuclear matrix protein implicated in messenger RNA stabilization and post-transcriptional regulation, and its annotations include heart developmental processes and innate immune response. It has extensive literature and disease associations including distal myopathy with vocal-cord weakness and amyotrophic lateral sclerosis, making it especially relevant to a module shared by neural-autonomic and cardiac contexts.
- **Conclusion**: Established evidence supports MATR3 as a nuclear RNA-regulatory protein with clinically relevant neuromuscular associations and a central position in this small co-abundance structure. It is plausible that MATR3 links cellular-state regulation to the structural and proteostasis components, but the module does not establish that MATR3 causally organizes the other genes.

#### CCT3

- **Related proteins** (co-abundance neighbors): EZR (0.84), DARS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a topological bridge between DARS1 and EZR and is a subunit of the CCT chaperonin complex. Its established function in ATP-dependent folding of actin, tubulin, and other proteins provides a direct mechanistic connection between translation-related activity and cytoskeletal organization. It has substantial literature and disease associations involving neurodevelopmental and neurodegenerative phenotypes as well as atrial fibrillation.
- **Conclusion**: Established evidence supports CCT3 as a proteostasis factor capable of influencing cytoskeletal protein availability. Its network position makes it a strong candidate bridge in the proposed module function, but the co-abundance data do not prove that CCT3 drives the observed pattern or that the complete CCT complex is co-regulated here.

#### EZR

- **Related proteins** (co-abundance neighbors): CCT3 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ezrin. The cytoplasmic peripheral membrane protein encoded by this gene functions as a protein-tyrosine kinase substrate in microvilli. As a member of the ERM protein family, this protein serves as an intermediate between the plasma membrane and the actin cytoskeleton. This protein plays a key role in cell surface structure adhesion, migration and organization, and it has been implicated in various human…
- **Diseases (Open Targets)**: hair color (0.477); non-small cell lung carcinoma (0.397); lung adenocarcinoma (0.382); autosomal recessive non-syndromic intellectual disability (0.370); glaucoma (0.347)
- **Europe PMC papers**: 4982
- **Why important**: EZR connects CCT3 to the plasma-membrane and actin-cytoskeleton interface. Its established roles include cell-surface structure, adhesion, migration, cell shape, and membrane organization. It has the largest literature volume among the module genes and disease associations that include cancer, glaucoma, and intellectual disability. Its cell-type-enhanced annotations in several epithelial populations also make it informative for evaluating cellular composition.
- **Conclusion**: Established evidence supports EZR as a membrane–cytoskeleton organizer and a plausible readout of cell shape or epithelial-like cellular states. Its presence does not demonstrate that the module is epithelial or that EZR physically interacts with CCT3 in this dataset; those are hypotheses requiring cell-resolved validation.

#### SEPTIN7

- **Related proteins** (co-abundance neighbors): DARS1 (0.86), MATR3 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: septin 7. This gene encodes a protein that is highly similar to the CDC10 protein of Saccharomyces cerevisiae. The protein also shares similarity with Diff 6 of Drosophila and with H5 of mouse. Each of these similar proteins, including the yeast CDC10, contains a GTP-binding motif. The yeast CDC10 protein is a structural component of the 10 nm filament which lies inside the cytoplasmic membrane and is essen…
- **Diseases (Open Targets)**: glaucoma (0.366); bone fracture (0.264); fracture of pelvis (0.264); open-angle glaucoma (0.262); male reproductive system disorder (0.260)
- **Europe PMC papers**: 304
- **Why important**: SEPTIN7 occupies an internal position between MATR3 and DARS1 and is a GTP-binding septin associated with cytoskeleton organization, cytokinesis, cell shape, and cilium assembly. Its annotations include oligodendrocyte and retinal horizontal-cell enhancement, while its disease associations include glaucoma. It therefore links the module to structural remodeling and potentially neural-relevant cellular organization.
- **Conclusion**: Established evidence supports SEPTIN7 as a cytoskeletal and cell-organization factor. Its position is consistent with a structural bridge in the co-abundance pattern, but the network does not establish direct binding to MATR3 or DARS1, nor does it identify a specific ciliary or neural mechanism.

#### DARS1

- **Related proteins** (co-abundance neighbors): SEPTIN7 (0.86), CCT3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 1. This gene encodes a member of a multienzyme complex that functions in mediating the attachment of amino acids to their cognate tRNAs. The encoded protein ligates L-aspartate to tRNA(Asp). Mutations in this gene have been found in patients showing hypomyelination with brainstem and spinal cord involvement and leg spasticity. Alternative splicing results in multiple transcript variants. [provided by…
- **Diseases (Open Targets)**: hypomyelination with brain stem and spinal cord involvement and leg spasticity (0.773); atrial fibrillation (0.268); Abnormal brain morphology (0.266); tooth hard tissue disease (0.226); Pancreatic pseudocyst (0.225)
- **Europe PMC papers**: 238
- **Why important**: DARS1 is an internal bridge between SEPTIN7 and CCT3 and encodes an aspartyl-tRNA synthetase required for aminoacylation and protein translation. Its established disease association with hypomyelination involving the brainstem and spinal cord, together with an association signal for atrial fibrillation, makes it relevant to a module spanning autonomic and cardiac tissues. Its broadly expressed profile is also compatible with a general translational component.
- **Conclusion**: Established evidence supports DARS1 as a core translation factor with important neurological disease relevance. In this module it may mark coordinated protein-production demand, but there is no evidence that it specifically couples translation to septin or chaperonin activity in these tissues.

## Module 8

**Tissue pair**: autonomic_nervous_system and heart  
**Genes (5)**: IMPDH2, ITGB1, NES, PDCD6IP, SEC23A

### Function

The module does not support a single statistically enriched GO or KEGG function: no GO/KEGG term passed global correction. Its gene-level annotations instead indicate a mixed cellular program involving cell adhesion and membrane signaling through ITGB1, intermediate-filament biology through NES, ER-to-Golgi trafficking through SEC23A, endosomal and cytokinetic membrane remodeling through PDCD6IP, and guanine-nucleotide biosynthesis through IMPDH2. The sparse co-abundance structure therefore appears more consistent with coordinated cellular state or shared cell composition than with a well-defined canonical pathway. The strongest biological interpretation is a relationship among adhesion and cytoskeletal organization, intracellular vesicle handling, and biosynthetic or proliferative capacity, but this remains an integrative interpretation rather than an enrichment result.

**Cell composition.** The module is not dominated by plasma or secreted proteins: HPA describes most members as having low tissue specificity, and the module summary reports only one secreted gene. It is also not blood-cell enriched. Most genes have low immune-cell specificity, while one is not detected in immune cells. Most members nevertheless have cell-type-enhanced annotations, distributed across several epithelial, stromal, vascular-support, platelet, and related cell types rather than a single shared cell type. NES is tissue enhanced in heart muscle and is detected there, while IMPDH2 and SEC23A are also detected in heart tissue. This pattern is compatible with a shared structural or cellular-state signal in the sampled tissues, including possible contributions from non-cardiomyocyte or autonomic-associated cell populations, but the fact sheet does not establish a specific contaminating cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship was reported among the module members, and no STRING functional-enrichment result was reported. No hu.MAP complex contained multiple module members. The co-abundance edges are therefore not supported here as previously documented physical interactions or membership in a known multiprotein complex. Known biology still exists at the individual-gene level: ITGB1 is an integrin beta subunit involved in adhesion and recognition; SEC23A is a COPII component; PDCD6IP participates in ESCRT-associated membrane remodeling and cytokinesis; IMPDH2 catalyzes a rate-limiting step in de novo guanine-nucleotide production; and NES is an intermediate-filament protein. Thus, the network may capture coordinated expression without implying direct binding between its members.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module is potentially novel as a cross-tissue co-abundance pattern, because its member set has no reported high-confidence STRING interactions and no shared hu.MAP complex. Those absences do not by themselves prove biological novelty: the genes are individually well characterized, and several have substantial disease and literature associations. The lack of globally significant GO/KEGG enrichment also means that the module is not independently supported as a newly defined pathway. A defensible conclusion is that the specific co-abundance organization may be a new observation, whereas the component gene functions are established and the module-level mechanism remains unvalidated.

**Hypothesis.** Hypothesis: the shared module reflects a coordinated cellular state in which adhesion and cytoskeletal organization, membrane trafficking, and nucleotide supply vary together across autonomic-nervous-system and heart samples. ITGB1 and NES could mark adhesion or structural remodeling, SEC23A and PDCD6IP could represent secretory and endosomal membrane-handling capacity, and IMPDH2 could support the nucleotide demand associated with biosynthesis or cell-cycle activity. An alternative hypothesis is that the signal arises from changing proportions of specialized cell populations, because HPA reports cell-type-enhanced annotations across several distinct cell types and only limited tissue specificity. This hypothesis requires validation with cell-resolved expression, independent cohorts, perturbation experiments, and direct protein-interaction or localization assays.

### Important genes

#### ITGB1

- **Related proteins** (co-abundance neighbors): PDCD6IP (0.90), NES (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is a central connector in the module, linked by co-abundance to PDCD6IP and NES. Its established function as an integrin beta subunit places it at the interface of cell adhesion, recognition, tissue repair, hemostasis, immune response, and metastatic dissemination. HPA places it at the plasma membrane and focal-adhesion sites and reports cell-type-enhanced expression in platelet-related and epithelial contexts. It has extensive literature coverage and Open Targets associations including Crohn disease, viral infectious disease, inflammation, anisometropia, and type one diabetes.
- **Conclusion**: Established: ITGB1 is a biologically plausible structural and adhesion anchor and is the most connected module member. Hypothesis: its co-abundance with NES and PDCD6IP may indicate coordinated adhesion-linked membrane remodeling in the shared tissue state. The network does not establish direct physical interaction or causality.

#### NES

- **Related proteins** (co-abundance neighbors): ITGB1 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nestin. This gene encodes a member of the intermediate filament protein family and is expressed primarily in nerve cells. [provided by RefSeq, Sep 2011].
- **Diseases (Open Targets)**: placental abruption (0.267); glioblastoma (0.119); central nervous system cancer (0.119); neoplasm (0.119); congenital fibrosis of the extraocular muscles (0.118)
- **Europe PMC papers**: 53286
- **Why important**: NES is connected to ITGB1 and is the module member with tissue-enhanced annotation in heart muscle. Its established role is as an intermediate-filament protein expressed primarily in nerve cells, with functions related to nervous-system development and intermediate-filament regulation. It is detected in heart tissue and has cell-type-enhanced annotations in stromal, vascular-support, podocyte, and epithelial-related populations. It has very extensive literature coverage and disease associations including placental abruption, glioblastoma, central nervous system cancer, neoplasm, and congenital fibrosis of the extraocular muscles.
- **Conclusion**: Established: NES provides the clearest tissue-contextual link to heart and a plausible cytoskeletal component. Hypothesis: coordinated NES and ITGB1 expression may reflect remodeling or representation of structural support cells rather than cardiomyocyte-specific biology. The fact sheet does not demonstrate that NES drives the module.

#### SEC23A

- **Related proteins** (co-abundance neighbors): IMPDH2 (0.91); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A connects to IMPDH2 and is the module member most directly annotated to ER-to-Golgi transport and COPII vesicle formation. Its established function places it in ER export, vesicle budding, cargo loading, and intracellular protein transport. It is detected in heart tissue and has low tissue and cell-type specificity, making it a plausible broadly required trafficking component rather than a specialized marker. Its disease associations include craniolenticulosutural dysplasia, vitamin D deficiency, alcohol drinking, male reproductive organ cancer, and metabolic syndrome X.
- **Conclusion**: Established: SEC23A is the strongest trafficking-related component and may report general secretory-pathway capacity. Hypothesis: its co-abundance with IMPDH2 could reflect coordinated biosynthetic demand and protein export. No direct SEC23A interaction with another module member was reported by STRING or hu.MAP.

#### PDCD6IP

- **Related proteins** (co-abundance neighbors): ITGB1 (0.90), IMPDH2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 6 interacting protein. This gene encodes a protein that functions within the ESCRT pathway in the abscission stage of cytokinesis, in intralumenal endosomal vesicle formation, and in enveloped virus budding. Studies using mouse cells have shown that overexpression of this protein can block apoptosis. In addition, the product of this gene binds to the product of the PDCD6 gene, a protein required for apoptosis, in a calc…
- **Diseases (Open Targets)**: HIV infectious disease (0.463); anthrax infection (0.462); alcohol drinking (0.388); autosomal recessive primary microcephaly (0.386); microcephaly 29, primary, autosomal recessive (0.383)
- **Europe PMC papers**: 1668
- **Why important**: PDCD6IP is a connector between ITGB1 and IMPDH2 in the co-abundance graph. Its established functions include ESCRT-pathway activity during cytokinetic abscission, intralumenal endosomal-vesicle formation, enveloped-virus budding, interaction with PDCD6, and links to apoptosis-related processes. HPA places it in vesicles and describes its protein as intracellular and membrane-associated, with low tissue and immune-cell specificity. Its disease associations include HIV infectious disease, anthrax infection, alcohol drinking, and autosomal-recessive primary microcephaly, and it has a substantial literature base.
- **Conclusion**: Established: PDCD6IP is a plausible membrane-remodeling and vesicle-associated component. Hypothesis: its position between adhesion-related and nucleotide-related genes may indicate a broader cellular remodeling state involving membrane turnover and cell division. The module does not establish that apoptosis or viral budding is occurring in either tissue.

#### IMPDH2

- **Related proteins** (co-abundance neighbors): SEC23A (0.91), PDCD6IP (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inosine monophosphate dehydrogenase 2. This gene encodes the rate-limiting enzyme in the de novo guanine nucleotide biosynthesis. It is thus involved in maintaining cellular guanine deoxy- and ribonucleotide pools needed for DNA and RNA synthesis. The encoded protein catalyzes the NAD-dependent oxidation of inosine-5'-monophosphate into xanthine-5'-monophosphate, which is then converted into guanosine-5'-monophosphate. This gene is up-…
- **Diseases (Open Targets)**: acute lymphoblastic leukemia (0.529); Crohn disease (0.447); acute myeloid leukemia (0.421); lupus nephritis (0.408); myelodysplastic syndrome (0.403)
- **Europe PMC papers**: 1438
- **Why important**: IMPDH2 is connected to both SEC23A and PDCD6IP and is detected in heart tissue. Its established enzymatic function is the rate-limiting step in de novo guanine-nucleotide biosynthesis, supporting DNA and RNA synthesis through production of guanosine nucleotides. Its cell-type-enhanced HPA annotations include colonocyte and intestinal progenitor-related populations, while its tissue specificity is low. It has disease associations including acute lymphoblastic leukemia, Crohn disease, acute myeloid leukemia, lupus nephritis, and myelodysplastic syndrome, with a substantial literature base.
- **Conclusion**: Established: IMPDH2 provides a metabolic and biosynthetic dimension to an otherwise structural and trafficking-oriented module. Hypothesis: its co-abundance with SEC23A and PDCD6IP may mark increased biosynthetic, proliferative, or repair-associated cellular activity. The module does not prove that proliferation or malignant transformation is present in the tissue samples.
