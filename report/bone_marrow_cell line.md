# Conserved co-abundance modules: bone_marrow and cell line

## Module 0

**Tissue pair**: bone_marrow and cell line  
**Genes (40)**: PPP2R2A, ANKRD28, ANKRD44, ARSB, AURKA, COX20, SLC44A1, DAAM2, DBR1, DIAPH2, TMEM68, HLA-DRA, FASTKD1, GMEB2, INSR, IQGAP2, IRF3, ITGA4, PRKACG, KIF1C, MBD3, METTL8, KIAA0753, NAMPT, NEK6, PPP4R3B, PI4KA, PSMG4, RAD9A, POLR1A, MRPS11, SH3TC1, TSEN2, SIRT7, SYNE2, TMC6, TTC38, UBR2, VRK3, WDFY4

### Function

No GO or KEGG term passed global correction, and STRING reported no supplementary functional enrichment. The module therefore does not support a single statistically established pathway-level function. Its gene annotations instead suggest a heterogeneous cellular-maintenance program spanning transcriptional and epigenetic regulation, RNA processing, mitochondrial maintenance, cell-cycle control, cytoskeletal organization, membrane transport, adhesion, and immune antigen presentation. The network is sparse and appears to contain several partially connected functional neighborhoods rather than one coherent pathway. The strongest internally connected features include the PRKACG-centered neighborhood, the KIAA0753-centered neighborhood, and the SIRT7-linked neighborhood. These observations support a cautious interpretation as a shared cellular-state or cell-composition-associated module rather than a definitively defined biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only NAMPT is annotated as secreted to blood, while ARSB is annotated as intracellular and membrane associated and ITGA4 as intracellular and membrane associated. The HPA profile argues against a purely housekeeping interpretation. Most genes have low tissue specificity or tissue-enhanced expression, but many show cell-type enhancement in hematopoietic or immune populations. Neutrophils and neutrophil progenitors are recurrently represented, with additional signals from dendritic cells, B cells, natural killer cells, macrophages, microglia, and other immune populations. WDFY4, HLA-DRA, ITGA4, SH3TC1, ANKRD44, and NAMPT particularly support a hematopoietic or immune-cell component. The strong protein detection in bone marrow and the lack of a matching HPA tissue for the cell-line comparison mean that the shared signal may partly reflect common cell states or shared hematopoietic-like cellular composition rather than a tissue-specific secreted program. The testis, brain, liver, and epithelial-cell annotations also indicate that the module is not restricted to one lineage.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The high-confidence STRING evidence is limited but non-random. ANKRD28 and ANKRD44 form a known relationship, NAMPT and SIRT7 form a strong known relationship, and POLR1A connects with MRPS11 and SIRT7. These links support a small connected core involving regulatory, metabolic, nucleolar, and mitochondrial functions, but they do not establish the entire module as one known complex. hu.MAP provides recurring pairwise co-membership for ANKRD28 with ANKRD44 in (hu.MAP huMAP3_01958.1), (hu.MAP huMAP3_14031.1), and (hu.MAP huMAP3_12079.1), and for METTL8 with GMEB2 in (hu.MAP huMAP3_14447.1), (hu.MAP huMAP3_12824.1), and (hu.MAP huMAP3_13917.1). The NAMPT and FASTKD1 pairing in (hu.MAP huMAP3_11084.1) adds a mitochondrial or metabolic context. However, each hu.MAP complex contains only a small subset of module members, with many additional complex members outside the module. Thus, the evidence supports several known local relationships and possible complex fragments, not a single experimentally established module-wide complex.

**STRING interactions (score >= 0.7)**: 4 of 780 gene pairs: ANKRD28–ANKRD44 (0.893); MRPS11–POLR1A (0.804); NAMPT–SIRT7 (0.948); POLR1A–SIRT7 (0.738)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14447.1 (METTL8, GMEB2; 2/7); huMAP3_01958.1 (ANKRD28, ANKRD44; 2/8); huMAP3_14031.1 (ANKRD28, ANKRD44; 2/10); huMAP3_12824.1 (METTL8, GMEB2; 2/10); huMAP3_12079.1 (ANKRD28, ANKRD44; 2/12); huMAP3_11084.1 (NAMPT, FASTKD1; 2/27); huMAP3_13917.1 (METTL8, GMEB2; 2/33)

### Novelty

This module should not be called a wholly new biological pathway. Several relationships and functional components are already known through STRING, hu.MAP, and extensive literature, including the NAMPT–SIRT7 relationship, the ANKRD28–ANKRD44 relationship, RNA polymerase and mitochondrial translation functions, antigen presentation, leukocyte adhesion, and cell-cycle regulation. At the same time, the particular cross-tissue co-abundance arrangement appears potentially novel because the module combines these components in a sparse network and includes many genes without recorded STRING or hu.MAP relationships. Absence from those resources is not evidence of novelty by itself. A defensible conclusion is that this is a potentially novel co-abundance association or cellular-state signature built from largely established genes and local interactions, requiring replication, preservation testing, and independent perturbation or protein-level validation before claiming a new mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared hematopoietic-like cellular state in which immune-cell composition or activation is coupled to proliferative and biosynthetic demands. In this model, ITGA4 and cytoskeletal regulators support leukocyte adhesion and migration, HLA-DRA and WDFY4 mark antigen-presentation and immune-processing capacity, NAMPT supplies NAD-related metabolic support, SIRT7 and POLR1A coordinate nucleolar or transcriptional stress responses, and mitochondrial or RNA-processing genes help sustain the energetic and proteostatic requirements of the state. KIAA0753 may act as a structural or centrosomal connector between this state and cell-cycle or organelle organization. This is a mechanistic interpretation, not an established causal pathway, because global GO/KEGG enrichment was absent and most module edges lack external interaction support.

### Important genes

#### KIAA0753

- **Related proteins** (co-abundance neighbors): IQGAP2 (0.93), IRF3 (0.91), NAMPT (0.90), VRK3 (0.88), TTC38 (0.88), FASTKD1 (0.87), ANKRD44 (0.85), ITGA4 (0.83), SLC44A1 (0.82), HLA-DRA (0.82), PPP2R2A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Centrosome; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: KIAA0753. This gene encodes a subunit of a protein complex that regulates ciliogenesis and cilia maintenance. The encoded protein has also been shown to regulate centriolar duplication. Mutations in this gene cause an orofaciodigital syndrome and a form of Joubert syndrome in human patients. [provided by RefSeq, May 2017].
- **Diseases (Open Targets)**: Joubert syndrome (0.685); short-rib thoracic dysplasia 21 without polydactyly (0.674); orofaciodigital syndrome type 6 (0.671); Jeune syndrome (0.592); Joubert syndrome 38 (0.578)
- **Europe PMC papers**: 190
- **Why important**: KIAA0753 is among the most connected genes in the module and links the module to IQGAP2, IRF3, NAMPT, FASTKD1, ANKRD44, and ITGA4. Its established association with centrosome regulation, centriole duplication, ciliogenesis, Joubert syndrome, and orofaciodigital syndrome gives it a plausible structural role connecting organelle organization with immune and metabolic features. Its HPA evidence includes bone-marrow detection and cell-type enhancement, while the absence of STRING or hu.MAP partners indicates that its central module position is not simply a reflection of a densely catalogued known complex.
- **Conclusion**: Established evidence supports a centrosomal and ciliogenesis-related function and a prominent position in this co-abundance network. It is a plausible module organizer, but a direct role in the proposed hematopoietic or immune state remains a hypothesis.

#### SIRT7

- **Related proteins** (co-abundance neighbors): TMEM68 (0.93), METTL8 (0.93), SLC44A1 (0.92), FASTKD1 (0.92), COX20 (0.86), ANKRD28 (0.86), GMEB2 (0.82); STRING partners: NAMPT (0.948), POLR1A (0.738)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sirtuin 7. This gene encodes a member of the sirtuin family of proteins, homologs to the yeast Sir2 protein. Members of the sirtuin family are characterized by a sirtuin core domain and grouped into four classes. The functions of human sirtuins have not yet been determined; however, yeast sirtuin proteins are known to regulate epigenetic gene silencing and suppress recombination of rDNA. Studies suggest that…
- **Diseases (Open Targets)**: neurodegenerative disease (0.313); neoplasm (0.117); hepatocellular carcinoma (0.113); breast cancer (0.112); cancer (0.112)
- **Europe PMC papers**: 5020
- **Why important**: SIRT7 is a central connector within the module and links to several genes, including NAMPT, POLR1A, METTL8, FASTKD1, COX20, ANKRD28, and GMEB2. STRING independently supports its relationships with NAMPT and POLR1A, while its annotations include transcriptional regulation, DNA repair, protein deacetylation, and osteoblast differentiation. It also has substantial literature support and is detected in bone marrow, making it a strong candidate for coordinating transcriptional, stress-response, and metabolic aspects of the module.
- **Conclusion**: Established evidence supports SIRT7 as a nuclear regulatory protein with known links to NAMPT and POLR1A. Its role as a coordinator of the complete module, especially in immune-cell state control, is a hypothesis requiring direct functional testing.

#### NAMPT

- **Related proteins** (co-abundance neighbors): KIAA0753 (0.90); STRING partners: SIRT7 (0.948)
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Nuclear speckles; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_11084.1
- **Function (MyGene.info)**: nicotinamide phosphoribosyltransferase. This gene encodes a protein that catalyzes the condensation of nicotinamide with 5-phosphoribosyl-1-pyrophosphate to yield nicotinamide mononucleotide, one step in the biosynthesis of nicotinamide adenine dinucleotide. The protein belongs to the nicotinic acid phosphoribosyltransferase (NAPRTase) family and is thought to be involved in many important biological processes, including metabolism, str…
- **Diseases (Open Targets)**: neurodegenerative disease (0.322); asthma (0.259); esophageal squamous cell carcinoma (0.174); Genu varum (0.172); Genu valgum (0.172)
- **Europe PMC papers**: 8350
- **Why important**: NAMPT is connected to KIAA0753 and SIRT7, with the latter relationship independently supported by STRING. It catalyzes a key step in NAD biosynthesis and is annotated for inflammatory response, cell-cell signaling, stress-related biology, and proliferation. HPA places it in lymphoid tissue and neutrophils, identifies it as immune-cell enriched, and records secretion to blood. Its extensive literature and disease associations make it a biologically informative bridge between metabolism, inflammation, and hematopoietic cell state.
- **Conclusion**: Established evidence supports NAMPT as an NAD-biosynthetic and inflammatory regulator with relevance to neutrophil-associated biology. Its contribution to this module may be metabolic support for activated or proliferating cells, but the co-abundance data do not establish causality.

#### HLA-DRA

- **Related proteins** (co-abundance neighbors): KIAA0753 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Group enriched; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: major histocompatibility complex, class II, DR alpha. HLA-DRA is one of the HLA class II alpha chain paralogues. This class II molecule is a heterodimer consisting of an alpha and a beta chain, both anchored in the membrane. This molecule is expressed on the surface of various antigen presenting cells such as B lymphocytes, dendritic cells, and monocytes/macrophages, and plays a central role in the immune system and response by presenting peptides de…
- **Diseases (Open Targets)**: Graham Little-Piccardi-Lassueur syndrome (0.263); lichen planopilaris (0.231); Sepsis (0.100); nonpapillary renal cell carcinoma (0.094); diffuse large B-cell lymphoma (0.082)
- **Europe PMC papers**: 9685
- **Why important**: HLA-DRA provides a strong lineage interpretation despite having only a local network connection to KIAA0753. It is tissue-enhanced in lung and lymphoid tissue, enriched across antigen-presenting blood-cell populations, and has an established role in MHC class two antigen processing and presentation. Its extensive literature and disease associations make it a key marker for an antigen-presenting or immune-composition component within the module.
- **Conclusion**: Established evidence supports HLA-DRA as an antigen-presentation marker in dendritic cells, monocytes, macrophages, and B cells. Its presence supports an immune-cell interpretation, but it does not demonstrate that antigen presentation is the causal function of the whole module.

#### ITGA4

- **Related proteins** (co-abundance neighbors): KIAA0753 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha 4. The gene encodes a member of the integrin alpha chain family of proteins. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha 4 subunit. This subunit associates with a beta 1 or beta 7 …
- **Diseases (Open Targets)**: Crohn disease (0.723); ulcerative colitis (0.605); inflammatory bowel disease (0.584); retinitis pigmentosa 26 (0.516); neurodegenerative disease (0.452)
- **Europe PMC papers**: 13014
- **Why important**: ITGA4 is associated with bone marrow and lymphoid tissue and is enhanced in B cells, dendritic cells, hematopoietic stem cells, innate lymphoid cells, and erythrocyte progenitors. Its established integrin function in leukocyte adhesion, cell-matrix interaction, and migration provides a plausible cellular-behavior link to the hematopoietic signal. It also has substantial literature and disease support, including inflammatory bowel disease associations, although it has only a local network edge to KIAA0753.
- **Conclusion**: Established evidence supports ITGA4 as an adhesion and leukocyte-migration molecule with broad hematopoietic relevance. Its participation is consistent with altered immune-cell trafficking or composition, while any direct interaction with the other module genes remains unestablished.

#### WDFY4

- **Related proteins** (co-abundance neighbors): DAAM2 (0.83), SLC44A1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WDFY family member 4. Predicted to be involved in autophagy. Predicted to act upstream of or within with a positive effect on CD8-positive, alpha-beta T cell activation. Predicted to act upstream of or within antigen processing and presentation and cellular response to virus. Predicted to be located in early endosome and endoplasmic reticulum. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: systemic lupus erythematosus (0.522); rheumatoid arthritis (0.415); primary biliary cholangitis (0.348); corneal neovascularization (0.253); frozen shoulder (0.220)
- **Europe PMC papers**: 579
- **Why important**: WDFY4 is tissue-enhanced in bone marrow and lymphoid tissue and shows broad enhancement across B cells, dendritic cells, macrophages, microglia, and several blood-cell groups. Its annotated roles in autophagy, antigen processing and presentation, and CD8-positive T-cell activation connect immune processing with intracellular trafficking. The WDFY4–SLC44A1 edge is one of the stronger module relationships, and WDFY4 has disease associations involving systemic lupus erythematosus and rheumatoid arthritis.
- **Conclusion**: Established evidence supports WDFY4 as an immune-processing and autophagy-related factor with strong hematopoietic relevance. It is a plausible contributor to the module’s immune component, but the proposed coupling to choline transport, mitochondrial function, or NAD metabolism remains a hypothesis.

## Module 1

**Tissue pair**: bone_marrow and cell line  
**Genes (47)**: SH3BP1, AFG2B, AGRN, APOC2, APOL2, ARIH1, GRAMD1C, BBX, GLB1, C1D, CD37, CD79B, CLASP2, COMMD4, CYBB, GMIP, HDAC5, INTS3, INTS4, ITGB2, ITIH4, JAK3, LPCAT4, LRP2, MAP7D2, MTA3, NCF4, NME1, NIPBL, MT-ND1, PIK3CD, POGLUT3, PTPN23, PTPN7, RBM10, RBM47, RIPOR1, RNASEL, ELAC1, RUNX3, SAMHD1, SLC25A24, SYNE1, TGFB1, TRAPPC5, TTF2, ZBTB1

### Function

The strongest functional interpretation is an innate immune and phagocyte-effector module centered on reactive oxygen biology. (GO:BP superoxide anion generation; q_global = 0.0102) is the only GO/KEGG term that passed global correction and links CYBB, ITGB2, NCF4, and TGFB1 to superoxide anion generation. This is biologically coherent with the established roles of CYBB as a core phagocyte NADPH-oxidase component, NCF4 as an oxidase regulatory factor, and ITGB2 as an immune-cell adhesion and signaling integrin. TGFB1 adds an immunoregulatory and cytokine-linked component rather than defining the entire module alone. The supplementary STRING terms (STRING HPO Pneumonia; within-query FDR = 0.0327) and (STRING HPO Increased inflammatory response; within-query FDR = 0.035) support an inflammatory and host-defense context, but they are not global enrichment evidence. Other module members indicate connected processes involving B-cell receptor signaling, leukocyte PI3K signaling, cytokine signaling, mitochondrial and oxidative-stress handling, vesicle trafficking, transcriptional control, RNA processing, and cytoskeletal organization. Thus, the module is best viewed as an immune-cell state module with a prominent phagocyte oxidative-burst axis, rather than as a narrowly specific single pathway.

**Cell composition.** The HPA profile strongly suggests that cellular composition contributes to the shared signal. Many genes are enhanced in lymphoid tissue, bone marrow, neutrophils, neutrophil progenitors, monocytes, macrophages, microglia, or T- and B-cell populations. The module therefore appears substantially blood-cell associated, especially with myeloid and neutrophil biology, although it also contains lymphoid and broadly expressed genes. Examples of immune or hematopoietic association include CYBB, NCF4, ITGB2, PIK3CD, JAK3, RUNX3, CD79B, and PTPN7. The module is not composed mostly of secreted proteins: the HPA summary identifies a minority as secreted, including APOC2, ITIH4, TGFB1, and AGRN. Those secreted or plasma-associated genes may reflect extracellular carryover or systemic inflammatory context rather than production by the same cell type. LRP2, ITIH4, APOC2, and several other genes have liver, kidney, brain, or epithelial associations, indicating that the module is heterogeneous and may combine cell-state variation with sample-composition effects. Protein detection in bone marrow is common across the module, whereas the cell-line comparison has no matching HPA tissue category, so the shared pattern should not automatically be interpreted as a purified bone-marrow cell program.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP superoxide anion generation | 0.0102 | CYBB, ITGB2, NCF4, TGFB1 |

### STRING and hu.MAP

STRING contains a coherent, experimentally or computationally supported interaction backbone involving CYBB–NCF4, CYBB–ITGB2, ITGB2–PIK3CD, PIK3CD–JAK3, and CD79B–PIK3CD. These links connect phagocyte oxidase activity with leukocyte adhesion, B-cell receptor signaling, and immune PI3K/JAK signaling. Additional STRING links connect RUNX3 with TGFB1, RNASEL with SAMHD1, and mitochondrial or transport-related proteins, but these relationships are more peripheral to the central oxidative-burst interpretation. The STRING enrichment terms (STRING HPO Pneumonia; within-query FDR = 0.0327) and (STRING HPO Increased inflammatory response; within-query FDR = 0.035) are consistent with inflammatory and pneumonia-related phenotypes, but remain supplementary evidence. hu.MAP provides two related Integrator-complex observations containing INTS3 and INTS4 (hu.MAP huMAP3_09230.1) and (hu.MAP huMAP3_10641.1), supporting a real nuclear RNA-processing submodule. It also places CYBB and ITGB2 together in a larger immune-cell complex (hu.MAP huMAP3_14295.1), supporting the phagocyte interpretation, while CLASP2 and HDAC5 occur in a broader regulatory complex (hu.MAP huMAP3_09810.1). Overall, the known interactions validate several local components, but they do not account for the complete co-abundance structure. The module is therefore a mixture of established complexes, known pathway links, and correlations that may arise from shared cell state or composition.

