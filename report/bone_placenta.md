# Conserved co-abundance modules: bone and placenta

## Module 0

**Tissue pair**: bone and placenta  
**Genes (13)**: PGD, LAP3, CNDP2, DPYSL2, FSCN1, LTA4H, PDLIM1, NARS1, SARS1, TARS1, CCT5, CCT3, ACAT2

### Function

The module appears to represent a coordinated intracellular biosynthetic, proteostasis, metabolic, and cytoskeletal state rather than a single established pathway. SARS1, TARS1, and NARS1 are cytoplasmic aminoacyl-tRNA synthetases, supporting protein translation capacity. CCT3 and CCT5 are subunits of the CCT/TRiC chaperonin, supporting ATP-dependent folding of proteins including actin and tubulin. PGD supports oxidative pentose-phosphate metabolism and NADPH regeneration; CNDP2 and LAP3 support peptide or dipeptide processing; LTA4H connects the module to leukotriene biosynthesis, peptide catabolism, and inflammatory biology; PDLIM1, DPYSL2, and FSCN1 connect it to actin, microtubule, polarity, and cell-migration processes; and ACAT2 connects it to lipid metabolism. The strongest interpretation is therefore a cellular maintenance and remodeling program combining translation, protein folding, redox support, cytoskeletal organization, and context-dependent inflammatory or migratory functions. No GO/KEGG term passed global correction, so the functional interpretation is based on the annotated genes and network structure rather than on statistically significant pathway enrichment.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the individual proteins are predominantly cytosolic, cytoskeletal, or membrane-associated. Most genes have low tissue specificity, which is consistent with broadly used cellular machinery rather than a placenta-exclusive or bone-exclusive program. The module is not uniformly blood-cell specific, although several genes show enrichment or enhancement in myeloid, granulocyte, platelet, or related cell populations. HPA also links subsets of the module to Hofbauer cells, monocytes, neutrophils, dendritic cells, megakaryocytes, and platelets, while other genes are associated with esophageal, brain, skeletal-muscle, liver, or lactating-cell contexts. All module proteins were detected by HPA immunohistochemistry in placenta, whereas the fact sheet provides no matching HPA tissue result for bone. Consequently, the shared bone–placenta signal could reflect a conserved intracellular program, shared stromal or vascular biology, or shared immune and myeloid cell admixture; the data do not justify assigning it specifically to osteoblasts or trophoblasts.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a connected aminoacyl-tRNA-synthetase subnetwork: NARS1 is linked to CNDP2, SARS1, and TARS1, while SARS1 and TARS1 are strongly linked to each other. STRING also supports the CCT3–CCT5 relationship and a CCT5–TARS1 relationship. These relationships are consistent with known functional or physical associations, but STRING provides no functional-enrichment result for this module and does not directly validate every module edge. hu.MAP provides the clearest complex-level support. (hu.MAP huMAP3_01951.1) through (hu.MAP huMAP3_14584.1) repeatedly place CCT3 and CCT5 in CCT-, chaperonin-, cytoskeletal-, and associated assembly contexts, indicating that their co-abundance is consistent with known multiprotein-complex biology. (hu.MAP huMAP3_14442.1) places PDLIM1, LTA4H, LAP3, and PGD in the same reported complex, providing a second, broader connection among cytoskeletal, inflammatory, peptidase, and metabolic proteins. However, most module genes are absent from the listed hu.MAP complexes, and the complex memberships are partial. Thus, known interactions explain important islands of the network, while the full cross-functional module remains an expression-level association rather than a demonstrated physical complex.

**STRING interactions (score >= 0.7)**: 6 of 78 gene pairs: CCT3–CCT5 (0.999); CCT5–TARS1 (0.727); CNDP2–NARS1 (0.856); NARS1–SARS1 (0.843); NARS1–TARS1 (0.924); SARS1–TARS1 (0.915)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (PDLIM1, LTA4H, LAP3, PGD; 4/57); huMAP3_01951.1 (CCT5, CCT3; 2/8); huMAP3_07938.1 (CCT5, CCT3; 2/23); huMAP3_06559.1 (CCT5, CCT3; 2/25); huMAP3_09191.1 (CCT5, CCT3; 2/32); huMAP3_10656.1 (CCT5, CCT3; 2/36); huMAP3_14584.1 (CCT5, CCT3; 2/61)

### Novelty

The module may be a useful cross-tissue co-abundance observation, but it cannot be called a newly discovered molecular complex or pathway from the available evidence. Its novelty lies mainly in the specific bone–placenta co-abundance configuration and in the joint behavior of translation, chaperoning, redox, cytoskeletal, and inflammatory genes. The CCT3–CCT5 pair, the aminoacyl-tRNA-synthetase relationships, and the hu.MAP memberships in (hu.MAP huMAP3_14442.1) through (hu.MAP huMAP3_14584.1) are already supported by external interaction or complex resources. Conversely, the absence of a STRING edge, hu.MAP membership, or enrichment term for other genes does not establish that those relationships are novel. A defensible conclusion is that the cross-tissue module is a potentially interesting integrative association that requires replication, cell-composition adjustment, and targeted physical or perturbational validation before being considered a novel mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in bone and placenta in which metabolically active or remodeling cells increase translational capacity and protein-folding capacity while maintaining NADPH-dependent redox support and cytoskeletal remodeling. Within this state, PGD could support reducing power, CCT3 and CCT5 could support folding of cytoskeletal and other newly synthesized proteins, SARS1 and TARS1 could support translation, and PDLIM1, DPYSL2, or FSCN1 could organize actin or microtubule-dependent morphology and migration. LTA4H could add an inflammatory or leukocyte-associated component, potentially reflecting myeloid-cell participation rather than a universal property of bone or placenta parenchymal cells. CNDP2, LAP3, and ACAT2 could provide peptide-processing and lipid-metabolic support. This is a mechanistic hypothesis, not a demonstrated causal pathway; it should be tested by cell-type-resolved replication, comparison with purified bone and placental populations, and perturbation of the proposed translation, chaperone, redox, or cytoskeletal components.

### Important genes

#### SARS1

- **Related proteins** (co-abundance neighbors): TARS1 (0.90), DPYSL2 (0.90), LTA4H (0.89), CNDP2 (0.87), CCT5 (0.86), PGD (0.84), PDLIM1 (0.81); STRING partners: NARS1 (0.843), TARS1 (0.915)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: seryl-tRNA synthetase 1. This gene belongs to the class II amino-acyl tRNA family. The encoded enzyme catalyzes the transfer of L-serine to tRNA (Ser) and is related to bacterial and yeast counterparts. Multiple alternatively spliced transcript variants have been described but the biological validity of all variants is unknown. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, ataxia, and seizures (0.670); autosomal recessive non-syndromic intellectual disability (0.370); autosomal recessive primary microcephaly (0.370); arteriovenous malformations of the brain (0.340); hereditary peripheral neuropathy (0.118)
- **Europe PMC papers**: 400
- **Why important**: SARS1 has the strongest network position in the module, connecting the aminoacyl-tRNA-synthetase group with DPYSL2, LTA4H, CNDP2, CCT5, PGD, and PDLIM1. Its established function is cytoplasmic serine-tRNA aminoacylation and participation in translation, with additional annotations involving tRNA modification and selenium-related metabolism. It has strong disease relevance in neurodevelopmental and neurological disorders and substantial literature support. Its STRING links to NARS1 and TARS1 reinforce a known translation-related interaction neighborhood, although it has no listed hu.MAP membership.
- **Conclusion**: Established evidence supports SARS1 as a central translation-related hub and a plausible marker of cellular biosynthetic demand. It is reasonable to hypothesize that SARS1 helps couple the translation subnetwork to the broader module, but the fact sheet does not establish that it drives the bone–placenta association.

#### TARS1

