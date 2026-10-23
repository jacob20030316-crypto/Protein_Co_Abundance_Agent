# Conserved co-abundance modules: cerebrospinal_fluid and prostate

## Module 0

**Tissue pair**: cerebrospinal_fluid and prostate  
**Genes (6)**: ADAM10, GNS, BPNT2, MAN2B1, IGF2R, NRP1

### Function

The module is most consistent with a lysosomal and glycoprotein-processing axis connected to membrane trafficking, cell-surface signaling, and extracellular matrix or proteoglycan turnover. MAN2B1 and GNS provide established lysosomal carbohydrate-catabolic functions, while IGF2R is an established receptor involved in mannose-phosphate-dependent lysosomal enzyme trafficking. BPNT2 contributes Golgi-localized phosphatase activity, and ADAM10 contributes membrane ectodomain proteolysis. NRP1 provides a signaling and cell-migration interface. No GO or KEGG term passed global correction, and there are no globally significant GO/KEGG terms; therefore this functional interpretation is based on individual gene annotations, the co-abundance topology, HPA evidence, and the hu.MAP relationship (hu.MAP huMAP3_06775.1), not on significant pathway enrichment. The module may represent coordinated abundance of intracellular trafficking and degradation machinery rather than a single demonstrated pathway.

**Cell composition.** The module is not tissue-specific by HPA: all module genes have low tissue specificity. HPA also indicates a strong immune-cell and myeloid-cell component, especially neutrophils, monocytes, dendritic cells, macrophages, Kupffer cells, and microglia. The majority of genes are classified in the HPA summary as secreted genes, although the individual localization annotations include intracellular, membrane, Golgi, vesicular, and plasma-membrane compartments. Prostate protein detection is present for most genes, whereas matching HPA cerebrospinal-fluid tissue data are unavailable. Consequently, the shared cerebrospinal-fluid–prostate signal could reflect blood contamination, infiltrating or resident myeloid cells, or a shared immune-cell contribution rather than a prostate- and cerebrospinal-fluid-specific program. The broad tissue distribution also supports caution against interpreting the module as organ-specific.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was detected among the module gene pairs, and STRING functional enrichment was absent. Thus, the co-abundance relationships are not supported here by established high-confidence binary protein interactions. hu.MAP identifies (hu.MAP huMAP3_06775.1), containing ADAM10 and IGF2R together with many other proteins, but only a small subset of that complex is represented in this module. This provides limited support for a shared trafficking or membrane-associated molecular context, while not establishing that the entire module is one physical complex. The strongest network position belongs to MAN2B1, which connects to GNS, ADAM10, and BPNT2; NRP1 connects to IGF2R and BPNT2. These topological links suggest coordinated abundance across related cellular compartments, but they should not be treated as direct biochemical interactions.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (ADAM10, IGF2R; 2/60)

### Novelty

This may be a potentially interesting cross-tissue co-abundance observation, but it cannot be claimed as a new biological mechanism from the present evidence. The absence of STRING support and the limited hu.MAP overlap do not by themselves establish novelty, because interaction databases are incomplete and co-abundance can capture shared cell composition, secretion, trafficking, or technical effects. The lack of globally significant GO or KEGG enrichment further limits pathway-level claims, although it does not invalidate the module. A defensible novelty claim would require replication in independent cerebrospinal-fluid and prostate cohorts, adjustment for blood-cell admixture, and comparison with published tissue proteomic modules and cell-type signatures.

**Hypothesis.** Hypothesis: the module reflects a shared myeloid-associated lysosomal and glycoprotein-handling program present in both sample types, with MAN2B1 and GNS supporting lysosomal carbohydrate degradation, IGF2R and BPNT2 supporting intracellular trafficking and Golgi processing, and ADAM10 and NRP1 linking this machinery to cell-surface proteolysis, migration, and signaling. In cerebrospinal fluid and prostate, the signal may arise from similar immune-cell populations or from proteins released by such cells, rather than from a dedicated epithelial or neural program. This hypothesis should be tested by cell-type deconvolution, measurement of blood contamination, targeted protein validation, and perturbation of lysosomal or membrane-trafficking pathways.

### Important genes

#### MAN2B1

- **Related proteins** (co-abundance neighbors): GNS (0.85), ADAM10 (0.84), BPNT2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Nucleoplasm, Vesicles; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosidase alpha class 2B member 1. This gene encodes an enzyme that hydrolyzes terminal, non-reducing alpha-D-mannose residues in alpha-D-mannosides. Its activity is necessary for the catabolism of N-linked carbohydrates released during glycoprotein turnover and it is member of family 38 of glycosyl hydrolases. The full length protein is processed in two steps. First, a 49 aa leader sequence is cleaved off and the remainder of the …
- **Diseases (Open Targets)**: alpha-mannosidosis (0.858); hereditary disease (0.516); Intellectual disability (0.426); alpha-mannosidosis, adult form (0.379); alpha-mannosidosis, infantile form (0.378)
- **Europe PMC papers**: 731
- **Why important**: MAN2B1 is the central network node, linking GNS, ADAM10, and BPNT2. Its established function in alpha-mannoside and glycoprotein catabolism gives the module a plausible lysosomal carbohydrate-processing anchor. It is enriched in several myeloid and microglial cell types by HPA, is detected in prostate, has established alpha-mannosidosis associations, and has a substantial literature base.
- **Conclusion**: Established evidence supports MAN2B1 as the principal lysosomal carbohydrate-catabolism marker and the topological hub of the module. It is a strong candidate for representing shared myeloid or lysosomal biology. It remains a hypothesis that its abundance drives the cross-tissue module or directly coordinates the other proteins.

#### GNS

