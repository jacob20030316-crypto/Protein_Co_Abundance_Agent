# Conserved co-abundance modules: colon and heart

## Module 0

**Tissue pair**: colon and heart  
**Genes (8)**: BZW2, DNM2, EIF3C, GPD2, PDCD6IP, SLC27A6, QARS1, USP5

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent. Therefore, this module does not establish a statistically supported canonical pathway. Its topology is a star-like co-abundance pattern centered on SLC27A6, with peripheral genes representing fatty-acid transport, mitochondrial redox metabolism, translation, ubiquitin-dependent protein regulation, endocytosis, vesicle biology, and translational initiation. These annotations suggest a possible shared cellular state involving membrane and lipid handling together with protein synthesis and turnover, but the co-abundance data do not demonstrate direct biochemical cooperation or a single unified function.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: the HPA summary identifies only one secreted gene, while the remainder are intracellular or membrane-associated. Most genes have low tissue specificity, and most are detected in both colon and heart. The module is also not strongly blood-cell specific overall: most genes have low immune-cell specificity, one is group-enriched in myeloid cells, and one is not detected in immune cells. All genes show some cell-type enhancement, but the enriched cell types are diverse rather than concentrated in one shared lineage. Thus, blood contamination is not the leading interpretation, although cellular composition and broadly shared cell states could contribute. HPA protein detection is concordant across the two tissues for most genes, with tissue-specific exceptions for SLC27A6 and PDCD6IP.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair in the module has a high-confidence STRING interaction, so the co-abundance links are not supported here as established physical or functional protein interactions. The only hu.MAP evidence is (hu.MAP huMAP3_11232.1), in which DNM2 and BZW2 occur together in a large, heterogeneous complex annotation. Because only a small subset of that complex belongs to this module, (hu.MAP huMAP3_11232.1) supports limited complex-context evidence rather than a compact module-specific complex. The absence of STRING links and the sparse hu.MAP overlap indicate that most relationships in this module are not already represented as well-established molecular interactions in these resources.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11232.1 (DNM2, BZW2; 2/78)

### Novelty

This may be a novel tissue-shared co-abundance pattern, particularly because SLC27A6 links to genes from several cellular processes without corresponding high-confidence STRING relationships or a globally enriched GO or KEGG theme. However, it cannot be called a new biological pathway or a newly discovered molecular complex from these data alone. The star topology may reflect coordinated regulation, shared cell-type composition, technical or sampling effects, or indirect biological coupling. Absence from STRING or hu.MAP does not prove novelty. Stronger novelty claims would require replication in independent colon and heart datasets, preservation of the gene-gene associations, and experimental or orthogonal molecular validation.

**Hypothesis.** Hypothesis: the module reflects a shared cellular program in which SLC27A6-associated lipid handling is coordinated with energy metabolism, membrane trafficking, and protein homeostasis. In this model, SLC27A6 could mark fatty-acid uptake or handling, GPD2 could reflect mitochondrial glycerol-phosphate-shuttle activity, DNM2 and PDCD6IP could reflect membrane remodeling and vesicle processes, and EIF3C, BZW2, and USP5 could reflect regulation of protein production and stability. This is a mechanistic hypothesis, not an established pathway: the absence of global enrichment and STRING support means that the genes may be co-regulated or compositionally coupled without directly interacting.

### Important genes

#### SLC27A6

