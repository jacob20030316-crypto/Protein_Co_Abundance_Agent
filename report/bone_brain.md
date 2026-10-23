# Conserved co-abundance modules: bone and brain

## Module 0

**Tissue pair**: bone and brain  
**Genes (45)**: PPP2R5D, AAK1, GOT1, ALDOC, AMPD2, ATG7, CAP2, CLASP2, CNDP2, CUL2, DCTN1, DCTN5, DNM1L, DUSP3, DYNC1H1, DNM1, GSPT2, EXOC1, GFUS, AGL, RAP1GDS1, GNL1, GNPDA2, CAMK2G, KIF3B, LANCL2, MAP1A, MARK2, NCKAP1, NDUFA13, NUDT3, PAK1, PFKM, PDXP, PPP3CA, PREPL, PTPN23, PYGB, SLK, TCP11L1, TKFC, VAC14, ATP6V1A, ATP6V1C1, ATP6V1H

### Function

The strongest interpretation is a cytosolic, phosphorylation-sensitive module coupling energy and phosphate metabolism to vesicle trafficking, synaptic secretion, cytoskeletal transport, autophagy, and intracellular acidification. The primary evidence is the globally corrected enrichment for phosphorus metabolic process (GO:BP phosphorus metabolic process; q_global = 0.00301), phosphate-containing compound metabolic process (GO:BP phosphate-containing compound metabolic process; q_global = 0.00301), cytosol (GO:CC cytosol; q_global = 0.00332), phagocytosis (KEGG Phagocytosis - Homo sapiens (human); q_global = 0.00886), vesicle-mediated transport in synapse (GO:BP vesicle-mediated transport in synapse; q_global = 0.0223), secretion by cell (GO:BP secretion by cell; q_global = 0.032), histone modifying activity (GO:MF histone modifying activity; q_global = 0.0445), export from cell (GO:BP export from cell; q_global = 0.0479), and the V-type ATPase V1-domain terms (GO:CC vacuolar proton-transporting V-type ATPase, V1 domain; q_global = 0.0483), (GO:CC proton-transporting two-sector ATPase complex, catalytic domain; q_global = 0.0483), and (GO:CC proton-transporting V-type ATPase, V1 domain; q_global = 0.0483). The convergence of glycolytic and glycogen-related genes, kinases and phosphatases, dynamin and motor proteins, exocytic machinery, autophagy machinery, and V-ATPase subunits supports a coordinated intracellular trafficking and metabolic-support function rather than a single narrowly defined pathway. The phagocytosis result (KEGG Phagocytosis - Homo sapiens (human); q_global = 0.00886) should be interpreted broadly as evidence for conserved vesicle, membrane-remodelling, and lysosomal machinery, not as proof that the module represents phagocytic cells.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the module is dominated by intracellular proteins. Most genes have low tissue specificity, while many are detected in brain and several are brain- or neuron-enhanced, including DNM1, MAP1A, DYNC1H1, PAK1, PPP3CA, CLASP2, ALDOC, PDXP, and AMPD2. The HPA profile also contains skeletal-muscle, retinal, glial, and neuronal signals. Some genes are enhanced in neutrophils or other myeloid cells, and STRING supplementary terms include immune and innate immune system annotations (STRING RCTM Immune System; within-query FDR = 0.0016) and (STRING RCTM Innate Immune System; within-query FDR = 0.0056). However, the module-wide HPA summary indicates broadly low immune cell specificity, so blood-cell contamination is a possible contributor but is not the most compelling overall explanation. A shared neuronal or metabolically active cytoskeletal program, potentially mixed with common immune or stromal cell content in tissue samples, is more consistent with the combined evidence.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP phosphorus metabolic process | 0.00301 | AAK1, ALDOC, AMPD2, ATP6V1A, CAMK2G, DNM1L, DUSP3, GFUS, GNPDA2, GOT1, MARK2, NDUFA13, NUDT3, PAK1, PDXP, PFKM, PPP3CA, PTPN23, SLK, TKFC, VAC14 |
| GO:BP phosphate-containing compound metabolic process | 0.00301 | AAK1, ALDOC, AMPD2, ATP6V1A, CAMK2G, DNM1L, DUSP3, GFUS, GNPDA2, GOT1, MARK2, NDUFA13, NUDT3, PAK1, PDXP, PFKM, PPP3CA, PTPN23, SLK, TKFC, VAC14 |
| GO:CC cytosol | 0.00332 | AAK1, AGL, ALDOC, AMPD2, ATG7, ATP6V1A, ATP6V1C1, ATP6V1H, CAMK2G, CLASP2, CNDP2, CUL2, DCTN1, DCTN5, DNM1L, DUSP3, DYNC1H1, EXOC1, GFUS, GNPDA2, GOT1, GSPT2, KIF3B, LANCL2, MAP1A, NCKAP1, NUDT3, PAK1, PDXP, PFKM, PPP2R5D, PPP3CA, PREPL, PTPN23, RAP1GDS1, SLK, TKFC, VAC14 |
| KEGG Phagocytosis - Homo sapiens (human) | 0.00886 | ATG7, ATP6V1A, ATP6V1C1, ATP6V1H, DCTN1, DCTN5, DNM1, DYNC1H1 |
| GO:BP vesicle-mediated transport in synapse | 0.0223 | AAK1, ATP6V1A, ATP6V1C1, DNM1, PPP3CA, PREPL, VAC14 |
| GO:BP secretion by cell | 0.032 | CAMK2G, CLASP2, DNM1L, EXOC1, PAK1, PFKM, PPP3CA, PREPL, PTPN23, RAP1GDS1 |
| GO:MF histone modifying activity | 0.0445 | AAK1, DUSP3, MARK2, PAK1, PDXP, PPP3CA, PTPN23, SLK |
| GO:BP export from cell | 0.0479 | CAMK2G, CLASP2, DNM1L, EXOC1, PAK1, PFKM, PPP3CA, PREPL, PTPN23, RAP1GDS1 |
| GO:CC vacuolar proton-transporting V-type ATPase, V1 domain | 0.0483 | ATP6V1A, ATP6V1C1, ATP6V1H |
| GO:CC proton-transporting two-sector ATPase complex, catalytic domain | 0.0483 | ATP6V1A, ATP6V1C1, ATP6V1H |
| GO:CC proton-transporting V-type ATPase, V1 domain | 0.0483 | ATP6V1A, ATP6V1C1, ATP6V1H |

### STRING and hu.MAP

STRING supports several concrete substructures already known in molecular biology. ATP6V1A, ATP6V1C1, and ATP6V1H form a strongly supported V-ATPase V1 relationship; DCTN1, DCTN5, and DYNC1H1 form a dynactin-dynein transport relationship; AGL, PYGB, PFKM, and ALDOC connect glycogen handling with glycolysis; and CLASP2 connects with MARK2 and DCTN1 in a microtubule-associated group. PPP2R5D and PPP3CA also have a supported phosphatase relationship. These edges mean that part of the module recapitulates established complexes and biochemical partnerships rather than being an entirely uncharacterized network. hu.MAP independently supports recurring assemblies involving CLASP2 and MARK2 (hu.MAP huMAP3_02924.1), (hu.MAP huMAP3_03180.1), (hu.MAP huMAP3_09979.1), (hu.MAP huMAP3_07247.1), (hu.MAP huMAP3_10707.1), and (hu.MAP huMAP3_09810.1); ATP6V1A and ATP6V1C1 (hu.MAP huMAP3_05070.1), (hu.MAP huMAP3_07099.1), (hu.MAP huMAP3_07329.1) through (hu.MAP huMAP3_10511.1), (hu.MAP huMAP3_12042.1); AGL and PYGB (hu.MAP huMAP3_08013.1) through (hu.MAP huMAP3_06909.1), (hu.MAP huMAP3_01396.1), (hu.MAP huMAP3_08093.1) through (hu.MAP huMAP3_13075.1), (hu.MAP huMAP3_11993.1), and (hu.MAP huMAP3_12186.1); DCTN1 and DCTN5 (hu.MAP huMAP3_04946.1), (hu.MAP huMAP3_09952.1), and (hu.MAP huMAP3_12900.1); and GNL1 with TKFC (hu.MAP huMAP3_08533.1). The remaining co-abundance links are not necessarily direct physical interactions, and STRING supplementary enrichment should be treated as supportive context rather than global enrichment evidence.

