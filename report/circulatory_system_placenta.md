# Conserved co-abundance modules: circulatory_system and placenta

## Module 0

**Tissue pair**: circulatory_system and placenta  
**Genes (12)**: SERPINF2, BASP1, CD44, CFH, VCAN, FHL2, ITIH2, MFGE8, IGF2R, POSTN, TNC, VASN

### Function

The module is most consistent with a vascular and extracellular-matrix remodeling program that links cell adhesion, hyaluronan-associated matrix organization, complement regulation, protease and fibrinolysis control, growth-factor handling, and clearance of apoptotic material. This interpretation is based on the co-abundance connections among CFH, POSTN, TNC, VASN, CD44, VCAN, ITIH2, SERPINF2, MFGE8, and IGF2R, together with the gene descriptions and HPA localization. The module also contains genes associated with fibroblasts, pericytes, smooth muscle cells, trophoblast-related cells, and vascular tissue, making a vascular stromal or placental interface interpretation plausible. No GO/KEGG term passed global correction; therefore the functional interpretation is gene- and network-based rather than enrichment-based.

**Cell composition.** The module is strongly biased toward extracellular and circulating proteins: most genes are secreted to blood, secreted to the extracellular matrix, secreted with an unspecified location, or associated with the plasma membrane and extracellular vesicles. HPA evidence highlights blood vessel and liver expression, with fibroblasts and pericytes among the most frequent enriched cell types. Several genes are associated with neutrophils or other immune cells, but the module is not uniformly blood-cell specific, and several genes are not detected in immune cells. Placental protein detection is present for several members, while some circulating proteins are not detected in placenta tissue by immunohistochemistry. Thus, the shared module may partly reflect vascular stromal cells and extracellular matrix in both tissues, while its plasma-protein component could also reflect blood content or blood-derived material in the samples.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, CD44--VCAN, supporting a known cell-surface and extracellular-matrix connection. The absence of additional high-confidence STRING relationships means that most co-abundance edges are not confirmed here as direct physical or curated functional interactions. hu.MAP identifies CFH and ITIH2 together in both (hu.MAP huMAP3_15040.1) complexes, but each complex contains many proteins outside the module and only a small subset of its members belongs to this module. This supports a possible shared plasma or extracellular protein context rather than a complete module-sized molecular complex. Overall, the network appears to combine extracellular matrix and adhesion biology with circulating complement, protease-inhibitory, and coagulation-related proteins.

**STRING interactions (score >= 0.7)**: 1 of 66 gene pairs: CD44–VCAN (0.996)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (CFH, ITIH2; 2/64); huMAP3_10678.1 (CFH, ITIH2; 2/71)

### Novelty

The module should not be called a new molecular complex or a newly discovered pathway. Its individual genes and several relationships have substantial prior biological literature, CD44--VCAN is supported by STRING, and CFH with ITIH2 occurs in hu.MAP complexes (hu.MAP huMAP3_15040.1). Nevertheless, the specific conserved co-abundance pattern shared by circulatory_system and placenta may represent a useful systems-level observation, especially because it brings vascular matrix genes together with plasma regulators and placental or stromal cell signals. The limited STRING connectivity and broad membership of the hu.MAP complexes prevent a strong claim of a previously unknown physical interaction network. Absence from STRING or hu.MAP alone is not evidence of novelty.

**Hypothesis.** Hypothesis: this conserved module reflects coordinated remodeling and protection of the vascular extracellular environment at the blood-tissue interface. In this model, POSTN, TNC, VCAN, and CD44 organize matrix adhesion and cell migration; VASN may restrain transforming-growth-factor-beta signaling and epithelial-to-mesenchymal transition; CFH limits alternative-pathway complement activation; ITIH2 supports hyaluronan-associated matrix stability; SERPINF2 restrains plasmin activity; MFGE8 supports clearance of apoptotic material; and IGF2R links extracellular ligand handling with intracellular trafficking and growth-factor processing. The shared tissue signal could therefore arise from vascular stromal cells, pericytes, fibroblasts, and placental interface cells, with an additional contribution from circulating proteins in blood-containing samples. This is a mechanistic hypothesis, not a demonstrated causal pathway.

### Important genes

#### CFH