- **Related proteins** (co-abundance neighbors): MAN2B1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glucosamine (N-acetyl)-6-sulfatase. The product of this gene is a lysosomal enzyme found in all cells. It is involved in the catabolism of heparin, heparan sulphate, and keratan sulphate. Deficiency of this enzyme results in the accumulation of undegraded substrate and the lysosomal storage disorder mucopolysaccharidosis type IIID (Sanfilippo D syndrome). Mucopolysaccharidosis type IIID is the least common of the four subtypes of Sa…
- **Diseases (Open Targets)**: mucopolysaccharidosis type 3D (0.811); mucopolysaccharidosis type 3 (0.610); mucopolysaccharidosis (0.372); ventricular fibrillation (0.233); preeclampsia (0.223)
- **Europe PMC papers**: 3078
- **Why important**: GNS is directly connected to MAN2B1 and encodes a lysosomal sulfatase involved in degradation of heparin, heparan sulfate, and keratan sulfate. HPA associates it with monocytes, neutrophils, Kupffer cells, and other cell types, while its disease association with mucopolysaccharidosis type IIID provides strong functional context. Its literature base is substantial.
- **Conclusion**: Established evidence supports GNS as a second lysosomal glycosaminoglycan-catabolism component and reinforces the interpretation of a degradative or storage-organelle program. The coordinated abundance with MAN2B1 is biologically plausible, but the module does not demonstrate a direct GNS–MAN2B1 physical interaction.

#### IGF2R

- **Related proteins** (co-abundance neighbors): NRP1 (0.93); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enhanced; location Golgi apparatus; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_06775.1
- **Function (MyGene.info)**: insulin like growth factor 2 receptor. This gene encodes a receptor for both insulin-like growth factor 2 and mannose 6-phosphate. The binding sites for each ligand are located on different segments of the protein. This receptor has various functions, including in the intracellular trafficking of lysosomal enzymes, the activation of transforming growth factor beta, and the degradation of insulin-like growth factor 2. Mutation or loss o…
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.498); coronary artery disorder (0.477); Hypercholesterolemia (0.369); myocardial ischemia (0.359); coronary atherosclerosis (0.349)
- **Europe PMC papers**: 12245
- **Why important**: IGF2R is connected to NRP1 and forms the only hu.MAP-supported pair in the module through (hu.MAP huMAP3_06775.1) with ADAM10. Its established roles include IGF2 and mannose-phosphate receptor activity, lysosomal enzyme trafficking, IGF2 degradation, and signaling. HPA places it in neutrophils and detects it in prostate. It also has an extensive literature base and disease associations including hepatocellular carcinoma and cardiovascular disorders.
- **Conclusion**: Established evidence supports IGF2R as a bridge between lysosomal targeting and receptor-mediated signaling or trafficking. Its presence gives the module a coherent intracellular transport interpretation. The hypothesis that IGF2R coordinates NRP1 or ADAM10 in this cross-tissue module is not established by the available interaction evidence.

#### NRP1

- **Related proteins** (co-abundance neighbors): IGF2R (0.93), BPNT2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neuropilin 1. This gene encodes one of two neuropilins, which contain specific protein domains which allow them to participate in several different types of signaling pathways that control cell migration. Neuropilins contain a large N-terminal extracellular domain, made up of complement-binding, coagulation factor V/VIII, and meprin domains. These proteins also contains a short membrane-spanning domain and a sm…
- **Diseases (Open Targets)**: COVID-19 (0.490); Abnormality of the skeletal system (0.466); mathematical ability (0.355); migraine disorder (0.346); obstructive sleep apnea syndrome (0.345)
- **Europe PMC papers**: 12192
- **Why important**: NRP1 occupies a connecting position between IGF2R and BPNT2 and is a multifunctional receptor or co-receptor involved in angiogenesis, vascular morphogenesis, and cell migration. HPA associates it with plasmacytoid dendritic cells and several stromal or macrophage-related cell types. It has the largest literature volume among the selected signaling candidates and broad disease relevance.
- **Conclusion**: Established evidence supports NRP1 as a membrane-signaling and migration component that could connect immune-cell state to vascular or tissue-remodeling biology. Its network placement supports a coordinating role within the module, but the proposed connection to lysosomal processing is a hypothesis rather than a demonstrated molecular pathway.

#### ADAM10

- **Related proteins** (co-abundance neighbors): MAN2B1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_06775.1
- **Function (MyGene.info)**: ADAM metallopeptidase domain 10. Members of the ADAM family are cell surface proteins with a unique structure possessing both potential adhesion and protease domains. This gene encodes and ADAM family member that cleaves many proteins including TNF-alpha and E-cadherin. Alternate splicing results in multiple transcript variants encoding different proteins that may undergo similar processing. [provided by RefSeq, Feb 2016].
- **Diseases (Open Targets)**: reticulate acropigmentation of Kitamura (0.679); Alzheimer disease 18 (0.621); Alzheimer disease (0.522); dementia (0.415); schizophrenia (0.354)
- **Europe PMC papers**: 11139
- **Why important**: ADAM10 is connected to MAN2B1 and is one of the two module members represented in hu.MAP complex (hu.MAP huMAP3_06775.1). It is an established cell-surface metalloprotease that cleaves TNF-alpha, E-cadherin, and other substrates and participates in ectodomain proteolysis and Notch signaling. HPA detects it in prostate and associates it with neutrophils. It has an extensive literature base and broad neurological and oncological disease associations.
- **Conclusion**: Established evidence supports ADAM10 as the module's clearest extracellular-shedding and membrane-proteolysis component. It could link immune-cell activation or tissue remodeling to the intracellular trafficking machinery. Whether ADAM10 is functionally coupled to MAN2B1 in this module is not established by the absent STRING evidence.

#### BPNT2

