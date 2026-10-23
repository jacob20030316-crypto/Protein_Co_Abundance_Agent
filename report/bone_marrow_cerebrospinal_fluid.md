# Conserved co-abundance modules: bone_marrow and cerebrospinal_fluid

## Module 0

**Tissue pair**: bone_marrow and cerebrospinal_fluid  
**Genes (7)**: SLC3A2, SERPINA3, GOLM2, HSPA13, BPNT2, PLXNB2, SIRPA

### Function

No GO or KEGG term passed global correction, and there are no supplementary STRING enrichment terms. Therefore this module does not support a statistically established pathway-level function. Its gene-level composition is compatible with a mixed interface involving myeloid-cell signalling, cell adhesion or migration, membrane transport, Golgi biology, protein quality control, and extracellular protease regulation. SIRPA is the main network hub and is annotated for negative regulation of receptor-linked signalling, cell adhesion, migration, and inflammatory signalling. PLXNB2 connects the receptor-related component to SERPINA3 and GOLM2 and is annotated for semaphorin-related axon guidance, cell migration, endocytosis, and cell adhesion. These annotations suggest a possible cell-surface and trafficking theme, but this remains an interpretation rather than enrichment-supported function.

**Cell composition.** The module is not predominantly a plasma or secreted-protein module: only SERPINA3 is explicitly secreted to blood, while the other genes are membrane, intracellular, or Golgi-associated. HPA indicates that most genes have low tissue specificity, with isolated enhancement in brain, liver, or pancreas. Several genes show cell-type enhancement in monocytes, myeloid dendritic cells, astrocytes, plasma cells, syncytiotrophoblasts, or other specialized cells, while most have low immune-cell specificity. Bone-marrow protein detection is present for several members, whereas there is no matching HPA cerebrospinal-fluid tissue entry. Thus the shared signal could reflect broadly expressed proteins together with myeloid or glial and other cell-type contributions in the sampled material; it should not be treated as evidence for a cerebrospinal-fluid-specific secreted program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING pair among the tested module genes met the supplied interaction threshold, and no STRING functional enrichment was reported. No hu.MAP complex contains multiple module members. The co-abundance links are therefore not corroborated by the supplied physical-interaction or complex resources. This does not disprove coordinated regulation or co-occurrence across samples, but it argues against describing the module as a known protein complex or established interaction network.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be novel as a tissue-pair co-abundance pattern, because its exact gene set has no reported high-confidence STRING interactions, no multi-member hu.MAP complex, and no globally significant GO or KEGG annotation. However, these absences do not establish biological novelty: several individual genes and their functions are well characterized, and co-abundance can arise from shared cell composition, broad expression, or sample handling. The defensible conclusion is that the coordinated module-level observation is unvalidated and potentially novel, not that the underlying biology is newly discovered.

**Hypothesis.** Hypothesis: variation in a shared myeloid or glial-associated cellular state may coordinate SIRPA-linked inhibitory signalling and adhesion or migration machinery with PLXNB2-mediated receptor trafficking, while Golgi and protein-quality-control genes support membrane-protein processing. SERPINA3 could represent a blood-borne or astrocyte-associated inflammatory and protease-regulatory component that covaries with this state. This model predicts that the co-abundance pattern will track cell-type proportions or activation state more strongly than a single canonical pathway, and it requires validation with cell deconvolution, independent cohorts, protein-level measurements, and targeted interaction or perturbation experiments.

### Important genes

#### SIRPA

- **Related proteins** (co-abundance neighbors): PLXNB2 (0.96), HSPA13 (0.92), SLC3A2 (0.91); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal regulatory protein alpha. The protein encoded by this gene is a member of the signal-regulatory-protein (SIRP) family, and also belongs to the immunoglobulin superfamily. SIRP family members are receptor-type transmembrane glycoproteins known to be involved in the negative regulation of receptor tyrosine kinase-coupled signaling processes. This protein can be phosphorylated by tyrosine kinases. The phospho-tyrosine residue…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.376); thrombocytopenia 4 (0.364); neurodegenerative disease (0.361); hemorrhagic disease (0.351); diabetes mellitus (0.324)
- **Europe PMC papers**: 3860
- **Why important**: SIRPA is the central network connector in the supplied graph, linking PLXNB2, HSPA13, and SLC3A2. It is a signal-regulatory immunoglobulin-superfamily receptor with annotations for cell adhesion, migration, and negative regulation of inflammatory signalling. HPA places it in brain-enhanced and monocyte or myeloid-associated contexts, and it has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports SIRPA as the strongest cellular-signalling anchor and as a plausible marker of myeloid or glial-associated biology. It is not established that SIRPA drives this module or directly interacts with the linked proteins in this dataset; that causal role is a hypothesis.

#### PLXNB2

- **Related proteins** (co-abundance neighbors): SIRPA (0.96), SERPINA3 (0.93), GOLM2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plexin B2. Members of the B class of plexins, such as PLXNB2 are transmembrane receptors that participate in axon guidance and cell migration in response to semaphorins (Perrot et al. (2002) [PubMed 12183458]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Intellectual disability (0.519); amelogenesis imperfecta (0.518); sensorineural hearing loss disorder (0.516); cutaneous melanoma (0.486); neurodegenerative disease (0.455)
- **Europe PMC papers**: 2109
- **Why important**: PLXNB2 is tied to SIRPA and also connects the module to SERPINA3 and GOLM2, making it a bridge between the receptor-like and secreted or Golgi-associated portions. Its established annotations include semaphorin-responsive axon guidance, cell migration, receptor-mediated endocytosis, and cell adhesion. HPA reports enhancement in several epithelial cell types and enrichment across monocyte and dendritic-cell categories, while disease associations include neurodevelopmental and neurodegenerative contexts.
- **Conclusion**: Established evidence supports PLXNB2 as a multifunctional membrane receptor relevant to adhesion, trafficking, and cell movement. Its bridge position makes it a useful mechanistic candidate, but the module does not establish a specific PLXNB2 pathway or direct physical interaction.

#### SERPINA3

- **Related proteins** (co-abundance neighbors): PLXNB2 (0.93); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family A member 3. The protein encoded by this gene is a member of the serpin family of proteins, a group of proteins that inhibit serine proteases. This gene is one in a cluster of serpin genes located on the q arm of chromosome 14. Polymorphisms in this protein appear to be tissue specific and influence protease targeting. Variations in this protein's sequence have been implicated in Alzheimer's disease, and defic…
- **Diseases (Open Targets)**: prostate carcinoma (0.359); chronic kidney disease (0.217); peripheral arterial occlusive disease 1 (0.118); central nervous system cancer (0.118); glioma (0.105)
- **Europe PMC papers**: 5458
- **Why important**: SERPINA3 is the module's explicitly blood-secreted component and is linked to PLXNB2. HPA reports liver and pancreas tissue enrichment, astrocyte cell-type enrichment, and detection in bone marrow. Its established biology as a serine-protease inhibitor, together with inflammatory and cytokine-response annotations and extensive literature, gives it a plausible extracellular or inflammatory context.
- **Conclusion**: Established evidence supports SERPINA3 as a secreted protease-regulatory and inflammation-associated protein that could reflect circulating material or astrocyte-related biology. It is not established that SERPINA3 mechanistically regulates PLXNB2 or the other module members; that linkage is a hypothesis.

#### BPNT2

- **Related proteins** (co-abundance neighbors): HSPA13 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3'(2'), 5'-bisphosphate nucleotidase 2. This gene encodes a member of the inositol monophosphatase family. The encoded protein is localized to the Golgi apparatus and catalyzes the hydrolysis of phosphoadenosine phosphate (PAP) to adenosine monophosphate (AMP). Mutations in this gene are a cause of GRAPP type chondrodysplasia with joint dislocations, and a pseudogene of this gene is located on the long arm of chromosome 1. [provided by …
- **Diseases (Open Targets)**: chondrodysplasia with joint dislocations, gPAPP type (0.738); chronic kidney disease (0.316); breast disorder (0.294); liver disorder (0.288); ovarian neoplasm (0.288)
- **Europe PMC papers**: 63
- **Why important**: BPNT2 is connected to HSPA13 and supplies a defined Golgi metabolic function: hydrolysis of phosphoadenosine phosphate. It is annotated for phosphatidylinositol dephosphorylation and skeletal-system development, and its disease associations include gPAPP-type chondrodysplasia with joint dislocations. Although it has limited literature, its disease annotation gives it distinctive biological relevance.
- **Conclusion**: Established evidence supports BPNT2 as a Golgi-localized phosphatase with relevance to skeletal development and inherited chondrodysplasia. Its co-abundance with HSPA13 may indicate shared secretory or Golgi-related cell state, but a role in the complete module or in cross-tissue biology remains hypothetical.

## Module 1

**Tissue pair**: bone_marrow and cerebrospinal_fluid  
**Genes (5)**: A2M, GOT1, ATP1B1, SELL, SERPINF1

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. Therefore, this module does not support a statistically established single pathway or biological process. The gene annotations instead suggest a mixed extracellular, adhesion, transport, protease-regulatory, and metabolic signal. SERPINF1 and A2M support extracellular protease and inflammatory regulation; SELL supports leukocyte adhesion and migration; ATP1B1 supports transmembrane ion gradients; and GOT1 supports amino-acid and intermediary metabolism. The small co-abundance network may therefore reflect coordinated sample composition or cellular state rather than one canonical molecular pathway.

**Cell composition.** The module is heterogeneous rather than uniformly plasma-derived, secreted, blood-cell enriched, or housekeeping-like. SERPINF1 and A2M are secreted to blood, while SELL is enriched in bone marrow and lymphoid tissue and is associated with neutrophils. HPA evidence also links the genes to diverse tissues and cell types, including choroid plexus, lung, kidney, muscle, cardiomyocytes, fibroblasts, hepatocytes, mast cells, plasmacytoid dendritic cells, basophils, and gdT-cells. SELL has detected protein in bone marrow, whereas A2M and GOT1 were not detected there and several other measurements were unavailable. This mixture is consistent with possible contributions from blood or stromal and tissue-associated cells in the shared samples. The choroid-plexus enrichment of SERPINF1 is particularly compatible with a cerebrospinal-fluid-associated source, but it does not establish that the entire module originates there.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship reported within the module is between A2M and SERPINF1. This is consistent with both proteins being secreted extracellular regulators, but it does not demonstrate that all module members form one physical complex. The other co-abundance edges have no reported high-confidence STRING interaction support. No hu.MAP complex contains multiple module members. Thus, the network combines one supported extracellular relationship with additional expression covariation that may arise from shared cellular composition, coordinated regulation, or indirect biology.

**STRING interactions (score >= 0.7)**: 1 of 10 gene pairs: A2M–SERPINF1 (0.88)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module is a potentially interesting tissue-pair co-abundance observation, but it cannot be called a new molecular complex or a newly established pathway. The lack of globally significant GO/KEGG terms, the absence of STRING functional enrichment, the absence of a hu.MAP multi-member complex, and the limited STRING support argue against claiming a previously unknown coherent mechanism. Conversely, absence from STRING or hu.MAP alone does not prove novelty, because co-abundance relationships can reflect context-specific regulation, secretion, cell mixture, or tissue sampling that is not represented in those resources. Its most defensible novelty is the shared bone-marrow and cerebrospinal-fluid co-abundance pattern, which would require replication, cell-composition analysis, and independent experimental validation.

**Hypothesis.** Hypothesis: the module reflects a cross-tissue extracellular and cellular-composition program linking a choroid-plexus-associated secreted factor with circulating protease and inflammatory regulation, leukocyte trafficking, membrane ion handling, and metabolic state. SERPINF1 and A2M may form the extracellular regulatory component, while SELL may report bone-marrow leukocyte contribution and ATP1B1 and GOT1 may report membrane and metabolic states of contributing cells. This is a hypothesis rather than an established pathway, because global enrichment was negative and only the A2M-SERPINF1 relationship was supported by STRING.

### Important genes

#### SERPINF1

- **Related proteins** (co-abundance neighbors): SELL (0.90), GOT1 (0.86), ATP1B1 (0.84); STRING partners: A2M (0.88)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family F member 1. This gene encodes a member of the serpin family that does not display the serine protease inhibitory activity shown by many of the other serpin proteins. The encoded protein is secreted and strongly inhibits angiogenesis. In addition, this protein is a neurotrophic factor involved in neuronal differentiation in retinoblastoma cells. Mutations in this gene were found in individuals with osteogenesi…
- **Diseases (Open Targets)**: osteogenesis imperfecta (0.716); osteogenesis imperfecta, recessive (0.462); osteogenesis imperfecta type 3 (0.447); osteogenesis imperfecta type 4 (0.371); refractive error (0.348)
- **Europe PMC papers**: 2744
- **Why important**: SERPINF1 has the strongest network position in the module, connecting to SELL, GOT1, and ATP1B1. It is secreted to blood, is tissue enriched in choroid plexus, and has annotations involving inhibition of angiogenesis and neuronal projection development. It is also associated with osteogenesis imperfecta and has substantial literature coverage, making it the most informative candidate for linking the module to bone and cerebrospinal-fluid biology.
- **Conclusion**: Established evidence supports SERPINF1 as a secreted, noncanonical serpin with angiogenesis-inhibitory and neurotrophic functions, and as a protein associated with choroid plexus and skeletal disease. It is a plausible anchor for the module, but the co-abundance data do not establish that it drives the other genes or that it mediates a cerebrospinal-fluid mechanism.

#### A2M

