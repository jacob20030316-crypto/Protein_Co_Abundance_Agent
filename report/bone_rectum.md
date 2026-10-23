# Conserved co-abundance modules: bone and rectum

## Module 0

**Tissue pair**: bone and rectum  
**Genes (25)**: SLC3A2, SLC1A5, ARHGEF1, CPSF7, DHX36, EPB41L2, FAM120A, FAM91A1, FLOT1, EIF5, LBR, CHCHD3, IMMT, NES, NSUN2, NUBP2, OXA1L, RFTN1, POLR1C, SLC12A2, TUBA1C, TGM2, TRNT1, VDAC2, WASHC5

### Function

The strongest functional interpretation is a conserved cellular response to double-stranded RNA, supported by the globally corrected GO terms (GO:BP response to exogenous dsRNA; q_global = 0.0167) and (GO:BP response to dsRNA; q_global = 0.0248). Both terms converge on DHX36, FLOT1, RFTN1, and SLC3A2, making this the primary module-level evidence rather than a nominal or within-module-only signal. The module also contains coherent supporting processes involving RNA maturation and translation, membrane transport and trafficking, cytoskeletal organization, mitochondrial membrane organization, and amino-acid transport. These supporting annotations are biologically compatible with antiviral sensing and cellular stress responses, but they are not globally significant GO or KEGG evidence here. The sparse network is not a single densely connected complex; instead, it appears to combine several functional neighborhoods linked by co-abundance. Thus, the safest interpretation is a dsRNA-responsive cellular-state module with accompanying membrane, RNA-processing, metabolic, and mitochondrial features.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: HPA identifies only a small secreted component, and most proteins are intracellular or membrane-associated. It is also not strongly blood-cell specific overall, because most genes have low immune-cell specificity. Nevertheless, neutrophil-associated signals recur among the single-cell annotations, with additional lymphoid, plasmacytoid dendritic-cell, B-cell, T-cell, and NK-cell associations for selected genes. The module therefore could partly reflect shared immune or stromal cell populations in bone and rectum, but the evidence does not support treating it as a simple blood-contamination signature. Many genes have broad tissue or cell-type profiles and functions typical of general cellular maintenance, including RNA processing, translation, cytoskeletal organization, membrane transport, and mitochondrial biology. Rectal protein detection is common among the module members, whereas the bone comparison has no matching HPA tissue protein dataset, so tissue-level protein support is asymmetric and should be interpreted cautiously.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP response to exogenous dsRNA | 0.0167 | DHX36, FLOT1, RFTN1, SLC3A2 |
| GO:BP response to dsRNA | 0.0248 | DHX36, FLOT1, RFTN1, SLC3A2 |

### STRING and hu.MAP

STRING provides no functional enrichment for the module. Its high-confidence evidence is limited to a mitochondrial interaction neighborhood involving CHCHD3, IMMT, OXA1L, and VDAC2, plus the transporter relationship between SLC1A5 and SLC3A2. These relationships support genuine mitochondrial and amino-acid-transport substructures, but the lack of broader STRING connectivity argues against interpreting the whole module as a previously defined physical complex. hu.MAP independently supports several small or partial complex overlaps: NSUN2 with TRNT1 in (hu.MAP huMAP3_12301.1) and (hu.MAP huMAP3_12727.1), TUBA1C with NUBP2 in (hu.MAP huMAP3_09233.1), (hu.MAP huMAP3_10475.1), and (hu.MAP huMAP3_10665.1), VDAC2 with CHCHD3 in (hu.MAP huMAP3_10725.1), and DHX36 with FAM120A in (hu.MAP huMAP3_05807.1). Because each complex overlap contains only a small subset of the module and several complexes have low or intermediate confidence, hu.MAP supports local biological coherence rather than a single unified complex. The agreement between STRING and hu.MAP is strongest for the mitochondrial neighborhood, while the dsRNA-response interpretation is driven primarily by GO evidence and gene annotations rather than by known physical interactions.

**STRING interactions (score >= 0.7)**: 4 of 300 gene pairs: CHCHD3–IMMT (0.999); IMMT–OXA1L (0.854); IMMT–VDAC2 (0.708); SLC1A5–SLC3A2 (0.894)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12301.1 (NSUN2, TRNT1; 2/26); huMAP3_12727.1 (NSUN2, TRNT1; 2/32); huMAP3_09233.1 (TUBA1C, NUBP2; 2/34); huMAP3_10475.1 (TUBA1C, NUBP2; 2/39); huMAP3_10665.1 (TUBA1C, NUBP2; 2/42); huMAP3_10725.1 (VDAC2, CHCHD3; 2/59); huMAP3_05807.1 (DHX36, FAM120A; 2/81)

### Novelty

The module should not be called entirely novel on the basis of database absence. Several component relationships are already established in STRING or hu.MAP, and the individual genes have substantial prior literature and disease annotation. What may be new is the co-abundance configuration that brings dsRNA-response genes together with mitochondrial, transport, RNA-processing, and cytoskeletal components across bone and rectum. The globally corrected enrichment in (GO:BP response to exogenous dsRNA; q_global = 0.0167) and (GO:BP response to dsRNA; q_global = 0.0248) gives this cross-tissue association stronger support than an isolated nominal observation. However, the sparse network, limited database overlap, broad expression of many members, and possible contribution from shared immune or stromal cell populations mean that novelty remains a hypothesis requiring replication in independent cohorts, cell-composition adjustment, and ideally perturbation or longitudinal evidence. The defensible conclusion is a potentially novel cross-tissue co-abundance state built from partly known biology, not proof of a new molecular complex or pathway.

**Hypothesis.** Hypothesis: a shared cell state in bone and rectum exposes cells to endogenous or exogenous double-stranded-RNA-related stress, engaging DHX36 and raft-associated signaling involving RFTN1 and FLOT1. SLC1A5 and SLC3A2 may support the metabolic and membrane response, while mitochondrial structural components represented by IMMT, CHCHD3, OXA1L, and VDAC2 may maintain or remodel mitochondrial function during that response. RNA-processing and translation-related genes could tune gene expression and protein production during the state. This model predicts coordinated changes in dsRNA sensing, membrane trafficking, amino-acid availability, and mitochondrial organization, but the co-abundance data alone do not establish causality or the direction of regulation.

### Important genes

#### RFTN1

- **Related proteins** (co-abundance neighbors): FAM120A (0.88), NES (0.84), EPB41L2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: raftlin, lipid raft linker 1. Enables double-stranded RNA binding activity. Involved in B cell receptor signaling pathway; membrane raft assembly; and positive regulation of growth rate. Acts upstream of or within dsRNA transport; response to exogenous dsRNA; and toll-like receptor 3 signaling pathway. Located in endosome; membrane raft; and plasma membrane. Part of protein-containing complex. [provided by Alliance of Genome R…
- **Diseases (Open Targets)**: neurodegenerative disease (0.486); COVID-19 (0.299); lysosomal storage disease (0.288); digestive system disorder (0.282); bone Paget disease (0.230)
- **Europe PMC papers**: 444
- **Why important**: RFTN1 is one of the module's central connectors, linking FAM120A with NES and EPB41L2. It is one of the four genes in both globally corrected dsRNA-response terms (GO:BP response to exogenous dsRNA; q_global = 0.0167) and (GO:BP response to dsRNA; q_global = 0.0248). Its annotation directly includes dsRNA binding, dsRNA transport, membrane-raft assembly, and Toll-like receptor three signaling. Its lymphoid tissue and several immune-cell-associated annotations make it particularly relevant to distinguishing a true conserved response from a shared cell-composition effect. Its disease links include immune, digestive, bone, and viral disease contexts, while its literature volume is moderate.
- **Conclusion**: Established: RFTN1 is the strongest functional bridge between the significant dsRNA signal and membrane or immune signaling in this module. Hypothesis: it may help organize a membrane-raft response to dsRNA in the shared bone-rectum state. The cell-composition explanation remains plausible and must be tested.

#### DHX36

- **Related proteins** (co-abundance neighbors): FAM120A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_05807.1
- **Function (MyGene.info)**: DEAH-box helicase 36. This gene is a member of the DEAH-box family of RNA-dependent NTPases which are named after the conserved amino acid sequence Asp-Glu-Ala-His in motif II. The protein encoded by this gene has been shown to enhance the deadenylation and decay of mRNAs with 3'-UTR AU-rich elements (ARE-mRNA). The protein has also been shown to resolve into single strands the highly stable tetramolecular DNA configur…
- **Diseases (Open Targets)**: neurodegenerative disease (0.522); Abnormality of the skeletal system (0.517); Epiretinal membrane (0.388); degeneration of macula and posterior pole (0.383); retinal disorder (0.372)
- **Europe PMC papers**: 1293
- **Why important**: DHX36 is a high-connectivity module member through FAM120A and is present in both (GO:BP response to exogenous dsRNA; q_global = 0.0167) and (GO:BP response to dsRNA; q_global = 0.0248). It is an RNA helicase with documented roles in RNA metabolism, regulation of gene expression, and resolution of stable nucleic-acid structures. It also appears with FAM120A in the hu.MAP overlap (hu.MAP huMAP3_05807.1). Its annotations include myeloid dendritic-cell cytokine regulation and an abnormality of the skeletal system among disease associations, making it relevant to both immune signaling and the bone tissue context. Its literature volume is substantial.
- **Conclusion**: Established: DHX36 is a plausible nucleic-acid-processing component of the globally supported dsRNA-response signature. Hypothesis: it may act upstream or alongside RFTN1 to shape the transcriptional and translational response to dsRNA. The module does not demonstrate direct physical coupling between DHX36 and the other significant-term genes.

#### SLC3A2

- **Related proteins** (co-abundance neighbors): SLC1A5 (0.85), VDAC2 (0.81); STRING partners: SLC1A5 (0.894)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 3 member 2. This gene is a member of the solute carrier family and encodes a cell surface, transmembrane protein. The protein exists as the heavy chain of a heterodimer, covalently bound through di-sulfide bonds to one of several possible light chains. The encoded transporter plays a role in regulation of intracellular calcium levels and transports L-type amino acids. Alternatively spliced transcript variants…
- **Diseases (Open Targets)**: sensorineural hearing loss disorder (0.370); neurodegenerative disease (0.324); neoplasm (0.117); breast cancer (0.113); breast carcinoma (0.110)
- **Europe PMC papers**: 6815
- **Why important**: SLC3A2 is present in both (GO:BP response to exogenous dsRNA; q_global = 0.0167) and (GO:BP response to dsRNA; q_global = 0.0248) and forms the module's clearest STRING-supported transporter pair with SLC1A5. It is a cell-surface transporter heavy chain involved in amino-acid transport and calcium-related regulation, and its partners provide a plausible metabolic support arm for an activated cellular state. It has broad disease relevance and the largest literature volume among the selected genes. Its HPA profile is not strongly immune-specific, which helps separate the dsRNA signal from a purely blood-cell interpretation.
- **Conclusion**: Established: SLC3A2 contributes directly to the significant dsRNA-associated gene set and has a known transporter relationship with SLC1A5. Hypothesis: the transporter pair may supply metabolic support or alter membrane signaling during the shared response state. Its presence does not prove that amino-acid transport drives dsRNA sensing.

#### IMMT

- **Related proteins** (co-abundance neighbors): CHCHD3 (0.86), FLOT1 (0.82), NES (0.80); STRING partners: CHCHD3 (0.999), OXA1L (0.854), VDAC2 (0.708)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inner membrane mitochondrial protein. Enables RNA binding activity. Involved in cristae formation. Located in mitochondrial inner membrane. Part of MICOS complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); multinodular goiter (0.196); alcohol drinking (0.190); breast cancer (0.094); neoplasm (0.087)
- **Europe PMC papers**: 933
- **Why important**: IMMT is a mitochondrial inner-membrane scaffold and a module connector to CHCHD3, NES, and FLOT1. STRING supports its relationships with CHCHD3, OXA1L, and VDAC2, and hu.MAP independently places VDAC2 with CHCHD3 in (hu.MAP huMAP3_10725.1). Its established role in cristae formation gives the mitochondrial substructure a coherent mechanistic interpretation. It has substantial literature and disease associations involving mitochondrial or neurological contexts.
- **Conclusion**: Established: IMMT anchors the best-supported mitochondrial neighborhood in the module and is consistent with cristae organization. Hypothesis: mitochondrial remodeling may be coupled to the dsRNA-associated state and may help determine its energetic or apoptotic consequences. The data do not establish whether mitochondrial changes are causes, consequences, or correlates of the response.

#### CHCHD3

- **Related proteins** (co-abundance neighbors): IMMT (0.86); STRING partners: IMMT (0.999)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_10725.1
- **Function (MyGene.info)**: coiled-coil-helix-coiled-coil-helix domain containing 3. The protein encoded by this gene is an inner mitochondrial membrane scaffold protein. Absence of the encoded protein affects the structural integrity of mitochondrial cristae and leads to reductions in ATP production, cell growth, and oxygen consumption. This protein is part of the mitochondrial contact site and cristae organizing system (MICOS). Several transcript variants encoding different isof…
- **Diseases (Open Targets)**: neurodegenerative disease (0.537); smoking initiation (0.414); intelligence (0.385); insomnia (0.362); mathematical ability (0.312)
- **Europe PMC papers**: 549
- **Why important**: CHCHD3 has a direct high-confidence STRING relationship with IMMT and is part of the hu.MAP mitochondrial overlap (hu.MAP huMAP3_10725.1). It is an inner-membrane scaffold involved in MICOS-related cristae organization, mitochondrial fusion, and mitochondrial structure. Its tissue-enhanced skeletal-muscle and tongue profile, together with rectal detection, makes it relevant to a cross-tissue structural or metabolic state rather than a purely immune explanation. Its disease and neurological associations provide additional biological context, although they do not specifically link it to dsRNA response.
- **Conclusion**: Established: CHCHD3 is a well-supported mitochondrial structural member of the module through both STRING and hu.MAP. Hypothesis: it may coordinate mitochondrial architecture with the stress response represented by the dsRNA-associated genes. Direct functional coupling to RFTN1 or DHX36 remains unproven.

#### FLOT1

- **Related proteins** (co-abundance neighbors): IMMT (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: flotillin 1. This gene encodes an protein that localizes to the caveolae, which are small domains on the inner cell membranes. This protein plays a role in vesicle trafficking and cell morphology. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016].
- **Diseases (Open Targets)**: neurodegenerative disease (0.332); gastric cancer (0.101); hepatocellular carcinoma (0.101); neoplasm (0.097); lung adenocarcinoma (0.093)
- **Europe PMC papers**: 3298
- **Why important**: FLOT1 is included in both globally corrected dsRNA-response terms (GO:BP response to exogenous dsRNA; q_global = 0.0167) and (GO:BP response to dsRNA; q_global = 0.0248) and connects to IMMT in the module graph. Its annotated roles in membrane domains, vesicle trafficking, receptor internalization, and cell-junction organization provide a plausible membrane-trafficking link between dsRNA signaling and the mitochondrial neighborhood. HPA associates it with neutrophils and other cell types, so it is also informative for evaluating possible cell-composition effects. Its literature volume is substantial.
- **Conclusion**: Established: FLOT1 is a significant-term gene with membrane-trafficking functions and a module connection to the mitochondrial component. Hypothesis: flotillin-dependent membrane organization may facilitate receptor or vesicle processes during the shared dsRNA-related state. The available evidence does not identify the specific receptor or trafficking event involved.

## Module 1

**Tissue pair**: bone and rectum  
**Genes (48)**: AATF, ABHD10, AGPS, ALDH2, ANP32E, HSPA5, MTHFD1L, CANX, HADHB, MMGT1, ETFA, SHMT2, HSD17B10, HSDL2, HYOU1, ITGA2, MARCHF5, MISP, MRE11, MTX1, NDUFAF4, OCIAD1, DDOST, PYCR1, GATAD2A, PPIC, PRDX3, PRDX4, PSMD13, PSMG1, PTCD3, MRPL4, MRPL19, MRPL48, RRP1, RRS1, MRPS23, MRPS31, SLC25A13, SCP2, SERPINH1, SSR1, STXBP2, TFRC, DNAJC19, TRAP1, UGGT1, VIRMA

### Function

The module is most strongly interpreted as a mitochondrial proteostasis and bioenergetic-support program. The primary evidence is the global enrichment of mitochondrial protein-containing complexes (GO:CC mitochondrial protein-containing complex; q_global = 0.00117), mitochondria (GO:CC mitochondrion; q_global = 0.00181), mitochondrial matrix (GO:CC mitochondrial matrix; q_global = 0.00394), mitochondrial inner membrane (GO:CC mitochondrial inner membrane; q_global = 0.0158), organellar ribosome (GO:CC organellar ribosome; q_global = 0.0239), mitochondrial ribosome (GO:CC mitochondrial ribosome; q_global = 0.0239), mitochondrial membrane (GO:CC mitochondrial membrane; q_global = 0.0341), and organelle inner membrane (GO:CC organelle inner membrane; q_global = 0.0344). The genes include a coherent mitochondrial translation core composed of MRPL19, MRPL4, MRPL48, MRPS23, MRPS31, and PTCD3, together with genes involved in fatty-acid oxidation, redox control, one-carbon metabolism, mitochondrial transport, membrane organization, and protein quality control. The ER-related STRING terms (STRING NetworkNeighborAL Mixed, incl. Endoplasmic reticulum protein-containing complex, and Cotranslational protein targeting to membrane; within-query FDR = 0.0017), (STRING NetworkNeighborAL Protein processing in endoplasmic reticulum, and Protein export; within-query FDR = 0.0047), and (STRING NetworkNeighborAL Mixed, incl. Protein targeting to ER, and Oligosaccharyltransferase complex; within-query FDR = 0.0136) indicate a connected secondary program of cotranslational targeting, glycoprotein processing, folding, and export. Thus, the module is better viewed as coordinated mitochondrial and ER proteostasis rather than as a narrowly defined single biochemical pathway. The absence of a specific biological-process enrichment among the primary terms limits pathway-level resolution, but it does not undermine the strong cellular-compartment interpretation.

