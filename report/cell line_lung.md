# Conserved co-abundance modules: cell line and lung

## Module 0

**Tissue pair**: cell line and lung  
**Genes (7)**: ABCB7, ATP2C1, PDS5B, PHIP, PRKDC, SEC24C, SUPV3L1

### Function

This is a small, heterogeneous co-abundance module rather than a module with a clearly established canonical pathway. No GO or KEGG term passed global correction, so those resources provide no primary enrichment evidence. The gene annotations instead point to several cellular systems: mitochondrial RNA quality control through SUPV3L1; mitochondrial iron-sulfur and heme handling through ABCB7; DNA damage repair and chromosomal maintenance through PRKDC and PDS5B; intracellular signaling and growth regulation through PHIP; Golgi calcium handling through ATP2C1; and ER-to-Golgi cargo transport through SEC24C. The network connects these functions through SUPV3L1, PHIP, PDS5B, and PRKDC, but the connections do not establish a single biochemical pathway. The most cautious interpretation is a conserved cellular-state module involving genome maintenance, mitochondrial homeostasis, and membrane or secretory trafficking.

**Cell composition.** The module does not resemble a plasma-protein or secreted-protein module: no member is annotated as secreted. HPA reports low tissue specificity for every member and low immune-cell specificity for every member, with no recurrent enriched blood-cell category. Protein was detected in lung for every member. A few genes show cell-type enhancement, but the enhanced cell types are disparate rather than a coherent blood or immune population. Thus, the module is more consistent with broadly expressed intracellular proteins than with an obvious blood-contamination signature, although shared cellular composition and general tissue state could still contribute to its conservation between cell line and lung.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING reports no high-confidence interaction among the module members and no supplementary STRING enrichment. Therefore, the co-abundance edges are not supported as already-known direct protein interactions by the supplied STRING evidence. hu.MAP identifies one complex, (hu.MAP huMAP3_09592.1), containing ABCB7 and PRKDC, but these are only a small subset of a broad complex membership list. This provides limited support for a shared complex context, not proof that the complete module is a physical complex. The remaining relationships are not represented in the supplied hu.MAP or STRING evidence.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09592.1 (ABCB7, PRKDC; 2/95)

### Novelty

The complete co-abundance pattern appears potentially novel because it is not reproduced as a high-confidence STRING interaction network, has no STRING functional enrichment, and is not represented as a compact hu.MAP complex. However, absence from those resources does not prove biological novelty: co-abundance can reflect co-regulation, shared cell state, organelle coordination, or indirect functional coupling rather than physical binding. In addition, the lack of globally significant GO or KEGG enrichment means that the module currently lacks independent pathway-level confirmation. It should therefore be described as a potentially new, data-derived cross-context association that requires replication and experimental or perturbational validation.

**Hypothesis.** Hypothesis: the module may represent a coordinated intracellular stress or growth state in which mitochondrial RNA and iron-sulfur homeostasis, DNA damage surveillance, chromosomal maintenance, calcium handling, and secretory trafficking are jointly regulated. SUPV3L1 and ABCB7 could mark mitochondrial maintenance, PRKDC and PDS5B could mark genome integrity, PHIP could connect growth or signaling state to the nuclear network, and ATP2C1 with SEC24C could reflect membrane-trafficking and calcium demands. This is a mechanistic hypothesis rather than an established pathway assignment, because the module has no globally significant GO or KEGG term and no high-confidence STRING interaction support.

### Important genes

#### SUPV3L1

