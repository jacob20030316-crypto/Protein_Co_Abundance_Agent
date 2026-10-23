# Conserved co-abundance modules: placenta and rectum

## Module 0

**Tissue pair**: placenta and rectum  
**Genes (6)**: AKAP12, CSRP1, DPYSL3, FLNA, FLNC, PDLIM7

### Function

The module is most consistent with a contractile, actin-associated cytoskeletal and membrane-signaling program. FLNA and FLNC are filamin proteins that crosslink actin and connect the cytoskeleton with membrane-associated proteins. PDLIM7 links PDZ and LIM domain functions to actin filaments, focal adhesions, and muscle structure. CSRP1 is associated with sarcomere organization, muscle development, and platelet aggregation. DPYSL3 has filamin-binding activity and is associated with actin organization and cell migration, while AKAP12 provides a signaling-scaffold function through localized protein kinase A, protein kinase C, and phosphatase interactions. The network therefore suggests coordinated regulation of cell shape, adhesion, contractility, and signal transduction, particularly in vascular or smooth-muscle-related cells. No GO or KEGG term passed global correction, so this functional interpretation is based on the gene annotations, network structure, HPA evidence, and individual-gene biology rather than on globally significant pathway enrichment.

**Cell composition.** The module is not composed of plasma or secreted proteins: the secreted-protein annotation is absent for all members. It is also not broadly characterized as an immune-cell module. Most genes show cell-type-enhanced or group-enriched expression, with smooth muscle cells represented across the module and vascular smooth muscle cells represented for much of it. Blood-vessel, intestine, skeletal-muscle, and heart-muscle tissue associations are recurrent. Decidual stromal cells, myoepithelial cells, hepatic stellate cells, megakaryocytes, and neutrophils also occur among the HPA annotations. This profile favors a structural and contractile cell-state signal shared by vascular, stromal, smooth-muscle, or related cells in placenta and rectum. The blood-cell annotations, especially for PDLIM7 and selected other members, mean that a contribution from shared cellular composition cannot be excluded, but the overall pattern does not support a simple plasma-protein or generic blood-contamination explanation. Protein detection in both tissues supports tissue presence for much of the module, although not every member is detected by immunohistochemistry in each tissue.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known STRING relationship in the module is FLNA--FLNC. This supports a real connection between the two filamin proteins and is compatible with their shared actin-crosslinking roles. The remaining module relationships are not supported by high-confidence STRING pair evidence in the supplied results, and STRING functional enrichment is absent. No hu.MAP complex contains multiple module members. Thus, the co-abundance structure is broader than the currently documented physical-interaction structure: it may represent a coordinated cell state or shared regulatory program rather than a single established protein complex. The FLNA--FLNC relationship provides an anchored structural connection, while the links involving CSRP1, PDLIM7, DPYSL3, and AKAP12 should be treated as co-abundance relationships or biologically plausible associations rather than proven direct physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: FLNA–FLNC (0.907)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may represent a previously unreported cross-tissue co-abundance pattern, but the supplied evidence is insufficient to call it a new molecular complex or a definitively novel biological pathway. The absence of a multi-member hu.MAP complex and the limited STRING support indicate that the exact six-gene combination is not already established as a canonical complex in these resources. However, absence from STRING or hu.MAP does not prove novelty, because those resources emphasize experimentally supported physical interactions and curated complexes, whereas co-abundance can arise from shared cell type, regulation, tissue composition, or indirect pathway coupling. The most defensible conclusion is that the cross-tissue module configuration is potentially novel, while its individual biological themes are established and recognizable.

**Hypothesis.** Hypothesis: the shared placenta--rectum module reflects a conserved smooth-muscle, vascular, or stromal structural state in which filamin-mediated actin organization is coordinated with focal-adhesion and sarcomeric scaffolding and with localized cyclic-AMP or related signaling. FLNA and FLNC may provide the central cytoskeletal framework; PDLIM7 and CSRP1 may stabilize actin-associated and muscle-related structures; DPYSL3 may connect filamin biology to cell projection or migration processes; and AKAP12 may spatially organize signaling inputs. The same program could be observed in both tissues because they contain related vascular, stromal, or contractile cell populations. This is a mechanistic hypothesis, not a demonstrated physical complex or causal pathway.

### Important genes

#### FLNC

- **Related proteins** (co-abundance neighbors): FLNA (0.97), CSRP1 (0.94), AKAP12 (0.88), DPYSL3 (0.83), PDLIM7 (0.83); STRING partners: FLNA (0.907)
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin C. This gene encodes one of three related filamin genes, specifically gamma filamin. These filamin proteins crosslink actin filaments into orthogonal networks in cortical cytoplasm and participate in the anchoring of membrane proteins for the actin cytoskeleton. Three functional domains exist in filamin: an N-terminal filamentous actin-binding domain, a C-terminal self-association domain, and a membr…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy 26 (0.833); myofibrillar myopathy 5 (0.791); distal myopathy with posterior leg and anterior hand involvement (0.742); dilated cardiomyopathy (0.714); familial restrictive cardiomyopathy (0.660)
- **Europe PMC papers**: 3861
- **Why important**: FLNC is among the most connected members of the module and links to every other member in the supplied co-abundance subgraph. It is an actin-crosslinking protein involved in sarcomere organization and muscle-cell development, has tissue enhancement in heart and skeletal muscle, and is detected in rectum. Its established disease associations include cardiomyopathy and myofibrillar myopathy. It also forms the strongest supplied STRING relationship with FLNA, giving the module a clear structural anchor. Its substantial literature support makes it a particularly informative entry point for interpreting the module.
- **Conclusion**: Established evidence supports FLNC as a central actin and muscle-structural component and as a partner of FLNA. The hypothesis that it organizes the entire cross-tissue module is plausible from its network position but is not demonstrated by the supplied interaction or enrichment evidence.

#### FLNA

- **Related proteins** (co-abundance neighbors): FLNC (0.97), CSRP1 (0.92), PDLIM7 (0.86), DPYSL3 (0.82); STRING partners: FLNC (0.907)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in placenta, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is a highly connected module member with tissue enhancement in blood vessel and intestine and protein detection in both placenta and rectum. It crosslinks actin, connects actin to membrane glycoproteins, and participates in cell-shape remodeling and migration. Its annotations include platelet activation and blood coagulation-related biology, while its established disease associations include several developmental skeletal and neuronal syndromes. It has the strongest literature representation among the module genes and is the known STRING partner of FLNC.
- **Conclusion**: Established evidence supports FLNA as a membrane-linked actin organizer that could explain the vascular, intestinal, stromal, and contractile context. A coordinating role in the shared module is a hypothesis based on its connectivity and biology, not proof that FLNA drives the observed co-abundance.

#### PDLIM7

- **Related proteins** (co-abundance neighbors): FLNA (0.86), CSRP1 (0.83), FLNC (0.83), DPYSL3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Actin filaments, Focal adhesion sites; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 7. The protein encoded by this gene is representative of a family of proteins composed of conserved PDZ and LIM domains. LIM domains are proposed to function in protein-protein recognition in a variety of contexts including gene transcription and development and in cytoskeletal interaction. The LIM domains of this protein bind to protein kinases, whereas the PDZ domain binds to actin filaments. The g…
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); nasopharyngeal carcinoma (0.121); neoplasm (0.120); lymphoma (0.115); Hodgkins lymphoma (0.105)
- **Europe PMC papers**: 808
- **Why important**: PDLIM7 occupies a well-connected position and is linked in the supplied network to FLNA, CSRP1, FLNC, and DPYSL3. Its PDZ and LIM domains support interactions with actin filaments and protein kinases, and its annotations include actin cytoskeleton organization, heart development, muscle structure development, focal adhesions, and membrane-associated architecture. HPA associates it with blood vessels, skeletal muscle, smooth-muscle-related cells, and several blood-cell categories, making it useful for interpreting both the structural and cell-composition dimensions of the module.
- **Conclusion**: Established evidence supports PDLIM7 as a cytoskeletal and signaling adaptor with relevance to muscle and focal-adhesion organization. Its blood-cell annotations require caution about cellular composition, while its proposed role in coupling the other module members is mechanistic speculation.

