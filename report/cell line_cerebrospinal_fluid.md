# Conserved co-abundance modules: cell line and cerebrospinal_fluid

## Module 0

**Tissue pair**: cell line and cerebrospinal_fluid  
**Genes (13)**: SLC3A2, ASPH, ATP1B1, ADAMTSL4, CPD, EXTL2, FSTL5, FUCA1, GSN, MDGA2, NEGR1, PTPRF, ROBO1

### Function

The module has no GO or KEGG term that passed global correction, and STRING functional enrichment is absent. Its biology is therefore inferred from the gene identities and network context rather than from significant pathway enrichment. The strongest coherent signal is a neuronal and extracellular-cell-surface theme: MDGA2, FSTL5, NEGR1, PTPRF and ROBO1 are associated with neuronal development, synaptic organization, cell adhesion, neuronal migration or axon guidance. Other members contribute membrane transport, glycan and proteoglycan metabolism, extracellular-matrix biology, proteolysis, calcium handling and actin remodeling. The sparse topology, with MDGA2 and FSTL5 as the principal local hubs, is consistent with a coordinated cell-surface or extracellular-interface program, but it does not establish a single biochemical pathway.

**Cell composition.** The module is mixed rather than uniformly neuronal. HPA annotations show brain and retina enrichment for several genes and frequent enhancement in excitatory, inhibitory and other brain neurons, supporting a neural component relevant to cerebrospinal fluid. At the same time, several genes are broadly expressed or associated with non-neural cell types, including trophoblast, epithelial, adipose, kidney, cardiac and gastrointestinal populations. Several members are secreted or extracellular, including FSTL5, ADAMTSL4 and GSN, and the HPA summary identifies a substantial secreted fraction. Immune-cell annotations are also mixed: some genes are enhanced in neutrophils or other blood-cell populations, whereas others are not detected in immune cells. Thus, the shared signal could reflect neural material, extracellular protein abundance, shared cell types, or a blood or cellular-composition contribution in the samples; the current HPA evidence does not justify assigning it exclusively to neurons. HPA protein-detection evidence is unavailable for the specified cell-line and cerebrospinal-fluid contexts.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair reaches the reported STRING interaction threshold, and no STRING functional enrichment is present. No hu.MAP complex contains at least two module members. Consequently, the observed co-abundance relationships are not supported here by high-confidence curated or predicted physical associations, nor by a recognized protein complex. The strongest module edges are internal statistical co-abundance links, especially those centered on MDGA2 and FSTL5; they should be treated as relationships requiring experimental validation rather than as established direct interactions. Known functions of individual proteins still provide biological context, but they do not convert the module edges into physical binding evidence.

**STRING interactions (score >= 0.7)**: 0 of 78 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel co-abundance association, but the data do not prove a new biological mechanism. The absence of STRING interactions and hu.MAP complexes means that this exact assembled module is not represented by those resources, while also reflecting the possibility of incomplete database coverage, tissue-specific regulation, extracellular carryover or indirect co-regulation. The lack of globally significant GO or KEGG enrichment limits claims of a newly discovered pathway. A defensible conclusion is that the coordinated abundance pattern appears under-characterized and merits replication in independent cell-line and cerebrospinal-fluid datasets, followed by protein-level and cell-composition controls.

**Hypothesis.** Hypothesis: the module represents a context-dependent extracellular and neuronal-interface program in which adhesion and guidance proteins, glycan or proteoglycan processing, membrane transport, calcium-related functions and cytoskeletal remodeling vary together. In cerebrospinal fluid, this could arise from release or turnover of neuronal and extracellular proteins; in cell-line material, it could reflect a shared differentiation, membrane-trafficking or extracellular-matrix state. A competing hypothesis is that the pattern is driven partly by variable contribution from blood-derived or other non-neural cells, especially given the immune-cell annotations and secreted proteins. Testing should distinguish these models using matched cell-composition markers, targeted protein measurements and perturbation of candidate adhesion or glycan-processing components.

### Important genes

#### MDGA2

- **Related proteins** (co-abundance neighbors): SLC3A2 (0.99), PTPRF (0.95), EXTL2 (0.93), ATP1B1 (0.92), FUCA1 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MAM domain containing glycosylphosphatidylinositol anchor 2. Predicted to be involved in regulation of presynapse assembly; regulation of synaptic membrane adhesion; and spinal cord motor neuron differentiation. Predicted to act upstream of or within neuron migration and pattern specification process. Predicted to be located in extracellular region and plasma membrane. Predicted to be active in GABA-ergic synapse and glutamatergic synapse. [provided by Alli…
- **Diseases (Open Targets)**: dermatophytosis (0.412); attention deficit-hyperactivity disorder (0.384); substance abuse (0.366); Abnormality of the skeletal system (0.360); smoking initiation (0.354)
- **Europe PMC papers**: 402
- **Why important**: MDGA2 is the principal network hub, linking SLC3A2, PTPRF, EXTL2, ATP1B1 and FUCA1. HPA places it in brain and retina-enriched expression with enhancement in several neuronal cell types and no detection in immune cells. Its curated functional description connects it to presynapse assembly, synaptic membrane adhesion, neuron migration and synaptic transmission. It also has substantial literature and disease-association coverage, making it a strong anchor for the neural interpretation.
- **Conclusion**: Established evidence supports MDGA2 as a neural cell-surface and synaptic-adhesion candidate with the most central position in this module. It is not established that its module edges are direct interactions or that MDGA2 drives the shared abundance pattern. The hypothesis that MDGA2 organizes the module around neuronal adhesion should be tested experimentally.

#### FSTL5

- **Related proteins** (co-abundance neighbors): FUCA1 (0.95), CPD (0.90), GSN (0.88), ASPH (0.84), ROBO1 (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: follistatin like 5. Predicted to enable calcium ion binding activity. Predicted to be involved in cell differentiation. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: placenta praevia (0.341); retinal degeneration (0.332); Jaundice (0.299); ovarian neoplasm (0.270); Abnormality of the skeletal system (0.250)
- **Europe PMC papers**: 429
- **Why important**: FSTL5 is a co-hub with links to FUCA1, CPD, GSN, ASPH and ROBO1. It is brain and retina group-enriched, enhanced in multiple neural cell types, and annotated as secreted in brain. Its extracellular location and calcium-binding prediction provide a plausible bridge between neuronal extracellular biology and the other module proteins. It has disease associations involving retinal degeneration and other phenotypes, with a moderate literature base.
- **Conclusion**: Established evidence supports FSTL5 as an extracellular, brain-associated protein and as a central statistical connector in the module. The proposed role as an organizer of a cerebrospinal-fluid extracellular program remains a hypothesis because neither STRING nor hu.MAP supports direct complex membership here.

#### NEGR1

- **Related proteins** (co-abundance neighbors): ADAMTSL4 (0.98); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles, Actin filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neuronal growth regulator 1. Predicted to act upstream of or within several processes, including feeding behavior; locomotory behavior; and positive regulation of neuron projection development. Predicted to be located in extracellular region and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: major depressive disorder (0.585); intelligence (0.571); obesity disorder (0.547); Abnormality of the skeletal system (0.539); schizophrenia (0.505)
- **Europe PMC papers**: 1724
- **Why important**: NEGR1 is brain tissue-enhanced, enriched or enhanced across several neuronal cell types, and absent from immune-cell detection in the supplied HPA evidence. Its annotations include heterophilic cell-cell adhesion, regulation of synapse assembly, neuron projection development and plasma-membrane localization. It connects the module to ADAMTSL4 and has extensive literature and disease-association coverage, including psychiatric and metabolic phenotypes.
- **Conclusion**: Established evidence supports NEGR1 as a neuronal adhesion and synapse-related candidate that strengthens the neural interpretation. Its low local degree means it is not a topological hub, and the data do not establish that it mediates the module. A testable hypothesis is that NEGR1 marks a neuronal extracellular-adhesion state shared across the two sample contexts.

#### FUCA1

- **Related proteins** (co-abundance neighbors): FSTL5 (0.95), ADAMTSL4 (0.83), MDGA2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alpha-L-fucosidase 1. The protein encoded by this gene is a lysosomal enzyme involved in the degradation of fucose-containing glycoproteins and glycolipids. Mutations in this gene are associated with fucosidosis (FUCA1D), which is an autosomal recessive lysosomal storage disease. A pseudogene of this locus is present on chr 2.[provided by RefSeq, Oct 2009].
- **Diseases (Open Targets)**: fucosidosis (0.834); hereditary disease (0.415); Intellectual disability (0.371); Seizure (0.370); Abnormality of the nervous system (0.340)
- **Europe PMC papers**: 1004
- **Why important**: FUCA1 connects the two prominent local regions through FSTL5, ADAMTSL4 and MDGA2. It encodes a lysosomal alpha-L-fucosidase involved in degradation of fucose-containing glycoproteins and glycolipids, with annotations covering carbohydrate and glycoside catabolism. Its disease association with fucosidosis is well established and it has a substantial literature base. Its broad tissue profile and intracellular or vesicular localization provide a possible processing component rather than a specifically neuronal marker.
- **Conclusion**: Established evidence supports FUCA1 as a glycan-degradation enzyme and a topological bridge between extracellular or adhesion-related genes. Its participation in a neural extracellular mechanism is not established and may instead reflect general vesicular or cellular processing, sample composition or indirect co-regulation.

#### PTPRF

- **Related proteins** (co-abundance neighbors): MDGA2 (0.95); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein tyrosine phosphatase receptor type F. The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP possesses an extracellular region, a single transmembrane region, and two tandem intracytoplasmic catalytic domains, and thu…
- **Diseases (Open Targets)**: breasts and/or nipples, aplasia or hypoplasia of, 2 (0.505); smoking initiation (0.420); attention deficit-hyperactivity disorder (0.419); isolated congenital breast hypoplasia/aplasia (0.370); substance-related disorder (0.329)
- **Europe PMC papers**: 4709
- **Why important**: PTPRF is directly connected to the module hub MDGA2 and encodes a receptor-type protein tyrosine phosphatase with extracellular, transmembrane and intracellular catalytic regions. Its annotations include cell adhesion, signal transduction, cell migration and nervous-system development. It has a large literature base and disease associations involving developmental and behavioral phenotypes, making it a biologically plausible signaling counterpart to MDGA2.
- **Conclusion**: Established evidence supports PTPRF as a cell-surface adhesion and signaling regulator compatible with the module's inferred interface biology. The co-abundance link to MDGA2 does not demonstrate receptor binding or signaling dependence. A mechanistic connection between the two proteins remains a hypothesis requiring interaction and perturbation studies.

## Module 1

**Tissue pair**: cell line and cerebrospinal_fluid  
**Genes (21)**: A2M, AEBP1, SMPDL3A, ASTN2, CDH5, CLMP, F5, FBLN1, FN1, FREM2, SELL, MAN1A1, NAGA, PODXL2, PLXNB3, PTPRK, SPINT2, SPARCL1, TMEM132C, SPOCK3, VCAM1

### Function

No GO or KEGG term passed global correction, so there is no globally significant pathway assignment for this module. The most coherent biological interpretation is an extracellular and cell-surface adhesion module linking endothelial or vascular-junction biology, extracellular-matrix organization, leukocyte trafficking, and tissue-interface structure. This interpretation is supported by SELL as the network hub and by the functions of CDH5, VCAM1, FN1, FBLN1, PODXL2, PTPRK, FREM2, SPARCL1, and PLXNB3. The module therefore appears more consistent with coordinated abundance of adhesion, matrix, vascular-interface, and immune-trafficking proteins than with a defined intracellular pathway. The absence of a globally significant GO or KEGG term does not invalidate the module.

**Cell composition.** The module is strongly compatible with extracellular, vascular, stromal, and secreted-protein biology rather than a uniform neuronal or cell-line-specific program. Ten genes are annotated as secreted, secreted to blood, or secreted to extracellular matrix, including FN1, FBLN1, VCAM1, F5, A2M, SPARCL1, SPOCK3, SMPDL3A, and AEBP1. HPA tissue evidence is distributed across choroid plexus, blood vessel, liver, placenta, brain, adipose tissue, and lymphoid tissue. Single-cell evidence frequently points to fibroblasts, choroid plexus epithelial cells, oligodendrocyte progenitor cells, vascular smooth muscle cells, stromal cells, endothelial-related populations, and several myeloid or other blood-cell populations. Several genes are not detected or have low immune-cell specificity, but other genes show immune-cell enrichment or group enrichment. Thus, the shared signal may reflect extracellular matrix and vascular or choroid-plexus interfaces, but it could also partly reflect blood-derived material, vascular contamination, or shared stromal and immune-associated cell types. HPA protein detection is unavailable for both sampled categories, so protein-level tissue localization cannot be confirmed from this fact sheet.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited but biologically coherent set of pairwise relationships. FN1 is connected to FBLN1, VCAM1, A2M, and CDH5; SELL is connected to VCAM1 and PODXL2; and CDH5 is connected to VCAM1. These relationships independently support extracellular-matrix, endothelial-adhesion, and leukocyte-trafficking biology. The remaining module edges are not represented by high-confidence STRING interactions in the supplied evidence, and STRING functional enrichment is absent. No hu.MAP complex contains multiple module members. Consequently, the module is not a known canonical multiprotein complex; it is better viewed as a co-abundance neighborhood containing a validated extracellular-adhesion core plus additional genes whose coordinated behavior may be tissue- or sample-context dependent.

**STRING interactions (score >= 0.7)**: 7 of 210 gene pairs: A2M–FN1 (0.851); CDH5–FN1 (0.704); CDH5–VCAM1 (0.806); FBLN1–FN1 (0.992); FN1–VCAM1 (0.983); PODXL2–SELL (0.704); SELL–VCAM1 (0.97)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be called a definitively new biological discovery. Its central biology is established: SELL mediates leukocyte rolling, CDH5 supports endothelial junctions, VCAM1 mediates leukocyte-endothelial adhesion, and FN1 and FBLN1 participate in extracellular matrix structure and adhesion. Several of these relationships are already supported by STRING, and the genes have substantial prior literature. The potentially novel aspect is the specific cross-context co-abundance configuration shared by cell line and cerebrospinal fluid, particularly the connection of established vascular and matrix genes with less-characterized or context-specific genes such as CLMP, TMEM132C, FREM2, and SPOCK3. However, absence from hu.MAP or absence of some edges from STRING does not establish novelty. Demonstrating novelty would require comparison with prior co-abundance modules, cerebrospinal-fluid proteomic studies, cell-line datasets, and independent replication.

**Hypothesis.** Mechanistic hypothesis: the module represents a shared tissue-interface program involving vascular or choroid-plexus-associated cells, extracellular-matrix remodeling, and regulated leukocyte interaction. In this model, FN1 and FBLN1 provide matrix scaffolding; CDH5 and VCAM1 mark endothelial-junction and inflammatory adhesion states; SELL and PODXL2 support leukocyte tethering or rolling; and SPINT2, A2M, SPOCK3, FREM2, and related genes modulate protease activity, matrix organization, or cell-migration cues. In cerebrospinal fluid, the signal could arise from choroid-plexus or vascular-interface material and circulating extracellular proteins rather than from neurons themselves. In the cell-line context, the same abundance pattern could reflect endothelial-like, stromal-like, or matrix-producing cells. This remains a hypothesis because the supplied data are co-abundance and annotation evidence, not perturbation or causal evidence.

### Important genes

#### SELL

- **Related proteins** (co-abundance neighbors): FBLN1 (0.99), CDH5 (0.93), VCAM1 (0.91), SPINT2 (0.90), PTPRK (0.89), SMPDL3A (0.88), FN1 (0.85), MAN1A1 (0.85), F5 (0.85), NAGA (0.84), A2M (0.84); STRING partners: PODXL2 (0.704), VCAM1 (0.97)
- **HPA**: Group enriched; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: selectin L. This gene encodes a cell surface adhesion molecule that belongs to a family of adhesion/homing receptors. The encoded protein contains a C-type lectin-like domain, a calcium-binding epidermal growth factor-like domain, and two short complement-like repeats. The gene product is required for binding and subsequent rolling of leucocytes on endothelial cells, facilitating their migration into secondar…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.367); asthma (0.304); lymphatic system disorder (0.286); ankylosing spondylitis (0.202); atrial fibrillation (0.189)
- **Europe PMC papers**: 14927
- **Why important**: SELL is the strongest network hub in the supplied module and connects to matrix, adhesion, signaling, and glycoprotein-associated neighbors. Its established function is leukocyte rolling and migration through a cell-surface adhesion receptor. HPA places it in lymphoid and bone-marrow-associated tissue and highlights neutrophils, while its literature volume is substantial. It is therefore the best candidate for coordinating the immune-trafficking aspect of the module.
- **Conclusion**: Established evidence supports SELL as a central leukocyte-adhesion component and as the principal network organizer. It is plausible, but unproven, that SELL abundance links blood-cell or vascular-interface variation to the rest of the module.

#### FN1

- **Related proteins** (co-abundance neighbors): SELL (0.85); STRING partners: A2M (0.851), CDH5 (0.704), FBLN1 (0.992), VCAM1 (0.983)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 is a major extracellular-matrix and plasma glycoprotein with very extensive literature. It is linked in STRING to FBLN1, VCAM1, CDH5, and A2M, connecting the matrix and vascular-adhesion portions of the module. HPA annotates it in blood vessel, liver, and placenta and as secreted to blood. Its established roles in cell adhesion, cell-matrix adhesion, migration, wound repair, coagulation, and host defense make it a strong functional anchor.
- **Conclusion**: Established evidence supports FN1 as an extracellular scaffold and circulating or tissue-interface marker. The module may reflect coordinated matrix and vascular remodeling, but the co-abundance data do not establish that FN1 drives the other genes.

#### VCAM1

- **Related proteins** (co-abundance neighbors): SELL (0.91), SPOCK3 (0.82); STRING partners: CDH5 (0.806), FN1 (0.983), SELL (0.97)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vascular cell adhesion molecule 1. This gene is a member of the Ig superfamily and encodes a cell surface sialoglycoprotein expressed by cytokine-activated endothelium. This type I membrane protein mediates leukocyte-endothelial cell adhesion and signal transduction, and may play a role in the development of artherosclerosis and rheumatoid arthritis. Three alternatively spliced transcripts encoding different isoforms have been desc…
- **Diseases (Open Targets)**: neurodegenerative disease (0.373); glaucoma (0.298); open-angle glaucoma (0.273); Crohn disease (0.192); neoplasm (0.118)
- **Europe PMC papers**: 13790
- **Why important**: VCAM1 is a well-established cytokine-inducible endothelial adhesion molecule that mediates leukocyte-endothelial interaction. It has strong STRING links to SELL, FN1, and CDH5, and HPA annotates it as secreted to blood, enriched in lymphoid tissue, and localized to cell junctions. Its disease associations include inflammatory and neurovascularly relevant conditions, making it informative for interpreting a cerebrospinal-fluid-associated module.
- **Conclusion**: Established evidence supports VCAM1 as an endothelial inflammatory-adhesion marker. A reasonable hypothesis is that its co-abundance with SELL and FN1 reflects vascular activation or barrier-interface remodeling, but activation cannot be inferred directly from this module.

#### FBLN1

- **Related proteins** (co-abundance neighbors): SELL (0.99), TMEM132C (0.95), CLMP (0.89); STRING partners: FN1 (0.992)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibulin 1. Fibulin 1 is a secreted glycoprotein that becomes incorporated into a fibrillar extracellular matrix. Calcium-binding is apparently required to mediate its binding to laminin and nidogen. It mediates platelet adhesion via binding fibrinogen. Four splice variants which differ in the 3' end have been identified. Each variant encodes a different isoform, but no functional distinctions have been ident…
- **Diseases (Open Targets)**: synpolydactyly type 2 (0.447); FBLN1-related developmental delay-central nervous system anomaly-syndactyly syndrome (0.377); synpolydactyly (0.371); adolescent idiopathic scoliosis (0.306); alcohol drinking (0.219)
- **Europe PMC papers**: 2655
- **Why important**: FBLN1 is a secreted extracellular-matrix glycoprotein and is the strongest STRING-connected partner of FN1 in the supplied evidence. It is especially notable because HPA identifies choroid plexus and several stromal or trophoblast populations, directly connecting it to a plausible cerebrospinal-fluid interface and matrix-producing cellular sources. Its known roles include matrix organization, laminin and nidogen binding, platelet adhesion, and integrin-related signaling.
- **Conclusion**: Established evidence supports FBLN1 as a matrix and tissue-interface component with particular relevance to choroid-plexus-associated biology. Its co-abundance with FN1 may mark matrix deposition or remodeling, although the direction and mechanism remain untested.

#### CDH5

- **Related proteins** (co-abundance neighbors): AEBP1 (0.94), SELL (0.93); STRING partners: FN1 (0.704), VCAM1 (0.806)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cadherin 5. This gene encodes a classical cadherin of the cadherin superfamily. The encoded preproprotein is proteolytically processed to generate the mature glycoprotein. This calcium-dependent cell-cell adhesion molecule is comprised of five extracellular cadherin repeats, a transmembrane region and a highly conserved cytoplasmic tail. Functioning as a classical cadherin by imparting to cells the ability to…
- **Diseases (Open Targets)**: hypertensive disorder (0.454); essential hypertension (0.324); morbid obesity (0.312); cornea transplantation (0.310); injury (0.304)
- **Europe PMC papers**: 16859
- **Why important**: CDH5 is a classical endothelial cadherin involved in adherens-junction assembly, endothelial morphogenesis, and cell-cell adhesion. It connects in STRING to VCAM1 and FN1, placing it at the intersection of endothelial junctions, inflammatory adhesion, and extracellular matrix. HPA supports vascular and endothelial-related cellular associations, including lymphatic endothelial cells and Kupffer cells. Its extensive literature makes its interpretation comparatively secure.
- **Conclusion**: Established evidence supports CDH5 as an endothelial-junction marker. The module may therefore include a vascular-barrier component, but the data do not prove that the cerebrospinal-fluid signal originates from intact endothelial cells or that barrier function is altered.

## Module 2

**Tissue pair**: cell line and cerebrospinal_fluid  
**Genes (13)**: APP, SERPINC1, APOD, APOM, BMP1, CDH13, ECM1, CHL1, NICOL1, PCDH19, PROS1, PTPRD, PTPRM

### Function

No GO or KEGG term passed global correction, and there are no supplementary STRING enrichment terms. Therefore, the module does not support a statistically established pathway-level annotation from enrichment analysis. Its gene-level composition instead points toward an extracellular and cell-surface interface linking lipid transport, plasma protease regulation, vascular biology, neural adhesion, and nervous-system signaling. The network contains a central NICOL1-centered neighborhood connecting APP, ECM1, CDH13, SERPINC1, and PROS1, alongside a neural adhesion branch involving PCDH19, CHL1, BMP1, and receptor phosphatases. These are biological interpretations of the genes and network, not globally significant GO or KEGG enrichment claims.

**Cell composition.** Most genes are secreted to blood, secreted to extracellular matrix, or associated with extracellular and membrane compartments. The module includes liver and hepatocyte-associated plasma proteins such as APOM, SERPINC1, and PROS1, as well as brain, choroid plexus, neuronal, glial, vascular, and endothelial associations. Several genes also show immune-cell enhancement or enrichment, including associations with B cells, plasmacytoid dendritic cells, basophils, monocytes, and T cells, while other genes are not detected in immune cells. This mixed profile argues against interpreting the module as a pure neuronal program. In cerebrospinal fluid, the shared signal could reflect circulating or locally produced extracellular proteins, choroid plexus and vascular interfaces, or shared cellular and sample-composition effects. The cell-line concordance may likewise capture broadly available extracellular or membrane-associated proteins rather than a tissue-exclusive biological process.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING-supported relationships are APOD with APOM, APOM with APP, and PROS1 with SERPINC1. These links provide limited support for a lipid-carrier and plasma-coagulation component within the module. The remaining co-abundance relationships are not represented by high-confidence STRING interactions in the supplied evidence, so co-abundance should not be treated as proof of direct physical binding or a single molecular complex. No hu.MAP complex contains multiple module members. Together, the evidence favors a mixed extracellular network or shared abundance environment rather than a known multiprotein complex.

**STRING interactions (score >= 0.7)**: 3 of 78 gene pairs: APOD–APOM (0.79); APOM–APP (0.754); PROS1–SERPINC1 (0.743)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared co-abundance pattern may be a new observation because the module combines neural adhesion and receptor-signaling proteins with plasma lipid and coagulation proteins, while having sparse STRING support and no multi-member hu.MAP complex. However, it cannot be called a definitively new biological mechanism from these data alone. Several individual genes and the three STRING relationships are already well studied, and the absence of a STRING or hu.MAP entry does not establish novelty. The defensible claim is that the cross-context co-abundance configuration is potentially novel and requires independent replication, control for blood and choroid-plexus contributions, and orthogonal protein or interaction measurements.

**Hypothesis.** Hypothesis: the module represents an extracellular cerebrovascular and choroid-plexus interface in which lipid-carrier proteins, coagulation regulators, adhesion molecules, and neural receptor proteins vary together. APOM and APOD could mark lipid transport or lipoprotein-associated extracellular material; SERPINC1 and PROS1 could mark anticoagulant balance; CDH13, PCDH19, CHL1, PTPRM, and PTPRD could connect that extracellular environment to vascular, glial, neuronal, or cell-adhesion states; and APP, ECM1, BMP1, and NICOL1 could contribute extracellular signaling, matrix, or proteolytic context. This hypothesis predicts that the module will be sensitive to blood contamination, choroid plexus and vascular abundance, and disease-related changes in extracellular transport or barrier biology. It does not imply that these proteins form one physical complex.

### Important genes

#### NICOL1

- **Related proteins** (co-abundance neighbors): APP (0.91), ECM1 (0.86), CDH13 (0.85), SERPINC1 (0.85), PROS1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NELL2 interacting cell ontogeny regulator 1. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: lagophthalmos (0.202); rectosigmoid junction neoplasm (0.088); pericarditis (0.088); non-syndromic male infertility due to sperm motility disorder (0.077); spermatogenic failure 55 (0.064)
- **Europe PMC papers**: 43
- **Why important**: NICOL1 is the network hub, linking APP, ECM1, CDH13, SERPINC1, and PROS1 with strong co-abundance relationships. It is brain-enhanced, secreted to blood, and annotated as an extracellular-region protein, making it a plausible integrator of the module's neural and plasma-facing components. Its direct functional annotation is comparatively limited and its literature volume is modest relative to several other module genes, which makes it especially informative for testing whether the hub is a genuine biological organizer or a context-specific abundance correlate.
- **Conclusion**: Established evidence: NICOL1 is the central co-abundance connector and has brain-enhanced and blood-secreted annotation. Hypothesis: NICOL1 may help couple extracellular neural or vascular biology to circulating coagulation and lipid-associated proteins. This proposed organizing role remains unproven because it lacks supplied STRING partners and hu.MAP support.

#### APOM

- **Related proteins** (co-abundance neighbors): PTPRM (0.98), BMP1 (0.87), CDH13 (0.85); STRING partners: APOD (0.79), APP (0.754)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein M. The protein encoded by this gene is an apolipoprotein and member of the lipocalin protein family. It is found associated with high density lipoproteins and to a lesser extent with low density lipoproteins and triglyceride-rich lipoproteins. The encoded protein is secreted through the plasma membrane but remains membrane-bound, where it is involved in lipid transport. Alternate splicing results in …
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.104); Sepsis (0.101); diabetes mellitus (0.099); liver cancer (0.096); Alzheimer disease (0.095)
- **Europe PMC papers**: 1712
- **Why important**: APOM connects to PTPRM, BMP1, and CDH13 in the module and has known STRING relationships with APOD and APP. It is a liver- and hepatocyte-associated secreted apolipoprotein involved in cholesterol efflux, lipoprotein remodeling, lipid transport, and protection against lipoprotein oxidation. Its disease associations include metabolic disease, sepsis, liver cancer, and Alzheimer disease, and it has substantial literature support. It is therefore a strong candidate for the plasma lipid-transport component of the module.
- **Conclusion**: Established evidence: APOM is a secreted liver-associated lipid carrier with relevant STRING links and well-described lipid functions. Hypothesis: APOM may be the principal circulating component that couples lipid status to neural, vascular, or choroid-plexus-associated proteins in this module. The co-abundance data do not establish that APOM directly regulates those proteins.

