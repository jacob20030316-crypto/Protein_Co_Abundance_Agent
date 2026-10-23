# Conserved co-abundance modules: bone_marrow and placenta

## Module 0

**Tissue pair**: bone_marrow and placenta  
**Genes (5)**: PGD, SARS1, TARS1, CCT5, CCT3

### Function

The module is most consistently interpreted as a cytosolic protein-maintenance and translation-support module. The sole globally corrected GO/KEGG result, (GO:MF adenyl nucleotide binding; q_global = 0.0258), is adenyl nucleotide binding and includes every module gene, supporting a shared relationship with nucleotide-dependent cellular activities. The gene annotations refine this interpretation: CCT3 and CCT5 encode subunits of the ATP-dependent CCT/TRiC chaperonin involved in protein folding, TARS1 and SARS1 support tRNA charging and translation, and PGD supports the oxidative pentose-phosphate pathway and NADPH regeneration. Thus, the strongest interpretation is coordinated expression of core protein folding, translation, and redox-support machinery rather than a tissue-specific secreted signaling pathway. No STRING functional-enrichment term was reported, so no additional pathway claim is supported by STRING enrichment.

**Cell composition.** All module proteins are cytosolic rather than secreted, and all are detected by HPA in both bone marrow and placenta. Most genes have low tissue specificity and low immune-cell specificity, which is more consistent with broadly expressed cellular machinery than with a plasma-protein or narrowly restricted blood-cell module. PGD is the main compositional exception: HPA classifies it as group-enriched in bone marrow and enhanced in neutrophil progenitors and neutrophils, with enrichment also reported across several blood-cell categories. CCT5 has a cell-type enhancement unrelated to the shared bone-marrow/placenta interpretation. Therefore, the module may partly reflect abundant housekeeping machinery in cells present in both tissues, with a possible contribution from myeloid or erythroid-related cellular composition through PGD, but the evidence does not support calling it a blood-secreted module.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF adenyl nucleotide binding | 0.0258 | CCT3, CCT5, PGD, SARS1, TARS1 |

### STRING and hu.MAP

STRING supports a compact protein-associated core involving CCT3-CCT5 [the high-confidence relationship], CCT5-TARS1 [the supportive relationship], and SARS1-TARS1 [the high-confidence relationship]. PGD has no reported STRING partner within this module. hu.MAP independently places CCT3 and CCT5 together in each reported complex association, while the remaining listed complex members are outside the module. These observations strongly support the CCT3-CCT5 relationship as known chaperonin-complex biology and support a known association between the two aminoacyl-tRNA synthetase genes through STRING. They do not establish that all module genes form one physical complex, nor do they establish a direct molecular interaction between PGD and the other genes. The network therefore appears to combine a known chaperonin pair, a translation-related synthetase connection, and a metabolic gene linked by co-abundance rather than by reported physical interaction.

**STRING interactions (score >= 0.7)**: 3 of 10 gene pairs: CCT3–CCT5 (0.999); CCT5–TARS1 (0.727); SARS1–TARS1 (0.915)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01951.1 (CCT5, CCT3; 2/8); huMAP3_07938.1 (CCT5, CCT3; 2/23); huMAP3_06559.1 (CCT5, CCT3; 2/25); huMAP3_09191.1 (CCT5, CCT3; 2/32); huMAP3_10656.1 (CCT5, CCT3; 2/36); huMAP3_14584.1 (CCT5, CCT3; 2/61)

### Novelty

The module should not be claimed as a newly discovered molecular complex. Several of its relationships are already represented in STRING or hu.MAP, especially the CCT3-CCT5 chaperonin association and the TARS1-SARS1 relationship. At the same time, the exact cross-tissue co-abundance pattern linking the chaperonin genes, aminoacyl-tRNA synthetases, and PGD is not directly established by the supplied interaction resources. This makes the tissue-pair module potentially novel as an expression-level combination, but not demonstrably novel as a biochemical pathway. Absence of PGD from the reported STRING and hu.MAP relationships is compatible with a co-abundance or cellular-composition association and is not evidence by itself for novelty.

**Hypothesis.** Hypothesis: in cells shared between bone marrow and placenta, increased demand for growth, differentiation, or stress adaptation may coordinately increase cytosolic protein folding, translation capacity, and oxidative pentose-phosphate support. CCT3 and CCT5 could help fold newly synthesized proteins, TARS1 and SARS1 could support aminoacyl-tRNA availability and translation, and PGD could provide NADPH and oxidative-stress buffering. A contribution from myeloid cell abundance is also plausible because PGD has bone-marrow and neutrophil-related HPA enrichment. This hypothesis requires validation with cell-resolved expression, protein abundance, perturbation, and tissue-composition analyses; the co-abundance network alone does not establish causality.

### Important genes

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT3 (0.88), TARS1 (0.80); STRING partners: CCT3 (0.999), TARS1 (0.727)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: huMAP3_01951.1, huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is a central bridge in the module, connecting CCT3 with TARS1, and it is the module member most repeatedly represented with CCT3 across the hu.MAP complex annotations (hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). Its chaperonin function directly supports the protein-folding interpretation. It also has substantial literature and disease associations including hereditary sensory and autonomic neuropathy and neurodegenerative disease, making it biologically and clinically informative.
- **Conclusion**: Established evidence supports CCT5 as a CCT/TRiC chaperonin subunit and as a known complex-associated partner of CCT3. It is a strong candidate for the structural core of the module. It remains a hypothesis that CCT5 coordinates the module-wide relationship with translation and PGD in these tissues.

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT5 (0.88); STRING partners: CCT5 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: huMAP3_01951.1, huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is directly connected to CCT5 in STRING and is repeatedly paired with CCT5 in hu.MAP complexes (hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). Its annotated role in ATP-dependent folding of proteins, including actin and tubulin, provides a mechanistic basis for the module's protein-maintenance interpretation. It has substantial literature and disease associations involving neurodevelopmental and neurodegenerative phenotypes.
- **Conclusion**: Established evidence supports CCT3 as part of the CCT/TRiC folding machinery and validates the CCT3-CCT5 portion of the module as known biology. Its role as an organizer linking this chaperonin machinery to the other module genes is a hypothesis rather than an established interaction.

#### TARS1

- **Related proteins** (co-abundance neighbors): PGD (0.88), SARS1 (0.81), CCT5 (0.80); STRING partners: CCT5 (0.727), SARS1 (0.915)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: threonyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Threonyl-tRNA synthetase belongs to the class-II aminoacyl-tRNA synthetase family [provided by RefSeq, Jul 2008]…
- **Diseases (Open Targets)**: trichothiodystrophy 7, nonphotosensitive (0.520); trichothiodystrophy (0.430); actinic keratosis (0.356); dyshidrosis (0.315); placental abruption (0.307)
- **Europe PMC papers**: 147
- **Why important**: TARS1 has the strongest network connectivity in the module and links PGD, SARS1, and CCT5. It is an aminoacyl-tRNA synthetase that supplies threonine-charged tRNA for protein translation and is included in the globally corrected adenyl nucleotide-binding term (GO:MF adenyl nucleotide binding; q_global = 0.0258). Its position makes it a plausible bridge between translation machinery, chaperone demand, and cellular metabolism. It also has disease associations including trichothiodystrophy and placental abruption.
- **Conclusion**: Established evidence supports TARS1 as a translation enzyme and as the network bridge connecting the synthetase, chaperonin, and PGD portions of the module. It is a strong integrative marker of the module. A direct regulatory role for TARS1 in coordinating the other genes is not established and remains hypothetical.

#### PGD

- **Related proteins** (co-abundance neighbors): TARS1 (0.88); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphogluconate dehydrogenase. 6-phosphogluconate dehydrogenase is the second dehydrogenase in the pentose phosphate shunt. Deficiency of this enzyme is generally asymptomatic, and the inheritance of this disorder is autosomal dominant. Hemolysis results from combined deficiency of 6-phosphogluconate dehydrogenase and 6-phosphogluconolactonase suggesting a synergism of the two enzymopathies. Several transcript variants encoding…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); Abnormality of the skeletal system (0.329); autoimmune disorder of central nervous system (0.246); smoking behavior (0.245); essential hypertension (0.199)
- **Europe PMC papers**: 8652
- **Why important**: PGD is the metabolic outlier and the only gene with HPA group enrichment in bone marrow, together with enhancement in neutrophil-related cell types and several blood-cell categories. It catalyzes a step in the oxidative pentose-phosphate pathway and contributes to NADPH regeneration. Its connection to TARS1 and its inclusion in (GO:MF adenyl nucleotide binding; q_global = 0.0258) suggest that metabolic and nucleotide-dependent support may accompany the translation and folding machinery. PGD also has a large literature base and disease associations including skeletal-system abnormalities and neurodegenerative disease.
- **Conclusion**: Established evidence supports PGD as a cytosolic pentose-phosphate enzyme and as a marker potentially sensitive to bone-marrow or myeloid cellular composition. Its inclusion may reflect metabolic support for biosynthesis and redox control, but it may also partly reflect cell-type abundance. Whether PGD functionally drives the shared module is unresolved.

#### SARS1

- **Related proteins** (co-abundance neighbors): TARS1 (0.81); STRING partners: TARS1 (0.915)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: seryl-tRNA synthetase 1. This gene belongs to the class II amino-acyl tRNA family. The encoded enzyme catalyzes the transfer of L-serine to tRNA (Ser) and is related to bacterial and yeast counterparts. Multiple alternatively spliced transcript variants have been described but the biological validity of all variants is unknown. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, ataxia, and seizures (0.670); autosomal recessive non-syndromic intellectual disability (0.370); autosomal recessive primary microcephaly (0.370); arteriovenous malformations of the brain (0.340); hereditary peripheral neuropathy (0.118)
- **Europe PMC papers**: 400
- **Why important**: SARS1 encodes seryl-tRNA synthetase and is directly connected to TARS1 by a high-confidence STRING relationship. It is included in (GO:MF adenyl nucleotide binding; q_global = 0.0258) and has annotations related to cytoplasmic translation, tRNA modification, and selenocysteine incorporation. Its disease associations include neurodevelopmental and microcephaly-related disorders, while its literature volume is lower than that of the chaperonin genes and PGD.
- **Conclusion**: Established evidence supports SARS1 as a translation-related aminoacyl-tRNA synthetase and supports its known association with TARS1. It strengthens the interpretation of a translation-support component within the module. A broader role in coordinating chaperone activity or tissue sharing is a hypothesis.

## Module 1

**Tissue pair**: bone_marrow and placenta  
**Genes (7)**: ACLY, LAP3, CANX, CNDP2, PDLIM1, SEPTIN7, CCT8

### Function

