# Conserved co-abundance modules: autonomic_nervous_system and testis

## Module 0

**Tissue pair**: autonomic_nervous_system and testis  
**Genes (31)**: GOT1, ALG5, CCAR1, CCDC6, CCS, CORO1C, DDX6, DIAPH2, ECHS1, ECI1, ELMOD2, GNA11, GNAI3, KIF5C, MEMO1, MESD, MSH2, PPP1R12A, PARVA, SKIC2, SKIC3, SRSF5, SUCLA2, ACAA1, THOP1, TIMM50, TMEM70, UMPS, UNC45A, ATP6V1C1, TJP2

### Function

No GO/KEGG term passed global correction, so the module does not support a formally significant pathway assignment from enrichment alone. Its gene-level evidence instead points to a mixed cellular program combining mitochondrial and peroxisomal energy metabolism, RNA quality control, intracellular trafficking, cytoskeletal organization, junctional biology, and signal transduction. The clearest biochemical core is lipid and mitochondrial metabolism: ACAA1 is a peroxisomal beta-oxidation enzyme, while ECHS1 and ECI1 are mitochondrial fatty-acid oxidation enzymes and SUCLA2 supports the tricarboxylic-acid cycle. GOT1 adds amino-acid and intermediary metabolism, and TIMM50 and TMEM70 support mitochondrial protein import and ATP-synthase biogenesis. A second layer involves RNA surveillance and turnover through SKIC2, SKIC3, DDX6, and SRSF5. A third layer involves signaling and cell architecture through GNA11, GNAI3, TJP2, DIAPH2, PARVA, and PPP1R12A. Thus, the most defensible interpretation is a shared cellular maintenance and energetic-demand module rather than a narrowly defined autonomic-neural or testis-specific pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only one secreted gene, and the listed proteins are overwhelmingly intracellular, mitochondrial, peroxisomal, nuclear, cytoskeletal, or membrane-associated. It is also not strongly blood-cell enriched. Most genes have low immune-cell specificity, although isolated immune-cell annotations occur for genes such as GNA11, TJP2, DIAPH2, ATP6V1C1, and PPP1R12A. Most genes have low tissue specificity, with selected enrichment in skeletal muscle, tongue, liver, heart muscle, brain, kidney, and testis-related cell populations. The recurrent HPA annotations for spermatids, Sertoli cells, and other testicular cell types are compatible with a genuine testis component, but the broad tissue distribution argues against a testis-exclusive program. Protein detection in testis is widespread among the module genes, whereas the autonomic-nervous-system comparison lacks a matching HPA tissue measurement. The module could therefore reflect a broadly expressed metabolic and cellular-maintenance program that becomes prominent in both tissues, with possible contributions from shared metabolically active or structurally specialized cell types rather than blood contamination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a compact, biologically coherent metabolic subnetwork. ACAA1 has high-confidence links to ECHS1, ECI1, and SUCLA2, while ECHS1 also links to ECI1. These relationships connect peroxisomal fatty-acid processing with mitochondrial fatty-acid oxidation and central metabolism. STRING provides no functional-enrichment result for the full module, so the metabolic interpretation should not be presented as a globally significant STRING enrichment claim. hu.MAP independently supports several partial complex or machinery relationships. ECHS1 and ECI1 co-occur in the high-confidence complex (hu.MAP huMAP3_12099.1). SKIC2 and SKIC3 repeatedly occur together across RNA surveillance and RNA-processing complexes (hu.MAP huMAP3_09415.1), (hu.MAP huMAP3_06383.1), (hu.MAP huMAP3_07717.1), (hu.MAP huMAP3_09525.1), (hu.MAP huMAP3_11037.1), (hu.MAP huMAP3_12301.1), (hu.MAP huMAP3_12727.1). TIMM50 and UNC45A co-occur in mitochondrial or protein-homeostasis complexes (hu.MAP huMAP3_08568.1), (hu.MAP huMAP3_09247.1), while GNAI3 and GNA11 co-occur in G-protein-associated complexes (hu.MAP huMAP3_13105.1), (hu.MAP huMAP3_11173.1). UMPS and UNC45A share a broader complex assignment (hu.MAP huMAP3_09042.1). Because most hu.MAP entries contain only a subset of their members in this module, the data support convergence of several known cellular machineries rather than one established multiprotein complex containing the entire module.

**STRING interactions (score >= 0.7)**: 4 of 465 gene pairs: ACAA1–ECHS1 (0.977); ACAA1–ECI1 (0.825); ACAA1–SUCLA2 (0.86); ECHS1–ECI1 (0.855)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12099.1 (ECHS1, ECI1; 2/2); huMAP3_09415.1 (SKIC2, SKIC3; 2/4); huMAP3_06383.1 (SKIC2, SKIC3; 2/5); huMAP3_07717.1 (SKIC2, SKIC3; 2/7); huMAP3_09525.1 (SKIC2, SKIC3; 2/7); huMAP3_08568.1 (TIMM50, UNC45A; 2/7); huMAP3_09247.1 (TIMM50, UNC45A; 2/9); huMAP3_11037.1 (SKIC2, SKIC3; 2/14); huMAP3_12301.1 (SKIC2, SKIC3; 2/26); huMAP3_09042.1 (UMPS, UNC45A; 2/26); huMAP3_13105.1 (GNAI3, GNA11; 2/27); huMAP3_12727.1 (SKIC2, SKIC3; 2/32); huMAP3_11173.1 (GNAI3, GNA11; 2/34)

### Novelty

The exact conserved co-abundance module appears potentially novel as a tissue-shared network observation, because the supplied resources document biochemical interactions and partial complexes but do not identify this precise set of genes as one established autonomic-nervous-system and testis module. However, the functional components themselves are not novel: the metabolic relationships among ACAA1, ECHS1, ECI1, and SUCLA2 are already supported by STRING, and several RNA-processing and G-protein relationships are represented in hu.MAP. Therefore, the defensible claim is novelty of the cross-tissue co-abundance organization or its integration, not discovery of previously unknown molecular functions or physical interactions. Absence of the full module from STRING or hu.MAP cannot by itself establish novelty, and the lack of globally significant GO/KEGG enrichment means that novelty cannot be justified by a distinctive enrichment signature. Independent replication, comparison with published tissue co-expression modules, and experimental testing would be required before calling the module a new biological mechanism.

**Hypothesis.** Hypothesis: this module represents a coordinated cellular-maintenance state required in both autonomic nervous system tissue and testis, in which high energetic demand couples fatty-acid oxidation and mitochondrial function to RNA surveillance, intracellular transport, cytoskeletal remodeling, and receptor-linked signaling. The metabolic arm could provide energy and metabolic intermediates; SKIC2, SKIC3, and DDX6 could maintain transcript quality and translation control; GNA11 and GNAI3 could transmit extracellular signals; and TJP2, DIAPH2, PARVA, and PPP1R12A could connect signaling to cell architecture. In testis, the spermatid and mitochondrial annotations make this model particularly plausible for metabolically active differentiating germ cells. In autonomic nervous system tissue, the same program could support vesicle handling, cytoskeletal transport, signaling, and neuronal or glial maintenance. This remains a mechanistic hypothesis: co-abundance does not demonstrate physical interaction, causal regulation, or identical cell-type composition across the two tissues.

### Important genes

#### ACAA1

- **Related proteins** (co-abundance neighbors): SRSF5 (0.90), GNAI3 (0.87), SKIC2 (0.86), GNA11 (0.85), ALG5 (0.81); STRING partners: ECHS1 (0.977), ECI1 (0.825), SUCLA2 (0.86)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Peroxisomes; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA acyltransferase 1. This gene encodes an enzyme operative in the beta-oxidation system of the peroxisomes. Deficiency of this enzyme leads to pseudo-Zellweger syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: hyperpituitarism (0.348); Follicular Cyst (0.127); Sepsis (0.103); neoplasm (0.098); Alzheimer disease (0.082)
- **Europe PMC papers**: 1153
- **Why important**: ACAA1 is a high-connectivity module member and the strongest STRING bridge within the metabolic portion of the network. It is a peroxisomal beta-oxidation enzyme and connects in STRING to ECHS1, ECI1, and SUCLA2. Its HPA profile is enriched in kidney and liver-related tissue contexts and in digestive epithelial and hepatocyte populations, while it is detected in testis. Its substantial literature and disease annotations provide stronger prior biological support than for many of the less characterized module members.
- **Conclusion**: Established evidence supports ACAA1 as a metabolic anchor linking peroxisomal lipid processing to the mitochondrial enzymes in this module. It is plausible, but not proven, that ACAA1 helps explain why the module is shared by tissues with substantial energetic and lipid-metabolic requirements.

#### ECHS1

- **Related proteins** (co-abundance neighbors): MEMO1 (0.88), ELMOD2 (0.84); STRING partners: ACAA1 (0.977), ECI1 (0.855)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_12099.1
- **Function (MyGene.info)**: enoyl-CoA hydratase, short chain 1. The protein encoded by this gene functions in the second step of the mitochondrial fatty acid beta-oxidation pathway. It catalyzes the hydration of 2-trans-enoyl-coenzyme A (CoA) intermediates to L-3-hydroxyacyl-CoAs. The gene product is a member of the hydratase/isomerase superfamily. It localizes to the mitochondrial matrix. Transcript variants utilizing alternative transcription initiation site…
- **Diseases (Open Targets)**: mitochondrial short-chain Enoyl-Coa hydratase 1 deficiency (0.848); Leigh syndrome (0.759); hereditary disease (0.509); neurodegenerative disease (0.371); colorectal carcinoma (0.095)
- **Europe PMC papers**: 1714
- **Why important**: ECHS1 is part of the compact high-confidence STRING metabolic cluster with ACAA1 and ECI1 and is also present with ECI1 in hu.MAP complex (hu.MAP huMAP3_12099.1). It catalyzes a step in mitochondrial fatty-acid and branched-chain amino-acid catabolism. Its liver-enhanced HPA profile and testis protein detection are consistent with a metabolic role in the shared module. Its established mitochondrial disease associations make it biologically informative for interpreting the module.
- **Conclusion**: Established evidence identifies ECHS1 as a mitochondrial metabolic component and a known interaction partner of other module enzymes. The module data support coordinated abundance with the peroxisomal and mitochondrial metabolic arm, but do not establish that ECHS1 controls the module or that its disease biology is responsible for the tissue-sharing pattern.

#### SUCLA2

- **Related proteins** (co-abundance neighbors): CCDC6 (0.91), ECI1 (0.90), CCAR1 (0.89), TIMM50 (0.88), GOT1 (0.83); STRING partners: ACAA1 (0.86)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase ADP-forming subunit beta. Succinyl-CoA synthetase (SCS) is a mitochondrial matrix enzyme that acts as a heterodimer, being composed of an invariant alpha subunit and a substrate-specific beta subunit. The protein encoded by this gene is an ATP-specific SCS beta subunit that dimerizes with the SCS alpha subunit to form SCS-A, an essential component of the tricarboxylic acid cycle. SCS-A hydrolyzes ATP to convert succinate t…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome, encephalomyopathic form with methylmalonic aciduria (0.816); mitochondrial DNA depletion syndrome, encephalomyopathic form (0.581); neurodegenerative disease (0.485); mitochondrial disease (0.374); disease of peritoneum (0.372)
- **Europe PMC papers**: 1440
- **Why important**: SUCLA2 has strong network connectivity to ECI1, TIMM50, GOT1, CCDC6, and CCAR1 and is linked by STRING to ACAA1. It is an ATP-forming succinyl-CoA synthetase subunit in the mitochondrial tricarboxylic-acid cycle. Its tissue-enhanced profile in skeletal muscle and tongue, cell-type enhancement in early and late spermatids, mitochondrial localization, and association with mitochondrial DNA depletion syndrome make it a strong candidate for the energetic core.
- **Conclusion**: Established evidence supports SUCLA2 as a mitochondrial energy-metabolism anchor with direct relevance to testicular germ-cell biology and muscle-like energetic states. A coordinated SUCLA2-centered metabolic program is a reasonable hypothesis, but co-abundance alone cannot show that SUCLA2 is rate-limiting or causally upstream.

#### GNA11

- **Related proteins** (co-abundance neighbors): DIAPH2 (0.88), MEMO1 (0.88), SKIC2 (0.87), TJP2 (0.85), ACAA1 (0.85), GNAI3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_13105.1, huMAP3_11173.1
- **Function (MyGene.info)**: G protein subunit alpha 11. The protein encoded by this gene belongs to the family of guanine nucleotide-binding proteins (G proteins), which function as modulators or transducers in various transmembrane signaling systems. G proteins are composed of 3 units: alpha, beta and gamma. This gene encodes one of the alpha subunits (subunit alpha-11). Mutations in this gene have been associated with hypocalciuric hypercalcemia type…
- **Diseases (Open Targets)**: familial hypoparathyroidism (0.754); familial hypocalciuric hypercalcemia 2 (0.736); autosomal dominant hypocalcemia (0.611); congenital hemangioma (0.494); uveal melanoma (0.469)
- **Europe PMC papers**: 4418
- **Why important**: GNA11 is among the more highly connected module genes and links to DIAPH2, MEMO1, SKIC2, TJP2, ACAA1, and GNAI3. It encodes a G-protein alpha subunit involved in transmembrane signal transduction and is represented with GNAI3 in hu.MAP complexes (hu.MAP huMAP3_13105.1) and (hu.MAP huMAP3_11173.1). Its established associations with calcium-related disorders and its detection in testis give it disease and tissue relevance. Its network position connects signaling to metabolic, RNA-processing, and junctional portions of the module.
- **Conclusion**: Established evidence supports GNA11 as a signaling integrator and a known component of G-protein-associated machinery. It may couple extracellular cues to the metabolic and structural state represented by the module, but that coupling is a hypothesis rather than a demonstrated mechanism in these tissues.

#### SKIC2

- **Related proteins** (co-abundance neighbors): GNA11 (0.87), TJP2 (0.86), ACAA1 (0.86), DIAPH2 (0.84), SKIC3 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_09415.1, huMAP3_06383.1, huMAP3_07717.1, huMAP3_09525.1, huMAP3_11037.1, huMAP3_12301.1, huMAP3_12727.1
- **Function (MyGene.info)**: SKI2 subunit of superkiller complex. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: trichohepatoenteric syndrome (0.745); immunodeficiency 57 (0.340); hereditary disease (0.195); African iron overload (0.059); maple syrup urine disease (0.058)
- **Europe PMC papers**: 360
- **Why important**: SKIC2 is a highly connected module member and repeatedly occurs with SKIC3 across hu.MAP RNA-processing and RNA-surveillance complexes (hu.MAP huMAP3_09415.1), (hu.MAP huMAP3_06383.1), (hu.MAP huMAP3_07717.1), (hu.MAP huMAP3_09525.1), (hu.MAP huMAP3_11037.1), (hu.MAP huMAP3_12301.1), (hu.MAP huMAP3_12727.1). Its annotated functions include nuclear-transcribed mRNA decay, nonsense-mediated decay, non-stop decay, and rescue of stalled cytosolic ribosomes. Its nuclear localization, testis detection, spermatogenesis-relevant DEAD-box context, and disease associations make it a strong candidate for explaining how the module links metabolism to proteome and transcriptome maintenance.
- **Conclusion**: Established evidence supports SKIC2 as an RNA quality-control component embedded in several known complexes. Its co-abundance with mitochondrial and signaling genes suggests a possible coordinated response to energetic or translational stress, but the module does not establish direct biochemical coupling between RNA surveillance and fatty-acid oxidation.

## Module 1

**Tissue pair**: autonomic_nervous_system and testis  
**Genes (28)**: GOT2, ABCD3, ACTL6A, ATG7, COPG2, COQ9, CIAPIN1, CPSF2, QDPR, EIF3F, FUS, HACL2, HYOU1, EIF4A2, LMNB1, MBOAT7, MCCC1, OCIAD1, PAFAH1B3, PAK2, PRKDC, CAD, SF3B3, STOM, LARS1, UBA3, UGDH, USO1

### Function

No GO or KEGG term passed global correction, so there is no statistically established pathway annotation for this module. The gene content instead suggests a heterogeneous cellular-maintenance program combining protein synthesis and RNA handling, intracellular trafficking, lipid and amino-acid metabolism, mitochondrial and peroxisomal function, membrane organization, autophagy, and stress responses. The strongest internal structure is not a single pathway: CAD, COPG2, MBOAT7, and related genes connect metabolic and vesicle-trafficking functions, while EIF3F and EIF4A2 form a translation-initiation connection supported by STRING and hu.MAP (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1). Thus, the most defensible interpretation is a shared metabolic, proteostatic, and biosynthetic state rather than a discrete autonomic-nervous-system or testis-specific pathway. The absence of globally significant GO or KEGG enrichment does not invalidate the module, but it limits pathway-level claims.

