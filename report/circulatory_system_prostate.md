# Conserved co-abundance modules: circulatory_system and prostate

## Module 0

**Tissue pair**: circulatory_system and prostate  
**Genes (22)**: HIBADH, ACADM, ACOT1, DNAJC10, GLS, HSDL2, IDH3A, EIF4E2, LRRC40, CHCHD3, OCIAD1, PITRM1, MRRF, SGPL1, STT3A, IARS2, WARS2, THEM6, ACAT1, TIMMDC1, TIMM8B, UBA3

### Function

The primary evidence supports a mitochondrial module (GO:CC mitochondrion; q_global = 0.0229). Most of the module genes in (GO:CC mitochondrion; q_global = 0.0229) are mitochondrial, and the supplementary STRING terms independently point to mitochondrial localization, mitochondrial matrix, transit peptides, and mitochondrial protein import (5 supplementary STRING terms; within-query FDR 0.0103–0.0341). The genes span complementary mitochondrial activities: fatty-acid and acetyl-CoA metabolism through ACADM, ACAT1, ACOT1, and HSDL2; amino-acid metabolism through GLS and HIBADH; the tricarboxylic-acid cycle through IDH3A; mitochondrial translation through IARS2, WARS2, and MRRF; inner-membrane import through TIMMDC1 and TIMM8B; cristae organization through CHCHD3; and mitochondrial proteostasis through PITRM1. Thus, the most defensible interpretation is coordinated mitochondrial oxidative metabolism, protein import, translation, and organelle maintenance rather than a narrowly defined single biochemical pathway. DNAJC10, STT3A, SGPL1, and EIF4E2 suggest links to endoplasmic-reticulum proteostasis, glycosylation, sphingolipid metabolism, and translational control, but these are supporting features rather than the primary annotation. The sparse network structure and concentration of connectivity around TIMMDC1 indicate a coordinated organelle program with several biochemical branches, not proof of direct physical interaction among all members.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. HPA marks THEM6 as secreted with unknown location, while the other genes are not reported as secreted; the dominant pattern is intracellular, especially mitochondrial. Most genes have low tissue specificity, with tissue-enhanced genes represented in liver, tongue, skeletal muscle, kidney, and epididymis. Cell-type enhancement is common, including hepatocytes, spermatids, syncytiotrophoblasts, and other specialized cells, which is compatible with differing mitochondrial demands across tissues. Blood-cell specificity is low for nearly the entire module, with IDH3A the notable immune-cell-enhanced exception in plasmacytoid dendritic cells. Therefore, the shared circulatory-system and prostate signal is unlikely to be explained mainly by blood-cell contamination or a circulating secretome; it more plausibly reflects a broadly reused mitochondrial program, tissue composition, or shared metabolically active cell populations. HPA protein detection in prostate is widespread among the annotated genes, whereas circulatory-system protein evidence is unavailable in the supplied summary, so the cross-tissue interpretation should not be treated as direct evidence of circulating protein secretion.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrion | 0.0229 | ACADM, ACAT1, ACOT1, CHCHD3, GLS, HIBADH, HSDL2, IARS2, IDH3A, MRRF, OCIAD1, PITRM1, TIMM8B, TIMMDC1, WARS2 |

### STRING and hu.MAP

STRING provides a limited but coherent set of high-confidence relationships. ACADM connects with ACAT1 and HSDL2, forming a fatty-acid and acyl-CoA metabolic neighborhood; IARS2 connects with WARS2, supporting a mitochondrial translation neighborhood; and OCIAD1 connects with TIMMDC1, supporting an inner-mitochondrial or organelle-organization neighborhood. These known relationships strengthen the interpretation that parts of the co-abundance module correspond to established mitochondrial biology, but they do not establish a single physical complex for the whole module. hu.MAP supplies additional context rather than a complete explanation: STT3A and THEM6 co-occur as module members in two broad complexes (hu.MAP huMAP3_06247.1) and (hu.MAP huMAP3_09592.1), while GLS and IARS2 co-occur in a large mitochondrial-associated complex (hu.MAP huMAP3_13468.1). Because each complex contains many members outside this module and only a small subset of its members is represented here, the hu.MAP results support functional neighborhoods and shared cellular context, not membership of the entire module in one canonical complex. The absence of STRING or hu.MAP support for many module edges is expected for a co-abundance network and should not be interpreted as evidence against coordinated regulation.