- **Related proteins** (co-abundance neighbors): LTA4H (0.92), SARS1 (0.90), PGD (0.90), CNDP2 (0.87), DPYSL2 (0.80), CCT5 (0.80); STRING partners: CCT5 (0.727), NARS1 (0.924), SARS1 (0.915)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: threonyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Threonyl-tRNA synthetase belongs to the class-II aminoacyl-tRNA synthetase family [provided by RefSeq, Jul 2008]…
- **Diseases (Open Targets)**: trichothiodystrophy 7, nonphotosensitive (0.520); trichothiodystrophy (0.430); actinic keratosis (0.356); dyshidrosis (0.315); placental abruption (0.307)
- **Europe PMC papers**: 147
- **Why important**: TARS1 is a high-connectivity bridge linking SARS1, NARS1, CCT5, PGD, CNDP2, LTA4H, and DPYSL2. Its established role is threonine-tRNA aminoacylation for protein translation. STRING independently supports its relationships with NARS1, SARS1, and CCT5, making it one of the best-supported molecular connectors in the module. It also has disease associations involving trichothiodystrophy and a reported association with placental abruption.
- **Conclusion**: Established evidence supports TARS1 as a translation-related network bridge rather than a tissue-specific effector. Its position makes it a strong candidate for testing whether increased protein synthesis capacity contributes to the shared module, but causality and placental relevance remain unproven.

#### PGD

- **Related proteins** (co-abundance neighbors): CNDP2 (0.94), TARS1 (0.90), LTA4H (0.85), SARS1 (0.84), FSCN1 (0.82), ACAT2 (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: phosphogluconate dehydrogenase. 6-phosphogluconate dehydrogenase is the second dehydrogenase in the pentose phosphate shunt. Deficiency of this enzyme is generally asymptomatic, and the inheritance of this disorder is autosomal dominant. Hemolysis results from combined deficiency of 6-phosphogluconate dehydrogenase and 6-phosphogluconolactonase suggesting a synergism of the two enzymopathies. Several transcript variants encoding…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); Abnormality of the skeletal system (0.329); autoimmune disorder of central nervous system (0.246); smoking behavior (0.245); essential hypertension (0.199)
- **Europe PMC papers**: 8652
- **Why important**: PGD is a highly connected metabolic hub linking CNDP2, TARS1, LTA4H, SARS1, FSCN1, and ACAT2. It catalyzes a step in the oxidative pentose-phosphate pathway and supports NADPH regeneration. HPA gives PGD a group-enriched tissue pattern involving bone marrow and esophagus, enhanced association with neutrophil-related cell types, and blood-cell enrichment involving basophils, monocytes, eosinophils, and neutrophils. It is also the most extensively studied gene among the selected candidates and has an established association with hemolysis in deficiency contexts.
- **Conclusion**: Established evidence supports PGD as a metabolic and possible cell-composition indicator. Its module position suggests that redox metabolism may connect the translation and remodeling components, but the apparent bone–placenta signal could also be influenced by myeloid or granulocyte content.

#### LTA4H

- **Related proteins** (co-abundance neighbors): TARS1 (0.92), SARS1 (0.89), PGD (0.85), CNDP2 (0.84), DPYSL2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: leukotriene A4 hydrolase. The protein encoded by this gene is an enzyme that contains both hydrolase and aminopeptidase activities. The hydrolase activity is used in the final step of the biosynthesis of leukotriene B4, a proinflammatory mediator. The aminopeptidase activity has been shown to degrade proline-glycine-proline (PGP), a neutrophil chemoattractant and biomarker for chronic obstructive pulmonary disease (COPD). …
- **Diseases (Open Targets)**: hypotensive disorder (0.198); small intestine neuroendocrine neoplasm (0.150); cystic fibrosis (0.104); COVID-19 (0.096); hepatocellular carcinoma (0.086)
- **Europe PMC papers**: 1823
- **Why important**: LTA4H is a high-connectivity bridge between translation-related genes, PGD, CNDP2, and DPYSL2. Its established activities include leukotriene B4 biosynthesis and aminopeptidase-mediated degradation of proline-glycine-proline, a neutrophil chemoattractant. HPA links it to monocytes and neutrophil progenitors as well as other cell contexts. It is present with PGD, LAP3, and PDLIM1 in (hu.MAP huMAP3_14442.1), and it has substantial literature concerning inflammatory and proteolytic biology.
- **Conclusion**: Established evidence supports LTA4H as an inflammatory and peptidase-related component that may connect cellular metabolism to immune-cell behavior. Its inclusion supports an immune or remodeling interpretation, but it does not prove that leukotriene signaling is the principal function of the complete module.

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT3 (0.91), SARS1 (0.86), TARS1 (0.80); STRING partners: CCT3 (0.999), TARS1 (0.727)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_01951.1, huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is directly paired with CCT3 in STRING and appears with CCT3 across (hu.MAP huMAP3_01951.1) through (hu.MAP huMAP3_14584.1), making the CCT pair the most consistently represented known complex relationship in the module. CCT5 is an established subunit of the CCT/TRiC chaperonin, which folds proteins including actin and tubulin. It also connects in the module to SARS1 and TARS1, linking protein folding to translation-related genes. Its disease associations include hereditary sensory and autonomic neuropathy with spastic paraplegia and neurodegenerative disease, with substantial literature support.
- **Conclusion**: Established evidence supports CCT5 as a protein-homeostasis and cytoskeletal-folding component with strong complex-level validation. It is a plausible mechanistic bridge between increased translation and cytoskeletal remodeling, but the module does not show that CCT5 activity is altered or causal in either tissue.

## Module 1

**Tissue pair**: bone and placenta  
**Genes (9)**: DBI, COTL1, GSTP1, JPT1, MDH1, NME1, STMN1, TAGLN2, TAGLN

### Function

The module has no GO or KEGG term passing global correction. Therefore, its function cannot be assigned from statistically significant pathway enrichment. The network nevertheless contains coherent functional themes: cytoskeletal remodeling through STMN1, TAGLN2, TAGLN, and COTL1; cellular redox and xenobiotic handling through GSTP1; central carbon metabolism through MDH1; nucleotide metabolism through NME1; lipid handling through DBI; and microtubule-associated biology through JPT1. The strongest within-module connectivity is concentrated around JPT1 and STMN1, with additional links joining actin-associated, stress-response, and metabolic proteins. These annotations support a cautious interpretation as a cell-state or cellular remodeling module rather than a demonstrated single biochemical pathway. The absence of enriched GO or KEGG terms does not invalidate the module.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary identifies no secreted genes. It is also not uniformly blood-cell specific, because most genes have low immune-cell specificity, although COTL1 and TAGLN show group-enriched blood-cell patterns and several genes are associated with monocytes, neutrophils, or other immune cells. All genes have cell-type-enhanced HPA annotations, with recurring signals in extravillous trophoblasts, Hofbauer cells, esophageal epithelial populations, and spermatogenic cells. Six genes are tissue enhanced and the remainder have low tissue specificity. Placental protein detection is reported for most of the module, whereas bone protein data are unavailable in the fact sheet. The shared bone–placenta signal may therefore reflect placental or stromal cellular composition, trophoblast or Hofbauer-cell contribution, immune-cell admixture, or a broadly reused cellular state rather than a bone–placenta-specific pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction reaches the stated high-confidence threshold for any module gene pair, and STRING reports no supplementary enrichment. No hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not supported by corresponding high-confidence protein associations or a known shared complex in these resources. This suggests that the module captures coordinated abundance, cell composition, regulation, or context-dependent biology rather than a validated physical protein complex. The lack of STRING and hu.MAP support also means that the network should not be described as a confirmed interaction network.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is a potentially interesting co-abundance observation, but it is not established as a new molecular mechanism. Its novelty is supported only in the limited sense that this particular bone–placenta module is not represented as a high-confidence STRING interaction set or a hu.MAP multi-member complex. That absence does not prove novelty, because co-abundance relationships can arise from shared cell types, correlated regulation, common stress states, or technical and sampling effects. Several component functions are already well established, including STMN1 microtubule regulation, TAGLN cytoskeletal biology, GSTP1 detoxification, MDH1 metabolism, and DBI lipid handling. Published and indexed web evidence also links TAGLN with osteoblastic differentiation and STMN1 with bone repair biology, while JPT1 has prior microtubule-related characterization. The defensible conclusion is that the cross-tissue combination and its coordinated abundance pattern may be novel, but the module requires independent replication, cell-resolved analysis, and perturbation before being claimed as a new mechanism.