- **Related proteins** (co-abundance neighbors): VASN (0.88), ITIH2 (0.84), CD44 (0.82), POSTN (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: complement factor H. This gene is a member of the Regulator of Complement Activation (RCA) gene cluster and encodes a protein with twenty short consensus repeat (SCR) domains. This protein is secreted into the bloodstream and has an essential role in the regulation of complement activation, restricting this innate defense mechanism to microbial infections. Mutations in this gene have been associated with hemolytic-ure…
- **Diseases (Open Targets)**: complement factor H deficiency (0.769); age-related macular degeneration (0.750); atypical hemolytic-uremic syndrome (0.729); age related macular degeneration 4 (0.711); Doyne honeycomb retinal dystrophy (0.688)
- **Europe PMC papers**: 9287
- **Why important**: CFH has the strongest network position in the module and connects the vascular and matrix-linked part of the network to the circulating-protein component. It is a secreted blood protein that regulates alternative-pathway complement activation, has liver and stromal-cell evidence, occurs with ITIH2 in both hu.MAP complexes (hu.MAP huMAP3_15040.1), and has extensive literature and disease associations including complement factor H deficiency, hemolytic-uremic syndrome, and retinal disease.
- **Conclusion**: Established evidence supports CFH as a central circulating complement regulator and as a plausible bridge between vascular tissue and extracellular matrix signals. Its centrality supports a role in the module, but does not establish that CFH causally organizes the co-abundance pattern.

#### POSTN

- **Related proteins** (co-abundance neighbors): TNC (0.95), VASN (0.85), CFH (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: periostin. This gene encodes a secreted extracellular matrix protein that functions in tissue development and regeneration, including wound healing, and ventricular remodeling following myocardial infarction. The encoded protein binds to integrins to support adhesion and migration of epithelial cells. This protein plays a role in cancer stem cell maintenance and metastasis. Mice lacking this gene exhibit car…
- **Diseases (Open Targets)**: smoking initiation (0.417); Varicose veins (0.359); substance abuse (0.337); attention deficit-hyperactivity disorder (0.337); ankylosing spondylitis (0.318)
- **Europe PMC papers**: 10221
- **Why important**: POSTN is a highly connected extracellular-matrix gene linked to TNC, VASN, and CFH. It is secreted to the extracellular matrix, detected in placenta, and associated with fibroblasts, pericytes, cell adhesion, tissue development, wound healing, and vascular or cardiac remodeling. It also has a substantial literature base and disease associations involving vascular and inflammatory traits.
- **Conclusion**: Established evidence supports POSTN as a matrix-remodeling and cell-adhesion component of the module. Its network position and placental detection make it a strong candidate for coordinating local stromal responses, although a direct causal role in the shared tissue module remains a hypothesis.

#### CD44

- **Related proteins** (co-abundance neighbors): CFH (0.82), FHL2 (0.82); STRING partners: VCAN (0.996)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD44 molecule (IN blood group). The protein encoded by this gene is a cell-surface glycoprotein involved in cell-cell interactions, cell adhesion and migration. It is a receptor for hyaluronic acid (HA) and can also interact with other ligands, such as osteopontin, collagens, and matrix metalloproteinases (MMPs). This protein participates in a wide variety of cellular functions including lymphocyte activation, recirculation and …
- **Diseases (Open Targets)**: nephrolithiasis, calcium oxalate (0.523); calcium oxalate urolithiasis (0.521); uterine corpus leiomyoma (0.480); systemic lupus erythematosus (0.467); autoimmune disease (0.330)
- **Europe PMC papers**: 102058
- **Why important**: CD44 connects to CFH and FHL2 and is the module member participating in the high-confidence STRING relationship with VCAN. It is a plasma-membrane adhesion receptor for hyaluronic acid and other matrix ligands, with roles in adhesion, migration, inflammatory-cell behavior, and placental detection. It has by far the largest literature volume among the module genes and broad disease associations.
- **Conclusion**: Established evidence supports CD44 as a biologically important interface between matrix structure, cell migration, and immune or stromal signaling. The CD44--VCAN relationship gives the module a known molecular anchor, but does not prove that all module edges form one direct pathway.

#### TNC

- **Related proteins** (co-abundance neighbors): IGF2R (0.96), POSTN (0.95); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tenascin C. This gene encodes an extracellular matrix protein with a spatially and temporally restricted tissue distribution. This protein is homohexameric with disulfide-linked subunits, and contains multiple EGF-like and fibronectin type-III domains. It is implicated in guidance of migrating neurons as well as axons during development, synaptic plasticity, and neuronal regeneration. [provided by RefSeq, Jul…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss (0.619); deafness (0.552); osteoarthritis, hip (0.551); total hip arthroplasty (0.468); Varicose veins (0.460)
- **Europe PMC papers**: 12274
- **Why important**: TNC is connected to POSTN and IGF2R and is enriched in blood vessel and smooth-muscle tissue. It is a secreted extracellular-matrix protein involved in cell adhesion, tissue morphogenesis, wounding, and regulation of cell growth. Its substantial literature and vascular disease associations support its importance in a matrix-remodeling interpretation.
- **Conclusion**: Established evidence supports TNC as a vascular and extracellular-matrix remodeling component. Its connection to POSTN is consistent with coordinated matrix organization, while its connection to IGF2R may indicate coupling to receptor-mediated trafficking or growth-factor biology; the latter interpretation remains a hypothesis.

#### IGF2R

- **Related proteins** (co-abundance neighbors): TNC (0.96), MFGE8 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enhanced; location Golgi apparatus; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor 2 receptor. This gene encodes a receptor for both insulin-like growth factor 2 and mannose 6-phosphate. The binding sites for each ligand are located on different segments of the protein. This receptor has various functions, including in the intracellular trafficking of lysosomal enzymes, the activation of transforming growth factor beta, and the degradation of insulin-like growth factor 2. Mutation or loss o…
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.498); coronary artery disorder (0.477); Hypercholesterolemia (0.369); myocardial ischemia (0.359); coronary atherosclerosis (0.349)
- **Europe PMC papers**: 12245
- **Why important**: IGF2R connects the TNC branch to MFGE8 and provides a non-secreted receptor and trafficking component within an otherwise extracellularly biased module. It binds insulin-like growth factor two and mannose-six-phosphate, participates in lysosomal enzyme trafficking, can activate transforming-growth-factor-beta, and is detected in placenta with neutrophil enrichment. It also has extensive literature and associations with liver and coronary disease.
- **Conclusion**: Established evidence supports IGF2R as a receptor and intracellular trafficking regulator that could connect matrix signals to growth-factor processing and lysosomal biology. Its presence broadens the module beyond a simple plasma or matrix signature, but the proposed functional coupling to the other genes is not directly demonstrated by the available interaction evidence.

## Module 1

**Tissue pair**: circulatory_system and placenta  
**Genes (12)**: ANXA3, TUFM, FHL1, HSPB1, HYOU1, KRT18, KRT19, KRT8, PDIA4, SERPINH1, TGM2, TF

### Function

The module is best interpreted as a mixed epithelial–trophoblast structural and proteostasis module rather than as a narrowly defined pathway. Its network contains a TGM2-centered group linked to KRT8, KRT18, KRT19, SERPINH1 and HSPB1, an epithelial intermediate-filament unit formed by KRT8, KRT18 and KRT19, and an endoplasmic-reticulum proteostasis pair formed by PDIA4 and HYOU1. TGM2 supports protein crosslinking, extracellular-matrix organization and apoptotic regulation; the keratins support epithelial structural integrity; SERPINH1 supports collagen folding; HSPB1 supports stress-responsive chaperoning; and PDIA4 and HYOU1 support protein folding, secretion and responses to ER stress or hypoxia. No GO/KEGG term passed global correction, so these functional interpretations are based on individual gene annotations, network structure, STRING relationships and hu.MAP evidence rather than on significant module-level enrichment. The absence of a globally significant term does not invalidate the module.

**Cell composition.** The module is compositionally mixed, with prominent epithelial and trophoblast features rather than a predominantly plasma-protein or blood-cell signature. HPA identifies migrating and extravillous trophoblasts, cytotrophoblasts, epithelial cell types and decidual stromal cells among the recurring enriched populations. KRT8, KRT18 and KRT19 are epithelial intermediate-filament genes, while TGM2, SERPINH1, HSPB1, PDIA4 and HYOU1 are compatible with matrix, folding or stress-related cellular programs. TF is secreted to blood and may contribute a circulating-protein component, but the module is not dominated by secreted proteins. Blood-cell evidence is mixed and limited: some genes show immune-cell enrichment or enhancement, whereas others have low immune specificity or are not detected in immune cells. All module proteins are detected in placenta, while the circulatory-system protein summary has no matching HPA tissue result. Thus, the shared signal may reflect trophoblast or epithelial-cell content, together with a stress or secretory state, rather than a blood-cell program alone.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a compact set of established relationships: the strongest relationship is between HYOU1 and PDIA4, and the keratin relationships connect KRT18 with KRT19 and KRT8 and KRT19 with KRT8. These known relationships support the interpretation of an ER-folding arm and an epithelial intermediate-filament arm, but STRING does not provide functional enrichment for the module and does not connect every module member. hu.MAP provides additional support for a shared proteostasis or trafficking context: PDIA4, SERPINH1 and HYOU1 occur together in (hu.MAP huMAP3_09327.1), while PDIA4 and HYOU1 recur in (hu.MAP huMAP3_06775.1). The complexes contain many proteins outside the module, so they support membership in broader cellular assemblies rather than proving that the entire module is one physical complex. TGM2, the keratin genes, TF, FHL1, TUFM, HSPB1 and ANXA3 have no reported hu.MAP complex membership in the fact sheet, and several module edges are not backed by high-confidence STRING interactions. The network therefore combines established submodules with co-abundance relationships that remain mechanistically unresolved.

**STRING interactions (score >= 0.7)**: 4 of 66 gene pairs: HYOU1–PDIA4 (0.997); KRT18–KRT19 (0.928); KRT18–KRT8 (0.999); KRT19–KRT8 (0.796)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09327.1 (PDIA4, SERPINH1, HYOU1; 3/93); huMAP3_06775.1 (PDIA4, HYOU1; 2/60)

### Novelty

The module-level finding should be treated as a candidate shared co-abundance pattern, not as an established new molecular complex or pathway. Parts of it are clearly known: the KRT8–KRT18–KRT19 epithelial structure is supported by STRING, and the PDIA4–HYOU1 relationship is supported by both STRING and hu.MAP, with SERPINH1 joining the broader hu.MAP context in (hu.MAP huMAP3_09327.1). The fact sheet provides no globally significant GO/KEGG term and no STRING functional-enrichment result, which limits claims of a newly defined biological process. At the same time, the specific cross-tissue co-abundance arrangement, including TGM2 as a network connector between keratins, matrix-related proteins and stress proteins, is not directly represented as a single established STRING or hu.MAP entity. It is therefore potentially interesting as a tissue-sharing signature, but novelty would require independent replication, cell-composition adjustment, comparison with published co-abundance modules and experimental validation. Absence from a database alone is not evidence of novelty.

**Hypothesis.** Hypothesis: the shared module reflects a placenta-associated epithelial or trophoblast state in which intermediate-filament remodeling is coordinated with extracellular-matrix handling and ER protein quality control. TGM2 may couple cytoskeletal or matrix remodeling to cellular stress responses, while SERPINH1 supports collagen maturation and PDIA4–HYOU1 supports folding and secretion under hypoxic or secretory conditions. HSPB1 may buffer proteotoxic stress, and TF may represent a circulating or vascular-facing component of the same tissue state. In circulatory-system samples, the apparent module could partly arise from placental-like epithelial or vascular-associated cellular content, shared stress programs, or circulating material rather than from a common cell-intrinsic pathway. This hypothesis is not established by the enrichment analysis and should be tested with cell-resolved expression, covariate-adjusted co-abundance analysis and perturbation of the ER-stress or matrix-remodeling components.

### Important genes

#### TGM2

- **Related proteins** (co-abundance neighbors): KRT8 (0.93), KRT18 (0.90), KRT19 (0.86), SERPINH1 (0.85), HSPB1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transglutaminase 2. Transglutaminases are enzymes that catalyze the crosslinking of proteins by epsilon-gamma glutamyl lysine isopeptide bonds. While the primary structure of transglutaminases is not conserved, they all have the same amino acid sequence at their active sites and their activity is calcium-dependent. The protein encoded by this gene acts as a monomer, is induced by retinoic acid, and appears to be invo…
- **Diseases (Open Targets)**: neurodegenerative disease (0.495); autoimmune disorder of central nervous system (0.324); placental abruption (0.297); arterial embolism (0.266); seborrheic dermatitis (0.251)
- **Europe PMC papers**: 4586
- **Why important**: TGM2 is the most connected node in the module and links the keratin group with SERPINH1 and HSPB1. Its documented functions include calcium-dependent protein crosslinking, extracellular-matrix organization and regulation of apoptosis. HPA supports tissue enhancement in blood vessel and cell-type enhancement in cytotrophoblasts and stromal populations, while the secretome annotation places it in the extracellular matrix. Its disease associations include celiac disease as an autoantigen and reported links to placental abruption and arterial embolism. It also has a substantial literature base.
- **Conclusion**: Established evidence supports TGM2 as the principal network connector and as a plausible matrix–stress interface. The idea that it causally organizes the shared module across circulatory system and placenta remains a hypothesis because no direct module-level interaction or globally significant enrichment establishes that role.

#### KRT8

- **Related proteins** (co-abundance neighbors): KRT18 (0.98), TGM2 (0.93); STRING partners: KRT18 (0.999), KRT19 (0.796)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Intermediate filaments; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 8. This gene is a member of the type II keratin family clustered on the long arm of chromosome 12. Type I and type II keratins heteropolymerize to form intermediate-sized filaments in the cytoplasm of epithelial cells. The product of this gene typically dimerizes with keratin 18 to form an intermediate filament in simple single-layered epithelial cells. This protein plays a role in maintaining cellul…
- **Diseases (Open Targets)**: cirrhosis of liver (0.596); cirrhosis, familial (0.401); neurodegenerative disease (0.371); prostate carcinoma (0.314); Abnormality of the liver (0.306)
- **Europe PMC papers**: 5942
- **Why important**: KRT8 is a central member of the epithelial intermediate-filament unit and has strong STRING support with KRT18 and additional support with KRT19. It is enriched in intestinal and gastric tissue contexts and in enterocytes, colonocytes, goblet cells and extravillous trophoblasts. Its established function is to heteropolymerize with KRT18 and maintain epithelial structural integrity, with roles in signaling and differentiation. It has associations with cirrhosis, neurodegenerative disease and other disorders, and a large literature base.
- **Conclusion**: KRT8 is strong evidence that the module contains an epithelial or trophoblast structural program. Its presence does not by itself show a placenta-specific mechanism, because the gene is broadly relevant to simple epithelia and may also report cell composition.

#### KRT18

- **Related proteins** (co-abundance neighbors): KRT8 (0.98), TGM2 (0.90), TUFM (0.84); STRING partners: KRT19 (0.928), KRT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 18. KRT18 encodes the type I intermediate filament chain keratin 18. Keratin 18, together with its filament partner keratin 8, are perhaps the most commonly found members of the intermediate filament gene family. They are expressed in single layer epithelial tissues of the body. Mutations in this gene have been linked to cryptogenic cirrhosis. Two transcript variants encoding the same protein have bee…
- **Diseases (Open Targets)**: cirrhosis of liver (0.623); cirrhosis, familial (0.396); prostate carcinoma (0.140); neoplasm (0.117); breast carcinoma (0.113)
- **Europe PMC papers**: 6539
- **Why important**: KRT18 is a high-connectivity epithelial structural gene that connects KRT8 to TGM2 and TUFM and participates in the STRING-supported keratin subnetwork with KRT19. HPA identifies it in cytotrophoblasts and extravillous trophoblasts as well as several epithelial populations. Its established functions include intermediate-filament organization, epithelial cell adhesion and protection from apoptosis. It is associated with cirrhosis and neoplastic disease and has a substantial literature base.
- **Conclusion**: KRT18 provides established support for an epithelial cytoskeletal component shared with trophoblast biology. Its co-abundance with stress and matrix genes may indicate a cellular-state association, but causality and tissue sharing cannot be inferred from this network alone.

#### PDIA4

- **Related proteins** (co-abundance neighbors): HYOU1 (0.82), KRT19 (0.80); STRING partners: HYOU1 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_09327.1, huMAP3_06775.1
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 is part of the strongest STRING-supported relationship in the module through HYOU1 and is present in both hu.MAP contexts (hu.MAP huMAP3_09327.1) and (hu.MAP huMAP3_06775.1). It is an ER protein-folding catalyst with roles in thiol-disulfide exchange, protein secretion and ER-stress responses. HPA places it in the ER and identifies it in extravillous trophoblasts, hepatocytes and plasma cells. Its disease associations include neurodegenerative disease and ovarian cancer, and its literature base is smaller than that of the keratins but directly relevant to proteostasis.
- **Conclusion**: Established evidence supports PDIA4 as a core ER-proteostasis component and as one of the best-supported physical or complex-associated members of the module. Its proposed coordination with keratin and matrix remodeling is plausible but remains inferential.

#### HYOU1

- **Related proteins** (co-abundance neighbors): PDIA4 (0.82); STRING partners: PDIA4 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_09327.1, huMAP3_06775.1
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 forms the strongest STRING relationship with PDIA4 and occurs with PDIA4 in both hu.MAP contexts (hu.MAP huMAP3_09327.1) and (hu.MAP huMAP3_06775.1). Its documented biology includes hypoxia-responsive ER chaperoning, protein folding, ER-to-Golgi transport and protection from stress-associated apoptosis. HPA identifies it in plasma cells and other cell types and classifies its location as intracellular and membrane-associated in the supplied summary. It has disease associations involving granulocytopenia, neurodegenerative disease, dengue disease and coronary artery disorder.
- **Conclusion**: Established evidence supports HYOU1 as a stress-sensitive ER partner of PDIA4. A hypoxia-linked secretory mechanism in trophoblasts is a reasonable interpretation, but the module data do not prove that HYOU1 drives the cross-tissue co-abundance pattern.

#### SERPINH1

- **Related proteins** (co-abundance neighbors): TGM2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_09327.1
- **Function (MyGene.info)**: serpin family H member 1. This gene encodes a member of the serpin superfamily of serine proteinase inhibitors. The encoded protein is localized to the endoplasmic reticulum and plays a role in collagen biosynthesis as a collagen-specific molecular chaperone. Autoantibodies to the encoded protein have been found in patients with rheumatoid arthritis. Expression of this gene may be a marker for cancer, and nucleotide polymo…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 10 (0.714); preterm premature rupture of the membranes (0.559); coronary artery disorder (0.554); myocardial infarction (0.510); Abnormality of the skeletal system (0.474)
- **Europe PMC papers**: 2762
- **Why important**: SERPINH1 is connected to the network hub TGM2 and joins PDIA4 and HYOU1 in hu.MAP context (hu.MAP huMAP3_09327.1). It is an ER collagen-specific chaperone with functions in collagen biosynthesis, protein folding, unfolded-protein responses and collagen fibril organization. HPA identifies it in cytotrophoblasts, extravillous trophoblasts and decidual or endometrial stromal cells. Its disease associations include osteogenesis imperfecta, preterm premature rupture of membranes, coronary artery disorder and myocardial infarction.
- **Conclusion**: Established evidence supports SERPINH1 as a matrix-collagen folding component that strengthens the interpretation of coordinated extracellular-matrix and ER proteostasis biology. Its connection to TGM2 and the trophoblast context is compelling, but a direct role in the shared module requires validation.

## Module 2

**Tissue pair**: circulatory_system and placenta  
**Genes (5)**: CALD1, CORO1C, ITGB1, PDLIM7, TPM1

### Function

The module is most consistent with an actin-cytoskeleton, contractility, focal-adhesion, and cell-adhesion program. TPM1 and CALD1 are directly associated with actin–tropomyosin regulation and muscle or non-muscle contraction; PDLIM7 links PDZ/LIM-mediated cytoskeletal organization with focal adhesions; ITGB1 is a membrane adhesion receptor involved in cell adhesion, angiogenesis, hemostasis, embryogenesis, and tissue repair; and CORO1C is an actin-associated WD-repeat protein involved in actin organization, phagocytosis, and signaling. The co-abundance topology supports a connected cytoskeletal module centered on TPM1 and PDLIM7, with CALD1 and ITGB1 providing contractile and adhesion-related peripheral links. No GO or KEGG term passed global correction, so the functional interpretation rests on the convergent gene annotations, network structure, and supplementary STRING result rather than on globally significant pathway enrichment.

**Cell composition.** The module is not composed of plasma or secreted proteins: all genes have no secretome annotation. HPA shows a mixture of low-specificity and tissue-enhanced proteins, with enrichment pointing toward skeletal muscle, heart muscle, blood vessel, and intestine. At the single-cell level, the genes are repeatedly enhanced in smooth-muscle, vascular smooth-muscle, stromal, myoepithelial, trophoblast, platelet, and selected immune-cell populations. Blood-cell evidence is mixed rather than uniformly blood-cell specific, including basophil, eosinophil, neutrophil, and platelet associations. Thus, in circulatory-system and placenta samples, the shared module may reflect vascular or stromal contractile cells, trophoblast-associated cytoskeletal biology, platelet or blood-cell contributions, or shared structural cell types, rather than a circulating secreted-protein program. Placental protein detection supports presence of most module proteins in placenta, whereas the supplied circulatory-system protein-detection field has no matching HPA tissue.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports one high-confidence direct relationship, CALD1–TPM1, which is biologically coherent with actin–tropomyosin regulation and contractility. STRING also places PDLIM7, TPM1, ITGB1, and CORO1C in the supplementary Ruffle component (STRING Component Ruffle; within-query FDR = 0.0475). This supports an actin-remodeling and adhesion interpretation, but (STRING Component Ruffle; within-query FDR = 0.0475) is supplementary and its original within-query FDR is not global module-level evidence. The remaining module relationships are not supported by the supplied high-confidence STRING pair list. No hu.MAP complex contains at least two module members. Consequently, the co-abundance module extends beyond currently catalogued physical interactions or complexes and should not be treated as a demonstrated multiprotein complex.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: CALD1–TPM1 (0.869)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Ruffle (FDR = 0.0475, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially interesting shared co-abundance pattern, but it cannot be called a wholly new biological pathway or interaction module. The functions of the individual genes, the CALD1–TPM1 relationship, and the broad actin, adhesion, and contractility biology are established. The potentially novel aspect is their coordinated abundance across circulatory system and placenta, particularly the combination of contractile, focal-adhesion, and actin-remodeling genes. Absence of a matching hu.MAP complex and the limited STRING interaction coverage suggest that this exact tissue-pair co-abundance configuration may not be well represented in those resources, but database absence alone does not establish novelty. The lack of globally corrected GO or KEGG enrichment also means the module should be presented as a network-level observation requiring replication, not as a newly discovered pathway.

**Hypothesis.** Hypothesis: the shared module reflects a conserved structural-cell program in which TPM1 and CALD1 regulate actin–myosin contractility, PDLIM7 organizes actin and focal-adhesion interfaces, ITGB1 transmits extracellular-matrix adhesion signals, and CORO1C supports actin remodeling. In placenta this could relate to stromal, vascular, smooth-muscle, platelet, or trophoblast-associated remodeling, while in circulatory-system material it could reflect vascular or other contractile structural cells and blood-cell contributions. The cross-tissue co-abundance may therefore arise from shared cellular composition or a conserved adhesion-and-contractility response, rather than from secretion into blood. This hypothesis is consistent with the network and HPA evidence but is not established by the supplied enrichment results.

### Important genes

#### TPM1

- **Related proteins** (co-abundance neighbors): CALD1 (0.84), PDLIM7 (0.84), CORO1C (0.82); STRING partners: CALD1 (0.869)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tropomyosin 1. This gene is a member of the tropomyosin family of highly conserved, widely distributed actin-binding proteins involved in the contractile system of striated and smooth muscles and the cytoskeleton of non-muscle cells. Tropomyosin is composed of two alpha-helical chains arranged as a coiled-coil. It is polymerized end to end along the two grooves of actin filaments and provides stability to the fi…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy (0.798); left ventricular noncompaction (0.760); left ventricular noncompaction 9 (0.664); familial isolated dilated cardiomyopathy (0.639); hypertrophic cardiomyopathy 3 (0.596)
- **Europe PMC papers**: 6278
- **Why important**: TPM1 has a central network position, connecting CALD1, PDLIM7, and CORO1C, and it is the partner in the only high-confidence STRING interaction. Its actin-binding and tropomyosin functions directly support regulation of muscle and non-muscle contractility, cytoskeleton organization, and cell shape. HPA links it to heart and skeletal muscle and to several relevant cell types, including decidual stromal cells, extravillous trophoblasts, and megakaryocytes. Its extensive literature and disease associations with cardiomyopathy make it the strongest established contractile anchor of the module.
- **Conclusion**: Established evidence supports TPM1 as a central actin–contractility component and a plausible marker of contractile or structural-cell content. It is not established that TPM1 drives the shared circulatory-system–placenta co-abundance pattern or that it has a tissue-pair-specific function here.

#### PDLIM7

- **Related proteins** (co-abundance neighbors): TPM1 (0.84), CORO1C (0.84), ITGB1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Actin filaments, Focal adhesion sites; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 7. The protein encoded by this gene is representative of a family of proteins composed of conserved PDZ and LIM domains. LIM domains are proposed to function in protein-protein recognition in a variety of contexts including gene transcription and development and in cytoskeletal interaction. The LIM domains of this protein bind to protein kinases, whereas the PDZ domain binds to actin filaments. The g…
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); nasopharyngeal carcinoma (0.121); neoplasm (0.120); lymphoma (0.115); Hodgkins lymphoma (0.105)
- **Europe PMC papers**: 808
- **Why important**: PDLIM7 has a central network position, linking TPM1, CORO1C, and ITGB1. Its PDZ and LIM domains connect actin filaments, protein kinases, and focal-adhesion-associated organization. HPA places it in blood vessel and skeletal-muscle contexts and in stromal, smooth-muscle, vascular, neutrophil, and megakaryocyte-related cell populations. Its placement between the contractile and adhesion components makes it a strong candidate for organizing the module rather than merely marking one pathway.
- **Conclusion**: Established evidence supports PDLIM7 as an actin-associated scaffold connecting contractile and adhesion-related biology. Its role as the organizing coordinator of this shared module remains a hypothesis because no direct STRING partner or hu.MAP complex is supplied for PDLIM7.

#### CALD1

- **Related proteins** (co-abundance neighbors): TPM1 (0.84); STRING partners: TPM1 (0.869)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Actin filaments; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caldesmon 1. This gene encodes a calmodulin- and actin-binding protein that plays an essential role in the regulation of smooth muscle and nonmuscle contraction. The conserved domain of this protein possesses the binding activities to Ca(2+)-calmodulin, actin, tropomyosin, myosin, and phospholipids. This protein is a potent inhibitor of the actin-tropomyosin activated myosin MgATPase, and serves as a mediating…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.499); diaphragmatic hernia (0.447); glaucoma (0.405); diverticular disease (0.393); open-angle glaucoma (0.390)
- **Europe PMC papers**: 3386
- **Why important**: CALD1 provides the clearest contractile regulatory link to TPM1, which is both its module neighbor and its high-confidence STRING partner. Caldesmon binds calmodulin, actin, tropomyosin, myosin, and phospholipids and regulates calcium-dependent smooth-muscle and non-muscle contraction. Its plasma-membrane and actin-filament localization and placental detection are consistent with a structural-cell contribution. Its substantial literature and disease associations further support its biological relevance.
- **Conclusion**: Established evidence supports CALD1 as a contractility regulator and as the most directly validated physical interaction partner of TPM1 in this module. The data do not establish whether CALD1-mediated contraction is the primary reason for the cross-tissue co-abundance.

#### ITGB1

- **Related proteins** (co-abundance neighbors): PDLIM7 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 links the module to cell-surface adhesion and extracellular-matrix signaling. It occupies an edge connecting to PDLIM7 and is localized at the plasma membrane and focal-adhesion sites. Its established roles include cell adhesion, angiogenesis, embryogenesis, hemostasis, tissue repair, immune response, and metastatic diffusion. HPA detects it in placenta and associates it with platelet-related cell populations. Its broad disease and literature record makes it an important functional bridge between cytoskeletal organization and tissue remodeling.
- **Conclusion**: Established evidence supports ITGB1 as an adhesion and mechanotransduction-related component compatible with vascular, placental, stromal, or platelet biology. Its specific physical connection to PDLIM7 is inferred from co-abundance here, not demonstrated by the supplied STRING or hu.MAP evidence.

#### CORO1C

- **Related proteins** (co-abundance neighbors): PDLIM7 (0.84), TPM1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coronin 1C. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.453); Parkinson disease (0.322); Alzheimer disease (0.312); lysosomal storage disease (0.310); liver disorder (0.261)
- **Europe PMC papers**: 774
- **Why important**: CORO1C is connected to both PDLIM7 and TPM1 and is included in the supplementary STRING Ruffle component (STRING Component Ruffle; within-query FDR = 0.0475). Its WD-repeat protein architecture and annotations connect it to actin filament organization, phagocytosis, signal transduction, and regulation of protein phosphorylation. HPA identifies platelet-related cell-type enhancement and placental detection, providing a possible explanation for its occurrence in the shared module. Its literature and disease associations support relevance while also indicating that it is less specifically contractile than TPM1 or CALD1.
- **Conclusion**: Established evidence supports CORO1C as an actin-remodeling and signaling component, potentially reflecting platelet or other structural-cell contributions. Its role in coordinating the contractile and adhesion features of this module is a hypothesis, because the supplied data do not demonstrate a direct physical complex involving CORO1C.

