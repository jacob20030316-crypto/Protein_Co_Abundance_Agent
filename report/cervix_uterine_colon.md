# Conserved co-abundance modules: cervix_uterine and colon

## Module 0

**Tissue pair**: cervix_uterine and colon  
**Genes (30)**: YWHAH, ABLIM1, ARPC4, CACNA1F, COTL1, SPECC1L, DCTN1, DNAJB1, DYNC1H1, EHD4, FLII, G6PD, GPRC5B, GPD2, H1-2, HARS1, HMOX1, KRT16, KRT9, KRT1, METAP2, IMMT, PDCD6IP, PDLIM2, PYGL, RRBP1, SCFD1, SLX4, UBA6, TJP1

### Function

No GO or KEGG term passed global multiple-testing correction, so there is no globally significant pathway annotation for this module. The network is sparse and heterogeneous, but its strongest co-abundance structure is centered on CACNA1F and GPRC5B. The gene annotations suggest several convergent cellular themes: epithelial and cell-junction organization through TJP1, KRT1, KRT9, KRT16, ABLIM1 and SPECC1L; actin and cytoskeletal regulation through ABLIM1, ARPC4, PDLIM2, COTL1, FLII and SPECC1L; vesicle, membrane and intracellular transport through GPRC5B, PDCD6IP, EHD4, SCFD1, DYNC1H1 and DCTN1; and cellular stress or metabolic support through HMOX1, G6PD, DNAJB1 and related genes. The module should therefore be interpreted as a mixed epithelial, cytoskeletal, membrane-transport and stress-associated co-abundance signal rather than as a demonstrated single biochemical pathway. The apparent convergence may reflect shared cell composition or coordinated tissue-state regulation rather than direct physical interaction among most module members.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the fact sheet identifies only one secreted gene, and most genes are intracellular, membrane-associated, cytoskeletal, nuclear or metabolic proteins. It is also not a uniformly broadly expressed housekeeping module. HPA evidence shows a mixture of low tissue specificity, tissue-enhanced and tissue-enriched genes, with recurring signals from brain, lymphoid tissue, skin and blood vessel. At the single-cell level, esophageal apical cells, platelets, megakaryocytes, astrocytes and oligodendrocytes recur among the enriched annotations. Blood-cell annotations also recur, especially for eosinophils, neutrophils and monocyte populations. These findings raise a substantial possibility that the shared cervix_uterine and colon signal partly reflects epithelial, vascular, platelet or infiltrating myeloid-cell composition. The HPA protein-detection pattern is compatible with tissue presence for many genes, but several genes are not detected in one or both tissues, so transcript or protein co-abundance should not be assumed to represent a single resident cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence known interaction within the module, DCTN1-DYNC1H1. This is biologically coherent because DCTN1 is a dynactin subunit and DYNC1H1 is the cytoplasmic dynein heavy chain, together supporting microtubule-based intracellular transport. No STRING functional-enrichment result was reported, and the absence of STRING enrichment is supplementary evidence rather than evidence against the module. The co-abundance edges are therefore mostly not established STRING physical interactions. hu.MAP identifies ABLIM1 and SPECC1L together in two complexes, (hu.MAP huMAP3_08205.1) and (hu.MAP huMAP3_09542.1). Both complexes contain broader actin, contractility, adhesion and small-GTPase-associated membership, which supports a cytoskeletal or junctional interpretation, but only a small subset of each complex is represented in this module. Consequently, the hu.MAP results provide partial structural support rather than evidence that the complete module is one known complex.

**STRING interactions (score >= 0.7)**: 1 of 435 gene pairs: DCTN1–DYNC1H1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08205.1 (ABLIM1, SPECC1L; 2/17); huMAP3_09542.1 (ABLIM1, SPECC1L; 2/38)

### Novelty

The module may represent a context-specific co-abundance pattern, but the fact sheet does not establish it as a new biological mechanism. Several components have well-established functions, including tight-junction organization, keratin biology, actin remodeling, heme metabolism, dynein-dynactin transport and calcium-channel activity. The known DCTN1-DYNC1H1 interaction and the ABLIM1-SPECC1L hu.MAP associations show that parts of the module overlap established biology. At the same time, most module relationships are absent from the reported STRING network and the module has no globally significant GO or KEGG term, making it difficult to assign a previously recognized pathway identity. Absence from STRING or hu.MAP does not prove novelty because co-abundance can reflect tissue composition, regulation, cell state or technical covariance rather than physical binding. The defensible conclusion is that the cross-tissue co-abundance configuration is potentially novel, whereas the individual gene functions and some relationships are not novel.

**Hypothesis.** Hypothesis: the shared cervix_uterine-colon module reflects a mixed epithelial and vascular or immune-cell state in which junctional and actin remodeling, membrane trafficking, cytoskeletal transport, oxidative-stress handling and metabolic support vary together. TJP1, keratins, ABLIM1 and SPECC1L could mark epithelial architecture and actin-linked adhesion; HMOX1 and G6PD could reflect stress adaptation and redox support; GPRC5B, PDCD6IP, EHD4 and SCFD1 could contribute to membrane or vesicle regulation; and the DCTN1-DYNC1H1 pair could represent intracellular transport. CACNA1F may act as a highly connected co-abundance hub without implying that a retinal calcium-channel mechanism is active in cervix or colon. A competing explanation is that the module is driven primarily by variable contributions from epithelial cells, platelets or myeloid cells. This hypothesis requires validation by cell-resolved expression, tissue histology, replication in independent cohorts and perturbation of candidate regulators.

### Important genes

#### GPRC5B

- **Related proteins** (co-abundance neighbors): ABLIM1 (0.96), DNAJB1 (0.96), H1-2 (0.94), KRT16 (0.91), HMOX1 (0.91), TJP1 (0.89), KRT1 (0.88), HARS1 (0.88), ARPC4 (0.85), GPD2 (0.85), YWHAH (0.85), IMMT (0.84), SCFD1 (0.83), SPECC1L (0.80), RRBP1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein-coupled receptor class C group 5 member B. This gene encodes a member of the type 3 G protein-coupled receptor family. Members of this superfamily are characterized by a signature 7-transmembrane domain motif. The encoded protein may modulate insulin secretion and increased protein expression is associated with type 2 diabetes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2015].
- **Diseases (Open Targets)**: megalencephalic leukoencephalopathy with subcortical cysts 3 (0.436); Abnormality of the skeletal system (0.401); megalencephalic leukoencephalopathy with subcortical cysts (0.372); osteoarthritis, knee (0.318); osteoarthritis (0.312)
- **Europe PMC papers**: 727
- **Why important**: GPRC5B is one of the most highly connected module genes and links genes associated with epithelial junctions, keratins, stress response, chaperoning, translation and cytoskeletal organization. Its HPA profile is tissue-enhanced in brain and cell-type-enhanced in several glial and epithelial-related populations, while its protein is not detected in the two named tissues. Its known role as a class C G-protein-coupled receptor family member and its association with insulin secretion and type two diabetes make it a plausible signaling or cell-state marker. The literature is substantial enough to support a recognized biological role, but the module provides no direct evidence for a specific GPRC5B-mediated pathway.
- **Conclusion**: Established: GPRC5B is a membrane signaling protein with a prominent position in this co-abundance network and documented metabolic associations. Hypothesis: it may coordinate or report a tissue-state program involving epithelial organization, vesicle handling and stress adaptation, but this regulatory role in cervix_uterine and colon remains unproven.

#### CACNA1F

- **Related proteins** (co-abundance neighbors): PDLIM2 (1.00), HMOX1 (1.00), G6PD (0.98), KRT9 (0.97), YWHAH (0.95), COTL1 (0.89), ARPC4 (0.88), DYNC1H1 (0.86), METAP2 (0.85), PYGL (0.85), PDCD6IP (0.84), FLII (0.84), UBA6 (0.84), EHD4 (0.81), DCTN1 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium voltage-gated channel subunit alpha1 F. This gene encodes a multipass transmembrane protein that functions as an alpha-1 subunit of the voltage-dependent calcium channel, which mediates the influx of calcium ions into the cell. The encoded protein forms a complex of alpha-1, alpha-2/delta, beta, and gamma subunits in a 1:1:1:1 ratio. Mutations in this gene can cause X-linked eye disorders, including congenital stationary night blindness…
- **Diseases (Open Targets)**: congenital stationary night blindness 2A (0.803); Aland island eye disease (0.735); X-linked cone-rod dystrophy 3 (0.665); cone-rod dystrophy (0.646); congenital stationary night blindness (0.644)
- **Europe PMC papers**: 1115
- **Why important**: CACNA1F is a major network hub and connects to genes spanning redox metabolism, keratin biology, actin regulation, cytoskeletal transport and the DYNC1H1 axis. HPA strongly associates it with retina and photoreceptor cell types, and its established function is a voltage-dependent calcium-channel alpha subunit involved in calcium entry and visual signaling. Its disease associations with inherited retinal disorders and its substantial literature make the annotation reliable, while its lack of STRING or hu.MAP partners in this module argues against treating it as a validated physical scaffold here.
- **Conclusion**: Established: CACNA1F is a calcium-channel subunit with strong retinal biology and inherited eye-disease associations. Hypothesis: in this module it may be a surrogate for membrane excitability, calcium-dependent trafficking or cell-composition covariance rather than evidence of retinal-like signaling in the two tissues.

#### HMOX1

- **Related proteins** (co-abundance neighbors): CACNA1F (1.00), GPRC5B (0.91); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location Golgi apparatus, Plasma membrane; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heme oxygenase 1. Heme oxygenase, an essential enzyme in heme catabolism, cleaves heme to form biliverdin, which is subsequently converted to bilirubin by biliverdin reductase, and carbon monoxide, a putative neurotransmitter. Heme oxygenase activity is induced by its substrate heme and by various nonheme substances. Heme oxygenase occurs as 2 isozymes, an inducible heme oxygenase-1 and a constitutive heme oxygenas…
- **Diseases (Open Targets)**: heme oxygenase 1 deficiency (0.686); amyloidosis (0.465); neurodegenerative disease (0.459); cystic fibrosis (0.392); chronic obstructive pulmonary disease (0.360)
- **Europe PMC papers**: 38190
- **Why important**: HMOX1 is a biologically important stress-response and heme-catabolism gene, with extensive literature and associations involving inflammation, angiogenesis, wound healing and leukocyte migration. Its HPA annotations point to lymphoid tissue, macrophage-related cell types and monocyte populations, and its protein is detected in colon but not cervix_uterine. Although it has limited connectivity within the module, its direct links to CACNA1F and GPRC5B may identify a stress or inflammatory branch of the co-abundance pattern.
- **Conclusion**: Established: HMOX1 is an inducible heme-catabolic enzyme associated with inflammatory and tissue-repair biology. Hypothesis: its presence may indicate oxidative or inflammatory state variation, or variation in myeloid-cell contribution, rather than a core structural component of the module.

#### TJP1

- **Related proteins** (co-abundance neighbors): GPRC5B (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cell Junctions; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tight junction protein 1. This gene encodes a member of the membrane-associated guanylate kinase (MAGUK) family of proteins, and acts as a tight junction adaptor protein that also regulates adherens junctions. Tight junctions regulate the movement of ions and macromolecules between endothelial and epithelial cells. The multidomain structure of this scaffold protein, including a postsynaptic density 95/disc-large/zona occlu…
- **Diseases (Open Targets)**: dengue disease (0.476); COVID-19 (0.373); skin disorder (0.312); Hypocalcemia (0.264); cataract (0.256)
- **Europe PMC papers**: 6421
- **Why important**: TJP1 is a key epithelial and endothelial junctional adaptor with extensive literature and established roles in tight-junction assembly, adherens-junction maintenance and actin-linked barrier organization. It is connected to GPRC5B in the module, is localized to cell junctions, and is detected by HPA in both tissues. Its epithelial and barrier function provides one of the clearest mechanistic anchors for interpreting the module in cervix_uterine and colon.
- **Conclusion**: Established: TJP1 supports cell-cell junctions and links membrane junctions to the actin cytoskeleton. Hypothesis: coordinated TJP1 abundance may indicate epithelial barrier remodeling or differences in epithelial content across samples, but the module does not demonstrate altered junctional function.

#### ABLIM1

- **Related proteins** (co-abundance neighbors): GPRC5B (0.96); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: huMAP3_08205.1, huMAP3_09542.1
- **Function (MyGene.info)**: actin binding LIM protein 1. This gene encodes a LIM zinc-binding domain-containing protein that binds to actin filaments and mediates interactions between actin and cytoplasmic targets. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jun 2017].
- **Diseases (Open Targets)**: atrial fibrillation (0.464); diabetic ketoacidosis (0.269); preeclampsia (0.256); tooth disorder (0.244); lacrimal apparatus disorder (0.244)
- **Europe PMC papers**: 832
- **Why important**: ABLIM1 is an actin-binding LIM protein with a direct cytoskeletal role and is detected in both named tissues. It is connected to GPRC5B and occurs with SPECC1L in both hu.MAP complexes (hu.MAP huMAP3_08205.1) and (hu.MAP huMAP3_09542.1), providing the strongest complex-level support for an actin, adhesion or morphogenesis-related component. Its literature and disease associations are less extensive than those of TJP1 or HMOX1, but its molecular function and complex placement are particularly informative for this module.
- **Conclusion**: Established: ABLIM1 binds actin-associated structures and participates in cytoskeletal organization, and its co-membership with SPECC1L is supported by hu.MAP. Hypothesis: ABLIM1 may connect epithelial junctional remodeling with the broader membrane and transport signal, although the module does not establish a direct interaction with GPRC5B.

## Module 1

**Tissue pair**: cervix_uterine and colon  
**Genes (29)**: NT5C3A, ANXA3, ARG1, BCL10, CALML3, CCDC138, COPG2, FERRY3, GLTP, GPAT3, KRT10, KRT2, PACSIN3, CBFB, PKP3, PSTPIP2, PRIM2, RAP2B, RIOK3, RTN1, SASH1, STARD10, STRN, TAP1, TAP2, TTC3, UBAP1, WDR26, ZNF462

### Function

The module does not have a single statistically established pathway function: no GO or KEGG term passed global correction, and there are no supplementary STRING enrichment terms. Its biological signal is nevertheless coherent at the level of constituent genes. It combines epithelial differentiation and structural maintenance, antigen-processing machinery, immune and inflammatory signaling, vesicle and membrane trafficking, and selected metabolic or cellular-maintenance functions. The strongest network-organizing feature is CCDC138, which connects genes from several otherwise weakly connected branches. The pattern is therefore best interpreted as a mixed epithelial-interface and immune-surveillance module rather than as evidence for one defined biochemical pathway. The absence of globally significant enrichment does not invalidate the module.

**Cell composition.** The module is not predominantly plasma or secreted: HPA identifies only one secreted gene. It is also not uniformly broadly expressed housekeeping biology, because many members show tissue or cell-type enhancement. The most frequent HPA signals point to epithelial populations, especially esophageal apical cells and suprabasal keratinocytes, with additional signals in neutrophils, neutrophil progenitors, platelets, bone marrow, skeletal muscle, and liver. Several genes are enriched in skin or esophagus, including KRT2, KRT10, CALML3, PKP3, and GLTP, while ARG1, ANXA3, and related genes support a myeloid or neutrophil-associated component. Protein detection in both cervix and colon supports that the module is technically observable in both tissues, but the mixed epithelial and blood-cell profile means that shared epithelial cell states, immune admixture, or both may contribute to the co-abundance pattern. ARG1 is not detected by HPA protein in either queried tissue, and some other members have tissue-specific absence, so transcript co-abundance should not automatically be interpreted as coordinated protein production.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports only a few high-confidence pairwise relationships: CALML3 with STRN, KRT10 with KRT2, and TAP1 with TAP2. These are biologically interpretable links involving calcium or signaling scaffolding, epithelial keratins, and peptide transport for antigen presentation, respectively. Most module pairs are not supported by the reported STRING network, so the co-abundance graph should not be treated as a densely established physical interaction network. hu.MAP provides convergent complex-level evidence for CALML3 and PKP3, with ARG1 also present in the larger complexes (hu.MAP huMAP3_09125.1) and (hu.MAP huMAP3_09929.1). CALML3 and PKP3 recur across (hu.MAP huMAP3_09125.1), (hu.MAP huMAP3_09929.1), (hu.MAP huMAP3_06046.1), and (hu.MAP huMAP3_07972.1), making them the clearest complex-associated module members. These complexes contain many epithelial, junctional, keratinization, and immune-associated proteins, but the module includes only a subset of their members. Thus, the hu.MAP results support shared complex context, while STRING confirms only selected direct relationships.

**STRING interactions (score >= 0.7)**: 3 of 406 gene pairs: CALML3–STRN (0.959); KRT10–KRT2 (0.904); TAP1–TAP2 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09125.1 (ARG1, CALML3, PKP3; 3/53); huMAP3_09929.1 (ARG1, CALML3, PKP3; 3/75); huMAP3_06046.1 (CALML3, PKP3; 2/5); huMAP3_07972.1 (CALML3, PKP3; 2/7)

### Novelty

This is not established as a new molecular complex or pathway. The KRT10-KRT2 pair, TAP1-TAP2 pair, CALML3-STRN relationship, and the CALML3-PKP3-containing hu.MAP complexes are already known interaction or complex contexts. The module may still represent a new cross-tissue co-abundance pattern because most of its edges lack reported STRING or hu.MAP support and because it brings epithelial, antigen-presentation, myeloid, trafficking, and metabolic genes together in cervix and colon. However, absence from STRING or hu.MAP alone cannot establish novelty. A defensible claim is that the cross-tissue module configuration is potentially novel and hypothesis-generating, not that its individual relationships or functions are newly discovered.

**Hypothesis.** Hypothesis: the module reflects a shared mucosal-interface state in which epithelial differentiation and junctional integrity are coordinated with local immune surveillance and cellular stress handling. In this model, CALML3 and PKP3 mark an epithelial structural or complex-associated axis, KRT2 and KRT10 represent epithelial differentiation, TAP1 and TAP2 represent antigenic peptide transport, and BCL10, SASH1, RIOK3, ANXA3, and ARG1 represent immune or inflammatory context. CCDC138 may act as a co-abundance hub that links these otherwise heterogeneous programs, but its molecular role in this module is unknown. The observed pattern could arise from coordinated biology within epithelial cells, from shared epithelial and immune cell proportions across samples, or from both. Testing this hypothesis would require cell-composition adjustment, independent cohorts, and perturbational or spatial validation.

### Important genes

#### CCDC138

- **Related proteins** (co-abundance neighbors): RAP2B (0.92), TAP1 (0.91), WDR26 (0.88), PRIM2 (0.84), PACSIN3 (0.84), BCL10 (0.83), KRT2 (0.82), TAP2 (0.81), KRT10 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coiled-coil domain containing 138
- **Diseases (Open Targets)**: Hirsutism (0.316); placental abruption (0.262); benign urinary system neoplasm (0.173); disturbance of skin sensation (0.097); acne (0.069)
- **Europe PMC papers**: 72
- **Why important**: CCDC138 has the strongest network position in the module and connects RAP2B, TAP1, WDR26, PRIM2, PACSIN3, BCL10, KRT2, and TAP2. It is detected by HPA in both cervix and colon, but has no reported STRING partner, no hu.MAP assignment, and limited functional annotation. Its position makes it the main candidate for organizing the cross-program co-abundance pattern, while its sparse literature and uncertain function make it particularly informative for follow-up.
- **Conclusion**: Established evidence supports CCDC138 as the network hub and as a protein-detected member of both tissues. It is not established that CCDC138 mechanistically controls epithelial, immune, or antigen-presentation biology. Its role as a coordinator is a hypothesis based on network position, not a demonstrated function.

#### CALML3

- **Related proteins** (co-abundance neighbors): RTN1 (0.95), COPG2 (0.88), STARD10 (0.84); STRING partners: STRN (0.959)
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location None; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1, huMAP3_06046.1, huMAP3_07972.1
- **Function (MyGene.info)**: calmodulin like 3. Predicted to enable calcium ion binding activity and enzyme regulator activity. Predicted to be involved in regulation of catalytic activity. Located in extracellular exosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: ocular hypotension (0.296); gastric ulcer (0.184); neoplasm (0.091); hepatocellular carcinoma (0.077); thyroid gland papillary carcinoma (0.075)
- **Europe PMC papers**: 907
- **Why important**: CALML3 is tissue-enhanced in cervix, esophagus, skin, and vagina, is associated with esophageal epithelial cell types, and is detected in both queried tissues. It has a direct STRING relationship with STRN and appears in all reported hu.MAP complexes containing module members (hu.MAP huMAP3_09125.1), (hu.MAP huMAP3_09929.1), (hu.MAP huMAP3_06046.1), and (hu.MAP huMAP3_07972.1). Its annotated calcium-binding and regulatory potential, together with its epithelial distribution, makes it a strong bridge between epithelial state and complex-level evidence.
- **Conclusion**: Established evidence supports CALML3 as an epithelial-associated module member with repeated hu.MAP context and one high-confidence STRING relationship. A specific role for CALML3 in coordinating this cervix-colon module remains unproven.

#### PKP3

- **Related proteins** (co-abundance neighbors): ARG1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cell Junctions; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1, huMAP3_06046.1, huMAP3_07972.1
- **Function (MyGene.info)**: plakophilin 3. This gene encodes a member of the arm-repeat (armadillo) and plakophilin gene families. Plakophilin proteins contain numerous armadillo repeats, localize to cell desmosomes and nuclei, and participate in linking cadherins to intermediate filaments in the cytoskeleton. This protein may act in cellular desmosome-dependent adhesion and signaling pathways. Two transcript variants encoding different is…
- **Diseases (Open Targets)**: anorectal malformation (0.295); neurodegenerative disease (0.292); lymphopenia (0.111); neutropenia (0.111); hypertensive disorder (0.106)
- **Europe PMC papers**: 747
- **Why important**: PKP3 is associated with colonocytes, enterocytes, and epithelial cell populations, is tissue-enhanced in esophagus and skin, and is localized to cell junctions. It is present with CALML3 in every reported hu.MAP complex relevant to this module (hu.MAP huMAP3_09125.1), (hu.MAP huMAP3_09929.1), (hu.MAP huMAP3_06046.1), and (hu.MAP huMAP3_07972.1). Its established role in desmosome assembly, epithelial structure maintenance, and cytokine-related regulation provides a plausible structural anchor for a mucosal epithelial component.
- **Conclusion**: Established evidence supports PKP3 as an epithelial junction and desmosome-associated gene embedded in recurrent complex context. The data do not establish that PKP3 drives the shared co-abundance state or directly links epithelial structure to immune surveillance here.

#### TAP1

- **Related proteins** (co-abundance neighbors): CCDC138 (0.91); STRING partners: TAP2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Centriolar satellite; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transporter 1, ATP binding cassette subfamily B member. The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily ar…
- **Diseases (Open Targets)**: MHC class I deficiency (0.760); MHC class II deficiency (0.371); autoimmune disorder of central nervous system (0.357); neurodegenerative disease (0.240); hereditary disease (0.193)
- **Europe PMC papers**: 7090
- **Why important**: TAP1 is detected in both cervix and colon, is connected to CCDC138 in the module graph, and forms a high-confidence STRING pair with TAP2. Its established function in cytosol-to-endoplasmic-reticulum peptide transport and MHC class I antigen presentation gives the module a clear immune-surveillance component. Its disease associations include MHC class I deficiency and immune disorders.
- **Conclusion**: Established evidence supports TAP1 as part of the TAP1-TAP2 antigen-processing transporter and as a module link to the CCDC138 hub. It is plausible that the module reflects epithelial antigen presentation or immune-cell admixture, but the source of the TAP signal cannot be resolved from the fact sheet.

#### ARG1

- **Related proteins** (co-abundance neighbors): PRIM2 (0.96), GPAT3 (0.96), CBFB (0.91), ANXA3 (0.85), NT5C3A (0.84), STRN (0.83), PKP3 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: arginase 1. Arginase catalyzes the hydrolysis of arginine to ornithine and urea. At least two isoforms of mammalian arginase exist (types I and II) which differ in their tissue distribution, subcellular localization, immunologic crossreactivity and physiologic function. The type I isoform encoded by this gene, is a cytosolic enzyme and expressed predominantly in the liver as a component of the urea cycle. Inh…
- **Diseases (Open Targets)**: arginase deficiency (0.836); type 2 diabetes mellitus (0.430); hereditary disease (0.414); obesity disorder (0.345); metabolic syndrome (0.320)
- **Europe PMC papers**: 24778
- **Why important**: ARG1 has a strong network position relative to most module members and connects PRIM2, GPAT3, CBFB, ANXA3, NT5C3A, STRN, and PKP3. It is tissue-enriched in liver and associated with neutrophils and neutrophil progenitors, while its established enzyme function is arginine hydrolysis in the urea-cycle context. It also occurs in the larger hu.MAP complexes with CALML3 and PKP3 (hu.MAP huMAP3_09125.1) and (hu.MAP huMAP3_09929.1), despite lacking a reported STRING partner.
- **Conclusion**: Established evidence supports ARG1 as a metabolic enzyme with strong liver and neutrophil associations and as a member of the reported hu.MAP contexts. Its absence from HPA protein detection in both queried tissues weakens a claim that it is produced by the principal tissue cells. A blood-cell or neutrophil contribution is therefore a plausible interpretation, not a demonstrated source.

## Module 2

**Tissue pair**: cervix_uterine and colon  
**Genes (6)**: A1BG, APOE, SERPINF1, PLG, F2, VTN

### Function

The strongest interpretation is a secreted extracellular blood-proteostasis and wound-response module centered on coagulation, hemostasis, fibrinolysis, and regulation of wound healing. The primary GO evidence is highly coherent: the same core of APOE, F2, PLG, and VTN supports regulation of coagulation and hemostasis (6 globally significant GO/KEGG terms, q_global 0.000456–0.00078; see the table), while F2, PLG, and VTN support fibrinolysis and positive regulation of wound responses (11 globally significant GO/KEGG terms, q_global 0.00139–0.0116; see the table). The blood-microparticle and heparin-binding terms provide additional support (GO:CC blood microparticle; q_global = 0.00128) and (GO:MF heparin binding; q_global = 0.043). This is a functional interpretation of the module rather than evidence that these proteins form one obligatory biochemical complex. The relatively sparse co-abundance graph nevertheless has a central PLG position, connecting F2, VTN, and A1BG, with VTN linking to SERPINF1 and APOE linking to VTN through the broader interaction evidence. The module therefore most plausibly represents coordinated extracellular and circulating regulation of clot formation, clot resolution, matrix interaction, and tissue repair.

**Cell composition.** All module genes are annotated as secreted to blood by HPA. The HPA profile is dominated by liver enrichment and hepatocyte association, with additional tissue or cell-type associations for adrenal gland, brain, choroid plexus, cholangiocytes, proximal tubule cells, decidual stromal cells, retinal pigment epithelial cells, and plasmacytoid dendritic cells. Most genes were not detected in immune cells, so this does not primarily resemble a blood-cell transcriptional program. Protein was not detected in the sampled cervix or colon tissues for the genes with available HPA measurements. The shared tissue module may therefore reflect circulating plasma or extracellular-fluid carryover, vascular or stromal material, or a common contribution from liver-derived proteins rather than coordinated local expression by cervix and colon cells. A1BG is a plasma glycoprotein with unknown function, which further supports caution about assigning the entire module to a local tissue mechanism.

**GO/KEGG enrichment**: 26 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP negative regulation of blood coagulation | 0.000456 | APOE, F2, PLG, VTN |
| GO:BP negative regulation of hemostasis | 0.000456 | APOE, F2, PLG, VTN |
| GO:BP regulation of blood coagulation | 0.000552 | APOE, F2, PLG, VTN |
| GO:BP regulation of hemostasis | 0.000552 | APOE, F2, PLG, VTN |
| GO:BP negative regulation of coagulation | 0.000656 | APOE, F2, PLG, VTN |
| GO:BP regulation of coagulation | 0.00078 | APOE, F2, PLG, VTN |
| GO:BP negative regulation of wound healing | 0.00119 | APOE, F2, PLG, VTN |
| GO:CC blood microparticle | 0.00128 | A1BG, APOE, F2, PLG, VTN |
| GO:BP positive regulation of blood coagulation | 0.00139 | F2, PLG, VTN |
| GO:BP positive regulation of coagulation | 0.00139 | F2, PLG, VTN |
| GO:BP regulation of fibrinolysis | 0.00139 | F2, PLG, VTN |
| GO:BP negative regulation of fibrinolysis | 0.00139 | F2, PLG, VTN |
| GO:BP positive regulation of hemostasis | 0.00139 | F2, PLG, VTN |
| GO:BP negative regulation of response to wounding | 0.00178 | APOE, F2, PLG, VTN |
| GO:BP regulation of wound healing | 0.00252 | APOE, F2, PLG, VTN |

### STRING and hu.MAP

STRING supports a connected extracellular interaction neighborhood: PLG has strong links with VTN and SERPINF1 and a lower-confidence link with F2; VTN is linked with APOE and SERPINF1; and F2 is linked with SERPINF1 (4 supplementary STRING terms; within-query FDR 6.57e-06–0.00024). The STRING functional results independently emphasize collagen-containing extracellular matrix, blood microparticles, and secreted proteins (4 supplementary STRING terms; within-query FDR 6.57e-06–0.00024). The STRING relationships are therefore consistent with the inferred biology, but they are database-supported associations and do not by themselves establish physical interaction in cervix or colon. hu.MAP provides repeated complex-context support for F2, PLG, and A1BG across several plasma-protein and complement-related complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1), and supports F2 with PLG in additional complexes (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1). PLG with A1BG is also represented in another complex context (hu.MAP huMAP3_15040.1). These complexes contain many circulating coagulation, complement, acute-phase, and transport proteins, suggesting that the module is embedded in a broader plasma-protein network rather than defining a private complex. VTN, SERPINF1, and APOE lack hu.MAP complex representation in the supplied results.

