# Conserved co-abundance modules: cerebrospinal_fluid and testis

## Module 0

**Tissue pair**: cerebrospinal_fluid and testis  
**Genes (9)**: SLC3A2, SERPINF2, APOA1, ASPH, C6, ITIH4, HSPG2, SOD2, AZGP1

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established pathway assignment from enrichment. Its gene content instead points to a circulating extracellular protein context involving complement, coagulation and fibrinolysis, lipid transport, extracellular-matrix organization, protease regulation, and cellular stress or calcium-related biology. ITIH4 is the central network connector, linking the secreted plasma-associated genes with ASPH, SOD2, AZGP1, and the complement component C6. The pattern is therefore more consistent with a mixed extracellular and tissue-interface signature than with a single intracellular pathway. The co-abundance relationships should not be interpreted as direct molecular interactions.

**Cell composition.** The module is dominated by secreted or extracellular proteins and by genes with liver-associated expression, including ITIH4, C6, SERPINF2, AZGP1, and APOA1. APOA1 is a major plasma HDL protein; ITIH4, C6, SERPINF2, and AZGP1 are also secreted to blood. HSPG2 is an extracellular-matrix proteoglycan. HPA evidence additionally links parts of the module to hepatocytes, adipocytes, blood vessels, bone marrow, neutrophils, and plasmacytoid dendritic cells. This composition makes a circulating plasma contribution, blood or vascular carryover, or a shared barrier-associated cell source plausible in both cerebrospinal fluid and testis. It is not a uniformly blood-cell-enriched module: several genes are not detected in immune cells, while selected genes show immune-cell enhancement or enrichment. HPA reports no matching cerebrospinal-fluid protein data, whereas testis protein detection is mixed. The shared signal should therefore be interpreted cautiously rather than assumed to represent a specialized cerebrospinal-fluid–testis program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no STRING functional-enrichment result. Thus, STRING does not provide evidence for a pre-existing direct interaction network. hu.MAP provides partial complex-context evidence: SERPINF2 and C6 co-occur in the complement-associated complexes (hu.MAP huMAP3_14445.1) and (hu.MAP huMAP3_14656.1), while APOA1 and ITIH4 co-occur in the broad plasma, complement, and extracellular-protein complexes (hu.MAP huMAP3_09434.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_15040.1), and (hu.MAP huMAP3_10678.1). These complexes contain many proteins not present in the module, so they support shared biochemical context rather than a compact module-specific complex. The network is consequently stronger as a co-abundance pattern than as a map of established physical interactions.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14445.1 (SERPINF2, C6; 2/18); huMAP3_14656.1 (SERPINF2, C6; 2/21); huMAP3_09434.1 (APOA1, ITIH4; 2/33); huMAP3_09531.1 (APOA1, ITIH4; 2/47); huMAP3_10101.1 (APOA1, ITIH4; 2/49); huMAP3_15040.1 (APOA1, ITIH4; 2/64); huMAP3_10678.1 (APOA1, ITIH4; 2/71)

### Novelty

The module may represent a dataset-specific co-abundance signature, but the evidence is insufficient to call it a new biological mechanism. Its lack of STRING interactions and its partial, broad hu.MAP memberships do not by themselves establish novelty. The genes have established roles in plasma transport, complement, fibrinolysis, extracellular matrix, oxidative defense, calcium biology, and membrane transport, and the absence of globally significant GO/KEGG enrichment argues against a newly defined coherent pathway. A potentially novel aspect is the reproducible sharing of this mixed secreted and tissue-associated signature between cerebrospinal fluid and testis, but that claim requires validation in independent cohorts, control for blood contamination and cell composition, and comparison with previously reported co-abundance modules.

**Hypothesis.** Hypothesis: the module reflects coordinated variation in proteins exchanged through the circulation or produced at vascular and barrier interfaces, rather than a single intracellular pathway. In this model, liver-derived APOA1, ITIH4, C6, SERPINF2, and AZGP1 form the circulating inflammatory, lipid, complement, and protease-regulatory background; HSPG2 may provide extracellular-matrix or barrier context; and ASPH, SLC3A2, and SOD2 may represent local tissue responses involving calcium handling, amino-acid transport, and oxidative stress. Shared exposure of cerebrospinal fluid and testis to vascular, barrier, or blood-derived influences could generate the observed co-abundance pattern. This remains a hypothesis because the network has no supporting STRING interactions, no globally significant enrichment, and no direct evidence that the proteins act together in either tissue.

### Important genes

#### ITIH4

- **Related proteins** (co-abundance neighbors): SOD2 (0.94), ASPH (0.93), AZGP1 (0.88), C6 (0.85), SERPINF2 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09434.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 4. The protein encoded by this gene is secreted into the blood, where it is cleaved by plasma kallikrein into two smaller forms. Expression of this gene has been detected only in liver, and it seems to be upregulated during surgical trauma. This gene is part of a cluster of similar genes on chromosome 3. Two transcript variants encoding different isoforms have been found for this gene. [provided by R…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.466); coronary artery disorder (0.417); type 2 diabetes mellitus (0.397); osteoarthritis (0.387); diabetes mellitus (0.363)
- **Europe PMC papers**: 1710
- **Why important**: ITIH4 is the principal network hub and connects the module's secreted plasma-associated proteins with ASPH, SOD2, AZGP1, and C6. It is secreted to blood, enriched in liver, and has HPA single-cell enhancement in several brain-associated cell types. Its established functions include acute-phase response, hyaluronan metabolism, and cytokine response, while its hu.MAP context includes complement components. It therefore provides the strongest bridge between a circulating extracellular signature and a possible neural or barrier-associated context.
- **Conclusion**: Established evidence supports ITIH4 as the network organizer and a liver-derived extracellular or acute-phase protein. It is reasonable to hypothesize that ITIH4 helps couple circulating protein variation to tissue-interface biology, but the co-abundance data do not establish a direct interaction or a causal role in cerebrospinal fluid–testis sharing.

#### APOA1

- **Related proteins** (co-abundance neighbors): SLC3A2 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09434.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is a module member with a direct co-abundance link to SLC3A2 and shared hu.MAP context with ITIH4 in broad plasma and complement-related complexes. It is liver-enriched, secreted to blood, and is the major HDL protein involved in cholesterol efflux and lipid transport. Its extensive disease and literature record makes it a well-established marker of systemic lipid and plasma biology, but that same property makes it a strong candidate for reflecting circulating composition rather than tissue-specific regulation.
- **Conclusion**: Established evidence supports APOA1 as a circulating lipid-transport protein and a likely contributor to the module's plasma signature. Its presence supports a blood-derived or vascular explanation more strongly than a novel cerebrospinal-fluid–testis mechanism.

#### C6

- **Related proteins** (co-abundance neighbors): ITIH4 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14445.1, huMAP3_14656.1
- **Function (MyGene.info)**: complement C6. This gene encodes a component of the complement cascade. The encoded protein is part of the membrane attack complex that can be incorporated into the cell membrane and cause cell lysis. Mutations in this gene are associated with complement component-6 deficiency. Transcript variants encoding the same protein have been described.[provided by RefSeq, Nov 2012].
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.753); complement deficiency (0.464); hereditary disease (0.416); male reproductive organ cancer (0.257); benign neoplasm of brain (0.199)
- **Europe PMC papers**: 88422
- **Why important**: C6 is connected to ITIH4 and appears with SERPINF2 in hu.MAP complexes (hu.MAP huMAP3_14445.1) and (hu.MAP huMAP3_14656.1). It is a liver-enriched secreted complement protein and a component of the membrane attack complex. Its established disease associations with complement deficiency provide strong functional relevance, while its position links the network hub to immune effector biology.
- **Conclusion**: Established evidence supports C6 as a complement-related circulating component that reinforces the module's extracellular immune context. A role in the shared module could involve coordinated complement abundance, but the available data do not show that C6 directly drives the co-abundance pattern or tissue specificity.

#### SERPINF2

- **Related proteins** (co-abundance neighbors): ITIH4 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enriched; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14445.1, huMAP3_14656.1
- **Function (MyGene.info)**: serpin family F member 2. This gene encodes a member of the serpin family of serine protease inhibitors. The protein is a major inhibitor of plasmin, which degrades fibrin and various other proteins. Consequently, the proper function of this gene has a major role in regulating the blood clotting pathway. Mutations in this gene result in alpha-2-plasmin inhibitor deficiency, which is characterized by severe hemorrhagic diat…
- **Diseases (Open Targets)**: alpha-2-plasmin inhibitor deficiency (0.666); chronic kidney disease (0.452); Alzheimer disease (0.413); dementia (0.402); Abnormal bleeding (0.371)
- **Europe PMC papers**: 1441
- **Why important**: SERPINF2 is connected to ITIH4 and shares hu.MAP context with C6. It is secreted to blood, liver-enriched, and encodes a major inhibitor of plasmin, thereby regulating fibrinolysis and blood clotting. Its disease associations with alpha-two-plasmin inhibitor deficiency and abnormal bleeding make it an informative marker of the coagulation and protease-regulatory axis within the module.
- **Conclusion**: Established evidence supports SERPINF2 as a circulating fibrinolytic regulator that complements the module's plasma and vascular interpretation. Its relationship with C6 in hu.MAP supports shared extracellular context, but not a direct physical interaction or a specialized role in either sampled tissue.

#### ASPH

- **Related proteins** (co-abundance neighbors): AZGP1 (0.94), ITIH4 (0.93), SLC3A2 (0.83), HSPG2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aspartate beta-hydroxylase. This gene is thought to play an important role in calcium homeostasis. The gene is expressed from two promoters and undergoes extensive alternative splicing. The encoded set of proteins share varying amounts of overlap near their N-termini but have substantial variations in their C-terminal domains resulting in distinct functional properties. The longest isoforms (a and f) include a C-terminal Asp…
- **Diseases (Open Targets)**: facial dysmorphism-lens dislocation-anterior segment abnormalities-spontaneous filtering blebs syndrome (0.770); Abnormality of the skeletal system (0.505); malignant hyperthermia of anesthesia (0.427); exercise-induced malignant hyperthermia (0.416); alcohol drinking (0.374)
- **Europe PMC papers**: 1346
- **Why important**: ASPH is one of the strongest internal connectors after ITIH4, linking AZGP1, SLC3A2, and HSPG2 as well as ITIH4. Unlike the principal secreted proteins, ASPH is an endoplasmic-reticulum protein with tissue enhancement in adipose tissue and immune-cell enhancement in plasmacytoid dendritic cells; it is detected in testis. Its established annotations involve calcium detection and calcium transport, and its disease associations include syndromic developmental and muscle-related phenotypes. It may therefore represent a tissue-associated arm of the otherwise plasma-heavy module.
- **Conclusion**: Established evidence supports ASPH as a calcium-related, tissue-associated protein occupying a central bridging position in the co-abundance graph. A local testicular or barrier-related contribution is plausible, but it remains a hypothesis because ASPH has no supporting STRING or hu.MAP relationship within this module.

#### SLC3A2

