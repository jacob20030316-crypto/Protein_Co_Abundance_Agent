# Conserved co-abundance modules: breast and circulatory_system

## Module 0

**Tissue pair**: breast and circulatory_system  
**Genes (6)**: AGAP2, HSP90AA4P, IL16, MLX, RIC1, SH3PXD2A

### Function

The module does not have a globally significant GO or KEGG annotation: no globally significant GO/KEGG term passed global correction. The available gene-level evidence suggests a mixed regulatory program rather than a confidently defined canonical pathway. Its components include cytokine and immune signaling through IL16, redox and podosome-related biology through SH3PXD2A, intracellular trafficking and small-GTPase regulation through RIC1, transcriptional and metabolic regulation through MLX, and signaling, cytoskeletal, endosomal, and anti-apoptotic functions through AGAP2. These annotations support a cautious interpretation involving cell signaling, vesicle or membrane trafficking, cytoskeletal remodeling, and context-dependent regulation of survival or differentiation. They do not establish a single coherent pathway.

**Cell composition.** The module is not dominated by broadly expressed housekeeping genes, although several members have low tissue specificity. It contains one secreted-to-blood gene, IL16, but is not predominantly composed of plasma or secreted proteins. HPA evidence shows cell-type-enhanced expression for most annotated genes, with signals involving epithelial, neuronal, adipocyte, lymphoid, hematopoietic, and neutrophil-related cell types. Blood-cell specificity is generally low, and no enriched blood-cell category was reported. Breast protein detection is present for most genes with available data, whereas there is no matching HPA tissue for circulatory_system. Thus, the shared signal could reflect common cellular composition, especially particular epithelial or stromal contexts, or a blood-associated contribution from IL16, but the HPA evidence does not support interpreting the module simply as a blood-cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair in the module met the stated STRING interaction threshold, and there was no supplementary STRING functional enrichment. No hu.MAP complex contained multiple module members. Therefore, the co-abundance edges are not corroborated by the supplied high-confidence physical-interaction or complex evidence. The network may represent coordinated expression, indirect regulation, shared cellular origin, or technical and compositional effects rather than a known protein complex. The strongest co-abundance connections place HSP90AA4P between MLX, SH3PXD2A, and RIC1, while SH3PXD2A connects to IL16 and RIC1 connects to AGAP2; these are network observations, not established molecular interactions.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears to be a potentially novel co-abundance association rather than a demonstrated new molecular pathway. The absence of STRING interactions and hu.MAP complexes means that the particular combination and expression relationship are not represented by the supplied interaction resources, but that absence alone cannot prove novelty. The lack of globally significant GO or KEGG enrichment also prevents claiming discovery of a new enriched biological function. A defensible novelty claim would require replication in independent breast and circulatory-system datasets, control for cell composition and blood contamination, and direct comparison with published co-expression modules and tissue-specific expression studies.

**Hypothesis.** Hypothesis: the module reflects coordinated expression across a shared cellular or compositional context in breast and circulatory-system samples, linking IL16-associated extracellular immune signaling with SH3PXD2A-associated redox and actin or podosome biology, RIC1-associated membrane trafficking, AGAP2-associated survival and cytoskeletal signaling, and MLX-associated transcriptional regulation. HSP90AA4P may act as a co-abundance connector or genomic-expression correlate rather than as a proven functional hub. This model predicts that the module will weaken after adjustment for cell-type composition if it is primarily compositional, whereas persistence in purified or matched cell populations would support a genuine regulatory program.

### Important genes

#### IL16