**STRING interactions (score >= 0.7)**: 6 of 15 gene pairs: APOE–VTN (0.989); F2–PLG (0.826); F2–SERPINF1 (0.804); PLG–SERPINF1 (0.995); PLG–VTN (0.995); SERPINF1–VTN (0.828)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Collagen-containing extracellular matrix (FDR = 6.57e-06, 6 genes); Component Blood microparticle (FDR = 5.67e-05, 5 genes); Keyword Secreted (FDR = 0.00017, 6 genes); COMPARTMENTS Blood microparticle (FDR = 0.00024, 5 genes); TISSUES Cerebrospinal fluid (FDR = 0.0004, 4 genes); PMID (2014) Protein corona composition of superparamagnetic iron oxide nanoparticles with various physico-chemical properties and coatings. (FDR = 0.00043, 5 genes); Keyword Signal (FDR = 0.00044, 6 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 0.00073, 6 genes); PMID (2021) Detection of Circulating Serum Protein Biomarkers of Non-Muscle Invasive Bladder Cancer after Protein Corona-Silver Nanoparticles Analysis by SWATH-MS. (FDR = 0.0009, 5 genes); PMID (2010) Multifunctional agents for concurrent imaging and therapy in cardiovascular disease. (FDR = 0.0009, 4 genes); PMID (2023) Interrelationship between COVID-19 and Coagulopathy: Pathophysiological and Clinical Evidence. (FDR = 0.00093, 4 genes); PMID (2023) Differences in coagulation-relevant parameters: Comparing cryoprecipitate and a human fibrinogen concentrate. (FDR = 0.00093, 4 genes); PMID (2023) Comparison of in-gel and in-solution proteolysis in the proteome profiling of organ perfusion solutions. (FDR = 0.00093, 5 genes); PMID (2023) Immune cell-mediated venous thrombus resolution. (FDR = 0.00093, 4 genes); PMID (2022) Circulating Proteins Associated with Response and Resistance to Neoadjuvant Chemotherapy in HER2-Positive Breast Cancer. (FDR = 0.00093, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08395.1 (F2, PLG, A1BG; 3/43); huMAP3_09531.1 (F2, PLG, A1BG; 3/47); huMAP3_10101.1 (F2, PLG, A1BG; 3/49); huMAP3_10678.1 (F2, PLG, A1BG; 3/71); huMAP3_08796.1 (F2, PLG; 2/15); huMAP3_09832.1 (F2, PLG; 2/18); huMAP3_07701.1 (F2, PLG; 2/22); huMAP3_09273.1 (F2, PLG; 2/28); huMAP3_15040.1 (PLG, A1BG; 2/64)

### Novelty

The biological theme is not a new pathway: coagulation, fibrinolysis, extracellular matrix interaction, and circulating plasma proteins are established functions, and several of the pairwise associations are already represented in STRING or hu.MAP. The potentially novel result is the conserved co-abundance of this particular secreted protein set across cervix and colon. However, the supplied evidence does not establish that this tissue-pair module has not been reported previously, and absence of a complete match in STRING or hu.MAP would not prove novelty because those resources measure known interactions or complexes rather than this specific cross-tissue co-abundance pattern. The most defensible conclusion is that the module is a potentially novel dataset-level observation of a known circulating extracellular program, requiring comparison with prior co-expression, proteomic, and tissue-deconvolution studies before being called a new biological discovery.

**Hypothesis.** Hypothesis: the shared module reflects a liver-derived circulating plasma-protein program that enters or is retained in extracellular, vascular, stromal, or vesicular compartments associated with both cervix and colon samples. In this model, F2 and PLG represent coordinated coagulation and fibrinolytic capacity, VTN provides extracellular-matrix and adhesion context, SERPINF1 contributes anti-angiogenic and migration-regulatory activity, APOE contributes lipid transport and vesicular or extracellular organization, and A1BG marks the broader plasma-glycoprotein background. The co-abundance could therefore arise from common exposure to blood or extracellular fluid, vascular remodeling, or wound-repair conditions rather than synchronized transcription within the resident epithelial cells. This hypothesis should be tested with plasma-depletion or vascular-content controls, cell-type-resolved measurements, and orthogonal protein assays.

### Important genes

#### PLG

- **Related proteins** (co-abundance neighbors): F2 (0.86), VTN (0.83), A1BG (0.82); STRING partners: F2 (0.826), SERPINF1 (0.995), VTN (0.995)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07701.1, huMAP3_09273.1, huMAP3_15040.1
- **Function (MyGene.info)**: plasminogen. The plasminogen protein encoded by this gene is a serine protease that circulates in blood plasma as an inactive zymogen and is converted to the active protease, plasmin, by several plasminogen activators such as tissue plasminogen activator (tPA), urokinase plasminogen activator (uPA), kallikrein, and factor XII (Hageman factor). The conversion of plasminogen to plasmin involves the cleavage of t…
- **Diseases (Open Targets)**: hypoplasminogenemia (0.813); hereditary angioedema (0.737); hemorrhage (0.605); dysplasminogenemia (0.598); Menorrhagia (0.579)
- **Europe PMC papers**: 17740
- **Why important**: PLG is the most connected and strongest node in the supplied module graph. It links F2, VTN, and A1BG, has extensive STRING support with SERPINF1 and VTN, and appears across the hu.MAP contexts (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_15040.1). Its annotated conversion to plasmin directly connects coagulation, fibrinolysis, extracellular-matrix disassembly, and wound biology (25 globally significant GO/KEGG terms, q_global 0.000456–0.0415; see the table). It also has substantial disease and literature support, including plasminogen disorders, hemorrhage, and menorrhagia.
- **Conclusion**: Established evidence supports PLG as a central circulating proteolysis and fibrinolysis component and as the principal network bridge in this module. The hypothesis that PLG organizes the module in the sampled tissues remains unproven because its HPA profile indicates liver and hepatocyte enrichment, secretion to blood, and lack of protein detection in the sampled cervix and colon.

#### F2

- **Related proteins** (co-abundance neighbors): PLG (0.86); STRING partners: PLG (0.826), SERPINF1 (0.804)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07701.1, huMAP3_09273.1
- **Function (MyGene.info)**: coagulation factor II, thrombin. This gene encodes the prothrombin protein (also known as coagulation factor II). This protein is proteolytically cleaved in multiple steps to form the activated serine protease thrombin. The activated thrombin enzyme plays an important role in thrombosis and hemostasis by converting fibrinogen to fibrin during blood clot formation, by stimulating platelet aggregation, and by activating additional …
- **Diseases (Open Targets)**: congenital prothrombin deficiency (0.827); thrombophilia due to thrombin defect (0.738); venous thromboembolism (0.727); deep vein thrombosis (0.690); blood coagulation disease (0.670)
- **Europe PMC papers**: 109299
- **Why important**: F2 encodes prothrombin, whose activated product thrombin is a central coagulation protease and also participates in platelet activation, tissue repair, and angiogenesis. F2 is present in nearly all primary coagulation, hemostasis, fibrinolysis, and wound-response evidence (25 globally significant GO/KEGG terms, q_global 0.000456–0.0415; see the table). It connects to PLG in the module graph and is supported by STRING and repeated hu.MAP plasma-protein contexts (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1). Its disease associations include congenital prothrombin deficiency, thrombophilia, venous thromboembolism, deep vein thrombosis, and coagulation disease, with very extensive literature support.
- **Conclusion**: Established evidence identifies F2 as a biologically important coagulation and wound-response anchor. The module does not show that F2 is locally produced by cervix or colon; HPA instead supports liver and hepatocyte enrichment and secretion to blood, so its co-abundance may primarily report circulating or vascular material.

#### VTN

- **Related proteins** (co-abundance neighbors): PLG (0.83), SERPINF1 (0.81); STRING partners: APOE (0.989), PLG (0.995), SERPINF1 (0.828)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vitronectin. The protein encoded by this gene functions in part as an adhesive glycoprotein. Differential expression of this protein can promote either cell adhesion or migration as it links cells to the extracellular matrix through a variety of ligands. These ligands include integrins, plasminogen activator inhibitor-1, and urokinase plasminogen activator receptor. This secreted protein can be present in the …
- **Diseases (Open Targets)**: hypertensive disorder (0.421); dengue disease (0.376); neurodegenerative disease (0.343); temporal arteritis (0.338); age-related macular degeneration (0.313)
- **Europe PMC papers**: 3940
- **Why important**: VTN occupies a bridging position between PLG and SERPINF1 and has strong STRING links to APOE, PLG, and SERPINF1. Its annotated function as a secreted adhesive glycoprotein connects integrins, plasminogen-activator biology, cell adhesion, migration, and extracellular matrix. VTN contributes to the primary coagulation and wound-response terms (26 globally significant GO/KEGG terms, q_global 0.000456–0.043; see the table) and to the STRING extracellular-matrix and blood-microparticle findings (4 supplementary STRING terms; within-query FDR 6.57e-06–0.00024).
- **Conclusion**: Established evidence supports VTN as the module component that links circulating protease regulation to extracellular-matrix adhesion and cell migration. A local role in cervix or colon remodeling is a plausible hypothesis, but HPA instead indicates liver enrichment, secretion to blood, and no protein detection in the sampled tissues.

#### SERPINF1

- **Related proteins** (co-abundance neighbors): VTN (0.81); STRING partners: F2 (0.804), PLG (0.995), VTN (0.828)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family F member 1. This gene encodes a member of the serpin family that does not display the serine protease inhibitory activity shown by many of the other serpin proteins. The encoded protein is secreted and strongly inhibits angiogenesis. In addition, this protein is a neurotrophic factor involved in neuronal differentiation in retinoblastoma cells. Mutations in this gene were found in individuals with osteogenesi…
- **Diseases (Open Targets)**: osteogenesis imperfecta (0.716); osteogenesis imperfecta, recessive (0.462); osteogenesis imperfecta type 3 (0.447); osteogenesis imperfecta type 4 (0.371); refractive error (0.348)
- **Europe PMC papers**: 2744
- **Why important**: SERPINF1 is linked to VTN in the module graph and has strong STRING associations with PLG and additional support with F2 (STRING Component Collagen-containing extracellular matrix; within-query FDR = 6.57e-06), (STRING Keyword Secreted; within-query FDR = 0.00017), and (5 supplementary STRING terms; within-query FDR 0.00093–0.00093). Its secreted protein is described as a strong inhibitor of angiogenesis and a regulator of endothelial-cell migration, while its disease associations include osteogenesis imperfecta. It contributes to the primary negative-regulation-of-multicellular-process evidence (GO:BP negative regulation of multicellular organismal process; q_global = 0.0223) and helps extend the module beyond clotting toward vascular remodeling and repair.
- **Conclusion**: Established evidence supports SERPINF1 as an extracellular anti-angiogenic and migration-regulatory component that may modulate the coagulation and matrix environment. The proposed contribution to cervix or colon vascular remodeling remains hypothetical because its HPA associations emphasize choroid plexus and decidual stromal or retinal pigment epithelial cells rather than protein detection in the sampled tissues.

#### APOE

- **Related proteins** (co-abundance neighbors): A1BG (0.81); STRING partners: VTN (0.989)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein E. The protein encoded by this gene is a major apoprotein of the chylomicron. It binds to a specific liver and peripheral cell receptor, and is essential for the normal catabolism of triglyceride-rich lipoprotein constituents. This gene maps to chromosome 19 in a cluster with the related apolipoprotein C1 and C2 genes. Mutations in this gene result in familial dysbetalipoproteinemia, or type III hype…
- **Diseases (Open Targets)**: hyperlipoproteinemia type 3 (0.803); coronary artery disorder (0.782); lipoprotein glomerulopathy (0.759); Alzheimer disease (0.696); familial hypercholesterolemia (0.651)
- **Europe PMC papers**: 74272
- **Why important**: APOE contributes to the primary coagulation, hemostasis, wound-response, body-fluid, and heparin-binding evidence (6 globally significant GO/KEGG terms, q_global 0.000456–0.00078; see the table), (GO:BP negative regulation of response to wounding; q_global = 0.00178) (GO:BP regulation of wound healing; q_global = 0.00252) (GO:BP regulation of response to wounding; q_global = 0.00349), and (7 globally significant GO/KEGG terms, q_global 0.0165–0.043; see the table). It connects to VTN in STRING and is associated with lipid transport, receptor-mediated endocytosis, and regulation of endothelial proliferation. Its disease associations include type three hyperlipoproteinemia, coronary artery disease, lipoprotein glomerulopathy, Alzheimer disease, and familial hypercholesterolemia, with extensive literature support.
- **Conclusion**: Established evidence supports APOE as a circulating lipid-transport and extracellular regulatory component that may connect vascular biology with coagulation and repair. Its presence does not demonstrate a tissue-local APOE mechanism in cervix or colon, since HPA describes tissue-enhanced expression across adrenal gland, brain, and liver, secretion to blood, and no protein detection in the sampled tissues.

## Module 3

**Tissue pair**: cervix_uterine and colon  
**Genes (31)**: ABCD3, ADIRF, ALDH1A3, ACTR10, BAIAP2, CD5L, CLIP1, CYFIP1, DYNC1I2, DIAPH1, ITPRID2, TMPO, TMPO, LRRFIP2, MYO5B, MYO6, PPL, JUP, PPM1A, MRPL13, ROCK1, RUVBL2, SPTBN1, CCT5, CCT3, CCT7, CCT8, TGM1, TNFAIP2, UTRN, VSNL1

### Function

The strongest interpretation is a protein-folding and nuclear RNA-localization module centered on the CCT chaperonin complex. The CCT subunits CCT3, CCT5, CCT7 and CCT8 support the globally corrected enrichment for ATP-dependent protein folding, the chaperonin-containing T-complex, protein localization to the Cajal body and nucleus, and telomerase RNA localization and telomere maintenance (13 globally significant GO/KEGG terms, q_global 1.03e-05–0.00122; see the table), (4 globally significant GO/KEGG terms, q_global 0.00494–0.00855; see the table), (GO:BP positive regulation of telomere maintenance; q_global = 0.0186), (GO:BP regulation of telomere maintenance via telomere lengthening; q_global = 0.02), (GO:BP regulation of telomere maintenance; q_global = 0.0333), (4 globally significant GO/KEGG terms, q_global 0.0384–0.0466; see the table). RUVBL2 extends this core toward telomere maintenance, RNA localization and nuclear processes (4 globally significant GO/KEGG terms, q_global 1.03e-05–1.03e-05; see the table), (GO:CC protein folding chaperone complex; q_global = 0.00122), (GO:BP positive regulation of telomere maintenance; q_global = 0.0186), (GO:BP regulation of telomere maintenance; q_global = 0.0333), (GO:MF unfolded protein binding; q_global = 0.0466). A second coherent aspect is epithelial and cytoskeletal organization: many module genes occur in the globally corrected cytoskeleton and supramolecular fiber terms (GO:CC polymeric cytoskeletal fiber; q_global = 0.0103) (GO:CC supramolecular polymer; q_global = 0.0132) (GO:CC supramolecular fiber; q_global = 0.0132), (GO:CC cytoskeleton; q_global = 0.0286), (GO:BP positive regulation of protein localization; q_global = 0.038). Thus, the module is best viewed as a conserved cellular proteostasis and nuclear-RNA module embedded in an epithelial cytoskeletal context, rather than as a single narrowly defined pathway. The sperm-recognition and zona-pellucida terms (GO:BP binding of sperm to zona pellucida; q_global = 0.00252), (GO:BP sperm-egg recognition; q_global = 0.00855), (GO:BP cell-cell recognition; q_global = 0.02) should be interpreted cautiously because they are driven by the same CCT genes and may reflect annotation overlap rather than a reproductive function in cervix or colon.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins. HPA identifies only CD5L as secreted to blood, while most genes are intracellular, membrane-associated, cytoskeletal, nuclear, or broadly expressed. The HPA profile is mixed: many genes have low tissue specificity, while several are enhanced in epithelial populations such as esophageal apical or suprabasal cells, urothelial cells, and related epithelial states. The presence of PPL, JUP, TGM1, MYO5B, BAIAP2 and other structural genes is compatible with epithelial architecture, junctions, membrane trafficking and cytoskeletal organization. There is some immune or blood-cell enrichment, including monocyte, neutrophil, dendritic-cell and lymphocyte categories, but the overall profile does not support a predominantly blood-cell module. CD5L is an important exception because it is secreted and associated with lymphoid, Hofbauer and Kupffer cell contexts; its inclusion could reflect a minor immune or extracellular component, sample composition, or a shared cellular state. Protein detection is broadly supported in both tissues for most annotated genes, although TGM1, PPL, ADIRF, ITPRID2 and RUVBL2 show tissue-specific detection differences that caution against assuming identical cellular origins in cervix and colon.

**GO/KEGG enrichment**: 32 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP RNA localization to Cajal body | 1.03e-05 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP telomerase RNA localization to Cajal body | 1.03e-05 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP telomerase RNA localization | 1.03e-05 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP RNA localization to nucleus | 1.03e-05 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:CC chaperonin-containing T-complex | 0.000303 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 0.000303 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 0.000303 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 0.000303 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 0.000303 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 0.000303 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 0.000303 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 0.000303 | CCT3, CCT5, CCT7, CCT8 |
| GO:CC protein folding chaperone complex | 0.00122 | CCT3, CCT5, CCT7, CCT8, RUVBL2 |
| GO:BP binding of sperm to zona pellucida | 0.00252 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 0.00494 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING shows a well-supported known interaction core among CCT3, CCT5, CCT7 and CCT8, with additional links from these subunits to RUVBL2 (7 supplementary STRING terms; within-query FDR 0.00097–0.0026), (7 supplementary STRING terms; within-query FDR 0.0047–0.0048). STRING also supports cytoskeletal or junction-related relationships involving ACTR10-DYNC1I2, BAIAP2-CYFIP1, JUP-PPL and PPL-TGM1 (STRING Component Cytoskeleton; within-query FDR = 0.0029). The STRING functional results independently reinforce the CCT chaperonin, telomerase-RNA-localization and cytoskeletal interpretations, but they are supplementary evidence rather than global enrichment significance. hu.MAP repeatedly places the four CCT subunits together in chaperonin-containing complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). This is strong evidence that the central CCT signal represents a known physical or complex-level biology rather than an arbitrary co-abundance pattern. hu.MAP also connects PPL, JUP and TGM1 in epithelial structural complexes (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1) (hu.MAP huMAP3_09598.1) (hu.MAP huMAP3_05845.1) (hu.MAP huMAP3_08595.1), and connects BAIAP2 with CYFIP1 in actin-regulatory complexes (hu.MAP huMAP3_09598.1), (hu.MAP huMAP3_13345.1). The remaining module edges have limited direct support in STRING or hu.MAP, so co-abundance should not be interpreted as proof of physical interaction for every gene pair.

**STRING interactions (score >= 0.7)**: 14 of 465 gene pairs: ACTR10–DYNC1I2 (0.97); BAIAP2–CYFIP1 (0.945); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT3–RUVBL2 (0.766); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT5–RUVBL2 (0.705); CCT7–CCT8 (0.999); CCT7–RUVBL2 (0.802); CCT8–RUVBL2 (0.776); JUP–PPL (0.779); PPL–TGM1 (0.84)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam TCP-1/cpn60 chaperonin family (FDR = 0.00097, 4 genes); Process Positive regulation of telomerase RNA localization to Cajal body (FDR = 0.001, 5 genes); NetworkNeighborAL Chaperone complex, and Prefoldin (FDR = 0.002, 5 genes); Component Chaperonin-containing T-complex (FDR = 0.0024, 4 genes); Component Chaperone complex (FDR = 0.0024, 5 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 0.0026, 4 genes); COMPARTMENTS Chaperone complex (FDR = 0.0026, 5 genes); Component Cytoskeleton (FDR = 0.0029, 17 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis (FDR = 0.0047, 4 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 0.0048, 4 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 0.0048, 4 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 0.0048, 4 genes); InterPro GroEL-like apical domain superfamily (FDR = 0.0048, 4 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 0.0048, 4 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 0.0048, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_09125.1 (PPL, JUP, TGM1; 3/53); huMAP3_09929.1 (PPL, JUP, TGM1; 3/75); huMAP3_09598.1 (CYFIP1, BAIAP2; 2/23); huMAP3_05845.1 (JUP, TGM1; 2/24); huMAP3_08595.1 (JUP, TGM1; 2/25); huMAP3_13345.1 (CYFIP1, BAIAP2; 2/35); huMAP3_09542.1 (ITPRID2, LRRFIP2; 2/38)

### Novelty

The individual biological components are not novel: the CCT complex, its chaperone function, the association of RUVBL2 with nuclear and telomere-related processes, and epithelial junction or cytoskeletal complexes are already represented in STRING, hu.MAP and established annotations. The conserved co-abundance module across cervix and colon may nevertheless be a new systems-level observation, because the fact sheet does not establish that this exact tissue-pair module, including its combination of CCT, epithelial structural and trafficking genes, has previously been reported. However, absence of a complete match in STRING or hu.MAP would not prove novelty, since those resources capture physical interactions or curated complexes rather than tissue-specific co-abundance modules. The most defensible conclusion is therefore partial novelty: the module-level cross-tissue co-abundance pattern may be novel, whereas its central molecular mechanisms are largely established.

**Hypothesis.** Hypothesis: a shared epithelial cellular state in cervix and colon increases demand for CCT-dependent folding of cytoskeletal and membrane-associated proteins while coordinating nuclear RNA handling and telomerase-related processes. The CCT subunits and RUVBL2 could form the proteostasis and nuclear-RNA core, whereas TGM1, PPL, JUP, MYO5B, BAIAP2 and related genes could reflect epithelial barrier structure, junctional organization and vesicle or cytoskeletal remodeling. CD5L and the immune-enhanced genes may indicate a secondary contribution from local immune or myeloid cells, or secretion-related contamination, rather than belonging to the same physical complex. This hypothesis predicts that the module will track epithelial integrity, proliferative or repair states, and cellular stress more consistently than a tissue-specific secreted or blood-derived program. It requires validation with cell-resolved expression, perturbation of CCT or RUVBL2, and independent protein-level measurements.

### Important genes

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT8 (0.87), CCT5 (0.85), CCT7 (0.81); STRING partners: CCT5 (0.999), CCT7 (0.999), CCT8 (0.999), RUVBL2 (0.766)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a central member of the CCT chaperonin core and is connected in STRING to CCT5, CCT7, CCT8 and RUVBL2. It appears in every globally corrected enrichment term in the fact sheet, spanning chaperone activity, protein folding, Cajal-body localization, telomerase RNA localization, telomere maintenance and cytoskeletal annotations (32 globally significant GO/KEGG terms, q_global 1.03e-05–0.0466; see the table). It is detected in both tissues and has substantial literature and disease-association coverage, making it a strong anchor for the module's established biology.
- **Conclusion**: Established evidence supports CCT3 as a core protein-folding subunit and a principal driver of the module's enrichment. Its direct role in this specific cervix-colon co-abundance pattern, and whether it mediates telomerase-related effects in these tissues, remains a hypothesis.

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT3 (0.85); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999), RUVBL2 (0.705)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is part of the same highly supported CCT interaction core as CCT3, CCT7 and CCT8, and it occurs in the full set of globally corrected terms (32 globally significant GO/KEGG terms, q_global 1.03e-05–0.0466; see the table). Its known chaperone role includes folding actin and tubulin, providing a mechanistic bridge between the nuclear or proteostasis signal and the cytoskeletal signal. It also has a disease association with hereditary sensory and autonomic neuropathy and a substantial literature base.
- **Conclusion**: Established evidence identifies CCT5 as a chaperonin subunit that can support folding of structural proteins. A specific role for CCT5 in maintaining epithelial architecture or telomerase RNA handling in the two tissues is plausible but not demonstrated by this module alone.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): TGM1 (0.80); STRING partners: CCT3 (0.766), CCT5 (0.705), CCT7 (0.802), CCT8 (0.776)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 links the CCT core to the globally corrected terms for RNA localization to the Cajal body, telomerase RNA localization, telomere maintenance, RNA-templated DNA synthesis and unfolded-protein binding (4 globally significant GO/KEGG terms, q_global 1.03e-05–1.03e-05; see the table), (GO:CC protein folding chaperone complex; q_global = 0.00122), (GO:BP positive regulation of telomere maintenance; q_global = 0.0186), (GO:BP regulation of telomere maintenance; q_global = 0.0333), (GO:BP RNA-templated DNA biosynthetic process; q_global = 0.0384), (GO:BP telomere maintenance via telomerase; q_global = 0.0384), (GO:MF unfolded protein binding; q_global = 0.0466). It has STRING connections to all four CCT subunits and is described as an ATPase and DNA helicase involved in DNA repair, recombination and telomere-related processes. Its nuclear and cytosolic localization makes it a biologically credible bridge between proteostasis and nuclear maintenance.
- **Conclusion**: Established evidence supports RUVBL2 as a nuclear ATPase with roles in DNA and telomere biology and as a known partner of the CCT-associated module. Whether it functionally couples CCT activity to telomerase RNA localization in cervix or colon is an untested mechanistic hypothesis.

#### TGM1

- **Related proteins** (co-abundance neighbors): BAIAP2 (0.99), TMPO (0.96), ALDH1A3 (0.92), MYO5B (0.92), MYO6 (0.92), MRPL13 (0.90), ABCD3 (0.89), ITPRID2 (0.88), DIAPH1 (0.88), TNFAIP2 (0.88), PPL (0.87), CCT7 (0.87), ADIRF (0.85), CYFIP1 (0.83), JUP (0.81), VSNL1 (0.81), SPTBN1 (0.81), RUVBL2 (0.80), PPM1A (0.80), ROCK1 (0.80); STRING partners: PPL (0.84)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles, Plasma membrane; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1, huMAP3_05845.1, huMAP3_08595.1
- **Function (MyGene.info)**: transglutaminase 1. The protein encoded by this gene is a membrane protein that catalyzes the addition of an alkyl group from an akylamine to a glutamine residue of a protein, forming an alkylglutamine in the protein. This protein alkylation leads to crosslinking of proteins and catenation of polyamines to proteins. This gene contains either one or two copies of a 22 nt repeat unit in its 3' UTR. Mutations in this ge…
- **Diseases (Open Targets)**: lamellar ichthyosis (0.721); autosomal recessive congenital ichthyosis (0.714); congenital reticular ichthyosiform erythroderma (0.504); Abnormality of the skin (0.482); ichthyosis (0.456)
- **Europe PMC papers**: 2060
- **Why important**: TGM1 has the highest weighted network position in the supplied module and connects to a broad set of epithelial, trafficking, mitochondrial, cytoskeletal and signaling genes. It is tissue-enriched in esophagus, detected in cervix, localized to vesicles and plasma membrane, and associated with keratinocyte differentiation, cell-envelope organization and lamellar ichthyosis. Its STRING connection to PPL and its relationship to epithelial structural biology make it a useful candidate for the non-chaperone arm of the module.
- **Conclusion**: Established evidence supports TGM1 as a membrane-associated transglutaminase involved in epithelial differentiation and protein crosslinking. Its strong co-abundance connectivity may indicate epithelial structural state, but it is not itself part of the globally enriched CCT or telomerase terms, so a direct functional link to the CCT core remains unproven.

#### JUP

- **Related proteins** (co-abundance neighbors): TGM1 (0.81); STRING partners: PPL (0.779)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1, huMAP3_05845.1, huMAP3_08595.1
- **Function (MyGene.info)**: junction plakoglobin. This gene encodes a major cytoplasmic protein which is the only known constituent common to submembranous plaques of both desmosomes and intermediate junctions. This protein forms distinct complexes with cadherins and desmosomal cadherins and is a member of the catenin family since it contains a distinct repeating amino acid motif called the armadillo repeat. Mutation in this gene has been associa…
- **Diseases (Open Targets)**: Naxos disease (0.784); arrhythmogenic right ventricular dysplasia 12 (0.755); arrhythmogenic right ventricular cardiomyopathy (0.597); lethal acantholytic epidermolysis bullosa (0.383); familial isolated arrhythmogenic ventricular dysplasia, biventricular form (0.370)
- **Europe PMC papers**: 3429
- **Why important**: JUP is a desmosomal and intermediate-junction component with roles in cell adhesion, migration, cell-matrix adhesion and nuclear protein import. It contributes to the globally corrected cytoskeletal, supramolecular-fiber and protein-localization terms (GO:CC polymeric cytoskeletal fiber; q_global = 0.0103) (GO:CC supramolecular polymer; q_global = 0.0132) (GO:CC supramolecular fiber; q_global = 0.0132), (GO:BP positive regulation of protein localization to nucleus; q_global = 0.0277), (GO:CC cytoskeleton; q_global = 0.0286), (GO:BP positive regulation of protein localization; q_global = 0.038), and it participates with PPL and TGM1 in hu.MAP epithelial complexes (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1) (hu.MAP huMAP3_09598.1) (hu.MAP huMAP3_05845.1) (hu.MAP huMAP3_08595.1). Its established disease associations with Naxos disease and arrhythmogenic cardiomyopathy reinforce its importance for junctional integrity.
- **Conclusion**: Established evidence supports JUP as an epithelial junction and cytoskeletal scaffold. Within this module, JUP most likely reports epithelial structural organization rather than the CCT-centered nuclear function; any regulatory connection between JUP and telomerase-related activity is speculative.

## Module 4

**Tissue pair**: cervix_uterine and colon  
**Genes (28)**: ABCF1, PRMT5, CAPRIN1, CLUH, DDX46, EIF3C, FKBP4, FXR1, EIF4G1, IPO4, MCM2, MCM4, MCM5, MCM7, MSH2, MSH6, NAA15, NSUN2, NUP155, PSMC4, UPF1, PSAT1, SMC2, LARS1, TARS1, YARS1, TNPO3, XPO1

### Function