- **Related proteins** (co-abundance neighbors): ATP1B1 (0.94); STRING partners: SERPINF1 (0.88)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alpha-2-macroglobulin. The protein encoded by this gene is a protease inhibitor and cytokine transporter. It uses a bait-and-trap mechanism to inhibit a broad spectrum of proteases, including trypsin, thrombin and collagenase. It can also inhibit inflammatory cytokines, and it thus disrupts inflammatory cascades. Mutations in this gene are a cause of alpha-2-macroglobulin deficiency. This gene is implicated in Alzheimer…
- **Diseases (Open Targets)**: myopia (0.206); refractive error (0.151); primary angle-closure glaucoma (0.148); Abnormality of refraction (0.144); Aganglionic megacolon (0.118)
- **Europe PMC papers**: 5133
- **Why important**: A2M is connected to ATP1B1 in the co-abundance network and has the sole reported high-confidence STRING relationship with SERPINF1. It is a secreted protease inhibitor and cytokine transporter with roles in inflammatory-cascade regulation, and its literature coverage is substantial. Its reported relationship with amyloid-beta clearance also makes it relevant to nervous-system contexts.
- **Conclusion**: Established evidence supports A2M as a broad extracellular protease and cytokine regulator and supports its physical or functional association with SERPINF1 in STRING. Its presence in this module may indicate extracellular inflammatory or proteostatic biology, but it does not prove disease involvement or a direct role in cerebrospinal-fluid handling.

#### SELL

- **Related proteins** (co-abundance neighbors): SERPINF1 (0.90); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: selectin L. This gene encodes a cell surface adhesion molecule that belongs to a family of adhesion/homing receptors. The encoded protein contains a C-type lectin-like domain, a calcium-binding epidermal growth factor-like domain, and two short complement-like repeats. The gene product is required for binding and subsequent rolling of leucocytes on endothelial cells, facilitating their migration into secondar…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.367); asthma (0.304); lymphatic system disorder (0.286); ankylosing spondylitis (0.202); atrial fibrillation (0.189)
- **Europe PMC papers**: 14927
- **Why important**: SELL is a network neighbor of SERPINF1 and is group enriched in bone marrow and lymphoid tissue, with cell-type enrichment in neutrophils. It encodes a leukocyte adhesion and homing receptor involved in leukocyte rolling, migration, and cytokine responses. Its extensive literature coverage and bone-marrow protein detection make it an important indicator of immune-cell contribution.
- **Conclusion**: Established evidence supports SELL as a leukocyte trafficking and adhesion molecule and supports a bone-marrow or immune-cell component to the module. The data do not show that SELL physically interacts with SERPINF1, so the edge is better interpreted as co-abundance or shared context than as a demonstrated complex.

#### ATP1B1

- **Related proteins** (co-abundance neighbors): A2M (0.94), SERPINF1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit beta 1. The protein encoded by this gene belongs to the family of Na+/K+ and H+/K+ ATPases beta chain proteins, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a vari…
- **Diseases (Open Targets)**: cardiovascular disorder (0.634); atrial fibrillation (0.606); congestive heart failure (0.601); heart failure (0.585); cardiac arrhythmia (0.536)
- **Europe PMC papers**: 2226
- **Why important**: ATP1B1 connects to both A2M and SERPINF1 in the module and encodes a subunit of the sodium-potassium ATPase. Its function in maintaining electrochemical gradients, ion transport, and cellular excitability provides a membrane and homeostatic dimension distinct from the secreted proteins. HPA links it to kidney and several epithelial cell types, while disease associations include cardiovascular disorders.
- **Conclusion**: Established evidence supports ATP1B1 as a membrane ion-homeostasis component with broad physiological relevance. Its network placement suggests coordinated expression with the extracellular portion of the module, but there is no STRING or hu.MAP evidence here establishing a shared complex or a direct mechanistic connection.

## Module 2

**Tissue pair**: bone_marrow and cerebrospinal_fluid  
**Genes (17)**: DBI, APOC3, ASPH, CACNA2D1, CTSC, C5, F10, GOLM1, HPX, ICAM5, IGHG1, IGHG4, MCAM, SEMA7A, SIL1, STMN2, AZGP1

### Function

No GO or KEGG term passed global correction, so there is no statistically established pathway-level annotation for this module. The gene-level evidence instead points to a mixed extracellular and cellular program. One axis is hepatic plasma homeostasis, including heme transport and protection from heme-associated oxidative stress through HPX, lipid and triglyceride handling through APOC3, and complement-mediated innate immunity through C5. A second axis involves neuronal structure and signaling, represented by STMN2, ICAM5, SEMA7A, and CACNA2D1. A third axis involves immune-cell proteolysis and protein maturation, represented by CTSC and the immunoglobulin genes. The co-abundance pattern therefore appears more consistent with coordinated representation of secreted blood proteins together with tissue- or cell-type-derived signals than with a single narrowly defined biochemical pathway.

**Cell composition.** The module is compositionally heterogeneous but strongly influenced by secreted or plasma-associated proteins. The HPA summary identifies many secreted genes, with liver and hepatocyte enrichment especially prominent; HPX, F10, C5, and APOC3 are secreted to blood or liver-enriched proteins. There is also a lymphoid and plasma-cell component through IGHG1 and IGHG4, and a neuronal component through ICAM5 and STMN2. Several genes are enriched in brain cell types, while others are associated with hepatocytes, adipocytes, or selected blood-cell populations. Most genes are not specifically detected in immune cells, so the module should not automatically be interpreted as a bone-marrow immune-cell program. Its presence in bone marrow and cerebrospinal fluid may instead reflect shared blood-derived protein content, variable vascular or barrier contribution, shared secretory material, and smaller contributions from neuronal or immune-associated cell populations. The lack of matching HPA cerebrospinal-fluid tissue data limits direct assessment of protein abundance in that compartment.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a small set of high-confidence pairwise relationships: APOC3 with DBI, ASPH with F10, and AZGP1 with HPX. These links support connections among lipid or acyl-chain biology, secreted heme and plasma proteins, and endoplasmic-reticulum or protein-processing biology, but STRING reports no supplementary functional enrichment for the module. hu.MAP provides repeated complex-level associations centered on C5, APOC3, and HPX. In particular, these genes recur together in several large plasma-protein and complement or coagulation-related complexes, while APOC3 and C5 also recur in complexes containing lipid carriers, complement components, coagulation factors, and acute-phase proteins. Because the complexes are large and only a subset of their members occurs in the module, hu.MAP supports a shared extracellular plasma-protein context rather than proving that the entire module is one physical complex. The sparse STRING network and the absence of hu.MAP assignments for many neuronal, membrane, and intracellular genes indicate that much of the co-abundance structure is not explained by already catalogued direct protein interactions.

**STRING interactions (score >= 0.7)**: 3 of 136 gene pairs: APOC3–DBI (0.755); ASPH–F10 (0.916); AZGP1–HPX (0.784)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08395.1 (C5, APOC3, HPX; 3/43); huMAP3_09531.1 (C5, APOC3, HPX; 3/47); huMAP3_10101.1 (C5, APOC3, HPX; 3/49); huMAP3_10678.1 (C5, APOC3, HPX; 3/71); huMAP3_00178.1 (C5, APOC3; 2/9); huMAP3_08796.1 (C5, APOC3; 2/15); huMAP3_09832.1 (C5, APOC3; 2/18); huMAP3_07541.1 (C5, APOC3; 2/19); huMAP3_09273.1 (APOC3, HPX; 2/28); huMAP3_15040.1 (APOC3, HPX; 2/64)

### Novelty

The module may represent a new cross-tissue co-abundance pattern, but the fact sheet does not establish novelty as a biological discovery. The strongest recurring elements, especially C5, APOC3, and HPX, are already embedded in known plasma-protein and complement-related complexes in hu.MAP, and several pairwise relationships are already present in STRING. Conversely, the coupling of these plasma-associated genes with neuronal markers such as STMN2 and ICAM5, ER or processing genes such as SIL1 and ASPH, and immune-associated genes such as CTSC and IGHG4 is not explained by the listed databases. This cross-tissue combination is therefore potentially interesting, but it requires replication in independent cohorts, control for blood contamination and cell composition, and comparison with established co-abundance modules before it can be called a new biological mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared extracellular and cellular state contributed by blood-derived hepatic proteins in both sample types, with additional signals from marrow-associated immune or plasma cells and cerebrospinal-fluid-associated neuronal material. In this model, APOC3 and HPX mark a circulating lipoprotein and heme-handling environment, C5 contributes innate immune and inflammatory potential, F10 and ASPH connect the pattern to coagulation and protein or calcium-processing biology, and STMN2, ICAM5, SEMA7A, and CACNA2D1 represent a neuronal or membrane-signaling component. SIL1 may connect the abundance pattern to endoplasmic-reticulum protein folding, while CTSC and the immunoglobulin genes may reflect protease-rich immune or plasma-cell contributions. This is a hypothesis rather than an enrichment-supported pathway assignment, because no GO or KEGG term achieved global significance and the module contains both secreted and cell-type-associated genes.

### Important genes

#### HPX

- **Related proteins** (co-abundance neighbors): SIL1 (0.99), APOC3 (0.83); STRING partners: AZGP1 (0.784)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_09273.1, huMAP3_15040.1
- **Function (MyGene.info)**: hemopexin. This gene encodes a plasma glycoprotein that binds heme with high affinity. The encoded protein is an acute phase protein that transports heme from the plasma to the liver and may be involved in protecting cells from oxidative stress. [provided by RefSeq, Apr 2009].
- **Diseases (Open Targets)**: panniculitis (0.116); neoplasm (0.107); familial idiopathic steroid-resistant nephrotic syndrome (0.101); hepatocellular carcinoma (0.101); focal segmental glomerulosclerosis (0.097)
- **Europe PMC papers**: 6894
- **Why important**: HPX is a liver-enriched, hepatocyte-associated secreted plasma protein that binds heme and transports it to the liver, with a role in protection from oxidative stress. It is directly connected to APOC3 in STRING and recurs with C5 and APOC3 across multiple hu.MAP complexes, making it a central representative of the module's recurring plasma-protein context. Its disease associations include neoplastic and renal disorders, and its literature volume is substantial.
- **Conclusion**: Established evidence supports HPX as a circulating heme-handling and hepatocyte-associated component of the module. It is plausible, but not established, that HPX helps explain the shared signal between bone marrow and cerebrospinal fluid through blood-derived protein contribution.

#### APOC3

- **Related proteins** (co-abundance neighbors): HPX (0.83); STRING partners: DBI (0.755)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_00178.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07541.1, huMAP3_09273.1, huMAP3_15040.1
- **Function (MyGene.info)**: apolipoprotein C3. This gene encodes a protein component of triglyceride (TG)-rich lipoproteins (TRLs) including very low density lipoproteins (VLDL), high density lipoproteins (HDL) and chylomicrons. The encoded protein plays a role in role in the metabolism of these TRLs through multiple modes. This protein has been shown to promote the secretion of VLDL1, inhibit lipoprotein lipase enzyme activity, and delay cata…
- **Diseases (Open Targets)**: apolipoprotein c-III deficiency (0.610); hypertriglyceridemia (0.598); coronary artery disorder (0.573); familial lipoprotein lipase deficiency (0.531); Hypercholesterolemia (0.523)
- **Europe PMC papers**: 5854
- **Why important**: APOC3 is a liver- and hepatocyte-enriched secreted apolipoprotein involved in triglyceride-rich lipoprotein metabolism, including inhibition of lipoprotein-lipase activity and delayed remnant clearance. It connects to DBI in STRING and repeatedly co-occurs with C5 and HPX in hu.MAP complexes, placing it at the intersection of lipid transport and the module's plasma-protein architecture. It has well-established links to hypertriglyceridemia and cardiovascular disease and a substantial literature base.
- **Conclusion**: Established evidence supports APOC3 as a marker of circulating lipid metabolism rather than as evidence for a neuronal pathway. Its co-abundance with neuronal and marrow-associated genes may reflect compartment mixing, shared extracellular material, or coordinated sample composition; a direct mechanistic bridge remains hypothetical.

#### C5

- **Related proteins** (co-abundance neighbors): DBI (0.90); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_00178.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07541.1
- **Function (MyGene.info)**: complement C5. This gene encodes a component of the complement system, a part of the innate immune system that plays an important role in inflammation, host homeostasis, and host defense against pathogens. The encoded preproprotein is proteolytically processed to generate multiple protein products, including the C5 alpha chain, C5 beta chain, C5a anaphylatoxin and C5b. The C5 protein is comprised of the C5 alpha…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.744); paroxysmal nocturnal hemoglobinuria (0.610); myasthenia gravis (0.586); atypical hemolytic-uremic syndrome (0.544); neuromyelitis optica (0.516)
- **Europe PMC papers**: 81450
- **Why important**: C5 is a liver-enriched secreted complement component with roles in complement activation, chemotaxis, inflammation, and host defense. It is connected in hu.MAP to several related plasma-protein complexes containing APOC3 and HPX, although it has no listed high-confidence STRING partner in this module. Its extensive disease literature includes complement deficiency, paroxysmal nocturnal hemoglobinuria, myasthenia gravis, atypical hemolytic-uremic syndrome, and neuromyelitis optica.
- **Conclusion**: Established evidence supports C5 as an innate-immune and plasma-protein component. Its presence does not demonstrate active complement signaling in either tissue; it may instead report circulating protein abundance or inflammatory state.

#### STMN2