- **Related proteins** (co-abundance neighbors): HSPG2 (0.87), ASPH (0.83), APOA1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 3 member 2. This gene is a member of the solute carrier family and encodes a cell surface, transmembrane protein. The protein exists as the heavy chain of a heterodimer, covalently bound through di-sulfide bonds to one of several possible light chains. The encoded transporter plays a role in regulation of intracellular calcium levels and transports L-type amino acids. Alternatively spliced transcript variants…
- **Diseases (Open Targets)**: sensorineural hearing loss disorder (0.370); neurodegenerative disease (0.324); neoplasm (0.117); breast cancer (0.113); breast carcinoma (0.110)
- **Europe PMC papers**: 6815
- **Why important**: SLC3A2 links APOA1 to ASPH and HSPG2 and is located at the plasma membrane and nucleoplasm. It forms the heavy chain of heteromeric amino-acid transporters and is annotated for amino-acid and calcium transport. HPA describes broad tissue specificity with enhancement in selected epithelial and trophoblast-related cell types, and testis protein detection is reported. Its large literature record and membrane location make it a plausible interface between extracellular proteins and cellular transport biology.
- **Conclusion**: Established evidence supports SLC3A2 as a broadly expressed transporter-associated membrane protein that could mark cellular state rather than a secreted plasma process. Its network position suggests a possible bridge between extracellular-matrix or circulating signals and tissue transport responses, but this mechanistic connection is not established by the supplied data.

## Module 1

**Tissue pair**: cerebrospinal_fluid and testis  
**Genes (13)**: ORM1, ORM2, SERPINA1, A2M, ALB, GLB1, C3, ECE1, GNS, IGHG1, IGHG2, IGKC, TF

### Function

No GO/KEGG term passed global correction, so no GO/KEGG function can be called globally enriched. The gene identities, network structure, STRING evidence and hu.MAP evidence instead support a circulating secreted-plasma protein module involving acute-phase response, complement, protease inhibition, iron transport and immunoglobulin-associated biology. STRING supplementary annotations place many members in secretory granule and secretory granule lumen categories (4 supplementary STRING terms; within-query FDR 0.0079–0.0113). hu.MAP repeatedly recovers a core consisting of SERPINA1, A2M, C3, ORM1, ALB, TF and ORM2 in plasma-protein complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1). C3 contributes complement and inflammatory activity; SERPINA1 and A2M contribute extracellular protease control; ORM1 and ORM2 are acute-phase proteins with immune-regulatory associations; ALB is a major plasma carrier; and TF transports iron. The immunoglobulin genes add an antibody or plasma-cell-associated component. These are interpretations of member functions and supplementary network evidence, not globally corrected enrichment claims.

**Cell composition.** The module is dominated by secreted or blood-associated proteins. HPA identifies frequent liver and hepatocyte enrichment, together with lymphoid, plasma-cell, monocyte and neutrophil associations. Most members are secreted to blood or are immunoglobulin genes, although GLB1 and GNS are intracellular or membrane-associated lysosomal proteins and therefore the module is not exclusively composed of plasma proteins. The shared appearance in cerebrospinal fluid and testis may therefore reflect circulating proteins, blood exposure, vascular or barrier permeability, or shared extracellular-fluid composition. It should not automatically be interpreted as a testis-specific or cerebrospinal-fluid-specific pathway. HPA detection in testis shows that several proteins are present there, but the dominant liver, blood and secretome pattern provides a parsimonious explanation for much of the shared signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a known interaction backbone among A2M, ALB, ORM1, ORM2, SERPINA1, TF and C3. ORM1 is a central module node and links to ORM2, TF, GNS, GLB1, IGHG1 and SERPINA1. TF links several core plasma proteins, while GLB1 and GNS form a separate lysosomal-enzyme pair. hu.MAP independently recovers the same plasma-protein core across multiple complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1), with additional support from smaller complexes (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_08700.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1). Thus, much of the module reflects established protein associations, shared complex membership, co-localization or common plasma abundance rather than undiscovered pairwise biology. IGHG1, IGHG2 and IGKC have no reported STRING partners or hu.MAP complexes in the fact sheet, so their module connections may reflect co-abundance, antibody-related sample composition or relationships not represented in those resources.

**STRING interactions (score >= 0.7)**: 19 of 78 gene pairs: A2M–ALB (0.98); A2M–ORM1 (0.809); A2M–ORM2 (0.808); A2M–SERPINA1 (0.98); A2M–TF (0.82); ALB–C3 (0.959); ALB–ORM1 (0.998); ALB–ORM2 (0.998); ALB–SERPINA1 (0.998); ALB–TF (0.9); C3–ORM1 (0.775); C3–ORM2 (0.772); C3–SERPINA1 (0.859); GLB1–GNS (0.957); ORM1–ORM2 (0.999); ORM1–SERPINA1 (0.979); ORM1–TF (0.731); ORM2–SERPINA1 (0.972); SERPINA1–TF (0.848)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Secretory granule (FDR = 0.0079, 10 genes); COMPARTMENTS Secretory granule lumen (FDR = 0.0079, 9 genes); Component Secretory granule (FDR = 0.0113, 10 genes); Component Secretory granule lumen (FDR = 0.0113, 9 genes); PMID (2023) Direct Proteomic Detection and Prioritization of 19 Onchocerciasis Biomarker Candidates in Humans. (FDR = 0.0274, 6 genes); PMID (2023) Neural stem cell transplantation in patients with progressive multiple sclerosis: an open-label, phase 1 study. (FDR = 0.0274, 6 genes); PMID (2023) Quantitative proteomic analysis of human serum using tandem mass tags to predict cardiovascular risks in patients with psoriasis. (FDR = 0.0274, 7 genes); PMID (2023) An optimized workflow for MS-based quantitative proteomics of challenging clinical bronchoalveolar lavage fluid (BALF) samples. (FDR = 0.0274, 6 genes); PMID (2022) Elevated plasma alpha1-antichymotrypsin is a biomarker candidate for malaria patients. (FDR = 0.0274, 6 genes); PMID (2021) Fetal bovine serum albumin inhibits antimicrobial peptide activity and binds drug only in complex with alpha1-antitrypsin. (FDR = 0.0274, 6 genes); PMID (2021) Identification of serum prognostic biomarkers of severe COVID-19 using a quantitative proteomic approach. (FDR = 0.0274, 7 genes); PMID (2020) A Dual Workflow to Improve the Proteomic Coverage in Plasma Using Data-Independent Acquisition-MS. (FDR = 0.0274, 7 genes); PMID (2019) Affinity depletion versus relative protein enrichment: a side-by-side comparison of two major strategies for increasing human cerebrospinal fluid proteome coverage. (FDR = 0.0274, 6 genes); PMID (2018) Circulating MicroRNA Expression Levels Associated With Internet Gaming Disorder. (FDR = 0.0274, 7 genes); PMID (2017) Pulse of inflammatory proteins in the pregnant uterus of European polecats (Mustela putorius) leading to the time of implantation. (FDR = 0.0274, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08395.1 (SERPINA1, A2M, C3, ORM1, ALB, TF, ORM2; 7/43); huMAP3_09531.1 (SERPINA1, A2M, C3, ORM1, ALB, TF, ORM2; 7/47); huMAP3_10101.1 (SERPINA1, A2M, C3, ORM1, ALB, TF, ORM2; 7/49); huMAP3_15040.1 (SERPINA1, A2M, C3, ORM1, ALB, TF, ORM2; 7/64); huMAP3_10678.1 (SERPINA1, A2M, C3, ORM1, ALB, TF, ORM2; 7/71); huMAP3_07432.1 (SERPINA1, C3, ORM1, ALB, TF, ORM2; 6/18); huMAP3_07265.1 (SERPINA1, A2M, ORM1, ALB, TF, ORM2; 6/20); huMAP3_09434.1 (SERPINA1, C3, ORM1, ALB, TF; 5/33); huMAP3_02242.1 (C3, ORM1, TF; 3/9); huMAP3_08700.1 (SERPINA1, ORM1, ALB; 3/11); huMAP3_08224.1 (C3, TF; 2/21); huMAP3_07701.1 (A2M, ORM2; 2/22); huMAP3_09273.1 (A2M, ORM2; 2/28)

### Novelty

This should not be claimed as a wholly new molecular complex or interaction network. The central plasma-protein pattern is supported by established STRING relationships and repeated hu.MAP complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_08700.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1). The same proteins also recur in supplementary STRING literature annotations involving serum, plasma, cerebrospinal fluid and inflammatory biomarker studies (11 supplementary STRING terms; within-query FDR 0.0274–0.0274). A potentially novel aspect is the module-level co-abundance association shared by cerebrospinal fluid and testis, particularly the combination of the plasma-protein core with lysosomal and immunoglobulin members. However, absence from STRING or hu.MAP would not itself establish novelty, and the evidence does not demonstrate a tissue-specific mechanism, causality or a previously unknown physical complex. The conservative conclusion is that this is a new dataset-level association or reuse of known circulating-protein biology, not evidence for a newly discovered pathway.

**Hypothesis.** Hypothesis: the shared module reflects a circulating extracellular inflammatory and homeostatic compartment sampled in both cerebrospinal fluid and testis. Liver-derived acute-phase and transport proteins may covary with complement and protease-control proteins, while immunoglobulin and myeloid-associated proteins may reflect plasma-cell or blood-cell contribution. Albumin and transferrin could provide carrier and iron-handling context; C3, SERPINA1, A2M, ORM1 and ORM2 could jointly reflect regulation of complement, extracellular proteolysis and inflammatory signalling. GLB1 and GNS may represent lysosomal or vesicular material associated with the same extracellular or cellular contribution. This hypothesis predicts that the module will track blood contamination, barrier permeability, inflammation and cellular composition more strongly than a specialized testis or cerebrospinal-fluid program. It requires validation using independent cohorts, blood-contamination markers, cell-type deconvolution, targeted protein measurements and tissue-specific comparisons.

### Important genes

#### ORM1

- **Related proteins** (co-abundance neighbors): ORM2 (0.96), TF (0.89), GNS (0.85), GLB1 (0.84), IGHG1 (0.82), SERPINA1 (0.81); STRING partners: A2M (0.809), ALB (0.998), C3 (0.775), ORM2 (0.999), SERPINA1 (0.979), TF (0.731)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_02242.1, huMAP3_08700.1
- **Function (MyGene.info)**: orosomucoid 1. This gene encodes a key acute phase plasma protein. Because of its increase due to acute inflammation, this protein is classified as an acute-phase reactant.  The specific function of this protein has not yet been determined; however, it may be involved in aspects of immunosuppression. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.102); nephronophthisis (0.088); familial idiopathic steroid-resistant nephrotic syndrome (0.087); colorectal carcinoma (0.083); breast cancer (0.083)
- **Europe PMC papers**: 2436
- **Why important**: ORM1 has the strongest weighted network position in the module and connects the acute-phase and transport-associated core to ORM2, TF, GNS, GLB1, IGHG1 and SERPINA1. HPA identifies liver and hepatocyte enrichment, secretion to blood and neutrophil association. ORM1 appears in the secretory-granule STRING annotations (15 supplementary STRING terms; within-query FDR 0.0079–0.0274) and in many hu.MAP complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_08700.1). Its established identity as an acute-phase plasma protein and its substantial literature support make it a strong indicator of the module's circulating inflammatory context.
- **Conclusion**: Established evidence supports ORM1 as a central liver-derived acute-phase component of a known plasma-protein network. It may help mark the shared extracellular compartment, but co-abundance does not establish that ORM1 causally organizes the module.

