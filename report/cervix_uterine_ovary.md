# Conserved co-abundance modules: cervix_uterine and ovary

## Module 0

**Tissue pair**: cervix_uterine and ovary  
**Genes (13)**: SLC3A2, ADAM10, AGPS, MTHFD1L, GFM1, GNS, NCSTN, ALDH18A1, LPCAT1, NUP210, RAB24, RRBP1, MRPS22

### Function

No GO or KEGG term passed global correction, so the module does not support a formally established enriched pathway. Its gene-level evidence instead points to coordinated intracellular maintenance involving the endoplasmic reticulum and secretory machinery through RRBP1, membrane and amino-acid transport through SLC3A2, phospholipid and ether-lipid biology through LPCAT1 and AGPS, mitochondrial folate metabolism through MTHFD1L, mitochondrial translation through GFM1 and MRPS22, lysosomal glycosaminoglycan breakdown through GNS, and membrane-protein processing through ADAM10 and NCSTN. The network is therefore best interpreted as a mixed organelle, membrane-trafficking, metabolic, and protein-maintenance module rather than as a single demonstrated pathway. The strongest mechanistic anchors are the RRBP1-centered neighborhood, the MTHFD1L connections to mitochondrial genes, and the known ADAM10–NCSTN and GFM1–MRPS22 relationships.

**Cell composition.** The module is not dominated by plasma or classically secreted proteins; the HPA summary identifies only a small secreted subset, while GNS is intracellular and membrane-associated. Most genes have low tissue specificity, and all module genes are cell-type enhanced in the HPA summary. Several annotations point to syncytiotrophoblasts, neutrophils, monocytes, progenitors, epithelial or acinar cells, and other specialized cell types, but most genes have low immune-cell specificity. This argues against interpreting the module as a purely cervix or ovary intrinsic program. Because protein detection is broader in cervix than ovary and because the module contains broadly expressed housekeeping-like organelle and translation genes, shared cell composition, vascular or stromal content, trophoblast-like biology, or technical abundance effects remain plausible contributors. The module is not convincingly a blood-cell module, although immune-associated HPA signals warrant sensitivity analyses for blood and infiltrating-cell composition.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides two high-confidence known relationships within the module: ADAM10 with NCSTN, supporting membrane-protein processing and gamma-secretase-related biology, and GFM1 with MRPS22, supporting mitochondrial translation. The absence of STRING functional enrichment means that STRING does not provide an additional supported functional label; it does not invalidate the co-abundance module. hu.MAP supplies two overlapping mitochondrial or metabolic complex contexts, (hu.MAP huMAP3_10525.1) and (hu.MAP huMAP3_13468.1). Both complexes contain ALDH18A1, MTHFD1L, and GFM1, linking mitochondrial folate-related metabolism, amino-acid or nitrogen metabolism, and mitochondrial translation within larger assemblies. However, the module contains only a small subset of each large complex, so hu.MAP supports shared organelle context rather than membership in a complete, module-specific complex. Overall, some edges are already known molecular relationships, while many co-abundance edges lack direct STRING or hu.MAP support and may reflect coordinated expression, shared cell types, or indirect biology.

**STRING interactions (score >= 0.7)**: 2 of 78 gene pairs: ADAM10–NCSTN (0.865); GFM1–MRPS22 (0.978)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10525.1 (ALDH18A1, MTHFD1L, GFM1; 3/33); huMAP3_13468.1 (ALDH18A1, MTHFD1L, GFM1; 3/99)

### Novelty

This cannot be called a newly discovered molecular pathway on the present evidence. The ADAM10–NCSTN and GFM1–MRPS22 relationships are already known, and the repeated ALDH18A1–MTHFD1L–GFM1 membership in (hu.MAP huMAP3_10525.1) and (hu.MAP huMAP3_13468.1) places part of the module in previously catalogued mitochondrial and metabolic complex contexts. At the same time, the particular cross-organelle co-abundance arrangement shared by cervix and ovary may be a novel observation, because many module edges are not represented by the supplied STRING or hu.MAP evidence. That absence alone does not establish novelty: it may reflect incomplete interaction databases, indirect regulation, tissue composition, or correlated abundance without physical interaction. A defensible novelty claim would require replication in independent cervix and ovary cohorts, adjustment for cell composition and tissue quality, comparison with published tissue co-abundance modules, and experimental testing of the proposed cross-organelle coordination.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular state in which secretory and membrane-rich cells coordinate ER organization, amino-acid and lipid handling, mitochondrial one-carbon and translation capacity, lysosomal turnover, and regulated membrane-protein processing. RRBP1 may mark the ER and secretory-trafficking axis; SLC3A2, LPCAT1, and AGPS may connect nutrient transport with membrane-lipid production; MTHFD1L, GFM1, and MRPS22 may reflect mitochondrial biosynthetic and translational support; and ADAM10 with NCSTN may represent membrane-protein processing. This model predicts correlated organelle stress, secretory activity, membrane remodeling, and mitochondrial function in the same contributing cells. It remains a hypothesis because global GO or KEGG enrichment was absent, most network edges are not established physical interactions, and HPA indicates mixed cellular contexts.

### Important genes

#### RRBP1

- **Related proteins** (co-abundance neighbors): RAB24 (0.91), ADAM10 (0.86), LPCAT1 (0.85), NCSTN (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosome binding protein 1. This gene encodes a ribosome-binding protein of the endoplasmic reticulum (ER) membrane. Studies suggest that this gene plays a role in ER proliferation, secretory pathways and secretory cell differentiation, and mediation of ER-microtubule interactions. Alternative splicing has been observed and protein isoforms are characterized by regions of N-terminal decapeptide and C-terminal heptad repeats.…
- **Diseases (Open Targets)**: cancer (0.476); dengue disease (0.462); neurodegenerative disease (0.324); coronary artery disorder (0.292); placental abruption (0.279)
- **Europe PMC papers**: 1654
- **Why important**: RRBP1 has the most central network position in the module and connects RAB24, ADAM10, LPCAT1, and NCSTN. Its ER localization and documented roles in ER proliferation, secretory pathways, secretory-cell differentiation, and ER–microtubule interactions make it a plausible organizational anchor. It is detected in both tissues, has substantial literature support, and has disease links including cancer, dengue disease, neurodegenerative disease, coronary artery disorder, and placental abruption.
- **Conclusion**: Established: RRBP1 is an ER membrane ribosome-binding protein with functions in ER and secretory organization, and it is the most connected module gene. Hypothesis: RRBP1 may coordinate the membrane-trafficking side of this shared module and couple it to mitochondrial and lipid-related programs indirectly.

#### MTHFD1L

- **Related proteins** (co-abundance neighbors): SLC3A2 (0.84), LPCAT1 (0.82), GFM1 (0.82), MRPS22 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_10525.1, huMAP3_13468.1
- **Function (MyGene.info)**: methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 1 like. The protein encoded by this gene is involved in the synthesis of tetrahydrofolate (THF) in the mitochondrion. THF is important in the de novo synthesis of purines and thymidylate and in the regeneration of methionine from homocysteine. Several transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Jun 2011].
- **Diseases (Open Targets)**: Alzheimer disease (0.343); Abnormality of refraction (0.315); refractive error (0.312); COVID-19 (0.296); severe acute respiratory syndrome (0.295)
- **Europe PMC papers**: 1180
- **Why important**: MTHFD1L is among the most connected genes and links SLC3A2, LPCAT1, GFM1, and MRPS22. It is mitochondrial and participates in tetrahydrofolate interconversion and formate-related biosynthesis. Its inclusion in both hu.MAP contexts, (hu.MAP huMAP3_10525.1) and (hu.MAP huMAP3_13468.1), gives it the strongest complex-level bridge between the module and broader mitochondrial metabolic assemblies. It is detected in both tissues and has literature concerning mitochondrial folate metabolism and disease associations including Alzheimer disease and refractive abnormalities.
- **Conclusion**: Established: MTHFD1L is a mitochondrial folate-pathway enzyme and a recurrent member of both supplied hu.MAP contexts. Hypothesis: it may connect mitochondrial one-carbon metabolism with the membrane, transport, and translation signals represented elsewhere in the module.

#### SLC3A2

- **Related proteins** (co-abundance neighbors): MTHFD1L (0.84), AGPS (0.84), NUP210 (0.82), ALDH18A1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 3 member 2. This gene is a member of the solute carrier family and encodes a cell surface, transmembrane protein. The protein exists as the heavy chain of a heterodimer, covalently bound through di-sulfide bonds to one of several possible light chains. The encoded transporter plays a role in regulation of intracellular calcium levels and transports L-type amino acids. Alternatively spliced transcript variants…
- **Diseases (Open Targets)**: sensorineural hearing loss disorder (0.370); neurodegenerative disease (0.324); neoplasm (0.117); breast cancer (0.113); breast carcinoma (0.110)
- **Europe PMC papers**: 6815
- **Why important**: SLC3A2 is one of the most connected genes and links MTHFD1L, AGPS, NUP210, and ALDH18A1. Its plasma-membrane and nucleoplasmic localization, amino-acid transport function, and role in intracellular calcium regulation provide a plausible interface between nutrient availability, membrane biology, and organelle demand. It is broadly expressed, detected in cervix, and has extensive literature support with disease associations including sensorineural hearing loss, neurodegenerative disease, and breast cancer.
- **Conclusion**: Established: SLC3A2 is a cell-surface transporter component involved in amino-acid transport and calcium regulation. Hypothesis: it may help translate extracellular nutrient or stress conditions into the intracellular metabolic and membrane state captured by the module.

#### GFM1

- **Related proteins** (co-abundance neighbors): MTHFD1L (0.82); STRING partners: MRPS22 (0.978)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_10525.1, huMAP3_13468.1
- **Function (MyGene.info)**: G elongation factor mitochondrial 1. Eukaryotes contain two protein translational systems, one in the cytoplasm and one in the mitochondria. Mitochondrial translation is crucial for maintaining mitochondrial function and mutations in this system lead to a breakdown in the respiratory chain-oxidative phosphorylation system and to impaired maintenance of mitochondrial DNA. This gene encodes one of the mitochondrial translation elongati…
- **Diseases (Open Targets)**: hepatoencephalopathy due to combined oxidative phosphorylation defect type 1 (0.822); neurodegenerative disease (0.463); combined oxidative phosphorylation deficiency (0.451); hereditary disease (0.341); Leigh syndrome (0.313)
- **Europe PMC papers**: 1380
- **Why important**: GFM1 connects MTHFD1L in the network, belongs to both hu.MAP contexts (hu.MAP huMAP3_10525.1) and (hu.MAP huMAP3_13468.1), and has a high-confidence STRING relationship with MRPS22. Its mitochondrial localization and role in translational elongation make it a direct marker of mitochondrial protein-synthesis capacity. It is detected in both tissues and has established disease associations with combined oxidative-phosphorylation defects, hepatoencephalopathy, Leigh syndrome, and neurodegenerative disease.
- **Conclusion**: Established: GFM1 is a mitochondrial translation elongation factor supported by both STRING and hu.MAP evidence in this module. Hypothesis: GFM1 may report or contribute to the mitochondrial functional state that permits the module’s broader biosynthetic and membrane activities.

#### ADAM10

- **Related proteins** (co-abundance neighbors): RRBP1 (0.86); STRING partners: NCSTN (0.865)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ADAM metallopeptidase domain 10. Members of the ADAM family are cell surface proteins with a unique structure possessing both potential adhesion and protease domains. This gene encodes and ADAM family member that cleaves many proteins including TNF-alpha and E-cadherin. Alternate splicing results in multiple transcript variants encoding different proteins that may undergo similar processing. [provided by RefSeq, Feb 2016].
- **Diseases (Open Targets)**: reticulate acropigmentation of Kitamura (0.679); Alzheimer disease 18 (0.621); Alzheimer disease (0.522); dementia (0.415); schizophrenia (0.354)
- **Europe PMC papers**: 11139
- **Why important**: ADAM10 is connected to RRBP1 and forms the supplied high-confidence STRING pair with NCSTN. It is a plasma-membrane and vesicular metalloprotease that cleaves ectodomains, including TNF-alpha and E-cadherin, and is associated with Notch processing and regulation of cell adhesion. It has extensive literature support and disease associations spanning reticulate acropigmentation, Alzheimer disease, dementia, and schizophrenia.
- **Conclusion**: Established: ADAM10 is a membrane ectodomain protease with a known relationship to NCSTN and established roles in proteolysis, adhesion, and Notch-related biology. Hypothesis: its co-abundance with RRBP1 and NCSTN may indicate coordinated membrane-protein turnover or cell-contact remodeling in the shared tissue context, but the module does not establish a causal ADAM10 pathway.

## Module 1

**Tissue pair**: cervix_uterine and ovary  
**Genes (15)**: SLC1A5, ACSL3, ATP1A1, CANX, CPT1A, EMC1, LACTB, IGF2R, OPA1, PLXNB2, PNPT1, SEC63, TIMM50, TMEM214, TOR1AIP2

### Function

The module is most consistent with a conserved organelle-membrane program centered on the endoplasmic reticulum, mitochondria, and associated membrane systems. The primary enrichment is organelle membrane (GO:CC organelle membrane; q_global = 0.0359), with nearly the whole module represented in that term. The STRING annotations independently support membrane, integral membrane, organelle-membrane, and ER-membrane localization (7 supplementary STRING terms; within-query FDR 5.04e-09–0.0131). Functionally, the genes connect ER protein insertion and folding through SEC63, CANX, EMC1, and TMEM214; lipid activation and mitochondrial fatty-acid entry through ACSL3 and CPT1A; mitochondrial organization and import through OPA1, TIMM50, and PNPT1; and membrane transport or surface signaling through ATP1A1, SLC1A5, IGF2R, and PLXNB2. The liver-development and hepaticobiliary-development terms (GO:BP liver development; q_global = 0.0441) and (GO:BP hepaticobiliary system development; q_global = 0.0441) are globally corrected but should be interpreted cautiously: they are driven by CPT1A, IGF2R, PNPT1, and SEC63 and may reflect shared organelle, trafficking, and metabolic biology rather than a liver-specific process. No within-module term passed its stated within-module correction, so the strongest interpretation is a membrane and organelle-coordination module rather than a narrowly defined developmental pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and the proteins are detected in cervix_uterine and/or ovary where data are available, which supports a broadly expressed cellular program rather than a tissue-exclusive signature. HPA also reports mostly low immune-cell specificity, although selected genes show enrichment in neutrophils, monocytes, dendritic-cell populations, trophoblasts, and other specialized cell types. Thus, the module does not strongly indicate blood contamination or a dominant blood-cell program, but variable immune, trophoblast, or other cell-type composition could contribute to its co-abundance in particular samples. The absence of secreted proteins argues against a circulating-plasma explanation.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC organelle membrane | 0.0359 | ACSL3, ATP1A1, CANX, CPT1A, EMC1, IGF2R, OPA1, PNPT1, SEC63, TIMM50, TMEM214, TOR1AIP2 |
| GO:BP liver development | 0.0441 | CPT1A, IGF2R, PNPT1, SEC63 |
| GO:BP hepaticobiliary system development | 0.0441 | CPT1A, IGF2R, PNPT1, SEC63 |

### STRING and hu.MAP

STRING provides direct, high-confidence support for an ACSL3–CPT1A lipid-metabolism relationship, a CANX–EMC1 ER-membrane relationship, a CANX–SEC63 ER protein-handling relationship, and a SEC63–TMEM214 relationship. The broader STRING annotations reinforce membrane and ER-membrane organization (7 supplementary STRING terms; within-query FDR 5.04e-09–0.0131), but many module genes have no listed high-confidence STRING partner within the module. hu.MAP gives partial support for three kinds of known complex context: ATP1A1 with SLC1A5 in (hu.MAP huMAP3_10473.1), PLXNB2 with IGF2R in (hu.MAP huMAP3_06775.1), and ACSL3 with CPT1A in (hu.MAP huMAP3_09592.1). Because each hu.MAP complex contains many additional proteins and only a small subset of its members is present here, these results support biological coherence without showing that the entire co-abundance module is one established physical complex. Overall, the network combines known molecular relationships with co-abundance links that are not all represented by curated physical interactions.

**STRING interactions (score >= 0.7)**: 4 of 105 gene pairs: ACSL3–CPT1A (0.955); CANX–EMC1 (0.854); CANX–SEC63 (0.713); SEC63–TMEM214 (0.723)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transmembrane helix (FDR = 5.04e-09, 13 genes); Component Integral component of membrane (FDR = 1.86e-06, 13 genes); Keyword Membrane (FDR = 3.99e-05, 14 genes); Component Organelle membrane (FDR = 0.0058, 12 genes); Component Integral component of plasma membrane (FDR = 0.0083, 5 genes); Component Organelle subcompartment (FDR = 0.0083, 8 genes); Component Endoplasmic reticulum membrane (FDR = 0.0131, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10473.1 (ATP1A1, SLC1A5; 2/24); huMAP3_06775.1 (PLXNB2, IGF2R; 2/60); huMAP3_09592.1 (ACSL3, CPT1A; 2/95)

### Novelty

The module should not be described as a wholly new molecular pathway. Several of its relationships and functional contexts are already established by STRING and hu.MAP, especially the ACSL3–CPT1A lipid connection, ER protein-handling relationships involving CANX and SEC63, and the partial complexes in (hu.MAP huMAP3_10473.1) (hu.MAP huMAP3_06775.1) (hu.MAP huMAP3_09592.1). Nevertheless, the specific conserved co-abundance pattern shared by cervix_uterine and ovary may represent a new systems-level observation, because the module brings ER, mitochondrial, lipid, transport, and trafficking genes together across these tissues. That claim requires comparison with published tissue co-expression studies and independent cohorts. The absence of a complete match in STRING or hu.MAP would not by itself establish novelty, since those resources catalog physical interactions and complexes rather than every tissue-specific co-abundance relationship.

**Hypothesis.** Hypothesis: this conserved module reflects coordinated maintenance of membrane and organelle homeostasis in shared cellular populations of cervix_uterine and ovary. In this model, ER insertion and quality control through EMC1, CANX, SEC63, and TMEM214 are coupled to lipid supply and mitochondrial fatty-acid utilization through ACSL3 and CPT1A, while OPA1, TIMM50, and PNPT1 support mitochondrial structure, protein import, and RNA handling. ATP1A1, SLC1A5, IGF2R, and PLXNB2 could connect this intracellular program to ion balance, nutrient uptake, lysosomal trafficking, and cell-surface signaling. The developmental terms (GO:BP liver development; q_global = 0.0441) and (GO:BP hepaticobiliary system development; q_global = 0.0441) may therefore reflect a shared metabolic and trafficking state rather than direct activation of a liver-development program. This hypothesis should be tested with cell-type-resolved data, protein measurements, and perturbation of ER–mitochondrial or lipid-metabolism components.

### Important genes

#### EMC1

- **Related proteins** (co-abundance neighbors): CPT1A (0.84), ACSL3 (0.84), PLXNB2 (0.83), LACTB (0.83), PNPT1 (0.83); STRING partners: CANX (0.854)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ER membrane protein complex subunit 1. This gene encodes a single-pass type I transmembrane protein, which is a subunit of the endoplasmic reticulum membrane protein complex (EMC). Multiple alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2012].
- **Diseases (Open Targets)**: cerebellar atrophy, visual impairment, and psychomotor retardation; (0.769); hereditary disease (0.497); inherited retinal dystrophy (0.487); Global developmental delay (0.411); Cerebellar atrophy (0.410)
- **Europe PMC papers**: 416
- **Why important**: EMC1 is the most central node by the supplied network ranking and connects ACSL3, CPT1A, PLXNB2, LACTB, and PNPT1. It is an ER membrane protein-complex subunit involved in membrane-protein insertion and tail-anchored protein insertion. It belongs to the primary organelle-membrane evidence (GO:CC organelle membrane; q_global = 0.0359) and to the STRING membrane and ER categories (7 supplementary STRING terms; within-query FDR 5.04e-09–0.0131), while CANX–EMC1 is a known STRING relationship. Its disease associations include cerebellar atrophy, visual impairment, psychomotor retardation, and inherited retinal dystrophy, and it has an established literature base.
- **Conclusion**: Established: EMC1 is a strong structural anchor for the ER-membrane interpretation and links membrane biogenesis with mitochondrial and lipid-related module members. Hypothesis: its central co-abundance position may indicate that ER membrane-protein insertion is a coordinating constraint that helps synchronize the rest of the module in both tissues.

#### ACSL3

- **Related proteins** (co-abundance neighbors): TMEM214 (0.90), SLC1A5 (0.85), EMC1 (0.84), IGF2R (0.82); STRING partners: CPT1A (0.955)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 3. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme is highly expressed…
- **Diseases (Open Targets)**: prostate adenocarcinoma (0.370); acute myeloid leukemia (0.313); neurodegenerative disease (0.300); ovarian dysfunction (0.253); Abnormality of the skeletal system (0.215)
- **Europe PMC papers**: 2930
- **Why important**: ACSL3 has a highly connected position and links TMEM214, SLC1A5, EMC1, and IGF2R. It activates long-chain fatty acids as fatty acyl-CoA esters and is annotated in long-chain fatty-acid metabolism, lipid biosynthesis, fatty-acid degradation, and very-low-density-lipoprotein assembly. It participates in (GO:CC organelle membrane; q_global = 0.0359) and (7 supplementary STRING terms; within-query FDR 5.04e-09–0.0131), has the direct STRING relationship with CPT1A, and is present in hu.MAP complex context (hu.MAP huMAP3_09592.1). Its disease associations include prostate adenocarcinoma, acute myeloid leukemia, neurodegenerative disease, and ovarian dysfunction, with substantial literature support.
- **Conclusion**: Established: ACSL3 provides a direct biochemical bridge between membrane lipid handling and mitochondrial fatty-acid use. Hypothesis: ACSL3 may help couple ER membrane remodeling to CPT1A-dependent substrate delivery in the shared tissue state.

#### CPT1A

- **Related proteins** (co-abundance neighbors): EMC1 (0.84), SEC63 (0.84), CANX (0.82); STRING partners: ACSL3 (0.955)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: carnitine palmitoyltransferase 1A. The mitochondrial oxidation of long-chain fatty acids is initiated by the sequential action of carnitine palmitoyltransferase I (which is located in the outer membrane and is detergent-labile) and carnitine palmitoyltransferase II (which is located in the inner membrane and is detergent-stable), together with a carnitine-acylcarnitine translocase. CPT I is the key enzyme in the carnitine-dependent…
- **Diseases (Open Targets)**: carnitine palmitoyl transferase 1A deficiency (0.833); hereditary disease (0.489); hypertensive disorder (0.350); response to xenobiotic stimulus (0.350); aortic stenosis (0.215)
- **Europe PMC papers**: 11255
- **Why important**: CPT1A is connected to EMC1, SEC63, and CANX and has the direct STRING relationship with ACSL3. It controls the entry step for long-chain fatty acids into mitochondrial oxidation and is annotated in fatty-acid metabolism, beta-oxidation, glucose homeostasis, and hypoxia response. It is the only selected gene represented in all three primary evidence groups (GO:CC organelle membrane; q_global = 0.0359), (GO:BP liver development; q_global = 0.0441), and (GO:BP hepaticobiliary system development; q_global = 0.0441), and it appears in hu.MAP lipid and membrane complex context (hu.MAP huMAP3_09592.1). Its carnitine palmitoyltransferase deficiency association and extensive literature make it a strong metabolic anchor.
- **Conclusion**: Established: CPT1A supports a mitochondrial energy and lipid-oxidation interpretation of the module. Hypothesis: coordinated CPT1A and ACSL3 abundance may indicate coupling between fatty-acid activation and mitochondrial utilization rather than a generic membrane signal.

