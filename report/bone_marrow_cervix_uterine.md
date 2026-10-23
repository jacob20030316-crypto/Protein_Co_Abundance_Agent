# Conserved co-abundance modules: bone_marrow and cervix_uterine

## Module 0

**Tissue pair**: bone_marrow and cervix_uterine  
**Genes (45)**: PPP2R1B, ANXA1, B4GALT1, BOLA2, BPNT1, CASP3, CHMP1A, C5, CTDP1, CYBB, DSC2, EXOC5, FKBP4, GLIPR2, GLRX, H1-3, HABP2, HPX, IGHV3-23, IGHA1, IGHG1, IGHG2, IGHG4, JCHAIN, IVL, KRT10, LRRFIP2, NFKB1, NSDHL, PDLIM2, PSTPIP2, RAB18, RAB24, RBM47, ARHGAP27, RTCA, S100A8, S100A13, GM2A, SUCLG1, TTN, TF, UBTF, WDFY4, RP2

### Function

The strongest interpretation is a circulating humoral immune and antimicrobial module. The globally corrected terms consistently identify antibacterial and antimicrobial humoral responses, circulating immunoglobulin complexes, immunoglobulin-mediated immunity, antigen binding, B-cell-mediated immunity, B-cell receptor signaling, and classical complement activation (15 globally significant GO/KEGG terms, q_global 0.000362–0.0373; see the table). The immunoglobulin genes IGHA1, IGHG1, IGHG2, IGHG4, IGHV3-23, and JCHAIN provide the clearest functional core, while C5 and NFKB1 connect complement and inflammatory regulation to this antibody-associated signal. TF and HPX add extracellular iron and heme-handling functions that are compatible with host defense, although their inclusion may also reflect plasma protein abundance. The module therefore appears to represent a mixed humoral-defense and circulating-protein program rather than a narrowly defined intracellular pathway.

**Cell composition.** The module is strongly influenced by blood-associated and secreted proteins. HPA annotates many genes to plasma cells, memory or naive B cells, neutrophils, monocytes, lymphoid tissue, or bone marrow, and identifies sixteen module genes as secreted. The immunoglobulin genes and JCHAIN are characteristic of plasma-cell and circulating antibody material. C5, TF, HPX, HABP2, and ANXA1 are secreted or blood-associated proteins, with several showing liver enrichment rather than local expression in either target tissue. HPA also shows a substantial epithelial component, especially esophageal apical or suprabasal signatures involving IVL, KRT10, DSC2, S100A8, and related genes. The shared module may therefore partly reflect blood or immune-cell content, plasma-cell abundance, and extracellular protein carryover, with an additional epithelial or barrier-associated component in cervix_uterine. Detection of many module proteins in both tissues does not by itself establish that all genes are produced by the same local cell type.

**GO/KEGG enrichment**: 15 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP antibacterial humoral response | 0.000362 | IGHA1, IGHG1, IGHG2, IGHG4, JCHAIN, TF |
| GO:BP antimicrobial humoral response | 0.00112 | IGHA1, IGHG1, IGHG2, IGHG4, JCHAIN, TF |
| GO:CC immunoglobulin complex, circulating | 0.00112 | IGHA1, IGHG1, IGHG2, IGHG4, JCHAIN |
| GO:BP humoral immune response | 0.00116 | C5, HPX, IGHA1, IGHG1, IGHG2, IGHG4, JCHAIN, TF |
| GO:BP humoral immune response mediated by circulating immunoglobulin | 0.00278 | C5, HPX, IGHA1, IGHG1, IGHG2, IGHG4 |
| GO:CC immunoglobulin complex | 0.00278 | IGHA1, IGHG1, IGHG2, IGHG4, IGHV3-23, JCHAIN |
| GO:BP defense response to bacterium | 0.00298 | IGHA1, IGHG1, IGHG2, IGHG4, JCHAIN, NFKB1, S100A8, TF |
| GO:MF immunoglobulin receptor binding | 0.00454 | IGHA1, IGHG1, IGHG2, IGHG4, JCHAIN |
| GO:CC IgG immunoglobulin complex | 0.00689 | IGHA1, IGHG1, IGHG2, IGHG4 |
| GO:BP immunoglobulin mediated immune response | 0.0109 | C5, HPX, IGHA1, IGHG1, IGHG2, IGHG4, IGHV3-23 |
| GO:BP complement activation, classical pathway | 0.0124 | C5, IGHA1, IGHG1, IGHG2, IGHG4 |
| GO:BP B cell mediated immunity | 0.0135 | C5, HPX, IGHA1, IGHG1, IGHG2, IGHG4, IGHV3-23 |
| GO:MF antigen binding | 0.0247 | IGHA1, IGHG1, IGHG2, IGHG4, IGHV3-23, JCHAIN |
| GO:BP B cell receptor signaling pathway | 0.0269 | IGHA1, IGHG1, IGHG2, IGHG4, NFKB1 |
| GO:BP adaptive immune response based on somatic recombination of immune receptors built from immunoglobulin superfamily domains | 0.0373 | ANXA1, C5, HPX, IGHA1, IGHG1, IGHG2, IGHG4, IGHV3-23 |

### STRING and hu.MAP

STRING provides only a small set of high-confidence pairwise relationships. Known links include HPX–TF, IVL–KRT10, NFKB1–PPP2R1B, and CASP3–NFKB1. These relationships support several recognizable substructures: a plasma-protein pair, an epithelial structural pair, and an inflammatory or regulatory pair. The STRING secreted-protein annotation is supplementary (STRING Keyword Secreted; within-query FDR = 0.0417) and should not be interpreted as a globally corrected enrichment result. hu.MAP repeatedly places C5, TF, and HPX together in large extracellular or plasma-protein complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_09434.1), and (hu.MAP huMAP3_15040.1), while S100A8, IVL, and GM2A occur together in epithelial or immune-associated complexes (hu.MAP huMAP3_09929.1) and (hu.MAP huMAP3_09125.1). RP2–GLIPR2 forms a smaller hu.MAP association (hu.MAP huMAP3_14897.1). These observations indicate that the module contains known extracellular protein-complex and cellular-state signals, but most module edges are not supported by the supplied STRING or hu.MAP evidence. The network should therefore be viewed primarily as a co-abundance structure with selected biologically interpretable anchors, not as a single experimentally established protein complex.

