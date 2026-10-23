# Conserved co-abundance modules: bone and bone_marrow

## Module 0

**Tissue pair**: bone and bone_marrow  
**Genes (27)**: NUDT1, AP1B1, ARL6IP4, ARSA, BOP1, COPG2, CPSF1, CWC27, HEATR1, IFT27, LACTB2, MAPK14, MMS19, NSUN2, PEX19, MOB4, PPIE, PSMG4, RAP2C, MRPL42, SLC27A4, SPATS2, SPC24, LARS2, TATDN1, TCERG1, TIGAR

### Function

This module does not have any GO or KEGG term passing global correction, so no pathway-level enrichment can be claimed. Its gene content instead points to a heterogeneous intracellular program involving RNA processing and modification, ribosome and mitochondrial protein synthesis, cell-cycle and kinetochore biology, protein folding and quality control, vesicle trafficking, peroxisome maintenance, lipid handling, and stress signaling. The network is organized around a few highly connected genes, especially ARSA and IFT27, with many genes attached through isolated, high-weight co-abundance links. Thus, the most defensible interpretation is a shared cellular-state module rather than a coherent, globally enriched pathway. The absence of significant GO or KEGG enrichment does not invalidate the module.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only a small minority are annotated as secreted, and most proteins are intracellular. It is also not strongly blood-cell specific according to HPA, although bone-marrow protein detection is common and SPC24 and NUDT1 are tissue-enhanced in bone marrow. HPA indicates predominantly low tissue specificity and predominantly low immune-cell specificity, arguing against a simple leukocyte-specific module. Cell-type annotations are dispersed across germ-cell, epithelial, stromal, megakaryocytic, progenitor, and other cell types, with some enrichment in megakaryocytes and monocyte progenitors but no unified blood-cell signature. The shared signal may therefore reflect broadly expressed cellular machinery, proliferative or differentiation state, and the mixture of cell types present in bone and bone marrow rather than a specialized bone program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supplies only a few high-confidence relationships: BOP1--HEATR1, BOP1--NSUN2, and CWC27--PPIE. These are biologically plausible links involving ribosome biogenesis and RNA-processing or protein-folding machinery, but STRING provides no functional enrichment for the module and most co-abundance edges are not represented as high-confidence STRING interactions. hu.MAP contributes one large, heterogeneous complex containing the module members LARS2 and TATDN1 (hu.MAP huMAP3_13468.1). Because only a small subset of that complex is represented in the module and the complex spans many mitochondrial, metabolic, and protein-homeostasis proteins, this is supportive of shared cellular machinery but not evidence for a single dedicated complex. Overall, the co-abundance network extends beyond currently catalogued physical interactions and should not be interpreted as a protein-interaction map.

**STRING interactions (score >= 0.7)**: 3 of 351 gene pairs: BOP1–HEATR1 (0.971); BOP1–NSUN2 (0.731); CWC27–PPIE (0.831)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (LARS2, TATDN1; 2/99)

### Novelty

The precise shared co-abundance module may be a new observation because its full edge pattern is not recapitulated by STRING or hu.MAP. However, database absence alone does not establish novelty: many edges may reflect indirect regulation, shared cell composition, transcriptional state, or technical covariance, and several member functions are already well established. The most supportable claim is therefore novelty of the tissue-pair co-abundance organization, not discovery of a new molecular pathway. Replication in independent bone and bone-marrow datasets, adjustment for cell composition, and experimental testing of selected edges would be needed before claiming a novel biological mechanism.

**Hypothesis.** Hypothesis: this shared module captures a general cellular maintenance and biosynthetic state present in overlapping cell populations of bone and bone marrow. In this state, RNA maturation and modification, ribosome production, mitochondrial translation, proteostasis, vesicle trafficking, lipid or peroxisome handling, and stress responses vary together. ARSA-centered covariance may reflect intracellular trafficking and lysosomal or membrane-associated biology, while IFT27-linked covariance may connect ciliary or transport-related functions with RNA processing and signaling. The module could therefore represent coordinated demands of proliferating, differentiating, or metabolically stressed cells rather than a bone-specific pathway. This hypothesis is not established by the absent global enrichment and should be tested by cell-type deconvolution, longitudinal perturbation, and validation of the strongest module relationships.

### Important genes

#### ARSA

- **Related proteins** (co-abundance neighbors): BOP1 (0.97), CPSF1 (0.97), NUDT1 (0.92), MMS19 (0.91), NSUN2 (0.90), TCERG1 (0.90), SPC24 (0.87), COPG2 (0.82), AP1B1 (0.81), MOB4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: arylsulfatase A. The protein encoded by this gene hydrolyzes cerebroside sulfate to cerebroside and sulfate. Defects in this gene lead to metachromatic leucodystrophy (MLD), a progressive demyelination disease which results in a variety of neurological symptoms and ultimately death. Alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Dec 2010].
- **Diseases (Open Targets)**: metachromatic leukodystrophy (0.879); metachromatic leukodystrophy, juvenile form (0.782); metachromatic leukodystrophy, adult form (0.606); metachromatic leukodystrophy, late infantile form (0.592); hereditary disease (0.522)
- **Europe PMC papers**: 4753
- **Why important**: ARSA is the principal network hub by weighted connectivity and links genes involved in RNA processing, oxidative-stress protection, vesicle trafficking, and cellular maintenance. Its established function is hydrolysis of cerebroside sulfate, with roles in ganglioside and sphingolipid catabolism. It is intracellular and associated with the Golgi apparatus, is detected in bone marrow, and has a well documented association with metachromatic leukodystrophy and extensive literature.
- **Conclusion**: Established evidence supports ARSA as the strongest network anchor and a lysosomal or sphingolipid-related marker within the module. It should not be concluded that ARSA drives the entire module or that the module represents metachromatic leukodystrophy. A plausible but unproven interpretation is that ARSA covariance reflects membrane trafficking, lipid handling, or shared cell state.

#### IFT27

- **Related proteins** (co-abundance neighbors): SPC24 (0.95), PPIE (0.92), MAPK14 (0.91), LACTB2 (0.86), PEX19 (0.85), CWC27 (0.85), ARL6IP4 (0.85), TATDN1 (0.83), TIGAR (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: intraflagellar transport 27. This gene encodes a GTP-binding protein that is a core component of the intraflagellar transport complex B. Characterization of the similar Chlamydomonas protein indicates a function in cell cycle control. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: Bardet-Biedl syndrome (0.772); Jeune syndrome (0.432); ciliopathy (0.380); polydactyly (0.370); smoking initiation (0.278)
- **Europe PMC papers**: 552
- **Why important**: IFT27 is another major network hub and connects SPC24, PPIE, MAPK14, LACTB2, PEX19, CWC27, ARL6IP4, and TATDN1. Its established role is as a GTP-binding component of intraflagellar transport complex B, with links to intracellular transport, ciliary signaling, development, and spermatogenesis. It has recognized ciliopathy and Bardet-Biedl syndrome associations and provides a bridge between transport, signaling, and RNA-processing genes.
- **Conclusion**: Established evidence supports IFT27 as a structurally important connector in the co-abundance graph, but not as proof that cilia biology is the dominant module function in bone or marrow. The hypothesis that IFT27 links transport or signaling state to the other module processes requires direct testing in the relevant cell populations.

#### SPC24

- **Related proteins** (co-abundance neighbors): IFT27 (0.95), ARSA (0.87), RAP2C (0.85), HEATR1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SPC24 component of NDC80 kinetochore complex. Predicted to be involved in cell division. Located in nucleolus and nucleoplasm. Part of Ndc80 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypercholesterolemia, familial, 1 (0.508); metabolic disease (0.242); hyperlipidemia (0.242); rheumatoid arthritis (0.174); familial hypercholesterolemia (0.143)
- **Europe PMC papers**: 838
- **Why important**: SPC24 is tissue-enhanced in bone marrow, detected there by HPA, and annotated as a component of the NDC80 kinetochore complex involved in chromosome segregation and the spindle assembly checkpoint. It connects the transport-related IFT27 branch to ARSA, RAP2C, and HEATR1. Its cell-type annotations include erythrocyte progenitors and megakaryocyte progenitors, making it especially relevant to the cellular composition of marrow.
- **Conclusion**: Established evidence supports SPC24 as a marker of proliferative or progenitor-associated biology in the marrow component of the module. It does not establish that the module is a cell-division program, because global GO and KEGG enrichment is absent and the module includes many non-mitotic genes. A cell-composition or differentiation-state explanation is plausible.

#### MAPK14

- **Related proteins** (co-abundance neighbors): IFT27 (0.91); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Nuclear speckles; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitogen-activated protein kinase 14. The protein encoded by this gene is a member of the MAP kinase family. MAP kinases act as an integration point for multiple biochemical signals, and are involved in a wide variety of cellular processes such as proliferation, differentiation, transcription regulation and development. This kinase is activated by various environmental stresses and proinflammatory cytokines. The activation requires it…
- **Diseases (Open Targets)**: neurodegenerative disease (0.464); autoimmune disorder of central nervous system (0.459); Alzheimer disease (0.337); Parkinson disease (0.316); lysosomal storage disease (0.303)
- **Europe PMC papers**: 8074
- **Why important**: MAPK14 is a signaling kinase activated by environmental stress and proinflammatory cytokines and is involved in proliferation, differentiation, transcription, chemotaxis, and inflammatory signaling. HPA places it in monocyte and neutrophil progenitor or neutrophil-associated contexts and detects it in bone marrow. It also has a particularly extensive literature base relative to most module members. In the network it provides a high-weight link to IFT27.
- **Conclusion**: Established evidence supports MAPK14 as a biologically plausible indicator of stress, differentiation, or inflammatory signaling in marrow-associated cells. The module does not demonstrate MAPK14 activation, since co-abundance is not phosphorylation or activity. Its connection to IFT27 may be a state-level association rather than a direct physical interaction.

#### BOP1

- **Related proteins** (co-abundance neighbors): ARSA (0.97); STRING partners: HEATR1 (0.971), NSUN2 (0.731)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BOP1 ribosomal biogenesis factor. Enables RNA binding activity. Involved in regulation of cell cycle; regulation of signal transduction by p53 class mediator; and ribosomal large subunit biogenesis. Located in chromosome; nucleolus; and nucleoplasm. Part of PeBoW complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.318); cancer (0.090); neoplasm (0.087); polycystic ovary syndrome (0.082); colorectal carcinoma (0.078)
- **Europe PMC papers**: 1064
- **Why important**: BOP1 is a nucleolar ribosome-biogenesis factor and a component of the PeBoW complex. It has high-weight STRING relationships with HEATR1 and NSUN2, providing some external support for a ribosome and RNA-processing branch of the module. It is tissue-enhanced in skeletal muscle and has established links to cell-cycle regulation, p53 signaling, and ribosomal large-subunit biogenesis, with substantial literature.
- **Conclusion**: Established evidence supports BOP1 as an anchor for the module's ribosome-biogenesis and proliferative-cell-state interpretation. The STRING links strengthen that interpretation but do not make the entire co-abundance module a PeBoW complex. Its presence may reflect biosynthetic demand in shared or differentiating cells.

#### CWC27

- **Related proteins** (co-abundance neighbors): IFT27 (0.85); STRING partners: PPIE (0.831)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CWC27 spliceosome associated cyclophilin. Predicted to enable peptidyl-prolyl cis-trans isomerase activity. Predicted to be involved in protein peptidyl-prolyl isomerization. Located in nucleoplasm. Part of U2-type precatalytic spliceosome and catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: metaphyseal chondrodysplasia-retinitis pigmentosa syndrome (0.764); retinitis pigmentosa (0.450); inherited retinal dystrophy (0.433); Abnormality of the skeletal system (0.421); diverticular disease (0.394)
- **Europe PMC papers**: 282
- **Why important**: CWC27 is a spliceosome-associated cyclophilin involved in mRNA splicing and protein peptidyl-prolyl isomerization. It has a high-confidence STRING relationship with PPIE, which has related RNA-binding, splicing, and protein-folding functions, and it connects to IFT27 in the co-abundance network. CWC27 is associated with metaphyseal chondrodysplasia-retinitis pigmentosa syndrome and skeletal abnormalities, making it especially relevant to a bone-containing tissue pair.
- **Conclusion**: Established evidence supports CWC27 as a credible representative of the RNA-splicing and protein-folding component, with disease relevance to skeletal biology. The module does not prove that CWC27 mediates the tissue-pair association or that the disease relationship explains the observed covariance. A shared differentiation or proteostasis state remains the more cautious interpretation.

## Module 1

**Tissue pair**: bone and bone_marrow  
**Genes (15)**: ABCF3, ASPH, CAT, CIP2A, CORO1B, CYFIP1, DNAJB4, DST, LYPLA2, MTAP, PDLIM2, TSG101, UMPS, UNC45A, UTRN

### Function

The strongest supported function is cell-adhesion-related cytoskeletal organization, based on the globally corrected GO molecular-function term (GO:MF cell adhesion molecule binding; q_global = 0.0439). The term involves ABCF3, CIP2A, CORO1B, DST, LYPLA2, UNC45A and UTRN. This interpretation is biologically coherent with the annotations for UTRN, CORO1B, DST and PDLIM2, which concern actin binding, cell migration, adhesion junctions, focal adhesions and cytoskeletal organization. Additional genes suggest supporting processes rather than a single pathway: CAT contributes oxidative-stress handling, UMPS contributes pyrimidine synthesis, MTAP contributes methionine and polyamine salvage, and CYFIP1 contributes WAVE-complex-mediated actin dynamics and translation control. Thus, the module is best interpreted as a cell-adhesion and cytoskeletal-support module with metabolic, chaperone and redox components. The absence of other globally corrected GO or KEGG terms does not invalidate the module; it limits the specificity of the functional claim. The STRING enrichment (STRING Function Cell adhesion molecule binding; within-query FDR = 0.0468) is concordant but supplementary, not independent global evidence.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and the protein evidence is predominantly available in bone marrow, which is consistent with a broadly expressed cellular module rather than a bone-specific secreted program. HPA indicates extensive cell-type enhancement, especially in syncytiotrophoblasts, neutrophil progenitors, late primary spermatocytes, esophageal apical cells and neutrophils. Blood-cell evidence includes immune enhancement or enrichment for several genes, with monocyte, dendritic-cell, eosinophil and neutrophil signals. CYFIP1 is group-enriched across monocyte and dendritic-cell populations, while CAT is immune-cell enriched in eosinophils and UTRN and CORO1B are immune-cell enhanced in monocyte-related populations. These observations support caution that the shared bone and bone-marrow signal may partly reflect common hematopoietic or immune-cell composition, or broadly shared cellular machinery, rather than a mechanism unique to bone biology. The tissue-enhanced adipose and liver signals for ASPH and CAT also argue against a narrowly bone-restricted interpretation.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF cell adhesion molecule binding | 0.0439 | ABCF3, CIP2A, CORO1B, DST, LYPLA2, UNC45A, UTRN |

### STRING and hu.MAP

No pair among the module genes reaches the supplied high-confidence STRING interaction threshold, so STRING does not provide established physical or functional edges within this module. The concordant STRING enrichment (STRING Function Cell adhesion molecule binding; within-query FDR = 0.0468) supports the cell-adhesion-molecule-binding theme, but it should remain supplementary. hu.MAP identifies one complex-level association (hu.MAP huMAP3_09042.1), in which UMPS and UNC45A occur together within a larger complex. Because only these module members are represented in that complex and the supplied confidence is intermediate, this is evidence of a possible shared complex context rather than proof of a central module mechanism. Overall, the co-abundance edges are not recapitulated by established STRING interactions, and only limited complex evidence is available from hu.MAP. The network therefore appears to capture coordinated abundance in the sampled tissues more than a pre-existing, densely documented protein-interaction complex.

**STRING interactions (score >= 0.7)**: 0 of 105 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Function Cell adhesion molecule binding (FDR = 0.0468, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09042.1 (UMPS, UNC45A; 2/26)

### Novelty

This is a potentially novel tissue-shared co-abundance observation, but it cannot be called a newly discovered biological pathway from the supplied evidence alone. The case for novelty is that the module has no high-confidence STRING edges among its members and only a limited hu.MAP overlap, while bringing together adhesion, cytoskeletal, metabolic, redox and chaperone genes. However, absence from STRING or hu.MAP is not proof of novelty. Several component functions and disease associations are already established, and the HPA profile raises the alternative explanation of shared cell composition or broadly expressed cellular machinery. The defensible conclusion is that the specific coordinated abundance pattern across bone and bone marrow is a candidate novel observation requiring replication, cell-composition adjustment and independent experimental validation; the individual molecular functions are not novel.

**Hypothesis.** Hypothesis: the module reflects a shared structural and stress-adaptation program in cells present in bone and bone marrow, potentially including hematopoietic or immune cells. PDLIM2 may organize adhesion-associated actin structures, with UTRN, CORO1B, DST and CYFIP1 supporting membrane-to-cytoskeleton coupling, cell movement and actin remodeling. CAT may buffer oxidative stress, while UMPS, MTAP and the chaperone-related genes may support nucleotide, methylthioadenosine and protein-homeostasis demands. In this model, the apparent module is generated by coordinated cellular state or cell mixture rather than by one established multiprotein complex. This remains a hypothesis because the network has no high-confidence STRING links, the enrichment is concentrated in one GO term, and the data are co-abundance rather than mechanistic perturbation evidence.

### Important genes

#### PDLIM2

- **Related proteins** (co-abundance neighbors): TSG101 (0.92), UMPS (0.87), UNC45A (0.87), LYPLA2 (0.86), ABCF3 (0.84), CYFIP1 (0.82), MTAP (0.80), CIP2A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments, Focal adhesion sites; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 2. This gene encodes a member of the ALP subfamily of PDZ-LIM domain proteins. The encoded protein suppresses anchorage-dependent growth and promotes cell migration and adhesion through interactions with the actin cytoskeleton via the PDZ domain. The encoded protein is also a putative tumor suppressor protein, and decreased expression of this gene is associated with several malignancies including bre…
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); neoplasm (0.113); lung carcinoma (0.107); lung cancer (0.107); cancer (0.097)
- **Europe PMC papers**: 822
- **Why important**: PDLIM2 is the principal network hub by weighted connectivity in the supplied subgraph and links the adhesion-associated genes to additional module members including TSG101, UMPS, UNC45A, LYPLA2, ABCF3, CYFIP1, MTAP and CIP2A. Its HPA localization at actin filaments and focal adhesion sites, together with the MyGene.info description of actin-cytoskeleton interactions, migration and adhesion, makes it the strongest structural candidate. It has substantial literature volume and disease associations involving neoplasm and neurodegenerative disease.
- **Conclusion**: Established evidence supports PDLIM2 as an adhesion- and actin-associated scaffold and as the network-centered candidate in this module. The hypothesis that it organizes the shared bone and bone-marrow program is plausible from network position and localization but is not demonstrated by the supplied data, especially because it has no STRING or hu.MAP support here.