## Module 3

**Tissue pair**: circulatory_system and placenta  
**Genes (13)**: CNN2, COL4A2, COL18A1, FN1, IGFBP3, IGFBP7, LGALS3BP, PEPD, SPARC, TAGLN2, TIMP2, LTF, THBS1

### Function

The module is most consistent with an extracellular-matrix and basement-membrane remodeling program shared by vascular and placental tissues. Its genes include structural matrix components, matrix-associated glycoproteins, protease regulation, and IGF-binding proteins. FN1, COL18A1, and COL4A2 support matrix architecture; SPARC and THBS1 support cell–matrix interactions and angiogenic regulation; TIMP2 supports control of matrix proteolysis and endothelial proliferation; and IGFBP3 and IGFBP7 support regulation of IGF availability, cell growth, adhesion, and vascular behavior. The annotations also connect the genes with angiogenesis, endothelial or cell morphogenesis, cell adhesion, smooth-muscle or stromal biology, and placental implantation. No GO/KEGG term passed global correction, so this functional interpretation is based on the coherent gene annotations, network structure, STRING relationships, hu.MAP overlap, and HPA evidence rather than on a globally significant enrichment term.

**Cell composition.** The module is strongly dominated by secreted or extracellular-matrix-associated proteins. HPA identifies most of the genes as secreted, secreted to blood, or secreted to extracellular matrix, while FN1, COL18A1, COL4A2, SPARC, THBS1, IGFBP3, IGFBP7, and LGALS3BP provide particularly clear extracellular or circulating components. HPA links the genes especially to placenta, blood vessels, extravillous trophoblasts, fibroblasts, hepatic stellate cells, vascular-associated cells, and decidual stromal cells. Several genes also have neutrophil, eosinophil, monocyte, platelet, or other immune-cell associations, and LTF has a strong neutrophil and secretory-cell signature. Thus, the shared module may reflect a genuine vascular–placental stromal program, but it could also partly reflect extracellular proteins in blood or shared stromal, trophoblast, vascular, and immune-cell content in the samples. It is not a conventional housekeeping module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a connected extracellular-matrix network centered on FN1, with strong relationships to SPARC, THBS1, IGFBP3, LGALS3BP, TIMP2, COL18A1, and COL4A2. Additional relationships connect IGFBP3 with IGFBP7, IGFBP7 with TIMP2, and SPARC with THBS1. These known associations reinforce the interpretation of coordinated matrix organization, cell adhesion, growth-factor modulation, and protease control, but STRING enrichment itself is absent and STRING relationships do not prove that every co-abundance edge is a direct physical interaction. hu.MAP independently places COL4A2 and COL18A1 together in several collagen-rich complexes (hu.MAP huMAP3_07149.1) (hu.MAP huMAP3_02991.1) (hu.MAP huMAP3_06555.1) (hu.MAP huMAP3_08295.1) (hu.MAP huMAP3_09435.1) (hu.MAP huMAP3_10984.1) (hu.MAP huMAP3_10699.1) (hu.MAP huMAP3_13038.1). The repeated co-membership is consistent with a basement-membrane or collagen-assembly context, although only a small subset of each reported complex belongs to this module. The remaining module genes have no hu.MAP complex assignment in the fact sheet, so the module extends beyond a single established physical complex.