**Hypothesis.** Hypothesis: the module represents a shared remodeling state involving cytoskeletal reorganization, microtubule turnover, redox protection, intermediary metabolism, and nucleotide or lipid supply in placental and bone-associated cells. STMN1 and JPT1 may coordinate microtubule-state changes, while TAGLN2, TAGLN, and COTL1 may reflect actin remodeling and altered cell shape or motility. GSTP1 may buffer oxidative or electrophilic stress, with MDH1 and DBI supporting metabolic adaptation. In placenta, this state could arise in trophoblast, Hofbauer, vascular, or stromal compartments; in bone, it could occur in stromal, vascular, or immune-associated cells. This is a mechanistic hypothesis, not an inference established by enrichment or protein-interaction evidence.

Web sources: https://www.omim.org/entry/619242; https://www.sciencedirect.com/science/article/pii/S0006295224006944; https://www.nature.com/articles/s41698-026-01633-5.pdf; https://www.nature.com/articles/cddis2016196

### Important genes

#### STMN1

- **Related proteins** (co-abundance neighbors): JPT1 (0.91), COTL1 (0.90), TAGLN2 (0.88), NME1 (0.86), GSTP1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: stathmin 1. This gene belongs to the stathmin family of genes. It encodes a ubiquitous cytosolic phosphoprotein proposed to function as an intracellular relay integrating regulatory signals of the cellular environment. The encoded protein is involved in the regulation of the microtubule filament system by destabilizing microtubules. It prevents assembly and promotes disassembly of microtubules. Multiple trans…
- **Diseases (Open Targets)**: exostosis (0.162); neoplasm (0.116); hepatocellular carcinoma (0.116); non-small cell lung carcinoma (0.113); breast carcinoma (0.112)
- **Europe PMC papers**: 4603
- **Why important**: STMN1 is among the most connected genes in the module and links JPT1, COTL1, TAGLN2, NME1, and GSTP1. Its established function is regulation of microtubule assembly and disassembly, with roles in mitotic organization and cellular signaling. It has extensive literature and disease-association evidence, and the web search returned evidence connecting STMN1-related biology with bone repair and an osteosarcoma metastasis axis. Its HPA pattern includes placenta, extravillous trophoblasts, Hofbauer cells, and lymphoid tissue.
- **Conclusion**: Established evidence supports STMN1 as a central cytoskeletal and proliferative-state marker in this module. It is a plausible coordinator of the observed co-abundance pattern, but the module does not establish that STMN1 drives bone–placenta biology or that it causes the other genes to change.

#### JPT1

- **Related proteins** (co-abundance neighbors): COTL1 (0.96), STMN1 (0.91), TAGLN2 (0.88), MDH1 (0.88), DBI (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Jupiter microtubule associated homolog 1. Located in nuclear membrane; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.099); cancer (0.089); breast carcinoma (0.083); breast cancer (0.082); neoplasm (0.081)
- **Europe PMC papers**: 180
- **Why important**: JPT1 has the strongest network connectivity in the module and links cytoskeletal, metabolic, and stress-related members. The fact sheet describes it as a microtubule-associated or nuclear-associated protein, while the web search identified prior characterization as a microtubule-binding protein. Its HPA signal includes placenta, extravillous trophoblasts, and early spermatids, and it is one of the less extensively studied genes relative to STMN1, GSTP1, TAGLN, or DBI.
- **Conclusion**: Established evidence supports JPT1 as a highly connected microtubule-associated candidate. Its central network position makes it important for follow-up, but the absence of STRING and hu.MAP support means that any direct physical or regulatory role in this module remains hypothetical.

#### TAGLN2

- **Related proteins** (co-abundance neighbors): JPT1 (0.88), STMN1 (0.88), TAGLN (0.83), GSTP1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transgelin 2. The protein encoded by this gene is similar to the protein transgelin, which is one of the earliest markers of differentiated smooth muscle. The specific function of this protein has not yet been determined, although it is thought to be a tumor suppressor. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2013].
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); neoplasm (0.112); central nervous system cancer (0.108); glioma (0.108); cancer (0.105)
- **Europe PMC papers**: 1580
- **Why important**: TAGLN2 occupies a highly connected position and bridges JPT1, STMN1, TAGLN, and GSTP1. Its annotation supports actin filament organization and epithelial differentiation, and its HPA profile points to extravillous trophoblasts, megakaryocytes, and platelets. It therefore provides a plausible link between cytoskeletal remodeling and the cellular populations recurring in the module.
- **Conclusion**: Established evidence supports TAGLN2 as an actin-associated component compatible with altered cell shape or motility. Its participation in a bone–placenta mechanism is not established, and its association may instead reflect shared trophoblast, epithelial, or platelet-related cellular states.

#### COTL1

- **Related proteins** (co-abundance neighbors): JPT1 (0.96), STMN1 (0.90), NME1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coactosin like F-actin binding protein 1. This gene encodes one of the numerous actin-binding proteins which regulate the actin cytoskeleton. This protein binds F-actin, and also interacts with 5-lipoxygenase, which is the first committed enzyme in leukotriene biosynthesis. Although this gene has been reported to map to chromosome 17 in the Smith-Magenis syndrome region, the best alignments for this gene are to chromosome 16. The Smith-Ma…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.419); placental abruption (0.272); placenta praevia (0.272); placental retention (0.267); cervical carcinoma (0.262)
- **Europe PMC papers**: 1073
- **Why important**: COTL1 connects JPT1, STMN1, and NME1 and is annotated as an F-actin-binding protein involved in regulation of actin polymerization. It has a strong immune and myeloid HPA pattern, including monocyte, eosinophil, neutrophil, dendritic-cell, Hofbauer-cell, and extravillous-trophoblast associations. The fact sheet also links it to skeletal-system abnormality and placental disorders in Open Targets.
- **Conclusion**: Established evidence supports COTL1 as an actin-regulatory and immune-associated gene that could mark myeloid or Hofbauer-cell contribution. The module may therefore partly reflect shared immune-cell composition. A direct role for COTL1 in coordinating the entire module remains a hypothesis.

#### GSTP1

- **Related proteins** (co-abundance neighbors): MDH1 (0.90), STMN1 (0.85), TAGLN2 (0.82), TAGLN (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutathione S-transferase pi 1. Glutathione S-transferases (GSTs) are a family of enzymes that play an important role in detoxification by catalyzing the conjugation of many hydrophobic and electrophilic compounds with reduced glutathione. Based on their biochemical, immunologic, and structural properties, the soluble GSTs are categorized into 4 main classes: alpha, mu, pi, and theta. This GST family member is a polymorphic gene…
- **Diseases (Open Targets)**: neurodegenerative disease (0.350); breast cancer (0.117); hepatocellular carcinoma (0.115); neoplasm (0.114); posterior cortical atrophy (0.113)
- **Europe PMC papers**: 12759
- **Why important**: GSTP1 links MDH1, STMN1, TAGLN2, and TAGLN and has the largest literature volume among the module genes in the fact sheet. Its established biochemical role is glutathione-dependent detoxification, with annotations for oxidative-stress response, inflammatory regulation, and xenobiotic metabolism. Its HPA profile is enriched in esophageal epithelial populations and includes placenta, making it a plausible marker of epithelial or stress-adapted cellular states.
- **Conclusion**: Established evidence supports GSTP1 as a redox and detoxification component that may indicate oxidative or inflammatory adaptation. Its network association with cytoskeletal genes is compatible with a shared cell state, but it does not demonstrate that oxidative stress is the causal organizing mechanism of the module.

## Module 2

**Tissue pair**: bone and placenta  
**Genes (19)**: ACO2, ANXA1, ANXA5, ATP5F1B, HSPA5, CANX, CLTC, TUFM, EZR, GANAB, HYOU1, PDIA4, PRDX3, PRDX4, RRBP1, RTN4, SEPTIN7, CCT8, TXNDC5

### Function

The module is best interpreted as an endoplasmic-reticulum protein folding, glycoprotein maturation, disulfide-bond formation, and quality-control program. The primary evidence is the globally significant KEGG term for protein processing in the endoplasmic reticulum (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0254), which includes CANX, GANAB, HSPA5, HYOU1, PDIA4, RRBP1, and TXNDC5. This interpretation is reinforced, but not independently treated as global significance, by the supplementary STRING terms for the endoplasmic reticulum, unfolded-protein-response and quality-control neighborhoods, protein-disulfide-isomerase activity, and the same KEGG pathway (4 supplementary STRING terms; within-query FDR 0.0066–0.0349). The module also contains a smaller mitochondrial and oxidative-stress-associated component involving ATP5F1B, ACO2, TUFM, and PRDX3, plus trafficking, membrane, cytoskeletal, and annexin-associated genes. Thus, the most parsimonious function is secretory-cell proteostasis with links to energy production, redox control, and intracellular trafficking rather than a narrowly specific bone or placental differentiation pathway.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the fact sheet identifies a minority of genes as secreted, while many of the best-supported members are intracellular or endoplasmic-reticulum proteins. HPA indicates broadly distributed expression for most genes, with several cell-type-enhanced genes. Extravillous trophoblasts and syncytiotrophoblasts are recurrent enriched cell types, consistent with a placental secretory-cell contribution. Plasma cells are also recurrent, and TXNDC5 has enrichment involving B-cell and plasmacytoid-dendritic-cell populations. Nevertheless, most genes have low immune-cell specificity, so a general blood-cell explanation is not sufficient. The recurrent trophoblast and plasma-cell signals mean that the shared bone–placenta module could partly reflect common secretory or antibody-producing cell types, sample composition, or cellular stress rather than a process uniquely shared by osteogenic and placental cells. Protein detection is present for nearly all genes in placenta, whereas the fact sheet provides no matching HPA bone tissue for direct protein comparison; therefore the bone interpretation should remain cautious.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human) | 0.0254 | CANX, GANAB, HSPA5, HYOU1, PDIA4, RRBP1, TXNDC5 |

