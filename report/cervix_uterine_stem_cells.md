# Conserved co-abundance modules: cervix_uterine and stem_cells

## Module 0

**Tissue pair**: cervix_uterine and stem_cells  
**Genes (5)**: YWHAH, CS, TUFM, IGFBP2, LMNB1

### Function

The module does not have a globally significant GO or KEGG enrichment term, and it has no supplementary STRING enrichment term. Its strongest structural feature is IGFBP2 as the central co-abundance hub, connected to CS, TUFM, LMNB1, and YWHAH, while the peripheral genes represent distinct cellular compartments: mitochondrial metabolism and translation, the nuclear lamina, cytosolic phosphoserine-dependent signaling, and extracellular IGF binding. Therefore, the evidence supports a coordinated abundance state rather than a single established biochemical pathway. A cautious interpretation is that the module may report a shared cellular state involving growth-factor signaling together with mitochondrial, nuclear, and signaling machinery. This interpretation remains provisional because the module is small and its co-abundance edges are not physical interactions.

**Cell composition.** The module is not dominated by secreted or plasma proteins: IGFBP2 is the sole secreted-to-blood component, whereas the other genes are intracellular. It is also not strongly blood-cell enriched according to HPA: the genes have low immune-cell specificity or are not detected in immune cells, and no enriched blood-cell category was reported. Nevertheless, HPA assigns some genes to megakaryocyte, platelet, erythrocyte-progenitor, or related cell patterns, so sample composition or shared cellular states cannot be excluded. Tissue patterns are heterogeneous, including blood vessel, brain, skeletal muscle, tongue, pancreas, bone marrow, and lymphoid tissue. Protein detection is reported for most genes in cervix_uterine, while no matching HPA tissue is available for stem_cells. The mixed tissue and cell-type profile argues against a simple universal housekeeping module, although CS and TUFM have broadly compatible metabolic or mitochondrial roles.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module gene pair reaches the specified STRING interaction threshold, and no STRING functional enrichment is reported. No hu.MAP complex contains multiple module members. Thus, the observed co-abundance relationships are not supported here by known high-confidence protein-protein interactions or by a shared hu.MAP complex. The absence of these relationships does not invalidate the co-abundance module; it indicates that the network may capture coordinated regulation, cell-state variation, or tissue-composition effects rather than a stable physical complex. IGFBP2 is annotated as having extracellular and intracellular ligand interactions, but those annotations do not establish interactions with the other module members.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel cross-tissue co-abundance pattern, because the module links IGFBP2 with CS, TUFM, LMNB1, and YWHAH without corresponding high-confidence STRING links or a shared hu.MAP complex. However, it should not be called a newly discovered biological pathway on this evidence alone. The lack of database support can reflect incomplete interaction coverage, context dependence, or a correlation driven by abundance or sample composition. The strongest defensible claim is that the coordinated abundance pattern is a potentially new observation that requires replication in independent cervix_uterine and stem-cell datasets, control for cell composition, and experimental testing.

**Hypothesis.** Hypothesis: the module reflects a shared proliferative or differentiation-related cellular state in which IGFBP2-associated growth-factor regulation covaries with mitochondrial energy and translation capacity, nuclear-envelope organization, and phosphoserine-dependent signaling. IGFBP2 may act as the abundance-level bridge because it is the network hub and can function as a secreted or intracellular IGF-binding protein. The HPA patterns also raise an alternative hypothesis that part of the signal arises from shared vascular, stromal, progenitor, or platelet-associated cellular contributions. These are hypotheses, not established mechanisms from the enrichment or interaction evidence.

### Important genes

#### IGFBP2