**Cell composition.** The module is not dominated by plasma or secreted proteins: HPA identifies only a single secretome-associated gene, and the proteins are predominantly intracellular, including cytosolic, nuclear, mitochondrial, Golgi, vesicular, plasma-membrane, and peroxisomal locations. Most genes have low tissue specificity, which is consistent with broadly expressed housekeeping or general cell-maintenance functions rather than a tissue-exclusive program. HPA nevertheless shows recurring associations with neutrophils, oocytes, hepatocytes, and late spermatids, with additional tissue-enhanced signals in liver, skeletal muscle, adrenal gland, brain, and related tissues. Blood-cell specificity is generally low, although a subset has enrichment in granulocyte-related cell types. Protein detection in testis is widespread among the assayed genes, whereas there is no matching HPA protein-detection dataset for autonomic nervous system. The shared signal could therefore reflect common cellular states, germ-cell or somatic-cell composition, or sample-related cell mixtures rather than a conserved function unique to both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports only a small set of high-confidence pairwise relationships within the module: ATG7 with UBA3, CAD with GOT2, and EIF3F with EIF4A2. These links provide focused support for autophagy or ubiquitin-like modification, intermediary metabolism, and translation initiation, respectively, but they do not establish one connected biochemical pathway. hu.MAP independently places EIF3F and EIF4A2 together in two translation-related complexes (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1). It also places STOM and MBOAT7 together in two larger membrane, organelle, and lipid-associated complexes (hu.MAP huMAP3_09822.1) (hu.MAP huMAP3_10725.1). Because the latter complexes contain many additional proteins and only a small subset is represented in this module, they support compatibility with those cellular systems rather than a complete complex being captured. The sparse STRING connectivity and partial hu.MAP overlap indicate that some relationships are already known, while much of the co-abundance structure is not explained by established physical interactions.

**STRING interactions (score >= 0.7)**: 3 of 378 gene pairs: ATG7–UBA3 (0.826); CAD–GOT2 (0.931); EIF3F–EIF4A2 (0.838)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13175.1 (EIF3F, EIF4A2; 2/20); huMAP3_11246.1 (EIF3F, EIF4A2; 2/24); huMAP3_09822.1 (STOM, MBOAT7; 2/28); huMAP3_10725.1 (STOM, MBOAT7; 2/59)

### Novelty

This may be a new co-abundance observation, but the fact sheet does not justify calling it a newly discovered biological mechanism. The module has no globally significant GO or KEGG enrichment, no supplementary STRING enrichment, sparse known STRING connectivity, and only partial representation of broad hu.MAP complexes. Those features make the shared co-abundance pattern potentially novel as a tissue-pair association, while also making biological interpretation uncertain. Absence from STRING or hu.MAP cannot prove novelty, because co-abundance can arise from shared regulation, cell composition, transient interactions, or coordinated physiology without a documented physical interaction. A genuine novelty claim would require comparison with prior tissue co-expression or proteomic-module studies and independent replication in additional cohorts.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular resource-management state present in both tissues, in which translation, RNA processing, membrane and vesicle traffic, lipid remodeling, mitochondrial or peroxisomal metabolism, and protein-quality control are coordinated. In testis, this state could be associated with metabolically active germ cells and spermatid development; in autonomic nervous system samples, it could reflect metabolically demanding neural or supporting cells. The recurring HPA associations with germ-cell, neuronal, hepatic, muscle, and granulocyte-related populations also raise the alternative possibility that the shared module is partly driven by common cell-state or sample-composition effects. This hypothesis should be tested by cell-type-resolved data, independent cohorts, perturbation of the proposed metabolic and proteostatic nodes, and examination of whether the module persists after controlling for cell composition.

### Important genes

#### CAD

- **Related proteins** (co-abundance neighbors): LMNB1 (0.83), COPG2 (0.82), CIAPIN1 (0.81), STOM (0.81), CPSF2 (0.80); STRING partners: GOT2 (0.931)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carbamoyl-phosphate synthetase 2, aspartate transcarbamylase, and dihydroorotase. The de novo synthesis of pyrimidine nucleotides is required for mammalian cells to proliferate. This gene encodes a trifunctional protein which is associated with the enzymatic activities of the first 3 enzymes in the 6-step pathway of pyrimidine biosynthesis: carbamoylphosphate synthetase (CPS II), aspartate transcarbamoylase, and dihydroorotase. This protein is regulated by the mitogen-activated…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 50 (0.660); congenital disorder of glycosylation type I (0.595); infantile epileptic-dyskinetic encephalopathy (0.499); type 2 diabetes mellitus (0.286); urolithiasis (0.283)
- **Europe PMC papers**: 60667
- **Why important**: CAD is among the strongest network-connected genes in the module and links to LMNB1, COPG2, CIAPIN1, STOM, and CPSF2. Its established function combines the early steps of de novo pyrimidine synthesis, directly connecting nucleotide production with proliferative and biosynthetic demand. Its STRING relationship with GOT2 provides an independent metabolic connection. CAD also has extensive literature and disease associations involving developmental and epileptic encephalopathy and other disorders, making it a well-supported metabolic anchor.
- **Conclusion**: Established evidence supports CAD as a central biosynthetic node and a plausible marker of nucleotide demand. The module data do not establish that CAD drives the shared tissue program; its coordinated abundance may instead report general cellular growth, biosynthetic activity, or cell composition.

#### MBOAT7

- **Related proteins** (co-abundance neighbors): COPG2 (0.88), GOT2 (0.86), UBA3 (0.82), EIF4A2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_09822.1, huMAP3_10725.1
- **Function (MyGene.info)**: membrane bound acylglycerophosphatidylinositol O-acyltransferase MBOAT7. This gene encodes a member of the membrane-bound O-acyltransferases family of integral membrane proteins that have acyltransferase activity. The encoded protein is a lysophosphatidylinositol acyltransferase that has specificity for arachidonoyl-CoA as an acyl donor. This protein is involved in the reacylation of phospholipids as part of the phospholipid remodeling pathway known as the Land cycle. …
- **Diseases (Open Targets)**: intellectual disability, autosomal recessive 57 (0.754); hereditary disease (0.487); autosomal recessive non-syndromic intellectual disability (0.462); complex neurodevelopmental disorder (0.370); neurodegenerative disease (0.345)
- **Europe PMC papers**: 1344
- **Why important**: MBOAT7 has a prominent position in the module and connects to COPG2, GOT2, UBA3, and EIF4A2. It is an established lysophosphatidylinositol acyltransferase involved in phospholipid remodeling, including arachidonoyl-containing phospholipids. Its links to STOM in hu.MAP complexes (hu.MAP huMAP3_09822.1) (hu.MAP huMAP3_10725.1) provide support for a membrane and organelle context. MBOAT7 also has disease associations involving intellectual disability and neurodevelopmental disorders, relevant to the two tissues under study.
- **Conclusion**: Established evidence supports MBOAT7 as the strongest lipid-remodeling candidate in the module. A mechanistic role in coordinating membrane composition with translation or trafficking is plausible, but the co-abundance data alone do not demonstrate that such coordination occurs.

#### EIF3F