#### CSRP1

- **Related proteins** (co-abundance neighbors): FLNC (0.94), FLNA (0.92), DPYSL3 (0.87), PDLIM7 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in placenta, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cysteine and glycine rich protein 1. This gene encodes a member of the cysteine-rich protein (CSRP) family. This gene family includes a group of LIM domain proteins, which may be involved in regulatory processes important for development and cellular differentiation. The LIM/double zinc-finger motif found in this gene product occurs in proteins with critical functions in gene regulation, cell growth, and somatic differentiation. Alte…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy (0.272); placenta praevia (0.160); Varicose veins (0.113); acute myeloid leukemia (0.091); hepatocellular carcinoma (0.084)
- **Europe PMC papers**: 822
- **Why important**: CSRP1 is highly connected within the module and is associated with FLNC, FLNA, DPYSL3, and PDLIM7. It is a LIM-domain protein involved in regulatory and differentiation-related processes, with annotations for sarcomere organization, muscle development, and platelet aggregation. HPA places it in blood-vessel and intestinal tissue contexts and detects it in both tissues, with cell-type associations including decidual stromal cells, extravillous trophoblasts, myoepithelial cells, hepatic stellate cells, and megakaryocytes. Its disease links include hypertrophic cardiomyopathy and placenta-related disease, although these associations are less established than those of the filamin genes.
- **Conclusion**: Established evidence supports CSRP1 as a muscle- and differentiation-associated LIM protein that fits the module's structural theme and placenta context. Its contribution to a shared contractile or stromal state is a reasonable hypothesis, but the supplied data do not establish a direct complex with the other genes.

#### DPYSL3

- **Related proteins** (co-abundance neighbors): CSRP1 (0.87), FLNC (0.83), AKAP12 (0.82), FLNA (0.82), PDLIM7 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dihydropyrimidinase like 3. Enables filamin binding activity. Predicted to be involved in several processes, including actin filament organization; regulation of plasma membrane bounded cell projection organization; and response to axon injury. Predicted to act upstream of or within nervous system development. Predicted to be located in several cellular components, including cell body; growth cone; and lamellipodium. Predict…
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); brain compression (0.326); edema (0.326); liver disorder (0.214); alcohol drinking (0.200)
- **Europe PMC papers**: 1082
- **Why important**: DPYSL3 is one of the most connected genes in the co-abundance subgraph and is linked to all of the central structural members except that its supplied STRING partner list is empty. It has filamin-binding activity and annotations involving actin organization, cell migration, cell projections, neuronal development, and response to axon injury. Its broad tissue specificity and absence of immune-cell detection make it potentially informative as a general cytoskeletal or migratory component rather than as a tissue-restricted marker. Its literature volume is meaningful, though smaller than that of FLNA or FLNC.
- **Conclusion**: Established evidence supports DPYSL3 as a filamin-binding cytoskeletal regulator with possible relevance to migration and cell architecture. Its placement in this module suggests coordinated structural regulation, but the cross-tissue smooth-muscle interpretation remains a hypothesis because its individual annotations are broader and partly neuronal.

## Module 1

**Tissue pair**: placenta and rectum  
**Genes (9)**: ANXA4, CTNNA1, HNRNPK, HYOU1, KRT18, KRT19, KRT8, PDIA4, CCT8

### Function

No GO or KEGG term passed global correction, so the module does not have a statistically established pathway-level annotation from those analyses. Its gene-level biology instead supports a mixed epithelial structural and proteostasis module. KRT8, KRT18, and KRT19 form a known simple-epithelial intermediate-filament component, while CTNNA1 links epithelial adhesion to the actin cytoskeleton. PDIA4 and HYOU1 represent endoplasmic-reticulum protein folding, disulfide-bond processing, secretion, and stress-response biology. CCT8 and HNRNPK provide additional protein-folding and RNA-processing context. ANXA4 is compatible with epithelial membrane trafficking and differentiation. Thus, the most defensible interpretation is coordinated epithelial-cell abundance with contributions from protein quality control, rather than a uniquely demonstrated biochemical pathway. These are gene-function interpretations, not globally significant enrichment results.

**Cell composition.** The module is not predominantly a plasma-protein or secreted-protein module: only a minority of its genes are classified as secreted, and PDIA4 and HYOU1 are intracellular or membrane-associated ER proteins rather than freely circulating proteins. All module proteins are detected in both placenta and rectum by HPA. Most genes have low tissue specificity, while several show epithelial or organ-associated enrichment, including intestine, esophagus, gallbladder, pancreas, and salivary gland patterns. Single-cell evidence repeatedly points to colonocytes and trophoblast populations, with additional pancreatic duct, syncytiotrophoblast, and related epithelial populations. The blood-cell signal is limited and heterogeneous, with most genes showing low immune-cell specificity; isolated immune-cell annotations for KRT8 and KRT18 should not by themselves imply a blood-cell module. The shared module may therefore reflect common epithelial or trophoblast-like cellular programs, and could also be influenced by the cellular composition of the tissue samples.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a tightly connected keratin subnetwork: KRT18 with KRT8, KRT18 with KRT19, and KRT19 with KRT8. STRING also supports a very strong PDIA4-HYOU1 relationship. These are established database-supported relationships and make the epithelial-filament and ER-proteostasis interpretations more credible. No STRING functional-enrichment result was returned. hu.MAP places PDIA4 and HYOU1 together in both (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), but they represent only a small subset of the much larger complexes; this supports their participation in broader ER or protein-processing assemblies without proving that the entire module is one physical complex. The remaining module connections are not supported by the reported high-confidence STRING interactions or by reported hu.MAP co-membership, so the co-abundance network extends beyond currently catalogued physical interactions.

**STRING interactions (score >= 0.7)**: 4 of 36 gene pairs: HYOU1–PDIA4 (0.997); KRT18–KRT19 (0.928); KRT18–KRT8 (0.999); KRT19–KRT8 (0.796)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (PDIA4, HYOU1; 2/60); huMAP3_09327.1 (PDIA4, HYOU1; 2/93)

### Novelty

The module should not be claimed as a wholly new molecular complex or pathway. Several components are already well established: the KRT8-KRT18-KRT19 epithelial-filament relationships are known, and PDIA4-HYOU1 co-membership is represented in hu.MAP and STRING. The potentially novel aspect is the cross-tissue co-abundance configuration that combines these epithelial structural genes with ER quality-control genes and additional adhesion, chaperone, and RNA-processing genes in placenta and rectum. However, the fact that some edges are absent from STRING or hu.MAP is not evidence of biological novelty, because database coverage and assay context are incomplete. A cautious conclusion is that this is a potentially interesting tissue-pair-specific co-abundance pattern built partly from known biology, requiring replication and orthogonal validation before being described as a new mechanism.

**Hypothesis.** Hypothesis: the module reflects abundance of a shared epithelial or trophoblast-like cell program in placenta and rectum. In this model, KRT8, KRT18, KRT19, and CTNNA1 provide epithelial structural and adhesion support, while PDIA4 and HYOU1 buffer ER folding and secretory stress associated with production and trafficking of membrane or secreted proteins. CCT8 could support cytosolic protein maturation, HNRNPK could contribute to RNA processing, and ANXA4 could connect the program to epithelial membrane dynamics. The observed co-abundance could arise from coordinated cell-state regulation or shared cellular composition rather than direct physical interaction among every module member. This hypothesis predicts that module activity should track epithelial or trophoblast abundance and markers of ER stress or secretory load, and should be tested with cell-resolved expression, spatial data, and protein-level measurements.