**STRING interactions (score >= 0.7)**: 5 of 231 gene pairs: ACADM–ACAT1 (0.717); ACADM–HSDL2 (0.835); ACAT1–HSDL2 (0.909); IARS2–WARS2 (0.877); OCIAD1–TIMMDC1 (0.85)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Mitochondrion (FDR = 0.0103, 13 genes); Keyword Mitochondrion (FDR = 0.0129, 12 genes); Keyword Transit peptide (FDR = 0.0147, 9 genes); Component Mitochondrial matrix (FDR = 0.0293, 9 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.0341, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06247.1 (STT3A, THEM6; 2/65); huMAP3_09592.1 (STT3A, THEM6; 2/95); huMAP3_13468.1 (GLS, IARS2; 2/99)

### Novelty

The module should not be called a newly discovered mitochondrial pathway. Its principal biology is already established by the annotations of ACADM, ACAT1, IDH3A, GLS, IARS2, WARS2, TIMMDC1, CHCHD3, PITRM1, and related genes, and several of its relationships are already represented in STRING or hu.MAP. At the same time, the supplied evidence does not identify an exact previously published co-abundance module shared specifically by circulatory_system and prostate. The potentially novel aspect is therefore the cross-tissue co-abundance configuration and its particular combination of mitochondrial metabolism, import, translation, and organelle-architecture genes, not the underlying functions of the individual genes. Absence from the cited interaction resources is insufficient to establish novelty. A firm novelty claim would require comparison with published tissue coexpression studies, tissue-pair module atlases, and independent datasets, followed by replication of the gene-level pattern.

**Hypothesis.** Hypothesis: the shared module reflects coordinated mitochondrial capacity in metabolically active prostate-associated cells and in the cell populations represented in circulatory-system samples. A central program may couple mitochondrial import and respiratory-complex assembly through TIMMDC1 and TIMM8B with mitochondrial translation through IARS2, WARS2, and MRRF, while ACADM, ACAT1, ACOT1, HSDL2, IDH3A, and GLS supply lipid, acetyl-CoA, amino-acid, and tricarboxylic-acid-cycle metabolism. CHCHD3 may help preserve cristae architecture, and PITRM1 may support mitochondrial protein quality control. The ER-associated genes could indicate coordinated proteostasis or membrane-lipid handling. This remains a hypothesis: the co-abundance data do not demonstrate causal regulation, shared cell identity, direct protein binding, or increased mitochondrial function. It can be tested by replicating the module across independent prostate and circulatory datasets, adjusting for cell composition, measuring mitochondrial transcripts and proteins, and perturbing central genes such as TIMMDC1, ACADM, or IARS2 while assessing respiration, mitochondrial translation, import, and cristae integrity.

### Important genes

#### TIMMDC1

- **Related proteins** (co-abundance neighbors): HSDL2 (0.89), MRRF (0.86), THEM6 (0.86), OCIAD1 (0.84), GLS (0.83), DNAJC10 (0.81), IARS2 (0.81), EIF4E2 (0.80), LRRC40 (0.80); STRING partners: OCIAD1 (0.85)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translocase of inner mitochondrial membrane domain containing 1. Located in mitochondrion and nucleoplasm. Implicated in nuclear type mitochondrial complex I deficiency 31. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 31 (0.665); mitochondrial complex I deficiency (0.626); neurodegenerative disease (0.548); mitochondrial disease (0.371); primary biliary cholangitis (0.350)
- **Europe PMC papers**: 374
- **Why important**: TIMMDC1 is the principal network hub in the supplied module, connecting mitochondrial, metabolic, translation-related, and organelle-associated neighbors. It is included in the primary mitochondrial term (GO:CC mitochondrion; q_global = 0.0229) and the supplementary mitochondrial terms (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0103) and (STRING Keyword Mitochondrion; within-query FDR = 0.0129). Its annotated role in mitochondrial respiratory-chain complex I assembly and its disease associations with mitochondrial complex I deficiency make it a strong mechanistic anchor. It also has the largest literature volume among the module's central structural candidates, supporting comparatively mature biological interpretation.
- **Conclusion**: Established evidence supports TIMMDC1 as a mitochondrial inner-membrane and complex-I-assembly gene that organizes the module's network position. It is reasonable to hypothesize that variation in TIMMDC1-related respiratory assembly contributes to the shared co-abundance pattern, but the module does not establish that TIMMDC1 regulates the other genes.

#### ACADM

- **Related proteins** (co-abundance neighbors): IDH3A (0.80); STRING partners: ACAT1 (0.717), HSDL2 (0.835)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA dehydrogenase medium chain. This gene encodes the medium-chain specific (C4 to C12 straight chain) acyl-Coenzyme A dehydrogenase. The homotetramer enzyme catalyzes the initial step of the mitochondrial fatty acid beta-oxidation pathway. Defects in this gene cause medium-chain acyl-CoA dehydrogenase deficiency, a disease characterized by hepatic dysfunction, fasting hypoglycemia, and encephalopathy, which can result in infant…
- **Diseases (Open Targets)**: medium chain acyl-CoA dehydrogenase deficiency (0.854); hereditary disease (0.516); rhabdomyolysis (0.370); short chain acyl-CoA dehydrogenase deficiency (0.349); Epileptic spasm (0.333)
- **Europe PMC papers**: 4795
- **Why important**: ACADM links the module to the first step of medium-chain fatty-acid beta-oxidation and is part of (GO:CC mitochondrion; q_global = 0.0229) and (5 supplementary STRING terms; within-query FDR 0.0103–0.0341). It is tissue-enhanced in liver, skeletal muscle, and tongue, is detected in prostate, and has a well-established association with medium-chain acyl-CoA dehydrogenase deficiency. Its STRING links to ACAT1 and HSDL2 place it in the clearest established metabolic interaction neighborhood in the module, and its literature base is extensive.
- **Conclusion**: Established evidence identifies ACADM as a mitochondrial fatty-acid oxidation enzyme and a clinically validated metabolic gene. Within this module it is best interpreted as a metabolic effector that may report tissue energy demand; the co-abundance pattern alone does not show altered beta-oxidation flux.

#### ACAT1

- **Related proteins** (co-abundance neighbors): SGPL1 (0.82); STRING partners: ACADM (0.717), HSDL2 (0.909)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA acetyltransferase 1. This gene encodes a mitochondrially localized enzyme that catalyzes the reversible formation of acetoacetyl-CoA from two molecules of acetyl-CoA. Defects in this gene are associated with 3-ketothiolase deficiency, an inborn error of isoleucine catabolism characterized by urinary excretion of 2-methyl-3-hydroxybutyric acid, 2-methylacetoacetic acid, tiglylglycine, and butanone. [provided by RefSeq,…
- **Diseases (Open Targets)**: beta-ketothiolase deficiency (0.817); hereditary disease (0.470); Abnormality of the skeletal system (0.239); neoplasm (0.115); nonpapillary renal cell carcinoma (0.105)
- **Europe PMC papers**: 4147
- **Why important**: ACAT1 is a mitochondrial acetyl-CoA-processing enzyme involved in ketone-related and amino-acid metabolism, fatty-acid beta-oxidation, and CoA metabolism. It is supported by (GO:CC mitochondrion; q_global = 0.0229) and all of the mitochondrial STRING enrichment terms (5 supplementary STRING terms; within-query FDR 0.0103–0.0341). Its high-confidence STRING relationships with ACADM and HSDL2 provide direct support for a lipid and acyl-CoA metabolic subnetwork. Its association with beta-ketothiolase deficiency and its substantial literature volume make it an informative disease-linked representative.
- **Conclusion**: Established evidence supports ACAT1 as a central mitochondrial metabolic enzyme within a known acyl-CoA neighborhood. A plausible hypothesis is that the module coordinates substrate handling with respiratory demand, but no causal metabolic coupling can be inferred from co-abundance alone.

#### IARS2

- **Related proteins** (co-abundance neighbors): IDH3A (0.83), TIMMDC1 (0.81); STRING partners: WARS2 (0.877)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 2, mitochondrial. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Two forms of isoleucine-tRNA synthetase exist, a cytoplasmic form and a mitochondrial form. This gene encodes th…
- **Diseases (Open Targets)**: cataract-growth hormone deficiency-sensory neuropathy-sensorineural hearing loss-skeletal dysplasia syndrome (0.724); Leigh syndrome (0.563); hereditary disease (0.416); neurodegenerative disease (0.411); mitochondrial disease (0.374)
- **Europe PMC papers**: 411
- **Why important**: IARS2 connects mitochondrial translation to the module through mitochondrial isoleucyl-tRNA aminoacylation and translational fidelity. It is present in (GO:CC mitochondrion; q_global = 0.0229) and (5 supplementary STRING terms; within-query FDR 0.0103–0.0341), connects in STRING to WARS2, and appears with GLS in the hu.MAP complex (hu.MAP huMAP3_13468.1). Its disease associations include a mitochondrial neurodevelopmental syndrome and Leigh syndrome, making it a functionally consequential translation component.
- **Conclusion**: Established evidence supports IARS2 as a mitochondrial translation and protein-synthesis gene, and its relationships with WARS2 and the (hu.MAP huMAP3_13468.1) neighborhood reinforce that interpretation. The module may couple mitochondrial translation with respiratory metabolism, but the data do not show that defective IARS2 is responsible for the tissue-pair association.

#### CHCHD3

- **Related proteins** (co-abundance neighbors): OCIAD1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coiled-coil-helix-coiled-coil-helix domain containing 3. The protein encoded by this gene is an inner mitochondrial membrane scaffold protein. Absence of the encoded protein affects the structural integrity of mitochondrial cristae and leads to reductions in ATP production, cell growth, and oxygen consumption. This protein is part of the mitochondrial contact site and cristae organizing system (MICOS). Several transcript variants encoding different isof…
- **Diseases (Open Targets)**: neurodegenerative disease (0.537); smoking initiation (0.414); intelligence (0.385); insomnia (0.362); mathematical ability (0.312)
- **Europe PMC papers**: 549
- **Why important**: CHCHD3 represents mitochondrial architecture rather than metabolism alone. It is included in (GO:CC mitochondrion; q_global = 0.0229), appears in the supplementary mitochondrial terms (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0103) and (STRING Keyword Mitochondrion; within-query FDR = 0.0129), connects to OCIAD1 in the module, and is annotated as a MICOS-related inner-membrane scaffold involved in cristae formation, mitochondrial fusion, and inner-membrane organization. Its tissue enhancement in skeletal muscle and tongue and its disease associations with neurodegenerative disease provide relevant context for a module shared across metabolically demanding tissues.
- **Conclusion**: Established evidence supports CHCHD3 as a structural mitochondrial organizer that could connect cristae architecture with respiratory performance. It is a useful structural marker of the module, while any role in driving the shared tissue pattern remains hypothetical.

#### GLS

- **Related proteins** (co-abundance neighbors): TIMMDC1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: glutaminase. This gene encodes the K-type mitochondrial glutaminase. The encoded protein is an phosphate-activated amidohydrolase that catalyzes the hydrolysis of glutamine to glutamate and ammonia. This protein is primarily expressed in the brain and kidney plays an essential role in generating energy for metabolism, synthesizing the brain neurotransmitter glutamate and maintaining acid-base balance in the ki…
- **Diseases (Open Targets)**: global developmental delay, progressive ataxia, and elevated glutamine (0.662); genetic developmental and epileptic encephalopathy (0.626); infantile cataract, skin abnormalities, glutamate excess, and impaired intellectual development (0.591); neurodegenerative disease (0.372); glutaminase deficiency (0.371)
- **Europe PMC papers**: 15605
- **Why important**: GLS adds a distinct nutrient-entry function by converting glutamine to glutamate and ammonia and contributing to amino-acid metabolism and intracellular glutamate homeostasis. It is included in (GO:CC mitochondrion; q_global = 0.0229) and (5 supplementary STRING terms; within-query FDR 0.0103–0.0341), appears with IARS2 in hu.MAP complex (hu.MAP huMAP3_13468.1), and is tissue-enhanced in kidney with cell-type enhancement in renal populations. Its extensive literature and disease associations involving glutamine handling and neurodevelopment make it an important metabolic bridge.
- **Conclusion**: Established evidence supports GLS as a mitochondrial glutamine-catabolism enzyme that can supply carbon and nitrogen to cellular metabolism. In this module it may complement fatty-acid oxidation and the tricarboxylic-acid cycle, but that substrate-flow model is a hypothesis rather than a demonstrated property of the tissue-pair module.

## Module 1

**Tissue pair**: circulatory_system and prostate  
**Genes (22)**: SLC3A2, SLC1A5, ACACA, CISD2, CTNND1, DDX6, FKBP4, GMPS, IMPDH2, IPO11, KRT18, KRT8, MRE11, NUP155, NUP205, ALDH18A1, PIP4K2C, PKP3, RO60, SEC63, PSAT1, TJP1

### Function

The module is best interpreted as a mixed epithelial-cell structural and cellular-maintenance program rather than a single globally enriched pathway. Its strongest network position is occupied by TJP1, which connects genes involved in cell junctions, nuclear transport, RNA handling, DNA repair, endoplasmic-reticulum protein targeting, phosphoinositide metabolism, and cellular homeostasis. The KRT8–KRT18 pair, together with CTNND1 and PKP3, supports epithelial intermediate-filament, adherens-junction, and desmosome biology. Other branches support amino-acid transport and serine or glutamate metabolism, purine and GMP synthesis, lipid synthesis, nucleocytoplasmic transport, and autophagy-related processes. No GO or KEGG term passed global correction, so these annotations describe the genes and network structure but do not establish pathway enrichment for the module.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, while many are cell-type enhanced, indicating that the shared signal may reflect cellular composition or a recurring epithelial and structural program rather than a specialized circulatory-system or prostate pathway. HPA detects many module proteins in prostate, and the prostate staining is especially consistent with a resident epithelial or stromal cellular signal. Blood-cell specificity is generally low, although a subset is immune-cell enhanced or group enriched, including associations with plasmacytoid dendritic cells, monocytes, dendritic cells, T-reg cells, NK cells, and basophils. The tissue-enhanced annotations span several organs and cell types, including intestine, stomach, salivary gland, brain, kidney, liver, pancreas, and testis. Thus, the module does not look like a plasma-protein signature and is not convincingly blood-cell specific; shared epithelial, broadly expressed housekeeping, or mixed-cell content remains a plausible explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports several established relationships within the co-abundance module. The strongest links include KRT8 with KRT18, CTNND1 with TJP1, NUP155 with NUP205, GMPS with IMPDH2, ALDH18A1 with GMPS, and SLC1A5 with SLC3A2. Additional supported relationships connect KRT18 with PKP3, ALDH18A1 with PSAT1, and ACACA with ALDH18A1. These links validate recognizable local protein relationships involving epithelial cytoskeleton and junctions, nuclear pores, purine metabolism, amino-acid transport, and intermediary metabolism. They do not validate every co-abundance edge or prove that all branches form one physical complex. No hu.MAP complex containing multiple module members was reported, and STRING functional enrichment was absent. The module therefore contains several known molecular neighborhoods but lacks evidence for one unified experimentally defined multiprotein complex.

**STRING interactions (score >= 0.7)**: 9 of 231 gene pairs: ACACA–ALDH18A1 (0.876); ALDH18A1–GMPS (0.909); ALDH18A1–PSAT1 (0.842); CTNND1–TJP1 (0.956); GMPS–IMPDH2 (0.998); KRT18–KRT8 (0.999); KRT18–PKP3 (0.707); NUP155–NUP205 (0.999); SLC1A5–SLC3A2 (0.894)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is not established as a new biological mechanism merely because the complete module lacks a hu.MAP complex or because some co-abundance relationships are not represented in STRING. The presence of well-known relationships such as the KRT8–KRT18 filament pair, the TJP1–CTNND1 junction connection, the NUP155–NUP205 nuclear-pore connection, and the GMPS–IMPDH2 metabolic connection argues that important parts of the module recapitulate established biology. The potentially novel result is the cross-tissue co-abundance organization of these otherwise heterogeneous gene neighborhoods in circulatory_system and prostate. That claim remains provisional because there is no globally significant GO or KEGG term, no STRING enrichment, no hu.MAP complex, and no independent replication or literature comparison supplied here. Absence from an interaction resource should be treated as an evidence gap, not proof of novelty.

**Hypothesis.** Hypothesis: the shared module reflects coordinated abundance of epithelial or epithelial-associated cells that maintain barrier and junctional architecture while coupling cytoskeletal organization to biosynthetic, transport, nuclear-pore, RNA-control, and stress-homeostasis functions. TJP1 may represent a structural coordination point, with the KRT8–KRT18–CTNND1–PKP3 branch marking epithelial integrity and the PSAT1–SLC3A2–SLC1A5, ALDH18A1–GMPS–IMPDH2, and NUP155–NUP205 branches representing metabolic, nutrient-transport, and nucleocytoplasmic-support states. This should be tested by cell-composition adjustment, epithelial-marker deconvolution, and replication in independent circulatory-system and prostate datasets; it should not be presented as a demonstrated mechanism.

### Important genes

#### TJP1

- **Related proteins** (co-abundance neighbors): DDX6 (0.87), CTNND1 (0.86), NUP155 (0.85), MRE11 (0.85), SEC63 (0.85), PIP4K2C (0.82), CISD2 (0.82), NUP205 (0.81), ACACA (0.80); STRING partners: CTNND1 (0.956)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cell Junctions; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tight junction protein 1. This gene encodes a member of the membrane-associated guanylate kinase (MAGUK) family of proteins, and acts as a tight junction adaptor protein that also regulates adherens junctions. Tight junctions regulate the movement of ions and macromolecules between endothelial and epithelial cells. The multidomain structure of this scaffold protein, including a postsynaptic density 95/disc-large/zona occlu…
- **Diseases (Open Targets)**: dengue disease (0.476); COVID-19 (0.373); skin disorder (0.312); Hypocalcemia (0.264); cataract (0.256)
- **Europe PMC papers**: 6421
- **Why important**: TJP1 has the central network position in the module and links the epithelial junction branch to genes involved in RNA control, nuclear transport, DNA repair, endoplasmic-reticulum targeting, phosphoinositide metabolism, and cellular homeostasis. Its HPA localization is at cell junctions, it is detected in prostate, and its annotation supports tight-junction and adherens-junction maintenance. It also has substantial literature volume and disease associations involving infectious and epithelial-related conditions.
- **Conclusion**: Established evidence supports TJP1 as the strongest structural integrator and a marker of cell-junction biology in this module. It is plausible, but not established, that coordinated TJP1 abundance helps organize the broader module signal.

#### KRT8

- **Related proteins** (co-abundance neighbors): KRT18 (0.95), CTNND1 (0.88); STRING partners: KRT18 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Intermediate filaments; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 8. This gene is a member of the type II keratin family clustered on the long arm of chromosome 12. Type I and type II keratins heteropolymerize to form intermediate-sized filaments in the cytoplasm of epithelial cells. The product of this gene typically dimerizes with keratin 18 to form an intermediate filament in simple single-layered epithelial cells. This protein plays a role in maintaining cellul…
- **Diseases (Open Targets)**: cirrhosis of liver (0.596); cirrhosis, familial (0.401); neurodegenerative disease (0.371); prostate carcinoma (0.314); Abnormality of the liver (0.306)
- **Europe PMC papers**: 5942
- **Why important**: KRT8 is part of the highly coherent KRT8–KRT18 intermediate-filament pair, has a direct CTNND1 connection in the module, and is linked by STRING to KRT18. Its HPA annotations favor epithelial cell types and it is detected in prostate. Its function in epithelial structural integrity, differentiation, and signaling, together with prostate-carcinoma and liver-disease associations and substantial literature, makes it an important indicator of epithelial composition.
- **Conclusion**: Established evidence supports KRT8 as an epithelial structural marker and as a component of a known keratin pair. The module-level interpretation that KRT8 reports shared epithelial cellular content is a hypothesis supported by the HPA pattern, not a demonstrated causal role.

#### CTNND1

- **Related proteins** (co-abundance neighbors): KRT8 (0.88), TJP1 (0.86), PKP3 (0.82); STRING partners: TJP1 (0.956)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin delta 1. This gene encodes a member of the Armadillo protein family, which function in adhesion between cells and signal transduction. Multiple translation initiation codons and alternative splicing result in many different isoforms being translated. Not all of the full-length natures of the described transcript variants have been determined. Read-through transcription also exists between this gene and the…
- **Diseases (Open Targets)**: blepharocheilodontic syndrome (0.724); listeriosis (0.526); cleft lip (0.510); hereditary disease (0.415); exudative vitreoretinopathy (0.376)
- **Europe PMC papers**: 3021
- **Why important**: CTNND1 connects KRT8, TJP1, and PKP3, thereby occupying the junctional bridge between intermediate filaments, adherens junctions, and desmosomal architecture. Its annotation describes cadherin-mediated adhesion and cell migration, while HPA places it at the plasma membrane and detects it in prostate. It also has substantial literature and disease associations involving developmental and vascular-adhesion phenotypes.
- **Conclusion**: Established evidence supports CTNND1 as a meaningful adhesion-network connector. Its centrality within the epithelial branch supports a structural interpretation, whereas any role in coordinating the metabolic branches remains hypothetical.

#### GMPS

- **Related proteins** (co-abundance neighbors): IPO11 (0.86), ALDH18A1 (0.82), PSAT1 (0.81); STRING partners: ALDH18A1 (0.909), IMPDH2 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: guanosine monophosphate synthase. In the de novo synthesis of purine nucleotides, IMP is the branch point metabolite at which point the pathway diverges to the synthesis of either guanine or adenine nucleotides. In the guanine nucleotide pathway, there are 2 enzymes involved in converting IMP to GMP, namely IMP dehydrogenase (IMPD1), which catalyzes the oxidation of IMP to XMP, and GMP synthetase, which catalyzes the amination of …
- **Diseases (Open Targets)**: rheumatoid arthritis (0.277); nephrotic syndrome (0.259); lupus nephritis (0.259); rhabdomyosarcoma (0.247); hepatocellular carcinoma (0.237)
- **Europe PMC papers**: 5161
- **Why important**: GMPS links the module's metabolic branch to ALDH18A1 and PSAT1 and has a very strong STRING relationship with IMPDH2, the upstream enzyme in de novo guanine-nucleotide production. Its annotation directly supports GMP and purine biosynthesis, and it has substantial literature plus disease associations involving inflammatory, renal, and malignant conditions. The module topology therefore places GMPS at a plausible interface between nucleotide supply and other biosynthetic processes.
- **Conclusion**: Established evidence supports GMPS as a purine-biosynthesis component connected to IMPDH2. It is reasonable to hypothesize that this branch reflects biosynthetic demand in the shared cell population, but the module does not establish altered purine flux.

#### SLC1A5

- **Related proteins** (co-abundance neighbors): CISD2 (0.80); STRING partners: SLC3A2 (0.894)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 1 member 5. The SLC1A5 gene encodes a sodium-dependent neutral amino acid transporter that can act as a receptor for RD114/type D retrovirus (Larriba et al., 2001 [PubMed 11781704]).[supplied by OMIM, Jan 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.463); substance abuse (0.231); attention deficit-hyperactivity disorder (0.231); autoimmune disorder of central nervous system (0.213); hypotensive disorder (0.188)
- **Europe PMC papers**: 5038
- **Why important**: SLC1A5 is connected to CISD2 in the module and to SLC3A2 in STRING, forming a recognizable amino-acid transport neighborhood. Its annotation supports glutamine and neutral amino-acid transport, and HPA identifies cell-type enhancement in basal prostatic and prostatic hillock cells as well as plasmacytoid dendritic cells. Its substantial literature makes it informative for interpreting nutrient handling and cell-state composition.
- **Conclusion**: Established evidence supports SLC1A5 as an amino-acid transporter associated with prostatic epithelial cell types and a known transporter partner. A coordinated nutrient-support role in the module is a hypothesis, not proof that transport activity is increased.

## Module 2

**Tissue pair**: circulatory_system and prostate  
**Genes (5)**: ACY1, EEF1A2, NUDT5, CTSA, PTPRF

### Function

The strongest functional interpretation is regulation of chaperone-mediated autophagy, supported by the globally corrected GO term (GO:BP regulation of chaperone-mediated autophagy; q_global = 0.0171), which includes CTSA and EEF1A2. CTSA provides a lysosomal and proteostasis connection through its role in a lysosomal multienzyme complex, while EEF1A2 links the module to translation and translational elongation in addition to chaperone-mediated autophagy. The remaining genes provide compatible but less direct context: PTPRF is a receptor-type protein tyrosine phosphatase involved in signaling, adhesion, migration, and dephosphorylation; ACY1 participates in amino-acid salvage; and NUDT5 participates in nucleotide and ADP-ribose metabolism. Thus, the module is best viewed as a coordinated proteostasis and intracellular metabolic-signaling program rather than as a narrowly defined physical protein complex. No STRING functional-enrichment term was reported.

**Cell composition.** The module is not dominated by plasma proteins or classical secreted proteins. Two members are annotated as intracellular and membrane-associated, while the other members have no secretome annotation. HPA evidence argues against a blood-cell-dominated module: the genes have low immune-cell specificity or are not detected in immune cells, although CTSA is enriched in platelets and NUDT5 is associated with Hofbauer cells and neutrophils at the single-cell level. Tissue expression is heterogeneous rather than prostate-specific, with EEF1A2 enhanced in heart and skeletal muscle, ACY1 group-enriched in intestine, kidney, and liver, and CTSA enhanced in adrenal gland. In prostate, protein was detected for PTPRF and CTSA but not for the other members. The shared circulatory-system and prostate signal could therefore reflect coordinated expression in particular cellular compartments, tissue admixture, or common intracellular state rather than a prostate-specific secreted or blood-cell program.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulation of chaperone-mediated autophagy | 0.0171 | CTSA, EEF1A2 |

### STRING and hu.MAP

The co-abundance graph connects all members through a sparse set of expression relationships, with PTPRF acting as the principal network connector and linking EEF1A2, CTSA, and NUDT5, while EEF1A2 connects to ACY1. However, none of the possible gene pairs reaches the supplied high-confidence STRING interaction threshold, and no STRING functional-enrichment term is present. No hu.MAP complex contains multiple module members. These results indicate that the co-abundance structure is not corroborated as a known physical interaction network or established multiprotein complex. The module may instead represent coordinated regulation, shared cellular composition, or indirect pathway coupling.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be declared a definitively new biological discovery solely because it is absent from STRING and hu.MAP. Nevertheless, its particular cross-tissue co-abundance combination appears weakly supported by currently catalogued physical interactions and complexes, while the globally significant functional signal is restricted to the CTSA–EEF1A2 overlap in (GO:BP regulation of chaperone-mediated autophagy; q_global = 0.0171). The cautious conclusion is that the shared co-abundance pattern is a potentially novel systems-level association, but its novelty and biological specificity require validation in independent cohorts, cell-resolved data, and experimental perturbation. The absence of a globally significant term beyond (GO:BP regulation of chaperone-mediated autophagy; q_global = 0.0171) limits claims about additional pathway functions.

**Hypothesis.** Hypothesis: the module reflects a coordinated intracellular proteostasis state in which lysosomal processing by CTSA and translational or stress-related functions involving EEF1A2 are coupled to receptor-tyrosine-phosphatase signaling through PTPRF, with ACY1 and NUDT5 contributing metabolic and nucleotide-state context. In circulatory-system and prostate samples, this program may arise from shared cellular states or cellular admixture rather than direct binding among the encoded proteins. This hypothesis predicts that perturbing lysosomal autophagy or translational stress should alter the abundance of several module members together, whereas direct physical interaction among all members is not expected.

### Important genes

#### PTPRF

- **Related proteins** (co-abundance neighbors): EEF1A2 (0.82), CTSA (0.82), NUDT5 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein tyrosine phosphatase receptor type F. The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP possesses an extracellular region, a single transmembrane region, and two tandem intracytoplasmic catalytic domains, and thu…
- **Diseases (Open Targets)**: breasts and/or nipples, aplasia or hypoplasia of, 2 (0.505); smoking initiation (0.420); attention deficit-hyperactivity disorder (0.419); isolated congenital breast hypoplasia/aplasia (0.370); substance-related disorder (0.329)
- **Europe PMC papers**: 4709
- **Why important**: PTPRF is the main network connector in the module and links the autophagy-associated pair, EEF1A2 and CTSA, with NUDT5. Its established receptor-type protein tyrosine phosphatase architecture and annotations in cell adhesion, signal transduction, cell migration, and dephosphorylation make it a plausible regulatory interface between intracellular state and membrane-associated signaling. It has a substantial literature and prostate protein detection, strengthening its value for follow-up.
- **Conclusion**: Established: PTPRF is a receptor-type protein tyrosine phosphatase with a central position in this co-abundance graph and broad signaling functions. Hypothesis: it may regulate or report the cellular state that coordinates the module, but the supplied data do not establish a causal link to chaperone-mediated autophagy.

#### CTSA

- **Related proteins** (co-abundance neighbors): PTPRF (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Vesicles; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cathepsin A. This gene encodes a member of the peptidase S10 family of serine carboxypeptidases. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate two chains that comprise the heterodimeric active enzyme. This enzyme possesses deamidase, esterase and carboxypeptidase activities and acts as a scaffold in the …
- **Diseases (Open Targets)**: galactosialidosis (0.842); cathepsin a-related arteriopathy-strokes-leukoencephalopathy (0.464); hereditary disease (0.451); lysosomal storage disease (0.373); Lynch syndrome (0.340)
- **Europe PMC papers**: 8422
- **Why important**: CTSA is one of the two genes in the globally corrected GO term (GO:BP regulation of chaperone-mediated autophagy; q_global = 0.0171). It encodes a lysosomal serine carboxypeptidase with deamidase and esterase activities and acts as a scaffold in a lysosomal multienzyme complex. It is also the most extensively studied member by the supplied literature measure, has a strong disease connection to galactosialidosis, is associated with platelets, and is detected in prostate.
- **Conclusion**: Established: CTSA provides the clearest lysosomal and proteostasis anchor for the module and directly supports (GO:BP regulation of chaperone-mediated autophagy; q_global = 0.0171). Hypothesis: CTSA may be a functional driver or sensitive marker of the shared autophagy-related state, although co-abundance alone cannot distinguish either possibility.

#### EEF1A2

- **Related proteins** (co-abundance neighbors): PTPRF (0.82), ACY1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation elongation factor 1 alpha 2. This gene encodes an isoform of the alpha subunit of the elongation factor-1 complex, which is responsible for the enzymatic delivery of aminoacyl tRNAs to the ribosome. This isoform (alpha 2) is expressed in brain, heart and skeletal muscle, and the other isoform (alpha 1) is expressed in brain, placenta, lung, liver, kidney, and pancreas. This gene may be critical in the development of ovarian c…
- **Diseases (Open Targets)**: undetermined early-onset epileptic encephalopathy (0.721); developmental and epileptic encephalopathy, 33 (0.721); genetic developmental and epileptic encephalopathy (0.584); infantile epileptic encephalopathy (0.575); intellectual disability, autosomal dominant 38 (0.552)
- **Europe PMC papers**: 1771
- **Why important**: EEF1A2 is the second gene in (GO:BP regulation of chaperone-mediated autophagy; q_global = 0.0171) and connects directly to CTSA through the module network via PTPRF. It encodes a translation elongation factor isoform expressed in brain, heart, and skeletal muscle and is annotated in translation, translational elongation, lipid-kinase regulation, and chaperone-mediated autophagy. Its disease associations include developmental and epileptic encephalopathy, giving it biological importance beyond this module.
- **Conclusion**: Established: EEF1A2 contributes direct primary evidence for regulation of chaperone-mediated autophagy and has a well-defined translation-related function. Hypothesis: its presence may indicate coupling between translational activity and autophagic quality control in the shared tissue signal.

#### ACY1

- **Related proteins** (co-abundance neighbors): EEF1A2 (0.81); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aminoacylase 1. This gene encodes a cytosolic, homodimeric, zinc-binding enzyme that catalyzes the hydrolysis of acylated L-amino acids to L-amino acids and an acyl group, and has been postulated to function in the catabolism and salvage of acylated amino acids. This gene is located on chromosome 3p21.1, a region reduced to homozygosity in small-cell lung cancer (SCLC), and its expression has been reported to be …
- **Diseases (Open Targets)**: aminoacylase 1 deficiency (0.810); Intellectual disability (0.466); hereditary disease (0.452); toxic encephalopathy (0.370); inborn aminoacylase deficiency (0.266)
- **Europe PMC papers**: 719
- **Why important**: ACY1 is connected to EEF1A2 and contributes a distinct metabolic axis. It encodes a cytosolic aminoacylase involved in hydrolysis and salvage of acylated amino acids, is group-enriched in intestine, kidney, and liver, and has disease associations including aminoacylase deficiency and intellectual disability. Its more limited literature volume than CTSA or PTPRF makes it especially useful as a test of whether the module extends beyond canonical autophagy biology.
- **Conclusion**: Established: ACY1 is an amino-acid catabolism and salvage enzyme with tissue-enriched expression and a disease connection to aminoacylase deficiency. Hypothesis: it may reflect metabolic substrate availability that influences, or is influenced by, the proteostasis state represented by the module; this connection is not established by the supplied evidence.

#### NUDT5

- **Related proteins** (co-abundance neighbors): PTPRF (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nudix hydrolase 5. This gene belongs to the Nudix (nucleoside diphosphate linked moiety X) hydrolase superfamily. The encoded enzyme catalyzes the hydrolysis of modified nucleoside diphosphates, including ADP-ribose (ADPR) and 8-oxoGua-containing 8-oxo-dADP and 8-oxo-dGDP. Protein-bound ADP ribose can be hazardous to the cell because it can modify some amino acid residues, resulting in the inhibition of ATP-activate…
- **Diseases (Open Targets)**: neurodegenerative disease (0.513); type 2 diabetes mellitus (0.332); coronary artery disorder (0.324); gout (0.315); diabetic neuropathy (0.315)
- **Europe PMC papers**: 847
- **Why important**: NUDT5 is connected to PTPRF and contributes nucleotide and redox-related biochemical context through hydrolysis of modified nucleoside diphosphates, including ADP-ribose and oxidized guanine-containing nucleotides. It is annotated in nucleotide metabolism and chromatin remodeling and has disease associations involving neurodegeneration, diabetes, coronary artery disorder, gout, and diabetic neuropathy.
- **Conclusion**: Established: NUDT5 is a nucleotide-metabolism enzyme with functions relevant to modified nucleotides and cellular stress. Hypothesis: its co-abundance with PTPRF may mark a signaling-linked nucleotide or oxidative-stress component of the module, but no direct mechanistic connection to the autophagy term has been demonstrated.

## Module 3

**Tissue pair**: circulatory_system and prostate  
**Genes (6)**: AIMP1, BCLAF1, CNOT12, LIMA1, PYM1, SEC16A

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established shared pathway. Its gene annotations instead point to several connected cellular themes: SEC16A supports endoplasmic-reticulum to Golgi transport and COPII vesicle formation; LIMA1 supports actin filament organization and cell migration; PYM1 supports exon-junction-complex disassembly, nonsense-mediated decay, and translation; AIMP1 has cytosolic translation-related functions as well as signaling, angiogenesis, inflammation, and wound-healing activities; BCLAF1 is associated with transcriptional regulation, apoptosis, DNA-damage response, and mRNA stabilization; and CNOT12 is associated with the CCR4-NOT complex, RNA regulation, and DNA-damage repair. The co-abundance pattern is therefore best interpreted as a mixed cellular stress, trafficking, cytoskeletal, and RNA-processing signal rather than a demonstrated single molecular pathway. This interpretation is provisional because the module contains only sparse pairwise connectivity and no STRING enrichment.

**Cell composition.** The HPA evidence argues against a module dominated by plasma proteins, secreted proteins, or blood-cell contamination. Most genes have low tissue specificity and low immune-cell specificity, one gene is secreted to blood, and no recurrent enriched blood-cell population is reported. One gene is tissue enhanced in bone marrow, while several show cell-type-enhanced expression in distinct epithelial, stromal, or trophoblast populations rather than one shared cell type. Protein detection is reported for most module genes in prostate, whereas no matching circulatory-system tissue result is available. Thus the shared signal could reflect broadly expressed cellular programs present in both tissues, with a possible contribution from differing cell populations, but the evidence does not support a specifically blood-derived module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction meets the supplied high-confidence threshold, and there is no STRING functional enrichment. This means that the co-abundance edges are not independently supported here as established physical or functional protein interactions. hu.MAP provides one partial complex connection, C1, containing PYM1 and BCLAF1 among many other complex members. Because only a small portion of that large complex is represented, C1 supports known participation of those genes in a broad RNA-processing or nuclear regulatory context but does not establish that the whole module is one complex. SEC16A, CNOT12, LIMA1, and AIMP1 have no listed hu.MAP complex membership in this evidence set.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11073.1 (PYM1, BCLAF1; 2/67)

### Novelty

The module may be a new tissue-pair co-abundance observation, but it cannot be called a newly discovered molecular complex or pathway. The absence of STRING support and the limited hu.MAP overlap make the particular cross-tissue co-abundance arrangement potentially novel, while also reducing confidence that it reflects direct molecular interaction. Existing annotations and the partial C1 membership show that several component functions are already known. A defensible novelty claim would therefore be that this specific shared expression pattern is a candidate observation requiring replication, not that the underlying biology is entirely new.

**Hypothesis.** Hypothesis: the module reflects coordinated activity of a broadly expressed epithelial or stromal cellular program in which ER-to-Golgi trafficking and membrane organization are coupled to cytoskeletal remodeling, RNA quality control, translation, and stress or apoptosis responses. SEC16A could mark the trafficking component, LIMA1 the actin and junctional component, PYM1 and BCLAF1 an RNA-processing or nuclear-response component, and AIMP1 a secreted or intracellular signaling component. This model predicts that the co-abundance relationship will be strongest in matched cell populations or under tissue stress, but it is not established by the enrichment, STRING, or hu.MAP evidence supplied.

### Important genes

#### SEC16A

- **Related proteins** (co-abundance neighbors): PYM1 (0.84), CNOT12 (0.84), AIMP1 (0.82), BCLAF1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC16 homolog A, endoplasmic reticulum export factor. This gene encodes a protein that forms part of the Sec16 complex. This protein has a role in protein transport from the endoplasmic reticulum (ER) to the Golgi and mediates COPII vesicle formation at the transitional ER. Alternative splicing results in multiple transcript variants that encode different protein isoforms. [provided by RefSeq, Feb 2013].
- **Diseases (Open Targets)**: squamous cell carcinoma (0.288); Crohn disease (0.277); bladder calculus (0.241); nephrolithiasis (0.235); actinic keratosis (0.215)
- **Europe PMC papers**: 595
- **Why important**: SEC16A is the central network connector, linking PYM1, CNOT12, AIMP1, and BCLAF1. Its established ER-to-Golgi transport, COPII vesicle, Golgi trafficking, and ER-organization functions provide the clearest cellular-process anchor for the module. It is broadly expressed, detected in prostate, and has substantial literature support, while its disease associations include squamous cell carcinoma, Crohn disease, bladder calculus, nephrolithiasis, and actinic keratosis.
- **Conclusion**: Established evidence supports SEC16A as a trafficking and ER-organization gene and as the module’s main network bridge. It is plausible, but not demonstrated, that SEC16A coordinates the other module signals through shared cell-state regulation rather than direct protein interactions.

#### AIMP1

- **Related proteins** (co-abundance neighbors): SEC16A (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aminoacyl tRNA synthetase complex interacting multifunctional protein 1. The protein encoded by this gene is a cytokine that is specifically induced by apoptosis, and it is involved in the control of angiogenesis, inflammation, and wound healing. The release of this cytokine renders the tumor-associated vasculature sensitive to tumor necrosis factor. The precursor protein is identical to the p43 subunit, which is associated with the multi-tRNA synthetase complex, and i…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 3 (0.790); Pelizaeus-Merzbacher-like disease (0.657); POLR-related leukodystrophy (0.657); leukodystrophy (0.372); autosomal recessive non-syndromic intellectual disability (0.371)
- **Europe PMC papers**: 663
- **Why important**: AIMP1 connects directly to SEC16A and is the only module gene annotated as secreted to blood. It has unusually broad functional relevance in the supplied annotations, spanning tRNA aminoacylation, translation, endothelial proliferation, blood-vessel morphogenesis, leukocyte migration, inflammation, angiogenesis, and wound healing. Its disease associations include several leukodystrophy-related conditions, and its literature support is substantial.
- **Conclusion**: Established evidence supports AIMP1 as a multifunctional translation-associated protein and cytokine with vascular and inflammatory roles. Its secretion makes it a plausible contributor to a tissue-to-circulation signal, but the module data do not show that circulating AIMP1 drives the co-abundance pattern.

#### LIMA1

- **Related proteins** (co-abundance neighbors): CNOT12 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LIM domain and actin binding 1. This gene encodes a cytoskeleton-associated protein that inhibits actin filament depolymerization and cross-links filaments in bundles. It is downregulated in some cancer cell lines. Alternatively spliced transcript variants encoding different isoforms have been described for this gene, and expression of some of the variants maybe independently regulated. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.327); hypertensive disorder (0.276); malunion fracture (0.189); nephrotic syndrome (0.169); Abnormality of the skeletal system (0.157)
- **Europe PMC papers**: 1156
- **Why important**: LIMA1 is the strongest direct link to cytoskeletal and junctional biology in the module. It is connected to CNOT12, localizes to the plasma membrane and actin filaments, and is associated with actin bundling, inhibition of actin depolymerization, cell migration, ruffle organization, and cholesterol absorption. It is detected in prostate, has cell-type-enhanced expression in several epithelial or stromal populations, and has extensive literature support.
- **Conclusion**: Established evidence supports LIMA1 as an actin-associated regulator of cellular architecture and migration. Its cell-type pattern suggests that cell composition could influence the module, while any mechanistic coupling between LIMA1 and SEC16A remains a hypothesis rather than a demonstrated interaction.

#### BCLAF1

- **Related proteins** (co-abundance neighbors): SEC16A (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_11073.1
- **Function (MyGene.info)**: BCL2 associated transcription factor 1. This gene encodes a transcriptional repressor that interacts with several members of the BCL2 family of proteins. Overexpression of this protein induces apoptosis, which can be suppressed by co-expression of BCL2 proteins. The protein localizes to dot-like structures throughout the nucleus, and redistributes to a zone near the nuclear envelope in cells undergoing apoptosis. Multiple transcript var…
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); Pulmonary artery atresia (0.416); acute myeloid leukemia (0.357); bronchial disorder (0.288); Vertigo (0.253)
- **Europe PMC papers**: 1702
- **Why important**: BCLAF1 is connected to SEC16A and is one of the two module members in hu.MAP complex C1. Its annotations span apoptosis, DNA-damage response, transcriptional repression and activation, and mRNA stabilization. It is tissue enhanced in bone marrow, detected in prostate, and has the largest literature volume among the listed genes, with disease associations including neurodegenerative disease, pulmonary artery atresia, acute myeloid leukemia, and bronchial disorder.
- **Conclusion**: Established evidence supports BCLAF1 as a nuclear transcriptional and apoptosis-related regulator with participation in the broad C1 complex. Its presence may indicate a stress or cell-survival state, but the evidence does not establish a direct BCLAF1 connection to SEC16A or the other module genes.

#### PYM1

- **Related proteins** (co-abundance neighbors): SEC16A (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_11073.1
- **Function (MyGene.info)**: PYM1 exon junction complex associated factor. Enables ribosome binding activity. Involved in exon-exon junction complex disassembly; nuclear-transcribed mRNA catabolic process, nonsense-mediated decay; and positive regulation of translation. Located in cell junction; cytosol; and nuclear lumen. Part of exon-exon junction complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Alzheimer disease (0.049); esophageal cancer (0.033); neoplasm (0.030); hypothyroidism (0.026); cancer (0.025)
- **Europe PMC papers**: 132
- **Why important**: PYM1 is the second module member in hu.MAP complex C1 and is connected to SEC16A. Its established functions in exon-junction-complex disassembly, nonsense-mediated decay, and positive regulation of translation provide a plausible RNA-quality-control component. It is detected in prostate and has cell-type-enhanced expression in esophageal epithelial populations, with disease associations including esophageal cancer and other neoplastic or neurological conditions.
- **Conclusion**: Established evidence supports PYM1 as an RNA surveillance and translation-associated factor and supports its partial membership in C1. Its co-abundance with SEC16A may reflect a shared cellular state or coordinated gene regulation; a direct trafficking-to-RNA-quality-control mechanism is only a hypothesis.

## Module 4

**Tissue pair**: circulatory_system and prostate  
**Genes (8)**: ALB, COL6A1, FN1, GLIPR2, GSN, LAMB1, LAMB2, LTF

### Function

The strongest interpretation is an extracellular-matrix and basement-membrane module. The primary evidence is the enrichment of extracellular-matrix structural constituent (GO:MF extracellular matrix structural constituent; q_global = 4.23e-05), basement membrane (GO:CC basement membrane; q_global = 0.000227), external encapsulating structure (GO:CC external encapsulating structure; q_global = 0.000662), extracellular matrix (GO:CC extracellular matrix; q_global = 0.000662), and ECM-receptor interaction (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.00113). Basement-membrane organization (GO:BP basement membrane organization; q_global = 0.00286), regulation of extracellular-matrix organization (GO:BP regulation of extracellular matrix organization; q_global = 0.0155), integrin signaling (KEGG Integrin signaling - Homo sapiens (human); q_global = 0.0123), focal adhesion (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.0231), and PI3K-Akt signaling (KEGG PI3K-Akt signaling pathway - Homo sapiens (human); q_global = 0.0123) support a matrix-associated cell-adhesion and signaling program. The endoderm-related terms (GO:BP endoderm formation; q_global = 0.0112), (GO:BP endodermal cell differentiation; q_global = 0.0112), (GO:BP endoderm development; q_global = 0.0262), and (GO:BP formation of primary germ layer; q_global = 0.0328) are consistent with developmental or tissue-structural annotation but should not be treated as evidence that the adult module specifically performs endoderm development. The small-cell-lung-cancer and human-papillomavirus pathway terms (KEGG Small cell lung cancer - Homo sapiens (human); q_global = 0.04) and (KEGG Human papillomavirus infection - Homo sapiens (human); q_global = 0.0453) are pathway annotations containing matrix genes, not evidence that the module represents either disease. Overall, the module most plausibly reflects extracellular scaffold composition, basement-membrane organization, and matrix-mediated adhesion or signaling.

**Cell composition.** This is predominantly a secreted or extracellular-protein module rather than a conventional intracellular housekeeping module. The HPA summary identifies most members as secreted, and the individual annotations identify COL6A1, LAMB1, and LAMB2 as secreted to extracellular matrix, while FN1, LTF, GSN, and ALB are secreted to blood. HPA points toward fibroblasts, hepatic stellate cells, and peritubular myoid cells, with additional enrichment in hepatocytes, vascular or stromal contexts, and selected blood-cell populations. ALB is liver-enriched and hepatocyte-enriched, and LTF has bone-marrow and neutrophil or monocyte associations. Therefore, the shared circulatory-system and prostate signal may reflect extracellular matrix from stromal or vascular cells, but it may also partly reflect plasma carryover, secreted proteins in blood, or shared stromal cell types. The absence of immune-cell detection for several matrix genes argues against interpreting the whole module as an immune-cell module. Prostate protein detection is reported for LTF and GLIPR2, whereas the other listed prostate protein measurements were not detected; this limits direct tissue-level interpretation.

**GO/KEGG enrichment**: 18 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF extracellular matrix structural constituent | 4.23e-05 | COL6A1, FN1, LAMB1, LAMB2 |
| GO:CC basement membrane | 0.000227 | COL6A1, FN1, LAMB1, LAMB2 |
| GO:CC external encapsulating structure | 0.000662 | COL6A1, FN1, LAMB1, LAMB2 |
| GO:CC extracellular matrix | 0.000662 | COL6A1, FN1, LAMB1, LAMB2 |
| KEGG ECM-receptor interaction - Homo sapiens (human) | 0.00113 | COL6A1, FN1, LAMB1, LAMB2 |
| GO:BP basement membrane organization | 0.00286 | COL6A1, LAMB1, LAMB2 |
| GO:CC endoplasmic reticulum lumen | 0.00382 | ALB, COL6A1, FN1, LAMB1, LAMB2 |
| GO:BP endoderm formation | 0.0112 | COL6A1, FN1, LAMB1 |
| GO:BP endodermal cell differentiation | 0.0112 | COL6A1, FN1, LAMB1 |
| GO:BP positive regulation of cell differentiation | 0.012 | FN1, GLIPR2, LAMB1, LAMB2, LTF |
| KEGG PI3K-Akt signaling pathway - Homo sapiens (human) | 0.0123 | COL6A1, FN1, LAMB1, LAMB2 |
| KEGG Integrin signaling - Homo sapiens (human) | 0.0123 | COL6A1, FN1, LAMB1, LAMB2 |
| GO:BP regulation of extracellular matrix organization | 0.0155 | COL6A1, LAMB1, LAMB2 |
| KEGG Focal adhesion - Homo sapiens (human) | 0.0231 | COL6A1, FN1, LAMB1, LAMB2 |
| GO:BP endoderm development | 0.0262 | COL6A1, FN1, LAMB1 |

### STRING and hu.MAP

STRING supports several biologically coherent relationships already known from the database: ALB-FN1, ALB-LTF, COL6A1-FN1, COL6A1-LAMB1, FN1-GSN, and LAMB1-LAMB2. The STRING functional results independently emphasize secreted and extracellular proteins, extracellular matrix, laminin complex, collagen-containing extracellular matrix, cell-matrix adhesion, ECM-receptor interaction, and PI3K-Akt signaling (STRING Keyword Secreted; within-query FDR = 8.88e-07) through (STRING RCTM Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs); within-query FDR = 0.0015). These findings indicate that the module contains a real, partly pre-existing extracellular network rather than an arbitrary collection of genes. However, STRING evidence is supplementary and its reported FDR values are not global correction across all module tests. No hu.MAP complex contains multiple members of this module, so there is no independent hu.MAP complex-level support for a defined multiprotein complex.

**STRING interactions (score >= 0.7)**: 6 of 28 gene pairs: ALB–FN1 (0.998); ALB–LTF (0.996); COL6A1–FN1 (0.78); COL6A1–LAMB1 (0.843); FN1–GSN (0.809); LAMB1–LAMB2 (0.783)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Secreted (FDR = 8.88e-07, 7 genes); Keyword Signal (FDR = 1.52e-05, 7 genes); COMPARTMENTS External encapsulating structure (FDR = 1.61e-05, 5 genes); Keyword Extracellular matrix (FDR = 2.6e-05, 4 genes); Function Extracellular matrix structural constituent (FDR = 6.46e-05, 4 genes); KEGG ECM-receptor interaction (FDR = 0.00025, 4 genes); RCTM ECM proteoglycans (FDR = 0.00035, 4 genes); Keyword Disulfide bond (FDR = 0.00056, 6 genes); Keyword Glycoprotein (FDR = 0.00067, 6 genes); COMPARTMENTS Extracellular region (FDR = 0.00087, 7 genes); COMPARTMENTS Laminin complex (FDR = 0.00087, 3 genes); COMPARTMENTS Collagen-containing extracellular matrix (FDR = 0.00087, 4 genes); COMPARTMENTS Protein complex involved in cell-matrix adhesion (FDR = 0.00087, 3 genes); KEGG PI3K-Akt signaling pathway (FDR = 0.0012, 4 genes); RCTM Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) (FDR = 0.0015, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be called a wholly new molecular interaction network. Several of its relationships and functional associations are already represented in STRING, especially the links involving FN1, COL6A1, LAMB1, LAMB2, ALB, LTF, and GSN. At the same time, the co-abundance module is not simply equivalent to a known hu.MAP complex, and the tissue-pair context may provide a new observation about coordinated abundance across circulatory system and prostate. The appropriate conclusion is therefore context-specific novelty rather than discovery of previously unknown protein interactions. Its novelty would require validation against independent tissue cohorts and control for plasma contamination, stromal composition, and shared cell types; absence from hu.MAP alone cannot establish novelty.

**Hypothesis.** Hypothesis: a shared vascular or stromal extracellular-matrix program links circulatory-system and prostate samples. COL6A1, LAMB1, and LAMB2 may provide a collagen- and laminin-rich basement-membrane scaffold, while FN1 may connect that scaffold to cell-surface adhesion and integrin-associated signaling. Secreted ALB and LTF, together with blood-associated GSN, may contribute a circulating-protein component or may mark sample exposure to plasma and secretory-cell products. In this model, the module reflects coordinated matrix deposition and matrix-mediated signaling superimposed on a variable blood-derived secretome, rather than a single intracellular pathway. This is a testable hypothesis, not an established causal mechanism.

### Important genes

#### COL6A1

- **Related proteins** (co-abundance neighbors): GSN (0.93), GLIPR2 (0.91), LAMB2 (0.90), LTF (0.89), LAMB1 (0.86); STRING partners: FN1 (0.78), LAMB1 (0.843)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is the most connected member in the supplied module network and is linked within the module to GSN, GLIPR2, LAMB2, LTF, and LAMB1. It participates in nearly all of the core extracellular-matrix, basement-membrane, ECM-receptor, integrin, focal-adhesion, and matrix-organization terms, including (GO:MF extracellular matrix structural constituent; q_global = 4.23e-05) through (GO:CC endoplasmic reticulum lumen; q_global = 0.00382), (KEGG PI3K-Akt signaling pathway - Homo sapiens (human); q_global = 0.0123) through (GO:BP formation of primary germ layer; q_global = 0.0328), and (KEGG Human papillomavirus infection - Homo sapiens (human); q_global = 0.0453). Its annotation identifies collagen VI as a structural component of microfibrils, and its disease associations include Bethlem myopathy and Ullrich congenital muscular dystrophy. Its substantial literature supports an established structural role, while its position suggests that it may organize the shared matrix signal.
- **Conclusion**: Established: COL6A1 is an extracellular-matrix collagen with strong module connectivity and broad support from the primary enrichment results. Hypothesis: it is a central scaffold component linking laminin-associated and secreted proteins in this tissue-pair module. The network supports centrality, but does not by itself prove that COL6A1 causally drives the co-abundance pattern.

#### FN1

- **Related proteins** (co-abundance neighbors): LAMB2 (0.91); STRING partners: ALB (0.998), COL6A1 (0.78), GSN (0.809)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 is a major extracellular glycoprotein present in both soluble plasma and cell-associated matrix forms. It appears in most of the core primary matrix and adhesion terms, including (GO:MF extracellular matrix structural constituent; q_global = 4.23e-05) through (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.00113), (GO:CC endoplasmic reticulum lumen; q_global = 0.00382) through (KEGG Integrin signaling - Homo sapiens (human); q_global = 0.0123), and (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.0231) through (KEGG Human papillomavirus infection - Homo sapiens (human); q_global = 0.0453). STRING provides strong known associations with ALB and additional associations with COL6A1 and GSN. FN1 is annotated for cell adhesion, cell-matrix adhesion, migration, wound healing, coagulation, and integrin-mediated signaling, and it has extensive literature and disease associations including fibronectin-deposit glomerulopathy and coronary artery disorder.
- **Conclusion**: Established: FN1 is a well-characterized bridge between soluble plasma fibronectin, extracellular matrix, and cell-adhesion signaling. Hypothesis: FN1 may be the principal interface connecting the basement-membrane scaffold to circulating-protein variation in this module. Its low module degree does not negate its biological importance because database-supported functional connectivity is strong.

#### LAMB1

- **Related proteins** (co-abundance neighbors): COL6A1 (0.86); STRING partners: COL6A1 (0.843), LAMB2 (0.783)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit beta 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins are composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respecti…
- **Diseases (Open Targets)**: cobblestone lissencephaly without muscular or ocular involvement (0.800); Fuchs' endothelial dystrophy (0.494); eye disorder (0.434); corneal disorder (0.424); corneal dystrophy (0.423)
- **Europe PMC papers**: 3735
- **Why important**: LAMB1 is present in every primary enrichment term listed for this module and is connected in the module to COL6A1. STRING supports relationships with COL6A1 and LAMB2 and places LAMB1 in laminin, extracellular-matrix, basement-membrane, and cell-matrix adhesion annotations (STRING Keyword Secreted; within-query FDR = 8.88e-07) through (STRING RCTM Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs); within-query FDR = 0.0015). Laminins are major noncollagenous basement-membrane constituents involved in adhesion, migration, differentiation, and signaling. Its HPA annotation points toward placenta and stromal cell types, and its disease associations include cobblestone lissencephaly and corneal disorders.
- **Conclusion**: Established: LAMB1 is a basement-membrane laminin subunit that gives the module a coherent structural interpretation alongside COL6A1 and LAMB2. Hypothesis: LAMB1 may help define a stromal or vascular basement-membrane state shared by the two tissues. The co-abundance data do not establish whether its abundance reflects production, deposition, or altered matrix turnover.

#### LAMB2

- **Related proteins** (co-abundance neighbors): FN1 (0.91), COL6A1 (0.90), LTF (0.88); STRING partners: LAMB1 (0.783)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit beta 2. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: LAMB2-related infantile-onset nephrotic syndrome (0.808); Pierson syndrome (0.797); nephrotic syndrome (0.496); eye disorder (0.434); synaptic congenital myasthenic syndrome (0.381)
- **Europe PMC papers**: 2504
- **Why important**: LAMB2 is a connected laminin component associated in the module with FN1, COL6A1, and LTF, and STRING supports its relationships with LAMB1. It contributes to the primary extracellular-matrix, basement-membrane, ECM-receptor, integrin, focal-adhesion, and PI3K-Akt signals, including (GO:MF extracellular matrix structural constituent; q_global = 4.23e-05) through (GO:CC endoplasmic reticulum lumen; q_global = 0.00382), (GO:BP positive regulation of cell differentiation; q_global = 0.012) through (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.0231), (KEGG Small cell lung cancer - Homo sapiens (human); q_global = 0.04), and (KEGG Human papillomavirus infection - Homo sapiens (human); q_global = 0.0453). Its annotation supports roles in cell adhesion, basement-membrane organization, and integrin-mediated signaling. Its disease associations include Pierson syndrome and LAMB2-related infantile-onset nephrotic syndrome.
- **Conclusion**: Established: LAMB2 is a basement-membrane laminin subunit with relevant adhesion and signaling functions and a disease-linked structural role. Hypothesis: together with LAMB1 and COL6A1, it may form the matrix backbone underlying the shared module. The module does not demonstrate a physical laminin complex, especially because hu.MAP provides no multi-member complex for this module.

#### ALB

- **Related proteins** (co-abundance neighbors): GSN (0.81); STRING partners: FN1 (0.998), LTF (0.996)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB is liver-enriched and hepatocyte-enriched in HPA and is secreted to blood. It is the most abundant protein in human blood according to the supplied annotation and functions in plasma colloid-osmotic regulation and molecular transport. Its STRING associations with FN1 and LTF are very strong, and it contributes to the endoplasmic-reticulum-lumen term (GO:CC endoplasmic reticulum lumen; q_global = 0.00382) and several supplementary secreted-protein annotations (STRING Keyword Secreted; within-query FDR = 8.88e-07), (STRING COMPARTMENTS External encapsulating structure; within-query FDR = 1.61e-05), (STRING Keyword Disulfide bond; within-query FDR = 0.00056), (STRING Keyword Glycoprotein; within-query FDR = 0.00067), (STRING COMPARTMENTS Extracellular region; within-query FDR = 0.00087), and (STRING RCTM Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs); within-query FDR = 0.0015). Its disease associations include congenital analbuminemia and chronic kidney disease.
- **Conclusion**: Established: ALB is a circulating liver-derived protein and a plausible marker of plasma contribution to the module. Hypothesis: ALB may explain part of the circulatory-system signal and may be co-abundant with matrix proteins because of blood exposure rather than shared tissue synthesis. Its presence should therefore be treated as a potential composition or sampling factor, not as proof that albumin is a structural component of the basement membrane.

## Module 5

**Tissue pair**: circulatory_system and prostate  
**Genes (35)**: ANK3, CCDC25, CDK5RAP3, CNPY3, COG1, EML4, FKBP15, GAK, GGCT, GMPPB, LACTB2, MECR, MESD, APOOL, NDUFA10, NDUFS1, NDUFS5, NIT2, NSF, POLR2B, RTCA, S100A13, SEC23IP, SEC24D, SCP2, SFXN3, SIRT5, SMARCC2, SUPT16H, SRRT, STK39, TAOK3, TBC1D15, ACAA1, ATP6V1C1

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established pathway-level enrichment; this does not invalidate the module. The clearest functional signal is a combination of mitochondrial respiratory-chain complex I biology, intracellular trafficking, vesicle transport, membrane organization, lipid and sterol metabolism, and gene-expression processes. The strongest internally coherent unit is the complex I trio NDUFS1, NDUFA10, and NDUFS5, supported by very high-confidence STRING links and repeated hu.MAP complex membership (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1). Additional coherent units include COPII and ER-to-Golgi transport involving SEC23IP and SEC24D, peroxisomal lipid metabolism involving ACAA1 and SCP2, and transcriptional or chromatin functions involving POLR2B and SUPT16H. Because the module also contains many genes connected only through ANK3 in the inferred network, it is better interpreted as a mixed cellular co-abundance program than as a single established biochemical pathway.

**Cell composition.** The module is not predominantly plasma or secreted: only a small minority of genes are secreted according to HPA, and most proteins are intracellular or membrane-associated. It is also not strongly blood-cell specific, because HPA reports low immune-cell specificity for nearly all genes, with only limited immune-cell enhancement. Most genes have low tissue specificity, while several show cell-type enhancement across diverse populations, including neutrophils, spermatogenic cells, epithelial cells, trophoblasts, hepatocytes, and neural cells. This breadth is more consistent with broadly expressed cellular machinery and mixed cell-composition effects than with a prostate-specific secretory program. Protein detection in prostate is widespread in the available HPA evidence, whereas matching circulatory-system tissue protein data are unavailable, so the shared signal could partly reflect common cellular constituents or general housekeeping biology in the sampled tissues. Liver-related enhancement among several metabolic genes and cell-type enhancement in neutrophils and reproductive cells should be treated as contextual clues rather than proof of a common cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

Known relationships are concentrated in a few compact groups. NDUFA10, NDUFS1, and NDUFS5 have mutually high-confidence STRING interactions and recur together in multiple hu.MAP complex models (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1) and (hu.MAP huMAP3_07653.1), strongly supporting their shared membership in mitochondrial complex I. SEC23IP and SEC24D have a STRING interaction and co-occur in several hu.MAP COPII or ER-trafficking complexes (hu.MAP huMAP3_00065.1), (hu.MAP huMAP3_07775.1) (hu.MAP huMAP3_09282.1) (hu.MAP huMAP3_07653.1) (hu.MAP huMAP3_11128.1) (hu.MAP huMAP3_13535.1). ACAA1 and SCP2 form a high-confidence STRING pair involved in peroxisomal fatty-acid metabolism, while POLR2B and SUPT16H form a high-confidence transcriptional or chromatin-related pair. Other module edges, especially the many links centered on ANK3, lack corresponding STRING partners or hu.MAP complexes in the fact sheet. Thus, the network contains genuine known molecular relationships but is not uniformly supported as one physical complex; co-abundance likely combines several cellular programs.

**STRING interactions (score >= 0.7)**: 6 of 595 gene pairs: ACAA1–SCP2 (0.982); NDUFA10–NDUFS1 (0.999); NDUFA10–NDUFS5 (0.999); NDUFS1–NDUFS5 (0.999); POLR2B–SUPT16H (0.988); SEC23IP–SEC24D (0.718)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02819.1 (NDUFS5, NDUFA10, NDUFS1; 3/34); huMAP3_14018.1 (NDUFS5, NDUFA10, NDUFS1; 3/48); huMAP3_06397.1 (NDUFS5, NDUFA10, NDUFS1; 3/49); huMAP3_09982.1 (NDUFS5, NDUFA10, NDUFS1; 3/49); huMAP3_09567.1 (NDUFS5, NDUFA10, NDUFS1; 3/52); huMAP3_14878.1 (NDUFS5, NDUFA10, NDUFS1; 3/53); huMAP3_00065.1 (SEC24D, SEC23IP; 2/4); huMAP3_08741.1 (RTCA, MESD; 2/5); huMAP3_07775.1 (SEC24D, SEC23IP; 2/5); huMAP3_09282.1 (SEC24D, SEC23IP; 2/6); huMAP3_07653.1 (NDUFA10, NDUFS1; 2/7); huMAP3_11128.1 (SEC24D, SEC23IP; 2/8); huMAP3_13535.1 (SEC24D, SEC23IP; 2/14); huMAP3_12394.1 (GAK, SEC24D; 2/98)

### Novelty

The module should not be called a wholly new biological discovery. Its principal substructures recapitulate established biology: the complex I trio is represented in STRING and hu.MAP, SEC23IP–SEC24D is represented in both resources, and the ACAA1–SCP2 and POLR2B–SUPT16H relationships are already represented in STRING. The potentially novel aspect is the co-abundance association of these distinct programs across circulatory_system and prostate, particularly the way they are connected in this tissue-pair module. However, database absence for many edges does not establish novelty, and the lack of globally significant GO/KEGG enrichment limits confidence in a unified new pathway. Replication in independent cohorts, preservation after cell-composition adjustment, and targeted validation of the cross-program links would be needed before claiming a novel conserved mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared cellular maintenance state in which mitochondrial respiratory capacity, ER-to-Golgi cargo handling, peroxisomal lipid processing, and transcriptional or membrane organization are coordinately regulated. In prostate and circulatory-system samples, this coordination could arise from broadly expressed housekeeping machinery or from recurring mixtures of epithelial, vascular, metabolic, and immune-related cells rather than from a single specialized pathway. ANK3 may act as a high-connectivity co-abundance hub linking otherwise distinct programs, but this is a network-level hypothesis and is not established by the available physical-interaction evidence. A testable prediction is that the module will track mitochondrial and secretory or membrane-trafficking state while weakening after adjustment for cell-type composition.

### Important genes

#### NDUFS1

- **Related proteins** (co-abundance neighbors): NDUFS5 (0.84); STRING partners: NDUFA10 (0.999), NDUFS5 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_02819.1, huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1, huMAP3_07653.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S1. The protein encoded by this gene belongs to the complex I 75 kDa subunit family. Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Thi…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 5 (0.810); mitochondrial complex I deficiency (0.647); type 2 diabetes mellitus (0.608); Parkinson disease (0.603); diabetes mellitus (0.580)
- **Europe PMC papers**: 2567
- **Why important**: NDUFS1 is the most informative complex I anchor among the module genes: it is the largest complex I subunit described in the fact sheet, has NADH dehydrogenase and oxidoreductase functions, and belongs to the mitochondrial electron-transfer and ATP-synthesis machinery. It is supported by STRING links to NDUFA10 and NDUFS5 and by repeated hu.MAP complex membership (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1), (hu.MAP huMAP3_07653.1). Its disease associations include nuclear complex I deficiency, Parkinson disease, and diabetes, and its literature support is substantial.
- **Conclusion**: Established evidence supports NDUFS1 as a central marker of the module's mitochondrial respiratory-chain component. It is plausible, but not established, that variation in NDUFS1 abundance helps explain the shared module across the two tissues.

#### NDUFA10

- **Related proteins** (co-abundance neighbors): SEC23IP (0.83), CDK5RAP3 (0.82), CNPY3 (0.82), ANK3 (0.81), NDUFS5 (0.80); STRING partners: NDUFS1 (0.999), NDUFS5 (0.999)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02819.1, huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1, huMAP3_07653.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit A10. The protein encoded by this gene is a component of 42 kDa complex I, the first enzyme complex in the electron transport chain of mitochondria. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. A mutation in this gene was found in an individual with Leigh syndrome. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.677); Leigh syndrome (0.674); mitochondrial complex I deficiency, nuclear type 22 (0.668); type 2 diabetes mellitus (0.620); diabetes mellitus (0.578)
- **Europe PMC papers**: 1163
- **Why important**: NDUFA10 provides an independent complex I anchor and connects the complex I trio to other module genes in the co-abundance network. It has very high-confidence STRING relationships with NDUFS1 and NDUFS5 and appears in repeated hu.MAP complex models (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1), (hu.MAP huMAP3_07653.1). Its annotated role in NADH-to-ubiquinone electron transfer and associations with complex I deficiency, Leigh syndrome, and diabetes make it biologically consequential.
- **Conclusion**: Established evidence supports NDUFA10 as a component of the module's complex I signal. The network connection to trafficking and ER-related genes is a co-abundance observation, not evidence that NDUFA10 physically links those systems.

#### NDUFS5

- **Related proteins** (co-abundance neighbors): NDUFS1 (0.84), CNPY3 (0.83), NIT2 (0.82), NDUFA10 (0.80); STRING partners: NDUFA10 (0.999), NDUFS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_02819.1, huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit S5. This gene is a member of the NADH dehydrogenase (ubiquinone) iron-sulfur protein family. The encoded protein is a subunit of the NADH:ubiquinone oxidoreductase (complex I), the first enzyme complex in the electron transport chain located in the inner mitochondrial membrane. Alternative splicing results in multiple transcript variants and pseudogenes have been identified on chromosomes 1, 4 and 17.…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.608); Parkinson disease (0.605); diabetes mellitus (0.578); neurodegenerative disease (0.576); Alzheimer disease (0.536)
- **Europe PMC papers**: 800
- **Why important**: NDUFS5 completes the most reproducible molecular substructure in the module. It is linked at high confidence to NDUFA10 and NDUFS1 in STRING and appears with them across multiple hu.MAP complex models (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1). Its annotations place it in complex I electron transport, respiratory-chain assembly, and mitochondrial ATP synthesis, while disease associations include complex I deficiency, Parkinson disease, and diabetes.
- **Conclusion**: Established evidence supports NDUFS5 as a reliable representative of the mitochondrial complex I component. Its co-abundance with the broader module may indicate coordinated cellular energy demand, but the fact sheet does not establish a tissue-specific causal role.

