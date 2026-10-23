# Conserved co-abundance modules: kidney and placenta

## Module 0

**Tissue pair**: kidney and placenta  
**Genes (7)**: ACTN1, CALU, CORO1C, FLNA, FLNB, FLNC, PFKP

### Function

The module is most consistent with an actin-cytoskeleton and membrane-anchoring program, centered on filamin-family proteins and associated actin-binding proteins. FLNA, FLNB, FLNC, and ACTN1 connect actin filaments to membrane or adhesion-associated structures and are annotated with actin filament organization, cytoskeletal organization, cell migration, platelet activation, or muscle-related functions. The module also includes CORO1C, which is linked to actin filament organization and phagocytosis, CALU, an endoplasmic-reticulum calcium-binding and protein-folding factor, and PFKP, a platelet-specific glycolytic enzyme. No GO or KEGG term passed global correction, so the functional interpretation is based on the gene annotations, network structure, and supplementary STRING evidence rather than globally significant pathway enrichment.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the genes are predominantly intracellular or membrane-associated, and only CALU has an intracellular-and-membrane secretome annotation. It is also not a broadly expressed housekeeping module. HPA evidence indicates tissue-enhanced or low-specificity expression together with strong cell-type associations, especially extravillous trophoblasts, platelets, smooth muscle cells, and related vascular or contractile cell populations. ACTN1 has immune-cell enhancement for neutrophils, whereas most genes have low immune-cell specificity and FLNC is not detected in immune cells. Thus, the shared kidney-placenta signal could reflect a conserved cytoskeletal program in trophoblast, vascular, smooth-muscle, platelet, or other contractile cells, and sample cellular composition should be considered before interpreting it as a universal kidney-placenta program. Protein detection in both tissues supports tissue presence, but does not by itself establish the responsible cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a biologically coherent filamin and actin-binding core. FLNA is connected to FLNB, FLNC, and ACTN1, while FLNB is connected to FLNC; these are high-confidence known relationships in the supplied STRING network. The supplementary STRING terms (STRING COMPARTMENTS Z disc; within-query FDR = 0.0158) through (STRING InterPro Immunoglobulin E-set; within-query FDR = 0.0356) converge on Z-disc localization, calponin-homology domains, filamin-type immunoglobulin domains, actinin-type actin binding, and filamin or actin-binding-protein repeats. These terms reinforce the structural interpretation, but they are not globally corrected GO or KEGG evidence. CORO1C connects the module to FLNC and FLNB in the co-abundance network, and PFKP connects to CORO1C; CALU connects to FLNC. No hu.MAP complex contains multiple module members. Therefore, part of the module recapitulates established protein relationships, while its full co-abundance pattern is broader than a currently represented hu.MAP complex.