The module does not have a GO or KEGG term that passes global correction, so no pathway-level enrichment can be claimed. Its internal structure nevertheless points to a composite cellular maintenance program. SEPTIN7 is the central network connector, linking cytoskeletal organization through PDLIM1 with protein folding and quality-control components represented by CCT8 and CANX, and with LAP3 and ACLY. The annotations support roles in cytoskeletal organization, chaperone-mediated protein folding, endoplasmic-reticulum quality control, proteolysis, peptide turnover, and cytosolic acetyl-CoA production. These are functional interpretations of the gene set, not globally significant enrichment results.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and every module protein is detected in both bone marrow and placenta. Most genes have low tissue specificity and low immune-cell specificity, which is consistent with broadly expressed cellular machinery rather than a narrowly defined blood lineage. The HPA single-cell annotations span several cell types, including Hofbauer cells, lactating breast cells, enterocytes, oocytes, late spermatids, pancreatic islet cells, and stromal, megakaryocyte, or platelet-associated cells. PDLIM1 is tissue enhanced in skeletal muscle and has group-enriched blood-cell annotations, so cellular composition may contribute to the shared signal. Overall, the module is more consistent with shared cellular processes and cell-type mixtures than with a circulating secreted-protein program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair reaches the supplied STRING interaction threshold, and STRING reports no functional enrichment. Thus the co-abundance edges should not be interpreted as established physical protein interactions. hu.MAP provides one relevant complex association: PDLIM1 and LAP3 occur together in (hu.MAP huMAP3_14442.1), a large complex whose other members are outside this module. This is evidence for a known complex context involving those genes, but it does not establish a direct PDLIM1–LAP3 interaction or explain the entire co-abundance structure. The absence of STRING partners and the limited hu.MAP overlap suggest that much of the module relationship may reflect shared regulation, cellular state, or compartmental composition rather than a single experimentally established complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (PDLIM1, LAP3; 2/57)

### Novelty

This module should not be called a new molecular complex or a newly discovered pathway. The absence of STRING relationships and the limited hu.MAP overlap do not prove novelty, because co-abundance can arise without physical binding and database coverage is incomplete. The potentially novel aspect is the reproducible sharing of this particular combination of broadly expressed folding, cytoskeletal, proteolytic, and metabolic genes between bone marrow and placenta. That claim remains provisional: it would require replication in independent cohorts, control for cell-type composition, and comparison with published cross-tissue co-expression modules.

**Hypothesis.** Hypothesis: the module represents a shared cellular adaptation that coordinates proteostasis, cytoskeletal organization, peptide processing, and acetyl-CoA supply in cells present in both bone marrow and placenta. In this model, CCT8 and CANX support folding and quality control, LAP3 and CNDP2 support cytosolic peptide processing, SEPTIN7 and PDLIM1 organize cytoskeletal architecture, and ACLY supplies metabolic acetyl-CoA. The apparent conservation could reflect a common stress, differentiation, or biosynthetic state, or shared contributions from particular cell types, rather than a dedicated bone-marrow–placenta pathway.

### Important genes

#### SEPTIN7