- **Related proteins** (co-abundance neighbors): AZGP1 (0.97), ICAM5 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: stathmin 2. This gene encodes a member of the stathmin family of phosphoproteins. Stathmin proteins function in microtubule dynamics and signal transduction. The encoded protein plays a regulatory role in neuronal growth and is also thought to be involved in osteogenesis. Reductions in the expression of this gene have been associated with Down's syndrome and Alzheimer's disease. Alternatively spliced transcri…
- **Diseases (Open Targets)**: neurodegenerative disease (0.371); schizophrenia (0.313); intelligence (0.312); immune system disorder (0.307); alcohol drinking (0.275)
- **Europe PMC papers**: 2193
- **Why important**: STMN2 is brain-enriched and associated with excitatory and inhibitory neurons, and it regulates microtubule dynamics and neuronal projection development. It is connected to AZGP1 and ICAM5 in the module, providing a bridge between a neuronal signal and a secreted or adhesion-associated signal. It has established relevance to neuronal growth, Alzheimer's disease, and other neurodegenerative or neuropsychiatric traits, with a substantial literature base.
- **Conclusion**: Established evidence supports STMN2 as the clearest neuronal component of the module. Its co-abundance with liver-derived plasma proteins could reflect cerebrospinal-fluid neuronal material, shared cell composition, or sample handling; it does not by itself establish a functional interaction with APOC3 or HPX.

#### SIL1

- **Related proteins** (co-abundance neighbors): ASPH (1.00), HPX (0.99), F10 (0.99), AZGP1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SIL1 nucleotide exchange factor. This gene encodes a resident endoplasmic reticulum (ER), N-linked glycoprotein with an N-terminal ER targeting sequence, 2 putative N-glycosylation sites, and a C-terminal ER retention signal. This protein functions as a nucleotide exchange factor for another unfolded protein response protein. Mutations in this gene have been associated with Marinesco-Sjogren syndrome. Alternate transcriptional sp…
- **Diseases (Open Targets)**: Marinesco-Sjogren syndrome (0.810); hereditary neoplastic syndrome (0.554); hereditary diffuse gastric adenocarcinoma (0.551); Butterfly-shaped pigment dystrophy (0.516); colorectal cancer (0.483)
- **Europe PMC papers**: 929
- **Why important**: SIL1 has the highest weighted connectivity in the module and links ASPH, HPX, F10, and AZGP1. It is an endoplasmic-reticulum resident nucleotide-exchange factor involved in protein folding, cotranslational targeting, and intracellular protein transport. Its association with Marinesco-Sjogren syndrome and its large literature base make it an informative cellular-processing marker, even though it has no listed STRING or hu.MAP assignment.
- **Conclusion**: Established evidence supports SIL1 as an endoplasmic-reticulum protein-folding component and as a highly connected statistical bridge in this module. The possibility that it coordinates secretion or processing of the extracellular proteins is a hypothesis, not a demonstrated mechanism.

## Module 3

**Tissue pair**: bone_marrow and cerebrospinal_fluid  
**Genes (30)**: ADAM10, AFM, ALB, NAGLU, GLB1, CADM1, C3, DSG2, ECE1, FAT3, AHSG, HEXA, HYOU1, ICAM1, IGHG3, IGHM, JCHAIN, IGKC, ITGB2, CD58, MAN2B1, MBP, PILRA, SEMA4D, SLAMF7, SLITRK3, SORL1, TFRC, FAS, VTN

### Function

The module is best interpreted as a mixed blood, immune-cell adhesion, extracellular-serum, and lysosomal trafficking program rather than as a single conclusively defined biochemical pathway. Its strongest coherent biological signals are leukocyte adhesion and immune-cell interaction, represented by ICAM1, ITGB2, CD58, PILRA, SEMA4D, and related receptors, together with complement and extracellular matrix or plasma proteins such as C3, ALB, AHSG, and VTN. A second layer involves lysosomal and glycan turnover, supported by NAGLU, HEXA, GLB1, MAN2B1, and the hu.MAP assemblies (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Brain-associated genes including SLITRK3, FAT3, and MBP may reflect the cerebrospinal-fluid context, neural or glial biology, or shared extracellular material. No GO or KEGG term passed global correction, so these functional interpretations are based on gene annotations, network structure, HPA evidence, STRING relationships, and hu.MAP evidence rather than globally significant enrichment.

**Cell composition.** The module has a strong extracellular and blood-derived component. Many genes are secreted to blood or are liver-enriched plasma proteins, including ALB, AHSG, AFM, C3, and VTN; HPA also identifies many secreted genes overall. The repeated hu.MAP assemblies containing ALB, AHSG, and C3 (hu.MAP huMAP3_07432.1) through (hu.MAP huMAP3_07265.1) are consistent with serum protein co-occurrence or shared plasma-complex context. The module also has a substantial immune and blood-cell signature: HPA highlights neutrophils most frequently, with additional representation of plasma cells, macrophages, monocytes, and B-cell populations. IGHM, IGKC, IGHG3, and JCHAIN support immunoglobulin or plasma-cell material, while ICAM1, ITGB2, PILRA, SEMA4D, SLAMF7, and MAN2B1 support myeloid or leukocyte biology. Brain-enriched genes and cerebrospinal-fluid-associated material are present, but their co-abundance may reflect extracellular carryover, immune surveillance, or mixed cellular material rather than a dedicated neural pathway. The module therefore could partly reflect blood contamination, vascular or immune-cell content, and shared cell types across the sampled tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a connected serum and leukocyte-interaction subnetwork. ALB is linked to AHSG, C3, VTN, ICAM1, and TFRC; C3 is linked to ITGB2, ICAM1, and VTN; and ICAM1, ITGB2, CD58, and CADM1 form a known adhesion-related neighborhood. HEXA and GLB1 provide a lysosomal glycosidase relationship. These are established database relationships and make the module biologically interpretable, but they do not demonstrate that every co-abundant pair physically interacts or that the entire module is one complex. hu.MAP provides two lysosomal or glycoprotein-processing assemblies containing ADAM10, ECE1, NAGLU, and HYOU1 (hu.MAP huMAP3_06775.1) (hu.MAP huMAP3_09327.1). It also repeatedly places ALB, AHSG, and C3 within serum or complement-associated assemblies (hu.MAP huMAP3_07432.1) through (hu.MAP huMAP3_07265.1), and places ITGB2 with AFM in an immune-associated assembly (hu.MAP huMAP3_14295.1). Thus, the known relationships support several overlapping submodules: plasma and complement proteins, leukocyte adhesion, and intracellular glycan or lysosomal processing.

**STRING interactions (score >= 0.7)**: 18 of 435 gene pairs: AHSG–ALB (0.999); AHSG–C3 (0.7); AHSG–VTN (0.782); ALB–C3 (0.959); ALB–ICAM1 (0.709); ALB–TFRC (0.88); ALB–VTN (0.988); C3–ICAM1 (0.705); C3–ITGB2 (0.998); C3–VTN (0.79); CADM1–ICAM1 (0.773); CADM1–ITGB2 (0.816); CD58–ICAM1 (0.996); CD58–ITGB2 (0.778); GLB1–HEXA (0.959); ICAM1–ITGB2 (0.999); ICAM1–VTN (0.738); ITGB2–VTN (0.862)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (ADAM10, ECE1, NAGLU, HYOU1; 4/60); huMAP3_09327.1 (ADAM10, ECE1, NAGLU, HYOU1; 4/93); huMAP3_07432.1 (C3, AHSG, ALB; 3/18); huMAP3_09434.1 (C3, AHSG, ALB; 3/33); huMAP3_08395.1 (C3, AHSG, ALB; 3/43); huMAP3_09531.1 (C3, AHSG, ALB; 3/47); huMAP3_10101.1 (C3, AHSG, ALB; 3/49); huMAP3_15040.1 (C3, AHSG, ALB; 3/64); huMAP3_10678.1 (C3, AHSG, ALB; 3/71); huMAP3_02242.1 (C3, AHSG; 2/9); huMAP3_08700.1 (AHSG, ALB; 2/11); huMAP3_07265.1 (AHSG, ALB; 2/20); huMAP3_14295.1 (ITGB2, AFM; 2/38)

### Novelty

The exact co-abundance module may be a new observation in this tissue-pair analysis, but the underlying biology is not new. Its principal components and relationships are already represented in STRING and hu.MAP, especially the serum-protein, complement, adhesion, and lysosomal connections. The presence of brain-associated genes alongside blood and immune proteins could be a distinctive feature of this tissue-pair module, but the current evidence cannot determine whether that combination is biologically specific or caused by shared blood-derived material, cell mixtures, or technical factors. Lack of STRING or hu.MAP coverage for several genes does not establish novelty. A defensible conclusion is that this is a potentially novel co-abundance pattern built from largely established biological components, requiring replication and cell-type or compartment-specific validation before being called a new mechanism.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of circulating plasma and complement proteins with leukocyte adhesion, immune-cell trafficking, and lysosomal glycan-processing machinery that is shared between bone marrow and cerebrospinal fluid. In this model, serum proteins such as ALB, AHSG, C3, AFM, and VTN provide an extracellular background, while ICAM1, ITGB2, PILRA, SEMA4D, and related molecules mark immune-cell contact or retention. NAGLU, HEXA, GLB1, and MAN2B1 could represent glycoprotein and lysosomal turnover in myeloid, neural-support, or other secretory cells. The neural genes may indicate cerebrospinal-fluid or glial contribution, but this remains a hypothesis and should not be interpreted as evidence for a dedicated neuroimmune pathway without matched cell-type, protein-compartment, and perturbation data.

### Important genes

#### ICAM1

- **Related proteins** (co-abundance neighbors): FAT3 (1.00), SLITRK3 (1.00), PILRA (1.00), NAGLU (0.96), C3 (0.93); STRING partners: ALB (0.709), C3 (0.705), CADM1 (0.773), CD58 (0.996), ITGB2 (0.999), VTN (0.738)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: intercellular adhesion molecule 1. This gene encodes a cell surface glycoprotein which is typically expressed on endothelial cells and cells of the immune system. It binds to integrins of type CD11a / CD18, or CD11b / CD18 and is also exploited by Rhinovirus as a receptor. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.528); atrial fibrillation (0.407); vascular disorder (0.358); Crohn disease (0.340); lymphatic system disorder (0.285)
- **Europe PMC papers**: 19543
- **Why important**: ICAM1 is a central immune-adhesion anchor in the module and connects the module network to ITGB2, CD58, C3, CADM1, and VTN through STRING. HPA places it in immune-relevant myeloid contexts and detects it in bone marrow. Its established function in leukocyte adhesion, extravasation, and immune-cell interaction makes it a strong bridge between the co-abundance pattern and a plausible marrow or cerebrospinal-fluid immune interface.
- **Conclusion**: Established evidence supports ICAM1 as an immune-cell adhesion component and as a database-supported connector between complement, integrin, and adhesion proteins. It is plausible, but unproven, that ICAM1 helps organize the shared tissue-pair signal.

#### ITGB2

- **Related proteins** (co-abundance neighbors): SLITRK3 (1.00); STRING partners: C3 (0.998), CADM1 (0.816), CD58 (0.778), ICAM1 (0.999), VTN (0.862)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_14295.1
- **Function (MyGene.info)**: integrin subunit beta 2. This gene encodes an integrin beta chain, which combines with multiple different alpha chains to form different integrin heterodimers. Integrins are integral cell-surface proteins that participate in cell adhesion as well as cell-surface mediated signalling. The encoded protein plays an important role in immune response and defects in this gene cause leukocyte adhesion deficiency. Alternative spli…
- **Diseases (Open Targets)**: leukocyte adhesion deficiency 1 (0.827); psoriasis vulgaris (0.585); leukocyte adhesion deficiency (0.559); dry eye syndrome (0.556); psoriasis (0.490)
- **Europe PMC papers**: 6754
- **Why important**: ITGB2 is a canonical leukocyte integrin subunit with HPA enhancement in bone marrow and lymphoid tissue. It has strong STRING relationships with C3, ICAM1, CD58, CADM1, and VTN, and it appears in the immune-associated hu.MAP assembly with AFM (hu.MAP huMAP3_14295.1). Its disease association with leukocyte adhesion deficiency gives the gene direct mechanistic relevance to immune-cell trafficking and adhesion.
- **Conclusion**: Established evidence supports ITGB2 as a leukocyte adhesion and signaling component. The module may capture immune-cell abundance or activation, but co-abundance alone cannot establish altered ITGB2-mediated adhesion in either tissue.

#### C3

- **Related proteins** (co-abundance neighbors): SORL1 (0.96), ICAM1 (0.93), SLAMF7 (0.88); STRING partners: AHSG (0.7), ALB (0.959), ICAM1 (0.705), ITGB2 (0.998), VTN (0.79)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07432.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_02242.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a liver-enriched secreted complement protein and a major serum-associated module component. It connects through STRING to ITGB2, ICAM1, VTN, ALB, and AHSG, and it recurs with ALB and AHSG across multiple hu.MAP serum or complement assemblies (hu.MAP huMAP3_07432.1) through (hu.MAP huMAP3_07265.1). Its complement function and disease associations make it an important extracellular inflammatory anchor.
- **Conclusion**: Established evidence supports C3 as a circulating complement component that can connect immune recognition with extracellular serum biology. It is reasonable to hypothesize that complement-rich material contributes to the shared module, but the data do not show local complement activation.

#### ALB

- **Related proteins** (co-abundance neighbors): SLITRK3 (1.00), FAT3 (1.00), PILRA (1.00); STRING partners: AHSG (0.999), C3 (0.959), ICAM1 (0.709), TFRC (0.88), VTN (0.988)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_07432.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_08700.1, huMAP3_07265.1
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB is a liver-enriched protein secreted into blood and is the most prominent indicator of a plasma-derived component. It has strong STRING relationships with AHSG, C3, VTN, ICAM1, and TFRC and occurs repeatedly with AHSG and C3 in hu.MAP assemblies (hu.MAP huMAP3_07432.1) through (hu.MAP huMAP3_07265.1). Its network role is especially important for interpreting the module as potentially influenced by circulating protein abundance rather than solely by tissue-resident biology.
- **Conclusion**: Established evidence supports ALB as a plasma carrier and serum-complex marker. Its presence argues for caution: part of the shared signal may reflect blood or extracellular carryover rather than a tissue-specific functional program.

