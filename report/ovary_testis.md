# Conserved co-abundance modules: ovary and testis

## Module 0

**Tissue pair**: ovary and testis  
**Genes (12)**: SLC3A2, ANXA2, ATP1A1, HSD17B4, GFM1, GNA11, GNAI3, ALDH18A1, SEC22B, TFRC, TMX1, UFSP2

### Function

The strongest interpretation is a membrane-associated transport and signaling module with an additional vesicle and organelle-trafficking component. The primary evidence is the globally corrected enrichment for plasma membrane protein complex (GO:CC plasma membrane protein complex; q_global = 0.00207), melanosome (GO:CC melanosome; q_global = 0.00484), pigment granule (GO:CC pigment granule; q_global = 0.00484), and basolateral plasma membrane (GO:CC basolateral plasma membrane; q_global = 0.0373). The recurring genes ANXA2, ATP1A1, SLC3A2, and TFRC support a coordinated cell-surface system involving membrane organization, sodium-potassium electrochemical gradients, amino-acid transport, and receptor-mediated iron uptake. GNA11 and GNAI3 add G-protein-mediated transmembrane signaling, while SEC22B and TMX1 support vesicle trafficking and endoplasmic-reticulum protein handling. The melanosome and pigment-granule terms should be interpreted as shared cellular-compartment annotations rather than proof that this is a specialized pigment module. The remaining genes indicate that the module also connects membrane biology to mitochondrial translation, peroxisomal fatty-acid metabolism, proline and amino-acid biosynthesis, and UFM1-related proteostasis. Thus, the module appears functionally mixed but coherent around polarized membrane organization, intracellular trafficking, nutrient and ion handling, and cellular maintenance.

**Cell composition.** This is not best described as a purely plasma or secreted protein module. HPA identifies several secreted-to-blood or intracellular-and-membrane proteins, particularly ANXA2 and TFRC, but most genes have low tissue specificity rather than a strongly secretory profile. The module includes immune-cell-enhanced or blood-cell-associated signals involving ANXA2, GNA11, TFRC, HSD17B4, and related genes, including monocyte, neutrophil, basophil, and myeloid dendritic-cell associations. All module genes have cell-type-enhanced annotations, with enrichment spanning epithelial, trophoblast, immune, germ-cell-associated, and other cell types. This breadth makes a shared cellular composition or sample-content effect plausible, including contributions from blood or vascular and epithelial cells, rather than requiring a mechanism unique to ovary and testis. Protein detection is much more pervasive in testis than ovary, so the cross-tissue co-abundance signal should be checked against cell-type composition, tissue quality, and stromal or vascular content. The module nevertheless contains bona fide intracellular, mitochondrial, peroxisomal, endoplasmic-reticulum, and plasma-membrane proteins, arguing against a simple plasma-protein-only explanation.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC plasma membrane protein complex | 0.00207 | ANXA2, ATP1A1, GNA11, GNAI3, SLC3A2, TFRC |
| GO:CC melanosome | 0.00484 | ANXA2, ATP1A1, SEC22B, SLC3A2, TFRC |
| GO:CC pigment granule | 0.00484 | ANXA2, ATP1A1, SEC22B, SLC3A2, TFRC |
| GO:CC basolateral plasma membrane | 0.0373 | ANXA2, ATP1A1, SLC3A2, TFRC |

### STRING and hu.MAP

STRING provides no high-confidence pairwise interaction among the module genes at the supplied threshold. Therefore the co-abundance edges should not be presented as established physical interactions. STRING functional enrichment is concordant with the compartment interpretation: plasma membrane protein complex, melanosome, basolateral membrane, membrane complex, and organelle membrane annotations recur in (STRING Component Plasma membrane protein complex; within-query FDR = 0.00095) through (STRING COMPARTMENTS Plasma membrane protein complex; within-query FDR = 0.0391). These are supplementary annotations and do not replace the globally corrected GO evidence. hu.MAP supplies partial complex context. GNA11 and ANXA2 occur together in (hu.MAP huMAP3_05674.1) and (hu.MAP huMAP3_09165.1), while GNA11 and GNAI3 recur together in (hu.MAP huMAP3_13105.1) and (hu.MAP huMAP3_11173.1), supporting a relationship between membrane-associated signaling and cytoskeletal or membrane-organizing machinery. ALDH18A1 and GFM1 occur together in (hu.MAP huMAP3_10525.1) and (hu.MAP huMAP3_13468.1), linking part of the module to mitochondrial and metabolic machinery. However, each hu.MAP complex contains many additional proteins and only a small subset of its members belongs to this module. The evidence therefore supports embedded functional neighborhoods, not one experimentally established complex containing the whole module.