#### SEC23IP

- **Related proteins** (co-abundance neighbors): GAK (0.86), NDUFA10 (0.83); STRING partners: SEC24D (0.718)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_00065.1, huMAP3_07775.1, huMAP3_09282.1, huMAP3_11128.1, huMAP3_13535.1
- **Function (MyGene.info)**: SEC23 interacting protein. This gene encodes a member of the phosphatidic acid preferring-phospholipase A1 family. The encoded protein is localized to endoplasmic reticulum exit sites and plays a critical role in ER-Golgi transport as part of the multimeric coat protein II complex. An orthologous gene in frogs is required for normal neural crest cell development, suggesting that this gene may play a role in Waardenburg synd…
- **Diseases (Open Targets)**: Parkinson disease (0.409); type 2 diabetes mellitus (0.372); cardiomyopathy (0.326); diabetes mellitus (0.294); Genu valgum (0.269)
- **Europe PMC papers**: 265
- **Why important**: SEC23IP is a strategically important bridge gene because it has module links to GAK and NDUFA10 and a known STRING relationship with SEC24D. It is an ER-exit-site and COPII-associated protein involved in ER-to-Golgi transport, and it recurs with SEC24D in several hu.MAP complexes (hu.MAP huMAP3_00065.1), (hu.MAP huMAP3_07775.1) (hu.MAP huMAP3_09282.1) (hu.MAP huMAP3_07653.1) (hu.MAP huMAP3_11128.1) (hu.MAP huMAP3_13535.1). Its annotations include intracellular transport, Golgi organization, and spermatid development, with disease associations that include Parkinson disease, diabetes, and cardiomyopathy.
- **Conclusion**: Established evidence supports SEC23IP as a representative of the module's ER-to-Golgi trafficking component. Its network connection to the complex I signal is suggestive of coordinated cellular-state regulation, but a direct mechanistic bridge remains hypothetical.

