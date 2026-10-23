# Conserved co-abundance modules: bone_marrow and breast

## Module 0

**Tissue pair**: bone_marrow and breast  
**Genes (7)**: PPP2R5D, BID, GEMIN5, HIRIP3, IST1, OLA1, PUS7L

### Function

No GO/KEGG term passed global correction, so the module does not support a formally established pathway-level annotation. Its gene-level annotations instead point to a mixed intracellular program involving RNA modification and RNA-protein or spliceosomal biology through PUS7L and GEMIN5, chromatin organization through HIRIP3, apoptosis and mitochondrial stress signaling through BID, phosphatase-mediated signal regulation through PPP2R5D, ATPase and centrosome-associated biology through OLA1, and ESCRT-linked vesicle trafficking and cell division through IST1. The co-abundance structure is hub-and-spoke: PUS7L is connected to every other member, whereas the remaining genes are peripheral and are not mutually connected. This topology favors a coordinated expression module organized around PUS7L rather than evidence for one established physical pathway. The functional interpretation should therefore remain provisional and integrative rather than being described as a significantly enriched biological process.

**Cell composition.** The module is not composed of plasma or secreted proteins: no member is annotated as secreted. Most members have low tissue specificity and low cell-type specificity, and all have low immune-cell specificity in HPA, arguing against a purely blood-cell-specific or broadly immune-specific module. There are nevertheless cell-context signals: BID is tissue-enhanced in bone marrow and enriched in several myeloid and dendritic cell populations, IST1 is cell-type enhanced in neutrophils, and HIRIP3 is enhanced in selected germ-cell and megakaryocyte-progenitor populations. Protein detection is largely present in both tissues, with exceptions for BID and HIRIP3, so the shared signal is unlikely to be explained simply by a secreted blood-protein component. The overall composition is more consistent with broadly expressed intracellular proteins plus selected hematopoietic or proliferative context than with a canonical plasma-protein signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No pair among the module genes reaches the supplied STRING interaction threshold, and STRING provides no functional enrichment. Thus the co-abundance edges are not corroborated by high-confidence known STRING protein interactions. hu.MAP provides one relevant complex association (hu.MAP huMAP3_14442.1), in which BID and OLA1 occur together as module members. Because this is a large complex with only a small subset represented in the module, it supports limited shared complex context rather than demonstrating that the whole module is one molecular complex. Taken together, the evidence favors coordinated abundance or shared cellular regulation over a pre-existing, densely documented protein-interaction complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (BID, OLA1; 2/57)

### Novelty

The conserved co-abundance pattern appears potentially novel as a cross-tissue module because its internal relationships are absent from high-confidence STRING and are only sparsely represented in hu.MAP (hu.MAP huMAP3_14442.1). However, this is not proof of a new biological mechanism: lack of database support can reflect incomplete interaction coverage, context dependence, indirect regulation, or co-regulation without physical binding. The strongest novelty claim is therefore that this particular cross-tissue abundance pattern and its hub-and-spoke organization may be previously unreported, not that every constituent gene function or relationship is new. The absence of globally corrected GO/KEGG enrichment also means that novelty cannot be framed as discovery of a statistically established new pathway.

**Hypothesis.** Hypothesis: this module reflects a conserved intracellular stress-adaptation and remodeling program coordinated around PUS7L, in which RNA modification or RNA-protein homeostasis is coupled to chromatin regulation, apoptosis control, phosphatase signaling, ATPase activity, and ESCRT-dependent trafficking. In bone marrow, the program may be strengthened by myeloid and progenitor-cell states, while in breast it may reflect a shared intracellular maintenance or proliferative context. The hypothesis predicts that PUS7L abundance will track coordinated changes in the peripheral genes, but the present data do not establish direct regulation, physical binding, causal direction, or a single common pathway.

### Important genes

#### PUS7L

- **Related proteins** (co-abundance neighbors): GEMIN5 (0.87), HIRIP3 (0.86), BID (0.83), PPP2R5D (0.83), OLA1 (0.82), IST1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in bone_marrow, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pseudouridine synthase 7 like. Predicted to enable pseudouridine synthase activity. Predicted to be involved in pseudouridine synthesis. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: gram-positive bacterial infections (0.210); immunodeficiency 67 (0.176); alcohol drinking (0.169); stroke disorder (0.155); Proptosis (0.091)
- **Europe PMC papers**: 168
- **Why important**: PUS7L is the central network hub, connecting to every other module member, and is the only gene whose network position directly links the RNA-related, apoptotic, signaling, ATPase, chromatin, and vesicle-associated annotations. Its annotated function concerns pseudouridine synthesis and RNA modification, with predicted nuclear activity. It has a moderate literature base and disease or trait associations including immunodeficiency, infection-related traits, stroke disorder, and proptosis. Its low tissue and cell-type specificity and detection in both tissues make it a plausible conserved coordinator rather than a marker restricted to one sampled cell type.
- **Conclusion**: Established: PUS7L is the topological hub and has predicted RNA-modification functions. Hypothesis: PUS7L may organize the shared module by coupling RNA homeostasis to stress, trafficking, and survival programs. The data do not establish that it regulates the other genes.

#### BID