**STRING interactions (score >= 0.7)**: 12 of 1081 gene pairs: AGRN–LRP2 (0.914); CD79B–PIK3CD (0.836); CYBB–ITGB2 (0.816); CYBB–NCF4 (0.999); INTS3–INTS4 (0.999); INTS3–NIPBL (0.724); INTS4–NIPBL (0.741); ITGB2–PIK3CD (0.926); JAK3–PIK3CD (0.937); MT-ND1–SLC25A24 (0.877); RNASEL–SAMHD1 (0.72); RUNX3–TGFB1 (0.859)
**STRING functional enrichment (supplementary, within-query FDR)**: HPO Pneumonia (FDR = 0.0327, 8 genes); HPO Increased inflammatory response (FDR = 0.035, 14 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09230.1 (INTS3, INTS4; 2/9); huMAP3_10641.1 (INTS3, INTS4; 2/11); huMAP3_14295.1 (CYBB, ITGB2; 2/38); huMAP3_09810.1 (CLASP2, HDAC5; 2/56)

### Novelty

This module should not be claimed as a wholly new molecular pathway. Its central elements—phagocyte superoxide production, integrin-mediated leukocyte biology, leukocyte PI3K signaling, B-cell receptor signaling, and TGF-beta regulation—are established, and several relationships are already represented in STRING or hu.MAP. The sparse coverage of known interaction resources also means that many module edges are not currently documented there, but absence from STRING or hu.MAP does not demonstrate novelty. The potentially novel result is the reproducible co-abundance organization of these immune, inflammatory, secreted, mitochondrial, and regulatory genes across bone marrow and cell-line data. That interpretation remains provisional because blood-cell composition, extracellular proteins, and shared stress or culture states could generate part of the signal. Independent replication, cell-resolved measurements, and perturbation experiments would be needed to establish a new biological mechanism.

**Hypothesis.** Hypothesis: the module represents a shared immune-cell activation state in which myeloid or neutrophil-like cells coordinate integrin-dependent adhesion and migration with NADPH-oxidase-mediated superoxide production, while PI3K-delta, JAK3, TGFB1, and RUNX3 tune activation, differentiation, and inflammatory feedback. Mitochondrial transport and oxidative-stress genes may support the energetic and redox demands of activation, whereas vesicle, cytoskeletal, chromatin, and RNA-processing genes may reflect the cellular remodeling required for this state. The secreted APOC2, ITIH4, TGFB1, and AGRN signals could represent extracellular or plasma-associated modulation rather than direct membership in one intracellular complex. This hypothesis predicts that perturbing CYBB or NCF4 would alter the oxidative-burst component, perturbing ITGB2 would affect adhesion and phagocyte signaling, and perturbing PIK3CD or JAK3 would alter the broader immune-state signature. These are testable predictions, not established conclusions from co-abundance alone.

### Important genes

#### CYBB

- **Related proteins** (co-abundance neighbors): ELAC1 (0.84), MAP7D2 (0.82); STRING partners: ITGB2 (0.816), NCF4 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_14295.1
- **Function (MyGene.info)**: cytochrome b-245 beta chain. Cytochrome b (-245) is composed of cytochrome b alpha (CYBA) and beta (CYBB) chain. It has been proposed as a primary component of the microbicidal oxidase system of phagocytes. CYBB deficiency is one of five described biochemical defects associated with chronic granulomatous disease (CGD). In this disorder, there is decreased activity of phagocyte NADPH oxidase; neutrophils are able to phagocytiz…
- **Diseases (Open Targets)**: chronic granulomatous disease (0.864); neurodegenerative disease (0.352); hereditary disease (0.191); discoid lupus erythematosus (0.185); Kartagener Syndrome (0.118)
- **Europe PMC papers**: 6704
- **Why important**: CYBB is a core anchor of the globally significant oxidative-burst term (GO:BP superoxide anion generation; q_global = 0.0102). It has a direct high-confidence STRING relationship with NCF4 and a supported relationship with ITGB2, is enhanced in bone marrow and lymphoid tissue, and is associated with monocyte and macrophage populations. Its established role in phagocyte NADPH oxidase and its chronic granulomatous disease association make it the clearest mechanistic marker of the module.
- **Conclusion**: Established evidence supports CYBB as a central phagocyte reactive-oxygen component and a key explanation for (GO:BP superoxide anion generation; q_global = 0.0102). The hypothesis that CYBB coordinates the entire module is plausible but not proven, because co-abundance does not establish directionality or physical interaction for all module genes.

#### NCF4

- **Related proteins** (co-abundance neighbors): APOC2 (0.93), GRAMD1C (0.81); STRING partners: CYBB (0.999)
- **HPA**: Tissue enhanced; Group enriched; blood Group enriched; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neutrophil cytosolic factor 4. The protein encoded by this gene is a cytosolic regulatory component of the superoxide-producing phagocyte NADPH-oxidase, a multicomponent enzyme system important for host defense. This protein is preferentially expressed in cells of myeloid lineage. It interacts primarily with neutrophil cytosolic factor 2 (NCF2/p67-phox) to form a complex with neutrophil cytosolic factor 1 (NCF1/p47-phox), which…
- **Diseases (Open Targets)**: chronic granulomatous disease (0.742); inflammatory bowel disease (0.396); Crohn disease (0.375); atopic eczema (0.343); dermatitis (0.306)
- **Europe PMC papers**: 3314
- **Why important**: NCF4 is also part of (GO:BP superoxide anion generation; q_global = 0.0102) and is linked to CYBB by the strongest STRING relationship in the fact sheet. It is preferentially associated with myeloid cells, neutrophils, and neutrophil progenitors, and its established function is as a regulatory component of the phagocyte superoxide-producing oxidase. Its chronic granulomatous disease association gives the gene strong disease and mechanistic relevance despite its limited number of module connections.
- **Conclusion**: Established evidence identifies NCF4 as a direct oxidative-burst regulator and a strong indicator of myeloid or neutrophil composition. It is reasonable to hypothesize that NCF4 explains part of the conserved module through coordinated oxidase activity, but the broader module likely includes additional composition and signaling effects.

#### ITGB2

- **Related proteins** (co-abundance neighbors): APOC2 (0.85); STRING partners: CYBB (0.816), PIK3CD (0.926)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_14295.1
- **Function (MyGene.info)**: integrin subunit beta 2. This gene encodes an integrin beta chain, which combines with multiple different alpha chains to form different integrin heterodimers. Integrins are integral cell-surface proteins that participate in cell adhesion as well as cell-surface mediated signalling. The encoded protein plays an important role in immune response and defects in this gene cause leukocyte adhesion deficiency. Alternative spli…
- **Diseases (Open Targets)**: leukocyte adhesion deficiency 1 (0.827); psoriasis vulgaris (0.585); leukocyte adhesion deficiency (0.559); dry eye syndrome (0.556); psoriasis (0.490)
- **Europe PMC papers**: 6754
- **Why important**: ITGB2 connects the oxidative-burst axis to leukocyte adhesion and signaling. It participates in (GO:BP superoxide anion generation; q_global = 0.0102), has STRING links to CYBB and PIK3CD, and is enhanced in bone marrow and lymphoid tissue and across myeloid cell types. Its established role in leukocyte migration, phagocytosis, and leukocyte adhesion deficiency makes it an important functional bridge rather than merely a cell-type marker.
- **Conclusion**: Established evidence supports ITGB2 as an immune-cell adhesion and phagocytosis component that links oxidase activity with leukocyte signaling. The proposed role of ITGB2 as a coordinating bridge for the whole module remains a hypothesis because the module graph is co-abundance based.

#### PIK3CD

- **Related proteins** (co-abundance neighbors): C1D (0.81), HDAC5 (0.81); STRING partners: CD79B (0.836), ITGB2 (0.926), JAK3 (0.937)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit delta. Phosphoinositide 3-kinases (PI3Ks) phosphorylate inositol lipids and are involved in the immune response. The protein encoded by this gene is a class I PI3K found primarily in leukocytes. Like other class I PI3Ks (p110-alpha p110-beta, and p110-gamma), the encoded protein binds p85 adapter proteins and GTP-bound RAS. However, unlike the other class I PI3Ks, this protein phosphorylates itself, not …
- **Diseases (Open Targets)**: activated PI3K-delta syndrome (0.759); immunodeficiency 14b, autosomal recessive (0.689); combined immunodeficiency with faciooculoskeletal anomalies (0.615); B-cell chronic lymphocytic leukemia (0.608); follicular lymphoma (0.586)
- **Europe PMC papers**: 4991
- **Why important**: PIK3CD provides a signaling connection between immune receptors and downstream leukocyte responses. It is linked in STRING to ITGB2, JAK3, and CD79B and is enhanced in bone marrow and lymphoid tissue, including B-cell and hematopoietic populations. Its established leukocyte-restricted PI3K function and associations with activated PI3K-delta syndrome, immunodeficiency, and B-cell malignancy make it important for interpreting the module beyond oxidative metabolism.
- **Conclusion**: Established evidence supports PIK3CD as a major immune signaling component that could connect B-cell, myeloid, and cytokine-related signals. Its role as a driver of the conserved co-abundance state is a hypothesis requiring perturbation or phosphosignaling evidence.

#### JAK3

- **Related proteins** (co-abundance neighbors): RBM47 (0.91), AGRN (0.87), RIPOR1 (0.85), LPCAT4 (0.82), SYNE1 (0.80); STRING partners: PIK3CD (0.937)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Janus kinase 3. The protein encoded by this gene is a member of the Janus kinase (JAK) family of tyrosine kinases involved in cytokine receptor-mediated intracellular signal transduction. It is predominantly expressed in immune cells and transduces a signal in response to its activation via tyrosine phosphorylation by interleukin receptors. Mutations in this gene are associated with autosomal SCID (severe combine…
- **Diseases (Open Targets)**: T-B+ severe combined immunodeficiency due to JAK3 deficiency (0.844); ulcerative colitis (0.650); rheumatoid arthritis (0.618); myelofibrosis (0.614); atopic eczema (0.590)
- **Europe PMC papers**: 15148
- **Why important**: JAK3 is a hematopoietic cytokine-receptor kinase with extensive biological and disease literature. It is tissue enhanced in lymphoid tissue, cell-type enhanced in B cells, hematopoietic stem cells, neutrophils, and neutrophil progenitors, and has a STRING link to PIK3CD. Its association with severe combined immunodeficiency and inflammatory diseases makes it a useful candidate for connecting cytokine signaling to the observed immune-cell state.
- **Conclusion**: Established evidence supports JAK3 as a cytokine signaling regulator in hematopoietic cells. The idea that JAK3 amplifies or maintains the module's shared activation state is a mechanistic hypothesis, not a direct inference from the network alone.

#### TGFB1

- **Related proteins** (co-abundance neighbors): APOC2 (0.87); STRING partners: RUNX3 (0.859)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transforming growth factor beta 1. This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate a latency-associated peptide (LAP) and a mature peptide, and …
- **Diseases (Open Targets)**: Camurati-Engelmann disease (0.797); inflammatory bowel disease, immunodeficiency, and encephalopathy (0.693); myelodysplastic syndrome (0.591); coronary artery disorder (0.585); anemia (0.577)
- **Europe PMC papers**: 29180
- **Why important**: TGFB1 is one of the genes in the globally significant oxidative-anion-generation term (GO:BP superoxide anion generation; q_global = 0.0102), is linked to RUNX3 in STRING, and is also represented in the supplementary inflammatory and pneumonia terms (STRING HPO Pneumonia; within-query FDR = 0.0327) and (STRING HPO Increased inflammatory response; within-query FDR = 0.035). It is a secreted immune-regulatory ligand with extensive literature and disease relevance, including inflammatory, hematopoietic, skeletal, and vascular contexts. Its presence may connect extracellular regulation with the intracellular immune program.
- **Conclusion**: Established evidence supports TGFB1 as a secreted regulator of immune and developmental signaling and as part of the globally significant term (GO:BP superoxide anion generation; q_global = 0.0102). Whether TGFB1 is produced by the same cells driving the oxidative-burst signal, or instead reflects extracellular carryover or sample composition, remains unresolved.

## Module 2

**Tissue pair**: bone_marrow and cell line  
**Genes (43)**: ALDH16A1, ADAM8, ALG3, ARFIP2, CARD8, CD22, CNPY3, CEP135, HLA-DMB, DPH1, ERBIN, FAM98B, FAHD1, FASTKD2, FSAF1, FUT8, GRAP, HBA1, CD74, HIF1AN, HVCN1, INTS1, ITGB1BP1, LIN7A, ALOX5, LSR, MAD2L1, MON2, MSH6, NPRL3, NSFL1C, NSUN4, PDCD10, RIC1, RMP24, S100A8, SCO2, SMARCAL1, SRPK1, GTF2A1, TRIM22, UBIAD1, VPS72

### Function

The strongest supported function is leukocyte migration during inflammatory response, based on the globally corrected GO term (GO:BP leukocyte migration involved in inflammatory response; q_global = 0.0339), which includes ADAM8, ALOX5, and S100A8. The module also contains coherent immune-related biology involving antigen presentation through CD74 and HLA-DMB, B-cell regulation through CD22, innate immune and interferon-related signaling through several genes, and phagocyte-associated redox biology through HVCN1. These additional interpretations are supported by the gene annotations and HPA evidence rather than by another globally corrected GO or KEGG term. The network is highly uneven, with S100A8 acting as the central hub and many genes connected primarily to that hub; this favors a dominant inflammatory or cell-state signal rather than a single well-defined protein complex.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: only a small minority of genes are annotated as secreted, including S100A8 and CD74. The module does show a substantial hematopoietic and immune-cell signature. HPA highlights lymphoid tissue and bone marrow, with enrichment among neutrophils, B cells, monocytes, basophils, eosinophils, and related blood-cell populations. Many genes are broadly expressed or have low tissue specificity, so the shared signal may partly reflect common blood-derived or immune cell types in the bone-marrow and cell-line datasets rather than a pathway operating uniformly in every cell. Bone-marrow protein detection is common among the genes with available evidence, whereas the cell-line tissue comparison has no matching HPA tissue-level protein observations. HBA1 further suggests a possible erythroid or blood-related contribution, although it is isolated in the network.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP leukocyte migration involved in inflammatory response | 0.0339 | ADAM8, ALOX5, S100A8 |

### STRING and hu.MAP

STRING provides only two high-confidence relationships within the module: CD74 with HLA-DMB, and ITGB1BP1 with PDCD10. The CD74-HLA-DMB pair is biologically coherent with MHC class two antigen processing, while the ITGB1BP1-PDCD10 pair links integrin-associated adhesion biology with a vascular and signaling regulator. No STRING functional-enrichment term is reported, and no hu.MAP complex contains multiple module members. Thus, the module is not supported as a known multi-protein complex. Its co-abundance structure may capture shared cell state, transcriptional regulation, or indirect pathway coordination rather than direct physical interaction. The strong co-abundance links surrounding S100A8 should therefore not be interpreted as established molecular binding relationships.

**STRING interactions (score >= 0.7)**: 2 of 903 gene pairs: CD74–HLA-DMB (0.982); ITGB1BP1–PDCD10 (0.92)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a reproducible cross-context co-abundance signature, but the fact sheet does not establish it as a new biological pathway or protein complex. The globally supported inflammatory-migration signal is already biologically established for S100A8, ADAM8, and ALOX5, and the CD74-HLA-DMB relationship is already known from STRING. Conversely, the broader combination of inflammatory, antigen-presentation, B-cell, mitochondrial, RNA-processing, and housekeeping-related genes is not explained by a documented hu.MAP complex or by a STRING enrichment result. This makes the module potentially novel as a co-abundance pattern, especially if its preservation across bone marrow and cell line is independently replicated, but absence from interaction databases alone is insufficient to claim discovery. Cell-composition effects and the central-hub topology are important alternative explanations.

**Hypothesis.** Hypothesis: the module reflects a shared hematopoietic inflammatory state in which myeloid-cell programs centered on S100A8, ADAM8, and ALOX5 are co-abundant with antigen-processing and lymphoid programs represented by CD74, HLA-DMB, and CD22. HVCN1 may support phagocyte or B-cell redox and pH regulation within this state. In the cell-line data, the same signal could arise from immune-like differentiation, residual hematopoietic character, or mixed-cell contamination rather than from a complete inflammatory circuit in every cell. This hypothesis predicts that module abundance should track immune-cell proportions and inflammatory activation, and that single-cell or purified-cell validation should separate true within-cell coordination from composition-driven co-abundance.

### Important genes

#### S100A8

- **Related proteins** (co-abundance neighbors): ERBIN (0.95), FASTKD2 (0.90), NSUN4 (0.90), FSAF1 (0.90), FAM98B (0.89), PDCD10 (0.89), SCO2 (0.88), ALDH16A1 (0.88), HIF1AN (0.88), GTF2A1 (0.87), FAHD1 (0.85), TRIM22 (0.85), VPS72 (0.84), ALOX5 (0.82), MON2 (0.82), INTS1 (0.82), FUT8 (0.81), NSFL1C (0.81), SRPK1 (0.81), ARFIP2 (0.80), CEP135 (0.80), SMARCAL1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Group enriched; location Intermediate filaments; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: S100 calcium binding protein A8. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: inborn error of immunity (0.371); Sepsis (0.122); neoplasm (0.119); breast carcinoma (0.119); gastric cancer (0.119)
- **Europe PMC papers**: 18104
- **Why important**: S100A8 is the principal network hub, with many strong module connections, and it is one of the genes in the globally corrected inflammatory-migration term (GO:BP leukocyte migration involved in inflammatory response; q_global = 0.0339). HPA links it to bone marrow, monocytes, and neutrophils, and identifies it as secreted to blood. Its annotation supports calcium-binding, cytokine-like, inflammatory, and leukocyte-related functions, while its disease associations include sepsis and inborn errors of immunity. Its extensive literature makes it the best-established biological anchor for the module.
- **Conclusion**: Established evidence supports S100A8 as an inflammatory, myeloid-associated driver or marker and as the structural center of this co-abundance module. It is plausible that S100A8 captures the dominant cell-state signal, but the network does not prove that it directly regulates the other module genes.

#### ADAM8

- **Related proteins** (co-abundance neighbors): MAD2L1 (0.90), HLA-DMB (0.89), HVCN1 (0.88), HBA1; HBA2 (0.86), NSUN4 (0.85), CNPY3 (0.82), DPH1 (0.81), LSR (0.81), MSH6 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ADAM metallopeptidase domain 8. This gene encodes a member of the ADAM (a disintegrin and metalloprotease domain) family. Members of this family are membrane-anchored proteins structurally related to snake venom disintegrins, and have been implicated in a variety of biological processes involving cell-cell and cell-matrix interactions, including fertilization, muscle development, and neurogenesis. The protein encoded by this gen…
- **Diseases (Open Targets)**: neoplasm (0.112); pancreatic ductal adenocarcinoma (0.108); osteoarthritis (0.104); breast cancer (0.102); breast carcinoma (0.101)
- **Europe PMC papers**: 1768
- **Why important**: ADAM8 has a comparatively prominent position near the module core and is also part of (GO:BP leukocyte migration involved in inflammatory response; q_global = 0.0339). HPA associates it with bone marrow, lymphoid tissue, monocytes, mast cells, and granulocyte populations. Its annotated roles in cell adhesion, extracellular interactions, proteolysis, leukocyte migration, and acute inflammation provide a mechanistic bridge between inflammatory activation and cellular movement. It also has disease links involving inflammatory and neoplastic conditions and a substantial literature base.
- **Conclusion**: Established evidence supports ADAM8 as a leukocyte-associated adhesion and inflammatory protease relevant to the module's migration interpretation. A possible role as an effector connecting S100A8-associated inflammatory state to cell movement is a hypothesis, not demonstrated by this co-abundance network.

#### ALOX5

- **Related proteins** (co-abundance neighbors): S100A8 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: arachidonate 5-lipoxygenase. This gene encodes a member of the lipoxygenase gene family and plays a dual role in the synthesis of leukotrienes from arachidonic acid. The encoded protein, which is expressed specifically in bone marrow-derived cells, catalyzes the conversion of arachidonic acid to 5(S)-hydroperoxy-6-trans-8,11,14-cis-eicosatetraenoic acid, and further to the allylic epoxide 5(S)-trans-7,9-trans-11,14-cis-eicosa…
- **Diseases (Open Targets)**: ulcerative colitis (0.609); rheumatoid arthritis (0.595); asthma (0.576); juvenile idiopathic arthritis (0.536); proctitis (0.503)
- **Europe PMC papers**: 8205
- **Why important**: ALOX5 is one of the three genes in (GO:BP leukocyte migration involved in inflammatory response; q_global = 0.0339) and encodes the key enzyme initiating leukotriene production from arachidonic acid. It is described as being expressed in bone-marrow-derived cells and is associated with leukocyte chemotaxis and migration. Its strong literature base and associations with asthma, rheumatoid arthritis, and inflammatory bowel disease make it an important functional rather than merely correlative member of the module.
- **Conclusion**: Established evidence supports ALOX5 as a plausible biochemical effector of inflammatory leukocyte recruitment. Its co-abundance with S100A8 and ADAM8 is consistent with coordinated myeloid inflammation, but the module alone cannot show that leukotriene production is increased.

#### CD74

- **Related proteins** (co-abundance neighbors): NPRL3 (0.81); STRING partners: HLA-DMB (0.982)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Golgi apparatus; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD74 molecule. The protein encoded by this gene associates with class II major histocompatibility complex (MHC) and is an important chaperone that regulates antigen presentation for immune response. It also serves as cell surface receptor for the cytokine macrophage migration inhibitory factor (MIF) which, when bound to the encoded protein, initiates survival pathways and cell proliferation. This protein also in…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.626); neoplasm (0.400); cancer (0.394); lung adenocarcinoma (0.379); squamous cell lung carcinoma (0.376)
- **Europe PMC papers**: 17433
- **Why important**: CD74 provides an antigen-presentation component that complements the myeloid inflammatory signal. HPA places it in lymphoid tissue and multiple antigen-presenting cell types, including B cells, monocytes, and dendritic cells. Its annotated function includes MHC class two chaperoning, antigen presentation, cytokine signaling, and interaction with MIF. It forms the module's clearest known STRING relationship with HLA-DMB, and it has a large literature base.
- **Conclusion**: Established evidence supports CD74 as a marker and mediator of antigen-presenting immune-cell biology. Its presence suggests that the module is broader than a pure neutrophil program, while its connection to the inflammatory hub is a co-abundance association whose cellular basis remains unresolved.

#### HVCN1

- **Related proteins** (co-abundance neighbors): ITGB1BP1 (0.94), ALG3 (0.94), ADAM8 (0.88), RMP24 (0.86), LIN7A (0.85); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydrogen voltage gated channel 1. This gene encodes a voltage-gated protein channel protein expressed more highly in certain cells of the immune system. Phagocytic cells produce superoxide anions which require this channel protein, and in B cells this same process facilitates antibody production. This same channel protein, however, can also regulate functions in other cells including spermatozoa. Multiple transcript variants encod…
- **Diseases (Open Targets)**: Joubert syndrome (0.551); Meckel syndrome (0.548); Joubert syndrome and related disorders (0.489); neurodegenerative disease (0.349); gastroesophageal reflux disease (0.218)
- **Europe PMC papers**: 729
- **Why important**: HVCN1 occupies an intermediate network position and connects to genes including ITGB1BP1 and ADAM8. It is an immune-enriched voltage-gated proton channel; its annotation links it to phagocyte superoxide production, B-cell antibody production, ion transport, pH regulation, and redox homeostasis. HPA detects it in bone marrow and highlights B-cell-associated expression, while its disease associations and literature support a meaningful immune-cell function.
- **Conclusion**: Established evidence supports HVCN1 as a regulator of immune-cell pH and oxidative physiology. Its module position is compatible with a role coordinating cellular activation or redox demands, but the proposed connection to the S100A8-centered inflammatory state remains a hypothesis.

#### CD22

- **Related proteins** (co-abundance neighbors): UBIAD1 (0.85), CARD8 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD22 molecule. Predicted to enable CD4 receptor binding activity; protein phosphatase binding activity; and sialic acid binding activity. Involved in B cell activation; negative regulation of B cell receptor signaling pathway; and regulation of endocytosis. Located in early endosome and recycling endosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: acute lymphoblastic leukemia (0.599); hairy cell leukemia (0.532); neoplasm (0.490); B-cell acute lymphoblastic leukemia (0.453); systemic lupus erythematosus (0.408)
- **Europe PMC papers**: 11372
- **Why important**: CD22 is a B-cell-associated surface receptor with annotations for negative regulation of B-cell receptor signaling, immunoglobulin production, immune signaling, adhesion, and endocytosis. HPA links it to lymphoid tissue and memory and naive B-cell populations. Although it is not a central hub, its connection to UBIAD1 and CARD8 adds a lymphoid regulatory branch to the module and helps explain why the module may represent mixed hematopoietic composition rather than a purely granulocytic program. It also has a large literature base and disease associations in B-cell leukemia and autoimmunity.
- **Conclusion**: Established evidence supports CD22 as a B-cell identity and signaling-regulatory component. Its presence strengthens the cell-composition interpretation and suggests lymphoid participation, but it does not establish direct mechanistic cooperation with the S100A8-centered inflammatory genes.

## Module 3

**Tissue pair**: bone_marrow and cell line  
**Genes (38)**: ABCB7, CAPN7, NEDD9, CDK7, COMMD2, MT-CO2, CPTP, CRYL1, DCAF13, DGKE, EAF1, EWSR1, FAT3, ITGB7, JMJD6, LARP1B, MAPKAPK5, MGAT2, MTMR3, MTX1, MYO9B, NFRKB, NIP7, MT-ND2, PEX10, PPP1R21, PSD3, PEX11B, RAN, RDH11, RPL9, RPAP1, MRRF, SLC12A9, STK17A, STMN2, TAP1, UBN1

### Function

No GO or KEGG term passed global correction, so there is no statistically supported pathway label for this module from primary enrichment evidence. The module is biologically heterogeneous. Its genes point to several compatible processes: mitochondrial respiration and translation, peroxisome organization and protein import, RNA and ribosome biogenesis, transcriptional regulation, membrane trafficking, cell adhesion, cytoskeletal regulation, and leukocyte adhesion or migration. The network structure is dominated by FAT3 as a highly connected co-abundance hub, with smaller subnetworks involving peroxisomal genes, mitochondrial genes, ribosome-associated genes, and immune-adhesion genes. Thus, the safest interpretation is a shared cellular-state or cellular-composition module rather than a single established biochemical pathway. The lack of globally significant GO or KEGG enrichment does not invalidate the module, but it limits functional specificity.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module: only a single gene has secretome annotation, and the genes are largely intracellular, membrane-associated, or organelle-associated. The HPA profile is dominated by low tissue specificity, with additional tissue-enhanced signals in bone marrow, brain, heart muscle, lymphoid tissue, and kidney. Many genes are cell-type enhanced, especially in neutrophils and reproductive cell types, while most genes have low immune-cell specificity. Therefore, the module is not convincingly a blood-cell-specific program, although bone-marrow-associated and neutrophil-associated signals could contribute to its appearance in bone marrow samples. Protein detection in bone marrow is present for many genes, whereas there is no matching HPA tissue category for the cell-line comparison. The mixed tissue and cell-type profile argues for caution about interpreting the module as a dedicated bone-marrow mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING evidence is limited but biologically coherent in selected regions. Known high-confidence relationships include DCAF13 with NIP7, MRRF with RPL9, MT-CO2 with MT-ND2, NIP7 with RPL9, and PEX10 with PEX11B. These links support local ribosome or RNA-processing, mitochondrial, and peroxisomal subnetworks, but they do not establish a single connected molecular complex for the whole module. The hu.MAP evidence independently supports a PEX10–PEX11B relationship through both C1 and C2, with the two module genes representing only part of larger complexes. FAT3 is the dominant network hub despite having no listed STRING partner and no hu.MAP assignment, so its centrality is a co-abundance property rather than a confirmed physical-interaction hub. Overall, known interactions explain selected edges but only a small portion of the module architecture; the remaining associations may reflect co-expression, indirect regulation, shared cell states, or technical and compositional effects.

**STRING interactions (score >= 0.7)**: 5 of 703 gene pairs: DCAF13–NIP7 (0.838); MRRF–RPL9 (0.926); MT-CO2–MT-ND2 (0.999); NIP7–RPL9 (0.877); PEX10–PEX11B (0.879)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00452.1 (PEX10, PEX11B; 2/7); huMAP3_08983.1 (PEX10, PEX11B; 2/7)

### Novelty

The complete module may represent a new co-abundance pattern in the bone_marrow and cell_line comparison, but the evidence does not justify calling it a newly discovered molecular pathway or complex. Several component relationships and functions are already established, particularly the PEX10–PEX11B peroxisomal association, the MT-CO2–MT-ND2 mitochondrial relationship, and the NIP7–RPL9 and MRRF–RPL9 ribosome-related relationships. Conversely, the central FAT3-centered arrangement and the joining of peroxisomal, mitochondrial, nuclear, adhesion, and immune-associated genes are not explained by the listed STRING or hu.MAP evidence. That unusual arrangement supports possible novelty at the level of co-abundance organization, but absence from interaction databases alone cannot prove novelty. Replication in independent cohorts, preservation across normalization strategies, and perturbation or cell-resolved validation would be needed.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state signal in which organelle maintenance and energy metabolism are co-regulated with membrane trafficking, adhesion, and transcriptional or RNA-processing activity. In bone marrow, this could be influenced by immature or neutrophil-associated cellular states; in the cell line, it could reflect a related proliferative or metabolic state rather than the same cell type. FAT3 may act as a statistical bridge connecting otherwise distinct expression programs, while the PEX10–PEX11B and mitochondrial pairs represent more concrete organelle-linked components. This hypothesis predicts that the module will weaken after careful adjustment for cell composition and broad expression level, but that selected subnetworks may remain associated with peroxisome, mitochondrial, or adhesion-related phenotypes.

### Important genes

#### FAT3

- **Related proteins** (co-abundance neighbors): PEX11B (0.96), CDK7 (0.92), MTX1 (0.91), EWSR1 (0.91), MT-CO2 (0.91), CRYL1 (0.90), MAPKAPK5 (0.90), MYO9B (0.87), RAN (0.86), RDH11 (0.86), COMMD2 (0.85), MRRF (0.84), JMJD6 (0.83), NIP7 (0.83), EAF1 (0.82), DCAF13 (0.82), ABCB7 (0.82), TAP1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FAT atypical cadherin 3. Predicted to enable calcium ion binding activity. Predicted to be involved in cell-cell adhesion. Predicted to act upstream of or within several processes, including negative regulation of dendrite development; neuron migration; and retina layer formation. Predicted to be located in dendrite and plasma membrane. Predicted to be integral component of membrane. [provided by Alliance of Genome Resour…
- **Diseases (Open Targets)**: retinal detachment (0.450); mathematical ability (0.438); gestational diabetes (0.428); atrial fibrillation (0.421); retinal disorder (0.405)
- **Europe PMC papers**: 1546
- **Why important**: FAT3 is the principal network hub by weighted degree and connects genes spanning mitochondrial, nuclear, metabolic, signaling, and membrane-associated functions. HPA places it in cell junctions and associates it with blood vessels and brain-related cell types. Its annotated roles in calcium binding and homophilic cell adhesion, together with disease associations involving retinal and cardiovascular phenotypes, make it a plausible organizer of the module's membrane and adhesion-facing component. It also has substantial literature support, although the module contains no listed STRING or hu.MAP relationship for FAT3.
- **Conclusion**: Established evidence supports FAT3 as the strongest co-abundance hub and as an adhesion-associated membrane protein. It does not establish FAT3 as a physical interaction partner for the other module genes. The hypothesis that FAT3 connects the other functional sectors is therefore a network-based interpretation, not a demonstrated molecular mechanism.

#### PEX10

- **Related proteins** (co-abundance neighbors): NEDD9 (1.00), CPTP (0.96), STMN2 (0.88), MT-CO2 (0.83); STRING partners: PEX11B (0.879)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_00452.1, huMAP3_08983.1
- **Function (MyGene.info)**: peroxisomal biogenesis factor 10. This gene encodes a protein involved in import of peroxisomal matrix proteins. This protein localizes to the peroxisomal membrane. Mutations in this gene result in phenotypes within the Zellweger spectrum of peroxisomal biogenesis disorders, ranging from neonatal adrenoleukodystrophy to Zellweger syndrome. Alternative splicing results in two transcript variants encoding different isoforms. [provid…
- **Diseases (Open Targets)**: Zellweger spectrum disorders (0.832); peroxisome biogenesis disorder 6B (0.808); peroxisome biogenesis disorder (0.791); peroxisome biogenesis disorder 6A (Zellweger) (0.783); peroxisome biogenesis disorder, complementation group 7 (0.688)
- **Europe PMC papers**: 952
- **Why important**: PEX10 is directly connected to PEX11B in STRING and occurs with PEX11B in both C1 and C2 hu.MAP complexes. Its established function in peroxisomal matrix-protein import and peroxisome organization, together with strong disease associations with Zellweger-spectrum and related peroxisomal disorders, gives this gene unusually clear mechanistic relevance within an otherwise heterogeneous module. It also connects in the co-abundance graph to NEDD9, CPTP, STMN2, and MT-CO2, linking the peroxisomal signal to adhesion, lipid, neuronal, and mitochondrial-associated genes.
- **Conclusion**: Established evidence supports PEX10 as a genuine peroxisomal component with known interaction support from PEX11B. It is reasonable to regard the PEX10–PEX11B portion as a real organelle-related submodule. It is not established that PEX10 mechanistically coordinates the entire FAT3-centered module.

#### PEX11B

- **Related proteins** (co-abundance neighbors): FAT3 (0.96); STRING partners: PEX10 (0.879)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_00452.1, huMAP3_08983.1
- **Function (MyGene.info)**: peroxisomal biogenesis factor 11 beta. The protein encoded by this gene facilitates peroxisomal proliferation and interacts with PEX19. The encoded protein is found in the peroxisomal membrane. Several transcript variants, some protein-coding and some not protein-coding, have been found for this gene. [provided by RefSeq, Dec 2012].
- **Diseases (Open Targets)**: peroxisome biogenesis disorder 14B (0.769); Zellweger spectrum disorders (0.736); peroxisome biogenesis disorder (0.492); neurodegenerative disease (0.488); peroxisomal disease (0.464)
- **Europe PMC papers**: 397
- **Why important**: PEX11B is the partner of PEX10 in STRING and is present with PEX10 in both listed hu.MAP complexes. Its annotated role in peroxisome proliferation, fission, and regulation of peroxisome size provides a complementary function to PEX10-mediated matrix-protein import. Its peroxisomal disease associations further support biological importance, even though it has limited network degree and comparatively less literature than several other selected genes.
- **Conclusion**: Established evidence supports PEX11B as a peroxisomal membrane and division factor participating in a known PEX10-associated complex context. Its inclusion strengthens the interpretation of a peroxisomal subnetwork. Any claim that this pair drives the shared tissue module remains a hypothesis.

#### MT-CO2

- **Related proteins** (co-abundance neighbors): FAT3 (0.91), PEX10 (0.83); STRING partners: MT-ND2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome c oxidase subunit II. Contributes to cytochrome-c oxidase activity. Predicted to be involved in mitochondrial electron transport, cytochrome c to oxygen and positive regulation of vasoconstriction. Located in mitochondrial inner membrane. Part of respiratory chain complex IV. Biomarker of Huntington's disease and stomach cancer. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: mitochondrial complex IV deficiency, nuclear-type (0.726); mitochondrial disease (0.707); MELAS syndrome (0.662); leigh syndrome due to mitochondrial complex iv deficiency (0.536); MERRF syndrome (0.516)
- **Europe PMC papers**: 47751
- **Why important**: MT-CO2 is part of respiratory-chain complex IV and is directly linked to MT-ND2 by a very high-confidence STRING relationship. It is tissue-enhanced in heart muscle and is associated with mitochondrial disease, complex IV deficiency, and other mitochondrial phenotypes. It has extensive literature coverage and connects in the module to FAT3 and PEX10, making it important for evaluating whether the module contains a mitochondrial energy component alongside its peroxisomal component.
- **Conclusion**: Established evidence supports MT-CO2 as a mitochondrial respiratory-chain gene and supports its local relationship with MT-ND2. The module may therefore contain a real mitochondrial subcomponent. The connection from this mitochondrial pair to FAT3 and PEX10 is based on co-abundance and selected network edges, not proof of direct biochemical coordination.

#### ITGB7

- **Related proteins** (co-abundance neighbors): PSD3 (0.84), NFRKB (0.82), MTMR3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 7. This gene encodes a protein that is a member of the integrin superfamily. Members of this family are adhesion receptors that function in signaling from the extracellular matrix to the cell. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain. The encoded protein forms dimers with an alpha4 chain or an alphaE chain and plays a role in leukocyte adhesio…
- **Diseases (Open Targets)**: ulcerative colitis (0.600); Crohn disease (0.599); inflammation (0.370); mathematical ability (0.309); inflammatory bowel disease (0.274)
- **Europe PMC papers**: 1770
- **Why important**: ITGB7 is a membrane adhesion receptor with enhanced expression in lymphoid tissue and several lymphoid cell types. Its established functions include leukocyte adhesion, integrin-mediated signaling, and migration, and it is associated with inflammatory bowel disease and ulcerative or Crohn disease. Within the module it links to PSD3, NFRKB, and MTMR3, thereby connecting adhesion and immune-cell biology with vesicle, chromatin, and phosphoinositide-related functions. Its literature base is substantial compared with many of the less characterized module genes.
- **Conclusion**: Established evidence supports ITGB7 as an immune and adhesion-related component, but the HPA profile does not make the whole module a blood-cell program. ITGB7 may mark a cell-type or trafficking contribution to the shared signal. A direct mechanistic link between ITGB7 and the peroxisomal or mitochondrial subnetworks is not established.

## Module 4

**Tissue pair**: bone_marrow and cell line  
**Genes (46)**: ABL1, ALG6, APOC3, ACTR5, ATF1, ATG12, CTSO, CD79A, CHCHD5, MT-CYB, DMAC2, DPYSL5, HLA-DRB3, ELMOD2, GUF1, MACROH2A2, HMMR, PSMC3IP, EIF1AY, IFI44L, ITGAL, CSNK1E, KLHL7, KMO, KSR1, MIS18BP1, NFYA, NOTCH1, NXT1, OSGEPL1, OTUD7B, PDE7A, RBP4, SLAIN1, SPP2, STK26, NARS2, TUBB8, TCF3, TMEM160, TRAPPC12, UNC119B, UCKL1, WWTR1, XPO6, YIPF5

### Function

No GO or KEGG term passed global correction, and STRING functional enrichment was absent; therefore, the module does not support a single statistically established pathway label. Its gene-level biology is heterogeneous but points toward a bone-marrow and immune-cell context, including leukocyte adhesion and cell-cell interaction through ITGAL, B-cell receptor biology through CD79A, antigen presentation through HLA-DRB3, interferon and antiviral response through IFI44L and ELMOD2, and lymphocyte development through TCF3. Other components represent transcriptional regulation, mitochondrial activity, protein turnover, vesicle trafficking, glycosylation, lipid transport, and secreted plasma proteins. The strongest biological interpretation is therefore a mixed cell-state or cell-composition module rather than a coherent pathway.

**Cell composition.** The module is not predominantly a single lineage or molecular class. HPA indicates many genes have low tissue or immune-cell specificity, while others are enhanced or enriched in bone marrow, lymphoid tissue, B cells, monocytes, neutrophils, dendritic cells, or plasma cells. It also contains liver-enriched, hepatocyte-associated proteins, including RBP4 and APOC3, and secreted-to-blood proteins including RBP4, APOC3, and SPP2. The presence of such plasma proteins, together with the absence of matching HPA tissue evidence for several genes in bone marrow, suggests that blood or extracellular carryover and shared cell types may contribute to the conserved co-abundance pattern. HPA protein detection in bone marrow supports the presence of many module proteins there, but the cell-line interpretation should not be assumed to represent the same differentiated cell population.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a small set of high-confidence physical or functional relationships: ABL1 with TCF3, ABL1 with WWTR1, and CSNK1E with WWTR1. These links create limited support for a regulatory signaling substructure, but they do not connect most module genes. hu.MAP provides partial membership in several complexes. RBP4 and KLHL7 co-occur in (hu.MAP huMAP3_14155.1), while APOC3 and RBP4 co-occur in (hu.MAP huMAP3_00178.1), (hu.MAP huMAP3_08796.1), and (hu.MAP huMAP3_09832.1). Because each hu.MAP complex contains additional proteins outside the module and only a subset of its members is represented here, these findings support known biochemical or co-complex relationships rather than a complete module-wide complex. Overall, the known interaction evidence is sparse and concentrated in a few substructures.

**STRING interactions (score >= 0.7)**: 3 of 1035 gene pairs: ABL1–TCF3 (0.834); ABL1–WWTR1 (0.79); CSNK1E–WWTR1 (0.904)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14155.1 (RBP4, KLHL7; 2/3); huMAP3_00178.1 (APOC3, RBP4; 2/9); huMAP3_08796.1 (APOC3, RBP4; 2/15); huMAP3_09832.1 (APOC3, RBP4; 2/18)

### Novelty

This module should not be claimed as a new biological discovery on the present evidence. The absence of broad STRING or hu.MAP connectivity does not establish novelty, because co-abundance can arise from shared expression, cell composition, regulation, or technical context without documented physical interaction. Several genes have well-established functions and disease associations, and the module combines recognizable immune, plasma-protein, mitochondrial, transcriptional, and housekeeping-related signals. A potentially novel aspect could be the specific cross-tissue co-abundance pattern between bone marrow and cell line, but that would require replication in independent cohorts, control for cell-type composition and plasma contamination, and comparison with previously reported co-expression modules.

**Hypothesis.** Hypothesis: the module reflects a composite state produced by the shared abundance of bone-marrow or hematopoietic cells together with broadly expressed cellular maintenance programs and a circulating protein component. In this model, ITGAL, CD79A, TCF3, HLA-DRB3, IFI44L, and related genes represent hematopoietic adhesion, B-cell or antigen-presenting, and antiviral components, while RBP4, APOC3, and SPP2 represent a plasma or secretory component. ABL1, WWTR1, and CSNK1E may provide a signaling and transcriptional bridge, but their co-abundance should not be interpreted as direct physical regulation without perturbation or protein-interaction experiments.

### Important genes

#### ITGAL

- **Related proteins** (co-abundance neighbors): RBP4 (0.96), KSR1 (0.92), OTUD7B (0.90), UCKL1 (0.90), WWTR1 (0.89), ELMOD2 (0.85), TCF3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit alpha L. ITGAL encodes the integrin alpha L chain. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain. This I-domain containing alpha integrin combines with the beta 2 chain (ITGB2) to form the integrin lymphocyte function-associated antigen-1 (LFA-1), which is expressed on all leukocytes. LFA-1 plays a central role in leukocyte intercellular adhesion through…
- **Diseases (Open Targets)**: psoriasis vulgaris (0.585); dry eye syndrome (0.568); psoriasis (0.473); eye disorder (0.371); ulcerative colitis (0.336)
- **Europe PMC papers**: 2930
- **Why important**: ITGAL is the strongest network hub in the supplied module and connects to RBP4, KSR1, OTUD7B, UCKL1, WWTR1, ELMOD2, and TCF3. Its established function as the leukocyte integrin alpha chain of LFA-1, together with HPA enhancement in bone marrow, lymphoid tissue, B cells, monocytes, and neutrophils, makes it a strong marker of hematopoietic or leukocyte-related composition. It also has extensive literature and immune-disease associations.
- **Conclusion**: Established: ITGAL is a plausible biological anchor for the immune and cell-adhesion component of the module. Hypothesis: its hub position may reflect coordinated abundance of leukocyte-associated cells rather than a novel ITGAL-centered molecular complex.

#### CD79A

- **Related proteins** (co-abundance neighbors): PSMC3IP (0.94), CHCHD5 (0.93), CTSO (0.91), ATG12 (0.84), MIS18BP1 (0.83); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Group enriched; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD79a molecule. The B lymphocyte antigen receptor is a multimeric complex that includes the antigen-specific component, surface immunoglobulin (Ig). Surface Ig non-covalently associates with two other proteins, Ig-alpha and Ig-beta, which are necessary for expression and function of the B-cell antigen receptor. This gene encodes the Ig-alpha protein of the B-cell antigen component. Alternatively spliced transcrip…
- **Diseases (Open Targets)**: isolated agammaglobulinemia (0.663); agammaglobulinemia (0.472); autosomal agammaglobulinemia (0.470); diffuse large B-cell lymphoma (0.376); colorectal adenocarcinoma (0.372)
- **Europe PMC papers**: 13538
- **Why important**: CD79A is a highly connected module gene and is HPA group-enriched in lymphoid tissue and B cells, including memory and naive B-cell populations. Its established role as the Ig-alpha component of the B-cell antigen receptor directly supports B-cell identity and receptor signaling. It connects to PSMC3IP, CHCHD5, CTSO, ATG12, and MIS18BP1, and has particularly extensive literature and associations with agammaglobulinemia and B-cell malignancy.
- **Conclusion**: Established: CD79A supports a B-cell or B-lineage contribution to the module. Hypothesis: its co-abundance with cell-cycle, mitochondrial, and autophagy-related genes may reflect the state of proliferating or differentiating hematopoietic cells rather than a dedicated CD79A complex.

#### RBP4

- **Related proteins** (co-abundance neighbors): ITGAL (0.96), APOC3 (0.86); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14155.1, huMAP3_00178.1, huMAP3_08796.1, huMAP3_09832.1
- **Function (MyGene.info)**: retinol binding protein 4. This protein belongs to the lipocalin family and is the specific carrier for retinol (vitamin A alcohol) in the blood. It delivers retinol from the liver stores to the peripheral tissues. In plasma, the RBP-retinol complex interacts with transthyretin which prevents its loss by filtration through the kidney glomeruli. A deficiency of vitamin A blocks secretion of the binding protein posttranslatio…
- **Diseases (Open Targets)**: progressive retinal dystrophy due to retinol transport defect (0.696); microphthalmia, isolated, with coloboma 10 (0.643); microphthalmia, isolated, with coloboma (0.506); microphthalmia (0.501); inherited retinal dystrophy (0.421)
- **Europe PMC papers**: 18196
- **Why important**: RBP4 is a module connector to ITGAL and APOC3 and appears in all of the reported hu.MAP partial complexes (hu.MAP huMAP3_14155.1), (hu.MAP huMAP3_00178.1), (hu.MAP huMAP3_08796.1), and (hu.MAP huMAP3_09832.1). HPA identifies it as liver-enriched, hepatocyte-associated, and secreted to blood. Its established role is transport of retinol from liver stores to peripheral tissues, and it has extensive literature and strong disease associations involving retinol transport and retinal disorders.
- **Conclusion**: Established: RBP4 provides evidence for a circulating or liver-derived plasma-protein component, not for a bone-marrow intracellular pathway. Hypothesis: RBP4 may contribute to the apparent shared module through extracellular carryover or coordinated plasma-protein abundance.

#### ABL1

- **Related proteins** (co-abundance neighbors): SPP2 (0.89), HLA-DRB3 (0.89); STRING partners: TCF3 (0.834), WWTR1 (0.79)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ABL proto-oncogene 1, non-receptor tyrosine kinase. This gene is a protooncogene that encodes a protein tyrosine kinase involved in a variety of cellular processes, including cell division, adhesion, differentiation, and response to stress. The activity of the protein is negatively regulated by its SH3 domain, whereby deletion of the region encoding this domain results in an oncogene. The ubiquitously expressed protein has DNA-binding activity that…
- **Diseases (Open Targets)**: chronic myeloid leukemia (0.826); congenital heart defects and skeletal malformations syndrome (0.801); acute lymphoblastic leukemia (0.715); neoplasm (0.624); gastrointestinal stromal tumor (0.589)
- **Europe PMC papers**: 15686
- **Why important**: ABL1 is a signaling and transcriptional regulator with established roles in cell division, adhesion, differentiation, stress responses, DNA damage response, and signal transduction. It participates in the reported high-confidence STRING relationships with TCF3 and WWTR1 and connects within the module to SPP2 and HLA-DRB3. It has extensive literature and strong associations with chronic myeloid leukemia, acute lymphoblastic leukemia, and other neoplastic conditions.
- **Conclusion**: Established: ABL1 supplies a plausible signaling bridge between immune-associated and regulatory features. Hypothesis: ABL1 may help coordinate the module's cell-state signal, but the supplied data do not establish that its kinase activity drives the co-abundance pattern.

#### IFI44L

- **Related proteins** (co-abundance neighbors): NXT1 (0.90), KLHL7 (0.85), MACROH2A2 (0.84), GUF1 (0.84), ELMOD2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: interferon induced protein 44 like. Predicted to enable GTP binding activity. Involved in defense response to virus. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: MMR-related febrile seizures (0.427); Febrile seizure (within the age range of 3 months to 6 years) (0.344); response to vaccine (0.342); CINCA syndrome (0.185); Encephalopathy (0.148)
- **Europe PMC papers**: 3361
- **Why important**: IFI44L is a well-connected intermediate gene linked to NXT1, KLHL7, MACROH2A2, GUF1, and ELMOD2. Its established annotation includes interferon-induced antiviral defense and immune response. HPA shows enhancement in macrophages, microglia, ovarian stromal cells, and plasmacytoid dendritic cells, while the gene has substantial literature and associations with febrile seizures, vaccine response, and inflammatory syndromes.
- **Conclusion**: Established: IFI44L supports an interferon or antiviral cell-state interpretation within part of the module. Hypothesis: it may indicate inflammatory priming of hematopoietic cells, but the absence of globally significant GO or KEGG enrichment prevents assigning an interferon pathway to the entire module.

## Module 5

**Tissue pair**: bone_marrow and cell line  
**Genes (43)**: ACLY, ASNS, ATP1B1, C4BPA, CAPN1, COPB1, CSK, DYNC1H1, EIF3C, FASN, FLII, GLS2, HDAC1, HK1, EIF4G1, IQGAP1, CAMK2D, MYD88, NCKAP1, NSF, OSBPL9, PFKP, PLK1, PAICS, PYGL, CAD, RHBDD1, RUVBL2, RYBP, STAT1, EPRS1, FARSB, IARS1, LARS1, MARS1, QARS1, RARS1, TARS1, VARS1, CCT8, TMOD2, TNPO1, VPS35

### Function

The strongest and most coherent interpretation is cytosolic protein biosynthesis, centered on aminoacyl-tRNA charging. The primary evidence is the convergent enrichment of aminoacyl-tRNA ligase activity and tRNA aminoacylation for protein translation (GO:MF aminoacyl-tRNA ligase activity; q_global = 5.12e-07), (GO:BP tRNA aminoacylation for protein translation; q_global = 5.12e-07), the KEGG aminoacyl-tRNA biosynthesis pathway (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 1.26e-06), the aminoacyl-tRNA synthetase multienzyme complex (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 5.9e-06), tRNA-directed catalytic activity (GO:MF catalytic activity, acting on a tRNA; q_global = 0.000862), tRNA metabolic process (GO:BP tRNA metabolic process; q_global = 0.00801), translation (GO:BP translation; q_global = 0.0451), and protein biosynthetic process (GO:BP protein biosynthetic process; q_global = 0.0451). The module also contains a broader nucleotide and ATP-binding signal (GO:MF ATP binding; q_global = 1.11e-06), (GO:MF adenyl ribonucleotide binding; q_global = 1.22e-06), (GO:MF adenyl nucleotide binding; q_global = 4.96e-06), (GO:MF purine ribonucleoside triphosphate binding; q_global = 2.06e-05), (6 globally significant GO/KEGG terms, q_global 2.23e-05–0.000335; see the table), consistent with the ATP dependence of many biosynthetic enzymes. Additional globally significant terms support amino-acid metabolism (GO:BP amino acid metabolic process; q_global = 2.09e-05), cytosolic localization (GO:CC cytosol; q_global = 0.000603), and extracellular-vesicle or extracellular-space annotations (5 globally significant GO/KEGG terms, q_global 0.02–0.04; see the table), but the latter are less specific and should not override the translation-centered interpretation. The network is not a single uniform complex: it contains a densely connected aminoacyl-tRNA synthetase cluster, translation-initiation links, metabolic enzymes, trafficking proteins, cytoskeletal or motor proteins, and signaling or chromatin-associated proteins. Thus, the module most plausibly represents coordinated translational capacity with supporting energy, amino-acid, nucleotide, and intracellular-transport functions.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module. HPA identifies only C4BPA as secreted to blood, whereas the remaining genes are intracellular or broadly cellular proteins. The module is largely composed of genes with low tissue specificity, and many have low immune-cell specificity, arguing against a simple blood-cell-specific program. However, HPA also shows substantial cell-type enhancement across diverse cell types, including neutrophils, erythrocyte progenitors, lymphoid or myeloid-related cells, neural cells, epithelial cells, and germ-cell populations. Bone-marrow protein detection is present for many members, while some synthetases are not detected there despite their module membership. Therefore, the shared bone-marrow and cell-line signal may reflect a broadly expressed housekeeping and proliferative program, potentially influenced by common cellular composition, rather than a specialized secreted or immune-cell program. The liver and digestive-gland signals in STRING and HPA should be interpreted cautiously because they may reflect broad expression or shared biosynthetic demand rather than liver-specific function.

**GO/KEGG enrichment**: 31 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF aminoacyl-tRNA ligase activity | 5.12e-07 | EPRS1, FARSB, IARS1, LARS1, MARS1, QARS1, RARS1, TARS1, VARS1 |
| GO:BP tRNA aminoacylation for protein translation | 5.12e-07 | EPRS1, FARSB, IARS1, LARS1, MARS1, QARS1, RARS1, TARS1, VARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 5.12e-07 | EPRS1, FARSB, IARS1, LARS1, MARS1, QARS1, RARS1, TARS1, VARS1 |
| GO:BP amino acid activation | 1.01e-06 | EPRS1, FARSB, IARS1, LARS1, MARS1, QARS1, RARS1, TARS1, VARS1 |
| GO:BP tRNA aminoacylation | 1.01e-06 | EPRS1, FARSB, IARS1, LARS1, MARS1, QARS1, RARS1, TARS1, VARS1 |
| GO:MF ATP binding | 1.11e-06 | ACLY, ASNS, CAD, CAMK2D, CCT8, CSK, DYNC1H1, EIF4G1, EPRS1, FARSB, HK1, IARS1, LARS1, MARS1, NSF, PAICS, PFKP, PLK1, PYGL, QARS1, RARS1, RUVBL2, TARS1, VARS1 |
| GO:MF adenyl ribonucleotide binding | 1.22e-06 | ACLY, ASNS, CAD, CAMK2D, CCT8, CSK, DYNC1H1, EIF4G1, EPRS1, FARSB, HK1, IARS1, LARS1, MARS1, NSF, PAICS, PFKP, PLK1, PYGL, QARS1, RARS1, RUVBL2, TARS1, VARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 1.26e-06 | EPRS1, FARSB, IARS1, LARS1, MARS1, QARS1, RARS1, TARS1, VARS1 |
| GO:MF ligase activity | 1.51e-06 | ASNS, CAD, EPRS1, FARSB, IARS1, LARS1, MARS1, PAICS, QARS1, RARS1, TARS1, VARS1 |
| GO:MF adenyl nucleotide binding | 4.96e-06 | ACLY, ASNS, CAD, CAMK2D, CCT8, CSK, DYNC1H1, EIF4G1, EPRS1, FARSB, HK1, IARS1, LARS1, MARS1, NSF, PAICS, PFKP, PLK1, PYGL, QARS1, RARS1, RUVBL2, TARS1, VARS1 |
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 5.9e-06 | EPRS1, IARS1, LARS1, MARS1, QARS1, RARS1 |
| GO:MF anion binding | 1.73e-05 | ACLY, ASNS, CAD, CAMK2D, CCT8, CSK, DYNC1H1, EIF4G1, EPRS1, FARSB, FASN, FLII, HK1, IARS1, IQGAP1, LARS1, MARS1, NSF, PAICS, PFKP, PLK1, PYGL, QARS1, RARS1, RUVBL2, TARS1, VARS1 |
| GO:MF purine ribonucleoside triphosphate binding | 2.06e-05 | ACLY, ASNS, CAD, CAMK2D, CCT8, CSK, DYNC1H1, EIF4G1, EPRS1, FARSB, HK1, IARS1, LARS1, MARS1, NSF, PAICS, PFKP, PLK1, PYGL, QARS1, RARS1, RUVBL2, TARS1, VARS1 |
| GO:BP amino acid metabolic process | 2.09e-05 | ASNS, CAD, EPRS1, FARSB, GLS2, IARS1, LARS1, MARS1, QARS1, RARS1, TARS1, VARS1 |
| GO:MF purine ribonucleotide binding | 2.23e-05 | ACLY, ASNS, CAD, CAMK2D, CCT8, CSK, DYNC1H1, EIF4G1, EPRS1, FARSB, HK1, IARS1, LARS1, MARS1, NSF, PAICS, PFKP, PLK1, PYGL, QARS1, RARS1, RUVBL2, TARS1, VARS1 |

### STRING and hu.MAP

STRING independently supports the central synthetase interpretation: the aminoacyl-tRNA synthetase relationships and related functional groupings recur across (STRING RCTM Cytosolic tRNA aminoacylation; within-query FDR = 1.45e-08), (STRING Keyword Aminoacyl-tRNA synthetase; within-query FDR = 4.14e-08), (STRING Function aminoacyl-tRNA ligase activity; within-query FDR = 1.25e-07), (STRING KEGG Aminoacyl-tRNA biosynthesis; within-query FDR = 1.29e-07), (STRING Process tRNA aminoacylation for protein translation; within-query FDR = 1.34e-06), and (STRING NetworkNeighborAL tRNA Aminoacylation, and glutamyl-tRNA(Gln) amidotransferase complex; within-query FDR = 1.53e-06). The high-confidence STRING links among EPRS1, IARS1, LARS1, MARS1, QARS1, RARS1, TARS1, VARS1, and FARSB are consistent with known functional association within the aminoacylation machinery. STRING also supports translation-initiation connectivity through EIF3C and EIF4G1, metabolic coupling through ACLY and FASN, glycolysis through HK1 and PFKP, nucleotide or amino-acid metabolism through CAD, ASNS, and GLS2, and signaling or chromatin links involving MYD88, STAT1, HDAC1, and RUVBL2. hu.MAP provides stronger complex-level evidence: (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1) contain the same core group of aminoacyl-tRNA synthetases, while (hu.MAP huMAP3_10103.1) supports a CAD-FASN metabolic association and (hu.MAP huMAP3_13175.1) and (hu.MAP huMAP3_11246.1) support EIF3C-EIF4G1 translation complexes. These observations indicate that much of the module reflects established molecular machinery rather than arbitrary co-abundance. The remaining module edges may represent co-regulation, shared abundance across cell states, indirect functional coupling, or sample-composition effects; co-abundance alone does not establish direct physical interaction.

**STRING interactions (score >= 0.7)**: 51 of 903 gene pairs: ACLY–FASN (0.994); ASNS–CAD (0.945); ASNS–IARS1 (0.804); CAD–GLS2 (0.918); CCT8–RUVBL2 (0.776); DYNC1H1–PLK1 (0.829); EIF3C–EIF4G1 (0.99); EIF3C–EPRS1 (0.755); EIF4G1–VPS35 (0.899); EPRS1–FARSB (0.925); EPRS1–GLS2 (0.805); EPRS1–IARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–MARS1 (0.999); EPRS1–QARS1 (0.999); EPRS1–RARS1 (0.999); EPRS1–TARS1 (0.928); EPRS1–VARS1 (0.97); FARSB–IARS1 (0.914); FARSB–LARS1 (0.814); FARSB–MARS1 (0.705); FARSB–RARS1 (0.706); FARSB–TARS1 (0.735); FARSB–VARS1 (0.776); FLII–MYD88 (0.814); HDAC1–RUVBL2 (0.946); HDAC1–STAT1 (0.969); HK1–PFKP (0.995); IARS1–LARS1 (0.999); IARS1–MARS1 (0.999); IARS1–QARS1 (0.999); IARS1–RARS1 (0.999); IARS1–TARS1 (0.913); IARS1–VARS1 (0.9); LARS1–MARS1 (0.999); LARS1–QARS1 (0.999); LARS1–RARS1 (0.999); LARS1–TARS1 (0.98); LARS1–VARS1 (0.968); MARS1–QARS1 (0.999); MARS1–RARS1 (0.999); MARS1–TARS1 (0.881); MARS1–VARS1 (0.902); MYD88–STAT1 (0.877); PFKP–PYGL (0.721); QARS1–RARS1 (0.999); QARS1–TARS1 (0.807); QARS1–VARS1 (0.91); RARS1–TARS1 (0.806); RARS1–VARS1 (0.905); TARS1–VARS1 (0.905)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Liver (FDR = 3.91e-09, 30 genes); RCTM Cytosolic tRNA aminoacylation (FDR = 1.45e-08, 9 genes); Keyword Ligase (FDR = 2.35e-08, 12 genes); TISSUES Digestive gland (FDR = 2.8e-08, 32 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 4.14e-08, 9 genes); Keyword Protein biosynthesis (FDR = 4.21e-08, 11 genes); Function aminoacyl-tRNA ligase activity (FDR = 1.25e-07, 9 genes); Function ATP binding (FDR = 1.25e-07, 24 genes); Function Ligase activity (FDR = 1.25e-07, 12 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 1.29e-07, 9 genes); Keyword ATP-binding (FDR = 1.89e-07, 22 genes); Keyword Nucleotide-binding (FDR = 1.14e-06, 23 genes); Function Anion binding (FDR = 1.19e-06, 26 genes); Process tRNA aminoacylation for protein translation (FDR = 1.34e-06, 9 genes); NetworkNeighborAL tRNA Aminoacylation, and glutamyl-tRNA(Gln) amidotransferase complex (FDR = 1.53e-06, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, TARS1, IARS1, QARS1, RARS1, MARS1, LARS1; 7/14); huMAP3_13688.1 (EPRS1, TARS1, IARS1, QARS1, RARS1, MARS1, LARS1; 7/14); huMAP3_10103.1 (CAD, FASN; 2/4); huMAP3_13175.1 (EIF4G1, EIF3C; 2/20); huMAP3_11246.1 (EIF4G1, EIF3C; 2/24)

### Novelty

The core functional finding is not a new molecular complex: aminoacyl-tRNA synthetases are established components of translation machinery, and their relationships are supported by STRING (STRING RCTM Cytosolic tRNA aminoacylation; within-query FDR = 1.45e-08), (STRING Keyword Aminoacyl-tRNA synthetase; within-query FDR = 4.14e-08), (STRING Function aminoacyl-tRNA ligase activity; within-query FDR = 1.25e-07), (STRING KEGG Aminoacyl-tRNA biosynthesis; within-query FDR = 1.29e-07), (STRING Process tRNA aminoacylation for protein translation; within-query FDR = 1.34e-06), (STRING NetworkNeighborAL tRNA Aminoacylation, and glutamyl-tRNA(Gln) amidotransferase complex; within-query FDR = 1.53e-06) and hu.MAP (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1). The translation-initiation and metabolic substructures are also supported by hu.MAP (hu.MAP huMAP3_10103.1) (hu.MAP huMAP3_13175.1) (hu.MAP huMAP3_11246.1) and corresponding STRING relationships. Accordingly, this module should not be claimed as a newly discovered aminoacylation complex. What may be novel is the reproducible co-abundance organization of this established machinery with metabolic, transport, cytoskeletal, and signaling genes specifically shared between bone marrow and cell line. That claim remains provisional because the fact sheet does not provide an external replication cohort, perturbation evidence, temporal information, or a comparison with previously defined co-abundance modules. Absence of hu.MAP or STRING support for individual peripheral genes would not by itself establish novelty.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular state in which high translational demand is coordinated with amino-acid charging, nucleotide and energy metabolism, protein-folding or transport capacity, and cell-cycle or stress-related support. The aminoacyl-tRNA synthetase cluster may provide the core translational backbone, while EIF3C and EIF4G1 connect charging capacity to translation initiation; CAD, PAICS, ASNS, GLS2, ACLY, FASN, HK1, PFKP, and PYGL may supply biosynthetic or energetic support; and DYNC1H1, VPS35, COPB1, NSF, and cytoskeletal regulators may support intracellular distribution of newly synthesized proteins. The hypothesis predicts that module activity will track protein-synthesis demand or proliferative state more strongly than a lineage-specific immune identity. It also predicts that perturbing the synthetase or initiation submodule should alter the abundance or activity of the linked metabolic and transport components, but this causal prediction requires experimental testing.

### Important genes

#### EPRS1

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.87), IARS1 (0.86), RARS1 (0.85), LARS1 (0.85), TARS1 (0.82); STRING partners: EIF3C (0.755), FARSB (0.925), GLS2 (0.805), IARS1 (0.999), LARS1 (0.999), MARS1 (0.999), QARS1 (0.999), RARS1 (0.999), TARS1 (0.928), VARS1 (0.97)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is a central bridge in the synthetase component: it has direct STRING relationships with most of the aminoacyl-tRNA synthetase cluster, belongs to hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), and is represented across the primary translation and aminoacylation terms (5 globally significant GO/KEGG terms, q_global 5.12e-07–1.01e-06; see the table), (17 globally significant GO/KEGG terms, q_global 1.26e-06–0.00801; see the table), (GO:BP translation; q_global = 0.0451), and (GO:BP protein biosynthetic process; q_global = 0.0451). Its annotated function is glutamyl- and prolyl-tRNA charging, and it also has an annotation for negative regulation of translation. Its network position and broad literature support make it a strong representative of the module core.
- **Conclusion**: Established evidence supports EPRS1 as a core aminoacylation and translation gene in this module. It is reasonable to hypothesize that EPRS1 helps define the shared translational state, but the co-abundance data do not demonstrate that EPRS1 drives the module.

#### IARS1

- **Related proteins** (co-abundance neighbors): DYNC1H1 (0.87), EPRS1 (0.86), RARS1 (0.85), ACLY (0.84), CAD (0.84), VARS1 (0.84), EIF4G1 (0.83), CAPN1 (0.83), PYGL (0.81), NCKAP1 (0.80); STRING partners: ASNS (0.804), EPRS1 (0.999), FARSB (0.914), LARS1 (0.999), MARS1 (0.999), QARS1 (0.999), RARS1 (0.999), TARS1 (0.913), VARS1 (0.9)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Isoleucine-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family and has been identified as a …
- **Diseases (Open Targets)**: growth retardation, intellectual developmental disorder, hypotonia, and hepatopathy (0.733); Abnormality of the skeletal system (0.332); microcephaly (0.289); Global developmental delay (0.289); Hallux valgus (0.184)
- **Europe PMC papers**: 184
- **Why important**: IARS1 has one of the strongest network positions among the synthetases, extensive STRING connectivity to the synthetase cluster, membership in hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), and representation in every primary enrichment theme spanning aminoacylation, translation, nucleotide binding, cytosol, and extracellular-vesicle annotations. Its established role is charging tRNA with isoleucine, and the fact sheet links it to translational fidelity, autoimmune myositis or dermatomyositis autoantibodies, and developmental or skeletal disease associations.
- **Conclusion**: Established evidence supports IARS1 as a central component of the translation machinery represented by the module. Its network prominence makes it a useful marker of the module core, but disease associations do not establish that this module mediates those diseases.

