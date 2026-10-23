# Conserved co-abundance modules: autonomic_nervous_system and bone_marrow

## Module 0

**Tissue pair**: autonomic_nervous_system and bone_marrow  
**Genes (24)**: APP, RNF40, CBR3, CCDC117, CMBL, CNOT12, CIT, DPYSL2, EIPR1, ERGIC2, ESS2, MASTL, H2AC21, PRKCI, L2HGDH, LRRFIP2, OGFOD1, RAB22A, TACC3, UQCRFS1, PPIP5K2, ZCCHC3, ZDHHC5, ZWILCH

### Function

No GO or KEGG term passed global correction, so there is no statistically supported module-level pathway annotation from those analyses. The genes instead suggest a mixed cellular program involving intracellular trafficking and membrane organization, cell-cycle and cytokinesis machinery, mitochondrial respiration, cytoskeletal regulation, and selected innate-immune signaling functions. CIT, MASTL, TACC3, ZWILCH, and H2AC21 support a proliferation, chromosome-segregation, or cytokinesis component. RAB22A, ERGIC2, APP, ZDHHC5, EIPR1, and PRKCI support endosomal, Golgi, recycling, or plasma-membrane trafficking. UQCRFS1 and L2HGDH support mitochondrial energy metabolism. ZCCHC3 and LRRFIP2 provide links to antiviral or innate-immune regulation. The supplementary STRING kinase term (STRING SMART Extension to Ser/Thr-type protein kinases; within-query FDR = 0.0406) is consistent with PRKCI, MASTL, and CIT, but it is not global enrichment. Overall, the module is better interpreted as a shared cellular-state or cell-composition signal than as a single established biochemical pathway.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: only APP is annotated as secreted to blood, while the remainder are intracellular or membrane-associated proteins. The HPA profile is mixed, with many genes showing low tissue specificity and many showing cell-type enhancement rather than a uniform tissue-restricted pattern. Brain, kidney, skeletal muscle, lymphoid tissue, and bone marrow occur among the recurrent enriched tissues, and spermatocyte or spermatid, epithelial, neutrophil-progenitor, and epicardial cell annotations are also represented. Most genes have low immune-cell specificity, although selected genes show immune-cell enhancement or enrichment, including APP and DPYSL2-related myeloid annotations. Bone-marrow protein detection is present for many genes, whereas there is no matching autonomic-nervous-system HPA tissue assay. These observations make shared cell types, proliferative cells, or sample-composition effects plausible contributors to the conserved co-abundance pattern. They do not establish that the module is a blood-cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

At the stated high-confidence STRING threshold, none of the possible within-module gene pairs had a reported interaction, and no hu.MAP complex contained multiple module members. Thus the co-abundance edges are not recapitulated as established physical interactions or a recognized multiprotein complex. The only STRING functional signal is the supplementary serine/threonine-kinase annotation (STRING SMART Extension to Ser/Thr-type protein kinases; within-query FDR = 0.0406), containing PRKCI, MASTL, and CIT. This provides limited support for a kinase-related substructure, but the STRING result is not corrected across modules and cannot substitute for globally significant GO or KEGG enrichment. The absence of STRING and hu.MAP support argues against interpreting the entire module as one known physical complex; it is compatible with coordinated expression of proteins from different cellular systems.