#### PCDH19

- **Related proteins** (co-abundance neighbors): APOD (0.97), CHL1 (0.89), BMP1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protocadherin 19. The protein encoded by this gene is a member of the delta-2 protocadherin subclass of the cadherin superfamily. The encoded protein is thought to be a calcium-dependent cell-adhesion protein that is primarily expressed in the brain. Mutations in this gene on human chromosome X are associated with sporadic infantile epileptic encephalopathy and to a female-restricted form of epilepsy (EFMR; also kn…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 9 (0.847); hereditary disease (0.548); Seizure (0.539); Bilateral tonic-clonic seizure (0.436); glycine encephalopathy (0.405)
- **Europe PMC papers**: 1354
- **Why important**: PCDH19 occupies a bridge position between APOD, CHL1, and BMP1 and is strongly associated with brain and multiple neuronal cell types. Its established functions include calcium-dependent cell adhesion and homophilic cell-cell adhesion. Mutations are associated with developmental and epileptic encephalopathy and seizure phenotypes, and the gene has substantial literature support. Its presence gives the module a clear neural-adhesion axis despite the absence of globally enriched GO or KEGG terms.
- **Conclusion**: Established evidence: PCDH19 is a brain-associated adhesion gene with disease relevance and co-abundance links to neural and extracellular proteins. Hypothesis: its abundance may report neuronal or glial surface organization within a broader extracellular-fluid signature. A direct connection to APOD, CHL1, or BMP1 is not established by the supplied interaction databases.

#### SERPINC1

- **Related proteins** (co-abundance neighbors): NICOL1 (0.85), PTPRD (0.84); STRING partners: PROS1 (0.743)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 links the NICOL1-centered network to PTPRD and has a high-confidence STRING relationship with PROS1. It is a liver- and hepatocyte-associated secreted plasma protein that inhibits thrombin and other activated coagulation proteases. Its disease associations include hereditary antithrombin deficiency and venous thromboembolic disease, with extensive literature support. It is important because it provides a concrete coagulation interpretation for part of the shared extracellular signal.
- **Conclusion**: Established evidence: SERPINC1 is a plasma anticoagulant with a known relationship to PROS1 and established thrombotic disease relevance. Hypothesis: its co-abundance with neural and adhesion proteins may reflect vascular or blood-material exposure in cerebrospinal-fluid samples rather than a neuronal mechanism. The data do not demonstrate a causal coagulation effect on the other module members.

#### APP

- **Related proteins** (co-abundance neighbors): NICOL1 (0.91); STRING partners: APOM (0.754)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: amyloid beta precursor protein. This gene encodes a cell surface receptor and transmembrane precursor protein that is cleaved by secretases to form a number of peptides. Some of these peptides are secreted and can bind to the acetyltransferase complex APBB1/TIP60 to promote transcriptional activation, while others form the protein basis of the amyloid plaques found in the brains of patients with Alzheimer disease. In addition, t…
- **Diseases (Open Targets)**: Alzheimer disease (0.815); Alzheimer disease type 1 (0.788); cerebral amyloid angiopathy, APP-related (0.754); dementia (0.698); Hereditary cerebral hemorrhage with amyloidosis (0.633)
- **Europe PMC papers**: 83189
- **Why important**: APP is connected to NICOL1 and APOM, including a STRING relationship with APOM. It is a cell-surface precursor that is processed into secreted peptides and has annotations involving microglial and astrocyte immune responses. Its disease associations strongly include Alzheimer disease and cerebral amyloid angiopathy, and it has exceptionally extensive literature support. APP provides a biologically important bridge between extracellular protein handling, brain-associated biology, and disease-relevant cerebrospinal-fluid processes.
- **Conclusion**: Established evidence: APP is a brain-relevant, processed cell-surface precursor with strong neurodegenerative disease associations and a supplied STRING link to APOM. Hypothesis: APP may connect lipid-associated extracellular transport to glial or neuronal response states in the shared module. The module alone cannot distinguish normal APP biology from disease-related amyloid processing or sample-composition effects.

## Module 3

**Tissue pair**: cell line and cerebrospinal_fluid  
**Genes (8)**: GOT1, ALDOC, BASP1, CSF1, PGK1, PTPRZ1, CLEC3B, TXN

### Function

The strongest global enrichment supports central carbon and amino-acid metabolism, specifically gluconeogenesis, hexose biosynthesis, monosaccharide biosynthesis, and carbon metabolism (5 globally significant GO/KEGG terms, q_global 0.0125–0.0369; see the table). These terms are driven by the metabolic enzyme trio ALDOC, GOT1, and PGK1. ALDOC supports glycolytic and fructose metabolism, GOT1 links amino-acid, aspartate, oxaloacetate, and gluconeogenic metabolism, and PGK1 catalyzes a core glycolytic reaction. The module therefore most plausibly represents coordinated metabolic state rather than a discrete molecular complex. The broader network also contains extracellular, signaling, and redox-associated proteins, so the metabolic interpretation should not be extended to every member without qualification.

**Cell composition.** The module is compositionally mixed. A substantial fraction of its proteins are secreted or associated with extracellular biology, including CLEC3B, CSF1, and PTPRZ1, while TXN has intracellular and membrane localization. HPA profiles show strong representation of brain-related tissues and neural or glial cell types, including astrocytes, Bergmann glia, oligodendrocyte progenitors, and ependymal cells. Other members are enhanced in muscle, retina, esophagus, fibroblasts, or reproductive cell types. Blood-cell specificity is generally low or absent, although CSF1 and BASP1 show associations with basophils, eosinophils, or neutrophils. Thus, the module does not look like a uniformly blood-cell-enriched module, but its shared signal could reflect a mixture of neural, epithelial, stromal, and secreted-protein contributions in the sampled materials. The lack of matching HPA protein-detection data for either sample type prevents direct protein-level confirmation in cell line or cerebrospinal fluid.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Biosynthesis of amino acids - Homo sapiens (human) | 0.0125 | ALDOC, GOT1, PGK1 |
| GO:BP gluconeogenesis | 0.0369 | ALDOC, GOT1, PGK1 |
| GO:BP hexose biosynthetic process | 0.0369 | ALDOC, GOT1, PGK1 |
| GO:BP monosaccharide biosynthetic process | 0.0369 | ALDOC, GOT1, PGK1 |
| KEGG Carbon metabolism - Homo sapiens (human) | 0.0369 | ALDOC, GOT1, PGK1 |

### STRING and hu.MAP

STRING provides only a direct high-confidence relationship between ALDOC and PGK1. STRING supplementary enrichment independently highlights the same carbon-metabolism and gluconeogenesis trio, GOT1, PGK1, and ALDOC (STRING KEGG Carbon metabolism; within-query FDR = 0.0143), (STRING KEGG Biosynthesis of amino acids; within-query FDR = 0.0143), (STRING WikiPathways Glycolysis and gluconeogenesis; within-query FDR = 0.0393), (STRING RCTM Gluconeogenesis; within-query FDR = 0.0409), which strengthens the interpretation of a metabolic submodule but is not additional global enrichment evidence. STRING also assigns supplementary compartment associations involving CLEC3B, BASP1, CSF1, and TXN (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0377), (STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.0484), but these should be treated as contextual rather than proof of a shared physical complex. No hu.MAP complex contains multiple module members. The network therefore combines a supported metabolic relationship with module-level co-abundance links that are not established as a common biochemical complex.

**STRING interactions (score >= 0.7)**: 1 of 28 gene pairs: ALDOC–PGK1 (0.835)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Carbon metabolism (FDR = 0.0143, 3 genes); KEGG Biosynthesis of amino acids (FDR = 0.0143, 3 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0377, 4 genes); WikiPathways Glycolysis and gluconeogenesis (FDR = 0.0393, 3 genes); RCTM Gluconeogenesis (FDR = 0.0409, 3 genes); COMPARTMENTS Nucleoplasm (FDR = 0.0484, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The metabolic core is not biologically novel: the functions of ALDOC, GOT1, and PGK1 and their participation in glycolytic, gluconeogenic, and carbon-metabolism pathways are established. The module-level observation may nevertheless be a potentially new cross-tissue co-abundance pattern, because most of its pairwise relationships are not represented by high-confidence STRING links and no multi-member hu.MAP complex is present. That lack of database support alone cannot establish novelty. A defensible conclusion is that this is a potentially novel systems-level association built around a known metabolic core, requiring replication in independent cohorts and testing against cell-composition and sample-quality effects.

**Hypothesis.** Hypothesis: the conserved signal reflects coordinated metabolic activity in a mixed neural and secreted-protein environment. A metabolic core formed by ALDOC, GOT1, and PGK1 may track carbon flux and amino-acid interconversion, while CLEC3B, CSF1, PTPRZ1, BASP1, and TXN may report extracellular signaling, glial or stromal cellular context, membrane-associated regulation, and redox state. In cerebrospinal fluid, this could arise from contributions of neural or glial cells together with secreted proteins; in cell-line material, it could reflect a related metabolic and stress-associated state. This is a co-abundance model, not evidence that all members physically interact or that one member causally regulates the others.

### Important genes

#### CLEC3B

- **Related proteins** (co-abundance neighbors): BASP1 (0.85), PGK1 (0.85), GOT1 (0.84), ALDOC (0.83), TXN (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: C-type lectin domain family 3 member B. Enables calcium ion binding activity; heparin binding activity; and kringle domain binding activity. Involved in bone mineralization and cellular response to transforming growth factor beta stimulus. Located in cytoplasm; extracellular space; and granular component. Part of collagen-containing extracellular matrix. Implicated in osteoarthritis. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: macular dystrophy, retinal, 4 (0.453); neurodegenerative disease (0.314); Parkinson disease (0.232); Alzheimer disease (0.223); lysosomal storage disease (0.221)
- **Europe PMC papers**: 1141
- **Why important**: CLEC3B is the central network hub, connecting the metabolic genes ALDOC, GOT1, and PGK1 with BASP1 and TXN. HPA places it in extracellular and secreted-to-blood contexts and associates it with choroid plexus epithelial cells, ependymal cells, and fibroblasts. Its annotations include extracellular matrix, plasminogen activation, bone mineralization, and transforming-growth-factor response, and it has disease links including retinal macular dystrophy and neurodegenerative disease. Its extensive literature makes it a useful candidate for explaining how a metabolic signal could be connected to extracellular or tissue-context biology.
- **Conclusion**: Established evidence supports CLEC3B as the network connector and as an extracellular or secreted protein with tissue-context associations. It is not part of the globally enriched metabolic terms, so its role as a metabolic regulator remains a hypothesis rather than an established conclusion.

#### ALDOC

- **Related proteins** (co-abundance neighbors): CLEC3B (0.83); STRING partners: PGK1 (0.835)
- **HPA**: Group enriched; Group enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldolase, fructose-bisphosphate C. This gene encodes a member of the class I fructose-biphosphate aldolase gene family. Expressed specifically in the hippocampus and Purkinje cells of the brain, the encoded protein is a glycolytic enzyme that catalyzes the reversible aldol cleavage of fructose-1,6-biphosphate and fructose 1-phosphate to dihydroxyacetone phosphate and either glyceraldehyde-3-phosphate or glyceraldehyde, respectively…
- **Diseases (Open Targets)**: glioblastoma (0.098); non-small cell lung carcinoma (0.096); gastric cancer (0.087); breast cancer (0.085); breast carcinoma (0.084)
- **Europe PMC papers**: 2686
- **Why important**: ALDOC is part of every globally significant enrichment term (5 globally significant GO/KEGG terms, q_global 0.0125–0.0369; see the table) and is a brain- and retina-associated fructose-bisphosphate aldolase. It occupies the metabolic arm of the module and connects to PGK1 in STRING, providing the clearest link between the module's co-abundance structure and a known metabolic relationship. Its established functions include glycolysis, gluconeogenesis, and fructose metabolism, while its tissue profile includes astrocytes, Bergmann glia, neurons, and oligodendrocyte progenitors. It has a substantial literature and disease associations involving several cancers.
- **Conclusion**: Established evidence identifies ALDOC as a principal metabolic marker and a strong candidate driver of the module's pathway enrichment. Its connection to neural cell types supports a brain-related interpretation, but the data do not establish that ALDOC causes the co-abundance pattern.

#### GOT1

- **Related proteins** (co-abundance neighbors): CLEC3B (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamic-oxaloacetic transaminase 1. Glutamic-oxaloacetic transaminase is a pyridoxal phosphate-dependent enzyme which exists in cytoplasmic and mitochondrial forms, GOT1 and GOT2, respectively.  GOT plays a role in amino acid metabolism and the urea and tricarboxylic acid cycles. The two enzymes are homodimeric and show close homology. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); Parkinson disease (0.375); Alzheimer disease (0.367); lysosomal storage disease (0.356); obesity disorder (0.172)
- **Europe PMC papers**: 3793
- **Why important**: GOT1 is present in every globally significant enrichment term (5 globally significant GO/KEGG terms, q_global 0.0125–0.0369; see the table) and encodes a transaminase involved in amino-acid metabolism, gluconeogenesis, oxaloacetate, aspartate, and related carbon flux. Its tissue enhancement in heart muscle, skeletal muscle, and tongue indicates broad metabolic relevance rather than a uniquely cerebrospinal-fluid-specific role. It has substantial literature and disease associations involving neurodegenerative disease, Parkinson disease, and Alzheimer disease.
- **Conclusion**: Established evidence supports GOT1 as the amino-acid and carbon-metabolism component of the module. Its disease associations make it biologically important, but they do not demonstrate that this module mediates those diseases.

#### PGK1

- **Related proteins** (co-abundance neighbors): CLEC3B (0.85); STRING partners: ALDOC (0.835)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece, Principal piece, End piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglycerate kinase 1. The protein encoded by this gene is a glycolytic enzyme that catalyzes the conversion of 1,3-diphosphoglycerate to 3-phosphoglycerate. The encoded protein may also act as a cofactor for polymerase alpha. Additionally, this protein is secreted by tumor cells where it participates in angiogenesis by functioning to reduce disulfide bonds in the serine protease, plasmin, which consequently leads to th…
- **Diseases (Open Targets)**: glycogen storage disease due to phosphoglycerate kinase 1 deficiency (0.823); Menkes disease (0.578); X-linked distal spinal muscular atrophy type 3 (0.556); occipital horn syndrome (0.556); hereditary disease (0.520)
- **Europe PMC papers**: 14784
- **Why important**: PGK1 is present in every globally significant enrichment term (5 globally significant GO/KEGG terms, q_global 0.0125–0.0369; see the table), catalyzes a core glycolytic reaction, and forms the module's only high-confidence STRING pair with ALDOC. It is broadly expressed, has an extensive literature, and is associated with PGK1 deficiency and related inherited disorders. Its HPA profile includes neutrophil-associated expression but generally low immune-cell specificity, so it may report general metabolic state rather than a specialized blood-cell program.
- **Conclusion**: Established evidence supports PGK1 as a core glycolytic and metabolic marker, with independent network support from its ALDOC relationship. The module does not show that PGK1 is secreted or that it specifically drives cerebrospinal-fluid biology.

#### PTPRZ1

- **Related proteins** (co-abundance neighbors): CSF1 (0.87); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein tyrosine phosphatase receptor type Z1. This gene encodes a member of the receptor protein tyrosine phosphatase family. Expression of this gene is restricted to the central nervous system (CNS), and it may be involved in the regulation of specific developmental processes in the CNS. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, May 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.524); Abnormality of the integument (0.316); biliary tract disorder (0.314); placental retention (0.215); Hypocalcemia (0.180)
- **Europe PMC papers**: 2080
- **Why important**: PTPRZ1 is the most specifically brain-associated member in the HPA summary, with tissue enrichment in brain and cell-type enhancement in astrocytes, Bergmann glia, ependymal cells, and oligodendrocyte progenitors. Its annotated functions include protein dephosphorylation, central nervous system development, neuron projection development, learning or memory, and regulation of myelination. It connects to CSF1 in the module and has disease associations involving neurodegenerative disease. Its literature volume is substantial.
- **Conclusion**: Established evidence supports PTPRZ1 as a neural and glial context marker with receptor-phosphatase functions. Its placement beside CSF1 suggests a possible signaling context, but no STRING or hu.MAP support establishes a physical complex or causal interaction.

#### CSF1

- **Related proteins** (co-abundance neighbors): PTPRZ1 (0.87), BASP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: colony stimulating factor 1. The protein encoded by this gene is a cytokine that controls the production, differentiation, and function of macrophages. The active form of the protein is found extracellularly as a disulfide-linked homodimer, and is thought to be produced by proteolytic cleavage of membrane-bound precursors. The encoded protein may be involved in development of the placenta. Alternate splicing results in multip…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.308); metabolic syndrome (0.267); otosclerosis (0.264); adult-onset Still disease (0.200); triple-negative breast carcinoma (0.127)
- **Europe PMC papers**: 13069
- **Why important**: CSF1 is a secreted cytokine associated with macrophage production, differentiation, and function. It connects PTPRZ1 and BASP1 in the module, has a large literature, and shows HPA associations with fibroblasts, mast cells, erythroid and megakaryocytic progenitors, basophils, and eosinophils. Its disease associations include metabolic syndrome and type two diabetes mellitus, linking immune or stromal signaling to metabolic context.
- **Conclusion**: Established evidence supports CSF1 as a secreted immune and tissue-signaling factor that could explain non-metabolic context in the module. Its presence does not establish blood contamination, because the module is not predominantly blood-cell enriched and the co-abundance data do not identify the source cell.

## Module 4

**Tissue pair**: cell line and cerebrospinal_fluid  
**Genes (11)**: DBI, ANGPTL2, HSPA5, C1R, CACNA2D1, CACHD1, CLIC1, C7, EPHB2, LAMC1, SPARC

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent. The gene annotations nevertheless suggest a biologically coherent but broad extracellular and tissue-interface theme: complement and innate immune biology through C7 and C1R, extracellular-matrix and stromal organization through SPARC and LAMC1, vascular or endothelial signaling through ANGPTL2 and EPHB2, and supporting calcium, lipid, and proteostasis processes through CACNA2D1, CACHD1, DBI, and HSPA5. The network therefore appears more consistent with coordinated abundance of secreted, matrix-associated, signaling, and cellular-stress proteins than with a narrowly defined canonical pathway. These functional interpretations are established for the individual genes, whereas their joint module-level interpretation remains inferential.

**Cell composition.** The module is strongly compatible with extracellular and stromal biology: many members are secreted or extracellular-matrix associated, including ANGPTL2, C7, SPARC, and LAMC1. HPA cell-type annotations repeatedly point to fibroblasts, adipocytes, fibro-adipogenic progenitors, pituicytes or folliculostellate cells, and related stromal or epithelial populations. Tissue enrichment is heterogeneous rather than restricted to cerebrospinal fluid or neural tissue. Most genes are not detected in immune cells or have low immune-cell specificity, although SPARC is blood-cell enriched and several genes have single blood-cell associations. Thus, the shared module could reflect a conserved stromal, vascular-interface, or secreted-protein component of the samples, or shared cell-type composition, rather than a cerebrospinal-fluid-specific neuronal program. The absence of matched HPA protein-detection data for either sample context limits direct protein-level interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module members, and no hu.MAP complex contained multiple members. Consequently, the co-abundance edges are not corroborated here by established physical interaction or complex-membership evidence. Known biology exists within individual proteins and their canonical systems: C7 and C1R belong to complement pathways, LAMC1 is a laminin basement-membrane component, SPARC is an extracellular matrix regulator, ANGPTL2 is a secreted vascular-associated signaling protein, CACNA2D1 supports voltage-gated calcium-channel function, and HSPA5 is an endoplasmic-reticulum chaperone. The lack of database-supported pairwise relationships argues against describing this as a known molecular complex; it may instead represent coordinated secretion, extracellular remodeling, shared cellular origin, or correlated tissue composition.

**STRING interactions (score >= 0.7)**: 0 of 55 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is potentially a new co-abundance association because the module has no reported high-confidence STRING interactions, no reported multi-member hu.MAP complex, and no globally significant GO or KEGG enrichment. Those absences do not establish biological novelty: the pattern could arise from shared stromal or secreted-protein composition, correlated abundance across tissues, technical or sampling effects, or incomplete interaction databases. The most defensible conclusion is that the specific cross-context co-abundance pattern is not explained by currently supplied canonical interaction or complex evidence, while the individual gene functions are well established and not themselves novel.

**Hypothesis.** Hypothesis: the module reflects a conserved extracellular-tissue-interface state shared by the cell-line and cerebrospinal-fluid datasets. In this model, stromal or epithelial-like cells produce or release matrix and vascular-interface proteins such as LAMC1, SPARC, and ANGPTL2, while complement components C1R and C7 represent local innate-immune surveillance or extracellular remodeling. Eph signaling, calcium-channel-associated proteins, lipid handling, and ER chaperone activity may accompany the same cell state or the synthesis and trafficking of secreted proteins. The co-abundance structure could therefore arise from coordinated activity or shared cellular composition rather than direct protein binding. This hypothesis should be tested with cell-type deconvolution, independent cohorts, targeted protein measurements, and perturbation of complement, matrix, or ANGPTL2-related signaling.

### Important genes

#### ANGPTL2

- **Related proteins** (co-abundance neighbors): C1R (0.98), EPHB2 (0.88), CACNA2D1 (0.85), LAMC1 (0.84), HSPA5 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: angiopoietin like 2. Angiopoietins are members of the vascular endothelial growth factor family and the only known growth factors largely specific for vascular endothelium. Angiopoietin-1, angiopoietin-2, and angiopoietin-4 participate in the formation of blood vessels. ANGPTL2 protein is a secreted glycoprotein with homology to the angiopoietins and may exert a function on endothelial cells through autocrine or parac…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.351); spermatogenic failure (0.320); Abnormal male internal genitalia morphology (0.320); open-angle glaucoma (0.262); glaucoma (0.250)
- **Europe PMC papers**: 1583
- **Why important**: ANGPTL2 is the most connected module member and links complement-related C1R with EPHB2, CACNA2D1, LAMC1, and HSPA5 in the co-abundance graph. It is a secreted glycoprotein associated with vascular signaling and cell-cell communication, and its HPA profile points toward adipocyte, stromal, and choroid-plexus-related cell types. Its disease associations and substantial literature support make it a strong candidate for organizing a secreted vascular or stromal state.
- **Conclusion**: Established evidence supports ANGPTL2 as a secreted signaling protein with vascular and cell-communication functions. The module data support it as a central abundance correlate, but do not demonstrate that it regulates the other module genes or drives the module.

