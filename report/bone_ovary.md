# Conserved co-abundance modules: bone and ovary

## Module 0

**Tissue pair**: bone and ovary  
**Genes (26)**: SLC3A2, ABHD10, ACSL3, ADPGK, ASPH, ATP1A1, ATP1B3, ATL3, EMC1, GNAI3, GNAS, GNAS, HMGCL, HSDL2, IDH3A, ITGA3, ITGB1, IVD, SLC7A5, NDUFA6, PDPR, PITRM1, RHOG, RTN4, STX6, IARS2

### Function

The strongest interpretation is a membrane-centered module coupling cell adhesion, plasma-membrane transport, ion gradients, and signaling. The globally corrected GO/KEGG evidence supports plasma-membrane and membrane-protein complexes (GO:CC plasma membrane protein complex; q_global = 0.000555)(GO:CC membrane protein complex; q_global = 0.00101), import across the plasma membrane (GO:BP import across plasma membrane; q_global = 0.01), amino-acid import (GO:BP amino acid import across plasma membrane; q_global = 0.0496), and positive regulation of protein localization to membranes (GO:BP positive regulation of protein localization to plasma membrane; q_global = 0.0372)(GO:BP positive regulation of protein localization to membrane; q_global = 0.0461). The gastric-acid-secretion term (KEGG Gastric acid secretion - Homo sapiens (human); q_global = 0.0228) is best viewed as pathway reuse of Na+/K+-ATPase and G-protein components rather than evidence that the bone or ovary module performs gastric secretion. The genes form several functional arms: the ITGA3–ITGB1 adhesion receptor, the SLC3A2–SLC7A5 amino-acid transporter, the ATP1A1–ATP1B3 ion pump, GNAS and GNAI3 signaling, and membrane trafficking or endoplasmic-reticulum organization involving STX6, EMC1, ATL3, and RTN4. Mitochondrial metabolic genes, including IVD, HMGCL, IDH3A, PDPR, NDUFA6, and PITRM1, suggest that membrane activity is accompanied by energetic and biosynthetic support. Thus, the established function is a coordinated membrane-interface and transport/signaling program, while any specific bone-ovary mechanism remains inferential.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the HPA summary identifies only a single secreted gene, while many annotated proteins are intracellular, mitochondrial, endoplasmic-reticulum, Golgi, or plasma-membrane proteins. Most genes have low tissue specificity, and many have cell-type-enhanced rather than tissue-restricted expression. Neutrophil and neutrophil-progenitor enrichment is a notable feature, with additional signals in bone marrow, plasmacytoid dendritic cells, monocytes, and basophils. However, the overall immune-cell specificity is generally low, so the module is not convincingly a blood-cell module on HPA evidence alone. Blood or shared-cell-type composition in the samples remains a plausible contributor, especially because several genes are associated with neutrophils and bone marrow. Conversely, ovarian protein detection is present for many module genes, whereas matching bone protein data are unavailable, so the HPA results do not independently establish bone-specific protein expression.

**GO/KEGG enrichment**: 7 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC plasma membrane protein complex | 0.000555 | ATP1A1, ATP1B3, GNAI3, GNAS, ITGA3, ITGB1, SLC3A2, SLC7A5 |
| GO:CC membrane protein complex | 0.00101 | ASPH, ATP1A1, ATP1B3, EMC1, GNAI3, GNAS, ITGA3, ITGB1, NDUFA6, SLC3A2, SLC7A5, STX6 |
| GO:BP import across plasma membrane | 0.01 | ATP1A1, ATP1B3, ITGB1, SLC3A2, SLC7A5 |
| KEGG Gastric acid secretion - Homo sapiens (human) | 0.0228 | ATP1A1, ATP1B3, GNAI3, GNAS |
| GO:BP positive regulation of protein localization to plasma membrane | 0.0372 | ACSL3, ITGA3, ITGB1, RHOG |
| GO:BP positive regulation of protein localization to membrane | 0.0461 | ACSL3, ITGA3, ITGB1, RHOG |
| GO:BP amino acid import across plasma membrane | 0.0496 | ITGB1, SLC3A2, SLC7A5 |

### STRING and hu.MAP

STRING provides strong support for several canonical physical or functional relationships: ATP1A1 with ATP1B3, ITGA3 with ITGB1, SLC3A2 with SLC7A5, ATL3 with RTN4, HMGCL with IDH3A, and HSDL2 with IVD. The STRING supplementary terms (15 supplementary STRING terms; within-query FDR 5.82e-05–0.0111) consistently support membrane localization, transport, cell-membrane organization, and signaling, but they are supplementary evidence and their reported FDR values are not global module-level significance. hu.MAP independently recovers the ITGA3–ITGB1 adhesion partnership in several complexes (hu.MAP huMAP3_06815.1)(hu.MAP huMAP3_10503.1)(hu.MAP huMAP3_10980.1)(hu.MAP huMAP3_09336.1), the ATP1A1–SLC7A5-containing complexes (hu.MAP huMAP3_10607.1)(hu.MAP huMAP3_10473.1), and a mitochondrial metabolic or translation-associated grouping containing IVD, HMGCL, PDPR, and IARS2 (hu.MAP huMAP3_13468.1)(hu.MAP huMAP3_10525.1). These results indicate that the module contains known molecular assemblies rather than being composed entirely of previously unconnected proteins. At the same time, many co-abundance edges have no listed STRING or hu.MAP counterpart, so the module is broader than a single established complex and may reflect coordinated cellular state rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 6 of 325 gene pairs: ATL3–RTN4 (0.826); ATP1A1–ATP1B3 (0.995); HMGCL–IDH3A (0.865); HSDL2–IVD (0.777); ITGA3–ITGB1 (0.999); SLC3A2–SLC7A5 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Intrinsic component of membrane (FDR = 5.82e-05, 12 genes); COMPARTMENTS Integral component of membrane (FDR = 0.00015, 11 genes); COMPARTMENTS Plasma membrane protein complex (FDR = 0.00015, 8 genes); Component Membrane protein complex (FDR = 0.00023, 12 genes); Component Plasma membrane protein complex (FDR = 0.00023, 8 genes); COMPARTMENTS Membrane protein complex (FDR = 0.00036, 12 genes); RCTM Basigin interactions (FDR = 0.00068, 5 genes); Component Intrinsic component of membrane (FDR = 0.00081, 15 genes); Component Integral component of membrane (FDR = 0.0032, 14 genes); Process Import into cell (FDR = 0.0042, 5 genes); Keyword Transmembrane helix (FDR = 0.0064, 12 genes); KEGG Gastric acid secretion (FDR = 0.0087, 4 genes); Keyword Cell membrane (FDR = 0.0095, 10 genes); KEGG cAMP signaling pathway (FDR = 0.0111, 4 genes); KEGG Adrenergic signaling in cardiomyocytes (FDR = 0.0111, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (IVD, HMGCL, PDPR, IARS2; 4/99); huMAP3_06815.1 (ITGB1, ITGA3; 2/5); huMAP3_10607.1 (ATP1A1, SLC7A5; 2/9); huMAP3_10473.1 (ATP1A1, SLC7A5; 2/24); huMAP3_10503.1 (ITGB1, ITGA3; 2/27); huMAP3_10525.1 (PDPR, IARS2; 2/33); huMAP3_10980.1 (ITGB1, ITGA3; 2/44); huMAP3_09336.1 (ITGB1, ITGA3; 2/50)

### Novelty

The module should not be claimed as a wholly new molecular pathway. Its central relationships and functions are established independently by STRING, hu.MAP, curated gene annotations, and substantial literature, particularly the integrin, amino-acid transporter, Na+/K+-ATPase, mitochondrial metabolism, and G-protein components. Nevertheless, the conserved co-abundance organization across bone and ovary may be a new systems-level observation, especially if this exact cross-tissue combination and its coordinated membrane-to-mitochondrial structure have not previously been reported. The absence of some module edges from STRING or hu.MAP is compatible with novelty but does not prove it, because database coverage, tissue context, and co-abundance evidence differ from physical-interaction evidence. A defensible novelty claim is therefore contextual: potentially novel as a conserved bone-ovary co-abundance program, but not novel in the individual molecular functions or core complexes.

**Hypothesis.** Hypothesis: this module represents a shared cell-state program in which integrin-mediated adhesion and cytoskeletal signaling organize plasma-membrane transport, while LAT1 amino-acid uptake and Na+/K+-ATPase activity maintain nutrient and ion gradients needed for cellular maintenance. GNAS, GNAI3, and RHOG could connect extracellular or adhesion-related cues to membrane localization, actin remodeling, and trafficking. Endoplasmic-reticulum and Golgi components could support delivery and recycling of these membrane proteins, while mitochondrial amino-acid, glucose, lipid, and respiratory machinery supplies the associated energetic demand. In bone and ovary, the shared signal could arise from stromal or epithelial cells using a common adhesion-and-transport state, or partly from shared immune or marrow-associated cells. This is a mechanistic model, not an established causal conclusion; testing would require cell-resolved data and perturbation of the transporter, integrin, or ion-pump arms.

### Important genes

#### ITGB1

- **Related proteins** (co-abundance neighbors): RHOG (0.84), RTN4 (0.83), ITGA3 (0.81), ACSL3 (0.80), SLC7A5 (0.80); STRING partners: ITGA3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_06815.1, huMAP3_10503.1, huMAP3_10980.1, huMAP3_09336.1
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is a high-connectivity node and lies at the center of the strongest adhesion evidence. It is paired with ITGA3 by STRING and appears in several hu.MAP adhesion and membrane-associated complexes (hu.MAP huMAP3_06815.1)(hu.MAP huMAP3_10503.1)(hu.MAP huMAP3_10980.1)(hu.MAP huMAP3_09336.1). It contributes to every primary membrane, import, and membrane-localization term relevant to the adhesion arm (GO:CC plasma membrane protein complex; q_global = 0.000555)(GO:CC membrane protein complex; q_global = 0.00101)(GO:BP import across plasma membrane; q_global = 0.01)(GO:BP positive regulation of protein localization to plasma membrane; q_global = 0.0372)(GO:BP positive regulation of protein localization to membrane; q_global = 0.0461)(GO:BP amino acid import across plasma membrane; q_global = 0.0496). Its established functions include cell adhesion, cell-matrix adhesion, phagocytosis, angiogenesis, and integrin signaling. It also has extensive literature and disease associations.
- **Conclusion**: Established conclusion: ITGB1 is a credible structural and signaling anchor of the module. Hypothesis: variation in ITGB1-centered adhesion may help coordinate the transport and metabolic components in both tissues, but the co-abundance data do not establish that ITGB1 regulates the other module genes.

#### SLC7A5

- **Related proteins** (co-abundance neighbors): SLC3A2 (0.85), ITGA3 (0.81), HMGCL (0.80), ITGB1 (0.80); STRING partners: SLC3A2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_10607.1, huMAP3_10473.1
- **Function (MyGene.info)**: solute carrier family 7 member 5. Enables L-leucine transmembrane transporter activity; L-tryptophan transmembrane transporter activity; and thyroid hormone transmembrane transporter activity. Involved in carboxylic acid transport; thyroid hormone transport; and xenobiotic transport. Located in cytosol; intracellular membrane-bounded organelle; and plasma membrane. Is integral component of membrane. Part of amino acid transport co…
- **Diseases (Open Targets)**: musculoskeletal system disorder (0.326); chronic central serous retinopathy (0.317); vertebral joint disorder (0.313); insomnia (0.313); type 2 diabetes mellitus (0.298)
- **Europe PMC papers**: 5282
- **Why important**: SLC7A5 is a high-connectivity membrane transporter, forms a very strong known partnership with SLC3A2 in STRING, and is represented in hu.MAP transport-related complexes (hu.MAP huMAP3_10607.1)(hu.MAP huMAP3_10473.1). It is present in the primary plasma-membrane and amino-acid import terms (GO:CC plasma membrane protein complex; q_global = 0.000555)(GO:CC membrane protein complex; q_global = 0.00101)(GO:BP import across plasma membrane; q_global = 0.01)(GO:BP amino acid import across plasma membrane; q_global = 0.0496), and its HPA profile includes bone marrow, neutrophils, monocytes, plasmacytoid dendritic cells, and plasma cells. Its established role in transporting large neutral amino acids makes it a plausible link between membrane state and cellular biosynthetic demand.
- **Conclusion**: Established conclusion: SLC7A5 is a well-supported nutrient-import component and a likely marker of the module's transport arm. Hypothesis: its coordinated abundance with integrin and ion-pump genes may reflect nutrient support for an adhesive or remodeling cell state, although immune-cell contribution must be excluded experimentally.

#### ATP1A1

- **Related proteins** (co-abundance neighbors): PITRM1 (0.81); STRING partners: ATP1B3 (0.995)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10607.1, huMAP3_10473.1
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 is the catalytic Na+/K+-ATPase subunit and is paired with ATP1B3 by STRING with very strong support. It appears in the primary membrane-complex, plasma-membrane-import, and gastric-acid-secretion terms (GO:CC plasma membrane protein complex; q_global = 0.000555)(GO:CC membrane protein complex; q_global = 0.00101)(GO:BP import across plasma membrane; q_global = 0.01)(KEGG Gastric acid secretion - Homo sapiens (human); q_global = 0.0228), with matching supplementary STRING support (6 supplementary STRING terms; within-query FDR 5.82e-05–0.00036) and (6 supplementary STRING terms; within-query FDR 0.0042–0.0111). Its established role in maintaining sodium and potassium gradients provides a direct mechanism for supporting membrane transport and excitability. It also has substantial literature and disease associations.
- **Conclusion**: Established conclusion: ATP1A1 is a central ion-homeostasis component of the module. Hypothesis: coordinated ATP1A1 abundance could permit the amino-acid transport and signaling activities represented by SLC7A5, SLC3A2, GNAS, and GNAI3, but energetic coupling is not demonstrated by the network alone.

#### GNAS

- **Related proteins** (co-abundance neighbors): GNAS (0.99), NDUFA6 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GNAS complex locus. This locus has a highly complex imprinted expression pattern. It gives rise to maternally, paternally, and biallelically expressed transcripts that are derived from four alternative promoters and 5' exons. Some transcripts contain a differentially methylated region (DMR) at their 5' exons, and this DMR is commonly found in imprinted genes and correlates with transcript expression. An antisense tra…
- **Diseases (Open Targets)**: pseudohypoparathyroidism type 1A (0.839); pseudohypoparathyroidism type 1C (0.816); McCune-Albright syndrome (0.811); Albright hereditary osteodystrophy (0.798); pseudohypoparathyroidism type 1B (0.797)
- **Europe PMC papers**: 10304
- **Why important**: GNAS contributes to the primary membrane-complex and gastric-acid-secretion terms (GO:CC plasma membrane protein complex; q_global = 0.000555)(GO:CC membrane protein complex; q_global = 0.00101)(KEGG Gastric acid secretion - Homo sapiens (human); q_global = 0.0228) and to supplementary cAMP, adrenergic, membrane, and plasma-membrane signaling terms (STRING COMPARTMENTS Plasma membrane protein complex; within-query FDR = 0.00015)(STRING Component Plasma membrane protein complex; within-query FDR = 0.00023)(4 supplementary STRING terms; within-query FDR 0.0087–0.0111). Its established biology includes G-protein signaling, ovarian follicle development, glucose homeostasis, and imprinted regulation, and it has extensive literature and strong disease associations involving endocrine and skeletal phenotypes. Its network degree is more modest than the main transporter and adhesion nodes, but its signaling interpretation makes it biologically important.
- **Conclusion**: Established conclusion: GNAS provides a plausible signal-transduction component connecting membrane inputs to intracellular responses and is particularly relevant to the bone-ovary tissue pairing. Hypothesis: GNAS may help translate adhesion or nutrient-related membrane cues into tissue-specific cellular responses, but the module does not identify the upstream receptor or downstream cAMP effector.

#### RHOG

- **Related proteins** (co-abundance neighbors): GNAI3 (0.88), ITGB1 (0.84), RTN4 (0.83), PITRM1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ras homolog family member G. This gene encodes a member of the Rho family of small GTPases, which cycle between inactive GDP-bound and active GTP-bound states and function as molecular switches in signal transduction cascades. Rho proteins promote reorganization of the actin cytoskeleton and regulate cell shape, attachment, and motility. The encoded protein facilitates translocation of a functional guanine nucleotide exchange…
- **Diseases (Open Targets)**: atrial fibrillation (0.428); cancer (0.373); kidney transplant (0.296); eosinophilic esophagitis (0.239); cardiac arrhythmia (0.128)
- **Europe PMC papers**: 1929
- **Why important**: RHOG is among the more connected genes in the co-abundance graph and links to ITGB1, GNAI3, RTN4, and PITRM1. It is represented in the primary membrane-localization terms (GO:BP positive regulation of protein localization to plasma membrane; q_global = 0.0372)(GO:BP positive regulation of protein localization to membrane; q_global = 0.0461) and has established functions in actin organization, cell polarity, cell shape, motility, and Rho-family signaling. HPA places it in a bone-marrow-enhanced context and in several myeloid-related cell types. Its literature volume and disease associations are substantial, though less extensive than those of ITGB1 or GNAS.
- **Conclusion**: Established conclusion: RHOG is a plausible cytoskeletal and membrane-trafficking link between integrin-associated adhesion and signaling. Hypothesis: RHOG may mediate remodeling or migration in the shared cell state, but its absence from the listed STRING and hu.MAP relationships means this proposed bridging role requires direct validation.

## Module 1

**Tissue pair**: bone and ovary  
**Genes (7)**: AATF, BRIX1, CLINT1, NOL11, RPF2, RRS1, UTP14A

### Function

This is a nucleolar ribosome-biogenesis module. The strongest primary evidence is the coordinated representation of ribosome biogenesis and ribonucleoprotein-complex biogenesis (GO:BP ribosome biogenesis; q_global = 0.000417) (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.00178), with additional global evidence for rRNA processing, large-subunit assembly, rRNA metabolism, rRNA binding, ribosome assembly, nucleolar localization, and five-S rRNA binding (7 globally significant GO/KEGG terms, q_global 0.00364–0.0481; see the table). Six of the module genes contribute to the broad ribosome-biogenesis and nucleolar signals, while the large-subunit assembly and five-S rRNA-binding signals are driven particularly by BRIX1, RPF2, and RRS1. CLINT1 is the functional outlier: its annotation concerns clathrin-coated-vesicle assembly and endocytic trafficking rather than ribosome production. Thus, the most coherent interpretation is a ribosome-production and nucleolar-processing program, with CLINT1 potentially reflecting a peripheral or context-dependent co-abundance relationship rather than the central module function.

**Cell composition.** The module is not composed of secreted or plasma proteins, and the HPA profile does not indicate a blood-cell-dominated module. All genes have low tissue specificity, so the signal is better viewed as a broadly distributed cellular program than as a bone- or ovary-exclusive program. Several genes show cell-type enhancement in oocytes or trophoblast-related cells, while other enhancements occur in renal, germ-cell, erythroid, epithelial, or progenitor populations. The repeated oocyte association may be relevant to the bone–ovary comparison, but it does not establish ovary specificity. Protein detection in ovary for most assessed genes is compatible with activity of this intracellular nucleolar program there. The shared module could therefore reflect common proliferative, biosynthetic, or cell-state composition across the tissues rather than a tissue-specific extracellular mechanism.

**GO/KEGG enrichment**: 9 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP ribosome biogenesis | 0.000417 | AATF, BRIX1, NOL11, RPF2, RRS1, UTP14A |
| GO:BP ribonucleoprotein complex biogenesis | 0.00178 | AATF, BRIX1, NOL11, RPF2, RRS1, UTP14A |
| GO:BP rRNA processing | 0.00364 | BRIX1, NOL11, RPF2, RRS1, UTP14A |
| GO:BP ribosomal large subunit assembly | 0.00418 | BRIX1, RPF2, RRS1 |
| GO:BP rRNA metabolic process | 0.00665 | BRIX1, NOL11, RPF2, RRS1, UTP14A |
| GO:MF rRNA binding | 0.0257 | BRIX1, RPF2, RRS1 |
| GO:BP ribosome assembly | 0.0257 | BRIX1, RPF2, RRS1 |
| GO:CC nucleolus | 0.0327 | AATF, BRIX1, NOL11, RPF2, RRS1, UTP14A |
| GO:MF 5S rRNA binding | 0.0481 | RPF2, RRS1 |

### STRING and hu.MAP

STRING provides strong supplementary support for the proposed function. The module contains a densely connected core involving AATF, BRIX1, RPF2, RRS1, NOL11, and UTP14A, with especially strong relationships among RPF2, RRS1, and BRIX1 and between AATF and UTP14A. STRING functional terms independently point to preribosome formation, ribosome biogenesis, rRNA processing, large-subunit assembly, nucleolar localization, and rRNA binding (10 supplementary STRING terms; within-query FDR 9.06e-06–0.0344). These are concordant with, but secondary to, the globally corrected GO results. CLINT1 has no reported STRING partner within this module and is therefore not supported by the interaction evidence as part of the nucleolar core. No hu.MAP complex contains multiple module members. The lack of a hu.MAP complex does not negate the module; it indicates that the co-abundance group is not reproduced as a curated hu.MAP multi-member complex in the supplied resource.

**STRING interactions (score >= 0.7)**: 10 of 21 gene pairs: AATF–BRIX1 (0.853); AATF–NOL11 (0.811); AATF–RPF2 (0.789); AATF–UTP14A (0.996); BRIX1–RPF2 (0.993); BRIX1–RRS1 (0.977); NOL11–UTP14A (0.922); RPF2–RRS1 (0.999); RPF2–UTP14A (0.89); RRS1–UTP14A (0.76)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 9.06e-06, 6 genes); Keyword Ribosome biogenesis (FDR = 1.31e-05, 5 genes); Process Ribosome biogenesis (FDR = 0.00059, 6 genes); NetworkNeighborAL Preribosome, large subunit precursor, and Maturation of LSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA) (FDR = 0.0025, 3 genes); COMPARTMENTS Nucleolus (FDR = 0.0031, 6 genes); Process rRNA processing (FDR = 0.0035, 5 genes); Process Ribosomal large subunit assembly (FDR = 0.0065, 3 genes); NetworkNeighborAL rRNA modification in the nucleus and cytosol (FDR = 0.0124, 3 genes); NetworkNeighborAL Mixed, incl. 5S rRNA binding, and Brain meningioma (FDR = 0.014, 2 genes); SMART The Brix domain is found in a number of eukaryotic proteins including SSF proteins from yeast and humans, Arabidopsis thaliana Peter Pan-like protein and several hypothetical proteins. (FDR = 0.0148, 2 genes); Component Nucleolus (FDR = 0.0156, 6 genes); Function rRNA binding (FDR = 0.0344, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The biological function is not a new molecular mechanism: the genes are established ribosome-biogenesis or nucleolar factors, and many of their relationships are already represented in STRING. The absence of a hu.MAP complex and the absence of a STRING relationship for CLINT1 are insufficient to claim novelty. What may be novel is the tissue-pair-level co-abundance pattern, particularly the coordinated appearance of this nucleolar program in bone and ovary, but the supplied evidence does not establish that this pattern is absent from prior tissue-expression studies or that it represents a new physical complex. The defensible conclusion is a potentially interesting context-specific module organization built from largely known biology, not a demonstrably new pathway or interaction network.

**Hypothesis.** Hypothesis: the module represents a shared demand for nucleolar ribosome production in a common cellular state present in bone and ovary, potentially involving biosynthetically active or proliferative cells. The core factors may act together during preribosome formation, rRNA maturation, and large-subunit assembly, while AATF may connect this program to transcriptional and stress-related regulation. The co-abundance of CLINT1 with AATF could reflect cell-state coupling or vesicle-trafficking activity in the same cells rather than direct participation in ribosome biogenesis. This hypothesis should be tested with cell-composition adjustment, independent expression cohorts, perturbation of core nucleolar factors, and measurement of rRNA-processing outputs.

### Important genes

#### RPF2

- **Related proteins** (co-abundance neighbors): NOL11 (0.91), BRIX1 (0.89), RRS1 (0.85); STRING partners: AATF (0.789), BRIX1 (0.993), RRS1 (0.999), UTP14A (0.89)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosome production factor 2 homolog. Enables 5S rRNA binding activity. Involved in protein localization to nucleolus; regulation of signal transduction by p53 class mediator; and ribosomal large subunit biogenesis. Located in chromosome; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.479); Hypercholesterolemia (0.196); colorectal carcinoma (0.079); Helicobacter pylori infectious disease (0.048); asthma (0.047)
- **Europe PMC papers**: 424
- **Why important**: RPF2 is one of the most central module genes by network position and has strong relationships with BRIX1 and RRS1. It contributes to every primary enrichment term (9 globally significant GO/KEGG terms, q_global 0.000417–0.0481; see the table) and to the broad STRING ribosome-biogenesis, rRNA-processing, nucleolar, and large-subunit signals (10 supplementary STRING terms; within-query FDR 9.06e-06–0.0344). Its annotation directly supports five-S rRNA binding, nucleolar localization, rRNA maturation, and large-subunit biogenesis. It has disease associations including neurodegenerative disease and hypercholesterolemia, and its literature base is established though smaller than that of the most extensively studied module genes.
- **Conclusion**: Established evidence identifies RPF2 as a central large-subunit and rRNA-processing factor and a strong candidate core driver of the module. Its role in the bone–ovary co-abundance pattern remains a hypothesis requiring tissue-specific validation.

#### RRS1

- **Related proteins** (co-abundance neighbors): RPF2 (0.85); STRING partners: BRIX1 (0.977), RPF2 (0.999), UTP14A (0.76)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: regulator of ribosome synthesis 1. Enables 5S rRNA binding activity. Involved in several processes, including mitotic metaphase plate congression; protein localization to nucleolus; and ribosomal large subunit assembly. Located in condensed nuclear chromosome; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.473); post term pregnancy (0.229); breast cancer (0.111); breast carcinoma (0.101); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 1546
- **Why important**: RRS1 is tightly connected to RPF2 and BRIX1 in STRING, contributes to the large-subunit, rRNA-binding, and nucleolar primary signals (9 globally significant GO/KEGG terms, q_global 0.000417–0.0481; see the table), and participates in nearly all corresponding supplementary STRING annotations (9 supplementary STRING terms; within-query FDR 9.06e-06–0.0344). Its known functions include five-S rRNA binding, large-subunit assembly, rRNA cleavage, nucleolar localization, and regulation of p53-mediated signaling. It has substantial literature and disease associations including neurodegenerative disease, pregnancy-related disease, and carcinomas.
- **Conclusion**: Established evidence supports RRS1 as a core ribosome-biogenesis factor and a particularly informative marker of the module's large-subunit arm. Its disease associations do not demonstrate that the module causes those diseases; they motivate testing whether altered ribosome production contributes to relevant tissue states.

#### BRIX1

- **Related proteins** (co-abundance neighbors): RPF2 (0.89); STRING partners: AATF (0.853), RPF2 (0.993), RRS1 (0.977)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Mitotic chromosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biogenesis of ribosomes BRX1. Enables RNA binding activity. Predicted to be involved in ribosomal large subunit assembly. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: colorectal cancer (0.077); cancer (0.077); colorectal carcinoma (0.074); deficiency anemia (0.065); sialolithiasis (0.060)
- **Europe PMC papers**: 251
- **Why important**: BRIX1 is strongly linked to RPF2 and RRS1 and is represented in the primary evidence for ribosome biogenesis, rRNA processing, large-subunit assembly, rRNA binding, ribosome assembly, and nucleolar localization (8 globally significant GO/KEGG terms, q_global 0.000417–0.0327; see the table). STRING independently supports its preribosome and large-subunit relationships (9 supplementary STRING terms; within-query FDR 9.06e-06–0.0344). Its annotation directly identifies a ribosome-biogenesis role, and HPA shows enhancement in oocytes and trophoblast-related cell types, which may be relevant to the shared tissue context. Disease associations include colorectal cancer and deficiency anemia.
- **Conclusion**: Established evidence places BRIX1 in the nucleolar large-subunit assembly core. Its cell-type pattern is compatible with a reproductive or developmental contribution, but the current data do not establish a bone–ovary-specific role.

#### AATF

- **Related proteins** (co-abundance neighbors): NOL11 (0.91), UTP14A (0.90), CLINT1 (0.87); STRING partners: BRIX1 (0.853), NOL11 (0.811), RPF2 (0.789), UTP14A (0.996)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apoptosis antagonizing transcription factor. The protein encoded by this gene was identified on the basis of its interaction with MAP3K12/DLK, a protein kinase known to be involved in the induction of cell apoptosis. This gene product contains a leucine zipper, which is a characteristic motif of transcription factors, and was shown to exhibit strong transactivation activity when fused to Gal4 DNA binding domain. Overexpression of this gene i…
- **Diseases (Open Targets)**: skin neoplasm (0.147); generalized dystonia (0.116); multinodular goiter (0.115); bone fracture (0.113); neoplasm (0.107)
- **Europe PMC papers**: 6349
- **Why important**: AATF has a central position in the co-abundance subgraph and connects to multiple nucleolar partners, including UTP14A, NOL11, BRIX1, and RPF2 in STRING. It contributes to the primary ribosome-biogenesis, ribonucleoprotein-complex biogenesis, and nucleolar terms (GO:BP ribosome biogenesis; q_global = 0.000417) (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.00178) (GO:CC nucleolus; q_global = 0.0327), as well as STRING evidence for preribosome formation, rRNA processing, nucleolar localization, and rRNA modification (5 supplementary STRING terms; within-query FDR 9.06e-06–0.0156). Its annotation combines rRNA maturation with transcriptional regulation and apoptosis-related biology. It has an extensive literature base and reported associations with neoplasm, bone fracture, dystonia, and multinodular goiter.
- **Conclusion**: Established evidence supports AATF as a bridge between nucleolar RNA production and broader transcriptional or stress-response regulation. Its association with bone fracture is noteworthy but does not prove that this module mediates bone biology; that connection is a testable hypothesis.

#### UTP14A

