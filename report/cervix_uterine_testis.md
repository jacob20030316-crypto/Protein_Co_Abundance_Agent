# Conserved co-abundance modules: cervix_uterine and testis

## Module 0

**Tissue pair**: cervix_uterine and testis  
**Genes (49)**: ACTL6A, ARFGAP1, ATXN10, BCAT2, CCS, COPG2, CPS1, DDX6, DSP, DDX39B, EPS15, GFUS, HACD3, HNRNPH1, HNRNPF, HSDL2, IPO11, TMPO, TMPO, LMNB1, METAP1, MCM4, MAT2A, MYH10, NME1, NT5DC1, OAT, PDXDC1, PNPT1, ADSL, CAD, RRM1, MRPS27, SLC25A24, PSAT1, SERPINH1, SKIC3, SNAP23, SNX2, SPART, ACAA1, THOP1, TIMM44, TMOD3, TNPO3, TOM1, SNRNP200, UMPS, XPO5

### Function

The strongest supported function is pyrimidine-containing compound metabolism, based on the sole globally corrected term (GO:BP pyrimidine-containing compound metabolic process; q_global = 0.0237), which includes CAD, CPS1, NME1, RRM1 and UMPS. The supplementary STRING result (STRING WikiPathways Pyrimidine metabolism; within-query FDR = 0.0406) independently points toward pyrimidine metabolism through UMPS, CAD, RRM1 and NME1, although it is not global evidence. The module is not a clean linear pyrimidine pathway: its network also contains coherent RNA processing and transport components, including XPO5, SNRNP200, HNRNPH1, HNRNPF, DDX39B and TNPO3; mitochondrial RNA and protein-handling components; vesicle and endosomal trafficking proteins; and cell-cycle or chromatin-associated proteins. Thus, the most defensible interpretation is a metabolic and biosynthetic core embedded in a broader housekeeping program involving RNA handling, nucleocytoplasmic transport, organelle maintenance and proliferative capacity. No other GO or KEGG term passed global correction.

**Cell composition.** This does not resemble a plasma-protein or broadly secreted module: the fact sheet identifies only a single secreted gene, and the proteins are predominantly intracellular. The HPA profile is nevertheless broad, with low tissue specificity for most annotated genes and protein detection in both cervix_uterine and testis for nearly all members. The module is therefore compatible with a shared cellular or housekeeping signal rather than a specialized secretory program. Single-cell annotations frequently highlight late spermatids, hepatocytes, neutrophils, erythrocyte progenitors and other distinct cell types. Blood-cell specificity is mostly low, so the module is not best described as a blood-cell module, although the erythroid, neutrophil and lymphoid annotations indicate that cell composition could contribute in some samples. The hepatocyte and liver enrichment is especially relevant because CPS1 is liver-enriched and not detected in either target tissue by HPA, raising the possibility of a metabolic or contaminating-cell component rather than a uniformly resident tissue program.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP pyrimidine-containing compound metabolic process | 0.0237 | CAD, CPS1, NME1, RRM1, UMPS |

### STRING and hu.MAP

STRING supports several established local relationships rather than a single complete module mechanism. The pyrimidine-related core is supported by CAD-UMPS, CAD-CPS1, CPS1-UMPS, ADSL-UMPS, NME1-RRM1 and MCM4-RRM1 relationships, with the supplementary pathway result (STRING WikiPathways Pyrimidine metabolism; within-query FDR = 0.0406). Other established links connect XPO5 with DDX6, HNRNPH1 with HNRNPF and DDX39B, LMNB1 with TMPO, EPS15 with SPART, ACAA1 with HSDL2, and IPO11 with TNPO3. These interactions indicate that some module edges recapitulate known biochemical or protein-complex relationships, while many co-abundance links are not represented by high-confidence STRING associations. hu.MAP provides repeated support for the HNRNPH1-HNRNPF spliceosome or RNA-binding group (hu.MAP huMAP3_07055.1) (hu.MAP huMAP3_06054.1) (hu.MAP huMAP3_11034.1) (hu.MAP huMAP3_13511.1) (hu.MAP huMAP3_14523.1), the XPO5-TNPO3-IPO11 transport group (hu.MAP huMAP3_10202.1) (hu.MAP huMAP3_05832.1) (hu.MAP huMAP3_06077.1) (hu.MAP huMAP3_08298.1) (hu.MAP huMAP3_09053.1) (hu.MAP huMAP3_09114.1) (hu.MAP huMAP3_10287.1) (hu.MAP huMAP3_11232.1), the LMNB1-TMPO nuclear-envelope pair (hu.MAP huMAP3_09748.1), the EPS15-ARFGAP1 trafficking group (hu.MAP huMAP3_05120.1) (hu.MAP huMAP3_05849.1) (hu.MAP huMAP3_08320.1) (hu.MAP huMAP3_09403.1) (hu.MAP huMAP3_10876.1), and the CAD- or UMPS-associated complexes (hu.MAP huMAP3_09042.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_14442.1) (hu.MAP huMAP3_13468.1). Because many hu.MAP complexes contain only a small subset of this module, the module appears to combine several known cellular subsystems rather than correspond to one established complex.

**STRING interactions (score >= 0.7)**: 16 of 1176 gene pairs: ACAA1–HSDL2 (0.916); ADSL–UMPS (0.796); CAD–CPS1 (0.908); CAD–UMPS (0.946); CPS1–OAT (0.734); CPS1–UMPS (0.848); DDX39B–HNRNPF (0.736); DDX39B–HNRNPH1 (0.742); DDX39B–SNRNP200 (0.709); DDX6–XPO5 (0.943); EPS15–SPART (0.955); HNRNPF–HNRNPH1 (0.994); IPO11–TNPO3 (0.77); LMNB1–TMPO (0.981); MCM4–RRM1 (0.952); NME1–RRM1 (0.846)
**STRING functional enrichment (supplementary, within-query FDR)**: WikiPathways Pyrimidine metabolism (FDR = 0.0406, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10202.1 (XPO5, IPO11, TNPO3; 3/52); huMAP3_07055.1 (HNRNPH1, HNRNPF; 2/3); huMAP3_09748.1 (LMNB1, TMPO; 2/3); huMAP3_06054.1 (HNRNPH1, HNRNPF; 2/4); huMAP3_11034.1 (HNRNPH1, HNRNPF; 2/5); huMAP3_13511.1 (HNRNPH1, HNRNPF; 2/9); huMAP3_05120.1 (EPS15, ARFGAP1; 2/14); huMAP3_05832.1 (XPO5, TNPO3; 2/14); huMAP3_06077.1 (XPO5, TNPO3; 2/15); huMAP3_05849.1 (EPS15, ARFGAP1; 2/21); huMAP3_08320.1 (EPS15, ARFGAP1; 2/24); huMAP3_08298.1 (XPO5, TNPO3; 2/24); huMAP3_09053.1 (XPO5, TNPO3; 2/25); huMAP3_09403.1 (EPS15, ARFGAP1; 2/26); huMAP3_09042.1 (UMPS, ATXN10; 2/26); huMAP3_09114.1 (XPO5, TNPO3; 2/30); huMAP3_14523.1 (HNRNPH1, HNRNPF; 2/33); huMAP3_10876.1 (EPS15, ARFGAP1; 2/40); huMAP3_10287.1 (XPO5, TNPO3; 2/53); huMAP3_14306.1 (ACTL6A, MCM4; 2/55); huMAP3_14442.1 (ADSL, NT5DC1; 2/57); huMAP3_11232.1 (IPO11, TNPO3; 2/78); huMAP3_09592.1 (HACD3, ATXN10; 2/95); huMAP3_13468.1 (CPS1, PNPT1; 2/99)

### Novelty

This module should be considered a potentially interesting cross-tissue co-abundance pattern, not a demonstrated new biochemical pathway. The pyrimidine enzymes, RNA-processing proteins, nuclear transport proteins, mitochondrial proteins and trafficking proteins are individually well established, and several of their relationships are already present in STRING or hu.MAP. The distinctive aspect may be their coordinated abundance across cervix_uterine and testis, but the fact sheet does not provide an external replication cohort, perturbation evidence, tissue-specific validation or a comparison with previously reported co-abundance modules. The absence of the complete module from STRING or hu.MAP would not prove novelty, because those resources catalogue physical interactions and complexes rather than every expression-covariation pattern. Accordingly, the appropriate claim is a novel candidate module configuration that requires independent validation, rather than a newly discovered molecular mechanism.

**Hypothesis.** Hypothesis: the shared module reflects a cellular state that couples nucleotide supply with RNA maturation, nucleocytoplasmic transport, mitochondrial maintenance and membrane trafficking. In this model, CAD and UMPS provide a pyrimidine-biosynthetic signal, RRM1 and NME1 connect nucleotide availability to DNA precursor and nucleotide handling, while XPO5, SNRNP200, HNRNPH1, HNRNPF and related transport factors coordinate RNA processing and export. The trafficking, cytoskeletal and mitochondrial members may reflect the structural and energetic demands of germ-cell or epithelial-cell differentiation, or may partly represent shared housekeeping activity across the two tissues. CPS1 and its liver-associated HPA profile make a second possibility important: part of the apparent metabolic signal could arise from cell composition or tissue contamination rather than coordinated activity within one resident cell type. This hypothesis predicts that the module should separate into cell-type-specific submodules when tested with single-cell data and should show coordinated changes in pyrimidine flux, RNA processing and proliferative or differentiation state.

### Important genes

#### CAD

- **Related proteins** (co-abundance neighbors): PDXDC1 (0.85), LMNB1 (0.83), NT5DC1 (0.83), ACTL6A (0.82); STRING partners: CPS1 (0.908), UMPS (0.946)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carbamoyl-phosphate synthetase 2, aspartate transcarbamylase, and dihydroorotase. The de novo synthesis of pyrimidine nucleotides is required for mammalian cells to proliferate. This gene encodes a trifunctional protein which is associated with the enzymatic activities of the first 3 enzymes in the 6-step pathway of pyrimidine biosynthesis: carbamoylphosphate synthetase (CPS II), aspartate transcarbamoylase, and dihydroorotase. This protein is regulated by the mitogen-activated…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 50 (0.660); congenital disorder of glycosylation type I (0.595); infantile epileptic-dyskinetic encephalopathy (0.499); type 2 diabetes mellitus (0.286); urolithiasis (0.283)
- **Europe PMC papers**: 60667
- **Why important**: CAD is central to the primary evidence (GO:BP pyrimidine-containing compound metabolic process; q_global = 0.0237) and to the supplementary pyrimidine result (STRING WikiPathways Pyrimidine metabolism; within-query FDR = 0.0406). It is connected in the module to several relatively central genes and has established STRING relationships with UMPS and CPS1. Its encoded trifunctional enzyme catalyzes the initial portion of de novo pyrimidine biosynthesis, and the gene has a very large literature base and extensive disease annotation, making it the strongest anchor for the metabolic interpretation.
- **Conclusion**: Established evidence supports CAD as a de novo pyrimidine-biosynthesis component and a major biochemical anchor of the module. The hypothesis that CAD abundance coordinates the broader RNA-processing and transport program is plausible from co-abundance but is not established by the fact sheet.

#### UMPS

- **Related proteins** (co-abundance neighbors): XPO5 (0.87), NT5DC1 (0.85), PNPT1 (0.83), DSP (0.82), RRM1 (0.81); STRING partners: ADSL (0.796), CAD (0.946), CPS1 (0.848)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09042.1
- **Function (MyGene.info)**: uridine monophosphate synthetase. This gene encodes a uridine 5'-monophosphate synthase. The encoded protein is a bifunctional enzyme that catalyzes the final two steps of the de novo pyrimidine biosynthetic pathway. The first reaction is carried out by the N-terminal enzyme orotate phosphoribosyltransferase which converts orotic acid to orotidine-5'-monophosphate. The terminal reaction is carried out by the C-terminal enzyme OMP …
- **Diseases (Open Targets)**: orotic aciduria (0.773); coronary artery disorder (0.507); Intellectual disability (0.462); open-angle glaucoma (0.381); Abnormality of the skeletal system (0.374)
- **Europe PMC papers**: 965
- **Why important**: UMPS is directly included in (GO:BP pyrimidine-containing compound metabolic process; q_global = 0.0237) and (STRING WikiPathways Pyrimidine metabolism; within-query FDR = 0.0406), occupies a central position among the metabolic connections, and has STRING links to CAD, CPS1 and ADSL. It catalyzes the final steps of de novo pyrimidine production and is associated with orotic aciduria, giving the module a clear disease-linked metabolic readout. Its inclusion in hu.MAP (hu.MAP huMAP3_09042.1) also links the metabolic signal to a broader cellular complex context.
- **Conclusion**: Established evidence supports UMPS as a core pyrimidine-biosynthetic enzyme and one of the most reliable functional markers of this module. A role for UMPS in coupling nucleotide production to germ-cell or epithelial differentiation remains a hypothesis rather than a demonstrated mechanism.

#### XPO5

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.88), UMPS (0.87), NME1 (0.86), NT5DC1 (0.86), COPG2 (0.85), ACTL6A (0.85), ATXN10 (0.84), TNPO3 (0.83), IPO11 (0.81), PSAT1 (0.81); STRING partners: DDX6 (0.943)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: huMAP3_10202.1, huMAP3_05832.1, huMAP3_06077.1, huMAP3_08298.1, huMAP3_09053.1, huMAP3_09114.1, huMAP3_10287.1
- **Function (MyGene.info)**: exportin 5. This gene encodes a member of the karyopherin family that is required for the transport of small RNAs and double-stranded RNA-binding proteins from the nucleus to the cytoplasm. The encoded protein translocates cargo through the nuclear pore complex in a RanGTP-dependent process. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.533); smoking initiation (0.206); POLR1C-related disorder (0.111); hepatocellular carcinoma (0.099); cancer (0.097)
- **Europe PMC papers**: 1541
- **Why important**: XPO5 has the strongest network position in the supplied subgraph and connects metabolic, RNA-processing, transport and structural neighborhoods. It is supported by a STRING relationship with DDX6 and appears repeatedly in hu.MAP transport-related complexes (hu.MAP huMAP3_10202.1) (hu.MAP huMAP3_05832.1) (hu.MAP huMAP3_06077.1) (hu.MAP huMAP3_08298.1) (hu.MAP huMAP3_09053.1) (hu.MAP huMAP3_09114.1) (hu.MAP huMAP3_10287.1). Its established function is export of small RNAs and double-stranded RNA-binding proteins, including pre-microRNA export, and it has a substantial literature base and disease associations.
- **Conclusion**: Established evidence supports XPO5 as a nucleocytoplasmic RNA-transport hub that may explain why RNA handling is coupled to the metabolic genes in the module. Its proposed role as the bridge that coordinates pyrimidine metabolism with tissue-specific RNA programs is a hypothesis supported by network position, not direct mechanistic evidence.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): PSAT1 (0.90), XPO5 (0.88), ACTL6A (0.84), MRPS27 (0.83), DDX6 (0.82), HNRNPH1 (0.82), MCM4 (0.80); STRING partners: DDX39B (0.709)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is among the more connected module genes and links XPO5, DDX6, HNRNPH1 and MCM4. It is a core U5 snRNP helicase required for spliceosome assembly and conformational remodeling, and it has a STRING relationship with DDX39B. Its disease associations include inherited retinal disorders, and its literature volume is substantial, making it a strong representative of the RNA-processing arm.
- **Conclusion**: Established evidence supports SNRNP200 as a spliceosome component whose co-abundance is consistent with active pre-mRNA processing. The idea that enhanced splicing capacity is functionally coordinated with pyrimidine production in these tissues remains a hypothesis.

