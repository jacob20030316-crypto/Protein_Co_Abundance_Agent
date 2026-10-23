# Conserved co-abundance modules: autonomic_nervous_system and circulatory_system

## Module 0

**Tissue pair**: autonomic_nervous_system and circulatory_system  
**Genes (43)**: HIBADH, GOT2, ABHD14B, ALG5, ARAP1, BCL2L1, CFAP20, CLTB, DECR1, EGFR, ENDOD1, FAM241A, FKBP5, FTH1, GHDC, HMGA1, MTIF2, ILK, ITGB1, KATNAL1, KLC1, LMNB2, IMMT, MSH6, MTAP, NCSTN, OPA1, REXO2, PCF11, PHPT1, ARHGAP5, POLR3B, SLC27A4, SAPCD2, SLC6A6, SEPTIN11, SNX6, SSR1, STOM, TRMT11, ATP6V1C1, VCL, RP2

### Function

This module does not support a single statistically established GO or KEGG function: no GO/KEGG term passed global correction. The gene-level evidence instead points to a mixed cellular program involving cell adhesion and mechanotransduction, membrane and receptor trafficking, cytoskeletal organization, mitochondrial maintenance, and general intracellular transport. The strongest coherent substructure is the adhesion-associated chain involving FAM241A, ILK, ITGB1, and VCL, with EGFR connected to ITGB1 and BCL2L1 connected to EGFR in STRING. The module also contains genes involved in endosomal sorting, clathrin-dependent transport, V-ATPase-dependent compartment acidification, mitochondrial organization and metabolism, RNA processing, and cell-cycle or nuclear functions. Thus, the most defensible interpretation is a broad membrane–cytoskeleton–organelle homeostasis module rather than a narrowly defined pathway. The mixed annotations and lack of globally corrected enrichment argue against assigning a specific autonomic or circulatory pathway solely from this module.

**Cell composition.** The module is not predominantly composed of secreted or plasma proteins: HPA identifies only a small secreted subset, and most genes have low tissue specificity. It is also not strongly blood-cell specific at the bulk module level, because most genes have low immune-cell specificity and only a minority show immune or blood-cell-associated patterns. Nevertheless, HPA single-cell evidence repeatedly highlights neutrophils and platelets, while several genes are enhanced in esophageal apical cells and other specialized cell types. STOM, ILK, ITGB1, VCL, ENDOD1, and SLC6A6 provide examples of platelet, neutrophil, or vascular-associated signals, but the module also includes mitochondrial, nuclear, Golgi, and metabolic proteins. The shared signal could therefore partly reflect common cell-type composition or blood-related material in samples, rather than a tissue-specific autonomic–circulatory mechanism. HPA protein detection cannot resolve the two target tissue groups because no matching HPA tissue was available.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a compact, biologically interpretable adhesion and receptor-associated subnetwork: EGFR–ITGB1, ILK–ITGB1, ILK–VCL, and ITGB1–VCL are high-confidence relationships, and BCL2L1–EGFR is also supported. These links are consistent with known integrin, focal-adhesion, receptor-signaling, and cytoskeletal biology, but they do not establish that all module genes form one physical complex. The MTIF2–POLR3B relationship is a separate supported connection linking mitochondrial translation with a transcription-related protein. STRING reports no functional enrichment for the query, so the interaction evidence is more informative about selected subnetworks than about the module as a whole. hu.MAP contributes one complex with at least two module members: ATP6V1C1 and STOM occur together in complex (hu.MAP huMAP3_12042.1). Because only a small portion of that large complex is represented, (hu.MAP huMAP3_12042.1) supports possible convergence on vesicle or membrane-compartment biology, but does not define the entire module. The absence of additional hu.MAP assignments indicates limited direct complex evidence, not absence of biological relationships.

**STRING interactions (score >= 0.7)**: 6 of 903 gene pairs: BCL2L1–EGFR (0.847); EGFR–ITGB1 (0.966); ILK–ITGB1 (0.999); ILK–VCL (0.995); ITGB1–VCL (0.966); MTIF2–POLR3B (0.792)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12042.1 (ATP6V1C1, STOM; 2/56)

### Novelty

The module may be a new co-abundance observation, but it cannot be called a new molecular pathway or a newly discovered interaction network on the present evidence. Several of its central relationships are already known in STRING, especially the ILK–ITGB1–VCL adhesion structure and the EGFR–ITGB1 connection, and (hu.MAP huMAP3_12042.1) provides existing complex-level support for ATP6V1C1 with STOM. Conversely, most module-member pairings are not represented in the supplied STRING or hu.MAP results. That absence alone does not demonstrate novelty, because co-abundance can reflect indirect regulation, shared cell composition, or context-dependent biology. The appropriate novelty claim is therefore limited: the cross-tissue conservation of this particular mixed module, and its combination of adhesion, trafficking, mitochondrial, nuclear, and cell-type-associated genes, may be novel and merits replication. Independent cohorts, cell-composition adjustment, and validation at the protein or perturbation level would be needed before claiming a new mechanism.

**Hypothesis.** Mechanistic hypothesis: in both autonomic nervous system and circulatory system samples, a shared population or state of adherent vascular, smooth-muscle, platelet-related, or other interface cells may coordinate integrin-based adhesion with receptor trafficking, cytoskeletal remodeling, organelle quality control, and survival. In this model, ITGB1, ILK, and VCL form the mechanical adhesion core; EGFR and ARAP1 connect receptor trafficking and small-GTPase or membrane-remodeling processes; STOM and ATP6V1C1 contribute membrane or vesicular compartment functions; and OPA1, IMMT, DECR1, and related genes support mitochondrial structure and metabolism. The repeated HPA association with neutrophils and platelets raises an alternative explanation in which shared blood-cell or blood-derived composition drives part of the signal. This is a hypothesis, not an established causal pathway, and should be tested by cell-type deconvolution, spatial or single-cell data, and perturbation of the adhesion and trafficking components.

### Important genes

#### FAM241A

- **Related proteins** (co-abundance neighbors): ILK (0.98), STOM (0.95), KATNAL1 (0.94), ARAP1 (0.93), SNX6 (0.88), ITGB1 (0.87), HIBADH (0.87), LMNB2 (0.86), ATP6V1C1 (0.85), MSH6 (0.84), PHPT1 (0.84), RP2 (0.83), IMMT (0.83), DECR1 (0.82), FTH1 (0.82), VCL (0.82), CFAP20 (0.81), GOT2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: family with sequence similarity 241 member A. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: atrial fibrillation (0.414); pathological myopia (0.310); appendicitis (0.303); smoking cessation (0.292); placenta praevia (0.279)
- **Europe PMC papers**: 69
- **Why important**: FAM241A is the highest-connectivity hub in the supplied module and links many otherwise heterogeneous genes, including ILK, STOM, KATNAL1, ARAP1, SNX6, and ITGB1. HPA places it in the Golgi apparatus and shows enhanced signal in vascular endothelial cells among other cell types. It has no supplied STRING or hu.MAP relationship, so its hub status is driven by the co-abundance network rather than established physical interaction evidence. Its disease associations include atrial fibrillation and other conditions, while its literature volume is comparatively limited. This combination makes it important as a module-organizing marker and a candidate regulator, but not yet as an established mechanistic driver.
- **Conclusion**: Established evidence: FAM241A is the central co-abundance hub, has Golgi localization, and is associated with vascular endothelial cell expression in HPA. Hypothesis: FAM241A may coordinate Golgi or membrane trafficking with the adhesion-associated subnetwork and could help explain conservation across the two tissue groups. Its causal role remains unproven.

#### ITGB1

- **Related proteins** (co-abundance neighbors): FAM241A (0.87), TRMT11 (0.84), ARAP1 (0.81), EGFR (0.81); STRING partners: EGFR (0.966), ILK (0.999), VCL (0.966)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is a core adhesion receptor with direct high-confidence STRING relationships to EGFR, ILK, and VCL, and it is connected to the module hub FAM241A and to TRMT11 and ARAP1 in the co-abundance network. Its documented functions include cell adhesion, angiogenesis, phagocytosis, cellular defense, and hemostasis-related integrin biology. HPA places it at the plasma membrane and focal adhesion sites and highlights platelets. It has extensive literature and disease associations involving inflammatory and immune conditions, making it the strongest established mechanistic anchor for the adhesion interpretation.
- **Conclusion**: Established evidence: ITGB1 is a membrane adhesion receptor embedded in a STRING-supported ILK–VCL–EGFR interaction neighborhood and is relevant to platelet and vascular biology. Hypothesis: altered ITGB1-centered adhesion or mechanosignaling could be a shared driver of the module in autonomic and circulatory tissues, although the co-abundance data do not establish direction or causality.

#### ILK

- **Related proteins** (co-abundance neighbors): FAM241A (0.98), TRMT11 (0.82), STOM (0.82), SLC6A6 (0.80); STRING partners: ITGB1 (0.999), VCL (0.995)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin linked kinase. This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastas…
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); familial hypertrophic cardiomyopathy (0.194); Abnormality of the cardiovascular system (0.148); Prolonged QT interval (0.118); neoplasm (0.118)
- **Europe PMC papers**: 8401
- **Why important**: ILK connects the module hub FAM241A with STOM and SLC6A6 and has high-confidence STRING relationships with ITGB1 and VCL. Its documented role is association with the cytoplasmic domain of beta integrins and regulation of integrin-mediated signaling, cell-matrix adhesion, cell morphogenesis, and outflow tract morphogenesis. HPA places ILK at focal adhesion sites and identifies megakaryocytes, platelets, and smooth-muscle cells. Its cardiovascular and neurodegenerative disease associations and substantial literature support make it a biologically plausible bridge between tissue mechanics and cell state.
- **Conclusion**: Established evidence: ILK is a focal-adhesion and integrin-associated signaling protein supported by both annotation and STRING relationships. Hypothesis: ILK may couple extracellular or vascular mechanical cues to the broader trafficking and organelle-maintenance program represented by the module. This extension beyond the known adhesion subnetwork remains to be tested.

#### VCL

- **Related proteins** (co-abundance neighbors): SLC6A6 (0.82), FAM241A (0.82); STRING partners: ILK (0.995), ITGB1 (0.966)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vinculin. Vinculin is a cytoskeletal protein associated with cell-cell and cell-matrix junctions, where it is thought to function as one of several interacting proteins involved in anchoring F-actin to the membrane. Defects in VCL are the cause of cardiomyopathy dilated type 1W. Dilated cardiomyopathy is a disorder characterized by ventricular dilation and impaired systolic function, resulting in congestive…
- **Diseases (Open Targets)**: dilated cardiomyopathy 1W (0.692); hypertrophic cardiomyopathy 15 (0.660); hypertrophic cardiomyopathy (0.652); familial isolated dilated cardiomyopathy (0.642); cancer (0.605)
- **Europe PMC papers**: 10760
- **Why important**: VCL is part of the STRING-supported ILK–ITGB1–VCL adhesion cluster and is connected in the co-abundance network to FAM241A and SLC6A6. Its established function is anchoring F-actin to cell-cell and cell-matrix junctions. HPA identifies focal adhesion localization and platelet enrichment. VCL has extensive literature and strong disease relevance to dilated and hypertrophic cardiomyopathy, making it particularly relevant to a module shared with circulatory tissue.
- **Conclusion**: Established evidence: VCL is a cytoskeletal adhesion component with direct STRING support and established cardiomyopathy associations. Hypothesis: VCL may transmit or stabilize mechanical signals in the shared module and could connect platelet or vascular cell composition to tissue-level co-abundance. The data do not show whether VCL is causal or merely a marker of the relevant cell state.

#### SLC6A6

- **Related proteins** (co-abundance neighbors): NCSTN (0.96), ENDOD1 (0.92), KATNAL1 (0.91), HMGA1 (0.87), MTAP (0.84), GHDC (0.84), BCL2L1 (0.84), VCL (0.82), ILK (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cell Junctions, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 6 member 6. This gene encodes a multi-pass membrane protein that is a member of a family of sodium and chloride-ion dependent transporters. The encoded protein transports taurine and beta-alanine. There is a pseudogene for this gene on chromosome 21. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2013].
- **Diseases (Open Targets)**: hypotaurinemic retinal degeneration and cardiomyopathy (0.445); cardiomyopathy (0.420); retinal degeneration (0.340); inherited retinal dystrophy (0.340); revision of total joint arthroplasty (0.334)
- **Europe PMC papers**: 1500
- **Why important**: SLC6A6 is a relatively central module gene connected to NCSTN, ENDOD1, KATNAL1, HMGA1, MTAP, GHDC, BCL2L1, and VCL. It encodes a sodium- and chloride-dependent taurine and beta-alanine transporter, linking membrane transport to cellular osmotic, metabolic, and stress biology. HPA highlights neutrophils and places the protein at cell junctions and in the cytosol. Its disease associations include cardiomyopathy and retinal degeneration, and it has substantial literature. Unlike ITGB1, ILK, and VCL, it has no supplied STRING or hu.MAP relationship, so its connection to the adhesion core is currently co-abundance-based.
- **Conclusion**: Established evidence: SLC6A6 is a membrane amino-acid transporter with neutrophil-associated expression and disease links that include cardiomyopathy. Hypothesis: taurine transport may support stress resistance or membrane homeostasis in the cell population underlying the shared module and may functionally couple to adhesion and mitochondrial demands. This proposed coupling is not demonstrated by the supplied interaction data.

## Module 1

**Tissue pair**: autonomic_nervous_system and circulatory_system  
**Genes (33)**: NT5E, ACE, SERPINC1, APOA1, APOH, CCNY, CORO1C, CYFIP1, DHFR, F5, FBXO30, AHSG, FHL1, GGH, HSPB1, INF2, PRKAR2B, LGALS3BP, LIMS1, NAA20, NQO1, NUCB1, PEPD, PRDX4, CHML, RAB39A, RBM12, SLC39A14, AARS1, TMEM87B, TPM1, GC, VTN

### Function

The module is most consistent with a circulating extracellular-vesicle and blood-plasma protein program linked to lipid transport, coagulation control, extracellular adhesion, and vascular homeostasis. The strongest primary evidence is enrichment for blood microparticle (GO:CC blood microparticle; q_global = 0.00156) and for secretory, cytoplasmic-vesicle, vesicle, and extracellular-organelle lumens (GO:CC secretory granule lumen; q_global = 0.0117) (GO:CC cytoplasmic vesicle lumen; q_global = 0.0117) (GO:CC vesicle lumen; q_global = 0.0129) (GO:CC extracellular organelle; q_global = 0.0446) (GO:CC extracellular membrane-bounded organelle; q_global = 0.0446) (GO:CC extracellular vesicle; q_global = 0.0446). APOA1, APOH, AHSG, GC, SERPINC1, VTN, and F5 connect lipoprotein-associated biology with coagulation and extracellular matrix or adhesion biology. ACE adds a blood-pressure and vasoactive-peptide dimension, while TPM1 and related cytoskeletal genes are compatible with vascular or muscle structural context. The module therefore appears to represent coordinated abundance of circulating proteins and vesicle-associated vascular proteins more strongly than a narrowly defined intracellular pathway.

**Cell composition.** The module is strongly dominated by secreted or extracellular proteins rather than being a uniformly tissue-intrinsic autonomic or circulatory cellular program. HPA identifies secreted-to-blood proteins including APOA1, AHSG, APOH, ACE, F5, GC, SERPINC1, and VTN, and identifies a substantial secreted-gene component overall. Liver and hepatocytes are recurrent enriched sources, especially for APOA1, AHSG, APOH, GC, SERPINC1, and VTN. The HPA blood-cell evidence is mixed: several genes show immune-cell enhancement or myeloid, platelet, megakaryocyte, or plasmacytoid-dendritic-cell associations, but many major plasma proteins are not detected in immune cells. This pattern makes blood or plasma carryover, extracellular vesicles, and shared vascular or hepatic material plausible contributors to the apparent cross-tissue module. The HPA data do not support calling the whole module a blood-cell module, and they do not establish protein detection in the two queried tissue groups because matching HPA tissues were unavailable.

**GO/KEGG enrichment**: 7 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 0.00156 | AHSG, APOA1, GC, LGALS3BP, SERPINC1, VTN |
| GO:CC secretory granule lumen | 0.0117 | AHSG, APOA1, APOH, CYFIP1, F5, GGH, LGALS3BP, PRDX4 |
| GO:CC cytoplasmic vesicle lumen | 0.0117 | AHSG, APOA1, APOH, CYFIP1, F5, GGH, LGALS3BP, PRDX4 |
| GO:CC vesicle lumen | 0.0129 | AHSG, APOA1, APOH, CYFIP1, F5, GGH, LGALS3BP, PRDX4 |
| GO:CC extracellular organelle | 0.0446 | AARS1, ACE, AHSG, APOA1, APOH, CYFIP1, F5, GC, GGH, HSPB1, LGALS3BP, NT5E, NUCB1, PEPD, PRDX4, PRKAR2B, SERPINC1, VTN |
| GO:CC extracellular membrane-bounded organelle | 0.0446 | AARS1, ACE, AHSG, APOA1, APOH, CYFIP1, F5, GC, GGH, HSPB1, LGALS3BP, NT5E, NUCB1, PEPD, PRDX4, PRKAR2B, SERPINC1, VTN |
| GO:CC extracellular vesicle | 0.0446 | AARS1, ACE, AHSG, APOA1, APOH, CYFIP1, F5, GC, GGH, HSPB1, LGALS3BP, NT5E, NUCB1, PEPD, PRDX4, PRKAR2B, SERPINC1, VTN |

