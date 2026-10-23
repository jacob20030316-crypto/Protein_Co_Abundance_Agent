# Conserved co-abundance modules: breast and liver

## Module 0

**Tissue pair**: breast and liver  
**Genes (5)**: COL6A1, COL6A2, COL6A3, FGA, HSPG2

### Function

The module is best interpreted as an extracellular-matrix and tissue-scaffold program. Every module gene supports the globally corrected extracellular-matrix structural-constituent term (GO:MF extracellular matrix structural constituent; q_global = 3.39e-05), while collagen structure, extracellular matrix, external encapsulating structure, collagen-trimer, basement-membrane/interstitial-matrix interface, integrin signaling, and ECM-receptor interaction are also supported by (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.00068) through (GO:CC endoplasmic reticulum lumen; q_global = 0.0311). The central biological unit is the COL6A1–COL6A2–COL6A3 type VI collagen assembly, with HSPG2 providing a basement-membrane and proteoglycan component and FGA contributing a fibrinogen-based matrix and adhesion component. The muscle-cell cytoskeleton and protein-digestion terms (KEGG Protein digestion and absorption - Homo sapiens (human); q_global = 0.00749) and (KEGG Cytoskeleton in muscle cells - Homo sapiens (human); q_global = 0.0177) should be treated as contextual pathway representations rather than evidence that the module is principally a muscle or digestive program.

**Cell composition.** All module genes are annotated by HPA as secreted proteins, so this is not a broadly expressed intracellular housekeeping module. Most genes are associated with extracellular matrix, stromal, fibroblast, fibro-adipogenic progenitor, hepatic stellate, or smooth-muscle contexts. HPA indicates that the module is largely not detected in immune cells, although COL6A2 has group-enriched blood-cell annotation. FGA is liver-enriched and secreted to blood, whereas HSPG2 is associated with blood vessels and is detected in both breast and liver. The shared breast–liver signal may therefore reflect conserved stromal, vascular, or matrix-producing cell types, with a possible contribution from liver-derived circulating fibrinogen, rather than a shared epithelial or immune-cell program. Protein detection is incomplete in both tissues, so absence of tissue staining should not be interpreted as absence of the transcript-level co-abundance signal.

**GO/KEGG enrichment**: 15 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF extracellular matrix structural constituent | 3.39e-05 | COL6A1, COL6A2, COL6A3, FGA, HSPG2 |
| KEGG ECM-receptor interaction - Homo sapiens (human) | 0.00068 | COL6A1, COL6A2, COL6A3, HSPG2 |
| GO:MF extracellular matrix structural constituent conferring tensile strength | 0.00249 | COL6A1, COL6A2, COL6A3 |
| KEGG Integrin signaling - Homo sapiens (human) | 0.00298 | COL6A1, COL6A2, COL6A3, FGA |
| GO:CC external encapsulating structure | 0.0039 | COL6A1, COL6A2, COL6A3, HSPG2 |
| GO:CC extracellular matrix | 0.0039 | COL6A1, COL6A2, COL6A3, HSPG2 |
| KEGG Protein digestion and absorption - Homo sapiens (human) | 0.00749 | COL6A1, COL6A2, COL6A3 |
| GO:MF structural molecule activity | 0.00909 | COL6A1, COL6A2, COL6A3, FGA, HSPG2 |
| GO:CC collagen trimer | 0.00924 | COL6A1, COL6A2, COL6A3 |
| GO:CC collagen type VI trimer | 0.0157 | COL6A1, COL6A3 |
| GO:CC collagen beaded filament | 0.0157 | COL6A1, COL6A3 |
| GO:CC basement membrane/interstitial matrix interface | 0.0157 | COL6A1, COL6A3 |
| GO:CC von-Willerbrand-factor-A-domain-rich collagen trimer | 0.0157 | COL6A1, COL6A3 |
| KEGG Cytoskeleton in muscle cells - Homo sapiens (human) | 0.0177 | COL6A1, COL6A2, COL6A3, HSPG2 |
| GO:CC endoplasmic reticulum lumen | 0.0311 | COL6A1, COL6A2, COL6A3, FGA |