**STRING interactions (score >= 0.7)**: 4 of 21 gene pairs: ACTN1–FLNA (0.716); FLNA–FLNB (0.979); FLNA–FLNC (0.907); FLNB–FLNC (0.921)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Z disc (FDR = 0.0158, 4 genes); SMART Calponin homology domain (FDR = 0.0158, 4 genes); SMART Filamin-type immunoglobulin domains (FDR = 0.0158, 3 genes); InterPro Actinin-type actin-binding domain, conserved site (FDR = 0.0174, 4 genes); InterPro Filamin/ABP280 repeat (FDR = 0.0309, 3 genes); InterPro Calponin homology domain (FDR = 0.0309, 4 genes); InterPro Filamin/ABP280 repeat-like (FDR = 0.0309, 3 genes); InterPro CH domain superfamily (FDR = 0.0309, 4 genes); InterPro Filamin family (FDR = 0.0309, 3 genes); InterPro Immunoglobulin E-set (FDR = 0.0356, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be described as wholly novel, because the FLNA-FLNB-FLNC-ACTN1 relationships and the associated actin-binding domain architecture are already represented by STRING and by well-established gene functions. At the same time, the kidney-placenta co-abundance configuration, including CORO1C, CALU, and PFKP, is not explained by a single hu.MAP complex and is not fully covered by the reported STRING relationships. The defensible conclusion is that this may be a new tissue-pair or co-abundance observation built around a known cytoskeletal core, but the fact sheet alone cannot establish discovery-level novelty. Absence from hu.MAP or from STRING would not, by itself, prove that the biological association is new.

**Hypothesis.** Hypothesis: the module represents coordinated remodeling and stabilization of actin-linked membrane and adhesion structures in shared kidney and placental cell populations, particularly extravillous trophoblasts, vascular or smooth-muscle cells, and platelets. FLNA, FLNB, FLNC, and ACTN1 could provide complementary actin-crosslinking or membrane-anchoring functions; CORO1C could link the structure to actin dynamics and vesicular or phagocytic behavior; CALU could support calcium-dependent endoplasmic-reticulum protein handling; and PFKP could provide glycolytic support in platelet-associated or metabolically active cells. This is a mechanistic model rather than a demonstrated pathway, and it requires cell-resolved expression, localization, and perturbation experiments.

### Important genes

#### FLNA

- **Related proteins** (co-abundance neighbors): FLNC (0.82), FLNB (0.81), ACTN1 (0.81); STRING partners: ACTN1 (0.716), FLNB (0.979), FLNC (0.907)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in kidney, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is a central network gene with connections to FLNB, FLNC, and ACTN1. Its established function is to crosslink actin, connect actin to membrane glycoproteins, and participate in cytoskeletal remodeling, cell shape, and migration. It is present in the kidney and placenta by HPA immunohistochemistry, is associated with vascular, intestinal, decidual stromal, hepatic stellate, and megakaryocyte cell types, and has extensive disease and literature support. It is included in every relevant supplementary STRING structural term listed in the fact sheet.
- **Conclusion**: Established evidence supports FLNA as a structural hub and a strong anchor for the module's actin-membrane interpretation. A possible but unproven implication is that FLNA coordinates the shared cytoskeletal state across vascular, trophoblast, or platelet-related cells in the two tissues.

#### FLNB

- **Related proteins** (co-abundance neighbors): FLNA (0.81), CORO1C (0.81), FLNC (0.80); STRING partners: FLNA (0.979), FLNC (0.921)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in kidney, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin B. This gene encodes a member of the filamin family. The encoded protein interacts with glycoprotein Ib alpha as part of the process to repair vascular injuries. The platelet glycoprotein Ib complex includes glycoprotein Ib alpha, and it binds the actin cytoskeleton. Mutations in this gene have been found in several conditions: atelosteogenesis type 1 and type 3; boomerang dysplasia; autosomal domina…
- **Diseases (Open Targets)**: Larsen syndrome (0.829); spondylocarpotarsal synostosis syndrome (0.775); atelosteogenesis type I (0.763); atelosteogenesis type III (0.756); Boomerang dysplasia (0.723)
- **Europe PMC papers**: 2274
- **Why important**: FLNB is directly connected in STRING to FLNA and FLNC and links the module to the filamin domain architecture represented by (STRING SMART Filamin-type immunoglobulin domains; within-query FDR = 0.0158), (STRING InterPro Filamin/ABP280 repeat; within-query FDR = 0.0309), (STRING InterPro Filamin/ABP280 repeat-like; within-query FDR = 0.0309), (STRING InterPro Filamin family; within-query FDR = 0.0309), and (STRING InterPro Immunoglobulin E-set; within-query FDR = 0.0356). Its annotated functions include actin-cytoskeleton organization and interaction with glycoprotein Ib alpha in vascular injury repair. HPA detects it in both tissues and associates it with extravillous trophoblasts and other epithelial or glandular cell types. Its skeletal and developmental disease associations provide substantial biological and clinical context.
- **Conclusion**: Established evidence supports FLNB as a filamin-family component that may connect cell adhesion and cytoskeletal organization in the module. Its trophoblast association makes it particularly relevant to the placenta side, but a kidney-placenta-specific mechanism remains a hypothesis.

#### FLNC

- **Related proteins** (co-abundance neighbors): CORO1C (0.87), FLNA (0.82), CALU (0.81), FLNB (0.80); STRING partners: FLNA (0.907), FLNB (0.921)
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin C. This gene encodes one of three related filamin genes, specifically gamma filamin. These filamin proteins crosslink actin filaments into orthogonal networks in cortical cytoplasm and participate in the anchoring of membrane proteins for the actin cytoskeleton. Three functional domains exist in filamin: an N-terminal filamentous actin-binding domain, a C-terminal self-association domain, and a membr…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy 26 (0.833); myofibrillar myopathy 5 (0.791); distal myopathy with posterior leg and anterior hand involvement (0.742); dilated cardiomyopathy (0.714); familial restrictive cardiomyopathy (0.660)
- **Europe PMC papers**: 3861
- **Why important**: FLNC has the strongest network position in the supplied module and connects to FLNA, FLNB, CORO1C, and CALU. It encodes a muscle-associated filamin that crosslinks actin and anchors membrane proteins, with annotations involving actin-cytoskeleton organization, sarcomere organization, and muscle-cell development. HPA links it to heart muscle, skeletal muscle, cardiomyocytes, myonuclei, smooth-muscle cells, and thymic myoid cells. Its cardiomyopathy and myopathy associations and extensive literature make it an important biological interpretive anchor, despite lack of kidney or placenta IHC detection in the supplied data.
- **Conclusion**: Established evidence supports FLNC as a structural and contractile-cell marker that helps explain the module's actin-binding architecture. The discrepancy between strong network centrality and absent tissue IHC detection suggests that transcript co-abundance, a minor cell population, or technical factors should be tested before assigning FLNC a dominant protein-level role in these tissues.

#### ACTN1

- **Related proteins** (co-abundance neighbors): FLNA (0.81); STRING partners: FLNA (0.716)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Actin filaments, Focal adhesion sites; IHC detected in kidney, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: actinin alpha 1. Alpha actinins belong to the spectrin gene superfamily which represents a diverse group of cytoskeletal proteins, including the alpha and beta spectrins and dystrophins. Alpha actinin is an actin-binding protein with multiple roles in different cell types. In nonmuscle cells, the cytoskeletal isoform is found along microfilament bundles and adherens-type junctions, where it is involved in binding …
- **Diseases (Open Targets)**: platelet-type bleeding disorder 15 (0.781); Macrothrombocytopenia (0.622); autosomal dominant macrothrombocytopenia (0.550); Thrombocytopenia (0.482); type 2 diabetes mellitus (0.410)
- **Europe PMC papers**: 3070
- **Why important**: ACTN1 links directly to FLNA and contributes the actinin-type actin-binding signal in (STRING COMPARTMENTS Z disc; within-query FDR = 0.0158), (STRING SMART Calponin homology domain; within-query FDR = 0.0158), (STRING InterPro Actinin-type actin-binding domain, conserved site; within-query FDR = 0.0174), (STRING InterPro Calponin homology domain; within-query FDR = 0.0309), and (STRING InterPro CH domain superfamily; within-query FDR = 0.0309). It is an actin-binding spectrin-superfamily protein involved in microfilament bundles, adherens-type junctions, focal adhesions, platelet activation, platelet formation, and platelet morphogenesis. HPA detects it in both tissues and associates it with extravillous trophoblasts, platelets, neutrophils, breast myoepithelial cells, and smooth-muscle-related populations. Its platelet-type bleeding disorder associations provide disease relevance.
- **Conclusion**: Established evidence supports ACTN1 as a membrane-associated actin-bundling component and a plausible indicator of platelet or trophoblast cytoskeletal biology. Its peripheral position in the module suggests a supporting rather than organizing role, although its cell-type specificity could make it informative about sample composition.

## Module 1

**Tissue pair**: kidney and placenta  
**Genes (6)**: AHNAK, EEA1, FASN, IQGAP1, PLEC, TLN1

### Function

The module most plausibly represents a cytoskeletal, cell-adhesion, and membrane-organization program, with contributions from focal-adhesion signaling, intermediate-filament organization, endosomal trafficking, and lipid biosynthesis. AHNAK, PLEC, TLN1, and IQGAP1 connect the module to cell shape, adhesion, migration, and cytoskeletal remodeling; EEA1 supports an endosomal component; and FASN supports a metabolic and lipid-synthesis component. The interpretation is necessarily cautious because no GO or KEGG term passed global correction: the globally significant GO/KEGG term set is empty. There is also no supplementary STRING enrichment in the supplementary STRING analysis. Thus, the network and gene functions support a coherent broad cellular interpretation, but not a formally globally enriched pathway assignment.

**Cell composition.** This is not a module dominated by plasma proteins, secreted proteins, or blood-cell-enriched genes. None of the genes is secreted, and the HPA summary reports low immune-cell specificity for most genes, with some genes not detected in immune cells. The tissue patterns are heterogeneous, including low tissue specificity and enhancement in adipose tissue, breast, liver, skeletal muscle, and blood vessel. The single-cell annotations are also diverse rather than concentrated in one shared kidney or placenta cell type. Most proteins are detected in both kidney and placenta, whereas FASN is not detected in either tissue by the supplied HPA protein evidence. These observations argue against interpreting the module as a simple plasma or blood-cell signature, while leaving open the possibility that shared structural cell populations or sample-composition effects contribute to the co-abundance pattern.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The supplied STRING evidence supports known relationships within a structural core: AHNAK is connected to PLEC, IQGAP1 is connected to TLN1, and PLEC is connected to TLN1. These links reinforce a cytoskeletal and adhesion interpretation, especially around TLN1, PLEC, and AHNAK. EEA1 and FASN have no reported STRING partners within this module. No hu.MAP complex contains multiple module members. Therefore, the module has partial support from known protein relationships but is not reproduced as a shared hu.MAP complex, and the co-abundance network should not be treated as proof of direct physical interaction for every edge.

**STRING interactions (score >= 0.7)**: 3 of 15 gene pairs: AHNAK–PLEC (0.73); IQGAP1–TLN1 (0.893); PLEC–TLN1 (0.706)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be called a wholly new biological pathway. Its component biology is established: TLN1, PLEC, AHNAK, and IQGAP1 are individually associated with cytoskeletal organization, adhesion, membrane interactions, or cell motility, while EEA1 and FASN have established roles in endosomal trafficking and fatty-acid synthesis. The particular co-abundance pattern shared by kidney and placenta may still be a new observation, especially because no multi-member hu.MAP complex is reported and only part of the network is supported by STRING. However, absence from STRING or hu.MAP alone does not establish novelty. The strongest defensible claim is that this may be a novel cross-tissue co-abundance configuration assembled from largely known cellular functions.

**Hypothesis.** Hypothesis: the module reflects coordinated remodeling of cell adhesion and cytoskeletal architecture in shared structural cell populations of kidney and placenta. In this model, TLN1 links integrin-associated adhesion to actin organization, IQGAP1 couples membrane signaling to cytoskeletal dynamics, and AHNAK and PLEC provide large structural scaffolds connecting membrane, actin, and intermediate-filament systems. EEA1 may represent coordinated endocytic trafficking at remodeling cell membranes, while FASN may provide lipid-synthesis capacity that supports membrane production or metabolic adaptation. This is a mechanistic hypothesis rather than an established pathway conclusion, because the globally significant GO/KEGG enrichment evidence is absent and the network contains only partial known-interaction support.

### Important genes

#### TLN1

- **Related proteins** (co-abundance neighbors): IQGAP1 (0.81), AHNAK (0.80); STRING partners: IQGAP1 (0.893), PLEC (0.706)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in kidney, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 is a central connector in the supplied network, linking IQGAP1 and PLEC, and it has the strongest direct interaction support among the module's adhesion-related genes. Its annotations connect it to focal adhesions, cell-cell junction assembly, integrin activation, actin organization, and cell adhesion. HPA places it in focal-adhesion sites and associates it with blood vessels and megakaryocyte or platelet-related cells. It also has substantial disease and literature evidence.
- **Conclusion**: Established evidence supports TLN1 as a core adhesion and cytoskeletal organizer and as an important anchor for the module's structural interpretation. It is plausible, but not established, that TLN1 coordinates the kidney-placenta co-abundance signal.

#### PLEC

- **Related proteins** (co-abundance neighbors): AHNAK (0.80); STRING partners: AHNAK (0.73), TLN1 (0.706)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments, Cytosol; IHC detected in kidney, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plectin. Plectin is a prominent member of an important family of structurally and in part functionally related proteins, termed plakins or cytolinkers, that are capable of interlinking different elements of the cytoskeleton. Plakins, with their multi-domain structure and enormous size, not only play crucial roles in maintaining cell and tissue integrity and orchestrating dynamic changes in cytoarchitecture…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 5B, with muscular dystrophy (0.796); epidermolysis bullosa simplex 5A, Ogna type (0.775); autosomal recessive limb-girdle muscular dystrophy type 2Q (0.768); epidermolysis bullosa simplex 5C, with pyloric atresia (0.755); epidermolysis bullosa simplex with nail dystrophy (0.695)
- **Europe PMC papers**: 2578
- **Why important**: PLEC is a large cytolinker with a direct STRING relationship to AHNAK and TLN1, placing it in the module's structural interaction core despite its peripheral network degree. Its annotations support intermediate-filament organization, actin organization, cell morphogenesis, and tissue integrity. HPA associates it with skeletal muscle and urothelial cells, and its disease associations include several inherited skin and muscular disorders. The supplied record also shows a substantial literature base.
- **Conclusion**: Established evidence supports PLEC as a cytoskeletal scaffold capable of integrating multiple filament systems. Its participation in a shared kidney-placenta structural program is a reasonable interpretation, but direct tissue-specific mechanism is not demonstrated here.

#### AHNAK

- **Related proteins** (co-abundance neighbors): EEA1 (0.83), TLN1 (0.80), PLEC (0.80); STRING partners: PLEC (0.73)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in kidney, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: AHNAK nucleoprotein. The protein encoded by this gene is a large (700 kDa) structural scaffold protein consisting of a central domain with 128 aa repeats. The encoded protein may play a role in such diverse processes as blood-brain barrier formation, cell structure and migration, cardiac calcium channel regulation, and tumor metastasis. A much shorter variant encoding a 17 kDa isoform exists for this gene, and the sho…
- **Diseases (Open Targets)**: Aganglionic megacolon (0.266); neoplasm (0.108); hepatocellular carcinoma (0.093); cancer (0.085); melanoma (0.085)
- **Europe PMC papers**: 2886
- **Why important**: AHNAK has the highest network connectivity in the module and links EEA1, TLN1, and PLEC. It is a very large structural scaffold associated with membrane organization, cell migration, plasma-membrane repair, and regulation of RNA splicing. HPA detects it in both kidney and placenta and places it at the plasma membrane and in the cytosol. Its disease and cancer associations and extensive literature record make it an important candidate for interpreting the module's membrane-cytoskeletal component.
- **Conclusion**: Established evidence supports AHNAK as a broad membrane-associated structural regulator and a plausible bridge between adhesion and endosomal features. Its role as the principal organizer of this particular module remains a hypothesis.

#### IQGAP1

- **Related proteins** (co-abundance neighbors): FASN (0.81), TLN1 (0.81); STRING partners: TLN1 (0.893)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in kidney, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IQ motif containing GTPase activating protein 1. This gene encodes a member of the IQGAP family. The protein contains four IQ domains, one calponin homology domain, one Ras-GAP domain and one WW domain. It interacts with components of the cytoskeleton, with cell adhesion molecules, and with several signaling molecules to regulate cell morphology and motility. Expression of the protein is upregulated by gene amplification in two gastric cancer ce…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.515); Costello syndrome (0.503); allergic rhinitis (0.474)
- **Europe PMC papers**: 3787
- **Why important**: IQGAP1 connects FASN to TLN1 and is directly linked to cell morphology, motility, adhesion-associated signaling, and growth-factor pathways. Its domain architecture and annotations support a role at the interface of signaling and cytoskeletal remodeling. HPA places it at the plasma membrane and cell junctions and reports enhancement in neutrophils, although the overall immune-cell specificity is low. It has a substantial literature record and multiple disease associations.
- **Conclusion**: Established evidence supports IQGAP1 as a signaling and cytoskeletal regulator that could connect adhesion dynamics with metabolic or membrane changes. Its proposed bridging role in this module is mechanistically plausible but not proven by the supplied co-abundance data.