#### C7

- **Related proteins** (co-abundance neighbors): CLIC1 (0.93), SPARC (0.84), DBI (0.84), CACNA2D1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C7. This gene encodes a serum glycoprotein that forms a membrane attack complex together with complement components C5b, C6, C8, and C9 as part of the terminal complement pathway of the innate immune system. The protein encoded by this gene contains a cholesterol-dependent cytolysin/membrane attack complex/perforin-like (CDC/MACPF) domain and belongs to a large family of structurally related molecules…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.785); complement deficiency (0.463); alcohol drinking (0.271); inflammatory bowel disease (0.207); hereditary disease (0.194)
- **Europe PMC papers**: 36065
- **Why important**: C7 is highly connected and links CLIC1, SPARC, DBI, and CACNA2D1. It is a terminal complement component that participates in membrane-attack-complex formation, has strong complement-deficiency disease relevance, and has extensive literature support. Its association with stromal and adipocyte-related cell types suggests that complement abundance may be coupled to non-immune tissue interfaces in this module.
- **Conclusion**: Established evidence identifies C7 as a complement effector with innate-immune function. Its module association is compatible with local extracellular surveillance or shared secreted-protein composition, but it does not establish active complement-mediated damage in either sample context.

#### C1R

- **Related proteins** (co-abundance neighbors): ANGPTL2 (0.98), CACHD1 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C1r. This gene encodes a member of the peptidase S1 protein family. The encoded protein is a proteolytic subunit in the complement system C1 complex. The complement system acts as a mediator in the innate immune response by ultimately triggering phagocytosis, inflammation, and rupturing the bacterial cell wall. Mutations in this gene are associated with Ehlers-Danlos Syndrome. [provided by RefSeq, Dec …
- **Diseases (Open Targets)**: Ehlers-Danlos syndrome, periodontitis type (0.715); immunodeficiency due to a classical component pathway complement deficiency (0.555); coronary artery disorder (0.486); systemic lupus erythematosus (0.467); complement deficiency (0.463)
- **Europe PMC papers**: 5739
- **Why important**: C1R is connected to ANGPTL2 and CACHD1 and is a proteolytic component of the classical complement C1 complex. It has disease associations involving complement deficiency and Ehlers-Danlos syndrome, while its HPA annotations include liver, astrocyte, stromal, and fibroblast-related contexts. It provides a plausible upstream complement-related component alongside C7.
- **Conclusion**: Established evidence supports C1R as a complement protease involved in classical-pathway activation. The co-abundance relationship with ANGPTL2 and CACHD1 is a hypothesis-generating association, not evidence of direct biochemical interaction or pathway activation.

#### SPARC

- **Related proteins** (co-abundance neighbors): C7 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: secreted protein acidic and cysteine rich. This gene encodes a cysteine-rich acidic matrix-associated protein. The encoded protein is required for the collagen in bone to become calcified but is also involved in extracellular matrix synthesis and promotion of changes to cell shape. The gene product has been associated with tumor suppression but has also been correlated with metastasis based on changes to cell shape which can promote tumor …
- **Diseases (Open Targets)**: osteogenesis imperfecta (0.707); neurodegenerative disease (0.443); hereditary disease (0.414); osteogenesis imperfecta type 4 (0.381); Abnormality of the skeletal system (0.358)
- **Europe PMC papers**: 17798
- **Why important**: SPARC is a secreted matrix-associated protein connected to C7 and is enriched in stromal populations including fibroblasts and hepatic stellate cells. Its established roles in extracellular-matrix synthesis, cell shape, endothelial behavior, and tissue remodeling make it a key bridge between complement-related proteins and a stromal extracellular environment. It is also blood-cell enriched in HPA, which is relevant to possible sample-composition effects.
- **Conclusion**: Established evidence supports SPARC as an extracellular-matrix and cell-morphogenesis regulator. In this module it is consistent with stromal or vascular-interface biology, but its blood-cell association means that tissue or cellular composition must be excluded before assigning a specific local mechanism.

#### LAMC1

- **Related proteins** (co-abundance neighbors): ANGPTL2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit gamma 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: Fuchs' endothelial dystrophy (0.487); prostate carcinoma (0.467); colorectal cancer (0.447); eye disorder (0.434); benign colon neoplasm (0.427)
- **Europe PMC papers**: 4227
- **Why important**: LAMC1 is linked to the central ANGPTL2 node and is a secreted extracellular-matrix component of laminin basement membranes. Its fibroblast, adipocyte, fibro-adipogenic progenitor, and pituicyte or folliculostellate annotations support a stromal or tissue-boundary interpretation. Laminin biology provides a plausible structural context for coordinated abundance of matrix and signaling proteins.
- **Conclusion**: Established evidence supports LAMC1 in basement-membrane organization, adhesion, migration, and tissue development. Its module membership supports a matrix-associated interpretation, but does not prove that LAMC1 physically binds the other module members or causes their coordinated abundance.

#### HSPA5

- **Related proteins** (co-abundance neighbors): ANGPTL2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is connected to ANGPTL2 and is a major endoplasmic-reticulum chaperone involved in protein folding, assembly, ER homeostasis, and the unfolded-protein response. Its presence may be relevant to the production or handling of secreted and membrane-associated proteins in a shared cellular state. It also has substantial literature and disease-related context.
- **Conclusion**: Established evidence supports HSPA5 as an ER proteostasis factor. Its module association is compatible with secretory or cellular-stress activity, but the data do not distinguish a mechanistic stress response from broad abundance coupling or cell-type composition.

## Module 5

**Tissue pair**: cell line and cerebrospinal_fluid  
**Genes (11)**: ADAM10, GLB1, BTD, CADM1, DCBLD1, EFNA3, SERPING1, CD58, LCN2, PLXNB1, PRSS23

### Function

No GO or KEGG term passed global correction, so the module does not support a formally significant pathway assignment. Its strongest biological interpretation is a mixed extracellular and cell-interaction module. EFNA3 forms the central co-abundance hub and is annotated for ephrin signaling, axon guidance, cell-cell signaling, and regulation of angiogenesis. SERPING1 and LCN2 form the only hu.MAP-supported pair and connect the module to complement regulation, acute-phase biology, innate defense, and secreted plasma proteins. ADAM10 and EFNA3 are the sole high-confidence STRING interaction, supporting a possible membrane signaling or proteolytic relationship. CD58, CADM1, and PLXNB1 add immune-cell adhesion, cell recognition, semaphorin signaling, and regulation of cell shape to the interpretation. Overall, the module is better described as a cross-context extracellular and cell-surface co-abundance pattern than as a single established biochemical pathway.

**Cell composition.** Most module genes are annotated by HPA as secreted or associated with extracellular or membrane compartments, including SERPING1, LCN2, PRSS23, and BTD. SERPING1 is liver enhanced and secreted to blood, while LCN2 is associated with bone marrow and granulocytic populations and is secreted in other tissues. The module has mixed tissue associations involving liver, retina, esophagus, skin, bone marrow, and cervix rather than one uniform tissue source. Many genes are cell-type enhanced, with signals involving neutrophils, adipocytes, rod photoreceptors, astrocytes, pericytes, and epithelial populations. Blood-cell specificity is mixed: some genes are immune-cell enhanced or group enriched, whereas others have low immune specificity or are not detected in immune cells. This composition means that the shared signal may partly reflect circulating proteins, blood or immune-cell contributions, extracellular carryover, or shared cell types in the samples, rather than a cell-intrinsic program common to cell lines and cerebrospinal fluid.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only one high-confidence relationship within the module, ADAM10–EFNA3, and reports no supplementary functional enrichment. This supports a specific known relationship but not a densely established protein-interaction network. hu.MAP identifies SERPING1 and LCN2 together in complex C1, whose full membership is much broader than this module and includes many plasma, complement, coagulation, and extracellular proteins. Thus, C1 provides contextual support for an extracellular or blood-associated component, but the presence of only a small subset of that complex in the module does not establish that the entire module is one physical complex. The remaining co-abundance edges are not independently supported by the supplied STRING or hu.MAP evidence and should be interpreted as statistical associations rather than confirmed direct interactions.

**STRING interactions (score >= 0.7)**: 1 of 55 gene pairs: ADAM10–EFNA3 (0.75)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10678.1 (SERPING1, LCN2; 2/71)

### Novelty

The individual biology is not new: EFNA3, ADAM10, SERPING1, LCN2, CD58, PLXNB1, CADM1, and the other members have established functions, disease links, or literature. The module-level observation may still be a new co-abundance pattern shared by cell line and cerebrospinal fluid, but novelty cannot be established from this fact sheet alone because there is no comparison with previously reported co-abundance modules, datasets, or publications. The limited STRING support and partial hu.MAP overlap argue against calling it a newly discovered physical complex. Absence from STRING or hu.MAP is not evidence of novelty; it mainly indicates that the observed module organization is not well represented in those resources.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of extracellular and membrane-associated proteins arising from a mixture of secreted plasma-like proteins, immune or myeloid contributions, and neural or epithelial cell-surface biology. A possible mechanistic axis is EFNA3-associated cell signaling and adhesion, coupled to ADAM10-mediated ectodomain processing, with CD58, CADM1, and PLXNB1 contributing cell-contact signals. In parallel, SERPING1 and LCN2 may report complement regulation and innate inflammatory or iron-sequestration activity in the extracellular environment. This hypothesis predicts that the module will track sample composition, barrier or vascular state, and inflammatory activity more strongly than a single intracellular pathway. It requires validation with independent cohorts, cell-deconvolution, protein-level measurements, and perturbation or targeted interaction assays.

### Important genes

#### EFNA3

- **Related proteins** (co-abundance neighbors): ADAM10 (0.95), GLB1 (0.94), BTD (0.89), CD58 (0.88), PLXNB1 (0.87), CADM1 (0.85); STRING partners: ADAM10 (0.75)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ephrin A3. This gene encodes a member of the ephrin (EPH) family. The ephrins and EPH-related receptors comprise the largest subfamily of receptor protein-tyrosine kinases and have been implicated in mediating developmental events, especially in the nervous system and in erythropoiesis. Based on their structures and sequence relationships, ephrins are divided into the ephrin-A (EFNA) class, which are anchore…
- **Diseases (Open Targets)**: non-alcoholic fatty liver (0.291); bladder exstrophy (0.105); neoplasm (0.100); hepatocellular carcinoma (0.097); lung adenocarcinoma (0.096)
- **Europe PMC papers**: 1093
- **Why important**: EFNA3 is the central network hub, connecting to ADAM10, GLB1, BTD, CD58, PLXNB1, and CADM1. Its established annotations include ephrin receptor signaling, cell-cell signaling, axon guidance, regulation of angiogenesis, and promotion of amyloid precursor protein catabolism. It therefore provides the clearest bridge between the neural context of cerebrospinal fluid and the module’s membrane and adhesion features. It also has extensive literature and disease associations, making it the best anchor for biological interpretation.
- **Conclusion**: Established evidence supports EFNA3 as the network-centered cell-surface signaling component of the module. It is plausible, but not demonstrated, that EFNA3 organizes the broader co-abundance pattern or links neural and epithelial or vascular biology across the two sample contexts.

#### SERPING1

- **Related proteins** (co-abundance neighbors): LCN2 (0.97), PRSS23 (0.92), DCBLD1 (0.87), CD58 (0.87), ADAM10 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1
- **Function (MyGene.info)**: serpin family G member 1. This gene encodes a highly glycosylated plasma protein involved in the regulation of the complement cascade. Its encoded protein, C1 inhibitor, inhibits activated C1r and C1s of the first complement component and thus regulates complement activation. It is synthesized in the liver, and its deficiency is associated with hereditary angioneurotic oedema (HANE). Alternative splicing results in multipl…
- **Diseases (Open Targets)**: hereditary angioedema with C1Inh deficiency (0.828); hereditary angioedema type 1 (0.750); hereditary angioedema (0.728); angioedema (0.616); hereditary angioedema type 2 (0.614)
- **Europe PMC papers**: 4203
- **Why important**: SERPING1 is the second major network connector and links to LCN2, PRSS23, DCBLD1, CD58, and ADAM10. HPA annotates it as liver enhanced and secreted to blood. Its established function is inhibition of complement activation, with a strong disease connection to hereditary angioedema and extensive literature. Its membership in hu.MAP complex C1 with LCN2 reinforces an extracellular, plasma-associated interpretation.
- **Conclusion**: Established evidence supports SERPING1 as a secreted regulator of complement and a major marker of extracellular or blood-derived biology. It is a strong candidate for explaining why this module appears across disparate sample contexts, but the data do not show that complement activation is the causal driver of the module.

#### LCN2

- **Related proteins** (co-abundance neighbors): SERPING1 (0.97); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1
- **Function (MyGene.info)**: lipocalin 2. This gene encodes a protein that belongs to the lipocalin family. Members of this family transport small hydrophobic molecules such as lipids, steroid hormones and retinoids. The protein encoded by this gene is a neutrophil gelatinase-associated lipocalin and plays a role in innate immunity by limiting bacterial growth as a result of sequestering iron-containing siderophores. The presence of this …
- **Diseases (Open Targets)**: psoriasis (0.124); type 2 diabetes mellitus (0.122); acute kidney injury (0.121); coronary artery disorder (0.121); neoplasm (0.120)
- **Europe PMC papers**: 11549
- **Why important**: LCN2 is directly connected to SERPING1 and is associated with bone marrow, neutrophil progenitors, basophils, neutrophils, and monocytes in HPA. It is secreted in other tissues and has established roles in acute-phase response, oxidative stress, bacterial defense, and sequestration of iron-containing siderophores. Its extensive literature and clinical biomarker associations make it an important indicator of innate immune or extracellular inflammatory state.
- **Conclusion**: Established evidence supports LCN2 as an innate-defense and secreted extracellular component that may reflect myeloid or inflammatory contributions. Its co-abundance with SERPING1 is consistent with a shared extracellular state, but it does not prove that the module represents active infection or inflammation.

#### ADAM10

- **Related proteins** (co-abundance neighbors): EFNA3 (0.95), SERPING1 (0.83); STRING partners: EFNA3 (0.75)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ADAM metallopeptidase domain 10. Members of the ADAM family are cell surface proteins with a unique structure possessing both potential adhesion and protease domains. This gene encodes and ADAM family member that cleaves many proteins including TNF-alpha and E-cadherin. Alternate splicing results in multiple transcript variants encoding different proteins that may undergo similar processing. [provided by RefSeq, Feb 2016].
- **Diseases (Open Targets)**: reticulate acropigmentation of Kitamura (0.679); Alzheimer disease 18 (0.621); Alzheimer disease (0.522); dementia (0.415); schizophrenia (0.354)
- **Europe PMC papers**: 11139
- **Why important**: ADAM10 has a focused position between EFNA3 and SERPING1 and is the only gene participating in the module’s high-confidence STRING interaction. It is a membrane-associated metalloprotease involved in ectodomain proteolysis, cell adhesion regulation, and Notch signaling, and it has very extensive literature with disease associations including neurodegenerative conditions. Its position makes it a plausible interface between membrane signaling and extracellular protein abundance.
- **Conclusion**: Established evidence supports ADAM10 as a membrane protease with a known relationship to EFNA3 and relevant neurobiological functions. A role in processing module proteins or shaping the observed extracellular pattern is a mechanistic possibility, but the co-abundance data do not establish substrate processing or directionality.

#### CD58

- **Related proteins** (co-abundance neighbors): EFNA3 (0.88), SERPING1 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD58 molecule. This gene encodes a member of the immunoglobulin superfamily. The encoded protein is a ligand of the T lymphocyte CD2 protein, and functions in adhesion and activation of T lymphocytes. The protein is localized to the plasma membrane. Alternatively spliced transcript variants have been described. [provided by RefSeq, Jan 2009].
- **Diseases (Open Targets)**: primary biliary cholangitis (0.408); diffuse large B-cell lymphoma (0.388); non-Hodgkin lymphoma (0.371); systemic lupus erythematosus (0.300); arthropathy (0.131)
- **Europe PMC papers**: 3682
- **Why important**: CD58 connects the EFNA3 and SERPING1 portions of the network and encodes a membrane ligand for CD2 that supports T-cell adhesion and activation. Its annotations include immune response, heterotypic cell adhesion, cytokine regulation, and responses to interferon and tumor necrosis factor. It has extensive literature and disease associations involving immune and lymphoid disorders, making it informative for the module’s cell-contact and immune component.
- **Conclusion**: Established evidence supports CD58 as an immune-cell adhesion and activation marker that may connect extracellular protein abundance to cellular composition. Its position suggests a bridging role in the module, but the available evidence does not show that CD58 drives the secreted-protein component or indicates a specific immune disease process.

## Module 6

**Tissue pair**: cell line and cerebrospinal_fluid  
**Genes (12)**: ADGRG6, GUSB, CPM, CD109, CD44, CPVL, IGHM, LAYN, LIFR, OLFM3, PLXNA4, SIAE

### Function

This is not a clearly defined canonical pathway module. No GO or KEGG term passed global correction, so there is no globally significant pathway annotation to assign. The annotations instead suggest a mixed cell-surface, extracellular, immune-associated, and intracellular catabolic signal. PLXNA4 is the network hub and is annotated with semaphorin receptor activity, axon guidance, synapse assembly, and regulation of GTPase activity. CPM, CPVL, GUSB, and SIAE provide enzymatic or lysosomal and carbohydrate-processing themes, whereas CD44, LIFR, ADGRG6, LAYN, and CD109 provide receptor, adhesion, cytokine-response, or cell-surface signaling functions. IGHM contributes a B-cell and immunoglobulin signal, and OLFM3 contributes a brain- and synapse-associated signal. Overall, the module is best interpreted as a heterogeneous co-abundance program involving membrane interactions, immune or myeloid biology, extracellular or glycan-related processing, and possible neural or cerebrospinal-fluid-associated biology rather than as a single established biochemical pathway.

**Cell composition.** The module is strongly mixed in cellular and subcellular character. HPA annotates most members as cell-type enhanced, with recurring associations to Kupffer cells, Hofbauer cells, macrophages, monocytes, myeloid dendritic cells, and other immune or myeloid populations. IGHM is associated with B cells, plasma cells, and memory or naive B-cell populations. This makes shared blood, immune-cell, or cellular-composition effects plausible in the cell-line and cerebrospinal-fluid comparison. The module also contains secreted or extracellularly relevant proteins, including OLFM3, IGHM, and CD44, while other members are intracellular, vesicular, endoplasmic-reticulum, or plasma-membrane proteins. Tissue annotations span adipose tissue, lymphoid tissue, intestine, liver, placenta, brain, retina, and choroid plexus, without a single dominant tissue identity. Thus, the module may reflect shared cell types or sample composition more than a uniform tissue-independent protein pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module members, and no supplementary STRING functional enrichment is reported. This argues against interpreting the co-abundance edges as established physical protein interactions. The only hu.MAP evidence is (hu.MAP huMAP3_09327.1), in which GUSB and CD109 occur as module members of a much larger complex; this is partial complex overlap rather than evidence that the two module proteins directly interact or that the whole module is a complex. Known biology remains plausible at the level of individual proteins: GUSB is a lysosomal glycosaminoglycan hydrolase, CD109 is a cell-surface regulator of transforming growth factor beta signaling, PLXNA4 is a semaphorin receptor, and CD44 is a hyaluronan receptor involved in adhesion and migration. However, the network structure is not independently supported by current STRING or hu.MAP connectivity.

**STRING interactions (score >= 0.7)**: 0 of 66 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09327.1 (GUSB, CD109; 2/93)

### Novelty

The co-abundance pattern could represent a new observation, but the available evidence does not establish that it is a new biological module. Its novelty is supported only in the limited sense that the specific cross-context co-abundance structure is not reproduced by high-confidence STRING interactions and has little direct hu.MAP representation. Absence from those resources cannot prove novelty because databases are incomplete, co-abundance is not equivalent to physical interaction, and some proteins are poorly characterized. The mixed tissue and immune-cell annotations also raise the alternative explanation that the pattern reflects shared sample composition or cellular admixture. Independent replication, preservation in additional cohorts, adjustment for cell-type abundance, and experimental testing would be needed before calling this a novel conserved mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared extracellular-interface and cellular-composition program linking myeloid or immune-associated cells with membrane receptors, glycan or proteoglycan turnover, and neural or choroid-plexus-associated signals. In this model, PLXNA4, CD44, LIFR, ADGRG6, LAYN, and CD109 mark cell-surface communication or adhesion, while GUSB, CPM, CPVL, and SIAE support processing of extracellular or membrane-associated glycans and peptides. OLFM3 and the cerebrospinal-fluid context may indicate a neural or secreted component, whereas IGHM may mark B-cell contribution. The apparent conservation between cell line and cerebrospinal fluid could therefore arise from a shared population of secretory, immune, or barrier-associated cells rather than from one intracellular pathway. This is a testable hypothesis, not an established interpretation.

### Important genes

#### PLXNA4

- **Related proteins** (co-abundance neighbors): CPM (0.97), GUSB (0.91), IGHM (0.89), CD44 (0.85), CD109 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plexin A4. Predicted to enable semaphorin receptor activity. Predicted to be involved in several processes, including axon guidance; positive regulation of axonogenesis; and regulation of GTPase activity. Predicted to act upstream of or within several processes, including nervous system development; regulation of axon extension involved in axon guidance; and regulation of negative chemotaxis. Predicted to be…
- **Diseases (Open Targets)**: neurodegenerative disease (0.518); mathematical ability (0.385); type 1 diabetes mellitus (0.337); attention deficit-hyperactivity disorder (0.333); substance abuse (0.332)
- **Europe PMC papers**: 1002
- **Why important**: PLXNA4 is the most central node in the supplied subgraph and connects to CPM, GUSB, IGHM, CD44, and CD109. It has a coherent receptor-level annotation involving semaphorin signaling, axon guidance, axonogenesis, synapse assembly, and regulation of GTPase activity. Its HPA profile includes adipose tissue, neuronal cell types, and plasmacytoid dendritic cells, making it a plausible bridge between the neural or cerebrospinal-fluid context and the immune or cellular-composition signal. It also has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports PLXNA4 as a membrane semaphorin-receptor protein with neural-development and cell-signaling functions and as the central node of this module. It is a plausible biological anchor, but the module does not establish a new PLXNA4 interaction network. A role for PLXNA4 in the shared module is therefore supported as an association and remains mechanistic hypothesis.

#### CPM

- **Related proteins** (co-abundance neighbors): PLXNA4 (0.97), OLFM3 (0.88), LAYN (0.81), LIFR (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carboxypeptidase M. The protein encoded by this gene is a membrane-bound arginine/lysine carboxypeptidase. Its expression is associated with monocyte to macrophage differentiation. This encoded protein contains hydrophobic regions at the amino and carboxy termini and has 6 potential asparagine-linked glycosylation sites. The active site residues of carboxypeptidases A and B are conserved in this protein. Three altern…
- **Diseases (Open Targets)**: salivary gland disorder (0.287); diabetic ketoacidosis (0.254); facial pain (0.233); hydronephrosis (0.232); injury (0.212)
- **Europe PMC papers**: 75251
- **Why important**: CPM is one of the most connected module members and is linked to PLXNA4, OLFM3, LAYN, and LIFR. It is a membrane-bound carboxypeptidase whose expression is associated with monocyte-to-macrophage differentiation. HPA associates it with adipose tissue, Kupffer cells, macrophages, and monocyte populations, directly matching the recurring myeloid signature of the module. Its very extensive literature makes its immune and proteolytic relevance comparatively well established.
- **Conclusion**: Established evidence supports CPM as a membrane-associated peptidase and marker of monocyte or macrophage biology. It is a strong candidate for explaining the immune or cell-composition component of the module. It is not established that CPM functionally connects to the other module proteins in this co-abundance pattern.

#### GUSB

- **Related proteins** (co-abundance neighbors): PLXNA4 (0.91), OLFM3 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09327.1
- **Function (MyGene.info)**: glucuronidase beta. This gene encodes a hydrolase that degrades glycosaminoglycans, including heparan sulfate, dermatan sulfate, and chondroitin-4,6-sulfate. The enzyme forms a homotetramer that is localized to the lysosome. Mutations in this gene result in mucopolysaccharidosis type VII. Alternative splicing results in multiple transcript variants. There are many pseudogenes of this locus in the human genome.[provid…
- **Diseases (Open Targets)**: mucopolysaccharidosis type 7 (0.878); mucopolysaccharidosis type 6 (0.439); hereditary disease (0.415); Non-immune hydrops fetalis (0.391); mucopolysaccharidosis (0.374)
- **Europe PMC papers**: 7068
- **Why important**: GUSB links the central PLXNA4 and OLFM3 portion of the network and is the only member besides CD109 represented in the hu.MAP complex (hu.MAP huMAP3_09327.1). It encodes a lysosomal hydrolase that degrades several glycosaminoglycans and is associated with mucopolysaccharidosis type seven. HPA places it in Hofbauer and Kupffer cells, consistent with the module's recurring macrophage-associated signal. Its established lysosomal and extracellular-matrix-related substrate biology gives the module a plausible glycan-processing dimension.
- **Conclusion**: Established evidence supports GUSB as a lysosomal glycosaminoglycan hydrolase with disease relevance and macrophage-associated expression. The hu.MAP overlap provides limited complex context but not a direct module mechanism. Its participation in a shared glycan-remodeling program is plausible, yet remains a hypothesis.

#### CD44

- **Related proteins** (co-abundance neighbors): PLXNA4 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD44 molecule (IN blood group). The protein encoded by this gene is a cell-surface glycoprotein involved in cell-cell interactions, cell adhesion and migration. It is a receptor for hyaluronic acid (HA) and can also interact with other ligands, such as osteopontin, collagens, and matrix metalloproteinases (MMPs). This protein participates in a wide variety of cellular functions including lymphocyte activation, recirculation and …
- **Diseases (Open Targets)**: nephrolithiasis, calcium oxalate (0.523); calcium oxalate urolithiasis (0.521); uterine corpus leiomyoma (0.480); systemic lupus erythematosus (0.467); autoimmune disease (0.330)
- **Europe PMC papers**: 102058
- **Why important**: CD44 is directly connected to the central PLXNA4 node and is a well-characterized cell-surface receptor for hyaluronan that also participates in adhesion, migration, inflammatory responses, lymphocyte biology, and interactions with matrix-associated ligands. HPA associates it with monocytes and several immune cell types and reports secretion to blood. Its very large literature and broad disease-association record make it an important interpretive marker of adhesion, immune trafficking, and extracellular-matrix context.
- **Conclusion**: Established evidence supports CD44 as a multifunctional adhesion and hyaluronan receptor involved in immune-cell movement and matrix interactions. It strengthens the interpretation that the module may reflect cellular interfaces or sample composition. The data do not show that CD44 directly mediates the co-abundance relationships.

#### LIFR

- **Related proteins** (co-abundance neighbors): ADGRG6 (0.90), CPM (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LIF receptor subunit alpha. This gene encodes a protein that belongs to the type I cytokine receptor family. This protein combines with a high-affinity converter subunit, gp130, to form a receptor complex that mediates the action of the leukemia inhibitory factor, a polyfunctional cytokine that is involved in cellular differentiation, proliferation and survival in the adult and the embryo. Mutations in this gene cause Schwar…
- **Diseases (Open Targets)**: Stüve-Wiedemann syndrome 1 (0.789); Stuve-Wiedemann syndrome (0.660); congenital anomaly of kidney and urinary tract (0.489); osteoarthritis, knee (0.393); Salivary Gland Pleomorphic Adenoma (0.370)
- **Europe PMC papers**: 7265
- **Why important**: LIFR connects CPM with ADGRG6 and is annotated as the receptor subunit that combines with gp130 to transduce leukemia inhibitory factor and related cytokine signals. Its functions include cytokine-mediated signaling, cell survival, differentiation, and proliferation. HPA associates it with astrocytes, ependymal cells, and other cell types relevant to neural or barrier tissues, while it is not detected in immune cells in the supplied summary. Its extensive literature makes it a useful candidate for linking the immune-associated and cerebrospinal-fluid-associated interpretations.
- **Conclusion**: Established evidence supports LIFR as a cytokine-receptor component with roles in differentiation, survival, and tissue signaling. Its cell-type profile is compatible with a neural or barrier-cell contribution to the module. A specific LIFR-centered mechanism connecting this module to cerebrospinal-fluid biology is not established and should be treated as a hypothesis.

#### IGHM

- **Related proteins** (co-abundance neighbors): PLXNA4 (0.89); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: immunoglobulin heavy constant mu
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 3691
- **Why important**: IGHM is the module's clearest B-cell and immunoglobulin marker. HPA associates it with lymphoid and intestinal tissues, B cells, plasma cells, and memory or naive B-cell populations. It connects to PLXNA4, providing a direct link between the module hub and a likely immune-cell or immunoglobulin component. Its established immunological identity and substantial literature make it valuable for evaluating whether the apparent conservation is driven partly by cellular admixture.
- **Conclusion**: Established evidence supports IGHM as an immunoglobulin heavy-chain constant component associated with B-cell biology. Its presence argues that immune-cell composition may contribute to the module. It does not establish a functional interaction with PLXNA4 or demonstrate that immunoglobulin biology is the core mechanism.

## Module 7

**Tissue pair**: cell line and cerebrospinal_fluid  
**Genes (15)**: AMBP, CDH6, CD14, CNTNAP2, ERBB4, IGFBP6, ITIH2, LUM, MEGF8, MERTK, NCAM1, PCOLCE, RELN, SOD3, SPOCK2

### Function

The module is best interpreted as an extracellular, cell-adhesion and tissue-interface co-abundance program with a strong neural and vascular context, rather than as a confidently defined canonical pathway. CNTNAP2, NCAM1, CDH6, RELN and ERBB4 support neuronal adhesion, cell positioning, receptor signaling and nervous-system biology. LUM, SPOCK2, PCOLCE and SOD3 support extracellular-matrix organization, collagen handling and protection from oxidative stress. MERTK and CD14 add phagocytic and innate immune receptor biology, while AMBP and ITIH2 represent extracellular protease-inhibitory and plasma-associated functions. No GO or KEGG term passed global correction, so these functional interpretations are gene-level and network-level inferences, not globally significant enrichment claims. STRING functional enrichment was absent.

**Cell composition.** The module is compositionally mixed but strongly extracellular: many members are secreted to blood, secreted in brain, or secreted to the extracellular matrix. HPA tissue annotations frequently point to brain, liver, blood vessel and choroid plexus, while single-cell annotations include neurons, glial-related populations, choroid plexus epithelial cells, hepatocytes, stromal cells and vascular-associated cells. Several genes also have monocyte, lymphoid-cell or other blood-cell annotations, although many are not detected in immune cells. This mixture argues that the shared co-abundance signal may reflect extracellular fluid composition, blood or vascular exposure, choroid-plexus biology, and shared cell-type contributions rather than a uniform intracellular program. The liver-associated secreted proteins AMBP and ITIH2, together with CD14 and other blood-linked annotations, make sample-source or blood-contamination effects an important alternative explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship reported within the module is AMBP with ITIH2, supporting a known extracellular or plasma-associated connection. No other listed module pair was supported at the stated STRING threshold, and STRING functional enrichment was absent. No hu.MAP complex contained multiple module members. Thus, most of the co-abundance edges are not established protein-complex relationships in these resources. The network may capture co-regulated abundance, shared secretion, common tissue origin, or indirect extracellular relationships rather than a physical multiprotein complex.

**STRING interactions (score >= 0.7)**: 1 of 105 gene pairs: AMBP–ITIH2 (0.97)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a potentially interesting cross-context co-abundance pattern, but the available evidence does not establish it as a new biological mechanism. Its lack of broad STRING support and absence of a hu.MAP complex are compatible with novelty, yet database absence alone cannot prove novelty. Several component genes and relationships have substantial prior literature, and the module combines well-established neural adhesion, extracellular-matrix, vascular, liver and immune biology. The most defensible conclusion is that the coordinated abundance pattern is a candidate observation requiring replication, control for blood and cell-type composition, and comparison with independent tissue or fluid cohorts before being called a novel module.

**Hypothesis.** Hypothesis: the shared module reflects a soluble and membrane-associated tissue-interface program linking neural or choroid-plexus cell adhesion and positioning with extracellular-matrix remodeling, vascular oxidative-stress control and limited innate immune or phagocytic activity. In cerebrospinal fluid, this could arise from proteins released by neural, glial, vascular or choroid-plexus sources, with liver-derived plasma proteins and blood-associated material contributing to the shared signal. The observed edges may therefore represent coordinated tissue and fluid composition, with a possible biological connection through extracellular matrix and receptor signaling, rather than direct physical assembly of all module proteins.

### Important genes

#### CNTNAP2

- **Related proteins** (co-abundance neighbors): MERTK (0.87), NCAM1 (0.84), LUM (0.81), CDH6 (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: contactin associated protein 2. This gene encodes a member of the neurexin family which functions in the vertebrate nervous system as cell adhesion molecules and receptors. This protein, like other neurexin proteins, contains epidermal growth factor repeats and laminin G domains. In addition, it includes an F5/8 type C domain, discoidin/neuropilin- and fibrinogen-like domains, thrombospondin N-terminal-like domains and a putativ…
- **Diseases (Open Targets)**: cortical dysplasia-focal epilepsy syndrome (0.789); Pitt-Hopkins-like syndrome (0.682); hereditary disease (0.537); self-limited epilepsy with centrotemporal spikes (0.496); autism (0.473)
- **Europe PMC papers**: 3686
- **Why important**: CNTNAP2 has the strongest network position in the supplied subgraph and connects neural adhesion-related members with MERTK, LUM and CDH6. HPA places it in brain and retina and in neuronal and oligodendrocyte-related cell populations. Its annotated functions include cell adhesion, axon-associated biology, nervous-system development and learning, and it has substantial literature and disease links including epilepsy, autism and cortical dysplasia.
- **Conclusion**: Established evidence supports CNTNAP2 as a neural cell-adhesion and axonal-interface component. Its central network position makes it a plausible organizer of the neural side of the module. It remains a hypothesis, not an established fact, that CNTNAP2 drives the shared co-abundance pattern.

#### RELN

- **Related proteins** (co-abundance neighbors): MEGF8 (0.88), AMBP (0.84), IGFBP6 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: reelin. This gene encodes a large secreted extracellular matrix protein thought to control cell-cell interactions critical for cell positioning and neuronal migration during brain development. This protein may be involved in schizophrenia, autism, bipolar disorder, major depression and in migration defects associated with temporal lobe epilepsy. Mutations of this gene are associated with autosomal recessi…
- **Diseases (Open Targets)**: Norman-Roberts syndrome (0.785); familial temporal lobe epilepsy 7 (0.677); temporal lobe epilepsy (0.655); autosomal dominant epilepsy with auditory features (0.583); self-limited epilepsy with centrotemporal spikes (0.517)
- **Europe PMC papers**: 7639
- **Why important**: RELN connects MEGF8, AMBP and IGFBP6 and therefore sits at a boundary between neural extracellular biology and soluble or plasma-associated proteins. It is brain-enriched, secreted in brain, and annotated for neuronal migration, axon guidance, cell morphogenesis and central nervous-system development. Its disease associations include lissencephaly and several epilepsy and neuropsychiatric conditions, and it has extensive literature.
- **Conclusion**: Established evidence supports RELN as a secreted extracellular regulator of neuronal positioning and development. Its connections to both neural and soluble members make it a strong candidate marker of a neural extracellular-fluid component. Whether RELN mediates the module's cross-tissue coordination is a hypothesis.

#### MERTK

- **Related proteins** (co-abundance neighbors): ERBB4 (0.93), SOD3 (0.92), CNTNAP2 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MER proto-oncogene, tyrosine kinase. This gene is a member of the MER/AXL/TYRO3 receptor kinase family and encodes a transmembrane protein with two fibronectin type-III domains, two Ig-like C2-type (immunoglobulin-like) domains, and one tyrosine kinase domain. Mutations in this gene have been associated with disruption of the retinal pigment epithelium (RPE) phagocytosis pathway and onset of autosomal recessive retinitis pigmentosa (…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.799); inherited retinal dystrophy (0.571); autosomal recessive retinitis pigmentosa (0.524); dengue disease (0.503); hereditary disease (0.416)
- **Europe PMC papers**: 12286
- **Why important**: MERTK is connected to ERBB4, SOD3 and CNTNAP2, linking receptor signaling with neural, vascular and extracellular features. HPA associates it with choroid plexus, astrocytes, Kupffer cells and monocyte populations. Its established functions include receptor tyrosine-kinase signaling and phagocytosis, and its disease associations prominently include retinitis pigmentosa and inherited retinal dystrophy.
- **Conclusion**: Established evidence supports MERTK as a membrane receptor involved in phagocytosis, cell-surface signaling and retinal or neural tissue biology. It is a plausible bridge between tissue-interface signaling and immune or clearance processes. A role for MERTK as a causal hub in this co-abundance module remains unproven.

#### SOD3

- **Related proteins** (co-abundance neighbors): MERTK (0.92), PCOLCE (0.86); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: superoxide dismutase 3. This gene encodes a member of the superoxide dismutase (SOD) protein family. SODs are antioxidant enzymes that catalyze the conversion of superoxide radicals into hydrogen peroxide and oxygen, which may protect the brain, lungs, and other tissues from oxidative stress. Proteolytic processing of the encoded protein results in the formation of two distinct homotetramers that differ in their ability …
- **Diseases (Open Targets)**: alcohol drinking (0.286); transient ischemic attack (0.262); urolithiasis (0.257); aortic atherosclerosis (0.252); malunion fracture (0.251)
- **Europe PMC papers**: 5713
- **Why important**: SOD3 connects MERTK with PCOLCE and is secreted to blood. HPA associates it with blood vessel and choroid plexus, while its annotated function is removal of extracellular superoxide and protection from oxidative stress. It has substantial literature and disease associations involving vascular and oxidative-stress-related conditions.
- **Conclusion**: Established evidence supports SOD3 as an extracellular antioxidant enzyme relevant to vascular and tissue-fluid environments. Its position next to MERTK and PCOLCE is consistent with a vascular or matrix-remodeling interface. Its apparent importance could also reflect shared vascular or secreted-protein abundance rather than a module-specific mechanism.

#### CD14

- **Related proteins** (co-abundance neighbors): PCOLCE (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD14 molecule. The protein encoded by this gene is a surface antigen that is preferentially expressed on monocytes/macrophages. It cooperates with other proteins to mediate the innate immune response to bacterial lipopolysaccharide, and to viruses. This gene has been identified as a target candidate in the treatment of SARS-CoV-2-infected patients to potentially lessen or inhibit a severe inflammatory response. …
- **Diseases (Open Targets)**: dengue disease (0.393); inborn error of immunity (0.370); Back pain (0.195); Sepsis (0.140); COVID-19 (0.136)
- **Europe PMC papers**: 85222
- **Why important**: CD14 links the module through PCOLCE and provides a biologically distinct immune component. HPA identifies liver enrichment, Hofbauer-cell enrichment and classical-monocyte enhancement. Its established functions include recognition of bacterial molecules, cytokine induction, receptor-mediated endocytosis and phagocytosis. It also has very extensive literature and disease associations involving infection, inflammation and sepsis.
- **Conclusion**: Established evidence supports CD14 as a soluble or vesicular innate-immune marker associated with monocytes and inflammatory recognition. In this module it is more likely to identify blood, immune-cell or extracellular-fluid contribution than to define the neural core. A direct mechanistic connection between CD14 and the neural adhesion genes is only a hypothesis.

## Module 8

**Tissue pair**: cell line and cerebrospinal_fluid  
**Genes (23)**: PAM, ASAH1, CD163, COL1A2, COL5A1, COL6A1, COL6A3, C8A, COL12A1, FBN1, FTH1, FSTL1, HPX, LAMA4, LRP1, NRP2, HSPG2, PLXNA3, PVR, SEMA7A, TNXB, THSD7A, SPOCK1

### Function

The strongest functional interpretation is an extracellular-matrix structural module. The primary evidence is the globally corrected GO molecular-function term for extracellular-matrix structural constituent (GO:MF extracellular matrix structural constituent; q_global = 0.0414), supported by the coordinated presence of collagens, fibrillin, laminin, perlecan, tenascin-X, and SPOCK1. The collagen genes form a coherent structural core, while FBN1, HSPG2, LAMA4, TNXB, and SPOCK1 represent microfibrillar, basement-membrane, proteoglycan, and matrix-regulatory components. The module also contains peripheral signals involving complement, heme handling, cell adhesion, axon guidance, and receptor-mediated uptake, but these are not globally corrected GO/KEGG findings and should not replace the matrix interpretation. The co-abundance pattern therefore most plausibly reflects extracellular-matrix production or remodeling, with possible coupling to vascular, neural, and innate-immune interfaces.

**Cell composition.** This is predominantly a secreted or extracellular-matrix-associated module rather than a conventional intracellular housekeeping module. HPA evidence shows that most members are secreted, with many directed to extracellular matrix or blood. The strongest cellular context is fibroblast-like: fibro-adipogenic progenitors, fibroblasts, hepatic stellate cells, and related stromal populations recur across the annotations. Most genes are not detected as immune-cell specific, which argues against interpreting the module primarily as a blood-cell program. However, C8A and HPX are liver- and plasma-associated, CD163 is strongly monocyte/macrophage-associated, PVR has broad myeloid enrichment, and SEMA7A, FSTL1, and LRP1 have immune or myeloid context. Thus, the shared cell-line and cerebrospinal-fluid signal may combine a stromal or matrix component with soluble plasma carryover, vascular-interface material, or shared myeloid-associated material. The HPA evidence does not provide matching protein-detection results for either sampled compartment, so it cannot establish which source contributed the measured proteins.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF extracellular matrix structural constituent | 0.0414 | COL12A1, COL1A2, COL5A1, COL6A1, COL6A3, FBN1, HSPG2, LAMA4, SPOCK1, TNXB |

### STRING and hu.MAP

STRING supports a well-established collagen and matrix neighborhood. COL1A2, COL5A1, COL6A1, and COL6A3 are densely connected, with additional links to COL12A1, FBN1, LAMA4, TNXB, and HSPG2; these relationships are concordant with a collagenous extracellular-matrix scaffold (STRING WikiPathways miRNA targets in ECM and membrane receptors; within-query FDR = 0.0182) (STRING Function Extracellular matrix structural constituent; within-query FDR = 0.0455) (STRING Keyword Extracellular matrix; within-query FDR = 0.0473). A separate STRING component links HPX with LRP1 and CD163, consistent with heme clearance and scavenger-receptor biology. Another connects NRP2, PLXNA3, and SEMA7A, consistent with semaphorin-receptor signaling. hu.MAP independently places collagen members in several partially overlapping collagen-associated complexes (hu.MAP huMAP3_13038.1) (hu.MAP huMAP3_10095.1) (hu.MAP huMAP3_06555.1) (hu.MAP huMAP3_09435.1) (hu.MAP huMAP3_10984.1) (hu.MAP huMAP3_10699.1), and places FBN1 with LRP1 in a receptor-associated complex (hu.MAP huMAP3_10712.1). These results indicate that much of the module recapitulates known physical or functional neighborhoods. They also show that the module is not a single experimentally established complex: many module members lack hu.MAP complexes, and the network contains several linked substructures rather than one uniformly connected molecular assembly.

**STRING interactions (score >= 0.7)**: 23 of 253 gene pairs: CD163–HPX (0.931); COL12A1–COL1A2 (0.793); COL12A1–COL5A1 (0.792); COL12A1–COL6A1 (0.781); COL12A1–COL6A3 (0.788); COL1A2–COL5A1 (0.989); COL1A2–COL6A1 (0.875); COL1A2–COL6A3 (0.968); COL1A2–FBN1 (0.965); COL5A1–COL6A1 (0.879); COL5A1–COL6A3 (0.892); COL5A1–FBN1 (0.929); COL5A1–TNXB (0.781); COL6A1–COL6A3 (0.994); COL6A1–FBN1 (0.743); COL6A1–LAMA4 (0.743); COL6A1–TNXB (0.725); COL6A3–FBN1 (0.786); FBN1–HSPG2 (0.849); HPX–LRP1 (0.996); HSPG2–LRP1 (0.809); NRP2–PLXNA3 (0.996); PLXNA3–SEMA7A (0.731)
**STRING functional enrichment (supplementary, within-query FDR)**: WikiPathways miRNA targets in ECM and membrane receptors (FDR = 0.0182, 6 genes); Function Extracellular matrix structural constituent (FDR = 0.0455, 9 genes); Keyword Extracellular matrix (FDR = 0.0473, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13038.1 (COL6A3, COL5A1, COL12A1; 3/40); huMAP3_10095.1 (COL6A3, COL5A1; 2/9); huMAP3_10712.1 (FBN1, LRP1; 2/12); huMAP3_06555.1 (COL6A1, COL5A1; 2/14); huMAP3_09435.1 (COL5A1, COL12A1; 2/18); huMAP3_10984.1 (COL5A1, COL12A1; 2/21); huMAP3_10699.1 (COL5A1, COL12A1; 2/28)

### Novelty

The extracellular-matrix interpretation is not biologically novel in isolation because the principal collagen, laminin, fibrillin, proteoglycan, and tenascin relationships are already represented in STRING and hu.MAP. The potentially novel aspect is the reproducible co-abundance configuration shared by cell line and cerebrospinal fluid, especially the juxtaposition of a collagen-rich stromal block with complement, heme-clearance, semaphorin, and uptake-related components. The available evidence does not establish that this configuration is a new biological mechanism. Absence of some genes from STRING or hu.MAP cannot prove novelty, because those resources capture curated or experimentally supported relationships rather than every abundance correlation. A defensible conclusion is that this is a dataset-level or cross-compartment module with a coherent known matrix core, but its specific shared-sample organization remains a hypothesis requiring independent replication and tests that distinguish true cerebrospinal-fluid biology from plasma, stromal, or cellular-composition effects.

**Hypothesis.** Hypothesis: the module represents a stromal extracellular-matrix program entering or being sampled at the cerebrospinal-fluid and cell-line interface, with collagen and basement-membrane components forming the structural scaffold. FBN1, HSPG2, LAMA4, and TNXB may organize or modulate this scaffold, while LRP1 and the HPX/CD163 neighborhood may couple matrix material to clearance of extracellular cargo and heme-related stress. The SEMA7A–PLXNA3–NRP2 branch may connect matrix state to guidance, adhesion, or vascular and neural-interface signaling. C8A may mark a soluble complement-associated component that co-varies with this matrix state rather than proving that complement is the central function. This model predicts that the module should track fibroblast or stromal abundance and extracellular-matrix protein release, and that its apparent cerebrospinal-fluid signal should be tested against blood contamination, myeloid-cell markers, and independent matrix measurements.

### Important genes

#### C8A

- **Related proteins** (co-abundance neighbors): COL12A1 (0.98), SPOCK1 (0.96), PVR (0.95), COL6A1 (0.95), COL1A2 (0.92), PAM (0.90), COL6A3 (0.87), FSTL1 (0.86), COL5A1 (0.82), HSPG2 (0.82), LAMA4 (0.82), FBN1 (0.81), LRP1 (0.80), NRP2 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C8 alpha chain. C8 is a component of the complement system and contains three polypeptides, alpha, beta and gamma. This gene encodes the alpha subunit of C8. C8 participates in the formation of the membrane attack complex (MAC). The MAC assembles on bacterial membranes to form a pore, permitting disruption of bacterial membrane organization. Mutations in this gene cause complement C8 alpha-gamma deficiency. [prov…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.690); complement deficiency (0.462); focal epilepsy (0.234); ankylosing spondylitis (0.214); pernicious anemia (0.097)
- **Europe PMC papers**: 1382
- **Why important**: C8A is the highest-connectivity hub in the module and links the collagen-rich neighborhood to SPOCK1, PVR, PAM, and other peripheral members. Its established function is as the alpha subunit of complement C8, participating in membrane-attack-complex formation, and it is annotated as a secreted blood protein with liver and hepatocyte enrichment. It has substantial literature and a disease association with complement deficiency. Its central network position is therefore informative, but its lack of STRING partners and lack of membership in the enriched matrix term show that it may be a co-abundance bridge or soluble sample-context marker rather than a matrix scaffold component.
- **Conclusion**: Established evidence supports C8A as a soluble complement component and a network hub. It is plausible, but not established, that C8A couples complement-related material to the matrix signal or reflects plasma contribution to the shared module.

#### COL1A2

- **Related proteins** (co-abundance neighbors): C8A (0.92); STRING partners: COL12A1 (0.793), COL5A1 (0.989), COL6A1 (0.875), COL6A3 (0.968), FBN1 (0.965)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type I alpha 2 chain. This gene encodes the pro-alpha2 chain of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIB, recessive Ehlers-Danlos syndrome Classi…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 2 (0.845); osteogenesis imperfecta type 3 (0.830); osteogenesis imperfecta type 4 (0.820); Ehlers-Danlos syndrome, cardiac valvular type (0.777); osteogenesis imperfecta type 1 (0.770)
- **Europe PMC papers**: 67901
- **Why important**: COL1A2 is a core fibrillar-collagen gene with strong STRING links to COL5A1, COL6A1, COL6A3, COL12A1, and FBN1, and it belongs to the globally significant extracellular-matrix term (GO:MF extracellular matrix structural constituent; q_global = 0.0414) and the supplementary STRING matrix terms (STRING WikiPathways miRNA targets in ECM and membrane receptors; within-query FDR = 0.0182) (STRING Function Extracellular matrix structural constituent; within-query FDR = 0.0455) (STRING Keyword Extracellular matrix; within-query FDR = 0.0473). HPA places it in stromal and fibroblast-like cell contexts, and its disease associations include multiple osteogenesis-imperfecta and Ehlers-Danlos phenotypes. It also has a very large literature base, making its role biologically well established.
- **Conclusion**: Established evidence identifies COL1A2 as a central fibrillar-matrix component and a strong anchor for the module's main interpretation. The module does not by itself establish altered collagen deposition or a disease mechanism in either sampled compartment.

#### COL6A1

- **Related proteins** (co-abundance neighbors): C8A (0.95); STRING partners: COL12A1 (0.781), COL1A2 (0.875), COL5A1 (0.879), COL6A3 (0.994), FBN1 (0.743), LAMA4 (0.743), TNXB (0.725)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06555.1
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is part of the collagen VI structural unit and is linked in STRING to COL6A3, COL1A2, COL5A1, COL12A1, FBN1, LAMA4, and TNXB. It is included in the primary matrix term (GO:MF extracellular matrix structural constituent; q_global = 0.0414) and all of the supplementary matrix signals (STRING WikiPathways miRNA targets in ECM and membrane receptors; within-query FDR = 0.0182) (STRING Function Extracellular matrix structural constituent; within-query FDR = 0.0455) (STRING Keyword Extracellular matrix; within-query FDR = 0.0473). HPA supports fibroblast and stromal-cell context, while disease associations include Bethlem and Ullrich congenital muscular dystrophies and collagen-six-related myopathy. Its network position connects the collagen subfamilies with basement-membrane and matrix-modulatory proteins.
- **Conclusion**: Established evidence supports COL6A1 as a structural bridge within the extracellular-matrix core. A role in organizing the particular cross-compartment module is a reasonable hypothesis, but the co-abundance data do not demonstrate direct regulation or assembly in these samples.

#### LRP1

- **Related proteins** (co-abundance neighbors): FSTL1 (0.84), C8A (0.80); STRING partners: HPX (0.996), HSPG2 (0.809)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10712.1
- **Function (MyGene.info)**: LDL receptor related protein 1. This gene encodes a member of the low-density lipoprotein receptor family of proteins. The encoded preproprotein is proteolytically processed by furin to generate 515 kDa and 85 kDa subunits that form the mature receptor (PMID: 8546712). This receptor is involved in several cellular processes, including intracellular signaling, lipid homeostasis, and clearance of apoptotic cells. In addition, the …
- **Diseases (Open Targets)**: neurodegenerative disease (0.514); keratosis pilaris atrophicans (0.499); developmental dysplasia of the hip (0.466); Alzheimer disease (0.462); Parkinson disease (0.443)
- **Europe PMC papers**: 10645
- **Why important**: LRP1 connects FSTL1 and C8A in the module and has strong STRING relationships with HPX and HSPG2. hu.MAP places it with FBN1 in a receptor-associated complex (hu.MAP huMAP3_10712.1). Its established functions include receptor-mediated endocytosis, lipid homeostasis, phagocytosis, apoptotic-cell clearance, and regulation of inflammatory responses. HPA links it to fibroblasts, fibro-adipogenic progenitors, hepatocytes, Kupffer cells, and several monocyte populations; disease associations include neurodegenerative disease, Alzheimer disease, and Parkinson disease. It therefore provides a plausible interface between matrix material, soluble cargo, and cellular clearance.
- **Conclusion**: Established evidence supports LRP1 as a multifunctional uptake and signaling receptor connected to both matrix and clearance biology. It may mediate coupling between extracellular-matrix abundance and cellular uptake in the module, but that mechanistic coupling remains unproven.

#### SEMA7A

- **Related proteins** (co-abundance neighbors): TNXB (0.93), FBN1 (0.84); STRING partners: PLXNA3 (0.731)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: semaphorin 7A (JohnMiltonHagen blood group). This gene encodes a member of the semaphorin family of proteins. The encoded preproprotein is proteolytically processed to generate the mature glycosylphosphatidylinositol (GPI)-anchored membrane glycoprotein. The encoded protein is found on activated lymphocytes and erythrocytes and may be involved in immunomodulatory and neuronal processes. The encoded protein carries the John Milton Hagen (JMH)…
- **Diseases (Open Targets)**: osteoarthritis (0.442); cholestasis, progressive familial intrahepatic, 11 (0.333); poisoning (0.331); neurodegenerative disease (0.274); stricture (0.213)
- **Europe PMC papers**: 1730
- **Why important**: SEMA7A links TNXB and FBN1 in the module and has a STRING relationship with PLXNA3. HPA associates it with brain and lymphoid tissues, neuronal populations, microglia, oligodendrocyte progenitors, and selected blood-cell types. Its established functions include axon guidance, immune response, osteoblast differentiation, cell migration, and axon extension, while disease associations include osteoarthritis and neurodegenerative disease. It is therefore a biologically informative peripheral connector between matrix organization and neural or immune-interface signaling, despite having limited direct module connectivity.
- **Conclusion**: Established evidence supports SEMA7A as a semaphorin with neuronal, immune, and migratory functions and a known relationship to PLXNA3. Its participation suggests possible neural-interface biology, but the module does not establish that SEMA7A drives the extracellular-matrix program.

## Module 9

**Tissue pair**: cell line and cerebrospinal_fluid  
**Genes (33)**: NAGLU, APOA1, BMPR2, ALCAM, CP, CHST3, CNTN3, COL6A2, COL16A1, DNER, ECE1, EMILIN1, FKRP, HGFAC, IFNAR2, ITGB2, LRP4, MAN2A2, MAN2B1, MBP, MILR1, MSLN, NBL1, NCAM2, NFASC, PRG4, SDK1, SEMA4B, SEMA4D, FAP, TENM2, TENM4, FAS

### Function

No GO or KEGG term passed global correction, so the module does not support a formally enriched pathway assignment. Its topology and annotations nevertheless suggest a mixed extracellular-interface and neural-support module. The central network hub CNTN3 connects cell-adhesion, extracellular-matrix, glycosaminoglycan-processing, receptor, and neural-associated genes. CHST3, NCAM2, DNER, SDK1, TENM2, NFASC, SEMA4D, and MBP support roles in cell adhesion, axon guidance, synapse or myelin biology, and nervous-system development. MAN2A2, MAN2B1, NAGLU, and FKRP point to glycan processing and glycoprotein modification, while CP, APOA1, and HGFAC introduce circulating and metabolic biology. Thus, the most defensible interpretation is a heterogeneous interface module reflecting extracellular organization, neural or glial cell properties, glycan biology, and sample-fluid composition rather than a single established biochemical pathway.

**Cell composition.** The module is compositionally mixed rather than a uniform neural module. Many members are secreted or extracellular-matrix proteins, including APOA1, CP, HGFAC, PRG4, COL6A2, COL16A1, EMILIN1, FAP, and NBL1. HPA also shows frequent enrichment in brain, oligodendrocytes, ependymal cells, oligodendrocyte progenitors, fibroblasts, and neutrophils. Several genes are associated with liver or circulating protein biology, especially APOA1, CP, and HGFAC, and several are enhanced in immune or blood-cell contexts, including MILR1, MAN2A2, MAN2B1, ECE1, SEMA4D, and ITGB2. Therefore, the shared cell-line and cerebrospinal-fluid signal could reflect extracellular or plasma-derived proteins, blood or immune admixture, and shared glial or ependymal-related cell types. The HPA summary reports many secreted genes and substantial cell-type specificity, arguing against interpreting the module as broadly expressed housekeeping biology. HPA protein detection is unavailable for both sampled contexts, so protein-level confirmation in these materials is not possible.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides very limited direct support: the only high-confidence interaction is COL16A1 with COL6A2. This known extracellular-matrix relationship is consistent with a matrix component but does not explain the full module. No supplementary STRING functional enrichment was reported. hu.MAP provides several partial complex links. MAN2A2, ECE1, and NAGLU recur together in C1, C2, and C9, supporting a lysosomal, Golgi, or glycan-processing neighborhood. CHST3 and SEMA4D co-occur in C3, while CP and APOA1 recur across several plasma-protein complexes (hu.MAP huMAP3_07432.1), (hu.MAP huMAP3_07265.1), (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1), (hu.MAP huMAP3_10678.1). ALCAM and SDK1 recur across multiple adhesion or membrane-associated complexes (hu.MAP huMAP3_08103.1), (hu.MAP huMAP3_09105.1), (hu.MAP huMAP3_10503.1), (hu.MAP huMAP3_08689.1), (hu.MAP huMAP3_09336.1), (hu.MAP huMAP3_11349.1). These are partial memberships in broad complexes, not proof that the entire co-abundance module is one physical complex. The contrast between sparse STRING connectivity and repeated but incomplete hu.MAP memberships suggests that the module combines several biological neighborhoods linked by abundance covariation rather than representing one established protein complex.

**STRING interactions (score >= 0.7)**: 1 of 528 gene pairs: COL16A1–COL6A2 (0.772)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (COL6A2, ECE1, MAN2A2, NAGLU; 4/60); huMAP3_09327.1 (ECE1, MAN2A2, NAGLU; 3/93); huMAP3_07949.1 (CHST3, SEMA4D; 2/12); huMAP3_07432.1 (CP, APOA1; 2/18); huMAP3_07265.1 (CP, APOA1; 2/20); huMAP3_08103.1 (ALCAM, SDK1; 2/23); huMAP3_09105.1 (ALCAM, SDK1; 2/24); huMAP3_10503.1 (ALCAM, SDK1; 2/27); huMAP3_08802.1 (ECE1, MAN2A2; 2/33); huMAP3_08689.1 (ALCAM, SDK1; 2/37); huMAP3_08395.1 (CP, APOA1; 2/43); huMAP3_09531.1 (CP, APOA1; 2/47); huMAP3_10101.1 (CP, APOA1; 2/49); huMAP3_09336.1 (ALCAM, SDK1; 2/50); huMAP3_15040.1 (CP, APOA1; 2/64); huMAP3_10678.1 (CP, APOA1; 2/71); huMAP3_11349.1 (ALCAM, SDK1; 2/78)

### Novelty

This appears to be a potentially interesting cross-context co-abundance pattern, but it cannot be called a wholly new biological mechanism from the current evidence. The module contains established biology: COL16A1 with COL6A2 is supported by STRING, several gene groupings recur in hu.MAP, and the individual proteins have substantial prior literature and disease annotation. Conversely, the complete module-level combination is not established by the supplied databases: there is no globally significant GO or KEGG term, no STRING enrichment, and only sparse direct STRING connectivity. Absence from STRING or hu.MAP is not evidence of novelty because these resources emphasize curated physical or functional relationships and may not capture co-abundance across cell line and cerebrospinal fluid. The appropriate conclusion is that the module-level organization is a candidate new observation requiring replication, tissue or cell-composition adjustment, and orthogonal protein or transcript measurements.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of extracellular-interface proteins and glycan-processing machinery contributed by neural or glial-associated cells, ependymal or cerebrospinal-fluid interfaces, and variable circulating or immune-derived material. In this model, adhesion and guidance proteins such as CNTN3, NCAM2, DNER, SDK1, TENM2, NFASC, and SEMA4D define the cellular-interface component; CHST3, MAN2A2, MAN2B1, NAGLU, and FKRP modify or recycle extracellular and membrane glycoconjugates; and APOA1, CP, HGFAC, and other secreted proteins reflect fluid or blood-associated transport and proteolytic biology. The correlation structure may therefore arise from shared cellular composition and extracellular release, with a smaller true matrix relationship represented by COL16A1 and COL6A2. This is a mechanistic hypothesis, not an established causal pathway.

### Important genes

#### CNTN3

- **Related proteins** (co-abundance neighbors): MAN2A2 (0.97), CHST3 (0.95), BMPR2 (0.94), FAP (0.93), COL6A2 (0.93), LRP4 (0.91), SEMA4D (0.91), MAN2B1 (0.91), CP (0.89), ALCAM (0.86), ITGB2 (0.85), MBP (0.85), MSLN (0.82), FAS (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: contactin 3. Predicted to be involved in cell adhesion and nervous system development. Predicted to be located in extracellular region and plasma membrane. Predicted to be active in neuron projection. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: mathematical ability (0.335); coronary artery disorder (0.325); hepatitis B virus infection (0.324); substance abuse (0.317); attention deficit-hyperactivity disorder (0.317)
- **Europe PMC papers**: 480
- **Why important**: CNTN3 is the strongest topological hub in the supplied network and connects neural-interface genes with glycan-processing, matrix, receptor, and adhesion genes. HPA places it in ependymal cells and oligodendrocyte progenitors, while its annotation supports cell adhesion and nervous-system development. Its substantial literature provides context, but the supplied databases do not show a STRING partner or hu.MAP complex for CNTN3.
- **Conclusion**: Established evidence supports CNTN3 as the network-centered cell-adhesion and neural-development anchor of the module. Hypothesis: its hub position reflects coordinated abundance of a neural or cerebrospinal-fluid interface component, although the correlations may partly reflect shared cell composition rather than direct molecular binding.

#### CHST3

- **Related proteins** (co-abundance neighbors): MILR1 (0.97), CNTN3 (0.95), PRG4 (0.93), TENM2 (0.93), MAN2A2 (0.92), NCAM2 (0.91), CP (0.88), EMILIN1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07949.1
- **Function (MyGene.info)**: carbohydrate sulfotransferase 3. This gene encodes an enzyme which catalyzes the sulfation of chondroitin, a proteoglycan found in the extracellular matrix and most cells which is involved in cell migration and differentiation. Mutations in this gene are associated with spondylepiphyseal dysplasia and humerospinal dysostosis. [provided by RefSeq, Mar 2009].
- **Diseases (Open Targets)**: spondyloepiphyseal dysplasia with congenital joint dislocations (0.819); Back pain (0.434); lumbar disc herniation (0.420); vertebral column disorder (0.406); aortic stenosis (0.383)
- **Europe PMC papers**: 635
- **Why important**: CHST3 is a highly connected intermediate and encodes an enzyme involved in sulfation of chondroitin and related proteoglycan biology. It links CNTN3 to MILR1, PRG4, TENM2, NCAM2, MAN2A2, CP, and EMILIN1, thereby bridging extracellular matrix, neural adhesion, and glycan-processing signals. HPA highlights ependymal cells and oligodendrocytes, and its disease annotation includes a skeletal dysplasia caused by altered proteoglycan biology.
- **Conclusion**: Established evidence supports CHST3 as a plausible extracellular-glycan organizer within the module, but no globally significant GO/KEGG enrichment or STRING interaction establishes it as a module-wide driver. Hypothesis: altered glycosaminoglycan modification could help coordinate the adhesion and extracellular-protein abundance pattern.

#### IFNAR2

- **Related proteins** (co-abundance neighbors): NCAM2 (0.98), MAN2A2 (0.93), HGFAC (0.85), FKRP (0.85), CP (0.84), SDK1 (0.83), NAGLU (0.83), SEMA4B (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: interferon alpha and beta receptor subunit 2. The protein encoded by this gene is a type I membrane protein that forms one of the two chains of a receptor for interferons alpha and beta. Binding and activation of the receptor stimulates Janus protein kinases, which in turn phosphorylate several proteins, including STAT1 and STAT2. The protein belongs to the type II cytokine receptor family. Mutations in this gene are associated with Immunodef…
- **Diseases (Open Targets)**: COVID-19 (0.647); immunodeficiency 45 (0.635); hepatitis B virus infection (0.609); chronic hepatitis C virus infection (0.607); neoplasm (0.604)
- **Europe PMC papers**: 5992
- **Why important**: IFNAR2 is a connected membrane receptor linking NCAM2, MAN2A2, HGFAC, FKRP, CP, SDK1, NAGLU, and SEMA4B. Its established function is receptor signaling in response to interferon alpha and beta, with relevance to antiviral defense and immunodeficiency. HPA identifies expression in brain-associated cell types and notes secretion to blood, making it a plausible bridge between neural, immune, and fluid-associated signals. It is also among the most literature-rich genes in the module.
- **Conclusion**: Established evidence supports IFNAR2 as an immune-signaling and sample-interface marker that may connect otherwise distinct module neighborhoods. Hypothesis: inflammatory or interferon-related state could influence the shared abundance pattern, but the module does not demonstrate interferon-pathway enrichment.

#### CP

- **Related proteins** (co-abundance neighbors): CNTN3 (0.89), CHST3 (0.88), IFNAR2 (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07432.1, huMAP3_07265.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: ceruloplasmin. The protein encoded by this gene is a metalloprotein that binds most of the copper in plasma and is involved in the peroxidation of Fe(II)transferrin to Fe(III) transferrin. Mutations in this gene cause aceruloplasminemia, which results in iron accumulation and tissue damage, and is associated with diabetes and neurologic abnormalities. Two transcript variants, one protein-coding and the other not…
- **Diseases (Open Targets)**: aceruloplasminemia (0.827); cerebellar ataxia (0.572); Hermansky-Pudlak syndrome 3 (0.564); Hermansky-Pudlak syndrome (0.543); neurodegeneration with brain iron accumulation (0.510)
- **Europe PMC papers**: 171928
- **Why important**: CP is connected to CNTN3, CHST3, and IFNAR2 and repeatedly appears with APOA1 in hu.MAP plasma-protein complexes (hu.MAP huMAP3_07432.1), (hu.MAP huMAP3_07265.1), (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1), (hu.MAP huMAP3_10678.1). It is a liver-enriched protein secreted to blood that participates in copper and iron homeostasis and oxidative protection. Its disease association with aceruloplasminemia and neurologic iron accumulation makes it especially relevant to cerebrospinal-fluid interpretation.
- **Conclusion**: Established evidence supports CP as a circulating metal-handling and fluid-composition component rather than a specific neural structural component. Hypothesis: CP may mark blood or liver-derived contribution to the shared module and could modify interpretation of neural-looking correlations.

#### APOA1

- **Related proteins** (co-abundance neighbors): HGFAC (0.92), FKRP (0.81); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07432.1, huMAP3_07265.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is a liver-enriched protein secreted to blood and the major protein component of HDL. It connects to HGFAC and FKRP and repeatedly occurs in the same hu.MAP plasma-protein group as CP (hu.MAP huMAP3_07432.1), (hu.MAP huMAP3_07265.1), (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1), (hu.MAP huMAP3_10678.1). Its large literature base and established roles in lipid transport and cholesterol efflux make it a strong indicator of circulating or extracellular-fluid composition.
- **Conclusion**: Established evidence supports APOA1 as a plasma-derived transport component and a likely sample-composition marker. Hypothesis: APOA1 covariance with neural-interface genes may reflect fluid transport, vascular leakage, or shared extracellular abundance rather than a direct APOA1-mediated neural mechanism.

#### MBP

- **Related proteins** (co-abundance neighbors): CNTN3 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myelin basic protein. The protein encoded by the classic MBP gene is a major constituent of the myelin sheath of oligodendrocytes and Schwann cells in the nervous system. However, MBP-related transcripts are also present in the bone marrow and the immune system. These mRNAs arise from the long MBP gene (otherwise called 'Golli-MBP') that contains 3 additional exons located upstream of the classic MBP exons. Alternative…
- **Diseases (Open Targets)**: alcohol drinking (0.394); preeclampsia (0.273); placenta praevia (0.272); duodenal ulcer (0.270); Abnormality of the dentition (0.269)
- **Europe PMC papers**: 69467
- **Why important**: MBP is tissue-enriched in brain and is a major constituent of myelin produced by oligodendrocytes and Schwann cells. It connects to the central hub CNTN3, and its annotation directly supports myelin assembly, axon ensheathment, and nervous-system development. HPA also reports oligodendrocyte association, although it notes immune-related MBP transcripts, which is relevant when interpreting cerebrospinal-fluid material.
- **Conclusion**: Established evidence supports MBP as the clearest oligodendrocyte and myelin-associated marker in the module. Hypothesis: MBP may indicate a glial or myelin-derived contribution to the shared signal, but its single network edge and the lack of global enrichment do not establish a coordinated myelin pathway.

## Module 10

**Tissue pair**: cell line and cerebrospinal_fluid  
**Genes (12)**: APOH, BCAM, GNS, HEG1, IGFBP3, KIAA1549L, ACP2, PPM1L, SEZ6L2, SEMA3C, SUMF1, TXNDC16

### Function

The module does not have a GO or KEGG term passing global correction, so its function cannot be assigned from enrichment as a statistically established result. Its gene composition nevertheless points to a mixed lysosomal and extracellular or membrane-associated biology. GNS and SUMF1 provide an established sulfatase and glycosaminoglycan-processing axis, while ACP2 supports lysosomal function. APOH and IGFBP3 represent circulating extracellular regulators, and SEMA3C, HEG1, BCAM, and SEZ6L2 are compatible with cell-surface, adhesion, guidance, or tissue-interface biology. The network is organized around KIAA1549L as the central co-abundance hub, with most other genes connected primarily through that hub rather than through a dense, functionally annotated interaction network. Overall, the safest interpretation is a shared abundance program linking a poorly characterized brain-associated membrane component to lysosomal processing, extracellular proteins, and cell-interface biology, rather than a single proven pathway.

**Cell composition.** The module is compositionally heterogeneous. Many members are secreted or extracellularly detected proteins, including APOH, IGFBP3, SEMA3C, and TXNDC16, while GNS and SUMF1 are intracellular or membrane-associated and ACP2 is lysosomal. HPA indicates broad or low tissue specificity for many genes, with additional enrichment in brain, liver, blood vessel, kidney, and placenta. Several genes show immune-cell enhancement or enrichment, particularly in monocyte, dendritic-cell, basophil, or related populations, whereas some genes are not detected in immune cells. The combination of secreted proteins, immune-associated expression, and broad tissue distribution means that the shared module could partly reflect blood or shared cellular material in the samples, rather than a dedicated cerebrospinal-fluid neuronal program. Brain-associated evidence for KIAA1549L and SEZ6L2 remains notable, but it should not be treated as proof that the entire module is neuron-specific.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module: GNS with SUMF1. This is biologically coherent because SUMF1 activates sulfatases and GNS is a lysosomal sulfatase involved in glycosaminoglycan degradation. hu.MAP independently places GNS and SUMF1 together in complex C1, although that complex contains additional proteins outside the module. SEZ6L2 and HEG1 occur together among the module members in the broad hu.MAP complex C2, but their inclusion in that large complex is only partial evidence for a direct relationship. The remaining module relationships are not supported by the reported STRING or hu.MAP records. Thus, the network contains a small established lysosomal-processing anchor and a broad cell-interface association, but most co-abundance edges should be regarded as data-derived rather than previously established molecular interactions.

**STRING interactions (score >= 0.7)**: 1 of 66 gene pairs: GNS–SUMF1 (0.802)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10485.1 (GNS, SUMF1; 2/7); huMAP3_11349.1 (SEZ6L2, HEG1; 2/78)

### Novelty

This may represent a novel shared co-abundance pattern, especially because the central KIAA1549L-centered arrangement is not supported by reported STRING partners or hu.MAP membership for most genes. However, absence from STRING or hu.MAP does not prove novelty: those resources emphasize curated or experimentally supported physical and functional relationships, whereas co-abundance can arise from regulation, secretion, cell composition, or technical effects. The presence of the known GNS-SUMF1 relationship and the partial hu.MAP associations shows that the module is not wholly unprecedented. A defensible claim is therefore that the module offers a potentially new cross-compartment association requiring replication and adjustment for blood-cell and secreted-protein effects, not that it establishes a new molecular complex or pathway.

**Hypothesis.** Hypothesis: the shared module reflects coordinated abundance of a lysosomal sulfatase-processing system together with extracellular and membrane-interface proteins, with KIAA1549L acting as a co-abundance hub rather than a proven physical scaffold. In cerebrospinal fluid, the signal could arise from a mixture of brain-associated cell material, secreted plasma proteins, and immune or vascular contributions; in cell lines, it could reflect a conserved stress, trafficking, or membrane-composition state. The GNS-SUMF1 pair supplies a plausible lysosomal-processing core, while APOH, IGFBP3, SEMA3C, HEG1, and BCAM could report extracellular transport, adhesion, guidance, or barrier-related context. This hypothesis predicts that the module will be sensitive to sample cellular composition and secretion, and that its reproducibility should be tested after controlling for blood contamination, immune-cell abundance, and cell-line identity.

### Important genes

#### KIAA1549L

- **Related proteins** (co-abundance neighbors): PPM1L (1.00), TXNDC16 (0.99), SEZ6L2 (0.94), ACP2 (0.94), APOH (0.93), IGFBP3 (0.90), GNS (0.90), SEMA3C (0.88), SUMF1 (0.84), BCAM (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: KIAA1549 like. Predicted to be integral component of membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: glaucoma (0.419); open-angle glaucoma (0.416); cataract (0.240); drug-induced dyskinesia (0.240); brain cancer (0.222)
- **Europe PMC papers**: 120
- **Why important**: KIAA1549L is the central network hub, connected to every other module member in the reported co-abundance subgraph. It has brain and parathyroid group-enriched HPA expression, including neuronal and glial cell types, and is predicted to be an integral membrane component. Its relatively limited functional characterization and modest disease associations make it especially important for interpreting whether the module contains a genuinely underexplored biological signal.
- **Conclusion**: Established evidence supports KIAA1549L as the structural co-abundance hub and as a brain-associated, putative membrane protein. It is not established that it physically organizes the other proteins or drives the module. The hypothesis that KIAA1549L marks a conserved membrane or trafficking state remains testable but unproven.

#### GNS

- **Related proteins** (co-abundance neighbors): KIAA1549L (0.90); STRING partners: SUMF1 (0.802)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10485.1
- **Function (MyGene.info)**: glucosamine (N-acetyl)-6-sulfatase. The product of this gene is a lysosomal enzyme found in all cells. It is involved in the catabolism of heparin, heparan sulphate, and keratan sulphate. Deficiency of this enzyme results in the accumulation of undegraded substrate and the lysosomal storage disorder mucopolysaccharidosis type IIID (Sanfilippo D syndrome). Mucopolysaccharidosis type IIID is the least common of the four subtypes of Sa…
- **Diseases (Open Targets)**: mucopolysaccharidosis type 3D (0.811); mucopolysaccharidosis type 3 (0.610); mucopolysaccharidosis (0.372); ventricular fibrillation (0.233); preeclampsia (0.223)
- **Europe PMC papers**: 3078
- **Why important**: GNS is a lysosomal enzyme involved in degradation of heparin, heparan sulfate, and keratan sulfate. It is directly connected to SUMF1 in STRING and co-occurs with SUMF1 in hu.MAP complex C1, giving this pair the strongest independent interaction support in the module. Its established lysosomal-storage-disease association and substantial literature make it a strong biological anchor.
- **Conclusion**: Established evidence supports GNS as part of lysosomal glycosaminoglycan catabolism and as a functionally coherent partner of SUMF1. It is reasonable to interpret the pair as an established biochemical component within the module. It is not established that the other module members participate in the same lysosomal pathway.

#### SUMF1

- **Related proteins** (co-abundance neighbors): KIAA1549L (0.84); STRING partners: GNS (0.802)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10485.1
- **Function (MyGene.info)**: sulfatase modifying factor 1. This gene encodes an enzyme that catalyzes the hydrolysis of sulfate esters by oxidizing a cysteine residue in the substrate sulfatase to an active site 3-oxoalanine residue, which is also known as C-alpha-formylglycine. Mutations in this gene cause multiple sulfatase deficiency, a lysosomal storage disorder. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 20…
- **Diseases (Open Targets)**: mucosulfatidosis (0.853); spinocerebellar ataxia type 15/16 (0.417); inherited retinal dystrophy (0.372); hereditary disease (0.341); alcohol drinking (0.311)
- **Europe PMC papers**: 764
- **Why important**: SUMF1 activates sulfatases through formation of the catalytic residue required for sulfatase activity. Its STRING relationship with GNS and shared hu.MAP complex membership provide convergent support for a lysosomal sulfatase-processing connection. Its association with multiple sulfatase-related disorders gives it strong mechanistic and disease relevance despite its peripheral position in the co-abundance graph.
- **Conclusion**: Established evidence supports SUMF1 as a sulfatase maturation factor and as a biologically meaningful partner of GNS. The module therefore contains a credible lysosomal-processing submodule. Any extension of that mechanism to KIAA1549L or the secreted proteins is a hypothesis rather than an established conclusion.

#### APOH

- **Related proteins** (co-abundance neighbors): KIAA1549L (0.93); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein H. Apolipoprotein H, also known as beta-2-glycoprotein I, is a component of circulating plasma lipoproteins. It has been implicated in a variety of physiologic pathways including lipoprotein metabolism, coagulation, hemostasis, and the production of antiphospholipid autoantibodies. APOH may be a required cofactor for anionic phospholipid binding by the antiphospholipid autoantibodies found in sera of…
- **Diseases (Open Targets)**: atrial fibrillation (0.549); metabolic syndrome (0.502); Hypercholesterolemia (0.501); aortic stenosis (0.473); familial lipoprotein lipase deficiency (0.460)
- **Europe PMC papers**: 3121
- **Why important**: APOH is a liver-enriched, hepatocyte-associated protein secreted into blood and involved in lipoprotein biology, coagulation, hemostasis, and antiphospholipid autoantibody-related processes. It is linked to cardiovascular and metabolic traits and has a substantial literature. Its presence is important because it strongly raises the possibility that the shared module includes circulating plasma material rather than only tissue-resident biology.
- **Conclusion**: Established evidence supports APOH as a secreted plasma protein with coagulation and lipid-related functions. Its co-abundance with the module hub does not establish a direct interaction or a neuronal role. A blood-derived or vascular contribution is a more conservative interpretation than assigning APOH to the lysosomal mechanism.

#### IGFBP3

- **Related proteins** (co-abundance neighbors): KIAA1549L (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor binding protein 3. This gene is a member of the insulin-like growth factor binding protein (IGFBP) family and encodes a protein with an IGFBP domain and a thyroglobulin type-I domain. The protein forms a ternary complex with insulin-like growth factor acid-labile subunit (IGFALS) and either insulin-like growth factor (IGF) I or II. In this form, it circulates in the plasma, prolonging the half-life of IGFs and alter…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.494); lymphatic system disorder (0.383); Alzheimer disease (0.368); cancer (0.365); colorectal cancer (0.365)
- **Europe PMC papers**: 9893
- **Why important**: IGFBP3 is a secreted circulating binding protein that regulates the availability and actions of insulin-like growth factors. It is placenta-enhanced, associated with extravillous trophoblasts and plasmacytoid dendritic cells in HPA, and has extensive disease and biomedical literature. Its network connection to KIAA1549L makes it a prominent indicator that the module may combine extracellular signaling with sample-composition effects.
- **Conclusion**: Established evidence supports IGFBP3 as a circulating regulator of insulin-like growth-factor signaling and as a secreted protein. Its membership does not demonstrate that insulin-like growth-factor signaling is enriched in the module, because no GO or KEGG term passed global correction. A role as an extracellular context marker is plausible, while a direct mechanistic link to KIAA1549L remains unproven.

#### SEZ6L2

- **Related proteins** (co-abundance neighbors): KIAA1549L (0.94); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11349.1
- **Function (MyGene.info)**: seizure related 6 homolog like 2. This gene encodes a seizure-related protein that is localized on the cell surface. The gene is located in a region of chromosome 16p11.2 that is thought to contain candidate genes for autism spectrum disorders (ASD), though there is no evidence directly implicating this gene in ASD. Increased expression of this gene has been found in lung cancers, and the protein is therefore considered to be a no…
- **Diseases (Open Targets)**: neurodegenerative disease (0.274); colorectal carcinoma (0.077); hepatocellular carcinoma (0.075); intrahepatic cholangiocarcinoma (0.074); neoplasm (0.065)
- **Europe PMC papers**: 559
- **Why important**: SEZ6L2 is tissue-enhanced in brain and pituitary and is expressed in multiple neuronal and pituitary cell types. Its annotations connect it to synapse maturation, cerebellar development, and behavior, while its disease and cancer associations provide substantial biological context. It also shares hu.MAP complex C2 with HEG1, offering limited support for a cell-surface or membrane-associated context.
- **Conclusion**: Established evidence supports SEZ6L2 as a brain- and pituitary-associated cell-surface protein with developmental and synaptic annotations. It provides the strongest neuronal-contextual evidence in the module, but its STRING record has no reported partners and its connection to KIAA1549L is only a co-abundance relationship. A neuronal contribution to the cerebrospinal-fluid signal is plausible, not demonstrated.

## Module 11

**Tissue pair**: cell line and cerebrospinal_fluid  
**Genes (9)**: B2M, BCHE, CSPG4, F10, SERPINB1, KNG1, LTBP1, MFGE8, DCN

### Function

The module is most consistent with a vascular and extracellular-matrix-associated secreted protein program that is coupled to circulating protease, coagulation, kinin, and inflammatory or tissue-remodelling biology. DCN is the network hub and connects the extracellular-matrix component to BCHE, MFGE8, B2M, SERPINB1, CSPG4, and LTBP1. The annotations support collagen-fibril organisation and regulation of vascular migration and angiogenesis through DCN, extracellular-matrix targeting and latent TGF-beta handling through LTBP1, apoptotic-cell clearance through MFGE8, coagulation through F10, kinin biology through KNG1, and protease control through SERPINB1. There is no globally corrected GO or KEGG enrichment term in this module, so the functional interpretation is based on the individual gene annotations, network structure, HPA patterns, and curated interaction evidence rather than on enrichment.

**Cell composition.** The module is strongly dominated by extracellular or circulating proteins: most of the genes are annotated as secreted, including proteins secreted to blood or to the extracellular matrix. HPA patterns repeatedly point to liver, blood vessel, fibroblast, pericyte, hepatic-stellate, smooth-muscle, and hepatocyte contexts. This composition makes a blood or plasma contribution, vascular or stromal contribution, or shared cellular contamination a serious explanation for the conserved signal in cell line and cerebrospinal fluid. The presence of B2M and SERPINB1 also permits an immune or myeloid-associated contribution, although several members are not detected in immune cells and the module is not uniformly immune-cell specific. The HPA data therefore support a mixed extracellular-fluid and vascular-stromal signature more strongly than a coherent cell-intrinsic neuronal program. HPA provides no matching protein-detection result for either sampled material, so protein-level presence in those materials cannot be established from this summary.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only limited direct support. The high-confidence relationships are CSPG4 with DCN and F10 with KNG1. These links independently reinforce an extracellular-matrix or vascular branch and a coagulation or plasma branch, but they do not connect the entire module into a known physical interaction network. The remaining co-abundance edges are therefore not validated as direct molecular interactions by STRING. hu.MAP provides two partial complex observations, (hu.MAP huMAP3_04508.1) and (hu.MAP huMAP3_08907.1), in which BCHE and LTBP1 occur together with additional proteins including LOXL1 and PRIMA1. Because only a subset of each complex is represented, these results support possible extracellular-matrix or associated complex biology but do not demonstrate that the full complexes are present in this module. Overall, the network appears to combine a small amount of known molecular connectivity with broader co-abundance relationships.

**STRING interactions (score >= 0.7)**: 2 of 36 gene pairs: CSPG4–DCN (0.773); F10–KNG1 (0.717)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04508.1 (BCHE, LTBP1; 2/4); huMAP3_08907.1 (BCHE, LTBP1; 2/6)

### Novelty

The shared co-abundance pattern may be novel as a tissue-pair observation, but the module should not be described as a newly discovered molecular pathway. Several members have extensive prior literature and the module contains known STRING links and partial hu.MAP complex membership. Its potentially new aspect is the coordinated appearance of these extracellular, vascular, hepatic, coagulation, and protease regulators across the two sample contexts. However, the sparse direct interaction support, absence of globally significant GO or KEGG enrichment, and strong secreted and tissue-composition signal mean that a technical, plasma-derived, or shared-cell explanation remains plausible. Absence of additional STRING or hu.MAP relationships would not by itself establish novelty.

**Hypothesis.** Hypothesis: the module reflects co-variation of extracellular-matrix remodelling and vascular-interface proteins with liver-derived and plasma-derived haemostatic factors in the sampled material. In this model, DCN, LTBP1, and CSPG4 represent an extracellular vascular-stromal scaffold; MFGE8 may couple that environment to clearance of apoptotic material; and F10, KNG1, BCHE, and SERPINB1 represent circulating protease, coagulation, kinin, and protease-inhibitory activities. B2M could report a broadly distributed or inflammatory component. The hypothesis predicts that the apparent conservation would weaken after controlling for plasma abundance, vascular or stromal cell content, and shared sample handling effects. It does not imply that these proteins form one physical complex or that the module is specifically cerebrospinal-fluid neuronal biology.

### Important genes

#### DCN

- **Related proteins** (co-abundance neighbors): LTBP1 (0.96), BCHE (0.93), CSPG4 (0.90), B2M (0.87), MFGE8 (0.85), SERPINB1 (0.80); STRING partners: CSPG4 (0.773)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: decorin. This gene encodes a member of the small leucine-rich proteoglycan family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature protein. This protein plays a role in collagen fibril assembly. Binding of this protein to multiple cell surface receptors mediates its role in tumor…
- **Diseases (Open Targets)**: congenital stromal corneal dystrophy (0.696); lagophthalmos (0.295); refractive error (0.234); type 2 diabetes mellitus (0.224); hereditary disease (0.193)
- **Europe PMC papers**: 11630
- **Why important**: DCN is the principal network hub, linking the extracellular-matrix branch to most of the other module members. Its annotation supports collagen-fibril assembly, regulation of autophagy, inhibition of endothelial migration and angiogenesis, and tumour-related receptor signalling. HPA places it in stromal, fibroblast, hepatic-stellate, and decidual-stromal contexts and annotates it as secreted to the extracellular matrix. It also has very substantial literature and disease associations including congenital stromal corneal dystrophy and metabolic disease. The DCN-CSPG4 STRING relationship provides direct external support for part of its network position.
- **Conclusion**: Established: DCN is the strongest connective and extracellular-matrix indicator in the module and is a plausible marker of vascular or stromal sample composition. Hypothesis: DCN may organise the module by coupling matrix state to circulating inflammatory and haemostatic proteins, but the co-abundance data do not establish such causal regulation.

#### LTBP1

- **Related proteins** (co-abundance neighbors): DCN (0.96); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_04508.1, huMAP3_08907.1
- **Function (MyGene.info)**: latent transforming growth factor beta binding protein 1. The protein encoded by this gene belongs to the family of latent TGF-beta binding proteins (LTBPs). The secretion and activation of TGF-betas is regulated by their association with latency-associated proteins and with latent TGF-beta binding proteins. The product of this gene targets latent complexes of transforming growth factor beta to the extracellular matrix, where the latent cytokine is subse…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.551); diverticular disease (0.523); autosomal recessive cutis laxa type 2 (0.507); osteoarthritis, knee (0.485); osteoarthritis, hip (0.467)
- **Europe PMC papers**: 2354
- **Why important**: LTBP1 is directly connected to DCN and appears with BCHE in both reported hu.MAP complexes, (hu.MAP huMAP3_04508.1) and (hu.MAP huMAP3_08907.1). Its established function is to target latent TGF-beta complexes to the extracellular matrix and regulate their activation and localisation. HPA associates it with blood vessels, fibroblasts, hepatic stellate cells, and progenitor populations. Its disease associations include skeletal abnormalities and osteoarthritis, consistent with matrix biology.
- **Conclusion**: Established: LTBP1 supports an extracellular-matrix and latent TGF-beta interpretation and gives the module a plausible signalling-regulatory component. Hypothesis: its co-abundance with DCN and BCHE may mark a shared matrix-associated complex or coordinated secretion state, but partial complex membership is not proof of a complete functional assembly.

#### BCHE

- **Related proteins** (co-abundance neighbors): DCN (0.93), KNG1 (0.90); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_04508.1, huMAP3_08907.1
- **Function (MyGene.info)**: butyrylcholinesterase. This gene encodes a cholinesterase enzyme and member of the type-B carboxylesterase/lipase family of proteins. The encoded enzyme exhibits broad substrate specificity and is involved in the detoxification of poisons including organophosphate nerve agents and pesticides, and the metabolism of drugs including cocaine, heroin and aspirin. Humans homozygous for certain mutations in this gene exhibit p…
- **Diseases (Open Targets)**: butyrylcholinesterase deficiency (0.805); Alzheimer disease (0.628); Parkinson disease (0.608); dementia (0.608); mathematical ability (0.358)
- **Europe PMC papers**: 22805
- **Why important**: BCHE is connected to both DCN and KNG1 and is the only gene in the module that is represented with LTBP1 in both hu.MAP complex records, (hu.MAP huMAP3_04508.1) and (hu.MAP huMAP3_08907.1). It encodes a circulating cholinesterase with broad substrate specificity and roles in xenobiotic and drug metabolism. HPA describes liver enrichment and secretion to blood, with expression in several glial and hepatic-related cell types. It has extensive literature and disease associations involving enzyme deficiency, Alzheimer disease, Parkinson disease, and dementia.
- **Conclusion**: Established: BCHE is a strong indicator of a liver-derived or blood-borne component and provides a biochemical bridge between the plasma branch and the partial hu.MAP complexes. Hypothesis: BCHE could contribute to the co-abundance signal through coordinated secretion or shared extracellular handling, but the data do not show that its cholinesterase activity drives the module.

#### KNG1

- **Related proteins** (co-abundance neighbors): BCHE (0.90); STRING partners: F10 (0.717)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kininogen 1. This gene uses alternative splicing to generate two different proteins- high molecular weight kininogen (HMWK) and low molecular weight kininogen (LMWK). HMWK is essential for blood coagulation and assembly of the kallikrein-kinin system. Also, bradykinin, a peptide causing numerous physiological effects, is released from HMWK. Bradykinin also functions as an antimicrobial peptide with antibacteri…
- **Diseases (Open Targets)**: congenital high-molecular-weight kininogen deficiency (0.733); venous thromboembolism (0.547); hereditary angioedema (0.458); serum lipopolysaccharide activity (0.367); ischemic stroke (0.363)
- **Europe PMC papers**: 2325
- **Why important**: KNG1 is connected to BCHE and has an independent STRING relationship with F10, linking the kinin system to coagulation. Its products include high- and low-molecular-weight kininogen; the high-molecular-weight form participates in coagulation and releases bradykinin. HPA shows liver enrichment, hepatocyte association, and secretion to blood. Its disease associations include kininogen deficiency, venous thromboembolism, hereditary angioedema, and ischemic stroke.
- **Conclusion**: Established: KNG1 is a biologically informative marker of circulating coagulation and vasoactive-kinin biology, and the KNG1-F10 relationship supports that branch of the module. Hypothesis: this branch may reflect shared plasma abundance or vascular injury-related biology rather than a specific interaction with the matrix branch.

#### F10

- **Related proteins** (co-abundance neighbors): MFGE8 (0.85); STRING partners: KNG1 (0.717)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coagulation factor X. This gene encodes the vitamin K-dependent coagulation factor X of the blood coagulation cascade. This factor undergoes multiple processing steps before its preproprotein is converted to a mature two-chain form by the excision of the tripeptide RKR. Two chains of the factor are held together by 1 or more disulfide bonds; the light chain contains 2 EGF-like domains, while the heavy chain contains th…
- **Diseases (Open Targets)**: factor X deficiency (0.830); venous thromboembolism (0.739); congenital factor X deficiency (0.732); pulmonary embolism (0.683); atrial fibrillation (0.632)
- **Europe PMC papers**: 19092
- **Why important**: F10 is a liver-enriched secreted coagulation factor and is connected to MFGE8 in the module while also having the known STRING relationship with KNG1. Its established role is activation of the common blood-coagulation pathway and zymogen processing. HPA associates it with hepatocytes, fibroblasts, decidual stromal cells, and vascularly relevant contexts. It has extensive literature and disease associations involving factor X deficiency, venous thromboembolism, pulmonary embolism, and atrial fibrillation.
- **Conclusion**: Established: F10 identifies a plasma haemostasis component and strengthens the interpretation that sample composition may contribute substantially to the module. Hypothesis: its co-abundance with MFGE8 could indicate coupling between coagulation and vascular or apoptotic-cell-removal states, but that mechanism is not demonstrated here.

#### MFGE8

- **Related proteins** (co-abundance neighbors): DCN (0.85), F10 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: milk fat globule EGF and factor V/VIII domain containing. This gene encodes a preproprotein that is proteolytically processed to form multiple protein products. The major encoded protein product, lactadherin, is a membrane glycoprotein that promotes phagocytosis of apoptotic cells. This protein has also been implicated in wound healing, autoimmune disease, and cancer. Lactadherin can be further processed to form a smaller cleavage product, medin, which c…
- **Diseases (Open Targets)**: AL amyloidosis (0.462); angina pectoris (0.339); myocardial ischemia (0.333); coronary artery bypass (0.314); coronary atherosclerosis (0.312)
- **Europe PMC papers**: 2623
- **Why important**: MFGE8 connects DCN to F10, thereby occupying a potentially informative position between extracellular matrix and coagulation-related signals. Its established function includes recognition and phagocytic clearance of apoptotic cells, with additional links to wound healing, autoimmune disease, cancer, and vascular amyloid through its processed products. HPA associates it with blood vessels, fibroblasts, pericytes, and decidual stromal cells and annotates it as secreted to blood. Its disease associations include vascular and cardiac disorders.
- **Conclusion**: Established: MFGE8 is a plausible vascular-interface and tissue-clearance marker that connects two otherwise distinct portions of the module. Hypothesis: it may represent a transition between matrix remodelling, apoptotic-cell clearance, and haemostatic activity, although the sparse interaction evidence does not establish that integrated mechanism.

## Module 12

**Tissue pair**: cell line and cerebrospinal_fluid  
**Genes (16)**: B3GNT2, CPE, CFH, EPHB3, GPX3, ITIH4, KIT, POFUT4, SERPINF1, PLXNA1, ELFN2, PRNP, SCG3, SIRPA, ST3GAL6, SUSD5

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established pathway-level assignment from enrichment analysis. Its component annotations and network structure instead suggest a mixed extracellular and cell-surface biology involving secreted proteins, glycoprotein and glycolipid processing, neuroendocrine vesicle biology, receptor-mediated signaling, cell adhesion, complement regulation, acute-phase biology, and protection from oxidative stress. The strongest functional interpretation is therefore a tissue-interface or secretory environment rather than a single canonical pathway. The brain, choroid-plexus, astrocyte, retinal, and glial annotations are compatible with cerebrospinal-fluid-associated biology, while liver and immune-cell annotations indicate that circulating or inflammatory biology may also contribute.

**Cell composition.** The module is compositionally heterogeneous but contains a substantial secreted or extracellular component, including SERPINF1, ITIH4, CFH, and GPX3, with SERPINF1 and GPX3 secreted to blood and ITIH4 and CFH also secreted to blood. HPA reports several tissue-enhanced genes in brain, retina, liver, and choroid plexus, and many cell-type-enhanced genes in astrocytes, Bergmann glia, retinal pigment epithelial cells, and related epithelial populations. Some genes are enriched or enhanced in neutrophils, eosinophils, basophils, monocytes, or other immune populations, although several are not detected in immune cells. This pattern does not indicate a purely blood-cell module, but it does make blood-derived proteins, shared secretory compartments, and shared cell types plausible contributors to the co-abundance signal. The lack of matching HPA protein-detection data for the two sampled contexts limits direct protein-level localization claims.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a high-confidence relationship between B3GNT2 and ST3GAL6, consistent with coordinated glycan biosynthesis, and another relationship between CPE and SCG3, consistent with secretory-vesicle and neuroendocrine protein processing. No STRING functional-enrichment result was reported. hu.MAP provides several partially overlapping complexes: CFH, GPX3, and ITIH4 occur together in (hu.MAP huMAP3_10678.1), GPX3 and ITIH4 recur in (hu.MAP huMAP3_09531.1) and (hu.MAP huMAP3_10101.1), CFH and ITIH4 recur in (hu.MAP huMAP3_15040.1), and POFUT4 and PLXNA1 occur together in (hu.MAP huMAP3_09327.1). These complexes contain many additional plasma, complement, coagulation, lipid-transport, and extracellular proteins outside the module. Thus, the known relationships support selected biochemical and secretory substructures, but they do not establish that the entire module is one physical complex. The sparse STRING connectivity and partial hu.MAP overlaps favor a co-abundance assembly of related compartments or cell sources rather than a single experimentally defined molecular machine.

**STRING interactions (score >= 0.7)**: 2 of 120 gene pairs: B3GNT2–ST3GAL6 (0.942); CPE–SCG3 (0.803)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10678.1 (CFH, GPX3, ITIH4; 3/71); huMAP3_09531.1 (GPX3, ITIH4; 2/47); huMAP3_10101.1 (GPX3, ITIH4; 2/49); huMAP3_15040.1 (CFH, ITIH4; 2/64); huMAP3_09327.1 (POFUT4, PLXNA1; 2/93)

### Novelty

The module should not be called a new biological pathway or complex. Its individual components and several relationships are already well established, including the B3GNT2–ST3GAL6 glycosylation relationship, the CPE–SCG3 secretory relationship, and the hu.MAP associations involving CFH, GPX3, ITIH4, POFUT4, and PLXNA1. At the same time, the particular cross-tissue co-abundance combination is not explained by one of those known complexes, and most module-member pairs lack reported STRING or hu.MAP support. This makes the module potentially novel as a reproducible tissue-pair co-abundance pattern, but not sufficient evidence for a newly discovered mechanism. Replication in independent cell-line and cerebrospinal-fluid datasets, adjustment for blood contamination and cell composition, and experimental testing of the proposed links would be required before claiming novelty.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of secreted, vesicular, glycosylated, and surface-signaling proteins at a brain or choroid-plexus–fluid interface, with contributions from circulating liver-derived and immune-associated proteins. In this model, glycan-processing enzymes such as B3GNT2, ST3GAL6, and POFUT4 modify or traffic membrane and secreted proteins; CPE and SCG3 mark regulated secretory-vesicle biology; KIT, PLXNA1, SIRPA, and EPHB3 represent signaling or adhesion interfaces; and SERPINF1, GPX3, CFH, and ITIH4 provide extracellular neurotrophic, antioxidant, complement-regulatory, and acute-phase functions. The hypothesis is supported by the annotations, HPA localization patterns, STRING edges, and partial hu.MAP overlaps, but it remains unproven because global enrichment was negative and most pairwise relationships are not known.

### Important genes

#### KIT

- **Related proteins** (co-abundance neighbors): SERPINF1 (0.98), SUSD5 (0.97), CFH (0.86), EPHB3 (0.82), CPE (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: KIT proto-oncogene, receptor tyrosine kinase. This gene encodes a receptor tyrosine kinase. This gene was initially identified as a homolog of the feline sarcoma viral oncogene v-kit and is often referred to as proto-oncogene c-Kit. The canonical form of this glycosylated transmembrane protein has an N-terminal extracellular region with five immunoglobulin-like domains, a transmembrane region, and an intracellular tyrosine kinase domain at th…
- **Diseases (Open Targets)**: gastrointestinal stromal tumor (0.893); piebaldism (0.816); cutaneous mastocytosis (0.810); acute myeloid leukemia (0.741); chronic myeloid leukemia (0.698)
- **Europe PMC papers**: 1608759
- **Why important**: KIT has the strongest network centrality in the module and connects the secretory, extracellular, and receptor-associated portions of the graph, including SERPINF1, SUSD5, CFH, EPHB3, and CPE. It encodes a stem-cell-factor-responsive receptor tyrosine kinase with established roles in hematopoietic progenitor differentiation, mast-cell biology, cytokine regulation, and developmental signaling. Its HPA profile includes mast cells and several immune-associated populations, and its disease associations include gastrointestinal stromal tumor, piebaldism, mastocytosis, and myeloid leukemia. It is also one of the most extensively studied genes in the module.
- **Conclusion**: Established evidence supports KIT as a signaling and cell-composition marker that could connect immune, vascular, epithelial, and secretory sources. It is not established that KIT mechanistically drives the whole module; its central position may instead reflect shared source-cell abundance or coordinated receptor-associated biology.

#### SCG3

- **Related proteins** (co-abundance neighbors): PLXNA1 (0.90), CPE (0.88), SIRPA (0.81); STRING partners: CPE (0.803)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: secretogranin III. The protein encoded by this gene is a member of the chromogranin/secretogranin family of neuroendocrine secretory proteins. Granins may serve as precursors for biologically active peptides. Some granins have been shown to function as helper proteins in sorting and proteolytic processing of prohormones; however, the function of this protein is unknown. Two transcript variants encoding different iso…
- **Diseases (Open Targets)**: osteoarthritis, knee (0.403); intelligence (0.341); osteoarthritis, hip (0.317); placental abruption (0.253); total knee arthroplasty (0.212)
- **Europe PMC papers**: 797
- **Why important**: SCG3 occupies a connecting position between PLXNA1, CPE, and SIRPA and has a STRING relationship with CPE. HPA places it in brain, pituitary gland, and retina, with astrocyte, Bergmann glia, neuronal, and endocrine-cell enrichment, and reports secretion in brain. Its annotation links it to secretory-granule protein localization, while the gene encodes a neuroendocrine secretogranin whose precise function remains incompletely defined. Its literature base is substantial and includes neuroendocrine and brain-related investigation.
- **Conclusion**: Established evidence supports SCG3 as a brain-associated secretory-vesicle marker and as a plausible contributor to the CPE-linked secretory substructure. A direct role in coordinating the other module branches is a hypothesis rather than an established function.

#### SERPINF1

- **Related proteins** (co-abundance neighbors): KIT (0.98), GPX3 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family F member 1. This gene encodes a member of the serpin family that does not display the serine protease inhibitory activity shown by many of the other serpin proteins. The encoded protein is secreted and strongly inhibits angiogenesis. In addition, this protein is a neurotrophic factor involved in neuronal differentiation in retinoblastoma cells. Mutations in this gene were found in individuals with osteogenesi…
- **Diseases (Open Targets)**: osteogenesis imperfecta (0.716); osteogenesis imperfecta, recessive (0.462); osteogenesis imperfecta type 3 (0.447); osteogenesis imperfecta type 4 (0.371); refractive error (0.348)
- **Europe PMC papers**: 2744
- **Why important**: SERPINF1 connects KIT and GPX3 and is tissue-enriched in choroid plexus, with secretion to blood and cell-type associations involving retinal pigment epithelial and stromal populations. Its protein is a secreted serpin-family member with anti-angiogenic and neurotrophic activities, and its disease associations include osteogenesis imperfecta and refractive disorders. It has a large literature base relative to many module members and provides a biologically meaningful bridge between extracellular signaling, vascular regulation, retina, and nervous-system support.
- **Conclusion**: Established evidence supports SERPINF1 as an extracellular neurovascular and secretory component that is particularly relevant to a cerebrospinal-fluid-associated interpretation. Its connection to KIT and GPX3 may indicate coordinated abundance, but a direct regulatory interaction within this module is not established.

#### ITIH4

- **Related proteins** (co-abundance neighbors): SUSD5 (0.85), POFUT4 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 4. The protein encoded by this gene is secreted into the blood, where it is cleaved by plasma kallikrein into two smaller forms. Expression of this gene has been detected only in liver, and it seems to be upregulated during surgical trauma. This gene is part of a cluster of similar genes on chromosome 3. Two transcript variants encoding different isoforms have been found for this gene. [provided by R…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.466); coronary artery disorder (0.417); type 2 diabetes mellitus (0.397); osteoarthritis (0.387); diabetes mellitus (0.363)
- **Europe PMC papers**: 1710
- **Why important**: ITIH4 connects SUSD5 and POFUT4 and is represented in several hu.MAP complexes, including complexes that also contain CFH and GPX3. It is liver-enriched, secreted to blood, and associated in HPA with astrocytes, Bergmann glia, neurons, and ependymal cells. Its established functions and annotations include acute-phase response, hyaluronan metabolism, and cytokine response. Its disease associations span inflammatory, metabolic, cardiovascular, and skeletal conditions, and it has a substantial literature record.
- **Conclusion**: Established evidence supports ITIH4 as an extracellular matrix-associated and acute-phase protein that could connect liver-derived circulating material with nervous-system and fluid-interface signals. Its repeated complex membership supports biochemical context, but does not prove that it physically binds every module member.

#### CPE

- **Related proteins** (co-abundance neighbors): SCG3 (0.88), KIT (0.80); STRING partners: SCG3 (0.803)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles, Centrosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carboxypeptidase E. This gene encodes a member of the M14 family of metallocarboxypeptidases. The encoded preproprotein is proteolytically processed to generate the mature peptidase. This peripheral membrane protein cleaves C-terminal amino acid residues and is involved in the biosynthesis of peptide hormones and neurotransmitters, including insulin. This protein may also function independently of its peptidase activ…
- **Diseases (Open Targets)**: BDV syndrome (0.703); hereditary disease (0.414); neurodegenerative disease (0.314); atopic eczema (0.262); rhabdomyolysis (0.260)
- **Europe PMC papers**: 29435
- **Why important**: CPE connects SCG3 and KIT and forms the second high-confidence STRING-supported pair with SCG3. It is enriched in brain and retina, associated with astrocytes, Bergmann glia, photoreceptors, and pituitary cell types, and localized to vesicles and centrosomes. Its established functions include peptide-hormone and neurotransmitter biosynthesis, proteolysis, peptide metabolism, neuropeptide signaling, and intracellular protein localization. It is among the most extensively studied genes in the module and has reported associations with neurodegenerative and other disorders.
- **Conclusion**: Established evidence supports CPE as a core secretory and peptide-processing component, making it one of the strongest anchors for a neural or neuroendocrine interpretation. The data do not establish that CPE organizes the whole module; its co-abundance may reflect shared vesicular activity or cell-type composition.

#### CFH

- **Related proteins** (co-abundance neighbors): KIT (0.86); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_15040.1
- **Function (MyGene.info)**: complement factor H. This gene is a member of the Regulator of Complement Activation (RCA) gene cluster and encodes a protein with twenty short consensus repeat (SCR) domains. This protein is secreted into the bloodstream and has an essential role in the regulation of complement activation, restricting this innate defense mechanism to microbial infections. Mutations in this gene have been associated with hemolytic-ure…
- **Diseases (Open Targets)**: complement factor H deficiency (0.769); age-related macular degeneration (0.750); atypical hemolytic-uremic syndrome (0.729); age related macular degeneration 4 (0.711); Doyne honeycomb retinal dystrophy (0.688)
- **Europe PMC papers**: 9287
- **Why important**: CFH links to KIT in the co-abundance graph and appears with ITIH4 in multiple hu.MAP complexes. It is liver-enriched, secreted to blood, and associated with complement regulation, inflammatory response, alternative-pathway control, neurogenesis, and central-nervous-system myelination. Its disease associations include complement factor H deficiency, atypical hemolytic uremic syndrome, and age-related macular degeneration, and it has a very large literature base. It provides a strong extracellular innate-immunity axis within an otherwise neural and secretory module.
- **Conclusion**: Established evidence supports CFH as a circulating complement-regulatory protein that could report extracellular immune balance or blood-derived material in the samples. Its presence does not demonstrate active complement signaling in the module, and any proposed interaction with KIT or the neural secretory branch remains hypothetical.

## Module 13

**Tissue pair**: cell line and cerebrospinal_fluid  
**Genes (13)**: CDH2, CHST7, CLSTN3, ERBB3, SERPIND1, HSPA13, LSAMP, NTM, GPLD1, PLXDC2, QPCT, TIMP1, TIMP2

### Function

No GO or KEGG term passed global correction, so the module does not support a formally significant pathway assignment. Its gene-level evidence points instead to a mixed extracellular and cell-surface biology involving neural adhesion and synaptic organization, receptor signaling, extracellular-matrix regulation, protease inhibition, glycoprotein processing, and protein quality control. NTM, LSAMP, CLSTN3, and CDH2 support a neuronal or glial adhesion and synapse-related interpretation. SERPIND1, TIMP1, and TIMP2 support regulation of extracellular proteolysis, while ERBB3 provides a receptor-signaling component. These annotations are mechanistic context rather than enrichment claims.

**Cell composition.** The module is heterogeneous rather than a uniformly neuronal program. Many members are secreted, extracellular, membrane-associated, or vesicle-associated proteins, including SERPIND1, GPLD1, QPCT, TIMP1, and TIMP2. HPA tissue evidence is distributed across brain, retina, liver, heart muscle, ovary, blood vessel, adrenal gland, and other tissues. The single-cell annotations are especially frequent for brain neuronal and glial populations, but several genes are also associated with neutrophils, monocytes, basophils, or other immune populations. SERPIND1 and GPLD1 are liver-enriched and secreted to blood, and QPCT is associated with neutrophils and is secreted to blood. Therefore, the shared co-abundance pattern could reflect extracellular or blood-derived protein carryover, shared vascular or immune material, or broad sample composition effects, rather than a cell-intrinsic program specific to cerebrospinal fluid or cell lines. HPA provides no matching protein-detection result for either sampled context.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and there are no STRING functional-enrichment terms. No hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not corroborated by the queried physical-interaction or complex resources. This does not disprove coordinated abundance: the relationships may be indirect, tissue- or fluid-dependent, condition-dependent, below database thresholds, or driven by shared secretion, membrane shedding, extracellular transport, or cellular composition. The strongest network connections should therefore be treated as empirical co-abundance relationships rather than established molecular interactions.

**STRING interactions (score >= 0.7)**: 0 of 78 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported co-abundance pattern in this tissue pair, because it lacks high-confidence STRING interactions, STRING enrichment, and hu.MAP multi-member complexes. However, absence from these resources does not establish biological novelty. Most individual genes and several relevant functions are already well studied, including neural adhesion for NTM, LSAMP, CLSTN3, and CDH2, protease inhibition for SERPIND1 and the TIMPs, and receptor signaling for ERBB3. The defensible novelty claim is therefore limited to the particular cross-context co-abundance configuration and its possible relationship to extracellular, neural, vascular, and immune composition. Independent replication, adjustment for cell-type composition, and comparison with published co-abundance modules would be needed before calling it a new biological mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of extracellular and membrane-associated proteins contributed by a mixture of neural or glial material, vascular or blood-derived proteins, and immune-associated material. Within that mixture, an adhesion and signaling axis involving NTM, LSAMP, CLSTN3, CDH2, and ERBB3 may be coupled indirectly to extracellular protease control through SERPIND1, TIMP1, and TIMP2, with GPLD1 and QPCT contributing to processing or release of extracellular proteins. This is a hypothesis generated from co-abundance and annotations, not an experimentally demonstrated physical pathway.

### Important genes

#### NTM

- **Related proteins** (co-abundance neighbors): SERPIND1 (0.97), TIMP2 (0.87), PLXDC2 (0.81), LSAMP (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neurotrimin. This gene encodes a member of the IgLON (LAMP, OBCAM, Ntm) family of immunoglobulin (Ig) domain-containing glycosylphosphatidylinositol (GPI)-anchored cell adhesion molecules. The encoded protein may promote neurite outgrowth and adhesion via a homophilic mechanism. This gene is closely linked to a related family member, opioid binding protein/cell adhesion molecule-like (OPCML), on chromosome 11.…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.453); smoking initiation (0.429); refractive error (0.429); health study participation (0.404); hyperopia (0.383)
- **Europe PMC papers**: 7389
- **Why important**: NTM is the most connected node in the module and links SERPIND1, TIMP2, PLXDC2, and LSAMP. It encodes neurotrimin, a GPI-anchored IgLON cell-adhesion molecule associated with neurite outgrowth, neuron recognition, and synapse assembly. Its brain and retina tissue enhancement and broad neuronal and astrocytic cell-type associations make it a central candidate for the neural component. It also has substantial literature and several Open Targets associations.
- **Conclusion**: Established evidence supports NTM as a neuronal cell-adhesion and neurite-related protein and as a central empirical connector in this module. It is plausible, but unproven, that NTM helps organize the neural or glial component of the co-abundance pattern.

#### SERPIND1

- **Related proteins** (co-abundance neighbors): NTM (0.97), CLSTN3 (0.89), QPCT (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family D member 1. This gene belongs to the serpin gene superfamily. Serpins play roles in many processes including inflammation, blood clotting, and cancer metastasis. Members of this family have highly conserved secondary structures with a reactive center loop that interacts with the protease active site to inhibit protease activity. This gene encodes a plasma serine protease that functions as a thrombin and chymo…
- **Diseases (Open Targets)**: heparin cofactor 2 deficiency (0.721); Venous thrombosis (0.670); hemorrhage (0.266); neurodegenerative disease (0.265); thrombotic disease (0.120)
- **Europe PMC papers**: 1066
- **Why important**: SERPIND1 is a highly connected intermediary linking NTM, CLSTN3, and QPCT. It encodes a secreted plasma serine-protease inhibitor involved in blood coagulation and is liver-enriched, hepatocyte-enriched, and secreted to blood. Its disease associations include heparin cofactor deficiency and venous thrombosis. This makes it important for evaluating whether the module partly reflects blood-derived or extracellular material rather than a neural intracellular program.
- **Conclusion**: Established evidence supports SERPIND1 as a circulating anticoagulant-related protein and a marker of possible blood or liver contribution. Its connection to neural adhesion proteins is a co-abundance observation, not evidence of a direct molecular interaction.

#### ERBB3

- **Related proteins** (co-abundance neighbors): GPLD1 (0.90), QPCT (0.84), CHST7 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: erb-b2 receptor tyrosine kinase 3. This gene encodes a member of the epidermal growth factor receptor (EGFR) family of receptor tyrosine kinases. This membrane-bound protein has a neuregulin binding domain but not an active kinase domain. It therefore can bind this ligand but not convey the signal into the cell through protein phosphorylation. However, it does form heterodimers with other EGF receptor family members which do have k…
- **Diseases (Open Targets)**: visceral neuropathy, familial, 1, autosomal recessive (0.735); lethal congenital contracture syndrome 2 (0.702); cancer (0.664); urinary bladder cancer (0.604); urinary bladder carcinoma (0.600)
- **Europe PMC papers**: 14679
- **Why important**: ERBB3 is a connected signaling node linking GPLD1, QPCT, and CHST7. It is an EGFR-family receptor with a neuregulin-binding domain and impaired intrinsic kinase activity that can signal through heterodimerization with other family members. Its annotations include receptor signaling, nervous-system development, and heart development, while HPA links it to oligodendrocytes and other cell types. It has extensive literature and disease associations including cancer and developmental disorders.
- **Conclusion**: Established evidence supports ERBB3 as a receptor and developmental signaling component. The module does not establish that ERBB3 directly coordinates with the neighboring proteins, but it makes receptor-mediated regulation a reasonable mechanistic possibility.

#### CLSTN3

- **Related proteins** (co-abundance neighbors): CDH2 (0.91), SERPIND1 (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calsyntenin 3. Predicted to enable calcium ion binding activity. Predicted to be involved in positive regulation of synapse assembly and positive regulation of synaptic transmission. Predicted to act upstream of or within several processes, including chemical synaptic transmission; positive regulation of protein localization to synapse; and synapse assembly. Predicted to be located in postsynaptic density. Predi…
- **Diseases (Open Targets)**: autism spectrum disorder (0.333); neurodegenerative disease (0.288); Abdominal pain (0.139); familial focal epilepsy with variable foci (0.081); autosomal recessive primary microcephaly (0.076)
- **Europe PMC papers**: 352
- **Why important**: CLSTN3 connects CDH2 with SERPIND1 and is tissue-enhanced in brain, with associations to excitatory and inhibitory neurons and oligodendrocyte progenitors. Its annotations include calcium binding, synapse assembly, synaptic transmission, and homophilic cell adhesion. Disease links include autism spectrum disorder, neurodegenerative disease, epilepsy, and primary microcephaly, although its literature volume is smaller than that of the best-studied adhesion genes.
- **Conclusion**: Established evidence supports CLSTN3 as a synapse- and adhesion-related candidate. Its position provides a plausible bridge between the neural adhesion substructure and the extracellular SERPIND1 component, but that bridge remains a hypothesis because no supporting STRING or hu.MAP relationship was detected.

#### CDH2

- **Related proteins** (co-abundance neighbors): CLSTN3 (0.91); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cadherin 2. This gene encodes a classical cadherin and member of the cadherin superfamily. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein is proteolytically processed to generate a calcium-dependent cell adhesion molecule and glycoprotein. This protein plays a role in the establishment of left-right asymmetry, development of the nervous system and t…
- **Diseases (Open Targets)**: agenesis of corpus callosum, cardiac, ocular, and genital syndrome (0.809); arrhythmogenic right ventricular dysplasia, familial, 14 (0.583); Agenesis of corpus callosum (0.515); attention deficit-hyperactivity disorder 8 (0.505); aortic stenosis (0.481)
- **Europe PMC papers**: 35205
- **Why important**: CDH2 forms the module's connection with CLSTN3 and is a classical calcium-dependent cell-adhesion molecule. It is associated with nervous-system development, cell-cell junction assembly, synapse assembly, and tissue morphogenesis. HPA shows enrichment in heart muscle and enhancement across astrocytes, neurons, cardiomyocytes, and photoreceptor cells. It has very extensive literature and multiple developmental and cardiac disease associations.
- **Conclusion**: Established evidence supports CDH2 as a major cell-adhesion and junctional protein with neural and cardiac relevance. In this module it is best interpreted as evidence for a shared adhesion or cellular-composition signal, not as proof of a novel CDH2 complex.

#### TIMP1

- **Related proteins** (co-abundance neighbors): GPLD1 (0.92); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TIMP metallopeptidase inhibitor 1. This gene belongs to the TIMP gene family. The proteins encoded by this gene family are natural inhibitors of the matrix metalloproteinases (MMPs), a group of peptidases involved in degradation of the extracellular matrix. In addition to its inhibitory role against most of the known MMPs, the encoded protein is able to promote cell proliferation in a wide range of cell types, and may also have an …
- **Diseases (Open Targets)**: neoplasm (0.120); Sepsis (0.119); glioblastoma (0.119); colorectal carcinoma (0.119); neurodegenerative disease (0.117)
- **Europe PMC papers**: 25183
- **Why important**: TIMP1 is connected to GPLD1 and represents extracellular-matrix and protease regulation. It inhibits matrix metalloproteinases and can affect proliferation, apoptosis, cytokine responses, and signaling. HPA places it in vesicles and the Golgi, with associations across stromal and vascular-related cell types. It has extensive literature and disease links including sepsis, glioblastoma, colorectal carcinoma, and neurodegenerative disease.
- **Conclusion**: Established evidence supports TIMP1 as a secreted or vesicle-associated regulator of extracellular proteolysis and tissue remodeling. Its co-abundance with GPLD1 may reflect shared extracellular handling or tissue composition; a direct functional partnership is not established here.

## Module 14

**Tissue pair**: cell line and cerebrospinal_fluid  
**Genes (7)**: CFI, DSCAM, MDH1, NRXN3, PCDH1, SEMA6A, SGCE

### Function

No GO or KEGG term passed global multiple-testing correction, and there was no supplementary STRING functional enrichment. The descriptive gene annotations nevertheless converge on cell adhesion, homophilic cell-cell recognition, axon guidance, synaptic or neuronal signaling, and nervous-system development, especially through DSCAM, NRXN3, PCDH1, and SEMA6A. MDH1 contributes a cytosolic metabolic function, while CFI contributes complement regulation. Thus, the most defensible interpretation is a putative neurodevelopmental cell-contact and signaling module rather than a formally enriched pathway. The co-abundance pattern may reflect shared cellular composition or coordinated regulation, not proof that all proteins act in one biochemical complex.

**Cell composition.** The module is not predominantly a plasma or secreted-protein module: CFI is secreted to blood, whereas the other members are not annotated as secreted, with DSCAM annotated as intracellular and membrane associated. HPA indicates broad representation of tissue-enhanced or tissue-enriched genes, with brain-related enrichment recurring across several members and additional representation in retina, liver, pituitary gland, heart muscle, ovary, and adrenal gland. All members have cell-type-enhanced annotations, including neuronal, oligodendrocyte, epithelial, endocrine, and other cell types. Most genes are not detected in immune cells, although SGCE has blood-cell group enrichment and MDH1 has low immune-cell specificity. These observations argue against a simple blood-cell explanation, while leaving shared neuronal or other cell-type composition as a plausible contributor. HPA provides no matching protein-detection result for either study sample type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was detected among the module members, and no qualifying hu.MAP complex contained multiple module members. Therefore, the co-abundance edges are not supported here as established physical protein interactions or membership in a known multiprotein complex. The lack of STRING or hu.MAP support does not invalidate the module; it indicates that its structure is better treated as a data-derived co-abundance relationship whose molecular basis remains unresolved.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may represent a previously unreported co-abundance pattern shared by the cell-line and cerebrospinal-fluid datasets, because it has no matching high-confidence STRING network and no multi-member hu.MAP complex. However, those absences do not establish biological novelty. The genes and many of their individual functions are already well characterized, and the module could reflect shared cell composition, coordinated expression, indirect regulation, or technical covariance. A claim of a new biological mechanism would require replication, control for cellular composition, and independent validation of the co-abundance relationships.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of neuronal or neurodevelopmental cell-contact proteins, centered on DSCAM and connected through NRXN3, PCDH1, and SEMA6A, with CFI and MDH1 capturing extracellular complement regulation and cytosolic metabolic state. In cerebrospinal fluid and the cell-line context, this could arise from a shared neuronal or glial-associated program, release or representation of cell-associated proteins, or common regulatory state rather than a direct physical complex. This hypothesis predicts that the pattern should be stronger in samples with comparable neuronal or glial composition and should weaken after adjustment for cell-type abundance.

### Important genes

#### DSCAM

- **Related proteins** (co-abundance neighbors): NRXN3 (0.96), CFI (0.93), SGCE (0.91), PCDH1 (0.84); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DS cell adhesion molecule. This gene is a member of the immunoglobulin superfamily of cell adhesion molecules (Ig-CAMs), and is involved in human central and peripheral nervous system development. This gene is a candidate for Down syndrome and congenital heart disease (DSCHD). A gene encoding a similar Ig-CAM protein is located on chromosome 11. Alternatively spliced transcript variants encoding multiple isoforms have been …
- **Diseases (Open Targets)**: hereditary disease (0.510); alcohol drinking (0.346); arthropathy (0.336); head and neck cancer (0.333); spondylolisthesis (0.322)
- **Europe PMC papers**: 2789
- **Why important**: DSCAM is the central network connector, linked to NRXN3, CFI, SGCE, and PCDH1, and its annotations include cell adhesion, homophilic cell-cell adhesion, axon guidance, synapse assembly, and nervous-system development. HPA places it in brain-, pituitary-, and retina-associated contexts and in several neural or neuroglial cell types. Its substantial literature and disease relevance make it the strongest interpretive anchor.
- **Conclusion**: Established evidence supports DSCAM as a neural cell-adhesion and developmental gene and as the topological center of this module. It is not established that DSCAM physically interacts with the neighboring module proteins or drives their co-abundance; that role remains a hypothesis.

#### NRXN3

- **Related proteins** (co-abundance neighbors): DSCAM (0.96), MDH1 (0.95); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neurexin 3. This gene encodes a member of a family of proteins that function in the nervous system as receptors and cell adhesion molecules. Extensive alternative splicing and the use of alternative promoters results in multiple transcript variants and protein isoforms for this gene, but the full-length nature of many of these variants has not been determined. Transcripts that initiate from an upstream promot…
- **Diseases (Open Targets)**: obesity disorder (0.471); smoking initiation (0.429); Short stature (0.416); Relative macrocephaly (0.416); diabetes mellitus (0.383)
- **Europe PMC papers**: 2020
- **Why important**: NRXN3 connects directly to DSCAM and MDH1 and encodes a nervous-system receptor and cell-adhesion protein with extensive isoform diversity. Its annotations include neuron cell-cell adhesion, signal transduction, axon guidance, learning, and nervous-system development. HPA shows tissue enhancement in brain and retina and cell-type enhancement in neuronal and oligodendrocyte populations.
- **Conclusion**: Established evidence supports NRXN3 as a neuronal adhesion and signaling gene that fits the module's strongest functional theme. The connection to MDH1 is a co-abundance observation, not evidence of a direct molecular interaction or a shared complex.

#### PCDH1

- **Related proteins** (co-abundance neighbors): DSCAM (0.84), SEMA6A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm, Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protocadherin 1. This gene belongs to the protocadherin subfamily within the cadherin superfamily. The encoded protein is a membrane protein found at cell-cell boundaries. It is involved in neural cell adhesion, suggesting a possible role in neuronal development. The protein includes an extracelllular region, containing 7 cadherin-like domains, a transmembrane region and a C-terminal cytoplasmic region. Cells expr…
- **Diseases (Open Targets)**: Hypocalcemia (0.264); esophageal atresia/tracheoesophageal fistula (0.259); Tracheoesophageal fistula (0.259); asthma (0.223); nephrotic syndrome (0.210)
- **Europe PMC papers**: 966
- **Why important**: PCDH1 is connected to DSCAM and SEMA6A and encodes a protocadherin located at cell-cell boundaries, with cell adhesion, homophilic adhesion, cell-cell signaling, and nervous-system development annotations. Its network position bridges the central adhesion-related gene to a guidance-related gene, while HPA indicates cell-type enhancement in epithelial and salivary-duct contexts.
- **Conclusion**: Established evidence supports PCDH1 as a membrane cell-adhesion and signaling molecule compatible with the neural-contact interpretation, although its HPA profile also supports non-neural cellular sources. Its module role may therefore reflect cell composition as well as coordinated neural biology.

#### CFI

- **Related proteins** (co-abundance neighbors): DSCAM (0.93); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement factor I. This gene encodes a serine proteinase that is essential for regulating the complement cascade. The encoded preproprotein is cleaved to produce both heavy and light chains, which are linked by disulfide bonds to form a heterodimeric glycoprotein. This heterodimer can cleave and inactivate the complement components C4b and C3b, and it prevents the assembly of the C3 and C5 convertase enzymes. Defect…
- **Diseases (Open Targets)**: complement factor I deficiency (0.798); atypical hemolytic-uremic syndrome with I factor anomaly (0.795); age-related macular degeneration (0.782); atypical hemolytic-uremic syndrome (0.639); macular degeneration (0.571)
- **Europe PMC papers**: 14453
- **Why important**: CFI is directly connected to DSCAM and is the module's clearest extracellular and secreted component. It encodes a complement-regulating serine protease that inactivates complement components and is associated with complement deficiency and macular degeneration. HPA identifies liver enrichment and secretion to blood, while the module overall is represented in cerebrospinal fluid.
- **Conclusion**: Established evidence supports CFI as a secreted regulator of complement rather than a neuronal adhesion protein. Its co-abundance with DSCAM may indicate extracellular or tissue-composition coupling, but a direct DSCAM-CFI mechanism is not established.

#### MDH1

- **Related proteins** (co-abundance neighbors): NRXN3 (0.95); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Centrosome, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: malate dehydrogenase 1. This gene encodes an enzyme that catalyzes the NAD/NADH-dependent, reversible oxidation of malate to oxaloacetate in many metabolic pathways, including the citric acid cycle. Two main isozymes are known to exist in eukaryotic cells: one is found in the mitochondrial matrix and the other in the cytoplasm. This gene encodes the cytosolic isozyme, which plays a key role in the malate-aspartate shuttl…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 88 (0.499); prostate carcinoma (0.455); neurodegenerative disease (0.348); asthma (0.320); Abnormality of the skeletal system (0.295)
- **Europe PMC papers**: 3198
- **Why important**: MDH1 is connected to NRXN3 and encodes the cytosolic malate dehydrogenase involved in malate metabolism and the malate-aspartate shuttle. It is therefore the module member most directly linked to cellular redox and metabolic state. Its literature base is substantial, and its disease associations include developmental neurological and neurodegenerative contexts.
- **Conclusion**: Established evidence supports MDH1 as a metabolic enzyme, not as a cell-adhesion protein. Its presence may indicate metabolic state or cellular composition accompanying the neural-associated genes; any functional coupling to NRXN3 remains hypothetical.

#### SEMA6A

- **Related proteins** (co-abundance neighbors): PCDH1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: semaphorin 6A. The transmembrane semaphorin SEMA6A is expressed in developing neural tissue and is required for proper development of the thalamocortical projection (Leighton et al., 2001 [PubMed 11242070]).[supplied by OMIM, Feb 2011]
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); bipolar disorder (0.323); abscess (0.311); cellulitis (0.310); stomach disorder (0.293)
- **Europe PMC papers**: 1601
- **Why important**: SEMA6A is linked to PCDH1 and is a transmembrane semaphorin involved in nervous-system development and thalamocortical projection, with annotations for axon guidance, cytoskeletal organization, receptor signaling, and organ morphogenesis. HPA includes brain enrichment and several specialized cell types, and its literature supports an established developmental guidance role.
- **Conclusion**: Established evidence supports SEMA6A as a neural guidance and cell-surface signaling molecule that reinforces the module's neurodevelopmental interpretation. The observed edge with PCDH1 does not demonstrate direct binding or a shared complex.

## Module 15

**Tissue pair**: cell line and cerebrospinal_fluid  
**Genes (12)**: CNTN1, EXTL3, FAT3, FGFR1, ICOSLG, DGCR2, LRIG1, PLBD2, PLOD2, PTPRG, TNC, TYRO3

### Function

The module is most consistent with a cell-surface adhesion and receptor-signaling program linked to neural development, extracellular-matrix organization, and tissue-interface biology. TYRO3 is the central network connector, linking receptor-related, glycosaminoglycan-related, membrane, and adhesion genes. FAT3 connects adhesion and extracellular-matrix biology with PTPRG and FGFR1, while LRIG1 links EXTL3 with ICOSLG. The individual annotations support roles in neuronal migration, axon guidance, cell adhesion, receptor signaling, growth-factor signaling, collagen organization, and immune-cell communication. However, no GO or KEGG term passed global correction, so this functional interpretation is based on the gene annotations and network structure rather than statistically significant enrichment.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins. TNC is explicitly secreted to the extracellular matrix, whereas PLOD2, PLBD2, and CNTN1 are annotated as intracellular and/or membrane-associated; the remaining proteins are mainly membrane or intracellular signaling proteins. HPA evidence points most strongly toward brain and blood-vessel biology, with additional pancreas, adrenal, and smooth-muscle associations. The single-cell pattern is dominated by astrocytes, Bergmann glia, neurons, and other tissue-associated cell types, with some pancreatic and immune-cell signals. Most genes have low immune-cell specificity or are not detected in immune cells, although EXTL3, ICOSLG, and CNTN1 have selected immune-cell associations. Thus, the shared module is more compatible with conserved neural, vascular, glial, or tissue-interface biology than with a blood-cell-dominated signal. Because HPA reports no protein detection result for either sampled material, the tissue and cell-type interpretation remains inferential.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no supplementary STRING enrichment. This means the observed co-abundance structure is not supported by established STRING protein associations and should not be interpreted as a known physical interaction network. hu.MAP provides the only complex-level support: PTPRG and CNTN1 occur together in huMAP complex (hu.MAP huMAP3_12658.1), which contains many additional proteins outside the module. This supports a possible shared complex or related membrane-associated context for those genes, but it does not establish that all module members form one complex. The network therefore appears to combine a small amount of known complex context with predominantly unconfirmed co-abundance relationships.

**STRING interactions (score >= 0.7)**: 0 of 66 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12658.1 (PTPRG, CNTN1; 2/32)

### Novelty

The module may represent a novel cross-tissue co-abundance pattern, because its member set has no high-confidence STRING interactions and only a limited hu.MAP overlap. Nevertheless, absence from STRING or hu.MAP does not prove biological novelty: co-abundance can reflect shared cell states, coordinated regulation, extracellular exposure, or tissue composition without a documented physical interaction. The most defensible conclusion is that the specific conserved module organization is not directly established by the supplied interaction resources, while several component functions and some pairwise biological relationships are already well known.

**Hypothesis.** Hypothesis: the module captures a conserved tissue-interface program in which neural or glial adhesion proteins and extracellular-matrix components are coordinated with receptor tyrosine-kinase and phosphatase signaling. TYRO3 may organize or report this state through its connections to CNTN1, PLOD2, PLBD2, EXTL3, DGCR2, and FGFR1, while FAT3, PTPRG, and TNC may reflect adhesion and matrix remodeling. LRIG1 and ICOSLG could connect the program to local growth-factor regulation and conditional immune communication. In cerebrospinal fluid, the signal could arise from proteins released or sampled from neural, glial, vascular, or barrier-associated compartments rather than from a single intracellular pathway. This hypothesis requires validation with independent cohorts, cell-resolved measurements, protein-level assays, and perturbation experiments.

### Important genes

#### TYRO3

- **Related proteins** (co-abundance neighbors): EXTL3 (0.98), DGCR2 (0.93), PLOD2 (0.86), PLBD2 (0.82), CNTN1 (0.81), FGFR1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TYRO3 protein tyrosine kinase. The gene is part of a 3-member transmembrane receptor kinase receptor family with a processed pseudogene distal on chromosome 15. The encoded protein is activated by the products of the growth arrest-specific gene 6 and protein S genes and is involved in controlling cell survival and proliferation, spermatogenesis, immunoregulation and phagocytosis. The encoded protein has also been identified as …
- **Diseases (Open Targets)**: dengue disease (0.504); neurodegenerative disease (0.464); metabolic syndrome (0.332); chronic obstructive pulmonary disease (0.331); intelligence (0.326)
- **Europe PMC papers**: 4124
- **Why important**: TYRO3 is the network hub and connects the largest portion of the module's receptor, adhesion, glycosaminoglycan, and membrane-associated structure. Its established functions include receptor tyrosine-kinase signaling, cell adhesion, phagocytosis, nervous-system development, immunoregulation, and cell survival. HPA associates it with brain tissue, and the gene has substantial disease and literature coverage, making it a strong anchor for interpreting the module.
- **Conclusion**: Established evidence supports TYRO3 as a signaling receptor involved in neural, adhesion, survival, and immune-related biology, and the network identifies it as the principal organizational node. It is plausible, but not demonstrated, that TYRO3 coordinates the conserved module state.

#### FAT3

- **Related proteins** (co-abundance neighbors): PTPRG (0.86), TNC (0.82), FGFR1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FAT atypical cadherin 3. Predicted to enable calcium ion binding activity. Predicted to be involved in cell-cell adhesion. Predicted to act upstream of or within several processes, including negative regulation of dendrite development; neuron migration; and retina layer formation. Predicted to be located in dendrite and plasma membrane. Predicted to be integral component of membrane. [provided by Alliance of Genome Resour…
- **Diseases (Open Targets)**: retinal detachment (0.450); mathematical ability (0.438); gestational diabetes (0.428); atrial fibrillation (0.421); retinal disorder (0.405)
- **Europe PMC papers**: 1546
- **Why important**: FAT3 is a membrane cadherin-family adhesion protein with a network position connecting TNC, PTPRG, and FGFR1. Its HPA profile is enriched in brain and blood vessel and enhanced across several neural and glial cell types. Its established annotations include cell-cell adhesion, neuron migration, dendrite development, and morphogenesis, placing it at the interface between neural structure and tissue organization.
- **Conclusion**: Established evidence supports FAT3 as a neural and vascular adhesion regulator. Its position suggests that the module may encode coordinated cell-contact and matrix signaling, but the specific relationships inferred from co-abundance remain hypotheses.

#### FGFR1

- **Related proteins** (co-abundance neighbors): FAT3 (0.82), TYRO3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules, Cytokinetic bridge, Mitotic spindle; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibroblast growth factor receptor 1. The protein encoded by this gene is a member of the fibroblast growth factor receptor (FGFR) family, where amino acid sequence is highly conserved between members and throughout evolution. FGFR family members differ from one another in their ligand affinities and tissue distribution. A full-length representative protein consists of an extracellular region, composed of three immunoglobulin-like dom…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 2 with or without anosmia (0.849); Hartsfield-Bixler-Demyer syndrome (0.827); Pfeiffer syndrome (0.788); osteoglophonic dysplasia (0.773); hypogonadotropic hypogonadism (0.767)
- **Europe PMC papers**: 27461
- **Why important**: FGFR1 is a well-characterized receptor tyrosine kinase and a network bridge between FAT3 and TYRO3. Its established functions include MAPK signaling, protein phosphorylation, skeletal development, neuron migration, epithelial-to-mesenchymal transition, and regulation of cell proliferation. It has very extensive literature and strong disease-association coverage, giving the module a biologically interpretable growth-factor signaling axis.
- **Conclusion**: Established evidence supports FGFR1 as a major developmental and signaling regulator. Its inclusion supports a receptor-signaling interpretation, but the module does not establish that FGFR1 directly interacts with the other members.

#### TNC

- **Related proteins** (co-abundance neighbors): FAT3 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tenascin C. This gene encodes an extracellular matrix protein with a spatially and temporally restricted tissue distribution. This protein is homohexameric with disulfide-linked subunits, and contains multiple EGF-like and fibronectin type-III domains. It is implicated in guidance of migrating neurons as well as axons during development, synaptic plasticity, and neuronal regeneration. [provided by RefSeq, Jul…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss (0.619); deafness (0.552); osteoarthritis, hip (0.551); total hip arthroplasty (0.468); Varicose veins (0.460)
- **Europe PMC papers**: 12274
- **Why important**: TNC is the clearest extracellular-matrix component in the module and is explicitly secreted to the extracellular matrix. It connects to FAT3 and is associated with blood vessels, smooth muscle, astrocytes, and several stromal cell types. Its established functions include cell adhesion, neuronal and axonal guidance, synaptic plasticity, regeneration, morphogenesis, and response to wounding. It also has extensive literature coverage.
- **Conclusion**: Established evidence supports TNC as an extracellular scaffold and remodeling signal relevant to neural and vascular interfaces. Its co-abundance with FAT3 is compatible with coordinated adhesion and matrix biology, but a direct module mechanism is not proven.

#### CNTN1

- **Related proteins** (co-abundance neighbors): TYRO3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12658.1
- **Function (MyGene.info)**: contactin 1. The protein encoded by this gene is a member of the immunoglobulin superfamily. It is a glycosylphosphatidylinositol (GPI)-anchored neuronal membrane protein that functions as a cell adhesion molecule. It may play a role in the formation of axon connections in the developing nervous system. Multiple alternatively spliced transcript variants encoding different isoforms have been found for this gene…
- **Diseases (Open Targets)**: Compton-North congenital myopathy (0.709); Parkinson disease (0.393); urinary system disorder (0.307); exostosis (0.266); escherichia coli infection (0.263)
- **Europe PMC papers**: 1740
- **Why important**: CNTN1 is a GPI-anchored neuronal adhesion molecule associated with brain tissue, astrocytes, Bergmann glia, and excitatory and inhibitory neurons. It has established roles in axon guidance, brain development, central nervous-system myelination, and cell adhesion. It is also one of the two module members represented in huMAP complex (hu.MAP huMAP3_12658.1), providing the clearest complex-level connection within the module.
- **Conclusion**: Established evidence supports CNTN1 as a neural adhesion and developmental protein, with additional support from complex (hu.MAP huMAP3_12658.1). Its co-abundance with TYRO3 may reflect a shared neural-interface state, but the supplied resources do not establish a direct physical interaction.
