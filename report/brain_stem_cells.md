# Conserved co-abundance modules: brain and stem_cells

## Module 0

**Tissue pair**: brain and stem_cells  
**Genes (17)**: ACADS, ARSB, C1orf50, COX11, DNAJB14, ELMOD2, MAGED1, SLC25A20, NDUFV2, DLAT, PTPRK, RPP30, MRPS18B, SRI, SZRD1, TPBG, UCHL5

### Function

The module does not have any GO or KEGG term that passed global correction, so no pathway-level enrichment can be claimed. Its gene annotations nevertheless suggest a mixed cellular program with prominent mitochondrial metabolism and protein or organelle maintenance features. ACADS and SLC25A20 connect short-chain fatty-acid oxidation with mitochondrial acylcarnitine transport, while DLAT and COX11 represent pyruvate entry into acetyl-CoA metabolism and respiratory-chain complex assembly. NDUFV2 adds mitochondrial electron-transfer biology. DNAJB14 is the main network hub and is annotated for endoplasmic-reticulum protein folding, complex assembly, and responses to misfolded protein. The remaining links involve lysosomal or glycosaminoglycan processing, RNA processing, deubiquitination, calcium signaling, cell adhesion, and transcriptional regulation. Thus, the most defensible interpretation is a heterogeneous co-abundance program associated with cellular metabolic capacity and proteostatic or organelle-maintenance state, rather than a single established biological pathway. The network is sparse and contains several weakly connected branches, which limits confidence in a unified function.

**Cell composition.** The module is not dominated by secreted proteins and is not broadly characterized as a blood-cell module. HPA reports only one secreted gene, while most genes have low immune-cell specificity. Most genes are detected at the protein level in brain, supporting compatibility with brain-resident cellular biology, although the stem-cell tissue comparison has no matching HPA tissue. The module is compositionally mixed rather than a uniform housekeeping set: many genes have cell-type-enhanced profiles in enterocytes, colonocytes, enteric progenitors, oligodendrocyte progenitors, neurons, glia, hepatocytes, or muscle-related cells. Tissue-enhanced signals in liver, skeletal muscle, tongue, and intestine, together with the enteric and hepatocyte annotations, indicate that shared cell composition or general metabolic state could contribute to the cross-tissue module. A small amount of immune-cell enhancement is present, but the overall HPA evidence does not support blood contamination as the primary explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The module has no STRING functional-enrichment result and no hu.MAP complex containing multiple module members. Within the high-confidence STRING network, the only supported relationship is ACADS with SLC25A20, linking fatty-acid oxidation to mitochondrial acylcarnitine transport. The module co-abundance edges are therefore largely not backed by the queried known interaction resources. DNAJB14 is the co-abundance hub, connecting to MRPS18B, C1orf50, PTPRK, UCHL5, TPBG, and SZRD1, but none of these relationships has a listed STRING or hu.MAP counterpart. ARSB connects in the co-abundance graph to several metabolically or organelle-related genes, including NDUFV2 and DLAT, yet these links are also not established by the supplied reference networks. This pattern means the module captures coordinated abundance without demonstrating a single known physical complex. It could reflect shared cell type, shared organelle load, or coordinated regulation rather than direct protein interaction.

**STRING interactions (score >= 0.7)**: 1 of 136 gene pairs: ACADS–SLC25A20 (0.79)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a new biological discovery on the basis of the supplied evidence. Its strongest mechanistic elements are already established individually: ACADS is a fatty-acid oxidation enzyme, SLC25A20 is a mitochondrial acylcarnitine carrier, DLAT is a pyruvate dehydrogenase component, COX11 participates in respiratory-chain complex assembly, NDUFV2 participates in complex I electron transfer, and DNAJB14 has chaperone-related annotations. The absence of a corresponding hu.MAP complex, the lack of STRING functional enrichment, and the sparse overlap with high-confidence STRING interactions indicate that the particular co-abundance grouping may be under-characterized. However, absence from STRING or hu.MAP alone does not establish novelty. A cautious claim is that the cross-tissue co-abundance pattern is a potentially interesting association that requires replication, cell-composition control, perturbation, and comparison with additional co-expression and proteomics resources before it can be considered novel.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in which mitochondrial substrate handling, oxidative metabolism, and protein-quality control vary together across brain and stem-cell samples. One possible mechanism is that coordinated mitochondrial activity links SLC25A20-mediated acylcarnitine transport, ACADS-dependent fatty-acid oxidation, DLAT-dependent pyruvate utilization, NDUFV2 electron transfer, and COX11-supported respiratory-chain assembly, while DNAJB14 helps maintain folding and assembly of proteins under the associated organelle stress. ARSB, UCHL5, and SRI could mark lysosomal, proteostatic, or calcium-regulatory consequences of that state. This remains a hypothesis because the module lacks globally significant enrichment, contains no multi-member hu.MAP complex, has only one listed high-confidence STRING interaction, and includes cell-type patterns spanning several tissues and lineages. An alternative explanation is coordinated abundance caused by shared cellular composition rather than a direct mechanistic pathway.