- **Related proteins** (co-abundance neighbors): QARS1 (0.89), EIF3C (0.88), GPD2 (0.88), USP5 (0.87), DNM2 (0.86), PDCD6IP (0.84), BZW2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nuclear bodies; IHC detected in heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 27 member 6. This gene encodes a member of the fatty acid transport protein family (FATP). FATPs are involved in the uptake of long-chain fatty acids and have unique expression patterns. Alternatively spliced transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: atrial fibrillation (0.498); Abnormality of the skeletal system (0.362); Genu varum (0.352); Genu valgum (0.352); cardiac arrhythmia (0.325)
- **Europe PMC papers**: 619
- **Why important**: SLC27A6 is the central network hub, connected to every other module member with the strongest overall weighted connectivity. Its established function is fatty-acid transport and very-long-chain fatty-acid metabolism. It is tissue-enhanced in heart muscle and also detected in relevant cardiac cell types, while Open Targets links it to atrial fibrillation and cardiac arrhythmia. Its literature volume is more limited than that of several peripheral genes, making its hub position particularly important for interpretation rather than relying only on annotation depth.
- **Conclusion**: Established evidence supports SLC27A6 as the principal network-organizing gene and as a fatty-acid transport factor with cardiac relevance. It is not established that it directly regulates the other module genes. A plausible but unproven interpretation is that SLC27A6 marks a shared lipid-handling state in colon and heart.

#### GPD2

- **Related proteins** (co-abundance neighbors): SLC27A6 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Mitochondria; IHC detected in colon, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycerol-3-phosphate dehydrogenase 2. The protein encoded by this gene localizes to the inner mitochondrial membrane and catalyzes the conversion of glycerol-3-phosphate to dihydroxyacetone phosphate, using FAD as a cofactor. Along with GDP1, the encoded protein constitutes the glycerol phosphate shuttle, which reoxidizes NADH formed during glycolysis. Two transcript variants encoding the same protein have been found for this gene.[pr…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.709); diabetes mellitus (0.597); obstructive sleep apnea syndrome (0.424); polycystic ovary syndrome (0.419); obesity disorder (0.415)
- **Europe PMC papers**: 1990
- **Why important**: GPD2 is connected directly to the hub and provides a metabolic complement to SLC27A6. It encodes the mitochondrial glycerol-phosphate dehydrogenase that participates in the glycerol-phosphate shuttle and links glycolytic reducing equivalents to mitochondrial metabolism. It is detected in both tissues, has a blood-cell group-enriched pattern involving myeloid populations, and has disease associations involving diabetes, obesity, and related metabolic conditions. It also has substantial literature coverage.
- **Conclusion**: Established evidence supports GPD2 as a mitochondrial redox and glycerol-phosphate metabolic gene that could complement lipid transport biology. The module does not establish that GPD2 activity is coordinated mechanistically with SLC27A6, and the myeloid expression pattern means cell composition remains an alternative explanation.

#### DNM2

- **Related proteins** (co-abundance neighbors): SLC27A6 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in colon, heart
- **hu.MAP 3.0**: huMAP3_11232.1
- **Function (MyGene.info)**: dynamin 2. Dynamins represent one of the subfamilies of GTP-binding proteins. These proteins share considerable sequence similarity over the N-terminal portion of the molecule, which contains the GTPase domain. Dynamins are associated with microtubules. They have been implicated in cell processes such as endocytosis and cell motility, and in alterations of the membrane that accompany certain activities such …
- **Diseases (Open Targets)**: autosomal dominant centronuclear myopathy (0.844); Charcot-Marie-Tooth disease dominant intermediate B (0.830); fetal akinesia-cerebral and retinal hemorrhage syndrome (0.739); autosomal dominant Charcot-Marie-Tooth disease type 2M (0.715); centronuclear myopathy (0.692)
- **Europe PMC papers**: 2412
- **Why important**: DNM2 is directly connected to the hub and encodes a dynamin involved in GTPase-dependent membrane remodeling, endocytosis, vesicle transport, and autophagy. It has the strongest literature depth among the selected genes and extensive disease associations, including centronuclear myopathy and Charcot-Marie-Tooth disease. It is also one of the two module genes represented in the hu.MAP complex annotation (hu.MAP huMAP3_11232.1).
- **Conclusion**: Established evidence supports DNM2 as a major membrane-trafficking and muscle-disease gene, with limited complex-context support from (hu.MAP huMAP3_11232.1). Its co-abundance with SLC27A6 does not demonstrate a direct interaction. A reasonable hypothesis is that both respond to a shared membrane or energetic state.

#### PDCD6IP