**STRING interactions (score >= 0.7)**: 13 of 78 gene pairs: COL18A1–COL4A2 (0.733); COL18A1–FN1 (0.838); COL18A1–SPARC (0.757); COL18A1–THBS1 (0.864); COL4A2–FN1 (0.75); FN1–IGFBP3 (0.967); FN1–LGALS3BP (0.953); FN1–SPARC (0.969); FN1–THBS1 (0.999); FN1–TIMP2 (0.713); IGFBP3–IGFBP7 (0.764); IGFBP7–TIMP2 (0.874); SPARC–THBS1 (0.847)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07149.1 (COL4A2, COL18A1; 2/10); huMAP3_02991.1 (COL4A2, COL18A1; 2/14); huMAP3_06555.1 (COL4A2, COL18A1; 2/14); huMAP3_08295.1 (COL4A2, COL18A1; 2/17); huMAP3_09435.1 (COL4A2, COL18A1; 2/18); huMAP3_10984.1 (COL4A2, COL18A1; 2/21); huMAP3_10699.1 (COL4A2, COL18A1; 2/28); huMAP3_13038.1 (COL4A2, COL18A1; 2/40)

### Novelty

The exact cross-tissue co-abundance module may be a new systems-level finding, but the underlying biology is not wholly novel. Its central relationships involve well-established extracellular-matrix, collagen, angiogenesis, adhesion, IGF-binding, and protease-regulatory proteins, and the COL4A2–COL18A1 pairing recurs in hu.MAP collagen-related complexes (hu.MAP huMAP3_07149.1) (hu.MAP huMAP3_02991.1) (hu.MAP huMAP3_06555.1) (hu.MAP huMAP3_08295.1) (hu.MAP huMAP3_09435.1) (hu.MAP huMAP3_10984.1) (hu.MAP huMAP3_10699.1) (hu.MAP huMAP3_13038.1). STRING also contains many of the central pairwise relationships. Therefore, the defensible novelty claim is the conserved association of this particular gene combination across circulatory_system and placenta, not discovery of previously unknown functions or interactions. Absence of a complete matching module in STRING or hu.MAP would not by itself establish novelty, and the fact sheet does not provide an external reference showing that this exact co-abundance module has been previously reported.