**STRING interactions (score >= 0.7)**: 0 of 276 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Extension to Ser/Thr-type protein kinases (FDR = 0.0406, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The conserved co-abundance module may be a new observation in this tissue-pair analysis, because its particular combination of genes is not represented by a reported high-confidence STRING interaction network or a shared hu.MAP complex. However, the biological functions represented by its genes are not new: vesicle trafficking, cytokinesis, mitochondrial respiration, palmitoylation, innate-immune signaling, and neuronal or cytoskeletal biology are established functions in the fact sheet. Therefore the defensible claim is novelty of the cross-tissue co-abundance pattern or its particular gene combination, not discovery of a new molecular pathway. Lack of STRING or hu.MAP representation alone cannot prove novelty, and the absence of globally significant enrichment further limits mechanistic claims.

**Hypothesis.** Hypothesis: the module reflects a shared abundance state involving proliferative or progenitor-like cells together with coordinated intracellular membrane trafficking and mitochondrial support. In bone marrow, the signal could be contributed by progenitor or other actively cycling cells, consistent with H2AC21, TACC3, MASTL, and CIT annotations and with bone-marrow detection. In autonomic nervous system samples, broadly expressed trafficking, cytoskeletal, mitochondrial, and neuronal-associated proteins could generate a related abundance pattern. A possible mechanistic bridge is that kinase and palmitoylation activities regulate membrane or cytoskeletal organization while mitochondrial respiration supports the energetic demands of cell growth and trafficking. This remains a hypothesis: the lack of globally significant GO or KEGG terms, the absence of high-confidence STRING links, and the mixed HPA composition require validation with cell-resolved data, independent cohorts, and protein or functional assays.

### Important genes

#### CIT

- **Related proteins** (co-abundance neighbors): PRKCI (0.94), UQCRFS1 (0.83), MASTL (0.82), CCDC117 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citron rho-interacting serine/threonine kinase. This gene encodes a serine/threonine-protein kinase that functions in cell division. Together with the kinesin KIF14, this protein localizes to the central spindle and midbody, and functions to promote efficient cytokinesis. This protein is involved in central nervous system development. Polymorphisms in this gene are associated with bipolar disorder and risk for schizophrenia. Alternative splicin…
- **Diseases (Open Targets)**: autosomal recessive primary microcephaly (0.773); neurodegenerative disease (0.554); hereditary disease (0.472); Primary microcephaly (0.464); atrial fibrillation (0.286)
- **Europe PMC papers**: 16815
- **Why important**: CIT is a central network connector in the module and links PRKCI, UQCRFS1, MASTL, and CCDC117. Its established function in central-spindle organization and cytokinesis provides a biologically coherent cell-division anchor. It is also one of the genes in the supplementary kinase-related STRING term (STRING SMART Extension to Ser/Thr-type protein kinases; within-query FDR = 0.0406), has brain and lymphoid tissue enhancement, and has extensive literature and disease-association coverage, including neurodevelopmental and psychiatric associations.
- **Conclusion**: Established evidence supports CIT as an important cytokinesis and nervous-system development gene and as a network hub in this module. It is a plausible marker of a proliferative or cytoskeletal substate, but the module data do not prove that CIT drives the co-abundance pattern or that cytokinesis is the module's sole function.

#### UQCRFS1

- **Related proteins** (co-abundance neighbors): ZDHHC5 (0.95), CNOT12 (0.86), CIT (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase, Rieske iron-sulfur polypeptide 1. Predicted to enable oxidoreductase activity. Involved in mitochondrial respiratory chain complex III assembly and respiratory electron transport chain. Located in mitochondrion. Part of mitochondrial respiratory chain complex III and mitochondrial respiratory chain complex IV. Implicated in mitochondrial complex III deficiency. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: mitochondrial complex III deficiency, nuclear type 10 (0.745); neurodegenerative disease (0.484); cardiomyopathy (0.427); lactic acidosis (0.426); propionic acidemia (0.425)
- **Europe PMC papers**: 1748
- **Why important**: UQCRFS1 is among the stronger module connectors and links the CIT-centered region to ZDHHC5 and CNOT12. Its established role in respiratory-chain complex assembly and electron transport gives the module a defined mitochondrial component. It is tissue enhanced in skeletal muscle and tongue and is detected in bone marrow, while its disease associations include mitochondrial complex deficiency and cardiomyopathy.
- **Conclusion**: Established evidence supports UQCRFS1 as a mitochondrial respiratory-chain gene that may report energetic or biosynthetic state. Its module association is consistent with metabolic support for trafficking or proliferation, but a direct functional connection to the other module genes remains unproven.

#### ZDHHC5

- **Related proteins** (co-abundance neighbors): UQCRFS1 (0.95), CMBL (0.88), L2HGDH (0.86), EIPR1 (0.84), DPYSL2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zDHHC palmitoyltransferase 5. Enables palmitoyltransferase activity. Involved in positive regulation of pattern recognition receptor signaling pathway and positive regulation of protein localization to plasma membrane. Acts upstream of or within protein palmitoylation. Located in phagocytic vesicle and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: COVID-19 (0.372); tricuspid valve disorder (0.311); major depressive disorder (0.119); schizophrenia (0.094); mathematical ability (0.088)
- **Europe PMC papers**: 654
- **Why important**: ZDHHC5 has the strongest network connectivity in the supplied subgraph and connects proteins involved in mitochondrial metabolism, vesicle or endosomal transport, and cytoskeletal biology. Its established zDHHC palmitoyltransferase activity, plasma-membrane and phagocytic-vesicle localization, and roles in receptor signaling and protein localization make it a plausible membrane-regulatory node. It also has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports ZDHHC5 as a membrane-protein palmitoylation and trafficking regulator. Its network position makes it a strong candidate for linking the module's membrane and signaling components, but the co-abundance data do not demonstrate that its enzymatic activity coordinates the whole module.

#### RAB22A

- **Related proteins** (co-abundance neighbors): ZCCHC3 (0.89), OGFOD1 (0.87), ERGIC2 (0.85), APP (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB22A, member RAS oncogene family. The protein encoded by this gene is a member of the RAB family of small GTPases. The GTP-bound form of the encoded protein has been shown to interact with early-endosomal antigen 1, and may be involved in the trafficking of and interaction between endosomal compartments. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: alcohol drinking (0.273); urolithiasis (0.172); osteosarcoma (0.096); breast cancer (0.084); colorectal carcinoma (0.083)
- **Europe PMC papers**: 1119
- **Why important**: RAB22A is a network connector joining ZCCHC3, OGFOD1, ERGIC2, and APP. Its established small-GTPase functions in endosomal organization, intracellular transport, and vesicle-size regulation provide the clearest trafficking-centered interpretation of this branch. It has broad tissue specificity, vesicular and Golgi localization, and a substantial literature base.
- **Conclusion**: Established evidence supports RAB22A as an endosomal-trafficking component and makes it a useful indicator of vesicle biology in the module. Its position suggests coordination of trafficking-related abundance, but it is not evidence of a novel RAB22A-containing complex because STRING and hu.MAP provide no such support here.

#### MASTL

- **Related proteins** (co-abundance neighbors): PPIP5K2 (0.91), ZWILCH (0.89), CIT (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: microtubule associated serine/threonine kinase like. This gene encodes a microtubule-associated serine/threonine kinase. Mutations at this locus have been associated with autosomal dominant thrombocytopenia, also known as thrombocytopenia-2. Alternatively spliced transcript variants have been described for this locus. [provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.539); Alzheimer disease (0.515); Parkinson disease (0.503); lysosomal storage disease (0.503); autosomal thrombocytopenia with normal platelets (0.370)
- **Europe PMC papers**: 591
- **Why important**: MASTL connects PPIP5K2, ZWILCH, and CIT and is included in the supplementary serine/threonine-kinase STRING term (STRING SMART Extension to Ser/Thr-type protein kinases; within-query FDR = 0.0406). Its established functions in mitotic-cell-cycle regulation and its association with thrombocytopenia are especially relevant to a module observed in a bone-marrow comparison. It also has disease associations spanning thrombocytopenia and neurodegenerative conditions.
- **Conclusion**: Established evidence supports MASTL as a mitotic-cell-cycle regulator with relevance to platelet-related disease. It is a plausible indicator of proliferative or hematopoietic-state biology in the module, but the available evidence does not show that MASTL mechanistically links the bone-marrow and autonomic-nervous-system signals.

## Module 1

**Tissue pair**: autonomic_nervous_system and bone_marrow  
**Genes (40)**: SLC1A5, AKAP8L, ARIH1, ACTR8, CCNB1, CERT1, CLASP1, COPS8, DDX5, DNMT1, GAPVD1, TUBGCP2, RAP1GDS1, GNPNAT1, CPOX, HIRIP3, IDE, EIF4G3, LBR, NAA15, NAGK, NEMF, NFU1, NRDC, NUP160, PNPT1, PRRC2B, CHML, ARHGAP17, RPL6, RUFY1, SEC23A, SCAF8, IARS2, GTF3C5, TMEM87B, TNIK, UTP20, WDR12, CSE1L

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. Therefore, the module does not support a statistically established single pathway-level function. Its gene annotations instead indicate a heterogeneous cellular maintenance program involving ribosome biogenesis and translation, RNA processing and quality control, chromatin and transcriptional regulation, intracellular trafficking, mitochondrial RNA and protein maintenance, cytoskeletal organization, and cell-cycle activity. The network is relatively sparse and is organized around a highly connected ACTR8-centered neighborhood, with additional links involving CHML, DNMT1, RPL6, WDR12, UTP20, and NEMF. The most defensible interpretation is a shared abundance state of broadly required cellular machinery rather than a coherent tissue-specific pathway. The functional interpretation remains provisional because the absence of globally significant enrichment does not invalidate the module.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only IDE as secreted in other tissues. Most genes have low tissue specificity, and most have low immune-cell specificity. The module therefore resembles a broadly expressed housekeeping-type program more than a specialized autonomic nervous system or bone-marrow program. Nevertheless, HPA shows recurring associations with erythrocyte progenitors, neutrophils, megakaryocyte-lineage cells, and other progenitor populations, while bone-marrow protein detection is common for many members. This raises the possibility that the shared module partly reflects common proliferative or biosynthetic cell states, or shared blood and progenitor-cell content in the samples, rather than a unique biological program conserved between the tissues. The autonomic nervous system protein comparison is uninformative because no matching HPA tissue was available.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strong STRING evidence is limited to a few relationships: GNPNAT1 with NAGK, NEMF with RPL6, RPL6 with WDR12, and UTP20 with WDR12. These links support established connections involving amino-sugar metabolism, ribosome-associated quality control, and ribosome biogenesis, but they do not define the whole module. No STRING functional enrichment was reported. hu.MAP provides additional complex-level support: NEMF and SCAF8 co-occur in the complexes represented by (hu.MAP huMAP3_11021.1) and (hu.MAP huMAP3_10359.1); NEMF and DDX5 co-occur in (hu.MAP huMAP3_10631.1) and (hu.MAP huMAP3_11111.1); CLASP1 and CERT1 co-occur in (hu.MAP huMAP3_10808.1); UTP20 and NUP160 co-occur in (hu.MAP huMAP3_11232.1); and PNPT1 and IARS2 co-occur in (hu.MAP huMAP3_13468.1). Because each complex contains only a small subset of module members, these results indicate that some module genes participate in known multiprotein systems, while also showing that the module is not itself a single established complex. The concordance between co-abundance and selected known interactions is compatible with a real shared cellular state, but the sparse connectivity and broad functional diversity argue against treating every co-abundance edge as a direct physical interaction.

**STRING interactions (score >= 0.7)**: 4 of 780 gene pairs: GNPNAT1–NAGK (0.98); NEMF–RPL6 (0.81); RPL6–WDR12 (0.945); UTP20–WDR12 (0.848)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11021.1 (NEMF, SCAF8; 2/18); huMAP3_10359.1 (NEMF, SCAF8; 2/27); huMAP3_10631.1 (NEMF, DDX5; 2/28); huMAP3_11111.1 (NEMF, DDX5; 2/29); huMAP3_10808.1 (CLASP1, CERT1; 2/54); huMAP3_11232.1 (UTP20, NUP160; 2/78); huMAP3_13468.1 (PNPT1, IARS2; 2/99)

### Novelty

The module may be novel as a tissue-pair co-abundance pattern, but the available evidence does not establish a newly discovered molecular complex or pathway. Several relationships are already documented by STRING or hu.MAP, and most genes have established cellular functions and disease associations. Conversely, the particular combination of genes, its conservation between autonomic nervous system and bone marrow, and its co-abundance topology are not shown in the fact sheet to have been previously described. Absence from STRING or hu.MAP cannot demonstrate novelty because those resources mainly catalogue physical or curated molecular relationships, not every tissue-specific or cross-tissue abundance pattern. A credible novelty claim would require comparison with published co-expression modules, independent cohorts, cell-composition-adjusted analyses, and replication in separate datasets. At present, the appropriate conclusion is a potentially novel association pattern with a largely non-novel molecular repertoire.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular resource-management state present in both tissues, combining ribosome production and quality control with RNA handling, chromatin maintenance, mitochondrial support, vesicle trafficking, and cell-cycle-related functions. In bone marrow, this state could be accentuated by biosynthetically active progenitors and blood-cell populations. In autonomic nervous system samples, it could arise from broadly expressed support or proliferative cell populations, technical abundance effects, or shared cellular stress and maintenance demands. The model predicts that the module will weaken after adjustment for cell composition and general expression abundance, while selected submodules involving NEMF, RPL6, WDR12, and UTP20 may remain linked to translational and ribosome-related activity. This is a hypothesis, not an established pathway assignment.

### Important genes

#### ACTR8

- **Related proteins** (co-abundance neighbors): HIRIP3 (0.96), TUBGCP2 (0.95), RPL6 (0.92), NRDC (0.87), UTP20 (0.87), NAGK (0.87), NAA15 (0.87), GTF3C5 (0.87), RUFY1 (0.86), NUP160 (0.86), CERT1 (0.86), RAP1GDS1 (0.84), COPS8 (0.83), AKAP8L (0.83), SLC1A5 (0.83), CSE1L (0.83), DDX5 (0.83), EIF4G3 (0.82), GNPNAT1 (0.81), IARS2 (0.80), CPOX (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: actin related protein 8. Predicted to enable ATP binding activity. Predicted to be involved in chromatin remodeling; double-strand break repair; and regulation of transcription, DNA-templated. Located in centrosome and nucleoplasm. Part of Ino80 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.381); tympanic membrane disorder (0.167); hypertensive disorder (0.075); alcohol drinking (0.075); bone remodeling disease (0.062)
- **Europe PMC papers**: 274
- **Why important**: ACTR8 is the central network connector in the supplied subgraph, linking genes involved in chromatin organization, centrosomal and microtubule biology, amino-sugar metabolism, transcription, translation-related machinery, and nuclear transport. Its MyGene annotation places it in the Ino eighty chromatin-remodeling complex and in DNA repair and transcriptional regulation. Its high literature volume and disease links make it an informative anchor for distinguishing a genuine regulatory program from simple abundance co-variation.
- **Conclusion**: Established evidence supports ACTR8 as a broadly expressed chromatin-remodeling and genome-maintenance component with a prominent network position. The hypothesis that ACTR8 organizes the entire module is not established, because the fact sheet reports no STRING or hu.MAP relationship for ACTR8 and no globally significant enrichment.

#### DNMT1

- **Related proteins** (co-abundance neighbors): CHML (0.83), NEMF (0.83), PRRC2B (0.81), CLASP1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA methyltransferase 1. This gene encodes an enzyme that transfers methyl groups to cytosine nucleotides of genomic DNA. This protein is the major enzyme responsible for maintaining methylation patterns following DNA replication and shows a preference for hemi-methylated DNA. Methylation of DNA is an important component of mammalian epigenetic gene regulation. Aberrant methylation patterns are found in human tumors and a…
- **Diseases (Open Targets)**: autosomal dominant cerebellar ataxia, deafness and narcolepsy (0.806); hereditary sensory neuropathy-deafness-dementia syndrome (0.777); acute myeloid leukemia (0.623); myelodysplastic syndrome (0.615); cancer (0.612)
- **Europe PMC papers**: 30754
- **Why important**: DNMT1 is connected in the module to CHML, NEMF, PRRC2B, and CLASP1 and is the principal maintenance DNA methyltransferase described in the fact sheet. It links the module to epigenetic inheritance and transcriptional regulation. Its extensive literature and associations with acute myeloid leukemia, myelodysplastic syndrome, and neurological disease are especially relevant to a module shared by a hematopoietic tissue and a nervous-system-related tissue.
- **Conclusion**: Established evidence supports DNMT1 as an epigenetic maintenance enzyme with major disease relevance and plausible importance in progenitor-cell biology. It is not established that DNMT1 drives the observed cross-tissue co-abundance pattern; its inclusion may instead reflect a general proliferative or nuclear-maintenance state.

#### NEMF

- **Related proteins** (co-abundance neighbors): DNMT1 (0.83); STRING partners: RPL6 (0.81)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_11021.1, huMAP3_10359.1, huMAP3_10631.1, huMAP3_11111.1
- **Function (MyGene.info)**: nuclear export mediator factor. This gene encodes a component of the ribosome quality control complex. The encoded protein facilitates the recognition and ubiquitination of stalled 60S subunits by the ubiquitin ligase listerin. A similar protein in fly functions as a tumor suppressor. [provided by RefSeq, Jul 2016].
- **Diseases (Open Targets)**: intellectual developmental disorder with speech delay and axonal peripheral neuropathy (0.708); hereditary disease (0.471); Global developmental delay (0.374); Intellectual disability (0.371); cerebellar ataxia (0.370)
- **Europe PMC papers**: 2061
- **Why important**: NEMF has direct STRING support with RPL6 and appears with SCAF8 and DDX5 in multiple hu.MAP complexes (hu.MAP huMAP3_11021.1), (hu.MAP huMAP3_10359.1), (hu.MAP huMAP3_10631.1), and (hu.MAP huMAP3_11111.1). Its annotated function in ribosome quality control, recognition of stalled ribosomes, and ubiquitin-dependent rescue provides a mechanistic bridge between translation, RNA-associated complexes, and proteostasis. It also has substantial literature and disease associations involving developmental delay, peripheral neuropathy, and ataxia.
- **Conclusion**: Established evidence supports NEMF as a ribosome quality-control factor embedded in several known molecular contexts. It is reasonable to view NEMF as a strong candidate marker of translational stress or proteostasis activity in this module, but the fact sheet does not establish that such stress caused the module or is specific to either tissue.

#### WDR12

- **Related proteins** (co-abundance neighbors): TMEM87B (0.87); STRING partners: RPL6 (0.945), UTP20 (0.848)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 12. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); poisoning (0.233); non-autoimmune hemolytic anemia (0.214); coronary artery disorder (0.210); myocardial infarction (0.168)
- **Europe PMC papers**: 602
- **Why important**: WDR12 is linked by STRING to RPL6 and UTP20 and is annotated for ribosome biogenesis and maturation of ribosomal RNA. Its connections provide a coherent molecular bridge to the ribosome-related interpretation, while its HPA bone-marrow detection is compatible with activity in biosynthetically active marrow cells. Its disease associations further motivate testing whether altered ribosome production contributes to the module.
- **Conclusion**: Established evidence supports WDR12 as a ribosome-biogenesis component with known links to RPL6 and UTP20. A hypothesis that WDR12 marks coordinated ribosome production within the shared module is plausible, but no globally corrected GO/KEGG enrichment or module-specific perturbation evidence confirms it.

#### CHML

- **Related proteins** (co-abundance neighbors): ARIH1 (0.90), NFU1 (0.90), LBR (0.90), CLASP1 (0.88), NRDC (0.88), IDE (0.88), ARHGAP17 (0.86), DNMT1 (0.83), RUFY1 (0.82), TNIK (0.81), SEC23A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CHM like Rab escort protein. The product of the CHML gene supports geranylgeranylation of most Rab proteins and may substitute for REP-1 in tissues other than retina. CHML is localized close to the gene for Usher syndrome type II. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: glomerulonephritis (0.275); alopecia areata (0.183); hepatocellular carcinoma (0.099); renal osteodystrophy (0.077); Miyoshi myopathy (0.074)
- **Europe PMC papers**: 317
- **Why important**: CHML has a comparatively well-connected position outside the ACTR8 neighborhood and links genes involved in Rab-protein geranylgeranylation, vesicle transport, cytoskeletal regulation, epigenetic maintenance, and mitochondrial function. Its HPA profile includes bone-marrow detection and enrichment among several progenitor populations. Its function provides a possible trafficking and membrane-organization axis that complements the nuclear and ribosome-related genes.
- **Conclusion**: Established evidence supports CHML as a Rab-escort factor involved in protein targeting, intracellular transport, and geranylgeranylation. The hypothesis that CHML connects vesicle trafficking to the rest of the module is supported by the local network structure but not by direct STRING or hu.MAP evidence for this module.

## Module 2

**Tissue pair**: autonomic_nervous_system and bone_marrow  
**Genes (41)**: GOT2, ARHGEF12, AURKA, BCL2, BCL7A, GLB1, BUB1B, BYSL, CD47, CDK7, NCAPH2, COMMD9, COPG2, DDX41, DAGLB, FASTKD5, GBA1, GHDC, GPATCH8, GSTCD, GSTM2, H1-0, IMP4, CKB, KIF21A, LYPLA1, MYLK, NCDN, NELFE, P3H1, PI4KA, PRC1, RETSAT, MRPL10, SCD, SRP68, SRSF8, TMOD1, TOP2B, TSPYL5, SNRNP200

### Function

No GO/KEGG term passed global multiple-testing correction, so the module does not support a statistically established single pathway-level function from enrichment analysis. The gene annotations and network instead indicate a heterogeneous cellular module with several connected themes: mitotic progression and chromosome segregation through AURKA, BUB1B, PRC1, NCAPH2 and related genes; RNA processing and splicing through SRSF8, GPATCH8, SNRNP200 and DDX41; intracellular lipid, lysosomal and membrane biology through DAGLB, GBA1, GLB1, PI4KA and SCD; and neuronal or cytoskeletal functions through NCDN, MYLK, TMOD1 and related genes. The strongest direct network-supported motif is the known AURKA–BUB1B–PRC1 interaction group, while the hu.MAP memberships support RNA-processing and spliceosomal associations (hu.MAP huMAP3_09943.1) (hu.MAP huMAP3_07622.1) (hu.MAP huMAP3_09637.1) (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1), (hu.MAP huMAP3_09621.1) (hu.MAP huMAP3_09945.1) (hu.MAP huMAP3_11073.1) (hu.MAP huMAP3_08980.1). These observations support a broad cellular-state interpretation rather than a uniquely defined biological process. The lack of globally significant enrichment does not invalidate the module, but it limits functional specificity.

**Cell composition.** The module is not predominantly composed of secreted or plasma proteins: the HPA summary identifies only a minority of secreted genes, and many proteins are intracellular or membrane-associated. It is also not uniformly blood-cell enriched. Most genes have low immune-cell specificity, although selected genes show enhancement in B-cell, neutrophil, basophil, platelet, megakaryocyte or erythrocyte-progenitor populations. HPA tissue evidence is similarly mixed: many genes have low tissue specificity, while subsets are enhanced in bone marrow, brain, testis, adipose tissue, liver or skeletal muscle. Protein detection in bone marrow is common, whereas no matching HPA tissue is available for autonomic nervous system. The shared module could therefore partly reflect broadly expressed cellular machinery and bone-marrow cellular composition, especially proliferative or hematopoietic states, rather than a specialized autonomic-nervous-system program. The presence of brain-enhanced genes such as NCDN and PI4KA and bone-marrow-enhanced mitotic genes such as AURKA, BUB1B and PRC1 argues against reducing the module to a simple blood-contamination signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a limited set of high-confidence relationships rather than broad support for one unified interaction network. Established relationships include AURKA with BUB1B and PRC1, BYSL with IMP4, CDK7 with NELFE, and GBA1 with GLB1. These links connect cell-cycle control, ribosome biogenesis, transcriptional regulation and lysosomal biology, but they do not establish a common biochemical complex for the entire module. hu.MAP provides repeated support for RNA-processing and spliceosomal associations involving SRSF8, GPATCH8, SNRNP200, NCDN and DDX41 (hu.MAP huMAP3_09943.1) (hu.MAP huMAP3_07622.1) (hu.MAP huMAP3_09637.1) (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1), (hu.MAP huMAP3_09621.1) (hu.MAP huMAP3_09945.1) (hu.MAP huMAP3_11073.1) (hu.MAP huMAP3_08980.1). RETSAT and GHDC occur together in a lipid-associated hu.MAP complex (hu.MAP huMAP3_15113.1). Most module genes have no listed STRING partner or hu.MAP membership, so the co-abundance structure extends beyond currently catalogued physical interactions. The known interactions support parts of the module and suggest that the co-abundance signal may combine several cellular programs.

**STRING interactions (score >= 0.7)**: 6 of 820 gene pairs: AURKA–BUB1B (0.924); AURKA–PRC1 (0.91); BUB1B–PRC1 (0.893); BYSL–IMP4 (0.999); CDK7–NELFE (0.713); GBA1–GLB1 (0.976)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09943.1 (SRSF8, DDX41, GPATCH8; 3/78); huMAP3_07622.1 (SNRNP200, NCDN; 2/9); huMAP3_09637.1 (SRSF8, GPATCH8; 2/21); huMAP3_08501.1 (SNRNP200, NCDN; 2/47); huMAP3_09504.1 (SNRNP200, NCDN; 2/51); huMAP3_15113.1 (RETSAT, GHDC; 2/53); huMAP3_09621.1 (SRSF8, GPATCH8; 2/56); huMAP3_09945.1 (SNRNP200, NCDN; 2/61); huMAP3_11073.1 (SRSF8, GPATCH8; 2/67); huMAP3_08980.1 (SNRNP200, NCDN; 2/97)

### Novelty

This module should not be called a definitively new biological discovery. Its strongest interpretable components involve well-established genes and known relationships, including the mitotic AURKA–BUB1B–PRC1 group, the BYSL–IMP4 relationship, the GBA1–GLB1 relationship, and several spliceosomal complexes. At the same time, the particular co-abundance combination across autonomic nervous system and bone marrow, including genes from cell-cycle, RNA-processing, lipid, lysosomal and neuronal programs, is not directly established by the listed STRING or hu.MAP evidence. The module may therefore represent a potentially novel cross-tissue co-abundance pattern, but novelty requires independent replication, control for cell composition, comparison with existing co-expression studies and experimental validation. Absence of a complete matching STRING or hu.MAP complex is evidence of incomplete cataloguing, not proof of novelty.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program that becomes co-abundant in bone-marrow-associated proliferative cells and in autonomic-nervous-system samples containing related broadly expressed or neuronal-support cellular states. In this model, mitotic machinery represented by AURKA, BUB1B and PRC1 is coupled at the abundance level to RNA processing, ribosome production, lipid or membrane handling and lysosomal activity. Bone-marrow cell composition may contribute substantially, while the neuronal annotations may reflect a tissue-specific component or shared cellular machinery rather than a single autonomic function. This hypothesis predicts that the module will vary with proliferative-cell abundance, hematopoietic composition and neuronal or glial representation, and that its genes will not necessarily colocalize in one physical complex.

### Important genes

#### AURKA

- **Related proteins** (co-abundance neighbors): GHDC (0.84), TSPYL5 (0.80), GSTM2 (0.80); STRING partners: BUB1B (0.924), PRC1 (0.91)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitotic spindle, Centrosome, Basal body; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aurora kinase A. The protein encoded by this gene is a cell cycle-regulated kinase that appears to be involved in microtubule formation and/or stabilization at the spindle pole during chromosome segregation. The encoded protein is found at the centrosome in interphase cells and at the spindle poles in mitosis. This gene may play a role in tumor development and progression. A processed pseudogene of this gene has b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.521); Alzheimer disease (0.520); Parkinson disease (0.502); lysosomal storage disease (0.499); plasma cell myeloma (0.288)
- **Europe PMC papers**: 10027
- **Why important**: AURKA is a central connector in the module and participates in the directly supported STRING interaction group with BUB1B and PRC1. Its established function is a centrosomal and spindle-associated kinase involved in mitotic progression, spindle organization and chromosome segregation. HPA reports enhancement in lymphoid tissue and testis, cell-type enhancement in erythrocyte progenitors and differentiating germ cells, and protein detection in bone marrow. It also has substantial disease and literature support, including cancer and neurodegenerative-disease associations.
- **Conclusion**: Established evidence supports AURKA as a marker of proliferative and mitotic cellular state in this module. It is a plausible driver of the cell-cycle component, but the co-abundance data do not establish that AURKA mechanistically regulates the other module branches.

#### BUB1B

- **Related proteins** (co-abundance neighbors): GHDC (0.89), GLB1 (0.87), GPATCH8 (0.86); STRING partners: AURKA (0.924), PRC1 (0.893)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BUB1 mitotic checkpoint serine/threonine kinase B. This gene encodes a kinase involved in spindle checkpoint function. The protein has been localized to the kinetochore and plays a role in the inhibition of the anaphase-promoting complex/cyclosome (APC/C), delaying the onset of anaphase and ensuring proper chromosome segregation. Impaired spindle checkpoint function has been found in many forms of cancer. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: mosaic variegated aneuploidy syndrome (0.815); mosaic variegated aneuploidy syndrome 1 (0.794); premature chromatid separation trait (0.631); neurodegenerative disease (0.537); colorectal cancer (0.503)
- **Europe PMC papers**: 3723
- **Why important**: BUB1B links the module to spindle-checkpoint control and chromosome segregation and forms high-confidence STRING relationships with AURKA and PRC1. Its HPA profile is enhanced in bone marrow and lymphoid tissue, with cell-type enhancement in erythrocyte and megakaryocyte progenitors. Its disease associations include mosaic variegated aneuploidy and premature chromatid-separation phenotypes, and it has substantial literature support.
- **Conclusion**: Established evidence identifies BUB1B as a strong indicator of proliferating progenitor or mitotic cells within the shared module. Its presence supports a cell-cycle interpretation, but does not by itself demonstrate a tissue-specific autonomic mechanism.

#### GSTCD

- **Related proteins** (co-abundance neighbors): BYSL (0.93), GOT2 (0.92), COPG2 (0.89), LYPLA1 (0.89), GHDC (0.89), GSTM2 (0.88), SCD (0.86), PRC1 (0.85), SNRNP200 (0.83), SRP68 (0.83), FASTKD5 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutathione S-transferase C-terminal domain containing. Located in cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: psoriasis (0.352); asthma (0.239); adolescent idiopathic scoliosis (0.230); chronic obstructive pulmonary disease (0.157); ovarian neoplasm (0.140)
- **Europe PMC papers**: 245
- **Why important**: GSTCD has the strongest network position in the supplied module and connects multiple otherwise distinct neighborhoods, including BYSL, GOT2, COPG2, LYPLA1, GHDC, GSTM2, SCD and PRC1. It has bone-marrow protein detection and low tissue specificity, while its functional annotation suggests a glutathione-related or inflammatory role. Although it lacks listed STRING partners and hu.MAP membership, its network position makes it important for the observed co-abundance topology. Its disease associations include inflammatory, respiratory and neoplastic conditions.
- **Conclusion**: Established evidence supports GSTCD as a structural network hub and possible integrator of metabolic, vesicular and proliferative signals. Its biochemical role in this module remains uncertain because its direct interaction support is absent and its annotation is comparatively limited.

#### SRSF8

- **Related proteins** (co-abundance neighbors): COMMD9 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_09943.1, huMAP3_09637.1, huMAP3_09621.1, huMAP3_11073.1
- **Function (MyGene.info)**: serine and arginine rich splicing factor 8. This gene encodes a member of a family of proteins containing a ribonucleoprotein (RNP)-type RNA binding motif and a carboxyl-terminal arginine-serine-rich (RS) domain. The encoded protein functions as a pre-mRNA splicing factor. There is a pseudogene for this gene on chromosome 7. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2013].
- **Diseases (Open Targets)**: gestational diabetes (0.155); alcohol drinking (0.107); urolithiasis (0.099); Abnormality of the skeletal system (0.099); obesity disorder (0.066)
- **Europe PMC papers**: 160
- **Why important**: SRSF8 is a canonical pre-mRNA splicing factor and is present in several hu.MAP complexes with GPATCH8 and other RNA-processing proteins (hu.MAP huMAP3_09943.1), (hu.MAP huMAP3_09637.1), (hu.MAP huMAP3_09621.1), (hu.MAP huMAP3_11073.1). It connects to COMMD9 in the co-abundance graph and has bone-marrow protein detection. Its HPA single-cell annotation includes platelets, and its known function provides a direct interpretation for the RNA-processing branch of the module.
- **Conclusion**: Established evidence supports SRSF8 as a representative of the module's spliceosomal and RNA-processing component. The data support coordinated abundance with other module genes, but do not show that altered SRSF8 activity causes the broader cross-tissue pattern.

#### NCDN

- **Related proteins** (co-abundance neighbors): DAGLB (0.89); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_08980.1
- **Function (MyGene.info)**: neurochondrin. This gene encodes a leucine-rich cytoplasmic protein, which is highly similar to a mouse protein that negatively regulates Ca/calmodulin-dependent protein kinase II phosphorylation and may be essential for spatial learning processes. Several alternatively spliced transcript variants of this gene have been described. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodevelopmental disorder with infantile epileptic spasms (0.670); epilepsy (0.430); Intellectual disability (0.416); autosomal recessive non-syndromic intellectual disability (0.370); neurodegenerative disease (0.212)
- **Europe PMC papers**: 301
- **Why important**: NCDN is tissue-enriched in brain and has cell-type enhancement across neuronal populations, providing the clearest nervous-system-related annotation in the module. It is also present with SNRNP200 in multiple hu.MAP complexes (hu.MAP huMAP3_07622.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), (hu.MAP huMAP3_09945.1), (hu.MAP huMAP3_08980.1), linking a neuronal-associated gene to spliceosomal or RNA-processing complex evidence. Its established functions include regulation of neuronal synaptic plasticity and postsynaptic receptor internalization, and it has disease associations involving epilepsy and neurodevelopment.
- **Conclusion**: Established evidence supports NCDN as a biologically meaningful nervous-system-associated member and as a bridge between neuronal annotation and RNA-processing complex membership. Its presence does not prove that the whole module is neuronal, especially because it lacks listed STRING partners and is not detected in bone-marrow protein assays.

#### GBA1

- **Related proteins** (co-abundance neighbors): MRPL10 (0.82), MYLK (0.81); STRING partners: GLB1 (0.976)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glucosylceramidase beta 1. This gene encodes a lysosomal membrane protein that cleaves the beta-glucosidic linkage of glycosylceramide, an intermediate in glycolipid metabolism. Mutations in this gene cause Gaucher disease, a lysosomal storage disease characterized by an accumulation of glucocerebrosides. A related pseudogene is approximately 12 kb downstream of this gene on chromosome 1. Alternative splicing results in mul…
- **Diseases (Open Targets)**: Gaucher disease (0.815); Gaucher disease type I (0.814); Gaucher disease type II (0.806); Gaucher disease type III (0.798); Gaucher disease perinatal lethal (0.774)
- **Europe PMC papers**: 2888
- **Why important**: GBA1 represents the lysosomal and sphingolipid component of the module. It has a high-confidence STRING relationship with GLB1, is connected in the module to MYLK and MRPL10, and is detected in bone marrow. Its established function is lysosomal glucosylceramide degradation, and its disease associations include Gaucher disease and related lysosomal-storage phenotypes. Its literature support is substantial.
- **Conclusion**: Established evidence supports GBA1 as a lysosomal lipid-catabolism marker and as part of a known relationship with GLB1. The module does not establish that lysosomal dysfunction is the central function, because the global enrichment analysis found no significant GO/KEGG term and the lysosomal genes form only one branch of a heterogeneous network.

## Module 3

**Tissue pair**: autonomic_nervous_system and bone_marrow  
**Genes (41)**: ABHD10, ACADM, ACTL6A, AMPD2, ARFIP1, ARFIP2, BAX, CEP41, NCAPD2, TTC4, CSTF1, CYRIB, DDX6, DNM1L, DPH5, POLE, ADAR, EIF2AK2, EIF3F, FAF1, MACROH2A1, HEATR1, KPNA2, DTYMK, MYO9B, NELFCD, ODF2, PHB2, GART, ADSS2, RAB8B, RSL1D1, RRS1, TMEM97, SYMPK, TOE1, TRAP1, UCHL5, ATP6V1A, XPO5, ZC3H7B

### Function

The module does not have a globally significant GO or KEGG enrichment term; no GO/KEGG term passed global correction. Its gene-level annotations instead indicate a broad cellular maintenance program involving DNA replication and repair, RNA processing and export, ribosome biogenesis, translation control, purine and nucleotide metabolism, mitochondrial organization, vesicle trafficking, and cytoskeletal or ciliary biology. The co-abundance structure is therefore more consistent with coordinated expression of proliferative, biosynthetic, RNA-regulatory, and organelle-maintenance functions than with a narrowly defined pathway. The network hub ODF2 connects many otherwise weakly connected genes, while POLE links several replication, metabolism, chromatin, and RNA-processing genes. STRING support is limited to selected pairwise relationships, so the inferred function should remain broad and provisional. The absence of a globally significant enrichment term does not invalidate the module.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and most have low immune-cell specificity, supporting a substantial housekeeping or broadly cellular component. At the same time, the module shows a mixed cell-state signature. HPA links several genes to bone marrow, erythrocyte or megakaryocyte progenitors, neutrophils, and other myeloid populations, while many genes are enhanced in germ-cell states and some are enriched in testis. Bone-marrow protein detection is frequent among the tested genes, whereas ODF2, ARFIP2, ARFIP1, NELFCD, TMEM97, and AMPD2 are not detected there in the stated HPA measurements. The shared signal may therefore reflect broadly expressed cellular programs together with shared proliferative or progenitor cell types, rather than a specialized autonomic-nervous-system secretory program. The testis and spermatogenic associations also warrant caution about interpreting the module as a tissue-specific neural or marrow pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING contains established or database-supported relationships for ACTL6A with UCHL5; ADAR with EIF2AK2; ADSS2 with AMPD2 and GART; ARFIP1 with ARFIP2; CSTF1 with SYMPK; DDX6 with XPO5; DTYMK with GART; HEATR1 with RSL1D1; KPNA2 with XPO5; and RRS1 with RSL1D1. These links support real molecular neighborhoods involving RNA regulation, purine or nucleotide metabolism, RNA export, polyadenylation, and nucleolar or ribosome biology, but they cover only a minority of possible module pairs and do not establish a single coherent complex. hu.MAP provides repeated support for the ARFIP1–ARFIP2 pair in complexes (hu.MAP huMAP3_02954.1), (hu.MAP huMAP3_00294.1), and (hu.MAP huMAP3_11483.1), for the DTYMK–PHB2 pair in (hu.MAP huMAP3_09122.1), and for the CSTF1–SYMPK pair in (hu.MAP huMAP3_09096.1) and (hu.MAP huMAP3_11757.1). The hu.MAP complexes generally contain additional proteins outside the module, so they support embedded known subcomplexes rather than proving that the full module is a single physical complex. ODF2 is the major network connector despite lacking STRING partners and hu.MAP assignment, which suggests that co-abundance structure extends beyond currently catalogued physical interactions.

**STRING interactions (score >= 0.7)**: 11 of 820 gene pairs: ACTL6A–UCHL5 (0.952); ADAR–EIF2AK2 (0.873); ADSS2–AMPD2 (0.992); ADSS2–GART (0.981); ARFIP1–ARFIP2 (0.785); CSTF1–SYMPK (0.939); DDX6–XPO5 (0.943); DTYMK–GART (0.835); HEATR1–RSL1D1 (0.982); KPNA2–XPO5 (0.708); RRS1–RSL1D1 (0.992)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02954.1 (ARFIP2, ARFIP1; 2/2); huMAP3_00294.1 (ARFIP2, ARFIP1; 2/3); huMAP3_09122.1 (DTYMK, PHB2; 2/3); huMAP3_11483.1 (ARFIP2, ARFIP1; 2/4); huMAP3_09096.1 (CSTF1, SYMPK; 2/15); huMAP3_11757.1 (CSTF1, SYMPK; 2/16)

### Novelty

The module should not be called a wholly new molecular complex. Several internal relationships and subcomplexes are already represented in STRING and hu.MAP, and the functions of many genes are well established. Its potentially novel aspect is the conserved co-abundance association of this particular mixture across autonomic nervous system and bone marrow, especially the connection centered on ODF2 between ciliary or spermatogenic biology and broadly expressed replication, RNA, metabolic, mitochondrial, and trafficking genes. However, absence from STRING or hu.MAP cannot establish novelty, and the lack of globally significant GO/KEGG enrichment makes a strong pathway-level novelty claim inappropriate. The most defensible conclusion is that this is a potentially novel cross-tissue co-abundance pattern built partly from known molecular relationships, requiring independent replication and cell-composition controls.

**Hypothesis.** Hypothesis: the conserved module reflects a shared cellular-state program present in selected progenitor or proliferative populations rather than a dedicated autonomic-nervous-system or bone-marrow pathway. In this model, POLE-associated replication and repair activity is coordinated with nucleotide supply, ribosome production, RNA processing and export, mitochondrial stress management, vesicle or actin organization, and selective apoptotic control. ODF2 may act as a statistical connector because ciliary or centrosomal and spermatogenic programs covary with this state, or because a small number of cell populations contribute both signals. ADAR–EIF2AK2 could couple RNA surveillance and antiviral stress signaling to translational control. This remains a hypothesis: the co-abundance network does not demonstrate physical interaction, causal regulation, or a shared cellular origin.

### Important genes

#### ODF2

- **Related proteins** (co-abundance neighbors): ACTL6A (0.98), NELFCD (0.95), TOE1 (0.94), ZC3H7B (0.94), TMEM97 (0.93), DNM1L (0.92), EIF3F (0.91), ABHD10 (0.91), ACADM (0.89), ADAR (0.89), ATP6V1A (0.87), DTYMK (0.86), RSL1D1 (0.86), ARFIP2 (0.84), RAB8B (0.84), TRAP1 (0.83), XPO5 (0.83), BAX (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location Primary cilium, Centrosome, Basal body, Connecting piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: outer dense fiber of sperm tails 2. The outer dense fibers are cytoskeletal structures that surround the axoneme in the middle piece and principal piece of the sperm tail. The fibers function in maintaining the elastic structure and recoil of the sperm tail as well as in protecting the tail from shear forces during epididymal transport and ejaculation. Defects in the outer dense fibers lead to abnormal sperm morphology and infertili…
- **Diseases (Open Targets)**: non-syndromic male infertility due to sperm motility disorder (0.074); spermatogenic failure 43 (0.067); spermatogenic failure 27 (0.067); spermatogenic failure 34 (0.067); spermatogenic failure 24 (0.066)
- **Europe PMC papers**: 861
- **Why important**: ODF2 is the dominant network hub and connects genes spanning replication, mitochondrial function, RNA regulation, translation, centrosomal biology, and membrane or metabolic processes. Its HPA annotation is strongly associated with testis and late spermatids, and its established function in sperm outer dense fibers and cilium organization provides a distinctive biological anchor. It also has extensive literature and associations with male infertility and spermatogenic failure.
- **Conclusion**: Established evidence supports ODF2 as a ciliary, centrosomal, and sperm-tail structural protein and as the central statistical connector of this module. The hypothesis that ODF2 organizes the cross-tissue module biologically is not established; its hub position may instead reflect cell-state composition or coordinated regulation.

#### POLE

- **Related proteins** (co-abundance neighbors): GART (0.94), KPNA2 (0.90), DPH5 (0.90), ADSS2 (0.90), HEATR1 (0.88), ATP6V1A (0.88), CYRIB (0.88), SYMPK (0.87), FAF1 (0.87), RRS1 (0.86), PHB2 (0.84), CSTF1 (0.84), UCHL5 (0.83), NCAPD2 (0.83), DNM1L (0.83), MYO9B (0.81), AMPD2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA polymerase epsilon, catalytic subunit. This gene encodes the catalytic subunit of DNA polymerase epsilon. The enzyme is involved in DNA repair and chromosomal DNA replication. Mutations in this gene have been associated with colorectal cancer 12 and facial dysmorphism, immunodeficiency, livedo, and short stature. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal cancer, susceptibility to, 12 (0.739); intrauterine growth retardation, metaphyseal dysplasia, adrenal hypoplasia congenita, genital anomalies, and immunodeficiency (0.735); facial dysmorphism-immunodeficiency-livedo-short stature syndrome (0.732); non-small cell lung carcinoma (0.668); B-cell chronic lymphocytic leukemia (0.660)
- **Europe PMC papers**: 71098
- **Why important**: POLE is among the strongest network hubs and is connected to genes involved in nucleotide metabolism, nuclear transport, chromatin or RNA functions, and organelle biology. It is tissue enhanced in bone marrow and cell-type enhanced in erythrocyte and megakaryocyte progenitor states as well as neutrophil progenitors. Its catalytic role in DNA replication and repair, disease associations involving colorectal cancer and immunodeficiency, and very large literature base make it a strong marker of proliferative and genome-maintenance activity.
- **Conclusion**: Established evidence supports POLE as a core DNA replication and repair enzyme and a plausible indicator of proliferative progenitor biology in the bone-marrow component. It does not prove that DNA replication is the sole or defining function of the module, especially because no GO/KEGG term passed global correction.

#### ADAR

- **Related proteins** (co-abundance neighbors): ODF2 (0.89), RSL1D1 (0.81), DNM1L (0.81); STRING partners: EIF2AK2 (0.873)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR provides a mechanistically informative bridge between RNA editing and innate antiviral signaling. It is connected in the module to DNM1L and RSL1D1, and STRING supports its relationship with EIF2AK2. HPA reports enhancement in neutrophils, while its established function is adenosine-to-inosine RNA editing and regulation of double-stranded-RNA responses. Its associations with Aicardi-Goutieres syndrome and related interferonopathy, together with substantial literature, strengthen its interpretive value.
- **Conclusion**: Established evidence supports ADAR as an RNA-editing and antiviral-response regulator. A coordinated ADAR–EIF2AK2 stress-response axis is a plausible interpretation of the module, but the co-abundance data do not establish activation of antiviral signaling.

#### DNM1L

- **Related proteins** (co-abundance neighbors): ODF2 (0.92), POLE (0.83), ADAR (0.81), TRAP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 1L. This gene encodes a member of the dynamin superfamily of GTPases. The encoded protein mediates mitochondrial and peroxisomal division, and is involved in developmentally regulated apoptosis and programmed necrosis. Dysfunction of this gene is implicated in several neurological disorders, including Alzheimer's disease. Mutations in this gene are associated with the autosomal dominant disorder, ence…
- **Diseases (Open Targets)**: encephalopathy, lethal, due to defective mitochondrial peroxisomal fission 1 (0.815); autosomal dominant optic atrophy, classic form (0.721); neurodegenerative disease (0.531); encephalopathy due to mitochondrial and peroxisomal fission defect (0.455); hereditary disease (0.451)
- **Europe PMC papers**: 3015
- **Why important**: DNM1L links the high-centrality ODF2 region to mitochondrial and stress-related biology through connections with ODF2, POLE, ADAR, and TRAP1. Its established role in mitochondrial and peroxisomal fission, apoptosis, and organelle organization gives the module a plausible organelle-quality-control component. Its disease associations include lethal encephalopathy caused by defective mitochondrial and peroxisomal fission and optic atrophy, with a substantial literature base.
- **Conclusion**: Established evidence supports DNM1L as a mitochondrial and peroxisomal division factor involved in stress and apoptotic responses. Its position makes it a credible mediator of organelle maintenance within the module, but a causal role in the cross-tissue conservation remains hypothetical.

#### ARFIP2

- **Related proteins** (co-abundance neighbors): ODF2 (0.84); STRING partners: ARFIP1 (0.785)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02954.1, huMAP3_00294.1, huMAP3_11483.1
- **Function (MyGene.info)**: ARF interacting protein 2. Enables several functions, including GTP-dependent protein binding activity; membrane curvature sensor activity; and phosphatidylinositol-4-phosphate binding activity. Involved in actin cytoskeleton organization. Located in cell cortex; ruffle; and trans-Golgi network membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.081); familial idiopathic steroid-resistant nephrotic syndrome (0.071); early-onset non-syndromic cataract (0.068); retinitis pigmentosa (0.065); focal segmental glomerulosclerosis (0.065)
- **Europe PMC papers**: 226
- **Why important**: ARFIP2 is supported by STRING with ARFIP1 and is represented with ARFIP1 in several hu.MAP complexes (hu.MAP huMAP3_02954.1), (hu.MAP huMAP3_00294.1), and (hu.MAP huMAP3_11483.1). Its established functions include membrane-curvature sensing, phosphatidylinositol binding, intracellular transport, actin organization, and mitophagy. It therefore supplies a defined trafficking and cytoskeletal component that complements the module's nuclear, metabolic, and mitochondrial annotations.
- **Conclusion**: Established evidence supports ARFIP2 as part of an ARFIP1-associated membrane-trafficking and actin-regulatory system. Its inclusion supports a trafficking or organelle-localization facet of the module, while its role as a cross-tissue coordinator remains a hypothesis.

## Module 4

**Tissue pair**: autonomic_nervous_system and bone_marrow  
**Genes (37)**: ACADVL, AIMP1, HCCS, CCNH, DDX56, DOHH, MPP1, SLC2A6, MTIF2, KIF11, LYSMD2, MPDU1, OSBPL9, PHPT1, PML, CAD, MRPL48, RRP1, MRPS33, SNRPA1, SEC24C, SCAMP1, SF3B3, NANS, SRCAP, SSR1, STMN1, XAB2, TEX10, TMEM41B, TM9SF4, TRIO, TRMT1L, UFD1, VHL, VPS33B, WDHD1

### Function

The module does not support a single formally enriched GO or KEGG function: no GO/KEGG term passed global correction. Its composition instead points to a broadly expressed cellular maintenance program with several connected themes: pre-mRNA splicing through SF3B3, SNRPA1, and XAB2; mitochondrial protein synthesis through MRPS33, MRPL48, and MTIF2; cell-cycle and chromosome-segregation activity through KIF11, WDHD1, CCNH, and STMN1; and protein quality control, oxygen-responsive regulation, trafficking, and membrane metabolism through VHL, UFD1, SEC24C, VPS33B, SLC2A6, and related genes. The sparse co-abundance structure is therefore more consistent with coordinated basic cellular state, proliferation, and organelle activity than with a narrowly specialized tissue function. The autonomic-nervous-system and bone-marrow sharing may reflect common cellular programs rather than a tissue-specific pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: AIMP1 is the only gene annotated as secreted to blood, and the other genes are intracellular or membrane-associated. HPA indicates predominantly low tissue specificity and predominantly low immune-cell specificity, arguing against a strongly blood-cell-restricted module. Nevertheless, several genes show bone-marrow or lymphoid enhancement, and KIF11, WDHD1, STMN1, MPP1, and related genes are associated with hematopoietic progenitor or marrow cell types. Bone-marrow protein detection is present for many members, while several others are not detected there. The pattern is compatible with a broadly expressed housekeeping-like program that may be amplified by shared proliferating or hematopoietic cell populations in the sampled tissues. The few immune-cell-enhanced genes and the single secreted gene are insufficient to establish a blood-derived explanation, but sample cellular composition remains an important alternative explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no supplementary functional enrichment. The high-confidence relationships that are present are concentrated in a few known substructures: MRPS33 connects with MRPL48 and MTIF2 in a mitochondrial translation group; SF3B3 connects with SNRPA1 and XAB2 in spliceosome-related interactions; KIF11 connects with WDHD1 in a mitotic or replication-associated pair; and SEC24C connects with TM9SF4 in vesicle and endomembrane biology. hu.MAP independently places SF3B3 and SNRPA1 together in both reported complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1), although each complex contributes only a small subset of its members to the module. These results show that several edges are biologically established rather than arbitrary, especially the spliceosomal and mitochondrial substructures. At the same time, most module genes lack listed STRING partners or hu.MAP complex membership, so the full module is not a known physical complex. The network may therefore combine several established cellular subsystems linked by co-abundance rather than direct molecular binding.