- **Related proteins** (co-abundance neighbors): SLC27A6 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 6 interacting protein. This gene encodes a protein that functions within the ESCRT pathway in the abscission stage of cytokinesis, in intralumenal endosomal vesicle formation, and in enveloped virus budding. Studies using mouse cells have shown that overexpression of this protein can block apoptosis. In addition, the product of this gene binds to the product of the PDCD6 gene, a protein required for apoptosis, in a calc…
- **Diseases (Open Targets)**: HIV infectious disease (0.463); anthrax infection (0.462); alcohol drinking (0.388); autosomal recessive primary microcephaly (0.386); microcephaly 29, primary, autosomal recessive (0.383)
- **Europe PMC papers**: 1668
- **Why important**: PDCD6IP is directly connected to SLC27A6 and encodes an ESCRT-associated factor involved in cytokinetic abscission, intralumenal endosomal-vesicle formation, viral budding, and membrane organization. HPA places it in vesicles and describes intracellular and membrane-associated secretome localization. It has broad literature coverage and disease associations involving primary microcephaly and infection-related traits.
- **Conclusion**: Established evidence supports PDCD6IP as a vesicle and membrane-remodeling factor. Its detection in colon but not heart argues against assuming identical protein-level behavior in the two tissues. The module supports, at most, a hypothesis of shared regulation with lipid transport and trafficking.

#### EIF3C

- **Related proteins** (co-abundance neighbors): SLC27A6 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in colon, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C is directly connected to the hub and is a component of the eukaryotic translation-initiation complex. Its established functions include ribosome binding, translational initiation, and positive regulation of translation. It is detected in both tissues, has broad neural and glial cell-type enhancement, and has the deepest literature coverage among the selected genes, although its disease associations in this fact sheet are less specific.
- **Conclusion**: Established evidence supports EIF3C as a general protein-synthesis factor rather than a tissue-specific effector. Its presence may indicate shared translational demand or cellular state. The data do not show that translation initiation is a primary function of the module, because no GO or KEGG term passed global correction.

## Module 1

**Tissue pair**: colon and heart  
**Genes (6)**: ACO2, CS, COQ9, ETFA, MECR, MYOM2

### Function

The module is most consistent with mitochondrial energy metabolism in muscle-associated tissue, coupled to sarcomere structure. CS and ACO2 are established tricarboxylic-acid-cycle enzymes; ETFA supports mitochondrial fatty-acid and amino-acid oxidation; COQ9 supports ubiquinone biosynthesis; MECR supports mitochondrial fatty-acid synthesis; and MYOM2 is a sarcomeric M-band protein. The network places MYOM2 at the center of the co-abundance pattern, with the metabolic genes linked to it. However, no GO or KEGG term passed global correction, so this functional interpretation is based on the convergent gene annotations, tissue evidence, and network architecture rather than statistically significant enrichment. There are no supplementary STRING-enrichment terms either.