#### EEA1

- **Related proteins** (co-abundance neighbors): AHNAK (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Vesicles; IHC detected in kidney, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: early endosome antigen 1. Enables 1-phosphatidylinositol binding activity; GTP-dependent protein binding activity; and protein homodimerization activity. Involved in endocytosis; vesicle fusion; and viral RNA genome replication. Located in cytosol and early endosome. Is extrinsic component of plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: autoimmune disorder of central nervous system (0.370); liver disorder (0.298); external ear disorder (0.273); benign digestive system neoplasm (0.256); Alzheimer disease (0.163)
- **Europe PMC papers**: 7344
- **Why important**: EEA1 is connected to AHNAK and is the module's clearest endosomal component. Its established functions include phosphatidylinositol binding, endocytosis, vesicle fusion, and early-endosome trafficking. HPA localizes it to vesicles, reports low cell-type specificity, and does not detect it in immune cells. The supplied record indicates a very extensive literature base, making it a strong interpretive marker even though it has no reported STRING partner within the module beyond the co-abundance edge.
- **Conclusion**: Established evidence supports EEA1 as an endocytic trafficking protein. Its association with AHNAK may indicate coordinated membrane turnover, but a direct functional connection within this module is only a hypothesis.

#### FASN

- **Related proteins** (co-abundance neighbors): IQGAP1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fatty acid synthase. The enzyme encoded by this gene is a multifunctional protein. Its main function is to catalyze the synthesis of palmitate from acetyl-CoA and malonyl-CoA, in the presence of NADPH, into long-chain saturated fatty acids. In some cancer cell lines, this protein has been found to be fused with estrogen receptor-alpha (ER-alpha), in which the N-terminus of FAS is fused in-frame with the C-terminus of …
- **Diseases (Open Targets)**: dengue disease (0.469); autism spectrum disorder (0.333); Parkinson disease (0.295); Epileptic encephalopathy (0.211); neurodegenerative disease (0.205)
- **Europe PMC papers**: 21528
- **Why important**: FASN is the module's metabolic outlier and connects to IQGAP1 in the co-abundance network. It catalyzes palmitate synthesis and is annotated to fatty-acid and lipid biosynthetic processes and nutrient response. HPA reports tissue enhancement in adipose tissue, breast, and liver and enrichment in breast lactating cells, while protein is not detected in the supplied kidney or placenta measurements. FASN has an especially extensive literature record and multiple disease associations.
- **Conclusion**: Established evidence supports FASN as a lipid-biosynthetic enzyme with broad metabolic and disease relevance. Its inclusion may reflect metabolic state or membrane-lipid demand rather than a stable structural complex; linking it mechanistically to IQGAP1 in kidney and placenta remains a hypothesis.

## Module 2

**Tissue pair**: kidney and placenta  
**Genes (8)**: HSPA5, CTNNA1, GANAB, HYOU1, PDIA4, RRBP1, SEPTIN9, TXNDC5

### Function

The module is most strongly characterized as an endoplasmic-reticulum protein quality-control and secretory-pathway module. The primary evidence is (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.000729), in which six module genes participate in protein processing in the endoplasmic reticulum, including chaperoning, disulfide-bond formation, glycan processing, and ER-associated secretory functions. The same biological interpretation is supported independently but only supplementarily by (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.00027) through (STRING Keyword Endoplasmic reticulum; within-query FDR = 0.021). HSPA5, HYOU1, PDIA4, TXNDC5, GANAB, and RRBP1 form the core annotated ER-processing group, while CTNNA1 and SEPT9 may connect the module to cell-junction or cytoskeletal context rather than define its principal function.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the HPA annotations describe the proteins mainly as intracellular or membrane-associated, with several localized to the ER. All module proteins were detected in placenta and nearly all were detected in kidney. Most genes have low tissue specificity, but the single-cell annotations show enrichment in cell types with substantial secretory or epithelial specialization, including plasma cells, extravillous trophoblasts, syncytiotrophoblasts, acinar cells, and related epithelial populations. The concentration of plasma-cell annotations for several genes and the blood-cell annotations for TXNDC5 and RRBP1 raise the possibility that shared immune or secretory-cell content contributes to the cross-tissue signal. However, the module is not simply a blood-cell module because most genes have low immune-cell specificity and the principal functional genes are broadly expressed ER machinery.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human) | 0.000729 | GANAB, HSPA5, HYOU1, PDIA4, RRBP1, TXNDC5 |