#### ANK3

- **Related proteins** (co-abundance neighbors): MESD (0.94), NIT2 (0.87), NSF (0.86), TBC1D15 (0.86), CCDC25 (0.86), GAK (0.86), STK39 (0.86), SUPT16H (0.85), COG1 (0.85), ATP6V1C1 (0.84), GMPPB (0.83), GGCT (0.83), TAOK3 (0.82), SEC24D (0.81), SMARCC2 (0.81), SRRT (0.81), EML4 (0.81), ACAA1 (0.81), NDUFA10 (0.81), SFXN3 (0.80), POLR2B (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ankyrin 3. Ankyrins are a family of proteins that are believed to link the integral membrane proteins to the underlying spectrin-actin cytoskeleton and play key roles in activities such as cell motility, activation, proliferation, contact, and the maintenance of specialized membrane domains. Multiple isoforms of ankyrin with different affinities for various target proteins are expressed in a tissue-specific,…
- **Diseases (Open Targets)**: intellectual disability-hypotonia-spasticity-sleep disorder syndrome (0.726); bipolar disorder (0.536); hereditary disease (0.472); smoking initiation (0.411); smoking cessation (0.391)
- **Europe PMC papers**: 2941
- **Why important**: ANK3 has the strongest network position in the supplied module and connects to many otherwise weakly connected genes, including genes involved in membrane trafficking, stress signaling, cytoskeletal organization, transcription, and mitochondrial biology. Its annotated function is to link integral membrane proteins to the spectrin-actin cytoskeleton and organize specialized membrane domains. It is detected in prostate and has extensive literature support, with disease associations including intellectual disability, bipolar disorder, and sleep-related disease.
- **Conclusion**: Established evidence supports ANK3 as a membrane and cytoskeletal organizer with unusually high network centrality in this module. Its apparent role as a bridge among the module's functional groups is a network hypothesis rather than a demonstrated physical interaction, because the fact sheet reports no STRING partners or hu.MAP complex for ANK3.

## Module 6

**Tissue pair**: circulatory_system and prostate  
**Genes (24)**: APOB, APOE, APOH, ARRB1, BIN1, CALD1, C3, CSRP1, DUSP3, AHSG, ILK, ITGA5, ITGAV, ITIH2, LIMS1, LRP1, MYLK, PDLIM7, RRAS, RSU1, SLMAP, TPM1, THBS1, GC

### Function

The module is best interpreted as a vascular and extracellular-interface program linking blood-vessel development, cell–matrix adhesion, lipid handling, endocytosis, wound response, and contractile-cell behavior. The strongest primary evidence is the coherent enrichment for circulatory-system development (GO:BP circulatory system development; q_global = 1.98e-06), tube morphogenesis (GO:BP tube morphogenesis; q_global = 1.29e-05), blood-vessel morphogenesis and development (GO:BP blood vessel morphogenesis; q_global = 2.63e-05)(GO:BP blood vessel development; q_global = 4.51e-05), vasculature development (GO:BP vasculature development; q_global = 5.84e-05), wound healing and response to wounding (GO:BP wound healing; q_global = 0.000417)(GO:BP response to wounding; q_global = 0.00167), cell–substrate adhesion (GO:BP cell-substrate adhesion; q_global = 0.000812)(GO:BP cell-matrix adhesion; q_global = 0.00235), endocytosis (GO:BP endocytosis; q_global = 0.00274), integrin signaling (KEGG Integrin signaling - Homo sapiens (human); q_global = 0.00543), and focal adhesions (GO:CC focal adhesion; q_global = 0.0436). The lipid axis is also established by cholesterol metabolism (KEGG Cholesterol metabolism - Homo sapiens (human); q_global = 0.00423), lipid localization and transport (GO:BP lipid localization; q_global = 0.00625)(GO:BP lipid transport; q_global = 0.0389), lipoprotein particles (GO:CC plasma lipoprotein particle; q_global = 0.0238)(GO:CC lipoprotein particle; q_global = 0.0238), and cholesterol efflux (GO:BP cholesterol efflux; q_global = 0.0238). The combined pattern is more informative than any isolated annotation: it connects circulating lipoprotein and complement components with integrin-linked cytoskeletal and smooth-muscle machinery. STRING independently supports circulatory development, tube morphogenesis, blood-vessel morphogenesis, and cell-substrate adhesion (STRING Process Circulatory system development; within-query FDR = 1.88e-05)(STRING Process Tube morphogenesis; within-query FDR = 7.35e-05)(STRING Process Blood vessel morphogenesis; within-query FDR = 7.35e-05)(STRING Process Regulation of cell-substrate adhesion; within-query FDR = 0.00062).

**Cell composition.** The module is compositionally mixed rather than a uniform tissue-intrinsic program. A substantial secreted-to-blood and liver-enriched component includes APOB, APOE, APOH, AHSG, C3, GC, and ITIH2; this is consistent with plasma lipoprotein, complement, and acute extracellular-protein biology (GO:CC protein-lipid complex; q_global = 0.00217)(KEGG Cholesterol metabolism - Homo sapiens (human); q_global = 0.00423)(GO:CC chylomicron; q_global = 0.00805)(GO:CC blood microparticle; q_global = 0.0228)(GO:CC plasma lipoprotein particle; q_global = 0.0238)(STRING TISSUES Plasma cell; within-query FDR = 6.63e-05)(STRING NetworkNeighborAL Complement and coagulation cascades, and Protein-lipid complex; within-query FDR = 9.29e-05)(STRING Keyword Secreted; within-query FDR = 0.0005). HPA also identifies liver and hepatocyte enrichment for several members and reports secreted-to-blood localization for C3, GC, and ITIH2. A second component is enriched in smooth-muscle, vascular, platelet, and stromal cell contexts, including MYLK, TPM1, CALD1, PDLIM7, ILK, LIMS1, RSU1, and CSRP1; this agrees with contractile-fiber and myofibril terms (GO:CC myofibril; q_global = 0.00548)(GO:CC contractile muscle fiber; q_global = 0.00625)(GO:CC sarcomere; q_global = 0.0188). The frequent smooth-muscle and megakaryocyte associations, together with the blood microparticle term (GO:CC blood microparticle; q_global = 0.0228), mean that the shared signal may partly reflect blood-derived material, vascular or smooth-muscle cells, platelets, or other shared cell types in the samples rather than a prostate-specific mechanism. The HPA profile also includes broadly expressed genes and multiple immune-cell associations, so cellular mixture and circulating protein carryover should be considered. Prostate protein detection is present for some members but absent for many others, which further argues against treating the entire module as a uniformly prostate-resident program.

**GO/KEGG enrichment**: 73 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP circulatory system development | 1.98e-06 | APOB, APOE, APOH, C3, ILK, ITGA5, ITGAV, LRP1, MYLK, PDLIM7, RRAS, THBS1, TPM1 |
| GO:BP tube morphogenesis | 1.29e-05 | APOB, APOE, APOH, C3, ILK, ITGA5, ITGAV, LRP1, MYLK, RRAS, THBS1 |
| GO:BP blood vessel morphogenesis | 2.63e-05 | APOB, APOE, APOH, C3, ITGA5, ITGAV, LRP1, MYLK, RRAS, THBS1 |
| GO:BP blood vessel development | 4.51e-05 | APOB, APOE, APOH, C3, ITGA5, ITGAV, LRP1, MYLK, RRAS, THBS1 |
| GO:BP tube development | 5.81e-05 | APOB, APOE, APOH, C3, ILK, ITGA5, ITGAV, LRP1, MYLK, RRAS, THBS1 |
| GO:BP vasculature development | 5.84e-05 | APOB, APOE, APOH, C3, ITGA5, ITGAV, LRP1, MYLK, RRAS, THBS1 |
| GO:BP regulation of endocytosis | 0.000381 | AHSG, APOE, ARRB1, BIN1, C3, ITGAV, LRP1, MYLK |
| GO:BP wound healing | 0.000417 | APOE, APOH, CSRP1, ILK, ITGA5, ITGAV, MYLK, THBS1, TPM1 |
| GO:BP regulation of lipid localization | 0.000547 | APOB, APOE, C3, ITGAV, LRP1, THBS1 |
| GO:BP cell-substrate adhesion | 0.000812 | DUSP3, ILK, ITGA5, ITGAV, LIMS1, RRAS, RSU1, THBS1 |
| GO:BP apoptotic cell clearance | 0.000923 | C3, ITGAV, LRP1, THBS1 |
| GO:BP positive regulation of endocytosis | 0.000951 | AHSG, APOE, ARRB1, BIN1, C3, LRP1 |
| GO:BP negative regulation of cell migration | 0.00104 | APOE, APOH, DUSP3, LRP1, RRAS, THBS1, TPM1 |
| GO:BP negative regulation of cell motility | 0.00123 | APOE, APOH, DUSP3, LRP1, RRAS, THBS1, TPM1 |
| GO:BP negative regulation of locomotion | 0.00146 | APOE, APOH, DUSP3, LRP1, RRAS, THBS1, TPM1 |

### STRING and hu.MAP

STRING contains established high-confidence relationships in several coherent sub-networks. The plasma-protein branch links AHSG, APOB, APOH, APOE, C3, GC, and ITIH2, with particularly strong links among apolipoproteins, complement, and other secreted proteins. The receptor and matrix branch includes APOE–LRP1, LRP1–THBS1, ITGAV–THBS1, ITGA5–ITGAV, and ITGA5–ILK. The cytoskeletal branch includes ILK–LIMS1, ILK–RSU1, CALD1–MYLK, CALD1–TPM1, and MYLK–TPM1. These are known relationships, not evidence that the co-abundance edges themselves represent direct physical binding in the tissues. STRING functional enrichment supports the same vascular, plasma-membrane, secreted-protein, and adhesion themes (STRING Process Circulatory system development; within-query FDR = 1.88e-05)(STRING Component Cell periphery; within-query FDR = 2.11e-05)(STRING COMPARTMENTS Plasma membrane; within-query FDR = 0.00013)(STRING Keyword Secreted; within-query FDR = 0.0005)(STRING Process Regulation of cell-substrate adhesion; within-query FDR = 0.00062). hu.MAP provides additional support for two partially distinct assemblies: complexes containing C3, AHSG, GC, APOH, or ITIH2 within broad plasma and complement-associated complexes (hu.MAP huMAP3_15040.1)(hu.MAP huMAP3_10678.1)(hu.MAP huMAP3_09434.1)(hu.MAP huMAP3_08395.1)(hu.MAP huMAP3_09531.1)(hu.MAP huMAP3_10101.1), and repeated focal-adhesion assemblies containing LIMS1, ILK, and RSU1 (hu.MAP huMAP3_06647.1)(hu.MAP huMAP3_04827.1)(hu.MAP huMAP3_09385.1)(hu.MAP huMAP3_11194.1). CALD1–MYLK complexes are also represented (hu.MAP huMAP3_11074.1)(hu.MAP huMAP3_10673.1). Thus, the module integrates known extracellular plasma-protein associations with known intracellular adhesion and contractile assemblies, while the cross-branch co-abundance relationship remains biologically interpretable but not necessarily a single physical complex.

**STRING interactions (score >= 0.7)**: 27 of 276 gene pairs: AHSG–APOB (0.9); AHSG–APOH (0.957); AHSG–C3 (0.7); AHSG–GC (0.959); AHSG–ITIH2 (0.922); APOB–APOE (0.999); APOB–APOH (0.985); APOB–C3 (0.819); APOB–ITIH2 (0.788); APOE–APOH (0.921); APOE–BIN1 (0.908); APOE–C3 (0.732); APOE–LRP1 (0.999); APOH–GC (0.766); APOH–ITIH2 (0.867); C3–GC (0.768); CALD1–MYLK (0.832); CALD1–TPM1 (0.869); ILK–ITGA5 (0.973); ILK–LIMS1 (0.999); ILK–RSU1 (0.991); ITGA5–ITGAV (0.946); ITGA5–THBS1 (0.812); ITGAV–THBS1 (0.981); LIMS1–RSU1 (0.999); LRP1–THBS1 (0.958); MYLK–TPM1 (0.857)
**STRING functional enrichment (supplementary, within-query FDR)**: Process Circulatory system development (FDR = 1.88e-05, 11 genes); Component Cell periphery (FDR = 2.11e-05, 20 genes); TISSUES Plasma cell (FDR = 6.63e-05, 7 genes); Process Tube morphogenesis (FDR = 7.35e-05, 9 genes); Process Tube development (FDR = 7.35e-05, 10 genes); Process Blood vessel morphogenesis (FDR = 7.35e-05, 8 genes); NetworkNeighborAL Complement and coagulation cascades, and Protein-lipid complex (FDR = 9.29e-05, 6 genes); COMPARTMENTS Plasma membrane (FDR = 0.00013, 15 genes); Keyword Signal (FDR = 0.00013, 11 genes); Keyword Disulfide bond (FDR = 0.00015, 11 genes); Keyword Glycoprotein (FDR = 0.0002, 11 genes); Keyword Secreted (FDR = 0.0005, 8 genes); Process Regulation of cell-substrate adhesion (FDR = 0.00062, 7 genes); Process Negative regulation of cell migration (FDR = 0.00062, 7 genes); Process Regulation of developmental process (FDR = 0.00062, 14 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (C3, APOH, AHSG, GC, ITIH2; 5/64); huMAP3_10678.1 (C3, AHSG, GC, ITIH2; 4/71); huMAP3_06647.1 (LIMS1, ILK, RSU1; 3/6); huMAP3_04827.1 (LIMS1, ILK, RSU1; 3/7); huMAP3_09385.1 (LIMS1, ILK, RSU1; 3/8); huMAP3_11194.1 (LIMS1, ILK, RSU1; 3/10); huMAP3_09434.1 (C3, AHSG, GC; 3/33); huMAP3_08395.1 (C3, AHSG, ITIH2; 3/43); huMAP3_09531.1 (C3, AHSG, ITIH2; 3/47); huMAP3_10101.1 (C3, AHSG, ITIH2; 3/49); huMAP3_11074.1 (CALD1, MYLK; 2/6); huMAP3_02242.1 (C3, AHSG; 2/9); huMAP3_10673.1 (CALD1, MYLK; 2/14); huMAP3_07432.1 (C3, AHSG; 2/18); huMAP3_07265.1 (AHSG, ITIH2; 2/20); huMAP3_08224.1 (C3, GC; 2/21)

### Novelty

This should not be described as a newly discovered molecular pathway. The functions of the major genes, the lipoprotein and complement relationships, integrin-linked adhesion machinery, and contractile assemblies are already established by gene annotations, STRING, and hu.MAP. The potentially novel result is the reproducible co-abundance organization of these branches as one module shared by circulatory_system and prostate. That claim requires validation in independent cohorts, adjustment for plasma content and cell composition, and comparison with previously reported tissue co-expression modules. The presence of known STRING and hu.MAP relationships supports biological plausibility but does not establish novelty; conversely, the absence of hu.MAP or STRING support for some module pairs does not prove that those relationships are novel. The most defensible conclusion is therefore a potentially distinctive cross-tissue co-abundance configuration built from largely established biology.

**Hypothesis.** Hypothesis: the shared module reflects coupling between circulating lipid/complement cargo and vascular or smooth-muscle cell responses. Secreted lipoprotein and complement proteins may provide the extracellular signal or sample-level carrier component; LRP1 and integrin receptors may coordinate uptake, clearance, and matrix sensing; THBS1 and the ITGA5–ITGAV–ILK axis may transmit adhesion and remodeling signals; and MYLK, TPM1, CALD1, PDLIM7, LIMS1, and RSU1 may translate those signals into contractile and cytoskeletal behavior. This could link lipid localization, apoptotic-cell clearance, wound repair, endothelial or vascular morphogenesis, and smooth-muscle tone. The hypothesis predicts that the module will weaken after controlling for plasma protein abundance and shared vascular or platelet content, but that a residual adhesion–contractility signal may remain in vascular and stromal cells. This is a testable interpretation, not an established causal mechanism.

### Important genes

#### APOE

- **Related proteins** (co-abundance neighbors): ITIH2 (0.86); STRING partners: APOB (0.999), APOH (0.921), BIN1 (0.908), C3 (0.732), LRP1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein E. The protein encoded by this gene is a major apoprotein of the chylomicron. It binds to a specific liver and peripheral cell receptor, and is essential for the normal catabolism of triglyceride-rich lipoprotein constituents. This gene maps to chromosome 19 in a cluster with the related apolipoprotein C1 and C2 genes. Mutations in this gene result in familial dysbetalipoproteinemia, or type III hype…
- **Diseases (Open Targets)**: hyperlipoproteinemia type 3 (0.803); coronary artery disorder (0.782); lipoprotein glomerulopathy (0.759); Alzheimer disease (0.696); familial hypercholesterolemia (0.651)
- **Europe PMC papers**: 74272
- **Why important**: APOE is a central biological marker of the lipid branch: it participates in cholesterol metabolism, lipid transport, lipoprotein localization, endocytosis, and vascular-development terms (GO:BP circulatory system development; q_global = 1.98e-06)(GO:BP regulation of endocytosis; q_global = 0.000381)(GO:BP regulation of lipid localization; q_global = 0.000547)(KEGG Cholesterol metabolism - Homo sapiens (human); q_global = 0.00423)(GO:BP cholesterol efflux; q_global = 0.0238)(GO:BP lipid transport; q_global = 0.0389). It is connected in STRING to APOB, APOH, C3, BIN1, and LRP1, including strong links to the lipoprotein and clearance machinery. HPA places it in liver, adrenal, and brain contexts and as secreted to blood, while its disease associations include hyperlipoproteinemia, coronary artery disease, and Alzheimer disease. It has a very large literature, making it an important interpretive anchor rather than a novel marker.
- **Conclusion**: Established evidence: APOE supports a circulating lipid-transport and receptor-mediated-clearance interpretation of the module, with plausible vascular relevance. Hypothesis: APOE-containing particles may help couple the plasma branch to LRP1, integrin, and matrix responses in the shared tissues. The co-abundance data alone do not establish that APOE causally drives the adhesion or contractile branch.

#### LRP1

- **Related proteins** (co-abundance neighbors): GC (0.84), APOH (0.83); STRING partners: APOE (0.999), THBS1 (0.958)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LDL receptor related protein 1. This gene encodes a member of the low-density lipoprotein receptor family of proteins. The encoded preproprotein is proteolytically processed by furin to generate 515 kDa and 85 kDa subunits that form the mature receptor (PMID: 8546712). This receptor is involved in several cellular processes, including intracellular signaling, lipid homeostasis, and clearance of apoptotic cells. In addition, the …
- **Diseases (Open Targets)**: neurodegenerative disease (0.514); keratosis pilaris atrophicans (0.499); developmental dysplasia of the hip (0.466); Alzheimer disease (0.462); Parkinson disease (0.443)
- **Europe PMC papers**: 10645
- **Why important**: LRP1 provides a mechanistic bridge between extracellular cargo and cellular response. It is annotated for lipid homeostasis, receptor-mediated endocytosis, phagocytosis, and apoptotic-cell clearance (GO:BP regulation of endocytosis; q_global = 0.000381)(GO:BP apoptotic cell clearance; q_global = 0.000923)(GO:BP positive regulation of endocytosis; q_global = 0.000951)(GO:BP endocytosis; q_global = 0.00274), and it appears repeatedly in vascular-development, lipid-transport, adhesion, and focal-adhesion terms (GO:BP circulatory system development; q_global = 1.98e-06)(GO:BP artery morphogenesis; q_global = 0.00217)(KEGG Cholesterol metabolism - Homo sapiens (human); q_global = 0.00423)(GO:BP cholesterol efflux; q_global = 0.0238)(GO:CC focal adhesion; q_global = 0.0436). STRING links LRP1 strongly with APOE and THBS1. HPA places it at the plasma membrane and in adipocyte, fibroblast, hepatocyte, Kupffer-cell, and monocyte contexts. Its disease associations include neurodegenerative disease and inflammatory or tissue-clearance relevance, and it has a substantial literature.
- **Conclusion**: Established evidence: LRP1 is a credible interface between lipoprotein handling, endocytosis, apoptotic-cell clearance, and matrix signaling. Hypothesis: LRP1 could transmit the extracellular plasma-protein signal into vascular or stromal cells and thereby help explain the cross-branch module structure. Direct causal action in prostate or circulatory tissue is not demonstrated here.

#### ITGAV

- **Related proteins** (co-abundance neighbors): ITGA5 (0.87), SLMAP (0.85), BIN1 (0.82), ITIH2 (0.81); STRING partners: ITGA5 (0.946), THBS1 (0.981)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha V. The product of this gene belongs to the integrin alpha chain family. Integrins are heterodimeric integral membrane proteins composed of an alpha subunit and a beta subunit that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha V subunit. This subunit associates with beta 1, beta 3, beta…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); myocardial infarction (0.396); angina pectoris (0.371); Recurrent thrombophlebitis (0.370); intermediate coronary syndrome (0.370)
- **Europe PMC papers**: 5475
- **Why important**: ITGAV is a key adhesion and vascular-interface gene. It is included in the globally significant terms for vessel development, wound response, cell-substrate adhesion, endocytosis, cell migration, phagocytosis, and integrin signaling (GO:BP circulatory system development; q_global = 1.98e-06)(GO:BP wound healing; q_global = 0.000417)(GO:BP cell-substrate adhesion; q_global = 0.000812)(GO:BP apoptotic cell clearance; q_global = 0.000923)(KEGG Integrin signaling - Homo sapiens (human); q_global = 0.00543)(GO:BP phagocytosis; q_global = 0.0228). STRING supports its relationships with ITGA5 and THBS1. HPA places it at focal-adhesion sites and in relevant epithelial or podocyte contexts, and it is detected in prostate tissue. Its disease associations include myocardial infarction and thrombotic vascular disease. Its literature is extensive, particularly for integrin signaling and angiogenesis.
- **Conclusion**: Established evidence: ITGAV represents the cell-surface adhesion and vascular-remodeling arm of the module and is supported by both enrichment and known STRING relationships. Hypothesis: ITGAV may be the principal receptor-side mediator through which THBS1 and circulating extracellular proteins influence migration, clearance, or remodeling. The module does not identify the specific beta-integrin partner or prove ligand-dependent signaling in either tissue.

#### ILK

- **Related proteins** (co-abundance neighbors): LIMS1 (0.89), DUSP3 (0.86), RSU1 (0.82), MYLK (0.81), PDLIM7 (0.81), CALD1 (0.81), THBS1 (0.81); STRING partners: ITGA5 (0.973), LIMS1 (0.999), RSU1 (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_06647.1, huMAP3_04827.1, huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: integrin linked kinase. This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastas…
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); familial hypertrophic cardiomyopathy (0.194); Abnormality of the cardiovascular system (0.148); Prolonged QT interval (0.118); neoplasm (0.118)
- **Europe PMC papers**: 8401
- **Why important**: ILK is a high-connectivity intracellular organizer linking integrin signaling to focal adhesions, cell-matrix adhesion, migration, morphogenesis, and contractile structures (GO:BP circulatory system development; q_global = 1.98e-06)(GO:BP tube morphogenesis; q_global = 1.29e-05)(GO:BP cell-substrate adhesion; q_global = 0.000812)(GO:BP cell-matrix adhesion; q_global = 0.00235)(KEGG Integrin signaling - Homo sapiens (human); q_global = 0.00543)(GO:BP cell adhesion; q_global = 0.0219)(GO:CC focal adhesion; q_global = 0.0436). It has strong STRING relationships with ITGA5, LIMS1, and RSU1, and the LIMS1–ILK–RSU1 triad is repeatedly represented in hu.MAP complexes (hu.MAP huMAP3_06647.1)(hu.MAP huMAP3_04827.1)(hu.MAP huMAP3_09385.1)(hu.MAP huMAP3_11194.1). HPA places ILK at focal-adhesion sites and in megakaryocyte, platelet, and smooth-muscle contexts, with prostate protein detection. Its disease associations include neoplasm and cardiovascular abnormalities, and it has a large literature.
- **Conclusion**: Established evidence: ILK is a well-supported intracellular hub for the module's integrin, adhesion, and cytoskeletal interpretation. Hypothesis: ILK may couple extracellular THBS1 or integrin engagement to the contractile and migration program. Because ILK is a scaffold-like signaling component and the data are co-abundance data, the module does not demonstrate ILK enzymatic activity or direction of signaling.

#### MYLK

- **Related proteins** (co-abundance neighbors): RSU1 (0.88), SLMAP (0.86), TPM1 (0.85), LIMS1 (0.83), PDLIM7 (0.83), CALD1 (0.82), ILK (0.81), CSRP1 (0.81); STRING partners: CALD1 (0.832), TPM1 (0.857)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11074.1, huMAP3_10673.1
- **Function (MyGene.info)**: myosin light chain kinase. This gene, a muscle member of the immunoglobulin gene superfamily, encodes myosin light chain kinase which is a calcium/calmodulin dependent enzyme. This kinase phosphorylates myosin regulatory light chains to facilitate myosin interaction with actin filaments to produce contractile activity. This gene encodes both smooth muscle and nonmuscle isoforms. In addition, using a separate promoter in an …
- **Diseases (Open Targets)**: aortic aneurysm, familial thoracic 7 (0.767); familial thoracic aortic aneurysm and aortic dissection (0.710); megacystis-microcolon-intestinal hypoperistalsis syndrome 1 (0.617); megacystis-microcolon-intestinal hypoperistalsis syndrome (0.597); Rare genetic vascular disease (0.483)
- **Europe PMC papers**: 10503
- **Why important**: MYLK represents the contractile effector arm and is among the most connected module genes. It is present in the globally significant vascular-development, tube-morphogenesis, wound-response, migration, endocytosis, and focal-adhesion terms (GO:BP circulatory system development; q_global = 1.98e-06)(GO:BP tube morphogenesis; q_global = 1.29e-05)(GO:BP wound healing; q_global = 0.000417)(GO:BP artery morphogenesis; q_global = 0.00217)(GO:BP endocytosis; q_global = 0.00274)(GO:BP cell migration; q_global = 0.0148)(GO:CC focal adhesion; q_global = 0.0436). STRING links it to CALD1 and TPM1, while hu.MAP contains CALD1–MYLK assemblies (hu.MAP huMAP3_11074.1)(hu.MAP huMAP3_10673.1). HPA shows enrichment in smooth muscle and seminal vesicle contexts and association with peritubular myoid cells, hepatic stellate cells, megakaryocytes, platelets, basophils, and neutrophils. Its disease associations include familial aortic aneurysm and dissection, and it has a very large literature.
- **Conclusion**: Established evidence: MYLK supports a smooth-muscle and actomyosin interpretation of the vascular and adhesion signal. Hypothesis: MYLK-dependent contractility may be the downstream cellular output of integrin and matrix engagement in the shared module. The present data do not establish phosphorylation, calcium activation, or a tissue-specific MYLK isoform.

#### C3

- **Related proteins** (co-abundance neighbors): PDLIM7 (0.82); STRING partners: AHSG (0.7), APOB (0.819), APOE (0.732), GC (0.768)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_02242.1, huMAP3_07432.1, huMAP3_08224.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is the principal complement representative and connects inflammatory extracellular biology with lipid and clearance signals. It is included in globally significant terms for vascular development, endocytosis, apoptotic-cell clearance, phagocytosis, lipid metabolism, and integrin signaling (GO:BP circulatory system development; q_global = 1.98e-06)(GO:BP regulation of endocytosis; q_global = 0.000381)(GO:BP apoptotic cell clearance; q_global = 0.000923)(GO:BP endocytosis; q_global = 0.00274)(KEGG Cholesterol metabolism - Homo sapiens (human); q_global = 0.00423)(KEGG Integrin signaling - Homo sapiens (human); q_global = 0.00543)(GO:BP phagocytosis; q_global = 0.0228). STRING links it with AHSG, APOB, APOE, and GC, and hu.MAP repeatedly places it in plasma and complement-associated complexes (hu.MAP huMAP3_15040.1)(hu.MAP huMAP3_10678.1)(hu.MAP huMAP3_09434.1)(hu.MAP huMAP3_08395.1)(hu.MAP huMAP3_09531.1)(hu.MAP huMAP3_10101.1). HPA identifies liver enrichment, secretion to blood, and an association with non-classical monocytes. Its disease associations include complement deficiency, atypical hemolytic-uremic syndrome, and complement-mediated kidney disease, and it has a very large literature.
- **Conclusion**: Established evidence: C3 supports a blood-borne complement and apoptotic-clearance component that is integrated with lipoprotein and adhesion annotations. Hypothesis: complement activation or complement-bearing particles may modulate integrin-dependent vascular remodeling and contractility. The module does not show complement activation state, cleavage products, or causal inflammation.

## Module 7

**Tissue pair**: circulatory_system and prostate  
**Genes (15)**: CACYBP, SHMT2, HMGCS1, HMGB3, MCM2, MCM5, MCM6, MCM7, PCNA, GART, PFAS, PAICS, PUS7, SMC2, TFRC

### Function

The module is best interpreted as a proliferative nuclear DNA-replication and genome-maintenance program. The strongest primary evidence is the coordinated presence of MCM2, MCM5, MCM6 and MCM7 in the MCM, CMG and DNA-replication-initiation annotations (6 globally significant GO/KEGG terms, q_global 5.14e-05–0.000185; see the table), (GO:BP DNA replication initiation; q_global = 0.000436), (6 globally significant GO/KEGG terms, q_global 0.00229–0.00907; see the table), (GO:MF DNA helicase activity; q_global = 0.0278) (GO:BP DNA replication; q_global = 0.0351) (KEGG Homologous recombination - Homo sapiens (human); q_global = 0.0394). PCNA extends this signal to DNA polymerase processivity, replication regulation and cell-cycle DNA replication (KEGG DNA replication - Homo sapiens (human); q_global = 0.000195) (GO:CC nuclear chromosome; q_global = 0.000246) (GO:BP regulation of DNA replication; q_global = 0.000283), (KEGG Cell cycle - Homo sapiens (human); q_global = 0.00122) (GO:BP DNA-templated DNA replication; q_global = 0.00194) (GO:CC protein-DNA complex; q_global = 0.00194), (GO:BP nuclear DNA replication; q_global = 0.0151), (GO:BP cell cycle DNA replication; q_global = 0.026), (GO:BP DNA replication; q_global = 0.0351). SMC2 and HMGB3 add chromosome, DNA-binding and recombination-related context (GO:CC nuclear chromosome; q_global = 0.000246), (GO:MF single-stranded DNA binding; q_global = 0.000553), (GO:BP DNA recombination; q_global = 0.00228), (GO:BP DNA metabolic process; q_global = 0.0496). A secondary metabolic component is represented by GART, PAICS and PFAS, which support de novo purine biosynthesis (GO:BP 'de novo' IMP biosynthetic process; q_global = 0.026), (4 globally significant GO/KEGG terms, q_global 0.0399–0.0399; see the table). Thus, the most defensible interpretation is a replication-competent, cell-cycle-associated module with linked nucleotide-supply activity, rather than a single narrowly defined pathway.

**Cell composition.** This is not primarily a plasma or secreted-protein module. Most members are intracellular nuclear or cytosolic proteins, and only TFRC is annotated as secreted to blood. The HPA profile nevertheless indicates a strong cellular-composition signal: many genes are enhanced in bone marrow, lymphoid tissue or liver, and all annotated genes show cell-type enhancement, especially in erythrocyte progenitors, megakaryocyte-related populations, trophoblasts and monocyte progenitors. Most genes have low immune-cell specificity, so the pattern is not specific to mature immune cells. The shared circulatory_system–prostate signal may therefore reflect proliferating or progenitor-like cells present in blood-associated material and prostate samples, or a shared cell-cycle state, rather than a prostate-specific secreted program. Protein detection in prostate for nearly all members is compatible with local expression, but does not by itself establish that the co-abundance relationship originates from prostate epithelial cells.

**GO/KEGG enrichment**: 35 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP double-strand break repair via break-induced replication | 5.14e-05 | MCM2, MCM5, MCM6, MCM7 |
| GO:CC DNA replication preinitiation complex | 5.14e-05 | MCM2, MCM5, MCM6, MCM7 |
| GO:CC MCM complex | 5.14e-05 | MCM2, MCM5, MCM6, MCM7 |
| GO:CC CMG complex | 5.14e-05 | MCM2, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication initiation | 0.000185 | MCM2, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication | 0.000185 | MCM2, MCM5, MCM6, MCM7 |
| KEGG DNA replication - Homo sapiens (human) | 0.000195 | MCM2, MCM5, MCM6, MCM7, PCNA |
| GO:CC nuclear chromosome | 0.000246 | MCM2, MCM5, MCM6, MCM7, PCNA, SMC2 |
| GO:BP regulation of DNA replication | 0.000283 | MCM2, MCM5, MCM6, MCM7, PCNA |
| GO:BP DNA replication initiation | 0.000436 | MCM2, MCM5, MCM6, MCM7 |
| GO:MF single-stranded DNA binding | 0.000553 | MCM2, MCM5, MCM6, MCM7, SMC2 |
| KEGG Cell cycle - Homo sapiens (human) | 0.00122 | MCM2, MCM5, MCM6, MCM7, PCNA |
| GO:BP DNA-templated DNA replication | 0.00194 | MCM2, MCM5, MCM6, MCM7, PCNA |
| GO:CC protein-DNA complex | 0.00194 | MCM2, MCM5, MCM6, MCM7, PCNA |
| GO:BP DNA recombination | 0.00228 | HMGB3, MCM2, MCM5, MCM6, MCM7, TFRC |

### STRING and hu.MAP

STRING provides strong, biologically coherent support for the MCM subnetwork: MCM2, MCM5, MCM6 and MCM7 are densely interconnected, and each also connects to PCNA; SMC2 has weaker links to several MCM proteins. The STRING functional results independently recover DNA replication, cell-cycle control, MCM and CMG annotations (15 supplementary STRING terms; within-query FDR 1.54e-05–0.00032), but these are supplementary within-query results and are not treated as global enrichment evidence. hu.MAP directly supports the same interpretation. Multiple complexes contain MCM2, MCM5, MCM6 and MCM7 together, with additional expected replication-fork, GINS and CMG-associated proteins outside the module (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1), (hu.MAP huMAP3_09860.1), (hu.MAP huMAP3_00154.1), (hu.MAP huMAP3_09238.1). hu.MAP also supports a smaller purine-associated grouping containing GART and PFAS (hu.MAP huMAP3_03291.1), (hu.MAP huMAP3_00676.1). The agreement between co-abundance structure, STRING relationships and hu.MAP complexes indicates that the central MCM signal is largely a recovery of known molecular machinery. The weaker links joining the replication group to purine enzymes, metabolic genes and TFRC may represent coordinated proliferation, nucleotide demand and iron acquisition rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 18 of 105 gene pairs: GART–PAICS (0.999); GART–PFAS (0.999); GART–SHMT2 (0.999); MCM2–MCM5 (0.999); MCM2–MCM6 (0.999); MCM2–MCM7 (0.999); MCM2–PCNA (0.939); MCM5–MCM6 (0.999); MCM5–MCM7 (0.999); MCM5–PCNA (0.918); MCM5–SMC2 (0.754); MCM6–MCM7 (0.999); MCM6–PCNA (0.912); MCM6–SMC2 (0.75); MCM7–PCNA (0.985); MCM7–SMC2 (0.7); PAICS–PFAS (0.821); PAICS–SHMT2 (0.843)
**STRING functional enrichment (supplementary, within-query FDR)**: WikiPathways G1 to S cell cycle control (FDR = 1.54e-05, 5 genes); WikiPathways DNA replication (FDR = 2.87e-05, 5 genes); KEGG DNA replication (FDR = 6.48e-05, 5 genes); WikiPathways Cell cycle (FDR = 9.61e-05, 5 genes); NetworkNeighborAL DNA replication, and Regulation of DNA-directed DNA polymerase activity (FDR = 9.67e-05, 5 genes); KEGG Cell cycle (FDR = 0.0001, 5 genes); RCTM DNA strand elongation (FDR = 0.00014, 5 genes); Component Nuclear chromosome (FDR = 0.00016, 6 genes); Component MCM complex (FDR = 0.00016, 4 genes); Component CMG complex (FDR = 0.00016, 4 genes); Component protein-DNA complex (FDR = 0.00019, 5 genes); RCTM Unwinding of DNA (FDR = 0.00023, 4 genes); NetworkNeighborAL Activation of the pre-replicative complex, and GINS complex (FDR = 0.00025, 4 genes); COMPARTMENTS Nuclear chromosome (FDR = 0.00032, 6 genes); COMPARTMENTS protein-DNA complex (FDR = 0.00032, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05529.1 (MCM5, MCM7, MCM2, MCM6; 4/6); huMAP3_14758.1 (MCM5, MCM7, MCM2, MCM6; 4/14); huMAP3_08554.1 (MCM5, MCM7, MCM2, MCM6; 4/15); huMAP3_11832.1 (MCM5, MCM7, MCM2, MCM6; 4/15); huMAP3_12180.1 (MCM5, MCM7, MCM2, MCM6; 4/17); huMAP3_06061.1 (MCM7, MCM2, MCM6; 3/5); huMAP3_07113.1 (MCM7, MCM2, MCM6; 3/6); huMAP3_11119.1 (MCM5, MCM7, MCM6; 3/14); huMAP3_03291.1 (PFAS, GART; 2/3); huMAP3_09860.1 (MCM2, MCM6; 2/4); huMAP3_00676.1 (PFAS, GART; 2/4); huMAP3_00154.1 (MCM2, MCM6; 2/5); huMAP3_09238.1 (MCM5, MCM7; 2/11); huMAP3_09466.1 (MCM2, MCM6; 2/23); huMAP3_10862.1 (MCM2, MCM6; 2/33); huMAP3_14306.1 (MCM2, MCM6; 2/55)

### Novelty

The module should not be described as a newly discovered DNA-replication complex. Its central relationships are already established by STRING and hu.MAP, and the functions of the MCM proteins and PCNA are well documented in the supplied literature and annotation evidence. A potentially novel aspect could be the reproducible co-abundance of this known replication machinery with purine-biosynthesis genes, TFRC and selected tissue or progenitor-cell signals across circulatory_system and prostate. However, the fact sheet does not provide an external comparison against prior tissue-pair modules, published co-abundance studies or independent replication cohorts. Therefore, the appropriate conclusion is that the molecular components are established, while the tissue-pair co-abundance configuration is a candidate observation requiring independent validation before it can be called a new finding. Absence of a STRING or hu.MAP entry for peripheral genes such as CACYBP, SHMT2 or HMGB3 would not by itself establish novelty.

**Hypothesis.** Hypothesis: the shared module reflects a proliferative progenitor or cycling-cell state in which the MCM helicase machinery licenses and supports replication, PCNA supports DNA synthesis and repair, SMC2 helps organize replicated chromosomes, and purine-biosynthesis enzymes supply nucleotide precursors. TFRC may contribute iron uptake required by proliferating cells, while HMGB3 and CACYBP may modulate chromatin or protein-turnover context. The circulatory_system association may arise partly from blood-associated progenitor cells or other proliferating cell populations, whereas the prostate association may reflect proliferating basal, stromal or tumor-related cells; the supplied data do not identify the responsible cell population. This model predicts that the module should track cell-cycle activity, replication stress, nucleotide demand and progenitor-cell abundance more strongly than a tissue-specific secretory function.

### Important genes

#### MCM6

- **Related proteins** (co-abundance neighbors): MCM7 (0.94), MCM5 (0.91), PCNA (0.87), SMC2 (0.84), TFRC (0.83), PAICS (0.80); STRING partners: MCM2 (0.999), MCM5 (0.999), MCM7 (0.999), PCNA (0.912), SMC2 (0.75)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 6. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: lactose intolerance (0.246); neurodegenerative disease (0.225); obesity disorder (0.166); nervous system disorder (0.141); systemic lupus erythematosus (0.140)
- **Europe PMC papers**: 3766
- **Why important**: MCM6 is a central network member with strong links to MCM2, MCM5, MCM7, PCNA, SMC2 and TFRC. It is present across the core MCM, CMG, DNA-replication, helicase and homologous-recombination evidence (30 globally significant GO/KEGG terms, q_global 5.14e-05–0.0394; see the table), (GO:BP DNA metabolic process; q_global = 0.0496). Its HPA profile is enhanced in lymphoid tissue and in erythroid, megakaryocyte and monocyte progenitor populations. MyGene.info describes it as an essential component of the pre-replication complex and replication-fork formation. It also appears in many hu.MAP complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1), (hu.MAP huMAP3_09860.1), (hu.MAP huMAP3_00154.1), (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1), giving it unusually strong complex-level support.
- **Conclusion**: Established conclusion: MCM6 is a core replication-initiation component and one of the strongest anchors of the module. Hypothesis: its association with TFRC and progenitor-enriched HPA profiles may mark cells with high replication and iron requirements, but this cannot be inferred as a direct MCM6–TFRC mechanism from the current data.

#### MCM5

- **Related proteins** (co-abundance neighbors): MCM6 (0.91), MCM7 (0.88), SMC2 (0.87), MCM2 (0.83), TFRC (0.83), PCNA (0.82), CACYBP (0.81); STRING partners: MCM2 (0.999), MCM6 (0.999), MCM7 (0.999), PCNA (0.918), SMC2 (0.754)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 5. The protein encoded by this gene is structurally very similar to the CDC46 protein from S. cerevisiae, a protein involved in the initiation of DNA replication. The encoded protein is a member of the MCM family of chromatin-binding proteins and can interact with at least two other members of this family. The encoded protein is upregulated in the transition from the G0 to G1/S phase of the cell cycl…
- **Diseases (Open Targets)**: Meier-Gorlin syndrome (0.563); neurodegenerative disease (0.397); lysosomal storage disease (0.362); kidney transplant (0.198); diabetic ketoacidosis (0.129)
- **Europe PMC papers**: 4143
- **Why important**: MCM5 has the strongest network connectivity in the supplied module and links the MCM core to SMC2, TFRC, PCNA and CACYBP. It participates in virtually all primary replication, helicase, chromosome and repair annotations listed for the module (21 globally significant GO/KEGG terms, q_global 5.14e-05–0.00907; see the table), (GO:CC chromosome, telomeric region; q_global = 0.0162) (GO:MF catalytic activity, acting on DNA; q_global = 0.0162) (GO:BP regulation of DNA metabolic process; q_global = 0.0251), (GO:MF DNA helicase activity; q_global = 0.0278) (GO:BP DNA replication; q_global = 0.0351) (KEGG Homologous recombination - Homo sapiens (human); q_global = 0.0394), (GO:BP DNA metabolic process; q_global = 0.0496), as well as all listed STRING functional terms (15 supplementary STRING terms; within-query FDR 1.54e-05–0.00032). It is supported by numerous hu.MAP replication complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1), (hu.MAP huMAP3_11119.1), (hu.MAP huMAP3_09238.1). Its HPA expression is enhanced in bone marrow and several progenitor populations, including erythrocyte and megakaryocyte progenitors. The supplied literature volume is substantial, consistent with an established replication role.
- **Conclusion**: Established conclusion: MCM5 is a network and annotation hub representing the canonical MCM replication machinery. Hypothesis: its peripheral links could help connect replication state to chromosome organization or protein turnover, but those links should not be interpreted as demonstrated physical or causal interactions beyond the reported evidence.