#### LARS1

- **Related proteins** (co-abundance neighbors): EPRS1 (0.85), DYNC1H1 (0.82), CAD (0.81); STRING partners: EPRS1 (0.999), FARSB (0.814), IARS1 (0.999), MARS1 (0.999), QARS1 (0.999), RARS1 (0.999), TARS1 (0.98), VARS1 (0.968)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: leucyl-tRNA synthetase 1. This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals w…
- **Diseases (Open Targets)**: infantile liver failure syndrome 1 (0.670); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.510); Global developmental delay (0.119); sensorineural hearing loss disorder (0.119); Generalized-onset seizure (0.118)
- **Europe PMC papers**: 267
- **Why important**: LARS1 is part of the densely connected aminoacyl-tRNA synthetase group in STRING and hu.MAP (hu.MAP huMAP3_02637.1), (hu.MAP huMAP3_13688.1), and is represented throughout the primary aminoacylation and translation terms (5 globally significant GO/KEGG terms, q_global 5.12e-07–1.01e-06; see the table), (17 globally significant GO/KEGG terms, q_global 1.26e-06–0.00801; see the table), (GO:BP translation; q_global = 0.0451), and (GO:BP protein biosynthetic process; q_global = 0.0451). It catalyzes leucine-tRNA charging, is part of a multisynthetase complex, and has annotations for cellular responses to amino-acid availability and leucine. Its links to amino-acid sensing and infantile liver failure provide biological context beyond generic translation.
- **Conclusion**: Established evidence supports LARS1 as both a translation enzyme and a plausible indicator of nutrient-responsive biosynthetic demand. A role for LARS1 in coordinating the broader metabolic portion of this module is a hypothesis, not a demonstrated mechanism.