- **Related proteins** (co-abundance neighbors): AATF (0.90); STRING partners: AATF (0.996), NOL11 (0.922), RPF2 (0.89), RRS1 (0.76)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UTP14A small subunit processome component. This gene encodes a member of the uridine triphosphate 14 family. As an essential component of a large ribonucleoprotein complex bound to the U3 small nucleolar RNA, the encoded protein is involved in ribosome biogenesis and 18S rRNA synthesis. An autosomal retrotransposed copy of this X-linked gene exists on chromosome 13. Alternative splicing results in multiple transcript variants.[provided by …
- **Diseases (Open Targets)**: male infertility with azoospermia or oligozoospermia due to single gene mutation (0.085); partial chromosome Y deletion (0.080); non-syndromic male infertility due to sperm motility disorder (0.076); esophageal squamous cell carcinoma (0.072); 46 XX gonadal dysgenesis (0.071)
- **Europe PMC papers**: 277
- **Why important**: UTP14A is connected to AATF in the module and has strong STRING relationships with AATF, NOL11, RPF2, and RRS1. It contributes to the primary ribosome-biogenesis, ribonucleoprotein-complex biogenesis, rRNA-processing, rRNA-metabolism, and nucleolar terms (5 globally significant GO/KEGG terms, q_global 0.000417–0.0327; see the table), with concordant supplementary STRING support (7 supplementary STRING terms; within-query FDR 9.06e-06–0.0156). Its annotation identifies it as a U3-small-nucleolar-RNA-associated component involved in small-subunit production and eighteen-S rRNA synthesis. HPA shows oocyte enhancement, and disease associations include infertility-related phenotypes and gonadal dysgenesis.
- **Conclusion**: Established evidence identifies UTP14A as a small-subunit processome component and a plausible contributor to the oocyte-associated aspect of the module. The reproductive disease associations support biological relevance but do not establish that this shared module causes ovarian or gonadal phenotypes.

## Module 2

**Tissue pair**: bone and ovary  
**Genes (16)**: GOT2, CS, TUFM, GOLT1B, CPOX, OAT, POLDIP2, PNPT1, PRDX3, PRDX4, DARS2, TFRC, TIMM44, TMX1, TRAP1, SLC30A7

### Function

The strongest interpretation is a mitochondrial metabolic and proteostatic module. The primary globally corrected evidence is enrichment for mitochondrial matrix and mitochondrion (GO:CC mitochondrial matrix; q_global = 0.000287)(GO:CC mitochondrion; q_global = 0.0015). The module contains enzymes of the tricarboxylic acid cycle and amino-acid metabolism such as CS, GOT2, and OAT; mitochondrial protein import and chaperoning components such as TIMM44 and TRAP1; mitochondrial translation and RNA-processing components such as DARS2, TUFM, and PNPT1; and redox-protective proteins such as PRDX3. CPOX adds a connection to mitochondrial heme biosynthesis, while TFRC and SLC30A7 connect the module to iron and zinc handling. STRING supplementary annotations independently support mitochondrial targeting and matrix localization (STRING Keyword Transit peptide; within-query FDR = 1.91e-06)(STRING Component Mitochondrial matrix; within-query FDR = 4.73e-05)(STRING Keyword Mitochondrion; within-query FDR = 0.0002)(STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.00027)(STRING Component Mitochondrion; within-query FDR = 0.00077)(STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0012). No KEGG term is listed as having passed global correction. Overall, the module is most consistent with coordinated mitochondrial energy metabolism, macromolecular maintenance, and oxidative-stress control rather than a narrowly bone-specific or ovary-specific pathway.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. The genes are mainly intracellular mitochondrial, endoplasmic-reticulum, Golgi, or vesicular proteins, with only a minor secreted-to-blood signal represented by TFRC in the HPA summary. Most genes have low immune-cell specificity, and the module is not strongly blood-cell enriched; CPOX has an association with erythrocyte progenitors and TFRC is immune-cell enhanced in non-classical monocytes, but these are not sufficient to define the whole module as a blood-cell program. The broad tissue distribution and frequent low tissue specificity are compatible with a housekeeping-like mitochondrial program. HPA also shows enrichment in metabolically active cell types and tissues, including hepatocytes, muscle-related tissues, cardiomyocytes, adipocytes, trophoblasts, and oocytes. Thus, shared abundance in bone and ovary may reflect common oxidative and biosynthetic demands, shared cell types, or sample composition rather than a specialized function unique to those organs.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrial matrix | 0.000287 | CS, DARS2, GOT2, OAT, PNPT1, POLDIP2, PRDX3, TIMM44, TRAP1, TUFM |
| GO:CC mitochondrion | 0.0015 | CPOX, CS, DARS2, GOT2, OAT, PNPT1, POLDIP2, PRDX3, SLC30A7, TIMM44, TMX1, TRAP1, TUFM |

### STRING and hu.MAP

STRING provides strong direct support for the CS–GOT2 relationship and the GOT2–TUFM relationship. These links connect central carbon metabolism with mitochondrial translation, but the limited number of directly supported STRING pairs means that most co-abundance edges are not established physical interactions in STRING. hu.MAP provides complementary complex evidence: TRAP1, DARS2, and PNPT1 co-occur in (hu.MAP huMAP3_13468.1), PRDX3 and PRDX4 co-occur in (hu.MAP huMAP3_12666.1), and TFRC and GOLT1B co-occur in (hu.MAP huMAP3_10725.1). The hu.MAP complexes are broad and include many proteins outside this module, so they support shared complex or compartment context rather than proving that every module member forms one physical complex. Together, STRING and hu.MAP support a biologically coherent mitochondrial and organelle-maintenance program, while also showing that the abundance network is not simply a known protein-interaction complex.

**STRING interactions (score >= 0.7)**: 2 of 120 gene pairs: CS–GOT2 (0.952); GOT2–TUFM (0.849)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transit peptide (FDR = 1.91e-06, 11 genes); Component Mitochondrial matrix (FDR = 4.73e-05, 10 genes); Keyword Mitochondrion (FDR = 0.0002, 11 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.00027, 9 genes); Component Mitochondrion (FDR = 0.00077, 12 genes); COMPARTMENTS Mitochondrion (FDR = 0.0012, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (TRAP1, DARS2, PNPT1; 3/99); huMAP3_12666.1 (PRDX3, PRDX4; 2/5); huMAP3_10725.1 (TFRC, GOLT1B; 2/59)

### Novelty

The biological theme itself is not new: mitochondrial metabolism, import, translation, redox control, and heme handling are established functions, and several relationships are already represented by STRING or hu.MAP. However, the specific conserved co-abundance module shared by bone and ovary may still be a new systems-level observation. Its novelty would lie in the cross-tissue co-regulation and in the particular combination of metabolic enzymes, mitochondrial maintenance factors, redox proteins, and organelle-trafficking components. That claim should remain provisional because absence from interaction resources does not prove novelty, and the available evidence does not establish whether the pattern arises from within-cell regulation, shared cell composition, or technical and sample-level effects.

**Hypothesis.** Hypothesis: bone and ovary share a coordinated mitochondrial state in which respiratory metabolism and amino-acid flux are coupled to mitochondrial protein import, translation, RNA quality control, heme production, metal handling, and peroxide detoxification. CS and GOT2 may represent the metabolic core; TRAP1 and TIMM44 may help maintain imported and folded mitochondrial proteins; DARS2, TUFM, and PNPT1 may maintain mitochondrial gene expression; and PRDX3 may buffer the resulting oxidative burden. The shared module could therefore reflect a common demand for mitochondrial resilience in metabolically active bone and ovarian cells. This is a mechanistic model, not a demonstrated causal pathway, and it should be tested with cell-type-resolved data, mitochondrial functional measurements, and perturbation of selected hub genes.

### Important genes

#### CS

- **Related proteins** (co-abundance neighbors): DARS2 (0.82), OAT (0.81), GOT2 (0.80), PRDX3 (0.80); STRING partners: GOT2 (0.952)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS has the strongest network position in the module and connects to DARS2, OAT, GOT2, and PRDX3. It is a mitochondrial matrix tricarboxylic-acid-cycle enzyme, appears in both primary enrichment terms (GO:CC mitochondrial matrix; q_global = 0.000287)(GO:CC mitochondrion; q_global = 0.0015) and all listed STRING supplementary terms, and has extensive literature coverage. Its ovary protein detection and tissue enhancement in skeletal muscle and tongue are consistent with a broadly used oxidative-metabolism component.
- **Conclusion**: Established evidence supports CS as a central mitochondrial metabolic marker and a network anchor. It is plausible, but not established, that CS abundance helps couple carbon flux to the other module processes in bone and ovary.

#### GOT2

- **Related proteins** (co-abundance neighbors): CS (0.80); STRING partners: CS (0.952), TUFM (0.849)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamic-oxaloacetic transaminase 2. Glutamic-oxaloacetic transaminase is a pyridoxal phosphate-dependent enzyme which exists in cytoplasmic and inner-membrane mitochondrial forms, GOT1 and GOT2, respectively. GOT plays a role in amino acid metabolism and the urea and tricarboxylic acid cycles. The two enzymes are homodimeric and show close homology. Two transcript variants encoding different isoforms have been found for this gene. […
- **Diseases (Open Targets)**: genetic developmental and epileptic encephalopathy (0.618); developmental and epileptic encephalopathy (0.393); Encephalopathy (0.370); neurodegenerative disease (0.356); lagophthalmos (0.298)
- **Europe PMC papers**: 2463
- **Why important**: GOT2 is directly connected to CS in STRING and to TUFM, making it the clearest bridge between central metabolism and mitochondrial translation. It participates in amino-acid metabolism and the tricarboxylic-acid and urea-cycle context, appears in (GO:CC mitochondrial matrix; q_global = 0.000287)(GO:CC mitochondrion; q_global = 0.0015) and all STRING supplementary terms, and has ovary protein detection. Its tissue pattern also points to metabolically active tissues and hepatocytes.
- **Conclusion**: Established evidence identifies GOT2 as a mitochondrial metabolic enzyme with unusually strong direct network support in this module. The proposed bridge between metabolic flux and mitochondrial translation is a hypothesis derived from the network, not a demonstrated physical or regulatory mechanism.

#### TRAP1

- **Related proteins** (co-abundance neighbors): POLDIP2 (0.87), DARS2 (0.85), SLC30A7 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: TNF receptor associated protein 1. This gene encodes a mitochondrial chaperone protein that is member of the heat shock protein 90 (HSP90) family. The encoded protein has ATPase activity and interacts with tumor necrosis factor type I. This protein may function in regulating cellular stress responses. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jan 2013].
- **Diseases (Open Targets)**: congenital anomaly of kidney and urinary tract (0.643); VACTERL/vater association (0.492); atrial fibrillation (0.467); neurodegenerative disease (0.372); Blindness (0.338)
- **Europe PMC papers**: 2586
- **Why important**: TRAP1 has a highly connected position and links POLDIP2, DARS2, and SLC30A7. It is a mitochondrial HSP ninety-family chaperone associated with protein folding and cellular stress responses, appears in both primary mitochondrial terms (GO:CC mitochondrial matrix; q_global = 0.000287)(GO:CC mitochondrion; q_global = 0.0015) and all STRING supplementary terms, and is represented in hu.MAP complex (hu.MAP huMAP3_13468.1). HPA also reports oocyte cell-type enhancement and ovary protein detection, which is particularly relevant to the tissue pair.
- **Conclusion**: Established evidence supports TRAP1 as a mitochondrial proteostasis and stress-response component with direct relevance to ovarian cells. Its role as a coordinator linking metal handling, translation, and metabolic maintenance in this module remains a hypothesis.

#### DARS2

- **Related proteins** (co-abundance neighbors): TRAP1 (0.85), PNPT1 (0.84), CS (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 2, mitochondrial. The protein encoded by this gene belongs to the class-II aminoacyl-tRNA synthetase family. It is a mitochondrial enzyme that specifically aminoacylates aspartyl-tRNA. Mutations in this gene are associated with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation (LBSL). [provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: leukoencephalopathy with brain stem and spinal cord involvement-high lactate syndrome (0.843); neurodegenerative disease (0.527); hereditary disease (0.518); hypertensive disorder (0.425); Cerebral cortical atrophy (0.425)
- **Europe PMC papers**: 796
- **Why important**: DARS2 occupies a central position linking TRAP1, PNPT1, and CS. It is the mitochondrial aspartyl-tRNA synthetase, appears in both primary enrichment terms (GO:CC mitochondrial matrix; q_global = 0.000287)(GO:CC mitochondrion; q_global = 0.0015) and all STRING supplementary terms, and is included in hu.MAP complex (hu.MAP huMAP3_13468.1). Its established disease association with leukoencephalopathy and lactate elevation underscores the importance of mitochondrial translation and respiratory competence.
- **Conclusion**: Established evidence supports DARS2 as a core mitochondrial translation factor whose dysfunction can impair oxidative metabolism. Its co-abundance with metabolic and protein-quality-control genes suggests coordinated mitochondrial maintenance, but the module does not establish that DARS2 regulates the other genes.

#### PRDX3

- **Related proteins** (co-abundance neighbors): CS (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_12666.1
- **Function (MyGene.info)**: peroxiredoxin 3. This gene encodes a mitochondrial protein with antioxidant function. The protein is similar to the C22 subunit of Salmonella typhimurium alkylhydroperoxide reductase, and it can rescue bacterial resistance to alkylhydroperoxide in E. coli that lack the C22 subunit. The human and mouse genes are highly conserved, and they map to the regions syntenic between mouse and human chromosomes. Sequence com…
- **Diseases (Open Targets)**: spinocerebellar ataxia, autosomal recessive 32 (0.653); corneal dystrophy, punctiform and polychromatic pre-descemet (0.571); autosomal recessive cerebellar ataxia (0.268); neurodegenerative disease (0.257); hereditary disease (0.191)
- **Europe PMC papers**: 2613
- **Why important**: PRDX3 connects to CS and is one of the module's mitochondrial antioxidant components. It appears in both primary mitochondrial terms (GO:CC mitochondrial matrix; q_global = 0.000287)(GO:CC mitochondrion; q_global = 0.0015) and all STRING supplementary terms, and it is represented in hu.MAP complex (hu.MAP huMAP3_12666.1) with PRDX4. Its established function in peroxide reduction and oxidative-stress responses makes it biologically important for protecting the metabolic and translation machinery represented by the module.
- **Conclusion**: Established evidence supports PRDX3 as a mitochondrial redox-protection factor. It is reasonable to hypothesize that its coordinated abundance buffers oxidative stress generated by the module's metabolic activity, but this buffering role has not been demonstrated specifically in the bone–ovary module.

#### TFRC

- **Related proteins** (co-abundance neighbors): TMX1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes, Lysosomes; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_10725.1
- **Function (MyGene.info)**: transferrin receptor. This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: TFRC-related combined immunodeficiency (0.623); type 2 diabetes mellitus (0.518); mucopolysaccharidosis type 2 (0.490); diabetes mellitus (0.471); diabetic retinopathy (0.343)
- **Europe PMC papers**: 14164
- **Why important**: TFRC is a useful peripheral and interpretive gene in the module. It links the network to cellular iron uptake, erythropoiesis, hypoxia responses, and endosomal trafficking; it is included in hu.MAP complex (hu.MAP huMAP3_10725.1), has ovary protein detection, and is the only module member explicitly reported as secreted to blood and immune-cell enhanced. Its presence provides a plausible connection between iron availability, heme production through CPOX, and mitochondrial function.
- **Conclusion**: Established evidence supports TFRC as an iron-uptake and cellular-context marker, not as a mitochondrial matrix component. Its inclusion may reflect iron and heme demand, or it may indicate cell-composition effects; distinguishing these possibilities requires cell-type-resolved measurements.

## Module 3

**Tissue pair**: bone and ovary  
**Genes (33)**: ACIN1, ADNP, PRMT5, CHERP, DDX5, DHX9, ADAR, EIF2B4, FIP1L1, HNRNPH1, HNRNPL, HNRNPR, PAK2, PPP6R3, PRPF4, RBM10, RBM39, MRPL2, POLR2A, SF3B3, SMARCE1, SNRNP40, SNW1, SRSF7, XAB2, ALYREF, TP53BP1, SNRNP200, EFTUD2, UBTF, YLPM1, ZMYND8, TJP1

### Function

The module is a conserved nuclear RNA-processing and pre-mRNA-splicing module. The primary evidence is exceptionally coherent: globally corrected terms identify RNA splicing and spliceosome biology (GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 6.18e-11), (GO:BP mRNA splicing, via spliceosome; q_global = 6.18e-11), (GO:BP RNA splicing, via transesterification reactions; q_global = 7.31e-11), (GO:BP RNA splicing; q_global = 1.24e-08), mRNA processing and RNA metabolism (GO:BP mRNA processing; q_global = 8.35e-10), (GO:BP mRNA metabolic process; q_global = 1.04e-07), the KEGG spliceosome (KEGG Spliceosome - Homo sapiens (human); q_global = 1.09e-07), the catalytic step two spliceosome (GO:CC catalytic step 2 spliceosome; q_global = 6.14e-06), the spliceosomal complex (GO:CC spliceosomal complex; q_global = 6.98e-06), regulation of RNA splicing (GO:BP regulation of RNA splicing; q_global = 7.45e-06), and the U2-type spliceosomal complex (GO:CC U2-type spliceosomal complex; q_global = 0.00245). The nucleoplasm, nuclear speck, nuclear ribonucleoprotein granule, and spliceosomal snRNP annotations (GO:CC nucleoplasm; q_global = 2.42e-06), (GO:CC catalytic step 2 spliceosome; q_global = 6.14e-06), (GO:CC nuclear ribonucleoprotein granule; q_global = 8.47e-06), (GO:CC nuclear speck; q_global = 1.99e-05), (GO:CC spliceosomal snRNP complex; q_global = 0.0311) support a physically coherent nuclear process rather than a generic association. Most of the module is composed of spliceosomal proteins, RNA helicases, heterogeneous nuclear ribonucleoproteins, RNA-binding proteins, and factors involved in RNA export or transcription. The module therefore most plausibly represents coordinated abundance of the spliceosome and coupled RNA maturation machinery in bone and ovary. The additional nucleic-acid, transcription, chromatin, and DNA-damage annotations (GO:BP RNA biosynthetic process; q_global = 2.91e-06), (GO:BP nucleic acid biosynthetic process; q_global = 6.64e-06), (GO:MF nucleic acid binding; q_global = 7.63e-06), (GO:BP nucleic acid metabolic process; q_global = 6.01e-05) suggest functional coupling to gene expression and genome maintenance, but they are secondary to the strong splicing signal.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly intracellular and nuclear. It is also not strongly blood-cell specific. HPA reports low immune-cell specificity for nearly all genes, with no recurrent enriched blood-cell category. Most genes have low tissue specificity, which is consistent with broadly expressed housekeeping-like RNA-processing machinery rather than a bone- or ovary-exclusive program. The few tissue-enhanced signals include bone marrow-associated ALYREF and RBM39 and lymphoid-associated POLR2A, while several cell-type-enhanced signals include oocytes, erythrocyte progenitors, and other differentiated cell types. These scattered signals do not establish a blood contamination explanation. The shared bone and ovary module is therefore more likely to reflect a conserved requirement for nuclear RNA maturation, although sample cellular composition and proliferative state could influence its abundance. Protein detection in ovary for most assessed proteins is compatible with genuine ovarian expression, while the absence of matching bone tissue data limits direct tissue-level confirmation.

**GO/KEGG enrichment**: 39 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile | 6.18e-11 | ACIN1, DDX5, DHX9, EFTUD2, HNRNPH1, HNRNPL, HNRNPR, PRMT5, PRPF4, RBM10, RBM39, SF3B3, SNRNP200, SNRNP40, SNW1, SRSF7, XAB2 |
| GO:BP mRNA splicing, via spliceosome | 6.18e-11 | ACIN1, DDX5, DHX9, EFTUD2, HNRNPH1, HNRNPL, HNRNPR, PRMT5, PRPF4, RBM10, RBM39, SF3B3, SNRNP200, SNRNP40, SNW1, SRSF7, XAB2 |
| GO:BP RNA splicing, via transesterification reactions | 7.31e-11 | ACIN1, DDX5, DHX9, EFTUD2, HNRNPH1, HNRNPL, HNRNPR, PRMT5, PRPF4, RBM10, RBM39, SF3B3, SNRNP200, SNRNP40, SNW1, SRSF7, XAB2 |
| GO:BP mRNA processing | 8.35e-10 | ACIN1, ADAR, DDX5, DHX9, EFTUD2, FIP1L1, HNRNPH1, HNRNPL, HNRNPR, PRMT5, PRPF4, RBM10, RBM39, SF3B3, SNRNP200, SNRNP40, SNW1, SRSF7, XAB2 |
| GO:BP RNA splicing | 1.24e-08 | ACIN1, DDX5, DHX9, EFTUD2, HNRNPH1, HNRNPL, HNRNPR, PRMT5, PRPF4, RBM10, RBM39, SF3B3, SNRNP200, SNRNP40, SNW1, SRSF7, XAB2 |
| GO:BP mRNA metabolic process | 1.04e-07 | ACIN1, ADAR, DDX5, DHX9, EFTUD2, FIP1L1, HNRNPH1, HNRNPL, HNRNPR, PRMT5, PRPF4, RBM10, RBM39, SF3B3, SNRNP200, SNRNP40, SNW1, SRSF7, XAB2 |
| KEGG Spliceosome - Homo sapiens (human) | 1.09e-07 | ACIN1, ALYREF, CHERP, DDX5, EFTUD2, PRPF4, SF3B3, SNRNP200, SNRNP40, SNW1, SRSF7, XAB2 |
| GO:BP RNA processing | 1.17e-06 | ACIN1, ADAR, CHERP, DDX5, DHX9, EFTUD2, FIP1L1, HNRNPH1, HNRNPL, HNRNPR, PRMT5, PRPF4, RBM10, RBM39, SF3B3, SNRNP200, SNRNP40, SNW1, SRSF7, XAB2 |
| GO:CC nucleoplasm | 2.42e-06 | ACIN1, ADAR, ALYREF, CHERP, DDX5, DHX9, EFTUD2, FIP1L1, HNRNPH1, HNRNPL, HNRNPR, MRPL2, PAK2, POLR2A, PPP6R3, PRMT5, PRPF4, RBM10, RBM39, SF3B3, SMARCE1, SNRNP200, SNRNP40, SNW1, SRSF7, TP53BP1, UBTF, XAB2, YLPM1, ZMYND8 |
| GO:BP RNA biosynthetic process | 2.91e-06 | ACIN1, ADAR, ADNP, CHERP, DDX5, DHX9, EFTUD2, FIP1L1, HNRNPH1, HNRNPL, HNRNPR, POLR2A, PRMT5, PRPF4, RBM10, RBM39, SF3B3, SMARCE1, SNRNP200, SNRNP40, SNW1, SRSF7, TP53BP1, UBTF, XAB2, ZMYND8 |
| GO:BP regulation of mRNA processing | 4.69e-06 | ACIN1, DDX5, DHX9, HNRNPL, PRMT5, RBM10, RBM39, SNW1, SRSF7 |
| GO:CC catalytic step 2 spliceosome | 6.14e-06 | DDX5, EFTUD2, HNRNPH1, HNRNPR, SF3B3, SNRNP200, SNRNP40, SNW1, XAB2 |
| GO:BP nucleic acid biosynthetic process | 6.64e-06 | ACIN1, ADAR, ADNP, CHERP, DDX5, DHX9, EFTUD2, FIP1L1, HNRNPH1, HNRNPL, HNRNPR, POLR2A, PRMT5, PRPF4, RBM10, RBM39, SF3B3, SMARCE1, SNRNP200, SNRNP40, SNW1, SRSF7, TP53BP1, UBTF, XAB2, ZMYND8 |
| GO:CC spliceosomal complex | 6.98e-06 | ADAR, DDX5, EFTUD2, HNRNPH1, HNRNPR, PRPF4, SF3B3, SNRNP200, SNRNP40, SNW1, XAB2 |
| GO:BP regulation of RNA splicing | 7.45e-06 | ACIN1, DDX5, HNRNPH1, HNRNPL, PRMT5, RBM10, RBM39, SF3B3, SNW1, SRSF7 |

### STRING and hu.MAP

STRING independently supports the same interpretation. The supplementary pathway results repeatedly identify mRNA processing, RNA splicing, RNA metabolism, the spliceosome, the catalytic step two spliceosome, and the nucleoplasm (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 9.06e-16) through (STRING COMPARTMENTS Catalytic step 2 spliceosome; within-query FDR = 5.19e-08). These STRING results are supplementary rather than globally corrected enrichment evidence, but the individual high-confidence relationships provide useful structural support. Particularly coherent edges connect DDX5, DHX9, HNRNPH1, HNRNPL, HNRNPR, ALYREF, RBM39, and SRSF7, while another dense group connects EFTUD2, PRPF4, SF3B3, SNRNP200, SNRNP40, SNW1, and XAB2. hu.MAP independently places module members in spliceosomal, catalytic-step, U five, U two, and RNA-binding complexes (hu.MAP huMAP3_08980.1) through (hu.MAP huMAP3_09621.1). The repeated recovery of the EFTUD2, SNRNP200, SNRNP40, SNW1, and XAB2 group across hu.MAP complexes is especially consistent with a shared spliceosome-associated assembly. Known STRING and hu.MAP relationships show that much of the module recapitulates established molecular machinery rather than an unexplained interaction network. The co-abundance edges therefore likely capture coordinated abundance of physically and functionally connected complexes, with additional links among regulatory RNA-binding and transcription-coupled factors.

**STRING interactions (score >= 0.7)**: 55 of 528 gene pairs: ACIN1–ALYREF (0.92); ADAR–DHX9 (0.922); ALYREF–DDX5 (0.929); ALYREF–DHX9 (0.953); ALYREF–EFTUD2 (0.89); ALYREF–HNRNPH1 (0.914); ALYREF–HNRNPL (0.844); ALYREF–HNRNPR (0.851); ALYREF–RBM39 (0.906); ALYREF–SRSF7 (0.958); CHERP–RBM39 (0.744); DDX5–DHX9 (0.996); DDX5–HNRNPH1 (0.96); DDX5–HNRNPR (0.844); DDX5–POLR2A (0.718); DDX5–RBM39 (0.971); DDX5–SNW1 (0.76); DHX9–HNRNPH1 (0.878); DHX9–HNRNPL (0.901); DHX9–HNRNPR (0.909); DHX9–POLR2A (0.781); DHX9–RBM39 (0.909); DHX9–SF3B3 (0.73); DHX9–SNRNP200 (0.784); DHX9–SRSF7 (0.789); EFTUD2–MRPL2 (0.811); EFTUD2–PRPF4 (0.999); EFTUD2–SF3B3 (0.999); EFTUD2–SNRNP200 (0.999); EFTUD2–SNRNP40 (0.999); EFTUD2–SNW1 (0.999); EFTUD2–SRSF7 (0.751); EFTUD2–XAB2 (0.999); HNRNPH1–HNRNPL (0.982); HNRNPH1–HNRNPR (0.947); HNRNPH1–SRSF7 (0.922); HNRNPL–HNRNPR (0.961); HNRNPL–RBM39 (0.75); HNRNPL–SRSF7 (0.926); HNRNPR–SRSF7 (0.833); POLR2A–XAB2 (0.761); PRMT5–SMARCE1 (0.706); PRPF4–SF3B3 (0.995); PRPF4–SNRNP200 (0.999); PRPF4–SNRNP40 (0.986); SF3B3–SNRNP200 (0.999); SF3B3–SNRNP40 (0.852); SF3B3–SNW1 (0.99); SF3B3–XAB2 (0.977); SNRNP200–SNRNP40 (0.999); SNRNP200–SNW1 (0.998); SNRNP200–XAB2 (0.997); SNRNP40–SNW1 (0.994); SNRNP40–XAB2 (0.994); SNW1–XAB2 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM mRNA Splicing - Major Pathway (FDR = 9.06e-16, 19 genes); RCTM Processing of Capped Intron-Containing Pre-mRNA (FDR = 1.61e-14, 20 genes); Keyword mRNA processing (FDR = 2.17e-12, 18 genes); Process mRNA processing (FDR = 6.57e-12, 20 genes); Keyword mRNA splicing (FDR = 1.25e-11, 16 genes); RCTM Metabolism of RNA (FDR = 4.45e-11, 22 genes); Process mRNA splicing, via spliceosome (FDR = 2.99e-10, 15 genes); Process RNA splicing (FDR = 2.99e-10, 17 genes); Process RNA processing (FDR = 5.72e-09, 21 genes); KEGG Spliceosome (FDR = 6.45e-09, 12 genes); COMPARTMENTS Nucleoplasm (FDR = 1.72e-08, 20 genes); COMPARTMENTS Spliceosomal complex (FDR = 1.72e-08, 12 genes); Keyword Spliceosome (FDR = 2.43e-08, 11 genes); Process RNA metabolic process (FDR = 4.48e-08, 23 genes); COMPARTMENTS Catalytic step 2 spliceosome (FDR = 5.19e-08, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (PRMT5, PRPF4, SNRNP200, EFTUD2, SF3B3, SNRNP40; 6/97); huMAP3_08501.1 (SNRNP200, SNW1, EFTUD2, SNRNP40, XAB2; 5/47); huMAP3_09504.1 (SNRNP200, SNW1, EFTUD2, SNRNP40, XAB2; 5/51); huMAP3_09945.1 (SNRNP200, SNW1, EFTUD2, SNRNP40, XAB2; 5/61); huMAP3_06726.1 (SNRNP200, SNW1, SNRNP40, XAB2; 4/37); huMAP3_00960.1 (SNRNP200, EFTUD2, SNRNP40; 3/8); huMAP3_07622.1 (SNRNP200, EFTUD2, SNRNP40; 3/9); huMAP3_10625.1 (HNRNPR, HNRNPL, ADAR; 3/57); huMAP3_11073.1 (SRSF7, FIP1L1, ACIN1; 3/67); huMAP3_09943.1 (SRSF7, ALYREF, ACIN1; 3/78); huMAP3_06511.1 (PRMT5, PRPF4, SF3B3; 3/79); huMAP3_07225.1 (HNRNPR, HNRNPL; 2/7); huMAP3_00424.1 (EFTUD2, SNRNP40; 2/8); huMAP3_08220.1 (RBM10, CHERP; 2/9); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09594.1 (RBM10, CHERP; 2/11); huMAP3_08486.1 (SRSF7, FIP1L1; 2/11); huMAP3_09654.1 (HNRNPR, HNRNPL; 2/13); huMAP3_06429.1 (SNW1, XAB2; 2/18); huMAP3_09587.1 (SRSF7, FIP1L1; 2/21); huMAP3_07581.1 (HNRNPR, HNRNPL; 2/21); huMAP3_08703.1 (SNW1, XAB2; 2/21); huMAP3_06097.1 (SRSF7, ACIN1; 2/22); huMAP3_08467.1 (RBM39, SRSF7; 2/22); huMAP3_10359.1 (RBM10, CHERP; 2/27); huMAP3_10659.1 (HNRNPR, HNRNPL; 2/28); huMAP3_14523.1 (HNRNPH1, YLPM1; 2/33); huMAP3_10564.1 (SRSF7, ACIN1; 2/37); huMAP3_09621.1 (SRSF7, ACIN1; 2/56)

### Novelty

The module should not be described as a newly discovered spliceosome or as proof of a novel protein complex. Its central biology is already well established by the globally corrected annotations, the STRING relationships, and the hu.MAP complexes. The potentially novel aspect is the co-abundance organization of this particular set across bone and ovary, especially the joint behavior of core spliceosomal, RNA-export, RNA-editing, chromatin, and tissue-associated factors. However, the fact that some genes or edges lack STRING or hu.MAP support does not establish novelty: absence can reflect incomplete databases, context dependence, technical coverage, or indirect co-regulation. A defensible conclusion is that this is a biologically credible conserved tissue-pair module with a potentially novel cross-tissue co-abundance pattern, but novelty of the molecular mechanism requires validation in independent cohorts, cell-type-resolved data, perturbation experiments, and direct interaction or activity assays.

**Hypothesis.** Mechanistic hypothesis: in bone and ovary, cellular states that require substantial or carefully regulated gene expression increase coordinated production of a nuclear RNA-maturation apparatus. Core spliceosomal components such as SNRNP200, SNRNP40, EFTUD2, PRPF4, SF3B3, SNW1, and XAB2 could form the structural and catalytic backbone, while DDX5, DHX9, hnRNP proteins, SRSF7, RBM10, RBM39, ADAR, ALYREF, and FIP1L1 tune transcript selection, RNA processing, RNA editing, export, and three-prime end formation. This coordinated machinery may help bone and ovarian cells adapt alternative splicing and transcript maturation to differentiation, developmental, hormonal, or DNA-damage-associated demands. The bone and ovary sharing may therefore reflect a conserved transcriptional and post-transcriptional state rather than a tissue-specific pathway. This remains a hypothesis: the co-abundance data support coordination, but do not establish directionality, cell autonomy, physical assembly of every module member, or a specific bone-ovary signaling mechanism.

### Important genes

#### ACIN1

- **Related proteins** (co-abundance neighbors): HNRNPR (0.95), DHX9 (0.92), FIP1L1 (0.88), ALYREF (0.86), SNRNP40 (0.86), XAB2 (0.86), ADAR (0.86), MRPL2 (0.85), RBM10 (0.84), HNRNPL (0.82), SRSF7 (0.81), UBTF (0.80); STRING partners: ALYREF (0.92)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_11073.1, huMAP3_09943.1, huMAP3_06097.1, huMAP3_10564.1, huMAP3_09621.1
- **Function (MyGene.info)**: apoptotic chromatin condensation inducer 1. Apoptosis is defined by several morphologic nuclear changes, including chromatin condensation and nuclear fragmentation. This gene encodes a nuclear protein that induces apoptotic chromatin condensation after activation by caspase-3, without inducing DNA fragmentation. This protein has also been shown to be a component of a splicing-dependent multiprotein exon junction complex (EJC) that is deposi…
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); adolescent idiopathic scoliosis (0.090); hepatocellular carcinoma (0.076); acute lymphoblastic leukemia (0.074); pancreatic neoplasm (0.045)
- **Europe PMC papers**: 894
- **Why important**: ACIN1 is the strongest network connector in the supplied module and links the spliceosome-associated group with RNA-binding and processing factors. It appears across nearly all primary splicing and RNA-processing annotations, is located in the nucleoplasm, and has established roles in splicing-dependent exon-junction biology and apoptotic chromatin condensation. Its extensive literature and disease associations make it a useful integrative marker of the module rather than merely a peripheral spliceosomal component.
- **Conclusion**: Established evidence supports ACIN1 as a central nuclear RNA-processing and splicing-associated protein with a bridge to apoptosis-related nuclear remodeling. The module data support its use as a network-level indicator of coordinated RNA maturation. A bone- or ovary-specific regulatory role is a hypothesis, not established by this module.

#### DDX5

- **Related proteins** (co-abundance neighbors): RBM10 (0.89), FIP1L1 (0.80); STRING partners: ALYREF (0.929), DHX9 (0.996), HNRNPH1 (0.96), HNRNPR (0.844), POLR2A (0.718), RBM39 (0.971), SNW1 (0.76)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 is a well-studied RNA helicase and transcriptional coregulator with strong STRING connectivity to DHX9, hnRNP proteins, ALYREF, RBM39, POLR2A, and SNW1. It is present in the primary splicing, mRNA-processing, RNA-metabolism, nuclear-speck, and spliceosomal annotations (GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 6.18e-11), (GO:BP mRNA processing; q_global = 8.35e-10), (KEGG Spliceosome - Homo sapiens (human); q_global = 1.09e-07), (GO:CC nuclear speck; q_global = 1.99e-05). Its substantial literature volume and disease associations make it a biologically informative regulatory hub even though its module-network degree is not maximal.
- **Conclusion**: Established evidence supports DDX5 as an RNA-structure remodeler and regulator of splicing and transcription. Its position connecting RNA helicases, RNA-binding proteins, and transcription machinery supports a coordinating role in this module. Whether it drives the conserved bone-ovary co-abundance pattern remains untested.

#### SNRNP40

- **Related proteins** (co-abundance neighbors): FIP1L1 (0.94), TP53BP1 (0.89), EIF2B4 (0.87), ACIN1 (0.86), PRPF4 (0.86), PPP6R3 (0.85), PRMT5 (0.82), DHX9 (0.82), HNRNPH1 (0.81); STRING partners: EFTUD2 (0.999), PRPF4 (0.986), SF3B3 (0.852), SNRNP200 (0.999), SNW1 (0.994), XAB2 (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_06726.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_00424.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 40. This gene encodes a component of the U5 small nuclear ribonucleoprotein (snRNP) particle. The U5 snRNP is part of the spliceosome, a multiprotein complex that catalyzes the removal of introns from pre-messenger RNAs. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.530); dengue disease (0.377); X-linked lymphoproliferative syndrome (0.058); autoimmune lymphoproliferative syndrome (0.055); Familial hemophagocytic lymphohistiocytosis (0.053)
- **Europe PMC papers**: 235
- **Why important**: SNRNP40 is a core U5 small nuclear ribonucleoprotein component and one of the most connected module members. It has strong STRING relationships with EFTUD2, PRPF4, SF3B3, SNRNP200, SNW1, and XAB2, and it recurs across numerous hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1) through (hu.MAP huMAP3_07622.1), (hu.MAP huMAP3_00424.1). It is represented in the primary spliceosome, catalytic-step, U2-type complex, and spliceosomal snRNP annotations (KEGG Spliceosome - Homo sapiens (human); q_global = 1.09e-07), (GO:CC catalytic step 2 spliceosome; q_global = 6.14e-06), (GO:CC U2-type spliceosomal complex; q_global = 0.00245), (GO:CC spliceosomal snRNP complex; q_global = 0.0311).
- **Conclusion**: Established evidence identifies SNRNP40 as a structural component of the spliceosomal machinery. Its network and complex membership make it a strong anchor gene for the module and support the interpretation that the co-abundance signal includes coordinated core spliceosome abundance. The data do not show that SNRNP40 is a tissue-specific driver.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): CHERP (0.85), SNRNP200 (0.84), FIP1L1 (0.82), SF3B3 (0.82), RBM10 (0.80); STRING partners: ALYREF (0.89), MRPL2 (0.811), PRPF4 (0.999), SF3B3 (0.999), SNRNP200 (0.999), SNRNP40 (0.999), SNW1 (0.999), SRSF7 (0.751), XAB2 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_00424.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 is a spliceosomal GTPase associated with tri-snRNP assembly and spliceosome conformational change. It connects the module's central spliceosomal cluster and has very strong STRING relationships with PRPF4, SF3B3, SNRNP200, SNRNP40, SNW1, and XAB2. It is repeatedly recovered in hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1) through (hu.MAP huMAP3_07622.1), (hu.MAP huMAP3_00424.1) and in the primary spliceosome and catalytic-step annotations (KEGG Spliceosome - Homo sapiens (human); q_global = 1.09e-07), (GO:CC catalytic step 2 spliceosome; q_global = 6.14e-06), (GO:CC U2-type spliceosomal complex; q_global = 0.00245), (GO:CC spliceosomal snRNP complex; q_global = 0.0311). Its disease associations include mandibulofacial dysostosis with microcephaly, providing evidence that perturbing core splicing can have developmental consequences.
- **Conclusion**: Established evidence supports EFTUD2 as a core structural and conformational component of the spliceosome. Its position at the center of known complex relationships makes it an important mechanistic anchor. The shared bone-ovary module may reflect demand for EFTUD2-dependent spliceosome assembly, but that tissue interpretation requires direct testing.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.84), TP53BP1 (0.83), POLR2A (0.81); STRING partners: DHX9 (0.784), EFTUD2 (0.999), PRPF4 (0.999), SF3B3 (0.999), SNRNP40 (0.999), SNW1 (0.998), XAB2 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_06726.1, huMAP3_00960.1, huMAP3_07622.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is a U5 small nuclear ribonucleoprotein RNA helicase and a recurrent member of the central hu.MAP spliceosomal complexes (hu.MAP huMAP3_08980.1) through (hu.MAP huMAP3_07622.1). It shows strong STRING relationships with EFTUD2, PRPF4, SF3B3, SNRNP40, SNW1, XAB2, and DHX9, linking core spliceosome structure to RNA helicase activity. It is present across the primary splicing, catalytic-step, U2-type complex, and spliceosomal snRNP annotations (GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile; q_global = 6.18e-11), (KEGG Spliceosome - Homo sapiens (human); q_global = 1.09e-07), (GO:CC catalytic step 2 spliceosome; q_global = 6.14e-06), (GO:CC U2-type spliceosomal complex; q_global = 0.00245), (GO:CC spliceosomal snRNP complex; q_global = 0.0311). Its disease associations with inherited retinal degeneration illustrate the physiological importance of accurate spliceosome function.
- **Conclusion**: Established evidence supports SNRNP200 as a core U5 spliceosomal helicase required for spliceosome function. Its repeated complex membership and dense connections make it a strong representative of the module's conserved molecular core. A specific role in bone or ovarian differentiation is plausible but remains a hypothesis.

## Module 4

**Tissue pair**: bone and ovary  
**Genes (35)**: ACO2, ACOT9, ATP5PB, ATAD3A, ATP5F1A, ATP5F1B, ATP5MK, BCL2L13, CANX, ECE1, ITGAV, LYRM4, MAIP1, MARCHF5, IMMT, NME3, NDUFAF4, NCSTN, DDOST, RAB10, RAB18, RAB21, RAB8A, SEC61A1, SEC22B, SCARB2, SCRIB, SOD2, HM13, SPTLC1, STX7, AARS2, SYNJ2BP, VAPB, VDAC2

### Function

The module is best interpreted as a conserved organelle-membrane and mitochondrial energy-maintenance program, coupled to endoplasmic-reticulum protein handling and vesicle trafficking. The primary evidence is the strong enrichment of organelle membranes (GO:CC organelle membrane; q_global = 1.5e-07), mitochondrial membranes and envelopes (GO:CC mitochondrial membrane; q_global = 0.000328) (GO:CC mitochondrial envelope; q_global = 0.000818), ER membranes and ER subcompartments (GO:CC endoplasmic reticulum membrane; q_global = 0.00433) (GO:CC endoplasmic reticulum subcompartment; q_global = 0.00433) (GO:CC nuclear outer membrane-endoplasmic reticulum membrane network; q_global = 0.00541), the mitochondrial ATP synthase complex (GO:CC proton-transporting ATP synthase complex; q_global = 0.00664), membrane-protein complexes (GO:CC membrane protein complex; q_global = 0.0308), and vesicle membranes (GO:CC cytoplasmic vesicle membrane; q_global = 0.0308) (GO:CC vesicle membrane; q_global = 0.0323). Mitochondrial localization and organization are also supported by (GO:CC mitochondrion; q_global = 0.0237) (GO:BP mitochondrion organization; q_global = 0.0276). The ion-channel and passive-transporter annotations (4 globally significant GO/KEGG terms, q_global 0.00147–0.0076; see the table) should be interpreted cautiously because they include components of membrane complexes rather than demonstrating a single stand-alone channel pathway. Overall, the genes suggest coordinated oxidative phosphorylation, mitochondrial architecture and quality control, ER protein translocation and folding, and intracellular membrane transport. The broad membrane annotation (GO:CC membrane; q_global = 0.0399) is consistent with this integrated organelle maintenance interpretation rather than defining the function by itself.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module: the HPA summary identifies only a small secreted component, while the genes are predominantly intracellular membrane, mitochondrial, ER, lysosomal, or vesicle-associated proteins. Most genes have low tissue specificity and low immune-cell specificity, which is compatible with a broadly expressed housekeeping-like program. Nevertheless, many genes show cell-type-enhanced patterns, including neutrophils, epithelial populations, trophoblasts, parietal cells, oocytes, platelets, and muscle-related tissues. Several genes also have blood-cell-enriched or immune-cell-enhanced HPA annotations, especially STX7, SCARB2, ECE1, and SOD2. Therefore, blood or shared cell types could contribute to the cross-tissue signal, but the overall HPA pattern does not support a predominantly blood-derived module. Protein detection in ovary is present for many module members, whereas the supplied bone HPA tissue comparison has no matching tissue result, so tissue-level protein confirmation is asymmetric.

**GO/KEGG enrichment**: 19 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC organelle membrane | 1.5e-07 | ATAD3A, ATP5F1A, ATP5F1B, ATP5MK, ATP5PB, BCL2L13, CANX, DDOST, ECE1, HM13, IMMT, ITGAV, MAIP1, MARCHF5, NCSTN, NDUFAF4, NME3, RAB10, RAB18, RAB21, RAB8A, SCARB2, SEC22B, SEC61A1, SPTLC1, STX7, SYNJ2BP, VAPB, VDAC2 |
| GO:CC mitochondrial membrane | 0.000328 | ATAD3A, ATP5F1A, ATP5F1B, ATP5MK, ATP5PB, BCL2L13, CANX, IMMT, MAIP1, MARCHF5, NDUFAF4, NME3, SYNJ2BP, VDAC2 |
| GO:CC mitochondrial envelope | 0.000818 | ATAD3A, ATP5F1A, ATP5F1B, ATP5MK, ATP5PB, BCL2L13, CANX, IMMT, MAIP1, MARCHF5, NDUFAF4, NME3, SYNJ2BP, VDAC2 |
| GO:CC bounding membrane of organelle | 0.000996 | CANX, DDOST, ECE1, IMMT, ITGAV, MARCHF5, NCSTN, NME3, RAB10, RAB18, RAB21, RAB8A, SCARB2, SEC22B, SEC61A1, STX7, SYNJ2BP, VDAC2 |
| GO:MF monoatomic ion channel activity | 0.00147 | ATP5F1A, ATP5F1B, ATP5PB, ITGAV, SEC61A1, VDAC2 |
| GO:MF monoatomic cation channel activity | 0.00394 | ATP5F1A, ATP5F1B, ATP5PB, ITGAV, SEC61A1 |
| GO:CC endoplasmic reticulum membrane | 0.00433 | CANX, DDOST, HM13, MARCHF5, NCSTN, RAB10, RAB18, RAB21, SCARB2, SEC22B, SEC61A1, SPTLC1, VAPB |
| GO:CC endoplasmic reticulum subcompartment | 0.00433 | CANX, DDOST, HM13, MARCHF5, NCSTN, RAB10, RAB18, RAB21, SCARB2, SEC22B, SEC61A1, SPTLC1, VAPB |
| GO:CC nuclear outer membrane-endoplasmic reticulum membrane network | 0.00541 | CANX, DDOST, HM13, MARCHF5, NCSTN, RAB10, RAB18, RAB21, SCARB2, SEC22B, SEC61A1, SPTLC1, VAPB |
| GO:CC proton-transporting ATP synthase complex | 0.00664 | ATP5F1A, ATP5F1B, ATP5MK, ATP5PB |
| GO:MF channel activity | 0.0076 | ATP5F1A, ATP5F1B, ATP5PB, ITGAV, SEC61A1, VDAC2 |
| GO:MF passive transmembrane transporter activity | 0.0076 | ATP5F1A, ATP5F1B, ATP5PB, ITGAV, SEC61A1, VDAC2 |
| GO:CC organelle subcompartment | 0.0119 | CANX, DDOST, HM13, MARCHF5, NCSTN, RAB10, RAB18, RAB21, RAB8A, SCARB2, SEC22B, SEC61A1, SPTLC1, VAPB |
| GO:CC mitochondrion | 0.0237 | AARS2, ACO2, ACOT9, ATAD3A, ATP5F1A, ATP5F1B, ATP5MK, ATP5PB, BCL2L13, CANX, IMMT, LYRM4, MAIP1, MARCHF5, NDUFAF4, NME3, SOD2, SYNJ2BP, VDAC2 |
| GO:BP mitochondrion organization | 0.0276 | ATAD3A, BCL2L13, IMMT, MAIP1, MARCHF5, NDUFAF4, NME3, SOD2, VDAC2 |

### STRING and hu.MAP

STRING provides established relationships in several coherent parts of the module. The ATP synthase group is linked through ATP5F1A, ATP5F1B, and ATP5PB, with additional links to IMMT, VDAC2, and ACO2. The ER machinery is supported by CANX, DDOST, SEC61A1, and SEC22B, including strong links among DDOST, SEC61A1, and CANX. SEC22B is linked to STX7, and RAB10 is linked to RAB8A. ITGAV is linked to SCARB2, while ACO2 is linked to SOD2 and LYRM4. These relationships indicate that the module contains known molecular subsystems rather than being a collection of unrelated genes. hu.MAP supports this interpretation through repeated ATP synthase complexes containing ATP5F1A, ATP5F1B, ATP5PB, and ATP5MK; complexes connecting ATP synthase components with ATAD3A; ER or membrane assemblies involving SEC61A1, HM13, and VDAC2; Rab-trafficking assemblies involving RAB8A and RAB10; and assemblies containing MAIP1 with RAB18 or VAPB with VDAC2. However, many module edges are not directly represented by high-confidence STRING links, and hu.MAP complexes often contain only a subset of the module. Thus, the co-abundance network appears to join several related organelle systems, rather than reproduce one single canonical protein complex.

**STRING interactions (score >= 0.7)**: 21 of 595 gene pairs: ACO2–ATP5F1A (0.884); ACO2–ATP5F1B (0.874); ACO2–LYRM4 (0.842); ACO2–SOD2 (0.968); ATP5F1A–ATP5F1B (0.999); ATP5F1A–ATP5PB (0.999); ATP5F1A–IMMT (0.809); ATP5F1A–SEC61A1 (0.886); ATP5F1A–VDAC2 (0.715); ATP5F1B–ATP5PB (0.999); ATP5F1B–IMMT (0.745); ATP5F1B–VDAC2 (0.758); CANX–DDOST (0.886); CANX–NCSTN (0.754); CANX–SEC22B (0.703); CANX–SEC61A1 (0.914); DDOST–SEC61A1 (0.998); IMMT–VDAC2 (0.708); ITGAV–SCARB2 (0.807); RAB10–RAB8A (0.831); SEC22B–STX7 (0.962)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Organelle membrane (FDR = 1.44e-08, 25 genes); Component Organelle membrane (FDR = 1.6e-07, 27 genes); Keyword Membrane (FDR = 7.98e-07, 27 genes); COMPARTMENTS Membrane (FDR = 3.64e-06, 27 genes); Keyword Transmembrane (FDR = 4.87e-06, 18 genes); Keyword Transmembrane helix (FDR = 1.85e-05, 17 genes); Component Integral component of membrane (FDR = 0.00021, 19 genes); Component Endoplasmic reticulum membrane (FDR = 0.0003, 13 genes); COMPARTMENTS Organelle subcompartment (FDR = 0.00031, 12 genes); COMPARTMENTS Bounding membrane of organelle (FDR = 0.00031, 15 genes); COMPARTMENTS Endoplasmic reticulum subcompartment (FDR = 0.00031, 10 genes); COMPARTMENTS Endoplasmic reticulum membrane (FDR = 0.00033, 10 genes); COMPARTMENTS Membrane protein complex (FDR = 0.00033, 14 genes); Component Membrane protein complex (FDR = 0.00045, 13 genes); Keyword Mitochondrion (FDR = 0.00046, 16 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09307.1 (ATP5F1B, ATP5PB, ATP5F1A, ATP5MK; 4/35); huMAP3_11095.1 (ATP5F1B, ATP5PB, ATP5F1A, ATP5MK; 4/45); huMAP3_08750.1 (ATP5F1B, ATP5F1A, ATP5MK; 3/12); huMAP3_10473.1 (ATP5F1A, ATP5MK, ATAD3A; 3/24); huMAP3_06247.1 (ATP5PB, SEC61A1, HM13; 3/65); huMAP3_09592.1 (VDAC2, SEC61A1, HM13; 3/95); huMAP3_05462.1 (MAIP1, RAB18; 2/3); huMAP3_00261.1 (ATP5F1A, ATP5MK; 2/5); huMAP3_02620.1 (ATP5MK, ATAD3A; 2/6); huMAP3_10008.1 (MAIP1, RAB18; 2/7); huMAP3_10607.1 (ATP5MK, ATAD3A; 2/9); huMAP3_07462.1 (ATP5F1A, ATP5MK; 2/9); huMAP3_07302.1 (RAB8A, RAB10; 2/13); huMAP3_08716.1 (ATP5F1B, ATP5PB; 2/15); huMAP3_06607.1 (RAB8A, RAB10; 2/16); huMAP3_07476.1 (ATP5F1B, ATP5PB; 2/18); huMAP3_01895.1 (RAB8A, RAB10; 2/19); huMAP3_09775.1 (ATP5F1B, ATP5PB; 2/21); huMAP3_06994.1 (RAB8A, RAB10; 2/24); huMAP3_05784.1 (SPTLC1, SEC61A1; 2/27); huMAP3_08941.1 (RAB8A, RAB10; 2/28); huMAP3_09217.1 (RAB8A, RAB10; 2/29); huMAP3_11094.1 (RAB8A, RAB10; 2/43); huMAP3_11860.1 (RAB8A, RAB10; 2/44); huMAP3_10725.1 (VAPB, VDAC2; 2/59)

### Novelty

The module should not be described as a newly discovered molecular complex. Many of its components, including ATP synthase subunits, SEC61A1, CANX, DDOST, Rab proteins, ACO2, SOD2, and VDAC2, have established functions and known relationships. The apparent novelty is instead at the systems level: a conserved bone-ovary co-abundance pattern joining mitochondrial energy metabolism, mitochondrial membrane organization, ER proteostasis, and vesicle trafficking. The supplied evidence does not establish that this cross-tissue module has been reported previously, and absence of an exact match in STRING or hu.MAP would not prove novelty. A defensible conclusion is that this is a potentially novel tissue-pair co-abundance association built from largely familiar biological subsystems, requiring replication, cell-composition adjustment, and experimental validation before being called a novel mechanism.

**Hypothesis.** Hypothesis: the shared bone-ovary module reflects coordinated demand for mitochondrial energy production and organelle remodeling in metabolically active or differentiating cells. Mitochondrial ATP synthase components, ACO2, SOD2, ATAD3A, IMMT, and related factors could maintain respiratory capacity, cristae organization, metabolite flow, and oxidative-stress control. In parallel, SEC61A1, CANX, DDOST, SEC22B, VAPB, Rab proteins, STX7, and SCARB2 could support synthesis, folding, sorting, recycling, and degradation of membrane and secretory cargo. ITGAV and RAB21 may connect organelle state to adhesion and trafficking. This may represent a shared cellular state in bone and ovary, but it could also partly reflect common cell types or variable blood-cell content. The hypothesis can be tested by single-cell or spatial deconvolution, independent tissue cohorts, and perturbation of mitochondrial or ER-trafficking components followed by measurement of co-abundance and cellular phenotypes.

### Important genes

#### SEC22B

- **Related proteins** (co-abundance neighbors): MARCHF5 (0.89), RAB21 (0.88), ATP5PB (0.83), SEC61A1 (0.83), CANX (0.83), ATP5F1A (0.82), VAPB (0.81), ACO2 (0.80), STX7 (0.80); STRING partners: CANX (0.703), STX7 (0.962)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC22 homolog B, vesicle trafficking protein. The protein encoded by this gene is a member of the SEC22 family of vesicle trafficking proteins. It seems to complex with SNARE and it is thought to play a role in the ER-Golgi protein trafficking. This protein has strong similarity to Mus musculus and Cricetulus griseus proteins.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: inflammatory bowel disease (0.285); luminal A breast carcinoma (0.271); colitis (0.238); enteritis (0.238); Crohn disease (0.233)
- **Europe PMC papers**: 1006
- **Why important**: SEC22B is the strongest network connector in the supplied module and links vesicle trafficking with ATP synthase-related, ER, and Rab-associated neighbors. It is annotated for ER-to-Golgi transport, retrograde transport, vesicle fusion, and autophagy. Its STRING relationship with STX7 and links with CANX and SEC61A1 support a real trafficking and membrane-fusion subsystem. It has substantial literature and disease-association coverage, while HPA indicates broad tissue expression with neutrophil enhancement.
- **Conclusion**: Established evidence supports SEC22B as a central vesicle-trafficking and ER-Golgi component that helps connect otherwise distinct module subsystems. It is a plausible organizational hub, but the supplied data do not prove that SEC22B drives the bone-ovary association. Hypothesis: variation in SEC22B-dependent cargo traffic may coordinate ER function with mitochondrial and lysosomal remodeling.

#### ATP5F1A

- **Related proteins** (co-abundance neighbors): ATP5F1B (0.93), ACO2 (0.83), SEC22B (0.82); STRING partners: ACO2 (0.884), ATP5F1B (0.999), ATP5PB (0.999), IMMT (0.809), SEC61A1 (0.886), VDAC2 (0.715)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_09307.1, huMAP3_11095.1, huMAP3_08750.1, huMAP3_10473.1, huMAP3_00261.1, huMAP3_07462.1
- **Function (MyGene.info)**: ATP synthase F1 subunit alpha. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, using an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic po…
- **Diseases (Open Targets)**: mitochondrial complex V (ATP synthase) deficiency, nuclear type 4A (0.655); mitochondrial proton-transporting ATP synthase complex deficiency (0.648); mitochondrial complex V (ATP synthase) deficiency, nuclear type 4B (0.532); hereditary disease (0.394); Mitochondrial encephalopathy (0.371)
- **Europe PMC papers**: 822
- **Why important**: ATP5F1A is a core mitochondrial ATP synthase subunit, occupies a central position among the module's mitochondrial and membrane-linked genes, and participates in the ATP synthase complexes supported by STRING and multiple hu.MAP assemblies. It is included in the globally significant mitochondrial membrane, ATP synthase, channel, and mitochondrial organization terms (6 globally significant GO/KEGG terms, q_global 0.000328–0.0276; see the table). Its disease associations include mitochondrial complex V deficiency, and its literature base is substantial.
- **Conclusion**: Established evidence identifies ATP5F1A as a strong marker of the module's oxidative-phosphorylation component. Its presence is more consistent with a genuine mitochondrial energy program than with a generic membrane artifact. Hypothesis: ATP synthase abundance may couple energetic state to ER and vesicle-trafficking capacity in the shared tissue state.

#### CANX

- **Related proteins** (co-abundance neighbors): DDOST (0.87), BCL2L13 (0.84), SEC22B (0.83), ACO2 (0.81), ATP5PB (0.80); STRING partners: DDOST (0.886), NCSTN (0.754), SEC22B (0.703), SEC61A1 (0.914)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is an ER-resident calcium-binding chaperone involved in folding and quality control of newly synthesized glycoproteins and ER associated degradation. It has a prominent position among the ER, mitochondrial-membrane, and vesicle-related neighbors and is linked by STRING to DDOST, SEC61A1, SEC22B, and NCSTN. It appears across many primary membrane and organelle terms (8 globally significant GO/KEGG terms, q_global 1.5e-07–0.0399; see the table) and has extensive literature and disease relevance.
- **Conclusion**: Established evidence supports CANX as a proteostasis bridge between ER protein handling and the broader organelle-membrane program. It strengthens the interpretation that the module includes functional ER quality control rather than only mitochondrial abundance. Hypothesis: altered ER folding load may be coordinated with mitochondrial stress management in bone and ovary.

#### RAB10

- **Related proteins** (co-abundance neighbors): RAB8A (0.88), RAB18 (0.86), ATP5PB (0.84); STRING partners: RAB8A (0.831)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_07302.1, huMAP3_06607.1, huMAP3_01895.1, huMAP3_06994.1, huMAP3_08941.1, huMAP3_09217.1, huMAP3_11094.1, huMAP3_11860.1
- **Function (MyGene.info)**: RAB10, member RAS oncogene family. RAB10 belongs to the RAS (see HRAS; MIM 190020) superfamily of small GTPases. RAB proteins localize to exocytic and endocytic compartments and regulate intracellular vesicle trafficking (Bao et al., 1998 [PubMed 9918381]).[supplied by OMIM, Mar 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.549); digestive system disorder (0.242); cervical carcinoma (0.215); lobular capilliary hemangioma (0.165); hepatocellular carcinoma (0.109)
- **Europe PMC papers**: 2856
- **Why important**: RAB10 is a membrane-trafficking GTPase involved in exocytosis, Golgi-to-plasma-membrane transport, endosomal transport, and antigen processing. It is connected in the module to RAB8A, RAB18, and ATP5PB, and it participates in repeated hu.MAP assemblies of Rab trafficking proteins. Its placement provides a mechanistic link between the module's vesicle-membrane enrichment and its organelle energy component. HPA shows broad tissue specificity with epithelial cell-type enhancement.
- **Conclusion**: Established evidence supports RAB10 as a trafficking component that helps explain the vesicular side of the module. Its network position is less dominant than the major ER and ATP synthase connectors, so it is best viewed as a pathway integrator rather than a proven master regulator. Hypothesis: RAB10-dependent recycling or exocytosis may be responsive to the mitochondrial energetic state.

#### ACO2

- **Related proteins** (co-abundance neighbors): DDOST (0.84), ATP5F1A (0.83), CANX (0.81), SEC22B (0.80); STRING partners: ATP5F1A (0.884), ATP5F1B (0.874), LYRM4 (0.842), SOD2 (0.968)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aconitase 2. The protein encoded by this gene belongs to the aconitase/IPM isomerase family. It is an enzyme that catalyzes the interconversion of citrate to isocitrate via cis-aconitate in the second step of the TCA cycle. This protein is encoded in the nucleus and functions in the mitochondrion. It was found to be one of the mitochondrial matrix proteins that are preferentially degraded by the serine proteas…
- **Diseases (Open Targets)**: infantile cerebellar-retinal degeneration (0.814); optic atrophy 9 (0.693); autosomal dominant optic atrophy, classic form (0.619); optic atrophy (0.601); mitochondrial disease (0.505)
- **Europe PMC papers**: 3559
- **Why important**: ACO2 catalyzes a central step of the mitochondrial TCA cycle and is linked by STRING to ATP5F1A, ATP5F1B, LYRM4, and SOD2. It connects energy metabolism with oxidative-stress control and iron-sulfur biology, while appearing in the mitochondrial term (GO:CC mitochondrion; q_global = 0.0237). It has strong disease associations involving mitochondrial dysfunction and a large literature base. Its tissue-enhanced HPA pattern includes muscle-related tissues, and protein detection is reported in ovary.
- **Conclusion**: Established evidence supports ACO2 as a metabolic anchor for the mitochondrial portion of the module. Its limited direct network connectivity does not diminish its biochemical importance, but it does argue against labeling it a topological hub. Hypothesis: TCA cycle flux may help couple respiratory output to membrane trafficking and organelle quality-control demands.

#### SOD2

- **Related proteins** (co-abundance neighbors): RAB18 (0.82); STRING partners: ACO2 (0.968)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: superoxide dismutase 2. This gene is a member of the iron/manganese superoxide dismutase family. It encodes a mitochondrial protein that forms a homotetramer and binds one manganese ion per subunit. This protein binds to the superoxide byproducts of oxidative phosphorylation and converts them to hydrogen peroxide and diatomic oxygen. Mutations in this gene have been associated with idiopathic cardiomyopathy (IDC), premat…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); diabetic retinopathy (0.379); malunion fracture (0.295); coronary artery disorder (0.267); prostate carcinoma (0.227)
- **Europe PMC papers**: 28293
- **Why important**: SOD2 detoxifies mitochondrial superoxide and is strongly linked to ACO2 in STRING. It contributes to the globally significant mitochondrial and mitochondrion-organization terms (GO:CC mitochondrion; q_global = 0.0237) (GO:BP mitochondrion organization; q_global = 0.0276), and its disease associations include mitochondrial, cardiovascular, neurodegenerative, and bone-related phenotypes. HPA reports enhancement in bone marrow and several myeloid cell types, including neutrophils.
- **Conclusion**: Established evidence supports SOD2 as an oxidative-stress component that complements the module's respiratory and mitochondrial organization signals. Its myeloid enrichment means that cell composition must be considered when interpreting the shared tissue pattern. Hypothesis: SOD2 may buffer respiratory stress generated during coordinated mitochondrial and vesicle activity, but the module does not establish causality.

## Module 5

**Tissue pair**: bone and ovary  
**Genes (13)**: AIMP2, EIF3F, PSMC6, PSMC4, PSMC2, PSMD13, CAD, RRM2, LARS1, CCT5, CCT3, CCT7, CCT8

### Function

The module is best interpreted as a protein proteostasis and assembly module composed of two strongly represented machinery groups. The CCT/TRiC chaperonin component, represented by CCT3, CCT5, CCT7, and CCT8, provides primary evidence for ATP-dependent protein folding, unfolded-protein binding, protein stabilization, and localization of RNA or proteins to the Cajal body (GO:CC chaperonin-containing T-complex; q_global = 1.38e-05), (GO:BP regulation of telomerase RNA localization to Cajal body; q_global = 1.38e-05), (GO:BP positive regulation of telomerase RNA localization to Cajal body; q_global = 1.38e-05), (10 globally significant GO/KEGG terms, q_global 4.89e-05–4.89e-05; see the table), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.0013), (GO:CC protein folding chaperone complex; q_global = 0.00399), (GO:MF protein folding chaperone; q_global = 0.00912), (GO:MF unfolded protein binding; q_global = 0.0258). The proteasome component, represented by PSMC2, PSMC4, PSMC6, and PSMD13, provides primary evidence for the proteasome regulatory particle, proteasome accessory complex, ATP-dependent proteasome activity, and proteasome-mediated protein catabolism (GO:CC proteasome regulatory particle; q_global = 4.89e-05), (GO:CC proteasome accessory complex; q_global = 4.89e-05), (GO:MF proteasome-activating activity; q_global = 0.000916), (KEGG Proteasome - Homo sapiens (human); q_global = 0.00238), (GO:CC proteasome regulatory particle, base subcomplex; q_global = 0.00272), (GO:CC proteasome complex; q_global = 0.00399), (GO:CC endopeptidase complex; q_global = 0.0128), (GO:CC peptidase complex; q_global = 0.0172). The broad intracellular protein-complex and protein-metabolism signals (GO:CC intracellular protein-containing complex; q_global = 1.15e-05), (GO:BP protein metabolic process; q_global = 0.00658) support a general protein quality-control interpretation. Telomerase-RNA and Cajal-body terms are statistically supported (14 globally significant GO/KEGG terms, q_global 1.38e-05–4.89e-05; see the table), but they should be interpreted as a functional association of the CCT-containing machinery rather than proof that the module directly regulates telomerase in bone or ovary. Fertilization, sperm–egg recognition, and cell-recognition terms are also supported (GO:BP binding of sperm to zona pellucida; q_global = 0.000118), (GO:BP sperm-egg recognition; q_global = 0.000228), (GO:BP cell-cell recognition; q_global = 0.000918), (GO:BP single fertilization; q_global = 0.005), (GO:BP cell recognition; q_global = 0.005), (GO:BP fertilization; q_global = 0.0199), but the shared chaperonin signal makes a general protein-folding or cellular-assembly explanation more compelling than a tissue-specific reproductive mechanism. The KEGG proteasome result (KEGG Proteasome - Homo sapiens (human); q_global = 0.00238) is concordant with the GO evidence. The module therefore most plausibly reflects coordinated protein folding, complex assembly, and selective protein turnover, with possible links to nuclear-body and telomere-associated processes.

**Cell composition.** This is not a plasma-protein or secreted-protein module: HPA identifies no secreted genes, and every module gene has low immune-cell specificity. Most genes have low tissue specificity, which is compatible with broadly expressed intracellular housekeeping or proteostasis machinery rather than a specialized bone or ovary product. HPA protein detection is present for most assessed genes in ovary, while bone lacks a matching HPA tissue result, so the ovary evidence supports detectability but does not establish ovary-specific function. Several genes show cell-type enhancement in reproductive or placental populations, including oocytes, spermatocytes, spermatids, and trophoblast populations. AIMP2 is tissue-enhanced in skeletal muscle, while RRM2 is tissue-enhanced in bone marrow and lymphoid tissue. These patterns do not indicate a blood-cell module, because blood-cell specificity is low throughout and no enriched blood-cell category is reported. The shared module could therefore reflect broadly expressed proteostasis machinery, shared proliferative or specialized reproductive cell states, or sample cellular composition rather than a bone–ovary-specific pathway.

**GO/KEGG enrichment**: 58 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC intracellular protein-containing complex | 1.15e-05 | AIMP2, CCT3, CCT5, CCT7, CCT8, LARS1, PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:CC chaperonin-containing T-complex | 1.38e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 1.38e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 1.38e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:CC proteasome regulatory particle | 4.89e-05 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:CC proteasome accessory complex | 4.89e-05 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:BP positive regulation of telomere maintenance via telomerase | 4.89e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to Cajal body | 4.89e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 4.89e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 4.89e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 4.89e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 4.89e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 4.89e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 4.89e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 4.89e-05 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING provides strong, established relationships within the two principal machinery groups. CCT3, CCT5, CCT7, and CCT8 form a tightly connected CCT/TRiC group, while PSMC2, PSMC4, PSMC6, and PSMD13 form a tightly connected proteasome-regulatory group. STRING also supports a cross-group connection between CCT8 and PSMC2, and weaker links involving EIF3F and PSMD13. The STRING functional results (15 supplementary STRING terms; within-query FDR 2.2e-05–0.00017) independently recover the CCT/TCP-1 chaperonin and proteasome-regulatory components, but they are supplementary because their reported FDR is not global correction across module-term tests. hu.MAP supports the same interpretation: CCT genes recur together in multiple CCT-associated complexes (hu.MAP huMAP3_07938.1), (hu.MAP huMAP3_06559.1), (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1), (hu.MAP huMAP3_01951.1); proteasome genes recur together in proteasome complexes (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1); and AIMP2 with LARS1 recur in aminoacyl-tRNA-synthetase-associated complexes (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1). Thus, much of the module is explained by known physical or complex-level organization. The co-abundance network appears to connect established complexes rather than reveal an entirely unrecognized protein complex.

**STRING interactions (score >= 0.7)**: 15 of 78 gene pairs: AIMP2–LARS1 (0.995); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999); CCT8–PSMC2 (0.733); EIF3F–PSMD13 (0.705); PSMC2–PSMC4 (0.999); PSMC2–PSMC6 (0.999); PSMC2–PSMD13 (0.999); PSMC4–PSMC6 (0.999); PSMC4–PSMD13 (0.999); PSMC6–PSMD13 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam TCP-1/cpn60 chaperonin family (FDR = 2.2e-05, 4 genes); Component Chaperonin-containing T-complex (FDR = 6.49e-05, 4 genes); Component Proteasome regulatory particle (FDR = 6.49e-05, 4 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 6.96e-05, 4 genes); COMPARTMENTS Proteasome regulatory particle (FDR = 6.96e-05, 4 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 9.35e-05, 4 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 9.35e-05, 4 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 9.35e-05, 4 genes); InterPro GroEL-like apical domain superfamily (FDR = 9.35e-05, 4 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 9.35e-05, 4 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 9.35e-05, 4 genes); RCTM Folding of actin by CCT/TriC (FDR = 0.00017, 4 genes); RCTM Association of TriC/CCT with target proteins during biosynthesis (FDR = 0.00017, 4 genes); RCTM Metabolism of proteins (FDR = 0.00017, 11 genes); RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding (FDR = 0.00017, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_05064.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/31); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_09656.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/64); huMAP3_13725.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/69); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_02637.1 (AIMP2, LARS1; 2/14); huMAP3_13688.1 (AIMP2, LARS1; 2/14)