#### TF

- **Related proteins** (co-abundance neighbors): SERPINA1 (0.92), ORM1 (0.89), ORM2 (0.85), ALB (0.83), IGHG2 (0.83), IGKC (0.81); STRING partners: A2M (0.82), ALB (0.9), ORM1 (0.731), SERPINA1 (0.848)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_02242.1, huMAP3_08224.1
- **Function (MyGene.info)**: transferrin. This gene encodes a glycoprotein with an approximate molecular weight of 76.5 kDa. It is thought to have been created as a result of an ancient gene duplication event that led to generation of homologous C and N-terminal domains each of which binds one ion of ferric iron. The function of this protein is to transport iron from the intestine, reticuloendothelial system, and liver parenchymal cells t…
- **Diseases (Open Targets)**: atransferrinemia (0.776); alcohol drinking (0.492); hemochromatosis type 1 (0.471); neurodegenerative disease (0.400); urolithiasis (0.329)
- **Europe PMC papers**: 143656
- **Why important**: TF is among the most connected module members and links SERPINA1, ORM1, ORM2, ALB, IGHG2 and IGKC. It is secreted to blood and is enriched in liver-related contexts. It recurs in hu.MAP plasma-protein complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1), (hu.MAP huMAP3_09434.1), (hu.MAP huMAP3_02242.1) and (hu.MAP huMAP3_08224.1). Its established role in ferric-iron transport provides a distinct physiological function within a module otherwise dominated by acute-phase and complement proteins. It also has extensive disease and literature associations.
- **Conclusion**: Established evidence supports TF as a circulating iron-transport protein embedded in the known plasma network. It is plausible that iron homeostasis covaries with the inflammatory state represented by the module, but the module does not show that TF drives this relationship.

#### SERPINA1

- **Related proteins** (co-abundance neighbors): TF (0.92), ORM2 (0.87), ORM1 (0.81); STRING partners: A2M (0.98), ALB (0.998), C3 (0.859), ORM1 (0.979), ORM2 (0.972), TF (0.848)
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08700.1
- **Function (MyGene.info)**: serpin family A member 1. The protein encoded by this gene is a serine protease inhibitor belonging to the serpin superfamily whose targets include elastase, plasmin, thrombin, trypsin, chymotrypsin, and plasminogen activator. This protein is produced in the liver, the bone marrow, by lymphocytic and monocytic cells in lymphoid tissue, and by the Paneth cells of the gut. Defects in this gene are associated with chronic obs…
- **Diseases (Open Targets)**: alpha 1-antitrypsin deficiency (0.768); chronic obstructive pulmonary disease (0.690); cirrhosis of liver (0.573); cholelithiasis (0.569); pulmonary emphysema (0.569)
- **Europe PMC papers**: 6526
- **Why important**: SERPINA1 is connected to A2M, ALB, C3, ORM1, ORM2 and TF in STRING and recurs across hu.MAP complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_02242.1) (hu.MAP huMAP3_08700.1). HPA places it in liver and epithelial contexts, in monocyte and neutrophil-associated blood groups, and in the secreted-to-blood compartment. Its established serine-protease inhibitory function and associations with alpha-one-antitrypsin deficiency, chronic obstructive pulmonary disease, emphysema and liver disease give it strong biological and disease relevance.
- **Conclusion**: Established evidence supports SERPINA1 as a circulating protease-control and acute-inflammatory component. It could help explain coordinated extracellular proteolysis, but a mechanistic role in the cross-tissue association remains hypothetical.

#### C3

- **Related proteins** (co-abundance neighbors): A2M (0.90), IGKC (0.84); STRING partners: ALB (0.959), ORM1 (0.775), ORM2 (0.772), SERPINA1 (0.859)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_02242.1, huMAP3_08224.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is connected to A2M and IGKC in the module and has STRING relationships with ALB, ORM1, ORM2 and SERPINA1. HPA identifies liver enrichment, secretion to blood and monocyte association. C3 appears in many hu.MAP complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1), (hu.MAP huMAP3_09434.1), (hu.MAP huMAP3_02242.1) and (hu.MAP huMAP3_08224.1). Its established central role in complement activation, inflammatory signalling and antimicrobial activity, together with extensive disease literature, makes it the clearest immune-effector representative.
- **Conclusion**: Established evidence supports C3 as a complement and inflammatory component of the known extracellular plasma network. Its presence is compatible with immune activation or barrier-associated fluid composition, but it does not establish active complement processing in either sampled tissue.

#### ALB

- **Related proteins** (co-abundance neighbors): ECE1 (0.87), TF (0.83); STRING partners: A2M (0.98), C3 (0.959), ORM1 (0.998), ORM2 (0.998), SERPINA1 (0.998), TF (0.9)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08700.1
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB is a core plasma protein in STRING and appears repeatedly in hu.MAP complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1) and (hu.MAP huMAP3_08700.1). HPA identifies liver and hepatocyte enrichment and secretion to blood. Its established role as a major blood protein and carrier of endogenous and exogenous molecules makes it especially informative for sample composition and vascular or blood-derived influence. It also links to C3, A2M, ORM1, ORM2, SERPINA1 and TF in STRING.
- **Conclusion**: Established evidence supports ALB as a marker of the circulating plasma compartment and a carrier protein within the known network. Its importance here is more likely to indicate sample origin and extracellular context than a specialized tissue mechanism.

## Module 2

**Tissue pair**: cerebrospinal_fluid and testis  
**Genes (12)**: A1BG, APP, C1R, C5, GSN, HPX, SERPIND1, SERPINA5, ITIH1, RBP4, F2, GC

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established pathway annotation from enrichment analysis. Its composition and network structure instead point to a circulating extracellular protease, coagulation, complement, carrier-protein, and extracellular-matrix-associated program. The strongest biological interpretation is coordinated abundance of plasma proteins involved in hemostasis, innate immune proteolysis, transport of heme, vitamin D and retinol, and extracellular matrix or hyaluronan handling. This is an interpretation of the gene identities and network structure, not a claim of significant GO/KEGG enrichment. The APP–GSN connection and the cluster involving ITIH1, GC, GSN and HPX provide a possible link to nervous-system or extracellular-remodelling biology, but the shared module is more convincingly characterized as a secreted plasma-protein assemblage than as a neuronal pathway.

**Cell composition.** The module is strongly dominated by secreted proteins and by liver or hepatocyte-associated expression. HPA classifies nearly all members as secreted to blood or as tissue-enriched or tissue-enhanced in liver, with hepatocytes the most recurrent single-cell annotation. Most members are not detected in immune cells, arguing against the module being primarily a blood-cell transcript or protein signature. A small minority have immune-cell annotations, including APP and GSN-associated annotations, but these do not define the overall composition. The abundance of liver-derived plasma proteins means that the shared cerebrospinal-fluid/testis pattern could reflect circulating protein access, vascular or barrier exchange, or common extracellular material rather than coordinated local production in both tissues. HPA testis protein detection is present for some members and absent for others, while the supplied cerebrospinal-fluid HPA field has no informative tissue comparison. Thus, local testis expression for selected genes should not be generalized to the entire module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a biologically coherent core rather than an entirely unconnected set. Established high-confidence relationships include F2 with C5, SERPINA5 and SERPIND1; GC with HPX, GSN and RBP4; F2 with GC and HPX; and APP with GSN. These relationships connect coagulation and protease regulation with carrier and extracellular proteins. The co-abundance edges involving C1R are not represented as STRING partners in the fact sheet, so they should be treated as module-level associations rather than established physical interactions. hu.MAP repeatedly places F2, C5, HPX, A1BG, ITIH1, GC, SERPIND1 and RBP4 in plasma-protein complexes, especially in C1, C2, C3, C4, C5, C6, C7, C8, C10, C11, C12 and related complexes. The recurrence of overlapping members across these complexes supports a shared extracellular or plasma-protein context, but the complexes are broad and include many proteins absent from the module. Therefore, hu.MAP supports membership in known protein milieus more strongly than it demonstrates one discrete physical complex formed by all module members.

**STRING interactions (score >= 0.7)**: 9 of 66 gene pairs: APP–GSN (0.86); C5–F2 (0.921); F2–GC (0.792); F2–HPX (0.716); F2–SERPINA5 (0.996); F2–SERPIND1 (0.999); GC–GSN (0.826); GC–HPX (0.827); GC–RBP4 (0.749)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10678.1 (F2, C5, GC, HPX, A1BG, SERPIND1, ITIH1; 7/71); huMAP3_08395.1 (F2, C5, HPX, A1BG, ITIH1; 5/43); huMAP3_09531.1 (F2, C5, HPX, A1BG, ITIH1; 5/47); huMAP3_10101.1 (F2, C5, HPX, A1BG, ITIH1; 5/49); huMAP3_15040.1 (GC, HPX, A1BG, SERPIND1, ITIH1; 5/64); huMAP3_08796.1 (F2, C5, RBP4, ITIH1; 4/15); huMAP3_09832.1 (F2, C5, RBP4, ITIH1; 4/18); huMAP3_09434.1 (C5, GC, A1BG, SERPIND1; 4/33); huMAP3_00178.1 (C5, RBP4, ITIH1; 3/9); huMAP3_07541.1 (F2, C5, ITIH1; 3/19); huMAP3_08224.1 (C5, GC, SERPIND1; 3/21); huMAP3_09273.1 (F2, HPX, ITIH1; 3/28); huMAP3_07119.1 (C5, RBP4; 2/6); huMAP3_02236.1 (HPX, A1BG; 2/7); huMAP3_02811.1 (C5, ITIH1; 2/8); huMAP3_08700.1 (HPX, A1BG; 2/11); huMAP3_07432.1 (HPX, A1BG; 2/18); huMAP3_07265.1 (HPX, A1BG; 2/20); huMAP3_07701.1 (F2, ITIH1; 2/22)

### Novelty

The module should not be described as a newly discovered molecular complex or pathway. Several of its central relationships are already represented in STRING, and many of its proteins recur in hu.MAP plasma-protein complexes. The lack of globally significant GO/KEGG enrichment also limits claims of a newly defined functional pathway. A potentially novel aspect is the co-abundance of this particular secreted-protein assemblage across cerebrospinal fluid and testis, especially the dataset-level association involving APP, GSN, ITIH1, GC, coagulation proteins and complement proteins. However, the fact sheet does not establish that this cross-tissue association has not been reported elsewhere, and absence from a database would not prove novelty. The most defensible conclusion is that the cross-tissue co-abundance pattern may be a new observation, whereas much of its molecular content and interaction context is already known.