**STRING interactions (score >= 0.7)**: 8 of 666 gene pairs: KIF11–WDHD1 (0.853); MRPL48–MRPS33 (0.938); MRPL48–MTIF2 (0.925); MRPS33–MTIF2 (0.918); SEC24C–TM9SF4 (0.787); SF3B3–SNRPA1 (0.999); SF3B3–XAB2 (0.977); SNRPA1–XAB2 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06511.1 (SNRPA1, SF3B3; 2/79); huMAP3_08980.1 (SNRPA1, SF3B3; 2/97)

### Novelty

The module may be a new tissue-pair co-abundance observation, but the available evidence does not establish a new molecular pathway or complex. Its strongest subnetworks correspond to well-known spliceosomal, mitochondrial translation, mitotic, and trafficking functions, and many members are broadly expressed housekeeping-type genes. The absence of a complete matching STRING or hu.MAP structure would not by itself prove novelty. A defensible conclusion is that the potentially novel feature is the coordinated abundance pattern shared between autonomic nervous system and bone marrow, whereas the component biology is largely established. Independent replication, preservation across cohorts, cell-type deconvolution, and comparison with existing tissue co-expression modules would be needed to claim a genuinely new module.

**Hypothesis.** Hypothesis: the shared module reflects a common cellular-state program present in neural-associated and marrow samples, combining oxygen and protein-quality control centered on VHL, RNA processing centered on SF3B3 and SNRPA1, mitochondrial translation centered on MRPS33 with MRPL48 and MTIF2, and proliferative or cytoskeletal activity involving KIF11, WDHD1, and STMN1. In bone marrow, this could be strengthened by proliferating progenitors and metabolically active hematopoietic cells; in autonomic nervous system samples, it could reflect shared support cells or broadly expressed maintenance programs rather than neurons specifically. The co-abundance signal should not be interpreted as proof that these proteins form one physical pathway. A testable prediction is that the module will track cellular proliferation, mitochondrial activity, and RNA-processing state after adjustment for tissue cell composition, with the relative contribution of each subprogram varying between tissues.

### Important genes

#### VHL

- **Related proteins** (co-abundance neighbors): DDX56 (0.95), TRMT1L (0.93), LYSMD2 (0.85), RRP1 (0.84), XAB2 (0.84), UFD1 (0.84), WDHD1 (0.83), MRPL48 (0.81), HCCS (0.81), MTIF2 (0.80), TM9SF4 (0.80), KIF11 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: von Hippel-Lindau tumor suppressor. This gene encodes a component of a ubiquitination complex. The encoded protein is involved in the ubiquitination and degradation of hypoxia-inducible-factor (HIF), which is a transcription factor that plays a central role in the regulation of gene expression by oxygen. In addition to oxygen-related gene expression, this protein plays a role in many other cellular processes including cilia formatio…
- **Diseases (Open Targets)**: von Hippel-Lindau disease (0.889); Chuvash polycythemia (0.794); pheochromocytoma (0.759); hereditary pheochromocytoma-paraganglioma (0.726); clear cell renal carcinoma (0.643)
- **Europe PMC papers**: 27012
- **Why important**: VHL is the central network hub by weighted degree and links multiple otherwise weakly connected parts of the module, including RNA-associated, mitochondrial, replication-associated, and trafficking-related genes. Its established function as a ubiquitination-complex component regulating HIF degradation provides a plausible oxygen-sensitive organizing axis. It is detected in bone marrow, has extensive disease literature, and is associated with von Hippel–Lindau disease, Chuvash polycythemia, and pheochromocytoma. It has no listed STRING partners or hu.MAP complex membership in this module, so its hub status is a co-abundance property rather than evidence of direct physical interaction.
- **Conclusion**: Established evidence supports VHL as a biologically important oxygen-response and protein-degradation regulator and as the strongest statistical connector in this module. It is a plausible coordinating marker, but it is not established that VHL mechanistically drives the abundance of the other module genes.

#### SF3B3

- **Related proteins** (co-abundance neighbors): CAD (0.85), SLC2A6 (0.83), SEC24C (0.82); STRING partners: SNRPA1 (0.999), XAB2 (0.977)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Nucleoli rim; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: splicing factor 3b subunit 3. This gene encodes subunit 3 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); dengue disease (0.370); cervical cancer (0.189); cervical carcinoma (0.189); prostate cancer (0.111)
- **Europe PMC papers**: 965
- **Why important**: SF3B3 is one of the module's clearest mechanistic anchors. It has STRING relationships with SNRPA1 and XAB2, and it shares membership with SNRPA1 in both hu.MAP complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1). Its annotation establishes a role in spliceosome assembly, conformational change, and pre-mRNA splicing. It is detected in bone marrow and has disease associations that include neurodegenerative disease and cancer, with substantial literature support.
- **Conclusion**: Established evidence supports SF3B3 as a spliceosome-associated component represented by a real known subnetwork within the module. Its presence does not demonstrate global spliceosome enrichment, because no GO/KEGG term passed global correction. A role for this spliceosomal subnetwork in the tissue-pair co-abundance pattern remains a hypothesis.

#### SNRPA1

- **Related proteins** (co-abundance neighbors): CCNH (0.88); STRING partners: SF3B3 (0.999), XAB2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein polypeptide A'. Enables RNA binding activity. Involved in mRNA splicing, via spliceosome and spermatogenesis. Located in nuclear speck. Part of U2-type catalytic step 2 spliceosome and U2-type precatalytic spliceosome. Implicated in connective tissue disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.538); dengue disease (0.370); phosphorus metabolism disease (0.196); hypotensive disorder (0.196); cancer (0.087)
- **Europe PMC papers**: 520
- **Why important**: SNRPA1 is directly connected to SF3B3 and XAB2 in STRING and appears with SF3B3 in both hu.MAP complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1). It is a spliceosomal small nuclear ribonucleoprotein component involved in RNA splicing and spliceosomal assembly. It is detected in bone marrow and has disease associations involving neurodegenerative disease, dengue disease, and cancer. Its literature volume is substantial relative to many less characterized module members.
- **Conclusion**: Established evidence supports SNRPA1 as a member of a known spliceosomal interaction group embedded in the module. The data support using it as a marker of RNA-processing state, but do not establish that altered SNRPA1 activity causes the module or explains its sharing between tissues.

#### MRPS33

- **Related proteins** (co-abundance neighbors): TMEM41B (0.98), SRCAP (0.97), TRIO (0.96), MPP1 (0.95), STMN1 (0.84); STRING partners: MRPL48 (0.938), MTIF2 (0.918)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial ribosomal protein S33. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: bipolar disorder (0.336); ovarian neoplasm (0.253); alopecia areata (0.251); schizophrenia (0.235); obsessive-compulsive disorder (0.235)
- **Europe PMC papers**: 206
- **Why important**: MRPS33 is part of a coherent mitochondrial translation subnetwork: it is linked in STRING to MRPL48 and MTIF2, and it also connects within the co-abundance graph to genes involved in mitochondria, cytoskeletal regulation, and cellular growth. Its established function is as a mitochondrial small-subunit ribosomal protein involved in mitochondrial translation. It is broadly expressed, has bone-marrow protein detection, and provides a mechanistic bridge between organelle protein synthesis and the broader cellular-maintenance interpretation.
- **Conclusion**: Established evidence supports MRPS33 as a mitochondrial translation marker and as part of a known mitochondrial protein group. Its disease associations are comparatively less specific than those of VHL or the spliceosomal genes, and the module does not establish that mitochondrial translation is globally enriched. Its contribution is best treated as a supported submodule rather than a complete explanation.

#### KIF11

- **Related proteins** (co-abundance neighbors): VHL (0.80); STRING partners: WDHD1 (0.853)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Mid piece; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 11. This gene encodes a motor protein that belongs to the kinesin-like protein family. Members of this protein family are known to be involved in various kinds of spindle dynamics. The function of this gene product includes chromosome positioning, centrosome separation and establishing a bipolar spindle during cell mitosis. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: microcephaly with or without chorioretinopathy, lymphedema, or intellectual disability (0.821); hereditary disease (0.509); inherited retinal dystrophy (0.507); neurodegenerative disease (0.484); microcephaly (0.412)
- **Europe PMC papers**: 3618
- **Why important**: KIF11 is tissue enhanced in bone marrow and is associated with several hematopoietic progenitor populations in HPA. Its established function in centrosome separation, bipolar spindle formation, chromosome positioning, and mitotic spindle organization makes it a strong indicator of proliferative cellular state. It is connected to WDHD1 by STRING, has substantial literature volume, and is associated with microcephaly and other hereditary or neurodegenerative conditions.
- **Conclusion**: Established evidence supports KIF11 as a mitotic spindle motor and as a plausible marker of proliferating marrow-derived cells. Its presence supports a cell-state or composition explanation for part of the module, but does not prove that proliferation is the dominant function in autonomic nervous system samples.

## Module 5

**Tissue pair**: autonomic_nervous_system and bone_marrow  
**Genes (21)**: ACLY, ATP5F1A, ATP5F1B, CAPRIN1, CASK, CUX1, DPYSL3, EBP, FASN, GSTP1, COLGALT1, H1-10, HSD17B10, AK1, LDHB, PDLIM5, RAN, SUCLG2, IARS1, TUBB6, MPST

### Function

The strongest interpretation is a broadly shared cellular energy and biosynthetic module, centered on small-molecule, purine-containing, nucleoside-phosphate, and nucleobase-containing metabolism, with metabolic-pathway support from (GO:BP small molecule metabolic process; q_global = 0.0053) through (GO:BP nucleobase-containing small molecule metabolic process; q_global = 0.0428). ACLY and FASN connect acetyl-CoA supply with fatty-acid synthesis, LDHB supports lactate and redox metabolism, SUCLG2 supports the tricarboxylic-acid cycle, and AK1 together with ATP5F1A and ATP5F1B links adenine-nucleotide balance to mitochondrial ATP production. HSD17B10 and MPST add mitochondrial lipid, steroid, and sulfur-compound metabolism. RAN, CUX1, H1-10, and TUBB6 indicate that cellular proliferation, chromatin, nuclear transport, and cytoskeletal state may also influence the co-abundance pattern, but these are secondary interpretations rather than globally significant enrichment results. The STRING metabolic annotations (STRING Process Small molecule metabolic process; within-query FDR = 0.0091) and (STRING KEGG Metabolic pathways; within-query FDR = 0.0121) are concordant supplementary evidence, not independent global enrichment evidence.