**STRING interactions (score >= 0.7)**: 0 of 66 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Component Plasma membrane protein complex (FDR = 0.00095, 6 genes); Component Melanosome (FDR = 0.0015, 5 genes); Component Basolateral plasma membrane (FDR = 0.0083, 4 genes); Component Membrane protein complex (FDR = 0.0093, 7 genes); Component Organelle membrane (FDR = 0.0201, 10 genes); COMPARTMENTS Plasma membrane protein complex (FDR = 0.0391, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05674.1 (ANXA2, GNA11; 2/12); huMAP3_13105.1 (GNAI3, GNA11; 2/27); huMAP3_10525.1 (ALDH18A1, GFM1; 2/33); huMAP3_11173.1 (GNAI3, GNA11; 2/34); huMAP3_09165.1 (ANXA2, GNA11; 2/39); huMAP3_13468.1 (ALDH18A1, GFM1; 2/99)

### Novelty

The module may represent a new tissue-pair co-abundance pattern, but the underlying biology is not wholly new. ANXA2, ATP1A1, TFRC, GNA11, GNAI3, SLC3A2, and SEC22B have established roles in membrane function, signaling, transport, or vesicle biology, and hu.MAP places subsets of the genes in previously characterized complexes. Conversely, the absence of high-confidence STRING edges among the module genes and the lack of a single hu.MAP complex containing the module argue against simply rediscovering a canonical protein complex. The most defensible novelty claim is that coordinated abundance of this particular mixture across ovary and testis may be a new systems-level observation. It is not evidence for a newly discovered molecular interaction or a new gene function. Independent replication, adjustment for cell-type composition, and comparison with published ovary-testis co-expression or proteomic modules would be required before calling the pattern novel.

**Hypothesis.** Hypothesis: the shared module reflects a conserved membrane-homeostasis program in a common cellular compartment present in both tissues. In this model, ATP1A1 establishes ion gradients; SLC3A2 supports amino-acid transport; TFRC supplies iron through endocytic recycling; ANXA2 organizes membrane domains, adhesion, and vesicle behavior; and GNA11 with GNAI3 transduces signals from membrane receptors. SEC22B and TMX1 could coordinate secretory-pathway trafficking and protein-folding quality control, while ALDH18A1, GFM1, and HSD17B4 connect the membrane state to mitochondrial, amino-acid, and peroxisomal metabolism. The pigment-granule annotations may indicate a vesicular or polarized membrane architecture rather than pigmentation itself. A competing explanation is that the module largely reflects shared epithelial, vascular, immune, or other non-germ-cell content. This hypothesis should be tested with cell-resolved data, protein-level localization, perturbation of transport or signaling components, and replication in independent ovary and testis cohorts.

### Important genes

#### ANXA2

- **Related proteins** (co-abundance neighbors): TMX1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in ovary, testis
- **hu.MAP 3.0**: huMAP3_05674.1, huMAP3_09165.1
- **Function (MyGene.info)**: annexin A2. This gene encodes a member of the annexin family. Members of this calcium-dependent phospholipid-binding protein family play a role in the regulation of cellular growth and in signal transduction pathways. This protein functions as an autocrine factor which heightens osteoclast formation and bone resorption. This gene has three pseudogenes located on chromosomes 4, 9 and 10, respectively. Multiple…
- **Diseases (Open Targets)**: neurodegenerative disease (0.443); Alzheimer disease (0.312); Parkinson disease (0.298); lysosomal storage disease (0.289); benign urinary system neoplasm (0.270)
- **Europe PMC papers**: 12966
- **Why important**: ANXA2 is central to the primary compartment signal, appearing in every globally corrected GO term and several supplementary STRING terms. It connects membrane organization, raft assembly, receptor recycling, vesicle budding, adhesion, and angiogenesis. Its module relationship to TMX1 and its membership with GNA11 in hu.MAP contexts place it at the interface of membrane architecture and trafficking. It has strong tissue protein detection in both tissues, broad immune-cell associations, secretion to blood, and a substantial literature base, making it both biologically informative and important for evaluating blood or stromal contamination.
- **Conclusion**: Established evidence supports ANXA2 as a membrane-organizing and trafficking-related component of the module. It is a plausible anchor for the membrane interpretation. The hypothesis that ANXA2 coordinates the entire shared ovary-testis program remains unproven, especially because its blood and immune-cell associations could make it a composition marker rather than a tissue-specific driver.

#### ATP1A1

- **Related proteins** (co-abundance neighbors): GNA11 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 is present in all primary GO compartment terms and all listed STRING compartment terms. Its established function is to maintain sodium and potassium gradients, which can support epithelial polarity, nutrient transport, membrane excitability, and osmotic homeostasis. It is connected to GNA11 in the module and is detected in testis. Its substantial disease and literature record makes it a well-supported functional marker rather than an obscure annotation-driven candidate.
- **Conclusion**: Established evidence supports ATP1A1 as a membrane-homeostasis component that can provide the physiological foundation for the module's transport and polarized-membrane signal. It is not established that ATP1A1 directly drives the co-abundance pattern or that the pattern is specific to reproductive tissue.

#### TFRC

- **Related proteins** (co-abundance neighbors): ALDH18A1 (0.86), GFM1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes, Lysosomes; IHC detected in ovary, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transferrin receptor. This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: TFRC-related combined immunodeficiency (0.623); type 2 diabetes mellitus (0.518); mucopolysaccharidosis type 2 (0.490); diabetes mellitus (0.471); diabetic retinopathy (0.343)
- **Europe PMC papers**: 14164
- **Why important**: TFRC is the most pervasive primary GO member, occurring in the plasma membrane, melanosome, pigment granule, and basolateral membrane terms. Its known role in receptor-mediated iron uptake links the module to endocytosis, growth, hypoxia response, and intracellular iron homeostasis. It connects the metabolic branch containing ALDH18A1 and GFM1, is detected in both tissues, is secreted to blood according to HPA, and has the largest literature volume among the selected genes. Its erythroid, macrophage, monocyte, and trophoblast associations make it especially useful for separating a true tissue program from shared cellular composition.
- **Conclusion**: Established evidence supports TFRC as an iron-uptake and endocytic component of the module. Its position makes nutrient supply and vesicular recycling plausible mechanisms. The hypothesis that TFRC links membrane transport to reproductive-cell metabolism needs cell-specific validation because its blood and immune associations provide a strong alternative explanation.

#### GNA11

- **Related proteins** (co-abundance neighbors): UFSP2 (0.88), GNAI3 (0.85), ATP1A1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in ovary, testis
- **hu.MAP 3.0**: huMAP3_05674.1, huMAP3_13105.1, huMAP3_11173.1, huMAP3_09165.1
- **Function (MyGene.info)**: G protein subunit alpha 11. The protein encoded by this gene belongs to the family of guanine nucleotide-binding proteins (G proteins), which function as modulators or transducers in various transmembrane signaling systems. G proteins are composed of 3 units: alpha, beta and gamma. This gene encodes one of the alpha subunits (subunit alpha-11). Mutations in this gene have been associated with hypocalciuric hypercalcemia type…
- **Diseases (Open Targets)**: familial hypoparathyroidism (0.754); familial hypocalciuric hypercalcemia 2 (0.736); autosomal dominant hypocalcemia (0.611); congenital hemangioma (0.494); uveal melanoma (0.469)
- **Europe PMC papers**: 4418
- **Why important**: GNA11 has one of the strongest network positions in the module and connects to GNAI3 and ATP1A1. It is the principal signaling gene represented in the primary plasma membrane complex term and recurs across multiple hu.MAP complexes with ANXA2 or GNAI3. Its established roles in G-protein-coupled receptor, adenylate-cyclase-modulating, and phospholipase-C-activating signaling, together with disease associations involving calcium regulation, make it a strong mechanistic bridge between membrane transport and signal transduction.
- **Conclusion**: Established evidence supports GNA11 as a signaling component embedded in membrane organization and ion-handling biology. A reasonable hypothesis is that GNA11-dependent signals help coordinate the module, but the co-abundance network does not establish direct GNA11-mediated regulation of the other genes.

#### SEC22B

- **Related proteins** (co-abundance neighbors): TMX1 (0.81), GNAI3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC22 homolog B, vesicle trafficking protein. The protein encoded by this gene is a member of the SEC22 family of vesicle trafficking proteins. It seems to complex with SNARE and it is thought to play a role in the ER-Golgi protein trafficking. This protein has strong similarity to Mus musculus and Cricetulus griseus proteins.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: inflammatory bowel disease (0.285); luminal A breast carcinoma (0.271); colitis (0.238); enteritis (0.238); Crohn disease (0.233)
- **Europe PMC papers**: 1006
- **Why important**: SEC22B is represented in the globally corrected melanosome and pigment-granule terms and in the corresponding STRING supplementary terms. Its established function in ER-to-Golgi and retrograde vesicle transport, vesicle fusion, and autophagy provides a mechanistic explanation for why membrane and organelle annotations co-occur. Its module links to TMX1 and GNAI3, connecting protein-folding and vesicle trafficking with membrane signaling. Although its disease and literature associations are less extensive than those of ANXA2 or TFRC, it is a particularly informative mechanistic gene because it explains the trafficking aspect of the module.
- **Conclusion**: Established evidence supports SEC22B as a vesicle-trafficking component that strengthens the interpretation of the module as a membrane and intracellular transport program. The hypothesis that SEC22B mediates a shared reproductive-tissue trafficking state remains untested, and its lack of direct STRING partners in this module limits claims of a known physical subcomplex.

## Module 1

**Tissue pair**: ovary and testis  
**Genes (6)**: SERPINA1, ACO1, SERPINC1, CAPN5, H6PD, GSN

### Function

No GO or KEGG term passed global correction, so the module does not support a formally established shared biological pathway. Its composition instead suggests a mixed module containing liver-associated plasma protease inhibitors together with intracellular metabolic, cytoskeletal, and proteolytic proteins. ACO1 is the network hub, connecting SERPINA1, CAPN5, GSN, and H6PD, while SERPINA1 and SERPINC1 form a linked inhibitor pair. The supplementary STRING disease association with nervous system disease (STRING DISEASES Nervous system disease; within-query FDR = 0.0437) should not be interpreted as globally significant functional enrichment. Overall, the strongest interpretation is a coordinated abundance pattern involving hepatocyte or plasma-derived proteins rather than a clearly defined ovary-testis cellular pathway.

**Cell composition.** The module is strongly biased toward liver and hepatocyte-associated expression, with additional intestine, heart muscle, and epithelial associations. Several members are secreted to blood or otherwise represented in the plasma proteome, especially SERPINA1, SERPINC1, and GSN. The HPA profile also includes immune-cell associations for some genes, although other members have low immune specificity or are not detected in immune cells. This mixture makes shared blood content, plasma protein carryover, or common non-gonadal cell populations plausible contributors to the ovary-testis co-abundance pattern. Protein detection is also discordant across the two tissues: some members are detected in ovary or testis, whereas others are not detected in either tissue. Thus, the module should not be assumed to represent a gonadal cell-intrinsic program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was detected among the module genes. Therefore, the co-abundance edges do not presently correspond to a known physical or functional interaction network in STRING. hu.MAP provides one known complex-level connection: SERPINA1 and SERPINC1 occur together in huMAP3_15040.1 (hu.MAP huMAP3_15040.1), but they are only a small subset of a very broad complex annotation. This supports a plausible relationship between the two circulating serpin proteins, while providing little evidence that the entire module is a single molecular complex. The absence of STRING links for ACO1, CAPN5, GSN, and H6PD means that their module co-abundance relationships remain observational rather than mechanistically established.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: DISEASES Nervous system disease (FDR = 0.0437, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINC1, SERPINA1; 2/64)

### Novelty

The module may be a novel tissue-pair co-abundance pattern, but it cannot be claimed as a newly discovered biological mechanism. Its lack of high-confidence STRING interactions and its limited hu.MAP overlap do not by themselves prove novelty. The absence of globally significant GO or KEGG enrichment, the liver and plasma bias, and the mixed intracellular and secreted composition instead suggest that the pattern may reflect shared sample composition, circulating proteins, or coordinated abundance without a previously annotated pathway. A stronger novelty claim would require replication, control for blood and cell-type composition, comparison with independent ovary and testis datasets, and testing whether the same gene relationships recur after such adjustment.

**Hypothesis.** Hypothesis: the module reflects a shared abundance axis driven partly by liver-derived or plasma-associated proteins entering or being measured in both gonadal tissue datasets, with ACO1-linked metabolic abundance varying alongside protease inhibitors, gelsolin, calpain, and H6PD. A possible biological component is coordination between extracellular protease inhibition and intracellular metabolic or cytoskeletal state, but this remains a hypothesis because the module has no STRING-supported interaction network and no globally significant GO or KEGG enrichment.

### Important genes

#### ACO1

- **Related proteins** (co-abundance neighbors): SERPINA1 (0.89), CAPN5 (0.89), GSN (0.87), H6PD (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in ovary, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aconitase 1. The protein encoded by this gene is a bifunctional, cytosolic protein that functions as an essential enzyme in the TCA cycle and interacts with mRNA to control the levels of iron inside cells. When cellular iron levels are high, this protein binds to a 4Fe-4S cluster and functions as an aconitase. Aconitases are iron-sulfur proteins that function to catalyze the conversion of citrate to isocitrate…
- **Diseases (Open Targets)**: smoking initiation (0.300); smoking behavior (0.277); ovarian neoplasm (0.276); attention deficit-hyperactivity disorder (0.261); substance abuse (0.261)
- **Europe PMC papers**: 3372
- **Why important**: ACO1 is the central network hub, connecting every other member except SERPINC1 through the observed co-abundance graph. Its established functions include citrate-to-isocitrate conversion in the TCA cycle and iron-responsive mRNA regulation. It is liver enhanced, detected in both tissues, and has a substantial literature base. Its hub position makes it the most informative candidate for testing whether the module reflects intracellular metabolism or a broader abundance factor.
- **Conclusion**: Established evidence supports ACO1 as a multifunctional metabolic and iron-responsive protein and as the module's central co-abundance connector. It is not established that ACO1 mechanistically regulates the other module genes; the observed links may instead reflect shared tissue, cell, or sample-composition effects.

#### SERPINA1

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.91), ACO1 (0.89); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family A member 1. The protein encoded by this gene is a serine protease inhibitor belonging to the serpin superfamily whose targets include elastase, plasmin, thrombin, trypsin, chymotrypsin, and plasminogen activator. This protein is produced in the liver, the bone marrow, by lymphocytic and monocytic cells in lymphoid tissue, and by the Paneth cells of the gut. Defects in this gene are associated with chronic obs…
- **Diseases (Open Targets)**: alpha 1-antitrypsin deficiency (0.768); chronic obstructive pulmonary disease (0.690); cirrhosis of liver (0.573); cholelithiasis (0.569); pulmonary emphysema (0.569)
- **Europe PMC papers**: 6526
- **Why important**: SERPINA1 is liver enriched, secreted to blood, associated with hepatocytes and several myeloid blood-cell populations, and connected to SERPINC1 and ACO1 in the module. It is a well-studied serine-protease inhibitor with established associations with alpha-one-antitrypsin deficiency, pulmonary disease, and chronic liver disease. It also participates in the huMAP complex annotation with SERPINC1 (hu.MAP huMAP3_15040.1).
- **Conclusion**: Established evidence supports SERPINA1 as a circulating protease inhibitor and a likely marker of liver or plasma contribution. Its co-abundance with intracellular proteins does not establish a direct intracellular mechanism, and its absence by immunohistochemistry in both listed gonadal tissues argues for caution when interpreting it as a local gonadal product.

#### SERPINC1

- **Related proteins** (co-abundance neighbors): SERPINA1 (0.91); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 is a liver-enriched, hepatocyte-associated plasma protein that inhibits thrombin and other activated coagulation proteases. It is linked to SERPINA1 in the module and shares their huMAP complex annotation (hu.MAP huMAP3_15040.1). Its established disease associations involve antithrombin deficiency and venous thrombotic disorders, making it a biologically informative representative of the coagulation and plasma-protease component.
- **Conclusion**: Established evidence supports SERPINC1 as an extracellular anticoagulant and as part of the plasma-associated component of the module. The module data support co-abundance with SERPINA1 but do not demonstrate that SERPINC1 drives the broader network or participates in an ovary-testis-specific mechanism.

#### H6PD

- **Related proteins** (co-abundance neighbors): ACO1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hexose-6-phosphate dehydrogenase/glucose 1-dehydrogenase. There are 2 forms of glucose-6-phosphate dehydrogenase. G form is X-linked and H form, encoded by this gene, is autosomally linked. This H form shows activity with other hexose-6-phosphates, especially galactose-6-phosphate, whereas the G form is specific for glucose-6-phosphate. Both forms are present in most tissues, but H form is not found in red cells. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: cortisone reductase deficiency (0.735); Abnormality of the skeletal system (0.473); obesity disorder (0.364); stroke disorder (0.325); alcohol drinking (0.324)
- **Europe PMC papers**: 3634
- **Why important**: H6PD is liver enhanced, detected in both tissues, and connected to the hub ACO1. It is an intracellular enzyme involved in hexose metabolism, the oxidative pentose-phosphate pathway, NADP-related metabolism, and responses to nutrient levels. Its established association with cortisone reductase deficiency provides disease relevance, while its intracellular localization contrasts with the secreted serpin members.
- **Conclusion**: Established evidence supports H6PD as a metabolic enzyme that could report intracellular nutrient or redox state. Its connection to ACO1 is a co-abundance observation rather than a known physical interaction, so a shared metabolic mechanism remains unproven.

#### GSN

- **Related proteins** (co-abundance neighbors): ACO1 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gelsolin. The protein encoded by this gene binds to the 'plus' ends of actin monomers and filaments to prevent monomer exchange. The encoded calcium-regulated protein functions in both assembly and disassembly of actin filaments. Defects in this gene are a cause of familial amyloidosis Finnish type (FAF). Multiple transcript variants encoding several different isoforms have been found for this gene. [provid…
- **Diseases (Open Targets)**: Finnish type amyloidosis (0.805); AL amyloidosis (0.463); neuropathy (0.418); cardiomyopathy (0.418); cutis laxa (0.417)
- **Europe PMC papers**: 5062
- **Why important**: GSN is connected to ACO1 and encodes a calcium-regulated actin-binding protein involved in actin filament assembly and disassembly. It is secreted to blood, associated with epithelial, fibroblast, endothelial, and eosinophil-related cell types, and has a substantial literature base. Its disease associations include Finnish-type amyloidosis, amyloidosis, neuropathy, cardiomyopathy, and cutis laxa.
- **Conclusion**: Established evidence supports GSN as a regulator of actin dynamics with both cellular and circulating forms. Its module association may reflect cytoskeletal state, vascular or epithelial material, or plasma contribution; a direct functional bridge from GSN to ACO1 or the serpins is not established.

#### CAPN5

- **Related proteins** (co-abundance neighbors): ACO1 (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calpain 5. Calpains are calcium-dependent cysteine proteases involved in signal transduction in a variety of cellular processes. A functional calpain protein consists of an invariant small subunit and 1 of a family of large subunits. CAPN5 is one of the large subunits. Unlike some of the calpains, CAPN5 and CAPN6 lack a calmodulin-like domain IV. Because of the significant similarity to Caenorhabditis elegan…
- **Diseases (Open Targets)**: proliferative vitreoretinopathy (0.646); CAPN5-related vitreoretinopathy (0.514); hereditary disease (0.415); inherited retinal dystrophy (0.186); occult macular dystrophy (0.118)
- **Europe PMC papers**: 501
- **Why important**: CAPN5 is connected to ACO1 and encodes a calcium-dependent cysteine protease involved in proteolysis and signal transduction. It is enriched in intestine and liver-related contexts, including enterocytes and epithelial populations, and is detected in testis but not ovary by the supplied immunohistochemistry summary. Its disease associations include CAPN5-related vitreoretinopathy and inherited retinal disorders, providing a clear disease-linked protease example within an otherwise mixed module.
- **Conclusion**: Established evidence supports CAPN5 as a tissue-associated calcium-dependent protease with disease relevance. Its testis detection and ACO1 connection make it useful for follow-up, but the current data do not show that CAPN5 links the gonadal tissues through a shared proteolytic mechanism.

## Module 2

**Tissue pair**: ovary and testis  
**Genes (8)**: ABCD3, ACO2, ASPH, ATL3, CANX, ITGB1, PITRM1, IARS2

### Function

No GO or KEGG term passed global correction, so the module has no statistically established pathway annotation from those analyses. Its co-abundance structure is centered on ITGB1 and connects cell adhesion and focal-adhesion biology with endoplasmic-reticulum organization and protein quality control, mitochondrial metabolism and protein processing, peroxisomal lipid handling, calcium-related biology, and mitochondrial translation. These links support a broad cellular-maintenance interpretation rather than a single demonstrated pathway. The spermatid-associated HPA pattern suggests that the module may also reflect biology shared by germ cells in ovary and testis. The functional annotations are established for individual genes, but their coordination in this module remains inferential.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, while the tissue-enhanced signals are distributed across liver, muscle, tongue, and adipose tissue rather than concentrated in one tissue. The module is also not strongly blood-cell enriched, because most genes have low immune-cell specificity and only ASPH shows immune-cell enhancement. HPA single-cell evidence includes early and late spermatids for several genes, with additional signals in enterocytes, adipocytes, neutrophil-lineage cells, and other cell types. Protein detection is broadly present in both ovary and testis, with some gene-specific exceptions. Thus, contamination by plasma proteins or a generic blood-cell module is not supported; shared germ-cell or broadly expressed cellular programs are more plausible explanations.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no STRING functional-enrichment result. No hu.MAP complex contains at least two module members. Therefore, the co-abundance edges are not corroborated here as established physical interactions or as membership in a known multiprotein complex. The network should be interpreted as a coordinated expression or abundance pattern, not as a validated molecular complex. Known individual functions still provide biological context: ITGB1 is a membrane adhesion receptor, CANX and ATL3 are associated with the endoplasmic reticulum, PITRM1 and IARS2 with mitochondria, ACO2 with the mitochondrial tricarboxylic-acid cycle, ABCD3 with peroxisomal lipid transport, and ASPH with calcium-related biology.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a new co-abundance observation because its specific gene combination has no supporting STRING interaction set or hu.MAP complex. However, absence from those resources alone does not establish novelty: co-abundance can arise from shared cell type, organelle state, tissue composition, or coordinated regulation without direct physical interaction. The strongest defensible conclusion is that the cross-tissue co-abundance pattern is not explained by a currently documented STRING or hu.MAP relationship in the supplied evidence, while its biological novelty remains unproven until it is replicated and compared with independent co-expression, proteomic, and tissue-composition datasets.

**Hypothesis.** Hypothesis: in germ-cell-rich regions shared by ovary and testis, this module may coordinate membrane adhesion and cellular organization with the proteostasis, organelle-communication, energy-production, lipid-handling, and translation demands of differentiating cells. ITGB1 may mark the central cell-interface component, while CANX and ATL3 reflect endoplasmic-reticulum organization, PITRM1 and IARS2 reflect mitochondrial protein processing and translation, and ACO2 and ABCD3 reflect energy and lipid metabolism. This is a mechanistic model rather than demonstrated causality; the absence of STRING and hu.MAP support means that the links may be indirect or driven by shared cell state.

### Important genes

#### ITGB1

- **Related proteins** (co-abundance neighbors): ATL3 (0.90), ACO2 (0.85), ASPH (0.85), PITRM1 (0.85), CANX (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 has the highest network degree and weighted strength in the module, making it the principal network hub. Its established location at the plasma membrane and focal-adhesion sites, together with integrin roles in cell adhesion, tissue repair, embryogenesis, immune response, and metastatic diffusion, gives it a strong connection to tissue organization. It also has extensive literature coverage and disease associations involving inflammatory and immune-related disorders.
- **Conclusion**: Established evidence supports ITGB1 as the central adhesion-associated marker of the module. It is plausible that its abundance tracks a shared cell-interface or tissue-organization state, but the module does not establish that ITGB1 regulates the other genes or that the observed links are physical.

#### CANX

- **Related proteins** (co-abundance neighbors): ABCD3 (0.87), ITGB1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in ovary, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is directly connected to ITGB1 and ABCD3 and is detected in both ovary and testis. Its established role as an endoplasmic-reticulum chaperone places it at the intersection of glycoprotein folding, assembly, retention of misfolded proteins, and ER-associated degradation. Its late-spermatid enrichment is particularly relevant to the shared reproductive-tissue context.
- **Conclusion**: Established evidence supports CANX as a proteostasis and ER component that could report biosynthetic demand in the shared module. A coordinated role with ITGB1 or ABCD3 is a hypothesis because neither STRING nor hu.MAP supports a known complex here.

#### PITRM1

- **Related proteins** (co-abundance neighbors): IARS2 (0.85), ITGB1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pitrilysin metallopeptidase 1. The protein encoded by this gene is an ATP-dependent metalloprotease that degrades post-cleavage mitochondrial transit peptides. The encoded protein binds zinc and can also degrade amyloid beta A4 protein, suggesting a possible role in Alzheimer's disease. [provided by RefSeq, Dec 2016].
- **Diseases (Open Targets)**: spinocerebellar ataxia, autosomal recessive 30 (0.721); mitochondrial DNA depletion syndrome 7 (hepatocerebral type) (0.333); thyroid gland disorder (0.252); skin disorder (0.244); sporadic amyotrophic lateral sclerosis (0.209)
- **Europe PMC papers**: 400
- **Why important**: PITRM1 is connected to ITGB1 and IARS2 and is detected in both tissues, with early- and late-spermatid enhancement. Its established mitochondrial metalloprotease activity links it to degradation of mitochondrial transit peptides and protein catabolism. Its disease associations include recessive spinocerebellar ataxia and mitochondrial DNA depletion syndrome.
- **Conclusion**: Established evidence supports PITRM1 as a mitochondrial protein-processing component of the module. Its co-abundance with a membrane receptor and a mitochondrial translation factor may indicate shared organelle or cell-state demands, but that mechanistic connection is not demonstrated.

#### ACO2

- **Related proteins** (co-abundance neighbors): ITGB1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aconitase 2. The protein encoded by this gene belongs to the aconitase/IPM isomerase family. It is an enzyme that catalyzes the interconversion of citrate to isocitrate via cis-aconitate in the second step of the TCA cycle. This protein is encoded in the nucleus and functions in the mitochondrion. It was found to be one of the mitochondrial matrix proteins that are preferentially degraded by the serine proteas…
- **Diseases (Open Targets)**: infantile cerebellar-retinal degeneration (0.814); optic atrophy 9 (0.693); autosomal dominant optic atrophy, classic form (0.619); optic atrophy (0.601); mitochondrial disease (0.505)
- **Europe PMC papers**: 3559
- **Why important**: ACO2 is connected to ITGB1 and is a core mitochondrial tricarboxylic-acid-cycle enzyme. It is detected in both ovary and testis and has tissue-enhanced expression in heart muscle, skeletal muscle, and tongue. Its extensive literature and disease associations with optic atrophy and mitochondrial disease make it an informative marker of oxidative metabolic state.
- **Conclusion**: Established evidence supports ACO2 as an indicator of mitochondrial energy metabolism within the module. Its presence suggests that metabolic activity may accompany the co-abundance pattern, but no evidence shows that ACO2 drives the adhesion, ER, or germ-cell-associated signals.

#### IARS2

- **Related proteins** (co-abundance neighbors): PITRM1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 2, mitochondrial. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Two forms of isoleucine-tRNA synthetase exist, a cytoplasmic form and a mitochondrial form. This gene encodes th…
- **Diseases (Open Targets)**: cataract-growth hormone deficiency-sensory neuropathy-sensorineural hearing loss-skeletal dysplasia syndrome (0.724); Leigh syndrome (0.563); hereditary disease (0.416); neurodegenerative disease (0.411); mitochondrial disease (0.374)
- **Europe PMC papers**: 411
- **Why important**: IARS2 is connected to PITRM1 and encodes the mitochondrial isoleucine-tRNA synthetase, an established component of mitochondrial translation and translational fidelity. It is detected in both ovary and testis and has disease associations including Leigh syndrome and a multisystem inherited syndrome. Its focused mitochondrial function complements the PITRM1 and ACO2 signals.
- **Conclusion**: Established evidence supports IARS2 as a mitochondrial translation marker in the module. Its co-abundance with PITRM1 is biologically coherent at the organelle level, but the supplied data do not establish a direct interaction or a reproductive-tissue-specific mechanism.

## Module 3

**Tissue pair**: ovary and testis  
**Genes (15)**: AFDN, CORO1C, DDX46, EIF3C, EZR, HSPH1, HSPA8, EIF4G1, NASP, NSUN2, SCFD1, SF3A1, SMC4, SRP68, SRP72

### Function

The best-supported interpretation is a broadly expressed RNA and protein-homeostasis module linking pre-mRNA processing, translation, endoplasmic-reticulum targeting, vesicle transport, cytoskeletal organization, and stress handling. The only globally corrected GO/KEGG evidence is (GO:MF protein-containing complex binding; q_global = 0.0322), protein-containing complex binding, involving AFDN, CORO1C, EIF3C, EZR, HSPA8, NASP, SCFD1, SRP68, and SRP72. This supports coordinated participation in multiprotein assemblies rather than a narrowly defined pathway. The supplementary STRING terms reinforce a ribonucleoprotein-complex component (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.0013)(STRING Component Ribonucleoprotein complex; within-query FDR = 0.0042) and protein-containing complex binding (STRING Function Protein-containing complex binding; within-query FDR = 0.0274), but they are not independent globally corrected evidence. Established gene functions indicate several connected processes: DDX46 and SF3A1 support spliceosome assembly and pre-mRNA splicing; EIF4G1 and EIF3C support translation initiation; SRP68 and SRP72 support cotranslational targeting of secretory and membrane proteins to the ER; HSPA8 and HSPH1 support chaperoning and protein-folding quality control; SCFD1 supports ER-to-Golgi and related vesicle transport; and EZR, AFDN, and CORO1C support membrane, junctional, and actin-associated organization. Thus, the module is most plausibly a coordination module for RNA maturation, translation, protein targeting, folding, and cell-structural organization, rather than evidence for one exclusive biological pathway.

**Cell composition.** The module is not dominated by secreted proteins, plasma proteins, or blood-cell-enriched genes. HPA identifies only one secreted gene, and most genes have low tissue specificity and low immune-cell specificity. Protein detection is present across the module in both ovary and testis, supporting that the signal is not simply explained by absence of protein in one tissue. Several genes show cell-type enhancement in epithelial, trophoblast, germ-cell, or other specialized populations, including late spermatids, differentiating spermatogonia, and early primary spermatocytes, while SMC4 is tissue-enhanced in lymphoid tissue and immune-cell enhanced in basophils. This pattern is compatible with a broadly expressed cellular machinery module that may be strengthened by shared proliferative, differentiating, epithelial, or germ-cell populations in the two tissues. The HPA evidence does not support interpreting it primarily as a blood-contamination module, although cellular composition remains a possible contributor to co-abundance.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF protein-containing complex binding | 0.0322 | AFDN, CORO1C, EIF3C, EZR, HSPA8, NASP, SCFD1, SRP68, SRP72 |

### STRING and hu.MAP

STRING provides a mixture of direct and functionally coherent known relationships. Strong direct links include DDX46-SF3A1, EIF3C-EIF4G1, EIF4G1-HSPA8, HSPA8-HSPH1, and SRP68-SRP72. These links independently support spliceosome-associated RNA processing, translation initiation, chaperone activity, and SRP function. The STRING supplementary ribonucleoprotein terms (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.0013)(STRING Component Ribonucleoprotein complex; within-query FDR = 0.0042) are consistent with the presence of SF3A1, DDX46, SRP68, SRP72, EIF3C, EIF4G1, and HSPA8, but remain supplementary evidence. hu.MAP supplies known complex context: EIF3C and EIF4G1 co-occur in translation-initiation complexes (hu.MAP huMAP3_13175.1)(hu.MAP huMAP3_11246.1); HSPA8 and HSPH1 co-occur in chaperone-related complexes (hu.MAP huMAP3_07919.1)(hu.MAP huMAP3_11049.1)(hu.MAP huMAP3_14723.1); and SF3A1 and DDX46 co-occur in spliceosome or snRNP-related complexes (hu.MAP huMAP3_04549.1)(hu.MAP huMAP3_06511.1)(hu.MAP huMAP3_08980.1). Several other module edges lack STRING or hu.MAP support, so the co-abundance network is not equivalent to a single pre-existing physical complex. Instead, it appears to connect several established molecular subsystems through a shared abundance program.

**STRING interactions (score >= 0.7)**: 5 of 105 gene pairs: DDX46–SF3A1 (0.999); EIF3C–EIF4G1 (0.99); EIF4G1–HSPA8 (0.97); HSPA8–HSPH1 (0.998); SRP68–SRP72 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Ribonucleoprotein complex (FDR = 0.0013, 7 genes); Component Ribonucleoprotein complex (FDR = 0.0042, 7 genes); Function Protein-containing complex binding (FDR = 0.0274, 9 genes); Keyword Acetylation (FDR = 0.0287, 15 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13175.1 (EIF4G1, EIF3C; 2/20); huMAP3_11246.1 (EIF4G1, EIF3C; 2/24); huMAP3_07919.1 (HSPA8, HSPH1; 2/27); huMAP3_11049.1 (HSPA8, HSPH1; 2/30); huMAP3_04549.1 (SF3A1, DDX46; 2/52); huMAP3_14723.1 (HSPA8, HSPH1; 2/52); huMAP3_06511.1 (SF3A1, DDX46; 2/79); huMAP3_08980.1 (SF3A1, DDX46; 2/97)

### Novelty

This module should not be called a wholly new molecular complex or a newly discovered pathway. Multiple components and relationships are already established by STRING and hu.MAP, especially the spliceosomal, translation-initiation, SRP, and chaperone-associated relationships. At the same time, the particular conserved co-abundance organization across ovary and testis is not directly established by the supplied interaction resources. The available web search produced no usable publication or database result specifically describing this exact module, but that absence is not proof of novelty. The defensible conclusion is that the module may represent a novel tissue-pair co-abundance configuration or regulatory coordination of known systems, while its constituent biology is largely established. Confirmation would require replication in independent ovary and testis datasets, preservation of the gene-level correlations, and testing against cell-composition and technical covariates.

**Hypothesis.** Hypothesis: shared ovarian and testicular cellular populations coordinate a program that couples RNA processing with productive protein synthesis and downstream protein handling. In this model, DDX46 and SF3A1 support maturation of transcripts, EIF4G1 and EIF3C promote their translation, SRP68 and SRP72 route a subset of nascent proteins to the ER, HSPA8 and HSPH1 protect and remodel newly synthesized proteins, and SCFD1, EZR, AFDN, and CORO1C connect trafficking and cytoskeletal or junctional organization. The co-abundance signal could therefore reflect a demand for synchronized RNA-to-protein flux during germ-cell differentiation, epithelial specialization, or other active cellular states shared between the tissues. This is a mechanistic model, not a demonstrated causal pathway; the data do not establish physical contact among all module members or tissue-specific regulation.

### Important genes

#### DDX46

- **Related proteins** (co-abundance neighbors): EIF4G1 (0.88), AFDN (0.87), NSUN2 (0.85), SF3A1 (0.85), HSPH1 (0.82); STRING partners: SF3A1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in ovary, testis
- **hu.MAP 3.0**: huMAP3_04549.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: DEAD-box helicase 46. This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribu…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); dengue disease (0.370); Hypercholesterolemia (0.203); lung adenocarcinoma (0.074); osteosarcoma (0.053)
- **Europe PMC papers**: 592
- **Why important**: DDX46 is among the most connected genes in the module and links EIF4G1, AFDN, NSUN2, SF3A1, and HSPH1 in the co-abundance graph. Its established DEAD-box helicase function and annotations in mRNA splicing and U2-type prespliceosome assembly make it a plausible bridge between RNA processing and the other module components. The DDX46-SF3A1 relationship is strongly supported by STRING, and DDX46 occurs in several hu.MAP spliceosome-related complexes (hu.MAP huMAP3_04549.1)(hu.MAP huMAP3_06511.1)(hu.MAP huMAP3_08980.1). Its literature base is substantial, but smaller than that of the best-studied translation and chaperone genes.
- **Conclusion**: Established evidence supports DDX46 as an RNA-processing and spliceosome-associated component with a central position in this module. It is a plausible upstream or bridging component, but the co-abundance data do not establish that DDX46 regulates the other genes in ovary or testis.

#### EIF4G1

- **Related proteins** (co-abundance neighbors): DDX46 (0.88), NSUN2 (0.85), SF3A1 (0.84), SRP68 (0.82), EZR (0.81); STRING partners: EIF3C (0.99), HSPA8 (0.97)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary, testis
- **hu.MAP 3.0**: huMAP3_13175.1, huMAP3_11246.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 is highly connected in the module and links DDX46, NSUN2, SF3A1, SRP68, and EZR. It is an established scaffold of the EIF4F translation-initiation complex and is annotated in cap-dependent translational initiation. EIF4G1 has direct STRING support with EIF3C and HSPA8 and occurs with EIF3C in hu.MAP translation-initiation complexes (hu.MAP huMAP3_13175.1)(hu.MAP huMAP3_11246.1). Its extensive literature and disease-association record make it a strong anchor for interpreting the module as a protein-production program.
- **Conclusion**: Established evidence supports EIF4G1 as a central translation-initiation component and a likely molecular bridge to chaperone and membrane-targeting functions. Its role as a tissue-pair-specific driver remains a hypothesis requiring perturbation or longitudinal expression evidence.

#### SRP68

- **Related proteins** (co-abundance neighbors): SRP72 (0.91), EIF4G1 (0.82), SCFD1 (0.82), EZR (0.80); STRING partners: SRP72 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal recognition particle 68. This gene encodes a subunit of the signal recognition particle (SRP). The SRP is a ribonucleoprotein complex that transports secreted and membrane proteins to the endoplasmic reticulum for processing. The complex includes a 7S RNA and six protein subunits. The encoded protein is the 68kDa component of the SRP, and forms a heterodimer with the 72kDa subunit that is required for SRP function. Altern…
- **Diseases (Open Targets)**: neurodegenerative disease (0.347); neutropenia, severe congenital, 10, autosomal recessive (0.333); COVID-19 (0.155); metabolic syndrome (0.074); atrial septal defect (0.073)
- **Europe PMC papers**: 440
- **Why important**: SRP68 is a relatively connected module member and links SRP72 with EIF4G1, SCFD1, and EZR. It forms the established SRP68-SRP72 heterodimer and participates in cotranslational targeting of secretory and membrane proteins to the ER. The SRP68-SRP72 interaction is strongly supported by STRING, and both genes contribute to the globally corrected complex-binding term (GO:MF protein-containing complex binding; q_global = 0.0322) and the supplementary STRING terms (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.0013)(STRING Component Ribonucleoprotein complex; within-query FDR = 0.0042)(STRING Function Protein-containing complex binding; within-query FDR = 0.0274)(STRING Keyword Acetylation; within-query FDR = 0.0287).
- **Conclusion**: Established evidence supports SRP68 as the module's clearest ER-targeting component and as a physical partner of SRP72. The connection from translation initiation to ER targeting is biologically plausible, but the network does not prove that this module specifically controls secretory-protein output in either tissue.

#### HSPA8

- **Related proteins** (co-abundance neighbors): SCFD1 (0.82); STRING partners: EIF4G1 (0.97), HSPH1 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Flagellar centriole, Annulus; IHC detected in ovary, testis
- **hu.MAP 3.0**: huMAP3_07919.1, huMAP3_11049.1, huMAP3_14723.1
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 8. This gene encodes a member of the heat shock protein 70 family, which contains both heat-inducible and constitutively expressed members. This protein belongs to the latter group, which are also referred to as heat-shock cognate proteins. It functions as a chaperone, and binds to nascent polypeptides to facilitate correct folding. It also functions as an ATPase in the disassembly of clathrin-coated…
- **Diseases (Open Targets)**: dengue disease (0.505); systemic lupus erythematosus (0.375); smoking initiation (0.199); Lennox-Gastaut syndrome (0.118); neoplasm (0.105)
- **Europe PMC papers**: 6937
- **Why important**: HSPA8 is a broadly expressed constitutive chaperone with established roles in nascent-polypeptide folding, unfolded-protein responses, and clathrin-coated-vesicle disassembly. It connects to SCFD1 in the co-abundance graph and has STRING relationships with EIF4G1 and HSPH1. HSPA8 and HSPH1 co-occur in multiple hu.MAP chaperone-related complexes (hu.MAP huMAP3_07919.1)(hu.MAP huMAP3_11049.1)(hu.MAP huMAP3_14723.1), and HSPA8 is represented in the ribonucleoprotein and complex-binding supplementary terms (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 0.0013)(STRING Component Ribonucleoprotein complex; within-query FDR = 0.0042)(STRING Function Protein-containing complex binding; within-query FDR = 0.0274). Its very large literature base makes it a strong interpretive anchor, although its broad expression reduces specificity.
- **Conclusion**: Established evidence supports HSPA8 as a protein-folding, trafficking, and proteostasis component that may connect translation to downstream protein handling. Because HSPA8 is broadly expressed and multifunctional, its presence does not by itself identify a specialized ovarian or testicular mechanism.

#### SF3A1

- **Related proteins** (co-abundance neighbors): DDX46 (0.85), EIF4G1 (0.84), NASP (0.83), EIF3C (0.81); STRING partners: DDX46 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in ovary, testis
- **hu.MAP 3.0**: huMAP3_04549.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 is highly connected and links DDX46, EIF4G1, NASP, and EIF3C. It is a defined component of the SF3A complex and U2 snRNP, with established roles in spliceosome assembly, splice-site recognition, and pre-mRNA splicing. The DDX46-SF3A1 STRING relationship and their shared hu.MAP spliceosome-related complexes (hu.MAP huMAP3_04549.1)(hu.MAP huMAP3_06511.1)(hu.MAP huMAP3_08980.1) provide direct support for a known RNA-processing subnetwork. Its literature volume is substantial and its HPA profile includes cell-type enhancement in late spermatids, which is relevant to the tissue pair.
- **Conclusion**: Established evidence supports SF3A1 as a core RNA-splicing component and a strong marker of the module's RNA-processing arm. Its cell-type pattern is compatible with germ-cell involvement, but does not prove that the module is specific to germ cells or that SF3A1 drives the shared tissue signal.

## Module 4

**Tissue pair**: ovary and testis  
**Genes (8)**: ATP5PB, ATP5F1A, ATP5F1B, ATP5F1C, MTX1, UQCRC1, UQCRC2, SCCPDH

### Function

The module is strongly consistent with mitochondrial oxidative phosphorylation and respiratory-chain energy production. The primary evidence is the globally corrected enrichment for respiratory-chain complex (GO:CC respiratory chain complex; q_global = 1.24e-05), oxidative phosphorylation (KEGG Oxidative phosphorylation - Homo sapiens (human); q_global = 1.98e-05) (GO:BP oxidative phosphorylation; q_global = 2.66e-05), proton-channel and rotational proton-transporting ATP-synthase activity (GO:MF proton channel activity; q_global = 3.68e-05) (GO:MF proton-transporting ATP synthase activity, rotational mechanism; q_global = 3.68e-05), the proton-transporting ATP-synthase complex (GO:CC proton-transporting ATP synthase complex; q_global = 7.1e-05), the mitochondrial inner membrane (GO:CC mitochondrial inner membrane; q_global = 0.000203), aerobic and cellular respiration (GO:BP aerobic respiration; q_global = 0.00102) (GO:BP cellular respiration; q_global = 0.00173), proton-motive-force-driven ATP synthesis (GO:BP proton motive force-driven mitochondrial ATP synthesis; q_global = 0.00339) (GO:BP proton motive force-driven ATP synthesis; q_global = 0.0047), and ATP biosynthesis (GO:BP ATP biosynthetic process; q_global = 0.00728). The pathway terms for neurodegenerative diseases and reactive oxygen species are best interpreted as pathway reuse by mitochondrial genes, not as evidence that this module specifically causes those diseases. The module appears to link ATP synthase components with respiratory complex III core components, with MTX1 and SCCPDH providing additional network connections.

**Cell composition.** This is not a plasma-protein, secreted-protein, or blood-cell module: HPA reports no secreted genes, and most genes have low immune-cell specificity. Protein detection is present across the module in testis and for most genes in ovary, supporting a genuine tissue-detectable signal rather than an absent protein program. The HPA pattern is nevertheless not ovary- or testis-exclusive. Several genes are enhanced in tongue, skeletal muscle, or heart muscle, and many are enriched in parietal, esophageal, trophoblast, or other specialized cell types. SCCPDH is enriched in spermatogenic cell groups and is the sole gene with immune-cell enrichment, specifically basophils. Thus, the shared module most plausibly reflects a broadly conserved mitochondrial energy program expressed in metabolically active cells, with possible contribution from shared cellular states or cell-type composition rather than a reproductive-organ-specific secreted signal.

**GO/KEGG enrichment**: 53 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC respiratory chain complex | 1.24e-05 | ATP5F1A, ATP5F1B, ATP5F1C, ATP5PB, UQCRC1, UQCRC2 |
| KEGG Oxidative phosphorylation - Homo sapiens (human) | 1.98e-05 | ATP5F1A, ATP5F1B, ATP5F1C, ATP5PB, UQCRC1, UQCRC2 |
| GO:BP oxidative phosphorylation | 2.66e-05 | ATP5F1A, ATP5F1B, ATP5F1C, ATP5PB, UQCRC1, UQCRC2 |
| GO:MF proton channel activity | 3.68e-05 | ATP5F1A, ATP5F1B, ATP5F1C, ATP5PB |
| GO:MF proton-transporting ATP synthase activity, rotational mechanism | 3.68e-05 | ATP5F1A, ATP5F1B, ATP5F1C, ATP5PB |
| KEGG Chemical carcinogenesis - reactive oxygen species - Homo sapiens (human) | 5.54e-05 | ATP5F1A, ATP5F1B, ATP5F1C, ATP5PB, UQCRC1, UQCRC2 |
| GO:CC proton-transporting ATP synthase complex | 7.1e-05 | ATP5F1A, ATP5F1B, ATP5F1C, ATP5PB |
| KEGG Thermogenesis - Homo sapiens (human) | 7.8e-05 | ATP5F1A, ATP5F1B, ATP5F1C, ATP5PB, UQCRC1, UQCRC2 |
| GO:CC transmembrane transporter complex | 8.73e-05 | ATP5F1A, ATP5F1B, ATP5F1C, ATP5PB, UQCRC1, UQCRC2 |
| KEGG Diabetic cardiomyopathy - Homo sapiens (human) | 9.69e-05 | ATP5F1A, ATP5F1B, ATP5F1C, ATP5PB, UQCRC1, UQCRC2 |
| GO:CC transporter complex | 0.000108 | ATP5F1A, ATP5F1B, ATP5F1C, ATP5PB, UQCRC1, UQCRC2 |
| GO:CC mitochondrial inner membrane | 0.000203 | ATP5F1A, ATP5F1B, ATP5F1C, ATP5PB, MTX1, UQCRC1, UQCRC2 |
| KEGG Parkinson disease - Homo sapiens (human) | 0.000265 | ATP5F1A, ATP5F1B, ATP5F1C, ATP5PB, UQCRC1, UQCRC2 |
| KEGG Prion disease - Homo sapiens (human) | 0.000265 | ATP5F1A, ATP5F1B, ATP5F1C, ATP5PB, UQCRC1, UQCRC2 |
| GO:MF monoatomic cation channel activity | 0.000288 | ATP5F1A, ATP5F1B, ATP5F1C, ATP5PB |

### STRING and hu.MAP

STRING provides extensive known physical or functional support among the mitochondrial genes. ATP5F1A, ATP5F1B, ATP5F1C, and ATP5PB form a highly supported ATP-synthase-associated group, while UQCRC1 and UQCRC2 form a highly supported complex-III-core pair and also connect strongly to the ATP-synthase genes. These relationships are summarized by the supplementary STRING enrichments for the inner mitochondrial membrane, electron transport, oxidative phosphorylation, ATP synthesis, and cristae formation (11 supplementary STRING terms; within-query FDR 1.36e-07–7.97e-06). The STRING results are supplementary rather than global enrichment evidence. hu.MAP independently places the ATP synthase genes together in several complexes (hu.MAP huMAP3_09307.1) (hu.MAP huMAP3_11095.1) (hu.MAP huMAP3_08716.1) (hu.MAP huMAP3_07476.1) (hu.MAP huMAP3_09775.1) (hu.MAP huMAP3_08750.1) (hu.MAP huMAP3_05994.1) (hu.MAP huMAP3_08393.1), places UQCRC1 and UQCRC2 together in multiple respiratory complexes (hu.MAP huMAP3_08546.1) (hu.MAP huMAP3_09600.1) (hu.MAP huMAP3_12621.1) (hu.MAP huMAP3_10623.1) (hu.MAP huMAP3_12457.1), and links selected ATP-synthase and complex-III members in additional complexes (hu.MAP huMAP3_07245.1) (hu.MAP huMAP3_06247.1). Together, the databases indicate that much of the module recapitulates established mitochondrial protein-complex biology rather than an arbitrary co-abundance association.

**STRING interactions (score >= 0.7)**: 15 of 28 gene pairs: ATP5F1A–ATP5F1B (0.999); ATP5F1A–ATP5F1C (0.999); ATP5F1A–ATP5PB (0.999); ATP5F1A–UQCRC1 (0.97); ATP5F1A–UQCRC2 (0.986); ATP5F1B–ATP5F1C (0.999); ATP5F1B–ATP5PB (0.999); ATP5F1B–UQCRC1 (0.969); ATP5F1B–UQCRC2 (0.942); ATP5F1C–ATP5PB (0.999); ATP5F1C–UQCRC1 (0.955); ATP5F1C–UQCRC2 (0.98); ATP5PB–UQCRC1 (0.903); ATP5PB–UQCRC2 (0.973); UQCRC1–UQCRC2 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Inner mitochondrial membrane protein complex (FDR = 1.36e-07, 7 genes); COMPARTMENTS Inner mitochondrial membrane protein complex (FDR = 1.89e-07, 7 genes); WikiPathways Electron transport chain: OXPHOS system in mitochondria (FDR = 9.94e-07, 6 genes); KEGG Oxidative phosphorylation (FDR = 1.34e-06, 6 genes); NetworkNeighborAL Respiratory electron transport, ATP synthesis by chemiosmotic coupling, and heat production by uncoupling proteins. (FDR = 2.23e-06, 6 genes); KEGG Thermogenesis (FDR = 2.65e-06, 6 genes); COMPARTMENTS Mitochondrial proton-transporting ATP synthase complex (FDR = 5.51e-06, 4 genes); NetworkNeighborAL Mitochondrial proton-transporting ATP synthase complex (FDR = 5.67e-06, 4 genes); RCTM Respiratory electron transport, ATP synthesis by chemiosmotic coupling, and heat production by uncoupling proteins. (FDR = 6.32e-06, 6 genes); RCTM Cristae formation (FDR = 6.32e-06, 5 genes); KEGG Parkinson disease (FDR = 6.59e-06, 6 genes); KEGG Huntington disease (FDR = 6.59e-06, 6 genes); KEGG Prion disease (FDR = 6.59e-06, 6 genes); KEGG Alzheimer disease (FDR = 7.5e-06, 6 genes); Component Mitochondrial proton-transporting ATP synthase complex (FDR = 7.97e-06, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09307.1 (ATP5F1B, ATP5PB, ATP5F1A, ATP5F1C; 4/35); huMAP3_11095.1 (ATP5F1B, ATP5PB, ATP5F1A, ATP5F1C; 4/45); huMAP3_08716.1 (ATP5F1B, ATP5PB, ATP5F1C; 3/15); huMAP3_07476.1 (ATP5F1B, ATP5PB, ATP5F1C; 3/18); huMAP3_09775.1 (ATP5F1B, ATP5PB, ATP5F1C; 3/21); huMAP3_07245.1 (UQCRC2, ATP5F1A; 2/4); huMAP3_08546.1 (UQCRC2, UQCRC1; 2/9); huMAP3_09600.1 (UQCRC2, UQCRC1; 2/9); huMAP3_08750.1 (ATP5F1B, ATP5F1A; 2/12); huMAP3_05994.1 (ATP5PB, ATP5F1C; 2/19); huMAP3_08393.1 (ATP5PB, ATP5F1C; 2/19); huMAP3_12621.1 (UQCRC2, UQCRC1; 2/22); huMAP3_10623.1 (UQCRC2, UQCRC1; 2/24); huMAP3_12457.1 (UQCRC2, UQCRC1; 2/31); huMAP3_06247.1 (UQCRC2, ATP5PB; 2/65)

### Novelty

The module is unlikely to be a newly discovered molecular complex: most of its central relationships are already represented in STRING and hu.MAP, and its globally significant annotations are canonical mitochondrial respiratory and ATP-synthase functions. The potentially less-established aspect is the specific conserved co-abundance configuration across ovary and testis, especially the placement of MTX1 and SCCPDH alongside the respiratory genes. However, absence of STRING or hu.MAP support for MTX1 or SCCPDH does not establish novelty, because database coverage, tissue context, and the distinction between co-abundance and physical interaction can all explain missing links. The defensible conclusion is that this is a biologically coherent tissue-shared co-abundance module with a potentially informative context-specific organization, not evidence for a wholly new pathway or complex.

**Hypothesis.** Hypothesis: in both ovary and testis, the module coordinates mitochondrial inner-membrane organization with respiratory electron transfer and ATP synthase activity, thereby supporting the high energetic demands of reproductive tissues and differentiating germ cells. In this model, UQCRC1 and UQCRC2 represent the complex-III respiratory segment, ATP5F1A, ATP5F1B, ATP5F1C, and ATP5PB represent the ATP-synthase segment, and MTX1 may help connect mitochondrial membrane organization to the co-abundance program. SCCPDH may mark a spermatogenic or lipid-metabolic context within the module, but its mechanistic participation in the respiratory machinery is unproven. This hypothesis should be tested with cell-type-resolved expression, mitochondrial functional assays, and perturbation of the candidate bridge genes rather than inferred from co-abundance alone.

### Important genes

#### ATP5F1A

- **Related proteins** (co-abundance neighbors): MTX1 (0.81), ATP5F1B (0.80); STRING partners: ATP5F1B (0.999), ATP5F1C (0.999), ATP5PB (0.999), UQCRC1 (0.97), UQCRC2 (0.986)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary, testis
- **hu.MAP 3.0**: huMAP3_09307.1, huMAP3_11095.1, huMAP3_07245.1, huMAP3_08750.1
- **Function (MyGene.info)**: ATP synthase F1 subunit alpha. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, using an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic po…
- **Diseases (Open Targets)**: mitochondrial complex V (ATP synthase) deficiency, nuclear type 4A (0.655); mitochondrial proton-transporting ATP synthase complex deficiency (0.648); mitochondrial complex V (ATP synthase) deficiency, nuclear type 4B (0.532); hereditary disease (0.394); Mitochondrial encephalopathy (0.371)
- **Europe PMC papers**: 822
- **Why important**: ATP5F1A is a central network member and is connected to the other ATP-synthase subunits and both complex-III core genes in STRING. It appears in every primary enrichment term (53 globally significant GO/KEGG terms, q_global 1.24e-05–0.0488; see the table), including the ATP-synthase, proton-motive-force, mitochondrial respiration, and ATP-biosynthesis terms. Its curated description identifies it as the ATP-synthase F1 alpha subunit, and disease evidence includes mitochondrial complex V deficiency and mitochondrial encephalopathy. Its literature volume is substantial, supporting strong prior biological interpretation.
- **Conclusion**: Established: ATP5F1A is a core catalytic-complex component and a robust representative of the module's oxidative-phosphorylation function. Hypothesis: its central co-abundance position may make it a useful readout of coordinated ATP-synthase activity in the shared reproductive-tissue program.

#### ATP5F1B

- **Related proteins** (co-abundance neighbors): ATP5F1A (0.80); STRING partners: ATP5F1A (0.999), ATP5F1C (0.999), ATP5PB (0.999), UQCRC1 (0.969), UQCRC2 (0.942)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary, testis
- **hu.MAP 3.0**: huMAP3_09307.1, huMAP3_11095.1, huMAP3_08716.1, huMAP3_07476.1, huMAP3_09775.1, huMAP3_08750.1
- **Function (MyGene.info)**: ATP synthase F1 subunit beta. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: hypermetabolism due to uncoupled mitochondrial oxidative phosphorylation 2 (0.499); hypertrophic cardiomyopathy (0.212); Alzheimer disease (0.177); hypertensive disorder (0.117); response to xenobiotic stimulus (0.117)
- **Europe PMC papers**: 735
- **Why important**: ATP5F1B is a member of the ATP-synthase group with very strong STRING support to ATP5F1A, ATP5F1C, and ATP5PB, and it occurs in multiple hu.MAP ATP-synthase complexes (hu.MAP huMAP3_09307.1) (hu.MAP huMAP3_11095.1) (hu.MAP huMAP3_08716.1) (hu.MAP huMAP3_07476.1) (hu.MAP huMAP3_09775.1) (hu.MAP huMAP3_08750.1). It contributes to nearly the complete primary enrichment pattern (53 globally significant GO/KEGG terms, q_global 1.24e-05–0.0488; see the table) and is annotated for ATP biosynthesis and proton-motive-force-driven mitochondrial ATP synthesis. Its disease associations include uncoupled oxidative-phosphorylation hypermetabolism and hypertrophic cardiomyopathy, while its literature volume is substantial.
- **Conclusion**: Established: ATP5F1B is a canonical ATP-synthase F1 beta subunit and a major functional anchor of the module. Hypothesis: variation in its abundance could report altered coupling between respiratory proton gradients and ATP production in ovary and testis.

#### UQCRC1

- **Related proteins** (co-abundance neighbors): UQCRC2 (0.90); STRING partners: ATP5F1A (0.97), ATP5F1B (0.969), ATP5F1C (0.955), ATP5PB (0.903), UQCRC2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary, testis
- **hu.MAP 3.0**: huMAP3_08546.1, huMAP3_09600.1, huMAP3_12621.1, huMAP3_10623.1, huMAP3_12457.1
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase core protein 1. Enables ubiquitin protein ligase binding activity. Predicted to be involved in oxidative phosphorylation. Predicted to act upstream of or within mitochondrial electron transport, ubiquinol to cytochrome c. Located in mitochondrion. Implicated in Alzheimer's disease. Biomarker of Alzheimer's disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: parkinsonism with polyneuropathy (0.642); neurodegenerative disease (0.569); Parkinson disease (0.521); Alzheimer disease (0.519); lysosomal storage disease (0.498)
- **Europe PMC papers**: 1860
- **Why important**: UQCRC1 is the complex-III-side representative of the module and forms a strongly supported STRING pair with UQCRC2 while connecting to the ATP-synthase genes. It participates in the respiratory-chain, oxidative-phosphorylation, aerobic-respiration, and mitochondrial terms (29 globally significant GO/KEGG terms, q_global 1.24e-05–0.0482; see the table). Its curated function is mitochondrial electron transport from ubiquinol to cytochrome c, and disease associations include Parkinson disease, Alzheimer disease, and other neurodegenerative disease categories. Its literature volume is substantial.
- **Conclusion**: Established: UQCRC1 supports the interpretation that the module spans respiratory electron transfer rather than representing ATP synthase alone. Hypothesis: coordinated abundance of UQCRC1 with ATP-synthase genes may reflect coupling between complex III activity and downstream ATP generation.

#### MTX1

- **Related proteins** (co-abundance neighbors): ATP5F1C (0.88), SCCPDH (0.83), ATP5F1A (0.81), ATP5PB (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: metaxin 1. Predicted to be involved in mitochondrion organization. Part of MIB complex and SAM complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: gastric carcinoma (0.516); gastric cancer (0.444); neurodegenerative disease (0.412); gout (0.406); polyp of large intestine (0.342)
- **Europe PMC papers**: 484
- **Why important**: MTX1 has the strongest network connectivity in the supplied module and connects ATP-synthase members with SCCPDH. It occurs in the globally significant mitochondrial inner-membrane, organelle-envelope, membrane-complex, and mitochondrion terms (8 globally significant GO/KEGG terms, q_global 0.000203–0.0291; see the table), and STRING supplementary evidence places it in inner-membrane and cristae-related groups (STRING Component Inner mitochondrial membrane protein complex; within-query FDR = 1.36e-07) (STRING COMPARTMENTS Inner mitochondrial membrane protein complex; within-query FDR = 1.89e-07) (STRING RCTM Cristae formation; within-query FDR = 6.32e-06). Its curated annotations concern mitochondrial organization, protein insertion into the mitochondrial outer membrane, and mitochondrial translocase or SAM-complex assembly. It has disease associations involving gastric cancer, neurodegenerative disease, gout, and intestinal polyps, together with a substantial literature record.
- **Conclusion**: Established: MTX1 is a mitochondrial organization gene and the main network-position candidate for connecting membrane organization with the respiratory module. Hypothesis: MTX1 may help explain why this co-abundance program is preserved across tissues by coordinating mitochondrial architecture with energetic capacity; direct functional coupling to the other module genes remains unproven.

#### SCCPDH

- **Related proteins** (co-abundance neighbors): MTX1 (0.83), UQCRC2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Immune cell enriched; location Vesicles; IHC detected in ovary, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: saccharopine dehydrogenase (putative). Predicted to enable oxidoreductase activity. Predicted to be involved in glycolipid biosynthetic process. Located in lipid droplet and midbody. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: liver disorder (0.271); stomach disorder (0.256); iridocyclitis (0.245); ovarian neoplasm (0.240); nephritis (0.237)
- **Europe PMC papers**: 755
- **Why important**: SCCPDH is unusual in the module because it has no reported STRING partners or hu.MAP complex assignment, yet it connects in the co-abundance graph to MTX1 and UQCRC2. It contributes to the globally significant mitochondrion term (GO:CC mitochondrion; q_global = 0.0291) but not to the more specific respiratory enrichment terms. Its curated annotation is tentative, involving predicted oxidoreductase activity and glycolipid biosynthesis, with localization to lipid droplets and the midbody. HPA places it in early and late spermatogenic cell groups and also reports basophil enrichment. Its disease evidence and literature volume are more limited than those of the core respiratory genes.
- **Conclusion**: Established: SCCPDH is a tissue-detectable, comparatively less-characterized member associated with the module through co-abundance rather than established protein-complex evidence. Hypothesis: it may mark a lipid-metabolic or germ-cell-specific state that is coordinated with mitochondrial energy demand, but it should not currently be described as a respiratory-chain component.

## Module 5

**Tissue pair**: ovary and testis  
**Genes (15)**: ATXN2L, CAPRIN1, DDX5, MATR3, MYH10, PRPF31, UPF1, SF3B3, LARS1, CCT5, CCT3, CCT7, CCT8, SNRNP200, EFTUD2

### Function

The strongest interpretation is a conserved intracellular RNA and protein-handling module with two tightly connected components. The CCT chaperonin component, comprising CCT3, CCT5, CCT7 and CCT8, is supported directly by the globally corrected chaperonin and protein-folding terms (GO:CC chaperonin-containing T-complex; q_global = 4.48e-05), (GO:CC protein folding chaperone complex; q_global = 0.00295), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.00781) and (GO:MF protein folding chaperone; q_global = 0.0401). The second component is spliceosomal and RNA-processing machinery, supported by the globally corrected spliceosome and RNA-splicing terms (GO:CC spliceosomal complex; q_global = 0.00042), (KEGG Spliceosome - Homo sapiens (human); q_global = 0.00358), (GO:BP RNA splicing, via transesterification reactions; q_global = 0.00375), (GO:BP mRNA splicing, via spliceosome; q_global = 0.00375), (GO:CC U2-type precatalytic spliceosome; q_global = 0.00423), (GO:CC precatalytic spliceosome; q_global = 0.00423), (GO:CC catalytic step 2 spliceosome; q_global = 0.0102), (GO:BP RNA splicing; q_global = 0.0118), (GO:CC U2-type spliceosomal complex; q_global = 0.0129), (GO:CC spliceosomal snRNP complex; q_global = 0.0129), (GO:CC small nuclear ribonucleoprotein complex; q_global = 0.0199) and (GO:BP mRNA processing; q_global = 0.0234). The broad globally corrected RNA-binding, mRNA-processing, nucleic-acid metabolic and gene-expression terms (GO:MF RNA binding; q_global = 0.000358), (GO:BP nucleic acid metabolic process; q_global = 0.000558), (GO:BP mRNA metabolic process; q_global = 0.00179), (GO:MF nucleic acid binding; q_global = 0.00222), (GO:BP gene expression; q_global = 0.0195) and (GO:BP macromolecule biosynthetic process; q_global = 0.0372) indicate coordinated RNA handling rather than a single narrowly specialized pathway. Telomere, Cajal-body, fertilization and sperm-egg-recognition annotations are also globally corrected (19 globally significant GO/KEGG terms, q_global 4.48e-05–0.000373; see the table), (5 globally significant GO/KEGG terms, q_global 0.000741–0.00129; see the table), (GO:BP telomere organization; q_global = 0.00161), (GO:BP telomere maintenance via telomere lengthening; q_global = 0.00197) (GO:BP regulation of chromosome organization; q_global = 0.002) and (GO:BP cell-cell recognition; q_global = 0.00295), but most of these signals are carried by the same CCT subunits; they should therefore be treated as annotations of the CCT-associated machinery, not as proof that this entire module is a tissue-specific fertilization or telomere program. Overall, the module most plausibly reflects coordinated chaperone-assisted protein folding, spliceosome function, RNA processing and RNA quality control.

**Cell composition.** This is not a plasma-protein, secreted-protein or blood-cell module. HPA reports no secreted genes, low immune-cell specificity for nearly all genes, and no recurrent enriched blood-cell category. Most genes have low tissue specificity and are detected in both ovary and testis, which is consistent with broadly expressed intracellular housekeeping or core gene-expression machinery. There is nevertheless a germ-cell signal: CCT7 is enhanced in early and late spermatids, CCT5 in late primary spermatocytes, CCT8 in oocytes, CAPRIN1 in early spermatids and late primary spermatocytes, and PRPF31 in early primary spermatocytes. Thus, the shared module is unlikely to be explained by circulating blood contamination, but its abundance may partly reflect shared germ-cell or reproductive-cell composition alongside broadly expressed cellular machinery. The apparent tissue sharing should not by itself be interpreted as evidence for a uniquely ovary-testis-specific biochemical pathway.

**GO/KEGG enrichment**: 81 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chaperonin-containing T-complex | 4.48e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 4.48e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 4.48e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 4.48e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 4.48e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 4.48e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 4.48e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 4.48e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomere maintenance via telomerase | 0.00016 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 0.00016 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to Cajal body | 0.00016 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 0.00016 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 0.00016 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 0.00016 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomere maintenance | 0.000163 | CCT3, CCT5, CCT7, CCT8, UPF1 |

### STRING and hu.MAP

STRING strongly confirms the internal CCT relationships among CCT3, CCT5, CCT7 and CCT8, and independently confirms the spliceosomal relationships among EFTUD2, PRPF31, SF3B3 and SNRNP200. DDX5 is connected to MATR3 and is also a network bridge to both the CCT and spliceosomal portions; CAPRIN1 and UPF1 provide a smaller RNA-regulatory connection. These observations agree with the supplementary STRING enrichments for the spliceosomal complex, CCT chaperonin, RNA binding and ATP-dependent activity (15 supplementary STRING terms; within-query FDR 6.66e-05–0.00038). hu.MAP independently places the CCT genes together in several complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_01951.1), the spliceosomal genes together in multiple complexes (hu.MAP huMAP3_08980.1), (hu.MAP huMAP3_00960.1), (hu.MAP huMAP3_07622.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), (hu.MAP huMAP3_09945.1) and (hu.MAP huMAP3_06511.1), and links DDX5, CAPRIN1, MATR3 and UPF1 in RNA-associated complexes (hu.MAP huMAP3_05711.1) (hu.MAP huMAP3_07909.1) (hu.MAP huMAP3_00960.1) (hu.MAP huMAP3_10207.1) (hu.MAP huMAP3_09754.1) (hu.MAP huMAP3_07622.1) (hu.MAP huMAP3_10631.1) (hu.MAP huMAP3_11111.1) (hu.MAP huMAP3_06975.1) (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_10625.1). Known STRING and hu.MAP relationships explain a substantial part of the module, especially the CCT and spliceosome clusters. The co-abundance module therefore has strong support from established physical or functional machinery, while the cross-cluster co-abundance links should be interpreted as coordination rather than as proof of direct binding.

**STRING interactions (score >= 0.7)**: 14 of 105 gene pairs: CAPRIN1–UPF1 (0.72); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999); DDX5–MATR3 (0.894); EFTUD2–PRPF31 (0.999); EFTUD2–SF3B3 (0.999); EFTUD2–SNRNP200 (0.999); PRPF31–SF3B3 (0.997); PRPF31–SNRNP200 (0.999); SF3B3–SNRNP200 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Spliceosomal complex (FDR = 6.66e-05, 6 genes); Pfam TCP-1/cpn60 chaperonin family (FDR = 8.86e-05, 4 genes); Function RNA binding (FDR = 0.00012, 12 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 0.00013, 4 genes); Component Spliceosomal complex (FDR = 0.00018, 6 genes); Component Chaperonin-containing T-complex (FDR = 0.00018, 4 genes); Function ATP hydrolysis activity (FDR = 0.00036, 7 genes); Function Organic cyclic compound binding (FDR = 0.00036, 15 genes); Function ATP-dependent activity (FDR = 0.00036, 8 genes); Function Heterocyclic compound binding (FDR = 0.00036, 15 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 0.00038, 4 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 0.00038, 4 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 0.00038, 4 genes); InterPro GroEL-like apical domain superfamily (FDR = 0.00038, 4 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 0.00038, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_08980.1 (SNRNP200, EFTUD2, SF3B3, PRPF31; 4/97); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_05711.1 (DDX5, CAPRIN1; 2/8); huMAP3_07909.1 (DDX5, CAPRIN1; 2/8); huMAP3_00960.1 (SNRNP200, EFTUD2; 2/8); huMAP3_10207.1 (CAPRIN1, ATXN2L; 2/9); huMAP3_09754.1 (DDX5, CAPRIN1; 2/9); huMAP3_07622.1 (SNRNP200, EFTUD2; 2/9); huMAP3_10631.1 (DDX5, CAPRIN1; 2/28); huMAP3_11111.1 (DDX5, CAPRIN1; 2/29); huMAP3_06975.1 (MATR3, UPF1; 2/31); huMAP3_08501.1 (SNRNP200, EFTUD2; 2/47); huMAP3_09504.1 (SNRNP200, EFTUD2; 2/51); huMAP3_10625.1 (MATR3, UPF1; 2/57); huMAP3_09945.1 (SNRNP200, EFTUD2; 2/61); huMAP3_06511.1 (SF3B3, PRPF31; 2/79)

### Novelty

The module is unlikely to represent a wholly new molecular complex: its principal substructures are already well established in STRING and hu.MAP, including the CCT chaperonin and spliceosomal assemblies. A potentially novel aspect is the conserved co-abundance of these established RNA-processing and protein-folding systems across ovary and testis, together with their reproductive-cell expression pattern. However, the fact sheet does not compare this module with previously published tissue co-abundance modules, so a claim that the module is a new biological discovery would be premature. Absence of selected relationships, such as the lack of STRING or hu.MAP support for some peripheral genes, does not establish novelty; it may reflect indirect regulation, incomplete databases or co-abundance without physical interaction.

**Hypothesis.** Hypothesis: in ovary and testis cells, especially germ-line cells, elevated demand for proteostasis and extensive transcript remodeling causes coordinated activity of the CCT chaperonin, spliceosome, RNA helicases and RNA-surveillance or RNA-granule machinery. The CCT component could support folding and stabilization of proteins needed for RNA metabolism and reproductive-cell development, while DDX5, EFTUD2, SF3B3, PRPF31 and SNRNP200 could coordinate spliceosome assembly and remodeling. UPF1, MATR3, CAPRIN1 and ATXN2L could connect processing with RNA export, surveillance, translation control or stress-granule behavior. The telomere and Cajal-body annotations suggest a possible connection to nuclear RNA organization, but the current evidence does not demonstrate that telomere maintenance is the causal driver of the module. This mechanism should be tested by cell-type-resolved expression, perturbation of the CCT or spliceosomal components, and measurement of splicing, RNA surveillance, protein-folding capacity and telomere-related phenotypes.

### Important genes

#### DDX5

- **Related proteins** (co-abundance neighbors): CCT5 (0.89), CCT3 (0.88), CCT7 (0.83), EFTUD2 (0.82), SF3B3 (0.82), PRPF31 (0.81), ATXN2L (0.80); STRING partners: MATR3 (0.894)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in ovary, testis
- **hu.MAP 3.0**: huMAP3_05711.1, huMAP3_07909.1, huMAP3_09754.1, huMAP3_10631.1, huMAP3_11111.1
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 has the strongest bridging position in the module and connects CCT-associated genes with spliceosomal genes and ATXN2L. It is annotated as a DEAD-box RNA helicase, adaptor, transcriptional coregulator and regulator of splicing and small noncoding-RNA processing. It participates in many globally corrected RNA-binding, spliceosome, mRNA-processing and gene-expression terms (GO:MF RNA binding; q_global = 0.000358), (GO:CC spliceosomal complex; q_global = 0.00042), (GO:BP mRNA metabolic process; q_global = 0.00179), (4 globally significant GO/KEGG terms, q_global 0.00358–0.00375; see the table), (GO:BP RNA splicing; q_global = 0.0118), (GO:BP gene expression; q_global = 0.0195) and (GO:BP mRNA processing; q_global = 0.0234). Its established STRING relationship with MATR3 and extensive literature support make it a strong integrative marker, although literature volume alone does not prove that it drives this module.
- **Conclusion**: Established: DDX5 is a central RNA-processing connector with broad functional and disease-literature support. Hypothesis: DDX5 may coordinate the chaperone and spliceosome arms in reproductive cells. This regulatory-bridge interpretation requires perturbational testing.

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT3 (0.94), CCT8 (0.92), DDX5 (0.89), CCT7 (0.87); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in ovary, testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is a central member of the CCT subnetwork, has strong links to the other CCT subunits and DDX5, and occurs in the globally corrected chaperonin, protein-folding, Cajal-body, telomere and reproductive-process terms (20 globally significant GO/KEGG terms, q_global 4.48e-05–0.000373; see the table), (5 globally significant GO/KEGG terms, q_global 0.000741–0.00129; see the table), (GO:BP telomere maintenance via telomere lengthening; q_global = 0.00197), (GO:CC protein folding chaperone complex; q_global = 0.00295), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.00781), (GO:BP single fertilization; q_global = 0.0102) and (GO:MF protein folding chaperone; q_global = 0.0401). STRING gives direct support for its CCT relationships, and hu.MAP places it in multiple CCT-containing complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_01951.1). HPA detects it in ovary and testis and enhances it in late primary spermatocytes. Its disease associations include hereditary sensory and autonomic neuropathy with spastic paraplegia and neurodegenerative disease.
- **Conclusion**: Established: CCT5 is a core chaperonin subunit and a well-supported structural anchor of the module. Hypothesis: its reproductive-cell enrichment may indicate increased chaperone demand during germ-cell differentiation, but the module does not establish a CCT5-specific reproductive function.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): MATR3 (0.87), SNRNP200 (0.84), DDX5 (0.82), SF3B3 (0.82); STRING partners: PRPF31 (0.999), SF3B3 (0.999), SNRNP200 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary, testis
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 is a spliceosomal GTPase and has direct STRING relationships with PRPF31, SF3B3 and SNRNP200. It is represented in the globally corrected spliceosome, U2 spliceosome, tri-snRNP, mRNA-splicing and mRNA-processing terms (GO:CC spliceosomal complex; q_global = 0.00042), (4 globally significant GO/KEGG terms, q_global 0.00358–0.00375; see the table), (GO:CC U2-type precatalytic spliceosome; q_global = 0.00423), (GO:CC precatalytic spliceosome; q_global = 0.00423), (GO:CC catalytic step 2 spliceosome; q_global = 0.0102), (GO:BP RNA splicing; q_global = 0.0118), (GO:CC U2-type spliceosomal complex; q_global = 0.0129), (GO:CC spliceosomal snRNP complex; q_global = 0.0129), (GO:CC small nuclear ribonucleoprotein complex; q_global = 0.0199) and (GO:BP mRNA processing; q_global = 0.0234). It also appears in several hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1), (hu.MAP huMAP3_00960.1), (hu.MAP huMAP3_07622.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1) and (hu.MAP huMAP3_09945.1). Its established disease association with mandibulofacial dysostosis with microcephaly provides evidence that disruption of this core process can have organism-level consequences.
- **Conclusion**: Established: EFTUD2 is a core spliceosome-associated component and a major anchor of the RNA-processing arm. Hypothesis: coordinated EFTUD2 abundance may help tune spliceosome capacity in ovary and testis, but tissue-specific substrate selection is not demonstrated here.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.84), MYH10 (0.82); STRING partners: EFTUD2 (0.999), PRPF31 (0.999), SF3B3 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is a U5 snRNP-associated RNA helicase and is embedded in the strongest spliceosomal STRING relationships with EFTUD2, PRPF31 and SF3B3. It contributes to the globally corrected spliceosome, RNA-splicing, ATP-dependent and mRNA-processing terms (GO:CC spliceosomal complex; q_global = 0.00042), (5 globally significant GO/KEGG terms, q_global 0.00354–0.00375; see the table), (GO:CC U2-type precatalytic spliceosome; q_global = 0.00423) (GO:CC precatalytic spliceosome; q_global = 0.00423) (GO:MF ATP hydrolysis activity; q_global = 0.00428), (GO:CC catalytic step 2 spliceosome; q_global = 0.0102), (5 globally significant GO/KEGG terms, q_global 0.0118–0.0129; see the table) and (GO:BP mRNA processing; q_global = 0.0234). It is also present in many hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1), (hu.MAP huMAP3_00960.1), (hu.MAP huMAP3_07622.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1) and (hu.MAP huMAP3_09945.1). Its disease associations with retinitis pigmentosa and inherited retinal dystrophy, together with its detection in testis but not ovary by HPA, make it informative for interpreting both conserved machinery and possible tissue-composition differences.
- **Conclusion**: Established: SNRNP200 is a conserved spliceosomal helicase and a well-supported component of the module's RNA-processing core. Hypothesis: its asymmetric HPA detection may reflect sample or cell-state differences rather than absence of the conserved module from ovary.