- **Related proteins** (co-abundance neighbors): ACTL6A (0.89), STOM (0.83); STRING partners: EIF4A2 (0.838)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_13175.1, huMAP3_11246.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit F. Enables deubiquitinase activity and identical protein binding activity. Contributes to translation initiation factor activity. Involved in IRES-dependent viral translational initiation; protein deubiquitination; and translational initiation. Located in membrane. Part of eukaryotic translation initiation factor 3 complex. Implicated in autosomal recessive non-syndromic intellectual disability. [pro…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal recessive 67 (0.675); hereditary disease (0.413); developmental disability (0.371); neurodegenerative disease (0.370); syndromic intellectual disability (0.370)
- **Europe PMC papers**: 997
- **Why important**: EIF3F connects to ACTL6A and STOM and forms the clearest translation-related module relationship through its STRING interaction with EIF4A2 and its shared membership in two hu.MAP complexes (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1). It is a component of the eukaryotic translation-initiation machinery and has disease associations involving intellectual disability and developmental disorders. Its HPA association with late spermatids makes it particularly relevant to the testis component.
- **Conclusion**: Established evidence supports EIF3F as a translation-initiation representative and a bridge between the module and known initiation complexes. Its abundance may indicate translational activity in germ cells or other active cell populations, but a specific autonomic-nervous-system role remains unproven.

#### EIF4A2

- **Related proteins** (co-abundance neighbors): COQ9 (0.84), MBOAT7 (0.81); STRING partners: EIF3F (0.838)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_13175.1, huMAP3_11246.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4A2. Enables ATP hydrolysis activity. Involved in negative regulation of RNA-directed 5'-3' RNA polymerase activity. Located in perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and speech delay, with or without seizures (0.744); neurodevelopmental disorder (0.565); hereditary disease (0.448); dengue disease (0.370); complex neurodevelopmental disorder (0.370)
- **Europe PMC papers**: 2227
- **Why important**: EIF4A2 is directly connected to EIF3F by STRING and is present with EIF3F in both hu.MAP complexes (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1). It is an RNA helicase and translation-initiation factor, providing a complementary component to EIF3F rather than an isolated annotation. It has substantial literature and disease associations involving neurodevelopmental disorders, which makes it relevant to a shared neural and reproductive tissue comparison.
- **Conclusion**: Established evidence supports EIF4A2 as part of a known translation-initiation relationship within the module. The module may reflect coordinated translational capacity, but it does not show whether translation is the primary biological process or merely one component of a broader housekeeping state.

#### ATG7

- **Related proteins** (co-abundance neighbors): USO1 (0.81); STRING partners: UBA3 (0.826)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: autophagy related 7. This gene encodes an E1-like activating enzyme that is essential for autophagy and cytoplasmic to vacuole transport. The encoded protein is also thought to modulate p53-dependent cell cycle pathways during prolonged metabolic stress. It has been associated with multiple functions, including axon membrane trafficking, axonal homeostasis, mitophagy, adipose differentiation, and hematopoietic stem ce…
- **Diseases (Open Targets)**: spinocerebellar ataxia, autosomal recessive 31 (0.765); neurodegenerative disease (0.558); cancer (0.556); hypertensive disorder (0.431); essential hypertension (0.387)
- **Europe PMC papers**: 20472
- **Why important**: ATG7 is a recognized autophagy and mitophagy factor with a direct STRING relationship to UBA3. It is associated with axonal homeostasis, autophagy, metabolic stress, and hematopoietic maintenance, and it has substantial literature and disease associations including neurodegenerative disorders. Its HPA associations with neutrophil progenitors, neutrophils, and oocytes indicate that its presence may be sensitive to cell state or composition.
- **Conclusion**: Established evidence supports ATG7 as a protein-quality-control and stress-response candidate. Its participation in the shared module could indicate coordinated autophagy or organelle maintenance, but the module contains no globally significant enrichment that confirms this interpretation.

#### ABCD3

- **Related proteins** (co-abundance neighbors): UGDH (0.84), HACL2 (0.83), COPG2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Peroxisomes; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP binding cassette subfamily D member 3. The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the ALD subfamily, which is involved in peroxisomal import of fatty acids and/…
- **Diseases (Open Targets)**: congenital bile acid synthesis defect 5 (0.454); oculopharyngodistal myopathy (0.380); Abnormality of the skeletal system (0.359); food allergy (0.097); colorectal carcinoma (0.097)
- **Europe PMC papers**: 1205
- **Why important**: ABCD3 connects to UGDH, HACL2, and COPG2 and is tissue-enhanced in liver. It is a peroxisomal transporter involved in import of fatty acids or fatty acyl-CoAs and is associated with fatty-acid metabolism, bile-acid biosynthesis, and peroxisome organization. Its position connects lipid and organelle metabolism to the vesicle-trafficking component represented by COPG2. It also has documented disease associations involving bile-acid synthesis and muscle abnormalities.
- **Conclusion**: Established evidence supports ABCD3 as a peroxisomal lipid-handling marker and a useful indicator of organelle metabolic state. Its inclusion may reflect coordinated lipid utilization, especially in particular cell populations, but does not establish a conserved peroxisomal mechanism across both tissues.

## Module 2

**Tissue pair**: autonomic_nervous_system and testis  
**Genes (38)**: ABHD14B, ANXA6, ATP1A1, ATXN2L, ACOT7, CDK5, CKAP4, COPB1, CPSF3, CPSF6, EIF2A, EIF3C, ENAH, AGL, GDPD1, GGPS1, GLOD4, HSPBP1, HSPA4L, CAMK4, MCM5, IMMT, NDRG3, NUP155, NUP205, NUCB2, NUP93, PSME4, SLC27A4, SEC24C, SCFD1, SMCHD1, SMARCC2, U2SURP, UBA6, UBE4A, VPS13C, VPS41

### Function

No GO/KEGG term passed global correction; therefore no globally significant GO/KEGG evidence is available. The module is best interpreted as a mixed cellular gene-expression and proteostasis program rather than as a formally established pathway. Its central genes connect translation initiation, messenger RNA processing and polyadenylation, nuclear pore transport, protein folding, vesicle trafficking, chromatin regulation, mitochondrial organization, and intermediary metabolism. EIF3C and CPSF6 occupy prominent positions in the co-abundance structure, linking translation with RNA processing. NUP93 and NUP205 connect the module to nuclear pore organization and nucleocytoplasmic transport, while HSPA4L and HSPBP1 support a chaperone and protein-quality-control component. AGL, GGPS1, ACOT7, and SLC27A4 provide metabolic and lipid-handling links. Thus, the most defensible functional description is coordinated maintenance of RNA and protein homeostasis, nuclear-cytoplasmic exchange, and cellular metabolic capacity in cells with specialized demands. These are functional inferences from annotations and network structure, not globally significant enrichment results. STRING supplied no supplementary functional-enrichment terms.

**Cell composition.** This does not resemble a plasma-protein or blood-cell module. Only NUCB2 is annotated as secreted to blood, and most genes have low immune-cell specificity; the blood-cell annotations are scattered rather than defining the module. The module is nevertheless substantially composed of broadly expressed cellular machinery: many genes have low tissue specificity and encode nuclear, cytosolic, mitochondrial, or vesicle-associated proteins. Testis protein detection is near-universal among genes with available HPA data, and several genes show enrichment in spermatids, spermatocytes, Sertoli cells, or oocytes. Brain enrichment and neuronal or glial cell-type enhancement also recur, which is compatible with the autonomic-nervous-system side of the comparison. The shared signal may therefore reflect a combination of broadly required housekeeping functions and recurrent specialized cell states, especially germ-cell differentiation, rather than contamination by blood or circulating secreted proteins. HPA has no matching autonomic-nervous-system tissue protein result, so tissue-level protein confirmation for that side is limited.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known STRING relationships form several coherent but separate pieces. CPSF3--CPSF6 supports the cleavage and polyadenylation machinery; NUP155--NUP205--NUP93 supports the nuclear pore complex; HSPA4L--HSPBP1 supports a chaperone-associated relationship; and COPB1--SEC24C together with COPB1--SCFD1 supports vesicle and Golgi trafficking. These are established relationships represented within the module, not proof that every module gene participates in one physical complex. hu.MAP independently places HSPA4L with HSPBP1 in several chaperone-related complexes (hu.MAP huMAP3_04877.1), (hu.MAP huMAP3_06506.1), (hu.MAP huMAP3_07919.1), (hu.MAP huMAP3_11049.1), (hu.MAP huMAP3_13774.1), and (hu.MAP huMAP3_14723.1), and places NUP93 with NUP205 in several broader complexes (hu.MAP huMAP3_07789.1), (hu.MAP huMAP3_05673.1), and (hu.MAP huMAP3_09042.1). The fact that these complexes contain only a subset of module members means the module is more likely a co-abundance program assembled from several connected cellular systems than a single canonical complex.

**STRING interactions (score >= 0.7)**: 7 of 703 gene pairs: COPB1–SCFD1 (0.729); COPB1–SEC24C (0.714); CPSF3–CPSF6 (0.988); HSPA4L–HSPBP1 (0.947); NUP155–NUP205 (0.999); NUP155–NUP93 (0.999); NUP205–NUP93 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04877.1 (HSPA4L, HSPBP1; 2/7); huMAP3_07789.1 (NUP93, NUP205; 2/7); huMAP3_05673.1 (NUP93, NUP205; 2/11); huMAP3_06506.1 (HSPA4L, HSPBP1; 2/23); huMAP3_09042.1 (NUP93, NUP205; 2/26); huMAP3_07919.1 (HSPA4L, HSPBP1; 2/27); huMAP3_11049.1 (HSPA4L, HSPBP1; 2/30); huMAP3_13774.1 (HSPA4L, HSPBP1; 2/33); huMAP3_14723.1 (HSPA4L, HSPBP1; 2/52)

### Novelty

The module may represent a novel cross-tissue co-abundance association, but the fact sheet does not establish that it is a new biological mechanism. Several internal relationships are already known in STRING and hu.MAP, including nuclear-pore, chaperone, cleavage-factor, and vesicle-trafficking links. Conversely, the absence of other module-wide relationships from those resources cannot prove novelty because database coverage, evidence thresholds, and complex membership are incomplete. The defensible claim is that the particular conserved co-abundance combination across autonomic nervous system and testis is potentially novel and merits validation, whereas many of its component interactions and functions are established. Replication in independent cohorts, cell-type-resolved data, perturbation experiments, and comparison with published co-expression modules would be needed to call it a new finding.

**Hypothesis.** Hypothesis: the shared module coordinates a stress-sensitive cellular maintenance program that is especially important in highly specialized cells. In this model, nuclear pore components regulate exchange of RNA and proteins; CPSF3 and CPSF6 shape transcript maturation; EIF3C and EIF2A support translation; HSPA4L and HSPBP1 protect or remove damaged proteins; COPB1, SEC24C, SCFD1, VPS41, and VPS13C maintain membrane and organelle trafficking; and AGL, GGPS1, ACOT7, and SLC27A4 supply carbohydrate, isoprenoid, and lipid metabolic support. Testis enrichment, particularly in developing germ cells, could reflect the need to couple transcript processing, proteostasis, nuclear remodeling, and metabolism during spermatogenesis. In autonomic nervous system samples, the same program could reflect neuronal or glial maintenance and high demands for transport and proteostasis. This remains a mechanistic hypothesis: the co-abundance data do not demonstrate direct regulation, physical interaction among all members, or causal conservation between the tissues.

### Important genes

#### EIF3C

- **Related proteins** (co-abundance neighbors): SCFD1 (0.94), COPB1 (0.90), AGL (0.89), CPSF6 (0.88), HSPA4L (0.85), ANXA6 (0.84), ATP1A1 (0.82), NUCB2 (0.81), SMARCC2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C is among the most connected genes in the module and links several otherwise distinct partners, including CPSF6, HSPA4L, COPB1, SCFD1, AGL, ANXA6, ATP1A1, and NUCB2. Its established function is as a subunit of the eukaryotic translation-initiation factor and it contributes to cytoplasmic translational initiation and positive regulation of translation. HPA indicates broad tissue distribution with enhancement across several brain cell types and testis protein detection. It also has a substantial literature and disease links involving neoplastic and developmental conditions.
- **Conclusion**: Established evidence supports EIF3C as a central translation-initiation component and a network bridge. My hypothesis is that its high connectivity marks translational capacity as a coordinating layer between RNA processing, proteostasis, and specialized-cell demands; the module does not establish that EIF3C controls the other genes.

#### CPSF6

- **Related proteins** (co-abundance neighbors): NUP93 (0.91), UBA6 (0.90), SMARCC2 (0.89), EIF3C (0.88), ATP1A1 (0.84), NUCB2 (0.84), AGL (0.83), SCFD1 (0.83), ATXN2L (0.81); STRING partners: CPSF3 (0.988)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cleavage and polyadenylation specific factor 6. The protein encoded by this gene is one subunit of a cleavage factor required for 3' RNA cleavage and polyadenylation processing. The interaction of the protein with the RNA is one of the earliest steps in the assembly of the 3' end processing complex and facilitates the recruitment of other processing factors. The cleavage factor complex is composed of four polypeptides. This gene encodes the 68k…
- **Diseases (Open Targets)**: cancer (0.579); neurodegenerative disease (0.463); Abnormality of the skeletal system (0.451); smoking initiation (0.424); leukemia (0.376)
- **Europe PMC papers**: 1665
- **Why important**: CPSF6 is highly connected and links the module to EIF3C, NUP93, UBA6, SMARCC2, ATP1A1, NUCB2, AGL, and SCFD1. It is an established subunit of the cleavage and polyadenylation machinery, participates in mRNA three-prime-end processing and alternative polyadenylation, and has a direct high-confidence STRING relationship with CPSF3. It is detected in testis and has extensive literature and disease associations spanning cancer, neurodegenerative disease, skeletal abnormalities, and leukemia.
- **Conclusion**: Established evidence identifies CPSF6 as a transcript-processing factor with a strong internal connection to CPSF3 and to central module genes. My hypothesis is that transcript-end processing helps couple the module across germ cells and neural-related cells, but this tissue-sharing interpretation requires transcriptomic and functional validation.

#### NUP93

- **Related proteins** (co-abundance neighbors): CPSF6 (0.91), ATXN2L (0.89), NUP205 (0.87), SMARCC2 (0.87), UBA6 (0.84), VPS13C (0.83), HSPA4L (0.82); STRING partners: NUP155 (0.999), NUP205 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_07789.1, huMAP3_05673.1, huMAP3_09042.1
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 is a central bridge between CPSF6, ATXN2L, NUP205, SMARCC2, UBA6, VPS13C, and HSPA4L. It is an established nucleoporin involved in nuclear pore assembly, nuclear import, messenger RNA export, and nucleocytoplasmic transport. STRING places it in a highly supported relationship with NUP155 and NUP205, and hu.MAP places it with NUP205 in multiple complexes (hu.MAP huMAP3_07789.1), (hu.MAP huMAP3_05673.1), and (hu.MAP huMAP3_09042.1). It is detected in testis and is associated with nephrotic syndrome and viral or infectious disease annotations.
- **Conclusion**: Established evidence supports NUP93 as a nuclear-pore structural and transport component that anchors a real subnetwork within the module. My hypothesis is that nuclear transport provides the interface connecting transcript processing to translation and proteostasis in both tissues; the co-abundance result alone cannot determine whether transport is the primary driver.

#### HSPA4L

- **Related proteins** (co-abundance neighbors): EIF3C (0.85), HSPBP1 (0.85), NUP93 (0.82); STRING partners: HSPBP1 (0.947)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_04877.1, huMAP3_06506.1, huMAP3_07919.1, huMAP3_11049.1, huMAP3_13774.1, huMAP3_14723.1
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 4 like. The protein encoded by this gene is heat shock inducible and may act as a chaperone. The encoded protein can protect the heat-shocked cell against the harmful effects of aggregated proteins. This gene is highly expressed in leukemia cells and may be a good target for therapeutic intervention. Several transcripts encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 20…
- **Diseases (Open Targets)**: alcohol drinking (0.111); ovarian neoplasm (0.110); open-angle glaucoma (0.094); nasopharyngeal carcinoma (0.074); familial idiopathic steroid-resistant nephrotic syndrome (0.061)
- **Europe PMC papers**: 815
- **Why important**: HSPA4L connects EIF3C, HSPBP1, and NUP93 and is tissue enriched in testis, with enhancement in early and late spermatids and late primary spermatocytes. It is an inducible HSP seventy-family chaperone associated with protein folding and response to unfolded protein. Its high-confidence STRING relationship with HSPBP1 is supported by repeated hu.MAP membership in chaperone-related complexes (hu.MAP huMAP3_04877.1), (hu.MAP huMAP3_06506.1), (hu.MAP huMAP3_07919.1), (hu.MAP huMAP3_11049.1), (hu.MAP huMAP3_13774.1), and (hu.MAP huMAP3_14723.1). It also has literature and disease associations involving protein stress, neoplasia, glaucoma, and renal disease.
- **Conclusion**: Established evidence supports HSPA4L as a testis-relevant chaperone and as one half of a replicated chaperone relationship with HSPBP1. My hypothesis is that the module captures a proteostasis requirement during germ-cell development and possibly neuronal maintenance, but direct conservation of this role across the two tissues remains unproven.

#### AGL

- **Related proteins** (co-abundance neighbors): ATXN2L (0.91), SMARCC2 (0.89), EIF3C (0.89), IMMT (0.85), CPSF3 (0.83), CPSF6 (0.83), SMCHD1 (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: amylo-alpha-1,6-glucosidase and 4-alpha-glucanotransferase. This gene encodes the glycogen debrancher enzyme which is involved in glycogen degradation. This enzyme has two independent catalytic activities which occur at different sites on the protein: a 4-alpha-glucotransferase activity and a amylo-1,6-glucosidase activity. Mutations in this gene are associated with glycogen storage disease although a wide range of enzymatic and clinical variability occurs…
- **Diseases (Open Targets)**: glycogen storage disease III (0.831); disorder of glycogen metabolism (0.768); glycogen storage disease XV (0.608); hereditary disease (0.507); Acute rhabdomyolysis (0.463)
- **Europe PMC papers**: 4441
- **Why important**: AGL is highly connected to ATXN2L, SMARCC2, EIF3C, IMMT, CPSF3, and CPSF6, making it a metabolic bridge to the module's RNA and nuclear machinery. Its established enzymatic role is glycogen debranching during glycogen degradation, with functions related to carbohydrate metabolism, nutrient response, and hormone response. HPA shows group enrichment in skeletal muscle and tongue and protein detection in testis. AGL has extensive literature and strong disease associations with glycogen storage and glycogen-metabolism disorders.
- **Conclusion**: Established evidence supports AGL as a metabolic component with a prominent network position and clear disease relevance. My hypothesis is that glycogen availability or nutrient-responsive metabolism helps support the RNA-processing and proteostasis activities represented by the module; this metabolic coupling is not demonstrated by the enrichment analysis.

## Module 3

**Tissue pair**: autonomic_nervous_system and testis  
**Genes (48)**: ABRACL, ANXA5, AP1B1, APEX1, ATG5, ARFGEF1, CLIC1, CNOT1, CORO7, CYP51A1, CTNND1, DYNC1I2, EIPR1, ENOPH1, GFUS, FKBP3, FSD1, HDGFL3, HNRNPH1, IDI1, EIF5, ISYNA1, LGALS1, MACROD1, ME1, MAT2A, MYO1C, FAM114A1, PCYOX1L, PDXK, PGK1, PRDX3, PRPF31, PTGR1, PYGB, RAN, RAB22A, SACM1L, SERPINH1, SUGP2, YARS1, TECR, THYN1, TMEM109, TMOD3, UBLCP1, NAE1, WASHC4

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent, so the module does not support a statistically established single pathway. Its genes nevertheless suggest a mixed intracellular program involving vesicle and endosome trafficking, microtubule and actin organization, protein synthesis and RNA processing, lipid and sterol metabolism, DNA maintenance, autophagy, redox control, and protein folding. The strongest biological interpretation is therefore a shared cellular-maintenance and trafficking state rather than a narrowly defined autonomic-nervous-system or testis-specific pathway. The testis context makes relevance to germ-cell differentiation and spermatid biology plausible, but the module alone does not establish that interpretation.

**Cell composition.** This is not primarily a plasma-protein, secreted-protein, or blood-cell module. Only a small subset is secreted to blood, and HPA assigns low immune-cell specificity to most genes. The module is broadly expressed at the tissue level, with many genes showing low tissue specificity, although several have enhanced expression in brain, liver, skeletal muscle, or testis-related cell types. HPA shows frequent cell-type enhancement in epithelial, trophoblast, and germ-cell populations, including late spermatids and spermatogenic cells. Protein detection in testis is widespread among the module genes, whereas there is no matching autonomic-nervous-system HPA tissue dataset. Thus, a shared cell-state or sample-composition effect remains possible, but a simple blood contamination explanation is not supported by the HPA summary.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING evidence is sparse: the only high-confidence reported pair is CYP51A1 with IDI1, linking sterol biosynthesis with isoprenoid metabolism. This supports a localized metabolic relationship, not a physical explanation for the entire module. hu.MAP provides partial support for several protein assemblies. APEX1, YARS1, and FKBP3 recur across multiple complexes, while EIF5, FKBP3, and YARS1 participate in translation-associated or broader cellular assemblies; UBLCP1 appears in one complex. These overlaps indicate that parts of the module intersect known macromolecular machinery, but the complexes contain many members outside the module and do not define the full co-abundance network. The network should therefore be interpreted as coordinated abundance across several cellular systems rather than as one established protein complex.

**STRING interactions (score >= 0.7)**: 1 of 1128 gene pairs: CYP51A1–IDI1 (0.942)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13998.1 (APEX1, YARS1, EIF5, FKBP3; 4/23); huMAP3_10115.1 (APEX1, YARS1, FKBP3; 3/14); huMAP3_14442.1 (APEX1, YARS1, UBLCP1; 3/57); huMAP3_03126.1 (APEX1, FKBP3; 2/3); huMAP3_04783.1 (APEX1, YARS1; 2/4); huMAP3_14982.1 (EIF5, FKBP3; 2/28)

### Novelty

A new co-abundance pattern is plausible, but novelty is not established by this fact sheet alone. The sparse STRING connectivity and partial hu.MAP overlap argue against the module being a previously recognized single complex. However, absence from STRING or hu.MAP cannot demonstrate biological novelty, because co-abundance relationships may reflect regulation, cell state, compartmental changes, or tissue composition rather than direct physical interaction. The appropriate conclusion is that the shared module is a potentially novel cross-tissue co-abundance signature whose distinctiveness requires comparison with published co-expression modules, independent cohorts, and cell-composition controls.

**Hypothesis.** Hypothesis: the module reflects a coordinated cellular-maintenance program that is especially visible in testis and may also occur in autonomic nervous system samples because both tissues contain cells requiring intense intracellular transport, cytoskeletal organization, membrane trafficking, metabolic support, and proteostatic control. In this model, dynein- and adaptor-mediated transport, WASH and actin-associated trafficking, sterol and isoprenoid metabolism, translation, RNA processing, redox defense, and endoplasmic-reticulum protein folding vary together during germ-cell or neuronal-support-cell states. The co-abundance signal could also be strengthened by shared cell populations or changing proportions of differentiating germ cells, so this mechanism should be tested with single-cell localization, cell-composition adjustment, and perturbation experiments.

### Important genes

#### DYNC1I2

- **Related proteins** (co-abundance neighbors): WASHC4 (0.91), ISYNA1 (0.90), CTNND1 (0.87), FAM114A1 (0.85), AP1B1 (0.84), NAE1 (0.83), SUGP2 (0.82), PCYOX1L (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Microtubules, Centrosome, Cytosol, Flagellar centriole, Mid piece, Principal piece; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 1 intermediate chain 2. This gene encodes a member of the dynein intermediate chain family. The encoded protein is a non-catalytic component of the cytoplasmic dynein 1 complex, which acts as a retrograde microtubule motor to transport organelles and vesicles. A pseudogene of this gene is located on chromosome 10. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly and structural brain anomalies (0.698); neurodegenerative disease (0.484); viral infectious disease (0.462); lysosomal storage disease (0.432); neurodevelopmental disorder with microcephaly, hypotonia, and variable brain anomalies (0.425)
- **Europe PMC papers**: 407
- **Why important**: DYNC1I2 is among the most connected genes in the module and links several trafficking- and cytoskeleton-related neighbors. Its established function is as a non-catalytic component of cytoplasmic dynein, supporting retrograde microtubule transport of organelles and vesicles. HPA shows broad tissue and cell-type distribution with localization to microtubules, centrosomes, and flagellar structures, including testis detection. Its disease associations include neurodevelopmental and neurodegenerative disorders, making it relevant to both tissue contexts. It is not represented in STRING or hu.MAP here, so its importance comes from network position and biological plausibility rather than documented complex membership.
- **Conclusion**: Established evidence supports DYNC1I2 as a transport and microtubule component with relevance to neuronal and testicular cellular architecture. Its central network position makes it a strong candidate for organizing the module, but a module-specific regulatory role remains a hypothesis.

#### ISYNA1

- **Related proteins** (co-abundance neighbors): SUGP2 (0.91), AP1B1 (0.91), DYNC1I2 (0.90), FSD1 (0.84), PCYOX1L (0.84), ME1 (0.82), WASHC4 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inositol-3-phosphate synthase 1. This gene encodes an inositol-3-phosphate synthase enzyme. The encoded protein plays a critical role in the myo-inositol biosynthesis pathway by catalyzing the rate-limiting conversion of glucose 6-phosphate to myoinositol 1-phosphate. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene, and a pseudogene of this gene is located on the short arm of …
- **Diseases (Open Targets)**: neurodegenerative disease (0.303); breast carcinoma (0.262); systemic lupus erythematosus (0.162); placental abruption (0.121); luminal A breast carcinoma (0.113)
- **Europe PMC papers**: 485
- **Why important**: ISYNA1 is a highly connected metabolic node linked to trafficking, cytoskeletal, and metabolic genes. It catalyzes the rate-limiting step in myo-inositol biosynthesis and contributes to phospholipid biosynthesis. HPA identifies testis and choroid plexus enhancement and cell-type enhancement in late spermatids and several reproductive-associated cell types. Its position provides a plausible bridge between membrane lipid supply and intracellular trafficking. It has relatively limited literature compared with the most extensively studied module genes, which makes its coordinated behavior particularly useful for follow-up.
- **Conclusion**: Established evidence supports ISYNA1 as an inositol and phospholipid biosynthetic enzyme with testis-relevant expression. Its connection to the broader trafficking state is a hypothesis supported by network context, not by significant enrichment or a documented physical interaction.

#### AP1B1

- **Related proteins** (co-abundance neighbors): ISYNA1 (0.91), PCYOX1L (0.86), DYNC1I2 (0.84), WASHC4 (0.83), SUGP2 (0.83), NAE1 (0.82), YARS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor related protein complex 1 subunit beta 1. Adaptor protein complex 1 is found at the cytoplasmic face of coated vesicles located at the Golgi complex, where it mediates both the recruitment of clathrin to the membrane and the recognition of sorting signals within the cytosolic tails of transmembrane receptors. This complex is a heterotetramer composed of two large, one medium, and one small adaptin subunit. The protein encoded by this gene…
- **Diseases (Open Targets)**: ichthyosiform erythroderma, corneal involvement, and hearing loss (0.715); HIV infectious disease (0.503); MEDNIK syndrome (0.371); neurodegenerative disease (0.370); KID syndrome (0.292)
- **Europe PMC papers**: 500
- **Why important**: AP1B1 is connected to the trafficking-rich portion of the network and encodes a large subunit of adaptor protein complex one, which recruits clathrin and recognizes sorting signals at the Golgi. It is present in several hu.MAP complexes through APEX1 and YARS1-related assemblies, although those complexes do not establish AP1B1 as part of one unified module complex. HPA places it at the Golgi and shows testis detection, with cell-type enhancement in Hofbauer cells and microglia. Its disease associations include syndromic epithelial and neurodegenerative conditions, consistent with a broad trafficking role.
- **Conclusion**: Established evidence supports AP1B1 as a Golgi sorting and vesicle-trafficking component. Its module association is consistent with coordinated intracellular transport, while any specific role in autonomic or germ-cell biology remains a hypothesis.

#### SERPINH1

- **Related proteins** (co-abundance neighbors): HNRNPH1 (0.88), PRDX3 (0.88), EIF5 (0.88), ENOPH1 (0.87), TMOD3 (0.84), ANXA5 (0.82), LGALS1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family H member 1. This gene encodes a member of the serpin superfamily of serine proteinase inhibitors. The encoded protein is localized to the endoplasmic reticulum and plays a role in collagen biosynthesis as a collagen-specific molecular chaperone. Autoantibodies to the encoded protein have been found in patients with rheumatoid arthritis. Expression of this gene may be a marker for cancer, and nucleotide polymo…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 10 (0.714); preterm premature rupture of the membranes (0.559); coronary artery disorder (0.554); myocardial infarction (0.510); Abnormality of the skeletal system (0.474)
- **Europe PMC papers**: 2762
- **Why important**: SERPINH1 occupies a connected position near RNA-processing, redox, translation, cytoskeletal, and annexin-related genes. It is an endoplasmic-reticulum collagen-specific molecular chaperone involved in protein folding, unfolded-protein response, and collagen fibril organization. HPA shows enhancement in several stromal, trophoblast, and reproductive-associated cell types and detects the protein in testis. Its disease associations include osteogenesis imperfecta and premature membrane rupture, while its literature supports a substantial and established chaperone biology. It therefore represents the module's proteostasis and extracellular-matrix-related axis.
- **Conclusion**: Established evidence supports SERPINH1 as an endoplasmic-reticulum folding factor with matrix-related function. Its co-abundance with trafficking and stress-related genes may indicate coordinated proteostasis, but the module does not prove a collagen-specific mechanism in either tissue.

#### IDI1

- **Related proteins** (co-abundance neighbors): CYP51A1 (0.92), LGALS1 (0.89), APEX1 (0.85), CLIC1 (0.83), ANXA5 (0.82); STRING partners: CYP51A1 (0.942)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: isopentenyl-diphosphate delta isomerase 1. IDI1 encodes a peroxisomally-localized enzyme that catalyzes the interconversion of isopentenyl diphosphate (IPP) to its highly electrophilic isomer, dimethylallyl diphosphate (DMAPP), which are the substrates for the successive reaction that results in the synthesis of farnesyl diphosphate and, ultimately, cholesterol.  It has been shown in peroxisomal deficiency diseases such as Zellweger syndro…
- **Diseases (Open Targets)**: neurodegenerative disease (0.539); hypotensive disorder (0.215); placental retention (0.191); liver disorder (0.147); esophageal cancer (0.138)
- **Europe PMC papers**: 1844
- **Why important**: IDI1 is connected to ANXA5, LGALS1, APEX1, and CLIC1 and forms the sole reported high-confidence STRING pair in the module with CYP51A1. It catalyzes the interconversion of isoprenoid precursors that feed sterol and cholesterol synthesis. HPA shows enhancement in several epithelial, reproductive, and testis-associated cell types. Its established biochemical role gives the module a concrete metabolic anchor, and its disease associations include neurodegenerative and liver-related disorders. The limited direct network connectivity means it should be interpreted as a pathway anchor rather than a global hub.
- **Conclusion**: Established evidence supports IDI1 as an isoprenoid and cholesterol-biosynthesis enzyme, with a documented relationship to CYP51A1. A coordinated sterol-metabolic contribution to the shared module is a reasonable hypothesis, but it is not supported by globally significant enrichment.

## Module 4

**Tissue pair**: autonomic_nervous_system and testis  
**Genes (48)**: ACE, ACSL1, ALDH1B1, ATP5PB, ATG4B, ATG9A, ATP5F1C, BAG5, BOLA2, TRIP10, DCUN1D1, SORD, DNAJB1, ERGIC2, ERLIN1, SIRAL1, HMOX2, HSDL1, IDE, IQGAP2, L2HGDH, ME2, MSTO1, NME7, NDUFS1, NFS1, NRDC, NUP188, NUP37, NUP54, OXSM, PFKP, PGP, PIP4K2C, NUP210, PPM1A, PSMC2, PSMA1, PTPMT1, UQCRC2, RAE1, RCC1, SDHA, CARS1, DARS2, IARS2, CCT3, ACAT1

### Function

No GO/KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The most coherent interpretation is a heterogeneous cellular-maintenance program combining mitochondrial energy and metabolic functions, nuclear transport, protein folding and quality control, proteasomal turnover, and autophagy. The mitochondrial interpretation is supported by the supplementary STRING component term (STRING Component Mitochondrion; within-query FDR = 0.0412), which includes SDHA, NDUFS1, ATP5PB, ATP5F1C, UQCRC2, NFS1, DARS2, IARS2, and related genes, while the supplementary amyotrophic-lateral-sclerosis pathway (STRING KEGG Amyotrophic lateral sclerosis; within-query FDR = 0.0197) mainly reflects respiratory-chain, ATP-synthase, proteasome, and nuclear-pore components rather than evidence of an amyotrophic-lateral-sclerosis-specific module. Nuclear transport is represented by NUP54, NUP188, NUP210, NUP37, RAE1, and RCC1. Proteostasis is represented by DNAJB1, BAG5, CCT3, PSMA1, PSMC2, ATG4B, and ATG9A. Thus, the safest functional description is a general cellular homeostasis and energy-demand program, with a possible germ-cell differentiation context, rather than a single narrowly defined pathway.

**Cell composition.** The module does not appear to be dominated by plasma or secreted proteins: only ACE and IDE have secretome annotations, and ACE is specifically reported as secreted to blood. It also does not look primarily blood-cell derived, because most genes have low immune-cell specificity; a smaller subset has immune-cell enhancement or enrichment, including ACSL1, SORD, IQGAP2, and related genes. The strongest compositional signal is cell type rather than blood: many genes are enhanced or enriched in early or late spermatids and primary spermatocytes, and several are tissue enhanced in testis. This is compatible with the module being influenced by germ-cell composition in testis. The autonomic-nervous-system interpretation cannot be checked by matching HPA tissue protein data because that tissue has no matching HPA tissue entry. Testis protein detection is broad across the module, supporting biological presence there, but it does not establish that the same cell population drives the signal in both tissues. The mixture of low tissue specificity, mitochondrial proteins, nuclear-pore proteins, chaperones, and proteostasis genes also leaves open a shared housekeeping or cellular-stress component.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides several established physical or functional relationship groups. The strongest coherent group is the respiratory and ATP-production cluster linking SDHA, NDUFS1, UQCRC2, ATP5PB, and ATP5F1C; ACAT1 also connects to SDHA (STRING KEGG Amyotrophic lateral sclerosis; within-query FDR = 0.0197) (STRING Component Mitochondrion; within-query FDR = 0.0412). A second established group is the nuclear-pore cluster linking NUP188, NUP210, NUP37, NUP54, and RAE1 (STRING KEGG Amyotrophic lateral sclerosis; within-query FDR = 0.0197). PSMA1 and PSMC2 form a proteasome relationship, DNAJB1 and BAG5 form a chaperone relationship, DARS2 and IARS2 form a mitochondrial translation-related relationship, and ATG4B and ATG9A form an autophagy relationship. hu.MAP independently supports the nuclear-pore assemblies (hu.MAP huMAP3_12581.1) (hu.MAP huMAP3_07492.1) (hu.MAP huMAP3_09710.1) (hu.MAP huMAP3_10000.1) (hu.MAP huMAP3_08489.1) (hu.MAP huMAP3_09220.1) (hu.MAP huMAP3_13857.1) (hu.MAP huMAP3_06369.1) (hu.MAP huMAP3_09825.1), the ATP-synthase assemblies (hu.MAP huMAP3_08716.1) (hu.MAP huMAP3_10957.1) (hu.MAP huMAP3_07476.1) (hu.MAP huMAP3_05994.1) (hu.MAP huMAP3_08393.1) (hu.MAP huMAP3_09775.1) (hu.MAP huMAP3_09307.1) (hu.MAP huMAP3_11095.1), the proteasome assemblies (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1), the DNAJB1-BAG5 chaperone assemblies (hu.MAP huMAP3_06506.1) (hu.MAP huMAP3_07919.1) (hu.MAP huMAP3_11049.1) (hu.MAP huMAP3_13774.1) (hu.MAP huMAP3_14723.1), the mitochondrial translation assemblies containing DARS2 and IARS2 (hu.MAP huMAP3_09668.1) (hu.MAP huMAP3_10525.1) (hu.MAP huMAP3_13468.1), and the PIP4K2C-DCUN1D1, ALDH1B1-PTPMT1, and other smaller complexes. These findings show that substantial parts of the module recapitulate known molecular machines. They support biological coherence, but they do not prove that every co-abundance edge is a direct physical interaction or that the module is one biochemical complex.

**STRING interactions (score >= 0.7)**: 26 of 1128 gene pairs: ACAT1–SDHA (0.762); ATG4B–ATG9A (0.776); ATP5F1C–ATP5PB (0.999); ATP5F1C–NDUFS1 (0.959); ATP5F1C–SDHA (0.75); ATP5F1C–UQCRC2 (0.98); ATP5PB–NDUFS1 (0.886); ATP5PB–SDHA (0.755); ATP5PB–UQCRC2 (0.973); BAG5–DNAJB1 (0.85); BOLA2–NFS1 (0.737); CARS1–IARS2 (0.901); DARS2–IARS2 (0.895); NDUFS1–SDHA (0.995); NDUFS1–UQCRC2 (0.998); NUP188–NUP210 (0.992); NUP188–NUP37 (0.983); NUP188–NUP54 (0.981); NUP188–RAE1 (0.878); NUP210–NUP37 (0.975); NUP210–NUP54 (0.967); NUP210–RAE1 (0.865); NUP37–NUP54 (0.968); NUP54–RAE1 (0.916); PSMA1–PSMC2 (0.999); SDHA–UQCRC2 (0.99)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Amyotrophic lateral sclerosis (FDR = 0.0197, 12 genes); Component Mitochondrion (FDR = 0.0412, 23 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12581.1 (RCC1, RAE1, NUP54, NUP37; 4/58); huMAP3_07492.1 (NUP188, NUP37, NUP210; 3/10); huMAP3_09710.1 (NUP188, NUP37, NUP210; 3/13); huMAP3_10000.1 (RCC1, RAE1, NUP54; 3/44); huMAP3_05855.1 (PIP4K2C, DCUN1D1; 2/2); huMAP3_01275.1 (PIP4K2C, DCUN1D1; 2/3); huMAP3_07859.1 (PIP4K2C, DCUN1D1; 2/3); huMAP3_09161.1 (ALDH1B1, PTPMT1; 2/4); huMAP3_10794.1 (ALDH1B1, PTPMT1; 2/5); huMAP3_09668.1 (DARS2, IARS2; 2/8); huMAP3_08489.1 (NUP188, NUP37; 2/10); huMAP3_09220.1 (RAE1, NUP54; 2/11); huMAP3_13857.1 (PIP4K2C, DCUN1D1; 2/12); huMAP3_06369.1 (RAE1, NUP54; 2/12); huMAP3_08716.1 (ATP5PB, ATP5F1C; 2/15); huMAP3_10957.1 (PIP4K2C, DCUN1D1; 2/15); huMAP3_07476.1 (ATP5PB, ATP5F1C; 2/18); huMAP3_05994.1 (ATP5PB, ATP5F1C; 2/19); huMAP3_08393.1 (ATP5PB, ATP5F1C; 2/19); huMAP3_09775.1 (ATP5PB, ATP5F1C; 2/21); huMAP3_06506.1 (DNAJB1, BAG5; 2/23); huMAP3_11084.1 (ACSL1, SIRAL1; 2/27); huMAP3_07919.1 (DNAJB1, BAG5; 2/27); huMAP3_09825.1 (NUP188, NUP37; 2/27); huMAP3_11049.1 (DNAJB1, BAG5; 2/30); huMAP3_13774.1 (DNAJB1, BAG5; 2/33); huMAP3_10525.1 (DARS2, IARS2; 2/33); huMAP3_09307.1 (ATP5PB, ATP5F1C; 2/35); huMAP3_11095.1 (ATP5PB, ATP5F1C; 2/45); huMAP3_14723.1 (DNAJB1, BAG5; 2/52); huMAP3_06247.1 (UQCRC2, ATP5PB; 2/65); huMAP3_09656.1 (PSMA1, PSMC2; 2/64); huMAP3_13725.1 (PSMA1, PSMC2; 2/69); huMAP3_11349.1 (ACE, ATG9A; 2/78); huMAP3_13468.1 (DARS2, IARS2; 2/99)

### Novelty

The module should not be called a wholly new molecular complex. Several of its strongest relationships are already represented in STRING and hu.MAP, especially the respiratory-chain, ATP-synthase, nuclear-pore, proteasome, chaperone, autophagy, and mitochondrial translation groups. The potentially novel observation is the coordinated co-abundance of these established components across autonomic nervous system and testis, together with the strong spermatid-associated composition in HPA. However, the fact sheet provides no comparison against previously published tissue-pair modules, no replication cohort, no perturbation experiment, and no evidence that the cross-system coordination is independent of cell composition. Absence of a STRING or hu.MAP relationship for an edge does not establish novelty. The appropriate conclusion is that this may be a new cross-tissue co-abundance pattern assembled from largely known cellular systems, but novelty remains provisional until tested against independent data, cell-composition controls, and existing co-expression studies.

**Hypothesis.** Hypothesis: the shared module reflects a demand-coupled cellular homeostasis program in metabolically active or differentiating germ-cell-like populations and in autonomic-nervous-system cells. Mitochondrial respiration, iron-sulfur and mitochondrial translation functions, ATP production, nuclear import and RNA export, chaperone-assisted folding, proteasomal degradation, and autophagy may be coordinated to maintain protein and organelle quality during high metabolic activity or differentiation. In testis, the enrichment of genes in spermatids and primary spermatocytes suggests that germ-cell composition could generate much of the signal. ACE may add a tissue-interface or vesicular component, but its presence should not be interpreted as evidence that the whole module is a circulating plasma-protein module. This hypothesis requires validation by cell-resolved expression, protein abundance, and perturbation experiments.

### Important genes

#### SDHA

- **Related proteins** (co-abundance neighbors): NDUFS1 (0.89), ME2 (0.88), DARS2 (0.82), BAG5 (0.81), PFKP (0.81), NUP54 (0.81), IARS2 (0.81); STRING partners: ACAT1 (0.762), ATP5F1C (0.75), ATP5PB (0.755), NDUFS1 (0.995), UQCRC2 (0.99)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate dehydrogenase complex flavoprotein subunit A. This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identi…
- **Diseases (Open Targets)**: mitochondrial complex II deficiency, nuclear type 1 (0.813); pheochromocytoma/paraganglioma syndrome 5 (0.790); dilated cardiomyopathy 1GG (0.768); neurodegeneration with ataxia and late-onset optic atrophy (0.761); gastrointestinal stromal tumor (0.743)
- **Europe PMC papers**: 12756
- **Why important**: SDHA is a highly connected module gene linking the mitochondrial signal to NDUFS1, UQCRC2, ATP5F1C, ATP5PB, ACAT1, ME2, and other module members. It is the catalytic flavoprotein subunit of succinate dehydrogenase and therefore connects succinate metabolism with respiratory-chain electron transfer. It is tissue enhanced in heart and skeletal muscle, detected in testis, and has extensive literature and disease associations involving mitochondrial respiratory deficiency, cardiomyopathy, neurodegeneration, and tumor predisposition. STRING places it in the supplementary mitochondrial term (STRING Component Mitochondrion; within-query FDR = 0.0412) and the supplementary amyotrophic-lateral-sclerosis term (STRING KEGG Amyotrophic lateral sclerosis; within-query FDR = 0.0197).
- **Conclusion**: Established evidence supports SDHA as a central mitochondrial anchor of the module and as a plausible marker of respiratory capacity. It does not establish that SDHA initiates the cross-tissue co-abundance pattern. The hypothesis that SDHA coordinates the nuclear-pore and proteostasis arms is indirect and should be tested rather than treated as established.

#### NUP54

- **Related proteins** (co-abundance neighbors): BAG5 (0.91), DNAJB1 (0.84), CCT3 (0.83), ACE (0.82), SIRAL1 (0.82), NUP188 (0.81), SDHA (0.81); STRING partners: NUP188 (0.981), NUP210 (0.967), NUP37 (0.968), RAE1 (0.916)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_12581.1, huMAP3_10000.1, huMAP3_09220.1, huMAP3_06369.1
- **Function (MyGene.info)**: nucleoporin 54. The nuclear envelope creates distinct nuclear and cytoplasmic compartments in eukaryotic cells. It consists of two concentric membranes perforated by nuclear pores, large protein complexes that form aqueous channels to regulate the flow of macromolecules between the nucleus and the cytoplasm. These complexes are composed of at least 100 different polypeptide subunits, many of which belong to the n…
- **Diseases (Open Targets)**: dystonia 37, early-onset, with striatal lesions (0.548); Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.526); neurodegenerative disease (0.371)
- **Europe PMC papers**: 541
- **Why important**: NUP54 is among the more connected genes and links BAG5, DNAJB1, CCT3, ACE, NUP188, and SDHA in the module. It is a nuclear-pore component involved in nucleocytoplasmic transport and nuclear-pore organization. STRING shows strong relationships with NUP188, NUP210, NUP37, and RAE1, while hu.MAP places it in several nuclear-pore and RNA-transport assemblies (hu.MAP huMAP3_12581.1) (hu.MAP huMAP3_10000.1) (hu.MAP huMAP3_09220.1) (hu.MAP huMAP3_06369.1). It has substantial literature and disease associations involving dystonia, infection-related biology, and neurodegenerative disease.
- **Conclusion**: Established evidence supports NUP54 as a representative nuclear-transport component embedded in known nuclear-pore assemblies. Its co-abundance with mitochondrial and chaperone genes suggests coordinated cellular maintenance, but a direct mechanistic bridge between these systems is a hypothesis rather than an established function of this module.

#### BAG5

- **Related proteins** (co-abundance neighbors): NUP54 (0.91), MSTO1 (0.84), SORD (0.83), SDHA (0.81), NFS1 (0.80); STRING partners: DNAJB1 (0.85)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_06506.1, huMAP3_07919.1, huMAP3_11049.1, huMAP3_13774.1, huMAP3_14723.1
- **Function (MyGene.info)**: BAG cochaperone 5. The protein encoded by this gene is a member of the BAG1-related protein family. BAG1 is an anti-apoptotic protein that functions through interactions with a variety of cell apoptosis and growth related proteins including BCL-2, Raf-protein kinase, steroid hormone receptors, growth factor receptors and members of the heat shock protein 70 kDa family. This protein contains a BAG domain near the C-t…
- **Diseases (Open Targets)**: cardiomyopathy, dilated, 2F (0.614); mitochondrial complex IV deficiency, nuclear type 17 (0.533); mitochondrial complex IV deficiency, nuclear-type (0.420); leigh syndrome due to mitochondrial complex iv deficiency (0.420); familial isolated dilated cardiomyopathy (0.391)
- **Europe PMC papers**: 635
- **Why important**: BAG5 occupies a connected position between NUP54, MSTO1, SORD, SDHA, and NFS1. It is a cochaperone involved in protein folding, protein stabilization, and regulation of ubiquitin-dependent proteasomal processes. It is tissue enriched in testis and enhanced across early spermatids, late primary spermatocytes, and late spermatids. STRING links it to DNAJB1, and hu.MAP repeatedly places the BAG5-DNAJB1 pair in chaperone complexes (hu.MAP huMAP3_06506.1) (hu.MAP huMAP3_07919.1) (hu.MAP huMAP3_11049.1) (hu.MAP huMAP3_13774.1) (hu.MAP huMAP3_14723.1). Its disease associations include cardiomyopathy and mitochondrial complex deficiencies.
- **Conclusion**: Established evidence supports BAG5 as a testis-relevant proteostasis component that connects chaperoning with mitochondrial and quality-control signals. The hypothesis that BAG5 helps protect differentiating germ cells from mitochondrial or folding stress is biologically plausible but is not demonstrated by the co-abundance data alone.

#### NFS1

- **Related proteins** (co-abundance neighbors): ME2 (0.84), PPM1A (0.84), PSMC2 (0.82), HMOX2 (0.82), BAG5 (0.80), OXSM (0.80); STRING partners: BOLA2 (0.737)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NFS1 cysteine desulfurase. Iron-sulfur clusters are required for the function of many cellular enzymes. The proteins encoded by this gene supply inorganic sulfur to these clusters by removing the sulfur from cysteine, creating alanine in the process. This gene uses alternate in-frame translation initiation sites to generate mitochondrial forms and cytoplasmic/nuclear forms. Selection of the alternative initiation sites is d…
- **Diseases (Open Targets)**: combined oxidative phosphorylation deficiency 52 (0.543); neurodegenerative disease (0.469); severe neonatal lactic acidosis due to NFS1-ISD11 complex deficiency (0.370); placenta praevia (0.151); coronary artery disorder (0.132)
- **Europe PMC papers**: 1560
- **Why important**: NFS1 links ME2, PPM1A, PSMC2, HMOX2, BAG5, and OXSM. It supplies sulfur for iron-sulfur cluster assembly and has mitochondrial and cytosolic or nuclear forms. It is detected in testis and is cell-type enhanced in adipocytes, cardiomyocytes, and myonuclei. STRING connects it to BOLA2 and includes it in the supplementary mitochondrial component (STRING Component Mitochondrion; within-query FDR = 0.0412). Its literature and disease associations include iron-sulfur biology, combined oxidative-phosphorylation deficiency, severe lactic acidosis, and neurodegeneration.
- **Conclusion**: Established evidence supports NFS1 as a metabolic and mitochondrial quality-control component that could explain part of the module's connection between respiration and cellular stress responses. It does not prove that iron-sulfur assembly is the module's defining function, especially because no GO/KEGG term passed global correction.

#### ACE

- **Related proteins** (co-abundance neighbors): PGP (0.86), SIRAL1 (0.83), NUP54 (0.82), DNAJB1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_11349.1
- **Function (MyGene.info)**: angiotensin I converting enzyme. This gene encodes an enzyme involved in blood pressure regulation and electrolyte balance. It catalyzes the conversion of angiotensin I into a physiologically active peptide angiotensin II. Angiotensin II is a potent vasopressor and aldosterone-stimulating peptide that controls blood pressure and fluid-electrolyte balance. This angiotensin converting enzyme (ACE) also inactivates the vasodilator p…
- **Diseases (Open Targets)**: hypertensive disorder (0.750); renal tubular dysgenesis of genetic origin (0.729); renal tubular dysgenesis (0.724); cardiovascular disorder (0.704); diabetic kidney disease (0.689)
- **Europe PMC papers**: 95248
- **Why important**: ACE is a lower-connectivity but biologically distinctive module member linking PGP, SIRAL1, NUP54, and DNAJB1. It is a well-studied enzyme in angiotensin and bradykinin metabolism, is tissue enhanced in testis and intestine, is enriched in late spermatids and enterocytes, and is secreted to blood. It has extensive literature and strong disease associations involving hypertension, renal developmental disorders, cardiovascular disease, and diabetic kidney disease. Its hu.MAP membership is in a mixed complex containing ATG9A (hu.MAP huMAP3_11349.1), rather than a dedicated ACE complex.
- **Conclusion**: Established evidence supports ACE as a testis-associated, vesicular or extracellular-interface marker that may help identify the tissue or cell context of the module. Because only a small part of the module is secreted and most genes are intracellular, ACE should not be used to define the module as a plasma-protein program. Its connection to the mitochondrial and nuclear-pore arms remains a co-abundance hypothesis.

## Module 5

**Tissue pair**: autonomic_nervous_system and testis  
**Genes (35)**: ACO2, ALDOC, AP3B1, ATP2B4, BLMH, BPNT1, CHKA, CARHSP1, CISD2, COG1, CYB5A, SHMT1, HSPA8, TMPO, TMPO, MATR3, WDR77, MMS19, MYG1, NDUFAF4, NDUFS4, PPP6R3, PSMD13, RPL3, POLR2E, FARSB, SYNE2, VARS1, WARS1, YARS2, TBCE, CCT8, TKFC, UAP1, XPO4

### Function

This is not a strongly unified pathway module: no GO or KEGG term passed global correction, and STRING reported no supplementary functional enrichment. The gene-level annotations nevertheless indicate a composite cellular-maintenance program. Its prominent themes are protein folding and proteostasis through TBCE and CCT8, cytosolic and mitochondrial translation through WARS1, VARS1, FARSB and YARS2, mitochondrial respiration through NDUFS4 and NDUFAF4, and intermediary metabolism through UAP1, ACO2, ALDOC, SHMT1 and TKFC. COG1, AP3B1, XPO4, POLR2E and related genes add Golgi trafficking, vesicle transport and nuclear gene-expression functions. The network therefore appears more consistent with coordinated biosynthetic, folding and energetic demands than with a single narrowly defined biological process. The strongest network hub is UAP1, which links metabolic, folding, translation-related and calcium-handling genes. These interpretations are based on gene annotations and network structure, not on significant GO/KEGG enrichment.

**Cell composition.** The module is not dominated by plasma or secreted proteins: HPA reports no secreted genes. It is also not primarily blood-cell enriched, because most genes have low immune-cell specificity, although a small subset has immune-cell or blood-cell associations. Most genes have low tissue specificity, while many are cell-type enhanced, including genes associated with late spermatids, oocytes, astrocytes and Bergmann glia. This pattern is compatible with broadly required intracellular functions that become coordinated in particular cell states, rather than a secreted-tissue program. Testis protein detection is broad among the annotated genes, whereas HPA has no matching autonomic-nervous-system tissue protein dataset. The shared module could therefore partly reflect common cellular composition or activity states in the sampled tissues, including germ-cell and neural-lineage programs, rather than a tissue-pair-specific molecular pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited set of established relationships. The strongest links include NDUFAF4 with NDUFS4, CCT8 with HSPA8, ALDOC with TKFC, and a connected aminoacyl-tRNA-synthetase group involving VARS1, WARS1, YARS2 and FARSB. These links show that parts of the module contain biologically plausible known interactions, especially mitochondrial complex-I assembly, chaperoning and translation. hu.MAP independently places NDUFS4 and NDUFAF4 together in several complex-I-related complexes (hu.MAP huMAP3_14018.1) through (hu.MAP huMAP3_14878.1). However, each hu.MAP complex contains only a small subset of this module, and most module genes have no listed hu.MAP complex or STRING partner in the supplied evidence. Thus, the network is not simply a recovered complete known complex; it combines several established molecular neighborhoods with co-abundance links that remain mechanistically unresolved.

**STRING interactions (score >= 0.7)**: 8 of 595 gene pairs: ALDOC–TKFC (0.915); CCT8–HSPA8 (0.905); FARSB–VARS1 (0.776); FARSB–YARS2 (0.705); NDUFAF4–NDUFS4 (0.958); VARS1–WARS1 (0.901); VARS1–YARS2 (0.878); WARS1–YARS2 (0.932)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14018.1 (NDUFS4, NDUFAF4; 2/48); huMAP3_06397.1 (NDUFS4, NDUFAF4; 2/49); huMAP3_09982.1 (NDUFS4, NDUFAF4; 2/49); huMAP3_09567.1 (NDUFS4, NDUFAF4; 2/52); huMAP3_14878.1 (NDUFS4, NDUFAF4; 2/53)

### Novelty

The module should be described as a potentially interesting co-abundance association, not as a newly discovered biological complex or pathway. Its novelty is not established by the supplied evidence: globally corrected GO/KEGG enrichment is absent, STRING provides only a limited set of known pairwise relationships, and hu.MAP support is concentrated on the NDUFS4–NDUFAF4 complex-I pair. Absence of broader STRING or hu.MAP coverage does not prove that the remaining associations are novel, because those resources measure curated or experimentally supported physical and functional relationships rather than tissue-specific co-abundance. A defensible novelty claim would require replication in independent autonomic-nervous-system and testis datasets, comparison with existing co-expression modules, and testing whether the association persists after adjustment for cell-type composition and general expression abundance.

**Hypothesis.** Hypothesis: the module may represent a shared high-demand cellular state in autonomic neural cells and testicular germ or supporting cells, in which protein synthesis, chaperone-assisted folding, mitochondrial energy production, RNA processing and membrane or nuclear trafficking are coordinately increased. UAP1 may connect metabolic and biosynthetic demand to the folding and translation portion of the network, while the NDUFS4–NDUFAF4 pair may mark a mitochondrial respiratory component. The aminoacyl-tRNA-synthetase cluster could reflect translational demand, and the HPA cell-type pattern raises the possibility that the apparent tissue sharing is partly driven by related cell-state composition rather than a dedicated autonomic–testis mechanism. This remains a hypothesis because no globally significant functional term or direct physical interaction spanning the full module was demonstrated.

### Important genes

#### UAP1

- **Related proteins** (co-abundance neighbors): NDUFAF4 (0.90), CCT8 (0.83), TBCE (0.82), YARS2 (0.81), SHMT1 (0.81), ATP2B4 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UDP-N-acetylglucosamine pyrophosphorylase 1. Enables identical protein binding activity. Predicted to be involved in UDP-N-acetylglucosamine biosynthetic process. Located in cytosol; nucleoplasm; and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.303); gout (0.205); tuberculosis (0.205); sialolithiasis (0.186); viral eye infection (0.177)
- **Europe PMC papers**: 765
- **Why important**: UAP1 is the strongest network hub in the supplied topology and connects NDUFAF4, CCT8, TBCE, YARS2, SHMT1 and ATP2B4. Its established function is UDP-N-acetylglucosamine biosynthesis, linking it to cellular biosynthetic capacity, and its HPA profile indicates liver enhancement with several cell-type associations. It also has substantial literature and disease-oriented associations including neurodegenerative disease and gout.
- **Conclusion**: Established evidence supports UAP1 as a central integrator of several module neighborhoods and as a nucleotide-sugar biosynthetic enzyme. It is reasonable to hypothesize that UAP1 helps couple biosynthetic demand to protein folding, metabolism and mitochondrial function in this module, but the co-abundance data do not establish UAP1 as the module regulator.

#### TBCE

- **Related proteins** (co-abundance neighbors): CCT8 (0.90), FARSB (0.89), MYG1 (0.83), UAP1 (0.82), VARS1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tubulin folding cofactor E. Cofactor E is one of four proteins (cofactors A, D, E, and C) involved in the pathway leading to correctly folded beta-tubulin from folding intermediates. Cofactors A and D are believed to play a role in capturing and stabilizing beta-tubulin intermediates in a quasi-native confirmation. Cofactor E binds to the cofactor D/beta-tubulin complex; interaction with cofactor C then causes the release of…
- **Diseases (Open Targets)**: hypoparathyroidism-retardation-dysmorphism syndrome (0.777); autosomal recessive Kenny-Caffey syndrome (0.737); encephalopathy, progressive, with amyotrophy and optic atrophy (0.700); Kenny-Caffey syndrome (0.620); neurodegenerative disease (0.527)
- **Europe PMC papers**: 642
- **Why important**: TBCE is one of the more connected genes and links CCT8, FARSB, MYG1, UAP1 and VARS1. Its established role is tubulin folding-cofactor activity, with functions in microtubule organization, protein folding and mitotic-spindle organization. HPA associates it with astrocytes, Bergmann glia and multiple neuronal cell types, while disease associations include Kenny-Caffey syndromes and progressive encephalopathy.
- **Conclusion**: Established evidence supports TBCE as a proteostasis and cytoskeletal-folding component with relevance to neural cell biology. Its position suggests that it may bridge chaperoning, translation and cell-structure demands in the module, but a specific autonomic–testis mechanism is not demonstrated.

#### CCT8

- **Related proteins** (co-abundance neighbors): FARSB (0.90), TBCE (0.90), VARS1 (0.88), UAP1 (0.83); STRING partners: HSPA8 (0.905)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is connected to TBCE, FARSB, VARS1 and UAP1 and has a high-confidence STRING relationship with HSPA8. It is a subunit of the cytosolic CCT chaperonin involved in folding and stabilization of newly synthesized proteins. HPA shows cell-type enhancement in oocytes and localization in testicular connecting and end pieces, and the gene has a substantial literature describing chaperone and protein-homeostasis functions.
- **Conclusion**: Established evidence supports CCT8 as a central protein-folding component and identifies a known chaperone relationship with HSPA8. Its network position supports a hypothesis that the module reflects increased proteome-construction and folding demand, but CCT8 cannot by itself define the module’s tissue function.

#### WARS1

- **Related proteins** (co-abundance neighbors): SYNE2 (0.90), TKFC (0.86), ACO2 (0.84), MYG1 (0.80); STRING partners: VARS1 (0.901), YARS2 (0.932)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tryptophanyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Two forms of tryptophanyl-tRNA synthetase exist, a cytoplasmic form, named WARS, and a mitochondrial form, named…
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly and speech delay, with or without brain abnormalities (0.556); distal hereditary motor neuropathy (0.377); complex neurodevelopmental disorder (0.370); autosomal recessive primary microcephaly (0.370); neuronopathy, distal hereditary motor, type 9 (0.330)
- **Europe PMC papers**: 380
- **Why important**: WARS1 connects SYNE2, TKFC, ACO2 and MYG1 in the co-abundance network and has established STRING links with VARS1 and YARS2. It catalyzes tryptophan charging of cytoplasmic tRNA and is annotated in translation, tRNA aminoacylation, intracellular signaling and regulation of angiogenesis. HPA associates it with late primary spermatocytes, late spermatids and several other cell types, while disease associations include neurodevelopmental and hereditary motor-neuron disorders.
- **Conclusion**: Established evidence supports WARS1 as a translation-related enzyme that also has broader cellular associations. Its links to other aminoacyl-tRNA synthetases make it a plausible marker of translational demand in the module, but the data do not show that WARS1 drives the shared tissue association.

#### NDUFS4

- **Related proteins** (co-abundance neighbors): ALDOC (0.84); STRING partners: NDUFAF4 (0.958)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit S4. This gene encodes an nuclear-encoded accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (complex I, or NADH:ubiquinone oxidoreductase). Complex I removes electrons from NADH and passes them to the electron acceptor ubiquinone. Mutations in this gene can cause mitochondrial complex I deficiencies such as Leigh syndrome. Alternative splicing results in multiple tran…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.800); Leigh syndrome (0.775); mitochondrial complex I deficiency, nuclear type 1 (0.721); type 2 diabetes mellitus (0.689); diabetes mellitus (0.662)
- **Europe PMC papers**: 2283
- **Why important**: NDUFS4 is directly linked to NDUFAF4 by STRING and occurs with NDUFAF4 in each of the listed hu.MAP complex-I-related complexes (hu.MAP huMAP3_14018.1) through (hu.MAP huMAP3_14878.1). It is an accessory subunit of mitochondrial respiratory complex I, with established roles in NADH-to-ubiquinone electron transfer and aerobic respiration. It has strong disease associations with mitochondrial complex-I deficiency and Leigh syndrome.
- **Conclusion**: Established evidence makes NDUFS4 the clearest mitochondrial-respiration marker in the module and provides independent STRING and hu.MAP support for a complex-I substructure. A contribution of mitochondrial energetic demand to the module is plausible, but the limited representation of complex-I components means the entire module should not be labeled a complex-I module.

#### NDUFAF4

- **Related proteins** (co-abundance neighbors): UAP1 (0.90); STRING partners: NDUFS4 (0.958)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase complex assembly factor 4. NADH:ubiquinone oxidoreductase (complex I) catalyzes the transfer of electrons from NADH to ubiquinone (coenzyme Q) in the first step of the mitochondrial respiratory chain, resulting in the translocation of protons across the inner mitochondrial membrane. This gene encodes a complex I assembly factor. Mutations in this gene are a cause of mitochondrial complex I deficiency. [provided by RefSeq, O…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.714); type 2 diabetes mellitus (0.607); mitochondrial disease (0.597); diabetes mellitus (0.578); mitochondrial complex I deficiency, nuclear type 15 (0.568)
- **Europe PMC papers**: 378
- **Why important**: NDUFAF4 has a direct high-confidence STRING relationship with NDUFS4 and is repeatedly represented with NDUFS4 in hu.MAP complex-I-related complexes (hu.MAP huMAP3_14018.1) through (hu.MAP huMAP3_14878.1). Its established function is assembly of mitochondrial respiratory complex I, and disease associations include mitochondrial complex-I deficiency and mitochondrial disease. Although it is not a broad network hub, its complex-specific evidence is unusually consistent.
- **Conclusion**: Established evidence supports NDUFAF4 as a complex-I assembly factor and validates a mitochondrial submodule together with NDUFS4. It is therefore an important mechanistic anchor, while its limited connectivity argues against treating it as evidence that the full co-abundance module is one mitochondrial complex.

## Module 6

**Tissue pair**: autonomic_nervous_system and testis  
**Genes (32)**: AKR1B1, ANXA2, ASPH, ASS1, CAPN5, CNPY2, CPNE1, CSRP1, HSD17B4, EFHD2, EZR, FAHD1, HNRNPL, EPHX1, IQGAP1, MTR, NUCB1, P4HA1, PRAF2, PFN2, CRYZ, RAD50, RRBP1, SEC23B, SEC24D, SCP2, SFXN3, SRI, SPTAN1, SARS1, TRNT1, EFTUD2

### Function

The most defensible interpretation is a calcium-dependent membrane, cytoskeletal, and intracellular-trafficking module, with linked contributions from peroxisomal lipid metabolism and RNA or protein processing. The primary enrichment evidence is (GO:MF calcium ion binding; q_global = 0.0457), calcium ion binding, supported by ANXA2, ASPH, CPNE1, EFHD2, IQGAP1, NUCB1, SPTAN1, and SRI. This is consistent with the functions of annexin A2, EF-hand proteins, spectrin, IQGAP1, nucleobindin, and sorcin. The network also contains a membrane-to-cytoskeleton branch involving ANXA2, EZR, IQGAP1, and SPTAN1, a COPII trafficking branch involving SEC23B and SEC24D, and a peroxisomal lipid-metabolism branch involving SCP2 and HSD17B4. Other genes indicate mitochondrial serine import, tRNA processing, splicing, DNA repair, and metabolic activity, so the module is biologically mixed rather than a narrowly defined pathway. No STRING functional-enrichment term was reported. Therefore, (GO:MF calcium ion binding; q_global = 0.0457) is the only primary GO or KEGG evidence, while the other interpretations are supported by gene functions and network structure rather than by globally corrected enrichment.

**Cell composition.** This does not look predominantly like a plasma-protein or secreted-protein module: the HPA summary identifies only a minority of secreted genes, and most proteins are intracellular or membrane-associated. It also does not show a dominant immune-cell signature, because most genes have low immune-cell specificity, although several genes are enhanced in neutrophils, monocytes, dendritic cells, basophils, or related immune contexts. The composition is heterogeneous and includes genes enhanced in liver, kidney, intestine, adrenal gland, esophagus, reproductive cells, and several epithelial or stromal cell types. Many genes have low tissue specificity and broad cellular roles. Thus, the shared signal may reflect common cellular machinery, tissue or cell-type mixtures, or sample-composition effects rather than a specialized autonomic-nervous-system and testis program. Testis protein detection is widespread in the supplied HPA data, but the absence of matching autonomic-nervous-system HPA tissue data prevents a direct protein-level comparison.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF calcium ion binding | 0.0457 | ANXA2, ASPH, CPNE1, EFHD2, IQGAP1, NUCB1, SPTAN1, SRI |

### STRING and hu.MAP

STRING provides a small set of high-confidence pairwise relationships rather than a dense interaction network. The strongest links are SEC23B-SEC24D, EZR-IQGAP1, HSD17B4-SCP2, and the connections of ANXA2 and IQGAP1 with cytoskeletal partners. These relationships independently support COPII vesicle trafficking, peroxisomal fatty-acid metabolism, and membrane-cytoskeleton organization. hu.MAP repeatedly places SEC23B and SEC24D together across several COPII-related complexes (hu.MAP huMAP3_00065.1) through (hu.MAP huMAP3_11128.1), (hu.MAP huMAP3_11237.1), (hu.MAP huMAP3_13535.1), and (hu.MAP huMAP3_12394.1), making that pair the clearest established complex signal. EZR and EFHD2 occur together in (hu.MAP huMAP3_10281.1), while ANXA2 and SPTAN1 occur together in (hu.MAP huMAP3_09165.1). However, these complexes contain many members outside the module, so the module captures partial complexes rather than a complete novel complex. The limited STRING coverage and the repeated hu.MAP recovery of known complexes favor a model of co-abundance among established cellular systems.

**STRING interactions (score >= 0.7)**: 5 of 496 gene pairs: ANXA2–EZR (0.725); EZR–IQGAP1 (0.938); HSD17B4–SCP2 (0.986); IQGAP1–SPTAN1 (0.753); SEC23B–SEC24D (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00065.1 (SEC24D, SEC23B; 2/4); huMAP3_00707.1 (SEC24D, SEC23B; 2/4); huMAP3_07775.1 (SEC24D, SEC23B; 2/5); huMAP3_06453.1 (SEC24D, SEC23B; 2/6); huMAP3_09282.1 (SEC24D, SEC23B; 2/6); huMAP3_11128.1 (SEC24D, SEC23B; 2/8); huMAP3_10281.1 (EZR, EFHD2; 2/9); huMAP3_11237.1 (SEC24D, SEC23B; 2/12); huMAP3_13535.1 (SEC24D, SEC23B; 2/14); huMAP3_09165.1 (ANXA2, SPTAN1; 2/39); huMAP3_12394.1 (SEC24D, SEC23B; 2/98)

### Novelty

The module may be novel as a cross-tissue co-abundance pattern, but the supplied evidence does not establish a new molecular pathway or complex. Several relationships are already known through STRING and hu.MAP, especially the SEC23B-SEC24D COPII pair, the EZR-IQGAP1 cytoskeletal relationship, the HSD17B4-SCP2 metabolic relationship, and the ANXA2-SPTAN1 complex context. Many member functions and disease associations are also well established, as indicated by the substantial literature attached to genes such as ANXA2, SRI, RAD50, MTR, and EZR. Conversely, the specific combination of calcium-binding, trafficking, cytoskeletal, peroxisomal, and reproductive-tissue co-abundance across autonomic nervous system and testis is not demonstrated by the supplied databases. Therefore the appropriate claim is a potentially novel module-level association that requires replication, tissue deconvolution, and independent validation; absence of a complete STRING or hu.MAP representation alone is not evidence of novelty.

**Hypothesis.** Hypothesis: in both autonomic nervous system and testis, this module coordinates calcium-sensitive membrane remodeling with vesicle trafficking and cytoskeletal organization, while supporting the metabolic and proteostatic demands of specialized cells. ANXA2, EZR, IQGAP1, EFHD2, and SPTAN1 could couple calcium-dependent membrane events to actin or spectrin structures; SEC23B and SEC24D could support ER-to-Golgi cargo export; and SCP2 with HSD17B4 could provide a linked peroxisomal lipid-metabolism component. This could be especially relevant to cell polarity, junctional organization, secretory handling, or spermatogenic cell architecture. The hypothesis remains provisional because the module is compositionally heterogeneous, the autonomic-nervous-system HPA protein comparison is unavailable, and the enrichment evidence is limited to (GO:MF calcium ion binding; q_global = 0.0457).

### Important genes

#### ANXA2

- **Related proteins** (co-abundance neighbors): CSRP1 (0.94), SEC23B (0.85), IQGAP1 (0.83), HNRNPL (0.81), SRI (0.81); STRING partners: EZR (0.725)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_09165.1
- **Function (MyGene.info)**: annexin A2. This gene encodes a member of the annexin family. Members of this calcium-dependent phospholipid-binding protein family play a role in the regulation of cellular growth and in signal transduction pathways. This protein functions as an autocrine factor which heightens osteoclast formation and bone resorption. This gene has three pseudogenes located on chromosomes 4, 9 and 10, respectively. Multiple…
- **Diseases (Open Targets)**: neurodegenerative disease (0.443); Alzheimer disease (0.312); Parkinson disease (0.298); lysosomal storage disease (0.289); benign urinary system neoplasm (0.270)
- **Europe PMC papers**: 12966
- **Why important**: ANXA2 is a central connector in the module, linked to CSRP1, SEC23B, IQGAP1, HNRNPL, and SRI. It is included in (GO:MF calcium ion binding; q_global = 0.0457), is a calcium-dependent phospholipid-binding protein, and is annotated for membrane-raft assembly, receptor recycling, vesicle budding, and cell adhesion. STRING links it to EZR, and hu.MAP places it with SPTAN1 in (hu.MAP huMAP3_09165.1). HPA describes plasma-membrane localization, secretion to blood, and enhancement in epithelial and several immune-cell contexts. Its disease literature is substantial.
- **Conclusion**: Established: ANXA2 is a strong candidate bridge between calcium-dependent membrane behavior, trafficking, adhesion, and the cytoskeleton. Hypothesis: it may help organize the shared module's membrane-remodeling arm in both tissues, although blood or epithelial contributions could also explain part of its co-abundance.

#### IQGAP1

- **Related proteins** (co-abundance neighbors): P4HA1 (0.84), CSRP1 (0.84), ANXA2 (0.83), NUCB1 (0.82); STRING partners: EZR (0.938), SPTAN1 (0.753)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IQ motif containing GTPase activating protein 1. This gene encodes a member of the IQGAP family. The protein contains four IQ domains, one calponin homology domain, one Ras-GAP domain and one WW domain. It interacts with components of the cytoskeleton, with cell adhesion molecules, and with several signaling molecules to regulate cell morphology and motility. Expression of the protein is upregulated by gene amplification in two gastric cancer ce…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.515); Costello syndrome (0.503); allergic rhinitis (0.474)
- **Europe PMC papers**: 3787
- **Why important**: IQGAP1 connects ANXA2, EZR, CSRP1, P4HA1, and NUCB1 and is included in (GO:MF calcium ion binding; q_global = 0.0457). Its annotated domains and functions connect cytoskeletal regulation, cell adhesion, cell morphology, motility, and signaling. It has strong STRING links to EZR and SPTAN1, placing it at the best-supported membrane-cytoskeleton junction in the module. HPA places it at the plasma membrane and cell junctions, with enhancement in neutrophils. It has broad disease and signaling literature.
- **Conclusion**: Established: IQGAP1 is a plausible structural and signaling hub that integrates calcium-associated membrane proteins with cytoskeletal organization. Hypothesis: it may translate calcium-sensitive membrane events into changes in cell shape or junctional behavior shared by autonomic and testicular cells.

#### SEC23B

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.89), ANXA2 (0.85), SCP2 (0.83), CRYZ (0.82), SFXN3 (0.81), EZR (0.81); STRING partners: SEC24D (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Vesicles, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_00065.1, huMAP3_00707.1, huMAP3_07775.1, huMAP3_06453.1, huMAP3_09282.1, huMAP3_11128.1, huMAP3_11237.1, huMAP3_13535.1, huMAP3_12394.1
- **Function (MyGene.info)**: SEC23 homolog B, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The function of this gene product has been implicated in cargo selection and concentration. Multiple alternativel…
- **Diseases (Open Targets)**: congenital dyserythropoietic anemia type 2 (0.834); Cowden syndrome 7 (0.730); congenital dyserythropoietic anemia (0.438); hereditary disease (0.194); hereditary ataxia (0.118)
- **Europe PMC papers**: 847
- **Why important**: SEC23B is connected to several module genes and forms the clearest established trafficking relationship with SEC24D in STRING. It is present with SEC24D in the repeated hu.MAP complexes (hu.MAP huMAP3_00065.1) through (hu.MAP huMAP3_11128.1), (hu.MAP huMAP3_11237.1), (hu.MAP huMAP3_13535.1), and (hu.MAP huMAP3_12394.1). Its established function is COPII vesicle budding, cargo selection, and ER-to-Golgi transport. HPA places it in the ER, vesicles, and cytosol, and it has disease associations involving congenital dyserythropoietic anemia and related disorders.
- **Conclusion**: Established: SEC23B supplies strong evidence that the module includes canonical ER export machinery rather than only a correlation-defined cytoskeletal signal. Hypothesis: coordinated COPII activity may support membrane-protein or secretory cargo handling in the shared cell populations.

#### SCP2

- **Related proteins** (co-abundance neighbors): RAD50 (0.90), SFXN3 (0.87), EFHD2 (0.87), CRYZ (0.85), EPHX1 (0.84), SPTAN1 (0.84), SEC23B (0.83), HSD17B4 (0.82), SRI (0.81); STRING partners: HSD17B4 (0.986)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Peroxisomes; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sterol carrier protein 2. This gene encodes two proteins: sterol carrier protein X (SCPx) and sterol carrier protein 2 (SCP2), as a result of transcription initiation from 2 independently regulated promoters. The transcript initiated from the proximal promoter encodes the longer SCPx protein, and the transcript initiated from the distal promoter encodes the shorter SCP2 protein, with the 2 proteins sharing a common C-termi…
- **Diseases (Open Targets)**: sterol carrier protein 2 deficiency (0.708); spermatogenic failure (0.191); stroke disorder (0.187); alcohol drinking (0.186); leukodystrophy (0.119)
- **Europe PMC papers**: 2268
- **Why important**: SCP2 has one of the strongest network positions and connects CRYZ, SFXN3, EFHD2, EPHX1, SPTAN1, SEC23B, and HSD17B4. STRING gives strong support for the HSD17B4-SCP2 relationship. SCP2 encodes proteins associated with peroxisomes and is annotated for fatty-acid beta-oxidation, steroid and bile-acid metabolism, and progesterone biosynthesis. HPA shows liver enhancement and peroxisomal localization, with detection in testis. Its deficiency has a direct disease association and it has a substantial literature.
- **Conclusion**: Established: SCP2 identifies a metabolic and peroxisomal component that is particularly relevant to lipid and steroid handling. Hypothesis: this metabolic arm may support membrane remodeling or reproductive-cell function, but its presence could also reflect shared liver-like or broadly metabolic cell states rather than a tissue-pair-specific mechanism.

#### SPTAN1

- **Related proteins** (co-abundance neighbors): RAD50 (0.88), RRBP1 (0.84), SCP2 (0.84), HNRNPL (0.81), CSRP1 (0.80), NUCB1 (0.80); STRING partners: IQGAP1 (0.753)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Microtubules; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_09165.1
- **Function (MyGene.info)**: spectrin alpha, non-erythrocytic 1. Spectrins are a family of filamentous cytoskeletal proteins that function as essential scaffold proteins that stabilize the plasma membrane and organize intracellular organelles. Spectrins are composed of alpha and beta dimers that associate to form tetramers linked in a head-to-head arrangement. This gene encodes an alpha spectrin that is specifically expressed in nonerythrocytic cells. The encod…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 5 (0.749); developmental delay with or without epilepsy (0.681); spastic paraplegia 91, autosomal dominant, with or without cerebellar ataxia (0.681); infantile spasms (0.651); genetic developmental and epileptic encephalopathy (0.651)
- **Europe PMC papers**: 1422
- **Why important**: SPTAN1 is a network connector linked to RAD50, RRBP1, SCP2, HNRNPL, CSRP1, and NUCB1. It is one of the genes in (GO:MF calcium ion binding; q_global = 0.0457), is annotated as a non-erythrocytic spectrin, and supports membrane stabilization and intracellular-organellar organization through the actin cytoskeleton. It connects to IQGAP1 in STRING and to ANXA2 in hu.MAP complex (hu.MAP huMAP3_09165.1). It has well documented associations with developmental and epileptic encephalopathy and other neurological disorders, making it particularly relevant to the autonomic-nervous-system side.
- **Conclusion**: Established: SPTAN1 provides a strong cytoskeletal scaffold interpretation and links the module to neurological disease biology. Hypothesis: it may stabilize calcium-responsive membrane and vesicle structures in the shared module, but the co-abundance result does not prove a direct functional interaction in either tissue.

## Module 7

**Tissue pair**: autonomic_nervous_system and testis  
**Genes (43)**: ANXA7, AP2B1, APOB, BABAM2, MTHFD1, CAPRIN1, CPNE3, DSTN, DHRS7, DHX9, DNM1L, DPYSL3, EXOC4, FKBP15, GSTM2, COLGALT1, GMPS, HERC4, HNRNPK, IPO11, KIF21A, PRKCA, LNPEP, MYLK, NASP, NBAS, PPP4R3A, PDCD4, PDLIM5, PI4KA, PPM1B, RO60, SCAMP2, SH3GLB2, SNTB2, SNX4, IARS1, TAGLN2, TRAP1, TRIM25, TXNRD1, USP5, XPO1

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent; therefore the module does not support a statistically established single pathway-level function. Its gene-level annotations and network architecture instead suggest a composite intracellular program involving vesicle and membrane trafficking, actin-dependent structure and contractility, RNA processing and transport, nucleotide production, protein quality control, and cellular stress handling. The strongest network-connected components include NBAS with trafficking-related neighbors, MYLK with cytoskeletal and contractile associations, HNRNPK and DHX9 with RNA metabolism relationships, and MTHFD1 with GMPS in purine-related complex structure. These convergent annotations support a cautious interpretation as a cellular maintenance and remodeling module rather than a narrowly defined biological pathway.

**Cell composition.** The HPA profile argues against this being primarily a plasma-protein or secreted-protein module: only a small subset is secreted, and APOB is the clearest blood-secreted component. Most genes have low tissue specificity, while many are detected in testis and several show enhancement in spermatogenic cell types. The module also contains genes enhanced in smooth muscle, cardiomyocytes, neural or glial populations, epithelial cells, and several blood-cell types. Thus the shared signal may reflect broadly expressed cellular machinery combined with cell-type composition, especially germ-cell or supporting-cell representation in testis; a blood contribution is possible but is not the dominant explanation from the HPA summary. There is no matching HPA tissue protein evidence for the autonomic nervous system, so the tissue-level interpretation should remain cautious.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The listed high-confidence STRING relationships provide a small set of already known connections: CAPRIN1 with DHX9, DHX9 with HNRNPK and XPO1, and GMPS with MTHFD1. These relationships reinforce two local neighborhoods, one involving RNA handling and nucleocytoplasmic transport and another involving purine-associated metabolism. The absence of STRING functional enrichment means these known links do not establish a unified pathway for the whole module. hu.MAP provides additional support for the MTHFD1–GMPS pair through complexes C1 and C2, and places GMPS with TRAP1 in the broader complex C3. Because the hu.MAP complexes contain many members outside the module, they support shared biochemical or proteostatic context rather than a module-specific complex. Most co-abundance edges are not represented by the supplied STRING or hu.MAP evidence, so the network likely captures coordinated abundance beyond currently catalogued physical interactions.

**STRING interactions (score >= 0.7)**: 4 of 903 gene pairs: CAPRIN1–DHX9 (0.705); DHX9–HNRNPK (0.939); DHX9–XPO1 (0.791); GMPS–MTHFD1 (0.879)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13695.1 (MTHFD1, GMPS; 2/4); huMAP3_12823.1 (MTHFD1, GMPS; 2/7); huMAP3_14442.1 (GMPS, TRAP1; 2/57)

### Novelty

This appears to be a potentially interesting tissue-pair co-abundance finding, but it cannot be called a newly discovered molecular complex or pathway. The module combines established processes and includes several relationships already documented by STRING or hu.MAP, while most of its co-abundance links lack matching interaction evidence. The failed global GO/KEGG enrichment and lack of STRING functional enrichment also argue against claiming a previously unrecognized canonical pathway. A defensible novelty claim is therefore limited to the cross-tissue co-abundance pattern linking autonomic nervous system and testis, subject to replication in independent cohorts and control for cell composition. Absence from STRING or hu.MAP alone does not demonstrate novelty.

**Hypothesis.** Hypothesis: the module reflects coordinated support of highly active or differentiating cells through coupled vesicle trafficking, cytoskeletal remodeling, RNA handling, nucleotide supply, and stress protection. In testis, this could support germ-cell development and changing membrane, chromatin, and translational demands, with GMPS and MTHFD1 contributing biosynthetic capacity, HNRNPK and DHX9 regulating RNA fate, and NBAS, EXOC4, SNX4, and AP2B1 supporting intracellular trafficking. In autonomic nervous system samples, the same machinery could be recruited for neuronal or glial membrane turnover, synaptic or axonal transport, and actin-dependent remodeling. The apparent conservation may therefore arise from shared cellular demands rather than a tissue-specific autonomic–testis pathway. This hypothesis should be tested by cell-resolved analysis, perturbation of hub genes, and validation of protein-level co-localization.

### Important genes

#### MTHFD1

- **Related proteins** (co-abundance neighbors): EXOC4 (0.83), HNRNPK (0.83), MYLK (0.83), AP2B1 (0.81), SNTB2 (0.80); STRING partners: GMPS (0.879)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_13695.1, huMAP3_12823.1
- **Function (MyGene.info)**: methylenetetrahydrofolate dehydrogenase, cyclohydrolase and formyltetrahydrofolate synthetase 1. This gene encodes a protein that possesses three distinct enzymatic activities, 5,10-methylenetetrahydrofolate dehydrogenase, 5,10-methenyltetrahydrofolate cyclohydrolase and 10-formyltetrahydrofolate synthetase. Each of these activities catalyzes one of three sequential reactions in the interconversion of 1-carbon derivatives of tetrahydrofolate, which are substrates for methionine, thymidylate, …
- **Diseases (Open Targets)**: combined immunodeficiency and megaloblastic anemia with or without hyperhomocysteinemia (0.773); severe combined immunodeficiency (0.473); neural tube defects, folate-sensitive (0.414); isolated spina bifida (0.376); atrial fibrillation (0.332)
- **Europe PMC papers**: 1939
- **Why important**: MTHFD1 is a highly connected module member and is linked to MYLK, HNRNPK, EXOC4, AP2B1, and SNTB2. It is the multifunctional folate-pathway enzyme supporting one-carbon reactions relevant to methionine, thymidylate, and purine synthesis. It is present in hu.MAP complexes C1 and C2 with GMPS, has testis protein detection, and shows liver tissue enrichment plus several metabolically active cell-type associations. Its disease associations include combined immunodeficiency and megaloblastic anemia and folate-sensitive developmental disorders, while its literature coverage is substantial.
- **Conclusion**: Established evidence supports MTHFD1 as a metabolic and biosynthetic anchor of the module and as part of a known complex relationship with GMPS. The hypothesis that it couples biosynthetic demand to trafficking or cytoskeletal remodeling in this tissue pair remains unproven.

#### GMPS

- **Related proteins** (co-abundance neighbors): NASP (0.82), PI4KA (0.80); STRING partners: MTHFD1 (0.879)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13695.1, huMAP3_12823.1, huMAP3_14442.1
- **Function (MyGene.info)**: guanosine monophosphate synthase. In the de novo synthesis of purine nucleotides, IMP is the branch point metabolite at which point the pathway diverges to the synthesis of either guanine or adenine nucleotides. In the guanine nucleotide pathway, there are 2 enzymes involved in converting IMP to GMP, namely IMP dehydrogenase (IMPD1), which catalyzes the oxidation of IMP to XMP, and GMP synthetase, which catalyzes the amination of …
- **Diseases (Open Targets)**: rheumatoid arthritis (0.277); nephrotic syndrome (0.259); lupus nephritis (0.259); rhabdomyosarcoma (0.247); hepatocellular carcinoma (0.237)
- **Europe PMC papers**: 5161
- **Why important**: GMPS connects to NASP and PI4KA in the module and has the clearest complex and STRING support: it pairs with MTHFD1 in STRING and occurs in hu.MAP complexes C1, C2, and C3. Its established function is conversion of an intermediate toward GMP in de novo purine synthesis. HPA identifies testis tissue enhancement and enhancement in early and late spermatogenic cell types, making it particularly relevant to the testis side of the shared module. It also has extensive literature and disease associations involving immune and neoplastic conditions.
- **Conclusion**: Established evidence supports GMPS as a testis-relevant purine biosynthesis component with reproducible complex context. It is plausible, but not demonstrated, that coordinated GMPS abundance supplies nucleotide demand during germ-cell differentiation or neuronal cellular maintenance.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): MYLK (0.92), COLGALT1 (0.86), MTHFD1 (0.83), PDLIM5 (0.82), AP2B1 (0.81); STRING partners: DHX9 (0.939)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is among the more connected genes and links MYLK, COLGALT1, MTHFD1, PDLIM5, and AP2B1. It is a broadly expressed RNA-binding protein involved in pre-mRNA processing, RNA transport, and transcriptional regulation. The STRING relationship with DHX9 is strong within the supplied evidence, connecting this module neighborhood to RNA helicase activity and nucleocytoplasmic RNA handling. HNRNPK is detected in testis, has major developmental and neurodevelopmental disease associations, and has a substantial literature base.
- **Conclusion**: Established evidence supports HNRNPK as an RNA-processing hub that may help explain coordinated abundance across dissimilar tissues. Its proposed role as a bridge between RNA regulation and the module's membrane or contractile features is a hypothesis rather than a demonstrated mechanism.