#### UTRN

- **Related proteins** (co-abundance neighbors): ASPH (0.86), MTAP (0.84), CORO1B (0.80), CAT (0.80), DST (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: utrophin. This gene shares both structural and functional similarities with the dystrophin gene. It contains an actin-binding N-terminus, a triple coiled-coil repeat central region, and a C-terminus that consists of protein-protein interaction motifs which interact with dystroglycan protein components. The protein encoded by this gene is located at the neuromuscular synapse and myotendinous junctions, where…
- **Diseases (Open Targets)**: schizophrenia (0.413); smoking initiation (0.374); multisite chronic pain (0.374); bilirubin metabolism disease (0.319); ovarian dysfunction (0.299)
- **Europe PMC papers**: 1371
- **Why important**: UTRN has a prominent network position and is connected to ASPH, MTAP, CORO1B, CAT and DST. It is one of the genes in the globally corrected adhesion-binding term (GO:MF cell adhesion molecule binding; q_global = 0.0439) and the supplementary STRING term (STRING Function Cell adhesion molecule binding; within-query FDR = 0.0468). Its established actin-binding and membrane-maintenance functions, plasma-membrane localization, and role in cell-matrix adhesion provide a direct mechanistic bridge between the module's network structure and its functional interpretation. It also has substantial literature volume and an HPA immune-cell enhancement signal in non-classical monocytes.
- **Conclusion**: Established evidence supports UTRN as a cytoskeletal and adhesion component that could connect membrane structure with cell movement. Its participation in a bone-marrow-associated immune or stromal program is a hypothesis, not an established conclusion from this module.

#### CORO1B

- **Related proteins** (co-abundance neighbors): UTRN (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coronin 1B. Members of the coronin family, such as CORO1B, are WD repeat-containing actin-binding proteins that regulate cell motility (Cai et al., 2005 [PubMed 16027158]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Abnormality of refraction (0.067); refractive error (0.049); alcohol drinking (0.027); asthma (0.025); diabetes mellitus (0.025)
- **Europe PMC papers**: 339
- **Why important**: CORO1B is linked to UTRN and is included in (GO:MF cell adhesion molecule binding; q_global = 0.0439) and (STRING Function Cell adhesion molecule binding; within-query FDR = 0.0468). Its established functions include actin-filament organization, cell migration, ruffle organization and regulation of Arp2/3-mediated actin nucleation. HPA places it at the plasma membrane and in the cytosol, with enhancement in several epithelial or specialized cell types and in non-classical monocytes. It therefore provides a specific actin-remodeling explanation for the adhesion signal.
- **Conclusion**: Established evidence supports CORO1B as an actin-remodeling and motility factor. Its co-abundance with UTRN may indicate coordinated cytoskeletal behavior, but a direct partnership in this module is not established because STRING reports no qualifying interaction.

#### CAT

- **Related proteins** (co-abundance neighbors): UTRN (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Vesicles; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catalase. This gene encodes catalase, a key antioxidant enzyme in the bodies defense against oxidative stress. Catalase is a heme enzyme that is present in the peroxisome of nearly all aerobic cells. Catalase converts the reactive oxygen species hydrogen peroxide to water and oxygen and thereby mitigates the toxic effects of hydrogen peroxide. Oxidative stress is hypothesized to play a role in the developme…
- **Diseases (Open Targets)**: acatalasia (0.697); type 2 diabetes mellitus (0.354); COVID-19 (0.299); major depressive disorder (0.272); neurodegenerative disease (0.224)
- **Europe PMC papers**: 432201
- **Why important**: CAT is connected to UTRN and is the most extensively studied gene among the selected candidates according to the supplied literature volume. It is a canonical antioxidant enzyme, and its supplied annotations include responses to reactive oxygen species, hypoxia and oxidative stress, as well as osteoblast differentiation. HPA shows liver tissue enhancement, enrichment in eosinophils and enhancement in erythroid and neutrophil progenitor populations, making it informative for interpreting possible marrow-cell composition.
- **Conclusion**: Established evidence supports CAT as an oxidative-stress defense enzyme with relevance to progenitor and bone-related annotations. Its inclusion suggests that redox state may accompany the adhesion program, but the module does not establish that CAT mechanistically regulates the adhesion genes.

#### CYFIP1

- **Related proteins** (co-abundance neighbors): PDLIM2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Group enriched; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytoplasmic FMR1 interacting protein 1. This gene encodes a protein that regulates cytoskeletal dynamics and protein translation. The encoded protein is a component of the WAVE regulatory complex (WRC), which promotes actin polymerization. This protein also interacts with the synaptic functional regulator FMR1 protein and translation initiation factor 4E to inhibit protein translation. A large chromosomal deletion including this gene is…
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); lymphatic system disorder (0.336); vein disorder (0.336); Varicose veins (0.305); autism (0.154)
- **Europe PMC papers**: 1698
- **Why important**: CYFIP1 is directly connected to the network hub PDLIM2 and has HPA group enrichment across monocyte and dendritic-cell populations, with cell-type enrichment in microglia. Its established functions in the WAVE regulatory complex, actin polymerization, lamellipodium assembly, Rac signaling and translation regulation make it a strong candidate for linking cytoskeletal remodeling with cell state. Its disease associations include neurodegenerative and lymphatic-system disorders.
- **Conclusion**: Established evidence supports CYFIP1 as a regulator of actin dynamics and translation with a myeloid-cell expression pattern. It strengthens the interpretation that shared immune or hematopoietic cell composition may contribute to the module, while a direct role in bone or bone-marrow co-abundance remains a hypothesis.

## Module 2

**Tissue pair**: bone and bone_marrow  
**Genes (44)**: AKAP8, ANO10, AQR, BCLAF1, CAPRIN1, CLTB, CORO1C, DDX21, DDX5, DHX9, EXOSC6, MACROH2A2, MACROH2A1, HNRNPL, HNRNPR, INTS1, ITPR3, LBR, LMNB1, LMNB2, MATR3, MBNL1, MYEF2, NELFA, SNU13, NNT, NOP2, ORMDL3, UQCRC2, RAB5C, RSL1D1, POLR2E, SF3A1, SMARCA4, SMARCC2, SUPT16H, SPIN1, SPTBN1, SPTAN1, SYNPO, TCOF1, SNRNP200, EFTUD2, CSE1L

### Function

This module is best interpreted as a conserved nuclear gene-expression and RNA-processing program. The primary evidence includes broad nucleic-acid binding and nuclear-lumen enrichment (GO:MF nucleic acid binding; q_global = 0.00471) (GO:CC nuclear lumen; q_global = 0.00486), with coherent enrichment for RNA binding (GO:MF mRNA binding; q_global = 0.013) (GO:MF RNA binding; q_global = 0.0235), pre-mRNA splicing and the catalytic step of the spliceosome (GO:BP RNA splicing; q_global = 0.0274) (GO:CC catalytic step 2 spliceosome; q_global = 0.0389), nucleolar and ribosomal RNA transcription (GO:BP rRNA transcription; q_global = 0.0124) (GO:BP nucleolar large rRNA transcription by RNA polymerase I; q_global = 0.0125) (GO:BP transcription by RNA polymerase I; q_global = 0.0389), and chromatin or heterochromatin regulation (4 globally significant GO/KEGG terms, q_global 0.0332–0.0473; see the table). The module therefore links several connected layers of gene regulation: chromatin accessibility and nuclear architecture, transcription, rRNA production, RNA maturation, and RNA surveillance. Negative regulation of biosynthetic and macromolecule biosynthetic processes (GO:BP negative regulation of biosynthetic process; q_global = 0.025) (GO:BP negative regulation of macromolecule biosynthetic process; q_global = 0.044) is consistent with regulatory control rather than with a narrowly specialized metabolic pathway. The result is biologically coherent even though the module also contains peripheral cytoskeletal, vesicular, mitochondrial, and membrane-associated genes that may reflect cell-state or sample-composition effects.

**Cell composition.** The module is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity and low immune-cell specificity, and many encode broadly used nuclear, RNA-binding, chromatin, or structural proteins. Thus, the shared signal is more consistent with a broadly expressed housekeeping or proliferative nuclear program than with a bone-specific extracellular matrix program. HPA detects most tested proteins in bone marrow, but this does not establish a blood-cell-specific module. Some genes are enriched in erythrocyte, neutrophil, monocyte, megakaryocyte, lymphoid, or other progenitor populations, while the aggregate blood-cell specificity remains low. The module could therefore partly reflect shared nucleated cell types or common transcriptional activity in bone and bone marrow samples, rather than a function unique to osteoblasts or marrow tissue.

**GO/KEGG enrichment**: 15 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleic acid binding | 0.00471 | AKAP8, AQR, BCLAF1, CAPRIN1, DDX21, DDX5, DHX9, EFTUD2, EXOSC6, HNRNPL, HNRNPR, LBR, LMNB1, MACROH2A1, MACROH2A2, MATR3, MBNL1, MYEF2, NOP2, POLR2E, RSL1D1, SF3A1, SMARCA4, SMARCC2, SNRNP200, SNU13, SPTBN1, SUPT16H, TCOF1 |
| GO:CC nuclear lumen | 0.00486 | AKAP8, AQR, BCLAF1, CSE1L, DDX21, DDX5, DHX9, EFTUD2, EXOSC6, HNRNPL, HNRNPR, INTS1, ITPR3, LBR, LMNB1, LMNB2, MACROH2A1, MACROH2A2, MATR3, MBNL1, NELFA, NOP2, POLR2E, RSL1D1, SF3A1, SMARCA4, SMARCC2, SNRNP200, SNU13, SPIN1, SPTBN1, SUPT16H, TCOF1, UQCRC2 |
| GO:BP rRNA transcription | 0.0124 | MACROH2A1, MACROH2A2, SMARCA4, SPIN1, TCOF1 |
| GO:BP nucleolar large rRNA transcription by RNA polymerase I | 0.0125 | MACROH2A1, MACROH2A2, SMARCA4, TCOF1 |
| GO:MF mRNA binding | 0.013 | AQR, BCLAF1, CAPRIN1, DDX21, DDX5, DHX9, HNRNPL, HNRNPR, MYEF2, RSL1D1 |
| GO:MF RNA binding | 0.0235 | AKAP8, AQR, BCLAF1, CAPRIN1, DDX21, DDX5, DHX9, EFTUD2, EXOSC6, HNRNPL, HNRNPR, LBR, MATR3, MBNL1, MYEF2, NOP2, RSL1D1, SF3A1, SMARCA4, SNRNP200, SNU13, SPTBN1, SUPT16H, TCOF1 |
| GO:BP negative regulation of biosynthetic process | 0.025 | AKAP8, BCLAF1, CAPRIN1, DDX21, DDX5, DHX9, EXOSC6, HNRNPL, LBR, LMNB1, LMNB2, MACROH2A1, MACROH2A2, NELFA, ORMDL3, SMARCA4, SMARCC2, SPIN1 |
| GO:BP RNA splicing | 0.0274 | AQR, BCLAF1, DDX5, DHX9, EFTUD2, HNRNPL, HNRNPR, MBNL1, SF3A1, SNRNP200, SNU13 |
| GO:BP heterochromatin formation | 0.0332 | LBR, LMNB1, LMNB2, MACROH2A1, MACROH2A2, SPIN1 |
| GO:BP heterochromatin organization | 0.0332 | LBR, LMNB1, LMNB2, MACROH2A1, MACROH2A2, SPIN1 |
| GO:BP transcription by RNA polymerase I | 0.0389 | DDX21, MACROH2A1, MACROH2A2, POLR2E, SMARCA4, TCOF1 |
| GO:CC catalytic step 2 spliceosome | 0.0389 | AQR, DDX5, EFTUD2, HNRNPR, SF3A1, SNRNP200 |
| GO:BP negative regulation of macromolecule biosynthetic process | 0.044 | AKAP8, BCLAF1, CAPRIN1, DDX21, DDX5, DHX9, EXOSC6, HNRNPL, LBR, LMNB1, LMNB2, MACROH2A1, MACROH2A2, NELFA, SMARCA4, SMARCC2, SPIN1 |
| GO:BP negative regulation of gene expression, epigenetic | 0.0455 | LBR, LMNB1, LMNB2, MACROH2A1, MACROH2A2, SPIN1 |
| GO:BP epigenetic regulation of gene expression | 0.0473 | LBR, LMNB1, LMNB2, MACROH2A1, MACROH2A2, SMARCA4, SPIN1 |

### STRING and hu.MAP

STRING supports a substantial known interaction backbone. The strongest relationships form recognizable spliceosomal and RNA-processing connections involving AQR, EFTUD2, SF3A1, SNRNP200, SNU13, DDX5, DHX9, HNRNPL, HNRNPR, and MATR3. Additional established relationships connect DDX21 with DHX9, NOP2, and RSL1D1; LMNB1 with LMNB2 and LBR; SMARCA4 with SMARCC2; NELFA with POLR2E; and SPTAN1 with SPTBN1. STRING enrichment for nuclear lumen, RNA metabolism, mRNA splicing, spliceosomes, and RNA binding (8 supplementary STRING terms; within-query FDR 0.00029–0.0204) agrees with the primary GO interpretation, but these are supplementary database evidence rather than globally corrected module enrichment. hu.MAP independently recovers spliceosomal assemblies (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1) (hu.MAP huMAP3_00960.1) (hu.MAP huMAP3_07622.1) (hu.MAP huMAP3_06726.1) (hu.MAP huMAP3_06511.1), heterogeneous nuclear ribonucleoprotein assemblies (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_10659.1), chromatin or histone-related assemblies (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_10592.1) (hu.MAP huMAP3_11470.1) (hu.MAP huMAP3_03221.1), lamin complexes (hu.MAP huMAP3_03501.1) (hu.MAP huMAP3_00325.1) (hu.MAP huMAP3_13519.1) (hu.MAP huMAP3_10433.1) (hu.MAP huMAP3_09259.1) (hu.MAP huMAP3_10492.1) (hu.MAP huMAP3_10614.1), and spectrin or cytoskeletal assemblies (hu.MAP huMAP3_07940.1) (hu.MAP huMAP3_05473.1) (hu.MAP huMAP3_09165.1). These overlaps show that much of the module reflects known molecular machinery. They also indicate that the co-abundance network combines several interacting nuclear subsystems rather than representing a single purified protein complex. Genes such as ITPR3, SPIN1, ORMDL3, and several peripheral structural or trafficking genes have limited or absent STRING or hu.MAP support, so their placement may represent co-regulation, cell-state coupling, or indirect association rather than direct physical interaction.

**STRING interactions (score >= 0.7)**: 39 of 946 gene pairs: AQR–EFTUD2 (0.999); AQR–SF3A1 (0.88); AQR–SNRNP200 (0.994); CAPRIN1–DHX9 (0.705); DDX21–DHX9 (0.908); DDX21–HNRNPR (0.73); DDX21–NOP2 (0.761); DDX21–RSL1D1 (0.81); DDX5–DHX9 (0.996); DDX5–HNRNPR (0.844); DDX5–MATR3 (0.894); DDX5–MBNL1 (0.743); DDX5–SMARCA4 (0.782); DHX9–HNRNPL (0.901); DHX9–HNRNPR (0.909); DHX9–MATR3 (0.786); DHX9–MBNL1 (0.876); DHX9–SNRNP200 (0.784); EFTUD2–SF3A1 (0.999); EFTUD2–SNRNP200 (0.999); EFTUD2–SNU13 (0.998); HNRNPL–HNRNPR (0.961); HNRNPL–MATR3 (0.757); HNRNPL–MBNL1 (0.896); HNRNPR–MATR3 (0.714); INTS1–NELFA (0.833); INTS1–POLR2E (0.845); LBR–LMNB1 (0.999); LBR–LMNB2 (0.998); LMNB1–LMNB2 (0.999); NELFA–POLR2E (0.919); NOP2–RSL1D1 (0.982); POLR2E–SUPT16H (0.966); RSL1D1–SNU13 (0.893); SF3A1–SNRNP200 (0.999); SF3A1–SNU13 (0.994); SMARCA4–SMARCC2 (0.999); SNRNP200–SNU13 (0.999); SPTAN1–SPTBN1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Isopeptide bond (FDR = 0.00015, 23 genes); COMPARTMENTS Nuclear lumen (FDR = 0.00029, 25 genes); Keyword Ubl conjugation (FDR = 0.0011, 23 genes); TISSUES Leukemia cell (FDR = 0.0016, 19 genes); RCTM mRNA Splicing - Major Pathway (FDR = 0.0033, 10 genes); Keyword Nucleus (FDR = 0.004, 31 genes); TISSUES Lymphocyte (FDR = 0.0044, 13 genes); Keyword mRNA splicing (FDR = 0.0049, 9 genes); Keyword Spliceosome (FDR = 0.0049, 7 genes); Component Nuclear lumen (FDR = 0.0057, 33 genes); Keyword RNA-binding (FDR = 0.0069, 13 genes); Process RNA metabolic process (FDR = 0.0094, 22 genes); TISSUES Head (FDR = 0.0182, 36 genes); TISSUES T-lymphocyte (FDR = 0.019, 7 genes); Component Spliceosomal complex (FDR = 0.0204, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (SNRNP200, SNU13, EFTUD2, SF3A1; 4/97); huMAP3_07581.1 (HNRNPR, HNRNPL, MATR3; 3/21); huMAP3_10862.1 (MACROH2A1, MACROH2A2, SUPT16H; 3/33); huMAP3_08501.1 (AQR, SNRNP200, EFTUD2; 3/47); huMAP3_09504.1 (AQR, SNRNP200, EFTUD2; 3/51); huMAP3_10625.1 (HNRNPR, HNRNPL, MATR3; 3/57); huMAP3_09945.1 (AQR, SNRNP200, EFTUD2; 3/61); huMAP3_03689.1 (SYNPO, CORO1C; 2/2); huMAP3_03501.1 (LMNB1, LMNB2; 2/2); huMAP3_09555.1 (SYNPO, CORO1C; 2/3); huMAP3_00325.1 (LMNB1, LMNB2; 2/3); huMAP3_04826.1 (SYNPO, CORO1C; 2/4); huMAP3_13519.1 (LMNB1, LMNB2; 2/4); huMAP3_10592.1 (MACROH2A1, MACROH2A2; 2/5); huMAP3_10433.1 (LMNB1, LMNB2; 2/5); huMAP3_07940.1 (SPTBN1, SPTAN1; 2/5); huMAP3_05721.1 (HNRNPL, MATR3; 2/6); huMAP3_07776.1 (SYNPO, CORO1C; 2/7); huMAP3_07225.1 (HNRNPR, HNRNPL; 2/7); huMAP3_05473.1 (SPTBN1, SPTAN1; 2/7); huMAP3_05711.1 (DDX5, CAPRIN1; 2/8); huMAP3_07909.1 (DDX5, CAPRIN1; 2/8); huMAP3_05614.1 (SYNPO, CORO1C; 2/8); huMAP3_09259.1 (LMNB1, LMNB2; 2/8); huMAP3_00960.1 (SNRNP200, EFTUD2; 2/8); huMAP3_09754.1 (DDX5, CAPRIN1; 2/9); huMAP3_09579.1 (SYNPO, CORO1C; 2/9); huMAP3_10492.1 (LMNB1, LMNB2; 2/9); huMAP3_10614.1 (LMNB1, LMNB2; 2/9); huMAP3_07622.1 (SNRNP200, EFTUD2; 2/9); huMAP3_11076.1 (SYNPO, CORO1C; 2/10); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_10784.1 (SYNPO, CORO1C; 2/13); huMAP3_09654.1 (HNRNPR, HNRNPL; 2/13); huMAP3_11470.1 (SMARCA4, SMARCC2; 2/27); huMAP3_10631.1 (DDX5, CAPRIN1; 2/28); huMAP3_10659.1 (HNRNPR, HNRNPL; 2/28); huMAP3_03221.1 (SMARCA4, SMARCC2; 2/28); huMAP3_11111.1 (DDX5, CAPRIN1; 2/29); huMAP3_06726.1 (AQR, SNRNP200; 2/37); huMAP3_09165.1 (SPTBN1, SPTAN1; 2/39); huMAP3_06511.1 (SNU13, SF3A1; 2/79)

### Novelty

The broad biological interpretation is not a new molecular discovery: spliceosomal, heterogeneous nuclear ribonucleoprotein, lamin, chromatin-remodeling, nucleolar, and spectrin relationships are already represented in STRING and hu.MAP. The module may nevertheless provide a potentially useful new observation at the level of coordinated abundance across bone and bone marrow, especially because it brings these established subsystems into one conserved tissue-pair module and includes genes with weak or absent prior interaction evidence. However, the fact sheet does not establish that this exact cross-tissue co-abundance configuration is absent from previous transcriptomic or proteomic studies. Therefore the appropriate conclusion is that the module has a potentially novel systems-level organization, but its component biology is largely established and the module should not be presented as a wholly new pathway.

**Hypothesis.** Hypothesis: the shared module reflects a conserved nuclear maintenance and cell-state program operating in common nucleated cells of bone and bone marrow. In this model, chromatin and nuclear-envelope regulators such as LMNB1, LMNB2, LBR, MACROH2A1, MACROH2A2, SMARCA4, and SMARCC2 establish nuclear organization and transcriptional accessibility; nucleolar factors such as TCOF1, DDX21, NOP2, and RSL1D1 support ribosomal RNA production and ribosome biogenesis; and spliceosomal and RNA-binding factors such as SNRNP200, EFTUD2, AQR, SF3A1, DDX5, DHX9, HNRNPL, and HNRNPR process transcripts. Cell-state inputs involving calcium handling, vesicle trafficking, cytoskeletal organization, mitochondrial activity, and sphingolipid regulation could modulate this nuclear program through ITPR3, RAB5C, CLTB, spectrins, NNT, UQCRC2, and ORMDL3. This hypothesis predicts that the module will track transcriptional and RNA-processing demand or shared progenitor composition more strongly than bone-specific matrix production. It requires validation using cell-resolved data, perturbation, and comparison with purified osteogenic and hematopoietic populations.

### Important genes

#### DDX5

- **Related proteins** (co-abundance neighbors): DHX9 (0.86), ITPR3 (0.86); STRING partners: DHX9 (0.996), HNRNPR (0.844), MATR3 (0.894), MBNL1 (0.743), SMARCA4 (0.782)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_05711.1, huMAP3_07909.1, huMAP3_09754.1, huMAP3_10631.1, huMAP3_11111.1
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 is a highly connected RNA helicase within the module and links DHX9, HNRNPR, MATR3, MBNL1, and SMARCA4 in STRING. It is present in the globally significant nucleic-acid binding, nuclear-lumen, RNA-binding, RNA-splicing, and transcription-regulatory terms (8 globally significant GO/KEGG terms, q_global 0.00471–0.044; see the table). Its established functions include RNA restructuring, spliceosome regulation, transcriptional co-regulation, and small noncoding RNA processing. It also has substantial literature support and disease associations across infection and cancer contexts.
- **Conclusion**: Established evidence supports DDX5 as a central integrator of RNA processing and transcriptional regulation in this module. Its co-abundance with chromatin and RNA-binding factors is consistent with a shared gene-expression program. A role for DDX5 in coordinating the bone and bone-marrow state represented by this module remains a hypothesis rather than a demonstrated tissue-specific function.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.90), DHX9 (0.86); STRING partners: AQR (0.994), DHX9 (0.784), EFTUD2 (0.999), SF3A1 (0.999), SNU13 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_06726.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is a core U5 small nuclear ribonucleoprotein helicase and occupies the spliceosomal backbone of the module. It connects with EFTUD2 and DHX9 in the network and has very strong STRING relationships with AQR, EFTUD2, SF3A1, and SNU13. It occurs in the globally significant RNA-binding, RNA-splicing, nuclear-lumen, and catalytic-step spliceosome terms (5 globally significant GO/KEGG terms, q_global 0.00471–0.0389; see the table). Its established spliceosomal role, disease associations involving retinal degeneration, and meaningful literature support make it a strong functional anchor.
- **Conclusion**: Established evidence identifies SNRNP200 as a genuine spliceosome-centered component rather than a generic abundance marker. Its presence supports the interpretation that transcript maturation is a core function of the module. The module does not show that SNRNP200 specifically controls bone or marrow biology; that tissue connection is a hypothesis.

#### LMNB1

- **Related proteins** (co-abundance neighbors): LMNB2 (0.89), MATR3 (0.86), HNRNPL (0.82); STRING partners: LBR (0.999), LMNB2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_03501.1, huMAP3_00325.1, huMAP3_13519.1, huMAP3_10433.1, huMAP3_09259.1, huMAP3_10492.1, huMAP3_10614.1
- **Function (MyGene.info)**: lamin B1. This gene encodes one of the two B-type lamin proteins and is a component of the nuclear lamina. A duplication of this gene is associated with autosomal dominant adult-onset leukodystrophy (ADLD). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: microcephaly 26, primary, autosomal dominant (0.723); autosomal dominant primary microcephaly (0.675); adult-onset autosomal dominant demyelinating leukodystrophy (0.670); hereditary disease (0.488); Syndrome with microcephaly as major feature (0.487)
- **Europe PMC papers**: 3851
- **Why important**: LMNB1 is a nuclear-envelope scaffold with tissue enhancement in bone marrow and lymphoid tissue, and it is enriched in the globally significant nuclear-lumen, heterochromatin, epigenetic-regulation, nucleic-acid binding, and negative gene-regulation terms (8 globally significant GO/KEGG terms, q_global 0.00471–0.0473; see the table). It forms a strongly supported lamin backbone with LMNB2 and LBR in STRING and recurs across multiple hu.MAP lamin complexes (hu.MAP huMAP3_03501.1) (hu.MAP huMAP3_00325.1) (hu.MAP huMAP3_13519.1) (hu.MAP huMAP3_10433.1) (hu.MAP huMAP3_09259.1) (hu.MAP huMAP3_10492.1) (hu.MAP huMAP3_10614.1). It has extensive literature and disease associations involving leukodystrophy, microcephaly, and nuclear-envelope biology.
- **Conclusion**: Established evidence supports LMNB1 as the principal nuclear-architecture component of the module and provides a plausible bridge between nuclear structure, heterochromatin, and transcriptional regulation. Its bone-marrow enhancement strengthens the relevance of this program to the shared tissue context, but does not prove a specialized osteogenic mechanism.

#### SMARCA4

- **Related proteins** (co-abundance neighbors): MACROH2A2 (0.90); STRING partners: DDX5 (0.782), SMARCC2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center, Nucleoli rim; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_11470.1, huMAP3_03221.1
- **Function (MyGene.info)**: SWI/SNF related BAF chromatin remodeling complex subunit ATPase 4. The protein encoded by this gene is a member of the SWI/SNF family of proteins and is similar to the brahma protein of Drosophila. Members of this family have helicase and ATPase activities and are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI, wh…
- **Diseases (Open Targets)**: intellectual disability, autosomal dominant 16 (0.796); rhabdoid tumor predisposition syndrome 2 (0.788); familial rhabdoid tumor (0.685); rhabdoid tumor (0.627); medulloblastoma (0.586)
- **Europe PMC papers**: 9906
- **Why important**: SMARCA4 is the ATPase component of the SWI/SNF chromatin-remodeling machinery and is linked to SMARCC2 by a strong STRING relationship and by hu.MAP chromatin-remodeling complexes (hu.MAP huMAP3_11470.1) (hu.MAP huMAP3_03221.1). It participates in the globally significant nucleic-acid binding, nuclear-lumen, RNA-binding, rRNA-transcription, and transcription-regulatory terms (9 globally significant GO/KEGG terms, q_global 0.00471–0.0473; see the table). Its role in chromatin remodeling, RNA polymerase regulation, and nucleolar transcription connects the chromatin and RNA-processing arms of the module. It also has extensive literature and strong disease associations involving developmental disorders and rhabdoid tumors.
- **Conclusion**: Established evidence supports SMARCA4 as a mechanistic bridge between chromatin state and transcriptional output within the module. Its co-abundance with RNA helicases and nucleolar factors is biologically coherent. Whether altered SMARCA4 activity drives the conserved bone and marrow module is an untested hypothesis.

#### TCOF1

- **Related proteins** (co-abundance neighbors): ORMDL3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: treacle ribosome biogenesis factor 1. This gene encodes a nucleolar protein with a LIS1 homology domain. The protein is involved in ribosomal DNA gene transcription through its interaction with upstream binding factor (UBF). Mutations in this gene have been associated with Treacher Collins syndrome, a disorder which includes abnormal craniofacial development. Multiple transcript variants encoding different isoforms have been found for…
- **Diseases (Open Targets)**: Treacher Collins syndrome 1 (0.761); Treacher-Collins syndrome (0.713); hereditary disease (0.472); neurodegenerative disease (0.459); Emery-Dreifuss muscular dystrophy 4, autosomal dominant (0.266)
- **Europe PMC papers**: 1248
- **Why important**: TCOF1 is a nucleolar ribosome-biogenesis factor involved in ribosomal DNA transcription and skeletal-system development. It is included in the globally significant nucleic-acid binding, nuclear-lumen, rRNA-transcription, nucleolar large rRNA transcription, RNA polymerase I transcription, and RNA-binding terms (6 globally significant GO/KEGG terms, q_global 0.00471–0.0389; see the table). Its position connects the module to DDX21, NOP2, RSL1D1, and other nucleolar or RNA-processing factors. It has substantial literature and established disease associations with Treacher Collins syndrome, making it particularly relevant to craniofacial and skeletal biology.
- **Conclusion**: Established evidence supports TCOF1 as a meaningful nucleolar and skeletal-development-related component rather than a generic housekeeping marker. Its inclusion strengthens a model in which ribosome biogenesis and transcriptional capacity contribute to the shared module. A direct role in the observed bone and bone-marrow co-abundance pattern remains hypothetical.

#### ITPR3

- **Related proteins** (co-abundance neighbors): POLR2E (0.89), CLTB (0.88), RAB5C (0.87), DDX5 (0.86), CAPRIN1 (0.85), SUPT16H (0.82), DHX9 (0.82), MBNL1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inositol 1,4,5-trisphosphate receptor type 3. This gene encodes a receptor for inositol 1,4,5-trisphosphate, a second messenger that mediates the release of intracellular calcium. The receptor contains a calcium channel at the C-terminus and the ligand-binding site at the N-terminus. Knockout studies in mice suggest that type 2 and type 3 inositol 1,4,5-trisphosphate receptors play a key role in exocrine secretion underlying energy metabolism…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease, demyelinating, type 1J (0.656); immunodeficiency 133 with ectodermal dysplasia with or without peripheral neuropathy (0.532); type 1 diabetes mellitus (0.496); rheumatoid arthritis (0.454); chronic hepatitis B virus infection (0.443)
- **Europe PMC papers**: 2080
- **Why important**: ITPR3 has the strongest network position in the supplied module and links RNA-processing, transcription-associated, vesicular, and cytoskeletal neighbors, including POLR2E, CLTB, RAB5C, DDX5, CAPRIN1, SUPT16H, DHX9, and MBNL1. It is included in the globally significant nuclear-lumen term (GO:CC nuclear lumen; q_global = 0.00486), while its established function is an intracellular calcium-release channel involved in calcium signaling and secretion. It has no recorded STRING partners or hu.MAP complexes in the fact sheet, so its module placement is especially informative as a co-abundance association rather than a known physical interaction. It also has substantial literature and disease associations including immunodeficiency, rheumatoid arthritis, and diabetes.
- **Conclusion**: Established evidence supports ITPR3 as a calcium-signaling and vesicle-associated gene that may connect cellular signaling to the nuclear RNA-processing program. Its central network position suggests an important systems-level bridge, but the absence of recorded STRING and hu.MAP relationships argues against claiming a direct molecular complex with the nuclear factors. Any role in coupling calcium signals to the conserved bone and marrow module is a hypothesis.

## Module 3

**Tissue pair**: bone and bone_marrow  
**Genes (32)**: ALG8, ANXA4, CHMP1A, COMMD1, CRYAB, COPS7B, CSTF3, DCUN1D1, QDPR, DOHH, DPP3, ELOC, FDPS, SLC2A6, KIF2C, LCLAT1, LGALS3, LZTFL1, MSH2, NIT2, PHPT1, PSMF1, RFC2, RRP1B, SLC35B2, SEC24C, SF3B3, THUMPD1, TRAPPC6B, USP10, UCHL3, UFD1

### Function

This module does not have a statistically supported GO or KEGG functional enrichment: no globally significant GO/KEGG term passed global correction. Its internal structure instead suggests a heterogeneous cellular-maintenance program. The strongest network hub is SLC2A6, which links glucose and hexose transport to genes involved in RNA processing, DNA maintenance, vesicle traffic, and protein quality control. ALG8 connects the network to protein N-linked glycosylation, while UCHL3, PSMF1, UFD1, COPS7B, DCUN1D1, COMMD1, and ELOC point toward ubiquitin-dependent proteostasis and neddylation-related biology. These latter themes are supported only as supplementary STRING evidence by (STRING RCTM Neddylation; within-query FDR = 0.0005) and (STRING RCTM Post-translational protein modification; within-query FDR = 0.0162), not as globally corrected enrichment. Additional branches involve mismatch repair through MSH2 and RFC2, vesicle transport through SEC24C and TRAPPC6B, cytoskeletal or mitotic processes through KIF2C and CHMP1A, and metabolic functions through NIT2, FDPS, and QDPR. Overall, the module is best interpreted as a mixed housekeeping and biosynthetic co-abundance program rather than a discrete bone-specific pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins. Only a small minority are annotated as secreted, with LGALS3 explicitly secreted to blood; most members are intracellular, cytosolic, nuclear, vesicular, or membrane-associated. HPA indicates low tissue specificity for most genes, with a smaller set showing enhancement in brain, liver, testis, lymphoid tissue, or other tissues. Cell-type enhancement is widespread, especially for esophageal and germ-cell populations, rather than being concentrated in bone or marrow lineages. Most genes have low immune-cell specificity, although LGALS3 and USP10 show informative myeloid or neutrophil associations and SLC2A6 is enhanced in a monocyte population. Bone-marrow protein detection is common among the genes with available data, whereas the supplied bone tissue comparison has no matching HPA protein result. Thus, the shared module could reflect broadly expressed cellular machinery, the cellular mixture represented in marrow samples, or a shared cell population, rather than secretion or a bone-lineage program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited set of established relationships. COMMD1 is strongly connected to ELOC, and ELOC also connects to COPS7B and DCUN1D1. MSH2 connects to RFC2, and PSMF1 connects to UFD1. These relationships provide plausible local anchors for neddylation, ubiquitin regulation, proteasome or ER-associated degradation, and DNA repair. The supplementary STRING annotations (STRING RCTM Neddylation; within-query FDR = 0.0005) and (STRING RCTM Post-translational protein modification; within-query FDR = 0.0162) similarly support protein modification, but they are not global enrichment evidence. Most co-abundance edges are not represented by high-confidence STRING relationships, including the central SLC2A6 connections and the LZTFL1-centered branch. No hu.MAP complex contains multiple module members. Therefore, the network is not simply a recovered known protein complex; it combines a few established interaction islands with many relationships that may represent co-regulation, shared cell composition, or indirect cellular-state effects.

**STRING interactions (score >= 0.7)**: 5 of 496 gene pairs: COMMD1–ELOC (0.955); COPS7B–ELOC (0.838); DCUN1D1–ELOC (0.765); MSH2–RFC2 (0.884); PSMF1–UFD1 (0.702)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Neddylation (FDR = 0.0005, 8 genes); RCTM Post-translational protein modification (FDR = 0.0162, 13 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The co-abundance pattern may be a new observation because it is shared by bone and bone marrow while lacking a matching multi-member hu.MAP complex and showing only sparse high-confidence STRING support. However, it should not be called a newly discovered biological pathway. The absence of STRING or hu.MAP support alone does not establish novelty, and the lack of globally corrected GO or KEGG enrichment weakens a claim of a unified new function. The most defensible claim is that this is a potentially novel cross-tissue co-abundance configuration assembled from partly known cellular processes. Replication in independent bone and marrow datasets, preservation after cell-composition adjustment, and experimental testing of the unconnected co-abundance relationships would be needed to establish biological novelty.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program in bone and bone marrow in which carbohydrate transport and metabolic supply, glycoprotein processing, vesicle trafficking, and ubiquitin-dependent protein quality control are coordinated. SLC2A6 may mark the metabolic component; ALG8 and vesicle genes may support processing and trafficking of newly synthesized proteins; and UCHL3, UFD1, COPS7B, DCUN1D1, COMMD1, and ELOC may regulate protein turnover and modification. LGALS3 and the HPA cell-type patterns raise the alternative possibility that part of the signal comes from shared immune or stromal cell content. This is a hypothesis rather than an established pathway, because global functional enrichment is absent and direct complex evidence is limited.

### Important genes

#### SLC2A6

- **Related proteins** (co-abundance neighbors): RRP1B (0.97), USP10 (0.93), THUMPD1 (0.92), MSH2 (0.89), QDPR (0.86), SEC24C (0.85), CSTF3 (0.84), NIT2 (0.82), SF3B3 (0.82), DPP3 (0.81), DCUN1D1 (0.81), CHMP1A (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 2 member 6. Hexose transport into mammalian cells is catalyzed by a family of membrane proteins, including SLC2A6, that contain 12 transmembrane domains and a number of critical conserved residues.[supplied by OMIM, Jul 2002].
- **Diseases (Open Targets)**: osteoarthritis (0.188); Alzheimer disease (0.130); cancer (0.080); lung adenocarcinoma (0.076); metabolic syndrome (0.074)
- **Europe PMC papers**: 559
- **Why important**: SLC2A6 is the central network hub by weighted connectivity and links many otherwise disparate branches, including USP10, MSH2, SEC24C, CSTF3, and QDPR. Its established function is hexose and glucose transport, with annotations involving glycolytic regulation and dehydroascorbate transport. HPA shows tissue enhancement in brain and lymphoid tissue and immune-cell enhancement in a monocyte population. It has no supplied high-confidence STRING partner and no hu.MAP support, making its hub position especially informative for interpreting the co-abundance structure rather than a known complex. Its disease associations include osteoarthritis, Alzheimer disease, cancer, lung adenocarcinoma, and metabolic syndrome, with a substantial literature.
- **Conclusion**: Established: SLC2A6 is a broadly relevant hexose transporter and the principal network connector in this module. Hypothesis: its co-abundance may report shared metabolic demand or cellular composition in bone and marrow, but the data do not establish a bone-specific SLC2A6 mechanism.

#### ALG8

- **Related proteins** (co-abundance neighbors): KIF2C (0.98), CHMP1A (0.93), COPS7B (0.93), LGALS3 (0.93), SLC35B2 (0.90), RFC2 (0.89), NIT2 (0.88), THUMPD1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ALG8 alpha-1,3-glucosyltransferase. This gene encodes a member of the ALG6/ALG8 glucosyltransferase family. The encoded protein catalyzes the addition of the second glucose residue to the lipid-linked oligosaccharide precursor for N-linked glycosylation of proteins. Mutations in this gene have been associated with congenital disorder of glycosylation type Ih (CDG-Ih). Alternatively spliced transcript variants encoding different isof…
- **Diseases (Open Targets)**: ALG8-congenital disorder of glycosylation (0.818); polycystic liver disease 3 with or without kidney cysts (0.749); autosomal dominant polycystic liver disease (0.608); neurodegenerative disease (0.538); familial cystic renal disease (0.515)
- **Europe PMC papers**: 948
- **Why important**: ALG8 is a network bridge connecting the SLC2A6-centered region with KIF2C, CHMP1A, COPS7B, LGALS3, SLC35B2, RFC2, and NIT2. Its established function is addition of a glucose residue during lipid-linked oligosaccharide synthesis for protein N-linked glycosylation, and it is associated with congenital disorders of glycosylation and cystic kidney or liver disease. It appears in the supplementary STRING post-translational modification term (STRING RCTM Post-translational protein modification; within-query FDR = 0.0162) and is detected in bone marrow by HPA. Its position makes it a plausible biosynthetic and secretory-processing anchor, despite the absence of global GO or KEGG enrichment and direct STRING or hu.MAP complex evidence.
- **Conclusion**: Established: ALG8 supports N-linked glycosylation and is a structurally important bridge in the module. Hypothesis: ALG8 may couple metabolic state to protein processing in the shared tissue context, but a specific bone or marrow role is not demonstrated.

#### LZTFL1

- **Related proteins** (co-abundance neighbors): PSMF1 (0.93), UCHL3 (0.92), NIT2 (0.88), FDPS (0.88), PHPT1 (0.86), ANXA4 (0.85), DOHH (0.83), UFD1 (0.81), ELOC (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: leucine zipper transcription factor like 1. This gene encodes a ubiquitously expressed protein that localizes to the cytoplasm. This protein interacts with Bardet-Biedl Syndrome (BBS) proteins and, through its interaction with BBS protein complexes, regulates protein trafficking to the ciliary membrane. Nonsense mutations in this gene cause a form of Bardet-Biedl Syndrome; a ciliopathy characterized in part by polydactyly, obesity, cognitiv…
- **Diseases (Open Targets)**: Bardet-Biedl syndrome (0.791); COVID-19 (0.493); respiratory failure (0.405); polydactyly (0.371); eye disorder (0.370)
- **Europe PMC papers**: 1015
- **Why important**: LZTFL1 has one of the strongest network positions and connects PSMF1, UCHL3, NIT2, FDPS, PHPT1, ANXA4, DOHH, and UFD1. Its established function concerns ciliary membrane trafficking through interactions with Bardet-Biedl syndrome proteins; pathogenic variants cause Bardet-Biedl syndrome, and the gene has also been proposed to function as a tumour suppressor. HPA places it in a cytosolic, broadly expressed context with enhancement in ciliated cells, spermatocytes, and thymocytes. It has no supplied STRING partner or hu.MAP complex, so its network position is a co-abundance observation rather than evidence of a known physical complex. Its disease associations include Bardet-Biedl syndrome, polydactyly, respiratory failure, and COVID-19.
- **Conclusion**: Established: LZTFL1 is a ciliary-trafficking and disease-associated protein that occupies a prominent integrative position in this module. Hypothesis: it may connect proteostasis and trafficking states in the shared samples, but ciliary biology is not established as the module function.

#### UCHL3

- **Related proteins** (co-abundance neighbors): LZTFL1 (0.92), CRYAB (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin C-terminal hydrolase L3. The protein encoded by this gene is a member of the deubiquitinating enzyme family. Members of this family are proteases that catalyze the removal of ubiquitin from polypeptides and are divided into five classes, depending on the mechanism of catalysis. This protein may hydrolyze the ubiquitinyl-N-epsilon amide bond of ubiquitinated proteins to regenerate ubiquitin for another catalytic cycle. Alt…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.354); liver disorder (0.232); placenta praevia (0.147); Varicose veins (0.144); smoking initiation (0.140)
- **Europe PMC papers**: 998
- **Why important**: UCHL3 connects the LZTFL1 branch to CRYAB and is included in both supplementary STRING terms (STRING RCTM Neddylation; within-query FDR = 0.0005) and (STRING RCTM Post-translational protein modification; within-query FDR = 0.0162). Its established function is deubiquitination and participation in ubiquitin-dependent protein catabolism, with additional annotation in homologous-recombination repair. HPA detects it in bone marrow and shows enhancement in several epithelial and germ-cell populations, while immune-cell specificity is low. Its disease associations include skeletal-system abnormality, liver disorder, placenta praevia, and varicose veins. Its literature volume is substantial relative to many less studied module members, making it a useful mechanistic candidate for the proteostasis interpretation.
- **Conclusion**: Established: UCHL3 provides credible enzymatic support for the supplementary ubiquitin and post-translational-modification signal. Hypothesis: it may help coordinate protein turnover with the other module branches, but the co-abundance data do not prove that it directly drives the module.

#### KIF2C

- **Related proteins** (co-abundance neighbors): ALG8 (0.98); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Immune cell enhanced; location Nucleoplasm, Midbody, Centrosome; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 2C. This gene encodes a kinesin-like protein that functions as a microtubule-dependent molecular motor. The encoded protein can depolymerize microtubules at the plus end, thereby promoting mitotic chromosome segregation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.320); Abnormality of the skeletal system (0.165); placenta praevia (0.159); neuroendocrine neoplasm (0.159); placental retention (0.129)
- **Europe PMC papers**: 2214
- **Why important**: KIF2C has limited local connectivity but is notable because HPA reports group enrichment in bone marrow and lymphoid tissue and immune-cell enhancement in T-reg cells. Its established function is microtubule depolymerization and mitotic chromosome segregation, including metaphase alignment and cytoskeleton-dependent transport. It connects to ALG8, placing cell division and cytoskeletal behavior near the glycosylation branch. Its disease associations include neurodegenerative disease, skeletal-system abnormality, placental disorders, and neuroendocrine neoplasm, and it has a large literature.
- **Conclusion**: Established: KIF2C is a marrow-relevant marker of mitotic and microtubule biology. Hypothesis: its presence may indicate proliferating marrow cells or coordinated cytoskeletal demand, but it does not establish that the entire module is a proliferation program.

#### LGALS3

- **Related proteins** (co-abundance neighbors): ALG8 (0.93); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galectin 3. This gene encodes a member of the galectin family of carbohydrate binding proteins. Members of this protein family have an affinity for beta-galactosides. The encoded protein is characterized by an N-terminal proline-rich tandem repeat domain and a single C-terminal carbohydrate recognition domain. This protein can self-associate through the N-terminal domain allowing it to bind to multivalent sac…
- **Diseases (Open Targets)**: melanoma (0.126); COVID-19 (0.123); neoplasm (0.120); hepatocellular carcinoma (0.117); cancer (0.117)
- **Europe PMC papers**: 13803
- **Why important**: LGALS3 is connected to ALG8 and is the clearest composition-sensitive member because HPA identifies it as secreted to blood and enriched in several monocyte and myeloid cell categories. Its established function is beta-galactoside binding, with roles in monocyte and neutrophil chemotaxis, epithelial differentiation, T-cell proliferation, and extracellular, cytoplasmic, and nuclear signaling. Its disease associations include melanoma, hepatocellular carcinoma, COVID-19, and cancer, and it has an especially extensive literature. The relatively modest network position means it is more useful as a biological-context marker than as a structural hub.
- **Conclusion**: Established: LGALS3 can report immune, extracellular, and tissue-composition influences in marrow samples. Hypothesis: LGALS3 may help explain why this module is shared across tissues through common immune or stromal content, but the data do not show that secreted LGALS3 organizes the intracellular network.

## Module 4

**Tissue pair**: bone and bone_marrow  
**Genes (39)**: ANXA6, CNN2, CNOT12, CFL2, DBNL, DPYSL2, DPYSL3, FERMT2, FLNA, FLNB, FLNC, FSCN1, GARS1, GSN, HSP90AA1, PKM, LDHA, MAP1B, MVP, FAM114A1, PALLD, PDLIM1, PDLIM4, PGK1, PALM2AKAP2, PLIN3, RNH1, S100A13, PHGDH, CTTN, TUBB4B, TUBB6, TKT, TLN1, UBA5, USP5, UGDH, VCL, WDR1

### Function

This is a conserved actin–adhesion–motility module. The primary evidence is the globally corrected enrichment for actin binding (GO:MF actin binding; q_global = 4.44e-07), podosome (GO:CC podosome; q_global = 1.73e-06), actin cytoskeleton organization (GO:BP actin cytoskeleton organization; q_global = 2e-06), actin filament-based processes (GO:BP actin filament-based process; q_global = 6.54e-06), actin filament binding (GO:MF actin filament binding; q_global = 6.82e-06), cytoskeleton organization (GO:BP cytoskeleton organization; q_global = 1.09e-05), actin cytoskeleton (GO:CC actin cytoskeleton; q_global = 2.53e-05), and cytoskeletal protein binding (GO:MF cytoskeletal protein binding; q_global = 3.44e-05). Enrichment for anchoring junctions, cell junctions, focal adhesions, cell-substrate junctions, lamellipodia, leading edges, cell motility, and cell migration (7 globally significant GO/KEGG terms, q_global 5.45e-05–0.0123; see the table) supports a coordinated program of actin remodeling, cell adhesion, protrusion, and movement. The contractile and sarcomeric terms (9 globally significant GO/KEGG terms, q_global 0.000357–0.00636; see the table) are consistent with force-bearing actin bundles, although they should not be interpreted as evidence that the entire module is muscle-specific. Extracellular vesicle and exosome terms (5 globally significant GO/KEGG terms, q_global 0.00105–0.00363; see the table) suggest an additional vesicle-associated component. The metabolic genes and their STRING links (4 supplementary STRING terms; within-query FDR 5.88e-06–7.35e-06) indicate coupling to glycolysis and cellular energy production rather than a separate dominant function. Thus, the best interpretation is a structural and dynamic cytoskeletal program involved in adhesion, force transmission, protrusion, migration, and vesicle-associated membrane remodeling.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: the HPA summary identifies only a small secreted subset, with GSN secreted to blood and S100A13 secreted in other tissues, while most proteins are intracellular or membrane-associated. Most genes have low tissue specificity, and many are cell-type enhanced rather than restricted to bone or bone marrow. HPA points particularly toward smooth muscle cells, platelets, megakaryocytes, epithelial populations, and several myeloid populations. The presence of platelet and megakaryocyte-associated genes such as TLN1, VCL, WDR1, DBNL, and FLNA, together with monocyte, dendritic-cell, neutrophil, and other immune-cell signals, means that the shared module may partly reflect common blood or stromal-cell content in the samples. The muscle-associated signal, including CFL2, FLNC, PDLIM1, and CNN2, is compatible with a contractile cytoskeletal program but does not establish skeletal-muscle contamination. Bone-marrow protein detection is present for many module proteins, whereas matched HPA protein evidence is unavailable for bone, so the tissue-level interpretation should remain cautious.

**GO/KEGG enrichment**: 56 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF actin binding | 4.44e-07 | CFL2, CNN2, DBNL, FERMT2, FLNA, FLNB, FLNC, FSCN1, GSN, MAP1B, PALLD, PDLIM1, PDLIM4, TLN1, VCL, WDR1 |
| GO:CC podosome | 1.73e-06 | CTTN, DBNL, FLNA, FSCN1, GSN, PALLD, VCL, WDR1 |
| GO:BP actin cytoskeleton organization | 2e-06 | CFL2, CNN2, CTTN, DBNL, DPYSL3, FERMT2, FLNA, FLNB, FLNC, FSCN1, GSN, PALLD, PDLIM1, PDLIM4, RNH1, TLN1, WDR1 |
| GO:BP actin filament-based process | 6.54e-06 | CFL2, CNN2, CTTN, DBNL, DPYSL3, FERMT2, FLNA, FLNB, FLNC, FSCN1, GSN, PALLD, PDLIM1, PDLIM4, RNH1, TLN1, WDR1 |
| GO:MF actin filament binding | 6.82e-06 | CFL2, CNN2, DBNL, FERMT2, FLNA, FLNB, FLNC, FSCN1, GSN, TLN1, VCL, WDR1 |
| GO:BP cytoskeleton organization | 1.09e-05 | CFL2, CNN2, CTTN, DBNL, DPYSL2, DPYSL3, FERMT2, FLNA, FLNB, FLNC, FSCN1, GSN, MAP1B, PALLD, PDLIM1, PDLIM4, RNH1, TLN1, TUBB4B, TUBB6, WDR1 |
| GO:CC actin cytoskeleton | 2.53e-05 | CFL2, CNN2, CTTN, DBNL, DPYSL3, FERMT2, FLNA, FLNB, FSCN1, GSN, PALLD, PDLIM1, PDLIM4, VCL, WDR1 |
| GO:MF cytoskeletal protein binding | 3.44e-05 | CFL2, CNN2, DBNL, DPYSL3, FERMT2, FLNA, FLNB, FLNC, FSCN1, GSN, HSP90AA1, MAP1B, PALLD, PDLIM1, PDLIM4, TLN1, VCL, WDR1 |
| GO:CC anchoring junction | 5.45e-05 | ANXA6, CNN2, CNOT12, CTTN, DBNL, FERMT2, FLNA, FLNB, FLNC, FSCN1, GSN, PALLD, PDLIM1, PDLIM4, TLN1, VCL, WDR1 |
| GO:MF cell adhesion molecule binding | 9.97e-05 | CNN2, CNOT12, CTTN, DBNL, FERMT2, FLNA, FLNB, FSCN1, LDHA, PALLD, PDLIM1, PKM, PLIN3, TLN1, VCL |
| GO:CC cytoskeleton | 0.000248 | CFL2, CNN2, CNOT12, CTTN, DBNL, DPYSL2, DPYSL3, FERMT2, FLNA, FLNB, FLNC, FSCN1, GSN, MAP1B, MVP, PALLD, PDLIM1, PDLIM4, TLN1, TUBB4B, TUBB6, VCL, WDR1 |
| GO:CC I band | 0.000357 | CFL2, FERMT2, FLNA, FLNB, FLNC, PALLD, PDLIM1, PDLIM4 |
| GO:MF cadherin binding | 0.000533 | CNN2, CNOT12, CTTN, DBNL, FLNA, FLNB, FSCN1, LDHA, PDLIM1, PKM, PLIN3, TLN1, VCL |
| GO:CC myofibril | 0.000665 | CFL2, FERMT2, FLNA, FLNB, FLNC, PALLD, PDLIM1, PDLIM4, VCL |
| GO:CC contractile muscle fiber | 0.000665 | CFL2, FERMT2, FLNA, FLNB, FLNC, PALLD, PDLIM1, PDLIM4, VCL |

### STRING and hu.MAP

STRING independently supports a dense, known actin network. The strongest relationships include the CFL2–CTTN and CFL2–WDR1 links, the FLNA–TLN1 and TLN1–VCL links, the filamin network involving FLNA, FLNB, and FLNC, and interactions among GSN, CTTN, FSCN1, FERMT2, and focal-adhesion components (7 supplementary STRING terms; within-query FDR 3.41e-10–6.97e-06). STRING also identifies a coherent metabolic subnetwork involving LDHA, PGK1, PKM, and TKT (4 supplementary STRING terms; within-query FDR 5.88e-06–7.35e-06), plus a literature-linked relationship between cortactin, fascin, and extracellular-vesicle release (STRING PMID (2018) Cortactin and fascin-1 regulate extracellular vesicle release by controlling endosomal trafficking or invadopodia formation and function.; within-query FDR = 8.5e-06). These observations show that much of the module recapitulates established protein relationships rather than an entirely unknown interaction system. hu.MAP provides complementary support for CFL2–WDR1 complexes (hu.MAP huMAP3_02272.1) (hu.MAP huMAP3_06026.1) (hu.MAP huMAP3_11076.1), DPYSL2–DPYSL3 complexes (hu.MAP huMAP3_00051.1) (hu.MAP huMAP3_11599.1) (hu.MAP huMAP3_11626.1), TUBB4B–TUBB6 complexes (hu.MAP huMAP3_09233.1) (hu.MAP huMAP3_10475.1) (hu.MAP huMAP3_10665.1), and a broader complex containing PDLIM1, PKM, and GARS1 (hu.MAP huMAP3_14442.1). The partial membership of the module in these complexes supports several mechanistic subassemblies, but it does not prove that all module proteins form one physical complex or that every co-abundance relationship is a direct interaction.

**STRING interactions (score >= 0.7)**: 50 of 741 gene pairs: CFL2–CTTN (0.996); CFL2–FLNA (0.888); CFL2–FLNB (0.821); CFL2–FLNC (0.841); CFL2–FSCN1 (0.758); CFL2–GSN (0.864); CFL2–VCL (0.83); CFL2–WDR1 (0.993); CNN2–VCL (0.711); CTTN–FSCN1 (0.771); CTTN–GSN (0.987); CTTN–TLN1 (0.937); CTTN–VCL (0.97); DPYSL2–DPYSL3 (0.976); DPYSL2–MAP1B (0.756); DPYSL3–PDLIM4 (0.748); FERMT2–FLNA (0.852); FERMT2–FLNB (0.757); FERMT2–FLNC (0.747); FERMT2–TLN1 (0.705); FERMT2–VCL (0.896); FLNA–FLNB (0.979); FLNA–FLNC (0.907); FLNA–FSCN1 (0.887); FLNA–GSN (0.831); FLNA–TLN1 (0.998); FLNA–VCL (0.998); FLNA–WDR1 (0.874); FLNB–FLNC (0.921); FLNB–FSCN1 (0.788); FLNB–GSN (0.745); FLNB–TLN1 (0.995); FLNB–VCL (0.995); FLNC–FSCN1 (0.794); FLNC–GSN (0.749); FLNC–TLN1 (0.996); FLNC–VCL (0.994); GSN–TLN1 (0.941); GSN–VCL (0.918); HSP90AA1–PGK1 (0.713); LDHA–PGK1 (0.923); LDHA–PKM (0.997); LDHA–TKT (0.925); PDLIM1–VCL (0.706); PGK1–PKM (0.936); PGK1–TKT (0.831); PHGDH–PKM (0.718); PKM–TKT (0.951); TLN1–VCL (0.999); TLN1–WDR1 (0.744)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Actin binding (FDR = 3.41e-10, 18 genes); Function Cytoskeletal protein binding (FDR = 5.06e-09, 21 genes); Function Actin filament binding (FDR = 4.75e-08, 13 genes); Component Actin cytoskeleton (FDR = 1.14e-06, 15 genes); COMPARTMENTS Actin cytoskeleton (FDR = 2.5e-06, 14 genes); Keyword Cytoskeleton (FDR = 2.5e-06, 19 genes); COMPARTMENTS Podosome (FDR = 2.7e-06, 7 genes); Component Podosome (FDR = 4.12e-06, 7 genes); COMPARTMENTS Cell junction (FDR = 5.88e-06, 16 genes); COMPARTMENTS Extracellular membrane-bounded organelle (FDR = 5.88e-06, 14 genes); COMPARTMENTS Extracellular vesicle (FDR = 5.88e-06, 14 genes); COMPARTMENTS Anchoring junction (FDR = 6.97e-06, 14 genes); COMPARTMENTS Extracellular exosome (FDR = 7.22e-06, 13 genes); COMPARTMENTS Extracellular region (FDR = 7.35e-06, 17 genes); PMID (2018) Cortactin and fascin-1 regulate extracellular vesicle release by controlling endosomal trafficking or invadopodia formation and function. (FDR = 8.5e-06, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (PDLIM1, PKM, GARS1; 3/57); huMAP3_02272.1 (WDR1, CFL2; 2/2); huMAP3_06026.1 (WDR1, CFL2; 2/5); huMAP3_00051.1 (DPYSL3, DPYSL2; 2/6); huMAP3_11599.1 (DPYSL3, DPYSL2; 2/8); huMAP3_11076.1 (WDR1, CFL2; 2/10); huMAP3_09233.1 (TUBB4B, TUBB6; 2/34); huMAP3_10475.1 (TUBB4B, TUBB6; 2/39); huMAP3_11626.1 (DPYSL3, DPYSL2; 2/42); huMAP3_10665.1 (TUBB4B, TUBB6; 2/42)

### Novelty

The module should not be described as a new discovery of actin biology: its central components and many of its relationships are already established by GO annotation, STRING, hu.MAP, and extensive gene-specific literature. Its potentially novel aspect is the conserved co-abundance pattern across bone and bone marrow, especially the coordinated connection of actin remodeling, focal adhesion, podosome biology, microtubule-associated proteins, glycolytic enzymes, and vesicle-associated proteins. The fact sheet does not document a prior report of this exact tissue-pair module, so the network-level observation may be novel, but that is not demonstrated by the absence of a matching STRING or hu.MAP complex. A defensible novelty claim is therefore that this is a potentially new tissue-pair co-abundance configuration assembled from largely known molecular components. Confirmation would require replication in independent bone and bone-marrow cohorts, cell-composition adjustment, and comparison with published tissue-specific co-expression modules.

**Hypothesis.** Hypothesis: the shared module reflects a mechanically active, migratory and adhesive cell-state program present in common bone and bone-marrow cellular populations. Integrin-associated adhesion machinery involving FERMT2, TLN1, VCL, and filamins could couple the plasma membrane to actin bundles, while CFL2, GSN, WDR1, FSCN1, and CTTN could remodel, sever, bundle, and protrude actin at podosomes or leading edges. DPYSL2 and DPYSL3 could connect this actin program to microtubule organization and polarized cell projections. Glycolytic enzymes could supply or coordinate energy for cytoskeletal remodeling, while vesicle-associated proteins could support membrane turnover and extracellular-vesicle release. In bone marrow, this may represent a shared program of platelet or megakaryocyte structure, myeloid-cell motility, and stromal or vascular adhesion; in bone, it may reflect related contractile, matrix-interacting, or remodeling cells. This remains a hypothesis because co-abundance does not establish cell identity, direction of regulation, or direct molecular causality.

### Important genes

#### PALLD

- **Related proteins** (co-abundance neighbors): MVP (0.95), GSN (0.94), VCL (0.93), DPYSL3 (0.93), FLNA (0.92), MAP1B (0.91), DPYSL2 (0.91), GARS1 (0.91), TUBB4B (0.90), FSCN1 (0.89), TUBB6 (0.87), TLN1 (0.87), RNH1 (0.86), PKM (0.86), HSP90AA1 (0.86), PLIN3 (0.86), ANXA6 (0.85), FLNC (0.84), PGK1 (0.82), UGDH (0.82), PHGDH (0.81), FAM114A1 (0.81), FLNB (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: palladin, cytoskeletal associated protein. This gene encodes a cytoskeletal protein that is required for organizing the actin cytoskeleton. The protein is a component of actin-containing microfilaments, and it is involved in the control of cell shape, adhesion, and contraction. Polymorphisms in this gene are associated with a susceptibility to pancreatic cancer type 1, and also with a risk for myocardial infarction. Alternative splicing re…
- **Diseases (Open Targets)**: coronary artery disorder (0.444); exocrine pancreatic carcinoma (0.372); coronary atherosclerosis (0.360); Bicuspid aortic valve (0.325); aortic stenosis (0.319)
- **Europe PMC papers**: 1170
- **Why important**: PALLD is the strongest network hub in the supplied module and connects actin-associated, microtubule-associated, adhesion, and metabolic neighbors. It is annotated as a cytoskeletal protein required for actin organization, cell shape, adhesion, contraction, and migration, and it appears across a broad set of primary enrichment terms including actin binding, podosome, cytoskeleton organization, focal adhesion, cell motility, and cell migration (8 globally significant GO/KEGG terms, q_global 4.44e-07–0.00553; see the table). It has no recorded STRING partner or hu.MAP complex in the fact sheet, despite its central co-abundance position, and it has substantial literature and disease associations involving vascular and pancreatic disease.
- **Conclusion**: Established evidence supports PALLD as a central cytoskeletal organizer and a major network connector. Its lack of recorded STRING or hu.MAP support makes it an especially interesting candidate for a tissue-pair-specific co-abundance role, but it does not establish a novel physical interaction. Hypothesis: PALLD may coordinate the actin and adhesion machinery that gives this module its shared structural phenotype.

#### FLNA

- **Related proteins** (co-abundance neighbors): PALLD (0.92), FLNC (0.87), PDLIM4 (0.83), CNOT12 (0.81), MVP (0.81); STRING partners: CFL2 (0.888), FERMT2 (0.852), FLNB (0.979), FLNC (0.907), FSCN1 (0.887), GSN (0.831), TLN1 (0.998), VCL (0.998), WDR1 (0.874)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is a highly connected structural scaffold in the STRING-supported actin network and links actin filaments to membrane glycoproteins, integrins, receptor complexes, and second messengers. It participates in cell-shape remodeling and migration and is present in a wide range of primary terms, including actin binding, podosome, cytoskeleton organization, anchoring junction, focal adhesion, cell-substrate junction, and cell migration (8 globally significant GO/KEGG terms, q_global 4.44e-07–0.00553; see the table). Its known relationships with FLNB, FLNC, TLN1, VCL, GSN, FSCN1, and WDR1 provide strong molecular support for the module’s adhesion and force-transmission interpretation. Its disease associations include skeletal-developmental syndromes and periventricular nodular heterotopia.
- **Conclusion**: Established evidence identifies FLNA as a plausible structural bridge between membrane adhesion systems and the actin cytoskeleton. Its network role is strongly supported by known interactions, so FLNA is more likely a conserved core component than a novel module-specific factor. Hypothesis: FLNA may transmit adhesion-generated mechanical signals into the broader actin-remodeling program in the shared bone and bone-marrow cellular environment.

#### TLN1

- **Related proteins** (co-abundance neighbors): PALLD (0.87), FERMT2 (0.87), DPYSL3 (0.81); STRING partners: CTTN (0.937), FERMT2 (0.705), FLNA (0.998), FLNB (0.995), FLNC (0.996), GSN (0.941), VCL (0.999), WDR1 (0.744)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 is a focal-adhesion protein that supports integrin activation, cell adhesion, cell-substrate contacts, cell-cell junction assembly, and actin organization. It occupies a central position in the known STRING adhesion network, with strong relationships to VCL, FLNA, FLNB, FLNC, GSN, CTTN, and FERMT2. It contributes to many primary terms covering actin binding, anchoring junctions, focal adhesions, cell-substrate junctions, cell motility, and junction assembly (9 globally significant GO/KEGG terms, q_global 4.44e-07–0.0273; see the table). HPA links TLN1 particularly to blood vessels, megakaryocytes, and platelets, which is relevant to a bone-marrow-containing tissue pair.
- **Conclusion**: Established evidence supports TLN1 as an adhesion-to-actin coupling component and gives a biologically coherent explanation for the platelet, megakaryocyte, vascular, and migratory signals. Its relationships are already well represented in STRING, so its importance here is functional integration rather than novelty. Hypothesis: TLN1 may anchor the shared module to integrin-dependent adhesion and force sensing in marrow-associated cells.

#### FSCN1

- **Related proteins** (co-abundance neighbors): PGK1 (0.90), PALLD (0.89), DPYSL3 (0.87), ANXA6 (0.85), WDR1 (0.82); STRING partners: CFL2 (0.758), CTTN (0.771), FLNA (0.887), FLNB (0.788), FLNC (0.794)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fascin actin-bundling protein 1. This gene encodes a member of the fascin family of actin-binding proteins. Fascin proteins organize F-actin into parallel bundles, and are required for the formation of actin-based cellular protrusions. The encoded protein plays a critical role in cell migration, motility, adhesion and cellular interactions. Expression of this gene is known to be regulated by several microRNAs, and overexpression …
- **Diseases (Open Targets)**: ankylosing spondylitis (0.355); Alzheimer disease (0.179); hypothyroidism (0.164); neoplasm (0.118); breast cancer (0.116)
- **Europe PMC papers**: 4005
- **Why important**: FSCN1 is an actin-bundling protein required for actin-based protrusions, migration, motility, adhesion, and cellular interactions. It is represented across the actin, podosome, lamellipodium, leading-edge, cell-migration, focal-adhesion, and junction-related primary terms (9 globally significant GO/KEGG terms, q_global 4.44e-07–0.0123; see the table). STRING connects it to the cortactin, filamin, cofilin, gelsolin, and vinculin-centered network, and the STRING literature term directly links cortactin and fascin to extracellular-vesicle release and invadopodia (STRING COMPARTMENTS Podosome; within-query FDR = 2.7e-06) (STRING Component Podosome; within-query FDR = 4.12e-06) (STRING PMID (2018) Cortactin and fascin-1 regulate extracellular vesicle release by controlling endosomal trafficking or invadopodia formation and function.; within-query FDR = 8.5e-06). HPA identifies immune-cell enhancement in myeloid dendritic cells and protein detection in bone marrow. FSCN1 also has substantial literature and disease associations involving inflammatory and neoplastic processes.
- **Conclusion**: Established evidence supports FSCN1 as a functional effector of protrusion, podosome formation, and motility, with a plausible connection to vesicle release. Its established interaction network argues against calling it a newly discovered actin factor. Hypothesis: FSCN1 may help convert the shared module’s cytoskeletal organization into migratory or membrane-protrusive behavior in marrow-associated immune, vascular, or stromal cells.

#### DPYSL3

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.95), PKM (0.94), PALLD (0.93), DBNL (0.93), HSP90AA1 (0.92), TUBB6 (0.91), USP5 (0.90), PGK1 (0.87), MAP1B (0.87), FSCN1 (0.87), TUBB4B (0.86), PHGDH (0.86), RNH1 (0.85), TKT (0.84), CTTN (0.84), ANXA6 (0.83), FAM114A1 (0.83), PLIN3 (0.83), WDR1 (0.82), MVP (0.82), UGDH (0.82), TLN1 (0.81); STRING partners: DPYSL2 (0.976), PDLIM4 (0.748)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_00051.1, huMAP3_11599.1, huMAP3_11626.1
- **Function (MyGene.info)**: dihydropyrimidinase like 3. Enables filamin binding activity. Predicted to be involved in several processes, including actin filament organization; regulation of plasma membrane bounded cell projection organization; and response to axon injury. Predicted to act upstream of or within nervous system development. Predicted to be located in several cellular components, including cell body; growth cone; and lamellipodium. Predict…
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); brain compression (0.326); edema (0.326); liver disorder (0.214); alcohol drinking (0.200)
- **Europe PMC papers**: 1082
- **Why important**: DPYSL3 is a high-position network connector that links DPYSL2, PALLD, DBNL, HSP90AA1, tubulin, metabolic, and ubiquitin-related neighbors. It is present in primary terms for actin organization, cytoskeletal organization, lamellipodia, growth cones, cell projections, cell motility, and cell migration (8 globally significant GO/KEGG terms, q_global 2e-06–0.00553; see the table). STRING supports its relationship with DPYSL2 and PDLIM4, while hu.MAP repeatedly places DPYSL3 with DPYSL2 in complexes associated with microtubules, neuronal projections, and related cytoskeletal machinery (hu.MAP huMAP3_00051.1) (hu.MAP huMAP3_11599.1) (hu.MAP huMAP3_11626.1). Its annotation and disease associations emphasize cytoskeletal projection biology, nervous-system development, and neurodegenerative disease, while HPA shows low tissue specificity and no immune-cell detection.
- **Conclusion**: Established evidence supports DPYSL3 as a bridge between actin remodeling, microtubule organization, and polarized cellular projections. Its presence does not imply neuronal contamination, because the module also contains broad cytoskeletal and cell-migration evidence and HPA reports low tissue specificity. Hypothesis: DPYSL3 may coordinate actin–microtubule polarity and directional movement in the shared cellular population, linking the module’s adhesion machinery to intracellular transport and projection dynamics.

## Module 5

**Tissue pair**: bone and bone_marrow  
**Genes (19)**: C2orf49, BCAT1, CAPZB, CLIC4, DDAH2, DDX10, DIDO1, FOXK1, MIDEAS, MICALL1, PALS2, PLXNB2, POGZ, PRRC1, RSU1, SLC12A2, SKIC8, SRPK1, TPD52L2

### Function

This is a heterogeneous intracellular co-abundance module rather than a clearly defined canonical bone or bone-marrow pathway. No GO/KEGG term passed global correction, and there were no supplementary STRING functional-enrichment terms, so no pathway-level enrichment should be claimed. The network is organized around MICALL1, whose annotated functions include phosphatidic-acid binding, small-GTPase binding, plasma-membrane tubulation, endocytosis, endosomal localization, and actin-cytoskeleton organization. Other module annotations point to related cellular themes, including actin regulation through CAPZB, membrane and ion transport through SLC12A2, cell adhesion and signaling through RSU1 and PLXNB2, nitric-oxide regulation through DDAH2, and transcriptional or chromatin regulation through FOXK1, MIDEAS, POGZ, DDX10, SRPK1, and SKIC8. Because these themes are distributed across disconnected branches and lack global enrichment, the most defensible interpretation is a coordinated cellular-state signal involving membrane trafficking, cytoskeletal organization, intracellular signaling, and gene-expression control.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, while several are cell-type enhanced across diverse epithelial, reproductive, stromal, vascular, and hematopoietic populations. Blood-cell evidence is mixed rather than uniformly immune-cell enriched: most genes have low immune-cell specificity, with a subset enhanced in monocytes, dendritic-cell populations, B-cell populations, basophils, or plasma cells. This pattern argues against interpreting the module as a dedicated bone program. It may instead reflect shared cellular composition or a broadly expressed intracellular state in bone and bone marrow samples, with possible contribution from hematopoietic or vascular cells. Bone-marrow protein detection supports expression of much of the module there, whereas the fact sheet provides no matching HPA bone tissue result, so tissue-level protein confirmation in bone remains limited.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interactions met the supplied high-confidence threshold, and STRING reported no functional-enrichment terms. Thus the co-abundance edges should not be presented as established physical interactions. hu.MAP provides limited complex-level support: FOXK1 and MIDEAS co-occur in the two related hu.MAP complexes (hu.MAP huMAP3_08800.1) and (hu.MAP huMAP3_09031.1), while CAPZB and MICALL1 co-occur in (hu.MAP huMAP3_12900.1). These observations provide some support for transcriptional-corepressor and actin-associated interpretations, but each complex contains many additional proteins and only a small subset is represented in the module. The remaining co-abundance relationships are not corroborated by the supplied STRING or hu.MAP evidence and may reflect shared regulation, cell composition, or indirect cellular-state effects.

**STRING interactions (score >= 0.7)**: 0 of 171 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08800.1 (FOXK1, MIDEAS; 2/48); huMAP3_09031.1 (FOXK1, MIDEAS; 2/49); huMAP3_12900.1 (CAPZB, MICALL1; 2/50)

### Novelty

The tissue-pair co-abundance pattern may be a potentially new observation, because the module has a distinctive hub-centered structure but little support from the supplied interaction resources. However, it cannot be called a newly discovered mechanism on these data alone. The lack of STRING interactions or broad hu.MAP coverage does not prove novelty, especially for co-expression relationships that need not be physical interactions. The absence of globally significant GO/KEGG enrichment, the heterogeneous annotations, and the mixed HPA cell-type profile all make a strong novelty claim premature. A credible novelty claim would require replication across independent bone and bone-marrow cohorts, control for cellular composition, and experimental or orthogonal validation of the proposed relationships.

**Hypothesis.** Hypothesis: this module represents a shared cellular-state program in bone and bone marrow in which MICALL1-centered membrane trafficking and actin remodeling are co-regulated with nitric-oxide-related mitochondrial control, adhesion or receptor signaling, and transcriptional or chromatin regulation. The MICALL1-centered branch could coordinate endosomal recycling and cytoskeletal remodeling, while the DDAH2 and CLIC4 branch could reflect cellular redox, membrane, differentiation, or migration state. The FOXK1-MIDEAS relationship may represent a chromatin or transcriptional component, and PLXNB2 may mark a cell-migration or immune-associated contribution. This is a mechanistic proposal, not an established pathway inferred from enrichment, because the module lacks globally significant GO/KEGG terms and high-confidence STRING support.

### Important genes

#### MICALL1

- **Related proteins** (co-abundance neighbors): FOXK1 (0.93), PLXNB2 (0.92), POGZ (0.92), DIDO1 (0.90), C2orf49 (0.87), DDX10 (0.87), BCAT1 (0.85), RSU1 (0.85), PRRC1 (0.84), SRPK1 (0.83), SLC12A2 (0.83), PALS2 (0.82), SKIC8 (0.80), MIDEAS (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cell Junctions, Centriolar satellite, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_12900.1
- **Function (MyGene.info)**: MICAL like 1. Enables identical protein binding activity; phosphatidic acid binding activity; and small GTPase binding activity. Involved in several processes, including plasma membrane tubulation; protein localization to endosome; and slow endocytic recycling. Located in late endosome and recycling endosome membrane. Is extrinsic component of membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: obesity disorder (0.099); Alzheimer disease (0.038); COVID-19 (0.032); severe acute respiratory syndrome (0.032); Epiretinal membrane (0.027)
- **Europe PMC papers**: 165
- **Why important**: MICALL1 is the central network hub in the supplied module and connects to genes spanning membrane trafficking, transcription, metabolism, RNA processing, and cytoskeletal biology. Its annotations directly support phosphatidic-acid binding, small-GTPase binding, endocytosis, endosomal targeting, plasma-membrane tubulation, and actin organization. It is therefore the strongest candidate for organizing the module's cellular-state signal. Its literature base is moderate compared with heavily studied signaling genes, and the absence of STRING partners means the hub status here is specifically a co-abundance observation rather than proof of physical binding.
- **Conclusion**: Established: MICALL1 is a module hub with annotations linking it to membrane trafficking and cytoskeletal remodeling, and it participates in the hu.MAP-supported CAPZB relationship (hu.MAP huMAP3_12900.1). Hypothesis: altered MICALL1-associated trafficking or membrane remodeling helps generate the shared bone and bone-marrow co-abundance pattern.

#### DDAH2

- **Related proteins** (co-abundance neighbors): CLIC4 (0.89), TPD52L2 (0.83), RSU1 (0.81), CAPZB (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DDAH family member 2, ADMA-independent. This gene encodes a dimethylarginine dimethylaminohydrolase. The encoded enzyme functions in nitric oxide generation by regulating the cellular concentrations of methylarginines, which in turn inhibit nitric oxide synthase activity. The protein may be localized to the mitochondria. Alternative splicing resulting in multiple transcript variants. [provided by RefSeq, Dec 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.412); neoplasm (0.099); coronary artery disorder (0.084); Myocardial fibrosis (0.075); lung adenocarcinoma (0.071)
- **Europe PMC papers**: 879
- **Why important**: DDAH2 forms a branch with CLIC4, TPD52L2, RSU1, and CAPZB and is annotated as a dimethylarginine dimethylaminohydrolase that regulates methylarginines and nitric-oxide synthase activity. Its reported biological processes include positive regulation of nitric-oxide biosynthesis and negative regulation of apoptosis. Its relatively substantial literature base and disease associations involving neurodegenerative, neoplastic, cardiovascular, and fibrotic contexts make it a plausible state-regulatory component rather than a generic uncharacterized member.
- **Conclusion**: Established: DDAH2 provides a biochemical nitric-oxide and cell-survival interpretation for one module branch and is co-abundant with membrane, adhesion, and actin-related genes. Hypothesis: DDAH2-dependent nitric-oxide regulation may couple metabolic or survival state to the membrane and cytoskeletal program in the shared tissues.

#### CLIC4

- **Related proteins** (co-abundance neighbors): DDAH2 (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Centrosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CLIC family member 4. Chloride channels are a diverse group of proteins that regulate fundamental cellular processes including stabilization of cell membrane potential, transepithelial transport, maintenance of intracellular pH, and regulation of cell volume. Chloride intracellular channel 4 (CLIC4) protein, encoded by the CLIC4 gene, is a member of the p64 family; the gene is expressed in many tissues and exhibits a i…
- **Diseases (Open Targets)**: hypertensive disorder (0.352); Short stature (0.259); cardiovascular disorder (0.237); response to xenobiotic stimulus (0.233); exostosis (0.212)
- **Europe PMC papers**: 4070
- **Why important**: CLIC4 is linked to DDAH2 in the module and has the strongest literature support among the selected genes. Its annotations include intracellular chloride-related biology, cell differentiation, regulation of migration, apical-basal polarity, and cytoskeletal organization. HPA identifies tissue enhancement in blood vessel and immune-cell enhancement in memory and naive B-cell populations, which makes CLIC4 relevant to vascular or hematopoietic composition as well as intracellular cell-state biology.
- **Conclusion**: Established: CLIC4 is a broadly studied intracellular protein associated with differentiation, polarity, migration, and cytoskeletal regulation, and it occupies the DDAH2 branch. Hypothesis: CLIC4 may help connect vascular or immune-cell representation with the DDAH2-associated signaling state, but the module data do not establish a direct CLIC4-DDAH2 interaction.

#### FOXK1

- **Related proteins** (co-abundance neighbors): MICALL1 (0.93); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_08800.1, huMAP3_09031.1
- **Function (MyGene.info)**: forkhead box K1. Enables 14-3-3 protein binding activity; DNA-binding transcription repressor activity, RNA polymerase II-specific; and transcription cis-regulatory region binding activity. Involved in several processes, including cellular glucose homeostasis; negative regulation of autophagy; and regulation of transcription, DNA-templated. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resource…
- **Diseases (Open Targets)**: neurodegenerative disease (0.520); Abnormality of the skeletal system (0.456); hypothyroidism (0.393); Parkinson disease (0.374); autoimmune disorder of central nervous system (0.370)
- **Europe PMC papers**: 1745
- **Why important**: FOXK1 is a transcriptional regulator with annotations for transcriptional repression, glucose homeostasis, and negative regulation of autophagy. It is one of the two module members in both related hu.MAP complexes (hu.MAP huMAP3_08800.1) and (hu.MAP huMAP3_09031.1), together with MIDEAS, providing the clearest complex-level support for a nuclear regulatory branch. Its disease-association profile includes skeletal-system abnormality and several neurological or autoimmune categories, making it relevant to tissue-state regulation despite its low tissue specificity.
- **Conclusion**: Established: FOXK1 is a transcriptional regulator and forms the module's principal hu.MAP-supported relationship with MIDEAS (hu.MAP huMAP3_08800.1)(hu.MAP huMAP3_09031.1). Hypothesis: FOXK1-mediated control of transcription, glucose handling, or autophagy may coordinate the nuclear branch with the membrane and metabolic signals represented elsewhere in the module.

#### PLXNB2

- **Related proteins** (co-abundance neighbors): MICALL1 (0.92); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plexin B2. Members of the B class of plexins, such as PLXNB2 are transmembrane receptors that participate in axon guidance and cell migration in response to semaphorins (Perrot et al. (2002) [PubMed 12183458]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Intellectual disability (0.519); amelogenesis imperfecta (0.518); sensorineural hearing loss disorder (0.516); cutaneous melanoma (0.486); neurodegenerative disease (0.455)
- **Europe PMC papers**: 2109
- **Why important**: PLXNB2 is a membrane receptor associated with semaphorin-responsive axon guidance and cell migration, and its annotations also include receptor-mediated endocytosis, cell adhesion, and regulation of phosphorylation. HPA places it in several monocyte and dendritic-cell populations, including a group-enriched blood-cell pattern, making it especially informative for assessing whether the shared module partly reflects hematopoietic composition. Its disease associations span neurodevelopmental, hearing, enamel, and melanoma-related categories, consistent with a receptor involved in cell positioning and tissue organization.
- **Conclusion**: Established: PLXNB2 contributes a receptor, adhesion, migration, and immune-cell-associated interpretation and is co-abundant with the central MICALL1 branch. Hypothesis: PLXNB2 may indicate a myeloid or other migratory-cell contribution to the module, or may participate in a shared membrane-trafficking state, but the present evidence cannot distinguish these possibilities.

## Module 6

**Tissue pair**: bone and bone_marrow  
**Genes (29)**: ATXN2, BORCS5, PPP3R1, CCDC167, COMMD8, COMMD9, CPPED1, DDX46, HSD17B11, FBXO22, GIPC1, GNPDA1, GON7, CAMK2G, LMCD1, GSTZ1, MEAK7, MTHFS, NUP188, NUP37, PIH1D1, TP53RK, PYM1, UPF1, RPL26L1, RPE, TBPL1, TTLL12, UBE2E2

### Function

This is a heterogeneous intracellular co-abundance module rather than a clearly defined pathway module. No GO or KEGG term passed global correction, so there is no globally significant pathway annotation to assign. The network nevertheless contains several interpretable functional threads: RNA surveillance and translation through UPF1, ATXN2 and PYM1; nuclear pore and nucleocytoplasmic transport through NUP188 and NUP37; the KEOPS-associated translational-fidelity machinery through GON7 and TP53RK; endocytic recycling and signalling through COMMD8 and COMMD9; and membrane, vesicle and organelle-trafficking functions through GIPC1, BORCS5 and related genes. The co-abundance structure therefore appears to combine general RNA-processing, nuclear-transport, proteostasis and intracellular-trafficking programs. These annotations support biological interpretability, but they do not establish a single enriched function. The absence of a globally enriched term does not invalidate the module.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, while many show cell-type-enhanced expression in diverse populations, including epithelial, germ-cell, trophoblast, neural, hepatic and myeloid populations. Several genes have neutrophil or other immune-cell associations, but the overall immune-cell specificity is predominantly low and UPF1 is not detected in immune cells. The broad distribution and the detection of most proteins in bone marrow are more consistent with a mixture of broadly expressed intracellular proteins and shared bone-marrow cell populations than with a bone-specific extracellular program. The HPA patterns also raise the possibility that sample cellular composition contributes to the conserved co-abundance signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING identifies a small set of high-confidence relationships rather than a densely connected interaction network. The established pairs include ATXN2 with UPF1, PYM1 with UPF1, COMMD8 with COMMD9, GON7 with TP53RK, and NUP188 with NUP37. These relationships independently support RNA surveillance, COMM-domain complex biology, the KEOPS-associated machinery, and nuclear-pore biology. STRING reports no supplementary functional enrichment. hu.MAP provides stronger complex-level context: GON7 and TP53RK recur together in KEOPS-related complexes (hu.MAP huMAP3_00664.1) and (hu.MAP huMAP3_11762.1); NUP188 and NUP37 recur together in nuclear-pore complexes (hu.MAP huMAP3_07492.1), (hu.MAP huMAP3_08489.1), (hu.MAP huMAP3_09710.1) and (hu.MAP huMAP3_09825.1); COMMD8 and COMMD9 recur together in COMM-domain and endocytic-recycling complexes (hu.MAP huMAP3_01290.1), (hu.MAP huMAP3_07032.1) and (hu.MAP huMAP3_14444.1); and UPF1 with ATXN2 occurs in an RNA-processing complex (hu.MAP huMAP3_06975.1). Thus, several module edges or local pairings reflect known molecular machinery, while the broader co-abundance connections between these machinery groups are not directly established by STRING or hu.MAP.

**STRING interactions (score >= 0.7)**: 5 of 406 gene pairs: ATXN2–UPF1 (0.748); COMMD8–COMMD9 (0.955); GON7–TP53RK (0.999); NUP188–NUP37 (0.983); PYM1–UPF1 (0.953)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00664.1 (TP53RK, GON7; 2/7); huMAP3_11762.1 (TP53RK, GON7; 2/10); huMAP3_07492.1 (NUP188, NUP37; 2/10); huMAP3_08489.1 (NUP188, NUP37; 2/10); huMAP3_01290.1 (COMMD8, COMMD9; 2/12); huMAP3_09710.1 (NUP188, NUP37; 2/13); huMAP3_07032.1 (COMMD8, COMMD9; 2/20); huMAP3_14444.1 (COMMD8, COMMD9; 2/21); huMAP3_09825.1 (NUP188, NUP37; 2/27); huMAP3_06975.1 (UPF1, ATXN2; 2/31)

### Novelty

This module should not be claimed as a newly discovered molecular complex or pathway. Its strongest interpretable pairings are already represented in STRING or hu.MAP, including KEOPS-associated, nuclear-pore, COMM-domain and RNA-processing relationships. The potentially novel aspect is the coordinated co-abundance of these otherwise distinct intracellular systems in the conserved bone and bone-marrow context. However, the supplied evidence does not establish whether this cross-system organization is absent from previous co-expression studies, and absence of an edge from STRING or hu.MAP would not by itself prove novelty. The appropriate conclusion is a potentially interesting tissue-pair co-abundance pattern requiring replication and comparison with independent bone and bone-marrow datasets.

**Hypothesis.** Hypothesis: the module reflects a shared state of biosynthetically active bone-marrow-associated cells in which RNA quality control, translation fidelity, nuclear transport, intracellular trafficking and stress-responsive signalling are coordinately regulated. GIPC1 may provide a high-connectivity scaffold linking trafficking or membrane-associated biology to nuclear and RNA-related genes, while the established GON7–TP53RK, NUP188–NUP37, COMMD8–COMMD9 and UPF1-associated relationships represent embedded molecular subsystems. The signal may therefore arise from coordinated cellular activity or shared cell composition rather than one canonical bone-specific pathway. This is a mechanistic hypothesis, not a demonstrated causal model.

### Important genes

#### GIPC1

- **Related proteins** (co-abundance neighbors): UBE2E2 (0.99), NUP37 (0.95), RPL26L1 (0.91), ATXN2 (0.85), DDX46 (0.84), PPP3R1 (0.83), CCDC167 (0.82), PYM1 (0.81), RPE (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GIPC PDZ domain containing family member 1. GIPC1 is a scaffolding protein that regulates cell surface receptor expression and trafficking (Lee et al., 2008 [PubMed 18775991]).[supplied by OMIM, Apr 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); oculopharyngodistal myopathy 2 (0.409); oculopharyngodistal myopathy (0.376); smoking initiation (0.205); risk-taking behaviour (0.192)
- **Europe PMC papers**: 653
- **Why important**: GIPC1 is the most connected and strongest local hub in the module. It links genes involved in trafficking, nuclear-pore biology, RNA handling, translation and signalling, and its established function as a scaffold regulating cell-surface receptor expression and trafficking makes it a plausible integrative connector. HPA places it at the plasma membrane and cell junctions, with bone-marrow protein detection, while its literature and disease associations provide more support than would be expected for an uncharacterized connector.
- **Conclusion**: Established: GIPC1 is a trafficking and receptor-expression scaffold and is the principal network connector in this module. Hypothesis: it may help couple membrane or junctional state to the intracellular RNA-processing and transport programs. The co-abundance data alone do not demonstrate that GIPC1 causally organizes the other genes.

#### GON7

- **Related proteins** (co-abundance neighbors): LMCD1 (0.97), GNPDA1 (0.91), COMMD8 (0.90), RPL26L1 (0.88), HSD17B11 (0.88), CPPED1 (0.83), FBXO22 (0.81); STRING partners: TP53RK (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Nucleoli rim; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_00664.1, huMAP3_11762.1
- **Function (MyGene.info)**: GON7 subunit of KEOPS complex. Located in cytosol; nucleolus; and nucleoplasm. Part of EKC/KEOPS complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Galloway-Mowat syndrome 9 (0.572); Galloway-Mowat syndrome (0.504); eye injury (0.053); systemic inflammatory response syndrome (0.037); corneal degeneration (0.031)
- **Europe PMC papers**: 134
- **Why important**: GON7 is a central module member with links to several genes and a direct high-confidence STRING relationship with TP53RK. Both genes recur together in multiple hu.MAP complexes (hu.MAP huMAP3_00664.1) and (hu.MAP huMAP3_11762.1). GON7 is an established KEOPS subunit involved in tRNA modification and translational fidelity, and it has a disease association with Galloway-Mowat syndrome. Its position connects the KEOPS signal to genes with metabolic, transcriptional and signalling annotations.
- **Conclusion**: Established: GON7 participates in KEOPS-associated biology and translational fidelity, supported by its annotation, STRING relationship and hu.MAP membership. Hypothesis: the module may mark demand for accurate translation in the shared cellular state. A bone-specific role is not established.

#### TP53RK

- **Related proteins** (co-abundance neighbors): TBPL1 (0.85); STRING partners: GON7 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_00664.1, huMAP3_11762.1
- **Function (MyGene.info)**: TP53 regulating kinase. Enables p53 binding activity and protein serine/threonine kinase activity. Involved in protein phosphorylation. Located in cytoplasm and nucleus. Part of EKC/KEOPS complex. Implicated in Galloway-Mowat syndrome 4. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Galloway-Mowat syndrome (0.762); neurodegenerative disease (0.429); Global developmental delay (0.324); Seizure (0.323); microcephaly (0.112)
- **Europe PMC papers**: 361
- **Why important**: TP53RK is the kinase partner of GON7 in the strongest STRING-supported pair and is present with GON7 in the same hu.MAP complex groups (hu.MAP huMAP3_00664.1) and (hu.MAP huMAP3_11762.1). It contributes protein phosphorylation, p53-related signalling and translational-fidelity biology, and it has a documented association with Galloway-Mowat syndrome. This gives the module a concrete regulatory component rather than only structural or housekeeping annotations.
- **Conclusion**: Established: TP53RK is a KEOPS-associated kinase linked to translational fidelity and p53-class signalling. Hypothesis: TP53RK may couple cellular stress or damage signalling to the RNA and translation-related components of the module. The data do not show kinase activity within bone or bone marrow specifically.

#### NUP188

- **Related proteins** (co-abundance neighbors): TBPL1 (0.91); STRING partners: NUP37 (0.983)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_07492.1, huMAP3_08489.1, huMAP3_09710.1, huMAP3_09825.1
- **Function (MyGene.info)**: nucleoporin 188. The nuclear pore complex (NPC) is found on the nuclear envelope and forms a gateway that regulates the flow of proteins and RNAs between the cytoplasm and nucleoplasm. The NPC is comprised of approximately 30 distinct proteins collectively known as nucleoporins. Nucleoporins are pore-complex-specific glycoproteins which often have cytoplasmically oriented O-linked N-acetylglucosamine residues and …
- **Diseases (Open Targets)**: sandestig-stefanova syndrome (0.799); HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.527); microcephaly (0.453)
- **Europe PMC papers**: 629
- **Why important**: NUP188 is part of a known nuclear-pore relationship with NUP37 in STRING and appears with NUP37 across several hu.MAP nuclear-pore complexes (hu.MAP huMAP3_07492.1), (hu.MAP huMAP3_08489.1), (hu.MAP huMAP3_09710.1) and (hu.MAP huMAP3_09825.1). Its annotated roles in RNA export, protein import and nucleocytoplasmic transport provide a direct explanation for the module's nuclear-transport component. It also has a substantial literature base and disease associations involving developmental and infectious phenotypes.
- **Conclusion**: Established: NUP188 is a nuclear-pore component involved in nucleocytoplasmic transport and is supported by both STRING and hu.MAP. Hypothesis: altered nuclear transport demand may be one reason this gene tracks with RNA surveillance and translation-related genes. The module does not establish altered pore function.

#### UPF1

- **Related proteins** (co-abundance neighbors): CAMK2G (0.86); STRING partners: ATXN2 (0.748), PYM1 (0.953)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_06975.1
- **Function (MyGene.info)**: UPF1 RNA helicase and ATPase. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons.…
- **Diseases (Open Targets)**: Intellectual disability (0.437); Global developmental delay (0.426); High anterior hairline (0.425); Frontal bossing (0.425); Hypertelorism (0.425)
- **Europe PMC papers**: 4252
- **Why important**: UPF1 is a well-studied RNA helicase and ATPase central to nonsense-mediated decay, mRNA export and translational termination. It is supported by STRING relationships with ATXN2 and PYM1 and by the hu.MAP RNA-processing complex (hu.MAP huMAP3_06975.1). Its extensive literature and developmental disease associations make it an important biological anchor for interpreting the RNA-quality-control aspect of the module, even though its direct module degree is limited.
- **Conclusion**: Established: UPF1 is a core mRNA-surveillance factor with known RNA-processing partners represented in this module. Hypothesis: the conserved co-abundance signal may reflect coordinated control of transcript quality and translation in bone-marrow-associated cells. It is not established that nonsense-mediated decay is specifically altered.

#### COMMD8

- **Related proteins** (co-abundance neighbors): GON7 (0.90); STRING partners: COMMD9 (0.955)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_01290.1, huMAP3_07032.1, huMAP3_14444.1
- **Function (MyGene.info)**: COMM domain containing 8. The protein encoded by this gene binds coiled-coil domain-containing protein 22 (CCDC22), and this complex can regulate the turnover of I-kappa-B and the activation of NF-kappa-B. [provided by RefSeq, Jul 2016].
- **Diseases (Open Targets)**: neurodegenerative disease (0.455); Hydrocephalus (0.319); non-autoimmune hemolytic anemia (0.254); alcohol drinking (0.116); stroke disorder (0.116)
- **Europe PMC papers**: 188
- **Why important**: COMMD8 is linked to GON7 in the module and has a high-confidence STRING relationship with COMMD9. COMMD8 and COMMD9 co-occur in several hu.MAP complexes (hu.MAP huMAP3_01290.1), (hu.MAP huMAP3_07032.1) and (hu.MAP huMAP3_14444.1), providing repeated complex-level support. COMMD8 is associated with regulation of I-kappa-B turnover, NF-kappa-B activation and endocytic recycling, which connects the module to signalling and intracellular trafficking. Its bone-marrow detection and broad cell-type associations are also relevant to a shared bone and bone-marrow module.
- **Conclusion**: Established: COMMD8 participates in COMM-domain-associated trafficking and NF-kappa-B-related regulation and is supported with COMMD9 by STRING and hu.MAP. Hypothesis: this pair may connect inflammatory or receptor-trafficking state to the RNA, nuclear-pore and translation systems. The module does not prove inflammatory activation.

## Module 7

**Tissue pair**: bone and bone_marrow  
**Genes (29)**: GUSB, CAPN2, COL12A1, DHX57, DIS3L2, ECE1, EDC4, ERCC6L, FIP1L1, H2AC21, HMMR, KIF20A, TMPO, MAD1L1, NHLRC2, OARD1, PCNA, PHF3, PLCB3, PLGRKT, RBM7, POLR1A, SNRNP27, STRN, TMEM70, TOM1, THBS1, USP16, UTP25

### Function

The module does not have a globally significant GO or KEGG enrichment; no GO/KEGG term passed global correction. Its gene-level annotations instead suggest a heterogeneous bone-marrow-associated program with a prominent cell-division and genome-maintenance axis. ERCC6L, MAD1L1, KIF20A and HMMR point toward chromosome segregation, spindle or cytokinesis-related processes, while PCNA, USP16, H2AC21 and OARD1 support DNA replication, chromatin or DNA-damage-associated activity. RBM7, UTP25, SNRNP27, FIP1L1, DIS3L2 and EDC4 add RNA processing, ribosome biogenesis or RNA-decay functions. THBS1, COL12A1, GUSB, ECE1 and PLCB3 indicate additional extracellular-matrix, lysosomal, proteolytic or receptor-signaling components. Thus, the safest interpretation is a mixed proliferative and biosynthetic program rather than a single established pathway. Lack of global enrichment does not invalidate the module, but it limits pathway-level certainty.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. Only a small secreted component is reported, represented most clearly by THBS1 and COL12A1, whereas many genes are intracellular nuclear, cytosolic, mitochondrial or vesicular proteins. HPA indicates that most genes have low tissue specificity, with a substantial subset enhanced in bone marrow or lymphoid tissue. Cell-type enhancement is frequent for erythrocyte progenitors, monocyte progenitors, megakaryocyte-related cells, neutrophils and other proliferative or developing cell types, but also occurs in spermatogenic and nonhematopoietic cells. Most genes have low immune-cell specificity, so this is not a clearly immune-lineage-specific module. The shared bone and bone-marrow signal may therefore reflect proliferating marrow-derived or stromal-associated cell populations, or a broadly expressed cellular state, rather than a bone-specific program. Protein detection is reported for most genes in bone marrow, while matching bone tissue protein data are unavailable.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, HMMR–KIF20A, supporting a real connection between two genes associated with microtubule-related cell division. No STRING functional-enrichment result is available. hu.MAP provides repeated support for the KIF20A–MAD1L1 pair across several complexes (hu.MAP huMAP3_00721.1), (hu.MAP huMAP3_00728.1), (hu.MAP huMAP3_01908.1), (hu.MAP huMAP3_07733.1) and (hu.MAP huMAP3_12766.1), although these complexes contain additional members not present in the module. GUSB–ECE1 co-occur in broader hu.MAP complexes (hu.MAP huMAP3_08802.1), (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), but these complexes contain many external proteins and therefore provide weaker evidence for a compact module mechanism. Overall, the external resources validate selected pairwise or complex-level relationships, especially the mitotic KIF20A–MAD1L1 and HMMR–KIF20A connections, but do not support the entire co-abundance structure as one previously defined protein complex.

**STRING interactions (score >= 0.7)**: 1 of 406 gene pairs: HMMR–KIF20A (0.909)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00721.1 (KIF20A, MAD1L1; 2/2); huMAP3_00728.1 (KIF20A, MAD1L1; 2/3); huMAP3_01908.1 (KIF20A, MAD1L1; 2/6); huMAP3_07733.1 (KIF20A, MAD1L1; 2/9); huMAP3_12766.1 (KIF20A, MAD1L1; 2/11); huMAP3_08802.1 (GUSB, ECE1; 2/33); huMAP3_06775.1 (GUSB, ECE1; 2/60); huMAP3_09327.1 (GUSB, ECE1; 2/93)

### Novelty

The module should be regarded as a potentially novel co-abundance pattern, not as a newly established biological pathway. Its exact cross-tissue association is not directly represented by the available STRING or hu.MAP evidence, and the sparse STRING connectivity plus absence of global GO/KEGG enrichment argue against calling it a known canonical module. However, these absences do not prove biological novelty: the pattern could reflect coordinated expression across proliferating marrow cells, shared cell composition, or a mixture of partially related processes. The most defensible novelty claim is therefore that this particular bone and bone-marrow co-abundance configuration is a candidate observation requiring replication and cell-composition-aware validation.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of genes expressed by proliferating or developing bone-marrow-associated cells, combining mitotic machinery with RNA and chromatin maintenance, intracellular trafficking, lysosomal processing and extracellular-matrix interaction. In this model, ERCC6L, MAD1L1, KIF20A and HMMR represent a cell-cycle or cytoskeletal backbone, while THBS1 and COL12A1 may reflect stromal or matrix context and GUSB or ECE1 may reflect vesicular or proteolytic context. The apparent conservation between bone and bone marrow could arise because both samples contain related marrow-derived, stromal, vascular or progenitor populations. This remains a hypothesis because the module lacks globally significant pathway enrichment and contains only limited experimentally supported internal interactions.

### Important genes

#### ERCC6L

- **Related proteins** (co-abundance neighbors): DHX57 (0.90), DIS3L2 (0.89), RBM7 (0.84), TOM1 (0.83), MAD1L1 (0.83), HMMR (0.82), USP16 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Centrosome; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ERCC excision repair 6 like DNA helicase. This gene encodes a member of the SWItch/Sucrose Non-Fermentable (SWI/SNF2) family of proteins, and contains a SNF2-like ATPase domain and a PICH family domain. One distinguishing feature of this SWI/SNF protein family member is that during interphase, the protein is excluded from the nucleus, and only associates with chromatin after the nuclear envelope has broken down. This protein is a DNA tran…
- **Diseases (Open Targets)**: neurodegenerative disease (0.534); frozen shoulder (0.291); neoplasm (0.111); hepatocellular carcinoma (0.106); cancer (0.105)
- **Europe PMC papers**: 494
- **Why important**: ERCC6L has the strongest network position in the supplied graph and connects to genes involved in RNA handling, mitotic control and DNA-associated processes, including MAD1L1 and HMMR. Its annotation describes an SNF2-like DNA translocase associated with stretched DNA and chromosome-related cellular states. HPA links it to bone marrow and lymphoid tissue and to erythrocyte progenitor and other progenitor-like cell types. It has a substantial literature record and disease links including neoplastic and skeletal-relevant associations.
- **Conclusion**: Established evidence supports ERCC6L as a prominent integrator of the module and as a plausible marker of proliferative or chromosome-maintenance activity. It is not established that ERCC6L drives the shared bone–bone-marrow co-abundance pattern; that causal interpretation remains hypothetical.

#### KIF20A

- **Related proteins** (co-abundance neighbors): PHF3 (0.81); STRING partners: HMMR (0.909)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm, Cytokinetic bridge, Cleavage furrow, Mitotic spindle; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_00721.1, huMAP3_00728.1, huMAP3_01908.1, huMAP3_07733.1, huMAP3_12766.1
- **Function (MyGene.info)**: kinesin family member 20A. Enables protein kinase binding activity. Involved in microtubule bundle formation; midbody abscission; and regulation of cytokinesis. Located in several cellular components, including cleavage furrow; intercellular bridge; and midbody. Implicated in restrictive cardiomyopathy. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: cardiomyopathy, familial restrictive, 6 (0.586); familial isolated restrictive cardiomyopathy (0.370); hepatocellular carcinoma (0.123); central nervous system cancer (0.120); neoplasm (0.111)
- **Europe PMC papers**: 2386
- **Why important**: KIF20A is directly supported by the STRING relationship with HMMR and repeatedly co-occurs with MAD1L1 in hu.MAP complexes (hu.MAP huMAP3_00721.1) (hu.MAP huMAP3_00728.1) (hu.MAP huMAP3_01908.1) (hu.MAP huMAP3_07733.1) (hu.MAP huMAP3_12766.1). Its established function includes microtubule bundle formation, cytokinesis and midbody abscission. HPA reports enhancement in bone marrow and lymphoid tissue and in several developing or proliferative cell types. It also has disease associations involving restrictive cardiomyopathy and cancer, with a substantial literature record.
- **Conclusion**: Established evidence makes KIF20A one of the strongest candidates for the module's cell-division component. The data support participation in a mitotic expression program, but do not establish that KIF20A is the organizing driver of the whole module.

#### MAD1L1

- **Related proteins** (co-abundance neighbors): DHX57 (0.83), ERCC6L (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_00721.1, huMAP3_00728.1, huMAP3_01908.1, huMAP3_07733.1, huMAP3_12766.1
- **Function (MyGene.info)**: mitotic arrest deficient 1 like 1. MAD1L1 is a component of the mitotic spindle-assembly checkpoint that prevents the onset of anaphase until all chromosome are properly aligned at the metaphase plate. MAD1L1 functions as a homodimer and interacts with MAD2L1. MAD1L1 may play a role in cell cycle control and tumor suppression. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2015].
- **Diseases (Open Targets)**: mosaic variegated aneuploidy syndrome 7 with inflammation and tumor predisposition (0.533); schizophrenia (0.498); neurodegenerative disease (0.452); bipolar disorder (0.452); major depressive disorder (0.438)
- **Europe PMC papers**: 1331
- **Why important**: MAD1L1 is connected to ERCC6L and DHX57 and is repeatedly paired with KIF20A in hu.MAP complexes (hu.MAP huMAP3_00721.1) (hu.MAP huMAP3_00728.1) (hu.MAP huMAP3_01908.1) (hu.MAP huMAP3_07733.1) (hu.MAP huMAP3_12766.1). Its established function is the spindle-assembly checkpoint, including kinetochore attachment, metaphase alignment and control of the metaphase-to-anaphase transition. HPA detects it in bone marrow and shows enhancement in several cell types capable of active division. Its disease associations include mosaic variegated aneuploidy syndrome and tumor predisposition, and it has a substantial literature record.
- **Conclusion**: Established evidence identifies MAD1L1 as a credible cell-cycle checkpoint component within the module. The module-level interpretation that checkpoint activity is coordinated with the other processes is plausible but remains unproven.

#### HMMR

- **Related proteins** (co-abundance neighbors): ERCC6L (0.82); STRING partners: KIF20A (0.909)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Microtubules; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hyaluronan mediated motility receptor. The protein encoded by this gene is involved in cell motility. It is expressed in breast tissue and together with other proteins, it forms a complex with BRCA1 and BRCA2, thus is potentially associated with higher risk of breast cancer. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene. [provided by RefSeq, Dec 2008].
- **Diseases (Open Targets)**: ovarian cancer (0.342); thyroid gland carcinoma (0.306); alcohol drinking (0.298); Alzheimer disease (0.279); Parkinson disease (0.279)
- **Europe PMC papers**: 2289
- **Why important**: HMMR occupies a direct network connection to ERCC6L and has the strongest internal STRING relationship in the module through HMMR–KIF20A. Its annotation links it to cell motility, receptor-mediated endocytosis and hyaluronan-related processes, while HPA shows enhancement in bone marrow, lymphoid tissue and several progenitor or proliferative cell types. Its literature record is substantial and includes cancer-related associations.
- **Conclusion**: Established evidence supports HMMR as a bridge between the module's mitotic or cytoskeletal signal and motility or extracellular-matrix-related biology. Whether it mediates communication between marrow cells and bone matrix in this module is a hypothesis rather than a demonstrated mechanism.

#### THBS1

- **Related proteins** (co-abundance neighbors): PLGRKT (0.95), TMEM70 (0.83), COL12A1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum, Plasma membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thrombospondin 1. The protein encoded by this gene is a subunit of a disulfide-linked homotrimeric protein. This protein is an adhesive glycoprotein that mediates cell-to-cell and cell-to-matrix interactions. This protein can bind to fibrinogen, fibronectin, laminin, type V collagen and integrins alpha-V/beta-1. This protein has been shown to play roles in platelet aggregation, angiogenesis, and tumorigenesis. [pro…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.385); tooth disorder (0.350); autism spectrum disorder (0.336); neurodegenerative disease (0.323); metabolic syndrome (0.309)
- **Europe PMC papers**: 12762
- **Why important**: THBS1 provides an important non-nuclear component of the module. It connects to COL12A1 and PLGRKT and is annotated as a secreted extracellular-matrix adhesive glycoprotein involved in cell–cell and cell–matrix interactions, platelet aggregation, angiogenesis and inflammatory regulation. HPA places it in fibroblast-, macrophage-, monocyte- and platelet-associated contexts and reports secretion to extracellular matrix. It has a particularly extensive literature record and multiple disease associations.
- **Conclusion**: Established evidence supports THBS1 as a plausible indicator of stromal, matrix or platelet-associated context rather than as evidence for a purely intracellular cell-cycle module. Its co-abundance with proliferative genes may reflect shared cellular composition or coordinated marrow niche biology, but the causal link is not established.

## Module 8

**Tissue pair**: bone and bone_marrow  
**Genes (12)**: CDCA5, EIF1AD, HMGA1, NOP16, NUP35, P3H1, PAFAH1B3, RBM3, MRPL30, SYNE1, SZRD1, TUBB2B

### Function

The module is most consistent with a nuclear, proliferative and biosynthetic program associated with bone-marrow cells, rather than with a narrowly defined pathway. CDCA5 is the central network hub and is annotated with mitotic sister-chromatid segregation, double-strand-break repair and cell-cycle regulation. The connected genes add functions involving chromatin regulation through HMGA1, nuclear-envelope organization through SYNE1, nuclear transport through NUP35, microtubule organization through TUBB2B, RNA processing and translational regulation through RBM3, ribosome biogenesis through NOP16, mitochondrial translation through MRPL30, and collagen processing through P3H1. These annotations support a coordinated state involving cell division, nuclear organization, RNA and protein production, and structural maintenance, but they do not establish a single canonical pathway. No GO or KEGG term passed global correction; therefore no GO or KEGG enrichment is claimed. The lack of a globally significant term does not invalidate the module.

**Cell composition.** The module is not dominated by plasma or secreted proteins. It is mainly composed of intracellular or nuclear proteins, with only a single secretome annotation and no evidence for a plasma-protein signature. HPA indicates predominantly low tissue specificity, while many genes show cell-type-enhanced expression. Bone marrow protein detection is common among the genes, whereas the immune-cell specificity profile is generally low rather than strongly blood-cell restricted. Some cell-type associations involve erythrocyte progenitors, megakaryocytes, neutrophil progenitors, NK cells, T-reg cells and eosinophils, but other associations involve esophageal, reproductive, neural and trophoblast cell types. Thus, the shared bone and bone-marrow signal may partly reflect proliferating or structurally similar cells present in both sample groups, rather than a bone-specific extracellular-matrix program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes, no STRING functional-enrichment result, and no hu.MAP complex containing multiple module members. The co-abundance edges are therefore not supported by already catalogued physical interactions or a recognized multiprotein complex in these resources. This does not show that the relationships are biologically false: co-abundance can reflect shared regulation, cell-state composition, common RNA or protein turnover, or indirect pathway coordination. It does mean that the module should be interpreted as a transcriptomic or proteomic association pattern rather than as an established physical complex.

**STRING interactions (score >= 0.7)**: 0 of 66 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module appears potentially novel as a coordinated co-abundance pattern because its internal relationships are absent from the supplied high-confidence STRING and hu.MAP evidence, and because it lacks a globally significant GO or KEGG annotation. However, it cannot be called a newly discovered biological pathway solely from those absences. Several component genes have established individual functions and disease associations, and the centrality of CDCA5 may cause the pattern to represent a shared proliferative state or sample-cell composition. The strongest novelty claim is therefore that this particular cross-tissue co-abundance configuration may be under-characterized, not that the genes or their functions are unprecedented.

**Hypothesis.** Hypothesis: the shared module marks a bone-marrow-associated proliferative cell state in which CDCA5-linked cell-cycle and DNA-repair activity is coordinated with chromatin regulation, nuclear-envelope and pore organization, cytoskeletal remodeling, RNA handling, ribosome and mitochondrial protein production, and collagen-processing capacity. In bone and bone marrow, this state could arise from shared progenitor, hematopoietic-support, or other proliferating cell populations. The P3H1 connection raises the possibility that this state also couples cellular proliferation with extracellular-matrix maturation, but the current evidence does not establish that coupling mechanistically.

### Important genes

#### CDCA5

- **Related proteins** (co-abundance neighbors): EIF1AD (0.95), RBM3 (0.90), NOP16 (0.88), PAFAH1B3 (0.88), NUP35 (0.87), TUBB2B (0.87), SZRD1 (0.86), HMGA1 (0.84), MRPL30 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell division cycle associated 5. Predicted to enable chromatin binding activity. Involved in double-strand break repair; mitotic sister chromatid segregation; and regulation of cell cycle process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.306); hepatocellular carcinoma (0.121); breast cancer (0.113); neoplasm (0.112); breast carcinoma (0.111)
- **Europe PMC papers**: 1491
- **Why important**: CDCA5 is the clear network hub, connecting most of the module directly and with the strongest aggregate association in the supplied graph. Its established annotations link it to sister-chromatid cohesion, mitotic segregation, cell-cycle regulation and double-strand-break repair. HPA places it in the nucleoplasm and associates it with bone marrow, lymphoid tissue, testis, erythrocyte progenitors and several other cell types. It also has a substantial literature and disease-association record, including neoplastic and neurodegenerative categories.
- **Conclusion**: Established: CDCA5 is the best-supported organizing marker of the module and is compatible with proliferating bone-marrow-associated cells. Hypothesis: variation in CDCA5-linked cell-cycle activity may help generate the co-abundance pattern and may indirectly pull otherwise diverse nuclear and biosynthetic genes into the same module.

#### HMGA1

- **Related proteins** (co-abundance neighbors): SYNE1 (0.93), CDCA5 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: high mobility group AT-hook 1. This gene encodes a chromatin-associated protein involved in the regulation of gene transcription, integration of retroviruses into chromosomes, and the metastatic progression of cancer cells. The encoded protein preferentially binds to the minor groove of AT-rich regions in double-stranded DNA. Multiple transcript variants encoding different isoforms have been found for this gene. Pseudogenes of …
- **Diseases (Open Targets)**: HIV infectious disease (0.581); neurodegenerative disease (0.526); atrial fibrillation (0.435); type 2 diabetes mellitus (0.409); head and neck squamous cell carcinoma (0.389)
- **Europe PMC papers**: 5150
- **Why important**: HMGA1 is a chromatin-associated transcriptional regulator and forms a strong edge with the central CDCA5 node while also connecting to SYNE1. Its annotations include regulation of transcription, nucleosome disassembly and DNA repair. It has the largest literature footprint among the selected genes and broad disease associations, including cancer, metabolic and neurodegenerative categories. Its HPA profile is nuclear and cell-type enhanced rather than secreted.
- **Conclusion**: Established: HMGA1 provides a plausible chromatin and transcriptional component of the module and is a heavily studied disease-relevant regulator. Hypothesis: HMGA1 may couple proliferative signaling represented by CDCA5 to changes in chromatin accessibility or transcriptional state in the shared tissue samples.

#### SYNE1

- **Related proteins** (co-abundance neighbors): HMGA1 (0.93), P3H1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Nuclear membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: spectrin repeat containing nuclear envelope protein 1. This gene encodes a spectrin repeat containing protein expressed in skeletal and smooth muscle, and peripheral blood lymphocytes, that localizes to the nuclear membrane. Mutations in this gene have been associated with autosomal recessive spinocerebellar ataxia 8, also referred to as autosomal recessive cerebellar ataxia type 1 or recessive ataxia of Beauce. Alternatively spliced transcript varian…
- **Diseases (Open Targets)**: autosomal recessive ataxia, Beauce type (0.802); Emery-Dreifuss muscular dystrophy 4, autosomal dominant (0.769); arthrogryposis multiplex congenita 3, myogenic type (0.753); juvenile amyotrophic lateral sclerosis (0.523); uterine corpus leiomyoma (0.517)
- **Europe PMC papers**: 4332
- **Why important**: SYNE1 occupies the small branch linking HMGA1 and P3H1, giving it a potentially informative position between nuclear regulation and collagen-related cellular function. Its established function concerns the nuclear membrane, nuclear organization, nuclear migration and anchoring of the nuclear matrix. It is associated with peripheral blood lymphocytes and with multiple inherited neuromuscular or ataxia disorders. HPA also reports enhancement in neutrophil-related cell types and nuclear-membrane localization.
- **Conclusion**: Established: SYNE1 is a large nuclear-envelope organizer with recognized disease associations and is co-abundant with both HMGA1 and P3H1 in this module. Hypothesis: SYNE1 may connect proliferative nuclear remodeling with cell-shape or matrix-related processes, although the current network does not demonstrate a physical interaction.

#### P3H1

- **Related proteins** (co-abundance neighbors): SYNE1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prolyl 3-hydroxylase 1. This gene encodes an enzyme that is a member of the collagen prolyl hydroxylase family. These enzymes are localized to the endoplasmic reticulum and their activity is required for proper collagen synthesis and assembly. Mutations in this gene are associated with osteogenesis imperfecta type VIII. Three alternatively spliced transcript variants encoding different isoforms have been described. Other…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 8 (0.751); osteogenesis imperfecta (0.642); osteogenesis imperfecta type 3 (0.533); osteogenesis imperfecta, recessive (0.455); osteogenesis imperfecta type 2 (0.370)
- **Europe PMC papers**: 676
- **Why important**: P3H1 is the module's most directly bone-relevant gene because it encodes an endoplasmic-reticulum collagen prolyl hydroxylase required for collagen synthesis and assembly. It is associated with osteogenesis imperfecta and with collagen metabolic processes, protein folding, protein stabilization and regulation of protein secretion. Its edge to SYNE1 places this extracellular-matrix-related enzyme in the module's secondary branch rather than at the central hub.
- **Conclusion**: Established: P3H1 provides a credible collagen-processing and skeletal-disease connection, and its disease associations make it important for interpreting the bone component. Hypothesis: P3H1 may indicate that the module includes a matrix-producing or matrix-supporting cell state, but its peripheral network position and the absence of enrichment or physical-complex evidence prevent that interpretation from being treated as established.

## Module 9

**Tissue pair**: bone and bone_marrow  
**Genes (7)**: COTL1, GSTP1, PHB1, RNF2, SH3BGRL3, SRXN1, TAGLN2

### Function

No GO or KEGG term passed global correction, so the module does not have a statistically established pathway annotation from those analyses. Its structure instead suggests a mixed cytoskeletal, redox-protective, mitochondrial, and transcriptional-regulatory program. TAGLN2 and COTL1 support actin-related functions, GSTP1 and SRXN1 support protection from reactive or electrophilic stress, PHB1 supports mitochondrial and cellular-state functions, and RNF2 represents chromatin-associated transcriptional regulation. These annotations are heterogeneous rather than pathway-coherent, so the most cautious interpretation is a shared cellular-state module rather than a defined bone-specific biological pathway.

**Cell composition.** The module appears strongly influenced by shared hematopoietic or blood-associated cell composition. HPA shows cell-type enhancement for every module gene, with repeated representation in megakaryocytes and platelets and additional representation in monocytes, myeloid dendritic cells, neutrophils, Hofbauer cells, and related cell types. COTL1 is enriched across several myeloid blood-cell groups, while TAGLN2, SRXN1, and other genes are enhanced in megakaryocytes or platelets. Most genes have low tissue specificity, and only one gene is secreted; therefore this is not primarily a plasma-protein module. The shared bone and bone_marrow signal may consequently reflect common blood-derived or marrow-associated cell types rather than a program intrinsic to bone tissue.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was detected among the module genes, and no STRING functional-enrichment result was reported. No hu.MAP complex contained multiple module members. The co-abundance structure is therefore not supported by currently catalogued physical protein interactions or a recognized multiprotein complex. Within the co-abundance network, RNF2 connects to SH3BGRL3, TAGLN2, and PHB1; TAGLN2 connects onward to GSTP1 and SRXN1; and GSTP1 connects to COTL1. These relationships describe coordinated abundance, not established molecular binding. The lack of STRING and hu.MAP support argues against interpreting the module as a known physical complex, while remaining compatible with shared cell composition, coordinated regulation, or indirect cellular-state effects.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a previously under-characterized co-abundance pattern because it has no reported high-confidence STRING relationships, no multi-member hu.MAP complex, and no globally significant GO or KEGG term. However, it cannot be called a new biological discovery from these facts alone. The genes themselves are well studied, and several have established functions in chromatin regulation, actin organization, oxidative-stress response, mitochondrial biology, or immune-cell biology. The most defensible claim is novelty of the cross-tissue co-abundance pattern, not novelty of the individual genes or of a validated molecular mechanism. Its apparent novelty should also be evaluated against blood-cell composition and dataset-specific technical or sampling effects.

**Hypothesis.** Hypothesis: the module reflects a shared marrow-associated hematopoietic cellular state present in both bone and bone_marrow, particularly involving megakaryocyte or platelet-related cells with contributions from myeloid cells. In this state, actin and cytoskeletal remodeling involving TAGLN2 and COTL1 may be coordinated with antioxidant defenses involving GSTP1 and SRXN1, while RNF2 and PHB1 may reflect broader transcriptional and mitochondrial state changes. This is a mechanistic hypothesis rather than an established pathway assignment. It should be tested by controlling for cell-type abundance, examining single-cell or spatial localization, and validating whether the genes are co-expressed within the same cells rather than contributed by different cell populations.

### Important genes

#### RNF2

- **Related proteins** (co-abundance neighbors): SH3BGRL3 (0.88), TAGLN2 (0.86), PHB1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ring finger protein 2. Polycomb group (PcG) of proteins form the multiprotein complexes that are important for the transcription repression of various genes involved in development and cell proliferation. The protein encoded by this gene is one of the PcG proteins. It has been shown to interact with, and suppress the activity of, transcription factor CP2 (TFCP2/CP2). Studies of the mouse counterpart suggested the involv…
- **Diseases (Open Targets)**: Luo-Schoch-Yamamoto syndrome (0.616); complex neurodevelopmental disorder (0.370); neurodegenerative disease (0.352); body weight gain (0.278); glomerulonephritis (0.220)
- **Europe PMC papers**: 1811
- **Why important**: RNF2 is the most connected network node and links the module's cytoskeletal, mitochondrial, and poorly characterized components. Its established role as a Polycomb-group protein places it in transcriptional repression, chromatin remodeling, heterochromatin formation, development, and cell proliferation. It also has substantial literature coverage and disease associations, making it a biologically informative central candidate rather than merely a peripheral marker.
- **Conclusion**: Established evidence supports RNF2 as a chromatin and transcriptional regulator with relevance to development and proliferation. Its central position in this co-abundance network suggests that it may mark a coordinated cellular state, but there is no evidence here that RNF2 physically regulates the other module genes or drives the shared bone and bone_marrow pattern. Any role as an upstream organizer is therefore a hypothesis.

#### TAGLN2

- **Related proteins** (co-abundance neighbors): RNF2 (0.86), GSTP1 (0.82), SRXN1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transgelin 2. The protein encoded by this gene is similar to the protein transgelin, which is one of the earliest markers of differentiated smooth muscle. The specific function of this protein has not yet been determined, although it is thought to be a tumor suppressor. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2013].
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); neoplasm (0.112); central nervous system cancer (0.108); glioma (0.108); cancer (0.105)
- **Europe PMC papers**: 1580
- **Why important**: TAGLN2 is a central connector between RNF2, GSTP1, and SRXN1. Its established annotation involves actin filament organization and epithelial differentiation, and HPA places it in megakaryocytes and platelets as well as other cell types. This combination makes it a useful candidate linking cellular structure with the blood-associated composition signal.
- **Conclusion**: Established evidence supports TAGLN2 as an actin-related protein with enhancement in megakaryocyte and platelet populations. Its network position is consistent with coordination between cytoskeletal state and stress-response genes, but the fact sheet does not establish a direct TAGLN2 interaction with those proteins or a specific role in bone biology.

#### GSTP1

- **Related proteins** (co-abundance neighbors): COTL1 (0.83), TAGLN2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutathione S-transferase pi 1. Glutathione S-transferases (GSTs) are a family of enzymes that play an important role in detoxification by catalyzing the conjugation of many hydrophobic and electrophilic compounds with reduced glutathione. Based on their biochemical, immunologic, and structural properties, the soluble GSTs are categorized into 4 main classes: alpha, mu, pi, and theta. This GST family member is a polymorphic gene…
- **Diseases (Open Targets)**: neurodegenerative disease (0.350); breast cancer (0.117); hepatocellular carcinoma (0.115); neoplasm (0.114); posterior cortical atrophy (0.113)
- **Europe PMC papers**: 12759
- **Why important**: GSTP1 connects the TAGLN2 branch to COTL1 and has extensive literature coverage. Its established biochemical function includes glutathione-dependent detoxification, response to reactive oxygen species, glutathione metabolism, and modulation of inflammatory responses. Its tissue enhancement in esophagus and lack of bone-marrow protein detection caution against treating it as a bone-specific marker.
- **Conclusion**: Established evidence supports GSTP1 as a redox and detoxification enzyme with inflammatory relevance. In this module it may report oxidative or electrophilic stress in the sampled cellular mixture, but the data do not establish that it is produced by the same cells as TAGLN2 or COTL1, nor that it is causally responsible for the co-abundance pattern.

#### COTL1

- **Related proteins** (co-abundance neighbors): GSTP1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coactosin like F-actin binding protein 1. This gene encodes one of the numerous actin-binding proteins which regulate the actin cytoskeleton. This protein binds F-actin, and also interacts with 5-lipoxygenase, which is the first committed enzyme in leukotriene biosynthesis. Although this gene has been reported to map to chromosome 17 in the Smith-Magenis syndrome region, the best alignments for this gene are to chromosome 16. The Smith-Ma…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.419); placental abruption (0.272); placenta praevia (0.272); placental retention (0.267); cervical carcinoma (0.262)
- **Europe PMC papers**: 1073
- **Why important**: COTL1 is directly connected to GSTP1 and has a strong blood and immune-cell signature in HPA, including classical and non-classical monocytes, eosinophils, neutrophils, and myeloid dendritic cells. Its established function involves F-actin binding and regulation of actin filament polymerization, and it also interacts functionally with five-lipoxygenase in leukotriene biosynthesis. Its skeletal-system disease association makes it relevant to the tissue context, although that association is not evidence of a module mechanism.
- **Conclusion**: Established evidence supports COTL1 as an actin-associated, myeloid-enriched protein with links to inflammatory lipid biology. It is a strong candidate for explaining the blood-cell component of the shared module. The co-abundance data do not show whether COTL1 contributes to bone biology directly or simply tracks immune-cell abundance.

#### SRXN1

- **Related proteins** (co-abundance neighbors): TAGLN2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sulfiredoxin 1. Enables oxidoreductase activity, acting on a sulfur group of donors. Involved in response to oxidative stress. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.101); neoplasm (0.099); colorectal carcinoma (0.077); cervical cancer (0.077); cervical carcinoma (0.077)
- **Europe PMC papers**: 1442
- **Why important**: SRXN1 is connected to TAGLN2 and is annotated for oxidoreductase activity, oxidative-stress response, and cellular oxidant detoxification. HPA reports enhancement in megakaryocytes and immune-cell enrichment in neutrophils, placing it at the intersection of the platelet-associated and myeloid-associated signals. Its literature volume is substantial enough to support a well-established stress-response interpretation.
- **Conclusion**: Established evidence supports SRXN1 as an oxidative-stress response protein. Its presence may indicate redox adaptation in the shared cellular environment, especially in blood-associated cells. It is not possible from this module alone to conclude that oxidative stress drives the co-abundance pattern or that SRXN1 acts directly with TAGLN2.