#### EIF4G1

- **Related proteins** (co-abundance neighbors): IARS1 (0.83), CAD (0.82), DYNC1H1 (0.82), QARS1 (0.81); STRING partners: EIF3C (0.99), VPS35 (0.899)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_13175.1, huMAP3_11246.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 connects the aminoacylation-rich portion of the module to translation initiation through its module edges and the STRING relationship with EIF3C. It belongs to hu.MAP complexes (hu.MAP huMAP3_13175.1) and (hu.MAP huMAP3_11246.1), is included in the primary translation and protein-biosynthesis terms (GO:BP translation; q_global = 0.0451), (GO:BP protein biosynthetic process; q_global = 0.0451), and is annotated as a scaffold of the EIF4F complex that recruits capped mRNA to the ribosome. Its disease associations include Parkinson disease and neurodegenerative disease, while its literature volume is substantial.
- **Conclusion**: Established evidence supports EIF4G1 as the principal translation-initiation connector in the module. It may couple aminoacylation capacity to initiation demand, but the co-abundance structure alone cannot establish directionality or regulation.

#### DYNC1H1

- **Related proteins** (co-abundance neighbors): IARS1 (0.87), PYGL (0.87), EPRS1 (0.87), VPS35 (0.85), VARS1 (0.84), ACLY (0.84), CAD (0.83), RARS1 (0.83), FLII (0.83), EIF3C (0.83), TARS1 (0.83), EIF4G1 (0.82), LARS1 (0.82), TNPO1 (0.81), NCKAP1 (0.81), QARS1 (0.81), COPB1 (0.80), NSF (0.80); STRING partners: PLK1 (0.829)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 1 heavy chain 1. Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polyp…
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy without contractures (0.816); intellectual disability, autosomal dominant 13 (0.815); Charcot-Marie-Tooth disease axonal type 2O (0.799); autosomal dominant non-syndromic intellectual disability (0.634); hereditary disease (0.545)
- **Europe PMC papers**: 1731
- **Why important**: DYNC1H1 has the strongest network position in the reported subgraph and connects synthetase genes with metabolic, trafficking, and cell-cycle-related members, including STRING support for PLK1. Its established function is cytoplasmic dynein-mediated intracellular transport, organelle movement, retrograde transport, and spindle dynamics. It is detected in bone marrow, has brain-enhanced HPA expression, and has extensive disease and literature associations.
- **Conclusion**: Established evidence supports DYNC1H1 as a structural or transport-related connector rather than as a core aminoacylation enzyme. A plausible hypothesis is that it links translational capacity to intracellular distribution or proliferative architecture, but this proposed role is not directly demonstrated by the module.