- **Related proteins** (co-abundance neighbors): CCT8 (0.94), CANX (0.86), LAP3 (0.82), PDLIM1 (0.81), ACLY (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: septin 7. This gene encodes a protein that is highly similar to the CDC10 protein of Saccharomyces cerevisiae. The protein also shares similarity with Diff 6 of Drosophila and with H5 of mouse. Each of these similar proteins, including the yeast CDC10, contains a GTP-binding motif. The yeast CDC10 protein is a structural component of the 10 nm filament which lies inside the cytoplasmic membrane and is essen…
- **Diseases (Open Targets)**: glaucoma (0.366); bone fracture (0.264); fracture of pelvis (0.264); open-angle glaucoma (0.262); male reproductive system disorder (0.260)
- **Europe PMC papers**: 304
- **Why important**: SEPTIN7 has the strongest network connectivity in the module and links the folding, proteolytic, cytoskeletal, and metabolic portions of the subgraph through CCT8, CANX, LAP3, PDLIM1, and ACLY. Its annotation supports cytoskeleton organization, cytokinesis, cell shape, and cilium assembly. It has a substantial literature and disease associations including glioma-related biology, glaucoma, and bone-fracture phenotypes.
- **Conclusion**: Established evidence supports SEPTIN7 as the network hub and a cytoskeletal organizer. It is plausible, but not established, that SEPTIN7 helps couple cytoskeletal state to proteostasis in this module.

#### CCT8

- **Related proteins** (co-abundance neighbors): SEPTIN7 (0.94), LAP3 (0.88), CANX (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is a central connector among SEPTIN7, LAP3, and CANX. Its established function as a subunit of the cytosolic CCT chaperonin directly supports protein folding, stabilization, and assembly as a core interpretation of the module. It is broadly expressed, has a substantial literature, and is associated in Open Targets with several cancer-related phenotypes.
- **Conclusion**: Established evidence supports CCT8 as a proteostasis component that may explain part of the shared module signal. A specific role for CCT8 in coordinating bone-marrow and placental states remains a hypothesis.

#### CANX

- **Related proteins** (co-abundance neighbors): CCT8 (0.87), SEPTIN7 (0.86), LAP3 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is a central module connector and an endoplasmic-reticulum chaperone. Its established functions in calcium binding, folding of newly synthesized glycoproteins, retention of misfolded proteins, and ER quality control provide a strong mechanistic link to cellular proteostasis. CANX also has extensive literature and disease associations involving neurodegenerative and infectious disease biology.
- **Conclusion**: Established evidence supports CANX as an ER quality-control component of the module. Its co-abundance with cytoskeletal and cytosolic machinery may indicate a shared cellular stress or biosynthetic state, but that connection is not experimentally demonstrated here.

#### PDLIM1

- **Related proteins** (co-abundance neighbors): SEPTIN7 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Actin filaments; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: PDZ and LIM domain 1. This gene encodes a member of the enigma protein family. The protein contains two protein interacting domains, a PDZ domain at the amino terminal end and one to three LIM domains at the carboxyl terminal. It is a cytoplasmic protein associated with the cytoskeleton. The protein may function as an adapter to bring other LIM-interacting proteins to the cytoskeleton. Pseudogenes associated with this …
- **Diseases (Open Targets)**: ovarian dysfunction (0.167); atrial fibrillation (0.138); liver disorder (0.126); Peyronie disease (0.117); uterine corpus leiomyoma (0.092)
- **Europe PMC papers**: 1123
- **Why important**: PDLIM1 connects to the network hub SEPTIN7 and is one of the two module members in the hu.MAP association (hu.MAP huMAP3_14442.1) with LAP3. Its PDZ and LIM domains support adapter activity at the actin cytoskeleton, while its annotations include actin organization, cell polarity, migration, hypoxia response, and oxidative-stress response. HPA also gives it the most distinctive tissue and blood-cell pattern in the module.
- **Conclusion**: Established evidence supports PDLIM1 as a cytoskeletal adapter and a possible indicator of cell-type composition. Its role as the interface between cytoskeletal organization and the other module processes is a plausible hypothesis rather than a demonstrated mechanism.

#### LAP3

- **Related proteins** (co-abundance neighbors): CCT8 (0.88), CANX (0.84), CNDP2 (0.83), SEPTIN7 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: leucine aminopeptidase 3. Predicted to enable peptidase activity. Predicted to be involved in proteolysis. Located in cytosol; midbody; and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: upper respiratory tract disorder (0.283); preeclampsia (0.199); multinodular goiter (0.181); Alzheimer disease (0.165); acute myeloid leukemia (0.108)
- **Europe PMC papers**: 1293
- **Why important**: LAP3 is strongly connected to CCT8, CANX, CNDP2, and SEPTIN7 and shares the hu.MAP complex context (hu.MAP huMAP3_14442.1) with PDLIM1. Its established aminopeptidase and proteolysis annotations provide a peptide-processing function complementary to the folding and quality-control genes. It has a substantial literature and an Open Targets association with preeclampsia among other disorders, which is relevant to placental interpretation.
- **Conclusion**: Established evidence supports LAP3 as a cytosolic proteolytic enzyme and as part of a known hu.MAP complex context. Its possible contribution to a shared placental and bone-marrow proteostasis program is suggestive, not proven.

## Module 2

**Tissue pair**: bone_marrow and placenta  
**Genes (8)**: ACO2, ANXA4, COPB1, TUFM, FERMT2, LMNB1, PRDX3, VPS35

### Function

This module does not support a single specialized pathway on enrichment evidence: no GO or KEGG term passed global correction. Its gene composition instead suggests coordinated basic cellular maintenance across mitochondrial metabolism, mitochondrial protein synthesis, oxidative-stress control, endosomal and Golgi trafficking, membrane-associated signaling, and cell adhesion. ACO2, TUFM, and PRDX3 support mitochondrial metabolic and proteostatic functions; VPS35 and COPB1 support intracellular cargo trafficking; ANXA4 supports calcium-dependent membrane processes; and FERMT2 supports integrin-linked adhesion and receptor signaling. The co-abundance pattern is therefore most consistent with a mixed cellular-maintenance program rather than a demonstrated canonical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of the genes is annotated as secreted. Most genes have low tissue specificity, and the module has low immune-cell specificity overall, arguing against a simple blood-cell-specific signature. Nevertheless, many genes show cell-type-enhanced expression, including enterocyte, cholangiocyte, pancreatic duct, trophoblast, progenitor, adipocyte, podocyte, and smooth-muscle patterns. ANXA4 is enhanced in syncytiotrophoblasts and ductal cell types, while LMNB1 is enhanced in bone-marrow and lymphoid tissue and in marrow progenitor populations. All genes are detected at the protein level in placenta and nearly all are detected in bone marrow, with FERMT2 being the notable exception in bone marrow. The shared module may therefore reflect broadly used cellular machinery combined with shared or variable cell-state composition in the two tissues, rather than a blood or secreted-protein program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The module has no STRING interactions at the supplied high-confidence threshold and no hu.MAP complex containing multiple module members. Thus, the co-abundance structure is not corroborated by the queried high-confidence physical-interaction resources. This does not disprove biological coordination: the genes participate in different cellular systems, their regulation may be indirect, and co-abundance can arise from shared cell states, organelle content, stress responses, or tissue composition. The absence of STRING and hu.MAP support means that the network should be interpreted as an expression-level association rather than as a demonstrated physical complex.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a new co-abundance observation, but it cannot be called a new biological pathway or a novel molecular complex from the supplied evidence. Its lack of high-confidence STRING and hu.MAP support makes the particular cross-tissue association less obviously pre-established in those resources, yet database absence alone does not establish novelty. The lack of globally significant GO or KEGG enrichment also prevents assigning a previously recognized pathway label. The most defensible claim is that this is a potentially novel tissue-pair co-abundance pattern involving known cellular functions, requiring replication and targeted validation.

**Hypothesis.** Hypothesis: the shared module reflects a coordinated cellular-maintenance state present in selected bone-marrow and placental cells. Mitochondrial energy production and translation, represented by ACO2, TUFM, and PRDX3, may be coupled to vesicle and cargo handling through VPS35 and COPB1, while ANXA4 and FERMT2 connect this state to membrane remodeling, adhesion, and tissue-specific signaling. In placenta, trophoblast or epithelial-like cellular programs may contribute to this pattern; in bone marrow, progenitor or other non-immune cellular states may contribute. This hypothesis predicts that the module will track mitochondrial activity, trafficking demand, and adhesion or differentiation state, rather than a single lineage-restricted immune function. It should be tested by cell-resolved expression, perturbation of candidate genes, and independent cohorts from both tissues.

### Important genes

#### ACO2

- **Related proteins** (co-abundance neighbors): ANXA4 (0.87), TUFM (0.84), LMNB1 (0.83), VPS35 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aconitase 2. The protein encoded by this gene belongs to the aconitase/IPM isomerase family. It is an enzyme that catalyzes the interconversion of citrate to isocitrate via cis-aconitate in the second step of the TCA cycle. This protein is encoded in the nucleus and functions in the mitochondrion. It was found to be one of the mitochondrial matrix proteins that are preferentially degraded by the serine proteas…
- **Diseases (Open Targets)**: infantile cerebellar-retinal degeneration (0.814); optic atrophy 9 (0.693); autosomal dominant optic atrophy, classic form (0.619); optic atrophy (0.601); mitochondrial disease (0.505)
- **Europe PMC papers**: 3559
- **Why important**: ACO2 is among the most connected genes in the module and links ANXA4, TUFM, LMNB1, and VPS35. It is the mitochondrial aconitase that catalyzes a step in the tricarboxylic acid cycle and is therefore a direct marker of mitochondrial metabolic capacity. It has strong disease associations with optic atrophy and mitochondrial disease and a substantial literature base.
- **Conclusion**: Established evidence supports ACO2 as a central mitochondrial metabolic component of the co-abundance pattern. It is plausible, but not demonstrated, that ACO2 links metabolic state to the trafficking and membrane-associated genes in this module.

#### VPS35

- **Related proteins** (co-abundance neighbors): ANXA4 (0.84), ACO2 (0.82), TUFM (0.81), COPB1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS35 retromer complex component. This gene belongs to a group of vacuolar protein sorting (VPS) genes. The encoded protein is a component of a large multimeric complex, termed the retromer complex, involved in retrograde transport of proteins from endosomes to the trans-Golgi network. The close structural similarity between the yeast and human proteins that make up this complex suggests a similarity in function. Expression studie…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.743); neurodegenerative disease (0.553); young-onset Parkinson disease (0.503); Parkinson disease (0.482); Parkinson disease, dominant (0.370)
- **Europe PMC papers**: 3611
- **Why important**: VPS35 is one of the most connected genes and links ANXA4, ACO2, TUFM, and COPB1. It is a core retromer component involved in endosome-to-Golgi retrograde transport, protein transport, lysosome organization, and regulation of mitochondrial organization. It has well-established associations with Parkinson disease and related neurodegenerative conditions and a substantial literature base.
- **Conclusion**: Established evidence supports VPS35 as a central intracellular-trafficking and organelle-maintenance gene. Its placement between mitochondrial and vesicle-related genes supports a possible coordinating role, but the module does not establish direct physical or regulatory coupling.

#### TUFM

- **Related proteins** (co-abundance neighbors): PRDX3 (0.86), ACO2 (0.84), VPS35 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Tu translation elongation factor, mitochondrial. This gene encodes a protein which participates in protein translation in mitochondria. Mutations in this gene have been associated with combined oxidative phosphorylation deficiency resulting in lactic acidosis and fatal encephalopathy. A pseudogene has been identified on chromosome 17. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 4 (0.769); neurodegenerative disease (0.502); COVID-19 (0.471); combined oxidative phosphorylation deficiency (0.370); ulcerative colitis (0.303)
- **Europe PMC papers**: 1391
- **Why important**: TUFM is centrally connected to PRDX3, ACO2, and VPS35. It is required for mitochondrial translation and mitochondrial large-ribosomal-subunit assembly, making it a strong indicator of mitochondrial protein-production demand. Its disease associations include combined oxidative-phosphorylation deficiency and related mitochondrial disease, with a substantial literature base.
- **Conclusion**: Established evidence supports TUFM as a mitochondrial translation component and as a biologically meaningful bridge between mitochondrial genes in the module. Its connection to VPS35 is an expression-network observation; a direct trafficking mechanism remains hypothetical.

#### PRDX3

- **Related proteins** (co-abundance neighbors): TUFM (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Mitochondria; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peroxiredoxin 3. This gene encodes a mitochondrial protein with antioxidant function. The protein is similar to the C22 subunit of Salmonella typhimurium alkylhydroperoxide reductase, and it can rescue bacterial resistance to alkylhydroperoxide in E. coli that lack the C22 subunit. The human and mouse genes are highly conserved, and they map to the regions syntenic between mouse and human chromosomes. Sequence com…
- **Diseases (Open Targets)**: spinocerebellar ataxia, autosomal recessive 32 (0.653); corneal dystrophy, punctiform and polychromatic pre-descemet (0.571); autosomal recessive cerebellar ataxia (0.268); neurodegenerative disease (0.257); hereditary disease (0.191)
- **Europe PMC papers**: 2613
- **Why important**: PRDX3 connects to TUFM and provides the module with a mitochondrial antioxidant component. It participates in responses to oxidative stress, mitochondrial organization, myeloid-cell differentiation, and responses to lipopolysaccharide. It has disease associations involving spinocerebellar and cerebellar ataxia and a substantial literature base.
- **Conclusion**: Established evidence supports PRDX3 as an oxidative-stress safeguard within the mitochondrial portion of the module. It may indicate that mitochondrial translation and energy metabolism are coordinated with redox control, but the shared-tissue mechanism is not established.

#### ANXA4

- **Related proteins** (co-abundance neighbors): ACO2 (0.87), VPS35 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A4. Annexin IV (ANX4) belongs to the annexin family of calcium-dependent phospholipid binding proteins. Although their functions are still not clearly defined, several members of the annexin family have been implicated in membrane-related events along exocytotic and endocytotic pathways. ANX4 has 45 to 59% identity with other members of its family and shares a similar size and exon-intron organization…
- **Diseases (Open Targets)**: atrial fibrillation (0.445); Abnormality of the skeletal system (0.385); dentures (0.301); neurodegenerative disease (0.268); placental abruption (0.235)
- **Europe PMC papers**: 1395
- **Why important**: ANXA4 connects the central ACO2 and VPS35 portion of the network and is a calcium-dependent phospholipid-binding protein involved in membrane-related processes. Its annotations include epithelial differentiation and modulation of inflammatory signaling, and its cell-type pattern includes cholangiocytes, pancreatic duct cells, and syncytiotrophoblasts. It also has a reported association with placental abruption and a substantial literature base.
- **Conclusion**: Established evidence supports ANXA4 as a membrane and epithelial or trophoblast-associated component that may connect cellular trafficking to tissue-interface biology. Its apparent bridge to mitochondrial genes is a co-abundance relationship and should not be interpreted as a proven molecular interaction.

#### FERMT2

- **Related proteins** (co-abundance neighbors): COPB1 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Focal adhesion sites; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FERM domain containing kindlin 2. Enables several functions, including actin binding activity; phosphatidylinositol-3,4,5-trisphosphate binding activity; and type I transforming growth factor beta receptor binding activity. Involved in several processes, including cell surface receptor signaling pathway; positive regulation of cell differentiation; and positive regulation of cellular component biogenesis. Acts upstream of or withi…
- **Diseases (Open Targets)**: open-angle glaucoma (0.501); prostate carcinoma (0.488); glaucoma (0.488); neurodegenerative disease (0.473); primary angle-closure glaucoma (0.407)
- **Europe PMC papers**: 1336
- **Why important**: FERMT2 is a focal-adhesion and integrin-signaling gene with functions in cell adhesion, cell-matrix adhesion, receptor signaling, differentiation, and cellular component biogenesis. It is connected to COPB1 and is enhanced in adipocytes, podocytes, and smooth-muscle cells. It has disease associations involving glaucoma and prostate carcinoma and a substantial literature base. Its protein is detected in placenta but not bone marrow in the supplied HPA evidence, making it informative for tissue or cellular-composition interpretation.
- **Conclusion**: Established evidence supports FERMT2 as an adhesion and cell-state marker that may explain part of the placental contribution to the module. Its limited network connectivity and lack of bone-marrow protein detection make a shared cell-intrinsic role uncertain; a contribution from tissue composition is a reasonable hypothesis.

## Module 3

**Tissue pair**: bone_marrow and placenta  
**Genes (6)**: ACTN1, CALD1, FLNA, FLNB, FLNC, MVP

### Function

The module most plausibly represents an actin–membrane cytoskeleton and contractile-architecture program, rather than a narrowly defined pathway. Its strongest supporting evidence is the coherent presence of filamin, calponin-homology, actinin and myofibrillar or Z-disc features in the supplementary STRING results (14 supplementary STRING terms; within-query FDR 0.0087–0.0499). FLNC is the central network connector, linking the filamin genes with ACTN1 and the MVP–CALD1 branch. FLNA, FLNB and FLNC provide a filamin-based actin-crosslinking framework; ACTN1 supports actin–membrane attachment and platelet-related cytoskeletal functions; CALD1 supports actin–tropomyosin regulation and contraction; and MVP may connect the structural program with intracellular signaling and transport. No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The functional interpretation therefore rests on convergent gene descriptions, network structure and supplementary STRING domain or compartment evidence, not on a globally significant enrichment result.

**Cell composition.** This is not a plasma or secreted-protein module: the secretome annotation is absent for all members. HPA indicates a predominantly cell-associated cytoskeletal composition, with tissue or cell-type enhancement involving smooth muscle cells, myoepithelial cells, trophoblast populations, vascular or muscle-related cells and, for some genes, platelets or neutrophils. CALD1 and ACTN1 have immune or neutrophil-related HPA evidence, whereas several members have low immune-cell specificity or are not detected in immune cells. Most members are detected at the protein level in both bone marrow and placenta, while FLNC is not detected by the cited IHC assays in either tissue. The shared signal could therefore reflect smooth-muscle-like, vascular, trophoblast, stromal, platelet or related structural cell populations in the samples, rather than a tissue-wide housekeeping program or circulating plasma proteins.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a known filamin-centered structural neighborhood: FLNA–FLNB, FLNA–FLNC and FLNB–FLNC are strong relationships, and ACTN1–FLNA is also supported. These links agree with the supplementary actin-binding, filamin-domain, focal-adhesion, myofibril and Z-disc annotations (14 supplementary STRING terms; within-query FDR 0.0087–0.0499). The module graph is nevertheless sparse relative to all possible gene pairs, so the co-abundance pattern should not be treated as proof of one stable physical complex. No hu.MAP complex contains multiple module members. Thus, the evidence favors a shared cytoskeletal program assembled from known protein relationships rather than a newly identified hu.MAP-defined multiprotein complex. The STRING enrichment results remain supplementary and are not global GO/KEGG significance evidence.

**STRING interactions (score >= 0.7)**: 4 of 15 gene pairs: ACTN1–FLNA (0.716); FLNA–FLNB (0.979); FLNA–FLNC (0.907); FLNB–FLNC (0.921)
**STRING functional enrichment (supplementary, within-query FDR)**: InterPro Actinin-type actin-binding domain, conserved site (FDR = 0.0087, 4 genes); SMART Calponin homology domain (FDR = 0.0088, 4 genes); SMART Filamin-type immunoglobulin domains (FDR = 0.0088, 3 genes); COMPARTMENTS Z disc (FDR = 0.0089, 4 genes); InterPro Filamin/ABP280 repeat (FDR = 0.0189, 3 genes); InterPro Calponin homology domain (FDR = 0.0189, 4 genes); InterPro Filamin/ABP280 repeat-like (FDR = 0.0189, 3 genes); InterPro CH domain superfamily (FDR = 0.0189, 4 genes); InterPro Filamin family (FDR = 0.0189, 3 genes); InterPro Immunoglobulin E-set (FDR = 0.0219, 3 genes); WikiPathways Ebola virus infection in host (FDR = 0.0279, 4 genes); WikiPathways Focal adhesion (FDR = 0.0476, 4 genes); Component Myofibril (FDR = 0.0499, 5 genes); Component Z disc (FDR = 0.0499, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The molecular components and much of their biology are not intrinsically novel: filamins, ACTN1 and CALD1 are established actin-associated or contractile proteins, and STRING already documents several relationships among them. The potentially novel aspect is the coordinated co-abundance of this particular combination across bone marrow and placenta, especially the connection of muscle-, vascular-, trophoblast-, platelet- and stromal-associated signatures in a shared module. That claim should remain provisional because the fact sheet does not provide a comparison with prior tissue co-abundance modules or an external replication cohort. The absence of a hu.MAP complex does not establish novelty, and the lack of globally significant GO/KEGG enrichment does not invalidate the module.

**Hypothesis.** Hypothesis: the module reflects a conserved cell-structural state shared by selected bone-marrow and placental populations, in which filamin-mediated actin crosslinking, ACTN1-dependent actin anchoring and CALD1-dependent regulation of actomyosin tension support cell shape, adhesion, migration or contractility. FLNC may organize the central cytoskeletal scaffold, while FLNA and FLNB provide partially overlapping membrane-linked filamin functions. MVP may associate with this structural state through signaling or intracellular transport rather than as a direct component of the actin complex. In placenta, this could relate to trophoblast or vascular-stromal architecture; in bone marrow, it could relate to megakaryocyte or other structurally specialized cells. These tissue- and cell-type assignments are hypotheses from the HPA composition pattern, not demonstrated mechanisms in this module.

### Important genes

#### FLNC

- **Related proteins** (co-abundance neighbors): FLNA (0.95), ACTN1 (0.89), MVP (0.80), FLNB (0.80); STRING partners: FLNA (0.907), FLNB (0.921)
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin C. This gene encodes one of three related filamin genes, specifically gamma filamin. These filamin proteins crosslink actin filaments into orthogonal networks in cortical cytoplasm and participate in the anchoring of membrane proteins for the actin cytoskeleton. Three functional domains exist in filamin: an N-terminal filamentous actin-binding domain, a C-terminal self-association domain, and a membr…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy 26 (0.833); myofibrillar myopathy 5 (0.791); distal myopathy with posterior leg and anterior hand involvement (0.742); dilated cardiomyopathy (0.714); familial restrictive cardiomyopathy (0.660)
- **Europe PMC papers**: 3861
- **Why important**: FLNC is the principal network connector in the module and links to FLNA, FLNB, ACTN1 and MVP. Its established function is actin crosslinking and membrane-associated cytoskeletal anchoring, with GO descriptions involving actin cytoskeleton organization, sarcomere organization and muscle-cell development. It has strong muscle-associated HPA evidence and well-established cardiomyopathy and myopathy associations, with substantial literature volume. Its broad connectivity makes it the best candidate for the structural core of the module.
- **Conclusion**: Established evidence supports FLNC as a central actin-network organizer with muscle and cardiomyopathy relevance. It is plausible, but not proven here, that FLNC is the main scaffold coordinating the shared bone-marrow–placenta co-abundance program.

#### FLNA

- **Related proteins** (co-abundance neighbors): FLNC (0.95); STRING partners: ACTN1 (0.716), FLNB (0.979), FLNC (0.907)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is connected to FLNC in the module and has several known STRING relationships with ACTN1 and FLNB. It crosslinks actin, links the cytoskeleton to membrane glycoproteins and participates in cell-shape remodeling, migration, integrin and receptor-complex biology. Its HPA profile includes vascular and stromal or myoepithelial cell contexts, and its disease associations include several developmental skeletal and neurological syndromes. It is among the most extensively studied members of the module.
- **Conclusion**: Established evidence supports FLNA as a membrane-linked actin organizer and cell-migration regulator. Its presence is consistent with a structural or adhesion-related module, while any specific role in the shared tissues remains a hypothesis.

#### FLNB

- **Related proteins** (co-abundance neighbors): FLNC (0.80); STRING partners: FLNA (0.979), FLNC (0.921)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin B. This gene encodes a member of the filamin family. The encoded protein interacts with glycoprotein Ib alpha as part of the process to repair vascular injuries. The platelet glycoprotein Ib complex includes glycoprotein Ib alpha, and it binds the actin cytoskeleton. Mutations in this gene have been found in several conditions: atelosteogenesis type 1 and type 3; boomerang dysplasia; autosomal domina…
- **Diseases (Open Targets)**: Larsen syndrome (0.829); spondylocarpotarsal synostosis syndrome (0.775); atelosteogenesis type I (0.763); atelosteogenesis type III (0.756); Boomerang dysplasia (0.723)
- **Europe PMC papers**: 2274
- **Why important**: FLNB is a filamin-family member connected to FLNA and FLNC by STRING and participates in actin-cytoskeleton organization. Its documented interaction with glycoprotein Ib alpha is relevant to vascular injury repair and platelet-associated cytoskeletal function. HPA detects it in extravillous trophoblasts and other specialized cell populations, and its established skeletal dysplasia associations provide strong biological context. Its position directly alongside the other filamins makes it important for interpreting the module as a filamin-based structural program.
- **Conclusion**: Established evidence supports FLNB as a filamin-family cytoskeletal and vascular or platelet-related component with developmental disease relevance. A trophoblast-specific or bone-marrow-specific mechanistic role is not established by this module alone.

#### ACTN1

- **Related proteins** (co-abundance neighbors): FLNC (0.89); STRING partners: FLNA (0.716)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Actin filaments, Focal adhesion sites; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: actinin alpha 1. Alpha actinins belong to the spectrin gene superfamily which represents a diverse group of cytoskeletal proteins, including the alpha and beta spectrins and dystrophins. Alpha actinin is an actin-binding protein with multiple roles in different cell types. In nonmuscle cells, the cytoskeletal isoform is found along microfilament bundles and adherens-type junctions, where it is involved in binding …
- **Diseases (Open Targets)**: platelet-type bleeding disorder 15 (0.781); Macrothrombocytopenia (0.622); autosomal dominant macrothrombocytopenia (0.550); Thrombocytopenia (0.482); type 2 diabetes mellitus (0.410)
- **Europe PMC papers**: 3070
- **Why important**: ACTN1 connects to FLNC in the module and to FLNA in STRING. It anchors actin to membranes and microfilament bundles and has annotations for actin organization, platelet activation, platelet formation and platelet morphogenesis. HPA places it in smooth muscle, myoepithelial, extravillous trophoblast, neutrophil and platelet contexts. Its disease associations include platelet-type bleeding and thrombocytopenia disorders, making it especially informative for a possible megakaryocyte or platelet-related contribution in bone marrow.
- **Conclusion**: Established evidence supports ACTN1 as an actin-anchoring protein with platelet and cytoskeletal functions. Its contribution to the shared module may involve specialized adhesive or contractile cells, but the data do not distinguish platelet, progenitor or trophoblast mechanisms.

#### CALD1

- **Related proteins** (co-abundance neighbors): MVP (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Actin filaments; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caldesmon 1. This gene encodes a calmodulin- and actin-binding protein that plays an essential role in the regulation of smooth muscle and nonmuscle contraction. The conserved domain of this protein possesses the binding activities to Ca(2+)-calmodulin, actin, tropomyosin, myosin, and phospholipids. This protein is a potent inhibitor of the actin-tropomyosin activated myosin MgATPase, and serves as a mediating…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.499); diaphragmatic hernia (0.447); glaucoma (0.405); diverticular disease (0.393); open-angle glaucoma (0.390)
- **Europe PMC papers**: 3386
- **Why important**: CALD1 occupies the MVP-linked branch of the module and is the only member specifically represented in the supplementary myofibril component annotation alongside the broader structural signature (STRING Component Myofibril; within-query FDR = 0.0499). It binds calmodulin, actin, tropomyosin, myosin and phospholipids, and regulates actomyosin contraction. HPA associates it with myoepithelial, stromal, trophoblast and neutrophil-related contexts, while disease associations include skeletal, diaphragmatic and ocular abnormalities.
- **Conclusion**: Established evidence supports CALD1 as a regulator of actin–tropomyosin contractility. Its position suggests a possible contractile or tension-regulating arm of the module, but the proposed connection to MVP and tissue-specific mechanics remains hypothetical.

## Module 4

**Tissue pair**: bone_marrow and placenta  
**Genes (5)**: AGRN, FN1, MFGE8, LTF, THBS1

### Function

The strongest primary evidence supports extracellular glycosaminoglycan-binding and matrix-associated biology: (GO:MF glycosaminoglycan binding; q_global = 0.0493) links AGRN, FN1, LTF, and THBS1 to glycosaminoglycan binding. The supplementary STRING results reinforce glycosaminoglycan, sulfur-compound, heparin, and proteoglycan binding (STRING Function Glycosaminoglycan binding; within-query FDR = 0.0337)(STRING Function Sulfur compound binding; within-query FDR = 0.0337)(STRING Function Heparin binding; within-query FDR = 0.0418)(STRING Function Proteoglycan binding; within-query FDR = 0.0418), while epidermal growth factor-like domains are represented by AGRN, MFGE8, and THBS1 (STRING SMART Epidermal growth factor-like domain.; within-query FDR = 0.0185). The gene annotations support an extracellular interface involving adhesion, cell-matrix interactions, vascular or stromal biology, innate defense, iron binding, apoptotic-cell clearance, and tissue remodeling. FN1 and THBS1 provide matrix adhesion and regulatory functions; AGRN provides a glycosaminoglycan-modified extracellular scaffold; LTF adds iron-binding and antimicrobial activity; and MFGE8 adds apoptotic-cell clearance. Thus, the most defensible module interpretation is a secreted extracellular matrix and glycosaminoglycan-binding program that may integrate stromal or vascular remodeling with innate immune and tissue-interface functions. Only (GO:MF glycosaminoglycan binding; q_global = 0.0493) is primary GO evidence; the STRING terms are supplementary.

**Cell composition.** The module is strongly extracellular and secreted: HPA annotates every member as secreted, with FN1 and LTF secreted to blood, THBS1 secreted to extracellular matrix, and MFGE8 secreted to blood. Protein detection is present in bone marrow for every member and in placenta for nearly all members, with LTF specifically not detected in placenta by the supplied HPA result. This composition argues against interpreting the module as a pure intracellular pathway. It may reflect extracellular material in the samples, vascular or stromal cells, and shared tissue interfaces. HPA associates several members with fibroblasts, smooth-muscle or vascular smooth-muscle cells, and hepatic stellate cells; it also shows associations with trophoblast, pericyte, macrophage, monocyte, neutrophil, eosinophil, and regulatory T-cell populations. LTF is particularly compatible with bone-marrow myeloid or neutrophil biology, whereas FN1, THBS1, AGRN, and MFGE8 support matrix, vascular, stromal, or tissue-remodeling interpretations. Therefore, shared cell composition and extracellular protein carryover are plausible contributors to the conserved co-abundance pattern.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF glycosaminoglycan binding | 0.0493 | AGRN, FN1, LTF, THBS1 |

### STRING and hu.MAP

STRING provides high-confidence support for AGRN–FN1 and FN1–THBS1, establishing a connected extracellular matrix or glycosaminoglycan-related core. STRING also connects LTF with MFGE8, but this link is separate from the AGRN–FN1–THBS1 chain in the supplied pairwise network. The STRING functional results are concordant with the primary GO interpretation, especially for glycosaminoglycan, heparin, and proteoglycan binding (STRING Function Glycosaminoglycan binding; within-query FDR = 0.0337)(STRING Function Heparin binding; within-query FDR = 0.0418)(STRING Function Proteoglycan binding; within-query FDR = 0.0418). No hu.MAP complex contains multiple module members. This absence means that the module is not supported here as a canonical intracellular multiprotein complex; it does not negate extracellular co-function, secreted protein interaction, shared regulation, or sample-composition effects. Overall, the known STRING links support a biologically coherent extracellular network, while the incomplete pairwise connectivity indicates that co-abundance is broader than the currently documented physical interaction set.

**STRING interactions (score >= 0.7)**: 3 of 10 gene pairs: AGRN–FN1 (0.983); FN1–THBS1 (0.999); LTF–MFGE8 (0.826)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Epidermal growth factor-like domain. (FDR = 0.0185, 3 genes); Function Glycosaminoglycan binding (FDR = 0.0337, 4 genes); Function Sulfur compound binding (FDR = 0.0337, 4 genes); Function Heparin binding (FDR = 0.0418, 3 genes); Function Proteoglycan binding (FDR = 0.0418, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be described as a wholly new molecular pathway. Its central biology is already established by known FN1–THBS1 and AGRN–FN1 STRING relationships, the documented extracellular functions of the proteins, and concordant glycosaminoglycan-binding annotations. The conserved co-abundance of this particular gene set across bone marrow and placenta may nevertheless be a useful systems-level observation, especially because no multi-member hu.MAP complex is supplied and because LTF and MFGE8 connect immune or clearance biology with the matrix-associated core. That tissue-pair-specific co-abundance context is potentially novel, but it requires independent cohorts, adjustment for cell composition, and experimental validation before being called a new mechanism. Absence from hu.MAP or incomplete STRING connectivity alone is not evidence of novelty.

**Hypothesis.** Hypothesis: a shared vascular-stromal or tissue-interface compartment in bone marrow and placenta releases or presents a glycosaminoglycan-rich extracellular scaffold. FN1, THBS1, and AGRN could organize or modulate this matrix environment, while MFGE8 could support clearance of apoptotic material and LTF could contribute local iron sequestration and antimicrobial defense. The resulting extracellular milieu could couple tissue remodeling, vascular regulation, innate immune protection, and cell adhesion, producing the conserved co-abundance pattern. This is a hypothesis rather than a demonstrated causal pathway; it should be tested by cell-resolved expression, measurement of secreted proteins, and perturbation of the proposed matrix interactions.

### Important genes

#### FN1

- **Related proteins** (co-abundance neighbors): THBS1 (0.94), LTF (0.85); STRING partners: AGRN (0.983), THBS1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 is a central connector in the module, linking THBS1 and AGRN in the supplied network and appearing in the primary glycosaminoglycan-binding term (GO:MF glycosaminoglycan binding; q_global = 0.0493) and the supplementary binding terms (STRING Function Glycosaminoglycan binding; within-query FDR = 0.0337)(STRING Function Sulfur compound binding; within-query FDR = 0.0337)(STRING Function Heparin binding; within-query FDR = 0.0418)(STRING Function Proteoglycan binding; within-query FDR = 0.0418). Its established functions include cell adhesion, cell-matrix adhesion, migration, embryogenesis, wound healing, coagulation, host defense, and extracellular-matrix organization. HPA supports relevance to blood vessel, placenta, fibroblast, and extravillous-trophoblast contexts. It also has the broadest literature footprint among the selected genes and disease associations involving skeletal, renal, cardiovascular, developmental, and cancer phenotypes.
- **Conclusion**: Established evidence identifies FN1 as the most plausible structural hub and an anchor for the glycosaminoglycan-binding and matrix-adhesion interpretation. It is a leading candidate for organizing the shared extracellular program. It remains a hypothesis that FN1 directly drives the conserved co-abundance pattern rather than merely marking the relevant stromal or vascular compartment.

#### THBS1

- **Related proteins** (co-abundance neighbors): FN1 (0.94), MFGE8 (0.81); STRING partners: FN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum, Plasma membrane; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thrombospondin 1. The protein encoded by this gene is a subunit of a disulfide-linked homotrimeric protein. This protein is an adhesive glycoprotein that mediates cell-to-cell and cell-to-matrix interactions. This protein can bind to fibrinogen, fibronectin, laminin, type V collagen and integrins alpha-V/beta-1. This protein has been shown to play roles in platelet aggregation, angiogenesis, and tumorigenesis. [pro…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.385); tooth disorder (0.350); autism spectrum disorder (0.336); neurodegenerative disease (0.323); metabolic syndrome (0.309)
- **Europe PMC papers**: 12762
- **Why important**: THBS1 is a strong network connector to FN1 and MFGE8 and participates in (GO:MF glycosaminoglycan binding; q_global = 0.0493) plus every supplementary STRING functional category listed for the module (STRING SMART Epidermal growth factor-like domain.; within-query FDR = 0.0185)(STRING Function Glycosaminoglycan binding; within-query FDR = 0.0337)(STRING Function Sulfur compound binding; within-query FDR = 0.0337)(STRING Function Heparin binding; within-query FDR = 0.0418)(STRING Function Proteoglycan binding; within-query FDR = 0.0418). Its established roles include cell-to-cell and cell-to-matrix adhesion, platelet aggregation, angiogenesis regulation, inflammatory responses, and interactions with fibrinogen, fibronectin, laminin, collagen, and integrins. HPA places it in fibroblast, hepatic-stellate, macrophage, monocyte, and platelet-associated contexts, with extracellular-matrix secretion and detection in both tissues. It also has a substantial disease and literature record.
- **Conclusion**: Established evidence supports THBS1 as a multifunctional extracellular regulator connecting matrix adhesion with vascular and inflammatory biology. It is a strong candidate for mediating tissue remodeling or vascular-interface behavior in the module. Whether it is mechanistically upstream of the other members is unresolved.

#### AGRN

- **Related proteins** (co-abundance neighbors): LTF (0.82); STRING partners: FN1 (0.983)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: agrin. This gene encodes one of several proteins that are critical in the development of the neuromuscular junction (NMJ), as identified in mouse knock-out studies. The encoded protein contains several laminin G, Kazal type serine protease inhibitor, and epidermal growth factor domains. Additional post-translational modifications occur to add glycosaminoglycans and disulfide bonds. In one family with con…
- **Diseases (Open Targets)**: congenital myasthenic syndrome 8 (0.793); congenital myasthenic syndrome (0.680); presynaptic congenital myasthenic syndrome (0.652); postsynaptic congenital myasthenic syndrome (0.626); COVID-19 (0.546)
- **Europe PMC papers**: 2731
- **Why important**: AGRN contributes to the primary glycosaminoglycan-binding term (GO:MF glycosaminoglycan binding; q_global = 0.0493), connects to FN1 in STRING, and is also represented in the supplementary epidermal-growth-factor-like, glycosaminoglycan, sulfur-compound, and proteoglycan categories (STRING SMART Epidermal growth factor-like domain.; within-query FDR = 0.0185)(STRING Function Glycosaminoglycan binding; within-query FDR = 0.0337)(STRING Function Sulfur compound binding; within-query FDR = 0.0337)(STRING Function Proteoglycan binding; within-query FDR = 0.0418). Its established protein architecture includes laminin-G, Kazal-type inhibitor, and epidermal-growth-factor domains, with glycosaminoglycan modifications. Its known biology includes extracellular signaling and neuromuscular-junction development, and its disease associations include congenital myasthenic syndromes. HPA detects it in both tissues and supports multiple epithelial and renal cell-type associations.
- **Conclusion**: Established evidence makes AGRN a plausible extracellular scaffold or signaling ligand within the glycosaminoglycan-associated core. Its presence broadens the module beyond generic plasma proteins toward specialized matrix signaling. A role in bone-marrow or placental matrix remodeling is a hypothesis, not an annotation directly demonstrated by the supplied data.

#### LTF

- **Related proteins** (co-abundance neighbors): FN1 (0.85), AGRN (0.82); STRING partners: MFGE8 (0.826)
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lactotransferrin. This gene is a member of the transferrin family of genes and its protein product is found in the secondary granules of neutrophils. The protein is a major iron-binding protein in milk and body secretions with an antimicrobial activity, making it an important component of the non-specific immune system. The protein demonstrates a broad spectrum of properties, including regulation of iron homeostasi…
- **Diseases (Open Targets)**: tuberculosis (0.517); AL amyloidosis (0.467); Abnormality of the skeletal system (0.435); schizophrenia (0.235); inflammatory bowel disease (0.218)
- **Europe PMC papers**: 7000
- **Why important**: LTF is part of the primary glycosaminoglycan-binding term (GO:MF glycosaminoglycan binding; q_global = 0.0493) and the supplementary binding categories (STRING Function Glycosaminoglycan binding; within-query FDR = 0.0337)(STRING Function Sulfur compound binding; within-query FDR = 0.0337)(STRING Function Heparin binding; within-query FDR = 0.0418). It connects to AGRN and FN1 in the module network and is the clearest immune-associated member: its established functions include iron binding, iron homeostasis, antimicrobial defense, anti-inflammatory activity, and innate immune responses in mucosa. HPA associates it with bone marrow, salivary gland, neutrophil progenitors, neutrophils, and non-classical monocytes, and detects it in bone marrow but not placenta. Its disease and literature record is substantial.
- **Conclusion**: Established evidence supports LTF as an immune and secreted iron-binding component that may connect the matrix-associated module to bone-marrow myeloid biology. Its absence of placental protein detection raises the possibility that transcript co-abundance or shared extracellular regulation, rather than equivalent protein contribution in both tissues, underlies part of the conserved signal. Direct participation in the proposed matrix mechanism remains a hypothesis.

#### MFGE8

- **Related proteins** (co-abundance neighbors): THBS1 (0.81); STRING partners: LTF (0.826)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: milk fat globule EGF and factor V/VIII domain containing. This gene encodes a preproprotein that is proteolytically processed to form multiple protein products. The major encoded protein product, lactadherin, is a membrane glycoprotein that promotes phagocytosis of apoptotic cells. This protein has also been implicated in wound healing, autoimmune disease, and cancer. Lactadherin can be further processed to form a smaller cleavage product, medin, which c…
- **Diseases (Open Targets)**: AL amyloidosis (0.462); angina pectoris (0.339); myocardial ischemia (0.333); coronary artery bypass (0.314); coronary atherosclerosis (0.312)
- **Europe PMC papers**: 2623
- **Why important**: MFGE8 is connected to THBS1 in the module network and to LTF in STRING, and it contributes to the supplementary epidermal-growth-factor-like domain result (STRING SMART Epidermal growth factor-like domain.; within-query FDR = 0.0185). Its established function is promotion of phagocytosis of apoptotic cells, with additional roles reported in wound healing, autoimmune disease, cancer, and vascular amyloid biology. HPA identifies it as tissue enriched in blood vessel and associates it with fibroblasts, pericytes, decidual stromal cells, breast secretory cells, and regulatory T cells. It is detected in both bone marrow and placenta and has a meaningful disease and literature record.
- **Conclusion**: Established evidence supports MFGE8 as a vascular-stromal and apoptotic-cell-clearance component that could complement the FN1–THBS1 matrix axis. It is especially relevant to a tissue-interface model involving remodeling and clearance. Its direct functional coupling to LTF in this module is suggested by STRING but is not proven by the co-abundance data.

## Module 5

**Tissue pair**: bone_marrow and placenta  
**Genes (6)**: ANXA6, CLTC, GANAB, HYOU1, PDIA4, RRBP1

### Function

The module most plausibly represents endoplasmic-reticulum proteostasis linked to glycoprotein maturation, protein folding, secretion, and vesicular trafficking. PDIA4, GANAB, and HYOU1 provide a coherent ER quality-control axis: PDIA4 catalyzes disulfide rearrangement and supports immunoglobulin assembly, GANAB participates in glucose trimming during N-glycan processing, and HYOU1 supports ER folding and stress responses. RRBP1 connects ER membranes with ribosomes and secretory pathways, while CLTC and ANXA6 are compatible with intracellular trafficking and membrane remodeling. This interpretation is supported by the supplementary STRING term (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0328) and by the hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). However, no GO or KEGG term passed global correction, so the pathway interpretation remains integrative rather than globally significant enrichment evidence. The module should therefore be viewed as a biologically coherent ER and trafficking signal, not as proof of a single exclusive pathway.

**Cell composition.** The module is not dominated by broadly immune-specific genes: most members have low tissue specificity and low immune-cell specificity in HPA. All members are cell-type enhanced, with signals involving syncytiotrophoblasts, extravillous trophoblasts, and plasma cells; RRBP1 also has an immune-enhanced signal involving eosinophils and plasmacytoid dendritic cells. This makes shared trophoblast biology and secretory-cell biology plausible contributors in placenta, while plasma-cell or other secretory-cell representation could contribute in bone marrow. HPA detects the proteins throughout the placenta and in nearly all module members in bone marrow. The aggregate HPA summary flags several secreted genes, but the gene-level annotations predominantly place the proteins intracellularly, in the ER, cytosol, or endosomal and lysosomal compartments rather than describing a classic plasma-protein module. The tissue-enhanced pancreas signal for RRBP1 also indicates that the module contains a secretory-cell program rather than a narrowly bone-marrow-specific program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a known interaction core among GANAB, HYOU1, and PDIA4, with especially strong support for the HYOU1–PDIA4 relationship and additional support for the GANAB links. STRING's supplementary ER protein-processing term (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0328) includes GANAB, RRBP1, HYOU1, and PDIA4, but it is not a globally corrected module-level result. hu.MAP independently places PDIA4, GANAB, and HYOU1 together in both (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), indicating that this portion of the module overlaps known multiprotein machinery. RRBP1, CLTC, and ANXA6 do not have listed STRING partners or hu.MAP complexes in the supplied evidence, although they are connected to the known core through the co-abundance network. Thus, the module combines a previously characterized ER quality-control subnetwork with co-abundance links that may reflect shared cellular state, trafficking, or cell composition rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 3 of 15 gene pairs: GANAB–HYOU1 (0.83); GANAB–PDIA4 (0.717); HYOU1–PDIA4 (0.997)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Protein processing in endoplasmic reticulum (FDR = 0.0328, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (PDIA4, GANAB, HYOU1; 3/60); huMAP3_09327.1 (PDIA4, GANAB, HYOU1; 3/93)

### Novelty

The module is not wholly novel because the PDIA4–GANAB–HYOU1 core is represented in STRING and in two hu.MAP complexes. Conversely, the supplied evidence does not establish that this exact six-gene co-abundance module, or its conservation between bone marrow and placenta, has previously been reported. The links involving RRBP1, CLTC, and ANXA6 are not supported by listed STRING or hu.MAP relationships, but database absence alone cannot demonstrate novelty because interaction resources are incomplete and co-abundance is not equivalent to physical interaction. The cautious conclusion is that the module contains a known ER proteostasis core embedded in a potentially less-characterized tissue-shared co-abundance context; direct comparison with published co-expression modules and tissue-specific datasets would be required before calling the full module a new discovery.

**Hypothesis.** Hypothesis: in shared secretory or trophoblast-rich cellular contexts, increased demand for synthesis and export of folded and glycosylated proteins coordinates ER ribosome engagement through RRBP1, folding and disulfide quality control through PDIA4 and HYOU1, and N-glycan maturation through GANAB. The resulting protein flux may couple to CLTC-dependent vesicular trafficking and ANXA6-dependent membrane organization. The conservation between bone marrow and placenta may therefore reflect a shared secretory-cell or stress-adaptation program, potentially involving plasma cells in bone marrow and trophoblasts in placenta, rather than a tissue-independent interaction pathway. This hypothesis requires validation with cell-resolved expression, perturbation, and direct protein-interaction or ER-stress measurements.

### Important genes

#### PDIA4

- **Related proteins** (co-abundance neighbors): GANAB (0.85), HYOU1 (0.84), CLTC (0.83), ANXA6 (0.80); STRING partners: GANAB (0.717), HYOU1 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 is the most connected and strongest node in the module and directly links to GANAB and HYOU1 in STRING while occurring in both hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Its established function in ER disulfide exchange, protein folding, secretion, and immunoglobulin assembly makes it a strong mechanistic anchor. It is also detected in both tissues and has substantial literature support, with disease associations reported for neurodegenerative disease and neoplastic disorders.
- **Conclusion**: Established evidence supports PDIA4 as a central ER folding and secretory-quality-control component of the module. It is reasonable to hypothesize that PDIA4 helps organize the module's biological signal, but the co-abundance data do not establish that PDIA4 regulates the other genes or drives tissue sharing.

#### HYOU1

- **Related proteins** (co-abundance neighbors): RRBP1 (0.84), PDIA4 (0.84); STRING partners: GANAB (0.83), PDIA4 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 is tightly connected to PDIA4 and GANAB in STRING and is present in both hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Its known role as an ER heat-shock-family protein induced under hypoxia, with functions in folding, secretion, ER stress, vesicle transport, and protection from apoptosis, makes it particularly relevant to placenta and to stressed or highly secretory bone-marrow cells. It is detected in placenta and has disease associations including granulocytopenia with immunoglobulin abnormality and neurodegenerative disease.
- **Conclusion**: Established evidence supports HYOU1 as a stress-responsive ER chaperone within the known module core. Its placental detection and hypoxia-related biology make a stress-adaptation contribution plausible, but the lack of detection in bone marrow in the supplied HPA result means the cross-tissue interpretation should not assume uniform protein presence.

#### GANAB

- **Related proteins** (co-abundance neighbors): PDIA4 (0.85); STRING partners: HYOU1 (0.83), PDIA4 (0.717)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: glucosidase II alpha subunit. This gene encodes the alpha subunit of glucosidase II and a member of the glycosyl hydrolase 31 family of proteins. The heterodimeric enzyme glucosidase II plays a role in protein folding and quality control by cleaving glucose residues from immature glycoproteins in the endoplasmic reticulum. Expression of the encoded protein is elevated in lung tumor tissue and in response to UV irradiation. Mut…
- **Diseases (Open Targets)**: polycystic kidney disease 3 with or without polycystic liver disease (0.792); autosomal dominant polycystic liver disease (0.515); autosomal dominant polycystic kidney disease (0.470); Biliary tract abnormality (0.438); COVID-19 (0.370)
- **Europe PMC papers**: 1240
- **Why important**: GANAB is part of the known PDIA4–HYOU1 core, appears in both hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), and participates in ER glucose trimming and N-glycan processing. Its disease associations include autosomal-dominant polycystic kidney and liver disease. Although it is a lower-connectivity node than PDIA4, its enzymatic role complements disulfide-based folding and makes it important for maturation of secretory glycoproteins.
- **Conclusion**: Established evidence supports GANAB as the glycan-processing component of the ER quality-control core. Its presence supports a model involving maturation of secreted or membrane glycoproteins, but the module does not establish a disease-specific glycosylation defect or a direct causal role in either tissue.

#### RRBP1

- **Related proteins** (co-abundance neighbors): HYOU1 (0.84), CLTC (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosome binding protein 1. This gene encodes a ribosome-binding protein of the endoplasmic reticulum (ER) membrane. Studies suggest that this gene plays a role in ER proliferation, secretory pathways and secretory cell differentiation, and mediation of ER-microtubule interactions. Alternative splicing has been observed and protein isoforms are characterized by regions of N-terminal decapeptide and C-terminal heptad repeats.…
- **Diseases (Open Targets)**: cancer (0.476); dengue disease (0.462); neurodegenerative disease (0.324); coronary artery disorder (0.292); placental abruption (0.279)
- **Europe PMC papers**: 1654
- **Why important**: RRBP1 connects the module to ER membrane organization, ribosome binding, secretory pathways, and secretory-cell differentiation. It is linked by co-abundance to HYOU1 and CLTC and is included in the supplementary STRING ER-processing term (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0328), even though no listed STRING partner or hu.MAP complex is provided for it. Its tissue-enhanced pancreas signal and cell-type signals in pancreatic and salivary acinar cells, syncytiotrophoblasts, eosinophils, and plasmacytoid dendritic cells make it informative for interpreting the module as a secretory-cell program. It also has a reported association with placental abruption and substantial literature support.
- **Conclusion**: Established evidence supports RRBP1 as an ER membrane and secretory-pathway marker that broadens the module beyond the physical interaction core. Its co-abundance with the core may reflect coordinated secretory demand or cell composition; a direct molecular interaction with the other module members is not established here.

#### CLTC

- **Related proteins** (co-abundance neighbors): RRBP1 (0.84), PDIA4 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: clathrin heavy chain. Clathrin is a major protein component of the cytoplasmic face of intracellular organelles, called coated vesicles and coated pits. These specialized organelles are involved in the intracellular trafficking of receptors and endocytosis of a variety of macromolecules.  The basic subunit of the clathrin coat is composed of three heavy chains and three light chains. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: intellectual disability, autosomal dominant 56 (0.787); cancer (0.576); hereditary disease (0.540); Alzheimer disease (0.466); neurodegenerative disease (0.465)
- **Europe PMC papers**: 2902
- **Why important**: CLTC connects to RRBP1 and PDIA4 in the module and provides an intracellular trafficking interpretation through its established role as the clathrin heavy chain in coated vesicles, endocytosis, and receptor transport. It is detected in both tissues and has a broad disease literature, including intellectual disability and neurodegenerative disease associations. Its neutrophil cell-type signal may also contribute to bone-marrow sample composition.
- **Conclusion**: Established evidence supports CLTC as a trafficking component that could connect ER output to downstream vesicle handling. Its inclusion in the co-abundance module does not prove that clathrin directly assembles with the ER quality-control core, so the trafficking connection remains a mechanistic interpretation rather than a demonstrated complex.

## Module 6

**Tissue pair**: bone_marrow and placenta  
**Genes (9)**: CALU, CAPN2, CORO1C, DPYSL3, MAP1B, PDLIM5, PDLIM7, TPM1, WDR1

### Function

The module is most consistent with a cytoskeletal organization and remodeling program, especially involving actin filaments, focal-adhesion or membrane-associated scaffolding, contractile machinery, and linked microtubule organization. This interpretation is supported by the functions of TPM1, PDLIM5, PDLIM7, CORO1C, WDR1, DPYSL3, MAP1B, and CAPN2. CALU adds an endoplasmic-reticulum calcium-binding and protein-folding component. No GO or KEGG term passed global correction, so the functional interpretation is gene- and network-based rather than enrichment-based. There was also no supplementary STRING functional enrichment.

**Cell composition.** The module is not dominated by plasma or secreted proteins: HPA identifies only CALU as having intracellular and membrane secretome annotation, while the other genes are not annotated as secreted. The composition is mixed rather than uniformly blood-cell specific or uniformly housekeeping-like. HPA repeatedly links genes to smooth muscle, vascular smooth muscle, skeletal muscle, heart muscle, platelets, megakaryocytes, and extravillous trophoblasts. Several genes also have low tissue specificity, while others are enhanced in muscle, blood vessel, brain, retina, or placenta-associated cell types. This pattern suggests that the shared bone-marrow and placenta signal may partly reflect common cytoskeletal programs and shared vascular, contractile, platelet, megakaryocyte, or trophoblast-related cell populations. Protein detection in both tissues for several genes supports biological presence, but the absence of immunohistochemical detection for some genes means that transcript co-abundance should not be interpreted as uniform protein abundance across either tissue.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, between PDLIM5 and PDLIM7. hu.MAP provides the complex relationship (hu.MAP huMAP3_11076.1), in which WDR1 and CORO1C occur together with actin-associated proteins including CFL1, CORO1A, DSTN, SYNPO, AFAP1, CORO1B, CFL2, and CORO6. Thus, the module contains a supported PDLIM scaffold relationship and a supported WDR1-CORO1C complex membership relationship. The remaining co-abundance relationships are not supported by the reported STRING interaction evidence or hu.MAP complex membership. This combination suggests that the module is a broader coordinated expression program around cytoskeletal and contractile biology, rather than a single experimentally established protein complex.

**STRING interactions (score >= 0.7)**: 1 of 36 gene pairs: PDLIM5–PDLIM7 (0.81)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11076.1 (WDR1, CORO1C; 2/10)

### Novelty

The shared co-abundance module may represent a new tissue-pair-level observation, but the fact sheet does not establish it as a new molecular mechanism. Its most defensible novelty is the combination of genes co-abundant across bone marrow and placenta despite having limited STRING support and only one hu.MAP complex containing multiple module members. However, absence from STRING or hu.MAP does not prove novelty: it may reflect incomplete interaction coverage, tissue-specific regulation, indirect regulation, or co-expression without direct physical binding. The module should therefore be described as a potentially novel cross-tissue co-abundance pattern whose mechanistic novelty remains to be tested.

**Hypothesis.** Hypothesis: the module reflects a shared cell-structural state in vascular, contractile, platelet or megakaryocyte, and trophoblast-related populations in bone marrow and placenta. In this model, PDLIM5 and PDLIM7 organize actin-associated signaling and contractile structures; TPM1 stabilizes actin filaments; CORO1C and WDR1 coordinate actin-associated remodeling; CAPN2 provides calcium-responsive proteolytic remodeling; DPYSL3 links actin organization with cell projection and migration programs; MAP1B contributes microtubule organization; and CALU may couple endoplasmic-reticulum calcium handling or protein folding to cytoskeletal behavior. This is a mechanistic hypothesis, not a demonstrated pathway or complex.

### Important genes

#### DPYSL3

- **Related proteins** (co-abundance neighbors): CALU (0.90), MAP1B (0.87), WDR1 (0.82), CORO1C (0.82), PDLIM5 (0.81), PDLIM7 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dihydropyrimidinase like 3. Enables filamin binding activity. Predicted to be involved in several processes, including actin filament organization; regulation of plasma membrane bounded cell projection organization; and response to axon injury. Predicted to act upstream of or within nervous system development. Predicted to be located in several cellular components, including cell body; growth cone; and lamellipodium. Predict…
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); brain compression (0.326); edema (0.326); liver disorder (0.214); alcohol drinking (0.200)
- **Europe PMC papers**: 1082
- **Why important**: DPYSL3 has the strongest central network position in the module and connects to CALU, MAP1B, WDR1, CORO1C, PDLIM5, and PDLIM7. Its annotation includes filamin binding, actin filament organization, cell projection organization, cell migration, neuron projection development, and response to axon injury. It is not detected in immune cells and has no reported STRING partners or hu.MAP complex membership, making its central co-abundance position particularly informative. Its extensive literature and disease associations also make it a biologically prominent bridge between cytoskeletal and cell-projection programs.
- **Conclusion**: Established evidence supports DPYSL3 as a cytoskeleton- and cell-projection-associated protein with a central position in this module. The hypothesis that it coordinates the other module genes in bone marrow or placenta is plausible from the co-abundance structure but is not established by the reported interaction databases.

#### TPM1

- **Related proteins** (co-abundance neighbors): CORO1C (0.81), CAPN2 (0.80), PDLIM7 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tropomyosin 1. This gene is a member of the tropomyosin family of highly conserved, widely distributed actin-binding proteins involved in the contractile system of striated and smooth muscles and the cytoskeleton of non-muscle cells. Tropomyosin is composed of two alpha-helical chains arranged as a coiled-coil. It is polymerized end to end along the two grooves of actin filaments and provides stability to the fi…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy (0.798); left ventricular noncompaction (0.760); left ventricular noncompaction 9 (0.664); familial isolated dilated cardiomyopathy (0.639); hypertrophic cardiomyopathy 3 (0.596)
- **Europe PMC papers**: 6278
- **Why important**: TPM1 is a conserved actin-binding tropomyosin associated with stabilization of actin filaments, cytoskeleton organization, muscle contraction, and regulation of cell shape. HPA links it strongly to heart and skeletal muscle and to several stromal, trophoblast, megakaryocyte, and basophil cell types. Its module connections to CORO1C, CAPN2, and PDLIM7 place it at the interface of actin stability, remodeling, and contractile biology. It also has substantial literature and well-established cardiac disease associations.
- **Conclusion**: Established evidence supports TPM1 as a structural actin and contractile-system component. Its presence in the module supports a contractile or actin-stabilizing interpretation, while a specific role in the shared bone-marrow and placenta state remains a hypothesis.

#### PDLIM7

- **Related proteins** (co-abundance neighbors): DPYSL3 (0.81), TPM1 (0.80); STRING partners: PDLIM5 (0.81)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Actin filaments, Focal adhesion sites; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 7. The protein encoded by this gene is representative of a family of proteins composed of conserved PDZ and LIM domains. LIM domains are proposed to function in protein-protein recognition in a variety of contexts including gene transcription and development and in cytoskeletal interaction. The LIM domains of this protein bind to protein kinases, whereas the PDZ domain binds to actin filaments. The g…
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); nasopharyngeal carcinoma (0.121); neoplasm (0.120); lymphoma (0.115); Hodgkins lymphoma (0.105)
- **Europe PMC papers**: 808
- **Why important**: PDLIM7 is an actin-filament and focal-adhesion-associated PDZ-LIM scaffold linked to actin cytoskeleton organization, heart development, muscle structure, and receptor-mediated endocytosis. It is enhanced in blood vessel, intestine, and skeletal muscle and is associated with myoepithelial, stromal, hepatic stellate, megakaryocyte, and neutrophil populations. It connects to DPYSL3 and TPM1 and has the module's reported STRING relationship with PDLIM5, providing direct support for a scaffold-centered substructure.
- **Conclusion**: Established evidence supports PDLIM7 as an actin-associated signaling and structural scaffold, with a known relationship to PDLIM5. Its role as an organizer of the entire cross-tissue module is a hypothesis based on network context rather than a demonstrated molecular mechanism.

#### CORO1C

- **Related proteins** (co-abundance neighbors): DPYSL3 (0.82), TPM1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: huMAP3_11076.1
- **Function (MyGene.info)**: coronin 1C. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.453); Parkinson disease (0.322); Alzheimer disease (0.312); lysosomal storage disease (0.310); liver disorder (0.261)
- **Europe PMC papers**: 774
- **Why important**: CORO1C is a WD-repeat protein associated with actin filament organization, phagocytosis, signal transduction, and regulation of protein phosphorylation. It is detected by immunohistochemistry in both tissues and is cell-type enhanced in platelets. CORO1C is connected to DPYSL3 and TPM1 in the module and participates with WDR1 in the hu.MAP complex (hu.MAP huMAP3_11076.1), which also contains several actin-remodeling proteins. Its literature and disease associations provide additional support for its relevance to cytoskeletal regulation.
- **Conclusion**: Established evidence supports CORO1C as an actin-associated regulatory and complex component present in both tissues. A role in linking platelet or trophoblast-associated cytoskeletal remodeling to the wider module is plausible but remains a hypothesis.