#### MYLK

- **Related proteins** (co-abundance neighbors): PDLIM5 (0.92), HNRNPK (0.92), COLGALT1 (0.87), MTHFD1 (0.83), RO60 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin light chain kinase. This gene, a muscle member of the immunoglobulin gene superfamily, encodes myosin light chain kinase which is a calcium/calmodulin dependent enzyme. This kinase phosphorylates myosin regulatory light chains to facilitate myosin interaction with actin filaments to produce contractile activity. This gene encodes both smooth muscle and nonmuscle isoforms. In addition, using a separate promoter in an …
- **Diseases (Open Targets)**: aortic aneurysm, familial thoracic 7 (0.767); familial thoracic aortic aneurysm and aortic dissection (0.710); megacystis-microcolon-intestinal hypoperistalsis syndrome 1 (0.617); megacystis-microcolon-intestinal hypoperistalsis syndrome (0.597); Rare genetic vascular disease (0.483)
- **Europe PMC papers**: 10503
- **Why important**: MYLK has high network connectivity and links PDLIM5, HNRNPK, COLGALT1, MTHFD1, and RO60. Its established enzymatic function is calcium and calmodulin-dependent phosphorylation of myosin regulatory light chains, supporting actomyosin contractility and cell migration. HPA shows enhancement in seminal vesicle and smooth muscle and in peritubular myoid cells, among other contractile or platelet-associated cell types. Its disease associations prominently include vascular disorders, and it has the largest literature volume among the selected genes.
- **Conclusion**: Established evidence supports MYLK as a cytoskeletal and contractility anchor, especially relevant to smooth-muscle or peritubular testicular cells and potentially autonomic tissue architecture. A direct functional partnership between MYLK and the RNA or folate-related components is not established by the supplied interaction databases.