**STRING interactions (score >= 0.7)**: 4 of 990 gene pairs: CASP3–NFKB1 (0.821); HPX–TF (0.852); IVL–KRT10 (0.933); NFKB1–PPP2R1B (0.909)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Secreted (FDR = 0.0417, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08395.1 (C5, TF, HPX; 3/43); huMAP3_09531.1 (C5, TF, HPX; 3/47); huMAP3_10101.1 (C5, TF, HPX; 3/49); huMAP3_10678.1 (C5, TF, HPX; 3/71); huMAP3_09929.1 (S100A8, IVL, GM2A; 3/75); huMAP3_14897.1 (RP2, GLIPR2; 2/9); huMAP3_07432.1 (TF, HPX; 2/18); huMAP3_07265.1 (TF, HPX; 2/20); huMAP3_08224.1 (C5, TF; 2/21); huMAP3_09434.1 (C5, TF; 2/33); huMAP3_09125.1 (S100A8, GM2A; 2/53); huMAP3_15040.1 (TF, HPX; 2/64)

### Novelty

This module should not be described as a wholly new biological pathway. Its principal components are established: circulating immunoglobulins, JCHAIN, complement C5, transferrin, hemopexin, inflammatory S100A8, and epithelial structural proteins each have documented functions, and several relationships or complexes are already represented in STRING or hu.MAP. A potentially novel aspect is the specific co-abundance pattern shared by bone_marrow and cervix_uterine, particularly the combination of antibody, complement, plasma-protein, inflammatory, and epithelial signatures. However, the supplied evidence does not establish that this cross-tissue module has not been reported previously, and absence of a STRING or hu.MAP relationship cannot prove novelty. The cautious conclusion is that the constituent biology is established, whereas the tissue-pair-specific module organization may be a new observation requiring independent replication and cell-composition control.

**Hypothesis.** Hypothesis: the shared module reflects coordinated abundance of circulating antibody and complement material at an interface between hematopoietic or plasma-cell input and epithelial tissue. Plasma-cell immunoglobulins and JCHAIN could provide the adaptive humoral component, while C5 and NFKB1 could represent complement-linked inflammatory responsiveness. TF and HPX may contribute iron and heme handling that limits damage during inflammation, and S100A8 may connect myeloid inflammatory states to epithelial or tissue-associated signals. The cervix_uterine component may additionally reflect epithelial barrier differentiation, supported by IVL, KRT10, and DSC2. This hypothesis predicts that module strength will track plasma-cell, myeloid, and epithelial-cell proportions and extracellular protein abundance; it does not establish direct physical or regulatory interactions among all module genes.

### Important genes

#### S100A8

- **Related proteins** (co-abundance neighbors): PSTPIP2 (1.00), PPP2R1B (0.99), RAB24 (0.95), CHMP1A (0.93), WDFY4 (0.91), RAB18 (0.88), CTDP1 (0.87), DSC2 (0.85), CASP3 (0.84), UBTF (0.84), CYBB (0.82), NFKB1 (0.82), BPNT1 (0.81), BOLA2; BOLA2B (0.81), GLRX (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Group enriched; location Intermediate filaments; IHC detected in bone_marrow, cervix_uterine
- **hu.MAP 3.0**: huMAP3_09929.1, huMAP3_09125.1
- **Function (MyGene.info)**: S100 calcium binding protein A8. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: inborn error of immunity (0.371); Sepsis (0.122); neoplasm (0.119); breast carcinoma (0.119); gastric cancer (0.119)
- **Europe PMC papers**: 18104
- **Why important**: S100A8 is the highest-connectivity gene in the supplied module and links many otherwise weakly connected genes, including inflammatory, trafficking, epithelial, and intracellular regulators. HPA associates it with bone marrow, cervix, monocytes, and neutrophils, and it is secreted to blood. It is included in the globally supported bacterial-defense term (GO:BP defense response to bacterium; q_global = 0.00298) and in the supplementary secreted annotation (STRING Keyword Secreted; within-query FDR = 0.0417). Its documented inflammatory and leukocyte-migration functions, together with disease associations involving sepsis and inborn errors of immunity, make it a key indicator of myeloid or inflammatory composition rather than merely a peripheral module member.
- **Conclusion**: Established evidence supports S100A8 as a central network marker of inflammatory and myeloid-associated biology. It is plausible that S100A8 helps connect immune and epithelial signals in this module, but the co-abundance data do not demonstrate that it mechanistically drives the antibody or complement program.

#### C5

- **Related proteins** (co-abundance neighbors): WDFY4 (1.00), H1-3 (0.98), FKBP4 (0.86); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_08224.1, huMAP3_09434.1
- **Function (MyGene.info)**: complement C5. This gene encodes a component of the complement system, a part of the innate immune system that plays an important role in inflammation, host homeostasis, and host defense against pathogens. The encoded preproprotein is proteolytically processed to generate multiple protein products, including the C5 alpha chain, C5 beta chain, C5a anaphylatoxin and C5b. The C5 protein is comprised of the C5 alpha…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.744); paroxysmal nocturnal hemoglobinuria (0.610); myasthenia gravis (0.586); atypical hemolytic-uremic syndrome (0.544); neuromyelitis optica (0.516)
- **Europe PMC papers**: 81450
- **Why important**: C5 is present in several globally corrected humoral, immunoglobulin-mediated, complement, and B-cell-related terms (GO:BP humoral immune response; q_global = 0.00116), (GO:BP humoral immune response mediated by circulating immunoglobulin; q_global = 0.00278), (GO:BP immunoglobulin mediated immune response; q_global = 0.0109) (GO:BP complement activation, classical pathway; q_global = 0.0124) (GO:BP B cell mediated immunity; q_global = 0.0135), (GO:BP adaptive immune response based on somatic recombination of immune receptors built from immunoglobulin superfamily domains; q_global = 0.0373). It is a secreted liver-enriched complement protein and appears with TF and HPX across multiple hu.MAP extracellular or plasma-protein complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_08224.1) (hu.MAP huMAP3_09434.1), (hu.MAP huMAP3_15040.1). Its disease associations include late complement deficiency and paroxysmal nocturnal hemoglobinuria, and it has extensive literature support. Its relatively modest local network connectivity but repeated complex membership make it an important extracellular anchor.
- **Conclusion**: Established evidence supports C5 as a complement and circulating-plasma component of the module. Its HPA profile cautions that its co-abundance may reflect blood or extracellular protein contribution rather than C5 production by bone-marrow or cervical cells.

#### IGHG4

- **Related proteins** (co-abundance neighbors): IGHA1 (0.95), ANXA1 (0.91), IGHG1 (0.90); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Group enriched; location None; IHC detected in bone_marrow, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: immunoglobulin heavy constant gamma 4 (G4m marker)
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 1010
- **Why important**: IGHG4 is connected to the other immunoglobulin-heavy-chain genes and is included in every globally corrected enrichment term (15 globally significant GO/KEGG terms, q_global 0.000362–0.0373; see the table). HPA places it in lymphoid tissue and plasma cells, with immunoglobulin secretion and blood-cell enrichment. It therefore represents the antibody-producing component of the module and helps explain the repeated immunoglobulin-complex and humoral-response signals. Its literature volume is substantial, although the supplied Open Targets field does not provide a disease association for this gene.
- **Conclusion**: Established evidence identifies IGHG4 as a core circulating antibody and plasma-cell marker. Its presence supports a humoral immune interpretation, but it cannot by itself establish antigen specificity, local antibody production, or a direct interaction with the non-immunoglobulin genes.

#### JCHAIN

- **Related proteins** (co-abundance neighbors): RP2 (1.00), PDLIM2 (0.91); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Group enriched; location None; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: joining chain of multimeric IgA and IgM. Enables IgA binding activity and protein homodimerization activity. Contributes to several functions, including immunoglobulin receptor binding activity; peptidoglycan binding activity; and phosphatidylcholine binding activity. Involved in several processes, including defense response to other organism; glomerular filtration; and positive regulation of respiratory burst. Located in extracellular s…
- **Diseases (Open Targets)**: breast carcinoma (0.101); breast cancer (0.093); neoplasm (0.089); cancer (0.081); Barrett esophagus (0.062)
- **Europe PMC papers**: 2428
- **Why important**: JCHAIN connects immunoglobulin biology with the broader module and is included in the antibacterial, antimicrobial, immunoglobulin-complex, receptor-binding, antigen-binding, and adaptive immune terms (8 globally significant GO/KEGG terms, q_global 0.000362–0.00454; see the table), (GO:MF antigen binding; q_global = 0.0247). HPA identifies it in plasma cells and as secreted to blood. Its documented role in joining multimeric IgA and IgM makes it especially informative for interpreting the module as an extracellular antibody assembly or secretion signal. It also has a direct module connection to PDLIM2 and RP2, although those edges are co-abundance relationships rather than established physical interactions in the supplied evidence.
- **Conclusion**: Established evidence supports JCHAIN as a strong marker of secreted multimeric immunoglobulin biology. A possible interpretation is that it reports plasma-cell or antibody-material abundance in the tissue samples, but the data do not show that JCHAIN regulates the inflammatory or epithelial subnetwork.

#### TF

- **Related proteins** (co-abundance neighbors): IGHG2 (0.97), ARHGAP27 (0.89), GLIPR2 (0.84); STRING partners: HPX (0.852)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_08224.1, huMAP3_09434.1, huMAP3_15040.1
- **Function (MyGene.info)**: transferrin. This gene encodes a glycoprotein with an approximate molecular weight of 76.5 kDa. It is thought to have been created as a result of an ancient gene duplication event that led to generation of homologous C and N-terminal domains each of which binds one ion of ferric iron. The function of this protein is to transport iron from the intestine, reticuloendothelial system, and liver parenchymal cells t…
- **Diseases (Open Targets)**: atransferrinemia (0.776); alcohol drinking (0.492); hemochromatosis type 1 (0.471); neurodegenerative disease (0.400); urolithiasis (0.329)
- **Europe PMC papers**: 143656
- **Why important**: TF is a highly studied secreted iron-transport protein with very extensive literature support. It is included in globally corrected antibacterial, antimicrobial, humoral, and bacterial-defense terms (GO:BP antibacterial humoral response; q_global = 0.000362), (GO:BP antimicrobial humoral response; q_global = 0.00112), (GO:BP humoral immune response; q_global = 0.00116), (GO:BP defense response to bacterium; q_global = 0.00298), and it forms a high-confidence STRING relationship with HPX while recurring with C5 and HPX in hu.MAP complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_07432.1), (hu.MAP huMAP3_07265.1), (hu.MAP huMAP3_15040.1). HPA associates it with liver and hepatocytes and does not detect it in immune cells, which is important for distinguishing circulating protein from local immune-cell expression. Its iron-transport function provides a plausible host-defense context but does not make it an antibody component.
- **Conclusion**: Established evidence supports TF as a circulating iron-transport and plasma-protein anchor that helps explain the extracellular character of the module. The most cautious interpretation is that TF reflects shared plasma or extracellular abundance and may contribute to antimicrobial context indirectly, rather than acting as a demonstrated core regulator of B-cell immunity.