**Cell composition.** The module is not composed of secreted or plasma proteins and does not show a blood-cell-enriched pattern. All module proteins were detected in both colon and heart. Most genes have tissue-enhanced expression in skeletal muscle, tongue, or heart muscle, while the remaining genes are broadly expressed or show cell-type enhancement in specialized cells. The low immune-cell specificity across the module argues against an immune or blood-contamination explanation. The shared colon-heart signal therefore more plausibly reflects mitochondrial abundance and muscle-associated cellular programs, although tissue composition and shared cell types could contribute.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only listed high-confidence STRING relationship is between CS and ACO2, which is biologically coherent because both are enzymes in the tricarboxylic acid cycle. The other module relationships are not represented by high-confidence STRING links in the supplied evidence. No STRING functional-enrichment terms were reported. No hu.MAP complex contains multiple module members. Thus, the co-abundance module extends beyond a documented physical complex and should not be interpreted as a confirmed protein complex. Its structure is instead compatible with coordinated abundance of a sarcomeric scaffold and mitochondrial metabolic proteins, with the CS–ACO2 link providing limited independent support.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: ACO2–CS (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a biologically informative co-abundance pattern, but it cannot be called a definitively new molecular pathway. The absence of a hu.MAP complex and the sparse STRING support indicate that most of the module is not already represented as a known physical interaction group. That supports novelty at the level of a shared colon-heart co-abundance module, while not proving novel molecular interactions. The established functions of the individual genes and the known CS–ACO2 relationship provide alternative explanations, including coordinated mitochondrial abundance, muscle-cell composition, or shared metabolic state. The lack of globally significant GO or KEGG enrichment limits the strength of any claim that the module defines a previously unrecognized pathway.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of mitochondria and contractile muscle-associated material across colon and heart samples. MYOM2 may mark the muscle or sarcomeric component, while CS, ACO2, ETFA, COQ9, and MECR represent complementary mitochondrial pathways involving the tricarboxylic acid cycle, respiratory electron supply, fatty-acid handling, and ubiquinone production. In this model, the co-abundance signal arises primarily from shared cellular composition or mitochondrial content rather than direct binding among all module proteins. Testing this would require cell-resolved measurements, mitochondrial-content markers, and targeted assessment of whether the metabolic genes covary after controlling for muscle-cell abundance.

### Important genes

#### MYOM2

- **Related proteins** (co-abundance neighbors): CS (0.88), COQ9 (0.88), MECR (0.87), ACO2 (0.85), ETFA (0.85); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Mitochondria; IHC detected in colon, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myomesin 2. The giant protein titin, together with its associated proteins, interconnects the major structure of sarcomeres, the M bands and Z discs. The C-terminal end of the titin string extends into the M line, where it binds tightly to M-band constituents of apparent molecular masses of 190 kD and 165 kD. The predicted MYOM2 protein contains 1,465 amino acids. Like MYOM1, MYOM2 has a unique N-terminal dom…
- **Diseases (Open Targets)**: alcohol drinking (0.407); infectious meningitis (0.360); trauma complication (0.303); breast benign neoplasm (0.303); Alzheimer disease (0.303)
- **Europe PMC papers**: 2384
- **Why important**: MYOM2 is the central network node, connecting to every other module member in the supplied co-abundance graph. Its HPA profile is enriched in heart and skeletal muscle and in cardiomyocytes and myonuclei, and its established function is organization of the sarcomere and M-band. It therefore provides the strongest link between the network structure and a muscle-associated biological context. It also has substantial literature coverage and reported associations with several disease contexts.
- **Conclusion**: Established evidence supports MYOM2 as a muscle-sarcomere structural protein and as the principal co-abundance organizer of this module. It is plausible, but not established, that MYOM2 abundance is acting as a marker of muscle-cell or contractile-material abundance that brings the mitochondrial genes into the shared module.

#### CS

- **Related proteins** (co-abundance neighbors): MYOM2 (0.88); STRING partners: ACO2 (0.999)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in colon, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS is a core mitochondrial matrix enzyme that catalyzes citrate formation at the entry of the tricarboxylic acid cycle. It is tissue-enhanced in skeletal muscle and tongue, is detected in both relevant tissues, and has extensive literature coverage. It is also one member of the only high-confidence STRING pair in the module, linking it to ACO2 through a coherent metabolic pathway.
- **Conclusion**: Established evidence supports CS as a mitochondrial oxidative-metabolism marker and as a plausible contributor to the module's metabolic interpretation. Its association with MYOM2 in the co-abundance graph should not be treated as proof of direct binding; coordinated mitochondrial or muscle abundance is an alternative explanation.

#### ACO2

- **Related proteins** (co-abundance neighbors): MYOM2 (0.85); STRING partners: CS (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in colon, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aconitase 2. The protein encoded by this gene belongs to the aconitase/IPM isomerase family. It is an enzyme that catalyzes the interconversion of citrate to isocitrate via cis-aconitate in the second step of the TCA cycle. This protein is encoded in the nucleus and functions in the mitochondrion. It was found to be one of the mitochondrial matrix proteins that are preferentially degraded by the serine proteas…
- **Diseases (Open Targets)**: infantile cerebellar-retinal degeneration (0.814); optic atrophy 9 (0.693); autosomal dominant optic atrophy, classic form (0.619); optic atrophy (0.601); mitochondrial disease (0.505)
- **Europe PMC papers**: 3559
- **Why important**: ACO2 catalyzes the conversion of citrate to isocitrate in the mitochondrial tricarboxylic acid cycle and is enriched in heart muscle, skeletal muscle, and tongue. It is detected in both tissues, has substantial literature coverage, and forms the documented high-confidence STRING relationship with CS. Its disease associations also connect mitochondrial metabolism with neurodegenerative and optic-atrophy phenotypes.
- **Conclusion**: Established evidence supports ACO2 as a central mitochondrial oxidative-metabolism enzyme and strengthens the interpretation of the CS–ACO2 portion of the module. The module data support coordinated abundance with MYOM2 and the other metabolic genes, but do not establish a new ACO2 interaction or a disease mechanism.

#### COQ9

- **Related proteins** (co-abundance neighbors): MYOM2 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in colon, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coenzyme Q9. This locus represents a mitochondrial ubiquinone biosynthesis gene. The encoded protein is likely necessary for biosynthesis of coenzyme Q10, as mutations at this locus have been associated with autosomal-recessive neonatal-onset primary coenzyme Q10 deficiency.[provided by RefSeq, Sep 2010].
- **Diseases (Open Targets)**: encephalopathy-hypertrophic cardiomyopathy-renal tubular disease syndrome (0.766); coenzyme Q10 deficiency (0.635); hereditary disease (0.415); mitochondrial disease (0.372); coenzyme Q10 deficiency, primary, 1 (0.370)
- **Europe PMC papers**: 958
- **Why important**: COQ9 is a mitochondrial ubiquinone-biosynthesis protein and is associated with primary coenzyme Q deficiency and a syndrome involving hypertrophic cardiomyopathy and renal disease. It is tissue-enhanced in skeletal muscle and tongue, detected in both tissues, and provides a mechanistically important connection between mitochondrial respiratory capacity and cardiac biology. Its literature volume is more limited than that of CS or ACO2, making its inclusion particularly informative for a focused hypothesis.
- **Conclusion**: Established evidence supports COQ9 as a mitochondrial coenzyme-Q biosynthesis factor with clinically relevant deficiency phenotypes. Its co-abundance with the module is consistent with coordinated respiratory metabolism, but the supplied data do not establish that COQ9 is a driver of the shared colon-heart pattern.

#### ETFA

- **Related proteins** (co-abundance neighbors): MYOM2 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in colon, heart
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein subunit alpha. ETFA participates in catalyzing the initial step of the mitochondrial fatty acid beta-oxidation. It shuttles electrons between primary flavoprotein dehydrogenases and the membrane-bound electron transfer flavoprotein ubiquinone oxidoreductase. Defects in electron-transfer-flavoprotein have been implicated in type II glutaricaciduria in which multiple acyl-CoA dehydrogenase deficiencies result in l…
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.834); glutaric aciduria (0.756); hereditary disease (0.469); multiple acyl-CoA dehydrogenase deficiency, mild type (0.370); multiple acyl-CoA dehydrogenase deficiency, severe neonatal type (0.370)
- **Europe PMC papers**: 1433
- **Why important**: ETFA transfers electrons from several mitochondrial dehydrogenases toward the respiratory chain and supports fatty-acid and amino-acid catabolism. It is tissue-enhanced in liver and tongue, detected in both relevant tissues, and has well-established disease associations with multiple acyl-CoA dehydrogenase deficiency. Its presence broadens the module beyond the tricarboxylic acid cycle to mitochondrial substrate oxidation.
- **Conclusion**: Established evidence supports ETFA as a mitochondrial electron-transfer and substrate-oxidation component. Its module association is compatible with a generalized mitochondrial abundance program, while the data do not show that ETFA directly interacts with MYOM2 or any other module member.