#### PILRA

- **Related proteins** (co-abundance neighbors): HEXA (1.00), FAS (1.00), VTN (1.00), HYOU1 (1.00), MAN2B1 (1.00), SORL1 (1.00), IGHM (1.00), ALB (1.00), TFRC (1.00), SEMA4D (1.00), MBP (1.00), JCHAIN (1.00), DSG2 (1.00), ICAM1 (1.00), AHSG (1.00); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: paired immunoglobin like type 2 receptor alpha. Cell signaling pathways rely on a dynamic interaction between activating and inhibiting processes. SHP-1-mediated dephosphorylation of protein tyrosine residues is central to the regulation of several cell signaling pathways. Two types of inhibitory receptor superfamily members are immunoreceptor tyrosine-based inhibitory motif (ITIM)-bearing receptors and their non-ITIM-bearing, activating counte…
- **Diseases (Open Targets)**: Alzheimer disease (0.513); dementia (0.434); late-onset Alzheimers disease (0.149); neurodegenerative disease (0.121); atrial fibrillation (0.076)
- **Europe PMC papers**: 1170
- **Why important**: PILRA is highly connected within the co-abundance network and is HPA-enriched in neutrophils and enhanced in non-classical monocytes, with detection in bone marrow. Its annotated inhibitory immunoreceptor function places it at the interface of myeloid-cell signaling and immune regulation. Although it lacks STRING partners in the supplied evidence, its connections to HEXA, FAS, VTN, HYOU1, MAN2B1, SORL1, IGHM, and ALB make it an important network bridge.
- **Conclusion**: Established evidence supports PILRA as a myeloid-associated inhibitory receptor. Its position suggests a possible role in coordinating the immune and extracellular portions of the module, but that coordinating role is a hypothesis rather than a demonstrated molecular interaction.

#### NAGLU