### STRING and hu.MAP

STRING supports the three pairwise relationships among COL6A1, COL6A2, and COL6A3 with very high confidence, matching the established type VI collagen heterotrimer. STRING also reports coherent extracellular-matrix, integrin-interaction, proteoglycan, and ECM-receptor functional groupings (STRING RCTM Integrin cell surface interactions; within-query FDR = 1.48e-06), (STRING Function Extracellular matrix structural constituent; within-query FDR = 5.14e-06), (STRING RCTM ECM proteoglycans; within-query FDR = 8.59e-05), and (STRING KEGG ECM-receptor interaction; within-query FDR = 8.69e-05), but these are supplementary within-query results and are not global enrichment evidence. The HPO and keyword groupings (STRING HPO Wrist flexion contracture; within-query FDR = 2.66e-05) and (STRING HPO Lumbar hyperlordosis; within-query FDR = 0.00012) through (STRING HPO Short neck; within-query FDR = 0.00019) are consistent with collagen-related connective-tissue and muscular phenotypes, but do not establish a module-level disease mechanism. No hu.MAP complex contains multiple module members. STRING does not report the FGA or HSPG2 relationships as known protein interactions at the specified confidence threshold. Thus, the network combines a well-established collagen subassembly with less directly established co-abundance links to fibrinogen and perlecan.