- **Related proteins** (co-abundance neighbors): PUS7L (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: BH3 interacting domain death agonist. This gene encodes a death agonist that heterodimerizes with either agonist BAX or antagonist BCL2, and thus regulate apoptosis. The encoded protein is a member of the BCL-2 family of cell death regulators. It is a mediator of mitochondrial damage induced by caspase-8 (CASP8); CASP8 cleaves this encoded protein, and the COOH-terminal part translocates to mitochondria where it triggers cytochrome c …
- **Diseases (Open Targets)**: neurodegenerative disease (0.505); smoking initiation (0.326); neoplasm (0.104); hepatocellular carcinoma (0.092); open-angle glaucoma (0.091)
- **Europe PMC papers**: 35202
- **Why important**: BID is a peripheral neighbor of PUS7L and is the most biologically distinctive context marker in the module. It is a BCL-two-family death agonist involved in caspase-associated mitochondrial damage, cytochrome-c release, and apoptotic signaling. HPA identifies bone-marrow tissue enhancement and enrichment across dendritic, monocyte, neutrophil-progenitor, neutrophil, and plasmacytoid-dendritic-cell contexts. It has by far the largest literature volume among the members and broad disease associations including neoplasm, neurodegenerative disease, hepatocellular carcinoma, and glaucoma. It shares hu.MAP complex membership with OLA1 (hu.MAP huMAP3_14442.1).
- **Conclusion**: Established: BID supplies a strong apoptosis and hematopoietic-context interpretation and is supported by extensive literature. Hypothesis: BID may connect the conserved intracellular program to survival-versus-death decisions in bone-marrow-associated cells. Its absence from breast protein detection cautions against treating it as a uniformly expressed protein component in both tissues.

#### GEMIN5

- **Related proteins** (co-abundance neighbors): PUS7L (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gem nuclear organelle associated protein 5. This gene encodes a WD repeat protein that is a component of the survival of motor neurons (SMN) complex. The SMN complex plays a critical role in mRNA splicing through the assembly of spliceosomal small nuclear ribonucleoproteins (snRNPs), and may also mediate the assembly and transport of other classes of ribonucleoproteins. The encoded protein is the snRNA-binding component of the SMN complex. …
- **Diseases (Open Targets)**: neurodevelopmental disorder with cerebellar atrophy and motor dysfunction (0.819); hereditary disease (0.505); neurodegenerative disease (0.463); alcohol drinking (0.374); autosomal recessive non-syndromic intellectual disability (0.370)
- **Europe PMC papers**: 608
- **Why important**: GEMIN5 is directly connected to the hub PUS7L and provides the clearest RNA-processing bridge within the module. It is a component of the survival-of-motor-neurons complex, binds small nuclear RNA, and is implicated in spliceosomal small nuclear ribonucleoprotein assembly, mRNA splicing, translation regulation, and protein-containing complex assembly. It has a substantial literature base and disease associations involving neurodevelopmental and neurodegenerative disorders. Its low tissue and cell-type specificity and detection in both tissues support a broadly expressed intracellular role.
- **Conclusion**: Established: GEMIN5 participates in RNA-protein and spliceosomal biology and is co-abundant with the module hub. Hypothesis: GEMIN5 may represent the RNA-processing arm through which the module coordinates post-transcriptional adaptation. The module does not show that GEMIN5 physically interacts with PUS7L.

#### OLA1

- **Related proteins** (co-abundance neighbors): PUS7L (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, breast
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: Obg like ATPase 1. This gene encodes a member of the GTPase protein family. The encoded protein interacts with breast cancer-associated gene 1 (BRCA1) and BRCA1-associated RING domain protein (BARD1), and is involved in centrosome regulation. Overexpression of this gene has been observed in multiple types of cancer and may be associated with poor survival. Pseudogenes of this gene have been defined on chromosomes 17…
- **Diseases (Open Targets)**: urolithiasis (0.288); alcohol drinking (0.288); pilocytic astrocytoma (0.281); smoking initiation (0.278); Abnormality of the skeletal system (0.269)
- **Europe PMC papers**: 564
- **Why important**: OLA1 is a direct peripheral neighbor of PUS7L and shares the hu.MAP complex association with BID (hu.MAP huMAP3_14442.1). It is an Obg-like GTPase associated with ATP metabolism, centrosome regulation, and interactions involving BRCA1 and BARD1; its overexpression has been observed in several cancers. It has a moderate literature base and disease or trait associations including skeletal-system abnormality, pilocytic astrocytoma, urolithiasis, and smoking initiation. Its broad tissue and cell-type profile and detection in both tissues make it relevant to a conserved cellular-maintenance interpretation.
- **Conclusion**: Established: OLA1 contributes ATPase, centrosome, and cancer-related biology and is the second module member linked to BID in hu.MAP (hu.MAP huMAP3_14442.1). Hypothesis: OLA1 may connect RNA or stress adaptation to energy use and cell-cycle or centrosome control. The available evidence does not demonstrate that this connection is causal or mediated by the hu.MAP complex.

#### IST1

- **Related proteins** (co-abundance neighbors): PUS7L (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in bone_marrow, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IST1 factor associated with ESCRT-III. This gene encodes a protein with MIT-interacting motifs that interacts with components of endosomal sorting complexes required for transport (ESCRT). ESCRT functions in vesicle budding, such as that which occurs during membrane abscission in cytokinesis. There is a pseudogene for this gene on chromosome 19. Alternatively spliced transcript variants encoding multiple isoforms have been observed for…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); major depressive disorder (0.364); atrial fibrillation (0.210); Hypercholesterolemia (0.170); abdominal aortic aneurysm (0.153)
- **Europe PMC papers**: 709
- **Why important**: IST1 is a direct peripheral neighbor of PUS7L and is the module member with the clearest vesicle-trafficking annotation. It associates with ESCRT machinery and is involved in intracellular protein localization, protein transport, multivesicular-body assembly, proteolysis regulation, and cell division. It is cell-type enhanced in neutrophils, is detected in both tissues, and has a moderate literature base with associations including neurodegenerative disease, atrial fibrillation, hypercholesterolemia, and abdominal aortic aneurysm. Its vesicular localization complements the RNA, apoptosis, and ATPase annotations without requiring a direct physical interaction.
- **Conclusion**: Established: IST1 links the module to ESCRT-related trafficking and cell-division biology and shows a neutrophil-associated HPA signal. Hypothesis: IST1 may mediate a downstream remodeling or disposal response coordinated with the PUS7L-centered program. The data do not establish that the module is an ESCRT complex.

## Module 1

**Tissue pair**: bone_marrow and breast  
**Genes (39)**: NT5E, ACOX3, ACSM3, AIG1, ALG1, BAK1, CYB561D2, CHSY1, CDK5RAP1, CTTNBP2NL, CWC27, DPCD, FADS2, FN1, GCSH, H2AC21, HRNR, EPHX2, IRF4, ITGB5, CAMK2G, KRT85, LCK, PPFIBP1, LYRM7, MED1, NCF2, NUBPL, PDE7A, PPP1R3D, PRUNE1, QTMAN, RNF2, STAG1, THBS1, UQCRFS1, UFSP2, YIPF4, AZGP1

### Function

The strongest defensible interpretation is a mixed phosphoric-ester and nucleotide-signaling module, with possible links to immune-cell state, extracellular-matrix adhesion, and cellular energy metabolism. (GO:MF phosphoric ester hydrolase activity; q_global = 0.0313) is the sole GO/KEGG term that passed global correction: phosphoric ester hydrolase activity, represented by CAMK2G, EPHX2, LCK, NT5E, PDE7A, PPP1R3D, and PRUNE1. (STRING Function Phosphoric ester hydrolase activity; within-query FDR = 0.0359) independently supports the same functional theme, but is supplementary evidence rather than global significance. The module is not a single tightly connected pathway: QTMAN is the principal co-abundance hub, while the hydrolase-related genes are distributed across relatively weakly connected branches. LCK and IRF4 suggest lymphoid signaling, NT5E and PDE7A suggest extracellular nucleotide and cAMP regulation, and FN1, THBS1, and ITGB5 suggest adhesion and matrix signaling. Mitochondrial respiratory components provide an additional metabolic branch. Thus, the most cautious interpretation is coordinated regulation of phosphorylation-related and nucleotide-signaling processes in a mixed tissue or cellular context, rather than proof of one unified biochemical complex.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: only a minority of the genes are secreted, with FN1, THBS1, AZGP1, CHSY1, and possibly extracellularly exposed NT5E providing the main extracellular signal. The HPA profile is heterogeneous. Many genes have low tissue specificity, while others are enhanced in liver, lymphoid tissue, bone marrow, tongue, blood vessel, or epithelial populations. Cell-type enhancement is especially frequent for neutrophils and neutrophil progenitors, with additional signals from B cells, T cells, dendritic cells, megakaryocytes, platelets, and epithelial populations. IRF4 and LCK are strongly compatible with lymphoid material; NCF2 is compatible with neutrophils; and H2AC21, PPP1R3D, and PRUNE1 are compatible with hematopoietic or platelet associated populations. AZGP1 and several epithelial or skin-associated genes introduce a breast or epithelial component. Therefore, the shared module may partly reflect shared blood, immune, stromal, epithelial, or vascular cell content across the tissues, rather than a tissue-specific program. Protein detection in both tissues for many genes supports detectability, but does not establish that the same cell type expresses the complete module in both.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF phosphoric ester hydrolase activity | 0.0313 | CAMK2G, EPHX2, LCK, NT5E, PDE7A, PPP1R3D, PRUNE1 |

### STRING and hu.MAP

STRING provides a small set of high-confidence relationships rather than a densely interconnected network. The most informative known links are FN1 with ITGB5 and THBS1, EPHX2 with NT5E, and NT5E with PDE7A. These relationships support an extracellular-matrix and nucleotide-signaling subnetwork. The STRING link involving LYRM7 and UQCRFS1 supports a mitochondrial respiratory-complex branch. The remaining co-abundance edges are not confirmed by the listed high-confidence STRING interactions, so co-abundance should not be interpreted as direct physical binding. hu.MAP repeatedly places LYRM7 and UQCRFS1 together in complexes containing mitochondrial respiratory-chain components, providing consistent complex-level support for that branch. hu.MAP also places AZGP1 and HRNR in several large epithelial or cornified-envelope-associated complexes, although these are only partial overlaps and do not establish that the entire module is one complex. Overall, known interaction evidence supports several local subnetworks but argues against a single established multiprotein assembly spanning all module genes.

**STRING interactions (score >= 0.7)**: 7 of 741 gene pairs: EPHX2–NT5E (0.795); FN1–ITGB5 (0.995); FN1–NT5E (0.737); FN1–THBS1 (0.999); ITGB5–THBS1 (0.859); LYRM7–UQCRFS1 (0.959); NT5E–PDE7A (0.769)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Phosphoric ester hydrolase activity (FDR = 0.0359, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04728.1 (UQCRFS1, LYRM7; 2/3); huMAP3_01826.1 (UQCRFS1, LYRM7; 2/4); huMAP3_07870.1 (UQCRFS1, LYRM7; 2/4); huMAP3_07890.1 (UQCRFS1, LYRM7; 2/4); huMAP3_07021.1 (UQCRFS1, LYRM7; 2/5); huMAP3_10294.1 (UQCRFS1, LYRM7; 2/6); huMAP3_12621.1 (UQCRFS1, LYRM7; 2/22); huMAP3_14580.1 (UQCRFS1, LYRM7; 2/23); huMAP3_05845.1 (AZGP1, HRNR; 2/24); huMAP3_10623.1 (UQCRFS1, LYRM7; 2/24); huMAP3_08595.1 (AZGP1, HRNR; 2/25); huMAP3_12170.1 (UQCRFS1, LYRM7; 2/25); huMAP3_12457.1 (UQCRFS1, LYRM7; 2/31); huMAP3_09125.1 (AZGP1, HRNR; 2/53); huMAP3_09929.1 (AZGP1, HRNR; 2/75)

### Novelty

The co-abundance module may be a new observation in this particular bone-marrow and breast comparison, but the available evidence is insufficient to call it a new biological mechanism. Several component relationships and functions are already established in STRING, hu.MAP, HPA, and the supplied gene annotations, especially the FN1–THBS1–ITGB5 adhesion branch, the NT5E–PDE7A and EPHX2–NT5E signaling links, and the LYRM7–UQCRFS1 mitochondrial relationship. Conversely, the overall combination of these genes, its cross-tissue co-abundance, and the central position of QTMAN are not shown in the supplied resources to constitute a previously described module. Database absence for individual edges or complexes is not evidence of novelty, particularly because co-abundance can arise from shared cell composition, regulation, or technical effects. A novelty claim would require replication in independent cohorts, cell-type-aware analysis, and comparison with published co-expression modules.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program in which immune or hematopoietic cells, together with stromal, vascular, or epithelial cells, coordinate extracellular nucleotide handling and cyclic-nucleotide signaling with adhesion and matrix interactions. NT5E could shape extracellular nucleotide availability, PDE7A could tune intracellular cAMP responses, and EPHX2 could connect lipid or phospholipid metabolism to that signaling state. LCK and IRF4 could mark the lymphoid component, while FN1, THBS1, and ITGB5 could represent matrix-mediated retention or migration. The mitochondrial LYRM7–UQCRFS1 branch may reflect energetic support for the shared cellular state, rather than direct participation in the hydrolase pathway. This is a testable hypothesis, not an established causal model; single-cell localization, perturbation of NT5E or PDE7A, and replication across tissue cohorts would be needed.

### Important genes

#### QTMAN

- **Related proteins** (co-abundance neighbors): UFSP2 (0.99), PRUNE1 (0.96), PPP1R3D (0.92), FN1 (0.92), CAMK2G (0.92), THBS1 (0.90), GCSH (0.90), AZGP1 (0.89), UQCRFS1 (0.87), EPHX2 (0.87), DPCD (0.83), H2AC21 (0.82), ACOX3 (0.80), HRNR (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: queuosine-tRNA mannosyltransferase. Predicted to enable glycosyltransferase activity. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Oral ulcer (0.396); intelligence (0.395); osteoporosis (0.340); open-angle glaucoma (0.316); chronic atrophic gastritis (0.301)
- **Europe PMC papers**: 10
- **Why important**: QTMAN is the central co-abundance hub and has the strongest network position in the module, connecting multiple branches that include PRUNE1, PPP1R3D, FN1, CAMK2G, THBS1, GCSH, and AZGP1. Its annotation supports a role in queuosine-tRNA mannosylation and translation regulation, but it has no listed STRING or hu.MAP support in this module and only limited literature. It is therefore important primarily as the network organizer and as a candidate marker of the shared co-abundance state, not as an established pathway driver.
- **Conclusion**: Established evidence supports QTMAN as the module's strongest co-abundance connector and as a tRNA-modification factor. Its role in coordinating the other module branches is a hypothesis requiring functional testing.

#### NT5E

- **Related proteins** (co-abundance neighbors): PDE7A (0.83); STRING partners: EPHX2 (0.795), FN1 (0.737), PDE7A (0.769)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in bone_marrow, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 5'-nucleotidase ecto. The protein encoded by this gene is a plasma membrane protein that catalyzes the conversion of extracellular nucleotides to membrane-permeable nucleosides. The encoded protein is used as a determinant of lymphocyte differentiation. Defects in this gene can lead to the calcification of joints and arteries. Two transcript variants encoding different isoforms have been found for this gene.[provided b…
- **Diseases (Open Targets)**: hereditary arterial and articular multiple calcification syndrome (0.721); autosomal recessive spinocerebellar ataxia 20 (0.556); Spinocerebellar atrophy (0.340); non-small cell lung carcinoma (0.329); placental abruption (0.289)
- **Europe PMC papers**: 4404
- **Why important**: NT5E belongs to (GO:MF phosphoric ester hydrolase activity; q_global = 0.0313) and (STRING Function Phosphoric ester hydrolase activity; within-query FDR = 0.0359), is a plasma-membrane ectonucleotidase, and connects in STRING to PDE7A, EPHX2, and FN1. Its annotations link extracellular nucleotide catabolism with leukocyte adhesion and biomineral tissue development. HPA detects it in both tissues and associates it with immune-cell populations, making it a strong bridge between signaling, cell composition, and the extracellular environment. Its disease associations include hereditary arterial and articular calcification, which is relevant to a bone-associated context.
- **Conclusion**: Established evidence supports NT5E as a central extracellular nucleotide regulator and as a known interaction bridge within the module. Its role as a causal coordinator of the shared tissue program remains a hypothesis.

#### PDE7A

- **Related proteins** (co-abundance neighbors): CDK5RAP1 (0.93), NUBPL (0.89), PPFIBP1 (0.88), NT5E (0.83), CTTNBP2NL (0.83), RNF2 (0.82), CHSY1 (0.82), ITGB5 (0.81); STRING partners: NT5E (0.769)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphodiesterase 7A. The protein encoded by this gene belongs to the cyclic nucleotide phosphodiesterase (PDE) family, and PDE7 subfamily. This PDE hydrolyzes the second messenger, cAMP, which is a regulator and mediator of a number of cellular responses to extracellular signals. Thus, by regulating the cellular concentration of cAMP, this protein plays a key role in many important physiological processes. Alternative…
- **Diseases (Open Targets)**: stroke disorder (0.554); coronary artery disorder (0.543); Abnormality of the skeletal system (0.536); dysuria (0.462); intermittent vascular claudication (0.434)
- **Europe PMC papers**: 817
- **Why important**: PDE7A belongs to (GO:MF phosphoric ester hydrolase activity; q_global = 0.0313) and (STRING Function Phosphoric ester hydrolase activity; within-query FDR = 0.0359), occupies a relatively prominent network position, and has the listed STRING relationship with NT5E. It hydrolyzes cAMP and is therefore mechanistically suited to connect extracellular nucleotide conditions with intracellular signal responsiveness. HPA shows lymphoid and several immune-related cell-type enhancements, while the supplied disease associations include vascular and skeletal abnormalities. Its literature volume is substantial compared with most module genes, making its function comparatively well established.
- **Conclusion**: Established evidence supports PDE7A as a cAMP-regulating enzyme linked to the NT5E branch. Its participation in a shared bone-marrow and breast co-abundance program, and any causal relationship to that program, remain hypotheses.

#### IRF4

- **Related proteins** (co-abundance neighbors): PRUNE1 (0.86), PPP1R3D (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: interferon regulatory factor 4. The protein encoded by this gene belongs to the IRF (interferon regulatory factor) family of transcription factors, characterized by an unique tryptophan pentad repeat DNA-binding domain. The IRFs are important in the regulation of interferons in response to infection by virus, and in the regulation of interferon-inducible genes. This family member is lymphocyte specific and negatively regulates T…
- **Diseases (Open Targets)**: B-cell chronic lymphocytic leukemia (0.642); plasma cell myeloma (0.562); melanoma (0.557); skin cancer (0.554); skin neoplasm (0.548)
- **Europe PMC papers**: 15402
- **Why important**: IRF4 is directly connected in the module to PRUNE1 and PPP1R3D and has strong HPA support for bone marrow, lymphoid tissue, B-cell, dendritic-cell, and regulatory T-cell populations. Its established function as a lymphocyte-associated transcription factor regulating immune and cytokine programs gives biological context to the immune-cell component of the module. It also has the largest literature volume among the listed genes and established associations with B-cell malignancy, plasma-cell myeloma, and melanoma.
- **Conclusion**: Established evidence supports IRF4 as a marker and regulator of lymphoid cellular state. The module data support an immune-composition interpretation, but do not show that IRF4 transcriptionally controls the other module genes.

#### FN1

- **Related proteins** (co-abundance neighbors): QTMAN (0.92); STRING partners: ITGB5 (0.995), NT5E (0.737), THBS1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in bone_marrow, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 is a secreted extracellular-matrix protein with a strong network connection to QTMAN and high-confidence STRING relationships with ITGB5, NT5E, and THBS1. Its functions in adhesion, migration, wound healing, coagulation, and matrix signaling make it a plausible interface between stromal or vascular material and immune-cell retention. HPA identifies it as secreted to blood and detected in both tissues, while its disease and literature associations are extensive.
- **Conclusion**: Established evidence supports FN1 as an extracellular-matrix and adhesion component with known links to several module proteins. Its presence may reflect stromal, vascular, or circulating material; a specific role in the shared module is a hypothesis.

## Module 2

**Tissue pair**: bone_marrow and breast  
**Genes (7)**: ALB, HBA1, CAMK1D, NIT2, SLC39A11, SESN2, UCHL3

### Function

The strongest supported function is cellular protection against oxidative or toxic stress, including oxidant detoxification and oxygen-related biology. This interpretation is driven by the globally corrected GO terms (GO:MF antioxidant activity; q_global = 0.0181) through (GO:BP detoxification; q_global = 0.0437), all of which converge on antioxidant activity, cellular oxidant detoxification, oxygen binding, and cellular detoxification. ALB, HBA1, and SESN2 provide the primary functional signal. HBA1 supports oxygen, carbon dioxide, and nitric oxide handling, ALB has documented links to oxidative-stress responses and heme-related processes, and SESN2 is a stress-response regulator associated with cell survival, growth control, amino-acid starvation responses, and autophagy. The network topology also suggests that SESN2 is the central connector linking otherwise weakly connected genes. This is a functional interpretation of the co-abundance pattern, not proof that all genes participate in one molecular pathway.

**Cell composition.** The module is compositionally mixed rather than a uniformly breast- or bone-marrow-specific program. ALB is a liver-enriched, hepatocyte-enriched protein secreted to blood, and is not detected in immune cells; its presence can reflect circulating plasma protein or sample carryover rather than local production. HBA1 is enriched in bone marrow and lymphoid tissue and in erythrocytes, with additional blood-cell enrichment reported by HPA, so it may reflect erythroid or blood-associated material. Only ALB is annotated as secreted, so most module genes are not plasma proteins. SESN2, UCHL3, and SLC39A11 have low tissue specificity, while NIT2 is liver-enhanced and CAMK1D is enhanced in brain and retina and associated with granulocyte-related cell types. The HPA profile therefore supports a mixture of broadly expressed or housekeeping-like intracellular genes, blood or erythroid contribution, and possible plasma contribution. The shared signal could consequently reflect blood content, shared cell types, or systemic protein abundance in the samples rather than a breast-intrinsic mechanism.

**GO/KEGG enrichment**: 6 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF antioxidant activity | 0.0181 | ALB, HBA1, SESN2 |
| GO:BP cellular oxidant detoxification | 0.0253 | ALB, HBA1, SESN2 |
| GO:MF oxygen binding | 0.0277 | ALB, HBA1 |
| GO:BP cellular response to toxic substance | 0.0411 | ALB, HBA1, SESN2 |
| GO:BP cellular detoxification | 0.0411 | ALB, HBA1, SESN2 |
| GO:BP detoxification | 0.0437 | ALB, HBA1, SESN2 |

### STRING and hu.MAP

The STRING evidence is weak for direct molecular connectivity: no high-confidence STRING interaction is present among the module genes. The STRING hemoglobin-complex enrichment (STRING COMPARTMENTS Hemoglobin complex; within-query FDR = 0.0335) is supplementary and is driven by ALB and HBA1; it should not be treated as globally corrected enrichment. hu.MAP provides one complex-level connection (hu.MAP huMAP3_15040.1), in which ALB and HBA1 occur together within a large, heterogeneous complex annotation. This supports some prior biochemical or proteomic co-membership, but the limited module representation and modest complex confidence do not establish a compact physical complex. Overall, the co-abundance edges are not corroborated by a dense known interaction network. The pattern is more consistent with coordinated abundance, shared sample composition, or a stress-related association than with a well-established protein complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Hemoglobin complex (FDR = 0.0335, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (ALB, HBA1; 2/64)

### Novelty

The exact conserved co-abundance module may be a new observation because the supplied resources do not show a matching dense STRING network or a module-specific hu.MAP complex. However, it would be inappropriate to call the underlying biology entirely novel. Oxidative-stress and detoxification functions are already established for SESN2, ALB, and HBA1, and ALB with HBA1 has prior complex-level support (hu.MAP huMAP3_15040.1) and supplementary hemoglobin-complex support (STRING COMPARTMENTS Hemoglobin complex; within-query FDR = 0.0335). The absence of a STRING or hu.MAP interaction is not evidence of novelty by itself. The defensible conclusion is that the cross-tissue co-abundance configuration is potentially novel, while its component functions and some of its protein associations are established. Its biological specificity remains uncertain because of the blood and plasma composition signals.

**Hypothesis.** Hypothesis: the module reflects a shared oxidative-stress and detoxification state superimposed on variable blood or plasma content in bone-marrow and breast samples. In this model, SESN2 acts as a stress-responsive intracellular coordinator, while HBA1 marks erythroid or blood-associated oxygen and redox biology and ALB represents circulating plasma protein with antioxidant, carrier, and detoxification-related properties. CAMK1D, SLC39A11, UCHL3, and NIT2 could be co-abundant markers of cell-state regulation, metal or nutrient handling, proteostasis, and intermediary metabolism, respectively. This hypothesis predicts that the module will track sample blood fraction and oxidative-stress state more strongly than a breast epithelial program; it requires validation with cell deconvolution, protein localization, and independent cohorts.

### Important genes

#### SESN2

- **Related proteins** (co-abundance neighbors): NIT2 (0.90), UCHL3 (0.89), SLC39A11 (0.88), CAMK1D (0.84), ALB (0.82), HBA1; HBA2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sestrin 2. This gene encodes a member of the sestrin family of PA26-related proteins. The encoded protein may function in the regulation of cell growth and survival. This protein may be involved in cellular response to different stress conditions. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.326); benign urinary system neoplasm (0.182); exostosis (0.110); neoplasm (0.106); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 2337
- **Why important**: SESN2 is the network hub, connecting the other module members in the supplied co-abundance graph. It is present in nearly all primary GO terms (GO:MF antioxidant activity; q_global = 0.0181), (GO:BP cellular oxidant detoxification; q_global = 0.0253), (GO:BP cellular response to toxic substance; q_global = 0.0411), (GO:BP cellular detoxification; q_global = 0.0411), and (GO:BP detoxification; q_global = 0.0437), and its established annotations include stress responses, regulation of growth, protein phosphorylation, autophagy, and amino-acid starvation responses. Its disease literature is substantial, including links to neurodegenerative disease, neoplasm, hepatocellular carcinoma, and exostosis. Its central network position and direct overlap with the detoxification signal make it the strongest candidate for organizing the module's intracellular stress component.
- **Conclusion**: Established evidence supports SESN2 as a stress-response and cellular-protection gene and as the central co-abundance connector. It is plausible, but not established, that SESN2 coordinates the entire module or links the intracellular genes to circulating ALB and erythroid HBA1.

#### ALB

- **Related proteins** (co-abundance neighbors): SESN2 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB contributes to every primary GO term (GO:MF antioxidant activity; q_global = 0.0181) through (GO:BP detoxification; q_global = 0.0437), is the most abundant protein in blood according to the supplied annotation, and functions as a carrier with broad ligand-binding and detoxification relevance. It is liver- and hepatocyte-enriched, secreted to blood, and not detected in immune cells by HPA. It also participates with HBA1 in the hu.MAP complex (hu.MAP huMAP3_15040.1) and the supplementary STRING hemoglobin-complex term (STRING COMPARTMENTS Hemoglobin complex; within-query FDR = 0.0335). ALB has the largest literature volume among the module genes and established disease associations including congenital analbuminemia, hyperthyroxinemia, and chronic kidney disease.
- **Conclusion**: Established evidence supports ALB as a circulating plasma protein that can contribute to antioxidant, carrier, and detoxification annotations. In this module, its presence may be a biological signal of plasma exposure or sample composition rather than evidence of local ALB synthesis in breast or bone marrow.

#### HBA1

- **Related proteins** (co-abundance neighbors): none; STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Group enriched; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: hemoglobin subunit alpha 1. The human alpha globin gene cluster located on chromosome 16 spans about 30 kb and includes seven loci: 5'- zeta - pseudozeta - mu - pseudoalpha-1 - alpha-2 - alpha-1 - theta - 3'. The alpha-2 (HBA2) and alpha-1 (HBA1) coding sequences are identical. These genes differ slightly over the 5' untranslated regions and the introns, but they differ significantly over the 3' untranslated regions. Two alp…
- **Diseases (Open Targets)**: alpha thalassemia spectrum (0.758); hemoglobin H disease (0.755); hemoglobin M disease (0.735); Heinz body anemia (0.698); primary familial polycythemia due to EPO receptor mutation (0.689)
- **Europe PMC papers**: 4551
- **Why important**: HBA1 contributes to every primary GO term (GO:MF antioxidant activity; q_global = 0.0181) through (GO:BP detoxification; q_global = 0.0437), including the oxygen-binding term (GO:MF oxygen binding; q_global = 0.0277), and is annotated for oxygen, carbon dioxide, and nitric oxide transport as well as hydrogen-peroxide-related biology. HPA places it in a bone-marrow, lymphoid, and erythrocyte context and reports blood-cell enrichment. It also occurs with ALB in (hu.MAP huMAP3_15040.1) and (STRING COMPARTMENTS Hemoglobin complex; within-query FDR = 0.0335). Its disease associations include alpha-thalassemia spectrum, hemoglobin H disease, hemoglobin M disease, and Heinz body anemia, and it has a substantial literature base.
- **Conclusion**: Established evidence supports HBA1 as an erythroid oxygen- and redox-related marker that drives much of the module's functional enrichment. Its isolated position in the supplied subgraph argues against treating it as a demonstrated physical interaction partner of the other genes; it may instead report blood or erythroid content.

#### CAMK1D

- **Related proteins** (co-abundance neighbors): SESN2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium/calmodulin dependent protein kinase ID. This gene is a member of the calcium/calmodulin-dependent protein kinase 1 family, a subfamily of the serine/threonine kinases. The encoded protein is a component of the calcium-regulated calmodulin-dependent protein kinase cascade. It has been associated with multiple processes including regulation of granulocyte function, activation of CREB-dependent gene transcription, aldosterone synthesis, di…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.499); diabetes mellitus (0.481); type 2 diabetes nephropathy (0.409); coronary artery disorder (0.358); diabetic retinopathy (0.353)
- **Europe PMC papers**: 1804
- **Why important**: CAMK1D is directly connected to SESN2 in the module and has annotations linking calcium-calmodulin kinase signaling to granulocyte function, neutrophil differentiation and activation, phagocytosis, respiratory burst, and CREB-dependent transcription. HPA reports tissue enhancement in brain and retina, cell-type enrichment involving photoreceptors and neutrophils, and immune-cell enhancement in eosinophils. Its disease associations include diabetes, diabetic nephropathy, coronary artery disorder, and diabetic retinopathy, with a substantial literature base.
- **Conclusion**: Established evidence supports CAMK1D as a signaling kinase with granulocyte and respiratory-burst relevance. Its participation could connect the module to immune-cell oxidative responses, but the supplied data do not establish that CAMK1D mediates the ALB-HBA1 detoxification signal or that the module is immune-cell intrinsic.

#### NIT2

- **Related proteins** (co-abundance neighbors): SESN2 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nitrilase family member 2. Enables omega-amidase activity. Involved in asparagine metabolic process; glutamine metabolic process; and oxaloacetate metabolic process. Located in centrosome and cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: synovium disorder (0.187); neoplasm (0.079); lung adenocarcinoma (0.074); poisoning (0.037); glaucoma (0.028)
- **Europe PMC papers**: 977
- **Why important**: NIT2 is directly connected to the SESN2 hub and is tissue-enhanced in liver and cell-type-enhanced in hepatocytes. Its annotated omega-amidase activity and roles in asparagine, glutamine, oxaloacetate, and methionine-salvage metabolism provide a metabolic context for stress adaptation. It is detected by HPA in both bone marrow and breast, and it has disease associations involving synovium disorder, neoplasm, lung adenocarcinoma, poisoning, and glaucoma, with a meaningful literature base.
- **Conclusion**: Established evidence supports NIT2 as a metabolic enzyme associated with liver and hepatocyte biology and with the SESN2-centered co-abundance pattern. Its role in this module is best viewed as a possible metabolic companion to stress regulation, not as an established detoxification effector.

## Module 3

**Tissue pair**: bone_marrow and breast  
**Genes (10)**: CYBB, CTBS, F9, GOLT1B, ICAM1, IFIT3, LACTB2, NUDT6, PSMB10, GTF2H1

### Function

This module does not support a single formally enriched GO or KEGG function: no term passed global correction. Its strongest interpretive signal is a mixed immune and inflammatory context, with CYBB linked to phagocyte oxidative defense, ICAM1 linked to leukocyte adhesion and extravasation, IFIT3 linked to antiviral innate responses, and PSMB10 linked to proteasomal processing and antigen presentation. F9 contributes an established coagulation function, while GOLT1B, GTF2H1, CTBS, LACTB2, and NUDT6 represent vesicle transport, transcription and DNA repair, glycan degradation, RNA processing, and regulatory biology. The network is therefore better interpreted as a co-abundance program associated with immune or blood-related cellular context and general cellular state than as evidence for a single biochemical pathway.

**Cell composition.** The module is not predominantly a plasma or secreted-protein module, although F9 is a liver-enriched secreted blood protein and the HPA summary identifies secreted genes. Several genes show immune-related cell-type enhancement, including monocytes, neutrophils, macrophages, microglia, Kupffer cells, and monocyte progenitors. CYBB is enhanced in bone marrow and lymphoid tissue, PSMB10 is enhanced in lymphoid tissue, and ICAM1 is enhanced in lung and urinary bladder with immune-associated cell types. At the same time, most genes have low tissue specificity or broad cellular distributions, and several are intracellular housekeeping-like components. The shared bone-marrow and breast signal could therefore reflect shared immune or stromal cellular composition, circulating blood material, or a broad cellular-state program rather than a breast-specific mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was detected among the module genes, and no STRING functional-enrichment result was available. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated by the supplied physical-interaction or curated-complex resources. The strongest network position belongs to NUDT6, which connects to ICAM1, IFIT3, CTBS, PSMB10, and LACTB2. F9 forms a separate bridge connecting GOLT1B, ICAM1, GTF2H1, and CYBB. These topological relationships describe coordinated abundance in the data, not established direct molecular binding. The absence of STRING and hu.MAP support makes a shared expression or cellular-composition explanation more plausible than a demonstrated multiprotein complex.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported co-abundance pattern in this tissue-pair analysis because the supplied resources provide no known STRING interactions, no shared hu.MAP complex, and no globally significant GO or KEGG term. However, those absences do not establish biological novelty. Several component functions are already well established, including coagulation for F9, leukocyte adhesion for ICAM1, phagocyte oxidase activity for CYBB, antiviral signaling for IFIT3, and proteasomal activity for PSMB10. A defensible conclusion is that the coordinated module-level pattern appears novel or at least not explained by the queried interaction resources, while its individual gene biology is not novel.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of immune-associated and circulating components across bone marrow and breast, potentially driven by shared myeloid or other immune-cell representation together with blood-derived protein contribution. In this model, CYBB, ICAM1, IFIT3, and PSMB10 mark inflammatory, innate-defense, adhesion, and antigen-processing states; F9 represents a circulating coagulation component; and NUDT6 may act as a data-defined regulatory hub that co-varies with these states rather than directly binding them. This hypothesis requires validation with cell deconvolution, independent cohorts, protein-level measurements, and targeted tests of whether the module tracks immune-cell abundance or local inflammatory activation.

### Important genes

#### NUDT6

- **Related proteins** (co-abundance neighbors): ICAM1 (0.87), IFIT3 (0.87), CTBS (0.82), PSMB10 (0.81), LACTB2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nudix hydrolase 6. This gene overlaps and lies on the opposite strand from FGF2 gene, and is thought to be the FGF2 antisense gene. The two genes are independently transcribed, and their expression shows an inverse relationship, suggesting that this antisense transcript may regulate FGF2 expression. This gene has also been shown to have hormone-regulatory and antiproliferative actions in the pituitary that are indep…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.439); neurodegenerative disease (0.404); atrial fibrillation (0.399); type 2 diabetes mellitus (0.224); arthropathy (0.188)
- **Europe PMC papers**: 274
- **Why important**: NUDT6 is the central network hub, connecting to ICAM1, IFIT3, CTBS, PSMB10, and LACTB2. Its annotation includes negative regulation of cell proliferation and cell-cycle regulation, and it has a reported antisense relationship with FGF2 together with hormone-regulatory and antiproliferative actions. It is detected in both tissues and has disease associations spanning skeletal abnormality, neurodegenerative disease, atrial fibrillation, and metabolic disease. Its literature is more limited than that of the best-studied immune genes, which makes its hub status especially informative for generating a module-specific hypothesis.
- **Conclusion**: Established evidence supports NUDT6 as the network hub and supports regulatory and antiproliferative functions from the supplied annotations. It is not established that NUDT6 mechanistically organizes the other module genes; its hub role may instead reflect coordinated expression or an unmeasured cellular-state factor.

#### ICAM1

- **Related proteins** (co-abundance neighbors): NUDT6 (0.87), F9 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: intercellular adhesion molecule 1. This gene encodes a cell surface glycoprotein which is typically expressed on endothelial cells and cells of the immune system. It binds to integrins of type CD11a / CD18, or CD11b / CD18 and is also exploited by Rhinovirus as a receptor. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.528); atrial fibrillation (0.407); vascular disorder (0.358); Crohn disease (0.340); lymphatic system disorder (0.285)
- **Europe PMC papers**: 19543
- **Why important**: ICAM1 connects the NUDT6 and F9 portions of the network and encodes a plasma-membrane adhesion molecule expressed on endothelial and immune cells. Its annotations include leukocyte cytotoxicity, T-cell contact with antigen-presenting cells, cellular extravasation, immune response, and cell adhesion. HPA links it to macrophages, monocytes, Kupffer cells, and lung cell types, and it has extensive disease-oriented literature including vascular, inflammatory, and neurodegenerative associations.
- **Conclusion**: Established evidence strongly supports ICAM1 as an immune-cell adhesion and trafficking marker. Its position may make it a biological bridge between circulating coagulation-related abundance and cellular immune activation, but a direct regulatory connection to F9 or NUDT6 is only a hypothesis.

#### CYBB

- **Related proteins** (co-abundance neighbors): F9 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome b-245 beta chain. Cytochrome b (-245) is composed of cytochrome b alpha (CYBA) and beta (CYBB) chain. It has been proposed as a primary component of the microbicidal oxidase system of phagocytes. CYBB deficiency is one of five described biochemical defects associated with chronic granulomatous disease (CGD). In this disorder, there is decreased activity of phagocyte NADPH oxidase; neutrophils are able to phagocytiz…
- **Diseases (Open Targets)**: chronic granulomatous disease (0.864); neurodegenerative disease (0.352); hereditary disease (0.191); discoid lupus erythematosus (0.185); Kartagener Syndrome (0.118)
- **Europe PMC papers**: 6704
- **Why important**: CYBB is associated with bone marrow and lymphoid tissue and is enhanced in classical monocytes, macrophages, microglia, Kupffer cells, and monocyte progenitors. It encodes a core component of the phagocyte NADPH oxidase and is annotated for superoxide metabolism, defense, inflammation, and tumor-necrosis-factor regulation. Its disease evidence includes chronic granulomatous disease and other inflammatory or hereditary disorders, and its literature is substantial.
- **Conclusion**: Established evidence supports CYBB as a marker and mediator of phagocyte antimicrobial and oxidative defense. Its co-abundance with F9 and ICAM1 is consistent with an immune or blood-associated sample signal, but the module does not establish a new CYBB-specific mechanism.

#### F9

- **Related proteins** (co-abundance neighbors): GOLT1B (0.87), ICAM1 (0.86), GTF2H1 (0.82), CYBB (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coagulation factor IX. This gene encodes vitamin K-dependent coagulation factor IX that circulates in the blood as an inactive zymogen. This factor is converted to an active form by factor XIa, which excises the activation peptide and thus generates a heavy chain and a light chain held together by one or more disulfide bonds. The role of this activated factor IX in the blood coagulation cascade is to activate factor X t…
- **Diseases (Open Targets)**: hemophilia B (0.890); hemophilia A (0.763); thrombophilia, X-linked, due to factor 9 defect (0.747); x-linked warfarin sensitivity (0.694); hemorrhage (0.581)
- **Europe PMC papers**: 13996
- **Why important**: F9 is a liver-enriched, hepatocyte-enriched protein that is secreted into blood and functions as a vitamin K-dependent coagulation factor in the intrinsic pathway. It has the strongest disease and literature support among the module genes, especially for hemophilia B, thrombophilia, warfarin sensitivity, and hemorrhage. In the co-abundance graph it connects GOLT1B, ICAM1, GTF2H1, and CYBB, making it a prominent bridge between a circulating protein signal and intracellular or immune-associated genes.
- **Conclusion**: Established evidence supports F9 as a circulating coagulation protein and a plausible indicator of blood-derived material. Its network connections should not be interpreted as direct physical interactions; they may reflect shared sample composition or coordinated tissue-associated abundance.

#### PSMB10

- **Related proteins** (co-abundance neighbors): NUDT6 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in bone_marrow, breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 20S subunit beta 10. The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent proc…
- **Diseases (Open Targets)**: proteasome-associated autoinflammatory syndrome 5 (0.634); plasma cell myeloma (0.604); immunodeficiency 121 with autoinflammation (0.578); mantle cell lymphoma (0.542); neoplasm (0.529)
- **Europe PMC papers**: 1477
- **Why important**: PSMB10 is enhanced in lymphoid tissue and in monocytes, monocyte progenitors, and NK cells. It is a proteasome subunit associated with immune-system processes, antigen processing and presentation, and proteasomal protein catabolism. It is detected in both tissues and has disease associations involving proteasome-associated autoinflammation, plasma-cell myeloma, immunodeficiency, lymphoma, and neoplasia. Its link to the NUDT6 hub gives it importance as an intracellular immune-state component.
- **Conclusion**: Established evidence supports PSMB10 as an immune-relevant proteasomal component connected to antigen processing and protein turnover. Its module association is compatible with immune-cell representation or activation, but the available evidence does not show that it forms a new complex with NUDT6 or the other module members.