- **Related proteins** (co-abundance neighbors): SH3PXD2A (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: interleukin 16. The protein encoded by this gene is a pleiotropic cytokine that functions as a chemoattractant, a modulator of T cell activation, and an inhibitor of HIV replication. The signaling process of this cytokine is mediated by CD4. The product of this gene undergoes proteolytic processing, which is found to yield two functional proteins. The cytokine function is exclusively attributed to the secreted C-…
- **Diseases (Open Targets)**: hair color (0.352); primary biliary cholangitis (0.338); placenta praevia (0.290); nodular goiter (0.239); facial morphology (0.211)
- **Europe PMC papers**: 9642
- **Why important**: IL16 is the clearest extracellular and immune-related component: it is a pleiotropic chemoattractant and modulator of T-cell activation, is processed into functional products, and is secreted to blood according to HPA. It is connected to SH3PXD2A in the module and has the largest literature volume among the genes, making it important for interpreting a possible blood-associated or immune-signaling contribution. Its HPA tissue enhancement in lymphoid tissue supports biological relevance, while its lack of breast protein detection cautions against assuming that it originates from breast epithelial cells.
- **Conclusion**: Established evidence supports IL16 as a secreted cytokine-related gene with immune and leukocyte-chemotaxis functions. The module does not establish that IL16 physically interacts with SH3PXD2A or drives the shared co-abundance pattern. A blood-derived or immune-context contribution is plausible but remains a hypothesis requiring cell-composition analysis.

#### SH3PXD2A

- **Related proteins** (co-abundance neighbors): IL16 (0.85), HSP90AA4P (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Primary cilium transition zone, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SH3 and PX domains 2A. Predicted to enable superoxide-generating NADPH oxidase activator activity. Involved in osteoclast fusion and superoxide metabolic process. Located in podosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: atrial fibrillation (0.512); stroke disorder (0.486); ischemic stroke (0.470); hypertensive disorder (0.440); diverticular disease (0.438)
- **Europe PMC papers**: 802
- **Why important**: SH3PXD2A is an informative bridge between IL16 and the central HSP90AA4P-associated portion of the network. Its curated functions include superoxide generation, superoxide metabolism, osteoclast fusion, and podosome biology, providing a mechanistic link to redox and cytoskeletal remodeling. It has substantial literature support, HPA cell-type enhancement in basal keratinocytes and esophageal apical cells, and reported associations with cardiovascular and cerebrovascular disorders in Open Targets.
- **Conclusion**: Established evidence supports roles in redox biology, podosomes, and osteoclast-related cell fusion. Its position in this module is consistent with a signaling or cytoskeletal interpretation, but the module supplies no validated physical partners and no globally significant enrichment. Its disease associations should therefore be treated as contextual evidence, not as proof that this module causes cardiovascular disease.

#### RIC1

- **Related proteins** (co-abundance neighbors): AGAP2 (0.83), HSP90AA4P (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RIC1 partner of RAB6A GEF complex. Enables guanyl-nucleotide exchange factor activity and small GTPase binding activity. Involved in several processes, including positive regulation of GTPase activity; regulation of extracellular matrix constituent secretion; and retrograde transport, endosome to Golgi. Located in cytosol and membrane. Part of Ric1-Rgp1 guanyl-nucleotide exchange factor complex. [provided by Alliance of Genome Reso…
- **Diseases (Open Targets)**: Catifa syndrome (0.606); respiratory system disorder (0.376); bipolar disorder (0.241); asthma (0.217); lower respiratory tract disorder (0.212)
- **Europe PMC papers**: 511
- **Why important**: RIC1 connects the HSP90AA4P side of the network to AGAP2 and has a defined role as a partner of the RAB6A guanyl-nucleotide exchange factor complex. Its annotated activities include small-GTPase binding, regulation of extracellular-matrix constituent secretion, intracellular transport, and retrograde endosome-to-Golgi transport. These functions make it a strong candidate for explaining how the module could coordinate membrane trafficking with extracellular or cytoskeletal processes.
- **Conclusion**: Established evidence supports RIC1 as a trafficking and small-GTPase regulator that participates in a RAB6A-associated complex. The module is compatible with a trafficking-related hypothesis, but no hu.MAP complex or STRING relationship involving multiple module genes was detected. The shared abundance of RIC1 with the other genes therefore remains an association rather than evidence of a module-specific complex.

#### AGAP2

- **Related proteins** (co-abundance neighbors): RIC1 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ArfGAP with GTPase domain, ankyrin repeat and PH domain 2. The protein encoded by this gene belongs to the centaurin gamma-like family. It mediates anti-apoptotic effects of nerve growth factor by activating nuclear phosphoinositide 3-kinase. It is overexpressed in cancer cells, and promotes cancer cell invasion. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.341); neoplasm (0.110); central nervous system cancer (0.110); glioma (0.110); glioblastoma (0.104)
- **Europe PMC papers**: 1152
- **Why important**: AGAP2 is the connection between RIC1 and a gene with strong tissue and cell-type context in the HPA data. It is tissue-enriched in brain and enhanced in excitatory and inhibitory neurons, hematopoietic stem cells, neutrophil progenitors, and neutrophils. Its annotated functions include endosomal transport, actin-cytoskeleton organization, anti-apoptotic regulation, and protein-kinase regulation. It is also reported to promote cancer-cell invasion and has disease associations involving neoplasia and nervous-system disorders.
- **Conclusion**: Established evidence supports AGAP2 as a signaling, endosomal, cytoskeletal, and survival regulator with context-dependent disease relevance. Its module connection to RIC1 supports a possible trafficking-signaling relationship, but the co-abundance network cannot determine whether this reflects shared cell types, indirect regulation, or a direct mechanism. The neuronal and hematopoietic HPA patterns make cellular composition an especially important alternative explanation.

#### MLX

- **Related proteins** (co-abundance neighbors): HSP90AA4P (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MAX dimerization protein MLX. The product of this gene belongs to the family of basic helix-loop-helix leucine zipper (bHLH-Zip) transcription factors. These factors form heterodimers with Mad proteins and play a role in proliferation, determination and differentiation. This gene product may act to diversify Mad family function by its restricted association with a subset of the Mad family of transcriptional repressors, namely,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.463); 46 XX gonadal dysgenesis (0.423); metabolic syndrome (0.235); type 2 diabetes mellitus (0.175); coronary artery disorder (0.092)
- **Europe PMC papers**: 2024
- **Why important**: MLX is the transcription-factor component and is connected to HSP90AA4P. It belongs to the bHLH-Zip family and can heterodimerize with Mad-family repressors, with annotations involving transcriptional regulation, glucose homeostasis, proliferation, and differentiation. Its HPA profile includes enhancement in breast lactating cells and other epithelial cell types, making it relevant to a breast-associated cellular state. Its substantial literature volume and links to metabolic and coronary-related disease contexts add interpretive importance.
- **Conclusion**: Established evidence supports MLX as a transcriptional regulator with roles related to proliferation, differentiation, and metabolic regulation. It could plausibly mediate a downstream expression state associated with the other module members, but there is no evidence here that MLX directly regulates them. Its presence favors a regulatory-state interpretation over a simple secreted-protein interpretation, while the lack of global GO or KEGG enrichment limits confidence in any specific pathway assignment.

## Module 1

**Tissue pair**: breast and circulatory_system  
**Genes (23)**: AP4E1, DGKE, DHRS11, DIAPH2, DOCK2, SIRAL2, FAM241B, EIF4E2, KDM2B, RPS6KC1, MAP3K4, MED20, MON1B, MAP2K7, NDOR1, PARP10, PIK3CA, ARHGAP27, SEPSECS, SARS2, TBC1D1, TIPRL, ZBTB44

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent. The genes instead suggest a heterogeneous intracellular program spanning chromatin and transcriptional regulation through KDM2B and MED20, lipid and phosphoinositide signaling through DGKE and PIK3CA, stress-activated kinase signaling through MAP2K7 and MAP3K4, vesicle trafficking through AP4E1 and MON1B, immune-cell migration through DOCK2, redox-related maintenance through NDOR1, and selenocysteine-related translation through SEPSECS and SARS2. KDM2B is the main network hub, with several smaller branches. The most cautious interpretation is a conserved cellular-state or maintenance program rather than a proven single biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only DHRS11 is annotated as secreted, while the other genes lack secretome annotation. Most genes have low tissue specificity, but many are cell-type enhanced across diverse epithelial, neural, reproductive, vascular, and immune cell types. Blood-cell evidence is mixed: most genes have low immune-cell specificity, while a minority are immune-cell enhanced or group enriched, including DOCK2, RPS6KC1, AP4E1, MAP3K4, and FAM241B. Breast protein detection is present for part of the module, whereas no matching HPA circulatory tissue is available. The shared signal could therefore reflect broadly expressed maintenance biology, shared cell types, or sample composition; the evidence does not support assigning it primarily to blood contamination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

Two relationships are supported by high-confidence STRING evidence: MAP2K7 with TIPRL and SARS2 with SEPSECS. These support limited links to stress or phosphatase-regulatory biology and to mitochondrial seryl-tRNA and selenocysteine-related biology. The remaining co-abundance edges lack supplied high-confidence STRING support. No hu.MAP complex contains multiple module members. Thus, this is mainly a co-abundance network rather than a demonstrated physical complex. The STRING-supported pairs may be functional anchors, but they do not establish one connected molecular pathway for the whole module.

**STRING interactions (score >= 0.7)**: 2 of 253 gene pairs: MAP2K7–TIPRL (0.821); SARS2–SEPSECS (0.959)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The conserved breast–circulatory-system co-abundance pattern may be a new dataset-level observation because the supplied evidence does not identify an established module or hu.MAP complex corresponding to it. It should not be presented as a new biological mechanism. The functions of several component genes are already well established, and the module lacks globally significant GO or KEGG enrichment. Limited STRING and hu.MAP support may indicate that the particular co-abundance organization is under-characterized, but absence from those resources does not prove novelty. Independent replication, comparison with published co-expression modules, and experimental testing would be required for a stronger novelty claim.

**Hypothesis.** Hypothesis: the module represents a shared cellular-state program coupling basal intracellular maintenance with context-responsive signaling. KDM2B may organize the abundance pattern through chromatin and transcriptional regulation. DGKE and PIK3CA may connect lipid signaling with membrane, growth, or vascular responses; DOCK2 may contribute an immune-cell motility component; and MAP2K7 with MAP3K4 may reflect stress or inflammatory responsiveness. SEPSECS and SARS2 may represent translational and mitochondrial maintenance rather than direct interaction with every other branch. The apparent conservation between tissues may therefore arise from shared cell types or shared physiological states rather than one universal protein complex.

### Important genes

#### KDM2B

- **Related proteins** (co-abundance neighbors): DGKE (0.90), TIPRL (0.90), AP4E1 (0.88), MED20 (0.87), PIK3CA (0.86), NDOR1 (0.85), DIAPH2 (0.84), SEPSECS (0.82), SARS2 (0.82), EIF4E2 (0.81), FAM241B (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lysine demethylase 2B. This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls con…
- **Diseases (Open Targets)**: hereditary disease (0.471); complex neurodevelopmental disorder (0.370); neurodegenerative disease (0.358); type 2 diabetes mellitus (0.340); diabetes mellitus (0.338)
- **Europe PMC papers**: 1964
- **Why important**: KDM2B is the central network hub, connecting multiple otherwise separate branches, including DGKE, TIPRL, AP4E1, MED20, PIK3CA, NDOR1, DIAPH2, and SEPSECS. Its established roles include chromatin remodeling, transcriptional regulation, and participation in ubiquitin-ligase-related biology. It also has a substantial literature and disease associations involving neurodevelopmental, neurodegenerative, and metabolic disorders.
- **Conclusion**: Established evidence supports KDM2B as the main network-position gene and as a regulator of gene expression and chromatin biology. It is not established that KDM2B causes the cross-tissue module or directly binds the other module proteins. Its hub position supports a regulatory interpretation, while causality remains hypothetical.

#### DGKE

- **Related proteins** (co-abundance neighbors): KDM2B (0.90), SEPSECS (0.85), DOCK2 (0.84), TBC1D1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: diacylglycerol kinase epsilon. Diacylglycerol kinases are thought to be involved mainly in the regeneration of phosphatidylinositol (PI) from diacylglycerol in the PI-cycle during cell signal transduction. When expressed in mammalian cells, DGK-epsilon shows specificity for arachidonyl-containing diacylglycerol. DGK-epsilon is expressed predominantly in testis. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: immunoglobulin-mediated membranoproliferative glomerulonephritis (0.793); atypical hemolytic-uremic syndrome (0.656); atypical hemolytic-uremic syndrome with DGKE deficiency (0.644); membranoproliferative glomerulonephritis (0.616); neurodegenerative disease (0.519)
- **Europe PMC papers**: 1092
- **Why important**: DGKE is a local connector between KDM2B and SEPSECS, DOCK2, and TBC1D1. Its established activity in diacylglycerol and phosphatidylinositol-related signaling provides a plausible link to membrane signaling, platelet biology, and immune or vascular cellular responses. It has substantial literature and disease associations involving complement-related renal disorders.
- **Conclusion**: Established evidence supports DGKE as a lipid-signaling regulator with relevance to platelet and immune-associated biology. Its network position suggests that it may connect signaling with cell-composition effects, but a direct DGKE-mediated mechanism for the whole module is not established.

#### SEPSECS

- **Related proteins** (co-abundance neighbors): MON1B (0.90), DGKE (0.85), KDM2B (0.82), SIRAL2 (0.80); STRING partners: SARS2 (0.959)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Sep (O-phosphoserine) tRNA:Sec (selenocysteine) tRNA synthase. The amino acid selenocysteine is the only amino acid that does not have its own tRNA synthetase. Instead, this amino acid is synthesized on its cognate tRNA in a three step process. The protein encoded by this gene catalyzes the third step in the process, the conversion of O-phosphoseryl-tRNA(Sec) to selenocysteinyl-tRNA(Sec).[provided by RefSeq, Mar 2011].
- **Diseases (Open Targets)**: pontocerebellar hypoplasia type 2D (0.757); progressive cerebello-cerebral atrophy (0.667); pontocerebellar hypoplasia type 2 (0.667); pontocerebellar hypoplasia (0.660); neurodegenerative disease (0.537)
- **Europe PMC papers**: 491
- **Why important**: SEPSECS connects MON1B, DGKE, KDM2B, and SIRAL2 and has a high-confidence STRING relationship with SARS2. It catalyzes the final step in selenocysteine-tRNA formation, making it relevant to selenoprotein production and cellular redox maintenance. It has established associations with pontocerebellar and cerebello-cerebral disorders.
- **Conclusion**: Established evidence supports SEPSECS as an enzyme in selenocysteine incorporation and as part of a known relationship with SARS2. The module supports a possible translation or redox-maintenance branch, but does not show that this branch drives conservation between the tissues.

#### DOCK2

- **Related proteins** (co-abundance neighbors): DGKE (0.84); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dedicator of cytokinesis 2. The protein encoded by this gene belongs to the CDM protein family. It is specifically expressed in hematopoietic cells and is predominantly expressed in peripheral blood leukocytes. The protein is involved in remodeling of the actin cytoskeleton required for lymphocyte migration in response to chemokine signaling. It activates members of the Rho family of GTPases, for example RAC1 and RAC2, by ac…
- **Diseases (Open Targets)**: DOCK2 deficiency (0.788); severe combined immunodeficiency (0.371); HIV infectious disease (0.370); bipolar disorder (0.346); muscle cramp (0.315)
- **Europe PMC papers**: 3228
- **Why important**: DOCK2 is connected to DGKE and has strong HPA evidence for hematopoietic and leukocyte biology. Its established function as a guanine-nucleotide exchange factor for Rho-family signaling supports lymphocyte migration, actin remodeling, and immune-cell activation. It has substantial literature and disease associations involving DOCK2 deficiency and severe immune dysfunction.
- **Conclusion**: Established evidence supports DOCK2 as an immune-cell migration and cytoskeletal-signaling gene. Its presence makes an immune-cell abundance or activation contribution plausible, but the module as a whole is not blood-cell specific in the HPA summary. The composition-related explanation therefore remains unproven.

#### PIK3CA

- **Related proteins** (co-abundance neighbors): KDM2B (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Primary cilium, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit alpha. Phosphatidylinositol 3-kinase is composed of an 85 kDa regulatory subunit and a 110 kDa catalytic subunit. The protein encoded by this gene represents the catalytic subunit, which uses ATP to phosphorylate PtdIns, PtdIns4P and PtdIns(4,5)P2. This gene has been found to be oncogenic and has been implicated in cervical cancers. A pseudogene of this gene has been defined on chromosome 22. [provided b…
- **Diseases (Open Targets)**: megalencephaly-capillary malformation-polymicrogyria syndrome (0.849); CLOVES syndrome (0.795); PIK3CA-related overgrowth spectrum (0.770); breast cancer (0.754); Cowden syndrome 5 (0.754)
- **Europe PMC papers**: 45816
- **Why important**: PIK3CA is connected to the central KDM2B hub and encodes the catalytic subunit of phosphatidylinositol kinase. Its established roles in growth-factor, insulin, vascular-development, and membrane signaling make it biologically influential despite its peripheral network position. It has extensive literature and strong disease associations, including breast cancer and PIK3CA-related overgrowth disorders.
- **Conclusion**: Established evidence supports PIK3CA as a major signaling gene relevant to breast and vascular biology. Its connection to KDM2B is a co-abundance observation rather than proof of direct regulation. It is an important contextual marker for growth and membrane signaling, but it does not by itself define the module function.