#### WDR1

- **Related proteins** (co-abundance neighbors): DPYSL3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions, Cytosol; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: huMAP3_11076.1
- **Function (MyGene.info)**: WD repeat domain 1. This gene encodes a protein containing 9 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, mostly including a trp-asp at the C-terminal end. WD domains are involved in protein-protein interactions. The encoded protein may help induce the disassembly of actin filaments. Two transcript variants encoding different isoforms have been found for…
- **Diseases (Open Targets)**: periodic fever, immunodeficiency, and thrombocytopenia syndrome (0.705); gout (0.528); neurodegenerative disease (0.526); atrial fibrillation (0.519); intellectual developmental disorder 61 (0.416)
- **Europe PMC papers**: 1861
- **Why important**: WDR1 is an actin-filament depolymerization regulator with annotations for cortical cytoskeleton organization, platelet formation, and neutrophil-mediated immunity. HPA links it to megakaryocytes and platelets and detects it in both tissues. Its membership with CORO1C in hu.MAP complex (hu.MAP huMAP3_11076.1) supplies the clearest complex-level evidence for actin remodeling within the module, even though WDR1 has no reported STRING partner in the fact sheet.
- **Conclusion**: Established evidence supports WDR1 as an actin-remodeling and platelet-associated protein that participates with CORO1C in (hu.MAP huMAP3_11076.1). Its contribution to a shared bone-marrow and placenta cytoskeletal state is a reasonable hypothesis, not a proven tissue-specific mechanism.