### STRING and hu.MAP

STRING provides a coherent interaction neighborhood centered on HSPA5, with strong links to HYOU1, PDIA4, GANAB, and TXNDC5; HYOU1 and PDIA4 are also strongly connected. STRING supplementary enrichment recapitulates ER protein processing, ER quality control, protein-disulfide-isomerase activity, and an unfolded-protein-response context (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.00027) through (STRING Keyword Endoplasmic reticulum; within-query FDR = 0.021). These STRING results are concordant with, but do not replace, the globally corrected primary evidence (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.000729). hu.MAP identifies recurring co-membership of PDIA4, GANAB, and HYOU1 in (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), and HSPA5 with HYOU1 in (hu.MAP huMAP3_07455.1). Because the hu.MAP complexes contain many additional proteins and only a subset of their members occurs in this module, they support shared complex or pathway context rather than proving that the entire module is one discrete complex. CTNNA1, RRBP1, and SEPT9 have no listed STRING partners within the supplied evidence, so their module links may reflect co-abundance or indirect cellular coordination rather than established physical interaction.

**STRING interactions (score >= 0.7)**: 7 of 28 gene pairs: GANAB–HSPA5 (0.846); GANAB–HYOU1 (0.83); GANAB–PDIA4 (0.717); HSPA5–HYOU1 (0.999); HSPA5–PDIA4 (0.99); HSPA5–TXNDC5 (0.798); HYOU1–PDIA4 (0.997)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Protein processing in endoplasmic reticulum (FDR = 0.00027, 6 genes); NetworkNeighborAL Mixed, incl. Photodynamic therapy-induced unfolded protein response, and Endoplasmic reticulum quality control compartment (FDR = 0.002, 5 genes); NetworkNeighborAL Mixed, incl. Photodynamic therapy-induced unfolded protein response, and Protein disulfide isomerase activity (FDR = 0.0036, 4 genes); NetworkNeighborAL Photodynamic therapy-induced unfolded protein response, and IRE1-TRAF2-ASK1 complex (FDR = 0.019, 3 genes); Keyword Endoplasmic reticulum (FDR = 0.021, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (PDIA4, GANAB, HYOU1; 3/60); huMAP3_09327.1 (PDIA4, GANAB, HYOU1; 3/93); huMAP3_07455.1 (HSPA5, HYOU1; 2/4)

### Novelty

The ER protein-processing theme itself is established rather than novel: it is supported by the globally significant pathway (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.000729), concordant STRING evidence, and known hu.MAP complex membership. The potentially new aspect is the specific kidney–placenta co-abundance configuration, especially the combination of ER quality-control genes with RRBP1, CTNNA1, and SEPT9. However, this cannot be claimed as a new biological mechanism from the fact sheet alone. Absence of listed STRING or hu.MAP relationships for some genes does not establish novelty, and shared secretory-cell composition or sample-cell admixture could generate part of the cross-tissue association. A defensible conclusion is that the module is a new or potentially informative cross-tissue co-abundance observation, but not a demonstrated novel ER complex or pathway.

**Hypothesis.** Hypothesis: in kidney and placenta, a shared population of secretory, epithelial, trophoblast, or immune-secretory cells increases coordinated demand for ER folding, glycoprotein maturation, disulfide-bond formation, and secretory trafficking. HSPA5 and HYOU1 may provide chaperone and stress-response support, PDIA4 and TXNDC5 may promote oxidative folding, GANAB may support N-glycan quality control, and RRBP1 may organize ER-bound ribosome and secretory functions. CTNNA1 and SEPT9 could reflect coupling of this secretory state to cell adhesion or cytoskeletal organization. This is a mechanistic model, not an established causal conclusion; it should be tested with cell-composition adjustment, spatial or single-cell measurements, and perturbation of the ER-quality-control genes.

### Important genes

#### HSPA5

- **Related proteins** (co-abundance neighbors): HYOU1 (0.82), GANAB (0.81), TXNDC5 (0.80); STRING partners: GANAB (0.846), HYOU1 (0.999), PDIA4 (0.99), TXNDC5 (0.798)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in kidney, placenta
- **hu.MAP 3.0**: huMAP3_07455.1
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is the most central gene in the module by the supplied network position and connects to HYOU1, GANAB, and TXNDC5. It is included in the primary pathway (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.000729) and every listed STRING enrichment term (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.00027) through (STRING Keyword Endoplasmic reticulum; within-query FDR = 0.021). Its established function is as an ER HSP seventy chaperone and regulator of ER homeostasis, and it has extensive literature and disease-association coverage.
- **Conclusion**: Established evidence supports HSPA5 as the principal chaperone and network hub of the module. The hypothesis that it coordinates the kidney–placenta co-abundance state is plausible but cannot be inferred as causation from co-abundance alone.

#### PDIA4

- **Related proteins** (co-abundance neighbors): HYOU1 (0.84), CTNNA1 (0.83); STRING partners: GANAB (0.717), HSPA5 (0.99), HYOU1 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in kidney, placenta
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 has strong module connections to HYOU1 and CTNNA1 and is a member of two hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). It belongs to the primary ER-processing overlap (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.000729) and all listed STRING enrichment terms (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.00027) through (STRING Keyword Endoplasmic reticulum; within-query FDR = 0.021). Its established biochemical role is ER thiol-disulfide exchange and protein folding, including support of immunoglobulin assembly, and it has substantial disease and literature associations.
- **Conclusion**: Established evidence identifies PDIA4 as a core oxidative-folding component and a bridge between the central ER chaperone group and the CTNNA1-linked branch. Its contribution to a tissue-specific secretory adaptation remains a hypothesis.