#### UPF1

- **Related proteins** (co-abundance neighbors): MATR3 (0.84), SF3B3 (0.81); STRING partners: CAPRIN1 (0.72)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in ovary, testis
- **hu.MAP 3.0**: huMAP3_06975.1, huMAP3_10625.1
- **Function (MyGene.info)**: UPF1 RNA helicase and ATPase. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons.…
- **Diseases (Open Targets)**: Intellectual disability (0.437); Global developmental delay (0.426); High anterior hairline (0.425); Frontal bossing (0.425); Hypertelorism (0.425)
- **Europe PMC papers**: 4252
- **Why important**: UPF1 links RNA processing and surveillance to the rest of the module through MATR3 and SF3B3, and STRING also supports a CAPRIN1 relationship. It appears in globally corrected RNA-binding, spliceosome, RNA-localization, mRNA-processing, gene-expression and telomere-maintenance terms (GO:BP regulation of telomere maintenance; q_global = 0.000163), (GO:MF RNA binding; q_global = 0.000358), (GO:CC spliceosomal complex; q_global = 0.00042), (GO:BP nucleic acid metabolic process; q_global = 0.000558), (4 globally significant GO/KEGG terms, q_global 0.00129–0.00179; see the table), (GO:BP RNA splicing, via transesterification reactions; q_global = 0.00375) (GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 0.00375) (GO:BP mRNA splicing, via spliceosome; q_global = 0.00375), (GO:BP RNA localization; q_global = 0.00375), (GO:BP RNA splicing; q_global = 0.0118), (GO:BP gene expression; q_global = 0.0195) and (GO:BP mRNA processing; q_global = 0.0234). Its annotated role in nonsense-mediated decay, mRNA export and translational termination gives the module a quality-control dimension beyond splicing. It has substantial literature support and disease associations involving intellectual disability and global developmental delay.
- **Conclusion**: Established: UPF1 is an RNA helicase and ATPase involved in mRNA surveillance and export, and it connects the module to post-splicing quality control. Hypothesis: UPF1 may couple spliceosome output to RNA-surveillance demand in reproductive cells; the present co-abundance data do not establish directionality.

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT5 (0.92), CCT7 (0.85), CCT3 (0.84), LARS1 (0.81); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in ovary, testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is a core CCT subunit with strong STRING links to CCT3, CCT5 and CCT7 and membership in several hu.MAP CCT-containing complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). It contributes to the globally corrected chaperonin, protein-folding, Cajal-body, telomere and fertilization-related terms (14 globally significant GO/KEGG terms, q_global 4.48e-05–0.00016; see the table), (4 globally significant GO/KEGG terms, q_global 0.000373–0.000373; see the table), (5 globally significant GO/KEGG terms, q_global 0.000741–0.00129; see the table), (GO:BP telomere maintenance via telomere lengthening; q_global = 0.00197), (GO:CC protein folding chaperone complex; q_global = 0.00295), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.00781), (GO:BP single fertilization; q_global = 0.0102) and (GO:MF protein folding chaperone; q_global = 0.0401). HPA enhances it in oocytes and detects it in both ovary and testis. Its established function in folding newly synthesized proteins, including actin and tubulin, makes it a biologically interpretable link between proteostasis and reproductive-cell biology.
- **Conclusion**: Established: CCT8 is a core chaperonin component with reproductive-cell expression support and extensive complex-level confirmation. Hypothesis: CCT8 may contribute to the shared oocyte and spermatogenic proteostasis program, but the module cannot distinguish that possibility from general cellular demand for CCT activity.