**STRING interactions (score >= 0.7)**: 3 of 10 gene pairs: COL6A1–COL6A2 (0.998); COL6A1–COL6A3 (0.994); COL6A2–COL6A3 (0.994)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Integrin cell surface interactions (FDR = 1.48e-06, 5 genes); Function Extracellular matrix structural constituent (FDR = 5.14e-06, 5 genes); HPO Wrist flexion contracture (FDR = 2.66e-05, 4 genes); RCTM ECM proteoglycans (FDR = 8.59e-05, 4 genes); KEGG ECM-receptor interaction (FDR = 8.69e-05, 4 genes); HPO Lumbar hyperlordosis (FDR = 0.00012, 4 genes); HPO Spinal rigidity (FDR = 0.00012, 4 genes); HPO Foot joint contracture (FDR = 0.00012, 4 genes); HPO Joint contracture of the hand (FDR = 0.00012, 4 genes); HPO Craniofacial dystonia (FDR = 0.00014, 4 genes); Keyword Hydroxylation (FDR = 0.00017, 4 genes); Keyword Congenital muscular dystrophy (FDR = 0.00017, 3 genes); Keyword Limb-girdle muscular dystrophy (FDR = 0.00017, 3 genes); HPO Tall stature (FDR = 0.00019, 4 genes); HPO Short neck (FDR = 0.00019, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The underlying biology is not new: type VI collagen assembly, perlecan biology, fibrinogen function, extracellular-matrix structure, and integrin-associated matrix signaling are established. The module is therefore not plausibly a novel molecular complex. Its potentially new aspect is the conserved co-abundance pattern across breast and liver and the observed connection between the collagen VI trio, HSPG2, and FGA in this dataset. That interpretation remains a context-specific network observation rather than a demonstrated new physical interaction or mechanism. Lack of a hu.MAP complex, or lack of STRING support for some edges, is insufficient by itself to establish novelty.

**Hypothesis.** Hypothesis: the conserved module reflects coordinated production and remodeling of a vascular and stromal extracellular niche. Collagen VI may provide the structural microfibrillar scaffold, HSPG2 may organize basement-membrane and cell-surface interactions, and FGA may couple the matrix environment to coagulation-associated adhesion and circulating liver-derived protein. In breast and liver samples, variation in stromal, vascular, or hepatic stellate cell abundance could therefore generate the shared co-abundance pattern. This hypothesis should be tested with cell-composition adjustment, spatial localization, and independent measurements of matrix deposition rather than inferred solely from co-abundance.

### Important genes

#### COL6A1

- **Related proteins** (co-abundance neighbors): COL6A2 (0.95), COL6A3 (0.88), FGA (0.81); STRING partners: COL6A2 (0.998), COL6A3 (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is the most connected and strongest module node and links the collagen VI trio to FGA. It appears across all globally corrected GO and KEGG terms (GO:MF extracellular matrix structural constituent; q_global = 3.39e-05) through (GO:CC endoplasmic reticulum lumen; q_global = 0.0311), is secreted to extracellular matrix, and is associated with fibroblast and stromal cell contexts. Its established role is as an alpha chain of the collagen VI heterotrimer, and its disease associations include Bethlem myopathy and Ullrich congenital muscular dystrophy. Its literature support is substantial, making it the best network anchor for the module.
- **Conclusion**: Established evidence supports COL6A1 as a core structural component and principal network anchor of a collagen VI extracellular-matrix program. It is a plausible marker of the conserved matrix-producing cell population. It is not established that COL6A1 drives the breast–liver co-abundance pattern; that causal interpretation remains a hypothesis.

#### COL6A3

- **Related proteins** (co-abundance neighbors): COL6A2 (0.89), COL6A1 (0.88); STRING partners: COL6A1 (0.994), COL6A2 (0.994)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 3 chain. This gene encodes the alpha-3 chain, one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The alpha-3 chain of type VI collagen is much larger than the alpha-1 and -2 chains. This difference in size is largely due to an increase in the number of subdomains, similar to von Willebrand Factor type A domains, that are found in the amino termin…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy (0.766); dystonia 27 (0.764); Bethlem myopathy (0.758); Bethlem myopathy 1C (0.747); Bethlem myopathy 1A (0.718)
- **Europe PMC papers**: 5386
- **Why important**: COL6A3 is a core collagen VI component connected to both other collagen VI chains and appears across the globally corrected matrix and integrin-related terms (GO:MF extracellular matrix structural constituent; q_global = 3.39e-05) through (GO:CC endoplasmic reticulum lumen; q_global = 0.0311). It is tissue-enhanced in smooth muscle and cell-type enhanced in fibroblast, fibro-adipogenic progenitor, stromal, and hepatic stellate contexts. Its large alpha chain contains von Willebrand factor type A-related domains, and it is associated with Bethlem myopathy, Ullrich congenital muscular dystrophy, and dystonia. It has substantial literature support.
- **Conclusion**: Established evidence identifies COL6A3 as a central structural and cell-context marker of the module, especially for stromal and smooth-muscle-associated matrix biology. Its domain architecture could support matrix organization, but a specific signaling role in this conserved module is not demonstrated by the fact sheet.

#### COL6A2

- **Related proteins** (co-abundance neighbors): COL6A1 (0.95), COL6A3 (0.89); STRING partners: COL6A1 (0.998), COL6A3 (0.994)
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 2 chain. This gene encodes one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The product of this gene contains several domains similar to von Willebrand Factor type A domains. These domains have been shown to bind extracellular matrix proteins, an interaction that explains the importance of this collagen in organizing matrix components. Mutation…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy 1B (0.770); Bethlem myopathy (0.755); Ullrich congenital muscular dystrophy (0.743); Bethlem myopathy 1B (0.723); Bethlem myopathy 1A (0.713)
- **Europe PMC papers**: 4115
- **Why important**: COL6A2 completes the collagen VI trio and is connected to both COL6A1 and COL6A3 in the module and in STRING. It participates in the globally corrected structural, matrix, collagen, and integrin terms (GO:MF extracellular matrix structural constituent; q_global = 3.39e-05) through (GO:CC collagen trimer; q_global = 0.00924), (KEGG Cytoskeleton in muscle cells - Homo sapiens (human); q_global = 0.0177), and (GO:CC endoplasmic reticulum lumen; q_global = 0.0311). HPA places it in stromal, fibroblast, fibro-adipogenic progenitor, and hepatic stellate contexts, with additional group-enriched blood-cell annotation. It is associated with Bethlem myopathy and Ullrich muscular dystrophy and has substantial literature support.
- **Conclusion**: Established evidence supports COL6A2 as an essential component of the collagen VI structural subassembly and as a marker of matrix-producing cell populations. The blood-cell annotation warrants attention when analyzing tissue samples, but it does not establish that immune cells generate the module because most module genes are not detected in immune cells.

#### HSPG2

- **Related proteins** (co-abundance neighbors): FGA (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in breast, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 is the perlecan proteoglycan and is the module's vascular-associated matrix component. It participates in the globally corrected extracellular-matrix, external-structure, ECM-receptor, and structural-molecule terms (GO:MF extracellular matrix structural constituent; q_global = 3.39e-05), (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.00068), (GO:CC external encapsulating structure; q_global = 0.0039), (GO:CC extracellular matrix; q_global = 0.0039), (GO:MF structural molecule activity; q_global = 0.00909), and (KEGG Cytoskeleton in muscle cells - Homo sapiens (human); q_global = 0.0177). It is connected in the module to FGA, is associated with hepatic stellate and fibro-adipogenic progenitor contexts, is tissue-enhanced in blood vessel, and is detected in both breast and liver. Its established functions include cross-linking extracellular-matrix and cell-surface molecules and regulating angiogenesis-related biology.
- **Conclusion**: Established evidence supports HSPG2 as a plausible bridge between the collagen-rich scaffold and vascular or basement-membrane biology. Its module-level connection to FGA is a co-abundance observation rather than a confirmed physical interaction, so any proposed bridging mechanism requires experimental validation.

#### FGA

- **Related proteins** (co-abundance neighbors): COL6A1 (0.81), HSPG2 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibrinogen alpha chain. This gene encodes the alpha subunit of the coagulation factor fibrinogen, which is a component of the blood clot. Following vascular injury, the encoded preproprotein is proteolytically processed by thrombin during the conversion of fibrinogen to fibrin. Mutations in this gene lead to several disorders, including dysfibrinogenemia, hypofibrinogenemia, afibrinogenemia and renal amyloidosis. Alterna…
- **Diseases (Open Targets)**: familial dysfibrinogenemia (0.789); familial visceral amyloidosis (0.765); congenital afibrinogenemia (0.757); familial hypodysfibrinogenemia (0.659); congenital fibrinogen deficiency (0.619)
- **Europe PMC papers**: 7516
- **Why important**: FGA is the liver-enriched, hepatocyte-associated, blood-secreted member of the module and connects COL6A1 with HSPG2. It contributes to the globally corrected structural-molecule, ECM-receptor, integrin-signaling, extracellular-matrix, and endoplasmic-reticulum-lumen terms (GO:MF extracellular matrix structural constituent; q_global = 3.39e-05), (KEGG Integrin signaling - Homo sapiens (human); q_global = 0.00298), (GO:MF structural molecule activity; q_global = 0.00909), and (GO:CC endoplasmic reticulum lumen; q_global = 0.0311). Its established protein product is the alpha chain of fibrinogen, with functions in coagulation, platelet activation, fibrinolysis, and cell-matrix adhesion. It has extensive literature support and disease associations involving fibrinogen deficiency and dysfibrinogenemia.
- **Conclusion**: Established evidence supports FGA as a liver-derived circulating and adhesion-related component that may connect matrix biology with hemostatic biology. Its presence makes shared sample composition or vascular and plasma contribution an important alternative explanation. A direct functional role for FGA in organizing the collagen VI–HSPG2 module is not established.