#### CPS1

- **Related proteins** (co-abundance neighbors): RRM1 (0.84); STRING partners: CAD (0.908), OAT (0.734), UMPS (0.848)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Nucleoli, Nucleoli rim; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: carbamoyl-phosphate synthase 1. The mitochondrial enzyme encoded by this gene catalyzes synthesis of carbamoyl phosphate from ammonia and bicarbonate. This reaction is the first committed step of the urea cycle, which is important in the removal of excess urea from cells. The encoded protein may also represent a core mitochondrial nucleoid protein. Three transcript variants encoding different isoforms have been found for this ge…
- **Diseases (Open Targets)**: carbamoyl phosphate synthetase I deficiency disease (0.866); Abnormality of the skeletal system (0.584); venous thromboembolism (0.524); Hyperammonemia (0.522); kidney failure (0.503)
- **Europe PMC papers**: 4139
- **Why important**: CPS1 is one of the genes in the primary term (GO:BP pyrimidine-containing compound metabolic process; q_global = 0.0237) and has strong STRING relationships with CAD, UMPS and OAT. Its established canonical function is the first committed step of the urea cycle, while the supplied annotation also places it in pyrimidine-related metabolism. HPA identifies it as liver-enriched and hepatocyte-enriched, with no protein detection in either target tissue, making it important both biologically and as a possible composition confounder.
- **Conclusion**: Established evidence supports CPS1 as a metabolic enzyme connected to the CAD-UMPS neighborhood, but its HPA profile weakens the case that it represents a resident cervix_uterine-testis program. A liver-like metabolic component, ambient signal or cell-composition effect is therefore a serious hypothesis that should be tested before assigning CPS1 a direct role in the shared tissue module.

## Module 1

**Tissue pair**: cervix_uterine and testis  
**Genes (26)**: ADD3, ALDH1A3, CPT2, CRLF3, EXOC7, FXR1, AGL, GMDS, LRBA, ME1, MYO6, NSF, NUCB2, PIP4K2C, PYGB, PYGL, RELCH, SACM1L, SAMHD1, SRPK2, STK39, STXBP2, SUN2, UBA6, UCHL5, WDR26

### Function

The module has no GO or KEGG term passing global correction, so no pathway-level enrichment can be claimed from globally significant GO/KEGG evidence. Its most coherent biological signal is glycogen metabolism: AGL is a glycogen debranching enzyme, while PYGL and PYGB are glycogen phosphorylases. These three genes form a densely supported functional core through the STRING interactions and the repeated hu.MAP complexes (hu.MAP huMAP3_08013.1) (hu.MAP huMAP3_06909.1) (hu.MAP huMAP3_01396.1) (hu.MAP huMAP3_08093.1) (hu.MAP huMAP3_10227.1) (hu.MAP huMAP3_09760.1) (hu.MAP huMAP3_13075.1) (hu.MAP huMAP3_11993.1) (hu.MAP huMAP3_12186.1). The remaining network connects this metabolic core to intracellular trafficking, cytoskeletal organization, nuclear-envelope organization, lipid and phosphoinositide handling, protein quality control, and immune or secretory-cell biology. Thus, the most defensible interpretation is a glycogen and cellular-trafficking co-abundance program rather than a single globally enriched pathway. The absence of significant GO or KEGG enrichment does not invalidate the module; it indicates that the observed signal is distributed across related but heterogeneous processes.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: only NUCB2 is annotated as secreted to blood, and the other genes are intracellular or membrane-associated. HPA shows generally broad or mixed tissue distribution, with many genes having low tissue specificity and a smaller group showing tissue enhancement in tissues such as liver, lymphoid tissue, skeletal muscle, salivary gland, or testis. Cell-type enhancement is common, especially in epithelial, neutrophil, spermatid, and secretory-cell populations. Most genes have low immune-cell specificity, but selected genes show neutrophil, monocyte, lymphoid, or T-cell associations. Therefore, the shared cervix and testis module could reflect a conserved intracellular program, shared epithelial or germ-cell-related cell states, or variable cell composition in the samples; it should not be interpreted as a purely tissue-intrinsic program without cell-composition adjustment.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a strong, specific glycogen-related interaction triangle among AGL, PYGB, and PYGL. No supplementary STRING functional-enrichment result is available. hu.MAP independently supports the same three-gene glycogen-associated core across (hu.MAP huMAP3_08013.1) (hu.MAP huMAP3_06909.1) (hu.MAP huMAP3_01396.1) (hu.MAP huMAP3_08093.1) (hu.MAP huMAP3_10227.1) (hu.MAP huMAP3_09760.1) (hu.MAP huMAP3_13075.1) (hu.MAP huMAP3_11993.1) (hu.MAP huMAP3_12186.1), with additional complex members including glycogen, starch-binding, glycogen-synthase, and regulatory proteins. This repeated complex membership is stronger evidence for a genuine biochemical core than the rest of the sparse network. hu.MAP also links LRBA with RELCH in (hu.MAP huMAP3_08114.1), and NSF with STXBP2 in (hu.MAP huMAP3_13160.1). These relationships are consistent with vesicle trafficking, membrane recycling, and regulated secretion. Most other co-abundance edges lack a corresponding reported STRING interaction or hu.MAP complex, so they should be treated as network associations rather than established physical interactions.

**STRING interactions (score >= 0.7)**: 3 of 325 gene pairs: AGL–PYGB (0.999); AGL–PYGL (0.997); PYGB–PYGL (0.984)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08013.1 (PYGL, PYGB, AGL; 3/8); huMAP3_06909.1 (PYGL, PYGB, AGL; 3/9); huMAP3_01396.1 (PYGL, PYGB, AGL; 3/10); huMAP3_08093.1 (PYGL, PYGB, AGL; 3/12); huMAP3_10227.1 (PYGL, PYGB, AGL; 3/14); huMAP3_09760.1 (PYGL, PYGB, AGL; 3/15); huMAP3_13075.1 (PYGL, PYGB, AGL; 3/15); huMAP3_11993.1 (PYGL, PYGB, AGL; 3/20); huMAP3_12186.1 (PYGL, PYGB, AGL; 3/23); huMAP3_08114.1 (LRBA, RELCH; 2/10); huMAP3_13160.1 (NSF, STXBP2; 2/49)

### Novelty