## Module 6

**Tissue pair**: ovary and testis  
**Genes (6)**: KRT10, KRT14, KRT9, KRT2, KRT1, KRT5

### Function

The module is a coherent epithelial intermediate-filament and keratinization program. Every module gene contributes to the globally corrected keratin-filament and intermediate-filament terms (6 globally significant GO/KEGG terms, q_global 1.8e-10–1.31e-07; see the table), while the same genes support cornified-envelope formation, skin and epidermis development, keratinocyte differentiation, epithelial differentiation, and cytoskeletal organization (KEGG Cornified envelope formation - Homo sapiens (human); q_global = 4.58e-07) (GO:BP skin development; q_global = 6.55e-07) (GO:BP epidermis development; q_global = 1.07e-06), (GO:BP keratinocyte differentiation; q_global = 4.65e-06) (GO:BP epidermal cell differentiation; q_global = 1.27e-05) (GO:BP epithelial cell differentiation; q_global = 5.31e-05), (5 globally significant GO/KEGG terms, q_global 0.000402–0.00139; see the table), (5 globally significant GO/KEGG terms, q_global 0.00667–0.0248; see the table). The cadherin-signaling and estrogen-signaling annotations (KEGG Cadherin signaling - Homo sapiens (human); q_global = 4.12e-06), (KEGG Estrogen signaling pathway - Homo sapiens (human); q_global = 0.0232) should be interpreted cautiously because they are pathway annotations containing these keratins, not evidence that the module directly performs hormone signaling. The strongest biological interpretation is structural reinforcement and differentiation of stratified epithelial cells, rather than a gonad-specific function.