**Hypothesis.** Hypothesis: the module represents a shared extracellular-fluid state in which liver-derived carrier proteins and protease regulators enter or are retained in cerebrospinal fluid and testis-associated extracellular compartments. Within this state, F2 and C5 provide protease and complement activity, SERPIND1 and SERPINA5 restrain serine proteases, HPX buffers heme-associated oxidative stress, GC and RBP4 transport metabolites, and ITIH1 may link the circulating protein environment to hyaluronan-rich extracellular matrix. GSN and APP could connect this extracellular milieu to actin or membrane-associated processes in nervous-system and barrier tissues. This hypothesis predicts that the module will track vascular permeability, barrier integrity, inflammation, coagulation or extracellular-matrix remodelling more strongly than a tissue-specific intracellular program. It requires validation with independent cohorts, measurements of plasma contamination or barrier leakage, and protein-level localization in cerebrospinal fluid and testis.

### Important genes

#### ITIH1

- **Related proteins** (co-abundance neighbors): GSN (0.86), HPX (0.85), APP (0.85), F2 (0.83), GC (0.81), SERPINA5 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_00178.1, huMAP3_07541.1, huMAP3_09273.1, huMAP3_02811.1, huMAP3_07701.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 1. This gene encodes a member of the inter-alpha-trypsin inhibitor family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the heavy chain of the inter-alpha-trypsin inhibitor complex, which is secreted by hepatocytes into the blood. The heavy chain also interacts with hyaluronan, and…
- **Diseases (Open Targets)**: osteoarthritis, hip (0.305); osteoarthritis (0.188); schizophrenia (0.185); major depressive disorder (0.183); psychiatric disorder (0.171)
- **Europe PMC papers**: 963
- **Why important**: ITIH1 has the strongest central network position in the supplied module and connects GSN, HPX, APP, F2, GC and SERPINA5. It is a liver-derived secreted inter-alpha-trypsin inhibitor family protein that interacts with hyaluronan and has reported relevance to ovulation and fertilization. It is represented across many hu.MAP complexes, while STRING does not list partners for it, making its co-abundance connectivity especially informative but not equivalent to established physical interaction. Its disease and literature associations include osteoarthritis and psychiatric disorders, with a moderate literature volume relative to the best-studied module members.
- **Conclusion**: Established evidence supports ITIH1 as a secreted liver protein with extracellular-matrix and hyaluronan-related biology and as a network bridge in this module. It is plausible, but unproven, that ITIH1 helps organize the shared extracellular environment in cerebrospinal fluid and testis.

#### F2

- **Related proteins** (co-abundance neighbors): ITIH1 (0.83), C1R (0.81); STRING partners: C5 (0.921), GC (0.792), HPX (0.716), SERPINA5 (0.996), SERPIND1 (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07541.1, huMAP3_09273.1, huMAP3_07701.1
- **Function (MyGene.info)**: coagulation factor II, thrombin. This gene encodes the prothrombin protein (also known as coagulation factor II). This protein is proteolytically cleaved in multiple steps to form the activated serine protease thrombin. The activated thrombin enzyme plays an important role in thrombosis and hemostasis by converting fibrinogen to fibrin during blood clot formation, by stimulating platelet aggregation, and by activating additional …
- **Diseases (Open Targets)**: congenital prothrombin deficiency (0.827); thrombophilia due to thrombin defect (0.738); venous thromboembolism (0.727); deep vein thrombosis (0.690); blood coagulation disease (0.670)
- **Europe PMC papers**: 109299
- **Why important**: F2 is a central coagulation component with strong STRING relationships to C5, SERPINA5, SERPIND1, GC and HPX, and it occurs across many hu.MAP complexes represented in the module. Its established function includes thrombin generation, fibrin formation, platelet activation, wound responses and cell-surface receptor signalling. It has very extensive disease literature involving prothrombin deficiency, thrombophilia and venous thromboembolism.
- **Conclusion**: Established evidence identifies F2 as the module's clearest coagulation anchor and as a known interaction hub linking coagulation to carrier and complement-associated proteins. The module does not establish active thrombin generation in either tissue; coordinated F2 abundance could instead reflect transport, vascular access or altered protease balance.

#### C5

- **Related proteins** (co-abundance neighbors): SERPIND1 (0.87), C1R (0.81); STRING partners: F2 (0.921)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_09434.1, huMAP3_00178.1, huMAP3_07541.1, huMAP3_08224.1, huMAP3_07119.1, huMAP3_02811.1
- **Function (MyGene.info)**: complement C5. This gene encodes a component of the complement system, a part of the innate immune system that plays an important role in inflammation, host homeostasis, and host defense against pathogens. The encoded preproprotein is proteolytically processed to generate multiple protein products, including the C5 alpha chain, C5 beta chain, C5a anaphylatoxin and C5b. The C5 protein is comprised of the C5 alpha…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.744); paroxysmal nocturnal hemoglobinuria (0.610); myasthenia gravis (0.586); atypical hemolytic-uremic syndrome (0.544); neuromyelitis optica (0.516)
- **Europe PMC papers**: 81450
- **Why important**: C5 is a complement component with established roles in complement activation, chemotaxis and inflammatory responses. It connects to F2 and SERPIND1 in STRING and is repeatedly represented in hu.MAP complexes with F2, HPX, A1BG, ITIH1, GC and RBP4. Its extensive disease literature includes complement deficiencies, paroxysmal nocturnal hemoglobinuria, myasthenia gravis, atypical hemolytic-uremic syndrome and neuromyelitis optica.
- **Conclusion**: Established evidence supports C5 as the principal innate-immune proteolysis anchor of the module, alongside coagulation-related proteins. The co-abundance pattern may indicate a shared inflammatory or vascular-fluid context, but it does not by itself show complement activation or local complement synthesis.

#### GC

- **Related proteins** (co-abundance neighbors): A1BG (0.86), GSN (0.85), ITIH1 (0.81); STRING partners: F2 (0.792), GSN (0.826), HPX (0.827), RBP4 (0.749)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_15040.1, huMAP3_09434.1, huMAP3_08224.1
- **Function (MyGene.info)**: GC vitamin D binding protein. The protein encoded by this gene belongs to the albumin gene family. It is a multifunctional protein found in plasma, ascitic fluid, cerebrospinal fluid and on the surface of many cell types. It binds to vitamin D and its plasma metabolites and transports them to target tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq,…
- **Diseases (Open Targets)**: vitamin D deficiency (0.574); vitamin deficiency (0.552); chronic obstructive pulmonary disease (0.499); squamous cell carcinoma (0.339); central nervous system cancer (0.334)
- **Europe PMC papers**: 363974
- **Why important**: GC is a highly connected carrier protein linking A1BG, GSN and ITIH1 in the module and linking F2, GSN, HPX and RBP4 through STRING. It is a secreted liver-associated vitamin D binding protein found in plasma and cerebrospinal fluid, with functions in vitamin D and metabolite transport. It is represented in several hu.MAP complexes and has a very large literature base, including associations with vitamin deficiency and central nervous system cancer.
- **Conclusion**: Established evidence supports GC as a strong marker of circulating extracellular-fluid composition and as a transport-related bridge between the module's carrier and protease components. Its presence makes plasma access or fluid exchange a particularly plausible explanation for the shared tissue-module pattern, although it does not identify the direction or mechanism of transport.

#### SERPINA5

- **Related proteins** (co-abundance neighbors): ITIH1 (0.81); STRING partners: F2 (0.996)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family A member 5. The protein encoded by this gene is a member of the serpin family of proteins, a group of proteins that inhibit serine proteases. This gene is one in a cluster of serpin genes located on the q arm of chromosome 14. This family member is a glycoprotein that can inhibit several serine proteases, including protein C and various plasminogen activators and kallikreins, and it thus plays diverse roles i…
- **Diseases (Open Targets)**: chronic kidney disease (0.432); preeclampsia (0.352); ankylosing spondylitis (0.204); neurodegenerative disease (0.195); hematologic disorder (0.116)
- **Europe PMC papers**: 1059
- **Why important**: SERPINA5 is directly connected to F2 in STRING and is the module member with the clearest testis-associated annotation, including tissue enhancement in testis and early spermatids. It inhibits several serine proteases, including protein C, plasminogen activators and kallikreins, and is annotated for spermatogenesis, sperm-egg membrane fusion and seminal clot liquefaction. Its literature volume is smaller than that of F2, C5, GC or APP, but its tissue and functional specificity is particularly relevant to this tissue pair.
- **Conclusion**: Established evidence supports SERPINA5 as a testis-relevant extracellular protease regulator and a plausible bridge between reproductive biology and the module's coagulation network. Its co-abundance with liver-derived proteins may reflect genuine testicular extracellular biology, circulating protein exposure, or both; the present data cannot distinguish these possibilities.

## Module 3

**Tissue pair**: cerebrospinal_fluid and testis  
**Genes (9)**: SERPINA3, CADM1, SERPINA6, GSTP1, LDHB, LGALS1, PGK1, ACP2, TFRC

### Function

No GO or KEGG term passed global correction, and there were no supplementary STRING enrichment terms. The module therefore does not support a single statistically established pathway-level function. Its members span several established biological activities: lactate and glycolytic metabolism through LDHB and PGK1; glutathione-dependent detoxification and oxidative-stress responses through GSTP1; cell adhesion, cell recognition, and cytokine-related signaling through CADM1; galectin-mediated cell and matrix interactions through LGALS1; lysosomal phosphatase activity through ACP2; iron uptake through TFRC; and extracellular protease inhibition or steroid transport through SERPINA3 and SERPINA6. The co-abundance structure may therefore represent a mixed metabolic, stress-response, adhesion, and extracellular-protein state rather than a canonical molecular complex. The network is internally connected, with SERPINA3, LDHB, CADM1, PGK1, and LGALS1 occupying the more central positions, but the absence of independent pathway or interaction enrichment weakens a claim of a unified biochemical mechanism.No GO or KEGG term passed global correction.No STRING functional-enrichment term was reported.

**Cell composition.** The module has a substantial extracellular or blood-associated component: SERPINA3, LGALS1, SERPINA6, and TFRC are annotated as secreted to blood in the HPA summary. SERPINA6 is liver-enriched, while SERPINA3 is group-enriched in liver and pancreas and has astrocyte cell-type enrichment. This raises the possibility that part of the shared cerebrospinal-fluid and testis signal reflects circulating proteins, vascular or barrier-associated material, or sample composition rather than a tissue-specific intracellular program. The module is not predominantly blood-cell specific: several genes have low immune-cell specificity, some are immune-cell enhanced, and some are not detected in immune cells. HPA profiles are heterogeneous, including liver, heart muscle, kidney, retina, and esophagus tissue associations, as well as astrocyte, hepatocyte, epithelial, stromal, and trophoblast cell-type associations. Most module proteins are detected in testis, but the supplied HPA cerebrospinal-fluid protein field has no informative matching data. Thus, shared cell states, extracellular carryover, or broad cellular stress may be more plausible explanations than a dedicated cerebrospinal-fluid–testis program. The composition is mixed rather than uniformly tissue-specific.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module gene pair reached the supplied high-confidence STRING interaction threshold, and no hu.MAP complex contained at least two module members. The observed co-abundance edges are therefore not corroborated by the queried physical or functional interaction resources. Known biology still exists for individual genes: LDHB, PGK1, GSTP1, and ACP2 have enzymatic or lysosomal functions; CADM1 mediates cell recognition and adhesion; LGALS1 participates in cell and matrix interactions; TFRC mediates receptor-dependent iron uptake; and SERPINA3 and SERPINA6 are extracellular serpin-family proteins with protease-inhibitory or steroid-transport roles. The distinction is important: the module network indicates coordinated abundance, not established direct binding, shared complex membership, or a validated signaling pathway. The lack of STRING and hu.MAP support makes a technical, compositional, or context-dependent co-abundance explanation more important to consider.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The coordinated module pattern may be a new observation because this particular combination of genes has no corroborating high-confidence STRING pair and no shared hu.MAP complex in the supplied resources. However, that absence does not establish novelty: the component genes and their individual functions are well studied, and several have extensive disease and literature associations. The strongest defensible claim is that a cerebrospinal-fluid–testis co-abundance pattern involving these genes is not explained by currently supplied interaction or complex annotations. Novelty should be tested by replication in independent cohorts, preservation analysis, adjustment for blood contamination and cell-type composition, comparison with other tissue pairs, and targeted measurement of the proteins or transcripts. Until then, the module should be considered a potentially novel association rather than a newly discovered molecular complex.