**STRING interactions (score >= 0.7)**: 14 of 990 gene pairs: AGL–PYGB (0.999); ALDOC–PFKM (0.977); ALDOC–TKFC (0.915); ATG7–MAP1A (0.866); ATP6V1A–ATP6V1C1 (0.999); ATP6V1A–ATP6V1H (0.999); ATP6V1C1–ATP6V1H (0.999); CLASP2–DCTN1 (0.77); CLASP2–MARK2 (0.794); DCTN1–DCTN5 (0.999); DCTN1–DYNC1H1 (0.999); DCTN5–DYNC1H1 (0.991); PFKM–PYGB (0.736); PPP2R5D–PPP3CA (0.722)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Cytosol (FDR = 0.0011, 38 genes); RCTM Immune System (FDR = 0.0016, 21 genes); Process Phosphorus metabolic process (FDR = 0.0048, 20 genes); RCTM Innate Immune System (FDR = 0.0056, 15 genes); COMPARTMENTS Cytosol (FDR = 0.0262, 29 genes); Process Phosphate-containing compound metabolic process (FDR = 0.0327, 18 genes); TISSUES Brain (FDR = 0.0422, 36 genes); TISSUES Head (FDR = 0.0422, 37 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02924.1 (CLASP2, MARK2; 2/3); huMAP3_03180.1 (CLASP2, MARK2; 2/4); huMAP3_05070.1 (ATP6V1C1, ATP6V1A; 2/4); huMAP3_09979.1 (CLASP2, MARK2; 2/5); huMAP3_07247.1 (CLASP2, MARK2; 2/6); huMAP3_10707.1 (CLASP2, MARK2; 2/6); huMAP3_08013.1 (PYGB, AGL; 2/8); huMAP3_06909.1 (PYGB, AGL; 2/9); huMAP3_08533.1 (GNL1, TKFC; 2/9); huMAP3_01396.1 (PYGB, AGL; 2/10); huMAP3_04946.1 (DCTN1, DCTN5; 2/12); huMAP3_08093.1 (PYGB, AGL; 2/12); huMAP3_10227.1 (PYGB, AGL; 2/14); huMAP3_09760.1 (PYGB, AGL; 2/15); huMAP3_13075.1 (PYGB, AGL; 2/15); huMAP3_09952.1 (DCTN1, DCTN5; 2/16); huMAP3_07099.1 (ATP6V1C1, ATP6V1A; 2/18); huMAP3_11993.1 (PYGB, AGL; 2/20); huMAP3_07329.1 (ATP6V1C1, ATP6V1A; 2/20); huMAP3_08381.1 (ATP6V1C1, ATP6V1A; 2/20); huMAP3_09242.1 (ATP6V1C1, ATP6V1A; 2/20); huMAP3_05805.1 (ATP6V1C1, ATP6V1A; 2/21); huMAP3_08678.1 (ATP6V1C1, ATP6V1A; 2/22); huMAP3_12186.1 (PYGB, AGL; 2/23); huMAP3_09873.1 (ATP6V1C1, ATP6V1A; 2/24); huMAP3_09477.1 (ATP6V1C1, ATP6V1A; 2/26); huMAP3_13872.1 (ATP6V1C1, ATP6V1A; 2/29); huMAP3_10516.1 (ATP6V1C1, ATP6V1A; 2/31); huMAP3_10511.1 (ATP6V1C1, ATP6V1A; 2/35); huMAP3_12900.1 (DCTN1, DCTN5; 2/50); huMAP3_09810.1 (CLASP2, MARK2; 2/56); huMAP3_12042.1 (ATP6V1C1, ATP6V1A; 2/56)

### Novelty

The module is unlikely to be a wholly new molecular complex because several of its strongest relationships are already represented in STRING and hu.MAP, including the V-ATPase, dynactin-dynein, glycogen-metabolism, and microtubule-associated relationships. Nevertheless, the tissue-pair co-abundance organization may still be novel: the fact sheet does not establish that this exact gene combination, cross-tissue conservation, or bone-brain co-abundance pattern has previously been reported. Absence of some genes from STRING or hu.MAP is not evidence of novelty, because those resources emphasize physical interactions and curated complexes rather than tissue-specific co-abundance. The defensible conclusion is that the module provides a potentially novel systems-level association built partly from known molecular machinery, requiring validation in independent bone and brain datasets and with cell-type-aware analysis.

**Hypothesis.** Hypothesis: in bone and brain cells, coordinated abundance of glycolytic and glycogen enzymes supplies ATP and phosphate intermediates for kinase and phosphatase control of microtubules, membrane trafficking, and secretion. V-ATPase activity could acidify endosomal, lysosomal, and synaptic compartments, while dynamin, dynactin, kinesin, exocyst, and autophagy components move and recycle cargo. Calcium-sensitive PPP3CA and kinase regulators such as PAK1, MARK2, AAK1, and CAMK2G may couple activity-dependent signaling to cytoskeletal remodeling and vesicle release. In bone, the same program could reflect metabolically active or vesicle-trafficking cells rather than neuronal synapses. This is a mechanistic model, not a demonstrated causal pathway; it should be tested by measuring cell-type composition, organelle acidification, glycolytic state, and vesicle trafficking in matched bone and brain samples.

### Important genes

#### PAK1

- **Related proteins** (co-abundance neighbors): MARK2 (0.88), DNM1 (0.85), NUDT3 (0.85), PFKM (0.84), GFUS (0.83), TKFC (0.82), VAC14 (0.80), PPP3CA (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: p21 (RAC1) activated kinase 1. This gene encodes a family member of serine/threonine p21-activating kinases, known as PAK proteins. These proteins are critical effectors that link RhoGTPases to cytoskeleton reorganization and nuclear signaling, and they serve as targets for the small GTP binding proteins Cdc42 and Rac. This specific family member regulates cell motility and morphology. Mutations in this gene have been associate…
- **Diseases (Open Targets)**: intellectual developmental disorder with macrocephaly, seizures, and speech delay (0.712); neurodevelopmental disorder (0.477); hereditary disease (0.339); cutaneous melanoma (0.187); Myoclonus (0.187)
- **Europe PMC papers**: 9937
- **Why important**: PAK1 is among the more connected module genes and links MARK2, DNM1, NUDT3, PFKM, GFUS, TKFC, VAC14, and PPP3CA in the co-abundance graph. It appears in many primary globally corrected terms, including phosphorus metabolism (GO:BP phosphorus metabolic process; q_global = 0.00301), phosphate-containing compound metabolism (GO:BP phosphate-containing compound metabolic process; q_global = 0.00301), secretion (GO:BP secretion by cell; q_global = 0.032), and export from cell (GO:BP export from cell; q_global = 0.0479). Its established function as a RhoGTPase-responsive kinase connecting cytoskeletal remodeling with signaling provides a plausible regulatory bridge between metabolism, membrane dynamics, and secretion. HPA reports brain enhancement and cell-type enhancement in mast cells and neutrophils, while disease resources associate it with a neurodevelopmental disorder involving macrocephaly, seizures, and speech delay. It also has a large literature base.
- **Conclusion**: Established: PAK1 is a signaling and cytoskeletal regulator with strong module connectivity, broad primary enrichment support, brain expression, and disease relevance. Hypothesis: PAK1 may act as a central activity- or cell-state-sensitive controller that couples metabolic status to vesicle trafficking in the conserved bone-brain module.

#### DNM1

- **Related proteins** (co-abundance neighbors): PFKM (0.86), PAK1 (0.85), TCP11L1 (0.84), ATP6V1C1 (0.81), PREPL (0.81), RAP1GDS1 (0.81), MAP1A (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 1. This gene encodes a member of the dynamin subfamily of GTP-binding proteins. The encoded protein possesses unique mechanochemical properties used to tubulate and sever membranes, and is involved in clathrin-mediated endocytosis and other vesicular trafficking processes. Actin and other cytoskeletal proteins act as binding partners for the encoded protein, which can also self-assemble leading to st…
- **Diseases (Open Targets)**: Lennox-Gastaut syndrome (0.733); developmental and epileptic encephalopathy, 31A (0.731); developmental and epileptic encephalopathy, 31B (0.615); hereditary disease (0.533); Epileptic encephalopathy (0.488)
- **Europe PMC papers**: 2657
- **Why important**: DNM1 is brain tissue enriched and enhanced in excitatory and inhibitory neurons and is not detected in immune cells according to HPA. It is connected in the module to PFKM, PAK1, TCP11L1, ATP6V1C1, PREPL, RAP1GDS1, and MAP1A. It is part of the globally corrected phagocytosis and synaptic vesicle transport terms (KEGG Phagocytosis - Homo sapiens (human); q_global = 0.00886) and (GO:BP vesicle-mediated transport in synapse; q_global = 0.0223). Its established dynamin GTPase function in membrane scission, receptor endocytosis, and synaptic vesicle budding, together with strong epilepsy and developmental disease associations, makes it a direct functional anchor for the trafficking interpretation.
- **Conclusion**: Established: DNM1 provides strong neuronal and vesicle-trafficking support and helps connect the module to synaptic membrane recycling. Hypothesis: coordinated DNM1 abundance may indicate regulated endocytic demand or synaptic-like vesicle turnover in both tissues, although a neuronal interpretation cannot be assumed for bone without cell-type validation.

#### ATP6V1A

- **Related proteins** (co-abundance neighbors): GOT1 (0.82); STRING partners: ATP6V1C1 (0.999), ATP6V1H (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_05070.1, huMAP3_07099.1, huMAP3_07329.1, huMAP3_08381.1, huMAP3_09242.1, huMAP3_05805.1, huMAP3_08678.1, huMAP3_09873.1, huMAP3_09477.1, huMAP3_13872.1, huMAP3_10516.1, huMAP3_10511.1, huMAP3_12042.1
- **Function (MyGene.info)**: ATPase H+ transporting V1 subunit A. This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 d…
- **Diseases (Open Targets)**: genetic developmental and epileptic encephalopathy (0.735); developmental and epileptic encephalopathy 93 (0.696); neurodegenerative disease (0.573); Alzheimer disease (0.519); Parkinson disease (0.499)
- **Europe PMC papers**: 1447
- **Why important**: ATP6V1A is a core V-ATPase V1 subunit and is connected in STRING to ATP6V1C1 and ATP6V1H. It contributes to the cytosol, phagocytosis, synaptic vesicle transport, and all three globally corrected V-ATPase terms (GO:CC cytosol; q_global = 0.00332), (KEGG Phagocytosis - Homo sapiens (human); q_global = 0.00886), (GO:BP vesicle-mediated transport in synapse; q_global = 0.0223), (GO:CC vacuolar proton-transporting V-type ATPase, V1 domain; q_global = 0.0483), (GO:CC proton-transporting two-sector ATPase complex, catalytic domain; q_global = 0.0483), and (GO:CC proton-transporting V-type ATPase, V1 domain; q_global = 0.0483). hu.MAP repeatedly places it with ATP6V1C1 in V-ATPase-related complexes (hu.MAP huMAP3_05070.1), (hu.MAP huMAP3_07099.1), (hu.MAP huMAP3_07329.1) through (hu.MAP huMAP3_10511.1), and (hu.MAP huMAP3_12042.1). Its established role in organelle acidification, protein sorting, receptor endocytosis, autophagy, and synaptic vesicle proton-gradient generation is central to the module's trafficking interpretation. It is associated with developmental epileptic encephalopathy and neurodegenerative disease.
- **Conclusion**: Established: ATP6V1A is a molecularly supported V-ATPase component and one of the clearest functional anchors of the module. Hypothesis: variation in the module may reflect coordinated control of endosomal, lysosomal, or vesicle acidification, linking metabolic activity to cargo processing in bone and brain.

#### MARK2

- **Related proteins** (co-abundance neighbors): PAK1 (0.88), AAK1 (0.86), RAP1GDS1 (0.85), TCP11L1 (0.84), TKFC (0.84), PFKM (0.81), PREPL (0.81), GNL1 (0.81); STRING partners: CLASP2 (0.794)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_02924.1, huMAP3_03180.1, huMAP3_09979.1, huMAP3_07247.1, huMAP3_10707.1, huMAP3_09810.1
- **Function (MyGene.info)**: microtubule affinity regulating kinase 2. This gene encodes a member of the Par-1 family of serine/threonine protein kinases. The protein is an important regulator of cell polarity in epithelial and neuronal cells, and also controls the stability of microtubules through phosphorylation and inactivation of several microtubule-associating proteins. The protein localizes to cell membranes. Multiple transcript variants encoding different isof…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 76 (0.661); autism spectrum disorder (0.570); Intellectual disability (0.408); neurodegenerative disease (0.375); complex neurodevelopmental disorder (0.370)
- **Europe PMC papers**: 1689
- **Why important**: MARK2 has substantial module connectivity and links PAK1, AAK1, RAP1GDS1, TCP11L1, TKFC, PFKM, PREPL, and GNL1. It contributes to phosphorus metabolism (GO:BP phosphorus metabolic process; q_global = 0.00301) and (GO:BP phosphate-containing compound metabolic process; q_global = 0.00301) and histone modifying activity (GO:MF histone modifying activity; q_global = 0.0445). STRING supports its relationship with CLASP2, while hu.MAP repeatedly places MARK2 and CLASP2 in related complexes (hu.MAP huMAP3_02924.1), (hu.MAP huMAP3_03180.1), (hu.MAP huMAP3_09979.1), (hu.MAP huMAP3_07247.1), (hu.MAP huMAP3_10707.1), and (hu.MAP huMAP3_09810.1). Its established role as a Par-1 family kinase regulating cell polarity and microtubule stability is particularly relevant to long-range intracellular transport. HPA reports brain detection and neutrophil enhancement, and disease resources associate it with intellectual developmental disorders, autism spectrum disorder, and neurodegenerative disease.
- **Conclusion**: Established: MARK2 is a kinase and polarity regulator embedded in a cytoskeletal subnetwork supported by both STRING and hu.MAP. Hypothesis: MARK2 may coordinate microtubule organization with metabolic and trafficking state, helping explain why the module is conserved across tissues with different cell types.

#### PFKM

- **Related proteins** (co-abundance neighbors): DNM1 (0.86), ATP6V1C1 (0.85), PAK1 (0.84), CNDP2 (0.83), MARK2 (0.81), ALDOC (0.81), PDXP (0.80); STRING partners: ALDOC (0.977), PYGB (0.736)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphofructokinase, muscle. Three phosphofructokinase isozymes exist in humans: muscle, liver and platelet. These isozymes function as subunits of the mammalian tetramer phosphofructokinase, which catalyzes the phosphorylation of fructose-6-phosphate to fructose-1,6-bisphosphate. Tetramer composition varies depending on tissue type. This gene encodes the muscle-type isozyme. Mutations in this gene have been associated with g…
- **Diseases (Open Targets)**: glycogen storage disease VII (0.819); disorder of glycogen metabolism (0.372); peroxisome biogenesis disorder (0.333); neurodegenerative disease (0.319); anemia (phenotype) (0.288)
- **Europe PMC papers**: 2506
- **Why important**: PFKM connects DNM1, ATP6V1C1, PAK1, CNDP2, MARK2, ALDOC, and PDXP. It appears in the primary phosphorus and phosphate-containing compound terms (GO:BP phosphorus metabolic process; q_global = 0.00301) and (GO:BP phosphate-containing compound metabolic process; q_global = 0.00301), as well as secretion and export terms (GO:BP secretion by cell; q_global = 0.032) and (GO:BP export from cell; q_global = 0.0479). STRING supports relationships with ALDOC, TKFC, and PYGB, linking glycolysis with glycogen metabolism. Its established role as the muscle-type phosphofructokinase makes it a direct indicator of glycolytic capacity, and its association with glycogen storage disease provides disease relevance. HPA reports enrichment in skeletal muscle and tongue, with detection in brain.
- **Conclusion**: Established: PFKM supplies a metabolic explanation for the module and connects to both energy-related and trafficking-related genes. Hypothesis: glycolytic flux may support ATP-intensive vesicle transport and organelle acidification, but the co-abundance data do not prove that PFKM activity drives the other module processes.

#### PREPL

- **Related proteins** (co-abundance neighbors): RAP1GDS1 (0.88), AAK1 (0.84), CNDP2 (0.82), GOT1 (0.82), EXOC1 (0.82), TCP11L1 (0.81), DNM1 (0.81), MARK2 (0.81), PPP2R5D (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prolyl endopeptidase like. The protein encoded by this gene belongs to the prolyl oligopeptidase subfamily of serine peptidases. Mutations in this gene have been associated with hypotonia-cystinuria syndrome, also known as the 2p21 deletion syndrome. Several alternatively spliced transcript variants encoding either the same or different isoforms have been described for this gene.[provided by RefSeq, Jan 2010].
- **Diseases (Open Targets)**: myasthenic syndrome, congenital, 22 (0.581); cystinuria (0.567); hypotonia-cystinuria syndrome (0.550); Hypotonia - cystinuria syndrome (0.510); premature menopause (0.416)
- **Europe PMC papers**: 4024
- **Why important**: PREPL is highly connected to RAP1GDS1, AAK1, CNDP2, GOT1, EXOC1, TCP11L1, DNM1, and MARK2. It appears in the primary cytosol, synaptic vesicle transport, secretion, and export terms (GO:CC cytosol; q_global = 0.00332), (GO:BP vesicle-mediated transport in synapse; q_global = 0.0223), (GO:BP secretion by cell; q_global = 0.032), and (GO:BP export from cell; q_global = 0.0479). Its established annotations include proteolysis, endosome-to-Golgi transport, Golgi-to-plasma-membrane transport, and regulation of synaptic vesicle exocytosis. HPA reports enhancement in brain inhibitory neurons, and human disease associations include congenital myasthenic syndrome, cystinuria, and hypotonia-cystinuria syndrome. It also has a substantial literature base.
- **Conclusion**: Established: PREPL is a trafficking-linked enzyme-like protein with strong network position and direct relevance to exocytosis and intracellular transport. Hypothesis: PREPL may help connect endomembrane cargo handling with neuronal or muscle-like secretory demands in the shared module.

## Module 1

**Tissue pair**: bone and brain  
**Genes (31)**: ABLIM1, SLC25A4, CNN1, CNPY3, CYSTM1, EHD1, FAM241B, FUNDC2, MCM3AP, GDAP1, GOLGA7, GPC1, JUND, LMO7, LRP1, APOOL, NDUFA10, PARVA, PIP5K1A, JUP, PRNP, SLC25A12, SFT2D2, SMIM20, SPTBN1, SPTLC2, SYNPO, TMEM209, FAS, TSTD1, UQCC1

### Function

The strongest supported function is organization and trafficking of proteins at the cell surface. (GO:BP protein localization to membrane; q_global = 0.0356) identifies protein localization to membrane, and (GO:BP protein localization to plasma membrane; q_global = 0.0369) identifies protein localization to the plasma membrane; these are the only GO/KEGG terms that passed global correction. The contributing genes include EHD1, GOLGA7, GPC1, JUP, LRP1, PIP5K1A, PRNP and SPTBN1. Their annotations support a broader membrane-interface program involving endocytic recycling, Golgi-to-plasma-membrane transport, cell adhesion, actin-linked membrane organization and receptor-mediated uptake. Mitochondrial energy and membrane maintenance are also represented, particularly through NDUFA10, SLC25A4, SLC25A12, GDAP1, APOOL, SMIM20 and UQCC1, but these are supporting biological themes rather than globally significant enrichment results. No GO/KEGG term passed within-module correction. The absence of additional globally significant terms does not invalidate the module.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: most genes are intracellular, membrane, cytoskeletal or mitochondrial proteins, while only a minority are annotated as secreted to blood. The HPA profile instead indicates a mixed cellular signal. Many genes have cell-type-enhanced expression, with recurring associations to epithelial, muscle, vascular, neuronal, germ-cell and neutrophil populations. Several genes also show immune-cell enhancement or enrichment, including monocyte, T-cell, B-cell and neutrophil populations. Brain protein detection is broad across the module, whereas HPA provides no matching bone-tissue protein comparison. Thus the shared bone-brain signal could reflect a conserved membrane and cytoskeletal program, but sample composition, vascular or stromal cells, and shared immune or other cell types remain plausible contributors. It should not be interpreted automatically as a bone-neuron-specific program.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP protein localization to membrane | 0.0356 | EHD1, GOLGA7, GPC1, JUP, LRP1, PIP5K1A, PRNP, SPTBN1 |
| GO:BP protein localization to plasma membrane | 0.0369 | EHD1, GOLGA7, JUP, LRP1, PIP5K1A, PRNP, SPTBN1 |

### STRING and hu.MAP

STRING provides a small set of high-confidence known relationships within the module: GOLGA7 with SPTLC2, GPC1 with LRP1, and LRP1 with PRNP. These relationships connect Golgi and sphingolipid biology, cell-surface proteoglycan and receptor biology, and membrane-associated prion-receptor biology. STRING enrichment supports membrane and integral-membrane localization in (STRING Component Intrinsic component of membrane; within-query FDR = 0.0013), (STRING Keyword Membrane; within-query FDR = 0.0064) and (STRING Component Integral component of membrane; within-query FDR = 0.0126), but those terms are supplementary and their STRING FDR is not global module significance. hu.MAP identifies ABLIM1 and LMO7 together in (hu.MAP huMAP3_05977.1), (hu.MAP huMAP3_08205.1) and (hu.MAP huMAP3_09542.1), each within larger actin- or adhesion-related complexes. This supports a cytoskeletal or junctional component, but the limited overlap with each complex does not establish that the whole co-abundance module is a single physical complex. Overall, the network is more consistent with coordinated cellular machinery and shared localization than with one fully validated macromolecular assembly.

**STRING interactions (score >= 0.7)**: 3 of 465 gene pairs: GOLGA7–SPTLC2 (0.9); GPC1–LRP1 (0.722); LRP1–PRNP (0.806)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Intrinsic component of membrane (FDR = 0.0013, 18 genes); Keyword Membrane (FDR = 0.0064, 21 genes); Component Integral component of membrane (FDR = 0.0126, 16 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05977.1 (ABLIM1, LMO7; 2/12); huMAP3_08205.1 (ABLIM1, LMO7; 2/17); huMAP3_09542.1 (ABLIM1, LMO7; 2/38)

### Novelty

The module may be a new co-abundance observation, but the fact sheet does not establish that it is a wholly new biological mechanism. Several component relationships are already represented by STRING, and the ABLIM1-LMO7 association is represented in hu.MAP. The globally significant membrane-localization signal is also biologically coherent with known functions of multiple members. Conversely, the particular cross-tissue co-abundance pattern, its conservation between bone and brain, and its combination of membrane trafficking, cytoskeletal, mitochondrial and stress-related genes are not directly demonstrated by the supplied interaction resources. Therefore the defensible claim is that this is a novel candidate module-level association requiring replication, cell-composition adjustment, and experimental testing; absence from STRING or hu.MAP alone would not prove novelty.

**Hypothesis.** Hypothesis: the module represents a coordinated membrane-interface state in which plasma-membrane trafficking and receptor turnover are coupled to actin or spectrin scaffolding, lipid handling, mitochondrial energy production and stress or inflammatory signaling. In this model, LRP1, GPC1, PRNP and EHD1 organize receptor and membrane recycling; SPTBN1, SYNPO, ABLIM1, LMO7, PARVA and JUP stabilize membrane-associated cytoskeletal structures; and NDUFA10, GDAP1, SLC25A4 and SLC25A12 support the energetic and mitochondrial requirements of these processes. The observed co-abundance could arise from a shared differentiated-cell state or from coordinated variation in vascular, stromal, neuronal and immune cell content. This is a mechanistic proposal, not an established causal pathway.

### Important genes

#### LRP1

- **Related proteins** (co-abundance neighbors): ABLIM1 (0.81); STRING partners: GPC1 (0.722), PRNP (0.806)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LDL receptor related protein 1. This gene encodes a member of the low-density lipoprotein receptor family of proteins. The encoded preproprotein is proteolytically processed by furin to generate 515 kDa and 85 kDa subunits that form the mature receptor (PMID: 8546712). This receptor is involved in several cellular processes, including intracellular signaling, lipid homeostasis, and clearance of apoptotic cells. In addition, the …
- **Diseases (Open Targets)**: neurodegenerative disease (0.514); keratosis pilaris atrophicans (0.499); developmental dysplasia of the hip (0.466); Alzheimer disease (0.462); Parkinson disease (0.443)
- **Europe PMC papers**: 10645
- **Why important**: LRP1 is a membrane-localized receptor with a relatively central bridging position in the module's membrane and cytoskeletal neighborhood. It is present in (GO:BP protein localization to membrane; q_global = 0.0356) and (GO:BP protein localization to plasma membrane; q_global = 0.0369), has STRING-supported relationships with GPC1 and PRNP, and is annotated for receptor-mediated endocytosis, lipid metabolism, phagocytosis and inflammatory regulation. HPA links it to brain protein detection and to adipose, fibroblast, hepatocyte, Kupffer-cell and monocyte-associated expression. It also has a substantial disease literature involving neurodegenerative and metabolic biology.
- **Conclusion**: Established evidence supports LRP1 as a plausible membrane-trafficking and uptake anchor for the module. Its role as the causal organizer of the bone-brain co-abundance pattern remains a hypothesis.

#### SPTBN1

- **Related proteins** (co-abundance neighbors): GDAP1 (0.87), MCM3AP (0.81), SYNPO (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: spectrin beta, non-erythrocytic 1. Spectrin is an actin crosslinking and molecular scaffold protein that links the plasma membrane to the actin cytoskeleton, and functions in the determination of cell shape, arrangement of transmembrane proteins, and organization of organelles. It is composed of two antiparallel dimers of alpha- and beta- subunits. This gene is one member of a family of beta-spectrin genes. The encoded protein cont…
- **Diseases (Open Targets)**: developmental delay, impaired speech, and behavioral abnormalities (0.802); cancer (0.597); hereditary disease (0.516); hearing loss disorder (0.459); neurodevelopmental disorder (0.453)
- **Europe PMC papers**: 1635
- **Why important**: SPTBN1 has a comparatively connected position in the co-abundance subgraph and is present in both primary terms, (GO:BP protein localization to membrane; q_global = 0.0356) and (GO:BP protein localization to plasma membrane; q_global = 0.0369). Its established function as a spectrin-based membrane and actin scaffold links plasma-membrane organization, vesicle transport and cell shape to the module's membrane signal. HPA shows brain protein detection and vascular and stromal cell-type associations. Its disease associations include neurodevelopmental and sensory phenotypes, and it has substantial literature.
- **Conclusion**: Established evidence supports SPTBN1 as a structural integrator connecting membrane localization with the cytoskeleton. Whether altered SPTBN1 activity drives the shared tissue module is not established.

#### GDAP1

- **Related proteins** (co-abundance neighbors): SPTBN1 (0.87), SYNPO (0.81), NDUFA10 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ganglioside induced differentiation associated protein 1. This gene encodes a member of the ganglioside-induced differentiation-associated protein family, which may play a role in a signal transduction pathway during neuronal development. Mutations in this gene have been associated with various forms of Charcot-Marie-Tooth Disease and neuropathy. Two transcript variants encoding different isoforms and a noncoding variant have been identified for this gen…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2K (0.833); Charcot-Marie-Tooth disease type 4A (0.803); Charcot-Marie-Tooth disease recessive intermediate A (0.784); autosomal dominant Charcot-Marie-Tooth disease type 2K (0.664); Charcot-Marie-Tooth disease (0.631)
- **Europe PMC papers**: 1052
- **Why important**: GDAP1 occupies a connected position linking SPTBN1 and SYNPO with the mitochondrial component represented by NDUFA10. It is HPA tissue-enhanced in brain and detected in neuronal and glial cell types. Its established annotations involve mitochondrial fission and fusion, neuronal development and response to vitamin D, while its disease associations with Charcot-Marie-Tooth disease and neuropathy provide strong biological relevance. Its literature is substantial.
- **Conclusion**: Established evidence supports GDAP1 as the strongest brain-relevant mitochondrial and neuronal connector in the module. Its participation in a shared bone-brain membrane program, rather than an independent neuronal signal, remains to be tested.

#### NDUFA10

- **Related proteins** (co-abundance neighbors): PRNP (0.89), SLC25A4 (0.83), SLC25A12 (0.80), GDAP1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit A10. The protein encoded by this gene is a component of 42 kDa complex I, the first enzyme complex in the electron transport chain of mitochondria. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. A mutation in this gene was found in an individual with Leigh syndrome. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.677); Leigh syndrome (0.674); mitochondrial complex I deficiency, nuclear type 22 (0.668); type 2 diabetes mellitus (0.620); diabetes mellitus (0.578)
- **Europe PMC papers**: 1163
- **Why important**: NDUFA10 has a highly connected position within the module and links PRNP, SLC25A4, SLC25A12 and GDAP1. It is a component of mitochondrial complex I with established roles in electron transport, aerobic respiration and proton-motive-force-linked ATP production. HPA detects its protein in brain, and disease evidence includes Leigh syndrome and mitochondrial complex I deficiency. It has substantial literature.
- **Conclusion**: Established evidence supports NDUFA10 as an energetic component that could enable membrane trafficking and cytoskeletal maintenance. The module data do not demonstrate that mitochondrial respiratory impairment causes the observed co-abundance pattern.

#### SYNPO

- **Related proteins** (co-abundance neighbors): UQCC1 (0.82), GDAP1 (0.81), SPTBN1 (0.81), APOOL (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: synaptopodin. Synaptopodin is an actin-associated protein that may play a role in actin-based cell shape and motility. The name synaptopodin derives from the protein's associations with postsynaptic densities and dendritic spines and with renal podocytes (Mundel et al., 1997 [PubMed 9314539]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: nephrotic syndrome (0.260); Hypocalcemia (0.159); cervical carcinoma (0.156); osteoarthritis, hip (0.148); osteoarthritis, knee (0.148)
- **Europe PMC papers**: 1599
- **Why important**: SYNPO is among the more connected genes in the module and links UQCC1, GDAP1, SPTBN1 and APOOL. Its established functions include actin-bundle assembly, stress-fiber organization, postsynaptic modulation and neuronal synaptic plasticity. HPA detects it in brain and associates it with cardiomyocytes, myonuclei and vascular or epithelial cell types. It has substantial literature and disease associations involving renal and joint phenotypes.
- **Conclusion**: Established evidence supports SYNPO as a cytoskeletal and neuronal-interface representative that helps explain the connection between membrane organization and tissue-specific cell architecture. A direct role in the conserved bone-brain module is a hypothesis rather than a demonstrated mechanism.

## Module 2

**Tissue pair**: bone and brain  
**Genes (40)**: AGPS, ADPGK, ALDH1B1, ASPH, AGTRAP, GLB1, HSPA5, MTHFD1L, CKAP4, COIL, DCBLD2, DDX31, FNDC3B, GANAB, GBE1, SHMT2, GPD2, HYOU1, MCM2, MCM4, MCM5, MCM6, MCM7, MOGS, IGF2R, POR, P4HA1, ALDH18A1, PDIA4, PLOD2, PPIC, PRDX4, PRKDC, PVR, RPP25L, RRBP1, DARS2, TFRC, TWSG1, TXNDC5

### Function

The module has two prominent, biologically coherent components. The strongest primary evidence identifies the MCM2–MCM4–MCM5–MCM6–MCM7 group as a mini-chromosome maintenance and CMG-associated replication-initiation unit, supported by the globally corrected terms for the MCM complex, DNA replication initiation and regulation, replication-fork helicase activity, break-induced replication, DNA replication, and cell cycle (6 globally significant GO/KEGG terms, q_global 1.87e-05–0.00082; see the table), (12 globally significant GO/KEGG terms, q_global 0.00488–0.0481; see the table). A second component is an endoplasmic-reticulum protein maturation and quality-control program involving CKAP4, GANAB, HSPA5, HYOU1, MOGS, PDIA4, RRBP1, and TXNDC5, supported by the globally corrected protein-processing-in-the-endoplasmic-reticulum and ER-lumen terms (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0013), (GO:CC endoplasmic reticulum lumen; q_global = 0.0218). Thus, this is not best described as a single narrowly specialized pathway: it combines a proliferative or replication-associated signal with ER folding, glycan processing, redox control, and secretory-protein quality control. The replication signal is especially compelling because the same MCM genes recur across many independent primary terms, whereas the ER signal is supported by a distinct, functionally consistent set.

**Cell composition.** The module is not a clean tissue-specific bone or brain program. HPA reports low tissue specificity for much of the module, with additional tissue-enhanced or tissue-enriched genes associated with bone marrow, liver, blood vessels, skeletal muscle, and lymphoid tissue. Cell-type patterns prominently include neutrophil and neutrophil-progenitor, erythrocyte-progenitor, hepatocyte, and trophoblast states. The module also contains many secreted or secretome-associated genes, while several other genes are ER-resident or involved in secretory processing. This raises the possibility that the shared bone–brain co-abundance signal partly reflects blood content, vascular or infiltrating cell populations, shared stromal or secretory cell types, or a general stress and biosynthetic state rather than a neuron–osteoblast-specific mechanism. The blood-cell specificity summary is mostly low, so a purely blood-derived interpretation would also be too strong. Brain protein detection is broad for the module, but the lack of matching HPA bone tissue data prevents a direct protein-level bone-versus-brain comparison.

**GO/KEGG enrichment**: 19 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC MCM complex | 1.87e-05 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication initiation | 7.58e-05 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP double-strand break repair via break-induced replication | 0.000203 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication | 0.000203 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC DNA replication preinitiation complex | 0.00082 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC CMG complex | 0.00082 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human) | 0.0013 | CKAP4, GANAB, HSPA5, HYOU1, MOGS, PDIA4, RRBP1, TXNDC5 |
| GO:BP DNA replication initiation | 0.00488 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF four-way junction helicase activity | 0.00691 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF forked DNA-dependent helicase activity | 0.00691 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF double-stranded DNA helicase activity | 0.00947 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF 3'-5' DNA helicase activity | 0.00947 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded 3'-5' DNA helicase activity | 0.00947 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| KEGG DNA replication - Homo sapiens (human) | 0.0163 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC endoplasmic reticulum lumen | 0.0218 | ASPH, CKAP4, GANAB, HSPA5, HYOU1, P4HA1, PDIA4, TXNDC5 |

### STRING and hu.MAP

STRING provides strong support for two established physical or functional neighborhoods. The MCM genes form a highly connected cluster, with very strong pairwise links among MCM2, MCM4, MCM5, MCM6, and MCM7, and an additional link from MCM4 to PRKDC (STRING Component MCM complex; within-query FDR = 0.00032), (6 supplementary STRING terms; within-query FDR 0.00047–0.00047), (STRING Component CMG complex; within-query FDR = 0.0012), (STRING KEGG Cell cycle; within-query FDR = 0.0012), (STRING COMPARTMENTS CMG complex; within-query FDR = 0.0013), (STRING COMPARTMENTS protein-DNA complex; within-query FDR = 0.0014). The ER neighborhood links HSPA5 with HYOU1, PDIA4, GANAB, and TXNDC5, and links GANAB with MOGS and PDIA4; it also includes relationships involving PRDX4 and TXNDC5 (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.00046), (STRING Keyword Signal; within-query FDR = 0.00059), (STRING COMPARTMENTS Endoplasmic reticulum lumen; within-query FDR = 0.0013). hu.MAP independently recovers the five-member MCM subset in multiple replication and chromatin-associated complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1), (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1), (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1), (hu.MAP huMAP3_10862.1), (hu.MAP huMAP3_14306.1), (hu.MAP huMAP3_02602.1), (hu.MAP huMAP3_09238.1), (hu.MAP huMAP3_08848.1). hu.MAP also supports an ER/trafficking-related grouping containing IGF2R, PDIA4, GANAB, DCBLD2, and HYOU1, as well as an HSPA5–HYOU1 complex (hu.MAP huMAP3_06775.1), (hu.MAP huMAP3_09327.1), (hu.MAP huMAP3_07455.1). These results indicate that much of the module reflects known molecular machinery, not previously unrecognized direct interactions. STRING and hu.MAP coverage is uneven for the remaining genes, so absence of a reported relationship should not be interpreted as evidence against their biological co-regulation.

**STRING interactions (score >= 0.7)**: 26 of 780 gene pairs: ALDH18A1–ALDH1B1 (0.756); ALDH18A1–SHMT2 (0.804); GANAB–HSPA5 (0.846); GANAB–HYOU1 (0.83); GANAB–MOGS (0.997); GANAB–PDIA4 (0.717); HSPA5–HYOU1 (0.999); HSPA5–PDIA4 (0.99); HSPA5–TXNDC5 (0.798); HYOU1–PDIA4 (0.997); MCM2–MCM4 (0.999); MCM2–MCM5 (0.999); MCM2–MCM6 (0.999); MCM2–MCM7 (0.999); MCM4–MCM5 (0.999); MCM4–MCM6 (0.999); MCM4–MCM7 (0.999); MCM4–PRKDC (0.887); MCM5–MCM6 (0.999); MCM5–MCM7 (0.999); MCM6–MCM7 (0.999); MOGS–PDIA4 (0.73); MTHFD1L–SHMT2 (0.995); P4HA1–PDIA4 (0.765); P4HA1–PLOD2 (0.853); PRDX4–TXNDC5 (0.994)
**STRING functional enrichment (supplementary, within-query FDR)**: Component MCM complex (FDR = 0.00032, 5 genes); COMPARTMENTS MCM complex (FDR = 0.00034, 5 genes); KEGG Protein processing in endoplasmic reticulum (FDR = 0.00046, 8 genes); InterPro MCM domain (FDR = 0.00047, 5 genes); InterPro Mini-chromosome maintenance, conserved site (FDR = 0.00047, 5 genes); InterPro MCM N-terminal domain (FDR = 0.00047, 5 genes); InterPro Mini-chromosome maintenance protein (FDR = 0.00047, 5 genes); InterPro MCM OB domain (FDR = 0.00047, 5 genes); InterPro MCM, AAA-lid domain (FDR = 0.00047, 5 genes); Keyword Signal (FDR = 0.00059, 14 genes); Component CMG complex (FDR = 0.0012, 5 genes); KEGG Cell cycle (FDR = 0.0012, 6 genes); COMPARTMENTS Endoplasmic reticulum lumen (FDR = 0.0013, 8 genes); COMPARTMENTS CMG complex (FDR = 0.0013, 5 genes); COMPARTMENTS protein-DNA complex (FDR = 0.0014, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05529.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/6); huMAP3_14758.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/14); huMAP3_08554.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_11832.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_12180.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/17); huMAP3_06775.1 (IGF2R, PDIA4, GANAB, DCBLD2, HYOU1; 5/60); huMAP3_06061.1 (MCM4, MCM7, MCM2, MCM6; 4/5); huMAP3_07113.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_11119.1 (MCM4, MCM5, MCM7, MCM6; 4/14); huMAP3_09327.1 (PDIA4, GANAB, DCBLD2, HYOU1; 4/93); huMAP3_09860.1 (MCM4, MCM2, MCM6; 3/4); huMAP3_00154.1 (MCM4, MCM2, MCM6; 3/5); huMAP3_09466.1 (MCM4, MCM2, MCM6; 3/23); huMAP3_10525.1 (ALDH18A1, DARS2, MTHFD1L; 3/33); huMAP3_10862.1 (MCM4, MCM2, MCM6; 3/33); huMAP3_14306.1 (MCM4, MCM2, MCM6; 3/55); huMAP3_13468.1 (ALDH18A1, DARS2, MTHFD1L; 3/99); huMAP3_02602.1 (MCM4, MCM6; 2/2); huMAP3_07455.1 (HSPA5, HYOU1; 2/4); huMAP3_09238.1 (MCM5, MCM7; 2/11); huMAP3_08848.1 (MCM4, MCM6; 2/15); huMAP3_10725.1 (TFRC, CKAP4; 2/59)

### Novelty

The individual functional components are not new: the MCM assembly is a well-established replication system, and the ER genes belong to recognized folding, glycan-processing, oxidoreductase, and stress-response machinery. The module is therefore unlikely to represent discovery of a new protein complex. Its potentially novel aspect is the co-abundance coupling of these established systems across bone and brain, together with metabolic, mitochondrial, membrane, and cell-surface genes that bridge the two neighborhoods. However, the current evidence does not establish that this cross-tissue coupling is mechanistically specific. The broad HPA expression pattern, secretory composition, and enrichment of hematopoietic-associated cell states provide plausible sample-composition or shared-cell-type explanations. A claim of novelty would require replication in independent cohorts, cell-type-aware analysis, and testing whether the coupling persists after controlling for blood, vascular, immune, and proliferative signals.

**Hypothesis.** Hypothesis: the module represents a shared regenerative or stress-adaptive state in which proliferating or replication-competent cells increase MCM-dependent genome-replication capacity while secretory and metabolically active cells increase ER folding, glycan maturation, redox buffering, and protein-quality-control capacity. In bone and brain samples, this state may be coupled through vascular, hematopoietic, stromal, glial, or other shared non-parenchymal cell populations, rather than being a direct bone–neuron or bone–osteoblast circuit. HSPA5, PDIA4, TXNDC5, GANAB, and related ER genes could reflect proteostatic demand, while the MCM group could reflect cell-cycle entry or repair competence. This is a mechanistic hypothesis, not an established conclusion from co-abundance alone; it should be tested with cell-type-resolved expression, proliferation and ER-stress measurements, and perturbation of the relevant cell populations.

### Important genes

#### MCM2

- **Related proteins** (co-abundance neighbors): MCM5 (0.89), MCM6 (0.86), MCM7 (0.85), RPP25L (0.83), TWSG1 (0.80); STRING partners: MCM4 (0.999), MCM5 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a central member of the MCM replication module, connects to MCM5, MCM6, MCM7, RPP25L, and TWSG1 in the co-abundance graph, and participates in essentially all of the primary replication-related terms (6 globally significant GO/KEGG terms, q_global 1.87e-05–0.00082; see the table), (12 globally significant GO/KEGG terms, q_global 0.00488–0.0481; see the table). Its established role is initiation of eukaryotic genome replication and participation in the pre-replication and replication-fork machinery. It also has extensive literature support and disease associations involving hearing and developmental phenotypes, making it a strong anchor for interpreting the replication signal.
- **Conclusion**: Established evidence supports MCM2 as a core replication-initiation component and a reliable marker of the module's replication-associated subprogram. The co-abundance data support its use as an indicator of proliferative or repair-competent cell states, but do not demonstrate that MCM2 drives the shared bone–brain pattern.

#### MCM6

- **Related proteins** (co-abundance neighbors): MCM4 (0.92), MCM5 (0.86), MCM2 (0.86); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 6. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: lactose intolerance (0.246); neurodegenerative disease (0.225); obesity disorder (0.166); nervous system disorder (0.141); systemic lupus erythematosus (0.140)
- **Europe PMC papers**: 3766
- **Why important**: MCM6 is embedded in the highly connected MCM2–MCM4–MCM5–MCM7 cluster and is recovered in the primary MCM, replication, helicase, DNA-repair, and cell-cycle terms (6 globally significant GO/KEGG terms, q_global 1.87e-05–0.00082; see the table), (12 globally significant GO/KEGG terms, q_global 0.00488–0.0481; see the table). STRING shows strong links to the other MCM members, and hu.MAP repeatedly places it in replication, chromatin, and CMG-related complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1), (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1), (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1), (hu.MAP huMAP3_10862.1), (hu.MAP huMAP3_14306.1), (hu.MAP huMAP3_02602.1), (hu.MAP huMAP3_08848.1). Its HPA profile is enhanced in lymphoid tissue and hematopoietic progenitor states, which is important when interpreting the apparent bone–brain conservation.
- **Conclusion**: Established evidence identifies MCM6 as part of the canonical replicative helicase system. Its hematopoietic-associated expression makes shared cell composition or progenitor abundance a plausible contributor to the module, while a direct tissue-specific role remains unproven.

#### HSPA5

- **Related proteins** (co-abundance neighbors): PDIA4 (0.85), HYOU1 (0.84), TFRC (0.83), TXNDC5 (0.82), P4HA1 (0.80); STRING partners: GANAB (0.846), HYOU1 (0.999), PDIA4 (0.99), TXNDC5 (0.798)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_07455.1
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is a highly connected ER-side hub linked in the module to PDIA4, HYOU1, TFRC, TXNDC5, and P4HA1. It appears in the primary ER-processing and ER-lumen terms (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0013), (GO:CC endoplasmic reticulum lumen; q_global = 0.0218), in the corresponding STRING evidence (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.00046), (STRING Keyword Signal; within-query FDR = 0.00059), (STRING COMPARTMENTS Endoplasmic reticulum lumen; within-query FDR = 0.0013), and in an HSPA5–HYOU1 hu.MAP complex (hu.MAP huMAP3_07455.1). Its established function is as an ER HSP70 chaperone and regulator of ER homeostasis, with documented involvement in protein folding, targeting, and the unfolded-protein response. It also has extensive literature and disease relevance, including neurodegenerative and neoplastic associations.
- **Conclusion**: Established evidence supports HSPA5 as a principal proteostasis hub in the module. Its brain detection and broad cell-type distribution are compatible with a genuine brain proteostasis signal, but they do not distinguish intrinsic neural biology from stress, secretion, or cellular-composition effects.

#### PDIA4

- **Related proteins** (co-abundance neighbors): TXNDC5 (0.90), PRDX4 (0.86), HSPA5 (0.85), GANAB (0.83), ADPGK (0.80); STRING partners: GANAB (0.717), HSPA5 (0.99), HYOU1 (0.997), MOGS (0.73), P4HA1 (0.765)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 occupies the ER-quality-control neighborhood and connects to TXNDC5, PRDX4, HSPA5, GANAB, and ADPGK. It contributes to the primary ER-processing and ER-lumen terms (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0013), (GO:CC endoplasmic reticulum lumen; q_global = 0.0218) and is supported by STRING links to HSPA5, HYOU1, GANAB, MOGS, and P4HA1 (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.00046), (STRING Keyword Signal; within-query FDR = 0.00059), (STRING COMPARTMENTS Endoplasmic reticulum lumen; within-query FDR = 0.0013). hu.MAP places it in ER-associated complexes with GANAB, HYOU1, and DCBLD2 (hu.MAP huMAP3_06775.1), (hu.MAP huMAP3_09327.1). Its established function includes thiol-disulfide exchange, protein folding, protein secretion, and response to ER stress.
- **Conclusion**: Established evidence supports PDIA4 as an ER folding and stress-response component that helps define the second major module neighborhood. Its position suggests coordination with other ER proteins, but the data do not establish whether it is causal, merely co-regulated, or a marker of secretory-cell abundance.

#### TXNDC5

- **Related proteins** (co-abundance neighbors): PDIA4 (0.90), RPP25L (0.89), P4HA1 (0.89), IGF2R (0.84), HSPA5 (0.82), PLOD2 (0.82); STRING partners: HSPA5 (0.798), PRDX4 (0.994)
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Endoplasmic reticulum; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin domain containing 5. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal endoplasmic reticulum (ER)-signal sequence, three catalytically active thioredoxin domains and a C-terminal ER-retention sequence. Its expression is induced by hypoxia and its role ma…
- **Diseases (Open Targets)**: colorectal carcinoma (0.321); spinal stenosis (0.203); neoplasm (0.096); central nervous system cancer (0.092); glioma (0.091)
- **Europe PMC papers**: 1026
- **Why important**: TXNDC5 has one of the strongest positions in the module and links the ER neighborhood to PDIA4, RPP25L, P4HA1, IGF2R, HSPA5, and PLOD2. It contributes to the primary ER-processing and ER-lumen terms (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0013), (GO:CC endoplasmic reticulum lumen; q_global = 0.0218) and to the supplementary ER and signal-associated terms (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.00046), (STRING Keyword Signal; within-query FDR = 0.00059), (STRING COMPARTMENTS Endoplasmic reticulum lumen; within-query FDR = 0.0013). Its established function is as an ER-resident thioredoxin-family protein involved in disulfide exchange, protein folding, and protection from hypoxia-associated apoptosis. It has substantial literature and disease associations involving spinal stenosis, neoplasia, and central nervous system disease.
- **Conclusion**: Established evidence supports TXNDC5 as a highly connected ER redox and folding component, making it a plausible bridge between proteostasis, hypoxia, and extracellular-matrix-related biology. Its cross-tissue co-abundance could reflect a shared stress-adaptive state, but that interpretation remains a hypothesis.

#### P4HA1

- **Related proteins** (co-abundance neighbors): MOGS (0.90), TXNDC5 (0.89), GBE1 (0.86), GANAB (0.82), HSPA5 (0.80), PRDX4 (0.80); STRING partners: PDIA4 (0.765), PLOD2 (0.853)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prolyl 4-hydroxylase subunit alpha 1. This gene encodes a component of prolyl 4-hydroxylase, a key enzyme in collagen synthesis composed of two identical alpha subunits and two beta subunits. The encoded protein is one of several different types of alpha subunits and provides the major part of the catalytic site of the active enzyme. In collagen and related proteins, prolyl 4-hydroxylase catalyzes the formation of 4-hydroxyproline tha…
- **Diseases (Open Targets)**: neurodegenerative disease (0.406); dengue disease (0.370); Parkinson disease (0.201); intervertebral disk degenerative disorder (0.193); neoplasm (0.115)
- **Europe PMC papers**: 1910
- **Why important**: P4HA1 is a highly connected ER-associated gene linked to MOGS, TXNDC5, GBE1, GANAB, HSPA5, and PRDX4. It contributes to the primary ER-lumen term (GO:CC endoplasmic reticulum lumen; q_global = 0.0218) and to STRING ER and signal evidence (STRING Keyword Signal; within-query FDR = 0.00059), (STRING COMPARTMENTS Endoplasmic reticulum lumen; within-query FDR = 0.0013). Its established function is as the catalytic alpha subunit of prolyl four-hydroxylase, supporting collagen maturation and proper folding of procollagen, with relevance to extracellular-matrix biology. It also has disease associations involving neurodegenerative disease, Parkinson disease, and connective-tissue or disc degeneration.
- **Conclusion**: Established evidence supports P4HA1 as an ER collagen-processing and matrix-related component that may be particularly relevant to bone-associated biology while remaining detectable in brain. Its bridging position makes it a useful candidate for testing a connection between proteostasis, hypoxia, and matrix remodeling, but the proposed connection is not demonstrated by this module alone.

## Module 3

**Tissue pair**: bone and brain  
**Genes (8)**: ARL6IP4, CAPRIN1, CPSF2, FXR1, PPFIBP1, PAWR, PLRG1, XRN2

### Function

The strongest functional interpretation is an mRNA metabolism and post-transcriptional RNA-control module. The primary evidence is (GO:BP mRNA metabolic process; q_global = 0.0203), the globally corrected enrichment for mRNA metabolic process, supported by ARL6IP4, CAPRIN1, CPSF2, FXR1, PLRG1 and XRN2. These genes collectively span spliceosome-associated processing, mRNA cleavage and polyadenylation, RNA degradation, translation control and cytoplasmic RNA regulation. PLRG1 is a central network node and is a component of the CDC5L spliceosome complex; CPSF2 participates in mRNA three-prime-end processing; XRN2 contributes to RNA degradation and transcription termination; ARL6IP4 is predicted to participate in RNA splicing; and CAPRIN1 and FXR1 regulate translation or post-transcriptional gene expression. The network therefore supports a coordinated RNA-processing interpretation rather than a narrowly defined pathway. PAWR and PPFIBP1 do not have primary-term support, so their inclusion should not be taken as proof that apoptosis, adhesion or neuronal development is the module function. No STRING functional-enrichment term was reported.

**Cell composition.** This is not a secreted-protein module: the secretome annotation reports no secreted genes. The genes are also not predominantly blood-cell-specific; most have low immune-cell specificity, although PAWR has group-enriched blood-cell annotation and several genes have cell-type-enhanced annotations. Most genes have low tissue specificity, while FXR1 is group-enriched in skeletal muscle and tongue. All genes were detected by brain immunohistochemistry, but the HPA summary does not establish corresponding protein detection in bone because no matching bone tissue evidence was available. Overall, the composition is consistent with broadly expressed intracellular proteins, especially RNA-processing machinery, rather than a plasma-protein or strongly blood-derived module. Shared cell types or common cellular states in the sampled tissues remain possible, but the HPA evidence does not by itself identify blood contamination as the explanation.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP mRNA metabolic process | 0.0203 | ARL6IP4, CAPRIN1, CPSF2, FXR1, PLRG1, XRN2 |

### STRING and hu.MAP

The network contains one high-confidence STRING relationship: CAPRIN1 with FXR1. This independently supports a functional connection between two RNA-associated proteins and is concordant with the mRNA metabolism interpretation. No other module pair met the stated STRING interaction threshold, and no STRING functional-enrichment term was reported. No hu.MAP complex contained multiple module members. Thus, the module has limited externally catalogued physical-network support: the CAPRIN1–FXR1 relationship is established by the supplied STRING evidence, whereas the remaining co-abundance relationships should be interpreted as module-level associations rather than confirmed direct interactions. The absence of hu.MAP complexes does not exclude transient, tissue-dependent or condition-dependent assemblies.

**STRING interactions (score >= 0.7)**: 1 of 28 gene pairs: CAPRIN1–FXR1 (0.891)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a new tissue-pair co-abundance observation, but it cannot be called a definitively new molecular complex or pathway. The globally corrected mRNA-metabolism signal and the CAPRIN1–FXR1 STRING relationship provide biological coherence, while the lack of a hu.MAP complex and the sparse high-confidence STRING connectivity suggest that the particular bone–brain co-abundance configuration is not simply a well-established multigene complex in the supplied resources. However, absence from STRING or hu.MAP alone does not prove novelty. A stronger novelty claim would require comparison with published bone–brain co-abundance modules, independent cohorts, perturbation data and tissue- or cell-resolved replication.

**Hypothesis.** Hypothesis: this conserved bone–brain module reflects a shared intracellular RNA-homeostasis program in which spliceosome-associated processing, transcript three-prime-end formation, RNA degradation and cytoplasmic translation control are coordinated across the two tissues. PLRG1 may organize the nuclear RNA-processing component, while CAPRIN1 and FXR1 may connect transcript handling to cytoplasmic translation regulation; XRN2, CPSF2 and ARL6IP4 may contribute to transcript maturation, termination and turnover. PPFIBP1 and PAWR could link this RNA-centered state to cell architecture or survival, but that connection is speculative because they lack primary enrichment-term support. This hypothesis predicts coordinated changes in transcript processing or RNA stability rather than secretion of a common extracellular factor.

### Important genes

#### PLRG1

- **Related proteins** (co-abundance neighbors): FXR1 (0.82), CPSF2 (0.81), CAPRIN1 (0.81), PPFIBP1 (0.80), XRN2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pleiotropic regulator 1. This gene encodes a core component of the cell division cycle 5-like (CDC5L) complex. The CDC5L complex is part of the spliceosome and is required for pre-mRNA splicing. The encoded protein plays a critical role in alternative splice site selection. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jan 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); Alzheimer disease (0.462); lysosomal storage disease (0.462); Parkinson disease (0.462); dengue disease (0.370)
- **Europe PMC papers**: 379
- **Why important**: PLRG1 is the most central network gene in the supplied subgraph, connecting the RNA-associated members and occupying the clearest organizing position. It is a core component of the CDC5L complex and is required for pre-mRNA splicing and alternative splice-site selection. It is included in (GO:BP mRNA metabolic process; q_global = 0.0203), has brain protein detection and has substantial literature coverage. Its disease-association evidence includes neurodegenerative and neurodegenerative disease categories, although these associations do not establish a causal role in this module.
- **Conclusion**: Established evidence supports PLRG1 as a central spliceosome-related regulator and the strongest candidate for the module's nuclear RNA-processing component. Hypothesis: its network centrality reflects coordination of several RNA-processing activities in the conserved bone–brain state.

#### CAPRIN1

- **Related proteins** (co-abundance neighbors): PLRG1 (0.81); STRING partners: FXR1 (0.891)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell cycle associated protein 1. Enables RNA binding activity. Predicted to be involved in negative regulation of translation and positive regulation of dendritic spine morphogenesis. Located in cell leading edge and cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder with language impairment, autism, and attention deficit-hyperactivity disorder (0.692); neurodegeneration, childhood-onset, with cerebellar ataxia and cognitive decline (0.677); complex neurodevelopmental disorder (0.370); juvenile myoclonic epilepsy (0.340); Seizure (0.333)
- **Europe PMC papers**: 1194
- **Why important**: CAPRIN1 is one of the two module members linked by the high-confidence STRING relationship, with FXR1. It is included in (GO:BP mRNA metabolic process; q_global = 0.0203) and is annotated for RNA binding, translational repression, dendritic and dendritic-spine morphogenesis, stress-granule assembly and mRNA decay-related regulation. It has brain detection, extensive literature coverage and disease associations involving neurodevelopmental disorders, neurodegeneration and seizures.
- **Conclusion**: Established evidence supports CAPRIN1 as a cytoplasmic RNA-regulatory gene that independently connects the module to the CAPRIN1–FXR1 relationship. Hypothesis: CAPRIN1 may provide the link between nuclear transcript processing and local or stress-responsive translation in brain and bone-associated cells.

#### FXR1

- **Related proteins** (co-abundance neighbors): PLRG1 (0.82); STRING partners: CAPRIN1 (0.891)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FMR1 autosomal homolog 1. The protein encoded by this gene is an RNA binding protein that interacts with the functionally-similar proteins FMR1 and FXR2. These proteins shuttle between the nucleus and cytoplasm and associate with polyribosomes, predominantly with the 60S ribosomal subunit. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: myopathy, congenital proximal, with minicore lesions (0.594); cancer (0.569); myopathy, congenital, with respiratory insufficiency and bone fractures (0.502); congenital myopathy (0.408); schizophrenia (0.386)
- **Europe PMC papers**: 2052
- **Why important**: FXR1 is included in (GO:BP mRNA metabolic process; q_global = 0.0203) and forms the only supplied high-confidence STRING pair with CAPRIN1. It is an RNA-binding protein related to FMR1 and FXR2, associates with polyribosomes and regulates translation and post-transcriptional gene expression. It has group-enriched tissue annotation in skeletal muscle and tongue, brain detection, substantial literature coverage and disease associations involving congenital myopathy and schizophrenia.
- **Conclusion**: Established evidence supports FXR1 as a translational and post-transcriptional component of the module, with direct network support from CAPRIN1. Hypothesis: its tissue enrichment and disease links may indicate that the module is sensitive to cell-type-specific translational demands, but the supplied data do not establish a bone-specific or brain-specific FXR1 mechanism.

#### XRN2

- **Related proteins** (co-abundance neighbors): PLRG1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 5'-3' exoribonuclease 2. This gene encodes a 5'-3' exonuclease that promotes transcription termination at cotranscriptional cleavage sites. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: attention deficit-hyperactivity disorder (0.339); neurodegenerative disease (0.326); atrial fibrillation (0.305); food allergy (0.271); adolescent idiopathic scoliosis (0.221)
- **Europe PMC papers**: 1676
- **Why important**: XRN2 is included in (GO:BP mRNA metabolic process; q_global = 0.0203) and encodes a five-prime-to-three-prime exoribonuclease involved in RNA degradation, RNA polymerase transcription termination and rRNA processing. It is located in the nucleolus, has brain detection, substantial literature coverage and disease associations including attention-related, neurodegenerative and skeletal conditions. Its direct network degree is limited, but its function is highly complementary to the other RNA-processing genes.
- **Conclusion**: Established evidence supports XRN2 as a transcript turnover and transcription-termination component of the module. Hypothesis: XRN2 may help maintain RNA-quality control in the shared cellular state, but the co-abundance data do not demonstrate direct regulation by or of the other module genes.

#### PPFIBP1

- **Related proteins** (co-abundance neighbors): PAWR (0.81), PLRG1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PPFIB scaffold protein 1. The protein encoded by this gene is a member of the LAR protein-tyrosine phosphatase-interacting protein (liprin) family. Liprins interact with members of LAR family of transmembrane protein tyrosine phosphatases, which are known to be important for axon guidance and mammary gland development. It has been proposed that liprins are multivalent proteins that form complex structures and act as scaffo…
- **Diseases (Open Targets)**: neurodevelopmental disorder with seizures, microcephaly, and brain abnormalities (0.757); microcephaly (0.529); Seizure (0.525); Cerebral calcification (0.525); Severe intellectual disability (0.525)
- **Europe PMC papers**: 485
- **Why important**: PPFIBP1 is a bridge between PAWR and the central PLRG1-centered portion of the subgraph. It encodes a liprin-family scaffold associated with LAR-family protein-tyrosine phosphatases and is annotated for cell adhesion, cell polarity, neuromuscular-junction development and cortical microtubule organization. It has brain detection and disease associations involving neurodevelopmental disorders, seizures, microcephaly and cerebral calcification.
- **Conclusion**: Established evidence supports PPFIBP1 as a scaffold and cell-organization protein with relevant neurodevelopmental associations, but it is not included in the primary enrichment term. Hypothesis: PPFIBP1 may connect RNA-state variation to cell polarity or structural organization, although this proposed connection is weaker than the RNA-processing interpretation.

## Module 4

**Tissue pair**: bone and brain  
**Genes (11)**: CLTB, GCC2, LEMD3, MTHFS, NELFA, NELFE, PUS1, RBM27, SNW1, SRSF5, UIMC1

### Function

The strongest primary evidence supports a nuclear transcriptional regulation module centered on the negative elongation factor complex. The globally corrected terms identify a transcription elongation factor complex containing NELFA, NELFE, and SNW1 (GO:CC transcription elongation factor complex; q_global = 0.0212), and the NELF complex containing NELFA and NELFE (GO:CC NELF complex; q_global = 0.038). NELFA and NELFE therefore provide the clearest functional anchor. The supplementary STRING annotations are consistent with chromatin and nuclear-body biology, including positive regulation of histone H three lysine four methylation (STRING Process Positive regulation of histone H3-K4 methylation; within-query FDR = 0.0312) and nuclear-body localization (STRING Component Nuclear body; within-query FDR = 0.0476), but these are supportive rather than globally corrected evidence. The remaining genes suggest connected RNA processing, DNA-damage regulation, vesicle trafficking, folate metabolism, and nuclear-envelope biology. Thus, this is best interpreted as a transcriptional and RNA-regulatory module with additional context-dependent cellular functions, rather than as a narrowly defined pathway.

**Cell composition.** The module does not resemble a plasma or secreted-protein module: HPA reports no secreted genes. Most genes have low tissue specificity, and many are cell-type enhanced rather than restricted to bone or brain. Neutrophil-related enhancement is present for UIMC1 and MTHFS, while several genes show enhancement in epithelial or reproductive cell types. This raises the possibility that part of the shared co-abundance signal reflects common cell populations, sample composition, or broadly expressed nuclear machinery rather than a bone-brain-specific program. The liver-enriched status of MTHFS is an additional compositional caveat. Brain protein detection is widespread among the module genes, but there is no matching HPA bone tissue result, so the shared tissue interpretation should not be treated as direct evidence of a bone-localized protein complex.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC transcription elongation factor complex | 0.0212 | NELFA, NELFE, SNW1 |
| GO:CC NELF complex | 0.038 | NELFA, NELFE |

### STRING and hu.MAP

STRING provides one high-confidence physical or functional relationship within the module, between NELFA and NELFE. This strongly supports the NELF-centered core but leaves most co-abundance edges without an established STRING relationship. hu.MAP independently places NELFA and NELFE together in two complexes (hu.MAP huMAP3_01088.1) (hu.MAP huMAP3_09446.1), with the complexes also containing NELFB, NELFCD, IGHMBP2, XYLT1, TMEM141, and, in one complex, GPR137B and ICA1. These results confirm that the NELFA-NELFE pair is known complex biology, while the broader module is not simply a recovered complete canonical complex. The co-abundance links involving PUS1, MTHFS, LEMD3, GCC2, CLTB, RBM27, SRSF5, UIMC1, and SNW1 should therefore be regarded as module-level associations requiring experimental validation, not as established direct physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 55 gene pairs: NELFA–NELFE (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Process Positive regulation of histone H3-K4 methylation (FDR = 0.0312, 3 genes); Component Nuclear body (FDR = 0.0476, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01088.1 (NELFE, NELFA; 2/7); huMAP3_09446.1 (NELFE, NELFA; 2/9)

### Novelty

The complete shared bone-brain module is plausibly a new systems-level observation, because the known NELFA-NELFE core is embedded with genes spanning RNA modification, splicing, DNA repair, Golgi trafficking, folate metabolism, and nuclear-envelope signaling, while most of those relationships are absent from the supplied STRING and hu.MAP evidence. However, absence from those resources does not prove novelty: it may reflect incomplete interaction coverage, indirect regulation, tissue context, or co-abundance caused by cell composition. The defensible conclusion is that the NELF-centered core is established, whereas the particular cross-tissue co-abundance configuration and its proposed connections are potentially novel and need replication in independent bone and brain datasets, cell-type deconvolution, and perturbation experiments.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of transcriptional elongation and RNA maturation in a shared nuclear cell state, with NELFA-NELFE acting as the central transcription-pausing component. SNW1 and SRSF5 may connect transcriptional regulation to co-transcriptional splicing, while PUS1 and MTHFS may couple RNA modification and folate-dependent metabolic capacity to the transcriptional state. UIMC1 may contribute DNA-damage-responsive chromatin regulation, and LEMD3 may provide a bone-relevant nuclear-envelope and transforming-growth-factor-beta signaling connection. GCC2 and CLTB could represent downstream trafficking or vesicle-related consequences rather than members of the same physical complex. This hypothesis predicts that perturbing NELFA or NELFE would alter the co-abundance and transcriptional behavior of selected module members, but the current evidence does not establish those causal links.

### Important genes

#### NELFE

- **Related proteins** (co-abundance neighbors): UIMC1 (0.86), GCC2 (0.83), PUS1 (0.81), RBM27 (0.81), NELFA (0.80); STRING partners: NELFA (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_01088.1, huMAP3_09446.1
- **Function (MyGene.info)**: negative elongation factor complex member E. The protein encoded by this gene is part of a complex termed negative elongation factor (NELF) which represses RNA polymerase II transcript elongation. This protein bears similarity to nuclear RNA-binding proteins; however, it has not been demonstrated that this protein binds RNA. The protein contains a tract of alternating basic and acidic residues, largely arginine (R) and aspartic acid (D). The…
- **Diseases (Open Targets)**: HIV infectious disease (0.592); neurodegenerative disease (0.385); iridocyclitis (0.341); ankylosing spondylitis (0.304); gastric cancer (0.089)
- **Europe PMC papers**: 390
- **Why important**: NELFE is the strongest network-centered gene in the module, linking the NELF core to UIMC1, GCC2, PUS1, and RBM27. It is present in both primary globally corrected terms (GO:CC transcription elongation factor complex; q_global = 0.0212) (GO:CC NELF complex; q_global = 0.038), both supplementary STRING terms (STRING Process Positive regulation of histone H3-K4 methylation; within-query FDR = 0.0312) (STRING Component Nuclear body; within-query FDR = 0.0476), the high-confidence STRING NELFA relationship, and both hu.MAP complexes (hu.MAP huMAP3_01088.1) (hu.MAP huMAP3_09446.1). Its nucleoplasmic and nuclear-body localization and substantial literature support make it the best anchor for interpreting the module.
- **Conclusion**: Established evidence supports NELFE as a component of NELF-mediated RNA polymerase transcriptional pausing and elongation control, and as the principal network bridge in this module. It is plausible, but not established, that NELFE coordinates the module's RNA-processing and DNA-regulatory neighbors in bone and brain.

#### NELFA

- **Related proteins** (co-abundance neighbors): NELFE (0.80); STRING partners: NELFE (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_01088.1, huMAP3_09446.1
- **Function (MyGene.info)**: negative elongation factor complex member A. This gene is expressed ubiquitously with higher levels in fetal than in adult tissues. It encodes a protein sharing 93% sequence identity with the mouse protein. Wolf-Hirschhorn syndrome (WHS) is a malformation syndrome associated with a hemizygous deletion of the distal short arm of chromosome 4. This gene is mapped to the 165 kb WHS critical region, and may play a role in the phenotype of the WH…
- **Diseases (Open Targets)**: HIV infectious disease (0.592); pericarditis (0.160); rectosigmoid junction neoplasm (0.160); esophageal squamous cell carcinoma (0.074); cancer (0.071)
- **Europe PMC papers**: 315
- **Why important**: NELFA forms the module's most strongly supported molecular core with NELFE. It contributes to both primary enrichment terms (GO:CC transcription elongation factor complex; q_global = 0.0212) (GO:CC NELF complex; q_global = 0.038), both hu.MAP complexes (hu.MAP huMAP3_01088.1) (hu.MAP huMAP3_09446.1), the high-confidence STRING pair, and the supplementary nuclear and chromatin annotations (STRING Process Positive regulation of histone H3-K4 methylation; within-query FDR = 0.0312) (STRING Component Nuclear body; within-query FDR = 0.0476). Its known role in transcriptional pausing and its developmental and disease relevance make it essential for distinguishing a genuine NELF-centered signal from a generic housekeeping module.
- **Conclusion**: Established evidence supports NELFA as a NELF complex component involved in transcriptional elongation control. The shared abundance of NELFA with the other module genes suggests coordinated regulation, but does not demonstrate that NELFA directly regulates them or that the program is specific to either bone or brain.

#### SNW1

- **Related proteins** (co-abundance neighbors): UIMC1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SNW domain containing 1. This gene, a member of the SNW gene family, encodes a coactivator that enhances transcription from some Pol II promoters. This coactivator can bind to the ligand-binding domain of the vitamin D receptor and to retinoid receptors to enhance vitamin D-, retinoic acid-, estrogen-, and glucocorticoid-mediated gene expression. It can also function as a splicing factor by interacting with poly(A)-bindin…
- **Diseases (Open Targets)**: cancer (0.580); dengue disease (0.370); neurodegenerative disease (0.261); congenital lactic acidosis, Saguenay-Lac-Saint-Jean type (0.118); chondromalacia (0.052)
- **Europe PMC papers**: 653
- **Why important**: SNW1 is one of the genes in the globally corrected transcription elongation factor complex term (GO:CC transcription elongation factor complex; q_global = 0.0212) and also appears in the supplementary histone and nuclear-body terms (STRING Process Positive regulation of histone H3-K4 methylation; within-query FDR = 0.0312) (STRING Component Nuclear body; within-query FDR = 0.0476). It connects to UIMC1 in the module and has a documented role as a transcriptional coactivator and splicing factor, including regulation of receptor-responsive transcription. Its literature base and links to transcription, splicing, transforming-growth-factor-beta signaling, and DNA-damage responses make it a plausible functional bridge beyond the NELF pair.
- **Conclusion**: Established evidence supports SNW1 as a transcriptional coactivator and splicing-related regulator associated with the enriched complex annotation. Its direct physical relationship to UIMC1 or the wider module is not established here; its bridging role remains a hypothesis.

#### PUS1

- **Related proteins** (co-abundance neighbors): MTHFS (0.86), LEMD3 (0.84), NELFE (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pseudouridine synthase 1. This gene encodes a pseudouridine synthase that converts uridine to pseudouridine once it has been incorporated into an RNA molecule. The encoded enzyme may play an essential role in tRNA function and in stabilizing the secondary and tertiary structure of many RNAs. A mutation in this gene has been linked to mitochondrial myopathy and sideroblastic anemia. Alternate splicing results in multiple tr…
- **Diseases (Open Targets)**: myopathy, lactic acidosis, and sideroblastic anemia (0.819); mitochondrial disease (0.400); Intellectual disability (0.370); sulfite oxidase deficiency due to molybdenum cofactor deficiency type B1 (0.340); hereditary disease (0.193)
- **Europe PMC papers**: 993
- **Why important**: PUS1 occupies a central connecting position between NELFE, MTHFS, and LEMD3, thereby linking the NELF-centered part of the graph to RNA modification, folate metabolism, and nuclear-envelope biology. Its established pseudouridine-synthase function and mitochondrial and RNA-related disease associations provide a biologically meaningful alternative axis for the module. It has no supplied STRING or hu.MAP support, making its co-abundance relationships especially important to test.
- **Conclusion**: Established evidence supports PUS1 as an RNA-modifying enzyme important for pseudouridine synthesis and RNA stability, with disease links involving mitochondrial and hematologic phenotypes. The module data support co-regulation with NELFE, MTHFS, and LEMD3, but do not establish a shared biochemical complex or a direct role in the bone-brain signal.

#### LEMD3

- **Related proteins** (co-abundance neighbors): PUS1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LEM domain containing 3. This locus encodes a LEM domain-containing protein. The encoded protein functions to antagonize transforming growth factor-beta signaling at the inner nuclear membrane. Two transcript variants encoding different isoforms have been found for this gene. Mutations in this gene have been associated with osteopoikilosis, Buschke-Ollendorff syndrome and melorheostosis.[provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: Buschke-Ollendorff syndrome (0.775); osteopoikilosis (0.513); melorheostosis with osteopoikilosis (0.509); hereditary disease (0.471); melorheostosis (0.469)
- **Europe PMC papers**: 553
- **Why important**: LEMD3 is a low-degree peripheral gene, but it is biologically important for interpreting the tissue pair because its known functions include antagonism of transforming-growth-factor-beta and bone morphogenetic protein signaling, and its disease associations include osteopoikilosis, Buschke-Ollendorff syndrome, and melorheostosis. Its edge to PUS1 may connect the transcription and RNA-modification core to a bone-relevant signaling context, although no STRING or hu.MAP relationship is supplied.
- **Conclusion**: Established evidence supports LEMD3 as a nuclear-envelope regulator of transforming-growth-factor-beta and bone morphogenetic protein signaling, with established skeletal disease associations. Its inclusion may provide a mechanistic link to bone biology, but the present network does not show that LEMD3 drives the shared module or connects it directly to brain function.

## Module 5

**Tissue pair**: bone and brain  
**Genes (5)**: EIF3C, PSMG1, RAN, SRP68, SRP72

### Function

The strongest and globally corrected evidence identifies signal recognition particle biology. (GO:MF signal recognition particle binding; q_global = 0.00998) through (GO:CC signal recognition particle; q_global = 0.0405) consistently implicate signal recognition particle binding, seven-S RNA binding, the signal recognition particle, and endoplasmic-reticulum targeting, with SRP68 and SRP72 driving all primary enrichments. Their established function is to support recognition of signal sequences, translational arrest, and cotranslational targeting of secretory and membrane proteins to the endoplasmic reticulum. EIF3C adds translation-initiation biology, while PSMG1 contributes proteasome-assembly chaperone activity and RAN contributes nucleocytoplasmic transport and cell-cycle functions. Thus, the module appears to combine a coherent SRP core with broadly connected protein-synthesis, protein-complex-assembly, and nuclear-transport processes. No within-module GO or KEGG term passed correction, but the globally corrected evidence is sufficient to support the SRP-centered interpretation.

**Cell composition.** This is not a plasma-protein, secreted-protein, or blood-cell-enriched module: the HPA summary reports no secreted genes and low immune-cell specificity for every member. Most genes have low tissue specificity, consistent with broadly expressed intracellular machinery rather than a specialized bone or brain program. Several genes show cell-type enhancement, including neuronal and glial populations for EIF3C and brain protein detection for most members, while PSMG1 is tissue-enhanced in testis and several genes are enriched in reproductive or epithelial cell types. HPA protein data show brain detection but no matching bone tissue dataset, so the evidence does not establish bone-specific protein expression. The shared bone-brain signal could therefore reflect ubiquitous translation and proteostasis machinery, shared cellular composition, or a technical or physiological feature common to both tissues rather than a dedicated bone-brain pathway.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF signal recognition particle binding | 0.00998 | SRP68, SRP72 |
| GO:CC signal recognition particle, endoplasmic reticulum targeting | 0.0405 | SRP68, SRP72 |
| GO:MF 7S RNA binding | 0.0405 | SRP68, SRP72 |
| GO:CC signal recognition particle | 0.0405 | SRP68, SRP72 |

### STRING and hu.MAP

The clearest established relationship is the very strong STRING association between SRP68 and SRP72, matching the known heterodimeric SRP subcomplex and the primary GO evidence. STRING supplementary enrichment independently supports the SRP interpretation through (STRING Keyword Signal recognition particle; within-query FDR = 0.0176) through (STRING COMPARTMENTS Signal recognition particle, endoplasmic reticulum targeting; within-query FDR = 0.0429). (STRING Function Ribonucleoprotein complex binding; within-query FDR = 0.0484) additionally links SRP68, SRP72, and EIF3C through ribonucleoprotein-complex binding. The co-abundance network also contains SRP72–EIF3C, SRP68–PSMG1, and EIF3C–RAN relationships, but only the SRP68–SRP72 pair is represented as a high-confidence STRING interaction in the fact sheet. No hu.MAP complex contains multiple module members. Consequently, the module has a validated SRP core but its full network topology is not an already established physical complex.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: SRP68–SRP72 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Signal recognition particle (FDR = 0.0176, 2 genes); Function Signal recognition particle binding (FDR = 0.0319, 2 genes); Function 7S RNA binding (FDR = 0.0398, 2 genes); Component Signal recognition particle, endoplasmic reticulum targeting (FDR = 0.0402, 2 genes); COMPARTMENTS Signal recognition particle, endoplasmic reticulum targeting (FDR = 0.0429, 2 genes); Function Ribonucleoprotein complex binding (FDR = 0.0484, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The SRP68–SRP72 association and the underlying SRP function are established biology, so that core should not be described as a new molecular discovery. The broader conserved co-abundance pattern linking the SRP core with EIF3C, PSMG1, and RAN across bone and brain may be a new systems-level observation, but the fact sheet does not establish that it is novel. The absence of a hu.MAP complex and the limited STRING support for most edges are compatible with novelty, yet absence from those resources alone cannot prove it. A claim of novelty would require replication in independent cohorts, comparison with published tissue co-expression modules, and testing whether the pattern persists after controlling for cell composition and general expression abundance.

**Hypothesis.** Hypothesis: the conserved module reflects coordinated demand for intracellular protein handling in shared or biologically active cell populations. The SRP68–SRP72 core may coordinate cotranslational delivery of selected membrane and secretory proteins, while EIF3C couples this activity to translation initiation; PSMG1 may connect it to proteasome assembly and RAN may connect it to nuclear transport and proliferative or biosynthetic state. In bone and brain, this could represent a cell-state program supporting production, trafficking, quality control, and turnover of proteins rather than a tissue-specific pathway. This hypothesis is mechanistically plausible but is not directly demonstrated by the co-abundance data.

### Important genes

#### SRP72

- **Related proteins** (co-abundance neighbors): EIF3C (0.85), SRP68 (0.81); STRING partners: SRP68 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal recognition particle 72. This gene encodes the 72 kDa subunit of the signal recognition particle (SRP), a ribonucleoprotein complex that mediates the targeting of secretory proteins to the endoplasmic reticulum (ER). The SRP complex consists of a 7S RNA and 6 protein subunits: SRP9, SRP14, SRP19, SRP54, SRP68, and SRP72, that are bound to the 7S RNA as monomers or heterodimers. SRP has at least 3 distinct functions that c…
- **Diseases (Open Targets)**: autosomal dominant aplasia and myelodysplasia (0.641); neurodegenerative disease (0.416); intracranial subdural hematoma (0.280); type 2 diabetes mellitus (0.044); oropharynx cancer (0.032)
- **Europe PMC papers**: 696
- **Why important**: SRP72 is a central network member, connecting EIF3C and SRP68, and it participates in every primary globally corrected term (GO:MF signal recognition particle binding; q_global = 0.00998) through (GO:CC signal recognition particle; q_global = 0.0405) and every SRP-focused STRING term (STRING Keyword Signal recognition particle; within-query FDR = 0.0176) through (STRING Function Ribonucleoprotein complex binding; within-query FDR = 0.0484). Its established role is as the signal recognition particle subunit that functions with SRP68 and seven-S RNA in cotranslational targeting to the endoplasmic reticulum. It has brain protein detection and substantial literature, with disease associations including aplasia and myelodysplasia and neurodegenerative disease.
- **Conclusion**: Established evidence identifies SRP72 as a principal marker and likely functional anchor of the module. The hypothesis that it organizes the conserved bone-brain co-abundance signal is reasonable from its network position, but the data do not show that SRP72 causally drives the module or has a bone-brain-specific function.

#### SRP68

- **Related proteins** (co-abundance neighbors): PSMG1 (0.84), SRP72 (0.81); STRING partners: SRP72 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal recognition particle 68. This gene encodes a subunit of the signal recognition particle (SRP). The SRP is a ribonucleoprotein complex that transports secreted and membrane proteins to the endoplasmic reticulum for processing. The complex includes a 7S RNA and six protein subunits. The encoded protein is the 68kDa component of the SRP, and forms a heterodimer with the 72kDa subunit that is required for SRP function. Altern…
- **Diseases (Open Targets)**: neurodegenerative disease (0.347); neutropenia, severe congenital, 10, autosomal recessive (0.333); COVID-19 (0.155); metabolic syndrome (0.074); atrial septal defect (0.073)
- **Europe PMC papers**: 440
- **Why important**: SRP68 is the other member of the SRP68–SRP72 heterodimer and participates in every primary term (GO:MF signal recognition particle binding; q_global = 0.00998) through (GO:CC signal recognition particle; q_global = 0.0405) and every SRP-focused STRING term (STRING Keyword Signal recognition particle; within-query FDR = 0.0176) through (STRING Function Ribonucleoprotein complex binding; within-query FDR = 0.0484). Its annotated role is to form the functional SRP subcomplex required for targeting secretory and membrane proteins to the endoplasmic reticulum. It has brain protein detection, disease associations including neurodegenerative disease and severe congenital neutropenia, and a substantial literature base.
- **Conclusion**: The SRP68–SRP72 pair is the strongest established biological core in the module, supported by annotations, enrichment, and STRING. A coordinated SRP activity is therefore well supported; any specific effect on bone or brain physiology remains a hypothesis.

#### EIF3C

- **Related proteins** (co-abundance neighbors): SRP72 (0.85), RAN (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C occupies an internal network position between SRP72 and RAN and is included in the supplementary ribonucleoprotein-complex binding signal (STRING Function Ribonucleoprotein complex binding; within-query FDR = 0.0484). It is an established component of the eukaryotic translation-initiation complex and supports ribosome binding, translational initiation, and positive regulation of translation. HPA reports cell-type enhancement across neuronal and glial populations, and it has a broad literature base and disease associations including neoplasms and a developmental syndrome.
- **Conclusion**: Established evidence supports EIF3C as a plausible bridge between SRP-dependent targeting and general translation initiation. Its brain cell-type pattern makes it relevant to the tissue pair, but the co-abundance data do not establish a direct physical interaction with SRP72 or a specialized brain-bone translation program.

#### PSMG1

- **Related proteins** (co-abundance neighbors): SRP68 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome assembly chaperone 1. Enables molecular adaptor activity. Involved in chaperone-mediated protein complex assembly. Located in several cellular components, including Golgi apparatus; endoplasmic reticulum; and nucleoplasm. Part of chaperone complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.541); intelligence (0.326); smoking initiation (0.322); atrial fibrillation (0.312); attention deficit-hyperactivity disorder (0.240)
- **Europe PMC papers**: 358
- **Why important**: PSMG1 is a peripheral network member linked to SRP68 and is annotated as a proteasome-assembly chaperone involved in chaperone-mediated protein-complex assembly. HPA shows tissue enhancement in testis and cell-type enhancement in germ-cell populations, while protein detection is reported in brain. It has disease associations including neurodegenerative disease and a moderate literature base.
- **Conclusion**: Established evidence supports PSMG1 as a proteostasis-related component that could connect SRP-associated protein production with protein-complex assembly and quality control. Its inclusion may reflect a shared proteostasis state, but its direct functional relationship to the SRP core is not established.

#### RAN

- **Related proteins** (co-abundance neighbors): EIF3C (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAN, member RAS oncogene family. RAN (ras-related nuclear protein) is a small GTP binding protein belonging to the RAS superfamily that is essential for the translocation of RNA and proteins through the nuclear pore complex. The RAN protein is also involved in control of DNA synthesis and cell cycle progression. Nuclear localization of RAN requires the presence of regulator of chromosome condensation 1 (RCC1). Mutations in RAN di…
- **Diseases (Open Targets)**: HIV infectious disease (0.565); Orthomyxoviridae infectious disease (0.376); pemphigus foliaceus (0.298); neurodegenerative disease (0.270); Genu valgum (0.136)
- **Europe PMC papers**: 133080
- **Why important**: RAN is connected to EIF3C in the module and is an extensively studied small GTP-binding protein. Its established functions include nuclear transport, ribosomal-subunit export, DNA synthesis, and cell-cycle control. It has low tissue specificity, low immune-cell specificity, several cell-type enhancements, and disease associations including infectious, neurological, and developmental phenotypes.
- **Conclusion**: Established evidence supports RAN as a broadly important regulator of nucleocytoplasmic transport and biosynthetic state. Its module association may indicate coupling between translation and nuclear transport or proliferative activity, but this coupling is a hypothesis rather than a demonstrated RAN-dependent mechanism.

## Module 6

**Tissue pair**: bone and brain  
**Genes (6)**: FAR1, HNRNPK, PTBP1, SF3B3, SNRNP200, XRCC6

### Function

The strongest and globally corrected functional interpretation is nuclear pre-mRNA splicing through the spliceosome. The same four genes—HNRNPK, PTBP1, SF3B3, and SNRNP200—support both primary GO terms (GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 0.0485) and (GO:BP mRNA splicing, via spliceosome; q_global = 0.0485), which identify spliceosomal mRNA splicing and splicing through transesterification reactions. STRING independently supports this interpretation through mRNA-splicing and spliceosome enrichment (STRING Keyword mRNA splicing; within-query FDR = 0.0123), (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0226), and (STRING Keyword Spliceosome; within-query FDR = 0.0231). SF3B3 and SNRNP200 are components of spliceosomal machinery, while PTBP1 and HNRNPK are RNA-binding regulators of pre-mRNA processing and alternative splicing. XRCC6 and FAR1 suggest possible links to DNA repair and ether-lipid metabolism, respectively, but neither has primary GO/KEGG support in this module. Thus, the best-supported function is a conserved nuclear RNA-processing module, with peripheral connections to genome maintenance and lipid biology.

**Cell composition.** The module is composed entirely of intracellular proteins rather than plasma or secreted proteins; HPA reports no secreted genes. All genes have low tissue specificity, and all are detected in brain by immunohistochemistry. The genes also have low immune-cell specificity, with no recurring enriched blood-cell category, so the module does not strongly resemble a blood-cell or plasma-protein artifact. The absence of matching HPA bone tissue data prevents a direct protein-level comparison in bone. The broadly expressed, mostly nucleoplasmic character is consistent with a housekeeping-like RNA-processing program that can be shared across tissues, although the co-abundance pattern could still reflect shared cellular composition or common cellular state rather than a bone-and-brain-specific mechanism.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile | 0.0485 | HNRNPK, PTBP1, SF3B3, SNRNP200 |
| GO:BP mRNA splicing, via spliceosome | 0.0485 | HNRNPK, PTBP1, SF3B3, SNRNP200 |

### STRING and hu.MAP

STRING provides high-confidence support for a connected core: HNRNPK links to PTBP1 and SF3B3, SF3B3 links to SNRNP200, and HNRNPK also links to XRCC6. The strongest relationships are between HNRNPK and PTBP1 and between SF3B3 and SNRNP200, while the HNRNPK–XRCC6 relationship is weaker but still above the stated confidence threshold. These interactions indicate that the co-abundance structure is not merely a collection of unrelated genes. The STRING functional results (STRING Keyword mRNA splicing; within-query FDR = 0.0123), (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0226), and (STRING Keyword Spliceosome; within-query FDR = 0.0231) reinforce the spliceosomal interpretation, but are supplementary rather than globally corrected evidence. hu.MAP identifies SF3B3 and SNRNP200 together in a large spliceosomal complex (hu.MAP huMAP3_08980.1). This is established complex membership, although only a small portion of that complex is represented in the module; the module therefore appears to capture a focused spliceosomal subnetwork rather than the complete complex.

**STRING interactions (score >= 0.7)**: 4 of 15 gene pairs: HNRNPK–PTBP1 (0.997); HNRNPK–SF3B3 (0.971); HNRNPK–XRCC6 (0.738); SF3B3–SNRNP200 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword mRNA splicing (FDR = 0.0123, 4 genes); RCTM mRNA Splicing - Major Pathway (FDR = 0.0226, 4 genes); Keyword Spliceosome (FDR = 0.0231, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (SNRNP200, SF3B3; 2/97)

### Novelty

The module is unlikely to represent a wholly new molecular function: spliceosomal roles for PTBP1, HNRNPK, SF3B3, and SNRNP200, their STRING relationships, and the SF3B3–SNRNP200 complex association are already established. Its potentially novel aspect is the reproducible co-abundance of this particular combination across bone and brain, especially the inclusion of XRCC6 and FAR1 alongside a spliceosomal core. However, the fact sheet does not provide replication, independent cohorts, perturbation experiments, tissue-cell deconvolution, or a direct comparison with previously reported cross-tissue modules. Therefore, this should be described as a potentially distinctive cross-tissue co-abundance configuration, not as a proven new biological complex or a definitively novel discovery. Absence of hu.MAP or STRING annotations for some genes does not establish novelty.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of nuclear RNA processing across bone and brain, in which a spliceosomal core involving PTBP1, HNRNPK, SF3B3, and SNRNP200 is co-regulated with cellular stress or maintenance programs represented by XRCC6 and FAR1. In brain, this could support the broad pre-mRNA processing demands of neural cells; in bone, it could accompany transcriptional programs in bone-associated cells. The apparent connection to DNA repair through XRCC6 and to peroxisomal ether-lipid synthesis through FAR1 is mechanistically plausible from the annotations, but it is not demonstrated by the enrichment results. Testing this hypothesis would require cell-resolved expression, perturbation of the core splicing genes, and measurement of splicing, DNA-repair, and lipid phenotypes in relevant bone and brain cell types.

### Important genes

#### PTBP1

- **Related proteins** (co-abundance neighbors): SF3B3 (0.82), HNRNPK (0.81), FAR1 (0.81); STRING partners: HNRNPK (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypyrimidine tract binding protein 1. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA-binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.505); dengue disease (0.372); open-angle glaucoma (0.330); glaucoma (0.309); neoplasm (0.116)
- **Europe PMC papers**: 4849
- **Why important**: PTBP1 has the highest network centrality in the module and connects to SF3B3, HNRNPK, and FAR1. It is a ubiquitously expressed heterogeneous nuclear ribonucleoprotein involved in pre-mRNA processing and alternative splicing. It is present in both primary enrichment terms (GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 0.0485) and (GO:BP mRNA splicing, via spliceosome; q_global = 0.0485) and in STRING splicing terms (STRING Keyword mRNA splicing; within-query FDR = 0.0123) and (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0226). Its disease associations include neurodevelopmental disorder and glaucoma, and it has the largest literature volume among the module genes.
- **Conclusion**: Established evidence supports PTBP1 as a central RNA-binding regulator and a major anchor of the module's spliceosomal interpretation. Its disease associations make it biologically relevant to neural tissues, but the module alone does not establish that PTBP1 causes the bone–brain co-abundance pattern or any particular disease phenotype.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): PTBP1 (0.81), XRCC6 (0.81); STRING partners: PTBP1 (0.997), SF3B3 (0.971), XRCC6 (0.738)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is a highly connected bridge in the module, linking PTBP1, SF3B3, and XRCC6. It participates in RNA processing, mRNA splicing, and transcriptional regulation, appears in both primary terms (GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 0.0485) and (GO:BP mRNA splicing, via spliceosome; q_global = 0.0485), and is supported by all listed STRING splicing terms (STRING Keyword mRNA splicing; within-query FDR = 0.0123), (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0226), and (STRING Keyword Spliceosome; within-query FDR = 0.0231). It also has substantial literature coverage and disease associations including Au-Kline syndrome, neurodevelopmental disorder, and neurodegenerative disease.
- **Conclusion**: Established evidence identifies HNRNPK as a multifunctional nuclear RNA-processing protein and a plausible network bridge between splicing and DNA-repair-related biology. Its central position supports importance, but it remains a hypothesis that HNRNPK functionally couples the XRCC6 branch to the spliceosomal core in this module.

#### SF3B3

- **Related proteins** (co-abundance neighbors): PTBP1 (0.82), SNRNP200 (0.82); STRING partners: HNRNPK (0.971), SNRNP200 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Nucleoli rim; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: splicing factor 3b subunit 3. This gene encodes subunit 3 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); dengue disease (0.370); cervical cancer (0.189); cervical carcinoma (0.189); prostate cancer (0.111)
- **Europe PMC papers**: 965
- **Why important**: SF3B3 is a direct component of the SF3B/U2 spliceosomal machinery and connects PTBP1 with SNRNP200. It occurs in both primary GO terms (GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 0.0485) and (GO:BP mRNA splicing, via spliceosome; q_global = 0.0485), all listed STRING splicing terms (STRING Keyword mRNA splicing; within-query FDR = 0.0123), (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0226), and (STRING Keyword Spliceosome; within-query FDR = 0.0231), and the hu.MAP spliceosomal complex (hu.MAP huMAP3_08980.1). Its relationship with SNRNP200 is among the strongest STRING-supported links in the module. It is also associated with neurodegenerative disease and has substantial literature support.
- **Conclusion**: Established evidence makes SF3B3 a core mechanistic member of the module rather than a peripheral correlate. Its network and complex placement strongly support a spliceosome-centered interpretation. The disease associations do not by themselves show that this module mediates neurodegeneration or tissue-specific pathology.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): SF3B3 (0.82); STRING partners: SF3B3 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 encodes a U5 small nuclear ribonucleoprotein component and RNA helicase involved in spliceosome assembly and conformational transitions. It is linked to SF3B3 by an exceptionally strong STRING relationship, appears in both primary enrichment terms (GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 0.0485) and (GO:BP mRNA splicing, via spliceosome; q_global = 0.0485) and all listed STRING splicing terms (STRING Keyword mRNA splicing; within-query FDR = 0.0123), (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.0226), and (STRING Keyword Spliceosome; within-query FDR = 0.0231), and shares the hu.MAP complex (hu.MAP huMAP3_08980.1) with SF3B3. Its disease associations include retinitis pigmentosa, inherited retinal dystrophy, and neurodegenerative disease.
- **Conclusion**: Established evidence places SNRNP200 in the catalytic and remodeling machinery of the spliceosome, making it a strong representative of the module's core function. The reported osteoblast-differentiation annotation provides tissue relevance, but the co-abundance data do not prove that SNRNP200 directly drives differentiation in bone or neural biology here.

## Module 7

**Tissue pair**: bone and brain  
**Genes (8)**: GIPC1, IMPDH1, METAP1, MMTAG2, PPIE, PYM1, SMNDC1, ZCCHC8

### Function

The module does not have a statistically supported GO or KEGG functional enrichment: no globally significant GO/KEGG term passed global correction. The gene annotations nevertheless suggest a heterogeneous cellular program centered on RNA handling, transcript quality control, translation, and protein homeostasis. PPIE links RNA binding and protein folding; SMNDC1 is associated with spliceosomal RNA processing; ZCCHC8 supports nuclear RNA-exosome targeting and RNA degradation; PYM1 participates in exon-junction-complex disassembly, nonsense-mediated decay, and translation; and METAP1 supports protein maturation and translation-related processes. GIPC1 contributes receptor trafficking and synaptic or glutamatergic signaling, while IMPDH1 supplies guanine-nucleotide biosynthesis. Thus, the most defensible interpretation is a candidate shared cellular maintenance program rather than a demonstrated pathway. The absence of globally significant GO/KEGG enrichment does not invalidate the module, but it limits pathway-level confidence.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity and low immune-cell specificity, and the proteins are predominantly nuclear or cytosolic, with additional plasma-membrane, junctional, or specialized retinal localization. Several genes show tissue or cell-type enhancement in esophagus, retina, bone marrow, epithelial populations, photoreceptors, or myeloid cells. IMPDH1 has blood-cell group enrichment, but most genes do not show blood-cell specificity. Brain protein detection is present for most genes with available brain measurements, whereas matching HPA bone tissue protein data are unavailable. Overall, the composition is compatible with broadly expressed, partly housekeeping-like RNA, translation, folding, and nucleotide-metabolism machinery. A shared cell-state or sample-composition contribution remains possible, but a simple plasma-protein or generalized blood-contamination explanation is not supported by the HPA summary.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no supplementary STRING enrichment terms, no high-confidence STRING interaction among the module gene pairs, and no hu.MAP complex containing multiple module members. The co-abundance network therefore does not recapitulate a known high-confidence physical interaction network or a recognized multiprotein complex. PPIE is the central network connector, linking METAP1, GIPC1, SMNDC1, IMPDH1, and MMTAG2, while MMTAG2 connects SMNDC1, ZCCHC8, PYM1, and PPIE. These network relationships may represent coordinated abundance, shared regulation, or indirect cellular context rather than direct binding. Known biology exists for individual genes, especially RNA processing, RNA surveillance, protein folding, trafficking, and nucleotide synthesis, but the module-level relationships are not independently established by STRING or hu.MAP.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The dataset-level co-abundance pattern may be a new observation, particularly because it connects genes from several functional areas in a conserved bone-brain module without corresponding STRING or hu.MAP support. However, absence from those resources does not prove biological novelty: interactions may be transient, indirect, tissue-dependent, technically unresolved, or absent from current databases. The individual genes and many of their functions are already established, with substantial literature for PPIE, ZCCHC8, GIPC1, METAP1, SMNDC1, and especially IMPDH1. The appropriate conclusion is that the shared co-abundance association is potentially novel, while a novel molecular complex or novel mechanism has not been demonstrated.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of RNA maturation and quality control together with translation and protein-homeostasis capacity in a cell population shared by bone and brain. In this model, ZCCHC8 and SMNDC1 represent nuclear RNA surveillance and spliceosomal processing, PYM1 links transcript quality control to translation, and PPIE couples RNA binding with protein folding and acts as the principal abundance-network connector. METAP1 could support maturation of newly synthesized proteins, while IMPDH1 could provide guanine-nucleotide capacity for transcription, translation, and cellular maintenance. GIPC1 may connect this intracellular program to receptor trafficking or synaptic and junctional biology. This is a mechanistic hypothesis, not an established pathway: the lack of globally significant globally significant GO/KEGG terms, STRING enrichment, and hu.MAP support means it requires replication, cell-composition adjustment, perturbation experiments, and direct interaction or regulatory assays.

### Important genes

#### PPIE

- **Related proteins** (co-abundance neighbors): METAP1 (0.89), GIPC1 (0.84), SMNDC1 (0.81), IMPDH1 (0.81), MMTAG2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peptidylprolyl isomerase E. The protein encoded by this gene is a member of the peptidyl-prolyl cis-trans isomerase (PPIase) family. PPIases catalyze the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and accelerate the folding of proteins. This protein contains a highly conserved cyclophilin (CYP) domain as well as an RNA-binding domain. It was shown to possess PPIase and protein folding activities…
- **Diseases (Open Targets)**: dengue disease (0.370); diabetes mellitus (0.102); hemochromatosis type 5 (0.049); sideroblastic anemia 3 (0.049); sleep apnea syndrome (0.047)
- **Europe PMC papers**: 758
- **Why important**: PPIE is the principal network connector in the module and links several otherwise weakly connected genes. Its established functions include peptidyl-prolyl isomerase activity, protein folding, and RNA binding, with annotations involving splicing and transcriptional regulation. It has brain protein detection, a nuclear-speckle location, disease associations including dengue disease and diabetes mellitus, and a substantial literature base.
- **Conclusion**: Established: PPIE is a multifunctional RNA-binding and protein-folding factor and the central connector of this co-abundance subgraph. Hypothesis: its central position may reflect coordination between RNA processing and proteostasis in the shared bone-brain program, but the network does not establish direct binding or causal control by PPIE.

#### ZCCHC8

- **Related proteins** (co-abundance neighbors): MMTAG2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger CCHC-type containing 8. This gene encodes a scaffold protein which serves as an assessory factor to the nuclear RNA exosome complex. The encoded protein forms a trimeric human nuclear exosome targeting (NEXT) complex, together with hMTR4 and the RNA-binding factor RBM7 which promotes the exosomal degradation of non-coding promoter-upstream transcripts, enhancer RNAs and 3'-extended products of histone- and small nuclear …
- **Diseases (Open Targets)**: pulmonary fibrosis, and/or bone marrow failure, telomere-related, 5 (0.562); neurodegenerative disease (0.460); dyskeratosis congenita (0.355); inherited aplastic anemia (0.333); inherited acute myeloid leukemia (0.266)
- **Europe PMC papers**: 597
- **Why important**: ZCCHC8 provides the clearest link to nuclear RNA surveillance. It is an accessory scaffold for the NEXT RNA-exosome targeting complex and is associated with degradation of noncoding transcripts, enhancer-related transcripts, intronic RNA, and RNA-processing products. It is tissue-enhanced in bone marrow, detected in brain, and has disease associations involving telomere-related bone-marrow failure, dyskeratosis congenita, neurodegenerative disease, and inherited marrow disorders.
- **Conclusion**: Established: ZCCHC8 participates in nuclear RNA processing and degradation and has relevant marrow and neurological disease connections. Hypothesis: its co-abundance with PPIE, MMTAG2, and the broader module may indicate coordinated RNA quality control in bone- and brain-related cells, but no direct module complex is demonstrated.

#### SMNDC1

- **Related proteins** (co-abundance neighbors): MMTAG2 (0.88), PPIE (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: survival motor neuron domain containing 1. This gene is a paralog of SMN1 gene, which encodes the survival motor neuron protein, mutations in which are cause of autosomal recessive proximal spinal muscular atrophy. The protein encoded by this gene is a nuclear protein that has been identified as a constituent of the spliceosome complex. This gene is differentially expressed, with abundant levels in skeletal muscle, and may share similar ce…
- **Diseases (Open Targets)**: dengue disease (0.370); premature birth (0.318); Splenomegaly (0.265); Abnormality of the skeletal system (0.204); pneumoconiosis (0.185)
- **Europe PMC papers**: 256
- **Why important**: SMNDC1 is a spliceosome-associated nuclear protein with established roles in RNA splicing, mRNA processing, and apoptosis-related biology. It is connected in the module to PPIE and MMTAG2 and has disease associations including skeletal-system abnormality, splenomegaly, and premature birth. Its literature base is substantial enough to support a meaningful interpretation despite the absence of enrichment evidence.
- **Conclusion**: Established: SMNDC1 is a nuclear RNA-processing factor associated with the spliceosome. Hypothesis: it may help explain the module's RNA-processing axis and its conservation across bone and brain, but its module-level role remains inferential because no globally significant globally significant GO/KEGG term or known complex supports the connection.

#### GIPC1

- **Related proteins** (co-abundance neighbors): PPIE (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GIPC PDZ domain containing family member 1. GIPC1 is a scaffolding protein that regulates cell surface receptor expression and trafficking (Lee et al., 2008 [PubMed 18775991]).[supplied by OMIM, Apr 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); oculopharyngodistal myopathy 2 (0.409); oculopharyngodistal myopathy (0.376); smoking initiation (0.205); risk-taking behaviour (0.192)
- **Europe PMC papers**: 653
- **Why important**: GIPC1 is a membrane and cell-junction scaffold that regulates receptor trafficking, actin organization, G-protein signaling, and glutamate secretion. It is tissue-enhanced in esophagus, enriched or enhanced in several epithelial cell populations, detected in brain, and associated with neurodegenerative disease and oculopharyngodistal myopathy. Its connection to the central PPIE node makes it important for interpreting the module as more than a purely nuclear RNA-processing signal.
- **Conclusion**: Established: GIPC1 supports receptor trafficking and cell-surface or synaptic signaling and has a relevant brain-associated disease context. Hypothesis: GIPC1 may mark a cell-state or trafficking component that couples the intracellular maintenance program to membrane or synaptic biology; the co-abundance data do not establish a direct PPIE-GIPC1 mechanism.

#### IMPDH1

- **Related proteins** (co-abundance neighbors): PPIE (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol, Rods & Rings; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inosine monophosphate dehydrogenase 1. The protein encoded by this gene acts as a homotetramer to regulate cell growth. The encoded protein is an enzyme that catalyzes the synthesis of xanthine monophosphate (XMP) from inosine-5'-monophosphate (IMP). This is the rate-limiting step in the de novo synthesis of guanine nucleotides. Defects in this gene are a cause of retinitis pigmentosa type 10 (RP10). Several transcript variants encodin…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.725); retinitis pigmentosa 10 (0.683); Leber congenital amaurosis (0.625); chronic hepatitis C virus infection (0.604); hepatitis C virus infection (0.602)
- **Europe PMC papers**: 1978
- **Why important**: IMPDH1 is the best-supported metabolic and disease-linked gene in the module. It catalyzes a rate-limiting step in de novo guanine-nucleotide synthesis, is tissue-enhanced in retina, is detected in brain, and is associated with retinitis pigmentosa, Leber congenital amaurosis, and viral infection phenotypes. It also shows enrichment across several myeloid and granulocyte populations, making it important for evaluating possible cell-composition effects. Its literature volume is extensive.
- **Conclusion**: Established: IMPDH1 supplies guanine-nucleotide biosynthetic capacity, has strong retinal and inherited-eye-disease relevance, and may reflect myeloid-cell composition in some samples. Hypothesis: its co-abundance with PPIE could indicate coupling between nucleotide availability and RNA or protein maintenance, but the module does not prove that metabolic coupling.

## Module 8

**Tissue pair**: bone and brain  
**Genes (8)**: KIF2C, LARP4, NCOR2, PPP4R2, PRRC2C, TIA1, TRIM33, ZC3H4

### Function

The module does not have a statistically supported GO or KEGG functional enrichment: no GO/KEGG term passed global correction, and there was no supplementary STRING enrichment. Its gene annotations nevertheless suggest a mixed regulatory program rather than a single established pathway. ZC3H4 and NCOR2 support transcriptional and nuclear RNA regulation; LARP4, PRRC2C, and TIA1 support post-transcriptional control, translation, RNA binding, and stress-granule biology; PPP4R2 contributes phosphatase-regulated DNA repair and microtubule organization; and KIF2C contributes microtubule dynamics and chromosome segregation. The co-abundance pattern is therefore most consistent with coordinated regulation of RNA handling, transcriptional repression, stress responses, cytoskeletal organization, and cell-cycle-related processes, but this interpretation remains integrative rather than enrichment-supported.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and protein detection is reported in brain for most genes with available brain measurements. However, the module is not uniformly brain-specific. KIF2C is enriched in bone marrow, lymphoid tissue, and testis and is associated with late spermatids and T-reg cells; PPP4R2 is enhanced in neutrophils; LARP4 is enhanced in myonuclei; TIA1 is enhanced in late primary spermatocytes, platelets, and tuft cells; and TRIM33 and NCOR2 are enhanced in basophils. These findings indicate a broadly expressed intracellular module with contributions from immune, blood, reproductive, and other cell populations. The shared bone–brain signal could therefore partly reflect common cellular composition, blood or immune material, or broadly expressed housekeeping and regulatory programs rather than a bone–brain-specific mechanism. Bone protein detection cannot be evaluated because matching HPA bone tissue data were unavailable.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, there was no STRING functional enrichment, and no hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated here as established physical protein interactions or a known multisubunit complex. The strongest network connections place ZC3H4 and LARP4 near the center of the co-abundance subgraph, with links extending toward RNA-related genes and transcriptional regulators, while the remaining genes form more peripheral connections. The absence of STRING and hu.MAP support argues against describing this module as a known protein complex. It may instead represent coordinated expression across distinct intracellular processes, indirect regulation, shared cell-state dependence, or technical and compositional covariance.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module cannot be called a definitively new biological discovery from the supplied evidence. Its exact co-abundance configuration may be novel in this bone–brain analysis, but that requires comparison with prior co-expression studies, independent cohorts, and matched cell-type or bulk-tissue datasets. The lack of high-confidence STRING interactions and hu.MAP complexes is compatible with a previously unassembled regulatory association, but absence from those resources does not establish novelty. The lack of globally significant GO or KEGG enrichment also prevents assigning novelty or validity on the basis of pathway enrichment. The most defensible conclusion is that the module is a potentially novel dataset-level co-abundance pattern whose biological specificity remains unconfirmed.

**Hypothesis.** Hypothesis: the module captures a shared intracellular cell-state program in bone and brain samples in which RNA processing, translation control, stress-granule behavior, transcriptional repression, DNA-repair regulation, and cytoskeletal or mitotic organization fluctuate together. A plausible explanation is that the apparent cross-tissue conservation is driven partly by broadly expressed regulatory genes and partly by shared or contaminating immune, blood, or other cell populations. This hypothesis predicts that the module will be more strongly associated with cell composition and stress or proliferative state than with a single specialized bone or neural function. It should be tested by cell-type deconvolution, single-cell or spatial data, replication in independent cohorts, and perturbation of the central RNA-regulatory connections.

### Important genes

#### ZC3H4

- **Related proteins** (co-abundance neighbors): LARP4 (0.83), PRRC2C (0.82), NCOR2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger CCCH-type containing 4. This gene encodes a member of a family of CCCH (C-x8-C-x5-C-x3-H type) zinc finger domain-containing proteins. These zinc finger domains, which coordinate zinc finger binding and are characterized by three cysteine residues and one histidine residue, are nucleic acid-binding. Other family members are known to function in post-transcriptional regulation. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.415); Abnormality of the skeletal system (0.355); Chest pain (0.352); neurodegenerative disease (0.344); obesity disorder (0.293)
- **Europe PMC papers**: 309
- **Why important**: ZC3H4 has a central position in the module and connects the RNA-associated genes LARP4 and PRRC2C with the transcriptional corepressor NCOR2. Its annotations support negative regulation of transcription, transcriptional elongation, nuclear RNA surveillance, and lncRNA catabolism. It is broadly expressed, detected in brain, and has disease associations involving skeletal abnormality, neurodegenerative disease, and metabolic disorders. Its literature volume is moderate relative to the most heavily studied genes in the module.
- **Conclusion**: Established evidence supports ZC3H4 as a nucleic-acid-binding and transcriptional or RNA-surveillance regulator with a central position in this co-abundance pattern. Hypothesis: ZC3H4 may help connect nuclear RNA quality control with transcriptional repression in the shared module, but the module does not establish a direct biochemical interaction or a bone–brain-specific role.

#### LARP4

- **Related proteins** (co-abundance neighbors): ZC3H4 (0.83), TIA1 (0.81), TRIM33 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: La ribonucleoprotein 4. Enables mRNA 3'-UTR binding activity and poly(A) binding activity. Involved in cytoskeleton organization; positive regulation of translation; and regulation of cell morphogenesis. Located in cytosol. Colocalizes with cytoplasmic stress granule; cytosolic small ribosomal subunit; and polysome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: cardiac transplant (0.230); Alzheimer disease (0.178); neoplasm (0.096); osteosarcoma (0.079); breast cancer (0.078)
- **Europe PMC papers**: 540
- **Why important**: LARP4 is one of the most connected genes in the module and links ZC3H4 with TIA1 and TRIM33. It binds messenger RNA three-prime untranslated regions and polyadenylated RNA, promotes translation, and is associated with polysomes and cytoplasmic stress granules. It is detected in brain, has an association with myonuclei, and has reported links to Alzheimer disease and osteosarcoma. Its literature volume is substantial.
- **Conclusion**: Established evidence supports LARP4 as a plausible post-transcriptional and translational regulator occupying a central network position. Hypothesis: LARP4 may coordinate translation with stress-granule or cytoskeletal state across the sampled tissues, although no direct interaction with the neighboring module genes is supported by STRING or hu.MAP here.

#### TIA1

- **Related proteins** (co-abundance neighbors): LARP4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TIA1 cytotoxic granule associated RNA binding protein. The product encoded by this gene is a member of a RNA-binding protein family and possesses nucleolytic activity against cytotoxic lymphocyte (CTL) target cells. It has been suggested that this protein may be involved in the induction of apoptosis as it preferentially recognizes poly(A) homopolymers and induces DNA fragmentation in CTL targets. The major granule-associated species is a 15-kDa prote…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis 26 with or without frontotemporal dementia (0.663); distal myopathy, Welander type (0.648); Abnormality of the skeletal system (0.530); hereditary disease (0.187); neoplasm (0.114)
- **Europe PMC papers**: 3316
- **Why important**: TIA1 connects to LARP4 and provides a strong mechanistic link to RNA metabolism and stress responses. Its annotations include RNA binding, alternative splicing, negative regulation of translation, apoptosis, and cytoplasmic stress-granule localization. It is enhanced in several specialized cell types, including platelets and late primary spermatocytes, and it has substantial literature coverage. Its disease associations include amyotrophic lateral sclerosis with or without frontotemporal dementia and a distal myopathy.
- **Conclusion**: Established evidence supports TIA1 as an RNA-binding stress and translation regulator with relevance to neuromuscular disease. Hypothesis: TIA1 may be a functional readout of cellular stress or altered ribonucleoprotein handling in the module, but its cell-type associations also make a compositional explanation plausible.

#### NCOR2

- **Related proteins** (co-abundance neighbors): ZC3H4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Immune cell enhanced; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nuclear receptor corepressor 2. This gene encodes a nuclear receptor co-repressor that mediates transcriptional silencing of certain target genes. The encoded protein is a member of a family of thyroid hormone- and retinoic acid receptor-associated co-repressors. This protein acts as part of a multisubunit complex which includes histone deacetylases to modify chromatin structure that prevents basal transcriptional activity of ta…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.493); prostate adenocarcinoma (0.443); colorectal adenocarcinoma (0.412); smoking initiation (0.403); respiratory system disorder (0.398)
- **Europe PMC papers**: 3320
- **Why important**: NCOR2 links to ZC3H4 and represents the transcriptional-repression arm of the module. It mediates nuclear receptor-associated transcriptional silencing and participates in chromatin modification through corepressor complexes. It is detected in brain, is immune-cell enhanced in basophils, has associations with skeletal abnormality and multiple cancers, and has extensive literature coverage.
- **Conclusion**: Established evidence supports NCOR2 as a transcriptional corepressor capable of coupling cellular state and receptor signaling to gene-expression programs. Hypothesis: NCOR2 may help explain why the module spans nuclear regulation and RNA control, but the present data do not show that NCOR2 directly regulates the other module members.

#### KIF2C

- **Related proteins** (co-abundance neighbors): TRIM33 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Immune cell enhanced; location Nucleoplasm, Midbody, Centrosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 2C. This gene encodes a kinesin-like protein that functions as a microtubule-dependent molecular motor. The encoded protein can depolymerize microtubules at the plus end, thereby promoting mitotic chromosome segregation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.320); Abnormality of the skeletal system (0.165); placenta praevia (0.159); neuroendocrine neoplasm (0.159); placental retention (0.129)
- **Europe PMC papers**: 2214
- **Why important**: KIF2C is connected to TRIM33 and supplies the clearest cytoskeletal and proliferative component. It is a microtubule-dependent motor involved in microtubule depolymerization, chromosome alignment, chromosome segregation, and intracellular transport. Unlike most module genes, it is group-enriched in bone marrow, lymphoid tissue, and testis, with cell-type enrichment in late spermatids and immune enhancement in T-reg cells. It has extensive literature coverage and reported associations with neurodegenerative disease and skeletal abnormality.
- **Conclusion**: Established evidence supports KIF2C as a mitotic microtubule regulator, while its HPA pattern raises a strong possibility that cell composition contributes to the shared module. Hypothesis: KIF2C may mark a proliferative or cytoskeletal cell-state component rather than a core bone–brain mechanism; this should be tested by controlling for proliferating and immune cell populations.