#### CANX

- **Related proteins** (co-abundance neighbors): ATP1A1 (0.90), SEC63 (0.84), CPT1A (0.82); STRING partners: EMC1 (0.854), SEC63 (0.713)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX occupies a central network position and connects ATP1A1, SEC63, and CPT1A. It is an ER calcium-binding molecular chaperone that supports folding and assembly of newly synthesized glycoproteins and ER quality control. It is present in (GO:CC organelle membrane; q_global = 0.0359) and all of the membrane and ER STRING categories (7 supplementary STRING terms; within-query FDR 5.04e-09–0.0131), with known STRING relationships to EMC1 and SEC63. Its disease and infection-related associations include neurodegenerative disease and several viral diseases, and it has a substantial literature base.
- **Conclusion**: Established: CANX provides direct evidence for ER protein-folding and quality-control activity within the module. Hypothesis: CANX may couple ER proteostasis to membrane transport and mitochondrial metabolic demand through its links with ATP1A1 and CPT1A.

#### SEC63

- **Related proteins** (co-abundance neighbors): CPT1A (0.84), CANX (0.84); STRING partners: CANX (0.713), TMEM214 (0.723)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC63 protein translocation regulator. The Sec61 complex is the central component of the protein translocation apparatus of the endoplasmic reticulum (ER) membrane. The protein encoded by this gene and SEC62 protein are found to be associated with ribosome-free SEC61 complex. It is speculated that Sec61-Sec62-Sec63 may perform post-translational protein translocation into the ER. The Sec61-Sec62-Sec63 complex might also perform the bac…
- **Diseases (Open Targets)**: autosomal dominant polycystic liver disease (0.795); neurodegenerative disease (0.526); polycystic liver disease 1 (0.430); Biliary tract abnormality (0.346); placental abruption (0.232)
- **Europe PMC papers**: 1756
- **Why important**: SEC63 connects CPT1A and CANX and also links to TMEM214 through STRING. It is part of the ER translocation machinery associated with SEC61 and SEC62, supporting protein targeting and translocation into the ER. It is represented in (GO:CC organelle membrane; q_global = 0.0359), (GO:BP liver development; q_global = 0.0441), and (GO:BP hepaticobiliary system development; q_global = 0.0441) and in the membrane and ER STRING categories (7 supplementary STRING terms; within-query FDR 5.04e-09–0.0131). Its disease associations include autosomal dominant polycystic liver disease and biliary tract abnormality, and it has substantial literature support.
- **Conclusion**: Established: SEC63 is a mechanistically plausible ER-translocation component and helps explain the module's strong organelle-membrane signal. Hypothesis: its co-abundance with CPT1A may reflect coordinated expansion or maintenance of ER protein-handling capacity during metabolically active states.

## Module 2

**Tissue pair**: cervix_uterine and ovary  
**Genes (24)**: ACIN1, ACTL6A, BCLAF1, DDX5, DHX9, FAM120A, FKBP15, HNRNPH1, HNRNPL, HNRNPR, MATR3, PLRG1, PRPF31, CAD, RBM10, SF3B3, SNRNP40, SNW1, SUPT16H, QARS1, SNRNP200, EFTUD2, USP10, TJP1

### Function

The module is best interpreted as a conserved nuclear pre-mRNA processing and spliceosome module. The strongest primary evidence is the coordinated enrichment for RNA splicing and spliceosome biology in (GO:BP RNA splicing, via transesterification reactions; q_global = 5.9e-10) through (KEGG Spliceosome - Homo sapiens (human); q_global = 2.22e-05), including the catalytic step two spliceosome (GO:CC catalytic step 2 spliceosome; q_global = 3.13e-07), the spliceosomal complex (GO:CC spliceosomal complex; q_global = 1.1e-06), and the KEGG spliceosome pathway (KEGG Spliceosome - Homo sapiens (human); q_global = 2.22e-05). The module also contains U2-type spliceosomal, tri-snRNP, and small nuclear ribonucleoprotein annotations (GO:CC U2-type spliceosomal complex; q_global = 0.000244), (GO:CC U4/U6 x U5 tri-snRNP complex; q_global = 0.00825) through (GO:CC Sm-like protein family complex; q_global = 0.0141), and (GO:CC U2-type precatalytic spliceosome; q_global = 0.0372) through (GO:CC precatalytic spliceosome; q_global = 0.0372). The broad RNA-processing and RNA-binding terms (GO:BP mRNA metabolic process; q_global = 2.81e-06), (GO:BP RNA processing; q_global = 1.28e-05), (GO:MF RNA binding; q_global = 0.000887), (GO:BP RNA metabolic process; q_global = 0.00278), (GO:BP regulation of RNA splicing; q_global = 0.00288), and (GO:BP regulation of mRNA processing; q_global = 0.00363) indicate that the signal is not restricted to one isolated annotation but spans core spliceosome assembly, catalysis, and regulation. The nucleoplasmic, nuclear-speckle, and ribonucleoprotein-complex locations in (GO:CC ribonucleoprotein complex; q_global = 6.81e-05), (GO:CC nuclear ribonucleoprotein granule; q_global = 0.000253), (GO:CC nuclear speck; q_global = 0.00077), and (GO:CC ribonucleoprotein granule; q_global = 0.00117) are consistent with this interpretation. A secondary interpretation is that the module couples spliceosome activity to transcription, chromatin, nucleotide production, and post-transcriptional regulation through ACTL6A, SUPT16H, CAD, QARS1, USP10, TJP1, and the RNA-binding proteins. However, the primary evidence supports spliceosomal RNA processing rather than a tissue-specific metabolic or structural function.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly nuclear, nucleoplasmic, nuclear-speckle, nucleolar, or cytosolic. The module is also not strongly blood-cell specific. Most genes have low immune-cell specificity, and the tissue specificity is broadly low, with protein detection in cervix_uterine and nearly all proteins detected in ovary. A minority of genes show cell-type enhancement, including USP10 in neutrophils, FKBP15 in monocytes and neutrophils, SUPT16H in erythrocyte progenitors, and several genes in reproductive, neural, or epithelial cell types. Therefore, the shared co-abundance pattern is more plausibly a broadly expressed housekeeping or cell-state program involving RNA processing than an artifact driven mainly by plasma proteins or blood contamination. Cell composition may still contribute, particularly through shared epithelial, reproductive, or immune-associated cell states, but HPA does not support a dominant blood-cell explanation.

**GO/KEGG enrichment**: 40 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA splicing, via transesterification reactions | 5.9e-10 | ACIN1, DDX5, DHX9, EFTUD2, HNRNPH1, HNRNPL, HNRNPR, PLRG1, PRPF31, RBM10, SF3B3, SNRNP200, SNRNP40, SNW1 |
| GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile | 5.9e-10 | ACIN1, DDX5, DHX9, EFTUD2, HNRNPH1, HNRNPL, HNRNPR, PLRG1, PRPF31, RBM10, SF3B3, SNRNP200, SNRNP40, SNW1 |
| GO:BP mRNA splicing, via spliceosome | 5.9e-10 | ACIN1, DDX5, DHX9, EFTUD2, HNRNPH1, HNRNPL, HNRNPR, PLRG1, PRPF31, RBM10, SF3B3, SNRNP200, SNRNP40, SNW1 |
| GO:BP RNA splicing | 3.07e-09 | ACIN1, BCLAF1, DDX5, DHX9, EFTUD2, HNRNPH1, HNRNPL, HNRNPR, PLRG1, PRPF31, RBM10, SF3B3, SNRNP200, SNRNP40, SNW1 |
| GO:BP mRNA processing | 2.71e-08 | ACIN1, BCLAF1, DDX5, DHX9, EFTUD2, HNRNPH1, HNRNPL, HNRNPR, PLRG1, PRPF31, RBM10, SF3B3, SNRNP200, SNRNP40, SNW1 |
| GO:CC catalytic step 2 spliceosome | 3.13e-07 | DDX5, EFTUD2, HNRNPH1, HNRNPR, PLRG1, SF3B3, SNRNP200, SNRNP40, SNW1 |
| GO:CC spliceosomal complex | 1.1e-06 | DDX5, EFTUD2, HNRNPH1, HNRNPR, PLRG1, PRPF31, SF3B3, SNRNP200, SNRNP40, SNW1 |
| GO:BP mRNA metabolic process | 2.81e-06 | ACIN1, BCLAF1, DDX5, DHX9, EFTUD2, HNRNPH1, HNRNPL, HNRNPR, PLRG1, PRPF31, RBM10, SF3B3, SNRNP200, SNRNP40, SNW1 |
| GO:BP RNA processing | 1.28e-05 | ACIN1, BCLAF1, DDX5, DHX9, EFTUD2, HNRNPH1, HNRNPL, HNRNPR, PLRG1, PRPF31, RBM10, SF3B3, SNRNP200, SNRNP40, SNW1 |
| KEGG Spliceosome - Homo sapiens (human) | 2.22e-05 | ACIN1, DDX5, EFTUD2, PLRG1, PRPF31, SF3B3, SNRNP200, SNRNP40, SNW1 |
| GO:CC ribonucleoprotein complex | 6.81e-05 | DDX5, DHX9, EFTUD2, HNRNPH1, HNRNPL, HNRNPR, PLRG1, PRPF31, SF3B3, SNRNP200, SNRNP40, SNW1 |
| GO:BP nucleic acid biosynthetic process | 0.000163 | ACIN1, ACTL6A, BCLAF1, DDX5, DHX9, EFTUD2, HNRNPH1, HNRNPL, HNRNPR, PLRG1, PRPF31, QARS1, RBM10, SF3B3, SNRNP200, SNRNP40, SNW1, SUPT16H, USP10 |
| GO:CC U2-type spliceosomal complex | 0.000244 | EFTUD2, PLRG1, PRPF31, SF3B3, SNRNP200, SNRNP40, SNW1 |
| GO:CC nuclear ribonucleoprotein granule | 0.000253 | ACIN1, BCLAF1, DDX5, DHX9, EFTUD2, PLRG1, PRPF31, RBM10, SNRNP40, SNW1 |
| GO:CC nuclear protein-containing complex | 0.000302 | ACIN1, ACTL6A, BCLAF1, DDX5, EFTUD2, HNRNPH1, HNRNPR, PLRG1, PRPF31, SF3B3, SNRNP200, SNRNP40, SNW1, SUPT16H |

### STRING and hu.MAP

STRING provides strong supportive evidence for a real spliceosomal organization. The dense interaction group containing EFTUD2, PLRG1, PRPF31, SF3B3, SNRNP200, SNRNP40, and SNW1 corresponds to U five, U two, and tri-snRNP-related spliceosomal machinery, with additional known relationships among DDX5, DHX9, HNRNPH1, HNRNPL, HNRNPR, and MATR3. The STRING functional results independently recover mRNA splicing, mRNA processing, spliceosome, catalytic step two spliceosome, nucleoplasm, nuclear lumen, and nuclear speck evidence (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 1.32e-11) through (STRING COMPARTMENTS Nuclear speck; within-query FDR = 2.23e-06). hu.MAP further supports several distinct physical or complex-level groupings: (hu.MAP huMAP3_08501.1) through (hu.MAP huMAP3_06726.1) capture a recurring PLRG1-SNRNP200-SNW1-EFTUD2-SNRNP40 assembly; (hu.MAP huMAP3_08980.1), (hu.MAP huMAP3_00960.1), (hu.MAP huMAP3_07622.1), (hu.MAP huMAP3_00424.1), and (hu.MAP huMAP3_06511.1) connect the module to U-type snRNP and spliceosomal assemblies; and (hu.MAP huMAP3_10625.1) through (hu.MAP huMAP3_09223.1) support an hnRNP or RNA-binding group involving HNRNPR, HNRNPL, MATR3, and FAM120A. The ACIN1-BCLAF1 group in (hu.MAP huMAP3_06097.1) and (hu.MAP huMAP3_10564.1) through (hu.MAP huMAP3_09943.1), and the DDX5-USP10 group in (hu.MAP huMAP3_10631.1) and (hu.MAP huMAP3_11111.1), provide additional connections to RNA processing and RNA-associated complexes. These resources show that much of the network reflects known molecular machinery rather than an unexplained set of correlations. They do not, by themselves, establish that every co-abundance edge is a direct physical interaction or that the complete module exists as one stable complex.

**STRING interactions (score >= 0.7)**: 37 of 276 gene pairs: BCLAF1–SNW1 (0.823); DDX5–DHX9 (0.996); DDX5–HNRNPH1 (0.96); DDX5–HNRNPR (0.844); DDX5–MATR3 (0.894); DDX5–SNW1 (0.76); DHX9–HNRNPH1 (0.878); DHX9–HNRNPL (0.901); DHX9–HNRNPR (0.909); DHX9–MATR3 (0.786); DHX9–SF3B3 (0.73); DHX9–SNRNP200 (0.784); EFTUD2–PLRG1 (0.999); EFTUD2–PRPF31 (0.999); EFTUD2–SF3B3 (0.999); EFTUD2–SNRNP200 (0.999); EFTUD2–SNRNP40 (0.999); EFTUD2–SNW1 (0.999); HNRNPH1–HNRNPL (0.982); HNRNPH1–HNRNPR (0.947); HNRNPH1–MATR3 (0.911); HNRNPL–HNRNPR (0.961); HNRNPL–MATR3 (0.757); HNRNPR–MATR3 (0.714); PLRG1–SF3B3 (0.973); PLRG1–SNRNP200 (0.996); PLRG1–SNRNP40 (0.992); PLRG1–SNW1 (0.999); PRPF31–SF3B3 (0.997); PRPF31–SNRNP200 (0.999); PRPF31–SNRNP40 (0.944); SF3B3–SNRNP200 (0.999); SF3B3–SNRNP40 (0.852); SF3B3–SNW1 (0.99); SNRNP200–SNRNP40 (0.999); SNRNP200–SNW1 (0.998); SNRNP40–SNW1 (0.994)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM mRNA Splicing - Major Pathway (FDR = 1.32e-11, 14 genes); Keyword mRNA splicing (FDR = 8.33e-10, 13 genes); Process mRNA processing (FDR = 5.59e-09, 15 genes); Process RNA splicing (FDR = 5.59e-09, 14 genes); Process mRNA splicing, via spliceosome (FDR = 7.55e-09, 12 genes); Keyword Spliceosome (FDR = 1.2e-08, 10 genes); COMPARTMENTS Nucleoplasm (FDR = 1.67e-07, 16 genes); COMPARTMENTS Spliceosomal complex (FDR = 1.67e-07, 10 genes); COMPARTMENTS Catalytic step 2 spliceosome (FDR = 1.67e-07, 9 genes); Component Spliceosomal complex (FDR = 2.79e-07, 10 genes); Component Catalytic step 2 spliceosome (FDR = 2.79e-07, 9 genes); COMPARTMENTS Nuclear lumen (FDR = 6.53e-07, 18 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 1.96e-06, 12 genes); Process Nucleic acid metabolic process (FDR = 2.17e-06, 19 genes); COMPARTMENTS Nuclear speck (FDR = 2.23e-06, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08501.1 (PLRG1, SNRNP200, SNW1, EFTUD2, SNRNP40; 5/47); huMAP3_09504.1 (PLRG1, SNRNP200, SNW1, EFTUD2, SNRNP40; 5/51); huMAP3_09945.1 (PLRG1, SNRNP200, SNW1, EFTUD2, SNRNP40; 5/61); huMAP3_08980.1 (SNRNP200, EFTUD2, SF3B3, PRPF31, SNRNP40; 5/97); huMAP3_06726.1 (PLRG1, SNRNP200, SNW1, SNRNP40; 4/37); huMAP3_10625.1 (HNRNPR, HNRNPL, MATR3, FAM120A; 4/57); huMAP3_07225.1 (HNRNPR, HNRNPL, FAM120A; 3/7); huMAP3_00960.1 (SNRNP200, EFTUD2, SNRNP40; 3/8); huMAP3_07622.1 (SNRNP200, EFTUD2, SNRNP40; 3/9); huMAP3_09654.1 (HNRNPR, HNRNPL, FAM120A; 3/13); huMAP3_07581.1 (HNRNPR, HNRNPL, MATR3; 3/21); huMAP3_10659.1 (HNRNPR, HNRNPL, FAM120A; 3/28); huMAP3_05721.1 (HNRNPL, MATR3; 2/6); huMAP3_00424.1 (EFTUD2, SNRNP40; 2/8); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09281.1 (HNRNPR, FAM120A; 2/14); huMAP3_09223.1 (MATR3, FAM120A; 2/15); huMAP3_06097.1 (BCLAF1, ACIN1; 2/22); huMAP3_10631.1 (DDX5, USP10; 2/28); huMAP3_11111.1 (DDX5, USP10; 2/29); huMAP3_10564.1 (BCLAF1, ACIN1; 2/37); huMAP3_11073.1 (BCLAF1, ACIN1; 2/67); huMAP3_09943.1 (BCLAF1, ACIN1; 2/78); huMAP3_06511.1 (SF3B3, PRPF31; 2/79)

### Novelty

The biological function is not a new discovery: spliceosome and RNA-processing roles are already established by the primary GO/KEGG annotations, STRING relationships, hu.MAP complexes, and gene literature. The co-abundance observation may nevertheless be a useful new systems-level finding because it identifies a conserved module shared by cervix_uterine and ovary and combines several spliceosomal assemblies with RNA-binding, chromatin, nucleotide, and regulatory genes. The fact sheet does not provide a matched prior module catalog, independent replication, perturbation experiment, or tissue-specific causal test, so it is not justified to call the entire module novel. Absence of STRING or hu.MAP support for genes such as SUPT16H, CAD, FAM120A, RBM10, DHX9, or TJP1 within particular complexes is not evidence of novelty; it may reflect incomplete coverage, indirect relationships, or co-regulation rather than physical binding. The defensible conclusion is that the module represents a conserved and biologically coherent co-abundance configuration, with potentially novel tissue-pair organization but an established underlying molecular function.

**Hypothesis.** Hypothesis: shared epithelial or reproductive-tissue cell states in cervix_uterine and ovary coordinate expression of core spliceosomal machinery with RNA surveillance, alternative-splicing regulation, transcriptional elongation, and biosynthetic capacity. In this model, the EFTUD2-PLRG1-PRPF31-SF3B3-SNRNP200-SNRNP40-SNW1 group supplies core spliceosome and tri-snRNP functions, while DDX5, DHX9, HNRNPH1, HNRNPL, HNRNPR, MATR3, RBM10, ACIN1, and BCLAF1 tune transcript selection, RNA structure, RNA stability, and nuclear organization. SUPT16H and ACTL6A could couple transcription and chromatin remodeling to co-transcriptional RNA processing, whereas CAD and QARS1 could reflect the biosynthetic demands of active gene expression. The co-abundance signal could therefore arise from coordinated transcriptional and post-transcriptional activity rather than from one physical mega-complex. This hypothesis requires testing with cell-resolved expression, isoform-level splicing measurements, perturbation of core spliceosome or regulatory genes, and comparison of the module across independent cervix and ovary datasets.

### Important genes

#### EFTUD2

- **Related proteins** (co-abundance neighbors): MATR3 (0.87), TJP1 (0.84), FAM120A (0.84), SNRNP200 (0.84), DDX5 (0.82), SF3B3 (0.82), RBM10 (0.82), BCLAF1 (0.80); STRING partners: PLRG1 (0.999), PRPF31 (0.999), SF3B3 (0.999), SNRNP200 (0.999), SNRNP40 (0.999), SNW1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_08980.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_00424.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 has a strong central position in the module and is connected to the core spliceosomal group. It is present across the primary splicing, spliceosome, U2, and tri-snRNP evidence (GO:BP RNA splicing, via transesterification reactions; q_global = 5.9e-10) through (GO:CC precatalytic spliceosome; q_global = 0.0372), is linked to PLRG1, PRPF31, SF3B3, SNRNP200, SNRNP40, and SNW1 by STRING, and occurs in several hu.MAP spliceosomal complexes (hu.MAP huMAP3_08501.1) through (hu.MAP huMAP3_06726.1), (hu.MAP huMAP3_00960.1), (hu.MAP huMAP3_07622.1), and (hu.MAP huMAP3_00424.1). Its established role is as a spliceosomal GTPase involved in snRNP assembly and spliceosome conformational change. It has substantial literature and a disease association with mandibulofacial dysostosis with microcephaly.
- **Conclusion**: Established evidence identifies EFTUD2 as a core spliceosome and tri-snRNP component that helps explain the module's central function. Its co-abundance with the surrounding spliceosomal genes is biologically expected. A module-specific role in cervix_uterine or ovary is a hypothesis, not established by the fact sheet.

#### DDX5

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.82), PRPF31 (0.81), SF3B3 (0.81), SNW1 (0.80), QARS1 (0.80), USP10 (0.80); STRING partners: DHX9 (0.996), HNRNPH1 (0.96), HNRNPR (0.844), MATR3 (0.894), SNW1 (0.76)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_10631.1, huMAP3_11111.1
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 is among the more connected genes in the co-abundance network and links the core spliceosomal group to RNA helicase and heterogeneous nuclear ribonucleoprotein relationships. It participates in nearly all of the primary splicing evidence and in the STRING splicing results (GO:BP RNA splicing, via transesterification reactions; q_global = 5.9e-10) through (GO:CC ribonucleoprotein complex; q_global = 6.81e-05), (GO:CC nuclear ribonucleoprotein granule; q_global = 0.000253) through (GO:CC nuclear body; q_global = 0.00642), and (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 1.32e-11) through (STRING COMPARTMENTS Nuclear speck; within-query FDR = 2.23e-06). Its established functions include RNA structure remodeling, alternative-splicing regulation, transcriptional co-regulation, and small noncoding RNA processing. It has the largest literature volume among the highlighted genes and disease associations spanning viral disease and cancer.
- **Conclusion**: Established evidence supports DDX5 as an RNA helicase and regulatory bridge between spliceosomal machinery and RNA-binding proteins. Its position makes it a plausible coordinator of module activity, but the co-abundance data do not prove that DDX5 drives the module or specifies a cervix-ovary program.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): CAD (0.88), BCLAF1 (0.86), SUPT16H (0.86), EFTUD2 (0.84); STRING partners: DHX9 (0.784), EFTUD2 (0.999), PLRG1 (0.996), PRPF31 (0.999), SF3B3 (0.999), SNRNP40 (0.999), SNW1 (0.998)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_08980.1, huMAP3_06726.1, huMAP3_00960.1, huMAP3_07622.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is a U5 snRNP-specific RNA helicase and a core component of the U4/U6-U5 tri-snRNP. It is represented in the primary spliceosome and tri-snRNP terms (GO:BP RNA splicing, via transesterification reactions; q_global = 5.9e-10) through (GO:CC U2-type spliceosomal complex; q_global = 0.000244) and (GO:CC U4/U6 x U5 tri-snRNP complex; q_global = 0.00825) through (GO:CC Sm-like protein family complex; q_global = 0.0141), has strong STRING relationships with the core spliceosomal group, and appears in multiple high-confidence hu.MAP complexes (hu.MAP huMAP3_08501.1) through (hu.MAP huMAP3_06726.1), (hu.MAP huMAP3_00960.1), and (hu.MAP huMAP3_07622.1). Its established disease associations include retinitis pigmentosa and inherited retinal dystrophy, and its literature directly concerns spliceosome assembly and conformational change.
- **Conclusion**: Established evidence makes SNRNP200 a strong mechanistic anchor for the module's tri-snRNP interpretation. Its lower network degree does not reduce its importance because it represents a specialized core component. The tissue-pair data support coordinated abundance with other spliceosomal components but do not establish a tissue-specific SNRNP200 function.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): BCLAF1 (0.83), PLRG1 (0.83); STRING partners: DHX9 (0.901), HNRNPH1 (0.982), HNRNPR (0.961), MATR3 (0.757)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_07225.1, huMAP3_09654.1, huMAP3_07581.1, huMAP3_10659.1, huMAP3_05721.1, huMAP3_06093.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL represents the regulatory RNA-binding arm of the module. It is included in the primary RNA-splicing, RNA-processing, RNA-binding, and regulation-of-splicing evidence (GO:BP RNA splicing, via transesterification reactions; q_global = 5.9e-10) through (GO:BP mRNA processing; q_global = 2.71e-08), (GO:BP mRNA metabolic process; q_global = 2.81e-06), (GO:BP RNA processing; q_global = 1.28e-05), (GO:CC ribonucleoprotein complex; q_global = 6.81e-05), (GO:MF RNA binding; q_global = 0.000887), (GO:BP regulation of RNA splicing; q_global = 0.00288), and (GO:BP regulation of mRNA processing; q_global = 0.00363). STRING connects it strongly with HNRNPH1, HNRNPR, DHX9, and MATR3, while hu.MAP repeatedly places it with hnRNP-associated complexes (hu.MAP huMAP3_10625.1), (hu.MAP huMAP3_07225.1), (hu.MAP huMAP3_09654.1) through (hu.MAP huMAP3_09223.1). It has broad literature, established roles in hnRNA packaging and alternative-splicing regulation, and an ovarian cancer association in the supplied evidence.
- **Conclusion**: Established evidence supports HNRNPL as a regulator of transcript processing that complements the core spliceosome proteins. It may help determine which transcripts respond to the module, but a specific ovarian or cervical transcript program remains a hypothesis.