The module should not be called a wholly new biological mechanism. The central AGL–PYGB–PYGL relationship is already supported by STRING and several hu.MAP complexes, and the functions of these proteins are established. The module may nevertheless represent a new cross-tissue co-abundance configuration because the supplied databases do not establish the full set of links among the glycogen, trafficking, cytoskeletal, nuclear, and lipid-handling genes. That is a hypothesis of novelty, not proof: absence from STRING or hu.MAP can reflect incomplete coverage, context dependence, or co-abundance without direct physical binding. Demonstrating novelty would require comparison with published cervix and testis co-expression modules, independent cohorts, cell-composition-aware analyses, and experimental validation.

**Hypothesis.** Hypothesis: in selected cervix and testis cell states, glycogen availability and mobilization are coordinated with vesicle trafficking, membrane remodeling, and cytoskeletal or nuclear organization. AGL, PYGL, and PYGB could define the carbohydrate-energy core, while NSF, STXBP2, MYO6, EXOC7, and related genes could couple energy state to vesicle movement, docking, recycling, or regulated secretion. This coordination may be especially visible when epithelial, germ-cell, secretory, or immune-associated cell populations vary between samples. The hypothesis predicts that the module will track glycogen turnover and trafficking-state markers after controlling for cell composition, and that perturbing the glycogen core may alter trafficking or secretory phenotypes. These predictions are not established by the current co-abundance data.

### Important genes

#### AGL

- **Related proteins** (co-abundance neighbors): GMDS (0.86), WDR26 (0.82), MYO6 (0.81); STRING partners: PYGB (0.999), PYGL (0.997)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: huMAP3_08013.1, huMAP3_06909.1, huMAP3_01396.1, huMAP3_08093.1, huMAP3_10227.1, huMAP3_09760.1, huMAP3_13075.1, huMAP3_11993.1, huMAP3_12186.1
- **Function (MyGene.info)**: amylo-alpha-1,6-glucosidase and 4-alpha-glucanotransferase. This gene encodes the glycogen debrancher enzyme which is involved in glycogen degradation. This enzyme has two independent catalytic activities which occur at different sites on the protein: a 4-alpha-glucotransferase activity and a amylo-1,6-glucosidase activity. Mutations in this gene are associated with glycogen storage disease although a wide range of enzymatic and clinical variability occurs…
- **Diseases (Open Targets)**: glycogen storage disease III (0.831); disorder of glycogen metabolism (0.768); glycogen storage disease XV (0.608); hereditary disease (0.507); Acute rhabdomyolysis (0.463)
- **Europe PMC papers**: 4441
- **Why important**: AGL is a central member of the module's most strongly supported biochemical core. It encodes the glycogen debrancher enzyme, is connected to PYGB and PYGL by STRING, and occurs with those genes in repeated hu.MAP complexes (hu.MAP huMAP3_08013.1) (hu.MAP huMAP3_06909.1) (hu.MAP huMAP3_01396.1) (hu.MAP huMAP3_08093.1) (hu.MAP huMAP3_10227.1) (hu.MAP huMAP3_09760.1) (hu.MAP huMAP3_13075.1) (hu.MAP huMAP3_11993.1) (hu.MAP huMAP3_12186.1). It also has a well-established association with glycogen storage disease and is group enriched in skeletal muscle and tongue according to HPA.
- **Conclusion**: Established evidence supports AGL as the best anchor for a glycogen-metabolism interpretation and as a biologically meaningful module member. It is plausible, but not established, that AGL coordinates the module's metabolic signal with trafficking or cytoskeletal programs.

#### PYGL

- **Related proteins** (co-abundance neighbors): CRLF3 (0.88); STRING partners: AGL (0.997), PYGB (0.984)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_08013.1, huMAP3_06909.1, huMAP3_01396.1, huMAP3_08093.1, huMAP3_10227.1, huMAP3_09760.1, huMAP3_13075.1, huMAP3_11993.1, huMAP3_12186.1
- **Function (MyGene.info)**: glycogen phosphorylase L. This gene encodes a homodimeric protein that catalyses the cleavage of alpha-1,4-glucosidic bonds to release glucose-1-phosphate from liver glycogen stores. This protein switches from inactive phosphorylase B to active phosphorylase A by phosphorylation of serine residue 15. Activity of this enzyme is further regulated by multiple allosteric effectors and hormonal controls. Humans have three glyco…
- **Diseases (Open Targets)**: glycogen storage disease VI (0.821); disorder of glycogen metabolism (0.647); glycogen storage disease XV (0.596); neurodegenerative disease (0.370); Cholecystitis (0.357)
- **Europe PMC papers**: 1838
- **Why important**: PYGL is the liver glycogen phosphorylase and catalyzes glycogen breakdown to glucose one phosphate. It has direct STRING links to AGL and PYGB and participates with them in repeated hu.MAP complexes (hu.MAP huMAP3_08013.1) (hu.MAP huMAP3_06909.1) (hu.MAP huMAP3_01396.1) (hu.MAP huMAP3_08093.1) (hu.MAP huMAP3_10227.1) (hu.MAP huMAP3_09760.1) (hu.MAP huMAP3_13075.1) (hu.MAP huMAP3_11993.1) (hu.MAP huMAP3_12186.1). HPA shows liver enhancement and immune-cell enhancement in selected granulocyte populations, while disease associations include glycogen storage disease.
- **Conclusion**: Established evidence identifies PYGL as a strong metabolic-core gene and supports glycogen mobilization as part of the module's interpretation. Its absence of detected protein in cervix and detection in testis cautions against assuming that its co-abundance represents the same active protein program in both tissues.

#### PYGB

- **Related proteins** (co-abundance neighbors): LRBA (0.84), WDR26 (0.81); STRING partners: AGL (0.999), PYGL (0.984)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: huMAP3_08013.1, huMAP3_06909.1, huMAP3_01396.1, huMAP3_08093.1, huMAP3_10227.1, huMAP3_09760.1, huMAP3_13075.1, huMAP3_11993.1, huMAP3_12186.1
- **Function (MyGene.info)**: glycogen phosphorylase B. The protein encoded by this gene is a glycogen phosphorylase found predominantly in the brain. The encoded protein forms homodimers which can associate into homotetramers, the enzymatically active form of glycogen phosphorylase. The activity of this enzyme is positively regulated by AMP and negatively regulated by ATP, ADP, and glucose-6-phosphate. This enzyme catalyzes the rate-determining step i…
- **Diseases (Open Targets)**: neurodegenerative disease (0.419); prostate carcinoma (0.329); Short stature (0.259); neoplasm (0.102); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 901
- **Why important**: PYGB is a glycogen phosphorylase associated mainly with brain in the supplied annotation, and it catalyzes a rate-limiting step in glycogen degradation. It has strong STRING relationships with AGL and PYGL and appears with them in repeated hu.MAP complexes (hu.MAP huMAP3_08013.1) (hu.MAP huMAP3_06909.1) (hu.MAP huMAP3_01396.1) (hu.MAP huMAP3_08093.1) (hu.MAP huMAP3_10227.1) (hu.MAP huMAP3_09760.1) (hu.MAP huMAP3_13075.1) (hu.MAP huMAP3_11993.1) (hu.MAP huMAP3_12186.1). Its network links to LRBA and WDR26 may connect the metabolic core to trafficking or proteostasis-related cellular states.
- **Conclusion**: Established evidence supports PYGB as a second glycogen-breakdown component that reinforces the AGL–PYGL core. The proposed connection to LRBA or WDR26 is a network-based hypothesis rather than a demonstrated physical or causal interaction in these tissues.

#### NSF

- **Related proteins** (co-abundance neighbors): EXOC7 (0.91), ADD3 (0.89), STK39 (0.86), SUN2 (0.84), SRPK2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: huMAP3_13160.1
- **Function (MyGene.info)**: N-ethylmaleimide sensitive factor, vesicle fusing ATPase. Enables PDZ domain binding activity and ionotropic glutamate receptor binding activity. Involved in intracellular protein transport; positive regulation of protein catabolic process; and positive regulation of receptor recycling. Located in Golgi apparatus; cytosol; and plasma membrane. Implicated in developmental and epileptic encephalopathy. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy 96 (0.561); neurodegenerative disease (0.529); atrial fibrillation (0.310); Abnormality of the skeletal system (0.303); androgenetic alopecia (0.300)
- **Europe PMC papers**: 65784
- **Why important**: NSF is a relatively central network gene and encodes an ATPase involved in SNARE disassembly, intracellular protein transport, exocytosis, and receptor recycling. It is paired with STXBP2 in hu.MAP complex (hu.MAP huMAP3_13160.1) and connects in the module to EXOC7, ADD3, STK39, SUN2, and SRPK2. It also has a large literature base and established disease associations involving developmental and epileptic encephalopathy.
- **Conclusion**: Established evidence supports NSF as a trafficking and vesicle-cycle component that broadens the module beyond glycogen metabolism. Its placement next to the glycogen core suggests coordination of energy and trafficking states, but does not demonstrate that NSF directly regulates glycogen enzymes.

#### STXBP2

- **Related proteins** (co-abundance neighbors): RELCH (0.86), MYO6 (0.83), ALDH1A3 (0.82), SUN2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13160.1
- **Function (MyGene.info)**: syntaxin binding protein 2. This gene encodes a member of the STXBP/unc-18/SEC1 family. The encoded protein is involved in intracellular trafficking, control of SNARE (soluble NSF attachment protein receptor) complex assembly, and the release of cytotoxic granules by natural killer cells. Mutations in this gene are associated with familial hemophagocytic lymphohistiocytosis. Alternatively spliced transcript variants encoding…
- **Diseases (Open Targets)**: Familial hemophagocytic lymphohistiocytosis (0.823); autoinflammatory syndrome (0.466); hereditary hemophagocytic lymphohistiocytosis (0.372); hereditary disease (0.342); Thrombocytopenia (0.153)
- **Europe PMC papers**: 1259
- **Why important**: STXBP2 is a member of the Sec one family that controls SNARE-complex assembly and regulated cytotoxic-granule release. It participates with NSF in hu.MAP complex (hu.MAP huMAP3_13160.1), is connected to MYO6, RELCH, and ALDH1A3, and has HPA associations with lymphoid tissue, late spermatids, neutrophil-lineage cells, and monocytes. Its established disease association is familial hemophagocytic lymphohistiocytosis.
- **Conclusion**: Established evidence supports STXBP2 as a trafficking and regulated-secretion marker, with a possible link to immune or germ-cell-associated cell states. Because HPA reports no detected protein in either target tissue, its module membership may reflect transcript-level co-abundance, rare cell populations, or context-dependent regulation rather than abundant tissue-wide protein.

#### MYO6