**Cell composition.** This does not look like a plasma-protein or secreted-protein module: the HPA summary identifies only one secreted gene, and most proteins are intracellular, including cytosolic, mitochondrial, nuclear, membrane, or vesicular proteins. The module is also not strongly blood-cell specific overall. Most genes have low immune-cell specificity, while a smaller subset is immune-cell enhanced or enriched, especially COLGALT1, CUX1, PDLIM5, CASK, and TUBB6. HPA points more often toward epithelial, digestive, liver, muscle, tongue, and parietal-cell contexts than toward a uniform hematopoietic identity. Bone-marrow protein detection for many members is compatible with expression by cells present in bone marrow, but the absence of matching autonomic-nervous-system protein data prevents a direct tissue-level protein comparison. The shared signal should therefore be interpreted cautiously as a conserved intracellular metabolic and energetic program, potentially influenced by shared cell types or sample composition, rather than as a blood-specific secreted signature.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP small molecule metabolic process | 0.0053 | ACLY, AK1, ATP5F1A, ATP5F1B, CASK, EBP, FASN, GSTP1, HSD17B10, LDHB, MPST, RAN, SUCLG2 |
| GO:BP purine-containing compound metabolic process | 0.0106 | ACLY, AK1, ATP5F1A, ATP5F1B, CASK, FASN, LDHB, RAN, SUCLG2 |
| KEGG Metabolic pathways - Homo sapiens (human) | 0.0229 | ACLY, AK1, ATP5F1A, ATP5F1B, COLGALT1, EBP, FASN, GSTP1, HSD17B10, LDHB, MPST, SUCLG2 |
| GO:BP nucleoside phosphate metabolic process | 0.0365 | ACLY, AK1, ATP5F1A, ATP5F1B, CASK, FASN, LDHB, RAN, SUCLG2 |
| GO:BP nucleobase-containing small molecule metabolic process | 0.0428 | ACLY, AK1, ATP5F1A, ATP5F1B, CASK, FASN, LDHB, RAN, SUCLG2 |

### STRING and hu.MAP

The strongest known STRING relationships are ACLY-FASN, ATP5F1A-ATP5F1B, and AK1-ATP5F1A. The ATP synthase pair is also represented together in all listed hu.MAP complexes (hu.MAP huMAP3_08750.1), (hu.MAP huMAP3_09307.1), and (hu.MAP huMAP3_11095.1), providing independent complex-level support for a mitochondrial ATP-synthesis component. The ACLY-FASN relationship supports coordinated lipid biosynthesis, while AK1-ATP5F1A connects nucleotide homeostasis with oxidative phosphorylation. Apart from these relationships, the module has sparse high-confidence STRING connectivity, and most module edges do not have a listed STRING partner or hu.MAP complex. Thus, the module is not simply a single established physical complex; it combines a validated ATP-synthase submodule with broader co-abundance links among metabolic, structural, nuclear, and regulatory proteins. STRING process and tissue enrichments (STRING TISSUES Digestive gland; within-query FDR = 0.0053) through (STRING TISSUES Interstitial cell of Cajal; within-query FDR = 0.0358) are useful supporting context but should not be treated as globally corrected enrichment evidence.