- **Related proteins** (co-abundance neighbors): TFRC (1.00), SEMA4D (0.97), IGHM (0.97), ICAM1 (0.96), GLB1 (0.91), FAS (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: N-acetyl-alpha-glucosaminidase. This gene encodes an enzyme that degrades heparan sulfate by hydrolysis of terminal N-acetyl-D-glucosamine residues in N-acetyl-alpha-D-glucosaminides. Defects in this gene are the cause of mucopolysaccharidosis type IIIB (MPS-IIIB), also known as Sanfilippo syndrome B. This disease is characterized by the lysosomal accumulation and urinary excretion of heparan sulfate. [provided by RefSeq, Jul 20…
- **Diseases (Open Targets)**: mucopolysaccharidosis type 3B (0.870); Charcot-Marie-Tooth disease axonal type 2V (0.734); mucopolysaccharidosis type 3 (0.723); hereditary disease (0.532); Abnormality of metabolism/homeostasis (0.455)
- **Europe PMC papers**: 1140
- **Why important**: NAGLU links the immune-facing portion of the network to lysosomal and glycan-processing biology. It connects to TFRC, SEMA4D, IGHM, ICAM1, GLB1, and FAS, and it occurs with ADAM10, ECE1, and HYOU1 in both hu.MAP assemblies (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Its established role in heparan-sulfate degradation and its disease association with mucopolysaccharidosis type three B provide a mechanistic rationale for a lysosomal turnover component.
- **Conclusion**: Established evidence supports NAGLU as a lysosomal glycan-degradation enzyme and as a member of hu.MAP assemblies containing several module genes. The hypothesis that lysosomal processing links immune and cerebrospinal-fluid biology is plausible but not established by this co-abundance module.

## Module 4

**Tissue pair**: bone_marrow and cerebrospinal_fluid  
**Genes (9)**: ADA2, COL6A1, COL6A3, COL12A1, ENDOD1, F5, FN1, MFGE8, ROBO1

### Function

The module is most consistent with an extracellular-matrix and vascular or stromal interface module, with a secondary contribution from circulating coagulation and immune-associated proteins. The strongest structural signal is the coordinated presence of COL6A1, COL6A3, COL12A1, FN1, and MFGE8. COL6A1 and COL6A3 form collagen-six structural components, COL12A1 is a fibril-associated collagen, FN1 supports cell-matrix adhesion and migration, and MFGE8 supports apoptotic-cell clearance and tissue repair. F5 and ADA2 add plausible blood-borne and inflammatory context, while ROBO1 and ENDOD1 are less directly connected to the matrix pattern. No GO or KEGG term passed global correction; therefore the functional interpretation is based on gene annotations, network structure, HPA evidence, STRING relationships, and hu.MAP evidence rather than statistically significant enrichment.

**Cell composition.** The module is predominantly composed of secreted or extracellular-matrix proteins. HPA identifies most module genes as secreted, with several enriched in fibroblasts, smooth-muscle cells, hepatic stellate cells, or stromal cell types. Five genes are not detected in immune cells, and the remaining immune-related signals are limited or cell-context specific. FN1, F5, ADA2, and MFGE8 are secreted to blood, whereas COL6A1, COL6A3, and COL12A1 are secreted to extracellular matrix. Bone-marrow protein detection is present for several genes, while there is no matching HPA cerebrospinal-fluid tissue category. Thus, the shared signal could reflect extracellular matrix, vascular or stromal material, and blood-derived protein content in the sampled material, rather than a specialized cerebrospinal-fluid cellular program. The HPA profile does not support interpreting this primarily as a broad immune-cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a coherent collagen and matrix subnetwork: COL6A1 is strongly connected with COL6A3, and both connect with COL12A1; COL6A1 and COL6A3 also connect with FN1. These relationships are concordant with established collagen and fibronectin biology and indicate that part of the module recapitulates known extracellular-matrix organization. hu.MAP provides an independent complex-level connection through (hu.MAP huMAP3_13038.1), which contains COL6A3 and COL12A1 among a larger collagen-and matrix-related complex. ADA2, F5, ENDOD1, and ROBO1 do not have reported STRING partners or hu.MAP complexes within the supplied evidence. The known relationships support biological coherence for the matrix core, but they do not establish that the entire module is a single physical complex or a single pathway.

**STRING interactions (score >= 0.7)**: 5 of 36 gene pairs: COL12A1–COL6A1 (0.781); COL12A1–COL6A3 (0.788); COL6A1–COL6A3 (0.994); COL6A1–FN1 (0.78); COL6A3–FN1 (0.736)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13038.1 (COL6A3, COL12A1; 2/40)

### Novelty

This module should not be called a wholly new molecular system. Its central collagen and fibronectin relationships are already represented by STRING and the collagen-related hu.MAP complex (hu.MAP huMAP3_13038.1), and the functions of the principal genes are well established. A potentially novel aspect is the co-abundance of this matrix core with blood-secreted proteins such as F5 and ADA2, the clearance factor MFGE8, and the less characterized ENDOD1 signal across bone marrow and cerebrospinal fluid. However, absence of some genes from STRING or hu.MAP does not prove novelty. The appropriate conclusion is that the cross-tissue co-abundance pattern may be a new observational association, while its main molecular components and several pairwise relationships are already known.

**Hypothesis.** Hypothesis: the module represents a shared extracellular compartment or stromal-vascular remodeling program sampled in both bone marrow and cerebrospinal fluid. A collagen-six scaffold involving COL6A1 and COL6A3, modified or positioned by COL12A1 and FN1, could provide a matrix environment that supports adhesion, migration, tissue repair, and vascular interaction. MFGE8 could link this matrix environment to apoptotic-cell clearance and repair, while ADA2 and F5 could reflect co-sampled blood-borne inflammatory and coagulation context. ENDOD1 and ROBO1 may mark an additional platelet, membrane, or migratory component, but their role in the shared module remains uncertain. This hypothesis requires validation with cellular deconvolution, matched cerebrospinal-fluid protein measurements, and independent cohorts.

### Important genes

#### COL6A3

- **Related proteins** (co-abundance neighbors): MFGE8 (0.85), COL12A1 (0.83), COL6A1 (0.81); STRING partners: COL12A1 (0.788), COL6A1 (0.994), FN1 (0.736)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_13038.1
- **Function (MyGene.info)**: collagen type VI alpha 3 chain. This gene encodes the alpha-3 chain, one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The alpha-3 chain of type VI collagen is much larger than the alpha-1 and -2 chains. This difference in size is largely due to an increase in the number of subdomains, similar to von Willebrand Factor type A domains, that are found in the amino termin…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy (0.766); dystonia 27 (0.764); Bethlem myopathy (0.758); Bethlem myopathy 1C (0.747); Bethlem myopathy 1A (0.718)
- **Europe PMC papers**: 5386
- **Why important**: COL6A3 is one of the most connected genes in the module and directly links MFGE8, COL12A1, and COL6A1. It is an extracellular-matrix collagen, is associated with fibroblasts, stromal cells, and hepatic stellate cells in HPA, participates in the hu.MAP complex (hu.MAP huMAP3_13038.1), and has established links to collagen-six myopathies. Its substantial literature supports a central structural interpretation.
- **Conclusion**: Established: COL6A3 is a plausible structural anchor of the matrix core, supported by its network position, HPA localization, STRING relationships, and hu.MAP membership. Hypothesis: its co-abundance in both tissues may mark shared stromal or vascular matrix material rather than local synthesis by a common cell type.

#### COL6A1

- **Related proteins** (co-abundance neighbors): MFGE8 (0.83), COL12A1 (0.83), COL6A3 (0.81); STRING partners: COL12A1 (0.781), COL6A3 (0.994), FN1 (0.78)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is highly connected to COL6A3, COL12A1, and MFGE8 and forms part of the collagen-six structural unit. HPA places it in fibroblast and fibro-adipogenic cell contexts and does not detect it in immune cells. Its annotations include tissue development, cell differentiation, and osteoblast differentiation, and it has extensive disease and literature support through collagen-six myopathies.
- **Conclusion**: Established: COL6A1 is a core extracellular-matrix component whose co-abundance with COL6A3 is strongly biologically interpretable. Hypothesis: the module may reflect matrix turnover or remodeling relevant to marrow stroma and barrier-associated tissue interfaces.

#### FN1

- **Related proteins** (co-abundance neighbors): ADA2 (1.00), MFGE8 (0.86); STRING partners: COL6A1 (0.78), COL6A3 (0.736)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 connects the matrix arm to ADA2 and MFGE8 and has STRING support with COL6A1 and COL6A3. It is a secreted plasma and extracellular-matrix glycoprotein involved in adhesion, migration, wound healing, coagulation, and host defense. HPA associates it with blood vessel, liver, placenta, fibroblast, hepatic stellate, and trophoblast contexts. Its very large literature base and disease associations make it an important anchor, although its broad biology reduces specificity.
- **Conclusion**: Established: FN1 is a plausible integrator of matrix, vascular, and blood-derived signals in this module. Hypothesis: FN1 may help explain why a stromal matrix signature is detectable across the two sampled tissue groups.

#### MFGE8

- **Related proteins** (co-abundance neighbors): FN1 (0.86), COL6A3 (0.85), COL6A1 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: milk fat globule EGF and factor V/VIII domain containing. This gene encodes a preproprotein that is proteolytically processed to form multiple protein products. The major encoded protein product, lactadherin, is a membrane glycoprotein that promotes phagocytosis of apoptotic cells. This protein has also been implicated in wound healing, autoimmune disease, and cancer. Lactadherin can be further processed to form a smaller cleavage product, medin, which c…
- **Diseases (Open Targets)**: AL amyloidosis (0.462); angina pectoris (0.339); myocardial ischemia (0.333); coronary artery bypass (0.314); coronary atherosclerosis (0.312)
- **Europe PMC papers**: 2623
- **Why important**: MFGE8 has a central network position, linking FN1 with COL6A1 and COL6A3. It is secreted to blood, enriched in a vascular context, and associated with fibroblasts, pericytes, and stromal cell types in HPA. Its annotated role in apoptotic-cell clearance, together with reported roles in wound healing, autoimmune disease, and cancer, provides a functional bridge between matrix organization and tissue remodeling.
- **Conclusion**: Established: MFGE8 is a credible repair and clearance-related component of the matrix-associated module. Hypothesis: it may couple extracellular matrix material to removal of apoptotic cells or remodeling in marrow and vascular interfaces.

#### F5

- **Related proteins** (co-abundance neighbors): ADA2 (1.00), ENDOD1 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coagulation factor V. This gene encodes an essential cofactor of the blood coagulation cascade. This factor circulates in plasma, and is converted to the active form by the release of the activation peptide by thrombin during coagulation. This generates a heavy chain and a light chain which are held together by calcium ions. The activated protein is a cofactor that participates with activated coagulation factor X to ac…
- **Diseases (Open Targets)**: thrombophilia due to activated protein C resistance (0.796); congenital factor V deficiency (0.777); factor V deficiency (0.768); ischemic stroke (0.662); venous thromboembolism (0.603)
- **Europe PMC papers**: 25771
- **Why important**: F5 connects ADA2 and ENDOD1 and is a secreted blood protein with HPA enrichment in choroid plexus, liver, placenta, and several blood-cell contexts. It is an essential coagulation cofactor with extensive disease and literature support. Its inclusion broadens the module beyond a pure collagen network and is particularly relevant when interpreting shared signals between marrow and cerebrospinal-fluid samples.
- **Conclusion**: Established: F5 is a biologically meaningful blood and coagulation marker within the module. Hypothesis: its co-abundance may reflect plasma exposure, vascular leakage, or shared blood-derived material rather than direct incorporation into the collagen matrix.

## Module 5

**Tissue pair**: bone_marrow and cerebrospinal_fluid  
**Genes (5)**: AGRN, B2M, CD47, FUCA2, CHGB

### Function

No GO or KEGG term passed global correction, and there are no supplementary STRING enrichment terms. The module therefore does not support a specific pathway-level functional assignment. Its components instead suggest a mixed extracellular, secretory, vesicular, membrane-signaling, and immune-associated profile. FUCA2 and B2M are secreted to blood; CHGB is associated with secretory vesicles and neuroendocrine cells; AGRN is an extracellular-matrix protein with synaptic and receptor-signaling roles; and CD47 is a broadly distributed plasma-membrane signaling protein. The co-abundance structure is centered on FUCA2, which connects to CD47, CHGB, and B2M, while CHGB connects to AGRN. This pattern is more consistent with a context-dependent abundance module than with a demonstrated unified biochemical pathway.

**Cell composition.** The module is compositionally biased toward secreted or extracellularly released proteins, with FUCA2, B2M, and AGRN having secreted or extracellular roles. CHGB is associated with secretory vesicles, whereas CD47 is a plasma-membrane protein. HPA indicates low tissue specificity for several genes and tissue enhancement in endocrine, brain, or parathyroid contexts for others. All module genes show cell-type enhancement, but the highlighted cell types span stromal, endocrine, renal epithelial, podocyte, neuronal, and immune-related populations rather than a single lineage. HPA does not indicate a strong blood-cell-specific signature, and several genes are not detected in immune cells. The module may therefore reflect shared secretory, stromal, epithelial, endocrine, or neural material in the samples rather than a blood-cell program. Bone-marrow protein detection is present for part of the module, while there is no matching HPA tissue for cerebrospinal fluid.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no hu.MAP complex containing multiple module members. The observed co-abundance edges are therefore not supported here by established physical interaction evidence. The absence of STRING and hu.MAP support argues against interpreting the module as a known stable protein complex. It does not exclude indirect regulation, shared cellular origin, co-secretion, extracellular carryover, or condition-dependent interactions. Existing functional annotations nevertheless provide established roles for the individual genes: FUCA2 in fucose and glycoprotein carbohydrate metabolism, CHGB in secretory endocrine and neuronal biology, CD47 in adhesion and membrane signaling, AGRN in extracellular-matrix and neuromuscular-junction biology, and B2M in MHC-associated antigen presentation and immune regulation.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is plausibly a new tissue-pair co-abundance observation, because the particular module is not represented as a known STRING interaction group or hu.MAP complex. However, those database absences do not establish biological novelty. The genes individually have well-established functions and substantial prior literature, while their mixed secretory, extracellular, endocrine, neural, epithelial, and immune associations provide plausible non-novel explanations for co-abundance. A defensible claim is therefore that the shared bone-marrow and cerebrospinal-fluid association is potentially novel as a statistical module, but a novel molecular mechanism or complex has not been demonstrated. Replication across independent cohorts, adjustment for cellular composition, and targeted measurement of the proteins would be needed to support novelty.

**Hypothesis.** Hypothesis: the module reflects coordinated variation in secreted and extracellular material contributed by differing cellular sources, with FUCA2 and B2M representing circulating or released proteins, CHGB representing secretory-vesicle activity, and AGRN representing extracellular-matrix or synaptic-associated material. CD47 may track the abundance or state of the membrane-bearing cells that contribute this material. In this model, the network is generated primarily by shared sample composition, secretion, or extracellular persistence rather than by a single intracellular pathway or stable multiprotein complex. This hypothesis predicts that the module will weaken after adjustment for cellular composition and may correlate with independent measures of secretory or extracellular protein content.

### Important genes

#### FUCA2

- **Related proteins** (co-abundance neighbors): CD47 (1.00), CHGB (0.99), B2M (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alpha-L-fucosidase 2. This gene encodes a plasma alpha-L-fucosidase, which represents 10-20% of the total cellular fucosidase activity. The protein is a member of the glycosyl hydrolase 29 family, and catalyzes the hydrolysis of the alpha-1,6-linked fucose joined to the reducing-end N-acetylglucosamine of the carbohydrate moieties of glycoproteins. This enzyme is essential for Helicobacter pylori adhesion to human gast…
- **Diseases (Open Targets)**: asthma (0.363); chronic rhinosinusitis (0.362); inflammatory bowel disease (0.361); Precordial pain (0.271); major salivary gland cancer (0.180)
- **Europe PMC papers**: 364
- **Why important**: FUCA2 is the network hub-like member, connecting to CD47, CHGB, and B2M. It encodes a plasma alpha-L-fucosidase involved in glycoprotein carbohydrate and fucose metabolism, and HPA classifies it as secreted to blood with tissue enhancement in parathyroid gland. Its central position and secreted biochemical role make it a strong candidate for driving or reporting the module's extracellular abundance pattern. It also has disease associations involving inflammatory and airway disorders and a substantial literature base.
- **Conclusion**: Established evidence supports FUCA2 as a secreted carbohydrate-processing enzyme and the most structurally central module member. It is a plausible marker of extracellular or plasma-derived material. It is not established that FUCA2 mechanistically regulates the other module genes; that interpretation remains a hypothesis.

#### CHGB

- **Related proteins** (co-abundance neighbors): FUCA2 (0.99), AGRN (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromogranin B. This gene encodes a tyrosine-sulfated secretory protein abundant in peptidergic endocrine cells and neurons. This protein may serve as a precursor for regulatory peptides. [provided by RefSeq, Jan 2009].
- **Diseases (Open Targets)**: Meniere disease (0.190); prostate cancer (0.112); Familial prostate cancer (0.112); placenta praevia (0.112); hypertensive disorder (0.111)
- **Europe PMC papers**: 1555
- **Why important**: CHGB connects FUCA2 and AGRN and is the module's clearest secretory-vesicle and neuroendocrine-associated component. It encodes chromogranin B, a secretory protein abundant in peptidergic endocrine cells and neurons and potentially serving as a precursor for regulatory peptides. HPA shows enhancement in adrenal, brain, and pituitary tissues and in several endocrine or neuroendocrine cell types. Its extensive literature makes it an informative indicator of secretory-cell contribution.
- **Conclusion**: Established evidence supports CHGB as a marker of endocrine and neuronal secretory biology. Its connection to AGRN is consistent with a possible neural or secretory context, but the module data do not establish a direct CHGB–AGRN mechanism or prove that neural tissue is the source in either sample type.

#### CD47

- **Related proteins** (co-abundance neighbors): FUCA2 (1.00); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD47 molecule. This gene encodes a membrane protein, which is involved in the increase in intracellular calcium concentration that occurs upon cell adhesion to extracellular matrix. The encoded protein is also a receptor for the C-terminal cell binding domain of thrombospondin, and it may play a role in membrane transport and signal transduction. This gene has broad tissue distribution, and is reduced in express…
- **Diseases (Open Targets)**: myelodysplastic syndrome (0.370); smoking initiation (0.341); Abnormality of refraction (0.295); hypothyroidism (0.280); systemic lupus erythematosus (0.279)
- **Europe PMC papers**: 20803
- **Why important**: CD47 is directly connected to FUCA2 and occupies a biologically distinctive membrane-signaling position in the module. It is broadly distributed, localized to the plasma membrane, and associated with adhesion, migration, calcium-related signaling, and regulation of immune cytokine responses. HPA detects it in bone marrow and shows low tissue specificity, while its disease associations include myelodysplastic syndrome and systemic lupus erythematosus. Its very large literature base supports strong prior knowledge of its biology.
- **Conclusion**: Established evidence supports CD47 as a broadly expressed cell-surface signaling and adhesion molecule that can report cellular composition. The co-abundance link to FUCA2 may reflect shared source-cell abundance or association with released material; a direct functional relationship between CD47 and FUCA2 is not established here.

#### AGRN

- **Related proteins** (co-abundance neighbors): CHGB (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: agrin. This gene encodes one of several proteins that are critical in the development of the neuromuscular junction (NMJ), as identified in mouse knock-out studies. The encoded protein contains several laminin G, Kazal type serine protease inhibitor, and epidermal growth factor domains. Additional post-translational modifications occur to add glycosaminoglycans and disulfide bonds. In one family with con…
- **Diseases (Open Targets)**: congenital myasthenic syndrome 8 (0.793); congenital myasthenic syndrome (0.680); presynaptic congenital myasthenic syndrome (0.652); postsynaptic congenital myasthenic syndrome (0.626); COVID-19 (0.546)
- **Europe PMC papers**: 2731
- **Why important**: AGRN connects to CHGB and provides the module's strongest extracellular-matrix and synaptic-development interpretation. It encodes agrin, a multidomain protein involved in neuromuscular-junction development, cell-surface receptor signaling, cytoskeletal organization, and synaptic transmission. HPA shows enhancement in several renal epithelial and podocyte populations, and its disease associations include congenital myasthenic syndromes. Its literature supports substantial prior knowledge while its network placement links it to the secretory CHGB branch.
- **Conclusion**: Established evidence supports AGRN as an extracellular and synaptic or neuromuscular-junction-associated protein, with additional epithelial expression. Its module association may indicate shared extracellular material or cellular-source variation. A functional role for AGRN in a bone-marrow–cerebrospinal-fluid module is not demonstrated and should remain hypothetical.

#### B2M

- **Related proteins** (co-abundance neighbors): FUCA2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Plasma membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: beta-2-microglobulin. This gene encodes a serum protein found in association with the major histocompatibility complex (MHC) class I heavy chain on the surface of nearly all nucleated cells. The protein has a predominantly beta-pleated sheet structure that can form amyloid fibrils in some pathological conditions. The encoded antimicrobial protein displays antibacterial activity in amniotic fluid. A mutation in this gen…
- **Diseases (Open Targets)**: MHC class I deficiency (0.656); diffuse large B-cell lymphoma (0.595); HIV infectious disease (0.532); amyloidosis, hereditary systemic 6 (0.528); AL amyloidosis (0.468)
- **Europe PMC papers**: 25100
- **Why important**: B2M is connected to FUCA2 and is a secreted-to-blood component of the MHC class I system. It is broadly associated with nucleated cells and has roles in antigen presentation and immune regulation. HPA detects it in bone marrow, shows low tissue specificity, and reports enhancement across diverse cell types including antigen-presenting and stromal populations. Its extensive literature and disease associations involving immune deficiency, lymphoma, HIV infection, and amyloidosis make it an important biological and clinical anchor.
- **Conclusion**: Established evidence supports B2M as a broadly distributed immune-associated serum protein and a potential indicator of cellular or inflammatory composition. Its co-abundance with FUCA2 may reflect shared release into extracellular fluid rather than a direct interaction. The module does not justify assigning a specific immune mechanism to B2M.

## Module 6

**Tissue pair**: bone_marrow and cerebrospinal_fluid  
**Genes (27)**: ALDOC, SERPINC1, APOH, BASP1, CD99L2, CADM3, ALCAM, CD44, CFB, CFH, CLIC1, FAM3C, ICOSLG, IGF2, IGHA2, ITIH1, LDHA, LDHB, LRP1, MDH1, PGK1, PLD4, PLOD2, PROS1, GM2A, SELENBP1, TXN

### Function

No GO or KEGG term passed global correction, so the module does not have a statistically established pathway annotation from those analyses. The gene-level evidence instead supports a mixed biological signal. One component is extracellular plasma and innate-defense biology, represented by complement factor B, complement factor H, antithrombin, protein S, apolipoprotein H, and inter-alpha-trypsin inhibitor heavy chain one, with support from STRING links such as CFB–CFH and SERPINC1–APOH and from the hu.MAP assemblies (hu.MAP huMAP3_15040.1) and (hu.MAP huMAP3_10678.1). A second component is cellular adhesion and immune or stromal interaction, represented by CD44, ALCAM, ICOSLG, CADM3, and LRP1. A third component is central carbon metabolism, represented by LDHA, LDHB, ALDOC, PGK1, and MDH1, with STRING support for ALDOC–LDHA, ALDOC–PGK1, and LDHA–PGK1. Thus, the most defensible interpretation is a composite extracellular homeostasis and cell-interaction module with a glycolytic or metabolic substructure, rather than a single proven pathway.

**Cell composition.** The module is strongly influenced by secreted and plasma-associated proteins: many genes are secreted to blood or encode immunoglobulin, complement, coagulation, or extracellular matrix-related proteins. HPA identifies liver and hepatocyte enrichment for several prominent genes, including ITIH1, SERPINC1, CFB, APOH, and CFH, while PROS1 is enriched in liver and choroid plexus. The module also contains brain-associated or neural-interface genes, including CADM3, ALDOC, BASP1, and PLD4, as well as immune or hematopoietic-associated genes such as ICOSLG, CD44, ALCAM, IGHA2, and PLD4. HPA additionally shows bone-marrow protein detection for a subset of the module, but not for many of the liver-derived secreted proteins. This composition makes shared blood contamination, vascular or choroid-plexus exposure, extracellular carryover, or shared cell types plausible contributors to the co-abundance pattern. It should not be interpreted as evidence that every gene is produced by the same cell population in both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a limited but biologically coherent set of high-confidence relationships. The complement pair CFB–CFH supports an alternative-complement connection; APOH–SERPINC1 and PROS1–SERPINC1 support a coagulation and plasma-protein connection; ALCAM–CD44 supports adhesion; and the ALDOC, LDHA, and PGK1 links support a glycolytic connection. These known relationships validate parts of the module but do not explain all of its edges. hu.MAP provides stronger support for the plasma-protein component than for a single unified complex. CFB, CFH, ITIH1, SERPINC1, and APOH recur in the large extracellular or plasma-associated assemblies (hu.MAP huMAP3_15040.1) and (hu.MAP huMAP3_10678.1), while LDHA and LDHB recur together in the lactate-dehydrogenase assemblies (hu.MAP huMAP3_06798.1), (hu.MAP huMAP3_09010.1), (hu.MAP huMAP3_14812.1), and (hu.MAP huMAP3_12061.1). CFB and ITIH1 also recur in several broader extracellular assemblies (hu.MAP huMAP3_06724.1) and (hu.MAP huMAP3_08796.1) through (hu.MAP huMAP3_10101.1). The module therefore contains known subnetwork structure, but its full co-abundance pattern is broader than any one established complex.

**STRING interactions (score >= 0.7)**: 8 of 351 gene pairs: ALCAM–CD44 (0.859); ALDOC–LDHA (0.93); ALDOC–PGK1 (0.835); APOH–SERPINC1 (0.944); CD44–SERPINC1 (0.716); CFB–CFH (0.961); LDHA–PGK1 (0.923); PROS1–SERPINC1 (0.743)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (CFB, SERPINC1, APOH, CFH, ITIH1; 5/64); huMAP3_10678.1 (CFB, CFH, ITIH1; 3/71); huMAP3_06798.1 (LDHA, LDHB; 2/3); huMAP3_09010.1 (LDHA, LDHB; 2/5); huMAP3_14812.1 (LDHA, LDHB; 2/5); huMAP3_06724.1 (CFB, ITIH1; 2/6); huMAP3_12061.1 (LDHA, LDHB; 2/6); huMAP3_08796.1 (CFB, ITIH1; 2/15); huMAP3_09832.1 (CFB, ITIH1; 2/18); huMAP3_07701.1 (CFB, ITIH1; 2/22); huMAP3_09273.1 (CFB, ITIH1; 2/28); huMAP3_08395.1 (CFB, ITIH1; 2/43); huMAP3_09531.1 (CFB, ITIH1; 2/47); huMAP3_10101.1 (CFB, ITIH1; 2/49)

### Novelty

This module should not be called a wholly new molecular complex or a newly discovered pathway. Its principal components are already represented by established complement, coagulation, plasma-protein, adhesion, and glycolytic relationships in STRING and hu.MAP. The potentially novel aspect is the cross-tissue co-abundance organization linking these components in bone marrow and cerebrospinal fluid, especially the combination of liver-derived circulating proteins with brain-associated adhesion or metabolic genes. However, absence of a complete matching interaction network in STRING or hu.MAP would not prove novelty. The result could reflect coordinated abundance of proteins from blood, choroid plexus, extracellular vesicles, or mixed cellular material. A claim of novelty would require independent cohorts, cell- and compartment-resolved measurements, and comparison with previously published tissue-pair modules.

**Hypothesis.** Hypothesis: the module reflects a shared extracellular-interface state in which circulating liver-derived complement, coagulation, and matrix-stabilizing proteins co-vary with adhesion receptors and metabolic proteins contributed by hematopoietic, vascular, choroid-plexus, glial, or other tissue-associated cells. In bone marrow, this may arise from blood and immune-cell exposure together with stromal interactions; in cerebrospinal fluid, it may arise from plasma-interface permeability, choroid-plexus production, extracellular vesicles, or local neural-support cells. The glycolytic subnetwork could indicate the metabolic state of contributing cells, but this is a hypothesis rather than proof that glycolysis mechanistically drives the plasma-protein component. A useful test would be matched plasma, cerebrospinal fluid, and bone-marrow measurements with cell-type deconvolution, assessment of blood contamination, and targeted validation of complement, coagulation, adhesion, and glycolytic proteins.

### Important genes

#### IGF2

- **Related proteins** (co-abundance neighbors): GM2A (0.99), MDH1 (0.98), CFB (0.98), BASP1 (0.97), LDHA (0.97), FAM3C (0.96), ITIH1 (0.95), PGK1 (0.92), ALCAM (0.92), LDHB (0.90), CD44 (0.90), APOH (0.83), TXN (0.82), ALDOC (0.81), PROS1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor 2. This gene encodes a member of the insulin family of polypeptide growth factors, which are involved in development and growth. It is an imprinted gene, expressed only from the paternal allele, and epigenetic changes at this locus are associated with Wilms tumour, Beckwith-Wiedemann syndrome, rhabdomyosarcoma, and Silver-Russell syndrome. A read-through INS-IGF2 gene exists, whose 5' region overlaps…
- **Diseases (Open Targets)**: Silver-Russell syndrome due to a point mutation (0.716); Silver-Russell syndrome (0.685); Beckwith-Wiedemann syndrome (0.594); diabetes mellitus, permanent neonatal 4 (0.479); maturity-onset diabetes of the young type 10 (0.467)
- **Europe PMC papers**: 24881
- **Why important**: IGF2 is the strongest network hub in the supplied subgraph and connects extracellular or secreted proteins with metabolic, adhesion, and cellular proteins, including GM2A, MDH1, CFB, BASP1, LDHA, FAM3C, ITIH1, and PGK1. It is secreted to blood, is tissue-enriched in placenta, and has established roles in growth, development, and osteoblast differentiation. Its imprinting and disease associations with growth disorders and tumors give it substantial biological and literature importance. The absence of STRING partners or hu.MAP assignment in this module means that its hub status is a co-abundance property rather than evidence of a known physical complex.
- **Conclusion**: Established evidence: IGF2 is a highly connected secreted growth factor with developmental and skeletal relevance. Hypothesis: IGF2 may help organize the cross-compartment co-abundance signal by linking circulating proteins to metabolic and adhesion states, but the module does not establish direct molecular interaction or causal regulation.

#### LRP1

- **Related proteins** (co-abundance neighbors): PLOD2 (0.97), MDH1 (0.96), ALCAM (0.91), ALDOC (0.91), LDHB (0.88), CD44 (0.87), PGK1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LDL receptor related protein 1. This gene encodes a member of the low-density lipoprotein receptor family of proteins. The encoded preproprotein is proteolytically processed by furin to generate 515 kDa and 85 kDa subunits that form the mature receptor (PMID: 8546712). This receptor is involved in several cellular processes, including intracellular signaling, lipid homeostasis, and clearance of apoptotic cells. In addition, the …
- **Diseases (Open Targets)**: neurodegenerative disease (0.514); keratosis pilaris atrophicans (0.499); developmental dysplasia of the hip (0.466); Alzheimer disease (0.462); Parkinson disease (0.443)
- **Europe PMC papers**: 10645
- **Why important**: LRP1 is a central membrane receptor in the module and connects PLOD2, MDH1, ALCAM, ALDOC, LDHB, CD44, and PGK1. Its documented functions include lipid homeostasis, receptor-mediated endocytosis, phagocytosis, inflammatory regulation, and clearance of apoptotic material. HPA places it in adipose and monocyte or myeloid dendritic-cell contexts, making it relevant to stromal, phagocytic, and immune-interface biology. Its disease associations include neurodegenerative disorders and skeletal abnormalities, which are pertinent to a bone-marrow and cerebrospinal-fluid comparison.
- **Conclusion**: Established evidence: LRP1 is a multifunctional clearance and signaling receptor positioned at the interface of lipid handling, inflammation, adhesion, and metabolism. Hypothesis: LRP1 may be a cellular bridge connecting extracellular plasma-protein exposure with uptake or clearance programs in marrow or cerebrospinal-fluid-associated cells.

#### ITIH1

- **Related proteins** (co-abundance neighbors): IGF2 (0.95), PGK1 (0.93), PROS1 (0.93), LDHA (0.92), LDHB (0.91), CLIC1 (0.91); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_06724.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07701.1, huMAP3_09273.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 1. This gene encodes a member of the inter-alpha-trypsin inhibitor family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the heavy chain of the inter-alpha-trypsin inhibitor complex, which is secreted by hepatocytes into the blood. The heavy chain also interacts with hyaluronan, and…
- **Diseases (Open Targets)**: osteoarthritis, hip (0.305); osteoarthritis (0.188); schizophrenia (0.185); major depressive disorder (0.183); psychiatric disorder (0.171)
- **Europe PMC papers**: 963
- **Why important**: ITIH1 is a network connector between IGF2, PGK1, PROS1, LDHA, LDHB, and CLIC1 and appears repeatedly in the hu.MAP extracellular assemblies (hu.MAP huMAP3_15040.1), (hu.MAP huMAP3_10678.1), and (hu.MAP huMAP3_06724.1) through (hu.MAP huMAP3_10101.1). It is a liver- and hepatocyte-enriched secreted protein that interacts with hyaluronan and belongs to the inter-alpha-trypsin inhibitor family. Its position links the plasma-protein component to the metabolic subnetwork, while its reported associations include osteoarthritis and neuropsychiatric disease.
- **Conclusion**: Established evidence: ITIH1 is a circulating extracellular matrix-associated protein with repeated complex-level support and a plausible role in hyaluronan-related extracellular organization. Hypothesis: ITIH1 may help transmit a shared extracellular-matrix or plasma signal across the two tissues, although its module connectivity does not prove a direct interaction with the metabolic genes.

#### CFB

- **Related proteins** (co-abundance neighbors): IGF2 (0.98), ALCAM (0.88); STRING partners: CFH (0.961)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_06724.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07701.1, huMAP3_09273.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1
- **Function (MyGene.info)**: complement factor B. This gene encodes complement factor B, a component of the alternative pathway of complement activation. Factor B circulates in the blood as a single chain polypeptide. Upon activation of the alternative pathway, it is cleaved by complement factor D yielding the noncatalytic chain Ba and the catalytic subunit Bb. The active subunit Bb is a serine protease which associates with C3b to form the alter…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with B factor anomaly (0.764); atypical hemolytic-uremic syndrome (0.705); Immunodeficiency due to a complement cascade protein anomaly (0.614); paroxysmal nocturnal hemoglobinuria (0.561); complement 3 glomerulopathy (0.546)
- **Europe PMC papers**: 7226
- **Why important**: CFB is a representative complement component and is linked to CFH by a high-confidence STRING relationship. It recurs with CFH and ITIH1 across many hu.MAP assemblies, especially the plasma-associated assemblies (hu.MAP huMAP3_15040.1) and (hu.MAP huMAP3_10678.1). CFB is secreted by liver-associated sources and participates in alternative-pathway complement activation, proteolysis, and pre-B-cell differentiation. Its disease associations include atypical hemolytic-uremic syndrome, complement glomerulopathy, immunodeficiency, and paroxysmal nocturnal hemoglobinuria.
- **Conclusion**: Established evidence: CFB anchors a known alternative-complement and circulating-plasma subnetwork. Hypothesis: its co-abundance with adhesion and metabolic genes may reflect innate-defense exposure or inflammatory cell composition in the samples, rather than a novel intracellular complement-metabolism complex.

#### CD44

- **Related proteins** (co-abundance neighbors): IGF2 (0.90), LRP1 (0.87), ICOSLG (0.84), PGK1 (0.82); STRING partners: ALCAM (0.859), SERPINC1 (0.716)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD44 molecule (IN blood group). The protein encoded by this gene is a cell-surface glycoprotein involved in cell-cell interactions, cell adhesion and migration. It is a receptor for hyaluronic acid (HA) and can also interact with other ligands, such as osteopontin, collagens, and matrix metalloproteinases (MMPs). This protein participates in a wide variety of cellular functions including lymphocyte activation, recirculation and …
- **Diseases (Open Targets)**: nephrolithiasis, calcium oxalate (0.523); calcium oxalate urolithiasis (0.521); uterine corpus leiomyoma (0.480); systemic lupus erythematosus (0.467); autoimmune disease (0.330)
- **Europe PMC papers**: 102058
- **Why important**: CD44 is a cell-surface adhesion and hyaluronan receptor with links to IGF2, LRP1, ICOSLG, and PGK1 in the module. STRING supports its relationships with ALCAM and SERPINC1. HPA detects it in bone marrow and associates it with dendritic cells, mast cells, monocytes, and neutrophils. Its established functions include cell adhesion, migration, inflammatory response, lymphocyte homing, and hematopoiesis, and it has a very large literature base and broad disease relevance.
- **Conclusion**: Established evidence: CD44 is a biologically credible marker of cell-surface interaction and hematopoietic or immune composition. Hypothesis: CD44 may connect marrow or cerebrospinal-fluid cellular interfaces to the extracellular plasma-protein signal, but its co-abundance cannot distinguish true regulation from shared cell-type abundance.

## Module 7

**Tissue pair**: bone_marrow and cerebrospinal_fluid  
**Genes (19)**: APOA1, APOA4, GUSB, CP, ERAP2, SERPING1, ICAM2, IGHG2, ITIH2, ITIH4, KNG1, LAMA2, LGMN, LY75, CHL1, PLBD2, PLG, F2, TF

### Function

The module is best interpreted as a circulating extracellular-plasma protein program linking hemostasis, fibrinolysis, lipid transport, iron handling, protease inhibition, complement regulation, and extracellular-matrix or hyaluronan biology. This interpretation is supported by the functions of F2, PLG, KNG1, APOA1, APOA4, TF, SERPING1, ITIH2, and ITIH4, together with the dense co-abundance relationships among these proteins. The hu.MAP complexes repeatedly contain the same plasma-protein set, especially CP, F2, PLG, KNG1, APOA1, TF, SERPING1, APOA4, ITIH2, and ITIH4 (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1). However, no GO or KEGG term passed global correction, so these annotations are an evidence-based functional interpretation rather than statistically validated enrichment. The module may therefore represent coordinated abundance of circulating proteins rather than a single intracellular pathway.

**Cell composition.** The composition strongly favors secreted or extracellular proteins: HPA classifies most module genes as secreted, and liver or hepatocyte enrichment is especially frequent. CP, APOA1, TF, SERPING1, ITIH2, KNG1, PLG, F2, and ITIH4 are liver-associated and secreted to blood or otherwise described as plasma proteins. APOA4 is intestine- and enterocyte-associated, while IGHG2 and ERAP2 point toward plasma-cell or lymphoid contributions. LY75, CHL1, ICAM2, GUSB, LGMN, and LAMA2 provide less purely hepatic or plasma-like signals, including lymphoid, neural, lysosomal, membrane, or extracellular-matrix biology. The HPA pattern argues that the shared module is substantially influenced by blood or plasma proteins in the samples and possibly by shared vascular or blood-associated material, rather than being evidence for a bone-marrow-specific and cerebrospinal-fluid-specific cellular program. The limited bone-marrow protein detection and the lack of a matching HPA cerebrospinal-fluid tissue category make direct local production in both tissues uncertain. Immune-cell associations are present but are not dominant across the whole module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a connected biochemical neighborhood among the plasma proteins. APOA1 is linked to APOA4, F2, ITIH2, and TF; F2 is linked to CP, ITIH2, KNG1, PLG, and TF; KNG1 is linked to PLG, SERPING1, and ITIH4; and ITIH4 is linked to PLG. These are consistent with established relationships involving coagulation, fibrinolysis, kinin biology, transport proteins, and protease regulation. The hu.MAP evidence is broader and repeatedly places the same proteins in multi-protein complexes (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1), with additional support for smaller recurring groupings such as F2–PLG–ITIH4 (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1), F2–KNG1–ITIH2 (hu.MAP huMAP3_07541.1), and CP–APOA4 (hu.MAP huMAP3_08700.1). The separate hu.MAP pair involving GUSB and LGMN (hu.MAP huMAP3_06775.1) (hu.MAP huMAP3_09327.1) suggests a lysosomal or endosomal component distinct from the main plasma-protein cluster. Known STRING and hu.MAP relationships show that much of the module is biologically coherent, but they do not establish that every co-abundance edge is a direct physical interaction or that the module is a single molecular complex.

**STRING interactions (score >= 0.7)**: 15 of 171 gene pairs: APOA1–APOA4 (0.989); APOA1–F2 (0.927); APOA1–ITIH2 (0.793); APOA1–TF (0.919); CP–F2 (0.703); CP–TF (0.835); F2–ITIH2 (0.852); F2–KNG1 (0.891); F2–PLG (0.826); F2–TF (0.725); ITIH2–TF (0.733); ITIH4–KNG1 (0.723); ITIH4–PLG (0.715); KNG1–PLG (0.898); KNG1–SERPING1 (0.964)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09531.1 (CP, F2, PLG, KNG1, APOA1, TF, SERPING1, APOA4, ITIH2, ITIH4; 10/47); huMAP3_10101.1 (CP, F2, PLG, KNG1, APOA1, TF, SERPING1, APOA4, ITIH2, ITIH4; 10/49); huMAP3_10678.1 (CP, F2, PLG, KNG1, APOA1, TF, SERPING1, APOA4, ITIH2, ITIH4; 10/71); huMAP3_15040.1 (CP, PLG, KNG1, APOA1, TF, SERPING1, APOA4, ITIH2, ITIH4; 9/64); huMAP3_08395.1 (CP, F2, PLG, KNG1, APOA1, TF, APOA4, ITIH2; 8/43); huMAP3_07265.1 (CP, KNG1, APOA1, TF, APOA4, ITIH2; 6/20); huMAP3_09273.1 (CP, F2, PLG, KNG1, SERPING1, ITIH2; 6/28); huMAP3_07432.1 (CP, APOA1, TF, APOA4; 4/18); huMAP3_07701.1 (F2, PLG, KNG1, ITIH2; 4/22); huMAP3_09434.1 (APOA1, TF, APOA4, ITIH4; 4/33); huMAP3_02236.1 (CP, KNG1, ITIH2; 3/7); huMAP3_08796.1 (F2, PLG, ITIH4; 3/15); huMAP3_09832.1 (F2, PLG, ITIH4; 3/18); huMAP3_07541.1 (F2, KNG1, ITIH2; 3/19); huMAP3_02242.1 (TF, APOA4; 2/9); huMAP3_08700.1 (CP, APOA4; 2/11); huMAP3_08224.1 (APOA1, TF; 2/21); huMAP3_06775.1 (GUSB, LGMN; 2/60); huMAP3_09327.1 (GUSB, LGMN; 2/93)

### Novelty

The module should not be called a newly discovered molecular pathway on the basis of this evidence. Its central proteins and many of their relationships are already represented in STRING and in recurring hu.MAP complexes, while the HPA and protein annotations identify them largely as familiar circulating, hepatic, intestinal, immune, or extracellular proteins. A potentially novel aspect is the reproducible co-abundance of this particular combination across bone marrow and cerebrospinal fluid, especially the connection of the plasma-protein core with LY75, CHL1, ICAM2, ERAP2, GUSB, and LGMN. Nevertheless, that cross-tissue association could arise from shared blood exposure, sample composition, vascular leakage, or common extracellular material. Demonstrating novelty would require comparison with previously published cross-tissue co-abundance modules, independent cohorts, and measurements that distinguish local tissue production from imported plasma proteins. Absence of some edges from STRING or hu.MAP is not evidence of novelty by itself.

**Hypothesis.** Hypothesis: this module reflects a shared extracellular-fluid compartment in which liver-derived plasma proteins enter or influence both bone-marrow and cerebrospinal-fluid samples, while a smaller immune, endothelial, neural, and lysosomal component modulates or records local handling of that material. The plasma core could coordinate protease balance, coagulation and fibrinolysis, complement restraint, lipid transport, iron transport, and extracellular-matrix stability. The association of CHL1, LY75, ICAM2, ERAP2, GUSB, and LGMN may indicate local uptake, antigen-processing, adhesion, or lysosomal processing of extracellular proteins, but the present data do not establish directionality, cellular origin, or causality. This hypothesis should be tested using matched plasma, bone marrow, and cerebrospinal-fluid samples, cell-resolved measurements, and assays that distinguish intact circulating proteins from locally synthesized proteins.

### Important genes

#### CP

- **Related proteins** (co-abundance neighbors): ITIH2 (0.98), GUSB (0.97), APOA4 (0.89), LY75 (0.88), ICAM2 (0.85), PLG (0.85), LGMN (0.83); STRING partners: F2 (0.703), TF (0.835)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_15040.1, huMAP3_08395.1, huMAP3_07265.1, huMAP3_09273.1, huMAP3_07432.1, huMAP3_02236.1, huMAP3_08700.1
- **Function (MyGene.info)**: ceruloplasmin. The protein encoded by this gene is a metalloprotein that binds most of the copper in plasma and is involved in the peroxidation of Fe(II)transferrin to Fe(III) transferrin. Mutations in this gene cause aceruloplasminemia, which results in iron accumulation and tissue damage, and is associated with diabetes and neurologic abnormalities. Two transcript variants, one protein-coding and the other not…
- **Diseases (Open Targets)**: aceruloplasminemia (0.827); cerebellar ataxia (0.572); Hermansky-Pudlak syndrome 3 (0.564); Hermansky-Pudlak syndrome (0.543); neurodegeneration with brain iron accumulation (0.510)
- **Europe PMC papers**: 171928
- **Why important**: CP has the strongest network position in the module and connects the plasma-protein core to ITIH2, APOA4, PLG, and several less plasma-like genes. It is a liver-enriched secreted protein that binds most circulating copper and participates in iron handling and oxidant detoxification. It is also represented across many hu.MAP complexes (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_02236.1) (hu.MAP huMAP3_08700.1). Its disease associations include aceruloplasminemia and neurologic abnormalities, giving it particular relevance to a module shared with cerebrospinal fluid. The literature is extensive.
- **Conclusion**: Established evidence supports CP as a central circulating metal-handling and redox-related component of the module, with strong support from its network position, HPA liver and secreted-protein annotation, and hu.MAP recurrence. Hypothesis: CP may help connect systemic iron and oxidative state to extracellular-fluid biology in the two sampled compartments. The module does not show that CP is locally produced or causally driving the cross-tissue association.

#### APOA1

- **Related proteins** (co-abundance neighbors): ICAM2 (1.00), PLBD2 (1.00), GUSB (1.00), LY75 (0.95); STRING partners: APOA4 (0.989), F2 (0.927), ITIH2 (0.793), TF (0.919)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_15040.1, huMAP3_08395.1, huMAP3_07265.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_08224.1
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is a highly studied major HDL protein with an important network bridge to ICAM2, PLBD2, GUSB, and LY75, and it is linked in STRING to APOA4, F2, ITIH2, and TF. It is liver-enriched, associated with hepatocytes and enterocytes, secreted to blood, and represented in many hu.MAP complexes (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08224.1). Its established functions include lipid transport, cholesterol efflux, and regulation of immune-related signaling. Its disease literature is extensive, including apolipoprotein deficiency and amyloidosis.
- **Conclusion**: Established evidence identifies APOA1 as a central plasma lipid-transport component and a plausible marker of circulating protein carryover. Hypothesis: APOA1 may organize or report the lipid-rich extracellular environment that couples the module across tissues, possibly influencing inflammatory or adhesion-related signals. The co-abundance data do not demonstrate that APOA1 physically organizes the other module proteins.

#### F2

- **Related proteins** (co-abundance neighbors): APOA4 (0.90); STRING partners: APOA1 (0.927), CP (0.703), ITIH2 (0.852), KNG1 (0.891), PLG (0.826), TF (0.725)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_08395.1, huMAP3_09273.1, huMAP3_07701.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07541.1
- **Function (MyGene.info)**: coagulation factor II, thrombin. This gene encodes the prothrombin protein (also known as coagulation factor II). This protein is proteolytically cleaved in multiple steps to form the activated serine protease thrombin. The activated thrombin enzyme plays an important role in thrombosis and hemostasis by converting fibrinogen to fibrin during blood clot formation, by stimulating platelet aggregation, and by activating additional …
- **Diseases (Open Targets)**: congenital prothrombin deficiency (0.827); thrombophilia due to thrombin defect (0.738); venous thromboembolism (0.727); deep vein thrombosis (0.690); blood coagulation disease (0.670)
- **Europe PMC papers**: 109299
- **Why important**: F2 encodes prothrombin and is a canonical hemostasis protein whose activated product, thrombin, controls fibrin formation, platelet activation, coagulation signaling, tissue repair, and angiogenesis. Although its direct module degree is limited, it has strong STRING connections to APOA1, CP, ITIH2, KNG1, PLG, and TF and appears across many hu.MAP complexes (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07541.1). It is liver- and hepatocyte-enriched and secreted to blood. The literature is exceptionally extensive, and disease associations include prothrombin deficiency and thromboembolic disease.
- **Conclusion**: Established evidence supports F2 as a mechanistic anchor for the module's coagulation and extracellular-protease interpretation. Hypothesis: variation in coagulation or vascular permeability could help generate the shared abundance pattern in bone marrow and cerebrospinal fluid. The module alone cannot distinguish active thrombin biology from passive abundance of circulating prothrombin.

#### PLG

- **Related proteins** (co-abundance neighbors): APOA4 (0.87), CP (0.85), CHL1 (0.80); STRING partners: F2 (0.826), ITIH4 (0.715), KNG1 (0.898)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_15040.1, huMAP3_08395.1, huMAP3_09273.1, huMAP3_07701.1, huMAP3_08796.1, huMAP3_09832.1
- **Function (MyGene.info)**: plasminogen. The plasminogen protein encoded by this gene is a serine protease that circulates in blood plasma as an inactive zymogen and is converted to the active protease, plasmin, by several plasminogen activators such as tissue plasminogen activator (tPA), urokinase plasminogen activator (uPA), kallikrein, and factor XII (Hageman factor). The conversion of plasminogen to plasmin involves the cleavage of t…
- **Diseases (Open Targets)**: hypoplasminogenemia (0.813); hereditary angioedema (0.737); hemorrhage (0.605); dysplasminogenemia (0.598); Menorrhagia (0.579)
- **Europe PMC papers**: 17740
- **Why important**: PLG is a liver-enriched secreted zymogen that is converted to plasmin and participates in fibrinolysis, extracellular-matrix disassembly, collagen catabolism, and cell-substrate adhesion. It connects to APOA4, CP, and CHL1 in the module and has established STRING relationships with F2, ITIH4, and KNG1. It recurs in numerous hu.MAP complexes, including the large plasma-protein groupings and the F2–PLG–ITIH4 groupings (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1). Its disease associations include plasminogen deficiency, hemorrhage, and dysplasminogenemia, and the literature is extensive.
- **Conclusion**: Established evidence supports PLG as the principal fibrinolytic and extracellular-matrix-remodeling component of the module. Hypothesis: the PLG signal may reflect a shared vascular or extracellular-matrix interface between marrow and cerebrospinal-fluid compartments. The data do not show that plasmin is activated in either tissue.

#### SERPING1

- **Related proteins** (co-abundance neighbors): ERAP2 (1.00), LY75 (0.99), LGMN (0.95); STRING partners: KNG1 (0.964)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_15040.1, huMAP3_09273.1
- **Function (MyGene.info)**: serpin family G member 1. This gene encodes a highly glycosylated plasma protein involved in the regulation of the complement cascade. Its encoded protein, C1 inhibitor, inhibits activated C1r and C1s of the first complement component and thus regulates complement activation. It is synthesized in the liver, and its deficiency is associated with hereditary angioneurotic oedema (HANE). Alternative splicing results in multipl…
- **Diseases (Open Targets)**: hereditary angioedema with C1Inh deficiency (0.828); hereditary angioedema type 1 (0.750); hereditary angioedema (0.728); angioedema (0.616); hereditary angioedema type 2 (0.614)
- **Europe PMC papers**: 4203
- **Why important**: SERPING1 encodes C1 inhibitor, a secreted liver-associated regulator of complement and plasma protease systems. Its direct module links include ERAP2, LY75, and LGMN, while STRING connects it strongly to KNG1. It is present in several hu.MAP complexes (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_09273.1). Its established disease associations include hereditary angioedema and C1-inhibitor deficiency, and its literature is substantial. The combination of plasma secretion with links to immune-associated genes makes it informative for interpreting the module beyond simple hepatic protein abundance.
- **Conclusion**: Established evidence supports SERPING1 as a regulator of complement and contact-system activity within the plasma-like core. Hypothesis: its links to LY75, ERAP2, and LGMN may reflect immune-cell handling of complement or contact-system proteins in marrow or cerebrospinal-fluid-associated material. The co-abundance network cannot establish complement activation or inhibition in vivo.

#### LY75

- **Related proteins** (co-abundance neighbors): SERPING1 (0.99), CHL1 (0.97), APOA1 (0.95), CP (0.88), KNG1 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lymphocyte antigen 75. Predicted to enable signaling receptor activity. Predicted to be involved in immune response and inflammatory response. Located in extracellular exosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: insomnia (0.357); clonal hematopoiesis (0.294); type 2 diabetes mellitus (0.282); placental abruption (0.276); membranous glomerulonephritis (0.247)
- **Europe PMC papers**: 738
- **Why important**: LY75 is a useful noncanonical module member because it has a relatively central position connecting SERPING1, CHL1, APOA1, CP, and KNG1, yet it has no reported STRING partners and no hu.MAP assignment in the fact sheet. HPA associates it with lymphoid tissue and microglia, with receptor-mediated endocytosis and immune or inflammatory functions in the supplied annotations. Its disease-association and literature footprint is smaller than that of the major plasma proteins. This combination makes LY75 a potentially informative bridge rather than a well-established biochemical core member.
- **Conclusion**: Established evidence supports LY75 as an immune-associated endocytic or receptor-related gene that is co-abundant with the plasma-protein network, but independent interaction evidence is absent here. Hypothesis: LY75 may mark uptake or processing of circulating proteins by microglia-like or lymphoid-associated cells, helping connect a blood-derived signal to cerebrospinal-fluid biology. This remains speculative and requires cell-resolved validation.

## Module 8

**Tissue pair**: bone_marrow and cerebrospinal_fluid  
**Genes (5)**: GSN, MINPP1, RBP4, SOD2, GC

### Function

No globally significant GO/KEGG GO or KEGG term passed global correction, so the module does not support a statistically established single pathway assignment. Its composition and network instead suggest a mixed extracellular and cellular-state signature. RBP4 and GC support circulating transport of retinoid and vitamin D-related molecules, GSN supports actin filament remodeling, SOD2 supports mitochondrial superoxide defense, and MINPP1 supports inositol-phosphate and related metabolic functions. The co-abundance pattern is therefore more consistent with coordinated abundance of plasma proteins and selected marrow-associated cellular proteins than with a coherent canonical pathway. This interpretation is compatible with a shared fluid or cellular-mixture signal in bone marrow and cerebrospinal-fluid samples, rather than proof that all members act in one biochemical complex.

**Cell composition.** The module is strongly enriched in secreted or blood-associated proteins at the protein-class level: RBP4, GC, GSN, and MINPP1 are annotated as secreted to blood, while SOD2 is mitochondrial and not secreted. RBP4 and GC are liver-enriched and hepatocyte-associated, and both are not detected in immune cells according to HPA. GSN has heart-muscle enhancement and an eosinophil-associated signal. SOD2 is bone-marrow enhanced and immune-cell enriched in neutrophils, while MINPP1 is associated with erythrocyte and megakaryocyte progenitors. HPA therefore points to a heterogeneous mixture of plasma proteins, marrow-associated progenitor or myeloid signals, and broadly distributed cellular biology, rather than a uniformly bone-marrow-specific or cerebrospinal-fluid-specific module. The absence of a matching HPA cerebrospinal-fluid tissue category limits direct interpretation of the fluid source.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports two high-confidence relationships within the module: GC with GSN and GC with RBP4. These connections provide external support for part of the observed co-abundance structure, especially the relationship between the two circulating transport proteins and gelsolin. The remaining observed co-abundance links, including those involving SOD2 and MINPP1, are not supported by the reported high-confidence STRING interaction set. STRING functional enrichment is absent. No hu.MAP complex contains multiple module members. Thus, the module is not supported as a known stable multiprotein complex; it appears to combine some known protein relationships with abundance covariation that may reflect shared secretion, tissue contribution, cellular composition, or physiological state.

**STRING interactions (score >= 0.7)**: 2 of 10 gene pairs: GC–GSN (0.826); GC–RBP4 (0.749)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact conserved co-abundance module may represent a new computational observation, but the available evidence is insufficient to call it a new biological mechanism. RBP4, GC, GSN, SOD2, and MINPP1 are individually established proteins with substantial functional and disease literature, and part of the module is supported by known STRING relationships. Conversely, the absence of a hu.MAP complex and the lack of STRING support for several module edges indicate that the complete five-gene pattern is not represented as an established complex in the supplied resources. That database absence does not prove novelty, because co-abundance modules can reflect tissue mixtures, secretion, post-transcriptional regulation, or condition-dependent biology. A defensible conclusion is that the module-level association is potentially novel and worth validation, while its individual components and some pairwise relationships are not novel.

**Hypothesis.** Hypothesis: the shared module reflects a systemic extracellular transport and stress-response axis that is visible in both bone marrow and cerebrospinal-fluid-associated samples because of plasma protein contribution and shared cellular or physiological states. Liver-derived RBP4 and GC may represent coordinated transport-protein abundance; GSN may connect this extracellular signal to actin turnover and vascular or immune-cell biology; SOD2 may report mitochondrial oxidative-stress handling in marrow-associated cells; and MINPP1 may report progenitor-cell metabolism or mineral and inositol phosphate regulation. The direct GC relationships supported by STRING make the extracellular part of this model plausible, but the links from the circulating proteins to SOD2 and MINPP1 remain hypotheses about coordinated abundance rather than demonstrated molecular interactions. Testing matched plasma contamination, cell-type composition, and targeted protein measurements would be necessary.

### Important genes

#### RBP4

- **Related proteins** (co-abundance neighbors): SOD2 (0.95), GSN (0.92), GC (0.92); STRING partners: GC (0.749)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: retinol binding protein 4. This protein belongs to the lipocalin family and is the specific carrier for retinol (vitamin A alcohol) in the blood. It delivers retinol from the liver stores to the peripheral tissues. In plasma, the RBP-retinol complex interacts with transthyretin which prevents its loss by filtration through the kidney glomeruli. A deficiency of vitamin A blocks secretion of the binding protein posttranslatio…
- **Diseases (Open Targets)**: progressive retinal dystrophy due to retinol transport defect (0.696); microphthalmia, isolated, with coloboma 10 (0.643); microphthalmia, isolated, with coloboma (0.506); microphthalmia (0.501); inherited retinal dystrophy (0.421)
- **Europe PMC papers**: 18196
- **Why important**: RBP4 is the strongest network hub in the module, connecting SOD2, GSN, and GC. It is a liver-enriched, hepatocyte-associated secreted blood protein that transports retinol from liver stores to peripheral tissues. Its extensive literature and associations with retinal dystrophy and microphthalmia make it biologically and clinically prominent. Its connection to GC is also supported by STRING.
- **Conclusion**: Established: RBP4 is a circulating retinol carrier with liver and hepatocyte enrichment and a central position in this module. Hypothesis: its hub position may indicate that systemic retinoid transport or plasma contribution helps organize the shared co-abundance signal, but the module does not establish a causal role for RBP4 in marrow or cerebrospinal-fluid biology.

#### GC

- **Related proteins** (co-abundance neighbors): RBP4 (0.92), MINPP1 (0.90); STRING partners: GSN (0.826), RBP4 (0.749)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GC vitamin D binding protein. The protein encoded by this gene belongs to the albumin gene family. It is a multifunctional protein found in plasma, ascitic fluid, cerebrospinal fluid and on the surface of many cell types. It binds to vitamin D and its plasma metabolites and transports them to target tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq,…
- **Diseases (Open Targets)**: vitamin D deficiency (0.574); vitamin deficiency (0.552); chronic obstructive pulmonary disease (0.499); squamous cell carcinoma (0.339); central nervous system cancer (0.334)
- **Europe PMC papers**: 363974
- **Why important**: GC is a central connector between RBP4 and MINPP1 and has the clearest external interaction support, with STRING relationships to GSN and RBP4. It is a liver-enriched, hepatocyte-associated secreted plasma protein that binds and transports vitamin D and its metabolites and is also reported in cerebrospinal fluid. It has very substantial literature and disease associations in vitamin deficiency and other conditions.
- **Conclusion**: Established: GC is a multifunctional circulating vitamin D-binding protein and a supported interaction node in the module. Hypothesis: GC may be the principal extracellular scaffold of the shared abundance pattern, but its presence does not demonstrate formation of a physical complex with every module member.

#### SOD2

- **Related proteins** (co-abundance neighbors): RBP4 (0.95); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: superoxide dismutase 2. This gene is a member of the iron/manganese superoxide dismutase family. It encodes a mitochondrial protein that forms a homotetramer and binds one manganese ion per subunit. This protein binds to the superoxide byproducts of oxidative phosphorylation and converts them to hydrogen peroxide and diatomic oxygen. Mutations in this gene have been associated with idiopathic cardiomyopathy (IDC), premat…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); diabetic retinopathy (0.379); malunion fracture (0.295); coronary artery disorder (0.267); prostate carcinoma (0.227)
- **Europe PMC papers**: 28293
- **Why important**: SOD2 is directly connected to the module hub RBP4 and is the only clearly mitochondrial, non-secreted component. It is bone-marrow enhanced, associated with neutrophils, and encodes the mitochondrial manganese superoxide dismutase that converts superoxide to hydrogen peroxide and oxygen. Its disease links include neurodegenerative disease and cardiometabolic or cancer-related conditions, and it has a substantial literature.
- **Conclusion**: Established: SOD2 represents mitochondrial oxidative-stress defense in a marrow-associated cellular context. Hypothesis: its covariation with RBP4 may indicate shared oxidative or cellular-state regulation, but there is no reported STRING support for a direct SOD2 interaction within this module.

#### GSN

- **Related proteins** (co-abundance neighbors): RBP4 (0.92); STRING partners: GC (0.826)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gelsolin. The protein encoded by this gene binds to the 'plus' ends of actin monomers and filaments to prevent monomer exchange. The encoded calcium-regulated protein functions in both assembly and disassembly of actin filaments. Defects in this gene are a cause of familial amyloidosis Finnish type (FAF). Multiple transcript variants encoding several different isoforms have been found for this gene. [provid…
- **Diseases (Open Targets)**: Finnish type amyloidosis (0.805); AL amyloidosis (0.463); neuropathy (0.418); cardiomyopathy (0.418); cutis laxa (0.417)
- **Europe PMC papers**: 5062
- **Why important**: GSN connects directly to RBP4 in the module and has STRING support with GC, giving it a position at the interface between the circulating transport signal and cytoskeletal biology. Gelsolin regulates actin filament assembly and disassembly, is secreted to blood, and shows associations with vascular, stromal, epithelial, and eosinophil-related cell types. It is also linked to Finnish-type amyloidosis, neuropathy, cardiomyopathy, and cutis laxa.
- **Conclusion**: Established: GSN is an actin-remodeling protein with extracellular and cell-associated biology and known relationships to GC and RBP4. Hypothesis: GSN may connect plasma abundance to vascular, immune, or stromal remodeling in the shared samples, but the module alone cannot identify which cell type supplies the signal.

#### MINPP1

- **Related proteins** (co-abundance neighbors): GC (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: multiple inositol-polyphosphate phosphatase 1. This gene encodes multiple inositol polyphosphate phosphatase; an enzyme that removes 3-phosphate from inositol phosphate substrates. It is the only enzyme known to hydrolzye inositol pentakisphosphate and inositol hexakisphosphate. This enzyme also converts 2,3 bisphosphoglycerate (2,3-BPG) to 2-phosphoglycerate; an activity formerly thought to be exclusive to 2,3-BPG synthase/2-phosphatase (BPGM…
- **Diseases (Open Targets)**: pontocerebellar hypoplasia, type 16 (0.784); pontocerebellar hypoplasia (0.682); thyroid gland follicular carcinoma (0.555); thyroid cancer, nonmedullary, 2 (0.467); neurodegenerative disease (0.424)
- **Europe PMC papers**: 603
- **Why important**: MINPP1 is connected to GC and is the module member most specifically associated with erythrocyte, megakaryocyte, and megakaryocyte-erythroid progenitor populations in the HPA summary. It encodes an enzyme that removes phosphate from inositol phosphate substrates and also acts on a metabolite in the red-cell glycolytic shunt. Its reported functions include inositol-phosphate metabolism, bone mineralization, and ossification, while its disease associations include pontocerebellar hypoplasia and neurodegenerative disease.
- **Conclusion**: Established: MINPP1 provides a plausible marrow-progenitor and metabolic component and is connected to GC in the co-abundance graph. Hypothesis: it may mark a progenitor or red-cell metabolic contribution that couples to the extracellular protein signal, but no direct molecular interaction with GC or the other module members is established by the supplied STRING or hu.MAP evidence.