### Novelty

The individual molecular relationships are not a new discovery: the CCT/TRiC and proteasome assemblies are already represented in STRING and hu.MAP, and their component genes have established protein-folding, translation, or proteasome functions. The potentially novel observation is the conserved co-abundance of these machinery groups across bone and ovary, especially the coordinated bridge involving CCT8, PSMC2, AIMP2, LARS1, EIF3F, PSMD13, and CAD. However, the available evidence does not establish that this cross-tissue co-abundance represents a new biochemical interaction or a bone–ovary-specific mechanism. Absence of a relationship from STRING or hu.MAP would not by itself establish novelty, and the presence of known complexes argues for cautious wording. This module is therefore best described as a potentially informative cross-tissue co-expression or co-abundance configuration built largely from known proteostasis machinery, rather than a demonstrated new complex or pathway.

**Hypothesis.** Hypothesis: in shared cellular populations present in bone and ovary, increased demand for synthesis, folding, remodeling, and disposal of proteins coordinately raises CCT/TRiC chaperonin activity and proteasome-regulatory activity. CCT-mediated folding could support assembly of cytoskeletal, signaling, or nuclear proteins, while the proteasome removes damaged or surplus proteins; the CCT8–PSMC2 connection may represent functional coupling between folding and degradation. AIMP2 and LARS1 could connect this proteostasis state to aminoacyl-tRNA-synthetase-associated translation machinery, while CAD and RRM2 may reflect nucleotide-production or proliferative demands and EIF3F may connect translation initiation with protein turnover. The telomerase, Cajal-body, reproductive-recognition, and DNA-biosynthesis enrichments suggest testable consequences involving nuclear RNA handling, cell proliferation, or reproductive cell states, but they remain mechanistic hypotheses rather than demonstrated functions of the conserved bone–ovary module. Testing should assess whether module activity tracks cell composition, proliferation, protein-folding stress, and proteasome activity independently in purified bone and ovarian cell populations.