**Cell composition.** The HPA profile does not support a module dominated by plasma or secreted proteins, and it does not support a broadly blood-cell-specific module. Most genes have low tissue specificity and low immune-cell specificity, while many are cell-type enhanced across diverse epithelial, hepatic, reproductive, muscle, and progenitor populations. The secreted-gene annotation is present for a minority of the module, including TFRC as a blood-secreted protein, but the module is principally intracellular. The enrichment of hepatocyte-associated genes and the presence of liver-enhanced metabolic genes may reflect shared metabolic cell states rather than a bone-rectum-specific mechanism. The broad housekeeping-like distribution, together with the mitochondrial ribosomal and ER quality-control components, also raises the possibility that the conserved signal reflects common cellular stress, biosynthetic demand, or shared cell types in the sampled tissues. Rectal protein detection is widespread in HPA, whereas the bone comparison has no matching HPA tissue data, so tissue-protein support is asymmetric and cannot establish bone-specific localization.

**GO/KEGG enrichment**: 8 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrial protein-containing complex | 0.00117 | DNAJC19, HADHB, HSD17B10, MRPL19, MRPL4, MRPL48, MRPS23, MRPS31, MTX1, PTCD3 |
| GO:CC mitochondrion | 0.00181 | ABHD10, AGPS, ALDH2, CANX, DNAJC19, ETFA, HADHB, HSD17B10, HSDL2, HSPA5, HYOU1, MARCHF5, MRPL19, MRPL4, MRPL48, MRPS23, MRPS31, MTHFD1L, MTX1, NDUFAF4, OCIAD1, PRDX3, PTCD3, PYCR1, SCP2, SHMT2, SLC25A13, TRAP1 |
| GO:CC mitochondrial matrix | 0.00394 | ABHD10, ALDH2, DNAJC19, ETFA, HADHB, HSD17B10, MRPL19, MRPL4, MRPL48, MRPS23, MRPS31, MTHFD1L, PRDX3, PTCD3, PYCR1, SHMT2, TRAP1 |
| GO:CC mitochondrial inner membrane | 0.0158 | DNAJC19, HADHB, MRPL19, MRPL4, MRPL48, MRPS23, MRPS31, MTX1, NDUFAF4, PTCD3, SHMT2, SLC25A13, TRAP1 |
| GO:CC organellar ribosome | 0.0239 | MRPL19, MRPL4, MRPL48, MRPS23, MRPS31, PTCD3 |
| GO:CC mitochondrial ribosome | 0.0239 | MRPL19, MRPL4, MRPL48, MRPS23, MRPS31, PTCD3 |
| GO:CC mitochondrial membrane | 0.0341 | CANX, DNAJC19, HADHB, MARCHF5, MRPL19, MRPL4, MRPL48, MRPS23, MRPS31, MTX1, NDUFAF4, PTCD3, SHMT2, SLC25A13, TRAP1 |
| GO:CC organelle inner membrane | 0.0344 | DNAJC19, HADHB, MRPL19, MRPL4, MRPL48, MRPS23, MRPS31, MTX1, NDUFAF4, PTCD3, SHMT2, SLC25A13, TRAP1 |

### STRING and hu.MAP

STRING provides established relationships within several coherent substructures. The mitochondrial ribosomal genes MRPL19, MRPL4, MRPL48, MRPS23, MRPS31, and PTCD3 form a dense known interaction group, with particularly strong links among the small-subunit and large-subunit-associated proteins (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0011), (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.0011), (STRING Component Mitochondrion; within-query FDR = 0.0016), (STRING Component Mitochondrial matrix; within-query FDR = 0.0016), (STRING Keyword Mitochondrion; within-query FDR = 0.0022), (STRING Component Mitochondrial inner membrane; within-query FDR = 0.0067), (STRING COMPARTMENTS Mitochondrial ribosome; within-query FDR = 0.014), (STRING Component Mitochondrial ribosome; within-query FDR = 0.0189), and (STRING Component Mitochondrial membrane; within-query FDR = 0.0189). A metabolic branch links ETFA, HADHB, HSD17B10, HSDL2, SCP2, and related mitochondrial or peroxisomal proteins. A separate ER branch links CANX, HSPA5, HYOU1, UGGT1, DDOST, SSR1, and related quality-control proteins (STRING NetworkNeighborAL Mixed, incl. Endoplasmic reticulum protein-containing complex, and Cotranslational protein targeting to membrane; within-query FDR = 0.0017), (STRING NetworkNeighborAL Protein processing in endoplasmic reticulum, and Protein export; within-query FDR = 0.0047), (STRING NetworkNeighborAL Mixed, incl. Protein targeting to ER, and Oligosaccharyltransferase complex; within-query FDR = 0.0136), and (STRING Keyword Chaperone; within-query FDR = 0.0196). The hu.MAP evidence independently supports partial mitochondrial small- and large-subunit complexes (hu.MAP huMAP3_05954.1), (hu.MAP huMAP3_06439.1), (hu.MAP huMAP3_06589.1), (hu.MAP huMAP3_05807.1), as well as ER chaperone complexes (hu.MAP huMAP3_07455.1), antioxidant cooperation (hu.MAP huMAP3_12666.1), proteasome-associated complexes (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1), and a metabolic complex containing TRAP1 and MTHFD1L (hu.MAP huMAP3_13468.1). These results show that important portions of the module recapitulate known molecular machinery. They support biological coherence, but they also indicate that the module is assembled from several known submodules rather than representing one previously characterized physical complex.

**STRING interactions (score >= 0.7)**: 38 of 1128 gene pairs: AGPS–SCP2 (0.829); CANX–DDOST (0.886); CANX–HSPA5 (0.998); CANX–HYOU1 (0.869); CANX–SSR1 (0.93); CANX–UGGT1 (0.935); DDOST–HSPA5 (0.721); DDOST–SSR1 (0.972); ETFA–HADHB (0.829); HADHB–HSD17B10 (0.971); HADHB–HSDL2 (0.918); HADHB–SCP2 (0.793); HSDL2–SCP2 (0.704); HSPA5–HYOU1 (0.999); HSPA5–SERPINH1 (0.747); HSPA5–TRAP1 (0.787); HSPA5–UGGT1 (0.747); HYOU1–UGGT1 (0.791); MRPL19–MRPL4 (0.999); MRPL19–MRPL48 (0.848); MRPL19–MRPS23 (0.849); MRPL19–MRPS31 (0.856); MRPL19–PSMG1 (0.86); MRPL19–PTCD3 (0.859); MRPL4–MRPL48 (0.982); MRPL4–MRPS23 (0.894); MRPL4–MRPS31 (0.885); MRPL4–PSMG1 (0.814); MRPL4–PTCD3 (0.887); MRPL4–RRP1 (0.811); MRPL48–MRPS23 (0.922); MRPL48–MRPS31 (0.894); MRPL48–PTCD3 (0.917); MRPS23–MRPS31 (0.998); MRPS23–PTCD3 (0.996); MRPS31–PTCD3 (0.999); MTHFD1L–SHMT2 (0.995); RRP1–RRS1 (0.949)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Mitochondrion (FDR = 0.0011, 24 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.0011, 16 genes); Component Mitochondrion (FDR = 0.0016, 26 genes); Component Mitochondrial matrix (FDR = 0.0016, 17 genes); NetworkNeighborAL Mixed, incl. Endoplasmic reticulum protein-containing complex, and Cotranslational protein targeting to membrane (FDR = 0.0017, 9 genes); Keyword Mitochondrion (FDR = 0.0022, 22 genes); COMPARTMENTS Intracellular organelle lumen (FDR = 0.004, 32 genes); COMPARTMENTS Intracellular membrane-bounded organelle (FDR = 0.0044, 46 genes); NetworkNeighborAL Protein processing in endoplasmic reticulum, and Protein export (FDR = 0.0047, 8 genes); Component Mitochondrial inner membrane (FDR = 0.0067, 13 genes); NetworkNeighborAL Mixed, incl. Protein targeting to ER, and Oligosaccharyltransferase complex (FDR = 0.0136, 7 genes); COMPARTMENTS Mitochondrial ribosome (FDR = 0.014, 6 genes); Component Mitochondrial ribosome (FDR = 0.0189, 6 genes); Component Mitochondrial membrane (FDR = 0.0189, 14 genes); Keyword Chaperone (FDR = 0.0196, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05954.1 (MRPS31, PTCD3, MRPS23; 3/28); huMAP3_06439.1 (MRPL19, MRPL48, MRPL4; 3/57); huMAP3_06589.1 (MRPL19, MRPL48, MRPL4; 3/79); huMAP3_05807.1 (MRPS31, PTCD3, MRPS23; 3/81); huMAP3_07455.1 (HSPA5, HYOU1; 2/4); huMAP3_12666.1 (PRDX3, PRDX4; 2/5); huMAP3_04652.1 (MRPL19, MRPL4; 2/30); huMAP3_10725.1 (TFRC, MMGT1; 2/59); huMAP3_06550.1 (MRPL19, MRPL4; 2/62); huMAP3_09656.1 (PSMG1, PSMD13; 2/64); huMAP3_13725.1 (PSMG1, PSMD13; 2/69); huMAP3_07939.1 (MRPL19, MRPL4; 2/68); huMAP3_08458.1 (MRPL19, MRPL4; 2/70); huMAP3_09113.1 (MRPL19, MRPL4; 2/72); huMAP3_09483.1 (MRPL19, MRPL4; 2/74); huMAP3_09327.1 (SERPINH1, HYOU1; 2/93); huMAP3_13468.1 (TRAP1, MTHFD1L; 2/99)

### Novelty

The module should not be called a wholly new molecular complex or a newly discovered mitochondrial pathway. Its mitochondrial ribosomal, ER chaperone, redox, and metabolic components are already represented in STRING and hu.MAP, and many individual genes have extensive literature support. The potentially novel aspect is the conserved co-abundance relationship between these established substructures across bone and rectum, especially the way mitochondrial translation, mitochondrial metabolism, and ER quality control are coordinated in the same tissue-pair module. However, the fact sheet does not provide an external comparison against published bone-rectum co-abundance studies, replication cohorts, or unrelated tissue pairs. Therefore, novelty is plausible at the network-organization and cross-tissue level, but it is not established as a new biological mechanism. Database absence for individual edges, such as the absence of hu.MAP annotation for several genes, is insufficient evidence of novelty.

**Hypothesis.** Hypothesis: the module represents a conserved cellular adaptation that couples mitochondrial protein synthesis and energy metabolism to ER protein folding and quality control. Increased mitochondrial translational capacity, supported by the MRPL and MRPS genes and PTCD3, could maintain respiratory-chain protein production under biosynthetic or stress demands. SHMT2, MTHFD1L, HSD17B10, HADHB, ETFA, and related genes could provide one-carbon, fatty-acid, and redox-linked metabolic support. In parallel, HSPA5, HYOU1, UGGT1, CANX, DDOST, and SSR1 could limit accumulation of misfolded or improperly glycosylated proteins in the ER. This coordination could be especially relevant in cells exposed to oxidative, hypoxic, secretory, or remodeling demands, but the co-abundance data alone do not demonstrate causal regulation, directionality, or cell-type specificity.

### Important genes

#### PTCD3

- **Related proteins** (co-abundance neighbors): MRE11 (0.87), MRPL48 (0.86), UGGT1 (0.84), ANP32E (0.83), ITGA2 (0.82); STRING partners: MRPL19 (0.859), MRPL4 (0.887), MRPL48 (0.917), MRPS23 (0.996), MRPS31 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_05954.1, huMAP3_05807.1
- **Function (MyGene.info)**: pentatricopeptide repeat domain 3. Enables rRNA binding activity and ribosomal small subunit binding activity. Involved in mitochondrial translation. Located in several cellular components, including cytosol; mitochondrion; and nucleoplasm. Implicated in combined oxidative phosphorylation deficiency 51. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: combined oxidative phosphorylation deficiency 51 (0.678); mixed connective tissue disease (0.230); hereditary disease (0.193); alcohol drinking (0.110); posterior cortical atrophy (0.074)
- **Europe PMC papers**: 308
- **Why important**: PTCD3 is a high-connectivity module gene and is included in every primary mitochondrial enrichment term (GO:CC mitochondrial protein-containing complex; q_global = 0.00117) through (GO:CC organelle inner membrane; q_global = 0.0344). It binds rRNA and the mitochondrial small ribosomal subunit, participates in mitochondrial translation, and is supported by the mitochondrial ribosome complexes (hu.MAP huMAP3_05954.1) and (hu.MAP huMAP3_05807.1). Its STRING relationships with the mitochondrial ribosomal proteins are very strong, and its disease association with combined oxidative phosphorylation deficiency gives the module a direct link to mitochondrial respiratory function.
- **Conclusion**: Established evidence supports PTCD3 as a structural and functional anchor of the mitochondrial translation branch. It is a stronger module marker than a disease-specific explanation for the bone-rectum conservation. A reasonable hypothesis is that PTCD3 helps couple mitochondrial translational capacity to the broader stress and metabolic state represented by the module, but that coupling is not demonstrated by the available data.

#### MRPS23

- **Related proteins** (co-abundance neighbors): UGGT1 (0.85), MRPS31 (0.84), HSD17B10 (0.81), DNAJC19 (0.81), MARCHF5 (0.81); STRING partners: MRPL19 (0.849), MRPL4 (0.894), MRPL48 (0.922), MRPS31 (0.998), PTCD3 (0.996)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_05954.1, huMAP3_05807.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein S23. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.495); combined oxidative phosphorylation deficiency 46 (0.399); tendon sheath disorder (0.307); gout (0.204); liver disorder (0.186)
- **Europe PMC papers**: 362
- **Why important**: MRPS23 is a central connector within the mitochondrial ribosomal subnetwork and is present in all primary mitochondrial terms (GO:CC mitochondrial protein-containing complex; q_global = 0.00117) through (GO:CC organelle inner membrane; q_global = 0.0344). It has strong STRING relationships with MRPS31, PTCD3, MRPL48, MRPL4, and MRPL19 and is represented in hu.MAP mitochondrial complexes (hu.MAP huMAP3_05954.1) and (hu.MAP huMAP3_05807.1). Its annotated function in mitochondrial translation and association with combined oxidative phosphorylation deficiency make it a direct indicator of mitochondrial protein synthesis rather than a generic mitochondrial marker.
- **Conclusion**: Established evidence supports MRPS23 as a core component of the module's mitochondrial translation machinery. Its presence is consistent with coordinated expression of a mitoribosome-related program in both tissues. The data do not establish that MRPS23 is a regulatory driver or that its disease associations explain the tissue-pair pattern.

#### SHMT2

- **Related proteins** (co-abundance neighbors): MTHFD1L (0.90), TRAP1 (0.87), PSMG1 (0.84), HYOU1 (0.80); STRING partners: MTHFD1L (0.995)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine hydroxymethyltransferase 2. This gene encodes the mitochondrial form of a pyridoxal phosphate-dependent enzyme that catalyzes the reversible reaction of serine and tetrahydrofolate to glycine and 5,10-methylene tetrahydrofolate. The encoded product is primarily responsible for glycine synthesis. The activity of the encoded protein has been suggested to be the primary source of intracellular glycine. The gene which encodes th…
- **Diseases (Open Targets)**: neurodevelopmental disorder with cardiomyopathy, spasticity, and brain abnormalities (0.771); microcephaly (0.370); polymicrogyria (0.370); neurodevelopmental disorder (0.336); hereditary disease (0.192)
- **Europe PMC papers**: 2579
- **Why important**: SHMT2 connects mitochondrial structure to metabolism in the module graph and is included in several primary mitochondrial compartment terms (GO:CC mitochondrion; q_global = 0.00181), (GO:CC mitochondrial matrix; q_global = 0.00394), (GO:CC mitochondrial inner membrane; q_global = 0.0158), (GO:CC mitochondrial membrane; q_global = 0.0341), and (GO:CC organelle inner membrane; q_global = 0.0344). It catalyzes mitochondrial serine and tetrahydrofolate metabolism, supports glycine and one-carbon metabolism, and has a very strong STRING relationship with MTHFD1L. Its liver-enhanced HPA pattern and disease associations involving neurodevelopment and cardiomyopathy make it biologically informative, while its literature volume indicates that its function is well established.
- **Conclusion**: Established evidence supports SHMT2 as a metabolic support gene that may provide biosynthetic and redox-related inputs to mitochondrial function. The liver enhancement cautions that part of the shared signal could reflect metabolic cell composition rather than a bone-rectum-specific mechanism. Its proposed role as a bridge between mitochondrial translation demand and one-carbon metabolism remains a hypothesis.

#### HSPA5

- **Related proteins** (co-abundance neighbors): CANX (0.82); STRING partners: CANX (0.998), DDOST (0.721), HYOU1 (0.999), SERPINH1 (0.747), TRAP1 (0.787), UGGT1 (0.747)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_07455.1
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is a key ER chaperone and a high-confidence STRING partner of CANX and HYOU1, with additional links to UGGT1, DDOST, SERPINH1, and TRAP1. It is represented in the ER quality-control enrichment terms (STRING NetworkNeighborAL Mixed, incl. Endoplasmic reticulum protein-containing complex, and Cotranslational protein targeting to membrane; within-query FDR = 0.0017), (STRING NetworkNeighborAL Protein processing in endoplasmic reticulum, and Protein export; within-query FDR = 0.0047), (STRING NetworkNeighborAL Mixed, incl. Protein targeting to ER, and Oligosaccharyltransferase complex; within-query FDR = 0.0136), and (STRING Keyword Chaperone; within-query FDR = 0.0196) and in the hu.MAP chaperone complex (hu.MAP huMAP3_07455.1). Its established role as a master regulator of ER protein folding and homeostasis gives the module a clear stress-proteostasis component beyond the mitochondrial core.
- **Conclusion**: Established evidence supports HSPA5 as an anchor of the ER branch and as a plausible mediator of cellular protein-folding stress. Its broad tissue and cell-type distribution argues against interpreting it as a bone- or rectum-specific marker. It is plausible, but unproven, that ER stress signaling coordinates the ER branch with the mitochondrial branch.

#### UGGT1