- **Related proteins** (co-abundance neighbors): NRP1 (0.83), MAN2B1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3'(2'), 5'-bisphosphate nucleotidase 2. This gene encodes a member of the inositol monophosphatase family. The encoded protein is localized to the Golgi apparatus and catalyzes the hydrolysis of phosphoadenosine phosphate (PAP) to adenosine monophosphate (AMP). Mutations in this gene are a cause of GRAPP type chondrodysplasia with joint dislocations, and a pseudogene of this gene is located on the long arm of chromosome 1. [provided by …
- **Diseases (Open Targets)**: chondrodysplasia with joint dislocations, gPAPP type (0.738); chronic kidney disease (0.316); breast disorder (0.294); liver disorder (0.288); ovarian neoplasm (0.288)
- **Europe PMC papers**: 63
- **Why important**: BPNT2 connects NRP1 and MAN2B1 and is localized to the Golgi apparatus, providing a possible compartmental link between protein processing and lysosomal trafficking. Its established enzymatic activity involves phosphoadenosine phosphate hydrolysis, and it is associated with gPAPP-type chondrodysplasia with joint dislocations. HPA shows low tissue and cell-type specificity and detects it in prostate, while its literature base is comparatively limited.
- **Conclusion**: Established evidence supports BPNT2 as a Golgi metabolic and trafficking marker, but its role in this module is less well characterized than the roles of the lysosomal enzymes or membrane protease. Its network placement makes it a plausible connector, while any mechanistic coupling to NRP1 or MAN2B1 remains hypothetical.

## Module 1

**Tissue pair**: cerebrospinal_fluid and prostate  
**Genes (10)**: SERPINC1, APOE, COL12A1, GSN, LAMA5, LAMB2, LAMC1, SOD2, F2, GC

### Function

The module is most consistent with a mixed extracellular and circulating-protein program linking basement-membrane or extracellular-matrix organization with plasma transport, coagulation, lipid handling, and oxidative-stress biology. LAMC1 is the main network hub and connects the laminin genes LAMA5 and LAMB2 with COL12A1, GC, APOE, and SERPINC1. The laminin and collagen annotations support an extracellular-matrix or basement-membrane component, whereas F2, SERPINC1, and GC support a circulating coagulation and transport component. APOE contributes lipid transport, and SOD2 contributes mitochondrial superoxide defense. No GO/KEGG term passed global correction, so this functional interpretation is based on gene-level annotations, network structure, HPA evidence, STRING, and hu.MAP rather than statistically enriched GO/KEGG categories.

**Cell composition.** The module is strongly dominated by secreted proteins: HPA classifies nearly all module genes as secreted, either to blood or to the extracellular matrix. Several genes are liver-enhanced or hepatocyte-associated, especially GC, SERPINC1, and F2, while APOE is enhanced in liver and brain and GSN is enhanced in heart muscle. The extracellular-matrix genes are associated with fibroblasts, adipocytes, vascular or stromal populations, and prostate detection is present for some members. Most genes are not detected as immune-cell-specific, although SOD2 is enriched in neutrophils and GSN is enhanced in eosinophils. Thus, the shared cerebrospinal-fluid and prostate module may substantially reflect circulating plasma proteins, extracellular matrix, blood-derived material, or shared stromal and vascular components rather than a prostate-specific or cerebrospinal-fluid-specific cellular program. HPA reports no matching cerebrospinal-fluid protein-detection data and mixed detection in prostate, so tissue-level protein localization should be interpreted cautiously.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a coherent laminin subnetwork involving LAMC1, LAMA5, and LAMB2, with additional support for the pairs LAMC1–COL12A1, GC–GSN, APOE–GSN, F2–GC, F2–SERPINC1, and GC–SERPINC1. These are established database-supported relationships and show that part of the module recapitulates known extracellular-matrix and plasma-protein biology. hu.MAP places SERPINC1 and GC together in (hu.MAP huMAP3_15040.1), and F2 and GC together in (hu.MAP huMAP3_10678.1). However, each complex contains only a small subset of the module, so the complexes support selected relationships rather than a single complete molecular complex. SOD2 has no listed STRING partners and no hu.MAP membership, despite its co-abundance links within the module. Overall, the evidence indicates a biologically mixed network with several known edges rather than an entirely novel physical complex.

**STRING interactions (score >= 0.7)**: 9 of 45 gene pairs: APOE–GSN (0.828); COL12A1–LAMC1 (0.721); F2–GC (0.792); F2–SERPINC1 (0.999); GC–GSN (0.826); GC–SERPINC1 (0.84); LAMA5–LAMB2 (0.924); LAMA5–LAMC1 (0.999); LAMB2–LAMC1 (0.962)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINC1, GC; 2/64); huMAP3_10678.1 (F2, GC; 2/71)

### Novelty

This module should not be claimed as a wholly new molecular complex or as a newly discovered pathway. The laminin interactions, coagulation relationships, GC associations, and the hu.MAP memberships are already represented in established resources. A potentially novel aspect is the coordinated co-abundance of these extracellular-matrix, plasma, lipid-transport, coagulation, and oxidative-stress genes across cerebrospinal fluid and prostate, but that cross-tissue pattern requires independent replication and controls for blood contamination, shared extracellular material, and stromal or vascular composition. Absence of an edge from STRING or hu.MAP, such as the SOD2 connections, is not evidence that the relationship itself is novel.