- **Related proteins** (co-abundance neighbors): CS (0.90), TUFM (0.88), LMNB1 (0.84), YWHAH (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor binding protein 2. The protein encoded by this gene is one of six similar proteins that bind insulin-like growth factors I and II (IGF-I and IGF-II). The encoded protein can be secreted into the bloodstream, where it binds IGF-I and IGF-II with high affinity, or it can remain intracellular, interacting with many different ligands. High expression levels of this protein promote the growth of several types of tumors a…
- **Diseases (Open Targets)**: neurodegenerative disease (0.313); intelligence (0.303); pregnancy disorder (0.290); open-angle glaucoma (0.258); carcinoma of esophagus (0.254)
- **Europe PMC papers**: 6255
- **Why important**: IGFBP2 is the module hub, connecting every other member in the co-abundance graph. It binds IGF-I and IGF-II, can be secreted into blood or remain intracellular, and is associated in the fact sheet with growth, pregnancy, nutrient and mechanical responses, and several disease areas. Its broad literature volume is the highest among the module members. Its tissue-enhanced vascular and pancreatic pattern and secreted status make it especially important for distinguishing a biological signaling module from a sample-composition effect.
- **Conclusion**: Established evidence: IGFBP2 is the central co-abundance node and an IGF-binding protein with both extracellular and intracellular descriptions. Hypothesis: it may organize or mark the shared growth-factor and cellular-state signal. The co-abundance data do not demonstrate that IGFBP2 regulates the other genes.

#### CS

- **Related proteins** (co-abundance neighbors): IGFBP2 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS is the canonical citrate synthase enzyme of the mitochondrial Krebs cycle and is described as present in cells capable of oxidative metabolism. It is the most extensively represented gene in the literature among the module members and is tissue enhanced in skeletal muscle and tongue. Its direct edge to IGFBP2 places mitochondrial oxidative metabolism at the edge of the module rather than in a documented mitochondrial complex with the other genes.
- **Conclusion**: Established evidence: CS marks mitochondrial oxidative metabolism and is co-abundant with IGFBP2 in this module. Hypothesis: its covariation may indicate changing energetic demand during a shared cellular state. The data do not establish a direct metabolic interaction between CS and IGFBP2.

#### TUFM

- **Related proteins** (co-abundance neighbors): IGFBP2 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Tu translation elongation factor, mitochondrial. This gene encodes a protein which participates in protein translation in mitochondria. Mutations in this gene have been associated with combined oxidative phosphorylation deficiency resulting in lactic acidosis and fatal encephalopathy. A pseudogene has been identified on chromosome 17. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 4 (0.769); neurodegenerative disease (0.502); COVID-19 (0.471); combined oxidative phosphorylation deficiency (0.370); ulcerative colitis (0.303)
- **Europe PMC papers**: 1391
- **Why important**: TUFM supports mitochondrial translation and mitochondrial large-ribosomal-subunit assembly. It has disease associations involving combined oxidative-phosphorylation deficiency and neurological disease, and its HPA single-cell pattern includes esophageal basal cells and late spermatids. Its connection to IGFBP2 places mitochondrial protein synthesis alongside the module’s signaling and structural components.
- **Conclusion**: Established evidence: TUFM is a mitochondrial translation factor and is co-abundant with IGFBP2. Hypothesis: coordinated TUFM and IGFBP2 abundance could reflect a state requiring both mitochondrial protein production and growth-related signaling. No physical interaction or pathway enrichment supports this mechanism in the supplied evidence.

#### LMNB1

- **Related proteins** (co-abundance neighbors): IGFBP2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lamin B1. This gene encodes one of the two B-type lamin proteins and is a component of the nuclear lamina. A duplication of this gene is associated with autosomal dominant adult-onset leukodystrophy (ADLD). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: microcephaly 26, primary, autosomal dominant (0.723); autosomal dominant primary microcephaly (0.675); adult-onset autosomal dominant demyelinating leukodystrophy (0.670); hereditary disease (0.488); Syndrome with microcephaly as major feature (0.487)
- **Europe PMC papers**: 3851
- **Why important**: LMNB1 is a nuclear-lamina component involved in nuclear-envelope organization, nuclear migration, heterochromatin formation, and nuclear-envelope localization. It has disease associations with adult-onset demyelinating leukodystrophy and primary microcephaly. Its HPA pattern includes bone marrow and lymphoid tissue and several progenitor or spermatid populations, making it relevant to possible differentiation or cell-state variation.
- **Conclusion**: Established evidence: LMNB1 represents nuclear architecture and is co-abundant with the IGFBP2 hub. Hypothesis: its covariation may indicate coordinated changes in nuclear organization during differentiation or proliferation. The module does not show that LMNB1 directly mediates IGFBP2 signaling.

#### YWHAH

- **Related proteins** (co-abundance neighbors): IGFBP2 (0.83); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein eta. This gene product belongs to the 14-3-3 family of proteins which mediate signal transduction by binding to phosphoserine-containing proteins. This highly conserved protein family is found in both plants and mammals, and this protein is 99% identical to the mouse, rat and bovine orthologs. This gene contains a 7 bp repeat sequence in its 5' UTR, and changes in the number of this repeat have been as…
- **Diseases (Open Targets)**: COVID-19 (0.371); severe acute respiratory syndrome (0.370); placenta praevia (0.247); chronic hepatitis C virus infection (0.180); response to xenobiotic stimulus (0.080)
- **Europe PMC papers**: 1273
- **Why important**: YWHAH is a conserved fourteen-three-three family signaling adaptor that binds phosphoserine-containing proteins and participates in signal transduction and intracellular protein localization. It has a group-enriched HPA pattern involving blood vessel and brain and a single-cell pattern involving megakaryocytes and platelets. Its position as an IGFBP2-connected peripheral node provides a plausible signaling component distinct from the mitochondrial and nuclear proteins.
- **Conclusion**: Established evidence: YWHAH is a cytosolic phosphoserine-binding signaling adaptor and is co-abundant with IGFBP2. Hypothesis: it may reflect downstream signaling-state variation associated with the module. The supplied data do not identify its binding partners in this module or prove a pathway connecting it to IGFBP2.

## Module 1

**Tissue pair**: cervix_uterine and stem_cells  
**Genes (26)**: SFN, ANXA1, CAT, CD109, CARHSP1, CNN3, COL6A1, CORO1A, CRYAB, FN1, GMPPB, GSTP1, H1-3, H1-5, H2AC21, H4C1, IDH2, KRT19, LGALS1, HSPG2, PSME3IP1, RAB5C, RAN, RPL9, SERPINB9, TIMP1

### Function

The strongest interpretation is a structural and extracellular-matrix module with a parallel chromatin and cellular-stress component. The globally corrected evidence supports structural molecule activity (GO:MF structural molecule activity; q_global = 0.00578), basement membrane (GO:CC basement membrane; q_global = 0.0311), structural constituent of chromatin (GO:MF structural constituent of chromatin; q_global = 0.0311), and extracellular space, exosome, extracellular organelle, extracellular membrane-bounded organelle, and extracellular vesicle annotations (5 globally significant GO/KEGG terms, q_global 0.0323–0.0426; see the table). The matrix arm is represented by FN1, COL6A1, HSPG2, TIMP1, LGALS1, and related genes; the chromatin arm is represented by H1-3, H1-5, H2AC21, and H4C1. The module therefore appears to capture coordinated abundance of extracellular scaffold and remodeling proteins together with epithelial, stromal, and proliferative or chromatin-associated signals. The vesicle annotations should be interpreted as localization or annotation overlap, not as proof that the entire module is an exosome biogenesis program. The STRING collagen-containing extracellular-matrix and structural-molecule results (STRING Component Collagen-containing extracellular matrix; within-query FDR = 0.0028) and (STRING Function Structural molecule activity; within-query FDR = 0.0058) support this interpretation but are supplementary rather than globally corrected evidence.

**Cell composition.** This is not a uniformly secreted or plasma-protein module. The HPA summary identifies a substantial secreted component, including FN1, TIMP1, COL6A1, HSPG2, LGALS1, and ANXA1, but also intracellular, membrane, cytoskeletal, mitochondrial, ribosomal, and nuclear histone proteins. HPA tissue patterns are mixed, with recurring signals in esophagus, bone marrow, lymphoid tissue, skeletal muscle, and blood vessel, while single-cell patterns include epithelial, trophoblast, stromal, progenitor, plasma-cell, and myeloid-associated populations. Most genes have low immune-cell specificity or are not detected in immune cells, although a smaller subset has immune-cell enrichment or enhancement. The module is detected at the protein level in cervix_uterine for many genes, whereas the supplied stem-cell tissue protein comparison has no matching HPA tissue. Thus, the shared module may reflect a conserved epithelial or stromal extracellular environment and cell-state program, with possible contribution from shared cell types or sample composition; it should not be labeled simply as a blood-contamination module.

**GO/KEGG enrichment**: 8 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF structural molecule activity | 0.00578 | COL6A1, CRYAB, FN1, H1-3, H1-5, H2AC21, H4C1, HSPG2, KRT19, RPL9 |
| GO:CC basement membrane | 0.0311 | COL6A1, FN1, HSPG2, TIMP1 |
| GO:MF structural constituent of chromatin | 0.0311 | H1-3, H1-5, H2AC21, H4C1 |
| GO:CC extracellular space | 0.0323 | ANXA1, CAT, CD109, COL6A1, CORO1A, CRYAB, FN1, GSTP1, H2AC21, H4C1, HSPG2, IDH2, KRT19, LGALS1, RAB5C, RAN, SERPINB9, SFN, TIMP1 |
| GO:CC extracellular exosome | 0.0415 | ANXA1, CAT, COL6A1, CORO1A, CRYAB, FN1, GSTP1, H2AC21, H4C1, HSPG2, IDH2, KRT19, LGALS1, RAB5C, RAN, SERPINB9, SFN, TIMP1 |
| GO:CC extracellular organelle | 0.0426 | ANXA1, CAT, COL6A1, CORO1A, CRYAB, FN1, GSTP1, H2AC21, H4C1, HSPG2, IDH2, KRT19, LGALS1, RAB5C, RAN, SERPINB9, SFN, TIMP1 |
| GO:CC extracellular membrane-bounded organelle | 0.0426 | ANXA1, CAT, COL6A1, CORO1A, CRYAB, FN1, GSTP1, H2AC21, H4C1, HSPG2, IDH2, KRT19, LGALS1, RAB5C, RAN, SERPINB9, SFN, TIMP1 |
| GO:CC extracellular vesicle | 0.0426 | ANXA1, CAT, COL6A1, CORO1A, CRYAB, FN1, GSTP1, H2AC21, H4C1, HSPG2, IDH2, KRT19, LGALS1, RAB5C, RAN, SERPINB9, SFN, TIMP1 |

### STRING and hu.MAP

STRING contains a coherent set of known extracellular relationships centered on FN1: FN1 connects with COL6A1, HSPG2, LGALS1, TIMP1, and ANXA1, and the module also contains the known histone relationships H1-3–H1-5, H1-5–H4C1, and H2AC21–H4C1. These links indicate that part of the co-abundance structure recapitulates established extracellular-matrix biology and a separate nucleosome or histone association. The STRING enrichment results for collagen-containing extracellular matrix, extracellular space, extracellular vesicles, structural molecule activity, nucleosome, and secreted proteins (11 supplementary STRING terms; within-query FDR 0.0028–0.0439) are supportive context, not global significance. The remaining module edges are not established by the supplied high-confidence STRING network, so co-abundance should not be treated as direct physical interaction. No hu.MAP complex contains multiple module members. The data therefore support a composite module with a known matrix interaction core and a known histone subnetwork, rather than one experimentally established multiprotein complex.

**STRING interactions (score >= 0.7)**: 8 of 325 gene pairs: ANXA1–FN1 (0.793); COL6A1–FN1 (0.78); FN1–HSPG2 (0.996); FN1–LGALS1 (0.878); FN1–TIMP1 (0.954); H1-3–H1-5 (0.911); H1-5–H4C1 (0.777); H2AC21–H4C1 (0.961)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Collagen-containing extracellular matrix (FDR = 0.0028, 7 genes); PMID (2020) DIPPER, a spatiotemporal proteomics atlas of human intervertebral discs for exploring ageing and degeneration dynamics. (FDR = 0.0034, 8 genes); Function Structural molecule activity (FDR = 0.0058, 10 genes); Component Extracellular space (FDR = 0.0062, 19 genes); Component Extracellular exosome (FDR = 0.0067, 18 genes); Component Nucleosome (FDR = 0.0126, 4 genes); Component Vesicle (FDR = 0.0255, 19 genes); Function Structural constituent of chromatin (FDR = 0.0384, 4 genes); Keyword Extracellular matrix (FDR = 0.0404, 4 genes); Keyword Secreted (FDR = 0.0404, 7 genes); Keyword Hydroxylation (FDR = 0.0439, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is not demonstrated to be a wholly new biological pathway. Several of its relationships and annotations are already well established, especially the FN1-centered matrix relationships and the histone associations in STRING. Its potentially novel aspect is the coordinated co-abundance of these extracellular, epithelial or stromal, stress-response, vesicle-associated, and chromatin signals across cervix_uterine and stem_cells, particularly because hu.MAP provides no shared complex. However, absence from hu.MAP or from the supplied STRING edge set cannot establish novelty: it may reflect incomplete interaction coverage, indirect regulation, tissue composition, or correlated secretion. The defensible conclusion is that this is a potentially informative cross-tissue co-abundance pattern built from largely familiar biology, not proof of a newly discovered molecular complex or pathway.

**Hypothesis.** Hypothesis: a conserved epithelial or stromal state in cervix_uterine and stem_cells coordinates extracellular scaffold production with matrix protection, vesicle-associated release, oxidative or proteotoxic stress handling, and altered chromatin state. FN1, COL6A1, and HSPG2 could organize a basement-membrane and pericellular scaffold, while TIMP1 could restrain matrix proteolysis and influence survival or proliferation. LGALS1 and ANXA1 could provide cell-matrix or inflammatory signaling, and the histone genes could mark a proliferative, progenitor-like, or chromatin-remodeling state. This is a mechanistic model rather than a demonstrated causal chain: the co-abundance graph and annotations do not establish secretion, directionality, cell-of-origin, or direct regulation between the arms.

### Important genes

#### FN1

- **Related proteins** (co-abundance neighbors): CD109 (0.96), COL6A1 (0.95), IDH2 (0.90); STRING partners: ANXA1 (0.793), COL6A1 (0.78), HSPG2 (0.996), LGALS1 (0.878), TIMP1 (0.954)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 is the clearest extracellular hub in the biological interpretation: it is linked in STRING to COL6A1, HSPG2, LGALS1, TIMP1, and ANXA1, and it appears across the matrix, basement-membrane, extracellular-space, vesicle, and structural-molecule evidence (GO:MF structural molecule activity; q_global = 0.00578), (GO:CC basement membrane; q_global = 0.0311), (5 globally significant GO/KEGG terms, q_global 0.0323–0.0426; see the table), (5 supplementary STRING terms; within-query FDR 0.0028–0.0067), and (4 supplementary STRING terms; within-query FDR 0.0255–0.0404). It is a secreted-to-blood matrix glycoprotein with established roles in adhesion, migration, wound healing, and cell-matrix signaling, and it has extensive disease and literature support.
- **Conclusion**: Established: FN1 is a central and biologically credible marker of the module's extracellular-matrix arm. Hypothesis: its coordinated abundance may organize the shared matrix state, but the data do not show that FN1 drives the other module genes.

#### COL6A1

- **Related proteins** (co-abundance neighbors): FN1 (0.95), CAT (0.93), LGALS1 (0.86); STRING partners: FN1 (0.78)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is a secreted extracellular-matrix collagen component with fibroblast and stromal-associated HPA patterns. It connects to FN1, CAT, and LGALS1 in the module and contributes to every matrix and extracellular annotation supported by (GO:MF structural molecule activity; q_global = 0.00578), (GO:CC basement membrane; q_global = 0.0311), and (5 globally significant GO/KEGG terms, q_global 0.0323–0.0426; see the table), as well as the STRING matrix evidence (STRING Component Collagen-containing extracellular matrix; within-query FDR = 0.0028), (STRING Function Structural molecule activity; within-query FDR = 0.0058) (STRING Component Extracellular space; within-query FDR = 0.0062) (STRING Component Extracellular exosome; within-query FDR = 0.0067), (STRING Component Vesicle; within-query FDR = 0.0255), and (STRING Keyword Extracellular matrix; within-query FDR = 0.0404) (STRING Keyword Secreted; within-query FDR = 0.0404) (STRING Keyword Hydroxylation; within-query FDR = 0.0439). Its established links to collagen-related muscular disease and tissue integrity make it a functionally informative structural gene rather than a generic abundance marker.
- **Conclusion**: Established: COL6A1 supports a genuine extracellular-scaffold interpretation. Hypothesis: it may help define the stromal or basement-membrane context shared by the tissues, but the module cannot identify which cell type produces it.

#### HSPG2

- **Related proteins** (co-abundance neighbors): CD109 (0.90), IDH2 (0.81); STRING partners: FN1 (0.996)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 encodes perlecan, a secreted extracellular proteoglycan that cross-links matrix and cell-surface components. It is connected to FN1 in STRING and is represented in basement membrane, extracellular space, structural-molecule, vesicle, and matrix annotations (GO:MF structural molecule activity; q_global = 0.00578), (GO:CC basement membrane; q_global = 0.0311), (5 globally significant GO/KEGG terms, q_global 0.0323–0.0426; see the table), (STRING Component Collagen-containing extracellular matrix; within-query FDR = 0.0028), (STRING Function Structural molecule activity; within-query FDR = 0.0058) (STRING Component Extracellular space; within-query FDR = 0.0062) (STRING Component Extracellular exosome; within-query FDR = 0.0067), (STRING Component Vesicle; within-query FDR = 0.0255), and (STRING Keyword Extracellular matrix; within-query FDR = 0.0404) (STRING Keyword Secreted; within-query FDR = 0.0404). Its blood-vessel and stromal-associated HPA patterns and disease associations involving tissue structure further support its importance.
- **Conclusion**: Established: HSPG2 is a strong marker of the module's basement-membrane and pericellular-scaffold arm. Hypothesis: it may modulate the local presentation of growth or inflammatory signals, but that regulatory role is not directly established by this module.

#### TIMP1

- **Related proteins** (co-abundance neighbors): CARHSP1 (0.96), GMPPB (0.87); STRING partners: FN1 (0.954)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TIMP metallopeptidase inhibitor 1. This gene belongs to the TIMP gene family. The proteins encoded by this gene family are natural inhibitors of the matrix metalloproteinases (MMPs), a group of peptidases involved in degradation of the extracellular matrix. In addition to its inhibitory role against most of the known MMPs, the encoded protein is able to promote cell proliferation in a wide range of cell types, and may also have an …
- **Diseases (Open Targets)**: neoplasm (0.120); Sepsis (0.119); glioblastoma (0.119); colorectal carcinoma (0.119); neurodegenerative disease (0.117)
- **Europe PMC papers**: 25183
- **Why important**: TIMP1 is a secreted matrix regulator connected to FN1 in STRING and appears in basement membrane, extracellular-space, vesicle, and collagen-matrix evidence (GO:CC basement membrane; q_global = 0.0311), (5 globally significant GO/KEGG terms, q_global 0.0323–0.0426; see the table), (STRING Component Collagen-containing extracellular matrix; within-query FDR = 0.0028), (STRING PMID (2020) DIPPER, a spatiotemporal proteomics atlas of human intervertebral discs for exploring ageing and degeneration dynamics.; within-query FDR = 0.0034), (STRING Component Extracellular space; within-query FDR = 0.0062), (STRING Component Extracellular exosome; within-query FDR = 0.0067), (STRING Component Vesicle; within-query FDR = 0.0255), and (STRING Keyword Secreted; within-query FDR = 0.0404). Its established inhibition of matrix metalloproteinases, together with effects on proliferation, survival, cytokine response, and apoptosis, gives it a plausible bridge between matrix structure and cell state. It also has substantial disease and literature support.
- **Conclusion**: Established: TIMP1 can couple matrix protection to survival and signaling. Hypothesis: it may stabilize the matrix-rich state represented by the module, but causality and the relevant protease targets are not resolved.

#### H1-3

- **Related proteins** (co-abundance neighbors): SFN (0.88), H1-5 (0.86), RAB5C (0.85), H4C1; H4C2; H4C3; H4C4; H4C5; H4C6; H4C8; H4C9; H4C11; H4C12; H4C13; H4C14; H4C15; H4C16 (0.84), CARHSP1 (0.84), GSTP1 (0.80); STRING partners: H1-5 (0.911)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: H1.3 linker histone, cluster member. Histones are basic nuclear proteins responsible for nucleosome structure of the chromosomal fiber in eukaryotes. Two molecules of each of the four core histones (H2A, H2B, H3, and H4) form an octamer, around which approximately 146 bp of DNA is wrapped in repeating units, called nucleosomes. The linker histone, H1, interacts with linker DNA between nucleosomes and functions in the compaction of ch…
- **Diseases (Open Targets)**: breast carcinoma (0.080); actinic keratosis (0.066); sebaceous of Jadassohn nevus (0.057); squamous cell carcinoma (0.045); non-small cell lung carcinoma (0.036)
- **Europe PMC papers**: 118293
- **Why important**: H1-3 has the strongest module connectivity in the supplied network and links the histone-associated portion to SFN, RAB5C, CARHSP1, and GSTP1. It is present in structural-molecule and chromatin terms (GO:MF structural molecule activity; q_global = 0.00578) and (GO:MF structural constituent of chromatin; q_global = 0.0311), and in the STRING structural-molecule, nucleosome, chromatin, and hydroxylation results (STRING Function Structural molecule activity; within-query FDR = 0.0058), (STRING Component Nucleosome; within-query FDR = 0.0126), (STRING Function Structural constituent of chromatin; within-query FDR = 0.0384), and (STRING Keyword Hydroxylation; within-query FDR = 0.0439). HPA associates it with bone marrow and hematopoietic progenitor states, while its linker-histone function and extensive literature support make it informative for a chromatin or progenitor-state interpretation.
- **Conclusion**: Established: H1-3 identifies a genuine chromatin-related component that is distinct from the extracellular-matrix arm. Hypothesis: its co-abundance may indicate proliferation or progenitor-state composition, but it does not prove chromatin remodeling caused the extracellular program.

## Module 2

**Tissue pair**: cervix_uterine and stem_cells  
**Genes (11)**: APOC1, APOE, BLVRA, CAPZB, ERMP1, H1-10, HSPA4L, SQOR, SUCLG2, TXN, UTS2

### Function

No GO or KEGG term passed global correction, and STRING returned no supplementary enrichment term. The most defensible interpretation is therefore a composite co-abundance program rather than a demonstrated single pathway. APOC1 is the central network hub and is linked to genes spanning lipid and lipoprotein biology, mitochondrial metabolism, redox control, protein stress, chromatin, and cytoskeletal regulation. The strongest coherent functional signal is lipid transport and lipoprotein metabolism through APOC1 and APOE, with a secondary mitochondrial metabolic and detoxification component represented by SUCLG2, SQOR, and BLVRA. TXN and ERMP1 provide plausible redox and endoplasmic-reticulum stress context. These functions are inferred from gene annotations and network structure, not from significant module-level enrichment.

**Cell composition.** The module is heterogeneous rather than a uniform tissue program. It contains secreted-to-blood proteins, especially APOC1, APOE, and UTS2, and HPA profiles prominently include liver-associated genes and hepatocytes. This raises the possibility that part of the shared cervix and stem-cell co-abundance signal reflects circulating proteins, tissue admixture, or shared stromal or other non-target cell populations rather than a cell-intrinsic program. The module is not predominantly blood-cell specific: most genes have low immune-cell specificity, although selected genes show myeloid, NK-cell, eosinophil, or T-reg associations. Several genes are tissue enhanced in esophageal, liver, adrenal, brain, bone-marrow, intestinal, or reproductive-cell contexts, indicating broad biological heterogeneity. Cervical protein detection is present for several intracellular or mitochondrial proteins, whereas the HPA summary provides no matching stem-cell tissue protein evidence. The module is therefore not best described as a simple housekeeping module, although TXN, BLVRA, and CAPZB have relatively broad tissue profiles.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The known STRING evidence is concentrated in the APOC1–APOE relationship, which has very high confidence and supports a biologically meaningful lipoprotein-associated submodule. The network also contains the co-abundance connection between SUCLG2 and SQOR, consistent with a mitochondrial metabolic branch, but this relationship is not represented as a reported STRING interaction in the fact sheet. The remaining module edges connect APOC1 to diverse proteins without corresponding high-confidence STRING partners. No hu.MAP complex contains multiple module members. Thus, the module is not a recovered canonical multiprotein complex; it is mainly a co-abundance structure centered on APOC1, with one externally supported apolipoprotein interaction and a separate mitochondrial pair.

**STRING interactions (score >= 0.7)**: 1 of 55 gene pairs: APOC1–APOE (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The underlying biology is not wholly new because APOC1 and APOE are established lipid-associated proteins with a known high-confidence STRING relationship, and the individual functions of the other genes are already annotated. However, the particular conserved co-abundance module across cervix_uterine and stem_cells may represent a new dataset-level observation, especially because no hu.MAP multi-member complex and no STRING enrichment program explain the full module. This should be described as a potentially novel cross-tissue co-abundance pattern rather than a newly discovered molecular pathway. Its novelty remains provisional because the pattern could arise from circulating apolipoproteins, shared cell populations, tissue admixture, or coordinated stress and metabolic state. Replication with cell-resolved measurements, matched protein data, and adjustment for composition would be needed before claiming a new biological mechanism.

**Hypothesis.** Hypothesis: the conserved module reflects a mixed extracellular-lipid and intracellular metabolic state rather than one physical complex. A liver-like or lipid-handling signal, potentially contributed by circulating APOC1 and APOE, may covary with mitochondrial succinate and sulfide metabolism through SUCLG2 and SQOR, while TXN, BLVRA, and ERMP1 report redox, detoxification, and protein-stress conditions. APOC1 may act as the abundance-linked organizing feature because it is the network hub, but the inferred connections outside the APOC1–APOE pair should be treated as statistical co-abundance hypotheses rather than direct molecular interactions.

### Important genes

#### APOC1

- **Related proteins** (co-abundance neighbors): SUCLG2 (1.00), HSPA4L (0.95), UTS2 (0.93), ERMP1 (0.92), H1-10 (0.91), TXN (0.90), BLVRA (0.87), APOE (0.87), CAPZB (0.84); STRING partners: APOE (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein C1. This gene encodes a member of the apolipoprotein C1 family. This gene is expressed primarily in the liver, and it is activated when monocytes differentiate into macrophages. The encoded protein plays a central role in high density lipoprotein (HDL) and very low density lipoprotein (VLDL) metabolism. This protein has also been shown to inhibit cholesteryl ester transfer protein in plasma. A pseudog…
- **Diseases (Open Targets)**: Alzheimer disease (0.574); dementia (0.523); metabolic syndrome (0.464); Hypercholesterolemia (0.461); familial hyperlipidemia (0.461)
- **Europe PMC papers**: 4121
- **Why important**: APOC1 is the central network hub, connects to most of the module, is liver enriched and hepatocyte enriched, is secreted to blood, and has annotations in HDL and VLDL metabolism, triglyceride handling, and cholesterol transport. It also has substantial literature and disease links involving lipid disorders, metabolic syndrome, and neurodegenerative disease. Its central position makes it the best candidate for explaining why otherwise diverse genes co-abundance with the module.
- **Conclusion**: Established evidence supports APOC1 as the principal lipid-associated marker and network organizer of the module. It is plausible, but not established, that APOC1-related circulating lipoprotein biology drives the conserved cross-tissue signal.

#### APOE

- **Related proteins** (co-abundance neighbors): APOC1 (0.87); STRING partners: APOC1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein E. The protein encoded by this gene is a major apoprotein of the chylomicron. It binds to a specific liver and peripheral cell receptor, and is essential for the normal catabolism of triglyceride-rich lipoprotein constituents. This gene maps to chromosome 19 in a cluster with the related apolipoprotein C1 and C2 genes. Mutations in this gene result in familial dysbetalipoproteinemia, or type III hype…
- **Diseases (Open Targets)**: hyperlipoproteinemia type 3 (0.803); coronary artery disorder (0.782); lipoprotein glomerulopathy (0.759); Alzheimer disease (0.696); familial hypercholesterolemia (0.651)
- **Europe PMC papers**: 74272
- **Why important**: APOE is the only partner of APOC1 supported by a very high-confidence STRING interaction in this module. It is tissue enhanced in liver, adrenal gland, and brain, is enriched in hepatocytes and macrophages, is secreted to blood, and functions in lipid transport, triglyceride-rich lipoprotein clearance, receptor-mediated endocytosis, and retinoid metabolism. It has an extensive literature and strong disease associations involving dyslipidemia, coronary disease, and Alzheimer disease.
- **Conclusion**: Established evidence identifies APOE as a biologically credible partner of APOC1 and reinforces a lipoprotein-related interpretation. The data do not establish that APOE mediates the other module edges or that the module is a single APOE-containing complex.

#### TXN

- **Related proteins** (co-abundance neighbors): APOC1 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin. The protein encoded by this gene acts as a homodimer and is involved in many redox reactions. The encoded protein is active in the reversible S-nitrosylation of cysteines in certain proteins, which is part of the response to intracellular nitric oxide. This protein is found in the cytoplasm. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct…
- **Diseases (Open Targets)**: neurodegenerative disease (0.530); smoking initiation (0.288); ovarian neoplasm (0.171); cancer (0.122); neoplasm (0.114)
- **Europe PMC papers**: 4080
- **Why important**: TXN is connected to the central APOC1 hub and is detected in cervix_uterine tissue. It is an intracellular redox protein with annotations for redox homeostasis, peroxide detoxification, radiation response, and signaling. Its substantial literature and cancer and neurodegenerative disease associations make it a useful indicator of cellular stress context rather than a specific lipid pathway component.
- **Conclusion**: Established evidence supports TXN as a redox and stress-related component of the module. Its co-abundance with APOC1 may reflect a shared physiological state or tissue composition; a direct APOC1–TXN mechanism is only a hypothesis.

#### SUCLG2

- **Related proteins** (co-abundance neighbors): APOC1 (1.00), SQOR (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase GDP-forming subunit beta. This gene encodes a GTP-specific beta subunit of succinyl-CoA synthetase. Succinyl-CoA synthetase catalyzes the reversible reaction involving the formation of succinyl-CoA and succinate. Alternate splicing results in multiple transcript variants. Pseudogenes of this gene are found on chromosomes 5 and 12. [provided by RefSeq, Apr 2010].
- **Diseases (Open Targets)**: smoking initiation (0.377); breast disorder (0.325); vitamin B deficiency (0.318); alcohol drinking (0.314); duodenal ulcer (0.270)
- **Europe PMC papers**: 1184
- **Why important**: SUCLG2 forms the mitochondrial branch with SQOR and is detected in cervix_uterine tissue. It encodes a subunit of succinyl-CoA synthetase and is annotated for the tricarboxylic acid cycle and succinyl-CoA metabolism. Its liver and hepatocyte enrichment provides a possible metabolic bridge between the lipoprotein-associated signal and mitochondrial energy metabolism.
- **Conclusion**: Established evidence supports SUCLG2 as a mitochondrial intermediary in central metabolism. Its placement in the module is consistent with coordinated metabolic state, but the data do not show that SUCLG2 physically interacts with APOC1 or APOE.

#### SQOR

- **Related proteins** (co-abundance neighbors): SUCLG2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sulfide quinone oxidoreductase. The protein encoded by this gene may function in mitochondria to catalyze the conversion of sulfide to persulfides, thereby decreasing toxic concencrations of sulfide. Alternative splicing results in multiple transcript variants that encode the same protein. [provided by RefSeq, Sep 2012].
- **Diseases (Open Targets)**: sulfide quinone oxidoreductase deficiency (0.675); Leigh syndrome (0.381); urolithiasis (0.320); alcohol drinking (0.320); type 2 diabetes mellitus (0.285)
- **Europe PMC papers**: 376
- **Why important**: SQOR is the mitochondrial partner of SUCLG2 in the co-abundance graph and is annotated for sulfide oxidation. It is enhanced in intestine and in several intestinal and esophageal cell populations, and its deficiency is associated with mitochondrial and metabolic disease phenotypes. This gives the module a distinctive sulfur-redox and mitochondrial detoxification component.
- **Conclusion**: Established evidence supports SQOR as a mitochondrial sulfide-detoxification marker that may complement the SUCLG2 metabolic signal. Its relationship to the APOC1-centered portion remains a co-abundance hypothesis rather than an established molecular interaction.

## Module 3

**Tissue pair**: cervix_uterine and stem_cells  
**Genes (10)**: C2orf49, CLIC4, GGH, HEBP1, HMGA1, LGALS3, NOP16, PPIL1, RAB34, VAPB

### Function

No GO or KEGG term passed global correction, and there were no supplementary STRING enrichment terms. The co-abundance pattern therefore does not establish a single annotated pathway. The network instead suggests a coordinated cellular state linking nucleolar and transcriptional regulation with vesicle, membrane, lysosome, cilium, and epithelial-polarity biology. NOP16 is the most connected node and is annotated for ribosomal large-subunit biogenesis; HMGA1 is a chromatin-associated transcriptional regulator; RAB34 is involved in Golgi trafficking, lysosome positioning, macropinocytosis, and cilium assembly; VAPB supports endoplasmic-reticulum and vesicle functions; CLIC4 is linked to differentiation, polarity, cytoskeletal organization, and chloride transport; and LGALS3 can connect intracellular regulation with extracellular-matrix and immune-related processes. These annotations support a broad cell-state interpretation rather than a demonstrated canonical pathway. The co-abundance edges are evidence of coordinated abundance, not proof of direct biochemical interaction.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: LGALS3 is secreted to blood, whereas GGH is classified as intracellular and membrane-associated, and the remaining proteins are not secreted. The module is also not dominated by blood-cell markers. Most genes have low immune-cell specificity, although several show enrichment or enhancement in monocyte, dendritic-cell, B-cell, or plasma-cell populations. HPA indicates broad tissue distribution for many genes, with cell-type enhancement for nearly the whole module. Extravillous, cytotrophoblast, and migrating cytotrophoblast annotations recur, while epithelial, stromal, smooth-muscle, and other cell types also appear. Cervical protein detection is present for most genes, whereas there is no matching HPA tissue for stem cells. Thus, the shared signal could reflect a shared epithelial, stromal, progenitor-like, or other cellular composition, or a common state across samples; the data do not support attributing it specifically to blood contamination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module-member pair met the supplied stringent STRING interaction criterion, and no STRING functional-enrichment term was reported. No hu.MAP complex contained multiple module members. Consequently, the observed network is not corroborated here as a known physical complex or a densely documented interaction network. The strongest co-abundance relationships are therefore potentially informative, but they should be treated as dataset-specific associations until tested with independent protein-interaction, perturbation, or spatial data. Known functions of individual proteins, such as NOP16 in nucleolar ribosome biogenesis, RAB34 in trafficking and lysosome positioning, VAPB in endoplasmic-reticulum membrane organization, and CLIC4 in polarity and differentiation, provide biological context without validating direct interactions among the module members.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a novel co-abundance association because its members form a cross-functional pattern without reported STRING enrichment, without a multi-member hu.MAP complex, and without globally significant GO or KEGG enrichment. However, absence from these resources does not prove novelty: the genes have established individual functions and some have extensive literature, while co-abundance modules can capture tissue composition or cell state rather than a previously unknown molecular complex. A defensible claim is that the specific shared association across cervix_uterine and stem_cells is a candidate finding requiring replication, comparison with independent cohorts, cell-composition adjustment, and validation at the protein or spatial level.

**Hypothesis.** Hypothesis: the module reflects a shared epithelial or progenitor-like cellular state in which nucleolar and chromatin programs are coordinated with membrane trafficking, lysosome positioning, vesicle handling, and cell-surface or extracellular signaling. NOP16 and HMGA1 could mark the biosynthetic and transcriptional state, while RAB34, VAPB, and CLIC4 could support membrane, organelle, polarity, and trafficking changes; LGALS3 could provide an extracellular or immune-interacting output. An alternative hypothesis is that the association is driven mainly by a recurring cell population or mixed-tissue composition rather than coordinated regulation within individual cells. This distinction should be tested by single-cell deconvolution, cell-stratified co-abundance analysis, and targeted protein validation.

### Important genes

#### NOP16

- **Related proteins** (co-abundance neighbors): C2orf49 (0.90), LGALS3 (0.87), HEBP1 (0.84), PPIL1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP16 nucleolar protein. This gene encodes a protein that is localized to the nucleolus. Expression of this gene is induced by estrogens and Myc protein and is a marker of poor patient survival in breast cancer. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.473); Parkinson disease (0.462); lysosomal storage disease (0.462); Alzheimer disease (0.462); colorectal carcinoma (0.083)
- **Europe PMC papers**: 258
- **Why important**: NOP16 is the network hub with the broadest set of module connections. It is a nucleolar protein annotated for ribosomal large-subunit biogenesis, is induced by estrogens and Myc according to the supplied RefSeq summary, and has been described as a marker of poor survival in breast cancer. Its broad HPA distribution and detectable cervical protein support biological relevance in the shared tissue context. Its substantial literature and disease links make it a strong anchor for interpreting the module's biosynthetic and growth-related component.
- **Conclusion**: Established evidence supports NOP16 as a central co-abundance node associated with nucleolar ribosome biogenesis and cancer-related expression context. It is plausible, but not established, that NOP16 coordinates the broader module or drives the shared state; the network alone cannot distinguish regulation from correlated cell composition.

#### LGALS3

- **Related proteins** (co-abundance neighbors): NOP16 (0.87), HMGA1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galectin 3. This gene encodes a member of the galectin family of carbohydrate binding proteins. Members of this protein family have an affinity for beta-galactosides. The encoded protein is characterized by an N-terminal proline-rich tandem repeat domain and a single C-terminal carbohydrate recognition domain. This protein can self-associate through the N-terminal domain allowing it to bind to multivalent sac…
- **Diseases (Open Targets)**: melanoma (0.126); COVID-19 (0.123); neoplasm (0.120); hepatocellular carcinoma (0.117); cancer (0.117)
- **Europe PMC papers**: 13803
- **Why important**: LGALS3 is the most extensively studied module member in the supplied literature information and has a distinctive secreted-to-blood annotation. It can self-associate, bind multivalent beta-galactoside ligands, localize to the extracellular matrix, cytoplasm, and nucleus, and is associated with monocyte and neutrophil chemotaxis, epithelial differentiation, complex assembly, and T-cell regulation. Its link to NOP16 and HMGA1 places an extracellular and immune-responsive protein beside nucleolar and chromatin-associated components.
- **Conclusion**: Established evidence supports LGALS3 as a multifunctional carbohydrate-binding protein with epithelial, extracellular-matrix, and immune-related roles. It is a plausible interface between cell state and extracellular or immune signaling, but the module does not establish that LGALS3 mediates the shared cervix_uterine and stem_cells association.

#### RAB34

- **Related proteins** (co-abundance neighbors): GGH (0.86), CLIC4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Nucleoplasm, Primary cilium; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB34, member RAS oncogene family. This gene encodes a protein belonging to the RAB family of proteins, which are small GTPases involved in protein transport. This family member is a Golgi-bound member of the secretory pathway that is involved in the repositioning of lysosomes and the activation of macropinocytosis. Alternative splicing of this gene results in multiple transcript variants. An alternatively spliced transcript varian…
- **Diseases (Open Targets)**: orofaciodigital syndrome 20 (0.605); Jeune syndrome (0.341); orofaciodigital syndrome (0.185); neurodegenerative disease (0.175); glioma (0.085)
- **Europe PMC papers**: 632
- **Why important**: RAB34 connects GGH with CLIC4 and is annotated as a Golgi-bound small GTPase involved in protein transport, lysosome repositioning, macropinocytosis, cilium assembly, and Golgi-to-plasma-membrane transport. HPA places it in several cell types relevant to stromal, trophoblast, and myeloid contexts. Its disease associations include ciliopathy-related disorders and neurodegenerative disease, giving it functional relevance beyond a generic expression marker.
- **Conclusion**: Established evidence supports RAB34 as a trafficking and organelle-positioning regulator. Its bridging position makes it a credible candidate for the module's membrane and lysosomal component. Whether it mechanistically links the other module processes is a hypothesis requiring perturbation or localization experiments.

#### HMGA1

- **Related proteins** (co-abundance neighbors): LGALS3 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: high mobility group AT-hook 1. This gene encodes a chromatin-associated protein involved in the regulation of gene transcription, integration of retroviruses into chromosomes, and the metastatic progression of cancer cells. The encoded protein preferentially binds to the minor groove of AT-rich regions in double-stranded DNA. Multiple transcript variants encoding different isoforms have been found for this gene. Pseudogenes of …
- **Diseases (Open Targets)**: HIV infectious disease (0.581); neurodegenerative disease (0.526); atrial fibrillation (0.435); type 2 diabetes mellitus (0.409); head and neck squamous cell carcinoma (0.389)
- **Europe PMC papers**: 5150
- **Why important**: HMGA1 is the module's chromatin-associated regulatory component and is connected to LGALS3. It binds AT-rich DNA and is annotated for regulation of transcription, nucleosome disassembly, DNA repair, signal transduction, and cancer progression. Its HPA cell-type annotations include trophoblast and epithelial populations, and it has a substantial disease and literature record. These features make it informative for testing whether the module reflects a transcriptional state rather than only protein trafficking.
- **Conclusion**: Established evidence supports HMGA1 as a transcriptional and chromatin regulator associated with differentiation and disease biology. It could contribute to a shared progenitor-like or epithelial transcriptional state, but no evidence here demonstrates that HMGA1 regulates the other module members.

#### CLIC4

- **Related proteins** (co-abundance neighbors): RAB34 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Centrosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CLIC family member 4. Chloride channels are a diverse group of proteins that regulate fundamental cellular processes including stabilization of cell membrane potential, transepithelial transport, maintenance of intracellular pH, and regulation of cell volume. Chloride intracellular channel 4 (CLIC4) protein, encoded by the CLIC4 gene, is a member of the p64 family; the gene is expressed in many tissues and exhibits a i…
- **Diseases (Open Targets)**: hypertensive disorder (0.352); Short stature (0.259); cardiovascular disorder (0.237); response to xenobiotic stimulus (0.233); exostosis (0.212)
- **Europe PMC papers**: 4070
- **Why important**: CLIC4 is the partner of RAB34 in the module and is annotated for chloride transport, cell differentiation, keratinocyte differentiation, cell migration, apical-basal polarity, and cytoskeletal organization. Its HPA annotations include blood-vessel, stromal, trophoblast, mesothelial, and plasma-cell contexts. Its broad functional relevance and substantial literature make it a useful candidate for connecting trafficking with epithelial or stromal organization, despite its lack of detected cervical protein in the supplied HPA record.
- **Conclusion**: Established evidence supports CLIC4 as a multifunctional intracellular and membrane-associated protein involved in differentiation and polarity. Its association with RAB34 is consistent with a trafficking or cell-architecture hypothesis, but the absent cervical protein detection and lack of external interaction support argue for cautious interpretation.

## Module 4

**Tissue pair**: cervix_uterine and stem_cells  
**Genes (5)**: ATP5F1C, CDH1, CDA, CZIB, TNC

### Function

The module does not have a statistically supported GO or KEGG functional theme: no term passed global correction. Its genes instead suggest a mixed cell-state signal involving epithelial adhesion and tissue remodeling through CDH1 and TNC, pyrimidine salvage through CDA, mitochondrial energy production through ATP5F1C, and a poorly characterized zinc-binding protein through CZIB. TNC is the most connected gene and links the adhesion-related CDH1 signal with CDA and ATP5F1C, but the network does not establish a single biochemical pathway. The most defensible interpretation is a shared epithelial or stromal state involving extracellular-matrix remodeling, cell-cell adhesion, nucleotide metabolism, and energy demand, rather than a validated molecular complex.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only TNC is annotated as secreted to the extracellular matrix. It is also not predominantly blood-cell enriched. HPA shows tissue enhancement for most genes and cell-type enhancement for all genes, with heterogeneous epithelial, stromal, gastrointestinal, hepatic, neural, and reproductive-cell annotations. CDA has immune-cell enhancement for neutrophils, whereas the other genes have low, absent, or limited immune-cell specificity. This argues against interpreting the module primarily as a blood-contamination signal, although shared cell types or cellular state differences between tissues remain plausible. In cervix_uterine, CDH1 is protein-detected while the other proteins are not detected; there is no matching HPA tissue for stem_cells, so the protein-level evidence for the shared signal is limited.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence criterion, no supplementary STRING enrichment was present, and no hu.MAP complex contained multiple module members. Therefore, the co-abundance edges are not supported here as established physical interactions or membership in a known multiprotein complex. The absence of STRING and hu.MAP support weakens a direct-complex interpretation, while not disproving coordinated regulation, shared cellular localization, or indirect association.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a novel cross-tissue co-abundance pattern, because the specific module has no matching high-confidence STRING relationships, no supported hu.MAP complex, and no globally corrected GO or KEGG annotation. However, it cannot be called a new biological mechanism from these data alone. The module is small, contains genes with well-established and heterogeneous functions, and lacks independent interaction or enrichment support. A stronger novelty claim would require replication in independent samples, control for cell composition, and validation at the transcript or protein level.

**Hypothesis.** Hypothesis: the shared module reflects a conserved epithelial or stromal remodeling state in which TNC-mediated extracellular-matrix remodeling is coordinated with CDH1-dependent epithelial adhesion, while CDA and ATP5F1C report accompanying changes in nucleotide handling and mitochondrial energy demand. CZIB may mark a less characterized regulatory component of this state. This is a mechanistic hypothesis, not an established pathway, because the module lacks globally significant enrichment and external interaction support.

### Important genes

#### TNC

- **Related proteins** (co-abundance neighbors): CDH1 (0.91), CDA (0.90), ATP5F1C (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tenascin C. This gene encodes an extracellular matrix protein with a spatially and temporally restricted tissue distribution. This protein is homohexameric with disulfide-linked subunits, and contains multiple EGF-like and fibronectin type-III domains. It is implicated in guidance of migrating neurons as well as axons during development, synaptic plasticity, and neuronal regeneration. [provided by RefSeq, Jul…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss (0.619); deafness (0.552); osteoarthritis, hip (0.551); total hip arthroplasty (0.468); Varicose veins (0.460)
- **Europe PMC papers**: 12274
- **Why important**: TNC is the network hub, connecting CDH1, CDA, and ATP5F1C. Its established extracellular-matrix role, association with cell adhesion, epithelial morphogenesis, wound response, and cell growth regulation makes it the strongest candidate for coordinating tissue remodeling. It also has substantial literature and disease-association evidence.
- **Conclusion**: Established evidence supports TNC as an extracellular-matrix and adhesion-regulatory protein and as the central co-abundance connector. It is plausible, but not demonstrated, that TNC organizes the shared module's remodeling signal.

#### CDH1

- **Related proteins** (co-abundance neighbors): TNC (0.91); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cadherin 1. This gene encodes a classical cadherin of the cadherin superfamily. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature glycoprotein. This calcium-dependent cell-cell adhesion protein is comprised of five extracellular cadherin repeats, a transmembrane region and a highly conserved cyto…
- **Diseases (Open Targets)**: CDH1-related diffuse gastric and lobular breast cancer syndrome (0.833); blepharocheilodontic syndrome 1 (0.760); Familial gastric cancer (0.686); ovarian cancer (0.684); endometrial carcinoma (0.676)
- **Europe PMC papers**: 32214
- **Why important**: CDH1 is the module's epithelial cell-cell adhesion component and is located at the plasma membrane and cell junctions. It is protein-detected in cervix_uterine, connects directly to TNC, has extensive literature, and has strong associations with hereditary and sporadic epithelial cancers.
- **Conclusion**: Established evidence supports a role for CDH1 in epithelial cohesion and junctional organization. Its participation in this module is consistent with an epithelial-state interpretation, but the co-abundance data do not show that CDH1 mechanistically regulates the other genes.

#### CDA

- **Related proteins** (co-abundance neighbors): TNC (0.90), CZIB (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytidine deaminase. This gene encodes an enzyme involved in pyrimidine salvaging. The encoded protein forms a homotetramer that catalyzes the irreversible hydrolytic deamination of cytidine and deoxycytidine to uridine and deoxyuridine, respectively. It is one of several deaminases responsible for maintaining the cellular pyrimidine pool. Mutations in this gene are associated with decreased sensitivity to the cytosin…
- **Diseases (Open Targets)**: myelodysplastic syndrome (0.511); myeloid leukemia (0.393); acute myeloid leukemia (0.378); chronic myelomonocytic leukemia (0.341); neurodegenerative disease (0.318)
- **Europe PMC papers**: 8763
- **Why important**: CDA is the metabolic bridge between TNC and CZIB in the inferred network. Its established cytidine and deoxycytidine deamination activity connects the module to pyrimidine salvage, and its tissue and immune-cell annotations are compatible with differentiated epithelial or myeloid-associated contexts. It also has substantial literature and leukemia-related disease associations.
- **Conclusion**: Established evidence supports CDA as a pyrimidine-metabolism enzyme. Its inclusion may reflect nucleotide demand or cell-state composition, but linking its enzymatic activity directly to TNC-mediated remodeling remains a hypothesis.

#### ATP5F1C

- **Related proteins** (co-abundance neighbors): TNC (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP synthase F1 subunit gamma. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: late-onset Alzheimers disease (0.350); scleritis (0.189); diaphragm disorder (0.082); glioblastoma (0.044); external ear disorder (0.042)
- **Europe PMC papers**: 306
- **Why important**: ATP5F1C is the mitochondrial ATP synthase gamma subunit and contributes to oxidative phosphorylation and ATP biosynthesis. Its connection to the TNC hub provides a possible energetic component to the module, while its epithelial cell-type annotations support a tissue-state interpretation. Its literature volume is more limited than that of TNC, CDH1, or CDA.
- **Conclusion**: Established evidence supports ATP5F1C as a mitochondrial ATP-synthesis component. Its module association may indicate altered energy requirements accompanying adhesion or remodeling, but this energetic coupling is not directly demonstrated.

