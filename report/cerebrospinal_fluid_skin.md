# Conserved co-abundance modules: cerebrospinal_fluid and skin

## Module 1

**Tissue pair**: cerebrospinal_fluid and skin  
**Genes (6)**: CD276, NRCAM, PLBD2, ACP2, SOD2, TFRC

### Function

No GO or KEGG term passed global correction, and there were no supplementary STRING enrichment terms. The module therefore does not support a statistically established single pathway-level function. Its gene content is heterogeneous: NRCAM suggests neuronal adhesion, axon guidance and cell-cell signaling; TFRC supports iron uptake and receptor-mediated endocytosis; PLBD2 suggests phospholipid catabolism; ACP2 suggests lysosomal biology; CD276 suggests immune and T-cell regulation; and SOD2 suggests mitochondrial oxidative-stress control. The network is organized around NRCAM, with the other genes connected to it directly or through PLBD2, but the lack of external interaction support makes a common molecular function uncertain. The most defensible interpretation is a cross-tissue co-abundance signature combining cell-contact or signaling biology with vesicular, lysosomal, immune and stress-related processes, rather than a validated conserved biochemical complex.

**Cell composition.** The module is not convincingly a predominantly plasma-protein module, although the HPA summary reports secreted annotation for several members. Its composition is heterogeneous and includes intracellular, membrane, vesicular, mitochondrial and blood-associated proteins. Three genes have low tissue specificity, while the remaining genes are tissue enhanced, most often in adrenal gland, brain, retina or bone marrow. Five genes show cell-type enhancement or enrichment, including monocytes, Hofbauer cells, adrenal cells, astrocytes, glia, neurons and late spermatids. Immune-cell enrichment or enhancement is present for several genes, while another is not detected in immune cells and one has low immune-cell specificity. Skin protein detection is available for most members, whereas the CSF HPA protein field has no matching data. These patterns raise the possibility that the shared signal reflects blood or immune-cell carryover, vascular or stromal contributions, or shared cell types in the sampled tissues. TFRC, ACP2 and SOD2 also fit broadly distributed cellular functions, so a housekeeping or general cellular-stress component cannot be excluded. The module should therefore not be interpreted as tissue-specific biology without controlling for sample composition.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair met the stated high-confidence STRING interaction threshold, and no STRING functional-enrichment term was reported. No hu.MAP complex contained multiple module members. The co-abundance edges are therefore not corroborated by the supplied protein-interaction or complex resources. The strongest internal connectivity is centered on NRCAM, which links to TFRC, PLBD2, CD276 and SOD2, while PLBD2 links to ACP2. This topology indicates a reproducible statistical co-abundance pattern within the module, but not an established physical complex. Known individual functions remain informative: NRCAM is a neuronal cell-adhesion molecule, TFRC mediates iron uptake, PLBD2 is associated with phospholipid catabolism, ACP2 is lysosomal, CD276 regulates immune signaling, and SOD2 detoxifies mitochondrial superoxide. These annotations support several plausible biological themes but do not establish direct molecular relationships among the encoded proteins.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a new cross-tissue co-abundance observation, but the evidence is insufficient to call it a new biological mechanism or a new protein complex. Its novelty is supported only in the limited sense that the supplied resources show no high-confidence STRING links, no multi-member hu.MAP complex and no STRING enrichment. Those absences do not prove novelty, because co-abundance can arise from shared cell composition, regulation, secretion, tissue injury or technical factors that are not represented in interaction databases. The heterogeneous annotations, immune-cell associations and partial secreted-protein representation make a composition-driven explanation particularly plausible. A stronger novelty claim would require replication in independent CSF and skin cohorts, adjustment for cell-type and blood contamination, preservation of the module after such adjustment, and experimental or orthogonal evidence connecting the proteins.

**Hypothesis.** Hypothesis: the shared module reflects a coordinated extracellular or cellular-state signal contributed by neural or barrier-associated cells together with immune or blood-associated cells. In this model, NRCAM marks cell-contact and neural or tissue-interface biology; TFRC, ACP2 and PLBD2 represent endocytic, lysosomal and lipid-handling activity; CD276 represents immune-regulatory signaling; and SOD2 represents mitochondrial oxidative-stress adaptation. The apparent conservation between CSF and skin could arise because both compartments contain related tissue-interface, immune, vascular or injury-response signals, or because circulating material and shared cell types contribute to both datasets. This is a mechanistic hypothesis, not an established pathway, and should be tested by cell-type deconvolution, blood-contamination controls, protein-level validation and perturbation of candidate hub relationships.

### Important genes

#### NRCAM

- **Related proteins** (co-abundance neighbors): TFRC (0.88), PLBD2 (0.87), CD276 (0.82), SOD2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neuronal cell adhesion molecule. Cell adhesion molecules (CAMs) are members of the immunoglobulin superfamily. This gene encodes a neuronal cell adhesion molecule with multiple immunoglobulin-like C2-type domains and fibronectin type-III domains. This ankyrin-binding protein is involved in neuron-neuron adhesion and promotes directional signaling during axonal cone growth. This gene is also expressed in non-neural tissues and may…
- **Diseases (Open Targets)**: neurodevelopmental disorder with neuromuscular and skeletal abnormalities (0.774); complex neurodevelopmental disorder (0.370); stroke disorder (0.261); alcohol drinking (0.257); ovarian neoplasm (0.255)
- **Europe PMC papers**: 2314
- **Why important**: NRCAM is the central network node, connected to TFRC, PLBD2, CD276 and SOD2, and has the strongest internal network position. Its established annotation as a neuronal cell-adhesion molecule, together with roles in neuron-neuron adhesion, axon guidance, axonal fasciculation and synapse assembly, provides the clearest link to the cerebrospinal-fluid side of the module. HPA places it in brain and retina among other tissues and reports neural cell-type enhancement. It also has substantial literature and disease associations involving neurodevelopmental and neuromuscular phenotypes.
- **Conclusion**: Established evidence supports NRCAM as a neural cell-adhesion and signaling marker and as the statistical hub of this module. It is a plausible biological anchor, but the absence of STRING or hu.MAP support means that its direct relationships with the other module proteins remain hypothetical.