- **Related proteins** (co-abundance neighbors): PHIP (0.83), ABCB7 (0.81), PRKDC (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Suv3 like RNA helicase. Enables helicase activity; nucleic acid binding activity; and protein homodimerization activity. Involved in several processes, including mitochondrial RNA metabolic process; mitochondrion morphogenesis; and positive regulation of mitochondrial RNA catabolic process. Located in mitochondrial nucleoid and nucleus. Part of mitochondrial degradosome. [provided by Alliance of Genome Resources, Apr 202…
- **Diseases (Open Targets)**: neurodegenerative disease (0.541); response to vaccine (0.276); neoplasm (0.041); gestational diabetes (0.036); seasonal allergic rhinitis (0.025)
- **Europe PMC papers**: 275
- **Why important**: SUPV3L1 has the strongest network position in the module and connects PHIP, ABCB7, and PRKDC. Its established annotation as a mitochondrial RNA helicase and component of the mitochondrial degradosome makes it a plausible central marker of mitochondrial RNA quality control. It also has a substantial literature footprint and disease-oriented links involving neurodegenerative disease.
- **Conclusion**: Established: SUPV3L1 is a mitochondrial RNA-processing and RNA-catabolic factor and is the most connected module member. Hypothesis: its central co-abundance position may indicate that mitochondrial RNA quality control is a major organizing feature of the module, but the network does not demonstrate direct physical coupling to its neighbors.

#### PRKDC

- **Related proteins** (co-abundance neighbors): SUPV3L1 (0.81), SEC24C (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: protein kinase, DNA-activated, catalytic subunit. This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to DNA-PKcs deficiency (0.752); neurodegenerative disease (0.548); severe combined immunodeficiency (0.470); combined immunodeficiency (0.464); ovarian neoplasm (0.210)
- **Europe PMC papers**: 12461
- **Why important**: PRKDC is a highly studied DNA-dependent protein kinase catalytic subunit with a major role in DNA double-strand break repair, recombination, telomere maintenance, and innate immune signaling. It connects SUPV3L1 to SEC24C and is one of the two module members in hu.MAP complex (hu.MAP huMAP3_09592.1). Its disease associations include DNA-PK deficiency and immunodeficiency, and it has the largest literature footprint in the module.
- **Conclusion**: Established: PRKDC is a core genome-integrity and DNA-repair factor, with limited complex-level support from (hu.MAP huMAP3_09592.1). Hypothesis: its co-abundance with mitochondrial and trafficking factors may reflect a shared stress-response or proliferation state rather than a direct PRKDC-centered complex.

#### PDS5B

- **Related proteins** (co-abundance neighbors): ATP2C1 (0.84), PHIP (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDS5 cohesin associated factor B. This gene encodes a protein that interacts with the conserved protein complex termed cohesin. The cohesin complex holds together sister chromatids and facilitates accurate chromosome segregation during mitosis and meiosis. This protein is also a negative regulator of cell proliferation and may be a tumor-suppressor gene. [provided by RefSeq, Jul 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.522); hypothyroidism (0.294); lysosomal storage disease (0.292); cervical carcinoma (0.287); smoking initiation (0.274)
- **Europe PMC papers**: 735
- **Why important**: PDS5B occupies a connecting position between PHIP and ATP2C1. It is an established cohesin-associated factor involved in sister-chromatid cohesion, homologous-recombination repair, and regulation of cell proliferation. Its tumor-suppressor and disease-related relevance, together with a substantial literature footprint, makes it important for interpreting the module's genome-maintenance and growth dimensions.
- **Conclusion**: Established: PDS5B supports chromosome maintenance, DNA repair, and control of proliferation. Hypothesis: its link to ATP2C1 may indicate coordinated regulation of proliferation with calcium-dependent cellular state, but no supplied interaction database establishes that mechanism.

#### PHIP

- **Related proteins** (co-abundance neighbors): PDS5B (0.83), SUPV3L1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PHIP subunit of CUL4-Ring ligase complex. This gene encodes a protein that binds to the insulin receptor substrate 1 protein and regulates glucose transporter translocation in skeletal muscle cells. The encoded protein may also regulate growth and survival of pancreatic beta cells. Elevated copy number of this gene may be associated with melanoma severity and the encoded protein may promote melanoma metastasis in human patients. [provided…
- **Diseases (Open Targets)**: PHIP-related behavioral problems-intellectual disability-obesity-dysmorphic features syndrome (0.805); Intellectual disability (0.544); hereditary disease (0.543); obesity due to melanocortin 4 receptor deficiency (0.383); obesity disorder (0.383)
- **Europe PMC papers**: 2064
- **Why important**: PHIP links PDS5B and SUPV3L1 and is therefore one of the module's internal connectors. Its annotations include participation in a CUL4-Ring ligase complex, regulation of protein phosphorylation, chromatin organization, transcription, proliferation, insulin-receptor signaling, and signal transduction. It also has the largest literature footprint after PRKDC and strong disease relevance involving intellectual disability, obesity, and melanoma-related biology.
- **Conclusion**: Established: PHIP is a multifunctional signaling, chromatin, and growth-regulatory protein with a central position in this module. Hypothesis: PHIP may couple a growth or metabolic state to mitochondrial and genome-maintenance programs, but the co-abundance data alone cannot identify the direction or molecular mechanism of that coupling.

#### ABCB7

- **Related proteins** (co-abundance neighbors): SUPV3L1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_09592.1
- **Function (MyGene.info)**: ATP binding cassette subfamily B member 7. The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily ar…
- **Diseases (Open Targets)**: X-linked sideroblastic anemia with ataxia (0.819); sideroblastic anemia (0.378); hereditary disease (0.340); spinocerebellar ataxia type 1 (0.333); mitochondrial disease (0.187)
- **Europe PMC papers**: 1100
- **Why important**: ABCB7 is a mitochondrial transporter involved in heme biosynthesis, iron handling, heme transport, and iron-sulfur cluster assembly. It connects directly to SUPV3L1 and is the other module member represented in hu.MAP complex (hu.MAP huMAP3_09592.1). Its disease associations with sideroblastic anemia and ataxia make it biologically informative for interpreting mitochondrial and hematologic aspects of the module.
- **Conclusion**: Established: ABCB7 provides a strong mitochondrial iron-sulfur and heme-homeostasis interpretation and has limited complex-level support through (hu.MAP huMAP3_09592.1). Hypothesis: its co-abundance with SUPV3L1 may reflect coordinated mitochondrial quality control, but the absence of STRING support prevents treating this as a known direct interaction.

## Module 1

**Tissue pair**: cell line and lung  
**Genes (5)**: APOC3, FBN1, HSPB6, IGHM, RBP4

### Function

The module appears to represent a mixed extracellular and tissue-state signal rather than a single, statistically established biochemical pathway. Its strongest coherent biological themes are circulating retinol and triglyceride-associated proteins, extracellular-matrix biology, and a B-cell immunoglobulin signal. RBP4 and APOC3 connect the module to hepatic retinol transport and triglyceride-rich lipoprotein metabolism, while FBN1 represents structural extracellular matrix and asprosin-related biology. HSPB6 is the principal network bridge, linking RBP4 and FBN1 and also connecting to IGHM. Its recorded functions include protein folding, stress response, apoptosis regulation, smooth-muscle relaxation, and angiogenesis. IGHM adds an immunoglobulin and B-cell component. No GO or KEGG term passed global correction, so no pathway-level enrichment can be presented as primary evidence. The functional interpretation therefore rests on the individual gene annotations, network arrangement, HPA profiles, supplementary STRING evidence (STRING Keyword Secreted; within-query FDR = 0.0105), and hu.MAP relationships (hu.MAP huMAP3_00178.1) through (hu.MAP huMAP3_09832.1).

**Cell composition.** The module is strongly biased toward secreted or blood-associated proteins according to the HPA summary. RBP4 and APOC3 are liver- and hepatocyte-enriched and are secreted to blood; FBN1 is secreted to blood and is associated with adipose tissue, placenta, fibroblasts, and hepatic stellate cells. IGHM is an immunoglobulin gene associated with B cells, plasma cells, and memory and naive B-cell populations. HSPB6 is annotated as intracellular and membrane-associated rather than secreted in its individual HPA entry, although the module-level HPA summary classifies all module genes as secreted genes. Four genes are not detected in immune cells, whereas IGHM has a B-cell-associated profile. The module is therefore not predominantly a broad blood-cell program, but IGHM could indicate a B-cell contribution or sample admixture. All module proteins were reported as not detected in lung by HPA, while the cell-line comparison had no matching HPA tissue. This makes a shared circulating-protein signal, extracellular carryover, or shared cellular composition plausible explanations for the cross-context co-abundance.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no high-confidence pairwise interactions among the module genes. The supplementary STRING keyword result for secreted proteins (STRING Keyword Secreted; within-query FDR = 0.0105) includes HSPB6, APOC3, FBN1, and RBP4, but it is not global multiple-testing evidence and should be interpreted descriptively. hu.MAP provides the clearest prior interaction context: APOC3 and RBP4 occur together in three complexes (hu.MAP huMAP3_00178.1), (hu.MAP huMAP3_08796.1), and (hu.MAP huMAP3_09832.1). Those complexes also contain proteins involved in plasma transport, complement, coagulation, and extracellular or acute-phase biology, including F2, PLG, CFB, C5, APCS, TTR, SERPINA6, and serum amyloid-associated proteins. HSPB6, IGHM, and FBN1 have no recorded hu.MAP membership in the supplied results. Thus, the module contains a known APOC3-RBP4 complex-associated core embedded in a broader co-abundance pattern, but the complete five-gene arrangement is not supported as a known physical complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Secreted (FDR = 0.0105, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00178.1 (APOC3, RBP4; 2/9); huMAP3_08796.1 (APOC3, RBP4; 2/15); huMAP3_09832.1 (APOC3, RBP4; 2/18)

### Novelty

The exact co-abundance module may be a potentially new cross-context association, because the supplied evidence does not identify a previously catalogued STRING network or hu.MAP complex containing all of its genes. However, it cannot be called a new biological complex or a definitive new pathway. APOC3-RBP4 relationships are already represented in hu.MAP (hu.MAP huMAP3_00178.1) through (hu.MAP huMAP3_09832.1), and several individual gene functions are well established. The absence of STRING edges or a matching hu.MAP complex is not proof of novelty. The defensible conclusion is that the module-level combination and its conservation between cell line and lung merit validation, while its biological components are largely established and heterogeneous.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of circulating or extracellular proteins together with a stress-responsive structural-cell signal, rather than a single intracellular pathway. A liver-derived RBP4-APOC3 component may mark retinoid and triglyceride-rich lipoprotein handling; FBN1 may report extracellular-matrix or stromal activity; HSPB6 may couple this extracellular or stromal state to cellular stress, survival, contractile, or angiogenic programs; and IGHM may reflect a localized or contaminating B-cell contribution. The conservation between cell line and lung could therefore arise from shared extracellular protein exposure, a common stromal-like state, or shared sample composition. This is a hypothesis, not a conclusion from GO or KEGG enrichment.

### Important genes

#### HSPB6

- **Related proteins** (co-abundance neighbors): IGHM (0.87), FBN1 (0.86), RBP4 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Mitochondria, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family B (small) member 6. This locus encodes a heat shock protein. The encoded protein likely plays a role in smooth muscle relaxation. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.102); neoplasm (0.089); breast cancer (0.085); bladder transitional cell carcinoma (0.077); prostate carcinoma (0.075)
- **Europe PMC papers**: 1062
- **Why important**: HSPB6 is the central network bridge, connecting to IGHM, FBN1, and RBP4, and its recorded network strength is the highest in the module. Its annotations support protein folding, heat response, anti-apoptotic activity, angiogenesis, and smooth-muscle relaxation. It also has the largest supplied literature volume among the module genes and has disease-area associations spanning several cancers. Its tissue and single-cell associations with muscle, fibroblasts, and hepatic stellate cells make it a plausible marker of a shared stromal or contractile-cell state.
- **Conclusion**: Established evidence supports HSPB6 as the module's network connector and a stress- and smooth-muscle-associated protein. It is a strong candidate for coordinating the module statistically, but the supplied data do not establish a direct physical interaction with the other genes or prove that HSPB6 drives the module.

#### RBP4

- **Related proteins** (co-abundance neighbors): APOC3 (0.86), HSPB6 (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_00178.1, huMAP3_08796.1, huMAP3_09832.1
- **Function (MyGene.info)**: retinol binding protein 4. This protein belongs to the lipocalin family and is the specific carrier for retinol (vitamin A alcohol) in the blood. It delivers retinol from the liver stores to the peripheral tissues. In plasma, the RBP-retinol complex interacts with transthyretin which prevents its loss by filtration through the kidney glomeruli. A deficiency of vitamin A blocks secretion of the binding protein posttranslatio…
- **Diseases (Open Targets)**: progressive retinal dystrophy due to retinol transport defect (0.696); microphthalmia, isolated, with coloboma 10 (0.643); microphthalmia, isolated, with coloboma (0.506); microphthalmia (0.501); inherited retinal dystrophy (0.421)
- **Europe PMC papers**: 18196
- **Why important**: RBP4 is liver- and hepatocyte-enriched, is secreted to blood, and is the specific carrier for retinol in the supplied annotation. It connects directly to APOC3 and HSPB6 and is present with APOC3 in all three reported hu.MAP complexes (hu.MAP huMAP3_00178.1) through (hu.MAP huMAP3_09832.1). Its extensive literature and strong associations with inherited retinal and retinol-transport disorders make it an informative functional anchor.
- **Conclusion**: Established evidence supports RBP4 as a circulating liver-derived retinol-transport component and as part of a known APOC3-associated complex context. Its role as a mechanistic bridge to HSPB6 is a hypothesis based on co-abundance, not a demonstrated molecular interaction.

#### APOC3

- **Related proteins** (co-abundance neighbors): RBP4 (0.86); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_00178.1, huMAP3_08796.1, huMAP3_09832.1
- **Function (MyGene.info)**: apolipoprotein C3. This gene encodes a protein component of triglyceride (TG)-rich lipoproteins (TRLs) including very low density lipoproteins (VLDL), high density lipoproteins (HDL) and chylomicrons. The encoded protein plays a role in role in the metabolism of these TRLs through multiple modes. This protein has been shown to promote the secretion of VLDL1, inhibit lipoprotein lipase enzyme activity, and delay cata…
- **Diseases (Open Targets)**: apolipoprotein c-III deficiency (0.610); hypertriglyceridemia (0.598); coronary artery disorder (0.573); familial lipoprotein lipase deficiency (0.531); Hypercholesterolemia (0.523)
- **Europe PMC papers**: 5854
- **Why important**: APOC3 is liver- and hepatocyte-enriched, secreted to blood, and annotated as a component and regulator of triglyceride-rich lipoprotein metabolism. It is directly connected to RBP4 and appears with RBP4 in the hu.MAP complexes (hu.MAP huMAP3_00178.1) through (hu.MAP huMAP3_09832.1). Its disease associations include hypertriglyceridemia, coronary artery disease, and disorders of lipoprotein-lipase function, giving it strong metabolic and clinical relevance.
- **Conclusion**: Established evidence supports APOC3 as a lipid-transport and triglyceride-remnant regulator that contributes to the known RBP4-associated complex context. The data support interpreting the APOC3-RBP4 pair as a metabolic submodule, but do not show that APOC3 directly organizes the full module.

#### FBN1

- **Related proteins** (co-abundance neighbors): HSPB6 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibrillin 1. This gene encodes a member of the fibrillin family of proteins. The encoded preproprotein is proteolytically processed to generate two proteins including the extracellular matrix component fibrillin-1 and the protein hormone asprosin. Fibrillin-1 is an extracellular matrix glycoprotein that serves as a structural component of calcium-binding microfibrils. These microfibrils provide force-bearing s…
- **Diseases (Open Targets)**: Marfan syndrome (0.892); ectopia lentis 1, isolated, autosomal dominant (0.811); Acromicric dysplasia (0.802); geleophysic dysplasia 2 (0.802); stiff skin syndrome (0.799)
- **Europe PMC papers**: 9216
- **Why important**: FBN1 is connected to the central HSPB6 node and contributes an extracellular-matrix dimension distinct from the hepatic lipid and retinol proteins. It is associated with adipose tissue, placenta, fibroblasts, and hepatic stellate cells, and its product provides structural support through calcium-binding microfibrils. The supplied annotation also records asprosin production and links to development, angiogenesis, glucose metabolism, and inflammatory response. Its disease associations, especially Marfan syndrome and related connective-tissue disorders, are well established.
- **Conclusion**: Established evidence supports FBN1 as an extracellular-matrix and connective-tissue marker. Its connection to HSPB6 may indicate a shared stromal or structural-cell state, but the co-abundance data do not establish a direct FBN1-HSPB6 mechanism.

#### IGHM

- **Related proteins** (co-abundance neighbors): HSPB6 (0.87); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: immunoglobulin heavy constant mu
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 3691
- **Why important**: IGHM is the only module gene with a clearly B-cell and plasma-cell-associated HPA profile and it is group-enriched in memory and naive B cells. It is connected to HSPB6 in the module, thereby providing a possible immune or sample-composition explanation for part of the pattern. Its immunoglobulin identity is established, although it has no supplied STRING or hu.MAP relationship to the other module members.
- **Conclusion**: Established evidence supports IGHM as a B-cell immunoglobulin marker rather than as part of the hepatic, lipoprotein, or extracellular-matrix machinery. Its presence may reflect a genuine B-cell component or sample admixture; distinguishing these possibilities requires cell-resolved or orthogonal validation.

## Module 2

**Tissue pair**: cell line and lung  
**Genes (11)**: BRIX1, CLTC, DYNC1H1, EIF4G1, NSF, EPRS1, IARS1, LARS1, RARS1, TEX10, SNRNP200

### Function

The module is best interpreted as a cytosolic translation-support module centered on aminoacyl-tRNA charging. The primary evidence is the convergence of (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.000109) through (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 0.00577), which identifies an aminoacyl-tRNA synthetase multienzyme complex, aminoacyl-tRNA ligase activity, tRNA aminoacylation, amino acid activation, and aminoacyl-tRNA biosynthesis through EPRS1, IARS1, LARS1, and RARS1. The adenyl-nucleotide binding terms (GO:MF ATP binding; q_global = 0.02) through (GO:MF adenyl nucleotide binding; q_global = 0.0376) are consistent with the ATP-dependent chemistry of these enzymes and with broader translation-related activity, but do not by themselves establish a separate pathway. The module has a coherent synthetase core and peripheral links to RNA processing, translation initiation, ribosome biogenesis, intracellular transport, and vesicle biology. The strongest interpretation is coordinated protein-biosynthetic capacity, with the non-core genes potentially reflecting coupling to RNA maturation and cellular logistics rather than a second independently established function.

**Cell composition.** The module is not composed of plasma or secreted proteins: HPA reports no secreted genes, and the listed proteins are intracellular, with cytosolic, nucleoplasmic, nucleolar, Golgi, endosomal, or lysosomal locations. HPA indicates generally low tissue specificity and low immune-cell specificity across the module, with no enriched blood-cell category. Therefore, the shared cell-line and lung signal is not most plausibly explained by a plasma-protein or blood-cell contamination pattern. Lung protein detection is present for most genes with available lung data, while RARS1 is not detected there and some genes have no lung data; this is compatible with a broadly used intracellular program but does not prove that every protein is active in the same lung cell. Cell-type-enhanced annotations occur for several genes, including epithelial, neuronal, reproductive, and neutrophil-associated categories, so cellular composition could contribute to individual edges, but the overall HPA profile favors a broadly expressed housekeeping-like translation and RNA-processing program.

**GO/KEGG enrichment**: 10 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 0.000109 | EPRS1, IARS1, LARS1, RARS1 |
| GO:MF aminoacyl-tRNA ligase activity | 0.00427 | EPRS1, IARS1, LARS1, RARS1 |
| GO:BP tRNA aminoacylation for protein translation | 0.00427 | EPRS1, IARS1, LARS1, RARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 0.00427 | EPRS1, IARS1, LARS1, RARS1 |
| GO:BP amino acid activation | 0.00577 | EPRS1, IARS1, LARS1, RARS1 |
| GO:BP tRNA aminoacylation | 0.00577 | EPRS1, IARS1, LARS1, RARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 0.00577 | EPRS1, IARS1, LARS1, RARS1 |
| GO:MF ATP binding | 0.02 | DYNC1H1, EIF4G1, EPRS1, IARS1, LARS1, NSF, RARS1, SNRNP200 |
| GO:MF adenyl ribonucleotide binding | 0.021 | DYNC1H1, EIF4G1, EPRS1, IARS1, LARS1, NSF, RARS1, SNRNP200 |
| GO:MF adenyl nucleotide binding | 0.0376 | DYNC1H1, EIF4G1, EPRS1, IARS1, LARS1, NSF, RARS1, SNRNP200 |

### STRING and hu.MAP

STRING strongly supports the four-member synthetase core: EPRS1, IARS1, LARS1, and RARS1 are mutually connected at very high confidence, and the supplementary STRING results (STRING Component aminoacyl-tRNA synthetase multienzyme complex; within-query FDR = 6.82e-05), (STRING COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex; within-query FDR = 0.0001), (STRING InterPro Aminoacyl-tRNA synthetase, class I, conserved site; within-query FDR = 0.00023), (STRING Keyword Aminoacyl-tRNA synthetase; within-query FDR = 0.00061), (STRING KEGG Aminoacyl-tRNA biosynthesis; within-query FDR = 0.0011), (STRING RCTM Cytosolic tRNA aminoacylation; within-query FDR = 0.0011), (STRING NetworkNeighborAL tRNA Aminoacylation; within-query FDR = 0.003), (STRING Function aminoacyl-tRNA ligase activity; within-query FDR = 0.0041), and (STRING InterPro Aminoacyl-tRNA synthetase, class Ia, anticodon-binding; within-query FDR = 0.0055) independently converge on the aminoacyl-tRNA synthetase complex and its conserved catalytic features. (STRING Keyword Protein biosynthesis; within-query FDR = 0.00049) and (STRING RCTM Translation; within-query FDR = 0.0028) extend the context toward protein biosynthesis and translation, while (STRING PMID (2023) A viral pan-end RNA element and host complex define a SARS-CoV-2 regulon.; within-query FDR = 0.0049) is a database association with a viral host complex and should not be treated as proof of the module's physiological role. hu.MAP provides orthogonal complex support through (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), where the same synthetase genes occur together with additional aminoacyl-tRNA synthetases, AIMP proteins, and related complex members. In contrast, SNRNP200, EIF4G1, DYNC1H1, BRIX1, TEX10, NSF, and CLTC lack reported STRING high-confidence partners or hu.MAP complexes within this evidence set, despite their co-abundance edges. This means the synthetase core is already a known molecular assembly, whereas several peripheral relationships are co-abundance observations with less direct physical-complex support.

**STRING interactions (score >= 0.7)**: 6 of 55 gene pairs: EPRS1–IARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–RARS1 (0.999); IARS1–LARS1 (0.999); IARS1–RARS1 (0.999); LARS1–RARS1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component aminoacyl-tRNA synthetase multienzyme complex (FDR = 6.82e-05, 4 genes); COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.0001, 4 genes); InterPro Aminoacyl-tRNA synthetase, class I, conserved site (FDR = 0.00023, 4 genes); Keyword Protein biosynthesis (FDR = 0.00049, 5 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 0.00061, 4 genes); TISSUES Gut (FDR = 0.00073, 4 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 0.0011, 4 genes); RCTM Cytosolic tRNA aminoacylation (FDR = 0.0011, 4 genes); RCTM Selenoamino acid metabolism (FDR = 0.0014, 4 genes); InterPro Rossmann-like alpha/beta/alpha sandwich fold (FDR = 0.0017, 4 genes); RCTM Translation (FDR = 0.0028, 5 genes); NetworkNeighborAL tRNA Aminoacylation (FDR = 0.003, 4 genes); Function aminoacyl-tRNA ligase activity (FDR = 0.0041, 4 genes); PMID (2023) A viral pan-end RNA element and host complex define a SARS-CoV-2 regulon. (FDR = 0.0049, 5 genes); InterPro Aminoacyl-tRNA synthetase, class Ia, anticodon-binding (FDR = 0.0055, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, IARS1, RARS1, LARS1; 4/14); huMAP3_13688.1 (EPRS1, IARS1, RARS1, LARS1; 4/14)

### Novelty

The module is not a wholly new molecular complex: the synthetase core is explicitly represented in STRING and hu.MAP through (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), and its function is supported by established annotations (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.000109) through (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 0.00577). The potentially novel aspect could instead be the reproducible co-abundance coupling of this known core to SNRNP200, EIF4G1, DYNC1H1, BRIX1, TEX10, NSF, or CLTC in the shared cell-line and lung context. However, absence of those peripheral relationships from STRING or hu.MAP does not establish novelty, because those resources emphasize curated or experimentally supported physical associations and may not capture context-specific co-abundance. Accordingly, this is best described as a context-specific module containing a known synthetase complex, with possible novel systems-level coupling that requires independent validation in additional cohorts, cell types, perturbations, or physical-interaction assays.

**Hypothesis.** Hypothesis: the shared module reflects coordinated maintenance of translational proteostasis in which the aminoacyl-tRNA synthetase core supplies charged tRNAs, while EIF4G1 supports translation initiation and SNRNP200 supports spliceosomal RNA processing. BRIX1 and TEX10 may link the program to ribosome biogenesis, whereas DYNC1H1, NSF, and CLTC may represent downstream demands for intracellular transport, receptor trafficking, or cell-state-specific protein handling. The observed co-abundance could therefore arise from a common transcriptional or translational-demand state rather than direct binding among every module member. This hypothesis predicts that perturbing the synthetase core or translational demand should alter coordinated expression or abundance of at least part of the peripheral RNA-processing and trafficking branch, but the fact sheet does not test that prediction.

### Important genes

#### EPRS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.86), RARS1 (0.81); STRING partners: IARS1 (0.999), LARS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is a member of the central synthetase core, connects to IARS1 and RARS1 in the module, and is present in both hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1) as well as the convergent primary terms (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.000109) through (GO:MF adenyl nucleotide binding; q_global = 0.0376). Its established function is multifunctional glutamyl- and prolyl-tRNA charging, with additional annotation for translation regulation and cellular response to insulin. It has a substantial literature base and disease associations involving hypomyelinating leukodystrophy and developmental phenotypes.
- **Conclusion**: Established evidence supports EPRS1 as a structural and catalytic component of the module's aminoacyl-tRNA synthetase core. Its co-abundance here is consistent with translational capacity and does not, by itself, establish a special lung-specific or disease-specific role.

#### RARS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.84), LARS1 (0.82), EPRS1 (0.81), BRIX1 (0.81), DYNC1H1 (0.80); STRING partners: EPRS1 (0.999), IARS1 (0.999), LARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 has one of the strongest network positions in the module and connects the synthetase core to peripheral genes including BRIX1 and DYNC1H1. It is present in both hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), participates in every primary enrichment entry (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.000109) through (GO:MF adenyl nucleotide binding; q_global = 0.0376), and has extensive STRING support with the other core synthetases. It encodes arginyl-tRNA synthetase, and its disease associations include hypomyelinating leukodystrophy and related neurological phenotypes.
- **Conclusion**: Established evidence identifies RARS1 as a core aminoacyl-tRNA charging enzyme and a network bridge. The peripheral links suggest a possible coordination point between translation and other cellular programs, but that bridging role remains a hypothesis rather than a demonstrated physical mechanism.

#### IARS1

- **Related proteins** (co-abundance neighbors): EPRS1 (0.86), RARS1 (0.84), SNRNP200 (0.82), EIF4G1 (0.81); STRING partners: EPRS1 (0.999), LARS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Isoleucine-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family and has been identified as a …
- **Diseases (Open Targets)**: growth retardation, intellectual developmental disorder, hypotonia, and hepatopathy (0.733); Abnormality of the skeletal system (0.332); microcephaly (0.289); Global developmental delay (0.289); Hallux valgus (0.184)
- **Europe PMC papers**: 184
- **Why important**: IARS1 is embedded in the same highly supported synthetase core, occurs in (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), and contributes to all primary synthetase and nucleotide-binding terms (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.000109) through (GO:MF adenyl nucleotide binding; q_global = 0.0376). Its network position links EPRS1 and RARS1 to SNRNP200 and EIF4G1, giving it a plausible interface between tRNA charging, RNA processing, and translation initiation. It encodes isoleucyl-tRNA synthetase, has an established role in translational fidelity, and is associated with developmental, skeletal, and autoimmune-related evidence in the supplied annotations.
- **Conclusion**: Established evidence supports IARS1 as a core enzyme with a possible network-bridging position. The proposed connection to spliceosome or initiation activity is inferred from co-abundance and topology, not proven direct interaction.

#### LARS1

- **Related proteins** (co-abundance neighbors): RARS1 (0.82), SNRNP200 (0.81); STRING partners: EPRS1 (0.999), IARS1 (0.999), RARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: leucyl-tRNA synthetase 1. This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals w…
- **Diseases (Open Targets)**: infantile liver failure syndrome 1 (0.670); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.510); Global developmental delay (0.119); sensorineural hearing loss disorder (0.119); Generalized-onset seizure (0.118)
- **Europe PMC papers**: 267
- **Why important**: LARS1 is part of the synthetase core supported by (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 0.000109) through (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 0.00577), (STRING Component aminoacyl-tRNA synthetase multienzyme complex; within-query FDR = 6.82e-05) through (STRING Keyword Aminoacyl-tRNA synthetase; within-query FDR = 0.00061), (STRING KEGG Aminoacyl-tRNA biosynthesis; within-query FDR = 0.0011) through (STRING Function aminoacyl-tRNA ligase activity; within-query FDR = 0.0041), and both hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). It catalyzes leucine-tRNA charging, interacts with RARS1 through its C-terminal domain according to the supplied annotation, and carries annotations for amino-acid sensing and response to amino-acid starvation. It has a substantial literature base and disease associations including infantile liver failure and developmental or neurological phenotypes.
- **Conclusion**: Established evidence supports LARS1 as both a catalytic core member and a plausible nutrient-responsive component of the module. A role in coupling amino-acid availability to the broader co-abundance state is biologically plausible, but is not demonstrated by this module alone.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): IARS1 (0.82), EIF4G1 (0.81), LARS1 (0.81), TEX10 (0.81), NSF (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 has a strong network position outside the synthetase clique and links IARS1 and LARS1 to EIF4G1, TEX10, and NSF. Its established function is as a U5 snRNP-specific RNA helicase and core spliceosomal component, while the module annotations connect it to adenyl-nucleotide binding (GO:MF ATP binding; q_global = 0.02) through (GO:MF adenyl nucleotide binding; q_global = 0.0376). HPA detects it in lung, and it has a substantial literature base with retinal degeneration associations.
- **Conclusion**: Established evidence supports SNRNP200 as an RNA-splicing factor that is co-abundant with the synthetase and translation-initiation program. Its position makes coordination between RNA maturation and protein synthesis a reasonable hypothesis, but the fact sheet does not establish direct binding to the synthetases.

## Module 3

**Tissue pair**: cell line and lung  
**Genes (9)**: CHD1, CHD4, DHX36, NOP56, RSL1D1, RRP12, PDCD11, UTP6, WDR3

### Function

The module is best interpreted as a nucleolar ribosome-biogenesis and RNA-processing module, with a particularly strong association with the small-subunit processome and preribosome. The primary evidence is the enrichment of the small-subunit processome (GO:CC small-subunit processome; q_global = 0.00128), preribosome (GO:CC preribosome; q_global = 0.00619), the Pwp2p-containing preribosome subcomplex (GO:CC Pwp2p-containing subcomplex of 90S preribosome; q_global = 0.0121), and snoRNA binding (GO:MF snoRNA binding; q_global = 0.0191). NOP56, PDCD11, UTP6, and WDR3 provide the clearest core of this interpretation. NOP56, PDCD11, RRP12, RSL1D1, UTP6, and WDR3 also have annotations or supplementary network support for rRNA processing (5 supplementary STRING terms; within-query FDR 3.26e-07–6.38e-05), (9 supplementary STRING terms; within-query FDR 6.38e-05–0.0032). The nucleic-acid-binding enrichment (GO:MF nucleic acid binding; q_global = 0.00941) is broad but consistent with this RNA-centered function. CHD1, CHD4, and DHX36 account for the globally supported helicase terms (6 globally significant GO/KEGG terms, q_global 0.0244–0.0448; see the table), suggesting a linked nucleic-acid remodeling component. The data therefore support a composite module involving preribosome assembly and rRNA maturation, with possible coupling to chromatin or structured-nucleic-acid remodeling.

**Cell composition.** This does not resemble a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly nuclear or nucleolar. Most genes have low tissue specificity, which is compatible with broadly expressed housekeeping biology rather than a lung-specific program. HPA nevertheless identifies cell-type-enhanced patterns for many genes, including monocytes, neutrophils, glial populations, and germ-cell populations. RRP12 is group-enriched in bone marrow and skeletal muscle and is immune-cell enhanced in neutrophil lineages. Because the module is shared by cell line and lung, its recurrence may reflect a conserved core cellular process, shared proliferative or biosynthetic state, or shared cell types rather than a specialized lung function. The HPA protein observations in lung are consistent with expression of much of the module there, while the cell-line protein evidence is not informative.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC small-subunit processome | 0.00128 | NOP56, PDCD11, UTP6, WDR3 |
| GO:CC preribosome | 0.00619 | NOP56, PDCD11, UTP6, WDR3 |
| GO:MF nucleic acid binding | 0.00941 | CHD1, CHD4, DHX36, NOP56, PDCD11, RRP12, RSL1D1, UTP6, WDR3 |
| GO:CC Pwp2p-containing subcomplex of 90S preribosome | 0.0121 | UTP6, WDR3 |
| GO:MF snoRNA binding | 0.0191 | NOP56, UTP6, WDR3 |
| GO:MF four-way junction helicase activity | 0.0244 | CHD1, CHD4, DHX36 |
| GO:MF forked DNA-dependent helicase activity | 0.0244 | CHD1, CHD4, DHX36 |
| GO:MF double-stranded DNA helicase activity | 0.0273 | CHD1, CHD4, DHX36 |
| GO:MF 3'-5' DNA helicase activity | 0.0273 | CHD1, CHD4, DHX36 |
| GO:MF single-stranded 3'-5' DNA helicase activity | 0.0273 | CHD1, CHD4, DHX36 |
| GO:MF single-stranded DNA helicase activity | 0.0448 | CHD1, CHD4, DHX36 |

### STRING and hu.MAP

STRING shows a coherent, highly connected known-interaction neighborhood among NOP56, PDCD11, RRP12, RSL1D1, UTP6, and WDR3. The strongest connectivity is concentrated among the preribosome and small-subunit-processome genes, and the STRING functional results independently point to preribosome, small-subunit processome, nucleolar localization, and rRNA processing (15 supplementary STRING terms; within-query FDR 3.26e-07–0.0032). These results support the interpretation that much of the module recapitulates an established ribosome-biogenesis machinery rather than an arbitrary correlation. STRING does not provide listed interactions for CHD1, CHD4, or DHX36 within this set, so their co-abundance links should not be treated as established physical interactions. hu.MAP supplies one partial complex connection, containing CHD1 and RRP12 (hu.MAP huMAP3_01045.1), but the other listed members of that complex are outside the module. Thus, the module combines a well-known nucleolar interaction core with a less well-established helicase or chromatin-associated extension.

**STRING interactions (score >= 0.7)**: 15 of 36 gene pairs: NOP56–PDCD11 (0.997); NOP56–RRP12 (0.938); NOP56–RSL1D1 (0.991); NOP56–UTP6 (0.998); NOP56–WDR3 (0.999); PDCD11–RRP12 (0.984); PDCD11–RSL1D1 (0.978); PDCD11–UTP6 (0.994); PDCD11–WDR3 (0.997); RRP12–RSL1D1 (0.97); RRP12–UTP6 (0.742); RRP12–WDR3 (0.878); RSL1D1–UTP6 (0.993); RSL1D1–WDR3 (0.993); UTP6–WDR3 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 3.26e-07, 7 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 3.16e-06, 6 genes); COMPARTMENTS Preribosome (FDR = 3.45e-05, 5 genes); Component Preribosome (FDR = 3.47e-05, 5 genes); COMPARTMENTS 90S preribosome (FDR = 6.38e-05, 4 genes); COMPARTMENTS Nuclear lumen (FDR = 6.38e-05, 9 genes); COMPARTMENTS Small-subunit processome (FDR = 6.38e-05, 4 genes); PMID (2016) Stepwise and dynamic assembly of the earliest precursors of small ribosomal subunits in yeast. (FDR = 6.43e-05, 6 genes); Component Small-subunit processome (FDR = 0.00014, 4 genes); Process rRNA processing (FDR = 0.00028, 6 genes); RCTM rRNA modification in the nucleus and cytosol (FDR = 0.00097, 4 genes); NetworkNeighborAL Small-subunit processome, and Positive regulation of rRNA processing (FDR = 0.0012, 3 genes); PMID (2018) The SSU processome interactome in Saccharomyces cerevisiae reveals novel protein subcomplexes. (FDR = 0.0018, 5 genes); COMPARTMENTS Nucleolus (FDR = 0.0022, 6 genes); Component 90S preribosome (FDR = 0.0032, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01045.1 (CHD1, RRP12; 2/5)

### Novelty

The biological function is not a new discovery: preribosome assembly, rRNA processing, snoRNA-associated activity, and the roles of NOP56, PDCD11, UTP6, and WDR3 are already established and are supported by STRING and the supplied gene annotations. The potentially new aspect is the reproducible co-abundance organization of this particular set across cell line and lung, especially the association of the nucleolar core with CHD1, CHD4, and DHX36. However, the fact sheet does not establish that this exact module is absent from prior co-expression studies, and absence of a STRING or hu.MAP edge cannot demonstrate novelty. The defensible conclusion is therefore that this is a potentially novel cross-context module configuration built around a known ribosome-biogenesis program, not a newly discovered molecular pathway.

**Hypothesis.** Hypothesis: the module represents a conserved biosynthetic-state program in which a nucleolar preribosome and small-subunit-processome core coordinates with nucleic-acid remodeling factors. In this model, NOP56, PDCD11, UTP6, and WDR3 organize or process pre-rRNA and snoRNA-associated intermediates; RRP12 and RSL1D1 support maturation, transport, or quality control of ribosome-related particles; and CHD1, CHD4, and DHX36 provide a linked capacity for chromatin or structured-nucleic-acid remodeling. The co-abundance signal could therefore report coordinated demand for ribosome production and genome or RNA remodeling, rather than a stable physical complex containing all module members. This model requires experimental testing by perturbation, localization, and interaction assays.

### Important genes

#### NOP56

- **Related proteins** (co-abundance neighbors): PDCD11 (0.88), WDR3 (0.85), CHD1 (0.83), RSL1D1 (0.81); STRING partners: PDCD11 (0.997), RRP12 (0.938), RSL1D1 (0.991), UTP6 (0.998), WDR3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP56 ribonucleoprotein. Nop56p is a yeast nucleolar protein that is part of a complex with the nucleolar proteins Nop58p and fibrillarin. Nop56p is required for assembly of the 60S ribosomal subunit and is involved in pre-rRNA processing. The protein encoded by this gene is similar in sequence to Nop56p and is also found in the nucleolus. Expansion of a GGCCTG repeat from 3-8 copies to 1500-2500 copies in an intron of th…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 36 (0.586); neurodegenerative disease (0.495); ovarian neoplasm (0.272); hereditary disease (0.193); cerebellar ataxia (0.121)
- **Europe PMC papers**: 1517
- **Why important**: NOP56 is a central network hub, connected to several members of the module, including the principal preribosome-associated genes. It is localized to the nucleolar fibrillar center and is annotated for rRNA processing, rRNA modification, and small-subunit biogenesis. It participates in the strongest primary enrichments (GO:CC small-subunit processome; q_global = 0.00128), (GO:CC preribosome; q_global = 0.00619), and (GO:MF snoRNA binding; q_global = 0.0191) and in extensive supplementary STRING support. Its association with spinocerebellar ataxia type thirty-six and its large literature base make it both mechanistically and disease-relevant.
- **Conclusion**: Established: NOP56 is a key nucleolar rRNA-processing component and a strong anchor of the module. Hypothesis: its central co-abundance position may make it a principal indicator of coordinated preribosome activity in both contexts.

#### UTP6

- **Related proteins** (co-abundance neighbors): CHD1 (0.81); STRING partners: NOP56 (0.998), PDCD11 (0.994), RRP12 (0.742), RSL1D1 (0.993), WDR3 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UTP6 small subunit processome component. Predicted to enable snoRNA binding activity. Predicted to be involved in maturation of SSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: post-traumatic stress disorder (0.069); colorectal carcinoma (0.067); type 1 diabetes mellitus (0.057); ovarian neoplasm (0.057); prostate carcinoma (0.040)
- **Europe PMC papers**: 283
- **Why important**: UTP6 is a nucleolar small-subunit-processome component with snoRNA-binding and pre-rRNA maturation annotations. It contributes to the primary small-subunit processome, preribosome, Pwp2p-containing subcomplex, and snoRNA-binding enrichments (GO:CC small-subunit processome; q_global = 0.00128), (GO:CC preribosome; q_global = 0.00619), (GO:CC Pwp2p-containing subcomplex of 90S preribosome; q_global = 0.0121), and (GO:MF snoRNA binding; q_global = 0.0191). Its very strong STRING relationships with the nucleolar core make it one of the clearest molecular markers of the module's central function.
- **Conclusion**: Established: UTP6 supports small-subunit processome assembly and pre-rRNA maturation. Hypothesis: its co-abundance with the helicase-associated part of the module may reflect coordination between ribosome assembly and broader nucleic-acid remodeling.

#### WDR3

- **Related proteins** (co-abundance neighbors): NOP56 (0.85), DHX36 (0.82); STRING partners: NOP56 (0.999), PDCD11 (0.997), RRP12 (0.878), RSL1D1 (0.993), UTP6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 3. This gene encodes a nuclear protein containing 10 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, which usually include a trp-asp at the C-terminal end. Proteins belonging to the WD repeat family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. [provid…
- **Diseases (Open Targets)**: presbycusis (0.335); respiratory tract infectious disorder (0.184); neurodegenerative disease (0.143); preeclampsia (0.120); alcohol drinking (0.098)
- **Europe PMC papers**: 280
- **Why important**: WDR3 is a nucleolar WD-repeat protein annotated for small-subunit rRNA maturation and ribosome biogenesis. It participates in all of the principal processome and preribosome enrichments involving the nucleolar core (GO:CC small-subunit processome; q_global = 0.00128), (GO:CC preribosome; q_global = 0.00619), (GO:CC Pwp2p-containing subcomplex of 90S preribosome; q_global = 0.0121), and (GO:MF snoRNA binding; q_global = 0.0191), and has strong STRING relationships with that core. Its position links NOP56 and DHX36 in the module, making it a plausible bridge between the established nucleolar machinery and the less-characterized extension.
- **Conclusion**: Established: WDR3 is a core nucleolar ribosome-biogenesis-associated member. Hypothesis: WDR3 may be one of the organizational points through which the module's rRNA-processing and nucleic-acid-remodeling signals become co-abundant.

#### RRP12

- **Related proteins** (co-abundance neighbors): CHD4 (0.81), PDCD11 (0.81), RSL1D1 (0.80); STRING partners: NOP56 (0.938), PDCD11 (0.984), RSL1D1 (0.97), UTP6 (0.742), WDR3 (0.878)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: huMAP3_01045.1
- **Function (MyGene.info)**: ribosomal RNA processing 12 homolog. Enables RNA binding activity. Predicted to be involved in rRNA processing. Located in cytosol; nucleolus; and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.435); bilateral striopallidodentate calcinosis (0.370); colorectal carcinoma (0.079); hepatocellular carcinoma (0.075); neoplasm (0.067)
- **Europe PMC papers**: 367
- **Why important**: RRP12 occupies an intermediate network position and connects to several members of the nucleolar core. It is annotated for RNA binding and rRNA processing, is supported by the STRING preribosome and rRNA-processing results (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 3.26e-07), (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 3.16e-06), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 6.38e-05), (STRING PMID (2016) Stepwise and dynamic assembly of the earliest precursors of small ribosomal subunits in yeast.; within-query FDR = 6.43e-05), (STRING Process rRNA processing; within-query FDR = 0.00028), and (STRING COMPARTMENTS Nucleolus; within-query FDR = 0.0022), and is the module member represented in the partial hu.MAP complex with CHD1 (hu.MAP huMAP3_01045.1). Its bone-marrow and neutrophil-associated HPA pattern is also relevant to interpreting possible cell-type contributions.
- **Conclusion**: Established: RRP12 connects the ribosome-biogenesis interpretation to a documented complex association and to cell-type-enriched expression patterns. Hypothesis: it may help couple nucleolar maturation with the chromatin-associated arm represented by CHD1.

#### CHD4

- **Related proteins** (co-abundance neighbors): PDCD11 (0.81), RRP12 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromodomain helicase DNA binding protein 4. The product of this gene belongs to the SNF2/RAD54 helicase family. It represents the main component of the nucleosome remodeling and deacetylase complex and plays an important role in epigenetic transcriptional repression. Patients with dermatomyositis develop antibodies against this protein. Somatic mutations in this gene are associated with serous endometrial tumors. Alternative splicing result…
- **Diseases (Open Targets)**: Sifrim-Hitz-Weiss syndrome (0.810); neurodegenerative disease (0.551); hereditary disease (0.505); endometrial cancer (0.470); uterine carcinosarcoma (0.439)
- **Europe PMC papers**: 3617
- **Why important**: CHD4 contributes to the globally supported helicase terms (GO:MF nucleic acid binding; q_global = 0.00941) and (6 globally significant GO/KEGG terms, q_global 0.0244–0.0448; see the table) and is annotated as a major component of the nucleosome-remodeling and deacetylase complex, with roles in chromatin remodeling, transcriptional repression, and DNA repair. It is highly studied and has disease associations including Sifrim-Hitz-Weiss syndrome and endometrial cancer. Its module links are to PDCD11 and RRP12, but STRING lists no direct interaction with the other module members.
- **Conclusion**: Established: CHD4 supplies a chromatin-remodeling and helicase-related component distinct from the nucleolar core. Hypothesis: its co-abundance may indicate coordinated regulation of chromatin accessibility during states requiring elevated ribosome biogenesis, not necessarily direct incorporation into the preribosome.

#### DHX36

- **Related proteins** (co-abundance neighbors): WDR3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAH-box helicase 36. This gene is a member of the DEAH-box family of RNA-dependent NTPases which are named after the conserved amino acid sequence Asp-Glu-Ala-His in motif II. The protein encoded by this gene has been shown to enhance the deadenylation and decay of mRNAs with 3'-UTR AU-rich elements (ARE-mRNA). The protein has also been shown to resolve into single strands the highly stable tetramolecular DNA configur…
- **Diseases (Open Targets)**: neurodegenerative disease (0.522); Abnormality of the skeletal system (0.517); Epiretinal membrane (0.388); degeneration of macula and posterior pole (0.383); retinal disorder (0.372)
- **Europe PMC papers**: 1293
- **Why important**: DHX36 is connected to WDR3 and contributes to the globally supported helicase enrichments (GO:MF nucleic acid binding; q_global = 0.00941) and (6 globally significant GO/KEGG terms, q_global 0.0244–0.0448; see the table). Its supplied annotation describes resolution of guanine-rich four-stranded DNA structures and roles in RNA metabolism, transcription, translation regulation, and spermatogenesis. It has a substantial literature base and disease associations involving neurodegenerative, skeletal, and retinal disorders, while lacking a listed STRING interaction with the module.
- **Conclusion**: Established: DHX36 is a nucleic-acid helicase with functions compatible with structured RNA and DNA remodeling. Hypothesis: its association with WDR3 may represent a functional or regulatory extension of the nucleolar program, but the current evidence does not establish a direct preribosome role.