The strongest interpretation is a conserved nuclear nucleic-acid metabolism module centered on DNA replication initiation, replication-fork activity, and genome maintenance. The primary evidence is the globally corrected enrichment for nucleic-acid binding and catalytic activity on nucleic acids (GO:MF nucleic acid binding; q_global = 8.66e-05)(GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.000118), together with the MCM-complex, CMG-complex, and DNA-replication preinitiation-complex terms (GO:CC DNA replication preinitiation complex; q_global = 0.000863)(GO:CC MCM complex; q_global = 0.000863)(GO:CC CMG complex; q_global = 0.000863). The MCM2, MCM4, MCM5, and MCM7 quartet provides a particularly coherent replication core, supported by globally corrected helicase, ATP-dependent DNA activity, replication-initiation, and break-induced-replication terms (GO:MF ATP-dependent activity, acting on DNA; q_global = 0.000965)(GO:MF double-stranded DNA helicase activity; q_global = 0.00139)(GO:BP double-strand break repair via break-induced replication; q_global = 0.002)(GO:BP regulation of DNA-templated DNA replication initiation; q_global = 0.00393)(GO:BP regulation of DNA-templated DNA replication; q_global = 0.0068)(GO:MF DNA helicase activity; q_global = 0.0172)(GO:BP DNA replication initiation; q_global = 0.0308)(GO:MF helicase activity; q_global = 0.0399). MSH2 and MSH6 add mismatch-recognition and DNA-repair biology, while SMC2 is consistent with chromosome organization. A second layer involves RNA handling and translation: EIF4G1, EIF3C, UPF1, DDX46, CAPRIN1, FXR1, PRMT5, XPO1, and the aminoacyl-tRNA synthetases connect translation, RNA processing, transport, and surveillance to the replication-associated core. The globally corrected terms establish a broad nucleic-acid and ATP-dependent molecular signature; the more specific RNA-transport interpretation is supplementary because it comes from STRING (STRING KEGG RNA transport; within-query FDR = 0.0016).

**Cell composition.** This does not resemble a module dominated by plasma or secreted proteins. The HPA summary identifies only a single secreted gene, while nearly all module proteins are detected in both cervix and colon and are intracellular or nuclear. Most genes have low tissue specificity, so the shared signal is compatible with broadly used cellular machinery rather than a tissue-exclusive program. At the same time, many genes are cell-type enhanced, especially in erythrocyte progenitors, megakaryocyte progenitors, spermatogenic cells, and trophoblast-related cells, and several are tissue enhanced in bone marrow or lymphoid tissue. Blood-cell specificity is generally low, with only limited immune-cell enrichment, so the data do not strongly support a plasma or immune infiltrate explanation. Nevertheless, the bone-marrow and erythroid-progenitor patterns mean that cellular composition and proliferative state should be considered as possible contributors to the shared cervix-colon co-abundance. The lack of HPA detection for NUP155 and PSAT1 in the examined tissues also argues against treating every module member as uniformly expressed.

**GO/KEGG enrichment**: 37 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleic acid binding | 8.66e-05 | ABCF1, CAPRIN1, CLUH, DDX46, EIF3C, EIF4G1, FKBP4, FXR1, MCM2, MCM4, MCM5, MCM7, MSH2, MSH6, NAA15, NSUN2, PRMT5, SMC2, TARS1, UPF1, XPO1, YARS1 |
| GO:MF catalytic activity, acting on a nucleic acid | 0.000118 | DDX46, FXR1, LARS1, MCM2, MCM4, MCM5, MCM7, MSH2, MSH6, NSUN2, TARS1, UPF1, YARS1 |
| GO:CC DNA replication preinitiation complex | 0.000863 | MCM2, MCM4, MCM5, MCM7 |
| GO:CC MCM complex | 0.000863 | MCM2, MCM4, MCM5, MCM7 |
| GO:CC CMG complex | 0.000863 | MCM2, MCM4, MCM5, MCM7 |
| GO:MF ATP-dependent activity, acting on DNA | 0.000965 | MCM2, MCM4, MCM5, MCM7, MSH2, MSH6, UPF1 |
| GO:MF double-stranded DNA helicase activity | 0.00139 | MCM2, MCM4, MCM5, MCM7, UPF1 |
| GO:MF ATP binding | 0.00193 | ABCF1, CAPRIN1, DDX46, EIF4G1, FKBP4, LARS1, MCM2, MCM4, MCM5, MCM7, MSH2, MSH6, PSMC4, SMC2, TARS1, UPF1, YARS1 |
| GO:MF ATP hydrolysis activity | 0.00197 | ABCF1, DDX46, MCM2, MCM4, MCM5, MCM7, MSH2, PSMC4, SMC2, UPF1 |
| GO:MF adenyl ribonucleotide binding | 0.002 | ABCF1, CAPRIN1, DDX46, EIF4G1, FKBP4, LARS1, MCM2, MCM4, MCM5, MCM7, MSH2, MSH6, PSMC4, SMC2, TARS1, UPF1, YARS1 |
| GO:BP double-strand break repair via break-induced replication | 0.002 | MCM2, MCM4, MCM5, MCM7 |
| GO:MF single-stranded DNA binding | 0.00226 | MCM2, MCM4, MCM5, MCM7, MSH2, SMC2 |
| GO:MF ATP-dependent activity | 0.00315 | ABCF1, DDX46, MCM2, MCM4, MCM5, MCM7, MSH2, MSH6, PSMC4, SMC2, UPF1 |
| GO:BP regulation of DNA-templated DNA replication initiation | 0.00393 | MCM2, MCM4, MCM5, MCM7 |
| GO:MF nucleic acid conformation isomerase activity | 0.00507 | DDX46, FXR1, MCM2, MCM4, MCM5, MCM7, UPF1 |

### STRING and hu.MAP

STRING independently recapitulates the module's two principal structures. The MCM2-MCM4-MCM5-MCM7 relationships are very strong, and MSH2-MSH6 is a known mismatch-repair pair; additional links connect MCM proteins with MSH6 and SMC2 (STRING Pfam MCM N-terminal domain; within-query FDR = 0.00073)(STRING Function DNA helicase activity; within-query FDR = 0.0011)(STRING Function Single-stranded DNA binding; within-query FDR = 0.002)(STRING Component Chromosome, telomeric region; within-query FDR = 0.0041)(STRING Component MCM complex; within-query FDR = 0.0041). A separate translation and RNA-control structure is supported by EIF3C-EIF4G1, EIF4G1-UPF1, EIF4G1-FXR1, CAPRIN1-FXR1, and CAPRIN1-UPF1, while LARS1, TARS1, and YARS1 form a recognizable aminoacyl-tRNA-synthetase neighborhood. Nuclear transport links include XPO1 with NUP155, IPO4, and TNPO3. These are known relationships rather than newly demonstrated physical interactions in this tissue pair. hu.MAP provides especially strong complex-level support for the MCM quartet: MCM2, MCM4, MCM5, and MCM7 recur together in several replication-related complexes (hu.MAP huMAP3_05529.1)(hu.MAP huMAP3_14758.1)(hu.MAP huMAP3_08554.1)(hu.MAP huMAP3_11832.1)(hu.MAP huMAP3_12180.1). hu.MAP also supports the EIF3C-EIF4G1 complex, the LARS1-TARS1 group, the PRMT5-DDX46 spliceosomal context, and transport-associated XPO1-MSH6 contexts (hu.MAP huMAP3_08764.1)(hu.MAP huMAP3_02637.1)(hu.MAP huMAP3_13175.1)(hu.MAP huMAP3_06511.1). Thus, the network is not merely an arbitrary co-abundance cluster: substantial portions map onto established protein complexes, although the tissue-level co-abundance links between these complexes may reflect shared cellular state rather than one physical complex.

**STRING interactions (score >= 0.7)**: 25 of 378 gene pairs: CAPRIN1–EIF4G1 (0.758); CAPRIN1–FXR1 (0.891); CAPRIN1–UPF1 (0.72); EIF3C–EIF4G1 (0.99); EIF4G1–FXR1 (0.83); EIF4G1–UPF1 (0.974); IPO4–XPO1 (0.714); LARS1–TARS1 (0.98); LARS1–YARS1 (0.98); MCM2–MCM4 (0.999); MCM2–MCM5 (0.999); MCM2–MCM7 (0.999); MCM4–MCM5 (0.999); MCM4–MCM7 (0.999); MCM4–MSH6 (0.735); MCM4–SMC2 (0.748); MCM5–MCM7 (0.999); MCM5–MSH6 (0.749); MCM5–SMC2 (0.754); MCM7–MSH2 (0.71); MCM7–SMC2 (0.7); MSH2–MSH6 (0.999); NUP155–XPO1 (0.769); TARS1–YARS1 (0.911); TNPO3–XPO1 (0.764)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Nucleic acid binding (FDR = 3.68e-05, 22 genes); Function Catalytic activity, acting on a nucleic acid (FDR = 7.12e-05, 12 genes); Function ATP-dependent activity, acting on DNA (FDR = 0.00014, 7 genes); Pfam MCM N-terminal domain (FDR = 0.00073, 4 genes); Function ATP hydrolysis activity (FDR = 0.00098, 9 genes); Function DNA helicase activity (FDR = 0.0011, 5 genes); Function ATP binding (FDR = 0.0011, 16 genes); Function Organic cyclic compound binding (FDR = 0.0011, 25 genes); Function ATP-dependent activity (FDR = 0.0011, 10 genes); Function Heterocyclic compound binding (FDR = 0.0011, 25 genes); KEGG RNA transport (FDR = 0.0016, 7 genes); Function Single-stranded DNA binding (FDR = 0.002, 5 genes); Function Helicase activity (FDR = 0.002, 6 genes); Component Chromosome, telomeric region (FDR = 0.0041, 6 genes); Component MCM complex (FDR = 0.0041, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05529.1 (MCM4, MCM5, MCM7, MCM2; 4/6); huMAP3_14758.1 (MCM4, MCM5, MCM7, MCM2; 4/14); huMAP3_08554.1 (MCM4, MCM5, MCM7, MCM2; 4/15); huMAP3_11832.1 (MCM4, MCM5, MCM7, MCM2; 4/15); huMAP3_12180.1 (MCM4, MCM5, MCM7, MCM2; 4/17); huMAP3_06061.1 (MCM4, MCM7, MCM2; 3/5); huMAP3_07113.1 (MCM4, MCM7, MCM2; 3/6); huMAP3_11119.1 (MCM4, MCM5, MCM7; 3/14); huMAP3_09860.1 (MCM4, MCM2; 2/4); huMAP3_00154.1 (MCM4, MCM2; 2/5); huMAP3_08764.1 (XPO1, MSH6; 2/7); huMAP3_09238.1 (MCM5, MCM7; 2/11); huMAP3_07170.1 (XPO1, MSH6; 2/14); huMAP3_02637.1 (TARS1, LARS1; 2/14); huMAP3_13688.1 (TARS1, LARS1; 2/14); huMAP3_13175.1 (EIF4G1, EIF3C; 2/20); huMAP3_09466.1 (MCM4, MCM2; 2/23); huMAP3_11246.1 (EIF4G1, EIF3C; 2/24); huMAP3_10747.1 (MCM2, IPO4; 2/25); huMAP3_09042.1 (XPO1, MSH6; 2/26); huMAP3_10862.1 (MCM4, MCM2; 2/33); huMAP3_14270.1 (CAPRIN1, ABCF1; 2/47); huMAP3_14306.1 (MCM4, MCM2; 2/55); huMAP3_06511.1 (PRMT5, DDX46; 2/79); huMAP3_08980.1 (PRMT5, DDX46; 2/97)

### Novelty

The module should not be described as a newly discovered molecular complex or as proof of a novel protein interaction. The replication core, mismatch-repair pair, translation-initiation links, aminoacyl-tRNA-synthetase links, and nuclear-transport relationships are already represented in STRING and hu.MAP. The potentially novel aspect is the reproducible co-abundance of these established functional neighborhoods across cervix and colon, especially the coupling of replication, RNA handling, translation, and genome surveillance in this tissue pair. That observation is hypothesis-generating rather than proof of a new mechanism. Absence of hu.MAP or STRING support for genes such as NAA15, UPF1, DDX46, NSUN2, or CLUH does not establish novelty, because database coverage, context specificity, and assay limitations can explain missing relationships. Establishing novelty would require comparison with existing cross-tissue module studies and independent replication in additional cohorts.

**Hypothesis.** Hypothesis: the conserved module reflects a shared epithelial or proliferative cellular state in which DNA replication licensing and fork activity are coordinated with RNA maturation, translation initiation, nuclear transport, and RNA surveillance. The MCM core may mark replication competence, MSH2-MSH6 and SMC2 may support genome integrity and chromosome organization, and the EIF4G1-UPF1-DDX46-CAPRIN1/FXR1 neighborhood may coordinate the production, export, translation, and quality control of transcripts needed during that state. HPA patterns suggest that variation in proliferating or progenitor-like cell content could generate part of the shared signal. This is a mechanistic model, not an experimentally established causal pathway; it should be tested with cell-resolved expression, replication-state markers, perturbation of MCM or mismatch-repair components, and measurement of RNA processing and translation.

### Important genes

#### MCM2

- **Related proteins** (co-abundance neighbors): MCM7 (0.91), MSH6 (0.83), NUP155 (0.82), MCM5 (0.82), EIF4G1 (0.81), MCM4 (0.81); STRING partners: MCM4 (0.999), MCM5 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10747.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a high-connectivity module member and links directly to the MCM quartet, MSH6, NUP155, and EIF4G1. It appears in all globally corrected terms, including the MCM, CMG, replication-initiation, helicase, and DNA-repair signatures (GO:CC DNA replication preinitiation complex; q_global = 0.000863)(GO:CC MCM complex; q_global = 0.000863)(GO:CC CMG complex; q_global = 0.000863)(GO:MF double-stranded DNA helicase activity; q_global = 0.00139)(GO:BP double-strand break repair via break-induced replication; q_global = 0.002)(GO:BP regulation of DNA-templated DNA replication initiation; q_global = 0.00393)(GO:BP DNA replication initiation; q_global = 0.0308). STRING and hu.MAP independently place it in established replication complexes. Its annotation identifies it as a core component of replication licensing and fork formation, and its disease associations include gastrointestinal abnormalities and inherited hearing disorders. Its extensive literature support makes it a strong anchor for interpreting the module.
- **Conclusion**: Established evidence supports MCM2 as a central replication-licensing component and a major structural anchor of this module. The hypothesis that its co-abundance specifically reports proliferative activity in both tissues remains to be tested against cell composition and direct proliferation measurements.

#### MCM4

- **Related proteins** (co-abundance neighbors): MCM7 (0.89), MCM5 (0.85), MCM2 (0.81); STRING partners: MCM2 (0.999), MCM5 (0.999), MCM7 (0.999), MSH6 (0.735), SMC2 (0.748)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 4. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication rel…
- **Diseases (Open Targets)**: primary immunodeficiency with natural-killer cell deficiency and adrenal insufficiency (0.714); X-linked adrenal hypoplasia congenita (0.185); lung adenocarcinoma (0.112); microcephaly (0.111); neoplasm (0.102)
- **Europe PMC papers**: 4082
- **Why important**: MCM4 is part of the complete MCM2-MCM4-MCM5-MCM7 replication core, has direct strong STRING links to the other MCM members, and recurs across multiple hu.MAP replication complexes (hu.MAP huMAP3_05529.1)(hu.MAP huMAP3_14758.1)(hu.MAP huMAP3_08554.1)(hu.MAP huMAP3_11832.1)(hu.MAP huMAP3_12180.1). It contributes to every globally corrected MCM, helicase, replication-initiation, and DNA-repair term (GO:CC DNA replication preinitiation complex; q_global = 0.000863)(GO:CC MCM complex; q_global = 0.000863)(GO:CC CMG complex; q_global = 0.000863)(GO:MF double-stranded DNA helicase activity; q_global = 0.00139)(GO:BP double-strand break repair via break-induced replication; q_global = 0.002)(GO:BP regulation of DNA-templated DNA replication initiation; q_global = 0.00393)(GO:BP DNA replication initiation; q_global = 0.0308). Its established roles in DNA replication and fork-associated processes, together with associations with adrenal insufficiency, primary immunodeficiency, microcephaly, and neoplastic disease, make it biologically informative despite its lower network connectivity than MCM2.
- **Conclusion**: Established evidence supports MCM4 as an essential member of the replication helicase core and a direct explanation for the module's most specific enrichment. Its presence does not by itself show replication stress or disease activity in the tissues.

#### MSH2

- **Related proteins** (co-abundance neighbors): MSH6 (0.81); STRING partners: MCM7 (0.71), MSH6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutS homolog 2. This locus is frequently mutated in hereditary nonpolyposis colon cancer (HNPCC). When cloned, it was discovered to be a human homolog of the E. coli mismatch repair gene mutS, consistent with the characteristic alterations in microsatellite sequences (RER+ phenotype) found in HNPCC. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: Lynch syndrome (0.891); colorectal cancer (0.776); mismatch repair cancer syndrome (0.775); Muir-Torre syndrome (0.752); mismatch repair cancer syndrome 1 (0.740)
- **Europe PMC papers**: 22581
- **Why important**: MSH2 connects the replication-associated part of the module to mismatch repair through its strong relationship with MSH6 and its additional STRING link to MCM7. It contributes to globally corrected nucleic-acid, ATP-dependent DNA, mismatch-relevant, and telomeric-region signatures (GO:MF nucleic acid binding; q_global = 8.66e-05)(GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.000118)(GO:MF ATP-dependent activity, acting on DNA; q_global = 0.000965)(GO:MF single-stranded DNA binding; q_global = 0.00226)(GO:MF catalytic activity, acting on DNA; q_global = 0.0083)(GO:CC chromosome, telomeric region; q_global = 0.0445). MSH2 is a recognized mismatch-repair protein with especially important disease associations involving Lynch syndrome, colorectal cancer, and mismatch-repair cancer syndromes. Its very extensive literature supports an established genome-maintenance role and gives the shared colon component particular clinical relevance.
- **Conclusion**: Established evidence supports MSH2 as a genome-surveillance and mismatch-repair component that complements the MCM replication core. It is reasonable to hypothesize coordinated replication and repair, but the co-abundance data do not demonstrate mismatch-repair activation or mutation burden.

#### EIF4G1

- **Related proteins** (co-abundance neighbors): NSUN2 (0.85), CLUH (0.83), DDX46 (0.83), MSH6 (0.82), MCM2 (0.81), UPF1 (0.81), NAA15 (0.80); STRING partners: CAPRIN1 (0.758), EIF3C (0.99), FXR1 (0.83), UPF1 (0.974)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: huMAP3_13175.1, huMAP3_11246.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 has the highest weighted connectivity in the module and bridges RNA and translation-related members with replication-associated genes, including NSUN2, CLUH, DDX46, MSH6, MCM2, UPF1, and NAA15. It is supported by STRING links to EIF3C, FXR1, UPF1, and CAPRIN1, and by hu.MAP translation-initiation complexes (hu.MAP huMAP3_13175.1)(hu.MAP huMAP3_11246.1). Its established function as the scaffolding component of the EIF4F complex places it at the interface of capped-mRNA recruitment, translation initiation, and ATP-dependent RNA unwinding. It also has a substantial literature base and disease associations involving Parkinson disease, neurodegeneration, dengue, and preeclampsia.
- **Conclusion**: Established evidence supports EIF4G1 as the principal translational bridge in the module. Its central network position supports coordination between translation and the replication-associated program, but does not prove that EIF4G1 drives the tissue-shared module.

#### UPF1

- **Related proteins** (co-abundance neighbors): DDX46 (0.82), LARS1 (0.82), NAA15 (0.82), EIF4G1 (0.81), PSMC4 (0.81), ABCF1 (0.80); STRING partners: CAPRIN1 (0.72), EIF4G1 (0.974)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UPF1 RNA helicase and ATPase. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons.…
- **Diseases (Open Targets)**: Intellectual disability (0.437); Global developmental delay (0.426); High anterior hairline (0.425); Frontal bossing (0.425); Hypertelorism (0.425)
- **Europe PMC papers**: 4252
- **Why important**: UPF1 is highly connected and links EIF4G1 and CAPRIN1 to DDX46, LARS1, NAA15, PSMC4, and ABCF1. It contributes broadly to the globally corrected nucleic-acid, ATP-dependent, helicase, and DNA-related terms (GO:MF nucleic acid binding; q_global = 8.66e-05)(GO:MF catalytic activity, acting on a nucleic acid; q_global = 0.000118)(GO:MF ATP-dependent activity, acting on DNA; q_global = 0.000965)(GO:MF double-stranded DNA helicase activity; q_global = 0.00139)(GO:MF ATP binding; q_global = 0.00193)(GO:MF nucleic acid conformation isomerase activity; q_global = 0.00507)(GO:MF DNA helicase activity; q_global = 0.0172)(GO:MF helicase activity; q_global = 0.0399). STRING supports its relationship with EIF4G1 and CAPRIN1, while its annotation establishes roles in RNA surveillance, nonsense-mediated decay, mRNA export, and RNA helicase or ATPase activity. Its disease associations include intellectual disability and developmental delay, and its literature support is substantial.
- **Conclusion**: Established evidence supports UPF1 as an RNA-quality-control and helicase component that connects the module's RNA and nucleic-acid functions. The proposed coordination of nonsense-mediated decay with replication-state regulation is a hypothesis requiring direct measurement of transcript quality and UPF1 activity.

## Module 5

**Tissue pair**: cervix_uterine and colon  
**Genes (30)**: ADK, ATP5F1C, CCDC43, CCDC6, CEACAM5, CTNNBIP1, GLUD1, DSG1, FAM120A, GFUS, FKBP15, FTL, GNAQ, GNS, HEBP2, HMOX2, KRT13, KRT17, MARCKS, MYO18A, MYH14, NSF, PSMC2, RUFY1, SARG, SERPINB3, CTTN, SYTL1, UEVLD, WASHC4

### Function

The strongest interpretation is an epithelial structural and adhesion module, centered on desmosomal and intermediate-filament biology, epithelial differentiation, and cell-surface organization. DSG1 is the dominant network hub and is a desmosomal cadherin involved in cell-cell adhesion. KRT13 and KRT17 support epithelial intermediate-filament structure and differentiation, while CEACAM5 and SARG provide cell-surface and epithelial-associated components. CTNNBIP1 adds a possible regulatory connection through negative regulation of Wnt signaling. These functional themes are biologically coherent with the tissue and single-cell expression profiles, but no GO/KEGG term passed global correction; therefore, the functional interpretation is based on gene annotations, HPA evidence, network organization, and complex membership rather than significant enrichment. The module also contains genes related to vesicle trafficking, actin organization, oxidative or metabolic stress, proteostasis, and intracellular transport, suggesting a broader epithelial maintenance state rather than a narrowly defined pathway.

**Cell composition.** The module is predominantly epithelial rather than plasma-protein or secreted-protein dominated. HPA profiles repeatedly point to esophageal apical or suprabasal cells, keratinocytes, colonocytes, goblet cells, respiratory basal cells, and other epithelial populations. Tissue enrichment in cervix, esophagus, skin, intestine, stomach, and related epithelial sites is consistent with a shared epithelial cell-state signal across cervix_uterine and colon. Only one module gene is annotated as secreted, while most are intracellular, membrane-associated, or structural. Several genes have low tissue or cell-type specificity, and some are enhanced in monocytes, neutrophils, basophils, or other immune-related populations, so a contribution from shared immune or stromal content cannot be excluded. The broad protein detection in both tissues supports biological detectability, but the different detection patterns for selected keratin and epithelial genes indicate that the module may partly reflect differences in epithelial composition between the tissues. It does not primarily resemble a blood or circulating-protein module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides little direct physical-interaction support: there is no STRING functional enrichment, and the only high-confidence STRING relationship is FKBP15-WASHC4. This pair is consistent with endosomal, membrane-trafficking, and actin-related biology, but it does not establish the whole module as one physical complex. hu.MAP provides partial support for epithelial structural organization. KRT13 and KRT17 co-occur in hu.MAP complexes (hu.MAP huMAP3_14196.1) and (hu.MAP huMAP3_14076.1), consistent with keratin-associated epithelial structure. CEACAM5 and SARG co-occur in (hu.MAP huMAP3_08861.1) and (hu.MAP huMAP3_14537.1), supporting a shared epithelial or cell-surface context. SERPINB3 and DSG1 co-occur in (hu.MAP huMAP3_09125.1) and (hu.MAP huMAP3_09929.1), linking the serpin-associated epithelial state with desmosomal organization. In each case only part of the reported complex is represented in the module, so these are partial complex overlaps rather than evidence that the entire module is a single assembled complex. The contrast between strong co-abundance connectivity and sparse known physical interactions suggests that the network primarily captures coordinated expression or shared cellular origin.

**STRING interactions (score >= 0.7)**: 1 of 435 gene pairs: FKBP15–WASHC4 (0.81)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14196.1 (KRT13, KRT17; 2/3); huMAP3_14076.1 (KRT13, KRT17; 2/5); huMAP3_08861.1 (CEACAM5, SARG; 2/18); huMAP3_14537.1 (CEACAM5, SARG; 2/24); huMAP3_09125.1 (SERPINB3, DSG1; 2/53); huMAP3_09929.1 (SERPINB3, DSG1; 2/75)

### Novelty

This module should not be called a newly discovered molecular complex or a definitively novel pathway. Its core biology is well established: DSG1, KRT13, KRT17, CEACAM5, and SERPINB3 have recognized epithelial, adhesion, keratin, or tissue-associated functions, and several module subsets overlap known hu.MAP complexes. At the same time, the specific conserved co-abundance arrangement across cervix_uterine and colon is not explained by a globally significant GO/KEGG term, STRING enrichment, or extensive known physical interaction network in the supplied evidence. The arrangement may therefore represent a potentially useful tissue-crossing expression signature or epithelial cell-state association, but its novelty requires independent validation, comparison with published cross-tissue co-expression modules, and testing in external cohorts. Absence from STRING or hu.MAP alone is insufficient to establish novelty.

**Hypothesis.** Hypothesis: the conserved module reflects coordinated abundance of epithelial cells undergoing maintenance of cell-cell adhesion, intermediate-filament organization, surface glycoprotein display, and vesicle or cytoskeletal trafficking. DSG1 may mark the structural epithelial core, with KRT13 and KRT17 representing differentiated or basal-to-suprabasal epithelial states, CEACAM5 and SARG representing epithelial surface organization, and trafficking or actin-related genes helping maintain membrane turnover and junctional remodeling. CTNNBIP1 may modulate the balance between epithelial differentiation and Wnt-linked proliferative signaling. In cervix_uterine and colon, the shared signal could therefore arise from a common epithelial program or from similar epithelial cell-type composition rather than direct protein interaction among all module members. The immune-associated HPA signals suggest that inflammatory or myeloid admixture could modify this program, but the supplied data do not establish that mechanism.

### Important genes

#### DSG1

- **Related proteins** (co-abundance neighbors): SYTL1 (1.00), UEVLD (1.00), CTNNBIP1 (0.99), KRT13 (0.98), FTL (0.96), CEACAM5 (0.94), MYO18A (0.92), FKBP15 (0.92), ATP5F1C (0.91), NSF (0.90), CCDC43 (0.90), HMOX2 (0.90), ADK (0.89), WASHC4 (0.88), GNS (0.88), CTTN (0.87), FAM120A (0.87), PSMC2 (0.87), KRT17 (0.87), HEBP2 (0.86), RUFY1 (0.86), SARG (0.84), GNAQ (0.82), CCDC6 (0.82), MARCKS (0.82), GLUD1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: desmoglein 1. This gene encodes a member of the desmoglein protein subfamily. Desmogleins, along with desmocollins, are cadherin-like transmembrane glycoproteins that are major components of the desmosome. Desmosomes are cell-cell junctions that help resist shearing forces and are found in high concentrations in cells subject to mechanical stress. This gene is found in a cluster with other desmoglein family mem…
- **Diseases (Open Targets)**: palmoplantar keratoderma i, striate, focal, or diffuse (0.738); severe dermatitis-multiple allergies-metabolic wasting syndrome (0.732); striate palmoplantar keratoderma (0.464); hereditary palmoplantar keratoderma (0.455); epidermolytic palmoplantar keratoderma, 1 (0.375)
- **Europe PMC papers**: 3455
- **Why important**: DSG1 is the central network hub, with the strongest connectivity and weighted strength in the module. It encodes a desmosomal cadherin that mediates calcium-dependent cell-cell adhesion and resistance to mechanical stress. Its HPA profile is enriched in skin and keratinocyte-related cell types, and it overlaps the SERPINB3-DSG1 hu.MAP complexes (hu.MAP huMAP3_09125.1) and (hu.MAP huMAP3_09929.1). It has extensive literature and established associations with several palmoplantar keratoderma and dermatitis syndromes.
- **Conclusion**: Established evidence supports DSG1 as the principal epithelial adhesion and structural anchor of the module. The network position makes it a strong marker of the module's epithelial organization, but the co-abundance data do not prove that DSG1 physically interacts with every connected gene.

#### KRT13

- **Related proteins** (co-abundance neighbors): DSG1 (0.98); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Intermediate filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_14196.1, huMAP3_14076.1
- **Function (MyGene.info)**: keratin 13. The protein encoded by this gene is a member of the keratin gene family. The keratins are intermediate filament proteins responsible for the structural integrity of epithelial cells and are subdivided into cytokeratins and hair keratins. Most of the type I cytokeratins consist of acidic proteins which are arranged in pairs of heterotypic keratin chains. This type I cytokeratin is paired with kerat…
- **Diseases (Open Targets)**: White sponge nevus (0.596); hereditary disease (0.194); oral cavity squamous cell carcinoma (0.105); neoplasm (0.104); breast cancer (0.096)
- **Europe PMC papers**: 1551
- **Why important**: KRT13 is an epithelial intermediate-filament protein associated with suprabasal layers of non-cornified stratified epithelia. It is tissue enhanced in cervix, esophagus, and vagina and is enriched in esophageal apical and suprabasal cells. It participates with KRT17 in hu.MAP complexes (hu.MAP huMAP3_14196.1) and (hu.MAP huMAP3_14076.1), providing direct complex-level support for an epithelial structural component. It also has substantial literature and disease associations including white sponge nevus.
- **Conclusion**: Established evidence supports KRT13 as a marker of differentiated stratified epithelial structure and tissue identity. Its membership in the module is consistent with a conserved epithelial program, while its absence from globally significant GO/KEGG enrichment means it should be interpreted as gene-level and network evidence rather than enrichment proof.

#### KRT17

- **Related proteins** (co-abundance neighbors): DSG1 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14196.1, huMAP3_14076.1
- **Function (MyGene.info)**: keratin 17. This gene encodes the type I intermediate filament chain keratin 17, expressed in nail bed, hair follicle, sebaceous glands, and other epidermal appendages. Mutations in this gene lead to Jackson-Lawler type pachyonychia congenita and steatocystoma multiplex. [provided by RefSeq, Aug 2008].
- **Diseases (Open Targets)**: pachyonychia congenita 2 (0.817); sebocystomatosis (0.758); pachyonychia congenita (0.570); hereditary disease (0.414); nonsyndromic congenital nail disorder 4 (0.351)
- **Europe PMC papers**: 3504
- **Why important**: KRT17 is an intermediate-filament keratin involved in epithelial differentiation, filament organization, and epithelial growth. It is enriched in basal keratinocytes and several epithelial populations and shares hu.MAP complexes with KRT13 in (hu.MAP huMAP3_14196.1) and (hu.MAP huMAP3_14076.1). Its disease associations include pachyonychia congenita and related keratin disorders, and it has a substantial literature base.
- **Conclusion**: Established evidence supports KRT17 as a structural and differentiation-related epithelial marker that complements KRT13. Its lack of protein detection in the listed tissues cautions that transcript or network association may not always translate into detectable protein abundance in these samples. A coordinated KRT13-KRT17 signal is a plausible epithelial-state feature, not proof of a complete keratin complex in this module.

#### CEACAM5

- **Related proteins** (co-abundance neighbors): DSG1 (0.94); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Plasma membrane; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: huMAP3_08861.1, huMAP3_14537.1
- **Function (MyGene.info)**: CEA cell adhesion molecule 5. This gene encodes a cell surface glycoprotein that represents the founding member of the carcinoembryonic antigen (CEA) family of proteins. The encoded protein is used as a clinical biomarker for gastrointestinal cancers and may promote tumor development through its role as a cell adhesion molecule. Additionally, the encoded protein may regulate differentiation, apoptosis, and cell polarity. This …
- **Diseases (Open Targets)**: neurodegenerative disease (0.452); breast cancer (0.426); non-small cell lung carcinoma (0.399); gonorrhea (0.379); colorectal neoplasm (0.375)
- **Europe PMC papers**: 57842
- **Why important**: CEACAM5 is a cell-surface glycoprotein involved in homophilic and heterophilic adhesion, epithelial polarity, differentiation, apoptosis, and anoikis regulation. HPA places it in intestine and in colonocyte, goblet-cell, and esophageal epithelial populations. It overlaps hu.MAP complexes with SARG in (hu.MAP huMAP3_08861.1) and (hu.MAP huMAP3_14537.1). It has a very large literature base and is an established clinical biomarker associated with gastrointestinal malignancy.
- **Conclusion**: Established evidence supports CEACAM5 as an epithelial surface and adhesion component that may help explain the module's conservation between cervix_uterine and colon. Its cancer associations make it biologically important, but the module alone does not indicate malignancy or a tumor-specific process.

#### SERPINB3

- **Related proteins** (co-abundance neighbors): MYH14 (0.88), HEBP2 (0.85), GFUS (0.85), CCDC43 (0.80); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: serpin family B member 3. Enables cysteine-type endopeptidase inhibitor activity; protease binding activity; and virus receptor activity. Involved in several processes, including autocrine signaling; paracrine signaling; and regulation of cellular protein metabolic process. Located in cytoplasmic vesicle; extracellular exosome; and nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.206); cervical carcinoma (0.195); cutaneous melanoma (0.186); neoplasm (0.114); hepatocellular carcinoma (0.102)
- **Europe PMC papers**: 1163
- **Why important**: SERPINB3 is an epithelial-associated cysteine protease inhibitor with roles in protease binding, apoptotic regulation, and autocrine or paracrine signaling. HPA enriches it in cervix, esophagus, and vagina and in apical, suprabasal, and basal epithelial populations. It overlaps hu.MAP complexes containing DSG1 in (hu.MAP huMAP3_09125.1) and (hu.MAP huMAP3_09929.1). It has substantial literature and reported associations with cervical carcinoma and other neoplastic contexts.
- **Conclusion**: Established evidence supports SERPINB3 as an epithelial stress, protease-regulatory, and disease-relevant component of the module. Its co-occurrence with DSG1 may reflect coordinated epithelial barrier or differentiation biology, but the data do not establish that SERPINB3 drives the network or that the module represents cancer.