### Important genes

#### PDIA4

- **Related proteins** (co-abundance neighbors): CCT8 (0.82), CTNNA1 (0.81), KRT18 (0.81), ANXA4 (0.81); STRING partners: HYOU1 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in placenta, rectum
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 has the strongest network position in the module and connects to CCT8, CTNNA1, KRT18, and ANXA4. It is an ER protein-disulfide isomerase with multiple thioredoxin domains and an ER-retention sequence. Its reported roles in protein folding, secretion, and ER stress, its high-confidence STRING relationship with HYOU1, and its membership in (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1) make it the principal bridge between epithelial-associated genes and proteostasis biology. Its substantial literature and disease associations also make it a practical candidate for follow-up.
- **Conclusion**: Established evidence supports PDIA4 as an ER folding and secretion factor and as a central co-abundance bridge. It is plausible, but not established, that PDIA4 coordinates ER proteostasis with the epithelial program in this module.

#### KRT18

- **Related proteins** (co-abundance neighbors): KRT8 (0.87), ANXA4 (0.84), PDIA4 (0.81); STRING partners: KRT19 (0.928), KRT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in placenta, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 18. KRT18 encodes the type I intermediate filament chain keratin 18. Keratin 18, together with its filament partner keratin 8, are perhaps the most commonly found members of the intermediate filament gene family. They are expressed in single layer epithelial tissues of the body. Mutations in this gene have been linked to cryptogenic cirrhosis. Two transcript variants encoding the same protein have bee…
- **Diseases (Open Targets)**: cirrhosis of liver (0.623); cirrhosis, familial (0.396); prostate carcinoma (0.140); neoplasm (0.117); breast carcinoma (0.113)
- **Europe PMC papers**: 6539
- **Why important**: KRT18 is a high-connectivity module member linking KRT8, KRT19, ANXA4, and PDIA4. It is a type one intermediate-filament protein expressed in simple epithelia and is associated with epithelial organization, cell-cell adhesion, and apoptosis-related biology. HPA identifies it in colonocyte and trophoblast-related cell types, and it has extensive literature and established disease associations involving liver cirrhosis and neoplasia.
- **Conclusion**: Established evidence supports KRT18 as a structural marker of simple epithelial cells and as part of the known KRT8-KRT18 filament system. Its connection to PDIA4 in this co-abundance module may indicate shared epithelial state or cellular composition; a direct functional link to PDIA4 remains a hypothesis.

#### KRT8

- **Related proteins** (co-abundance neighbors): KRT19 (0.88), KRT18 (0.87); STRING partners: KRT18 (0.999), KRT19 (0.796)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Intermediate filaments; IHC detected in placenta, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 8. This gene is a member of the type II keratin family clustered on the long arm of chromosome 12. Type I and type II keratins heteropolymerize to form intermediate-sized filaments in the cytoplasm of epithelial cells. The product of this gene typically dimerizes with keratin 18 to form an intermediate filament in simple single-layered epithelial cells. This protein plays a role in maintaining cellul…
- **Diseases (Open Targets)**: cirrhosis of liver (0.596); cirrhosis, familial (0.401); neurodegenerative disease (0.371); prostate carcinoma (0.314); Abnormality of the liver (0.306)
- **Europe PMC papers**: 5942
- **Why important**: KRT8 is part of the most coherent STRING-supported subnetwork, with relationships to KRT18 and KRT19, and it has tissue enhancement in intestine and stomach together with cell-type enhancement in colonocytes, enterocytes, goblet cells, and trophoblast-related populations. It encodes a type two keratin that typically dimerizes with KRT18 and contributes to epithelial structural integrity, differentiation, and signaling. Its disease associations and extensive literature further support its importance as an epithelial-state indicator.
- **Conclusion**: Established evidence supports KRT8 as a core simple-epithelial intermediate-filament component and a strong indicator of the epithelial contribution to the module. The module does not establish that KRT8 drives the shared placenta-rectum program rather than marking the abundance of the relevant cells.

#### HYOU1

- **Related proteins** (co-abundance neighbors): CCT8 (0.84), HNRNPK (0.82); STRING partners: PDIA4 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in placenta, rectum
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 links CCT8 and HNRNPK in the network and has a very strong STRING relationship with PDIA4. It is an ER heat-shock-family protein induced in hypoxic and stress contexts and is associated with protein folding, secretion, ER-to-Golgi transport, hypoxia, and protection from apoptosis. It is represented with PDIA4 in both (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), and its detection in both tissues supports relevance to the shared module.
- **Conclusion**: Established evidence supports HYOU1 as an ER stress and protein-folding factor that forms a known database-supported relationship with PDIA4. It is a reasonable candidate mediator of secretory or hypoxic stress in the module, but the co-abundance data do not prove that such stress is the cause of the tissue-pair pattern.

#### CTNNA1

- **Related proteins** (co-abundance neighbors): CCT8 (0.83), PDIA4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in placenta, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin alpha 1. This gene encodes a member of the catenin family of proteins that play an important role in cell adhesion process by connecting cadherins located on the plasma membrane to the actin filaments inside the cell. The encoded mechanosensing protein contains three vinculin homology domains and undergoes conformational changes in response to cytoskeletal tension, resulting in the reconfiguration of cadhe…
- **Diseases (Open Targets)**: Butterfly-shaped pigment dystrophy (0.750); hereditary neoplastic syndrome (0.557); hereditary diffuse gastric adenocarcinoma (0.555); colorectal cancer (0.506); exudative vitreoretinopathy (0.390)
- **Europe PMC papers**: 2688
- **Why important**: CTNNA1 connects PDIA4 and CCT8 and provides the clearest adhesion-related element in the network. It links cadherin-based cell junctions to actin filaments and functions as a mechanosensitive component of epithelial architecture. HPA places it at the plasma membrane and cell junctions, while its reported functions include adhesion, migration, and gap-junction assembly. Its disease associations include inherited epithelial and neoplastic conditions.
- **Conclusion**: Established evidence supports CTNNA1 as an epithelial junction and cytoskeletal-linking protein. Its position suggests a possible interface between epithelial architecture and ER or protein-maturation programs, but that cross-compartment mechanism is a hypothesis rather than a demonstrated interaction.

## Module 2

**Tissue pair**: placenta and rectum  
**Genes (5)**: HSPA5, CANX, CLTC, VDAC2, VPS35

### Function

This module most plausibly represents a conserved intracellular protein-trafficking and proteostasis program linking endosomal trafficking, clathrin-mediated transport, endoplasmic-reticulum quality control, and mitochondrial membrane biology. VPS35 and CLTC connect the module to endosomal and coated-vesicle trafficking, while CANX and HSPA5 support protein folding and ER homeostasis. VDAC2 adds a mitochondrial outer-membrane and apoptosis-related component. The module contains no GO/KEGG term with global significance; therefore, no GO/KEGG pathway is claimed as statistically enriched. STRING provides supplementary support for an organelle-membrane context through (STRING COMPARTMENTS Organelle membrane; within-query FDR = 0.0329), but this evidence is not global enrichment evidence.