- **Related proteins** (co-abundance neighbors): HYOU1 (0.90), MRPL48 (0.89), MRPS23 (0.85), PTCD3 (0.84), HSD17B10 (0.83), ANP32E (0.82), DDOST (0.82), OCIAD1 (0.81), SERPINH1 (0.81), PSMD13 (0.81); STRING partners: CANX (0.935), HSPA5 (0.747), HYOU1 (0.791)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UDP-glucose glycoprotein glucosyltransferase 1. UDP-glucose:glycoprotein glucosyltransferase (UGT) is a soluble protein of the endoplasmic reticulum (ER) that selectively reglucosylates unfolded glycoproteins, thus providing quality control for protein transport out of the ER.[supplied by OMIM, Oct 2009].
- **Diseases (Open Targets)**: congenital disorder of glycosylation (0.416); hypercholesterolemia, familial, 1 (0.333); connective tissue disorder (0.234); ovarian dysfunction (0.216); chronic laryngitis (0.147)
- **Europe PMC papers**: 507
- **Why important**: UGGT1 has the highest network connectivity in the supplied module and links the ER quality-control genes with several mitochondrial-associated module genes. Its known function is selective reglucosylation of unfolded glycoproteins during ER quality control, and it participates in the STRING-supported ER network with CANX, HSPA5, and HYOU1 (STRING NetworkNeighborAL Mixed, incl. Endoplasmic reticulum protein-containing complex, and Cotranslational protein targeting to membrane; within-query FDR = 0.0017), (STRING NetworkNeighborAL Protein processing in endoplasmic reticulum, and Protein export; within-query FDR = 0.0047), and (STRING NetworkNeighborAL Mixed, incl. Protein targeting to ER, and Oligosaccharyltransferase complex; within-query FDR = 0.0136). Despite its central network position, it has no hu.MAP assignment in the fact sheet, making it an informative example of a module connector that is not fully represented by current complex databases.
- **Conclusion**: Established evidence supports UGGT1 as an ER glycoprotein-quality-control factor and as a prominent co-abundance connector. Its high network position may reflect coordination between ER proteostasis and mitochondrial state, but network centrality does not prove regulatory importance. The cross-compartment bridging role is therefore a hypothesis requiring perturbation or cell-resolved validation.

## Module 2

**Tissue pair**: bone and rectum  
**Genes (25)**: ABCF3, AP1B1, ATP1B1, CD2AP, COPG2, CIAPIN1, DDX42, HSD17B11, DLG1, DPP3, GFM1, FASTKD2, GFPT1, CPOX, HMGCL, LARP4, PDCD4, POLDIP2, PNPT1, PSMA4, RAB3GAP2, RRM2, DARS2, THOP1, TIMM44

### Function

The module does not support a single narrowly defined pathway. Its strongest globally corrected annotation is organelle envelope lumen (GO:CC organelle envelope lumen; q_global = 0.0239), supported by CD2AP, CIAPIN1, CPOX, PNPT1, and THOP1. The gene functions additionally point toward mitochondrial RNA processing and translation, mitochondrial protein import, heme biosynthesis, ketone-body and amino-acid metabolism, proteolysis, vesicle trafficking, actin organization, and carbohydrate derivative synthesis. The network is sparse and appears to contain several connected functional neighborhoods rather than one coherent canonical pathway. The most prominent neighborhood is centered on THOP1, with links to PNPT1, while PNPT1 connects to mitochondrial translation and import-related genes. The globally significant term should therefore be interpreted as evidence for an organelle-associated cellular program, not as proof that every member performs the same molecular function. No STRING functional-enrichment term was reported.

**Cell composition.** This is not a plasma-protein or secreted-protein module: no member is annotated as secreted. Most genes have low tissue specificity and low immune-cell specificity, arguing against a strongly blood-cell-driven module. The cell-type annotations are heterogeneous, including epithelial, hepatic, muscle-associated, reproductive, neural-support, progenitor, and selected immune-cell contexts. A small subset is enhanced in basophils, plasmacytoid dendritic cells, or neutrophils, but the overall pattern does not resemble a blood-cell module. Rectal protein detection is broad among the tested genes, whereas matching bone protein data are unavailable, so the apparent sharing between bone and rectum cannot be assigned confidently to a tissue-specific protein program. The shared signal may instead reflect broadly expressed intracellular machinery, common cell states, or technical and compositional features shared between the tissues.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC organelle envelope lumen | 0.0239 | CD2AP, CIAPIN1, CPOX, PNPT1, THOP1 |

### STRING and hu.MAP

STRING provides one high-confidence relationship, between GFM1 and PNPT1. This is consistent with the mitochondrial translation and RNA-processing interpretation, but the limited STRING connectivity means that most co-abundance edges are not independently supported as known physical or functional interactions by this resource. hu.MAP provides established complex context for DARS2 and GFM1 in one complex (hu.MAP huMAP3_13468.1), and for DARS2 and GFM1 in a second complex (hu.MAP huMAP3_10525.1). PNPT1 and GFM1 are also represented together in (hu.MAP huMAP3_13468.1). These overlaps support a real mitochondrial gene-function neighborhood, particularly involving translation and related organelle processes, but they do not validate the entire co-abundance module as one physical complex. The remaining module edges should therefore be regarded primarily as co-abundance relationships pending orthogonal interaction, perturbation, or tissue-resolved validation.

**STRING interactions (score >= 0.7)**: 1 of 300 gene pairs: GFM1–PNPT1 (0.842)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (HMGCL, DARS2, PNPT1, GFM1; 4/99); huMAP3_10525.1 (DARS2, GFM1; 2/33)

### Novelty

The module cannot be called a wholly new biological discovery solely because most of its pairs are absent from STRING or hu.MAP. Several members have established functions, and the mitochondrial subset is represented in hu.MAP and partly supported by STRING, indicating that at least part of the biology is already known. A potentially novel aspect is the cross-tissue co-abundance organization that brings mitochondrial RNA and translation genes together with proteolysis, heme metabolism, vesicle trafficking, cytoskeletal regulation, and epithelial or metabolic cell-state markers. However, this is a hypothesis about novelty rather than a demonstrated new mechanism. Establishing novelty would require comparison with published co-expression modules, independent cohorts, tissue-cell composition controls, and experimental validation.

**Hypothesis.** Hypothesis: the shared bone–rectum module reflects a broadly expressed intracellular stress-and-maintenance program that couples mitochondrial RNA handling and translation with organelle quality control, heme and intermediary metabolism, proteolytic peptide processing, and membrane trafficking. THOP1 may organize a co-abundance hub linking cytosolic peptide processing to mitochondrial and membrane-associated processes, while PNPT1 and GFM1 represent a mitochondrial RNA-translation arm. CD2AP, COPG2, RAB3GAP2, and AP1B1 may represent a trafficking and cortical-organization arm. This model could arise from a shared epithelial or metabolically active cell state, or from similar mixtures of cell types in bone and rectum, rather than from direct physical assembly of all module proteins.

### Important genes

#### THOP1

- **Related proteins** (co-abundance neighbors): CD2AP (0.89), ATP1B1 (0.88), PDCD4 (0.87), GFPT1 (0.86), POLDIP2 (0.83), PNPT1 (0.82), HSD17B11 (0.81), CPOX (0.81), DLG1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thimet oligopeptidase 1. The protein encoded by this gene is a kininase that uses zinc as a cofactor. The encoded oligopeptidase cleaves cytosolic peptides, making them unavailable for display on antigen-presenting cells. This protein also cleaves neuropeptides under 20 aa in length and can degrade beta-amyloid precursor protein to amyloidogenic peptides. [provided by RefSeq, Nov 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.371); Hypercholesterolemia (0.325); atrial fibrillation (0.246); asthma (0.245); neuroendocrine neoplasm (0.144)
- **Europe PMC papers**: 460
- **Why important**: THOP1 is the strongest network hub in the module and connects the mitochondrial-associated PNPT1 neighborhood with ATP1B1, PDCD4, GFPT1, POLDIP2, HSD17B11, CPOX, and other members. It is one of the genes contributing to the globally significant organelle annotation (GO:CC organelle envelope lumen; q_global = 0.0239). Its established function is cytosolic zinc-dependent peptide cleavage, including processing of short neuropeptides and degradation of amyloid precursor-derived material. It has substantial literature coverage and disease associations involving neurodegenerative disease and metabolic or cardiovascular traits.
- **Conclusion**: Established evidence supports THOP1 as a central co-abundance organizer connected to peptide processing and the module's organelle-associated signal. It is not established that THOP1 mechanistically controls the other module genes. Its role as a bridge between peptide metabolism and mitochondrial or epithelial maintenance is a testable hypothesis.

#### PNPT1

- **Related proteins** (co-abundance neighbors): DARS2 (0.84), POLDIP2 (0.83), THOP1 (0.82), GFM1 (0.81), TIMM44 (0.81); STRING partners: GFM1 (0.842)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: polyribonucleotide nucleotidyltransferase 1. The protein encoded by this gene belongs to the evolutionary conserved polynucleotide phosphorylase family comprised of phosphate dependent 3'-to-5' exoribonucleases implicated in RNA processing and degradation. This enzyme is predominantly localized in the mitochondrial intermembrane space and is involved in import of RNA to mitochondria. Mutations in this gene have been associated with combined …
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 13 (0.807); autosomal recessive nonsyndromic hearing loss 70 (0.740); spinocerebellar ataxia type 25 (0.709); deafness (0.676); hearing loss, autosomal recessive (0.634)
- **Europe PMC papers**: 839
- **Why important**: PNPT1 is a central connector linking DARS2, GFM1, TIMM44, POLDIP2, and THOP1. It contributes to (GO:CC organelle envelope lumen; q_global = 0.0239), is the sole STRING interaction partner reported for GFM1, and occurs in hu.MAP complex (hu.MAP huMAP3_13468.1). Its established molecular functions include mitochondrial RNA processing, RNA degradation, and RNA import. It is associated with combined oxidative phosphorylation deficiency and inherited hearing disorders and has substantial literature support.
- **Conclusion**: Established evidence strongly supports PNPT1 as a mitochondrial RNA-processing component and as an important bridge within the module. The data support a mitochondrial maintenance subprogram, but they do not demonstrate that PNPT1 drives the shared bone–rectum co-abundance pattern.

#### GFM1

- **Related proteins** (co-abundance neighbors): PNPT1 (0.81), LARP4 (0.80); STRING partners: PNPT1 (0.842)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_13468.1, huMAP3_10525.1
- **Function (MyGene.info)**: G elongation factor mitochondrial 1. Eukaryotes contain two protein translational systems, one in the cytoplasm and one in the mitochondria. Mitochondrial translation is crucial for maintaining mitochondrial function and mutations in this system lead to a breakdown in the respiratory chain-oxidative phosphorylation system and to impaired maintenance of mitochondrial DNA. This gene encodes one of the mitochondrial translation elongati…
- **Diseases (Open Targets)**: hepatoencephalopathy due to combined oxidative phosphorylation defect type 1 (0.822); neurodegenerative disease (0.463); combined oxidative phosphorylation deficiency (0.451); hereditary disease (0.341); Leigh syndrome (0.313)
- **Europe PMC papers**: 1380
- **Why important**: GFM1 is supported by the high-confidence STRING relationship with PNPT1 and by both hu.MAP complexes (hu.MAP huMAP3_13468.1) and (hu.MAP huMAP3_10525.1). Its established function is mitochondrial translation elongation, and its disease associations include combined oxidative phosphorylation disorders and Leigh syndrome. Although its local network connectivity is limited, its external interaction and complex evidence make it a strong representative of the mitochondrial translation arm.
- **Conclusion**: Established evidence supports GFM1 as a mitochondrial translation factor embedded in known complexes and linked to PNPT1. The hypothesis that its co-abundance with non-mitochondrial genes reflects coordinated organelle stress or metabolic demand remains unproven.

#### CD2AP

- **Related proteins** (co-abundance neighbors): THOP1 (0.89), COPG2 (0.82), RAB3GAP2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD2 associated protein. This gene encodes a scaffolding molecule that regulates the actin cytoskeleton. The protein directly interacts with filamentous actin and a variety of cell membrane proteins through multiple actin binding sites, SH3 domains, and a proline-rich region containing binding sites for SH3 domains. The cytoplasmic protein localizes to membrane ruffles, lipid rafts, and the leading edges of cells. It is i…
- **Diseases (Open Targets)**: familial idiopathic steroid-resistant nephrotic syndrome (0.701); focal segmental glomerulosclerosis (0.585); Alzheimer disease (0.493); dementia (0.395); Abnormality of the skeletal system (0.314)
- **Europe PMC papers**: 3461
- **Why important**: CD2AP is connected to THOP1, COPG2, and RAB3GAP2 and contributes to (GO:CC organelle envelope lumen; q_global = 0.0239). It is an established membrane and actin-cytoskeleton scaffold involved in membrane trafficking, cell migration, receptor-related organization, and secretion. Its rectal detection and enterocyte-related annotation provide tissue-contextual relevance, while its associations with nephrotic and glomerular disease, Alzheimer disease, and skeletal abnormality indicate broad disease relevance and substantial literature coverage.
- **Conclusion**: Established evidence supports CD2AP as a membrane-cytoskeletal and trafficking component that may connect the module to epithelial organization. Its inclusion does not establish a direct connection to mitochondrial RNA biology; that linkage is a hypothesis based on co-abundance and network placement.

#### CPOX