## Module 1

**Tissue pair**: bone_marrow and cervix_uterine  
**Genes (46)**: ACO1, ADPGK, BUB1B, MTHFD1L, NCAPD2, CNOT12, CORO1B, CORO1C, CYFIP1, DNAAF5, DDX42, DECR1, DNMT1, EEA1, ELP1, EPS15L1, EXOC8, FANCI, FNDC3A, GAPVD1, GEMIN5, MTIF2, KIF11, LEMD3, MDN1, PPP1R12A, NCKAP1, NEDD4L, NEMF, NKRF, NSUN2, NUP160, NUP98, P4HA1, PLCB3, PITRM1, RPAP3, SEPTIN2, SMARCC2, TOR1AIP2, TRIO, UBR5, UTRN, WDHD1, YAP1, ZNF326

### Function

The strongest interpretation is a cell-cycle and chromosome-organization module, especially involving centromeric and condensed centromeric chromosome regions. The primary evidence is the globally corrected GO cellular-component enrichment for chromosome, centromeric region (GO:CC chromosome, centromeric region; q_global = 0.0211) and condensed chromosome, centromeric region (GO:CC condensed chromosome, centromeric region; q_global = 0.0383). BUB1B, NCAPD2, and KIF11 support a mitotic chromosome-segregation and spindle interpretation, while DNMT1 and SMARCC2 connect the module to chromatin maintenance and remodeling. A secondary actin and cell-migration component is supported by NCKAP1, CYFIP1, CORO1B, CORO1C, PPP1R12A, SEPTIN2, TRIO, and UTRN, but this component is not represented by a globally significant GO or KEGG term. Thus, the module is best viewed as a mixed proliferative nuclear and cytoskeletal program rather than a single narrowly defined biochemical pathway. No STRING functional-enrichment term was reported.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the HPA summary identifies only a small secreted subset, and many characterized proteins are intracellular or membrane-associated. The module is also not uniformly immune-cell specific, because most genes have low immune-cell specificity and many have low tissue specificity. Nevertheless, its cellular context is strongly compatible with blood and marrow progenitors: HPA enrichment is frequent in neutrophil, erythrocyte, megakaryocyte, and monocyte progenitor populations, with additional enrichment in lymphoid tissue and bone marrow. Several genes are detected in both bone marrow and cervix, and the module includes broadly expressed housekeeping-like machinery for chromosome maintenance, nuclear transport, RNA processing, translation, and metabolism. Therefore, the shared signal may partly reflect proliferating or shared blood-related cell populations in the samples, rather than a cervix-specific secreted program.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chromosome, centromeric region | 0.0211 | BUB1B, DNMT1, NCAPD2, NUP160, NUP98, PPP1R12A, SEPTIN2, SMARCC2 |
| GO:CC condensed chromosome, centromeric region | 0.0383 | BUB1B, NCAPD2, NUP160, NUP98, PPP1R12A, SEPTIN2, SMARCC2 |

### STRING and hu.MAP

STRING supplies a limited but coherent set of high-confidence pairwise relationships. The most informative connections are BUB1B with KIF11, FANCI, NUP98, and UBR5; KIF11 with NCAPD2 and WDHD1; NUP160 with NUP98; CORO1B with CORO1C; CYFIP1 with NCKAP1; and EEA1 with GAPVD1. These known relationships support real substructures involving spindle and chromosome control, nuclear pores, actin regulation, and endosomal trafficking, but the absence of STRING functional enrichment means that the entire module is not an established STRING pathway. hu.MAP independently recovers the NUP98-NUP160 nuclear-pore pair (hu.MAP huMAP3_06517.1) (hu.MAP huMAP3_09710.1) (hu.MAP huMAP3_12581.1), the CORO1B-CORO1C actin-associated pair across several complexes (hu.MAP huMAP3_04826.1) (hu.MAP huMAP3_07776.1) (hu.MAP huMAP3_05614.1) (hu.MAP huMAP3_09579.1) (hu.MAP huMAP3_11076.1) (hu.MAP huMAP3_10784.1) (hu.MAP huMAP3_09710.1), the CYFIP1-NCKAP1 WAVE or actin-regulatory associations (hu.MAP huMAP3_02474.1) (hu.MAP huMAP3_09598.1) (hu.MAP huMAP3_13345.1), the ACO1-LEMD3 associations (hu.MAP huMAP3_14587.1) (hu.MAP huMAP3_13623.1), the NSUN2-DECR1 associations (hu.MAP huMAP3_11037.1) (hu.MAP huMAP3_12301.1) (hu.MAP huMAP3_12727.1), the DNMT1-PLCB3 association (hu.MAP huMAP3_13998.1), the DDX42-GEMIN5 ribonucleoprotein associations (hu.MAP huMAP3_04549.1) (hu.MAP huMAP3_08980.1), and the MTIF2-MTHFD1L association (hu.MAP huMAP3_13468.1). Because most hu.MAP complexes contain only a subset of their members in the module, these results validate local components rather than a single complete complex spanning the module.

**STRING interactions (score >= 0.7)**: 11 of 1035 gene pairs: BUB1B–FANCI (0.818); BUB1B–KIF11 (0.994); BUB1B–NUP98 (0.833); BUB1B–UBR5 (0.782); CORO1B–CORO1C (0.917); CYFIP1–NCKAP1 (0.999); EEA1–GAPVD1 (0.802); FANCI–KIF11 (0.856); KIF11–NCAPD2 (0.86); KIF11–WDHD1 (0.853); NUP160–NUP98 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06517.1 (NUP98, NUP160; 2/3); huMAP3_04826.1 (CORO1B, CORO1C; 2/4); huMAP3_07776.1 (CORO1B, CORO1C; 2/7); huMAP3_05614.1 (CORO1B, CORO1C; 2/8); huMAP3_09579.1 (CORO1B, CORO1C; 2/9); huMAP3_14587.1 (ACO1, LEMD3; 2/10); huMAP3_11076.1 (CORO1B, CORO1C; 2/10); huMAP3_13623.1 (ACO1, LEMD3; 2/11); huMAP3_10784.1 (CORO1B, CORO1C; 2/13); huMAP3_02474.1 (CYFIP1, NCKAP1; 2/13); huMAP3_09710.1 (NUP98, NUP160; 2/13); huMAP3_11037.1 (NSUN2, DECR1; 2/14); huMAP3_09598.1 (CYFIP1, NCKAP1; 2/23); huMAP3_13998.1 (DNMT1, PLCB3; 2/23); huMAP3_12301.1 (NSUN2, DECR1; 2/26); huMAP3_12727.1 (NSUN2, DECR1; 2/32); huMAP3_13345.1 (CYFIP1, NCKAP1; 2/35); huMAP3_04549.1 (DDX42, GEMIN5; 2/52); huMAP3_12581.1 (NUP98, NUP160; 2/58); huMAP3_08980.1 (DDX42, GEMIN5; 2/97); huMAP3_13468.1 (MTIF2, MTHFD1L; 2/99)

### Novelty

The module should not be called a newly discovered molecular complex or pathway. Its central biology is already well established through the known functions of BUB1B, KIF11, NCAPD2, DNMT1, NUP98, NUP160, CORO proteins, and the CYFIP1-NCKAP1 actin machinery, as well as the STRING and hu.MAP relationships. The potentially novel aspect is the conserved co-abundance arrangement across bone marrow and cervix uterine tissue groups, particularly the coupling of a proliferative chromosome-maintenance program with actin and trafficking components. However, co-abundance alone does not establish physical interaction, causal regulation, or tissue-specific mechanism. Absence from STRING or hu.MAP is not evidence of novelty; the tissue-pair context and reproducibility in independent material would be needed to support a new finding.

**Hypothesis.** Hypothesis: the shared module reflects proliferating progenitor or progenitor-like cells present in both tissue groups. A core involving BUB1B, KIF11, NCAPD2, DNMT1, and the NUP98-NUP160 pore pair may coordinate chromosome surveillance, condensation, epigenetic maintenance, spindle function, and nucleocytoplasmic transport. In parallel, NCKAP1, CYFIP1, CORO1B, CORO1C, PPP1R12A, SEPTIN2, and related proteins may support actin remodeling, adhesion, migration, cytokinesis, or vesicle positioning. The apparent cross-tissue conservation could therefore arise from a shared mixture of cycling hematopoietic cells, other proliferating cells, and broadly expressed cellular machinery. This is a testable hypothesis, not a demonstrated causal model; it should be evaluated with cell-resolved measurements, proliferation markers, and perturbation of the proposed chromosome and actin submodules.