#### CTNNBIP1

- **Related proteins** (co-abundance neighbors): DSG1 (0.99); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin beta interacting protein 1. The protein encoded by this gene binds CTNNB1 and prevents interaction between CTNNB1 and TCF family members. The encoded protein is a negative regulator of the Wnt signaling pathway. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: liver disorder (0.313); adolescent idiopathic scoliosis (0.241); colorectal carcinoma (0.102); breast cancer (0.088); breast carcinoma (0.088)
- **Europe PMC papers**: 852
- **Why important**: CTNNBIP1 encodes a beta-catenin-interacting protein that negatively regulates Wnt signaling and can restrain transcriptional and proliferative programs. It is tissue enhanced in esophagus and skin and enriched in esophageal apical and suprabasal cells. It has a meaningful literature base and disease associations including colorectal carcinoma. Its connection to DSG1 places a Wnt-regulatory gene within the epithelial structural network.
- **Conclusion**: Established evidence supports CTNNBIP1 as a plausible regulatory link between epithelial structure and Wnt-related differentiation or proliferation control. The proposed connection to the module's epithelial state is a hypothesis supported by annotation and network placement, not a demonstrated causal mechanism in cervix_uterine or colon.

## Module 6

**Tissue pair**: cervix_uterine and colon  
**Genes (13)**: ALB, APOA1, FGB, HBA1, HBB, IGHG1, IGHM, IGKC, KIAA0825, LUM, S100A8, S100A9, TF

### Function

The strongest interpretation is a blood-associated extracellular and humoral-defense module rather than a tissue-intrinsic cervix or colon pathway. The primary evidence is the globally corrected enrichment for blood microparticle (GO:CC blood microparticle; q_global = 2.61e-05), antimicrobial and antibacterial humoral responses (GO:BP antimicrobial humoral response; q_global = 0.000888) (GO:BP antibacterial humoral response; q_global = 0.00627), defense or response to bacterium (GO:BP defense response to bacterium; q_global = 0.00105) (GO:BP response to bacterium; q_global = 0.0368), and humoral immune response (GO:BP humoral immune response; q_global = 0.0121). Oxygen binding (GO:MF oxygen binding; q_global = 0.0116), antioxidant activity (GO:MF antioxidant activity; q_global = 0.0247), and cellular oxidant detoxification (GO:BP cellular oxidant detoxification; q_global = 0.0362) indicate an additional erythrocyte and redox component. Signaling receptor binding (GO:MF signaling receptor binding; q_global = 0.0341) is consistent with extracellular protein-mediated signaling. The African trypanosomiasis term (KEGG African trypanosomiasis - Homo sapiens (human); q_global = 0.0355) should not be interpreted as evidence of that infection; its overlap is explained by the module's apolipoprotein and hemoglobin genes. Overall, the module is best viewed as a coordinated plasma, blood-cell, innate-defense, immunoglobulin, oxygen-transport, and extracellular-material signal.

**Cell composition.** The module is dominated by plasma or secreted proteins and blood-associated products. Secreted-to-blood proteins include ALB, APOA1, FGB, TF, and S100A9, while IGHG1, IGHM, and IGKC represent immunoglobulin or plasma-cell-associated signals. HBA1 and HBB indicate erythrocyte material, and S100A8 and S100A9 indicate neutrophil or monocyte-associated material. HPA evidence repeatedly points to liver, hepatocytes, bone marrow, lymphoid tissue, plasma cells, erythrocytes, neutrophils, monocytes, and B-cell populations. Protein detection is limited in both represented tissues, especially in colon, and several of the most connected genes are not detected in cervix or colon by immunohistochemistry. Therefore, the shared module may largely reflect blood, plasma, immune-cell admixture, vascular leakage, or common sampled cell types rather than a conserved epithelial program. The cervix-associated S100A8 and S100A9 signal and the intestine-associated immune and enterocyte annotations leave open a genuine local inflammatory contribution, but they do not outweigh the strong blood and liver signature.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 2.61e-05 | ALB, APOA1, FGB, HBA1, HBB, IGHG1, IGHM, TF |
| GO:BP antimicrobial humoral response | 0.000888 | FGB, IGHG1, IGHM, S100A9, TF |
| GO:BP defense response to bacterium | 0.00105 | FGB, IGHG1, IGHM, S100A8, S100A9, TF |
| GO:BP antibacterial humoral response | 0.00627 | FGB, IGHG1, IGHM, TF |
| GO:MF oxygen binding | 0.0116 | ALB, HBA1, HBB |
| GO:BP humoral immune response | 0.0121 | FGB, IGHG1, IGHM, S100A9, TF |
| GO:MF antioxidant activity | 0.0247 | ALB, HBA1, HBB, S100A9 |
| GO:MF signaling receptor binding | 0.0341 | APOA1, FGB, IGHG1, IGHM, S100A8, S100A9, TF |
| KEGG African trypanosomiasis - Homo sapiens (human) | 0.0355 | APOA1, HBA1, HBB |
| GO:BP cellular oxidant detoxification | 0.0362 | ALB, HBA1, HBB, S100A9 |
| GO:BP response to bacterium | 0.0368 | FGB, IGHG1, IGHM, S100A8, S100A9, TF |

### STRING and hu.MAP

STRING supports several established relationships: ALB connects strongly with APOA1, FGB, TF, and LUM; APOA1 connects with HBB and TF; HBA1 and HBB form the expected hemoglobin relationship; and S100A8 and S100A9 form the expected inflammatory heterodimer. These known links show that important parts of the network recapitulate established extracellular, plasma, hemoglobin, and inflammatory biology. They also imply that the module is not composed solely of novel gene-gene relationships. hu.MAP independently places APOA1, FGB, ALB, and TF together across several plasma-protein complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_08224.1), places APOA1 with FGB (hu.MAP huMAP3_04772.1), HBA1 with HBB (hu.MAP huMAP3_04556.1) (hu.MAP huMAP3_06991.1) (hu.MAP huMAP3_10486.1) (hu.MAP huMAP3_13522.1), and S100A8 with S100A9 (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1). The complexes therefore reinforce a modular interpretation involving circulating protein assemblies, hemoglobin, and inflammatory S100 proteins. IGKC, IGHG1, IGHM, KIAA0825, and LUM have little or no direct STRING or hu.MAP support within the reported results, so their co-abundance should not automatically be treated as physical interaction.

**STRING interactions (score >= 0.7)**: 8 of 78 gene pairs: ALB–APOA1 (0.998); ALB–FGB (0.878); ALB–LUM (0.737); ALB–TF (0.9); APOA1–HBB (0.839); APOA1–TF (0.919); HBA1–HBB (0.999); S100A8–S100A9 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: PMID (2022) Serum alpha-1-antitrypsin level in the severity prognosis of systemic lupus erythematosus patients: Systematic exploration of novel biomarker. (FDR = 1.28e-05, 7 genes); TISSUES Left atrium (FDR = 9.89e-05, 5 genes); TISSUES Right atrium (FDR = 9.89e-05, 5 genes); WikiPathways Selenium micronutrient network (FDR = 0.0001, 5 genes); WikiPathways Folate metabolism (FDR = 0.0001, 5 genes); COMPARTMENTS Extracellular space (FDR = 0.00011, 9 genes); COMPARTMENTS Blood microparticle (FDR = 0.00013, 6 genes); COMPARTMENTS Extracellular vesicle (FDR = 0.00019, 8 genes); Component Blood microparticle (FDR = 0.00025, 6 genes); TISSUES Left ventricle (FDR = 0.00025, 5 genes); WikiPathways Network map of SARS-CoV-2 signaling pathway (FDR = 0.00039, 5 genes); WikiPathways Vitamin B12 metabolism (FDR = 0.00042, 4 genes); TISSUES Skeletal system (FDR = 0.00074, 8 genes); PMID (2022) The Implant Proteome-The Right Surgical Glue to Fix Titanium Implants In Situ. (FDR = 0.0013, 6 genes); COMPARTMENTS Hemoglobin complex (FDR = 0.0014, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (APOA1, FGB, ALB, TF, HBB, HBA1; 6/64); huMAP3_07432.1 (APOA1, FGB, ALB, TF; 4/18); huMAP3_09434.1 (APOA1, FGB, ALB, TF; 4/33); huMAP3_08395.1 (APOA1, FGB, ALB, TF; 4/43); huMAP3_09531.1 (APOA1, FGB, ALB, TF; 4/47); huMAP3_10101.1 (APOA1, FGB, ALB, TF; 4/49); huMAP3_10678.1 (APOA1, FGB, ALB, TF; 4/71); huMAP3_07265.1 (APOA1, ALB, TF; 3/20); huMAP3_04772.1 (APOA1, FGB; 2/2); huMAP3_04556.1 (HBB, HBA1; 2/3); huMAP3_06991.1 (HBB, HBA1; 2/4); huMAP3_10486.1 (HBB, HBA1; 2/4); huMAP3_13522.1 (HBB, HBA1; 2/10); huMAP3_08224.1 (APOA1, TF; 2/21); huMAP3_09125.1 (S100A8, S100A9; 2/53); huMAP3_09929.1 (S100A8, S100A9; 2/75)

### Novelty

The co-abundance module may be a new observation in the specific cervix_uterine-colon tissue-pair analysis, but the underlying biology is not a new molecular mechanism. Its central relationships, including albumin with apolipoprotein A-I, transferrin, and fibrinogen; alpha- with beta-hemoglobin; and S100A8 with S100A9, are already supported by STRING or hu.MAP. The convergence of globally corrected blood-microparticle, humoral-defense, oxygen-binding, and redox terms also gives a coherent established explanation. Lack of STRING or hu.MAP support for some genes does not demonstrate novelty, because co-abundance can arise from shared cell composition, secretion, blood contamination, or incomplete interaction databases. The defensible novelty claim is therefore limited to the reproducible cross-tissue co-abundance pattern and its particular mixture of plasma, erythrocyte, immunoglobulin, and inflammatory signals; it should not be claimed as a newly discovered complex or pathway without independent validation.

**Hypothesis.** Hypothesis: this shared module reflects variation in the amount or composition of blood-derived extracellular material present in cervix and colon samples. A plasma-protein axis involving ALB, APOA1, FGB, and TF may covary with erythrocyte material represented by HBA1 and HBB, immunoglobulin or plasma-cell material represented by IGKC, IGHG1, and IGHM, and local myeloid inflammation represented by S100A8 and S100A9. The combined signal could arise from vascular permeability, mucosal or cervical inflammation, tissue injury, or differences in immune-cell and blood-cell admixture. This hypothesis predicts that module abundance should track independent measures of blood contamination, erythrocyte transcripts, plasma proteins, immune-cell fractions, or histological inflammation. It does not establish that the genes act together inside one tissue cell or that the module represents a single biochemical complex.

### Important genes

#### TF

- **Related proteins** (co-abundance neighbors): ALB (0.90), HBA1; HBA2 (0.89), APOA1 (0.88), FGB (0.88), HBB (0.87), IGHM (0.83), IGKC (0.81); STRING partners: ALB (0.9), APOA1 (0.919)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07265.1, huMAP3_08224.1
- **Function (MyGene.info)**: transferrin. This gene encodes a glycoprotein with an approximate molecular weight of 76.5 kDa. It is thought to have been created as a result of an ancient gene duplication event that led to generation of homologous C and N-terminal domains each of which binds one ion of ferric iron. The function of this protein is to transport iron from the intestine, reticuloendothelial system, and liver parenchymal cells t…
- **Diseases (Open Targets)**: atransferrinemia (0.776); alcohol drinking (0.492); hemochromatosis type 1 (0.471); neurodegenerative disease (0.400); urolithiasis (0.329)
- **Europe PMC papers**: 143656
- **Why important**: TF is the highest-connectivity gene in the reported co-abundance subgraph and links the plasma-protein cluster to ALB, APOA1, FGB, hemoglobin genes, and IGHM or IGKC. It is secreted to blood, enriched in liver and hepatocytes, and is annotated for iron transport and antibacterial humoral response. It appears in many primary enrichment terms (7 globally significant GO/KEGG terms, q_global 2.61e-05–0.0368; see the table) and across several hu.MAP plasma-protein complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_08224.1). Its disease associations include atransferrinemia and hemochromatosis, and its literature volume is very large.
- **Conclusion**: Established evidence supports TF as a central plasma and iron-transport marker that connects several biologically distinct portions of the module. My conclusion is that TF is important mainly as an integrative marker of circulating protein composition and host defense, not as proof that the module is a TF-centered intracellular pathway. Its high network position may partly reflect shared plasma abundance.

#### ALB

- **Related proteins** (co-abundance neighbors): TF (0.90), HBB (0.89), IGKC (0.84), FGB (0.83), KIAA0825 (0.82), LUM (0.81); STRING partners: APOA1 (0.998), FGB (0.878), LUM (0.737), TF (0.9)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07265.1
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB has a highly connected position and links TF, APOA1, FGB, HBB, KIAA0825, and LUM. It is liver- and hepatocyte-enriched, secreted to blood, and described as the most abundant protein in human blood with carrier and antioxidant-related functions. It is present in primary terms for blood microparticle, oxygen binding, antioxidant activity, and oxidant detoxification (4 globally significant GO/KEGG terms, q_global 2.61e-05–0.0362; see the table), in many STRING-supported supplementary categories, and across numerous hu.MAP plasma-protein complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07265.1). It has extensive literature and disease associations including congenital analbuminemia and chronic kidney disease.
- **Conclusion**: Established evidence identifies ALB as a strong indicator of plasma carryover or extracellular blood content and as a plausible contributor to the module's transport and redox annotations. My conclusion is that ALB is a compositional anchor and network hub, but its presence provides little evidence for a cervix- or colon-specific mechanism.

#### S100A9

- **Related proteins** (co-abundance neighbors): S100A8 (0.93), IGKC (0.84); STRING partners: S100A8 (0.999)
- **HPA**: Group enriched; Cell type enriched; blood Group enriched; location Plasma membrane, Intermediate filaments, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: S100 calcium binding protein A9. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: inborn error of immunity (0.370); Sepsis (0.121); neoplasm (0.119); psoriasis (0.114); cancer (0.114)
- **Europe PMC papers**: 16393
- **Why important**: S100A9 is tightly linked to S100A8 and to IGKC, with strong support for the S100A8-S100A9 relationship in both STRING and hu.MAP (hu.MAP huMAP3_09125.1) (hu.MAP huMAP3_09929.1). It is enriched in cervix, bone marrow, esophagus, and vagina, is associated with classical monocytes and neutrophils, and is secreted to blood. It appears in primary antimicrobial, bacterial-defense, humoral, receptor-binding, and oxidant-related terms (7 globally significant GO/KEGG terms, q_global 0.000888–0.0368; see the table). It has disease associations involving immunity, sepsis, psoriasis, and cancer, together with extensive literature.
- **Conclusion**: Established evidence supports S100A9 as the clearest local inflammatory and myeloid component of the module, especially because it is detected in cervix while not detected in colon by the reported immunohistochemistry summary. My conclusion is that S100A9 may provide a genuine inflammatory contribution, although its co-abundance with plasma and erythrocyte genes could still reflect admixture or inflammation-associated vascular leakage.

#### APOA1

- **Related proteins** (co-abundance neighbors): TF (0.88), IGKC (0.85); STRING partners: ALB (0.998), HBB (0.839), TF (0.919)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07265.1, huMAP3_04772.1, huMAP3_08224.1
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 connects to TF and IGKC in the module and has strong STRING links to ALB, HBB, and TF. It is liver-enriched, associated with hepatocytes and enterocytes, secreted to blood, and is the major protein component of HDL with roles in lipid transport and cholesterol efflux. It contributes to blood-microparticle and signaling-receptor-binding enrichment (GO:CC blood microparticle; q_global = 2.61e-05) (GO:MF signaling receptor binding; q_global = 0.0341) and to the African trypanosomiasis term through the hemoglobin or apolipoprotein gene combination (KEGG African trypanosomiasis - Homo sapiens (human); q_global = 0.0355). It is present across many hu.MAP plasma-protein complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_04772.1) (hu.MAP huMAP3_08224.1) and has extensive literature and lipid-related disease associations.
- **Conclusion**: Established evidence supports APOA1 as a plasma lipid-transport and extracellular-complex marker that helps define the circulating-protein axis. My conclusion is that it is important for interpreting the module as systemic or compositional, rather than as evidence for a tissue-specific lipid pathway in cervix or colon.

#### FGB

- **Related proteins** (co-abundance neighbors): TF (0.88), ALB (0.83); STRING partners: ALB (0.878)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_04772.1
- **Function (MyGene.info)**: fibrinogen beta chain. The protein encoded by this gene is the beta component of fibrinogen, a blood-borne glycoprotein comprised of three pairs of nonidentical polypeptide chains. Following vascular injury, fibrinogen is cleaved by thrombin to form fibrin which is the most abundant component of blood clots. In addition, various cleavage products of fibrinogen and fibrin regulate cell adhesion and spreading, display vas…
- **Diseases (Open Targets)**: congenital afibrinogenemia (0.786); familial dysfibrinogenemia (0.705); congenital fibrinogen deficiency (0.622); familial hypodysfibrinogenemia (0.597); cancer (0.592)
- **Europe PMC papers**: 4215
- **Why important**: FGB connects to TF and ALB and is present across the principal humoral-defense terms (7 globally significant GO/KEGG terms, q_global 2.61e-05–0.0368; see the table). It is liver- and hepatocyte-enriched, secreted to blood, and encodes a fibrinogen component involved in coagulation, platelet activation, cell-matrix adhesion, fibrinolysis, and chemotactic or adhesion-related signaling. It participates in multiple hu.MAP plasma-protein complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_04772.1) and has established disease associations involving congenital or familial fibrinogen disorders and cancer.
- **Conclusion**: Established evidence supports FGB as a marker of circulating coagulation and extracellular-matrix biology that links the immune-defense interpretation with vascular or injury responses. My conclusion is that FGB strengthens the hypothesis of plasma leakage or tissue injury, but its co-abundance does not establish active coagulation in either tissue.

## Module 7

**Tissue pair**: cervix_uterine and colon  
**Genes (5)**: APOB, FLG, PRKCD, UBTF, VASP

### Function

No GO/KEGG term passed global correction, and there was no supplementary STRING enrichment. The module therefore does not support a single established pathway-level function. Its structure is dominated by FLG, which co-abundance-links to PRKCD, UBTF, VASP, and APOB, while the other genes do not form a coherent annotated functional group. The genes collectively point to several biological themes: epithelial barrier and differentiation through FLG, lipid transport through APOB, actin and cell-junction regulation through VASP, signaling and stress or apoptotic regulation through PRKCD, and ribosomal RNA transcription through UBTF. These mixed annotations make a unified molecular function uncertain. The most defensible interpretation is a cross-tissue co-abundance pattern reflecting correlated epithelial, vascular or platelet-associated, and lipid or secretory signals rather than a demonstrated protein complex or pathway.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: APOB is the only secreted gene and is secreted to blood, whereas the other genes are not secreted. APOB is enriched in intestine and liver and in enterocytes and hepatocytes, but it was not detected by immunohistochemistry in either studied tissue. This raises the possibility that circulating or tissue-associated lipoprotein signal contributes to the module. FLG is tissue enriched in skin and cell-type enriched in esophageal apical cells, with protein detected in cervix_uterine but not colon, suggesting an epithelial or barrier-related component that may not represent a shared protein abundance program in both tissues. PRKCD and VASP show enhancement in neutrophil or platelet-related cell types, while UBTF is enhanced in erythrocyte progenitors; however, the HPA blood-cell evidence does not indicate a strongly blood-cell-specific module, and no enriched blood-cell category was reported. PRKCD, UBTF, and VASP have low tissue specificity, consistent with broadly distributed cellular functions. Overall, shared cell composition, circulating APOB, epithelial differentiation, or technical co-variation may contribute to the cross-tissue module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was detected among any module gene pair, and no hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated as established direct or complex-level physical relationships by these resources. The absence of STRING and hu.MAP support argues against interpreting the module as a known molecular complex. It does not exclude indirect regulation, context-dependent interactions, shared cell-type composition, or coordinated expression. The strongest internal network feature is the apparent central position of FLG, which is connected to each of the other genes in the co-abundance subgraph, but this topology alone does not establish molecular binding or mechanistic regulation.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a newly discovered biological pathway or complex. The data establish a conserved co-abundance pattern between cervix_uterine and colon, but they do not establish that the pattern is a novel molecular mechanism. The genes have well-established individual functions and disease associations, yet they span epithelial barrier biology, lipid transport, cytoskeletal regulation, kinase signaling, and ribosomal transcription. The lack of STRING and hu.MAP relationships makes a previously characterized shared complex unlikely, but absence from those databases alone cannot prove novelty. A novelty claim would require independent replication, adjustment for cell composition and circulating protein contamination, and experimental or orthogonal validation of the cross-tissue association.

**Hypothesis.** Hypothesis: the module represents a shared tissue-sample composition or state signal rather than a single intracellular pathway. In this model, FLG reflects epithelial differentiation or barrier-related material, APOB reflects blood-borne or lipid-transport-associated signal, VASP reflects actin, adhesion, endothelial, trophoblast, platelet, or neutrophil-related state, and PRKCD and UBTF reflect broadly expressed signaling and biosynthetic activity. Their coordinated abundance across cervix_uterine and colon could arise from recurring mixtures of epithelial cells, vascular or platelet-associated material, circulating lipoproteins, and general cellular activity. A secondary possibility is indirect coordination between epithelial stress or differentiation and lipid or cytoskeletal remodeling. This remains a hypothesis because no globally significant GO/KEGG term, STRING interaction, or hu.MAP complex supports the mechanism.

### Important genes

#### FLG