#### CAD

- **Related proteins** (co-abundance neighbors): IARS1 (0.84), DYNC1H1 (0.83), EIF4G1 (0.82), LARS1 (0.81); STRING partners: ASNS (0.945), GLS2 (0.918)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_10103.1
- **Function (MyGene.info)**: carbamoyl-phosphate synthetase 2, aspartate transcarbamylase, and dihydroorotase. The de novo synthesis of pyrimidine nucleotides is required for mammalian cells to proliferate. This gene encodes a trifunctional protein which is associated with the enzymatic activities of the first 3 enzymes in the 6-step pathway of pyrimidine biosynthesis: carbamoylphosphate synthetase (CPS II), aspartate transcarbamoylase, and dihydroorotase. This protein is regulated by the mitogen-activated…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 50 (0.660); congenital disorder of glycosylation type I (0.595); infantile epileptic-dyskinetic encephalopathy (0.499); type 2 diabetes mellitus (0.286); urolithiasis (0.283)
- **Europe PMC papers**: 60667
- **Why important**: CAD provides a metabolic bridge from the translation-centered core to nucleotide production. It has module links to several synthetase-associated genes, STRING support with ASNS and GLS2, and membership with FASN in hu.MAP complex (hu.MAP huMAP3_10103.1). Its established function is the trifunctional first portion of de novo pyrimidine biosynthesis, and it contributes to the primary ATP-binding, ligase, nucleotide-binding, amino-acid-metabolism, and extracellular annotations (GO:MF ATP binding; q_global = 1.11e-06), (14 globally significant GO/KEGG terms, q_global 1.51e-06–0.000757; see the table), (5 globally significant GO/KEGG terms, q_global 0.02–0.04; see the table). It has a very large literature base and substantial disease relevance.
- **Conclusion**: Established evidence supports CAD as a biosynthetic support node that can supply nucleotide demand associated with protein synthesis and proliferation. Its exact contribution to the shared bone-marrow and cell-line co-abundance pattern remains a hypothesis requiring perturbation or flux evidence.

## Module 6

**Tissue pair**: bone_marrow and cell line  
**Genes (46)**: ACOX3, AFDN, AKAP17A, AQR, BAG5, BAZ2A, CACNG6, CEP44, COTL1, POLD1, POLD3, EHBP1L1, ERGIC2, GLTP, GMPR, HMGA1, HSPBP1, SERPING1, EIF4A2, INTS14, IRF5, NDUFA3, NDUFS5, NDFIP2, NIPSNAP1, NOL11, NOL6, NUP85, NUP88, P4HA1, LPCAT1, PELO, PREPL, RBM15, SLC29A1, SLC35F3, SCFD1, SMARCA4, SNAP23, SNX6, HARS2, THUMPD1, TMX1, TOP2A, VAC14, WDR18

### Function

No GO/KEGG term passed global correction, and STRING supplied no functional enrichment; therefore this module should not be assigned a single statistically established pathway. The network is better interpreted as a composite co-abundance state containing several connected functional themes. Its strongest organizing signal is SLC35F3, which links genes involved in membrane transport, vesicle biology, mitochondrial respiration, RNA surveillance, and translation-related processes. Other subnetworks contain complement regulation and immune signaling around SERPING1 and IRF5; mitochondrial complex I components NDUFA3 and NDUFS5; nucleolar ribosome biogenesis involving NOL6, NOL11, and WDR18; nuclear pore biology involving NUP85 and NUP88; and DNA replication and repair involving POLD1 and POLD3. The evidence therefore supports a broad cellular-state interpretation involving transport, proteostasis, energy metabolism, RNA and DNA processing, and immune or blood-associated biology, rather than a single defined biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a small secreted component, with SERPING1 being the clearest plasma protein. Most genes have low tissue specificity, and many have low immune-cell specificity, which is compatible with broadly expressed cellular or housekeeping-type biology. Nevertheless, the module includes immune-enhanced genes and cell types associated with eosinophils, basophils, neutrophils, plasmacytoid dendritic cells, monocytes, megakaryocytes, and platelets. HPA also shows frequent enhancement in esophageal apical cells, reproductive cell types, and other specialized cells, so the module is not a simple bone-marrow lineage signature. Protein detection in bone marrow is widespread among the annotated genes, whereas there is no matching HPA tissue measurement for the cell-line condition. The shared module may therefore reflect a mixture of broadly expressed cellular programs plus variable blood or immune-cell composition, rather than a bone-marrow-specific mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a small set of high-confidence relationships: NDUFA3 with NDUFS5, NOL11 with NOL6, NOL6 with WDR18, NUP85 with NUP88, and POLD1 with POLD3. These relationships support real local molecular units involving mitochondrial complex I, ribosome biogenesis, the nuclear pore, and DNA polymerase delta. However, STRING does not connect most of the module and reports no functional enrichment, so it does not establish a unified interaction network. hu.MAP independently supports partial membership in the DNA polymerase delta complex through POLD1 and POLD3 (hu.MAP huMAP3_04554.1), heat-shock or cochaperone-related assemblies through HSPBP1 and BAG5 (hu.MAP huMAP3_06506.1), (hu.MAP huMAP3_07919.1), (hu.MAP huMAP3_11049.1), (hu.MAP huMAP3_13774.1), and mitochondrial complex I assemblies through NDUFA3 and NDUFS5 (hu.MAP huMAP3_02819.1), (hu.MAP huMAP3_14018.1), (hu.MAP huMAP3_06397.1), (hu.MAP huMAP3_09982.1), (hu.MAP huMAP3_09567.1), (hu.MAP huMAP3_14878.1). It also supports partial membership of SNAP23 and SCFD1 in vesicle-fusion complexes (hu.MAP huMAP3_06458.1), (hu.MAP huMAP3_08929.1), (hu.MAP huMAP3_10587.1), (hu.MAP huMAP3_13160.1), of NUP85 and NUP88 in a nuclear-pore complex (hu.MAP huMAP3_12581.1), and of HARS2 and PREPL in a broad mitochondrial or metabolic assembly (hu.MAP huMAP3_13468.1). Because most hu.MAP complexes contain only a small subset of their members in this module, these results support molecular plausibility for local subnetworks but not a single physical complex spanning the module.

**STRING interactions (score >= 0.7)**: 5 of 1035 gene pairs: NDUFA3–NDUFS5 (0.999); NOL11–NOL6 (0.919); NOL6–WDR18 (0.773); NUP85–NUP88 (0.998); POLD1–POLD3 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04554.1 (POLD1, POLD3; 2/5); huMAP3_06506.1 (HSPBP1, BAG5; 2/23); huMAP3_07919.1 (HSPBP1, BAG5; 2/27); huMAP3_11049.1 (HSPBP1, BAG5; 2/30); huMAP3_13774.1 (HSPBP1, BAG5; 2/33); huMAP3_02819.1 (NDUFS5, NDUFA3; 2/34); huMAP3_06458.1 (SNAP23, SCFD1; 2/41); huMAP3_08929.1 (SNAP23, SCFD1; 2/44); huMAP3_10587.1 (SNAP23, SCFD1; 2/45); huMAP3_14018.1 (NDUFS5, NDUFA3; 2/48); huMAP3_06397.1 (NDUFS5, NDUFA3; 2/49); huMAP3_09982.1 (NDUFS5, NDUFA3; 2/49); huMAP3_13160.1 (SNAP23, SCFD1; 2/49); huMAP3_14723.1 (HSPBP1, BAG5; 2/52); huMAP3_09567.1 (NDUFS5, NDUFA3; 2/52); huMAP3_14878.1 (NDUFS5, NDUFA3; 2/53); huMAP3_12581.1 (NUP88, NUP85; 2/58); huMAP3_13468.1 (HARS2, PREPL; 2/99)