#### MCM7

- **Related proteins** (co-abundance neighbors): MCM6 (0.94), MCM5 (0.88), PCNA (0.84), SMC2 (0.83), TFRC (0.83), MCM2 (0.82); STRING partners: MCM2 (0.999), MCM5 (0.999), MCM6 (0.999), PCNA (0.985), SMC2 (0.7)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 is tightly connected to MCM2, MCM5, MCM6, PCNA, SMC2 and TFRC and is repeatedly recovered in the primary DNA-replication and helicase terms (21 globally significant GO/KEGG terms, q_global 5.14e-05–0.00907; see the table), (GO:CC chromosome, telomeric region; q_global = 0.0162) (GO:MF catalytic activity, acting on DNA; q_global = 0.0162) (GO:BP regulation of DNA metabolic process; q_global = 0.0251), (GO:MF DNA helicase activity; q_global = 0.0278) (GO:BP DNA replication; q_global = 0.0351) (KEGG Homologous recombination - Homo sapiens (human); q_global = 0.0394), (GO:BP DNA metabolic process; q_global = 0.0496). STRING supports highly coherent relationships with the other MCM proteins and PCNA, while hu.MAP places MCM7 in multiple MCM and replication-fork complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1), (hu.MAP huMAP3_09238.1). HPA shows bone-marrow enhancement and enrichment in erythroid, megakaryocyte and trophoblast-related cell types. Its supplied disease associations include several developmental and replication-related disorders, and its literature volume is substantial.
- **Conclusion**: Established conclusion: MCM7 is a core helicase-complex member and a reliable marker of the module's replication function. Hypothesis: the shared tissue signal may reflect coordinated activation of MCM7-containing replication machinery in progenitor-like or cycling cells, but tissue composition and cell-cycle state remain alternative explanations.