**Cell composition.** This is not a plasma-protein or secreted-protein module and it is not primarily a blood-cell module. HPA assigns most genes to skin and to suprabasal or basal keratinocytes, with additional enrichment in epithelial tissues such as cervix, esophagus, and vagina. One gene is annotated as secreted in other tissues, but the module is overwhelmingly composed of intracellular structural keratins. Some genes show immune-cell enhancement or low immune-cell specificity, but others are not detected in immune cells, so the collective pattern does not support a blood-cell origin. Protein staining is not detected for any module gene in ovary or testis, despite the co-abundance module being shared by those tissues. This makes epithelial-cell admixture, tissue-surface contamination, or a low-level epithelial transcript signal more plausible explanations than a resident ovary-and-testis keratin program. The HPA pattern also argues against treating the module as evidence for a specialized gonadal function.

**GO/KEGG enrichment**: 30 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC keratin filament | 1.8e-10 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament organization | 1.01e-09 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament-based process | 5.77e-09 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament cytoskeleton organization | 5.77e-09 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:CC intermediate filament | 5.85e-08 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:CC intermediate filament cytoskeleton | 1.31e-07 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| KEGG Cornified envelope formation - Homo sapiens (human) | 4.58e-07 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP skin development | 6.55e-07 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP epidermis development | 1.07e-06 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:MF structural constituent of skin epidermis | 1.26e-06 | KRT1, KRT10, KRT2, KRT5 |
| KEGG Cadherin signaling - Homo sapiens (human) | 4.12e-06 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:BP keratinocyte differentiation | 4.65e-06 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| GO:BP epidermal cell differentiation | 1.27e-05 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| GO:BP epithelial cell differentiation | 5.31e-05 | KRT1, KRT10, KRT14, KRT2, KRT5, KRT9 |
| GO:CC cornified envelope | 8.7e-05 | KRT1, KRT10, KRT14, KRT2 |