### Novelty

The module as a cross-tissue co-abundance pattern could be a new observation, but the present evidence is insufficient to call it a newly discovered biological pathway or complex. Its component relationships are largely established: several are directly represented in STRING and hu.MAP, while the individual genes have well-described functions and disease associations. The potentially novel aspect is the reproducible combination of these otherwise distinct programs in bone marrow and a cell line. That combination may reflect a shared cellular state, sample composition, or correlated expression of common stress, growth, transport, and biosynthetic programs. Absence of many edges from STRING or hu.MAP does not demonstrate novelty, because co-abundance can arise from regulation, cell mixture, or condition-specific coordination without direct physical interaction. Replication in independent datasets, control for cell composition, and comparison with published co-expression modules would be needed before claiming novelty.

**Hypothesis.** Hypothesis: this conserved module reflects a shared proliferative or stress-adaptive cellular state that coordinates mitochondrial energy production, protein and RNA quality control, vesicle and membrane trafficking, nuclear transport, DNA synthesis and repair, and selected innate-immune or complement-related responses. SLC35F3 may mark the broad co-abundance backbone, while NDFIP2 may connect trafficking, ubiquitin regulation, nuclear-pore, nucleolar, and mitochondrial components. SERPING1 and IRF5 could represent an immune or extracellular-complement overlay, potentially strengthened by blood-cell mixture in bone marrow. This hypothesis predicts that module activity will track cell-state composition and stress or growth conditions more strongly than it will track one isolated pathway, and that its apparent conservation will weaken after careful adjustment for lineage composition.

### Important genes

#### SLC35F3

- **Related proteins** (co-abundance neighbors): EIF4A2 (0.94), NDUFA3 (0.93), NIPSNAP1 (0.90), SNAP23 (0.89), LPCAT1 (0.89), TMX1 (0.88), SCFD1 (0.86), PELO (0.85), GLTP (0.85), INTS14 (0.85), BAZ2A (0.83), RBM15 (0.82), HSPBP1 (0.82), NUP88 (0.81), SLC29A1 (0.81), AKAP17A (0.80), NOL6 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 35 member F3. Involved in thiamine transport. Predicted to be integral component of membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypertensive disorder (0.465); neurodegenerative disease (0.369); alcohol drinking (0.338); diverticular disease (0.320); pericarditis (0.309)
- **Europe PMC papers**: 590
- **Why important**: SLC35F3 is the principal network hub by weighted connectivity and links otherwise diverse parts of the module, including EIF4A2, NDUFA3, NIPSNAP1, SNAP23, LPCAT1, TMX1, SCFD1, and PELO. Its annotation supports thiamine and choline transport and a Golgi-associated membrane role. HPA places it in brain-enriched and plasmacytoid-dendritic-cell-associated contexts, while the literature volume is substantial. It has no STRING or hu.MAP support in this module, making its central co-abundance position especially important to validate.
- **Conclusion**: Established evidence: SLC35F3 is the strongest network connector and has annotated transporter biology. Hypothesis: it may be a marker or regulator of the shared cellular state, but the module does not establish that it mechanistically controls the other genes.

#### SERPING1

- **Related proteins** (co-abundance neighbors): HARS2 (0.98), IRF5 (0.92), ACOX3 (0.91), COTL1 (0.91), PREPL (0.89), CEP44 (0.89), SMARCA4 (0.87), VAC14 (0.86), HMGA1 (0.86), AFDN (0.86), ERGIC2 (0.86), P4HA1 (0.84), THUMPD1 (0.83), BAG5 (0.83), EHBP1L1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family G member 1. This gene encodes a highly glycosylated plasma protein involved in the regulation of the complement cascade. Its encoded protein, C1 inhibitor, inhibits activated C1r and C1s of the first complement component and thus regulates complement activation. It is synthesized in the liver, and its deficiency is associated with hereditary angioneurotic oedema (HANE). Alternative splicing results in multipl…
- **Diseases (Open Targets)**: hereditary angioedema with C1Inh deficiency (0.828); hereditary angioedema type 1 (0.750); hereditary angioedema (0.728); angioedema (0.616); hereditary angioedema type 2 (0.614)
- **Europe PMC papers**: 4203
- **Why important**: SERPING1 is a second major network hub and is the clearest secreted, plasma-associated gene in the module. Its established function is inhibition of complement activation, and HPA links it to liver, neutrophil, and plasmacytoid-dendritic-cell contexts. It connects to IRF5, COTL1, HARS2, ACOX3, PREPL, CEP44, SMARCA4, and VAC14 in the co-abundance network, despite having no STRING or hu.MAP relationship reported here. Its disease associations and extensive literature make it a biologically interpretable anchor for the immune or extracellular component.
- **Conclusion**: Established evidence: SERPING1 is a complement-regulatory plasma protein with strong disease relevance. Hypothesis: its presence may report extracellular inflammatory or blood-composition variation rather than participation in a physical complex with the intracellular module.

#### NDFIP2

- **Related proteins** (co-abundance neighbors): CACNG6 (0.88), NUP85 (0.85), LPCAT1 (0.84), IRF5 (0.84), WDR18 (0.82), NDUFS5 (0.81), AQR (0.81), NOL11 (0.80), POLD3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Nedd4 family interacting protein 2. Enables WW domain binding activity. Involved in negative regulation of gene expression; negative regulation of transport; and positive regulation of protein ubiquitination. Located in several cellular components, including Golgi apparatus; mitochondrion; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: diverticular disease (0.386); refractive error (0.342); response to antihypertensive drug (0.298); smoking initiation (0.280); Apnea (0.279)
- **Europe PMC papers**: 354
- **Why important**: NDFIP2 occupies an intermediate network position and connects CACNG6, NUP85, LPCAT1, IRF5, WDR18, NDUFS5, AQR, and NOL11. Its annotations involve ubiquitin regulation, vesicular transport, mitochondria, and positive regulation of canonical NF-kappa B signaling. HPA shows broad tissue specificity with enhancement in eosinophils and several epithelial or reproductive cell types. Although it lacks STRING and hu.MAP partners in the supplied evidence, its position between multiple functional neighborhoods makes it a useful candidate integrator.
- **Conclusion**: Established evidence: NDFIP2 has functions compatible with trafficking, ubiquitin regulation, and inflammatory signaling. Hypothesis: NDFIP2 may help couple the module's cellular-maintenance and immune-associated signals, but this inferred bridging role requires perturbation or independent datasets.

#### IRF5

- **Related proteins** (co-abundance neighbors): SERPING1 (0.92), NDFIP2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: interferon regulatory factor 5. This gene encodes a member of the interferon regulatory factor (IRF) family, a group of transcription factors with diverse roles, including virus-mediated activation of interferon, and modulation of cell growth, differentiation, apoptosis, and immune system activity. Members of the IRF family are characterized by a conserved N-terminal DNA-binding domain containing tryptophan (W) repeats. Alternat…
- **Diseases (Open Targets)**: systemic lupus erythematosus (0.646); rheumatoid arthritis (0.634); inflammatory bowel disease (0.532); hypothyroidism (0.525); systemic sclerosis (0.523)
- **Europe PMC papers**: 8196
- **Why important**: IRF5 is the most direct transcriptional and innate-immune regulator represented among the selected genes. Its annotations include cytokine production, type I interferon production, immune-system activity, and transcriptional regulation. It is connected in the module to SERPING1 and NDFIP2, and HPA places it in dendritic-cell, macrophage-associated, and epithelial contexts with bone-marrow protein detection. Its extensive literature and associations with systemic lupus erythematosus, rheumatoid arthritis, inflammatory bowel disease, and systemic sclerosis make it a strong biological interpretive anchor.
- **Conclusion**: Established evidence: IRF5 is an immune transcription factor with well-supported inflammatory and interferon-related functions. Hypothesis: IRF5 may explain an immune-state component of the module, but the co-abundance pattern alone cannot show that IRF5 transcriptionally drives the other module genes.

#### POLD1

- **Related proteins** (co-abundance neighbors): GMPR (0.82); STRING partners: POLD3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_04554.1
- **Function (MyGene.info)**: DNA polymerase delta 1, catalytic subunit. This gene encodes the 125-kDa catalytic subunit of DNA polymerase delta. DNA polymerase delta possesses both polymerase and 3' to 5' exonuclease activity and plays a critical role in DNA replication and repair. Alternatively spliced transcript variants have been observed for this gene, and a pseudogene of this gene is located on the long arm of chromosome 6. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: mandibular hypoplasia-deafness-progeroid syndrome (0.768); non-small cell lung carcinoma (0.690); acute lymphoblastic leukemia (0.671); colorectal cancer (0.670); acute myeloid leukemia (0.659)
- **Europe PMC papers**: 3886
- **Why important**: POLD1 is the catalytic subunit of DNA polymerase delta and is directly paired with POLD3 in STRING and hu.MAP (hu.MAP huMAP3_04554.1). Its established functions include DNA replication, DNA repair, exonuclease activity, and gap filling. It connects in the module to GMPR, and GMPR also links to TOP2A, providing a plausible local relationship to nucleotide metabolism and proliferative DNA handling. POLD1 has extensive literature and disease associations including leukemia and multiple cancers, making it a strong representative of the replication and genome-maintenance component.
- **Conclusion**: Established evidence: POLD1 and POLD3 form a supported DNA polymerase delta subnetwork with established replication and repair functions. Hypothesis: this subnetwork may indicate a proliferative or genome-maintenance state shared by the bone-marrow and cell-line samples, rather than a module-specific interaction with the immune or secreted components.

## Module 7

**Tissue pair**: bone_marrow and cell line  
**Genes (41)**: AP1B1, AP3B1, ATP2A3, ATAD2B, BTK, CORO1A, CPPED1, DOCK8, DPP3, EPHB6, PTK2B, HCK, ICAM2, IKZF2, KNG1, PRKCB, MEFV, MTA2, MTMR9, NSD1, ORC3, PKN1, LCP1, PTPN6, RAC2, RRM1, RMI1, RNASEH1, DIS3, RRS1, SEPTIN6, SIPA1, SORL1, SRR, TBC1D5, TBXAS1, TIMM29, TOP2B, FERMT3, VRK1, ZNF512

### Function

This is a hematopoietic immune-cell activation module, with the strongest primary evidence for lymphocyte, leukocyte, and general cell activation (GO:BP lymphocyte activation; q_global = 0.00784)(GO:BP cell activation; q_global = 0.0142)(GO:BP leukocyte activation; q_global = 0.0169). It also supports lymphocyte proliferation and mononuclear-cell proliferation (GO:BP lymphocyte proliferation; q_global = 0.0425)(GO:BP mononuclear cell proliferation; q_global = 0.0473), together with natural-killer-cell mediated cytotoxicity (KEGG Natural killer cell mediated cytotoxicity - Homo sapiens (human); q_global = 0.0279). The genes span proximal immune signaling, integrin and adhesion control, actin remodeling, vesicle trafficking, and transcriptional or cell-cycle support. The co-abundance graph is organized around MEFV as a prominent hub, with many genes connected to it but relatively few direct high-confidence functional interactions among the peripheral genes. Thus, the module is best interpreted as a coordinated immune-cell state or cellular program rather than as a single obligatory protein complex.

**Cell composition.** HPA evidence strongly points to hematopoietic composition. Many genes are enhanced in lymphoid tissue or bone marrow, and the most frequent single-cell associations are with neutrophils, neutrophil progenitors, monocytes, and their progenitors. Additional associations with B cells, NK cells, macrophages, megakaryocytes, and other hematopoietic populations indicate that the module is not restricted to one mature lineage. Most genes have low immune-cell specificity, so the signal may reflect shared hematopoietic programs or variation in cell composition rather than a narrowly defined cell type. The module is not predominantly secreted: only a small subset is annotated as secreted, with KNG1 and SORL1 specifically described as secreted to blood. Protein detection in bone marrow is substantial but incomplete, while the cell-line comparison has no matching HPA tissue category. A plausible interpretation is that the shared signal partly reflects conserved immune or hematopoietic cell-state composition in the two sample groups.

**GO/KEGG enrichment**: 6 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP lymphocyte activation | 0.00784 | AP3B1, BTK, CORO1A, DOCK8, EPHB6, LCP1, PKN1, PRKCB, PTK2B, PTPN6, RAC2, TOP2B |
| GO:BP cell activation | 0.0142 | AP3B1, BTK, CORO1A, DOCK8, EPHB6, FERMT3, LCP1, PKN1, PRKCB, PTK2B, PTPN6, RAC2, TOP2B |
| GO:BP leukocyte activation | 0.0169 | AP3B1, BTK, CORO1A, DOCK8, EPHB6, LCP1, PKN1, PRKCB, PTK2B, PTPN6, RAC2, TOP2B |
| KEGG Natural killer cell mediated cytotoxicity - Homo sapiens (human) | 0.0279 | ICAM2, PRKCB, PTK2B, PTPN6, RAC2 |
| GO:BP lymphocyte proliferation | 0.0425 | BTK, CORO1A, DOCK8, EPHB6, PKN1, PTPN6, RAC2 |
| GO:BP mononuclear cell proliferation | 0.0473 | BTK, CORO1A, DOCK8, EPHB6, PKN1, PTPN6, RAC2 |

### STRING and hu.MAP

STRING supports a limited but biologically coherent interaction backbone. BTK connects with HCK, PRKCB, and PTPN6; HCK connects with PTK2B; and PTK2B connects with RAC2. These links support a signaling axis involving tyrosine phosphorylation, Src-family signaling, Rho-family control, and immune-cell activation. STRING functional results independently point to natural killer cytotoxicity (STRING KEGG Natural killer cell mediated cytotoxicity; within-query FDR = 0.0086), beta-two integrin signaling in neutrophils (STRING PMID (2020) beta2 Integrin Signaling Cascade in Neutrophils: More Than a Single Function.; within-query FDR = 0.0212), L-plastin-related T-cell motility and activation (STRING PMID (2013) The actin-bundling protein L-plastin supports T-cell motility and activation.; within-query FDR = 0.0212), blood and hematopoietic expression (STRING TISSUES Blood; within-query FDR = 0.0407)(STRING TISSUES Hematopoietic system; within-query FDR = 0.0407), and leukocyte proliferation (STRING Process Leukocyte proliferation; within-query FDR = 0.0416). These are supplementary confirmations and are not replacements for the globally corrected GO and KEGG results. hu.MAP provides partial complex support: PTPN6 and FERMT3 occur together in one complex (hu.MAP huMAP3_14295.1), KNG1 and LCP1 in another (hu.MAP huMAP3_10678.1), and PRKCB and AP1B1 in a third (hu.MAP huMAP3_12394.1). Because each complex contains only a small subset of the module, the module is not itself a single hu.MAP complex. The database evidence therefore supports several known molecular subsystems embedded within a broader co-abundance program.