### Important genes

#### NCKAP1

- **Related proteins** (co-abundance neighbors): ACO1 (0.93), TOR1AIP2 (0.93), CYFIP1 (0.89), EPS15L1 (0.89), BUB1B (0.88), ZNF326 (0.88), SEPTIN2 (0.87), EXOC8 (0.87), MTHFD1L (0.86), DDX42 (0.84), TRIO (0.84), PITRM1 (0.84), CORO1C (0.84), P4HA1 (0.83), CORO1B (0.82), DECR1 (0.82); STRING partners: CYFIP1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_02474.1, huMAP3_09598.1, huMAP3_13345.1
- **Function (MyGene.info)**: NCK associated protein 1. Contributes to small GTPase binding activity. Involved in Rac protein signal transduction; positive regulation of Arp2/3 complex-mediated actin nucleation; and positive regulation of lamellipodium assembly. Located in extracellular exosome and focal adhesion. Part of SCAR complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.528); neurodevelopmental disorder (0.471); hereditary disease (0.451); complex neurodevelopmental disorder (0.443); Intellectual disability (0.437)
- **Europe PMC papers**: 1019
- **Why important**: NCKAP1 is the principal network hub in the supplied subgraph and connects the module to ACO1, CYFIP1, SEPTIN2, and several trafficking, nuclear, and cytoskeletal proteins. Its annotation places it in Rac signaling, Arp two-thirds complex-mediated actin nucleation, lamellipodium assembly, migration, and the SCAR complex. The CYFIP1-NCKAP1 relationship is supported by STRING and multiple hu.MAP complexes (hu.MAP huMAP3_02474.1) (hu.MAP huMAP3_09598.1) (hu.MAP huMAP3_13345.1). It is broadly expressed rather than immune restricted, and its disease associations include neurodevelopmental and neurodegenerative disorders, with substantial literature support.
- **Conclusion**: Established: NCKAP1 is a central cytoskeletal and Rac-linked organizer and is strongly connected within this module. Hypothesis: its hub position may couple actin remodeling or migration to the chromosome and trafficking program, but the co-abundance data do not prove that it regulates the nuclear submodule.

#### BUB1B

- **Related proteins** (co-abundance neighbors): NCKAP1 (0.88), FNDC3A (0.86), MDN1 (0.85), UBR5 (0.81), GAPVD1 (0.81); STRING partners: FANCI (0.818), KIF11 (0.994), NUP98 (0.833), UBR5 (0.782)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BUB1 mitotic checkpoint serine/threonine kinase B. This gene encodes a kinase involved in spindle checkpoint function. The protein has been localized to the kinetochore and plays a role in the inhibition of the anaphase-promoting complex/cyclosome (APC/C), delaying the onset of anaphase and ensuring proper chromosome segregation. Impaired spindle checkpoint function has been found in many forms of cancer. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: mosaic variegated aneuploidy syndrome (0.815); mosaic variegated aneuploidy syndrome 1 (0.794); premature chromatid separation trait (0.631); neurodegenerative disease (0.537); colorectal cancer (0.503)
- **Europe PMC papers**: 3723
- **Why important**: BUB1B is directly represented in both primary centromeric enrichment terms (GO:CC chromosome, centromeric region; q_global = 0.0211) (GO:CC condensed chromosome, centromeric region; q_global = 0.0383) and is annotated as a spindle-checkpoint kinase controlling anaphase timing and chromosome segregation. It connects to KIF11, FANCI, NUP98, and UBR5 in STRING, including especially strong spindle-related support. HPA indicates enrichment in bone marrow and lymphoid tissue and in several hematopoietic progenitor populations. Its disease associations include mosaic variegated aneuploidy and premature chromatid separation, with substantial literature.
- **Conclusion**: Established: BUB1B is a strong marker of the module's mitotic chromosome-surveillance component. Hypothesis: coordinated BUB1B abundance may indicate active or recently active proliferation in the shared tissue samples, but it cannot by itself identify the responsible cell population.

#### DNMT1

- **Related proteins** (co-abundance neighbors): NEDD4L (0.89), NCAPD2 (0.86), FANCI (0.85), NEMF (0.83), GEMIN5 (0.82), NKRF (0.81), MTHFD1L (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_13998.1
- **Function (MyGene.info)**: DNA methyltransferase 1. This gene encodes an enzyme that transfers methyl groups to cytosine nucleotides of genomic DNA. This protein is the major enzyme responsible for maintaining methylation patterns following DNA replication and shows a preference for hemi-methylated DNA. Methylation of DNA is an important component of mammalian epigenetic gene regulation. Aberrant methylation patterns are found in human tumors and a…
- **Diseases (Open Targets)**: autosomal dominant cerebellar ataxia, deafness and narcolepsy (0.806); hereditary sensory neuropathy-deafness-dementia syndrome (0.777); acute myeloid leukemia (0.623); myelodysplastic syndrome (0.615); cancer (0.612)
- **Europe PMC papers**: 30754
- **Why important**: DNMT1 is one of the module's highest-connectivity genes and is directly included in the globally significant centromeric-region term (GO:CC chromosome, centromeric region; q_global = 0.0211). It maintains DNA methylation after replication and is linked to constitutive heterochromatin, transcriptional control, acute myeloid leukemia, and myelodysplastic syndrome. Its network links include NEDD4L, NCAPD2, FANCI, NEMF, GEMIN5, and MTHFD1L, placing it at the interface of chromatin maintenance, genome stability, RNA-related machinery, and metabolism. HPA shows bone-marrow detection and enrichment in erythrocyte and megakaryocyte progenitors; the literature volume is very substantial.
- **Conclusion**: Established: DNMT1 provides a biologically credible bridge between DNA methylation maintenance and the module's chromosome-centered signal. Hypothesis: it may help preserve the proliferative or differentiation state of the shared cell population, but this module does not establish altered methylation or direct regulation of its neighboring genes.

#### NUP98

- **Related proteins** (co-abundance neighbors): NEDD4L (0.84); STRING partners: BUB1B (0.833), NUP160 (0.999)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06517.1, huMAP3_09710.1, huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 98 and 96 precursor. Nuclear pore complexes (NPCs) regulate the transport of macromolecules between the nucleus and cytoplasm, and are composed of many polypeptide subunits, many of which belong to the nucleoporin family. This gene belongs to the nucleoporin gene family and encodes a 186 kDa precursor protein that undergoes autoproteolytic cleavage to generate a 98 kDa nucleoporin and 96 kDa nucleoporin. The 98 kDa nu…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); acute myeloid leukemia (0.399); lung carcinoma (0.376)
- **Europe PMC papers**: 4839
- **Why important**: NUP98 is included in both primary centromeric enrichment terms (GO:CC chromosome, centromeric region; q_global = 0.0211) (GO:CC condensed chromosome, centromeric region; q_global = 0.0383) and is paired with NUP160 by STRING and several hu.MAP complexes (hu.MAP huMAP3_06517.1) (hu.MAP huMAP3_09710.1) (hu.MAP huMAP3_12581.1). Its established functions include nuclear-pore organization, RNA export, protein transport, and peripheral genome organization. It also connects to BUB1B, linking nuclear transport to the chromosome and spindle component. HPA places it in a neutrophil-enriched single-cell context, and its disease associations include viral disease, acute myeloid leukemia, and carcinoma, with a substantial literature.
- **Conclusion**: Established: NUP98 is a credible nuclear-transport and genome-organization component, and the NUP98-NUP160 relationship is independently supported. Hypothesis: the pair may coordinate nuclear transport with proliferative chromosome organization in the shared module, but the abundance data do not demonstrate altered pore function.

#### CORO1B