- **Related proteins** (co-abundance neighbors): PRKCD (0.89), UBTF (0.84), VASP (0.83), APOB (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Cytoplasmic bodies; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filaggrin. The protein encoded by this gene is an intermediate filament-associated protein that aggregates keratin intermediate filaments in mammalian epidermis. It is initially synthesized as a polyprotein precursor, profilaggrin (consisting of multiple filaggrin units of 324 aa each), which is localized in keratohyalin granules, and is subsequently proteolytically processed into individual functional filag…
- **Diseases (Open Targets)**: atopic eczema (0.836); ichthyosis vulgaris (0.747); asthma (0.747); dermatitis (0.718); skin disorder (0.702)
- **Europe PMC papers**: 7929
- **Why important**: FLG is the network hub of the module, connected to every other member in the co-abundance subgraph. It encodes filaggrin, an intermediate filament-associated protein involved in keratinocyte differentiation, skin-barrier establishment, and cornification. Its tissue enrichment in skin and cell-type enrichment in esophageal apical cells provide a plausible epithelial-barrier interpretation, while its disease associations with ichthyosis vulgaris and atopic eczema make it biologically informative. Its large literature base also makes it the best-characterized candidate for testing whether the module reflects epithelial differentiation or barrier state.
- **Conclusion**: Established evidence supports FLG as an epithelial barrier and differentiation marker and as the central co-abundance node. It is not established that FLG directly regulates the other module genes. The most cautious conclusion is that FLG may mark an epithelial component or state associated with the module, rather than define a mechanistic complex.

#### APOB

- **Related proteins** (co-abundance neighbors): FLG (0.81); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Vesicles, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein B. This gene product is the main apolipoprotein of chylomicrons and low density lipoproteins (LDL), and is the ligand for the LDL receptor. It occurs in plasma as two main isoforms, apoB-48 and apoB-100: the former is synthesized exclusively in the gut and the latter in the liver. The intestinal and the hepatic forms of apoB are encoded by a single gene from a single, very long mRNA. The two isoforms…
- **Diseases (Open Targets)**: hypercholesterolemia, autosomal dominant, type B (0.814); Hypercholesterolemia (0.812); familial hypobetalipoproteinemia 1 (0.803); familial hypercholesterolemia (0.780); metabolic disease (0.729)
- **Europe PMC papers**: 28452
- **Why important**: APOB is the clearest marker of lipid transport and circulating material. It encodes the main apolipoprotein of chylomicrons and low-density lipoproteins, with intestinal and hepatic production, and is annotated for lipid transport, triglyceride mobilization, and cholesterol metabolism. HPA places it in intestine and liver, in enterocytes and hepatocytes, and identifies it as secreted to blood. Its strong disease relevance includes hypercholesterolemia and familial lipid disorders, and it has an extensive literature base. Its co-abundance link to FLG may therefore reflect sample composition or systemic lipid signal rather than a direct interaction.
- **Conclusion**: Established evidence supports APOB as a secreted lipid-transport protein and a potential contributor from blood or tissue-associated lipoproteins. It is not established that APOB participates in an FLG-centered intracellular program in cervix_uterine or colon. Its presence makes contamination, vascular exposure, or systemic metabolic state important alternative explanations.

#### VASP

- **Related proteins** (co-abundance neighbors): FLG (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions, Focal adhesion sites; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vasodilator stimulated phosphoprotein. Vasodilator-stimulated phosphoprotein (VASP) is a member of the Ena-VASP protein family. Ena-VASP family members contain an EHV1 N-terminal domain that binds proteins containing E/DFPPPPXD/E motifs and targets Ena-VASP proteins to focal adhesions. In the mid-region of the protein, family members have a proline-rich domain that binds SH3 and WW domain-containing proteins. Their C-terminal EVH2 doma…
- **Diseases (Open Targets)**: neurodegenerative disease (0.215); Hypercholesterolemia (0.133); breast cancer (0.110); breast carcinoma (0.105); hepatocellular carcinoma (0.102)
- **Europe PMC papers**: 5374
- **Why important**: VASP occupies a direct co-abundance connection to FLG and encodes an Ena-VASP family actin-regulatory protein associated with focal adhesions, cell junctions, plasma membrane structures, and actin polymerization. HPA reports enhancement in megakaryocytes, platelets, neutrophils, and extravillous trophoblasts, which is relevant to vascular, adhesive, and blood-associated sample composition. VASP also has a substantial literature base and disease links involving cancer and neurodegenerative disease, although those associations do not establish a role in this module.
- **Conclusion**: Established evidence supports VASP as a cytoskeletal, adhesion, and actin-regulatory protein with expression in several relevant cell types. The module data support it as a possible marker of epithelial junctional or vascular or platelet-associated state. They do not establish direct functional cooperation with FLG or the other module members.

#### PRKCD

- **Related proteins** (co-abundance neighbors): FLG (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase C delta. The protein encoded by this gene is a member of the protein kinase C family of serine- and threonine-specific protein kinases. The encoded protein is activated by diacylglycerol and is both a tumor suppressor and a positive regulator of cell cycle progression. Also, this protein can positively or negatively regulate apoptosis. Defects in this gene are a cause of autoimmune lymphoproliferative synd…
- **Diseases (Open Targets)**: autoimmune lymphoproliferative syndrome (0.685); acute myeloid leukemia (0.556); mast cell leukemia (0.475); systemic mastocytosis (0.471); mastocytosis (0.464)
- **Europe PMC papers**: 3335
- **Why important**: PRKCD is connected to FLG and encodes protein kinase C delta, a signaling kinase involved in phosphorylation, stress responses, DNA-damage responses, apoptosis, and cell-cycle regulation. HPA reports enhancement in neutrophils and platelets and detection in both studied tissues, making it relevant to both general tissue signaling and possible cellular-composition effects. Its disease associations include autoimmune lymphoproliferative syndrome and hematologic malignancies, and its literature supports a well-established role in signal transduction and cell fate.
- **Conclusion**: Established evidence supports PRKCD as a pleiotropic signaling and apoptosis-related kinase with relevance to immune-associated and platelet-associated cell states. Its co-abundance with FLG may indicate shared tissue stress, cell composition, or indirect signaling, but the module does not demonstrate a direct PRKCD–FLG mechanism.

#### UBTF

- **Related proteins** (co-abundance neighbors): FLG (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: upstream binding transcription factor. This gene encodes a member of the HMG-box DNA-binding protein family. The encoded protein plays a critical role in ribosomal RNA transcription as a key component of the pre-initiation complex, mediating the recruitment of RNA polymerase I to rDNA promoter regions. The encoded protein may also play important roles in chromatin remodeling and pre-rRNA processing, and its activity is regulated by bot…
- **Diseases (Open Targets)**: childhood-onset motor and cognitive regression syndrome with extrapyramidal movement disorder (0.721); hereditary disease (0.413); rare syndromic intellectual disability (0.340); neurodegenerative disease (0.290); upper respiratory tract disorder (0.175)
- **Europe PMC papers**: 879
- **Why important**: UBTF is connected to FLG and encodes a nucleolar transcription factor required for ribosomal RNA transcription and ribosomal transcription-complex assembly. It is detected in both studied tissues and has low tissue specificity, while its enhancement in erythrocyte progenitors suggests that its abundance may also reflect cellular composition. Its disease associations include rare syndromic neurodevelopmental disorders, and its literature supports a role in fundamental nucleolar and biosynthetic processes.
- **Conclusion**: Established evidence supports UBTF as a broadly relevant regulator of ribosomal RNA transcription rather than a tissue-specific marker. Its inclusion may reflect general cellular activity or composition. There is no evidence here that UBTF mechanistically connects ribosomal transcription to FLG, APOB, VASP, or PRKCD.

## Module 8

**Tissue pair**: cervix_uterine and colon  
**Genes (9)**: ATR, CHEK1, MASTL, HMMR, RNGTT, MAP2K4, SAP30BP, WDR62, ZNF106

### Function

The module is best interpreted as a sparse, mixed nuclear cell-cycle, DNA-damage-response, RNA-processing, and cytoskeletal or motility signal rather than as one proven pathway. ATR and CHEK1 provide established DNA-replication-stress checkpoint biology, while MASTL contributes mitotic-cell-cycle regulation. HMMR contributes microtubule and cell-motility biology, and RNGTT and SAP30BP contribute RNA processing, transcriptional regulation, or chromatin-related functions. No GO or KEGG term passed global correction, and STRING reported no supplementary functional enrichment. Therefore, this is an integrative biological interpretation rather than statistically confirmed pathway enrichment. The co-abundance pattern may reflect a shared proliferative or cellular-stress state.

**Cell composition.** The module is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the encoded proteins are predominantly nuclear, nucleolar, cytosolic, or microtubule-associated. Several genes have low tissue specificity, while others are enhanced in bone marrow, lymphoid tissue, testis, skeletal muscle, or tongue. HPA also shows a notable blood and immune-cell component, including neutrophil, T-reg, and monocyte-related annotations, together with progenitor and proliferative cell states. This makes contribution from blood cells, immune cells, or shared proliferating cell types a plausible explanation for part of the cervix-colon co-abundance signal. Protein detection in both tissues for many members supports presence in the sampled tissues, but the lack of detection for WDR62 in both tissues cautions against interpreting every transcript as a uniformly expressed tissue protein.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship among module members is ATR-CHEK1. This is biologically coherent with the established ATR-CHEK1 replication-stress and DNA-damage checkpoint axis. The remaining co-abundance relationships are not supported by high-confidence STRING interactions in the supplied result, so they should not be presented as physical binding relationships. No hu.MAP complex contains multiple module members. Consequently, the network appears to combine one known checkpoint relationship with co-expression or co-abundance associations that may arise from shared regulation, cell-state composition, or indirect pathway coupling.

**STRING interactions (score >= 0.7)**: 1 of 36 gene pairs: ATR–CHEK1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a potentially interesting cross-tissue co-abundance pattern, but the supplied evidence does not establish it as a new biological module. The known ATR-CHEK1 relationship shows that at least part of the signal recapitulates established biology, whereas the absence of additional STRING or hu.MAP support could reflect indirect regulation, incomplete database coverage, or tissue-composition effects. The absence of globally corrected GO or KEGG enrichment and the lack of STRING functional enrichment also prevent a strong claim of a newly defined pathway. Novelty would require independent replication, control for cell composition, comparison with published co-abundance modules, and experimental testing of the less-established connections.

**Hypothesis.** Hypothesis: in cervix and colon samples, a shared proliferative or stress-responsive cell state, potentially influenced by immune or hematopoietic cell admixture, coordinately increases DNA-replication surveillance through ATR and CHEK1, couples this response to mitotic control through MASTL, and associates it with RNA-processing, microtubule, and motility programs involving SAP30BP, RNGTT, HMMR, ZNF106, and WDR62. This hypothesis is supported by the known ATR-CHEK1 relationship, the annotated functions of the genes, and the HPA cell-state pattern, but the indirect edges and cross-tissue mechanism remain unproven.

### Important genes

#### ATR

- **Related proteins** (co-abundance neighbors): SAP30BP (0.82); STRING partners: CHEK1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATR checkpoint kinase. The protein encoded by this gene is a serine/threonine kinase and DNA damage sensor, activating cell cycle checkpoint signaling upon DNA stress. The encoded protein can phosphorylate and activate several proteins involved in the inhibition of DNA replication and mitosis, and can promote DNA repair, recombination, and apoptosis. This protein is also important for fragile site stability and centroso…
- **Diseases (Open Targets)**: Seckel syndrome 1 (0.744); familial cutaneous telangiectasia and oropharyngeal predisposition cancer syndrome (0.669); Seckel syndrome (0.666); microcephalic primordial dwarfism (0.513); hereditary disease (0.474)
- **Europe PMC papers**: 41041
- **Why important**: ATR is a central mechanistic anchor because it is an established DNA-damage sensor and replication-stress checkpoint kinase, with functions in DNA repair, replication, mitotic control, telomere maintenance, recombination, apoptosis, fragile-site stability, and centrosome duplication. It participates in the only high-confidence STRING relationship detected within the module, the ATR-CHEK1 connection, and has a very large literature footprint and strong disease relevance in the supplied evidence.
- **Conclusion**: Established evidence supports ATR as the strongest checkpoint interpretation of the module. Its co-abundance with SAP30BP and its connection to CHEK1 may indicate coordinated replication-stress biology, but the module does not prove that ATR physically interacts with the other co-abundant genes.

#### CHEK1

- **Related proteins** (co-abundance neighbors): MASTL (0.84); STRING partners: ATR (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: checkpoint kinase 1. The protein encoded by this gene belongs to the Ser/Thr protein kinase family. It is required for checkpoint mediated cell cycle arrest in response to DNA damage or the presence of unreplicated DNA. This protein acts to integrate signals from ATM and ATR, two cell cycle proteins involved in DNA damage responses, that also associate with chromatin in meiotic prophase I. Phosphorylation of CDC25A pr…
- **Diseases (Open Targets)**: neurodegenerative disease (0.542); oocyte/zygote/embryo maturation arrest 21 (0.482); female infertility due to oocyte meiotic arrest (0.370); Male infertility due to gonadal dysgenesis or sperm disorder (0.266); alopecia areata (0.172)
- **Europe PMC papers**: 9282
- **Why important**: CHEK1 is the direct checkpoint counterpart of ATR in the known STRING relationship. It is established as a serine-threonine kinase required for checkpoint-mediated cell-cycle arrest in response to DNA damage or unreplicated DNA, and it contributes to DNA replication, DNA repair, chromatin remodeling, and mitotic G2 checkpoint signaling. It also has a very large literature footprint and broad disease and reproductive biology associations.
- **Conclusion**: Established evidence supports a genuine ATR-CHEK1 checkpoint component within the module. The association of CHEK1 with MASTL in the co-abundance graph is biologically plausible as coordination between DNA-damage surveillance and mitotic control, but it remains a co-abundance inference rather than a demonstrated physical complex in this dataset.

#### MASTL

- **Related proteins** (co-abundance neighbors): CHEK1 (0.84), SAP30BP (0.83), MAP2K4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: microtubule associated serine/threonine kinase like. This gene encodes a microtubule-associated serine/threonine kinase. Mutations at this locus have been associated with autosomal dominant thrombocytopenia, also known as thrombocytopenia-2. Alternatively spliced transcript variants have been described for this locus. [provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.539); Alzheimer disease (0.515); Parkinson disease (0.503); lysosomal storage disease (0.503); autosomal thrombocytopenia with normal platelets (0.370)
- **Europe PMC papers**: 591
- **Why important**: MASTL has a prominent position in the module graph and connects CHEK1 with SAP30BP and MAP2K4. Its established annotations include G2/M transition, regulation of the mitotic cell cycle, DNA-damage response, and intracellular signaling. Its disease associations include autosomal thrombocytopenia, and its literature volume is substantial. This makes it a useful bridge between the checkpoint interpretation and broader cell-cycle regulation.
- **Conclusion**: Established evidence supports MASTL as a mitotic and cell-cycle regulator that could complement ATR-CHEK1 activity. The proposed role of MASTL as a bridge linking checkpoint, transcriptional, and MAPK-related signals is a hypothesis from the co-abundance structure, not a demonstrated complex or enriched pathway.

#### HMMR

- **Related proteins** (co-abundance neighbors): ZNF106 (0.85), SAP30BP (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Microtubules; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hyaluronan mediated motility receptor. The protein encoded by this gene is involved in cell motility. It is expressed in breast tissue and together with other proteins, it forms a complex with BRCA1 and BRCA2, thus is potentially associated with higher risk of breast cancer. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene. [provided by RefSeq, Dec 2008].
- **Diseases (Open Targets)**: ovarian cancer (0.342); thyroid gland carcinoma (0.306); alcohol drinking (0.298); Alzheimer disease (0.279); Parkinson disease (0.279)
- **Europe PMC papers**: 2289
- **Why important**: HMMR connects ZNF106 and SAP30BP in the module and is associated with microtubules, cell motility, receptor-mediated endocytosis, hyaluronan catabolism, and carbohydrate-derivative transport. HPA reports tissue enhancement in bone marrow and lymphoid tissue as well as cell-state enhancement in proliferating or germline-related populations, with an immune-cell association. Its substantial literature and cancer-related disease associations make it an important candidate for linking cell-cycle state, cytoskeletal behavior, and tissue or immune composition.
- **Conclusion**: Established evidence supports HMMR as a cytoskeletal and motility-related regulator with relevance to proliferative and tissue-context biology. Its position in this module may indicate coupling of checkpoint or proliferative programs to cell movement or cell-state composition, but that coupling is a hypothesis and is not supported by a detected hu.MAP complex.

#### ZNF106

- **Related proteins** (co-abundance neighbors): RNGTT (0.87), HMMR (0.85), WDR62 (0.85); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoli; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger protein 106. Enables RNA binding activity. Predicted to be involved in insulin receptor signaling pathway. Predicted to be located in nuclear speck and nucleolus. Predicted to be active in cytosol and membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: urethritis (0.352); hyperaldosteronism (0.191); benign neoplasm of eye (0.179); preeclampsia (0.179); Complete right bundle branch block (0.178)
- **Europe PMC papers**: 130
- **Why important**: ZNF106 has one of the most connected positions in the module, linking RNGTT, HMMR, and WDR62. The supplied annotations support RNA binding and predicted roles in insulin-receptor signaling, with predicted localization in nuclear specks and nucleoli as well as cytosol and membrane. HPA places it in muscle- and tongue-enhanced tissue contexts and shows neutrophil-related cell enhancement. Its disease associations are broad, while its literature footprint is more limited than those of the major checkpoint genes, making it a potentially informative but less established connector.
- **Conclusion**: Established evidence supports ZNF106 as an RNA-binding and multi-compartment protein with a prominent position in this co-abundance graph. Its role as a coordinator of RNA processing, cytoskeletal, and immune-cell-associated signals is a hypothesis based on network position and annotations; no direct STRING or hu.MAP relationship establishes that mechanism.

## Module 9

**Tissue pair**: cervix_uterine and colon  
**Genes (26)**: ATXN2L, RNF40, CCAR1, CHD4, CSTF2, DDX24, DDX5, DNMT1, RNMT, NUP107, NUP205, NUP214, NUP88, NUP93, NUP98, PRRC2C, PRPF4, RBM39, RPAP3, POLR2B, SDAD1, SF3A1, SMARCA4, SRRT, TCERG1, ZNF638

### Function

This is a nuclear gene-expression and RNA-handling module. The strongest primary evidence identifies structural constituents of the nuclear pore and nuclear pore complex assembly or organization (GO:MF structural constituent of nuclear pore; q_global = 1.05e-05), (GO:CC nuclear pore; q_global = 0.00191), (GO:BP nuclear pore complex assembly; q_global = 0.00306), (GO:BP nuclear pore organization; q_global = 0.00841), (GO:BP pore complex assembly; q_global = 0.0125). The module also supports nucleocytoplasmic transport, RNA export, and mRNA transport (GO:BP mRNA transport; q_global = 0.0091), (KEGG Nucleocytoplasmic transport - Homo sapiens (human); q_global = 0.0137), (GO:BP RNA export from nucleus; q_global = 0.0186), (GO:BP nuclear export; q_global = 0.0251), (GO:BP nucleic acid transport; q_global = 0.028), (GO:BP RNA transport; q_global = 0.028), (GO:BP establishment of RNA localization; q_global = 0.0346), (GO:BP nucleobase-containing compound transport; q_global = 0.0382). A broad RNA-processing program is represented by RNA binding, RNA metabolic processes, mRNA processing, mRNA metabolism, and RNA biosynthesis (GO:MF RNA binding; q_global = 0.000491), (GO:BP RNA metabolic process; q_global = 0.00422), (GO:BP mRNA processing; q_global = 0.00857), (GO:BP RNA biosynthetic process; q_global = 0.0193), (GO:BP mRNA metabolic process; q_global = 0.0231), (GO:BP nucleic acid metabolic process; q_global = 0.0261), (GO:BP nucleic acid biosynthetic process; q_global = 0.0322). Nuclear pore and RNA-processing genes are connected to transcriptional, splicing, RNA capping, chromatin-remodeling, and RNA export functions in the individual annotations. The ALS pathway term (KEGG Amyotrophic lateral sclerosis - Homo sapiens (human); q_global = 0.0479) should be interpreted as pathway overlap involving nucleocytoplasmic transport and RNA biology, not as evidence that this module specifically causes ALS. The supplementary STRING results independently support capped pre-mRNA processing and RNA metabolism (STRING RCTM Processing of Capped Intron-Containing Pre-mRNA; within-query FDR = 2.12e-11), (STRING RCTM Metabolism of RNA; within-query FDR = 1.94e-08), while not serving as global enrichment evidence.

**Cell composition.** The module is predominantly composed of broadly expressed intracellular nuclear or nucleoplasmic proteins rather than plasma proteins or secreted proteins. HPA reports no secreted genes, generally low tissue specificity, and generally low immune-cell specificity. Although selected genes show cell-type enhancement in spermatogenic cells, neutrophils, neural or glial cells, epithelial cells, or bone marrow, the overall profile does not support a blood-cell module or a plasma-protein contamination explanation. Protein detection in both cervix_uterine and colon for most assayed genes is consistent with a conserved housekeeping-like nuclear program. The shared signal therefore most plausibly reflects common cellular machinery, while variation in cell composition remains a possible contributor for the genes with cell-type-enhanced HPA profiles.

**GO/KEGG enrichment**: 34 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF structural constituent of nuclear pore | 1.05e-05 | NUP107, NUP205, NUP214, NUP88, NUP93, NUP98 |
| GO:CC nuclear lumen | 2.99e-05 | ATXN2L, CCAR1, CHD4, CSTF2, DDX24, DDX5, DNMT1, NUP107, NUP205, NUP214, NUP88, NUP93, NUP98, POLR2B, PRPF4, RBM39, RNF40, RNMT, SDAD1, SF3A1, SMARCA4, SRRT, TCERG1, ZNF638 |
| GO:CC nuclear protein-containing complex | 0.000213 | CHD4, CSTF2, DDX5, NUP107, NUP205, NUP214, NUP88, NUP93, NUP98, POLR2B, PRPF4, RNMT, SF3A1, SMARCA4 |
| GO:MF RNA binding | 0.000491 | ATXN2L, CCAR1, CSTF2, DDX24, DDX5, DNMT1, NUP98, POLR2B, PRPF4, PRRC2C, RBM39, RNF40, RNMT, SF3A1, SMARCA4, SRRT, TCERG1, ZNF638 |
| GO:CC nuclear pore | 0.00191 | NUP107, NUP205, NUP214, NUP88, NUP93, NUP98 |
| GO:MF nucleic acid binding | 0.00266 | ATXN2L, CCAR1, CHD4, CSTF2, DDX24, DDX5, DNMT1, NUP98, POLR2B, PRPF4, PRRC2C, RBM39, RNF40, RNMT, SF3A1, SMARCA4, SRRT, TCERG1, ZNF638 |
| GO:BP nuclear pore complex assembly | 0.00306 | NUP107, NUP205, NUP93, NUP98 |
| GO:BP RNA metabolic process | 0.00422 | ATXN2L, CCAR1, CHD4, CSTF2, DDX24, DDX5, DNMT1, NUP98, POLR2B, PRPF4, RBM39, RNF40, RNMT, SF3A1, SMARCA4, SRRT, TCERG1, ZNF638 |
| GO:CC nuclear body | 0.00477 | ATXN2L, CSTF2, DDX5, NUP98, PRPF4, RBM39, SF3A1, SRRT, TCERG1, ZNF638 |
| GO:CC nucleoplasm | 0.00776 | ATXN2L, CCAR1, CHD4, CSTF2, DDX5, DNMT1, NUP214, NUP88, NUP98, POLR2B, PRPF4, RBM39, RNF40, RNMT, SDAD1, SF3A1, SMARCA4, SRRT, TCERG1, ZNF638 |
| GO:BP nuclear pore organization | 0.00841 | NUP107, NUP205, NUP93, NUP98 |
| GO:BP mRNA processing | 0.00857 | CSTF2, DDX5, NUP98, PRPF4, RBM39, RNMT, SF3A1, SRRT, TCERG1 |
| GO:BP mRNA transport | 0.0091 | NUP107, NUP205, NUP214, NUP88, NUP93, NUP98 |
| GO:CC nuclear periphery | 0.0125 | NUP107, NUP205, NUP93, NUP98 |
| GO:BP pore complex assembly | 0.0125 | NUP107, NUP205, NUP93, NUP98 |

### STRING and hu.MAP

STRING shows a coherent nucleoporin block involving NUP107, NUP205, NUP214, NUP88, NUP93, and NUP98, with very strong known relationships among these proteins. It also shows established RNA-processing connections involving DDX5, RBM39, SRRT, TCERG1, SF3A1, PRPF4, and CCAR1, plus chromatin-related links involving CHD4, SMARCA4, and DNMT1. These relationships indicate that the co-abundance structure substantially recapitulates known molecular machinery rather than being an arbitrary association. STRING functional results support capped pre-mRNA processing, RNA metabolism, and nuclear localization (STRING RCTM Processing of Capped Intron-Containing Pre-mRNA; within-query FDR = 2.12e-11), (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 1.84e-08), (STRING RCTM Metabolism of RNA; within-query FDR = 1.94e-08). hu.MAP complexes provide orthogonal support for nucleoporin assemblies containing NUP98, NUP214, NUP88, NUP107, NUP93, and NUP205 (hu.MAP huMAP3_10000.1) through (hu.MAP huMAP3_09710.1), spliceosomal complexes containing SF3A1 and PRPF4 (hu.MAP huMAP3_06511.1), (hu.MAP huMAP3_08980.1), a transcription-associated complex containing POLR2B and RPAP3 (hu.MAP huMAP3_14318.1), (hu.MAP huMAP3_11092.1), and complexes linking TCERG1 with DNMT1 or SF3A1 with CCAR1 (hu.MAP huMAP3_13998.1), (hu.MAP huMAP3_10359.1). The module therefore contains several established physical or functional subassemblies connected by RNA processing and nuclear transport.

**STRING interactions (score >= 0.7)**: 36 of 325 gene pairs: CCAR1–DDX5 (0.836); CCAR1–RBM39 (0.875); CCAR1–SRRT (0.857); CCAR1–TCERG1 (0.92); CHD4–DNMT1 (0.831); CHD4–SMARCA4 (0.966); CHD4–SRRT (0.76); DDX24–DDX5 (0.768); DDX24–SDAD1 (0.854); DDX5–RBM39 (0.971); DDX5–SMARCA4 (0.782); DDX5–SRRT (0.855); DDX5–TCERG1 (0.836); DNMT1–SMARCA4 (0.759); NUP107–NUP205 (0.999); NUP107–NUP214 (0.999); NUP107–NUP88 (0.994); NUP107–NUP93 (0.999); NUP107–NUP98 (0.999); NUP205–NUP214 (0.998); NUP205–NUP88 (0.995); NUP205–NUP93 (0.999); NUP205–NUP98 (0.996); NUP214–NUP88 (0.999); NUP214–NUP93 (0.999); NUP214–NUP98 (0.999); NUP88–NUP93 (0.995); NUP88–NUP98 (0.999); NUP93–NUP98 (0.999); POLR2B–RPAP3 (0.817); PRPF4–SF3A1 (0.998); RBM39–SF3A1 (0.722); RBM39–SRRT (0.936); RBM39–TCERG1 (0.887); SF3A1–TCERG1 (0.992); SRRT–TCERG1 (0.839)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Processing of Capped Intron-Containing Pre-mRNA (FDR = 2.12e-11, 15 genes); COMPARTMENTS Nuclear lumen (FDR = 1.84e-08, 20 genes); RCTM Metabolism of RNA (FDR = 1.94e-08, 16 genes); Keyword Isopeptide bond (FDR = 6.66e-07, 18 genes); Component Nuclear lumen (FDR = 2.75e-06, 24 genes); RCTM Viral Messenger RNA Synthesis (FDR = 3.86e-06, 7 genes); RCTM SUMO E3 ligases SUMOylate target proteins (FDR = 5.15e-06, 8 genes); RCTM Transcriptional regulation by small RNAs (FDR = 5.15e-06, 7 genes); RCTM tRNA processing in the nucleus (FDR = 5.78e-06, 7 genes); Keyword Ubl conjugation (FDR = 8.57e-06, 18 genes); COMPARTMENTS Nucleus (FDR = 8.85e-06, 24 genes); COMPARTMENTS Nucleoplasm (FDR = 8.85e-06, 14 genes); RCTM Late Phase of HIV Life Cycle (FDR = 1.23e-05, 8 genes); Component Nuclear protein-containing complex (FDR = 1.61e-05, 14 genes); RCTM Transport of the SLBP independent Mature mRNA (FDR = 2.22e-05, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10000.1 (RNMT, NUP214, NUP98, NUP88; 4/44); huMAP3_12581.1 (NUP214, NUP98, NUP107, NUP88; 4/58); huMAP3_05948.1 (NUP214, NUP98, NUP88; 3/5); huMAP3_06369.1 (NUP214, NUP98, NUP88; 3/12); huMAP3_07789.1 (NUP93, NUP205; 2/7); huMAP3_07705.1 (NUP98, NUP107; 2/9); huMAP3_05673.1 (NUP93, NUP205; 2/11); huMAP3_09220.1 (NUP214, NUP88; 2/11); huMAP3_09710.1 (NUP98, NUP107; 2/13); huMAP3_13998.1 (TCERG1, DNMT1; 2/23); huMAP3_09042.1 (NUP93, NUP205; 2/26); huMAP3_10359.1 (SF3A1, CCAR1; 2/27); huMAP3_14318.1 (POLR2B, RPAP3; 2/58); huMAP3_11092.1 (POLR2B, RPAP3; 2/65); huMAP3_06511.1 (PRPF4, SF3A1; 2/79); huMAP3_08980.1 (PRPF4, SF3A1; 2/97)

### Novelty

The molecular functions represented here are not new: nuclear pores, nucleocytoplasmic transport, pre-mRNA processing, splicing, transcription, and chromatin regulation are well-established processes, and many within-module relationships are already captured by STRING and hu.MAP. The potentially novel aspect is the conserved co-abundance configuration across cervix_uterine and colon, particularly the coordinated signal linking nucleoporin machinery with RNA-processing and transcriptional factors in these tissue groups. The fact sheet does not provide an external replication cohort, perturbation experiment, temporal information, or a comparison with previously published cross-tissue modules. Therefore this should be described as a plausible tissue-pair-specific network observation, not as a confirmed new biological mechanism. Lack of database representation would not establish novelty, and in this case database support is substantial.

**Hypothesis.** Hypothesis: in both cervix_uterine and colon, variation in a shared nuclear infrastructure program coordinates nuclear pore abundance with RNA processing, transcription, and chromatin regulation. Changes in nucleoporin availability could alter RNA export and nuclear organization, while coordinated activity of splicing, RNA capping, RNA-binding, and chromatin-remodeling factors could help maintain productive gene expression. The observed co-abundance may consequently reflect a conserved epithelial or proliferative cell-state program, or a common response to cellular stress, rather than direct physical interaction among every module member. This hypothesis should be tested using independent tissue cohorts, cell-type-resolved measurements, perturbation of nucleoporin or RNA-processing components, and assays of RNA export and splicing.

### Important genes

#### NUP93

- **Related proteins** (co-abundance neighbors): TCERG1 (0.85), NUP107 (0.84), SDAD1 (0.83), NUP88 (0.81), NUP205 (0.81), DNMT1 (0.81), NUP98 (0.80), DDX5 (0.80); STRING partners: NUP107 (0.999), NUP205 (0.999), NUP214 (0.999), NUP88 (0.995), NUP98 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: huMAP3_07789.1, huMAP3_05673.1, huMAP3_09042.1
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 is a highly connected module hub and is linked within STRING to the principal nucleoporin block containing NUP107, NUP205, NUP214, NUP88, and NUP98. It is represented in many primary nuclear pore, transport, export, and assembly terms (GO:MF structural constituent of nuclear pore; q_global = 1.05e-05), (GO:BP nuclear pore complex assembly; q_global = 0.00306), (GO:BP nuclear pore organization; q_global = 0.00841), (GO:BP mRNA transport; q_global = 0.0091), (KEGG Nucleocytoplasmic transport - Homo sapiens (human); q_global = 0.0137), (GO:BP RNA export from nucleus; q_global = 0.0186), (GO:BP nuclear export; q_global = 0.0251), (GO:BP nucleic acid transport; q_global = 0.028), (GO:BP RNA transport; q_global = 0.028), (GO:BP establishment of RNA localization; q_global = 0.0346), (GO:BP nucleobase-containing compound transport; q_global = 0.0382). Its established role is as a structural and transport component of the nuclear pore, and its disease associations include nephrotic syndromes and viral or infectious disease annotations. Its literature support is substantial.
- **Conclusion**: Established conclusion: NUP93 is a central structural anchor for the nuclear pore component of this module. Hypothesis: coordinated NUP93 abundance may couple pore organization to RNA export in the shared tissue program.

#### NUP98

- **Related proteins** (co-abundance neighbors): NUP214 (0.81), NUP88 (0.81), SF3A1 (0.81), SRRT (0.80), NUP93 (0.80); STRING partners: NUP107 (0.999), NUP205 (0.996), NUP214 (0.999), NUP88 (0.999), NUP93 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10000.1, huMAP3_12581.1, huMAP3_05948.1, huMAP3_06369.1, huMAP3_07705.1, huMAP3_09710.1
- **Function (MyGene.info)**: nucleoporin 98 and 96 precursor. Nuclear pore complexes (NPCs) regulate the transport of macromolecules between the nucleus and cytoplasm, and are composed of many polypeptide subunits, many of which belong to the nucleoporin family. This gene belongs to the nucleoporin gene family and encodes a 186 kDa precursor protein that undergoes autoproteolytic cleavage to generate a 98 kDa nucleoporin and 96 kDa nucleoporin. The 98 kDa nu…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); acute myeloid leukemia (0.399); lung carcinoma (0.376)
- **Europe PMC papers**: 4839
- **Why important**: NUP98 has broad connectivity across the module and is the most broadly represented nucleoporin in the primary enrichment results, spanning nuclear pore structure, pore assembly, RNA export, nucleocytoplasmic transport, RNA binding, and RNA metabolism (GO:MF structural constituent of nuclear pore; q_global = 1.05e-05) through (KEGG Amyotrophic lateral sclerosis - Homo sapiens (human); q_global = 0.0479) except (GO:CC nuclear speck; q_global = 0.0329). STRING and hu.MAP place it in several established nucleoporin assemblies (hu.MAP huMAP3_10000.1) through (hu.MAP huMAP3_07705.1), and it has extensive literature support. Its annotations include RNA export, nuclear pore organization, nucleocytoplasmic transport, and nuclear periphery functions, with disease associations including acute myeloid leukemia and viral disease.
- **Conclusion**: Established conclusion: NUP98 is a strong integrator of the pore and RNA-processing signals. Hypothesis: NUP98 may help couple transport selectivity or nuclear organization to the RNA metabolic state represented by the module.

#### SRRT

- **Related proteins** (co-abundance neighbors): NUP107 (0.87), TCERG1 (0.87), CSTF2 (0.84), SMARCA4 (0.84), CHD4 (0.83), DDX5 (0.82), SF3A1 (0.80), NUP98 (0.80); STRING partners: CCAR1 (0.857), CHD4 (0.76), DDX5 (0.855), RBM39 (0.936), TCERG1 (0.839)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serrate, RNA effector molecule. Enables mRNA cap binding complex binding activity and protein-macromolecule adaptor activity. Involved in primary miRNA processing. Located in nucleoplasm. Part of ribonucleoprotein complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dengue disease (0.370); myxedema (0.228); hypothyroidism (0.228); neurodegenerative disease (0.227); hair color (0.175)
- **Europe PMC papers**: 413
- **Why important**: SRRT has the strongest network position in the module and connects the nucleoporin, RNA-processing, transcriptional, and chromatin-related portions of the graph. It is present in a wide range of primary nuclear, RNA-binding, RNA-processing, and RNA-metabolism terms (GO:CC nuclear lumen; q_global = 2.99e-05), (GO:MF RNA binding; q_global = 0.000491), (GO:BP RNA metabolic process; q_global = 0.00422), (GO:BP mRNA processing; q_global = 0.00857), (GO:BP RNA biosynthetic process; q_global = 0.0193), (GO:BP mRNA metabolic process; q_global = 0.0231), (GO:BP nucleic acid metabolic process; q_global = 0.0261), (GO:BP nucleic acid biosynthetic process; q_global = 0.0322), and has STRING links to CCAR1, CHD4, DDX5, RBM39, and TCERG1. Its established annotations include mRNA cap-binding complex interaction, protein-adaptor activity, and primary microRNA processing. Its literature volume is substantial, although lower than that of the major nucleoporins.
- **Conclusion**: Established conclusion: SRRT is a plausible connector between nuclear RNA regulation and the nucleoporin-associated subgraph. Hypothesis: SRRT could help transmit changes in nuclear organization into RNA maturation or post-transcriptional regulation.

#### DDX5

- **Related proteins** (co-abundance neighbors): SRRT (0.82), RBM39 (0.80), NUP93 (0.80); STRING partners: CCAR1 (0.836), DDX24 (0.768), RBM39 (0.971), SMARCA4 (0.782), SRRT (0.855), TCERG1 (0.836)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 is a well-studied RNA helicase and transcriptional or splicing regulator with strong STRING relationships to RBM39, SRRT, TCERG1, CCAR1, DDX24, and SMARCA4. It participates in many primary RNA-binding, RNA-processing, RNA-metabolic, nuclear-body, and nuclear-speck terms (GO:MF RNA binding; q_global = 0.000491), (GO:BP RNA metabolic process; q_global = 0.00422), (GO:CC nuclear body; q_global = 0.00477), (GO:BP mRNA processing; q_global = 0.00857), (GO:BP RNA biosynthetic process; q_global = 0.0193), (GO:BP mRNA metabolic process; q_global = 0.0231), (GO:BP nucleic acid metabolic process; q_global = 0.0261), (GO:BP nucleic acid biosynthetic process; q_global = 0.0322), (GO:CC nuclear speck; q_global = 0.0329). Its disease and cancer associations include colorectal and colon adenocarcinoma annotations, making it particularly relevant to the tissue pair. Its literature volume is high.
- **Conclusion**: Established conclusion: DDX5 represents the RNA remodeling and splicing arm of the module and is a biologically credible bridge to transcriptional regulation. Hypothesis: DDX5 activity may mediate tissue-state-dependent changes in RNA processing downstream of altered nuclear transport.

#### SF3A1

- **Related proteins** (co-abundance neighbors): NUP98 (0.81), SRRT (0.80), CCAR1 (0.80); STRING partners: PRPF4 (0.998), RBM39 (0.722), TCERG1 (0.992)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: huMAP3_10359.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 is a core U2 spliceosomal component with STRING support for PRPF4, TCERG1, RBM39, and SRRT and hu.MAP support for spliceosomal complexes (hu.MAP huMAP3_10359.1), (hu.MAP huMAP3_06511.1), (hu.MAP huMAP3_08980.1). It occurs across the primary nuclear RNA-binding, mRNA-processing, RNA-metabolism, and nuclear-speck terms (GO:MF RNA binding; q_global = 0.000491), (GO:BP RNA metabolic process; q_global = 0.00422), (GO:BP mRNA processing; q_global = 0.00857), (GO:BP mRNA metabolic process; q_global = 0.0231), (GO:BP nucleic acid biosynthetic process; q_global = 0.0322), (GO:CC nuclear speck; q_global = 0.0329). Its established function in spliceosome assembly and splice-site recognition directly explains the RNA-processing component of the module. It has substantial literature and disease annotations including retinal dystrophy and neurodegenerative disease.
- **Conclusion**: Established conclusion: SF3A1 is a key established spliceosomal representative of the module. Hypothesis: coordinated SF3A1 abundance could alter alternative splicing as a downstream consequence of shared nuclear transport or transcriptional-state changes.

## Module 10

**Tissue pair**: cervix_uterine and colon  
**Genes (19)**: SLC4A1, C4BPA, CP, CFB, CFH, CLU, C3, C5, COL6A1, C9, FGA, HPX, SERPIND1, SERPING1, ITIH2, ITIH4, KNG1, PLTP, SDR16C5

### Function

The module is best interpreted as a circulating complement, humoral immune, and coagulation-associated protein program. The primary evidence is the globally corrected enrichment for blood microparticle (GO:CC blood microparticle; q_global = 5.23e-12), complement and coagulation cascades (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 5.47e-12), humoral immune response (GO:BP humoral immune response; q_global = 5.48e-08), complement activation (GO:BP complement activation; q_global = 1.57e-07), alternative and classical complement pathways (GO:BP complement activation, alternative pathway; q_global = 5.76e-06) and (GO:BP complement activation, classical pathway; q_global = 1.58e-05), extracellular space (GO:CC extracellular space; q_global = 0.000489), innate immune response (GO:BP innate immune response; q_global = 0.00149), and regulation of complement activation (GO:BP regulation of complement activation; q_global = 0.00288). The enrichment for peptidase inhibitor activity (GO:MF endopeptidase inhibitor activity; q_global = 0.000203), (GO:MF peptidase inhibitor activity; q_global = 0.000203), (GO:MF endopeptidase regulator activity; q_global = 0.000311), and (GO:MF enzyme inhibitor activity; q_global = 0.0108) indicates that protease control is an important accompanying feature. The coronavirus and pertussis pathway terms (KEGG Coronavirus disease - Homo sapiens (human); q_global = 0.0311) and (KEGG Pertussis - Homo sapiens (human); q_global = 0.0488) should be interpreted as pathway-overlap annotations rather than evidence of infection. Overall, the module represents coordinated extracellular host-defense, complement regulation, protease inhibition, and blood coagulation biology.

**Cell composition.** The module is overwhelmingly composed of secreted or extracellular proteins, with HPA identifying most members as secreted to blood and nearly all as extracellular or plasma-associated. HPA tissue annotations are dominated by liver, and hepatocytes are the most frequent enriched single-cell type. This strongly suggests that the shared cervix_uterine and colon signal may largely reflect circulating liver-derived plasma proteins present in the samples, rather than a locally expressed module in either tissue. The blood microparticle enrichment (GO:CC blood microparticle; q_global = 5.23e-12) and the supplementary STRING annotations for bone marrow, plasma cells, blood microparticles, extracellular space, and secreted proteins (STRING TISSUES Bone marrow cell; within-query FDR = 2.18e-15) through (STRING COMPARTMENTS Blood microparticle; within-query FDR = 5.19e-14) and (STRING TISSUES Bone marrow; within-query FDR = 1.42e-12) through (STRING COMPARTMENTS Extracellular region; within-query FDR = 2.08e-10) reinforce this interpretation. SLC4A1 is consistent with an erythrocyte-related contribution, while the immune-cell annotations are limited and heterogeneous. The module should therefore not be described as a conventional tissue-resident immune-cell program. HPA detects very little protein in either tissue for most members, which further supports a blood-contamination, vascular, or shared extracellular-fluid explanation. COL6A1 provides a possible extracellular-matrix or stromal component, and SDR16C5 is a more tissue-associated outlier, but neither changes the dominant plasma-protein interpretation.

**GO/KEGG enrichment**: 45 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 5.23e-12 | C3, C4BPA, C9, CFB, CFH, CLU, CP, FGA, HPX, ITIH2, ITIH4, KNG1, SERPING1, SLC4A1 |
| KEGG Complement and coagulation cascades - Homo sapiens (human) | 5.47e-12 | C3, C4BPA, C5, C9, CFB, CFH, CLU, FGA, KNG1, SERPIND1, SERPING1 |
| GO:BP humoral immune response | 5.48e-08 | C3, C4BPA, C5, C9, CFB, CFH, CLU, FGA, HPX, SERPING1 |
| GO:BP complement activation | 1.57e-07 | C3, C4BPA, C5, C9, CFB, CFH, CLU, SERPING1 |
| GO:BP humoral immune response mediated by circulating immunoglobulin | 1.32e-06 | C3, C4BPA, C5, C9, CLU, HPX, SERPING1 |
| GO:BP complement activation, alternative pathway | 5.76e-06 | C3, C5, C9, CFB, CFH |
| GO:BP complement activation, classical pathway | 1.58e-05 | C3, C4BPA, C5, C9, CLU, SERPING1 |
| GO:CC endoplasmic reticulum lumen | 2.31e-05 | C3, CLU, COL6A1, CP, FGA, ITIH2, KNG1, SERPIND1, SERPING1 |
| GO:BP immunoglobulin mediated immune response | 4.96e-05 | C3, C4BPA, C5, C9, CLU, HPX, SERPING1 |
| GO:BP B cell mediated immunity | 6.01e-05 | C3, C4BPA, C5, C9, CLU, HPX, SERPING1 |
| GO:MF endopeptidase inhibitor activity | 0.000203 | C3, C5, ITIH2, ITIH4, KNG1, SERPIND1, SERPING1 |
| GO:MF peptidase inhibitor activity | 0.000203 | C3, C5, ITIH2, ITIH4, KNG1, SERPIND1, SERPING1 |
| GO:MF endopeptidase regulator activity | 0.000311 | C3, C5, ITIH2, ITIH4, KNG1, SERPIND1, SERPING1 |
| GO:BP regulation of humoral immune response | 0.000387 | C3, C4BPA, CFH, HPX, SERPING1 |
| GO:BP defense response | 0.000485 | C3, C4BPA, C5, C9, CFB, CFH, CLU, COL6A1, FGA, HPX, ITIH4, KNG1, SERPING1 |

### STRING and hu.MAP

STRING supports a coherent, already known complement and coagulation network. C3 is connected to CFB, CFH, SERPING1, C5, KNG1, CP, HPX, ITIH4, and CLU; C5 is connected to C9 and complement regulators; KNG1 connects complement, coagulation, and protease-regulatory proteins; and FGA connects with KNG1, SERPIND1, ITIH2, HPX, and C9. These relationships are concordant with the primary GO/KEGG interpretation and indicate that the module is not merely an arbitrary correlation cluster. hu.MAP independently places many of the same proteins in multiple plasma-protein and complement/coagulation complexes, especially complexes represented by C3, CFB, C5, KNG1, FGA, HPX, C4BPA, SERPING1, SERPIND1, CFH, ITIH2, and ITIH4 (hu.MAP huMAP3_10678.1) through (hu.MAP huMAP3_09434.1). The repeated recovery of overlapping complex memberships suggests a known extracellular proteome architecture. PLTP, CLU, COL6A1, SLC4A1, and SDR16C5 have weaker or absent hu.MAP support, so their co-abundance may reflect shared sample composition, extracellular association, or tissue-specific covariation rather than membership in a single stable molecular complex.

**STRING interactions (score >= 0.7)**: 33 of 171 gene pairs: C3–C4BPA (0.817); C3–C5 (0.974); C3–CFB (0.999); C3–CFH (0.999); C3–CLU (0.803); C3–CP (0.751); C3–HPX (0.841); C3–ITIH4 (0.745); C3–KNG1 (0.804); C3–SERPING1 (0.954); C5–C9 (0.999); C5–CFB (0.774); C5–CFH (0.824); C5–KNG1 (0.701); C9–CLU (0.797); C9–FGA (0.731); CFB–CFH (0.961); CFB–SERPING1 (0.88); CFH–SERPING1 (0.722); CLU–CP (0.794); CLU–HPX (0.743); CLU–PLTP (0.894); CLU–SERPING1 (0.721); CP–HPX (0.88); FGA–HPX (0.791); FGA–ITIH2 (0.811); FGA–KNG1 (0.908); FGA–SERPIND1 (0.96); HPX–ITIH4 (0.706); ITIH2–SERPIND1 (0.712); ITIH4–KNG1 (0.723); KNG1–SERPIND1 (0.779); KNG1–SERPING1 (0.964)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Bone marrow cell (FDR = 2.18e-15, 15 genes); TISSUES Plasma cell (FDR = 4.11e-14, 14 genes); Component Blood microparticle (FDR = 4.94e-14, 14 genes); COMPARTMENTS Blood microparticle (FDR = 5.19e-14, 14 genes); NetworkNeighborAL Complement and coagulation cascades, and Protein-lipid complex (FDR = 2.4e-13, 13 genes); KEGG Complement and coagulation cascades (FDR = 6.64e-13, 11 genes); TISSUES Bone marrow (FDR = 1.42e-12, 16 genes); Keyword Glycoprotein (FDR = 4.04e-12, 18 genes); Keyword Signal (FDR = 4.04e-12, 17 genes); Keyword Secreted (FDR = 4.04e-12, 16 genes); NetworkNeighborAL Complement and coagulation cascades, and Positive regulation of opsonization (FDR = 5.82e-12, 11 genes); PMID (2022) Construction of 2DE Patterns of Plasma Proteins: Aspect of Potential Tumor Markers. (FDR = 5.93e-11, 14 genes); COMPARTMENTS Extracellular space (FDR = 9.78e-11, 17 genes); TISSUES Skeletal system (FDR = 1.4e-10, 17 genes); COMPARTMENTS Extracellular region (FDR = 2.08e-10, 18 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10678.1 (CP, CFB, C3, C5, KNG1, FGA, HPX, C4BPA, SERPING1, SERPIND1, CFH, ITIH2, ITIH4; 13/71); huMAP3_15040.1 (CP, CFB, C3, KNG1, FGA, HPX, C4BPA, SERPING1, SERPIND1, CFH, ITIH2, ITIH4; 12/64); huMAP3_09531.1 (CP, CFB, C3, C5, KNG1, FGA, HPX, C4BPA, SERPING1, ITIH2, ITIH4; 11/47); huMAP3_10101.1 (CP, CFB, C3, C5, KNG1, FGA, HPX, C4BPA, SERPING1, ITIH2, ITIH4; 11/49); huMAP3_08395.1 (CP, CFB, C3, C5, KNG1, FGA, HPX, C4BPA, ITIH2; 9/43); huMAP3_09273.1 (CP, CFB, KNG1, HPX, C4BPA, SERPING1, ITIH2; 7/28); huMAP3_09434.1 (C3, C5, FGA, SERPIND1, ITIH4; 5/33); huMAP3_02236.1 (CP, KNG1, HPX, ITIH2; 4/7); huMAP3_08796.1 (CFB, C5, C4BPA, ITIH4; 4/15); huMAP3_09832.1 (CFB, C5, C4BPA, ITIH4; 4/18); huMAP3_07432.1 (CP, C3, FGA, HPX; 4/18); huMAP3_07541.1 (C5, KNG1, C4BPA, ITIH2; 4/19); huMAP3_07265.1 (CP, KNG1, HPX, ITIH2; 4/20); huMAP3_08224.1 (C3, C5, FGA, SERPIND1; 4/21); huMAP3_07701.1 (CFB, KNG1, C4BPA, ITIH2; 4/22); huMAP3_07376.1 (C5, C4BPA; 2/4); huMAP3_02811.1 (C5, C4BPA; 2/8); huMAP3_02242.1 (C3, FGA; 2/9); huMAP3_08700.1 (CP, HPX; 2/11)

### Novelty

The biological components and many of their relationships are established rather than novel: complement activation, complement regulation, coagulation, kinin biology, plasma protease inhibition, and extracellular plasma complexes are supported by STRING, hu.MAP, gene annotations, and substantial literature. The potentially new aspect is the reproducible co-abundance of this circulating protein program as a conserved module across cervix_uterine and colon. However, the fact sheet does not provide a direct literature comparison with prior co-abundance studies, so it cannot establish that this tissue-pair module is a new finding. Absence of a relationship from STRING or hu.MAP would not prove novelty, and the present evidence instead supports a cautious conclusion: the pathway biology is well known, while the cross-tissue co-abundance organization may be a useful dataset-specific observation requiring independent replication and adjustment for blood content.

**Hypothesis.** Hypothesis: the conserved module is generated primarily by a shared circulating plasma or blood-microparticle signal entering both tissue sample types. Liver-derived complement, coagulation, kinin, heme-handling, and protease-inhibitory proteins may co-vary in the sampled extracellular fluid, with complement activation and its restraint occurring as a coordinated host-defense state. Erythrocyte-associated SLC4A1, extracellular-matrix-associated COL6A1, and the tissue-associated SDR16C5 may represent secondary contributions from blood, stromal, epithelial, or sample-composition effects. A testable prediction is that module abundance will track independent measures of plasma or erythrocyte contamination and will diminish after adjustment for blood-content markers, while the complement and coagulation proteins will remain tightly correlated in matched plasma or vascular samples.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): SERPING1 (0.91), CFB (0.85), KNG1 (0.85), CP (0.83), COL6A1 (0.83), CLU (0.81); STRING partners: C4BPA (0.817), C5 (0.974), CFB (0.999), CFH (0.999), CLU (0.803), CP (0.751), HPX (0.841), ITIH4 (0.745), KNG1 (0.804), SERPING1 (0.954)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_15040.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_09434.1, huMAP3_07432.1, huMAP3_08224.1, huMAP3_02242.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is the strongest biological anchor of the module: it has a highly connected position in the co-abundance network and links the complement core to CLU, CP, HPX, KNG1, CFB, CFH, SERPING1, and COL6A1. It appears in the primary enrichment terms spanning blood microparticles, complement activation, humoral and innate immunity, extracellular compartments, and immune regulation (GO:CC blood microparticle; q_global = 5.23e-12) through (KEGG Pertussis - Homo sapiens (human); q_global = 0.0488). Established annotation describes C3 as central to classical and alternative complement activation, with inflammatory and antimicrobial products after proteolytic processing. Its extensive disease and literature record, including complement deficiencies, complement-mediated renal disease, atypical hemolytic-uremic syndrome, and macular degeneration, makes it the most informative representative of the module.
- **Conclusion**: Established evidence supports C3 as the central complement component and a principal driver of the module's immune interpretation. Its co-abundance with regulators and downstream complement proteins is consistent with a coordinated circulating complement state. It is not established from these data that C3 is locally produced in cervix_uterine or colon; the HPA pattern instead favors a plasma-derived explanation.

#### CFB

- **Related proteins** (co-abundance neighbors): KNG1 (0.86), C3 (0.85), ITIH2 (0.82), FGA (0.80); STRING partners: C3 (0.999), C5 (0.774), CFH (0.961), SERPING1 (0.88)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_15040.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_09273.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07701.1
- **Function (MyGene.info)**: complement factor B. This gene encodes complement factor B, a component of the alternative pathway of complement activation. Factor B circulates in the blood as a single chain polypeptide. Upon activation of the alternative pathway, it is cleaved by complement factor D yielding the noncatalytic chain Ba and the catalytic subunit Bb. The active subunit Bb is a serine protease which associates with C3b to form the alter…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with B factor anomaly (0.764); atypical hemolytic-uremic syndrome (0.705); Immunodeficiency due to a complement cascade protein anomaly (0.614); paroxysmal nocturnal hemoglobinuria (0.561); complement 3 glomerulopathy (0.546)
- **Europe PMC papers**: 7226
- **Why important**: CFB occupies a connected position linking C3 with KNG1, ITIH2, and FGA, and it has strong STRING support with C3, CFH, C5, and SERPING1. It is present in the primary complement and coagulation, alternative-pathway, extracellular, innate-immune, and defense-response terms (GO:CC blood microparticle; q_global = 5.23e-12), (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 5.47e-12), (GO:BP humoral immune response; q_global = 5.48e-08), (GO:BP complement activation; q_global = 1.57e-07), (GO:BP complement activation, alternative pathway; q_global = 5.76e-06), (GO:BP defense response; q_global = 0.000485), (GO:BP immune effector process; q_global = 0.00078), (GO:BP innate immune response; q_global = 0.00149), and related terms. Its established function as the alternative-pathway factor that forms the C3 convertase makes it mechanistically important. The disease associations with atypical hemolytic-uremic syndrome, complement cascade abnormalities, and paroxysmal nocturnal hemoglobinuria provide clinically relevant support, while its literature volume is substantial.
- **Conclusion**: Established evidence supports CFB as the alternative-pathway arm of the complement signal and as a meaningful connector between complement activation and the broader plasma-protein network. The module does not demonstrate pathway activation directly; it demonstrates coordinated abundance of proteins that participate in that pathway.

#### C5

- **Related proteins** (co-abundance neighbors): ITIH2 (0.84), C9 (0.83); STRING partners: C3 (0.974), C9 (0.999), CFB (0.774), CFH (0.824), KNG1 (0.701)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_09434.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07541.1, huMAP3_08224.1, huMAP3_07376.1, huMAP3_02811.1
- **Function (MyGene.info)**: complement C5. This gene encodes a component of the complement system, a part of the innate immune system that plays an important role in inflammation, host homeostasis, and host defense against pathogens. The encoded preproprotein is proteolytically processed to generate multiple protein products, including the C5 alpha chain, C5 beta chain, C5a anaphylatoxin and C5b. The C5 protein is comprised of the C5 alpha…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.744); paroxysmal nocturnal hemoglobinuria (0.610); myasthenia gravis (0.586); atypical hemolytic-uremic syndrome (0.544); neuromyelitis optica (0.516)
- **Europe PMC papers**: 81450
- **Why important**: C5 is a core complement effector connected to C3, C9, CFB, CFH, and KNG1 and is represented across the primary complement, humoral immune, defense, extracellular, and immune-response terms (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 5.47e-12) through (GO:BP complement activation, classical pathway; q_global = 1.58e-05) and (GO:BP defense response; q_global = 0.000485) through (KEGG Pertussis - Homo sapiens (human); q_global = 0.0488). Its proteolytic products include the inflammatory anaphylatoxin C5a and the terminal complement component that initiates membrane-attack-complex assembly. C5 has extensive disease and literature support involving complement deficiency, paroxysmal nocturnal hemoglobinuria, myasthenia gravis, atypical hemolytic-uremic syndrome, and neuromyelitis optica.
- **Conclusion**: Established evidence supports C5 as the transition from upstream complement activation to inflammatory and terminal complement effector biology. Its relatively limited network degree does not lessen its biological importance, because its position reflects pathway function rather than simple network centrality. The data support association with a complement-rich plasma state, not a claim that terminal complement attack is occurring in either tissue.

#### SERPING1

- **Related proteins** (co-abundance neighbors): C3 (0.91), PLTP (0.82), CP (0.80); STRING partners: C3 (0.954), CFB (0.88), CFH (0.722), CLU (0.721), KNG1 (0.964)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_15040.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_09273.1
- **Function (MyGene.info)**: serpin family G member 1. This gene encodes a highly glycosylated plasma protein involved in the regulation of the complement cascade. Its encoded protein, C1 inhibitor, inhibits activated C1r and C1s of the first complement component and thus regulates complement activation. It is synthesized in the liver, and its deficiency is associated with hereditary angioneurotic oedema (HANE). Alternative splicing results in multipl…
- **Diseases (Open Targets)**: hereditary angioedema with C1Inh deficiency (0.828); hereditary angioedema type 1 (0.750); hereditary angioedema (0.728); angioedema (0.616); hereditary angioedema type 2 (0.614)
- **Europe PMC papers**: 4203
- **Why important**: SERPING1 is a network bridge connecting C3, CFB, CFH, CLU, KNG1, and PLTP. It is repeatedly represented in the primary terms for complement activation, regulation of complement activation, humoral immunity, extracellular space, and peptidase inhibition (GO:CC blood microparticle; q_global = 5.23e-12) through (GO:BP humoral immune response mediated by circulating immunoglobulin; q_global = 1.32e-06), (GO:BP complement activation, classical pathway; q_global = 1.58e-05), (GO:MF endopeptidase inhibitor activity; q_global = 0.000203) through (GO:BP defense response; q_global = 0.000485), and (GO:BP innate immune response; q_global = 0.00149) through (KEGG Pertussis - Homo sapiens (human); q_global = 0.0488). Its established function as C1 inhibitor provides direct mechanistic control of complement and related protease systems. The strong disease associations with hereditary angioedema and C1-inhibitor deficiency, together with a substantial literature record, make it especially important for interpreting the module as a regulated rather than simply activated immune program.
- **Conclusion**: Established evidence supports SERPING1 as a principal counter-regulatory component that balances complement and protease activity. Its co-abundance with both complement effectors and inhibitors is compatible with coordinated production or circulation of a regulated plasma defense system. Whether its abundance reflects compensatory regulation in the tissues cannot be determined from this module alone.

#### KNG1

- **Related proteins** (co-abundance neighbors): PLTP (0.90), CFB (0.86), C3 (0.85), ITIH2 (0.84), C4BPA (0.84), CFH (0.82), ITIH4 (0.81); STRING partners: C3 (0.804), C5 (0.701), FGA (0.908), ITIH4 (0.723), SERPIND1 (0.779), SERPING1 (0.964)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_15040.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_09273.1, huMAP3_02236.1, huMAP3_07541.1, huMAP3_07265.1, huMAP3_07701.1
- **Function (MyGene.info)**: kininogen 1. This gene uses alternative splicing to generate two different proteins- high molecular weight kininogen (HMWK) and low molecular weight kininogen (LMWK). HMWK is essential for blood coagulation and assembly of the kallikrein-kinin system. Also, bradykinin, a peptide causing numerous physiological effects, is released from HMWK. Bradykinin also functions as an antimicrobial peptide with antibacteri…
- **Diseases (Open Targets)**: congenital high-molecular-weight kininogen deficiency (0.733); venous thromboembolism (0.547); hereditary angioedema (0.458); serum lipopolysaccharide activity (0.367); ischemic stroke (0.363)
- **Europe PMC papers**: 2325
- **Why important**: KNG1 has the highest network connectivity and links complement-related proteins with ITIH proteins, PLTP, FGA, and SERPIND1. It is present in the primary extracellular, complement/coagulation, peptidase-inhibitor, and defense terms (GO:CC blood microparticle; q_global = 5.23e-12), (KEGG Complement and coagulation cascades - Homo sapiens (human); q_global = 5.47e-12), (GO:CC endoplasmic reticulum lumen; q_global = 2.31e-05), (GO:MF endopeptidase inhibitor activity; q_global = 0.000203) through (GO:MF endopeptidase regulator activity; q_global = 0.000311), (GO:BP defense response; q_global = 0.000485), (GO:CC extracellular space; q_global = 0.000489), (GO:MF peptidase regulator activity; q_global = 0.000786), (GO:CC extracellular region; q_global = 0.00113), and related terms. Its established biology spans high- and low-molecular-weight kininogen, coagulation, the kallikrein-kinin system, bradykinin release, protease regulation, vasodilation, and antimicrobial activity. The disease associations with kininogen deficiency, venous thromboembolism, hereditary angioedema, and ischemic stroke, alongside a substantial literature record, make it a key integrator of the module.
- **Conclusion**: Established evidence supports KNG1 as a central connector between complement, coagulation, and kinin biology and as a strong marker of a circulating plasma program. Its network position makes it a useful candidate for testing whether the module reflects vascular or blood-derived biology. A direct causal role for KNG1 in the cross-tissue co-abundance pattern remains a hypothesis.

## Module 11

**Tissue pair**: cervix_uterine and colon  
**Genes (5)**: BPI, CTSG, MNDA, MPO, LTF

### Function

The module is most consistent with a neutrophil and myeloid-cell secretory-granule program involved in antimicrobial defense, phagocytosis, and regulation of inflammatory activation. The strongest primary evidence is the enrichment of azurophil granule lumen (GO:CC azurophil granule lumen; q_global = 0.003), secretory granule lumen (GO:CC secretory granule lumen; q_global = 0.00404), vesicle and vacuolar lumen (GO:CC cytoplasmic vesicle lumen; q_global = 0.00404) (GO:CC vesicle lumen; q_global = 0.00417) (GO:CC vacuolar lumen; q_global = 0.0084), primary lysosome (GO:CC primary lysosome; q_global = 0.0117), and phagocytic vesicle lumen (GO:CC phagocytic vesicle lumen; q_global = 0.0127). The biological-process terms support defense against Gram-negative bacteria, fungi, bacterial molecules, and other biotic stimuli (9 globally significant GO/KEGG terms, q_global 0.00335–0.0489; see the table), together with phagocytosis (KEGG Phagocytosis - Homo sapiens (human); q_global = 0.0105). The negative-regulation terms (GO:BP negative regulation of immune system process; q_global = 0.0215) (GO:BP negative regulation of leukocyte activation; q_global = 0.0281) (GO:BP negative regulation of cell activation; q_global = 0.049) suggest that this is not solely a destructive antimicrobial program; it may also include mechanisms that limit leukocyte or immune-cell activation. The near-complete representation of the module in secretory-vesicle terms (GO:CC secretory granule lumen; q_global = 0.00404) (GO:CC secretory granule; q_global = 0.0388) (GO:CC secretory vesicle; q_global = 0.0497) indicates a coordinated granule-associated program rather than an arbitrary set of immune genes.

**Cell composition.** The module is strongly enriched for blood and myeloid-cell markers, especially neutrophil and neutrophil-progenitor signatures. HPA identifies bone marrow enrichment for the module genes and links the genes mainly to neutrophils, monocytes, and their progenitors. Most of the genes are secreted or granule-associated proteins, with LTF and BPI secreted to blood and MPO and CTSG localized to intracellular vesicular compartments. HPA protein staining was absent in cervix_uterine for the module genes and was detected for only a minority of genes in colon, while MNDA was detected in colon. This combination is more compatible with infiltrating or resident immune-cell abundance, or with blood-derived material, than with a protein program intrinsic to the bulk epithelial tissues themselves. The shared cervix_uterine-colon signal may therefore reflect common neutrophil or myeloid-cell content. It could also reflect extracellular granule proteins in tissue or blood, although the lack of tissue protein detection means that transcript-level co-abundance should not automatically be interpreted as local protein activity.

**GO/KEGG enrichment**: 24 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC azurophil granule lumen | 0.003 | BPI, CTSG, MNDA, MPO |
| GO:BP defense response to Gram-negative bacterium | 0.00335 | BPI, CTSG, LTF |
| GO:CC secretory granule lumen | 0.00404 | BPI, CTSG, LTF, MNDA, MPO |
| GO:CC cytoplasmic vesicle lumen | 0.00404 | BPI, CTSG, LTF, MNDA, MPO |
| GO:CC vesicle lumen | 0.00417 | BPI, CTSG, LTF, MNDA, MPO |
| GO:BP defense response to bacterium | 0.00472 | BPI, CTSG, LTF, MPO |
| GO:BP defense response to fungus | 0.00543 | CTSG, LTF, MPO |
| GO:BP response to lipopolysaccharide | 0.00661 | BPI, CTSG, LTF, MPO |
| GO:BP response to fungus | 0.00672 | CTSG, LTF, MPO |
| GO:BP response to molecule of bacterial origin | 0.00793 | BPI, CTSG, LTF, MPO |
| GO:CC vacuolar lumen | 0.0084 | BPI, CTSG, MNDA, MPO |
| KEGG Phagocytosis - Homo sapiens (human) | 0.0105 | BPI, CTSG, LTF, MPO |
| GO:CC primary lysosome | 0.0117 | BPI, CTSG, MNDA, MPO |
| GO:CC azurophil granule | 0.0117 | BPI, CTSG, MNDA, MPO |
| GO:CC phagocytic vesicle lumen | 0.0127 | LTF, MPO |

### STRING and hu.MAP

STRING supports a biologically coherent antimicrobial-granule network. The observed high-confidence relationships connect BPI, LTF, MPO, and CTSG, with particularly strong connectivity among MPO, CTSG, and LTF; these relationships are consistent with their established participation in neutrophil granules and host defense. MNDA has no listed STRING partner in this module, so its placement is not supported by a listed STRING pair, but its myeloid nuclear localization and HPA immune-cell pattern provide independent biological support. hu.MAP identifies several complexes containing combinations of MPO, CTSG, BPI, LTF, and MNDA (hu.MAP huMAP3_10260.1) (hu.MAP huMAP3_11343.1) (hu.MAP huMAP3_13546.1) (hu.MAP huMAP3_03846.1). The complexes include additional neutrophil and myeloid proteins such as ELANE, ITGAM, MMP8, PRTN3, and LYZ. Thus, the network is substantially supported by previously characterized protein associations and complex membership. The co-abundance module appears to recover a known neutrophil granule and myeloid-cell neighborhood, rather than revealing an isolated molecular relationship.

**STRING interactions (score >= 0.7)**: 6 of 10 gene pairs: BPI–CTSG (0.959); BPI–LTF (0.96); BPI–MPO (0.995); CTSG–LTF (0.997); CTSG–MPO (0.999); LTF–MPO (0.998)
**STRING functional enrichment (supplementary, within-query FDR)**: PMID (2009) Neutrophil extracellular traps contain calprotectin, a cytosolic protein complex involved in host defense against Candida albicans. (FDR = 1.39e-05, 5 genes); PMID (1998) Clinical and immunological study of 7 patients with minocycline-induced autoimmune phenomena. (FDR = 0.0003, 4 genes); Keyword Antibiotic (FDR = 0.00034, 3 genes); PMID (2025) Prevalence and clinical implications of major and minor ANCAs in Tunisian (North African) patients with systemic lupus erythematosus. (FDR = 0.00036, 4 genes); PMID (2024) Association of atypical anti-neutrophil cytoplasmic antibody with comorbidities and outcome in a hospital-based population. (FDR = 0.00036, 4 genes); PMID (2023) A rare case of vasculitis in cystic fibrosis: A clinical case. (FDR = 0.00036, 4 genes); PMID (2023) Rat bite fever mimicking ANCA-associated vasculitis. (FDR = 0.00036, 4 genes); PMID (2023) Interference of anti-nuclear antibodies on determination of anti-neutrophil cytoplasmic antibodies in patients suspected of vasculitis: a case series. (FDR = 0.00036, 4 genes); PMID (2023) The Role of Neutrophils in ANCA-Associated Vasculitis: The Pathogenic Role and Diagnostic Utility of Autoantibodies. (FDR = 0.00036, 4 genes); PMID (2022) Level and avidity of antineutrophil cytoplasmic antibodies specific to lactoferrin are useful biomarkers in systemic lupus erythematosus. (FDR = 0.00036, 4 genes); PMID (2022) Neutrophils, Cancer and Thrombosis: The New Bermuda Triangle in Cancer Research. (FDR = 0.00036, 4 genes); PMID (2022) Neutrophil extracellular traps in chronic lung disease: implications for pathogenesis and therapy. (FDR = 0.00036, 4 genes); PMID (2022) Dual-Positive MPO- and PR3-ANCA-Associated Vasculitis Following SARS-CoV-2 mRNA Booster Vaccination: A Case Report and Systematic Review. (FDR = 0.00036, 4 genes); PMID (2022) Microenvironmental Landscape of Human Melanoma Brain Metastases in Response to Immune Checkpoint Inhibition. (FDR = 0.00036, 4 genes); PMID (2022) A rare case of Immunoglobulin A dominant post-infectious glomerulonephritis (IgA PIGN) in a young patient. (FDR = 0.00036, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10260.1 (MPO, CTSG, BPI, MNDA; 4/14); huMAP3_11343.1 (LTF, MPO, CTSG, MNDA; 4/54); huMAP3_13546.1 (MPO, CTSG, MNDA; 3/8); huMAP3_03846.1 (MPO, CTSG; 2/2)

### Novelty

This is not a new discovery of the individual gene functions or of the core protein relationships: the antimicrobial, neutrophil-granule, lysosomal, and myeloid associations are already supported by the globally corrected GO/KEGG results, STRING relationships, hu.MAP complexes, HPA expression patterns, disease annotations, and substantial literature. The potentially distinctive observation is the shared co-abundance of this entire program in cervix_uterine and colon. However, the fact sheet does not establish that this tissue-pair module has never been reported, and absence of a relationship from STRING or hu.MAP would not prove novelty. The most defensible conclusion is that the module may represent a tissue-pair-specific or dataset-specific recurrence of a known neutrophil/myeloid program, with novelty at the context or co-abundance level remaining unproven.

**Hypothesis.** Hypothesis: the shared module reflects variation in neutrophil or related myeloid-cell abundance, activation, or granule release across cervix_uterine and colon samples. In this model, BPI and LTF contribute antimicrobial and lipopolysaccharide-binding activity, MPO generates microbicidal oxidants, CTSG contributes proteolytic antimicrobial and inflammatory effects, and MNDA represents the myeloid nuclear and differentiation component. Coordinated expression could arise when tissue immune-cell infiltration or blood contamination changes across samples. A further possibility is that local microbial exposure or mucosal inflammation drives both the abundance of these cells and their granule program. This remains a hypothesis because the module data do not by themselves distinguish altered cell composition from coordinated regulation within resident or infiltrating cells, nor do they demonstrate protein release or enzymatic activity in either tissue.

### Important genes

#### MPO

- **Related proteins** (co-abundance neighbors): MNDA (0.86), CTSG (0.85); STRING partners: BPI (0.995), CTSG (0.999), LTF (0.998)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10260.1, huMAP3_11343.1, huMAP3_13546.1, huMAP3_03846.1
- **Function (MyGene.info)**: myeloperoxidase. Myeloperoxidase (MPO) is a heme protein synthesized during myeloid differentiation that constitutes the major component of neutrophil azurophilic granules. Produced as a single chain precursor, myeloperoxidase is subsequently cleaved into a light and heavy chain. The mature myeloperoxidase is a tetramer composed of 2 light chains and 2 heavy chains. This enzyme produces hypohalous acids central to…
- **Diseases (Open Targets)**: myeloperoxidase deficiency (0.767); Alzheimer disease type 1 (0.485); multiple system atrophy (0.286); amyotrophic lateral sclerosis (0.242); Alzheimer disease (0.146)
- **Europe PMC papers**: 36383
- **Why important**: MPO is a central mechanistic marker of the module: it participates in the module's antimicrobial, granule, lysosomal, phagocytic, and bacterial or fungal defense terms (20 globally significant GO/KEGG terms, q_global 0.003–0.0497; see the table). It occupies several hu.MAP complexes (hu.MAP huMAP3_10260.1) (hu.MAP huMAP3_11343.1) (hu.MAP huMAP3_13546.1) (hu.MAP huMAP3_03846.1) and has strong STRING relationships with BPI, CTSG, and LTF. HPA places it in bone marrow and myeloid progenitor populations, with vesicular localization. Its established role is the production of microbicidal hypohalous acids in neutrophil granules, and its disease associations include MPO deficiency and neurodegenerative conditions. It also has a very large literature base.
- **Conclusion**: Established evidence supports MPO as a core neutrophil-granule effector and one of the strongest functional anchors of the module. The module data support interpreting MPO as a marker of myeloid granule biology, but they do not prove that MPO enzymatic activity or oxidant production is occurring in the sampled tissues.

#### CTSG

- **Related proteins** (co-abundance neighbors): MPO (0.85), LTF (0.85); STRING partners: BPI (0.959), LTF (0.997), MPO (0.999)
- **HPA**: Tissue enriched; Group enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10260.1, huMAP3_11343.1, huMAP3_13546.1, huMAP3_03846.1
- **Function (MyGene.info)**: cathepsin G. The protein encoded by this gene, a member of the peptidase S1 protein family, is found in azurophil granules of neutrophilic polymorphonuclear leukocytes. The encoded protease has a specificity similar to that of chymotrypsin C, and may participate in the killing and digestion of engulfed pathogens, and in connective tissue remodeling at sites of inflammation. In addition, the encoded protein is …
- **Diseases (Open Targets)**: tuberculosis (0.374); ptosis (0.180); neoplasm (0.103); colorectal carcinoma (0.095); non-small cell lung carcinoma (0.093)
- **Europe PMC papers**: 4011
- **Why important**: CTSG is highly integrated with the antimicrobial core through STRING links to BPI, LTF, and MPO and through all listed hu.MAP complexes (hu.MAP huMAP3_10260.1) (hu.MAP huMAP3_11343.1) (hu.MAP huMAP3_13546.1) (hu.MAP huMAP3_03846.1). It contributes to the azurophil-granule, lysosomal, phagocytic, bacterial-defense, fungal-defense, and immune-regulatory terms (24 globally significant GO/KEGG terms, q_global 0.003–0.0497; see the table). HPA associates it with bone marrow, neutrophil progenitors, and mast cells. Its established function is a neutrophil azurophil-granule protease involved in antimicrobial killing, digestion of engulfed pathogens, and inflammatory tissue remodeling. Its literature and disease annotation support broad relevance to infection and inflammation.
- **Conclusion**: Established evidence supports CTSG as a core granule protease that links antimicrobial defense with inflammatory remodeling. A module-level hypothesis is that CTSG co-abundance marks activated or accumulated granule-rich myeloid cells, but the data do not establish whether its protease activity is increased.

#### LTF

- **Related proteins** (co-abundance neighbors): CTSG (0.85), BPI (0.80), MNDA (0.80); STRING partners: BPI (0.96), CTSG (0.997), MPO (0.998)
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11343.1
- **Function (MyGene.info)**: lactotransferrin. This gene is a member of the transferrin family of genes and its protein product is found in the secondary granules of neutrophils. The protein is a major iron-binding protein in milk and body secretions with an antimicrobial activity, making it an important component of the non-specific immune system. The protein demonstrates a broad spectrum of properties, including regulation of iron homeostasi…
- **Diseases (Open Targets)**: tuberculosis (0.517); AL amyloidosis (0.467); Abnormality of the skeletal system (0.435); schizophrenia (0.235); inflammatory bowel disease (0.218)
- **Europe PMC papers**: 7000
- **Why important**: LTF has the strongest network integration in the module by weighted connectivity and links to CTSG, BPI, and MNDA, while also appearing in many of the primary defense and secretory-compartment terms (18 globally significant GO/KEGG terms, q_global 0.00335–0.0497; see the table). HPA identifies bone marrow, neutrophil progenitor, neutrophil, and monocyte associations, and classifies the protein as secreted to blood. Its established function includes iron binding, antimicrobial activity, mucosal innate defense, and regulation of inflammatory responses. It has extensive literature and disease associations including inflammatory bowel disease and tuberculosis.
- **Conclusion**: Established evidence supports LTF as both a secretory antimicrobial effector and a plausible indicator of mucosal or circulating myeloid-cell activity. Its co-abundance with the granule enzymes could reflect coordinated neutrophil content or secretion, but the tissue data do not determine whether LTF is being produced locally or delivered from blood or infiltrating cells.

#### BPI

- **Related proteins** (co-abundance neighbors): LTF (0.80); STRING partners: CTSG (0.959), LTF (0.96), MPO (0.995)
- **HPA**: Tissue enriched; Group enriched; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10260.1
- **Function (MyGene.info)**: bactericidal permeability increasing protein. This gene encodes a lipopolysaccharide binding protein. It is associated with human neutrophil granules and has antimicrobial activity against gram-negative organisms. [provided by RefSeq, Nov 2014].
- **Diseases (Open Targets)**: retinal degeneration (0.297); alcohol drinking (0.266); asthma (0.251); acute tonsillitis (0.243); infection (0.091)
- **Europe PMC papers**: 241427
- **Why important**: BPI is the module's most direct Gram-negative defense marker. It appears in the globally corrected Gram-negative bacterial-defense and bacterial-response terms (16 globally significant GO/KEGG terms, q_global 0.003–0.0497; see the table) and is strongly connected in STRING to MPO, CTSG, and LTF. hu.MAP places it with MPO, CTSG, and MNDA (hu.MAP huMAP3_10260.1). HPA associates it with bone marrow, neutrophil progenitors, classical monocytes, and neutrophils, and identifies it as secreted to blood. Its established function is binding bacterial lipopolysaccharide and contributing to antimicrobial activity and suppression of inflammatory cytokine production. It has a particularly large literature base and multiple infection- and inflammation-related associations.
- **Conclusion**: Established evidence supports BPI as a defining antimicrobial and endotoxin-response component of the module. Its presence strengthens the interpretation of bacterial-defense biology, while its blood-secreted character also strengthens the possibility that the shared tissue signal reflects myeloid-cell abundance or blood-derived material rather than tissue-cell expression alone.

#### MNDA

- **Related proteins** (co-abundance neighbors): MPO (0.86), LTF (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_10260.1, huMAP3_11343.1, huMAP3_13546.1
- **Function (MyGene.info)**: myeloid cell nuclear differentiation antigen. The myeloid cell nuclear differentiation antigen (MNDA) is detected only in nuclei of cells of the granulocyte-monocyte lineage. A 200-amino acid region of human MNDA is strikingly similar to a region in the proteins encoded by a family of interferon-inducible mouse genes, designated Ifi-201, Ifi-202, and Ifi-203, that are not regulated in a cell- or tissue-specific fashion. The 1.8-kb MNDA mRNA, …
- **Diseases (Open Targets)**: COVID-19 (0.221); type 1 diabetes mellitus (0.158); autosomal dominant macrothrombocytopenia (0.082); hereditary thrombocytopenia with normal platelets (0.075); Thrombocytopenia (0.072)
- **Europe PMC papers**: 1563
- **Why important**: MNDA provides a complementary, non-secreted myeloid component. It is present in the azurophil and secretory-compartment terms and in the negative-regulation-of-immune-activation terms (15 globally significant GO/KEGG terms, q_global 0.003–0.0497; see the table). It participates in several hu.MAP complexes (hu.MAP huMAP3_10260.1) (hu.MAP huMAP3_11343.1) (hu.MAP huMAP3_13546.1), despite having no listed STRING partner in the module. HPA links it to bone marrow, lymphoid tissue, neutrophils, monocytes, and dendritic-cell-related populations, with nucleoplasmic localization and protein detection in colon. Its established biology places it in granulocyte-monocyte lineage cells and connects it with innate immune activation, interferon response, DNA damage response, apoptosis, and regulation of B-cell proliferation. Its literature volume is smaller than that of the major granule proteins but remains substantial.
- **Conclusion**: Established evidence supports MNDA as a myeloid-lineage and nuclear-regulatory component that helps distinguish the module from a purely secreted antimicrobial protein set. Its presence is compatible with changes in myeloid-cell composition or state, but the module cannot determine whether MNDA actively regulates the accompanying granule program.

## Module 12

**Tissue pair**: cervix_uterine and colon  
**Genes (8)**: DCAF13, DDX21, LMNB1, NOP56, RRP12, PDCD11, ZFR, ZNF326

### Function

The module is most strongly interpreted as a nucleolar ribosome-biogenesis and pre-rRNA-processing module. The primary evidence is the convergence of small-subunit processome enrichment (GO:CC small-subunit processome; q_global = 0.00494), rRNA processing (GO:BP rRNA processing; q_global = 0.0185), rRNA metabolic process (GO:BP rRNA metabolic process; q_global = 0.0341), preribosome (GO:CC preribosome; q_global = 0.0371), and nucleic-acid binding (GO:MF nucleic acid binding; q_global = 0.0393). DCAF13, NOP56, and PDCD11 support the small-subunit processome and preribosome signals, while DDX21 adds a directly relevant RNA-helicase component to rRNA processing. The module therefore appears to capture coordinated production, maturation, modification, and handling of ribosomal RNA, with additional RNA-processing and nuclear structural functions represented by the remaining genes. The STRING results independently reinforce preribosome, ribosome biogenesis, rRNA processing, and nuclear RNA-processing interpretations (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 0.00032) through (STRING Function Nucleic acid binding; within-query FDR = 0.0393).

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly nuclear, nucleolar, or nuclear-envelope localized. Most genes have low tissue specificity and low immune-cell specificity, which is consistent with a broadly deployed cellular program rather than a tissue-restricted signature. HPA nevertheless shows cell-type-enhanced patterns for several genes and tissue enrichment for LMNB1 and RRP12 in bone marrow-related contexts, with RRP12 also enhanced in neutrophil-related cell types. Thus, a shared cell-state or cellular-composition contribution cannot be excluded, but the available evidence does not support interpreting the module primarily as a blood-cell or plasma-protein signature. Protein detection in both cervix and colon for most assayed genes is compatible with a conserved intracellular program in both tissues.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC small-subunit processome | 0.00494 | DCAF13, NOP56, PDCD11 |
| GO:BP rRNA processing | 0.0185 | DCAF13, DDX21, NOP56, PDCD11 |
| GO:BP rRNA metabolic process | 0.0341 | DCAF13, DDX21, NOP56, PDCD11 |
| GO:CC preribosome | 0.0371 | DCAF13, NOP56, PDCD11 |
| GO:MF nucleic acid binding | 0.0393 | DCAF13, DDX21, LMNB1, NOP56, PDCD11, RRP12, ZFR, ZNF326 |

### STRING and hu.MAP

STRING contains high-confidence relationships among the core nucleolar genes, especially DCAF13 with NOP56 and PDCD11, NOP56 with PDCD11 and RRP12, and DDX21 with NOP56. These relationships agree with the primary GO interpretation and indicate that the central ribosome-biogenesis signal is already represented in known functional association data. RRP12 connects the core through several high-confidence STRING relationships. By contrast, ZNF326 and ZFR have no listed STRING partners within this module, and LMNB1 also has no listed STRING partners, suggesting that their co-abundance links may reflect broader RNA-processing, nuclear, or structural context rather than a documented direct interaction. hu.MAP identifies ZNF326 and ZFR together in two large RNA-binding or RNA-processing complexes (hu.MAP huMAP3_07581.1) and (hu.MAP huMAP3_10625.1). These complexes support an RNA-associated interpretation, but the module includes only a small part of each complex and therefore does not establish that the entire module is one physical complex.

**STRING interactions (score >= 0.7)**: 7 of 28 gene pairs: DCAF13–NOP56 (0.998); DCAF13–PDCD11 (0.994); DCAF13–RRP12 (0.762); DDX21–NOP56 (0.811); NOP56–PDCD11 (0.997); NOP56–RRP12 (0.938); PDCD11–RRP12 (0.984)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 0.00032, 5 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 0.0014, 4 genes); Process rRNA processing (FDR = 0.002, 5 genes); Component Small-subunit processome (FDR = 0.0055, 3 genes); RCTM rRNA modification in the nucleus and cytosol (FDR = 0.0059, 3 genes); RCTM Major pathway of rRNA processing in the nucleolus and cytosol (FDR = 0.0059, 4 genes); Keyword Isopeptide bond (FDR = 0.0067, 7 genes); Keyword rRNA processing (FDR = 0.0089, 3 genes); Keyword Ubl conjugation (FDR = 0.0089, 7 genes); Process RNA processing (FDR = 0.0151, 6 genes); Keyword Nucleus (FDR = 0.0193, 8 genes); NetworkNeighborAL Small-subunit processome, and Positive regulation of rRNA processing (FDR = 0.0214, 2 genes); Function Nucleic acid binding (FDR = 0.0393, 8 genes); NetworkNeighborAL Mixed, incl. Hypotrichosis 11, and Suppressor of forked (FDR = 0.0466, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07581.1 (ZNF326, ZFR; 2/21); huMAP3_10625.1 (ZNF326, ZFR; 2/57)

### Novelty

The module is not wholly a new biological pathway: its core interpretation is supported by established ribosome-biogenesis knowledge, strong STRING associations, and globally corrected GO terms. The co-abundance observation may nevertheless be a new tissue-pair-level finding because the fact sheet does not establish that this exact conserved cervix-colon module, its particular gene combination, or its network organization has previously been reported. The absence of some genes from STRING or hu.MAP should not be treated as proof of novelty. A defensible novelty claim is therefore limited to the reproducible cross-tissue co-abundance pattern and its specific combination of a known nucleolar core with less directly connected RNA-binding and nuclear-envelope genes; confirmation would require comparison with prior tissue co-expression studies and independent datasets.

**Hypothesis.** Hypothesis: in both cervix and colon, the module reflects coordinated demand for nucleolar ribosome production and RNA maturation, with DCAF13, NOP56, PDCD11, DDX21, and RRP12 forming the functional core. ZNF326 and ZFR may couple RNA-associated regulation or processing to this core, while LMNB1 may reflect nuclear-envelope or cell-state context that influences the abundance of the broader nuclear program. The shared signal could therefore arise from a conserved proliferative, biosynthetic, or differentiation-related state rather than from a tissue-specific pathway. This remains a hypothesis because co-abundance does not prove physical interaction, causal regulation, or a common cellular origin.

### Important genes

#### PDCD11

- **Related proteins** (co-abundance neighbors): DDX21 (0.87), DCAF13 (0.84), ZNF326 (0.83), NOP56 (0.81); STRING partners: DCAF13 (0.994), NOP56 (0.997), RRP12 (0.984)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 11. PDCD11 is a NF-kappa-B (NFKB1; 164011)-binding protein that colocalizes with U3 RNA (MIM 180710) in the nucleolus and is required for rRNA maturation and generation of 18S rRNA (Sweet et al., 2003 [PubMed 14624448]; Sweet et al., 2008 [PubMed 17654514]).[supplied by OMIM, Oct 2008].
- **Diseases (Open Targets)**: Back pain (0.277); insomnia (0.216); systemic lupus erythematosus (0.170); neoplasm (0.095); colorectal carcinoma (0.093)
- **Europe PMC papers**: 334
- **Why important**: PDCD11 has the highest network connectivity in the module and connects to DDX21, DCAF13, ZNF326, and NOP56. It is present in every globally corrected GO term (GO:CC small-subunit processome; q_global = 0.00494) through (GO:MF nucleic acid binding; q_global = 0.0393) and in nearly all relevant STRING annotations, including small-subunit processome and rRNA processing. Its nucleolar-rim localization and established role in U three RNA-associated rRNA maturation make it a central mechanistic anchor. The literature supports substantial study, and disease associations include systemic lupus erythematosus, neoplasm, and colorectal carcinoma.
- **Conclusion**: Established evidence supports PDCD11 as a central nucleolar rRNA-maturation component and a major driver of the module interpretation. Its network position makes it a strong candidate for representing the shared functional core. It is not established that PDCD11 initiates the cross-tissue co-abundance pattern or links directly to ZNF326 in vivo.

#### NOP56

- **Related proteins** (co-abundance neighbors): PDCD11 (0.81); STRING partners: DCAF13 (0.998), DDX21 (0.811), PDCD11 (0.997), RRP12 (0.938)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP56 ribonucleoprotein. Nop56p is a yeast nucleolar protein that is part of a complex with the nucleolar proteins Nop58p and fibrillarin. Nop56p is required for assembly of the 60S ribosomal subunit and is involved in pre-rRNA processing. The protein encoded by this gene is similar in sequence to Nop56p and is also found in the nucleolus. Expansion of a GGCCTG repeat from 3-8 copies to 1500-2500 copies in an intron of th…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 36 (0.586); neurodegenerative disease (0.495); ovarian neoplasm (0.272); hereditary disease (0.193); cerebellar ataxia (0.121)
- **Europe PMC papers**: 1517
- **Why important**: NOP56 is present in every globally corrected GO term (GO:CC small-subunit processome; q_global = 0.00494) through (GO:MF nucleic acid binding; q_global = 0.0393) and has strong STRING relationships with DCAF13, DDX21, PDCD11, and RRP12. It is a nucleolar fibrillar-center protein involved in pre-rRNA processing, rRNA modification, maturation of the small ribosomal subunit, and ribosomal biogenesis. Its extensive literature and association with spinocerebellar ataxia type thirty-six make it both a mechanistically informative and clinically established gene.
- **Conclusion**: Established evidence identifies NOP56 as a core ribosome-biogenesis and rRNA-processing component, strongly corroborated by both enrichment and network evidence. Its presence is sufficient to support a nucleolar interpretation, but the module does not demonstrate that disease-associated NOP56 variation explains the tissue-pair co-abundance.

#### DCAF13

- **Related proteins** (co-abundance neighbors): PDCD11 (0.84), RRP12 (0.84), DDX21 (0.81); STRING partners: NOP56 (0.998), PDCD11 (0.994), RRP12 (0.762)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DDB1 and CUL4 associated factor 13. Enables estrogen receptor binding activity. Predicted to be involved in maturation of SSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Located in several cellular components, including centrosome; cytosol; and nuclear lumen. Part of Cul4-RING E3 ubiquitin ligase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.285); acute tonsillitis (0.133); breast cancer (0.105); breast carcinoma (0.099); hepatocellular carcinoma (0.087)
- **Europe PMC papers**: 311
- **Why important**: DCAF13 has high connectivity to PDCD11, RRP12, and DDX21 and is present in every globally corrected GO term (GO:CC small-subunit processome; q_global = 0.00494) through (GO:MF nucleic acid binding; q_global = 0.0393). It is annotated as part of a Cul four RING E three ubiquitin-ligase complex and is predicted to participate in maturation of the small ribosomal subunit. It is detected in both tissues and has substantial literature, with reported associations spanning neurodegenerative disease and several cancers.
- **Conclusion**: Established evidence supports DCAF13 as a bridge between ubiquitin-related regulation and nucleolar rRNA maturation. Its central position suggests that it may coordinate or stabilize the core module, but a regulatory role in the observed cross-tissue co-abundance remains hypothetical.

#### DDX21

- **Related proteins** (co-abundance neighbors): PDCD11 (0.87), DCAF13 (0.81), ZNF326 (0.80); STRING partners: NOP56 (0.811)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 connects to PDCD11, DCAF13, ZNF326, and NOP56 and contributes directly to the globally corrected rRNA-processing and rRNA-metabolism terms (GO:BP rRNA processing; q_global = 0.0185) and (GO:BP rRNA metabolic process; q_global = 0.0341). It is a DEAD-box RNA helicase associated with alteration of RNA structure and is localized at the nucleolar rim and mitotic chromosome. It has the largest literature volume among the module genes and disease associations including colorectal carcinoma and other cancers.
- **Conclusion**: Established evidence supports DDX21 as an RNA-remodelling component that is functionally compatible with rRNA maturation and ribosome assembly. Its connection to ZNF326 suggests a possible interface between nucleolar RNA processing and broader nuclear RNA regulation, but that interface is not demonstrated as a direct physical mechanism here.

#### RRP12

- **Related proteins** (co-abundance neighbors): DCAF13 (0.84); STRING partners: DCAF13 (0.762), NOP56 (0.938), PDCD11 (0.984)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal RNA processing 12 homolog. Enables RNA binding activity. Predicted to be involved in rRNA processing. Located in cytosol; nucleolus; and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.435); bilateral striopallidodentate calcinosis (0.370); colorectal carcinoma (0.079); hepatocellular carcinoma (0.075); neoplasm (0.067)
- **Europe PMC papers**: 367
- **Why important**: RRP12 is connected by STRING to DCAF13, NOP56, and PDCD11 and is repeatedly represented in the supplementary ribosome-biogenesis and rRNA-processing terms (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 0.00032) through (STRING Process RNA processing; within-query FDR = 0.0151). It is annotated as an RNA-binding protein involved in rRNA processing and is localized partly to the nucleolus. HPA shows group enrichment in bone marrow and skeletal muscle and immune-cell enhancement in neutrophil-related cell types, making it informative for evaluating possible cellular-composition contributions.
- **Conclusion**: Established evidence supports RRP12 as a ribosome-biogenesis-associated RNA-binding component linked to the module core. Its HPA pattern raises a composition or cell-state hypothesis, particularly for samples containing myeloid-related cells, but the fact sheet does not establish that blood-cell abundance drives the shared module.

#### ZNF326

- **Related proteins** (co-abundance neighbors): PDCD11 (0.83), ZFR (0.82), LMNB1 (0.82), DDX21 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_07581.1, huMAP3_10625.1
- **Function (MyGene.info)**: zinc finger protein 326. Enables RNA polymerase II complex binding activity. Involved in regulation of DNA-templated transcription, elongation and regulation of RNA splicing. Located in nucleoplasm. Part of DBIRD complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: ocular hypotension (0.227); insomnia (0.222); adolescent idiopathic scoliosis (0.207); juvenile dermatomyositis (0.205); major depressive disorder (0.205)
- **Europe PMC papers**: 258
- **Why important**: ZNF326 has high network connectivity despite lacking listed STRING partners within the module. It is linked to ZFR in both hu.MAP complexes (hu.MAP huMAP3_07581.1) and (hu.MAP huMAP3_10625.1), is annotated for RNA-splicing and transcriptional-elongation regulation, and is detected in colon. Its nucleoplasmic localization and connection to DDX21, PDCD11, and LMNB1 make it a plausible peripheral or bridging component between the nucleolar core and broader nuclear RNA regulation.
- **Conclusion**: Established evidence supports ZNF326 as a nuclear RNA-processing and transcription-associated protein that participates in larger RNA-binding complexes. Its placement in this module may indicate coupling to the ribosome-biogenesis program, but that coupling is a hypothesis rather than a demonstrated direct interaction.

## Module 13

**Tissue pair**: cervix_uterine and colon  
**Genes (6)**: FN1, IFI30, KRT15, LGALS1, LCP1, SOD2

### Function

The strongest supported interpretation is a fibroblast-associated tissue-remodelling and stress-response module. The primary evidence is (GO:BP regulation of fibroblast proliferation; q_global = 0.014) and (GO:BP fibroblast proliferation; q_global = 0.0228), both of which identify fibroblast proliferation or its regulation and both include FN1, IFI30, and SOD2. FN1 provides an extracellular-matrix and cell-adhesion link; SOD2 provides mitochondrial oxidative-stress handling; IFI30 provides antigen-processing activity in antigen-presenting cells. KRT15 adds an epithelial intermediate-filament and wound-healing component, while LGALS1 links cell-matrix interactions with proliferation and apoptosis. LCP1 contributes actin organisation, cell migration, and wound-healing biology. Thus, the module is most consistent with coordinated epithelial, stromal, immune, and oxidative-stress biology rather than a narrowly defined molecular complex. No STRING functional enrichment was reported, and no additional GO or KEGG interpretation should be assigned from nominal or within-module results.

**Cell composition.** The module is compositionally mixed. HPA annotates most genes as tissue enhanced and most as cell-type enhanced, with recurring associations to monocytes, fibroblasts, smooth-muscle cells, hepatic stellate cells, and extravillous trophoblasts. IFI30 has a particularly clear antigen-presenting and monocyte association, while LCP1 is associated with hematopoietic and myeloid lineages. FN1 and LGALS1 are secreted to blood, and the module therefore contains a substantial extracellular or circulating-protein component, but secreted proteins are not the majority. KRT15 is associated with basal epithelial cells, and SOD2 with monocytes and neutrophils. The shared signal between cervix and colon could consequently reflect conserved stromal or epithelial repair biology, immune-cell admixture, or both, rather than expression by one uniform cell population. Protein detection also differs between tissues for several genes, so co-abundance should not be interpreted as equivalent protein abundance in every constituent cell type.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulation of fibroblast proliferation | 0.014 | FN1, IFI30, SOD2 |
| GO:BP fibroblast proliferation | 0.0228 | FN1, IFI30, SOD2 |

### STRING and hu.MAP

The only high-confidence STRING relationship within the module is FN1--LGALS1, supporting a known extracellular-matrix or cell-matrix association. The other module relationships are not represented as high-confidence STRING links in the supplied evidence. No hu.MAP complex contains multiple module members. This pattern argues against the module being a canonical stable protein complex. Instead, the co-abundance structure is more compatible with coordinated expression across interacting tissue processes, cellular states, or sample composition. The absence of STRING functional enrichment further limits claims of a well-established shared pathway.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: FN1–LGALS1 (0.878)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact cross-tissue co-abundance module appears potentially novel in this dataset because the supplied evidence identifies a tissue-pair module but does not report a matching hu.MAP complex or broad STRING interaction or enrichment pattern. However, it cannot be called a wholly new biological mechanism. FN1, LGALS1, SOD2, IFI30, KRT15, and LCP1 each have established functions, and the FN1--LGALS1 relationship is already known. The appropriate conclusion is that the specific conserved co-abundance arrangement and its shared cervix-colon context may be a new observation, while its component biology is largely established. Absence from STRING or hu.MAP alone is not evidence of novelty.

**Hypothesis.** Hypothesis: the module marks a conserved repair or remodelling state in which epithelial structural activity is coupled to extracellular-matrix deposition, fibroblast-associated proliferation, oxidative stress control, and local antigen processing. KRT15 may represent the epithelial structural component; FN1 and LGALS1 may organise matrix and cell-matrix signalling; SOD2 may buffer mitochondrial oxidative stress; and IFI30 and LCP1 may reflect antigen-presenting or myeloid and cytoskeletal participation. An alternative or complementary explanation is shared variation in stromal and immune-cell abundance across cervix and colon samples. This is a mechanistic hypothesis, not a demonstrated causal pathway.

### Important genes

#### FN1

- **Related proteins** (co-abundance neighbors): KRT15 (0.83); STRING partners: LGALS1 (0.878)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 is one of the genes in both primary globally corrected terms, (GO:BP regulation of fibroblast proliferation; q_global = 0.014) and (GO:BP fibroblast proliferation; q_global = 0.0228). It is a major extracellular-matrix and cell-adhesion protein involved in migration, wound healing, coagulation, and integrin-mediated signalling. It is associated with fibroblasts, hepatic stellate cells, extravillous trophoblasts, and blood-vessel or liver-enriched tissue contexts. Its connection to LGALS1 is the sole high-confidence STRING relationship within the module. FN1 also has extensive literature and multiple disease associations, making it the strongest extracellular and stromal anchor.
- **Conclusion**: Established evidence supports FN1 as a central matrix-remodelling and fibroblast-associated component of the module. It is plausible, but unproven, that FN1 helps connect the epithelial, stromal, and repair-related signals.

#### SOD2

- **Related proteins** (co-abundance neighbors): KRT15 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Mitochondria; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: superoxide dismutase 2. This gene is a member of the iron/manganese superoxide dismutase family. It encodes a mitochondrial protein that forms a homotetramer and binds one manganese ion per subunit. This protein binds to the superoxide byproducts of oxidative phosphorylation and converts them to hydrogen peroxide and diatomic oxygen. Mutations in this gene have been associated with idiopathic cardiomyopathy (IDC), premat…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); diabetic retinopathy (0.379); malunion fracture (0.295); coronary artery disorder (0.267); prostate carcinoma (0.227)
- **Europe PMC papers**: 28293
- **Why important**: SOD2 is included in both primary terms, (GO:BP regulation of fibroblast proliferation; q_global = 0.014) and (GO:BP fibroblast proliferation; q_global = 0.0228), and encodes a mitochondrial enzyme that converts superoxide into hydrogen peroxide and oxygen. It is detected in both tissues and is associated with bone marrow, monocytes, neutrophils, hypoxia response, and oxidative-stress biology. Its position is peripheral in the supplied network, but its annotation provides an important functional bridge between tissue remodelling and cellular stress. It has a large literature base and disease associations including cancer and cardiometabolic or vascular conditions.
- **Conclusion**: Established evidence supports SOD2 as an oxidative-stress component of the module and as a co-member of the fibroblast-related enrichment. Its participation does not establish that oxidative stress causes the co-abundance pattern.

#### IFI30

- **Related proteins** (co-abundance neighbors): KRT15 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Group enriched; location Vesicles, Cytosol; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IFI30 lysosomal thiol reductase. The protein encoded by this gene is a lysosomal thiol reductase that at low pH can reduce protein disulfide bonds. The enzyme is expressed constitutively in antigen-presenting cells and induced by gamma-interferon in other cell types. This enzyme has an important role in MHC class II-restricted antigen processing. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.454); health study participation (0.272); movement disorder (0.194); cholestasis, intrahepatic, of pregnancy 3 (0.173); Intrahepatic cholestasis of pregnancy (0.161)
- **Europe PMC papers**: 1626
- **Why important**: IFI30 is included in both primary terms, (GO:BP regulation of fibroblast proliferation; q_global = 0.014) and (GO:BP fibroblast proliferation; q_global = 0.0228). It is a lysosomal thiol reductase expressed constitutively in antigen-presenting cells and involved in MHC class II-restricted antigen processing. HPA associates it with monocytes and myeloid dendritic cells, and it is detected in both tissues. Its network position is peripheral, but its function supplies a specific immune interpretation that cannot be inferred from extracellular-matrix genes alone. Its literature and disease-association record is more limited than that of FN1 or SOD2, but its cellular annotation is highly informative.
- **Conclusion**: Established evidence supports IFI30 as an antigen-processing and myeloid-associated component. Its presence raises the possibility of immune-cell contribution or interferon-related tissue activation, but the module does not by itself prove either mechanism.

#### KRT15

- **Related proteins** (co-abundance neighbors): SOD2 (0.90), LCP1 (0.90), LGALS1 (0.89), FN1 (0.83), IFI30 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 15. The protein encoded by this gene is a member of the keratin gene family. The keratins are intermediate filament proteins responsible for the structural integrity of epithelial cells and are subdivided into cytokeratins and hair keratins. Most of the type I cytokeratins consist of acidic proteins which are arranged in pairs of heterotypic keratin chains and are clustered in a region on chromosome 1…
- **Diseases (Open Targets)**: Alzheimer disease (0.142); neurodegenerative disease (0.136); Parkinson disease (0.136); lysosomal storage disease (0.136); neoplasm (0.108)
- **Europe PMC papers**: 3402
- **Why important**: KRT15 is the network hub connecting every other module member in the supplied subgraph. It encodes an epithelial intermediate-filament protein associated with epithelial integrity, differentiation, morphogenesis, and wound healing. HPA links it to basal keratinocytes and other basal epithelial cell types, and it is detected in colon but not cervix in the supplied immunohistochemistry summary. Although it is absent from the primary enrichment terms and has no reported STRING partner, its network position and epithelial specificity make it important for interpreting the shared module.
- **Conclusion**: Established evidence supports KRT15 as the epithelial structural anchor of the co-abundance pattern. It is plausible that KRT15 reflects epithelial repair or epithelial-cell abundance, but its hub status does not demonstrate direct biochemical interaction with the other proteins.

#### LGALS1

- **Related proteins** (co-abundance neighbors): KRT15 (0.89); STRING partners: FN1 (0.878)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galectin 1. The galectins are a family of beta-galactoside-binding proteins implicated in modulating cell-cell and cell-matrix interactions. This gene product may act as an autocrine negative growth factor that regulates cell proliferation. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: glaucoma (0.349); open-angle glaucoma (0.343); chronic kidney disease (0.330); smoking initiation (0.162); melanoma (0.121)
- **Europe PMC papers**: 4025
- **Why important**: LGALS1 is a secreted-to-blood galectin involved in cell-cell and cell-matrix interactions, proliferation, apoptosis, and NF-kappaB-related signalling. It is associated with fibroblasts, stromal cells, and extravillous trophoblasts, and it forms the sole high-confidence STRING pair with FN1 in the module. It has a broader literature base than IFI30 or LCP1 and is detected in cervix in the supplied tissue summary. Its network position is peripheral, but its functional relationship with FN1 gives it disproportionate interpretive value.
- **Conclusion**: Established evidence supports LGALS1 as an extracellular or cell-matrix signalling component linked to FN1. A role in coordinating matrix remodelling and proliferation is biologically plausible, but causality within this module is not established.

## Module 14

**Tissue pair**: cervix_uterine and colon  
**Genes (6)**: GTPBP4, MATR3, PRPF31, THOC5, SNRNP200, EFTUD2

### Function

The module is best interpreted as a core pre-mRNA splicing and spliceosome-assembly module. The strongest primary evidence is the repeated enrichment of spliceosomal tri-snRNP, small nuclear ribonucleoprotein, precatalytic spliceosome, and spliceosome terms (GO:CC U4/U6 x U5 tri-snRNP complex; q_global = 0.00317)(GO:CC spliceosomal tri-snRNP complex; q_global = 0.00317)(KEGG Spliceosome - Homo sapiens (human); q_global = 0.0061)(GO:CC U2-type precatalytic spliceosome; q_global = 0.00947)(GO:CC precatalytic spliceosome; q_global = 0.00947)(GO:CC small nuclear ribonucleoprotein complex; q_global = 0.0228)(GO:CC spliceosomal snRNP complex; q_global = 0.0228)(GO:CC Sm-like protein family complex; q_global = 0.0301). The shared signal is driven particularly by SNRNP200, PRPF31, EFTUD2, with THOC5 also contributing to the KEGG spliceosome term (KEGG Spliceosome - Homo sapiens (human); q_global = 0.0061). This supports coordinated expression of machinery involved in spliceosomal assembly, conformational rearrangement, and removal of introns. The enrichment is biologically coherent with the network because the central spliceosomal genes are connected to one another and to the remaining genes. The module should not be interpreted as evidence for a tissue-specific biological pathway beyond RNA processing.

**Cell composition.** The module is composed of nuclear, non-secreted proteins rather than plasma or secreted proteins. HPA assigns low tissue specificity to all module genes, low immune-cell specificity across the module, and no secreted genes. Protein detection is reported in both cervix_uterine and colon for most genes, while THOC5 has no HPA protein-detection result. The absence of blood-cell enrichment and secreted proteins argues against a simple plasma or blood-cell contamination explanation. The low tissue specificity instead supports a broadly expressed housekeeping-like RNA-processing program, although the cell-type-enhanced HPA annotations for some genes, including tuft cells and other epithelial or specialized cell types, leave open the possibility that shared cellular composition contributes to the co-abundance signal.

**GO/KEGG enrichment**: 8 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC U4/U6 x U5 tri-snRNP complex | 0.00317 | EFTUD2, PRPF31, SNRNP200 |
| GO:CC spliceosomal tri-snRNP complex | 0.00317 | EFTUD2, PRPF31, SNRNP200 |
| KEGG Spliceosome - Homo sapiens (human) | 0.0061 | EFTUD2, PRPF31, SNRNP200, THOC5 |
| GO:CC U2-type precatalytic spliceosome | 0.00947 | EFTUD2, PRPF31, SNRNP200 |
| GO:CC precatalytic spliceosome | 0.00947 | EFTUD2, PRPF31, SNRNP200 |
| GO:CC small nuclear ribonucleoprotein complex | 0.0228 | EFTUD2, PRPF31, SNRNP200 |
| GO:CC spliceosomal snRNP complex | 0.0228 | EFTUD2, PRPF31, SNRNP200 |
| GO:CC Sm-like protein family complex | 0.0301 | EFTUD2, PRPF31, SNRNP200 |

### STRING and hu.MAP

STRING provides especially strong support for a known physical or functional spliceosomal core: EFTUD2, PRPF31, and SNRNP200 are mutually connected with very high confidence. STRING also independently places these genes in the tri-snRNP, precatalytic spliceosome, U5 snRNP, Cajal-body, and mRNA-splicing contexts (STRING COMPARTMENTS U4/U6 x U5 tri-snRNP complex; within-query FDR = 0.0021)(STRING COMPARTMENTS U2-type precatalytic spliceosome; within-query FDR = 0.0026)(STRING Component U4/U6 x U5 tri-snRNP complex; within-query FDR = 0.0027)(STRING Component U2-type precatalytic spliceosome; within-query FDR = 0.0027)(STRING Keyword mRNA splicing; within-query FDR = 0.0068)(STRING COMPARTMENTS U5 snRNP; within-query FDR = 0.0136)(STRING Keyword Spliceosome; within-query FDR = 0.0154)(STRING COMPARTMENTS Cajal body; within-query FDR = 0.0406). The STRING evidence is supplementary rather than global enrichment evidence. hu.MAP places SNRNP200, EFTUD2, and PRPF31 together in a large spliceosome-related complex (hu.MAP huMAP3_08980.1), and places SNRNP200 with EFTUD2 in several additional spliceosomal complexes (hu.MAP huMAP3_00960.1)(hu.MAP huMAP3_07622.1)(hu.MAP huMAP3_08501.1)(hu.MAP huMAP3_09504.1)(hu.MAP huMAP3_09945.1). MATR3, THOC5, and GTPBP4 do not have reported STRING partners or hu.MAP complex membership in the fact sheet, so their links to the core may reflect co-abundance, indirect regulation, or shared cellular state rather than established direct physical interaction.

**STRING interactions (score >= 0.7)**: 3 of 15 gene pairs: EFTUD2–PRPF31 (0.999); EFTUD2–SNRNP200 (0.999); PRPF31–SNRNP200 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS U4/U6 x U5 tri-snRNP complex (FDR = 0.0021, 3 genes); COMPARTMENTS U2-type precatalytic spliceosome (FDR = 0.0026, 3 genes); Component U4/U6 x U5 tri-snRNP complex (FDR = 0.0027, 3 genes); Component U2-type precatalytic spliceosome (FDR = 0.0027, 3 genes); Keyword mRNA splicing (FDR = 0.0068, 4 genes); COMPARTMENTS U5 snRNP (FDR = 0.0136, 2 genes); Keyword Spliceosome (FDR = 0.0154, 3 genes); COMPARTMENTS Cajal body (FDR = 0.0406, 2 genes); Keyword Retinitis pigmentosa (FDR = 0.042, 2 genes); Keyword Isopeptide bond (FDR = 0.042, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08980.1 (SNRNP200, EFTUD2, PRPF31; 3/97); huMAP3_00960.1 (SNRNP200, EFTUD2; 2/8); huMAP3_07622.1 (SNRNP200, EFTUD2; 2/9); huMAP3_08501.1 (SNRNP200, EFTUD2; 2/47); huMAP3_09504.1 (SNRNP200, EFTUD2; 2/51); huMAP3_09945.1 (SNRNP200, EFTUD2; 2/61)

### Novelty

This module is not well supported as a newly discovered molecular complex. Its main core reproduces a well-established spliceosomal tri-snRNP relationship, supported by primary GO and KEGG enrichment (GO:CC U4/U6 x U5 tri-snRNP complex; q_global = 0.00317)(GO:CC spliceosomal tri-snRNP complex; q_global = 0.00317)(KEGG Spliceosome - Homo sapiens (human); q_global = 0.0061)(GO:CC U2-type precatalytic spliceosome; q_global = 0.00947)(GO:CC precatalytic spliceosome; q_global = 0.00947)(GO:CC small nuclear ribonucleoprotein complex; q_global = 0.0228)(GO:CC spliceosomal snRNP complex; q_global = 0.0228)(GO:CC Sm-like protein family complex; q_global = 0.0301), high-confidence STRING links, and hu.MAP complexes (hu.MAP huMAP3_08980.1)(hu.MAP huMAP3_00960.1)(hu.MAP huMAP3_07622.1)(hu.MAP huMAP3_08501.1)(hu.MAP huMAP3_09504.1)(hu.MAP huMAP3_09945.1). The potentially novel aspect is the observation that this coordinated expression pattern is conserved between cervix_uterine and colon, and that MATR3, THOC5, and GTPBP4 co-abundance with the spliceosomal core in this tissue comparison. However, the fact sheet does not establish that this cross-tissue co-abundance pattern is absent from prior studies, so it should be described as a potentially useful tissue-pair observation rather than a proven novel biological complex. Lack of STRING or hu.MAP membership for peripheral genes alone does not demonstrate novelty.

**Hypothesis.** Hypothesis: the conserved module reflects a broadly expressed RNA-processing state in which coordinated availability of spliceosomal tri-snRNP components supports efficient pre-mRNA maturation in both tissues. SNRNP200, EFTUD2, and PRPF31 may form the principal co-abundance backbone, while THOC5 could link spliceosome activity with nuclear messenger-RNA export and GTPBP4 could reflect a neighboring nucleolar or RNA-biogenesis state. MATR3 may represent a regulatory connection through nuclear RNA stabilization or post-transcriptional control. This model is consistent with the annotations and network structure, but the peripheral connections and any tissue-specific functional consequence require experimental testing and should not be treated as established direct interactions.

### Important genes

#### SNRNP200

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.84), PRPF31 (0.82), THOC5 (0.80), GTPBP4 (0.80); STRING partners: EFTUD2 (0.999), PRPF31 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is the most connected gene in the module and links the principal spliceosomal core to THOC5 and GTPBP4. It appears in every primary GO and KEGG term (GO:CC U4/U6 x U5 tri-snRNP complex; q_global = 0.00317)(GO:CC spliceosomal tri-snRNP complex; q_global = 0.00317)(KEGG Spliceosome - Homo sapiens (human); q_global = 0.0061)(GO:CC U2-type precatalytic spliceosome; q_global = 0.00947)(GO:CC precatalytic spliceosome; q_global = 0.00947)(GO:CC small nuclear ribonucleoprotein complex; q_global = 0.0228)(GO:CC spliceosomal snRNP complex; q_global = 0.0228)(GO:CC Sm-like protein family complex; q_global = 0.0301), in the principal STRING spliceosome annotations (STRING COMPARTMENTS U4/U6 x U5 tri-snRNP complex; within-query FDR = 0.0021)(STRING COMPARTMENTS U2-type precatalytic spliceosome; within-query FDR = 0.0026)(STRING Component U4/U6 x U5 tri-snRNP complex; within-query FDR = 0.0027)(STRING Component U2-type precatalytic spliceosome; within-query FDR = 0.0027)(STRING Keyword mRNA splicing; within-query FDR = 0.0068)(STRING COMPARTMENTS U5 snRNP; within-query FDR = 0.0136)(STRING Keyword Spliceosome; within-query FDR = 0.0154), and across all listed hu.MAP complexes (hu.MAP huMAP3_08980.1)(hu.MAP huMAP3_00960.1)(hu.MAP huMAP3_07622.1)(hu.MAP huMAP3_08501.1)(hu.MAP huMAP3_09504.1)(hu.MAP huMAP3_09945.1). Its annotation identifies it as a U5 snRNP-specific RNA helicase and a core component of tri-snRNP assembly and spliceosome conformational change. It also has substantial literature and established associations with retinitis pigmentosa and inherited retinal disease.
- **Conclusion**: Established evidence supports SNRNP200 as the central structural and functional anchor of the module. Its links to THOC5 and GTPBP4 are co-abundance relationships in this module, not established direct interactions from the supplied STRING or hu.MAP results. A plausible hypothesis is that variation in spliceosome activity is coordinated with broader nuclear RNA-processing activity through SNRNP200.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): MATR3 (0.85), SNRNP200 (0.84); STRING partners: PRPF31 (0.999), SNRNP200 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 is a core member of the spliceosomal tri-snRNP and is connected to both SNRNP200 and PRPF31 in STRING with very high confidence. It appears in every primary enrichment term (GO:CC U4/U6 x U5 tri-snRNP complex; q_global = 0.00317)(GO:CC spliceosomal tri-snRNP complex; q_global = 0.00317)(KEGG Spliceosome - Homo sapiens (human); q_global = 0.0061)(GO:CC U2-type precatalytic spliceosome; q_global = 0.00947)(GO:CC precatalytic spliceosome; q_global = 0.00947)(GO:CC small nuclear ribonucleoprotein complex; q_global = 0.0228)(GO:CC spliceosomal snRNP complex; q_global = 0.0228)(GO:CC Sm-like protein family complex; q_global = 0.0301), in multiple STRING spliceosome annotations (STRING COMPARTMENTS U4/U6 x U5 tri-snRNP complex; within-query FDR = 0.0021)(STRING COMPARTMENTS U2-type precatalytic spliceosome; within-query FDR = 0.0026)(STRING Component U4/U6 x U5 tri-snRNP complex; within-query FDR = 0.0027)(STRING Component U2-type precatalytic spliceosome; within-query FDR = 0.0027)(STRING Keyword mRNA splicing; within-query FDR = 0.0068)(STRING COMPARTMENTS U5 snRNP; within-query FDR = 0.0136)(STRING Keyword Spliceosome; within-query FDR = 0.0154), and in every listed hu.MAP complex (hu.MAP huMAP3_08980.1)(hu.MAP huMAP3_00960.1)(hu.MAP huMAP3_07622.1)(hu.MAP huMAP3_08501.1)(hu.MAP huMAP3_09504.1)(hu.MAP huMAP3_09945.1). Its known function as a spliceosomal GTPase and its disease association with mandibulofacial dysostosis with microcephaly provide strong biological support. It has substantial literature volume.
- **Conclusion**: Established evidence identifies EFTUD2 as a central tri-snRNP component and a major reason the module has a spliceosome interpretation. The co-abundance relationship with MATR3 is not independently supported by STRING or hu.MAP in the fact sheet. A hypothesis is that EFTUD2 abundance may help coordinate spliceosome assembly with broader nuclear RNA-processing demand.

#### PRPF31

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.82); STRING partners: EFTUD2 (0.999), SNRNP200 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: pre-mRNA processing factor 31. This gene encodes a component of the spliceosome complex and is one of several retinitis pigmentosa-causing genes. When the gene product is added to the spliceosome complex, activation occurs.[provided by RefSeq, Jan 2009].
- **Diseases (Open Targets)**: retinitis pigmentosa (0.798); inherited retinal dystrophy (0.576); autosomal dominant retinitis pigmentosa (0.376); eye disorder (0.371); cone-rod dystrophy (0.365)
- **Europe PMC papers**: 1184
- **Why important**: PRPF31 is directly connected to SNRNP200 and EFTUD2 in STRING, belongs to the principal hu.MAP spliceosomal complex (hu.MAP huMAP3_08980.1), and appears in every primary GO and KEGG term (GO:CC U4/U6 x U5 tri-snRNP complex; q_global = 0.00317)(GO:CC spliceosomal tri-snRNP complex; q_global = 0.00317)(KEGG Spliceosome - Homo sapiens (human); q_global = 0.0061)(GO:CC U2-type precatalytic spliceosome; q_global = 0.00947)(GO:CC precatalytic spliceosome; q_global = 0.00947)(GO:CC small nuclear ribonucleoprotein complex; q_global = 0.0228)(GO:CC spliceosomal snRNP complex; q_global = 0.0228)(GO:CC Sm-like protein family complex; q_global = 0.0301). It is an established spliceosome component involved in tri-snRNP assembly, spliceosomal activation, and pre-mRNA splicing. Its strong disease associations with retinitis pigmentosa and inherited retinal dystrophy, together with substantial literature, make it an important functional and disease-relevant representative of the module.
- **Conclusion**: Established evidence supports PRPF31 as a core spliceosomal component whose co-abundance with SNRNP200 and EFTUD2 reflects a known molecular relationship. The presence of this gene in a cervix_uterine and colon module does not imply an eye-specific process; the disease associations demonstrate functional sensitivity of spliceosome biology rather than tissue identity.

#### MATR3

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: matrin 3. This gene encodes a nuclear matrix protein, which is proposed to stabilize certain messenger RNA species. Mutations of this gene are associated with distal myopathy 2, which often includes vocal cord and pharyngeal weakness. Alternatively spliced transcript variants, including read-through transcripts composed of the upstream small nucleolar RNA host gene 4 (non-protein coding) and matrin 3 gene s…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.735); distal myopathy with vocal cord weakness (0.569); neurodegenerative disease (0.529); distal myopathy (0.384); hereditary disease (0.193)
- **Europe PMC papers**: 1756
- **Why important**: MATR3 is connected to EFTUD2 in the module but has no reported STRING partner, hu.MAP complex membership, or enriched GO or KEGG term in the fact sheet. It is a nuclear matrix protein proposed to stabilize messenger RNA and is annotated for post-transcriptional regulation of gene expression. It has the largest literature volume among the listed genes and established disease associations with distal myopathy and amyotrophic lateral sclerosis. Its HPA profile includes cell-type-enhanced expression in several specialized cell populations.
- **Conclusion**: Established evidence supports MATR3 as a nuclear RNA-associated and post-transcriptional regulator, but not as a demonstrated physical component of the spliceosomal core in this dataset. Its connection to EFTUD2 is therefore best treated as a module-level co-abundance observation. A hypothesis is that MATR3 links spliceosomal output to RNA stability or post-transcriptional regulation.