#### PCNA

- **Related proteins** (co-abundance neighbors): MCM6 (0.87), MCM7 (0.84), HMGB3 (0.84), MCM5 (0.82), SHMT2 (0.82); STRING partners: MCM2 (0.939), MCM5 (0.918), MCM6 (0.912), MCM7 (0.985)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proliferating cell nuclear antigen. The protein encoded by this gene is found in the nucleus and is a cofactor of DNA polymerase delta. The encoded protein acts as a homotrimer and helps increase the processivity of leading strand synthesis during DNA replication. In response to DNA damage, this protein is ubiquitinated and is involved in the RAD6-dependent DNA repair pathway. Two transcript variants encoding the same protein have b…
- **Diseases (Open Targets)**: ataxia-telangiectasia-like disorder (0.497); neurodegenerative disease (0.188); neoplasm (0.118); diabetes mellitus (0.116); hepatocellular carcinoma (0.113)
- **Europe PMC papers**: 61820
- **Why important**: PCNA connects the MCM core to HMGB3 and SHMT2 and is included in the primary DNA-replication, cell-cycle, protein-DNA-complex and DNA-metabolism annotations (KEGG DNA replication - Homo sapiens (human); q_global = 0.000195) (GO:CC nuclear chromosome; q_global = 0.000246) (GO:BP regulation of DNA replication; q_global = 0.000283), (KEGG Cell cycle - Homo sapiens (human); q_global = 0.00122) (GO:BP DNA-templated DNA replication; q_global = 0.00194) (GO:CC protein-DNA complex; q_global = 0.00194), (4 globally significant GO/KEGG terms, q_global 0.0151–0.0251; see the table), (GO:BP cell cycle DNA replication; q_global = 0.026), (GO:BP DNA replication; q_global = 0.0351), (GO:BP DNA metabolic process; q_global = 0.0496). STRING supports its relationships with MCM2, MCM5, MCM6 and MCM7 (8 supplementary STRING terms; within-query FDR 1.54e-05–0.00016), (STRING Component protein-DNA complex; within-query FDR = 0.00019), (STRING COMPARTMENTS Nuclear chromosome; within-query FDR = 0.00032), (STRING COMPARTMENTS protein-DNA complex; within-query FDR = 0.00032). Its established function as a DNA-polymerase-delta processivity factor and participant in DNA-damage repair makes it a functional bridge between replication and genome maintenance. It is enhanced in bone marrow and several proliferative progenitor or germ-cell populations, is detected in prostate, and has the largest supplied literature volume among the selected genes.
- **Conclusion**: Established conclusion: PCNA is the strongest bridge between replication initiation and DNA synthesis or repair in this module. Hypothesis: its connection to SHMT2 could reflect coupling between DNA synthesis and one-carbon or glycine metabolism, but the module data do not establish a direct metabolic mechanism.