### STRING and hu.MAP

STRING provides a coherent, already known interaction backbone among AHSG, APOA1, APOH, GC, SERPINC1, and VTN, with additional links involving F5. These relationships support a genuine plasma-protein and coagulation-associated cluster rather than an arbitrary co-abundance grouping. STRING also connects DHFR with GGH, while the remaining module edges are sparse or absent in the high-confidence interaction set. Its supplementary keywords independently emphasize signal peptides, secretion, glycoproteins, extracellular space, vesicles, blood microparticles, and blood or vascular proteomic studies (STRING Keyword Signal; within-query FDR = 2.25e-07) through (STRING TISSUES Skeletal system; within-query FDR = 0.0039). These are supportive annotations, not globally corrected GO evidence. hu.MAP shows the same plasma-protein core in complexes containing SERPINC1, APOA1, APOH, AHSG, and GC (hu.MAP huMAP3_15040.1), and repeatedly places APOA1, AHSG, and GC in larger plasma-protein assemblies (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1) through (hu.MAP huMAP3_10101.1). hu.MAP also supports an AARS1-RBM12 pairing (hu.MAP huMAP3_10302.1) (hu.MAP huMAP3_10115.1). Because most hu.MAP complexes contain many members outside this module, they support shared complex or plasma milieu membership but do not prove that the entire module is one physical complex.

**STRING interactions (score >= 0.7)**: 16 of 528 gene pairs: AHSG–APOA1 (0.944); AHSG–APOH (0.957); AHSG–F5 (0.701); AHSG–GC (0.959); AHSG–SERPINC1 (0.838); AHSG–VTN (0.782); APOA1–APOH (0.985); APOA1–SERPINC1 (0.708); APOA1–VTN (0.755); APOH–GC (0.766); APOH–SERPINC1 (0.944); APOH–VTN (0.787); DHFR–GGH (0.966); F5–SERPINC1 (0.817); GC–SERPINC1 (0.84); SERPINC1–VTN (0.949)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Signal (FDR = 2.25e-07, 15 genes); Keyword Secreted (FDR = 3.64e-06, 11 genes); Keyword Glycoprotein (FDR = 3.65e-05, 14 genes); TISSUES Bone marrow cell (FDR = 0.00012, 7 genes); TISSUES Plasma cell (FDR = 0.00083, 6 genes); PMID (2021) Proteomic Studies of Blood and Vascular Wall in Atherosclerosis. (FDR = 0.0017, 8 genes); Component Blood microparticle (FDR = 0.0021, 6 genes); COMPARTMENTS Extracellular region (FDR = 0.0022, 14 genes); COMPARTMENTS Vesicle (FDR = 0.0022, 17 genes); COMPARTMENTS Blood microparticle (FDR = 0.0022, 6 genes); COMPARTMENTS Extracellular space (FDR = 0.0025, 11 genes); COMPARTMENTS Secretory granule lumen (FDR = 0.0025, 7 genes); COMPARTMENTS Extracellular membrane-bounded organelle (FDR = 0.0025, 10 genes); COMPARTMENTS Extracellular vesicle (FDR = 0.0027, 10 genes); TISSUES Skeletal system (FDR = 0.0039, 13 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINC1, APOA1, APOH, AHSG, GC; 5/64); huMAP3_09434.1 (APOA1, AHSG, GC; 3/33); huMAP3_10678.1 (APOA1, AHSG, GC; 3/71); huMAP3_10302.1 (AARS1, RBM12; 2/9); huMAP3_10115.1 (AARS1, RBM12; 2/14); huMAP3_07432.1 (APOA1, AHSG; 2/18); huMAP3_07265.1 (APOA1, AHSG; 2/20); huMAP3_08224.1 (APOA1, GC; 2/21); huMAP3_08395.1 (APOA1, AHSG; 2/43); huMAP3_09531.1 (APOA1, AHSG; 2/47); huMAP3_10101.1 (APOA1, AHSG; 2/49)

### Novelty

The module should not be presented as a newly discovered molecular complex. Its central plasma-protein relationships are already represented in STRING and hu.MAP, and the major genes have extensive functional and disease literature. What may be new is the observation that this particular co-abundance pattern is conserved across the autonomic nervous system and circulatory system, especially the combination of a plasma-protein core with smaller cytoskeletal, vesicle-trafficking, signaling, and metabolic branches. However, co-abundance conservation alone does not establish a new mechanism, and the strong liver, plasma, and extracellular-vesicle signature means that shared sample composition could explain part of the finding. Demonstrating novelty would require independent tissue-resolved replication, control for blood contamination and cell composition, and testing whether the non-plasma branch remains coordinated after those adjustments.

**Hypothesis.** Hypothesis: the conserved module reflects a blood-borne vascular homeostasis program in which liver-derived plasma proteins and extracellular vesicles coordinate lipid handling, coagulation restraint, endothelial or extracellular-matrix interactions, and vascular signaling across both tissue groups. APOA1, APOH, AHSG, GC, SERPINC1, VTN, and F5 could form the circulating protein context; ACE could connect that context to vasoactive and blood-pressure regulation; and TPM1, PRKAR2B, FHL1, LIMS1, and vesicle-trafficking genes could represent tissue or cell-state responses in vascular, muscle, platelet, or related cells. This is a mechanistic proposal rather than a demonstrated pathway, because the co-abundance data and annotations do not establish directionality, physical interaction for every edge, or tissue-of-origin.

### Important genes

#### APOA1

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.91), VTN (0.84), GC (0.81); STRING partners: AHSG (0.944), APOH (0.985), SERPINC1 (0.708), VTN (0.755)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_09434.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_08224.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is a central member of the plasma-protein core, connects directly to AHSG, APOH, SERPINC1, and VTN in STRING, appears in every primary vesicle-related enrichment term (GO:CC blood microparticle; q_global = 0.00156) through (GO:CC extracellular vesicle; q_global = 0.0446), and is represented across many hu.MAP plasma-protein complexes (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_10678.1) and (hu.MAP huMAP3_07432.1) through (hu.MAP huMAP3_10101.1). HPA places it in liver and hepatocytes or enterocytes and identifies secretion to blood. Its established function in HDL structure, lipid transport, cholesterol efflux, and immune-related signaling gives the module a strong circulating lipid-transport anchor. It also has exceptionally extensive literature and disease evidence.
- **Conclusion**: Established evidence supports APOA1 as a biologically meaningful plasma and lipoprotein component of the module. It is a plausible marker of shared blood or extracellular material, but the data do not show that APOA1 drives the conserved tissue program.

#### SERPINC1

- **Related proteins** (co-abundance neighbors): VTN (0.92), APOA1 (0.91), AARS1 (0.81); STRING partners: AHSG (0.838), APOA1 (0.708), APOH (0.944), F5 (0.817), GC (0.84), VTN (0.949)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 is a highly connected coagulation-related node linked in STRING to VTN, APOH, F5, GC, AHSG, and APOA1, and it participates in the primary blood-microparticle and extracellular-organelle enrichments (GO:CC blood microparticle; q_global = 0.00156) (GO:CC extracellular organelle; q_global = 0.0446) (GO:CC extracellular membrane-bounded organelle; q_global = 0.0446) (GO:CC extracellular vesicle; q_global = 0.0446). HPA identifies liver and hepatocytes and secretion to blood. Its established antithrombin function directly connects the module to regulation of thrombin and the coagulation cascade, with strong associations to antithrombin deficiency and venous thromboembolic disease. It is also part of the major hu.MAP plasma-protein complex (hu.MAP huMAP3_15040.1).
- **Conclusion**: Established evidence supports SERPINC1 as a functional coagulation anchor and as part of a known circulating protein network. Its module membership is more readily explained by plasma and vascular biology than by autonomic-neuron-specific biology.

#### VTN

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.92), F5 (0.85), ACE (0.85), PEPD (0.85), APOA1 (0.84), TMEM87B (0.83), NQO1 (0.81); STRING partners: AHSG (0.782), APOA1 (0.755), APOH (0.787), SERPINC1 (0.949)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vitronectin. The protein encoded by this gene functions in part as an adhesive glycoprotein. Differential expression of this protein can promote either cell adhesion or migration as it links cells to the extracellular matrix through a variety of ligands. These ligands include integrins, plasminogen activator inhibitor-1, and urokinase plasminogen activator receptor. This secreted protein can be present in the …
- **Diseases (Open Targets)**: hypertensive disorder (0.421); dengue disease (0.376); neurodegenerative disease (0.343); temporal arteritis (0.338); age-related macular degeneration (0.313)
- **Europe PMC papers**: 3940
- **Why important**: VTN has the strongest network position in the supplied module and connects to SERPINC1, F5, ACE, PEPD, APOA1, TMEM87B, and NQO1. It appears in the blood microparticle and extracellular-organelle terms (GO:CC blood microparticle; q_global = 0.00156) (GO:CC extracellular organelle; q_global = 0.0446) (GO:CC extracellular membrane-bounded organelle; q_global = 0.0446) (GO:CC extracellular vesicle; q_global = 0.0446) and in many supplementary secretion, vesicle, and vascular annotations (STRING Keyword Signal; within-query FDR = 2.25e-07) through (STRING TISSUES Skeletal system; within-query FDR = 0.0039). HPA identifies liver and hepatocytes or cholangiocytes and secretion to blood. Its established adhesive glycoprotein function links integrins, extracellular matrix, plasminogen-activator-related biology, cell adhesion, and smooth-muscle migration. It has substantial literature and disease associations including hypertensive disorder.
- **Conclusion**: Established evidence supports VTN as a network-level bridge between the plasma protein core and vascular extracellular-matrix biology. Its central position makes it a strong candidate marker of the module, while any causal role in conservation across the two tissue groups remains hypothetical.

#### ACE