- **Related proteins** (co-abundance neighbors): CPT2 (0.87), SRPK2 (0.85), STXBP2 (0.83), CRLF3 (0.83), SUN2 (0.82), AGL (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin VI. This gene encodes a reverse-direction motor protein that moves toward the minus end of actin filaments and plays a role in intracellular vesicle and organelle transport. The protein consists of a motor domain containing an ATP- and an actin-binding site and a globular tail which interacts with other proteins. This protein maintains the structural integrity of inner ear hair cells and mutations in …
- **Diseases (Open Targets)**: progressive sensorineural hearing loss-hypertrophic cardiomyopathy syndrome (0.760); autosomal dominant nonsyndromic hearing loss (0.721); hearing loss, autosomal recessive (0.702); nonsyndromic genetic hearing loss (0.660); hearing loss disorder (0.653)
- **Europe PMC papers**: 2084
- **Why important**: MYO6 has the highest network connectivity in the supplied subgraph and links trafficking, actin organization, and the module core through AGL. It encodes a reverse-direction actin motor involved in intracellular vesicle and organelle transport and has extensive literature and established hearing-loss associations. HPA detects it in both cervix and testis and shows enhancement in epithelial and selected lymphoid-associated cell types.
- **Conclusion**: Established evidence supports MYO6 as a plausible structural and trafficking bridge within the module. Its connection to AGL is compatible with the mechanistic hypothesis, but the co-abundance data do not establish that MYO6 physically couples glycogen mobilization to vesicle transport.

## Module 2

**Tissue pair**: cervix_uterine and testis  
**Genes (18)**: ASRGL1, CDH1, CFH, CLU, GLUL, SHMT1, HMOX2, HSPA2, PFKP, RAB3D, RUVBL2, S100A8, S100A9, SLC27A4, SKIC8, SRSF5, LTF, TRIM23

### Function

No GO/KEGG term passed global correction, so there is no statistically established GO/KEGG functional annotation for this module. The supplementary STRING evidence supports an innate mucosal-defense and antimicrobial theme involving LTF, CLU, S100A8 and S100A9 (STRING Keyword Immunity; within-query FDR = 0.0098)(STRING RCTM Antimicrobial peptides; within-query FDR = 0.012)(STRING Keyword Innate immunity; within-query FDR = 0.0257)(STRING Keyword Antimicrobial; within-query FDR = 0.0291). LTF contributes iron binding and antimicrobial defense; S100A8 and S100A9 support inflammatory leukocyte signaling; CLU contributes extracellular chaperoning, immune-complex clearance and regulation of membrane-attack-complex activation; and CFH regulates alternative-pathway complement activity. Other members indicate epithelial junctions, secretion, metabolism, proteostasis, RNA processing and spermatogenic biology. The most cautious interpretation is therefore a mixed epithelial and reproductive-tissue module with an innate-defense component, rather than a single proven pathway.

**Cell composition.** The module is heterogeneous rather than uniformly composed of one cell type or protein class. LTF, CLU, S100A8, S100A9 and CFH are secreted to blood. HPA associates several members with neutrophils, monocytes and other immune cells, particularly S100A8, S100A9 and LTF. This raises the possibility that part of the shared signal reflects blood, inflammatory cells or extracellular secreted proteins, especially in cervix. The module also contains epithelial and junctional biology through CDH1, reproductive-cell associations through ASRGL1, RUVBL2 and HSPA2, and broadly distributed intracellular proteins. Protein detection is widespread in both tissues, but prominent members show tissue-specific staining differences: S100A8, S100A9 and CDH1 are detected in cervix but not testis, whereas CFH and HSPA2 are detected in testis but not cervix. The shared signal may therefore reflect a mixture of resident epithelial or reproductive cells, secreted proteins and variable immune or blood contribution.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The known STRING relationships form a compact core rather than explaining the whole module. The strongest supplied relationships include CLU-LTF, S100A8-S100A9, CDH1-S100A8 and LTF-S100A8. STRING supplementary annotations connect LTF, CLU, S100A8, S100A9, TRIM23 and CFH with immunity or innate immunity, and connect LTF, CLU, S100A8 and S100A9 with antimicrobial terms (STRING Keyword Immunity; within-query FDR = 0.0098)(STRING RCTM Antimicrobial peptides; within-query FDR = 0.012)(STRING Keyword Innate immunity; within-query FDR = 0.0257)(STRING Keyword Antimicrobial; within-query FDR = 0.0291). hu.MAP contains the S100A8-S100A9 pair in two complexes (hu.MAP huMAP3_09125.1)(hu.MAP huMAP3_09929.1). Most other module genes have no supplied high-confidence STRING partner or hu.MAP complex membership. Thus, the S100A8-S100A9 pair and several secreted-defense relationships are already known, while the broader co-abundance structure is not explained by one established physical complex.

**STRING interactions (score >= 0.7)**: 4 of 153 gene pairs: CDH1–S100A8 (0.944); CLU–LTF (0.993); LTF–S100A8 (0.701); S100A8–S100A9 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Immunity (FDR = 0.0098, 6 genes); RCTM Antimicrobial peptides (FDR = 0.012, 4 genes); Keyword Innate immunity (FDR = 0.0257, 5 genes); Keyword Antimicrobial (FDR = 0.0291, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09125.1 (S100A8, S100A9; 2/53); huMAP3_09929.1 (S100A8, S100A9; 2/75)

### Novelty

This should not be described as a wholly new biological pathway. The S100A8-S100A9 relationship, CLU-LTF relationship, antimicrobial and innate-immunity associations, epithelial association through CDH1, and tissue or cell-type associations are already supported by the supplied resources. The potentially novel aspect is the particular cross-tissue co-abundance arrangement linking epithelial, reproductive, secreted-defense and intracellular genes. However, absence from STRING or hu.MAP does not establish novelty. Because no globally corrected GO/KEGG term supports the module and blood or shared-cell effects are plausible, a claim of a new mechanism would require independent replication, cell-composition adjustment and experimental validation.

**Hypothesis.** Hypothesis: the module reflects coordinated variation in a mucosal or reproductive-tissue barrier state in which epithelial integrity and secretion covary with innate antimicrobial and complement-regulatory activity. CDH1 may represent epithelial junctional state; LTF, CLU, CFH, S100A8 and S100A9 may represent extracellular defense and inflammatory activity; and the remaining genes may capture metabolic, proteostatic, trafficking, RNA-processing or spermatogenic context. A shared blood or neutrophil contribution could generate part of the signal, especially for the S100 proteins and LTF. The testis component may additionally reflect reproductive-cell programs involving HSPA2, ASRGL1 or RUVBL2. This is a testable hypothesis, not an established module function.

### Important genes

#### S100A8

- **Related proteins** (co-abundance neighbors): S100A9 (0.95), LTF (0.91), ASRGL1 (0.87); STRING partners: CDH1 (0.944), LTF (0.701), S100A9 (0.999)
- **HPA**: Tissue enhanced; Group enriched; blood Group enriched; location Intermediate filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: S100 calcium binding protein A8. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: inborn error of immunity (0.371); Sepsis (0.122); neoplasm (0.119); breast carcinoma (0.119); gastric cancer (0.119)
- **Europe PMC papers**: 18104
- **Why important**: S100A8 is a central inflammatory node connected to S100A9, LTF and ASRGL1, and it appears in every supplied STRING supplementary immunity or antimicrobial annotation (STRING Keyword Immunity; within-query FDR = 0.0098)(STRING RCTM Antimicrobial peptides; within-query FDR = 0.012)(STRING Keyword Innate immunity; within-query FDR = 0.0257)(STRING Keyword Antimicrobial; within-query FDR = 0.0291). HPA links it with cervix, bone marrow, epithelial populations, classical monocytes and neutrophils. It is also one of the module members in both supplied hu.MAP complexes (hu.MAP huMAP3_09125.1)(hu.MAP huMAP3_09929.1). Its extensive literature and disease associations make it a strong biological anchor, while its blood-cell and secreted-to-blood profile makes it important for evaluating composition effects.
- **Conclusion**: Established: S100A8 is a well-studied inflammatory and antimicrobial-associated protein that forms a known pair with S100A9 and is compatible with epithelial and myeloid contributions. Hypothesis: its network position may report a shared barrier-inflammatory state. It does not prove tissue-resident inflammation.

#### S100A9

- **Related proteins** (co-abundance neighbors): S100A8 (0.95), LTF (0.88), TRIM23 (0.81); STRING partners: S100A8 (0.999)
- **HPA**: Group enriched; Cell type enriched; blood Group enriched; location Plasma membrane, Intermediate filaments, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: S100 calcium binding protein A9. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: inborn error of immunity (0.370); Sepsis (0.121); neoplasm (0.119); psoriasis (0.114); cancer (0.114)
- **Europe PMC papers**: 16393
- **Why important**: S100A9 is tightly linked to S100A8 and LTF and is the other module member represented in both supplied hu.MAP complexes (hu.MAP huMAP3_09125.1)(hu.MAP huMAP3_09929.1). It participates in all supplied STRING immunity and antimicrobial annotations (STRING Keyword Immunity; within-query FDR = 0.0098)(STRING RCTM Antimicrobial peptides; within-query FDR = 0.012)(STRING Keyword Innate immunity; within-query FDR = 0.0257)(STRING Keyword Antimicrobial; within-query FDR = 0.0291). HPA associates it with cervix, bone marrow, epithelial cells, classical monocytes and neutrophils, and it has substantial disease literature. Its secreted-to-blood annotation makes it especially informative for assessing immune or blood contribution.
- **Conclusion**: Established: S100A9 is a recognized inflammatory partner of S100A8 with strong external network support. Hypothesis: coordinated S100A8-S100A9 abundance may form the most coherent core of the module and may report inflammatory signaling. The data do not establish whether the source is resident tissue, infiltrating myeloid cells or extracellular blood-derived material.

#### LTF

- **Related proteins** (co-abundance neighbors): CDH1 (0.94), S100A8 (0.91), S100A9 (0.88), TRIM23 (0.86), ASRGL1 (0.82); STRING partners: CLU (0.993), S100A8 (0.701)
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lactotransferrin. This gene is a member of the transferrin family of genes and its protein product is found in the secondary granules of neutrophils. The protein is a major iron-binding protein in milk and body secretions with an antimicrobial activity, making it an important component of the non-specific immune system. The protein demonstrates a broad spectrum of properties, including regulation of iron homeostasi…
- **Diseases (Open Targets)**: tuberculosis (0.517); AL amyloidosis (0.467); Abnormality of the skeletal system (0.435); schizophrenia (0.235); inflammatory bowel disease (0.218)
- **Europe PMC papers**: 7000
- **Why important**: LTF has the highest connectivity in the supplied module and links the S100 pair to CDH1, TRIM23 and ASRGL1. It has a strong STRING relationship with CLU and participates in the supplied immunity and antimicrobial terms (STRING Keyword Immunity; within-query FDR = 0.0098)(STRING RCTM Antimicrobial peptides; within-query FDR = 0.012)(STRING Keyword Antimicrobial; within-query FDR = 0.0291). Its annotations support iron binding, mucosal innate defense and antibacterial or antifungal activity. HPA places it in neutrophil-related and glandular or secretory contexts and annotates it as secreted to blood. It also has extensive literature and multiple disease associations.
- **Conclusion**: Established: LTF is a secreted host-defense and iron-binding protein with strong network integration and known association with CLU and S100A8. Hypothesis: it may connect epithelial secretion or mucosal defense to the inflammatory S100 core. Its lack of detected staining in the queried tissues, together with blood secretion, makes extracellular or blood-derived contribution an important alternative explanation.

#### CLU

- **Related proteins** (co-abundance neighbors): GLUL (0.90), CFH (0.81), ASRGL1 (0.81), SLC27A4 (0.80); STRING partners: LTF (0.993)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: clusterin. The protein encoded by this gene is a secreted chaperone that can under some stress conditions also be found in the cell cytosol. It has been suggested to be involved in several basic biological events such as cell death, tumor progression, and neurodegenerative disorders. Alternate splicing results in both coding and non-coding variants.[provided by RefSeq, May 2011].
- **Diseases (Open Targets)**: Alzheimer disease (0.583); dementia (0.525); refractive error (0.444); late-onset Alzheimers disease (0.406); prostate cancer (0.376)
- **Europe PMC papers**: 10677
- **Why important**: CLU links GLUL, CFH, ASRGL1 and SLC27A4 and has the strongest supplied STRING relationship with LTF. It appears in the immunity, antimicrobial-peptide and innate-immunity terms (STRING Keyword Immunity; within-query FDR = 0.0098)(STRING RCTM Antimicrobial peptides; within-query FDR = 0.012)(STRING Keyword Innate immunity; within-query FDR = 0.0257). Its annotation as a secreted chaperone involved in immune-complex clearance and regulation of membrane-attack-complex activation gives it a plausible extracellular defense role. HPA associates it with liver, glandular and reproductive epithelial populations and secretion to blood, and it has extensive literature and disease associations.
- **Conclusion**: Established: CLU is a secreted stress-associated chaperone with immune-regulatory functions and a known relationship to LTF. Hypothesis: it could coordinate extracellular protein protection or complement-related restraint with antimicrobial activity. Its broad secreted and tissue distribution prevents assigning the signal specifically to cervix or testis without localization evidence.

#### CDH1

- **Related proteins** (co-abundance neighbors): LTF (0.94), RUVBL2 (0.86), GLUL (0.85), PFKP (0.84); STRING partners: S100A8 (0.944)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cadherin 1. This gene encodes a classical cadherin of the cadherin superfamily. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature glycoprotein. This calcium-dependent cell-cell adhesion protein is comprised of five extracellular cadherin repeats, a transmembrane region and a highly conserved cyto…
- **Diseases (Open Targets)**: CDH1-related diffuse gastric and lobular breast cancer syndrome (0.833); blepharocheilodontic syndrome 1 (0.760); Familial gastric cancer (0.686); ovarian cancer (0.684); endometrial carcinoma (0.676)
- **Europe PMC papers**: 32214
- **Why important**: CDH1 is one of the more connected genes and is the clearest epithelial-architecture marker in the module. It links LTF to RUVBL2, GLUL and PFKP, has a supplied high-confidence STRING relationship with S100A8, and is localized to the plasma membrane and cell junctions. Its established roles include cell-cell adhesion, junction assembly and epithelial morphogenesis. HPA detects it in cervix and associates it with several epithelial cell types, while its disease literature is extensive and includes epithelial cancers and inherited gastric cancer syndromes.
- **Conclusion**: Established: CDH1 marks epithelial junctional biology and provides a known connection between epithelial structure and the S100A8-associated defense signal. Hypothesis: variation in epithelial integrity or epithelial-cell abundance may help organize the module and explain part of its cervix component. The association with S100A8 does not establish direct mechanistic coupling in these tissues.

## Module 3

**Tissue pair**: cervix_uterine and testis  
**Genes (5)**: ATP5PB, CARM1, NDUFA10, PSMA1, PSMA4

### Function

The module is most consistent with coordinated cellular proteostasis and mitochondrial energy metabolism. The strongest primary evidence is the repeated enrichment of ATP5PB, NDUFA10, PSMA1, and PSMA4 in several globally corrected KEGG pathways related to neurodegenerative disease (KEGG Parkinson disease - Homo sapiens (human); q_global = 0.0122), (KEGG Prion disease - Homo sapiens (human); q_global = 0.0144), (KEGG Huntington disease - Homo sapiens (human); q_global = 0.0169), (KEGG Alzheimer disease - Homo sapiens (human); q_global = 0.0228), and (KEGG Pathways of neurodegeneration - multiple diseases - Homo sapiens (human); q_global = 0.0379). These pathway labels should not be interpreted as evidence that the tissues have neurodegenerative disease; rather, they are shared pathway annotations containing mitochondrial respiratory and proteasomal components. The proteasome interpretation is directly supported by the globally corrected proteasome core alpha-subunit term containing PSMA1 and PSMA4 (GO:CC proteasome core complex, alpha-subunit complex; q_global = 0.0289). ATP5PB is a mitochondrial ATP-synthase component, NDUFA10 is a mitochondrial respiratory-chain complex-I component, and PSMA1 and PSMA4 are proteasome core alpha subunits. CARM1 contributes a chromatin and transcriptional-regulatory dimension, but it has no globally corrected GO or KEGG annotation in this module. Overall, the data support a module linking protein degradation and quality control with oxidative phosphorylation, with CARM1 as a possible regulatory association rather than a proven member of either physical complex.

**Cell composition.** This is not a plasma-protein or secreted-protein module: none of the genes is annotated as secreted. It is also not strongly blood-cell enriched; the HPA summary reports low immune-cell specificity for most genes and no enriched blood-cell category, with one gene not detected in immune cells. All genes have protein detection in both cervix_uterine and testis. The composition is therefore more compatible with intracellular proteins than with blood contamination. HPA nevertheless indicates tissue or cell-type-enhanced expression for several genes, including skeletal muscle, tongue, late primary spermatocytes, trophoblast-related cells, adipocytes, microglia, and other listed cell types. Thus, the shared signal could partly reflect common cellular programs or shared cell populations, particularly metabolically active or differentiating cells, rather than a tissue-pair-specific mechanism. Two genes have low tissue specificity and two have low cell-type specificity, supporting a mixture of broadly expressed housekeeping-like machinery and more context-dependent expression.

**GO/KEGG enrichment**: 6 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Parkinson disease - Homo sapiens (human) | 0.0122 | ATP5PB, NDUFA10, PSMA1, PSMA4 |
| KEGG Prion disease - Homo sapiens (human) | 0.0144 | ATP5PB, NDUFA10, PSMA1, PSMA4 |
| KEGG Huntington disease - Homo sapiens (human) | 0.0169 | ATP5PB, NDUFA10, PSMA1, PSMA4 |
| KEGG Alzheimer disease - Homo sapiens (human) | 0.0228 | ATP5PB, NDUFA10, PSMA1, PSMA4 |
| GO:CC proteasome core complex, alpha-subunit complex | 0.0289 | PSMA1, PSMA4 |
| KEGG Pathways of neurodegeneration - multiple diseases - Homo sapiens (human) | 0.0379 | ATP5PB, NDUFA10, PSMA1, PSMA4 |

### STRING and hu.MAP

STRING provides a very strong known relationship only for PSMA1 with PSMA4 (STRING KEGG Alzheimer disease; within-query FDR = 0.0019) through (STRING KEGG Proteasome; within-query FDR = 0.0407). STRING functional enrichment independently recapitulates proteasome annotations and the same neurodegeneration-related pathway group (STRING KEGG Alzheimer disease; within-query FDR = 0.0019) through (STRING KEGG Proteasome; within-query FDR = 0.0407), but these results are supplementary and do not replace the globally corrected enrichment evidence. hu.MAP identifies PSMA1 and PSMA4 together in three proteasome-containing complexes (hu.MAP huMAP3_00356.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1), alongside many additional proteasome subunits and associated proteins. ATP5PB, NDUFA10, and CARM1 have no listed STRING partner or hu.MAP complex in the supplied evidence. Consequently, the module contains a validated proteasome pair embedded in known proteasome assemblies, whereas the connections involving mitochondrial genes and CARM1 are co-abundance relationships without demonstrated physical interaction here.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: PSMA1–PSMA4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Alzheimer disease (FDR = 0.0019, 4 genes); KEGG Parkinson disease (FDR = 0.0019, 4 genes); KEGG Huntington disease (FDR = 0.0019, 4 genes); KEGG Prion disease (FDR = 0.0019, 4 genes); KEGG Amyotrophic lateral sclerosis (FDR = 0.0023, 4 genes); SMART Proteasome subunit A N-terminal signature  Add an annotation (FDR = 0.0155, 2 genes); Pfam Proteasome subunit (FDR = 0.0311, 2 genes); KEGG Proteasome (FDR = 0.0407, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00356.1 (PSMA1, PSMA4; 2/33); huMAP3_09656.1 (PSMA1, PSMA4; 2/64); huMAP3_13725.1 (PSMA1, PSMA4; 2/69)

### Novelty

The underlying protein functions and the PSMA1–PSMA4 relationship are established rather than novel, and the participation of these genes in proteasome complexes is already represented in STRING and hu.MAP. The repeated association of mitochondrial and proteasomal genes is biologically plausible and is also reflected by the shared pathway annotations, so it should not be presented as a newly discovered molecular pathway. A potentially novel aspect is the cross-tissue co-abundance module linking these components with CARM1 in cervix_uterine and testis, but the supplied evidence does not include an external module catalogue, replication cohort, perturbation experiment, or tissue-specific comparison that would establish novelty. Therefore, this is best described as a potentially useful cross-tissue network observation with partly known molecular components, not as a definitively new biological discovery. Absence of STRING or hu.MAP links for some pairs is insufficient to prove novelty.

**Hypothesis.** Hypothesis: in shared cellular populations of cervix_uterine and testis, coordinated mitochondrial respiratory activity may increase the requirement for proteasome-mediated removal of damaged or misfolded proteins. ATP5PB and NDUFA10 could represent the energetic and redox component, while PSMA1 and PSMA4 could represent the proteolytic quality-control component. CARM1 may couple this metabolic and proteostatic state to chromatin or transcriptional regulation, potentially in differentiating or metabolically specialized cells. This proposed coupling is consistent with the co-abundance structure and annotations, but it remains a hypothesis because the mitochondrial genes and CARM1 lack listed physical interactions with the proteasome pair, and co-abundance alone does not establish direction, causality, or a shared molecular complex.

### Important genes

#### PSMA1

- **Related proteins** (co-abundance neighbors): PSMA4 (0.83); STRING partners: PSMA4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: huMAP3_00356.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 20S subunit alpha 1. The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent proc…
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.535); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1417
- **Why important**: PSMA1 is a central proteasome-core marker in the module. It is directly represented in every globally corrected enrichment term (KEGG Parkinson disease - Homo sapiens (human); q_global = 0.0122) through (KEGG Pathways of neurodegeneration - multiple diseases - Homo sapiens (human); q_global = 0.0379), in all listed STRING functional terms (STRING KEGG Alzheimer disease; within-query FDR = 0.0019) through (STRING KEGG Proteasome; within-query FDR = 0.0407), and in all three hu.MAP complexes (hu.MAP huMAP3_00356.1) through (hu.MAP huMAP3_13725.1). Its HPA profile includes cell-type-enhanced expression and detection in both tissues. It also has extensive literature support and disease associations involving plasma-cell and other neoplastic disorders, HIV infectious disease, and amyloidosis.
- **Conclusion**: Established evidence supports PSMA1 as a core proteasome component and one of the most interpretable anchors of the module. Its module-level association with mitochondrial genes is observed co-abundance, not proof that PSMA1 directly regulates mitochondrial respiration.

#### PSMA4

- **Related proteins** (co-abundance neighbors): ATP5PB (0.90), PSMA1 (0.83); STRING partners: PSMA1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: huMAP3_00356.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 20S subunit alpha 4. This gene encodes a core alpha subunit of the 20S proteosome, which is a highly ordered ring-shaped structure composed of four rings of 28 non-identical subunits. Proteasomes cleave peptides in an ATP- and ubiquitin-dependent manner. [provided by RefSeq, Aug 2016].
- **Diseases (Open Targets)**: plasma cell myeloma (0.616); mantle cell lymphoma (0.542); neoplasm (0.513); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1240
- **Why important**: PSMA4 has the strongest direct network and complex evidence in the module through its highly supported STRING relationship with PSMA1 and its membership with PSMA1 in all three hu.MAP complexes (hu.MAP huMAP3_00356.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1). It is present in every globally corrected term (KEGG Parkinson disease - Homo sapiens (human); q_global = 0.0122) through (KEGG Pathways of neurodegeneration - multiple diseases - Homo sapiens (human); q_global = 0.0379) and every listed STRING term (STRING KEGG Alzheimer disease; within-query FDR = 0.0019) through (STRING KEGG Proteasome; within-query FDR = 0.0407). It is detected in both tissues, has cell-type-enhanced HPA expression, extensive literature support, and disease associations involving plasma-cell myeloma, mantle-cell lymphoma, neoplasm, HIV infectious disease, and amyloidosis.
- **Conclusion**: Established evidence identifies PSMA4 as a proteasome alpha-subunit and a validated physical partner of PSMA1. Its presence in the cross-tissue module strongly supports a proteostasis component, while any disease-specific interpretation remains an association rather than evidence of disease in these samples.

#### ATP5PB

- **Related proteins** (co-abundance neighbors): PSMA4 (0.90), NDUFA10 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP synthase peripheral stalk-membrane subunit b. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: deficiency anemia (0.178); ocular hypotension (0.038); myasthenia gravis (0.022); ulcerative colitis (0.016); nonpapillary renal cell carcinoma (0.012)
- **Europe PMC papers**: 302
- **Why important**: ATP5PB is a mitochondrial ATP-synthase subunit and occupies a connecting position between PSMA4 and NDUFA10 in the co-abundance graph. It contributes to the globally corrected neurodegeneration-related pathway terms (KEGG Parkinson disease - Homo sapiens (human); q_global = 0.0122), (KEGG Prion disease - Homo sapiens (human); q_global = 0.0144), (KEGG Huntington disease - Homo sapiens (human); q_global = 0.0169), (KEGG Alzheimer disease - Homo sapiens (human); q_global = 0.0228), and (KEGG Pathways of neurodegeneration - multiple diseases - Homo sapiens (human); q_global = 0.0379), and to the corresponding supplementary STRING terms (STRING KEGG Alzheimer disease; within-query FDR = 0.0019) through (STRING KEGG Amyotrophic lateral sclerosis; within-query FDR = 0.0023). HPA shows tissue enhancement in skeletal muscle and tongue and cell-type enhancement including late primary spermatocytes, with detection in both tissues. Its literature is substantial, and listed disease associations include deficiency anemia, ocular hypotension, myasthenia gravis, ulcerative colitis, and nonpapillary renal cell carcinoma.
- **Conclusion**: Established evidence supports ATP5PB as an oxidative-phosphorylation component and a plausible energetic arm of the module. Its connection to the proteasome and CARM1 is a network hypothesis rather than a demonstrated physical or causal interaction.

#### NDUFA10

- **Related proteins** (co-abundance neighbors): CARM1 (0.85), ATP5PB (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit A10. The protein encoded by this gene is a component of 42 kDa complex I, the first enzyme complex in the electron transport chain of mitochondria. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. A mutation in this gene was found in an individual with Leigh syndrome. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.677); Leigh syndrome (0.674); mitochondrial complex I deficiency, nuclear type 22 (0.668); type 2 diabetes mellitus (0.620); diabetes mellitus (0.578)
- **Europe PMC papers**: 1163
- **Why important**: NDUFA10 is a component of mitochondrial respiratory-chain complex I and is connected in the module to ATP5PB and CARM1. It is present in the globally corrected pathway terms (KEGG Parkinson disease - Homo sapiens (human); q_global = 0.0122), (KEGG Prion disease - Homo sapiens (human); q_global = 0.0144), (KEGG Huntington disease - Homo sapiens (human); q_global = 0.0169), (KEGG Alzheimer disease - Homo sapiens (human); q_global = 0.0228), and (KEGG Pathways of neurodegeneration - multiple diseases - Homo sapiens (human); q_global = 0.0379) and in the matching supplementary STRING terms (STRING KEGG Alzheimer disease; within-query FDR = 0.0019) through (STRING KEGG Amyotrophic lateral sclerosis; within-query FDR = 0.0023). HPA indicates tissue enhancement in tongue, low cell-type specificity, and protein detection in both tissues. It has extensive literature support and disease associations with mitochondrial complex-I deficiency, Leigh syndrome, and diabetes mellitus.
- **Conclusion**: Established evidence supports NDUFA10 as a mitochondrial electron-transport component with clinically relevant deficiency associations. The module supports coordinated abundance with ATP5PB and proteasome genes, but does not establish that NDUFA10 drives proteostasis or that the module represents a neurodegenerative process.

#### CARM1

- **Related proteins** (co-abundance neighbors): NDUFA10 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coactivator associated arginine methyltransferase 1. This gene belongs to the protein arginine methyltransferase (PRMT) family. The encoded enzyme catalyzes the methylation of guanidino nitrogens of arginyl residues of proteins. The enzyme acts specifically on histones and other chromatin-associated proteins and is involved in regulation of gene expression. The enzyme may act in association with other proteins or within multi-protein complexes and m…
- **Diseases (Open Targets)**: neurodegenerative disease (0.491); lysosomal storage disease (0.258); mucositis (0.183); oral mucositis (0.183); hypothyroidism (0.160)
- **Europe PMC papers**: 3438
- **Why important**: CARM1 is the module's transcriptional and chromatin-regulatory component and is connected to NDUFA10 in the co-abundance graph. Its annotation supports protein arginine methylation, chromatin remodeling, transcriptional regulation, cell-population proliferation, estrogen-receptor signaling, and fat-cell differentiation. HPA reports tissue enhancement in skeletal muscle, no detection in immune cells, and detection in both tissues. It has the largest literature volume among the module genes and listed associations with neurodegenerative disease, lysosomal storage disease, mucositis, oral mucositis, and hypothyroidism, although it is absent from the enriched GO and KEGG terms and from the listed STRING and hu.MAP relationships.
- **Conclusion**: Established evidence supports CARM1 as a chromatin-associated methyltransferase and transcriptional regulator. Its association with the mitochondrial arm is a plausible regulatory hypothesis based on network position and co-abundance, not an established physical or functional link in this module.

## Module 4

**Tissue pair**: cervix_uterine and testis  
**Genes (5)**: ACOT7, ECI2, PCYT2, PSMC6, SUCLA2

### Function

The module has no globally significant GO or KEGG enrichment, so its function cannot be assigned from enrichment analysis alone. Its gene-level annotations nevertheless suggest a coordinated metabolic and cellular-maintenance program: ECI2 and ACOT7 participate in fatty-acid handling, PCYT2 in phospholipid synthesis, SUCLA2 in mitochondrial tricarboxylic-acid-cycle metabolism, and PSMC6 in proteasome-mediated protein turnover. The co-abundance pattern therefore most plausibly reflects lipid and mitochondrial metabolism with a proteostasis component, rather than a demonstrated single pathway. The metabolic interpretation remains biologically coherent but is inferential because no GO/KEGG term passed global correction.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are detected in testis and mostly detected in cervix_uterine. Most genes are tissue or cell-type enhanced rather than broadly expressed housekeeping genes. Late spermatids are a recurring enriched cell type, while liver, brain, skeletal muscle, tongue, and several specialized epithelial or immune-associated cell types also appear. Blood-cell specificity is generally low, with only ACOT7 showing group enrichment for NK cells and plasmacytoid dendritic cells. The shared module may therefore reflect a conserved metabolic state or shared cellular composition, particularly a germ-cell-related signal in testis, rather than blood contamination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship is present among the module genes, and no STRING functional-enrichment result is available. No hu.MAP complex contains multiple module members. The absence of these records means that the observed co-abundance links are not supported here as established physical interactions or membership in a known multiprotein complex. The genes may still be connected indirectly through metabolism, organelle demands, or cell state, but that interpretation is not demonstrated by STRING or hu.MAP.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared co-abundance pattern may be a new observation for the cervix_uterine and testis tissue pair, but the fact sheet does not establish novelty against all prior co-expression studies or independent cohorts. Its novelty is therefore provisional. The lack of STRING and hu.MAP support does not by itself prove a novel biological mechanism, because those resources emphasize curated, experimentally supported, or previously reported relationships. Established biology exists for each component separately, whereas the specific cross-tissue module organization and its proposed coordination require independent validation.

**Hypothesis.** Hypothesis: the module marks a conserved, tissue-adapted demand for lipid remodeling and mitochondrial energy metabolism, with proteasome activity helping maintain protein quality during metabolically intensive differentiation or specialized tissue function. In testis, the recurring late-spermatid signal suggests that germ-cell maturation could generate this coordinated metabolic state. In cervix_uterine, the same abundance pattern may arise from a metabolically similar cell population or physiological state rather than from a shared physical complex. This hypothesis should be tested using cell-resolved expression, protein abundance, and independent tissue cohorts.

### Important genes

#### PCYT2

- **Related proteins** (co-abundance neighbors): ECI2 (0.84), SUCLA2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphate cytidylyltransferase 2, ethanolamine. This gene encodes an enzyme that catalyzes the formation of CDP-ethanolamine from CTP and phosphoethanolamine in the Kennedy pathway of phospholipid synthesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010].
- **Diseases (Open Targets)**: spastic paraplegia 82, autosomal recessive (0.771); complex hereditary spastic paraplegia (0.554); neurodegenerative disease (0.542); Global developmental delay (0.462); Intellectual disability (0.462)
- **Europe PMC papers**: 4199
- **Why important**: PCYT2 is a central bridge in the module, connected to ECI2 and SUCLA2, and its function in phosphatidylethanolamine biosynthesis provides a direct link between membrane lipid production and mitochondrial metabolism. It is tissue enhanced in liver and testis, is associated with late spermatids, is detected in both tissues, has extensive literature coverage, and has disease associations involving hereditary spastic paraplegia and neurodegenerative disease.
- **Conclusion**: Established evidence supports PCYT2 as a phospholipid-biosynthesis enzyme and a strong candidate for linking membrane composition to the metabolic state represented by the module. Its role as the organizing biochemical driver of this particular co-abundance module is a hypothesis, not an established conclusion.

#### ECI2

- **Related proteins** (co-abundance neighbors): ACOT7 (0.87), PCYT2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Peroxisomes, Mitochondria; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: enoyl-CoA delta isomerase 2. This gene encodes a member of the hydratase/isomerase superfamily. The protein encoded is a key mitochondrial enzyme involved in beta-oxidation of unsaturated fatty acids. It catalyzes the transformation of 3-cis and 3-trans-enoyl-CoA esters arising during the stepwise degradation of cis-, mono-, and polyunsaturated fatty acids to the 2-trans-enoyl-CoA intermediates. Alternatively spliced transcri…
- **Diseases (Open Targets)**: thyroiditis (0.247); glomerulonephritis (0.161); nephritis (0.141); Abnormality of the skeletal system (0.140); brain aneurysm (0.138)
- **Europe PMC papers**: 516
- **Why important**: ECI2 is one of the two more connected module members and links ACOT7 with PCYT2. It encodes a mitochondrial and peroxisomal enoyl-CoA isomerase involved in beta-oxidation of unsaturated fatty acids. Its liver-enhanced expression, detection in both tissues, and disease associations involving thyroiditis, glomerulonephritis, nephritis, skeletal abnormalities, and brain aneurysm make it informative for interpreting the module as a lipid-use program.
- **Conclusion**: Established evidence supports ECI2 as a fatty-acid beta-oxidation enzyme and supports its relevance to the module's metabolic interpretation. Whether ECI2 drives the shared tissue-pair signal, rather than simply tracking cellular energy demand, remains unresolved.

#### ACOT7

- **Related proteins** (co-abundance neighbors): ECI2 (0.87), PSMC6 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA thioesterase 7. This gene encodes a member of the acyl coenzyme family. The encoded protein hydrolyzes the CoA thioester of palmitoyl-CoA and other long-chain fatty acids. Decreased expression of this gene may be associated with mesial temporal lobe epilepsy. Alternatively spliced transcript variants encoding distinct isoforms with different subcellular locations have been characterized. [provided by RefSeq, Jul …
- **Diseases (Open Targets)**: alcohol drinking (0.233); stroke disorder (0.173); diabetic ketoacidosis (0.114); Alzheimer disease (0.090); hepatocellular carcinoma (0.085)
- **Europe PMC papers**: 804
- **Why important**: ACOT7 is a highly connected node relative to the module and links ECI2 with PSMC6. It hydrolyzes palmitoyl-CoA and other long-chain fatty-acyl-CoA molecules, providing a plausible control point for fatty-acid and coenzyme-A balance. It is brain enhanced, associated with several specialized cell types including late spermatids, and has substantial literature coverage and disease associations involving epilepsy, stroke, Alzheimer disease, diabetic ketoacidosis, and hepatocellular carcinoma.
- **Conclusion**: Established evidence supports ACOT7 as a regulator of fatty-acyl-CoA availability. Its network position makes it a plausible metabolic connector, but the module does not establish that its enzymatic activity is coordinated directly with proteasome activity or that it explains the cervix_uterine signal.

#### SUCLA2

- **Related proteins** (co-abundance neighbors): PCYT2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase ADP-forming subunit beta. Succinyl-CoA synthetase (SCS) is a mitochondrial matrix enzyme that acts as a heterodimer, being composed of an invariant alpha subunit and a substrate-specific beta subunit. The protein encoded by this gene is an ATP-specific SCS beta subunit that dimerizes with the SCS alpha subunit to form SCS-A, an essential component of the tricarboxylic acid cycle. SCS-A hydrolyzes ATP to convert succinate t…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome, encephalomyopathic form with methylmalonic aciduria (0.816); mitochondrial DNA depletion syndrome, encephalomyopathic form (0.581); neurodegenerative disease (0.485); mitochondrial disease (0.374); disease of peritoneum (0.372)
- **Europe PMC papers**: 1440
- **Why important**: SUCLA2 connects to PCYT2 and contributes a mitochondrial tricarboxylic-acid-cycle function to the module. It encodes the ATP-specific beta subunit of succinyl-CoA synthetase, is enhanced in skeletal muscle and tongue, is associated with early and late spermatids, is detected in both tissues, and has well-established disease links to mitochondrial DNA depletion syndromes and other mitochondrial disorders.
- **Conclusion**: Established evidence supports SUCLA2 as a mitochondrial energy-metabolism component with important human disease relevance. Its presence strengthens the interpretation of energetic support for lipid and membrane metabolism, while its precise contribution to the shared co-abundance pattern remains a hypothesis.

#### PSMC6

- **Related proteins** (co-abundance neighbors): ACOT7 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 6. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.606); mantle cell lymphoma (0.542); neoplasm (0.528); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 748
- **Why important**: PSMC6 is connected to ACOT7 and contributes a proteasome ATPase function that broadens the module beyond intermediary metabolism. It has low tissue specificity, is detected in both tissues, has an annotation related to proteasomal protein catabolism and oxidative-stress response, and has disease associations involving plasma-cell myeloma, mantle-cell lymphoma, neoplasia, HIV infection, and amyloidosis.
- **Conclusion**: Established evidence supports PSMC6 as a component of proteasome-dependent protein quality control. Its inclusion suggests that the module may track a broader metabolically demanding or stress-adapted cellular state, but a direct mechanistic connection between PSMC6 and the lipid-metabolism genes is not established by the available interaction resources.

## Module 5

**Tissue pair**: cervix_uterine and testis  
**Genes (7)**: CDO1, KRT10, KRT14, KRT16, KRT2, KRT1, KRT5

### Function

The module is best interpreted as a stratified epithelial keratin and cornified-envelope program. The primary GO/KEGG evidence is highly coherent: keratin filament, intermediate-filament organization, keratinocyte and epidermal differentiation, cornified-envelope formation, keratinization, epithelial development, and structural cytoskeletal activity are all supported by globally corrected terms (26 globally significant GO/KEGG terms, q_global 1.64e-08–0.0307; see the table). Most of the functional signal is carried by KRT1, KRT10, KRT14, KRT16, KRT2, and KRT5, while CDO1 contributes to the broad organ-development term (GO:BP animal organ development; q_global = 0.00995). The network therefore reflects epithelial structural integrity and differentiation rather than a general metabolic or immune process. Cadherin signaling (KEGG Cadherin signaling - Homo sapiens (human); q_global = 7.88e-05) is compatible with epithelial adhesion, but the module does not establish a specific signaling mechanism.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary identifies only one secreted gene, and the individual proteins are predominantly intracellular intermediate-filament or nuclear proteins. It is also not primarily a blood-cell module. Although some genes show immune-cell enhancement or enrichment, the dominant HPA pattern is tissue and cell-type enrichment for skin, cervix, vagina, suprabasal keratinocytes, and basal keratinocytes. The composition is therefore strongly epithelial and keratinocyte-like. The shared cervix_uterine and testis signal may reflect epithelial or keratinizing cell content, tissue sampling composition, or contamination by an epithelial compartment rather than a program intrinsic to germ cells. Protein detection supports this caution: several proteins are detected in cervix_uterine but none are detected in testis in the supplied HPA evidence. The absence of testis protein detection does not disprove transcript-level co-abundance, but it weakens an interpretation as a testis-specific protein program.

**GO/KEGG enrichment**: 26 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC keratin filament | 1.64e-08 | KRT1, KRT10, KRT14, KRT16, KRT2, KRT5 |
| GO:BP intermediate filament organization | 6.53e-08 | KRT1, KRT10, KRT14, KRT16, KRT2, KRT5 |
| GO:BP intermediate filament-based process | 1.13e-07 | KRT1, KRT10, KRT14, KRT16, KRT2, KRT5 |
| GO:BP intermediate filament cytoskeleton organization | 1.13e-07 | KRT1, KRT10, KRT14, KRT16, KRT2, KRT5 |
| GO:BP keratinocyte differentiation | 6.01e-07 | KRT1, KRT10, KRT14, KRT16, KRT2, KRT5 |
| GO:CC intermediate filament | 8.52e-07 | KRT1, KRT10, KRT14, KRT16, KRT2, KRT5 |
| GO:BP epidermal cell differentiation | 1.59e-06 | KRT1, KRT10, KRT14, KRT16, KRT2, KRT5 |
| GO:CC intermediate filament cytoskeleton | 2.11e-06 | KRT1, KRT10, KRT14, KRT16, KRT2, KRT5 |
| GO:MF structural constituent of skin epidermis | 8.12e-06 | KRT1, KRT10, KRT2, KRT5 |
| KEGG Cornified envelope formation - Homo sapiens (human) | 8.54e-06 | KRT1, KRT10, KRT14, KRT16, KRT2, KRT5 |
| GO:CC cornified envelope | 9.52e-06 | KRT1, KRT10, KRT14, KRT16, KRT2 |
| GO:BP skin development | 1.52e-05 | KRT1, KRT10, KRT14, KRT16, KRT2, KRT5 |
| GO:BP epidermis development | 1.82e-05 | KRT1, KRT10, KRT14, KRT16, KRT2, KRT5 |
| GO:BP keratinization | 2.99e-05 | KRT1, KRT16, KRT2, KRT5 |
| KEGG Cadherin signaling - Homo sapiens (human) | 7.88e-05 | KRT1, KRT10, KRT14, KRT16, KRT2, KRT5 |

### STRING and hu.MAP

STRING provides strong, established functional support for a keratin and intermediate-filament interpretation through the supplementary terms (12 supplementary STRING terms; within-query FDR 7.93e-09–4.62e-07), including keratin, intermediate filament, conserved rod-domain, and cornified-envelope annotations. The STRING pairwise network is especially coherent among KRT1, KRT10, KRT14, KRT16, KRT2, and KRT5, with the strongest relationships centered on known keratin partners. These STRING results are supplementary and should not be treated as globally corrected enrichment. hu.MAP independently places KRT14 and KRT16 together in two related complexes (hu.MAP huMAP3_14922.1) and (hu.MAP huMAP3_15329.1), although each complex contains additional keratins outside this module. Thus, the module is supported by known keratin-family relationships and partial overlap with known complexes, rather than representing an entirely unconnected interaction group. CDO1 has no supplied STRING partner and does not occur in the supplied hu.MAP complexes, so its co-abundance with KRT1 is more plausibly a tissue-state or cell-composition association than an established physical interaction.

**STRING interactions (score >= 0.7)**: 10 of 21 gene pairs: KRT1–KRT10 (0.999); KRT1–KRT2 (0.956); KRT1–KRT5 (0.923); KRT10–KRT16 (0.788); KRT10–KRT2 (0.904); KRT10–KRT5 (0.793); KRT14–KRT16 (0.868); KRT14–KRT5 (0.999); KRT16–KRT5 (0.861); KRT2–KRT5 (0.871)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Keratin (FDR = 7.93e-09, 6 genes); SMART Intermediate filament protein (FDR = 1.11e-08, 6 genes); Keyword Intermediate filament (FDR = 1.34e-08, 6 genes); NetworkNeighborAL Formation of the cornified envelope, and Serpin, conserved site (FDR = 1.39e-08, 6 genes); InterPro Intermediate filament protein, conserved site (FDR = 6.54e-08, 6 genes); InterPro Intermediate filament, rod domain (FDR = 6.54e-08, 6 genes); RCTM Formation of the cornified envelope (FDR = 7.65e-08, 6 genes); COMPARTMENTS Intermediate filament (FDR = 1.05e-07, 6 genes); HPO Abnormal blistering of the skin (FDR = 1.32e-07, 6 genes); Component Intermediate filament (FDR = 1.9e-07, 6 genes); Component Keratin filament (FDR = 4.51e-07, 5 genes); COMPARTMENTS Keratin filament (FDR = 4.62e-07, 5 genes); PMID (2025) Mass spectrometric detection of keratins in tear fluid. (FDR = 5.93e-07, 6 genes); PMID (2023) FAM3CILEI protein is elevated in psoriatic lesions and triggers psoriasiform hyperproliferation in mice. (FDR = 5.93e-07, 6 genes); PMID (2022) A metatranscriptomic approach to explore longitudinal tissue specimens from non-healing diabetes related foot ulcers. (FDR = 5.93e-07, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14922.1 (KRT14, KRT16; 2/7); huMAP3_15329.1 (KRT14, KRT16; 2/8)

### Novelty

The module is unlikely to be a wholly new molecular mechanism because its principal genes form a canonical keratin differentiation program, its central pairings are already represented in STRING, and KRT14–KRT16 are represented in hu.MAP complexes (hu.MAP huMAP3_14922.1) and (hu.MAP huMAP3_15329.1). A potentially novel aspect is the reproducible co-abundance of this epithelial program across cervix_uterine and testis, particularly the inclusion of CDO1, but the supplied evidence does not establish that this cross-tissue association is mechanistically new. Absence of CDO1 from the supplied STRING and hu.MAP evidence is not sufficient to claim novelty. A defensible conclusion is that the module is a new tissue-pair observation or network-context observation, not a newly discovered keratin complex or biological pathway.

**Hypothesis.** Hypothesis: the shared module marks abundance of a keratinizing epithelial cell state in both tissue groups. In that state, basal epithelial structure involving KRT5 and KRT14 transitions toward suprabasal and cornified differentiation involving KRT1, KRT10, KRT2, and KRT16, producing the intermediate-filament and cornified-envelope signature observed in (14 globally significant GO/KEGG terms, q_global 1.64e-08–2.99e-05; see the table). CDO1 may track a broader tissue or cellular state associated with this program, but its role in the module is presently unclear. This hypothesis predicts that cell-type deconvolution, microscopy, or spatial measurements would localize most module expression to epithelial or keratinocyte-like cells and would distinguish genuine testicular epithelial expression from sample-composition effects.

### Important genes

#### KRT1

- **Related proteins** (co-abundance neighbors): KRT14 (0.93), KRT10 (0.89), KRT16 (0.88), KRT5 (0.83), CDO1 (0.83); STRING partners: KRT10 (0.999), KRT2 (0.956), KRT5 (0.923)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 is the most connected module gene and has the greatest weighted network strength in the supplied subgraph. It participates in nearly all primary enrichment terms, including keratin filament, intermediate-filament organization, keratinocyte differentiation, cornified-envelope formation, and epithelial development (26 globally significant GO/KEGG terms, q_global 1.64e-08–0.0307; see the table). HPA assigns it to skin and suprabasal keratinocytes, and the supplied annotation describes its partnership with KRT10 in differentiated stratified epithelium. Its disease associations include several inherited keratinization disorders, and its literature volume is substantial.
- **Conclusion**: Established evidence supports KRT1 as a central structural marker of the differentiated epithelial state represented by this module. It is a strong anchor gene for interpreting the module, but the network does not by itself show that KRT1 initiates the program or drives the cross-tissue association.

#### KRT5

- **Related proteins** (co-abundance neighbors): KRT14 (0.96), KRT10 (0.93), KRT1 (0.83); STRING partners: KRT1 (0.923), KRT10 (0.793), KRT14 (0.999), KRT16 (0.861), KRT2 (0.871)
- **HPA**: Group enriched; Group enriched; blood Immune cell enriched; location Intermediate filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 5. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the basal layer of the epidermis with family member KRT14. Mutations in t…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 2C, localized (0.768); epidermolysis bullosa simplex 2A, generalized severe (0.761); epidermolysis bullosa simplex 2B, generalized intermediate (0.761); epidermolysis bullosa simplex 2F, with mottled pigmentation (0.729); Dowling-Degos disease 1 (0.697)
- **Europe PMC papers**: 7044
- **Why important**: KRT5 is a central connector linking KRT14 with multiple other keratins in the module and is represented across the primary filament, differentiation, cornification, and epithelial terms (26 globally significant GO/KEGG terms, q_global 1.64e-08–0.0307; see the table). HPA places it in cervix, skin, and vagina and in basal and suprabasal epithelial populations. The supplied annotation identifies KRT5 with basal-layer epithelium and its heterotypic partnership with KRT14. Its disease associations include multiple forms of epidermolysis bullosa and related epithelial fragility disorders, with a substantial literature base.
- **Conclusion**: Established evidence supports KRT5 as a basal epithelial cytoskeletal component and a biologically important bridge between basal and differentiated keratin programs. Its co-abundance here is consistent with epithelial cell-state composition; it does not prove a disease process in either tissue.

#### KRT14

- **Related proteins** (co-abundance neighbors): KRT5 (0.96), KRT10 (0.94), KRT1 (0.93), KRT2 (0.86); STRING partners: KRT16 (0.868), KRT5 (0.999)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Intermediate filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_14922.1, huMAP3_15329.1
- **Function (MyGene.info)**: keratin 14. This gene encodes a member of the keratin family, the most diverse group of intermediate filaments. This gene product, a type I keratin, is usually found as a heterotetramer with two keratin 5 molecules, a type II keratin. Together they form the cytoskeleton of epithelial cells. Mutations in the genes for these keratins are associated with epidermolysis bullosa simplex. At least one pseudogene has…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 1A, generalized severe (0.823); epidermolysis bullosa simplex 1C, localized (0.818); epidermolysis bullosa simplex 1B, generalized intermediate (0.802); epidermolysis bullosa simplex 1D, generalized, intermediate or severe, autosomal recessive (0.759); Naegeli-Franceschetti-Jadassohn syndrome (0.759)
- **Europe PMC papers**: 6348
- **Why important**: KRT14 has strong connectivity and is tightly linked to KRT5, KRT1, KRT10, and KRT2 in the module. It contributes to the primary intermediate-filament, epithelial-differentiation, and cornified-envelope evidence (26 globally significant GO/KEGG terms, q_global 1.64e-08–0.0307; see the table). HPA assigns it to skin and basal or suprabasal keratinocyte populations and detects it in cervix_uterine but not testis. It is present in both hu.MAP complexes (hu.MAP huMAP3_14922.1) and (hu.MAP huMAP3_15329.1), and its supplied disease associations include several epidermolysis bullosa simplex disorders. Its literature volume is substantial.
- **Conclusion**: Established evidence supports KRT14 as a basal epithelial intermediate-filament partner, with independent complex support from hu.MAP. A reasonable hypothesis is that KRT14 helps identify the epithelial structural compartment underlying the shared module, but the data do not establish a tissue-specific causal role.

#### KRT10

- **Related proteins** (co-abundance neighbors): KRT14 (0.94), KRT5 (0.93), KRT16 (0.90), KRT1 (0.89); STRING partners: KRT1 (0.999), KRT16 (0.788), KRT2 (0.904), KRT5 (0.793)
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 10. This gene encodes a member of the type I (acidic) cytokeratin family, which belongs to the superfamily of intermediate filament (IF) proteins. Keratins are heteropolymeric structural proteins which form the intermediate filament. These filaments, along with actin microfilaments and microtubules, compose the cytoskeleton of epithelial cells. Mutations in this gene are associated with epidermolytic …
- **Diseases (Open Targets)**: epidermolytic hyperkeratosis 2A, autosomal dominant (0.787); epidermolytic ichthyosis (0.772); congenital reticular ichthyosiform erythroderma (0.727); ichthyosis, annular epidermolytic 1 (0.647); annular epidermolytic ichthyosis (0.642)
- **Europe PMC papers**: 2736
- **Why important**: KRT10 is highly connected to the major keratin genes and is included in the primary evidence for keratin filaments, keratinocyte differentiation, cornification, and epithelial development (26 globally significant GO/KEGG terms, q_global 1.64e-08–0.0307; see the table). HPA assigns it to skin and suprabasal keratinocytes, while its supplied annotation describes a type I cytokeratin involved in intermediate-filament structure and cornification. It has established associations with epidermolytic hyperkeratosis and related ichthyoses, together with a substantial literature volume.
- **Conclusion**: Established evidence supports KRT10 as a marker of suprabasal differentiation within the module. Its presence strengthens the interpretation of a maturation or cornification program, but co-abundance cannot determine whether differentiation is occurring in the tissues or is produced by differing epithelial content.

#### KRT16

- **Related proteins** (co-abundance neighbors): KRT10 (0.90), KRT1 (0.88); STRING partners: KRT10 (0.788), KRT14 (0.868), KRT5 (0.861)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14922.1, huMAP3_15329.1
- **Function (MyGene.info)**: keratin 16. The protein encoded by this gene is a member of the keratin gene family. The keratins are intermediate filament proteins responsible for the structural integrity of epithelial cells and are subdivided into cytokeratins and hair keratins. Most of the type I cytokeratins consist of acidic proteins which are arranged in pairs of heterotypic keratin chains and are clustered in a region of chromosome 1…
- **Diseases (Open Targets)**: pachyonychia congenita (0.777); palmoplantar keratoderma, nonepidermolytic, focal 1 (0.666); pachyonychia congenita 1 (0.657); diffuse nonepidermolytic palmoplantar keratoderma (0.556); focal palmoplantar keratoderma (0.463)
- **Europe PMC papers**: 1935
- **Why important**: KRT16 connects the differentiated keratin genes and is linked to KRT14 and KRT5 through STRING as well as to KRT14 in both hu.MAP complexes (hu.MAP huMAP3_14922.1) and (hu.MAP huMAP3_15329.1). It contributes to the primary keratin, intermediate-filament, epithelial-differentiation, cornification, and cytoskeletal terms (26 globally significant GO/KEGG terms, q_global 1.64e-08–0.0307; see the table). HPA describes it as tissue-enhanced in cervix, esophagus, vagina, and skin and enhanced in several epithelial cell populations. Its supplied disease associations include pachyonychia congenita and palmoplantar keratoderma, with established but smaller literature volume than the most extensively studied keratins.
- **Conclusion**: Established evidence supports KRT16 as an epithelial intermediate-filament component associated with keratinocyte differentiation and tissue remodeling. Its complex and STRING relationships reinforce the module's known keratin architecture. Whether it indicates a stress, repair, or disease-associated epithelial state in these samples remains a hypothesis.