#### NBAS

- **Related proteins** (co-abundance neighbors): FKBP15 (0.91), EXOC4 (0.88), HERC4 (0.86), PPP4R3A (0.83), NASP (0.82), SNX4 (0.82), PDCD4 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NBAS subunit of NRZ tethering complex. This gene encodes a protein with two leucine zipper domains, a ribosomal protein S14 signature domain and a Sec39 like domain. The protein is thought to be involved in Golgi-to-ER transport. Mutations in this gene are associated with short stature, optic nerve atrophy, and Pelger-Huet anomaly. [provided by RefSeq, Oct 2012].
- **Diseases (Open Targets)**: infantile liver failure syndrome 2 (0.817); short stature-optic atrophy-Pelger-Huët anomaly syndrome (0.793); infantile liver failure (0.548); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.546); hereditary optic neuropathy (0.421)
- **Europe PMC papers**: 2184
- **Why important**: NBAS has the strongest network position in the supplied module and connects FKBP15, EXOC4, HERC4, PPP4R3A, NASP, SNX4, and PDCD4. Its established role involves the NRZ tethering complex and retrograde Golgi-to-endoplasmic-reticulum transport, with additional annotation related to RNA surveillance. It is broadly expressed, detected in testis, and associated with infantile liver failure and short stature with optic atrophy and Pelger-Huët anomaly. Its substantial literature volume supports relatively mature functional interpretation even though no STRING or hu.MAP relationship was supplied for NBAS.
- **Conclusion**: Established evidence supports NBAS as a trafficking and intracellular homeostasis hub that could organize several peripheral module neighborhoods. Its role as the principal structural coordinator of this tissue-pair module remains a hypothesis based on co-abundance topology, not a proven physical assembly.