**STRING interactions (score >= 0.7)**: 6 of 820 gene pairs: BTK–HCK (0.759); BTK–PRKCB (0.775); BTK–PTPN6 (0.953); HCK–PTK2B (0.93); MEFV–PKN1 (0.96); PTK2B–RAC2 (0.936)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Natural killer cell mediated cytotoxicity (FDR = 0.0086, 5 genes); PMID (2020) beta2 Integrin Signaling Cascade in Neutrophils: More Than a Single Function. (FDR = 0.0212, 8 genes); PMID (2013) The actin-bundling protein L-plastin supports T-cell motility and activation. (FDR = 0.0212, 7 genes); TISSUES Blood (FDR = 0.0407, 17 genes); TISSUES Hematopoietic system (FDR = 0.0407, 22 genes); Process Leukocyte proliferation (FDR = 0.0416, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14295.1 (PTPN6, FERMT3; 2/38); huMAP3_10678.1 (KNG1, LCP1; 2/71); huMAP3_12394.1 (PRKCB, AP1B1; 2/98)

### Novelty

The biological functions represented by this module are not new: immune activation, leukocyte adhesion, cytoskeletal remodeling, BTK signaling, RAC2 signaling, and neutrophil or lymphocyte biology are established. The module-level finding may still be novel as a conserved co-abundance pattern shared by bone marrow and a cell line, but the supplied evidence does not include a comparison against previously reported co-abundance modules or tissue-pair networks. The sparse STRING connectivity and partial hu.MAP overlap do not establish novelty, because database incompleteness and context-specific regulation can obscure real relationships. The most defensible conclusion is that the component biology is established, whereas novelty of the particular cross-tissue co-abundance architecture remains unresolved and requires external module-level comparison.

**Hypothesis.** Hypothesis: this module reflects a conserved hematopoietic activation state in which immune receptor and integrin inputs converge through BTK, HCK, PTPN6, PRKCB, PTK2B, and RAC2 to coordinate adhesion, actin remodeling, migration, cytotoxic or degranulation-related behavior, and proliferation. CORO1A and LCP1 could help translate signaling into cortical actin and cell motility, while FERMT3 could support integrin activation and adhesion. MEFV may act as a major co-abundance anchor linking this immune state to innate-inflammatory regulation. The hub-like structure may arise from a shared lineage or activation program rather than direct physical binding of all module members. This hypothesis should be tested by cell-composition adjustment, perturbation of the signaling genes, and validation across independent bone-marrow and cell-line datasets.

### Important genes

#### MEFV

- **Related proteins** (co-abundance neighbors): NSD1 (0.97), MTA2 (0.95), ATAD2B (0.95), IKZF2 (0.90), TOP2B (0.90), AP1B1 (0.89), TBC1D5 (0.89), PTPN6 (0.88), ICAM2 (0.88), DPP3 (0.87), PKN1 (0.87), RMI1 (0.86), FERMT3 (0.86), ZNF512 (0.85), RAC2 (0.84), RNASEH1 (0.84), DIS3 (0.84), PRKCB (0.84), ATP2A3 (0.83), SIPA1 (0.83), VRK1 (0.83), CORO1A (0.83), LCP1 (0.82), AP3B1 (0.82), BTK (0.82), CPPED1 (0.81), PTK2B (0.81), SORL1 (0.81), MTMR9 (0.81), SRR (0.80), RRS1 (0.80), SEPTIN6 (0.80); STRING partners: PKN1 (0.96)
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enhanced; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MEFV innate immunity regulator, pyrin. This gene encodes a protein, also known as pyrin or marenostrin, that is an important modulator of innate immunity. Mutations in this gene are associated with Mediterranean fever, a hereditary periodic fever syndrome. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: familial Mediterranean fever (0.809); autosomal recessive familial Mediterranean fever (0.805); sweet syndrome (0.789); autoinflammatory syndrome (0.547); hereditary disease (0.505)
- **Europe PMC papers**: 4906
- **Why important**: MEFV is the prominent network hub and connects the immune-associated portion of the module to genes involved in chromatin, trafficking, cytoskeletal, and signaling functions. HPA associates it with bone marrow, lymphoid tissue, and neutrophils. Its annotated role as pyrin, an innate-immunity regulator controlling inflammatory and interleukin-one-related processes, gives a plausible bridge between innate inflammatory state and the broader activation module. Its familial Mediterranean fever and other autoinflammatory disease associations are well established, with extensive literature.
- **Conclusion**: Established: MEFV is an innate-immune regulator and a disease-associated gene, and its network position makes it a useful module anchor. Hypothesis: MEFV may organize or mark the shared inflammatory cell state, but the co-abundance data do not demonstrate that it causally regulates the other module genes.

#### RAC2

- **Related proteins** (co-abundance neighbors): MEFV (0.84); STRING partners: PTK2B (0.936)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rac family small GTPase 2. This gene encodes a member of the Ras superfamily of small guanosine triphosphate (GTP)-metabolizing proteins. The encoded protein localizes to the plasma membrane, where it regulates diverse processes, such as secretion, phagocytosis, and cell polarization. Activity of this protein is also involved in the generation of reactive oxygen species. Mutations in this gene are associated with neutrophil…
- **Diseases (Open Targets)**: neutrophil immunodeficiency syndrome (0.717); immunodeficiency 73b with defective neutrophil chemotaxis and lymphopenia (0.692); immunodeficiency 73c with defective neutrophil chemotaxis and hypogammaglobulinemia (0.585); T-B+ severe combined immunodeficiency (0.526); T-B- severe combined immunodeficiency (0.526)
- **Europe PMC papers**: 5552
- **Why important**: RAC2 is present in every primary GO and KEGG evidence category listed for the module (GO:BP lymphocyte activation; q_global = 0.00784)(GO:BP cell activation; q_global = 0.0142)(GO:BP leukocyte activation; q_global = 0.0169)(KEGG Natural killer cell mediated cytotoxicity - Homo sapiens (human); q_global = 0.0279)(GO:BP lymphocyte proliferation; q_global = 0.0425)(GO:BP mononuclear cell proliferation; q_global = 0.0473) and in every STRING supplementary category (STRING KEGG Natural killer cell mediated cytotoxicity; within-query FDR = 0.0086)(STRING PMID (2020) beta2 Integrin Signaling Cascade in Neutrophils: More Than a Single Function.; within-query FDR = 0.0212)(STRING PMID (2013) The actin-bundling protein L-plastin supports T-cell motility and activation.; within-query FDR = 0.0212)(STRING TISSUES Blood; within-query FDR = 0.0407)(STRING TISSUES Hematopoietic system; within-query FDR = 0.0407)(STRING Process Leukocyte proliferation; within-query FDR = 0.0416). It connects in STRING to PTK2B and is annotated as a hematopoietic small GTPase controlling chemotaxis, actin organization, polarity, secretion, phagocytosis, and reactive oxygen species. Its strong association with bone marrow and lymphoid tissue and its immunodeficiency disease associations make it a central mechanistic candidate.
- **Conclusion**: Established: RAC2 is a core immune-cell signaling and cytoskeletal regulator whose dysfunction causes neutrophil and broader immunodeficiency phenotypes. Hypothesis: RAC2 may be a key downstream convergence point coupling the module to migration, adhesion, cytotoxicity, and oxidative responses.

#### PTPN6

- **Related proteins** (co-abundance neighbors): MEFV (0.88); STRING partners: BTK (0.953)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_14295.1
- **Function (MyGene.info)**: protein tyrosine phosphatase non-receptor type 6. The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. N-terminal part of this PTP contains two tandem Src homolog (SH2) domains, which act as protein phospho-tyrosine binding domains, and…
- **Diseases (Open Targets)**: diffuse large B-cell lymphoma (0.311); autoimmune disorder of central nervous system (0.280); melanoma (0.263); acute myeloid leukemia (0.211); hepatocellular carcinoma (0.208)
- **Europe PMC papers**: 3271
- **Why important**: PTPN6 is represented in all primary enrichment categories (GO:BP lymphocyte activation; q_global = 0.00784)(GO:BP cell activation; q_global = 0.0142)(GO:BP leukocyte activation; q_global = 0.0169)(KEGG Natural killer cell mediated cytotoxicity - Homo sapiens (human); q_global = 0.0279)(GO:BP lymphocyte proliferation; q_global = 0.0425)(GO:BP mononuclear cell proliferation; q_global = 0.0473) and all STRING supplementary categories (STRING KEGG Natural killer cell mediated cytotoxicity; within-query FDR = 0.0086)(STRING PMID (2020) beta2 Integrin Signaling Cascade in Neutrophils: More Than a Single Function.; within-query FDR = 0.0212)(STRING TISSUES Blood; within-query FDR = 0.0407)(STRING TISSUES Hematopoietic system; within-query FDR = 0.0407)(STRING Process Leukocyte proliferation; within-query FDR = 0.0416). It has a high-confidence STRING relationship with BTK and participates with FERMT3 in a hu.MAP complex (hu.MAP huMAP3_14295.1). HPA places it in bone marrow and lymphoid tissue and in neutrophils, monocytes, and related progenitors. Its SH2-containing tyrosine phosphatase function makes it a credible regulator of immune receptor signal strength, while its hematologic and immune disease associations add clinical relevance.
- **Conclusion**: Established: PTPN6 is a hematopoietic signaling phosphatase with a well-supported role in regulating immune activation. Hypothesis: its co-abundance with BTK, RAC2, and integrin-related genes may indicate coordinated tuning of activation thresholds in the shared cell state.

#### BTK

- **Related proteins** (co-abundance neighbors): MEFV (0.82); STRING partners: HCK (0.759), PRKCB (0.775), PTPN6 (0.953)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Bruton tyrosine kinase. The protein encoded by this gene plays a crucial role in B-cell development. Mutations in this gene cause X-linked agammaglobulinemia type 1, which is an immunodeficiency characterized by the failure to produce mature B lymphocytes, and associated with a failure of Ig heavy chain rearrangement. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by R…
- **Diseases (Open Targets)**: Bruton-type agammaglobulinemia (0.857); isolated growth hormone deficiency type III (0.733); B-cell chronic lymphocytic leukemia (0.719); isolated congenital growth hormone deficiency (0.718); mantle cell lymphoma (0.693)
- **Europe PMC papers**: 14674
- **Why important**: BTK is included in the primary activation and proliferation terms (GO:BP lymphocyte activation; q_global = 0.00784)(GO:BP cell activation; q_global = 0.0142)(GO:BP leukocyte activation; q_global = 0.0169)(GO:BP lymphocyte proliferation; q_global = 0.0425)(GO:BP mononuclear cell proliferation; q_global = 0.0473) and in several STRING immune categories (STRING PMID (2020) beta2 Integrin Signaling Cascade in Neutrophils: More Than a Single Function.; within-query FDR = 0.0212)(STRING TISSUES Blood; within-query FDR = 0.0407)(STRING TISSUES Hematopoietic system; within-query FDR = 0.0407)(STRING Process Leukocyte proliferation; within-query FDR = 0.0416). It has known STRING links to HCK, PRKCB, and PTPN6, forming the clearest signaling subnetwork in the module. HPA associates it with bone marrow, lymphoid tissue, B cells, and basophils. Its established role in B-cell development and the disease association with Bruton-type agammaglobulinemia make it a particularly informative marker of immune signaling competence.
- **Conclusion**: Established: BTK is a central B-cell developmental and receptor-signaling kinase, and its module relationships are supported by known interactions. Hypothesis: BTK may contribute to the shared module through a mixture of B-lineage signaling and broader myeloid or basophil-associated activation programs.

#### CORO1A

- **Related proteins** (co-abundance neighbors): MEFV (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coronin 1A. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: severe combined immunodeficiency due to CORO1A deficiency (0.763); severe combined immunodeficiency (0.532); neurodegenerative disease (0.492); combined immunodeficiency (0.463); Omenn syndrome (0.462)
- **Europe PMC papers**: 1857
- **Why important**: CORO1A occurs in the primary lymphocyte, leukocyte, activation, and proliferation terms (GO:BP lymphocyte activation; q_global = 0.00784)(GO:BP cell activation; q_global = 0.0142)(GO:BP leukocyte activation; q_global = 0.0169)(GO:BP lymphocyte proliferation; q_global = 0.0425)(GO:BP mononuclear cell proliferation; q_global = 0.0473) and in the STRING motility, blood, hematopoietic, and leukocyte categories (STRING PMID (2020) beta2 Integrin Signaling Cascade in Neutrophils: More Than a Single Function.; within-query FDR = 0.0212)(STRING PMID (2013) The actin-bundling protein L-plastin supports T-cell motility and activation.; within-query FDR = 0.0212)(STRING TISSUES Blood; within-query FDR = 0.0407)(STRING TISSUES Hematopoietic system; within-query FDR = 0.0407)(STRING Process Leukocyte proliferation; within-query FDR = 0.0416). HPA places it in bone marrow and lymphoid tissue and across B-cell, dendritic, innate lymphoid, and macrophage populations. Its annotated functions in immunological synapse formation, phagolysosome assembly, phagocytosis, migration, and actin organization connect the signaling part of the module to cellular behavior. CORO1A deficiency is associated with severe combined immunodeficiency, providing strong functional and disease support.
- **Conclusion**: Established: CORO1A is a broad leukocyte cytoskeletal and immune-trafficking regulator. Hypothesis: it may help explain why the module captures both lymphocyte activation and myeloid or neutrophil-associated signatures rather than a single lineage-specific program.

## Module 8

**Tissue pair**: bone_marrow and cell line  
**Genes (18)**: AP1S1, CAMKMT, CNIH1, COX14, GGT1, IL2RG, ITIH3, LGALS3BP, NMNAT1, PLEKHD1, RIN3, RNF115, SLC39A11, KNSTRN, WRAP53, TNRC6A, TRMT61A, TTYH3

### Function

No GO or KEGG term passed global correction, and STRING supplied no functional enrichment; therefore the module does not support a statistically established single pathway or biological process. The gene composition nevertheless suggests a mixed module involving immune and hematopoietic signaling, intracellular trafficking and endocytosis, RNA regulation, mitochondrial function, ion transport, and secreted or extracellular-matrix-associated biology. The network is sparse and appears to connect several functional neighborhoods rather than define one canonical pathway. The strongest biological themes are an IL2RG-associated immune signaling branch, an AP1S1-associated vesicle-trafficking branch, and a set of tissue- or cell-type-associated genes that may reflect sample composition or shared cellular states. The absence of globally significant enrichment does not invalidate the co-abundance module; it limits the strength of pathway-level interpretation.

**Cell composition.** This is not predominantly a plasma or secreted-protein module. ITIH3 and LGALS3BP are secreted to blood, while GGT1 has intracellular and membrane localization, so extracellular or circulating contributions are possible but do not define most of the module. HPA indicates broadly distributed expression for many genes, with several genes enhanced in brain, liver, intestine, kidney, or other epithelial tissues. Blood-cell specificity is mostly low, although immune-cell enhancement or enrichment is present for several genes, including RIN3, TTYH3, WRAP53, RNF115, and PLEKHD1. RIN3 is particularly compatible with a myeloid or antigen-presenting-cell contribution, and IL2RG is enhanced in several lymphoid and hematopoietic cell types. Bone-marrow protein detection is present for a subset of genes, including CNIH1, IL2RG, WRAP53, NMNAT1, KNSTRN, AP1S1, RNF115, RIN3, and TNRC6A, whereas protein detection in the cell-line context is unavailable. Overall, the shared signal may reflect a mixture of broadly expressed intracellular programs with contributions from hematopoietic or immune cells, rather than a blood-specific secreted-protein program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING reports no high-confidence interactions among the module genes and no supplementary STRING enrichment. Thus, the co-abundance edges are not corroborated by the supplied STRING protein-interaction evidence and should not be interpreted as established physical interactions. hu.MAP provides a limited connection: AP1S1 and TNRC6A occur together in complexes C1, C2, and C3. However, these complexes contain many proteins and only those two module genes are represented, so the result supports possible participation in broadly defined trafficking, vesicle, or regulatory assemblies but does not establish a direct AP1S1–TNRC6A interaction or a unified complex for the module. The absence of STRING or hu.MAP support for the remaining genes makes the network primarily a co-abundance observation.

**STRING interactions (score >= 0.7)**: 0 of 153 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10762.1 (AP1S1, TNRC6A; 2/62); huMAP3_12918.1 (AP1S1, TNRC6A; 2/62); huMAP3_12394.1 (AP1S1, TNRC6A; 2/98)

### Novelty

The exact cross-tissue co-abundance pattern may be a new observation because the module is not reproduced as a coherent high-confidence interaction network in STRING and has only limited, partial representation in hu.MAP. However, this does not establish a new biological mechanism. Most individual gene functions are already well characterized, and the module combines several known processes rather than revealing a previously recognized complex. A defensible conclusion is that the module-level association is potentially novel and hypothesis-generating, while the underlying gene functions and the AP1S1-associated complex context are established. Independent replication, cell-type deconvolution, perturbation, and validation in additional bone-marrow and cell-line datasets would be needed to claim biological novelty.

**Hypothesis.** Hypothesis: the module reflects a shared cellular state in which immune or hematopoietic signaling is coordinated with membrane trafficking, receptor internalization, RNA regulation, and cellular maintenance. IL2RG may mark cytokine-receptor signaling in hematopoietic cells; RIN3 and AP1S1 may connect receptor trafficking and endocytic control; SLC39A11 may contribute metal-ion handling; and WRAP53, NMNAT1, and COX14 may represent demands for RNA, nucleotide, telomere, or mitochondrial maintenance. Secreted ITIH3 and LGALS3BP could reflect extracellular or sample-composition effects rather than a direct intracellular pathway. This hypothesis predicts that the module will vary with the abundance or activation state of particular immune and stromal populations and that its genes will not necessarily form a single physical complex.

### Important genes

#### IL2RG

- **Related proteins** (co-abundance neighbors): CAMKMT (0.93), CNIH1 (0.88), AP1S1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: interleukin 2 receptor subunit gamma. The protein encoded by this gene is an important signaling component of many interleukin receptors, including those of interleukin -2, -4, -7 and -21, and is thus referred to as the common gamma chain. Mutations in this gene cause X-linked severe combined immunodeficiency (XSCID), as well as X-linked combined immunodeficiency (XCID), a less severe immunodeficiency disorder. [provided by RefSeq, Ma…
- **Diseases (Open Targets)**: T-B+ severe combined immunodeficiency due to gamma chain deficiency (0.848); combined immunodeficiency, X-linked (0.740); Omenn syndrome (0.561); primary cutaneous T-cell non-Hodgkin lymphoma (0.543); renal cell carcinoma (0.538)
- **Europe PMC papers**: 10741
- **Why important**: IL2RG is a central connector in the module's immune-signaling branch, linking to CAMKMT, CNIH1, and AP1S1. It encodes the common gamma chain used by several interleukin receptors and is associated with cytokine-mediated JAK-STAT signaling, leukocyte homeostasis, and severe combined immunodeficiency. HPA supports relevance to lymphoid and hematopoietic cell types and detects the protein in bone marrow. Its extensive disease and literature evidence makes it the strongest established immune anchor.
- **Conclusion**: Established evidence supports IL2RG as a marker and functional component of cytokine-receptor signaling in hematopoietic cells. The module does not establish that IL2RG physically interacts with the neighboring genes or that the whole module is an IL2RG pathway. A contribution from immune-cell composition or cytokine-state variation is a plausible hypothesis.

#### RIN3

- **Related proteins** (co-abundance neighbors): CNIH1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Ras and Rab interactor 3. Summary: This protein encoded by this gene is a member of the RIN family of Ras interaction-interference proteins, which are binding partners to the RAB5 small GTPases. The protein functions as a guanine nucleotide exchange for RAB5B and RAB31. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.519); Alzheimer disease (0.487); asthma (0.455); dementia (0.437); primary biliary cholangitis (0.373)
- **Europe PMC papers**: 835
- **Why important**: RIN3 is tissue enhanced in bone marrow and is enriched across multiple myeloid-associated cell populations in HPA, including monocytes, dendritic cells, macrophages, and related immune populations. It is a Rab-interacting guanine-nucleotide exchange factor involved in endocytosis, vesicle-mediated transport, receptor internalization, and vesicle-size regulation. Its connection to CNIH1 places it in a module branch that may link trafficking with immune-cell biology.
- **Conclusion**: Established evidence supports RIN3 as a bone-marrow- and myeloid-associated regulator of Rab-dependent endocytic biology. The co-abundance pattern is consistent with a myeloid contribution, but it does not prove that RIN3 drives the module or that its relationship with CNIH1 is a direct molecular interaction.

#### AP1S1

- **Related proteins** (co-abundance neighbors): IL2RG (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_10762.1, huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: adaptor related protein complex 1 subunit sigma 1. The protein encoded by this gene is part of the clathrin coat assembly complex which links clathrin to receptors in coated vesicles. These vesicles are involved in endocytosis and Golgi processing. This protein, as well as beta-prime-adaptin, gamma-adaptin, and the medium (mu) chain AP47, form the AP-1 assembly protein complex located at the Golgi vesicle. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: MEDNIK syndrome (0.762); HIV infectious disease (0.504); Abnormality of the skeletal system (0.359); neurodegenerative disease (0.344); hereditary disease (0.336)
- **Europe PMC papers**: 462
- **Why important**: AP1S1 is the module member most directly tied to a recognized vesicle-coat machinery. It participates in the AP one clathrin adaptor complex involved in Golgi trafficking, receptor-mediated endocytosis, protein transport, and platelet dense-granule organization. It connects to IL2RG in the network and is the only module gene pair represented with TNRC6A across the supplied hu.MAP complexes C1, C2, and C3. Its disease association with MEDNIK syndrome further supports functional importance.
- **Conclusion**: Established evidence supports AP1S1 as a vesicle-trafficking and receptor-sorting component, with partial complex-level support from hu.MAP. The module may capture coordinated trafficking and signaling, but the available data do not show that all module genes belong to the AP one complex or that AP1S1 explains the entire co-abundance pattern.

#### WRAP53

- **Related proteins** (co-abundance neighbors): ITIH3 (0.83), TNRC6A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nuclear bodies; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat containing antisense to TP53. This gene encodes an essential component of the telomerase holoenzyme complex, a ribonucleoprotein complex required for telomere synthesis. This protein is enriched in Cajal bodies, nuclear sites of RNP processing that are important for telomerase function. It interacts with dyskerin, TERT and TERC, other components of active telomerase, and with small Cajal body RNAs (scaRNAs), which are involved…
- **Diseases (Open Targets)**: dyskeratosis congenita (0.778); neurodegenerative disease (0.550); hereditary neoplastic syndrome (0.466); acute myeloid leukemia with minimal differentiation (0.462); Alzheimer disease (0.444)
- **Europe PMC papers**: 847
- **Why important**: WRAP53 is a highly informative nuclear-maintenance gene connected to ITIH3 and TNRC6A. It is an established component of telomerase and Cajal-body biology and contributes to telomere maintenance, RNA processing, and DNA-repair regulation. HPA detects it in bone marrow and shows enhancement in several ciliated cell types and basophils. Its associations with dyskeratosis congenita and neoplastic or neurodegenerative disease make it relevant to cellular longevity and genome maintenance.
- **Conclusion**: Established evidence supports WRAP53 as a telomerase, Cajal-body, and RNA-processing factor. Its inclusion suggests that the module may capture a broader cell-maintenance state rather than a dedicated trafficking or immune pathway. Any mechanistic connection between WRAP53 and the membrane or secreted genes remains hypothetical.

#### ITIH3

- **Related proteins** (co-abundance neighbors): TRMT61A (0.88), NMNAT1 (0.86), COX14 (0.86), KNSTRN (0.85), WRAP53 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 3. This gene encodes the heavy chain subunit of the pre-alpha-trypsin inhibitor complex. This complex may stabilize the extracellular matrix through its ability to bind hyaluronic acid. Polymorphisms of this gene may be associated with increased risk for schizophrenia and major depressive disorder. This gene is present in an inter-alpha-trypsin inhibitor family gene cluster on chromosome 3. [provided…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.527); schizophrenia (0.439); major depressive disorder (0.422); bipolar disorder (0.411); autism spectrum disorder (0.386)
- **Europe PMC papers**: 1167
- **Why important**: ITIH3 is the most connected node in the supplied module and links several otherwise diverse genes, including TRMT61A, NMNAT1, COX14, KNSTRN, and WRAP53. It encodes a heavy-chain component of the inter-alpha-trypsin inhibitor family, can bind hyaluronan, and may stabilize extracellular matrix. HPA identifies liver and hepatocyte enrichment and secretion to blood, while disease resources associate it with skeletal and neuropsychiatric phenotypes.
- **Conclusion**: Established evidence supports ITIH3 as a secreted extracellular-matrix-associated protein with liver enrichment. Its network position makes it important for interpreting the module, but the absence of STRING and hu.MAP support argues against treating it as a proven physical hub. A plausible explanation is that ITIH3 reflects circulating or tissue-composition effects that become correlated with intracellular genes in the shared datasets.

## Module 9

**Tissue pair**: bone_marrow and cell line  
**Genes (5)**: CIBAR2, GSKIP, MOGS, RAB27A, SMIM7

### Function

No GO or KEGG term passed global correction, so the module has no statistically established pathway-level annotation from the enrichment analysis. Gene-level evidence instead points to intracellular membrane and vesicle biology: GSKIP is associated with Wnt regulation and kinase regulation; RAB27A with vesicle transport, exocytosis, protein secretion and antigen processing; MOGS with ER protein folding and N-linked glycosylation; and CIBAR2 with cilium assembly. The co-abundance pattern is therefore most consistent with a possible membrane-trafficking, protein-processing and cell-structure program, but this interpretation remains provisional because the genes do not form a coherent known pathway in the enrichment results.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of the genes is annotated as secreted. It is also not a clearly blood-cell-specific module. Most genes have low immune-cell specificity, CIBAR2 is not detected in immune cells, and only RAB27A is immune-cell enhanced, particularly in basophils. HPA shows several genes with broad or low tissue specificity, while others are enhanced in ciliated cells, spermatid-related populations or other specialized cell types. Protein detection in bone marrow is reported for most of the genes, but the cell-line comparison has no matching HPA tissue. Thus, the shared module may partly reflect intracellular programs or shared cell-state composition rather than a bone-marrow-specific blood function.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and no hu.MAP complex contains multiple module members. Consequently, the co-abundance edges are not supported here by established physical interaction evidence. GSKIP is the central statistical connector, linking CIBAR2, SMIM7, RAB27A and MOGS, whereas the other genes are peripheral in this subgraph. Known gene functions still provide plausible biological links through vesicles, membranes, ER processing, cilia and signaling, but these links should not be described as experimentally established interactions within this module.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially interesting co-abundance association because it brings together genes spanning Wnt regulation, vesicle transport, cilium biology, membrane proteins and ER glycosylation. However, it cannot be claimed as a new biological module solely because STRING and hu.MAP provide no support: absence from those resources may reflect incomplete coverage, tissue or cell-state specificity, or a statistical rather than physical relationship. The absence of globally significant GO or KEGG enrichment and the lack of STRING or hu.MAP support mean that the module is best regarded as a candidate, hypothesis-generating pattern rather than a validated novel complex or pathway.

**Hypothesis.** Hypothesis: in the shared bone-marrow and cell-line context, GSKIP may organize a cell-state program connecting Wnt-related signaling with membrane and vesicle behavior, while RAB27A contributes regulated trafficking, MOGS supports ER glycoprotein processing, and CIBAR2 and SMIM7 mark specialized membrane or ciliary states. Co-abundance of these genes could therefore arise from coordinated remodeling of intracellular trafficking and protein-processing capacity, possibly influenced by the presence of specialized or differentiating cell states. This hypothesis requires validation with independent datasets, perturbation experiments and protein-level interaction or localization assays.

### Important genes

#### GSKIP

- **Related proteins** (co-abundance neighbors): CIBAR2 (0.97), SMIM7 (0.91), RAB27A (0.81), MOGS (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GSK3B interacting protein. This gene encodes a protein that is involved as a negative regulator of GSK3-beta in the Wnt signaling pathway. The encoded protein may play a role in the retinoic acid signaling pathway by regulating the functional interactions between GSK3-beta, beta-catenin and cyclin D1, and it regulates the beta-catenin/N-cadherin pool. The encoded protein contains a GSK3-beta interacting domain (GID) in its …
- **Diseases (Open Targets)**: Sjogren syndrome (0.101); neurodegenerative disease (0.070); surfactant metabolism dysfunction, pulmonary, 1 (0.066); hereditary pulmonary alveolar proteinosis (0.064); isolated Pierre-Robin syndrome (0.056)
- **Europe PMC papers**: 409
- **Why important**: GSKIP is the network hub, connected to every other module member, making it the strongest candidate for explaining the module's internal organization. It is annotated as a GSK3B-interacting protein involved in Wnt regulation, beta-catenin and N-cadherin regulation, kinase regulation and stress-linked apoptotic signaling. It also has substantial literature coverage and multiple disease associations, giving it a stronger evidence base than the less characterized genes.
- **Conclusion**: Established evidence supports GSKIP as a signaling regulator and the central co-abundance node. It is a plausible upstream organizer of the module, but the module does not establish direct physical binding or prove that GSKIP regulates the other four genes. Its proposed coordinating role is therefore a hypothesis.

#### RAB27A

- **Related proteins** (co-abundance neighbors): GSKIP (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mid piece, Principal piece; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB27A, member RAS oncogene family. The protein encoded by this gene belongs to the small GTPase superfamily, Rab family. The protein is membrane-bound and may be involved in protein transport and small GTPase mediated signal transduction. Mutations in this gene are associated with Griscelli syndrome type 2. Alternative splicing occurs at this locus and four transcript variants encoding the same protein have been identified. [provid…
- **Diseases (Open Targets)**: Griscelli syndrome type 2 (0.812); Griscelli syndrome (0.749); autoinflammatory syndrome (0.499); hereditary disease (0.450); acrocephalopolydactyly (0.370)
- **Europe PMC papers**: 5437
- **Why important**: RAB27A is a vesicle-associated small GTPase with established roles in protein transport, exocytosis, secretion, antigen processing and organelle transport. It is linked to Griscelli syndrome and related immune disease, has extensive literature coverage, and is the module member with immune-cell enhancement in the HPA summary. Its link to the GSKIP hub makes it especially informative for interpreting the module as a trafficking-related pattern.
- **Conclusion**: Established evidence supports RAB27A as a major regulator of membrane trafficking and secretory vesicles, with disease relevance. Its co-abundance with GSKIP may indicate coordination between signaling and trafficking, but that relationship is not confirmed as a direct molecular interaction in this module.

#### MOGS

- **Related proteins** (co-abundance neighbors): GSKIP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosyl-oligosaccharide glucosidase. This gene encodes the first enzyme in the N-linked oligosaccharide processing pathway. The enzyme cleaves the distal alpha-1,2-linked glucose residue from the Glc(3)-Man(9)-GlcNAc(2) oligosaccharide precursor. This protein is located in the lumen of the endoplasmic reticulum. Defects in this gene are a cause of type IIb congenital disorder of glycosylation (CDGIIb). Two transcript variants encodin…
- **Diseases (Open Targets)**: MOGS-congenital disorder of glycosylation (0.818); congenital disorder of glycosylation (0.374); congenital disorder of glycosylation type II (0.370); severe acute respiratory syndrome (0.370); SRD5A3-congenital disorder of glycosylation (0.370)
- **Europe PMC papers**: 987
- **Why important**: MOGS encodes an ER enzyme that initiates N-linked oligosaccharide processing and is involved in glycoprotein folding and maturation. It has a well-established connection to congenital disorders of glycosylation and substantial literature coverage. Its connection to the GSKIP hub adds an ER protein-processing component to the otherwise trafficking- and signaling-oriented interpretation.
- **Conclusion**: Established evidence supports MOGS as an ER glycoprotein-processing enzyme with disease relevance. Its presence may indicate coordinated demand for membrane or secretory protein maturation, but a specific functional connection to GSKIP or RAB27A remains hypothetical.

#### CIBAR2

- **Related proteins** (co-abundance neighbors): GSKIP (0.97); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CBY1 interacting BAR domain containing 2. Predicted to be involved in cilium assembly. Predicted to be located in centriole and cytoplasm. Predicted to be active in ciliary basal body and ciliary transition zone. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: gastric ulcer (0.320); hemorrhage (0.320); malunion fracture (0.291); Abnormality of the skeletal system (0.269); dermatitis (0.252)
- **Europe PMC papers**: 25
- **Why important**: CIBAR2 is the module member annotated as a predicted cilium-assembly factor and is connected to the GSKIP hub. HPA describes enhancement in choroid plexus, fallopian tube and several ciliated cell populations, while it is not detected in immune cells. Its comparatively limited literature coverage makes it a potentially informative but less established component of the pattern.
- **Conclusion**: Established evidence is currently limited to predicted involvement in cilium assembly and cell-type expression associations. CIBAR2 may represent a ciliary or specialized membrane-state component of the module, but its role in the shared bone-marrow and cell-line pattern is a hypothesis requiring experimental validation.

#### SMIM7

- **Related proteins** (co-abundance neighbors): GSKIP (0.91); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: small integral membrane protein 7. Predicted to be integral component of membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: preeclampsia (0.093); hypothyroidism (0.036); hepatocellular carcinoma (0.013); infection (0.002); pancreatic ductal adenocarcinoma (0.002)
- **Europe PMC papers**: 63
- **Why important**: SMIM7 is a predicted small integral membrane protein with Golgi localization and is connected to GSKIP. HPA indicates low tissue specificity but enhancement in a spermatocyte population, and the gene has limited literature compared with RAB27A, MOGS and GSKIP. Its inclusion may therefore help identify a membrane-state signal that is not captured by established pathway databases.
- **Conclusion**: Established evidence supports SMIM7 mainly as a predicted membrane protein with Golgi localization. Its role in this module is uncertain; it could be a marker of membrane or differentiation state rather than an active regulator. A mechanistic contribution to the proposed trafficking program remains hypothetical.

## Module 10

**Tissue pair**: bone_marrow and cell line  
**Genes (6)**: CLPB, GALK2, GNE, NRGN, VWA8, ZBBX

### Function

The module does not support a single statistically established functional annotation: no GO or KEGG term passed global correction, and no STRING functional-enrichment result was reported. The network is organized around ZBBX, which connects to GALK2, CLPB, GNE, and VWA8, while NRGN connects to GNE. The gene annotations suggest a mixed biology involving sialic-acid and carbohydrate metabolism through GNE and GALK2, mitochondrial protein quality control and innate immune biology through CLPB, predicted cilium-related activity through ZBBX, and neuronal signaling through NRGN. Because these signals are heterogeneous and the module is small, the most defensible interpretation is a co-abundance pattern rather than a validated common pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins; all genes are annotated as non-secreted. It is also not strongly blood-cell specific: most genes have low immune-cell specificity, one is immune-cell enhanced in myeloid dendritic cells, and one is not detected in immune cells. HPA tissue and single-cell evidence is heterogeneous, including testis and late spermatids, choroid plexus epithelial cells, intestine, liver, salivary gland, brain, hepatocytes, goblet cells, epicardial cells, and platelets. Four proteins are detected in bone marrow, whereas two are not detected there. These observations argue against interpreting the shared module simply as a plasma-protein signal or a uniform blood-cell program. The pattern may instead reflect shared cellular composition, broad cellular stress or metabolic variation, or coordinated abundance of genes expressed in distinct cell populations.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no STRING functional-enrichment result was reported. No hu.MAP complex contained at least two module members. Thus, the co-abundance edges are not corroborated by the supplied physical-interaction or complex resources. This does not invalidate the module: co-abundance can arise from shared regulation, cell composition, organelle state, or indirect biology rather than direct binding. However, the absence of corroborating interactions makes a stable protein complex or direct molecular machine an unsupported interpretation.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported co-abundance pattern, but novelty cannot be established from this fact sheet alone. The lack of STRING and hu.MAP support is evidence that the observed relationships are not captured in those resources, not proof that they are biologically new. The heterogeneous tissue and cell-type annotations, absence of globally significant GO or KEGG enrichment, and lack of STRING enrichment make a novel shared pathway less likely than a context-dependent co-abundance signal. A proper novelty claim would require comparison with published co-expression modules, independent cohorts, and replication in additional bone-marrow and cell-line datasets.

**Hypothesis.** Hypothesis: the module reflects a context-dependent transcriptional or compositional program linking cellular carbohydrate and sialic-acid handling with mitochondrial proteostasis and specialized cell-state markers. GNE and GALK2 could represent metabolic state, CLPB could represent mitochondrial protein-quality or innate-stress state, and ZBBX could act as the central abundance-correlated marker connecting these signals to cilium-associated or specialized epithelial and germ-cell programs. NRGN may capture a neuronal or platelet-related component rather than participate in a common biochemical pathway. This hypothesis is exploratory and should be tested by replication, cell-composition adjustment, perturbation of GNE or CLPB, and measurement of sialylation, mitochondrial stress, and relevant cell-state markers.

### Important genes

#### ZBBX

- **Related proteins** (co-abundance neighbors): GALK2 (0.94), CLPB (0.89), GNE (0.85), VWA8 (0.84); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger B-box domain containing. Predicted to enable zinc ion binding activity. Predicted to be involved in cilium movement. Predicted to be active in motile cilium. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: alcohol drinking (0.362); carotid artery disorder (0.289); diabetes mellitus (0.281); Back pain (0.280); musculoskeletal system disorder (0.258)
- **Europe PMC papers**: 95
- **Why important**: ZBBX is the network hub, connecting to GALK2, CLPB, GNE, and VWA8 with the strongest overall connectivity in the module. Its HPA profile is enriched across specialized tissues and cell types, including choroid plexus epithelial cells and spermatid-related populations, and its supplied annotation predicts zinc binding and involvement in motile cilia. It has comparatively limited literature and no reported STRING or hu.MAP support, making it important both as the structural center of the module and as a candidate marker requiring validation.
- **Conclusion**: Established evidence supports ZBBX as the module's central co-abundance gene and as a predicted cilium-associated protein with specialized expression. It is not established that ZBBX physically interacts with the neighboring proteins or controls the module. Its regulatory or mechanistic role remains a hypothesis.

#### GNE

- **Related proteins** (co-abundance neighbors): ZBBX (0.85), NRGN (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glucosamine (UDP-N-acetyl)-2-epimerase/N-acetylmannosamine kinase. The protein encoded by this gene is a bifunctional enzyme that initiates and regulates the biosynthesis of N-acetylneuraminic acid (NeuAc), a precursor of sialic acids. It is a rate-limiting enzyme in the sialic acid biosynthetic pathway. Sialic acid modification of cell surface molecules is crucial for their function in many biologic processes, including cell adhesion and signal transduction. Dif…
- **Diseases (Open Targets)**: GNE myopathy (0.860); sialuria (0.819); inclusion body myositis (0.728); thrombocytopenia 12 with or without myopathy (0.654); distal myopathy (0.470)
- **Europe PMC papers**: 3222
- **Why important**: GNE is directly connected to the hub ZBBX and to NRGN, and it has a well-defined enzymatic role initiating and regulating sialic-acid biosynthesis. Its HPA profile points to intestine, liver, and salivary gland expression, with detection in bone marrow. It has disease associations involving GNE myopathy, sialuria, and related myopathies, together with substantial literature, so it provides the strongest established biochemical anchor for the module.
- **Conclusion**: Established evidence supports GNE as a rate-limiting sialic-acid biosynthetic enzyme with disease relevance. It is plausible that its abundance reports glycan or metabolic state in the shared module, but the fact sheet does not establish that GNE links mechanistically to ZBBX or NRGN.

#### CLPB

- **Related proteins** (co-abundance neighbors): ZBBX (0.89); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ClpB family mitochondrial disaggregase. This gene belongs to the ATP-ases associated with diverse cellular activities (AAA+) superfamily. Members of this superfamily form ring-shaped homo-hexamers and have highly conserved ATPase domains that are involved in various processes including DNA replication, protein degradation and reactivation of misfolded proteins. All members of this family hydrolyze ATP through their AAA+ domains and use …
- **Diseases (Open Targets)**: 3-methylglutaconic aciduria with cataracts, neurologic involvement, and neutropenia (0.840); neutropenia, severe congenital, 9, autosomal dominant (0.788); 3-methylglutaconic aciduria, type VIIA (0.691); 3-methylglutaconic aciduria (0.665); hereditary disease (0.495)
- **Europe PMC papers**: 4069
- **Why important**: CLPB is connected to the hub and encodes a mitochondrial AAA-plus disaggregase involved in protein quality control. Its supplied annotations include granulocyte differentiation, heat response, RIG-I signaling, and antiviral innate immunity. HPA reports testis and late-spermatid enrichment, immune-cell enhancement in myeloid dendritic cells, and detection in bone marrow. Its disease associations include neutropenia and syndromes involving mitochondrial dysfunction, while its literature base is substantial.
- **Conclusion**: Established evidence supports CLPB as a mitochondrial proteostasis factor with hematologic and innate-immune relevance. Its co-abundance with the other module genes may reflect cellular stress or cell-state composition, but a shared CLPB-centered pathway is not demonstrated by the available interaction resources.

#### GALK2

- **Related proteins** (co-abundance neighbors): ZBBX (0.94); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galactokinase 2. This gene encodes a highly efficient N-acetylgalactosamine (GalNAc) kinase, which has galactokinase activity when galactose is present at high concentrations. The encoded protein is a member of the GHMP kinase family. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2017].
- **Diseases (Open Targets)**: neurodegenerative disease (0.352); nontoxic goiter (0.221); gastroesophageal reflux disease (0.132); Parkinson disease (0.124); Alzheimer disease (0.123)
- **Europe PMC papers**: 4251
- **Why important**: GALK2 is directly connected to the hub and encodes a kinase involved in galactose and N-acetylgalactosamine metabolism. Its supplied GO annotations concern carbohydrate metabolism and phosphorylation, and HPA describes broad tissue and immune-cell specificity with detection in bone marrow. It has a comparatively large literature base and disease links including neurodegenerative disease and Parkinson disease, making it a useful metabolic complement to GNE.
- **Conclusion**: Established evidence supports GALK2 as a carbohydrate kinase. Its pairing with GNE is consistent with a possible glycan or carbohydrate-metabolic state, but the module does not provide globally significant enrichment or direct interaction evidence for that interpretation.

#### NRGN

- **Related proteins** (co-abundance neighbors): GNE (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neurogranin. Neurogranin (NRGN) is the human homolog of the neuron-specific rat RC3/neurogranin gene. This gene encodes a postsynaptic protein kinase substrate that binds calmodulin in the absence of calcium. The NRGN gene contains four exons and three introns. The exons 1 and 2 encode the protein and exons 3 and 4 contain untranslated sequences. It is suggested that the NRGN is a direct target for thyroid hor…
- **Diseases (Open Targets)**: schizophrenia (0.472); neurodegenerative disease (0.439); autism spectrum disorder (0.350); attention deficit-hyperactivity disorder (0.345); major depressive disorder (0.297)
- **Europe PMC papers**: 1923
- **Why important**: NRGN is connected to GNE and encodes a calmodulin-binding postsynaptic kinase substrate associated with signal transduction, nervous-system development, learning, and synaptic plasticity. HPA reports brain enrichment and cell-type enrichment in platelets, while the supplied disease associations include schizophrenia, autism-spectrum disorder, attention-deficit or hyperactivity disorder, and neurodegenerative disease. Its substantial literature makes it an informative indicator of a neuronal or platelet-related component, despite its peripheral network position.
- **Conclusion**: Established evidence supports NRGN as a neuronal signaling protein and a marker associated with brain and platelet biology. Its presence does not establish that neuronal signaling is the module function; it may instead reflect sample composition or an indirect abundance relationship with GNE.