#### TFRC

- **Related proteins** (co-abundance neighbors): NRCAM (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes, Lysosomes; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transferrin receptor. This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: TFRC-related combined immunodeficiency (0.623); type 2 diabetes mellitus (0.518); mucopolysaccharidosis type 2 (0.490); diabetes mellitus (0.471); diabetic retinopathy (0.343)
- **Europe PMC papers**: 14164
- **Why important**: TFRC is directly connected to NRCAM and has the largest literature volume in the module. Its established function is receptor-mediated cellular iron uptake, with roles in endocytosis, erythropoiesis, neurologic development, hypoxia response and intracellular iron homeostasis. HPA indicates low tissue specificity, secretion to blood, and enhancement in monocytes and macrophages, making it important both biologically and for evaluating blood or immune-cell contributions.
- **Conclusion**: Established evidence supports TFRC as an iron-uptake and endocytic marker with broad cellular distribution. Within this module, its co-abundance with NRCAM may reflect a shared cellular state or sample composition; a direct NRCAM-TFRC mechanism is not established.

#### SOD2

- **Related proteins** (co-abundance neighbors): NRCAM (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: superoxide dismutase 2. This gene is a member of the iron/manganese superoxide dismutase family. It encodes a mitochondrial protein that forms a homotetramer and binds one manganese ion per subunit. This protein binds to the superoxide byproducts of oxidative phosphorylation and converts them to hydrogen peroxide and diatomic oxygen. Mutations in this gene have been associated with idiopathic cardiomyopathy (IDC), premat…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); diabetic retinopathy (0.379); malunion fracture (0.295); coronary artery disorder (0.267); prostate carcinoma (0.227)
- **Europe PMC papers**: 28293
- **Why important**: SOD2 is directly connected to the network hub and is the clearest oxidative-stress component. Its established mitochondrial function is conversion of superoxide into hydrogen peroxide and oxygen, with annotations for superoxide metabolism, hypoxia response and mitochondrial stress. HPA reports bone-marrow enhancement and associations with monocytes and neutrophils, while its disease literature includes neurodegenerative and other stress-related disorders.
- **Conclusion**: Established evidence supports SOD2 as a mitochondrial antioxidant and stress-response protein. Its presence may indicate oxidative or inflammatory state in the sampled material, but the module does not establish that oxidative stress drives the other genes.

#### CD276

- **Related proteins** (co-abundance neighbors): NRCAM (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD276 molecule. The protein encoded by this gene belongs to the immunoglobulin superfamily, and thought to participate in the regulation of T-cell-mediated immune response. Studies show that while the transcript of this gene is ubiquitously expressed in normal tissues and solid tumors, the protein is preferentially expressed only in tumor tissues. Additionally, it was observed that the 3' UTR of this transcript c…
- **Diseases (Open Targets)**: response to statin (0.321); Abnormality of the skeletal system (0.290); head and neck squamous cell carcinoma (0.228); prostate cancer (0.128); cancer (0.128)
- **Europe PMC papers**: 6027
- **Why important**: CD276 is directly connected to NRCAM and contributes an immune-regulatory interpretation distinct from the neural and metabolic annotations. Its established functions include regulation of cytokine production, type II interferon production and T-cell activation or proliferation. HPA reports vesicular localization and enhancement in Hofbauer cells and extravillous trophoblasts, while disease associations include cancer-related phenotypes.
- **Conclusion**: Established evidence supports CD276 as an immune-regulatory and cell-surface or vesicle-associated marker. Its co-abundance with NRCAM could reflect coordinated tissue-interface or immune-state biology, but a functional CD276-NRCAM interaction is a hypothesis rather than a demonstrated relationship.

#### ACP2

- **Related proteins** (co-abundance neighbors): PLBD2 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acid phosphatase 2, lysosomal. The protein encoded by this gene belongs to the histidine acid phosphatase family, which hydrolyze orthophosphoric monoesters to alcohol and phosphate. This protein is localized to the lysosomal membrane, and is chemically and genetically distinct from the red cell acid phosphatase. Mice lacking this gene showed multiple defects, including bone structure alterations, lysosomal storage defects, and…
- **Diseases (Open Targets)**: xeroderma pigmentosum group E (0.404); clear cell renal carcinoma (0.294); non-alcoholic fatty liver (0.254); neurodegenerative disease (0.203); hypertensive disorder (0.193)
- **Europe PMC papers**: 844
- **Why important**: ACP2 is connected to PLBD2 and provides a lysosomal component that helps explain the module's vesicular and degradative aspect. Its established annotation identifies it as a lysosomal acid phosphatase involved in lysosome organization, with reported animal-model links to bone defects, lysosomal storage abnormalities and seizure tendency. HPA shows low tissue specificity and enhancement in hepatocytes, Hofbauer cells and Kupffer cells, supporting possible myeloid or tissue-clearance contributions.
- **Conclusion**: Established evidence supports ACP2 as a lysosomal enzyme and a marker of intracellular degradation or trafficking. Its relationship to PLBD2 is supported only by the co-abundance edge; a shared lipid-lysosome mechanism remains a hypothesis.