## Module 8

**Tissue pair**: autonomic_nervous_system and testis  
**Genes (5)**: LDAH, NT5DC1, RAB10, RAB5B, RAB5C

### Function

The strongest functional interpretation is a conserved endosomal and vesicle-trafficking module centered on Rab small GTPase activity. The primary, globally corrected evidence is (GO:MF G protein activity; q_global = 0.015) G protein activity and (GO:MF GDP binding; q_global = 0.0232) GDP binding, both driven by RAB10, RAB5B, and RAB5C. The supplementary STRING terms support Rab-family identity, Rab geranylgeranylation, GEF-mediated nucleotide exchange, prenylation, and vesicle tethering (9 supplementary STRING terms; within-query FDR 0.001–0.0448). Gene-level annotations further support endocytosis and endosomal transport for RAB5B and RAB5C, and exocytosis, Golgi-to-plasma-membrane transport, axonogenesis, and vesicle-mediated transport for RAB10. LDAH contributes a lipid-droplet and intracellular lipid-homeostasis signal, while NT5DC1 remains functionally less defined. Thus, the best-supported interpretation is coordinated intracellular membrane trafficking, with a possible link to lipid handling. The GO/KEGG evidence is specific to molecular function; it does not by itself establish a tissue-specific physiological process.

**Cell composition.** This is not a plasma-protein or secreted-protein module: HPA reports no secreted genes, low immune-cell specificity for every gene, and no enrichment of blood-cell classes. Four genes have low tissue specificity, while NT5DC1 is tissue-enhanced in choroid plexus and cell-type enhanced in choroid plexus epithelial cells and oligodendrocytes. Several genes show cell-type enhancement in epithelial populations, and RAB5C is enhanced in spermatid and spermatocyte populations. Protein detection is reported for four genes in testis, with no matching autonomic-nervous-system HPA tissue available. These observations argue against a simple blood-contamination explanation, but they do support a cautious interpretation in which shared vesicle-trafficking programs, common cell types, or broad cellular machinery contribute to the cross-tissue signal.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF G protein activity | 0.015 | RAB10, RAB5B, RAB5C |
| GO:MF GDP binding | 0.0232 | RAB10, RAB5B, RAB5C |