- **Related proteins** (co-abundance neighbors): HMGCL (0.81), THOP1 (0.81), PSMA4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Not detected in immune cells; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coproporphyrinogen oxidase. The protein encoded by this gene is the sixth enzyme of the heme biosynthetic pathway. The encoded enzyme is soluble and found in the intermembrane space of mitochondria. This enzyme catalyzes the stepwise oxidative decarboxylation of coproporphyrinogen III to protoporphyrinogen IX, a precursor of heme. Defects in this gene are a cause of hereditary coproporphyria (HCP).[provided by RefSeq, Oct 20…
- **Diseases (Open Targets)**: hereditary coproporphyria (0.823); harderoporphyria (0.771); neurodegenerative disease (0.526); CPOX-related hereditary coproporphyria (0.519); hereditary disease (0.470)
- **Europe PMC papers**: 1085
- **Why important**: CPOX connects to HMGCL, THOP1, and PSMA4 and contributes to (GO:CC organelle envelope lumen; q_global = 0.0239). It is an established mitochondrial enzyme in heme biosynthesis, with a defined disease association with hereditary coproporphyria. Its erythrocyte-progenitor annotation provides a possible link to heme-related cellular states, although its blood-cell profile does not indicate a general immune-cell signature. Its literature base is substantial.
- **Conclusion**: Established evidence supports CPOX as a heme-biosynthetic and mitochondrial component that may explain part of the organelle-associated signal. A shared heme or erythroid-related state across bone and rectum is not demonstrated and should not be inferred without cell-resolved evidence.

## Module 3

**Tissue pair**: bone and rectum  
**Genes (25)**: ACACA, ARHGEF2, ATXN2L, CASP8, CNOT12, CNOT1, DIAPH1, DNM1L, EXOC7, FIP1L1, FLII, NDUFA9, NRDC, NUP155, NUP62, PAPSS1, PPP6R3, PSMC2, RRM1, POLR2B, MRPS22, SEC23IP, SDF2L1, VPS13C, ZW10

### Function

The module does not support a single narrowly defined biological function: no GO or KEGG term passed global correction, and STRING functional enrichment was absent. Its gene annotations instead converge on broadly shared intracellular maintenance processes, including cytoskeletal remodeling, vesicle and endomembrane trafficking, mitochondrial dynamics, RNA processing and transport, proteostasis, transcriptional regulation, and cell-cycle control. The network is therefore best interpreted as a mixed cellular-state module rather than a tissue-specific pathway. The strongest structural signals are the central connectivity of PPP6R3 and the linked cytoskeletal, mitochondrial, nuclear-transport, and RNA-regulatory branches. These interpretations are functional hypotheses supported by individual gene annotations, not globally significant enrichment results.

**Cell composition.** The module is predominantly intracellular and broadly expressed rather than plasma or secreted. HPA assigns low tissue specificity to most genes, low immune-cell specificity to nearly all genes, and only a single secretome annotation. The presence of cell-type-enhanced annotations for neutrophils, germ-cell populations, oligodendrocytes, progenitors, and other specialized cells indicates mixed cellular associations rather than a coherent bone or rectum lineage signature. PAPSS1 has a blood-cell group-enriched annotation, while CASP8 is tissue enhanced in bone marrow, but the overall HPA pattern does not support a predominantly blood-cell module. The shared bone–rectum signal could consequently reflect broad housekeeping activity, common intracellular stress or proliferative state, or shared cell types. Rectal protein detection is available for most genes, whereas bone has no matching HPA tissue protein data, so the apparent cross-tissue interpretation should be treated cautiously.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides two high-confidence pairwise relationships within the module: CASP8 with DNM1L and NUP155 with NUP62. These support a mitochondrial apoptosis or remodeling connection and a nuclear-pore connection, respectively, but they do not validate the entire co-abundance network. hu.MAP independently places CNOT1 with CNOT12 in two CCR4-NOT-related complexes and NUP155 with NUP62 in a nuclear-pore complex. In each case, only a small subset of the larger complex is represented in the module. Thus, the module contains several known molecular relationships embedded within a larger set of mostly unconfirmed co-abundance links. The lack of STRING partners for many genes and the absence of STRING enrichment argue against calling this a single established physical complex.

**STRING interactions (score >= 0.7)**: 2 of 300 gene pairs: CASP8–DNM1L (0.759); NUP155–NUP62 (0.997)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00551.1 (CNOT1, CNOT12; 2/23); huMAP3_11224.1 (CNOT1, CNOT12; 2/26); huMAP3_12581.1 (NUP155, NUP62; 2/58)

### Novelty

The cross-tissue co-abundance association may be a useful candidate observation, but the supplied evidence is insufficient to call the module a definitively new biological discovery. Known STRING and hu.MAP relationships show that parts of the module reproduce established biology, especially the CASP8–DNM1L, NUP155–NUP62, and CNOT1–CNOT12 relationships. At the same time, most within-module links are not represented by those resources, and no database evidence establishes the full gene set as a recognized unified module. Absence from STRING or hu.MAP cannot prove novelty, particularly because these resources emphasize physical interactions and curated complexes rather than tissue-specific co-abundance. The defensible conclusion is that the shared bone–rectum co-abundance pattern is a novel candidate module requiring replication, cell composition controls, and comparison with published co-expression modules.

**Hypothesis.** Hypothesis: this module reflects a shared intracellular adaptation state involving coordinated control of cytoskeletal organization, organelle remodeling, nuclear transport, RNA turnover, proteostasis, and survival signaling. PPP6R3 may act as a network coordinator through phosphatase regulation, while FLII and DIAPH1 connect cytoskeletal remodeling to trafficking, DNM1L and CASP8 connect mitochondrial dynamics with apoptotic signaling, and NUP155 with NUP62 connect the state to nuclear transport. CNOT1 and CNOT12 could couple the state to mRNA deadenylation and post-transcriptional regulation. This model predicts that the module will track cellular stress, remodeling, or proliferative composition across bone and rectum rather than represent a dedicated tissue function. It should be tested with cell-resolved data, perturbation experiments, and independent cohorts.

### Important genes

#### PPP6R3

- **Related proteins** (co-abundance neighbors): ATXN2L (0.92), NUP155 (0.86), DNM1L (0.85), RRM1 (0.85), FLII (0.84), SEC23IP (0.83), ZW10 (0.83), POLR2B (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase 6 regulatory subunit 3. Protein phosphatase regulatory subunits, such as SAPS3, modulate the activity of protein phosphatase catalytic subunits by restricting substrate specificity, recruiting substrates, and determining the intracellular localization of the holoenzyme. SAPS3 is a regulatory subunit for the protein phosphatase-6 catalytic subunit (PPP6C; MIM 612725) (Stefansson and Brautigan, 2006 [PubMed 16769727]).[sup…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.383); hair color (0.341); bone fracture (0.253); Pathologic fracture (0.190); obesity disorder (0.185)
- **Europe PMC papers**: 243
- **Why important**: PPP6R3 has the strongest hub-like position in the module and connects genes involved in nuclear transport, mitochondrial dynamics, DNA precursor supply, vesicle biology, transcription, and chromosome segregation. Its established role as a regulatory subunit of protein phosphatase six provides a plausible mechanism for coordinating multiple signaling outputs. It has skeletal-system and fracture associations in Open Targets, although its literature volume is more limited than that of the major apoptotic and metabolic genes in the module.
- **Conclusion**: Established evidence supports PPP6R3 as a phosphatase-regulatory protein and a network hub. It is a plausible module coordinator, but its role in the shared bone–rectum signal remains a hypothesis rather than a demonstrated causal function.

#### FLII

- **Related proteins** (co-abundance neighbors): ARHGEF2 (0.88), PPP6R3 (0.84), EXOC7 (0.81), CNOT12 (0.81), DIAPH1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Centriolar satellite, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FLII actin remodeling protein. This gene encodes a protein with a gelsolin-like actin binding domain and an N-terminal leucine-rich repeat-protein protein interaction domain. The protein is similar to a Drosophila protein involved in early embryogenesis and the structural organization of indirect flight muscle. The gene is located within the Smith-Magenis syndrome region on chromosome 17. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: cardiomyopathy, dilated, 2j (0.616); Abnormality of the skeletal system (0.397); dilated cardiomyopathy (0.313); neurodegenerative disease (0.287); Marfan syndrome (0.118)
- **Europe PMC papers**: 1832
- **Why important**: FLII is among the more connected genes and links PPP6R3 to ARHGEF2, EXOC7, CNOT12, and DIAPH1. Its established actin-binding and actin-remodeling functions, together with skeletal-system and cardiomyopathy associations, make it a strong candidate for the structural and trafficking component of the module. Its literature support is substantial.
- **Conclusion**: Established evidence supports FLII in actin filament remodeling, myofibril organization, and cytoskeletal structure. Its participation in a shared bone–rectum remodeling state is plausible but not proven by the co-abundance network.

#### DNM1L

- **Related proteins** (co-abundance neighbors): ZW10 (0.87), PPP6R3 (0.85), CASP8 (0.84), DIAPH1 (0.81); STRING partners: CASP8 (0.759)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 1L. This gene encodes a member of the dynamin superfamily of GTPases. The encoded protein mediates mitochondrial and peroxisomal division, and is involved in developmentally regulated apoptosis and programmed necrosis. Dysfunction of this gene is implicated in several neurological disorders, including Alzheimer's disease. Mutations in this gene are associated with the autosomal dominant disorder, ence…
- **Diseases (Open Targets)**: encephalopathy, lethal, due to defective mitochondrial peroxisomal fission 1 (0.815); autosomal dominant optic atrophy, classic form (0.721); neurodegenerative disease (0.531); encephalopathy due to mitochondrial and peroxisomal fission defect (0.455); hereditary disease (0.451)
- **Europe PMC papers**: 3015
- **Why important**: DNM1L occupies a central position in the mitochondrial branch and is directly linked in STRING to CASP8. Its established functions in mitochondrial and peroxisomal fission, mitochondrial organization, and apoptosis give the module a clear organelle-remodeling and cell-survival axis. It has extensive literature and strong associations with mitochondrial-fission encephalopathy and optic atrophy.
- **Conclusion**: Established evidence supports DNM1L as a mitochondrial-fission regulator with disease relevance. The module may capture mitochondrial remodeling or apoptosis-related state variation, but the co-abundance data do not establish that DNM1L drives the association.

#### CASP8

- **Related proteins** (co-abundance neighbors): DNM1L (0.84), CNOT1 (0.82), ZW10 (0.81); STRING partners: DNM1L (0.759)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caspase 8. This gene encodes a member of the cysteine-aspartic acid protease (caspase) family. Sequential activation of caspases plays a central role in the execution-phase of cell apoptosis. Caspases exist as inactive proenzymes composed of a prodomain, a large protease subunit, and a small protease subunit. Activation of caspases requires proteolytic processing at conserved internal aspartic residues to ge…
- **Diseases (Open Targets)**: autoimmune lymphoproliferative syndrome type 2B (0.780); head and neck squamous cell carcinoma (0.612); neurodegenerative disease (0.543); viral infectious disease (0.508); autoimmune lymphoproliferative syndrome (0.477)
- **Europe PMC papers**: 40495
- **Why important**: CASP8 links the mitochondrial branch to DNM1L and to the CNOT1 and ZW10 portions of the network. It is a well-studied caspase with established roles in apoptosis, cytokine regulation, immune processes, and proteolysis. Its extensive literature and associations with autoimmune lymphoproliferative disease, cancer, infection, and neurodegeneration make it an important biological anchor.
- **Conclusion**: Established evidence supports CASP8 as an apoptosis and immune-regulatory protease. A survival-versus-death or inflammatory component is a reasonable interpretation of this module, but no evidence shows that the module is an immune module or that CASP8 is activated in the sampled tissues.

#### NUP155

- **Related proteins** (co-abundance neighbors): NUP62 (0.88), PPP6R3 (0.86), CNOT1 (0.86); STRING partners: NUP62 (0.997)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 155. Nucleoporins are proteins that play an important role in the assembly and functioning of the nuclear pore complex (NPC) which regulates the movement of macromolecules across the nuclear envelope (NE). The protein encoded by this gene plays a role in the fusion of NE vesicles and formation of the double membrane NE. The protein may also be involved in cardiac physiology and may be associated with t…
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); atrial fibrillation (0.470); familial atrial fibrillation (0.390)
- **Europe PMC papers**: 944
- **Why important**: NUP155 forms the strongest STRING relationship in the module with NUP62 and is represented with NUP62 in a hu.MAP nuclear-pore complex. Its established role in nuclear-pore assembly, nucleocytoplasmic transport, and nuclear-envelope organization gives the module a concrete nuclear-architecture component. It also has disease associations involving atrial fibrillation and viral infection and has substantial literature support.
- **Conclusion**: Established evidence supports NUP155 as a nuclear-pore and nuclear-envelope protein functioning with NUP62. The pair may mark altered nuclear transport or cell-state composition, but a direct role in the bone–rectum association is not established.

#### CNOT1

- **Related proteins** (co-abundance neighbors): DIAPH1 (0.86), NUP155 (0.86), CASP8 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_00551.1, huMAP3_11224.1
- **Function (MyGene.info)**: CCR4-NOT transcription complex subunit 1. Enables armadillo repeat domain binding activity; molecular adaptor activity; and nuclear receptor binding activity. Contributes to poly(A)-specific ribonuclease activity. Involved in several processes, including negative regulation of signal transduction; positive regulation of cytoplasmic mRNA processing body assembly; and regulation of gene expression. Located in P-body and cytosol. Part of CCR…
- **Diseases (Open Targets)**: holoprosencephaly 12 with or without pancreatic agenesis (0.749); Vissers-Bodmer syndrome (0.697); hereditary disease (0.515); complex neurodevelopmental disorder (0.474); neurodegenerative disease (0.471)
- **Europe PMC papers**: 1262
- **Why important**: CNOT1 connects the network to DIAPH1, NUP155, and CASP8 and is represented with CNOT12 in two hu.MAP CCR4-NOT complexes. Its established functions in mRNA deadenylation, cytoplasmic RNA regulation, translation control, and signal regulation provide a plausible post-transcriptional layer. It has substantial literature and disease associations involving neurodevelopmental disorders and holoprosencephaly.
- **Conclusion**: Established evidence supports CNOT1 as a core CCR4-NOT regulatory component. It could help explain coordinated transcript turnover in the module, but the available data do not show that RNA decay is the dominant module function.

## Module 4

**Tissue pair**: bone and rectum  
**Genes (14)**: FDXR, CTBP2, CYFIP2, DBNL, DDX6, HMOX2, PAK2, UPF1, RUVBL2, SCRIB, CTTN, ACAA1, TRIM25, WDR5

### Function

The module does not have a GO or KEGG term that passes global correction; therefore, no GO or KEGG pathway can be assigned as statistically enriched. Its gene composition instead suggests a mixed cellular program involving RNA surveillance and decay, transcriptional and chromatin regulation, cytoskeletal organization, cell adhesion, membrane trafficking, oxidative or heme-related stress handling, and peroxisomal lipid metabolism. The network contains a coherent RNA-centered arm involving TRIM25, UPF1, DDX6, and CTBP2, a polarity and cytoskeletal arm involving SCRIB, PAK2, DBNL, and CTTN, and a chromatin or genome-maintenance arm involving RUVBL2 and WDR5. The STRING supplementary signals for synaptic biology, neuron differentiation, and neurite development (STRING Keyword Synapse; within-query FDR = 0.0051) (STRING Process Neuron differentiation; within-query FDR = 0.036) (STRING Process Neuron projection development; within-query FDR = 0.036) are compatible with shared machinery for cell architecture and signaling, but they are not globally corrected GO or KEGG evidence. The most defensible interpretation is a conserved cellular homeostasis and remodeling module rather than a narrowly defined tissue-specific pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and many are detected in rectum, which argues against a module composed primarily of highly tissue-restricted proteins. Immune-cell specificity is also generally low, although TRIM25, CTTN, and PAK2 show neutrophil-related HPA signals and several genes have cell-type-enhanced profiles in neutrophils or epithelial populations. Thus, blood or shared immune-cell content could contribute to part of the co-abundance pattern, but the evidence does not support a predominantly blood-cell module. The mixture of epithelial, neuronal or synaptic, germ-cell, renal, and immune-associated HPA profiles suggests that shared cellular states, ubiquitous intracellular machinery, or variable cell composition may be more plausible explanations than a single specialized bone or rectum function. Bone has no matching HPA tissue protein result in this fact sheet, whereas protein detection is broadly present in rectum.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited set of high-confidence relationships within the module. The strongest established links include DDX6 with UPF1, RUVBL2 with WDR5, RUVBL2 with UPF1, and PAK2 with SCRIB. These relationships provide independent support for the RNA-processing and chromatin-associated portions of the network and for a polarity-signaling connection, but they do not validate every co-abundance edge. STRING supplementary functional signals connect CTBP2, SCRIB, CTTN, DBNL, and CYFIP2 with synapse-related biology (STRING Keyword Synapse; within-query FDR = 0.0051), and connect PAK2, SCRIB, WDR5, CTTN, DBNL, DDX6, and CYFIP2 with neuron differentiation or projection development (STRING Process Neuron differentiation; within-query FDR = 0.036) (STRING Process Neuron projection development; within-query FDR = 0.036). These annotations are supportive context rather than globally significant enrichment. hu.MAP reports no complex containing multiple module members, so there is no independent complex-level confirmation. Overall, the network appears to combine several known protein relationships with co-abundance associations that may reflect shared regulation, cellular composition, or indirect functional coupling rather than one established physical complex.

**STRING interactions (score >= 0.7)**: 4 of 91 gene pairs: DDX6–UPF1 (0.93); PAK2–SCRIB (0.757); RUVBL2–UPF1 (0.742); RUVBL2–WDR5 (0.936)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Synapse (FDR = 0.0051, 5 genes); Process Neuron differentiation (FDR = 0.036, 7 genes); Process Neuron projection development (FDR = 0.036, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module-level observation may be a new cross-tissue co-abundance pattern, because the supplied evidence identifies a conserved association between bone and rectum that is not represented as a multi-member hu.MAP complex and is only sparsely covered by high-confidence STRING relationships. However, it would be inappropriate to call the biology wholly novel: the component genes, their functions, and several pairwise relationships are already well studied. Absence from STRING or hu.MAP alone does not prove novelty, and the lack of globally significant GO or KEGG enrichment also does not invalidate the module. A cautious conclusion is that the potentially novel result is the particular cross-tissue co-abundance configuration and its reproducibility, not the discovery of previously unknown functions for the individual genes.

**Hypothesis.** Hypothesis: the module reflects a conserved stress-responsive remodeling state in which RNA quality control and post-transcriptional regulation are coordinated with epithelial or neuronal-like polarity, actin remodeling, and chromatin maintenance. TRIM25 could couple RNA handling and innate-stress signaling to the module; UPF1 and DDX6 could regulate transcript surveillance, decay, and translation; SCRIB, PAK2, DBNL, and CTTN could translate this state into changes in polarity, adhesion, membrane trafficking, and cytoskeletal structure; and RUVBL2 with WDR5 could support transcriptional or genome-maintenance responses. HMOX2 and FDXR may mark redox or heme-related metabolic context, while ACAA1 may reflect epithelial or metabolic cell-state variation. This is a mechanistic model, not an established causal pathway: co-abundance alone cannot distinguish direct regulation from shared cell composition or coordinated response to tissue stress.

### Important genes

#### TRIM25

- **Related proteins** (co-abundance neighbors): UPF1 (0.88), DDX6 (0.86), SCRIB (0.85), CYFIP2 (0.80), WDR5 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tripartite motif containing 25. The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein is an RNA binding protein, functions as a ubiquitin E3 ligase and is involved in multiple cellular processes, including regulation of antiviral innate immunity. [provided by RefSeq, S…
- **Diseases (Open Targets)**: dengue disease (0.463); COVID-19 (0.376); severe acute respiratory syndrome (0.372); neoplasm (0.108); hepatocellular carcinoma (0.106)
- **Europe PMC papers**: 4363
- **Why important**: TRIM25 is the most connected node in the module and links the RNA-associated genes with SCRIB, CYFIP2, and WDR5. Established annotations identify it as an RNA-binding ubiquitin E3 ligase involved in antiviral innate immunity, ubiquitination, oxidative-stress response, and autophagy regulation. Its extensive literature and disease links make it a strong candidate for coordinating a broad cellular response rather than merely marking one tissue.
- **Conclusion**: Established evidence supports TRIM25 as a central regulatory and stress-response protein with broad intracellular functions. The hypothesis that it organizes the whole module or directly couples RNA surveillance to polarity and chromatin responses remains unproven.

#### UPF1

- **Related proteins** (co-abundance neighbors): TRIM25 (0.88), HMOX2 (0.83), CTBP2 (0.81); STRING partners: DDX6 (0.93), RUVBL2 (0.742)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UPF1 RNA helicase and ATPase. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons.…
- **Diseases (Open Targets)**: Intellectual disability (0.437); Global developmental delay (0.426); High anterior hairline (0.425); Frontal bossing (0.425); Hypertelorism (0.425)
- **Europe PMC papers**: 4252
- **Why important**: UPF1 occupies a central position in the RNA-processing portion of the network and has a high-confidence STRING relationship with DDX6, as well as links to TRIM25, HMOX2, and CTBP2. It is an RNA helicase and ATPase required for nonsense-mediated decay, mRNA export, and translational control, and it has a substantial literature and developmental disease association.
- **Conclusion**: Established evidence supports UPF1 as a plausible functional anchor for the module's RNA-surveillance component. It is reasonable to hypothesize that coordinated RNA quality control contributes to the cross-tissue signal, but the data do not establish that UPF1 drives the association.

#### SCRIB

- **Related proteins** (co-abundance neighbors): TRIM25 (0.85), CTBP2 (0.80); STRING partners: PAK2 (0.757)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cell Junctions; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: scribble planar cell polarity protein. This gene encodes a protein that was identified as being similar to the Drosophila scribble protein. The mammalian protein is involved in tumor suppression pathways. As a scaffold protein involved in cell polarization processes, this protein binds to many other proteins. The encoded protein binds to papillomavirus E6 protein via its PDZ domain and the C-terminus of E6. Two alternatively spliced tr…
- **Diseases (Open Targets)**: spina bifida (0.558); neural tube defect (0.268); gout (0.202); neoplasm (0.117); microcephaly (0.116)
- **Europe PMC papers**: 2369
- **Why important**: SCRIB connects the high-connectivity TRIM25 and CTBP2 portion of the network to the polarity and signaling arm through a known STRING relationship with PAK2. It is a membrane-associated scaffold involved in cell polarization, epithelial structure maintenance, migration, receptor recycling, and tumor-suppression pathways. Its localization at plasma membranes and cell junctions makes it particularly relevant to shared epithelial remodeling in rectum and other cell types.
- **Conclusion**: Established evidence supports SCRIB as a polarity and epithelial-organization regulator that could explain part of the module's structural biology. Its proposed role as the bridge between RNA or stress regulation and tissue architecture is a hypothesis requiring perturbation or spatial validation.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): WDR5 (0.84), CTTN (0.83); STRING partners: UPF1 (0.742), WDR5 (0.936)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 links WDR5 and CTTN in the co-abundance network and has high-confidence STRING relationships with WDR5 and UPF1. It is an ATPase and DNA helicase associated with DNA repair, recombination, replication regulation, telomere maintenance, and snoRNP assembly. These functions give it a plausible role in maintaining cellular integrity during remodeling or stress, while its disease and developmental associations add biological importance.
- **Conclusion**: Established evidence supports RUVBL2 as a genome-maintenance and multiprotein-regulation factor with known links to two module members. Its connection to cytoskeletal CTTN in this module may represent indirect coordination or shared cell-state regulation; a direct mechanistic bridge is not established.

#### CTTN

- **Related proteins** (co-abundance neighbors): RUVBL2 (0.83), DBNL (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Plasma membrane; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cortactin. This gene is overexpressed in breast cancer and squamous cell carcinomas of the head and neck. The encoded protein is localized in the cytoplasm and in areas of the cell-substratum contacts. This gene has two roles: (1) regulating the interactions between components of adherens-type junctions and (2) organizing the cytoskeleton and cell adhesion structures of epithelia and carcinoma cells. During …
- **Diseases (Open Targets)**: drug allergy (0.349); placenta praevia (0.265); response to antihypertensive drug (0.260); gallbladder disorder (0.258); non-autoimmune hemolytic anemia (0.240)
- **Europe PMC papers**: 2395
- **Why important**: CTTN is positioned in the cytoskeletal branch with DBNL and RUVBL2 and participates in all three supplementary STRING functional signals (STRING Keyword Synapse; within-query FDR = 0.0051) (STRING Process Neuron differentiation; within-query FDR = 0.036) (STRING Process Neuron projection development; within-query FDR = 0.036). It regulates actin polymerization, adherens-junction interactions, receptor-mediated endocytosis, cell-substratum contacts, and epithelial or carcinoma architecture. Its HPA profile includes epithelial and granulocyte-associated cell types, which is informative for interpreting possible tissue-composition effects.
- **Conclusion**: Established evidence supports CTTN as a structural and trafficking regulator that can report epithelial remodeling or changes in cell adhesion. Its association with the RNA and genome-maintenance genes is best regarded as a module-level hypothesis rather than evidence of a single direct pathway.

## Module 5

**Tissue pair**: bone and rectum  
**Genes (38)**: AKR1B1, ANXA6, CALD1, CBR1, CNN1, COL4A2, CRYAB, CSRP1, CZIB, DSTN, DPYSL2, DPYSL3, FERMT2, FHL1, FLNA, FLNC, PTGFRN, GSTT1, ILK, ITGA5, ITGB1, LTA4H, LPP, MYLK, PPP1R12A, PALLD, PARVA, PDLIM4, PGM1, PGM2, RRAS, SMTN, TAGLN, TUBB6, TLN1, TPM1, TPM2, VCL

### Function

The module is a contractile actin–adhesion and extracellular-matrix interface program. Globally corrected evidence supports myofibril and contractile muscle-fiber organization (GO:CC myofibril; q_global = 1.13e-07)(GO:CC contractile muscle fiber; q_global = 1.13e-07), actin binding and cytoskeletal protein binding (GO:MF actin binding; q_global = 1.61e-06)(GO:MF cytoskeletal protein binding; q_global = 6.44e-06), sarcomere and actin-cytoskeleton organization (GO:CC sarcomere; q_global = 2.08e-06)(GO:CC actin cytoskeleton; q_global = 2.25e-06), focal adhesion and cell-substrate junctions (GO:CC focal adhesion; q_global = 1.64e-05)(GO:CC cell-substrate junction; q_global = 1.64e-05), integrin signaling and focal adhesion pathways (KEGG Integrin signaling - Homo sapiens (human); q_global = 0.000109)(KEGG Focal adhesion - Homo sapiens (human); q_global = 0.000143), and muscle contraction (GO:BP muscle contraction; q_global = 0.000575). Additional primary evidence supports actomyosin, stress fibers, cell–matrix adhesion, wound healing and integrin-mediated signaling (GO:CC stress fiber; q_global = 0.0018)(GO:BP cell-substrate adhesion; q_global = 0.0021)(GO:BP response to wounding; q_global = 0.00459)(GO:BP wound healing; q_global = 0.0069)(GO:BP integrin-mediated signaling pathway; q_global = 0.0104). The best interpretation is a conserved structural program coupling actin organization, integrin anchoring, contractile behavior and tissue remodeling. It indicates a shared cellular state or cell-type program rather than a function necessarily unique to bone or rectum.

**Cell composition.** The module is not dominated by plasma or secreted proteins; most members are intracellular, membrane-associated or cytoskeletal, and the HPA summary identifies only a small secreted component. HPA points strongly toward smooth-muscle, vascular smooth-muscle, stromal, myoepithelial and related contractile populations. Blood-vessel enrichment is prominent, with additional intestine and skeletal-muscle enrichment. Immune-cell specificity is generally low or absent, although selected genes show enrichment in neutrophils, monocytes, platelets or megakaryocytes. The shared signal is therefore more consistent with vascular, smooth-muscle or stromal cell representation than with a generic blood-cell signature, while platelet or vascular contributions remain possible. Rectal protein detection is widespread among the annotated genes, whereas the bone comparison has no matching HPA tissue result, so the cross-tissue interpretation should remain cautious.

**GO/KEGG enrichment**: 44 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC myofibril | 1.13e-07 | CALD1, CRYAB, CSRP1, FERMT2, FLNA, FLNC, ILK, PALLD, PARVA, PDLIM4, PPP1R12A, TPM1, TPM2, VCL |
| GO:CC contractile muscle fiber | 1.13e-07 | CALD1, CRYAB, CSRP1, FERMT2, FLNA, FLNC, ILK, PALLD, PARVA, PDLIM4, PPP1R12A, TPM1, TPM2, VCL |
| GO:MF actin binding | 1.61e-06 | CALD1, CNN1, DSTN, FERMT2, FLNA, FLNC, ITGB1, MYLK, PALLD, PARVA, PDLIM4, SMTN, TAGLN, TLN1, TPM1, TPM2, VCL |
| GO:CC sarcomere | 2.08e-06 | CRYAB, CSRP1, FERMT2, FLNA, FLNC, ILK, PALLD, PARVA, PDLIM4, PPP1R12A, TPM1, TPM2 |
| GO:CC actin cytoskeleton | 2.25e-06 | CALD1, CNN1, CRYAB, DPYSL3, DSTN, FERMT2, FLNA, ILK, LPP, MYLK, PALLD, PARVA, PDLIM4, PPP1R12A, SMTN, TPM1, TPM2, VCL |
| GO:MF cytoskeletal protein binding | 6.44e-06 | CALD1, CNN1, CRYAB, CSRP1, DPYSL3, DSTN, FERMT2, FLNA, FLNC, ITGB1, MYLK, PALLD, PARVA, PDLIM4, SMTN, TAGLN, TLN1, TPM1, TPM2, VCL |
| GO:CC focal adhesion | 1.64e-05 | ANXA6, CNN1, CSRP1, FERMT2, FHL1, FLNA, FLNC, ILK, ITGA5, ITGB1, LPP, PALLD, PARVA, PPP1R12A, RRAS, TLN1, VCL |
| GO:CC cell-substrate junction | 1.64e-05 | ANXA6, CNN1, CSRP1, FERMT2, FHL1, FLNA, FLNC, ILK, ITGA5, ITGB1, LPP, PALLD, PARVA, PPP1R12A, RRAS, TLN1, VCL |
| KEGG Integrin signaling - Homo sapiens (human) | 0.000109 | COL4A2, FERMT2, FLNA, ILK, ITGA5, ITGB1, PARVA, TLN1, VCL |
| GO:BP cytoskeleton organization | 0.000142 | CALD1, CNN1, CRYAB, CSRP1, DPYSL2, DPYSL3, DSTN, FERMT2, FLNA, FLNC, ILK, ITGB1, PALLD, PARVA, PDLIM4, PPP1R12A, TLN1, TPM1, TPM2, TUBB6 |
| KEGG Focal adhesion - Homo sapiens (human) | 0.000143 | COL4A2, FLNA, ILK, ITGA5, ITGB1, MYLK, PARVA, PPP1R12A, TLN1, VCL |
| GO:CC anchoring junction | 0.000192 | ANXA6, CNN1, CSRP1, FERMT2, FHL1, FLNA, FLNC, ILK, ITGA5, ITGB1, LPP, PALLD, PARVA, PDLIM4, PPP1R12A, RRAS, TLN1, VCL |
| KEGG Cytoskeleton in muscle cells - Homo sapiens (human) | 0.000224 | COL4A2, CSRP1, FHL1, FLNC, ITGA5, ITGB1, PDLIM4, TLN1, TPM1, TPM2, VCL |
| GO:CC supramolecular polymer | 0.000237 | CALD1, CRYAB, CSRP1, DPYSL2, DPYSL3, FERMT2, FLNA, FLNC, ILK, PALLD, PARVA, PDLIM4, PPP1R12A, TPM1, TPM2, TUBB6, VCL |
| GO:CC supramolecular fiber | 0.000237 | CALD1, CRYAB, CSRP1, DPYSL2, DPYSL3, FERMT2, FLNA, FLNC, ILK, PALLD, PARVA, PDLIM4, PPP1R12A, TPM1, TPM2, TUBB6, VCL |

### STRING and hu.MAP

STRING independently recapitulates actin binding, cytoskeletal protein binding, myofibril, sarcomere, focal adhesion, cell junction and supramolecular-fiber themes (STRING Function Actin binding; within-query FDR = 1.94e-08)(STRING Function Cytoskeletal protein binding; within-query FDR = 1.94e-08)(STRING Component Myofibril; within-query FDR = 2.62e-08)(STRING COMPARTMENTS Focal adhesion; within-query FDR = 2e-07)(STRING Component Sarcomere; within-query FDR = 3.09e-07)(STRING Component Supramolecular polymer; within-query FDR = 9.18e-07)(STRING COMPARTMENTS Cell junction; within-query FDR = 5.1e-06)(STRING Component I band; within-query FDR = 2.01e-05). Known relationships form an integrin–talin–kindlin–ILK–parvin–vinculin–filamin adhesion neighborhood and a contractile neighborhood containing caldesmon, calponin, myosin light-chain kinase, tropomyosins, transgelin and smoothelin. hu.MAP supports integrin-containing complexes (hu.MAP huMAP3_10503.1)(hu.MAP huMAP3_10980.1)(hu.MAP huMAP3_05466.1)(hu.MAP huMAP3_06955.1), ILK–PARVA complexes (hu.MAP huMAP3_09385.1)(hu.MAP huMAP3_11194.1), CALD1–MYLK complexes (hu.MAP huMAP3_11074.1)(hu.MAP huMAP3_10673.1), tropomyosin complexes (hu.MAP huMAP3_06153.1)(hu.MAP huMAP3_08205.1)(hu.MAP huMAP3_06763.1), DPYSL complexes (hu.MAP huMAP3_00051.1)(hu.MAP huMAP3_11599.1)(hu.MAP huMAP3_11626.1), and a VCL–PGM1 complex (hu.MAP huMAP3_14275.1). Most hu.MAP complexes contain only a subset of the module and additional proteins outside it. Thus, the network combines established physical or functional subcomplexes with co-abundance links that may reflect shared cell state, regulation or tissue composition rather than direct binding.

**STRING interactions (score >= 0.7)**: 61 of 703 gene pairs: AKR1B1–CBR1 (0.991); CALD1–CNN1 (0.867); CALD1–MYLK (0.832); CALD1–TAGLN (0.794); CALD1–TPM1 (0.869); CALD1–TPM2 (0.747); CALD1–VCL (0.771); CNN1–MYLK (0.703); CNN1–SMTN (0.799); CNN1–TAGLN (0.781); CNN1–TPM1 (0.792); COL4A2–ITGA5 (0.803); COL4A2–ITGB1 (0.776); CRYAB–FLNC (0.727); DPYSL2–DPYSL3 (0.976); DPYSL3–PDLIM4 (0.748); FERMT2–FLNA (0.852); FERMT2–FLNC (0.747); FERMT2–ILK (0.997); FERMT2–ITGB1 (0.796); FERMT2–PARVA (0.893); FERMT2–TLN1 (0.705); FERMT2–VCL (0.896); FLNA–FLNC (0.907); FLNA–ILK (0.832); FLNA–ITGA5 (0.789); FLNA–ITGB1 (0.993); FLNA–TLN1 (0.998); FLNA–VCL (0.998); FLNC–ILK (0.714); FLNC–ITGA5 (0.747); FLNC–ITGB1 (0.928); FLNC–TLN1 (0.996); FLNC–TPM2 (0.742); FLNC–VCL (0.994); ILK–ITGA5 (0.973); ILK–ITGB1 (0.999); ILK–PARVA (0.999); ILK–TLN1 (0.996); ILK–VCL (0.995); ITGA5–ITGB1 (0.999); ITGA5–PARVA (0.735); ITGA5–TLN1 (0.978); ITGA5–VCL (0.78); ITGB1–PARVA (0.808); ITGB1–TLN1 (0.999); ITGB1–VCL (0.966); MYLK–PPP1R12A (0.739); MYLK–TPM1 (0.857); MYLK–TPM2 (0.82); MYLK–VCL (0.814); PARVA–TLN1 (0.939); PARVA–VCL (0.948); PGM1–PGM2 (0.993); SMTN–TAGLN (0.798); TAGLN–TPM1 (0.752); TAGLN–TPM2 (0.724); TLN1–VCL (0.999); TPM1–TPM2 (0.993); TPM1–VCL (0.957); TPM2–VCL (0.708)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Actin binding (FDR = 1.94e-08, 18 genes); Function Cytoskeletal protein binding (FDR = 1.94e-08, 22 genes); Component Myofibril (FDR = 2.62e-08, 14 genes); COMPARTMENTS Focal adhesion (FDR = 2e-07, 17 genes); Component Sarcomere (FDR = 3.09e-07, 12 genes); Component Focal adhesion (FDR = 6.42e-07, 17 genes); Component Supramolecular polymer (FDR = 9.18e-07, 18 genes); Component Actin cytoskeleton (FDR = 9.38e-07, 16 genes); KEGG Focal adhesion (FDR = 3.27e-06, 11 genes); Component Supramolecular fiber (FDR = 4.61e-06, 17 genes); COMPARTMENTS Cell junction (FDR = 5.1e-06, 18 genes); WikiPathways Focal adhesion (FDR = 5.56e-06, 11 genes); Component Cytoskeleton (FDR = 1.69e-05, 22 genes); Component Anchoring junction (FDR = 1.82e-05, 18 genes); Component I band (FDR = 2.01e-05, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10503.1 (ITGB1, ITGA5, PTGFRN; 3/27); huMAP3_10980.1 (ITGB1, ITGA5, PTGFRN; 3/44); huMAP3_14275.1 (VCL, PGM1; 2/2); huMAP3_05466.1 (ITGB1, ITGA5; 2/3); huMAP3_06955.1 (ITGB1, ITGA5; 2/5); huMAP3_11074.1 (CALD1, MYLK; 2/6); huMAP3_00051.1 (DPYSL3, DPYSL2; 2/6); huMAP3_06153.1 (TPM2, TPM1; 2/6); huMAP3_11599.1 (DPYSL3, DPYSL2; 2/8); huMAP3_09385.1 (ILK, PARVA; 2/8); huMAP3_11194.1 (ILK, PARVA; 2/10); huMAP3_10673.1 (CALD1, MYLK; 2/14); huMAP3_08205.1 (PPP1R12A, TPM1; 2/17); huMAP3_06763.1 (PPP1R12A, TPM2; 2/18); huMAP3_12303.1 (ANXA6, RRAS; 2/22); huMAP3_12658.1 (ANXA6, RRAS; 2/32); huMAP3_09542.1 (PPP1R12A, TPM1; 2/38); huMAP3_11626.1 (DPYSL3, DPYSL2; 2/42); huMAP3_09336.1 (ITGB1, PTGFRN; 2/50); huMAP3_11349.1 (ITGA5, PTGFRN; 2/78)

### Novelty

The central biology is not a newly discovered molecular complex: it is strongly supported by established STRING relationships, hu.MAP complexes and canonical GO and KEGG annotations. A potentially novel observation is the reproducible co-abundance of this integrated contractile–adhesion program across bone and rectum, particularly the combination of vascular or smooth-muscle markers with integrin anchoring, cytoskeletal remodeling and tissue-repair genes. That cross-tissue module-level pattern could be novel, but it requires independent replication, comparison with tissue co-expression studies and control for cell composition. Lack of a STRING or hu.MAP entry for a gene does not establish novelty, because interaction databases are incomplete and indirect co-regulation can occur.

**Hypothesis.** Hypothesis: the module reflects a conserved contractile stromal or vascular-cell state that couples extracellular-matrix engagement through integrin complexes to actin anchoring, myosin regulation and cytoskeletal remodeling. In bone, this may relate to matrix attachment and mechanically responsive stromal or vascular cells; in rectum, it may relate to smooth-muscle, vascular or stromal architecture and repair. The shared pattern may arise because both tissues contain related contractile and matrix-interacting cell populations, rather than because identical tissue-specific processes operate in both tissues. This hypothesis predicts that module abundance will track smooth-muscle or vascular-stromal cell abundance and focal-adhesion activity, and that it should be separable from a blood-cell signal using single-cell deconvolution or cell-type-specific measurements.

### Important genes

#### ILK

- **Related proteins** (co-abundance neighbors): PALLD (0.91), TAGLN (0.88), CSRP1 (0.88), DPYSL3 (0.87), LPP (0.86), VCL (0.86), TUBB6 (0.83), PARVA (0.81), FLNA (0.81), DPYSL2 (0.81); STRING partners: FERMT2 (0.997), FLNA (0.832), FLNC (0.714), ITGA5 (0.973), ITGB1 (0.999), PARVA (0.999), TLN1 (0.996), VCL (0.995)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: integrin linked kinase. This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastas…
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); familial hypertrophic cardiomyopathy (0.194); Abnormality of the cardiovascular system (0.148); Prolonged QT interval (0.118); neoplasm (0.118)
- **Europe PMC papers**: 8401
- **Why important**: ILK has the strongest network centrality in the supplied module and links the co-abundance neighborhood to integrin-associated adhesion. It appears across central primary structural and adhesion terms, including (GO:CC myofibril; q_global = 1.13e-07), (GO:CC focal adhesion; q_global = 1.64e-05), (KEGG Integrin signaling - Homo sapiens (human); q_global = 0.000109) and (GO:BP integrin-mediated signaling pathway; q_global = 0.0104). STRING connects it with FERMT2, ITGA5, ITGB1, PARVA, TLN1 and VCL, while hu.MAP supports ILK–PARVA complexes (hu.MAP huMAP3_09385.1)(hu.MAP huMAP3_11194.1). HPA places it at focal-adhesion sites and reports smooth-muscle and platelet-related cell types. The supplied annotation supports roles in integrin-linked signaling, cell–matrix adhesion and morphogenesis, and the gene has substantial literature and disease evidence.
- **Conclusion**: Established: ILK is a central integrin-associated adhesion and morphogenesis component that fits the module's structural architecture. Hypothesis: ILK may coordinate extracellular-matrix sensing with contractile remodeling in the shared bone–rectum cell state. The co-abundance data do not establish that ILK drives the module or that its disease associations explain the tissue pattern.

#### VCL

- **Related proteins** (co-abundance neighbors): PALLD (0.94), DPYSL3 (0.88), ILK (0.86), TLN1 (0.85), TAGLN (0.82), FLNC (0.81); STRING partners: CALD1 (0.771), FERMT2 (0.896), FLNA (0.998), FLNC (0.994), ILK (0.995), ITGA5 (0.78), ITGB1 (0.966), MYLK (0.814), PARVA (0.948), TLN1 (0.999), TPM1 (0.957), TPM2 (0.708)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_14275.1
- **Function (MyGene.info)**: vinculin. Vinculin is a cytoskeletal protein associated with cell-cell and cell-matrix junctions, where it is thought to function as one of several interacting proteins involved in anchoring F-actin to the membrane. Defects in VCL are the cause of cardiomyopathy dilated type 1W. Dilated cardiomyopathy is a disorder characterized by ventricular dilation and impaired systolic function, resulting in congestive…
- **Diseases (Open Targets)**: dilated cardiomyopathy 1W (0.692); hypertrophic cardiomyopathy 15 (0.660); hypertrophic cardiomyopathy (0.652); familial isolated dilated cardiomyopathy (0.642); cancer (0.605)
- **Europe PMC papers**: 10760
- **Why important**: VCL is a high-connectivity structural hub linking focal adhesions, actin-associated proteins, integrin components and contractile proteins. It appears in primary terms including (GO:CC myofibril; q_global = 1.13e-07), (GO:MF actin binding; q_global = 1.61e-06), (GO:CC focal adhesion; q_global = 1.64e-05), (KEGG Integrin signaling - Homo sapiens (human); q_global = 0.000109), (KEGG Focal adhesion - Homo sapiens (human); q_global = 0.000143) and (GO:BP platelet aggregation; q_global = 0.0497). STRING connects it with FLNA, FLNC, ILK, ITGB1, PARVA, TLN1, TPM1 and other module members. hu.MAP identifies a VCL-containing complex with PGM1 (hu.MAP huMAP3_14275.1). HPA localizes VCL to focal-adhesion sites and detects it in rectum, while the supplied annotation assigns it roles at cell–cell and cell–matrix junctions. VCL also has extensive literature and established cardiomyopathy associations.
- **Conclusion**: Established: VCL is a plausible physical and functional bridge between actin filaments and membrane adhesion complexes. Hypothesis: VCL may stabilize a force-transmission apparatus in vascular, smooth-muscle or stromal cells of both tissues. The module does not demonstrate altered vinculin mechanics or a causal role in bone or rectal disease.

#### FLNC

- **Related proteins** (co-abundance neighbors): FLNA (0.87), TLN1 (0.85), PALLD (0.84), DPYSL3 (0.83), VCL (0.81), FERMT2 (0.81); STRING partners: CRYAB (0.727), FERMT2 (0.747), FLNA (0.907), ILK (0.714), ITGA5 (0.747), ITGB1 (0.928), TLN1 (0.996), TPM2 (0.742), VCL (0.994)
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin C. This gene encodes one of three related filamin genes, specifically gamma filamin. These filamin proteins crosslink actin filaments into orthogonal networks in cortical cytoplasm and participate in the anchoring of membrane proteins for the actin cytoskeleton. Three functional domains exist in filamin: an N-terminal filamentous actin-binding domain, a C-terminal self-association domain, and a membr…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy 26 (0.833); myofibrillar myopathy 5 (0.791); distal myopathy with posterior leg and anterior hand involvement (0.742); dilated cardiomyopathy (0.714); familial restrictive cardiomyopathy (0.660)
- **Europe PMC papers**: 3861
- **Why important**: FLNC is part of the module's structural core and appears in globally corrected myofibril, sarcomere, focal-adhesion, muscle-development and cytoskeletal terms (GO:CC myofibril; q_global = 1.13e-07)(GO:CC sarcomere; q_global = 2.08e-06)(GO:CC focal adhesion; q_global = 1.64e-05)(KEGG Cytoskeleton in muscle cells - Homo sapiens (human); q_global = 0.000224)(GO:BP muscle structure development; q_global = 0.00231). STRING links it to FLNA, TLN1, VCL, ITGB1, FERMT2 and ILK, forming a coherent actin-crosslinking and adhesion neighborhood. HPA shows enrichment in heart muscle, skeletal muscle and tongue, with single-cell enrichment in cardiomyocytes, myonuclei and smooth-muscle cells. The supplied annotation supports actin-network crosslinking, membrane-protein anchoring and sarcomere organization, with substantial literature and multiple cardiomyopathy and myopathy associations.
- **Conclusion**: Established: FLNC is a muscle-associated actin-crosslinking protein that fits the module's contractile and adhesion architecture. Hypothesis: FLNC may provide tensile continuity between contractile filaments and adhesion structures in the shared cell population. The cross-tissue abundance pattern cannot determine whether the relevant cells are smooth muscle, vascular cells or another contractile population.

#### TLN1

- **Related proteins** (co-abundance neighbors): ANXA6 (0.88), FLNA (0.86), VCL (0.85), FLNC (0.85); STRING partners: FERMT2 (0.705), FLNA (0.998), FLNC (0.996), ILK (0.996), ITGA5 (0.978), ITGB1 (0.999), PARVA (0.939), VCL (0.999)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 is a core integrin-activation and cell-substrate-adhesion component. It occurs in primary terms for focal adhesion, integrin signaling, cell–matrix adhesion, cytoskeleton organization and platelet aggregation (GO:CC focal adhesion; q_global = 1.64e-05)(KEGG Integrin signaling - Homo sapiens (human); q_global = 0.000109)(GO:BP cell-substrate adhesion; q_global = 0.0021)(GO:BP integrin-mediated signaling pathway; q_global = 0.0104)(GO:BP platelet aggregation; q_global = 0.0497). STRING shows strong relationships with ITGA5, ITGB1, ILK, PARVA, VCL, FLNA and FLNC, connecting extracellular-matrix receptors to the actin cytoskeleton. HPA places it at focal adhesions and reports vascular, megakaryocyte and platelet-related enrichment. The supplied annotation links TLN1 to integrin activation, adhesion, spreading and migration, and it has extensive disease literature.
- **Conclusion**: Established: TLN1 links integrin engagement with actin organization and matches the module's strongest pathway themes. Hypothesis: TLN1-dependent adhesion may couple matrix stiffness or tissue strain to the contractile program shared by bone and rectum. The data do not show whether integrin activation is increased or whether TLN1 is a driver rather than a marker.

#### PALLD

- **Related proteins** (co-abundance neighbors): VCL (0.94), DPYSL3 (0.93), ILK (0.91), FLNA (0.90), TAGLN (0.89), FHL1 (0.86), FLNC (0.84), TUBB6 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: palladin, cytoskeletal associated protein. This gene encodes a cytoskeletal protein that is required for organizing the actin cytoskeleton. The protein is a component of actin-containing microfilaments, and it is involved in the control of cell shape, adhesion, and contraction. Polymorphisms in this gene are associated with a susceptibility to pancreatic cancer type 1, and also with a risk for myocardial infarction. Alternative splicing re…
- **Diseases (Open Targets)**: coronary artery disorder (0.444); exocrine pancreatic carcinoma (0.372); coronary atherosclerosis (0.360); Bicuspid aortic valve (0.325); aortic stenosis (0.319)
- **Europe PMC papers**: 1170
- **Why important**: PALLD has very high network centrality and connects to VCL, DPYSL3, ILK, FLNA, TAGLN, FHL1, FLNC and TUBB6. It is repeatedly represented in primary myofibril, actin-binding, focal-adhesion, sarcomere and cytoskeleton terms (GO:CC myofibril; q_global = 1.13e-07)(GO:MF actin binding; q_global = 1.61e-06)(GO:CC sarcomere; q_global = 2.08e-06)(GO:CC focal adhesion; q_global = 1.64e-05)(GO:BP cytoskeleton organization; q_global = 0.000142). STRING independently places it in actin-binding, myofibril, focal-adhesion, supramolecular-fiber and junction categories (STRING Function Actin binding; within-query FDR = 1.94e-08)(STRING Component Myofibril; within-query FDR = 2.62e-08)(STRING COMPARTMENTS Focal adhesion; within-query FDR = 2e-07)(STRING Component Supramolecular polymer; within-query FDR = 9.18e-07)(STRING COMPARTMENTS Cell junction; within-query FDR = 5.1e-06). HPA shows smooth-muscle and myonuclear cell-type enhancement, and the supplied annotation assigns PALLD roles in actin organization, cell shape, adhesion and contraction. Its disease associations include pancreatic and cardiovascular conditions, with meaningful literature support.
- **Conclusion**: Established: PALLD is a structural actin-organizing component occupying a central position in the module, despite no reported hu.MAP complex or STRING partner list in the fact sheet. Hypothesis: PALLD may integrate contractile fibers with focal-adhesion remodeling and help explain the cross-tissue co-abundance pattern. Its centrality is network evidence, not proof that PALLD physically binds every neighboring module member.

## Module 6

**Tissue pair**: bone and rectum  
**Genes (33)**: ANXA2, ARFGAP1, ATAD3A, C1QBP, CLTC, EIF3C, ERAP1, TBRG4, HNRNPK, TMPO, TMPO, MCM2, MCM4, MCM5, MCM6, MCM7, OCIAD2, ALDH18A1, PDIA4, PDS5B, PHB1, PHB2, PON2, PSPC1, PUS1, TAF15, MRPL2, RRBP1, SUPT16H, SRP68, SRP72, TAP2, XRCC6

### Function

The module is best interpreted as a DNA replication and genome-maintenance module. The strongest primary evidence is the coordinated presence of MCM2, MCM4, MCM5, MCM6 and MCM7 in the MCM and CMG complexes, DNA replication initiation, replication-fork helicase, recombinational repair and DNA-damage-response terms (29 globally significant GO/KEGG terms, q_global 3.85e-05–0.0423; see the table). The KEGG cell-cycle and DNA-replication terms (KEGG Cell cycle - Homo sapiens (human); q_global = 0.000832) and (KEGG DNA replication - Homo sapiens (human); q_global = 0.00689), together with the homologous-recombination term (KEGG Homologous recombination - Homo sapiens (human); q_global = 0.0182), support a role in licensing and progressing replication while protecting or repairing replication-associated DNA lesions. The broad nucleic-acid-binding enrichment (GO:MF nucleic acid binding; q_global = 0.000979) is consistent with a wider nuclear information-processing context, but is less specific than the MCM-centered terms. The module therefore appears to capture coordinated abundance of replication, repair, chromatin, RNA-processing, translation, mitochondrial and membrane-trafficking proteins rather than a single biochemical pathway acting in every constituent gene.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: most genes have low tissue specificity, most have low immune-cell specificity, and the module is largely intracellular. The HPA profile does, however, show frequent cell-type enhancement in progenitor populations, including erythrocyte and megakaryocyte progenitors, and recurrent enrichment in bone marrow and lymphoid tissue. MCM2, MCM4, MCM5, MCM6 and MCM7 are nuclear proteins with bone-marrow or lymphoid associations, which is compatible with proliferative progenitor cells. A smaller component is secreted to blood or has intracellular-and-membrane annotation, including ANXA2, C1QBP, ERAP1 and PON2, while PHB1 and PDIA4 have intracellular or membrane-related secretome annotations. Thus, the shared bone–rectum signal may partly reflect proliferating or progenitor-like cells, and possibly blood contribution, rather than a specialized function unique to mature bone and rectum. Rectal protein detection is broadly present across the annotated module, whereas matching bone tissue protein data are unavailable, so tissue-level protein equivalence cannot be established.

**GO/KEGG enrichment**: 29 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP double-strand break repair via break-induced replication | 3.85e-05 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication initiation | 3.85e-05 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC DNA replication preinitiation complex | 3.85e-05 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC MCM complex | 3.85e-05 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC CMG complex | 3.85e-05 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP DNA replication initiation | 0.000157 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication | 0.000157 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| KEGG Cell cycle - Homo sapiens (human) | 0.000832 | MCM2, MCM4, MCM5, MCM6, MCM7, PDS5B |
| GO:MF nucleic acid binding | 0.000979 | ALDH18A1, ANXA2, C1QBP, CLTC, EIF3C, FASTKD4, HNRNPK, MCM2, MCM4, MCM5, MCM6, MCM7, MRPL2, PDIA4, PDS5B, PSPC1, PUS1, RRBP1, SRP68, SRP72, SUPT16H, TAF15, TMPO, XRCC6 |
| GO:BP recombinational repair | 0.00209 | C1QBP, MCM2, MCM4, MCM5, MCM6, MCM7, XRCC6 |
| GO:MF four-way junction helicase activity | 0.00281 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF forked DNA-dependent helicase activity | 0.00281 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF DNA helicase activity | 0.00441 | MCM2, MCM4, MCM5, MCM6, MCM7, XRCC6 |
| GO:MF double-stranded DNA helicase activity | 0.0045 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF 3'-5' DNA helicase activity | 0.0045 | MCM2, MCM4, MCM5, MCM6, MCM7 |

### STRING and hu.MAP

STRING provides strong, direct support for a coherent MCM core: MCM2, MCM4, MCM5, MCM6 and MCM7 are mutually connected at very high confidence, and STRING also links this core to SUPT16H, XRCC6 and PHB1. The PHB1–PHB2 pair, the SRP68–SRP72 pair, the HNRNPK–TAF15 pair and several mitochondrial or RNA-related links represent additional established relationships. STRING functional results (15 supplementary STRING terms; within-query FDR 0.00067–0.001) independently recover the MCM, CMG, MCM-domain and DNA-helicase context, but remain supplementary rather than globally corrected enrichment evidence. hu.MAP repeatedly places the five MCM genes in complexes containing MCMBP and, in larger assemblies, CDC45, GINS proteins, TIMELESS, TIPIN and CLSPN (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1), directly supporting replication-initiation and replisome-complex membership. hu.MAP also supports PHB1–PHB2, HNRNPK–TAF15 and several broader chromatin, mitochondrial and RNA-associated assemblies (hu.MAP huMAP3_01706.1) (hu.MAP huMAP3_09671.1) (hu.MAP huMAP3_11743.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_08848.1) (hu.MAP huMAP3_12158.1) (hu.MAP huMAP3_14523.1) (hu.MAP huMAP3_10725.1) (hu.MAP huMAP3_11232.1) (hu.MAP huMAP3_13468.1). These databases show that much of the module is a known molecular neighborhood; the co-abundance module is therefore biologically coherent, but not evidence that every edge represents direct physical binding or that all genes belong to one complex.

**STRING interactions (score >= 0.7)**: 23 of 528 gene pairs: ANXA2–PHB1 (0.801); ATAD3A–PHB1 (0.756); ATAD3A–PHB2 (0.789); C1QBP–PHB1 (0.847); C1QBP–PHB2 (0.964); HNRNPK–TAF15 (0.805); HNRNPK–XRCC6 (0.738); MCM2–MCM4 (0.999); MCM2–MCM5 (0.999); MCM2–MCM6 (0.999); MCM2–MCM7 (0.999); MCM2–SUPT16H (0.735); MCM4–MCM5 (0.999); MCM4–MCM6 (0.999); MCM4–MCM7 (0.999); MCM4–SUPT16H (0.722); MCM5–MCM6 (0.999); MCM5–MCM7 (0.999); MCM6–MCM7 (0.999); MCM7–PHB1 (0.724); PHB1–PHB2 (0.999); SRP68–SRP72 (0.999); SUPT16H–XRCC6 (0.8)
**STRING functional enrichment (supplementary, within-query FDR)**: Component MCM complex (FDR = 0.00067, 5 genes); Component CMG complex (FDR = 0.00067, 5 genes); COMPARTMENTS MCM complex (FDR = 0.0007, 5 genes); COMPARTMENTS CMG complex (FDR = 0.0007, 5 genes); Function Nucleic acid binding (FDR = 0.0008, 24 genes); InterPro MCM domain (FDR = 0.00085, 5 genes); InterPro Mini-chromosome maintenance, conserved site (FDR = 0.00085, 5 genes); InterPro MCM N-terminal domain (FDR = 0.00085, 5 genes); InterPro Mini-chromosome maintenance protein (FDR = 0.00085, 5 genes); InterPro MCM OB domain (FDR = 0.00085, 5 genes); InterPro MCM, AAA-lid domain (FDR = 0.00085, 5 genes); Function DNA helicase activity (FDR = 0.001, 6 genes); RCTM Unwinding of DNA (FDR = 0.001, 5 genes); RCTM Activation of the pre-replicative complex (FDR = 0.001, 5 genes); NetworkNeighborAL Activation of the pre-replicative complex, and GINS complex (FDR = 0.001, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05529.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/6); huMAP3_14758.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/14); huMAP3_08554.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_11832.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_12180.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/17); huMAP3_06061.1 (MCM4, MCM7, MCM2, MCM6; 4/5); huMAP3_07113.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_11119.1 (MCM4, MCM5, MCM7, MCM6; 4/14); huMAP3_10862.1 (MCM4, MCM2, MCM6, SUPT16H; 4/33); huMAP3_09860.1 (MCM4, MCM2, MCM6; 3/4); huMAP3_00154.1 (MCM4, MCM2, MCM6; 3/5); huMAP3_09466.1 (MCM4, MCM2, MCM6; 3/23); huMAP3_14306.1 (MCM4, MCM2, MCM6; 3/55); huMAP3_02602.1 (MCM4, MCM6; 2/2); huMAP3_01706.1 (PHB1, PHB2; 2/2); huMAP3_09671.1 (PHB1, PHB2; 2/10); huMAP3_11743.1 (PHB1, PHB2; 2/10); huMAP3_09238.1 (MCM5, MCM7; 2/11); huMAP3_08848.1 (MCM4, MCM6; 2/15); huMAP3_12158.1 (HNRNPK, TAF15; 2/16); huMAP3_14523.1 (HNRNPK, TAF15; 2/33); huMAP3_10725.1 (PHB1, PHB2; 2/59); huMAP3_11232.1 (TBRG4, PDS5B; 2/78); huMAP3_13468.1 (ALDH18A1, PUS1; 2/99)

### Novelty

The module should not be presented as a newly discovered replication complex. The MCM-centered relationships, CMG association, prohibitin pair, SRP pair and RNA-binding associations are already represented in STRING and hu.MAP. The potentially novel aspect is the tissue-pair-level co-abundance observation: these established replication and genome-maintenance components covary with mitochondrial, translation, endoplasmic-reticulum, trafficking and RNA-processing genes in bone and rectum. That observation may reflect a shared cellular-state or cell-composition program, but novelty cannot be established from the supplied evidence alone. In particular, absence of a peripheral gene from STRING or hu.MAP would not prove a new interaction or pathway. Replication across independent cohorts, preservation after cell-composition adjustment, comparison with other tissue pairs, and perturbation or spatial validation would be needed to support a genuinely novel biological claim.

**Hypothesis.** Hypothesis: the shared bone–rectum module reflects a conserved proliferative and genome-protection state in progenitor or renewing cells. In this model, the MCM helicase core licenses and supports DNA replication, while XRCC6 and PDS5B help manage replication-associated DNA damage, recombinational repair and chromosome organization. SUPT16H could couple chromatin remodeling to access of replication machinery, whereas mitochondrial and protein-homeostasis components could support the energetic and biosynthetic demands of proliferation. The progenitor-enriched HPA profile makes this explanation plausible, but co-abundance alone cannot determine whether the signal is caused by cell proliferation, DNA damage, cell-type mixture, or coordinated regulation within the same cells. This hypothesis should be tested by cell-resolved expression and protein measurements, proliferation and damage markers, and replication or repair perturbations.

### Important genes

#### MCM2

- **Related proteins** (co-abundance neighbors): MCM5 (0.94), MCM6 (0.86), MCM7 (0.85), XRCC6 (0.83), ARFGAP1 (0.81); STRING partners: MCM4 (0.999), MCM5 (0.999), MCM6 (0.999), MCM7 (0.999), SUPT16H (0.735)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_10862.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a central member of the MCM helicase core, has strong network connections to the other MCM components and XRCC6, and participates across the full set of primary replication, helicase, repair and cell-cycle terms (29 globally significant GO/KEGG terms, q_global 3.85e-05–0.0423; see the table). It is represented in many hu.MAP replication assemblies (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_14306.1) and has substantial literature coverage. Its HPA enhancement in bone marrow and lymphoid tissue is compatible with the progenitor-cell interpretation. Disease associations in the fact sheet include gastrointestinal abnormality and inherited hearing-related conditions, showing that altered replication machinery can have organism-level consequences.
- **Conclusion**: Established: MCM2 is a core replication-initiation and helicase-associated component, and its position strongly anchors the module's primary functional interpretation. Hypothesis: its co-abundance across bone and rectum marks shared proliferative progenitor activity rather than a tissue-specific MCM2 function.

#### MCM6

- **Related proteins** (co-abundance neighbors): MCM4 (0.92), MCM5 (0.88), MCM2 (0.86), ARFGAP1 (0.84), TBRG4 (0.83), SUPT16H (0.82), PUS1 (0.82); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_10862.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 6. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: lactose intolerance (0.246); neurodegenerative disease (0.225); obesity disorder (0.166); nervous system disorder (0.141); systemic lupus erythematosus (0.140)
- **Europe PMC papers**: 3766
- **Why important**: MCM6 is one of the five-member MCM core recovered by every primary MCM-centered enrichment and by the STRING and hu.MAP evidence (29 globally significant GO/KEGG terms, q_global 3.85e-05–0.0423; see the table), (15 supplementary STRING terms; within-query FDR 0.00067–0.001), (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1). It has substantial network connectivity, links to SUPT16H and PUS1 in the module, and is tissue-enhanced in lymphoid tissue and cell-type-enhanced in several hematopoietic progenitor populations. Its literature volume is substantial, and the fact sheet links it to replication initiation and inherited or systemic disease associations.
- **Conclusion**: Established: MCM6 is a core component of the replication licensing and helicase machinery represented in this module. Hypothesis: its association with non-MCM genes may reflect coupling of replication to chromatin, RNA and mitochondrial programs in renewing cells.

#### MCM7

- **Related proteins** (co-abundance neighbors): XRCC6 (0.92), MCM5 (0.88), MCM2 (0.85), ALDH18A1 (0.82), OCIAD2 (0.82), C1QBP (0.81); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM6 (0.999), PHB1 (0.724)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 is a core MCM and CMG component with strong connections to MCM2, MCM4, MCM5 and MCM6 and additional links to XRCC6, PHB1 and other module genes. It appears in nearly all primary replication and repair terms (22 globally significant GO/KEGG terms, q_global 3.85e-05–0.0182; see the table) and (6 globally significant GO/KEGG terms, q_global 0.0221–0.0423; see the table), in all of the relevant STRING functional terms, and in multiple hu.MAP replication assemblies (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) and (hu.MAP huMAP3_09238.1). It has the largest literature volume among the highlighted MCM genes in the fact sheet and is tissue-enhanced in bone marrow, with progenitor and epithelial cell-type associations. Its disease associations include replication-linked developmental and neurological syndromes.
- **Conclusion**: Established: MCM7 is a highly supported structural and functional anchor of the module's replication program. Hypothesis: its links to PHB1 and mitochondrial-associated genes may indicate coordination between replication demand and cellular energy or organelle homeostasis, although the available data do not establish that mechanism.

#### XRCC6

- **Related proteins** (co-abundance neighbors): MCM7 (0.92), MCM5 (0.89), EIF3C (0.86), C1QBP (0.86), CLTC (0.85), OCIAD2 (0.84), MCM2 (0.83), ALDH18A1 (0.83), HNRNPK (0.81); STRING partners: HNRNPK (0.738), SUPT16H (0.8)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: X-ray repair cross complementing 6. The p70/p80 autoantigen is a nuclear complex consisting of two subunits with molecular masses of approximately 70 and 80 kDa. The complex functions as a single-stranded DNA-dependent ATP-dependent helicase. The complex may be involved in the repair of nonhomologous DNA ends such as that required for double-strand break repair, transposition, and V(D)J recombination. High levels of autoantibodies t…
- **Diseases (Open Targets)**: HIV infectious disease (0.505); neurodegenerative disease (0.441); intelligence (0.209); breast cancer (0.175); Abnormality of the skeletal system (0.154)
- **Europe PMC papers**: 2742
- **Why important**: XRCC6 is the most connected gene in the supplied module network and bridges the MCM core with HNRNPK, SUPT16H and several broader RNA, translation and trafficking-associated genes. It is included in globally significant DNA-damage, recombinational-repair, helicase, DNA-repair and protein-DNA-complex terms (GO:MF nucleic acid binding; q_global = 0.000979), (GO:BP recombinational repair; q_global = 0.00209), (GO:MF DNA helicase activity; q_global = 0.00441), (GO:BP DNA damage response; q_global = 0.0156), (6 globally significant GO/KEGG terms, q_global 0.0221–0.0423; see the table), and STRING supports its relationships with HNRNPK and SUPT16H. Its established function in an ATP-dependent DNA helicase complex involved in nonhomologous end joining gives the module a repair dimension beyond replication. The fact sheet also documents extensive literature and disease associations involving skeletal abnormality, cancer and neurological disease.
- **Conclusion**: Established: XRCC6 is a plausible bridge between replication-associated DNA damage and repair-related processes in the module. Hypothesis: its network position reflects coordinated replication-stress management, but the co-abundance data cannot prove that XRCC6 mediates the observed relationships.

#### PDS5B

- **Related proteins** (co-abundance neighbors): TMPO (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_11232.1
- **Function (MyGene.info)**: PDS5 cohesin associated factor B. This gene encodes a protein that interacts with the conserved protein complex termed cohesin. The cohesin complex holds together sister chromatids and facilitates accurate chromosome segregation during mitosis and meiosis. This protein is also a negative regulator of cell proliferation and may be a tumor-suppressor gene. [provided by RefSeq, Jul 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.522); hypothyroidism (0.294); lysosomal storage disease (0.292); cervical carcinoma (0.287); smoking initiation (0.274)
- **Europe PMC papers**: 735
- **Why important**: PDS5B contributes to the globally significant cell-cycle, DNA-damage-response, homologous-recombination and DNA-repair terms (KEGG Cell cycle - Homo sapiens (human); q_global = 0.000832), (GO:MF nucleic acid binding; q_global = 0.000979), (GO:BP DNA damage response; q_global = 0.0156), (KEGG Homologous recombination - Homo sapiens (human); q_global = 0.0182) and (GO:BP DNA repair; q_global = 0.0292). Its established role in cohesin-associated sister-chromatid organization connects replication and repair to chromosome segregation and proliferation control. It is represented in a hu.MAP assembly with TBRG4 and in the module's broader network through TMPO, although it is not a dense STRING hub. Its disease associations include neurological, lysosomal, cervical-carcinoma and proliferation-related findings, while its more modest literature volume compared with the MCM genes makes it a complementary rather than primary anchor.
- **Conclusion**: Established: PDS5B supplies a chromosome-cohesion and repair interpretation that complements the MCM helicase core. Hypothesis: it may help explain how the module couples replication with faithful chromosome inheritance in renewing bone or rectal cell populations.

## Module 7

**Tissue pair**: bone and rectum  
**Genes (15)**: ACOT7, DSP, GARS1, GMPS, EIF6, KPNA2, NIBAN2, NUP188, PFDN6, PRRC1, SRPK1, TOM1, TTLL12, UMPS, WDR43

### Function

This is a mixed cellular maintenance module rather than a confidently assigned pathway module. No GO or KEGG term passed global correction, so there is no globally significant pathway annotation to report. The strongest network-centered interpretation is coordinated core-cell biology: GMPS and UMPS represent de novo purine and pyrimidine nucleotide synthesis; GARS1 supports aminoacyl-tRNA charging and translation; EIF6, WDR43, SRPK1, KPNA2, and NUP188 point toward ribosome production, RNA processing, nuclear import, and nucleocytoplasmic transport; DSP and epithelial-associated HPA patterns add a tissue-structure component. The co-abundance pattern may therefore reflect shared proliferative, biosynthetic, and epithelial-cell states rather than one narrowly defined biochemical process.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only one secreted gene, and the listed proteins are predominantly intracellular, nuclear, cytosolic, or junctional. Blood-cell specificity is generally low, with only isolated immune-cell enhancements, so a blood-contamination explanation is not the leading interpretation. The module does show strong cell-type and tissue-context signals, especially esophageal epithelial cells, germ-cell populations, enterocytes, and selected skin or muscle contexts. Several genes are detected in rectum, whereas bone has no matching HPA tissue protein result in this summary. Thus, shared epithelial or other resident-cell composition, together with broadly expressed housekeeping-like biosynthetic machinery, could contribute substantially to the conserved bone-rectum signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, GMPS--UMPS, directly connecting purine and pyrimidine nucleotide biosynthesis. STRING reports no functional enrichment for the module. hu.MAP provides two partial complex memberships: KPNA2 and NUP188 occur together in a nucleocytoplasmic-transport or nuclear-pore-related complex listed as C1, while GARS1 and GMPS occur together in the broader multifunctional complex listed as C2. These observations support selected biochemical and macromolecular connections, but the module is not reproduced as one established protein complex. Most co-abundance edges lack corresponding high-confidence STRING or hu.MAP support, indicating that the network captures expression coordination beyond currently catalogued physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 105 gene pairs: GMPS–UMPS (0.802)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09825.1 (KPNA2, NUP188; 2/27); huMAP3_14442.1 (GARS1, GMPS; 2/57)

### Novelty

This may be a new cross-tissue co-abundance observation, but it cannot be called a newly discovered molecular complex or pathway. The absence of broad STRING enrichment and the limited overlap with hu.MAP argue against an already recognized unified interaction module. However, absence from those resources does not establish novelty, because co-abundance can arise from shared cell composition, regulation, or condition-dependent biology that is not represented by physical-interaction databases. The most defensible claim is that the conserved bone-rectum association is a potentially novel systems-level pattern requiring validation with independent cohorts, cell-composition adjustment, and perturbation or tissue-localized experiments.

**Hypothesis.** Hypothesis: the module reflects a shared epithelial or progenitor-like cellular state in bone and rectum in which nucleotide production, translation capacity, RNA and protein trafficking, and cell-junction maintenance are coordinately regulated. GMPS and UMPS could supply nucleotide demand, GARS1 and EIF6 could support protein production, KPNA2 and NUP188 could regulate nuclear-cytoplasmic exchange, and DSP could stabilize epithelial architecture. The tissue and germ-cell associations suggest that this may be a generic biosynthetic or renewal program rather than a bone-rectum-specific mechanism. This hypothesis predicts that module activity will track resident epithelial or progenitor-cell abundance and cellular proliferation or repair state, and that its apparent conservation will weaken after careful cell-composition correction.

### Important genes

#### GMPS

- **Related proteins** (co-abundance neighbors): GARS1 (0.88), ACOT7 (0.87), WDR43 (0.86), EIF6 (0.83), SRPK1 (0.81), PFDN6 (0.81), KPNA2 (0.80); STRING partners: UMPS (0.802)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: guanosine monophosphate synthase. In the de novo synthesis of purine nucleotides, IMP is the branch point metabolite at which point the pathway diverges to the synthesis of either guanine or adenine nucleotides. In the guanine nucleotide pathway, there are 2 enzymes involved in converting IMP to GMP, namely IMP dehydrogenase (IMPD1), which catalyzes the oxidation of IMP to XMP, and GMP synthetase, which catalyzes the amination of …
- **Diseases (Open Targets)**: rheumatoid arthritis (0.277); nephrotic syndrome (0.259); lupus nephritis (0.259); rhabdomyosarcoma (0.247); hepatocellular carcinoma (0.237)
- **Europe PMC papers**: 5161
- **Why important**: GMPS is the network hub with the broadest connectivity in the module and is linked to GARS1, ACOT7, WDR43, EIF6, SRPK1, PFDN6, and KPNA2. Its established function is the terminal step of guanine-nucleotide biosynthesis, and it forms the sole high-confidence STRING pair in the module with UMPS. It also participates in the hu.MAP complex represented by C2 and has extensive literature and disease-association coverage. Its centrality makes it the best anchor for testing whether the module has a biosynthetic core.
- **Conclusion**: Established evidence supports GMPS as a central purine-biosynthetic enzyme and a network organizer in this module. It is reasonable to hypothesize that GMPS abundance contributes to a coordinated nucleotide-demand state, but the co-abundance data do not establish that GMPS drives the module or that nucleotide synthesis is globally enriched.

#### GARS1

- **Related proteins** (co-abundance neighbors): GMPS (0.88), SRPK1 (0.88), TTLL12 (0.84), TOM1 (0.83), ACOT7 (0.82), EIF6 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: glycyl-tRNA synthetase 1. This gene encodes glycyl-tRNA synthetase, one of the aminoacyl-tRNA synthetases that charge tRNAs with their cognate amino acids. The encoded enzyme is an (alpha)2 dimer which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Two transcript variants encoding different isoforms ha…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease type 2D (0.790); neuronopathy, distal hereditary motor, type 5A (0.729); neuronopathy, distal hereditary motor, type 5 (0.698); spinal muscular atrophy, infantile, James type (0.649); Charcot-Marie-Tooth disease type 2 (0.565)
- **Europe PMC papers**: 302
- **Why important**: GARS1 is a highly connected module member associated with GMPS, SRPK1, TTLL12, TOM1, ACOT7, and EIF6. Its established role is glycyl-tRNA charging, linking the module to translational capacity, and it shares hu.MAP complex C2 with GMPS. It has a substantial literature base and important associations with inherited neuropathies and motor-neuron disease.
- **Conclusion**: Established evidence supports GARS1 as a translation-related enzyme that connects the nucleotide and protein-production signals. Its module association is consistent with coordinated biosynthetic activity, while any specific role in the bone-rectum phenotype remains hypothetical.

#### UMPS

- **Related proteins** (co-abundance neighbors): KPNA2 (0.90), PRRC1 (0.81); STRING partners: GMPS (0.802)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: uridine monophosphate synthetase. This gene encodes a uridine 5'-monophosphate synthase. The encoded protein is a bifunctional enzyme that catalyzes the final two steps of the de novo pyrimidine biosynthetic pathway. The first reaction is carried out by the N-terminal enzyme orotate phosphoribosyltransferase which converts orotic acid to orotidine-5'-monophosphate. The terminal reaction is carried out by the C-terminal enzyme OMP …
- **Diseases (Open Targets)**: orotic aciduria (0.773); coronary artery disorder (0.507); Intellectual disability (0.462); open-angle glaucoma (0.381); Abnormality of the skeletal system (0.374)
- **Europe PMC papers**: 965
- **Why important**: UMPS is the pyrimidine counterpart to GMPS and catalyzes the final steps of de novo UMP production. Although it has fewer module connections, its strongest listed edge is to KPNA2 and it is the only high-confidence STRING partner of GMPS, giving it disproportionate interpretive value. Its established disease association with orotic aciduria provides a clear biochemical and clinical rationale for prioritization.
- **Conclusion**: Established evidence supports UMPS as a core pyrimidine-biosynthesis component and as part of the module's nucleotide-balance signal. The GMPS--UMPS relationship supports a coordinated nucleotide hypothesis, but it does not prove that the entire module is a nucleotide-biosynthesis module.

#### KPNA2

- **Related proteins** (co-abundance neighbors): UMPS (0.90), GMPS (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_09825.1
- **Function (MyGene.info)**: karyopherin subunit alpha 2. The import of proteins into the nucleus is a process that involves at least 2 steps. The first is an energy-independent docking of the protein to the nuclear envelope and the second is an energy-dependent translocation through the nuclear pore complex. Imported proteins require a nuclear localization sequence (NLS) which generally consists of a short region of basic amino acids or 2 such regions s…
- **Diseases (Open Targets)**: severe acute respiratory syndrome (0.462); Orthomyxoviridae infectious disease (0.462); dengue disease (0.462); COVID-19 (0.373); non-alcoholic fatty liver (0.324)
- **Europe PMC papers**: 2442
- **Why important**: KPNA2 connects UMPS and GMPS in the co-abundance graph and belongs with NUP188 to hu.MAP complex C1, giving it a bridge position between nucleotide-associated genes and nuclear transport. Its established function is importin-alpha-mediated nuclear import of proteins bearing nuclear-localization signals. It has extensive literature and disease or infection-related associations, and HPA places it in a testis-enhanced and germ-cell-associated context while also detecting it in rectum.
- **Conclusion**: Established evidence supports KPNA2 as a plausible transport bridge within the module. It may couple biosynthetic state to nuclear signaling or RNA-related regulation, but that coupling is a hypothesis rather than a demonstrated mechanism in bone or rectum.

#### DSP

- **Related proteins** (co-abundance neighbors): WDR43 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cell Junctions; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: desmoplakin. This gene encodes a protein that anchors intermediate filaments to desmosomal plaques and forms an obligate component of functional desmosomes. Mutations in this gene are the cause of several cardiomyopathies and keratodermas, including skin fragility-woolly hair syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016].
- **Diseases (Open Targets)**: arrhythmogenic cardiomyopathy with wooly hair and keratoderma (0.841); arrhythmogenic right ventricular dysplasia 8 (0.812); arrhythmogenic right ventricular cardiomyopathy (0.760); lethal acantholytic epidermolysis bullosa (0.745); cardiomyopathy, dilated, with wooly hair, keratoderma, and tooth agenesis (0.741)
- **Europe PMC papers**: 17350
- **Why important**: DSP is the module's epithelial-structure specialist. It encodes desmoplakin, an obligate component of functional desmosomes, and has the largest literature volume among the listed genes. Its HPA pattern is enhanced in esophagus and skin, enriched in several epithelial cell types, localized to cell junctions, and detected in rectum. Its disease associations include cardiomyopathy and keratoderma, demonstrating strong functional and clinical relevance even though it has only one listed network neighbor.
- **Conclusion**: Established evidence supports DSP as a marker and structural mediator of epithelial integrity. Its presence suggests that cell-junction or epithelial composition may help explain conservation between bone and rectum, but it does not demonstrate direct coupling to the nucleotide enzymes.

## Module 8

**Tissue pair**: bone and rectum  
**Genes (26)**: BOP1, CHORDC1, CS, CLUH, DDX21, SORD, MYBBP1A, APOO, NOP2, NOP56, POLDIP3, PES1, GART, ATIC, RAE1, RCC1, RSL1D1, PDCD11, MRPS35, SMARCA4, STAT1, YARS1, TUBA4A, TBL3, VPS4A, XPNPEP1

### Function

The module is best interpreted as a nucleolar RNA-production and ribosome-biogenesis module. The primary evidence is the globally corrected enrichment for rRNA metabolic process (GO:BP rRNA metabolic process; q_global = 0.00285), ribosome biogenesis (GO:BP ribosome biogenesis; q_global = 0.0084), rRNA processing (GO:BP rRNA processing; q_global = 0.0101), nucleolus (GO:CC nucleolus; q_global = 0.0178), and preribosome (GO:CC preribosome; q_global = 0.0345). The recurring genes include BOP1, DDX21, NOP2, NOP56, PDCD11, PES1, TBL3, and related nucleolar factors. The module also contains a smaller set of genes associated with purine synthesis, cytoskeletal organization, mitotic or nuclear transport processes, mitochondrial function, and protein folding. These peripheral genes may reflect coupling of ribosome production to growth, metabolism, cell division, and intracellular organization rather than defining the central module function. No conclusion here relies on nominal enrichment values or on STRING FDR as global significance.

**Cell composition.** The HPA profile does not support a module dominated by plasma proteins, secreted proteins, or blood-cell markers. Most genes have low tissue specificity and low immune-cell specificity, while only APOO is annotated as secreted to blood. The module therefore does not resemble a blood-contamination signature on the available evidence. Several genes show tissue or cell-type enhancement in skeletal muscle, tongue, testis-related germ-cell populations, esophageal epithelial cells, and selected other cell types, but there is no single dominant shared tissue identity. Protein detection in rectum is broad among the measured genes, whereas bone has no matching HPA tissue dataset in this summary. A shared broadly expressed cellular program, possibly influenced by differences in cellular composition, is more plausible than a predominantly circulating-protein explanation.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP rRNA metabolic process | 0.00285 | BOP1, DDX21, NOP2, NOP56, PDCD11, PES1, SMARCA4, TBL3 |
| GO:BP ribosome biogenesis | 0.0084 | BOP1, DDX21, MYBBP1A, NOP2, NOP56, PDCD11, PES1, TBL3 |
| GO:BP rRNA processing | 0.0101 | BOP1, DDX21, NOP2, NOP56, PDCD11, PES1, TBL3 |
| GO:CC nucleolus | 0.0178 | BOP1, DDX21, MYBBP1A, NOP2, NOP56, PDCD11, PES1, RAE1, RSL1D1, SMARCA4, STAT1, TBL3 |
| GO:CC preribosome | 0.0345 | BOP1, NOP56, PDCD11, PES1, TBL3 |

### STRING and hu.MAP

STRING provides strong known relationships among the nucleolar core, especially BOP1, PES1, NOP2, NOP56, PDCD11, RSL1D1, TBL3, DDX21, and MYBBP1A. Its supplementary annotations independently converge on the nucleolus, preribosome, rRNA processing, and ribosome biogenesis (STRING COMPARTMENTS Nucleolus; within-query FDR = 0.00035) through (STRING Process ncRNA metabolic process; within-query FDR = 0.0257). These relationships indicate that much of the observed co-abundance structure recapitulates an established molecular neighborhood rather than an unexplained association. The strongest coherent interpretation is therefore biological coordination of a known ribosome-production apparatus. hu.MAP provides additional support but is more limited: NOP2 and TBL3 occur together in a small complex (hu.MAP huMAP3_03059.1), RCC1 and RAE1 recur in nuclear transport or chromosome-related complexes (hu.MAP huMAP3_10000.1) and (hu.MAP huMAP3_12581.1), and ATIC, YARS1, XPNPEP1, and CHORDC1 occur together in a broader complex (hu.MAP huMAP3_14442.1). The partial overlap of these complexes suggests that the module combines a well-supported nucleolar core with peripheral links to translation, metabolism, nuclear transport, and cell division.

**STRING interactions (score >= 0.7)**: 41 of 325 gene pairs: ATIC–GART (0.999); ATIC–SORD (0.86); BOP1–DDX21 (0.838); BOP1–MYBBP1A (0.915); BOP1–NOP2 (0.99); BOP1–NOP56 (0.974); BOP1–PDCD11 (0.97); BOP1–PES1 (0.999); BOP1–RSL1D1 (0.998); BOP1–TBL3 (0.967); DDX21–MYBBP1A (0.963); DDX21–NOP2 (0.761); DDX21–NOP56 (0.811); DDX21–PES1 (0.975); DDX21–RSL1D1 (0.81); GART–MYBBP1A (0.971); GART–PES1 (0.91); MYBBP1A–NOP2 (0.864); MYBBP1A–NOP56 (0.737); MYBBP1A–PDCD11 (0.949); MYBBP1A–PES1 (0.948); MYBBP1A–RSL1D1 (0.831); MYBBP1A–TBL3 (0.909); NOP2–NOP56 (0.969); NOP2–PDCD11 (0.927); NOP2–PES1 (0.983); NOP2–RSL1D1 (0.982); NOP2–TBL3 (0.839); NOP56–PDCD11 (0.997); NOP56–PES1 (0.956); NOP56–RSL1D1 (0.991); NOP56–TBL3 (0.999); NOP56–YARS1 (0.712); PDCD11–PES1 (0.969); PDCD11–RSL1D1 (0.978); PDCD11–TBL3 (0.996); PES1–RSL1D1 (0.996); PES1–TBL3 (0.935); POLDIP3–RAE1 (0.768); RSL1D1–TBL3 (0.991); SMARCA4–STAT1 (0.85)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Nucleolus (FDR = 0.00035, 12 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 0.00087, 8 genes); COMPARTMENTS Preribosome (FDR = 0.0013, 6 genes); COMPARTMENTS 90S preribosome (FDR = 0.0013, 5 genes); NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 0.0015, 7 genes); Component Preribosome (FDR = 0.0032, 6 genes); NetworkNeighborAL Mixed, incl. Preribosome, large subunit precursor, and Maturation of LSU-rRNA (FDR = 0.0034, 5 genes); Component Nucleolus (FDR = 0.0038, 12 genes); Process rRNA processing (FDR = 0.0042, 8 genes); Process Ribosome biogenesis (FDR = 0.0042, 9 genes); RCTM rRNA processing in the nucleus and cytosol (FDR = 0.0094, 7 genes); COMPARTMENTS Nuclear lumen (FDR = 0.0125, 14 genes); Component 90S preribosome (FDR = 0.0138, 4 genes); RCTM Major pathway of rRNA processing in the nucleolus and cytosol (FDR = 0.0232, 6 genes); Process ncRNA metabolic process (FDR = 0.0257, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (ATIC, YARS1, XPNPEP1, CHORDC1; 4/57); huMAP3_03059.1 (NOP2, TBL3; 2/3); huMAP3_10000.1 (RCC1, RAE1; 2/44); huMAP3_12581.1 (RCC1, RAE1; 2/58)

### Novelty

This should not be described as a newly discovered ribosome-biogenesis complex. The central genes and their relationships are already represented in STRING, and several components have established nucleolar or preribosome functions. Nevertheless, the conserved co-abundance of this combined gene set across bone and rectum may be a new systems-level observation, especially if that cross-tissue conservation was not previously reported. The evidence supports novelty at the level of tissue-pair co-abundance organization or module context, not novelty of the individual molecular functions. Absence of some genes from hu.MAP or absence of a particular edge from STRING is not sufficient to establish novelty.

**Hypothesis.** Hypothesis: the shared bone-rectum module reflects a conserved demand for coordinated nucleolar ribosome production in viable, biosynthetically active cells. A core involving NOP2, NOP56, PES1, BOP1, DDX21, PDCD11, TBL3, and related factors could coordinate rRNA modification, processing, preribosome assembly, and maturation. The accompanying metabolic, cytoskeletal, mitochondrial, and nuclear-transport genes may couple this process to nucleotide supply, translation, cell-cycle progression, and intracellular trafficking. The module could therefore mark a common proliferative or biosynthetic state shared by relevant cell populations in bone and rectum, but this remains a hypothesis requiring cell-resolved expression, perturbation, and independent tissue validation.

### Important genes

#### NOP2

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.88), TUBA4A (0.85), MYBBP1A (0.84), PES1 (0.84), PDCD11 (0.83), APOO (0.82), DDX21 (0.81); STRING partners: BOP1 (0.99), DDX21 (0.761), MYBBP1A (0.864), NOP56 (0.969), PDCD11 (0.927), PES1 (0.983), RSL1D1 (0.982), TBL3 (0.839)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_03059.1
- **Function (MyGene.info)**: NOP2 nucleolar protein. Enables RNA binding activity. Involved in positive regulation of cell population proliferation; regulation of signal transduction by p53 class mediator; and ribosomal large subunit assembly. Located in nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.273); nonpapillary renal cell carcinoma (0.097); neoplasm (0.097); cancer (0.091); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 2120
- **Why important**: NOP2 is among the most connected genes in the module and links several central nucleolar partners, including RSL1D1, MYBBP1A, PES1, PDCD11, DDX21, and the preribosome-associated network. It appears in the primary rRNA metabolism, ribosome biogenesis, rRNA processing, and nucleolus terms (GO:BP rRNA metabolic process; q_global = 0.00285) through (GO:CC nucleolus; q_global = 0.0178), as well as multiple STRING-supported nucleolar processes. Its annotated functions include rRNA processing and large-subunit assembly, and its disease and cancer associations have substantial literature support.
- **Conclusion**: Established: NOP2 is a central nucleolar ribosome-biogenesis factor and a strong representative of the module's core function. Hypothesis: its central co-abundance position may make it a useful state marker for coordinated ribosome production in the shared bone-rectum program, but the module does not by itself establish that NOP2 controls the behavior of either tissue.

#### PES1

- **Related proteins** (co-abundance neighbors): BOP1 (0.85), TBL3 (0.84), NOP2 (0.84); STRING partners: BOP1 (0.999), DDX21 (0.975), GART (0.91), MYBBP1A (0.948), NOP2 (0.983), NOP56 (0.956), PDCD11 (0.969), RSL1D1 (0.996), TBL3 (0.935)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli, Nucleoli rim, Mitotic chromosome; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pescadillo ribosomal biogenesis factor 1. This gene encodes a nuclear protein that contains a breast cancer associated gene 1 (BRCA1) C-terminal interaction domain. The encoded protein interacts with BOP1 and WDR12 to form the PeBoW complex, which plays a critical role in cell proliferation via pre-rRNA processing and 60S ribosomal subunit maturation. Expression of this gene may play an important role in breast cancer proliferation and tu…
- **Diseases (Open Targets)**: aortic stenosis (0.137); neoplasm (0.104); head and neck squamous cell carcinoma (0.097); schizophrenia (0.091); neuroblastoma (0.081)
- **Europe PMC papers**: 1080
- **Why important**: PES1 is a highly connected member of the nucleolar core and is linked in STRING to BOP1, DDX21, NOP2, NOP56, PDCD11, RSL1D1, TBL3, and MYBBP1A. It is present in every primary enrichment theme from rRNA metabolism through preribosome (GO:BP rRNA metabolic process; q_global = 0.00285) through (GO:CC preribosome; q_global = 0.0345). Its annotated role in the PeBoW complex, pre-rRNA processing, and large-subunit maturation directly explains the module's strongest biological signal. It also has a substantial literature base and documented relevance to cell proliferation and neoplasia.
- **Conclusion**: Established: PES1 is a mechanistically informative component of the ribosome-biogenesis core, not merely a correlated housekeeping transcript. Hypothesis: coordinated PES1 abundance may couple ribosome maturation to proliferative demand in the shared module, although causality and tissue-specific consequences remain untested.

#### NOP56

- **Related proteins** (co-abundance neighbors): TUBA4A (0.88), SORD (0.88), RSL1D1 (0.80), MYBBP1A (0.80); STRING partners: BOP1 (0.974), DDX21 (0.811), MYBBP1A (0.737), NOP2 (0.969), PDCD11 (0.997), PES1 (0.956), RSL1D1 (0.991), TBL3 (0.999), YARS1 (0.712)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP56 ribonucleoprotein. Nop56p is a yeast nucleolar protein that is part of a complex with the nucleolar proteins Nop58p and fibrillarin. Nop56p is required for assembly of the 60S ribosomal subunit and is involved in pre-rRNA processing. The protein encoded by this gene is similar in sequence to Nop56p and is also found in the nucleolus. Expansion of a GGCCTG repeat from 3-8 copies to 1500-2500 copies in an intron of th…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 36 (0.586); neurodegenerative disease (0.495); ovarian neoplasm (0.272); hereditary disease (0.193); cerebellar ataxia (0.121)
- **Europe PMC papers**: 1517
- **Why important**: NOP56 is embedded in the nucleolar network and connects to BOP1, NOP2, PDCD11, PES1, RSL1D1, TBL3, DDX21, and MYBBP1A. It participates in all of the primary terms (GO:BP rRNA metabolic process; q_global = 0.00285) through (GO:CC preribosome; q_global = 0.0345), including preribosome, and its annotated functions include rRNA processing, rRNA modification, and ribosomal-subunit biogenesis. Its established association with spinocerebellar ataxia provides a clinically important disease link, while its literature volume supports a well-characterized molecular role.
- **Conclusion**: Established: NOP56 is a core rRNA-processing and ribosome-assembly factor that helps anchor the module's functional interpretation. Hypothesis: its coordinated abundance with the other nucleolar factors could reflect shared regulation of ribosome quality or production, rather than a tissue-specific disease mechanism.

#### DDX21

- **Related proteins** (co-abundance neighbors): MYBBP1A (0.92), RSL1D1 (0.84), RCC1 (0.84), NOP2 (0.81), BOP1 (0.81); STRING partners: BOP1 (0.838), MYBBP1A (0.963), NOP2 (0.761), NOP56 (0.811), PES1 (0.975), RSL1D1 (0.81)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 has strong network connections to MYBBP1A, PES1, BOP1, NOP2, NOP56, and RSL1D1, and appears in the primary rRNA metabolism, ribosome biogenesis, rRNA processing, and nucleolus terms (GO:BP rRNA metabolic process; q_global = 0.00285) through (GO:CC nucleolus; q_global = 0.0178). As an RNA helicase, it provides a plausible RNA-structural component within the processing machinery. Its annotations also connect it to transcriptional regulation and osteoblast differentiation, which is especially relevant to a module shared with bone. It has broad disease and cancer literature.
- **Conclusion**: Established: DDX21 is a nucleolar RNA-processing factor with a strong position in the module and a documented bone-relevant annotation. Hypothesis: DDX21 may help couple rRNA processing to tissue-cell growth or differentiation states, but the co-abundance data cannot distinguish that possibility from general nucleolar activity.

#### BOP1

- **Related proteins** (co-abundance neighbors): PES1 (0.85), DDX21 (0.81); STRING partners: DDX21 (0.838), MYBBP1A (0.915), NOP2 (0.99), NOP56 (0.974), PDCD11 (0.97), PES1 (0.999), RSL1D1 (0.998), TBL3 (0.967)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BOP1 ribosomal biogenesis factor. Enables RNA binding activity. Involved in regulation of cell cycle; regulation of signal transduction by p53 class mediator; and ribosomal large subunit biogenesis. Located in chromosome; nucleolus; and nucleoplasm. Part of PeBoW complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.318); cancer (0.090); neoplasm (0.087); polycystic ovary syndrome (0.082); colorectal carcinoma (0.078)
- **Europe PMC papers**: 1064
- **Why important**: BOP1 is a member of the PeBoW complex and is directly connected in STRING to most of the nucleolar core, including PES1, NOP2, NOP56, PDCD11, RSL1D1, TBL3, DDX21, and MYBBP1A. It appears in every primary enrichment theme (GO:BP rRNA metabolic process; q_global = 0.00285) through (GO:CC preribosome; q_global = 0.0345). Its established functions in large-subunit assembly, rRNA cleavage, and maturation of the large ribosomal subunit make it a particularly direct mechanistic explanation for the module. It also has annotations related to cell-cycle regulation, proliferation, and colorectal carcinoma.
- **Conclusion**: Established: BOP1 is a central and mechanistically specific component of the nucleolar ribosome-biogenesis program. Hypothesis: BOP1 abundance may report coordinated PeBoW activity across the two tissues, but no causal role in the cross-tissue conservation can be inferred without perturbation.
