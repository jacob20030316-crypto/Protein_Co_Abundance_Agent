# Conserved co-abundance modules: autonomic_nervous_system and breast

## Module 0

**Tissue pair**: autonomic_nervous_system and breast  
**Genes (16)**: PPP2R5D, BRAP, CERS6, CNPY4, EHBP1, MSH3, NEMP1, PHF3, PI4KA, RPTOR, SENP3, SKA3, TBC1D24, ERCC4, XTBD1, ZNF638

### Function

The module does not support a single confidently established biological function from enrichment: no GO or KEGG term passed global correction, and STRING functional enrichment was absent. Its topology is highly hub-and-spoke, with CERS6 connected to every other module member, while the remaining genes are linked only to that hub. The gene annotations suggest several convergent cellular themes rather than one demonstrated pathway: membrane lipid and phosphoinositide biology through CERS6 and PI4KA, membrane trafficking through EHBP1 and TBC1D24, growth and nutrient-responsive signaling through RPTOR, genome maintenance through MSH3 and ERCC4, and cell-cycle or nuclear regulation through SKA3, SENP3, ZNF638 and related genes. These are annotation-based interpretations, not globally significant enrichment results. The shared signal may therefore represent coordinated cellular state or cellular composition rather than a discrete canonical pathway.

**Cell composition.** The module is not dominated by secreted or plasma proteins: the HPA summary identifies only one secreted gene, and most genes have low tissue specificity. It is also not strongly blood-cell enriched: most genes have low immune-cell specificity, several are not detected in immune cells, and only one is immune-cell enriched. The HPA profiles are heterogeneous, with signals in brain or glial cells, skeletal muscle, testis, erythrocyte progenitors, bone marrow, lymphoid tissue and other cell types. This heterogeneity argues against interpreting the module as a straightforward breast or autonomic-nervous-system lineage program. It could partly reflect shared cell types, tissue admixture, or broad cellular processes. Breast protein detection is present for many members, whereas matching autonomic-nervous-system protein data are unavailable, so the protein evidence does not establish matched protein abundance across the tissue pair.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship is ERCC4–MSH3, supporting a known connection between two DNA-repair proteins. The absence of other high-confidence STRING partners means that most co-abundance edges are not corroborated as established physical or functional interactions in this resource. The hu.MAP evidence consists of one complex containing PHF3 and XTBD1 among the module members, with the other reported complex components outside the module. Thus, the network contains a small amount of prior interaction or complex support, but most of its structure is not explained by known protein complexes. Co-abundance should consequently be treated as coordinated measurement behavior or shared regulation, not as proof of direct binding.

**STRING interactions (score >= 0.7)**: 1 of 120 gene pairs: ERCC4–MSH3 (0.936)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07778.1 (PHF3, XTBD1; 2/14)

### Novelty

This may be a novel tissue-shared co-abundance pattern, but the evidence does not establish a new molecular complex or pathway. The unusual combination of a CERS6-centered co-abundance structure with otherwise functionally diverse genes is not directly reproduced by the available STRING or hu.MAP evidence. However, absence from those resources cannot prove novelty, because databases are incomplete and co-abundance relationships need not be physical interactions. The strongest defensible claim is that this particular cross-tissue co-abundance organization appears under-characterized, while its component functions are individually established to varying degrees.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in which CERS6-linked membrane lipid metabolism is coordinated with phosphoinositide production, membrane trafficking, nutrient-responsive growth signaling and nuclear stress or genome-maintenance programs. CERS6 may act as the principal abundance hub because ceramide-related membrane biology is coupled to these processes, rather than because it physically binds every partner. In breast, the pattern could also be influenced by the mixture of epithelial, stromal and other cell populations. This hypothesis should be tested with independent cohorts, cell-type-resolved data, perturbation of CERS6 or PI4KA, and direct protein-interaction or localization assays.

### Important genes

#### CERS6

- **Related proteins** (co-abundance neighbors): PHF3 (0.97), XTBD1 (0.90), TBC1D24 (0.88), MSH3 (0.87), EHBP1 (0.85), SKA3 (0.85), RPTOR (0.85), BRAP (0.84), PI4KA (0.83), ZNF638 (0.83), PPP2R5D (0.82), ERCC4 (0.81), CNPY4 (0.81), NEMP1 (0.81), SENP3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ceramide synthase 6. Enables sphingosine N-acyltransferase activity. Involved in ceramide biosynthetic process. Located in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.349); frozen shoulder (0.306); type 2 diabetes mellitus (0.306); respiratory tract infectious disorder (0.280); sleep apnea syndrome (0.277)
- **Europe PMC papers**: 1355
- **Why important**: CERS6 is the central network hub, connecting to all other module members with the strongest overall network prominence. Its established annotation as a ceramide synthase places it in membrane sphingolipid and ceramide biosynthesis. It has broad disease associations including neurodegenerative disease and metabolic disorders, and it has extensive literature relative to most module members. Its HPA profile is broadly expressed with cell-type-enhanced signals rather than a simple tissue-restricted pattern.
- **Conclusion**: Established evidence supports CERS6 as the network anchor and as a ceramide-biosynthesis enzyme. It is the leading candidate for organizing the module-level signal, but the co-abundance network does not demonstrate that CERS6 physically regulates its neighbors. Its proposed coordinating role remains a hypothesis.

#### PI4KA

- **Related proteins** (co-abundance neighbors): CERS6 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphatidylinositol 4-kinase alpha. This gene encodes a phosphatidylinositol (PI) 4-kinase which catalyzes the first committed step in the biosynthesis of phosphatidylinositol 4,5-bisphosphate. The mammalian PI 4-kinases have been classified into two types, II and III, based on their molecular mass, and modulation by detergent and adenosine. The protein encoded by this gene is a type III enzyme that is not inhibited by adenosine. Al…
- **Diseases (Open Targets)**: polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis (0.749); spastic paraplegia 84, autosomal recessive (0.691); multiple intestinal atresia (0.595); PI4KA-related disorder (0.494); neurodegenerative disease (0.492)
- **Europe PMC papers**: 803
- **Why important**: PI4KA is a membrane phosphoinositide biosynthetic enzyme and is tissue enhanced in brain, with cell-type enhancement in plasmacytoid dendritic cells. Its annotations include phosphatidylinositol-mediated signaling and peripheral nervous-system myelination, making it relevant to the two tissue contexts while also fitting a membrane-lipid interpretation. It has established associations with severe neurodevelopmental and neurological disorders and a substantial literature base.
- **Conclusion**: Established evidence supports PI4KA as a biologically important membrane-lipid and signaling enzyme. Its presence is consistent with, but does not prove, a coordinated membrane-lipid program centered on CERS6. A functional connection within this module is therefore plausible but unconfirmed.

#### TBC1D24

- **Related proteins** (co-abundance neighbors): CERS6 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cell Junctions; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TBC1 domain family member 24. This gene encodes a protein with a conserved domain, referred to as the TBC domain, characteristic of proteins which interact with GTPases. TBC domain proteins may serve as GTPase-activating proteins for a particular group of GTPases, the Rab (Ras-related proteins in brain) small GTPases which are involved in the regulation of membrane trafficking. Mutations in this gene are associated with famili…
- **Diseases (Open Targets)**: DOORS syndrome (0.809); familial infantile myoclonic epilepsy (0.765); rolandic epilepsy-paroxysmal exercise-induced dystonia-writer's cramp syndrome (0.765); autosomal dominant nonsyndromic hearing loss 65 (0.736); autosomal recessive nonsyndromic hearing loss 86 (0.733)
- **Europe PMC papers**: 656
- **Why important**: TBC1D24 is connected directly to the module hub and encodes a protein associated with Rab-related membrane trafficking. Its HPA cell-type profile includes astrocytes, excitatory and inhibitory neurons, oligodendrocyte progenitors and other specialized cells, while its disease associations include familial epilepsy and hearing disorders. Its neuronal and trafficking annotations provide a potential bridge to autonomic nervous system biology.
- **Conclusion**: Established evidence supports TBC1D24 as a membrane-trafficking regulator with important neurological disease relevance. The module may link lipid composition to trafficking or neuronal membrane maintenance, but this connection is a mechanistic hypothesis rather than an enrichment-supported conclusion.

#### RPTOR

- **Related proteins** (co-abundance neighbors): CERS6 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Lysosomes; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: regulatory associated protein of MTOR complex 1. This gene encodes a component of a signaling pathway that regulates cell growth in response to nutrient and insulin levels. The encoded protein forms a stoichiometric complex with the mTOR kinase, and also associates with eukaryotic initiation factor 4E-binding protein-1 and ribosomal protein S6 kinase. The protein positively regulates the downstream effector ribosomal protein S6 kinase, and negat…
- **Diseases (Open Targets)**: neurodegenerative disease (0.440); Abnormality of the skeletal system (0.393); dengue disease (0.371); congestive heart failure (0.319); obesity disorder (0.304)
- **Europe PMC papers**: 6928
- **Why important**: RPTOR is a core component and regulator of mTOR complex one, integrating nutrient and insulin signals with cell growth, cell size and stress responses. It is directly connected to CERS6 in the module and has one of the largest literature bases among the genes listed. Its HPA profile is broadly expressed, with cell-type enhancement in thymic myoid cells, supporting a general cellular-state interpretation rather than a tissue-specific marker.
- **Conclusion**: Established evidence supports RPTOR as a major nutrient-responsive growth regulator. Its co-abundance with CERS6 is compatible with coupling between sphingolipid state and mTOR signaling, but the module alone cannot establish directionality, causation or a direct molecular interaction.

#### MSH3

- **Related proteins** (co-abundance neighbors): CERS6 (0.87); STRING partners: ERCC4 (0.936)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutS homolog 3. The protein encoded by this gene forms a heterodimer with MSH2 to form MutS beta, part of the post-replicative DNA mismatch repair system. MutS beta initiates mismatch repair by binding to a mismatch and then forming a complex with MutL alpha heterodimer. This gene contains a polymorphic 9 bp tandem repeat sequence in the first exon. The repeat is present 6 times in the reference genome sequence a…
- **Diseases (Open Targets)**: familial adenomatous polyposis 4 (0.743); endometrial carcinoma (0.651); hereditary neoplastic syndrome (0.576); endometrial cancer (0.374); endometrial neoplasm (0.370)
- **Europe PMC papers**: 4720
- **Why important**: MSH3 is a mismatch-repair protein that forms MutS beta with MSH2 and has extensive literature and disease relevance, including hereditary neoplastic conditions. It is the module member with the clearest known STRING relationship to another member, ERCC4, linking the network to established DNA-repair biology. Its nuclear localization is consistent with a genome-maintenance role distinct from the membrane-lipid annotations of the hub.
- **Conclusion**: Established evidence supports MSH3 as a DNA mismatch-repair factor and supports its known relationship with ERCC4. Whether its co-abundance with CERS6 reflects shared stress regulation, proliferation state or sample composition is unresolved; a direct CERS6-centered repair mechanism is not established.

#### ERCC4

- **Related proteins** (co-abundance neighbors): CERS6 (0.81); STRING partners: MSH3 (0.936)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ERCC excision repair 4, endonuclease catalytic subunit. The protein encoded by this gene forms a complex with ERCC1 and is involved in the 5' incision made during nucleotide excision repair. This complex is a structure specific DNA repair endonuclease that interacts with EME1. Defects in this gene are a cause of xeroderma pigmentosum complementation group F (XP-F), or xeroderma pigmentosum VI (XP6).[provided by RefSeq, Mar 2009].
- **Diseases (Open Targets)**: xeroderma pigmentosum group F (0.837); Fanconi anemia complementation group Q (0.808); xeroderma pigmentosum (0.780); xeroderma pigmentosum-Cockayne syndrome complex (0.731); XFE progeroid syndrome (0.730)
- **Europe PMC papers**: 2223
- **Why important**: ERCC4 is a DNA-repair endonuclease subunit that functions with ERCC1 in nucleotide-excision repair and other genome-maintenance processes. It is the partner of MSH3 in the only high-confidence STRING interaction reported for the module. Its disease associations include xeroderma pigmentosum and related repair disorders, and it has a substantial literature base.
- **Conclusion**: Established evidence supports ERCC4 as a genome-maintenance enzyme and supports its interaction with MSH3. The ERCC4–MSH3 pair may mark a DNA-repair or cellular-stress component within the module, but the broader connection to CERS6 and the tissue-shared pattern remains hypothetical.

## Module 1

**Tissue pair**: autonomic_nervous_system and breast  
**Genes (22)**: ABI2, CCNH, CORO2A, FAM107B, GPRIN1, ITPR1, KIF22, KIF5C, LNPK, LRRFIP2, MMTAG2, MAP2, MTCL2, NELFE, POGZ, RBM34, POLR2A, VIPAS39, DNTTIP2, TOE1, TP53BP1, ZBTB35

### Function

No GO or KEGG term passed global correction, so the module does not have a globally supported pathway annotation. Its gene-level annotations nevertheless suggest a neuron-associated structural and trafficking program: GPRIN1 is linked to neurite outgrowth and growth cones; MAP2 supports dendritic microtubule organization; KIF5C supports microtubule-based cargo and synaptic-vesicle transport; and ITPR1 mediates calcium release from the endoplasmic reticulum. The module also contains genes involved in transcription, RNA processing, chromatin regulation, DNA-damage responses, and intracellular sorting. The network therefore appears to be a mixed co-abundance signature, with a neuronal cytoskeletal and signaling component rather than evidence for one formally enriched biochemical pathway.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins, and it is not blood-cell enriched according to HPA: most genes have low immune-cell specificity and no enriched blood-cell category was reported. Only MTCL2 is annotated as secreted to blood. The HPA pattern instead points toward cell-type composition, especially neuronal and glial contexts: several genes are enhanced or enriched in brain-related tissues or neural cell types, while many others have broad tissue specificity. Breast protein detection for many genes shows that the genes can be present in breast samples, but does not establish a breast-specific function. A shared autonomic-nervous-system and breast module could therefore partly reflect shared neural or other cellular composition, technical covariation, or a broadly expressed cellular state rather than a tissue-independent pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides limited direct support for a physical interaction network. The known relationships are CCNH with POLR2A and NELFE with POLR2A, consistent with connections to RNA polymerase transcriptional regulation and transcriptional pausing. No STRING functional enrichment was reported. The hu.MAP evidence is also limited: (hu.MAP huMAP3_05807.1) places DNTTIP2 and MMTAG2 in the same large reported complex, but most of that complex is outside the module. Thus, the co-abundance edges should not be interpreted as established protein-protein interactions. The databases support a few local molecular relationships, while the broader module primarily represents coordinated abundance.

**STRING interactions (score >= 0.7)**: 2 of 231 gene pairs: CCNH–POLR2A (0.988); NELFE–POLR2A (0.955)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05807.1 (DNTTIP2, MMTAG2; 2/81)

### Novelty

This may be a novel cross-tissue co-abundance observation, but the fact sheet does not establish a new molecular complex or a newly discovered pathway. Most module relationships are absent from the reported STRING and hu.MAP matches, yet database absence alone cannot demonstrate novelty because interaction databases are incomplete and co-abundance does not require direct physical binding. The strongest interpretation is that the shared module architecture is a candidate new systems-level association that requires replication, adjustment for cell composition, and experimental testing.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of a neural or neuron-like cellular program that couples neurite or dendritic cytoskeletal organization, microtubule-dependent transport, vesicle handling, and intracellular calcium signaling. GPRIN1, MAP2, and KIF5C could represent the structural and transport arm, while ITPR1 could connect that arm to calcium-dependent signaling. The transcriptional and RNA-processing genes may reflect the biosynthetic state of the same cells or a parallel abundance program rather than a single physical complex. In breast samples, this hypothesis should be tested against neural-cell admixture, stromal composition, and other shared cell-type signals before assigning the module a breast-specific mechanism.

### Important genes

#### GPRIN1

- **Related proteins** (co-abundance neighbors): VIPAS39 (0.99), MAP2 (0.94), LNPK (0.93), KIF5C (0.89), ABI2 (0.89), CCNH (0.88), DNTTIP2 (0.85), NELFE (0.84), KIF22 (0.84), LRRFIP2 (0.83), POLR2A (0.82), POGZ (0.81), FAM107B (0.81), MTCL2 (0.81), RBM34 (0.80), TOE1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein regulated inducer of neurite outgrowth 1. Predicted to enable phosphoprotein binding activity. Predicted to be involved in neuron projection development. Predicted to be located in growth cone. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: gastric cancer (0.077); lung adenocarcinoma (0.074); non-small cell lung carcinoma (0.057); hemochromatosis type 5 (0.038); neoplasm (0.034)
- **Europe PMC papers**: 409
- **Why important**: GPRIN1 is the central network hub in the module and connects the strongest neighborhood containing VIPAS39, MAP2, LNPK, KIF5C, ABI2, CCNH, DNTTIP2, and NELFE. HPA links it to brain, pituitary, retina, and multiple neuronal cell types. Its annotation connects it to neurite outgrowth, neuron projection development, growth cones, and the plasma membrane. It therefore provides the clearest bridge between the module's network structure and its neural interpretation. Its substantial literature record supports relevance, although the module does not prove that GPRIN1 directly binds all of its co-abundant neighbors.
- **Conclusion**: Established evidence supports GPRIN1 as a neural-associated neurite-development gene and as the module's principal co-abundance hub. The hypothesis that it organizes the entire shared module is plausible from network position but remains unproven.

#### MAP2