### STRING and hu.MAP

The direct STRING evidence is concentrated in the RAB5B–RAB5C relationship, which is a high-confidence known interaction. The remaining module pairs lack high-confidence STRING links, so the co-abundance network should not be interpreted as a fully established physical interaction network. Nevertheless, STRING functional enrichment consistently identifies the three Rab proteins and supports Rab activation, prenylation, geranylgeranylation, and vesicle tethering (9 supplementary STRING terms; within-query FDR 0.001–0.0448). hu.MAP independently places RAB10, RAB5B, and RAB5C together in several Rab trafficking complexes (hu.MAP huMAP3_08941.1) (hu.MAP huMAP3_09217.1) (hu.MAP huMAP3_11094.1), while RAB5B–RAB5C recur in additional smaller complexes (hu.MAP huMAP3_07239.1) (hu.MAP huMAP3_05480.1) and RAB10–RAB5C in another broad complex (hu.MAP huMAP3_11860.1). These complexes contain many other Rab proteins, regulators, and trafficking factors, so they provide contextual support for a shared Rab-system program rather than proof that every module edge is a direct binding interaction. LDAH and NT5DC1 have no reported STRING partners or hu.MAP complexes in the supplied evidence, making their network linkage more novel and more dependent on the co-abundance result.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: RAB5B–RAB5C (0.966)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Rab subfamily of small GTPases (FDR = 0.001, 3 genes); Function G protein activity (FDR = 0.0014, 3 genes); RCTM RAB geranylgeranylation (FDR = 0.0074, 3 genes); RCTM RAB GEFs exchange GTP for GDP on RABs (FDR = 0.0082, 3 genes); Keyword Prenylation (FDR = 0.0107, 3 genes); Function GDP binding (FDR = 0.011, 3 genes); InterPro Small GTPase (FDR = 0.0125, 3 genes); InterPro Small GTP-binding protein domain (FDR = 0.0225, 3 genes); NetworkNeighborAL Mixed, incl. RAB geranylgeranylation, and Vesicle tethering complex (FDR = 0.0448, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08941.1 (RAB5C, RAB5B, RAB10; 3/28); huMAP3_09217.1 (RAB5C, RAB5B, RAB10; 3/29); huMAP3_11094.1 (RAB5C, RAB5B, RAB10; 3/43); huMAP3_07239.1 (RAB5C, RAB5B; 2/3); huMAP3_05480.1 (RAB5C, RAB5B; 2/4); huMAP3_11860.1 (RAB5C, RAB10; 2/44)

### Novelty

The module is not a wholly new biological mechanism: Rab-mediated endosomal trafficking, nucleotide exchange, prenylation, and vesicle tethering are established biology, and the Rab relationships are represented in STRING and hu.MAP. What may be novel is the coordinated co-abundance of this Rab-centered program with LDAH and NT5DC1 across autonomic nervous system and testis. That cross-tissue module-level association is not demonstrated by the database annotations alone. Its novelty should therefore be stated as a potentially new systems-level observation requiring replication, tissue and cell-composition controls, and experimental validation. Absence of database links for LDAH or NT5DC1 is not sufficient to claim a new interaction or mechanism.

**Hypothesis.** Hypothesis: in a shared cell population or shared cellular state present in autonomic nervous system and testis, coordinated expression of RAB5B, RAB5C, and RAB10 supports endosomal uptake, sorting, recycling, and exocytic delivery, while LDAH links this trafficking state to lipid-droplet or membrane-lipid homeostasis and NT5DC1 may mark or modulate a nucleotide-related cellular state. This model is consistent with the globally significant Rab molecular-function terms (GO:MF G protein activity; q_global = 0.015) and (GO:MF GDP binding; q_global = 0.0232), the STRING trafficking evidence (9 supplementary STRING terms; within-query FDR 0.001–0.0448), and the hu.MAP Rab-complex context (hu.MAP huMAP3_08941.1) (hu.MAP huMAP3_09217.1) (hu.MAP huMAP3_11094.1) (hu.MAP huMAP3_07239.1) (hu.MAP huMAP3_05480.1) (hu.MAP huMAP3_11860.1). The proposed roles of LDAH and NT5DC1 in coupling the Rab program to lipid or nucleotide biology are hypotheses, not established conclusions from the supplied data.

### Important genes

#### RAB5B

- **Related proteins** (co-abundance neighbors): LDAH (0.84), RAB5C (0.81); STRING partners: RAB5C (0.966)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_08941.1, huMAP3_09217.1, huMAP3_11094.1, huMAP3_07239.1, huMAP3_05480.1
- **Function (MyGene.info)**: RAB5B, member RAS oncogene family. Enables GDP binding activity; GTP-dependent protein binding activity; and GTPase activity. Involved in antigen processing and presentation and plasma membrane to endosome transport. Located in endosome and extracellular exosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypothyroidism (0.358); gastroesophageal reflux disease (0.331); neurodegenerative disease (0.319); smoking cessation (0.293); type 1 diabetes mellitus (0.289)
- **Europe PMC papers**: 1334
- **Why important**: RAB5B is a central bridge in the module, connecting LDAH to RAB5C, and it is one of the three genes driving both primary globally corrected terms (GO:MF G protein activity; q_global = 0.015) and (GO:MF GDP binding; q_global = 0.0232). It is also supported by every listed STRING functional term (9 supplementary STRING terms; within-query FDR 0.001–0.0448), has a direct high-confidence STRING relationship with RAB5C, and appears in multiple hu.MAP complexes (hu.MAP huMAP3_08941.1) (hu.MAP huMAP3_09217.1) (hu.MAP huMAP3_11094.1) (hu.MAP huMAP3_07239.1) (hu.MAP huMAP3_05480.1). Its annotations support endocytosis, endosomal transport, plasma-membrane-to-endosome transport, and antigen processing. Its substantial literature volume and disease-linked evidence make it one of the best-established anchors.
- **Conclusion**: Established evidence identifies RAB5B as a Rab-family nucleotide-binding and endosomal-trafficking component that is strongly supported by both enrichment and external interaction resources. A module-specific role in coordinating LDAH with the other Rab proteins is plausible from the network position but remains a hypothesis.

#### RAB5C

- **Related proteins** (co-abundance neighbors): RAB5B (0.81); STRING partners: RAB5B (0.966)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endosomes; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_08941.1, huMAP3_09217.1, huMAP3_11094.1, huMAP3_07239.1, huMAP3_05480.1, huMAP3_11860.1
- **Function (MyGene.info)**: RAB5C, member RAS oncogene family. Members of the Rab protein family are small GTPases of the Ras superfamily that are thought to ensure fidelity in the process of docking and/or fusion of vesicles with their correct acceptor compartment (Han et al., 1996 [PubMed 8646882]).[supplied by OMIM, Nov 2010].
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.508); hypothyroidism (0.391); hereditary disease (0.336); autoimmune thyroid disease (0.264); myxedema (0.213)
- **Europe PMC papers**: 1368
- **Why important**: RAB5C is the most strongly externally supported physical-interaction node in the module because it forms the high-confidence STRING pair with RAB5B and occurs in all supplied hu.MAP complexes (hu.MAP huMAP3_08941.1) (hu.MAP huMAP3_09217.1) (hu.MAP huMAP3_11094.1) (hu.MAP huMAP3_07239.1) (hu.MAP huMAP3_05480.1) (hu.MAP huMAP3_11860.1). It drives both primary terms (GO:MF G protein activity; q_global = 0.015) and (GO:MF GDP binding; q_global = 0.0232) and all supplementary STRING terms (9 supplementary STRING terms; within-query FDR 0.001–0.0448). Its established annotations place it in endosomes and implicate it in intracellular protein transport, endocytosis, endosomal transport, and plasma-membrane-to-endosome transport. HPA additionally shows enhancement in spermatid and spermatocyte populations, which is relevant to the testis side of the shared module.
- **Conclusion**: Established evidence supports RAB5C as a core endosomal Rab component and the strongest physical-network anchor. Its association with germ-cell populations may help explain the testis signal, but whether it has a specialized role in the cross-tissue module is not established.