## Module 7

**Tissue pair**: bone_marrow and placenta  
**Genes (5)**: CD44, IQGAP1, SPTBN1, SPTAN1, TLN1

### Function

The module is most consistent with a plasma-membrane, actin-cytoskeleton, cell-adhesion, and cell-motility program. SPTBN1 is the central network hub, connecting SPTAN1, IQGAP1, CD44, and TLN1. The gene functions support a coherent scaffold involving spectrins, adhesion receptors, integrin-associated talin, and IQGAP1-mediated cytoskeletal and signaling regulation. The STRING results provide supplementary support for RAF/MAP kinase signaling (STRING RCTM RAF/MAP kinase cascade; within-query FDR = 0.0052), nephrin-family interactions (STRING RCTM Nephrin family interactions; within-query FDR = 0.0143), RHOU and RHOV GTPase-cycle relationships (STRING RCTM RHOU GTPase cycle; within-query FDR = 0.0143) (STRING RCTM RHOV GTPase cycle; within-query FDR = 0.0143), and growth-factor signal transduction (STRING RCTM Diseases of signal transduction by growth factor receptors and second messengers; within-query FDR = 0.0375). However, no GO or KEGG term passed global correction, so there is no globally significant GO/KEGG enrichment to report. The absence of a globally corrected term does not invalidate the module.

