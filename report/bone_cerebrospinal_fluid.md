# Conserved co-abundance modules: bone and cerebrospinal_fluid

## Module 0

**Tissue pair**: bone and cerebrospinal_fluid  
**Genes (8)**: ALDOC, GSN, GSTP1, SERPINB1, LDHA, LDHB, MDH1, PGK1

### Function

The strongest interpretation is a shared central-carbon and redox-metabolism module. The primary evidence is the concordant enrichment of organic-acid, carboxylic-acid, and oxoacid metabolic processes (GO:BP organic acid metabolic process; q_global = 0.0353)(GO:BP carboxylic acid metabolic process; q_global = 0.0353)(GO:BP oxoacid metabolic process; q_global = 0.0353), all driven by ALDOC, GSTP1, LDHA, LDHB, MDH1, and PGK1. These genes collectively represent glycolysis, lactate and pyruvate interconversion, cytosolic malate metabolism, and glutathione-linked detoxification. The network is therefore consistent with coordinated metabolic state rather than a narrowly specialized signaling pathway. The acetylation keyword (STRING Keyword Acetylation; within-query FDR = 0.0148) is supplementary and may indicate shared regulation or protein modification, but it is not primary global enrichment evidence.

**Cell composition.** This is not predominantly a plasma or secreted-protein module and does not appear to be a blood-cell-enriched module. GSN and SERPINB1 are secreted to blood, but the remaining genes are not annotated as secreted, and most genes have low immune-cell specificity. HPA profiles instead point to a heterogeneous mixture of tissue-associated metabolic programs, including heart muscle, esophagus, brain, retina, kidney, tongue, and bone marrow, with cell-type signals in epithelial cells, neural cells, parietal cells, neutrophil-related cells, and other specialized populations. ALDOC provides a particularly relevant brain and glial or neuronal signal, whereas SERPINB1 and GSN could reflect extracellular or inflammatory components. Because HPA reports no matching protein-detection result for either sampled tissue, the module should not be interpreted as direct protein-level evidence in bone or cerebrospinal fluid. Shared cell composition, tissue injury, or general metabolic state remain plausible contributors.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP organic acid metabolic process | 0.0353 | ALDOC, GSTP1, LDHA, LDHB, MDH1, PGK1 |
| GO:BP carboxylic acid metabolic process | 0.0353 | ALDOC, GSTP1, LDHA, LDHB, MDH1, PGK1 |
| GO:BP oxoacid metabolic process | 0.0353 | ALDOC, GSTP1, LDHA, LDHB, MDH1, PGK1 |

### STRING and hu.MAP

STRING supports a compact glycolytic core: ALDOC is strongly connected to LDHA and PGK1, and LDHA is strongly connected to PGK1. These relationships agree with the functional interpretation and indicate that part of the module reflects already established molecular biology rather than an arbitrary correlation pattern. STRING does not provide listed interactions for LDHB, MDH1, or SERPINB1 within this module, and the STRING acetylation keyword (STRING Keyword Acetylation; within-query FDR = 0.0148) is supplementary rather than globally corrected enrichment. hu.MAP provides independent support for an LDHA-LDHB association through several lactate-dehydrogenase related complexes (hu.MAP huMAP3_06798.1)(hu.MAP huMAP3_09010.1)(hu.MAP huMAP3_14812.1)(hu.MAP huMAP3_12061.1), although those complexes also contain members outside the module. No hu.MAP complex is listed for the other module genes. Together, the evidence supports a real metabolic backbone with additional co-abundance links that may reflect shared regulation, cellular mixture, or context-dependent biology.