**Hypothesis.** Hypothesis: the module reflects a shared extracellular and cellular-stress state present in the two sample groups, combining secreted plasma-associated proteins with metabolic, detoxification, adhesion, lysosomal, and iron-uptake proteins. In cerebrospinal-fluid samples, circulating or barrier-associated proteins and astrocyte-related material could contribute to the signal; in testis, broad expression and the strong testis protein-detection pattern could generate a parallel abundance state. A possible mechanistic scenario is that altered tissue or barrier physiology produces extracellular SERPINA3, SERPINA6, and LGALS1 together with intracellular glycolytic and redox responses involving LDHB, PGK1, and GSTP1, while CADM1 and TFRC mark accompanying changes in cell contact and iron handling. This is a hypothesis, not an established pathway, because global GO/KEGG evidence, STRING support, and hu.MAP complex support are absent.

### Important genes

#### SERPINA3

- **Related proteins** (co-abundance neighbors): LDHB (0.92), PGK1 (0.87), CADM1 (0.85), GSTP1 (0.83), LGALS1 (0.82), TFRC (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family A member 3. The protein encoded by this gene is a member of the serpin family of proteins, a group of proteins that inhibit serine proteases. This gene is one in a cluster of serpin genes located on the q arm of chromosome 14. Polymorphisms in this protein appear to be tissue specific and influence protease targeting. Variations in this protein's sequence have been implicated in Alzheimer's disease, and defic…
- **Diseases (Open Targets)**: prostate carcinoma (0.359); chronic kidney disease (0.217); peripheral arterial occlusive disease 1 (0.118); central nervous system cancer (0.118); glioma (0.105)
- **Europe PMC papers**: 5458
- **Why important**: SERPINA3 is the most central network member by supplied connectivity and links metabolic, adhesion, detoxification, and iron-related neighbors. It is a secreted-to-blood protein with liver and pancreas group enrichment and astrocyte cell-type enrichment. Its serpin function, inflammatory and cytokine-related annotations, Alzheimer disease relevance, liver-disease association, and extensive literature make it a strong candidate for distinguishing extracellular or inflammatory composition from a true intracellular module.
- **Conclusion**: Established evidence supports SERPINA3 as a secreted serine-protease inhibitor associated with inflammatory biology and liver-related disease, and the network places it near the module center. It is not established that SERPINA3 mechanistically organizes this module. Hypothesis: SERPINA3 may be an extracellular or barrier-associated driver of the shared abundance pattern, or a marker of sample composition rather than a causal hub.

#### LDHB

- **Related proteins** (co-abundance neighbors): SERPINA3 (0.92), GSTP1 (0.89), PGK1 (0.89), LGALS1 (0.87), CADM1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lactate dehydrogenase B. This gene encodes the B subunit of lactate dehydrogenase enzyme, which catalyzes the interconversion of pyruvate and lactate with concomitant interconversion of NADH and NAD+ in a post-glycolysis process. Alternatively spliced transcript variants have been found for this gene. Recent studies have shown that a C-terminally extended isoform is produced by use of an alternative in-frame translation t…
- **Diseases (Open Targets)**: glycogen storage disease due to lactate dehydrogenase H-subunit deficiency (0.724); type 2 diabetes mellitus (0.271); adverse effect (0.184); neoplasm (0.117); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 5204
- **Why important**: LDHB is one of the most connected genes and forms strong co-abundance links with several central members. It has a defined role in lactate and pyruvate metabolism and NAD redox balance, is tissue-enhanced in heart muscle and kidney, and is associated with lactate dehydrogenase deficiency and metabolic disease. Its large literature base makes it a useful anchor for testing whether the module contains a reproducible metabolic component.
- **Conclusion**: Established evidence supports LDHB as a cytosolic metabolic enzyme, not as a component of a known complex with the other module genes. Hypothesis: its co-abundance may reflect altered glycolytic or redox state shared across cells in the two sample groups, but it could also be a broad cellular-state marker.

#### CADM1

- **Related proteins** (co-abundance neighbors): ACP2 (0.91), PGK1 (0.88), SERPINA6 (0.87), SERPINA3 (0.85), LDHB (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell adhesion molecule 1. Enables signaling receptor binding activity. Involved in several processes, including cell recognition; positive regulation of cytokine production; and susceptibility to natural killer cell mediated cytotoxicity. Located in plasma membrane. Implicated in breast carcinoma and prostate cancer. Biomarker of cervix uteri carcinoma in situ. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypothyroidism (0.505); Abnormality of the skeletal system (0.485); obesity disorder (0.420); restless legs syndrome (0.402); autoimmune thyroid disease (0.342)
- **Europe PMC papers**: 3471
- **Why important**: CADM1 is a highly connected membrane protein and links the central metabolic and extracellular members to ACP2 and SERPINA6. It has established roles in homophilic and heterophilic cell adhesion, cell recognition, cytokine regulation, and susceptibility to natural-killer-cell cytotoxicity. Its retina and astrocyte-related HPA annotations, plasma-membrane localization, cancer associations, and substantial literature make it important for evaluating a barrier, adhesion, or cell-composition interpretation.
- **Conclusion**: Established evidence supports CADM1 as a cell-adhesion and recognition molecule with immune-relevant signaling functions. There is no supplied evidence that it directly binds the other module proteins or forms a shared complex with them. Hypothesis: CADM1 may mark altered cell contacts or tissue-barrier composition that brings otherwise distinct extracellular and metabolic proteins into a co-abundance pattern.

#### PGK1

- **Related proteins** (co-abundance neighbors): LDHB (0.89), CADM1 (0.88), SERPINA3 (0.87), LGALS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece, Principal piece, End piece; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglycerate kinase 1. The protein encoded by this gene is a glycolytic enzyme that catalyzes the conversion of 1,3-diphosphoglycerate to 3-phosphoglycerate. The encoded protein may also act as a cofactor for polymerase alpha. Additionally, this protein is secreted by tumor cells where it participates in angiogenesis by functioning to reduce disulfide bonds in the serine protease, plasmin, which consequently leads to th…
- **Diseases (Open Targets)**: glycogen storage disease due to phosphoglycerate kinase 1 deficiency (0.823); Menkes disease (0.578); X-linked distal spinal muscular atrophy type 3 (0.556); occipital horn syndrome (0.556); hereditary disease (0.520)
- **Europe PMC papers**: 14784
- **Why important**: PGK1 is a central network member connected to LDHB, CADM1, SERPINA3, and LGALS1. It is a core glycolytic enzyme with additional reported roles in angiogenesis and epithelial differentiation, has broad tissue specificity, and shows testis localization in the supplied HPA evidence. Its very extensive literature and disease associations make it a strong metabolic-state marker and a practical candidate for experimental validation.
- **Conclusion**: Established evidence supports PGK1 as a glycolytic enzyme with context-dependent extracellular and angiogenic functions. The module does not establish which of these roles is relevant here. Hypothesis: PGK1 may report a shared energetic or hypoxic state, while its co-abundance with secreted proteins could reflect cellular stress, tissue injury, or sample composition.

#### LGALS1

- **Related proteins** (co-abundance neighbors): LDHB (0.87), GSTP1 (0.86), SERPINA3 (0.82), PGK1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galectin 1. The galectins are a family of beta-galactoside-binding proteins implicated in modulating cell-cell and cell-matrix interactions. This gene product may act as an autocrine negative growth factor that regulates cell proliferation. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: glaucoma (0.349); open-angle glaucoma (0.343); chronic kidney disease (0.330); smoking initiation (0.162); melanoma (0.121)
- **Europe PMC papers**: 4025
- **Why important**: LGALS1 is connected to several central members and is secreted to blood despite also being annotated in the cytosol. It regulates cell and matrix interactions, apoptosis, and NF-kappaB-related signaling, with cell-type enrichment in stromal and dendritic-cell contexts. Its associations with glaucoma, kidney disease, and melanoma and its broad literature make it relevant to extracellular signaling, inflammation, and tissue remodeling interpretations.
- **Conclusion**: Established evidence supports LGALS1 as a beta-galactoside-binding protein involved in cell interactions and regulated cell death, with both intracellular and secreted contexts. No supplied evidence demonstrates a physical complex with this module. Hypothesis: LGALS1 may connect extracellular remodeling or inflammatory signaling to the metabolic and adhesion state represented by the module, or may simply reflect shared secreted-protein abundance.

## Module 4

**Tissue pair**: cerebrospinal_fluid and testis  
**Genes (5)**: ACE, CTSF, CPVL, IGHG3, LCN2

### Function

No GO/KEGG term passed global correction, and there is no supplementary STRING enrichment. The most defensible functional interpretation is a secreted and vesicular proteolysis–immune module, combining ACE-mediated peptide processing, LCN2-associated innate immune and iron-sequestration biology, CPVL-associated carboxypeptidase-like activity, CTSF lysosomal proteolysis, and IGHG3 immunoglobulin biology. The co-abundance pattern is therefore more consistent with a tissue- or cell-composition-linked extracellular and intracellular protein-processing program than with a single demonstrated biochemical pathway. The functional interpretation remains provisional because the module has no globally significant pathway annotation and no experimentally supported interaction network in the supplied resources.

**Cell composition.** All module proteins are annotated as secreted, immunoglobulin-related, or intracellular and membrane-associated proteins rather than as broadly expressed housekeeping proteins. HPA annotations emphasize choroid plexus, lymphoid tissue, testis, spermatid populations, myeloid cells, B cells, and neutrophil-lineage cells. The presence of IGHG3 points to plasma-cell or B-cell material, while LCN2 and CPVL point toward innate immune and myeloid-associated material. Consequently, the shared cerebrospinal-fluid/testis module may reflect shared immune or secretory cell populations, blood-derived material, tissue-interface biology, or sample composition rather than a conserved program intrinsic to the same cell type in both tissues. HPA protein detection is available for testis for several members, whereas the cerebrospinal-fluid entry has no matching HPA tissue protein-detection result.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair reaches the supplied STRING interaction threshold, and no STRING functional enrichment is reported. No hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not corroborated by known high-confidence physical or functional interactions in these resources. The network may capture coordinated abundance, common cellular origin, secretion, trafficking, or inflammatory context rather than a stable molecular complex. The strongest network connectivity is centered on ACE and LCN2, with CPVL linked to both, whereas CTSF and IGHG3 have more peripheral positions.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module can be described as a potentially novel co-abundance association, but it cannot be established as a new molecular mechanism from the supplied evidence. Its lack of STRING and hu.MAP support is compatible with novelty, yet absence from those databases alone does not demonstrate novelty. The lack of globally significant GO/KEGG enrichment and the strong secretory, immune, choroid-plexus, testis, and germ-cell composition signals provide an important alternative explanation: the association may arise from shared cell types, tissue interfaces, or variable blood and secreted-protein content. A claim of novelty would require replication, control for cell composition and sample contamination, and independent validation of the co-abundance relationships.

**Hypothesis.** Hypothesis: this shared module reflects coordinated abundance of secreted, vesicular, and immune-associated proteins at tissue interfaces, potentially linking choroid-plexus or testicular secretory environments with immune-cell or blood-derived material. ACE could represent peptide and vasoactive-factor processing, LCN2 could represent innate immune and iron-sequestration activity, CPVL and CTSF could represent proteolytic processing in vesicular or lysosomal compartments, and IGHG3 could mark immunoglobulin-producing cell contribution. This is a mechanistic hypothesis rather than an established pathway, because the module lacks globally significant enrichment, STRING interactions, and hu.MAP complex support.

### Important genes

#### ACE

- **Related proteins** (co-abundance neighbors): CPVL (0.92), IGHG3 (0.87), LCN2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: angiotensin I converting enzyme. This gene encodes an enzyme involved in blood pressure regulation and electrolyte balance. It catalyzes the conversion of angiotensin I into a physiologically active peptide angiotensin II. Angiotensin II is a potent vasopressor and aldosterone-stimulating peptide that controls blood pressure and fluid-electrolyte balance. This angiotensin converting enzyme (ACE) also inactivates the vasodilator p…
- **Diseases (Open Targets)**: hypertensive disorder (0.750); renal tubular dysgenesis of genetic origin (0.729); renal tubular dysgenesis (0.724); cardiovascular disorder (0.704); diabetic kidney disease (0.689)
- **Europe PMC papers**: 95248
- **Why important**: ACE is the most network-connected member and links the central portion of the module to CPVL, LCN2, and IGHG3. Its established function is enzymatic conversion of angiotensin I to angiotensin II and inactivation of bradykinin, with roles in blood-pressure and fluid-electrolyte regulation. HPA supports intestine and testis enhancement, late-spermatid association, memory-B-cell association, secretion to blood, and testis detection. Its substantial literature and disease associations involving hypertension, renal tubular dysgenesis, cardiovascular disease, and diabetic kidney disease make it the strongest functional anchor for the module.
- **Conclusion**: Established evidence supports ACE as a secreted or circulating peptide-processing enzyme with vascular, renal, and electrolyte-related biology. Its central network position supports coordinated abundance within this module, but does not establish direct interaction with the other proteins. A possible role in linking tissue-interface secretion to local peptide signaling is a hypothesis.

#### LCN2

- **Related proteins** (co-abundance neighbors): CTSF (0.93), ACE (0.83), CPVL (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lipocalin 2. This gene encodes a protein that belongs to the lipocalin family. Members of this family transport small hydrophobic molecules such as lipids, steroid hormones and retinoids. The protein encoded by this gene is a neutrophil gelatinase-associated lipocalin and plays a role in innate immunity by limiting bacterial growth as a result of sequestering iron-containing siderophores. The presence of this …
- **Diseases (Open Targets)**: psoriasis (0.124); type 2 diabetes mellitus (0.122); acute kidney injury (0.121); coronary artery disorder (0.121); neoplasm (0.120)
- **Europe PMC papers**: 11549
- **Why important**: LCN2 is also highly connected and links CTSF, ACE, and CPVL. It is a secreted lipocalin involved in innate defense through sequestration of iron-containing siderophores and is associated with acute-phase and oxidative-stress responses. HPA places it in bone marrow and several secretory epithelia and associates it with neutrophil-lineage and monocyte populations. Its disease and biomarker literature, including acute kidney injury and inflammatory or metabolic disease associations, makes it an important indicator of immune and secretory context.
- **Conclusion**: Established evidence supports LCN2 as an innate-immune and secreted stress-response protein. Its co-abundance with this module may reflect immune-cell or secretory-material contribution. A direct LCN2-centered proteolytic mechanism involving CTSF or CPVL is not established by the supplied interaction resources.

#### CPVL

- **Related proteins** (co-abundance neighbors): ACE (0.92), LCN2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carboxypeptidase vitellogenic like. The protein encoded by this gene is a carboxypeptidase and bears strong sequence similarity to serine carboxypeptidases. Carboxypeptidases are a large class of proteases that act to cleave a single amino acid from the carboxy termini of proteins or peptides. The exact function of this protein, however, has not been determined. [provided by RefSeq, Jan 2017].
- **Diseases (Open Targets)**: basal cell carcinoma (0.553); skin neoplasm (0.547); skin cancer (0.534); hypothyroidism (0.510); non-melanoma skin carcinoma (0.488)
- **Europe PMC papers**: 621
- **Why important**: CPVL connects the two most central network members, ACE and LCN2. It encodes a carboxypeptidase-like protein, although its precise function is unresolved. HPA associates it with choroid plexus and lymphoid tissue, as well as macrophage, dendritic-cell, Kupffer-cell, and Hofbauer-cell populations, and detects it in testis. Its comparatively limited literature makes it especially valuable as a potentially informative but undercharacterized component of the module.
- **Conclusion**: Established evidence supports CPVL as an intracellular or membrane-associated carboxypeptidase-like protein with immune and tissue-interface expression, while its exact biochemical role remains uncertain. Its bridging network position suggests coordinated abundance with ACE and LCN2. Any proposed role in shared peptide processing or vesicular immune biology remains a hypothesis.

#### CTSF

- **Related proteins** (co-abundance neighbors): LCN2 (0.93); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cathepsin F. Cathepsins are papain family cysteine proteinases that represent a major component of the lysosomal proteolytic system. Cathepsins generally contain a signal sequence, followed by a propeptide and then a catalytically active mature region. The very long (251 amino acid residues) proregion of the cathepsin F precursor contains a C-terminal domain similar to the pro-segment of cathepsin L-like enzym…
- **Diseases (Open Targets)**: neuronal ceroid lipofuscinosis 13 (0.803); adult neuronal ceroid lipofuscinosis (0.624); neuronal ceroid lipofuscinosis (0.506); hereditary disease (0.468); ceroid lipofuscinosis, neuronal, 6B (Kufs type) (0.380)
- **Europe PMC papers**: 1248
- **Why important**: CTSF is the lysosomal cysteine protease member of the module and is connected to LCN2. It has choroid-plexus tissue enhancement, association with early and late spermatid-related populations and late primary spermatocytes, vesicular localization, and testis detection. Its established disease associations with neuronal ceroid lipofuscinosis give it particular importance for interpreting a module detected in a cerebrospinal-fluid-related tissue context.
- **Conclusion**: Established evidence supports CTSF as a lysosomal protease involved in proteolysis, protein catabolism, and antigen processing. Its choroid-plexus and germ-cell annotations provide a plausible tissue bridge, but the module does not establish that CTSF activity drives the shared co-abundance pattern. A role in vesicular proteolytic processing alongside LCN2 is a hypothesis.

#### IGHG3

- **Related proteins** (co-abundance neighbors): ACE (0.87); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: immunoglobulin heavy constant gamma 3 (G3m marker)
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 2659
- **Why important**: IGHG3 is peripheral in the network but is compositionally informative because it is an immunoglobulin heavy constant gene associated with lymphoid tissue, plasma cells, and memory and naive B-cell populations. It provides the clearest evidence that the module may include immunoglobulin-producing or blood-derived material. Its literature is substantial, although the supplied disease-association resource does not provide an Open Targets association for this gene.
- **Conclusion**: Established evidence supports IGHG3 as an immunoglobulin component marking antibody-producing or B-cell-related material. Its presence favors a cell-composition or secreted-protein explanation for the shared module. It does not establish a direct biochemical relationship with ACE, and any proposed coordination with proteolytic or peptide-processing proteins remains a hypothesis.

## Module 6

**Tissue pair**: cerebrospinal_fluid and testis  
**Genes (14)**: AMBP, SERPINC1, CFB, CFI, COL18A1, AHSG, GPX3, IGFBP7, KNG1, PROS1, PTPRF, SPARC, TIMP2, VTN

### Function

The most defensible functional interpretation is a secreted extracellular homeostasis module linking complement regulation, coagulation and anticoagulation, protease inhibition, extracellular-matrix adhesion, vascular or stromal signaling, and protection from oxidative damage. This interpretation is supported by the gene-level annotations for CFB, CFI, KNG1, SERPINC1, PROS1, VTN, SPARC, COL18A1, GPX3, and TIMP2, and by the dense STRING relationships among AHSG, AMBP, KNG1, SERPINC1, VTN, CFB, CFI, SPARC, and COL18A1. No GO/KEGG term passed global correction; therefore, no pathway is claimed as significantly enriched. The absence of a globally significant term does not invalidate the module, especially because the genes represent several related extracellular systems rather than a single narrowly defined pathway.

**Cell composition.** Composition is the strongest caution in interpreting this shared module. Every module gene is annotated by HPA as secreted either to blood or to extracellular matrix, apart from PTPRF, which is intracellular and membrane-associated. The HPA pattern is dominated by liver and hepatocyte associations, while many genes are not detected in immune cells. This is consistent with a plasma-protein or blood-derived signal in cerebrospinal fluid and possibly in testis samples, rather than expression by a common specialized cell type in both tissues. The presence of choroid-plexus and ependymal associations for PROS1, vascular or stromal associations for SPARC, IGFBP7, and COL18A1, and testis protein detection for several genes leaves open a genuine local blood-interface, vascular, stromal, or barrier contribution. However, the shared module should first be treated as an extracellular-fluid and tissue-interface signature, with possible contribution from blood contamination or vascular permeability.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides known, biologically coherent relationships rather than an unexplained interaction cluster. The strongest links include complement factor B with complement factor I, AHSG with KNG1, AMBP, and SERPINC1, SERPINC1 with VTN, and SPARC with VTN. KNG1, VTN, AHSG, and SERPINC1 form a particularly coherent plasma protease, coagulation, and adhesion neighborhood. hu.MAP independently places CFB, KNG1, AHSG, and GPX3 together in several complexes, places CFB with GPX3 in additional complexes, and places AMBP with CFI in additional complexes. These repeated overlaps support a real biochemical or co-fractionating extracellular community, but they do not establish that all module edges are direct physical interactions. The lack of STRING functional enrichment is supplementary and does not override the known pairwise relationships or the hu.MAP evidence.

**STRING interactions (score >= 0.7)**: 15 of 91 gene pairs: AHSG–AMBP (0.932); AHSG–KNG1 (0.936); AHSG–SERPINC1 (0.838); AHSG–VTN (0.782); AMBP–SERPINC1 (0.936); AMBP–VTN (0.737); CFB–CFI (0.97); COL18A1–SPARC (0.757); COL18A1–VTN (0.752); IGFBP7–TIMP2 (0.874); KNG1–SERPINC1 (0.758); KNG1–VTN (0.803); PROS1–SERPINC1 (0.743); SERPINC1–VTN (0.949); SPARC–VTN (0.922)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08395.1 (CFB, KNG1, AHSG, GPX3; 4/43); huMAP3_09531.1 (CFB, KNG1, AHSG, GPX3; 4/47); huMAP3_10101.1 (CFB, KNG1, AHSG, GPX3; 4/49); huMAP3_15040.1 (CFB, SERPINC1, KNG1, AHSG; 4/64); huMAP3_10678.1 (CFB, KNG1, AHSG, GPX3; 4/71); huMAP3_07701.1 (CFB, KNG1, GPX3; 3/22); huMAP3_09273.1 (CFB, KNG1, GPX3; 3/28); huMAP3_14445.1 (AMBP, CFI; 2/18); huMAP3_07541.1 (KNG1, GPX3; 2/19); huMAP3_07265.1 (KNG1, AHSG; 2/20); huMAP3_14656.1 (AMBP, CFI; 2/21)

### Novelty

The shared co-abundance observation may be novel as a tissue-pair result, but the underlying biology is not newly discovered by this module. Several edges are already supported by STRING, and recurrent hu.MAP overlaps show that many members belong to established plasma-protein and complement-associated complexes. The module therefore should not be described as a newly discovered molecular complex or pathway. Its potentially novel aspect is the coordinated abundance of this extracellular protein assemblage across cerebrospinal fluid and testis, particularly if that cross-tissue relationship has not previously been reported. Demonstrating novelty would require comparison with prior cerebrospinal-fluid, testis, plasma-contamination, and blood-brain-barrier co-abundance studies, together with independent validation and controls for sample leakage.

**Hypothesis.** Hypothesis: this module reflects a shared extracellular-fluid and barrier-interface program in which liver-derived plasma proteins enter or are sampled in cerebrospinal fluid and testis-associated fluid or vasculature, where complement activation is restrained by CFI, coagulation is balanced by SERPINC1 and PROS1, kinin and protease processes are represented by KNG1 and AMBP, and VTN, SPARC, IGFBP7, COL18A1, and TIMP2 organize adhesion, matrix remodeling, and vascular or stromal signaling. GPX3 may provide extracellular oxidative protection. This hypothesis predicts that the shared signal will track vascular or barrier permeability, plasma admixture, or extracellular matrix state more strongly than the identity of a unique cell population. It requires testing with matched plasma controls, measures of blood contamination, cell- or compartment-resolved data, and independent protein-level validation.

### Important genes

#### AHSG

- **Related proteins** (co-abundance neighbors): CFI (0.88), IGFBP7 (0.88), VTN (0.85), SPARC (0.85), KNG1 (0.83), CFB (0.82), PROS1 (0.82); STRING partners: AMBP (0.932), KNG1 (0.936), SERPINC1 (0.838), VTN (0.782)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07265.1
- **Function (MyGene.info)**: alpha 2-HS glycoprotein. The protein encoded by this gene is a negatively-charged serum glycoprotein that is synthesized by hepatocytes. The encoded protein consists of two polypeptide chains, which are both cleaved from a proprotein encoded from a single mRNA. It is involved in several processes, including endocytosis, brain development, and the formation of bone tissue. Defects in this gene are a cause of susceptibility…
- **Diseases (Open Targets)**: alopecia - intellectual disability syndrome (0.476); otosclerosis (0.465); nephrolithiasis, calcium oxalate (0.417); calcium oxalate urolithiasis (0.416); neurodegenerative disease (0.204)
- **Europe PMC papers**: 2310
- **Why important**: AHSG is the most central module node by weighted connectivity and links complement-related, coagulation-related, and extracellular proteins including KNG1, SERPINC1, VTN, CFB, CFI, SPARC, IGFBP7, and PROS1. HPA assigns it to liver and hepatocytes and to the blood secretome, while the gene-level annotation supports acute-phase, endocytic, and mineralization-related functions. It has extensive literature and disease connections, making it a strong anchor for distinguishing a plasma-derived module from a tissue-specific signaling module.
- **Conclusion**: Established evidence supports AHSG as a liver-derived secreted hub that can organize the observed plasma protein signature. The hypothesis that it is a functional regulator of the shared cerebrospinal-fluid and testis signal remains unproven; it may instead be a high-abundance carrier or correlated source marker.

#### VTN

- **Related proteins** (co-abundance neighbors): KNG1 (0.88), CFB (0.88), AHSG (0.85), AMBP (0.80), SPARC (0.80); STRING partners: AHSG (0.782), AMBP (0.737), COL18A1 (0.752), KNG1 (0.803), SERPINC1 (0.949), SPARC (0.922)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vitronectin. The protein encoded by this gene functions in part as an adhesive glycoprotein. Differential expression of this protein can promote either cell adhesion or migration as it links cells to the extracellular matrix through a variety of ligands. These ligands include integrins, plasminogen activator inhibitor-1, and urokinase plasminogen activator receptor. This secreted protein can be present in the …
- **Diseases (Open Targets)**: hypertensive disorder (0.421); dengue disease (0.376); neurodegenerative disease (0.343); temporal arteritis (0.338); age-related macular degeneration (0.313)
- **Europe PMC papers**: 3940
- **Why important**: VTN is a highly connected extracellular node linking KNG1, CFB, AHSG, AMBP, SERPINC1, COL18A1, and SPARC. Its established functions include cell adhesion, cell-matrix adhesion, integrin signaling, and interaction with fibrinolytic-system components. HPA identifies it as liver-associated and secreted to blood, and its strong STRING relationships place it at the interface between plasma protease regulation and extracellular matrix biology. Its literature and disease associations provide substantial context for interpreting the module as an adhesion and vascular-interface signature.
- **Conclusion**: Established evidence supports VTN as a plausible extracellular scaffold or carrier connecting the plasma and matrix parts of the module. It is not established that VTN drives the cross-tissue co-abundance; the co-abundance could reflect shared exposure to circulating VTN.

#### CFB

- **Related proteins** (co-abundance neighbors): SERPINC1 (0.92), VTN (0.88), KNG1 (0.82), AHSG (0.82); STRING partners: CFI (0.97)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07701.1, huMAP3_09273.1
- **Function (MyGene.info)**: complement factor B. This gene encodes complement factor B, a component of the alternative pathway of complement activation. Factor B circulates in the blood as a single chain polypeptide. Upon activation of the alternative pathway, it is cleaved by complement factor D yielding the noncatalytic chain Ba and the catalytic subunit Bb. The active subunit Bb is a serine protease which associates with C3b to form the alter…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with B factor anomaly (0.764); atypical hemolytic-uremic syndrome (0.705); Immunodeficiency due to a complement cascade protein anomaly (0.614); paroxysmal nocturnal hemoglobinuria (0.561); complement 3 glomerulopathy (0.546)
- **Europe PMC papers**: 7226
- **Why important**: CFB is a complement alternative-pathway component, occupies a central position among the complement-related module genes, and connects directly in STRING to CFI, SERPINC1, VTN, KNG1, and AHSG. It is liver-enriched, secreted to blood, and represented with CFI and other module members in several hu.MAP complexes. Its disease associations with complement dysregulation make it important for assessing whether the module reflects controlled innate immune activity rather than generic plasma abundance.
- **Conclusion**: Established evidence supports CFB as a complement-related component of the module, with CFI providing a counterbalancing regulatory context. A locally activated complement pathway in either tissue is only a hypothesis, because the HPA pattern is predominantly hepatic and plasma-associated and no global enrichment was detected.

#### CFI

- **Related proteins** (co-abundance neighbors): AHSG (0.88), IGFBP7 (0.86), PROS1 (0.81); STRING partners: CFB (0.97)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_14445.1, huMAP3_14656.1
- **Function (MyGene.info)**: complement factor I. This gene encodes a serine proteinase that is essential for regulating the complement cascade. The encoded preproprotein is cleaved to produce both heavy and light chains, which are linked by disulfide bonds to form a heterodimeric glycoprotein. This heterodimer can cleave and inactivate the complement components C4b and C3b, and it prevents the assembly of the C3 and C5 convertase enzymes. Defect…
- **Diseases (Open Targets)**: complement factor I deficiency (0.798); atypical hemolytic-uremic syndrome with I factor anomaly (0.795); age-related macular degeneration (0.782); atypical hemolytic-uremic syndrome (0.639); macular degeneration (0.571)
- **Europe PMC papers**: 14453
- **Why important**: CFI is a complement regulatory serine protease that inactivates C three b and C four b and prevents formation of complement convertases. It connects to CFB, AHSG, IGFBP7, and PROS1 in the module and forms known hu.MAP associations with AMBP. Its strong disease links to complement factor I deficiency, atypical hemolytic-uremic syndrome, and macular degeneration make it a mechanistically informative node despite its more modest network degree.
- **Conclusion**: Established evidence supports CFI as evidence for complement regulation rather than unrestrained complement activation. Whether its abundance indicates active complement control at the cerebrospinal-fluid or testis interface remains a hypothesis requiring functional measurements.

#### SPARC

- **Related proteins** (co-abundance neighbors): PROS1 (0.87), PTPRF (0.86), IGFBP7 (0.85), AHSG (0.85), COL18A1 (0.84), VTN (0.80); STRING partners: COL18A1 (0.757), VTN (0.922)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: secreted protein acidic and cysteine rich. This gene encodes a cysteine-rich acidic matrix-associated protein. The encoded protein is required for the collagen in bone to become calcified but is also involved in extracellular matrix synthesis and promotion of changes to cell shape. The gene product has been associated with tumor suppression but has also been correlated with metastasis based on changes to cell shape which can promote tumor …
- **Diseases (Open Targets)**: osteogenesis imperfecta (0.707); neurodegenerative disease (0.443); hereditary disease (0.414); osteogenesis imperfecta type 4 (0.381); Abnormality of the skeletal system (0.358)
- **Europe PMC papers**: 17798
- **Why important**: SPARC is a highly connected secreted extracellular-matrix node linked to VTN, COL18A1, AHSG, IGFBP7, PROS1, and PTPRF. HPA reports stromal, hepatic-stellate, vascular, and testis detection patterns, while the gene-level annotation supports matrix synthesis, cell-shape regulation, endothelial migration, angiogenesis regulation, and synapse organization. Its very large literature base and disease associations make it a strong candidate for interpreting the module's matrix, vascular, and tissue-interface component.
- **Conclusion**: Established evidence supports SPARC as a matrix and vascular-interface component that could connect circulating proteins to local tissue structure. A shared SPARC-mediated mechanism across cerebrospinal fluid and testis is plausible but not demonstrated by co-abundance alone.

## Module 8

**Tissue pair**: cerebrospinal_fluid and testis  
**Genes (5)**: CPD, CFH, FGB, FGG, MFGE8

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established pathway assignment from GO/KEGG enrichment. Its biological signal is instead consistent with extracellular blood-protein biology: FGB and FGG are fibrinogen chains involved in coagulation, platelet activation, cell-matrix adhesion and fibrinolysis; CFH regulates the alternative complement pathway; MFGE8 promotes clearance of apoptotic cells; and CPD is a regulatory carboxypeptidase involved in proteolysis and protein processing. The network is therefore most plausibly a plasma-associated coagulation, complement-regulation and tissue remodelling signal rather than a narrowly defined intracellular pathway. This interpretation is biologically coherent but remains an inference because neither GO/KEGG nor STRING functional enrichment provides globally corrected support.

**Cell composition.** The module is strongly biased toward secreted or plasma-associated proteins. FGB, FGG, CFH and MFGE8 are secreted to blood according to HPA, while CPD is a cytosolic protein with low tissue specificity. FGB, FGG and CFH show liver or hepatocyte enrichment, and MFGE8 is enriched in blood-vessel-associated tissue and stromal or perivascular cell types. CPD has neutrophil association, while several other module proteins show immune-cell enhancement. HPA detects CFH in testis and detects CPD there, but does not detect FGB, FGG or MFGE8 there; the CSF protein-detection comparison has no matching HPA data. Thus the shared CSF–testis module may reflect circulating plasma proteins, vascular leakage, or shared stromal and immune context rather than a testis- and CSF-specific program. The absence of GO/KEGG enrichment does not invalidate the module, but it argues against overinterpreting it as a discrete tissue pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING directly supports the FGB–FGG relationship, which is expected because the proteins are fibrinogen subunits. No STRING partners are reported for CPD, CFH or MFGE8 within the supplied evidence, and STRING functional enrichment is absent. hu.MAP independently places FGB and FGG together across complexes (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_10101.1). CFH joins FGB and FGG in (hu.MAP huMAP3_15040.1) and (hu.MAP huMAP3_10678.1), but those complexes contain broad collections of plasma, complement, coagulation, apolipoprotein and acute-phase proteins. This supports a known extracellular plasma-protein neighborhood, while the repeated FGB–FGG association is partly driven by their established biochemical partnership. The hu.MAP evidence does not establish that all module members form one physical complex, and CPD and MFGE8 lack reported hu.MAP or STRING relationships here.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: FGB–FGG (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (FGB, FGG, CFH; 3/64); huMAP3_10678.1 (FGB, FGG, CFH; 3/71); huMAP3_09434.1 (FGB, FGG; 2/33); huMAP3_08395.1 (FGB, FGG; 2/43); huMAP3_09531.1 (FGB, FGG; 2/47); huMAP3_10101.1 (FGB, FGG; 2/49)

### Novelty

The exact conserved co-abundance module could represent a new observation, particularly because the supplied STRING and hu.MAP evidence does not provide a complete relationship map for CPD and MFGE8. However, the main biological components are not novel individually: fibrinogen, complement regulation, apoptotic-cell clearance and plasma proteolysis are established processes, and FGB–FGG is a well-known molecular partnership. Absence of a complete match in STRING or hu.MAP cannot demonstrate novelty, because those resources capture physical or curated relationships rather than every co-abundance pattern. The most defensible conclusion is that this is a potentially novel cross-tissue co-abundance configuration built largely from known circulating proteins, requiring replication, assessment of blood contamination and comparison with independent CSF and testis datasets before being called a new tissue mechanism.

**Hypothesis.** Mechanistic hypothesis: variation in a circulating extracellular-protein milieu links the two tissues. Fibrinogen represented by FGB and FGG may mark coagulation and vascular-interface activity; CFH may constrain complement activation; MFGE8 may promote removal of apoptotic material and influence stromal or vascular remodelling; and CPD may process extracellular or secretory proteins and connect the other components at the co-abundance level. In CSF and testis, the apparent conservation may therefore arise from shared vascular, stromal or immune interfaces, or from blood-derived protein carryover, rather than coordinated expression by the same resident cell type. This is a hypothesis, not an experimentally demonstrated mechanism.

### Important genes

#### FGB

- **Related proteins** (co-abundance neighbors): CPD (0.90), FGG (0.81); STRING partners: FGG (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1
- **Function (MyGene.info)**: fibrinogen beta chain. The protein encoded by this gene is the beta component of fibrinogen, a blood-borne glycoprotein comprised of three pairs of nonidentical polypeptide chains. Following vascular injury, fibrinogen is cleaved by thrombin to form fibrin which is the most abundant component of blood clots. In addition, various cleavage products of fibrinogen and fibrin regulate cell adhesion and spreading, display vas…
- **Diseases (Open Targets)**: congenital afibrinogenemia (0.786); familial dysfibrinogenemia (0.705); congenital fibrinogen deficiency (0.622); familial hypodysfibrinogenemia (0.597); cancer (0.592)
- **Europe PMC papers**: 4215
- **Why important**: FGB is a central network connector linking FGG and CPD, has direct STRING support with FGG, and recurs in the hu.MAP complexes (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_10101.1). It is a liver- and hepatocyte- enriched secreted blood protein with established roles in fibrin formation, coagulation, platelet activation, cell-matrix adhesion and fibrinolysis. Its disease associations include inherited fibrinogen disorders and cancer, and it has substantial literature support.
- **Conclusion**: Established conclusion: FGB is the clearest marker of a circulating fibrinogen and coagulation component in this module. Hypothesis: its co-abundance may report vascular interface or plasma exposure in the sampled tissues rather than local production.

#### FGG

- **Related proteins** (co-abundance neighbors): FGB (0.81); STRING partners: FGB (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1
- **Function (MyGene.info)**: fibrinogen gamma chain. The protein encoded by this gene is the gamma component of fibrinogen, a blood-borne glycoprotein comprised of three pairs of nonidentical polypeptide chains. Following vascular injury, fibrinogen is cleaved by thrombin to form fibrin which is the most abundant component of blood clots. In addition, various cleavage products of fibrinogen and fibrin regulate cell adhesion and spreading, display va…
- **Diseases (Open Targets)**: familial dysfibrinogenemia (0.787); congenital afibrinogenemia (0.753); congenital fibrinogen deficiency (0.617); familial hypodysfibrinogenemia (0.597); cancer (0.596)
- **Europe PMC papers**: 4006
- **Why important**: FGG is directly connected to FGB by STRING and is repeatedly represented with FGB in hu.MAP complexes (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_10101.1). It is a liver- and hepatocyte-enriched secreted fibrinogen chain involved in coagulation, platelet activation, cell-matrix adhesion and fibrinolysis. It has strong disease relevance through familial and congenital fibrinogen disorders and substantial literature support.
- **Conclusion**: Established conclusion: FGG reinforces that the module contains the canonical fibrinogen signal rather than an isolated, poorly characterized protein association. Hypothesis: the FGB–FGG pair may be a stable plasma-protein anchor around which the remaining co-abundance relationships are organized.

#### CFH

- **Related proteins** (co-abundance neighbors): CPD (0.92); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1
- **Function (MyGene.info)**: complement factor H. This gene is a member of the Regulator of Complement Activation (RCA) gene cluster and encodes a protein with twenty short consensus repeat (SCR) domains. This protein is secreted into the bloodstream and has an essential role in the regulation of complement activation, restricting this innate defense mechanism to microbial infections. Mutations in this gene have been associated with hemolytic-ure…
- **Diseases (Open Targets)**: complement factor H deficiency (0.769); age-related macular degeneration (0.750); atypical hemolytic-uremic syndrome (0.729); age related macular degeneration 4 (0.711); Doyne honeycomb retinal dystrophy (0.688)
- **Europe PMC papers**: 9287
- **Why important**: CFH connects to CPD in the co-abundance network and joins FGB and FGG in hu.MAP complexes (hu.MAP huMAP3_15040.1) and (hu.MAP huMAP3_10678.1). It is a liver-enriched secreted regulator of complement activation, with additional relevance to inflammation, neurogenesis and central nervous system myelination. Its disease associations include complement factor H deficiency, atypical hemolytic uremic syndrome and retinal degeneration, and it has extensive literature support.
- **Conclusion**: Established conclusion: CFH supplies a credible complement-regulatory dimension to the plasma-protein interpretation. Hypothesis: CFH may couple vascular or blood-derived complement control to tissue-interface biology in CSF and testis.

#### MFGE8

- **Related proteins** (co-abundance neighbors): CPD (0.89); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: milk fat globule EGF and factor V/VIII domain containing. This gene encodes a preproprotein that is proteolytically processed to form multiple protein products. The major encoded protein product, lactadherin, is a membrane glycoprotein that promotes phagocytosis of apoptotic cells. This protein has also been implicated in wound healing, autoimmune disease, and cancer. Lactadherin can be further processed to form a smaller cleavage product, medin, which c…
- **Diseases (Open Targets)**: AL amyloidosis (0.462); angina pectoris (0.339); myocardial ischemia (0.333); coronary artery bypass (0.314); coronary atherosclerosis (0.312)
- **Europe PMC papers**: 2623
- **Why important**: MFGE8 is connected to CPD and is enriched in blood-vessel-associated tissue and stromal or perivascular cell types. Its established function in apoptotic-cell clearance, together with roles in wound healing, autoimmune disease and vascular pathology, gives it a plausible tissue-remodelling interpretation even though it lacks reported STRING or hu.MAP support in this module. It has substantial literature and associations with amyloidosis, ischemic and coronary disease.
- **Conclusion**: Established conclusion: MFGE8 is the strongest candidate for an apoptotic-cell-clearance or vascular-remodelling component. Hypothesis: its association with CPD may reflect shared stromal, vascular or secretory activity rather than a validated physical complex.

#### CPD

- **Related proteins** (co-abundance neighbors): CFH (0.92), FGB (0.90), MFGE8 (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enhanced; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carboxypeptidase D. The metallocarboxypeptidase family of enzymes is divided into 2 subfamilies based on sequence similarities. The pancreatic carboxypeptidase-like and the regulatory B-type carboxypeptidase subfamilies. Carboxypeptidase D has been identified as a regulatory B-type carboxypeptidase. CPD is a homolog of duck gp180, a hepatitis B virus-binding protein. Transcript variants utilizing alternative polyaden…
- **Diseases (Open Targets)**: neurodegenerative disease (0.348); autoimmune disorder of central nervous system (0.274); mental disorder (0.270); estrogen-receptor positive breast cancer (0.257); Graves disease (0.213)
- **Europe PMC papers**: 13682
- **Why important**: CPD has the highest network connectivity in the module and links CFH, FGB and MFGE8, despite having no reported STRING partners or hu.MAP membership here. Its annotated roles in proteolysis, peptide metabolism and protein processing provide a possible processing-related bridge between the secreted proteins. It is associated with neurodegenerative, central nervous system autoimmune and mental disorders and has extensive literature support.
- **Conclusion**: Established conclusion: CPD is the network-level connector and provides a plausible protein-processing interpretation, but its module relationships are not independently validated by the supplied interaction resources. Hypothesis: CPD may coordinate or reflect processing of proteins in a vascular, secretory or tissue-interface milieu.