**Cell composition.** All module proteins were detected in both bone marrow and placenta by HPA. The module is not dominated by secreted or plasma proteins: CD44 is the only gene annotated as secreted to blood, while the other proteins are intracellular or membrane-associated. HPA reports low immune-cell specificity for every gene, so this is not a strongly blood-cell-specific module despite its occurrence in bone marrow. The single-cell annotations include neutrophils, monocytes, dendritic cells, mast cells, megakaryocytes, platelets, endothelial cells, and other stromal or tissue cell types. This breadth favors a shared structural or adhesion program, although sample cell composition could contribute to the observed co-abundance. CD44 and TLN1 provide particular links to immune, vascular, platelet, and adhesive cellular contexts.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports four high-confidence pairwise relationships among the module genes. IQGAP1 connects with CD44, TLN1, and SPTAN1, while SPTAN1 has a very strong relationship with SPTBN1. These links make the module more than an arbitrary co-expression group and support a cytoskeletal adhesion network. The supplementary STRING pathways converge on MAP kinase signaling, nephrin-family interactions, RHOU and RHOV GTPase cycles, and growth-factor signaling (STRING RCTM RAF/MAP kinase cascade; within-query FDR = 0.0052) (STRING RCTM Nephrin family interactions; within-query FDR = 0.0143) (STRING RCTM RHOU GTPase cycle; within-query FDR = 0.0143) (STRING RCTM RHOV GTPase cycle; within-query FDR = 0.0143) (STRING RCTM Diseases of signal transduction by growth factor receptors and second messengers; within-query FDR = 0.0375), but they are not globally corrected enrichment results. hu.MAP places SPTBN1 and SPTAN1 together in three complexes (hu.MAP huMAP3_07940.1) (hu.MAP huMAP3_05473.1) (hu.MAP huMAP3_09165.1). Those complexes additionally contain spectrin-related, actin-associated, membrane-trafficking, adhesion, and signaling proteins. The repeated SPTBN1-SPTAN1 pairing is established complex-level support, whereas IQGAP1, CD44, and TLN1 do not occur in the listed hu.MAP complexes.