**Hypothesis.** Hypothesis: a shared vascular–placental stromal program produces and remodels extracellular matrix while coordinating angiogenesis, cell adhesion, basement-membrane integrity, and local growth-factor availability. FN1, collagen components, SPARC, and THBS1 may form the structural and signaling scaffold; TIMP2 may restrain matrix proteolysis and endothelial proliferation; and IGFBP3 and IGFBP7 may tune IGF-dependent growth and differentiation signals. Circulating or vesicular release of several module proteins could make this tissue program visible in circulatory samples. The LTF and immune-cell-associated signals raise the additional hypothesis that blood-cell or inflammatory composition contributes to the observed cross-tissue co-abundance. These mechanisms require experimental testing and should not be treated as demonstrated by the co-abundance network alone.

### Important genes

#### FN1

- **Related proteins** (co-abundance neighbors): TIMP2 (0.95), IGFBP3 (0.89), COL18A1 (0.85); STRING partners: COL18A1 (0.838), COL4A2 (0.75), IGFBP3 (0.967), LGALS3BP (0.953), SPARC (0.969), THBS1 (0.999), TIMP2 (0.713)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 is a central connector in the module and has the strongest STRING support among the matrix-associated relationships listed. It is a soluble plasma protein as well as an extracellular-matrix protein, and its established roles include cell adhesion, cell–matrix adhesion, migration, embryogenesis, wound healing, coagulation, and host defense. HPA links it to blood vessel, liver, and placenta and to extravillous trophoblasts, fibroblasts, hepatic stellate cells, and hepatocytes. Its extensive literature and disease associations make it the clearest integrative marker of the module.
- **Conclusion**: Established evidence supports FN1 as a major extracellular scaffold and adhesion regulator connecting the module to vascular and placental biology. It is also a plausible contributor to the blood-derived signal. It should not be assumed that FN1 mechanistically drives the entire module merely because it is highly connected.