### Important genes

#### DNAJB14

- **Related proteins** (co-abundance neighbors): MRPS18B (0.98), C1orf50 (0.95), PTPRK (0.89), UCHL5 (0.88), TPBG (0.86), SZRD1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DnaJ heat shock protein family (Hsp40) member B14. Enables Hsp70 protein binding activity. Involved in cellular protein-containing complex assembly and chaperone cofactor-dependent protein refolding. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.133); open-angle glaucoma (0.120); renal carcinoma (0.104); renal cell carcinoma (0.072); gout (0.050)
- **Europe PMC papers**: 226
- **Why important**: DNAJB14 is the network hub, with the broadest set of co-abundance connections in the module. Its endoplasmic-reticulum localization and annotations for Hsp70 binding, protein folding, complex assembly, and response to misfolded protein provide a plausible proteostasis axis that could connect otherwise heterogeneous genes. It has brain protein detection, low tissue and immune specificity, and a moderate literature base, making it more informative for module architecture than for a specific disease claim.
- **Conclusion**: Established evidence supports DNAJB14 as a chaperone cofactor involved in protein folding and complex assembly and as the central co-abundance node. It is reasonable to hypothesize that it marks proteostatic or organelle-assembly state in this module, but the supplied data do not establish that it physically interacts with its module neighbors or drives the shared program.

#### ACADS