#### HYOU1

- **Related proteins** (co-abundance neighbors): PDIA4 (0.84), HSPA5 (0.82); STRING partners: GANAB (0.83), HSPA5 (0.999), PDIA4 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1, huMAP3_07455.1
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 is strongly connected to HSPA5 and PDIA4, occurs in all three listed hu.MAP complexes (hu.MAP huMAP3_06775.1) through (hu.MAP huMAP3_07455.1), and is included in (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.000729) and every STRING enrichment term (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.00027) through (STRING Keyword Endoplasmic reticulum; within-query FDR = 0.021). Its established annotations link it to ER folding and secretion, hypoxia, ER stress, ischemia response, and protection from apoptosis. It is detected in placenta and has cell-type annotations that include plasma cells.
- **Conclusion**: Established evidence supports HYOU1 as a stress-responsive ER chaperone that may be particularly relevant to placental physiology. Linking its co-abundance to hypoxic or ischemic signaling in this module is a hypothesis requiring direct physiological testing.

#### GANAB

- **Related proteins** (co-abundance neighbors): HSPA5 (0.81); STRING partners: HSPA5 (0.846), HYOU1 (0.83), PDIA4 (0.717)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in kidney, placenta
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: glucosidase II alpha subunit. This gene encodes the alpha subunit of glucosidase II and a member of the glycosyl hydrolase 31 family of proteins. The heterodimeric enzyme glucosidase II plays a role in protein folding and quality control by cleaving glucose residues from immature glycoproteins in the endoplasmic reticulum. Expression of the encoded protein is elevated in lung tumor tissue and in response to UV irradiation. Mut…
- **Diseases (Open Targets)**: polycystic kidney disease 3 with or without polycystic liver disease (0.792); autosomal dominant polycystic liver disease (0.515); autosomal dominant polycystic kidney disease (0.470); Biliary tract abnormality (0.438); COVID-19 (0.370)
- **Europe PMC papers**: 1240
- **Why important**: GANAB connects to HSPA5 and is also linked to HYOU1 and PDIA4 in STRING. It occurs with PDIA4 and HYOU1 in hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1) and contributes to the primary pathway (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.000729) as well as supplementary terms (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.00027) and (STRING Keyword Endoplasmic reticulum; within-query FDR = 0.021). Its established function is the alpha subunit of glucosidase II, which removes glucose residues during ER glycoprotein folding and quality control. It also has a strong established association with autosomal-dominant polycystic kidney and liver disease.
- **Conclusion**: Established evidence places GANAB in ER glycoprotein quality control and gives it particular relevance to kidney biology. Its presence in the shared module may indicate coordinated glycoprotein maturation, but a kidney–placenta-specific role is not established.

