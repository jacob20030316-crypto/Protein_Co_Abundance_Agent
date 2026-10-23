# Conserved co-abundance modules: cerebrospinal_fluid and stem_cells

## Module 0

**Tissue pair**: cerebrospinal_fluid and stem_cells  
**Genes (25)**: SLC3A2, GOT1, ALDOC, HSPA5, CEMIP, COL1A2, COL6A1, COL6A3, CSPG4, CXADR, FN1, SERPINE2, GSN, LAMA5, LAMB1, MFGE8, IGF2R, PCDH1, PCOLCE, HSPG2, PTPRF, PTPRS, SELENBP1, SOD2, SPARC

### Function

The module most plausibly represents extracellular-matrix and basement-membrane organization, with linked cell adhesion, cell–matrix signaling, migration, and tissue structural support. This interpretation is driven by the coordinated presence of collagens, laminins, fibronectin, perlecan, SPARC, PCOLCE, and cell-surface adhesion or phosphatase proteins, together with the dense STRING connections among these proteins. The module also contains genes related to actin remodeling, proteolysis, oxidative stress, metabolism, and receptor trafficking, suggesting an extracellular structural core with associated cellular-response components. No GO or KEGG term passed global correction, so this functional interpretation is based on the gene annotations and network structure rather than on globally significant pathway enrichment. The shared appearance in cerebrospinal fluid and stem cells may reflect a conserved stromal, vascular, perivascular, or matrix-producing cellular program rather than a tissue-exclusive pathway.

**Cell composition.** The module is strongly enriched in secreted or extracellular-matrix proteins, including FN1, COL1A2, COL6A1, COL6A3, LAMA5, LAMB1, HSPG2, SPARC, PCOLCE, MFGE8, and SERPINE2. HPA supports a stromal and vascular interpretation: fibroblasts are the most recurrent enhanced cell type, with additional signals in decidual stromal cells, hepatic stellate cells, pericytes, vascular cells, and trophoblast-related populations. Several genes are enhanced in blood vessels, placenta, smooth muscle, or heart muscle. Most module genes are not detected in immune cells, although a minority show neutrophil or other immune-cell enhancement. Thus, the module does not look primarily like a blood-cell module, but its abundance in cerebrospinal-fluid samples could still reflect vascular or stromal material, extracellular vesicles, barrier-associated cells, or sample composition. The secreted nature of much of the module also means that co-abundance need not imply that all genes are expressed by the same cell.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides substantial support for a known extracellular-matrix interaction backbone. Particularly coherent relationships include collagen connections involving COL1A2, COL6A1, and COL6A3; laminin connections involving LAMA5 and LAMB1; and links from FN1 to collagen, laminin, HSPG2, SPARC, and GSN. HSPG2 is connected to FN1, LAMB1, SPARC, and CSPG4, consistent with basement-membrane and cell-surface organization. These are largely established molecular relationships and indicate that the module captures a biologically meaningful matrix network rather than an arbitrary gene list. hu.MAP adds a different type of support: SOD2 and GOT1 occur together in C1, while PTPRF and PTPRS occur together in C2 and C3. The PTPRF–PTPRS recurrence suggests a possible receptor-signaling or adhesion-associated substructure, but the complexes contain only a small subset of the module members and therefore do not establish one unified complex. The absence of STRING enrichment and the lack of broad hu.MAP coverage should not be interpreted as evidence against the module.

**STRING interactions (score >= 0.7)**: 20 of 300 gene pairs: COL1A2–COL6A1 (0.875); COL1A2–COL6A3 (0.968); COL1A2–FN1 (0.982); COL1A2–LAMA5 (0.761); COL1A2–PCOLCE (0.963); COL1A2–SPARC (0.959); COL6A1–COL6A3 (0.994); COL6A1–FN1 (0.78); COL6A1–LAMB1 (0.843); COL6A1–PCOLCE (0.779); COL6A3–FN1 (0.736); COL6A3–LAMB1 (0.76); CSPG4–HSPG2 (0.735); FN1–GSN (0.809); FN1–HSPG2 (0.996); FN1–LAMA5 (0.79); FN1–SPARC (0.969); HSPG2–LAMB1 (0.782); HSPG2–SPARC (0.733); LAMA5–LAMB1 (0.998)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14822.1 (SOD2, GOT1; 2/6); huMAP3_11149.1 (PTPRF, PTPRS; 2/32); huMAP3_11605.1 (PTPRF, PTPRS; 2/64)

### Novelty

The module may be a new observation as a conserved co-abundance pattern across cerebrospinal fluid and stem cells, but the underlying biology is not wholly novel. Many of its central relationships are already represented in STRING, especially the collagen–fibronectin–laminin–perlecan matrix backbone, and the individual genes have substantial prior literature and disease annotation. Conversely, the lack of a globally corrected GO or KEGG term, the absence of STRING functional enrichment, and the limited overlap with hu.MAP mean that the precise cross-tissue co-abundance configuration is not fully explained by existing pathway or complex resources. A defensible conclusion is that the module is potentially novel at the level of tissue-pair co-abundance and network assembly, not a demonstration of a previously unknown molecular function. Replication in independent cerebrospinal-fluid and stem-cell datasets, together with cell-type-aware analyses and protein-level validation, would be needed to establish novelty.

**Hypothesis.** Hypothesis: a conserved matrix-producing or matrix-associated cellular program contributes to this module in both tissue groups. Coordinated production of collagen, laminin, fibronectin, and perlecan could organize a basement-membrane-like scaffold, while SPARC and PCOLCE could modify matrix assembly and collagen maturation. CSPG4, PTPRF, PTPRS, CXADR, and PCDH1 could connect that scaffold to cell-surface adhesion and signaling, and CEMIP or SERPINE2 could influence extracellular-matrix turnover and protease control. GSN may couple extracellular or membrane-associated signals to actin remodeling, while SOD2, GOT1, and ALDOC may reflect oxidative and metabolic adaptation of the contributing cells. In cerebrospinal fluid, the signal could arise from barrier-associated, vascular, perivascular, or extracellular-vesicle material; in stem cells, it could reflect a shared differentiation or stromal-support state. This remains a mechanistic hypothesis rather than an established conclusion from the co-abundance data.

### Important genes

#### FN1

- **Related proteins** (co-abundance neighbors): LAMA5 (0.94), SOD2 (0.92); STRING partners: COL1A2 (0.982), COL6A1 (0.78), COL6A3 (0.736), GSN (0.809), HSPG2 (0.996), LAMA5 (0.79), SPARC (0.969)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 is a central connector within the matrix portion of the module and has STRING relationships with collagen, laminin, HSPG2, SPARC, and GSN. Its established functions include cell adhesion, cell–matrix adhesion, migration, embryogenesis, wound healing, and integrin-mediated signaling. HPA places it in blood vessels, liver, and placenta and in fibroblast, hepatic-stellate, and trophoblast-related cell types. It also has the largest literature volume among the listed genes and strong disease associations, making it the clearest anchor for interpreting the module.
- **Conclusion**: Established evidence supports FN1 as a major extracellular scaffold and signaling organizer in this module. The hypothesis that FN1 coordinates the shared cerebrospinal-fluid and stem-cell co-abundance state is plausible but is not proven by the present data.

#### COL1A2

- **Related proteins** (co-abundance neighbors): COL6A1 (0.89), PCOLCE (0.84); STRING partners: COL6A1 (0.875), COL6A3 (0.968), FN1 (0.982), LAMA5 (0.761), PCOLCE (0.963), SPARC (0.959)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type I alpha 2 chain. This gene encodes the pro-alpha2 chain of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIB, recessive Ehlers-Danlos syndrome Classi…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 2 (0.845); osteogenesis imperfecta type 3 (0.830); osteogenesis imperfecta type 4 (0.820); Ehlers-Danlos syndrome, cardiac valvular type (0.777); osteogenesis imperfecta type 1 (0.770)
- **Europe PMC papers**: 67901
- **Why important**: COL1A2 links the module to fibrillar collagen production and has strong STRING relationships with COL6A1, COL6A3, FN1, LAMA5, PCOLCE, and SPARC. Its HPA pattern emphasizes stromal and connective-tissue populations, including decidual stromal cells, endometrial stromal cells, and fibro-adipogenic progenitors. It has well-established structural functions and extensive disease associations involving osteogenesis imperfecta and connective-tissue disorders.
- **Conclusion**: Established evidence identifies COL1A2 as a structural matrix component and a strong indicator of fibroblast-like or stromal matrix production. It supports a matrix interpretation of the module, but does not by itself establish that collagen is produced locally in both sampled materials.

#### LAMA5

- **Related proteins** (co-abundance neighbors): FN1 (0.94), LAMB1 (0.94), HSPG2 (0.92), COL6A1 (0.91); STRING partners: COL1A2 (0.761), FN1 (0.79), LAMB1 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit alpha 5. This gene encodes one of the vertebrate laminin alpha chains. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins are composed of 3 non identical chains: l…
- **Diseases (Open Targets)**: nephrotic syndrome, IIa 26 (0.761); bent bone dysplasia syndrome 2 (0.563); colorectal cancer (0.491); LAMA5-related multisystemic syndrome (0.475); polyp of colon (0.467)
- **Europe PMC papers**: 2881
- **Why important**: LAMA5 is among the most connected module genes and forms a coherent basement-membrane interaction set with FN1, LAMB1, HSPG2, and COL6A1 in STRING. Laminin alpha five is a major noncollagenous basement-membrane constituent involved in adhesion, migration, differentiation, and integrin-mediated signaling. HPA detects enhanced expression in several epithelial and vascular-interface cell types, including podocytes and trophoblast-related populations.
- **Conclusion**: Established evidence supports LAMA5 as a basement-membrane organizer that can connect matrix structure to cellular signaling. Its presence is consistent with barrier-associated or stromal biology, while any specific role in stem-cell state maintenance or cerebrospinal-fluid biology remains a hypothesis.

#### HSPG2

- **Related proteins** (co-abundance neighbors): LAMA5 (0.92), COL6A3 (0.82); STRING partners: CSPG4 (0.735), FN1 (0.996), LAMB1 (0.782), SPARC (0.733)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 encodes perlecan, a multidomain extracellular proteoglycan that cross-links matrix and cell-surface molecules. It connects in STRING with FN1, LAMB1, SPARC, and CSPG4, placing it at the interface of basement-membrane architecture and signaling. HPA supports vascular, adipose, alveolar, trophoblast, and hepatic-stellate associations, and its annotations include brain development, cell differentiation, and regulation of angiogenesis.
- **Conclusion**: Established evidence supports HSPG2 as a plausible structural and signaling hub within the extracellular-matrix backbone. A possible contribution to vascular-barrier or neural-interface properties in cerebrospinal fluid is mechanistically reasonable, but it is not demonstrated by this module alone.

#### PTPRF