#### GART

- **Related proteins** (co-abundance neighbors): CACYBP (0.84), PFAS (0.82), PUS7 (0.80); STRING partners: PAICS (0.999), PFAS (0.999), SHMT2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_03291.1, huMAP3_00676.1
- **Function (MyGene.info)**: phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase. The protein encoded by this gene is a trifunctional polypeptide. It has phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase activity which is required for de novo purine biosynthesis. This enzyme is highly conserved in vertebrates. Alternative splicing of this gene results in two transcript variants encoding different isoforms.…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.606); mesothelioma (0.584); malignant pleural mesothelioma (0.557); adenocarcinoma (0.486); anaplastic lung carcinoma (0.462)
- **Europe PMC papers**: 1890
- **Why important**: GART marks the module's distinct purine-biosynthesis arm and is connected to PAICS, PFAS, SHMT2, CACYBP and PUS7. It is represented in the globally significant de novo IMP, AMP and XMP biosynthesis terms (GO:BP 'de novo' IMP biosynthetic process; q_global = 0.026), (4 globally significant GO/KEGG terms, q_global 0.0399–0.0399; see the table). STRING strongly supports its relationships with PAICS, PFAS and SHMT2, and hu.MAP supports complexes containing GART and PFAS (hu.MAP huMAP3_03291.1), (hu.MAP huMAP3_00676.1). Its HPA profile is broadly expressed with enhancement in cardiomyocytes and epicardial cells, and it is detected in prostate. Its established enzymatic role supplies several steps of de novo purine synthesis, while its disease associations include multiple malignancies.
- **Conclusion**: Established conclusion: GART is the clearest marker that the module includes nucleotide-supply metabolism in addition to replication machinery. Hypothesis: GART may be co-abundant because proliferating cells require increased purine production to sustain DNA replication; this is biologically plausible but not proven as a causal relationship here.

#### TFRC

- **Related proteins** (co-abundance neighbors): MCM7 (0.83), MCM5 (0.83), MCM6 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes, Lysosomes; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transferrin receptor. This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: TFRC-related combined immunodeficiency (0.623); type 2 diabetes mellitus (0.518); mucopolysaccharidosis type 2 (0.490); diabetes mellitus (0.471); diabetic retinopathy (0.343)
- **Europe PMC papers**: 14164
- **Why important**: TFRC is a peripheral but biologically informative module member, linking to MCM5, MCM6 and MCM7. It appears in the globally significant DNA-recombination and DNA-metabolism annotations (GO:BP DNA recombination; q_global = 0.00228), (GO:BP regulation of DNA metabolic process; q_global = 0.0251), (GO:BP DNA metabolic process; q_global = 0.0496), although it is not supported by the listed STRING interactions or STRING functional terms. HPA identifies it as secreted to blood, enhanced in erythrocyte progenitors, macrophages, monocytes and syncytiotrophoblasts, and immune-cell enhanced for a non-classical monocyte population. Its established function is receptor-mediated iron uptake, with a direct role in erythropoiesis and associations with immunodeficiency and metabolic disease.
- **Conclusion**: Established conclusion: TFRC is a plausible indicator of blood-associated or progenitor-cell composition and cellular iron demand, rather than a demonstrated member of the MCM physical complex. Hypothesis: TFRC may connect iron availability to replication capacity in the shared samples, but the observed co-abundance could instead be driven by cell-type mixture.

## Module 8

**Tissue pair**: circulatory_system and prostate  
**Genes (16)**: DAZAP1, DHX9, EIF3C, EIF3L, LMNB1, PHB1, UPF1, RPL12, RPL3, AARS1, FARSB, MARS1, ALYREF, TMEM70, SNRNP200, EFTUD2

### Function

This module is best interpreted as a conserved RNA-processing and protein-biosynthesis module. The strongest primary evidence is enrichment for ribonucleoprotein complex (GO:CC ribonucleoprotein complex; q_global = 0.000231), nucleic-acid binding (GO:MF nucleic acid binding; q_global = 0.00108), RNA binding (GO:MF RNA binding; q_global = 0.00124), cytoplasmic translation (GO:BP cytoplasmic translation; q_global = 0.00191), translation (GO:BP translation; q_global = 0.00204), protein biosynthetic process (GO:BP protein biosynthetic process; q_global = 0.00204), and gene expression (GO:BP gene expression; q_global = 0.0469). Its genes span translation initiation through ribosomal function, aminoacyl-tRNA charging, pre-mRNA splicing, mRNA export, RNA helicase activity, and nonsense-mediated mRNA decay. Thus, the module likely represents coordinated control of RNA maturation, RNA surveillance, and translation rather than a tissue-specific signaling pathway. The sparse co-abundance graph nonetheless links these processes through EIF3C, RNA-processing factors, ribosomal proteins, and translation-related enzymes.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a single secreted gene, and the individual annotations are overwhelmingly intracellular. Most genes have low tissue specificity and low immune-cell specificity, consistent with broadly expressed housekeeping-type machinery. There is, however, evidence for enrichment in bone marrow, lymphoid tissue, and several hematopoietic progenitor populations, particularly for ALYREF and LMNB1, while additional genes show cell-type enhancement in neutrophils, megakaryocyte progenitors, monocyte progenitors, erythrocyte progenitors, and other cell types. Therefore, the shared circulatory-system and prostate signal may reflect broadly expressed core gene-expression machinery, with a possible contribution from shared blood or progenitor-cell content rather than a prostate-specific biological program. The protein-detection evidence in prostate supports that many module proteins are present there, but it does not by itself establish a prostate-specific function.

**GO/KEGG enrichment**: 7 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC ribonucleoprotein complex | 0.000231 | DAZAP1, DHX9, EFTUD2, EIF3C, EIF3L, RPL12, RPL3, SNRNP200, UPF1 |
| GO:MF nucleic acid binding | 0.00108 | AARS1, ALYREF, DAZAP1, DHX9, EFTUD2, EIF3C, EIF3L, FARSB, LMNB1, MARS1, RPL12, RPL3, SNRNP200, UPF1 |
| GO:MF RNA binding | 0.00124 | AARS1, ALYREF, DAZAP1, DHX9, EFTUD2, EIF3C, EIF3L, FARSB, MARS1, RPL12, RPL3, SNRNP200, UPF1 |
| GO:BP cytoplasmic translation | 0.00191 | AARS1, DHX9, EIF3C, EIF3L, RPL12, RPL3 |
| GO:BP translation | 0.00204 | AARS1, DHX9, EIF3C, EIF3L, FARSB, MARS1, RPL12, RPL3, UPF1 |
| GO:BP protein biosynthetic process | 0.00204 | AARS1, DHX9, EIF3C, EIF3L, FARSB, MARS1, RPL12, RPL3, UPF1 |
| GO:BP gene expression | 0.0469 | AARS1, DAZAP1, DHX9, EFTUD2, EIF3C, EIF3L, FARSB, LMNB1, MARS1, PHB1, RPL12, RPL3, SNRNP200, UPF1 |

### STRING and hu.MAP

STRING supports several established relationships within the module. The strongest coherent groups are the EIF3C–EIF3L translation-initiation pair, the RPL3–RPL12 ribosomal pair, the AARS1–MARS1–FARSB aminoacyl-tRNA-synthetase group, and the ALYREF–DHX9–EFTUD2–UPF1 RNA-processing and surveillance connections. EFTUD2 and SNRNP200 are strongly connected in STRING and occur together across multiple hu.MAP spliceosomal complexes, supporting a genuine spliceosome-related substructure. EIF3C and EIF3L likewise recur together in multiple hu.MAP translation-initiation complexes. These observations indicate that part of the co-abundance module recapitulates known physical or functional machinery rather than being an arbitrary correlation pattern. The STRING enrichments are supplementary and reinforce, but do not replace, the globally corrected GO evidence.