**STRING interactions (score >= 0.7)**: 3 of 28 gene pairs: ALDOC–LDHA (0.93); ALDOC–PGK1 (0.835); LDHA–PGK1 (0.923)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Acetylation (FDR = 0.0148, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06798.1 (LDHA, LDHB; 2/3); huMAP3_09010.1 (LDHA, LDHB; 2/5); huMAP3_14812.1 (LDHA, LDHB; 2/5); huMAP3_12061.1 (LDHA, LDHB; 2/6)

### Novelty

The biochemical theme itself is not new: glycolysis, lactate metabolism, cytosolic malate metabolism, glutathione-related detoxification, and the LDHA-LDHB relationship are established biology. The direct STRING relationships and hu.MAP lactate-dehydrogenase complexes further argue against claiming that the entire module is a newly discovered molecular complex. A potentially novel aspect is the coordinated occurrence of this metabolic signature across bone and cerebrospinal-fluid co-abundance data, especially the specific combination of a glycolytic core with GSN, GSTP1, MDH1, and SERPINB1. However, the fact sheet does not include a comparison against prior cross-tissue modules or the literature, so this cross-tissue organization should be described as a candidate context-specific finding rather than a demonstrated new discovery. Absence from STRING or hu.MAP alone cannot establish novelty.

**Hypothesis.** Hypothesis: the shared module reflects a conserved metabolic-state program present in cells or extracellular material represented in both bone and cerebrospinal-fluid samples. The ALDOC-PGK1-LDHA backbone may coordinate glycolytic carbon flow and lactate handling, while LDHB and MDH1 extend the signal toward lactate balance and cytosolic redox transfer. GSTP1 may connect this metabolic state to oxidative or electrophilic stress, and GSN plus SERPINB1 may report cytoskeletal or protease-control responses associated with tissue remodeling, injury, or inflammatory exposure. This is a mechanistic hypothesis, not proof of physical interaction, secretion into cerebrospinal fluid, or a bone-specific pathway. It should be tested with cell-resolved measurements, matched protein assays, and analyses that separate tissue composition from within-cell metabolic regulation.

### Important genes

#### PGK1

- **Related proteins** (co-abundance neighbors): ALDOC (0.90), LDHA (0.89), GSN (0.87), GSTP1 (0.85), MDH1 (0.83), LDHB (0.82); STRING partners: ALDOC (0.835), LDHA (0.923)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece, Principal piece, End piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglycerate kinase 1. The protein encoded by this gene is a glycolytic enzyme that catalyzes the conversion of 1,3-diphosphoglycerate to 3-phosphoglycerate. The encoded protein may also act as a cofactor for polymerase alpha. Additionally, this protein is secreted by tumor cells where it participates in angiogenesis by functioning to reduce disulfide bonds in the serine protease, plasmin, which consequently leads to th…
- **Diseases (Open Targets)**: glycogen storage disease due to phosphoglycerate kinase 1 deficiency (0.823); Menkes disease (0.578); X-linked distal spinal muscular atrophy type 3 (0.556); occipital horn syndrome (0.556); hereditary disease (0.520)
- **Europe PMC papers**: 14784
- **Why important**: PGK1 is the most connected and strongest-linked node in the module, linking ALDOC, LDHA, GSN, GSTP1, MDH1, and LDHB. It is a glycolytic enzyme and participates in the globally significant metabolic terms (GO:BP organic acid metabolic process; q_global = 0.0353)(GO:BP carboxylic acid metabolic process; q_global = 0.0353)(GO:BP oxoacid metabolic process; q_global = 0.0353), as well as the supplementary acetylation signal (STRING Keyword Acetylation; within-query FDR = 0.0148). Its extensive literature and disease associations make it the best network anchor for interpreting the module.
- **Conclusion**: Established: PGK1 is a central glycolytic enzyme and a hub of the observed co-abundance structure. Hypothesis: PGK1 may organize the module around coordinated glycolytic flux or cellular energetic state, but the network does not establish a direct regulatory role for PGK1 in the other genes.

#### LDHA

- **Related proteins** (co-abundance neighbors): PGK1 (0.89), LDHB (0.87); STRING partners: ALDOC (0.93), PGK1 (0.923)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06798.1, huMAP3_09010.1, huMAP3_14812.1, huMAP3_12061.1
- **Function (MyGene.info)**: lactate dehydrogenase A. This gene encodes the A subunit of lactate dehydrogenase enzyme which catalyzes the reversible conversion of pyruvate to lactate with the concomitant oxidation of NADH to NAD in anaerobic glycolysis. The protein is found predominantly in skeletal muscle and belongs to the lactate dehydrogenase family. Mutations in this gene have been linked to exertional myoglobinuria. The human genome contains se…
- **Diseases (Open Targets)**: glycogen storage disease due to lactate dehydrogenase M-subunit deficiency (0.755); disorder of glycogen metabolism (0.505); glycogen storage disease XV (0.505); primary hyperoxaluria (0.447); hereditary disease (0.190)
- **Europe PMC papers**: 20747
- **Why important**: LDHA is part of all primary metabolic enrichments (GO:BP organic acid metabolic process; q_global = 0.0353)(GO:BP carboxylic acid metabolic process; q_global = 0.0353)(GO:BP oxoacid metabolic process; q_global = 0.0353), directly connects to PGK1 and LDHB in the module, and has strong STRING support with ALDOC and PGK1. It is also represented in every listed hu.MAP complex (hu.MAP huMAP3_06798.1)(hu.MAP huMAP3_09010.1)(hu.MAP huMAP3_14812.1)(hu.MAP huMAP3_12061.1), making it the principal bridge between the glycolytic network and the lactate-dehydrogenase complex evidence. It has extensive literature and established metabolic-disease associations.
- **Conclusion**: Established: LDHA provides a strong biochemical and network rationale for glycolytic and lactate-related interpretation. Hypothesis: its co-abundance with LDHB may reflect coordinated control of pyruvate-lactate balance in the shared sample context, rather than formation of a single complete complex in every sample.

#### ALDOC

- **Related proteins** (co-abundance neighbors): PGK1 (0.90); STRING partners: LDHA (0.93), PGK1 (0.835)
- **HPA**: Group enriched; Group enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldolase, fructose-bisphosphate C. This gene encodes a member of the class I fructose-biphosphate aldolase gene family. Expressed specifically in the hippocampus and Purkinje cells of the brain, the encoded protein is a glycolytic enzyme that catalyzes the reversible aldol cleavage of fructose-1,6-biphosphate and fructose 1-phosphate to dihydroxyacetone phosphate and either glyceraldehyde-3-phosphate or glyceraldehyde, respectively…
- **Diseases (Open Targets)**: glioblastoma (0.098); non-small cell lung carcinoma (0.096); gastric cancer (0.087); breast cancer (0.085); breast carcinoma (0.084)
- **Europe PMC papers**: 2686
- **Why important**: ALDOC participates in all primary metabolic terms (GO:BP organic acid metabolic process; q_global = 0.0353)(GO:BP carboxylic acid metabolic process; q_global = 0.0353)(GO:BP oxoacid metabolic process; q_global = 0.0353) and forms strong STRING-supported links to LDHA and PGK1. Its HPA annotation is group-enriched in brain and retina and includes astrocytes and neuronal populations, which is especially relevant to a module shared with cerebrospinal fluid. Its established role in fructose-bisphosphate cleavage adds a brain-associated glycolytic dimension to the module.
- **Conclusion**: Established: ALDOC is a brain- and retina-associated glycolytic enzyme that anchors the neural relevance of the module. Hypothesis: ALDOC may help explain why a general metabolic program is conserved in cerebrospinal-fluid-associated material, but the data do not prove that neural cells are the source in either tissue.

#### GSN

- **Related proteins** (co-abundance neighbors): PGK1 (0.87), MDH1 (0.83), SERPINB1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gelsolin. The protein encoded by this gene binds to the 'plus' ends of actin monomers and filaments to prevent monomer exchange. The encoded calcium-regulated protein functions in both assembly and disassembly of actin filaments. Defects in this gene are a cause of familial amyloidosis Finnish type (FAF). Multiple transcript variants encoding several different isoforms have been found for this gene. [provid…
- **Diseases (Open Targets)**: Finnish type amyloidosis (0.805); AL amyloidosis (0.463); neuropathy (0.418); cardiomyopathy (0.418); cutis laxa (0.417)
- **Europe PMC papers**: 5062
- **Why important**: GSN connects PGK1, MDH1, and SERPINB1, thereby linking the metabolic backbone to cytoskeletal and extracellular biology. It is tissue-enhanced in heart muscle, cell-type enhanced across several epithelial, stromal, and endothelial populations, and is annotated as secreted to blood. Its established actin-remodeling function and disease associations make it informative for distinguishing a purely metabolic module from a broader tissue-state or extracellular-response module.
- **Conclusion**: Established: GSN is an actin-regulatory protein with a secreted-to-blood annotation and a bridging position in the network. Hypothesis: GSN may reflect extracellular material, tissue remodeling, or cell-state composition contributing to the shared co-abundance pattern, but its link to the metabolic genes is not independently validated by the listed STRING or hu.MAP evidence.

#### SERPINB1

- **Related proteins** (co-abundance neighbors): GSN (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytoplasmic bodies; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family B member 1. The protein encoded by this gene is a member of the serpin family of proteinase inhibitors. Members of this family maintain homeostasis by neutralizing overexpressed proteinase activity through their function as suicide substrates. This protein inhibits the neutrophil-derived proteinases neutrophil elastase, cathepsin G, and proteinase-3 and thus protects tissues from damage at inflammatory sites.…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.089); neoplasm (0.086); benign chondrogenic neoplasm (0.079); infection (0.078); isolated agammaglobulinemia (0.076)
- **Europe PMC papers**: 1419
- **Why important**: SERPINB1 is connected to GSN and contributes to the supplementary acetylation keyword (STRING Keyword Acetylation; within-query FDR = 0.0148). HPA places it in bone marrow and esophagus, with signals in neutrophils and neutrophil progenitors, and annotates it as secreted to blood. Its established role as an inhibitor of neutrophil proteases and tissue-protective inflammatory factor provides a possible bridge from metabolism to protease control and tissue stress.
- **Conclusion**: Established: SERPINB1 is a cytoplasmic serpin associated with neutrophil-protease control and has a secreted-to-blood annotation. Hypothesis: its co-abundance may mark inflammatory or injury-related material accompanying the metabolic program, but the low overall immune-cell specificity and limited network connectivity argue against assigning the whole module to neutrophils.

## Module 1

**Tissue pair**: bone and cerebrospinal_fluid  
**Genes (5)**: SMPDL3B, PRNP, THY1, TWSG1, AXL

### Function

The module is most consistently interpreted as an immune-regulatory and tissue-interface program. The sole globally supported GO term, (GO:BP negative regulation of immune system process; q_global = 0.0138), is negative regulation of immune system process and includes every module gene: AXL, PRNP, SMPDL3B, THY1, and TWSG1. The annotations support complementary mechanisms rather than a single canonical complex: AXL mediates TAM-family receptor signaling, cytokine regulation, and phagocytosis; SMPDL3B is linked to membrane-lipid catabolism and negative regulation of inflammatory and Toll-like receptor signaling; THY1 participates in cell adhesion, cell communication, and immune-system regulation; TWSG1 modulates BMP and TGF-beta-related signaling and can restrain T-cell activation; and PRNP has annotations involving acute inflammatory responses, oxidative stress, ischemia, and intracellular copper homeostasis. The co-abundance graph is connected, with PRNP occupying the most central bridging position and linking to SMPDL3B, AXL, and TWSG1, while SMPDL3B links to THY1. This structure is compatible with a coordinated regulatory interface involving immune tone, cell adhesion, extracellular signaling, and membrane biology. No STRING functional-enrichment term was available, so the GO result is the primary functional evidence rather than STRING enrichment.

**Cell composition.** This does not appear to be a simple plasma-protein module or a uniformly blood-cell-derived module. SMPDL3B is secreted to blood and TWSG1 is annotated as secreted with an unknown location, whereas the remaining genes are not annotated as secreted. HPA tissue patterns are heterogeneous, including choroid plexus, brain, intestine, pancreas, and smooth muscle, and the single-cell annotations span epithelial, stromal, neural, hepatic, and immune-associated cell types. Blood-cell evidence is mixed: SMPDL3B is enriched in several myeloid-associated blood-cell categories, AXL is enhanced in natural-killer and plasmacytoid-dendritic-cell categories, PRNP is enriched in basophils, TWSG1 has low immune-cell specificity, and THY1 is not detected in immune cells. Thus, the shared bone–cerebrospinal-fluid signal could reflect a conserved tissue-interface or stromal/vascular program, with possible contribution from blood or immune-cell composition, but the HPA evidence does not justify assigning the module solely to blood contamination. HPA provides no matching protein-detection evidence for either bone or cerebrospinal fluid, so tissue-level protein localization in the two studied groups remains unresolved.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP negative regulation of immune system process | 0.0138 | AXL, PRNP, SMPDL3B, THY1, TWSG1 |

### STRING and hu.MAP

No high-confidence STRING interaction was reported among any gene pair in this module, and no STRING functional-enrichment term was available. No hu.MAP complex contained multiple module members. Therefore, the co-abundance relationships are not corroborated here by known physical interactions or membership in a curated human molecular complex. This does not invalidate the module: co-abundance can arise from coordinated regulation, shared cellular origin, common extracellular context, or indirect pathway coupling. The graph nevertheless has biologically interpretable internal structure, with PRNP as the principal connector and SMPDL3B linking PRNP to THY1. These edges should be regarded as module-level associations rather than established biochemical interactions.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unrecognized cross-tissue co-abundance pattern, because its gene set has no reported high-confidence STRING interactions, no multi-member hu.MAP complex, and no STRING enrichment signal. However, those absences do not establish novelty: the individual genes and several of their functions are well studied, and the globally supported immune-regulatory annotation is consistent with existing biology. The defensible conclusion is that the specific coordinated pattern across bone and cerebrospinal fluid is potentially novel, while the underlying gene functions and broad immune-regulatory themes are not novel. Replication in independent cohorts, control for cell composition and blood contribution, and comparison with published bone, cerebrospinal-fluid, and proteomic co-abundance modules would be needed before calling it a new biological mechanism.

**Hypothesis.** Hypothesis: this module reflects a conserved tissue-interface program in which stromal, neural or barrier-associated cells coordinate immune restraint with extracellular-matrix communication, membrane-lipid handling, and BMP/TGF-beta signaling. In this model, AXL provides a receptor-signaling and phagocytic component, SMPDL3B adjusts membrane-derived inflammatory signals, THY1 marks adhesion and cell-contact regulation, TWSG1 tunes BMP/TGF-beta activity and T-cell responses, and PRNP serves as a central stress-responsive membrane-associated connector. The shared abundance pattern in bone and cerebrospinal fluid could therefore arise from coordinated regulation of resident interface cells, with a possible additional contribution from immune-cell or blood-derived material. This is a mechanistic hypothesis, not a demonstrated physical pathway.

### Important genes

#### PRNP

- **Related proteins** (co-abundance neighbors): SMPDL3B (0.98), AXL (0.88), TWSG1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Nuclear membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prion protein (Kanno blood group). The protein encoded by this gene is a membrane glycosylphosphatidylinositol-anchored glycoprotein that tends to aggregate into rod-like structures. The encoded protein contains a highly unstable region of five tandem octapeptide repeats. This gene is found on chromosome 20, approximately 20 kbp upstream of a gene which encodes a biochemically and structurally similar protein to the one encoded by …
- **Diseases (Open Targets)**: Gerstmann-Straussler-Scheinker syndrome (0.826); Creutzfeldt Jacob disease (0.787); Huntington disease-like 1 (0.755); fatal familial insomnia (0.728); inherited Creutzfeldt-Jakob disease (0.719)
- **Europe PMC papers**: 6669
- **Why important**: PRNP is the central network connector, associating with SMPDL3B, AXL, and TWSG1, and it is part of the globally supported immune-regulatory term (GO:BP negative regulation of immune system process; q_global = 0.0138). Its membrane-associated biology, annotations involving inflammatory responses, oxidative stress, ischemia, and copper homeostasis, and extensive disease and literature associations make it a strong candidate for integrating tissue stress with immune regulation. Its choroid-plexus enrichment is particularly relevant to the cerebrospinal-fluid side of the module.
- **Conclusion**: Established evidence supports PRNP as the module’s main network bridge and as a biologically plausible stress and immune-regulatory component. It is reasonable to hypothesize that PRNP helps coordinate the shared tissue-interface signal, but the co-abundance data do not establish that PRNP causally regulates the other module genes.

#### AXL

- **Related proteins** (co-abundance neighbors): PRNP (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: AXL receptor tyrosine kinase. The protein encoded by this gene is a member of the Tyro3-Axl-Mer (TAM) receptor tyrosine kinase subfamily. The encoded protein possesses an extracellular domain which is composed of two immunoglobulin-like motifs at the N-terminal, followed by two fibronectin type-III motifs. It transduces signals from the extracellular matrix into the cytoplasm by binding to the vitamin K-dependent protein growt…
- **Diseases (Open Targets)**: acute myeloid leukemia (0.596); neurodegenerative disease (0.567); Alzheimer disease (0.536); Parkinson disease (0.528); lysosomal storage disease (0.526)
- **Europe PMC papers**: 17119
- **Why important**: AXL is a TAM-family receptor tyrosine kinase with established roles in cytokine regulation, phagocytosis, and signal transduction, and it contributes to (GO:BP negative regulation of immune system process; q_global = 0.0138). It is connected to the central PRNP node and has broad disease associations involving malignancy, neurodegeneration, and inflammatory or immune-related disorders. Its enhancement in stromal and immune-associated cell categories makes it a plausible receptor-level component of a bone–cerebrospinal-fluid interface program.
- **Conclusion**: Established evidence supports AXL as an immune-regulatory receptor and a network-linked module member. A role for AXL in transmitting local extracellular or inflammatory cues is a plausible hypothesis, but this module alone cannot distinguish resident-tissue signaling from altered immune-cell composition.

#### SMPDL3B

- **Related proteins** (co-abundance neighbors): PRNP (0.98), THY1 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sphingomyelin phosphodiesterase acid like 3B. Enables phosphoric diester hydrolase activity. Predicted to be involved in membrane lipid catabolic process; negative regulation of inflammatory response; and negative regulation of toll-like receptor signaling pathway. Located in extracellular exosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Moyamoya disease (0.346); retinal disorder (0.232); neoplasm (0.087); acute myeloid leukemia (0.077); hepatocellular carcinoma (0.077)
- **Europe PMC papers**: 415
- **Why important**: SMPDL3B is a direct member of (GO:BP negative regulation of immune system process; q_global = 0.0138), connects the central PRNP node to THY1, and has annotations for sphingomyelin and lipid catabolism, negative regulation of inflammatory responses, and negative regulation of Toll-like receptor signaling. Its secretion to blood and enrichment in several myeloid-associated categories make it important for interpreting whether the module contains a circulating or blood-related component. Its disease associations provide additional, though not definitive, relevance to vascular, retinal, hematologic, and neoplastic biology.
- **Conclusion**: Established evidence supports SMPDL3B as a lipid-linked anti-inflammatory regulator and as a possible extracellular or blood-facing component. Its secretion means that circulating protein contribution must be considered, while its precise role in the shared bone–cerebrospinal-fluid pattern remains hypothetical.

#### THY1

- **Related proteins** (co-abundance neighbors): SMPDL3B (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Thy-1 cell surface antigen. This gene encodes a cell surface glycoprotein and member of the immunoglobulin superfamily of proteins. The encoded protein is involved in cell adhesion and cell communication in numerous cell types, but particularly in cells of the immune and nervous systems. The encoded protein is widely used as a marker for hematopoietic stem cells. This gene may function as a tumor suppressor in nasopharyngeal…
- **Diseases (Open Targets)**: mathematical ability (0.268); Delayed puberty (0.161); type 2 diabetes mellitus (0.129); diabetes mellitus (0.122); neoplasm (0.119)
- **Europe PMC papers**: 12640
- **Why important**: THY1 is linked to SMPDL3B in the module and is included in (GO:BP negative regulation of immune system process; q_global = 0.0138). As a cell-surface glycoprotein involved in adhesion, cell communication, immune-system regulation, extravasation, and cytoskeletal organization, it provides a strong cellular-interface interpretation. Its enrichment in brain and stromal-related cell categories, together with substantial literature coverage, makes it relevant to tissue architecture and to distinguishing resident interface biology from a purely circulating signal.
- **Conclusion**: Established evidence supports THY1 as an adhesion and cell-contact regulator with relevance to neural and stromal contexts. It may represent the structural or cellular-identity component of the module, but the available data do not prove that THY1 mediates the observed co-abundance relationships.

#### TWSG1

- **Related proteins** (co-abundance neighbors): PRNP (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Centrosome, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: twisted gastrulation BMP signaling modulator 1. Enables transforming growth factor beta binding activity. Involved in several processes, including negative regulation of CD4-positive, alpha-beta T cell proliferation; positive regulation of pathway-restricted SMAD protein phosphorylation; and transforming growth factor beta receptor signaling pathway. Predicted to be located in extracellular region. Predicted to be active in extracellular space.…
- **Diseases (Open Targets)**: placental abruption (0.339); Tietze syndrome (0.305); alcohol drinking (0.304); urolithiasis (0.249); seasonal allergic rhinitis (0.220)
- **Europe PMC papers**: 640
- **Why important**: TWSG1 is connected to PRNP and is included in (GO:BP negative regulation of immune system process; q_global = 0.0138). It binds or modulates TGF-beta-related signaling, regulates BMP and SMAD pathways, and is annotated for negative regulation of T-cell activation and proliferation. Its predicted extracellular biology complements the membrane and cytosolic components of the module and provides a plausible developmental, stromal, and immune-regulatory link. Its disease associations and literature record are more limited than those of PRNP, AXL, or THY1, which increases its value as a potentially underexplored component.
- **Conclusion**: Established evidence supports TWSG1 as an extracellular BMP/TGF-beta pathway modulator with immune-regulatory effects. It is a credible candidate for linking tissue remodeling to immune restraint, but that proposed role in bone and cerebrospinal fluid is presently a hypothesis requiring direct validation.

## Module 2

**Tissue pair**: bone and cerebrospinal_fluid  
**Genes (9)**: ASPH, HSPA5, CADM3, COL12A1, CSPG4, LAMB1, LAMC1, MFGE8, IGF2R

### Function

The most coherent interpretation is an extracellular-matrix, basement-membrane, cell-adhesion, and tissue-interface module, with a possible contribution from protein trafficking and cellular stress handling. LAMC1 and LAMB1 are laminin subunits, COL12A1 is a fibril-associated collagen, CSPG4 is a cell-surface proteoglycan, and CADM3 is a cell-adhesion molecule. MFGE8 adds a secreted apoptotic-cell-clearance function, while IGF2R and HSPA5 support intracellular trafficking and protein-folding interpretations. No GO or KEGG term passed global multiple-testing correction; therefore the functional interpretation is based on the gene annotations, network structure, STRING relationships, hu.MAP evidence, and tissue or cell-type context rather than on globally significant enrichment. The module is biologically coherent but not a formally enriched pathway.

**Cell composition.** The module is strongly compatible with stromal and extracellular-matrix biology. Six genes are annotated as secreted, including the laminin subunits, MFGE8, and COL12A1, while the HPA single-cell annotations repeatedly point to fibroblasts, adipocytes, fibro-adipogenic progenitors, Schwann cells, pericytes, and related structural or vascular populations. This pattern favors extracellular matrix, vascular-interface, and stromal-cell contributions rather than a generic housekeeping program. It is not primarily a blood-cell module: most genes were not detected in immune cells, although immune-cell enhancement is reported for IGF2R, ASPH, and MFGE8. The presence of brain, choroid-plexus, glial, and neural annotations is compatible with a shared tissue-interface or supporting-cell signal between bone and cerebrospinal fluid. Because many constituents are secreted or extracellular, the shared signal could also reflect proteins released into or carried through sampled fluids; the supplied HPA data do not provide matched protein-detection results for either tissue.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a focused, partial extracellular-matrix connection: COL12A1 connects with LAMB1 and LAMC1, and LAMB1-LAMC1 is especially strongly supported. These relationships are consistent with laminin and collagen matrix organization. STRING reports no functional-enrichment result for the module, so it does not supply an additional statistically supported pathway interpretation. hu.MAP independently places LAMB1 and LAMC1 together in three complexes, represented by (hu.MAP huMAP3_01175.1), (hu.MAP huMAP3_08112.1), and (hu.MAP huMAP3_14233.1). (hu.MAP huMAP3_01175.1) is a complete two-member representation within the module, whereas (hu.MAP huMAP3_08112.1) and (hu.MAP huMAP3_14233.1) contain additional proteins outside the module; these complexes therefore support a recurring laminin-centered protein context but do not establish that the entire co-abundance module is one physical complex. The remaining genes have no listed STRING partners or hu.MAP complexes in the fact sheet. Overall, known molecular relationships support the laminin-centered core, while much of the co-abundance structure remains unexplained by curated physical-interaction resources.

**STRING interactions (score >= 0.7)**: 3 of 36 gene pairs: COL12A1–LAMB1 (0.715); COL12A1–LAMC1 (0.721); LAMB1–LAMC1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01175.1 (LAMB1, LAMC1; 2/2); huMAP3_08112.1 (LAMB1, LAMC1; 2/5); huMAP3_14233.1 (LAMB1, LAMC1; 2/14)

### Novelty

The underlying biology is not wholly new: laminin biology, collagen-matrix organization, cell adhesion, apoptotic-cell clearance, lysosomal trafficking, and endoplasmic-reticulum chaperoning are established functions. The laminin relationships involving LAMB1 and LAMC1 are also already represented in STRING and hu.MAP, as shown by (hu.MAP huMAP3_01175.1), (hu.MAP huMAP3_08112.1), and (hu.MAP huMAP3_14233.1). Nevertheless, the particular co-abundance module shared by bone and cerebrospinal fluid may represent a potentially novel tissue-pair observation, because the databases provide only partial interaction coverage and no globally significant GO or KEGG enrichment. It should not be called a new biological pathway or a definitive novel complex. Its novelty remains provisional and would require independent replication, assessment of sample composition and fluid contamination, and comparison with previous bone and cerebrospinal-fluid co-abundance studies. Absence from STRING or hu.MAP alone is not evidence of novelty.

**Hypothesis.** Hypothesis: the module reflects a shared basement-membrane and stromal-interface program in bone-associated and cerebrospinal-fluid-associated compartments. LAMB1 and LAMC1 may provide a laminin scaffold, COL12A1 may link that scaffold to collagen-rich matrix, and CADM3 or CSPG4 may connect matrix organization to neural, glial, vascular, or perivascular cell interfaces. MFGE8 may contribute to remodeling through clearance of apoptotic material, while IGF2R and HSPA5 could support trafficking, lysosomal handling, and secretory or ER proteostasis during matrix production. A further possibility is that the apparent shared module partly reflects extracellular proteins released by stromal or vascular cells rather than synchronized intracellular regulation. This is a mechanistic model, not an established causal conclusion from the co-abundance data.

### Important genes

#### LAMC1

- **Related proteins** (co-abundance neighbors): CADM3 (0.90), MFGE8 (0.88), HSPA5 (0.85); STRING partners: COL12A1 (0.721), LAMB1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_01175.1, huMAP3_08112.1, huMAP3_14233.1
- **Function (MyGene.info)**: laminin subunit gamma 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: Fuchs' endothelial dystrophy (0.487); prostate carcinoma (0.467); colorectal cancer (0.447); eye disorder (0.434); benign colon neoplasm (0.427)
- **Europe PMC papers**: 4227
- **Why important**: LAMC1 is central to the module's extracellular-matrix interpretation. It connects in STRING to LAMB1 and COL12A1, participates in all listed hu.MAP complexes (hu.MAP huMAP3_01175.1), (hu.MAP huMAP3_08112.1), and (hu.MAP huMAP3_14233.1), and is annotated as a secreted extracellular-matrix protein involved in adhesion, migration, tissue development, and signaling. Its fibroblast, fibro-adipogenic progenitor, adipocyte, and pituicyte or FSC annotations also fit a stromal or tissue-interface source. Its disease associations and substantial literature support make it a well-established matrix component.
- **Conclusion**: Established evidence: LAMC1 is a laminin subunit with matrix and adhesion functions and has direct database support for relationships with LAMB1 and COL12A1. Hypothesis: it is a principal structural anchor of the shared module and may help connect bone matrix with cerebrospinal-fluid interface biology.

#### LAMB1

- **Related proteins** (co-abundance neighbors): IGF2R (0.86), HSPA5 (0.84); STRING partners: COL12A1 (0.715), LAMC1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_01175.1, huMAP3_08112.1, huMAP3_14233.1
- **Function (MyGene.info)**: laminin subunit beta 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins are composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respecti…
- **Diseases (Open Targets)**: cobblestone lissencephaly without muscular or ocular involvement (0.800); Fuchs' endothelial dystrophy (0.494); eye disorder (0.434); corneal disorder (0.424); corneal dystrophy (0.423)
- **Europe PMC papers**: 3735
- **Why important**: LAMB1 is important because it forms the strongest listed STRING relationship with LAMC1 and recurs with LAMC1 in every listed hu.MAP complex, including the complete representation in (hu.MAP huMAP3_01175.1). It is a secreted extracellular-matrix laminin subunit with annotations for adhesion, migration, neuronal-glial interaction, and guided cortical migration. Its choroid-plexus epithelial and stromal cell annotations are especially relevant to a cerebrospinal-fluid-associated interpretation. Its developmental and ocular disease associations, together with a substantial literature base, support its importance.
- **Conclusion**: Established evidence: LAMB1 is a laminin component with matrix, adhesion, developmental, and neuronal-glial functions and known molecular context with LAMC1. Hypothesis: LAMB1 may help explain why the module is shared across a skeletal matrix environment and a cerebrospinal-fluid or choroid-plexus interface.

#### COL12A1

- **Related proteins** (co-abundance neighbors): ASPH (0.85); STRING partners: LAMB1 (0.715), LAMC1 (0.721)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type XII alpha 1 chain. This gene encodes the alpha chain of type XII collagen, a member of the FACIT (fibril-associated collagens with interrupted triple helices) collagen family. Type XII collagen is a homotrimer found in association with type I collagen, an association that is thought to modify the interactions between collagen I fibrils and the surrounding matrix. Alternatively spliced transcript variants encoding di…
- **Diseases (Open Targets)**: Bethlem myopathy 2 (0.794); Ullrich congenital muscular dystrophy 2 (0.709); Bethlem myopathy (0.617); Abnormality of the skeletal system (0.533); Ullrich congenital muscular dystrophy (0.501)
- **Europe PMC papers**: 3324
- **Why important**: COL12A1 provides the collagen-side complement to the laminin-centered signal. It is a secreted fibril-associated collagen that modifies interactions between collagen-I fibrils and surrounding matrix, and it is annotated for tissue development and collagen fibril organization. Although its network placement is peripheral, its STRING links to both LAMB1 and LAMC1 directly connect it to the module's matrix core. Its fibro-adipogenic progenitor, adipocyte, and stromal annotations and its associations with muscular and skeletal disorders further support a structural role.
- **Conclusion**: Established evidence: COL12A1 is a matrix collagen associated with tissue development and collagen organization and has known STRING links to both laminin subunits. Hypothesis: it may couple collagen-rich bone matrix architecture to the laminin scaffold represented in the shared module.

#### CADM3

- **Related proteins** (co-abundance neighbors): LAMC1 (0.90), HSPA5 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell adhesion molecule 3. The protein encoded by this gene is a calcium-independent cell-cell adhesion protein that can form homodimers or heterodimers with other nectin proteins. The encoded protein has both homophilic and heterophilic cell-cell adhesion activity. This gene is reported to be a tumor suppressor gene. [provided by RefSeq, Oct 2016].
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease, axonal, type 2FF (0.623); neurodegenerative disease (0.462); asthma (0.396); mathematical ability (0.370); Hypercholesterolemia (0.245)
- **Europe PMC papers**: 631
- **Why important**: CADM3 is the most specifically neural or brain-oriented member of the selected group. It is a calcium-independent cell-adhesion molecule with homophilic and heterophilic adhesion functions, has tissue-enriched brain expression, and is annotated across neuronal, glial, and ependymal cell types. Its network links to LAMC1 and HSPA5 provide a possible bridge between cell adhesion, extracellular matrix, and cellular proteostasis. Its association with axonal Charcot-Marie-Tooth disease and neurodegenerative disease makes it relevant to the cerebrospinal-fluid side of the interpretation, although its literature volume is smaller than that of the laminin genes.
- **Conclusion**: Established evidence: CADM3 mediates cell-cell adhesion and is associated with brain, neuronal, glial, and ependymal contexts. Hypothesis: CADM3 may mark the neural or supporting-cell interface that complements the stromal extracellular-matrix signal.

#### HSPA5

- **Related proteins** (co-abundance neighbors): IGF2R (0.86), CSPG4 (0.86), LAMC1 (0.85), LAMB1 (0.84), CADM3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is the most connected node in the supplied co-abundance graph and therefore may organize the non-matrix side of the module. It is an ER HSP70 chaperone and master regulator of ER homeostasis, with annotations for unfolded-protein response and protein targeting to membranes. It is linked in the module to IGF2R, CSPG4, LAMC1, LAMB1, and CADM3, despite having no listed STRING partners or hu.MAP complex. Its very large literature base and associations with neurodegenerative disease and other disease contexts make it an important interpretive control as well as a possible biological component.
- **Conclusion**: Established evidence: HSPA5 is an intracellular ER chaperone involved in proteostasis and stress responses and occupies a prominent position in the co-abundance network. Hypothesis: it may reflect secretory or ER stress accompanying production of extracellular matrix proteins, or it may be a context-dependent bridge rather than a specific component of the matrix mechanism.

## Module 3

**Tissue pair**: bone and cerebrospinal_fluid  
**Genes (7)**: BCAM, GLB1, GUSB, CADM4, ECE1, L1CAM, TFRC

### Function

This is a mixed lysosomal, cell-surface adhesion, endocytic, and neurovascular-associated module rather than a formally established pathway module. The most coherent functional signals come from ECE1, GLB1, and GUSB, which connect proteolytic or carbohydrate-processing biology with vesicular and lysosomal functions. TFRC adds receptor-mediated endocytosis and iron uptake, while CADM4, L1CAM, and BCAM add cell adhesion, membrane, neural, vascular, or extracellular-matrix interfaces. No GO/KEGG term passed global correction, so these functional themes are annotations of individual genes and network context rather than globally significant enrichment. The network is connected but heterogeneous: ECE1 and GLB1 occupy the strongest central positions, with GUSB also linking the two lysosomal hydrolases, whereas the adhesion-associated genes form peripheral connections.

**Cell composition.** The module is not predominantly composed of secreted plasma proteins. HPA indicates a mixed cellular and subcellular composition, including intracellular or vesicular proteins, plasma-membrane proteins, and a gene reported as secreted to blood. Several genes have low tissue specificity, while others are enhanced in brain, blood vessel, kidney, or intestine. Cell-type annotations include neural and glial populations, vascular or epithelial populations, and selected blood-cell populations. ECE1 is associated with neutrophils, TFRC with monocytes and macrophages, and CADM4 with plasmacytoid dendritic cells, but L1CAM and BCAM are not detected in immune cells and GUSB is associated with tissue macrophage populations. Thus, blood or shared immune-cell content could contribute to part of the co-abundance signal, but the HPA evidence does not support interpreting the entire module as a blood-cell module. The brain-enhanced adhesion genes and vesicular or lysosomal proteins are also compatible with shared neural, vascular, or tissue-interface biology. HPA provides no matched protein-detection result for either named fluid or tissue, so direct protein-level confirmation in bone and cerebrospinal fluid is unavailable.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no high-confidence pairwise interactions among the module genes and no supplementary STRING functional enrichment. This argues against treating the co-abundance edges as established physical interactions or as a canonical STRING-defined pathway. hu.MAP provides a more limited form of prior support: GUSB and ECE1 occur together in each of the reported complexes (hu.MAP huMAP3_08802.1), (hu.MAP huMAP3_06775.1), and (hu.MAP huMAP3_09327.1). However, in every case they represent only a small subset of a much larger complex membership, so the hu.MAP evidence supports a shared lysosomal, glycoprotein-processing, or membrane-trafficking context rather than a compact module-specific complex. GLB1, TFRC, CADM4, L1CAM, and BCAM have no reported hu.MAP membership in the supplied evidence. Overall, the network appears to capture coordinated abundance across related cellular compartments or tissue interfaces more readily than a known physical protein complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08802.1 (GUSB, ECE1; 2/33); huMAP3_06775.1 (GUSB, ECE1; 2/60); huMAP3_09327.1 (GUSB, ECE1; 2/93)

### Novelty

This may be a novel tissue-pair co-abundance pattern, but the evidence does not establish a wholly new biological mechanism. The absence of STRING interactions and the lack of a compact hu.MAP complex indicate that this particular combination is not already represented as a strongly supported interaction module in the supplied resources. That absence alone does not prove novelty, because co-abundance relationships can reflect shared cell composition, trafficking, compartmental abundance, or tissue sampling rather than direct binding. The established biology of the individual genes, especially lysosomal degradation, endocytosis, adhesion, neural development, and vascular interfaces, is not novel. The potentially new observation is their coordinated abundance across bone and cerebrospinal fluid, which requires validation in independent cohorts, adjustment for blood contamination and cell composition, and targeted protein measurements.

**Hypothesis.** Hypothesis: this module reflects coordinated abundance of vesicular and lysosomal processing machinery together with neural, vascular, and cell-adhesion interfaces that are shared between bone-associated tissue and cerebrospinal-fluid-associated material. ECE1 and the glycosidases GLB1 and GUSB may represent the intracellular processing core, while TFRC reflects endosomal uptake and iron handling and CADM4, L1CAM, and BCAM reflect membrane or extracellular-contact states. A contribution from blood-derived or immune-associated material is plausible because of the HPA blood-cell annotations, but it should be treated as an alternative or contributing explanation rather than the primary conclusion. The hypothesis predicts that the module will track lysosomal or endosomal activity and tissue-interface cell composition more strongly than direct protein-protein binding.

### Important genes

#### ECE1

- **Related proteins** (co-abundance neighbors): GLB1 (0.91), GUSB (0.87), BCAM (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08802.1, huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: endothelin converting enzyme 1. The protein encoded by this gene is involved in proteolytic processing of endothelin precursors to biologically active peptides. Mutations in this gene are associated with Hirschsprung disease, cardiac defects and autonomic dysfunction. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: Hirschsprung disease (0.591); neurodegenerative disease (0.362); Alzheimer disease (0.332); lysosomal storage disease (0.325); Parkinson disease (0.325)
- **Europe PMC papers**: 5314
- **Why important**: ECE1 has the strongest network position in the module and connects to GLB1, GUSB, and BCAM. Its established functions include proteolytic processing of endothelin precursors, receptor recycling, systemic arterial blood-pressure regulation, signal transduction, and axon guidance. It is also present with GUSB in all reported hu.MAP complexes (hu.MAP huMAP3_08802.1), (hu.MAP huMAP3_06775.1), and (hu.MAP huMAP3_09327.1). Its disease associations include Hirschsprung disease, cardiac defects, autonomic dysfunction, and reported links to neurodegenerative and lysosomal-storage disease. The substantial literature volume makes it a well-characterized anchor for interpreting the module.
- **Conclusion**: Established evidence supports ECE1 as a central proteolytic and signaling-related gene with neural, vascular, and disease relevance. The module data support its role as a network anchor and as part of a broader processing or trafficking context. It is a hypothesis, not an established fact, that ECE1 activity drives the shared bone–cerebrospinal-fluid signal.

#### GLB1

- **Related proteins** (co-abundance neighbors): ECE1 (0.91), CADM4 (0.86), GUSB (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galactosidase beta 1. This gene encodes a member of the glycosyl hydrolase 35 family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature lysosomal enzyme. This enzyme catalyzes the hydrolysis of a terminal beta-linked galactose residue from ganglioside substrates and other glycoconjugates. Mutat…
- **Diseases (Open Targets)**: mucopolysaccharidosis type 4B (0.849); GM1 gangliosidosis type 1 (0.847); GM1 gangliosidosis type 3 (0.842); GM1 gangliosidosis type 2 (0.842); GM1 gangliosidosis (0.771)
- **Europe PMC papers**: 2663
- **Why important**: GLB1 is nearly as central as ECE1 and connects to ECE1, CADM4, and GUSB. It encodes a lysosomal glycosidase involved in degradation of gangliosides and other glycoconjugates, including galactose-containing substrates and keratan-sulfate proteoglycans. Its disease associations include GM1 gangliosidosis and Morquio B syndrome. Its vesicular localization and carbohydrate-catabolic annotation provide a strong mechanistic link to GUSB and to the shared hu.MAP context, despite the absence of globally significant GO/KEGG enrichment.
- **Conclusion**: Established evidence supports GLB1 as a lysosomal glycoconjugate-degradation enzyme and a central member of the observed co-abundance structure. Its coordinated abundance with GUSB is biologically plausible, but the data do not demonstrate that GLB1 and GUSB directly interact or that lysosomal disease biology explains the tissue-pair pattern.

#### GUSB

- **Related proteins** (co-abundance neighbors): ECE1 (0.87), GLB1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08802.1, huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: glucuronidase beta. This gene encodes a hydrolase that degrades glycosaminoglycans, including heparan sulfate, dermatan sulfate, and chondroitin-4,6-sulfate. The enzyme forms a homotetramer that is localized to the lysosome. Mutations in this gene result in mucopolysaccharidosis type VII. Alternative splicing results in multiple transcript variants. There are many pseudogenes of this locus in the human genome.[provid…
- **Diseases (Open Targets)**: mucopolysaccharidosis type 7 (0.878); mucopolysaccharidosis type 6 (0.439); hereditary disease (0.415); Non-immune hydrops fetalis (0.391); mucopolysaccharidosis (0.374)
- **Europe PMC papers**: 7068
- **Why important**: GUSB connects to ECE1 and GLB1 and is present with ECE1 in the hu.MAP complexes (hu.MAP huMAP3_08802.1), (hu.MAP huMAP3_06775.1), and (hu.MAP huMAP3_09327.1). It encodes a lysosomal hydrolase that degrades several glycosaminoglycans, including heparan sulfate, dermatan sulfate, chondroitin sulfate, and hyaluronan-related substrates. Its established disease association with mucopolysaccharidosis type seven gives it strong pathological relevance. Its vesicular localization and macrophage-associated HPA annotations also make it informative for distinguishing tissue lysosomal biology from contributions of phagocytic or blood-associated cells.
- **Conclusion**: Established evidence supports GUSB as a lysosomal glycosaminoglycan-degradation component and a strong functional partner of GLB1 at the annotation level. The hu.MAP evidence supports shared complex context with ECE1, but not a dedicated module-specific complex. A contribution from macrophage or other vesicle-rich cell populations remains a hypothesis.

#### TFRC

- **Related proteins** (co-abundance neighbors): L1CAM (0.94), CADM4 (0.92); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes, Lysosomes; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transferrin receptor. This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: TFRC-related combined immunodeficiency (0.623); type 2 diabetes mellitus (0.518); mucopolysaccharidosis type 2 (0.490); diabetes mellitus (0.471); diabetic retinopathy (0.343)
- **Europe PMC papers**: 14164
- **Why important**: TFRC is connected to L1CAM and CADM4 and is the module gene most directly annotated for receptor-mediated endocytosis, iron uptake, intracellular iron homeostasis, erythropoiesis, and neurologic development. HPA places it in endosomes and lysosomes and reports secretion to blood, with enhancement in erythrocyte progenitors, macrophages, monocytes, and syncytiotrophoblasts. Its disease associations include TFRC-related combined immunodeficiency and metabolic or vascular disorders. Its extensive literature makes it an important indicator of endocytic activity and a possible marker of cellular-composition effects.
- **Conclusion**: Established evidence supports TFRC as an endocytic iron-uptake receptor with relevance to blood, immune, and neural biology. In this module it may connect the lysosomal-processing theme to membrane trafficking. It is also a plausible source of blood-related confounding, but the module does not establish whether TFRC reflects contamination, a shared cell population, or genuine tissue biology.

#### L1CAM

- **Related proteins** (co-abundance neighbors): TFRC (0.94); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: L1 cell adhesion molecule. The protein encoded by this gene is an axonal glycoprotein belonging to the immunoglobulin supergene family. The ectodomain, consisting of several immunoglobulin-like domains and fibronectin-like repeats (type III), is linked via a single transmembrane sequence to a conserved cytoplasmic domain. This cell adhesion molecule plays an important role in nervous system development, including neuronal m…
- **Diseases (Open Targets)**: X-linked hydrocephalus with stenosis of the aqueduct of Sylvius (0.855); MASA syndrome (0.833); X-linked complicated corpus callosum dysgenesis (0.762); L1 syndrome (0.725); Spastic paraplegia (0.571)
- **Europe PMC papers**: 6523
- **Why important**: L1CAM is connected to TFRC and has tissue-enhanced expression in brain and intestine, with cell-type enhancement in neurons and other neural populations. It is an axonal immunoglobulin-superfamily adhesion molecule involved in neuronal migration, differentiation, nervous-system development, and axon guidance. Its disease associations include L1 syndrome, hydrocephalus with aqueductal stenosis, corpus-callosum dysgenesis, MASA syndrome, and spastic paraplegia. The large literature base and strong neural specificity make it the clearest indicator that the module may include a neural or cerebrospinal-fluid interface component.
- **Conclusion**: Established evidence supports L1CAM as a neural cell-adhesion and axon-development gene. Its position at the edge of the module suggests a specialized interface rather than a central lysosomal role. A neural contribution to the bone–cerebrospinal-fluid co-abundance pattern is plausible, but the sparse network connection does not prove that L1CAM mechanistically organizes the module.

#### CADM4

- **Related proteins** (co-abundance neighbors): TFRC (0.92), GLB1 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell adhesion molecule 4. Enables vascular endothelial growth factor receptor 2 binding activity. Involved in several processes, including negative regulation of protein phosphorylation; regulation of Rac protein signal transduction; and regulation of wound healing. Located in cell leading edge and cell-cell contact zone. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: myocardial infarction (0.266); coronary artery disorder (0.259); angina pectoris (0.216); abdominal aortic aneurysm (0.144); Decreased total leukocyte count (0.126)
- **Europe PMC papers**: 386
- **Why important**: CADM4 links TFRC and GLB1 and is the most informative bridge between the lysosomal or endocytic genes and the adhesion-associated genes. HPA reports brain tissue enhancement, plasma-membrane localization, and enhancement in oligodendrocytes, oligodendrocyte progenitors, Schwann cells, and other cell types. Its annotated functions include homophilic cell adhesion, regulation of protein phosphorylation, central nervous-system myelination, and modulation of vascular endothelial growth-factor receptor signaling. Although its literature volume is smaller than that of the other selected genes, its network bridging position and neural or glial annotations make it important.
- **Conclusion**: Established evidence supports CADM4 as a membrane adhesion and signaling regulator with neural and myelination relevance. Its module position supports a possible interface between cell adhesion and intracellular processing. The idea that CADM4 helps couple neural or glial cell state to lysosomal abundance is a hypothesis rather than a demonstrated mechanism.

## Module 4

**Tissue pair**: bone and cerebrospinal_fluid  
**Genes (12)**: ALCAM, CD44, COL6A1, CXADR, FAM3C, NCAM1, NEGR1, NTM, PLXNB2, SOD2, TXN, TIMP1

### Function

The module is most consistent with a cell-adhesion and tissue-interface program, combining neural or glial adhesion biology with extracellular-matrix interaction, migration, redox protection, and protease regulation. NCAM1 and NTM support neuronal, glial, neurite-outgrowth, and synapse-related biology; ALCAM, CD44, CXADR, PLXNB2, and COL6A1 support cell-cell or cell-matrix adhesion; TIMP1 supports extracellular-matrix protease inhibition and cytokine-responsive tissue remodeling; and SOD2 with TXN supports oxidative-stress control. These are functional annotations and network patterns rather than globally significant enrichment results. No GO or KEGG term passed global correction. The STRING enrichment result was also empty, so the interpretation is based on gene-level annotations, topology, curated interactions, and complexes rather than significant pathway enrichment.

**Cell composition.** This is not a clean tissue-specific neuronal module. Most genes are secreted or extracellularly associated according to the HPA summary, including several secreted-to-blood or extracellular-matrix proteins. HPA also shows substantial cell-type heterogeneity: brain and neuronal or glial enrichment occurs for several genes, while monocytes, dendritic cells, B cells, NK cells, and neutrophils account for other annotations. Fibroblast and stromal annotations are also present. Thus, the shared bone and cerebrospinal-fluid signal could reflect a conserved adhesion or matrix interface, but it could also reflect blood, immune-cell, stromal, or shared extracellular protein content in the samples. The HPA tissue and cell-type evidence does not establish that the module originates from one cell population, and the absence of matching HPA protein detection data for these two sample types prevents direct protein-level confirmation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known STRING relationships include CD44 with COL6A1, TIMP1, ALCAM, and NCAM1, plus SOD2 with TXN. These interactions support a partial extracellular-adhesion and matrix-remodeling neighborhood and a separate redox neighborhood, with NCAM1 and TIMP1 connecting parts of the network through co-abundance relationships. Other module edges are not represented by high-confidence STRING links, so the full co-abundance structure should not be interpreted as an established physical interaction network. hu.MAP provides three complexes containing NCAM1 and NTM together (hu.MAP huMAP3_10860.1), (hu.MAP huMAP3_12359.1), and (hu.MAP huMAP3_11626.1). The larger complex (hu.MAP huMAP3_11626.1) contains many neuronal and synaptic proteins, whereas (hu.MAP huMAP3_10860.1) and (hu.MAP huMAP3_12359.1) include proteins associated with cell-surface or membrane organization. These complexes support a neuronal or membrane-adhesion component, but because only a minority of each complex is represented, they do not prove that the entire module is one physical complex.

**STRING interactions (score >= 0.7)**: 5 of 66 gene pairs: ALCAM–CD44 (0.859); CD44–COL6A1 (0.926); CD44–NCAM1 (0.712); CD44–TIMP1 (0.922); SOD2–TXN (0.728)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10860.1 (NCAM1, NTM; 2/5); huMAP3_12359.1 (NCAM1, NTM; 2/9); huMAP3_11626.1 (NCAM1, NTM; 2/42)

### Novelty

The module is a potentially interesting cross-tissue co-abundance observation, but it cannot be called a wholly new biological pathway. Several component functions and relationships are already established: NCAM1 and NTM have neural adhesion roles, CD44 and COL6A1 are linked in STRING, SOD2 and TXN form a known redox relationship, and NCAM1 with NTM recur in hu.MAP complexes. The potentially novel aspect is the coordinated occurrence of this mixed neural-adhesion, matrix, immune-associated, and redox signature across bone and cerebrospinal fluid. That claim remains provisional because the module has no globally significant GO or KEGG term, no STRING enrichment, substantial secreted-protein content, and plausible blood or shared-cell-type explanations. Lack of a STRING or hu.MAP relationship for some pairs is evidence of limited prior database support, not proof of biological novelty.

**Hypothesis.** Hypothesis: the module represents a shared extracellular and cell-surface interface in which adhesion molecules organize contacts among neural, stromal, and immune-associated cells, while COL6A1 and TIMP1 shape the surrounding matrix and protease environment and SOD2 with TXN buffers oxidative stress. In bone, this could relate to matrix-associated stromal or osteogenic interfaces; in cerebrospinal fluid, it could reflect neural or glial interfaces and extracellular material. A shared contribution from circulating or secreted proteins is an alternative explanation. This hypothesis should be tested with cell-resolved expression, matched protein measurements, and perturbation of adhesion, matrix-remodeling, and redox components rather than inferred from co-abundance alone.

Web sources: https://www.ncbi.nlm.nih.gov/gene?cmd=search&term=4684; https://www.uniprot.org/uniprotkb/P13591/entry; https://en.wikipedia.org/wiki/Neural_cell_adhesion_molecule

### Important genes

#### NCAM1

- **Related proteins** (co-abundance neighbors): ALCAM (0.96), PLXNB2 (0.84), TIMP1 (0.82), TXN (0.82), SOD2 (0.81), NTM (0.81); STRING partners: CD44 (0.712)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10860.1, huMAP3_12359.1, huMAP3_11626.1
- **Function (MyGene.info)**: neural cell adhesion molecule 1. This gene encodes a cell adhesion protein which is a member of the immunoglobulin superfamily. The encoded protein is involved in cell-to-cell interactions as well as cell-matrix interactions during development and differentiation. The encoded protein plays a role in the development of the nervous system by regulating neurogenesis, neurite outgrowth, and cell migration. This protein is also involv…
- **Diseases (Open Targets)**: major depressive disorder (0.532); smoking initiation (0.501); gastroesophageal reflux disease (0.498); schizophrenia (0.463); irritable bowel syndrome (0.462)
- **Europe PMC papers**: 6731
- **Why important**: NCAM1 is the principal network hub, with the broadest connectivity and strongest aggregate edge support in the module. It is brain- and glia-associated in HPA, is present in all three reported hu.MAP complexes, and has an established role in cell-cell and cell-matrix interactions, neurogenesis, neurite outgrowth, migration, and semaphorin-plexin signaling. Its extensive literature and disease associations make it the best anchor for the neural-adhesion interpretation, while its NK-cell annotation also keeps an immune-cell explanation plausible.
- **Conclusion**: Established evidence supports NCAM1 as a central adhesion-related and neural-associated component of the module. It is reasonable to hypothesize that NCAM1 helps connect the neural and extracellular-interface signals, but the co-abundance data do not establish that NCAM1 drives the module or that the signal is neuronal in origin.

#### NTM

- **Related proteins** (co-abundance neighbors): CD44 (0.88), SOD2 (0.84), TXN (0.83), NCAM1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10860.1, huMAP3_12359.1, huMAP3_11626.1
- **Function (MyGene.info)**: neurotrimin. This gene encodes a member of the IgLON (LAMP, OBCAM, Ntm) family of immunoglobulin (Ig) domain-containing glycosylphosphatidylinositol (GPI)-anchored cell adhesion molecules. The encoded protein may promote neurite outgrowth and adhesion via a homophilic mechanism. This gene is closely linked to a related family member, opioid binding protein/cell adhesion molecule-like (OPCML), on chromosome 11.…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.453); smoking initiation (0.429); refractive error (0.429); health study participation (0.404); hyperopia (0.383)
- **Europe PMC papers**: 7389
- **Why important**: NTM is among the more connected genes and is paired with NCAM1 in all three hu.MAP complexes (hu.MAP huMAP3_10860.1), (hu.MAP huMAP3_12359.1), and (hu.MAP huMAP3_11626.1). HPA places it in brain and retina and in neuronal and astrocytic cell types. Its established functions include GPI-anchored immunoglobulin-family adhesion, neurite outgrowth, neuron recognition, and synapse assembly. Its STRING absence despite strong module relationships makes it especially informative for distinguishing co-abundance from currently curated protein interaction evidence.
- **Conclusion**: Established evidence supports NTM as a neural cell-adhesion and membrane-associated component that reinforces the NCAM1-centered interpretation. It is a plausible contributor to a shared neural-interface hypothesis, but its presence does not demonstrate a direct physical interaction with every co-abundant gene.

#### TIMP1

- **Related proteins** (co-abundance neighbors): PLXNB2 (0.89), SOD2 (0.84), NCAM1 (0.82), ALCAM (0.82); STRING partners: CD44 (0.922)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TIMP metallopeptidase inhibitor 1. This gene belongs to the TIMP gene family. The proteins encoded by this gene family are natural inhibitors of the matrix metalloproteinases (MMPs), a group of peptidases involved in degradation of the extracellular matrix. In addition to its inhibitory role against most of the known MMPs, the encoded protein is able to promote cell proliferation in a wide range of cell types, and may also have an …
- **Diseases (Open Targets)**: neoplasm (0.120); Sepsis (0.119); glioblastoma (0.119); colorectal carcinoma (0.119); neurodegenerative disease (0.117)
- **Europe PMC papers**: 25183
- **Why important**: TIMP1 is a highly connected module member and has a high-confidence STRING relationship with CD44, as well as module relationships with NCAM1, ALCAM, PLXNB2, and SOD2. It is secreted to blood, is enhanced in vascular tissue, and is associated with fibroblast and stromal cell types. Its established functions include inhibition of matrix metalloproteinases, regulation of extracellular-matrix degradation, cytokine response, cell proliferation, and anti-apoptotic activity. It also has extensive literature and broad disease relevance.
- **Conclusion**: Established evidence supports TIMP1 as a matrix-remodeling and extracellular signaling component that could connect adhesion to tissue repair or inflammatory context. A role in coordinating the shared bone and cerebrospinal-fluid signal is a hypothesis, especially because secreted-to-blood localization makes sample-content effects possible.

#### SOD2

- **Related proteins** (co-abundance neighbors): TIMP1 (0.84), NTM (0.84), FAM3C (0.84), NCAM1 (0.81); STRING partners: TXN (0.728)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: superoxide dismutase 2. This gene is a member of the iron/manganese superoxide dismutase family. It encodes a mitochondrial protein that forms a homotetramer and binds one manganese ion per subunit. This protein binds to the superoxide byproducts of oxidative phosphorylation and converts them to hydrogen peroxide and diatomic oxygen. Mutations in this gene have been associated with idiopathic cardiomyopathy (IDC), premat…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); diabetic retinopathy (0.379); malunion fracture (0.295); coronary artery disorder (0.267); prostate carcinoma (0.227)
- **Europe PMC papers**: 28293
- **Why important**: SOD2 occupies a central position within the redox-associated portion of the module and connects to TIMP1, NTM, FAM3C, and NCAM1. It is mitochondrial, enhanced in bone marrow, and associated with monocytes and neutrophils in HPA. Its established function is conversion of mitochondrial superoxide into hydrogen peroxide and oxygen, with links to hypoxia responses, mitochondrial injury, aging, motor-neuron disease, and cancer. The known STRING relationship with TXN provides independent support for a redox component.
- **Conclusion**: Established evidence supports SOD2 as an oxidative-stress regulator and a plausible indicator of cellular stress or immune-associated material in the samples. It may help explain why the adhesion-associated genes co-vary with the module, but a causal redox role in the cross-tissue program remains unproven.

#### CD44

- **Related proteins** (co-abundance neighbors): NTM (0.88); STRING partners: ALCAM (0.859), COL6A1 (0.926), NCAM1 (0.712), TIMP1 (0.922)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD44 molecule (IN blood group). The protein encoded by this gene is a cell-surface glycoprotein involved in cell-cell interactions, cell adhesion and migration. It is a receptor for hyaluronic acid (HA) and can also interact with other ligands, such as osteopontin, collagens, and matrix metalloproteinases (MMPs). This protein participates in a wide variety of cellular functions including lymphocyte activation, recirculation and …
- **Diseases (Open Targets)**: nephrolithiasis, calcium oxalate (0.523); calcium oxalate urolithiasis (0.521); uterine corpus leiomyoma (0.480); systemic lupus erythematosus (0.467); autoimmune disease (0.330)
- **Europe PMC papers**: 102058
- **Why important**: CD44 has a comparatively limited module degree but unusually broad external support, including high-confidence STRING relationships with ALCAM, COL6A1, NCAM1, and TIMP1. It is a plasma-membrane adhesion receptor for hyaluronan and can interact with collagens and matrix metalloproteinases. HPA associates it with monocytes, neutrophils, mast cells, dendritic cells, and basal keratinocytes, while its known functions include cell adhesion, migration, inflammatory response, lymphocyte trafficking, and hematopoiesis. Its very large literature base makes it a strong interpretive bridge between matrix, immune, and adhesion biology.
- **Conclusion**: Established evidence supports CD44 as a matrix-sensing and immune- or stromal-interface marker that links several known interaction relationships in the module. It is a strong candidate for a shared extracellular-context explanation, but its broad biology makes it unsuitable as proof of a single specific cell source.

## Module 5

**Tissue pair**: bone and cerebrospinal_fluid  
**Genes (9)**: CLU, GNS, HEXA, HYOU1, LGALS3BP, LGMN, LRP1, MAN2B1, PLOD2

### Function

No GO/KEGG term passed global correction, and there are no supplementary STRING functional-enrichment terms. The biological interpretation therefore rests on the gene annotations, network organization, and interaction evidence rather than on formal pathway enrichment. The module is most consistent with a lysosome–endosome and secretory-system program involving glycan and proteoglycan turnover, protein processing, stress-adaptive folding, extracellular-protein clearance, and connective-tissue collagen maturation. GNS, HEXA, and MAN2B1 support lysosomal degradation of glycosaminoglycans, gangliosides, and glycoproteins. HYOU1 supports endoplasmic-reticulum protein folding, secretion, and responses to hypoxic or ER stress. PLOD2 supports collagen modification and fibril organization, while CLU and LRP1 support extracellular chaperoning, lipid handling, receptor-mediated uptake, and clearance. The graph contains a central connective component around PLOD2 and HYOU1, with lysosomal and clearance-related genes connected to that component. This pattern suggests coordinated cellular processing and clearance biology, but it does not by itself establish a bone- or cerebrospinal-fluid-specific pathway.

**Cell composition.** The HPA summary labels all module genes as secreted genes, but the gene-level secretome annotations distinguish mainly intracellular or membrane-associated proteins from proteins specifically secreted to blood. CLU and LGALS3BP are annotated as secreted to blood, whereas the other genes are predominantly intracellular, vesicular, membrane, or otherwise non-blood-secreted in the supplied annotations. Most genes have low tissue specificity, so the shared signal is not strongly tissue restricted. The single-cell evidence is dominated by immune and myeloid-associated populations, including Kupffer cells, monocytes, macrophages, dendritic-cell populations, neutrophils, and microglia, with additional representation in hepatocytes and other cell types. Several genes show immune-cell enrichment or group enrichment, especially LRP1, MAN2B1, GNS, LGMN, and CLU. Consequently, the conserved bone–cerebrospinal-fluid module could reflect shared myeloid or phagocytic cell biology, circulating material, or sample-associated blood and immune contributions rather than a mechanism unique to either tissue. HPA provides no matching protein-detection result for either bone or cerebrospinal fluid, so tissue-level protein localization cannot be confirmed from this evidence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a small set of high-confidence pairwise relationships within the module: GNS–HEXA is the strongest reported interaction, and CLU–LRP1 is also supported. These relationships independently reinforce lysosomal glycan catabolism and extracellular-protein or lipoprotein clearance, respectively. There is no STRING functional-enrichment result, so the interaction evidence should be interpreted as focused support for particular edges rather than proof of a globally coherent STRING pathway. hu.MAP identifies LGMN and HYOU1 together in complexes C1 and C2. In both cases, the complexes contain many proteins outside this module, so the hu.MAP evidence supports known participation of these two proteins in broader cellular assemblies but does not demonstrate that the entire module is a single physical complex. The remaining module relationships are not represented by the supplied high-confidence STRING or hu.MAP evidence and may reflect co-abundance, shared cell composition, indirect regulation, or context-dependent biology.

**STRING interactions (score >= 0.7)**: 2 of 36 gene pairs: CLU–LRP1 (0.715); GNS–HEXA (0.936)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (LGMN, HYOU1; 2/60); huMAP3_09327.1 (LGMN, HYOU1; 2/93)

### Novelty

This module should not be called an entirely new molecular complex or a wholly novel pathway. The GNS–HEXA and CLU–LRP1 relationships are already supported by STRING, and the LGMN–HYOU1 co-membership in hu.MAP complexes C1 and C2 is established. The individual functions and disease associations of the genes are also well represented in the literature, particularly for CLU, HEXA, LRP1, GNS, and PLOD2. What may be novel is the observation that these lysosomal, secretory-stress, clearance, and collagen-processing genes form a conserved co-abundance pattern across bone and cerebrospinal fluid in this dataset. However, the fact sheet supplies no comparison with earlier tissue co-abundance studies, independent cohorts, or matched-cell analyses. Therefore the appropriate conclusion is a potentially novel cross-tissue association built from partly known biology, requiring replication and cell-composition control before being described as a new biological mechanism.

**Hypothesis.** Hypothesis: the shared module reflects a myeloid- and secretory-system-mediated tissue maintenance program present in both bone-associated and cerebrospinal-fluid-associated samples. In this model, lysosomal enzymes such as GNS, HEXA, and MAN2B1 process extracellular or endosomal glycoconjugates; LGMN contributes to lysosomal proteolysis and antigen-processing biology; HYOU1 supports folding and trafficking of proteins under secretory or hypoxic stress; CLU and LRP1 mediate chaperoning, uptake, lipid handling, and clearance; and PLOD2 links the program to collagen maturation and extracellular-matrix organization. A shared population of macrophage-like, monocyte-like, microglial, or other phagocytic cells could produce much of the observed co-abundance signal. This is a hypothesis rather than an established tissue-specific mechanism, because global GO/KEGG enrichment is absent, HPA lacks direct protein-detection evidence for the two tissues, and the module contains both intracellular enzymes and blood-secreted proteins.

### Important genes

#### PLOD2

- **Related proteins** (co-abundance neighbors): HYOU1 (0.99), HEXA (0.96), CLU (0.87), LRP1 (0.87), GNS (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Not detected in immune cells; location Nucleoli, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: procollagen-lysine,2-oxoglutarate 5-dioxygenase 2. The protein encoded by this gene is a membrane-bound homodimeric enzyme that is localized to the cisternae of the rough endoplasmic reticulum. The enzyme (cofactors iron and ascorbate) catalyzes the hydroxylation of lysyl residues in collagen-like peptides. The resultant hydroxylysyl groups are attachment sites for carbohydrates in collagen and thus are critical for the stability of intermolecular…
- **Diseases (Open Targets)**: Bruck syndrome (0.779); osteogenesis imperfecta (0.572); osteoarthritis (0.552); osteoarthritis, hip (0.531); osteoarthritis, knee (0.472)
- **Europe PMC papers**: 3025
- **Why important**: PLOD2 is the most connected gene in the supplied module graph and links HYOU1, HEXA, CLU, LRP1, and GNS. Its established function is collagen-lysine hydroxylation in the endoplasmic reticulum, generating hydroxylysine residues important for collagen crosslinking and fibril stability. Its annotations include collagen biosynthesis, collagen fibril organization, and hypoxia response, and its disease associations include Bruck syndrome, osteogenesis imperfecta, and osteoarthritis. Its substantial literature volume makes it a strong anchor for interpreting the module in relation to bone and extracellular matrix.
- **Conclusion**: Established: PLOD2 provides a biologically credible extracellular-matrix and bone-relevant anchor and occupies a central network position. Hypothesis: its co-abundance with lysosomal and clearance genes may reflect matrix turnover or stress-adaptive remodeling, but the module does not establish that PLOD2 activity drives the shared cross-tissue signal.

#### HYOU1

- **Related proteins** (co-abundance neighbors): PLOD2 (0.99), HEXA (0.95), GNS (0.86), LGALS3BP (0.82), LRP1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 is among the most connected genes and links the collagen-associated, lysosomal, and clearance-related parts of the graph. It is an ER heat-shock protein associated with protein folding, secretion, ER-to-Golgi trafficking, hypoxia, ischemia, ER stress, and protection from apoptosis. It is also the only gene represented with LGMN in both hu.MAP complexes C1 and C2, providing direct complex-level support for its participation in broader cellular assemblies. Its disease associations include neurodegenerative disease and disorders involving abnormal immune or stress biology.
- **Conclusion**: Established: HYOU1 is a plausible coordinator of secretory and stress-related biology and has independent hu.MAP support with LGMN. Hypothesis: it may connect stress responses to lysosomal processing in the shared samples, although the supplied evidence does not prove a direct physical interaction with the other module members.

#### CLU

- **Related proteins** (co-abundance neighbors): PLOD2 (0.87), GNS (0.87), MAN2B1 (0.84), LGMN (0.82); STRING partners: LRP1 (0.715)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: clusterin. The protein encoded by this gene is a secreted chaperone that can under some stress conditions also be found in the cell cytosol. It has been suggested to be involved in several basic biological events such as cell death, tumor progression, and neurodegenerative disorders. Alternate splicing results in both coding and non-coding variants.[provided by RefSeq, May 2011].
- **Diseases (Open Targets)**: Alzheimer disease (0.583); dementia (0.525); refractive error (0.444); late-onset Alzheimers disease (0.406); prostate cancer (0.376)
- **Europe PMC papers**: 10677
- **Why important**: CLU is a central connector linking PLOD2, GNS, MAN2B1, and LGMN and is one of the two module genes annotated as secreted to blood. It is a secreted chaperone associated with protein folding, immune-complex clearance, inhibition of membrane-attack-complex activation, microglial activation, and neurodegenerative disorders. Its CLU–LRP1 relationship is supported by STRING, and it has extensive literature coverage and disease associations with Alzheimer disease and dementia. Its liver enhancement and immune-cell annotations also make it relevant to possible circulating or myeloid contributions.
- **Conclusion**: Established: CLU supports extracellular chaperoning and clearance and has a known relationship with LRP1. Hypothesis: CLU could act as a circulating or locally released bridge between immune-cell activity and tissue-protein clearance, but the module cannot distinguish secretion-driven biology from shared sample composition.

#### HEXA

- **Related proteins** (co-abundance neighbors): PLOD2 (0.96), HYOU1 (0.95), LRP1 (0.85); STRING partners: GNS (0.936)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hexosaminidase subunit alpha. This gene encodes a member of the glycosyl hydrolase 20 family of proteins. The encoded preproprotein is proteolytically processed to generate the alpha subunit of the lysosomal enzyme beta-hexosaminidase. This enzyme, together with the cofactor GM2 activator protein, catalyzes the degradation of the ganglioside GM2, and other molecules containing terminal N-acetyl hexosamines. Mutations in this g…
- **Diseases (Open Targets)**: Tay-Sachs disease (0.863); hereditary disease (0.541); Tay-Sachs disease, B1 variant (0.475); Tay-Sachs disease AB variant (0.463); Tay-Sachs disease, b variant, juvenile form (0.453)
- **Europe PMC papers**: 16230
- **Why important**: HEXA is strongly connected to PLOD2, HYOU1, and LRP1 and forms the STRING-supported GNS–HEXA pair. It encodes the alpha subunit of lysosomal beta-hexosaminidase, which participates in ganglioside and other terminal N-acetyl-hexosamine degradation. Its annotations include lysosomal carbohydrate and lipid catabolism, and defects are associated with Tay-Sachs disease and neurodegeneration. Its cell-type annotations include choroid-plexus epithelial cells and microglia, making it particularly relevant to cerebrospinal-fluid-associated biology.
- **Conclusion**: Established: HEXA provides strong evidence for lysosomal glycan and ganglioside processing and has a known enzymatic relationship with GNS. Hypothesis: HEXA may connect cerebrospinal-fluid-associated clearance biology with the broader module, but its co-abundance does not demonstrate altered lysosomal flux or disease-specific pathology.

#### LRP1

- **Related proteins** (co-abundance neighbors): PLOD2 (0.87), HEXA (0.85), HYOU1 (0.82); STRING partners: CLU (0.715)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LDL receptor related protein 1. This gene encodes a member of the low-density lipoprotein receptor family of proteins. The encoded preproprotein is proteolytically processed by furin to generate 515 kDa and 85 kDa subunits that form the mature receptor (PMID: 8546712). This receptor is involved in several cellular processes, including intracellular signaling, lipid homeostasis, and clearance of apoptotic cells. In addition, the …
- **Diseases (Open Targets)**: neurodegenerative disease (0.514); keratosis pilaris atrophicans (0.499); developmental dysplasia of the hip (0.466); Alzheimer disease (0.462); Parkinson disease (0.443)
- **Europe PMC papers**: 10645
- **Why important**: LRP1 connects PLOD2, HEXA, HYOU1, and CLU and is supported by the STRING CLU–LRP1 relationship. It is a cell-surface receptor involved in lipid homeostasis, receptor-mediated endocytosis, phagocytosis, inflammatory regulation, apoptotic-cell clearance, and clearance of secreted amyloid-related material. Its HPA annotations include adipocytes, fibroblasts, fibro-adipogenic progenitors, hepatocytes, Kupffer cells, and several monocyte or myeloid-cell groups. Its disease associations include neurodegenerative disease, Alzheimer disease, Parkinson disease, and developmental dysplasia of the hip.
- **Conclusion**: Established: LRP1 is a plausible uptake and clearance hub linking extracellular material to myeloid and stromal cell biology. Hypothesis: it may mediate the shared handling of extracellular proteins or lipids across the two sample types, but the data do not establish whether this reflects receptor activity, abundance of expressing cells, or both.