**Hypothesis.** Hypothesis: the module reflects a shared extracellular-fluid and tissue-interface state in which liver-derived circulating proteins and lipid or vitamin carriers coexist with basement-membrane proteins from stromal or vascular compartments. In this model, GC, APOE, F2, and SERPINC1 represent a circulating transport and coagulation layer; LAMC1, LAMA5, LAMB2, and COL12A1 represent a matrix layer; GSN may connect extracellular material to actin remodeling; and SOD2 may report oxidative stress in associated cells. The apparent preservation of this program between cerebrospinal fluid and prostate could arise from shared extracellular matrix, vascular interfaces, or plasma carryover rather than a dedicated tissue-specific mechanism. This hypothesis should be tested using cell-resolved measurements, matched plasma controls, and independent cohorts.

### Important genes

#### LAMC1

- **Related proteins** (co-abundance neighbors): COL12A1 (0.97), APOE (0.86), GC (0.86), LAMB2 (0.85), LAMA5 (0.84), SERPINC1 (0.83); STRING partners: COL12A1 (0.721), LAMA5 (0.999), LAMB2 (0.962)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Plasma membrane; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit gamma 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: Fuchs' endothelial dystrophy (0.487); prostate carcinoma (0.467); colorectal cancer (0.447); eye disorder (0.434); benign colon neoplasm (0.427)
- **Europe PMC papers**: 4227
- **Why important**: LAMC1 is the principal network hub, linking the matrix genes COL12A1, LAMA5, and LAMB2 with GC, APOE, and SERPINC1. It is a secreted-to-extracellular-matrix laminin component, is associated with fibroblast and stromal populations, and is detected by immunohistochemistry in prostate. STRING supports its relationships with COL12A1, LAMA5, and LAMB2. Its substantial literature and associations with tissue development, cell adhesion, migration, and prostate carcinoma make it the strongest structural anchor of the module.
- **Conclusion**: Established evidence supports LAMC1 as the central extracellular-matrix organizer in this module. It is plausible, but not established, that LAMC1 coordinates the observed prostate or cerebrospinal-fluid co-abundance pattern with circulating proteins.

#### GC

- **Related proteins** (co-abundance neighbors): GSN (0.91), LAMC1 (0.86), SOD2 (0.82); STRING partners: F2 (0.792), GSN (0.826), SERPINC1 (0.84)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in prostate
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: GC vitamin D binding protein. The protein encoded by this gene belongs to the albumin gene family. It is a multifunctional protein found in plasma, ascitic fluid, cerebrospinal fluid and on the surface of many cell types. It binds to vitamin D and its plasma metabolites and transports them to target tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq,…
- **Diseases (Open Targets)**: vitamin D deficiency (0.574); vitamin deficiency (0.552); chronic obstructive pulmonary disease (0.499); squamous cell carcinoma (0.339); central nervous system cancer (0.334)
- **Europe PMC papers**: 363974
- **Why important**: GC is a highly connected bridge between GSN, LAMC1, and SOD2 and is also linked in STRING to F2 and SERPINC1. It is a liver-enriched, hepatocyte-associated protein secreted to blood and is known to bind and transport vitamin D and its metabolites; it is also found in plasma and cerebrospinal fluid. GC participates in both hu.MAP complexes (hu.MAP huMAP3_15040.1) and (hu.MAP huMAP3_10678.1) and has a very large literature base.
- **Conclusion**: Established evidence supports GC as a circulating transport protein and as a major connector between the plasma and matrix portions of the network. Its presence may reflect blood or extracellular-fluid composition rather than local production in prostate or cerebrospinal fluid.

#### SERPINC1

- **Related proteins** (co-abundance neighbors): SOD2 (0.91), LAMC1 (0.83); STRING partners: F2 (0.999), GC (0.84)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 connects SOD2 and LAMC1 in the co-abundance graph and has strong STRING relationships with F2 and GC. It is liver-enriched, hepatocyte-associated, secreted to blood, and encodes antithrombin, a regulator of thrombin and other activated coagulation proteases. It participates with GC in hu.MAP complex (hu.MAP huMAP3_15040.1) and has well-established associations with antithrombin deficiency and thrombotic disease.
- **Conclusion**: Established evidence supports SERPINC1 as a plasma coagulation-regulatory component. Its network connection to matrix and oxidative-stress genes is an observation of co-abundance, not proof that antithrombin directly regulates those processes in this module.

#### F2