#### RAB10

- **Related proteins** (co-abundance neighbors): NT5DC1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_08941.1, huMAP3_09217.1, huMAP3_11094.1, huMAP3_11860.1
- **Function (MyGene.info)**: RAB10, member RAS oncogene family. RAB10 belongs to the RAS (see HRAS; MIM 190020) superfamily of small GTPases. RAB proteins localize to exocytic and endocytic compartments and regulate intracellular vesicle trafficking (Bao et al., 1998 [PubMed 9918381]).[supplied by OMIM, Mar 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.549); digestive system disorder (0.242); cervical carcinoma (0.215); lobular capilliary hemangioma (0.165); hepatocellular carcinoma (0.109)
- **Europe PMC papers**: 2856
- **Why important**: RAB10 drives both primary terms (GO:MF G protein activity; q_global = 0.015) and (GO:MF GDP binding; q_global = 0.0232) and all supplementary Rab-related STRING terms (9 supplementary STRING terms; within-query FDR 0.001–0.0448). It connects to NT5DC1 in the co-abundance graph and appears with the other Rab proteins in several hu.MAP complexes (hu.MAP huMAP3_08941.1) (hu.MAP huMAP3_09217.1) (hu.MAP huMAP3_11094.1) and (hu.MAP huMAP3_11860.1), despite lacking a supplied direct STRING partner. Its annotations support exocytosis, Golgi-to-plasma-membrane transport, endosomal transport, vesicle-mediated transport, and axonogenesis, making it especially relevant to a module shared with autonomic nervous system tissue. It also has the largest literature volume among the module genes and disease associations involving neurodegenerative disease.
- **Conclusion**: Established evidence supports RAB10 as a broad vesicle-trafficking and exocytic component with plausible relevance to neuronal biology. Its connection to NT5DC1 and its cross-tissue coordination with the RAB5 proteins are network-level observations, not proof of a direct molecular interaction.

#### LDAH

- **Related proteins** (co-abundance neighbors): NT5DC1 (0.86), RAB5B (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lipid droplet associated hydrolase. Predicted to enable lipase activity. Predicted to be involved in lipid storage. Predicted to be located in endoplasmic reticulum. Predicted to be active in lipid droplet. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: metabolic disease (0.280); luminal A breast carcinoma (0.254); hyperlipidemia (0.250); chronic pancreatitis (0.210); cervical carcinoma (0.202)
- **Europe PMC papers**: 756
- **Why important**: LDAH has the highest weighted network strength and connects both to NT5DC1 and RAB5B, placing it at the interface between the Rab-centered portion of the module and the less characterized genes. Its supplied functional annotations associate it with lipase activity, lipid storage, lipid-droplet organization, intracellular triglyceride homeostasis, cholesterol homeostasis, and lipid-droplet fusion. It has testis protein detection and a substantial literature volume, while lacking STRING partners, hu.MAP complexes, or enrichment-term assignments in the supplied evidence.
- **Conclusion**: Established evidence supports LDAH as a lipid-droplet and lipid-homeostasis-associated protein with a prominent position in this co-abundance network. Its possible coupling to endosomal trafficking is a hypothesis based on network placement and must not be treated as an established biochemical function.

#### NT5DC1

- **Related proteins** (co-abundance neighbors): LDAH (0.86), RAB10 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 5'-nucleotidase domain containing 1. While the exact function of the protein encoded by this gene is not known, it belongs to the 5'(3')-deoxyribonucleotidase family. [provided by RefSeq, May 2010].
- **Diseases (Open Targets)**: Schmid metaphyseal chondrodysplasia (0.552); osteoarthritis, hip (0.447); osteoarthritis, knee (0.355); Progressive visual loss (0.331); refractive error (0.329)
- **Europe PMC papers**: 169
- **Why important**: NT5DC1 has nearly the highest weighted network strength and bridges LDAH to RAB10, making it structurally important despite having no supplied STRING or hu.MAP support. HPA identifies tissue enhancement in choroid plexus and cell-type enhancement in choroid plexus epithelial cells and oligodendrocytes. The supplied annotation places it in the five-prime or three-prime deoxyribonucleotidase family but explicitly states that its exact function is unknown. Its disease associations include skeletal and visual phenotypes, although these do not establish a role in this module.
- **Conclusion**: Established evidence supports NT5DC1 as a functionally incompletely characterized nucleotide-related protein with a distinctive network position and tissue pattern. Its proposed role as a link between nucleotide biology and Rab or lipid trafficking is currently a hypothesis, not a demonstrated mechanism.