- **Related proteins** (co-abundance neighbors): MAGED1 (0.84), ARSB (0.81); STRING partners: SLC25A20 (0.79)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA dehydrogenase short chain. This gene encodes a tetrameric mitochondrial flavoprotein, which is a member of the acyl-CoA dehydrogenase family. This enzyme catalyzes the initial step of the mitochondrial fatty acid beta-oxidation pathway. Mutations in this gene have been associated with short-chain acyl-CoA dehydrogenase (SCAD) deficiency. Alternative splicing results in two variants which encode different isoforms. [provided…
- **Diseases (Open Targets)**: short chain acyl-CoA dehydrogenase deficiency (0.834); hereditary disease (0.480); substance-related disorder (0.336); type 2 diabetes mellitus (0.324); diabetes mellitus (0.254)
- **Europe PMC papers**: 2216
- **Why important**: ACADS is a direct metabolic enzyme with a clear role in mitochondrial short-chain fatty-acid beta-oxidation and butyrate catabolism. It is tissue-enhanced in liver and skeletal muscle and cell-type-enhanced across intestinal and progenitor populations, which fits the HPA indication that metabolic cell composition may influence the module. It also participates in the sole listed high-confidence STRING relationship, with SLC25A20, and has a strong disease association with short-chain acyl-CoA dehydrogenase deficiency.
- **Conclusion**: Established evidence supports ACADS as a mitochondrial fatty-acid oxidation enzyme and supports its known relationship with SLC25A20. The module-level conclusion is that ACADS supplies a credible metabolic anchor, but its co-abundance with the broader set does not prove that the entire module is a fatty-acid oxidation pathway.

#### SLC25A20

- **Related proteins** (co-abundance neighbors): MAGED1 (0.86), ELMOD2 (0.82); STRING partners: ACADS (0.79)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 25 member 20. This gene product is one of several closely related mitochondrial-membrane carrier proteins that shuttle substrates between cytosol and the intramitochondrial matrix space. This protein mediates the transport of acylcarnitines into mitochondrial matrix for their oxidation by the mitochondrial fatty acid-oxidation pathway. Mutations in this gene are associated with carnitine-acylcarnitine transloca…
- **Diseases (Open Targets)**: carnitine-acylcarnitine translocase deficiency (0.826); hereditary disease (0.192); Pancreatic pseudocyst (0.132); Abnormality of the skeletal system (0.110); neoplasm (0.097)
- **Europe PMC papers**: 1115
- **Why important**: SLC25A20 provides the transport counterpart to ACADS by moving acylcarnitines into the mitochondrial matrix for oxidation. It is tissue-enhanced in liver and cell-type-enhanced in enterocytes, hepatocytes, and myonuclei, and its disease association with carnitine-acylcarnitine translocase deficiency is well established in the supplied evidence. Its STRING-supported relationship with ACADS gives this pair stronger external support than most other module edges.
- **Conclusion**: Established evidence supports SLC25A20 as a mitochondrial carnitine-shuttle transporter and supports its connection to ACADS. It strengthens the interpretation of a mitochondrial lipid-substrate branch, but it does not validate the full module as a coherent physical complex or globally enriched pathway.

#### DLAT

- **Related proteins** (co-abundance neighbors): ARSB (0.83), COX11 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dihydrolipoamide S-acetyltransferase. This gene encodes component E2 of the multi-enzyme pyruvate dehydrogenase complex (PDC). PDC resides in the inner mitochondrial membrane and catalyzes the conversion of pyruvate to acetyl coenzyme A. The protein product of this gene, dihydrolipoamide acetyltransferase, accepts acetyl groups formed by the oxidative decarboxylation of pyruvate and transfers them to coenzyme A. Dihydrolipoamide acety…
- **Diseases (Open Targets)**: pyruvate dehydrogenase E2 deficiency (0.792); pyruvate decarboxylase deficiency (0.711); dystonic disorder (0.374); hereditary disease (0.341); neurodegenerative disease (0.322)
- **Europe PMC papers**: 3481
- **Why important**: DLAT is the E2 component of the pyruvate dehydrogenase complex and links pyruvate catabolism to acetyl-CoA production and the tricarboxylic acid cycle. Its connections to ARSB and COX11 place it within a co-abundance branch containing other mitochondrial or organelle-related genes. It has substantial literature and disease associations involving pyruvate dehydrogenase deficiency and neurodegenerative disease, while its HPA profile includes cardiomyocytes and adipocytes.
- **Conclusion**: Established evidence supports DLAT as a core pyruvate-oxidation enzyme. In this module it is best interpreted as evidence for a broader mitochondrial energy-metabolism state, not as proof that pyruvate dehydrogenase is the defining function of the whole module.

#### NDUFV2

- **Related proteins** (co-abundance neighbors): ARSB (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit V2. The NADH-ubiquinone oxidoreductase complex (complex I) of the mitochondrial respiratory chain catalyzes the transfer of electrons from NADH to ubiquinone, and consists of at least 43 subunits. The complex is located in the inner mitochondrial membrane. This gene encodes the 24 kDa subunit of complex I, and is involved in electron transfer. Mutations in this gene are implicated in Parkinson's disea…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 7 (0.717); mitochondrial complex I deficiency (0.623); type 2 diabetes mellitus (0.608); Parkinson disease (0.606); diabetes mellitus (0.579)
- **Europe PMC papers**: 1539
- **Why important**: NDUFV2 is a complex I subunit involved in mitochondrial electron transfer, aerobic respiration, and proton-motive-force-driven ATP synthesis. Its co-abundance connection to ARSB adds a respiratory-chain component to the metabolic interpretation, and its disease associations include complex I deficiency and Parkinson disease. The brain protein detection and extensive disease literature make it especially relevant to interpreting the module in a brain-containing tissue pair.
- **Conclusion**: Established evidence supports NDUFV2 as a mitochondrial respiratory-chain component with disease relevance. Its presence supports an oxidative-metabolism interpretation, but the absence of globally significant enrichment and the sparse reference-network support prevent a conclusion that the module represents a defined complex I program.

#### ARSB

- **Related proteins** (co-abundance neighbors): SRI (0.85), NDUFV2 (0.84), DLAT (0.83), MRPS18B (0.81), ACADS (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: arylsulfatase B. Arylsulfatase B encoded by this gene belongs to the sulfatase family. The arylsulfatase B homodimer hydrolyzes sulfate groups of N-Acetyl-D-galactosamine, chondriotin sulfate, and dermatan sulfate. The protein is targeted to the lysozyme. Mucopolysaccharidosis type VI is an autosomal recessive lysosomal storage disorder resulting from a deficiency of arylsulfatase B. Two alternatively spliced tran…
- **Diseases (Open Targets)**: mucopolysaccharidosis type 6 (0.872); mucopolysaccharidosis (0.509); mucopolysaccharidosis type 1 (0.466); metachromatic leukodystrophy (0.457); hereditary disease (0.453)
- **Europe PMC papers**: 5396
- **Why important**: ARSB is one of the more connected genes in the co-abundance graph and bridges several branches, including links to SRI, NDUFV2, DLAT, MRPS18B, and ACADS. Its established function is lysosomal or Golgi-associated degradation of sulfated glycosaminoglycans, with a strong disease association with mucopolysaccharidosis type six. HPA shows cell-type enhancement in microglia, oligodendrocyte progenitors, proximal tubule cells, and an immune-cell category, making it useful for considering cell-type and organelle-composition effects.
- **Conclusion**: Established evidence supports ARSB as a lysosomal sulfatase and disease gene, and its network position makes it an important bridge. A plausible interpretation is that it reflects lysosomal or cellular-clearance state alongside mitochondrial metabolism, but the data do not establish a direct mechanistic connection between ARSB and the mitochondrial genes.

## Module 1

**Tissue pair**: brain and stem_cells  
**Genes (8)**: ATP5MK, ACOT7, CLTCL1, CRMP1, TUBGCP6, GNA11, STRIP1, VPS35

### Function

The module does not support a formally enriched GO or KEGG function: no GO/KEGG term passed global correction, and there are no supplementary STRING enrichment terms. Its genes instead point to a mixed cellular infrastructure program involving microtubule nucleation and cytoskeletal organization, neuronal development and signaling, vesicle and endosomal trafficking, mitochondrial ATP synthesis, and long-chain fatty-acid metabolism. The co-abundance pattern is therefore better interpreted as a shared cellular-state or cell-composition signal than as evidence for a single established pathway. The strongest biological coherence is a possible connection between cytoskeletal organization, neuronal cell biology, intracellular trafficking, and energy or lipid handling, but this remains an interpretation rather than an enrichment result.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of the genes is annotated as secreted. Most genes have low tissue specificity, while a minority are tissue enhanced in brain, skeletal muscle, testis, tongue, or pituitary gland. Nearly all genes show cell-type enhancement, but the implicated cell types are diverse and include neuronal, epithelial, reproductive, muscle, and immune populations. Some genes have enrichment in neutrophils, monocytes, NK cells, or plasmacytoid dendritic cells, although the overall immune-cell evidence is mixed rather than uniformly blood-cell specific. Brain protein detection is common among the queried brain regions, whereas there is no matching HPA tissue for stem cells. Thus, the shared module could partly reflect broadly distributed cellular machinery or differing cell-type composition, rather than a stem-cell-specific program or a secreted blood-derived signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair reaches the supplied STRING interaction threshold, and no STRING functional-enrichment term is present. No hu.MAP complex contains multiple module members. The observed co-abundance edges are therefore not corroborated by the supplied high-confidence STRING network or by known hu.MAP complex membership. This does not disprove biological coordination, but it indicates that the module is not simply recovering a recognized physical complex or a well-established interaction neighborhood. The strongest internal organization is centered on TUBGCP6, which connects to several genes, with CRMP1 providing a smaller bridge between TUBGCP6, GNA11, and ACOT7.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel co-abundance pattern, because the module is not represented by a known STRING interaction network, a STRING enrichment result, or a hu.MAP complex. However, absence from those resources alone cannot establish novelty: co-abundance can arise from shared regulation, cell composition, indirect biology, or technical structure, and known protein interactions may be incomplete or context dependent. A defensible claim is that this particular cross-tissue co-abundance configuration is insufficiently explained by the supplied reference resources and warrants independent replication, cell-composition adjustment, and validation in additional brain and stem-cell datasets.

**Hypothesis.** Hypothesis: the module represents a shared cellular-state program in which microtubule-organizing and cytoskeletal machinery is coordinated with neuronal signaling, endosomal recycling, mitochondrial energy production, and fatty-acid handling. TUBGCP6 may provide the structural hub, CRMP1 and GNA11 may connect cytoskeletal organization to signaling, VPS35 may reflect intracellular cargo recycling, and ACOT7 may couple the state to neuronal lipid metabolism. The apparent conservation between brain and stem cells could reflect a common requirement for cytoskeletal remodeling, vesicle trafficking, and metabolic support, or could instead result from overlapping cell populations. This hypothesis should be tested through replication, perturbation of the proposed hub and bridge genes, and analysis controlling for cell-type composition.

### Important genes

#### TUBGCP6

- **Related proteins** (co-abundance neighbors): CLTCL1 (0.93), STRIP1 (0.86), VPS35 (0.83), ATP5MK (0.81), CRMP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tubulin gamma complex component 6. The protein encoded by this gene is part of a large multisubunit complex required for microtubule nucleation at the centrosome. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: microcephaly and chorioretinopathy 1 (0.789); microcephaly with or without chorioretinopathy, lymphedema, or intellectual disability (0.425); hereditary disease (0.416); inherited retinal dystrophy (0.406); Primary microcephaly (0.370)
- **Europe PMC papers**: 289
- **Why important**: TUBGCP6 is the most connected gene in the module and links CLTCL1, STRIP1, VPS35, ATP5MK, and CRMP1. Its established function in the gamma-tubulin complex places it directly in microtubule nucleation, spindle assembly, and cytoskeletal organization. HPA detects its protein in brain, and its disease associations include microcephaly and retinal or neurodevelopmental phenotypes. The available literature is substantial, making it the best network-defined candidate for a structural organizing role.
- **Conclusion**: Established evidence supports TUBGCP6 as a microtubule-nucleation component and the central network gene. It is plausible, but not established, that its co-abundance with trafficking, signaling, mitochondrial, and lipid genes marks a coordinated cytoskeletal cellular state.

#### CRMP1

- **Related proteins** (co-abundance neighbors): GNA11 (0.89), TUBGCP6 (0.81), ACOT7 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Centrosome; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collapsin response mediator protein 1. This gene encodes a member of a family of cytosolic phosphoproteins expressed exclusively in the nervous system. The encoded protein is thought to be a part of the semaphorin signal transduction pathway implicated in semaphorin-induced growth cone collapse during neural development. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.338); alcohol drinking (0.306); stroke disorder (0.298); neurodevelopmental disorder (0.217); acute tonsillitis (0.199)
- **Europe PMC papers**: 895
- **Why important**: CRMP1 is a network bridge connecting TUBGCP6 with GNA11 and ACOT7. It is described as a nervous-system cytosolic phosphoprotein involved in semaphorin signaling, growth-cone collapse, neuron projection development, and postsynaptic organization. Its HPA profile is tissue enhanced in brain, pituitary gland, and retina, with neuronal cell-type enhancement and brain protein detection. It also has the strongest neural functional context among the module genes and a substantial literature base.
- **Conclusion**: Established evidence supports CRMP1 as a neuronal signaling and cytoskeletal-regulatory protein. Its position suggests that it could connect neuronal morphology with the module's structural and metabolic genes, but that bridging role is a hypothesis because the supplied interaction resources do not support a known physical complex.

#### VPS35

- **Related proteins** (co-abundance neighbors): TUBGCP6 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS35 retromer complex component. This gene belongs to a group of vacuolar protein sorting (VPS) genes. The encoded protein is a component of a large multimeric complex, termed the retromer complex, involved in retrograde transport of proteins from endosomes to the trans-Golgi network. The close structural similarity between the yeast and human proteins that make up this complex suggests a similarity in function. Expression studie…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.743); neurodegenerative disease (0.553); young-onset Parkinson disease (0.503); Parkinson disease (0.482); Parkinson disease, dominant (0.370)
- **Europe PMC papers**: 3611
- **Why important**: VPS35 is the retromer complex component linked to TUBGCP6 in the module. Its established function involves retrograde transport from endosomes to the trans-Golgi network, protein transport, lysosome organization, and regulation of cellular signaling. It is localized to endosomes and lysosomes and has strong disease relevance to Parkinson disease and neurodegeneration. Its literature volume is substantial, and its neuronal disease associations make it important for interpreting the brain component.
- **Conclusion**: Established evidence supports VPS35 as an endosomal-retromer trafficking protein with major neurodegenerative disease relevance. Its co-abundance with TUBGCP6 may indicate coordination between microtubule organization and cargo trafficking, but the module does not establish that mechanism or a direct VPS35 interaction.

#### GNA11

- **Related proteins** (co-abundance neighbors): CRMP1 (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein subunit alpha 11. The protein encoded by this gene belongs to the family of guanine nucleotide-binding proteins (G proteins), which function as modulators or transducers in various transmembrane signaling systems. G proteins are composed of 3 units: alpha, beta and gamma. This gene encodes one of the alpha subunits (subunit alpha-11). Mutations in this gene have been associated with hypocalciuric hypercalcemia type…
- **Diseases (Open Targets)**: familial hypoparathyroidism (0.754); familial hypocalciuric hypercalcemia 2 (0.736); autosomal dominant hypocalcemia (0.611); congenital hemangioma (0.494); uveal melanoma (0.469)
- **Europe PMC papers**: 4418
- **Why important**: GNA11 is connected to CRMP1 and encodes a G-protein alpha subunit involved in transmembrane signal transduction, G-protein-coupled receptor signaling, adenylate cyclase modulation, and phospholipase C activation. It has brain protein detection, cell-type enhancement in colonocytes and enterocytes, immune-cell enhancement in neutrophils, and well-established associations with hypocalciuric hypercalcemia and hypocalcemia disorders. Its very extensive literature makes it a biologically well-characterized signaling component.
- **Conclusion**: Established evidence supports GNA11 as a signal-transduction regulator with endocrine and calcium-related disease associations. Its presence may indicate signaling-state variation within the module, but a specific connection to CRMP1-mediated neuronal cytoskeletal regulation remains hypothetical.

#### ACOT7

- **Related proteins** (co-abundance neighbors): CRMP1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA thioesterase 7. This gene encodes a member of the acyl coenzyme family. The encoded protein hydrolyzes the CoA thioester of palmitoyl-CoA and other long-chain fatty acids. Decreased expression of this gene may be associated with mesial temporal lobe epilepsy. Alternatively spliced transcript variants encoding distinct isoforms with different subcellular locations have been characterized. [provided by RefSeq, Jul …
- **Diseases (Open Targets)**: alcohol drinking (0.233); stroke disorder (0.173); diabetic ketoacidosis (0.114); Alzheimer disease (0.090); hepatocellular carcinoma (0.085)
- **Europe PMC papers**: 804
- **Why important**: ACOT7 is connected to CRMP1 and is tissue enhanced in brain. It hydrolyzes palmitoyl-CoA and other long-chain fatty-acyl-CoA species, linking the module to neuronal lipid and coenzyme-A metabolism. It shows enhancement in several specialized cell types, including photoreceptor, epithelial, reproductive, and mast-cell populations, and has associations with epilepsy, stroke, Alzheimer disease, and other disorders. Its literature is substantial enough to provide meaningful biological context.
- **Conclusion**: Established evidence supports ACOT7 as a fatty-acyl-CoA metabolic enzyme with strong brain relevance. Its module connection raises the hypothesis that lipid metabolism may support or modulate the cytoskeletal and neuronal signaling state, but no enriched term or reference interaction establishes that causal relationship.

## Module 2

**Tissue pair**: brain and stem_cells  
**Genes (8)**: CLTC, CSRP1, FHIP2A, PNPLA6, TANGO6, TRIO, WASHC4, WASHC5

### Function

The strongest interpretation is intracellular membrane-trafficking and actin-remodelling biology, centered on the WASH complex. (GO:CC WASH complex; q_global = 0.0476) is the only GO/KEGG term that passed global correction and identifies the WASH complex through WASHC4 and WASHC5. These genes are annotated with endosome organization, endosomal transport, and regulation of Arp2/3-mediated actin nucleation. The module graph is sparse, but the WASHC4–WASHC5 connection is exceptionally strong and is independently supported by (STRING Component WASH complex; within-query FDR = 0.0447) and (STRING COMPARTMENTS WASH complex; within-query FDR = 0.0485). The remaining genes suggest related cellular processes rather than a second statistically established pathway: PNPLA6 is linked to phospholipid metabolism and neurite outgrowth, TRIO to Rho-family signalling, actin cytoskeleton reorganization and axon guidance, TANGO6 to Golgi organization and protein secretion, FHIP2A to microtubule-associated protein transport, and CLTC to endocytosis and intracellular transport. No other GO or KEGG term passed global correction.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the individual genes have intracellular localizations or no reported secretome annotation. Most genes have low tissue specificity, while all are detected by immunohistochemistry in brain regions. Most show cell-type-enhanced rather than broadly uniform expression, with recurring enrichment for neutrophils or neutrophil progenitors and additional signals in oligodendrocytes, microglia, vascular or stromal populations, and other specialized cells. The blood-cell specificity summary is predominantly low, with an immune-cell-enhanced signal for TRIO, so the evidence does not establish that the module is simply a blood-cell contamination signature. Because the stem-cell samples have no matching HPA tissue category, HPA protein evidence cannot directly validate the stem-cell side. The shared signal may therefore reflect conserved intracellular machinery expressed across several cell types, with possible contributions from immune-lineage or progenitor populations.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC WASH complex | 0.0476 | WASHC4, WASHC5 |

### STRING and hu.MAP

STRING reports a high-confidence relationship only between WASHC4 and WASHC5, and (STRING Component WASH complex; within-query FDR = 0.0447) and (STRING COMPARTMENTS WASH complex; within-query FDR = 0.0485) independently identify the WASH complex. Thus, the core pair is already known and is not evidence for a novel physical interaction. hu.MAP likewise places WASHC4 and WASHC5 together in (hu.MAP huMAP3_05454.1) and in broader complexes (hu.MAP huMAP3_06652.1) through (hu.MAP huMAP3_12900.1). The pair is therefore a reproducible complex-level feature, while the other module genes are not represented in the listed hu.MAP complexes and have no listed STRING partners. This pattern suggests that the co-abundance module contains a validated WASH-complex core embedded in a broader, comparatively weakly connected expression context; it does not demonstrate that all module members form one physical complex.

**STRING interactions (score >= 0.7)**: 1 of 28 gene pairs: WASHC4–WASHC5 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component WASH complex (FDR = 0.0447, 2 genes); COMPARTMENTS WASH complex (FDR = 0.0485, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05454.1 (WASHC5, WASHC4; 2/2); huMAP3_06652.1 (WASHC5, WASHC4; 2/14); huMAP3_08077.1 (WASHC5, WASHC4; 2/16); huMAP3_10870.1 (WASHC5, WASHC4; 2/20); huMAP3_12900.1 (WASHC5, WASHC4; 2/50)

### Novelty

The WASHC4–WASHC5 association and its WASH-complex annotation are established rather than novel, because they are supported by the globally corrected term (GO:CC WASH complex; q_global = 0.0476), STRING evidence (STRING Component WASH complex; within-query FDR = 0.0447) and (STRING COMPARTMENTS WASH complex; within-query FDR = 0.0485), and several hu.MAP complexes (hu.MAP huMAP3_05454.1) through (hu.MAP huMAP3_12900.1). The potentially new aspect is the conservation of co-abundance between this WASH-complex core and TANGO6, CSRP1, PNPLA6, TRIO, FHIP2A, and CLTC across brain and stem-cell groups. However, the fact sheet does not establish that these pairwise relationships are new molecular interactions, and absence from the listed STRING or hu.MAP records cannot prove novelty. The defensible conclusion is that this is a potentially novel cross-tissue co-abundance configuration built around a known WASH-complex core, requiring independent replication and experimental testing.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of endosomal trafficking, membrane-associated actin dynamics, and intracellular lipid handling in neural or progenitor-associated cells. In this model, WASHC4 and WASHC5 provide the endosomal actin-remodelling core; PNPLA6 may connect membrane phospholipid turnover to neurite or cellular-process maintenance; TRIO may couple signalling to Rho-dependent cytoskeletal remodeling; and CLTC, TANGO6, and FHIP2A may represent associated trafficking, Golgi, and microtubule-transport demands. The observed co-abundance could therefore mark a shared state of active intracellular transport rather than a single physical complex. This remains a hypothesis because only the WASH-complex enrichment is globally significant and the module graph contains limited direct connectivity outside the WASHC4–WASHC5 pair.

### Important genes

#### WASHC4

- **Related proteins** (co-abundance neighbors): WASHC5 (0.84), PNPLA6 (0.82); STRING partners: WASHC5 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_05454.1, huMAP3_06652.1, huMAP3_08077.1, huMAP3_10870.1, huMAP3_12900.1
- **Function (MyGene.info)**: WASH complex subunit 4. This gene encodes a component of the WASH complex, which functions in the intracellular transport of endosomes. Mutations in this gene have been detected in individuals with autosomal recessive cognitive disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014].
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.611); Intellectual disability (0.345); mathematical ability (0.322); Abnormality of the skeletal system (0.148); corneal ulcer (0.140)
- **Europe PMC papers**: 116
- **Why important**: WASHC4 is a direct member of the globally supported WASH-complex term (GO:CC WASH complex; q_global = 0.0476), has the strongest STRING relationship in the module with WASHC5, and appears in every listed hu.MAP complex (hu.MAP huMAP3_05454.1) through (hu.MAP huMAP3_12900.1). Its annotations connect it to endosome organization, endosomal transport, Arp2/3-mediated actin nucleation, and nuclear-envelope budding. It also has a reported association with autosomal-recessive cognitive disability, making it particularly relevant to a brain-containing module.
- **Conclusion**: Established evidence supports WASHC4 as a core endosomal-trafficking and actin-regulatory component of the module. Its disease association makes altered WASH-dependent trafficking a plausible contributor to neural dysfunction, but the co-abundance data do not prove that WASHC4 drives the module or disease phenotype.

#### WASHC5

- **Related proteins** (co-abundance neighbors): WASHC4 (0.84); STRING partners: WASHC4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: huMAP3_05454.1, huMAP3_06652.1, huMAP3_08077.1, huMAP3_10870.1, huMAP3_12900.1
- **Function (MyGene.info)**: WASH complex subunit 5. This gene encodes a 134 kDa protein named strumpellin that is predicted to have multiple transmembrane domains and a spectrin-repeat-containing domain. This ubiquitously expressed gene has its highest expression in skeletal muscle. The protein is named for Strumpell disease; a form of hereditary spastic paraplegia (HSP). Spastic paraplegias are a diverse group of disorders in which the autosomal d…
- **Diseases (Open Targets)**: hereditary spastic paraplegia 8 (0.802); Ritscher-Schinzel syndrome 1 (0.727); Ritscher-Schinzel syndrome (0.711); hereditary disease (0.493); hereditary spastic paraplegia (0.350)
- **Europe PMC papers**: 238
- **Why important**: WASHC5 is the partner of WASHC4 in (GO:CC WASH complex; q_global = 0.0476), (STRING Component WASH complex; within-query FDR = 0.0447), (STRING COMPARTMENTS WASH complex; within-query FDR = 0.0485), and (hu.MAP huMAP3_05454.1) through (hu.MAP huMAP3_12900.1), making it the other unequivocal structural anchor. Its annotations include endosome organization, endosomal transport, actin-filament polymerization, Arp2/3 regulation, and positive regulation of neuron-projection development. It is also associated with hereditary spastic paraplegia and related hereditary syndromes.
- **Conclusion**: Established evidence identifies WASHC5 as a core WASH-complex component with direct relevance to endosomal and neuronal-process biology. The module is consistent with a role for WASHC5-dependent trafficking in neural maintenance, but it does not establish a specific mechanism linking this shared module to spastic paraplegia.

#### PNPLA6

- **Related proteins** (co-abundance neighbors): CSRP1 (0.84), WASHC4 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: patatin like domain 6, lysophospholipase. This gene encodes a phospholipase that deacetylates intracellular phosphatidylcholine to produce glycerophosphocholine. It is thought to function in neurite outgrowth and process elongation during neuronal differentiation. The protein is anchored to the cytoplasmic face of the endoplasmic reticulum in both neurons and non-neuronal cells. Mutations in this gene result in autosomal recessive spastic…
- **Diseases (Open Targets)**: hereditary spastic paraplegia 39 (0.811); ataxia-hypogonadism-choroidal dystrophy syndrome (0.807); trichomegaly-retina pigmentary degeneration-dwarfism syndrome (0.792); Laurence-Moon syndrome (0.678); inherited retinal dystrophy (0.488)
- **Europe PMC papers**: 868
- **Why important**: PNPLA6 connects the WASHC4-containing portion of the graph to CSRP1 and is annotated with phosphatidylcholine and glycerophospholipid metabolism. It is localized to the endoplasmic reticulum and cytosol, is described as relevant to neurite outgrowth and process elongation, and has substantial disease evidence for hereditary spastic paraplegia and several neurodegenerative or retinal syndromes.
- **Conclusion**: Established evidence supports PNPLA6 as a biologically meaningful link between lipid processing and neuronal morphology. Its position next to WASHC4 makes coordination between lipid homeostasis and endosomal trafficking plausible, but the module does not prove a direct PNPLA6–WASHC4 interaction.

#### TRIO

- **Related proteins** (co-abundance neighbors): TANGO6 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Immune cell enhanced; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: trio Rho guanine nucleotide exchange factor. This gene encodes a large protein that functions as a GDP to GTP exchange factor. This protein promotes the reorganization of the actin cytoskeleton, thereby playing a role in cell migration and growth. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 63, with macrocephaly (0.781); micrognathia-recurrent infections-behavioral abnormalities-mild intellectual disability syndrome (0.762); hereditary disease (0.552); Intellectual disability (0.521); syndromic intellectual disability (0.497)
- **Europe PMC papers**: 28706
- **Why important**: TRIO is connected to TANGO6 and contributes a signalling and cytoskeletal dimension to the module. Its annotated functions include Rho guanine-nucleotide exchange, actin-cytoskeleton reorganization, axon guidance, neuron-projection morphogenesis, and modulation of synaptic transmission. It has extensive literature and strong disease associations involving intellectual disability and neurodevelopmental syndromes.
- **Conclusion**: Established evidence supports TRIO as a major neuronal cytoskeletal and signalling gene that could contextualize the module's trafficking biology. Its inclusion may indicate coordinated regulation of membrane traffic and actin-dependent neuronal structure, but the sparse network does not establish a direct molecular relationship with the WASH complex.

#### CLTC

- **Related proteins** (co-abundance neighbors): TANGO6 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: clathrin heavy chain. Clathrin is a major protein component of the cytoplasmic face of intracellular organelles, called coated vesicles and coated pits. These specialized organelles are involved in the intracellular trafficking of receptors and endocytosis of a variety of macromolecules.  The basic subunit of the clathrin coat is composed of three heavy chains and three light chains. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: intellectual disability, autosomal dominant 56 (0.787); cancer (0.576); hereditary disease (0.540); Alzheimer disease (0.466); neurodegenerative disease (0.465)
- **Europe PMC papers**: 2902
- **Why important**: CLTC is connected to TANGO6 and is annotated as the clathrin heavy chain, a central component of coated vesicles and receptor-mediated endocytosis. Its functions include intracellular protein transport and endocytosis, and it has substantial literature and disease associations involving intellectual disability and neurodegeneration. Its endosomal and vesicular role is mechanistically compatible with the WASH-complex core.
- **Conclusion**: Established evidence supports CLTC as a biologically important trafficking gene whose function is compatible with the module's endosomal interpretation. The co-abundance pattern raises the possibility of coordinated clathrin- and WASH-dependent trafficking, but no direct interaction between CLTC and WASHC4 or WASHC5 is supplied.