#### RBM10

- **Related proteins** (co-abundance neighbors): BCLAF1 (0.84), EFTUD2 (0.82), CAD (0.82), FKBP15 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 10. This gene encodes a nuclear protein that belongs to a family proteins that contain an RNA-binding motif. The encoded protein associates with hnRNP proteins and may be involved in regulating alternative splicing. Defects in this gene are the cause of the X-linked recessive disorder, TARP syndrome. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Mar 2011].
- **Diseases (Open Targets)**: TARP syndrome (0.787); lung adenocarcinoma (0.629); neurodegenerative disease (0.526); pancreatic adenocarcinoma (0.513); non-small cell lung carcinoma (0.510)
- **Europe PMC papers**: 1601
- **Why important**: RBM10 is a nuclear-speckle RNA-binding protein with module connections to BCLAF1, EFTUD2, CAD, and FKBP15. It is present in the primary splicing and regulation-of-splicing terms (GO:BP RNA splicing, via transesterification reactions; q_global = 5.9e-10) through (GO:BP mRNA processing; q_global = 2.71e-08), (GO:CC nuclear ribonucleoprotein granule; q_global = 0.000253), (GO:CC nuclear speck; q_global = 0.00077), (GO:MF RNA binding; q_global = 0.000887), (GO:BP regulation of RNA splicing; q_global = 0.00288), (GO:BP regulation of mRNA processing; q_global = 0.00363), (GO:CC nuclear body; q_global = 0.00642), and (GO:BP regulation of mRNA splicing, via spliceosome; q_global = 0.0216). Its established role is regulation of alternative splicing through association with hnRNP proteins, and it is associated with TARP syndrome and several cancer or neurodegenerative disease categories. Its substantial literature provides functional context beyond simple network connectivity.
- **Conclusion**: Established evidence supports RBM10 as a regulatory rather than core catalytic spliceosome component. Its position suggests that the module may encode both spliceosome abundance and alternative-splicing control. Whether RBM10 mediates the shared cervix-ovary behavior is unproven.

## Module 3

**Tissue pair**: cervix_uterine and ovary  
**Genes (5)**: AFDN, DSP, MYH14, JUP, WASF2

### Function

This is a cell-junction and cytoskeletal module, with the strongest primary evidence for actin filament-based movement (GO:BP actin filament-based movement; q_global = 0.00103), cell-cell contact zones (GO:CC cell-cell contact zone; q_global = 0.0165), desmosome organization (GO:BP desmosome organization; q_global = 0.0428), and cell-junction organization (GO:BP cell junction organization; q_global = 0.0487). DSP and JUP account for the desmosomal and adhesive core, while AFDN links the module to adherens-junction organization and WASF2 to actin remodeling. MYH14 adds a non-muscle myosin component associated with actin-dependent movement and cell-shape regulation. The action-potential, striated-muscle, and cardiac-conduction terms (GO:BP action potential; q_global = 0.00743), (GO:BP bundle of His cell to Purkinje myocyte communication; q_global = 0.0182), (GO:BP striated muscle contraction; q_global = 0.0194), (GO:BP regulation of heart rate by cardiac conduction; q_global = 0.0428), and (GO:BP regulation of ventricular cardiac muscle cell action potential; q_global = 0.0428) are statistically supported but should be interpreted cautiously: they may reflect shared junctional and cytoskeletal biology rather than a cardiac-specific program in cervix or ovary.

**Cell composition.** The module is not dominated by secreted or plasma proteins; the HPA summary reports no secreted genes. It is also not a conventional housekeeping module. Most genes show cell-type enhancement, especially in epithelial populations, with recurrent enrichment in esophageal and suprabasal epithelial cells. DSP and JUP are tissue enhanced in esophagus and skin, whereas MYH14 is tissue enhanced in intestine and skeletal muscle. AFDN and WASF2 have low tissue specificity. Blood-cell evidence is mixed: DSP and JUP have immune-cell enrichment categories, but AFDN and WASF2 have low immune specificity and MYH14 is not detected in immune cells. Protein detection in both cervix_uterine and ovary is broadly concordant, although DSP is not detected by IHC in cervix_uterine. Overall, the shared module is more consistent with epithelial or junctional cell composition and cytoskeletal state than with a plasma-protein signal; immune-cell contribution cannot be excluded for DSP and JUP.

**GO/KEGG enrichment**: 13 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP actin filament-based movement | 0.00103 | DSP, JUP, MYH14, WASF2 |
| GO:BP action potential | 0.00743 | DSP, JUP, MYH14 |
| GO:CC cell-cell contact zone | 0.0165 | AFDN, DSP, JUP |
| GO:BP cardiac muscle cell-cardiac muscle cell adhesion | 0.0182 | DSP, JUP |
| GO:BP bundle of His cell to Purkinje myocyte communication | 0.0182 | DSP, JUP |
| GO:BP bundle of His cell-Purkinje myocyte adhesion involved in cell communication | 0.0182 | DSP, JUP |
| GO:MF cell adhesive protein binding involved in bundle of His cell-Purkinje myocyte communication | 0.0182 | DSP, JUP |
| GO:BP striated muscle contraction | 0.0194 | DSP, JUP, MYH14 |
| GO:BP desmosome organization | 0.0428 | DSP, JUP |
| GO:MF protein binding involved in heterotypic cell-cell adhesion | 0.0428 | DSP, JUP |
| GO:BP regulation of heart rate by cardiac conduction | 0.0428 | DSP, JUP |
| GO:BP regulation of ventricular cardiac muscle cell action potential | 0.0428 | DSP, JUP |
| GO:BP cell junction organization | 0.0487 | AFDN, DSP, JUP, WASF2 |

### STRING and hu.MAP