- **Related proteins** (co-abundance neighbors): GPRIN1 (0.94), ITPR1 (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: microtubule associated protein 2. This gene encodes a protein that belongs to the microtubule-associated protein family. The proteins of this family are thought to be involved in microtubule assembly, which is an essential step in neurogenesis. The products of similar genes in rat and mouse are neuron-specific cytoskeletal proteins that are enriched in dentrites, implicating a role in determining and stabilizing dentritic shape du…
- **Diseases (Open Targets)**: functional laterality (0.468); handedness (0.400); risk-taking behaviour (0.368); placenta praevia (0.345); septic shock (0.337)
- **Europe PMC papers**: 21514
- **Why important**: MAP2 has strong neural and retinal HPA enrichment and is enhanced in several neuronal and glial cell types. Its annotation supports dendrite development, microtubule cytoskeleton organization, and regulation of microtubule polymerization. It connects directly to GPRIN1 and ITPR1, linking the central hub to both neuronal structure and calcium signaling. MAP2 also has a very large literature base, making its functional interpretation substantially more established than that of poorly characterized module members.
- **Conclusion**: Established evidence supports MAP2 as a neuronal cytoskeletal and dendritic marker that strengthens the neural interpretation of the module. Its presence does not show that the whole module operates in dendrites, because shared abundance may still arise from cell composition.

#### KIF5C

- **Related proteins** (co-abundance neighbors): LNPK (0.98), GPRIN1 (0.89); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Cytosol, Equatorial segment, Connecting piece; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 5C. The protein encoded by this gene is a kinesin heavy chain subunit involved in the transport of cargo within the central nervous system. The encoded protein, which acts as a tetramer by associating with another heavy chain and two light chains, interacts with protein kinase CK2. Mutations in this gene have been associated with complex cortical dysplasia with other brain malformations-2. Two transcr…
- **Diseases (Open Targets)**: Genetic central nervous system malformation (0.754); neurodegenerative disease (0.435); complex cortical dysplasia with other brain malformations (0.370); cerebral cortical dysplasia (0.271); disturbances of sensation of smell and taste (0.262)
- **Europe PMC papers**: 1225
- **Why important**: KIF5C is tissue enriched in brain and is associated with neuronal cell types. Its function as a kinesin heavy-chain subunit supports cargo movement in the central nervous system, vesicle transport along microtubules, and synaptic vesicle transport. Its co-abundance links to GPRIN1 and LNPK connect neuronal transport with the module's neurite and endoplasmic-reticulum-related signals. KIF5C also has a substantial literature record and established associations with cortical malformation and other nervous-system phenotypes.
- **Conclusion**: Established evidence supports KIF5C as the module's most informative neuronal motor and transport component. A coordinated transport mechanism involving GPRIN1 and LNPK is a reasonable hypothesis, but the co-abundance graph does not establish direct cooperation.

#### ITPR1

- **Related proteins** (co-abundance neighbors): VIPAS39 (0.82), MAP2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inositol 1,4,5-trisphosphate receptor type 1. This gene encodes an intracellular receptor for inositol 1,4,5-trisphosphate. Upon stimulation by inositol 1,4,5-trisphosphate, this receptor mediates calcium release from the endoplasmic reticulum. Mutations in this gene cause spinocerebellar ataxia type 15, a disease associated with an heterogeneous group of cerebellar disorders. Multiple transcript variants have been identified for this gene. […
- **Diseases (Open Targets)**: aniridia-cerebellar ataxia-intellectual disability syndrome (0.824); spinocerebellar ataxia type 29 (0.812); spinocerebellar ataxia type 15/16 (0.767); hereditary disease (0.534); uterine corpus leiomyoma (0.460)
- **Europe PMC papers**: 3270
- **Why important**: ITPR1 encodes the intracellular inositol-trisphosphate receptor that releases calcium from the endoplasmic reticulum. It is connected in the module to MAP2 and VIPAS39, providing a signaling link between neuronal structure, organelle handling, and calcium homeostasis. Its annotations include calcium transport and signaling, and its disease associations include several cerebellar ataxia syndromes. Its literature record is extensive, supporting a well-established functional interpretation.
- **Conclusion**: Established evidence supports ITPR1 as a calcium-signaling component with particular relevance to neural function. The hypothesis that ITPR1-dependent calcium signaling coordinates the other module processes is mechanistically coherent but is not demonstrated by the enrichment or interaction evidence.

#### POLR2A

- **Related proteins** (co-abundance neighbors): GPRIN1 (0.82); STRING partners: CCNH (0.988), NELFE (0.955)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase II subunit A. This gene encodes the largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene contains a carboxy terminal domain composed of heptapeptide repeats that are essential for polymerase activity. These repeats contain serine and threonine residues that are phosphorylated in actively transcribing RNA polymerase. In addition, …
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and variable intellectual and behavioral abnormalities (0.738); HIV infectious disease (0.600); hereditary disease (0.479); syndromic intellectual disability (0.462); Orthomyxoviridae infectious disease (0.374)
- **Europe PMC papers**: 4546
- **Why important**: POLR2A is the largest subunit of RNA polymerase II and is directly supported by STRING relationships with CCNH and NELFE. These links provide the clearest known molecular relationships in the module and point to transcriptional initiation, elongation, and regulation. POLR2A is also associated with neurodevelopmental and intellectual-disability phenotypes and has a large literature base. Its position is peripheral in the co-abundance graph, so its importance comes more from molecular interpretation than from network centrality.
- **Conclusion**: Established evidence supports POLR2A as a general transcriptional machinery component and explains the local STRING-supported CCNH and NELFE relationships. It should not be taken as evidence that the entire module is a transcription complex or that its transcriptional genes are mechanistically coupled to the neuronal genes.

## Module 2

**Tissue pair**: autonomic_nervous_system and breast  
**Genes (21)**: ADAM10, ATP11C, CABP7, CAPN5, ERLIN1, FSD1, GABPA, IFIT5, JAM3, KDM3B, KRI1, ABCC1, NNT, NUP214, PRRC2C, PSPC1, RRP1, SMAP, TACC3, TNIK, XRN2

### Function

The module does not support a single established pathway-level function: no GO or KEGG term passed global correction, and there was no STRING functional enrichment. Its gene annotations instead suggest a mixed cellular program involving Wnt and MAPK-linked signaling through TNIK, junctional adhesion and barrier biology through JAM3, membrane lipid asymmetry through ATP11C, mitochondrial NADPH and redox maintenance through NNT, lipid and stress responses through ERLIN1 and PRRC2C, and membrane proteolysis or Notch-related signaling through ADAM10. The network is centered on TNIK, with several weakly connected branches rather than a densely interconnected canonical pathway. These observations support a cautious interpretation as a cross-tissue co-abundance pattern involving signaling, membrane organization, cellular stress, and metabolic state, not as proof of one unified biochemical process.

**Cell composition.** The module is not dominated by secreted or plasma proteins: only JAM3 and ADAM10 have secretome annotations, and most proteins are intracellular or membrane-associated. Most genes have low tissue specificity, while a smaller subset is enriched in liver, brain, skeletal muscle, intestine, or testis. Cell-type annotations are more prominent than tissue-level specificity, with recurrent signals in neutrophils, cardiomyocytes, choroid plexus epithelial cells, and neuronal or glial populations. Some genes show immune-cell enhancement or group enrichment, but the module is not uniformly blood-cell specific. Therefore, contamination by blood or shared immune cells is possible, especially for the neutrophil-associated component, but the HPA profile does not establish that the entire module is a blood-derived artifact. Breast protein detection is present for many genes, whereas autonomic-nervous-system protein data are unavailable in the matched HPA summary, limiting tissue-level interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module gene pair reaches the supplied high-confidence STRING interaction threshold, and no hu.MAP complex contains multiple module members. Thus the co-abundance edges are not independently supported here as established physical interactions or membership in a known multiprotein complex. Several genes nevertheless have well-described individual functions, including TNIK as a Wnt-linked serine/threonine kinase, JAM3 as a junctional adhesion molecule, ATP11C as a phospholipid flippase, NNT as a mitochondrial redox enzyme, and ADAM10 as a membrane sheddase. The network therefore may capture coordinated abundance across cellular compartments or shared cell-state composition rather than direct protein binding.

**STRING interactions (score >= 0.7)**: 0 of 210 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a new tissue-pair co-abundance observation, but it cannot be called a newly discovered molecular complex or pathway. The module has no high-confidence STRING pair, no hu.MAP complex, and no globally significant GO or KEGG term. Those absences do not prove novelty: sparse or context-dependent regulation, cell-mixture effects, incomplete database coverage, and correlations between proteins in different compartments can all produce this pattern. A defensible novelty claim is therefore limited to the reported conservation of this particular co-abundance pattern between autonomic nervous system and breast, pending replication in independent cohorts and validation at the protein or functional level.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cell-state program coupling membrane and junction remodeling to intracellular stress and metabolic adaptation. In this model, TNIK-associated signaling could coordinate cytoskeletal or transcriptional responses; JAM3 and ADAM10 could alter cell-cell contacts and ectodomain processing; ATP11C could maintain phospholipid asymmetry; and NNT could supply reducing power for biosynthesis and reactive-oxygen control. The pattern could be strengthened by shared epithelial, vascular, neural, muscle, or immune-cell contributions across the two tissues rather than by direct physical interaction among all module proteins. This hypothesis should be tested by cell-composition adjustment, replication across additional tissue datasets, perturbation of TNIK or membrane-lipid handling, and measurement of junctional, redox, and signaling phenotypes.

### Important genes

#### TNIK

- **Related proteins** (co-abundance neighbors): NNT (0.86), ATP11C (0.85), KDM3B (0.84), PRRC2C (0.83), PSPC1 (0.83), GABPA (0.82), ADAM10 (0.81), RRP1 (0.81), NUP214 (0.81), XRN2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TRAF2 and NCK interacting kinase. Wnt signaling plays important roles in carcinogenesis and embryonic development. The protein encoded by this gene is a serine/threonine kinase that functions as an activator of the Wnt signaling pathway. Mutations in this gene are associated with an autosomal recessive form of cognitive disability. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided …
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.536); neurodegenerative disease (0.532); autosomal recessive non-syndromic intellectual disability (0.512); alcohol drinking (0.348); Myoclonus (0.327)
- **Europe PMC papers**: 1284
- **Why important**: TNIK is the clear network hub, connecting signaling, membrane, cytoskeletal, transcriptional, and RNA-associated genes. Its documented role as a Wnt-pathway serine/threonine kinase and its annotations for MAPK cascade, cytoskeletal organization, and intracellular signal transduction make it the strongest integrative candidate. It is also associated with cognitive disability, skeletal abnormalities, and neurodegenerative disease, and it has extensive literature support.
- **Conclusion**: Established evidence supports TNIK as the principal network organizing candidate and as a plausible signaling regulator. It is not established that TNIK causally drives the shared module; its hub position may instead reflect abundance coupling or cell-state composition.

#### JAM3

- **Related proteins** (co-abundance neighbors): ABCC1 (0.86), ERLIN1 (0.84), NNT (0.84), ATP11C (0.82), IFIT5 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: junctional adhesion molecule 3. Tight junctions represent one mode of cell-to-cell adhesion in epithelial or endothelial cell sheets, forming continuous seals around cells and serving as a physical barrier to prevent solutes and water from passing freely through the paracellular space. The protein encoded by this immunoglobulin superfamily gene member is localized in the tight junctions between high endothelial cells. Unlike oth…
- **Diseases (Open Targets)**: porencephaly-microcephaly-bilateral congenital cataract syndrome (0.787); atrial fibrillation (0.433); corneal dystrophy (0.244); stroke disorder (0.238); alcohol drinking (0.237)
- **Europe PMC papers**: 1864
- **Why important**: JAM3 is a central connector in the membrane-associated branch and links the module to junctional adhesion, angiogenesis, migration, and barrier biology. HPA places it in choroid plexus epithelial cells, oligodendrocytes, platelets, and other specialized cell types, and annotates it as secreted to blood. Its association with porencephaly-microcephaly-bilateral congenital cataract syndrome and vascular or cardiac disorders gives it disease relevance, while its literature support is substantial.
- **Conclusion**: Established evidence supports JAM3 as a barrier and cell-adhesion marker that could report shared epithelial, endothelial, or specialized neural-cell biology. A direct JAM3-mediated mechanism connecting the other module genes remains hypothetical.

#### NNT

- **Related proteins** (co-abundance neighbors): TNIK (0.86), JAM3 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nicotinamide nucleotide transhydrogenase. This gene encodes an integral protein of the inner mitochondrial membrane. The enzyme couples hydride transfer between NAD(H) and NADP(+) to proton translocation across the inner mitochondrial membrane. Under most physiological conditions, the enzyme uses energy from the mitochondrial proton gradient to produce high concentrations of NADPH. The resulting NADPH is used for biosynthesis and in free …
- **Diseases (Open Targets)**: familial glucocorticoid deficiency (0.638); neurodegenerative disease (0.497); hereditary disease (0.453); atypical hemolytic-uremic syndrome with DGKE deficiency (0.416); Abnormality of the skeletal system (0.396)
- **Europe PMC papers**: 6111
- **Why important**: NNT connects the TNIK and JAM3 portions of the network and encodes a mitochondrial enzyme that generates NADPH for biosynthesis and reactive-oxygen control. Its HPA profile includes cardiomyocytes, hepatocytes, choroid plexus epithelial cells, and myonuclei, matching the cross-tissue nature of the module. It has extensive literature and disease associations involving glucocorticoid deficiency, neurodegenerative disease, and other hereditary phenotypes.
- **Conclusion**: Established evidence supports NNT as a mitochondrial redox and metabolic-state indicator. Its presence is consistent with oxidative-stress adaptation, but the network does not establish that redox control is the primary function of the module.

#### ATP11C

- **Related proteins** (co-abundance neighbors): TNIK (0.85), CAPN5 (0.84), JAM3 (0.82), SMAP (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase phospholipid transporting 11C (ATP11C blood group). Enables phosphatidylethanolamine flippase activity and phosphatidylserine flippase activity. Predicted to be involved in phospholipid translocation; positive regulation of B cell differentiation; and pre-B cell differentiation. Located in endoplasmic reticulum and plasma membrane. Is integral component of plasma membrane. Implicated in X-linked congenital hemolytic anemia. [provided by Alliance of…
- **Diseases (Open Targets)**: familial hemolytic anemia (0.558); neutropenia, severe congenital, 2, autosomal dominant (0.069); autosomal dominant severe congenital neutropenia (0.069); Rh deficiency syndrome (0.067); neonatal intrahepatic cholestasis due to citrin deficiency (0.062)
- **Europe PMC papers**: 536
- **Why important**: ATP11C occupies a bridge position between TNIK, JAM3, CAPN5, and SMAP. It encodes a phosphatidylserine and phosphatidylethanolamine flippase involved in membrane lipid asymmetry, and is also linked to B-cell differentiation and congenital hemolytic anemia. Its liver-enhanced HPA profile and membrane or endoplasmic-reticulum functions make it a plausible connection between cell-surface organization and intracellular lipid handling.
- **Conclusion**: Established evidence supports ATP11C as a membrane-lipid homeostasis gene with hematologic relevance. Its proposed role as a coordinator of the module is a hypothesis based on network position and functional complementarity, not a demonstrated interaction.

#### ADAM10

- **Related proteins** (co-abundance neighbors): TNIK (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ADAM metallopeptidase domain 10. Members of the ADAM family are cell surface proteins with a unique structure possessing both potential adhesion and protease domains. This gene encodes and ADAM family member that cleaves many proteins including TNF-alpha and E-cadherin. Alternate splicing results in multiple transcript variants encoding different proteins that may undergo similar processing. [provided by RefSeq, Feb 2016].
- **Diseases (Open Targets)**: reticulate acropigmentation of Kitamura (0.679); Alzheimer disease 18 (0.621); Alzheimer disease (0.522); dementia (0.415); schizophrenia (0.354)
- **Europe PMC papers**: 11139
- **Why important**: ADAM10 is directly connected to the TNIK hub and provides a functionally distinctive membrane-proteolysis component. It cleaves TNF-alpha and E-cadherin and is annotated for ectodomain proteolysis, cell adhesion, and Notch signaling. It has very extensive literature and disease associations spanning neurodegeneration, dementia, schizophrenia, and inherited skin disease. HPA places it at the plasma membrane and in vesicles, with neutrophil cell-type enhancement.
- **Conclusion**: Established evidence supports ADAM10 as a regulator of cell-surface signaling and adhesion through proteolytic shedding. Its involvement in this shared module could indicate remodeling of cell-cell communication, but causality and direction cannot be inferred from co-abundance alone.

## Module 3

**Tissue pair**: autonomic_nervous_system and breast  
**Genes (14)**: INA, AKAP9, BCL2L1, FAM241A, LARP7, NAB2, IVNS1ABP, UPF3B, POLR1A, POLR3B, SYT1, TMEM38B, UQCC4, VGF

### Function

(GO:BP transcription by RNA polymerase III; q_global = 0.0158) supports a transcriptional function involving transcription by RNA polymerase III, contributed by IVNS1ABP, NAB2, POLR1A, and POLR3B. POLR1A and POLR3B are the clearest mechanistic anchors: POLR1A is the catalytic subunit of RNA polymerase I, whereas POLR3B is a catalytic subunit of RNA polymerase III. The remaining annotations suggest that the module also captures neuronal and neuroendocrine biology, including synaptic vesicle release through SYT1, neuronal structural organization through INA, calcium handling through TMEM38B, and secretory or neuroendocrine biology through VGF. These additional themes are gene-level annotations rather than globally corrected enrichment. The network therefore appears to combine a transcriptional core with a neuronal or neuroendocrine co-abundance component, rather than representing one fully established physical complex.

**Cell composition.** The module is not dominated by plasma or secreted proteins: VGF is the only gene annotated as secreted to blood. It is also not broadly blood-cell enriched. Most genes have low immune-cell specificity or are not detected in immune cells, although SYT1 has immune-cell enhancement in memory and naive B cells and IVNS1ABP has enrichment in neutrophil-related cell types. HPA evidence instead points toward a mixed cellular composition with brain, pituitary, retina, neuronal, neuroendocrine, skeletal-muscle, and breast-associated signals. Several genes are broadly expressed, while others show neuronal or specialized-cell enrichment. The shared module could therefore partly reflect shared cell types or cellular admixture across autonomic nervous system and breast samples, rather than a breast-specific molecular program. Breast protein detection is present for many genes, but the absence of matching autonomic-nervous-system protein data limits direct tissue-level comparison.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP transcription by RNA polymerase III | 0.0158 | IVNS1ABP, NAB2, POLR1A, POLR3B |

### STRING and hu.MAP

STRING provides one high-confidence relationship, POLR1A–POLR3B, supporting a known connection between the two polymerase-associated genes. STRING supplies no enrichment result for the module as a whole. hu.MAP complexes (hu.MAP huMAP3_09057.1) through (hu.MAP huMAP3_11092.1) repeatedly contain POLR1A and POLR3B together, alongside many RNA polymerase, transcription-associated, assembly, and regulatory proteins. This convergence strengthens the interpretation that these two genes represent a real transcriptional-complex signal. However, the other module genes are not represented in those hu.MAP complexes, and hu.MAP co-membership does not establish direct physical interaction between every module member. The sparse STRING structure therefore argues against interpreting the entire module as one established protein complex.

**STRING interactions (score >= 0.7)**: 1 of 91 gene pairs: POLR1A–POLR3B (0.99)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09057.1 (POLR1A, POLR3B; 2/36); huMAP3_08487.1 (POLR1A, POLR3B; 2/37); huMAP3_06426.1 (POLR1A, POLR3B; 2/38); huMAP3_14318.1 (POLR1A, POLR3B; 2/58); huMAP3_11092.1 (POLR1A, POLR3B; 2/65)

### Novelty

The shared co-abundance module may be a new observation in this tissue-pair analysis, but novelty is not established by the supplied evidence alone. The POLR1A–POLR3B relationship and their participation in polymerase-related hu.MAP complexes are already known, and the neuronal, vesicular, cytoskeletal, calcium-handling, and survival functions of individual genes are also established. What may be novel is their reproducible co-abundance across autonomic nervous system and breast, particularly the apparent connection between a polymerase-associated pair and VGF-centered neuronal or secretory genes. This should be treated as a candidate context-specific association requiring replication in independent cohorts, control for cell composition, and testing against known expression programs. Absence of most module edges from STRING or hu.MAP is not evidence that the remaining relationships are novel.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of two partially overlapping programs. One component is a conserved nuclear transcription and RNA-processing state marked by POLR1A, POLR3B, IVNS1ABP, and NAB2. The other is a neuronal or neuroendocrine structural and secretory state marked by VGF, SYT1, and INA, with possible contributions from calcium handling, mitochondrial stress regulation, and Golgi organization. VGF may act as the co-abundance bridge linking these otherwise sparsely connected programs, but this is a network interpretation rather than evidence of direct VGF binding to the other proteins. In breast samples, the signal could arise from specialized epithelial, stromal, vascular, neuroendocrine-like, or contaminating neural-associated cells; in autonomic nervous system samples, it may reflect neuronal cellular composition. This hypothesis should be tested by cell-type deconvolution, single-cell or spatial measurements, and validation of coordinated expression at the protein level.

### Important genes

#### VGF

- **Related proteins** (co-abundance neighbors): TMEM38B (0.93), BCL2L1 (0.91), FAM241A (0.89), UPF3B (0.86), POLR3B (0.86), LARP7 (0.84), IVNS1ABP (0.81), POLR1A (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Not detected in immune cells; location Golgi apparatus, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VGF nerve growth factor inducible. This gene is specifically expressed in a subpopulation of neuroendocrine cells, and is upregulated by nerve growth factor. The structural organization of this gene is similar to that of the rat gene, and both the translated and the untranslated regions show a high degree of sequence similarity to the rat gene. The encoded secretory protein also shares similarities with the secretogranin/chromogran…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.144); amyotrophic lateral sclerosis (0.121); Alzheimer disease (0.108); neoplasm (0.099); infection (0.097)
- **Europe PMC papers**: 3253
- **Why important**: VGF is the central network connector and has the strongest weighted connectivity in the module. HPA places it in brain and pituitary group-enriched tissue categories, identifies pancreatic islet-cell enrichment, and annotates it as secreted to blood. Its gene-level annotations include neuronal synaptic plasticity, neuropeptide signaling, and response to cAMP. It also has a substantial literature and disease links involving neurological and neurodegenerative phenotypes. Its central position makes it the strongest candidate for explaining why neuronal or neuroendocrine biology is coupled to the rest of the module.
- **Conclusion**: Established evidence supports VGF as a neuroendocrine or neuronal secretory protein and as the principal co-abundance connector in this module. The hypothesis that VGF mediates a mechanistic link between the polymerase-associated genes and synaptic genes is not established; its network centrality may instead reflect shared cell composition or coordinated regulation.

#### SYT1

- **Related proteins** (co-abundance neighbors): INA (0.90), AKAP9 (0.84), UQCC4 (0.84), FAM241A (0.82), NAB2 (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: synaptotagmin 1. This gene encodes a member of the synaptotagmin protein family. The synaptotagmins are integral membrane proteins of synaptic vesicles that serve as calcium sensors in the process of vesicular trafficking and exocytosis. The encoded protein participates in triggering neurotransmitter release at the synapse in response to calcium binding. Mutations in this gene are associated with Baker-Gordon synd…
- **Diseases (Open Targets)**: infantile hypotonia-oculomotor anomalies-hyperkinetic movements-developmental delay syndrome (0.760); Intellectual disability (0.555); botulism (0.551); intelligence (0.517); hereditary disease (0.449)
- **Europe PMC papers**: 3724
- **Why important**: SYT1 is a major network connector on the synaptic branch and is group enriched in brain and retina. It is enhanced in neuronal, cone photoreceptor, adrenal-medulla, and breast-associated cell categories, with additional immune-cell enhancement in B-cell populations. Its established function as a calcium sensor for synaptic-vesicle fusion and neurotransmitter release gives the module a strong vesicular and neuronal interpretation. It has a substantial literature and well-supported developmental and neurological disease associations.
- **Conclusion**: Established evidence supports SYT1 as a calcium-dependent vesicle-fusion and neurotransmitter-release protein that marks neuronal or neuroendocrine cellular biology. Its inclusion does not prove active neurotransmission in breast tissue; a shared specialized-cell population or sample-composition effect remains a plausible explanation.

#### POLR1A

- **Related proteins** (co-abundance neighbors): VGF (0.80); STRING partners: POLR3B (0.99)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoli fibrillar center; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_09057.1, huMAP3_08487.1, huMAP3_06426.1, huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase I subunit A. The protein encoded by this gene is the largest subunit of the RNA polymerase I complex. The encoded protein represents the catalytic subunit of the complex, which transcribes DNA into ribosomal RNA precursors. Defects in this gene are a cause of the Cincinnati type of acrofacial dysostosis. [provided by RefSeq, May 2016].
- **Diseases (Open Targets)**: choanal atresia-hearing loss-cardiac defects-craniofacial dysmorphism syndrome (0.780); acrofacial dysostosis Cincinnati type (0.723); leukodystrophy, hypomyelinating, 27 (0.459); acrofacial dysostosis (0.372); microtia (0.370)
- **Europe PMC papers**: 555
- **Why important**: POLR1A is one of the two genes with the only high-confidence STRING relationship and is present with POLR3B in every reported hu.MAP complex (hu.MAP huMAP3_09057.1) through (hu.MAP huMAP3_11092.1). It is the largest subunit of RNA polymerase I and contributes to the globally corrected RNA-polymerase transcription term (GO:BP transcription by RNA polymerase III; q_global = 0.0158). Its nucleolar localization and disease associations involving craniofacial development and leukodystrophy make it a strong marker of a conserved nuclear transcriptional program.
- **Conclusion**: Established evidence supports POLR1A as a polymerase-associated transcription factor of the module and as part of a known relationship with POLR3B. The evidence does not show that POLR1A directly interacts with the neuronal or secretory genes in the module; that broader connection is a co-abundance observation.

#### POLR3B

- **Related proteins** (co-abundance neighbors): VGF (0.86); STRING partners: POLR1A (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_09057.1, huMAP3_08487.1, huMAP3_06426.1, huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase III subunit B. This gene encodes the second largest subunit of RNA polymerase III, the polymerase responsible for synthesizing transfer and small ribosomal RNAs in eukaryotes. The largest subunit and the encoded protein form the catalytic center of RNA polymerase III. Mutations in this gene are a cause of hypomyelinating leukodystrophy. Alternatively spliced transcript variants encoding multiple isoforms have be…
- **Diseases (Open Targets)**: hypomyelination-hypogonadotropic hypogonadism-hypodontia syndrome (0.796); leukodystrophy, hypomyelinating, 8, with or without oligodontia and/or hypogonadotropic hypogonadism (0.747); Charcot-Marie-Tooth disease, demyelinating, IIA 1I (0.729); POLR-related leukodystrophy (0.707); POLR3B-related disorder (0.575)
- **Europe PMC papers**: 587
- **Why important**: POLR3B is the partner of POLR1A in the only high-confidence STRING interaction and is included with POLR1A in hu.MAP complexes (hu.MAP huMAP3_09057.1) through (hu.MAP huMAP3_11092.1). It contributes directly to (GO:BP transcription by RNA polymerase III; q_global = 0.0158) and encodes a major RNA polymerase III subunit involved in synthesis of transfer and small ribosomal RNAs. Its disease associations with hypomyelinating leukodystrophy and related POLR3 disorders provide biological relevance beyond enrichment statistics.
- **Conclusion**: Established evidence supports POLR3B as a core RNA polymerase III component and as a known partner of POLR1A. Its presence supports a genuine transcriptional submodule, but it does not establish a direct mechanistic connection to VGF, SYT1, or INA.

#### INA

- **Related proteins** (co-abundance neighbors): SYT1 (0.90); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: internexin neuronal intermediate filament protein alpha. Neurofilaments are type IV intermediate filament heteropolymers composed of light, medium, and heavy chains. Neurofilaments comprise the axoskeleton and they functionally maintain the neuronal caliber. They may also play a role in intracellular transport to axons and dendrites. This gene is a member of the intermediate filament family and is involved in the morphogenesis of neurons. [provided by R…
- **Diseases (Open Targets)**: neurodegenerative disease (0.373); Abnormal brain morphology (0.266); kidney disorder (0.254); pathological myopia (0.111); myopia (0.111)
- **Europe PMC papers**: 35120
- **Why important**: INA is a neuron-enriched structural gene connected to SYT1 in the module. HPA places it in brain, pituitary, and retina group-enriched categories and in excitatory-neuron, inhibitory-neuron, cone-photoreceptor, and related specialized-cell categories. Its established role in neuronal intermediate filaments, axonal caliber, intracellular transport, and neuronal morphogenesis gives an independent structural basis for the neuronal interpretation. It also has an extensive literature and disease associations involving neurodegenerative and brain-morphology phenotypes.
- **Conclusion**: Established evidence supports INA as a neuronal cytoskeletal marker and as a biologically coherent partner of the SYT1 branch. Its module membership is more consistent with shared neuronal or specialized-cell composition than with evidence that INA participates in the polymerase complexes.

## Module 4

**Tissue pair**: autonomic_nervous_system and breast  
**Genes (10)**: PRMT3, DCX, IDE, EIF4G3, FAM114A1, P4HA1, PFKP, RASA1, RPP30, SRI

### Function

No GO or KEGG term passed global correction, so there is no statistically supported pathway-level annotation for this module. The co-abundance structure is a hub-and-spoke pattern centered on DCX, with the other genes connected only to DCX and not to one another. The genes span neuronal microtubule organization and migration through DCX, calcium handling through SRI, glycolysis through PFKP, peptide degradation through IDE, translation and ribosome-associated regulation through EIF4G3 and PRMT3, RNA processing through RPP30, collagen maturation through P4HA1, and RAS signaling and vascular biology through RASA1. This functional diversity argues against assigning the module a single established biochemical pathway. The most defensible interpretation is a coordinated abundance pattern involving a neuronal or specialized differentiated-cell signal together with general cellular metabolism, protein synthesis, RNA processing, and signaling. The pattern may represent shared cellular composition or a state-associated program rather than a physically integrated molecular complex.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only a minority are annotated as secreted, and most are intracellular. It is also not strongly blood-cell enriched. HPA reports low immune-cell specificity for most genes, with one gene not detected in immune cells and one group-enriched immune annotation. Thus, a generic blood-cell contamination explanation is not strongly supported. Most genes are cell-type enhanced, while tissue specificity is mixed. The annotations include brain and retina enrichment for DCX, intestine enrichment for SRI, placenta enrichment for RASA1, and specialized reproductive, epithelial, glial, neuronal, and muscle-associated cell types across the module. Breast protein detection is present for most genes, whereas autonomic-nervous-system protein data are unavailable in the supplied HPA comparison. The shared module may therefore reflect a mixture of differentiated-cell composition and broadly expressed intracellular proteins rather than a breast-specific secreted or immune program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is present among the module genes, and no hu.MAP complex contains multiple module members. Therefore, the co-abundance relationships are not corroborated as known direct protein interactions or as a shared annotated complex. The individual genes do have established functions, including DCX-mediated microtubule regulation, SRI-mediated calcium handling, PFKP-mediated glycolysis, IDE-mediated peptide degradation, RPP30-mediated RNA processing, and RASA1-mediated RAS regulation, but the supplied interaction resources do not connect these functions into one known protein machine. The network should consequently be interpreted as an abundance association rather than a demonstrated physical interaction network.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The specific cross-tissue co-abundance pattern may be a new observation because it is not represented by a known STRING interaction set or hu.MAP complex. However, the absence of external database support does not establish biological novelty. The sparse hub-centered topology, lack of globally significant GO or KEGG enrichment, mixed cellular functions, and strong cell-type specificity make it equally plausible that the pattern reflects tissue composition, correlated expression of differentiated cell populations, or a dataset-specific abundance effect. A claim of a newly discovered molecular module would require replication in independent cohorts, preservation of the gene relationships, and preferably orthogonal evidence such as cell-resolved measurements or perturbation experiments.

**Hypothesis.** Hypothesis: the module reflects a differentiated-cell abundance state organized statistically around DCX, in which neuronal or neuron-like cytoskeletal biology is correlated with cellular energetics, calcium regulation, translation, RNA processing, extracellular-matrix maturation, peptide turnover, and vascular or developmental signaling. DCX may mark the dominant cell-associated signal, while the other genes could report accompanying metabolic and regulatory states rather than form a single physical complex. This hypothesis predicts that the module will be strongest in samples containing the relevant specialized cell populations and may weaken after cell-composition adjustment. It should be tested by cell-type deconvolution, single-cell or spatial profiling, replication across independent autonomic-nervous-system and breast datasets, and experimental assessment of whether perturbing DCX-associated states changes the other genes.

### Important genes

#### DCX

- **Related proteins** (co-abundance neighbors): FAM114A1 (0.92), SRI (0.89), RPP30 (0.85), P4HA1 (0.85), PFKP (0.84), IDE (0.84), EIF4G3 (0.83), PRMT3 (0.82), RASA1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: doublecortin. This gene encodes a member of the doublecortin family. The protein encoded by this gene is a cytoplasmic protein and contains two doublecortin domains, which bind microtubules. In the developing cortex, cortical neurons must migrate over long distances to reach the site of their final differentiation. The encoded protein appears to direct neuronal migration by regulating the organization and stabi…
- **Diseases (Open Targets)**: lissencephaly type 1 due to doublecortin gene mutation (0.860); subcortical band heterotopia (0.673); Non-syndromic cerebral malformation due to abnormal neuronal migration (0.558); Abnormal cortical gyration (0.523); hereditary disease (0.520)
- **Europe PMC papers**: 10181
- **Why important**: DCX is the sole network hub, connected to every other module member with strong weighted associations. Its established function is cytoplasmic microtubule binding and regulation of neuronal migration, and HPA supports brain and retina tissue enrichment plus neuronal cell-type enhancement. It also has extensive literature and strong disease associations with abnormal neuronal migration and cortical malformation. This combination makes DCX the principal anchor for interpreting the module, although it has no STRING or hu.MAP support within this module.
- **Conclusion**: Established evidence supports DCX as the network-defined anchor and as a marker of neuronal or specialized differentiated-cell biology. It is not established that DCX mechanistically controls the other module genes. The interpretation of DCX as a driver of the module remains a hypothesis.

#### SRI

- **Related proteins** (co-abundance neighbors): DCX (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sorcin. This gene encodes a calcium-binding protein with multiple E-F hand domains that relocates from the cytoplasm to the sarcoplasmic reticulum in response to elevated calcium levels. In addition to regulating intracellular calcium homeostasis it also modulates excitation-contraction coupling in the heart. Alternative splicing results in multiple transcript variants encoding distinct proteins. Multiple…
- **Diseases (Open Targets)**: hereditary disease (0.340); benign neoplasm of pituitary gland (0.261); neoplasm (0.101); hepatocellular carcinoma (0.099); Abnormality of the skeletal system (0.087)
- **Europe PMC papers**: 25217
- **Why important**: SRI is directly connected to DCX and encodes a calcium-binding protein involved in intracellular calcium homeostasis and excitation-contraction coupling. Its intestine-enriched tissue annotation and enhancement in enteric and other specialized cell types broaden the possible cellular context beyond neurons. SRI also has extensive literature, making its calcium-regulatory function well established.
- **Conclusion**: Established evidence supports SRI as a calcium-handling component whose abundance could report cellular excitation or differentiation state. Its connection to DCX is an abundance association only; a direct DCX–SRI mechanism is not established by STRING, hu.MAP, or the supplied annotations.

#### PFKP

- **Related proteins** (co-abundance neighbors): DCX (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphofructokinase, platelet. This gene encodes a member of the phosphofructokinase A protein family. The encoded enzyme is the platelet-specific isoform of phosphofructokinase and plays a key role in glycolysis regulation. This gene may play a role in metabolic reprogramming in some cancers, including clear cell renal cell carcinomas, and cancer of the bladder, breast, and lung. Alternative splicing results in multiple transc…
- **Diseases (Open Targets)**: alcohol drinking (0.443); response to water (0.426); neurodegenerative disease (0.414); Alzheimer disease (0.372); spinocerebellar ataxia, autosomal recessive 30 (0.353)
- **Europe PMC papers**: 3384
- **Why important**: PFKP is directly connected to the DCX hub and encodes the platelet isoform of phosphofructokinase, a regulator of glycolysis. It is tissue enhanced in retina and cell-type enhanced in several specialized reproductive and retinal-associated populations. Its documented involvement in metabolic reprogramming, including cancer contexts, gives it value as a metabolic readout within an otherwise functionally mixed module.
- **Conclusion**: Established evidence supports PFKP as an indicator of glycolytic capacity or metabolic state. It is plausible that PFKP reflects energetic requirements of the cell population associated with the module, but the data do not establish that glycolysis is the defining function of the module.

#### IDE

- **Related proteins** (co-abundance neighbors): DCX (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin degrading enzyme. This gene encodes a zinc metallopeptidase that degrades intracellular insulin, and thereby terminates insulins activity, as well as participating in intercellular peptide signalling by degrading diverse peptides such as glucagon, amylin, bradykinin, and kallidin. The preferential affinity of this enzyme for insulin results in insulin-mediated inhibition of the degradation of other peptides such as…
- **Diseases (Open Targets)**: diabetes mellitus (0.307); type 2 diabetes mellitus (0.287); diabetic retinopathy (0.146); diabetic eye disease (0.144); brain cancer (0.142)
- **Europe PMC papers**: 19876
- **Why important**: IDE is directly connected to DCX and encodes a zinc metallopeptidase that degrades insulin and several other signaling peptides, including amyloid beta-related substrates in the supplied description. It has broad tissue expression, breast protein detection, substantial literature, and disease associations involving diabetes and neurodegenerative or retinal disease. It therefore links peptide signaling and proteostasis to the module's neuronal and metabolic interpretations.
- **Conclusion**: Established evidence supports IDE as a peptide-processing and proteostasis-related enzyme. Its presence may indicate altered peptide turnover or metabolic signaling, but no evidence here demonstrates that IDE participates in a shared complex with DCX or the other genes.

#### RASA1

- **Related proteins** (co-abundance neighbors): DCX (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Basal body; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAS p21 protein activator 1. The protein encoded by this gene is located in the cytoplasm and is part of the GAP1 family of GTPase-activating proteins. The gene product stimulates the GTPase activity of normal RAS p21 but not its oncogenic counterpart. Acting as a suppressor of RAS function, the protein enhances the weak intrinsic GTPase activity of RAS proteins resulting in the inactive GDP-bound form of RAS, thereby allowin…
- **Diseases (Open Targets)**: capillary malformation-arteriovenous malformation 1 (0.831); capillary malformation-arteriovenous malformation syndrome (0.711); angioosteohypertrophic syndrome (0.629); Parkes Weber syndrome (0.557); Abnormality of the cardiovascular system (0.544)
- **Europe PMC papers**: 2891
- **Why important**: RASA1 is directly connected to DCX and encodes a RAS GTPase-activating protein that suppresses RAS signaling. Its placenta tissue enrichment, enhancement in vascular and trophoblast-related cell types, and strong associations with capillary malformation and arteriovenous malformation make it informative for developmental and vascular-cell interpretations. It adds a signaling and cell-adhesion dimension that is not captured by the neuronal and metabolic genes alone.
- **Conclusion**: Established evidence supports RASA1 as a regulator of RAS signaling, vascular development, and cell-adhesion-related biology. Its module association may reflect shared abundance of specialized vascular or developmental cells. A direct mechanistic link between RASA1 and DCX is not established.

## Module 5

**Tissue pair**: autonomic_nervous_system and breast  
**Genes (6)**: ARHGEF40, CISD1, LYN, MMUT, NOA1, NUP88

### Function

No GO/KEGG term passed global correction, and there were no supplementary STRING enrichment terms. The network is therefore not assigned a statistically established pathway function. Its gene content suggests a mixed cellular program spanning Rho-family signaling through ARHGEF40, mitochondrial and metabolic biology through CISD1, NOA1, and MMUT, immune signaling through LYN, and nucleocytoplasmic transport through NUP88. These annotations support a possible connection among signaling, mitochondrial state, metabolism, and cellular stress, but the functional interpretation remains provisional rather than enrichment-established.

**Cell composition.** The module is not composed of plasma or secreted proteins: all module genes have no secretome annotation. It is also not uniformly blood-cell enriched. HPA indicates mostly low or enhanced tissue specificity, with tissue associations distributed across parathyroid gland, bone marrow, lymphoid tissue, and liver. Cell-type associations include neutrophils, adipocytes, adrenal cortex cells, enterocytes, and germ-cell populations. LYN has a clear neutrophil and immune-cell association, while ARHGEF40 also has neutrophil-associated annotation, but the other genes are not specifically immune-enriched. The shared autonomic-nervous-system and breast signal could therefore reflect a mixture of broadly present cellular programs, variable cell composition, or sample-specific covariation rather than a breast- or autonomic-specific biological pathway. Breast protein detection supports expression of several members in breast, but the absence of matching autonomic-nervous-system HPA tissue data limits tissue-level interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The co-abundance graph is star-like, with ARHGEF40 connected to every other member and the remaining genes not connected to one another. None of the possible gene pairs meets the supplied high-confidence STRING interaction criterion, and no hu.MAP complex contains multiple module members. Thus, the relationships already known in curated interaction or complex resources are effectively absent for this exact gene set. The module may represent coordinated abundance without direct physical interaction, indirect regulation, shared cellular composition, or technical and physiological covariation. The network topology identifies ARHGEF40 as the co-abundance hub, but it does not establish that ARHGEF40 physically regulates every neighbor.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact cross-tissue co-abundance module may be a new computational observation because it lacks matching high-confidence STRING interactions, lacks a shared hu.MAP complex, and has no globally significant GO/KEGG or STRING enrichment. However, those absences do not prove biological novelty: the individual genes and their functions are already established to varying degrees, and a co-abundance relationship can arise from indirect biology or shared sample composition. The defensible conclusion is that the module-level combination and its cross-tissue occurrence are potentially novel and require replication, independent cohorts, cell-composition adjustment, and experimental testing.

**Hypothesis.** Hypothesis: variation in a central ARHGEF40-associated signaling state may covary with mitochondrial redox and iron-sulfur biology through CISD1, mitochondrial translation and respiratory-complex support through NOA1, propionyl-CoA and succinyl-CoA metabolism through MMUT, immune signaling through LYN, and nuclear transport through NUP88. A shared stress, differentiation, or cellular-composition axis could consequently produce the observed abundance pattern in autonomic nervous system and breast samples without requiring direct protein-protein interactions. This hypothesis predicts that the module should weaken after adjustment for neutrophil and other cell-type abundance, while any residual signal should track Rho-family signaling, mitochondrial state, metabolic activity, or inflammatory signaling.

### Important genes

#### ARHGEF40

- **Related proteins** (co-abundance neighbors): NOA1 (0.90), CISD1 (0.84), MMUT (0.83), LYN (0.83), NUP88 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho guanine nucleotide exchange factor 40. This gene encodes a protein similar to guanosine nucleotide exchange factors for Rho GTPases. The encoded protein contains in its C-terminus a GEF domain involved in exchange activity and a pleckstrin homology domain. Alternatively spliced transcripts that encode different proteins have been described. [provided by RefSeq, Mar 2014].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.504); neuroblastoma (0.353); neurodegenerative disease (0.334); atrial fibrillation (0.311); aortic valve disorder (0.301)
- **Europe PMC papers**: 171
- **Why important**: ARHGEF40 is the sole network hub, connecting to every other module member with strong co-abundance links. Its annotated Rho guanine nucleotide exchange-factor function and links to axon guidance and small-GTPase signaling provide the clearest signaling framework for the module. It also has annotations involving adipocytes, adrenal cortex cells, and neutrophils, plus disease associations spanning skeletal, neural, cardiovascular, and neurodegenerative phenotypes. Its literature base is smaller than that of LYN but sufficient to support a biologically meaningful role.
- **Conclusion**: Established evidence supports ARHGEF40 as the module's co-abundance hub and as a Rho-family signaling candidate. It is not established that it mechanistically controls the other genes; that central regulatory interpretation remains a hypothesis.

#### LYN

- **Related proteins** (co-abundance neighbors): ARHGEF40 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enhanced; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LYN proto-oncogene, Src family tyrosine kinase. This gene encodes a tyrosine protein kinase, which maybe involved in the regulation of mast cell degranulation, and erythroid differentiation. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2011].
- **Diseases (Open Targets)**: autoinflammatory disease, systemic, with vasculitis (0.712); chronic myeloid leukemia (0.601); cancer (0.569); acute lymphoblastic leukemia (0.562); neurodegenerative disease (0.528)
- **Europe PMC papers**: 15695
- **Why important**: LYN is directly connected to ARHGEF40 and is the clearest immune-associated member. HPA links it to bone marrow, lymphoid tissue, neutrophils, and enhanced immune-cell specificity. Its annotated functions include cytokine regulation, C-type lectin receptor signaling, phosphorylation control, B-cell homeostasis, and mast-cell-related biology. It has extensive literature and disease associations involving inflammatory disease, leukemia, cancer, and neurodegenerative disease.
- **Conclusion**: Established evidence supports LYN as an immune and tyrosine-kinase signaling gene and makes it a plausible contributor to cell-composition or inflammatory variation. Its presence does not prove that the module is immune-specific, because the remaining genes have diverse tissue and cell associations.

#### CISD1

- **Related proteins** (co-abundance neighbors): ARHGEF40 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CDGSH iron sulfur domain 1. This gene encodes a protein with a CDGSH iron-sulfur domain and has been shown to bind a redox-active [2Fe-2S] cluster. The encoded protein has been localized to the outer membrane of mitochondria and is thought to play a role in regulation of oxidation. Genes encoding similar proteins are located on chromosomes 4 and 17, and a pseudogene of this gene is located on chromosome 2. [provided by RefSe…
- **Diseases (Open Targets)**: neurodegenerative disease (0.539); Abnormality of the integument (0.348); secondary malignant neoplasm (0.306); Parkinson disease (0.296); biliary tract disorder (0.283)
- **Europe PMC papers**: 1042
- **Why important**: CISD1 is directly connected to ARHGEF40 and encodes a mitochondrial CDGSH iron-sulfur-domain protein associated with redox regulation, intracellular iron homeostasis, autophagy, and protein maturation. HPA reports tissue enhancement in parathyroid gland and cell associations across digestive, gastric, and germ-cell populations. It has a substantial literature base and disease associations including neurodegenerative disease, Parkinson disease, and malignancy-related phenotypes.
- **Conclusion**: Established evidence supports CISD1 as a mitochondrial redox and iron-sulfur biology gene. Its inclusion supports a mitochondrial or oxidative-state interpretation, but a direct functional connection to ARHGEF40 or LYN is not established by the supplied interaction resources.

#### NOA1

- **Related proteins** (co-abundance neighbors): ARHGEF40 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nitric oxide associated 1. The protein encoded by this gene is a nuclear-encoded GTPase that functions in the mitochondrion. Upon translation, this protein is imported into the nucleus and then into the nucleolus before being exported to the mitochondrion. The encoded protein is required for oxygen-dependent regulation of mitochondrial respiratory complexes and for mitochondrial protein synthesis. [provided by RefSeq, Dec 2…
- **Diseases (Open Targets)**: neurodegenerative disease (0.263); risk-taking behaviour (0.149); ankylosing spondylitis (0.129); coronary artery disorder (0.105); myocardial infarction (0.093)
- **Europe PMC papers**: 448
- **Why important**: NOA1 is a peripheral module member connected to ARHGEF40 and is localized to mitochondria. Its established annotations involve mitochondrial organization, mitochondrial ribosome assembly, RNA folding, mitochondrial protein synthesis, and oxygen-dependent regulation of respiratory complexes. HPA shows low tissue and cell-type specificity, and it has a substantial literature base with disease associations involving neurodegeneration and cardiovascular phenotypes.
- **Conclusion**: Established evidence supports NOA1 as a mitochondrial translation and respiratory-function candidate with relatively broad expression. Its module membership may indicate covariation with mitochondrial state, but the module does not establish a direct NOA1-ARHGEF40 mechanism.

#### MMUT

- **Related proteins** (co-abundance neighbors): ARHGEF40 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methylmalonyl-CoA mutase. This gene encodes the mitochondrial enzyme methylmalonyl Coenzyme A mutase. In humans, the product of this gene is a vitamin B12-dependent enzyme which catalyzes the isomerization of methylmalonyl-CoA to succinyl-CoA, while in other species this enzyme may have different functions. Mutations in this gene may lead to various types of methylmalonic aciduria. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: methylmalonic aciduria due to methylmalonyl-CoA mutase deficiency (0.829); vitamin B12-unresponsive methylmalonic acidemia type mut0 (0.627); methylmalonic acidemia (0.578); vitamin B12-unresponsive methylmalonic acidemia type mut- (0.549); Methylmalonic aciduria (0.519)
- **Europe PMC papers**: 499
- **Why important**: MMUT is directly connected to ARHGEF40 and encodes the vitamin B12-dependent enzyme that converts methylmalonyl-CoA to succinyl-CoA. Its annotations implicate homocysteine metabolism, propionyl-CoA catabolism, and succinyl-CoA biosynthesis. HPA shows liver and hepatocyte enhancement, and disease evidence strongly links it to methylmalonic aciduria and methylmalonic acidemia. Its literature base is established but less extensive than that of LYN.
- **Conclusion**: Established evidence supports MMUT as a metabolic and mitochondrial-function marker. Its presence broadens the module beyond immune signaling and suggests that metabolic state or tissue composition may contribute. A coordinated metabolic role within this module remains a hypothesis.

## Module 6

**Tissue pair**: autonomic_nervous_system and breast  
**Genes (14)**: ARMC9, CACNA2D1, CHN1, CHURC1, DNMT3A, HDGFL3, NME7, NEFM, OGFOD3, SMARCD1, PLAT, UAP1L1, VANGL2, ZC3H6

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent; therefore the module does not support a statistically established single pathway label. Its gene content nevertheless points to a mixed neurodevelopmental, ciliary, cytoskeletal, calcium-signaling, chromatin-regulatory, and extracellular-remodeling program. CHN1 is the principal network hub and links neuronal signaling and axon guidance with CACNA2D1, ARMC9, DNMT3A, NEFM, and OGFOD3. The presence of NEFM, CHN1, CACNA2D1, ARMC9, and VANGL2 is compatible with neuronal structure, excitability, cilia, and developmental patterning, while DNMT3A, SMARCD1, CHURC1, ZC3H6, and HDGFL3 point to transcriptional or chromatin regulation. PLAT adds a distinct proteolytic and tissue-remodeling component. These annotations support a biologically heterogeneous module rather than a demonstrated unified pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only PLAT is explicitly secreted to blood, while CACNA2D1 is described as intracellular and membrane-associated. It is also not strongly blood-cell enriched overall. Most genes have low tissue specificity, but many show cell-type-enhanced patterns, especially in neuronal, retinal, epithelial, endocrine, or ciliated populations. CHN1, NEFM, ARMC9, CACNA2D1, and VANGL2 provide a neural or developmental signal; PLAT has breast hormone-responsive and stromal associations; and several genes are detected in breast by immunohistochemistry. The shared signal could therefore reflect mixtures of neural, epithelial, stromal, ciliated, or other cell types in the samples, rather than a breast-specific or autonomic-nervous-system-specific process. The HPA evidence does not support interpreting the module primarily as a blood-contamination module, although isolated immune-cell-enhanced annotations occur.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interactions were detected among the module genes, no STRING functional enrichment was reported, and no hu.MAP complex contained multiple module members. Thus the co-abundance relationships are not corroborated by the supplied physical-interaction or curated-complex resources. This does not refute coordinated regulation: co-abundance can arise from shared cell composition, transcriptional state, developmental programs, or indirect regulation. The strongest internal links, especially the CHN1-centered connections and the small subgraphs involving ARMC9–CHURC1–UAP1L1–HDGFL3 and PLAT–OGFOD3–VANGL2, should therefore be treated as expression-network associations rather than established protein complexes.

**STRING interactions (score >= 0.7)**: 0 of 91 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be novel as a cross-tissue co-abundance pattern, because its exact membership and internal organization are not represented by the supplied STRING or hu.MAP evidence. However, absence from those resources does not establish biological novelty. Most individual genes have established functions and disease associations, and several pairwise biological themes are already known, including neuronal signaling, neurofilament structure, calcium-channel biology, cilium assembly, chromatin regulation, planar cell polarity, and plasminogen activation. The defensible conclusion is that the integrated module-level association is potentially new, whereas the underlying gene functions and many biological themes are not.

**Hypothesis.** Hypothesis: the shared module reflects coordinated variation in a mixed neural-developmental and tissue-architecture state that couples neuronal or excitable-cell features with ciliary and planar-polarity programs, chromatin regulation, and local extracellular remodeling. CHN1 may organize the neuronal signaling component; CACNA2D1 may represent membrane calcium handling; ARMC9 and NME7 may represent ciliary or centrosomal biology; VANGL2 may connect polarity and migration; and PLAT may mark remodeling or proteolytic activity. This could arise from shared cellular composition or a common regulatory state across the two tissues, but it requires validation with cell-resolved data, replication cohorts, protein measurements, and perturbation experiments. It is not established by the enrichment results.

### Important genes

#### CHN1

- **Related proteins** (co-abundance neighbors): OGFOD3 (0.88), DNMT3A (0.85), CACNA2D1 (0.84), ARMC9 (0.83), NEFM (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chimerin 1. This gene encodes GTPase-activating protein for ras-related p21-rac and a phorbol ester receptor. It is predominantly expressed in neurons, and plays an important role in neuronal signal-transduction mechanisms. Mutations in this gene are associated with Duane's retraction syndrome 2 (DURS2). Alternatively spliced transcript variants encoding different isoforms have been described for this gene. […
- **Diseases (Open Targets)**: Duane retraction syndrome (0.781); Robinow syndrome (0.333); autosomal dominant Robinow syndrome (0.333); smoking initiation (0.296); Moebius syndrome (0.269)
- **Europe PMC papers**: 647
- **Why important**: CHN1 has the strongest network connectivity in the module and connects five biologically diverse neighbors, including CACNA2D1, DNMT3A, ARMC9, NEFM, and OGFOD3. It is predominantly neuronal, encodes a Rac GTPase-activating protein, and is annotated for neuronal signal transduction, axon guidance, ephrin-receptor signaling, and axonogenesis. It also has a substantial literature and established association with Duane retraction syndrome and Robinow syndrome.
- **Conclusion**: Established evidence supports CHN1 as the main neuronal signaling and network-organization candidate. The hypothesis that it coordinates the other module components is plausible from its network position but is not demonstrated by physical interaction data.

#### PLAT

- **Related proteins** (co-abundance neighbors): OGFOD3 (0.84), VANGL2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plasminogen activator, tissue type. This gene encodes tissue-type plasminogen activator, a secreted serine protease that converts the proenzyme plasminogen to plasmin, a fibrinolytic enzyme. The encoded preproprotein is proteolytically processed by plasmin or trypsin to generate heavy and light chains. These chains associate via disulfide linkages to form the heterodimeric enzyme. This enzyme plays a role in cell migration and tissu…
- **Diseases (Open Targets)**: pulmonary embolism (0.607); myocardial infarction (0.594); hemorrhage (0.586); stroke disorder (0.580); acute myocardial infarction (0.575)
- **Europe PMC papers**: 17953
- **Why important**: PLAT is a secreted serine protease with a direct role in plasminogen activation, proteolysis, coagulation-related biology, cell migration, and tissue remodeling. It links OGFOD3 and VANGL2 in the module and is enhanced in breast hormone-responsive and stromal-related cell types. Its disease literature is extensive, particularly for thrombotic, hemorrhagic, cardiovascular, and cerebrovascular conditions.
- **Conclusion**: Established evidence identifies PLAT as the clearest extracellular remodeling and proteolytic component. Its inclusion may reflect local tissue remodeling or sample composition; a direct mechanistic bridge from PLAT to the neural and ciliary genes remains hypothetical.

#### NEFM

- **Related proteins** (co-abundance neighbors): CHN1 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neurofilament medium chain. Neurofilaments are type IV intermediate filament heteropolymers composed of light, medium, and heavy chains. Neurofilaments comprise the axoskeleton and functionally maintain neuronal caliber. They may also play a role in intracellular transport to axons and dendrites. This gene encodes the medium neurofilament protein. This protein is commonly used as a biomarker of neuronal damage. Alternative s…
- **Diseases (Open Targets)**: neurodegenerative disease (0.379); placental abruption (0.286); facial pain (0.251); neutropenia (0.249); ovarian dysfunction (0.242)
- **Europe PMC papers**: 1730
- **Why important**: NEFM is a neuronal intermediate-filament protein that contributes to neurofilament bundle assembly and axonal caliber and transport. It is group-enriched in brain and retina, is enhanced in several neuronal and endocrine cell types, and is commonly used as a marker of neuronal damage. Its literature and disease-related annotation are substantial. In the network it connects directly to the central CHN1 node.
- **Conclusion**: Established evidence supports NEFM as a neural structural marker and makes it useful for testing whether the module reflects neuronal material or neuronal-like cell states. It does not by itself prove active neuronal signaling in breast or autonomic-nervous-system samples.

#### CACNA2D1

- **Related proteins** (co-abundance neighbors): ZC3H6 (0.85), CHN1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium voltage-gated channel auxiliary subunit alpha2delta 1. The preproprotein encoded by this gene is cleaved into multiple chains that comprise the alpha-2 and delta subunits of the voltage-dependent calcium channel complex. Calcium channels mediate the influx of calcium ions into the cell upon membrane polarization. Mutations in this gene can cause cardiac deficiencies, including Brugada syndrome and short QT syndrome. Alternate splicing results in multi…
- **Diseases (Open Targets)**: Seizure (0.694); epilepsy (0.609); neuropathic pain (0.603); fibromyalgia (0.603); restless legs syndrome (0.588)
- **Europe PMC papers**: 2155
- **Why important**: CACNA2D1 encodes the alpha-two-delta component of voltage-dependent calcium channels and is annotated for calcium transport, muscle contraction, insulin secretion responses, and cardiac membrane repolarization. It connects CHN1 and ZC3H6, is enhanced in skeletal muscle and tongue, and is associated with seizure, epilepsy, neuropathic pain, and related disorders. Its literature is well developed.
- **Conclusion**: Established evidence supports CACNA2D1 as a membrane-excitability and calcium-handling candidate. Its connection to CHN1 supports a possible excitable-cell interpretation, but the module does not establish a specific calcium-signaling mechanism.

#### ARMC9

- **Related proteins** (co-abundance neighbors): SMARCD1 (0.84), CHURC1 (0.84), CHN1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Flagellar centriole; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: armadillo repeat containing 9. Predicted to be involved in cilium assembly and positive regulation of smoothened signaling pathway. Located in centriole and ciliary basal body. Implicated in Joubert syndrome 30. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Joubert syndrome (0.773); Joubert syndrome 30 (0.761); Intellectual disability (0.371); Dandy-Walker syndrome (0.323); Vertigo (0.309)
- **Europe PMC papers**: 258
- **Why important**: ARMC9 connects CHN1 with SMARCD1 and CHURC1 and is tissue-enhanced in retina, with enrichment in photoreceptor and other ciliated or epithelial cell types. It is predicted to participate in cilium assembly and positive regulation of Smoothened signaling and is implicated in Joubert syndrome. Its network position places it at the interface of the neuronal and ciliary portions of the module.
- **Conclusion**: Established evidence supports ARMC9 as a ciliary and developmental candidate. The idea that it links ciliary biology to the module's neural signal is a reasonable hypothesis, but no curated complex or physical interaction evidence supports that link here.

#### DNMT3A

- **Related proteins** (co-abundance neighbors): NME7 (0.91), CHN1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA methyltransferase 3 alpha. CpG methylation is an epigenetic modification that is important for embryonic development, imprinting, and X-chromosome inactivation. Studies in mice have demonstrated that DNA methylation is required for mammalian development. This gene encodes a DNA methyltransferase that is thought to function in de novo methylation, rather than maintenance methylation. The protein localizes to the cytoplasm an…
- **Diseases (Open Targets)**: acute myeloid leukemia (0.858); Tatton-Brown-Rahman overgrowth syndrome (0.844); Heyn-Sproul-Jackson syndrome (0.763); myelodysplastic syndrome (0.741); myeloid leukemia (0.682)
- **Europe PMC papers**: 31456
- **Why important**: DNMT3A is a de novo DNA methyltransferase with a very extensive literature and major disease associations, including myeloid malignancy and developmental overgrowth or intellectual-disability syndromes. It connects NME7 and CHN1 and provides a plausible regulatory layer for a module whose other genes span multiple cell types and functions. Its annotations include developmental regulation, transcriptional repression, heterochromatin formation, and responses to cellular stress.
- **Conclusion**: Established evidence supports DNMT3A as an epigenetic regulator that could influence cell-state composition or transcriptional programs. Its role as a driver of this particular co-abundance module is hypothetical and cannot be inferred from the pairwise expression edge alone.

## Module 7

**Tissue pair**: autonomic_nervous_system and breast  
**Genes (8)**: ARFGEF1, CBLB, CPNE2, EXOSC9, GNAO1, IRS2, MAN1A1, MTFP1

### Function

No GO or KEGG term passed global correction. The module therefore does not support a statistically established pathway assignment from enrichment. Its gene annotations suggest a composite cellular program involving receptor and intracellular signal regulation, vesicle and Golgi trafficking, glycoprotein processing, mitochondrial dynamics, calcium-responsive membrane organization, and RNA processing. The network is centered on CBLB, with a second signaling-oriented connection through GNAO1; the remaining genes form sparse links to these central nodes. This pattern is more consistent with coordinated cellular state or signaling context than with a single established molecular complex.

**Cell composition.** The module is not composed of secreted proteins, and most genes have low tissue specificity. All genes are enhanced in at least one cell type, with recurring annotations for neutrophil progenitors and additional annotations spanning neural, epithelial, reproductive, stromal, and hematopoietic populations. IRS2 is immune-cell enhanced and associated with neutrophils, whereas most other genes have low immune-cell specificity or are not detected in immune cells. Thus, the module is not clearly a blood-cell module, although variable immune or progenitor-cell representation could contribute to its shared signal. Breast protein detection is reported for most genes, while there is no matching autonomic-nervous-system HPA tissue measurement; this limits tissue-level interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationships were reported among the module genes, and no supplementary STRING enrichment was reported. No hu.MAP complex contained multiple module members. Consequently, the co-abundance links are not corroborated here as established physical interactions or as membership in a known multiprotein complex. The network may instead reflect coordinated regulation, shared cell-state expression, indirect signaling relationships, or technical and cellular-composition effects.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared co-abundance pattern may be a novel observation because it is not represented by high-confidence STRING interactions or a hu.MAP complex. However, absence from those resources does not establish biological novelty: these databases favor experimentally characterized physical relationships, whereas co-abundance can arise from indirect regulation or shared cellular context. The absence of globally significant GO or KEGG enrichment and the sparse, heterogeneous annotations make this best described as a potentially novel module-level association requiring independent replication and targeted validation, rather than a newly established pathway.

**Hypothesis.** Hypothesis: the module reflects a context-dependent signaling and trafficking state shared by selected cells in autonomic-nervous-system and breast samples. CBLB may coordinate receptor-proximal signaling and ubiquitin-dependent attenuation, IRS2 may connect extracellular receptor cues to metabolic and proliferative signaling, and GNAO1 may represent a neural or membrane-signaling component. ARFGEF1 and MAN1A1 could indicate Golgi and vesicle-processing requirements, while MTFP1 and CPNE2 could couple mitochondrial dynamics and calcium-sensitive membrane responses. This model predicts that the module will track particular cell states or perturbations rather than a stable physical complex.

### Important genes

#### CBLB

- **Related proteins** (co-abundance neighbors): MAN1A1 (0.95), MTFP1 (0.87), EXOSC9 (0.85), IRS2 (0.82), ARFGEF1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Cbl proto-oncogene B. This gene encodes an E3 ubiquitin-protein ligase which promotes proteosome-mediated protein degradation by transferring ubiquitin from an E2 ubiquitin-conjugating enzyme to a substrate. The encoded protein is involved in the regulation of immune response by limiting T-cell receptor, B-cell receptor, and high affinity immunoglobulin epsilon receptor activation. Studies in mouse suggest that this ge…
- **Diseases (Open Targets)**: hypothyroidism (0.547); urticaria (0.488); myxedema (0.463); Hashimoto thyroiditis (0.429); thyroid gland disorder (0.420)
- **Europe PMC papers**: 2144
- **Why important**: CBLB is the central network node, linking the signaling, trafficking, mitochondrial, RNA-processing, and adaptor-related branches. Its established function as an E3 ubiquitin-protein ligase that limits receptor signaling, including T-cell and B-cell receptor activation, gives the module a plausible regulatory anchor. It is also extensively studied and has disease associations involving thyroid disorders.
- **Conclusion**: Established evidence supports CBLB as a signaling regulator and as the strongest network-organizing gene in this module. It is reasonable to hypothesize that CBLB helps coordinate the shared co-abundance state, but the absence of STRING and hu.MAP support means that direct physical coupling to the neighboring genes is not established.

#### GNAO1

- **Related proteins** (co-abundance neighbors): MTFP1 (0.85), CPNE2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein subunit alpha o1. The protein encoded by this gene represents the alpha subunit of the Go heterotrimeric G-protein signal-transducing complex. Defects in this gene are a cause of early-onset epileptic encephalopathy. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2015].
- **Diseases (Open Targets)**: neurodevelopmental disorder with involuntary movements (0.809); developmental and epileptic encephalopathy, 17 (0.801); genetic developmental and epileptic encephalopathy (0.692); Epileptic encephalopathy (0.657); infantile epileptic encephalopathy (0.555)
- **Europe PMC papers**: 1546
- **Why important**: GNAO1 occupies the second central position in the network and connects MTFP1 with CPNE2. It encodes the alpha subunit of the Go heterotrimeric G-protein complex and is associated with GPCR signaling and severe developmental epileptic encephalopathy. HPA places it in brain and retina and reports it as not detected in immune cells, providing a biologically distinctive neural component.
- **Conclusion**: Established evidence supports GNAO1 as a neural-enriched GPCR signaling component with important disease relevance. Its co-abundance with MTFP1 and CPNE2 may indicate a neural or membrane-signaling state, but a direct module-specific mechanism remains hypothetical.

#### IRS2

- **Related proteins** (co-abundance neighbors): CBLB (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin receptor substrate 2. This gene encodes the insulin receptor substrate 2, a cytoplasmic signaling molecule that mediates effects of insulin, insulin-like growth factor 1, and other cytokines by acting as a molecular adaptor between diverse receptor tyrosine kinases and downstream effectors. The product of this gene is phosphorylated by the insulin receptor tyrosine kinase upon receptor stimulation, as well as by an int…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.612); neurodegenerative disease (0.563); prostate carcinoma (0.469); cancer (0.381); lysosomal storage disease (0.370)
- **Europe PMC papers**: 8845
- **Why important**: IRS2 is a receptor-signaling adaptor that mediates insulin, insulin-like growth factor, and cytokine effects. It is associated with glucose metabolism, receptor tyrosine kinase signaling, and cell proliferation, and it has substantial literature and disease associations including type two diabetes and neurodegenerative disease. HPA links it particularly to bone marrow and neutrophil-lineage cells, making it informative for assessing cellular composition.
- **Conclusion**: Established evidence supports IRS2 as a broad signal-transduction adaptor and supports a possible immune or progenitor-cell contribution through its HPA profile. Its connection to CBLB is a co-abundance relationship here, not proof of direct biochemical interaction.

#### ARFGEF1

- **Related proteins** (co-abundance neighbors): CBLB (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ARF guanine nucleotide exchange factor 1. ADP-ribosylation factors (ARFs) play an important role in intracellular vesicular trafficking. The protein encoded by this gene is involved in the activation of ARFs by accelerating replacement of bound GDP with GTP. It contains a Sec7 domain, which may be responsible for guanine-nucleotide exchange activity and also brefeldin A inhibition. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: developmental delay, impaired speech, and behavioral abnormalities, with or without seizures (0.774); Intellectual disability (0.646); Joubert syndrome 21 (0.551); Global developmental delay (0.533); hereditary disease (0.528)
- **Europe PMC papers**: 363
- **Why important**: ARFGEF1 is connected to CBLB and encodes a Sec-seven-domain ARF guanine-nucleotide exchange factor involved in Golgi organization, vesicle-mediated transport, exocytosis, and glycoprotein biosynthesis. Its cell-type annotation includes neutrophil progenitors, and it has disease associations involving developmental delay and intellectual disability.
- **Conclusion**: Established evidence supports ARFGEF1 as a Golgi and vesicle-trafficking regulator. Its position next to CBLB makes intracellular trafficking a plausible component of the module, but the co-abundance data do not establish that ARFGEF1 directly modifies CBLB signaling.

#### MTFP1

- **Related proteins** (co-abundance neighbors): CBLB (0.87), GNAO1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial fission process 1. MTP18 is a mitochondrial protein and downstream target of the phosphatidylinositol 3-kinase (see PIK3CA, MIM 171834) signaling pathway that plays a role in cell viability and mitochondrial dynamics (Tondera et al., 2004 [PubMed 15155745]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: neoplasm (0.092); hepatocellular carcinoma (0.076); gastric cancer (0.063); cancer (0.053); pancreatic ductal adenocarcinoma (0.035)
- **Europe PMC papers**: 731
- **Why important**: MTFP1 links to both CBLB and GNAO1 and encodes a mitochondrial protein involved in mitochondrial fission and negative regulation of mitochondrial fusion. Its annotations in epithelial and enteric cell populations, together with disease associations involving several cancers, make it a candidate indicator of metabolic or organelle-state coordination.
- **Conclusion**: Established evidence supports MTFP1 as a mitochondrial-dynamics regulator. Its placement between the CBLB- and GNAO1-associated portions of the network suggests a possible connection between signaling and mitochondrial state, but that connection is a hypothesis rather than an established mechanism.

## Module 8

**Tissue pair**: autonomic_nervous_system and breast  
**Genes (6)**: BIRC5, ETNK1, FBXW11, MTMR2, SIK2, UQCRFS1

### Function

The module is best interpreted as a mixed intracellular regulatory and cellular-state module rather than a narrowly defined pathway. Its central SIK2 relationships connect signaling and phosphorylation control with ubiquitin-mediated regulation through FBXW11, phosphoinositide metabolism and membrane trafficking through MTMR2, mitochondrial respiratory function through UQCRFS1, and proliferative or survival state through BIRC5 [gene-function evidence]. No GO or KEGG term passed global correction, so there is no globally significant pathway-enrichment claim for this module. The co-abundance pattern may therefore reflect coordinated cellular state, growth, metabolic demand, and intracellular trafficking rather than membership in a demonstrated molecular complex.

**Cell composition.** The module is composed entirely of intracellular proteins; none is annotated as secreted. Most genes have low tissue specificity, and most have enhanced specificity for selected cell types rather than a uniform tissue lineage. The HPA pattern includes enrichment in skeletal muscle, tongue, bone marrow, lymphoid tissue, testis, and selected epithelial, germ-cell, neural, and endocrine cell types. Only BIRC5 is immune-cell enhanced, while the other genes have low immune-cell specificity or are not detected in immune cells. Thus, a blood-cell explanation is not strongly supported, although BIRC5 could reflect proliferating or regulatory immune-cell content. Breast protein detection is present for most members, whereas direct autonomic-nervous-system protein evidence is unavailable in the supplied HPA comparison. The module may consequently reflect shared proliferative, metabolic, or cell-state variation across the two tissues rather than a tissue-specific secreted or plasma-protein signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and no hu.MAP complex contains multiple module members [interaction evidence]. This means the co-abundance edges are not corroborated here as established physical interactions or a known multiprotein complex. The biology is nevertheless internally plausible at the level of complementary functions: SIK2 can connect signaling regulation to several partners, MTMR2 regulates phosphoinositide-dependent membrane processes, FBXW11 participates in SCF-dependent ubiquitination, UQCRFS1 represents mitochondrial respiratory activity, and BIRC5 represents mitotic survival and cytokinesis. These are functional links and hypotheses about coordinated state, not evidence of direct binding.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a new tissue-pair co-abundance observation, but it cannot be called a newly discovered molecular pathway or complex. Its novelty lies primarily in the reproducible shared abundance pattern across autonomic nervous system and breast, provided that the pattern is robust to cohort, cell-composition, and technical confounding. The absence of STRING and hu.MAP support does not establish novelty, because co-abundance can arise from co-regulation, shared cell states, or indirect cellular programs. The lack of globally significant GO or KEGG enrichment further argues for a cautious, hypothesis-generating interpretation.

**Hypothesis.** Hypothesis: the module marks a coordinated intracellular state in which SIK2-centered signaling is associated with ubiquitin-dependent protein turnover, phosphoinositide and vesicle regulation, mitochondrial respiratory capacity, and proliferative or anti-apoptotic activity. In breast, this state could reflect variation in proliferating epithelial or other specialized cell populations; in autonomic nervous system samples, it could reflect shared metabolic, glial, neuronal-support, or cell-composition programs. This hypothesis should be tested by cell-resolved expression, independent cohorts, perturbation of SIK2 or FBXW11, and measurement of phosphoinositide trafficking, mitochondrial respiration, and mitotic-survival phenotypes.

### Important genes

#### SIK2

- **Related proteins** (co-abundance neighbors): MTMR2 (0.91), FBXW11 (0.91), UQCRFS1 (0.87), BIRC5 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm, Vesicles; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: salt inducible kinase 2. Enables ATP binding activity; magnesium ion binding activity; and protein serine/threonine kinase activity. Involved in intracellular signal transduction and protein autophosphorylation. Predicted to be located in nucleus. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: asthma (0.436); autoimmune disorder of central nervous system (0.370); neurodegenerative disease (0.296); autoimmune thyroid disease (0.219); pernicious anemia (0.219)
- **Europe PMC papers**: 1261
- **Why important**: SIK2 is the network hub, with the broadest set of module connections and the strongest aggregate edge support. Its annotated kinase and intracellular-signal-transduction functions provide a plausible regulatory center linking MTMR2, FBXW11, UQCRFS1, and BIRC5. It also has substantial literature coverage and disease associations spanning asthma, central nervous system autoimmunity, neurodegeneration, autoimmune thyroid disease, and pernicious anemia [gene annotation; network evidence; disease evidence].
- **Conclusion**: Established evidence supports SIK2 as an intracellular serine/threonine kinase involved in phosphorylation and signal regulation and as the topological center of this module. It is a plausible organizer of the shared co-abundance state, but direct control of the other module genes is not established by the supplied STRING or hu.MAP results.

#### BIRC5

- **Related proteins** (co-abundance neighbors): SIK2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytokinetic bridge; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: baculoviral IAP repeat containing 5. This gene is a member of the inhibitor of apoptosis (IAP) gene family, which encode negative regulatory proteins that prevent apoptotic cell death. IAP family members usually contain multiple baculovirus IAP repeat (BIR) domains, but this gene encodes proteins with only a single BIR domain. The encoded proteins also lack a C-terminus RING finger domain. Gene expression is high during fetal develop…
- **Diseases (Open Targets)**: rheumatoid arthritis (0.140); non-small cell lung carcinoma (0.140); hepatocellular carcinoma (0.138); glioblastoma (0.133); acute myeloid leukemia (0.130)
- **Europe PMC papers**: 12439
- **Why important**: BIRC5 links the SIK2-centered subgraph to mitotic progression, chromosome segregation, spindle organization, cytokinesis, and suppression of apoptotic cell death. It has the largest literature volume in the module, is enriched in bone marrow, lymphoid tissue, and testis, and is enhanced in several developing or proliferative cell types including regulatory T cells. Its presence is especially informative for interpreting the module as a cellular-state signal involving proliferation or survival.
- **Conclusion**: Established evidence supports BIRC5 as a proliferation and survival marker that is often elevated in developmental and tumor contexts. In this module it may report a proliferative-cell component or a shared growth state; it should not be taken as evidence that the entire module is a cancer module.

#### MTMR2

- **Related proteins** (co-abundance neighbors): SIK2 (0.91), FBXW11 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myotubularin related protein 2. This gene is a member of the myotubularin family of phosphoinositide lipid phosphatases. The encoded protein possesses phosphatase activity towards phosphatidylinositol-3-phosphate and phosphatidylinositol-3,5-bisphosphate. Mutations in this gene are a cause of Charcot-Marie-Tooth disease type 4B, an autosomal recessive demyelinating neuropathy. Alternatively spliced transcript variants encoding m…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease type 4B1 (0.760); Charcot-Marie-Tooth disease type 4 (0.552); hereditary disease (0.503); demyelinating hereditary motor and sensory neuropathy (0.370); Abnormality of the skeletal system (0.290)
- **Europe PMC papers**: 903
- **Why important**: MTMR2 is a phosphoinositide lipid phosphatase connected to the two central regulatory nodes, SIK2 and FBXW11. Its functions in phosphoinositide dephosphorylation, endocytosis, receptor internalization, and excitatory-postsynaptic-potential regulation provide a mechanistic bridge between signaling, membrane trafficking, and nervous-system biology. Its established association with Charcot-Marie-Tooth disease type four B makes it particularly relevant to the autonomic-nervous-system side of the tissue pair [gene annotation; disease evidence].
- **Conclusion**: Established evidence supports MTMR2 as a membrane-lipid and trafficking regulator with important peripheral-neuropathy relevance. Its position suggests that membrane trafficking may be part of the shared module state, but the co-abundance data do not establish that MTMR2 drives the module or directly interacts with its neighbors.

#### FBXW11

- **Related proteins** (co-abundance neighbors): SIK2 (0.91), ETNK1 (0.89), MTMR2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: F-box and WD repeat domain containing 11. This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls con…
- **Diseases (Open Targets)**: neurodevelopmental, jaw, eye, and digital syndrome (0.792); neurodegenerative disease (0.502); syndromic intellectual disability (0.462); complex neurodevelopmental disorder (0.370); autism (0.370)
- **Europe PMC papers**: 803
- **Why important**: FBXW11 is a central connector in the regulatory portion of the graph and encodes an F-box protein involved in SCF-dependent, phosphorylation-dependent ubiquitination and proteasomal protein turnover. Its disease associations include neurodevelopmental and neurodegenerative conditions, which are relevant to the autonomic-nervous-system context. Its broad tissue and immune-cell profile makes it less useful as a tissue-specific marker but supports a general regulatory role [gene annotation; HPA; disease evidence].
- **Conclusion**: Established evidence supports FBXW11 as a ubiquitin-system regulator. Within this module it is a plausible post-translational-control component that could coordinate with SIK2 and MTMR2, while any direct functional relationship among them remains hypothetical.

#### UQCRFS1

- **Related proteins** (co-abundance neighbors): SIK2 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase, Rieske iron-sulfur polypeptide 1. Predicted to enable oxidoreductase activity. Involved in mitochondrial respiratory chain complex III assembly and respiratory electron transport chain. Located in mitochondrion. Part of mitochondrial respiratory chain complex III and mitochondrial respiratory chain complex IV. Implicated in mitochondrial complex III deficiency. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: mitochondrial complex III deficiency, nuclear type 10 (0.745); neurodegenerative disease (0.484); cardiomyopathy (0.427); lactic acidosis (0.426); propionic acidemia (0.425)
- **Europe PMC papers**: 1748
- **Why important**: UQCRFS1 provides the clearest mitochondrial and energetic dimension of the module. It is a component of respiratory complex three and is involved in electron transport, complex assembly, and cellular respiration. Its tissue-enhanced HPA pattern includes skeletal muscle and tongue, and it has associations with mitochondrial complex deficiency, neurodegeneration, cardiomyopathy, lactic acidosis, and propionic acidemia. Its direct connection to SIK2 gives the module a possible link between signaling state and energy production.
- **Conclusion**: Established evidence supports UQCRFS1 as a mitochondrial respiratory-chain component. In this module it may indicate energetic demand or mitochondrial state accompanying regulatory and proliferative variation, but the supplied evidence does not show direct regulation by SIK2.

## Module 9

**Tissue pair**: autonomic_nervous_system and breast  
**Genes (12)**: CALU, CHRAC1, CPSF7, FERMT2, GBE1, KATNAL1, MYCBP, PITRM1, SCG2, TIMM50, TPD52L2, USP47

### Function

No GO or KEGG term passed global multiple-testing correction, and there is no significant STRING functional enrichment. Therefore, the module does not support a statistically established pathway-level function from enrichment analysis. Its gene-level annotations suggest a mixed cellular program involving neuroendocrine secretory biology, glycogen and energy metabolism, mitochondrial protein handling, endoplasmic-reticulum calcium-dependent protein folding, cell adhesion, cytoskeletal remodeling, chromatin regulation, RNA processing, and protein deubiquitination. SCG2 is the dominant network hub and is associated with neuroendocrine secretory vesicles, while the remaining genes form a sparse set of connections around this hub or around KATNAL1. The appropriate interpretation is therefore a co-abundance state rather than a demonstrated biochemical complex or single pathway.supplementary STRING

**Cell composition.** The module is not strongly suggestive of a blood-cell module: HPA reports low immune-cell specificity for most genes, no frequently enriched blood-cell category, and some genes are not detected in immune cells. Most genes have low tissue specificity, while many show cell-type-enhanced expression across diverse cell types, including neural, glial, muscle, adipocyte, podocyte, reproductive, and neutrophil-related populations. This heterogeneity may indicate shared cellular or physiological states rather than a uniform tissue-specific program. HPA identifies two secreted genes in the module, and SCG2 is specifically secreted to blood and enriched in adrenal gland, brain, and pituitary gland. Protein detection in breast is present for most tested genes, but the autonomic-nervous-system comparison lacks matching HPA tissue data. Thus, a contribution from secretory or neuroendocrine material, cellular composition, or broadly expressed housekeeping-like biology should be considered, but a blood-contamination explanation is not supported by the available HPA summary.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module gene pair meets the stated high-confidence STRING interaction threshold, STRING reports no functional enrichment, and hu.MAP reports no complex containing multiple module members. The observed co-abundance links are therefore not corroborated as known physical protein interactions or a recognized multiprotein complex. SCG2 connects to several otherwise functionally diverse genes, while KATNAL1 connects to CHRAC1, GBE1, and MYCBP; this pattern is more consistent with coordinated abundance across samples than with a canonical molecular machine. The absence of database support limits mechanistic interpretation but does not invalidate the co-abundance signal.

**STRING interactions (score >= 0.7)**: 0 of 66 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unrecognized tissue-pair co-abundance pattern, because its specific gene combination and sparse network are not supported by the queried STRING or hu.MAP resources. However, this is not sufficient to claim a new biological mechanism. The lack of globally significant GO or KEGG enrichment, the absence of known physical interactions, the mixed subcellular functions, and the broad or heterogeneous HPA expression pattern all make a chance correlation, shared cellular composition, or coordinated tissue-state effect plausible. A defensible novelty claim is therefore limited to the observed cross-tissue co-abundance configuration, pending replication in independent samples and testing against cell-type composition and technical confounding.

**Hypothesis.** Hypothesis: the module reflects a shared secretory and cellular-stress state present in subsets of autonomic nervous system and breast samples. In this model, SCG2 marks neuroendocrine or vesicular secretory activity; CALU reflects endoplasmic-reticulum calcium handling and protein folding; TIMM50 reflects mitochondrial import and susceptibility to cytochrome-c release; GBE1 reflects glycogen availability; and FERMT2 reflects adhesion or mechanotransduction. Their coordinated abundance could arise from a common mixture of secretory, metabolic, mitochondrial, and adhesion-related cell states rather than direct physical interaction. This hypothesis predicts that module abundance will track neuroendocrine or secretory cell content, metabolic state, and tissue architecture, and should be tested with matched cell-type deconvolution, independent cohorts, protein-level measurements, and perturbation experiments.

### Important genes

#### SCG2

- **Related proteins** (co-abundance neighbors): PITRM1 (0.97), CALU (0.90), GBE1 (0.88), TIMM50 (0.85), FERMT2 (0.84), USP47 (0.83), CPSF7 (0.83), TPD52L2 (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: secretogranin II. The protein encoded by this gene is a member of the chromogranin/secretogranin family of neuroendocrine secretory proteins. Studies in rodents suggest that the full-length protein, secretogranin II, is involved in the packaging or sorting of peptide hormones and neuropeptides into secretory vesicles. The full-length protein is cleaved to produce the active peptide secretoneurin, which exerts chemo…
- **Diseases (Open Targets)**: psoriasis (0.316); Abnormality of the skeletal system (0.303); kidney disorder (0.266); retinal degeneration (0.261); knee fracture (0.215)
- **Europe PMC papers**: 1479
- **Why important**: SCG2 has the strongest network position and connects to the broadest set of module members. Its established role as secretogranin II places it at the clearest functional interface with neuroendocrine vesicle packaging and peptide secretion. HPA supports adrenal, brain, pituitary, and neuroendocrine associations, and the gene has extensive literature and several disease-linked annotations.
- **Conclusion**: Established evidence supports SCG2 as the principal marker of a neuroendocrine or secretory component and as the module hub. It is not established that SCG2 physically organizes the other proteins. The interpretation that it reports a shared secretory cell state is a hypothesis.

#### GBE1

- **Related proteins** (co-abundance neighbors): SCG2 (0.88), KATNAL1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 1,4-alpha-glucan branching enzyme 1. The protein encoded by this gene is a glycogen branching enzyme that catalyzes the transfer of alpha-1,4-linked glucosyl units from the outer end of a glycogen chain to an alpha-1,6 position on the same or a neighboring glycogen chain. Branching of the chains is essential to increase the solubility of the glycogen molecule and, consequently, in reducing the osmotic pressure within cells. Highest l…
- **Diseases (Open Targets)**: glycogen storage disease due to glycogen branching enzyme deficiency (0.848); adult polyglucosan body disease (0.801); glycogen storage disease due to glycogen branching enzyme deficiency, adult neuromuscular form (0.711); glycogen storage disease due to glycogen branching enzyme deficiency, congenital neuromuscular form (0.591); disorder of glycogen metabolism (0.573)
- **Europe PMC papers**: 1361
- **Why important**: GBE1 provides the clearest metabolic anchor in the module and occupies the connecting position between SCG2 and KATNAL1. It encodes the glycogen branching enzyme, is tissue-enhanced in skeletal muscle, and is associated with adipocyte, cardiomyocyte, muscle, and neutrophil-related cell types. Its established disease associations with glycogen-storage and polyglucosan disorders add strong biological relevance and it has substantial literature.
- **Conclusion**: Established evidence supports GBE1 as a glycogen and energy-metabolism marker. Its inclusion does not establish that glycogen metabolism drives the whole module. A coordinated metabolic-secretory state is a hypothesis.

#### CALU

- **Related proteins** (co-abundance neighbors): SCG2 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calumenin. The product of this gene is a calcium-binding protein localized in the endoplasmic reticulum (ER) and it is involved in such ER functions as protein folding and sorting. This protein belongs to a family of multiple EF-hand proteins (CERC) that include reticulocalbin, ERC-55, and Cab45 and the product of this gene. Alternatively spliced transcript variants encoding different isoforms have been iden…
- **Diseases (Open Targets)**: intelligence (0.490); mathematical ability (0.469); autism spectrum disorder (0.333); attention deficit-hyperactivity disorder (0.333); Alzheimer disease (0.308)
- **Europe PMC papers**: 9190
- **Why important**: CALU is directly connected to the SCG2 hub and represents a distinct intracellular process: endoplasmic-reticulum calcium binding, protein folding, and sorting. It is detected in breast and has a particularly extensive literature base, making it a useful candidate for assessing whether the module reflects secretory-pathway load or proteostatic state.
- **Conclusion**: Established evidence supports CALU as an endoplasmic-reticulum calcium and protein-handling marker. Its connection to SCG2 is a co-abundance relationship, not a known physical interaction. A shared secretory or proteostasis program remains hypothetical.

#### TIMM50

- **Related proteins** (co-abundance neighbors): SCG2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translocase of inner mitochondrial membrane 50. This gene encodes a subunit of the TIM23 inner mitochondrial membrane translocase complex. The encoded protein functions as the receptor subunit that recognizes the mitochondrial targeting signal, or presequence, on protein cargo that is destined for the mitochondrial inner membrane and matrix. This protein may also play a role in maintaining the membrane permeability barrier, and knockdown of thi…
- **Diseases (Open Targets)**: 3-methylglutaconic aciduria type 9 (0.773); neurodegenerative disease (0.519); Mitochondrial encephalopathy (0.425); hereditary disease (0.415); Epileptic encephalopathy (0.370)
- **Europe PMC papers**: 442
- **Why important**: TIMM50 is connected to SCG2 and provides a mitochondrial dimension to the module. It is a receptor subunit of the TIM23 import machinery, is linked to mitochondrial protein import and cytochrome-c release, and is detected in breast. Its disease associations include mitochondrial and neurodegenerative conditions, with a moderate literature base.
- **Conclusion**: Established evidence supports TIMM50 as a mitochondrial import and apoptosis-related marker. The module does not establish mitochondrial dysfunction, nor does it show a known TIMM50-SCG2 complex. Mitochondrial stress accompanying the shared tissue state is a hypothesis.

#### FERMT2

- **Related proteins** (co-abundance neighbors): SCG2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Focal adhesion sites; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FERM domain containing kindlin 2. Enables several functions, including actin binding activity; phosphatidylinositol-3,4,5-trisphosphate binding activity; and type I transforming growth factor beta receptor binding activity. Involved in several processes, including cell surface receptor signaling pathway; positive regulation of cell differentiation; and positive regulation of cellular component biogenesis. Acts upstream of or withi…
- **Diseases (Open Targets)**: open-angle glaucoma (0.501); prostate carcinoma (0.488); glaucoma (0.488); neurodegenerative disease (0.473); primary angle-closure glaucoma (0.407)
- **Europe PMC papers**: 1336
- **Why important**: FERMT2 is connected to SCG2 and contributes a cell-surface and tissue-architecture interpretation. It encodes kindlin two, supports integrin-mediated signaling and cell-matrix adhesion, is associated with focal adhesions, and is detected in breast. Its disease associations include glaucoma, prostate carcinoma, and neurodegenerative disease, and it has substantial literature.
- **Conclusion**: Established evidence supports FERMT2 as an adhesion and integrin-signaling marker. The available data do not establish that adhesion signaling causes the module or that FERMT2 interacts physically with SCG2. A relationship between tissue architecture, cell adhesion, and secretory-state abundance is a hypothesis.

## Module 10

**Tissue pair**: autonomic_nervous_system and breast  
**Genes (6)**: CAMSAP1, NRCAM, PRPF4, SNRNP40, STAG2, WASF1

### Function

This is a heterogeneous co-abundance module with two biologically interpretable components connected through WASF1. The WASF1–CAMSAP1–NRCAM side is consistent with neuronal development, axon guidance, cell adhesion, actin regulation, and microtubule organization, based on the supplied gene annotations and HPA tissue patterns. The PRPF4–SNRNP40 side represents established spliceosomal and small nuclear ribonucleoprotein biology, supported by their STRING relationship and their joint membership in hu.MAP complex (hu.MAP huMAP3_08980.1). STAG2 contributes a cohesin and chromosome-segregation function but is connected only to WASF1 in the module. No GO or KEGG term passed global correction, so no pathway-level enrichment is claimed. The overall module is therefore best interpreted as a mixed neural or tissue-structure and RNA-processing co-abundance signal rather than a single demonstrated biochemical pathway.

**Cell composition.** The module is not dominated by plasma or broadly secreted proteins: only NRCAM is annotated as secreted, specifically in brain. Its HPA profile is biased toward brain, retina, adrenal gland, and reproductive or germ-cell-associated contexts, while several genes have low tissue specificity. Most genes have low immune-cell specificity, although WASF1 has group-enriched B-cell and plasmacytoid-dendritic-cell patterns and NRCAM is immune-cell enriched in a T-cell population. This does not establish blood contamination, but it means shared immune or cellular-composition effects cannot be excluded. Protein detection in breast is present for most module genes, whereas matching HPA protein data are unavailable for autonomic nervous system tissue. The module therefore appears more compatible with shared cellular programs or tissue composition than with a plasma-protein module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest established molecular relationship is PRPF4–SNRNP40 in STRING. These proteins also occur together in hu.MAP complex (hu.MAP huMAP3_08980.1), a large spliceosomal or small nuclear ribonucleoprotein assembly containing many additional splicing factors. This supports the interpretation that their co-abundance reflects a real RNA-splicing complex relationship. No STRING partners or hu.MAP complexes were supplied for WASF1, CAMSAP1, STAG2, or NRCAM. Consequently, the remaining module edges should be treated as co-abundance associations rather than confirmed physical interactions. The single known spliceosomal connection anchors only part of the module and does not demonstrate that all members form one complex.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: PRPF4–SNRNP40 (0.986)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (PRPF4, SNRNP40; 2/97)

### Novelty

The module should not be described as a newly discovered molecular complex. The PRPF4–SNRNP40 relationship and their participation in a known spliceosomal complex are established. The functions of WASF1, CAMSAP1, NRCAM, and STAG2 are also individually well characterized. What may be novel is the observation that these otherwise distinct programs are conserved in a co-abundance module shared by autonomic nervous system and breast tissues. However, the supplied evidence does not establish whether that shared pattern reflects a new regulatory mechanism, common cell types, tissue composition, or technical structure. Absence of STRING or hu.MAP support for several edges is evidence of limited prior interaction annotation, not proof of novelty.

**Hypothesis.** Hypothesis: the conserved module may reflect coordinated abundance of neural or tissue-structural proteins with a general RNA-processing and proliferative state. In neural or neuroendocrine-like cells, NRCAM-mediated adhesion and signaling could be associated with CAMSAP1-dependent microtubule organization and WASF1-dependent actin remodeling, while PRPF4 and SNRNP40 support the splicing capacity required for cellular maintenance or state transitions. STAG2 may link the WASF1-associated signal to cell-cycle or chromosomal organization in a subset of cells. This hypothesis is not demonstrated by enrichment, because no GO or KEGG term passed global correction, and it should be tested with cell-type-resolved expression, proteomics, perturbation, and independent cohorts.

### Important genes

#### WASF1

- **Related proteins** (co-abundance neighbors): STAG2 (0.87), PRPF4 (0.83), CAMSAP1 (0.83), SNRNP40 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Group enriched; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WASP family member 1. The protein encoded by this gene, a member of the Wiskott-Aldrich syndrome protein (WASP)-family, plays a critical role downstream of Rac, a Rho-family small GTPase, in regulating the actin cytoskeleton required for membrane ruffling. It has been shown to associate with an actin nucleation core Arp2/3 complex while enhancing actin polymerization in vitro. Wiskott-Aldrich syndrome is a disease of t…
- **Diseases (Open Targets)**: neurodevelopmental disorder with absent language and variable seizures (0.721); Intellectual disability (0.547); hereditary disease (0.413); complex neurodevelopmental disorder (0.370); Epileptic encephalopathy (0.334)
- **Europe PMC papers**: 676
- **Why important**: WASF1 is the most central connector in the module's co-abundance structure, linking the cytoskeletal and neuronal-associated genes with the spliceosomal pair and STAG2. Its supplied annotations support Rac signaling, actin filament polymerization, membrane remodeling, receptor-mediated endocytosis, and neuron projection development. HPA places it in brain and testis-associated contexts and also reports immune-cell group enrichment. It has substantial literature coverage and disease associations involving neurodevelopmental disorders, intellectual disability, and seizures.
- **Conclusion**: Established evidence supports WASF1 as a cytoskeletal and signaling regulator with neural and immune relevance, and its network position makes it the leading candidate for coordinating otherwise distinct module components. It is plausible, but unproven, that WASF1 links tissue architecture to the RNA-processing signal. The module does not establish that WASF1 directly interacts with PRPF4, SNRNP40, CAMSAP1, or STAG2.

#### NRCAM

- **Related proteins** (co-abundance neighbors): CAMSAP1 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neuronal cell adhesion molecule. Cell adhesion molecules (CAMs) are members of the immunoglobulin superfamily. This gene encodes a neuronal cell adhesion molecule with multiple immunoglobulin-like C2-type domains and fibronectin type-III domains. This ankyrin-binding protein is involved in neuron-neuron adhesion and promotes directional signaling during axonal cone growth. This gene is also expressed in non-neural tissues and may…
- **Diseases (Open Targets)**: neurodevelopmental disorder with neuromuscular and skeletal abnormalities (0.774); complex neurodevelopmental disorder (0.370); stroke disorder (0.261); alcohol drinking (0.257); ovarian neoplasm (0.255)
- **Europe PMC papers**: 2314
- **Why important**: NRCAM is a neuronal cell-adhesion molecule with supplied functions in axonogenesis, axon guidance, neuronal migration, axonal fasciculation, and synapse assembly. It shows enhanced expression in adrenal gland, brain, and retina and is secreted in brain. Its disease associations include neurodevelopmental and neuromuscular disorders. Although it is peripheral in the module graph, it gives the module a strong neural or neuroendocrine tissue interpretation.
- **Conclusion**: Established evidence supports NRCAM as a neural cell-adhesion and axon-guidance protein, making it important for interpreting the tissue context. Its association with CAMSAP1 is a co-abundance relationship in this module, not a demonstrated physical interaction. A neural-cell or tissue-architecture contribution is a reasonable hypothesis, but direct relevance to breast biology is not established here.

#### CAMSAP1

- **Related proteins** (co-abundance neighbors): NRCAM (0.87), WASF1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitotic spindle, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calmodulin regulated spectrin associated protein 1. Enables microtubule minus-end binding activity and spectrin binding activity. Involved in several processes, including neuron projection development; regulation of cell morphogenesis; and regulation of microtubule polymerization. Located in microtubule. Colocalizes with microtubule minus-end. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: cortical dysplasia, complex, with other brain malformations 12 (0.672); neurodegenerative disease (0.509); hereditary disease (0.194); Abnormality of neuronal migration (0.190); preeclampsia (0.173)
- **Europe PMC papers**: 457
- **Why important**: CAMSAP1 connects to NRCAM and WASF1 and is annotated as a microtubule minus-end and spectrin-binding protein involved in microtubule organization, regulation of microtubule polymerization, cell morphogenesis, and neuron projection development. HPA strongly associates it with retina and several ocular or photoreceptor cell types. Its disease associations include cortical dysplasia and other brain-development or neurodegenerative conditions.
- **Conclusion**: Established evidence supports CAMSAP1 as a microtubule-organizing and morphogenesis factor with neural and retinal relevance. Its position reinforces a structural-cellular interpretation of the module. The data support coordinated abundance with NRCAM and WASF1, but do not prove that CAMSAP1 mechanistically bridges adhesion and actin regulation in these tissues.

#### PRPF4

- **Related proteins** (co-abundance neighbors): WASF1 (0.83); STRING partners: SNRNP40 (0.986)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: pre-mRNA splicing tri-snRNP complex factor PRPF4. The protein encoded by this gene is part of a heteromeric complex that binds U4, U5, and U6 small nuclear RNAs and is involved in pre-mRNA splicing. The encoded protein also is a mitotic checkpoint protein and a regulator of chemoresistance in human ovarian cancer. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: retinitis pigmentosa (0.634); retinitis pigmentosa 70 (0.578); inherited retinal dystrophy (0.377); neurodegenerative disease (0.203); refractive error (0.083)
- **Europe PMC papers**: 461
- **Why important**: PRPF4 is directly supported by STRING association with SNRNP40 and by shared membership in hu.MAP complex (hu.MAP huMAP3_08980.1). Its annotated functions include spliceosomal tri-snRNP assembly, pre-mRNA splicing, spliceosomal conformational change, and a mitotic checkpoint role. It also has disease associations involving retinal degeneration and neurodegenerative disease.
- **Conclusion**: Established evidence identifies PRPF4 as a spliceosome-associated factor, and its relationship with SNRNP40 is the best-supported molecular interaction in the module. It provides a credible RNA-processing component. Whether its co-abundance with WASF1 reflects a shared cell state, coordinated transcriptional regulation, or indirect tissue composition remains unresolved.

#### SNRNP40

- **Related proteins** (co-abundance neighbors): WASF1 (0.82); STRING partners: PRPF4 (0.986)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in breast
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 40. This gene encodes a component of the U5 small nuclear ribonucleoprotein (snRNP) particle. The U5 snRNP is part of the spliceosome, a multiprotein complex that catalyzes the removal of introns from pre-messenger RNAs. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.530); dengue disease (0.377); X-linked lymphoproliferative syndrome (0.058); autoimmune lymphoproliferative syndrome (0.055); Familial hemophagocytic lymphohistiocytosis (0.053)
- **Europe PMC papers**: 235
- **Why important**: SNRNP40 is the partner of PRPF4 in STRING and hu.MAP complex (hu.MAP huMAP3_08980.1). Its supplied annotations identify it as a component of the spliceosomal U5 small nuclear ribonucleoprotein and as a participant in intron removal, spliceosomal assembly, and RNA processing. HPA reports low tissue specificity but enrichment in an early germ-cell population, consistent with a broadly required cellular process.
- **Conclusion**: Established evidence supports SNRNP40 as a core spliceosomal factor and validates the PRPF4–SNRNP40 submodule. Its presence does not imply that the entire module is spliceosomal, because the other genes lack corresponding complex or STRING support. A shared RNA-processing state is a hypothesis rather than a demonstrated explanation for the full module.

## Module 11

**Tissue pair**: autonomic_nervous_system and breast  
**Genes (8)**: CCNY, GSR, GSK3B, RBM27, SESN3, SLC25A1, UTP25, SLC30A1

### Function

The module is best interpreted as a stress-responsive metabolic and cellular-maintenance program rather than as a single established pathway. SESN3 is the central co-abundance hub and is annotated with oxidative-stress control, glucose and insulin responses, amino-acid starvation responses, autophagy, and TORC2 signaling. GSR supports redox homeostasis, SLC25A1 supports mitochondrial citrate transport and is linked to ferroptosis regulation, and GSK3B connects energy metabolism, inflammation, ER stress, mitochondrial dysfunction, apoptosis, and phosphorylation. SLC30A1 adds intracellular zinc and calcium transport, while CCNY, RBM27, and UTP25 suggest links to cell-cycle regulation, RNA processing, and nucleolar ribosome biogenesis. These annotations are biologically compatible with coordinated management of redox state, nutrient status, mitochondrial metabolism, and cellular growth. However, no GO or KEGG term passed global correction, so this is an integrative functional interpretation rather than evidence of statistically established pathway enrichment.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not strongly blood-cell specific overall, although several genes show immune-cell enhancement and individual associations with neutrophils, basophils, eosinophils, or neutrophil progenitors. Most genes have low tissue specificity, while selected genes are enhanced in liver or testis and several show enrichment in spermatogenic, retinal pigment epithelial, hepatocyte, or other specialized cell types. This pattern is more consistent with a broadly distributed intracellular program with cell-type-dependent expression than with a circulating protein module. The breast protein evidence supports presence of several module proteins in breast, but the absence of matching autonomic-nervous-system HPA tissue data limits tissue-specific interpretation. Shared cell composition or shared cellular stress and metabolic states could therefore contribute to the co-abundance pattern.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module gene pair reaches the supplied high-confidence STRING interaction criterion, STRING functional enrichment is absent, and no hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not supported here as previously catalogued direct physical interactions or as membership in a known multiprotein complex. The star-like structure centered on SESN3 may represent coordinated regulation, shared expression control, or a common cell-state signal rather than a physical molecular assembly. The absence of STRING and hu.MAP support reduces confidence in a direct interaction mechanism but does not invalidate the reproducible co-abundance observation.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module appears potentially novel as a tissue-pair co-abundance pattern because its member combination has no accompanying high-confidence STRING network, no multi-member hu.MAP complex, and no globally significant GO or KEGG term. Its novelty should be stated cautiously: absence from these resources does not prove that the biological relationship is new, and the module may reflect a known regulatory state assembled across otherwise separate pathways. The strongest potentially distinctive feature is the co-abundance of SESN3 with redox, mitochondrial transport, metal transport, kinase, RNA-processing, and cell-cycle genes in both autonomic nervous system and breast. Independent replication, preservation across cohorts, cell-type deconvolution, and perturbation experiments would be needed before calling it a new mechanism.

**Hypothesis.** Hypothesis: the shared module reflects a SESN3-centered cellular adaptation program that coordinates nutrient and oxidative-stress sensing with antioxidant regeneration, mitochondrial citrate handling, metal-ion homeostasis, kinase signaling, and growth-related RNA or cell-cycle processes. In this model, SESN3 acts as the regulatory hub, GSR buffers oxidant load, SLC25A1 couples mitochondrial carbon metabolism to stress responses, SLC30A1 modulates metal-dependent cellular state, and GSK3B transmits metabolic and stress signals. CCNY, RBM27, and UTP25 may reflect downstream effects on proliferation, transcript processing, or ribosome production rather than direct components of one complex. This model remains a hypothesis because enrichment, STRING, and hu.MAP evidence do not independently establish a shared pathway or physical complex.

### Important genes

#### SESN3

- **Related proteins** (co-abundance neighbors): UTP25 (0.96), SLC30A1 (0.90), CCNY (0.88), RBM27 (0.87), SLC25A1 (0.84), GSK3B (0.83), GSR (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sestrin 3. This gene encodes a member of the sestrin family of stress-induced proteins. The encoded protein reduces the levels of intracellular reactive oxygen species induced by activated Ras downstream of RAC-alpha serine/threonine-protein kinase (Akt) and FoxO transcription factor. The protein is required for normal regulation of blood glucose, insulin resistance and plays a role in lipid storage in obesi…
- **Diseases (Open Targets)**: neurodegenerative disease (0.402); Abnormality of the skeletal system (0.375); atrial fibrillation (0.348); gestational diabetes (0.282); Graves disease (0.265)
- **Europe PMC papers**: 951
- **Why important**: SESN3 is the central network hub, connecting every other module member, and is the clearest functional anchor. Its annotations directly involve oxidative-stress reduction, glucose and insulin regulation, amino-acid and glucose starvation responses, autophagy, TORC2 signaling, and lipid storage. It has disease associations spanning neurodegenerative disease, skeletal abnormalities, atrial fibrillation, gestational diabetes, and Graves disease, together with substantial literature coverage. Its tissue and cell-type pattern is selective rather than ubiquitous, including testis and several specialized cell types.
- **Conclusion**: Established evidence supports SESN3 as the principal candidate regulator of a stress and metabolic co-abundance program. It is plausible, but not established, that SESN3 drives the other module genes in the shared tissue context.

#### GSK3B

- **Related proteins** (co-abundance neighbors): SESN3 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycogen synthase kinase 3 beta. The protein encoded by this gene is a serine-threonine kinase belonging to the glycogen synthase kinase subfamily. It is a negative regulator of glucose homeostasis and is involved in energy metabolism, inflammation, ER-stress, mitochondrial dysfunction, and apoptotic pathways. Defects in this gene have been associated with Parkinson disease and Alzheimer disease. [provided by RefSeq, Aug 2017].
- **Diseases (Open Targets)**: bipolar disorder (0.614); major depressive disorder (0.572); bipolar I disorder (0.571); cancer (0.557); Alzheimer disease (0.554)
- **Europe PMC papers**: 15204
- **Why important**: GSK3B is directly connected to the module hub and has broad, well-established functions in phosphorylation, glucose metabolism, inflammation, ER stress, mitochondrial dysfunction, apoptosis, cell-matrix adhesion, and developmental signaling. It has extensive literature coverage and disease associations including bipolar disorder, major depressive disorder, cancer, and Alzheimer disease. Its presence provides a credible signaling route through which metabolic or oxidative state could influence cellular behavior.
- **Conclusion**: Established evidence supports GSK3B as a biologically important stress, metabolism, and signaling effector. Its membership in this particular module is consistent with the proposed mechanism, but the co-abundance data do not show that GSK3B directly mediates the module.

#### GSR

- **Related proteins** (co-abundance neighbors): SESN3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutathione-disulfide reductase. This gene encodes a member of the class-I pyridine nucleotide-disulfide oxidoreductase family. This enzyme is a homodimeric flavoprotein. It is a central enzyme of cellular antioxidant defense, and reduces oxidized glutathione disulfide (GSSG) to the sulfhydryl form GSH, which is an important cellular antioxidant. Rare mutations in this gene result in hereditary glutathione reductase deficiency. M…
- **Diseases (Open Targets)**: hemolytic anemia due to glutathione reductase deficiency (0.702); glioblastoma (0.558); plasma cell myeloma (0.537); Hodgkins lymphoma (0.531); non-Hodgkin lymphoma (0.506)
- **Europe PMC papers**: 6439
- **Why important**: GSR is connected to SESN3 and encodes the central enzyme that regenerates reduced glutathione from oxidized glutathione. Its annotations directly support glutathione metabolism, cellular oxidant detoxification, redox homeostasis, and responses to oxidative stress. It has extensive literature coverage and disease associations involving glutathione reductase deficiency, hemolytic anemia, glioblastoma, and hematologic malignancies. Its enrichment in neutrophil progenitors and immune-cell enhancement may also make it sensitive to cellular composition.
- **Conclusion**: Established evidence supports GSR as the strongest antioxidant-defense component of the module. It is a plausible functional partner of SESN3 in redox adaptation, although a direct regulatory relationship is not demonstrated.

#### SLC25A1

- **Related proteins** (co-abundance neighbors): SESN3 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 25 member 1. This gene encodes a member of the mitochondrial carrier subfamily of solute carrier proteins. Members of this family include nuclear-encoded transporters that translocate small metabolites across the mitochondrial membrane. This protein regulates the movement of citrate across the inner membranes of the mitochondria. Mutations in this gene have been associated with combined D-2- and L-2-hydroxyglu…
- **Diseases (Open Targets)**: D,L-2-hydroxyglutaric aciduria (0.827); presynaptic congenital myasthenic syndrome (0.653); 2-hydroxyglutaric aciduria (0.506); hereditary disease (0.413); mitochondrial disease (0.370)
- **Europe PMC papers**: 1568
- **Why important**: SLC25A1 is connected to SESN3 and transports citrate across the inner mitochondrial membrane, linking mitochondrial metabolism with cytosolic biosynthetic and signaling processes. Its annotations include mitochondrial citrate transport, succinate transport, and negative regulation of ferroptosis. It has extensive literature coverage and strong disease relevance through D- and L-hydroxyglutaric aciduria, congenital myasthenic syndrome, and mitochondrial disease. Its hepatocyte and other metabolically active cell-type associations fit the metabolic interpretation of the module.
- **Conclusion**: Established evidence supports SLC25A1 as the mitochondrial metabolic component of the module. Its coordinated expression with SESN3 could indicate coupling between nutrient-stress sensing and mitochondrial carbon handling, but this remains a hypothesis.

#### SLC30A1

- **Related proteins** (co-abundance neighbors): SESN3 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 30 member 1. Predicted to enable calcium channel inhibitor activity and zinc ion transmembrane transporter activity. Predicted to be involved in several processes, including cellular divalent inorganic cation homeostasis; inorganic cation transmembrane transport; and negative regulation of transport. Predicted to act upstream of or within in utero embryonic development. Located in several cellular components, …
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); Abnormality of the skeletal system (0.428); type 2 diabetes mellitus (0.314); poisoning (0.194); glaucoma (0.178)
- **Europe PMC papers**: 890
- **Why important**: SLC30A1 is connected to SESN3 and encodes a membrane transporter implicated in zinc, calcium, and broader divalent-cation homeostasis. Metal-ion balance can influence redox chemistry, signaling, and cellular stress responses, making this gene a useful mechanistic bridge to the SESN3 and GSR annotations. It has substantial literature coverage and disease associations involving neurodegenerative disease, skeletal abnormalities, type two diabetes, poisoning, and glaucoma. Its liver and hepatocyte enhancement is consistent with the module's metabolic component.
- **Conclusion**: Established evidence supports SLC30A1 as a metal-homeostasis component with potential relevance to stress signaling. Its proposed coordination with SESN3 and GSR is biologically plausible but is not established by the available interaction or enrichment evidence.

## Module 12

**Tissue pair**: autonomic_nervous_system and breast  
**Genes (6)**: CGN, KNTC1, LZIC, NOL8, NUF2, NAPB

### Function

No GO/KEGG term passed global correction, and there was no supplementary STRING functional-enrichment result. The strongest biological signal is therefore gene-level and network-level rather than enrichment-level. NAPB is the central module gene and has established roles in SNAP-dependent vesicle docking and fusion, SNARE-complex disassembly, synaptic vesicle priming, and glutamatergic transmission. NUF2 and KNTC1 form a coherent cell-division axis involving the NDC80 kinetochore machinery, chromosome segregation, spindle organization, and the spindle assembly checkpoint. CGN represents epithelial junction and microtubule-cytoskeleton biology, while NOL8 represents nucleolar localization and ribosomal RNA processing, and LZIC has predicted beta-catenin binding and a radiation-response annotation. Overall, the module is best interpreted as a co-abundance pattern linking a brain-associated vesicle-trafficking gene to genes reflecting proliferative, epithelial, nucleolar, and kinetochore-related cellular states, rather than as a single experimentally established pathway.

**Cell composition.** The module is not plasma-derived or secreted: the HPA summary reports no secreted genes. It is also not predominantly immune-cell specific, although NUF2 is immune-cell enhanced in T-reg cells. The HPA pattern is heterogeneous, with brain and retina enrichment for NAPB, intestinal enrichment for CGN, bone-marrow and lymphoid enrichment for NUF2, bone-marrow enrichment for KNTC1, and reproductive-cell enrichment for several genes. All module genes are cell-type enhanced in HPA, including erythrocyte or megakaryocyte progenitor signals for NUF2, KNTC1, and NOL8 and germ-cell signals for NUF2, LZIC, and KNTC1. Thus, the shared module may partly reflect differing mixtures of proliferative or specialized cell types in the two tissues. Breast protein detection is present for most genes, whereas matched autonomic-nervous-system protein data are unavailable, so the tissue-level biological interpretation should be cautious.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship within the module is the established KNTC1-NUF2 interaction. This supports a real kinetochore and chromosome-segregation substructure involving those genes. NAPB has the highest weighted connectivity in the co-abundance graph and is connected to every other module member, but STRING reports no partner for NAPB within this module. CGN, LZIC, and NOL8 likewise have no reported STRING partner in the module. No hu.MAP complex contains at least two module members. Consequently, the co-abundance structure is broader than the currently catalogued physical-interaction structure: one known kinetochore relationship is embedded in a network whose remaining links may represent co-expression, shared cell composition, indirect regulation, or context-specific biology rather than direct binding.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: KNTC1–NUF2 (0.762)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a novel tissue-pair co-abundance pattern, but it cannot be claimed as a newly discovered molecular complex or pathway. The lack of a matching hu.MAP complex and the sparse STRING connectivity indicate that most within-module relationships are not already represented as known physical associations. However, absence from those resources does not establish novelty, because the module combines genes with independently known functions and may be driven partly by cell-type composition. The strongest defensible claim is novelty of the cross-tissue co-abundance configuration and its possible biological context, pending validation in independent cohorts, cell-resolved data, and perturbation experiments.

**Hypothesis.** Hypothesis: the module captures a shared cellular-state program present in autonomic nervous system and breast samples, in which NAPB-centered vesicle or membrane-trafficking biology covaries with epithelial-junction organization, nucleolar activity, and proliferative kinetochore function. The pattern could arise from coordinated regulation in a specialized cell population, but it could also be a composition signal caused by mixing neural, epithelial, germline-like, and hematopoietic or progenitor-associated expression states. A testable prediction is that the module will separate into a vesicle-trafficking component centered on NAPB and a proliferation or chromosome-segregation component centered on NUF2 and KNTC1 when analyzed with single-cell or deconvolution methods.

### Important genes

#### NAPB

- **Related proteins** (co-abundance neighbors): NOL8 (0.86), CGN (0.85), NUF2 (0.84), LZIC (0.83), KNTC1 (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NSF attachment protein beta. This gene encodes a member of the soluble N-ethyl-maleimide-sensitive fusion attachment protein (SNAP) family. SNAP proteins play a critical role in the docking and fusion of vesicles to target membranes as part of the 20S NSF-SNAP-SNARE complex. This gene encodes the SNAP beta isoform which has been shown to be preferentially expressed in brain tissue. The encoded protein also interacts with the …
- **Diseases (Open Targets)**: neurodegenerative disease (0.401); neurodevelopmental disorder (0.375); hereditary disease (0.191); abortion (0.187); X-linked spasticity-intellectual disability-epilepsy syndrome (0.111)
- **Europe PMC papers**: 1004
- **Why important**: NAPB is the topological hub, connected to every other module gene with the greatest weighted strength. Its established SNAP-family function links it to vesicle docking and fusion, SNARE-complex disassembly, synaptic vesicle priming, and glutamatergic transmission. HPA supports a brain and retina association, and the gene has substantial literature and disease-context coverage.
- **Conclusion**: Established evidence supports NAPB as the principal neural vesicle-trafficking anchor of the module. Its hub position is consistent with a coordinating role in the co-abundance pattern, but does not prove that NAPB physically regulates the other module genes.

#### NUF2

- **Related proteins** (co-abundance neighbors): NAPB (0.84); STRING partners: KNTC1 (0.762)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NUF2 component of NDC80 kinetochore complex. This gene encodes a protein that is highly similar to yeast Nuf2, a component of a conserved protein complex associated with the centromere. Yeast Nuf2 disappears from the centromere during meiotic prophase when centromeres lose their connection to the spindle pole body, and plays a regulatory role in chromosome segregation. The encoded protein is found to be associated with centromeres of mitotic…
- **Diseases (Open Targets)**: gout (0.458); irritable bowel syndrome (0.438); bipolar disorder (0.426); mathematical ability (0.401); prostate carcinoma (0.400)
- **Europe PMC papers**: 1971
- **Why important**: NUF2 contributes the clearest cell-division annotation, including kinetochore attachment, spindle assembly checkpoint signaling, spindle organization, and chromosome segregation. It is linked by STRING to KNTC1, and HPA associates it with bone marrow, lymphoid tissue, testis, T-reg cells, and progenitor or germ-cell states. Its literature volume is substantial.
- **Conclusion**: Established evidence supports NUF2 as a kinetochore and proliferative-state marker within the module. Its tissue and cell-type pattern makes cell composition a plausible explanation for its co-abundance with the other genes; a direct connection to NAPB is only a hypothesis.

#### KNTC1

- **Related proteins** (co-abundance neighbors): NAPB (0.82); STRING partners: NUF2 (0.762)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinetochore associated 1. This gene encodes a protein that is one of many involved in mechanisms to ensure proper chromosome segregation during cell division. Experimental evidence indicated that the encoded protein functioned in a similar manner to that of the Drosophila rough deal protein. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.314); osteoarthritis, knee (0.278); osteoarthritis (0.264); preeclampsia (0.178); total knee arthroplasty (0.148)
- **Europe PMC papers**: 576
- **Why important**: KNTC1 is the STRING-linked partner of NUF2 and has established roles in kinetochore assembly, sister-chromatid segregation, spindle-checkpoint signaling, and regulation of mitotic exit. HPA shows bone-marrow and progenitor cell associations, while its network connection to NAPB places it in the module's broader co-abundance pattern.
- **Conclusion**: Established evidence supports KNTC1 as the second component of the module's kinetochore substructure. Its co-abundance with NAPB may reflect a shared proliferative or cell-mixture context rather than a direct functional partnership.

#### CGN

- **Related proteins** (co-abundance neighbors): NAPB (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cell Junctions; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cingulin. Enables cadherin binding activity. Predicted to act upstream of or within bicellular tight junction assembly; epithelial cell morphogenesis; and microtubule cytoskeleton organization. Located in bicellular tight junction and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.359); nonsyndromic deafness (0.118); skin disorder (0.094); colorectal carcinoma (0.086); ovarian carcinoma (0.065)
- **Europe PMC papers**: 3593
- **Why important**: CGN provides the clearest epithelial interpretation. It encodes cingulin, has cadherin-binding and bicellular tight-junction annotations, and is associated with epithelial morphogenesis and microtubule-cytoskeleton organization. HPA shows intestinal and multiple epithelial cell-type associations, and the gene has the largest literature volume among the module members.
- **Conclusion**: Established evidence supports CGN as an epithelial junction and cytoskeletal marker. Its link to NAPB in the co-abundance graph is not supported by an identified STRING or hu.MAP physical association, so any shared mechanism remains hypothetical.

#### NOL8

- **Related proteins** (co-abundance neighbors): NAPB (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleolar protein 8. NOL8 binds Ras-related GTP-binding proteins (see MIM 608267) and plays a role in cell growth (Sekiguchi et al., 2004 [PubMed 14660641]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.281); Abnormality of the skeletal system (0.218); obstructive sleep apnea syndrome (0.105); maturity-onset diabetes of the young (0.068); mononeuropathy (0.062)
- **Europe PMC papers**: 142
- **Why important**: NOL8 adds a nucleolar and biosynthetic dimension through established roles in rRNA processing and nucleolar protein localization. It connects directly to the module hub NAPB in the co-abundance graph and is associated by HPA with megakaryocyte-erythroid progenitors. Its literature base is smaller than that of the other selected genes, making it a potentially informative but less established module component.
- **Conclusion**: Established evidence supports NOL8 as a nucleolar and growth-associated marker. Its module relationship may reflect a shared progenitor or cellular-state signal; a mechanistic link to vesicle trafficking is not established.

## Module 13

**Tissue pair**: autonomic_nervous_system and breast  
**Genes (10)**: CS, CPSF2, CTR9, FRAS1, GALNT2, IFI16, LMNB1, NUP93, RCL1, SMARCC2

### Function

This is a heterogeneous co-abundance module rather than a convincingly defined canonical pathway. No GO/KEGG term passed global correction, and there was no supplementary STRING enrichment. The genes span extracellular-matrix and epithelial-structure biology through FRAS1, mitochondrial oxidative metabolism through CS, nuclear transport through NUP93, chromatin remodeling through SMARCC2, transcriptional regulation through CTR9, RNA processing through CPSF2 and RCL1, nuclear-envelope biology through LMNB1, innate immune and cytokine regulation through IFI16, and Golgi O-linked glycosylation through GALNT2. The strongest structural observation is that FRAS1 is connected to every other module member, whereas the remaining genes are attached to FRAS1 without additional within-module edges. Thus, the module may represent coordinated abundance across several cellular programs rather than a single molecular complex or pathway.

**Cell composition.** The module is not predominantly plasma or secreted: only a minority of genes are annotated as secreted, and the listed secretome annotations are intracellular and membrane rather than circulating proteins. It is also not blood-cell enriched according to HPA: nearly all genes have low immune-cell specificity and no enriched blood-cell population is listed. Most genes have low tissue specificity, while the tissue-enhanced signals are dispersed across thyroid gland, skeletal muscle, tongue, bone marrow, lymphoid tissue, and liver. Cell-type-enhanced annotations are also dispersed, including renal epithelial populations, microglia, vascular endothelial cells, developing blood-cell populations, and other specialized cells. Breast protein detection is present for most assessed genes, but the autonomic nervous system has no matching HPA tissue assessment. Overall, the HPA evidence argues against a simple plasma-protein or blood-cell module and is more consistent with broadly distributed cellular proteins, mixed cell composition, or a shared abundance program that requires validation at the cell-type level.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, no STRING functional-enrichment result is reported, and no hu.MAP complex contains multiple module members. Therefore, the co-abundance edges are not supported here as established physical interactions or membership in a known multiprotein complex. The absence of database relationships does not disprove biological coordination: several genes are nuclear, metabolic, membrane-associated, or extracellular-matrix proteins whose relationships could be indirect, regulatory, cell-state dependent, or absent from the queried resources. The network topology should therefore be interpreted as a co-abundance structure centered on FRAS1, not as a validated protein-interaction complex.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel co-abundance association, but it cannot be called a new biological pathway or a newly discovered molecular complex from these data alone. The evidence supporting novelty is that the module has no reported high-confidence STRING interactions, no multi-member hu.MAP complex, and no globally significant GO/KEGG annotation. However, database absence alone is not proof of novelty, and the module contains well-studied genes with established functions and disease associations. A stronger novelty claim would require independent replication across cohorts, adjustment for tissue and cell composition, confirmation at the protein level, and targeted testing of the FRAS1-centered relationships.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state or tissue-composition signal in which FRAS1-associated extracellular-matrix and epithelial-structure biology covaries with broadly expressed mitochondrial, nuclear-envelope, transcriptional, chromatin, RNA-processing, innate-immune, and Golgi functions. One possible mechanism is that remodeling or altered abundance of epithelial or stromal compartments changes FRAS1 together with downstream changes in cellular biosynthetic and nuclear programs. This is a hypothesis, not an established pathway: the lack of globally significant GO/KEGG enrichment, STRING support, and hu.MAP support means that direct molecular coupling remains unproven.

### Important genes

#### FRAS1

- **Related proteins** (co-abundance neighbors): CS (0.92), NUP93 (0.88), CPSF2 (0.85), LMNB1 (0.85), IFI16 (0.84), RCL1 (0.82), SMARCC2 (0.82), GALNT2 (0.80), CTR9 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Fraser extracellular matrix complex subunit 1. This gene encodes an extracellular matrix protein that appears to function in the regulation of epidermal-basement membrane adhesion and organogenesis during development. Mutations in this gene cause Fraser syndrome, a multisystem malformation that can include craniofacial, urogenital and respiratory system abnormalities. Alternative splicing results in multiple transcript variants. [provided by R…
- **Diseases (Open Targets)**: Fraser syndrome (0.809); renal agenesis (0.564); congenital anomaly of kidney and urinary tract (0.472); hereditary disease (0.417); renal agenesis, unilateral (0.370)
- **Europe PMC papers**: 1305
- **Why important**: FRAS1 is the clear network hub, with connections to every other module member and the greatest weighted network strength. Its established annotation is extracellular-matrix regulation, epidermal-basement-membrane adhesion, epithelial-structure maintenance, and organogenesis. It is tissue enhanced in thyroid gland, detected in breast, and associated with Fraser syndrome and renal developmental disorders. Its literature volume is substantial, supporting biological interpretability, while its central position makes it the principal candidate for explaining the module's topology.
- **Conclusion**: Established evidence supports FRAS1 as an extracellular-matrix and epithelial-structure protein and as the central statistical node of this module. The hypothesis that FRAS1 organizes or drives the abundance relationships with the other genes is not established, because no STRING or hu.MAP relationship supports direct molecular coupling.

#### CS

- **Related proteins** (co-abundance neighbors): FRAS1 (0.92); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS is the module's representative mitochondrial metabolic gene and is connected directly to FRAS1. It encodes citrate synthase, a core enzyme of the tricarboxylic acid cycle found broadly in oxidative cells. HPA shows tissue enhancement in skeletal muscle and tongue, and its very large literature base makes it a strong marker of mitochondrial oxidative capacity or cellular metabolic state. Its disease associations include neurodegenerative and central-nervous-system autoimmune conditions.
- **Conclusion**: Established evidence supports CS as a broadly expressed mitochondrial oxidative-metabolism marker. In this module, its co-abundance with FRAS1 may indicate tissue metabolic state or cellular composition, but a specific FRAS1-to-CS mechanism is only a hypothesis.

#### SMARCC2

- **Related proteins** (co-abundance neighbors): FRAS1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SWI/SNF related BAF chromatin remodeling complex subunit C2. The protein encoded by this gene is a member of the SWI/SNF family of proteins, whose members display helicase and ATPase activities and which are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI and contains a predicted leucine zipper motif typical …
- **Diseases (Open Targets)**: Coffin-Siris syndrome 8 (0.720); Intellectual disability (0.564); Coffin-Siris syndrome (0.503); hereditary disease (0.468); Global developmental delay (0.463)
- **Europe PMC papers**: 1300
- **Why important**: SMARCC2 is a component of the ATP-dependent SWI/SNF chromatin-remodeling machinery and is directly connected to FRAS1. It is annotated for chromatin remodeling, transcriptional regulation, and cell differentiation, with cell-type enhancement in several renal epithelial populations. Its disease associations include Coffin-Siris syndrome and intellectual disability, and it has a substantial literature base. It therefore represents a plausible regulatory-state component of the module.
- **Conclusion**: Established evidence supports SMARCC2 as a chromatin and transcriptional regulator. Its coordinated abundance with FRAS1 could reflect epithelial differentiation or remodeling of cellular state, but the available evidence does not establish direct regulation by FRAS1 or membership in a shared complex.

#### IFI16

- **Related proteins** (co-abundance neighbors): FRAS1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: interferon gamma inducible protein 16. This gene encodes a member of the HIN-200 (hematopoietic interferon-inducible nuclear antigens with 200 amino acid repeats) family of cytokines. The encoded protein contains domains involved in DNA binding, transcriptional regulation, and protein-protein interactions. The protein localizes to the nucleoplasm and nucleoli, and interacts with p53 and retinoblastoma-1. It modulates p53 function, and …
- **Diseases (Open Targets)**: aging (0.205); Anisometropia (0.199); Decreased total leukocyte count (0.114); infection (0.114); retinitis pigmentosa (0.112)
- **Europe PMC papers**: 4990
- **Why important**: IFI16 contributes an innate-immune and cytokine-regulatory dimension and is directly connected to FRAS1. It is annotated for innate immune activation, cytokine production, autophagy, and myeloid differentiation, with cell-type enhancement in microglia, neutrophils, vascular endothelial cells, and other specialized populations. It interacts functionally with transcriptional regulators such as p five three and retinoblastoma one according to the supplied annotation, and it has a substantial literature base. Its presence makes cell-state or inflammatory context a plausible consideration.
- **Conclusion**: Established evidence supports IFI16 as a nuclear innate-immune and transcriptional regulator. Its co-abundance may reflect inflammatory or cell-state variation accompanying epithelial or stromal variation, but an FRAS1–IFI16 regulatory connection is not demonstrated by the supplied interaction resources.

#### NUP93

- **Related proteins** (co-abundance neighbors): FRAS1 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 represents nuclear-pore and nucleocytoplasmic-transport biology and is directly connected to FRAS1. It is annotated for nuclear-pore assembly, nuclear import, messenger RNA export, nuclear-envelope organization, and SMAD signal regulation. It has disease associations involving nephrotic syndrome and viral infection and a substantial literature base. Its inclusion broadens the module beyond metabolism and matrix biology to nuclear transport and epithelial-relevant nuclear function.
- **Conclusion**: Established evidence supports NUP93 as a nuclear-pore component with roles in nucleocytoplasmic transport. Its module association may reflect coordinated nuclear and epithelial-state changes, but there is no evidence here for a direct physical or regulatory relationship with FRAS1.

#### GALNT2

- **Related proteins** (co-abundance neighbors): FRAS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polypeptide N-acetylgalactosaminyltransferase 2. This gene encodes a member of the glycosyltransferase 2 protein family. Members of this family initiate mucin-type O-glycoslation of peptides in the Golgi apparatus. The encoded protein may be involved in O-linked glycosylation of the immunoglobulin A1 hinge region. This gene may influence triglyceride levels, and may be involved Type 2 diabetes, as well as several types of cancer. Alternative spl…
- **Diseases (Open Targets)**: congenital disorder of glycosylation, type iit (0.777); metabolic syndrome (0.546); familial lipoprotein lipase deficiency (0.486); alcohol drinking (0.450); familial hyperlipidemia (0.444)
- **Europe PMC papers**: 1178
- **Why important**: GALNT2 represents Golgi protein maturation and mucin-type O-linked glycosylation and is directly connected to FRAS1. It is cell-type enhanced in microglia and pancreatic acinar cells, detected in breast, and associated with glycosylation disorders, metabolic syndrome, lipoprotein biology, and cancer-related annotations. Its literature volume is substantial. Because extracellular-matrix and epithelial proteins are often influenced by glycosylation, GALNT2 provides a biologically plausible interface between cellular processing and FRAS1-associated tissue structure, although this connection is not demonstrated in the module data.
- **Conclusion**: Established evidence supports GALNT2 as a Golgi glycosyltransferase involved in protein maturation and mucin-type O-glycosylation. Its relationship to FRAS1 in this module is a mechanistic hypothesis rather than an established interaction, and the absence of STRING or hu.MAP support argues for caution.

## Module 14

**Tissue pair**: autonomic_nervous_system and breast  
**Genes (5)**: CRELD1, PRKAR2B, SDC2, PPAN, ZC3HAV1L

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established pathway-level function from enrichment analysis. STRING functional enrichment was also absent. The gene set instead suggests a mixed biology: SDC2 is associated with cell adhesion, extracellular matrix interaction, cytoskeletal organization, migration, and synaptic or dendritic processes; PRKAR2B represents cAMP-dependent protein kinase regulation and intracellular signaling; PPAN is associated with RNA processing, ribosomal RNA maturation, cell growth, and proliferation; and CRELD1 has cell-adhesion features and developmental associations. ZC3HAV1L contributes little specific functional annotation. Taken together, the most defensible interpretation is a cell-state or cell-composition-associated module linking membrane or adhesion biology with intracellular signaling and RNA or growth-related processes, rather than a demonstrated coherent biochemical pathway.

**Cell composition.**  This is not predominantly a plasma or secreted-protein module: the HPA summary identifies only one secreted gene, while the individual annotations mainly describe intracellular, cytosolic, Golgi, centrosomal, or plasma-membrane localization. Most genes have low tissue specificity, although tissue enhancement is seen in adipose tissue, liver, and thyroid gland. Cell-type enrichment is prominent across neural or glial populations, adipocytes, adrenal medulla cells, gonadotrophs, breast lactating cells, stromal cells, and hepatocytes. Immune-cell enrichment is present for ZC3HAV1L in basophils and SDC2 in neutrophils, whereas PRKAR2B is not detected in immune cells. These observations make shared cell types, stromal or neural components, or sample-composition effects plausible contributors to the conserved co-abundance pattern. Breast protein detection supports expression of most members in breast, but there is no matching HPA tissue for autonomic nervous system, limiting direct protein-level comparison.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

 None of the possible within-module gene pairs reaches the stated high-confidence interaction threshold, and there is no STRING functional enrichment. No complex contains at least two module members. Thus the co-abundance edges are not corroborated here as known physical interactions or membership in a recognized multiprotein complex. The module may reflect coordinated expression, shared cellular origin, or indirect regulation rather than a physically assembled molecular machine.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The tissue-pair co-abundance observation may be a new association, but the fact sheet does not establish a new molecular mechanism. Its novelty is weakened by the lack of globally significant GO or KEGG enrichment, lack of STRING enrichment, absence of high-confidence STRING links, and absence of a shared hu.MAP complex. The absence of these external records does not prove novelty; it may instead reflect limited knowledge, context dependence, weak physical coupling, or cell-composition effects. The appropriate claim is therefore a candidate conserved co-abundance pattern requiring independent replication and cell-type-aware validation.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance across a mixed neural, stromal, epithelial, or metabolic cell context rather than a single canonical pathway. In this model, SDC2-dependent adhesion and matrix or membrane signaling could be coupled to PRKAR2B-mediated cAMP signaling, while PPAN supports the RNA-processing and growth state of the contributing cells. CRELD1 may mark a related adhesion or developmental state, and ZC3HAV1L may be a context-dependent cytosolic component connecting the observed cellular state to SDC2 and CRELD1. This is a hypothesis, not an experimentally demonstrated mechanism.

### Important genes

#### SDC2

- **Related proteins** (co-abundance neighbors): ZC3HAV1L (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syndecan 2. The protein encoded by this gene is a transmembrane (type I) heparan sulfate proteoglycan and is a member of the syndecan proteoglycan family. The syndecans mediate cell binding, cell signaling, and cytoskeletal organization and syndecan receptors are required for internalization of the HIV-1 tat protein. The syndecan-2 protein functions as an integral membrane protein and participates in cell pro…
- **Diseases (Open Targets)**: COVID-19 (0.542); neurodegenerative disease (0.504); dengue disease (0.462); Abnormality of the skeletal system (0.415); glomerulonephritis (0.338)
- **Europe PMC papers**: 2321
- **Why important**:  SDC2 is connected to ZC3HAV1L and is the module member with the clearest membrane and cell-interaction role. Its syndecan function links cell binding, signaling, cytoskeletal organization, migration, and cell-matrix interactions, with additional annotations involving dendrite morphogenesis and synapse assembly. It is tissue-enhanced in liver and thyroid and enriched in several stromal, epithelial, endocrine, and hepatocyte-related cell types, with immune enrichment in neutrophils. It also has the largest literature volume among the selected genes, making it the best-established biological anchor.
- **Conclusion**: Established evidence supports SDC2 as a membrane proteoglycan involved in adhesion and signaling and as a plausible marker of cellular composition. It is not established that SDC2 drives the shared autonomic-nervous-system and breast module. Its proposed role as an upstream organizer of the module remains a hypothesis.

#### PRKAR2B

- **Related proteins** (co-abundance neighbors): PPAN (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus, Centrosome, Basal body, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase cAMP-dependent type II regulatory subunit beta. cAMP is a signaling molecule important for a variety of cellular functions. cAMP exerts its effects by activating the cAMP-dependent protein kinase, which transduces the signal through phosphorylation of different target proteins. The inactive kinase holoenzyme is a tetramer composed of two regulatory and two catalytic subunits. cAMP causes the dissociation of the inactive holoenzyme into a dimer …
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.372); trauma complication (0.275); cataract (0.275); spinal cord injury (0.263); esophageal ulcer (0.243)
- **Europe PMC papers**: 1375
- **Why important**:  PRKAR2B is a terminal module member connected to PPAN, so it may represent a signaling arm rather than a network hub. It encodes a regulatory subunit of protein kinase A and is linked to cAMP signaling, chemical synaptic transmission, intracellular signal transduction, and inflammatory-response regulation. It is tissue-enhanced in adipose tissue and enriched in adipocytes and several progenitor populations, while not being detected in immune cells. Its substantial literature base and direct connection to cAMP signaling make it important for interpreting the module's physiological state.
- **Conclusion**: Established evidence supports PRKAR2B as a regulator of cAMP-dependent protein kinase signaling with relevance to neural, metabolic, and progenitor-cell contexts. Its co-abundance with PPAN does not establish a direct interaction or prove that cAMP signaling explains the entire module.

#### PPAN

- **Related proteins** (co-abundance neighbors): CRELD1 (0.91), PRKAR2B (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peter pan homolog. The protein encoded by this gene is an evolutionarily conserved protein similar to yeast SSF1 as well as to the gene product of the Drosophila gene peter pan (ppan). SSF1 is known to be involved in the second step of mRNA splicing. Both SSF1 and ppan are essential for cell growth and proliferation. Exogenous expression of this gene was reported to reduce the anchorage-independent growth of some tu…
- **Diseases (Open Targets)**: Parkinson disease (0.462); Alzheimer disease (0.462); neurodegenerative disease (0.462); lysosomal storage disease (0.462); narcolepsy-cataplexy syndrome (0.435)
- **Europe PMC papers**: 417
- **Why important**:  PPAN occupies an internal bridging position between CRELD1 and PRKAR2B. It is an evolutionarily conserved protein associated with RNA processing, ribosomal RNA maturation, cell growth, and proliferation. It has low tissue specificity and a broad neural or glial group annotation, with detection in breast. Its literature volume is substantial, and its biology offers a plausible explanation for coordinated abundance during changes in cellular growth or biosynthetic state.
- **Conclusion**: Established evidence supports PPAN as a conserved RNA-processing and growth-related factor. It may mark the biosynthetic state of cells contributing to the module, but there is no evidence here that PPAN physically links the other proteins or causes the observed co-abundance.

#### CRELD1

- **Related proteins** (co-abundance neighbors): PPAN (0.91), ZC3HAV1L (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CRELD disulfide isomerase 1. This gene encodes a member of a subfamily of epidermal growth factor-related proteins. The encoded protein is characterized by a cysteine-rich with epidermal growth factor-like domain. This protein may function as a cell adhesion molecule. Mutations in this gene are the cause of atrioventricular septal defect. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Apr 2010…
- **Diseases (Open Targets)**: Jeffries-Lakhani neurodevelopmental syndrome (0.714); hereditary disease (0.486); ventricular septal defect 1 (0.416); congenital heart defects, multiple types, 4 (0.416); neurodevelopmental disorder with hypotonia and seizures (0.185)
- **Europe PMC papers**: 418
- **Why important**:  CRELD1 is an internal connector linked to PPAN and ZC3HAV1L and has the strongest weighted network position in the module. It encodes a cysteine-rich, epidermal-growth-factor-related protein proposed to function in cell adhesion and is associated with endocardial cushion and cardiac septum development. Disease associations include congenital heart defects and a neurodevelopmental syndrome. It has low tissue specificity, neural or glial cell-type enhancement, intracellular and membrane localization, and detection in breast. Its literature volume is substantial.
- **Conclusion**: Established evidence supports CRELD1 as a developmentally relevant adhesion-associated protein with cardiac and neurodevelopmental disease associations. Its network position makes it a useful candidate marker of the module, but the module does not demonstrate that CRELD1 mediates the shared tissue association.

#### ZC3HAV1L

- **Related proteins** (co-abundance neighbors): SDC2 (0.87), CRELD1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ZC3HAV1 like. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: stroke disorder (0.188); alcohol drinking (0.188); primary biliary cholangitis (0.134); preeclampsia (0.063); hypothyroidism (0.027)
- **Europe PMC papers**: 130
- **Why important**:  ZC3HAV1L links SDC2 with CRELD1 and therefore occupies a topological bridging position despite having limited functional annotation. The available record describes it as a cytosolic ZC3HAV1-like protein, without a defined pathway assignment. It is enriched in adipocytes, adrenal medulla cells, and gonadotrophs and is immune-cell enriched in basophils. Its comparatively small literature base makes it an especially informative candidate for follow-up if the module replicates.
- **Conclusion**: Established evidence is limited to its cytosolic annotation, disease or trait associations, and cell-type expression pattern. Its bridging position suggests a possible context-dependent role, but any mechanistic function in this module remains speculative and should not be inferred from co-abundance alone.

## Module 15

**Tissue pair**: autonomic_nervous_system and breast  
**Genes (6)**: DDX55, LONRF2, MEN1, PSMD9, CRABP1, TMEM87B

### Function

The module is best interpreted as a heterogeneous intracellular regulatory co-abundance module rather than a coherently established pathway. Its topology is centered on LONRF2, which co-abunds with CRABP1, PSMD9, MEN1, TMEM87B, and DDX55. The member annotations span protein quality control, retinoic-acid binding and differentiation, proteasome regulation, chromatin and transcriptional control, endosome-to-Golgi trafficking, and RNA or ribosome-related processes. This combination suggests a possible relationship between proteostasis, nuclear regulation, intracellular trafficking, and cell-state maintenance, but the evidence does not establish a single biological process. No GO or KEGG term passed global correction, and there was no supplementary STRING functional enrichment. Therefore, the proposed function is an informed interpretation of the gene annotations and topology, not a statistically confirmed pathway assignment.

**Cell composition.** The module does not have the profile of a plasma or secreted-protein module: none of the genes is annotated as secreted. It also does not appear to be driven by blood-cell contamination, because the HPA evidence shows low immune-cell specificity or absence from immune cells and no recurring enriched blood-cell population. Most genes have low tissue specificity, while a smaller subset shows tissue or cell-type enhancement in diverse contexts including retina, thyroid gland, adrenal cortex, inhibitory neurons, gonadotrophs, late spermatids, and Müller glia. All module proteins were detected in breast, whereas there was no matching HPA tissue assessment for autonomic nervous system. The mixed, largely intracellular composition is compatible with broadly distributed cellular machinery or shared cell-state biology rather than a tissue-exclusive secretory or immune signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was observed among the module members, and STRING provided no supplementary functional enrichment. No hu.MAP complex contained multiple module members. Thus, the co-abundance relationships are not corroborated by the supplied curated physical-interaction or complex resources. This does not disprove biological coordination: co-abundance can arise from shared regulation, cell composition, protein turnover, or indirect pathway relationships. However, the lack of known pairwise and complex support means that the network should not be described as a documented physical complex. The strongest network-centered role belongs to LONRF2, while the other genes are peripheral co-abundance partners in the supplied graph.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously uncharacterized co-abundance pattern, because its member relationships have no high-confidence STRING support, no multi-member hu.MAP complex support, and no globally significant GO or KEGG enrichment. The combination of LONRF2 with CRABP1, PSMD9, MEN1, TMEM87B, and DDX55 is therefore not presented here as an already established molecular module. Nevertheless, absence from STRING or hu.MAP alone cannot establish novelty: these resources emphasize curated or experimentally supported relationships and may miss indirect regulation, context-dependent interactions, and correlations caused by shared cell states. A novelty claim requires replication in independent autonomic nervous system and breast datasets, preservation of the co-abundance pattern after cell-composition adjustment, and experimental or orthogonal evidence for coordinated regulation.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular cell-state program in autonomic nervous system and breast tissues in which LONRF2-associated protein quality control is co-regulated with retinoic-acid-responsive differentiation, proteasome activity, chromatin regulation, vesicle trafficking, and RNA-processing machinery. LONRF2 may act as a network marker rather than a proven physical coordinator. CRABP1 could mark retinoic-acid-dependent differentiation state, PSMD9 could represent proteasome or protein-homeostasis demand, MEN1 could connect the state to chromatin regulation, and TMEM87B or DDX55 could reflect trafficking or RNA-processing requirements. This is a mechanistic model generated from annotations and co-abundance, not an established causal pathway; direct interactions, regulatory direction, and tissue-specific mechanism remain untested.

### Important genes

#### LONRF2

- **Related proteins** (co-abundance neighbors): CRABP1 (0.89), PSMD9 (0.88), MEN1 (0.84), TMEM87B (0.81), DDX55 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LON peptidase N-terminal domain and ring finger 2. Predicted to enable metal ion binding activity. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: rheumatoid arthritis (0.314); B-cell acute lymphoblastic leukemia (0.287); intelligence (0.216); osteoarthritis (0.206); mathematical ability (0.162)
- **Europe PMC papers**: 185
- **Why important**: LONRF2 is the central network gene, connected to every other member in the supplied subgraph and having the greatest weighted network prominence. Its annotation supports a role in protein quality control and neuronal processes, while HPA places it in the nucleoplasm and shows enhancement in several endocrine, neural, and reproductive cell contexts. Its disease and trait associations include inflammatory, skeletal, hematologic, cognitive, and neurological themes, but these associations are not evidence that it drives this module. Its literature volume is more limited than that of MEN1 or CRABP1, making it especially important for testing whether the module represents a genuinely underexplored biology.
- **Conclusion**: Established evidence supports LONRF2 as the network hub and as a protein-quality-control-related gene. It is a leading marker of the module, but there is no evidence here that it physically binds the other members or causally organizes their co-abundance. Its proposed coordinating role is a hypothesis.

#### CRABP1

- **Related proteins** (co-abundance neighbors): LONRF2 (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cellular retinoic acid binding protein 1. This gene encodes a specific binding protein for a vitamin A family member and is thought to play an important role in retinoic acid-mediated differentiation and proliferation processes. It is structurally similar to the cellular retinol-binding proteins, but binds only retinoic acid at specific sites within the nucleus, which may contribute to vitamin A-directed differentiation in epithelial tiss…
- **Diseases (Open Targets)**: neurodegenerative disease (0.272); alcohol drinking (0.260); urolithiasis (0.260); rheumatic disorder (0.081); neuroblastoma (0.080)
- **Europe PMC papers**: 1980
- **Why important**: CRABP1 is the most direct peripheral link to retinoic-acid biology and epithelial differentiation. It is tissue enhanced in retina and thyroid gland and cell enriched in Müller glia, which gives it a distinctive cell-state context relative to the broadly distributed intracellular genes. It has a substantial literature and associations with neurodegenerative disease, neuroblastoma, and other disorders, making it a biologically interpretable anchor for a differentiation or signaling component of the module. Its only supplied network connection is to LONRF2.
- **Conclusion**: Established evidence supports CRABP1 as a retinoic-acid-binding differentiation-related gene with relevant neural and epithelial contexts. Its role in this shared module is not established beyond co-abundance with LONRF2. A retinoic-acid-dependent explanation is a plausible hypothesis requiring independent validation.

#### MEN1

- **Related proteins** (co-abundance neighbors): LONRF2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: menin 1. This gene encodes menin, a tumor suppressor associated with a syndrome known as multiple endocrine neoplasia type 1. Menin is a scaffold protein that functions in histone modification and epigenetic gene regulation. It is thought to regulate several pathways and processes by altering chromatin structure through the modification of histones. [provided by RefSeq, May 2019].
- **Diseases (Open Targets)**: multiple endocrine neoplasia type 1 (0.866); parathyroid gland adenoma (0.675); endocrine gland neoplasm (0.663); multiple endocrine neoplasia (0.661); Angiofibroma (0.642)
- **Europe PMC papers**: 7686
- **Why important**: MEN1 encodes menin, a tumor suppressor and chromatin or transcriptional scaffold with established roles in DNA repair and transcriptional regulation. It is nucleoplasmic, detected in breast, and shows enhancement in megakaryocytes rather than a tissue-restricted secretory pattern. MEN1 has the strongest disease and literature context among the selected genes, particularly for endocrine neoplasia and tumor biology. Its position as a peripheral partner of LONRF2 means it may report a shared regulatory cell state rather than a direct interaction.
- **Conclusion**: Established evidence supports MEN1 as a chromatin-regulatory tumor-suppressor gene with endocrine disease relevance. The module does not demonstrate that MEN1 controls LONRF2 or the other members. Its inclusion supports a possible transcriptional or cell-state component, which remains a hypothesis.

#### PSMD9

- **Related proteins** (co-abundance neighbors): LONRF2 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 9. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.075); glioblastoma (0.074); neoplasm (0.051); refractive error (0.050); Alzheimer disease (0.046)
- **Europe PMC papers**: 456
- **Why important**: PSMD9 is a proteasome regulatory-particle component and therefore provides a concrete link to protein turnover and cellular quality control. It is cytosolic, has low tissue and immune-cell specificity, and is detected in breast. Its annotations include ubiquitin-dependent protein catabolism, protein folding, proteasome assembly, and transcriptional regulation, making it a useful functional bridge to the proposed proteostasis interpretation. It is a peripheral partner of LONRF2 and has less disease and literature prominence than MEN1 or CRABP1.
- **Conclusion**: Established evidence supports PSMD9 as a broadly distributed proteasome-associated gene. Its co-abundance with LONRF2 is consistent with shared protein-homeostasis demand, but does not prove a direct proteasome mechanism for the module. The proteostasis interpretation is plausible but requires perturbation or replication evidence.