#### RRBP1

- **Related proteins** (co-abundance neighbors): CTNNA1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in kidney, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosome binding protein 1. This gene encodes a ribosome-binding protein of the endoplasmic reticulum (ER) membrane. Studies suggest that this gene plays a role in ER proliferation, secretory pathways and secretory cell differentiation, and mediation of ER-microtubule interactions. Alternative splicing has been observed and protein isoforms are characterized by regions of N-terminal decapeptide and C-terminal heptad repeats.…
- **Diseases (Open Targets)**: cancer (0.476); dengue disease (0.462); neurodegenerative disease (0.324); coronary artery disorder (0.292); placental abruption (0.279)
- **Europe PMC papers**: 1654
- **Why important**: RRBP1 is part of the primary pathway (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.000729) and supplementary STRING terms (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.00027) and (STRING NetworkNeighborAL Mixed, incl. Photodynamic therapy-induced unfolded protein response, and Endoplasmic reticulum quality control compartment; within-query FDR = 0.002). Although it has no listed STRING partner, its module connection to CTNNA1 and its ER localization are informative. Its established functions include ER ribosome binding, ER proliferation, secretory pathways, ER–microtubule interactions, and secretory-cell differentiation. Its HPA annotations include syncytiotrophoblasts, acinar cells, and selected immune-cell populations, making it relevant to the cellular-composition interpretation.
- **Conclusion**: Established evidence supports RRBP1 as an ER architecture and secretory-pathway component that may connect the core folding machinery to specialized secretory cells. Its role as a determinant of the cross-tissue module, rather than a correlated marker of cell composition, remains a hypothesis.