STRING provides one high-confidence direct interaction within the module, DSP-JUP (STRING COMPARTMENTS Cell-cell contact zone; within-query FDR = 0.0044), and no listed STRING interactions for the other pairs. This supports a real desmosomal core but does not establish that all module members form one physical complex. The STRING functional results independently reinforce cell junctions, fascia adherens, desmosomes, and cell-junction organization (STRING COMPARTMENTS Cell-cell contact zone; within-query FDR = 0.0044), (STRING Component Cell-cell junction; within-query FDR = 0.0157), (STRING Process Cell junction organization; within-query FDR = 0.0227), (STRING Component Fascia adherens; within-query FDR = 0.0373), (STRING Component Desmosome; within-query FDR = 0.0391). The disease annotations for arrhythmogenic right ventricular cardiomyopathy and Naxos disease (STRING DISEASES Arrhythmogenic right ventricular cardiomyopathy; within-query FDR = 0.04), (STRING DISEASES Naxos disease; within-query FDR = 0.04) are driven by DSP and JUP and are biologically concordant with their junctional roles. hu.MAP identifies DSP and JUP together in several complexes (hu.MAP huMAP3_05845.1) (hu.MAP huMAP3_08595.1) (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1), including complexes populated by epithelial and desmosomal proteins, but AFDN, WASF2, and MYH14 are not represented in those listed complexes. Thus, known evidence supports a DSP-JUP desmosomal module embedded in a broader co-abundance neighborhood containing adhesion and actin-regulatory genes.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: DSP–JUP (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Cell-cell contact zone (FDR = 0.0044, 3 genes); Process Multicellular organismal signaling (FDR = 0.0114, 3 genes); Component Cell-cell contact zone (FDR = 0.0142, 3 genes); Component Cell-cell junction (FDR = 0.0157, 4 genes); Process Cell junction organization (FDR = 0.0227, 4 genes); Component Fascia adherens (FDR = 0.0373, 2 genes); COMPARTMENTS Fascia adherens (FDR = 0.0388, 2 genes); Component Desmosome (FDR = 0.0391, 2 genes); DISEASES Arrhythmogenic right ventricular cardiomyopathy (FDR = 0.04, 2 genes); DISEASES Naxos disease (FDR = 0.04, 2 genes); COMPARTMENTS Desmosome (FDR = 0.0407, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05845.1 (JUP, DSP; 2/24); huMAP3_08595.1 (JUP, DSP; 2/25); huMAP3_09125.1 (JUP, DSP; 2/53); huMAP3_09929.1 (JUP, DSP; 2/75)

### Novelty

The module is a plausible and biologically coherent conserved co-abundance pattern shared by cervix_uterine and ovary, but it should not be described as a newly discovered protein complex. DSP-JUP is already a very well-established interaction in STRING and hu.MAP, and the associated desmosome, adhesion, and cardiomyopathy biology is extensively documented. The potentially less-established aspect is the tissue-pair-specific co-abundance of DSP, JUP, AFDN, WASF2, and MYH14, especially the connection of the actin-regulatory genes to the known desmosomal core. However, the limited direct STRING connectivity and absence of the other module members from the listed hu.MAP complexes mean that novelty currently concerns the network context and tissue association, not a proven new molecular interaction. Independent validation at the protein and cell-type level would be needed.

**Hypothesis.** Hypothesis: in epithelial populations shared between cervix_uterine and ovary, junctional adhesion structures centered on DSP and JUP may be co-regulated with AFDN-mediated adherens-junction signaling and WASF2- and MYH14-associated actin remodeling. This could coordinate cell-cell adhesion, mechanical coupling, polarity, and shape changes. The cardiac-conduction and striated-muscle annotations may reflect the reuse of conserved junctional and cytoskeletal machinery rather than cardiac tissue contamination or a cardiac-specific function. The mixed immune-cell HPA signal suggests that sample composition could modulate the observed abundance, particularly for DSP and JUP.

### Important genes

#### DSP

- **Related proteins** (co-abundance neighbors): WASF2 (0.84), JUP (0.82), MYH14 (0.82); STRING partners: JUP (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cell Junctions; IHC detected in ovary
- **hu.MAP 3.0**: huMAP3_05845.1, huMAP3_08595.1, huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: desmoplakin. This gene encodes a protein that anchors intermediate filaments to desmosomal plaques and forms an obligate component of functional desmosomes. Mutations in this gene are the cause of several cardiomyopathies and keratodermas, including skin fragility-woolly hair syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016].
- **Diseases (Open Targets)**: arrhythmogenic cardiomyopathy with wooly hair and keratoderma (0.841); arrhythmogenic right ventricular dysplasia 8 (0.812); arrhythmogenic right ventricular cardiomyopathy (0.760); lethal acantholytic epidermolysis bullosa (0.745); cardiomyopathy, dilated, with wooly hair, keratoderma, and tooth agenesis (0.741)
- **Europe PMC papers**: 17350
- **Why important**: DSP is the highest-connectivity gene in the module and connects to JUP, WASF2, and MYH14. It appears in every primary enriched term (13 globally significant GO/KEGG terms, q_global 0.00103–0.0487; see the table), is the obligate desmosomal plaque component described in the fact sheet, and has extensive disease and literature support for cardiomyopathies, keratodermas, and skin-fragility disorders. Its presence in all listed hu.MAP complexes and its very strong STRING interaction with JUP make it a central anchor.
- **Conclusion**: Established evidence supports DSP as a core structural desmosome gene and a principal driver of the module's adhesion, cytoskeletal, and cardiomyopathy-related signal. The hypothesis that DSP abundance coordinates the other module genes in cervix_uterine and ovary remains unproven.

#### JUP

- **Related proteins** (co-abundance neighbors): DSP (0.82), AFDN (0.81), WASF2 (0.80); STRING partners: DSP (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_05845.1, huMAP3_08595.1, huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: junction plakoglobin. This gene encodes a major cytoplasmic protein which is the only known constituent common to submembranous plaques of both desmosomes and intermediate junctions. This protein forms distinct complexes with cadherins and desmosomal cadherins and is a member of the catenin family since it contains a distinct repeating amino acid motif called the armadillo repeat. Mutation in this gene has been associa…
- **Diseases (Open Targets)**: Naxos disease (0.784); arrhythmogenic right ventricular dysplasia 12 (0.755); arrhythmogenic right ventricular cardiomyopathy (0.597); lethal acantholytic epidermolysis bullosa (0.383); familial isolated arrhythmogenic ventricular dysplasia, biventricular form (0.370)
- **Europe PMC papers**: 3429
- **Why important**: JUP has high connectivity, linking DSP, AFDN, and WASF2, and appears in every primary enriched term (13 globally significant GO/KEGG terms, q_global 0.00103–0.0487; see the table). It is a catenin-family component shared by desmosomal and intermediate junction plaques, is detected in both tissues, and has established associations with Naxos disease and arrhythmogenic cardiomyopathy. Its near-maximal STRING association with DSP and repeated hu.MAP membership identify it as the second central anchor.
- **Conclusion**: Established evidence supports JUP as a multifunctional junctional scaffold that can connect desmosomal adhesion with broader cell-adhesion signaling. Its co-abundance with AFDN and WASF2 may indicate coordinated junction remodeling, but the fact sheet does not establish direct physical interactions among all three genes.

#### AFDN

- **Related proteins** (co-abundance neighbors): WASF2 (0.81), JUP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: afadin, adherens junction formation factor. This gene encodes a multi-domain protein involved in signaling and organization of cell junctions during embryogenesis. It has also been identified as the fusion partner of acute lymphoblastic leukemia (ALL-1) gene, involved in acute myeloid leukemias with t(6;11)(q27;q23) translocation. Alternatively spliced transcript variants encoding different isoforms have been described for this gene, howeve…
- **Diseases (Open Targets)**: colorectal adenocarcinoma (0.401); lung carcinoma (0.371); gastric carcinoma (0.371); carcinoma of liver and intrahepatic biliary tract (0.370); melanoma (0.370)
- **Europe PMC papers**: 633
- **Why important**: AFDN has intermediate network connectivity to WASF2 and JUP and contributes to the globally supported cell-cell contact and cell-junction terms (GO:CC cell-cell contact zone; q_global = 0.0165), (GO:BP cell junction organization; q_global = 0.0487). Its annotated functions include adherens-junction formation, cell adhesion, cell-cell signaling, and differentiation. HPA places it at the plasma membrane and cell junctions and detects it in both tissues, making it a plausible bridge between the DSP-JUP desmosomal core and other adhesion machinery.
- **Conclusion**: Established evidence supports AFDN as an adhesion and junction-organization component of the module. Its bridging role between the desmosomal core and actin-associated genes is a reasonable network-based hypothesis, not a demonstrated molecular complex.

#### WASF2

- **Related proteins** (co-abundance neighbors): DSP (0.84), AFDN (0.81), JUP (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WASP family member 2. This gene encodes a member of the Wiskott-Aldrich syndrome protein family. The gene product is a protein that forms a multiprotein complex that links receptor kinases and actin. Binding to actin occurs through a C-terminal verprolin homology domain in all family members. The multiprotein complex serves to tranduce signals that involve changes in cell shape, motility or function. The published map …
- **Diseases (Open Targets)**: hypertensive disorder (0.156); Abnormality of the skeletal system (0.155); cardiovascular disorder (0.144); aortic stenosis (0.140); neoplasm (0.107)
- **Europe PMC papers**: 791
- **Why important**: WASF2 has high connectivity and links DSP, AFDN, and JUP, despite having no listed STRING partner or hu.MAP complex membership. Its primary annotations support actin filament-based movement and cell-junction organization (GO:BP actin filament-based movement; q_global = 0.00103), (GO:BP cell junction organization; q_global = 0.0487), while its known function connects receptor signaling to actin, lamellipodium assembly, cell shape, and motility. HPA detects it in both tissues and shows epithelial cell-type enhancement.
- **Conclusion**: Established evidence supports WASF2 as the module's actin-remodeling and cell-shape component. Its co-abundance with desmosomal genes suggests coordinated junction-cytoskeleton regulation, but the absence of listed independent physical interaction evidence makes this connection provisional.

#### MYH14

- **Related proteins** (co-abundance neighbors): DSP (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin heavy chain 14. This gene encodes a member of the myosin superfamily. The protein represents a conventional non-muscle myosin; it should not be confused with the unconventional myosin-14 (MYO14). Myosins are actin-dependent motor proteins with diverse functions including regulation of cytokinesis, cell motility, and cell polarity. Mutations in this gene result in one form of autosomal dominant hearing impairment.…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 4A (0.736); peripheral neuropathy-myopathy-hoarseness-hearing loss syndrome (0.585); autosomal dominant nonsyndromic hearing loss (0.479); sensorineural hearing loss disorder (0.365); nonsyndromic genetic hearing loss (0.342)
- **Europe PMC papers**: 1724
- **Why important**: MYH14 is the least connected gene, with a single module neighbor, DSP, but it contributes to the globally supported actin movement, action-potential, and striated-muscle terms (GO:BP actin filament-based movement; q_global = 0.00103), (GO:BP action potential; q_global = 0.00743), (GO:BP striated muscle contraction; q_global = 0.0194). Its annotated functions include non-muscle myosin activity, cytokinesis, cell motility, polarity, and cell-shape regulation. Its disease associations include inherited hearing-loss and neuropathy-myopathy syndromes, and HPA shows tissue enhancement in intestine and skeletal muscle with no immune-cell detection.
- **Conclusion**: Established evidence supports MYH14 as a motor and cell-shape gene that may add contractile or remodeling capacity to the module. Its specific functional connection to DSP in cervix_uterine and ovary is a hypothesis based on co-abundance and network structure rather than established complex membership.

## Module 4

**Tissue pair**: cervix_uterine and ovary  
**Genes (9)**: SERPINC1, APOA1, CLU, C3, ALAD, MYLK, PLG, F2, VTN

### Function

The strongest interpretation is a complement, coagulation, fibrinolysis, and wound-response module. The primary evidence is the globally corrected KEGG complement and coagulation term (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 6.16e-08), together with globally corrected blood microparticle (GO:CC blood microparticle; q_global = 7.47e-07), wound-healing and response-to-wounding terms (GO:BP regulation of wound healing; q_global = 0.000351), (GO:BP regulation of response to wounding; q_global = 0.0006), (GO:BP positive regulation of wound healing; q_global = 0.0006), (GO:BP positive regulation of response to wounding; q_global = 0.0006), (GO:BP wound healing; q_global = 0.0305), coagulation and hemostasis terms (GO:BP regulation of blood coagulation; q_global = 0.00154), (GO:BP regulation of hemostasis; q_global = 0.00154), (GO:BP regulation of coagulation; q_global = 0.00257), (GO:BP positive regulation of hemostasis; q_global = 0.00432), (GO:BP blood coagulation; q_global = 0.0485), (GO:BP hemostasis; q_global = 0.0485), and fibrinolysis terms (GO:BP regulation of fibrinolysis; q_global = 0.00432), (GO:BP negative regulation of fibrinolysis; q_global = 0.00432), (GO:BP fibrinolysis; q_global = 0.0169). F2, PLG, SERPINC1, and VTN provide the clearest coagulation and fibrinolysis axis; C3 adds complement activation; APOA1 and CLU add lipoprotein, extracellular-particle, receptor-regulatory, and stress-associated context. MYLK provides a possible contractile and tissue-repair component, while ALAD is linked here mainly through the broad stress-response terms (GO:BP response to external stimulus; q_global = 0.00472) and (GO:BP response to stress; q_global = 0.026). The globally corrected enrichment supports a coherent extracellular hemostatic and injury-response interpretation rather than an isolated annotation. The neuroactive ligand-receptor result (KEGG Neuroactive ligand-receptor interaction - Homo sapiens (human); q_global = 0.00752) is secondary to the dominant complement, coagulation, and wound-response signal.

**Cell composition.** This module is strongly dominated by secreted or plasma-associated proteins. HPA classifies most genes as secreted, with frequent liver tissue enrichment and hepatocyte specificity, while protein detection is absent in ovary and largely absent in cervix_uterine. APOA1, C3, F2, PLG, SERPINC1, VTN, and CLU are especially consistent with a circulating hepatic secretome or blood-derived extracellular-particle signal. HPA also reports platelet, megakaryocyte, and selected immune-cell associations, although several genes are not detected in immune cells. Therefore, the shared cervix_uterine–ovary module may reflect plasma carryover, blood microparticles, vascular exposure, or shared blood-associated material rather than coordinated transcription by resident ovarian and cervical cells. CLU has cervix_uterine protein detection, but the overall HPA pattern does not support strong local protein production across both tissues. MYLK is the main non-secreted, contractile-cell-associated component, and ALAD is a cytosolic enzyme with liver and erythroid-related associations.

**GO/KEGG enrichment**: 37 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 6.16e-08 | C3, CLU, F2, PLG, SERPINC1, VTN |
| GO:CC blood microparticle | 7.47e-07 | APOA1, C3, CLU, F2, PLG, SERPINC1, VTN |
| GO:BP regulation of wound healing | 0.000351 | F2, MYLK, PLG, SERPINC1, VTN |
| GO:CC endoplasmic reticulum lumen | 0.0005 | APOA1, C3, CLU, F2, SERPINC1, VTN |
| GO:BP regulation of response to wounding | 0.0006 | F2, MYLK, PLG, SERPINC1, VTN |
| GO:BP positive regulation of wound healing | 0.0006 | F2, MYLK, PLG, VTN |
| GO:BP positive regulation of response to wounding | 0.0006 | F2, MYLK, PLG, VTN |
| GO:BP regulation of response to stress | 0.000865 | APOA1, C3, CLU, F2, MYLK, PLG, SERPINC1, VTN |
| GO:BP regulation of blood coagulation | 0.00154 | F2, PLG, SERPINC1, VTN |
| GO:BP regulation of hemostasis | 0.00154 | F2, PLG, SERPINC1, VTN |
| GO:BP regulation of endocytosis | 0.0016 | APOA1, C3, CLU, MYLK, VTN |
| GO:BP regulation of coagulation | 0.00257 | F2, PLG, SERPINC1, VTN |
| GO:BP positive regulation of blood coagulation | 0.00432 | F2, PLG, VTN |
| GO:BP positive regulation of coagulation | 0.00432 | F2, PLG, VTN |
| GO:BP regulation of fibrinolysis | 0.00432 | F2, PLG, VTN |

### STRING and hu.MAP

STRING provides extensive prior knowledge for the plasma-protein core: F2 is linked to SERPINC1, PLG, C3, and APOA1; PLG is linked to C3, SERPINC1, F2, and VTN; VTN is linked to PLG, SERPINC1, CLU, C3, and APOA1; and APOA1 and CLU are strongly connected. These relationships agree with the globally corrected complement, coagulation, blood-microparticle, and plasma-protein interpretations, but STRING evidence is supplementary and does not substitute for global correction. ALAD and MYLK have no listed high-confidence STRING partners, so their placement may reflect co-abundance rather than established physical interaction. hu.MAP repeatedly places F2, PLG, C3, and APOA1 within broad plasma-associated complexes (hu.MAP huMAP3_08395.1) through (hu.MAP huMAP3_10678.1), with additional pairwise or smaller-complex support in (hu.MAP huMAP3_08796.1) through (hu.MAP huMAP3_09434.1). This indicates that the module contains a known circulating-protein interaction and co-complex core, while not demonstrating that all module members form one physical complex in cervix_uterine or ovary.

**STRING interactions (score >= 0.7)**: 15 of 36 gene pairs: APOA1–C3 (0.957); APOA1–CLU (0.998); APOA1–F2 (0.927); APOA1–SERPINC1 (0.708); APOA1–VTN (0.755); C3–CLU (0.803); C3–F2 (0.874); C3–PLG (0.978); C3–VTN (0.79); CLU–VTN (0.962); F2–PLG (0.826); F2–SERPINC1 (0.999); PLG–SERPINC1 (0.992); PLG–VTN (0.995); SERPINC1–VTN (0.949)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Complement and coagulation cascades (FDR = 1.2e-08, 6 genes); Component Blood microparticle (FDR = 1.04e-07, 7 genes); COMPARTMENTS Blood microparticle (FDR = 1.08e-07, 7 genes); WikiPathways Complement and coagulation cascades (FDR = 1.32e-06, 5 genes); PMID (2022) Circulating Proteins Associated with Response and Resistance to Neoadjuvant Chemotherapy in HER2-Positive Breast Cancer. (FDR = 1.49e-06, 7 genes); PMID (2014) Proteomic analysis of human plasma in chronic rheumatic mitral stenosis reveals proteins involved in the complement and coagulation cascade. (FDR = 1.49e-06, 7 genes); NetworkNeighborAL Complement and coagulation cascades, and Protein-lipid complex (FDR = 1.51e-06, 6 genes); PMID (2024) The in vitro gastrointestinal digestion-associated protein corona of polystyrene nano- and microplastics increases their uptake by human THP-1-derived macrophages. (FDR = 3.07e-06, 6 genes); PMID (2020) Novel Associations between Related Proteins and Cellular Effects of High-Density Lipoprotein. (FDR = 3.07e-06, 6 genes); PMID (2018) Molecular Camouflage of Plasmodium falciparum Merozoites by Binding of Host Vitronectin to P47 Fragment of SERA5. (FDR = 3.07e-06, 6 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 3.37e-06, 7 genes); PMID (2017) Characterization of Vitreous and Aqueous Proteome in Humans With Proliferative Diabetic Retinopathy and Its Clinical Correlation. (FDR = 3.5e-06, 6 genes); PMID (2011) Immunoblot analysis of proteins associated with self-assembled monolayer surfaces of defined chemistries. (FDR = 3.5e-06, 6 genes); PMID (2016) Mass Spectrometry-based Proteomics in Acute Respiratory Distress Syndrome: A Powerful Modality for Pulmonary Precision Medicine. (FDR = 4.2e-06, 6 genes); PMID (2013) Identification of human plasma proteins associated with the cell wall of the pathogenic fungus Paracoccidioides brasiliensis. (FDR = 4.2e-06, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08395.1 (F2, PLG, C3, APOA1; 4/43); huMAP3_09531.1 (F2, PLG, C3, APOA1; 4/47); huMAP3_10101.1 (F2, PLG, C3, APOA1; 4/49); huMAP3_15040.1 (PLG, SERPINC1, C3, APOA1; 4/64); huMAP3_10678.1 (F2, PLG, C3, APOA1; 4/71); huMAP3_08796.1 (F2, PLG; 2/15); huMAP3_07432.1 (C3, APOA1; 2/18); huMAP3_09832.1 (F2, PLG; 2/18); huMAP3_08224.1 (C3, APOA1; 2/21); huMAP3_07701.1 (F2, PLG; 2/22); huMAP3_09273.1 (F2, PLG; 2/28); huMAP3_09434.1 (C3, APOA1; 2/33)

### Novelty

The biological process represented by the module is not itself a new discovery: complement, coagulation, fibrinolysis, lipoprotein, and blood-microparticle relationships are already represented in STRING and hu.MAP, and the module's plasma-protein core is well established. A potentially novel aspect is the reproducible co-abundance of this particular gene set as a conserved module shared by cervix_uterine and ovary. However, the fact sheet alone does not establish that this tissue-pair module has not been reported previously, and absence of ALAD or MYLK from STRING or hu.MAP would not prove novelty. The most defensible conclusion is that this is a potentially novel tissue-pair co-abundance observation built largely from known circulating-protein biology, rather than a newly discovered molecular pathway.

**Hypothesis.** Hypothesis: the shared module primarily represents a circulating hepatic secretome and blood-microparticle signal present in both tissue sample types, with a biological overlay of local vascular injury or tissue-remodeling activity. In this model, C3 and CLU reflect complement and extracellular-particle regulation; F2, SERPINC1, PLG, and VTN jointly reflect thrombin generation, anticoagulant control, plasmin-mediated fibrinolysis, and matrix or adhesion interactions; APOA1 reflects HDL-associated transport; and MYLK may report contractile or vascular remodeling context. This hypothesis predicts that the module will track plasma exposure, vascularity, platelet or microparticle abundance, or tissue injury more strongly than resident epithelial or stromal cell abundance. It should be tested using matched plasma measurements, cell-resolved expression, histology, and sample-level adjustment for blood contamination.

### Important genes

#### F2

- **Related proteins** (co-abundance neighbors): APOA1 (0.91), ALAD (0.91), VTN (0.90); STRING partners: APOA1 (0.927), C3 (0.874), PLG (0.826), SERPINC1 (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07701.1, huMAP3_09273.1
- **Function (MyGene.info)**: coagulation factor II, thrombin. This gene encodes the prothrombin protein (also known as coagulation factor II). This protein is proteolytically cleaved in multiple steps to form the activated serine protease thrombin. The activated thrombin enzyme plays an important role in thrombosis and hemostasis by converting fibrinogen to fibrin during blood clot formation, by stimulating platelet aggregation, and by activating additional …
- **Diseases (Open Targets)**: congenital prothrombin deficiency (0.827); thrombophilia due to thrombin defect (0.738); venous thromboembolism (0.727); deep vein thrombosis (0.690); blood coagulation disease (0.670)
- **Europe PMC papers**: 109299
- **Why important**: F2 is a high-connectivity module node and is connected in STRING to APOA1, C3, PLG, and SERPINC1. It is the prothrombin gene, producing thrombin, and appears across the complement/coagulation, wound-response, hemostasis, fibrinolysis, receptor-regulatory, and stress-related primary terms, including (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 6.16e-08), (GO:BP regulation of wound healing; q_global = 0.000351), (GO:BP regulation of blood coagulation; q_global = 0.00154), (GO:BP regulation of fibrinolysis; q_global = 0.00432), (GO:BP fibrinolysis; q_global = 0.0169), and (GO:BP wound healing; q_global = 0.0305). HPA supports a liver and hepatocyte source and secretion to blood. Its extensive disease and literature evidence makes it the clearest mechanistic anchor for the module.
- **Conclusion**: Established evidence supports F2 as a central circulating coagulation and wound-response component of the module. Its co-abundance does not establish local thrombin activity in cervix_uterine or ovary; a blood-derived explanation remains plausible.

#### C3

- **Related proteins** (co-abundance neighbors): ALAD (0.90), MYLK (0.81), CLU (0.81); STRING partners: APOA1 (0.957), CLU (0.803), F2 (0.874), PLG (0.978), VTN (0.79)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_08224.1, huMAP3_09434.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a high-connectivity node linking ALAD, MYLK, and CLU in the module and has established STRING relationships with APOA1, CLU, F2, PLG, and VTN. It is the central complement component and contributes to the globally corrected complement, blood-microparticle, receptor-regulatory, endocytosis, and stress terms, including (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 6.16e-08), (GO:CC blood microparticle; q_global = 7.47e-07), (KEGG Neuroactive ligand-receptor interaction - Homo sapiens (human); q_global = 0.00752), and (GO:BP positive regulation of receptor-mediated endocytosis; q_global = 0.0169). HPA identifies liver enrichment, secretion to blood, and an association with non-classical monocytes. C3 has very extensive disease and literature support.
- **Conclusion**: Established evidence supports C3 as the complement and inflammatory arm of the plasma-associated module. Its connection to MYLK is a co-abundance relationship in this module, not evidence that C3 directly regulates MYLK.

#### PLG

- **Related proteins** (co-abundance neighbors): VTN (0.94); STRING partners: C3 (0.978), F2 (0.826), SERPINC1 (0.992), VTN (0.995)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07701.1, huMAP3_09273.1
- **Function (MyGene.info)**: plasminogen. The plasminogen protein encoded by this gene is a serine protease that circulates in blood plasma as an inactive zymogen and is converted to the active protease, plasmin, by several plasminogen activators such as tissue plasminogen activator (tPA), urokinase plasminogen activator (uPA), kallikrein, and factor XII (Hageman factor). The conversion of plasminogen to plasmin involves the cleavage of t…
- **Diseases (Open Targets)**: hypoplasminogenemia (0.813); hereditary angioedema (0.737); hemorrhage (0.605); dysplasminogenemia (0.598); Menorrhagia (0.579)
- **Europe PMC papers**: 17740
- **Why important**: PLG is a biochemical hub despite its limited direct module connectivity: it connects to VTN and has strong STRING relationships with C3, F2, SERPINC1, and VTN. It is the circulating plasminogen zymogen and contributes directly to fibrinolysis, blood coagulation, wound response, and the complement/coagulation pathway in (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 6.16e-08), (GO:BP regulation of wound healing; q_global = 0.000351), (GO:BP regulation of fibrinolysis; q_global = 0.00432), (GO:BP negative regulation of fibrinolysis; q_global = 0.00432), (GO:BP fibrinolysis; q_global = 0.0169), and (GO:BP wound healing; q_global = 0.0305). HPA supports liver and hepatocyte-associated expression and secretion to blood. Its substantial literature and disease evidence includes disorders of plasminogen and bleeding.
- **Conclusion**: Established evidence supports PLG as a key link between coagulation, fibrinolysis, extracellular-matrix remodeling, and wound repair. The module does not show whether PLG is activated locally or is simply being measured as circulating protein.

#### VTN

- **Related proteins** (co-abundance neighbors): PLG (0.94), F2 (0.90); STRING partners: APOA1 (0.755), C3 (0.79), CLU (0.962), PLG (0.995), SERPINC1 (0.949)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vitronectin. The protein encoded by this gene functions in part as an adhesive glycoprotein. Differential expression of this protein can promote either cell adhesion or migration as it links cells to the extracellular matrix through a variety of ligands. These ligands include integrins, plasminogen activator inhibitor-1, and urokinase plasminogen activator receptor. This secreted protein can be present in the …
- **Diseases (Open Targets)**: hypertensive disorder (0.421); dengue disease (0.376); neurodegenerative disease (0.343); temporal arteritis (0.338); age-related macular degeneration (0.313)
- **Europe PMC papers**: 3940
- **Why important**: VTN connects the module's fibrinolytic and coagulation components through PLG and F2 and has strong STRING relationships with PLG, SERPINC1, CLU, C3, and APOA1. It is a secreted adhesive glycoprotein that can link cells to extracellular matrix and interact with integrins and plasminogen-activation machinery. It contributes to the primary complement/coagulation, blood-microparticle, wound-healing, fibrinolysis, hemostasis, endocytosis, and vesicle-transport terms, including (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 6.16e-08), (GO:CC blood microparticle; q_global = 7.47e-07), (GO:BP regulation of wound healing; q_global = 0.000351), (GO:BP regulation of fibrinolysis; q_global = 0.00432), (GO:BP positive regulation of endocytosis; q_global = 0.00489), (GO:BP fibrinolysis; q_global = 0.0169), and (GO:BP wound healing; q_global = 0.0305). HPA supports liver enrichment and secretion to blood. Its literature volume is smaller than that of the principal coagulation factors but its network position is informative.
- **Conclusion**: Established evidence supports VTN as an extracellular adhesion and matrix-interface component that can connect circulating proteolysis with tissue repair. Its presence may indicate vascular or plasma exposure rather than a tissue-specific VTN program.

#### MYLK

- **Related proteins** (co-abundance neighbors): C3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin light chain kinase. This gene, a muscle member of the immunoglobulin gene superfamily, encodes myosin light chain kinase which is a calcium/calmodulin dependent enzyme. This kinase phosphorylates myosin regulatory light chains to facilitate myosin interaction with actin filaments to produce contractile activity. This gene encodes both smooth muscle and nonmuscle isoforms. In addition, using a separate promoter in an …
- **Diseases (Open Targets)**: aortic aneurysm, familial thoracic 7 (0.767); familial thoracic aortic aneurysm and aortic dissection (0.710); megacystis-microcolon-intestinal hypoperistalsis syndrome 1 (0.617); megacystis-microcolon-intestinal hypoperistalsis syndrome (0.597); Rare genetic vascular disease (0.483)
- **Europe PMC papers**: 10503
- **Why important**: MYLK is the distinctive non-secreted component of the module. It is linked to C3 in the co-abundance graph and contributes to globally corrected wound-healing, response-to-wounding, stress, transport, and vesicle-related terms, including (GO:BP regulation of wound healing; q_global = 0.000351), (GO:BP positive regulation of wound healing; q_global = 0.0006), (GO:BP regulation of response to stress; q_global = 0.000865), (GO:BP regulation of endocytosis; q_global = 0.0016), (GO:BP positive regulation of transport; q_global = 0.00786), (GO:BP regulation of vesicle-mediated transport; q_global = 0.0241), and (GO:BP wound healing; q_global = 0.0305). Its known function is calcium/calmodulin-dependent phosphorylation of myosin regulatory light chains, supporting smooth-muscle and non-muscle contractility, migration, and repair. HPA associates it with smooth muscle, hepatic stellate cells, megakaryocytes, platelets, basophils, and neutrophils. It has substantial literature and vascular-disease associations, despite lacking listed STRING or hu.MAP support here.
- **Conclusion**: Established evidence supports MYLK as a possible contractile, vascular, platelet-associated, or tissue-remodeling context marker. The proposed link between MYLK and the circulating complement/coagulation core is a hypothesis based on co-abundance and shared wound-response annotations, not an established physical interaction.

## Module 5

**Tissue pair**: cervix_uterine and ovary  
**Genes (23)**: ASCC3, CSTF2, DYNC1I2, DDX46, DBN1, EPS15L1, EZR, FASN, FEN1, HSPH1, EIF4G1, KLC1, PPP1R12A, NSUN2, PLEC, CTPS1, RCC1, RRM1, RUVBL2, SF3A1, YARS1, TRIP11, ZFR

### Function

The module is best interpreted as a broadly expressed cellular maintenance and proliferation-associated program, rather than as a tissue-specific pathway. Its genes span pre-mRNA splicing and RNA processing through SF3A1 and DDX46, translation initiation through EIF4G1, RNA modification through NSUN2, nucleotide production through RRM1 and CTPS1, DNA replication and repair through FEN1 and RRM1, protein-folding stress protection through HSPH1, and cytoskeletal or intracellular transport functions through genes such as EZR, PLEC, KLC1, and DYNC1I2. The central co-abundance pattern therefore plausibly reflects coordinated demand for RNA maturation, protein synthesis, nucleotide supply, genome maintenance, and cell-cycle competence. No GO or KEGG term passed global correction, so this functional interpretation is based on the individual gene annotations, network organization, STRING relationships, and hu.MAP evidence rather than on a globally significant enrichment term.

**Cell composition.** The module does not resemble a plasma-protein or secreted-protein module: only one member is annotated as secreted, and most members are intracellular. It also does not show a blood-cell signature; HPA reports low immune-cell specificity for nearly all genes, with no enriched blood-cell category. Most genes have low tissue specificity, and protein detection is common in both cervix_uterine and ovary, supporting a shared cellular program rather than a strongly tissue-restricted one. The HPA single-cell annotations are heterogeneous, including reproductive, epithelial, stromal, neural-associated, and progenitor populations. This heterogeneity, together with the broad-expression profile, means that the module could reflect a shared proliferative, biosynthetic, or stress-related state, or shared cell types in the samples, rather than a specialized cervix–ovary function. The lack of a plasma or immune composition argues against explaining the module primarily as blood contamination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a small set of high-confidence relationships within the module. The strongest known connection is SF3A1 with DDX46, consistent with spliceosome and U2-type prespliceosome functions. EIF4G1 connects with RRM1, and FEN1 connects with RRM1, linking translation initiation with nucleotide production and DNA synthesis or repair. hu.MAP independently places FEN1 and YARS1 together in several complexes (hu.MAP huMAP3_10302.1), (hu.MAP huMAP3_10115.1), and (hu.MAP huMAP3_13998.1), although each complex contains many additional proteins not in the module. SF3A1 and DDX46 co-occur in spliceosome-related complexes (hu.MAP huMAP3_04549.1), (hu.MAP huMAP3_06511.1), and (hu.MAP huMAP3_08980.1), again with only a small subset of each complex represented. These results support real biological anchors around RNA splicing and genome or nucleotide maintenance, but they do not establish that the entire module is one physical complex. The sparse STRING connectivity and partial hu.MAP membership suggest that the co-abundance structure is broader than the currently catalogued direct interactions.

**STRING interactions (score >= 0.7)**: 3 of 253 gene pairs: DDX46–SF3A1 (0.999); EIF4G1–RRM1 (0.83); FEN1–RRM1 (0.766)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10302.1 (FEN1, YARS1; 2/9); huMAP3_10115.1 (FEN1, YARS1; 2/14); huMAP3_13998.1 (FEN1, YARS1; 2/23); huMAP3_04549.1 (SF3A1, DDX46; 2/52); huMAP3_06511.1 (SF3A1, DDX46; 2/79); huMAP3_08980.1 (SF3A1, DDX46; 2/97)

### Novelty

This is a potentially interesting cross-tissue co-abundance finding, but it cannot be called a newly discovered molecular complex or a definitively novel pathway. The absence of a globally significant GO or KEGG term and the limited STRING connectivity make the module difficult to assign to a canonical pathway. Conversely, absence from STRING or hu.MAP is not evidence of novelty, because co-abundance can arise from shared regulation, cell-state composition, indirect pathway coordination, or context-specific interactions that are not represented in those resources. The most defensible conclusion is that the shared cervix_uterine–ovary co-abundance pattern may be novel as a dataset-level observation, while its component biology is largely established and distributed across several cellular systems. Replication in independent cohorts, cell-type-aware analysis, and perturbation or interaction experiments would be needed to establish genuine mechanistic novelty.

**Hypothesis.** Hypothesis: the module represents a coordinated biosynthetic and genome-protection state shared by particular cell populations in cervix_uterine and ovary. Increased RNA processing and translation capacity, supported by DDX46, SF3A1, NSUN2, and EIF4G1, may accompany increased nucleotide production and DNA replication or repair supported by CTPS1, RRM1, and FEN1. HSPH1 may buffer the proteotoxic burden of this state, while cytoskeletal and transport genes may support the associated changes in cell architecture and intracellular trafficking. The observed pattern could therefore arise when related epithelial, stromal, reproductive, or proliferative cell states are represented in both tissues. This is a hypothesis from co-abundance and annotations, not evidence that these proteins act together in one physical complex.

### Important genes

#### SF3A1

- **Related proteins** (co-abundance neighbors): FEN1 (0.86), DDX46 (0.85), EIF4G1 (0.84), DBN1 (0.82); STRING partners: DDX46 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_04549.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 is a central network node and has a direct high-confidence STRING relationship with DDX46. Its established function as a component of the U2 snRNP and spliceosome provides a strong anchor for the RNA-processing interpretation. It is also present in the spliceosome-related hu.MAP complexes (hu.MAP huMAP3_04549.1), (hu.MAP huMAP3_06511.1), and (hu.MAP huMAP3_08980.1), and its protein is detected in both tissues. Its disease associations and substantial literature record show that it is well studied, although the shared tissue module may still reveal a context-specific abundance relationship.
- **Conclusion**: Established evidence supports SF3A1 as a core pre-mRNA-splicing component and as one of the best-supported molecular anchors of this module. The hypothesis that its coordinated abundance with the other module genes marks increased splicing demand in shared cervix–ovary cell states remains untested.

#### DDX46

- **Related proteins** (co-abundance neighbors): NSUN2 (0.86), SF3A1 (0.85), EIF4G1 (0.83), HSPH1 (0.82); STRING partners: SF3A1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_04549.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: DEAD-box helicase 46. This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribu…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); dengue disease (0.370); Hypercholesterolemia (0.203); lung adenocarcinoma (0.074); osteosarcoma (0.053)
- **Europe PMC papers**: 592
- **Why important**: DDX46 is connected to several of the module's higher-centrality genes and has the strongest STRING relationship in the module with SF3A1. Its established DEAD-box helicase function in RNA structure remodeling, mRNA splicing, and U2-type prespliceosome assembly directly complements the SF3A1 annotation. Its presence with SF3A1 in (hu.MAP huMAP3_04549.1), (hu.MAP huMAP3_06511.1), and (hu.MAP huMAP3_08980.1) gives independent complex-level support, while its detection in both tissues supports relevance to the shared module rather than one tissue alone.
- **Conclusion**: Established evidence identifies DDX46 as an RNA-processing and prespliceosome factor that likely explains part of the module's coherent core. It is a plausible marker of coordinated RNA maturation, but the data do not prove that DDX46 drives the module or that its abundance changes cause the tissue similarity.

#### FEN1

- **Related proteins** (co-abundance neighbors): SF3A1 (0.86), RRM1 (0.85), CSTF2 (0.83), HSPH1 (0.82), CTPS1 (0.81); STRING partners: RRM1 (0.766)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_10302.1, huMAP3_10115.1, huMAP3_13998.1
- **Function (MyGene.info)**: flap structure-specific endonuclease 1. The protein encoded by this gene removes 5' overhanging flaps in DNA repair and processes the 5' ends of Okazaki fragments in lagging strand DNA synthesis. Direct physical interaction between this protein and AP endonuclease 1 during long-patch base excision repair provides coordinated loading of the proteins onto the substrate, thus passing the substrate from one enzyme to another. The protein is…
- **Diseases (Open Targets)**: neurodegenerative disease (0.496); HIV infectious disease (0.370); hepatocellular carcinoma (0.213); breast carcinoma (0.213); oral cavity squamous cell carcinoma (0.208)
- **Europe PMC papers**: 5275
- **Why important**: FEN1 is a highly connected module member linking the spliceosome-associated branch with RRM1, HSPH1, CTPS1, and CSTF2. Its established role in Okazaki-fragment processing and base-excision repair provides a mechanistic bridge from nucleotide supply to genome maintenance. It has a direct STRING relationship with RRM1 and occurs with YARS1 in hu.MAP complexes (hu.MAP huMAP3_10302.1), (hu.MAP huMAP3_10115.1), and (hu.MAP huMAP3_13998.1). It is detected in both tissues and has extensive literature and disease-association evidence.
- **Conclusion**: Established evidence supports FEN1 as a genome-replication and DNA-repair component and as an important connector between module branches. The hypothesis that the module reflects a shared state of replication or repair demand is biologically plausible, but enrichment and co-abundance alone cannot establish active DNA damage or cell-cycle progression.

#### RRM1

- **Related proteins** (co-abundance neighbors): FEN1 (0.85), CTPS1 (0.81), FASN (0.81), RCC1 (0.81); STRING partners: EIF4G1 (0.83), FEN1 (0.766)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribonucleotide reductase catalytic subunit M1. This gene encodes the large and catalytic subunit of ribonucleotide reductase, an enzyme essential for the conversion of ribonucleotides into deoxyribonucleotides. A pool of available deoxyribonucleotides is important for DNA replication during S phase of the cell cycle as well as multiple DNA repair processes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec …
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.618); B-cell chronic lymphocytic leukemia (0.595); exocrine pancreatic carcinoma (0.584); sickle cell disease (0.581); ovarian carcinoma (0.571)
- **Europe PMC papers**: 5033
- **Why important**: RRM1 occupies a key network position at the intersection of FEN1, CTPS1, FASN, RCC1, and EIF4G1. Its established catalytic role in ribonucleotide reduction supplies deoxyribonucleotides for DNA replication and repair. The STRING relationships with EIF4G1 and FEN1 provide direct support for a connection between biosynthetic capacity, translation-related state, and genome maintenance. RRM1 is detected in both tissues and has substantial disease and cancer literature, including an ovarian carcinoma association in the supplied evidence.
- **Conclusion**: Established evidence makes RRM1 a strong candidate for the module's nucleotide-supply and genome-maintenance axis. Its abundance may report proliferative or repair-related demand, but the present module does not distinguish those possibilities or demonstrate a causal role for RRM1 in tissue-specific biology.

#### EIF4G1

- **Related proteins** (co-abundance neighbors): NSUN2 (0.88), SF3A1 (0.84), DDX46 (0.83), RCC1 (0.83), KLC1 (0.83); STRING partners: RRM1 (0.83)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 is a well-connected module member linking NSUN2, SF3A1, DDX46, RCC1, KLC1, and RRM1. As a scaffold of the EIF4F complex, it is established as an important factor in cap-dependent translation initiation and mRNA recruitment to ribosomes. Its direct STRING relationship with RRM1 supports a possible connection between protein synthesis and nucleotide or DNA metabolism. It is detected in both tissues and has a large literature base with disease associations.
- **Conclusion**: Established evidence supports EIF4G1 as the module's translation-initiation anchor and as a plausible indicator of general biosynthetic activity. A coordinated translation and DNA-maintenance state is a reasonable hypothesis, but the module does not show that EIF4G1 specifically regulates the other genes.

#### NSUN2

- **Related proteins** (co-abundance neighbors): EIF4G1 (0.88), ZFR (0.87), DDX46 (0.86), RCC1 (0.82), TRIP11 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP2/Sun RNA methyltransferase 2. This gene encodes a methyltransferase that catalyzes the methylation of cytosine to 5-methylcytosine (m5C) at position 34 of intron-containing tRNA(Leu)(CAA) precursors. This modification is necessary to stabilize the anticodon-codon pairing and correctly translate the mRNA. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Mar…
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.694); hereditary disease (0.518); Intellectual disability (0.489); phenylketonuria (0.470); neurodegenerative disease (0.462)
- **Europe PMC papers**: 2458
- **Why important**: NSUN2 is a network connector linking EIF4G1, ZFR, DDX46, RCC1, and TRIP11. Its established RNA methyltransferase activity in tRNA modification, together with roles in rRNA and mRNA processing and export, connects RNA maturation with translational capacity. It is detected in cervix_uterine and not detected in ovary by the supplied HPA protein summary, which makes it informative but also cautions against treating it as a universally shared protein-level feature. It has substantial literature and disease-association evidence.
- **Conclusion**: Established evidence supports NSUN2 as an RNA-modification and RNA-processing factor that could connect the module's post-transcriptional and translational features. The tissue-asymmetric HPA detection means that its role in the shared co-abundance signal should be tested at the protein and cell-type levels rather than assumed from the module alone.

## Module 6

**Tissue pair**: cervix_uterine and ovary  
**Genes (20)**: ATXN2L, BAG3, BYSL, CDC73, DDX21, ADAR, GOPC, HBS1L, CAST, MYBBP1A, NOP2, NUP98, PRRC2C, RBM22, RBM39, U2SURP, UBTF, UBR5, ZC3H4, ZNF326

### Function

This is a nuclear RNA and nucleic-acid metabolism module. The primary evidence is the globally corrected enrichment for RNA binding (GO:MF RNA binding; q_global = 0.00618), RNA metabolic process (GO:BP RNA metabolic process; q_global = 0.016), nucleic-acid metabolic process (GO:BP nucleic acid metabolic process; q_global = 0.0163), RNA processing (GO:BP RNA processing; q_global = 0.0225), and protein import into the nucleus (GO:BP protein import into nucleus; q_global = 0.0493). The gene composition supports a coordinated RNA-handling program spanning RNA editing, RNA helicase activity, RNA splicing, RNA surveillance, nucleolar ribosome biogenesis, transcriptional regulation, and nucleocytoplasmic transport. DDX21, NOP2, MYBBP1A, BYSL, and UBTF point particularly strongly toward nucleolar RNA and ribosome-related activity, while ADAR, RBM22, RBM39, U2SURP, ZNF326, and ZC3H4 support RNA processing and transcriptional control. The module therefore most plausibly represents a conserved nuclear RNA-processing and ribosome-biogenesis state rather than a pathway restricted to either reproductive tissue.

**Cell composition.** The module is not dominated by secreted or plasma proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and protein detection is frequent in both cervix_uterine and ovary, which is consistent with a broadly expressed intracellular program. The module is also not strongly blood-cell specific according to HPA, although several genes show enhancement in neutrophils or erythrocyte progenitors and one shows immune-cell enhancement. These signals could reflect shared cell populations or sample composition in part, but they do not support interpreting the module primarily as a blood or plasma signature. HPA localization and the gene annotations instead emphasize nucleoli, nucleoplasm, nuclear speckles, nuclear bodies, and related intracellular compartments.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF RNA binding | 0.00618 | ADAR, ATXN2L, BYSL, DDX21, MYBBP1A, NOP2, NUP98, PRRC2C, RBM22, RBM39, U2SURP, UBR5, UBTF, ZC3H4, ZNF326 |
| GO:BP RNA metabolic process | 0.016 | ADAR, ATXN2L, BYSL, CDC73, DDX21, HBS1L, MYBBP1A, NOP2, NUP98, RBM22, RBM39, U2SURP, UBTF, ZC3H4, ZNF326 |
| GO:BP nucleic acid metabolic process | 0.0163 | ADAR, ATXN2L, BYSL, CDC73, DDX21, HBS1L, MYBBP1A, NOP2, NUP98, RBM22, RBM39, U2SURP, UBR5, UBTF, ZC3H4, ZNF326 |
| GO:BP RNA processing | 0.0225 | ADAR, BYSL, CDC73, DDX21, NOP2, NUP98, RBM22, RBM39, U2SURP, ZNF326 |
| GO:BP protein import into nucleus | 0.0493 | ADAR, BAG3, NUP98, RBM22, UBR5 |

### STRING and hu.MAP

STRING supports a compact, biologically coherent nucleolar and RNA-associated core. The strongest reported links connect DDX21 with MYBBP1A and NOP2, MYBBP1A with NOP2 and UBTF, and BYSL with NOP2 and MYBBP1A; DDX21 also connects with RBM39. These known relationships support the interpretation that part of the co-abundance structure reflects established RNA and ribosome-related biology rather than an arbitrary gene grouping. STRING supplementary terms also support RNA binding, nucleic-acid binding, and ubiquitin or isopeptide-related functions (4 supplementary STRING terms; within-query FDR 0.00016–0.00063), but these are not global enrichment evidence. hu.MAP provides one overlapping complex containing ADAR and ZNF326 (hu.MAP huMAP3_10625.1), while the other module genes are not represented in a reported hu.MAP overlap. Thus, the module contains a recognized nucleolar and RNA-processing core, but the complete cross-tissue co-abundance pattern is not explained by one already catalogued complex.

**STRING interactions (score >= 0.7)**: 7 of 190 gene pairs: BYSL–MYBBP1A (0.73); BYSL–NOP2 (0.915); DDX21–MYBBP1A (0.963); DDX21–NOP2 (0.761); DDX21–RBM39 (0.724); MYBBP1A–NOP2 (0.864); MYBBP1A–UBTF (0.768)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Isopeptide bond (FDR = 0.00016, 14 genes); Function RNA binding (FDR = 0.00038, 16 genes); Function Nucleic acid binding (FDR = 0.00063, 17 genes); Keyword Ubl conjugation (FDR = 0.00063, 14 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10625.1 (ADAR, ZNF326; 2/57)

### Novelty

The module should not be called entirely novel, because several of its relationships and functions are established: the DDX21–MYBBP1A–NOP2 and MYBBP1A–UBTF relationships are supported by STRING, and ADAR with ZNF326 occurs in a hu.MAP complex (hu.MAP huMAP3_10625.1). The globally corrected enrichment also recovers well-established RNA biology (5 globally significant GO/KEGG terms, q_global 0.00618–0.0493; see the table). Nevertheless, the shared cervix_uterine–ovary co-abundance module may represent a new tissue-pair-level organization of these genes, especially because only part of the network is covered by known interaction resources and the hu.MAP overlap is limited. Absence from STRING or hu.MAP is not evidence of novelty by itself. A defensible conclusion is that the molecular functions are established, whereas the particular conserved co-abundance configuration and its relevance across these tissues remain potentially novel and require validation.

**Hypothesis.** Hypothesis: the module reflects coordinated demand for nuclear RNA production, maturation, quality control, and ribosome-related activity in a shared cellular state present in cervix_uterine and ovary. In this model, UBTF, MYBBP1A, BYSL, NOP2, and DDX21 support nucleolar transcription, rRNA processing, ribosome assembly, and nucleolar organization; ADAR, RBM22, RBM39, U2SURP, and ZNF326 coordinate RNA editing, splicing, and RNA-associated transcriptional regulation; NUP98 links the program to nuclear transport; and UBR5, BAG3, PRRC2C, and ATXN2L may connect RNA metabolism with protein quality control or stress-responsive regulation. The shared signal could therefore arise from a conserved proliferative, biosynthetic, or differentiation-associated intracellular state rather than from a cervix- or ovary-specific secreted program. This hypothesis should be tested with cell-resolved measurements, perturbation of the nucleolar and splicing components, and independent replication in samples with controlled cellular composition.

### Important genes

#### DDX21

- **Related proteins** (co-abundance neighbors): ZNF326 (0.89), UBR5 (0.87), NOP2 (0.85), MYBBP1A (0.84), BAG3 (0.83), U2SURP (0.83), BYSL (0.80); STRING partners: MYBBP1A (0.963), NOP2 (0.761), RBM39 (0.724)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 is the strongest network-connected member in the reported subgraph and links several module components, including ZNF326, UBR5, NOP2, MYBBP1A, BAG3, U2SURP, and BYSL. It is present in the primary RNA-binding, RNA-metabolism, nucleic-acid-metabolism, and RNA-processing terms (4 globally significant GO/KEGG terms, q_global 0.00618–0.0225; see the table). Its annotated DEAD-box helicase function is directly compatible with remodeling RNA structures, ribosome or spliceosome assembly, and nucleolar activity. It also has strong STRING support with MYBBP1A, NOP2, and RBM39. Its disease literature is substantial, with reported links to neurodegenerative disease and several cancers.
- **Conclusion**: Established evidence supports DDX21 as a central RNA-helicase and nucleolar connector in this module. It is a plausible organizing hub, but co-abundance does not establish that DDX21 drives the module or causes the associated disease links.

#### NOP2

- **Related proteins** (co-abundance neighbors): MYBBP1A (0.88), DDX21 (0.85); STRING partners: BYSL (0.915), DDX21 (0.761), MYBBP1A (0.864)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP2 nucleolar protein. Enables RNA binding activity. Involved in positive regulation of cell population proliferation; regulation of signal transduction by p53 class mediator; and ribosomal large subunit assembly. Located in nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.273); nonpapillary renal cell carcinoma (0.097); neoplasm (0.097); cancer (0.091); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 2120
- **Why important**: NOP2 is part of the dense STRING-supported nucleolar core with BYSL, DDX21, and MYBBP1A. It is included in (4 globally significant GO/KEGG terms, q_global 0.00618–0.0225; see the table), is localized to nucleoli, and is annotated for rRNA processing, ribosomal large-subunit assembly, and ribosome biogenesis. Its position in the nucleolar core gives it a direct mechanistic connection to the module-level RNA and biosynthetic interpretation. It also has a substantial literature base and disease associations involving neurodegenerative disease and neoplasia.
- **Conclusion**: Established evidence identifies NOP2 as a plausible marker of nucleolar RNA maturation and ribosome production within the module. Its role as a causal regulator of the shared tissue-pair pattern remains a hypothesis.

#### ADAR

- **Related proteins** (co-abundance neighbors): UBTF (0.87), U2SURP (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_10625.1
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR is present in every primary enrichment category (5 globally significant GO/KEGG terms, q_global 0.00618–0.0493; see the table), including protein import into the nucleus, and is also represented in all supplementary STRING terms (4 supplementary STRING terms; within-query FDR 0.00016–0.00063). Its established function is site-specific adenosine-to-inosine RNA editing, with effects on double-stranded RNA and antiviral responses. It connects to UBTF and U2SURP in the module and shares a hu.MAP complex with ZNF326 (hu.MAP huMAP3_10625.1). It is detected in both tissues and has extensive literature and disease associations involving Aicardi–Goutières syndrome, dyschromatosis symmetrica hereditaria, and interferonopathy.
- **Conclusion**: Established evidence supports ADAR as the module's most distinctive RNA-editing component and as a bridge between RNA processing and nuclear organization. Whether altered ADAR activity explains the shared co-abundance state is not established by this network.

#### NUP98

- **Related proteins** (co-abundance neighbors): GOPC (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 98 and 96 precursor. Nuclear pore complexes (NPCs) regulate the transport of macromolecules between the nucleus and cytoplasm, and are composed of many polypeptide subunits, many of which belong to the nucleoporin family. This gene belongs to the nucleoporin gene family and encodes a 186 kDa precursor protein that undergoes autoproteolytic cleavage to generate a 98 kDa nucleoporin and 96 kDa nucleoporin. The 98 kDa nu…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); acute myeloid leukemia (0.399); lung carcinoma (0.376)
- **Europe PMC papers**: 4839
- **Why important**: NUP98 appears in all primary terms (5 globally significant GO/KEGG terms, q_global 0.00618–0.0493; see the table) and is annotated for RNA export, protein import into the nucleus, nucleocytoplasmic transport, nuclear-pore organization, and peripheral RNA polymerase tethering. Its module connection to GOPC provides a transport-associated branch distinct from the nucleolar core. NUP98 also has extensive literature and disease associations involving viral infection, acute myeloid leukemia, and lung carcinoma.
- **Conclusion**: Established evidence supports NUP98 as the module's nuclear-transport component, linking RNA processing with movement of macromolecules across the nuclear envelope. A specific transport defect or tissue-specific NUP98 mechanism is only a hypothesis.

#### RBM39

- **Related proteins** (co-abundance neighbors): ZNF326 (0.84); STRING partners: DDX21 (0.724)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 39. This gene encodes a member of the U2AF65 family of proteins. The encoded protein is found in the nucleus, where it co-localizes with core spliceosomal proteins. It has been shown to play a role in both steroid hormone receptor-mediated transcription and alternative splicing, and it is also a transcriptional coregulator of the viral oncoprotein v-Rel. Multiple transcript variants have been observed…
- **Diseases (Open Targets)**: neurodegenerative disease (0.401); endometrial cancer (0.220); skin neoplasm (0.217); skin cancer (0.217); actinic keratosis (0.217)
- **Europe PMC papers**: 1169
- **Why important**: RBM39 is included in all primary RNA-related terms (4 globally significant GO/KEGG terms, q_global 0.00618–0.0225; see the table) and all supplementary STRING categories (4 supplementary STRING terms; within-query FDR 0.00016–0.00063). It is a nuclear RNA-binding and splicing-associated protein that also participates in steroid-hormone-receptor transcriptional regulation, making it especially relevant to reproductive tissues. It connects to ZNF326 in the module and to DDX21 in STRING. Its literature includes RNA processing, transcriptional regulation, neurodegenerative disease, and endometrial or skin neoplasia.
- **Conclusion**: Established evidence supports RBM39 as a nuclear splicing and transcriptional co-regulator that may help connect the conserved RNA program to reproductive-tissue regulatory states. Its possible role in coordinating the cervix_uterine–ovary module is a hypothesis rather than a demonstrated tissue-specific mechanism.

## Module 7

**Tissue pair**: cervix_uterine and ovary  
**Genes (8)**: ECI1, PRDX3, RAB21, RAB3D, SFXN1, SSR1, STX7, VDAC2

### Function

The module does not have a statistically significant GO or KEGG annotation: no globally significant GO/KEGG term passed global correction. It also has no supplementary STRING enrichment. Its gene-level pattern nevertheless suggests a mixed intracellular-trafficking and mitochondrial-maintenance program. RAB3D, RAB21, and STX7 support regulated secretion, endosomal trafficking, vesicle fusion, and lysosome or phagosome-related transport. VDAC2, ECI1, SFXN1, and PRDX3 support mitochondrial metabolite transport, fatty-acid oxidation, serine transport, and antioxidant protection. SSR1 adds an endoplasmic-reticulum protein-targeting component. The network therefore appears biologically heterogeneous rather than a sharply defined pathway, with vesicle trafficking connected to mitochondrial metabolism and stress control through VDAC2 and the RAB proteins. These are functional interpretations of individual genes and network structure, not evidence of globally enriched ontology terms.

**Cell composition.** The module contains no secreted genes, so it is not a plasma-protein or secretome module. Most genes have low tissue specificity, and the HPA data show cell-type enhancement for most of the genes. Neutrophils or neutrophil progenitors recur among the enriched cell types, while several genes also show enrichment in hepatocytes, basophils, monocytes, or other immune-related populations. STX7 has broad blood-cell group enrichment, and RAB3D is associated with neutrophils and neutrophil progenitors. This composition raises the possibility that the shared cervix and ovary signal partly reflects immune-cell abundance or another shared cell-type component rather than a tissue-specific reproductive program. Protein detection is complete in cervix but only partial in ovary, which also argues for caution when interpreting the module as a uniformly active ovary program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a high-confidence relationship between PRDX3 and VDAC2, and there is no STRING functional enrichment. The co-abundance network contains additional strong statistical associations, including links among RAB3D, RAB21, SSR1, STX7, VDAC2, ECI1, SFXN1, and PRDX3, but these co-abundance links should not be treated as established physical interactions. hu.MAP contains no complex with multiple module members. Thus, the module has limited support from established interaction or complex databases. The PRDX3–VDAC2 relationship supports a mitochondrial redox or outer-membrane connection, whereas the trafficking-related relationships remain primarily co-abundance observations in this dataset.

**STRING interactions (score >= 0.7)**: 1 of 28 gene pairs: PRDX3–VDAC2 (0.709)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a new tissue-pair co-abundance pattern, but the available evidence does not establish a new molecular complex, pathway, or mechanism. The absence of a hu.MAP complex and the sparse STRING support are compatible with novelty, yet database absence alone cannot prove that the module is novel. The mixed annotations, lack of globally significant GO or KEGG terms, lack of STRING enrichment, and possible immune-cell contribution make it more appropriate to describe this as a potentially novel association pattern requiring replication rather than as a newly discovered biological process. Direct comparison with prior cervix–ovary co-abundance studies and independent cohorts would be needed to support a stronger novelty claim.

**Hypothesis.** Hypothesis: the shared module reflects coordinated variation in vesicle and endolysosomal trafficking together with mitochondrial metabolic and oxidative-stress state, potentially driven in part by shared immune-cell composition in cervix and ovary samples. In this model, RAB3D, RAB21, SSR1, and STX7 represent trafficking and membrane-delivery activity, while VDAC2, ECI1, SFXN1, and PRDX3 represent mitochondrial transport, lipid oxidation, amino-acid import, and redox protection. The apparent coupling could arise from activated or changing immune-cell populations, from a common epithelial or stromal state, or from genuine coordination between secretory trafficking and mitochondrial stress adaptation. This hypothesis should be tested with cell-deconvolution or single-cell data, protein-level measurements, and perturbation experiments; the current module alone does not distinguish these explanations.

### Important genes

#### RAB3D

- **Related proteins** (co-abundance neighbors): RAB21 (0.89), SSR1 (0.87), STX7 (0.86), VDAC2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB3D, member RAS oncogene family. Enables myosin V binding activity. Involved in bone resorption and positive regulation of regulated secretory pathway. Located in cytoplasmic microtubule and secretory vesicle. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypertensive disorder (0.148); neoplasm (0.094); cancer (0.079); central nervous system cancer (0.075); glioma (0.075)
- **Europe PMC papers**: 854
- **Why important**: RAB3D is the most connected trafficking-associated node in the module and links RAB21, SSR1, STX7, and VDAC2. Its established functions include regulated exocytosis, secretory-vesicle biology, and myosin V binding. HPA associates it with neutrophils and neutrophil progenitors, while its tissue enhancement in pancreas and skin suggests that the signal may reflect cell composition rather than a cervix–ovary-specific process. It has substantial literature and reported associations with neoplasm and hypertension-related disease.
- **Conclusion**: Established evidence supports RAB3D as a central vesicle-trafficking gene and as a plausible marker of a cell-type or secretory-state component. It is hypothesized, but not demonstrated, to connect trafficking activity with the mitochondrial part of this module through its co-abundance relationship with VDAC2.

#### RAB21

- **Related proteins** (co-abundance neighbors): RAB3D (0.89), VDAC2 (0.85), SFXN1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB21, member RAS oncogene family. This gene belongs to the Rab family of monomeric GTPases, which are involved in the control of cellular membrane traffic. The encoded protein plays a role in the targeted trafficking of integrins via its association with integrin alpha tails. As a consequence, the encoded protein is involved in the regulation of cell adhesion and migration. Expression of this gene is associated with a poor prognos…
- **Diseases (Open Targets)**: neurodegenerative disease (0.469); small intestine neuroendocrine neoplasm (0.095); neoplasm (0.085); posterior cortical atrophy (0.074); nonpapillary renal cell carcinoma (0.065)
- **Europe PMC papers**: 999
- **Why important**: RAB21 is a highly connected module node linking RAB3D and VDAC2 with SFXN1. It is an established Rab-family regulator of intracellular membrane traffic, integrin targeting, cell adhesion, migration, receptor-mediated endocytosis, and exocytosis. HPA reports enhancement in neutrophils as well as spermatid populations. Its disease associations include neurodegenerative disease and neoplasm, and it has substantial literature.
- **Conclusion**: Established evidence supports RAB21 as a membrane-trafficking and adhesion regulator that could explain part of the module's shared structure. The proposed link from RAB21 to mitochondrial amino-acid transport through SFXN1 is a hypothesis based on co-abundance, not an established physical or regulatory interaction.

#### VDAC2

- **Related proteins** (co-abundance neighbors): RAB21 (0.85), ECI1 (0.82), RAB3D (0.82); STRING partners: PRDX3 (0.709)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: voltage dependent anion channel 2. This gene encodes a member of the voltage-dependent anion channel pore-forming family of proteins that are considered the main pathway for metabolite diffusion across the mitochondrial outer membrane. The encoded protein is also thought to be involved in the mitochondrial apoptotic pathway via regulation of BCL2-antagonist/killer 1 protein activity. Pseudogenes have been identified on chromosomes …
- **Diseases (Open Targets)**: neurodegenerative disease (0.345); alcohol drinking (0.204); atrial fibrillation (0.175); major depressive disorder (0.143); severe combined immunodeficiency (0.118)
- **Europe PMC papers**: 2914
- **Why important**: VDAC2 occupies a bridging position between the RAB trafficking genes and the mitochondrial genes ECI1 and PRDX3. It is an established mitochondrial outer-membrane channel involved in metabolite diffusion, transmembrane transport, phospholipid translocation, and mitochondrial apoptotic regulation. It is also the partner in the module's supported STRING relationship with PRDX3. Its literature is extensive, and disease associations include neurodegenerative and cardiovascular conditions.
- **Conclusion**: Established evidence supports VDAC2 as the strongest candidate for connecting mitochondrial function with the trafficking-associated part of the module. The hypothesis that it organizes a shared vesicle–mitochondrial state in these tissues remains unproven because hu.MAP does not identify a corresponding complex and the module has no globally significant enrichment.

#### PRDX3

- **Related proteins** (co-abundance neighbors): ECI1 (0.81); STRING partners: VDAC2 (0.709)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Mitochondria; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peroxiredoxin 3. This gene encodes a mitochondrial protein with antioxidant function. The protein is similar to the C22 subunit of Salmonella typhimurium alkylhydroperoxide reductase, and it can rescue bacterial resistance to alkylhydroperoxide in E. coli that lack the C22 subunit. The human and mouse genes are highly conserved, and they map to the regions syntenic between mouse and human chromosomes. Sequence com…
- **Diseases (Open Targets)**: spinocerebellar ataxia, autosomal recessive 32 (0.653); corneal dystrophy, punctiform and polychromatic pre-descemet (0.571); autosomal recessive cerebellar ataxia (0.268); neurodegenerative disease (0.257); hereditary disease (0.191)
- **Europe PMC papers**: 2613
- **Why important**: PRDX3 is a mitochondrial antioxidant protein connected to ECI1 in the co-abundance network and to VDAC2 in STRING. Its established functions include response to oxidative stress and mitochondrial organization. HPA shows enhancement in hepatocytes and trophoblast-related cell types, with low blood-cell specificity. It has substantial literature and reported associations with inherited neurodegenerative and corneal disorders.
- **Conclusion**: Established evidence supports PRDX3 as a marker of mitochondrial redox protection and oxidative-stress handling. Its relationship with VDAC2 is supported by STRING, but its connection to ECI1 in this module is only a co-abundance observation. A shared oxidative-stress response is therefore plausible but remains a hypothesis.

#### STX7

- **Related proteins** (co-abundance neighbors): SSR1 (0.87), RAB3D (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Lysosomes; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntaxin 7. The protein encoded by this gene is a syntaxin family membrane receptor involved in vesicle transport. The encoded protein binds alpha-SNAP, an important regulator of transport vesicle fusion. Along with syntaxin 13, this protein plays a role in the ordered fusion of endosomes and lysosomes with the phagosome. [provided by RefSeq, May 2016].
- **Diseases (Open Targets)**: neurodegenerative disease (0.489); Abnormality of neuronal migration (0.259); Raynaud disease (0.180); placental abruption (0.166); aortic stenosis (0.081)
- **Europe PMC papers**: 701
- **Why important**: STX7 is a lysosomal syntaxin involved in vesicle transport, vesicle fusion, and ordered fusion of endosomes and lysosomes with phagosomes. It is connected to RAB3D and SSR1 and shows broad blood-cell group enrichment, including myeloid and lymphoid populations. This makes it especially informative for distinguishing a genuine tissue program from immune-cell or phagolysosomal composition. Its disease and cell-biology literature is substantial.
- **Conclusion**: Established evidence supports STX7 as a vesicle-fusion and phagolysosomal trafficking marker. Its HPA blood-cell pattern strengthens the hypothesis that immune-cell abundance contributes to the shared module. It does not by itself establish that the module represents a coordinated cervix–ovary trafficking pathway.

## Module 8

**Tissue pair**: cervix_uterine and ovary  
**Genes (6)**: EIF2A, PPM1G, SMC4, RARS1, TANC1, YTHDF2

### Function

The module appears to combine intracellular processes rather than represent one established pathway. Its network links PPM1G with EIF2A, RARS1, and SMC4, while EIF2A connects to YTHDF2 and SMC4 connects to TANC1. The annotations collectively point to regulation of protein phosphorylation and pre-mRNA splicing through PPM1G, translation and aminoacyl-tRNA charging through EIF2A and RARS1, RNA turnover through YTHDF2, and chromosome condensation or segregation through SMC4. TANC1 contributes a predicted role in postsynapse organization. No GO or KEGG term passed global correction. Thus, the most defensible interpretation is a coordinated abundance pattern involving translation, RNA regulation, cell-cycle or chromosome biology, and tissue or cell-state composition, rather than a validated single functional pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of the members is annotated as secreted. Most members have low tissue specificity and low immune-cell specificity, while two show tissue enhancement and several show cell-type enhancement. PPM1G is tissue enhanced in testis and group enriched in spermatogenic cell types; SMC4 is tissue enhanced in lymphoid tissue and enhanced in several progenitor or spermatogenic populations; YTHDF2 is enhanced in syncytiotrophoblasts; and TANC1 is enhanced in several specialized nonimmune cell types. SMC4 is immune-cell enhanced in basophils, but the remaining members have low immune-cell specificity or are not detected in immune cells. Protein detection is present for most members in both cervix_uterine and ovary, with some tissue-specific absence for individual genes. The shared module could therefore reflect broadly expressed intracellular proteins combined with shared or varying cell states, including reproductive, progenitor, or lymphoid contributions, rather than blood contamination alone.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was present among the module pairs, and there was no STRING functional-enrichment result. No hu.MAP complex contained multiple module members. Consequently, the co-abundance edges are not supported here by previously catalogued physical interactions or a recognized multiprotein complex. The absence of these records does not mean that the proteins cannot influence one another; it indicates that this module is primarily a co-abundance observation and that its molecular connectivity remains unestablished.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a novel tissue-pair co-abundance pattern, because it links proteins from translation, RNA regulation, phosphorylation, chromosome organization, and a predicted neuronal or postsynaptic protein without support from STRING or hu.MAP. However, it should not be called a newly discovered molecular mechanism. The individual genes and their broad functions are already established, and the module has no globally significant GO or KEGG annotation. Its novelty is therefore best stated as a potentially new association of coordinated abundance across cervix_uterine and ovary, requiring replication, cell-composition adjustment, and experimental testing.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular state in which translational capacity and RNA fate are coordinated with phosphorylation-dependent control of RNA processing and with chromosome or cell-cycle activity. PPM1G could provide a regulatory connection through dephosphorylation of splicing factors, EIF2A and RARS1 could mark translational demand, YTHDF2 could couple the state to mRNA turnover, and SMC4 could represent proliferative or germ-cell-like chromosome organization. The reproductive and progenitor-associated HPA patterns suggest that this signal may partly arise from shared cell states or changing cellular composition in the two tissues, rather than from a single physical complex. This remains a hypothesis because the network lacks STRING and hu.MAP support and no GO or KEGG term passed global correction.

### Important genes

#### PPM1G

- **Related proteins** (co-abundance neighbors): EIF2A (0.87), RARS1 (0.82), SMC4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase, Mg2+/Mn2+ dependent 1G. The protein encoded by this gene is a member of the PP2C family of Ser/Thr protein phosphatases. PP2C family members are known to be negative regulators of cell stress response pathways. This phosphatase is found to be responsible for the dephosphorylation of Pre-mRNA splicing factors, which is important for the formation of functional spliceosome. Studies of a similar gene in mice suggested a rol…
- **Diseases (Open Targets)**: neurodegenerative disease (0.264); hepatocellular carcinoma (0.110); Crohn disease (0.106); lung adenocarcinoma (0.096); gout (0.081)
- **Europe PMC papers**: 799
- **Why important**: PPM1G is the central network node, connecting EIF2A, RARS1, and SMC4. Its established annotation as a magnesium- or manganese-dependent serine/threonine phosphatase links the module to protein dephosphorylation, stress-response regulation, pre-mRNA-splicing-factor dephosphorylation, and possible cell-cycle control. It is tissue enhanced in testis and enriched in several spermatogenic cell types, and it has substantial literature and disease-association coverage.
- **Conclusion**: Established: PPM1G is the strongest candidate regulatory hub and provides the clearest bridge between RNA processing, translation, and chromosome-related biology. Hypothesis: its co-abundance may mark phosphorylation-state control in a shared reproductive or proliferative cell state, but the module does not establish a direct interaction or causal role.

#### EIF2A

- **Related proteins** (co-abundance neighbors): PPM1G (0.87), YTHDF2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 2A. This gene encodes a eukaryotic translation initiation factor that catalyzes the formation of puromycin-sensitive 80 S preinitiation complexes and the poly(U)-directed synthesis of polyphenylalanine at low concentrations of Mg2+. This gene should not be confused with eIF2-alpha (EIF2S1, Gene ID: 1965), the alpha subunit of the eIF2 translation initiation complex. Although both of these proteins fun…
- **Diseases (Open Targets)**: aging (0.131); liver disorder (0.131); drug allergy (0.119); dystonia 33 (0.118); Marinesco-Sjogren syndrome (0.118)
- **Europe PMC papers**: 4315
- **Why important**: EIF2A connects the PPM1G-centered portion of the network to YTHDF2. Its established role in translation initiation and response to amino-acid starvation makes it a plausible marker of translational state. It is detected by immunohistochemistry in both tissues, has low tissue and immune-cell specificity, and has extensive literature and disease-association coverage.
- **Conclusion**: Established: EIF2A supports interpretation of the module as involving translation and translational regulation. Hypothesis: EIF2A may couple translational demand to RNA turnover through YTHDF2, although the co-abundance edge does not demonstrate a biochemical interaction.

#### SMC4

- **Related proteins** (co-abundance neighbors): TANC1 (0.82), PPM1G (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nuclear speckles, Cytosol; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: structural maintenance of chromosomes 4. This gene belongs to the 'structural maintenance of chromosomes' (SMC) gene family. Members of this gene family play a role in two changes in chromosome structure during mitotic segregation of chromosomes- chromosome condensation and sister chromatid cohesion. The protein encoded by this gene is likely a subunit of the 13S condensin complex, which is involved in chromosome condensation. A pseudoge…
- **Diseases (Open Targets)**: clonal hematopoiesis (0.233); bone marrow failure syndrome (0.148); hepatocellular carcinoma (0.111); central nervous system cancer (0.107); glioma (0.107)
- **Europe PMC papers**: 1967
- **Why important**: SMC4 is connected to PPM1G and TANC1. Its established role as a condensin-associated structural-maintenance protein supports chromosome condensation, sister-chromatid segregation, and meiotic chromosome biology. HPA annotations link it to lymphoid tissue, differentiating spermatogonia, primary spermatocytes, erythrocyte progenitors, and basophils. It also has substantial literature and disease-association coverage.
- **Conclusion**: Established: SMC4 contributes a chromosome-organization and cell-state component to the module. Hypothesis: its presence may indicate proliferative, meiotic, or progenitor-cell representation in the shared tissue signal, but the data do not identify which of these states drives the association.

#### YTHDF2

- **Related proteins** (co-abundance neighbors): EIF2A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: YTH N6-methyladenosine RNA binding protein F2. This gene encodes a member of the YTH (YT521-B homology) superfamily containing YTH domain. The YTH domain is typical for the eukaryotes and is particularly abundant in plants. The YTH domain is usually located in the middle of the protein sequence and may function in binding to RNA. In addition to a YTH domain, this protein has a proline rich region which may be involved in signal transduction. A…
- **Diseases (Open Targets)**: neurodegenerative disease (0.448); type 2 diabetes mellitus (0.157); neoplasm (0.118); hepatocellular carcinoma (0.117); gastric cancer (0.111)
- **Europe PMC papers**: 7075
- **Why important**: YTHDF2 is the terminal network member connected to EIF2A. Its established YTH-domain RNA-binding function and annotations for mRNA catabolism, oocyte maturation, gamete generation, and spermatogonial cell division make it particularly relevant to a cervix_uterine–ovary module with reproductive-cell associations. It is enhanced in syncytiotrophoblasts and has the largest literature and disease-association coverage among the listed members.
- **Conclusion**: Established: YTHDF2 provides the strongest RNA-fate and reproductive-cell annotation in the module. Hypothesis: it may coordinate selective mRNA turnover with translation in the shared tissue state, but this cannot be inferred as a direct mechanism from the sparse co-abundance network.

#### RARS1

- **Related proteins** (co-abundance neighbors): PPM1G (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 is directly connected to the central node PPM1G. Its established function in arginyl-tRNA aminoacylation provides a specific translation-related contribution distinct from EIF2A. It has low tissue and immune-cell specificity, is detected in cervix_uterine but not ovary by the reported immunohistochemistry evidence, and has documented associations with leukodystrophy-related disease categories.
- **Conclusion**: Established: RARS1 supports the interpretation that translational machinery contributes to the module. Hypothesis: its tissue-asymmetric protein detection could reflect regulation or cell composition, but it should not be interpreted as evidence that RARS1 drives the shared module.

## Module 9

**Tissue pair**: cervix_uterine and ovary  
**Genes (9)**: KPNA2, KRT18, KRT8, MCM2, MCM4, MCM5, MCM7, NASP, PSPC1

### Function

The module is most strongly associated with the MCM-dependent DNA-replication machinery and replication-associated DNA repair. The primary evidence is the globally corrected enrichment for the MCM, preinitiation, and CMG complexes and for DNA replication initiation (17 globally significant GO/KEGG terms, q_global 3.21e-05–0.00832; see the table), together with enrichment for homologous recombination and recombinational repair (6 globally significant GO/KEGG terms, q_global 0.00902–0.0217; see the table). The same MCM2, MCM4, MCM5, and MCM7 genes drive nearly all of these terms, so the most defensible interpretation is a cell-proliferation and genome-duplication program rather than a broad pathway specific to cervix or ovary. NASP extends the signal toward DNA replication-dependent chromatin assembly, while KPNA2 contributes to terms involving DNA recombination and DNA metabolism (GO:BP DNA recombination; q_global = 0.00902), (GO:BP DNA replication; q_global = 0.0174), (GO:BP regulation of DNA metabolic process; q_global = 0.0342), (GO:BP DNA metabolic process; q_global = 0.0438). KRT8 and KRT18 do not contribute to significant GO/KEGG enrichment in the supplied results and are better interpreted as epithelial structural markers within the network.

**Cell composition.** The module is not secreted and is not dominated by plasma proteins. Most genes have low immune-cell specificity, so the module is not best described as a blood-cell module, although HPA annotations show recurring enrichment in bone marrow, erythrocyte progenitors, megakaryocyte progenitors, and trophoblast populations. Several genes are also associated with proliferative or germ-cell populations. This pattern is consistent with a conserved nuclear replication program that may track the abundance of cycling or progenitor-like cells in both tissues. KRT8 and KRT18 indicate an epithelial component, and their presence could also reflect shared epithelial cell types. HPA detects the proteins broadly in cervix and detects most, but not all, in ovary; this supports biological plausibility while not proving that every module relationship occurs in the same cells.

**GO/KEGG enrichment**: 28 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP double-strand break repair via break-induced replication | 3.21e-05 | MCM2, MCM4, MCM5, MCM7 |
| GO:CC DNA replication preinitiation complex | 3.21e-05 | MCM2, MCM4, MCM5, MCM7 |
| GO:CC MCM complex | 3.21e-05 | MCM2, MCM4, MCM5, MCM7 |
| GO:CC CMG complex | 3.21e-05 | MCM2, MCM4, MCM5, MCM7 |
| GO:BP regulation of DNA-templated DNA replication initiation | 0.000148 | MCM2, MCM4, MCM5, MCM7 |
| GO:BP regulation of DNA-templated DNA replication | 0.000148 | MCM2, MCM4, MCM5, MCM7 |
| GO:MF four-way junction helicase activity | 0.00086 | MCM2, MCM4, MCM5, MCM7 |
| GO:MF forked DNA-dependent helicase activity | 0.00086 | MCM2, MCM4, MCM5, MCM7 |
| GO:BP DNA replication initiation | 0.00116 | MCM2, MCM4, MCM5, MCM7 |
| GO:MF double-stranded DNA helicase activity | 0.00116 | MCM2, MCM4, MCM5, MCM7 |
| GO:MF 3'-5' DNA helicase activity | 0.00116 | MCM2, MCM4, MCM5, MCM7 |
| GO:MF single-stranded 3'-5' DNA helicase activity | 0.00116 | MCM2, MCM4, MCM5, MCM7 |
| GO:MF single-stranded DNA helicase activity | 0.00325 | MCM2, MCM4, MCM5, MCM7 |
| GO:BP regulation of DNA replication | 0.00593 | MCM2, MCM4, MCM5, MCM7 |
| KEGG DNA replication - Homo sapiens (human) | 0.00593 | MCM2, MCM4, MCM5, MCM7 |

### STRING and hu.MAP

STRING provides strong, already-known relationships among MCM2, MCM4, MCM5, and MCM7, and links MCM7 with NASP (15 supplementary STRING terms; within-query FDR 9.77e-06–0.00037). It also supports the KRT8–KRT18 pair. The direct STRING edges therefore validate the central MCM subnetwork and show that much of the apparent module signal reflects a known replication complex rather than an uncharacterized interaction system. hu.MAP independently places the MCM genes together in several replication, CMG, and MCM-complex assemblies (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09238.1), while additional complexes connect MCM proteins with chromatin, histone, and replication-associated machinery (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10747.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_12711.1) (hu.MAP huMAP3_14306.1). NASP is represented in a chromatin assembly complex with MCM2 (hu.MAP huMAP3_10747.1), and KRT18 is represented with NASP in a broader complex (hu.MAP huMAP3_12711.1). These resources support a coherent replication and chromatin context, but partial membership in a complex does not establish direct physical interaction for every pair in the co-abundance network.

**STRING interactions (score >= 0.7)**: 8 of 36 gene pairs: KRT18–KRT8 (0.999); MCM2–MCM4 (0.999); MCM2–MCM5 (0.999); MCM2–MCM7 (0.999); MCM4–MCM5 (0.999); MCM4–MCM7 (0.999); MCM5–MCM7 (0.999); MCM7–NASP (0.81)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam MCM N-terminal domain (FDR = 9.77e-06, 4 genes); Component MCM complex (FDR = 6.12e-05, 4 genes); Component CMG complex (FDR = 6.12e-05, 4 genes); COMPARTMENTS MCM complex (FDR = 6.36e-05, 4 genes); COMPARTMENTS CMG complex (FDR = 6.36e-05, 4 genes); InterPro MCM domain (FDR = 8.5e-05, 4 genes); InterPro Mini-chromosome maintenance, conserved site (FDR = 8.5e-05, 4 genes); InterPro MCM N-terminal domain (FDR = 8.5e-05, 4 genes); InterPro Mini-chromosome maintenance protein (FDR = 8.5e-05, 4 genes); InterPro MCM OB domain (FDR = 8.5e-05, 4 genes); InterPro MCM, AAA-lid domain (FDR = 8.5e-05, 4 genes); RCTM Unwinding of DNA (FDR = 9.42e-05, 4 genes); Keyword DNA replication (FDR = 0.00015, 5 genes); NetworkNeighborAL Activation of the pre-replicative complex, and GINS complex (FDR = 0.00016, 4 genes); RCTM Activation of the pre-replicative complex (FDR = 0.00037, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05529.1 (MCM4, MCM5, MCM7, MCM2; 4/6); huMAP3_14758.1 (MCM4, MCM5, MCM7, MCM2; 4/14); huMAP3_08554.1 (MCM4, MCM5, MCM7, MCM2; 4/15); huMAP3_11832.1 (MCM4, MCM5, MCM7, MCM2; 4/15); huMAP3_12180.1 (MCM4, MCM5, MCM7, MCM2; 4/17); huMAP3_06061.1 (MCM4, MCM7, MCM2; 3/5); huMAP3_07113.1 (MCM4, MCM7, MCM2; 3/6); huMAP3_11119.1 (MCM4, MCM5, MCM7; 3/14); huMAP3_09860.1 (MCM4, MCM2; 2/4); huMAP3_00154.1 (MCM4, MCM2; 2/5); huMAP3_09238.1 (MCM5, MCM7; 2/11); huMAP3_09466.1 (MCM4, MCM2; 2/23); huMAP3_10747.1 (NASP, MCM2; 2/25); huMAP3_10862.1 (MCM4, MCM2; 2/33); huMAP3_12711.1 (KRT18, NASP; 2/35); huMAP3_14306.1 (MCM4, MCM2; 2/55)

### Novelty

The core biological interpretation is not a new discovery: MCM2, MCM4, MCM5, and MCM7 are established components of the MCM and CMG replication machinery, and their relationships are supported by STRING, hu.MAP, and the globally corrected GO/KEGG results. The potentially novel aspect is the reproducible co-abundance configuration shared by cervix and ovary, particularly the way the established MCM core is coupled to NASP, KPNA2, PSPC1, and epithelial keratins in these tissue groups. However, the supplied evidence does not establish tissue-specific causality, direct interaction among all module members, or novelty relative to every published co-expression study. Absence of KRT8, KRT18, KPNA2, or PSPC1 from some interaction resources is evidence of incomplete database coverage, not proof that those associations are novel.

**Hypothesis.** Hypothesis: the shared module reflects variation in the abundance of cycling epithelial, progenitor-like, or other proliferative cells across cervix and ovary. In this model, the MCM core licenses and supports replication, NASP coordinates histone handling and replication-dependent chromatin assembly, and KPNA2 supports nuclear import of relevant factors. PSPC1 may mark a nuclear RNA-regulatory context, while KRT8 and KRT18 report the epithelial cellular environment. The co-abundance pattern could therefore arise from coordinated cell-state composition or proliferation rather than from one specialized cervix–ovary pathway. This hypothesis should be tested with cell-resolved measurements, replication-state markers, and perturbation or physical-interaction assays.

### Important genes

#### MCM7

- **Related proteins** (co-abundance neighbors): MCM5 (0.91), MCM2 (0.90), MCM4 (0.89), NASP (0.84), KPNA2 (0.83); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), NASP (0.81)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 is the most connected module member and links the MCM core to NASP and KPNA2. It participates in every globally corrected GO/KEGG term listed for the module (28 globally significant GO/KEGG terms, q_global 3.21e-05–0.0444; see the table), is supported by strong STRING relationships with the other MCM genes and NASP, and appears across many hu.MAP replication complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1), (hu.MAP huMAP3_09238.1). Its established function is as a conserved component of the MCM helicase and replication-initiation machinery. The supplied disease associations include spastic paraplegia, Meier-Gorlin syndrome, AP-4 deficiency syndrome, microcephaly, and trichiasis. Its large literature base makes it a well-established anchor rather than a speculative marker.
- **Conclusion**: Established conclusion: MCM7 is a central structural and functional anchor of the module and strongly supports a DNA-replication interpretation. Hypothesis: its connectivity may make it a useful reporter of the abundance of actively cycling cells in both tissues, but the co-abundance data do not show that MCM7 initiates the tissue-level program.

#### MCM2

- **Related proteins** (co-abundance neighbors): MCM7 (0.90), KRT8 (0.84), MCM5 (0.82), MCM4 (0.81); STRING partners: MCM4 (0.999), MCM5 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10747.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a highly connected MCM-core member and is linked to MCM4, MCM5, MCM7, and KRT8 in the module. It contributes to every globally corrected GO/KEGG term (28 globally significant GO/KEGG terms, q_global 3.21e-05–0.0444; see the table), is supported by strong STRING relationships, and occurs in numerous hu.MAP complexes spanning replication, CMG, chromatin, and histone-associated assemblies (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1), (hu.MAP huMAP3_09860.1), (hu.MAP huMAP3_00154.1), (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10747.1) (hu.MAP huMAP3_10862.1), (hu.MAP huMAP3_14306.1). Its established role is in replication initiation and the MCM helicase complex. The supplied disease associations include autosomal dominant nonsyndromic hearing loss and related abnormalities. It also has the largest literature volume among the listed genes, reinforcing the strength of the established interpretation.
- **Conclusion**: Established conclusion: MCM2 is a core replication component and one of the strongest indicators that the module represents a bona fide replication-associated state. Hypothesis: its connection with KRT8 may couple epithelial cell abundance to proliferation, but this cannot be inferred as a direct molecular interaction from co-abundance alone.

#### MCM4

- **Related proteins** (co-abundance neighbors): MCM7 (0.89), NASP (0.86), MCM5 (0.85), MCM2 (0.81); STRING partners: MCM2 (0.999), MCM5 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 4. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication rel…
- **Diseases (Open Targets)**: primary immunodeficiency with natural-killer cell deficiency and adrenal insufficiency (0.714); X-linked adrenal hypoplasia congenita (0.185); lung adenocarcinoma (0.112); microcephaly (0.111); neoplasm (0.102)
- **Europe PMC papers**: 4082
- **Why important**: MCM4 is a central MCM-core member with strong links to MCM2, MCM5, MCM7, and NASP. It appears in every globally corrected GO/KEGG term (28 globally significant GO/KEGG terms, q_global 3.21e-05–0.0444; see the table), has strong STRING support, and is represented in more hu.MAP replication and chromatin complexes than most other module genes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1), (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1), (hu.MAP huMAP3_09466.1), (hu.MAP huMAP3_10862.1), (hu.MAP huMAP3_14306.1). Its established function is in the MCM helicase and replication-initiation machinery. The supplied disease associations include primary immunodeficiency with natural-killer-cell deficiency and adrenal insufficiency, X-linked adrenal hypoplasia congenita, lung adenocarcinoma, microcephaly, and neoplasm.
- **Conclusion**: Established conclusion: MCM4 independently reinforces the interpretation of a conserved replication-initiation module. Hypothesis: its association with NASP may indicate coordination between helicase abundance and replication-coupled chromatin handling, but the present data do not establish directionality or mechanism.

#### NASP

- **Related proteins** (co-abundance neighbors): MCM4 (0.86), MCM7 (0.84), PSPC1 (0.81); STRING partners: MCM7 (0.81)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_10747.1, huMAP3_12711.1
- **Function (MyGene.info)**: nuclear autoantigenic sperm protein. This gene encodes a H1 histone binding protein that is involved in transporting histones into the nucleus of dividing cells. Multiple isoforms are encoded by transcript variants of this gene. The somatic form is expressed in all mitotic cells, is localized to the nucleus, and is coupled to the cell cycle. The testicular form is expressed in embryonic tissues, tumor cells, and the testis. In male g…
- **Diseases (Open Targets)**: neurodegenerative disease (0.445); Paralytic ileus (0.301); glioma (0.080); central nervous system cancer (0.080); hepatocellular carcinoma (0.076)
- **Europe PMC papers**: 1349
- **Why important**: NASP connects the MCM core to chromatin biology through links with MCM4 and MCM7 and through the PSPC1 edge. It contributes to globally corrected DNA-replication and DNA-metabolism terms (GO:BP DNA replication; q_global = 0.0174), (GO:BP DNA metabolic process; q_global = 0.0438), and STRING supplementary evidence identifies a DNA-replication association (STRING Keyword DNA replication; within-query FDR = 0.00015). hu.MAP places NASP with MCM2 in a histone and chromatin assembly complex (hu.MAP huMAP3_10747.1). Its established function is histone binding and nuclear histone transport in dividing cells, with roles in replication-dependent chromatin assembly. The supplied disease associations include neurodegenerative disease, paralytic ileus, glioma, central nervous system cancer, and hepatocellular carcinoma.
- **Conclusion**: Established conclusion: NASP provides a credible chromatin-assembly bridge within the otherwise MCM-dominated module. Hypothesis: NASP may help explain why the shared co-abundance signal tracks proliferative cell states rather than replication helicase abundance alone.

## Module 10

**Tissue pair**: cervix_uterine and ovary  
**Genes (5)**: KRT10, KRT14, KRT2, KRT1, KRT5

### Function

The module is a keratin intermediate-filament program of stratified epithelial structure and differentiation. The primary evidence is exceptionally coherent: every module member contributes to keratin filament and intermediate-filament organization terms (4 globally significant GO/KEGG terms, q_global 1.72e-07–1.59e-06; see the table), (GO:CC intermediate filament; q_global = 5.35e-06), (GO:CC intermediate filament cytoskeleton; q_global = 1.6e-05), and to keratinocyte, epidermal, epithelial, cornified-envelope, keratinization, and tissue-development terms (GO:MF structural constituent of skin epidermis; q_global = 2.48e-06), (GO:BP keratinocyte differentiation; q_global = 1.15e-05), (16 globally significant GO/KEGG terms, q_global 2.95e-05–0.0454; see the table). The KEGG evidence for cornified-envelope formation and cadherin signaling (KEGG Cornified envelope formation - Homo sapiens (human); q_global = 2.95e-05), (KEGG Cadherin signaling - Homo sapiens (human); q_global = 0.000231) is consistent with epithelial barrier formation and cell–cell organization. These annotations support a structural and differentiation function, rather than a specialized endocrine or immune function.

**Cell composition.** This is an epithelial keratin module, not a plasma-protein or broadly expressed housekeeping module. HPA shows enrichment in skin and in suprabasal or basal keratinocyte populations across the module, with KRT5 also enriched in cervix-related epithelial groups. Four module proteins are detected in cervix_uterine, whereas none are detected in ovary by the reported HPA protein assay. The module is therefore compatible with shared stratified or squamous epithelial content in the two tissue datasets, but the ovarian signal should not be interpreted as evidence that these proteins are abundant in ovarian parenchymal cells. One member, KRT10, is annotated as secreted in other tissues, but the module as a whole is not a secreted-protein program. The reported immune-cell annotations are sparse and inconsistent with the dominant keratinocyte pattern, so blood-cell contamination is not the leading interpretation.

**GO/KEGG enrichment**: 24 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC keratin filament | 1.72e-07 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| GO:BP intermediate filament organization | 6.01e-07 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| GO:BP intermediate filament-based process | 1.59e-06 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| GO:BP intermediate filament cytoskeleton organization | 1.59e-06 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| GO:MF structural constituent of skin epidermis | 2.48e-06 | KRT1, KRT10, KRT2, KRT5 |
| GO:CC intermediate filament | 5.35e-06 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| GO:BP keratinocyte differentiation | 1.15e-05 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| GO:CC intermediate filament cytoskeleton | 1.6e-05 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| KEGG Cornified envelope formation - Homo sapiens (human) | 2.95e-05 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| GO:BP epidermal cell differentiation | 3.81e-05 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| GO:CC cornified envelope | 0.000125 | KRT1, KRT10, KRT14, KRT2 |
| GO:BP skin development | 0.000125 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| GO:BP epidermis development | 0.000195 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| KEGG Cadherin signaling - Homo sapiens (human) | 0.000231 | KRT1, KRT10, KRT14, KRT2, KRT5 |
| GO:BP epithelial cell differentiation | 0.00135 | KRT1, KRT10, KRT14, KRT2, KRT5 |

### STRING and hu.MAP

STRING provides strong supplementary support for a pre-existing keratin network: the module contains most of the high-confidence pairwise associations among its members, including the KRT5–KRT14 basal keratin pair, the KRT1–KRT10 and KRT1–KRT2 associations, and links connecting KRT5 with the suprabasal keratins. The STRING functional results independently recover keratin, intermediate-filament, keratin-filament, cornified-envelope, and skin-blistering annotations (10 supplementary STRING terms; within-query FDR 2.7e-08–4.1e-07). These STRING FDR values are supplementary and are not treated as global enrichment significance. No hu.MAP complex contains at least two module members. Thus, the network is well supported as a family of known protein associations, but the absence of a hu.MAP complex argues against claiming that it represents a newly defined experimentally resolved multiprotein complex.

**STRING interactions (score >= 0.7)**: 7 of 10 gene pairs: KRT1–KRT10 (0.999); KRT1–KRT2 (0.956); KRT1–KRT5 (0.923); KRT10–KRT2 (0.904); KRT10–KRT5 (0.793); KRT14–KRT5 (0.999); KRT2–KRT5 (0.871)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Keratin (FDR = 2.7e-08, 5 genes); Keyword Intermediate filament (FDR = 3.6e-08, 5 genes); SMART Intermediate filament protein (FDR = 3.92e-08, 5 genes); Component Keratin filament (FDR = 5.71e-08, 5 genes); COMPARTMENTS Keratin filament (FDR = 5.94e-08, 5 genes); NetworkNeighborAL Formation of the cornified envelope, and Serpin, conserved site (FDR = 9.01e-08, 5 genes); InterPro Intermediate filament protein, conserved site (FDR = 2.11e-07, 5 genes); InterPro Intermediate filament, rod domain (FDR = 2.11e-07, 5 genes); HPO Abnormal blistering of the skin (FDR = 3.13e-07, 5 genes); RCTM Formation of the cornified envelope (FDR = 4.1e-07, 5 genes); DISEASES Acanthoma (FDR = 1.23e-06, 4 genes); PMID (2025) Mass spectrometric detection of keratins in tear fluid. (FDR = 2.39e-06, 5 genes); PMID (2023) Neryl acetate, the major component of Corsican Helichrysum italicum essential oil, mediates its biological activities on skin barrier. (FDR = 2.39e-06, 5 genes); PMID (2023) FAM3CILEI protein is elevated in psoriatic lesions and triggers psoriasiform hyperproliferation in mice. (FDR = 2.39e-06, 5 genes); PMID (2023) Key Factors in the Complex and Coordinated Network of Skin Keratinization: Their Significance and Involvement in Common Skin Conditions. (FDR = 2.39e-06, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The biological interpretation is not novel: keratin heterotypic pairing, intermediate-filament assembly, keratinocyte differentiation, cornification, and associated epithelial disorders are established. The module-level observation may still be a useful dataset-specific finding because these genes co-abundance as a conserved module across cervix_uterine and ovary is not demonstrated by the supplied reference resources. However, absence from hu.MAP, or absence of a particular association from STRING, cannot establish novelty. The most defensible claim is a potentially novel cross-tissue co-abundance pattern built from well-known keratin biology, rather than discovery of a new molecular pathway or complex.

**Hypothesis.** Hypothesis: the conserved module reflects the abundance of stratified epithelial or squamous epithelial cells, with coordinated transition from a KRT5–KRT14 basal program toward KRT1, KRT10, and KRT2 suprabasal differentiation and cornified-envelope formation. In cervix_uterine this may represent epithelial barrier content directly; in ovary it may reflect shared epithelial components, tissue-interface material, or a related sample-composition effect rather than ovarian-specific keratin biology. The co-abundance pattern could therefore arise from coordinated cell-state composition and differentiation, while the actual physical filament assembly is supported by known keratin biology but is not proven by co-abundance alone.

### Important genes

#### KRT14

- **Related proteins** (co-abundance neighbors): KRT5 (0.96), KRT10 (0.95), KRT1 (0.92), KRT2 (0.86); STRING partners: KRT5 (0.999)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Intermediate filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 14. This gene encodes a member of the keratin family, the most diverse group of intermediate filaments. This gene product, a type I keratin, is usually found as a heterotetramer with two keratin 5 molecules, a type II keratin. Together they form the cytoskeleton of epithelial cells. Mutations in the genes for these keratins are associated with epidermolysis bullosa simplex. At least one pseudogene has…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 1A, generalized severe (0.823); epidermolysis bullosa simplex 1C, localized (0.818); epidermolysis bullosa simplex 1B, generalized intermediate (0.802); epidermolysis bullosa simplex 1D, generalized, intermediate or severe, autosomal recessive (0.759); Naegeli-Franceschetti-Jadassohn syndrome (0.759)
- **Europe PMC papers**: 6348
- **Why important**: KRT14 is the most connected and strongest-supported node in the module. HPA places it in basal and suprabasal keratinocyte contexts and detects it in cervix_uterine. It participates in the primary keratin-filament, intermediate-filament, keratinocyte-differentiation, and epithelial-development evidence (4 globally significant GO/KEGG terms, q_global 1.72e-07–1.59e-06; see the table), (10 globally significant GO/KEGG terms, q_global 5.35e-06–0.00135; see the table), (7 globally significant GO/KEGG terms, q_global 0.00355–0.0454; see the table). Its established KRT14–KRT5 heterotetramer role and epidermolysis bullosa simplex associations make it a key structural and disease-relevant anchor. Its extensive literature also makes it one of the best characterized members.
- **Conclusion**: Established conclusion: KRT14 is a basal epithelial intermediate-filament anchor and a central indicator of the module's epithelial identity. Hypothesis: variation in KRT14 abundance may mark the basal epithelial contribution that links cervix_uterine and ovary samples.

#### KRT5

- **Related proteins** (co-abundance neighbors): KRT14 (0.96), KRT10 (0.93); STRING partners: KRT1 (0.923), KRT10 (0.793), KRT14 (0.999), KRT2 (0.871)
- **HPA**: Group enriched; Group enriched; blood Immune cell enriched; location Intermediate filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 5. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the basal layer of the epidermis with family member KRT14. Mutations in t…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 2C, localized (0.768); epidermolysis bullosa simplex 2A, generalized severe (0.761); epidermolysis bullosa simplex 2B, generalized intermediate (0.761); epidermolysis bullosa simplex 2F, with mottled pigmentation (0.729); Dowling-Degos disease 1 (0.697)
- **Europe PMC papers**: 7044
- **Why important**: KRT5 is the principal basal type-II partner of KRT14 and has strong connections to both KRT14 and the suprabasal keratin group. HPA specifically supports epithelial enrichment involving cervix and multiple basal or suprabasal epithelial populations. It contributes broadly to the globally supported keratin-filament, epithelial differentiation, keratinization, and cornified-envelope evidence. Its established roles in basal-layer cytoskeletal organization, mechanical response, migration, and epidermolysis bullosa simplex make it important for interpreting both structure and disease relevance.
- **Conclusion**: Established conclusion: KRT5 identifies the basal epithelial arm of the module and provides a well-supported structural interpretation. Hypothesis: coordinated KRT5 abundance may indicate the amount or state of basal-like epithelium in each tissue sample.

#### KRT1

- **Related proteins** (co-abundance neighbors): KRT14 (0.92), KRT10 (0.89); STRING partners: KRT10 (0.999), KRT2 (0.956), KRT5 (0.923)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 connects the basal KRT5–KRT14 pair with the suprabasal KRT10 and KRT2 group, making it a useful network bridge. HPA identifies it with suprabasal keratinocytes and detects it in cervix_uterine. It appears across the primary evidence for intermediate filaments, keratinocyte differentiation, cornified envelope, keratinization, and epithelial development (4 globally significant GO/KEGG terms, q_global 1.72e-07–1.59e-06; see the table), (10 globally significant GO/KEGG terms, q_global 5.35e-06–0.00135; see the table), (7 globally significant GO/KEGG terms, q_global 0.00355–0.0454; see the table). Its established keratinization function and associations with epidermolytic and palmoplantar keratin disorders give it substantial biological and clinical relevance.
- **Conclusion**: Established conclusion: KRT1 is a central suprabasal structural component and a transition marker between basal and differentiated keratin programs. Hypothesis: its co-abundance may report the degree of epithelial maturation represented in the samples.

#### KRT10

- **Related proteins** (co-abundance neighbors): KRT14 (0.95), KRT5 (0.93), KRT1 (0.89); STRING partners: KRT1 (0.999), KRT2 (0.904), KRT5 (0.793)
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 10. This gene encodes a member of the type I (acidic) cytokeratin family, which belongs to the superfamily of intermediate filament (IF) proteins. Keratins are heteropolymeric structural proteins which form the intermediate filament. These filaments, along with actin microfilaments and microtubules, compose the cytoskeleton of epithelial cells. Mutations in this gene are associated with epidermolytic …
- **Diseases (Open Targets)**: epidermolytic hyperkeratosis 2A, autosomal dominant (0.787); epidermolytic ichthyosis (0.772); congenital reticular ichthyosiform erythroderma (0.727); ichthyosis, annular epidermolytic 1 (0.647); annular epidermolytic ichthyosis (0.642)
- **Europe PMC papers**: 2736
- **Why important**: KRT10 is a highly connected suprabasal member linked to KRT1, KRT5, and KRT14 in the module and in STRING. HPA assigns it to skin and suprabasal keratinocytes and reports it as absent by the stated protein assay in both sampled tissues, which highlights possible assay or abundance differences between transcript-level co-abundance and protein detection. It contributes to the primary intermediate-filament, epidermal differentiation, cornified-envelope, keratinization, and structural evidence (6 globally significant GO/KEGG terms, q_global 1.72e-07–5.35e-06; see the table), (9 globally significant GO/KEGG terms, q_global 1.6e-05–0.00214; see the table), (7 globally significant GO/KEGG terms, q_global 0.00355–0.0454; see the table). Its established associations with epidermolytic hyperkeratosis and ichthyotic disorders add disease relevance.
- **Conclusion**: Established conclusion: KRT10 represents differentiated suprabasal keratin biology. Hypothesis: its co-abundance may reflect epithelial maturation even when protein-level detection is limited, so this inference should be tested with matched transcript and protein measurements.

#### KRT2

- **Related proteins** (co-abundance neighbors): KRT14 (0.86); STRING partners: KRT1 (0.956), KRT10 (0.904), KRT5 (0.871)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location Intermediate filaments, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 2. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is expressed largely in the upper spinous layer of epidermal keratinocytes and mutations in this gene …
- **Diseases (Open Targets)**: superficial epidermolytic ichthyosis (0.815); exfoliative ichthyosis (0.358); Palmoplantar hyperkeratosis (0.267); hereditary disease (0.193); Vertigo (0.145)
- **Europe PMC papers**: 7459
- **Why important**: KRT2 is the most peripheral member of the module but is strongly integrated with the keratin network through STRING associations with KRT1, KRT10, KRT5, and KRT14. HPA assigns it to suprabasal keratinocytes and detects it in cervix_uterine. It contributes to the globally supported intermediate-filament, epidermal differentiation, cornified-envelope, keratinization, and structural terms (15 globally significant GO/KEGG terms, q_global 1.72e-07–0.00135; see the table), (8 globally significant GO/KEGG terms, q_global 0.00214–0.0454; see the table). Its established expression in upper spinous epidermal layers and associations with epidermolytic and exfoliative ichthyoses make it informative for the terminal differentiation end of the module.
- **Conclusion**: Established conclusion: KRT2 marks the differentiated suprabasal component and reinforces the keratinization interpretation. Hypothesis: KRT2 may help distinguish a mature suprabasal state from a predominantly basal epithelial signal, although the co-abundance data alone cannot establish directional differentiation.

## Module 11

**Tissue pair**: cervix_uterine and ovary  
**Genes (10)**: NUP160, PRRC2A, PSMC4, PUM1, UPF1, RPAP3, SRP54, EPRS1, IARS1, ZC3HAV1

### Function

The module is most consistent with a broadly expressed RNA and protein homeostasis program rather than a tissue-specific pathway. Its genes connect RNA surveillance and post-transcriptional regulation through UPF1 and PUM1, translation and translational fidelity through EPRS1 and IARS1, nuclear transport through NUP160, proteasome function through PSMC4, signal-recognition-particle activity through SRP54, and antiviral RNA decay through ZC3HAV1. The network therefore suggests coordinated control of RNA processing, translation, quality control, and intracellular protein handling. This interpretation is supported by the direct STRING relationship between EPRS1 and IARS1 and by the hu.MAP groupings linking UPF1 with PUM1 (hu.MAP huMAP3_08338.1), (hu.MAP huMAP3_10905.1), (hu.MAP huMAP3_05758.1), (hu.MAP huMAP3_06975.1), (hu.MAP huMAP3_10625.1) and EPRS1 with IARS1 (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1). No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The lack of a globally enriched term does not invalidate the module; it indicates that the genes represent a mixed or distributed cellular program rather than a sharply concentrated canonical pathway.

**Cell composition.** The module is not composed of secreted or plasma proteins, and the HPA evidence does not indicate a blood-cell-dominated signal. Most genes have low tissue specificity and low immune-cell specificity, with several not detected in immune cells. Protein detection is present for nearly all assayed genes in cervix_uterine and for most assayed genes in ovary, supporting a resident cellular expression program rather than a simple plasma contamination explanation. The module nevertheless contains broadly expressed housekeeping-like machinery involved in RNA surveillance, translation, nuclear transport, proteasomal degradation, and protein targeting. HPA cell-type annotations are heterogeneous, including reproductive, epithelial, neural, podocyte, and immune-associated cell annotations, so the shared signal could reflect common cellular maintenance machinery or shared cell states rather than a specialized cervix–ovary function. ZC3HAV1 is tissue enhanced in bone marrow and has cell-type-enhanced annotations involving endometrial cells, neutrophils, NK cells, and plasmacytoid dendritic cells, but the overall HPA profile does not support interpreting the complete module as blood-cell enriched.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING evidence is sparse: the only high-confidence recorded pair is the interaction between EPRS1 and IARS1. This is biologically coherent because both are aminoacyl-tRNA synthetases and both participate in translation-related activity. There is no STRING functional enrichment. hu.MAP provides convergent complex-level evidence for two substructures. UPF1 and PUM1 repeatedly occur together in RNA-binding, RNA-processing, and RNA-surveillance complexes (hu.MAP huMAP3_08338.1), (hu.MAP huMAP3_10905.1), (hu.MAP huMAP3_05758.1), (hu.MAP huMAP3_06975.1), (hu.MAP huMAP3_10625.1), while EPRS1 and IARS1 occur together in aminoacyl-tRNA synthetase-containing complexes (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1). The remaining module genes are connected to these substructures in the co-abundance network but lack corresponding hu.MAP or STRING support in the supplied evidence. Thus, the network appears to combine a comparatively well-supported RNA-regulatory branch with a translation-related branch, rather than representing one experimentally established physical complex.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: EPRS1–IARS1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08338.1 (PUM1, UPF1; 2/5); huMAP3_10905.1 (PUM1, UPF1; 2/6); huMAP3_05758.1 (PUM1, UPF1; 2/7); huMAP3_02637.1 (EPRS1, IARS1; 2/14); huMAP3_13688.1 (EPRS1, IARS1; 2/14); huMAP3_06975.1 (PUM1, UPF1; 2/31); huMAP3_10625.1 (PUM1, UPF1; 2/57)

### Novelty

The module should not be called a definitively new biological pathway. Its component processes and several relationships are already established: UPF1-mediated nonsense-mediated decay, PUM1-mediated post-transcriptional regulation, EPRS1 and IARS1 participation in translation, and the hu.MAP relationships listed above are known biology. What may be new is the co-abundance association of these particular genes across cervix_uterine and ovary and the apparent coupling of RNA surveillance, translation, protein targeting, and antiviral RNA control in this tissue pair. The sparse STRING support and absence of a globally significant GO or KEGG term mean that the shared module is best treated as a potentially novel systems-level association requiring independent validation. Absence from STRING or hu.MAP cannot by itself establish novelty.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular quality-control state in which RNA surveillance and post-transcriptional regulation are coordinated with accurate translation, protein targeting, and degradation. In this model, UPF1 and PUM1 organize RNA fate, EPRS1 and IARS1 support translational fidelity, NUP160 supports nucleocytoplasmic RNA exchange, SRP54 supports targeting of selected nascent proteins, PSMC4 removes damaged or unwanted proteins, and ZC3HAV1 adds an inducible antiviral RNA-decay component. The co-abundance pattern may therefore arise when cervix_uterine and ovary cells experience comparable demands for transcript quality control and proteome maintenance. This is a mechanistic hypothesis, not a demonstrated causal pathway; the current evidence does not establish physical interaction among all module members or prove that the module is tissue-specific.

### Important genes

#### UPF1

- **Related proteins** (co-abundance neighbors): EPRS1 (0.82), PSMC4 (0.81), IARS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_08338.1, huMAP3_10905.1, huMAP3_05758.1, huMAP3_06975.1, huMAP3_10625.1
- **Function (MyGene.info)**: UPF1 RNA helicase and ATPase. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons.…
- **Diseases (Open Targets)**: Intellectual disability (0.437); Global developmental delay (0.426); High anterior hairline (0.425); Frontal bossing (0.425); Hypertelorism (0.425)
- **Europe PMC papers**: 4252
- **Why important**: UPF1 has a central network position, connecting the translation-related genes EPRS1 and IARS1 with PSMC4, and it is represented across several hu.MAP complexes with PUM1 (hu.MAP huMAP3_08338.1), (hu.MAP huMAP3_10905.1), (hu.MAP huMAP3_05758.1), (hu.MAP huMAP3_06975.1), (hu.MAP huMAP3_10625.1). Its established functions in nonsense-mediated decay, mRNA export, translational termination, DNA replication, and DNA repair make it a strong mechanistic anchor for RNA quality control. It also has substantial literature and disease-association evidence involving developmental and intellectual phenotypes.
- **Conclusion**: Established evidence supports UPF1 as a core RNA-surveillance and post-transcriptional quality-control factor. Its network position and repeated hu.MAP occurrence support its importance in this module. It is plausible, but not proven, that UPF1 helps connect the RNA-regulatory and translation-related branches.

#### PUM1

- **Related proteins** (co-abundance neighbors): PRRC2A (0.87), ZC3HAV1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_08338.1, huMAP3_10905.1, huMAP3_05758.1, huMAP3_06975.1, huMAP3_10625.1
- **Function (MyGene.info)**: pumilio RNA binding family member 1. This gene encodes a member of the PUF family, evolutionarily conserved RNA-binding proteins related to the Pumilio proteins of Drosophila and the fem-3 mRNA binding factor proteins of C. elegans. The encoded protein contains a sequence-specific RNA binding domain comprised of eight repeats and N- and C-terminal flanking regions, and serves as a translational regulator of specific mRNAs by binding …
- **Diseases (Open Targets)**: spinocerebellar ataxia 47 (0.751); neurodevelopmental disorder with motor abnormalities, seizures, and facial dysmorphism (0.676); hereditary disease (0.504); neurodegenerative disease (0.487); hypertensive disorder (0.290)
- **Europe PMC papers**: 2316
- **Why important**: PUM1 is connected to PRRC2A and ZC3HAV1 and repeatedly co-occurs with UPF1 in hu.MAP complexes (hu.MAP huMAP3_08338.1), (hu.MAP huMAP3_10905.1), (hu.MAP huMAP3_05758.1), (hu.MAP huMAP3_06975.1), (hu.MAP huMAP3_10625.1). Its sequence-specific binding to messenger RNA three-prime untranslated regions and its roles in translational regulation, mRNA stability, post-transcriptional silencing, and microRNA processing provide a direct functional link to the proposed RNA-control interpretation. PUM1 also has substantial literature and strong disease-association evidence, including spinocerebellar ataxia.
- **Conclusion**: Established evidence supports PUM1 as an RNA-binding regulator capable of shaping transcript stability and translation. Its repeated complex association with UPF1 makes it an important module component. A specific cooperative PUM1–UPF1 mechanism in cervix_uterine or ovary remains a hypothesis.

#### EPRS1

- **Related proteins** (co-abundance neighbors): RPAP3 (0.83), UPF1 (0.82); STRING partners: IARS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is part of the module's strongest STRING-supported pair with IARS1 and is present with IARS1 in hu.MAP complexes (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1). As a glutamyl- and prolyl-tRNA synthetase, it provides a direct translation and aminoacylation function. It also links to RPAP3 and UPF1 in the co-abundance network, placing translational machinery near RNA surveillance. Its disease associations are relevant to inherited neurological disorders, although its literature volume is more limited than that of UPF1 or PUM1.
- **Conclusion**: Established evidence supports EPRS1 as a translation-enabling aminoacyl-tRNA synthetase and supports its relationship with IARS1 through STRING and hu.MAP. Its connection to the RNA-surveillance branch is a network-level observation rather than proof of direct physical or causal coupling.

#### ZC3HAV1

- **Related proteins** (co-abundance neighbors): PUM1 (0.86), SRP54 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger CCCH-type containing, antiviral 1. This gene encodes a CCCH-type zinc finger protein. This antiviral protein inhibits viral replication by recruiting cellular RNA degradation machineries to degrade viral mRNAs. The encoded protein plays an important role in the innate immune response against multiple DNA and RNA viruses, including Ebola virus, HIV and SARS-CoV-2 (which causes COVID-19). [provided by RefSeq, Sep 2021].
- **Diseases (Open Targets)**: cancer (0.549); hypothyroidism (0.429); neurodegenerative disease (0.358); autoimmune disease (0.308); Hashimoto thyroiditis (0.306)
- **Europe PMC papers**: 979
- **Why important**: ZC3HAV1 connects PUM1 and SRP54 in the module and has an established role in antiviral RNA degradation, interferon regulation, NF-kappaB signaling, and viral genome restriction. Its HPA tissue and cell-type-enhanced annotations distinguish it from the broadly expressed members and suggest that it may contribute context-sensitive regulation in reproductive or immune-adjacent cellular states. It also has disease associations involving cancer, autoimmunity, and neurodegeneration.
- **Conclusion**: Established evidence supports ZC3HAV1 as an inducible antiviral and RNA-decay regulator. Its position next to PUM1 makes it a plausible interface between general post-transcriptional control and antiviral defense. The module data do not establish that antiviral signaling is active in either tissue, so that interpretation remains conditional.

## Module 12

**Tissue pair**: cervix_uterine and ovary  
**Genes (7)**: PSMC2, SRPK1, LARS1, CCT5, CCT3, CCT7, CCT8

### Function

The strongest interpretation is an intracellular proteostasis and protein-folding module centered on the chaperonin-containing T-complex, with a secondary connection to proteasomal turnover, translation, and RNA-processing machinery. The primary GO evidence is highly coherent: CCT3, CCT5, CCT7, and CCT8 define the chaperonin-containing T-complex and ATP-dependent folding functions (GO:CC chaperonin-containing T-complex; q_global = 3.23e-06), (GO:CC protein folding chaperone complex; q_global = 0.000221), (GO:MF ATP-dependent protein folding chaperone; q_global = 0.000429), (GO:MF protein folding chaperone; q_global = 0.00214), (GO:MF unfolded protein binding; q_global = 0.00413), (GO:BP protein stabilization; q_global = 0.035), (GO:BP protein folding; q_global = 0.0459). The same four subunits account for the globally significant terms concerning nuclear-body and Cajal-body localization, telomerase-RNA localization, telomere maintenance, DNA biosynthesis, chromosome organization, and protein stabilization (7 globally significant GO/KEGG terms, q_global 3.23e-06–3.23e-06; see the table), (4 globally significant GO/KEGG terms, q_global 1.15e-05–1.15e-05; see the table), (5 globally significant GO/KEGG terms, q_global 5.31e-05–0.000148; see the table), (GO:BP RNA-templated DNA biosynthetic process; q_global = 0.000309) (GO:BP telomere maintenance via telomerase; q_global = 0.000309) (GO:BP telomere maintenance via telomere lengthening; q_global = 0.000429), (GO:BP regulation of DNA biosynthetic process; q_global = 0.000949) (GO:BP positive regulation of telomere maintenance; q_global = 0.00145), (9 globally significant GO/KEGG terms, q_global 0.00255–0.00907; see the table), (4 globally significant GO/KEGG terms, q_global 0.0301–0.035; see the table). These localization and telomere annotations should be interpreted as functional annotation of the CCT subunits, not as proof that the whole module directly regulates telomerase in cervix or ovary. The enrichment for fertilization, sperm–egg recognition, and zona-pellucida terms (GO:BP binding of sperm to zona pellucida; q_global = 1.15e-05), (GO:BP sperm-egg recognition; q_global = 2.8e-05), (GO:BP cell-cell recognition; q_global = 9.29e-05), (GO:BP cell recognition; q_global = 0.000577), (GO:BP single fertilization; q_global = 0.000756), (GO:BP fertilization; q_global = 0.00214), (GO:CC zona pellucida receptor complex; q_global = 0.0325) is also driven mainly by the same CCT genes and may reflect annotation overlap or reproductive-cell biology rather than a tissue-specific extracellular fertilization mechanism. LARS1 contributes aminoacyl-tRNA charging and SRPK1 contributes RNA-splicing regulation, while PSMC2 contributes ATP-dependent proteasomal activity. Overall, the module most plausibly reports coordinated abundance of a conserved cytosolic chaperone system embedded in broader protein synthesis, quality control, and nuclear RNA-processing activity.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It is also not predominantly blood-cell enriched; most genes have low immune-cell specificity, with SRPK1 showing immune-cell enhancement in basophils and expression in neutrophil-related cell types. All module proteins have broad tissue distribution, and HPA detects the proteins in cervix_uterine; all except LARS1 are detected in ovary. Several genes show enhancement in reproductive cell types, especially spermatocytes, spermatids, or oocytes, but the tissue-specificity profile is broadly low. Thus, the shared module is more consistent with a broadly expressed intracellular housekeeping and proteostasis program, with possible reproductive-cell contributions, than with a blood or plasma contamination signal. The reproductive-cell annotations should remain contextual because the analyzed tissues are cervix and ovary and the module does not establish which cell type produces the co-abundance pattern.

**GO/KEGG enrichment**: 53 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chaperonin-containing T-complex | 3.23e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 3.23e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 3.23e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 3.23e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 3.23e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 3.23e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 3.23e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 3.23e-06 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP binding of sperm to zona pellucida | 1.15e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to Cajal body | 1.15e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 1.15e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 1.15e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 1.15e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP sperm-egg recognition | 2.8e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 5.31e-05 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING provides direct, already-known relationships among the four CCT subunits: CCT3, CCT5, CCT7, and CCT8 form a densely connected subgraph (9 supplementary STRING terms; within-query FDR 2.74e-06–1.33e-05), and STRING also supports the CCT folding of actin and tubulin, association with target proteins during biosynthesis, and cooperation with folding machinery (5 supplementary STRING terms; within-query FDR 2.65e-05–3.73e-05). STRING additionally links CCT8 with PSMC2, but does not report the other module edges as established STRING relationships. hu.MAP independently places the four CCT subunits together in several complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1), with a lower-confidence complex containing three of them (hu.MAP huMAP3_01951.1). These complexes include other CCT components and factors involved in cytoskeletal folding, proteostasis, and protein-complex assembly. PSMC2, LARS1, and SRPK1 have no listed hu.MAP complex containing multiple module members, and only PSMC2 has a listed STRING partner within the module. Consequently, most of the module's apparent structure is explained by a known CCT core, whereas the links to proteasomal ATPase, leucyl-tRNA synthetase, and splicing kinase are weaker and may represent coordinated cellular state rather than one experimentally established physical complex.

**STRING interactions (score >= 0.7)**: 7 of 21 gene pairs: CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999); CCT8–PSMC2 (0.733)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam TCP-1/cpn60 chaperonin family (FDR = 2.74e-06, 4 genes); Component Chaperonin-containing T-complex (FDR = 9.55e-06, 4 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 9.93e-06, 4 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 1.33e-05, 4 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 1.33e-05, 4 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 1.33e-05, 4 genes); InterPro GroEL-like apical domain superfamily (FDR = 1.33e-05, 4 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 1.33e-05, 4 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 1.33e-05, 4 genes); RCTM Folding of actin by CCT/TriC (FDR = 2.65e-05, 4 genes); RCTM Association of TriC/CCT with target proteins during biosynthesis (FDR = 2.65e-05, 4 genes); RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding (FDR = 2.65e-05, 4 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis (FDR = 2.71e-05, 4 genes); RCTM Formation of tubulin folding intermediates by CCT/TriC (FDR = 3.73e-05, 4 genes); Process Binding of sperm to zona pellucida (FDR = 6.15e-05, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8)

### Novelty

The module should not be described as a newly discovered protein complex or as a new CCT mechanism. Its central relationships and its main functional interpretation are already well established by STRING, hu.MAP, and the gene annotations. What may be novel is the reproducible co-abundance of this CCT-centered set across cervix_uterine and ovary, together with its particular extensions toward PSMC2, LARS1, and SRPK1. However, the fact sheet does not provide an external atlas comparison, perturbation experiment, cell-resolved validation, or literature evidence for this exact tissue-pair module. Therefore the most defensible conclusion is that the tissue-pair co-abundance observation may be novel as a dataset-level association, but novelty of the biological mechanism is unproven. Absence of a complete module match in STRING or hu.MAP would not by itself establish novelty.

**Hypothesis.** Hypothesis: the shared cervix–ovary module reflects a conserved intracellular quality-control state in which the CCT chaperonin folds newly synthesized cytoskeletal and other client proteins, while PSMC2 supports removal of damaged or misfolded proteins, LARS1 supports translation capacity, and SRPK1 links the state to RNA processing. In reproductive-cell contexts, this proteostasis and biosynthetic program could support high protein-turnover demands and nuclear RNA or chromosome-related functions. The Cajal-body, telomerase, and fertilization annotations suggest testable biological connections, but they are not sufficient to claim that this module directly controls telomere maintenance, fertilization, or telomerase-RNA localization in either tissue. Testing should include cell-type-resolved abundance, measurement of complete CCT-complex components, proteasome and translation markers, and perturbation of the CCT core followed by assessment of the proposed downstream processes.

### Important genes

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT5 (0.90), CCT8 (0.84), PSMC2 (0.83); STRING partners: CCT5 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a central member of the module's CCT core, connects to CCT5, CCT8, and PSMC2, and has the greatest weighted network prominence among the listed genes. It participates in the globally significant chaperonin, protein-folding, protein-stabilization, nuclear-localization, telomere-related, and reproductive annotation groups (53 globally significant GO/KEGG terms, q_global 3.23e-06–0.0459; see the table). Its established function is ATP-dependent folding of client proteins, including actin and tubulin. It is represented across all listed hu.MAP CCT-containing complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1) and has substantial literature and disease-association support.
- **Conclusion**: Established evidence supports CCT3 as a structural and functional anchor of the module and as a marker of CCT-dependent proteostasis. A direct tissue-specific role for CCT3 in telomerase, fertilization, or cervix–ovary biology remains a hypothesis rather than an established conclusion.

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT7 (0.85), CCT3 (0.84), LARS1 (0.82); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999), PSMC2 (0.733)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is a core CCT subunit with strong links to CCT3 and CCT7 and the module's connection to LARS1. It is present in the principal hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1), is detected in both tissues, and has HPA enhancement in oocytes. It contributes to the globally significant chaperonin, folding, nuclear-localization, telomere, and fertilization annotation groups (53 globally significant GO/KEGG terms, q_global 3.23e-06–0.0459; see the table). Its established molecular role is participation in the CCT folding machine, while its position provides a plausible bridge between the chaperone core and translation-related biology.
- **Conclusion**: Established evidence supports CCT8 as a core component of the conserved chaperone signal and as a plausible contributor to reproductive-cell proteostasis. The association with LARS1 and any direct oocyte-specific mechanism should be treated as a hypothesis.

#### PSMC2

- **Related proteins** (co-abundance neighbors): CCT3 (0.83), SRPK1 (0.80); STRING partners: CCT8 (0.733)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is the module's proteasome ATPase component and connects the CCT-centered portion to SRPK1 while also showing a STRING link to CCT8. Its annotations support proteasomal protein catabolism, ubiquitin-dependent degradation, and oxidative-stress response, and it contributes to the globally significant ATP-related and intracellular-complex terms (GO:CC intracellular protein-containing complex; q_global = 0.0029), (4 globally significant GO/KEGG terms, q_global 0.0128–0.024; see the table), (GO:MF purine ribonucleoside triphosphate binding; q_global = 0.0355) (GO:MF purine ribonucleotide binding; q_global = 0.0361) (GO:MF ribonucleotide binding; q_global = 0.0378). HPA detects it in both tissues, with enhancement in syncytiotrophoblasts. It has substantial literature and disease-association support.
- **Conclusion**: Established evidence supports PSMC2 as a protein-quality-control partner that broadens the module beyond folding toward degradation. The module does not establish a direct physical CCT–proteasome complex or show that PSMC2 activity drives the tissue-pair association.

#### LARS1

- **Related proteins** (co-abundance neighbors): CCT8 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: leucyl-tRNA synthetase 1. This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals w…
- **Diseases (Open Targets)**: infantile liver failure syndrome 1 (0.670); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.510); Global developmental delay (0.119); sensorineural hearing loss disorder (0.119); Generalized-onset seizure (0.118)
- **Europe PMC papers**: 267
- **Why important**: LARS1 is the module's leucyl-tRNA synthetase and is connected to CCT8. Its established function is ATP-dependent charging of leucine onto transfer RNA within the cytosolic translation system, and it contributes to the shared ATP- and ribonucleotide-binding annotations (GO:CC intracellular protein-containing complex; q_global = 0.0029), (GO:MF ATP binding; q_global = 0.0128) (GO:MF adenyl ribonucleotide binding; q_global = 0.0131) (GO:MF adenyl nucleotide binding; q_global = 0.0229), (GO:MF purine ribonucleoside triphosphate binding; q_global = 0.0355) (GO:MF purine ribonucleotide binding; q_global = 0.0361) (GO:MF ribonucleotide binding; q_global = 0.0378). It has a clear disease association with infantile liver failure syndrome and a meaningful literature base, although it is not included in the listed hu.MAP complexes and has no listed STRING partner.
- **Conclusion**: Established evidence supports LARS1 as an indicator of translation and amino-acid-response capacity rather than as a CCT-complex subunit. Its co-abundance with CCT8 may reflect coordinated biosynthetic demand, but a direct mechanistic interaction is unproven.

#### SRPK1

- **Related proteins** (co-abundance neighbors): PSMC2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine, ovary
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SRSF protein kinase 1. This gene encodes a serine/arginine protein kinase specific for the SR (serine/arginine-rich domain) family of splicing factors. The protein localizes to the nucleus and the cytoplasm. It is thought to play a role in regulation of both constitutive and alternative splicing by regulating intracellular localization of splicing factors. Alternative splicing of this gene results in multiple transcript…
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); COVID-19 (0.372); celiac disease (0.190); ulcerative colitis (0.132); type 1 diabetes mellitus (0.123)
- **Europe PMC papers**: 1777
- **Why important**: SRPK1 is the module's RNA-processing kinase and connects to PSMC2. It regulates SR-family splicing factors and is annotated for RNA splicing, spliceosomal assembly, phosphorylation, chromosome segregation, and sperm DNA condensation. It contributes to the sexual-reproduction and ATP-binding groups (4 globally significant GO/KEGG terms, q_global 0.0105–0.0229; see the table), (GO:MF purine ribonucleoside triphosphate binding; q_global = 0.0355) (GO:MF purine ribonucleotide binding; q_global = 0.0361) (GO:MF ribonucleotide binding; q_global = 0.0378). HPA shows enhancement in reproductive cell types as well as selected immune and urothelial cell types, and the gene has a substantial literature and disease-association record.
- **Conclusion**: Established evidence supports SRPK1 as a plausible RNA-processing component of the module, distinct from the CCT core. Its reproductive-cell signal may be relevant to the shared tissue context, but it does not demonstrate that SRPK1 mediates the CCT–proteasome association or the telomere annotations.