### Important genes

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT3 (0.94), CCT8 (0.92), CCT7 (0.87), PSMC2 (0.86), PSMC4 (0.84); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is a central network member within the CCT/TRiC group and connects strongly to CCT3, CCT7, CCT8, PSMC2, and PSMC4. It participates in the chaperonin-containing T-complex and is represented across the extensive primary CCT, protein-folding, Cajal-body, telomere-maintenance, recognition, and fertilization evidence (4 globally significant GO/KEGG terms, q_global 1.15e-05–1.38e-05; see the table), (15 globally significant GO/KEGG terms, q_global 4.89e-05–0.000387; see the table), (6 globally significant GO/KEGG terms, q_global 0.000918–0.00179; see the table), (GO:MF ATP hydrolysis activity; q_global = 0.00296), (8 globally significant GO/KEGG terms, q_global 0.00399–0.0128; see the table), (6 globally significant GO/KEGG terms, q_global 0.0133–0.0199; see the table), (GO:MF unfolded protein binding; q_global = 0.0258), (GO:BP positive regulation of chromosome organization; q_global = 0.0292), (4 globally significant GO/KEGG terms, q_global 0.0409–0.0467; see the table). STRING and hu.MAP independently place it in the CCT complex (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 2.2e-05), (STRING Component Chaperonin-containing T-complex; within-query FDR = 6.49e-05), (hu.MAP huMAP3_07938.1), (hu.MAP huMAP3_06559.1), (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1), (hu.MAP huMAP3_01951.1). It also has a substantial literature and an established association with hereditary sensory and autonomic neuropathy.
- **Conclusion**: Established evidence supports CCT5 as a core chaperonin component and a major structural or functional anchor of the module. Its network position and annotations make it a strong candidate for representing the protein-folding arm. It is not established that CCT5 specifically drives the conserved bone–ovary association or directly controls telomerase in these tissues.

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT5 (0.92), CCT7 (0.85), CCT3 (0.84), LARS1 (0.82); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999), PSMC2 (0.733)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is a central CCT/TRiC member and the clearest network bridge from the chaperonin group to the proteasome group through its connection with PSMC2. It is part of the same highly supported CCT and chaperone evidence as CCT5 (4 globally significant GO/KEGG terms, q_global 1.15e-05–1.38e-05; see the table), (15 globally significant GO/KEGG terms, q_global 4.89e-05–0.000387; see the table), (6 globally significant GO/KEGG terms, q_global 0.000918–0.00179; see the table), (GO:MF ATP hydrolysis activity; q_global = 0.00296), (8 globally significant GO/KEGG terms, q_global 0.00399–0.0128; see the table), (6 globally significant GO/KEGG terms, q_global 0.0133–0.0199; see the table), (GO:MF unfolded protein binding; q_global = 0.0258), (GO:BP positive regulation of chromosome organization; q_global = 0.0292), (4 globally significant GO/KEGG terms, q_global 0.0409–0.0467; see the table), and is supported by STRING and several hu.MAP CCT complexes (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 2.2e-05), (STRING Component Chaperonin-containing T-complex; within-query FDR = 6.49e-05), (hu.MAP huMAP3_07938.1), (hu.MAP huMAP3_06559.1), (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). HPA shows cell-type enhancement in oocytes, making it especially relevant to interpretation of the ovary component, although its overall tissue specificity is low.
- **Conclusion**: Established evidence supports CCT8 as a CCT/TRiC subunit and as a plausible connectivity point between folding and degradation machinery. The oocyte signal and cross-group network position make it an important candidate for testing cell-state or tissue-composition explanations. A direct mechanistic bridge between CCT8 and the proteasome remains a hypothesis rather than an experimentally established conclusion here.

#### PSMC2

- **Related proteins** (co-abundance neighbors): PSMC4 (0.92), EIF3F (0.88), PSMD13 (0.88), CCT5 (0.86), CCT3 (0.83), PSMC6 (0.80); STRING partners: CCT8 (0.733), PSMC4 (0.999), PSMC6 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is the most connected module gene and links the proteasome-regulatory group to CCT proteins and EIF3F. It is an ATPase subunit of the proteasome regulatory particle, with primary evidence for proteasome complexes, ATP-dependent activity, proteasome pathways, and protein metabolism (GO:CC intracellular protein-containing complex; q_global = 1.15e-05), (GO:CC proteasome regulatory particle; q_global = 4.89e-05), (GO:CC proteasome accessory complex; q_global = 4.89e-05), (GO:MF proteasome-activating activity; q_global = 0.000916), (4 globally significant GO/KEGG terms, q_global 0.00238–0.00399; see the table), (GO:BP protein metabolic process; q_global = 0.00658), (5 globally significant GO/KEGG terms, q_global 0.0128–0.0172; see the table), (KEGG Spinocerebellar ataxia - Homo sapiens (human); q_global = 0.0199), (GO:MF hydrolase activity; q_global = 0.0269), (GO:MF adenyl nucleotide binding; q_global = 0.0283), (GO:MF ribonucleoside triphosphate phosphatase activity; q_global = 0.0321), (KEGG Epstein-Barr virus infection - Homo sapiens (human); q_global = 0.0368), (GO:MF pyrophosphatase activity; q_global = 0.0467) (GO:MF hydrolase activity, acting on acid anhydrides; q_global = 0.0467) (GO:MF hydrolase activity, acting on acid anhydrides, in phosphorus-containing anhydrides; q_global = 0.0467). STRING and hu.MAP strongly support its membership in the proteasome regulatory machinery (STRING Component Proteasome regulatory particle; within-query FDR = 6.49e-05), (STRING COMPARTMENTS Proteasome regulatory particle; within-query FDR = 6.96e-05), (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1). It has substantial literature and disease associations involving plasma-cell and lymphoid malignancies, neoplasia, infection, and amyloidosis.
- **Conclusion**: Established evidence supports PSMC2 as a central proteasome-regulatory ATPase and the principal network connector between the module's major machinery groups. Its presence is consistent with coordinated protein quality control. The disease associations do not demonstrate that the module is cancer-related, and a specific bone–ovary mechanism remains unproven.

#### PSMD13

- **Related proteins** (co-abundance neighbors): PSMC2 (0.88), PSMC6 (0.84), PSMC4 (0.82), CAD (0.82); STRING partners: EIF3F (0.705), PSMC2 (0.999), PSMC4 (0.999), PSMC6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 is the non-ATPase proteasome-regulatory component that completes the proteasome group with PSMC2, PSMC4, and PSMC6. It has primary support for the proteasome regulatory particle, proteasome complex, endopeptidase and peptidase complexes, and proteasome-related KEGG pathways (GO:CC intracellular protein-containing complex; q_global = 1.15e-05), (GO:CC proteasome regulatory particle; q_global = 4.89e-05), (GO:CC proteasome accessory complex; q_global = 4.89e-05), (KEGG Proteasome - Homo sapiens (human); q_global = 0.00238), (GO:CC proteasome complex; q_global = 0.00399), (GO:BP protein metabolic process; q_global = 0.00658), (GO:CC endopeptidase complex; q_global = 0.0128), (GO:CC peptidase complex; q_global = 0.0172), (KEGG Spinocerebellar ataxia - Homo sapiens (human); q_global = 0.0199), (KEGG Epstein-Barr virus infection - Homo sapiens (human); q_global = 0.0368). It occupies a network position connecting the proteasome group to CAD and EIF3F, and its STRING and hu.MAP relationships are concordant with proteasome membership (STRING Component Proteasome regulatory particle; within-query FDR = 6.49e-05), (STRING COMPARTMENTS Proteasome regulatory particle; within-query FDR = 6.96e-05), (hu.MAP huMAP3_05064.1), (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1). It has established disease associations involving plasma-cell malignancy, lymphoma, neurodegeneration, neoplasia, and HIV infection.
- **Conclusion**: Established evidence supports PSMD13 as a proteasome regulatory-particle component and as a useful marker of the degradation arm of the module. Its links to EIF3F and CAD suggest possible integration with translation and nucleotide metabolism, but those cross-process relationships should be treated as hypotheses rather than proven molecular functions of this module.

#### AIMP2

- **Related proteins** (co-abundance neighbors): RRM2 (0.83), CAD (0.82); STRING partners: LARS1 (0.995)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: aminoacyl tRNA synthetase complex interacting multifunctional protein 2. The protein encoded by this gene is part of the aminoacyl-tRNA synthetase complex, which contains nine different aminoacyl-tRNA synthetases and three non-enzymatic factors. The encoded protein is one of the non-enzymatic factors and is required for assembly and stability of the complex. [provided by RefSeq, May 2016].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 17 (0.617); hereditary disease (0.494); Neurodevelopmental abnormality (0.111); Parkinson disease (0.107); neoplasm (0.106)
- **Europe PMC papers**: 605
- **Why important**: AIMP2 connects the module to aminoacyl-tRNA-synthetase-associated complexes through hu.MAP complexes containing AIMP2 and LARS1 (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1), and it has a strong STRING relationship with LARS1. It contributes to the broad intracellular protein-complex and protein-metabolism evidence (GO:CC intracellular protein-containing complex; q_global = 1.15e-05), (GO:BP protein metabolic process; q_global = 0.00658) and is tissue-enhanced in skeletal muscle with cell-type enhancement in late primary spermatocytes. Its established function is as a multifunctional non-enzymatic component required for assembly and stability of an aminoacyl-tRNA-synthetase complex, and it has disease associations including hypomyelinating leukodystrophy and neurodevelopmental conditions.
- **Conclusion**: Established evidence supports AIMP2 as a translation-related complex-assembly factor that may connect protein synthesis with the proteostasis machinery. Its relatively peripheral network position means it is less suitable than the CCT or proteasome genes as a core module marker. A role in coupling translation demand to folding and degradation is a plausible hypothesis, not a demonstrated property of this conserved module.

## Module 6

**Tissue pair**: bone and ovary  
**Genes (7)**: AKAP8, BYSL, CIAO1, DDX21, MYBBP1A, NOP16, NOP2

### Function

The module is most strongly associated with nucleolar ribosome and ribonucleoprotein biogenesis. The primary evidence is the globally corrected enrichment for ribosome biogenesis (GO:BP ribosome biogenesis; q_global = 0.0111), nucleolus (GO:CC nucleolus; q_global = 0.0327), and ribonucleoprotein complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0365). Positive regulation of transcription by RNA polymerase III (GO:BP positive regulation of transcription by RNA polymerase III; q_global = 0.0481) and the B-WICH complex (GO:CC B-WICH complex; q_global = 0.0481) provide additional, more specific support involving DDX21 and MYBBP1A. The STRING results independently support a nucleolar ribosome-biogenesis interpretation through (STRING Component Nucleolus; within-query FDR = 0.0156), (STRING Process Ribosome biogenesis; within-query FDR = 0.0333), and (STRING Component B-WICH complex; within-query FDR = 0.048). Overall, this is best interpreted as a conserved RNA-processing and ribosome-assembly module rather than as a tissue-specific extracellular pathway. CIAO1 is the least directly integrated member because it has no GO or STRING enrichment assignment in this module, although its established role concerns iron-sulfur cluster assembly and protein maturation.

**Cell composition.** The module is not composed of plasma or secreted proteins: HPA reports no secreted genes. All genes have low tissue specificity, and all have low immune-cell specificity, arguing against a blood-cell or plasma-contamination explanation. Several genes show cell-type enhancement in epithelial, stromal, germ-cell, neural, or cardiac populations, but there is no repeated enriched tissue pattern. The nucleolar or nuclear localization and broadly expressed profiles are consistent with conserved cellular machinery, possibly reflecting shared proliferative or biosynthetic cell states in bone and ovary rather than a specialized bone-ovary signaling program. HPA protein detection in ovary is present for several members, including BYSL, NOP16, AKAP8, and CIAO1, while the bone comparison lacks matching HPA tissue data.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP ribosome biogenesis | 0.0111 | BYSL, DDX21, MYBBP1A, NOP16, NOP2 |
| GO:CC nucleolus | 0.0327 | AKAP8, BYSL, DDX21, MYBBP1A, NOP16, NOP2 |
| GO:BP ribonucleoprotein complex biogenesis | 0.0365 | BYSL, DDX21, MYBBP1A, NOP16, NOP2 |
| GO:BP positive regulation of transcription by RNA polymerase III | 0.0481 | DDX21, MYBBP1A |
| GO:CC B-WICH complex | 0.0481 | DDX21, MYBBP1A |

### STRING and hu.MAP

The strongest known relationships are concentrated around DDX21, MYBBP1A, NOP2, and BYSL. STRING supports BYSL with MYBBP1A and NOP2, DDX21 with MYBBP1A and NOP2, and MYBBP1A with NOP2. These links agree with the globally corrected nucleolar and ribosome-biogenesis terms and indicate that the co-abundance signal captures a biologically coherent, already recognized nucleolar interaction neighborhood. NOP16 and AKAP8 connect to DDX21 in the module network but lack listed high-confidence STRING partners, and the BYSL-CIAO1 module connection is not represented among the listed high-confidence STRING interactions. No hu.MAP complex contains at least two module members, so the absence of a hu.MAP match does not negate the network; it indicates that this particular co-abundance group is not recovered as a hu.MAP multi-member complex.

**STRING interactions (score >= 0.7)**: 5 of 21 gene pairs: BYSL–MYBBP1A (0.73); BYSL–NOP2 (0.915); DDX21–MYBBP1A (0.963); DDX21–NOP2 (0.761); MYBBP1A–NOP2 (0.864)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Nucleolus (FDR = 0.0156, 6 genes); Process Ribosome biogenesis (FDR = 0.0333, 5 genes); Component B-WICH complex (FDR = 0.048, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The underlying molecular function is not a new biological concept. Ribosome biogenesis, nucleolar localization, and several pairwise relationships are already supported by GO annotations, STRING, gene descriptions, and substantial literature. The potentially novel aspect is the coordinated co-abundance of these genes across bone and ovary and the inclusion of the less-connected members in one conserved module. However, the fact sheet does not establish that this tissue-pair association is specific, causal, or previously undescribed. Lack of a hu.MAP complex or lack of a listed STRING relationship for some edges is insufficient to claim discovery. The cautious conclusion is that this is a potentially novel cross-tissue co-abundance pattern built around an established nucleolar program.

**Hypothesis.** Hypothesis: the shared bone-ovary module reflects a conserved demand for nucleolar RNA production, ribosome assembly, and growth-related biosynthetic capacity in a common cellular state. DDX21, MYBBP1A, and NOP2 may form the central RNA-processing and nucleolar coordination axis, with BYSL and NOP16 supporting ribosome-biogenesis functions, while AKAP8 may connect the program to nuclear organization and cell-cycle-associated regulation. CIAO1 may represent a peripheral link to protein maturation or iron-sulfur-dependent cellular processes. This hypothesis predicts coordinated regulation of ribosome production and cell-state transitions, but the co-abundance data alone do not demonstrate physical complex formation, directionality, or tissue-specific causation.

### Important genes

#### DDX21

- **Related proteins** (co-abundance neighbors): NOP16 (0.94), AKAP8 (0.88), NOP2 (0.85), MYBBP1A (0.84), BYSL (0.80); STRING partners: MYBBP1A (0.963), NOP2 (0.761)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 is the most connected and strongest central node in the module, linking NOP16, AKAP8, NOP2, MYBBP1A, and BYSL. It appears in every primary GO term (GO:BP ribosome biogenesis; q_global = 0.0111), (GO:CC nucleolus; q_global = 0.0327), (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0365), (GO:BP positive regulation of transcription by RNA polymerase III; q_global = 0.0481), and (GO:CC B-WICH complex; q_global = 0.0481), as well as every supplementary STRING term (STRING Component Nucleolus; within-query FDR = 0.0156), (STRING Process Ribosome biogenesis; within-query FDR = 0.0333), and (STRING Component B-WICH complex; within-query FDR = 0.048). Its DEAD-box RNA-helicase annotation, nucleolar and mitotic-chromosome localization, osteoblast-differentiation annotation, and extensive literature support make it the clearest integrator of RNA processing, ribosome assembly, and cellular growth. Disease associations include neurodegenerative disease and several cancers.
- **Conclusion**: Established evidence supports DDX21 as the central nucleolar RNA-processing component of this module. It is plausible that DDX21 organizes the shared co-abundance program, but the network does not establish that it regulates the other genes in bone or ovary.

#### MYBBP1A

- **Related proteins** (co-abundance neighbors): NOP2 (0.88), DDX21 (0.84); STRING partners: BYSL (0.73), DDX21 (0.963), NOP2 (0.864)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MYB binding protein 1a. This gene encodes a nucleolar transcriptional regulator that was first identified by its ability to bind specifically to the Myb proto-oncogene protein. The encoded protein is thought to play a role in many cellular processes including response to nucleolar stress, tumor suppression and synthesis of ribosomal DNA. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep…
- **Diseases (Open Targets)**: neurodegenerative disease (0.507); Non-immune hydrops fetalis (0.370); ventricular septal defect (0.245); lysosomal storage disease (0.191); Meniere disease (0.162)
- **Europe PMC papers**: 763
- **Why important**: MYBBP1A is a central connector with strong relationships to DDX21 and NOP2 and additional support from BYSL. It participates in every primary GO term (GO:BP ribosome biogenesis; q_global = 0.0111), (GO:CC nucleolus; q_global = 0.0327), (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0365), (GO:BP positive regulation of transcription by RNA polymerase III; q_global = 0.0481), and (GO:CC B-WICH complex; q_global = 0.0481) and every supplementary STRING term (STRING Component Nucleolus; within-query FDR = 0.0156), (STRING Process Ribosome biogenesis; within-query FDR = 0.0333), and (STRING Component B-WICH complex; within-query FDR = 0.048). Its nucleolar transcription-regulator annotation, roles in nucleolar stress, tumor suppression, ribosomal DNA synthesis, chromatin remodeling, and osteoblast differentiation give it functional relevance to both the inferred ribosome program and bone biology. It also has disease associations involving neurodegenerative disease and developmental disorders.
- **Conclusion**: Established evidence places MYBBP1A at the intersection of nucleolar transcriptional regulation and ribosome production. A role in coordinating the bone-ovary shared state is a hypothesis rather than a demonstrated tissue-specific function.

#### NOP2

- **Related proteins** (co-abundance neighbors): MYBBP1A (0.88), DDX21 (0.85); STRING partners: BYSL (0.915), DDX21 (0.761), MYBBP1A (0.864)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP2 nucleolar protein. Enables RNA binding activity. Involved in positive regulation of cell population proliferation; regulation of signal transduction by p53 class mediator; and ribosomal large subunit assembly. Located in nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.273); nonpapillary renal cell carcinoma (0.097); neoplasm (0.097); cancer (0.091); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 2120
- **Why important**: NOP2 is tightly embedded in the DDX21-MYBBP1A core and has STRING support with BYSL, DDX21, and MYBBP1A. It contributes to the primary ribosome-biogenesis, nucleolus, and ribonucleoprotein-biogenesis terms (GO:BP ribosome biogenesis; q_global = 0.0111), (GO:CC nucleolus; q_global = 0.0327), and (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0365), and to the supplementary nucleolar and ribosome-biogenesis terms (STRING Component Nucleolus; within-query FDR = 0.0156) and (STRING Process Ribosome biogenesis; within-query FDR = 0.0333). Its established functions include rRNA processing, maturation of the large ribosomal subunit, and ribosomal large-subunit assembly. It has a substantial literature base and associations with neurodegenerative disease and neoplastic conditions.
- **Conclusion**: Established evidence identifies NOP2 as a core ribosome-maturation component and a strong functional marker of the module. Its co-abundance may indicate shared ribosome-production demand, but it does not by itself prove altered translation in either tissue.

#### BYSL

- **Related proteins** (co-abundance neighbors): CIAO1 (0.83), DDX21 (0.80); STRING partners: MYBBP1A (0.73), NOP2 (0.915)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim, Mitotic chromosome; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: bystin like. Bystin is expressed as a 2-kb major transcript and a 3.6-kb minor transcript in SNG-M cells and in human trophoblastic teratocarcinoma HT-H cells. Protein binding assays determined that bystin binds directly to trophinin and tastin, and that binding is enhanced when cytokeratins 8 and 18 are present. Immunocytochemistry of HT-H cells showed that bystin colocalizes with trophinin, tastin, and the c…
- **Diseases (Open Targets)**: neurodegenerative disease (0.393); glioma (0.084); central nervous system cancer (0.084); cancer (0.081); glioblastoma (0.078)
- **Europe PMC papers**: 392
- **Why important**: BYSL contributes to the primary ribosome-biogenesis, nucleolus, and ribonucleoprotein-biogenesis terms (GO:BP ribosome biogenesis; q_global = 0.0111), (GO:CC nucleolus; q_global = 0.0327), and (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0365), and to the supplementary STRING terms (STRING Component Nucleolus; within-query FDR = 0.0156) and (STRING Process Ribosome biogenesis; within-query FDR = 0.0333). It has established annotations for rRNA processing, ribosome biogenesis, and regulation of protein localization to the nucleolus. Its connections to NOP2, MYBBP1A, and DDX21 support the central nucleolar interpretation. HPA detects BYSL protein in ovary and reports enhancement in oocytes and decidual stromal cells, giving it particular relevance to the tissue context. Its literature volume is smaller than that of DDX21 or NOP2, but it has documented links to trophoblast-associated cellular complexes and cancer-related disease associations.
- **Conclusion**: Established evidence supports BYSL as a nucleolar ribosome-biogenesis component with relevant ovarian protein detection. Its possible role in linking the conserved module to reproductive or stromal cell states remains a hypothesis.

#### NOP16

- **Related proteins** (co-abundance neighbors): DDX21 (0.94); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP16 nucleolar protein. This gene encodes a protein that is localized to the nucleolus. Expression of this gene is induced by estrogens and Myc protein and is a marker of poor patient survival in breast cancer. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.473); Parkinson disease (0.462); lysosomal storage disease (0.462); Alzheimer disease (0.462); colorectal carcinoma (0.083)
- **Europe PMC papers**: 258
- **Why important**: NOP16 is a direct DDX21 neighbor and appears in the primary ribosome-biogenesis, nucleolus, and ribonucleoprotein-biogenesis terms (GO:BP ribosome biogenesis; q_global = 0.0111), (GO:CC nucleolus; q_global = 0.0327), and (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.0365), as well as the supplementary nucleolar and ribosome-biogenesis terms (STRING Component Nucleolus; within-query FDR = 0.0156) and (STRING Process Ribosome biogenesis; within-query FDR = 0.0333). Its annotated function is ribosomal large-subunit biogenesis, and HPA places it in the nucleolus with protein detection in ovary. Its cell-type enhancement in basal epithelial and cardiac populations suggests that its signal may track a broadly conserved biosynthetic state rather than a uniquely ovarian process. It has a more limited literature base than the central genes but has reported associations with cancer biology and neurodegenerative disease.
- **Conclusion**: Established evidence supports NOP16 as a supporting large-subunit biogenesis component. Its ovarian detection strengthens tissue relevance, while any special role in the shared bone-ovary module remains unproven.

#### AKAP8

- **Related proteins** (co-abundance neighbors): DDX21 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: A-kinase anchoring protein 8. This gene encodes a member of the A-kinase anchor protein family. A-kinase anchor proteins are scaffold proteins that contain a binding domain for the RI/RII subunit of protein kinase A (PKA) and recruit PKA and other signaling molecules to specific subcellular locations. This gene encodes a nuclear A-kinase anchor protein that binds to the RII alpha subunit of PKA and may play a role in chromosom…
- **Diseases (Open Targets)**: neurodegenerative disease (0.264); breast carcinoma (0.084); breast cancer (0.084); ovarian carcinoma (0.078); ovarian cancer (0.078)
- **Europe PMC papers**: 396
- **Why important**: AKAP8 is a DDX21 neighbor and the only module member assigned to the primary nucleolus term without assignment to the primary ribosome-biogenesis and ribonucleoprotein-biogenesis terms (GO:CC nucleolus; q_global = 0.0327). It also appears in the supplementary nucleolar term (STRING Component Nucleolus; within-query FDR = 0.0156). Its nuclear scaffold function, PKA anchoring, chromatin targeting, mitotic chromosome condensation, cell-cycle annotations, and ovarian follicle-development annotation provide a possible bridge between nucleolar activity and nuclear or proliferative state. HPA detects the protein in ovary and reports enhancement in endometrial glandular, luminal, and secretory cells. It has documented associations with ovarian and breast cancer and a moderate literature base.
- **Conclusion**: Established evidence supports AKAP8 as a nuclear organizational and cell-cycle-associated component connected to the nucleolar core through DDX21. Its role as a bridge between ribosome biogenesis and tissue-specific cell-state regulation is a hypothesis.

## Module 7

**Tissue pair**: bone and ovary  
**Genes (10)**: ATXN2L, BAG3, CCDC6, CD2AP, CIAPIN1, OGFOD1, ADSS2, SRPK1, TUBA1C, TBCE

### Function

The module does not support a single significantly enriched GO or KEGG function: no GO or KEGG term passed global correction. Its gene annotations instead point to a mixed cellular-maintenance program involving RNA processing and stress-granule biology through ATXN2L, SRPK1, and OGFOD1; cytoskeletal and microtubule organization through TBCE, TUBA1C, and CD2AP; proteostasis and stress responses through BAG3 and CIAPIN1; and purine biosynthesis through ADSS2. Because these processes are heterogeneous and the co-abundance graph is sparse, the most defensible interpretation is a candidate shared cellular-state module rather than a demonstrated pathway module. The co-abundance pattern may reflect coordinated regulation of housekeeping, stress-adaptation, cytoskeletal, and RNA-processing functions in shared cellular populations of bone and ovary.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and all have HPA annotations, which is compatible with broadly expressed cellular proteins rather than a specialized tissue-restricted program. At the same time, most genes show enhanced specificity for particular cell types. The highlighted cell types include germline populations, oocytes, esophageal cells, neural or glial populations, and several immune populations. Blood-cell enhancement occurs for several genes, especially SRPK1, CD2AP, BAG3, and TUBA1C, but the module is not uniformly blood-cell specific. The shared bone–ovary signal could therefore reflect common cellular composition or a shared stress, structural, or proliferative state rather than a bone–ovary-specific biochemical pathway. Ovary protein detection is broad across the module, whereas matching HPA bone protein data are unavailable, so the tissue-level protein evidence does not establish bone-specific expression.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and no STRING functional-enrichment result is reported. No hu.MAP complex contains multiple module members. Thus, the observed co-abundance relationships are not corroborated here as a known physical interaction network or a shared hu.MAP complex. The absence of STRING or hu.MAP support does not disprove biological coordination; it indicates that the module is better viewed as a co-expression or co-abundance pattern whose molecular mechanism remains unresolved. The strongest internal links connect ADSS2 with OGFOD1, TUBA1C, and TBCE; connect ATXN2L with CIAPIN1, BAG3, and CCDC6; and connect TBCE with SRPK1 and SRPK1 with CD2AP. These links span distinct annotated processes, reinforcing the need for a cautious interpretation.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel tissue-pair co-abundance pattern, but it should not be called a newly discovered biological complex or pathway. Its novelty is supported only in the limited sense that the particular cross-gene organization is not represented by the reported STRING interactions or hu.MAP complexes and has no globally significant GO or KEGG annotation. Those absences alone cannot establish novelty, because databases are incomplete and co-abundance relationships need not correspond to physical interactions. A stronger novelty claim would require replication in independent bone and ovary datasets, preservation of the module under alternative network procedures, and testing against cell-composition and sample-quality covariates. At present, the appropriate classification is a novel candidate module architecture with an unresolved biological basis.

**Hypothesis.** Hypothesis: the module represents a shared cellular stress-adaptation and structural-maintenance state present in cell populations sampled from bone and ovary. In this model, ATXN2L and OGFOD1 could mark stress-granule or translational-control activity, SRPK1 could coordinate RNA-splicing regulation, TBCE and TUBA1C could support microtubule organization, CD2AP could connect cytoskeletal remodeling with membrane trafficking, and CIAPIN1 and BAG3 could support oxidative-stress tolerance, protein quality control, and survival. ADSS2 could provide a metabolic component through purine biosynthesis. This model is mechanistically plausible from the supplied annotations and network arrangement, but it is not demonstrated by enrichment, STRING, hu.MAP, or causal experiments.

### Important genes

#### SRPK1

- **Related proteins** (co-abundance neighbors): TBCE (0.89), CD2AP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SRSF protein kinase 1. This gene encodes a serine/arginine protein kinase specific for the SR (serine/arginine-rich domain) family of splicing factors. The protein localizes to the nucleus and the cytoplasm. It is thought to play a role in regulation of both constitutive and alternative splicing by regulating intracellular localization of splicing factors. Alternative splicing of this gene results in multiple transcript…
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); COVID-19 (0.372); celiac disease (0.190); ulcerative colitis (0.132); type 1 diabetes mellitus (0.123)
- **Europe PMC papers**: 1777
- **Why important**: SRPK1 is among the more connected genes in the module and links TBCE with CD2AP, placing RNA-splicing regulation between cytoskeletal and membrane-associated components of the network. Its established function is phosphorylation of SR splicing factors, with roles in RNA splicing, spliceosomal assembly, chromosome segregation, and sperm DNA condensation. It also has substantial literature and disease associations spanning neurological and immune-related conditions.
- **Conclusion**: Established evidence supports SRPK1 as a regulator of splicing and phosphorylation-dependent cellular organization. Its position in this module supports the possibility that RNA-processing state is coordinated with structural remodeling, but the module does not establish that SRPK1 mediates the relationships.

#### ATXN2L

- **Related proteins** (co-abundance neighbors): CIAPIN1 (0.83), BAG3 (0.82), CCDC6 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ataxin 2 like. This gene encodes an ataxin type 2 related protein of unknown function. This protein is a member of the spinocerebellar ataxia (SCAs) family, which is associated with a complex group of neurodegenerative disorders. Several alternatively spliced transcripts encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.284); Crohn disease (0.230); Macrocephaly (0.185); Intellectual disability (0.185); neurodevelopmental disorder (0.119)
- **Europe PMC papers**: 465
- **Why important**: ATXN2L is one of the more connected genes and links CIAPIN1, BAG3, and CCDC6. Its annotations implicate mRNA metabolism and cytoplasmic stress-granule assembly, making it a plausible integrator of RNA handling and cellular stress. It has a substantial literature base and disease associations involving neurodegenerative and neurodevelopmental disorders.
- **Conclusion**: Established evidence supports ATXN2L in RNA metabolism and stress-granule biology, although its precise molecular function remains incompletely defined. Its network position makes it a strong candidate coordinator of the module, but that coordinating role remains a hypothesis.

#### CIAPIN1