### STRING and hu.MAP

STRING shows a dense, biologically coherent core centered on CANX, HSPA5, HYOU1, PDIA4, GANAB, TXNDC5, and PRDX4. The strongest relationships include chaperone and ER-quality-control links such as CANX–HSPA5, HSPA5–HYOU1, HSPA5–PDIA4, HYOU1–PDIA4, CANX–PDIA4, and PRDX4–TXNDC5. A separate group connects ACO2, ATP5F1B, TUFM, and PRDX3, consistent with mitochondrial energy production and redox control. hu.MAP independently places PDIA4, GANAB, and HYOU1 together in two large complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), HSPA5 with HYOU1 in an ER-associated complex (hu.MAP huMAP3_07455.1), and PRDX3 with PRDX4 in an antioxidant complex (hu.MAP huMAP3_12666.1). These results show that much of the module corresponds to already recognized protein interactions and complex membership. The co-abundance module therefore appears biologically grounded, but the databases support the molecular machinery more directly than they establish a tissue-specific regulatory mechanism.

**STRING interactions (score >= 0.7)**: 15 of 171 gene pairs: ACO2–ATP5F1B (0.874); ATP5F1B–TUFM (0.84); CANX–GANAB (0.953); CANX–HSPA5 (0.998); CANX–HYOU1 (0.869); CANX–PDIA4 (0.931); CCT8–HSPA5 (0.701); GANAB–HSPA5 (0.846); GANAB–HYOU1 (0.83); GANAB–PDIA4 (0.717); HSPA5–HYOU1 (0.999); HSPA5–PDIA4 (0.99); HSPA5–TXNDC5 (0.798); HYOU1–PDIA4 (0.997); PRDX4–TXNDC5 (0.994)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Mixed, incl. Photodynamic therapy-induced unfolded protein response, and Endoplasmic reticulum quality control compartment (FDR = 0.0066, 7 genes); Keyword Endoplasmic reticulum (FDR = 0.01, 8 genes); NetworkNeighborAL Mixed, incl. Photodynamic therapy-induced unfolded protein response, and Protein disulfide isomerase activity (FDR = 0.0257, 5 genes); KEGG Protein processing in endoplasmic reticulum (FDR = 0.0349, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (PDIA4, GANAB, HYOU1; 3/60); huMAP3_09327.1 (PDIA4, GANAB, HYOU1; 3/93); huMAP3_07455.1 (HSPA5, HYOU1; 2/4); huMAP3_12666.1 (PRDX3, PRDX4; 2/5)

### Novelty

The fact sheet does not justify calling this a wholly new molecular pathway. Most of its central ER relationships and several complex associations are already represented in STRING or hu.MAP, and the functional interpretation is concordant with established protein-folding and ER-quality-control biology. A potentially novel aspect is the coordinated co-abundance of this machinery across bone and placenta, especially the combination of ER proteostasis, mitochondrial metabolism, redox control, and secretory-cell composition. However, absence of a particular edge or complex annotation cannot establish novelty, and no literature search or independent cross-tissue replication is supplied here. The defensible conclusion is that the module may represent a new tissue-pair-level co-abundance observation built largely from known molecular machinery, rather than a demonstrably new pathway or interaction network.

**Hypothesis.** Hypothesis: the module marks an adaptive secretory-cell proteostasis state shared between placental trophoblast-rich samples and a cellular component present in bone samples. High secretory load or local stress could increase ER chaperoning and glycoprotein processing through HSPA5, CANX, GANAB, PDIA4, HYOU1, RRBP1, and TXNDC5, while PRDX4 and PRDX3 buffer peroxide and thiol stress. ATP5F1B, ACO2, and TUFM could provide or maintain mitochondrial energy and translation capacity for this response. ANXA1, ANXA5, CLTC, EZR, and SEPT7 may connect the state to membrane trafficking, inflammatory regulation, and cell architecture. This hypothesis predicts that the module will track secretory-cell abundance and ER-stress or hypoxia markers more strongly than it will track a bone-specific or placenta-specific lineage program; it requires validation with cell-resolved expression, independent cohorts, and perturbation experiments.

### Important genes

#### HSPA5

- **Related proteins** (co-abundance neighbors): ATP5F1B (0.91), TUFM (0.86), CANX (0.82), HYOU1 (0.82), RTN4 (0.82), TXNDC5 (0.80); STRING partners: CANX (0.998), CCT8 (0.701), GANAB (0.846), HYOU1 (0.999), PDIA4 (0.99), TXNDC5 (0.798)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_07455.1
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is a central ER chaperone and a stated master regulator of ER homeostasis. It is connected in STRING to CANX, GANAB, HYOU1, PDIA4, TXNDC5, and CCT8, and it participates in the primary globally significant ER-processing term (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0254) as well as all supplementary STRING terms (4 supplementary STRING terms; within-query FDR 0.0066–0.0349). Its very large literature base and associations with ER stress, infection, neurodegeneration, and neoplasia make it the most informative anchor for the module.
- **Conclusion**: Established evidence supports HSPA5 as a core component of ER folding, assembly, and unfolded-protein-response biology in this module. The hypothesis that its co-abundance specifically reflects trophoblast or plasma-cell secretory load is plausible from HPA cell-type enrichment, but is not demonstrated by the module alone.

#### CANX

- **Related proteins** (co-abundance neighbors): HYOU1 (0.95), GANAB (0.89), CCT8 (0.87), ANXA1 (0.87), PDIA4 (0.86), TXNDC5 (0.85), SEPTIN7 (0.85), ATP5F1B (0.83), HSPA5 (0.82), ACO2 (0.82); STRING partners: GANAB (0.953), HSPA5 (0.998), HYOU1 (0.869), PDIA4 (0.931)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX has one of the strongest network positions and connects to HSPA5, HYOU1, GANAB, PDIA4, TXNDC5, and other module members. It is an ER calcium-binding chaperone that assists folding and assembly of newly synthesized glycoproteins and retains misfolded products. It contributes to (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0254) and to the supplementary ER and quality-control terms (STRING NetworkNeighborAL Mixed, incl. Photodynamic therapy-induced unfolded protein response, and Endoplasmic reticulum quality control compartment; within-query FDR = 0.0066), (STRING Keyword Endoplasmic reticulum; within-query FDR = 0.01), and (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0349), with substantial literature support.
- **Conclusion**: Established evidence identifies CANX as a central glycoprotein-folding and ER-quality-control component. Its network position supports a structural role in the module; a specific role in coordinating bone and placental biology remains a hypothesis.

#### PDIA4

- **Related proteins** (co-abundance neighbors): ACO2 (0.91), CANX (0.86), HYOU1 (0.84), GANAB (0.83), ATP5F1B (0.83), PRDX4 (0.82); STRING partners: CANX (0.931), GANAB (0.717), HSPA5 (0.99), HYOU1 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 is a highly connected ER member linked to CANX, GANAB, HSPA5, HYOU1, and PRDX4. It catalyzes thiol-disulfide interchange and is involved in protein folding, secretion, and ER-stress responses. It belongs to the primary ER-processing term (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0254), all the supplementary STRING terms (4 supplementary STRING terms; within-query FDR 0.0066–0.0349), and two hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Its annotation also connects it to immunoglobulin disulfide bonding and antibody assembly, relevant to the plasma-cell signal.
- **Conclusion**: Established evidence supports PDIA4 as a core oxidative protein-folding enzyme and a bridge between ER proteostasis and secretory-cell biology. A contribution to antibody-producing or trophoblast-associated secretory activity is supported only indirectly by cell-type enrichment and should be tested experimentally.

#### HYOU1

- **Related proteins** (co-abundance neighbors): CANX (0.95), TXNDC5 (0.91), RRBP1 (0.89), PDIA4 (0.84), HSPA5 (0.82), CLTC (0.81); STRING partners: CANX (0.869), GANAB (0.83), HSPA5 (0.999), PDIA4 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1, huMAP3_07455.1
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 occupies a central position among the ER-quality-control genes and has strong STRING relationships with CANX, GANAB, HSPA5, PDIA4, TXNDC5, and RRBP1. It is induced by hypoxia and participates in ER folding, secretion, stress responses, and protection from apoptosis. It contributes to (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0254) and every supplementary STRING term (4 supplementary STRING terms; within-query FDR 0.0066–0.0349), and appears in three hu.MAP complexes (hu.MAP huMAP3_06775.1) (hu.MAP huMAP3_09327.1) (hu.MAP huMAP3_07455.1).
- **Conclusion**: Established evidence supports HYOU1 as a stress-responsive ER chaperone linking hypoxia, secretion, and cell survival. The hypothesis that it reports a shared hypoxic or high-secretory microenvironment in bone and placenta is biologically coherent but not proven by co-abundance alone.

#### GANAB

- **Related proteins** (co-abundance neighbors): TUFM (0.95), ACO2 (0.95), CANX (0.89), ATP5F1B (0.89), ANXA1 (0.88), CLTC (0.87), CCT8 (0.86), PRDX3 (0.83), PDIA4 (0.83), PRDX4 (0.83), ANXA5 (0.83); STRING partners: CANX (0.953), HSPA5 (0.846), HYOU1 (0.83), PDIA4 (0.717)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: glucosidase II alpha subunit. This gene encodes the alpha subunit of glucosidase II and a member of the glycosyl hydrolase 31 family of proteins. The heterodimeric enzyme glucosidase II plays a role in protein folding and quality control by cleaving glucose residues from immature glycoproteins in the endoplasmic reticulum. Expression of the encoded protein is elevated in lung tumor tissue and in response to UV irradiation. Mut…
- **Diseases (Open Targets)**: polycystic kidney disease 3 with or without polycystic liver disease (0.792); autosomal dominant polycystic liver disease (0.515); autosomal dominant polycystic kidney disease (0.470); Biliary tract abnormality (0.438); COVID-19 (0.370)
- **Europe PMC papers**: 1240
- **Why important**: GANAB has the highest weighted network prominence in the supplied ranking and connects the ER core with the mitochondrial and trafficking-associated portion of the module. It encodes the alpha subunit of glucosidase II, which removes glucose residues during ER glycoprotein folding and quality control. It contributes to (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0254) and (STRING Keyword Endoplasmic reticulum; within-query FDR = 0.01) (STRING NetworkNeighborAL Mixed, incl. Photodynamic therapy-induced unfolded protein response, and Protein disulfide isomerase activity; within-query FDR = 0.0257) (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0349), and is present with PDIA4 and HYOU1 in hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Its disease association with autosomal-dominant polycystic kidney and liver disease provides clinically established relevance.
- **Conclusion**: Established evidence supports GANAB as a central glycan-processing enzyme that helps connect glycoprotein maturation with the broader ER-quality-control machinery. Its high network prominence supports an organizing role, but the module does not establish that GANAB drives the cross-tissue co-abundance pattern.

#### TXNDC5

- **Related proteins** (co-abundance neighbors): HYOU1 (0.91), CANX (0.85), RRBP1 (0.82), HSPA5 (0.80); STRING partners: HSPA5 (0.798), PRDX4 (0.994)
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Endoplasmic reticulum; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin domain containing 5. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal endoplasmic reticulum (ER)-signal sequence, three catalytically active thioredoxin domains and a C-terminal ER-retention sequence. Its expression is induced by hypoxia and its role ma…
- **Diseases (Open Targets)**: colorectal carcinoma (0.321); spinal stenosis (0.203); neoplasm (0.096); central nervous system cancer (0.092); glioma (0.091)
- **Europe PMC papers**: 1026
- **Why important**: TXNDC5 is an ER thioredoxin-family protein involved in disulfide-bond formation, protein folding, and protection from hypoxia-associated apoptosis. It connects to HYOU1, CANX, RRBP1, and HSPA5, has a particularly strong relationship with PRDX4, and contributes to (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0254) and (4 supplementary STRING terms; within-query FDR 0.0066–0.0349). HPA links it to plasma-cell and selected immune-cell populations, making it useful for distinguishing a secretory-cell explanation from a purely tissue-intrinsic one.
- **Conclusion**: Established evidence supports TXNDC5 as an ER redox and folding component that complements PDIA4 and PRDX4. Its cell-type pattern makes shared secretory or immune-cell composition a credible explanation for part of the module, but does not prove that this is the sole source of the signal.

## Module 3

**Tissue pair**: bone and placenta  
**Genes (22)**: AHNAK, CAPN2, CNN2, COL1A1, CSRP1, DYNC1I2, DPP3, DPYSL3, FN1, FLNA, FLNB, FLNC, GBE1, EIF6, PKM, MAP1B, MVP, PEPD, PLS3, TKT, TXNRD1, WDR1

### Function

The module is most consistent with a structural cell-architecture and cytoskeletal remodeling program, with linked extracellular-matrix adhesion and cellular energy-support functions. The strongest network-centered pattern connects DPYSL3, MAP1B, PLS3, FLNA, FLNC, WDR1 and CAPN2, implicating coordinated actin organization, actin-filament turnover, membrane anchoring, microtubule organization and cell-shape regulation. FN1 and COL1A1 provide an extracellular-matrix and connective-tissue component, while TKT, PKM and GBE1 provide glycolytic, pentose-phosphate and glycogen-related metabolic support. PEPD adds proline-containing peptide recycling and is relevant to collagen production. No GO/KEGG term passed global correction; therefore, the functional interpretation is gene- and network-based rather than enrichment-confirmed. The absence of a globally significant term does not invalidate the module.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: only FN1 and COL1A1 are identified as secreted or extracellular-matrix proteins. It is also not strongly blood-cell enriched. Most genes have low immune-cell specificity or are not detected in immune cells, although PLS3 and TKT show blood-cell group enrichment and several genes are associated with megakaryocytes, monocytes, neutrophils or related cell types. HPA instead points toward vascular, smooth-muscle, epithelial, stromal, trophoblast and skeletal-muscle contexts, with many genes classified as cell-type enhanced. Placental protein detection is broad across the module, whereas the fact sheet provides no matching HPA bone protein result. Thus, the shared signal may reflect conserved stromal, vascular, trophoblast, contractile or cytoskeletal cell populations in the two tissues, rather than a blood-contamination signature. FN1 and COL1A1 could also contribute an extracellular-matrix component.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited set of specific, already known relationships rather than a globally enriched interaction network. Established interactions include COL1A1 with FN1; FLNA with FLNB, FLNC, FN1 and WDR1; FLNB with FLNC; and PKM with TKT. These links reinforce extracellular-matrix adhesion, filamin-based actin organization and metabolic coupling. Most module pairs do not have high-confidence STRING support, so co-abundance should not be interpreted as direct physical interaction for the whole module. hu.MAP provides partial complex-level support: (hu.MAP huMAP3_05674.1) places FLNB and AHNAK in a membrane-associated complex; (hu.MAP huMAP3_09165.1) places WDR1 and AHNAK in a larger signaling and cytoskeletal complex; and (hu.MAP huMAP3_14442.1) places PLS3 and PKM in a broad complex containing cytoskeletal, metabolic and regulatory proteins. In each case only a small subset of the relevant complex is represented in the module, so these observations support shared cellular context or partial complex membership rather than reconstruction of complete complexes. STRING has no supplementary enrichment terms, and the fact sheet provides no globally significant STRING enrichment.

**STRING interactions (score >= 0.7)**: 7 of 231 gene pairs: COL1A1–FN1 (0.974); FLNA–FLNB (0.979); FLNA–FLNC (0.907); FLNA–FN1 (0.809); FLNA–WDR1 (0.874); FLNB–FLNC (0.921); PKM–TKT (0.951)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05674.1 (FLNB, AHNAK; 2/12); huMAP3_09165.1 (WDR1, AHNAK; 2/39); huMAP3_14442.1 (PLS3, PKM; 2/57)

### Novelty

The module should not be declared a wholly new molecular pathway. Several of its relationships are established in STRING, and partial complex membership is represented in hu.MAP through (hu.MAP huMAP3_05674.1), (hu.MAP huMAP3_09165.1) and (hu.MAP huMAP3_14442.1). Its potentially novel aspect is the cross-tissue co-abundance pattern linking extracellular matrix, filamin-actin architecture, microtubule-associated proteins, proteolysis and intermediary metabolism across bone and placenta. That claim remains provisional because absence of a complete representation in STRING or hu.MAP does not prove novelty, and the module has no globally significant GO/KEGG or STRING enrichment. A genuine new finding would require independent replication, comparison with existing tissue co-expression modules, cell-composition adjustment and experimental validation of the proposed cross-tissue mechanism.

**Hypothesis.** Hypothesis: the conserved bone-placenta module reflects a shared stromal or vascular-cell state in which extracellular-matrix production and adhesion are mechanically coupled to cytoskeletal remodeling and metabolic adaptation. FN1 and COL1A1 may organize the extracellular scaffold; FLNA, FLNB, FLNC and PLS3 may connect that scaffold to actin; WDR1 and CAPN2 may regulate actin turnover; DPYSL3 and MAP1B may coordinate actin–microtubule architecture; and TKT, PKM, GBE1 and TXNRD1 may support biosynthetic, energetic and redox demands. In placenta this could relate to trophoblast or vascular remodeling, while in bone it could relate to matrix-producing or mechanically responsive stromal cells. This is a mechanistic model, not an established causal conclusion from the co-abundance data.

### Important genes

#### FN1

- **Related proteins** (co-abundance neighbors): COL1A1 (0.83), PLS3 (0.82); STRING partners: COL1A1 (0.974), FLNA (0.809)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 is a network bridge between COL1A1 and PLS3 and has established STRING relationships with COL1A1 and FLNA. It is a secreted and cell-surface extracellular-matrix glycoprotein involved in adhesion, migration, cell-substrate junctions and integrin signaling. HPA places it in blood vessels and placenta and in extravillous trophoblasts, fibroblasts and related stromal contexts. It also has exceptionally extensive literature and broad disease relevance.
- **Conclusion**: Established evidence supports FN1 as the principal extracellular-matrix and adhesion anchor of the module. It is a strong candidate for explaining conservation between bone and placenta. It is not established that FN1 drives the entire co-abundance module; that causal role is a hypothesis.

#### COL1A1

- **Related proteins** (co-abundance neighbors): FN1 (0.83); STRING partners: FN1 (0.974)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type I alpha 1 chain. This gene encodes the pro-alpha1 chains of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIA, Ehlers-Danlos syndrome Classical type,…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 2 (0.847); osteogenesis imperfecta type 4 (0.837); osteogenesis imperfecta type 3 (0.835); osteogenesis imperfecta type 1 (0.834); osteogenesis imperfecta (0.808)
- **Europe PMC papers**: 45548
- **Why important**: COL1A1 is directly connected to FN1 and is the major fibrillar collagen component represented in the module. It is abundant in connective tissues and is especially relevant to bone matrix, ossification and osteoblast differentiation. HPA associates it with stromal and fibroblast-like cells and detects it in placenta. Its extensive literature and strong links to osteogenesis imperfecta and skeletal disease make it biologically important even though its network connectivity is limited.
- **Conclusion**: Established evidence supports COL1A1 as the bone- and connective-tissue matrix component and as a plausible contributor to the shared extracellular scaffold. The data do not establish that collagen production is globally enriched in the module, because no GO/KEGG term passed global correction.

#### FLNA

- **Related proteins** (co-abundance neighbors): DPYSL3 (0.90), FLNC (0.87), FLNB (0.83); STRING partners: FLNB (0.979), FLNC (0.907), FN1 (0.809), WDR1 (0.874)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA connects several module components and has high-confidence STRING relationships with FLNB, FLNC, FN1 and WDR1. Its established function is to crosslink actin and connect the cytoskeleton to membrane proteins, integrins and receptor complexes. HPA supports vascular, intestinal, stromal, epithelial and megakaryocyte-associated contexts, including placenta. It has extensive literature and strong developmental and skeletal disease associations.
- **Conclusion**: Established evidence supports FLNA as a central cytoskeletal–membrane organizer that can link extracellular-matrix adhesion to intracellular architecture. Its role as the organizing hub of this particular bone–placenta module remains a hypothesis inferred from co-abundance and network placement.

#### PLS3

- **Related proteins** (co-abundance neighbors): PEPD (0.91), WDR1 (0.89), TXNRD1 (0.84), DPYSL3 (0.82), FN1 (0.82), DPP3 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: plastin 3. Plastins are a family of actin-binding proteins that are conserved throughout eukaryote evolution and expressed in most tissues of higher eukaryotes. In humans, two ubiquitous plastin isoforms (L and T) have been identified. Plastin 1 (otherwise known as Fimbrin) is a third distinct plastin isoform which is specifically expressed at high levels in the small intestine. The L isoform is expressed on…
- **Diseases (Open Targets)**: X-linked osteoporosis with fractures (0.727); congenital diaphragmatic hernia (0.553); osteoporosis (0.477); hernia, anterior diaphragmatic (0.380); postmenopausal osteoporosis (0.341)
- **Europe PMC papers**: 1365
- **Why important**: PLS3 is a highly connected actin-bundling protein in the module and links DPYSL3, WDR1, FN1, PEPD, TXNRD1 and DPP3. It is associated with actin-bundle assembly, bone development and presynaptic actin organization. HPA places it in blood vessels, placenta, epithelial populations and selected immune-cell groups. Its disease associations include X-linked osteoporosis and other skeletal disorders, making it especially relevant to the bone component.
- **Conclusion**: Established evidence supports PLS3 as an actin-architecture and skeletal-disease gene that may connect cell mechanics with matrix interactions. The module does not establish whether PLS3 is the tissue-specific driver or merely a marker of the shared cytoskeletal cell state.

#### WDR1

- **Related proteins** (co-abundance neighbors): PLS3 (0.89), CAPN2 (0.87), TXNRD1 (0.85), DPYSL3 (0.83); STRING partners: FLNA (0.874)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_09165.1
- **Function (MyGene.info)**: WD repeat domain 1. This gene encodes a protein containing 9 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, mostly including a trp-asp at the C-terminal end. WD domains are involved in protein-protein interactions. The encoded protein may help induce the disassembly of actin filaments. Two transcript variants encoding different isoforms have been found for…
- **Diseases (Open Targets)**: periodic fever, immunodeficiency, and thrombocytopenia syndrome (0.705); gout (0.528); neurodegenerative disease (0.526); atrial fibrillation (0.519); intellectual developmental disorder 61 (0.416)
- **Europe PMC papers**: 1861
- **Why important**: WDR1 is connected to PLS3, CAPN2, TXNRD1 and DPYSL3 and has a high-confidence STRING relationship with FLNA. Its known function includes actin-filament disassembly and regulation of cortical cytoskeleton organization, with additional links to platelet formation and immune processes. It is represented with AHNAK in hu.MAP complex (hu.MAP huMAP3_09165.1) and with placenta protein detection in HPA.
- **Conclusion**: Established evidence supports WDR1 as a regulator of actin turnover and a plausible link between cytoskeletal remodeling and cell-junction or platelet-associated biology. Its participation in a coordinated bone–placenta remodeling program is a hypothesis, not a demonstrated mechanism.

#### MAP1B

- **Related proteins** (co-abundance neighbors): DPYSL3 (0.94), FLNC (0.89), PKM (0.87), MVP (0.85), CNN2 (0.81), DYNC1I2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: microtubule associated protein 1B. This gene encodes a protein that belongs to the microtubule-associated protein family. The proteins of this family are thought to be involved in microtubule assembly, which is an essential step in neurogenesis. The product of this gene is a precursor polypeptide that presumably undergoes proteolytic processing to generate the final MAP1B heavy chain and LC1 light chain. Gene knockout studies of th…
- **Diseases (Open Targets)**: periventricular nodular heterotopia 9 (0.762); hearing loss, autosomal dominant 83 (0.547); neurodegenerative disease (0.538); periventricular nodular heterotopia (0.522); hereditary disease (0.496)
- **Europe PMC papers**: 3710
- **Why important**: MAP1B is among the more connected module genes and links DPYSL3, FLNC, PKM, MVP, CNN2 and DYNC1I2. Its established functions involve microtubule organization, microtubule bundle formation, neuronal development and intracellular transport. HPA associates it with blood vessels, brain, retina, pericytes and placenta, while its disease literature is extensive.
- **Conclusion**: Established evidence supports MAP1B as the module's microtubule and transport component, complementing its actin-associated genes. Its presence may indicate a broader cytoskeletal trafficking state rather than neuronal biology in bone or placenta; that interpretation remains a hypothesis requiring cell-resolved validation.

## Module 4

**Tissue pair**: bone and placenta  
**Genes (7)**: FASN, IMPDH2, IQGAP1, SEPTIN11, SEPTIN2, SEPTIN9, TLN1

### Function

The module most plausibly represents a cytoskeletal and cell-adhesion program coupled to septin filament biology, with additional links to nucleotide production and lipid synthesis. The strongest internal structure is a septin submodule formed by SEPTIN2, SEPTIN9, and SEPTIN11, supported by very strong STRING relationships and the hu.MAP complex (hu.MAP huMAP3_02362.1). TLN1 and IQGAP1 connect this septin component to adhesion, actin organization, cell junctions, and cell motility. IMPDH2 and FASN suggest that the co-abundance pattern may also track biosynthetic and metabolic state. No GO or KEGG term passed global correction; therefore, the functional interpretation is based on the gene annotations, network topology, STRING supplementary terms (STRING Pfam 50S ribosome-binding GTPase; within-query FDR = 0.013) and (STRING InterPro P-loop containing nucleoside triphosphate hydrolase; within-query FDR = 0.0461), and complex evidence rather than on a globally significant enrichment term.

**Cell composition.** This is not a secreted-protein module, and the HPA evidence does not indicate a plasma-protein composition. Most genes have low tissue specificity and low immune-cell specificity, while several show cell-type-associated patterns. Platelet and megakaryocyte associations occur for TLN1, and platelet association also occurs for SEPTIN11; SEPTIN11 is additionally associated with extravillous trophoblasts. FASN is enhanced in adipose tissue, breast, and liver and is enriched in breast lactating cells, whereas IMPDH2 and IQGAP1 have more restricted cell-type annotations. Protein detection is available for most genes in placenta, but the bone comparison lacks matching HPA tissue data. Thus, the shared signal could reflect a conserved cellular program in bone and placenta, but contribution from shared cell types, particularly vascular, trophoblast, platelet, or megakaryocyte-related components, should be considered. The available evidence does not support simply labeling the module as a blood cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a compact and internally coherent septin interaction unit: SEPTIN2, SEPTIN9, and SEPTIN11 are strongly connected to one another and are jointly represented in hu.MAP complex (hu.MAP huMAP3_02362.1), which contains additional septin family members outside this module. STRING also supports the TLN1-IQGAP1 relationship. The supplementary STRING annotations connect the septin genes to a ribosome-binding GTPase family domain (STRING Pfam 50S ribosome-binding GTPase; within-query FDR = 0.013) and connect IQGAP1 with the septin genes through a broader P-loop-containing nucleoside-triphosphate-hydrolase annotation (STRING InterPro P-loop containing nucleoside triphosphate hydrolase; within-query FDR = 0.0461). These STRING terms are supplementary and are not global enrichment results. IMPDH2 and FASN are connected to the central TLN1-IQGAP1 metabolic-adhesion neighborhood in the co-abundance network, but their listed relationships are not independently supported by high-confidence STRING partners. Overall, the network combines a known septin complex with a smaller adhesion-associated neighborhood and should not be interpreted as a single experimentally established complex containing all module genes.

**STRING interactions (score >= 0.7)**: 4 of 21 gene pairs: IQGAP1–TLN1 (0.893); SEPTIN11–SEPTIN2 (0.999); SEPTIN11–SEPTIN9 (0.996); SEPTIN2–SEPTIN9 (0.997)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam 50S ribosome-binding GTPase (FDR = 0.013, 3 genes); InterPro P-loop containing nucleoside triphosphate hydrolase (FDR = 0.0461, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02362.1 (SEPTIN2, SEPTIN11, SEPTIN9; 3/14)

### Novelty

The septin component is not novel as a molecular interaction: its members are represented in STRING and in the hu.MAP septin complex (hu.MAP huMAP3_02362.1), and the TLN1-IQGAP1 relationship is also already supported by STRING. The potentially new observation is the conserved co-abundance of this mixed septin, adhesion, nucleotide-biosynthetic, and lipid-biosynthetic set across bone and placenta. That claim cannot be established as a new biological mechanism from this fact sheet alone, because absence of a relationship from STRING or hu.MAP does not prove novelty and the module has no globally significant GO or KEGG enrichment. The finding is therefore best described as a potentially novel tissue-pair co-abundance pattern built partly from known molecular machinery, requiring replication and comparison with existing tissue-specific co-expression studies.

**Hypothesis.** Hypothesis: in shared bone and placental cellular populations, a septin filament scaffold involving SEPTIN2, SEPTIN9, and SEPTIN11 may coordinate with TLN1- and IQGAP1-dependent adhesion and actin organization. This cytoskeletal state could be coupled to the biosynthetic demands represented by IMPDH2 and FASN, supporting cell shape, junctional remodeling, migration, or vesicle-associated processes. The platelet, megakaryocyte, vascular, and trophoblast annotations raise the possibility that the pattern is partly driven by related adherent or vascular-associated cell populations rather than by a universal program of every bone and placental cell. This is a mechanistic hypothesis, not an established causal pathway; it should be tested by cell-resolved data, perturbation of the septin or adhesion components, and replication in independent bone and placenta cohorts.

### Important genes

#### SEPTIN9

- **Related proteins** (co-abundance neighbors): SEPTIN2 (0.91), SEPTIN11 (0.88), TLN1 (0.85), IQGAP1 (0.83); STRING partners: SEPTIN11 (0.996), SEPTIN2 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_02362.1
- **Function (MyGene.info)**: septin 9. This gene is a member of the septin family involved in cytokinesis and cell cycle control. This gene is a candidate for the ovarian tumor suppressor gene. Mutations in this gene cause hereditary neuralgic amyotrophy, also known as neuritis with brachial predilection. A chromosomal translocation involving this gene on chromosome 17 and the MLL gene on chromosome 11 results in acute myelomonocytic l…
- **Diseases (Open Targets)**: neuralgic amyotrophy (0.564); hypertensive disorder (0.496); cataract (0.437); essential hypertension (0.426); alcohol drinking (0.420)
- **Europe PMC papers**: 748
- **Why important**: SEPTIN9 is a central connector in the module, linking SEPTIN2 and SEPTIN11 to TLN1 and IQGAP1. It is part of the known septin complex (hu.MAP huMAP3_02362.1) and appears in both supplementary STRING annotations (STRING Pfam 50S ribosome-binding GTPase; within-query FDR = 0.013) and (STRING InterPro P-loop containing nucleoside triphosphate hydrolase; within-query FDR = 0.0461). Its annotations support cytoskeleton organization, intracellular localization, and cytokinesis. It also has substantial literature and disease associations including neuralgic amyotrophy and hematologic malignancy-related biology, making it a strong candidate for interpreting the septin-centered component.
- **Conclusion**: Established evidence supports SEPTIN9 as a structural and network-level bridge within the septin module. Its role as the specific driver of the bone-placenta co-abundance pattern remains a hypothesis.

#### TLN1

- **Related proteins** (co-abundance neighbors): FASN (0.92), IMPDH2 (0.90), SEPTIN9 (0.85), IQGAP1 (0.84); STRING partners: IQGAP1 (0.893)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 has the strongest connective role in the module, linking FASN, IMPDH2, SEPTIN9, and IQGAP1. Its annotations directly support integrin activation, cell adhesion, actin organization, cell junction assembly, and migration. It is detected in placenta, associated with vascular tissue and megakaryocyte or platelet cell types, and its relationship with IQGAP1 is supported by STRING. Its extensive literature and disease associations make it an important candidate for connecting the module to tissue architecture.
- **Conclusion**: Established evidence supports TLN1 as an adhesion and cytoskeletal hub that can connect the septin and metabolic neighborhoods. Whether TLN1 mediates the shared tissue-specific program is not demonstrated.

#### IQGAP1

- **Related proteins** (co-abundance neighbors): IMPDH2 (0.86), TLN1 (0.84), SEPTIN9 (0.83); STRING partners: TLN1 (0.893)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IQ motif containing GTPase activating protein 1. This gene encodes a member of the IQGAP family. The protein contains four IQ domains, one calponin homology domain, one Ras-GAP domain and one WW domain. It interacts with components of the cytoskeleton, with cell adhesion molecules, and with several signaling molecules to regulate cell morphology and motility. Expression of the protein is upregulated by gene amplification in two gastric cancer ce…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.515); Costello syndrome (0.503); allergic rhinitis (0.474)
- **Europe PMC papers**: 3787
- **Why important**: IQGAP1 links TLN1 and SEPTIN9 with IMPDH2 and is located at the plasma membrane and cell junctions. Its annotations include cytoskeletal regulation, signal transduction, receptor-linked signaling, mitotic-cycle regulation, and fibroblast migration. It is supported by the TLN1 STRING relationship and by the broader supplementary STRING term (STRING InterPro P-loop containing nucleoside triphosphate hydrolase; within-query FDR = 0.0461). IQGAP1 also has the largest literature volume among the module genes, strengthening its value as a biologically interpretable network connector.
- **Conclusion**: Established evidence supports IQGAP1 as a plausible interface between adhesion, signaling, and the septin cytoskeleton. Its proposed coordinating role in this module remains untested.

#### SEPTIN11

- **Related proteins** (co-abundance neighbors): SEPTIN9 (0.88), SEPTIN2 (0.85); STRING partners: SEPTIN2 (0.999), SEPTIN9 (0.996)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_02362.1
- **Function (MyGene.info)**: septin 11. SEPT11 belongs to the conserved septin family of filament-forming cytoskeletal GTPases that are involved in a variety of cellular functions including cytokinesis and vesicle trafficking (Hanai et al., 2004 [PubMed 15196925]; Nagata et al., 2004 [PubMed 15485874]).[supplied by OMIM, Jul 2009].
- **Diseases (Open Targets)**: autosomal recessive cerebellar ataxia (0.119); corneal edema (0.093); neoplasm (0.077); hepatocellular carcinoma (0.076); glomerulonephritis (0.050)
- **Europe PMC papers**: 113
- **Why important**: SEPTIN11 forms a tightly supported septin unit with SEPTIN2 and SEPTIN9 in STRING and hu.MAP (hu.MAP huMAP3_02362.1), and it contributes to both supplementary STRING annotations (STRING Pfam 50S ribosome-binding GTPase; within-query FDR = 0.013) and (STRING InterPro P-loop containing nucleoside triphosphate hydrolase; within-query FDR = 0.0461). Its known functions include septin filament biology, vesicle trafficking, intracellular localization, and cytokinesis. HPA associates it with extravillous trophoblasts, platelets, hepatic stellate cells, and podocytes, which is especially relevant to a bone-placenta module and to the possibility of shared specialized cell populations.
- **Conclusion**: Established evidence supports SEPTIN11 as a member of a known septin structural unit with potentially relevant placental and platelet-associated expression. Its tissue-pair-specific function is a hypothesis.

#### FASN

- **Related proteins** (co-abundance neighbors): TLN1 (0.92), IMPDH2 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fatty acid synthase. The enzyme encoded by this gene is a multifunctional protein. Its main function is to catalyze the synthesis of palmitate from acetyl-CoA and malonyl-CoA, in the presence of NADPH, into long-chain saturated fatty acids. In some cancer cell lines, this protein has been found to be fused with estrogen receptor-alpha (ER-alpha), in which the N-terminus of FAS is fused in-frame with the C-terminus of …
- **Diseases (Open Targets)**: dengue disease (0.469); autism spectrum disorder (0.333); Parkinson disease (0.295); Epileptic encephalopathy (0.211); neurodegenerative disease (0.205)
- **Europe PMC papers**: 21528
- **Why important**: FASN occupies a peripheral but informative position, connecting TLN1 and IMPDH2. It is the module's clearest lipid-biosynthetic marker, with annotations for fatty-acid and lipid biosynthesis, nutrient response, and osteoblast differentiation. Its tissue-enhanced pattern in adipose tissue, breast, and liver and its association with breast lactating cells indicate strong metabolic and cell-state specificity. It has a very large literature base and broad disease relevance, although it lacks a listed high-confidence STRING partner within this module.
- **Conclusion**: Established evidence supports FASN as a metabolic-state marker connected to the module's structural neighborhood. A direct role for FASN in septin or adhesion organization is not established by the supplied evidence.

#### IMPDH2

- **Related proteins** (co-abundance neighbors): TLN1 (0.90), FASN (0.86), IQGAP1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inosine monophosphate dehydrogenase 2. This gene encodes the rate-limiting enzyme in the de novo guanine nucleotide biosynthesis. It is thus involved in maintaining cellular guanine deoxy- and ribonucleotide pools needed for DNA and RNA synthesis. The encoded protein catalyzes the NAD-dependent oxidation of inosine-5'-monophosphate into xanthine-5'-monophosphate, which is then converted into guanosine-5'-monophosphate. This gene is up-…
- **Diseases (Open Targets)**: acute lymphoblastic leukemia (0.529); Crohn disease (0.447); acute myeloid leukemia (0.421); lupus nephritis (0.408); myelodysplastic syndrome (0.403)
- **Europe PMC papers**: 1438
- **Why important**: IMPDH2 connects TLN1, FASN, and IQGAP1 and represents nucleotide supply within the module. Its established function is rate-limiting guanine nucleotide biosynthesis, supporting DNA and RNA synthesis. It has broad cell-type associations, is detected in placenta, and has substantial literature and disease associations, including hematologic and inflammatory conditions. Unlike the septin genes, it has no listed STRING partner or hu.MAP complex assignment here, so its importance derives mainly from network placement and biochemical complementarity.
- **Conclusion**: Established evidence supports IMPDH2 as a biosynthetic-state component that may accompany cytoskeletal remodeling or proliferative activity. Its direct mechanistic connection to the septin-adhesion unit remains a hypothesis.