- **Related proteins** (co-abundance neighbors): YAP1 (0.88), NCKAP1 (0.82); STRING partners: CORO1C (0.917)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in bone_marrow, cervix_uterine
- **hu.MAP 3.0**: huMAP3_04826.1, huMAP3_07776.1, huMAP3_05614.1, huMAP3_09579.1, huMAP3_11076.1, huMAP3_10784.1
- **Function (MyGene.info)**: coronin 1B. Members of the coronin family, such as CORO1B, are WD repeat-containing actin-binding proteins that regulate cell motility (Cai et al., 2005 [PubMed 16027158]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Abnormality of refraction (0.067); refractive error (0.049); alcohol drinking (0.027); asthma (0.025); diabetes mellitus (0.025)
- **Europe PMC papers**: 339
- **Why important**: CORO1B represents the module's clearest actin-motility branch. It is connected to NCKAP1 and YAP1, is annotated for actin filament organization, cell migration, ruffle organization, and Arp2/3 regulation, and forms a recurrent CORO1B-CORO1C pair in STRING and hu.MAP complexes (hu.MAP huMAP3_04826.1) (hu.MAP huMAP3_07776.1) (hu.MAP huMAP3_05614.1) (hu.MAP huMAP3_09579.1) (hu.MAP huMAP3_11076.1) (hu.MAP huMAP3_10784.1). HPA detects it in both bone marrow and cervix and associates it with non-classical monocytes and several epithelial or trophoblast-related cell types. Its literature is smaller than that of the central chromosome genes, but its function is directly relevant to the cytoskeletal branch.
- **Conclusion**: Established: CORO1B supports an actin-remodeling and migration component that is independently reflected by CORO1C relationships. Hypothesis: this branch may represent cell movement, adhesion, or cytokinetic remodeling accompanying the proliferative program, but the module does not establish which of these processes dominates.

## Module 2

**Tissue pair**: bone_marrow and cervix_uterine  
**Genes (7)**: FDXR, CC2D1B, CEP170, KIF14, RBM27, INPPL1, WASHC4

### Function

No GO or KEGG term passed global correction, and there are no supplementary STRING enrichment terms. The strongest biological interpretation is therefore hypothesis-generating rather than enrichment-based. The co-abundance pattern is centered on KIF14, a microtubule motor associated with spindle organization, chromosome segregation, and cytokinesis, with peripheral genes related to centrosomal organization, endosomal transport, actin remodeling, mitochondrial electron transfer, RNA processing, and transcriptional regulation. This suggests a broad proliferative or structural-cellular program rather than a narrowly defined pathway. Because the network is based on abundance relationships, these genes may be coordinated through shared cell state or composition rather than direct molecular binding.

**Cell composition.** The module is not composed of plasma or secreted proteins: all module genes are annotated as non-secreted. Most genes have low tissue specificity and low immune-cell specificity, while several show cell-type-enhanced patterns in progenitors, epithelial cells, neural cells, spermatogenic cells, or microglia. KIF14 is enhanced in bone marrow and lymphoid tissue and is also associated with erythrocyte progenitors, whereas CEP170 is group-enriched in bone marrow, brain, and testis. CC2D1B is immune-cell enhanced in basophils, and WASHC4 is enhanced in neutrophils and neutrophil progenitors. Protein detection is mixed between bone marrow and cervix. Thus, the module is not a conventional blood or plasma-protein signature, but shared progenitor, proliferative, epithelial, or other cell-state composition could contribute to its preservation across the two tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No pair among the module genes has a high-confidence STRING interaction in the supplied results, and no hu.MAP complex contains multiple module members. The observed edges should therefore be interpreted as co-abundance relationships rather than established physical interactions. Known functional evidence comes mainly from individual-gene annotations: KIF14 links to microtubule-dependent movement and cytokinesis; CEP170 to centrosomes and spindle-associated microtubules; INPPL1 to endocytosis, actin organization, cell adhesion, and mitotic spindle orientation; WASHC4 to endosomal transport and actin nucleation; and FDXR to mitochondrial electron transfer and steroid or cholesterol-related metabolism. The lack of STRING and hu.MAP support weakens a claim for a preassembled protein complex, while still allowing coordinated regulation in particular cellular states.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears potentially novel as a conserved co-abundance module shared by bone marrow and cervix, because the supplied databases provide no high-confidence physical interactions, no shared hu.MAP complex, and no STRING enrichment. However, absence from these resources does not establish biological novelty: the module could reflect coordinated expression, cell composition, indirect regulation, or technical properties of the datasets. The lack of globally significant GO or KEGG enrichment also prevents assigning it a previously recognized pathway identity. A defensible claim is that the cross-tissue co-abundance pattern is a candidate finding requiring independent replication and testing at the protein, single-cell, and perturbation levels.

**Hypothesis.** Hypothesis: the module marks a shared proliferative or progenitor-like cellular state in bone marrow and cervix, in which KIF14-centered microtubule and centrosome activity is coordinated with endosomal trafficking, actin remodeling, transcriptional or RNA-processing control, and mitochondrial support. KIF14 may represent the central abundance-linked organizer, while CEP170 could reflect centrosomal and spindle architecture, INPPL1 and WASHC4 membrane-trafficking or cytoskeletal remodeling, and FDXR metabolic support. This is a mechanistic hypothesis, not an established pathway assignment, because the module has no globally significant enrichment and no corroborating STRING or hu.MAP complex.

### Important genes

#### KIF14

- **Related proteins** (co-abundance neighbors): FDXR (0.91), RBM27 (0.90), INPPL1 (0.90), WASHC4 (0.84), CC2D1B (0.83), CEP170 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol, End piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin family member 14. This gene encodes a member of the kinesin-3 superfamily of microtubule motor proteins. These proteins are involved in numerous processes including vesicle transport, chromosome segregation, mitotic spindle formation, and cytokinesis. In human HeLa-S3 and 293T cells, this protein is localized to the cytoplasm during interphase, to the spindle poles and spindle microtubules during mitosis, and to th…
- **Diseases (Open Targets)**: microcephaly 20, primary, autosomal recessive (0.722); lethal fetal cerebrorenogenitourinary agenesis/hypoplasia syndrome (0.695); autosomal recessive primary microcephaly (0.665); neurodegenerative disease (0.550); Joubert syndrome and related disorders (0.402)
- **Europe PMC papers**: 1550
- **Why important**: KIF14 is the topological hub of the module, connected to every other member in the supplied co-abundance subgraph. Its established functions include kinesin-mediated microtubule movement, spindle organization, chromosome alignment, cell-cycle progression, and cytokinesis. It has substantial literature and multiple disease associations involving neurodevelopment and microcephaly-related disorders. Its bone-marrow and lymphoid-tissue enhancement, together with progenitor-associated cell patterns, makes it a plausible marker of a proliferative or progenitor-related state.
- **Conclusion**: Established evidence supports KIF14 as the central network marker and as a regulator of microtubule-dependent cell division. It is reasonable to hypothesize that variation in KIF14 abundance helps organize the module signal, but the co-abundance data do not demonstrate that KIF14 regulates the other genes.

#### CEP170

- **Related proteins** (co-abundance neighbors): KIF14 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Centrosome, Basal body; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: centrosomal protein 170. The product of this gene is a component of the centrosome, a non-membraneous organelle that functions as the major microtubule-organizing center in animal cells. During interphase, the encoded protein localizes to the sub-distal appendages of mature centrioles, which are microtubule-based structures thought to help organize centrosomes. During mitosis, the protein associates with spindle microtubu…
- **Diseases (Open Targets)**: hypertensive disorder (0.463); mathematical ability (0.423); aortic stenosis (0.415); essential hypertension (0.398); health study participation (0.398)
- **Europe PMC papers**: 671
- **Why important**: CEP170 is directly connected to KIF14 and encodes a centrosomal protein associated with centriole appendages and spindle microtubules. Its group-enriched pattern in bone marrow, brain, and testis and its cell-type enhancement in neural and spermatogenic populations are consistent with involvement in specialized or dividing cells. It has a substantial literature and disease-trait associations in the supplied evidence.
- **Conclusion**: Established evidence supports CEP170 as a centrosome and microtubule-organization marker. Its co-abundance with KIF14 is compatible with a shared division or centrosomal program, but a direct CEP170–KIF14 interaction is not supported by the supplied STRING or hu.MAP results.

#### INPPL1

- **Related proteins** (co-abundance neighbors): KIF14 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inositol polyphosphate phosphatase like 1. The protein encoded by this gene is an SH2-containing 5'-inositol phosphatase that is involved in the regulation of insulin function. The encoded protein also plays a role in the regulation of epidermal growth factor receptor turnover and actin remodelling. Additionally, this gene supports metastatic growth in breast cancer and is a valuable biomarker for breast cancer. [provided by RefSeq, Jan 20…
- **Diseases (Open Targets)**: opsismodysplasia (0.800); endometrial cancer (0.370); schneckenbecken dysplasia (0.370); hereditary disease (0.194); gastric cancer (0.101)
- **Europe PMC papers**: 966
- **Why important**: INPPL1 is connected to the module hub and has functions spanning phosphoinositide signaling, endocytosis, actin remodeling, cell adhesion, mitotic spindle orientation, and endochondral ossification. It is detected by immunohistochemistry in both tissues and has substantial literature, including disease associations involving skeletal development and cancer-related biology. This gives it a plausible bridging role between cell division, adhesion, and membrane trafficking.
- **Conclusion**: Established evidence supports INPPL1 as a signaling and cytoskeletal-regulatory protein with relevance to tissue structure and cell behavior. Its participation in the module may reflect coordinated remodeling or proliferation, but the module does not establish a specific INPPL1-dependent mechanism.

#### WASHC4

- **Related proteins** (co-abundance neighbors): KIF14 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WASH complex subunit 4. This gene encodes a component of the WASH complex, which functions in the intracellular transport of endosomes. Mutations in this gene have been detected in individuals with autosomal recessive cognitive disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014].
- **Diseases (Open Targets)**: autosomal recessive non-syndromic intellectual disability (0.611); Intellectual disability (0.345); mathematical ability (0.322); Abnormality of the skeletal system (0.148); corneal ulcer (0.140)
- **Europe PMC papers**: 116
- **Why important**: WASHC4 is connected to KIF14 and encodes a WASH-complex subunit involved in endosome organization, endosomal transport, and regulation of actin nucleation. It is detected in both tissues and shows enhancement in microglia, neutrophils, and neutrophil progenitors. Although its literature is more limited than that of the hub genes, its function provides a concrete intracellular-trafficking and cytoskeletal link within the module.
- **Conclusion**: Established evidence supports WASHC4 as an endosomal and actin-regulatory component. Its association with the module could indicate coordinated trafficking during a progenitor or remodeling state, but no physical complex containing multiple module members was detected.