### STRING and hu.MAP

STRING strongly supports the interpretation as a keratin network. The high-confidence relationships include the canonical KRT1-KRT10 pair, KRT1-KRT2, KRT1-KRT5, KRT10-KRT2, KRT10-KRT5, KRT14-KRT5, and KRT2-KRT5 interactions. STRING functional annotations independently converge on keratin, keratin filament, intermediate filament, cornified-envelope formation, and intermediate-filament domains (8 supplementary STRING terms; within-query FDR 7.89e-11–1.25e-09). KRT9 has no listed STRING partner, although it shares the module's keratin annotations and is connected in the co-abundance graph. Thus, the network contains a well-supported core of known keratin relationships plus a co-abundance association involving KRT9. No hu.MAP complex contains at least two module members, so the module is not directly corroborated as a hu.MAP-defined multiprotein complex. The absence of a hu.MAP complex does not contradict a filamentous structural program, because intermediate-filament assemblies may be context-dependent, dynamic, or incompletely represented in complex catalogs.

**STRING interactions (score >= 0.7)**: 7 of 15 gene pairs: KRT1–KRT10 (0.999); KRT1–KRT2 (0.956); KRT1–KRT5 (0.923); KRT10–KRT2 (0.904); KRT10–KRT5 (0.793); KRT14–KRT5 (0.999); KRT2–KRT5 (0.871)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Keratin (FDR = 7.89e-11, 6 genes); Component Keratin filament (FDR = 9.23e-11, 6 genes); COMPARTMENTS Keratin filament (FDR = 9.69e-11, 6 genes); SMART Intermediate filament protein (FDR = 2.17e-10, 6 genes); Keyword Intermediate filament (FDR = 3.06e-10, 6 genes); RCTM Formation of the cornified envelope (FDR = 8.35e-10, 6 genes); InterPro Intermediate filament protein, conserved site (FDR = 1.25e-09, 6 genes); InterPro Intermediate filament, rod domain (FDR = 1.25e-09, 6 genes); PMID (2025) Mass spectrometric detection of keratins in tear fluid. (FDR = 3.36e-08, 6 genes); PMID (2023) Key Factors in the Complex and Coordinated Network of Skin Keratinization: Their Significance and Involvement in Common Skin Conditions. (FDR = 3.36e-08, 6 genes); PMID (2022) A metatranscriptomic approach to explore longitudinal tissue specimens from non-healing diabetes related foot ulcers. (FDR = 3.36e-08, 6 genes); PMID (2022) Palmoplantar Keratoderma: A Molecular Genetic Analysis of Family Cases. (FDR = 3.36e-08, 6 genes); PMID (2021) Keratin Biomaterials in Skin Wound Healing, an Old Player in Modern Medicine: A Mini Review. (FDR = 3.36e-08, 6 genes); PMID (2019) Keratin 9 L164P mutation in a Chinese pedigree with epidermolytic palmoplantar keratoderma, cytokeratin analysis, and literature review. (FDR = 3.36e-08, 6 genes); PMID (2019) Proteome Profiling of the Exhaled Breath Condensate after Long-Term Spaceflights. (FDR = 3.36e-08, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The biological function is not a new discovery: the genes, GO/KEGG terms, STRING annotations, disease links, and literature all identify a canonical epithelial keratin and cornification program. The module may nevertheless represent a new tissue-pair-specific observation if this exact co-abundance pattern in ovary and testis has not previously been reported. Its novelty would therefore concern the cross-tissue co-abundance context, not the molecular identity or function of the genes. The known STRING relationships support biological plausibility, while the lack of a hu.MAP complex provides no positive evidence for novelty. Because all module proteins are undetected by HPA in ovary and testis, the apparent cross-tissue signal should be validated with independent transcriptomic, proteomic, histological, and cell-composition analyses before being called a gonadal mechanism.

**Hypothesis.** Hypothesis: the shared module reflects coordinated detection of stratified epithelial or epithelial-like material in both tissue datasets, possibly through epithelial-cell admixture, surface contamination, or a common keratin-positive cell population, rather than a conserved ovary-and-testis-specific pathway. Within that signal, KRT5-KRT14 may represent a basal epithelial structural state, while KRT1, KRT10, KRT2, and KRT9 represent more differentiated or terminal keratin programs. The co-abundance of these states could arise from mixed epithelial differentiation states or from correlated changes in epithelial content. This hypothesis predicts that the module should track epithelial-cell markers and sample-level epithelial content, and that spatial validation should localize the signal to keratin-positive cells rather than to gonadal parenchymal cells.

### Important genes

#### KRT5

- **Related proteins** (co-abundance neighbors): KRT14 (0.96), KRT10 (0.93), KRT2 (0.87); STRING partners: KRT1 (0.923), KRT10 (0.793), KRT14 (0.999), KRT2 (0.871)
- **HPA**: Group enriched; Group enriched; blood Immune cell enriched; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 5. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the basal layer of the epidermis with family member KRT14. Mutations in t…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 2C, localized (0.768); epidermolysis bullosa simplex 2A, generalized severe (0.761); epidermolysis bullosa simplex 2B, generalized intermediate (0.761); epidermolysis bullosa simplex 2F, with mottled pigmentation (0.729); Dowling-Degos disease 1 (0.697)
- **Europe PMC papers**: 7044
- **Why important**: KRT5 is a central module node with connections to KRT14, KRT1, KRT10, and KRT2. It is a type II keratin expressed in basal epidermal cells and pairs with KRT14 to form an epithelial cytoskeleton. It contributes to the globally corrected intermediate-filament, epidermal-differentiation, keratinization, and structural-cytoskeleton evidence (9 globally significant GO/KEGG terms, q_global 1.8e-10–1.07e-06; see the table), (GO:BP keratinocyte differentiation; q_global = 4.65e-06) (GO:BP epidermal cell differentiation; q_global = 1.27e-05) (GO:BP epithelial cell differentiation; q_global = 5.31e-05), (5 globally significant GO/KEGG terms, q_global 0.000402–0.00139; see the table), (5 globally significant GO/KEGG terms, q_global 0.00667–0.0248; see the table). Its HPA profile emphasizes basal and suprabasal epithelial cells and several epithelial tissues. Its disease associations and extensive literature connect it to epidermolysis bullosa simplex and related epithelial fragility phenotypes.
- **Conclusion**: Established evidence supports KRT5 as a basal epithelial structural anchor and a strong indicator of keratin-positive cellular content. Its presence does not establish a gonadal-specific role. The interpretation that it marks epithelial admixture in this module is a hypothesis supported by its HPA pattern and network position.

#### KRT14

- **Related proteins** (co-abundance neighbors): KRT5 (0.96), KRT2 (0.95), KRT10 (0.94), KRT1 (0.92); STRING partners: KRT5 (0.999)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 14. This gene encodes a member of the keratin family, the most diverse group of intermediate filaments. This gene product, a type I keratin, is usually found as a heterotetramer with two keratin 5 molecules, a type II keratin. Together they form the cytoskeleton of epithelial cells. Mutations in the genes for these keratins are associated with epidermolysis bullosa simplex. At least one pseudogene has…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 1A, generalized severe (0.823); epidermolysis bullosa simplex 1C, localized (0.818); epidermolysis bullosa simplex 1B, generalized intermediate (0.802); epidermolysis bullosa simplex 1D, generalized, intermediate or severe, autosomal recessive (0.759); Naegeli-Franceschetti-Jadassohn syndrome (0.759)
- **Europe PMC papers**: 6348
- **Why important**: KRT14 has a highly connected position and its strongest listed STRING relationship is with KRT5, matching the established basal keratin pair. It contributes to the globally corrected keratin-filament, epithelial-development, keratinocyte-differentiation, and cytoskeletal terms (9 globally significant GO/KEGG terms, q_global 1.8e-10–1.07e-06; see the table), (GO:BP keratinocyte differentiation; q_global = 4.65e-06) (GO:BP epidermal cell differentiation; q_global = 1.27e-05) (GO:BP epithelial cell differentiation; q_global = 5.31e-05), (GO:CC polymeric cytoskeletal fiber; q_global = 0.000402), (GO:MF structural molecule activity; q_global = 0.000646) (GO:BP epithelium development; q_global = 0.000646) (GO:BP supramolecular fiber organization; q_global = 0.00139), (5 globally significant GO/KEGG terms, q_global 0.00667–0.0248; see the table). HPA places it in basal, suprabasal, and esophageal basal keratinocytes, and it is not detected in immune cells. Its disease associations include multiple forms of epidermolysis bullosa simplex and Naegeli-Franceschetti-Jadassohn syndrome, with a substantial literature base.
- **Conclusion**: Established evidence identifies KRT14 as a basal epithelial intermediate-filament component and a biologically credible core of the module. In this tissue-pair context, its most defensible interpretation is as evidence of keratin-positive epithelial material, while any direct role in ovary or testis remains unestablished.

#### KRT1

- **Related proteins** (co-abundance neighbors): KRT10 (0.95), KRT2 (0.94), KRT14 (0.92), KRT9 (0.88); STRING partners: KRT10 (0.999), KRT2 (0.956), KRT5 (0.923)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 is among the most connected genes in the module and links to KRT10, KRT2, KRT14, and KRT9. It participates in nearly all of the core globally corrected keratin, intermediate-filament, cornified-envelope, epidermal-development, and structural-function terms (9 globally significant GO/KEGG terms, q_global 1.8e-10–1.07e-06; see the table), (4 globally significant GO/KEGG terms, q_global 4.12e-06–5.31e-05; see the table), (9 globally significant GO/KEGG terms, q_global 0.000402–0.00443; see the table), (4 globally significant GO/KEGG terms, q_global 0.00902–0.0248; see the table). HPA associates it with skin and suprabasal keratinocytes. It has extensive literature and disease associations involving epidermolytic ichthyosis and palmoplantar keratoderma-related phenotypes.
- **Conclusion**: Established evidence supports KRT1 as a central differentiated epithelial cytoskeletal component and a major driver of the module's annotation profile. Its high connectivity makes it useful as a module marker, but neither its network position nor its estrogen-pathway annotation demonstrates a gonadal mechanism.

#### KRT10

- **Related proteins** (co-abundance neighbors): KRT1 (0.95), KRT14 (0.94), KRT5 (0.93), KRT2 (0.91), KRT9 (0.86); STRING partners: KRT1 (0.999), KRT2 (0.904), KRT5 (0.793)
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 10. This gene encodes a member of the type I (acidic) cytokeratin family, which belongs to the superfamily of intermediate filament (IF) proteins. Keratins are heteropolymeric structural proteins which form the intermediate filament. These filaments, along with actin microfilaments and microtubules, compose the cytoskeleton of epithelial cells. Mutations in this gene are associated with epidermolytic …
- **Diseases (Open Targets)**: epidermolytic hyperkeratosis 2A, autosomal dominant (0.787); epidermolytic ichthyosis (0.772); congenital reticular ichthyosiform erythroderma (0.727); ichthyosis, annular epidermolytic 1 (0.647); annular epidermolytic ichthyosis (0.642)
- **Europe PMC papers**: 2736
- **Why important**: KRT10 has the strongest module connectivity and links to the principal keratin core, including KRT1, KRT2, KRT5, KRT14, and KRT9. It appears in nearly every globally corrected term, including keratin filaments, cornified envelope, epidermal and keratinocyte differentiation, epithelial development, and structural cytoskeleton (9 globally significant GO/KEGG terms, q_global 1.8e-10–1.07e-06; see the table), (6 globally significant GO/KEGG terms, q_global 4.12e-06–0.000402; see the table), (8 globally significant GO/KEGG terms, q_global 0.000646–0.00443; see the table), (4 globally significant GO/KEGG terms, q_global 0.00902–0.0248; see the table). HPA specifically associates it with skin and suprabasal keratinocytes. It has extensive literature and disease associations involving epidermolytic hyperkeratosis, epidermolytic ichthyosis, and related disorders.
- **Conclusion**: Established evidence supports KRT10 as a highly informative marker of differentiated keratinizing epithelium. Its centrality makes it important for interpreting the module, but its absence from HPA protein detection in ovary and testis favors a contamination or cell-composition explanation over a gonad-specific function.

#### KRT2

- **Related proteins** (co-abundance neighbors): KRT14 (0.95), KRT1 (0.94), KRT10 (0.91), KRT5 (0.87); STRING partners: KRT1 (0.956), KRT10 (0.904), KRT5 (0.871)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location Intermediate filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 2. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is expressed largely in the upper spinous layer of epidermal keratinocytes and mutations in this gene …
- **Diseases (Open Targets)**: superficial epidermolytic ichthyosis (0.815); exfoliative ichthyosis (0.358); Palmoplantar hyperkeratosis (0.267); hereditary disease (0.193); Vertigo (0.145)
- **Europe PMC papers**: 7459
- **Why important**: KRT2 is a highly connected module member associated with KRT14, KRT1, KRT10, and KRT5. It contributes to the globally corrected keratin-filament, keratinization, epidermal-development, epithelial-differentiation, and cytoskeletal terms (9 globally significant GO/KEGG terms, q_global 1.8e-10–1.07e-06; see the table), (10 globally significant GO/KEGG terms, q_global 4.12e-06–0.00139; see the table), (GO:BP peptide cross-linking; q_global = 0.00443), (5 globally significant GO/KEGG terms, q_global 0.00667–0.0248; see the table). HPA places it in suprabasal keratinocytes. Its annotations describe roles in epidermal development, keratinization, keratinocyte activation, and proliferation, while disease associations include superficial and exfoliative ichthyosis and palmoplantar hyperkeratosis.
- **Conclusion**: Established evidence supports KRT2 as a differentiated suprabasal keratin and as part of the module's coherent structural program. Its co-abundance with basal and suprabasal keratins may reflect mixed epithelial states; that mixed-state interpretation is a hypothesis rather than a demonstrated process in ovary or testis.

#### KRT9

- **Related proteins** (co-abundance neighbors): KRT1 (0.88), KRT10 (0.86); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 9. This gene encodes the type I keratin 9, an intermediate filament chain expressed only in the terminally differentiated epidermis of palms and soles. Mutations in this gene cause epidermolytic palmoplantar keratoderma. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: epidermolytic palmoplantar keratoderma, 1 (0.828); palmoplantar keratoderma, epidermolytic (0.682); Localized epidermolytic hyperkeratosis (0.511); Palmoplantar hyperkeratosis (0.456); Palmoplantar keratoderma (0.438)
- **Europe PMC papers**: 773
- **Why important**: KRT9 is less connected than the other selected genes in the module and has no listed STRING partner, making it a useful contrast between co-abundance evidence and established protein-interaction evidence. It nevertheless participates in the globally corrected keratin-filament, epithelial-development, skin-development, cytoskeletal, and Staphylococcus aureus infection annotations (6 globally significant GO/KEGG terms, q_global 1.8e-10–1.31e-07; see the table), (GO:BP skin development; q_global = 6.55e-07), (GO:BP epidermis development; q_global = 1.07e-06), (KEGG Cadherin signaling - Homo sapiens (human); q_global = 4.12e-06), (GO:BP epithelial cell differentiation; q_global = 5.31e-05), (GO:CC polymeric cytoskeletal fiber; q_global = 0.000402), (6 globally significant GO/KEGG terms, q_global 0.000646–0.00387; see the table), (6 globally significant GO/KEGG terms, q_global 0.00443–0.0248; see the table). Its known biology is specialized terminal epidermal expression in palms and soles, and its disease associations include epidermolytic palmoplantar keratoderma. HPA instead reports tissue enrichment in lymphoid tissue and enhancement across several cell types, including basal keratinocytes.
- **Conclusion**: Established evidence supports KRT9 as a keratin-family member with a specialized epithelial differentiation association, but its lack of listed STRING partners and unusual HPA pattern make it less secure as a physical-network hub. Its inclusion may capture a shared epithelial or keratinized-cell signal, whereas any specific role in gonadal tissue is unestablished.

## Module 7

**Tissue pair**: ovary and testis  
**Genes (11)**: NME3, NDUFAF4, DDOST, RAB10, RAB18, RAB21, SFXN1, SYNGR2, STOM, STX7, VDAC2

### Function

The strongest interpretation is a membrane-trafficking and organelle-boundary module. The primary evidence is the globally corrected enrichment for organelle membrane (GO:CC organelle membrane; q_global = 0.00522), bounding membrane of organelle (GO:CC bounding membrane of organelle; q_global = 0.0129), cytoplasmic vesicle membrane (GO:CC cytoplasmic vesicle membrane; q_global = 0.0373), and vesicle membrane (GO:CC vesicle membrane; q_global = 0.0397). The genes include several established regulators or components of intracellular transport: RAB21, RAB18, and RAB10 are Rab-family GTPases involved in membrane traffic; STX7 is a vesicle-fusion syntaxin; and SYNGR2 is a membrane protein associated with regulated exocytosis and membrane traffic. The module also contains organelle and metabolic components, including the mitochondrial proteins SFXN1, VDAC2, and NDUFAF4, the endoplasmic-reticulum oligosaccharyl-transferase component DDOST, and the vesicle or plasma-membrane protein STOM. Thus, the evidence supports a broad intracellular membrane and vesicle-organization function, with possible coupling to mitochondrial metabolism, protein maturation, and membrane transport. The GO evidence does not establish one specific cargo, tissue-specific pathway, or direct physical complex for the entire module.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module: the HPA summary identifies only one secreted gene, while most proteins are intracellular or membrane-associated. Most genes have low tissue specificity, so the shared ovary-testis signal is unlikely to represent a narrowly ovary- or testis-exclusive program. At the single-cell level, many genes are cell-type enhanced, with recurring signals in esophageal epithelial cells and neutrophil-related populations, and additional signals in oocytes, spermatids, and other cell types. Several genes also show blood-cell associations, while STOM is associated with red-blood-cell biology and membrane vesicles. These patterns raise the possibility that the module partly reflects shared cell states, vascular or immune-cell contributions, or broadly conserved membrane biology in the samples rather than a reproductive-tissue-specific mechanism. HPA protein detection is present for most genes in both tissues, but absence of detection for selected genes and the lack of ovary detection for some members argue against treating the module as a uniformly expressed tissue program.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC organelle membrane | 0.00522 | DDOST, NDUFAF4, NME3, RAB10, RAB18, RAB21, SFXN1, STOM, STX7, SYNGR2, VDAC2 |
| GO:CC bounding membrane of organelle | 0.0129 | DDOST, NME3, RAB10, RAB18, RAB21, STOM, STX7, SYNGR2, VDAC2 |
| GO:CC cytoplasmic vesicle membrane | 0.0373 | DDOST, RAB10, RAB18, RAB21, STOM, STX7, SYNGR2 |
| GO:CC vesicle membrane | 0.0397 | DDOST, RAB10, RAB18, RAB21, STOM, STX7, SYNGR2 |

### STRING and hu.MAP

STRING provides no high-confidence pairwise interactions among the module genes at the stated threshold. Therefore, the co-abundance edges should not be interpreted as established direct protein-protein interactions. STRING functional annotations independently converge on organelle membranes, cytoplasmic and secretory vesicles, secretory granules, Rab GTPases, and membrane keywords (STRING COMPARTMENTS Organelle membrane; within-query FDR = 0.0022) through (STRING Component Synaptic vesicle; within-query FDR = 0.0433), but these are supplementary annotations and do not replace the globally corrected GO evidence. hu.MAP identifies STOM and VDAC2 together in two broad membrane complexes (hu.MAP huMAP3_09822.1) and (hu.MAP huMAP3_10725.1). This is evidence of a limited known complex-context connection, but the complexes contain many additional proteins and only those two module members, so it does not demonstrate that the full module is one physical complex. Overall, the network is better viewed as a coordinated abundance signature spanning membrane trafficking and organelle biology than as a validated molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 55 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Organelle membrane (FDR = 0.0022, 10 genes); COMPARTMENTS Cytoplasmic vesicle membrane (FDR = 0.0103, 6 genes); COMPARTMENTS Secretory vesicle (FDR = 0.0103, 7 genes); Component Cytoplasmic vesicle membrane (FDR = 0.016, 7 genes); Component Organelle membrane (FDR = 0.016, 10 genes); Component Bounding membrane of organelle (FDR = 0.016, 8 genes); Component Secretory vesicle (FDR = 0.016, 7 genes); COMPARTMENTS Cytoplasmic vesicle (FDR = 0.0174, 8 genes); COMPARTMENTS Bounding membrane of organelle (FDR = 0.0174, 7 genes); SMART Rab subfamily of small GTPases (FDR = 0.0209, 3 genes); Component Secretory granule membrane (FDR = 0.0211, 4 genes); Keyword Lipoprotein (FDR = 0.0238, 5 genes); Keyword Membrane (FDR = 0.0238, 10 genes); COMPARTMENTS Secretory granule (FDR = 0.0244, 6 genes); Component Synaptic vesicle (FDR = 0.0433, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09822.1 (STOM, VDAC2; 2/28); huMAP3_10725.1 (STOM, VDAC2; 2/59)

### Novelty

The module is potentially novel as a conserved ovary-testis co-abundance pattern, but novelty cannot be claimed as discovery of a new membrane-trafficking pathway. Its component functions are largely established, and STRING's lack of pairwise links does not prove that the relationships are novel because database coverage, context dependence, and the co-abundance nature of the network all limit that inference. The hu.MAP evidence also shows that at least part of the membership overlaps known membrane-complex contexts. The defensible claim is that the specific cross-tissue co-abundance organization and its combination of Rab, vesicle, mitochondrial, endoplasmic-reticulum, and membrane components may be a new systems-level observation requiring independent replication, tissue deconvolution, and experimental testing.

**Hypothesis.** Hypothesis: the module represents a conserved organelle-membrane trafficking state shared by ovary and testis, in which Rab-dependent endosomal and secretory-vesicle traffic is coordinated with lysosomal fusion, endoplasmic-reticulum protein processing, and mitochondrial metabolite handling. RAB21, RAB18, and RAB10 could provide complementary trafficking control, while STX7 and SYNGR2 could support vesicle fusion or regulated membrane traffic. SFXN1, VDAC2, and NDUFAF4 could couple this membrane state to mitochondrial amino-acid transport, outer-membrane exchange, and respiratory-complex assembly. This remains a hypothesis: the co-abundance network, GO enrichment, and database annotations do not establish directionality, direct binding, cargo identity, or a reproductive-specific mechanism. A competing explanation is shared abundance of common epithelial, immune, blood-derived, or other cell populations across the tissue samples.

### Important genes

#### RAB21

- **Related proteins** (co-abundance neighbors): VDAC2 (0.85), RAB10 (0.84), SFXN1 (0.84), RAB18 (0.84), NDUFAF4 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in ovary, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB21, member RAS oncogene family. This gene belongs to the Rab family of monomeric GTPases, which are involved in the control of cellular membrane traffic. The encoded protein plays a role in the targeted trafficking of integrins via its association with integrin alpha tails. As a consequence, the encoded protein is involved in the regulation of cell adhesion and migration. Expression of this gene is associated with a poor prognos…
- **Diseases (Open Targets)**: neurodegenerative disease (0.469); small intestine neuroendocrine neoplasm (0.095); neoplasm (0.085); posterior cortical atrophy (0.074); nonpapillary renal cell carcinoma (0.065)
- **Europe PMC papers**: 999
- **Why important**: RAB21 has the strongest network centrality in the module and connects the trafficking cluster with SFXN1, NDUFAF4, and VDAC2. It is an established Rab-family regulator of intracellular transport, integrin trafficking, cell adhesion, migration, receptor-mediated endocytosis, and exocytosis. It appears in every primary GO term (GO:CC organelle membrane; q_global = 0.00522) through (GO:CC vesicle membrane; q_global = 0.0397) and many supplementary membrane and Rab annotations (STRING COMPARTMENTS Organelle membrane; within-query FDR = 0.0022), (STRING COMPARTMENTS Cytoplasmic vesicle membrane; within-query FDR = 0.0103), (STRING Component Cytoplasmic vesicle membrane; within-query FDR = 0.016) through (STRING SMART Rab subfamily of small GTPases; within-query FDR = 0.0209), and (STRING Keyword Lipoprotein; within-query FDR = 0.0238) through (STRING Keyword Membrane; within-query FDR = 0.0238). Its literature base is substantial, but STRING and hu.MAP do not provide a recorded direct interaction with the other module members.
- **Conclusion**: Established: RAB21 is a strong candidate organizer of the module's membrane-trafficking signal. Hypothesis: its central co-abundance position may mark coordination between endosomal trafficking and mitochondrial or organelle-membrane processes in the shared ovary-testis state.

#### RAB18

- **Related proteins** (co-abundance neighbors): RAB21 (0.84), STOM (0.82), DDOST (0.81), RAB10 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in ovary, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB18, member RAS oncogene family. The protein encoded by this gene is a member of a family of Ras-related small GTPases that regulate membrane trafficking in organelles and transport vesicles. Knockdown studies is zebrafish suggest that this protein may have a role in eye and brain development. Mutations in this gene are associated with Warburg micro syndrome type 3. Alternatively spliced transcript variants have been found for th…
- **Diseases (Open Targets)**: Warburg micro syndrome (0.815); neurodegenerative disease (0.496); cerebral atherosclerosis (0.275); malunion fracture (0.239); adolescent idiopathic scoliosis (0.229)
- **Europe PMC papers**: 2168
- **Why important**: RAB18 is a highly connected module member linked to RAB21, RAB10, STOM, and DDOST. It is an established small GTPase involved in organelle and vesicle trafficking, lipid droplet organization, and sterol homeostasis, and it is associated with Warburg micro syndrome. It contributes to all primary GO terms (GO:CC organelle membrane; q_global = 0.00522) through (GO:CC vesicle membrane; q_global = 0.0397) and has broad supplementary support for vesicle, secretory-granule, membrane, and Rab annotations (STRING COMPARTMENTS Organelle membrane; within-query FDR = 0.0022) through (STRING Component Secretory vesicle; within-query FDR = 0.016) and (STRING SMART Rab subfamily of small GTPases; within-query FDR = 0.0209) through (STRING COMPARTMENTS Secretory granule; within-query FDR = 0.0244). Its literature volume is substantial.
- **Conclusion**: Established: RAB18 provides a biologically coherent trafficking and organelle component with relevant disease evidence. Hypothesis: RAB18 may coordinate lipid or organelle handling with the vesicle-trafficking program represented by the module.

#### RAB10

- **Related proteins** (co-abundance neighbors): RAB21 (0.84), SYNGR2 (0.84), RAB18 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in ovary, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB10, member RAS oncogene family. RAB10 belongs to the RAS (see HRAS; MIM 190020) superfamily of small GTPases. RAB proteins localize to exocytic and endocytic compartments and regulate intracellular vesicle trafficking (Bao et al., 1998 [PubMed 9918381]).[supplied by OMIM, Mar 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.549); digestive system disorder (0.242); cervical carcinoma (0.215); lobular capilliary hemangioma (0.165); hepatocellular carcinoma (0.109)
- **Europe PMC papers**: 2856
- **Why important**: RAB10 connects both other Rab-family members and SYNGR2, placing it at the core of the vesicle-trafficking portion of the network. Its established functions include exocytosis, Golgi-to-plasma-membrane transport, endosomal transport, vesicle-mediated transport, and antigen processing and presentation. It appears in every primary GO term (GO:CC organelle membrane; q_global = 0.00522) through (GO:CC vesicle membrane; q_global = 0.0397) and in the broadest set of supplementary membrane, vesicle, secretory, Rab, and synaptic-vesicle annotations (STRING COMPARTMENTS Organelle membrane; within-query FDR = 0.0022) through (STRING Component Synaptic vesicle; within-query FDR = 0.0433). It has a particularly large literature base and disease-linked evidence in the supplied resources.
- **Conclusion**: Established: RAB10 is a major molecular anchor for the module's vesicle and exocytic interpretation. Hypothesis: its co-abundance with RAB21, RAB18, and SYNGR2 may reflect coordinated control of cargo delivery or recycling, but this is not shown to be a direct protein complex.

#### STX7

- **Related proteins** (co-abundance neighbors): SFXN1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Lysosomes; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntaxin 7. The protein encoded by this gene is a syntaxin family membrane receptor involved in vesicle transport. The encoded protein binds alpha-SNAP, an important regulator of transport vesicle fusion. Along with syntaxin 13, this protein plays a role in the ordered fusion of endosomes and lysosomes with the phagosome. [provided by RefSeq, May 2016].
- **Diseases (Open Targets)**: neurodegenerative disease (0.489); Abnormality of neuronal migration (0.259); Raynaud disease (0.180); placental abruption (0.166); aortic stenosis (0.081)
- **Europe PMC papers**: 701
- **Why important**: STX7 is the module's annotated lysosomal syntaxin and is linked in the co-abundance graph to SFXN1. It is an established vesicle-fusion factor that binds alpha-SNAP and participates in endosome, lysosome, and phagosome fusion. It contributes to every primary GO term (GO:CC organelle membrane; q_global = 0.00522) through (GO:CC vesicle membrane; q_global = 0.0397) and to supplementary vesicle, secretory, lysosomal-context, and synaptic-vesicle annotations (STRING COMPARTMENTS Organelle membrane; within-query FDR = 0.0022) through (STRING Component Secretory vesicle; within-query FDR = 0.016) and (STRING Keyword Membrane; within-query FDR = 0.0238) through (STRING Component Synaptic vesicle; within-query FDR = 0.0433). Its literature base is established but smaller than that of the principal Rab genes. HPA shows strong cell-type and blood-cell associations and protein detection in testis but not ovary.
- **Conclusion**: Established: STX7 supports a vesicle-fusion interpretation and highlights a possible immune or phagolysosomal contribution. Hypothesis: its asymmetric HPA detection and blood-cell pattern may indicate cellular-composition effects rather than a reproductive tissue-specific vesicle mechanism.

#### VDAC2

- **Related proteins** (co-abundance neighbors): RAB21 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_09822.1, huMAP3_10725.1
- **Function (MyGene.info)**: voltage dependent anion channel 2. This gene encodes a member of the voltage-dependent anion channel pore-forming family of proteins that are considered the main pathway for metabolite diffusion across the mitochondrial outer membrane. The encoded protein is also thought to be involved in the mitochondrial apoptotic pathway via regulation of BCL2-antagonist/killer 1 protein activity. Pseudogenes have been identified on chromosomes …
- **Diseases (Open Targets)**: neurodegenerative disease (0.345); alcohol drinking (0.204); atrial fibrillation (0.175); major depressive disorder (0.143); severe combined immunodeficiency (0.118)
- **Europe PMC papers**: 2914
- **Why important**: VDAC2 provides the clearest mitochondrial outer-membrane bridge in the module and is connected to RAB21. It is an established metabolite channel associated with mitochondrial outer-membrane transport, phospholipid translocation, apoptotic membrane permeabilization, and sperm binding to the zona pellucida. It contributes to the primary organelle-membrane terms (GO:CC organelle membrane; q_global = 0.00522) and (GO:CC bounding membrane of organelle; q_global = 0.0129) and to multiple supplementary membrane and secretory annotations (STRING COMPARTMENTS Organelle membrane; within-query FDR = 0.0022), (STRING COMPARTMENTS Secretory vesicle; within-query FDR = 0.0103), and (STRING Component Organelle membrane; within-query FDR = 0.016) through (STRING COMPARTMENTS Bounding membrane of organelle; within-query FDR = 0.0174) and (STRING Keyword Membrane; within-query FDR = 0.0238) through (STRING COMPARTMENTS Secretory granule; within-query FDR = 0.0244). It has a substantial literature base and disease associations in the supplied resources. hu.MAP places it with STOM in two broad membrane complexes (hu.MAP huMAP3_09822.1) and (hu.MAP huMAP3_10725.1).
- **Conclusion**: Established: VDAC2 supports organelle-membrane and mitochondrial involvement and has reproductive relevance through the supplied sperm-binding annotation. Hypothesis: VDAC2 may couple Rab-associated membrane trafficking to mitochondrial metabolite exchange or stress responses, although the network does not establish that mechanism.