#### SPARC

- **Related proteins** (co-abundance neighbors): IGFBP7 (0.94), IGFBP3 (0.91), COL18A1 (0.87), LTF (0.84), THBS1 (0.81), COL4A2 (0.80); STRING partners: COL18A1 (0.757), FN1 (0.969), THBS1 (0.847)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: secreted protein acidic and cysteine rich. This gene encodes a cysteine-rich acidic matrix-associated protein. The encoded protein is required for the collagen in bone to become calcified but is also involved in extracellular matrix synthesis and promotion of changes to cell shape. The gene product has been associated with tumor suppression but has also been correlated with metastasis based on changes to cell shape which can promote tumor …
- **Diseases (Open Targets)**: osteogenesis imperfecta (0.707); neurodegenerative disease (0.443); hereditary disease (0.414); osteogenesis imperfecta type 4 (0.381); Abnormality of the skeletal system (0.358)
- **Europe PMC papers**: 17798
- **Why important**: SPARC is highly connected to IGFBP proteins, collagens, FN1, and THBS1, placing it at the interface of matrix structure and signaling. It is a secreted matrix-associated protein involved in matrix synthesis, cell-shape changes, endothelial proliferation and migration, and angiogenic regulation. HPA associates it with decidual stromal cells, extravillous trophoblasts, fibroblasts, hepatic stellate cells, and several blood-cell populations. Its substantial literature and links to skeletal and hereditary disease add biological and translational importance.
- **Conclusion**: Established evidence supports SPARC as a matrix-remodeling and cell-shape regulator that can connect stromal, vascular, and placental compartments. Its coordinated abundance with FN1, collagens, and THBS1 is compatible with a remodeling program. Whether SPARC is a causal organizer or mainly a readout of stromal composition remains unresolved.