**STRING interactions (score >= 0.7)**: 3 of 210 gene pairs: ACLY–FASN (0.994); AK1–ATP5F1A (0.717); ATP5F1A–ATP5F1B (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Digestive gland (FDR = 0.0053, 17 genes); Process Small molecule metabolic process (FDR = 0.0091, 13 genes); TISSUES Viscus (FDR = 0.0111, 19 genes); KEGG Metabolic pathways (FDR = 0.0121, 11 genes); TISSUES Alimentary canal (FDR = 0.0358, 11 genes); TISSUES Gland (FDR = 0.0358, 20 genes); TISSUES Interstitial cell of Cajal (FDR = 0.0358, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08750.1 (ATP5F1B, ATP5F1A; 2/12); huMAP3_09307.1 (ATP5F1B, ATP5F1A; 2/35); huMAP3_11095.1 (ATP5F1B, ATP5F1A; 2/45)

### Novelty

The module may represent a new cross-tissue co-abundance organization, because its particular combination of metabolic, mitochondrial, structural, nuclear, and regulatory genes is not shown as one established STRING interaction network or one hu.MAP complex. However, this is not sufficient to claim a new biological pathway. Several component relationships and functions are already well established, especially the ATP5F1A-ATP5F1B ATP-synthase pair and the ACLY-FASN metabolic connection. The sparse external interaction support could reflect tissue context, indirect regulation, shared cell composition, or limitations of interaction databases. Therefore, the defensible conclusion is that the cross-tissue module organization is potentially novel and warrants validation, while its component biology is largely established.

**Hypothesis.** Hypothesis: the shared module coordinates energetic and biosynthetic readiness in cells represented in both tissues. Mitochondrial ATP production through ATP5F1A and ATP5F1B, adenine-nucleotide buffering through AK1, carbon and acetyl-CoA allocation through ACLY and FASN, lactate-redox handling through LDHB, and intermediary metabolism through SUCLG2 may form a metabolic backbone. CUX1, RAN, H1-10, TUBB6, PDLIM5, and DPYSL3 could couple that metabolic state to chromatin, cell-cycle, cytoskeletal, neuronal, or muscle-associated programs. This is a mechanistic hypothesis derived from co-abundance and annotations; the fact sheet does not establish direct regulation among these genes or prove that the same cell type generates the module in both tissues.

### Important genes

#### ACLY

- **Related proteins** (co-abundance neighbors): IARS1 (0.84), LDHB (0.83), CAPRIN1 (0.82), SUCLG2 (0.82); STRING partners: FASN (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP citrate lyase. ATP citrate lyase is the primary enzyme responsible for the synthesis of cytosolic acetyl-CoA in many tissues. The enzyme is a tetramer (relative molecular weight approximately 440,000) of apparently identical subunits. It catalyzes the formation of acetyl-CoA and oxaloacetate from citrate and CoA with a concomitant hydrolysis of ATP to ADP and phosphate. The product, acetyl-CoA, serves several im…
- **Diseases (Open Targets)**: familial hypercholesterolemia (0.532); Hypercholesterolemia (0.532); atherosclerosis (0.470); inherited lipid metabolism disorder (0.467); cardiovascular disorder (0.449)
- **Europe PMC papers**: 7957
- **Why important**: ACLY is one of the most strongly integrated metabolic nodes in the module and appears in every globally significant term (GO:BP small molecule metabolic process; q_global = 0.0053) through (GO:BP nucleobase-containing small molecule metabolic process; q_global = 0.0428). Its established function supplies cytosolic acetyl-CoA for fatty-acid and cholesterol biosynthesis, and its STRING relationship with FASN provides a known biochemical connection. Its disease associations include lipid disorders and atherosclerosis, and it has extensive literature support.
- **Conclusion**: Established evidence supports ACLY as a central carbon-allocation enzyme and a plausible metabolic anchor of the module. It is a strong candidate for coordinating the module's lipid and small-molecule metabolism. A module-specific regulatory role linking ACLY across autonomic nervous system and bone marrow remains a hypothesis.

#### ATP5F1A

- **Related proteins** (co-abundance neighbors): LDHB (0.83), ATP5F1B (0.80); STRING partners: AK1 (0.717), ATP5F1B (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_08750.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit alpha. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, using an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic po…
- **Diseases (Open Targets)**: mitochondrial complex V (ATP synthase) deficiency, nuclear type 4A (0.655); mitochondrial proton-transporting ATP synthase complex deficiency (0.648); mitochondrial complex V (ATP synthase) deficiency, nuclear type 4B (0.532); hereditary disease (0.394); Mitochondrial encephalopathy (0.371)
- **Europe PMC papers**: 822
- **Why important**: ATP5F1A is a catalytic ATP-synthase subunit, appears in every globally significant term (GO:BP small molecule metabolic process; q_global = 0.0053) through (GO:BP nucleobase-containing small molecule metabolic process; q_global = 0.0428), and has a strong known STRING relationship with ATP5F1B plus an additional relationship with AK1. It is present in all listed hu.MAP complexes (hu.MAP huMAP3_08750.1), (hu.MAP huMAP3_09307.1), and (hu.MAP huMAP3_11095.1). Its bone-marrow protein detection and mitochondrial localization support a real cellular energy component, while its disease associations include nuclear mitochondrial-complex deficiencies.
- **Conclusion**: Established evidence identifies ATP5F1A as a core oxidative-phosphorylation component and a validated physical anchor of the module. Its co-abundance with nucleotide and glycolytic genes supports an energy-homeostasis interpretation. Whether it changes because of altered mitochondrial activity or merely tracks energetic cell composition is unresolved.

#### ATP5F1B

- **Related proteins** (co-abundance neighbors): CUX1 (0.84), ATP5F1A (0.80); STRING partners: ATP5F1A (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_08750.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit beta. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: hypermetabolism due to uncoupled mitochondrial oxidative phosphorylation 2 (0.499); hypertrophic cardiomyopathy (0.212); Alzheimer disease (0.177); hypertensive disorder (0.117); response to xenobiotic stimulus (0.117)
- **Europe PMC papers**: 735
- **Why important**: ATP5F1B is the complementary catalytic ATP-synthase subunit to ATP5F1A, appears in every globally significant term (GO:BP small molecule metabolic process; q_global = 0.0053) through (GO:BP nucleobase-containing small molecule metabolic process; q_global = 0.0428), and forms the strongest listed STRING pair in the module with ATP5F1A. It is included in all listed hu.MAP complexes (hu.MAP huMAP3_08750.1), (hu.MAP huMAP3_09307.1), and (hu.MAP huMAP3_11095.1), and has extensive supplementary STRING support across metabolic and tissue annotations.
- **Conclusion**: Established evidence supports ATP5F1B as a bona fide mitochondrial ATP-synthesis component and as part of the module's most clearly validated substructure. Its participation in the cross-tissue module likely reflects energetic demand or mitochondrial content. A specific role in coordinating the other module branches is not demonstrated.

#### AK1

- **Related proteins** (co-abundance neighbors): GSTP1 (0.93); STRING partners: ATP5F1A (0.717)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenylate kinase 1. This gene encodes an adenylate kinase enzyme involved in energy metabolism and homeostasis of cellular adenine nucleotide ratios in different intracellular compartments. This gene is highly expressed in skeletal muscle, brain and erythrocytes. Certain mutations in this gene resulting in a functionally inadequate enzyme are associated with a rare genetic disorder causing nonspherocytic hemolytic an…
- **Diseases (Open Targets)**: hemolytic anemia due to adenylate kinase deficiency (0.765); myeloid leukemia (0.131); acute myeloid leukemia (0.059); lung adenocarcinoma (0.051); nasopharyngeal carcinoma (0.049)
- **Europe PMC papers**: 2424
- **Why important**: AK1 appears in every globally significant term (GO:BP small molecule metabolic process; q_global = 0.0053) through (GO:BP nucleobase-containing small molecule metabolic process; q_global = 0.0428) and is an established regulator of intracellular adenine-nucleotide balance. Its known association with ATP5F1A connects nucleotide homeostasis to mitochondrial ATP synthesis. HPA describes enrichment in skeletal muscle and tongue and notes expression in erythrocytes, while the gene has established association with adenylate-kinase-related hemolytic anemia and additional hematologic disease links.
- **Conclusion**: Established evidence supports AK1 as a plausible bridge between purine metabolism and energy production in the module. It may be particularly informative for distinguishing a genuine energetic program from a generic abundance signal. Its cross-tissue role and relationship to the autonomic nervous system remain hypotheses.

#### FASN

- **Related proteins** (co-abundance neighbors): IARS1 (0.91); STRING partners: ACLY (0.994)
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fatty acid synthase. The enzyme encoded by this gene is a multifunctional protein. Its main function is to catalyze the synthesis of palmitate from acetyl-CoA and malonyl-CoA, in the presence of NADPH, into long-chain saturated fatty acids. In some cancer cell lines, this protein has been found to be fused with estrogen receptor-alpha (ER-alpha), in which the N-terminus of FAS is fused in-frame with the C-terminus of …
- **Diseases (Open Targets)**: dengue disease (0.469); autism spectrum disorder (0.333); Parkinson disease (0.295); Epileptic encephalopathy (0.211); neurodegenerative disease (0.205)
- **Europe PMC papers**: 21528
- **Why important**: FASN appears in every globally significant term (GO:BP small molecule metabolic process; q_global = 0.0053) through (GO:BP nucleobase-containing small molecule metabolic process; q_global = 0.0428), catalyzes long-chain fatty-acid synthesis, and has a very strong known STRING relationship with ACLY. HPA associates it with adipose tissue, breast, liver, and lactating cells, and the gene has extensive literature and disease-related evidence, including cancer and neurodegenerative contexts.
- **Conclusion**: Established evidence supports FASN as the lipid-biosynthetic counterpart to ACLY and as a meaningful metabolic component of the module. Its presence argues that the module is not limited to ATP production but includes anabolic carbon use. The extent to which FASN reflects active lipid synthesis rather than tissue or cell-type composition is unresolved.

#### CUX1

- **Related proteins** (co-abundance neighbors): PDLIM5 (0.93), HSD17B10 (0.90), H1-10 (0.89), GSTP1 (0.85), COLGALT1 (0.84), ATP5F1B (0.84), MPST (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Golgi apparatus; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cut like homeobox 1. The protein encoded by this gene is a member of the homeodomain family of DNA binding proteins. It may regulate gene expression, morphogenesis, and differentiation and it may also play a role in the cell cycle progession. Several alternatively spliced transcript variants encoding different isoforms have been identified.[provided by RefSeq, Feb 2011].
- **Diseases (Open Targets)**: global developmental delay with or without impaired intellectual development (0.754); cancer (0.588); myelodysplastic syndrome (0.536); hereditary disease (0.519); acute lymphoblastic leukemia (0.509)
- **Europe PMC papers**: 3914
- **Why important**: CUX1 has the strongest network integration in the supplied module and connects metabolic genes with PDLIM5, HSD17B10, H1-10, GSTP1, COLGALT1, ATP5F1B, and MPST. Its established functions include transcriptional regulation, differentiation, cell-cycle progression, and dendrite morphogenesis. HPA shows bone-marrow detection and immune-cell enhancement, and disease associations include myelodysplastic syndrome, leukemia, cancer, and developmental disorders. It also has extensive literature support.
- **Conclusion**: Established evidence supports CUX1 as a regulatory and differentiation-related hub that could connect the metabolic core to cell state. Its network position makes it important even though it is absent from the globally significant GO/KEGG overlaps. A direct role for CUX1 in driving the metabolic co-abundance program is a hypothesis, not an established conclusion.

## Module 6

**Tissue pair**: autonomic_nervous_system and bone_marrow  
**Genes (7)**: AKAP9, C5orf22, CENPF, DCAF13, NUCB2, STAM, TOR1AIP2

### Function

No GO or KEGG term passed global correction, and there is no supplementary STRING enrichment. The module therefore does not support a statistically established pathway assignment. Its co-abundance pattern is nevertheless compatible with a mixed cellular program involving cell-cycle and chromosome-segregation activity through CENPF, centrosome and Golgi-associated organization through AKAP9, endosomal and cytokine-receptor trafficking through STAM, nucleolar and ubiquitin-linked RNA-processing functions through DCAF13, and secretory or calcium-associated biology through NUCB2. Because these functions are diverse and the network is sparse, the most cautious interpretation is a shared cellular-state or cell-composition signal rather than a defined biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only NUCB2 is annotated as secreted to blood. Most genes are intracellular, with nuclear, nucleolar, Golgi, vesicular, endoplasmic-reticulum, or nuclear-membrane localizations. HPA shows bone-marrow protein detection for nearly all genes with available data, while autonomic-nervous-system protein data are unavailable. Every gene has a cell-type-enhanced annotation, including erythrocyte progenitors, neutrophil progenitors, innate lymphoid cells, mast cells, and T-reg cells, although several annotations also involve reproductive, epithelial, or sensory cell types. The module therefore may partly reflect bone-marrow cellular composition or a shared progenitor-related state rather than a tissue-wide autonomic program. Its mixed tissue and cell-type pattern argues against treating it as a uniform blood-cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING relationship met the supplied confidence threshold, and no STRING functional enrichment was reported. No hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not corroborated here as established physical or functional protein interactions. The absence of STRING or hu.MAP support does not exclude indirect regulation, context-specific interactions, transient complexes, or correlated expression caused by shared cell composition. It does mean that the module should be interpreted as a transcript or protein-abundance association rather than as a demonstrated molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The tissue-pair co-abundance pattern could be a new observation, but the fact sheet is insufficient to establish that it is a new biological mechanism. The lack of STRING and hu.MAP representation is only weakly supportive of novelty because those resources emphasize known physical or curated relationships and may miss tissue-specific or indirect associations. The absence of globally significant GO or KEGG enrichment also prevents a claim that the module defines a novel pathway. A defensible novelty statement is that this particular cross-tissue association may be under-characterized, while its component functions are individually established and heterogeneous.

**Hypothesis.** Hypothesis: the module reflects a shared abundance state of bone-marrow-associated or progenitor-related cells that combines proliferative and chromosome-segregation activity with intracellular trafficking, centrosome organization, and regulated secretion. CENPF and possibly DCAF13 may mark proliferative or biosynthetic state, AKAP9 may connect that state to centrosome and Golgi organization, STAM may represent cytokine-receptor and endosomal trafficking, and NUCB2 may represent a secretory component. C5orf22 may act as the abundance-network bridge linking these otherwise distinct processes. This hypothesis predicts that the module will track cell-state or cell-mixture variation more strongly than a single pathway, and it requires validation with cell deconvolution, independent cohorts, and perturbation or interaction assays.

### Important genes

#### C5orf22

- **Related proteins** (co-abundance neighbors): NUCB2 (0.92), AKAP9 (0.86), DCAF13 (0.86), STAM (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Nuclear membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromosome 5 open reading frame 22
- **Diseases (Open Targets)**: gout (0.281); neurodegenerative disease (0.263); non-autoimmune hemolytic anemia (0.095); Vertigo (0.091); actinic keratosis (0.057)
- **Europe PMC papers**: 70
- **Why important**: C5orf22 is the central network connector, linking NUCB2, AKAP9, DCAF13, and STAM. It has bone-marrow detection, mast-cell enhancement, and basophil enrichment in HPA, making it a plausible marker of the cell-composition component. Its functional annotation is sparse, while disease-association signals include gout, neurodegenerative disease, hemolytic anemia, and vertigo. The relatively limited literature compared with the better-established module genes makes it especially relevant for follow-up.
- **Conclusion**: Established evidence supports C5orf22 as the network bridge and as a bone-marrow-associated, mast-cell or basophil-linked marker. Its molecular function in this module remains unresolved. A role as an organizer of the observed co-abundance state is a hypothesis, not an established mechanism.

#### AKAP9

- **Related proteins** (co-abundance neighbors): C5orf22 (0.86), CENPF (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: A-kinase anchoring protein 9. The A-kinase anchor proteins (AKAPs) are a group of structurally diverse proteins which have the common function of binding to the regulatory subunit of protein kinase A (PKA) and confining the holoenzyme to discrete locations within the cell. This gene encodes a member of the AKAP family. Alternate splicing of this gene results in at least two isoforms that localize to the centrosome and the Golg…
- **Diseases (Open Targets)**: cancer (0.547); long QT syndrome 11 (0.501); Prolonged QT interval (0.399); lymphangioma (0.243); hemangioma (0.243)
- **Europe PMC papers**: 1761
- **Why important**: AKAP9 is connected to C5orf22 and CENPF and has the strongest functional annotation among the network-organizing genes. Its known AKAP activity localizes protein kinase A and other signaling components, while its isoforms associate with the centrosome and Golgi apparatus. HPA reports cell-type enhancement in cone photoreceptors and bone-marrow protein detection. Its disease associations include long-QT and prolonged-QT phenotypes, and it has extensive literature.
- **Conclusion**: Established evidence supports AKAP9 as a centrosome, Golgi, and signaling scaffold with disease relevance. In this module, it could connect cellular organization to the abundance pattern, but a direct relationship with C5orf22 or CENPF is not established by the supplied STRING or hu.MAP evidence.

#### CENPF

- **Related proteins** (co-abundance neighbors): TOR1AIP2 (0.84), AKAP9 (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: centromere protein F. This gene encodes a protein that associates with the centromere-kinetochore complex. The protein is a component of the nuclear matrix during the G2 phase of interphase. In late G2 the protein associates with the kinetochore and maintains this association through early anaphase. It localizes to the spindle midzone and the intracellular bridge in late anaphase and telophase, respectively, and is tho…
- **Diseases (Open Targets)**: Stromme syndrome (0.818); female infertility (0.461); Neurodevelopmental delay (0.425); neurodegenerative disease (0.390); microcephalic primordial dwarfism (0.370)
- **Europe PMC papers**: 4616
- **Why important**: CENPF connects AKAP9 and TOR1AIP2 and is HPA group-enriched in bone marrow and lymphoid tissue. It is enhanced in erythrocyte progenitors and other proliferative or differentiating cell types. Its established functions include the mitotic cell cycle, chromosome segregation, spindle-checkpoint signaling, and G2-to-M transition. It has extensive literature and strong associations with Stromme syndrome, infertility, neurodevelopmental disease, and microcephalic primordial dwarfism.
- **Conclusion**: Established evidence supports CENPF as a marker and mediator of proliferative chromosome-segregation states. Its presence makes a progenitor or cell-cycle interpretation plausible, especially in bone marrow. It does not establish that the entire module is a cell-cycle pathway, because no global GO or KEGG enrichment passed correction.

#### STAM

- **Related proteins** (co-abundance neighbors): C5orf22 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal transducing adaptor molecule. This gene encodes a member of the signal-transducing adaptor molecule family. These proteins mediate downstream signaling of cytokine receptors and also play a role in ER to Golgi trafficking by interacting with the coat protein II complex. The encoded protein also associates with hepatocyte growth factor-regulated substrate to form the endosomal sorting complex required for transport-0 (ESCRT-0),…
- **Diseases (Open Targets)**: listeriosis (0.370); nonpapillary renal cell carcinoma (0.076); hypertensive disorder (0.065); essential hypertension (0.059); supranuclear palsy, progressive, 1 (0.056)
- **Europe PMC papers**: 5115
- **Why important**: STAM is bone-marrow tissue-enhanced, cell-type-enhanced in erythrocyte and neutrophil progenitors, and immune-cell-enhanced in T-reg cells. It is a vesicular protein involved in cytokine-receptor signaling, ER-to-Golgi trafficking, ESCRT-related endosomal sorting, multivesicular-body assembly, and exosomal secretion. It has extensive literature and disease associations involving listeriosis and other conditions. Its connection to the central C5orf22 node links immune or progenitor-associated trafficking to the rest of the module.
- **Conclusion**: Established evidence supports STAM as an endosomal and cytokine-signaling adaptor relevant to bone-marrow cell biology. Its module-level role may be to report immune or progenitor-cell composition and vesicle trafficking. A direct functional partnership with C5orf22 is only a hypothesis because it is absent from the supplied STRING and hu.MAP results.

#### NUCB2

- **Related proteins** (co-abundance neighbors): C5orf22 (0.92); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleobindin 2. This gene encodes a protein with a suggested role in calcium level maintenance, eating regulation in the hypothalamus, and release of tumor necrosis factor from vascular endothelial cells. This protein binds calcium and has EF-folding domains. [provided by RefSeq, Oct 2011].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.400); spondylosis (0.366); hypothyroidism (0.315); abdominal aortic aneurysm (0.294); obesity disorder (0.245)
- **Europe PMC papers**: 1073
- **Why important**: NUCB2 is the only module member annotated as secreted to blood and is connected to C5orf22. It is tissue-enhanced in pancreas and salivary gland, has several secretory or epithelial cell-type enhancements, and is detected in bone marrow. Its annotation supports calcium binding, small-GTPase-mediated signaling, eating regulation, and regulation of tumor-necrosis-factor release. It has substantial literature and disease associations involving skeletal abnormalities, spondylosis, hypothyroidism, abdominal aortic aneurysm, and obesity.
- **Conclusion**: Established evidence supports NUCB2 as a secreted or Golgi-associated calcium-binding protein with signaling and metabolic relevance. It may provide a circulating or secretory component to the module, but the data do not establish that NUCB2 mediates the shared autonomic-nervous-system and bone-marrow association.

## Module 7

**Tissue pair**: autonomic_nervous_system and bone_marrow  
**Genes (39)**: ALDH1B1, ATP5F1C, CTSC, CBX5, CERS6, CHURC1, TRIP10, CORO7, DAZAP1, ERO1A, GEMIN8, HACD3, HADH, IFIT5, INF2, ISYNA1, LSM5, MAN2B1, METAP2, MRI1, NDUFS7, NSFL1C, PFKP, PHF3, PPM1A, PSMD9, PTPN9, RECQL, RO60, SDHA, SEPTIN2, SMC2, SRI, SUPT16H, TNPO1, TPM1, EFTUD2, UBR7, ZC3H6

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. Therefore, the module does not support a single statistically established pathway-level label. Its gene content nevertheless suggests a mixed cellular-maintenance program. The strongest coherent signals are mitochondrial energy metabolism, RNA processing and spliceosomal function, lipid and ceramide metabolism, cytoskeletal or vesicular organization, and genome maintenance. CHURC1 is the central network connector, linking genes from these otherwise distinct functional areas. The network may therefore represent coordinated abundance of general cellular state rather than a narrowly specialized autonomic-nervous-system or bone-marrow pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a small secreted subset, and the listed proteins are predominantly intracellular, nuclear, mitochondrial, cytoskeletal, vesicular, or membrane-associated. Most genes have low tissue specificity, while many are cell-type enhanced rather than restricted to autonomic nervous tissue or bone marrow. Immune-cell specificity is generally low, with only limited enrichment involving plasmacytoid dendritic cells and monocyte or myeloid populations. HPA protein detection is broadly present in bone marrow, whereas no matching autonomic-nervous-system tissue result is available. Thus, the shared signal could reflect common cellular composition, proliferative or biosynthetic state, or technical sampling effects in addition to a true cross-tissue biological program. It should not be interpreted as a blood or plasma secretome module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a small set of high-confidence relationships rather than broad functional enrichment. The strongest established connections include EFTUD2 with LSM5, NDUFS7 with SDHA, and EFTUD2 with SDHA; ATP5F1C also connects to EFTUD2, NDUFS7, and SDHA. These relationships support real links among spliceosomal or RNA-processing machinery and mitochondrial respiratory proteins, but they do not by themselves demonstrate that all module genes form one physical complex. hu.MAP gives more specific support for a spliceosomal or snRNP-related group containing EFTUD2, GEMIN8, and LSM5 in (hu.MAP huMAP3_08980.1). ATP5F1C and CERS6 recur together in several hu.MAP complexes (hu.MAP huMAP3_07476.1) through (hu.MAP huMAP3_11095.1), although they are only partial representations of much larger complexes and therefore should not be treated as proof of a direct ATP synthase–ceramide synthase complex. TNPO1 and HACD3 co-occur in lipid or membrane associated hu.MAP complexes (hu.MAP huMAP3_06247.1) and (hu.MAP huMAP3_09592.1). Overall, the module contains several known substructures embedded in a broader co-abundance network, with CHURC1 connecting many genes for which no STRING or hu.MAP relationship is recorded.

**STRING interactions (score >= 0.7)**: 6 of 741 gene pairs: ATP5F1C–EFTUD2 (0.791); ATP5F1C–NDUFS7 (0.722); ATP5F1C–SDHA (0.75); EFTUD2–LSM5 (0.998); EFTUD2–SDHA (0.892); NDUFS7–SDHA (0.988)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (EFTUD2, GEMIN8, LSM5; 3/97); huMAP3_07476.1 (ATP5F1C, CERS6; 2/18); huMAP3_05994.1 (ATP5F1C, CERS6; 2/19); huMAP3_08393.1 (ATP5F1C, CERS6; 2/19); huMAP3_09775.1 (ATP5F1C, CERS6; 2/21); huMAP3_09307.1 (ATP5F1C, CERS6; 2/35); huMAP3_11095.1 (ATP5F1C, CERS6; 2/45); huMAP3_06247.1 (TNPO1, HACD3; 2/65); huMAP3_09592.1 (TNPO1, HACD3; 2/95)

### Novelty

The module is not established as a wholly new biological pathway. Several of its relationships and components are already known: EFTUD2, GEMIN8, and LSM5 participate in a spliceosomal or snRNP-related complex; ATP5F1C is part of mitochondrial ATP synthase; SDHA and NDUFS7 belong to respiratory-chain complexes; and CERS6 participates in ceramide synthesis. The potentially novel aspect is the specific cross-tissue co-abundance configuration linking these processes through CHURC1 and a set of otherwise weakly connected genes. However, absence from STRING or hu.MAP is not evidence of novelty, and the lack of globally significant GO/KEGG enrichment makes a strong novelty claim premature. This should be described as a candidate cross-tissue module configuration requiring replication and functional testing.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program in bone-marrow and autonomic-nervous-system samples in which mitochondrial energy production, lipid remodeling, RNA maturation, proteostasis, and cytoskeletal or vesicular trafficking are jointly regulated. CHURC1 may act as a network-level co-abundance bridge rather than a proven molecular scaffold. In bone marrow, the signal may arise from a mixture of progenitor, megakaryocytic, stromal, and other cells; in the autonomic nervous system, it may reflect metabolically active neural or supporting cells. A testable prediction is that module activity will track cellular metabolic or biosynthetic state and will change alongside spliceosome activity, mitochondrial respiration, and membrane-lipid remodeling, rather than mark a single lineage.

### Important genes

#### CHURC1

- **Related proteins** (co-abundance neighbors): SEPTIN2 (0.98), ALDH1B1 (0.96), IFIT5 (0.96), EFTUD2 (0.94), CORO7 (0.92), MRI1 (0.92), HADH (0.91), METAP2 (0.90), MAN2B1 (0.90), SRI (0.89), PPM1A (0.89), ATP5F1C (0.88), HACD3 (0.88), INF2 (0.88), NSFL1C (0.88), SMC2 (0.87), RECQL (0.86), UBR7 (0.85), SDHA (0.85), TRIP10 (0.84), TNPO1 (0.83), CBX5 (0.82), CTSC (0.82), ERO1A (0.81), NDUFS7 (0.81), RO60 (0.80), DAZAP1 (0.80), SUPT16H (0.80), PSMD9 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: churchill domain containing 1. Predicted to enable zinc ion binding activity. Predicted to be involved in positive regulation of transcription, DNA-templated. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: lung adenocarcinoma (0.075); neoplasm (0.059); alcohol drinking (0.023); stroke disorder (0.023); placental abruption (0.022)
- **Europe PMC papers**: 210
- **Why important**: CHURC1 is the dominant network connector, with links to genes involved in mitochondrial metabolism, RNA processing, cytoskeletal organization, lipid metabolism, and protein handling. It has a predicted zinc-binding and transcription-related role, is detected in bone marrow, and has relatively substantial literature compared with several less characterized module members. Its central position makes it the best candidate for explaining the module's integrated topology, although no direct STRING or hu.MAP partner is reported for it.
- **Conclusion**: Established evidence supports CHURC1 as the network hub and as a gene with predicted transcription-related molecular functions. It does not establish CHURC1 as the biochemical organizer of the module. The hypothesis that CHURC1 coordinates the other processes is therefore plausible but requires perturbation or independent co-expression validation.

#### SDHA

- **Related proteins** (co-abundance neighbors): CHURC1 (0.85), PFKP (0.80); STRING partners: ATP5F1C (0.75), EFTUD2 (0.892), NDUFS7 (0.988)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate dehydrogenase complex flavoprotein subunit A. This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identi…
- **Diseases (Open Targets)**: mitochondrial complex II deficiency, nuclear type 1 (0.813); pheochromocytoma/paraganglioma syndrome 5 (0.790); dilated cardiomyopathy 1GG (0.768); neurodegeneration with ataxia and late-onset optic atrophy (0.761); gastrointestinal stromal tumor (0.743)
- **Europe PMC papers**: 12756
- **Why important**: SDHA is a catalytic subunit of mitochondrial respiratory complex two and participates in the tricarboxylic acid cycle and electron transport. It has STRING links to ATP5F1C, EFTUD2, and NDUFS7, providing one of the clearest known interaction backbones in the module. It is enhanced in heart and skeletal muscle and has extensive disease literature, including mitochondrial deficiency and tumor-associated disease.
- **Conclusion**: Established evidence supports SDHA as a mitochondrial energy-metabolism component and as part of a known respiratory-chain interaction neighborhood. Its co-abundance with spliceosomal genes does not prove direct metabolic control of RNA processing; that cross-process interpretation remains a hypothesis about shared cellular state.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): CHURC1 (0.94), RECQL (0.85); STRING partners: ATP5F1C (0.791), LSM5 (0.998), SDHA (0.892)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 is a spliceosomal GTPase involved in spliceosome assembly and conformational transitions. It belongs to hu.MAP complex (hu.MAP huMAP3_08980.1) with GEMIN8 and LSM5 and has high-confidence STRING connections to LSM5 and SDHA, as well as a connection to ATP5F1C. It has a well-developed literature and a clear disease association with mandibulofacial dysostosis with microcephaly.
- **Conclusion**: Established evidence supports EFTUD2 as a core RNA-splicing factor and as a bridge between a known spliceosomal group and the respiratory-associated portion of the network. It is not established that this module changes spliceosome activity in either tissue; that functional consequence must be tested directly.

#### LSM5

- **Related proteins** (co-abundance neighbors): PHF3 (0.92), ISYNA1 (0.90); STRING partners: EFTUD2 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: LSM5 homolog, U6 small nuclear RNA and mRNA degradation associated. Sm-like proteins were identified in a variety of organisms based on sequence homology with the Sm protein family (see SNRPD2; MIM 601061). Sm-like proteins contain the Sm sequence motif, which consists of 2 regions separated by a linker of variable length that folds as a loop. The Sm-like proteins are thought to form a stable heteromer present in tri-snRNP particles, which are important for pre-mR…
- **Diseases (Open Targets)**: neurodegenerative disease (0.499); food allergy (0.218); protozoa infectious disease (0.210); mathematical ability (0.206); intelligence (0.183)
- **Europe PMC papers**: 1988
- **Why important**: LSM5 is a Sm-like RNA-processing protein involved in spliceosomal snRNP assembly, tri-snRNP function, mRNA splicing, and RNA decay. It is present with EFTUD2 and GEMIN8 in hu.MAP complex (hu.MAP huMAP3_08980.1), and its STRING relationship with EFTUD2 is especially strong. Its extensive literature supports an established role in RNA metabolism, while its network degree is modest but biologically specific.
- **Conclusion**: Established evidence supports LSM5 as a spliceosomal and RNA-decay component that helps validate the RNA-processing arm of the module. The module does not establish a novel LSM5 function in autonomic nervous tissue or bone marrow, so any tissue-specific role remains hypothetical.

#### ATP5F1C

- **Related proteins** (co-abundance neighbors): CHURC1 (0.88); STRING partners: EFTUD2 (0.791), NDUFS7 (0.722), SDHA (0.75)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_07476.1, huMAP3_05994.1, huMAP3_08393.1, huMAP3_09775.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit gamma. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: late-onset Alzheimers disease (0.350); scleritis (0.189); diaphragm disorder (0.082); glioblastoma (0.044); external ear disorder (0.042)
- **Europe PMC papers**: 306
- **Why important**: ATP5F1C encodes the gamma subunit of mitochondrial ATP synthase and is linked to oxidative phosphorylation and proton-motive-force-driven ATP synthesis. It has STRING relationships with EFTUD2, NDUFS7, and SDHA and appears with CERS6 in multiple hu.MAP complexes (hu.MAP huMAP3_07476.1) through (hu.MAP huMAP3_11095.1). This makes it a useful representative of the energetic and membrane-associated portion of the module, despite its limited direct network degree.
- **Conclusion**: Established evidence supports ATP5F1C as an ATP-synthase component and as part of a known mitochondrial interaction neighborhood. Its association with CERS6 and spliceosomal genes in this module is co-abundance evidence, not proof of a direct shared complex or causal regulation.

#### CERS6

- **Related proteins** (co-abundance neighbors): ISYNA1 (0.97); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_07476.1, huMAP3_05994.1, huMAP3_08393.1, huMAP3_09775.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ceramide synthase 6. Enables sphingosine N-acyltransferase activity. Involved in ceramide biosynthetic process. Located in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.349); frozen shoulder (0.306); type 2 diabetes mellitus (0.306); respiratory tract infectious disorder (0.280); sleep apnea syndrome (0.277)
- **Europe PMC papers**: 1355
- **Why important**: CERS6 is a ceramide synthase involved in sphingolipid and ceramide biosynthesis. It is linked in the module to ISYNA1 and repeatedly co-occurs with ATP5F1C in hu.MAP complexes (hu.MAP huMAP3_07476.1) through (hu.MAP huMAP3_11095.1). Its HPA profile includes plasmacytoid dendritic-cell enrichment and several non-blood cell-type signals, making it relevant to both lipid remodeling and possible cell-composition effects.
- **Conclusion**: Established evidence supports CERS6 as a membrane lipid-biosynthesis enzyme and supports its recurring complex-context association with ATP5F1C. The module does not establish that ceramide remodeling drives mitochondrial or spliceosomal co-abundance; that is a testable mechanistic hypothesis.

## Module 8

**Tissue pair**: autonomic_nervous_system and bone_marrow  
**Genes (21)**: ALG1, ARHGEF2, COPS3, DHCR7, FDFT1, KIF14, KLC1, LAS1L, TRIP13, PRPF39, PSMB3, RWDD4, RXRA, SAAL1, SPTBN1, UTP14A, WDR18, XPO7, ZC3H7A, ZC3H4, ZNFX1

### Function

No GO or KEGG term passed global correction, so the module cannot be assigned a statistically supported pathway label from enrichment. Its gene-level annotations instead indicate a mixed cellular program involving nuclear transcriptional regulation through RXRA, cholesterol and sterol metabolism through DHCR7 and FDFT1, ribosome biogenesis through LAS1L, WDR18 and UTP14A, nucleocytoplasmic transport through XPO7, RNA processing through PRPF39 and ZC3H4, proteostasis through PSMB3 and COPS3, and cell division or cytoskeletal processes through KIF14, TRIP13, ARHGEF2 and SPTBN1. RXRA is the dominant network hub, with the remaining genes forming mostly hub-centered associations rather than a densely interconnected pathway. The most defensible interpretation is therefore a coordinated abundance pattern of broadly used cellular machinery, with possible contributions from lipid metabolism, biosynthetic capacity, RNA processing and proliferative state, rather than a single established biological process.

**Cell composition.** The module is not dominated by plasma or secreted proteins: no module gene is annotated as secreted. It is also not strongly blood-cell specific. Most genes have low tissue specificity and low immune-cell specificity, although many show enhancement in particular cell types. Bone-marrow protein detection is common among the assayed genes, while the available HPA summary has no matching autonomic-nervous-system tissue. The presence of RXRA in neutrophil- and monocyte-associated cell contexts, together with occasional neutrophil enrichment, leaves open a contribution from shared marrow cell populations, but the overall profile does not support a simple blood-contamination explanation. The pattern is more consistent with broadly expressed intracellular proteins combined with cell-state or cell-composition effects. Enrichment in reproductive and other specialized cell types should also be treated as evidence of cell-type expression patterns, not as evidence that those tissues drive this shared module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides four high-confidence pairwise relationships. DHCR7 is linked to FDFT1, supporting a known connection between two enzymes in sterol and cholesterol biosynthesis. LAS1L is linked to WDR18, and WDR18 is also linked to UTP14A, supporting a ribosome-biogenesis or RNA-processing neighborhood. KIF14 is linked to TRIP13, consistent with a cell-division and chromosome-segregation relationship. hu.MAP independently places TRIP13, ALG1 and DHCR7 together in one complex, although this is only a partial overlap and does not establish that the entire module is that complex. Multiple hu.MAP complexes contain LAS1L and WDR18, reinforcing their association with recurring ribosome-biogenesis assemblies. Other hu.MAP complexes contain SAAL1 and XPO7, but the overlap is limited and therefore supports only a possible shared transport or cellular-machinery context. There was no STRING functional enrichment. Overall, the external interaction evidence validates several local pairs and submodules, while the hub-centered co-abundance structure is substantially broader than the known physical interaction structure.

**STRING interactions (score >= 0.7)**: 4 of 210 gene pairs: DHCR7–FDFT1 (0.938); KIF14–TRIP13 (0.744); LAS1L–WDR18 (0.991); UTP14A–WDR18 (0.777)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06791.1 (TRIP13, ALG1, DHCR7; 3/31); huMAP3_05508.1 (WDR18, LAS1L; 2/4); huMAP3_03787.1 (WDR18, LAS1L; 2/5); huMAP3_07191.1 (WDR18, LAS1L; 2/6); huMAP3_11063.1 (WDR18, LAS1L; 2/8); huMAP3_07162.1 (WDR18, LAS1L; 2/9); huMAP3_05832.1 (SAAL1, XPO7; 2/14); huMAP3_09114.1 (SAAL1, XPO7; 2/30); huMAP3_10202.1 (SAAL1, XPO7; 2/52); huMAP3_10287.1 (SAAL1, XPO7; 2/53); huMAP3_11232.1 (SAAL1, XPO7; 2/78); huMAP3_09592.1 (ALG1, DHCR7; 2/95)

### Novelty

This may be a new tissue-pair co-abundance observation, but it should not be called a newly discovered molecular complex or pathway. The module combines established relationships involving sterol synthesis, ribosome biogenesis and mitotic machinery with many genes lacking recorded STRING or hu.MAP links to the other module members. That combination, and its reproducible appearance across autonomic nervous system and bone marrow in the supplied analysis, could be novel as a co-abundance pattern. However, absence from STRING or hu.MAP does not demonstrate novelty: some associations may be indirect, context dependent, abundance-driven, incompletely studied or caused by shared cell composition. The lack of globally significant GO/KEGG enrichment further argues for cautious description as a data-derived module rather than a newly established biological pathway.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in which RXRA-associated transcriptional regulation is co-varying with biosynthetic and maintenance demands. In this model, sterol production through DHCR7 and FDFT1, ribosome maturation through the LAS1L-WDR18-UTP14A neighborhood, RNA and nuclear transport through PRPF39, ZC3H4 and XPO7, and proteasome or signal-regulatory machinery through PSMB3 and COPS3 are coordinated by the abundance of a common intracellular cell state. KIF14 and TRIP13 may mark a proliferative or chromosome-maintenance component, while ARHGEF2 and SPTBN1 may reflect cytoskeletal remodeling. The module could therefore arise from shared progenitor or proliferative cell states represented in both tissues, with RXRA acting as a network-level regulatory correlate. This is a hypothesis generated from co-abundance and annotations, not a demonstrated causal mechanism.

### Important genes

#### RXRA

- **Related proteins** (co-abundance neighbors): ARHGEF2 (0.92), ZC3H4 (0.91), ALG1 (0.90), DHCR7 (0.88), ZC3H7A (0.87), UTP14A (0.86), SAAL1 (0.86), PSMB3 (0.85), TRIP13 (0.85), FDFT1 (0.85), LAS1L (0.85), RWDD4 (0.84), ZNFX1 (0.83), SPTBN1 (0.81), XPO7 (0.81), WDR18 (0.80), COPS3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: retinoid X receptor alpha. Retinoid X receptors (RXRs) and retinoic acid receptors (RARs) are nuclear receptors that mediate the biological effects of retinoids by their involvement in retinoic acid-mediated gene activation. These receptors function as transcription factors by binding as homodimers or heterodimers to specific sequences in the promoters of target genes. The protein encoded by this gene is a member of the ste…
- **Diseases (Open Targets)**: psoriasis (0.583); primary cutaneous T-cell non-Hodgkin lymphoma (0.551); psoriasis vulgaris (0.517); urinary bladder cancer (0.507); neoplasm (0.480)
- **Europe PMC papers**: 5301
- **Why important**: RXRA is the central network hub, connecting to nearly every other module member and therefore providing the strongest organizing signal in the co-abundance graph. Established annotation identifies it as a retinoid and steroid hormone receptor family transcription factor involved in retinoid-mediated gene activation, hormone signaling, transcriptional regulation and nervous-system development. It is broadly expressed, detected in bone marrow, and associated with neutrophil- and monocyte-related cell contexts. Its large literature base and disease associations make it the best candidate for interpreting the module as a regulatory state rather than as a single physical complex.
- **Conclusion**: Established evidence supports RXRA as the module's principal network-level correlate and a plausible transcriptional regulator of cellular state. It is not established that RXRA directly controls the other module genes in this tissue pair. A causal RXRA-centered mechanism remains a hypothesis.

#### DHCR7

- **Related proteins** (co-abundance neighbors): RXRA (0.88); STRING partners: FDFT1 (0.938)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_06791.1, huMAP3_09592.1
- **Function (MyGene.info)**: 7-dehydrocholesterol reductase. This gene encodes an enzyme that removes the C(7-8) double bond in the B ring of sterols and catalyzes the conversion of 7-dehydrocholesterol to cholesterol. This gene is ubiquitously expressed and its transmembrane protein localizes to the endoplasmic reticulum membrane and nuclear outer membrane. Mutations in this gene cause Smith-Lemli-Opitz syndrome (SLOS); a syndrome that is metabolically cha…
- **Diseases (Open Targets)**: Smith-Lemli-Opitz syndrome (0.867); hereditary disease (0.550); neurodegenerative disease (0.477); Intellectual disability (0.464); cataract (0.464)
- **Europe PMC papers**: 3788
- **Why important**: DHCR7 is part of the strongest STRING-supported metabolic pair with FDFT1 and is also present in hu.MAP complexes overlapping ALG1 and TRIP13. Its established function is conversion of a sterol precursor to cholesterol in the endoplasmic reticulum, and it is linked to cholesterol and sterol biosynthesis and Smith-Lemli-Opitz syndrome. It is tissue enhanced in liver, detected in bone marrow, and has substantial literature support. Its position near the RXRA hub connects lipid metabolism to the broader module.
- **Conclusion**: Established evidence supports DHCR7 as a meaningful sterol-biosynthesis component and as a validated local relationship with FDFT1. The module does not establish that sterol metabolism is its dominant function, because no GO or KEGG term passed global correction. Any RXRA-mediated regulation of this metabolic branch is a hypothesis.

#### FDFT1

- **Related proteins** (co-abundance neighbors): RXRA (0.85); STRING partners: DHCR7 (0.938)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: farnesyl-diphosphate farnesyltransferase 1. This gene encodes a membrane-associated enzyme located at a branch point in the mevalonate pathway. The encoded protein is the first specific enzyme in cholesterol biosynthesis, catalyzing the dimerization of two molecules of farnesyl diphosphate in a two-step reaction to form squalene. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: squalene synthase deficiency (0.519); Hypercholesterolemia (0.398); Abnormality of the skeletal system (0.353); inherited lipid metabolism disorder (0.324); myopathy (0.281)
- **Europe PMC papers**: 2443
- **Why important**: FDFT1 forms the strongest STRING-supported pair in the module with DHCR7 and catalyzes a branch-point reaction in the mevalonate pathway leading toward squalene and cholesterol biosynthesis. It is detected in bone marrow and has substantial literature and disease-association support. Although its direct module connectivity is limited, its biochemical complementarity with DHCR7 makes it more informative than an isolated hub-centered association.
- **Conclusion**: Established evidence supports FDFT1 as a cholesterol and lipid-biosynthesis enzyme linked to DHCR7. The co-abundance data support a local sterol-metabolism signal but do not prove pathway activation, coordinated flux, or a causal role in the shared tissue-pair module.

#### LAS1L

- **Related proteins** (co-abundance neighbors): RXRA (0.85); STRING partners: WDR18 (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_05508.1, huMAP3_03787.1, huMAP3_07191.1, huMAP3_11063.1, huMAP3_07162.1
- **Function (MyGene.info)**: LAS1 like ribosome biogenesis factor. Enables RNA binding activity. Predicted to be involved in maturation of 5.8S rRNA and maturation of LSU-rRNA. Located in membrane. Part of MLL1 complex. Implicated in Wilson-Turner syndrome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Wilson-Turner syndrome (0.658); spinal muscular atrophy with respiratory distress type 2 (0.370); hereditary disease (0.296); Global developmental delay (0.259); neurodevelopmental disorder (0.119)
- **Europe PMC papers**: 286
- **Why important**: LAS1L is repeatedly represented with WDR18 across several hu.MAP complexes and has a high-confidence STRING relationship with WDR18. Its established function is maturation of ribosomal RNA, particularly processing associated with the large ribosomal subunit, and it is linked to developmental disease. It is detected in bone marrow and has a cellular localization compatible with nuclear RNA processing. The repeated complex overlap gives this pair stronger structural support than most of the module's hub-centered edges.
- **Conclusion**: Established evidence supports LAS1L as part of ribosome-biogenesis machinery and supports its physical or functional association with WDR18. The module is consistent with variation in biosynthetic or proliferative demand, but it does not prove that ribosome biogenesis explains the whole module.

#### WDR18

- **Related proteins** (co-abundance neighbors): RXRA (0.80); STRING partners: LAS1L (0.991), UTP14A (0.777)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05508.1, huMAP3_03787.1, huMAP3_07191.1, huMAP3_11063.1, huMAP3_07162.1
- **Function (MyGene.info)**: WD repeat domain 18. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.417); ovarian neoplasm (0.263); COVID-19 (0.025); age-related macular degeneration (0.025); Alzheimer disease (0.023)
- **Europe PMC papers**: 245
- **Why important**: WDR18 is linked to LAS1L and UTP14A by high-confidence STRING relationships and recurs with LAS1L in multiple hu.MAP complexes. Its established annotations include rRNA processing and DNA replication, while its WD-repeat architecture is compatible with multiprotein-complex assembly. It therefore bridges the best-supported ribosome-biogenesis neighborhood in the module and provides a useful structural marker for interpreting the module's intracellular maintenance component.
- **Conclusion**: Established evidence supports WDR18 as a component of RNA-processing and ribosome-related machinery with known relationships to LAS1L and UTP14A. Its absence from bone-marrow protein detection in the supplied HPA record cautions against equating transcript or co-abundance with measured protein presence. A role in coordinating the full module is hypothetical.

#### TRIP13

- **Related proteins** (co-abundance neighbors): RXRA (0.85); STRING partners: KIF14 (0.744)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06791.1
- **Function (MyGene.info)**: thyroid hormone receptor interactor 13. This gene encodes a protein that interacts with thyroid hormone receptors, also known as hormone-dependent transcription factors. The gene product interacts specifically with the ligand binding domain. This gene is one of several that may play a role in early-stage non-small cell lung cancer. [provided by RefSeq, Oct 2009].
- **Diseases (Open Targets)**: mosaic variegated aneuploidy syndrome 3 (0.699); oocyte maturation defect 9 (0.600); neurodegenerative disease (0.555); mosaic variegated aneuploidy syndrome (0.503); Wilms tumor (0.375)
- **Europe PMC papers**: 1557
- **Why important**: TRIP13 has a STRING relationship with KIF14 and appears with KIF14 and DHCR7 in a hu.MAP complex. Its established annotations include the spindle assembly checkpoint, double-strand-break repair, meiotic processes and spermatogenesis. It is also associated with mosaic variegated aneuploidy and oocyte maturation disorders. Although its direct network connectivity is limited and it is not detected in bone marrow in the supplied HPA record, the KIF14 relationship gives the module a recognizable chromosome-maintenance and cell-division component.
- **Conclusion**: Established evidence supports TRIP13 as a chromosome-surveillance and cell-division factor and supports a local relationship with KIF14. Its participation in a shared autonomic-nervous-system and bone-marrow state is not established; a proliferative-cell-state interpretation remains a hypothesis.

## Module 9

**Tissue pair**: autonomic_nervous_system and bone_marrow  
**Genes (18)**: ARL3, CETN3, CWC15, SPECC1L, DIAPH3, EXOC5, GATC, GLOD4, GNA13, SLC2A1, PAXX, PDCL, SLC12A2, SERPINB6, TFCP2, METTL1, TTK, WAPL

### Function

No GO or KEGG term passed global correction. Therefore, the module does not have a statistically established pathway-level function from enrichment analysis. The gene-level annotations suggest a mixed cellular program involving mitotic control and chromosome segregation through TTK and WAPL, cytoskeletal remodeling and cell adhesion through DIAPH3 and SPECC1L, vesicle trafficking and membrane delivery through EXOC5 and ARL3, RNA modification and processing through METTL1 and CWC15, and signaling or transport through GNA13, PDCL, SLC2A1, and SLC12A2. These convergent annotations are biologically suggestive but are not equivalent to significant module enrichment. The co-abundance structure may therefore represent a coordinated cellular-state program rather than a single defined pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the fact sheet identifies no secreted genes. Most genes have low tissue specificity and low immune-cell specificity, so the module is not strongly characteristic of one circulating blood-cell lineage. Nevertheless, bone marrow is repeatedly represented among tissue-enhanced or protein-detected contexts, and several genes are associated with erythrocyte progenitors, megakaryocyte progenitors, myeloid cells, or pDCs. Testis and germ-cell states are also prominent in the HPA annotations, with additional trophoblast-associated signals. This mixture argues against interpreting the module as a dedicated autonomic-nervous-system program. It may instead reflect shared proliferative, cytoskeletal, vesicular, or housekeeping-like cellular states in the sampled tissues, with a possible contribution from bone-marrow cellular composition. The absence of matching autonomic-nervous-system HPA tissue data limits direct protein-level comparison between the two tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and no STRING functional-enrichment result was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated here as known high-confidence physical interactions or as membership in a recognized multi-protein complex. This does not invalidate the module: co-abundance can arise from shared regulation, cell-state composition, pathway convergence, or indirect biological coupling. It does mean that the network should be interpreted as an expression or abundance relationship rather than a validated protein-interaction network. Some individual gene annotations describe known functions, such as the exocyst role of EXOC5, checkpoint activity of TTK, and G-protein signaling involving GNA13 and PDCL, but those annotations do not establish direct interactions among the module members.

**STRING interactions (score >= 0.7)**: 0 of 153 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a novel cross-tissue co-abundance observation because the supplied resources do not identify a matching STRING interaction pattern or hu.MAP complex. However, absence from STRING or hu.MAP alone cannot establish biological novelty, and the module combines broadly expressed genes with functions that are already well documented individually. The strongest defensible conclusion is that this particular shared autonomic-nervous-system and bone-marrow abundance pattern is hypothesis-generating and not shown here to be an established canonical module. Demonstrating a new biological mechanism would require replication in independent cohorts, assessment of cell-composition effects, comparison with published co-expression modules, and experimental validation.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular-state program present in proliferative or differentiating cells, particularly in bone marrow, that couples mitotic surveillance and chromosome organization with cytoskeletal remodeling, vesicle trafficking, and metabolic or membrane transport demands. TTK and WAPL could mark cell-cycle and chromosome-management activity; DIAPH3, EXOC5, ARL3, GNA13, and SLC12A2 could coordinate cytoskeletal, membrane, and trafficking behavior; and METTL1, CWC15, and TFCP2 could support RNA maturation, translational capacity, or lineage-related transcription. The apparent sharing between the two tissues may therefore reflect common cell states or cellular composition rather than a specialized autonomic-neural mechanism. This is a hypothesis, not a demonstrated causal model.

### Important genes

#### TTK

- **Related proteins** (co-abundance neighbors): EXOC5 (0.87), ARL3 (0.86), WAPL (0.83), GLOD4 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TTK protein kinase. This gene encodes a dual specificity protein kinase with the ability to phosphorylate tyrosine, serine and threonine. Associated with cell proliferation, this protein is essential for chromosome alignment at the centromere during mitosis and is required for centrosome duplication. It has been found to be a critical mitotic checkpoint protein for accurate segregation of chromosomes during mitosis. …
- **Diseases (Open Targets)**: neurodegenerative disease (0.551); Alzheimer disease (0.380); Parkinson disease (0.375); lysosomal storage disease (0.375); ulna fracture (0.300)
- **Europe PMC papers**: 4437
- **Why important**: TTK is among the most connected genes in the module and links EXOC5, ARL3, WAPL, and GLOD4. Its established function in the mitotic spindle assembly checkpoint, chromosome alignment, centrosome duplication, and chromosome segregation gives the module a plausible proliferative-cell interpretation. HPA places it in bone marrow and lymphoid tissue and in erythrocyte and megakaryocyte progenitor contexts. It also has extensive literature and disease-association coverage, making it a strong biological anchor.
- **Conclusion**: Established evidence supports TTK as a mitotic checkpoint and chromosome-segregation regulator that is relevant to proliferative progenitor states. Its central co-abundance position is consistent with, but does not prove, a cell-cycle component of this module. It should be treated as an anchor gene rather than evidence that the entire module is a mitotic pathway.

#### EXOC5

- **Related proteins** (co-abundance neighbors): DIAPH3 (0.93), PDCL (0.87), TTK (0.87), GNA13 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exocyst complex component 5. The protein encoded by this gene is a component of the exocyst complex, a multiple protein complex essential for targeting exocytic vesicles to specific docking sites on the plasma membrane. Though best characterized in yeast, the component proteins and functions of exocyst complex have been demonstrated to be highly conserved in higher eukaryotes. At least eight components of the exocyst complex,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); placental abruption (0.305); thyroid cancer (0.143); injury (0.095); placenta praevia (0.087)
- **Europe PMC papers**: 321
- **Why important**: EXOC5 has the highest connectivity in the module and links DIAPH3, PDCL, TTK, and GNA13. Its established role as an exocyst-complex component connects the module to exocytosis, post-Golgi vesicle transport, membrane targeting, and membrane fission. HPA detects its protein in bone marrow, and its position connects the trafficking-related part of the network with the mitotic and G-protein-related portions.
- **Conclusion**: Established evidence supports EXOC5 as a membrane-trafficking and exocyst component. The network makes it a plausible integrator of vesicle delivery with cytoskeletal or signaling states, but the co-abundance data do not demonstrate that it physically interacts with the neighboring module genes or causally organizes the module.

#### DIAPH3

- **Related proteins** (co-abundance neighbors): PAXX (0.94), EXOC5 (0.93), SLC12A2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Microtubules; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: diaphanous related formin 3. This gene encodes a member of the diaphanous subfamily of the formin family. Members of this family are involved in actin remodeling and regulate cell movement and adhesion. Mutations in this gene are associated with autosomal dominant auditory neuropathy 1. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss (0.574); smoking initiation (0.376); insomnia (0.342); metabolic syndrome X (0.319); endometriosis (0.314)
- **Europe PMC papers**: 1094
- **Why important**: DIAPH3 is highly connected and links PAXX, EXOC5, and SLC12A2. Its established formin activity supports actin-filament polymerization, cytoskeletal organization, cell movement, and adhesion. HPA associates it with bone marrow, testis, erythrocyte progenitors, and several germ-cell states. Its disease association with auditory neuropathy also provides a well-defined functional context for cytoskeletal control.
- **Conclusion**: Established evidence supports DIAPH3 as a cytoskeletal remodeling factor. Its connection to EXOC5 and SLC12A2 makes a coordinated membrane-cytoskeleton state plausible, but this remains an interpretation of abundance relationships rather than proof of a shared DIAPH3-dependent mechanism.

#### TFCP2

- **Related proteins** (co-abundance neighbors): METTL1 (0.84), SLC2A1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transcription factor CP2. This gene encodes a transcription factor that binds the alpha-globin promoter and activates transcription of the alpha-globin gene. The encoded protein regulates erythroid gene expression, plays a role in the transcriptional switch of globin gene promoters, and it activates many other cellular and viral gene promoters. The gene product interacts with certain inflammatory response factors, and poly…
- **Diseases (Open Targets)**: hypertensive disorder (0.155); hepatocellular carcinoma (0.103); familial pancreatic carcinoma (0.102); pancreatic neoplasm (0.102); melanoma (0.095)
- **Europe PMC papers**: 716
- **Why important**: TFCP2 connects METTL1 with SLC2A1 and is an established transcription factor involved in alpha-globin promoter activity and erythroid gene regulation. This gives the module a direct link to hematopoietic differentiation, particularly relevant to the bone-marrow context. Its disease-association record includes several neoplastic and metabolic conditions, while its literature volume is substantial enough to support a well-characterized regulatory role.
- **Conclusion**: Established evidence supports TFCP2 as a regulator of transcription with an important erythroid connection. It could help explain bone-marrow representation in the module, but the available data do not establish that TFCP2 drives the shared module or that its erythroid function accounts for the autonomic-nervous-system association.

#### GNA13

- **Related proteins** (co-abundance neighbors): EXOC5 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein subunit alpha 13. Predicted to enable D5 dopamine receptor binding activity; G-protein beta/gamma-subunit complex binding activity; and GTPase activity. Predicted to be involved in several processes, including Rho protein signal transduction; activation of phospholipase D activity; and multicellular organism aging. Predicted to act upstream of or within several processes, including branching involved in blood vesse…
- **Diseases (Open Targets)**: lymphoma (0.373); neurodegenerative disease (0.370); diffuse large B-cell lymphoma (0.306); ovarian dysfunction (0.212); neoplasm (0.188)
- **Europe PMC papers**: 1664
- **Why important**: GNA13 connects EXOC5 and occupies the module branch linking G-protein signaling to vesicle trafficking. Its established functions include heterotrimeric G-protein signaling and Rho-related signal transduction. HPA associates it with bone marrow and with myeloid, monocyte, macrophage, neutrophil, dendritic-cell, and platelet contexts. Its disease associations include lymphoma and neurodegenerative disease.
- **Conclusion**: Established evidence supports GNA13 as a signaling regulator with roles relevant to cytoskeletal and hematopoietic-cell behavior. Its module position makes it a plausible bridge between signaling and membrane trafficking, but the module does not establish a direct GNA13-dependent pathway or explain why the same abundance pattern appears in autonomic nervous system samples.

## Module 10

**Tissue pair**: autonomic_nervous_system and bone_marrow  
**Genes (16)**: ASF1A, ATAD3A, CKAP4, DDX54, DIS3L2, NAB2, NUP205, PAXBP1, RASA1, RPAP1, POLR3D, RPE, SMARCAD1, TBL3, TMOD2, ZMYND8

### Function

No GO or KEGG term passed global correction, so no statistically supported pathway function should be assigned from enrichment. The gene annotations nevertheless point to a broad nuclear and cellular-maintenance program rather than a specialized tissue pathway. The module contains regulators of transcription and chromatin, RNA processing and ribosome biogenesis, nucleocytoplasmic transport, mitochondrial organization, carbohydrate metabolism, and actin organization. NAB2 is the central network-connected gene and is annotated as a transcriptional repressor; ASF1A and SMARCAD1 support chromatin assembly and remodeling; RPAP1 and POLR3D connect the module to RNA polymerase activity; TBL3 and DDX54 support ribosomal RNA processing. The sparse network and absence of STRING functional enrichment indicate that this is best interpreted as a co-abundance pattern involving general gene-expression and cell-maintenance machinery, not as evidence for one unified biochemical pathway. The apparent neuronal contribution from TMOD2 and the vascular or developmental relevance of RASA1 are biologically notable but do not establish the module's overall function.

**Cell composition.** The module is not composed of plasma or secreted proteins: the supplied HPA summary reports no secreted genes. Most genes have low tissue specificity, and most have low immune-cell specificity, which is more consistent with broadly expressed intracellular proteins than with a blood-specific program. HPA nevertheless reports cell-type-enhanced expression for many genes across diverse cell types, including megakaryocytes, neutrophil progenitors, cardiomyocytes, trophoblast-related cells, and neural or glial cells. Only a small subset has immune-cell enhancement, while one gene is not detected in immune cells. Protein detection in bone marrow is mixed, and the autonomic-nervous-system comparison has no matching HPA tissue. Thus, the shared module could partly reflect broadly expressed cellular machinery present in multiple cell populations, with possible contributions from shared or variable cell composition; it does not look like a plasma-protein signature or a clearly blood-cell-restricted module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only one high-confidence relationship within the module, between DDX54 and TBL3. This relationship is concordant with their supplied annotations in RNA processing and ribosomal RNA maturation, and it gives limited direct support to an RNA-processing subcomponent. No STRING functional enrichment was reported, and the remaining module relationships are not supported by the supplied high-confidence STRING network. hu.MAP identifies POLR3D and RPAP1 together in several related transcriptional complexes, with varying confidence. These complexes contain many RNA polymerase, transcriptional-regulation, and assembly factors, so the repeated pairing supports a connection to transcriptional machinery, but only a small portion of each complex is represented in the module. The hu.MAP findings therefore support local complex membership rather than a complete transcriptional complex being captured by the module. Overall, known physical or complex relationships explain selected edges or gene pairs, while most of the co-abundance structure remains distinct from the available interaction annotations.

**STRING interactions (score >= 0.7)**: 1 of 120 gene pairs: DDX54–TBL3 (0.848)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09057.1 (POLR3D, RPAP1; 2/36); huMAP3_08487.1 (POLR3D, RPAP1; 2/37); huMAP3_06426.1 (POLR3D, RPAP1; 2/38); huMAP3_14318.1 (POLR3D, RPAP1; 2/58); huMAP3_11092.1 (POLR3D, RPAP1; 2/65)

### Novelty

This module should not be called a newly discovered molecular complex or pathway. Its component functions and the DDX54–TBL3 relationship are already represented in established biological knowledge, and POLR3D–RPAP1 occur together in multiple hu.MAP complexes. The module may still be a novel tissue-pair co-abundance observation because the supplied evidence shows a sparse cross-tissue module linking autonomic nervous system and bone marrow genes, while the available STRING and hu.MAP annotations do not explain most of its network edges. However, absence from those resources is not proof of novelty. A defensible conclusion is that the tissue-pair association may be novel or under-characterized, whereas the underlying gene functions and some relationships are established. A targeted search for the exact full gene combination would be needed to claim that this module has not previously been reported.

**Hypothesis.** Hypothesis: the shared module reflects coordinated abundance of a broadly expressed nuclear and cellular-maintenance program that supports transcriptional regulation, chromatin state, RNA maturation, and stress-sensitive cell growth in cells represented in both tissue groups. NAB2 may organize the observed co-abundance pattern through transcriptional repression, while POLR3D and RPAP1 mark a transcriptional-machinery component and TBL3 with DDX54 mark an RNA-processing component. RASA1, ATAD3A, and the other peripheral genes could connect this general program to cell proliferation, mitochondrial state, adhesion or vascular signaling, and lineage-specific physiology. This is a mechanistic model, not an enrichment result or demonstrated physical assembly; it should be tested by cell-type-resolved expression, perturbation of NAB2 or the transcriptional machinery, and validation of the module in independent autonomic-nervous-system and bone-marrow cohorts.

### Important genes

#### NAB2

- **Related proteins** (co-abundance neighbors): ASF1A (0.91), CKAP4 (0.89), ATAD3A (0.88), SMARCAD1 (0.87), TBL3 (0.86), RPE (0.85), PAXBP1 (0.85), RPAP1 (0.84), ZMYND8 (0.83), DDX54 (0.82), TMOD2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NGFI-A binding protein 2. This gene encodes a member of the family of NGFI-A binding (NAB) proteins, which function in the nucleus to repress transcription induced by some members of the EGR (early growth response) family of transactivators. NAB proteins can homo- or hetero-multimerize with other EGR or NAB proteins through a conserved N-terminal domain, and repress transcription through two partially redundant C-terminal …
- **Diseases (Open Targets)**: solitary fibrous tumor (0.379); meningioma (0.374); hemangiopericytoma (0.374); meninges hemangiopericytoma (0.372); T-cell prolymphocytic leukemia (0.370)
- **Europe PMC papers**: 2424
- **Why important**: NAB2 is the hub of the supplied co-abundance graph, connecting to many of the other module genes with consistently strong edge weights. Its annotation as an NGFI-A binding protein and transcriptional repressor provides a plausible regulatory center for a module otherwise rich in chromatin, transcription, RNA-processing, and nuclear proteins. It has low tissue specificity, bone-marrow protein detection, broad disease associations in the supplied Open Targets evidence, and substantial literature support.
- **Conclusion**: Established evidence supports NAB2 as the network anchor and a transcriptional regulator with broad cellular relevance. It is reasonable to hypothesize that NAB2 helps coordinate the module's abundance pattern, but the co-abundance graph does not prove that NAB2 physically regulates every connected gene or that it explains sharing between the two tissues.

#### POLR3D

- **Related proteins** (co-abundance neighbors): RASA1 (0.83), PAXBP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_09057.1, huMAP3_08487.1, huMAP3_06426.1, huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase III subunit D. This gene complements a temperature-sensitive mutant isolated from the BHK-21 Syrian hamster cell line. It leads to a block in progression through the G1 phase of the cell cycle at nonpermissive temperatures. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: placental abruption (0.083); autosomal dominant macrothrombocytopenia (0.063); hyperlipoproteinemia type V (0.058); hypertriglyceridemia 2 (0.053); apolipoprotein c-III deficiency (0.052)
- **Europe PMC papers**: 287
- **Why important**: POLR3D links the module to RNA polymerase transcription and is one of the two module genes recurring across the hu.MAP complexes. Its direct module connections include RASA1 and PAXBP1, and its supplied annotation includes transcription by RNA polymerase III, tRNA transcription, and innate-immune-related functions. It is detected in bone marrow and has relevant disease associations involving placental and hematologic traits.
- **Conclusion**: Established evidence supports POLR3D as a component of RNA polymerase machinery and as a local bridge between the module and known hu.MAP complexes. Its role as a driver of the cross-tissue module, or as a link between transcription and innate immune state in these samples, remains a hypothesis.

#### RPAP1

- **Related proteins** (co-abundance neighbors): NAB2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_09057.1, huMAP3_08487.1, huMAP3_06426.1, huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase II associated protein 1. This protein forms part of the RNA polymerase II (RNAPII) enzyme complex and may recruit RNAPII to chromatin through its interaction with acetylated histones. [provided by RefSeq, Jul 2012].
- **Diseases (Open Targets)**: neurodegenerative disease (0.523); type 2 diabetes mellitus (0.345); diabetes mellitus (0.227); Crohn disease (0.181); cardiac arrhythmia (0.157)
- **Europe PMC papers**: 268
- **Why important**: RPAP1 is the second module member repeatedly present with POLR3D in hu.MAP complexes and is annotated as an RNA polymerase II-associated protein that can recruit polymerase to chromatin. Its inclusion provides independent support for a transcriptional-machinery interpretation, even though it has only a peripheral direct connection in the co-abundance graph. It is detected in bone marrow and has literature and disease-association support.
- **Conclusion**: Established evidence supports RPAP1 as a transcription-associated factor and supports its local complex context with POLR3D. The module data do not establish whether RPAP1 is functionally active in the shared tissue program or merely co-varies because of cell composition.

#### TBL3

- **Related proteins** (co-abundance neighbors): NAB2 (0.86), NUP205 (0.80); STRING partners: DDX54 (0.848)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transducin beta like 3. The protein encoded by this gene has sequence similarity with members of the WD40 repeat-containing protein family. The WD40 group is a large family of proteins, which appear to have a regulatory function. It is believed that the WD40 repeats mediate protein-protein interactions and members of the family are involved in signal transduction, RNA processing, gene regulation, vesicular trafficking, c…
- **Diseases (Open Targets)**: Huntington disease (0.011); pulmonary fibrosis (0.004); infection (0.004); neoplasm (0.004); cancer (0.004)
- **Europe PMC papers**: 283
- **Why important**: TBL3 is connected to NAB2 and NUP205 in the module and has the only supplied STRING interaction with DDX54. Its nucleolar localization and annotations in ribosomal RNA processing and small-subunit biogenesis give the module a concrete RNA-maturation component. Its broad tissue specificity and lack of bone-marrow protein detection argue against treating it as a bone-marrow-specific marker.
- **Conclusion**: Established evidence supports TBL3 as a nucleolar RNA-processing factor and supports a known relationship with DDX54. It may represent a functional RNA-processing branch of the module, but the sparse interaction evidence does not support a claim that it forms a complete module complex.

#### RASA1

- **Related proteins** (co-abundance neighbors): DIS3L2 (0.84), POLR3D (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Basal body; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAS p21 protein activator 1. The protein encoded by this gene is located in the cytoplasm and is part of the GAP1 family of GTPase-activating proteins. The gene product stimulates the GTPase activity of normal RAS p21 but not its oncogenic counterpart. Acting as a suppressor of RAS function, the protein enhances the weak intrinsic GTPase activity of RAS proteins resulting in the inactive GDP-bound form of RAS, thereby allowin…
- **Diseases (Open Targets)**: capillary malformation-arteriovenous malformation 1 (0.831); capillary malformation-arteriovenous malformation syndrome (0.711); angioosteohypertrophic syndrome (0.629); Parkes Weber syndrome (0.557); Abnormality of the cardiovascular system (0.544)
- **Europe PMC papers**: 2891
- **Why important**: RASA1 is a direct module neighbor of POLR3D and DIS3L2 and is annotated as a RAS GTPase-activating protein involved in control of proliferation and differentiation. Its supplied functions include angiogenesis, vasculogenesis, cytokinesis, and cell-adhesion regulation. It has tissue-enhanced expression in placenta, several cell-type enhancements, bone-marrow protein detection, and strong vascular disease associations.
- **Conclusion**: Established evidence supports RASA1 as a signaling regulator with vascular, proliferative, and adhesion-related functions. Its presence suggests a possible interface between the module's nuclear machinery and cellular-state signaling, but that interface is inferential because the module contains no demonstrated RASA1 protein interaction with the transcriptional components.

#### ATAD3A

- **Related proteins** (co-abundance neighbors): NAB2 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase family AAA domain containing 3A. This gene encodes a ubiquitously expressed mitochondrial membrane protein that contributes to mitochondrial dynamics, nucleoid organization, protein translation, cell growth, and cholesterol metabolism. This gene is a member of the ATPase family AAA-domain containing 3 gene family which, in humans, includes two other paralogs. Naturally occurring mutations in this gene are associated with distinct…
- **Diseases (Open Targets)**: Harel-Yoon syndrome (0.824); pontocerebellar hypoplasia, hypotonia, and respiratory insufficiency syndrome, neonatal lethal (0.785); lactic acidosis (0.462); hereditary disease (0.418); isolated cerebellar hypoplasia/agenesis (0.342)
- **Europe PMC papers**: 879
- **Why important**: ATAD3A is connected to the central NAB2 node and contributes a mitochondrial dimension to an otherwise nuclear-heavy module. Its annotation includes mitochondrial dynamics, nucleoid organization, protein translation, cell growth, cholesterol metabolism, DNA-damage response, and antiviral innate immunity. It has bone-marrow protein detection, a broad disease record, and substantial literature support, including associations with severe neurological syndromes.
- **Conclusion**: Established evidence supports ATAD3A as a mitochondrial and cellular-stress regulator. Its co-abundance with NAB2 may indicate coordination between nuclear regulation and mitochondrial state, but this remains a hypothesis rather than a demonstrated mechanism for the shared module.

## Module 11

**Tissue pair**: autonomic_nervous_system and bone_marrow  
**Genes (36)**: MT-ATP6, ATP5MK, MTHFD1, CCM2, CLTC, COG2, DDX21, DHX9, FKBP10, FDPS, FSCN1, GIPC1, SHMT2, GUF1, H1-5, HEATR6, HNRNPK, HK1, HYOU1, IFI16, ITM2C, KIF3A, LIPA, CHCHD3, MINPP1, NOLC1, PPP4R3B, PAICS, CTPS1, RRM1, MRPL40, RUVBL2, LARS1, CCT7, PBK, USO1

### Function

The primary functional signal is (GO:BP carbohydrate derivative biosynthetic process; q_global = 0.0178), carbohydrate derivative biosynthetic process, supported by coordinated representation of folate and one-carbon metabolism, purine and pyrimidine nucleotide synthesis, glycolytic entry, lysosomal lipid processing, and mitochondrial ATP synthesis. MTHFD1 and SHMT2 connect one-carbon metabolism with nucleotide production; PAICS supports de novo purine synthesis; CTPS1 supports pyrimidine and phospholipid precursor production; RRM1 supports deoxyribonucleotide supply; and HK1, MT-ATP6, and ATP5MK support energy production. The network therefore most plausibly reflects biosynthetic and energetic capacity in metabolically active cells rather than a narrowly tissue-specific pathway. Additional RNA-processing, protein-folding, vesicle-trafficking, chromatin, and cytoskeletal genes indicate supporting cellular infrastructure. (STRING TISSUES Lymphoblast; within-query FDR = 0.0087) is supplementary evidence for a lymphoblast-associated context, not globally corrected enrichment evidence.

**Cell composition.** This is not a module dominated by plasma or secreted proteins: only a minority are annotated as secreted, and most genes have low tissue specificity or broad cellular distribution. Many proteins are detected in bone marrow, whereas the HPA summary has no matching autonomic-nervous-system tissue measurement, so the apparent cross-tissue conservation should not be interpreted as direct protein-level evidence from both tissues. Several genes are enhanced in erythrocyte or megakaryocyte progenitors, monocyte-lineage cells, lymphoid tissue, or other specialized cell types, but the module overall has low immune-cell specificity. The shared signal could therefore reflect broadly expressed housekeeping and biosynthetic programs present in common or metabolically active marrow-associated cell populations, with a possible contribution from blood-cell composition, rather than a secreted plasma-protein program.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP carbohydrate derivative biosynthetic process | 0.0178 | ATP5MK, CLTC, CTPS1, HK1, ITM2C, LIPA, MT-ATP6, MTHFD1, PAICS, RRM1 |

### STRING and hu.MAP

STRING supports a limited set of already known relationships. The strongest metabolic links connect MTHFD1 with SHMT2 and PAICS, while the module also contains a connected RNA-helicase and RNA-binding neighborhood involving DDX21, DHX9, and HNRNPK, plus links involving CCT7, RUVBL2, GUF1, and RRM1. These relationships support real biochemical and RNA-processing substructures, but they cover only part of the co-abundance module. hu.MAP independently identifies partial matches involving IFI16 with histone-associated partners, LIPA with MINPP1, HEATR6 with ITM2C, mitochondrial ATP-synthase components, FKBP10 with HYOU1, and USO1 with CLTC. Because each complex match contains only a subset of module members, the evidence supports several embedded known complexes rather than one established complex containing the whole module.

**STRING interactions (score >= 0.7)**: 7 of 630 gene pairs: CCT7–RUVBL2 (0.802); DDX21–DHX9 (0.908); DHX9–HNRNPK (0.939); GUF1–RRM1 (0.871); MTHFD1–PAICS (0.9); MTHFD1–SHMT2 (0.996); PAICS–SHMT2 (0.843)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Lymphoblast (FDR = 0.0087, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06044.1 (H1-5, IFI16; 2/3); huMAP3_01213.1 (H1-5, IFI16; 2/4); huMAP3_10278.1 (H1-5, IFI16; 2/5); huMAP3_15307.1 (LIPA, MINPP1; 2/22); huMAP3_11084.1 (HEATR6, ITM2C; 2/27); huMAP3_09307.1 (MT-ATP6, ATP5MK; 2/35); huMAP3_11095.1 (MT-ATP6, ATP5MK; 2/45); huMAP3_06775.1 (FKBP10, HYOU1; 2/60); huMAP3_09327.1 (FKBP10, HYOU1; 2/93); huMAP3_12394.1 (USO1, CLTC; 2/98)

### Novelty

The module should be considered a potentially new cross-tissue co-abundance observation, not a discovery of new molecular functions. The exact shared module, its tissue-pair context, and its particular combination of metabolic, mitochondrial, RNA-processing, trafficking, and marrow-associated genes are not established by the supplied STRING or hu.MAP records. At the same time, many individual relationships and functions are already well known, and the sparse STRING connectivity plus partial hu.MAP overlaps argue against claiming a wholly novel physical pathway. Absence of a complete match in STRING or hu.MAP does not by itself establish novelty; confirmation would require comparison with published co-expression modules, independent cohorts, and cell-composition-controlled data.

**Hypothesis.** Hypothesis: the conserved module reports a biosynthetic stress-and-growth state shared by autonomic-nervous-system-associated cells and bone-marrow-associated cells. Increased demand for mitochondrial energy, one-carbon flux, purine and pyrimidine production, protein folding, RNA handling, and vesicle trafficking could produce the observed coordinated abundance pattern. In bone marrow, this may be linked to progenitor proliferation and differentiation; in autonomic nervous system samples, it may reflect metabolically active support or neural-associated cells rather than a neuron-specific program. This hypothesis predicts that module activity will track cell proliferation, nucleotide demand, mitochondrial function, and cellular composition, and that it will weaken after rigorous adjustment for shared cell types.

### Important genes

#### MTHFD1

- **Related proteins** (co-abundance neighbors): HK1 (0.87), CCT7 (0.86), SHMT2 (0.85), CTPS1 (0.83), HEATR6 (0.83); STRING partners: PAICS (0.9), SHMT2 (0.996)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methylenetetrahydrofolate dehydrogenase, cyclohydrolase and formyltetrahydrofolate synthetase 1. This gene encodes a protein that possesses three distinct enzymatic activities, 5,10-methylenetetrahydrofolate dehydrogenase, 5,10-methenyltetrahydrofolate cyclohydrolase and 10-formyltetrahydrofolate synthetase. Each of these activities catalyzes one of three sequential reactions in the interconversion of 1-carbon derivatives of tetrahydrofolate, which are substrates for methionine, thymidylate, …
- **Diseases (Open Targets)**: combined immunodeficiency and megaloblastic anemia with or without hyperhomocysteinemia (0.773); severe combined immunodeficiency (0.473); neural tube defects, folate-sensitive (0.414); isolated spina bifida (0.376); atrial fibrillation (0.332)
- **Europe PMC papers**: 1939
- **Why important**: MTHFD1 is a central network connector among HK1, CCT7, SHMT2, CTPS1, and HEATR6 and is one of the genes in the globally significant (GO:BP carbohydrate derivative biosynthetic process; q_global = 0.0178) term. Its trifunctional folate enzyme links one-carbon metabolism to methionine, thymidylate, and purine synthesis. It is detected in bone marrow, is enhanced in liver and several metabolically active cell types, has strong STRING links to SHMT2 and PAICS, and has substantial literature and disease evidence involving immunodeficiency, megaloblastic anemia, and folate-sensitive developmental disorders.
- **Conclusion**: Established evidence supports MTHFD1 as a metabolic and nucleotide-supply anchor of the module, with strong biochemical and network support. Its role as the driver of the shared tissue-level co-abundance pattern remains a hypothesis.

#### SHMT2

- **Related proteins** (co-abundance neighbors): CTPS1 (0.88), MTHFD1 (0.85), HK1 (0.82); STRING partners: MTHFD1 (0.996), PAICS (0.843)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine hydroxymethyltransferase 2. This gene encodes the mitochondrial form of a pyridoxal phosphate-dependent enzyme that catalyzes the reversible reaction of serine and tetrahydrofolate to glycine and 5,10-methylene tetrahydrofolate. The encoded product is primarily responsible for glycine synthesis. The activity of the encoded protein has been suggested to be the primary source of intracellular glycine. The gene which encodes th…
- **Diseases (Open Targets)**: neurodevelopmental disorder with cardiomyopathy, spasticity, and brain abnormalities (0.771); microcephaly (0.370); polymicrogyria (0.370); neurodevelopmental disorder (0.336); hereditary disease (0.192)
- **Europe PMC papers**: 2579
- **Why important**: SHMT2 is a mitochondrial one-carbon enzyme that generates glycine and methylene tetrahydrofolate and links mitochondrial metabolism to nucleotide synthesis. It is directly connected in STRING to MTHFD1 and PAICS and is connected within the module to CTPS1 and HK1. It is detected in bone marrow, enhanced in liver and several cell types, and has extensive literature and disease associations involving neurodevelopmental and mitochondrial phenotypes.
- **Conclusion**: Established evidence supports SHMT2 as a major bridge between mitochondrial metabolism and biosynthetic demand in the module. A tissue-pair-specific role in coordinating autonomic and marrow biology is plausible but unproven.

#### PAICS

- **Related proteins** (co-abundance neighbors): GIPC1 (0.82), CCT7 (0.82); STRING partners: MTHFD1 (0.9), SHMT2 (0.843)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoribosylaminoimidazole carboxylase and phosphoribosylaminoimidazolesuccinocarboxamide synthase. This gene encodes a bifunctional enzyme containing phosphoribosylaminoimidazole carboxylase activity in its N-terminal region and phosphoribosylaminoimidazole succinocarboxamide synthetase in its C-terminal region. It catalyzes steps 6 and 7 of purine biosynthesis. The gene is closely linked and divergently transcribed with a locus that encodes an enzyme in the same pathway, and transcription of t…
- **Diseases (Open Targets)**: PAICS deficiency (0.606); Polyhydramnios (0.370); acute myeloid leukemia (0.165); neoplasm (0.107); non-small cell lung carcinoma (0.100)
- **Europe PMC papers**: 960
- **Why important**: PAICS catalyzes consecutive steps in de novo purine biosynthesis and is included in (GO:BP carbohydrate derivative biosynthetic process; q_global = 0.0178). It has module connections to MTHFD1, SHMT2, GIPC1, and CCT7, with high-confidence STRING support from MTHFD1 and SHMT2. Its enrichment in erythrocyte progenitors and detection in bone marrow are consistent with nucleotide demand during hematopoietic development. It also has disease evidence for PAICS deficiency and reported links to leukemia and neoplasia.
- **Conclusion**: Established evidence identifies PAICS as a purine-biosynthesis component embedded in the module's metabolic core. The association with progenitor activity is supported by HPA context, but the co-abundance data do not establish causality or a leukemia-specific mechanism.

#### CTPS1

- **Related proteins** (co-abundance neighbors): SHMT2 (0.88), GUF1 (0.84), MTHFD1 (0.83), CCT7 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CTP synthase 1. This gene encodes an enzyme responsible for the catalytic conversion of UTP (uridine triphosphate) to CTP (cytidine triphospate). This reaction is an important step in the biosynthesis of phospholipids and nucleic acids. Activity of this proten is important in the immune system, and loss of function of this gene has been associated with immunodeficiency. Alternative splicing results in multiple tr…
- **Diseases (Open Targets)**: combined immunodeficiency due to CTPS1 deficiency (0.712); androgenetic alopecia (0.204); hyperpituitarism (0.195); urolithiasis (0.097); alcohol drinking (0.097)
- **Europe PMC papers**: 641
- **Why important**: CTPS1 is a nucleotide and phospholipid precursor enzyme included in (GO:BP carbohydrate derivative biosynthetic process; q_global = 0.0178). It occupies the metabolic subnetwork connecting SHMT2, GUF1, MTHFD1, and CCT7, is detected in bone marrow, and has cell-type enhancement in hepatocytes and smooth muscle cells. Its established immune function and disease association with combined immunodeficiency make it relevant to interpreting a module found in a tissue pair that includes bone marrow.
- **Conclusion**: Established evidence supports CTPS1 as a pyrimidine-synthesis and immune-cell fitness component of the module. Its presence may reflect biosynthetic demand in marrow-associated cells, but a specific autonomic-nervous-system function is not established.

#### LIPA

- **Related proteins** (co-abundance neighbors): HEATR6 (0.85), ITM2C (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_15307.1
- **Function (MyGene.info)**: lipase A, lysosomal acid type. This gene encodes lipase A, the lysosomal acid lipase (also known as cholesterol ester hydrolase). This enzyme functions in the lysosome to catalyze the hydrolysis of cholesteryl esters and triglycerides. Mutations in this gene can result in Wolman disease and cholesteryl ester storage disease. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jan 2014].
- **Diseases (Open Targets)**: cholesteryl ester storage disease (0.818); Wolman disease (0.803); lysosomal acid lipase deficiency (0.754); coronary artery disorder (0.563); myocardial infarction (0.523)
- **Europe PMC papers**: 6860
- **Why important**: LIPA is a lysosomal acid lipase involved in hydrolysis of cholesteryl esters and triglycerides and is included in (GO:BP carbohydrate derivative biosynthetic process; q_global = 0.0178). It connects to HEATR6 and ITM2C in the module, is represented in a partial hu.MAP complex with MINPP1, and is enhanced in lymphoid tissue and monocyte-lineage populations. Its disease associations with lysosomal acid lipase deficiency, Wolman disease, and cholesteryl ester storage disease provide strong functional and clinical context.
- **Conclusion**: Established evidence supports LIPA as a lipid-clearance and lysosomal component that may add a lipid-handling dimension to the module's biosynthetic program. Its monocyte and lymphoid enrichment raises a composition-related explanation, but does not prove that immune-cell abundance causes the cross-tissue module.

#### HEATR6

- **Related proteins** (co-abundance neighbors): CLTC (0.87), H1-5 (0.86), CCM2 (0.86), RRM1 (0.85), LIPA (0.85), CHCHD3 (0.84), MT-ATP6 (0.84), MTHFD1 (0.83), ATP5MK (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11084.1
- **Function (MyGene.info)**: HEAT repeat containing 6. Enables RNA binding activity. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.265); Parkinson disease (0.160); uterine corpus leiomyoma (0.038); lung adenocarcinoma (0.010); allergic rhinitis (0.009)
- **Europe PMC papers**: 108
- **Why important**: HEATR6 has the strongest weighted connectivity in the supplied module graph and links metabolic, mitochondrial, trafficking, and structural genes including CLTC, RRM1, LIPA, MTHFD1, CHCHD3, and MT-ATP6. It has low tissue and cell-type specificity, is annotated with RNA-binding activity, and has comparatively limited literature relative to the established metabolic genes. Its network position makes it useful for explaining module architecture even though it has no globally significant GO/KEGG annotation and no reported STRING partner in the supplied evidence.
- **Conclusion**: Established evidence supports HEATR6 as a topological hub and broadly expressed RNA-associated protein, but not as a validated pathway regulator. Its apparent coordinating role is a hypothesis generated by network position and requires perturbation or independent replication.

## Module 12

**Tissue pair**: autonomic_nervous_system and bone_marrow  
**Genes (6)**: BPHL, HSPA8, PKM, LGALS1, TXN, TRIM56

### Function

The module does not have a globally supported GO/KEGG functional annotation: no term passed global correction, so no GO/KEGG biological process should be treated as enriched. The gene set instead combines constitutive protein folding and trafficking support through HSPA8, glycolytic metabolism through PKM, redox homeostasis through TXN, galectin-mediated cell or matrix interaction and apoptosis-related regulation through LGALS1, innate antiviral and ubiquitin-related functions through TRIM56, and hydrolytic or xenobiotic-related metabolism through BPHL. BPHL is the central co-abundance connector, whereas the remaining genes form relatively weakly connected pairs or branches. The supplementary STRING tissue terms (STRING TISSUES Spleen; within-query FDR = 0.0126) through (STRING TISSUES Throat; within-query FDR = 0.0336) repeatedly involve subsets containing LGALS1, PKM, HSPA8, TXN, TRIM56, or BPHL, but they are not global GO/KEGG evidence. Overall, the module is best interpreted as a mixed metabolic, proteostatic, redox, extracellular-interaction, and innate-response expression state rather than as a narrowly defined pathway.

**Cell composition.** This is not a predominantly plasma-protein module. HPA classifies all genes as having low immune-cell specificity, with no enriched blood-cell category, arguing against a simple blood-cell identity assignment. Two genes are classified as secreted in the module summary, and LGALS1 is specifically reported as secreted to blood, so extracellular or sample-fluid contribution remains possible. Most genes have cell-type-enhanced rather than broadly nonspecific profiles, including epithelial, stromal, adipocyte, hepatocyte, and trophoblast-associated profiles, while tissue enhancement includes kidney, liver, skeletal muscle, tongue, and esophagus. This breadth makes shared cellular composition, stress, or tissue-state effects plausible. Bone-marrow protein detection is present for PKM, LGALS1, TRIM56, and HSPA8, while TXN and BPHL are not detected there; there is no matching HPA tissue record for the autonomic nervous system. Thus, the module should not be labelled a specific autonomic or marrow cell program without cell-resolved validation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The co-abundance network contains relationships among the six genes, with BPHL occupying the central position, but STRING reports no high-confidence interaction among any module-gene pair. hu.MAP reports no complex containing at least two module members. Therefore, the network edges are not corroborated as established direct protein interactions or shared physical complexes. The supplementary STRING tissue associations (STRING TISSUES Spleen; within-query FDR = 0.0126) through (STRING TISSUES Throat; within-query FDR = 0.0336) provide contextual co-occurrence: spleen and throat terms include TRIM56, PKM, and HSPA8 with additional genes; the interstitial-cell-of-Cajal term includes LGALS1, PKM, TXN, and HSPA8; and the breast-cancer-cell term includes LGALS1, TXN, and BPHL. These observations support recurring expression contexts but do not establish a common molecular mechanism.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Spleen (FDR = 0.0126, 4 genes); TISSUES Interstitial cell of Cajal (FDR = 0.0164, 4 genes); TISSUES Breast cancer cell (FDR = 0.0336, 3 genes); TISSUES Throat (FDR = 0.0336, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a new cross-tissue co-abundance observation, because its gene combination is not represented by a STRING interaction set or a hu.MAP complex. However, that absence does not establish biological novelty: the genes have well-described individual functions, several have substantial literature, and the module lacks a globally corrected GO/KEGG signal. The strongest defensible claim is therefore that the autonomic-nervous-system and bone-marrow co-abundance pattern is a potentially novel association requiring independent replication, rather than a newly discovered protein complex or pathway.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular-state program rather than a single biochemical complex. Metabolic activity involving PKM and BPHL may be coupled to proteostasis through HSPA8, redox control through TXN, extracellular or cell-matrix signalling through LGALS1, and inducible innate-response regulation through TRIM56. In autonomic nervous system and bone marrow samples, this state could arise from shared stress, metabolic demand, or mixed-cell composition. This hypothesis is not established by the enrichment results and should be tested with cell-type-resolved expression, independent cohorts, perturbation experiments, and direct protein or interaction assays.

### Important genes

#### BPHL

- **Related proteins** (co-abundance neighbors): LGALS1 (0.89), PKM (0.88), TXN (0.87), TRIM56 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biphenyl hydrolase like. This gene encodes a member of the serine protease family of hydrolytic enzymes which contain a serine in their active site. The encoded protein may play a role in activation of the antiviral prodrug valacyclovir. Alternatively spliced transcript variants have been described.[provided by RefSeq, Jan 2009].
- **Diseases (Open Targets)**: alcohol drinking (0.181); urolithiasis (0.181); handedness (0.164); musculoskeletal system disorder (0.122); tooth disorder (0.109)
- **Europe PMC papers**: 358
- **Why important**: BPHL is the network hub and connects to LGALS1, PKM, TXN, and TRIM56, making it the principal structural organizer of the co-abundance pattern. Its annotated serine-hydrolase function, amino-acid, xenobiotic, and homocysteine-related processes provide a plausible metabolic link to the other module components. Its HPA profile is tissue-enhanced in kidney and liver and cell-type-enhanced in adipocytes, enterocytes, and hepatocytes, while bone-marrow protein is not detected. It has a smaller literature base than the most intensively studied module genes, which increases the value of this cross-tissue association for follow-up.
- **Conclusion**: Established: BPHL is the central co-abundance connector and has hydrolytic and metabolic annotations. Hypothesis: BPHL may organize or report a metabolic state shared across the two tissues, but a causal role and any physical interaction with the other genes remain un demonstrated.

#### PKM

- **Related proteins** (co-abundance neighbors): BPHL (0.88), HSPA8 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyruvate kinase M1/2. This gene encodes a protein involved in glycolysis. The encoded protein is a pyruvate kinase that catalyzes the transfer of a phosphoryl group from phosphoenolpyruvate to ADP, generating ATP and pyruvate. This protein has been shown to interact with thyroid hormone and may mediate cellular metabolic effects induced by thyroid hormones. This protein has been found to bind Opa protein, a bacterial o…
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); autoimmune disorder of central nervous system (0.370); tympanic membrane perforation (0.204); neoplasm (0.121); hepatocellular carcinoma (0.120)
- **Europe PMC papers**: 8544
- **Why important**: PKM is connected to BPHL and HSPA8 and encodes the glycolytic pyruvate kinase that generates ATP and pyruvate. It is repeatedly represented in the supplementary STRING tissue terms (STRING TISSUES Spleen; within-query FDR = 0.0126), (STRING TISSUES Interstitial cell of Cajal; within-query FDR = 0.0164), and (STRING TISSUES Throat; within-query FDR = 0.0336), has bone-marrow protein detection, and has a large literature base. Its tissue and cell-type enhancement in skeletal muscle, tongue, esophageal epithelial populations, extravillous trophoblasts, and late spermatids indicates that its presence is compatible with varied metabolically active cell states rather than a marrow-specific identity.
- **Conclusion**: Established: PKM provides a credible metabolic component and is linked in the co-abundance graph to BPHL and HSPA8. Hypothesis: glycolytic demand may help explain the shared module, but the data do not show that PKM drives the co-abundance of the other genes.

#### HSPA8

- **Related proteins** (co-abundance neighbors): PKM (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Flagellar centriole, Annulus; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 8. This gene encodes a member of the heat shock protein 70 family, which contains both heat-inducible and constitutively expressed members. This protein belongs to the latter group, which are also referred to as heat-shock cognate proteins. It functions as a chaperone, and binds to nascent polypeptides to facilitate correct folding. It also functions as an ATPase in the disassembly of clathrin-coated…
- **Diseases (Open Targets)**: dengue disease (0.505); systemic lupus erythematosus (0.375); smoking initiation (0.199); Lennox-Gastaut syndrome (0.118); neoplasm (0.105)
- **Europe PMC papers**: 6937
- **Why important**: HSPA8 is a constitutive HSP70-family chaperone involved in protein folding and vesicle transport, and it is connected to PKM. It recurs in the supplementary STRING tissue terms (STRING TISSUES Spleen; within-query FDR = 0.0126), (STRING TISSUES Interstitial cell of Cajal; within-query FDR = 0.0164), and (STRING TISSUES Throat; within-query FDR = 0.0336), is detected in bone marrow, and has a very large literature base. Its low tissue specificity is consistent with a general proteostasis or cellular-maintenance component rather than a specialized tissue marker.
- **Conclusion**: Established: HSPA8 is a broadly relevant chaperone and a recurring member of the supplementary tissue signals. Hypothesis: it may indicate proteostatic load or altered intracellular trafficking in the shared state, but this cannot be distinguished from generic housekeeping co-abundance.

#### LGALS1

- **Related proteins** (co-abundance neighbors): BPHL (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galectin 1. The galectins are a family of beta-galactoside-binding proteins implicated in modulating cell-cell and cell-matrix interactions. This gene product may act as an autocrine negative growth factor that regulates cell proliferation. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: glaucoma (0.349); open-angle glaucoma (0.343); chronic kidney disease (0.330); smoking initiation (0.162); melanoma (0.121)
- **Europe PMC papers**: 4025
- **Why important**: LGALS1 is a secreted-to-blood galectin involved in cell-cell and cell-matrix interactions and regulation of apoptosis and signalling. It is connected to BPHL and recurs in the supplementary STRING terms (STRING TISSUES Spleen; within-query FDR = 0.0126), (STRING TISSUES Interstitial cell of Cajal; within-query FDR = 0.0164), and (STRING TISSUES Breast cancer cell; within-query FDR = 0.0336). It is detected in bone marrow, has cell-type enhancement in dendritic, stromal, fibroblast, and trophoblast-associated populations, and has a substantial literature base. Its extracellular status makes it especially relevant when considering tissue composition or paracrine effects.
- **Conclusion**: Established: LGALS1 is an extracellularly relevant signalling and interaction protein with repeated supplementary tissue associations. Hypothesis: it could connect cellular stress or composition effects to paracrine signalling in the shared module, but the co-abundance data do not establish secretion as the cause of the module.

#### TXN

- **Related proteins** (co-abundance neighbors): BPHL (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin. The protein encoded by this gene acts as a homodimer and is involved in many redox reactions. The encoded protein is active in the reversible S-nitrosylation of cysteines in certain proteins, which is part of the response to intracellular nitric oxide. This protein is found in the cytoplasm. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct…
- **Diseases (Open Targets)**: neurodegenerative disease (0.530); smoking initiation (0.288); ovarian neoplasm (0.171); cancer (0.122); neoplasm (0.114)
- **Europe PMC papers**: 4080
- **Why important**: TXN is connected to BPHL and encodes thioredoxin, a central redox-homeostasis protein involved in reversible cysteine modification and cellular detoxification. It recurs in the supplementary STRING terms (STRING TISSUES Interstitial cell of Cajal; within-query FDR = 0.0164) and (STRING TISSUES Breast cancer cell; within-query FDR = 0.0336). HPA places it in nucleoplasm and cytosol, with enhancement in esophageal and related epithelial cell populations, and reports it as intracellular and membrane-associated. Its substantial literature base and redox function make it a strong candidate marker of cellular stress state.
- **Conclusion**: Established: TXN supplies a well-supported redox and detoxification function and is associated with specific supplementary tissue contexts. Hypothesis: redox pressure may be one mechanism coupling TXN with metabolic and chaperone genes, but no causal coupling is demonstrated.

## Module 13

**Tissue pair**: autonomic_nervous_system and bone_marrow  
**Genes (5)**: HS1BP3, IGF2BP3, PHAX, SIN3A, TNPO2

### Function

No GO/KEGG term passed global correction, so the module does not support a formally significant pathway assignment. The strongest biological interpretation comes from the gene annotations and network structure: the module links an apparent HS1BP3-centered co-abundance pattern with RNA handling, nuclear transport, transcriptional regulation, and post-transcriptional control. HS1BP3 is connected to IGF2BP3, TNPO2, SIN3A, and PHAX, whereas the other genes are peripheral members. IGF2BP3 contributes RNA binding, mRNA stabilization, translation and cytokine-related annotations; TNPO2 contributes nuclear import; SIN3A contributes transcriptional repression and immune or antiviral response annotations; and PHAX contributes RNA stabilization and snRNA export. These annotations suggest coordinated regulation of gene expression and RNA metabolism, but they do not establish one unified pathway. The absence of globally significant GO/KEGG terms is compatible with a small, heterogeneous module and does not invalidate the co-abundance observation.

**Cell composition.** The module is not composed of plasma or secreted proteins: none of the members is annotated as secreted. Its members are predominantly broadly expressed according to HPA, with low tissue specificity for most genes. HPA reports low immune-cell specificity for most members and no enriched blood-cell category, so the module does not look like a simple blood-cell or plasma-protein signature. One member, IGF2BP3, is tissue enhanced in lymphoid tissue and placenta and is not detected in immune cells in the supplied HPA summary. Three members have cell-type-enhanced annotations, including neutrophils for SIN3A and several non-blood developmental or epithelial cell types for IGF2BP3. Bone marrow protein detection is present for HS1BP3, SIN3A, and PHAX but absent for IGF2BP3 and TNPO2. Because the autonomic-nervous-system comparison lacks a matching HPA tissue, the shared module should not be interpreted as tissue-specific protein expression. Overall, the composition is more consistent with broadly expressed intracellular regulatory proteins than with a secreted or overtly blood-cell-restricted program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The supplied STRING analysis contains no high-confidence interaction among the module members, and the supplementary STRING functional-enrichment analysis is empty. hu.MAP also reports no complex containing multiple module members. Thus, the co-abundance edges are not corroborated here as established physical interactions or membership in a known multi-protein complex. The four network links are therefore best treated as coordinated abundance relationships in the two tissues, not as evidence that the proteins form one physical complex. The lack of STRING and hu.MAP support also argues against assigning a specific canonical molecular machine to the module.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may represent a previously unreported tissue-pair co-abundance pattern, but the evidence is insufficient to call it a new biological mechanism. Its genes have substantial prior biological characterization, especially IGF2BP3 and SIN3A, and their individual functions are not novel. Conversely, the absence of a shared STRING interaction or hu.MAP complex means the observed cross-tissue combination is not explained by an already catalogued physical complex. The lack of globally significant GO/KEGG enrichment, the sparse network, and the broadly expressed intracellular composition make a cautious conclusion appropriate: the potentially novel feature is the coordinated abundance pattern across autonomic nervous system and bone marrow, not the discovery of new functions for these proteins. Independent replication and experimental testing would be needed before claiming novelty.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of RNA fate and nuclear gene expression in a cell population shared between the two tissue contexts. In this model, HS1BP3 acts as the abundance-associated hub, while IGF2BP3 influences RNA binding and translation, PHAX supports RNA export or stabilization, TNPO2 supports nuclear import, and SIN3A couples the state to transcriptional repression and cellular defense programs. This is a mechanistic hypothesis rather than an established complex or pathway: the lack of globally significant GO/KEGG terms, STRING support, and hu.MAP complexes means the data do not demonstrate direct physical cooperation. A testable prediction is that the abundance pattern will track a shared regulatory or cellular-state program, rather than secretion or a narrowly defined blood-cell population.

### Important genes

#### HS1BP3

- **Related proteins** (co-abundance neighbors): IGF2BP3 (0.89), TNPO2 (0.87), SIN3A (0.81), PHAX (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HCLS1 binding protein 3. The protein encoded by this gene shares similarity with mouse Hs1bp3, an Hcls1/Hs1-interacting protein that may be involved in lymphocyte activation. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: prolapse of female genital organ (0.300); liver disorder (0.233); Tietze syndrome (0.145); prostate carcinoma (0.090); Hypercholesterolemia (0.082)
- **Europe PMC papers**: 165
- **Why important**: HS1BP3 is the network hub, connected to every other module member in the supplied co-abundance graph. It is annotated as an HCLS1 binding protein that may be involved in lymphocyte activation and regulation of apoptosis, is detected in bone marrow, and has the largest supplied literature-supported context among the less established module components. Its central network position makes it the most important candidate for testing whether the module is organized around a shared regulatory state.
- **Conclusion**: Established evidence supports HS1BP3 as the central co-abundance member with links to RNA-related and nuclear-regulatory proteins, plus a possible connection to lymphocyte activation. It is not established that HS1BP3 physically organizes the other proteins or drives the module. Its hub role is therefore a hypothesis for experimental testing, not proof of causality.

#### IGF2BP3

- **Related proteins** (co-abundance neighbors): HS1BP3 (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor 2 mRNA binding protein 3. The protein encoded by this gene is primarily found in the nucleolus, where it can bind to the 5' UTR of the insulin-like growth factor II leader 3 mRNA and may repress translation of insulin-like growth factor II during late development. The encoded protein contains several KH domains, which are important in RNA binding and are known to be involved in RNA synthesis and metabolism. A pseudogene ex…
- **Diseases (Open Targets)**: neurodegenerative disease (0.536); type 2 diabetes mellitus (0.405); diabetes mellitus (0.304); celiac disease (0.254); placental abruption (0.175)
- **Europe PMC papers**: 5072
- **Why important**: IGF2BP3 is the most extensively studied member in the supplied literature summary and is the only tissue-enhanced member in the module, with enhancement in lymphoid tissue and placenta. It has annotations for RNA binding, mRNA stabilization, translation, cytokine production, and nervous-system development. Although it is a peripheral network member linked only to HS1BP3, its functional specificity and disease associations make it a key biological anchor.
- **Conclusion**: Established evidence supports IGF2BP3 as an RNA-associated regulatory protein with context-dependent tissue expression and broad disease relevance. The module data do not establish that IGF2BP3 creates the shared tissue-pair signal or that its RNA targets explain the other members. Its participation in a coordinated RNA-regulatory state remains a hypothesis.

#### SIN3A

- **Related proteins** (co-abundance neighbors): HS1BP3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SIN3 transcription regulator family member A. The protein encoded by this gene is a transcriptional regulatory protein. It contains paired amphipathic helix (PAH) domains, which are important for protein-protein interactions and may mediate repression by the Mad-Max complex. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: chromosome 15q24 deletion syndrome (0.748); SIN3A-related intellectual disability syndrome (0.618); syndromic intellectual disability (0.554); hereditary disease (0.537); neurodegenerative disease (0.430)
- **Europe PMC papers**: 5349
- **Why important**: SIN3A is a transcriptional regulatory protein with annotations for negative regulation of transcription, innate immune activation, antiviral defense, hormone regulation, and cerebral-cortex neuron differentiation. It is detected in bone marrow, has a cell-type-enhanced neutrophil annotation, and is among the most extensively studied genes in the module. Its connection to HS1BP3 places it at the interface between the module hub and transcriptional-state regulation.
- **Conclusion**: Established evidence supports SIN3A as a multifunctional transcriptional regulator with disease associations involving intellectual disability and neurodegeneration. The supplied data do not show that SIN3A forms a complex with HS1BP3 or that it explains the shared tissue pattern. Its role in a common transcriptional state is a plausible but unproven hypothesis.

#### PHAX

- **Related proteins** (co-abundance neighbors): HS1BP3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphorylated adaptor for RNA export. Enables mRNA cap binding complex binding activity. Involved in RNA stabilization. Located in centrosome and nucleoplasm. Part of ribonucleoprotein complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.525); adult-onset autosomal dominant demyelinating leukodystrophy (0.341); Aganglionic megacolon (0.111); Hirschsprung disease (0.111); testicular disorder (0.106)
- **Europe PMC papers**: 433
- **Why important**: PHAX contributes a distinct RNA-processing function through snRNA export and RNA stabilization, and it is annotated in the nucleoplasm and centrosome. It is detected in bone marrow and is connected to HS1BP3 in the module graph. Its function complements the RNA-binding and translation annotations of IGF2BP3, making it important for the proposed RNA-regulatory interpretation.
- **Conclusion**: Established evidence supports PHAX as an RNA-export and RNA-stability factor. The co-abundance data do not establish direct cooperation with HS1BP3 or the other members, and no hu.MAP or STRING relationship is supplied. Its contribution to a shared RNA-handling program is therefore a hypothesis.

#### TNPO2

- **Related proteins** (co-abundance neighbors): HS1BP3 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transportin 2. Predicted to enable nuclear import signal receptor activity and nuclear localization sequence binding activity. Predicted to be involved in protein import into nucleus. Predicted to act upstream of or within negative regulation of muscle cell differentiation. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: intellectual developmental disorder with hypotonia, impaired speech, and dysmorphic facies (0.685); Intellectual disability (0.504); Hypotonia (0.503); microcephaly (0.503); Seizure (0.503)
- **Europe PMC papers**: 280
- **Why important**: TNPO2 supplies the module's clearest nuclear-transport function through nuclear import and nuclear-localization-sequence binding. It is localized to the nucleoplasm and nucleoli, is broadly expressed by HPA, and is connected to HS1BP3. Its disease associations include developmental neurological disorders, which adds relevance to the cross-tissue context even though it is a peripheral member.
- **Conclusion**: Established evidence supports TNPO2 as a nuclear-import factor with neurological disease associations. The module does not establish that TNPO2 transports any specific module protein or that it mediates the tissue-pair association. Its placement in a shared nuclear-regulatory program is a hypothesis.