- **Related proteins** (co-abundance neighbors): PEPD (0.86), VTN (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: angiotensin I converting enzyme. This gene encodes an enzyme involved in blood pressure regulation and electrolyte balance. It catalyzes the conversion of angiotensin I into a physiologically active peptide angiotensin II. Angiotensin II is a potent vasopressor and aldosterone-stimulating peptide that controls blood pressure and fluid-electrolyte balance. This angiotensin converting enzyme (ACE) also inactivates the vasodilator p…
- **Diseases (Open Targets)**: hypertensive disorder (0.750); renal tubular dysgenesis of genetic origin (0.729); renal tubular dysgenesis (0.724); cardiovascular disorder (0.704); diabetic kidney disease (0.689)
- **Europe PMC papers**: 95248
- **Why important**: ACE links the high-connectivity extracellular branch through VTN and PEPD and is included in the globally significant extracellular-organelle terms (GO:CC extracellular organelle; q_global = 0.0446) (GO:CC extracellular membrane-bounded organelle; q_global = 0.0446) (GO:CC extracellular vesicle; q_global = 0.0446). STRING supplementary evidence places it among secreted, glycoprotein, extracellular, vesicle, and vascular-associated genes (STRING Keyword Signal; within-query FDR = 2.25e-07) through (STRING TISSUES Bone marrow cell; within-query FDR = 0.00012) and (STRING COMPARTMENTS Extracellular region; within-query FDR = 0.0022) through (STRING TISSUES Skeletal system; within-query FDR = 0.0039). HPA identifies tissue enhancement in intestine and testis, enterocyte and late spermatid associations, immune-cell enhancement in memory B cells, and secretion to blood. Its established enzymatic role in angiotensin maturation, bradykinin inactivation, blood-pressure regulation, and vessel remodeling gives the module a direct cardiovascular and vascular-signaling connection. ACE also has extensive literature and strong disease relevance.
- **Conclusion**: Established evidence supports ACE as a biologically important vascular-signaling component embedded in a broader circulating extracellular program. It provides a plausible bridge to circulatory physiology, but the co-abundance pattern does not demonstrate altered renin-angiotensin activity.

#### TPM1

- **Related proteins** (co-abundance neighbors): PRKAR2B (0.86), FBXO30 (0.84), TMEM87B (0.81), INF2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tropomyosin 1. This gene is a member of the tropomyosin family of highly conserved, widely distributed actin-binding proteins involved in the contractile system of striated and smooth muscles and the cytoskeleton of non-muscle cells. Tropomyosin is composed of two alpha-helical chains arranged as a coiled-coil. It is polymerized end to end along the two grooves of actin filaments and provides stability to the fi…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy (0.798); left ventricular noncompaction (0.760); left ventricular noncompaction 9 (0.664); familial isolated dilated cardiomyopathy (0.639); hypertrophic cardiomyopathy 3 (0.596)
- **Europe PMC papers**: 6278
- **Why important**: TPM1 occupies a branch connected to PRKAR2B, FBXO30, TMEM87B, and INF2, linking the plasma-dominated module to actin and contractile-cell biology. HPA identifies enhancement in heart and skeletal muscle and cell-type associations including hepatic stellate cells and megakaryocytes. Its established function is stabilization and regulation of actin filaments, with roles in muscle contraction, heart contraction, and cell shape. It has substantial literature and strong disease associations with cardiomyopathies. It is not part of the primary GO enrichment terms, and its STRING support is limited to the supplementary blood and vascular proteomic annotation (STRING PMID (2021) Proteomic Studies of Blood and Vascular Wall in Atherosclerosis.; within-query FDR = 0.0017).
- **Conclusion**: Established evidence supports TPM1 as a structural or contractile-context marker that may connect the circulating protein signal to cardiac, vascular, platelet, or muscle-related cells. Its inclusion supports a possible tissue-response branch, but it could also reflect cellular composition rather than a shared molecular mechanism.

## Module 2

**Tissue pair**: autonomic_nervous_system and circulatory_system  
**Genes (36)**: PRKAG1, PAM, ANXA5, ASPH, B2M, BAIAP2, BCS1L, COX20, CPNE2, DAGLB, ERG28, SHMT1, GNAO1, ME1, MELK, MSH3, NDUFS4, NEMP1, NUP37, OXA1L, PAGR1, LPCAT1, PCYOX1L, PON2, PUS7, STX18, SUGP2, TBC1D24, TCOF1, GTF3C4, F2, THYN1, LTF, USP16, UXT, VPS33A

### Function

The strongest function-level signal is host defense and cell killing. The globally corrected terms (GO:BP killing of cells of another organism; q_global = 0.0362) and (GO:BP disruption of cell in another organism; q_global = 0.0362) identify killing or disruption of cells in another organism through F2, LTF, and PCYOX1L, while (GO:BP cell killing; q_global = 0.0431) broadens this signal to cell killing and adds B2M. LTF is an established antimicrobial and iron-binding protein associated with neutrophil granules and mucosal defense; F2 is the coagulation protease precursor whose activated product participates in hemostasis, platelet activation, wound responses, and signaling; PCYOX1L is annotated for prenylated-protein catabolism and neutrophil-mediated bacterial killing; and B2M participates in antigen presentation and natural-killer and T-cell regulation. The module also contains secondary, non-global signals related to calcium biology (STRING Keyword Calcium; within-query FDR = 0.0278), including calcium-associated proteins and lipid or membrane regulators. Its remaining genes indicate several additional programs, including mitochondrial respiration, phospholipid metabolism, vesicle trafficking, nuclear transport, RNA processing, DNA repair, and neuroendocrine signaling. Because these programs are distributed across weakly connected branches rather than supported by globally corrected enrichment, the most defensible interpretation is a host-defense and vascular-interface module with accompanying cellular stress, membrane, and housekeeping components. No GO or KEGG term passed within-module correction, but globally corrected evidence is present in (GO:BP killing of cells of another organism; q_global = 0.0362) through (GO:BP cell killing; q_global = 0.0431).

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the fact sheet identifies six secreted genes, including F2, LTF, PCYOX1L, B2M, and PON2, with PAM secreted in other tissues. Nevertheless, the secreted members are biologically conspicuous and could contribute to a circulating-protein signal. HPA indicates broadly distributed expression for most genes, with low tissue specificity in twenty-four genes, while a substantial subset is cell-type enhanced. The most recurrent cell-type associations include glial populations and neutrophil progenitors, and the module includes tissue-enhanced genes in brain, liver, bone marrow, lymphoid tissue, heart muscle, lung, and adipose tissue. Blood-cell specificity is generally low, but selected genes are enriched or enhanced in neutrophils, monocytes, dendritic cells, T-regulatory cells, MAIT cells, and progenitors. Thus, the shared signal should not automatically be interpreted as a specialized autonomic–circulatory program. It may partly reflect blood exposure, immune or progenitor-cell admixture, and broadly expressed cellular machinery. The HPA protein-detection fields provide no tissue-matched protein measurements for either named tissue group, so they cannot independently validate tissue-specific protein abundance.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP killing of cells of another organism | 0.0362 | F2, LTF, PCYOX1L |
| GO:BP disruption of cell in another organism | 0.0362 | F2, LTF, PCYOX1L |
| GO:BP cell killing | 0.0431 | B2M, F2, LTF, PCYOX1L |

### STRING and hu.MAP

STRING provides very limited direct support for a unified physical interaction network. The only high-confidence STRING relationship is BCS1L with NDUFS4, linking mitochondrial respiratory-chain biology. The calcium keyword result (STRING Keyword Calcium; within-query FDR = 0.0278) is supplementary and should not be treated as globally corrected enrichment. hu.MAP provides recurring complex-level support for NEMP1, B2M, and NUP37 together across (hu.MAP huMAP3_09825.1) and (hu.MAP huMAP3_12581.1), with NEMP1 and B2M recurring in additional nuclear-transport complexes (hu.MAP huMAP3_07331.1), (hu.MAP huMAP3_08641.1), and (hu.MAP huMAP3_10000.1). This supports an association with nuclear-pore, nucleocytoplasmic-transport, and cell-cycle-related complex neighborhoods, but the module contains only a minority of members from each complex, so it does not establish that the entire module is one physical complex. The OXA1L–LPCAT1 membership in (hu.MAP huMAP3_06247.1) supports a separate mitochondrial and membrane-lipid branch. Overall, STRING and hu.MAP support isolated relationships and several functional neighborhoods rather than a single experimentally established multiprotein assembly.

**STRING interactions (score >= 0.7)**: 1 of 630 gene pairs: BCS1L–NDUFS4 (0.742)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Calcium (FDR = 0.0278, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09825.1 (NEMP1, B2M, NUP37; 3/27); huMAP3_12581.1 (NEMP1, B2M, NUP37; 3/58); huMAP3_07331.1 (NEMP1, B2M; 2/15); huMAP3_08641.1 (NEMP1, B2M; 2/19); huMAP3_10000.1 (NEMP1, B2M; 2/44); huMAP3_06247.1 (OXA1L, LPCAT1; 2/65)

### Novelty

The module may be a new co-abundance observation, but it should not be called a newly discovered biological pathway. Its novelty lies primarily in the cross-tissue co-abundance combination and the specific network organization. The globally corrected host-defense signal is biologically interpretable, yet the module also combines coagulation, antimicrobial defense, calcium and membrane biology, mitochondrial function, nuclear transport, RNA or DNA maintenance, and neural or neuroendocrine annotations. The sparse STRING network and partial hu.MAP overlaps argue against a previously recognized unified complex. However, absence from STRING or hu.MAP does not prove novelty, because co-abundance relationships can reflect shared regulation, cell composition, secretion, or tissue sampling rather than direct binding. A defensible conclusion is that this is a potentially novel cross-tissue co-abundance module whose mechanistic unity remains unestablished and requires replication, cell-composition adjustment, and independent validation.

**Hypothesis.** Hypothesis: the module reflects a blood-facing tissue state in which coagulation and antimicrobial defense are co-regulated with membrane remodeling, calcium-responsive signaling, and cellular stress adaptation. In this model, F2 and LTF represent circulating or secretory host-defense and hemostatic components, while B2M and PCYOX1L mark immune surveillance or antimicrobial activity. PAM, ASPH, ANXA5, CPNE2, LPCAT1, and DAGLB could connect secretory, calcium-dependent, and phospholipid processes, whereas mitochondrial and nuclear-maintenance genes may reflect the energetic and biosynthetic demands of the contributing cells. The shared autonomic–circulatory signal could therefore arise from common vascular or blood-associated cellular mixtures rather than direct regulation among all module genes. This hypothesis predicts that the module will weaken after correction for plasma proteins and immune or progenitor-cell abundance, while the core host-defense signal may persist in relevant vascular or immune compartments.

### Important genes

#### F2

- **Related proteins** (co-abundance neighbors): PAM (0.94), NEMP1 (0.86), GNAO1 (0.84), ASPH (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coagulation factor II, thrombin. This gene encodes the prothrombin protein (also known as coagulation factor II). This protein is proteolytically cleaved in multiple steps to form the activated serine protease thrombin. The activated thrombin enzyme plays an important role in thrombosis and hemostasis by converting fibrinogen to fibrin during blood clot formation, by stimulating platelet aggregation, and by activating additional …
- **Diseases (Open Targets)**: congenital prothrombin deficiency (0.827); thrombophilia due to thrombin defect (0.738); venous thromboembolism (0.727); deep vein thrombosis (0.690); blood coagulation disease (0.670)
- **Europe PMC papers**: 109299
- **Why important**: F2 is a central, relatively highly connected node in the module and is directly present in all globally corrected terms (GO:BP killing of cells of another organism; q_global = 0.0362), (GO:BP disruption of cell in another organism; q_global = 0.0362), and (GO:BP cell killing; q_global = 0.0431). Its established function as the precursor of thrombin links coagulation, platelet activation, wound response, and vascular signaling. HPA identifies it as liver-enriched, hepatocyte-enriched, and secreted to blood, making it particularly important for assessing whether the module reflects circulating protein contribution. It also has extensive disease and literature support, including thrombotic and prothrombin-deficiency associations.
- **Conclusion**: Established evidence supports F2 as the strongest vascular and coagulation anchor of the module and as a plausible contributor to a blood-derived co-abundance signal. It is not established that F2 physically regulates the other module genes. Its module membership may reflect shared abundance, secretion, or blood contamination rather than a direct intracellular mechanism.

#### LTF

- **Related proteins** (co-abundance neighbors): PAM (0.94), NEMP1 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lactotransferrin. This gene is a member of the transferrin family of genes and its protein product is found in the secondary granules of neutrophils. The protein is a major iron-binding protein in milk and body secretions with an antimicrobial activity, making it an important component of the non-specific immune system. The protein demonstrates a broad spectrum of properties, including regulation of iron homeostasi…
- **Diseases (Open Targets)**: tuberculosis (0.517); AL amyloidosis (0.467); Abnormality of the skeletal system (0.435); schizophrenia (0.235); inflammatory bowel disease (0.218)
- **Europe PMC papers**: 7000
- **Why important**: LTF is directly represented in (GO:BP killing of cells of another organism; q_global = 0.0362), (GO:BP disruption of cell in another organism; q_global = 0.0362), and (GO:BP cell killing; q_global = 0.0431), has an antimicrobial role, and is a secreted blood protein. HPA associates it with bone marrow and salivary gland, neutrophil progenitors, neutrophils, and non-classical monocytes. Its network links it to PAM, providing a small secretory branch, and its established host-defense function is more specific than the broad housekeeping annotations of many other module members. It also has substantial literature and disease-association support.
- **Conclusion**: Established evidence supports LTF as a host-defense and neutrophil-associated component that helps explain the globally corrected cell-killing signal. The data do not establish that LTF is a regulatory hub or that its co-abundance with autonomic genes reflects local antimicrobial activity in those tissues.

#### NEMP1

- **Related proteins** (co-abundance neighbors): OXA1L (0.88), ASPH (0.87), F2 (0.86), THYN1 (0.84), NDUFS4 (0.84), LPCAT1 (0.84), TBC1D24 (0.82), PRKAG1 (0.82), CPNE2 (0.81), TCOF1 (0.81), LTF (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09825.1, huMAP3_12581.1, huMAP3_07331.1, huMAP3_08641.1, huMAP3_10000.1
- **Function (MyGene.info)**: nuclear envelope integral membrane protein 1. Involved in nuclear membrane organization. Predicted to be located in nuclear inner membrane. Predicted to be integral component of membrane. Predicted to be active in nuclear envelope. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: allergic rhinitis (0.060); Female infertility due to fertilization defect (0.059); oocyte/zygote/embryo maturation arrest 22 (0.051); female infertility due to oocyte meiotic arrest (0.049); oocyte maturation defect 9 (0.049)
- **Europe PMC papers**: 85
- **Why important**: NEMP1 is the most highly connected module node by the supplied network ranking and connects several otherwise disparate branches, including F2, ASPH, mitochondrial genes, LPCAT1, and nuclear or membrane-associated genes. It recurs in the hu.MAP nuclear-transport complexes (hu.MAP huMAP3_09825.1) through (hu.MAP huMAP3_10000.1), together with B2M and, in some complexes, NUP37. HPA describes a nuclear-envelope location and erythrocyte-progenitor enhancement. Its established annotation concerns nuclear-membrane organization and erythrocyte maturation, while its disease and literature support are more limited than those of F2 or B2M.
- **Conclusion**: Established evidence supports NEMP1 as a network connector associated with nuclear-envelope organization and erythrocyte-related biology, and hu.MAP supports its placement in nuclear-transport neighborhoods. It is a promising structural or integrative marker, but a causal role linking host defense, coagulation, and neural or circulatory biology remains hypothetical.

#### PAM

- **Related proteins** (co-abundance neighbors): LTF (0.94), F2 (0.94), B2M (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peptidylglycine alpha-amidating monooxygenase. This gene encodes a multifunctional protein. The encoded preproprotein is proteolytically processed to generate the mature enzyme. This enzyme includes two domains with distinct catalytic activities, a peptidylglycine alpha-hydroxylating monooxygenase (PHM) domain and a peptidyl-alpha-hydroxyglycine alpha-amidating lyase (PAL) domain. These catalytic domains work sequentially to catalyze the conve…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.593); diabetes mellitus (0.538); Abnormality of the skeletal system (0.517); intelligence (0.492); diabetic eye disease (0.451)
- **Europe PMC papers**: 50367
- **Why important**: PAM connects F2, LTF, and B2M in the module and is included in the supplementary calcium keyword signal (STRING Keyword Calcium; within-query FDR = 0.0278). Its established enzymatic role in peptide amidation is relevant to neuroendocrine peptide maturation, and HPA reports enhancement in heart muscle and cardiomyocytes as well as secretion in other tissues. Its large literature base and disease associations make it an informative bridge between secretory biology and the autonomic–circulatory context.
- **Conclusion**: Established evidence supports PAM as a secretory-processing enzyme that could be relevant to neuroendocrine and cardiac-cell biology. The network supports association with the module's secreted host-defense branch, but does not show that PAM enzymatically processes F2, LTF, or B2M in this module.

#### B2M

- **Related proteins** (co-abundance neighbors): PAM (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09825.1, huMAP3_12581.1, huMAP3_07331.1, huMAP3_08641.1, huMAP3_10000.1
- **Function (MyGene.info)**: beta-2-microglobulin. This gene encodes a serum protein found in association with the major histocompatibility complex (MHC) class I heavy chain on the surface of nearly all nucleated cells. The protein has a predominantly beta-pleated sheet structure that can form amyloid fibrils in some pathological conditions. The encoded antimicrobial protein displays antibacterial activity in amniotic fluid. A mutation in this gen…
- **Diseases (Open Targets)**: MHC class I deficiency (0.656); diffuse large B-cell lymphoma (0.595); HIV infectious disease (0.532); amyloidosis, hereditary systemic 6 (0.528); AL amyloidosis (0.468)
- **Europe PMC papers**: 25100
- **Why important**: B2M is included in the globally corrected cell-killing term (GO:BP cell killing; q_global = 0.0431) and repeatedly appears with NEMP1 in the hu.MAP complexes (hu.MAP huMAP3_09825.1) through (hu.MAP huMAP3_10000.1). It is a broadly expressed MHC class I-associated serum protein with established roles in antigen presentation and regulation of natural-killer and T-cell responses. HPA indicates secretion to blood and enhancement in several immune-related cell types, including plasma cells and dendritic-cell populations. Its substantial literature and disease-association record make it a strong indicator of immune or blood-associated composition.
- **Conclusion**: Established evidence supports B2M as an immune-surveillance and circulating-protein component, and its repeated hu.MAP co-membership supports a nuclear-transport-associated complex neighborhood rather than a complete module-wide complex. Its presence strengthens the interpretation that part of the module may reflect immune or blood-cell composition. A direct role for B2M in the full co-abundance mechanism is not established.

## Module 3

**Tissue pair**: autonomic_nervous_system and circulatory_system  
**Genes (17)**: ABCD3, NCAPG, EXOSC9, GSTCD, LTN1, LUC7L, MAP4K4, MMS19, NCOR2, NOC3L, CAD, RBM26, SENP3, POMK, SNX4, TPD52, ZNF451

### Function

No GO or KEGG term passed global correction, and STRING provided no supplementary enrichment. The module therefore does not support a single statistically established biological pathway. Its genes nevertheless span several established processes: protein O-linked glycosylation and developmental biology through POMK, MAPK and cell-matrix signaling through MAP4K4, pyrimidine biosynthesis through CAD, iron-sulfur cluster assembly through MMS19, SUMO regulation and transcriptional repression through ZNF451, and RNA processing through EXOSC9 and related RNA-associated genes. Taken together, the most cautious interpretation is a broad intracellular maintenance and regulatory program rather than a tissue-specific autonomic or circulatory pathway. The sparse co-abundance network may reflect coordinated cell-state, growth, biosynthetic, or RNA and protein quality-control variation, but this remains inferential.

**Cell composition.** The module is not dominated by secreted or plasma proteins: HPA classifies none of the genes as secreted. Most genes have low tissue specificity, and most also have low immune-cell specificity, arguing against a clean blood-cell signature. Several genes do show tissue or cell-type enhancement, including bone marrow, liver, lymphoid tissue, brain, retina, epicardial cells, microglia, and reproductive cell types. A smaller subset is enhanced in neutrophils, basophils, or memory B cells, so shared immune or hematopoietic cell content could contribute in some samples, but the HPA pattern does not support a purely blood-derived module. HPA protein detection cannot resolve the two target tissue groups because no matching HPA tissue was available.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module gene pair met the supplied high-confidence STRING interaction threshold, and STRING reported no functional enrichment. No hu.MAP complex contained multiple module members. The co-abundance edges are therefore not corroborated by the supplied physical-interaction or complex resources. This suggests that the module is more likely to represent coordinated expression or shared cellular context than a known stable protein complex. The absence of STRING or hu.MAP support does not exclude transient, indirect, context-dependent, or poorly characterized relationships.

**STRING interactions (score >= 0.7)**: 0 of 136 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The co-abundance configuration may be a novel observation because it links genes from glycosylation, signaling, nucleotide metabolism, RNA processing, chromatin regulation, and protein quality control without support from the supplied interaction or complex databases. However, it cannot be called a new biological mechanism on this evidence alone. The lack of STRING and hu.MAP representation is not proof of novelty, especially because the module has no globally significant enrichment and contains broadly expressed genes. A stronger novelty claim would require replication in independent tissue cohorts, preservation of the same gene relationships, and experimental or perturbational validation.

**Hypothesis.** Hypothesis: variation in a broadly expressed intracellular maintenance state, involving RNA handling, proteostasis, nucleotide supply, post-translational regulation, and stress-responsive signaling, produces the shared co-abundance pattern in autonomic nervous system and circulatory system samples. POMK may mark the central expression axis of this state, while MAP4K4, ZNF451, MMS19, CAD, and RNA-processing genes could reflect linked signaling, transcriptional, metabolic, and biosynthetic demands. This is a hypothesis about coordinated cellular state, not an established pathway or physical complex.

### Important genes

#### POMK

- **Related proteins** (co-abundance neighbors): MMS19 (0.87), SNX4 (0.86), CAD (0.85), NOC3L (0.84), LUC7L (0.84), SENP3 (0.83), LTN1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein O-mannose kinase. This gene encodes a protein that may be involved in the presentation of the laminin-binding O-linked carbohydrate chain of alpha-dystroglycan (a-DG), which forms transmembrane linkages between the extracellular matrix and the exoskeleton. Some pathogens use this O-linked carbohydrate unit for host entry. Loss of function compound heterozygous mutations in this gene were found in a human patient af…
- **Diseases (Open Targets)**: muscular dystrophy-dystroglycanopathy (congenital with brain and eye anomalies), type a, 12 (0.806); limb-girdle muscular dystrophy due to POMK deficiency (0.694); muscular dystrophy-dystroglycanopathy, type A (0.669); muscular dystrophy-dystroglycanopathy (limb-girdle), type c, 12 (0.653); congenital muscular dystrophy with cerebellar involvement (0.381)
- **Europe PMC papers**: 262
- **Why important**: POMK is the strongest network hub in the module and connects to genes involved in trafficking, nucleotide metabolism, nucleolar regulation, RNA-associated functions, SUMO regulation, and protein quality control. Its established role in protein O-mannose kinase activity, alpha-dystroglycan glycosylation, and brain and muscle developmental disease makes it biologically relevant to a module shared by neural and circulatory tissues. Its literature coverage is substantial.
- **Conclusion**: Established evidence supports POMK as the central co-abundance hub and as a regulator of protein O-linked glycosylation with important neuromuscular and developmental disease associations. The hypothesis that it organizes the broader module or explains its cross-tissue behavior is not established.

#### MAP4K4

- **Related proteins** (co-abundance neighbors): NCOR2 (0.86), GSTCD (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitogen-activated protein kinase kinase kinase kinase 4. The protein encoded by this gene is a member of the serine/threonine protein kinase family. This kinase has been shown to specifically activate MAPK8/JNK. The activation of MAPK8 by this kinase is found to be inhibited by the dominant-negative mutants of MAP3K7/TAK1, MAP2K4/MKK4, and MAP2K7/MKK7, which suggests that this kinase may function through the MAP3K7-MAP2K4-MAP2K7 kinase cascade, and medi…
- **Diseases (Open Targets)**: neurodegenerative disease (0.572); hereditary disease (0.527); multiple congenital anomalies/dysmorphic syndrome-intellectual disability (0.503); RASopathy (0.400); asthma (0.372)
- **Europe PMC papers**: 2843
- **Why important**: MAP4K4 links the module to a signaling branch involving MAPK and JNK activation, TNF-related signaling, cell-matrix adhesion, migration, and Hippo regulation. It connects GSTCD and NCOR2 in the module and is tissue enhanced in brain, with cell-type enhancement across microglia, monocytes, neutrophils, oligodendrocytes, and retinal ganglion cells. It also has extensive disease and mechanistic literature.
- **Conclusion**: Established evidence supports MAP4K4 as a signaling kinase with roles in MAPK-related signaling, inflammatory signaling, adhesion, and migration. Its position in this module supports a possible regulatory connection, but does not prove that MAP4K4 drives the shared tissue module.

#### CAD

- **Related proteins** (co-abundance neighbors): POMK (0.85), NCAPG (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carbamoyl-phosphate synthetase 2, aspartate transcarbamylase, and dihydroorotase. The de novo synthesis of pyrimidine nucleotides is required for mammalian cells to proliferate. This gene encodes a trifunctional protein which is associated with the enzymatic activities of the first 3 enzymes in the 6-step pathway of pyrimidine biosynthesis: carbamoylphosphate synthetase (CPS II), aspartate transcarbamoylase, and dihydroorotase. This protein is regulated by the mitogen-activated…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 50 (0.660); congenital disorder of glycosylation type I (0.595); infantile epileptic-dyskinetic encephalopathy (0.499); type 2 diabetes mellitus (0.286); urolithiasis (0.283)
- **Europe PMC papers**: 60667
- **Why important**: CAD is connected to the central POMK branch and to NCAPG, and it encodes the multifunctional enzyme catalyzing the early steps of de novo pyrimidine biosynthesis. Nucleotide production is relevant to proliferating or biosynthetically active cells, while CAD has extensive literature and disease associations involving developmental and epileptic disorders and glycosylation disorders.
- **Conclusion**: Established evidence supports CAD as a core pyrimidine-biosynthesis enzyme whose abundance can reflect cellular biosynthetic demand. Its inclusion suggests that the module may capture a broad cellular-state signal, but there is no evidence that CAD is mechanistically linked to POMK or to the target tissues through this module.

#### MMS19

- **Related proteins** (co-abundance neighbors): POMK (0.87), ZNF451 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MMS19 cytosolic iron-sulfur assembly component. Enables estrogen receptor binding activity and transcription coactivator activity. Involved in several processes, including iron-sulfur cluster assembly; positive regulation of nucleobase-containing compound metabolic process; and protein maturation by iron-sulfur cluster transfer. Located in cytosol; nucleoplasm; and spindle. Part of CIA complex and MMXD complex. [provided by Alliance of Genome R…
- **Diseases (Open Targets)**: placental retention (0.334); neurodegenerative disease (0.242); liver disorder (0.131); respiratory system disorder (0.065); Reunion island Larsen syndrome (0.037)
- **Europe PMC papers**: 770
- **Why important**: MMS19 is directly connected to POMK and ZNF451 and is an established component of cytosolic iron-sulfur assembly and the CIA and MMXD complexes. Iron-sulfur cluster maturation connects cellular metabolism, protein maturation, and genome-associated processes. MMS19 also has comparatively extensive literature and disease links involving neurological and developmental phenotypes.
- **Conclusion**: Established evidence supports MMS19 as an iron-sulfur assembly and protein-maturation factor. Its network placement makes it a plausible indicator of intracellular maintenance or metabolic state, but the module does not establish a new MMS19 interaction or a direct role in autonomic or circulatory biology.

#### ZNF451

- **Related proteins** (co-abundance neighbors): EXOSC9 (0.84), MMS19 (0.83), GSTCD (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger protein 451. Enables SUMO ligase activity and transcription corepressor activity. Involved in negative regulation of nitrogen compound metabolic process; negative regulation of transforming growth factor beta receptor signaling pathway; and protein sumoylation. Located in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); ovarian neoplasm (0.176); coronary artery disorder (0.094); neoplasm (0.080); osteosarcoma (0.074)
- **Europe PMC papers**: 359
- **Why important**: ZNF451 connects EXOSC9 and MMS19 with GSTCD and is an established SUMO ligase and transcriptional corepressor. Its functions in protein sumoylation and negative regulation of transforming growth factor beta receptor signaling provide a plausible regulatory bridge among otherwise diverse module genes. It is tissue enhanced in bone marrow and has substantial literature and disease associations.
- **Conclusion**: Established evidence supports ZNF451 as a nuclear SUMO and transcriptional regulator. Its network position is consistent with a coordinating role in gene-expression state, but the hypothesis that it controls the module or mediates cross-tissue conservation remains untested.

## Module 4

**Tissue pair**: autonomic_nervous_system and circulatory_system  
**Genes (43)**: ABI2, AP3D1, ATAD3A, CEP41, CHD4, NCAPD2, COPG2, DDX19B, DDX10, DDX6, HSD17B7, DNAJC2, GNG11, GLS, H1-10, FECH, ITPA, JPT2, DTYMK, LMNB1, MAPRE2, MAT2B, MYBBP1A, CCDC51, MORC3, NELFCD, NTPCR, NUP155, NUP205, ALDH18A1, PIK3CA, NUP210, PTBP1, PFAS, RBBP4, SKIC3, TMEM70, TMOD1, UCHL3, UFD1, UMPS, WASHC5, ZW10

### Function

No GO/KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The gene-level evidence instead points to a mixed cellular-maintenance module. Its central network signal is associated with actin and cytoskeletal organization through TMOD1, with nuclear-envelope and nucleocytoplasmic transport biology through NUP155, NUP205, NUP210 and LMNB1, with chromatin regulation through CHD4 and RBBP4, and with mitochondrial and amino-acid metabolism through ALDH18A1, GLS and CCDC51. Additional genes support RNA processing, translation or protein quality control, nucleotide metabolism, vesicle trafficking and cell division. The most defensible interpretation is therefore coordinated structural, nuclear, metabolic and biosynthetic state rather than a single specific tissue pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: HPA reports no secreted genes. Most genes have low tissue specificity, and immune-cell specificity is generally low, arguing against a module composed primarily of mature blood immune cells. Nevertheless, HPA shows repeated enhancement in bone marrow, lymphoid tissue and erythrocyte or megakaryocyte progenitor populations, with additional signals in skeletal muscle, brain, testis and other specialized cell types. GNG11 is enriched in platelets and has basophil and neutrophil group enrichment, while FECH and LMNB1 show hematopoietic or erythroid-related signals. Thus, shared variation in blood or progenitor-cell representation could contribute to the cross-tissue module, although the evidence does not support calling it a purely blood-cell module. Protein-level HPA evidence is unavailable for both named tissue groups.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a small set of high-confidence known relationships rather than a densely connected interaction network. The strongest evidence concerns the nucleoporin relationships NUP155–NUP205 and NUP155–NUP210, plus the NUP205–NUP210 relationship; CHD4–RBBP4 also has very strong support. ALDH18A1–GLS is a strong metabolic association, while DTYMK–UMPS, HSD17B7–MAT2B, and the other listed pairs provide more limited support. hu.MAP independently places NUP155 and NUP210 together in one complex, UMPS and NUP205 together in two complexes, CHD4 and RBBP4 together in several chromatin-remodeling complexes, and ALDH18A1 and GLS together in a broad metabolic complex. LMNB1 and ATAD3A also co-occur in a membrane or organelle-associated complex. These results support real biological submodules embedded in the co-abundance graph, but the partial membership of the hu.MAP complexes and the sparse STRING support do not establish one unified physical complex.

**STRING interactions (score >= 0.7)**: 9 of 903 gene pairs: ALDH18A1–GLS (0.973); ALDH18A1–NELFCD (0.725); ALDH18A1–WASHC5 (0.734); CHD4–RBBP4 (0.999); DTYMK–UMPS (0.735); HSD17B7–MAT2B (0.746); NUP155–NUP205 (0.999); NUP155–NUP210 (0.991); NUP205–NUP210 (0.991)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07645.1 (NUP155, NUP210; 2/7); huMAP3_07789.1 (UMPS, NUP205; 2/7); huMAP3_10473.1 (LMNB1, ATAD3A; 2/24); huMAP3_09042.1 (UMPS, NUP205; 2/26); huMAP3_09499.1 (RBBP4, CHD4; 2/33); huMAP3_10472.1 (RBBP4, CHD4; 2/36); huMAP3_15128.1 (RBBP4, CHD4; 2/96); huMAP3_13468.1 (GLS, ALDH18A1; 2/99)

### Novelty

The module should not be described as a newly discovered molecular complex or as a novel pathway. Several of its strongest relationships are already known through STRING and hu.MAP, including nucleoporin, chromatin-remodeling and glutamine or glutamate-metabolism associations. What may be new is the cross-tissue co-abundance combination of these otherwise distinct cellular systems in autonomic nervous system and circulatory system samples. However, that observation could also arise from shared cell composition, broad housekeeping programs, or correlated tissue handling effects. Novelty therefore requires validation in independent cohorts, adjustment for cellular composition, and comparison with existing tissue coexpression modules; absence of an interaction in STRING or hu.MAP would not by itself demonstrate novelty.

**Hypothesis.** Mechanistic hypothesis: the module reflects a coordinated cellular state in which cytoskeletal organization and membrane or nuclear architecture are coupled to macromolecule transport, chromatin regulation and mitochondrial metabolism. TMOD1 may mark the structural or contractile component, the NUP155–NUP205–NUP210 group may support nuclear transport, CHD4–RBBP4 may represent transcriptional and chromatin control, and ALDH18A1–GLS may represent mitochondrial glutamate and amino-acid metabolism. In circulatory samples, hematopoietic or progenitor-cell representation may generate part of this shared signal; in autonomic or muscle-related samples, cytoskeletal and mitochondrial demands may reinforce it. This is a testable hypothesis, not a demonstrated causal mechanism.

### Important genes

#### TMOD1

- **Related proteins** (co-abundance neighbors): NUP155 (0.92), PFAS (0.90), DDX6 (0.89), TMEM70 (0.87), PTBP1 (0.87), DNAJC2 (0.87), UFD1 (0.87), UCHL3 (0.86), MYBBP1A (0.84), WASHC5 (0.83), UMPS (0.82), JPT2 (0.82), MORC3 (0.81), ALDH18A1 (0.81), CHD4 (0.81), ZW10 (0.81), NUP205 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tropomodulin 1. This gene encodes a member of the tropomodulin family. The encoded protein is an actin-capping protein that regulates tropomyosin by binding to its N-terminus, inhibiting depolymerization and elongation of the pointed end of actin filaments and thereby influencing the structure of the erythrocyte membrane skeleton. Multiple transcript variants encoding the same protein have been found for this gen…
- **Diseases (Open Targets)**: Barrett esophagus (0.359); neurodegenerative disease (0.272); fracture of pelvis (0.254); basal cell carcinoma (0.250); hypothyroidism (0.250)
- **Europe PMC papers**: 852
- **Why important**: TMOD1 is the principal network hub in the supplied graph and connects to genes spanning cytoskeletal, nuclear, metabolic and proteostasis signals. HPA shows tissue enhancement in skeletal muscle and tongue, with cell-type enhancement in cardiomyocytes, adrenal medulla cells and myonuclei. Its established function is actin pointed-end capping and regulation of the erythrocyte membrane skeleton, while its literature volume is substantial. This makes it a strong candidate for the structural component of a module shared by neural-autonomic and circulatory tissues.
- **Conclusion**: Established evidence supports TMOD1 as a structural and actin-related marker with a central position in this module. It is plausible, but not proven, that TMOD1 helps organize the shared tissue-state signal.

#### NUP155

- **Related proteins** (co-abundance neighbors): TMOD1 (0.92); STRING partners: NUP205 (0.999), NUP210 (0.991)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07645.1
- **Function (MyGene.info)**: nucleoporin 155. Nucleoporins are proteins that play an important role in the assembly and functioning of the nuclear pore complex (NPC) which regulates the movement of macromolecules across the nuclear envelope (NE). The protein encoded by this gene plays a role in the fusion of NE vesicles and formation of the double membrane NE. The protein may also be involved in cardiac physiology and may be associated with t…
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); atrial fibrillation (0.470); familial atrial fibrillation (0.390)
- **Europe PMC papers**: 944
- **Why important**: NUP155 is a component of the nuclear pore complex and has a direct STRING relationship with NUP205 and NUP210. It is also present with NUP210 in a hu.MAP complex. Its annotation includes nucleocytoplasmic transport, nuclear-envelope organization and RNA export, and its disease associations include atrial fibrillation. Its network connection to the major hub and its relevance to cardiac physiology make it especially informative for the tissue pair.
- **Conclusion**: Established evidence supports NUP155 as a nuclear-envelope and nuclear-transport component with cardiovascular disease relevance. A role as a mechanistic bridge between tissue state and autonomic or circulatory physiology remains a hypothesis.

#### ALDH18A1

- **Related proteins** (co-abundance neighbors): ABI2 (0.85), DDX19B (0.84), TMOD1 (0.81), CCDC51 (0.81); STRING partners: GLS (0.973), NELFCD (0.725), WASHC5 (0.734)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: aldehyde dehydrogenase 18 family member A1. This gene is a member of the aldehyde dehydrogenase family and encodes a bifunctional ATP- and NADPH-dependent mitochondrial enzyme with both gamma-glutamyl kinase and gamma-glutamyl phosphate reductase activities. The encoded protein catalyzes the reduction of glutamate to delta1-pyrroline-5-carboxylate, a critical step in the de novo biosynthesis of proline, ornithine and arginine. Mutations in …
- **Diseases (Open Targets)**: ALDH18A1-related de Barsy syndrome (0.832); cutis laxa, autosomal dominant 3 (0.816); autosomal recessive complex spastic paraplegia type 9B (0.814); de Barsy syndrome (0.731); autosomal dominant spastic paraplegia type 9 (0.706)
- **Europe PMC papers**: 1168
- **Why important**: ALDH18A1 occupies a connected position near the module hub and links to GLS in STRING and hu.MAP. It encodes a mitochondrial bifunctional enzyme in proline, ornithine and arginine biosynthesis and is annotated for glutamate and glutamine metabolism. Its disease associations include de Barsy syndrome and spastic-paraplegia disorders, and it has substantial literature support. It therefore represents a concrete metabolic axis within an otherwise heterogeneous module.
- **Conclusion**: Established evidence supports ALDH18A1 as a mitochondrial amino-acid metabolism gene with a known association to GLS. Its co-abundance with structural and nuclear genes may indicate shared cellular demand, but a direct causal coupling is not established.

#### CHD4

- **Related proteins** (co-abundance neighbors): TMOD1 (0.81); STRING partners: RBBP4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09499.1, huMAP3_10472.1, huMAP3_15128.1
- **Function (MyGene.info)**: chromodomain helicase DNA binding protein 4. The product of this gene belongs to the SNF2/RAD54 helicase family. It represents the main component of the nucleosome remodeling and deacetylase complex and plays an important role in epigenetic transcriptional repression. Patients with dermatomyositis develop antibodies against this protein. Somatic mutations in this gene are associated with serous endometrial tumors. Alternative splicing result…
- **Diseases (Open Targets)**: Sifrim-Hitz-Weiss syndrome (0.810); neurodegenerative disease (0.551); hereditary disease (0.505); endometrial cancer (0.470); uterine carcinosarcoma (0.439)
- **Europe PMC papers**: 3617
- **Why important**: CHD4 is paired with RBBP4 by a very strong STRING relationship and co-occurs with RBBP4 across several hu.MAP chromatin-remodeling complexes. It is a central component of the nucleosome remodeling and deacetylase complex and is annotated for chromatin remodeling, transcriptional repression and DNA repair. HPA shows enhancement in several neural and glial cell types, and the gene has substantial disease and literature support.
- **Conclusion**: Established evidence supports CHD4 as a chromatin-remodeling and transcriptional-regulation component of the module. Its contribution to the shared tissue co-abundance pattern is likely regulatory, but the specific target genes or direction of regulation are unknown.

#### GNG11

- **Related proteins** (co-abundance neighbors): HSD17B7 (0.95), NELFCD (0.90), MAPRE2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein subunit gamma 11. This gene is a member of the guanine nucleotide-binding protein (G protein) gamma family and encodes a lipid-anchored, cell membrane protein. As a member of the heterotrimeric G protein complex, this protein plays a role in this transmembrane signaling system. This protein is also subject to carboxyl-terminal processing. Decreased expression of this gene is associated with splenic marginal zone ly…
- **Diseases (Open Targets)**: bone fracture (0.271); alcohol drinking (0.127); ovarian carcinoma (0.060); ovarian cancer (0.051); ulcerative colitis (0.047)
- **Europe PMC papers**: 989
- **Why important**: GNG11 links the module to membrane G-protein signaling and has relationships with HSD17B7 and NELFCD in the co-abundance graph. HPA identifies platelet enrichment and group enrichment in basophils and neutrophils. Its established function is as a lipid-anchored gamma subunit of heterotrimeric G proteins, and its tissue or blood-cell pattern is particularly relevant when interpreting a module shared with circulatory samples.
- **Conclusion**: Established evidence supports GNG11 as a signaling and cell-composition indicator, especially for platelet or related blood-associated signals. It may help explain the circulatory component of the module, but it does not establish that the entire module is blood-derived.

## Module 5

**Tissue pair**: autonomic_nervous_system and circulatory_system  
**Genes (40)**: ABT1, AKAP9, ALDH2, ARFIP2, ATRX, CENPF, CWC22, CWC27, LIG3, LIG4, DNM1L, ADAR, FNDC3A, CAMK4, KIF20A, KIF15, KIF23, KMT2A, LAMC1, MDN1, MYLK, NDE1, OCIAD1, ODF2, PPP4R2, PRPF4, UPF3B, RFC2, RPAP1, POLR2A, POLR2B, PDCD11, RSU1, SCAMP1, SPATS2, UNC119B, UBQLN2, UTP4, XXYLT1, ZC3H7B

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established single pathway-level function. The gene annotations instead indicate a mixed nuclear and proliferative program. One component involves RNA polymerase II transcription through POLR2A, POLR2B and RPAP1, with associated ribosome biogenesis and transcriptional machinery involving PDCD11, UTP4 and ABT1. A second component involves pre-mRNA splicing through CWC22, CWC27 and PRPF4. A third component involves mitotic spindle organization, chromosome segregation and cytokinesis through CENPF, KIF15, KIF20A, KIF23 and NDE1. Additional branches involve DNA repair, chromatin regulation, RNA editing, cilium biology, vesicle transport, smooth-muscle contraction and extracellular-matrix organization. Thus, the most defensible interpretation is a coordinated expression module containing general nuclear gene-expression and cell-division machinery, rather than a specific autonomic or circulatory pathway. The absence of a globally enriched term does not by itself invalidate the module.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only LAMC1 is annotated as secreted to the extracellular matrix, and the remaining genes are intracellular or membrane-associated. Most genes have low tissue specificity, which is consistent with broadly expressed housekeeping-type machinery. HPA annotations also show recurrent association with lymphoid tissue, bone marrow, erythrocyte progenitors, megakaryocyte progenitors and testis or germ-cell populations. Several genes are cell-type enhanced in proliferative, hematopoietic, germ-cell, ciliated or neuronal populations, while most genes have low immune-cell specificity. This pattern makes shared cell composition, proliferative state or blood-associated material a plausible contributor to the cross-tissue co-abundance signal. It does not establish that the module is specific to autonomic nervous tissue or circulatory tissue. Protein-level HPA evidence for the two named tissue groups is unavailable, so tissue protein detection cannot independently validate the module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides established high-confidence relationships within several coherent substructures. The kinesin and mitotic group is supported by CENPF with KIF15, KIF20A, KIF23 and NDE1, and by the interconnected KIF15, KIF20A and KIF23 relationships. The spliceosome group is supported by CWC22 with CWC27, PRPF4 and UPF3B. The transcription and ribosome-biogenesis group is supported by POLR2A with POLR2B, POLR2B with PDCD11 and UTP4, and POLR2B with RPAP1. Other STRING-supported links connect DNA-repair proteins and additional module branches. hu.MAP independently places POLR2A, POLR2B and RPAP1 together in multiple RNA-polymerase-associated complexes, including (hu.MAP huMAP3_14318.1), (hu.MAP huMAP3_11092.1), (hu.MAP huMAP3_09843.1), (hu.MAP huMAP3_08487.1) and (hu.MAP huMAP3_06426.1). CWC22 and CWC27 recur together in spliceosome-related or associated complexes (hu.MAP huMAP3_07467.1), (hu.MAP huMAP3_08647.1), (hu.MAP huMAP3_09803.1), (hu.MAP huMAP3_11077.1), (hu.MAP huMAP3_11931.1) and (hu.MAP huMAP3_12350.1). These observations show that parts of the co-abundance module recover known molecular machinery. They support biological coherence for the submodules, but they do not demonstrate that all module genes form one physical complex or one unified pathway.

**STRING interactions (score >= 0.7)**: 19 of 780 gene pairs: ABT1–PDCD11 (0.727); ATRX–LIG4 (0.775); CENPF–KIF15 (0.959); CENPF–KIF20A (0.96); CENPF–KIF23 (0.93); CENPF–NDE1 (0.866); CWC22–CWC27 (0.999); CWC22–PRPF4 (0.916); CWC22–UPF3B (0.906); CWC27–PRPF4 (0.941); KIF15–KIF20A (0.942); KIF15–KIF23 (0.893); KIF20A–KIF23 (0.958); KIF23–LIG3 (0.747); LIG3–POLR2A (0.752); PDCD11–POLR2B (0.919); PDCD11–UTP4 (0.999); POLR2A–POLR2B (0.999); POLR2B–RPAP1 (0.746)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14318.1 (POLR2A, POLR2B, RPAP1; 3/58); huMAP3_11092.1 (POLR2A, POLR2B, RPAP1; 3/65); huMAP3_07467.1 (CWC27, CWC22; 2/5); huMAP3_08647.1 (CWC27, CWC22; 2/7); huMAP3_09803.1 (CWC27, CWC22; 2/9); huMAP3_11077.1 (CWC27, CWC22; 2/10); huMAP3_11931.1 (CWC27, CWC22; 2/19); huMAP3_09843.1 (POLR2A, POLR2B; 2/29); huMAP3_12350.1 (CWC27, CWC22; 2/34); huMAP3_08487.1 (POLR2A, RPAP1; 2/37); huMAP3_06426.1 (POLR2A, RPAP1; 2/38)

### Novelty

The co-abundance pattern may be a new observation for the autonomic-nervous-system and circulatory-system tissue pair, but the evidence is insufficient to call the complete module a new molecular mechanism. Several internal relationships correspond to well-established transcription, splicing, mitotic and DNA-repair machinery in STRING and hu.MAP, and many component genes have substantial prior literature and disease annotation. Conversely, the particular cross-tissue co-abundance combination, including its peripheral links among nuclear, cytoskeletal, ciliary, vesicular and extracellular-matrix genes, is not shown in the fact sheet to have been previously reported. Absence of a complete matching STRING or hu.MAP complex would not prove novelty, because co-abundance modules can capture shared regulation, cell composition or state rather than direct physical interaction. A claim of novelty would require replication in independent tissue cohorts, control for cell composition and comparison with previously published tissue co-expression modules.

**Hypothesis.** Hypothesis: the module reflects a shared transcriptional state of cells with active RNA production, RNA processing and cell-cycle or cytoskeletal remodeling, rather than a dedicated autonomic-circulatory function. In this model, POLR2A, POLR2B and RPAP1 represent transcriptional capacity; CWC22 and CWC27 coordinate transcript processing; and the CENPF-KIF15-KIF20A-KIF23 axis supports division-related microtubule remodeling. The presence of hematopoietic and germ-cell-associated HPA patterns suggests that variation in proliferative or immature cell populations could generate the signal in both tissue groups. MYLK, AKAP9, LAMC1 and related genes could connect this state to contractile, Golgi, cytoskeletal or matrix properties in particular samples. This is a testable hypothesis, not an established mechanism: it should be evaluated using cell-deconvolved expression, cell-cycle measurements, spatial data and perturbation or longitudinal evidence.

### Important genes

#### POLR2A

- **Related proteins** (co-abundance neighbors): AKAP9 (0.85); STRING partners: LIG3 (0.752), POLR2B (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14318.1, huMAP3_11092.1, huMAP3_09843.1, huMAP3_08487.1, huMAP3_06426.1
- **Function (MyGene.info)**: RNA polymerase II subunit A. This gene encodes the largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene contains a carboxy terminal domain composed of heptapeptide repeats that are essential for polymerase activity. These repeats contain serine and threonine residues that are phosphorylated in actively transcribing RNA polymerase. In addition, …
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and variable intellectual and behavioral abnormalities (0.738); HIV infectious disease (0.600); hereditary disease (0.479); syndromic intellectual disability (0.462); Orthomyxoviridae infectious disease (0.374)
- **Europe PMC papers**: 4546
- **Why important**: POLR2A is a high-connectivity module gene and the largest subunit of RNA polymerase II. It connects directly to POLR2B and is represented with POLR2B and RPAP1 in several hu.MAP complexes, including (hu.MAP huMAP3_14318.1), (hu.MAP huMAP3_11092.1), (hu.MAP huMAP3_09843.1), (hu.MAP huMAP3_08487.1) and (hu.MAP huMAP3_06426.1). Its HPA profile is enhanced in lymphoid tissue, and it has broad transcriptional and neurodevelopmental disease associations with extensive literature.
- **Conclusion**: Established: POLR2A is a central marker of the module's RNA-polymerase-associated machinery and provides strong support for a general transcriptional component. Hypothesis: coordinated POLR2A abundance may report increased transcriptional capacity or altered cellular composition in the shared tissue samples, but it does not identify a tissue-specific mechanism.

#### POLR2B

- **Related proteins** (co-abundance neighbors): PRPF4 (0.83), UTP4 (0.82); STRING partners: PDCD11 (0.919), POLR2A (0.999), RPAP1 (0.746)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14318.1, huMAP3_11092.1, huMAP3_09843.1
- **Function (MyGene.info)**: RNA polymerase II subunit B. This gene encodes the second largest subunit of RNA polymerase II (Pol II), a DNA-dependent RNA polymerase that catalyzes the transcription of DNA into precursors of mRNA, snRNA and microRNA. This subunit and the largest subunit form opposite sides of the center cleft of Pol II. Deletion of the flap loop region of this subunit results in a decrease in the rate of transcriptional elongation. Altern…
- **Diseases (Open Targets)**: HIV infectious disease (0.600); Orthomyxoviridae infectious disease (0.370); dengue disease (0.370); acrocephalosyndactyly (0.370); neurodegenerative disease (0.341)
- **Europe PMC papers**: 589
- **Why important**: POLR2B is the second major RNA polymerase II subunit, has a strong direct STRING relationship with POLR2A, and connects in STRING to PDCD11, UTP4, PRPF4 and RPAP1. It is present in the same hu.MAP transcriptional complexes as POLR2A and RPAP1, including (hu.MAP huMAP3_14318.1), (hu.MAP huMAP3_11092.1) and (hu.MAP huMAP3_09843.1). Its function directly supports transcription initiation and elongation, and its disease associations include infectious and neurodegenerative conditions.
- **Conclusion**: Established: POLR2B supports a known RNA polymerase II substructure within the module. Hypothesis: its co-abundance with ribosome-biogenesis and splicing genes may reflect coordinated demand for gene expression rather than a novel POLR2B-specific process.

#### RPAP1

- **Related proteins** (co-abundance neighbors): ABT1 (0.83), NDE1 (0.80); STRING partners: POLR2B (0.746)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14318.1, huMAP3_11092.1, huMAP3_08487.1, huMAP3_06426.1
- **Function (MyGene.info)**: RNA polymerase II associated protein 1. This protein forms part of the RNA polymerase II (RNAPII) enzyme complex and may recruit RNAPII to chromatin through its interaction with acetylated histones. [provided by RefSeq, Jul 2012].
- **Diseases (Open Targets)**: neurodegenerative disease (0.523); type 2 diabetes mellitus (0.345); diabetes mellitus (0.227); Crohn disease (0.181); cardiac arrhythmia (0.157)
- **Europe PMC papers**: 268
- **Why important**: RPAP1 is connected to ABT1 and NDE1 in the module and to POLR2B in STRING. It occurs with POLR2A and POLR2B across multiple hu.MAP complexes, including (hu.MAP huMAP3_14318.1), (hu.MAP huMAP3_11092.1), (hu.MAP huMAP3_08487.1) and (hu.MAP huMAP3_06426.1). Its established role in RNA polymerase II complex function makes it a useful bridge between the module network and the transcriptional machinery.
- **Conclusion**: Established: RPAP1 is credible evidence that the transcriptional branch is not based only on generic co-abundance, because it is supported by both STRING and hu.MAP complex membership. Hypothesis: RPAP1 may help couple transcriptional activity to the broader RNA-processing and proliferative state represented by the module.

#### CWC22

- **Related proteins** (co-abundance neighbors): NDE1 (0.87), UNC119B (0.87); STRING partners: CWC27 (0.999), PRPF4 (0.916), UPF3B (0.906)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07467.1, huMAP3_08647.1, huMAP3_09803.1, huMAP3_11077.1, huMAP3_11931.1, huMAP3_12350.1
- **Function (MyGene.info)**: CWC22 spliceosome associated protein. Enables RNA binding activity. Involved in mRNA splicing, via spliceosome. Located in cytosol and nuclear speck. Part of U2-type catalytic step 1 spliceosome; U2-type catalytic step 2 spliceosome; and U2-type precatalytic spliceosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.507); dengue disease (0.370); prostate carcinoma (0.330); mathematical ability (0.328); lagophthalmos (0.321)
- **Europe PMC papers**: 406
- **Why important**: CWC22 links NDE1 and UNC119B in the co-abundance network and has strong STRING relationships with CWC27, PRPF4 and UPF3B. It appears repeatedly with CWC27 in hu.MAP complexes (hu.MAP huMAP3_07467.1), (hu.MAP huMAP3_08647.1), (hu.MAP huMAP3_09803.1), (hu.MAP huMAP3_11077.1), (hu.MAP huMAP3_11931.1) and (hu.MAP huMAP3_12350.1). Its established spliceosome role and nuclear-speckle localization provide a mechanistic connection between transcription and post-transcriptional RNA processing.
- **Conclusion**: Established: CWC22 identifies a coherent spliceosome-associated branch supported by both STRING and hu.MAP. Hypothesis: its co-abundance with mitotic and transcriptional genes could reflect coordinated RNA processing during proliferative or developmentally active cell states.

#### KIF23

- **Related proteins** (co-abundance neighbors): UNC119B (0.90), UPF3B (0.84), LIG4 (0.83), ATRX (0.82); STRING partners: CENPF (0.93), KIF15 (0.893), KIF20A (0.958), LIG3 (0.747)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 23. The protein encoded by this gene is a member of kinesin-like protein family. This family includes microtubule-dependent molecular motors that transport organelles within cells and move chromosomes during cell division. This protein has been shown to cross-bridge antiparallel microtubules and drive microtubule movement in vitro. Alternate splicing of this gene results in multiple transcript variant…
- **Diseases (Open Targets)**: congenital dyserythropoietic anemia type 3 (0.735); hypertensive disorder (0.436); neurodegenerative disease (0.370); cardiovascular disorder (0.302); essential hypertension (0.302)
- **Europe PMC papers**: 2136
- **Why important**: KIF23 is connected to UNC119B, UPF3B, LIG4 and ATRX in the module and is embedded in a strongly interconnected STRING kinesin group with CENPF, KIF15 and KIF20A. Its established functions include mitotic cytokinesis, spindle-midzone assembly and microtubule-based movement. HPA associates it with bone marrow, lymphoid tissue and erythrocyte progenitors, while disease annotations include congenital dyserythropoietic anemia, hypertension and cardiovascular disorder.
- **Conclusion**: Established: KIF23 supports a cell-division and microtubule-remodeling submodule with clear relevance to hematopoietic cell populations. Hypothesis: KIF23 may be a useful indicator that the shared tissue signal is partly driven by proliferative or immature blood-associated cells, rather than by mature autonomic or vascular cells.

#### MYLK

- **Related proteins** (co-abundance neighbors): RSU1 (0.88), ZC3H7B (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin light chain kinase. This gene, a muscle member of the immunoglobulin gene superfamily, encodes myosin light chain kinase which is a calcium/calmodulin dependent enzyme. This kinase phosphorylates myosin regulatory light chains to facilitate myosin interaction with actin filaments to produce contractile activity. This gene encodes both smooth muscle and nonmuscle isoforms. In addition, using a separate promoter in an …
- **Diseases (Open Targets)**: aortic aneurysm, familial thoracic 7 (0.767); familial thoracic aortic aneurysm and aortic dissection (0.710); megacystis-microcolon-intestinal hypoperistalsis syndrome 1 (0.617); megacystis-microcolon-intestinal hypoperistalsis syndrome (0.597); Rare genetic vascular disease (0.483)
- **Europe PMC papers**: 10503
- **Why important**: MYLK connects RSU1 and ZC3H7B and is tissue enhanced in smooth muscle and seminal vesicle. Its established function is calcium-dependent phosphorylation of myosin light chains to promote actomyosin contraction, and its HPA single-cell annotations include smooth-muscle-related, megakaryocyte and platelet populations. It has extensive literature and disease associations involving thoracic aortic aneurysm, aortic dissection and other vascular disorders.
- **Conclusion**: Established: MYLK provides a biologically relevant contractile and vascular-facing component within an otherwise largely nuclear module. Hypothesis: MYLK may connect the general transcriptional or proliferative state to smooth-muscle, platelet or vascular cell composition in circulatory samples, but its sparse direct network connectivity argues against treating it as the module's primary molecular driver.

## Module 6

**Tissue pair**: autonomic_nervous_system and circulatory_system  
**Genes (32)**: ADAM10, ACTR8, CASP2, NCAPG2, CTR9, DDX52, EIF3L, MPP1, GCSH, GRK3, GSK3B, CPOX, HMGCS1, EIF4E2, KLC4, LEPROTL1, NOL6, ORC4, PDIA4, PHB1, TP53I3, RFC1, MRPL50, RSF1, MRPS33, RUSF1, SMYD3, SRCAP, TAF6L, TMA16, TTK, TXLNG

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. The module therefore does not support a narrowly defined autonomic or circulatory pathway on enrichment evidence alone. Its genes instead span several established cellular programs: mitotic chromosome segregation and chromatin organization through NCAPG2, TTK, ACTR8, SRCAP, TAF6L, ORC4, RFC1 and RSF1; RNA and ribosome biogenesis through DDX52, NOL6 and TMA16; mitochondrial translation through MRPS33 and MRPL50; intracellular transport through KLC4 and TXLNG; membrane signaling and proteolysis through GRK3 and ADAM10; protein folding and secretion through PDIA4; heme biosynthesis through CPOX; and metabolism or stress responses through HMGCS1, GSK3B, CASP2 and TP53I3. The network is therefore more consistent with a mixed cellular state involving proliferation, biosynthetic capacity, signaling regulation and stress handling than with a single established tissue-specific function. The strongest network connectivity is concentrated around NCAPG2, DDX52, GRK3 and TAF6L, but connectivity alone does not establish a shared biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a small secreted component, and the individual secretome annotations are mostly absent or intracellular and membrane-associated. Most genes have low tissue specificity and low immune-cell specificity, which is compatible with broadly expressed cellular machinery rather than a specialized autonomic or vascular program. The HPA cell-type annotations nevertheless show recurring enrichment in late spermatids and late primary spermatocytes, with additional representation of erythrocyte progenitors, hepatocytes, neutrophils and monocyte-related cells. Bone marrow and lymphoid tissue also recur among tissue-enhanced annotations. This pattern raises the possibility that the shared signal reflects common cell-state composition, proliferative or biosynthetic activity, or sample admixture rather than a function intrinsic to autonomic nervous tissue and circulatory tissue. It does not by itself demonstrate blood contamination, because most genes are not immune-cell specific and the module contains diverse intracellular genes.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports only a sparse set of high-confidence relationships within the module: ACTR8 with SRCAP, DDX52 with NOL6, GSK3B with KLC4, and MRPL50 with MRPS33. These relationships provide established anchors for chromatin remodeling, nucleolar RNA processing, signaling or transport, and mitochondrial translation, respectively, but they do not connect the entire module into one known protein interaction system. hu.MAP identifies ADAM10 and PDIA4 together in (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). These shared memberships are useful evidence for a possible membrane-protein-processing and endoplasmic-reticulum or secretory relationship, although each complex contains many members and only a small subset is represented in the module. The lack of additional hu.MAP assignments for the other genes and the limited STRING connectivity indicate that the co-abundance network is not simply a recovered canonical complex.

**STRING interactions (score >= 0.7)**: 4 of 496 gene pairs: ACTR8–SRCAP (0.801); DDX52–NOL6 (0.992); GSK3B–KLC4 (0.932); MRPL50–MRPS33 (0.922)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (ADAM10, PDIA4; 2/60); huMAP3_09327.1 (ADAM10, PDIA4; 2/93)

### Novelty

The co-abundance association across autonomic_nervous_system and circulatory_system may be a new observation, but the available evidence does not justify calling the biological mechanism novel. Several component functions and some pairwise relationships are already well established, including the DDX52–NOL6, ACTR8–SRCAP, GSK3B–KLC4 and MRPL50–MRPS33 STRING relationships and the ADAM10–PDIA4 hu.MAP memberships in (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Conversely, the sparse STRING structure, absence of globally significant GO/KEGG enrichment, and lack of a single coherent complex make it unlikely that the module corresponds to a previously defined canonical pathway as a whole. The defensible novelty claim is therefore limited: the tissue-pair-specific co-abundance pattern and its particular combination of genes may be new, whereas novelty of the underlying molecular functions is not established. Replication in independent tissue cohorts, adjustment for cell composition, and experimental testing would be required before claiming a new tissue mechanism.

**Hypothesis.** Hypothesis: the module represents a shared cellular-state program present in both tissue groups, rather than a dedicated autonomic-circulatory pathway. A proliferative or progenitor-like component could contribute NCAPG2, TTK, ORC4, RFC1 and related chromatin or replication genes; high biosynthetic demand could contribute DDX52, NOL6, TMA16, MRPS33 and MRPL50; cell-surface signaling and trafficking could be coordinated through GRK3, ADAM10, KLC4 and TXLNG; and proteostasis or metabolic stress could involve PDIA4, GSK3B, CASP2, HMGCS1 and TP53I3. The recurrent HPA annotations for reproductive, marrow, erythroid and myeloid cell states suggest that shared cell composition or cell-state variation may generate much of the signal. This is a testable hypothesis, not an established function: it should be examined by cell-type deconvolution, analysis of matched purified cell populations, and validation of whether the co-abundance relationships persist after controlling for proliferation, mitochondrial activity and sample composition.

### Important genes

#### GRK3

- **Related proteins** (co-abundance neighbors): NCAPG2 (0.92), KLC4 (0.91), TMA16 (0.83), NOL6 (0.82), CASP2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein-coupled receptor kinase 3. The beta-adrenergic receptor kinase specifically phosphorylates the agonist-occupied form of the beta-adrenergic and related G protein-coupled receptors. Overall, the beta adrenergic receptor kinase 2 has 85% amino acid similarity with beta adrenergic receptor kinase 1, with the protein kinase catalytic domain having 95% similarity. These data suggest the existence of a family of receptor kinases …
- **Diseases (Open Targets)**: Dental malocclusion (0.269); adolescent idiopathic scoliosis (0.266); ocular hypotension (0.258); bone neoplasm (0.245); connective tissue neoplasm (0.245)
- **Europe PMC papers**: 1559
- **Why important**: GRK3 is one of the most connected genes in the module and links NCAPG2, KLC4, TMA16, NOL6 and CASP2. Its established function is phosphorylation and desensitization of activated G-protein-coupled receptors, including receptor internalization, making it the clearest signaling-related hub in a module shared by tissues with major neural and cardiovascular signaling interfaces. HPA annotations associate it with adipose tissue and multiple immune or myeloid cell types, while the literature volume is substantial relative to many of the less characterized module genes.
- **Conclusion**: Established evidence supports GRK3 as a regulator of GPCR signaling and receptor desensitization. Its network position supports its importance for interpreting the module. It is a plausible mediator of shared signaling-state variation, but the data do not establish that GRK3 drives the co-abundance module or that the module represents autonomic signaling.

#### ADAM10

- **Related proteins** (co-abundance neighbors): TAF6L (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: ADAM metallopeptidase domain 10. Members of the ADAM family are cell surface proteins with a unique structure possessing both potential adhesion and protease domains. This gene encodes and ADAM family member that cleaves many proteins including TNF-alpha and E-cadherin. Alternate splicing results in multiple transcript variants encoding different proteins that may undergo similar processing. [provided by RefSeq, Feb 2016].
- **Diseases (Open Targets)**: reticulate acropigmentation of Kitamura (0.679); Alzheimer disease 18 (0.621); Alzheimer disease (0.522); dementia (0.415); schizophrenia (0.354)
- **Europe PMC papers**: 11139
- **Why important**: ADAM10 is a membrane-associated metalloprotease involved in ectodomain proteolysis, including cleavage of TNF-alpha and E-cadherin, and in Notch signaling. It is linked to TAF6L in the co-abundance graph and is one of the two module members shared by both hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), together with PDIA4. Its plasma-membrane and vesicular localization and extensive disease literature make it an important candidate for connecting cell-surface remodeling with the broader module state.
- **Conclusion**: Established evidence supports ADAM10 as a membrane protease and signaling regulator, and hu.MAP provides supporting complex context with PDIA4. A role for ADAM10 in a shared tissue-interface or cell-adhesion process is plausible, but the module does not prove a direct ADAM10-centered mechanism.

#### GSK3B

- **Related proteins** (co-abundance neighbors): TAF6L (0.91); STRING partners: KLC4 (0.932)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycogen synthase kinase 3 beta. The protein encoded by this gene is a serine-threonine kinase belonging to the glycogen synthase kinase subfamily. It is a negative regulator of glucose homeostasis and is involved in energy metabolism, inflammation, ER-stress, mitochondrial dysfunction, and apoptotic pathways. Defects in this gene have been associated with Parkinson disease and Alzheimer disease. [provided by RefSeq, Aug 2017].
- **Diseases (Open Targets)**: bipolar disorder (0.614); major depressive disorder (0.572); bipolar I disorder (0.571); cancer (0.557); Alzheimer disease (0.554)
- **Europe PMC papers**: 15204
- **Why important**: GSK3B is connected to TAF6L and has a high-confidence STRING relationship with KLC4. It is an extensively studied serine-threonine kinase involved in energy metabolism, inflammation, ER stress, mitochondrial dysfunction and apoptosis, with annotations also related to heart valve development and cell-matrix adhesion. Its broad functional reach and very large literature base make it a useful integrator of signaling, metabolic and stress-related interpretations.
- **Conclusion**: Established evidence supports GSK3B as a multifunctional kinase that can couple metabolic, inflammatory and stress pathways. Its presence is compatible with a shared cellular-state program, but it is too pleiotropic to identify the module function by itself, and no causal role is demonstrated.

#### NCAPG2

- **Related proteins** (co-abundance neighbors): GRK3 (0.92), RUSF1 (0.89), EIF3L (0.86), MRPL50 (0.82), ACTR8 (0.82), RSF1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: non-SMC condensin II complex subunit G2. This gene encodes a protein that belongs to the Condensin2nSMC family of proteins. The encoded protein is a regulatory subunit of the condensin II complex which, along with the condensin I complex, plays a role in chromosome assembly and segregation during mitosis. A similar protein in mouse is required for early development of the embryo. Alternate splicing results in multiple transcript variants…
- **Diseases (Open Targets)**: Khan-Khan-Katsanis syndrome (0.667); neurodegenerative disease (0.344); neoplasm (0.103); cancer (0.101); lung adenocarcinoma (0.098)
- **Europe PMC papers**: 554
- **Why important**: NCAPG2 has the strongest network centrality in the supplied graph and connects genes involved in signaling, translation, mitochondrial machinery and chromatin remodeling. Its established role is as a regulatory subunit of condensin II, supporting chromosome assembly, condensation and segregation during mitosis. HPA annotations emphasize bone marrow, lymphoid tissue and progenitor cell states, which is relevant to the possibility that proliferative or progenitor-cell composition contributes to the shared signal.
- **Conclusion**: Established evidence supports NCAPG2 as a mitotic chromosome-organization factor and a central network component. Its HPA pattern supports a progenitor or proliferative-state interpretation, but does not establish that the module is a blood-cell module or that mitosis is the primary driver in either tissue group.

#### TTK

- **Related proteins** (co-abundance neighbors): DDX52 (0.89), EIF4E2 (0.88); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TTK protein kinase. This gene encodes a dual specificity protein kinase with the ability to phosphorylate tyrosine, serine and threonine. Associated with cell proliferation, this protein is essential for chromosome alignment at the centromere during mitosis and is required for centrosome duplication. It has been found to be a critical mitotic checkpoint protein for accurate segregation of chromosomes during mitosis. …
- **Diseases (Open Targets)**: neurodegenerative disease (0.551); Alzheimer disease (0.380); Parkinson disease (0.375); lysosomal storage disease (0.375); ulna fracture (0.300)
- **Europe PMC papers**: 4437
- **Why important**: TTK connects DDX52 and EIF4E2 and is a well-established mitotic checkpoint kinase required for chromosome alignment, spindle assembly checkpoint signaling and accurate chromosome segregation. Its HPA annotations include bone marrow, lymphoid tissue and erythrocyte or megakaryocyte progenitor states, while its disease and literature evidence is extensive. Together with NCAPG2 and other chromatin or replication genes, it provides a biologically coherent anchor for a possible cell-cycle component.
- **Conclusion**: Established evidence supports TTK as a mitotic checkpoint regulator. Its presence strengthens the interpretation that cell-cycle or progenitor-state variation may contribute to the module. It does not demonstrate active proliferation in the sampled tissues or define a tissue-specific mechanism.

#### PDIA4

- **Related proteins** (co-abundance neighbors): LEPROTL1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 is connected to LEPROTL1 and is paired with ADAM10 in both hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Its established function is ER protein folding, thiol-disulfide exchange, protein secretion and response to ER stress. HPA detects it in hepatocytes and plasma cells and annotates it as intracellular and membrane-associated, providing a plausible proteostasis link to secretory or membrane-protein handling.
- **Conclusion**: Established evidence supports PDIA4 as an ER proteostasis factor, and the repeated hu.MAP pairing with ADAM10 supports a shared complex context. A connection between ER proteostasis and cell-surface proteolysis is a reasonable mechanistic possibility, but the co-abundance data do not establish direct physical interaction or directionality.

## Module 7

**Tissue pair**: autonomic_nervous_system and circulatory_system  
**Genes (27)**: ALG1, CD2AP, COA7, IPO4, PRPSAP2, LAS1L, LNPEP, MAD1L1, NIPBL, PDCD2L, CTSA, PRPF31, PRPF39, PSMB3, PYGB, RAB5B, RELL1, RRM1, RPL3, RXRA, SACM1L, PSAT1, FARSB, TBCE, TMEM50B, VIM, WDR36

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically validated pathway-level annotation from those analyses. The gene set is biologically heterogeneous, with signals involving membrane and cytoskeletal organization, intracellular trafficking, metabolism, RNA processing and ribosome biogenesis. RELL1 is the main co-abundance hub and connects genes such as VIM, CD2AP, CTSA, LNPEP, SACM1L, PYGB and PRPSAP2, while RXRA links several genes involved in nuclear regulation, protein turnover and ribosome biogenesis. These patterns are more consistent with a co-abundance program reflecting shared cellular state or cellular composition than with a single well-established molecular complex. The biological interpretation should therefore remain broad and provisional.

**Cell composition.** The module is not dominated by plasma or conventionally secreted proteins: the HPA summary identifies only a small secreted component, with CTSA and LNPEP described as intracellular or membrane-associated secretome proteins rather than a plasma-protein signature. Most genes have low tissue specificity, and most have cell-type-enhanced rather than broadly uniform expression. Enrichment of annotations involving brain-associated cells, glial and ventricular epithelial populations, reproductive cells, and selected immune populations suggests that shared cell types or cellular-state variation may contribute to the cross-tissue co-abundance. The overall HPA blood-cell signal is limited, although RELL1, RXRA, CTSA, CD2AP, PSAT1 and related genes have selected immune or platelet-associated annotations. HPA provides no matching tissue-level protein-detection result for either named tissue, so protein-level localization in these tissues cannot be inferred from this fact sheet.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no supplementary functional enrichment and identifies only the LAS1L–PRPF31 relationship among the tested module pairs. This is a known connection between a ribosome-biogenesis factor and a spliceosome component, but it does not explain the whole module. hu.MAP identifies RPL3 and WDR36 together in (hu.MAP huMAP3_03966.1) and (hu.MAP huMAP3_08465.1). In both cases, they are only a subset of a larger complex, so the evidence supports a shared ribosome-related complex context rather than complete recovery of either complex. The sparse STRING connectivity and partial hu.MAP overlap indicate that most co-abundance edges are not established physical interactions in these resources. Thus, the network should not be interpreted as a single protein complex.

**STRING interactions (score >= 0.7)**: 1 of 351 gene pairs: LAS1L–PRPF31 (0.902)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03966.1 (RPL3, WDR36; 2/10); huMAP3_08465.1 (RPL3, WDR36; 2/17)

### Novelty

The exact cross-tissue co-abundance module may be a new observation, because the supplied resources show little direct physical-interaction support and no globally significant GO or KEGG annotation. However, those absences do not establish novelty: many constituent genes and biological processes are well studied, and the module may arise from shared cell composition, coordinated expression, or technical and biological variation common to the two tissue groups. The defensible conclusion is that the module-level combination is potentially novel, but it is not demonstrated to be a newly discovered mechanism. Establishing novelty would require comparison with published co-expression modules, tissue deconvolution results, and independently replicated datasets.

**Hypothesis.** Hypothesis: the module represents a shared cellular-maintenance and stress-adaptation program present in cell populations sampled from both autonomic nervous and circulatory tissues. RELL1-associated membrane, cytoskeletal and signaling biology may be coupled to VIM and CD2AP-dependent structural or trafficking processes, while ALG1, PSAT1 and mitochondrial or proteostasis genes support glycoprotein production, intermediary metabolism and organelle function. RXRA could provide a transcriptional regulatory link, and the RPL3–WDR36 and LAS1L–PRPF31 observations suggest a smaller RNA and ribosome biogenesis component. This is a mechanistic hypothesis, not an enrichment result or proof of direct physical cooperation. It should be tested by cell-type-resolved expression analysis, perturbation of the hub genes, and independent replication across samples.

### Important genes

#### RELL1

- **Related proteins** (co-abundance neighbors): PYGB (0.94), CTSA (0.91), PRPSAP2 (0.89), LNPEP (0.89), ALG1 (0.89), SACM1L (0.83), MAD1L1 (0.82), CD2AP (0.82), PRPF31 (0.81), VIM (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Microtubules; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RELT like 1. Involved in positive regulation of p38MAPK cascade. Located in microtubule cytoskeleton and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: placental abruption (0.275); placental retention (0.173); contracture (0.136); esophageal cancer (0.121); urolithiasis (0.071)
- **Europe PMC papers**: 229
- **Why important**: RELL1 is the principal network hub in the supplied subgraph and connects genes spanning metabolism, membrane biology, cytoskeletal organization and intracellular processing. HPA links it to brain tissue and to neutrophil-related cell annotations, while MyGene.info describes positive regulation of the p38MAPK cascade and localization at the plasma membrane and microtubules. Its disease-association evidence includes placental and other disorders, and its literature is substantial enough to support biological relevance without making it a well-established explanation for this module.
- **Conclusion**: Established evidence supports RELL1 as the strongest network organizer and a membrane or microtubule-associated signaling protein. It is plausible that RELL1 helps coordinate the module's cellular-state signal, but a causal role in the shared autonomic–circulatory program is a hypothesis.

#### RXRA

- **Related proteins** (co-abundance neighbors): ALG1 (0.86), WDR36 (0.86), LAS1L (0.85), IPO4 (0.82), PSMB3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: retinoid X receptor alpha. Retinoid X receptors (RXRs) and retinoic acid receptors (RARs) are nuclear receptors that mediate the biological effects of retinoids by their involvement in retinoic acid-mediated gene activation. These receptors function as transcription factors by binding as homodimers or heterodimers to specific sequences in the promoters of target genes. The protein encoded by this gene is a member of the ste…
- **Diseases (Open Targets)**: psoriasis (0.583); primary cutaneous T-cell non-Hodgkin lymphoma (0.551); psoriasis vulgaris (0.517); urinary bladder cancer (0.507); neoplasm (0.480)
- **Europe PMC papers**: 5301
- **Why important**: RXRA is a nuclear receptor with broad transcriptional functions and is positioned between several module branches, including ALG1, WDR36, LAS1L, IPO4 and PSMB3. HPA shows low tissue specificity but selected liver and immune-cell annotations. MyGene.info supports roles in retinoid-mediated gene activation, hormone signaling and nervous-system development, and RXRA has a large literature and multiple disease associations. Its network placement makes it a candidate regulatory bridge rather than evidence of a direct physical interaction with all of its neighbors.
- **Conclusion**: Established evidence supports RXRA as a transcriptional regulator with broad systemic biology and strong literature support. Its role as a regulator of this particular co-abundance module remains unproven, but it is a reasonable candidate for testing as an upstream state-dependent factor.

#### VIM

- **Related proteins** (co-abundance neighbors): RELL1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vimentin. This gene encodes a type III intermediate filament protein. Intermediate filaments, along with microtubules and actin microfilaments, make up the cytoskeleton. The encoded protein is responsible for maintaining cell shape and integrity of the cytoplasm, and stabilizing cytoskeletal interactions. This protein is involved in neuritogenesis and cholesterol transport and functions as an organizer of a…
- **Diseases (Open Targets)**: dengue disease (0.516); early-onset non-syndromic cataract (0.462); early-onset partial cataract (0.458); Developmental cataract (0.435); cataract (0.372)
- **Europe PMC papers**: 86568
- **Why important**: VIM is directly connected to RELL1 and is the clearest structural marker in the module. HPA shows tissue enhancement in blood vessel and cell-type enhancement in stromal, fibroblast and hepatic stellate populations. MyGene.info describes intermediate-filament organization, maintenance of cell shape, migration, signaling and axon extension. VIM also has exceptionally large literature volume and broad disease associations, making it an important interpretive anchor for a module shared by neural-autonomic and circulatory tissues.
- **Conclusion**: Established evidence supports VIM as a cytoskeletal and cell-state marker compatible with vascular, stromal and neural structural biology. Its presence may indicate shared structural or cellular-composition variation, but it does not by itself establish a specialized autonomic vascular mechanism.

#### ALG1

- **Related proteins** (co-abundance neighbors): RELL1 (0.89), RXRA (0.86), NIPBL (0.84), TMEM50B (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ALG1 chitobiosyldiphosphodolichol beta-mannosyltransferase. The enzyme encoded by this gene catalyzes the first mannosylation step in the biosynthesis of lipid-linked oligosaccharides. This gene is mutated in congenital disorder of glycosylation type Ik. [provided by RefSeq, Dec 2008].
- **Diseases (Open Targets)**: ALG1-congenital disorder of glycosylation (0.857); congenital disorder of glycosylation (0.613); neurodegenerative disease (0.536); hereditary disease (0.510); congenital disorder of glycosylation type I (0.436)
- **Europe PMC papers**: 695
- **Why important**: ALG1 occupies a connective position between RELL1, RXRA, NIPBL and TMEM50B. It encodes an endoplasmic-reticulum enzyme required for an early step in lipid-linked oligosaccharide and protein N-glycosylation. HPA indicates low tissue specificity, and disease evidence strongly links ALG1 to congenital glycosylation disorders and broader neurodegenerative or hereditary phenotypes. Its function provides a plausible cellular-maintenance explanation for coordinated expression with trafficking and membrane-associated genes.
- **Conclusion**: Established evidence supports ALG1 as a core glycoprotein-biosynthesis enzyme with important developmental and neurological disease relevance. Its participation in this module most likely reflects secretory-pathway or cellular-maintenance demands; a specific role in autonomic or circulatory tissue biology is still a hypothesis.

#### CTSA

- **Related proteins** (co-abundance neighbors): RELL1 (0.91); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cathepsin A. This gene encodes a member of the peptidase S10 family of serine carboxypeptidases. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate two chains that comprise the heterodimeric active enzyme. This enzyme possesses deamidase, esterase and carboxypeptidase activities and acts as a scaffold in the …
- **Diseases (Open Targets)**: galactosialidosis (0.842); cathepsin a-related arteriopathy-strokes-leukoencephalopathy (0.464); hereditary disease (0.451); lysosomal storage disease (0.373); Lynch syndrome (0.340)
- **Europe PMC papers**: 8422
- **Why important**: CTSA is connected to the RELL1 hub and has a distinctive HPA annotation in platelets, with vesicular localization and intracellular or membrane-associated secretome status. It encodes a lysosomal serine carboxypeptidase with proteolytic, esterase, deamidase and scaffold functions in a multienzyme complex. CTSA has substantial literature and a strong association with galactosialidosis and related vascular or neurological disease. These features make it relevant to lysosomal processing, vesicle biology and possible blood-cell or vascular composition effects.
- **Conclusion**: Established evidence supports CTSA as a lysosomal and vesicle-associated enzyme with platelet and disease relevance. Its co-abundance with RELL1 may reflect vesicular or cellular-composition biology, but direct participation in the module's shared tissue mechanism is not established.

#### RPL3

- **Related proteins** (co-abundance neighbors): COA7 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_03966.1, huMAP3_08465.1
- **Function (MyGene.info)**: ribosomal protein L3. Ribosomes, the complexes that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L3P family of ribosomal proteins and it is located in the cytoplasm. The p…
- **Diseases (Open Targets)**: Duchenne muscular dystrophy (0.506); Orthomyxoviridae infectious disease (0.463); cystic fibrosis (0.389); neuromuscular disease caused by qualitative or quantitative defects of dystrophin (0.323); inflammatory bowel disease (0.308)
- **Europe PMC papers**: 2316
- **Why important**: RPL3 is one of the two module members jointly represented in both hu.MAP contexts (hu.MAP huMAP3_03966.1) and (hu.MAP huMAP3_08465.1), together with WDR36. It is a large-subunit ribosomal protein with established roles in translation and spermatogenesis. Although its network degree is modest, its complex annotations give it disproportionate interpretive value: it anchors the module's partial ribosome and RNA-processing signal. RPL3 also has broad disease and literature support.
- **Conclusion**: Established evidence supports RPL3 as a ribosomal component and as part of the partial hu.MAP complex overlap. Its module-level signal is more consistent with translation or cell-state variation than with a tissue-specific ribosomal complex, and any specialized mechanistic role is hypothetical.

## Module 8

**Tissue pair**: autonomic_nervous_system and circulatory_system  
**Genes (7)**: ANAPC5, CTNNA2, HYOU1, CKMT1A, PTCD3, SLC25A13, TEX10

### Function

No GO or KEGG term passed global correction, and STRING reported no functional enrichment. The module therefore does not support a narrowly defined pathway-level function on enrichment evidence alone. Its genes instead suggest a mixed cellular program involving neuronal and cell-adhesion biology through CTNNA2, endoplasmic-reticulum stress and protein-folding responses through HYOU1, mitochondrial transport and energy metabolism through SLC25A13 and CKMT1A, mitochondrial translation through PTCD3, cell-cycle ubiquitin control through ANAPC5, and ribosomal RNA processing through TEX10. The co-abundance structure may therefore reflect coordinated cellular state, organelle activity, or tissue composition rather than a single established molecular pathway.

**Cell composition.** The module does not look predominantly like a plasma-protein or blood-cell module. The HPA summary shows low immune-cell specificity for most genes, with one gene enriched in basophils and one not detected in immune cells. The per-gene secretome annotations describe HYOU1 and CKMT1A as intracellular and membrane-associated rather than as classical circulating proteins, although the module summary marks two genes as secreted. Most genes have low tissue specificity, while several show cell-type enhancement in brain neurons, astrocytes, cardiomyocytes, enteric or intestinal populations, and other specialized cells. CTNNA2 is especially associated with brain-related cell types, whereas SLC25A13 is tissue enriched in liver and CKMT1A is tissue enhanced in brain, esophagus, and intestine. Protein-level HPA evidence is unavailable for both named tissue groups, so a blood-contamination explanation is not supported but cannot be completely excluded.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module gene pair had a high-confidence STRING interaction in the supplied analysis, and no hu.MAP complex contained multiple module members. Thus the co-abundance edges should not be interpreted as established physical protein interactions. Known biology is instead distributed across distinct processes: CTNNA2 participates in cytoskeletal organization and neuronal development; HYOU1 supports stress-related ER protein folding and secretion; SLC25A13 performs calcium-regulated mitochondrial metabolite exchange; CKMT1A supports phosphocreatine production; ANAPC5 is part of the anaphase-promoting complex; TEX10 participates in ribosomal RNA processing; and PTCD3 supports mitochondrial translation. The absence of STRING and hu.MAP support suggests that the module is not a recognized protein complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a candidate co-abundance association rather than an established new biological module. Its genes have individually documented functions and disease links, but the supplied resources provide no recognized physical complex, no high-confidence STRING relationship, and no globally significant GO or KEGG enrichment. Those observations make the shared tissue-pair association potentially interesting, particularly because it joins neuronal, mitochondrial, stress-response, and cell-cycle genes, but they do not establish that it is novel. Confirmation would require replication in independent samples, preservation of the association after cell-composition adjustment, and comparison with existing tissue coexpression resources.

**Hypothesis.** Hypothesis: the module may represent a shared cellular-state signal across autonomic nervous and circulatory tissues in which specialized neuronal or excitable-cell biology is coupled to mitochondrial energy handling and proteostatic stress. CTNNA2 could mark the neuronal or structural component, CKMT1A and SLC25A13 could reflect energy and mitochondrial metabolite flux, HYOU1 could reflect stress-adaptive protein folding, and the remaining genes could reflect general biosynthetic and regulatory demands. This is a mechanistic proposal, not an established pathway assignment, because enrichment, physical-interaction, and complex evidence are absent.

### Important genes

#### CTNNA2

- **Related proteins** (co-abundance neighbors): ANAPC5 (0.85), HYOU1 (0.85), TEX10 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin alpha 2. Enables actin filament binding activity. Involved in negative regulation of Arp2/3 complex-mediated actin nucleation; regulation of neuron migration; and regulation of neuron projection development. Located in cytoplasm. Implicated in complex cortical dysplasia with other brain malformations. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: complex cortical dysplasia with other brain malformations (0.720); refractive error (0.392); diabetes mellitus (0.356); hereditary breast ovarian cancer syndrome (0.340); lung adenocarcinoma (0.340)
- **Europe PMC papers**: 1454
- **Why important**: CTNNA2 has the strongest network position in the supplied subgraph and connects the stress-related HYOU1 signal with ANAPC5 and TEX10. Its HPA profile is enriched in brain-related tissues and several neuronal or glial cell types. Its annotated roles in actin binding, cell adhesion, neuron migration, and neurite development make it the clearest candidate for the neural or structural component of the module. It also has substantial literature and a documented association with complex cortical dysplasia.
- **Conclusion**: Established evidence supports CTNNA2 as a neuronal and cytoskeletal regulator and as a central co-abundance member. It is plausible, but unproven, that CTNNA2 helps anchor the shared module to autonomic neural or excitable-cell biology.

#### HYOU1

- **Related proteins** (co-abundance neighbors): CKMT1A; CKMT1B (0.85), CTNNA2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 links CTNNA2 with both CKMT1A gene entries in the co-abundance structure. It is a heat-shock-protein-family member associated with ER protein folding, secretion, hypoxia, ischemia, stress responses, and protection from apoptosis. Its broad tissue profile and enhancement in several specialized cell types make it a plausible state marker rather than a tissue-exclusive marker. It also has substantial literature and disease links involving neurodegeneration and coronary artery disorder.
- **Conclusion**: Established evidence supports HYOU1 as a stress-adaptive ER chaperone. Its participation in this module may indicate proteostatic or hypoxic stress shared by the sampled tissues, but the co-abundance data do not demonstrate that HYOU1 regulates the other module genes.

#### SLC25A13

- **Related proteins** (co-abundance neighbors): CKMT1A; CKMT1B (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 25 member 13. This gene is a member of the mitochondrial carrier family. The encoded protein contains four EF-hand Ca(2+) binding motifs in the N-terminal domain, and localizes to mitochondria. The protein catalyzes the exchange of aspartate for glutamate and a proton across the inner mitochondrial membrane, and is stimulated by calcium on the external side of the inner mitochondrial membrane. Mutations in this…
- **Diseases (Open Targets)**: neonatal intrahepatic cholestasis due to citrin deficiency (0.804); citrullinemia type II (0.756); citrin deficiency (0.652); citrullinemia (0.649); citrullinemia type I (0.464)
- **Europe PMC papers**: 1421
- **Why important**: SLC25A13 is the module's tissue-enriched mitochondrial carrier and is connected to the CKMT1A side of the network. It exchanges aspartate for glutamate and proton across the inner mitochondrial membrane and is stimulated by calcium. Its established role in mitochondrial transport, gluconeogenesis, ATP biosynthesis, and citrullinemia-related disease gives it strong mechanistic relevance to energy and metabolic regulation.
- **Conclusion**: Established evidence supports SLC25A13 as a mitochondrial metabolite transporter with major metabolic disease relevance. Its inclusion supports an energy-handling interpretation, but it does not establish that the module is a citrin-deficiency or liver-specific program.

#### CKMT1A

- **Related proteins** (co-abundance neighbors): none; STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: creatine kinase, mitochondrial 1A. Mitochondrial creatine (MtCK) kinase is responsible for the transfer of high energy phosphate from mitochondria to the cytosolic carrier, creatine. It belongs to the creatine kinase isoenzyme family. It exists as two isoenzymes, sarcomeric MtCK and ubiquitous MtCK, encoded by separate genes. Mitochondrial creatine kinase occurs in two different oligomeric forms: dimers and octamers, in contrast to…
- **Diseases (Open Targets)**: neurodegenerative disease (0.365); lung cancer (0.110); Abnormality of the skeletal system (0.106); type 2 diabetes mellitus (0.090); neoplasm (0.083)
- **Europe PMC papers**: 354
- **Why important**: CKMT1A is strongly informative functionally despite having no displayed co-abundance neighbors in the supplied subgraph. It encodes mitochondrial creatine kinase, which transfers high-energy phosphate between mitochondria and the cytosolic creatine system. Its enhancement in brain, esophagus, and intestine and its absence from immune cells argue against a simple blood-cell explanation. It provides a direct link to cellular energetic buffering and has documented disease and cancer literature.
- **Conclusion**: Established evidence supports CKMT1A as an energy-buffering mitochondrial enzyme. Its isolated network position means that its membership may reflect a broader metabolic state or tissue-composition signal rather than a direct interaction with the other module genes.

#### ANAPC5

- **Related proteins** (co-abundance neighbors): CTNNA2 (0.85), PTCD3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: anaphase promoting complex subunit 5. This gene encodes a tetratricopeptide repeat-containing component of the anaphase promoting complex/cyclosome (APC/C), a large E3 ubiquitin ligase that controls cell cycle progression by targeting a number of cell cycle regulators such as B-type cyclins for 26S proteasome-mediated degradation through ubiquitination. The encoded protein is required for the proper ubiquitination function of APC/C an…
- **Diseases (Open Targets)**: neurodegenerative disease (0.366); spondylolisthesis (0.211); schizophrenia (0.171); atrial flutter (0.047); atrial fibrillation (0.047)
- **Europe PMC papers**: 480
- **Why important**: ANAPC5 is one of the connections linking the CTNNA2 side of the subgraph to PTCD3. It is a component of the anaphase-promoting complex, an E3 ubiquitin ligase that controls cell-cycle transitions and protein turnover. Its broadly expressed, low-cell-specificity HPA profile is consistent with a general cellular function. Its disease associations include neurodegenerative disease and cardiac rhythm disorders, giving it relevance to both neural and circulatory contexts.
- **Conclusion**: Established evidence supports ANAPC5 as a general cell-cycle and ubiquitin-regulatory component. Its module membership may reflect shared proliferative, turnover, or cellular-maintenance demands, but there is no evidence that the module is an anaphase-promoting-complex module.

## Module 9

**Tissue pair**: autonomic_nervous_system and circulatory_system  
**Genes (10)**: BOLA2, HSPA8, IDI1, PKM, LDHA, LSM5, MEAK7, QPRT, PGK1, PNPO

### Function

The strongest interpretation is coordinated central carbon and cofactor metabolism. The globally corrected terms identify pyridine-containing compound metabolism and catabolism, together with organophosphate metabolism (GO:BP pyridine-containing compound metabolic process; q_global = 0.00436), (GO:BP pyridine-containing compound catabolic process; q_global = 0.00814), (GO:BP organophosphate metabolic process; q_global = 0.0228). The participating genes connect glycolysis through PGK1, PKM, and LDHA with NAD-related quinolinate metabolism through QPRT, vitamin B6 cofactor production through PNPO, and isoprenoid metabolism through IDI1. The module therefore appears to represent a metabolic state rather than a narrowly tissue-specific signaling pathway. Supplementary STRING enrichments independently point toward aerobic glycolysis and glycolysis or gluconeogenesis (STRING WikiPathways Aerobic glycolysis; within-query FDR = 0.0041), (STRING WikiPathways Glycolysis and gluconeogenesis; within-query FDR = 0.008), (STRING KEGG Glycolysis / Gluconeogenesis; within-query FDR = 0.0253), while the right-atrium and left-ventricle tissue signals (STRING TISSUES Right atrium; within-query FDR = 0.0185), (STRING TISSUES Left ventricle; within-query FDR = 0.0442) are compatible with metabolic activity in circulatory tissues but are not globally corrected evidence. HSPA8 and LSM5 may connect metabolic expression with protein quality control and RNA processing, respectively. The lack of enrichment for a specialized autonomic or circulatory biological process means that the shared module should not be interpreted as uniquely neuronal or cardiovascular without additional experimental evidence.

**Cell composition.** The module is not dominated by secreted or plasma proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity and low immune-cell specificity, indicating a substantial broadly expressed or housekeeping-like component. The HPA tissue-enhanced genes include liver-associated QPRT and PNPO and skeletal-muscle- or tongue-associated PKM, while the single-cell annotations are distributed across several epithelial, reproductive, neural, and other cell types rather than concentrated in one shared cell type. One gene, QPRT, is group-enriched in several monocyte and dendritic-cell categories, but the overall module has low blood-cell specificity. Thus, contamination by plasma proteins is unlikely, and a simple blood-cell explanation is not strongly supported; however, broad metabolic expression and variable cellular composition remain plausible explanations for the cross-tissue conservation.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP pyridine-containing compound metabolic process | 0.00436 | LDHA, PGK1, PKM, PNPO, QPRT |
| GO:BP pyridine-containing compound catabolic process | 0.00814 | LDHA, PGK1, PKM, QPRT |
| GO:BP organophosphate metabolic process | 0.0228 | HSPA8, IDI1, LDHA, PGK1, PKM, PNPO, QPRT |

### STRING and hu.MAP

STRING provides a compact, coherent glycolytic core: LDHA–PKM is very strongly supported, and PGK1 connects to both PKM and LDHA, with an additional HSPA8–PGK1 relationship. These known relationships support the glycolytic interpretation and indicate that part of the co-abundance structure recapitulates established protein or functional associations. The other module relationships are not represented by high-confidence STRING links in the supplied results, including the connections involving QPRT, PNPO, IDI1, MEAK7, LSM5, and BOLA2. hu.MAP contributes one complex containing PKM and PNPO (hu.MAP huMAP3_14442.1), but the module contributes only a small subset of that large complex and no hu.MAP support is reported for the remaining genes. Consequently, the network combines a known glycolytic interaction core with co-abundance links that may reflect shared regulation, indirect metabolic coupling, or tissue-composition effects rather than physical protein complexes.

**STRING interactions (score >= 0.7)**: 4 of 45 gene pairs: HSPA8–PGK1 (0.755); LDHA–PGK1 (0.923); LDHA–PKM (0.997); PGK1–PKM (0.936)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Ascites (FDR = 0.0016, 4 genes); WikiPathways Aerobic glycolysis (FDR = 0.0041, 3 genes); WikiPathways Glycolysis in senescence (FDR = 0.0041, 3 genes); WikiPathways Photodynamic therapy-induced HIF-1 survival signaling (FDR = 0.0045, 3 genes); WikiPathways Glycolysis and gluconeogenesis (FDR = 0.008, 3 genes); TISSUES Stomach (FDR = 0.0122, 4 genes); TISSUES Kidney (FDR = 0.0143, 6 genes); TISSUES Right atrium (FDR = 0.0185, 3 genes); Process Organophosphate metabolic process (FDR = 0.0196, 7 genes); KEGG Glycolysis / Gluconeogenesis (FDR = 0.0253, 3 genes); TISSUES Eye (FDR = 0.0288, 5 genes); TISSUES Lymphoblast (FDR = 0.0288, 4 genes); WikiPathways Clear cell renal cell carcinoma pathways (FDR = 0.0301, 3 genes); WikiPathways Metabolic reprogramming in colon cancer (FDR = 0.0301, 3 genes); TISSUES Left ventricle (FDR = 0.0442, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (PKM, PNPO; 2/57)

### Novelty

This module is not wholly novel at the level of molecular function because its glycolytic core is supported by established STRING relationships and its broad metabolic genes have known biochemical roles. The combination of glycolysis, pyridine-compound metabolism, quinolinate catabolism, vitamin B6 production, isoprenoid metabolism, RNA processing, and chaperone activity in one conserved cross-tissue co-abundance module may nevertheless be a new systems-level observation. The supplied evidence does not establish that the exact module has been previously reported, and absence of STRING or hu.MAP links for several edges cannot by itself demonstrate novelty. A defensible conclusion is that the module is a potentially novel cross-tissue co-abundance configuration built partly from well-known metabolic relationships, requiring comparison against published co-expression modules and independent cohorts before being called a new biological mechanism.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular metabolic-support program shared by cells sampled from autonomic nervous and circulatory tissues. Increased coordinated activity in glycolysis through PGK1, PKM, and LDHA may support ATP production and redox balancing, while QPRT could couple the state to quinolinate disposal and NAD biosynthetic capacity. PNPO could connect the state to vitamin B6 availability for neurotransmitter- and amino-acid-related reactions, and HSPA8 could help maintain proteostasis during metabolic demand. LSM5, IDI1, MEAK7, and BOLA2 may represent accompanying RNA-processing, isoprenoid, nutrient-response, and iron or redox-related programs. This is a hypothesis based on co-abundance and annotations, not proof that the proteins act in one physical pathway or that the module is driven by autonomic or circulatory physiology.

### Important genes

#### PGK1

- **Related proteins** (co-abundance neighbors): HSPA8 (0.87), PKM (0.85); STRING partners: HSPA8 (0.755), LDHA (0.923), PKM (0.936)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece, Principal piece, End piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglycerate kinase 1. The protein encoded by this gene is a glycolytic enzyme that catalyzes the conversion of 1,3-diphosphoglycerate to 3-phosphoglycerate. The encoded protein may also act as a cofactor for polymerase alpha. Additionally, this protein is secreted by tumor cells where it participates in angiogenesis by functioning to reduce disulfide bonds in the serine protease, plasmin, which consequently leads to th…
- **Diseases (Open Targets)**: glycogen storage disease due to phosphoglycerate kinase 1 deficiency (0.823); Menkes disease (0.578); X-linked distal spinal muscular atrophy type 3 (0.556); occipital horn syndrome (0.556); hereditary disease (0.520)
- **Europe PMC papers**: 14784
- **Why important**: PGK1 is a central connector of the established glycolytic core, linking HSPA8 with PKM in the co-abundance graph and showing high-confidence STRING relationships with HSPA8, LDHA, and PKM. It participates in all globally corrected metabolic terms (GO:BP pyridine-containing compound metabolic process; q_global = 0.00436), (GO:BP pyridine-containing compound catabolic process; q_global = 0.00814), (GO:BP organophosphate metabolic process; q_global = 0.0228) and in the supplementary glycolysis signals (STRING TISSUES Ascites; within-query FDR = 0.0016) through (STRING TISSUES Left ventricle; within-query FDR = 0.0442). Its annotated phosphoglycerate-kinase activity gives the module a direct biochemical anchor, while its disease associations include PGK1 deficiency and related hereditary disorders. Its substantial literature volume also makes it one of the best-characterized genes in the module.
- **Conclusion**: Established evidence supports PGK1 as a core glycolytic and organophosphate-metabolism component of the module. It is reasonable to hypothesize that PGK1 helps organize the module's metabolic signal, but the co-abundance data do not establish a special autonomic or circulatory role.

#### LDHA

- **Related proteins** (co-abundance neighbors): LSM5 (0.86); STRING partners: PGK1 (0.923), PKM (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lactate dehydrogenase A. This gene encodes the A subunit of lactate dehydrogenase enzyme which catalyzes the reversible conversion of pyruvate to lactate with the concomitant oxidation of NADH to NAD in anaerobic glycolysis. The protein is found predominantly in skeletal muscle and belongs to the lactate dehydrogenase family. Mutations in this gene have been linked to exertional myoglobinuria. The human genome contains se…
- **Diseases (Open Targets)**: glycogen storage disease due to lactate dehydrogenase M-subunit deficiency (0.755); disorder of glycogen metabolism (0.505); glycogen storage disease XV (0.505); primary hyperoxaluria (0.447); hereditary disease (0.190)
- **Europe PMC papers**: 20747
- **Why important**: LDHA is part of every globally corrected term (GO:BP pyridine-containing compound metabolic process; q_global = 0.00436), (GO:BP pyridine-containing compound catabolic process; q_global = 0.00814), (GO:BP organophosphate metabolic process; q_global = 0.0228) and is embedded in the strongest STRING relationships, especially with PKM and PGK1. Its known function in the reversible conversion of pyruvate and lactate directly supports glycolytic flux and redox handling. It also has tissue relevance to skeletal muscle and disease associations involving lactate dehydrogenase deficiency and glycogen metabolism. LDHA has the largest literature volume among the module genes, strengthening confidence in its annotation while also making its presence less indicative of a novel mechanism.
- **Conclusion**: Established evidence identifies LDHA as a core glycolytic marker and likely contributor to the metabolic interpretation. A role in coordinating lactate or redox adaptation across the two tissue groups is plausible, but it remains a hypothesis rather than a demonstrated module-specific function.

#### PKM

- **Related proteins** (co-abundance neighbors): PGK1 (0.85); STRING partners: LDHA (0.997), PGK1 (0.936)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: pyruvate kinase M1/2. This gene encodes a protein involved in glycolysis. The encoded protein is a pyruvate kinase that catalyzes the transfer of a phosphoryl group from phosphoenolpyruvate to ADP, generating ATP and pyruvate. This protein has been shown to interact with thyroid hormone and may mediate cellular metabolic effects induced by thyroid hormones. This protein has been found to bind Opa protein, a bacterial o…
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); autoimmune disorder of central nervous system (0.370); tympanic membrane perforation (0.204); neoplasm (0.121); hepatocellular carcinoma (0.120)
- **Europe PMC papers**: 8544
- **Why important**: PKM participates in all globally corrected terms (GO:BP pyridine-containing compound metabolic process; q_global = 0.00436), (GO:BP pyridine-containing compound catabolic process; q_global = 0.00814), (GO:BP organophosphate metabolic process; q_global = 0.0228) and forms the central established glycolytic interaction cluster with LDHA and PGK1. It catalyzes ATP- and pyruvate-generating glycolytic chemistry, is tissue-enhanced in skeletal muscle and tongue, and is the only module gene represented in the supplied hu.MAP complex together with PNPO (hu.MAP huMAP3_14442.1). Its disease and cancer associations, together with a substantial literature base, make it an important bridge between core metabolism and possible cellular-state regulation.
- **Conclusion**: Established evidence supports PKM as a core enzymatic component of the module and a likely driver of its glycolytic signature. Any claim that PKM specifically links autonomic and circulatory physiology would require perturbation or tissue-resolved validation.

#### QPRT

- **Related proteins** (co-abundance neighbors): MEAK7 (0.85), HSPA8 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: quinolinate phosphoribosyltransferase. This gene encodes a key enzyme in catabolism of quinolinate, an intermediate in the tryptophan-nicotinamide adenine dinucleotide pathway. Quinolinate acts as a most potent endogenous exitotoxin to neurons. Elevation of quinolinate levels in the brain has been linked to the pathogenesis of neurodegenerative disorders such as epilepsy, Alzheimer's disease, and Huntington's disease. Alternative splic…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); breast cancer (0.096); Genetic central nervous system malformation (0.065); breast carcinoma (0.057); schizencephaly (0.053)
- **Europe PMC papers**: 1191
- **Why important**: QPRT participates in all globally corrected terms (GO:BP pyridine-containing compound metabolic process; q_global = 0.00436), (GO:BP pyridine-containing compound catabolic process; q_global = 0.00814), (GO:BP organophosphate metabolic process; q_global = 0.0228) and links in the module graph to HSPA8 and MEAK7. Its annotated role in quinolinate catabolism and de novo NAD biosynthesis adds a distinct cofactor and neuroactive-metabolite dimension beyond glycolysis. HPA identifies liver tissue enhancement and group enrichment in several monocyte and dendritic-cell categories, while its disease associations include neurodegenerative disease. Its literature volume is lower than that of the principal glycolytic genes, making it especially informative for assessing whether the module contains a meaningful non-glycolytic component.
- **Conclusion**: Established evidence supports QPRT as the module's clearest link to quinolinate disposal and NAD-related metabolism. It is plausible that QPRT contributes to metabolic resilience in cells shared between the tissue groups, but the data do not show whether its signal reflects regulation, cell composition, or causal metabolic coupling.

#### PNPO

- **Related proteins** (co-abundance neighbors): LSM5 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: pyridoxamine 5'-phosphate oxidase. The enzyme encoded by this gene catalyzes the terminal, rate-limiting step in the synthesis of pyridoxal 5'-phosphate, also known as vitamin B6. Vitamin B6 is a required co-factor for enzymes involved in both homocysteine metabolism and synthesis of neurotransmitters such as catecholamine. Mutations in this gene result in pyridoxamine 5'-phosphate oxidase (PNPO) deficiency, a form of neonatal epil…
- **Diseases (Open Targets)**: pyridoxal phosphate-responsive seizures (0.806); hereditary disease (0.485); Seizure (0.401); neuronopathy, distal hereditary motor, type 5A (0.340); fetal growth restriction (0.333)
- **Europe PMC papers**: 20173
- **Why important**: PNPO contributes to pyridine-containing compound metabolism and organophosphate metabolism (GO:BP pyridine-containing compound metabolic process; q_global = 0.00436), (GO:BP organophosphate metabolic process; q_global = 0.0228), and is included with PKM in the hu.MAP complex (hu.MAP huMAP3_14442.1). Its established enzymatic role is production of pyridoxal phosphate, a cofactor required for enzymes involved in homocysteine metabolism and neurotransmitter synthesis. HPA reports liver tissue enhancement and cell-type enhancement in ependymal and tuft cells, and its disease associations include pyridoxal-phosphate-responsive seizures and PNPO deficiency. The gene therefore provides a biologically relevant bridge between metabolism and nervous-system chemistry, despite limited STRING support.
- **Conclusion**: Established evidence supports PNPO as a vitamin B6 cofactor-metabolism component with potential relevance to neuronal chemistry. Its placement in this module may indicate coordinated cofactor supply, but the hu.MAP association and co-abundance edge do not prove a functional complex or a direct autonomic mechanism.

#### HSPA8

- **Related proteins** (co-abundance neighbors): PGK1 (0.87), LSM5 (0.82), QPRT (0.80); STRING partners: PGK1 (0.755)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Flagellar centriole, Annulus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 8. This gene encodes a member of the heat shock protein 70 family, which contains both heat-inducible and constitutively expressed members. This protein belongs to the latter group, which are also referred to as heat-shock cognate proteins. It functions as a chaperone, and binds to nascent polypeptides to facilitate correct folding. It also functions as an ATPase in the disassembly of clathrin-coated…
- **Diseases (Open Targets)**: dengue disease (0.505); systemic lupus erythematosus (0.375); smoking initiation (0.199); Lennox-Gastaut syndrome (0.118); neoplasm (0.105)
- **Europe PMC papers**: 6937
- **Why important**: HSPA8 connects to PGK1, LSM5, and QPRT in the module and has a high-confidence STRING relationship with PGK1. It contributes to the globally corrected organophosphate-metabolism term (GO:BP organophosphate metabolic process; q_global = 0.0228) and appears in multiple supplementary tissue and process enrichments (STRING TISSUES Ascites; within-query FDR = 0.0016), (STRING TISSUES Stomach; within-query FDR = 0.0122) through (STRING Process Organophosphate metabolic process; within-query FDR = 0.0196), (STRING TISSUES Eye; within-query FDR = 0.0288), (STRING TISSUES Lymphoblast; within-query FDR = 0.0288), (STRING TISSUES Left ventricle; within-query FDR = 0.0442). Its established functions in constitutive chaperoning, protein folding, unfolded-protein responses, and vesicle disassembly provide a plausible proteostasis context for a metabolically active module. It also has a large literature base and disease associations involving immune and neurological conditions.
- **Conclusion**: Established evidence supports HSPA8 as a proteostasis and trafficking component coupled to the metabolic core, especially through PGK1. It is reasonable to hypothesize that HSPA8 buffers protein stress during metabolic demand, but the module does not establish that this chaperone function is causally responsible for the cross-tissue pattern.