#### THOC5

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: THO complex subunit 5. Predicted to enable mRNA binding activity. Involved in several processes, including monocyte differentiation; negative regulation of DNA damage checkpoint; and viral mRNA export from host cell nucleus. Located in nucleoplasm. Part of THO complex part of transcription export complex. Colocalizes with chromosome, telomeric region. Implicated in breast carcinoma. [provided by Alliance of Genome Resou…
- **Diseases (Open Targets)**: hypothyroidism (0.338); neurodegenerative disease (0.225); thyroid gland disorder (0.092); neoplasm (0.083); cancer (0.082)
- **Europe PMC papers**: 477
- **Why important**: THOC5 is connected to SNRNP200 and contributes to the primary KEGG spliceosome term (KEGG Spliceosome - Homo sapiens (human); q_global = 0.0061). STRING places it with the module's core genes in the supplementary mRNA-splicing context (STRING Keyword mRNA splicing; within-query FDR = 0.0068), while its established annotation places it in the THO and transcription-export machinery and in messenger-RNA export from the nucleus. It also has annotations involving monocyte differentiation and viral messenger-RNA export, and it has a smaller literature base than the principal spliceosomal genes.
- **Conclusion**: Established evidence supports THOC5 as a nuclear messenger-RNA export and THO-complex factor that co-occurs with the spliceosomal core. The data do not establish that THOC5 is a direct spliceosome component or direct SNRNP200 interactor. A hypothesis is that its co-abundance marks coordination between pre-mRNA splicing and downstream nuclear export.