#### IGFBP3

- **Related proteins** (co-abundance neighbors): TAGLN2 (0.94), LGALS3BP (0.92), SPARC (0.91), THBS1 (0.91), COL18A1 (0.90), FN1 (0.89), TIMP2 (0.86); STRING partners: FN1 (0.967), IGFBP7 (0.764)
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor binding protein 3. This gene is a member of the insulin-like growth factor binding protein (IGFBP) family and encodes a protein with an IGFBP domain and a thyroglobulin type-I domain. The protein forms a ternary complex with insulin-like growth factor acid-labile subunit (IGFALS) and either insulin-like growth factor (IGF) I or II. In this form, it circulates in the plasma, prolonging the half-life of IGFs and alter…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.494); lymphatic system disorder (0.383); Alzheimer disease (0.368); cancer (0.365); colorectal cancer (0.365)
- **Europe PMC papers**: 9893
- **Why important**: IGFBP3 is among the most connected genes in the module and links the matrix network to endocrine and growth-factor regulation. It forms complexes with IGFs and IGFALS, can alter IGF receptor access, and is annotated with regulation of proliferation, phosphorylation, signal transduction, and smooth-muscle migration. HPA identifies it as secreted to blood, enriched in placenta and extravillous trophoblasts, and associated with plasmacytoid dendritic cells. It also has extensive literature and broad disease associations.
- **Conclusion**: Established evidence supports IGFBP3 as a circulating and placental growth-factor modulator embedded in the extracellular-matrix network. Its network position makes it a strong candidate for coupling matrix state to cellular growth or migration. A direct causal role in conservation of the module across the two tissues is a hypothesis rather than an established result.