**STRING interactions (score >= 0.7)**: 12 of 120 gene pairs: AARS1–FARSB (0.814); AARS1–MARS1 (0.913); ALYREF–DHX9 (0.953); ALYREF–EFTUD2 (0.89); ALYREF–UPF1 (0.998); DHX9–SNRNP200 (0.784); EFTUD2–RPL12 (0.752); EFTUD2–RPL3 (0.837); EFTUD2–SNRNP200 (0.999); EIF3C–EIF3L (0.999); FARSB–MARS1 (0.705); RPL12–RPL3 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Ribonucleoprotein complex (FDR = 9.41e-06, 10 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 5.6e-05, 9 genes); Function Nucleic acid binding (FDR = 0.00049, 14 genes); Function RNA binding (FDR = 0.00049, 13 genes); RCTM Formation of a pool of free 40S subunits (FDR = 0.0018, 4 genes); RCTM Translation (FDR = 0.0018, 7 genes); RCTM L13a-mediated translational silencing of Ceruloplasmin expression (FDR = 0.0029, 4 genes); RCTM GTP hydrolysis and joining of the 60S ribosomal subunit (FDR = 0.0029, 4 genes); Process Gene expression (FDR = 0.0051, 12 genes); Process Translation (FDR = 0.0092, 7 genes); Process Macromolecule biosynthetic process (FDR = 0.0092, 9 genes); RCTM Nonsense Mediated Decay (NMD) independent of the Exon Junction Complex (EJC) (FDR = 0.0128, 3 genes); Process Cytoplasmic translation (FDR = 0.0132, 4 genes); TISSUES Lymphocyte (FDR = 0.0158, 8 genes); Process Cellular macromolecule metabolic process (FDR = 0.0177, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00960.1 (SNRNP200, EFTUD2; 2/8); huMAP3_07622.1 (SNRNP200, EFTUD2; 2/9); huMAP3_01276.1 (EIF3C, EIF3L; 2/17); huMAP3_13175.1 (EIF3C, EIF3L; 2/20); huMAP3_11246.1 (EIF3C, EIF3L; 2/24); huMAP3_08501.1 (SNRNP200, EFTUD2; 2/47); huMAP3_09504.1 (SNRNP200, EFTUD2; 2/51); huMAP3_09945.1 (SNRNP200, EFTUD2; 2/61); huMAP3_08980.1 (SNRNP200, EFTUD2; 2/97)

### Novelty

The molecular functions represented here are established: translation, ribosome activity, spliceosomal RNA processing, mRNA export, and nonsense-mediated decay are well-characterized processes. The presence of known STRING links and recurring hu.MAP complexes argues against claiming a newly discovered molecular complex. A potentially novel aspect is the conserved co-abundance configuration shared between circulatory_system and prostate, especially the coupling of translation-initiation, ribosomal, spliceosomal, and RNA-surveillance components in these tissue groups. However, the fact sheet does not provide a literature comparison or an independent replication analysis that specifically establishes this tissue-pair module as new. The appropriate conclusion is that the module may be a novel tissue-level co-abundance pattern built from largely known machinery, but novelty is not demonstrated solely by relationships absent from STRING or hu.MAP.

**Hypothesis.** Hypothesis: in both circulatory_system and prostate, variation in cellular composition or physiological state produces coordinated changes in a core RNA-protein production program. EIF3C and EIF3L may organize translation initiation, while ribosomal proteins and aminoacyl-tRNA synthetases support protein synthesis; spliceosomal factors such as EFTUD2 and SNRNP200, together with ALYREF, DHX9, and UPF1, may couple pre-mRNA maturation, export, RNA quality control, and translation. The shared module could therefore reflect a coordinated demand for accurate production and surveillance of proteins, potentially amplified by common progenitor or proliferative cell contributions. This is a mechanistic interpretation to test, not an established causal conclusion; useful tests would include cell-composition adjustment, independent tissue cohorts, perturbation of translation or RNA-surveillance components, and assessment of coordinated changes in splicing, mRNA export, and translational output.

### Important genes

#### EIF3C

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.88), MARS1 (0.88), RPL3 (0.87), EIF3L (0.85), SNRNP200 (0.82), LMNB1 (0.81); STRING partners: EIF3L (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_01276.1, huMAP3_13175.1, huMAP3_11246.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C is the most connected node in the module graph and links translation-related genes with RNA-processing components. It appears in every globally significant GO term (GO:CC ribonucleoprotein complex; q_global = 0.000231) through (GO:BP gene expression; q_global = 0.0469), is part of the EIF3 translation-initiation complex, and has a direct STRING relationship with EIF3L. Its HPA profile is broadly expressed and intracellular, with protein detected in prostate. Its substantial literature and disease-association record make it a well-established anchor for the module.
- **Conclusion**: Established evidence supports EIF3C as a central translation-initiation component and a principal network organizer. The hypothesis that it coordinates the RNA-processing and translation arms of this tissue-pair module is plausible from its network position, but causality and tissue-pair specificity remain unproven.

#### DHX9

- **Related proteins** (co-abundance neighbors): RPL3 (0.89), ALYREF (0.82), RPL12 (0.82); STRING partners: ALYREF (0.953), SNRNP200 (0.784)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 connects ribosomal proteins with ALYREF and SNRNP200 in the module and is represented across all globally significant GO terms (GO:CC ribonucleoprotein complex; q_global = 0.000231) through (GO:BP gene expression; q_global = 0.0469). It is an ATP-dependent RNA and DNA-RNA helicase involved in RNA processing, transcriptional regulation, and interferon-related regulation. Its extensive literature and disease associations provide stronger biological context than would be inferred from enrichment alone.
- **Conclusion**: Established evidence supports DHX9 as a multifunctional RNA helicase linking RNA metabolism with translation-associated components. It is a credible bridge between RNA processing and protein synthesis in this module, but the specific cross-tissue mechanism remains a hypothesis.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): EIF3C (0.88), SNRNP200 (0.86); STRING partners: ALYREF (0.89), RPL12 (0.752), RPL3 (0.837), SNRNP200 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_08980.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 occupies a connector position between EIF3C and SNRNP200 in the module. It is a spliceosomal GTPase involved in tri-snRNP assembly, spliceosome conformational change, and pre-mRNA splicing, and it is included in multiple hu.MAP spliceosomal complexes with SNRNP200. STRING also supports relationships with ALYREF and ribosomal proteins. Its established association with mandibulofacial dysostosis with microcephaly highlights the developmental importance of accurate RNA processing.
- **Conclusion**: Established evidence identifies EFTUD2 as a spliceosome component and a plausible structural link between RNA splicing and the broader module. Its participation in a translation-centered tissue co-abundance pattern is an interpretation of the network, not evidence that EFTUD2 directly regulates translation in these tissues.

#### ALYREF

- **Related proteins** (co-abundance neighbors): DHX9 (0.82); STRING partners: DHX9 (0.953), EFTUD2 (0.89), UPF1 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Aly/REF export factor. The protein encoded by this gene is a heat stable, nuclear protein and functions as a molecular chaperone. It is thought to regulate dimerization, DNA binding, and transcriptional activity of basic region-leucine zipper (bZIP) proteins. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.542); dengue disease (0.370); neoplasm (0.103); non-small cell lung carcinoma (0.102); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 1636
- **Why important**: ALYREF links DHX9, EFTUD2, and UPF1 in STRING and is annotated for nuclear mRNA export, mRNA metabolism, and regulation of nonsense-mediated decay. It is tissue enhanced in bone marrow and cell-type enhanced in erythrocyte and megakaryocyte progenitor populations, making it especially informative for evaluating whether the circulatory-system signal reflects blood or progenitor-cell composition. It also appears in the ribonucleoprotein and RNA-binding supplementary STRING terms.
- **Conclusion**: Established evidence supports ALYREF as an mRNA export and RNA-metabolism factor with a relevant hematopoietic expression pattern. It may help explain the shared module through progenitor-cell composition or coordinated RNA export, but either explanation requires testing against cellular composition and independent samples.

#### UPF1

- **Related proteins** (co-abundance neighbors): MARS1 (0.86), FARSB (0.82); STRING partners: ALYREF (0.998)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UPF1 RNA helicase and ATPase. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons.…
- **Diseases (Open Targets)**: Intellectual disability (0.437); Global developmental delay (0.426); High anterior hairline (0.425); Frontal bossing (0.425); Hypertelorism (0.425)
- **Europe PMC papers**: 4252
- **Why important**: UPF1 is a core RNA helicase and ATPase involved in mRNA export, nonsense-mediated decay, and translational termination. It connects to ALYREF in STRING and to translation-related components through the module graph, while appearing in the globally significant nucleic-acid binding, RNA-binding, translation, protein-biosynthesis, and gene-expression terms (GO:MF nucleic acid binding; q_global = 0.00108), (GO:MF RNA binding; q_global = 0.00124), (GO:BP translation; q_global = 0.00204), (GO:BP protein biosynthetic process; q_global = 0.00204), and (GO:BP gene expression; q_global = 0.0469). Its extensive literature and disease-association record support its importance as an RNA-quality-control component.
- **Conclusion**: Established evidence supports UPF1 as a central mRNA-surveillance factor that can connect RNA export and translation. The proposed role of UPF1 in coupling quality control to the tissue-pair module is mechanistically reasonable, but the co-abundance data do not establish directionality or direct regulation.

## Module 10

**Tissue pair**: circulatory_system and prostate  
**Genes (14)**: GALE, HNRNPLL, HSPBP1, HSP90AA1, HSPA8, IDI1, IPO4, LDHA, NELFCD, NUP43, PAFAH1B3, PTBP1, ATIC, RAN

### Function

No GO/KEGG term passed global correction, so the module does not support a formally significant pathway assignment from those analyses. Its internal pattern instead suggests a broadly expressed intracellular program combining nuclear RNA and transcriptional regulation, nucleocytoplasmic transport, proteostasis, and core metabolism. The strongest network position is occupied by NELFCD, which connects the nuclear regulatory component to several other module branches. RAN and NUP43 support nuclear transport, while PTBP1 and HNRNPLL support RNA processing. HSPA8, HSP90AA1, and HSPBP1 support chaperone and protein-quality-control biology. ATIC, IDI1, GALE, and LDHA represent purine, isoprenoid, carbohydrate, and glycolytic metabolism, respectively. The STRING tissue annotations (STRING TISSUES Skin; within-query FDR = 0.00068) and (STRING TISSUES Abdomen; within-query FDR = 0.0301) are supplementary and consistent with a general intracellular maintenance program, not evidence of globally significant enrichment.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and the listed proteins are intracellular or nuclear. Most genes have low tissue specificity, which is compatible with broadly expressed housekeeping-like biology rather than a specialized circulatory or prostate secretory program. HPA reports low immune-cell specificity for every module gene and no enriched blood-cell category, arguing against a straightforward blood-cell-composition explanation. At the same time, most genes are cell-type enhanced in diverse cell types, including epithelial, reproductive, neural, and trophoblast-related populations. This heterogeneous pattern indicates that the shared circulatory-system and prostate signal could reflect a conserved cellular maintenance state or shared cellular constituents rather than a tissue-specific pathway. The prostate protein data show detection for several genes, but the circulatory-system protein comparison has no matching HPA tissue data, so protein-level tissue interpretation remains limited.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The high-confidence STRING evidence is sparse but coherent in selected parts of the module. HSP90AA1 connects strongly with HSPA8 and HSPBP1, and HSPA8 connects strongly with HSPBP1, forming a recognizable chaperone and co-chaperone neighborhood. IPO4 connects with RAN, consistent with nuclear import biology. The hu.MAP evidence independently places HSPA8 and HSPBP1 together across several chaperone-related complexes (hu.MAP huMAP3_04877.1) through (hu.MAP huMAP3_14723.1), although they are only partial members of those larger complexes. RAN and NUP43 occur together in a nuclear-pore-related complex (hu.MAP huMAP3_12581.1). Most other module edges have no corresponding STRING or hu.MAP support in the fact sheet. Thus, the module contains established protein-interaction substructures, but its complete co-abundance architecture is not equivalent to a single experimentally established multiprotein complex.

**STRING interactions (score >= 0.7)**: 4 of 91 gene pairs: HSP90AA1–HSPA8 (0.999); HSP90AA1–HSPBP1 (0.87); HSPA8–HSPBP1 (0.998); IPO4–RAN (0.985)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Skin (FDR = 0.00068, 10 genes); TISSUES Abdomen (FDR = 0.0301, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04877.1 (HSPA8, HSPBP1; 2/7); huMAP3_05866.1 (HSPA8, HSPBP1; 2/12); huMAP3_06506.1 (HSPA8, HSPBP1; 2/23); huMAP3_07919.1 (HSPA8, HSPBP1; 2/27); huMAP3_11049.1 (HSPA8, HSPBP1; 2/30); huMAP3_14723.1 (HSPA8, HSPBP1; 2/52); huMAP3_12581.1 (RAN, NUP43; 2/58)

### Novelty

This module should not be called a wholly new biological mechanism. Its chaperone relationships, the RAN nuclear-transport relationship, and the participation of HSPA8 and HSPBP1 in hu.MAP complexes are already established (hu.MAP huMAP3_04877.1) through (hu.MAP huMAP3_12581.1). Conversely, the complete cross-tissue co-abundance configuration has limited support from the listed interaction resources and has no globally significant GO/KEGG term. That combination may indicate a context-specific or composite co-abundance pattern, but absence from STRING or hu.MAP alone does not establish novelty. The most defensible conclusion is that the shared circulatory-system–prostate module may be a new observation at the network-configuration level, while its component functions are largely established.

**Hypothesis.** Hypothesis: the module reflects a conserved intracellular maintenance state shared by cells represented in circulatory-system and prostate samples. In this model, NELFCD and PTBP1 coordinate transcriptional elongation and RNA processing, RAN, IPO4, and NUP43 support nuclear transport, and the HSPA8–HSP90AA1–HSPBP1 neighborhood buffers protein folding and turnover. Metabolic genes such as ATIC, IDI1, GALE, and LDHA may provide biosynthetic and energetic support for that state. The observed co-abundance could therefore arise from coordinated demand for gene-expression control, nuclear trafficking, proteostasis, and metabolism rather than from a single canonical pathway. This is a testable hypothesis, not an enrichment-based conclusion.

### Important genes

#### NELFCD

- **Related proteins** (co-abundance neighbors): RAN (0.87), GALE (0.84), PTBP1 (0.83), HSP90AA1 (0.82), IPO4 (0.82), ATIC (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: negative elongation factor complex member C/D. The NELF complex of proteins interacts with the DSIF protein complex to repress transcriptional elongation by RNA polymerase II. The protein encoded by this gene is an essential part of the NELF complex. Alternative translation initiation site usage results in the formation of two isoforms with different N-termini. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: HIV infectious disease (0.593); neurodegenerative disease (0.549); hypertensive disorder (0.277); esophageal cancer (0.133); colorectal carcinoma (0.080)
- **Europe PMC papers**: 166
- **Why important**: NELFCD has the most central position in the module network and links the nuclear regulatory branch to RAN, GALE, PTBP1, HSP90AA1, IPO4, and ATIC. Its established role as an essential component of the negative elongation factor complex makes it a plausible organizer of the transcriptional component. It has relatively limited literature compared with the major chaperone and transport genes, so its prominent network position is especially informative.
- **Conclusion**: Established evidence supports a role in RNA polymerase transcriptional pausing and negative regulation of transcription elongation. The module topology supports NELFCD as a candidate coordinator of the shared nuclear-maintenance signal, but a direct regulatory role across the entire module remains a hypothesis.

#### RAN

- **Related proteins** (co-abundance neighbors): NELFCD (0.87), PTBP1 (0.85), LDHA (0.81), PAFAH1B3 (0.80); STRING partners: IPO4 (0.985)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12581.1
- **Function (MyGene.info)**: RAN, member RAS oncogene family. RAN (ras-related nuclear protein) is a small GTP binding protein belonging to the RAS superfamily that is essential for the translocation of RNA and proteins through the nuclear pore complex. The RAN protein is also involved in control of DNA synthesis and cell cycle progression. Nuclear localization of RAN requires the presence of regulator of chromosome condensation 1 (RCC1). Mutations in RAN di…
- **Diseases (Open Targets)**: HIV infectious disease (0.565); Orthomyxoviridae infectious disease (0.376); pemphigus foliaceus (0.298); neurodegenerative disease (0.270); Genu valgum (0.136)
- **Europe PMC papers**: 133080
- **Why important**: RAN is a central connector between NELFCD, PTBP1, LDHA, and PAFAH1B3 and has an experimentally supported STRING relationship with IPO4. It is also part of the nuclear-pore-related hu.MAP complex with NUP43 (hu.MAP huMAP3_12581.1). Its established roles in nuclear import, RNA and ribosomal export, DNA synthesis, and cell-cycle control give it a strong mechanistic link between nuclear transport and cellular growth.
- **Conclusion**: Established evidence supports RAN as a core regulator of nucleocytoplasmic transport and cell-cycle-associated nuclear processes. Its network position makes it a strong candidate for connecting the module's nuclear and metabolic branches, but the co-abundance data do not establish that RAN drives the module.

#### HSPA8

- **Related proteins** (co-abundance neighbors): HSP90AA1 (0.88); STRING partners: HSP90AA1 (0.999), HSPBP1 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Flagellar centriole, Annulus; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_04877.1, huMAP3_05866.1, huMAP3_06506.1, huMAP3_07919.1, huMAP3_11049.1, huMAP3_14723.1
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 8. This gene encodes a member of the heat shock protein 70 family, which contains both heat-inducible and constitutively expressed members. This protein belongs to the latter group, which are also referred to as heat-shock cognate proteins. It functions as a chaperone, and binds to nascent polypeptides to facilitate correct folding. It also functions as an ATPase in the disassembly of clathrin-coated…
- **Diseases (Open Targets)**: dengue disease (0.505); systemic lupus erythematosus (0.375); smoking initiation (0.199); Lennox-Gastaut syndrome (0.118); neoplasm (0.105)
- **Europe PMC papers**: 6937
- **Why important**: HSPA8 is part of the most strongly supported chaperone neighborhood, with STRING relationships to HSP90AA1 and HSPBP1 and repeated membership with HSPBP1 in hu.MAP complexes (hu.MAP huMAP3_04877.1) through (hu.MAP huMAP3_14723.1). It is a constitutive HSP seventy-family chaperone involved in nascent-polypeptide folding, unfolded-protein responses, and vesicle-related processes, and it is detected in prostate tissue.
- **Conclusion**: Established evidence supports HSPA8 as a proteostasis and trafficking chaperone embedded in known complexes. In this module it is the clearest representative of the chaperone substructure, while its role as a tissue-pair-specific coordinator remains a hypothesis.

#### PTBP1

- **Related proteins** (co-abundance neighbors): ATIC (0.88), RAN (0.85), NELFCD (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypyrimidine tract binding protein 1. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA-binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.505); dengue disease (0.372); open-angle glaucoma (0.330); glaucoma (0.309); neoplasm (0.116)
- **Europe PMC papers**: 4849
- **Why important**: PTBP1 connects ATIC, RAN, and NELFCD and has a substantial literature base. Its established function in pre-mRNA processing and alternative splicing provides a complementary RNA-regulatory link to NELFCD and RAN. HPA places it in the nucleoplasm and reports prostate detection, consistent with a cellular rather than secreted signal.
- **Conclusion**: Established evidence supports PTBP1 as a broadly expressed RNA-binding regulator of splicing and mRNA metabolism. Its position suggests that RNA processing may be part of the shared module state, but the data do not demonstrate a specific PTBP1-dependent mechanism in either tissue.

#### HSPBP1

- **Related proteins** (co-abundance neighbors): IPO4 (0.81); STRING partners: HSP90AA1 (0.87), HSPA8 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_04877.1, huMAP3_05866.1, huMAP3_06506.1, huMAP3_07919.1, huMAP3_11049.1, huMAP3_14723.1
- **Function (MyGene.info)**: HSPA (Hsp70) binding protein 1. Enables ubiquitin protein ligase binding activity. Involved in positive regulation of proteasomal ubiquitin-dependent protein catabolic process and positive regulation of protein ubiquitination. Predicted to be active in endoplasmic reticulum. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.372); hypothyroidism (0.218); breast cancer (0.077); non-syndromic male infertility due to sperm motility disorder (0.076); breast carcinoma (0.076)
- **Europe PMC papers**: 511
- **Why important**: HSPBP1 is a direct STRING partner of HSP90AA1 and HSPA8 and appears with HSPA8 across several hu.MAP chaperone complexes (hu.MAP huMAP3_04877.1) through (hu.MAP huMAP3_14723.1). Its annotated functions in HSPA binding, protein ubiquitination, and proteasomal degradation make it a useful mechanistic bridge between chaperone activity and protein quality control. It is detected in prostate tissue.
- **Conclusion**: Established evidence supports HSPBP1 as a chaperone-associated regulator of ubiquitin-dependent protein turnover. Its repeated complex associations strengthen the interpretation of a proteostasis submodule, but they do not prove that altered HSPBP1 activity explains the cross-tissue co-abundance.