- **Related proteins** (co-abundance neighbors): CEMIP (0.90), CSPG4 (0.90), SERPINE2 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11149.1, huMAP3_11605.1
- **Function (MyGene.info)**: protein tyrosine phosphatase receptor type F. The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP possesses an extracellular region, a single transmembrane region, and two tandem intracytoplasmic catalytic domains, and thu…
- **Diseases (Open Targets)**: breasts and/or nipples, aplasia or hypoplasia of, 2 (0.505); smoking initiation (0.420); attention deficit-hyperactivity disorder (0.419); isolated congenital breast hypoplasia/aplasia (0.370); substance-related disorder (0.329)
- **Europe PMC papers**: 4709
- **Why important**: PTPRF is a receptor-type protein tyrosine phosphatase with extracellular, transmembrane, and intracellular catalytic regions. It occupies a connective position with CSPG4, CEMIP, and SERPINE2 in the module and is represented with PTPRS in both hu.MAP complexes C2 and C3. Its established functions include cell adhesion, migration, receptor phosphatase signaling, and nervous-system development, while HPA shows enhanced expression in extravillous trophoblasts and goblet cells.
- **Conclusion**: Established evidence supports PTPRF as a candidate membrane signaling bridge between extracellular matrix and intracellular tyrosine-phosphorylation control. Its repeated hu.MAP pairing with PTPRS strengthens the existence of a receptor-signaling substructure, but the proposed bridge between matrix organization and stem-cell or cerebrospinal-fluid state is still a hypothesis.

## Module 1

**Tissue pair**: cerebrospinal_fluid and stem_cells  
**Genes (35)**: APP, ANPEP, ASAH1, ASPH, ATP1B1, CDH2, CPD, CD47, COL12A1, VCAN, ENDOD1, EXTL2, FBN1, FTH1, FUCA2, FUCA1, GPNMB, SERPINB1, LAMA4, LAMB2, LAMC1, MINPP1, MCAM, NAGA, OLFML3, PLXNA3, PLXNB2, CTSA, PTPRK, PVR, ROBO1, SEMA4C, SORT1, SPINT2, VGF

### Function

No GO or KEGG term passed global correction, so there is no statistically supported pathway label for this module from the primary enrichment analysis. The gene composition nevertheless points to a mixed extracellular-interface and intracellular-processing program. The strongest biological pattern is extracellular-matrix organization, basement-membrane and cell-adhesion biology, semaphorin and plexin-related guidance, vesicular trafficking, and lysosomal or glycan processing. FBN1, COL12A1, LAMC1, LAMA4, LAMB2, VCAN, OLFML3, MCAM, ROBO1, SEMA4C, PLXNB2, and PLXNA3 support an extracellular matrix, vascular, stromal, and guidance interpretation. NAGA, CPD, CTSA, ASAH1, FUCA1, FUCA2, and EXTL2 support lysosomal, proteolytic, sphingolipid, fucose, and glycoconjugate processing. VGF and APP provide a neurosecretory or neural-interface component, while PTPRK, CDH2, PVR, and CD47 support cell-contact and signaling roles. Because no globally significant GO/KEGG term exists, these are gene-level and network-level interpretations rather than globally corrected enrichment claims. The module is therefore best described as a heterogeneous extracellular-cell-interface and trafficking module, potentially combining matrix, vascular, neural-interface, and myeloid-associated biology.

**Cell composition.** Most of the module is compatible with secreted, extracellular-matrix, membrane, vesicular, or cell-surface biology, and the HPA summary identifies many secreted genes. HPA profiles prominently implicate fibroblasts, adipocytes, vascular-associated cells, trophoblast-related cells, neutrophils, monocytes, dendritic cells, and Hofbauer cells. Several genes are specifically associated with immune or myeloid populations, including NAGA, PLXNB2, PVR, GPNMB, VCAN, ANPEP, and APP, whereas FBN1, COL12A1, LAMC1, LAMA4, OLFML3, MCAM, and VCAN support stromal or vascular extracellular-matrix biology. This makes biological cell composition an important alternative explanation: the shared signal between cerebrospinal fluid and stem cells could reflect secreted proteins, extracellular vesicles, vascular or stromal material, or shared myeloid contamination rather than a lineage-specific stem-cell or cerebrospinal-fluid mechanism. The module is not uniformly blood-cell specific, since many genes are not detected in immune cells or have low immune specificity. HPA provides no matching tissue-level protein-detection data for either named sample group, so direct protein localization in these samples cannot be inferred.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a limited set of high-confidence known relationships rather than a coherent enriched interaction system. Established links include APP with SORT1, FBN1 with VCAN and LAMC1, COL12A1 with LAMC1, FUCA1 with FUCA2, laminin-chain relationships among LAMA4, LAMB2, and LAMC1, LAMA4 with MCAM, and PLXNB2 with SEMA4C. These links independently support matrix assembly, glycan processing, receptor trafficking, and semaphorin signaling, but they account for only part of the co-abundance structure. There is no STRING functional-enrichment result. hu.MAP adds a lysosomal or glycan-processing complex represented by PLXNB2, NAGA, LAMB2, and FUCA2 in (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). MCAM and LAMA4 recur across several hu.MAP complexes in (hu.MAP huMAP3_03825.1) through (hu.MAP huMAP3_12563.1), LAMC1 and LAMA4 co-occur in (hu.MAP huMAP3_14233.1), and VCAN with MINPP1 occurs in (hu.MAP huMAP3_15307.1). The repeated MCAM-laminin and PLXNB2-NAGA-LAMB2-FUCA2 relationships indicate that some parts of the module recapitulate known protein complexes. However, many module edges have no corresponding STRING or hu.MAP relationship, so the full co-abundance module should not be equated with a single physical complex. Co-abundance may reflect shared cell origin, secretion, trafficking, or coordinated regulation.

**STRING interactions (score >= 0.7)**: 10 of 595 gene pairs: APP–SORT1 (0.883); COL12A1–LAMC1 (0.721); FBN1–LAMC1 (0.72); FBN1–VCAN (0.91); FUCA1–FUCA2 (0.928); LAMA4–LAMB2 (0.93); LAMA4–LAMC1 (0.98); LAMA4–MCAM (0.961); LAMB2–LAMC1 (0.962); PLXNB2–SEMA4C (0.996)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (PLXNB2, NAGA, LAMB2, FUCA2; 4/60); huMAP3_09327.1 (PLXNB2, NAGA, LAMB2, FUCA2; 4/93); huMAP3_03825.1 (MCAM, LAMA4; 2/2); huMAP3_10163.1 (MCAM, LAMA4; 2/3); huMAP3_10902.1 (MCAM, LAMA4; 2/4); huMAP3_10056.1 (MCAM, LAMA4; 2/5); huMAP3_12563.1 (MCAM, LAMA4; 2/7); huMAP3_14233.1 (LAMC1, LAMA4; 2/14); huMAP3_15307.1 (VCAN, MINPP1; 2/22)

### Novelty

The complete module should be regarded as a potentially new cross-tissue co-abundance pattern, but not as a newly discovered molecular complex or proven pathway. The rationale for possible novelty is that the module combines extracellular matrix proteins, guidance receptors, lysosomal glycan enzymes, secreted neuroendocrine proteins, and immune-associated proteins in a module shared by cerebrospinal fluid and stem cells, while only selected subrelationships are represented in STRING and hu.MAP. The absence of a STRING or hu.MAP relationship for many pairs does not prove novelty, because those resources emphasize physical interactions and curated complexes rather than tissue-pair-specific co-abundance. A novelty claim would require replication in independent cerebrospinal-fluid and stem-cell datasets, control for cell-type composition and plasma carryover, and comparison with published coexpression modules. At present, the defensible conclusion is that the integrated module-level pattern may be novel, whereas several of its component biological relationships are established.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of extracellular-matrix and basement-membrane material together with vesicular and lysosomal processing machinery at a vascular, stromal, neural-interface, or myeloid boundary. In this model, laminins, fibrillin, collagen-associated proteins, versican, and OLFML3 provide an extracellular scaffold; MCAM, PTPRK, ROBO1, plexins, semaphorin signaling, PVR, CDH2, and CD47 couple that scaffold to cell adhesion, migration, and guidance; and NAGA, CPD, CTSA, ASAH1, FUCA1, FUCA2, and EXTL2 process membrane or extracellular glycoconjugates. APP, VGF, and SORT1 could connect this interface to neurosecretory cargo and endosomal trafficking. The shared cerebrospinal-fluid and stem-cell signal may therefore arise from a common extracellular-vesicle or vascular-interface biology, or from shared stromal and myeloid material, rather than from a dedicated stem-cell program. This is a testable hypothesis, not an established causal mechanism.

### Important genes

#### FBN1

- **Related proteins** (co-abundance neighbors): COL12A1 (0.99), VGF (0.98), SEMA4C (0.98), ASAH1 (0.95), GPNMB (0.94), SORT1 (0.94), ANPEP (0.94), ROBO1 (0.93), PTPRK (0.92), FTH1 (0.92), PLXNB2 (0.90), LAMC1 (0.90), NAGA (0.88), CPD (0.87), CD47 (0.84), CTSA (0.84), FUCA1 (0.81), MINPP1 (0.81); STRING partners: LAMC1 (0.72), VCAN (0.91)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibrillin 1. This gene encodes a member of the fibrillin family of proteins. The encoded preproprotein is proteolytically processed to generate two proteins including the extracellular matrix component fibrillin-1 and the protein hormone asprosin. Fibrillin-1 is an extracellular matrix glycoprotein that serves as a structural component of calcium-binding microfibrils. These microfibrils provide force-bearing s…
- **Diseases (Open Targets)**: Marfan syndrome (0.892); ectopia lentis 1, isolated, autosomal dominant (0.811); Acromicric dysplasia (0.802); geleophysic dysplasia 2 (0.802); stiff skin syndrome (0.799)
- **Europe PMC papers**: 9216
- **Why important**: FBN1 is the strongest network hub in the supplied module and connects matrix, guidance, trafficking, and immune-associated neighbors. Its HPA profile supports adipose, placental, fibroblast, and stromal biology, and it is secreted to blood. Its established function as fibrillin-one, a structural component of calcium-binding microfibrils, gives the module a plausible extracellular-scaffold anchor. The STRING links to VCAN and LAMC1 and its association with Marfan syndrome and related connective-tissue disorders make it biologically and clinically informative. Its extensive literature makes it a well-established anchor rather than a speculative marker.
- **Conclusion**: Established: FBN1 is a central extracellular-matrix gene with strong network connectivity, relevant tissue and cell-type associations, known matrix function, and established connective-tissue disease links. Hypothesis: FBN1 may organize or report the extracellular scaffold underlying the shared module. The co-abundance data do not establish that FBN1 causally drives the other genes.

#### LAMC1

- **Related proteins** (co-abundance neighbors): VGF (0.94), MCAM (0.92), COL12A1 (0.91), FBN1 (0.90), GPNMB (0.88), CD47 (0.88), ROBO1 (0.87); STRING partners: COL12A1 (0.721), FBN1 (0.72), LAMA4 (0.98), LAMB2 (0.962)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14233.1
- **Function (MyGene.info)**: laminin subunit gamma 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: Fuchs' endothelial dystrophy (0.487); prostate carcinoma (0.467); colorectal cancer (0.447); eye disorder (0.434); benign colon neoplasm (0.427)
- **Europe PMC papers**: 4227
- **Why important**: LAMC1 is a highly connected laminin component that links FBN1, COL12A1, LAMA4, LAMB2, MCAM, VGF, CD47, and ROBO1. HPA places it in extracellular matrix and plasma-membrane-associated compartments and in fibroblast, adipose-related, and pituicyte or folliculostellate cell contexts. STRING supports its relationships with multiple laminin chains and matrix proteins, while hu.MAP supports its occurrence with LAMA4 in (hu.MAP huMAP3_14233.1). Laminins have established roles in adhesion, migration, differentiation, signaling, and neurite outgrowth, making LAMC1 a strong bridge between matrix and neural-interface interpretations.
- **Conclusion**: Established: LAMC1 is a basement-membrane and cell-adhesion component supported by both network structure and known laminin relationships. Hypothesis: LAMC1 may be a physical extracellular scaffold that helps explain the module's shared signal across fluid and stem-cell contexts. The module does not demonstrate a new LAMC1 complex.