#### THBS1

- **Related proteins** (co-abundance neighbors): IGFBP7 (0.92), IGFBP3 (0.91), LTF (0.89), COL18A1 (0.84), SPARC (0.81); STRING partners: COL18A1 (0.864), FN1 (0.999), SPARC (0.847)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum, Plasma membrane; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thrombospondin 1. The protein encoded by this gene is a subunit of a disulfide-linked homotrimeric protein. This protein is an adhesive glycoprotein that mediates cell-to-cell and cell-to-matrix interactions. This protein can bind to fibrinogen, fibronectin, laminin, type V collagen and integrins alpha-V/beta-1. This protein has been shown to play roles in platelet aggregation, angiogenesis, and tumorigenesis. [pro…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.385); tooth disorder (0.350); autism spectrum disorder (0.336); neurodegenerative disease (0.323); metabolic syndrome (0.309)
- **Europe PMC papers**: 12762
- **Why important**: THBS1 connects FN1, SPARC, COL18A1, IGFBP proteins, and LTF and is a secreted extracellular-matrix glycoprotein with roles in cell–cell and cell–matrix interactions, platelet aggregation, angiogenesis, and tumor biology. HPA links it to fibroblasts, hepatic stellate cells, macrophages, monocytes, platelets, and eosinophils, with placental protein detection. Its substantial literature and disease associations make it an important candidate for integrating vascular, platelet, stromal, and inflammatory signals.
- **Conclusion**: Established evidence supports THBS1 as a multifunctional extracellular regulator relevant to angiogenesis, adhesion, and blood-associated biology. Its presence may indicate matrix remodeling and vascular or platelet-related composition. The network does not establish whether THBS1 actively coordinates the module or is co-regulated by the same tissue state.

#### COL18A1

- **Related proteins** (co-abundance neighbors): IGFBP3 (0.90), SPARC (0.87), CNN2 (0.86), FN1 (0.85), THBS1 (0.84); STRING partners: COL4A2 (0.733), FN1 (0.838), SPARC (0.757), THBS1 (0.864)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_07149.1, huMAP3_02991.1, huMAP3_06555.1, huMAP3_08295.1, huMAP3_09435.1, huMAP3_10984.1, huMAP3_10699.1, huMAP3_13038.1
- **Function (MyGene.info)**: collagen type XVIII alpha 1 chain. This gene encodes the alpha chain of type XVIII collagen. This collagen is one of the multiplexins, extracellular matrix proteins that contain multiple triple-helix domains (collagenous domains) interrupted by non-collagenous domains. A long isoform of the protein has an N-terminal domain that is homologous to the extracellular part of frizzled receptors. Proteolytic processing at several endogeno…
- **Diseases (Open Targets)**: Knobloch syndrome 1 (0.778); Knobloch syndrome (0.700); hereditary glaucoma, primary closed-angle (0.593); Dupuytren Contracture (0.587); severe early-childhood-onset retinal dystrophy (0.501)
- **Europe PMC papers**: 5223
- **Why important**: COL18A1 is a basement-membrane collagen and a repeated member of the hu.MAP collagen-related complexes (hu.MAP huMAP3_07149.1) (hu.MAP huMAP3_02991.1) (hu.MAP huMAP3_06555.1) (hu.MAP huMAP3_08295.1) (hu.MAP huMAP3_09435.1) (hu.MAP huMAP3_10984.1) (hu.MAP huMAP3_10699.1) (hu.MAP huMAP3_13038.1). Its proteolytic processing can generate endostatin, and the gene is annotated with angiogenesis, endothelial morphogenesis, and negative regulation of proliferation. HPA shows tissue enhancement in blood vessel and liver, extracellular-matrix secretion, placental detection, and association with neutrophils. It also connects in STRING to COL4A2, FN1, SPARC, and THBS1.
- **Conclusion**: Established evidence supports COL18A1 as a structural basement-membrane component with angiogenesis-related signaling potential. Its repeated hu.MAP co-membership with COL4A2 strengthens the collagen-network interpretation. The possible production of a functional anti-angiogenic fragment is biologically relevant, but its operation in this particular module is not demonstrated.

#### TIMP2

- **Related proteins** (co-abundance neighbors): FN1 (0.95), LTF (0.93), LGALS3BP (0.90), IGFBP3 (0.86), IGFBP7 (0.82); STRING partners: FN1 (0.713), IGFBP7 (0.874)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TIMP metallopeptidase inhibitor 2. This gene is a member of the TIMP gene family. The proteins encoded by this gene family are natural inhibitors of the matrix metalloproteinases, a group of peptidases involved in degradation of the extracellular matrix. In addition to an inhibitory role against metalloproteinases, the encoded protein has a unique role among TIMP family members in its ability to directly suppress the proliferation …
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.365); coronary artery disorder (0.328); benign neoplasm (0.200); asthma (0.199); acute kidney injury (0.121)
- **Europe PMC papers**: 7947
- **Why important**: TIMP2 is connected to FN1, IGFBP3, IGFBP7, and LTF and is a natural inhibitor of matrix metalloproteinases. It also has a distinctive role in suppressing endothelial proliferation and is annotated with regulation of extracellular-domain proteolysis and responses to hormones and cytokines. HPA associates it with fibroblasts, Hofbauer cells, and neutrophils and identifies extracellular-matrix secretion. Its disease associations include coronary artery disorder and acute kidney injury.
- **Conclusion**: Established evidence supports TIMP2 as a plausible matrix-proteolysis brake and endothelial regulator within this module. Its co-abundance with matrix and IGFBP genes is compatible with coordinated control of tissue remodeling. The network alone cannot determine whether TIMP2 activity is increased, decreased, or functionally limiting in either tissue.