**Cell composition.** The module is not dominated by secreted or plasma proteins and does not show a blood-cell-enriched profile. All module genes have low tissue specificity, and HPA detects all of them in both placenta and rectum. The genes are predominantly intracellular, with locations involving endosomes, lysosomes, the ER, cytosol, and mitochondria; HSPA5 is annotated as intracellular and membrane-associated rather than as a conventional secreted protein. The low immune-cell specificity argues against a straightforward blood-contamination explanation. Cell-type associations include trophoblast, plasma-cell, epithelial, neutrophil, and germ-cell annotations, but no single cell type accounts for the whole module. Thus, shared ubiquitous cellular machinery is a more conservative interpretation than a tissue-specific or blood-derived program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The module contains a strong known STRING relationship between CANX and HSPA5 and an additional STRING relationship between HSPA5 and VDAC2. These links support an established connection between ER chaperone biology and a mitochondrial outer-membrane component. VPS35, CANX, and CLTC are also co-abundant neighbors within the module, indicating a broader module-level association between retromer-related trafficking, clathrin-mediated transport, and ER quality control, although the fact sheet does not provide high-confidence STRING support for every such pair. STRING supplementary enrichment identifies organelle membrane under (STRING COMPARTMENTS Organelle membrane; within-query FDR = 0.0329). No hu.MAP complex contains multiple module members, so the module is not explained by a single known hu.MAP complex.