**STRING interactions (score >= 0.7)**: 4 of 10 gene pairs: CD44–IQGAP1 (0.988); IQGAP1–SPTAN1 (0.753); IQGAP1–TLN1 (0.893); SPTAN1–SPTBN1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM RAF/MAP kinase cascade (FDR = 0.0052, 4 genes); RCTM Nephrin family interactions (FDR = 0.0143, 3 genes); RCTM RHOU GTPase cycle (FDR = 0.0143, 3 genes); RCTM RHOV GTPase cycle (FDR = 0.0143, 3 genes); RCTM Diseases of signal transduction by growth factor receptors and second messengers (FDR = 0.0375, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07940.1 (SPTBN1, SPTAN1; 2/5); huMAP3_05473.1 (SPTBN1, SPTAN1; 2/7); huMAP3_09165.1 (SPTBN1, SPTAN1; 2/39)

### Novelty

This module should not be described as a wholly new molecular mechanism. Spectrin pairing, CD44-IQGAP1 association, IQGAP1-TLN1 association, and cytoskeletal adhesion functions are already supported by STRING, hu.MAP, and gene annotations. Its potentially novel aspect is the conserved co-abundance of this particular combination across bone marrow and placenta, especially the integration of a spectrin scaffold with CD44, IQGAP1, and talin. That claim remains provisional: the module is small, has no globally significant GO/KEGG term, and may partly reflect shared cell types or general structural gene expression. Absence of a relationship from hu.MAP or STRING would not by itself establish novelty.

**Hypothesis.** Hypothesis: in shared bone-marrow and placental cellular populations, an SPTBN1-SPTAN1 spectrin scaffold may organize membrane and cortical actin architecture while IQGAP1 couples that scaffold to CD44 and talin-dependent adhesion. This could coordinate cell shape, migration, cell-cell or cell-matrix attachment, and growth-factor or small-GTPase signaling. The hypothesis is consistent with the network topology, the STRING pathway signals (STRING RCTM RAF/MAP kinase cascade; within-query FDR = 0.0052) (STRING RCTM Nephrin family interactions; within-query FDR = 0.0143) (STRING RCTM RHOU GTPase cycle; within-query FDR = 0.0143) (STRING RCTM RHOV GTPase cycle; within-query FDR = 0.0143) (STRING RCTM Diseases of signal transduction by growth factor receptors and second messengers; within-query FDR = 0.0375), and the known functions of the genes, but the co-abundance data do not demonstrate physical assembly, pathway activity, or causality.

### Important genes

#### SPTBN1

- **Related proteins** (co-abundance neighbors): SPTAN1 (0.91), IQGAP1 (0.91), CD44 (0.82), TLN1 (0.80); STRING partners: SPTAN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: huMAP3_07940.1, huMAP3_05473.1, huMAP3_09165.1
- **Function (MyGene.info)**: spectrin beta, non-erythrocytic 1. Spectrin is an actin crosslinking and molecular scaffold protein that links the plasma membrane to the actin cytoskeleton, and functions in the determination of cell shape, arrangement of transmembrane proteins, and organization of organelles. It is composed of two antiparallel dimers of alpha- and beta- subunits. This gene is one member of a family of beta-spectrin genes. The encoded protein cont…
- **Diseases (Open Targets)**: developmental delay, impaired speech, and behavioral abnormalities (0.802); cancer (0.597); hereditary disease (0.516); hearing loss disorder (0.459); neurodevelopmental disorder (0.453)
- **Europe PMC papers**: 1635
- **Why important**: SPTBN1 is the network hub, linked to every other module member, and has the greatest weighted network strength. It is an actin-crosslinking and membrane-scaffold protein involved in plasma-membrane organization and vesicle transport. It also participates in all three listed hu.MAP complexes and in every supplementary STRING pathway signal (STRING RCTM RAF/MAP kinase cascade; within-query FDR = 0.0052) (STRING RCTM Nephrin family interactions; within-query FDR = 0.0143) (STRING RCTM RHOU GTPase cycle; within-query FDR = 0.0143) (STRING RCTM RHOV GTPase cycle; within-query FDR = 0.0143) (STRING RCTM Diseases of signal transduction by growth factor receptors and second messengers; within-query FDR = 0.0375). Its disease associations include developmental and neurodevelopmental phenotypes, and its literature support is substantial.
- **Conclusion**: Established evidence identifies SPTBN1 as the principal structural organizer and network anchor. It is a strong candidate for coordinating the module, but the data do not establish that it causally drives the shared tissue pattern.

#### IQGAP1

- **Related proteins** (co-abundance neighbors): SPTBN1 (0.91); STRING partners: CD44 (0.988), SPTAN1 (0.753), TLN1 (0.893)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IQ motif containing GTPase activating protein 1. This gene encodes a member of the IQGAP family. The protein contains four IQ domains, one calponin homology domain, one Ras-GAP domain and one WW domain. It interacts with components of the cytoskeleton, with cell adhesion molecules, and with several signaling molecules to regulate cell morphology and motility. Expression of the protein is upregulated by gene amplification in two gastric cancer ce…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.515); Costello syndrome (0.503); allergic rhinitis (0.474)
- **Europe PMC papers**: 3787
- **Why important**: IQGAP1 is connected to SPTBN1 and has STRING relationships with CD44, TLN1, and SPTAN1. It links cytoskeletal organization to cell adhesion, motility, MAPK signaling, growth-factor receptor signaling, and small-GTPase-related processes. It appears in all supplementary STRING signals (STRING RCTM RAF/MAP kinase cascade; within-query FDR = 0.0052) (STRING RCTM Nephrin family interactions; within-query FDR = 0.0143) (STRING RCTM RHOU GTPase cycle; within-query FDR = 0.0143) (STRING RCTM RHOV GTPase cycle; within-query FDR = 0.0143) (STRING RCTM Diseases of signal transduction by growth factor receptors and second messengers; within-query FDR = 0.0375), is associated with neutrophils by single-cell HPA annotation, and has the largest literature volume among the module genes.
- **Conclusion**: Established evidence supports IQGAP1 as the signaling and adhesion interface of the module. It is a plausible mediator between membrane contacts and cytoskeletal remodeling, although that role in this specific cross-tissue module remains a hypothesis.