#### FDXR

- **Related proteins** (co-abundance neighbors): KIF14 (0.91); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ferredoxin reductase. This gene encodes a mitochondrial flavoprotein that initiates electron transport for cytochromes P450 receiving electrons from NADPH. Multiple alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: auditory neuropathy-optic atrophy syndrome (0.772); multiple mitochondrial dysfunctions syndrome 9b (0.728); hereditary disease (0.518); optic atrophy-ataxia-peripheral neuropathy-global developmental delay syndrome (0.492); congenital adrenal hyperplasia (0.370)
- **Europe PMC papers**: 1148
- **Why important**: FDXR is connected to KIF14 and encodes a mitochondrial flavoprotein involved in electron transfer to cytochrome systems. Its annotations include precursor-metabolite generation, ferredoxin metabolism, and cholesterol-related biosynthetic processes. It has substantial literature and disease associations involving mitochondrial dysfunction, auditory or optic neuropathy, and adrenal biology. Its tissue enrichment in adrenal gland contrasts with the broader pattern of several other module genes and may represent metabolic-state variation rather than a shared tissue identity.
- **Conclusion**: Established evidence supports FDXR as a mitochondrial metabolic gene. Its co-abundance with the KIF14-centered structural program is compatible with metabolic support for active or dividing cells, but this connection remains a hypothesis because no pathway enrichment or known complex links FDXR to the other module members.

## Module 3

**Tissue pair**: bone_marrow and cervix_uterine  
**Genes (10)**: ATP5PB, C1QBP, CACYBP, ETFA, NNMT, PHB1, PSMA1, PSMA4, RPL6, SEC22B

### Function

No GO/KEGG term passed global correction, so the module does not have a statistically established pathway annotation from GO or KEGG. Its strongest functional signal is a proteostasis component: PSMA1 and PSMA4 are proteasome core alpha subunits, form a very strong STRING relationship, and occur together in multiple hu.MAP proteasome complexes (hu.MAP huMAP3_00356.1)(hu.MAP huMAP3_09656.1)(hu.MAP huMAP3_13725.1). The supplementary STRING annotation for a proteasome subunit signature (STRING SMART Proteasome subunit A N-terminal signature  Add an annotation; within-query FDR = 0.0479) supports this interpretation but is not global enrichment evidence. The remaining genes indicate potentially coordinated cellular maintenance processes, including mitochondrial energy metabolism through ATP5PB, ETFA, PHB1, and C1QBP; protein turnover and ubiquitin-associated regulation through CACYBP; translation through RPL6; and ER-to-Golgi trafficking through SEC22B. Because the module contains several weakly connected functional branches rather than a densely interconnected pathway, the most defensible interpretation is a broad cellular proteostasis and metabolic-maintenance program with a proteasome-related core, not a demonstrated specialized tissue pathway.

**Cell composition.** The module is predominantly intracellular rather than a plasma or secreted-protein module. C1QBP is annotated as secreted to blood, and PHB1 has intracellular and membrane localization, while the other genes are not annotated as secreted; thus the module does not appear dominated by circulating proteins. Most genes have low tissue specificity and low immune-cell specificity in HPA, and no blood-cell enrichment was reported. All module proteins have cell-type-enhanced annotations, but these span diverse epithelial, trophoblast, stromal, germ-cell, hepatic, platelet, and neural or myeloid-related cell types rather than defining a single shared lineage. Protein detection is broad in both bone marrow and cervix, with NNMT being detected in cervix but not bone marrow. Overall, the shared signal could reflect broadly expressed cellular maintenance machinery or shared cellular states, rather than a bone-marrow-specific or cervix-specific program; contamination by plasma proteins or a simple blood-cell explanation is not supported by the HPA summary.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports two specific relationships within the module: the PSMA1–PSMA4 proteasome relationship (STRING SMART Proteasome subunit A N-terminal signature  Add an annotation; within-query FDR = 0.0479) and the C1QBP–PHB1 relationship. The PSMA1–PSMA4 edge is especially well established and is reinforced by membership of both proteins in several hu.MAP proteasome complexes (hu.MAP huMAP3_00356.1)(hu.MAP huMAP3_09656.1)(hu.MAP huMAP3_13725.1). In those hu.MAP complexes, the module contributes only the PSMA1 and PSMA4 members while the complexes contain many additional proteasome subunits. This indicates that the module captures a recognizable proteasome fragment rather than a newly defined complete complex. The other module edges are not supported by the listed high-confidence STRING interactions or hu.MAP complexes. Therefore, the network contains a small known proteasome subnetwork and a known C1QBP–PHB1 association, but most co-abundance links remain molecularly unvalidated by these resources.

**STRING interactions (score >= 0.7)**: 2 of 45 gene pairs: C1QBP–PHB1 (0.847); PSMA1–PSMA4 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Proteasome subunit A N-terminal signature  Add an annotation (FDR = 0.0479, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00356.1 (PSMA1, PSMA4; 2/33); huMAP3_09656.1 (PSMA1, PSMA4; 2/64); huMAP3_13725.1 (PSMA1, PSMA4; 2/69)

### Novelty

This module should not be claimed as a newly discovered molecular complex or pathway. The PSMA1–PSMA4 association is already represented in STRING and multiple hu.MAP proteasome complexes, and the C1QBP–PHB1 relationship is also already represented in STRING. The potentially novel aspect is the co-abundance of these known proteasome, mitochondrial, metabolic, ribosomal, and trafficking genes across bone marrow and cervix. However, the absence of additional STRING or hu.MAP links does not establish novelty, especially because co-abundance can arise from shared cell composition, broad housekeeping activity, or coordinated cellular stress. The appropriate conclusion is that the cross-tissue co-abundance pattern is a candidate observation requiring independent validation, not evidence of a novel protein complex.

**Hypothesis.** Hypothesis: this shared module reflects a general cellular maintenance state in which proteasome capacity is coordinated with mitochondrial energy production, protein synthesis, vesicle trafficking, and regulated protein turnover. PSMA1 and PSMA4 may represent the most coherent proteasome component, while CACYBP could connect protein turnover to the less-established co-abundance relationships. ATP5PB, ETFA, PHB1, and C1QBP could reflect mitochondrial or metabolic support, and RPL6 and SEC22B could reflect biosynthetic and secretory-pathway demands. A possible biological explanation is that similar mixtures of metabolically active, differentiating, or stress-responsive cells in bone marrow and cervix generate this pattern. This is a hypothesis only; the sparse network and lack of globally significant GO/KEGG enrichment do not establish a causal mechanism.

### Important genes

#### PSMA4

- **Related proteins** (co-abundance neighbors): CACYBP (0.85), ATP5PB (0.83), ETFA (0.83), C1QBP (0.82), PSMA1 (0.81); STRING partners: PSMA1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow, cervix_uterine
- **hu.MAP 3.0**: huMAP3_00356.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 20S subunit alpha 4. This gene encodes a core alpha subunit of the 20S proteosome, which is a highly ordered ring-shaped structure composed of four rings of 28 non-identical subunits. Proteasomes cleave peptides in an ATP- and ubiquitin-dependent manner. [provided by RefSeq, Aug 2016].
- **Diseases (Open Targets)**: plasma cell myeloma (0.616); mantle cell lymphoma (0.542); neoplasm (0.513); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1240
- **Why important**: PSMA4 has the strongest network connectivity in the module and links the proteasome-related pair to CACYBP, ATP5PB, ETFA, and C1QBP. It is a core alpha subunit of the proteasome, is supported by the STRING proteasome annotation (STRING SMART Proteasome subunit A N-terminal signature  Add an annotation; within-query FDR = 0.0479), and occurs in multiple hu.MAP proteasome complexes (hu.MAP huMAP3_00356.1)(hu.MAP huMAP3_09656.1)(hu.MAP huMAP3_13725.1). Its disease associations include plasma cell myeloma, mantle cell lymphoma, neoplasm, HIV infectious disease, and amyloidosis, and it has substantial literature support.
- **Conclusion**: Established evidence supports PSMA4 as the principal proteasome-related anchor of the module. It is plausible, but not established, that its co-abundance marks altered proteasome demand or proteostasis in the shared tissue context.

#### PSMA1

- **Related proteins** (co-abundance neighbors): PSMA4 (0.81); STRING partners: PSMA4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, cervix_uterine
- **hu.MAP 3.0**: huMAP3_00356.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 20S subunit alpha 1. The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent proc…
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.535); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1417
- **Why important**: PSMA1 forms the strongest known within-module molecular relationship with PSMA4 and is present with PSMA4 in the same hu.MAP proteasome complexes (hu.MAP huMAP3_00356.1)(hu.MAP huMAP3_09656.1)(hu.MAP huMAP3_13725.1). Its annotation supports proteasome-dependent protein degradation, DNA repair, apoptotic processes, and immune-related functions. It has disease associations including plasma cell myeloma, mantle cell lymphoma, neoplasm, HIV infectious disease, and amyloidosis, with substantial literature support.
- **Conclusion**: Established evidence identifies PSMA1 as a second proteasome core anchor and strengthens the interpretation of a proteostasis-related module. The module data do not establish whether PSMA1 activity is altered or whether its signal merely reflects abundance of proteasome-containing cells.