**STRING interactions (score >= 0.7)**: 2 of 10 gene pairs: CANX–HSPA5 (0.998); HSPA5–VDAC2 (0.73)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Organelle membrane (FDR = 0.0329, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The individual proteins and at least some pairwise relationships are established biology, especially the CANX–HSPA5 and HSPA5–VDAC2 STRING relationships. The absence of a matching hu.MAP complex and the limited STRING connectivity across the full module make the exact co-abundance configuration potentially novel, but they do not establish novelty by themselves. A defensible conclusion is that this is a potentially new cross-organelle co-abundance module assembled from largely known cellular components, requiring comparison with published tissue co-abundance studies and independent datasets before being called a new biological mechanism.

**Hypothesis.** Hypothesis: in placenta and rectum, coordinated demand for membrane-protein synthesis, folding, sorting, and turnover couples ER quality control through CANX and HSPA5 to clathrin and retromer trafficking through CLTC and VPS35, while VDAC2 reflects linked mitochondrial membrane or stress-handling requirements. This could represent a shared homeostatic response in cells with active membrane remodeling or secretory and trafficking demands. The co-abundance data support coordinated activity, but they do not by themselves establish physical binding, directionality, or causal regulation.

### Important genes

#### VPS35

- **Related proteins** (co-abundance neighbors): VDAC2 (0.85), CLTC (0.84), CANX (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in placenta, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS35 retromer complex component. This gene belongs to a group of vacuolar protein sorting (VPS) genes. The encoded protein is a component of a large multimeric complex, termed the retromer complex, involved in retrograde transport of proteins from endosomes to the trans-Golgi network. The close structural similarity between the yeast and human proteins that make up this complex suggests a similarity in function. Expression studie…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.743); neurodegenerative disease (0.553); young-onset Parkinson disease (0.503); Parkinson disease (0.482); Parkinson disease, dominant (0.370)
- **Europe PMC papers**: 3611
- **Why important**: VPS35 is among the most connected genes in the module and links the trafficking arm to VDAC2, CLTC, and CANX in the co-abundance graph. Its established retromer function in retrograde transport, lysosome organization, and protein transport provides a mechanistic anchor for the module. It has a substantial literature and strong disease associations with Parkinson disease and broader neurodegenerative disease.
- **Conclusion**: Established evidence supports VPS35 as a central retromer and intracellular-sorting component. Its role as an organizer of this placenta–rectum module is a hypothesis based on network position and co-abundance, not a demonstrated causal function.

#### CANX

- **Related proteins** (co-abundance neighbors): HSPA5 (0.82), VPS35 (0.81), CLTC (0.80); STRING partners: HSPA5 (0.998)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in placenta, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is highly connected within the module and links HSPA5 with VPS35 and CLTC. As an ER calnexin chaperone, it supports folding and quality control of newly synthesized glycoproteins and is relevant to ER-associated degradation and protein secretion. It has a substantial literature and disease associations involving neurodegenerative and viral diseases.
- **Conclusion**: Established evidence supports CANX as an ER protein-folding and quality-control component. Its connection to endosomal trafficking in this module is supported by the co-abundance structure, whereas a coordinated trafficking–folding mechanism remains a hypothesis.

#### HSPA5

- **Related proteins** (co-abundance neighbors): CANX (0.82); STRING partners: CANX (0.998), VDAC2 (0.73)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in placenta, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is the strongest STRING-supported bridge in the module, connecting CANX and VDAC2, and it has the largest literature volume among the listed genes. It is an ER HSP seventy-family chaperone and a master regulator of ER homeostasis, with roles in the unfolded-protein response and membrane targeting. HPA associates it with trophoblast and plasma-cell populations as well as other cell types, while its tissue specificity remains low.
- **Conclusion**: Established evidence supports HSPA5 as a major ER proteostasis and stress-response component and supports its relationships with CANX and VDAC2 through STRING. Its proposed role as the functional bridge between ER and mitochondrial features is a biologically plausible hypothesis rather than a demonstrated causal relationship.

#### CLTC

- **Related proteins** (co-abundance neighbors): VPS35 (0.84), CANX (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in placenta, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: clathrin heavy chain. Clathrin is a major protein component of the cytoplasmic face of intracellular organelles, called coated vesicles and coated pits. These specialized organelles are involved in the intracellular trafficking of receptors and endocytosis of a variety of macromolecules.  The basic subunit of the clathrin coat is composed of three heavy chains and three light chains. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: intellectual disability, autosomal dominant 56 (0.787); cancer (0.576); hereditary disease (0.540); Alzheimer disease (0.466); neurodegenerative disease (0.465)
- **Europe PMC papers**: 2902
- **Why important**: CLTC contributes the coated-vesicle and receptor-mediated endocytosis arm of the module and is connected to VPS35 and CANX in the co-abundance graph. Its established role in intracellular trafficking and endocytosis complements the retromer and ER-quality-control functions. It has a substantial literature and disease associations including intellectual disability, cancer, Alzheimer disease, and neurodegenerative disease.
- **Conclusion**: Established evidence supports CLTC as an intracellular transport and endocytosis component. Its placement in this module supports a shared trafficking interpretation, but does not show that CLTC directly regulates the ER or mitochondrial genes.

#### VDAC2

- **Related proteins** (co-abundance neighbors): VPS35 (0.85); STRING partners: HSPA5 (0.73)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in placenta, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: voltage dependent anion channel 2. This gene encodes a member of the voltage-dependent anion channel pore-forming family of proteins that are considered the main pathway for metabolite diffusion across the mitochondrial outer membrane. The encoded protein is also thought to be involved in the mitochondrial apoptotic pathway via regulation of BCL2-antagonist/killer 1 protein activity. Pseudogenes have been identified on chromosomes …
- **Diseases (Open Targets)**: neurodegenerative disease (0.345); alcohol drinking (0.204); atrial fibrillation (0.175); major depressive disorder (0.143); severe combined immunodeficiency (0.118)
- **Europe PMC papers**: 2914
- **Why important**: VDAC2 supplies the module’s mitochondrial outer-membrane component and is connected to VPS35 in the co-abundance graph and to HSPA5 in STRING. Its established functions include metabolite transport across the mitochondrial outer membrane and participation in mitochondrial apoptotic regulation. Its disease associations include neurodegenerative and cardiovascular-related conditions, although the listed associations are less compelling than those for the central trafficking and ER genes.
- **Conclusion**: Established evidence supports VDAC2 as a mitochondrial membrane and apoptosis-related protein. Its inclusion suggests coupling between organelle trafficking or ER stress and mitochondrial state, but that cross-organelle coupling is a hypothesis inferred from the module rather than a proven mechanism.

## Module 3

**Tissue pair**: placenta and rectum  
**Genes (5)**: COL1A1, COL1A2, COL3A1, FN1, VIM

### Function

This is a conserved extracellular-matrix and connective-tissue module centered on fibrillar collagen assembly, matrix organization, and cell–matrix adhesion. The primary evidence is the global enrichment of the AGE–RAGE signaling pathway in diabetic complications (KEGG AGE-RAGE signaling pathway in diabetic complications - Homo sapiens (human); q_global = 0.00265), the fibrillar collagen trimer (GO:CC fibrillar collagen trimer; q_global = 0.0384), the fibrillar collagen complex (GO:CC fibrillar collagen complex; q_global = 0.0384), and the amoebiasis pathway (KEGG Amoebiasis - Homo sapiens (human); q_global = 0.0416). The collagen terms directly support a structural extracellular-matrix function. The AGE–RAGE and amoebiasis annotations should be interpreted mainly as pathway annotations capturing collagen and fibronectin biology, not as evidence that the tissues are infected or diabetic. Fibronectin and vimentin additionally connect matrix organization with cell attachment, migration, and cytoskeletal integrity. The sparse co-abundance network is therefore biologically coherent despite not containing every possible extracellular-matrix component.

**Cell composition.** The module is strongly stromal and extracellular-matrix associated rather than blood-cell associated. HPA classifies every gene as tissue enhanced and cell-type enhanced, with fibroblasts and hepatic stellate cells repeatedly represented; decidual and endometrial stromal cells are also prominent. Four genes are secreted or directed to the extracellular matrix, while VIM is an intracellular intermediate-filament component. Four genes are not detected in immune cells and VIM has low immune-cell specificity, with no enriched blood-cell category reported. Protein detection is present for most genes in both placenta and rectum. This pattern supports a shared fibroblast-like or stromal cell component in the two tissues, although it does not exclude contributions from other matrix-producing cells.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG AGE-RAGE signaling pathway in diabetic complications - Homo sapiens (human) | 0.00265 | COL1A1, COL1A2, COL3A1, FN1 |
| GO:CC fibrillar collagen trimer | 0.0384 | COL1A1, COL1A2, COL3A1 |
| GO:CC fibrillar collagen complex | 0.0384 | COL1A1, COL1A2, COL3A1 |
| KEGG Amoebiasis - Homo sapiens (human) | 0.0416 | COL1A1, COL1A2, COL3A1, FN1 |

### STRING and hu.MAP

STRING supports a dense, largely established interaction framework: the collagen genes are very strongly connected to one another, FN1 connects to the collagen genes, and VIM connects to FN1 and COL1A1. The STRING tissue and literature associations repeatedly identify fibroblasts, parenchymal or stromal contexts, bone, and vascular or endothelial settings (14 supplementary STRING terms; within-query FDR 0.0015–0.0016). These are supplementary convergent observations and do not replace the globally corrected GO/KEGG evidence. hu.MAP independently places COL1A1, COL1A2, and COL3A1 together in several complexes (hu.MAP huMAP3_09231.1) (hu.MAP huMAP3_09523.1) (hu.MAP huMAP3_09606.1) (hu.MAP huMAP3_10652.1) (hu.MAP huMAP3_14070.1), while additional complexes contain COL1A1 and COL1A2 (hu.MAP huMAP3_02141.1) (hu.MAP huMAP3_06460.1) (hu.MAP huMAP3_07562.1) (hu.MAP huMAP3_02069.1) (hu.MAP huMAP3_10780.1). The repeated collagen membership indicates that the collagen core reflects known molecular organization, whereas FN1 and VIM are connected mainly through known functional or physical associations rather than the listed hu.MAP complexes.

**STRING interactions (score >= 0.7)**: 8 of 10 gene pairs: COL1A1–COL1A2 (0.999); COL1A1–COL3A1 (0.999); COL1A1–FN1 (0.974); COL1A1–VIM (0.778); COL1A2–COL3A1 (0.999); COL1A2–FN1 (0.982); COL3A1–FN1 (0.928); FN1–VIM (0.809)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG AGE-RAGE signaling pathway in diabetic complications (FDR = 0.0011, 4 genes); TISSUES Bone (FDR = 0.0015, 5 genes); TISSUES Ear (FDR = 0.0015, 4 genes); TISSUES Parenchyma (FDR = 0.0015, 4 genes); TISSUES Fibroblast (FDR = 0.0016, 5 genes); PMID (2025) Spatial transcriptomics reveals prognostically LYZ(+) fibroblasts and colocalization with FN1(+) macrophages in diffuse large B-cell lymphoma. (FDR = 0.0016, 4 genes); PMID (2024) Single cell omic profiles of human aortic endothelial cells in vitro and human atherosclerotic lesions ex vivo reveals heterogeneity of endothelial subtype and response to activating perturbations. (FDR = 0.0016, 4 genes); PMID (2024) Pan-Cancer Single-Nucleus Total RNA Sequencing Using snHH-Seq. (FDR = 0.0016, 4 genes); PMID (2024) CYTOR Facilitates Formation of FOSL1 Phase Separation and Super Enhancers to Drive Metastasis of Tumor Budding Cells in Head and Neck Squamous Cell Carcinoma. (FDR = 0.0016, 4 genes); PMID (2024) Feeder-free generation and characterization of endocardial and cardiac valve cells from human pluripotent stem cells. (FDR = 0.0016, 4 genes); PMID (2024) The disruptor of telomeric silencing 1-like (DOT1L) promotes peritoneal fibrosis through the upregulation and activation of protein tyrosine kinases. (FDR = 0.0016, 4 genes); PMID (2024) Experimental and phylogenetic evidence for correlated gene expression evolution in endometrial and skin fibroblasts. (FDR = 0.0016, 4 genes); PMID (2024) Directional Endothelial Communication by Polarized Extracellular Vesicle Release. (FDR = 0.0016, 5 genes); PMID (2024) Single-cell profiling of the microenvironment in human bone metastatic renal cell carcinoma. (FDR = 0.0016, 5 genes); PMID (2024) Unsupervised spatially embedded deep representation of spatial transcriptomics. (FDR = 0.0016, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09231.1 (COL1A1, COL3A1, COL1A2; 3/6); huMAP3_09523.1 (COL1A1, COL3A1, COL1A2; 3/6); huMAP3_09606.1 (COL1A1, COL3A1, COL1A2; 3/6); huMAP3_10652.1 (COL1A1, COL3A1, COL1A2; 3/6); huMAP3_14070.1 (COL1A1, COL3A1, COL1A2; 3/8); huMAP3_02141.1 (COL1A1, COL1A2; 2/3); huMAP3_06460.1 (COL1A1, COL1A2; 2/3); huMAP3_07562.1 (COL1A1, COL1A2; 2/3); huMAP3_02069.1 (COL1A1, COL1A2; 2/4); huMAP3_10780.1 (COL1A1, COL1A2; 2/5)

### Novelty

The module should not be claimed as a wholly new molecular interaction system. Its central collagen relationships, FN1 connections, fibroblast associations, and collagen-complex memberships are already supported by STRING, hu.MAP, and prior gene biology. What may be novel is the observation that this particular co-abundance pattern is conserved across placenta and rectum, especially the coordinated behavior of the collagen core with FN1 and VIM. The fact sheet does not provide a comparison against previously reported cross-tissue modules, so genuine discovery novelty cannot be established. Absence of a gene from hu.MAP or absence of a particular edge from STRING would not by itself demonstrate novelty.

**Hypothesis.** Hypothesis: a shared fibroblast-like or stromal cell population in placenta and rectum produces a coordinated extracellular scaffold in which COL1A1 and COL1A2 form the principal type I collagen structure, COL3A1 contributes extensible fibrillar matrix, FN1 organizes cell–matrix adhesion and migration, and VIM couples the matrix-associated cellular state to the cytoskeleton. This shared stromal program could explain the conserved co-abundance pattern and may be responsive to tissue remodeling or repair. The hypothesis requires validation with cell-resolved localization, protein co-occurrence, and perturbation of matrix or adhesion pathways; the co-abundance data alone do not establish causality.

### Important genes

#### COL1A1

- **Related proteins** (co-abundance neighbors): COL1A2 (0.83), FN1 (0.82); STRING partners: COL1A2 (0.999), COL3A1 (0.999), FN1 (0.974), VIM (0.778)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in placenta, rectum
- **hu.MAP 3.0**: huMAP3_09231.1, huMAP3_09523.1, huMAP3_09606.1, huMAP3_10652.1, huMAP3_14070.1, huMAP3_02141.1, huMAP3_06460.1, huMAP3_07562.1, huMAP3_02069.1, huMAP3_10780.1
- **Function (MyGene.info)**: collagen type I alpha 1 chain. This gene encodes the pro-alpha1 chains of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIA, Ehlers-Danlos syndrome Classical type,…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 2 (0.847); osteogenesis imperfecta type 4 (0.837); osteogenesis imperfecta type 3 (0.835); osteogenesis imperfecta type 1 (0.834); osteogenesis imperfecta (0.808)
- **Europe PMC papers**: 45548
- **Why important**: COL1A1 is a central member of the collagen core, connects strongly with COL1A2, COL3A1, and FN1 in STRING, and occurs in every listed hu.MAP complex. It is present in all globally enriched terms (4 globally significant GO/KEGG terms, q_global 0.00265–0.0416; see the table). Its HPA profile points to fibroblast and stromal biology, and its established role is to encode a principal pro-alpha chain of type I collagen. Its disease associations include multiple forms of osteogenesis imperfecta and Ehlers–Danlos disease, and it has an extensive literature base.
- **Conclusion**: Established evidence supports COL1A1 as a principal structural component and an anchor of the module's fibrillar collagen program. Hypothesis: variation in COL1A1 abundance may be especially influential in determining the stiffness, organization, or remodeling state of the shared stromal matrix.

#### COL1A2

- **Related proteins** (co-abundance neighbors): COL1A1 (0.83), COL3A1 (0.80); STRING partners: COL1A1 (0.999), COL3A1 (0.999), FN1 (0.982)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in placenta, rectum
- **hu.MAP 3.0**: huMAP3_09231.1, huMAP3_09523.1, huMAP3_09606.1, huMAP3_10652.1, huMAP3_14070.1, huMAP3_02141.1, huMAP3_06460.1, huMAP3_07562.1, huMAP3_02069.1, huMAP3_10780.1
- **Function (MyGene.info)**: collagen type I alpha 2 chain. This gene encodes the pro-alpha2 chain of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIB, recessive Ehlers-Danlos syndrome Classi…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 2 (0.845); osteogenesis imperfecta type 3 (0.830); osteogenesis imperfecta type 4 (0.820); Ehlers-Danlos syndrome, cardiac valvular type (0.777); osteogenesis imperfecta type 1 (0.770)
- **Europe PMC papers**: 67901
- **Why important**: COL1A2 is the partner chain required for the type I collagen triple helix and is tightly connected to COL1A1 and COL3A1. It occurs in every listed hu.MAP complex and in every globally enriched term (4 globally significant GO/KEGG terms, q_global 0.00265–0.0416; see the table). HPA supports fibroblast, decidual stromal, endometrial stromal, and smooth-muscle-associated expression. Its annotations include collagen fibril organization and transforming growth factor beta receptor signaling, while disease associations include osteogenesis imperfecta, Ehlers–Danlos disease, and atypical Marfan syndrome. It also has an extensive literature base.
- **Conclusion**: Established evidence identifies COL1A2 as an essential structural partner of COL1A1 and a core marker of the module. Hypothesis: coordinated COL1A1–COL1A2 regulation is a primary determinant of the module's abundance and may reflect common stromal matrix production in both tissues.

#### COL3A1

- **Related proteins** (co-abundance neighbors): COL1A2 (0.80); STRING partners: COL1A1 (0.999), COL1A2 (0.999), FN1 (0.928)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09231.1, huMAP3_09523.1, huMAP3_09606.1, huMAP3_10652.1, huMAP3_14070.1
- **Function (MyGene.info)**: collagen type III alpha 1 chain. This gene encodes the pro-alpha1 chains of type III collagen, a fibrillar collagen that is found in extensible connective tissues such as skin, lung, uterus, intestine and the vascular system, frequently in association with type I collagen. Mutations in this gene are associated with Ehlers-Danlos syndrome type IV, and with aortic and arterial aneurysms. [provided by R. Dalgleish, Feb 2008].
- **Diseases (Open Targets)**: Ehlers-Danlos syndrome, vascular type (0.861); polymicrogyria with or without vascular-type Ehlers-Danlos syndrome (0.793); autosomal dominant Ehlers-Danlos syndrome, vascular type (0.705); familial thoracic aortic aneurysm and aortic dissection (0.596); Ehlers-Danlos syndrome (0.587)
- **Europe PMC papers**: 18289
- **Why important**: COL3A1 is linked to both type I collagen genes in STRING and is included with them in the higher-confidence hu.MAP collagen complexes (hu.MAP huMAP3_09231.1) (hu.MAP huMAP3_09523.1) (hu.MAP huMAP3_09606.1) (hu.MAP huMAP3_10652.1) (hu.MAP huMAP3_14070.1). It appears in all globally enriched terms (4 globally significant GO/KEGG terms, q_global 0.00265–0.0416; see the table). HPA associates it with fibroblasts, stromal cells, smooth muscle, and placenta. Its established function is production of type III collagen, which occurs in extensible tissues and frequently accompanies type I collagen, including intestine, uterus, and vascular tissue. Its disease associations include vascular Ehlers–Danlos disease and arterial aneurysm disorders.
- **Conclusion**: Established evidence supports COL3A1 as the extensible-matrix counterpart to the type I collagen core. Hypothesis: its coordinated abundance may tune matrix compliance and tissue integrity in the shared placenta–rectum stromal program.

#### FN1

- **Related proteins** (co-abundance neighbors): VIM (0.83), COL1A1 (0.82); STRING partners: COL1A1 (0.974), COL1A2 (0.982), COL3A1 (0.928), VIM (0.809)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in placenta, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 is a major network bridge between the collagen core and VIM, with STRING links to every other module gene. It appears in the globally enriched AGE–RAGE and amoebiasis terms (KEGG AGE-RAGE signaling pathway in diabetic complications - Homo sapiens (human); q_global = 0.00265) and (KEGG Amoebiasis - Homo sapiens (human); q_global = 0.0416), and in many supplementary fibroblast, tissue, vascular, and literature associations (15 supplementary STRING terms; within-query FDR 0.0011–0.0016). HPA identifies it in fibroblasts and extravillous trophoblasts, detects it in both tissues, and classifies it as secreted to blood. Its established functions include cell adhesion, cell–matrix adhesion, migration, wound healing, coagulation, and extracellular-matrix organization. Its disease associations include fibronectin-deposit glomerulopathy and cancer-related disorders, with a very extensive literature base.
- **Conclusion**: Established evidence supports FN1 as the principal interface between extracellular collagen and cellular adhesion or migration. Hypothesis: FN1 may coordinate assembly of the collagen scaffold with the migratory or remodeling state of stromal cells.

#### VIM

- **Related proteins** (co-abundance neighbors): FN1 (0.83); STRING partners: COL1A1 (0.778), FN1 (0.809)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments; IHC detected in placenta, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vimentin. This gene encodes a type III intermediate filament protein. Intermediate filaments, along with microtubules and actin microfilaments, make up the cytoskeleton. The encoded protein is responsible for maintaining cell shape and integrity of the cytoplasm, and stabilizing cytoskeletal interactions. This protein is involved in neuritogenesis and cholesterol transport and functions as an organizer of a…
- **Diseases (Open Targets)**: dengue disease (0.516); early-onset non-syndromic cataract (0.462); early-onset partial cataract (0.458); Developmental cataract (0.435); cataract (0.372)
- **Europe PMC papers**: 86568
- **Why important**: VIM is the module's cytoskeletal component and connects to FN1 and COL1A1 in STRING. It is not part of a globally enriched GO/KEGG term, so its importance comes from network bridging and cellular interpretation rather than primary enrichment. HPA places it in fibroblasts, hepatic stellate cells, decidual stromal cells, and vascular tissue, with low immune-cell specificity and detection in both tissues. Its established function is an intermediate-filament scaffold that supports cell shape, integrity, attachment, migration, and signaling. It has a very extensive literature base and disease associations including cataract-related disorders and dengue disease.
- **Conclusion**: Established evidence supports VIM as the intracellular component linking the matrix-associated state to cytoskeletal organization. Hypothesis: VIM may help transmit extracellular-matrix or adhesion changes into altered stromal-cell morphology and migration, but the module data do not establish directionality.

## Module 4

**Tissue pair**: placenta and rectum  
**Genes (5)**: LAMA5, LAMB1, LAMC1, NID2, HSPG2

### Function

The module is a basement-membrane and laminin-network module. The strongest primary evidence is (GO:CC basement membrane; q_global = 0.00446), where all module genes map to basement membrane, together with (GO:CC laminin trimer; q_global = 0.013) through (GO:CC laminin network; q_global = 0.013), which specifically identify a laminin trimer, laminin-511 trimer, non-collagenous basement-membrane components, and a laminin network. The module therefore most plausibly represents coordinated production, assembly, and maintenance of laminin-rich extracellular matrix. Laminins are relevant to cell adhesion, cell migration, tissue development, differentiation, and signaling, as supported by the gene annotations. The STRING annotations (STRING NetworkNeighborAL laminin-1 complex, and G2 nidogen domain and fibulin; within-query FDR = 1.33e-05) through (STRING PMID (2017) Quantitative proteomic profiling of the extracellular matrix of pancreatic islets during the angiogenic switch and insulinoma progression.; within-query FDR = 0.0081) are concordant supplementary evidence, but the global functional conclusion rests on the globally significant GO/KEGG terms. No KEGG term is reported as globally significant.

**Cell composition.** This is a strongly extracellular-matrix-composed module: every gene is annotated by HPA as secreted to the extracellular matrix. The genes are tissue or cell-type enriched rather than broadly housekeeping-like. Placenta enrichment is prominent, with additional associations involving ovary and blood vessel, and the single-cell annotations repeatedly implicate fibro-adipogenic progenitors, fibroblasts, trophoblast-related cells, adipocytes, and related stromal or epithelial populations. All module genes are reported as not detected in immune cells, so the shared signal is not suggestive of a blood-cell or immune-cell module. Detection in both placenta and rectum supports a genuine shared extracellular-matrix signal, although the signal could reflect shared stromal, vascular, or epithelial cell populations rather than identical biology in the two tissues. LAMA5 has low tissue specificity and is detected in rectum but not placenta, so its participation may be less placenta-restricted than that of the other genes.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC basement membrane | 0.00446 | HSPG2, LAMA5, LAMB1, LAMC1, NID2 |
| GO:CC laminin trimer | 0.013 | LAMA5, LAMB1, LAMC1 |
| GO:CC laminin-511 trimer | 0.013 | LAMA5, LAMB1, LAMC1 |
| GO:CC non-collagenous component of basement membrane | 0.013 | LAMA5, LAMB1, LAMC1 |
| GO:CC laminin network | 0.013 | LAMA5, LAMB1, LAMC1 |

### STRING and hu.MAP

The network is densely connected: nearly every possible gene pair has a high-confidence STRING relationship. LAMA5, LAMB1, and LAMC1 form the core laminin-chain relationships, while NID2 and HSPG2 connect the laminin components to basement-membrane organization. The strongest relationships are consistent with known physical or functional extracellular-matrix associations rather than unexplained co-expression alone. STRING enrichment for basement membrane, laminin interactions, laminin domains, and the laminin complex (STRING NetworkNeighborAL laminin-1 complex, and G2 nidogen domain and fibulin; within-query FDR = 1.33e-05) through (STRING PMID (2017) Quantitative proteomic profiling of the extracellular matrix of pancreatic islets during the angiogenic switch and insulinoma progression.; within-query FDR = 0.0081) reinforces this interpretation, but these are supplementary within-query results rather than globally corrected module-level evidence. hu.MAP independently supports known complex membership: LAMB1, LAMC1, and NID2 occur together in (hu.MAP huMAP3_14233.1), and LAMB1 with LAMC1 occur together in (hu.MAP huMAP3_01175.1) and (hu.MAP huMAP3_08112.1). HSPG2 and LAMA5 have no reported hu.MAP complex containing multiple module members, which does not exclude their extracellular association. Overall, the network is substantially explained by established laminin and basement-membrane biology.

**STRING interactions (score >= 0.7)**: 9 of 10 gene pairs: HSPG2–LAMB1 (0.782); HSPG2–LAMC1 (0.82); HSPG2–NID2 (0.999); LAMA5–LAMB1 (0.998); LAMA5–LAMC1 (0.999); LAMA5–NID2 (0.849); LAMB1–LAMC1 (0.999); LAMB1–NID2 (0.928); LAMC1–NID2 (0.984)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL laminin-1 complex, and G2 nidogen domain and fibulin (FDR = 1.33e-05, 5 genes); Keyword Basement membrane (FDR = 8.56e-05, 5 genes); RCTM Laminin interactions (FDR = 0.00019, 5 genes); SMART Laminin-type epidermal growth factor-like domai (FDR = 0.0003, 4 genes); InterPro EGF-like domain (FDR = 0.00036, 5 genes); COMPARTMENTS Basement membrane (FDR = 0.00049, 5 genes); InterPro Laminin-type EGF domain (FDR = 0.00057, 4 genes); Keyword Laminin EGF-like domain (FDR = 0.00058, 4 genes); Component Basement membrane (FDR = 0.0013, 5 genes); SMART Laminin N-terminal domain (domain VI) (FDR = 0.0026, 3 genes); SMART Laminin B domain (FDR = 0.0026, 3 genes); SMART EGF domain, unclasssified subfamily (FDR = 0.0053, 3 genes); InterPro Laminin IV (FDR = 0.0067, 3 genes); InterPro Laminin, N-terminal (FDR = 0.0067, 3 genes); PMID (2017) Quantitative proteomic profiling of the extracellular matrix of pancreatic islets during the angiogenic switch and insulinoma progression. (FDR = 0.0081, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14233.1 (LAMB1, LAMC1, NID2; 3/14); huMAP3_01175.1 (LAMB1, LAMC1; 2/2); huMAP3_08112.1 (LAMB1, LAMC1; 2/5)

### Novelty

The gene functions and many of the relationships are established rather than newly discovered: laminin chains, nidogen, and perlecan are known basement-membrane components, STRING contains dense relationships among them, and hu.MAP contains laminin-containing complexes (hu.MAP huMAP3_14233.1) through (hu.MAP huMAP3_08112.1). Therefore this should not be presented as a novel molecular complex or a newly discovered interaction. The potentially new aspect is the reproducible conservation of this coordinated abundance pattern across placenta and rectum, especially if that tissue-pair conservation was not previously reported. The fact sheet alone does not establish novelty at the module or biological-discovery level; it lacks an external replication set, comparison with published tissue co-abundance modules, and an experimental test. Absence from a database would not by itself prove novelty.

**Hypothesis.** Hypothesis: a shared stromal or vascular extracellular-matrix program in placenta and rectum coordinates LAMA5, LAMB1, and LAMC1 to assemble laminin-rich basement membrane, while NID2 stabilizes the laminin network and HSPG2 cross-links matrix components and cell-surface-associated signals. This matrix program could regulate adhesion, epithelial or endothelial barrier support, cell migration, and local tissue remodeling. The hypothesis is consistent with (GO:CC basement membrane; q_global = 0.00446) through (GO:CC laminin network; q_global = 0.013), the STRING relationships, hu.MAP evidence (hu.MAP huMAP3_14233.1) through (hu.MAP huMAP3_08112.1), and the HPA stromal, vascular, and extracellular-matrix annotations, but co-abundance does not demonstrate physical assembly, causal regulation, or a shared cellular source. These points should be tested by cell-resolved expression or proteomics, spatial localization, and perturbation of laminin or nidogen-perlecan interactions.

### Important genes

#### LAMB1

- **Related proteins** (co-abundance neighbors): LAMC1 (0.91), HSPG2 (0.86), LAMA5 (0.81); STRING partners: HSPG2 (0.782), LAMA5 (0.998), LAMC1 (0.999), NID2 (0.928)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in placenta, rectum
- **hu.MAP 3.0**: huMAP3_14233.1, huMAP3_01175.1, huMAP3_08112.1
- **Function (MyGene.info)**: laminin subunit beta 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins are composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respecti…
- **Diseases (Open Targets)**: cobblestone lissencephaly without muscular or ocular involvement (0.800); Fuchs' endothelial dystrophy (0.494); eye disorder (0.434); corneal disorder (0.424); corneal dystrophy (0.423)
- **Europe PMC papers**: 3735
- **Why important**: LAMB1 is a central network connector and participates in every primary enrichment term (GO:CC basement membrane; q_global = 0.00446) through (GO:CC laminin network; q_global = 0.013). It encodes a laminin beta subunit and is supported by dense STRING relationships with all other module genes and by all reported hu.MAP complexes (hu.MAP huMAP3_14233.1) through (hu.MAP huMAP3_08112.1). HPA supports placenta enrichment, extracellular-matrix secretion, and detection in both tissues. Its substantial literature and disease associations provide stronger external support than would co-abundance alone.
- **Conclusion**: Established evidence supports LAMB1 as a core structural laminin component and a key integrator of the module. It is a plausible organizing gene, but the fact sheet does not establish that LAMB1 causes the shared placenta-rectum abundance pattern.

#### LAMC1

- **Related proteins** (co-abundance neighbors): LAMB1 (0.91), NID2 (0.85); STRING partners: HSPG2 (0.82), LAMA5 (0.999), LAMB1 (0.999), NID2 (0.984)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Plasma membrane; IHC detected in placenta, rectum
- **hu.MAP 3.0**: huMAP3_14233.1, huMAP3_01175.1, huMAP3_08112.1
- **Function (MyGene.info)**: laminin subunit gamma 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: Fuchs' endothelial dystrophy (0.487); prostate carcinoma (0.467); colorectal cancer (0.447); eye disorder (0.434); benign colon neoplasm (0.427)
- **Europe PMC papers**: 4227
- **Why important**: LAMC1 is the laminin gamma chain and participates in every primary term (GO:CC basement membrane; q_global = 0.00446) through (GO:CC laminin network; q_global = 0.013). It has strong relationships with the other laminin chains and NID2, appears in all reported hu.MAP complexes (hu.MAP huMAP3_14233.1) through (hu.MAP huMAP3_08112.1), and occupies a connective position between the laminin core and nidogen. HPA supports placenta enrichment, extracellular-matrix secretion, fibroblast and adipocyte-associated cell types, and detection in both tissues. Its broad literature and disease associations make it a well-supported biological anchor.
- **Conclusion**: Established evidence identifies LAMC1 as a core basement-membrane and laminin-network component. Its network position makes it a strong candidate for maintaining the module, while a causal role in tissue-pair conservation remains a hypothesis.

#### LAMA5

- **Related proteins** (co-abundance neighbors): LAMB1 (0.81); STRING partners: LAMB1 (0.998), LAMC1 (0.999), NID2 (0.849)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit alpha 5. This gene encodes one of the vertebrate laminin alpha chains. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins are composed of 3 non identical chains: l…
- **Diseases (Open Targets)**: nephrotic syndrome, IIa 26 (0.761); bent bone dysplasia syndrome 2 (0.563); colorectal cancer (0.491); LAMA5-related multisystemic syndrome (0.475); polyp of colon (0.467)
- **Europe PMC papers**: 2881
- **Why important**: LAMA5 is the alpha chain associated with the laminin-511 trimer and appears in every primary term (GO:CC basement membrane; q_global = 0.00446) through (GO:CC laminin network; q_global = 0.013). It has very strong STRING relationships with LAMB1 and LAMC1 and annotations involving integrin-mediated signaling, adhesion, migration, and organ morphogenesis. HPA links it to multiple relevant cell types, including trophoblasts, podocytes, and alveolar cells, and detects it in rectum. Its substantial literature and colorectal disease associations increase its importance for interpreting the rectal component of the module.
- **Conclusion**: Established evidence supports LAMA5 as a defining laminin-chain component with potential signaling and adhesion consequences. Its lack of placenta protein detection in the supplied HPA result cautions against assuming equal protein contribution in both tissues.

#### HSPG2

- **Related proteins** (co-abundance neighbors): LAMB1 (0.86); STRING partners: LAMB1 (0.782), LAMC1 (0.82), NID2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in placenta, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 is the perlecan core protein and is the only module gene that appears exclusively in the globally significant basement-membrane term (GO:CC basement membrane; q_global = 0.00446). It provides a biologically distinct matrix function from the laminin chains by binding and cross-linking extracellular-matrix and cell-surface molecules. STRING links it to the laminin components and NID2, while HPA supports blood-vessel enrichment, extracellular-matrix secretion, relevant stromal and trophoblast-associated cell types, and detection in both tissues. Its substantial literature and disease associations make it important for vascular and matrix interpretation.
- **Conclusion**: Established evidence supports HSPG2 as a matrix-organizing and signaling interface within the module, not merely as a passive co-abundant protein. Its contribution to the shared tissue program is plausible but not proven to be causal.

#### NID2

- **Related proteins** (co-abundance neighbors): LAMC1 (0.85); STRING partners: HSPG2 (0.999), LAMA5 (0.849), LAMB1 (0.928), LAMC1 (0.984)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in placenta, rectum
- **hu.MAP 3.0**: huMAP3_14233.1
- **Function (MyGene.info)**: nidogen 2. This gene encodes a member of the nidogen family of basement membrane proteins. This protein is a cell-adhesion protein that binds collagens I and IV and laminin and may be involved in maintaining the structure of the basement membrane.[provided by RefSeq, Jun 2010].
- **Diseases (Open Targets)**: hearing loss disorder (0.474); benign colon neoplasm (0.439); presbycusis (0.436); sensorineural hearing loss disorder (0.436); Tinnitus (0.360)
- **Europe PMC papers**: 1495
- **Why important**: NID2 is a basement-membrane nidogen that binds laminin and collagen and participates in basement-membrane organization. It contributes to (GO:CC basement membrane; q_global = 0.00446), has strong STRING relationships with every laminin or perlecan partner, and is included with LAMB1 and LAMC1 in hu.MAP complex (hu.MAP huMAP3_14233.1). HPA supports placenta and ovary enrichment, extracellular-matrix secretion, fibro-adipogenic and related cell types, and detection in both tissues. Its literature is smaller than that of the major laminin chains but is directly relevant to matrix linkage and tissue architecture.
- **Conclusion**: Established evidence supports NID2 as a linker and stabilizer of the basement-membrane network. It is a credible mechanistic bridge between laminin assembly and matrix organization, although the module data do not prove that NID2 is the limiting or regulatory component.