- **Related proteins** (co-abundance neighbors): ATXN2L (0.83), CD2AP (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytokine induced apoptosis inhibitor 1. CIAPIN1 is a cytokine-induced inhibitor of apoptosis with no relation to apoptosis regulatory molecules of the BCL2 (MIM 151430) or CASP (see MIM 147678) families. Expression of CIAPIN1 is dependent on growth factor stimulation (Shibayama et al., 2004 [PubMed 14970183]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.513); coronary atherosclerosis (0.247); neoplasm (0.098); breast cancer (0.096); breast carcinoma (0.096)
- **Europe PMC papers**: 992
- **Why important**: CIAPIN1 connects ATXN2L with CD2AP and is annotated for iron-sulfur cluster assembly, hematopoiesis, oxidative-stress responses, and negative regulation of apoptosis. Its mitochondrial localization and enhanced representation in reproductive cell populations are relevant to metabolically demanding or stress-sensitive tissues. It also has substantial literature and disease associations involving neurodegeneration, atherosclerosis, and cancer.
- **Conclusion**: Established evidence supports CIAPIN1 as a broadly relevant survival, mitochondrial, and stress-response factor. In this module it could link stress tolerance with RNA and cytoskeletal processes, but the co-abundance data do not establish a causal survival pathway.

#### ADSS2

- **Related proteins** (co-abundance neighbors): OGFOD1 (0.84), TUBA1C (0.82), TBCE (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenylosuccinate synthase 2. This gene encodes the enzyme adenylosuccinate synthetase which catalyzes the first committed step in the conversion of inosine monophosphate to adenosine monophosphate. A pseudogene of this gene is found on chromosome 17.[provided by RefSeq, Nov 2010].
- **Diseases (Open Targets)**: atopic eczema (0.085); respiratory tract infectious disorder (0.077); dermatomycosis (0.062); hyperlipoproteinemia type V (0.056); LCAT deficiency (0.054)
- **Europe PMC papers**: 102
- **Why important**: ADSS2 is the most internally connected gene in the supplied graph and links OGFOD1, TUBA1C, and TBCE, thereby joining purine metabolism to stress-granule, microtubule, and tubulin-folding annotations. Its established biochemical role is catalysis of a committed step in AMP biosynthesis. It has fewer literature and disease associations than several other candidates, which makes its position in this module particularly useful for generating a testable metabolic hypothesis.
- **Conclusion**: Established evidence supports ADSS2 as a purine-biosynthetic enzyme. Its central network position suggests that nucleotide supply may covary with structural and stress-related programs in the sampled tissues, but this metabolic interpretation is not supported by significant GO or KEGG enrichment and remains provisional.

#### CD2AP

- **Related proteins** (co-abundance neighbors): CIAPIN1 (0.82), SRPK1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD2 associated protein. This gene encodes a scaffolding molecule that regulates the actin cytoskeleton. The protein directly interacts with filamentous actin and a variety of cell membrane proteins through multiple actin binding sites, SH3 domains, and a proline-rich region containing binding sites for SH3 domains. The cytoplasmic protein localizes to membrane ruffles, lipid rafts, and the leading edges of cells. It is i…
- **Diseases (Open Targets)**: familial idiopathic steroid-resistant nephrotic syndrome (0.701); focal segmental glomerulosclerosis (0.585); Alzheimer disease (0.493); dementia (0.395); Abnormality of the skeletal system (0.314)
- **Europe PMC papers**: 3461
- **Why important**: CD2AP connects CIAPIN1 with SRPK1 and encodes a well-characterized actin-associated scaffold involved in membrane organization, trafficking, migration, secretion, and synapse organization. It has one of the largest literature bases in the module and established disease associations involving kidney disease, Alzheimer disease, dementia, and skeletal abnormalities. Its plasma-membrane localization provides a potential interface between intracellular regulation and cellular morphology.
- **Conclusion**: Established evidence supports CD2AP as a cytoskeletal and membrane-trafficking scaffold. In this module it may represent remodeling of cell shape or cell–cell interactions, but its connection to the other module genes is a co-abundance observation rather than a demonstrated protein interaction.

#### BAG3

- **Related proteins** (co-abundance neighbors): ATXN2L (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BAG cochaperone 3. BAG proteins compete with Hip for binding to the Hsc70/Hsp70 ATPase domain and promote substrate release. All the BAG proteins have an approximately 45-amino acid BAG domain near the C terminus but differ markedly in their N-terminal regions. The protein encoded by this gene contains a WW domain in the N-terminal region and a BAG domain in the C-terminal region. The BAG domains of BAG1, BAG2, and …
- **Diseases (Open Targets)**: dilated cardiomyopathy 1HH (0.821); myofibrillar myopathy 6 (0.789); dilated cardiomyopathy (0.726); familial isolated dilated cardiomyopathy (0.678); heart failure (0.654)
- **Europe PMC papers**: 4304
- **Why important**: BAG3 connects to ATXN2L and is tissue enhanced in skeletal muscle, while also showing enhanced representation in several contractile, epithelial, pancreatic, and immune cell types. Its established functions include HSP70-associated protein handling, autophagosome assembly, protein folding, heat response, and protection from selected apoptotic stresses. BAG3 has extensive literature and strong disease associations involving cardiomyopathy, myofibrillar myopathy, and heart failure.
- **Conclusion**: Established evidence supports BAG3 as a proteostasis and stress-response regulator. Its connection to ATXN2L makes it a plausible bridge between protein quality control and stress-granule biology, but the module does not demonstrate that BAG3 drives the shared bone–ovary signal.

## Module 8

**Tissue pair**: bone and ovary  
**Genes (28)**: MTHFD1L, CMC1, DIABLO, HSD17B4, DHRS7, SLC25A10, ECI1, ETFA, GALNT2, HSD17B10, IKBIP, MANF, MYOF, NFU1, OCIAD2, ALDH18A1, PCK2, PPIC, PTPMT1, RAB32, RRBP1, MRRF, SYNGR2, SPRYD4, SUCLG1, YARS2, TACO1, VAMP7

### Function

The best-supported function is mitochondrial metabolic activity, with a prominent emphasis on mitochondrial matrix processes and fatty-acid catabolism. Mitochondrial localization is supported by the globally corrected cellular-component terms (GO:CC mitochondrion; q_global = 0.00243) and (GO:CC mitochondrial matrix; q_global = 0.0104). Fatty-acid catabolism and monocarboxylic-acid catabolism are supported by (GO:BP fatty acid catabolic process; q_global = 0.023) and (GO:BP monocarboxylic acid catabolic process; q_global = 0.0492). The contributing genes span fatty-acid oxidation, mitochondrial electron transfer, the tricarboxylic-acid cycle, mitochondrial translation, mitochondrial metabolite transport, folate metabolism, and mitochondrial quality or apoptotic control. The pattern therefore suggests a coordinated mitochondrial metabolic state rather than a narrowly defined pathway. The network itself is relatively sparse, so co-abundance may reflect shared regulation, shared cellular composition, or coordinated mitochondrial abundance rather than direct physical interaction among all module members.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: only a small subset is annotated as secreted, and most genes have intracellular or organellar annotations. HPA indicates that many genes have low tissue specificity, while others are enriched in liver, kidney, blood vessel, skeletal muscle, salivary gland, or intestine-related contexts. The single-cell annotations are broadly cell-type enhanced, with recurring signals in hepatocytes, enterocytes, epithelial cells, trophoblasts, and selected immune or blood-cell populations. Most genes have low immune-cell specificity, although several are immune-cell enhanced and a smaller subset is associated with NK cells, basophils, neutrophils, monocytes, or plasmacytoid dendritic cells. The module therefore does not look primarily like a blood-cell or plasma-protein signature, but shared cell types, tissue composition, or a general mitochondrial abundance signal could contribute to its appearance in bone and ovary. Protein detection in ovary is present for many module members, whereas bone protein evidence is unavailable in the supplied HPA summary, so the cross-tissue interpretation should not be treated as protein-level confirmation in bone.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrion | 0.00243 | ALDH18A1, CMC1, DIABLO, ECI1, ETFA, HSD17B10, MRRF, MTHFD1L, NFU1, OCIAD2, PCK2, PTPMT1, RAB32, SLC25A10, SPRYD4, SUCLG1, TACO1, YARS2 |
| GO:CC mitochondrial matrix | 0.0104 | ALDH18A1, CMC1, ECI1, ETFA, HSD17B10, MRRF, MTHFD1L, NFU1, PCK2, SUCLG1, YARS2 |
| GO:BP fatty acid catabolic process | 0.023 | ECI1, ETFA, HSD17B10, HSD17B4, PCK2 |
| GO:BP monocarboxylic acid catabolic process | 0.0492 | ECI1, ETFA, HSD17B10, HSD17B4, PCK2 |

### STRING and hu.MAP

STRING provides a small set of high-confidence known relationships within the module. The most compelling connections are ECI1 with ETFA, ECI1 with HSD17B10, and ETFA with SUCLG1. These relationships independently reinforce the mitochondrial fatty-acid oxidation and central-energy-metabolism interpretation, but they connect only a minority of the module and do not explain the entire co-abundance structure. STRING functional enrichment (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.00051) (STRING Keyword Mitochondrion; within-query FDR = 0.003) (STRING Component Mitochondrion; within-query FDR = 0.0069) also supports mitochondrial localization, but it is supplementary and should not be treated as globally corrected enrichment. hu.MAP shows partial membership in several mitochondrial or mitochondrial-translation-related complexes. MRRF and NFU1 co-occur in multiple hu.MAP complexes (hu.MAP huMAP3_02052.1) and (hu.MAP huMAP3_12054.1), while ALDH18A1, PCK2, and MTHFD1L occur together in (hu.MAP huMAP3_13468.1), and additional partial complex membership involves ALDH18A1 with MTHFD1L (hu.MAP huMAP3_10525.1) and SLC25A10 with YARS2 (hu.MAP huMAP3_06550.1) (hu.MAP huMAP3_07939.1) (hu.MAP huMAP3_08458.1) (hu.MAP huMAP3_09113.1) (hu.MAP huMAP3_09483.1) (hu.MAP huMAP3_06589.1). These observations indicate that portions of the module overlap known molecular systems, especially mitochondrial translation, iron-sulfur biology, metabolic enzymes, and mitochondrial ribosome-associated machinery. However, many module genes lack STRING partners or hu.MAP complex assignments in the supplied data, so the module is not simply a single established physical complex.

**STRING interactions (score >= 0.7)**: 3 of 378 gene pairs: ECI1–ETFA (0.72); ECI1–HSD17B10 (0.729); ETFA–SUCLG1 (0.956)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Mitochondrion (FDR = 0.00051, 16 genes); Keyword Mitochondrion (FDR = 0.003, 14 genes); Component Mitochondrion (FDR = 0.0069, 16 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (ALDH18A1, PCK2, MTHFD1L; 3/99); huMAP3_02052.1 (MRRF, NFU1; 2/2); huMAP3_12054.1 (MRRF, NFU1; 2/8); huMAP3_10525.1 (ALDH18A1, MTHFD1L; 2/33); huMAP3_06550.1 (SLC25A10, YARS2; 2/62); huMAP3_07939.1 (SLC25A10, YARS2; 2/68); huMAP3_08458.1 (SLC25A10, YARS2; 2/70); huMAP3_09113.1 (SLC25A10, YARS2; 2/72); huMAP3_09483.1 (SLC25A10, YARS2; 2/74); huMAP3_06589.1 (SLC25A10, YARS2; 2/79)

### Novelty

The mitochondrial and fatty-acid-metabolism interpretation is biologically established rather than wholly new, because the relevant genes, pathways, STRING links, and hu.MAP complexes are already documented. What may be novel is the conserved co-abundance module linking this particular set of mitochondrial, metabolic, membrane-trafficking, and stress-related genes across bone and ovary. The sparse overlap with known STRING interactions and the partial rather than complete overlap with hu.MAP complexes are consistent with a potentially new systems-level association, but they do not prove novelty. Absence of an interaction from STRING or hu.MAP can reflect incomplete coverage, context dependence, tissue-specific regulation, or an indirect co-abundance relationship. The appropriate conclusion is that the module may represent a new cross-tissue co-abundance pattern built from partly known biology, requiring independent replication and experimental testing.

**Hypothesis.** Hypothesis: bone and ovary share a regulated mitochondrial metabolic state in which fatty-acid oxidation, mitochondrial electron transfer, metabolite exchange, mitochondrial translation, and mitochondrial quality control rise and fall together. In this model, ETFA and ECI1 support electron handling and unsaturated-fatty-acid oxidation, SUCLG1 links oxidative metabolism to succinate and nucleotide-energy production, HSD17B4 contributes peroxisomal fatty-acid processing, and MRRF and MTHFD1L support mitochondrial translation and one-carbon metabolism. The co-abundance signal could arise from coordinated metabolic demand in a shared stromal, epithelial, vascular, or reproductive-cell context, or from variation in mitochondrial content. RAB32, VAMP7, SYNGR2, and related trafficking genes suggest that organelle-associated transport or vesicle biology may accompany this metabolic state, but that connection remains a hypothesis rather than an established mechanism. Testing should include cell-type-resolved replication, mitochondrial-content measurements, fatty-acid oxidation assays, and perturbation of representative metabolic and mitochondrial-translation genes.

### Important genes

#### ETFA

- **Related proteins** (co-abundance neighbors): RRBP1 (0.82), RAB32 (0.81), MTHFD1L (0.81); STRING partners: ECI1 (0.72), SUCLG1 (0.956)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: electron transfer flavoprotein subunit alpha. ETFA participates in catalyzing the initial step of the mitochondrial fatty acid beta-oxidation. It shuttles electrons between primary flavoprotein dehydrogenases and the membrane-bound electron transfer flavoprotein ubiquinone oxidoreductase. Defects in electron-transfer-flavoprotein have been implicated in type II glutaricaciduria in which multiple acyl-CoA dehydrogenase deficiencies result in l…
- **Diseases (Open Targets)**: multiple acyl-CoA dehydrogenase deficiency (0.834); glutaric aciduria (0.756); hereditary disease (0.469); multiple acyl-CoA dehydrogenase deficiency, mild type (0.370); multiple acyl-CoA dehydrogenase deficiency, severe neonatal type (0.370)
- **Europe PMC papers**: 1433
- **Why important**: ETFA is a central metabolic anchor because it participates in mitochondrial electron transfer during fatty-acid beta-oxidation and appears in all globally corrected terms (4 globally significant GO/KEGG terms, q_global 0.00243–0.0492; see the table). It has a direct STRING relationship with ECI1 and a particularly strong relationship with SUCLG1, providing some of the clearest known molecular support inside the module. Its HPA profile includes mitochondrial protein detection in ovary and enrichment in liver and tongue, while its disease associations include multiple acyl-CoA dehydrogenase deficiency and glutaric aciduria. Its literature volume is substantial, consistent with a well-established metabolic role.
- **Conclusion**: Established evidence supports ETFA as a core mitochondrial fatty-acid oxidation and electron-transfer component of the module. It is a strong candidate for a functional driver or readout of the shared metabolic state, although co-abundance alone does not establish that ETFA regulates the other genes.

#### ECI1

- **Related proteins** (co-abundance neighbors): SUCLG1 (0.83); STRING partners: ETFA (0.72), HSD17B10 (0.729)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: enoyl-CoA delta isomerase 1. This gene encodes a member of the hydratase/isomerase superfamily. The protein encoded is a key mitochondrial enzyme involved in beta-oxidation of unsaturated fatty acids. It catalyzes the transformation of 3-cis and 3-trans-enoyl-CoA esters arising during the stepwise degradation of cis-, mono-, and polyunsaturated fatty acids to the 2-trans-enoyl-CoA intermediates. Alternatively spliced transcri…
- **Diseases (Open Targets)**: metabolic syndrome (0.075); posterior cortical atrophy (0.022); neoplasm (0.021); systemic sclerosis (0.015); pemphigus foliaceus (0.015)
- **Europe PMC papers**: 655
- **Why important**: ECI1 is directly annotated to mitochondrial beta-oxidation of unsaturated fatty acids and appears in (4 globally significant GO/KEGG terms, q_global 0.00243–0.0492; see the table). It forms STRING relationships with ETFA and HSD17B10, connecting the fatty-acid oxidation arm of the module to both electron transfer and steroid or lipid metabolism. It is detected in ovary by HPA and is enriched in hepatocytes, fitting the broader metabolic composition of the module. Its disease and literature evidence is less extensive than for some other selected genes, but its biochemical specificity makes it particularly informative.
- **Conclusion**: Established evidence identifies ECI1 as a plausible biochemical core of the fatty-acid catabolic signal. Its position within the known STRING-supported metabolic subnetwork makes it a useful candidate for testing whether the module reflects altered unsaturated-fatty-acid oxidation.

#### SUCLG1

- **Related proteins** (co-abundance neighbors): DHRS7 (0.85), ECI1 (0.83), SYNGR2 (0.82); STRING partners: ETFA (0.956)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase GDP/ADP-forming subunit alpha. This gene encodes the alpha subunit of the heterodimeric enzyme succinate coenzyme A ligase. This enzyme is targeted to the mitochondria and catalyzes the conversion of succinyl CoA and ADP or GDP to succinate and ATP or GTP. Mutations in this gene are the cause of the metabolic disorder fatal infantile lactic acidosis and mitochondrial DNA depletion. [provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome 9 (0.811); neurodegenerative disease (0.520); mitochondrial DNA depletion syndrome (0.507); post term pregnancy (0.280); lysosomal storage disease (0.245)
- **Europe PMC papers**: 1277
- **Why important**: SUCLG1 links the module to the tricarboxylic-acid cycle and succinyl-CoA metabolism and appears in the mitochondrial terms (GO:CC mitochondrion; q_global = 0.00243) and (GO:CC mitochondrial matrix; q_global = 0.0104). It is connected to ETFA by STRING and is positioned within the module near DHRS7, ECI1, and SYNGR2. HPA reports mitochondrial localization and ovary protein detection. Its disease associations include mitochondrial DNA depletion syndromes, and it has a large literature base, making it one of the best-established genes for interpreting the module's energy-metabolism component.
- **Conclusion**: Established evidence supports SUCLG1 as a bridge between fatty-acid-linked electron metabolism and the tricarboxylic-acid cycle. Its inclusion strengthens the interpretation that the module reflects coordinated mitochondrial energy metabolism rather than isolated fatty-acid enzymes.

#### HSD17B4

- **Related proteins** (co-abundance neighbors): OCIAD2 (0.87), YARS2 (0.83), CMC1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Peroxisomes; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydroxysteroid 17-beta dehydrogenase 4. The protein encoded by this gene is a bifunctional enzyme that is involved in the peroxisomal beta-oxidation pathway for fatty acids. It also acts as a catalyst for the formation of 3-ketoacyl-CoA intermediates from both straight-chain and 2-methyl-branched-chain fatty acids. Defects in this gene that affect the peroxisomal fatty acid beta-oxidation activity are a cause of D-bifunctional protein d…
- **Diseases (Open Targets)**: d-bifunctional protein deficiency (0.830); Perrault syndrome 1 (0.761); Perrault syndrome (0.736); hereditary disease (0.488); hearing loss disorder (0.370)
- **Europe PMC papers**: 1624
- **Why important**: HSD17B4 is one of the clearest representatives of the fatty-acid catabolic signal because it appears in (GO:BP fatty acid catabolic process; q_global = 0.023) and (GO:BP monocarboxylic acid catabolic process; q_global = 0.0492) and encodes a bifunctional enzyme in peroxisomal beta-oxidation. It also participates in steroid and estrogen metabolism, which is relevant to ovary biology. Within the module it connects to OCIAD2, YARS2, and CMC1, while HPA places it in peroxisomes and reports liver enrichment. Its disease associations include D-bifunctional protein deficiency and Perrault syndrome, and its literature volume is substantial.
- **Conclusion**: Established evidence supports HSD17B4 as a peroxisomal fatty-acid and steroid-metabolism component that complements the mitochondrial signal. Its presence suggests that the module may coordinate fatty-acid handling across organelles, but cross-organelle coordination remains a hypothesis.

#### MRRF

- **Related proteins** (co-abundance neighbors): SYNGR2 (0.88), PPIC (0.83), OCIAD2 (0.83), RAB32 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules, Cytokinetic bridge; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_02052.1, huMAP3_12054.1
- **Function (MyGene.info)**: mitochondrial ribosome recycling factor. This gene encodes a ribosome recycling factor, which is a component of the mitochondrial translational machinery. The encoded protein, along with mitochondrial elongation factor 2, functions in ribosomal recycling at the termination of mitochondrial translation by mediating the disassembly of ribosomes from messenger RNA. A pseudogene of this gene has been identified on chromosome X. [provided by …
- **Diseases (Open Targets)**: neurodegenerative disease (0.415); ocular hypotension (0.173); myoepithelial tumor (0.111); deficiency anemia (0.101); squamous cell lung carcinoma (0.038)
- **Europe PMC papers**: 170
- **Why important**: MRRF is a mitochondrial ribosome recycling factor and appears in (GO:CC mitochondrion; q_global = 0.00243) and (GO:CC mitochondrial matrix; q_global = 0.0104), as well as all supplementary STRING mitochondrial terms. It has a relatively central position in the module, connecting SYNGR2, PPIC, OCIAD2, and RAB32. hu.MAP places MRRF with NFU1 in multiple complexes (hu.MAP huMAP3_02052.1) and (hu.MAP huMAP3_12054.1), providing complex-level support beyond the enrichment results. HPA reports ovary protein detection, and its disease associations include neurodegenerative disease and deficiency anemia.
- **Conclusion**: Established evidence supports MRRF as a mitochondrial translation and ribosome-recycling component that may report the organelle's capacity to maintain respiratory and metabolic proteins. Its co-abundance with metabolic genes supports a coordinated mitochondrial-state interpretation, but does not prove direct regulation between translation and fatty-acid oxidation.

#### MTHFD1L

- **Related proteins** (co-abundance neighbors): PTPMT1 (0.84), ETFA (0.81), VAMP7 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1
- **Function (MyGene.info)**: methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 1 like. The protein encoded by this gene is involved in the synthesis of tetrahydrofolate (THF) in the mitochondrion. THF is important in the de novo synthesis of purines and thymidylate and in the regeneration of methionine from homocysteine. Several transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Jun 2011].
- **Diseases (Open Targets)**: Alzheimer disease (0.343); Abnormality of refraction (0.315); refractive error (0.312); COVID-19 (0.296); severe acute respiratory syndrome (0.295)
- **Europe PMC papers**: 1180
- **Why important**: MTHFD1L appears in the mitochondrial terms (GO:CC mitochondrion; q_global = 0.00243) and (GO:CC mitochondrial matrix; q_global = 0.0104) and encodes a mitochondrial enzyme involved in tetrahydrofolate and formate metabolism. It occupies a connected position with PTPMT1, ETFA, and VAMP7 and participates in hu.MAP complexes (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1). HPA reports ovary protein detection and enrichment in blood vessel contexts, with single-cell enhancement in several vascular, placental, and neural-associated cell types. Its disease associations include Alzheimer disease and disorders of refraction, and its literature volume is substantial.
- **Conclusion**: Established evidence supports MTHFD1L as a mitochondrial one-carbon-metabolism component that broadens the module beyond fatty-acid oxidation. It may connect mitochondrial biosynthetic capacity with energetic demand in bone and ovary, but that integrative role is a hypothesis requiring metabolic flux evidence.

## Module 9

**Tissue pair**: bone and ovary  
**Genes (9)**: CCAR1, NUP98, RBM15, POLR1A, SMARCA4, U2SURP, VIRMA, WDR33, ZC3HAV1

### Function

The strongest supported interpretation is a conserved nuclear RNA and gene-expression regulatory module. Every module gene contributes to the globally significant GO biological-process term for RNA metabolic process (GO:BP RNA metabolic process; q_global = 0.0203), and every module gene also contributes to the globally significant molecular-function term for nucleic acid binding (GO:MF nucleic acid binding; q_global = 0.0292). The genes span RNA processing and methylation, alternative polyadenylation, RNA export and nucleocytoplasmic transport, ribosomal RNA transcription, chromatin remodeling, and RNA surveillance. This combination suggests coordinated regulation of RNA production, maturation, processing, and cellular handling rather than a pathway restricted to one biochemical reaction. The STRING RNA-binding and nucleic-acid-binding enrichments (STRING Function Nucleic acid binding; within-query FDR = 0.0268)(STRING Function RNA binding; within-query FDR = 0.0447) support this interpretation but are supplementary, not independent global enrichment evidence. No primary KEGG term is listed.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity and low immune-cell specificity, which is consistent with broadly used intracellular machinery rather than a tissue-restricted secretory program. Bone-marrow enhancement occurs for a subset, and cell-type enhancement or enrichment includes neutrophils, NK-cells, plasmacytoid dendritic cells, and endometrial cell populations. However, the overall blood-cell specificity is low, and POLR1A is not detected in immune cells. Thus, a blood or immune-cell explanation is possible for part of the signal but is not sufficient to explain the whole module. Protein detection in ovary is reported for most genes, whereas matching bone protein data are unavailable, so the apparent bone-ovary conservation should not be interpreted as proof of bone-specific protein expression.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA metabolic process | 0.0203 | CCAR1, NUP98, POLR1A, RBM15, SMARCA4, U2SURP, VIRMA, WDR33, ZC3HAV1 |
| GO:MF nucleic acid binding | 0.0292 | CCAR1, NUP98, POLR1A, RBM15, SMARCA4, U2SURP, VIRMA, WDR33, ZC3HAV1 |

### STRING and hu.MAP

The module is sparse at the high-confidence STRING threshold. The directly supported STRING relationships are CCAR1 with U2SURP and RBM15 with VIRMA; the RBM15-VIRMA relationship is especially strong in the supplied evidence. hu.MAP provides one complex-level connection containing U2SURP and CCAR1, with many additional complex members outside this module. These observations establish that parts of the module overlap known RNA-associated or multiprotein machinery. They do not establish one complete physical complex containing all module genes. The remaining co-abundance links are therefore more plausibly interpreted as coordinated activity, shared regulation, or indirect functional coupling unless independently validated.

**STRING interactions (score >= 0.7)**: 2 of 36 gene pairs: CCAR1–U2SURP (0.742); RBM15–VIRMA (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Nucleic acid binding (FDR = 0.0268, 9 genes); Function RNA binding (FDR = 0.0447, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10359.1 (U2SURP, CCAR1; 2/27)

### Novelty

This may be a novel tissue-pair co-abundance observation, but the fact sheet does not justify calling it a newly discovered molecular complex or pathway. The module combines established RNA-processing, RNA-surveillance, transcriptional, chromatin, and nuclear-transport genes, while only selected relationships are already represented by high-confidence STRING or hu.MAP evidence. The absence of other relationships from those resources cannot prove novelty, because database coverage, assay context, and detection thresholds are incomplete. The most defensible novelty claim is therefore that coordinated abundance of this particular gene set across bone and ovary may be new and merits replication, while its constituent biology is largely established.

**Hypothesis.** Hypothesis: the shared bone-ovary module reflects a conserved nuclear gene-expression state in which RNA synthesis, RNA maturation, RNA modification, RNA export, and chromatin accessibility are coordinated. A plausible mechanistic core is coupling between the RBM15-VIRMA RNA-modification axis, the U2SURP-centered RNA-processing neighborhood, WDR33-linked three-prime RNA handling, NUP98-mediated nuclear transport, POLR1A-dependent ribosomal RNA production, and SMARCA4- and CCAR1-associated transcriptional control. ZC3HAV1 may connect this state to RNA quality control and antiviral RNA decay. This is a mechanistic hypothesis, not a demonstrated physical assembly; perturbation and orthogonal protein-interaction or activity measurements would be required to test it.

### Important genes

#### U2SURP

- **Related proteins** (co-abundance neighbors): RBM15 (0.86), WDR33 (0.84), VIRMA (0.80); STRING partners: CCAR1 (0.742)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_10359.1
- **Function (MyGene.info)**: U2 snRNP associated SURP domain containing. Enables RNA binding activity. Predicted to be involved in RNA processing. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dengue disease (0.370); arthropathy (0.277); neurodegenerative disease (0.264); alcohol drinking (0.244); Hypercholesterolemia (0.207)
- **Europe PMC papers**: 228
- **Why important**: U2SURP has the strongest weighted connectivity in the module and links RBM15, WDR33, and VIRMA. It is annotated for RNA binding and RNA processing, appears in both primary terms (GO:BP RNA metabolic process; q_global = 0.0203)(GO:MF nucleic acid binding; q_global = 0.0292) and both supplementary STRING terms (STRING Function Nucleic acid binding; within-query FDR = 0.0268)(STRING Function RNA binding; within-query FDR = 0.0447), and also participates in the hu.MAP complex with CCAR1 (hu.MAP huMAP3_10359.1). Its literature volume is comparatively modest relative to several other module genes, making its central network position especially informative.
- **Conclusion**: Established evidence supports U2SURP as a central RNA-processing component and a bridge between several module neighborhoods. It is a strong candidate for an organizing node, but the co-abundance data do not prove that it physically binds every linked gene product.

#### RBM15

- **Related proteins** (co-abundance neighbors): ZC3HAV1 (0.88), U2SURP (0.86); STRING partners: VIRMA (0.999)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 15. Members of the SPEN (Split-end) family of proteins, including RBM15, have repressor function in several signaling pathways and may bind to RNA through interaction with spliceosome components (Hiriart et al., 2005 [PubMed 16129689]).[supplied by OMIM, Feb 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); lung adenocarcinoma (0.219); esophageal squamous cell carcinoma (0.209); osteosarcoma (0.209); hepatocellular carcinoma (0.206)
- **Europe PMC papers**: 3897
- **Why important**: RBM15 is connected to U2SURP and ZC3HAV1 and has a high-confidence STRING relationship with VIRMA. Its annotations include RNA binding, RNA methylation, alternative splicing regulation, and regulation of myeloid and megakaryocyte differentiation. It contributes to both primary terms (GO:BP RNA metabolic process; q_global = 0.0203)(GO:MF nucleic acid binding; q_global = 0.0292) and both supplementary terms (STRING Function Nucleic acid binding; within-query FDR = 0.0268)(STRING Function RNA binding; within-query FDR = 0.0447), has bone-marrow enhancement, and has a substantial literature supporting broad relevance to RNA regulation and disease.
- **Conclusion**: Established evidence supports RBM15 as a biologically meaningful RNA-regulatory anchor that could connect RNA modification with cell-state regulation. Its role as a causal bridge between the bone and ovary co-abundance patterns remains a hypothesis.

#### VIRMA

- **Related proteins** (co-abundance neighbors): NUP98 (0.83), U2SURP (0.80); STRING partners: RBM15 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vir like m6A methyltransferase associated. Enables RNA binding activity. Involved in mRNA alternative polyadenylation and mRNA methylation. Located in cytosol and nuclear speck. Colocalizes with RNA N6-methyladenosine methyltransferase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: smoking initiation (0.355); Abnormality of the skeletal system (0.355); obesity disorder (0.344); orofacial cleft (0.256); cleft palate (0.221)
- **Europe PMC papers**: 1994
- **Why important**: VIRMA is linked to RBM15 through STRING and to U2SURP and NUP98 in the module. It is annotated for mRNA methylation and alternative polyadenylation, contributes to both primary terms (GO:BP RNA metabolic process; q_global = 0.0203)(GO:MF nucleic acid binding; q_global = 0.0292) and both supplementary terms (STRING Function Nucleic acid binding; within-query FDR = 0.0268)(STRING Function RNA binding; within-query FDR = 0.0447), and is located in nuclear bodies. Its disease and trait associations and literature volume indicate that it is a well-established regulator with relevance beyond this module.
- **Conclusion**: Established evidence supports VIRMA as a key RNA-modification and mRNA-processing component. The module suggests coordinated activity with RBM15 and U2SURP, but does not demonstrate that this coordination is specific to bone and ovary.

#### ZC3HAV1

- **Related proteins** (co-abundance neighbors): POLR1A (0.89), RBM15 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger CCCH-type containing, antiviral 1. This gene encodes a CCCH-type zinc finger protein. This antiviral protein inhibits viral replication by recruiting cellular RNA degradation machineries to degrade viral mRNAs. The encoded protein plays an important role in the innate immune response against multiple DNA and RNA viruses, including Ebola virus, HIV and SARS-CoV-2 (which causes COVID-19). [provided by RefSeq, Sep 2021].
- **Diseases (Open Targets)**: cancer (0.549); hypothyroidism (0.429); neurodegenerative disease (0.358); autoimmune disease (0.308); Hashimoto thyroiditis (0.306)
- **Europe PMC papers**: 979
- **Why important**: ZC3HAV1 connects POLR1A and RBM15 and contributes to both primary terms (GO:BP RNA metabolic process; q_global = 0.0203)(GO:MF nucleic acid binding; q_global = 0.0292) and both supplementary terms (STRING Function Nucleic acid binding; within-query FDR = 0.0268)(STRING Function RNA binding; within-query FDR = 0.0447). Its established annotations include antiviral RNA degradation, RNA catabolism, and innate immune signaling. HPA describes bone-marrow enhancement and enrichment or enhancement in several immune-related and endometrial cell populations. Its literature volume is substantial, and it provides the clearest route by which the module could reflect RNA surveillance or cellular stress.
- **Conclusion**: Established evidence supports ZC3HAV1 as an RNA-quality-control and antiviral-response factor. Its inclusion may indicate a surveillance component, but the HPA pattern does not establish that immune-cell abundance is the primary source of the shared module.

#### WDR33

- **Related proteins** (co-abundance neighbors): U2SURP (0.84), CCAR1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 33. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.515); dengue disease (0.370); smoking initiation (0.292); connective tissue disorder (0.236); arthropathy (0.149)
- **Europe PMC papers**: 508
- **Why important**: WDR33 is connected to U2SURP and CCAR1 and contributes to both primary terms (GO:BP RNA metabolic process; q_global = 0.0203)(GO:MF nucleic acid binding; q_global = 0.0292) and both supplementary terms (STRING Function Nucleic acid binding; within-query FDR = 0.0268)(STRING Function RNA binding; within-query FDR = 0.0447). Its annotations include mRNA three-prime-end processing and formation of multiprotein complexes through WD repeats. It has low tissue and cell-type specificity, supporting a broadly applicable RNA-processing role rather than a secreted or strongly tissue-restricted function.
- **Conclusion**: Established evidence supports WDR33 as a structural or assembly-related component of RNA-processing machinery. Its position supports integration of RNA maturation into the module, while any direct functional partnership with U2SURP or CCAR1 remains to be tested.

#### SMARCA4

- **Related proteins** (co-abundance neighbors): CCAR1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center, Nucleoli rim; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SWI/SNF related BAF chromatin remodeling complex subunit ATPase 4. The protein encoded by this gene is a member of the SWI/SNF family of proteins and is similar to the brahma protein of Drosophila. Members of this family have helicase and ATPase activities and are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI, wh…
- **Diseases (Open Targets)**: intellectual disability, autosomal dominant 16 (0.796); rhabdoid tumor predisposition syndrome 2 (0.788); familial rhabdoid tumor (0.685); rhabdoid tumor (0.627); medulloblastoma (0.586)
- **Europe PMC papers**: 9906
- **Why important**: SMARCA4 connects to CCAR1 and contributes to both primary terms (GO:BP RNA metabolic process; q_global = 0.0203)(GO:MF nucleic acid binding; q_global = 0.0292) and both supplementary terms (STRING Function Nucleic acid binding; within-query FDR = 0.0268)(STRING Function RNA binding; within-query FDR = 0.0447). It is the module's clearest chromatin-remodeling and transcriptional regulator, with established roles in ATP-dependent chromatin remodeling and transcriptional control. It has extensive literature and major disease associations, making it an important candidate for linking chromatin state to the RNA-processing program.
- **Conclusion**: Established evidence supports SMARCA4 as a chromatin and transcriptional regulator that could influence the expression of the rest of the module. Its connection to the RNA-processing state is biologically plausible but remains a module-level hypothesis rather than a demonstrated direct mechanism.

## Module 10

**Tissue pair**: bone and ovary  
**Genes (5)**: CLIP1, HBS1L, CAST, MYH14, PSME3IP1

### Function

This module does not support a single significantly enriched GO or KEGG function: no GO/KEGG term passed global correction. The gene annotations instead indicate a mixed cellular program involving translation quality control and rescue of stalled ribosomes through HBS1L, microtubule organization and vesicle linkage through CLIP1, actin-dependent motor and cell-shape functions through MYH14, calcium-dependent protease regulation through CAST, and nuclear regulation of protein binding, proteasomal protein catabolism, and mRNA splicing through PSME3IP1. The co-abundance structure is therefore more consistent with shared cellular state, structural organization, or cell-type composition than with a demonstrated canonical pathway. The absence of significant enrichment does not invalidate the module.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins: none of the genes is annotated as secreted. It is also not blood-cell enriched according to HPA: most genes have low immune-cell specificity and one is not detected in immune cells, while no enriched blood-cell category was reported. The composition is heterogeneous. Several genes have low tissue specificity, whereas others are enhanced in skeletal muscle or intestine. All genes show cell-type enhancement, including epithelial, muscle, reproductive, and erythrocyte-progenitor contexts. This pattern suggests that the shared bone and ovary signal could partly reflect common cellular or sample-composition effects, especially structural or epithelial-like cell states, rather than a bone-and-ovary-specific secreted program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes, no STRING functional enrichment, and no hu.MAP complex containing multiple module members. Thus, the co-abundance edges should not be interpreted as established physical interactions or as membership in a known multiprotein complex. The strongest network position belongs to HBS1L, which connects to CAST, MYH14, and CLIP1. CLIP1 connects HBS1L to PSME3IP1, while CAST and MYH14 form separate single-neighbor branches. This topology may identify a coordinated expression pattern, but the external interaction resources provide no independent support for a unified molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a new data-derived co-abundance pattern because it is not represented by a matching STRING interaction network, STRING enrichment result, or hu.MAP complex. However, those absences do not prove biological novelty. The individual genes and their functions are established, and the module could arise from shared cell composition, correlated expression, or a context-dependent state that is not captured by interaction databases. The defensible conclusion is that the bone-and-ovary co-abundance combination is insufficiently characterized by the supplied reference resources, not that a new molecular pathway has been demonstrated.

**Hypothesis.** Hypothesis: the module reflects a coordinated cellular maintenance and architecture state in which HBS1L-linked translational quality control is correlated with microtubule organization through CLIP1, actin-dependent shape or contractile processes through MYH14, protease restraint through CAST, and nuclear control of protein handling and RNA processing through PSME3IP1. In bone and ovary, this signal may arise from shared structural, epithelial, muscle-like, or other specialized cell populations rather than from a dedicated bone-ovary pathway. This hypothesis requires validation by cell-resolved expression, replication in independent cohorts, and perturbation or protein-level experiments.

### Important genes

#### HBS1L

- **Related proteins** (co-abundance neighbors): CAST (0.82), MYH14 (0.82), CLIP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HBS1 like translational GTPase. This gene encodes a member of the GTP-binding elongation factor family. It is expressed in multiple tissues with the highest expression in heart and skeletal muscle. The intergenic region of this gene and the MYB gene has been identified to be a quantitative trait locus (QTL) controlling fetal hemoglobin level, and this region influnces erythrocyte, platelet, and monocyte counts as well as erythro…
- **Diseases (Open Targets)**: Hypercholesterolemia (0.445); sickle cell disease (0.439); deficiency anemia (0.433); metabolic disease (0.415); anemia (phenotype) (0.413)
- **Europe PMC papers**: 960
- **Why important**: HBS1L is the central network gene, connecting CAST, MYH14, and CLIP1. Its established annotation as a translational GTPase involved in ribosome disassembly, rescue of stalled cytosolic ribosomes, and mRNA quality control gives it the clearest candidate role in cellular proteome maintenance. It is broadly expressed with high expression reported in heart and skeletal muscle, has links to erythrocyte-related traits and anemia-associated phenotypes, and has substantial literature coverage.
- **Conclusion**: Established evidence supports HBS1L as the network hub and a regulator of translation quality control. It is not established that HBS1L drives the bone-and-ovary module or directly interacts with the other module proteins; that interpretation remains a hypothesis.

#### CLIP1

- **Related proteins** (co-abundance neighbors): PSME3IP1 (0.90), HBS1L (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Microtubule ends, Mid piece; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CAP-Gly domain containing linker protein 1. The protein encoded by this gene links endocytic vesicles to microtubules. This gene is highly expressed in Reed-Sternberg cells of Hodgkin disease. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011].
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.575); cancer (0.531); melanocytic neoplasm (0.370); spitz nevus (0.370); autosomal recessive non-syndromic intellectual disability (0.370)
- **Europe PMC papers**: 786
- **Why important**: CLIP1 occupies the bridge position between HBS1L and PSME3IP1. Its established function in linking endocytic vesicles to microtubules and promoting microtubule organization provides a plausible structural connection within an otherwise heterogeneous module. HPA reports tissue enhancement in skeletal muscle and cell-type enhancement in epithelial, muscle, and placental contexts. It also has substantial disease and cancer literature.
- **Conclusion**: Established evidence supports CLIP1 as a microtubule-end and vesicle-organizing protein with an important bridging position in the co-abundance graph. A direct mechanistic connection between its cytoskeletal function and HBS1L or PSME3IP1 is not established by the supplied STRING or hu.MAP evidence.

#### MYH14

- **Related proteins** (co-abundance neighbors): HBS1L (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin heavy chain 14. This gene encodes a member of the myosin superfamily. The protein represents a conventional non-muscle myosin; it should not be confused with the unconventional myosin-14 (MYO14). Myosins are actin-dependent motor proteins with diverse functions including regulation of cytokinesis, cell motility, and cell polarity. Mutations in this gene result in one form of autosomal dominant hearing impairment.…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 4A (0.736); peripheral neuropathy-myopathy-hoarseness-hearing loss syndrome (0.585); autosomal dominant nonsyndromic hearing loss (0.479); sensorineural hearing loss disorder (0.365); nonsyndromic genetic hearing loss (0.342)
- **Europe PMC papers**: 1724
- **Why important**: MYH14 is one of the two genes directly connected to the HBS1L hub and contributes a distinct cytoskeletal branch. It encodes a conventional non-muscle myosin involved in actin-dependent motor activity, cytokinesis, cell shape, and tissue development. Its tissue enhancement in intestine and skeletal muscle, absence from immune cells, and strong association with inherited hearing-loss disorders make it biologically informative for interpreting the module as a structural or cell-state signal.
- **Conclusion**: Established evidence supports MYH14 as a cell-shape and actin-motor component whose expression may mark specialized structural cells. Its presence does not establish that the module regulates bone or ovary mechanics, and the proposed linkage to translational quality control is hypothetical.

#### CAST

- **Related proteins** (co-abundance neighbors): HBS1L (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calpastatin
- **Diseases (Open Targets)**: peeling skin-leukonuchia-acral punctate keratoses-cheilitis-knuckle pads syndrome (0.688); Alzheimer disease (0.387); Bart-Pumphrey syndrome (0.378); cheilitis (0.373); punctate palmoplantar keratoderma (0.370)
- **Europe PMC papers**: 46701
- **Why important**: CAST is directly connected to the HBS1L hub and represents a regulatory branch distinct from the cytoskeletal genes. Its established identity as calpastatin indicates regulation of calpain proteolysis. HPA places it in endoplasmic-reticulum and cytosolic compartments and reports epithelial cell-type enhancement. CAST also has extensive literature and multiple disease associations, making it a useful candidate for follow-up despite its peripheral network position.
- **Conclusion**: Established evidence supports CAST as a proteolysis-regulating protein that may reflect cellular stress, remodeling, or epithelial state. A role for CAST in organizing this specific bone-and-ovary module is not established, and its connection to HBS1L is based on co-abundance rather than a documented physical interaction.

#### PSME3IP1

- **Related proteins** (co-abundance neighbors): CLIP1 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome activator subunit 3 interacting protein 1. Involved in negative regulation of proteasomal protein catabolic process and negative regulation of protein binding activity. Located in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.074); osteoporosis (0.060); arthritic joint disease (0.026); placenta praevia (0.022); Alzheimer disease (0.011)
- **Europe PMC papers**: 18
- **Why important**: PSME3IP1 is the terminal member of the CLIP1 branch and adds a nuclear protein-homeostasis and RNA-processing perspective. Its reported functions include negative regulation of proteasomal protein catabolism, regulation of protein binding, and spliceosomal mRNA processing. It is cell-type enhanced in spermatids and is not detected in ovary by the supplied HPA immunohistochemistry result. Its literature base is limited compared with the other selected genes, which makes it both a potentially informative and relatively under-characterized component.
- **Conclusion**: Established evidence supports PSME3IP1 as a nuclear regulator associated with RNA processing and protein handling. Its low literature volume and lack of supporting STRING or hu.MAP relationships mean that any role as a driver or mechanistic connector in the module remains speculative.

## Module 11

**Tissue pair**: bone and ovary  
**Genes (5)**: DDX56, HEATR1, PES1, UTP4, WDR12

### Function

The module is a coherent nucleolar ribosome-biogenesis program. All five genes occur in the globally significant rRNA-processing, rRNA-metabolic-process, ribosome-biogenesis, ribonucleoprotein-complex-biogenesis, nucleolar, and RNA-processing terms (GO:BP rRNA processing; q_global = 0.000341), (GO:BP rRNA metabolic process; q_global = 0.000629), (GO:BP ribosome biogenesis; q_global = 0.00104), (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.00357), (GO:CC nucleolus; q_global = 0.0411), (GO:BP RNA processing; q_global = 0.0451). HEATR1, PES1, UTP4, and WDR12 support the 90S preribosome (GO:CC 90S preribosome; q_global = 2.71e-05), (GO:CC preribosome; q_global = 0.00186). HEATR1 and UTP4 support the t-UTP complex (GO:CC t-UTP complex; q_global = 0.0271), while PES1 and WDR12 support the PeBoW complex (GO:CC PeBoW complex; q_global = 0.0271). The best interpretation is coordinated precursor-rRNA maturation and ribosomal-subunit assembly, rather than a specialized bone or ovary pathway. The complete membership in the core rRNA-processing and ribosome-biogenesis terms provides strong functional coherence. Because the module is also a connected co-abundance subgraph with strong STRING relationships throughout, its genes likely reflect a shared nucleolar biosynthetic state, although co-abundance does not prove direct physical binding between every pair.

**Cell composition.** The module is not composed of plasma proteins, secreted proteins, or blood-cell-enriched proteins. HPA reports no secreted genes and low immune-cell specificity for every gene. All genes have low tissue specificity, with no repeatedly enriched tissue in the supplied summary. Individual cell-type enhancements occur in unrelated cell types, including oocytes, epicardial cells, proximal tubule cells, adipocytes, and cardiomyocytes, but this does not indicate a shared blood or immune contaminant. The bone–ovary signal is therefore more consistent with a broadly distributed intracellular nucleolar program than with a plasma-protein or blood-cell module. Ovary protein detection is mixed, and matching bone protein data are unavailable, so the HPA protein evidence does not establish ovary-specific activity. Co-abundance may instead reflect shared cellular biosynthetic state, proliferation, differentiation, or nucleolar activity.

**GO/KEGG enrichment**: 10 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC 90S preribosome | 2.71e-05 | HEATR1, PES1, UTP4, WDR12 |
| GO:BP rRNA processing | 0.000341 | DDX56, HEATR1, PES1, UTP4, WDR12 |
| GO:BP rRNA metabolic process | 0.000629 | DDX56, HEATR1, PES1, UTP4, WDR12 |
| GO:BP ribosome biogenesis | 0.00104 | DDX56, HEATR1, PES1, UTP4, WDR12 |
| GO:CC preribosome | 0.00186 | HEATR1, PES1, UTP4, WDR12 |
| GO:BP ribonucleoprotein complex biogenesis | 0.00357 | DDX56, HEATR1, PES1, UTP4, WDR12 |
| GO:CC t-UTP complex | 0.0271 | HEATR1, UTP4 |
| GO:CC PeBoW complex | 0.0271 | PES1, WDR12 |
| GO:CC nucleolus | 0.0411 | DDX56, HEATR1, PES1, UTP4, WDR12 |
| GO:BP RNA processing | 0.0451 | DDX56, HEATR1, PES1, UTP4, WDR12 |

### STRING and hu.MAP

STRING provides extensive prior support. Every possible gene pair has a strong STRING relationship. STRING assigns the full set to ribosome biogenesis and rRNA processing (STRING Keyword Ribosome biogenesis; within-query FDR = 6.42e-07), (STRING Keyword rRNA processing; within-query FDR = 7.08e-07), (STRING Process rRNA processing; within-query FDR = 0.00053), and links most members to the 90S preribosome (STRING Component 90S preribosome; within-query FDR = 1.58e-05), (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 4.17e-05), (STRING COMPARTMENTS 90S preribosome; within-query FDR = 4.26e-05), nucleolus (STRING COMPARTMENTS Nucleolus; within-query FDR = 0.0018), and rRNA-processing pathway (STRING RCTM Major pathway of rRNA processing in the nucleolus and cytosol; within-query FDR = 0.0044). It supports the t-UTP complex through HEATR1 and UTP4 (STRING Component t-UTP complex; within-query FDR = 0.0115), and the PeBoW complex through PES1 and WDR12 (STRING NetworkNeighborAL PeBoW complex, and rRNA (uridine-2-O-)-methyltransferase activity; within-query FDR = 0.0056), (STRING Component PeBoW complex; within-query FDR = 0.0115), (STRING COMPARTMENTS PeBoW complex; within-query FDR = 0.0123). These are supplementary STRING findings; global enrichment conclusions rely on (GO:CC 90S preribosome; q_global = 2.71e-05) through (GO:BP RNA processing; q_global = 0.0451). No hu.MAP complex contains at least two module members. This absence does not refute the biology because STRING and hu.MAP use different evidence and experimental resources. Overall, the network is strongly supported as a ribosome-biogenesis neighborhood, but its co-abundance edges should not automatically be treated as direct binary interactions.

**STRING interactions (score >= 0.7)**: 10 of 10 gene pairs: DDX56–HEATR1 (0.844); DDX56–PES1 (0.97); DDX56–UTP4 (0.82); DDX56–WDR12 (0.917); HEATR1–PES1 (0.877); HEATR1–UTP4 (0.999); HEATR1–WDR12 (0.908); PES1–UTP4 (0.926); PES1–WDR12 (0.999); UTP4–WDR12 (0.939)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Ribosome biogenesis (FDR = 6.42e-07, 5 genes); Keyword rRNA processing (FDR = 7.08e-07, 5 genes); Component 90S preribosome (FDR = 1.58e-05, 4 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 4.17e-05, 5 genes); COMPARTMENTS 90S preribosome (FDR = 4.26e-05, 4 genes); Process rRNA processing (FDR = 0.00053, 5 genes); COMPARTMENTS Nucleolus (FDR = 0.0018, 5 genes); RCTM Major pathway of rRNA processing in the nucleolus and cytosol (FDR = 0.0044, 4 genes); NetworkNeighborAL Mixed, incl. Preribosome, large subunit precursor, and Maturation of LSU-rRNA (FDR = 0.0046, 3 genes); NetworkNeighborAL PeBoW complex, and rRNA (uridine-2-O-)-methyltransferase activity (FDR = 0.0056, 2 genes); Component Nucleolus (FDR = 0.007, 5 genes); Component t-UTP complex (FDR = 0.0115, 2 genes); Component PeBoW complex (FDR = 0.0115, 2 genes); COMPARTMENTS PeBoW complex (FDR = 0.0123, 2 genes); NetworkNeighborAL Mixed, incl. t-UTP complex, and Pwp2p-containing subcomplex of 90S preribosome (FDR = 0.0146, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The molecular function is not newly discovered: it is established by the globally significant annotations (GO:CC 90S preribosome; q_global = 2.71e-05) through (GO:BP RNA processing; q_global = 0.0451), the STRING evidence (STRING Keyword Ribosome biogenesis; within-query FDR = 6.42e-07) through (STRING NetworkNeighborAL Mixed, incl. t-UTP complex, and Pwp2p-containing subcomplex of 90S preribosome; within-query FDR = 0.0146), and the supplied gene descriptions. Absence of a qualifying hu.MAP complex cannot establish novelty, and database absence alone is not evidence of a new mechanism. The potentially novel observation is the conservation of this particular co-abundance module between bone and ovary in the present dataset. The supplied information does not compare it with published bone–ovary modules, independent cohorts, or prior tissue-pair analyses, so novelty of the exact tissue-pair organization remains unproven. The appropriate conclusion is established ribosome-biogenesis machinery with a potentially novel, but unvalidated, cross-tissue co-abundance pattern.

**Hypothesis.** Hypothesis: the shared bone–ovary module marks coordinated nucleolar biosynthetic capacity. Variation in common cellular composition, growth, differentiation, stress, or translational demand may synchronously regulate early preribosome production and later ribosomal-subunit maturation. The HEATR1–UTP4 arm may contribute to early precursor-rRNA processing, whereas the PES1–WDR12 arm may contribute to large-subunit maturation, with DDX56 providing RNA-remodeling activity. This assembly-line interpretation is a hypothesis. The supplied evidence establishes co-abundance and annotation, but not directionality, causality, tissue-specific regulation, or altered ribosome output.

### Important genes

#### PES1

- **Related proteins** (co-abundance neighbors): WDR12 (0.87), UTP4 (0.81); STRING partners: DDX56 (0.97), HEATR1 (0.877), UTP4 (0.926), WDR12 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli, Nucleoli rim, Mitotic chromosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pescadillo ribosomal biogenesis factor 1. This gene encodes a nuclear protein that contains a breast cancer associated gene 1 (BRCA1) C-terminal interaction domain. The encoded protein interacts with BOP1 and WDR12 to form the PeBoW complex, which plays a critical role in cell proliferation via pre-rRNA processing and 60S ribosomal subunit maturation. Expression of this gene may play an important role in breast cancer proliferation and tu…
- **Diseases (Open Targets)**: aortic stenosis (0.137); neoplasm (0.104); head and neck squamous cell carcinoma (0.097); schizophrenia (0.091); neuroblastoma (0.081)
- **Europe PMC papers**: 1080
- **Why important**: PES1 is a central connector linking the WDR12 arm with UTP4 and has STRING relationships throughout the module. It occurs in the 90S preribosome, preribosome, PeBoW-complex, nucleolar, rRNA-processing, and ribosome-biogenesis evidence (GO:CC 90S preribosome; q_global = 2.71e-05), (GO:BP rRNA processing; q_global = 0.000341), (GO:BP rRNA metabolic process; q_global = 0.000629), (GO:BP ribosome biogenesis; q_global = 0.00104), (GO:CC preribosome; q_global = 0.00186), (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.00357), (GO:CC PeBoW complex; q_global = 0.0271), (GO:CC nucleolus; q_global = 0.0411), (GO:BP RNA processing; q_global = 0.0451). The supplied description identifies PES1 as a PeBoW-complex component involved in precursor-rRNA processing and large-subunit maturation. It also has the largest literature volume in the fact sheet, making it one of the best-characterized module genes. Its disease and cancer associations are relevant context but do not establish a tissue-module role.
- **Conclusion**: Established: PES1 is a nucleolar ribosome-biogenesis factor and PeBoW-complex component and is a strong module anchor. Hypothesis: PES1 may couple module abundance to large-subunit maturation or cellular proliferative state in bone and ovary. A tissue-specific consequence is not demonstrated.

#### WDR12

- **Related proteins** (co-abundance neighbors): PES1 (0.87); STRING partners: DDX56 (0.917), HEATR1 (0.908), PES1 (0.999), UTP4 (0.939)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 12. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); poisoning (0.233); non-autoimmune hemolytic anemia (0.214); coronary artery disorder (0.210); myocardial infarction (0.168)
- **Europe PMC papers**: 602
- **Why important**: WDR12 is tightly connected to PES1 and has STRING relationships with all other module genes. It occurs in the globally significant 90S preribosome, preribosome, rRNA-processing, ribosome-biogenesis, nucleolar, and RNA-processing terms (GO:CC 90S preribosome; q_global = 2.71e-05), (GO:BP rRNA processing; q_global = 0.000341), (GO:BP rRNA metabolic process; q_global = 0.000629), (GO:BP ribosome biogenesis; q_global = 0.00104), (GO:CC preribosome; q_global = 0.00186), (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.00357), (GO:CC PeBoW complex; q_global = 0.0271), (GO:CC nucleolus; q_global = 0.0411), (GO:BP RNA processing; q_global = 0.0451). The supplied description supports a WD-repeat role in multiprotein complexes and identifies participation in PeBoW biology, rRNA maturation, ribosome biogenesis, and cell-cycle regulation. Its disease associations and substantial literature provide relevance but do not prove a bone–ovary-specific function.
- **Conclusion**: Established: WDR12 is part of the ribosome-biogenesis machinery, especially the PeBoW-related large-subunit maturation arm. Hypothesis: coordinated WDR12–PES1 abundance may report the capacity for pre-ribosomal large-subunit maturation in the shared cellular state. Direct causality remains untested.

#### UTP4

- **Related proteins** (co-abundance neighbors): DDX56 (0.90), PES1 (0.81); STRING partners: DDX56 (0.82), HEATR1 (0.999), PES1 (0.926), WDR12 (0.939)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UTP4 small subunit processome component. This gene encodes a WD40-repeat-containing protein that is localized to the nucleolus. Mutation of this gene causes North American Indian childhood cirrhosis, a severe intrahepatic cholestasis that results in transient neonatal jaundice, and progresses to periportal fibrosis and cirrhosis in childhood and adolescence. Alternative splicing results in multiple transcript variants. [provided by RefSe…
- **Diseases (Open Targets)**: hereditary North American Indian childhood cirrhosis (0.420); cardiovascular disorder (0.101); basal cell carcinoma (0.079); hypertensive disorder (0.064); osteosarcoma (0.052)
- **Europe PMC papers**: 214
- **Why important**: UTP4 has broad module connectivity and STRING relationships with every other member. It occurs in the 90S preribosome, t-UTP complex, preribosome, rRNA-processing, ribosome-biogenesis, nucleolar, and RNA-processing evidence (GO:CC 90S preribosome; q_global = 2.71e-05) through (GO:CC t-UTP complex; q_global = 0.0271), (GO:CC nucleolus; q_global = 0.0411), (GO:BP RNA processing; q_global = 0.0451). The supplied description identifies it as a WD40-repeat small-subunit processome component involved in precursor-rRNA maturation and small-subunit biogenesis. HPA reports low tissue specificity, with enhancement in oocytes and proximal tubule cells, consistent with a general intracellular function rather than a blood-specific signal. Its association with North American Indian childhood cirrhosis is an established clinical link in the fact sheet.
- **Conclusion**: Established: UTP4 is a nucleolar small-subunit processome factor and a strong marker of early rRNA processing. Hypothesis: UTP4 may connect the shared module to early precursor-rRNA maturation in cells present in both tissues; its oocyte enhancement is suggestive but not proof of an ovary-specific role.

#### HEATR1

- **Related proteins** (co-abundance neighbors): DDX56 (0.93); STRING partners: DDX56 (0.844), PES1 (0.877), UTP4 (0.999), WDR12 (0.908)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HEAT repeat containing 1. Enables RNA binding activity. Involved in positive regulation of rRNA processing and positive regulation of transcription by RNA polymerase I. Located in fibrillar center and mitochondrion. Implicated in pancreatic ductal carcinoma. Biomarker of glioblastoma. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.475); Alzheimer disease (0.463); Parkinson disease (0.462); lysosomal storage disease (0.462); musculoskeletal system disorder (0.168)
- **Europe PMC papers**: 342
- **Why important**: HEATR1 participates in the 90S preribosome and t-UTP-complex evidence (GO:CC 90S preribosome; q_global = 2.71e-05), (GO:CC preribosome; q_global = 0.00186), (GO:CC t-UTP complex; q_global = 0.0271), and in the globally significant rRNA-processing and ribosome-biogenesis terms (GO:BP rRNA processing; q_global = 0.000341), (GO:BP rRNA metabolic process; q_global = 0.000629), (GO:BP ribosome biogenesis; q_global = 0.00104), (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.00357), (GO:CC nucleolus; q_global = 0.0411), (GO:BP RNA processing; q_global = 0.0451). The supplied description assigns RNA binding, positive regulation of rRNA processing, and positive regulation of RNA polymerase I transcription. HEATR1 is connected to the other module genes by STRING and may link early preribosome functions with transcriptional output. Its disease and cancer associations provide biological context, while HPA indicates broad tissue distribution with enhancement in epicardial cells.
- **Conclusion**: Established: HEATR1 is associated with nucleolar rRNA processing and RNA polymerase I transcription and participates in the 90S preribosome and t-UTP complex. Hypothesis: HEATR1 may coordinate preribosome production with transcriptional activity in the shared cellular state. This coordinating role is not proven by the co-abundance network.

#### DDX56

- **Related proteins** (co-abundance neighbors): HEATR1 (0.93), UTP4 (0.90); STRING partners: HEATR1 (0.844), PES1 (0.97), UTP4 (0.82), WDR12 (0.917)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 56. This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribut…
- **Diseases (Open Targets)**: metabolic disease (0.246); hyperlipidemia (0.242); neurodegenerative disease (0.157); Hypercholesterolemia (0.151); alcohol drinking (0.131)
- **Europe PMC papers**: 374
- **Why important**: DDX56 is the module's DEAD-box RNA-helicase gene and occurs in all primary biological-process terms shared by the module (GO:BP rRNA processing; q_global = 0.000341), (GO:BP rRNA metabolic process; q_global = 0.000629), (GO:BP ribosome biogenesis; q_global = 0.00104), (GO:BP ribonucleoprotein complex biogenesis; q_global = 0.00357), (GO:CC nucleolus; q_global = 0.0411), (GO:BP RNA processing; q_global = 0.0451). Its supplied description supports RNA secondary-structure remodeling and roles in ribosome and spliceosome assembly. It has STRING relationships with every module member, and HPA places it in nucleoli with ovarian detection. Although it is less central by the supplied network position than the strongest connectors, its helicase activity provides a distinct mechanistic capability that complements the structural and assembly roles of the other genes.
- **Conclusion**: Established: DDX56 is a nucleolar DEAD-box RNA helicase associated with rRNA processing and ribosome assembly and is co-abundant with the rest of the module. Hypothesis: DDX56 may provide RNA-remodeling activity that enables precursor-rRNA maturation within the shared program. The evidence does not show that it is rate-limiting or tissue-specific.

## Module 12

**Tissue pair**: bone and ovary  
**Genes (6)**: DSP, GAR1, PPP1R12A, NUP37, NUP62, POLR1B

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. The module therefore does not support a single statistically established pathway-level function. Its gene annotations suggest a mixed nuclear and epithelial-cell program: GAR1 and POLR1B support nucleolar RNA processing, ribosome biogenesis, and rRNA transcription; NUP37 and NUP62 support nuclear-pore structure and nucleocytoplasmic transport; DSP supports desmosome organization and intermediate-filament anchoring; and PPP1R12A supports myosin phosphatase, actomyosin regulation, cell adhesion, and contractile signaling. The co-abundance structure may therefore reflect shared cellular state, proliferation, nuclear transport, or epithelial and reproductive-cell composition rather than one canonical biochemical pathway. This interpretation is consistent with the absence of globally significant globally significant GO/KEGG terms and should be regarded as an annotation-based model rather than a demonstrated pathway.

**Cell composition.** The module is not composed of secreted proteins, so a plasma-protein explanation is unlikely. Most genes have low tissue specificity and low immune-cell specificity, arguing against a strongly blood-derived module. DSP is tissue enhanced in esophagus and skin and is immune-cell enriched in naive B cells, while the remaining genes show cell-type enhancement in trophoblast, germ-cell, epithelial, neutrophil, or smooth-muscle populations. All module genes have cell-type-enhanced HPA annotations, indicating that cellular composition could contribute substantially to the shared bone–ovary signal. Protein detection is reported for most module genes in ovary, whereas matching bone protein data are unavailable. The module should therefore not be interpreted as bone- or ovary-specific without cell-composition and independent validation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known STRING relationship is between NUP37 and NUP62, directly supporting a nuclear-pore-complex connection. GAR1 and POLR1B also have a high-confidence STRING relationship, supporting a nucleolar RNA-processing and rRNA-transcription connection. The remaining co-abundance relationships are not represented by high-confidence STRING interactions. hu.MAP provides an independent complex-level observation through (hu.MAP huMAP3_12581.1), in which NUP37 and NUP62 occur together within a large nuclear-pore-related complex. Thus, part of the module recapitulates established nuclear transport and nucleolar biology, while the links involving DSP and PPP1R12A are not established as physical complexes by the supplied STRING or hu.MAP evidence. The network is consequently biologically heterogeneous, with a supported nuclear substructure and additional co-abundance associations that may be indirect or context dependent.

**STRING interactions (score >= 0.7)**: 2 of 15 gene pairs: GAR1–POLR1B (0.775); NUP37–NUP62 (0.98)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12581.1 (NUP62, NUP37; 2/58)

### Novelty

The module-level finding may be novel as a cross-tissue co-abundance pattern, but the available evidence is insufficient to claim discovery of a new molecular complex or pathway. The GAR1–POLR1B relationship, the NUP37–NUP62 relationship, and the NUP37–NUP62 membership in (hu.MAP huMAP3_12581.1) are already consistent with known biology. Conversely, the apparent association of these nuclear genes with DSP and PPP1R12A is not supported as a known physical complex by the supplied resources. Absence from STRING or hu.MAP does not establish novelty, because co-abundance can arise from indirect regulation, shared cell types, technical covariance, or context-specific interactions. A defensible novelty claim would require replication in independent bone and ovary cohorts, control for cellular composition, and orthogonal testing of the cross-compartment associations.

**Hypothesis.** Hypothesis: the shared module reflects coordinated abundance of a basic nuclear and cell-architecture program in selected bone- and ovary-associated cell populations. In this model, nucleolar activity involving GAR1 and POLR1B is coupled to nuclear transport through the NUP37–NUP62 pore components, while DSP and PPP1R12A report epithelial junctional or cytoskeletal state and actomyosin regulation. The module could therefore mark cells with linked demands for ribosome production, nucleocytoplasmic exchange, adhesion, and mechanical remodeling. This is a mechanistic hypothesis, not an established interaction map; the data do not demonstrate that DSP or PPP1R12A physically bind the nuclear components.

### Important genes

#### GAR1

- **Related proteins** (co-abundance neighbors): NUP37 (0.92), POLR1B (0.89), DSP (0.87); STRING partners: POLR1B (0.775)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GAR1 ribonucleoprotein. This gene is a member of the H/ACA snoRNPs (small nucleolar ribonucleoproteins) gene family. snoRNPs are involved in various aspects of rRNA processing and modification and have been classified into two families: C/D and H/ACA. The H/ACA snoRNPs also include the DKC1, NOLA2 and NOLA3 proteins. These four H/ACA snoRNP proteins localize to the dense fibrillar components of nucleoli and to coiled (Ca…
- **Diseases (Open Targets)**: neurodegenerative disease (0.400); prostate carcinoma (0.198); Thrombocytopenia (0.048); familial primary hypomagnesemia with normocalciuria and normocalcemia (0.041); renal hypomagnesemia 2 (0.041)
- **Europe PMC papers**: 1232
- **Why important**: GAR1 has the greatest network connectivity in the module and links the nucleolar arm to NUP37 and DSP. Its established H/ACA snoRNP role connects the module to snoRNA-guided rRNA pseudouridylation, rRNA processing, ribosome biogenesis, and telomere maintenance. It also has substantial literature coverage and disease associations, making it a strong candidate for a central abundance-state marker rather than merely a peripheral correlate.
- **Conclusion**: Established evidence supports GAR1 as a nucleolar RNA-processing and ribosome-biogenesis component and as a network hub. It is plausible, but unproven, that GAR1 helps define a shared high-nucleolar-activity state in the two tissues. The module does not establish a new GAR1 interaction with DSP or the nuclear-pore proteins.

#### NUP37

- **Related proteins** (co-abundance neighbors): GAR1 (0.92), PPP1R12A (0.82); STRING partners: NUP62 (0.98)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 37. Nuclear pore complexes (NPCs) are used for transporting macromolecules between the cytoplasm and the nucleus. NPCs consist of multiple copies of 30 distinct proteins (nucleoporins), which assemble into biochemically-separable subcomplexes. The protein encoded by this gene is part of a subcomplex (Nup107-160) that is required for proper NPC function as well as for normal kinetochore-microtubule int…
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); microcephaly 24, primary, autosomal recessive (0.492); neurodegenerative disease (0.463)
- **Europe PMC papers**: 481
- **Why important**: NUP37 connects GAR1 with PPP1R12A and is supported by both the strongest nuclear-pore STRING relationship in the module and the (hu.MAP huMAP3_12581.1) hu.MAP complex containing NUP62. Its established role in the NUP107–NUP160 subcomplex links the module to nucleocytoplasmic transport, kinetochore–microtubule interactions, and mitotic function. Its disease associations also make altered NUP37 abundance biologically consequential.
- **Conclusion**: Established evidence identifies NUP37 as a nuclear-pore and mitotic-function component that is physically or complexually related to NUP62. Its bridging position suggests that it may connect nuclear transport with the broader co-abundance pattern, but a functional bridge to PPP1R12A or GAR1 remains a hypothesis.

#### NUP62

- **Related proteins** (co-abundance neighbors): DSP (0.80); STRING partners: NUP37 (0.98)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 62. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. The protein encoded by this gene is a member of the FG-repeat containing nucleoporins and is localized to the nuclear pore ce…
- **Diseases (Open Targets)**: infantile bilateral striatal necrosis (0.609); familial infantile bilateral striatal necrosis (0.590); HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.529)
- **Europe PMC papers**: 1582
- **Why important**: NUP62 is a central-plug FG nucleoporin involved in RNA export, protein import, and cell-cycle-associated nuclear functions. It has a direct high-confidence STRING relationship with NUP37 and shares (hu.MAP huMAP3_12581.1) complex membership with NUP37, giving this pair the clearest independently supported structural core in the module. Its extensive literature and disease associations further support prioritizing it for validation.
- **Conclusion**: Established evidence supports NUP62 as a nuclear-pore component and supports its relationship with NUP37. The module is compatible with altered nucleocytoplasmic transport, but it does not show that transport is the primary driver of the bone–ovary association.

#### DSP

- **Related proteins** (co-abundance neighbors): GAR1 (0.87), NUP62 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cell Junctions; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: desmoplakin. This gene encodes a protein that anchors intermediate filaments to desmosomal plaques and forms an obligate component of functional desmosomes. Mutations in this gene are the cause of several cardiomyopathies and keratodermas, including skin fragility-woolly hair syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016].
- **Diseases (Open Targets)**: arrhythmogenic cardiomyopathy with wooly hair and keratoderma (0.841); arrhythmogenic right ventricular dysplasia 8 (0.812); arrhythmogenic right ventricular cardiomyopathy (0.760); lethal acantholytic epidermolysis bullosa (0.745); cardiomyopathy, dilated, with wooly hair, keratoderma, and tooth agenesis (0.741)
- **Europe PMC papers**: 17350
- **Why important**: DSP is the most tissue-specialized member according to the HPA summary and is enriched in epithelial cell types, with localization at cell junctions. It encodes desmoplakin, an obligate desmosomal component that anchors intermediate filaments, and it has extensive literature and strong disease associations involving cardiomyopathy, keratoderma, and epithelial fragility. Its connection to GAR1 and NUP62 in the co-abundance graph makes it important for interpreting the module as a possible cell-state or tissue-composition signal.
- **Conclusion**: Established evidence supports DSP as a desmosome and epithelial-architecture protein with major inherited disease relevance. Its module association may indicate epithelial or junctional cell composition rather than a direct link to nucleolar or nuclear-pore machinery. A coordinated mechanical–nuclear response is a hypothesis requiring direct validation.

#### PPP1R12A

- **Related proteins** (co-abundance neighbors): NUP37 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments, Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase 1 regulatory subunit 12A. Myosin phosphatase target subunit 1, which is also called the myosin-binding subunit of myosin phosphatase, is one of the subunits of myosin phosphatase. Myosin phosphatase regulates the interaction of actin and myosin downstream of the guanosine triphosphatase Rho. The small guanosine triphosphatase Rho is implicated in myosin light chain (MLC) phosphorylation, which results in contraction of smo…
- **Diseases (Open Targets)**: genitourinary and/or brain malformation syndrome (0.777); neurodegenerative disease (0.572); hereditary disease (0.415); holoprosencephaly (0.371); Genetic 46,XY disorder of sex development (0.370)
- **Europe PMC papers**: 1121
- **Why important**: PPP1R12A is the module member most directly associated with myosin phosphatase regulation, Rho-linked actomyosin behavior, cell adhesion, and contractile signaling. Its HPA cell-type annotations include neutrophil-lineage and smooth-muscle populations, and it connects to NUP37 in the module graph. These features make it useful for testing whether the module reflects cytoskeletal state or tissue-cell composition in addition to nuclear processes.
- **Conclusion**: Established evidence supports PPP1R12A as a regulator of myosin phosphatase and actomyosin-dependent adhesion or contractility. Its association with NUP37 is co-abundance evidence rather than demonstrated physical interaction. It may report mechanical or cellular-state coupling in the module, but this remains a hypothesis.

## Module 13

**Tissue pair**: bone and ovary  
**Genes (6)**: EZR, HSPH1, EIF4G1, SMC2, SMC4, TXLNA

### Function

The module is most consistent with a chromosome-organization and cell-cycle-associated program centered on the condensin machinery. SMC2 and SMC4 are the clearest functional anchors: they have a very strong STRING relationship, occur together in multiple hu.MAP condensin-related complexes (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_14663.1), and have supplementary domain evidence for the SMC flexible-hinge and AAA regions (STRING SMART SMC proteins Flexible Hinge Domain; within-query FDR = 0.0176) (STRING Pfam AAA domain; within-query FDR = 0.0233). SMC2 is annotated in chromosome condensation, chromosome organization and chromosome segregation, while SMC4 is annotated in mitotic and meiotic chromosome segregation and condensation. EIF4G1, HSPH1, EZR and TXLNA suggest additional links to translational capacity, proteostasis, membrane–cytoskeleton organization and exocytosis, respectively, but these connections are supported here by co-abundance rather than by matching STRING or hu.MAP relationships. No GO/KEGG term passed global correction, so the functional interpretation is driven by gene annotations, network structure and the independently supported SMC2–SMC4 relationship rather than by significant GO/KEGG enrichment. The module may therefore represent a mixed cellular-state program rather than a single complete biochemical pathway.

**Cell composition.** The module is not composed of secreted proteins. Most genes have low tissue specificity, and most have low immune-cell specificity, arguing against a straightforward plasma-protein or broadly blood-derived module. However, several genes show cell-type-enhanced expression in epithelial, germ-cell or progenitor populations, and SMC2 and SMC4 are tissue-enhanced in lymphoid tissue. The repeated enrichment for erythrocyte, megakaryocyte and monocyte progenitor annotations, together with the single immune-cell-enhanced signal for SMC4, leaves open a contribution from shared proliferative or hematopoietic cell populations in the samples. Protein detection in ovary is widespread across the module, whereas the bone comparison has no matching HPA tissue result, so the HPA data do not establish bone-specific protein expression. Overall, shared cell composition or a shared proliferative state is a plausible contributor, but the available evidence does not support labeling the module as a blood or secreted-protein module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a high-confidence relationship only for SMC2–SMC4, directly supporting the interpretation that these genes form a known condensin-related pair. The supplementary STRING domain terms (STRING SMART SMC proteins Flexible Hinge Domain; within-query FDR = 0.0176) (STRING Pfam AAA domain; within-query FDR = 0.0233) independently point toward the SMC protein architecture, but they are not global enrichment evidence. hu.MAP contains several complexes (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_14663.1) in which SMC2 and SMC4 occur together with condensin-associated proteins including NCAPD2, NCAPD3, NCAPH, NCAPH2, NCAPG and NCAPG2. Thus, the module captures a recognized condensin core, but only a subset of the broader complexes. EIF4G1, HSPH1, EZR and TXLNA have no listed STRING partners or hu.MAP complexes in this module. Their co-abundance edges should therefore be interpreted as coordinated abundance patterns, shared regulation, cellular composition effects or indirect functional coupling, not as established direct protein interactions.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: SMC2–SMC4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART SMC proteins Flexible Hinge Domain (FDR = 0.0176, 2 genes); Pfam AAA domain (FDR = 0.0233, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03084.1 (SMC2, SMC4; 2/8); huMAP3_14385.1 (SMC2, SMC4; 2/9); huMAP3_09855.1 (SMC2, SMC4; 2/10); huMAP3_11457.1 (SMC2, SMC4; 2/10); huMAP3_14663.1 (SMC2, SMC4; 2/14)

### Novelty

The module cannot be claimed as a wholly new biological complex. Its strongest signal, the SMC2–SMC4 pair, is already known from STRING and is repeatedly represented in hu.MAP complexes. The absence of the other module genes from the listed interaction resources does not prove novelty, because co-abundance can arise from indirect regulation, shared cell types, technical covariation or condition-specific biology. A more defensible conclusion is that this is a potentially interesting tissue-pair co-abundance configuration that combines a known condensin relationship with less-established associations to translation, chaperoning and membrane–cytoskeleton functions. Its novelty would require independent replication in bone and ovary, assessment against matched cell composition and validation of the non-SMC relationships.

**Hypothesis.** Hypothesis: the module reflects a coordinated proliferative or remodeling state in which condensin activity is coupled to increased translational demand, proteostasis and changes in cell architecture. In this model, SMC2–SMC4 provides the chromosome-condensation component; EIF4G1 supports the protein-synthesis capacity needed by active cells; HSPH1 buffers proteotoxic stress; and EZR and TXLNA relate the state to cytoskeletal organization and vesicle handling. The apparent sharing between bone and ovary could arise from common cycling progenitor, epithelial, germ-cell or immune-associated populations rather than from a bone–ovary-specific pathway. This is a mechanistic hypothesis, not an established physical interaction model.

### Important genes

#### SMC4

- **Related proteins** (co-abundance neighbors): SMC2 (0.87), EIF4G1 (0.86), HSPH1 (0.85); STRING partners: SMC2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nuclear speckles, Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_03084.1, huMAP3_14385.1, huMAP3_09855.1, huMAP3_11457.1, huMAP3_14663.1
- **Function (MyGene.info)**: structural maintenance of chromosomes 4. This gene belongs to the 'structural maintenance of chromosomes' (SMC) gene family. Members of this gene family play a role in two changes in chromosome structure during mitotic segregation of chromosomes- chromosome condensation and sister chromatid cohesion. The protein encoded by this gene is likely a subunit of the 13S condensin complex, which is involved in chromosome condensation. A pseudoge…
- **Diseases (Open Targets)**: clonal hematopoiesis (0.233); bone marrow failure syndrome (0.148); hepatocellular carcinoma (0.111); central nervous system cancer (0.107); glioma (0.107)
- **Europe PMC papers**: 1967
- **Why important**: SMC4 is a central network member and one half of the only STRING-supported pair in the module. It is present with SMC2 in every listed hu.MAP complex (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_14663.1), has supplementary SMC-domain and AAA-domain support (STRING SMART SMC proteins Flexible Hinge Domain; within-query FDR = 0.0176) (STRING Pfam AAA domain; within-query FDR = 0.0233), and is annotated in chromosome condensation and chromosome segregation. Its tissue-enhanced lymphoid signal and cell-type-enhanced progenitor and germ-cell annotations also make it relevant to possible shared cellular composition. Its substantial literature and disease associations provide more external support than the weaker module-specific links.
- **Conclusion**: Established evidence supports SMC4 as a condensin component and as the strongest functional anchor of the module. The module-specific connection of SMC4 to EIF4G1 and HSPH1 is an observed co-abundance relationship, not a demonstrated direct interaction. A plausible hypothesis is that SMC4 marks a shared proliferative or chromosome-management state in the two tissues.

#### SMC2

- **Related proteins** (co-abundance neighbors): SMC4 (0.87); STRING partners: SMC4 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_03084.1, huMAP3_14385.1, huMAP3_09855.1, huMAP3_11457.1, huMAP3_14663.1
- **Function (MyGene.info)**: structural maintenance of chromosomes 2. Predicted to enable ATP binding activity; chromatin binding activity; and single-stranded DNA binding activity. Involved in mitotic chromosome condensation. Located in condensed chromosome; cytoplasm; and nuclear lumen. Part of condensin complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: basal cell carcinoma (0.464); ovarian carcinoma (0.383); aortic stenosis (0.380); cancer (0.363); alcohol drinking (0.359)
- **Europe PMC papers**: 2065
- **Why important**: SMC2 is directly paired with SMC4 by STRING and occurs with SMC4 across the hu.MAP complexes (hu.MAP huMAP3_03084.1) (hu.MAP huMAP3_14385.1) (hu.MAP huMAP3_09855.1) (hu.MAP huMAP3_11457.1) (hu.MAP huMAP3_14663.1). Its annotations specifically support condensin function, chromosome condensation, chromosome organization and chromosome segregation. It is also associated with ovarian carcinoma and other disease contexts, making it biologically relevant to an ovary-containing tissue comparison. Although its network degree is limited, its established complex membership gives it high interpretive importance.
- **Conclusion**: Established evidence identifies SMC2 as a condensin subunit and validates the SMC2–SMC4 core. The evidence does not establish that SMC2 is functionally coupled to the other four genes in a single complex. A reasonable hypothesis is that SMC2–SMC4 abundance reflects cell-cycle activity or progenitor composition shared across the tissue samples.

#### EIF4G1

- **Related proteins** (co-abundance neighbors): SMC4 (0.86), TXLNA (0.84), HSPH1 (0.83), EZR (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 has the highest network connectivity in the module and links SMC4, TXLNA, HSPH1 and EZR. Its established function is as a scaffold in the EIF4F translation-initiation complex, placing it at the interface between cellular growth, mRNA recruitment and protein production. It is the most extensively represented gene in the supplied literature summary and has disease associations including neurodegenerative and hypertensive conditions. Its central network position makes it important even though it lacks listed STRING or hu.MAP support here.
- **Conclusion**: Established evidence supports EIF4G1 as a translation-initiation scaffold and a highly connected co-abundance hub in this module. There is no evidence here that it physically binds the SMC condensin pair or that the module is a translation complex. The hypothesis is that EIF4G1 reports increased biosynthetic demand or a shared growth state that covaries with condensin abundance.

#### HSPH1

- **Related proteins** (co-abundance neighbors): SMC4 (0.85), EZR (0.83), EIF4G1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family H (Hsp110) member 1. This gene encodes a member of the heat shock protein 70 family of proteins. The encoded protein functions as a nucleotide exchange factor for the molecular chaperone heat shock cognate 71 kDa protein (Hsc70). In addition, this protein plays a distinct but related role as a holdase that inhibits the aggregation of misfolded proteins, including the cystic fibrosis transmembrane conductance regulator…
- **Diseases (Open Targets)**: Parkinson disease (0.205); Phenotypic abnormality (0.187); hypertensive disorder (0.131); neoplasm (0.104); major depressive disorder (0.096)
- **Europe PMC papers**: 2050
- **Why important**: HSPH1 is connected to SMC4, EIF4G1 and EZR and is annotated as a chaperone-related protein involved in protein folding, unfolded-protein response and stress biology. Its cell-type-enhanced signals include monocytes and pancreatic duct cells, while its supplied disease associations include Parkinson disease and neoplasm. This makes HSPH1 a plausible indicator of proteostasis or cellular stress accompanying the module, although it has no listed STRING or hu.MAP relationship within the module.
- **Conclusion**: Established evidence supports HSPH1 in chaperoning and stress-response biology. Its participation in the module beyond co-abundance is not established. The hypothesis is that HSPH1 couples a stress-buffering response to the biosynthetic and proliferative state represented by EIF4G1 and the SMC pair.

#### EZR

- **Related proteins** (co-abundance neighbors): HSPH1 (0.83), EIF4G1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ezrin. The cytoplasmic peripheral membrane protein encoded by this gene functions as a protein-tyrosine kinase substrate in microvilli. As a member of the ERM protein family, this protein serves as an intermediate between the plasma membrane and the actin cytoskeleton. This protein plays a key role in cell surface structure adhesion, migration and organization, and it has been implicated in various human…
- **Diseases (Open Targets)**: hair color (0.477); non-small cell lung carcinoma (0.397); lung adenocarcinoma (0.382); autosomal recessive non-syndromic intellectual disability (0.370); glaucoma (0.347)
- **Europe PMC papers**: 4982
- **Why important**: EZR connects HSPH1 and EIF4G1 and is the module member with the strongest supplied literature representation. It is an ERM-family membrane–cytoskeleton linker involved in cell shape, adhesion, migration and surface organization, and it has extensive cancer-related disease associations. Its epithelial and syncytiotrophoblast cell-type annotations are relevant to the possibility that shared cell composition contributes to the bone–ovary pattern. It has no listed STRING or hu.MAP support in this module.
- **Conclusion**: Established evidence supports EZR as a membrane–actin cytoskeletal organizer with roles in adhesion and migration. The data do not establish a direct EZR interaction with EIF4G1 or HSPH1. The hypothesis is that EZR reflects cellular architecture or tissue-remodeling state that covaries with the condensin and stress-related signals.

## Module 14

**Tissue pair**: bone and ovary  
**Genes (8)**: FASN, PAICS, ATIC, CTPS1, RCC1, RRM1, RUVBL2, QARS1

### Function

The module is most consistent with coordinated anabolic nucleotide metabolism, especially de novo purine and pyrimidine biosynthesis. (GO:BP nucleobase metabolic process; q_global = 0.022) supports nucleobase metabolism through CTPS1, PAICS, and RRM1, while (GO:BP nucleoside phosphate biosynthetic process; q_global = 0.0233) supports nucleoside phosphate biosynthesis through ATIC, CTPS1, FASN, PAICS, and RRM1. The pathway interpretation is biologically coherent: PAICS and ATIC participate in successive de novo purine-biosynthetic reactions, CTPS1 produces CTP for nucleotide and phospholipid synthesis, and RRM1 supplies deoxyribonucleotides needed for DNA synthesis and repair. FASN adds lipid-anabolic metabolism, whereas QARS1, RUVBL2, and RCC1 connect the module to translation, genome maintenance, and cell-cycle-related biology. The co-abundance structure therefore suggests a growth, biosynthetic, or proliferative metabolic program rather than a narrowly tissue-specific signaling pathway. The globally corrected GO evidence is stronger than the supplementary STRING annotations; the latter independently point toward nucleotide metabolism through (STRING RCTM Metabolism of nucleotides; within-query FDR = 0.0145).

**Cell composition.** The module is composed entirely of intracellular proteins, with no secreted genes, so it is not a plasma-protein or secreted-protein module. The HPA profile indicates generally broad tissue distribution for most genes, with a smaller subset showing tissue enhancement in adipose tissue, breast, liver, or testis. Most genes have low immune-cell specificity, and no frequent enriched blood-cell population was reported; this argues against a straightforward blood-cell contamination explanation. However, several genes show cell-type enhancement in trophoblasts, spermatogenic cells, or erythrocyte progenitors, and the module includes broadly expressed metabolic and genome-maintenance genes. Thus, the shared bone–ovary signal may reflect a common biosynthetic or proliferative cell state, broadly expressed cellular machinery, or shared cellular composition rather than a specialized bone–ovary secretory program. Ovary protein detection is present for most members, whereas matched bone protein evidence was unavailable, so the bone interpretation should remain cautious.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP nucleobase metabolic process | 0.022 | CTPS1, PAICS, RRM1 |
| GO:BP nucleoside phosphate biosynthetic process | 0.0233 | ATIC, CTPS1, FASN, PAICS, RRM1 |

### STRING and hu.MAP

The strongest direct STRING relationship is the ATIC–PAICS pair, which is highly concordant with their established participation in successive de novo purine-biosynthetic steps. This provides focused biochemical support for part of the module, but STRING contains only a small subset of the possible within-module gene pairs. The remaining co-abundance links therefore should not automatically be interpreted as direct physical interactions. STRING functional enrichment independently supports nucleotide metabolism through (STRING RCTM Metabolism of nucleotides; within-query FDR = 0.0145), while the tissue-related results (STRING TISSUES Male reproductive gland; within-query FDR = 0.0157), (STRING TISSUES Mammary gland; within-query FDR = 0.0471), and (STRING TISSUES Internal male genital organ; within-query FDR = 0.0471) are supplementary and may reflect expression patterns rather than mechanism. The multifunctional-enzyme annotation (STRING Keyword Multifunctional enzyme; within-query FDR = 0.0374) is compatible with the presence of ATIC, FASN, and PAICS but is not primary global enrichment evidence. No hu.MAP complex contains multiple module members, so there is no detected multi-protein complex that explains the module as a single assembled molecular machine. Overall, the known interaction evidence validates a biochemical core centered on purine metabolism, while the broader co-abundance module likely combines pathway coupling with shared cell-state regulation.

**STRING interactions (score >= 0.7)**: 1 of 28 gene pairs: ATIC–PAICS (0.997)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Metabolism of nucleotides (FDR = 0.0145, 4 genes); TISSUES Male reproductive gland (FDR = 0.0157, 8 genes); Keyword Multifunctional enzyme (FDR = 0.0374, 3 genes); TISSUES Mammary gland (FDR = 0.0471, 3 genes); TISSUES Internal male genital organ (FDR = 0.0471, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be presented as a newly discovered biochemical pathway. Its central activities are established, and the ATIC–PAICS relationship is already represented in STRING. At the same time, the specific conserved co-abundance pattern across bone and ovary is not explained by a known hu.MAP complex and is only sparsely represented by direct STRING interactions. That makes the cross-tissue co-abundance organization potentially informative, but not sufficient by itself to establish novelty. A defensible conclusion is that the module may represent a new tissue-pair-level organization or regulatory context for known metabolic and genome-maintenance genes; confirmation would require replication in independent cohorts and testing against cell composition, proliferation, and technical confounding.

**Hypothesis.** Hypothesis: the conserved bone–ovary module reflects a shared high-biosynthetic-demand cell state in which purine and pyrimidine production, deoxyribonucleotide supply, lipid synthesis, translation capacity, and genome maintenance are coordinately increased. In this model, PAICS and ATIC form a biochemical purine-biosynthesis core, CTPS1 supports pyrimidine and phospholipid precursor production, RRM1 supplies substrates for DNA replication and repair, and FASN supports lipid anabolism. QARS1, RUVBL2, and RCC1 may reflect the accompanying demands of protein synthesis, DNA repair, chromatin or replication control, and cell-cycle progression. This is a mechanistic model inferred from annotations and co-abundance; the data do not demonstrate physical assembly, catalytic flux, or causal regulation.

### Important genes

#### CTPS1

- **Related proteins** (co-abundance neighbors): PAICS (0.90), RRM1 (0.82), QARS1 (0.81), ATIC (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CTP synthase 1. This gene encodes an enzyme responsible for the catalytic conversion of UTP (uridine triphosphate) to CTP (cytidine triphospate). This reaction is an important step in the biosynthesis of phospholipids and nucleic acids. Activity of this proten is important in the immune system, and loss of function of this gene has been associated with immunodeficiency. Alternative splicing results in multiple tr…
- **Diseases (Open Targets)**: combined immunodeficiency due to CTPS1 deficiency (0.712); androgenetic alopecia (0.204); hyperpituitarism (0.195); urolithiasis (0.097); alcohol drinking (0.097)
- **Europe PMC papers**: 641
- **Why important**: CTPS1 is the most connected node in the module and appears in both primary globally corrected terms, (GO:BP nucleobase metabolic process; q_global = 0.022) and (GO:BP nucleoside phosphate biosynthetic process; q_global = 0.0233). It encodes CTP synthase, linking nucleotide production with phospholipid and nucleic-acid biosynthesis, and it has a strong literature base. Its established disease association with CTPS1 deficiency and immunodeficiency adds biological and clinical relevance. Its ovary detection and broad cellular profile support a real intracellular metabolic role, while its network position makes it a plausible organizer of the module's co-abundance signal.
- **Conclusion**: Established: CTPS1 is a central pyrimidine-biosynthetic enzyme and a primary evidence gene for the module's nucleotide-metabolism interpretation. Hypothesis: its central network position may mark a rate-limiting or coordinately regulated biosynthetic demand shared by relevant bone and ovary cell populations.

#### PAICS

- **Related proteins** (co-abundance neighbors): CTPS1 (0.90); STRING partners: ATIC (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoribosylaminoimidazole carboxylase and phosphoribosylaminoimidazolesuccinocarboxamide synthase. This gene encodes a bifunctional enzyme containing phosphoribosylaminoimidazole carboxylase activity in its N-terminal region and phosphoribosylaminoimidazole succinocarboxamide synthetase in its C-terminal region. It catalyzes steps 6 and 7 of purine biosynthesis. The gene is closely linked and divergently transcribed with a locus that encodes an enzyme in the same pathway, and transcription of t…
- **Diseases (Open Targets)**: PAICS deficiency (0.606); Polyhydramnios (0.370); acute myeloid leukemia (0.165); neoplasm (0.107); non-small cell lung carcinoma (0.100)
- **Europe PMC papers**: 960
- **Why important**: PAICS is a bifunctional enzyme catalyzing successive steps in de novo purine biosynthesis and appears in both primary terms, (GO:BP nucleobase metabolic process; q_global = 0.022) and (GO:BP nucleoside phosphate biosynthetic process; q_global = 0.0233). It forms the strongest known STRING relationship in the module with ATIC, and it also participates in the supplementary nucleotide and multifunctional-enzyme signals (STRING RCTM Metabolism of nucleotides; within-query FDR = 0.0145) and (STRING Keyword Multifunctional enzyme; within-query FDR = 0.0374). Its position provides a direct biochemical bridge between the module's enrichment result and an established purine pathway.
- **Conclusion**: Established: PAICS is a core purine-biosynthetic component with direct network support from ATIC. Hypothesis: PAICS may be part of the metabolic core that drives the conserved cross-tissue co-abundance pattern, although the data do not show that its activity causes the pattern.

#### ATIC

- **Related proteins** (co-abundance neighbors): CTPS1 (0.81); STRING partners: PAICS (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase. This gene encodes a bifunctional protein that catalyzes the last two steps of the de novo purine biosynthetic pathway. The N-terminal domain has phosphoribosylaminoimidazolecarboxamide formyltransferase activity, and the C-terminal domain has IMP cyclohydrolase activity. A mutation in this gene results in AICA-ribosiduria. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: AICA-ribosiduria (0.708); cancer (0.571); Intellectual disability (0.463); lung adenocarcinoma (0.390); anaplastic large cell lymphoma (0.374)
- **Europe PMC papers**: 5200
- **Why important**: ATIC catalyzes the final stages of de novo purine biosynthesis, appears in (GO:BP nucleoside phosphate biosynthetic process; q_global = 0.0233), and has the strongest observed STRING link with PAICS. It has substantial literature support and established associations with AICA-ribosiduria and other disease contexts. Its biochemical position makes it especially useful for interpreting the module as a coordinated nucleotide-production program rather than a nonspecific collection of metabolic genes.
- **Conclusion**: Established: ATIC is a terminal de novo purine-pathway enzyme and is supported by both annotation and a known interaction with PAICS. Hypothesis: coordinated ATIC and PAICS abundance may indicate increased purine demand in the shared cellular state, but pathway flux has not been measured.

#### RRM1

- **Related proteins** (co-abundance neighbors): CTPS1 (0.82), FASN (0.81), RCC1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribonucleotide reductase catalytic subunit M1. This gene encodes the large and catalytic subunit of ribonucleotide reductase, an enzyme essential for the conversion of ribonucleotides into deoxyribonucleotides. A pool of available deoxyribonucleotides is important for DNA replication during S phase of the cell cycle as well as multiple DNA repair processes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec …
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.618); B-cell chronic lymphocytic leukemia (0.595); exocrine pancreatic carcinoma (0.584); sickle cell disease (0.581); ovarian carcinoma (0.571)
- **Europe PMC papers**: 5033
- **Why important**: RRM1 is a highly studied catalytic subunit of ribonucleotide reductase and appears in both primary terms, (GO:BP nucleobase metabolic process; q_global = 0.022) and (GO:BP nucleoside phosphate biosynthetic process; q_global = 0.0233), as well as the supplementary nucleotide-metabolism result (STRING RCTM Metabolism of nucleotides; within-query FDR = 0.0145). Its established function supplies deoxyribonucleotides for DNA replication and repair, connecting nucleotide metabolism to genome duplication and maintenance. Its disease associations include several cancers, including ovarian carcinoma, making it relevant to tissue-specific interpretation without implying a cancer mechanism here.
- **Conclusion**: Established: RRM1 links the module's nucleotide metabolism to deoxyribonucleotide production, DNA synthesis, and repair. Hypothesis: its inclusion may indicate replication or repair demand in the cell populations contributing to the bone–ovary module, but proliferation is not directly demonstrated.

#### FASN

- **Related proteins** (co-abundance neighbors): QARS1 (0.88), RRM1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fatty acid synthase. The enzyme encoded by this gene is a multifunctional protein. Its main function is to catalyze the synthesis of palmitate from acetyl-CoA and malonyl-CoA, in the presence of NADPH, into long-chain saturated fatty acids. In some cancer cell lines, this protein has been found to be fused with estrogen receptor-alpha (ER-alpha), in which the N-terminus of FAS is fused in-frame with the C-terminus of …
- **Diseases (Open Targets)**: dengue disease (0.469); autism spectrum disorder (0.333); Parkinson disease (0.295); Epileptic encephalopathy (0.211); neurodegenerative disease (0.205)
- **Europe PMC papers**: 21528
- **Why important**: FASN is a multifunctional fatty-acid synthase and the only module member in (GO:BP nucleoside phosphate biosynthetic process; q_global = 0.0233) that directly broadens the interpretation beyond nucleotide metabolism toward lipid biosynthesis. It has a highly studied literature record, is tissue enhanced in adipose tissue, breast, and liver, and is linked in the supplied annotations to osteoblast differentiation and fatty-acid metabolism. Its co-abundance links to QARS1 and RRM1 may reflect coupling between lipid production, translation, and nucleotide demand, although those links are not established physical interactions.
- **Conclusion**: Established: FASN provides an anabolic lipid-metabolism component and is included in the primary nucleoside-phosphate biosynthesis term (GO:BP nucleoside phosphate biosynthetic process; q_global = 0.0233). Hypothesis: FASN may indicate a broader growth or membrane-biogenesis state accompanying nucleotide production, but its role in this specific conserved module remains unresolved.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): QARS1 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 contributes a genome-maintenance and chromatin-related dimension through functions involving DNA repair, recombination, telomere maintenance, and replication regulation. It connects in the module to QARS1 and appears in the supplementary tissue-related signals (STRING TISSUES Male reproductive gland; within-query FDR = 0.0157), (STRING TISSUES Mammary gland; within-query FDR = 0.0471), and (STRING TISSUES Internal male genital organ; within-query FDR = 0.0471). Its testis-enhanced and spermatogenic-cell-associated HPA profile may help explain part of the reproductive-tissue signal, while its literature supports relevance to genome regulation and disease.
- **Conclusion**: Established: RUVBL2 is a nuclear and cytosolic ATPase associated with DNA and chromatin maintenance functions. Hypothesis: its co-abundance with biosynthetic enzymes may reflect a coordinated demand for genome maintenance during an active cellular state, but this interpretation is not supported by a primary GO term in the module.

## Module 15

**Tissue pair**: bone and ovary  
**Genes (5)**: KIF2A, KLC1, RPAP3, SWAP70, ZFR

### Function

The module does not have a globally significant GO or KEGG enrichment term, and STRING functional enrichment is absent. Its internal structure is a sparse chain-like network centered on KLC1, with links connecting KLC1 to ZFR, RPAP3, and KIF2A, and KIF2A linked to SWAP70. The gene annotations suggest a possible intersection of microtubule-based transport, mitotic and spindle organization, RNA-related regulation, protein stabilization, and actin or cell-adhesion regulation. Because these processes are heterogeneous and no enrichment term passed global correction, the most defensible conclusion is that the module represents a coordinated expression pattern rather than an established single biochemical pathway.

**Cell composition.** The module is not dominated by secreted proteins, since none of its members is annotated as secreted. Most members have low tissue specificity and low immune-cell specificity, which is consistent with broadly expressed intracellular or structural machinery rather than a strongly tissue-restricted program. HPA evidence does identify KLC1 with brain and Bergmann-glia enhancement, KIF2A with megakaryocyte and platelet grouping, and SWAP70 with B-cell, extravillous-trophoblast, vascular-endothelial, memory-B-cell, and naive-B-cell enrichment. Thus, blood or shared cell-type composition cannot be excluded, particularly for the KIF2A and SWAP70 signals, but the module as a whole is not demonstrably a plasma-protein or blood-cell module. Ovary protein detection is present for ZFR and RPAP3 but absent for the other assessed members, so the tissue-level interpretation should remain cautious.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship is reported among the module members, and no hu.MAP complex contains multiple module members. The co-abundance edges therefore are not supported by known high-confidence physical interactions or a shared curated complex. This does not invalidate the module: co-abundance can arise from shared cellular state, regulation, localization, or indirect pathway coupling. It does mean that the network should not be described as a known protein complex, and that the apparent KLC1 center is a co-expression feature rather than a demonstrated physical hub.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a new tissue-pair co-abundance observation, but it is not sufficient to claim a new molecular pathway or new protein interaction. The absence of STRING and hu.MAP support is compatible with novelty, yet absence from those resources alone does not prove novelty. The lack of globally significant GO or KEGG enrichment and the heterogeneous annotations instead support a cautious claim: the potentially novel finding is the shared bone–ovary co-abundance pattern involving these genes, which requires independent replication and adjustment for cell composition before being assigned a specific mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of cytoskeletal transport and cellular remodeling in a shared bone–ovary cellular or physiological state. KLC1 may link cargo transport to the microtubule system; KIF2A may connect that system to spindle, microtubule-depolymerization, and migration processes; SWAP70 may connect microtubule-linked state to actin organization, calcium handling, and integrin-related adhesion; and ZFR or RPAP3 may report accompanying RNA-regulatory or protein-stabilization changes. An alternative hypothesis is that the pattern is partly driven by shared or variable cellular composition, especially platelet, B-cell, endothelial, or trophoblast-related signals. These are hypotheses, not established causal relationships from the supplied evidence.

### Important genes

#### KLC1

- **Related proteins** (co-abundance neighbors): ZFR (0.89), RPAP3 (0.84), KIF2A (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Acrosome, Equatorial segment; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin light chain 1. Conventional kinesin is a tetrameric molecule composed of two heavy chains and two light chains, and transports various cargos along microtubules toward their plus ends. The heavy chains provide the motor activity, while the light chains bind to various cargos. This gene encodes a member of the kinesin light chain family. It associates with kinesin heavy chain through an N-terminal domain, and six…
- **Diseases (Open Targets)**: mitochondrial complex IV deficiency, nuclear type 17 (0.544); cancer (0.465); neurodegenerative disease (0.452); leigh syndrome due to mitochondrial complex iv deficiency (0.427); mitochondrial complex IV deficiency, nuclear-type (0.427)
- **Europe PMC papers**: 1114
- **Why important**: KLC1 is the apparent network center, connecting to ZFR, RPAP3, and KIF2A, and its annotation provides the clearest mechanistic anchor through kinesin cargo transport and microtubule-based movement. It also has substantial literature coverage and disease associations involving mitochondrial complex dysfunction, cancer, and neurodegenerative disease. HPA suggests brain and Bergmann-glia specialization, while the protein is not detected in ovary by the supplied IHC result.
- **Conclusion**: Established: KLC1 is a kinesin light-chain cargo adaptor associated with microtubule transport, and it is the most connected member of this module. Hypothesis: KLC1 may organize the shared module by coordinating transport-related cellular state with the other genes; the co-abundance data do not establish direct physical binding to the listed neighbors.

#### KIF2A

- **Related proteins** (co-abundance neighbors): SWAP70 (0.82), KLC1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Centrosome, Basal body, Annulus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 2A. The protein encoded by this gene is a plus end-directed motor required for normal mitotic progression. The encoded protein is required for normal spindle activity during mitosis and is necessary for normal brain development. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2011].
- **Diseases (Open Targets)**: Genetic central nervous system malformation (0.749); neurodegenerative disease (0.403); ovarian neoplasm (0.342); diabetes mellitus (0.307); major depressive disorder (0.302)
- **Europe PMC papers**: 1206
- **Why important**: KIF2A links KLC1 to SWAP70 and is annotated for mitotic progression, spindle organization, microtubule depolymerization, chromosome segregation, and cell migration. It has substantial literature coverage and an association with ovarian neoplasm among its reported disease links. HPA groups it with megakaryocytes and platelets, making it important both mechanistically and as a possible indicator of cellular-composition effects.
- **Conclusion**: Established: KIF2A is a microtubule motor-related regulator with roles in mitosis and microtubule organization. Hypothesis: it may connect transport and remodeling signals in the module, although platelet or megakaryocyte composition could also contribute to its co-abundance.

#### SWAP70

- **Related proteins** (co-abundance neighbors): KIF2A (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: switching B cell complex subunit SWAP70. Enables cadherin binding activity. Predicted to be involved in regulation of actin polymerization or depolymerization. Predicted to act upstream of or within isotype switching. Located in actin cytoskeleton; cytoplasm; and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypertensive disorder (0.578); essential hypertension (0.528); cardiovascular disorder (0.483); coronary artery disorder (0.474); hypothyroidism (0.470)
- **Europe PMC papers**: 596
- **Why important**: SWAP70 is the module member connected to KIF2A at the opposite end of the observed network and has annotations for actin regulation, calcium concentration, protein localization, cadherin binding, and integrin-related cell adhesion. Its HPA profile includes B-cell, trophoblast, and vascular-endothelial enrichment, as well as memory-B-cell and naive-B-cell enhancement. These features make it important for linking the proposed cytoskeletal interpretation to possible immune or stromal composition.
- **Conclusion**: Established: SWAP70 is associated with actin and adhesion-related cellular functions and shows immune-cell-enhanced HPA evidence. Hypothesis: it may couple microtubule-associated state to actin or adhesion remodeling, but the module does not distinguish regulation within bone or ovary from variation in B-cell, vascular, or trophoblast content.

#### ZFR

- **Related proteins** (co-abundance neighbors): KLC1 (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger RNA binding protein. This gene encodes an RNA-binding protein characterized by its DZF (domain associated with zinc fingers) domain. The encoded protein may play a role in the nucleocytoplasmic shuttling of another RNA-binding protein, Staufen homolog 2, in neurons. Expression of this gene is regulated through alternative polyadenylation that mediates differential microRNA targeting. Elevated expression of this gene h…
- **Diseases (Open Targets)**: neurodegenerative disease (0.483); autosomal recessive spastic paraplegia type 71 (0.370); hyperaldosteronism (0.320); placental abruption (0.311); hearing loss disorder (0.242)
- **Europe PMC papers**: 793
- **Why important**: ZFR is directly connected to KLC1 and contributes an RNA-regulatory dimension to an otherwise cytoskeletal-looking interpretation. It is a nucleoplasmic RNA-binding protein with reported roles in RNA-protein shuttling and alternative polyadenylation, has disease associations involving neurodegenerative and other disorders, and has ovary protein detection in the supplied HPA evidence.
- **Conclusion**: Established: ZFR is an RNA-binding protein with nucleoplasmic localization and reported RNA-regulatory functions. Hypothesis: ZFR may reflect post-transcriptional coordination of the module rather than a physical component of the kinesin system; the available evidence does not establish that link.

#### RPAP3

- **Related proteins** (co-abundance neighbors): KLC1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase II associated protein 3. This gene encodes an RNA polymerase II-associated protein. The encoded protein may function in transcriptional regulation and may also regulate apoptosis. Alternatively spliced transcript variants have been described. [provided by RefSeq, Mar 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.418); cardiovascular disorder (0.255); spermatocele (0.204); lysosomal storage disease (0.115); alcohol drinking (0.094)
- **Europe PMC papers**: 334
- **Why important**: RPAP3 is connected to KLC1 and supplies a protein-stabilization and transcription-associated interpretation. It is a cytosolic RNA polymerase-associated protein with reported roles in transcriptional regulation, apoptosis, and protein stabilization. Its ovary protein detection and disease-association record make it relevant to the bone–ovary context, although its literature volume is more limited than that of KLC1 or KIF2A.
- **Conclusion**: Established: RPAP3 is associated with RNA polymerase-related regulation and protein stabilization. Hypothesis: it may mark a shared proteostasis or transcriptional state that accompanies cytoskeletal remodeling, but there is no evidence here for a direct RPAP3–KLC1 complex or a module-specific causal role.

## Module 16

**Tissue pair**: bone and ovary  
**Genes (5)**: MCM2, MCM4, MCM5, MCM6, MCM7

### Function

This module is a coherent replication-associated module consisting entirely of MCM2, MCM4, MCM5, MCM6 and MCM7. The primary GO and KEGG evidence is exceptionally concordant: every module gene contributes to the MCM complex, DNA replication initiation, the DNA replication preinitiation and CMG complexes, helicase activity, cell-cycle DNA replication and DNA repair or recombination terms (26 globally significant GO/KEGG terms, q_global 5.41e-10–4.28e-05; see the table), (GO:BP double-strand break repair; q_global = 0.000123) (GO:BP DNA recombination; q_global = 0.00016) (GO:BP DNA replication; q_global = 0.000246), (GO:BP DNA repair; q_global = 0.00172), (GO:BP DNA damage response; q_global = 0.00752), (GO:BP DNA metabolic process; q_global = 0.0115) and (GO:CC chromosome; q_global = 0.0493). The KEGG DNA replication and cell-cycle terms provide pathway-level support (KEGG DNA replication - Homo sapiens (human); q_global = 4.97e-07) and (KEGG Cell cycle - Homo sapiens (human); q_global = 5.75e-06), while homologous recombination is also represented (4 globally significant GO/KEGG terms, q_global 6.7e-06–1.89e-05; see the table). The module therefore most directly reflects assembly or abundance of the MCM replicative helicase and associated replication machinery, rather than a tissue-specific secretory function. The break-induced-replication and replication-stress-related annotations support a role extending to replication-fork maintenance and DNA damage responses (GO:BP double-strand break repair via break-induced replication; q_global = 2.41e-09), (GO:BP double-strand break repair via homologous recombination; q_global = 1.68e-05), (GO:BP double-strand break repair; q_global = 0.000123), (GO:BP DNA repair; q_global = 0.00172) and (5 supplementary STRING terms; within-query FDR 6.28e-09–1.01e-08).

**Cell composition.** All module genes encode nucleoplasmic MCM proteins, and none is annotated as secreted. HPA indicates tissue enhancement primarily in bone marrow and lymphoid tissue, with cell-type enhancement across erythrocyte progenitors, megakaryocyte progenitors and monocyte progenitors; trophoblast enrichment is also present for some genes. Every gene has low immune-cell specificity in the supplied HPA summary, so this is not evidence for a mature immune-cell program. The shared bone–ovary signal may therefore reflect proliferating or progenitor-like cells, cell-cycle state, or blood and marrow-related material in the samples rather than a function unique to bone or ovary. HPA protein detection is available for ovary but not matching bone tissue: MCM2, MCM4 and MCM7 are detected in ovary, whereas MCM5 and MCM6 are not detected there. These observations support cautious interpretation of tissue specificity and do not establish that the module originates from blood contamination.

**GO/KEGG enrichment**: 54 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC MCM complex | 5.41e-10 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP double-strand break repair via break-induced replication | 2.41e-09 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication initiation | 2.41e-09 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication | 6.55e-09 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC DNA replication preinitiation complex | 1.56e-08 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC CMG complex | 1.56e-08 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF four-way junction helicase activity | 8.74e-08 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF forked DNA-dependent helicase activity | 8.74e-08 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF double-stranded DNA helicase activity | 1.32e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF 3'-5' DNA helicase activity | 1.32e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded 3'-5' DNA helicase activity | 1.32e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP DNA replication initiation | 1.96e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded DNA helicase activity | 4.97e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| KEGG DNA replication - Homo sapiens (human) | 4.97e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded DNA binding | 1.34e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |

### STRING and hu.MAP

STRING supports a fully connected set of pairwise relationships among the module genes, with every possible gene pair represented at the supplied high-confidence threshold. Its supplementary enrichment identifies the MCM complex, MCM domains, the CMG complex, DNA unwinding, pre-replicative-complex activation and replication-stress responses (15 supplementary STRING terms; within-query FDR 8.29e-10–1.01e-08). These are consistent with the primary GO and KEGG results but remain supplementary because STRING enrichment was not corrected across modules. hu.MAP independently places the genes in multiple complexes containing most or all of the module, including an MCM complex with MCMBP (hu.MAP huMAP3_05529.1), and larger replisome or CMG-related complexes containing MCM3, CDC45, GINS proteins, TIPIN, CLSPN and TIMELESS (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1), (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_08848.1). Thus, the network is not merely a statistical association: it recapitulates a known physical and functional replication machinery, while the absence of other replisome components from this module likely reflects module selection rather than absence from the cellular complexes.

**STRING interactions (score >= 0.7)**: 10 of 10 gene pairs: MCM2–MCM4 (0.999); MCM2–MCM5 (0.999); MCM2–MCM6 (0.999); MCM2–MCM7 (0.999); MCM4–MCM5 (0.999); MCM4–MCM6 (0.999); MCM4–MCM7 (0.999); MCM5–MCM6 (0.999); MCM5–MCM7 (0.999); MCM6–MCM7 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component MCM complex (FDR = 8.29e-10, 5 genes); COMPARTMENTS MCM complex (FDR = 8.89e-10, 5 genes); InterPro MCM domain (FDR = 1.19e-09, 5 genes); InterPro Mini-chromosome maintenance, conserved site (FDR = 1.19e-09, 5 genes); InterPro MCM N-terminal domain (FDR = 1.19e-09, 5 genes); InterPro Mini-chromosome maintenance protein (FDR = 1.19e-09, 5 genes); InterPro MCM OB domain (FDR = 1.19e-09, 5 genes); InterPro MCM, AAA-lid domain (FDR = 1.19e-09, 5 genes); Component CMG complex (FDR = 2.12e-09, 5 genes); COMPARTMENTS CMG complex (FDR = 2.27e-09, 5 genes); RCTM Unwinding of DNA (FDR = 6.28e-09, 5 genes); RCTM Activation of the pre-replicative complex (FDR = 7.32e-09, 5 genes); Process Double-strand break repair via break-induced replication (FDR = 9.59e-09, 5 genes); Process Regulation of DNA-templated DNA replication initiation (FDR = 9.59e-09, 5 genes); RCTM Activation of ATR in response to replication stress (FDR = 1.01e-08, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05529.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/6); huMAP3_14758.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/14); huMAP3_08554.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_11832.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_12180.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/17); huMAP3_06061.1 (MCM4, MCM7, MCM2, MCM6; 4/5); huMAP3_07113.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_11119.1 (MCM4, MCM5, MCM7, MCM6; 4/14); huMAP3_09860.1 (MCM4, MCM2, MCM6; 3/4); huMAP3_00154.1 (MCM4, MCM2, MCM6; 3/5); huMAP3_09466.1 (MCM4, MCM2, MCM6; 3/23); huMAP3_10862.1 (MCM4, MCM2, MCM6; 3/33); huMAP3_14306.1 (MCM4, MCM2, MCM6; 3/55); huMAP3_02602.1 (MCM4, MCM6; 2/2); huMAP3_09238.1 (MCM5, MCM7; 2/11); huMAP3_08848.1 (MCM4, MCM6; 2/15)

### Novelty

The molecular interpretation is not a newly discovered MCM function. The complete MCM-centered structure is strongly supported by established STRING relationships, hu.MAP complexes, MyGene descriptions and extensive literature annotations for each gene. The potentially novel result is the recurrence of this coherent MCM abundance pattern as a conserved module in the bone–ovary tissue pair, but the fact sheet does not provide comparison with prior tissue-pair module studies, independent cohorts, or experimental validation. Consequently, this should be described as a potentially interesting tissue-context observation, not as a new replication complex or a proven bone–ovary-specific mechanism. Absence of a relationship from a database would not by itself establish novelty; here, the databases instead provide extensive prior support.

**Hypothesis.** Hypothesis: the conserved bone–ovary module reflects coordinated abundance of the MCM helicase core in proliferating progenitor-like or cycling cells shared between the sampled tissues. In this model, increased or decreased module abundance marks the availability of replication-licensing and fork-protection machinery, with possible coupling to replication stress and DNA repair. The HPA enrichment for hematopoietic progenitor populations raises the alternative possibility that shared marrow-derived or blood-associated cellular composition contributes to the signal. This hypothesis should be tested by examining cell-cycle markers, mature blood-cell markers, additional replisome components, and cell-type-resolved data, rather than inferred from co-abundance alone.

### Important genes

#### MCM2

- **Related proteins** (co-abundance neighbors): MCM6 (0.86), MCM7 (0.85), MCM5 (0.84); STRING partners: MCM4 (0.999), MCM5 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a central member of the module network, connects to the other MCM genes in STRING, and is present in many hu.MAP complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1), (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1). It contributes to every primary enrichment term (54 globally significant GO/KEGG terms, q_global 5.41e-10–0.0493; see the table), is detected in ovary by HPA, and has the largest supplied literature volume among the module genes. Its MyGene annotation places it in the prereplication complex and replication-fork machinery, while the supplied disease associations include hearing-loss phenotypes and gastrointestinal abnormalities.
- **Conclusion**: Established evidence supports MCM2 as a core replication-licensing component and a strong representative marker of this module. It is not established from these data that MCM2 specifically drives the bone–ovary association or any of the supplied disease relationships.

#### MCM6

- **Related proteins** (co-abundance neighbors): MCM4 (0.92), MCM5 (0.88), MCM2 (0.86); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 6. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: lactose intolerance (0.246); neurodegenerative disease (0.225); obesity disorder (0.166); nervous system disorder (0.141); systemic lupus erythematosus (0.140)
- **Europe PMC papers**: 3766
- **Why important**: MCM6 has the strongest weighted network position in the supplied module and participates in nearly all listed hu.MAP complexes, including the compact MCM complex and larger replisome assemblies (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_08848.1). It contributes to the complete set of primary GO and KEGG terms (54 globally significant GO/KEGG terms, q_global 5.41e-10–0.0493; see the table). HPA places it in nucleoplasm with enhancement in lymphoid tissue and multiple progenitor populations, while MyGene describes its role in the conserved MCM helicase and replication-fork machinery. Its supplied literature volume is substantial, and Open Targets lists several disease associations.
- **Conclusion**: Established evidence supports MCM6 as a structurally central MCM-core component and a plausible abundance marker for replication machinery. Its network position does not demonstrate that it is a regulatory hub or causal mediator in bone or ovary.

#### MCM4

- **Related proteins** (co-abundance neighbors): MCM6 (0.92); STRING partners: MCM2 (0.999), MCM5 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 4. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication rel…
- **Diseases (Open Targets)**: primary immunodeficiency with natural-killer cell deficiency and adrenal insufficiency (0.714); X-linked adrenal hypoplasia congenita (0.185); lung adenocarcinoma (0.112); microcephaly (0.111); neoplasm (0.102)
- **Europe PMC papers**: 4082
- **Why important**: MCM4 is a constituent of every primary enrichment term (54 globally significant GO/KEGG terms, q_global 5.41e-10–0.0493; see the table), has STRING relationships with all other module genes, and appears across the compact MCM and larger hu.MAP replication complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_08848.1). HPA reports bone-marrow enhancement and ovary protein detection. MyGene identifies MCM4 as a conserved MCM protein involved in replication initiation and fork-associated functions. The supplied disease associations include natural-killer-cell deficiency with adrenal insufficiency, adrenal hypoplasia congenita, microcephaly and neoplasm, and its literature volume is substantial.
- **Conclusion**: Established evidence supports MCM4 as an essential MCM-complex constituent with relevance to replication and genome maintenance. The disease associations do not show that this module causes disease in the sampled tissues.

#### MCM5

- **Related proteins** (co-abundance neighbors): MCM7 (0.92), MCM6 (0.88), MCM2 (0.84); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 5. The protein encoded by this gene is structurally very similar to the CDC46 protein from S. cerevisiae, a protein involved in the initiation of DNA replication. The encoded protein is a member of the MCM family of chromatin-binding proteins and can interact with at least two other members of this family. The encoded protein is upregulated in the transition from the G0 to G1/S phase of the cell cycl…
- **Diseases (Open Targets)**: Meier-Gorlin syndrome (0.563); neurodegenerative disease (0.397); lysosomal storage disease (0.362); kidney transplant (0.198); diabetic ketoacidosis (0.129)
- **Europe PMC papers**: 4143
- **Why important**: MCM5 is fully integrated into the STRING-supported MCM network and occurs in the principal hu.MAP MCM and replisome complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1), (hu.MAP huMAP3_11119.1) and (hu.MAP huMAP3_09238.1). It contributes to the primary replication, helicase, repair and cell-cycle annotations (35 globally significant GO/KEGG terms, q_global 5.41e-10–0.00083; see the table), (14 globally significant GO/KEGG terms, q_global 0.00122–0.0128; see the table) and (GO:CC chromosome; q_global = 0.0493). HPA reports bone-marrow enhancement and enrichment in progenitor and trophoblast populations. MyGene describes its chromatin-binding and replication-initiation roles, and the supplied disease associations include Meier–Gorlin syndrome and other disorders.
- **Conclusion**: Established evidence supports MCM5 as a conserved replication-initiation component and a useful indicator of the module's proliferative biology. The progenitor and trophoblast enrichment suggests a possible composition effect, but does not establish the cellular source of the bone–ovary signal.

#### MCM7

- **Related proteins** (co-abundance neighbors): MCM5 (0.92), MCM2 (0.85); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM6 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 completes the module's MCM core and is connected by STRING to every other module gene. It appears in the principal hu.MAP complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) and (hu.MAP huMAP3_09238.1), contributes to the primary MCM, replication, helicase, repair and cell-cycle terms (35 globally significant GO/KEGG terms, q_global 5.41e-10–0.00083; see the table), (14 globally significant GO/KEGG terms, q_global 0.00122–0.0128; see the table) and (GO:CC chromosome; q_global = 0.0493), and is detected in ovary by HPA. MyGene identifies it as a conserved MCM protein involved in replication initiation and fork-related functions. The supplied disease associations include Meier–Gorlin syndrome, microcephaly, spastic paraplegia and AP-four deficiency syndrome, and its literature volume is substantial.
- **Conclusion**: Established evidence supports MCM7 as a core component of the replicative helicase and a robust marker of this module. Its presence does not by itself distinguish active replication from increased representation of cycling cells.

## Module 17

**Tissue pair**: bone and ovary  
**Genes (5)**: PRRC2A, PRRC2C, RPP30, RPP40, ZC3H4

### Function

The strongest interpretation is a nuclear RNA-processing module centered on ribonuclease P and ribonuclease MRP biology. The primary evidence is the shared enrichment of RPP30 and RPP40 in the ribonuclease MRP complex (GO:CC ribonuclease MRP complex; q_global = 0.0463) and the nucleolar ribonuclease P complex (GO:CC nucleolar ribonuclease P complex; q_global = 0.0463). RPP30 and RPP40 are annotated as ribonuclease P or MRP subunits involved in tRNA leader removal and RNA processing. Their very strong STRING relationship and repeated hu.MAP membership support a real molecular core rather than an arbitrary co-abundance pairing. PRRC2A and PRRC2C contribute a second, cytoplasmic RNA-regulatory or stress-granule-associated signal, supported by the BAT2 or PRRC2 domain annotations (STRING Pfam BAT2 N-terminus; within-query FDR = 0.0093) (STRING InterPro BAT2, N-terminal; within-query FDR = 0.0397) (STRING InterPro Protein PRRC2; within-query FDR = 0.0397) and their shared hu.MAP complex (hu.MAP huMAP3_08887.1). ZC3H4 is consistent with nuclear RNA surveillance and post-transcriptional regulation, but it has no primary GO or KEGG enrichment in this module. Overall, the module most plausibly reflects coordinated RNA maturation and RNA homeostasis, with a well-established ribonuclease P/MRP core and a less firmly established connection to cytoplasmic RNA regulation.

**Cell composition.** This is not a plasma-protein, secreted-protein, or blood-cell-enriched module. HPA reports no secreted genes, generally low tissue specificity, and low immune-cell specificity across the module. The genes are predominantly intracellular, with nucleoplasmic, nucleolar, or cytosolic localization. Several genes show enhancement in reproductive or specialized cell types, including oocytes, late primary spermatocytes, differentiating spermatogonia, decidual stromal cells, and podocytes, but there is no recurrent tissue-enriched pattern. The ovary protein evidence is mixed, while bone lacks matching HPA tissue protein data. Thus, the shared bone–ovary signal is more consistent with a broadly used intracellular RNA-processing program, possibly accentuated by shared cell states, than with contamination by circulating proteins or blood cells. The absence of a tissue-specific HPA pattern also limits any claim that this module is intrinsically bone- or ovary-specific.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC ribonuclease MRP complex | 0.0463 | RPP30, RPP40 |
| GO:CC nucleolar ribonuclease P complex | 0.0463 | RPP30, RPP40 |

### STRING and hu.MAP

STRING provides strong support for the RPP30–RPP40 relationship, which is the only high-confidence STRING relationship among the module genes. STRING functional annotations independently place RPP30 and RPP40 in ribonuclease P or MRP compartments (STRING COMPARTMENTS Ribonuclease MRP complex; within-query FDR = 0.0492) and (STRING COMPARTMENTS Nucleolar ribonuclease P complex; within-query FDR = 0.0492), while the PRRC2A–PRRC2C pair shares BAT2 or PRRC2-related annotations (STRING Pfam BAT2 N-terminus; within-query FDR = 0.0093) (STRING InterPro BAT2, N-terminal; within-query FDR = 0.0397) (STRING InterPro Protein PRRC2; within-query FDR = 0.0397). These STRING results are supplementary and do not replace the globally corrected GO evidence. hu.MAP repeatedly places RPP30 and RPP40 together in complexes containing additional ribonuclease P or MRP components (hu.MAP huMAP3_06709.1) (hu.MAP huMAP3_08418.1) (hu.MAP huMAP3_12090.1) (hu.MAP huMAP3_08469.1). hu.MAP also places PRRC2A and PRRC2C together in a separate complex (hu.MAP huMAP3_08887.1). Therefore, the module contains two database-supported relationship blocks: a ribonuclease P/MRP block and a PRRC2 block. The co-abundance links connecting these blocks, particularly links involving ZC3H4, are not established physical interactions in the supplied databases and should be treated as associations requiring validation.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: RPP30–RPP40 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam BAT2 N-terminus (FDR = 0.0093, 2 genes); InterPro BAT2, N-terminal (FDR = 0.0397, 2 genes); InterPro Protein PRRC2 (FDR = 0.0397, 2 genes); COMPARTMENTS Ribonuclease MRP complex (FDR = 0.0492, 2 genes); COMPARTMENTS Nucleolar ribonuclease P complex (FDR = 0.0492, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08887.1 (PRRC2A, PRRC2C; 2/2); huMAP3_06709.1 (RPP40, RPP30; 2/11); huMAP3_08418.1 (RPP40, RPP30; 2/13); huMAP3_12090.1 (RPP40, RPP30; 2/13); huMAP3_08469.1 (RPP40, RPP30; 2/14)

### Novelty

The ribonuclease P/MRP component of the module is not a new molecular finding: RPP30–RPP40 association, their RNA-processing functions, STRING relationship, and repeated hu.MAP complex membership are already established. The PRRC2A–PRRC2C association is also represented in hu.MAP and supported by shared domain-level STRING annotations. What may be less established is their coordinated co-abundance with one another and with ZC3H4 across bone and ovary. However, the fact sheet does not establish that this cross-tissue co-abundance configuration is absent from prior datasets, and absence of STRING or hu.MAP relationships does not demonstrate novelty. The appropriate conclusion is that the module may represent a potentially interesting cross-tissue regulatory association, but it should not be called a new biological complex or a novel pathway without independent replication, perturbation, and comparison with existing co-expression studies.

**Hypothesis.** Hypothesis: in shared bone and ovary cellular contexts, a constitutive ribonuclease P/MRP RNA-processing core involving RPP30 and RPP40 may be co-regulated with RNA-surveillance or post-transcriptional regulators involving ZC3H4, PRRC2A, and PRRC2C. This could coordinate nuclear RNA maturation with cytoplasmic translation control or stress-granule responses during cell-state transitions. The hypothesis is compatible with the localization and annotations in the fact sheet, but the cross-block mechanism is not established by the available physical-interaction evidence. Testing should determine whether these genes are co-regulated in the same cell populations and whether perturbing the PRRC2 or ZC3H4 components changes ribonuclease P/MRP activity, tRNA processing, or cellular stress responses.

### Important genes

#### RPP40

- **Related proteins** (co-abundance neighbors): RPP30 (0.92), PRRC2A (0.82); STRING partners: RPP30 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06709.1, huMAP3_08418.1, huMAP3_12090.1, huMAP3_08469.1
- **Function (MyGene.info)**: ribonuclease P/MRP subunit p40. Enables ribonuclease P RNA binding activity. Contributes to ribonuclease P activity. Involved in tRNA 5'-leader removal. Part of multimeric ribonuclease P complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.480); familial hemolytic anemia (0.186); keratinocyte carcinoma (0.117); squamous cell carcinoma (0.117); basal cell carcinoma (0.111)
- **Europe PMC papers**: 248
- **Why important**: RPP40 is a central network node, connecting the RPP30 ribonuclease P/MRP component to PRRC2A. It is present in the primary ribonuclease MRP and nucleolar ribonuclease P terms (GO:CC ribonuclease MRP complex; q_global = 0.0463) and (GO:CC nucleolar ribonuclease P complex; q_global = 0.0463), has the strongest STRING relationship with RPP30, and recurs across several hu.MAP ribonuclease P or MRP complexes (hu.MAP huMAP3_06709.1) (hu.MAP huMAP3_08418.1) (hu.MAP huMAP3_12090.1) (hu.MAP huMAP3_08469.1). Its annotated roles in tRNA leader removal and ribosomal RNA processing make it a direct mechanistic anchor. Its literature base is substantial, although less extensive than that of RPP30.
- **Conclusion**: Established evidence supports RPP40 as a bona fide ribonuclease P/MRP subunit and an important structural and functional anchor of the module. Its connection to PRRC2A is a co-abundance relationship rather than an established direct physical interaction. A role for RPP40 in linking the two apparent module blocks remains a hypothesis.

#### RPP30

- **Related proteins** (co-abundance neighbors): RPP40 (0.92); STRING partners: RPP40 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06709.1, huMAP3_08418.1, huMAP3_12090.1, huMAP3_08469.1
- **Function (MyGene.info)**: ribonuclease P/MRP subunit p30. Enables ribonuclease P RNA binding activity. Contributes to ribonuclease P activity. Involved in tRNA 5'-leader removal. Part of multimeric ribonuclease P complex and ribonuclease MRP complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); alcohol drinking (0.297); ovarian dysfunction (0.260); Chest pain (0.230); hyperpituitarism (0.205)
- **Europe PMC papers**: 1572
- **Why important**: RPP30 is the most strongly documented core component of the module. It shares the primary global GO evidence with RPP40 (GO:CC ribonuclease MRP complex; q_global = 0.0463) and (GO:CC nucleolar ribonuclease P complex; q_global = 0.0463), has the high-confidence STRING relationship with RPP40, and appears with RPP40 in multiple hu.MAP complexes (hu.MAP huMAP3_06709.1) (hu.MAP huMAP3_08418.1) (hu.MAP huMAP3_12090.1) (hu.MAP huMAP3_08469.1). Its established functions include ribonuclease P activity, tRNA leader removal, tRNA processing, and ribonuclease MRP-associated RNA processing. It also has the deepest literature support among the module genes and an Open Targets association with ovarian dysfunction.
- **Conclusion**: Established evidence identifies RPP30 as a core RNA-processing subunit and the clearest functional representative of the module. The ovarian disease association is supportive context rather than proof that this module causes ovarian dysfunction. Its broader co-abundance with the other genes remains to be mechanistically demonstrated.

#### PRRC2A

- **Related proteins** (co-abundance neighbors): ZC3H4 (0.84), RPP40 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08887.1
- **Function (MyGene.info)**: proline rich coiled-coil 2A. A cluster of genes, BAT1-BAT5, has been localized in the vicinity of the genes for TNF alpha and TNF beta. These genes are all within the human major histocompatibility complex class III region. This gene has microsatellite repeats which are associated with the age-at-onset of insulin-dependent diabetes mellitus (IDDM) and possibly thought to be involved with the inflammatory process of pancreatic…
- **Diseases (Open Targets)**: neurodegenerative disease (0.477); neoplasm (0.085); hepatocellular carcinoma (0.079); colorectal carcinoma (0.074); type 1 diabetes mellitus (0.051)
- **Europe PMC papers**: 993
- **Why important**: PRRC2A connects the ribonuclease P/MRP side of the network to PRRC2C and ZC3H4. It is part of the hu.MAP complex shared with PRRC2C (hu.MAP huMAP3_08887.1) and carries the BAT2 or PRRC2-related STRING annotations (STRING Pfam BAT2 N-terminus; within-query FDR = 0.0093) (STRING InterPro BAT2, N-terminal; within-query FDR = 0.0397) (STRING InterPro Protein PRRC2; within-query FDR = 0.0397). Its annotations support mRNA stabilization and regulation of cytoplasmic translation, and it is associated with stress-granule-related RNA regulation. It also has a relatively extensive literature record and disease-context associations including neurodegenerative disease and type one diabetes.
- **Conclusion**: Established evidence supports PRRC2A as a cytoplasmic RNA-regulatory protein and as a member of a PRRC2A–PRRC2C complex. Its role as a functional bridge to RPP40 or ZC3H4 is not established by the supplied physical-interaction databases and should be regarded as a testable hypothesis.

#### PRRC2C

- **Related proteins** (co-abundance neighbors): ZC3H4 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_08887.1
- **Function (MyGene.info)**: proline rich coiled-coil 2C. Enables protein C-terminus binding activity. Involved in stress granule assembly. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.425); neurodegenerative disease (0.387); mathematical ability (0.278); alcohol drinking (0.250); intelligence (0.209)
- **Europe PMC papers**: 327
- **Why important**: PRRC2C is the network partner of ZC3H4 and the hu.MAP partner of PRRC2A (hu.MAP huMAP3_08887.1). Its shared BAT2 or PRRC2 annotations (STRING Pfam BAT2 N-terminus; within-query FDR = 0.0093) (STRING InterPro BAT2, N-terminal; within-query FDR = 0.0397) (STRING InterPro Protein PRRC2; within-query FDR = 0.0397) and established involvement in stress-granule assembly and regulation of cytoplasmic translation provide a plausible RNA-homeostasis connection to PRRC2A. Its Open Targets annotations include skeletal-system abnormality and neurodegenerative disease, which are relevant context for a bone-associated module but do not establish causation.
- **Conclusion**: Established evidence supports PRRC2C as a cytoplasmic RNA-regulatory and stress-granule-associated protein that belongs to the PRRC2A-containing complex. Its relationship to the nuclear ribonuclease P/MRP core is an association observed in the module, not an established biochemical mechanism.

#### ZC3H4

- **Related proteins** (co-abundance neighbors): PRRC2A (0.84), PRRC2C (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger CCCH-type containing 4. This gene encodes a member of a family of CCCH (C-x8-C-x5-C-x3-H type) zinc finger domain-containing proteins. These zinc finger domains, which coordinate zinc finger binding and are characterized by three cysteine residues and one histidine residue, are nucleic acid-binding. Other family members are known to function in post-transcriptional regulation. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.415); Abnormality of the skeletal system (0.355); Chest pain (0.352); neurodegenerative disease (0.344); obesity disorder (0.293)
- **Europe PMC papers**: 309
- **Why important**: ZC3H4 is connected to both PRRC2A and PRRC2C in the module and is the only member without supplied STRING partners, hu.MAP complexes, or enriched GO or KEGG terms. Its annotations nevertheless point to nuclear RNA surveillance, lncRNA catabolism, and negative regulation of transcriptional elongation. Its presence may therefore represent a regulatory layer that is not captured by the known ribonuclease P/MRP complexes. It also has a substantial literature record and Open Targets associations involving skeletal-system abnormality and neurodegenerative disease.
- **Conclusion**: Established evidence supports ZC3H4 as a nuclear nucleic-acid-binding and RNA-surveillance regulator, but does not establish its participation in the ribonuclease P/MRP or PRRC2 complexes represented here. Its placement in the module is therefore the most hypothesis-generating aspect and requires direct validation.