#### CACYBP

- **Related proteins** (co-abundance neighbors): PSMA4 (0.85), NNMT (0.82), RPL6 (0.80), SEC22B (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcyclin binding protein. The protein encoded by this gene is a calcyclin binding protein. It may be involved in calcium-dependent ubiquitination and subsequent proteosomal degradation of target proteins. It probably serves as a molecular bridge in ubiquitin E3 complexes and participates in the ubiquitin-mediated degradation of beta-catenin. Two alternatively spliced transcript variants encoding different isoforms have bee…
- **Diseases (Open Targets)**: esophageal disorder (0.358); gastroesophageal reflux disease (0.291); Abnormality of the skeletal system (0.262); mood disorder (0.202); major depressive disorder (0.202)
- **Europe PMC papers**: 835
- **Why important**: CACYBP is a highly connected intermediary in the module, linking PSMA4 with NNMT, RPL6, and SEC22B. Its established annotation describes a calcyclin-binding protein that may participate in calcium-dependent ubiquitination, proteasomal degradation, and beta-catenin regulation. It has low tissue specificity, cell-type enhancement in megakaryocytes, migrating cytotrophoblasts, and oocytes, disease associations involving esophageal and skeletal disorders, and substantial literature support.
- **Conclusion**: Established evidence makes CACYBP a plausible bridge between proteostasis and the other module branches. Its role as the mechanistic connector in this module remains a hypothesis because the listed STRING and hu.MAP resources do not support its module edges.

#### C1QBP

- **Related proteins** (co-abundance neighbors): PSMA4 (0.82); STRING partners: PHB1 (0.847)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in bone_marrow, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C1q binding protein. The human complement subcomponent C1q associates with C1r and C1s in order to yield the first component of the serum complement system. The protein encoded by this gene is known to bind to the globular heads of C1q molecules and inhibit C1 activation. This protein has also been identified as the p32 subunit of pre-mRNA splicing factor SF2, as well as a hyaluronic acid-binding protein. [provided by…
- **Diseases (Open Targets)**: combined oxidative phosphorylation deficiency 33 (0.762); Mitochondrial disorder due to a defect in mitochondrial protein synthesis (0.527); neurodegenerative disease (0.459); mitochondrial disease (0.448); cardiomyopathy (0.374)
- **Europe PMC papers**: 1690
- **Why important**: C1QBP is connected to PSMA4 in the co-abundance network and to PHB1 in STRING, providing a link between the proteasome-associated portion and a mitochondrial or membrane-associated relationship. Its established functions include complement regulation, immune response, mitochondrial RNA catabolism, and regulation of inflammatory signaling. It is annotated as secreted to blood, is detected in both tissues, has broad cell-type enhancement, has associations with mitochondrial disorders and cardiomyopathy, and has extensive literature support.
- **Conclusion**: Established evidence supports C1QBP as a multifunctional mitochondrial and complement-related protein with a known PHB1 association. Its position as a bridge between proteostasis and mitochondrial or immune biology in this module is suggestive but not proven.

#### PHB1

- **Related proteins** (co-abundance neighbors): ATP5PB (0.83); STRING partners: C1QBP (0.847)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prohibitin 1. This gene is evolutionarily conserved, and its product is proposed to play a role in human cellular senescence and tumor suppression. Antiproliferative activity is reported to be localized to the 3' UTR, which is proposed to function as a trans-acting regulatory RNA. Several pseudogenes of this gene have been identified. Alternative splicing results in multiple transcript variants. [provided by Re…
- **Diseases (Open Targets)**: coronary artery disorder (0.458); myocardial ischemia (0.454); hypertensive disorder (0.396); heart disorder (0.343); asthma (0.339)
- **Europe PMC papers**: 1249
- **Why important**: PHB1 is connected to ATP5PB in the module and to C1QBP in STRING, forming the module's most evident mitochondrial or membrane-associated branch. Its established annotations include mitochondrion organization, transcriptional regulation, osteoblast differentiation, immunoglobulin production, and signal transduction. It is detected in both tissues, has low tissue specificity, is annotated as intracellular and membrane-associated, has cardiovascular and asthma-related disease associations, and has substantial literature support.
- **Conclusion**: Established evidence supports PHB1 as a broadly expressed mitochondrial and regulatory protein within the module. The hypothesis that PHB1 coordinates mitochondrial support for proteasome activity in this shared tissue pattern is not established by the available interaction evidence.

## Module 4

**Tissue pair**: bone_marrow and cervix_uterine  
**Genes (7)**: ECI1, NQO2, PYCR1, PHB2, PRDX3, ALYREF, TMEM109

### Function

The module does not have a GO or KEGG term that passes global correction, and STRING provides neither functional enrichment nor high-confidence pairwise interactions. Therefore, its function should be inferred cautiously from the gene identities and co-abundance structure rather than assigned from enrichment. NQO2 is the network hub and links genes involved in quinone reduction, mitochondrial antioxidant defense, proline and amino-acid metabolism, fatty-acid beta-oxidation, RNA export, and nuclear-membrane or cell-death regulation. PRDX3, PHB2, PYCR1, and ECI1 support a mitochondrial, redox, and metabolic interpretation, while ALYREF contributes a nuclear RNA-processing component and TMEM109 contributes an endoplasmic-reticulum and nuclear-membrane stress-response component. Overall, the module is most consistent with coordinated cellular maintenance involving redox control, mitochondrial function, intermediary metabolism, and stress adaptation, but this remains an interpretation rather than a globally validated pathway assignment.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and the individual annotations are intracellular or membrane-associated. Most genes have low tissue specificity, suggesting a broadly expressed cellular program rather than a strongly tissue-restricted one. All module genes show some cell-type enhancement, with recurring annotations in hepatocytes and trophoblast-related cells, while ALYREF is tissue enhanced in bone marrow. Most genes have low immune-cell specificity, although NQO2 is immune-cell enhanced in neutrophils and PYCR1 is enhanced in memory B cells. The module is detected at the protein level throughout bone marrow and nearly throughout cervix, so the shared signal is unlikely to be explained by secretion alone. Because several genes are broadly expressed and cell-type patterns span multiple lineages, the shared module may reflect a conserved intracellular state or shared cellular composition rather than a bone-marrow- or cervix-specific biological pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING reports no high-confidence interaction among the module members and no supplementary STRING enrichment. This means the co-abundance relationships are not simply a recovery of established STRING protein associations, although lack of a STRING edge does not demonstrate biological independence. hu.MAP identifies the PHB2–TMEM109 pair within complex huMAP3_10725.1 (hu.MAP huMAP3_10725.1). That complex also contains proteins associated with organelle membranes, mitochondria, membrane contact sites, ion handling, and endoplasmic-reticulum biology, providing limited curated support for a membrane-organelle context. However, only the PHB2–TMEM109 membership from this module is directly represented in the cited complex, so the complex evidence should not be generalized to the entire module.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10725.1 (PHB2, TMEM109; 2/59)

### Novelty

The shared co-abundance module appears potentially novel as a cross-tissue network observation because it has no high-confidence STRING interactions, no STRING functional enrichment, no globally corrected GO or KEGG term, and only partial representation in one hu.MAP complex. Nevertheless, it should not be called a newly discovered molecular complex or pathway. The constituent genes have established individual functions and substantial prior literature, and several pairings may reflect coordinated expression, common cellular state, or indirect biology rather than an undocumented physical interaction. The strongest defensible claim is that this particular cross-tissue co-abundance organization is not explained by the supplied curated interaction resources; confirmation would require replication, cell-composition adjustment, independent cohorts, perturbation, or biochemical testing.

**Hypothesis.** Hypothesis: the module marks a conserved intracellular stress-adaptation program in which NQO2-linked redox capacity is coordinated with mitochondrial antioxidant protection through PRDX3, mitochondrial organization and signaling through PHB2, proline and redox metabolism through PYCR1, lipid oxidation through ECI1, membrane-stress and cell-death regulation through TMEM109, and RNA export or transcript handling through ALYREF. In bone marrow and cervix, this program may be expressed by mixtures of broadly distributed progenitor, epithelial, stromal, or immune-related cells and may therefore appear as a shared co-abundance module without forming a single physical complex. This is a mechanistic hypothesis, not an experimentally established causal model.

### Important genes

#### NQO2

- **Related proteins** (co-abundance neighbors): PRDX3 (0.97), PYCR1 (0.94), TMEM109 (0.89), ALYREF (0.86), ECI1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-ribosyldihydronicotinamide:quinone dehydrogenase 2. This gene encodes a member of the thioredoxin family of enzymes. It is a cytosolic and ubiquitously expressed flavoprotein that catalyzes the two-electron reduction of quinone substrates and uses dihydronicotinamide riboside as a reducing coenzyme. Mutations in this gene have been associated with neurodegenerative diseases and several cancers. Alternative splicing results in multiple transcript va…
- **Diseases (Open Targets)**: neurodegenerative disease (0.374); intermediate coronary syndrome (0.102); Alzheimer disease (0.064); autosomal dominant macrothrombocytopenia (0.058); hereditary thrombocytopenia with normal platelets (0.057)
- **Europe PMC papers**: 1310
- **Why important**: NQO2 is the central network hub, connecting the other module components in the co-abundance graph. Its established quinone-reduction and thioredoxin-family function provides a plausible redox anchor for the module. It is broadly expressed, is enhanced in neutrophils, and has disease associations spanning neurodegenerative disease, thrombocytopenia, and cancer. Its literature base is substantial, making it the most informative entry point for testing whether the module reflects redox and stress biology.
- **Conclusion**: Established evidence supports NQO2 as the network-organizing gene and a cytosolic quinone-redox enzyme. The conclusion that it drives the shared module, rather than merely tracking the same cellular state, is a hypothesis requiring perturbation or longitudinal evidence.

#### PRDX3

- **Related proteins** (co-abundance neighbors): NQO2 (0.97), PHB2 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Mitochondria; IHC detected in bone_marrow, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peroxiredoxin 3. This gene encodes a mitochondrial protein with antioxidant function. The protein is similar to the C22 subunit of Salmonella typhimurium alkylhydroperoxide reductase, and it can rescue bacterial resistance to alkylhydroperoxide in E. coli that lack the C22 subunit. The human and mouse genes are highly conserved, and they map to the regions syntenic between mouse and human chromosomes. Sequence com…
- **Diseases (Open Targets)**: spinocerebellar ataxia, autosomal recessive 32 (0.653); corneal dystrophy, punctiform and polychromatic pre-descemet (0.571); autosomal recessive cerebellar ataxia (0.268); neurodegenerative disease (0.257); hereditary disease (0.191)
- **Europe PMC papers**: 2613
- **Why important**: PRDX3 links directly to NQO2 and PHB2 and is a mitochondrial antioxidant protein. Its established roles include response to oxidative stress, mitochondrial organization, and myeloid-cell differentiation. It is detected in both tissues and has broad disease relevance, including inherited neurologic and ocular disorders.
- **Conclusion**: Established evidence supports PRDX3 as a mitochondrial redox component that strengthens the oxidative-stress interpretation. It is plausible that PRDX3 couples the NQO2 signal to mitochondrial protection, but the co-abundance data do not establish that causal direction.

#### PHB2

- **Related proteins** (co-abundance neighbors): PRDX3 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, cervix_uterine
- **hu.MAP 3.0**: huMAP3_10725.1
- **Function (MyGene.info)**: prohibitin 2. Enables several functions, including protein C-terminus binding activity; protein N-terminus binding activity; and protein dimerization activity. Involved in several processes, including defense response to virus; positive regulation of cell cycle phase transition; and regulation of transcription, DNA-templated. Located in several cellular components, including cell surface; mitochondrial membrane…
- **Diseases (Open Targets)**: breast cancer (0.101); breast carcinoma (0.101); neoplasm (0.100); non-small cell lung carcinoma (0.096); colorectal carcinoma (0.085)
- **Europe PMC papers**: 2714
- **Why important**: PHB2 connects to PRDX3 and is one of the two module genes represented in huMAP complex huMAP3_10725.1 (hu.MAP huMAP3_10725.1). It is a mitochondrial and membrane-associated prohibitin with established roles in mitophagy, mitochondrial organization, transcriptional regulation, and immune-related biology. Its extensive literature and cancer associations make it an important candidate for linking cellular maintenance to disease-relevant states.
- **Conclusion**: Established evidence supports PHB2 as a mitochondrial organization and quality-control component with curated complex membership. Its proposed role as the physical bridge between the module and the huMAP complex is suggestive but not demonstrated, because the remaining module relationships lack STRING support.

#### PYCR1

- **Related proteins** (co-abundance neighbors): NQO2 (0.94); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in bone_marrow, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyrroline-5-carboxylate reductase 1. This gene encodes an enzyme that catalyzes the NAD(P)H-dependent conversion of pyrroline-5-carboxylate to proline. This enzyme may also play a physiologic role in the generation of NADP(+) in some cell types. The protein forms a homopolymer and localizes to the mitochondrion. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013].
- **Diseases (Open Targets)**: autosomal recessive cutis laxa type 2B (0.822); PYCR1-related de Barsy syndrome (0.774); cutis laxa (0.644); hereditary disease (0.521); geroderma osteodysplastica (0.374)
- **Europe PMC papers**: 1530
- **Why important**: PYCR1 is connected to the NQO2 hub and catalyzes mitochondrial proline biosynthesis while influencing NADP-positive balance and oxidative-stress responses. It is tissue enhanced in pancreas and salivary gland, cell-type enhanced in several progenitor and epithelial populations, and associated with inherited connective-tissue disorders. This gives the module a defined metabolic and redox link beyond generic mitochondrial annotation.
- **Conclusion**: Established evidence supports PYCR1 as a mitochondrial proline and redox-metabolism enzyme. Its inclusion suggests that the module may couple antioxidant capacity to biosynthetic or metabolic demand, but the shared-tissue network cannot establish that this metabolic coupling is functionally active.

#### ALYREF

- **Related proteins** (co-abundance neighbors): NQO2 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in bone_marrow, cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Aly/REF export factor. The protein encoded by this gene is a heat stable, nuclear protein and functions as a molecular chaperone. It is thought to regulate dimerization, DNA binding, and transcriptional activity of basic region-leucine zipper (bZIP) proteins. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.542); dengue disease (0.370); neoplasm (0.103); non-small cell lung carcinoma (0.102); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 1636
- **Why important**: ALYREF connects to NQO2 and is tissue enhanced in bone marrow, with cell-type enhancement in erythrocyte and megakaryocyte progenitor populations. Its established function in nuclear RNA export and mRNA handling introduces a transcript-processing dimension that is not captured by the mitochondrial genes alone. Its association with osteoblast differentiation and a substantial literature base makes it particularly relevant to the bone-marrow component.
- **Conclusion**: Established evidence supports ALYREF as a nuclear RNA-export factor and a plausible marker of bone-marrow progenitor activity. Its presence may indicate coordinated transcript handling during cellular stress or differentiation, but that connection to the mitochondrial-redox genes remains a hypothesis.