#### SPTAN1

- **Related proteins** (co-abundance neighbors): SPTBN1 (0.91); STRING partners: IQGAP1 (0.753), SPTBN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Microtubules; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: huMAP3_07940.1, huMAP3_05473.1, huMAP3_09165.1
- **Function (MyGene.info)**: spectrin alpha, non-erythrocytic 1. Spectrins are a family of filamentous cytoskeletal proteins that function as essential scaffold proteins that stabilize the plasma membrane and organize intracellular organelles. Spectrins are composed of alpha and beta dimers that associate to form tetramers linked in a head-to-head arrangement. This gene encodes an alpha spectrin that is specifically expressed in nonerythrocytic cells. The encod…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 5 (0.749); developmental delay with or without epilepsy (0.681); spastic paraplegia 91, autosomal dominant, with or without cerebellar ataxia (0.681); infantile spasms (0.651); genetic developmental and epileptic encephalopathy (0.651)
- **Europe PMC papers**: 1422
- **Why important**: SPTAN1 forms the strongest listed STRING relationship with SPTBN1 and is present with SPTBN1 in all three hu.MAP complexes (hu.MAP huMAP3_07940.1) (hu.MAP huMAP3_05473.1) (hu.MAP huMAP3_09165.1). As a non-erythrocytic alpha-spectrin, it provides the complementary spectrin component of a membrane-stabilizing scaffold and is annotated for actin-cytoskeleton organization. Its disease associations include developmental and epileptic encephalopathy phenotypes.
- **Conclusion**: Established evidence supports SPTAN1 as the principal partner of the SPTBN1 structural scaffold. The module data support a shared spectrin architecture, but do not show whether this architecture is active in all contributing cell types.

#### CD44

- **Related proteins** (co-abundance neighbors): SPTBN1 (0.82); STRING partners: IQGAP1 (0.988)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD44 molecule (IN blood group). The protein encoded by this gene is a cell-surface glycoprotein involved in cell-cell interactions, cell adhesion and migration. It is a receptor for hyaluronic acid (HA) and can also interact with other ligands, such as osteopontin, collagens, and matrix metalloproteinases (MMPs). This protein participates in a wide variety of cellular functions including lymphocyte activation, recirculation and …
- **Diseases (Open Targets)**: nephrolithiasis, calcium oxalate (0.523); calcium oxalate urolithiasis (0.521); uterine corpus leiomyoma (0.480); systemic lupus erythematosus (0.467); autoimmune disease (0.330)
- **Europe PMC papers**: 102058
- **Why important**: CD44 is a cell-surface adhesion receptor connected to SPTBN1 in the module and to IQGAP1 by a very high-confidence STRING relationship. It mediates interactions involving hyaluronic acid and other matrix or adhesion ligands and is implicated in cell adhesion, migration, hematopoiesis, and immune-cell trafficking. HPA annotates it in neutrophils, monocytes, dendritic cells, mast cells, and basal keratinocytes, and it is the sole secreted-to-blood gene in the module. It has a very large literature base.
- **Conclusion**: Established evidence makes CD44 the clearest extracellular or membrane interface in the module. Its broad immune and tissue annotation means it may also report cell composition, so a specific bone-marrow-to-placenta mechanism should not be inferred without cell-resolved tests.

#### TLN1

- **Related proteins** (co-abundance neighbors): SPTBN1 (0.80); STRING partners: IQGAP1 (0.893)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in bone_marrow, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 connects to SPTBN1 in the module and to IQGAP1 in STRING. It is a focal-adhesion and cytoskeletal protein involved in integrin activation, cell adhesion, junction assembly, and migration. HPA associates it with blood vessels and with megakaryocyte and platelet groups. It also contributes to the supplementary RAF/MAP kinase and growth-factor signaling signals (STRING RCTM RAF/MAP kinase cascade; within-query FDR = 0.0052) (STRING RCTM Diseases of signal transduction by growth factor receptors and second messengers; within-query FDR = 0.0375), and has established disease associations including cancer and developmental syndromes.
- **Conclusion**: Established evidence supports TLN1 as the integrin and focal-adhesion component of the network. Its vascular and platelet annotations make it biologically relevant to both tissues, but they also leave open the possibility that the module reflects shared vascular or platelet content rather than a tissue-specific mechanism.