- **Related proteins** (co-abundance neighbors): SOD2 (0.91); STRING partners: GC (0.792), SERPINC1 (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1
- **Function (MyGene.info)**: coagulation factor II, thrombin. This gene encodes the prothrombin protein (also known as coagulation factor II). This protein is proteolytically cleaved in multiple steps to form the activated serine protease thrombin. The activated thrombin enzyme plays an important role in thrombosis and hemostasis by converting fibrinogen to fibrin during blood clot formation, by stimulating platelet aggregation, and by activating additional …
- **Diseases (Open Targets)**: congenital prothrombin deficiency (0.827); thrombophilia due to thrombin defect (0.738); venous thromboembolism (0.727); deep vein thrombosis (0.690); blood coagulation disease (0.670)
- **Europe PMC papers**: 109299
- **Why important**: F2 is a biologically important coagulation node connected to SOD2 and supported by STRING relationships with GC and SERPINC1. Its encoded prothrombin is cleaved to thrombin, which participates in clot formation, platelet activation, tissue repair, angiogenesis, and cell-surface signaling. F2 also occurs with GC in hu.MAP complex (hu.MAP huMAP3_10678.1) and has extensive literature and strong disease associations involving thrombophilia and venous thromboembolism.
- **Conclusion**: Established evidence supports F2 as a circulating coagulation and tissue-repair factor represented in the module. Whether its co-abundance with SOD2 reflects a shared injury, vascular, or oxidative state remains a hypothesis.

#### APOE

- **Related proteins** (co-abundance neighbors): LAMC1 (0.86); STRING partners: GSN (0.828)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein E. The protein encoded by this gene is a major apoprotein of the chylomicron. It binds to a specific liver and peripheral cell receptor, and is essential for the normal catabolism of triglyceride-rich lipoprotein constituents. This gene maps to chromosome 19 in a cluster with the related apolipoprotein C1 and C2 genes. Mutations in this gene result in familial dysbetalipoproteinemia, or type III hype…
- **Diseases (Open Targets)**: hyperlipoproteinemia type 3 (0.803); coronary artery disorder (0.782); lipoprotein glomerulopathy (0.759); Alzheimer disease (0.696); familial hypercholesterolemia (0.651)
- **Europe PMC papers**: 74272
- **Why important**: APOE links to the central LAMC1 hub and to GSN through STRING. It is enhanced in brain, liver, and adrenal gland and in hepatocytes and Leydig cells, is secreted to blood, and mediates lipid transport and receptor-mediated uptake. Its disease associations include lipid disorders, coronary artery disease, and Alzheimer disease, giving it relevance to both vascular and nervous-system contexts.
- **Conclusion**: Established evidence supports APOE as a secreted lipid-transport component that could connect cerebrospinal-fluid biology with systemic and tissue-interface processes. Its direct mechanistic role in the shared module is not established by the available co-abundance data.

#### SOD2

- **Related proteins** (co-abundance neighbors): F2 (0.91), SERPINC1 (0.91), GC (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Mitochondria; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: superoxide dismutase 2. This gene is a member of the iron/manganese superoxide dismutase family. It encodes a mitochondrial protein that forms a homotetramer and binds one manganese ion per subunit. This protein binds to the superoxide byproducts of oxidative phosphorylation and converts them to hydrogen peroxide and diatomic oxygen. Mutations in this gene have been associated with idiopathic cardiomyopathy (IDC), premat…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); diabetic retinopathy (0.379); malunion fracture (0.295); coronary artery disorder (0.267); prostate carcinoma (0.227)
- **Europe PMC papers**: 28293
- **Why important**: SOD2 is connected to F2, SERPINC1, and GC and is the only selected gene that provides a clear intracellular mitochondrial oxidative-stress perspective. It encodes manganese superoxide dismutase, which converts superoxide generated during oxidative phosphorylation into hydrogen peroxide and oxygen. HPA associates it with bone marrow and neutrophils, and its disease associations include neurodegenerative disease and prostate carcinoma. It has a large literature base despite lacking listed STRING partners or hu.MAP membership.
- **Conclusion**: Established evidence supports SOD2 as an oxidative-stress and mitochondrial-defense marker. Its placement beside circulating coagulation proteins may indicate shared tissue injury or cellular stress, but a direct biochemical connection to the secreted-protein subnetwork is only a hypothesis.

## Module 3

**Tissue pair**: cerebrospinal_fluid and prostate  
**Genes (6)**: ASAH1, ATP1B1, ENDOD1, PLXNB2, RBP4, SELENBP1

### Function

No GO or KEGG term passed global multiple-testing correction, and there was no supplementary STRING enrichment. Therefore, this module does not support a formally validated pathway-level annotation. Its gene-level composition nevertheless points to a mixed membrane, lysosomal, lipid-handling, transport, and extracellular-carrier theme. ASAH1 provides an established sphingolipid and ceramide-degradation function; ATP1B1 supports transmembrane ion-gradient maintenance; RBP4 represents retinol transport in blood; PLXNB2 is a semaphorin-responsive receptor involved in cell migration, adhesion, endocytosis, and neurodevelopmental processes; SELENBP1 is linked to selenium biology and ubiquitination-related activity; and ENDOD1 has predicted nucleic-acid hydrolysis and metal-binding functions. The module is therefore better described as a heterogeneous co-abundance signal involving epithelial or membrane biology, lipid and retinoid handling, and extracellular or blood-associated proteins than as a proven single biochemical pathway. Absence of globally significant enrichment does not make the module biologically false, but it limits pathway-level confidence.

**Cell composition.** The module is compositionally mixed rather than uniformly secreted or uniformly housekeeping. RBP4 is a liver-enriched protein secreted to blood, while ENDOD1 is annotated as secreted with unknown location; together with the secreted status of another module member in the HPA summary, this raises the possibility of extracellular carryover or plasma-related co-abundance. RBP4 is not detected in immune cells, whereas several other members show immune-cell enhancement, group enrichment, or platelet association. HPA profiles also point to hepatocytes, myeloid dendritic cells, monocytes, platelets, esophageal apical cells, and other specialized cell types. Most members show tissue or cell-type restriction rather than broad uniform expression, with tissue associations spanning intestine, heart muscle, kidney, and liver. Prostate protein detection is reported for most members, but the cerebrospinal-fluid protein field has no matching HPA data. Consequently, the shared signal could reflect a combination of prostate-associated expression, extracellular protein contribution, and shared or variable cell-type composition; it should not automatically be interpreted as a cerebrospinal-fluid-specific biological program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module members, and no hu.MAP complex contains multiple members. Thus, the observed co-abundance edges are not corroborated by the supplied curated protein-interaction or complex resources. The strongest network-connected member is ENDOD1, which links to ASAH1, SELENBP1, ATP1B1, and PLXNB2 in the co-abundance graph. ASAH1 also links to PLXNB2, while SELENBP1 links to RBP4. These graph relationships may represent coordinated abundance, shared cellular origin, extracellular transfer, or technical and biological covariance rather than direct physical binding. The lack of STRING and hu.MAP support argues against describing the module as a known multiprotein complex.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel cross-tissue co-abundance association, because the specific module is not supported by the supplied STRING interaction network or hu.MAP complex catalogue. However, that absence alone does not establish discovery of a new mechanism: the genes have individually established functions, several have extensive literature, and the module may reflect shared cell types, tissue leakage, secreted-protein transport, or sample composition. The appropriate claim is that the coordinated abundance pattern appears under-characterized as a module and merits validation, not that the underlying biology is unprecedented. Replication in independent cerebrospinal-fluid and prostate cohorts, adjustment for blood contamination and cell composition, and orthogonal protein or transcript measurements would be needed to establish novelty.

**Hypothesis.** Hypothesis: the module captures a cross-tissue abundance state produced by a mixture of epithelial or membrane-associated cells and extracellular proteins, with lipid, retinoid, and ion-transport physiology contributing to the covariance. A possible mechanistic bridge is that ASAH1-dependent sphingolipid turnover and ATP1B1-dependent membrane-gradient maintenance influence membrane organization and trafficking, while PLXNB2 reflects receptor-mediated migration or adhesion biology. RBP4 may enter the shared signal through liver-derived circulating protein or blood-related contribution, and SELENBP1 and ENDOD1 may report tissue stress, metabolic state, or cell-type composition. This is a testable hypothesis rather than an established pathway: targeted measurement of sphingolipids, retinol-bound RBP4, membrane proteins, blood-contamination markers, and relevant cell-type proportions could distinguish coordinated biology from sample-mixture effects.

### Important genes

#### ENDOD1

- **Related proteins** (co-abundance neighbors): ASAH1 (0.85), SELENBP1 (0.84), ATP1B1 (0.83), PLXNB2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nuclear membrane; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: endonuclease domain containing 1. Predicted to enable endonuclease activity; metal ion binding activity; and nucleic acid binding activity. Predicted to be involved in nucleic acid phosphodiester bond hydrolysis. Located in extracellular exosome and membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: gestational diabetes (0.303); autoimmune disease (0.206); obesity disorder (0.133); alcohol drinking (0.109); urolithiasis (0.094)
- **Europe PMC papers**: 309
- **Why important**: ENDOD1 is the central network connector in the supplied co-abundance graph, linking the lipid enzyme ASAH1, SELENBP1, ATP1B1, and PLXNB2. It is annotated with predicted endonuclease, metal-binding, and nucleic-acid-binding activities and has a secreted-unknown-location annotation, making it a possible bridge between intracellular or membrane biology and extracellular protein abundance. Its prostate detection and substantial literature provide useful experimental grounding, although its direct role in this module is not established.
- **Conclusion**: Established evidence supports ENDOD1 as the principal network hub and as a protein with predicted nucleic-acid-related activity and prostate detection. The hypothesis that it organizes or mechanistically drives the module is unproven; its hub position may instead reflect correlated abundance or shared sample composition.

#### ASAH1

- **Related proteins** (co-abundance neighbors): ENDOD1 (0.85), PLXNB2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-acylsphingosine amidohydrolase 1. This gene encodes a member of the acid ceramidase family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed. Processing of this preproprotein generates alpha and beta subunits that heterodimerize to form the mature lysosomal enzyme, which catalyzes the degradation of ceramide into sphingosine an…
- **Diseases (Open Targets)**: Farber lipogranulomatosis (0.838); spinal muscular atrophy-progressive myoclonic epilepsy syndrome (0.806); ASAH1-related sphingolipidosis (0.600); atrial fibrillation (0.557); hydrops fetalis (0.467)
- **Europe PMC papers**: 2292
- **Why important**: ASAH1 is one of the most functionally informative members because it encodes acid ceramidase, whose mature enzyme degrades ceramide into sphingosine and free fatty acid. It is connected to ENDOD1 and PLXNB2, has a heart-muscle-enhanced profile and several immune-associated cell-type annotations, and has strong disease relevance including lysosomal and sphingolipid disorders. Its extensive literature makes it a strong anchor for testing a membrane-lipid interpretation.
- **Conclusion**: Established evidence supports ASAH1 as a lysosomal sphingolipid-catabolic enzyme with important disease associations. It is plausible that ceramide turnover contributes to the shared abundance pattern, but the module data do not establish that ASAH1 activity is driving the other proteins or that a common sphingolipid pathway is enriched.

#### PLXNB2

- **Related proteins** (co-abundance neighbors): ENDOD1 (0.82), ASAH1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location None; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plexin B2. Members of the B class of plexins, such as PLXNB2 are transmembrane receptors that participate in axon guidance and cell migration in response to semaphorins (Perrot et al. (2002) [PubMed 12183458]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Intellectual disability (0.519); amelogenesis imperfecta (0.518); sensorineural hearing loss disorder (0.516); cutaneous melanoma (0.486); neurodegenerative disease (0.455)
- **Europe PMC papers**: 2109
- **Why important**: PLXNB2 is a transmembrane plexin receptor associated with semaphorin-responsive axon guidance and cell migration, as well as adhesion, endocytosis, phosphorylation regulation, and neurodevelopmental processes. It connects to both ENDOD1 and ASAH1 and has annotations involving esophageal, foveolar, alveolar, and monocyte or dendritic-cell populations. Its receptor function offers a biologically meaningful interface between cell state, membrane organization, and tissue or immune-cell composition.
- **Conclusion**: Established evidence supports PLXNB2 as a membrane receptor involved in guidance, adhesion, migration, and endocytic biology. Its participation in this module may indicate shared membrane or cell-type biology, but a direct functional relationship with ASAH1 or ENDOD1 remains hypothetical.

#### RBP4

- **Related proteins** (co-abundance neighbors): SELENBP1 (0.88); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: retinol binding protein 4. This protein belongs to the lipocalin family and is the specific carrier for retinol (vitamin A alcohol) in the blood. It delivers retinol from the liver stores to the peripheral tissues. In plasma, the RBP-retinol complex interacts with transthyretin which prevents its loss by filtration through the kidney glomeruli. A deficiency of vitamin A blocks secretion of the binding protein posttranslatio…
- **Diseases (Open Targets)**: progressive retinal dystrophy due to retinol transport defect (0.696); microphthalmia, isolated, with coloboma 10 (0.643); microphthalmia, isolated, with coloboma (0.506); microphthalmia (0.501); inherited retinal dystrophy (0.421)
- **Europe PMC papers**: 18196
- **Why important**: RBP4 is the clearest extracellular and systemic component: it is liver-enriched, hepatocyte-enriched, secreted to blood, and transports retinol from liver stores to peripheral tissues. It is connected to SELENBP1 in the module and has extensive literature plus strong associations with inherited retinol-transport disorders. Its presence is important because it can mark circulating protein contribution rather than local prostate or cerebrospinal-fluid synthesis.
- **Conclusion**: Established evidence supports RBP4 as a circulating retinol carrier produced principally by liver. In this module, its most likely interpretive value is as a potential extracellular or blood-related contributor; a direct retinoid mechanism linking it to the other members is not demonstrated.

#### ATP1B1

- **Related proteins** (co-abundance neighbors): ENDOD1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit beta 1. The protein encoded by this gene belongs to the family of Na+/K+ and H+/K+ ATPases beta chain proteins, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a vari…
- **Diseases (Open Targets)**: cardiovascular disorder (0.634); atrial fibrillation (0.606); congestive heart failure (0.601); heart failure (0.585); cardiac arrhythmia (0.536)
- **Europe PMC papers**: 2226
- **Why important**: ATP1B1 encodes the beta subunit of the sodium-potassium ATPase, supporting electrochemical gradients, ion transport, osmoregulation, and coupled transport. It is connected to the ENDOD1 hub and shows kidney-enhanced, epithelial-associated, and basophil-associated HPA annotations, while also having substantial disease literature involving cardiovascular and arrhythmia-related conditions. It provides a membrane-physiology anchor distinct from the secreted proteins.
- **Conclusion**: Established evidence supports ATP1B1 as a component of sodium-potassium pump function and transmembrane homeostasis. Its module association could reflect membrane abundance or epithelial-cell composition; a specific causal link to the lipid, retinol, or receptor features is a hypothesis rather than a demonstrated mechanism.

## Module 4

**Tissue pair**: cerebrospinal_fluid and prostate  
**Genes (5)**: CD276, HSPA13, HYOU1, ICAM1, TFRC

### Function

No GO or KEGG term passed global correction, and STRING supplied no supplementary functional term. The strongest functional interpretation is therefore an integrated stress, protein-folding, iron-uptake, cell-adhesion, and immune-regulatory signal rather than a formally enriched pathway. HYOU1 is the network hub and connects the heat-shock proteins HSPA13, the transferrin receptor TFRC, the immune-regulatory molecule CD276, and the adhesion molecule ICAM1. This pattern is compatible with coordinated cellular stress and inflammatory or immune-state biology, but the small co-abundance subgraph does not establish a single biochemical pathway.

**Cell composition.** The module is not composed exclusively of a single tissue-restricted protein class. Several genes are classified by HPA as secreted to blood or otherwise compatible with extracellular or circulating detection, while HYOU1 and HSPA13 are intracellular and membrane-associated. Most genes have low tissue specificity, with ICAM1 showing tissue enhancement in lung and urinary bladder. All module genes have cell-type-enhanced annotations, with recurring associations to plasma cells, macrophages, monocytes, corticotrophs, and syncytiotrophoblasts. TFRC is immune-cell enhanced and associated with non-classical monocytes, whereas ICAM1 is associated with macrophages and monocytes. This composition raises the possibility that the shared cerebrospinal-fluid and prostate signal partly reflects blood, immune-cell content, or shared cell states rather than a prostate-and-cerebrospinal-fluid-specific mechanism. HPA reports prostate protein detection for HSPA13, TFRC, and CD276, but not for HYOU1 or ICAM1; it provides no matching cerebrospinal-fluid tissue detection result.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair reached the supplied high-confidence STRING interaction threshold, and no STRING functional-enrichment term was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not supported here as established physical interactions or membership in a known multiprotein complex. The absence of STRING and hu.MAP support limits mechanistic interpretation, but does not disprove co-regulation, indirect signaling, shared cellular origin, or context-dependent interactions. The network topology itself is hub-and-spoke, with HYOU1 connected to every other module member and each remaining gene connected only to HYOU1.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a previously unreported co-abundance pattern in the analyzed cerebrospinal-fluid and prostate data, because the module combines a stress-related hub with iron-uptake, immune-checkpoint, and adhesion genes without support from the queried STRING or hu.MAP resources. However, it cannot be called a new biological discovery from the fact sheet alone. The lack of globally significant GO or KEGG enrichment, the lack of high-confidence STRING relationships, the lack of a hu.MAP complex, and the broad or cell-type-associated HPA expression pattern all make the finding hypothesis-generating rather than established. Database absence alone is not evidence of novelty.

**Hypothesis.** Hypothesis: the module reflects a shared cellular stress and inflammatory state present in subsets of cells or extracellular material sampled from cerebrospinal fluid and prostate. In this model, endoplasmic-reticulum stress and hypoxia-related protein handling involving HYOU1 and HSPA13 could co-vary with iron acquisition through TFRC, immune regulation through CD276, and leukocyte or endothelial adhesion through ICAM1. A contribution from blood or immune-cell admixture is an alternative or complementary explanation. This hypothesis should be tested by cell-type deconvolution, independent cohorts, protein-level validation, and perturbation or longitudinal studies; the present co-abundance result does not demonstrate causality.

### Important genes

#### HYOU1

- **Related proteins** (co-abundance neighbors): HSPA13 (0.84), TFRC (0.83), CD276 (0.82), ICAM1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 is the central network hub, with connections to every other module member and the greatest weighted connectivity in the supplied subgraph. Its documented roles include hypoxia response, endoplasmic-reticulum stress, protein folding, secretion-related trafficking, stress response, and negative regulation of apoptosis. It also has broad disease associations and the largest literature volume among the module genes.
- **Conclusion**: Established evidence supports HYOU1 as the best marker of a stress, hypoxia, and protein-folding component of the module and as its topological anchor. It is not established that HYOU1 physically interacts with the other module proteins in this module, because STRING and hu.MAP provide no supporting relationship. Its role as a coordinating biological driver remains a hypothesis.

#### TFRC

- **Related proteins** (co-abundance neighbors): HYOU1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes, Lysosomes; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transferrin receptor. This gene encodes a cell surface receptor necessary for cellular iron uptake by the process of receptor-mediated endocytosis. This receptor is required for erythropoiesis and neurologic development. Multiple alternatively spliced variants have been identified. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: TFRC-related combined immunodeficiency (0.623); type 2 diabetes mellitus (0.518); mucopolysaccharidosis type 2 (0.490); diabetes mellitus (0.471); diabetic retinopathy (0.343)
- **Europe PMC papers**: 14164
- **Why important**: TFRC is the transferrin receptor and supports receptor-mediated iron uptake, endocytosis, erythropoiesis, and neurologic development. It is the only module member explicitly marked as immune-cell enhanced, with an association to non-classical monocytes, and it is classified as secreted to blood by HPA. Its prostate protein detection and extensive disease literature make it an important bridge between cellular metabolism, tissue context, and possible blood or immune contribution.
- **Conclusion**: Established evidence supports TFRC as an iron-uptake and endocytic marker with potential relevance to immune-cell or blood-related composition. Its co-abundance with HYOU1 does not establish that iron metabolism causes the module or that the relationship is direct.

#### CD276

- **Related proteins** (co-abundance neighbors): HYOU1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD276 molecule. The protein encoded by this gene belongs to the immunoglobulin superfamily, and thought to participate in the regulation of T-cell-mediated immune response. Studies show that while the transcript of this gene is ubiquitously expressed in normal tissues and solid tumors, the protein is preferentially expressed only in tumor tissues. Additionally, it was observed that the 3' UTR of this transcript c…
- **Diseases (Open Targets)**: response to statin (0.321); Abnormality of the skeletal system (0.290); head and neck squamous cell carcinoma (0.228); prostate cancer (0.128); cancer (0.128)
- **Europe PMC papers**: 6027
- **Why important**: CD276 is an immunoglobulin-superfamily molecule implicated in regulation of cytokine production, type II interferon responses, T-cell proliferation, and T-cell activation. It is detected in prostate by HPA and is associated with trophoblast-related and Hofbauer-cell populations. Its disease annotations include prostate cancer and cancer, making it particularly relevant to interpreting a prostate-containing module.
- **Conclusion**: Established evidence supports CD276 as an immune-regulatory and disease-relevant component, especially in a prostate context. The module does not demonstrate that CD276 mediates immune suppression, tumor biology, or communication with HYOU1; those are possible interpretations requiring validation.

#### ICAM1

- **Related proteins** (co-abundance neighbors): HYOU1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: intercellular adhesion molecule 1. This gene encodes a cell surface glycoprotein which is typically expressed on endothelial cells and cells of the immune system. It binds to integrins of type CD11a / CD18, or CD11b / CD18 and is also exploited by Rhinovirus as a receptor. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.528); atrial fibrillation (0.407); vascular disorder (0.358); Crohn disease (0.340); lymphatic system disorder (0.285)
- **Europe PMC papers**: 19543
- **Why important**: ICAM1 is a plasma-membrane adhesion molecule typically expressed on endothelial and immune cells. It is associated with immune effector processes, leukocyte extravasation, T-cell activation, and cell adhesion, and HPA links it to macrophages and monocytes as well as tissue enhancement in lung and urinary bladder. It also has extensive disease literature, including neurodegenerative and vascular associations.
- **Conclusion**: Established evidence supports ICAM1 as an inflammation, leukocyte-adhesion, and cellular-extravasation marker. Its presence may indicate immune or vascular-cell involvement in the samples, but the module does not prove that ICAM1 is active in prostate or cerebrospinal fluid in this setting.

#### HSPA13

- **Related proteins** (co-abundance neighbors): HYOU1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 13. The protein encoded by this gene is a member of the heat shock protein 70 family and is found associated with microsomes. Members of this protein family play a role in the processing of cytosolic and secretory proteins, as well as in the removal of denatured or incorrectly-folded proteins. The encoded protein contains an ATPase domain and has been shown to associate with a ubiquitin-like protein. …
- **Diseases (Open Targets)**: septic shock (0.210); spermatocele (0.186); schizophrenia (0.141); secondary malignant neoplasm (0.122); protozoa infectious disease (0.121)
- **Europe PMC papers**: 594
- **Why important**: HSPA13 is a microsome-associated heat-shock protein-family member with an ATPase domain and reported roles in processing cytosolic and secretory proteins, removal of misfolded proteins, and protein refolding. It is cell-type enhanced in plasma cells, corticotrophs, and syncytiotrophoblasts, and its protein is detected in prostate. Although it has less literature than the major hub and receptors, it provides an independent protein-quality-control link to HYOU1.
- **Conclusion**: Established evidence supports HSPA13 as a protein-folding and microsomal stress component that reinforces the heat-shock interpretation. Its single network connection means it is not independently supported as a module-wide coordinator, and any direct functional partnership with HYOU1 remains unconfirmed here.