#### OLFML3

- **Related proteins** (co-abundance neighbors): FTH1 (0.98), ASAH1 (0.93), ATP1B1 (0.93), CPD (0.90), SPINT2 (0.90), SEMA4C (0.90), APP (0.89), PTPRK (0.88), SORT1 (0.88), MINPP1 (0.87), VCAN (0.82), CDH2 (0.81), NAGA (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: olfactomedin like 3. This gene encodes a member of the olfactomedin-like gene family which also includes genes encoding noelin, tiarin, myocilin, amassin, optimedin, photomedin, and latrophilin. The encoded protein is a secreted extracellular matrix glycoprotein with a C-terminal olfactomedin domain that facilitates protein-protein interactions, cell adhesion, and intercellular interactions. It serves as both a scaffo…
- **Diseases (Open Targets)**: Familial prostate cancer (0.111); prostate cancer (0.111); neoplasm (0.094); glioblastoma (0.094); central nervous system cancer (0.078)
- **Europe PMC papers**: 930
- **Why important**: OLFML3 is a well-connected secreted extracellular-matrix glycoprotein associated in HPA with fibroblasts, stromal cells, hepatic stellate cells, microglia, and myeloid dendritic cells. It links matrix and signaling genes including FTH1, ASAH1, CPD, SPINT2, SEMA4C, APP, and PTPRK. Its annotated olfactomedin domain supports protein-protein interaction, cell adhesion, and intercellular-interaction functions, and its reported role as a scaffold for BMP-related extracellular processing is compatible with a matrix-interface interpretation. Its disease and literature associations are more limited than those of FBN1 or APP, which makes it especially useful as a candidate module-specific mediator rather than as a universally established driver.
- **Conclusion**: Established: OLFML3 is a secreted extracellular-matrix interaction protein with stromal and microglial or myeloid associations and substantial network connectivity. Hypothesis: OLFML3 may help couple matrix organization to local signaling or immune-interface biology in this module. Causality and relevance to cerebrospinal fluid remain unproven.

#### NAGA

- **Related proteins** (co-abundance neighbors): GPNMB (0.98), CPD (0.98), VGF (0.93), PVR (0.92), ROBO1 (0.88), FBN1 (0.88), COL12A1 (0.87), LAMB2 (0.87), ASAH1 (0.86), SEMA4C (0.83), FUCA2 (0.82), PLXNA3 (0.82), OLFML3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: alpha-N-acetylgalactosaminidase. NAGA encodes the lysosomal enzyme alpha-N-acetylgalactosaminidase, which cleaves alpha-N-acetylgalactosaminyl moieties from glycoconjugates. Mutations in NAGA have been identified as the cause of  Schindler disease types I and II (type II also known as Kanzaki disease). [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: alpha-N-acetylgalactosaminidase deficiency type 2 (0.803); alpha-N-acetylgalactosaminidase deficiency (0.759); alpha-N-acetylgalactosaminidase deficiency type 1 (0.752); alpha-N-acetylgalactosaminidase deficiency type 3 (0.603); hereditary disease (0.415)
- **Europe PMC papers**: 4236
- **Why important**: NAGA is a central processing-related node connected to CPD, GPNMB, VGF, PVR, ROBO1, FBN1, COL12A1, and LAMB2. It is enriched in monocyte-related and Hofbauer or macrophage-like contexts in HPA and encodes a lysosomal enzyme that removes alpha-linked N-acetylgalactosaminyl residues from glycoconjugates. NAGA is present with PLXNB2, LAMB2, and FUCA2 in the hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Its established association with Schindler disease types supports the biological importance of glycoconjugate degradation, while its position connects that process to extracellular and membrane biology.
- **Conclusion**: Established: NAGA is a lysosomal glycoconjugate-processing enzyme supported by hu.MAP membership, network centrality, myeloid-associated expression, and disease evidence. Hypothesis: NAGA may mark coordinated lysosomal or extracellular-glycan turnover within the shared module. The data do not show whether this reflects active glycan remodeling or merely shared abundance from particular cell types.

#### APP

- **Related proteins** (co-abundance neighbors): FUCA2 (0.93), VGF (0.92), OLFML3 (0.89), MINPP1 (0.87), COL12A1 (0.86); STRING partners: SORT1 (0.883)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: amyloid beta precursor protein. This gene encodes a cell surface receptor and transmembrane precursor protein that is cleaved by secretases to form a number of peptides. Some of these peptides are secreted and can bind to the acetyltransferase complex APBB1/TIP60 to promote transcriptional activation, while others form the protein basis of the amyloid plaques found in the brains of patients with Alzheimer disease. In addition, t…
- **Diseases (Open Targets)**: Alzheimer disease (0.815); Alzheimer disease type 1 (0.788); cerebral amyloid angiopathy, APP-related (0.754); dementia (0.698); Hereditary cerebral hemorrhage with amyloidosis (0.633)
- **Europe PMC papers**: 83189
- **Why important**: APP is a highly studied secreted or membrane-associated precursor with a distinctive connection to VGF, OLFML3, MINPP1, COL12A1, FUCA2, and SORT1. HPA associates it with secreted blood material and plasmacytoid dendritic cells, while its established biology includes secretase processing, trafficking, microglial and astrocyte immune responses, and Alzheimer disease associations. The STRING APP-SORT1 relationship provides a known trafficking link, and VGF provides a neurosecretory context. APP therefore helps distinguish a possible neural-interface or vesicular component from a purely stromal module.
- **Conclusion**: Established: APP is a well-characterized trafficking and proteolytic-processing precursor with neural and immune relevance, and its relationship with SORT1 is supported by STRING. Hypothesis: APP may represent neurosecretory or endosomal cargo biology shared with the extracellular-matrix and myeloid components. The module does not establish an Alzheimer-related mechanism.

## Module 2

**Tissue pair**: cerebrospinal_fluid and stem_cells  
**Genes (9)**: DBI, BTD, CTSC, COL1A1, FBLN1, GSTP1, LDHB, MAN1A1, SEMA6A

### Function

The module does not support a single established pathway-level function. No GO or KEGG term passed global multiple-testing correction, and there were no supplementary STRING enrichment terms. The gene set instead combines Golgi glycoprotein processing through MAN1A1, extracellular-matrix biology through COL1A1 and FBLN1, neural development and axon guidance through SEMA6A, lipid metabolism through DBI, redox and xenobiotic handling through GSTP1, lactate metabolism through LDHB, lysosomal proteolysis and immune-cell proteinase activation through CTSC, and biotin recycling through BTD. MAN1A1 is the principal network connector, linking glycoprotein processing with SEMA6A, DBI, CTSC, and LDHB, while the remaining relationships form small local pairs. The most defensible interpretation is therefore a mixed co-abundance program involving secretory or extracellular-matrix biology, cellular metabolism, and tissue or cell-composition effects rather than a demonstrated common molecular pathway.

**Cell composition.** The module is strongly tissue- and cell-type-associated rather than uniformly housekeeping-like. HPA annotations emphasize liver, brain, choroid plexus, reproductive or stromal tissues, heart, kidney, and esophageal tissues, with many genes showing cell-type-enhanced expression. FBLN1 and COL1A1 are extracellular-matrix secreted proteins, and BTD is secreted to blood; CTSC has intracellular and membrane localization. The module includes stromal, choroid-plexus epithelial, hepatocyte-associated, epithelial, hematopoietic, macrophage, and plasma-cell annotations, while most genes have low immune-cell specificity or are not detected in immune cells. This argues against a simple blood-cell module, although the circulating nature of BTD and the presence of tissue- and cell-type-restricted proteins mean that sample composition, barrier-associated cells, stromal cells, or shared cellular contaminants could contribute substantially to the cerebrospinal-fluid and stem-cell co-abundance signal. HPA provides no matching protein-detection evidence for either sampled tissue category, so it cannot establish that the proteins are directly produced in those samples.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, no STRING functional-enrichment result was reported, and no hu.MAP complex contained multiple module members. Thus the observed co-abundance edges are not corroborated here as established physical interactions or membership in a known multiprotein complex. Known biochemical functions still provide biological context: MAN1A1 is a Golgi mannosidase, COL1A1 and FBLN1 are extracellular-matrix proteins, CTSC is a lysosomal cysteine protease, and the other enzymes have established metabolic or detoxification roles. The absence of STRING and hu.MAP support makes the module look more like a coordinated expression or abundance signature than a previously characterized protein complex.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel cross-tissue co-abundance association, because the supplied network connects genes with diverse established functions and is not represented by a detected STRING interaction network or shared hu.MAP complex. However, those absences do not prove novelty: the individual genes and their functions are well established, and several genes have substantial literature and disease annotation. The appropriate claim is novelty of the specific cerebrospinal-fluid and stem-cell co-abundance pattern, pending independent replication, control for tissue and cell composition, and comparison with published co-abundance modules. It should not be described as a newly discovered pathway or molecular complex.

**Hypothesis.** Hypothesis: the module reflects a shared tissue-interface or cellular-composition state in which choroid-plexus, stromal, epithelial, hepatic-like, or stem-cell-associated populations contribute extracellular-matrix and secreted proteins while simultaneously exhibiting coordinated glycoprotein processing, lipid handling, redox defense, and intermediary metabolism. MAN1A1 could mark secretory-pathway and glycoprotein-processing activity; FBLN1 and COL1A1 could represent matrix-producing or barrier-associated cells; SEMA6A could connect the signal to neural or developmental tissue context; and BTD, DBI, GSTP1, and LDHB could reflect circulating or metabolic state. CTSC could indicate a minor myeloid or protease-related component. This is a composition and state hypothesis, not evidence of direct physical cooperation or causality.

### Important genes

#### MAN1A1

- **Related proteins** (co-abundance neighbors): SEMA6A (0.98), DBI (0.91), CTSC (0.88), LDHB (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosidase alpha class 1A member 1. This gene encodes a class I mammalian Golgi 1,2-mannosidase which is a type II transmembrane protein. This protein catalyzes the hydrolysis of three terminal mannose residues from peptide-bound Man(9)-GlcNAc(2) oligosaccharides and belongs to family 47 of glycosyl hydrolases. [provided by RefSeq, Jul 2012].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.368); nervous system benign neoplasm (0.353); smoking initiation (0.311); eye disorder (0.292); hypertrophic cardiomyopathy (0.280)
- **Europe PMC papers**: 645
- **Why important**: MAN1A1 is the central network connector and has the strongest apparent connectivity in the module. Its established Golgi mannosidase function links the co-abundance pattern to N-glycan mannose trimming, protein targeting, and glycoprotein quality control. HPA associates it with liver and several hematopoietic or immune-related cell types, while the literature and disease annotation are substantial.
- **Conclusion**: Established evidence supports MAN1A1 as the best network anchor and as a marker of Golgi glycoprotein processing. It is plausible that it helps reflect secretory-pathway activity, but the data do not establish that MAN1A1 drives the module or directly interacts with its neighbors.

#### COL1A1

- **Related proteins** (co-abundance neighbors): BTD (0.92), DBI (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type I alpha 1 chain. This gene encodes the pro-alpha1 chains of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIA, Ehlers-Danlos syndrome Classical type,…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 2 (0.847); osteogenesis imperfecta type 4 (0.837); osteogenesis imperfecta type 3 (0.835); osteogenesis imperfecta type 1 (0.834); osteogenesis imperfecta (0.808)
- **Europe PMC papers**: 45548
- **Why important**: COL1A1 is a prominent extracellular-matrix component with strong disease and literature support. Its HPA pattern points to stromal, fibroblast, hepatic-stellate, and reproductive-tissue contexts, and its module connection to BTD and DBI places matrix biology beside metabolic and secreted-protein signals. It provides a clear explanation for why cell composition could influence the module.
- **Conclusion**: Established evidence supports COL1A1 as a marker of matrix-producing stromal or connective-tissue contribution and as a biologically important disease gene. Its presence does not demonstrate a cerebrospinal-fluid structural program; a stromal or contaminating-cell explanation remains a serious alternative.

#### FBLN1

- **Related proteins** (co-abundance neighbors): SEMA6A (0.98); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibulin 1. Fibulin 1 is a secreted glycoprotein that becomes incorporated into a fibrillar extracellular matrix. Calcium-binding is apparently required to mediate its binding to laminin and nidogen. It mediates platelet adhesion via binding fibrinogen. Four splice variants which differ in the 3' end have been identified. Each variant encodes a different isoform, but no functional distinctions have been ident…
- **Diseases (Open Targets)**: synpolydactyly type 2 (0.447); FBLN1-related developmental delay-central nervous system anomaly-syndactyly syndrome (0.377); synpolydactyly (0.371); adolescent idiopathic scoliosis (0.306); alcohol drinking (0.219)
- **Europe PMC papers**: 2655
- **Why important**: FBLN1 is a secreted extracellular-matrix glycoprotein and the module’s link to SEMA6A. Its tissue annotation includes choroid plexus, and its cell-type annotations include choroid-plexus epithelial and stromal populations. That combination makes it particularly informative for the cerebrospinal-fluid side of the shared signal.
- **Conclusion**: Established evidence supports FBLN1 as an extracellular-matrix and choroid-plexus-associated marker. It is a plausible indicator of barrier or stromal-cell contribution, but the network does not establish a functional FBLN1–SEMA6A interaction or a causal role in the shared module.

#### SEMA6A

- **Related proteins** (co-abundance neighbors): FBLN1 (0.98), MAN1A1 (0.98); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: semaphorin 6A. The transmembrane semaphorin SEMA6A is expressed in developing neural tissue and is required for proper development of the thalamocortical projection (Leighton et al., 2001 [PubMed 11242070]).[supplied by OMIM, Feb 2011]
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); bipolar disorder (0.323); abscess (0.311); cellulitis (0.310); stomach disorder (0.293)
- **Europe PMC papers**: 1601
- **Why important**: SEMA6A is connected to MAN1A1 and FBLN1 and has established roles in neural development, axon guidance, cytoskeletal organization, and cell-surface signaling. HPA associates it with brain and several specialized cell types. Its inclusion gives the module a neural or developmental component that is relevant to cerebrospinal-fluid biology.
- **Conclusion**: Established evidence supports SEMA6A as a neural-development and guidance-related marker. A neural-interface interpretation is possible, but the co-abundance data alone cannot distinguish neural biology from shared tissue or cell-type composition.

#### BTD

- **Related proteins** (co-abundance neighbors): COL1A1 (0.92), GSTP1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biotinidase. The protein encoded by this gene functions to recycle protein-bound biotin by cleaving biocytin (biotin-epsilon-lysine), a normal product of carboxylase degradation, resulting in regeneration of free biotin. The encoded protein has also been shown to have biotinyl transferase activity. Mutations in this gene are associated with biotinidase deficiency. Multiple transcript variants encoding differen…
- **Diseases (Open Targets)**: biotinidase deficiency (0.840); hereditary disease (0.539); inborn vitamin metabolic disorder (0.462); Leber hereditary optic neuropathy (0.379); optic atrophy (0.371)
- **Europe PMC papers**: 2220
- **Why important**: BTD connects COL1A1 with GSTP1 and encodes the enzyme responsible for recycling protein-bound biotin. It is tissue-enhanced in liver, appears in several specialized cell types, and is secreted to blood. Its disease association with biotinidase deficiency is well established, making it informative for both metabolic interpretation and possible circulating-protein contribution.
- **Conclusion**: Established evidence supports BTD as a biotin-recycling enzyme and blood-secreted protein. In this module it may report metabolic or secreted-protein state, but it also raises the possibility that sample handling or circulating protein contribution contributes to the shared abundance pattern.

## Module 3

**Tissue pair**: cerebrospinal_fluid and stem_cells  
**Genes (26)**: ADAM10, SMPDL3B, GLB1, CADM1, CPVL, DSG2, EXTL3, FSTL1, GNS, GOLM1, HEXA, ICAM1, DGCR2, LGMN, LRIG1, LRRN1, PLTP, PRNP, CRABP1, FAP, SUMF1, SV2A, THY1, TPBG, TF, KDR

### Function

No GO or KEGG term passed global multiple-testing correction, and STRING functional enrichment was absent. Therefore, the module does not support a formally established pathway-level annotation from enrichment analysis. Its gene-level evidence is nevertheless consistent with a composite interface involving cell adhesion and cell-surface communication, lysosomal and endosomal proteolysis, glycosaminoglycan and glycolipid processing, membrane trafficking, vascular or stromal interactions, and neuronal or choroid-plexus biology. This interpretation is supported by the functions of FAP, ICAM1, SV2A, LGMN, EXTL3, SUMF1, HEXA, GNS, and related genes, but it should be treated as a functional synthesis rather than a globally significant enrichment result.

**Cell composition.** The module is heterogeneous rather than a clean tissue-specific program. Many members are broadly expressed or have low tissue specificity, while several are secreted to blood, including FAP, TF, FSTL1, PLTP, and SMPDL3B. HPA also shows recurring associations with neutrophils, basophils, monocytes, dendritic cells, Kupffer cells, Hofbauer cells, and other immune or myeloid populations. Other members are associated with brain, retina, choroid plexus, Müller glia, astrocytes, neurons, or vascular and stromal cells. This mixture raises the possibility that the shared signal partly reflects blood or immune-cell content, extracellular proteins, or common cell types present across the cerebrospinal-fluid and stem-cell samples. The presence of SV2A, LRRN1, THY1, CADM1, and choroid-plexus-associated genes also leaves open a genuine neural or barrier-interface component. HPA provides no matching tissue-level protein-detection result for either named sample group, so it cannot directly establish protein abundance in these samples.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a small set of already known relationships rather than a densely documented interaction system. The strongest connected group is the lysosomal and glycan-processing set GLB1, GNS, and HEXA, with SUMF1 also linked to GNS. STRING also reports the CADM1–ICAM1 relationship. These known interactions support a lysosomal catabolism component and a cell-adhesion component, but most module pairs lack high-confidence STRING support; consequently, the co-abundance edges should not be interpreted as direct physical interactions. hu.MAP provides additional complex-level context. ADAM10, SUMF1, and LGMN co-occur in complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), while GNS and SUMF1 co-occur in (hu.MAP huMAP3_10485.1). Because only a subset of members occurs in each large complex, these results support shared molecular neighborhoods or compartmental association rather than proof that the full module is one complex.

**STRING interactions (score >= 0.7)**: 5 of 325 gene pairs: CADM1–ICAM1 (0.773); GLB1–GNS (0.957); GLB1–HEXA (0.959); GNS–HEXA (0.936); GNS–SUMF1 (0.802)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (ADAM10, SUMF1, LGMN; 3/60); huMAP3_09327.1 (ADAM10, SUMF1, LGMN; 3/93); huMAP3_10485.1 (GNS, SUMF1; 2/7)

### Novelty

The module may represent a previously unreported co-abundance pattern, but the available evidence is insufficient to call it a new biological mechanism. Its combination of lysosomal enzymes, adhesion molecules, secreted proteins, neural markers, and immune-associated genes is distinctive at the module level, and most of its co-abundance relationships are not represented as high-confidence STRING interactions or hu.MAP complexes. However, absence from those resources does not establish novelty: databases are incomplete, co-abundance is not equivalent to physical interaction, and the module may reflect sample composition or shared cellular contamination. The strongest defensible conclusion is that this is a potentially novel cross-tissue co-abundance signature whose biological novelty requires independent replication, cell-composition adjustment, and experimental validation.

**Hypothesis.** Hypothesis: the module captures a shared extracellular and endolysosomal interface linking stromal or vascular adhesion, immune-cell interaction, glycosaminoglycan remodeling, and neural or choroid-plexus-associated membrane biology. In this model, FAP, ICAM1, CADM1, and THY1 mark or mediate cell-contact and matrix-associated states; ADAM10 and LGMN contribute membrane or endosomal proteolysis; SUMF1 enables maturation of lysosomal sulfatases; and HEXA, GNS, and GLB1 support degradation of complex glycans and glycolipids. Secreted proteins such as TF, FSTL1, PLTP, and FAP could make the signal visible in cerebrospinal fluid, while immune-associated expression could make it sensitive to blood or myeloid-cell content. SV2A, PRNP, LRRN1, and choroid-plexus-associated expression suggest a neural or barrier-interface contribution, but this part remains hypothetical and may instead reflect mixed cellular composition.

### Important genes

#### FAP

- **Related proteins** (co-abundance neighbors): THY1 (0.99), TF (0.99), LGMN (0.98), PRNP (0.98), CADM1 (0.97), FSTL1 (0.97), ICAM1 (0.97), GOLM1 (0.95), SUMF1 (0.92), EXTL3 (0.90), SV2A (0.87), KDR (0.85), CPVL (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibroblast activation protein alpha. The protein encoded by this gene is a homodimeric integral membrane gelatinase belonging to the serine protease family. It is selectively expressed in reactive stromal fibroblasts of epithelial cancers, granulation tissue of healing wounds, and malignant cells of bone and soft tissue sarcomas. This protein is thought to be involved in the control of fibroblast growth or epithelial-mesenchymal inte…
- **Diseases (Open Targets)**: inflammatory bowel disease (0.311); hypothyroidism (0.306); irritable bowel syndrome (0.290); autoimmune disease (0.288); psoriasis (0.261)
- **Europe PMC papers**: 22775
- **Why important**: FAP is a leading network hub and connects strongly with adhesion, stromal, neural-associated, and lysosomal members including THY1, TF, LGMN, PRNP, CADM1, FSTL1, and ICAM1. HPA identifies it as secreted to blood and associated with stromal and Müller-glia populations. Its established biology as a membrane gelatinase involved in fibroblast growth, tissue repair, extracellular-matrix turnover, and epithelial–mesenchymal interactions makes it a strong candidate for an extracellular or stromal component. It also has substantial literature and disease-association support.
- **Conclusion**: Established evidence supports FAP as a central extracellular-matrix and stromal-associated marker with a prominent network position. Its participation in a cerebrospinal-fluid and stem-cell module may indicate a shared reactive stromal or matrix state, but a direct causal role in this module is a hypothesis.

#### ICAM1

- **Related proteins** (co-abundance neighbors): FSTL1 (0.99), PRNP (0.98), FAP (0.97), CADM1 (0.97), GOLM1 (0.96), TF (0.96), EXTL3 (0.95), SV2A (0.93), THY1 (0.93), LGMN (0.92), SUMF1 (0.90), CPVL (0.84), ADAM10 (0.81); STRING partners: CADM1 (0.773)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: intercellular adhesion molecule 1. This gene encodes a cell surface glycoprotein which is typically expressed on endothelial cells and cells of the immune system. It binds to integrins of type CD11a / CD18, or CD11b / CD18 and is also exploited by Rhinovirus as a receptor. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.528); atrial fibrillation (0.407); vascular disorder (0.358); Crohn disease (0.340); lymphatic system disorder (0.285)
- **Europe PMC papers**: 19543
- **Why important**: ICAM1 is among the strongest network hubs and connects FAP, CADM1, FSTL1, PRNP, TF, EXTL3, and SV2A. HPA places it at the plasma membrane and associates it with endothelial, macrophage, monocyte, and Kupffer-cell populations. Its established functions in cell adhesion, leukocyte extravasation, immune effector processes, and antigen-presenting-cell contact provide a clear explanation for an immune or vascular-interface signal. CADM1–ICAM1 is also an explicitly supported STRING relationship, and ICAM1 has extensive literature and disease associations.
- **Conclusion**: Established evidence supports ICAM1 as a cell-contact and immune-interface component of the module. It is also a plausible indicator of blood or myeloid-cell contribution, so its co-abundance should not be interpreted as proof of a neural mechanism.

#### SV2A

- **Related proteins** (co-abundance neighbors): KDR (0.99), CADM1 (0.98), GLB1 (0.94), CPVL (0.94), ICAM1 (0.93), FSTL1 (0.89), FAP (0.87), SMPDL3B (0.87), SUMF1 (0.82), EXTL3 (0.81), GNS (0.81), HEXA (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: synaptic vesicle glycoprotein 2A. The protein encoded by this gene is one of three related synaptic vesicle proteins. The encoded protein may interact with synaptotagmin to enhance low frequency neurotransmission in quiescent neurons. [provided by RefSeq, Jun 2016].
- **Diseases (Open Targets)**: epilepsy (0.627); Seizure (0.608); Bilateral tonic-clonic seizure (0.603); botulism (0.578); neurodegenerative disease (0.550)
- **Europe PMC papers**: 2018
- **Why important**: SV2A has a strong network position and links neural-associated members with lysosomal, adhesion, and immune-associated genes. HPA shows brain enhancement and specificity for excitatory neurons, inhibitory neurons, and other neural cell types, while the gene is established as a synaptic-vesicle glycoprotein involved in neurotransmission and vesicle biology. Its epilepsy and seizure associations and substantial literature make it biologically informative for interpreting the neural side of the module.
- **Conclusion**: Established evidence supports SV2A as a neuronal synaptic-vesicle marker. Its presence suggests that at least part of the shared signal may involve neural or neural-adjacent material, but the mixed HPA profile means it could also mark cell composition rather than a coordinated module mechanism.

#### LGMN

- **Related proteins** (co-abundance neighbors): DGCR2 (0.98), FAP (0.98), CADM1 (0.97), PRNP (0.92), ICAM1 (0.92), SUMF1 (0.91), EXTL3 (0.89), TF (0.87), PLTP (0.85), LRIG1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: legumain. This gene encodes a cysteine protease that has a strict specificity for hydrolysis of asparaginyl bonds. This enzyme may be involved in the processing of bacterial peptides and endogenous proteins for MHC class II presentation in the lysosomal/endosomal systems. Enzyme activation is triggered by acidic pH and appears to be autocatalytic. Protein expression occurs after monocytes differentiate into…
- **Diseases (Open Targets)**: crush injury (0.329); Alzheimer disease (0.216); post term pregnancy (0.207); rosacea (0.194); neoplasm (0.113)
- **Europe PMC papers**: 1700
- **Why important**: LGMN is a central network member and participates in both hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1) with ADAM10 and SUMF1. HPA associates it with macrophage, Kupffer-cell, Hofbauer-cell, and other cell types, and places it in vesicular or intracellular and membrane compartments. Its established role as an acidic cysteine protease in endosomal and lysosomal protein processing and MHC class two peptide processing connects the module to immune and degradative biology. It also has disease associations involving injury, Alzheimer disease, and neoplasia.
- **Conclusion**: Established evidence supports LGMN as a lysosomal or endosomal proteolysis component that may connect immune-cell biology with extracellular or membrane remodeling. Its centrality and complex membership make it a strong mechanistic candidate, although the module data do not show that LGMN drives the co-abundance pattern.

#### SUMF1

- **Related proteins** (co-abundance neighbors): PRNP (0.96), FSTL1 (0.93), FAP (0.92), LGMN (0.91), ICAM1 (0.90), CADM1 (0.90), CPVL (0.86), SV2A (0.82); STRING partners: GNS (0.802)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1, huMAP3_10485.1
- **Function (MyGene.info)**: sulfatase modifying factor 1. This gene encodes an enzyme that catalyzes the hydrolysis of sulfate esters by oxidizing a cysteine residue in the substrate sulfatase to an active site 3-oxoalanine residue, which is also known as C-alpha-formylglycine. Mutations in this gene cause multiple sulfatase deficiency, a lysosomal storage disorder. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 20…
- **Diseases (Open Targets)**: mucosulfatidosis (0.853); spinocerebellar ataxia type 15/16 (0.417); inherited retinal dystrophy (0.372); hereditary disease (0.341); alcohol drinking (0.311)
- **Europe PMC papers**: 764
- **Why important**: SUMF1 connects to several high-ranking module members and is the only member represented in all three reported hu.MAP complexes (hu.MAP huMAP3_06775.1), (hu.MAP huMAP3_09327.1), and (hu.MAP huMAP3_10485.1). It has a STRING relationship with GNS, and its established function is activation of sulfatases through post-translational modification. This places it upstream of lysosomal sulfatase activity and provides a mechanistic bridge to glycosaminoglycan degradation. Its association with multiple sulfatase-related disorders and inherited retinal disease further supports its biological importance.
- **Conclusion**: Established evidence supports SUMF1 as a biochemical enabling factor for lysosomal sulfatase function and as the strongest complex-level bridge in the module. A coordinated SUMF1-centered degradative process is plausible, but global enrichment does not support claiming that this pathway is significantly overrepresented.

#### HEXA

- **Related proteins** (co-abundance neighbors): SMPDL3B (0.87), GNS (0.84), CPVL (0.83), SV2A (0.80); STRING partners: GLB1 (0.959), GNS (0.936)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hexosaminidase subunit alpha. This gene encodes a member of the glycosyl hydrolase 20 family of proteins. The encoded preproprotein is proteolytically processed to generate the alpha subunit of the lysosomal enzyme beta-hexosaminidase. This enzyme, together with the cofactor GM2 activator protein, catalyzes the degradation of the ganglioside GM2, and other molecules containing terminal N-acetyl hexosamines. Mutations in this g…
- **Diseases (Open Targets)**: Tay-Sachs disease (0.863); hereditary disease (0.541); Tay-Sachs disease, B1 variant (0.475); Tay-Sachs disease AB variant (0.463); Tay-Sachs disease, b variant, juvenile form (0.453)
- **Europe PMC papers**: 16230
- **Why important**: HEXA links the lysosomal subgroup to SV2A and CPVL in the module and has established STRING relationships with GLB1 and GNS. HPA associates it with choroid-plexus epithelial cells, microglia, Hofbauer cells, and other cell types. Its established role in degradation of GM2 ganglioside and other glycoconjugates, together with its well-known Tay–Sachs disease association and substantial literature, makes it an important indicator of lysosomal glycolipid processing and neural vulnerability.
- **Conclusion**: Established evidence supports HEXA as a lysosomal glycan and ganglioside-catabolism component with relevance to both neural and immune-associated cell types. Its co-abundance with GNS and GLB1 is biologically coherent, while the broader module-level connection to adhesion and stem-cell biology remains a hypothesis.

## Module 4

**Tissue pair**: cerebrospinal_fluid and stem_cells  
**Genes (13)**: AGRN, CLU, FAM3C, GGT7, HYOU1, IGFBP7, IL6ST, LUM, POFUT4, PTPRZ1, SIL1, STMN2, TIMP1

### Function

No GO or KEGG term passed global correction, so the module has no statistically established pathway annotation from the primary enrichment analysis. Its composition and network suggest a heterogeneous extracellular and secretory-stress interface rather than a single demonstrated pathway. IL6ST provides cytokine-receptor signal transduction; PTPRZ1 and STMN2 provide central-nervous-system and neuronal context; LUM, IGFBP7, TIMP1, AGRN, and FAM3C provide extracellular-matrix, growth-factor, adhesion, and secreted-signaling context; and HYOU1 with SIL1 provides endoplasmic-reticulum protein-folding and stress context. The co-abundance structure is therefore consistent with coordinated regulation of extracellular signaling, matrix or cell-surface biology, and secretory or ER stress, but this remains an interpretation rather than a globally enriched functional assignment.

**Cell composition.** The module is strongly biased toward secreted or extracellular proteins, with many members annotated as secreted to blood, secreted to extracellular matrix, secreted in brain, or secreted in other tissues. HPA also shows predominantly low tissue specificity but frequent cell-type enhancement, including platelets, stromal cells, fibroblasts, brain neuronal or glial populations, and several immune-cell categories. This makes a blood, vascular, stromal, or shared-cell-type contribution plausible, especially in cerebrospinal-fluid measurements, and cautions against interpreting the module as exclusively neural. PTPRZ1 and STMN2 provide relatively specific brain context, whereas LUM, IGFBP7, TIMP1, CLU, and FAM3C are compatible with extracellular, vascular, stromal, hepatic, or immune-associated sources. HPA reports no matching tissue evidence for the two sampled tissue labels, so it cannot directly establish protein detection in cerebrospinal fluid or stem cells.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, HYOU1–SIL1, supporting a known ER chaperone and nucleotide-exchange-factor relationship. STRING reports no functional enrichment for the module. hu.MAP places POFUT4 and HYOU1 together in (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), but each complex contains only a small subset of the module and the listed complexes are broad, multifunctional assemblies. These findings support selected mechanistic links involving ER protein folding and glycoprotein processing, but they do not establish that the whole co-abundance module is a known physical complex. The remaining co-abundance edges should therefore be treated as tissue-level or cell-composition relationships unless independently validated.

**STRING interactions (score >= 0.7)**: 1 of 78 gene pairs: HYOU1–SIL1 (0.997)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (POFUT4, HYOU1; 2/60); huMAP3_09327.1 (POFUT4, HYOU1; 2/93)

### Novelty

The module may represent a novel cross-tissue co-abundance pattern because most of its gene-gene relationships are not represented by high-confidence STRING interactions or by the reported hu.MAP overlaps. However, absence from STRING or hu.MAP does not prove novelty: co-abundance can arise from shared cell types, secretion into body fluids, coordinated stress responses, or technical sampling effects, and those relationships need not be physical interactions. The presence of established biology for IL6ST, PTPRZ1, extracellular-matrix proteins, neuronal proteins, and the HYOU1–SIL1 pair argues that the potentially new feature is the cross-tissue combination and its coordinated abundance, not necessarily a new molecular function for the individual genes. Independent replication, cell-source deconvolution, and targeted protein measurements would be needed to support a claim of a new conserved biological module.

**Hypothesis.** Hypothesis: the conserved module reflects a shared secretory and extracellular-response state present in a mixture of neural or glial, vascular or stromal, and blood-associated sources. In this model, cytokine responsiveness through IL6ST, brain-associated signaling through PTPRZ1 and STMN2, extracellular-matrix and growth-factor regulation through LUM, IGFBP7, TIMP1, and AGRN, and ER folding or secretion through HYOU1 and SIL1 become co-abundant across the two sample groups. POFUT4 could connect glycoprotein processing to this state, while CLU and GGT7 could reflect extracellular chaperoning or redox-related biology. This is a testable hypothesis, not an enrichment result: it predicts that the module will weaken after adjustment for blood, vascular, stromal, and glial or neuronal cell proportions, and that residual association will be strongest for secretory stress and extracellular signaling measurements.

### Important genes

#### IL6ST

- **Related proteins** (co-abundance neighbors): LUM (0.89), GGT7 (0.82), HYOU1 (0.80), IGFBP7 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: interleukin 6 cytokine family signal transducer. The protein encoded by this gene is a signal transducer shared by many cytokines, including interleukin 6 (IL6), ciliary neurotrophic factor (CNTF), leukemia inhibitory factor (LIF), and oncostatin M (OSM). This protein functions as a part of the cytokine receptor complex. The activation of this protein is dependent upon the binding of cytokines to their receptors. vIL6, a protein related to IL6 a…
- **Diseases (Open Targets)**: Autosomal recessive hyper-IgE syndrome (0.703); Stuve-Wiedemann syndrome 2 (0.668); hyper-IgE recurrent infection syndrome 4A, autosomal dominant (0.658); neuromyelitis optica (0.569); immunodeficiency 94 with autoinflammation and dysmorphic facies (0.424)
- **Europe PMC papers**: 11529
- **Why important**: IL6ST has the greatest network connectivity and links cytokine-family signal transduction to LUM, GGT7, HYOU1, and IGFBP7. Its HPA profile includes platelet and microglial enhancement, and its established biology covers cytokine receptor complexes, inflammatory signaling, adaptive immune regulation, and JAK-STAT-related signaling. Its disease associations include hyper-IgE syndromes and neuromyelitis optica, and its literature volume is very large.
- **Conclusion**: Established evidence supports IL6ST as a central cytokine-signal-transduction component and a plausible bridge between immune or inflammatory and neural sample contexts. The module does not establish that IL6ST drives the co-abundance pattern; its central position may instead reflect shared cellular composition or a common extracellular response.

#### PTPRZ1

- **Related proteins** (co-abundance neighbors): IGFBP7 (0.91), POFUT4 (0.82), FAM3C (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein tyrosine phosphatase receptor type Z1. This gene encodes a member of the receptor protein tyrosine phosphatase family. Expression of this gene is restricted to the central nervous system (CNS), and it may be involved in the regulation of specific developmental processes in the CNS. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, May 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.524); Abnormality of the integument (0.316); biliary tract disorder (0.314); placental retention (0.215); Hypocalcemia (0.180)
- **Europe PMC papers**: 2080
- **Why important**: PTPRZ1 is among the most connected genes and links IGFBP7, POFUT4, and FAM3C. It is tissue-enriched in brain and enhanced in astrocytes, Bergmann glia, ependymal cells, and oligodendrocyte progenitor cells, while being undetected in immune cells in the HPA summary. Its established functions include receptor-type tyrosine phosphatase activity, CNS development, neuron projection development, learning or memory, and myelination. It has a substantial literature and an Open Targets association with neurodegenerative disease.
- **Conclusion**: Established evidence supports PTPRZ1 as the strongest neural or glial anchor of the module. Its co-abundance with largely secreted and vascular-associated proteins is compatible with a brain extracellular-interface process, but the module alone cannot distinguish a neural mechanism from changing proportions of glial or other source cells.

#### HYOU1

- **Related proteins** (co-abundance neighbors): IL6ST (0.80); STRING partners: SIL1 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 connects to IL6ST in the module and has a high-confidence STRING relationship with SIL1. It also occurs with POFUT4 in both reported hu.MAP complexes. Its established biology involves ER protein folding, secretion, hypoxia, ER stress, and protection from apoptosis, and its HPA profile includes other brain neurons and plasma cells. It has disease associations involving neurodegenerative disease and immunoglobulin abnormalities, with a substantial literature.
- **Conclusion**: Established evidence supports HYOU1 as the clearest stress-and-secretory machinery component, strengthened by the HYOU1–SIL1 STRING relationship. It is a plausible mechanistic bridge between extracellular protein abundance and intracellular secretory load, but the co-abundance module does not prove that ER stress is its initiating cause.

#### LUM

- **Related proteins** (co-abundance neighbors): IL6ST (0.89), AGRN (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lumican. This gene encodes a member of the small leucine-rich proteoglycan (SLRP) family that includes decorin, biglycan, fibromodulin, keratocan, epiphycan, and osteoglycin. In these bifunctional molecules, the protein moiety binds collagen fibrils and the highly charged hydrophilic glycosaminoglycans regulate interfibrillar spacings. Lumican is the major keratan sulfate proteoglycan of the cornea but is …
- **Diseases (Open Targets)**: lumbar disc herniation (0.359); Dupuytren Contracture (0.357); fibroblastic disorder (0.357); Hallux valgus (0.357); preeclampsia (0.154)
- **Europe PMC papers**: 14825
- **Why important**: LUM links IL6ST and AGRN and provides a direct extracellular-matrix component. Its biology includes collagen-fibril organization and regulation of growth-factor signaling. HPA shows tissue enhancement in gallbladder and placenta, enrichment in decidual stromal cells, and immune enrichment in basophils, while identifying it as secreted to extracellular matrix. It has a very large literature and associations with several fibroblastic or connective-tissue disorders.
- **Conclusion**: Established evidence supports LUM as an extracellular-matrix and stromal-context marker. In this module it may report matrix-producing or vascular-associated source cells rather than a CNS-specific mechanism; its link to IL6ST and AGRN supports an extracellular signaling interpretation but does not establish direct molecular interaction.

#### IGFBP7

- **Related proteins** (co-abundance neighbors): PTPRZ1 (0.91), IL6ST (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor binding protein 7. This gene encodes a member of the insulin-like growth factor (IGF)-binding protein (IGFBP) family. IGFBPs bind IGFs with high affinity, and regulate IGF availability in body fluids and tissues and modulate IGF binding to its receptors. This protein binds IGF-I and IGF-II with relatively low affinity, and belongs to a subfamily of low-affinity IGFBPs. It also stimulates prostacyclin production and …
- **Diseases (Open Targets)**: familial retinal arterial macroaneurysm (0.607); schizophrenia (0.346); hyperemesis gravidarum (0.328); alcohol drinking (0.314); atrial fibrillation (0.314)
- **Europe PMC papers**: 4402
- **Why important**: IGFBP7 links PTPRZ1 and IL6ST and is secreted to blood. Its established functions include modulation of IGF availability, angiogenesis, cell adhesion, cell growth, and regulation of cell proliferation. HPA shows blood-vessel enhancement and enhancement in stromal, fibroblast, hepatic-stellate, and eosinophil-related cell contexts. It has a substantial literature and disease associations including familial retinal arterial macroaneurysm and schizophrenia.
- **Conclusion**: Established evidence supports IGFBP7 as a vascular or stromal extracellular signaling component that can connect the neural anchor PTPRZ1 with cytokine signaling through IL6ST. Its presence favors a mixed-source or body-fluid explanation and makes it an important candidate for testing whether the module is driven by vascular or secreted-protein composition.

## Module 5

**Tissue pair**: cerebrospinal_fluid and stem_cells  
**Genes (24)**: ALB, NAGLU, BCAM, CD109, ALCAM, CD276, CD44, ECE1, EGFR, HSPA13, IGFBP3, L1CAM, LGALS1, LGALS3BP, LRP1, MAN2B1, NECTIN1, PLBD2, PLOD2, ACP2, SEMA4D, SORL1, TFRC, TWSG1

### Function

The module does not have any GO or KEGG term passing global correction, and STRING reports no functional enrichment. Its network and gene annotations instead point to a mixed cell-surface interaction, adhesion, receptor-trafficking, endocytic, lysosomal, and extracellular-signaling program. EGFR, CD44, ALCAM, L1CAM, LRP1, SEMA4D, NECTIN1, and BCAM support cell-cell or cell-matrix interaction, while SORL1 and LRP1 support receptor-mediated uptake and sorting. ACP2, ECE1, MAN2B1, and NAGLU indicate lysosomal or extracellular processing functions. TWSG1 and CD109 provide links to TGF-beta or BMP-related regulation, whereas ALB, IGFBP3, LGALS3BP, and LGALS1 are compatible with extracellular or circulating protein interactions. The strongest interpretation is therefore a heterogeneous adhesion and receptor-handling module rather than a narrowly defined pathway. Co-abundance does not establish direct regulation or a single biochemical complex.

**Cell composition.** The module is compositionally mixed but is dominated by plasma or secreted proteins and proteins associated with extracellular vesicles or the cell surface. ALB is a liver-enriched, blood-secreted protein and is the most conspicuous marker of possible plasma carryover or blood-derived material. IGFBP3, ALCAM, CD44, SORL1, LGALS3BP, and TWSG1 also have secreted-to-blood, secreted, vesicular, or extracellular annotations. HPA additionally shows frequent enhancement in monocytes, neutrophils, dendritic-cell populations, macrophages, microglia, trophoblast populations, and related myeloid or vascular contexts. This makes a blood, myeloid, extracellular-vesicle, or shared-cell-type contribution plausible in the cerebrospinal-fluid and stem-cell comparison. It is not possible to verify tissue-specific protein detection in either named sample type from HPA because the fact sheet reports no matching HPA tissue data. The module should therefore not be interpreted as a purified stem-cell or cerebrospinal-fluid program without controlling for plasma contamination, immune-cell content, and shared cellular constituents.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supplies a focused set of high-confidence known relationships, especially the EGFR-centered links to CD44, IGFBP3, L1CAM, LRP1, TFRC, ALCAM, and ALB; additional known links include ALCAM with CD44 and L1CAM, and LGALS1 with LGALS3BP. These relationships support a biologically connected adhesion and receptor-signaling neighborhood, but they also mean that part of the module recapitulates established protein associations rather than representing entirely new links. hu.MAP provides repeated complex-level support for the ALCAM, NECTIN1, CD276, and LGALS1 combination across (hu.MAP huMAP3_10980.1) through (hu.MAP huMAP3_09336.1) and several lower-overlap complexes. L1CAM with SEMA4D is represented in (hu.MAP huMAP3_10729.1), BCAM with SEMA4D in (hu.MAP huMAP3_07949.1), and ECE1 with NAGLU in (hu.MAP huMAP3_09327.1) and (hu.MAP huMAP3_06775.1). The repeated ALCAM, NECTIN1, CD276, and LGALS1 memberships suggest a shared adhesion or membrane-associated complex context, whereas the ECE1 and NAGLU complexes support a separate lysosomal or glycoprotein-processing component. Because many module pairs lack STRING support and many hu.MAP complexes contain only a subset of module genes, the module is not equivalent to one validated physical complex.

**STRING interactions (score >= 0.7)**: 14 of 276 gene pairs: ALB–CD44 (0.739); ALB–EGFR (0.808); ALB–LRP1 (0.714); ALB–TFRC (0.88); ALCAM–CD44 (0.859); ALCAM–EGFR (0.708); ALCAM–L1CAM (0.979); CD44–EGFR (0.998); CD44–IGFBP3 (0.739); EGFR–IGFBP3 (0.981); EGFR–L1CAM (0.976); EGFR–LRP1 (0.838); EGFR–TFRC (0.832); LGALS1–LGALS3BP (0.826)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10980.1 (LGALS1, ALCAM, NECTIN1, CD276; 4/44); huMAP3_11349.1 (LGALS1, ALCAM, NECTIN1, CD276; 4/78); huMAP3_05590.1 (LGALS1, ALCAM, NECTIN1; 3/14); huMAP3_06308.1 (ALCAM, NECTIN1, CD276; 3/20); huMAP3_10503.1 (ALCAM, NECTIN1, CD276; 3/27); huMAP3_08689.1 (ALCAM, NECTIN1, CD276; 3/37); huMAP3_10848.1 (ALCAM, NECTIN1, CD276; 3/46); huMAP3_09336.1 (ALCAM, NECTIN1, CD276; 3/50); huMAP3_09327.1 (ECE1, NAGLU, CD109; 3/93); huMAP3_10729.1 (L1CAM, SEMA4D; 2/6); huMAP3_01717.1 (NECTIN1, CD276; 2/8); huMAP3_07927.1 (LGALS1, CD276; 2/8); huMAP3_10920.1 (LGALS1, NECTIN1; 2/8); huMAP3_02887.1 (ALCAM, CD276; 2/9); huMAP3_05555.1 (ALCAM, CD276; 2/9); huMAP3_09169.1 (LGALS1, CD276; 2/9); huMAP3_04614.1 (LGALS1, NECTIN1; 2/11); huMAP3_07949.1 (BCAM, SEMA4D; 2/12); huMAP3_06892.1 (LGALS1, NECTIN1; 2/15); huMAP3_14792.1 (LGALS1, NECTIN1; 2/19); huMAP3_05584.1 (ALCAM, NECTIN1; 2/22); huMAP3_08103.1 (ALCAM, NECTIN1; 2/23); huMAP3_09105.1 (ALCAM, NECTIN1; 2/24); huMAP3_06775.1 (ECE1, NAGLU; 2/60)

### Novelty

The exact conserved co-abundance module across cerebrospinal fluid and stem cells may be a new systems-level observation, especially because the module combines neural adhesion genes, receptor-trafficking genes, lysosomal enzymes, circulating proteins, and myeloid-associated markers. However, the underlying biology is not wholly new: several interactions are already present in STRING, and recurrent subsets are represented in hu.MAP. The lack of STRING or hu.MAP support for some pairs cannot by itself establish novelty, because co-abundance can reflect shared regulation, common cellular origin, extracellular carryover, or indirect biology rather than a physical interaction. The defensible conclusion is that the cross-tissue co-abundance pattern is potentially novel, while its component functions and several relationships are established. Independent replication, adjustment for plasma and immune-cell abundance, and validation in matched cerebrospinal-fluid and stem-cell material would be needed to claim a new mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared extracellular and membrane-associated state involving adhesion, receptor signaling, endocytic clearance, and glycoprotein or lysosomal processing. In cerebrospinal fluid, this state could arise from neural or glial adhesion and trafficking programs together with extracellular proteins and vesicles. In stem-cell material, it could arise from a mixture of progenitor adhesion, trophoblast-like or vascular-associated programs, and contaminating or shared myeloid components. EGFR, CD44, ALCAM, L1CAM, SEMA4D, and LRP1 could form a signaling and adhesion interface, while SORL1, ACP2, ECE1, MAN2B1, and NAGLU could process or route associated cargo. ALB and other circulating proteins may amplify the apparent module through plasma contribution rather than through intracellular co-regulation. This is a mechanistic model to test, not an established causal pathway.

### Important genes

#### EGFR

- **Related proteins** (co-abundance neighbors): IGFBP3 (0.97), ACP2 (0.95), ECE1 (0.95), SORL1 (0.94), PLBD2 (0.94), LRP1 (0.94), L1CAM (0.93), NAGLU (0.90), ALB (0.85), TFRC (0.85), MAN2B1 (0.82), ALCAM (0.82); STRING partners: ALB (0.808), ALCAM (0.708), CD44 (0.998), IGFBP3 (0.981), L1CAM (0.976), LRP1 (0.838), TFRC (0.832)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: epidermal growth factor receptor. The protein encoded by this gene is a transmembrane glycoprotein that is a member of the protein kinase superfamily. This protein is a receptor for members of the epidermal growth factor family. EGFR is a cell surface protein that binds to epidermal growth factor, thus inducing receptor dimerization and tyrosine autophosphorylation leading to cell proliferation. Mutations in this gene are associat…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.850); lung adenocarcinoma (0.774); cancer (0.737); head and neck squamous cell carcinoma (0.725); lung cancer (0.717)
- **Europe PMC papers**: 223694
- **Why important**: EGFR is among the most connected genes in the co-abundance network and is the main STRING-supported hub, linking ALB, ALCAM, CD44, IGFBP3, L1CAM, LRP1, and TFRC. It is a cell-surface protein tyrosine kinase involved in growth-factor receptor signaling, MAPK signaling, and protein phosphorylation. It has extensive disease and literature support, including strong cancer associations, making it the best-established signaling anchor in the module.
- **Conclusion**: Established evidence supports EGFR as a central receptor-signaling component and as a bridge between the adhesion, growth-factor, and trafficking portions of the module. It is not established that EGFR drives the conserved co-abundance pattern. Hypothesis: EGFR abundance may mark a shared activated or remodeling cell-surface state, or may reflect coordinated extracellular and membrane composition rather than receptor activation.

#### SEMA4D

- **Related proteins** (co-abundance neighbors): LGALS3BP (1.00), L1CAM (1.00), MAN2B1 (1.00), HSPA13 (0.99), PLBD2 (0.98), ALB (0.98), SORL1 (0.98), CD276 (0.97), PLOD2 (0.97), ECE1 (0.96), LRP1 (0.95), ALCAM (0.95); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10729.1, huMAP3_07949.1
- **Function (MyGene.info)**: semaphorin 4D. Enables identical protein binding activity; semaphorin receptor binding activity; and transmembrane signaling receptor activity. Involved in several processes, including positive regulation of phosphatidylinositol 3-kinase signaling; regulation of neuron projection development; and regulation of phosphate metabolic process. Is integral component of plasma membrane. [provided by Alliance of Genome …
- **Diseases (Open Targets)**: skin aging (0.442); sclerosing cholangitis (0.372); intelligence (0.283); placental abruption (0.191); otosclerosis (0.153)
- **Europe PMC papers**: 2198
- **Why important**: SEMA4D has very high network connectivity and links neural, immune, adhesion, and extracellular-vesicle-associated features. HPA places it in brain, microglial, neutrophil, oligodendrocyte, and platelet-related contexts. Its established functions include semaphorin receptor binding, cell adhesion, immune response, axon guidance, and regulation of phosphatidylinositol three-kinase signaling. It also connects to L1CAM and appears in hu.MAP contexts with L1CAM and BCAM through (hu.MAP huMAP3_10729.1) and (hu.MAP huMAP3_07949.1), although the fact sheet reports no STRING partners for it.
- **Conclusion**: Established evidence supports SEMA4D as a biologically plausible interface between neural guidance and immune or adhesion biology. Its strong network position makes it important despite the absence of STRING partners. Hypothesis: SEMA4D may help explain why the module is shared between a neural-fluid context and a progenitor or immune-contaminated context, but this requires cell-resolved validation.

#### L1CAM

- **Related proteins** (co-abundance neighbors): SEMA4D (1.00), LRP1 (0.97), ACP2 (0.94), EGFR (0.93), NAGLU (0.89), MAN2B1 (0.89), SORL1 (0.87), PLOD2 (0.84), PLBD2 (0.81); STRING partners: ALCAM (0.979), EGFR (0.976)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10729.1
- **Function (MyGene.info)**: L1 cell adhesion molecule. The protein encoded by this gene is an axonal glycoprotein belonging to the immunoglobulin supergene family. The ectodomain, consisting of several immunoglobulin-like domains and fibronectin-like repeats (type III), is linked via a single transmembrane sequence to a conserved cytoplasmic domain. This cell adhesion molecule plays an important role in nervous system development, including neuronal m…
- **Diseases (Open Targets)**: X-linked hydrocephalus with stenosis of the aqueduct of Sylvius (0.855); MASA syndrome (0.833); X-linked complicated corpus callosum dysgenesis (0.762); L1 syndrome (0.725); Spastic paraplegia (0.571)
- **Europe PMC papers**: 6523
- **Why important**: L1CAM is highly connected and has a strong brain-enhanced HPA profile, with expression in excitatory, inhibitory, and other brain neurons. It is an axonal cell-adhesion molecule involved in neuronal migration, differentiation, nervous-system development, and axon guidance. It has established STRING relationships with ALCAM and EGFR and is present with SEMA4D in hu.MAP complex (hu.MAP huMAP3_10729.1). Its disease associations include X-linked hydrocephalus, corpus-callosum dysgenesis, L1 syndrome, and spastic paraplegia, with extensive literature coverage.
- **Conclusion**: Established evidence supports L1CAM as the strongest neural-adhesion anchor in the module and as a plausible contributor to the cerebrospinal-fluid association. It does not prove that the entire module is neuronal, because L1CAM is co-abundant with circulating and myeloid-associated proteins. Hypothesis: L1CAM may connect neural adhesion or axonal material to EGFR- and SEMA4D-associated signaling in the conserved module.

#### LRP1

- **Related proteins** (co-abundance neighbors): L1CAM (0.97), SEMA4D (0.95), EGFR (0.94), ACP2 (0.94), PLOD2 (0.88), SORL1 (0.84), TWSG1 (0.81), ECE1 (0.81); STRING partners: ALB (0.714), EGFR (0.838)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LDL receptor related protein 1. This gene encodes a member of the low-density lipoprotein receptor family of proteins. The encoded preproprotein is proteolytically processed by furin to generate 515 kDa and 85 kDa subunits that form the mature receptor (PMID: 8546712). This receptor is involved in several cellular processes, including intracellular signaling, lipid homeostasis, and clearance of apoptotic cells. In addition, the …
- **Diseases (Open Targets)**: neurodegenerative disease (0.514); keratosis pilaris atrophicans (0.499); developmental dysplasia of the hip (0.466); Alzheimer disease (0.462); Parkinson disease (0.443)
- **Europe PMC papers**: 10645
- **Why important**: LRP1 is highly connected and links EGFR, L1CAM, SEMA4D, ACP2, PLOD2, SORL1, TWSG1, and ECE1 in the network. It is a membrane receptor involved in lipid homeostasis, receptor-mediated endocytosis, apoptotic-cell clearance, and signaling. HPA associates it with adipocytes, fibroblasts, hepatocytes, Kupffer cells, and several monocyte or dendritic-cell populations. Its established links to neurodegenerative disease, Alzheimer disease, and Parkinson disease make it particularly relevant to a cerebrospinal-fluid-related module.
- **Conclusion**: Established evidence supports LRP1 as a receptor-trafficking and clearance component that could connect extracellular cargo handling with neural and immune biology. The module does not establish LRP1-mediated clearance as the cause of the co-abundance pattern. Hypothesis: LRP1 may coordinate uptake or sorting of extracellular proteins and vesicles represented in this module, especially in microglial, monocyte-derived, or neural-supporting cells.

#### ALCAM

- **Related proteins** (co-abundance neighbors): SEMA4D (0.95), CD44 (0.85), ACP2 (0.85), TWSG1 (0.84), EGFR (0.82); STRING partners: CD44 (0.859), EGFR (0.708), L1CAM (0.979)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10980.1, huMAP3_11349.1, huMAP3_05590.1, huMAP3_06308.1, huMAP3_10503.1, huMAP3_08689.1, huMAP3_10848.1, huMAP3_09336.1, huMAP3_02887.1, huMAP3_05555.1, huMAP3_05584.1, huMAP3_08103.1, huMAP3_09105.1
- **Function (MyGene.info)**: activated leukocyte cell adhesion molecule. This gene encodes activated leukocyte cell adhesion molecule (ALCAM), also known as CD166 (cluster of differentiation 166), which is a member of a subfamily of immunoglobulin receptors with five immunoglobulin-like domains (VVC2C2C2) in the extracellular domain. This protein binds to T-cell differentiation antigene CD6, and is implicated in the processes of cell adhesion and migration. Multiple al…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.458); mathematical ability (0.453); open-angle glaucoma (0.396); restless legs syndrome (0.379); ovarian dysfunction (0.362)
- **Europe PMC papers**: 4212
- **Why important**: ALCAM occupies a connected adhesion position and has STRING support with CD44, EGFR, and L1CAM. It is represented repeatedly in hu.MAP complexes, particularly the complexes containing ALCAM, NECTIN1, CD276, and LGALS1 across (hu.MAP huMAP3_10980.1) through (hu.MAP huMAP3_09336.1) and additional complexes. Its established functions include cell-cell adhesion, cell migration, signal transduction, neuron projection development, and axon guidance. HPA also associates it with myeloid dendritic cells, while its tissue profile is enriched in parathyroid gland and its protein is reported in vesicles and blood.
- **Conclusion**: Established evidence supports ALCAM as a major adhesion and complex-context marker, with both neural-development and immune-cell relevance. The repeated hu.MAP membership is stronger evidence for shared complex context than for a single complete complex containing the whole module. Hypothesis: ALCAM may organize a membrane-adhesion state that is conserved across the two sample groups, while its blood or vesicle association may also contribute to the observed co-abundance.

## Module 6

**Tissue pair**: cerebrospinal_fluid and stem_cells  
**Genes (7)**: APOC1, APOE, BASP1, IGFBP2, MDH1, CHGB, TXN

### Function

The module does not support a single statistically confirmed GO or KEGG function because no GO/KEGG term passed global correction. Its gene composition and network structure instead suggest a mixed extracellular and intracellular biology involving lipoprotein handling, neuroendocrine or neuronal secretory biology, cellular redox control, central carbon metabolism, and growth-factor regulation. The strongest coherent functional signal is the APOC1–APOE lipoprotein axis, linking lipid transport and triglyceride-related biology. CHGB adds a secretory-vesicle and neuroendocrine component, while TXN, MDH1, BASP1, and IGFBP2 suggest cellular stress, metabolism, membrane-associated signaling, and growth-factor availability. These annotations are interpretive rather than evidence of significant pathway enrichment.

**Cell composition.** The module is compositionally heterogeneous rather than a clean tissue-specific intracellular pathway. Most of its genes are secreted or associated with vesicles, membranes, or extracellular transport, and the HPA summary identifies secreted proteins in a substantial majority of the module. APOC1, APOE, and IGFBP2 are secreted to blood, whereas CHGB and TXN have intracellular or membrane-associated localization. HPA expression points most often to brain, liver, and adrenal gland, with hepatocyte and neuroendocrine-related signals. Some genes also show immune-cell enrichment or low immune-cell specificity, including APOC1 in myeloid dendritic cells and BASP1 in neutrophils. This pattern means that the shared signal between cerebrospinal fluid and stem cells could reflect circulating or secreted proteins, tissue leakage, shared secretory biology, or shared cellular composition rather than a mechanism unique to both sample groups. HPA provides no direct protein-detection evidence for the named cerebrospinal-fluid or stem-cell tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only reported high-confidence STRING relationship within the module is APOC1 with APOE. This is an established interaction and supports a lipid-transport or lipoprotein-associated submodule. No other module pair is supported at the stated STRING threshold, and there is no STRING functional-enrichment result. No hu.MAP complex contains multiple members of the module. Therefore, the co-abundance structure is not explained by a known multiprotein complex; it appears to combine a validated APOC1–APOE relationship with additional expression covariation that may arise from secretion, tissue composition, or coordinated cellular state.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: APOC1–APOE (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is not established as a new molecular complex or a newly discovered interaction network. The APOC1–APOE relationship and the individual functions of the genes are already well documented, while hu.MAP provides no shared complex and STRING provides no broader high-confidence network support. The potentially novel aspect is the co-abundance of this particular set across cerebrospinal fluid and stem cells. However, that observation alone does not establish novelty or mechanism, because co-abundance can arise from shared secretion, blood-derived material, cellular composition, or technical and sampling effects. A claim of novelty would require replication, comparison with other tissue pairs, control for cell-type composition and plasma contamination, and independent validation at the protein level.

**Hypothesis.** Hypothesis: the module represents a secreted and vesicle-associated metabolic state that couples lipoprotein transport with neuronal or neuroendocrine secretion, redox balance, and growth-factor availability. In this model, APOC1 and APOE form the lipid-transport core; CHGB reflects secretory vesicles; IGFBP2 reflects extracellular growth-factor regulation; and TXN, MDH1, and BASP1 capture intracellular redox, metabolic, and membrane-associated responses. The shared detection in cerebrospinal fluid and stem cells could therefore reflect a common secretory or progenitor-associated state, but this remains a hypothesis and should not be interpreted as demonstrated direct interaction among all module members.

### Important genes

#### APOE

- **Related proteins** (co-abundance neighbors): APOC1 (0.87); STRING partners: APOC1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein E. The protein encoded by this gene is a major apoprotein of the chylomicron. It binds to a specific liver and peripheral cell receptor, and is essential for the normal catabolism of triglyceride-rich lipoprotein constituents. This gene maps to chromosome 19 in a cluster with the related apolipoprotein C1 and C2 genes. Mutations in this gene result in familial dysbetalipoproteinemia, or type III hype…
- **Diseases (Open Targets)**: hyperlipoproteinemia type 3 (0.803); coronary artery disorder (0.782); lipoprotein glomerulopathy (0.759); Alzheimer disease (0.696); familial hypercholesterolemia (0.651)
- **Europe PMC papers**: 74272
- **Why important**: APOE is the most literature-rich gene in the module and occupies the lipoprotein-associated branch through its high-confidence STRING relationship with APOC1. It is secreted to blood, has enhanced expression in brain, liver, and adrenal gland, and is associated with lipid transport, receptor-mediated endocytosis, hyperlipoproteinemia, coronary artery disease, and Alzheimer disease. Its terminal network position does not imply broad physical connectivity, but its biological relevance and disease evidence make it a central interpretive anchor.
- **Conclusion**: Established evidence supports APOE as a secreted lipid-transport protein and as a validated interaction partner of APOC1. The hypothesis that APOE drives the shared cerebrospinal-fluid and stem-cell co-abundance pattern is plausible but unproven.

#### APOC1

- **Related proteins** (co-abundance neighbors): TXN (0.90), APOE (0.87); STRING partners: APOE (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein C1. This gene encodes a member of the apolipoprotein C1 family. This gene is expressed primarily in the liver, and it is activated when monocytes differentiate into macrophages. The encoded protein plays a central role in high density lipoprotein (HDL) and very low density lipoprotein (VLDL) metabolism. This protein has also been shown to inhibit cholesteryl ester transfer protein in plasma. A pseudog…
- **Diseases (Open Targets)**: Alzheimer disease (0.574); dementia (0.523); metabolic syndrome (0.464); Hypercholesterolemia (0.461); familial hyperlipidemia (0.461)
- **Europe PMC papers**: 4121
- **Why important**: APOC1 is directly connected to APOE and is the clearest module member linking the network to lipoprotein biology. It is liver-enriched, hepatocyte-enriched, secreted to blood, and immune-cell enriched in myeloid dendritic cells. Its reported functions include lipid and triglyceride metabolism and regulation of cholesterol transport, with disease associations including Alzheimer disease, dementia, metabolic syndrome, and hypercholesterolemia.
- **Conclusion**: Established evidence supports APOC1 as a secreted regulator of lipoprotein metabolism and as a validated partner of APOE. Its presence may indicate a circulating or hepatic contribution to the module; a direct role in stem-cell biology is not established by the fact sheet.

#### CHGB

- **Related proteins** (co-abundance neighbors): MDH1 (0.98), TXN (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromogranin B. This gene encodes a tyrosine-sulfated secretory protein abundant in peptidergic endocrine cells and neurons. This protein may serve as a precursor for regulatory peptides. [provided by RefSeq, Jan 2009].
- **Diseases (Open Targets)**: Meniere disease (0.190); prostate cancer (0.112); Familial prostate cancer (0.112); placenta praevia (0.112); hypertensive disorder (0.111)
- **Europe PMC papers**: 1555
- **Why important**: CHGB links the module to secretory vesicles, neurons, and endocrine cell types. It has enhanced expression in brain, adrenal gland, and pituitary gland and is associated with neuroendocrine and pancreatic islet cell types. Its network position connects the lipoprotein-associated branch indirectly through TXN, while its substantial literature supports its importance as a marker and component of peptidergic secretory biology.
- **Conclusion**: Established evidence supports CHGB as a secretory protein associated with endocrine cells and neurons. Its co-abundance with APOC1 and APOE may indicate coordinated secretion or sample composition, but a direct mechanistic connection is hypothetical.

#### IGFBP2

- **Related proteins** (co-abundance neighbors): BASP1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor binding protein 2. The protein encoded by this gene is one of six similar proteins that bind insulin-like growth factors I and II (IGF-I and IGF-II). The encoded protein can be secreted into the bloodstream, where it binds IGF-I and IGF-II with high affinity, or it can remain intracellular, interacting with many different ligands. High expression levels of this protein promote the growth of several types of tumors a…
- **Diseases (Open Targets)**: neurodegenerative disease (0.313); intelligence (0.303); pregnancy disorder (0.290); open-angle glaucoma (0.258); carcinoma of esophagus (0.254)
- **Europe PMC papers**: 6255
- **Why important**: IGFBP2 is a secreted growth-factor-binding protein with enhanced expression in blood vessel and pancreas and cell-type enhancement in several epithelial and stromal populations, including hepatocytes. It connects to BASP1 in the module and has reported roles in binding IGF proteins, nutrient and mechanical responses, and tumor-associated biology. Its extracellular location and disease associations make it relevant to a possible secretory or progenitor-associated state.
- **Conclusion**: Established evidence supports IGFBP2 as an IGF-binding protein that can be secreted into the bloodstream. Its participation in a shared cerebrospinal-fluid and stem-cell program is a hypothesis that requires independent validation.
