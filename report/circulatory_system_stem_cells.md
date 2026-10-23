# Conserved co-abundance modules: circulatory_system and stem_cells

## Module 0

**Tissue pair**: circulatory_system and stem_cells  
**Genes (6)**: CTNNA2, FKBP7, LZIC, MYO1D, TMEM109, TOR2A

### Function

No GO or KEGG term passed global correction, and STRING supplied no supplementary enrichment. The co-abundance pattern therefore does not support a formally established pathway-level function. The local network is compatible with a heterogeneous cell-structure and membrane-trafficking theme: MYO1D is linked to actin organization, endocytic recycling and vesicle transport; CTNNA2 is linked to actin binding, cell adhesion, migration and neuronal projection development; FKBP7 is an endoplasmic-reticulum chaperone; TMEM109 is associated with membrane transport and cell-death responses; LZIC is linked to beta-catenin binding and radiation response; and TOR2A is associated with endoplasmic-reticulum and plasma-membrane biology, calcium transport and secreted salusin peptides. These annotations are suggestive rather than evidence of a single unified pathway. The most defensible interpretation is a weak, mixed cell-architecture and membrane-homeostasis co-abundance program, or a shared cell-state signal, rather than a defined conserved biochemical module.

**Cell composition.** The module does not look like a conventional plasma-protein or blood-cell module. Only a minority of genes have secretome annotations, with TOR2A specifically described as secreted to blood and FKBP7 described as intracellular and membrane-associated. Most members are intracellular or membrane-associated, and the tissue annotations are heterogeneous, including vessel, intestine, ovary, brain, epididymis and retina. Blood-cell evidence is generally low, with one gene immune-cell enriched and another not detected in immune cells; basophils are the only specifically enriched blood-cell signal. All members show cell-type enhancement, but the highlighted cell types span reproductive, epithelial, stromal, neural, vascular and megakaryocytic contexts. Thus, the shared signal is unlikely to be explained simply by a uniform blood-cell or plasma-protein contribution. It may instead reflect mixed cellular composition, a broadly reused structural or membrane-related state, or coordinated regulation in particular cell populations present in both tissue groups.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING relationships among the module members and no STRING functional enrichment. There are also no hu.MAP complexes containing multiple module members. Consequently, the co-abundance edges should not be interpreted as established physical interactions, a protein complex, or a validated signaling pathway. The absence of STRING and hu.MAP support makes the observed network more consistent with coordinated expression, shared cellular context, indirect regulation or sample-composition effects. Some functional relationships are biologically plausible from individual annotations, especially the MYO1D and CTNNA2 connection to actin-associated cell architecture, but this is not independently confirmed as a physical interaction in the supplied evidence.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may be a newly observed tissue-pair co-abundance pattern, because the supplied resources show no shared STRING interactions, no multi-member hu.MAP complex and no globally significant GO or KEGG term. However, those absences do not establish biological novelty. The individual genes and their functions are already represented in gene databases, disease resources and the literature, and the broad themes of actin organization, membrane biology, endoplasmic-reticulum function, cell adhesion and stress response are established. The appropriate conclusion is that the specific conserved co-abundance configuration appears insufficiently characterized in these resources, not that it represents a new pathway or new gene biology. Replication in independent cohorts, preservation after cell-composition adjustment and comparison with published transcriptomic modules would be needed to support a claim of a new finding.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of cell architecture and membrane or organelle homeostasis in a shared cellular state occurring in circulatory-system and stem-cell samples. In this model, MYO1D and CTNNA2 represent actin-linked trafficking, adhesion and cortical organization; FKBP7 and TOR2A represent endoplasmic-reticulum and membrane proteostasis; and TMEM109 and LZIC represent stress-response or survival-related components. TOR2A could additionally connect the intracellular program to extracellular or vascular signaling through its salusin-related products. This is a hypothesis only: the lack of enriched terms, STRING relationships and hu.MAP complexes means that the proposed connections are not established as one mechanism.

### Important genes

#### MYO1D

- **Related proteins** (co-abundance neighbors): FKBP7 (0.91), CTNNA2 (0.84), TOR2A (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin ID. Enables protein domain specific binding activity. Predicted to be involved in actin filament organization; early endosome to recycling endosome transport; and vesicle transport along actin filament. Located in extracellular exosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: alcohol drinking (0.337); Dupuytren Contracture (0.287); male reproductive organ cancer (0.286); Inguinal hernia (0.267); autoimmune disorder of central nervous system (0.261)
- **Europe PMC papers**: 681
- **Why important**: MYO1D has the strongest network connectivity in the module and links FKBP7, CTNNA2 and TOR2A. Its annotation directly supports actin filament organization, endocytic recycling and vesicle transport, making it the clearest candidate for connecting membrane trafficking with cell architecture. It also has substantial literature coverage and disease associations including Dupuytren contracture, inguinal hernia and autoimmune disease.
- **Conclusion**: Established evidence supports MYO1D as the principal network-connected actin and trafficking candidate in this module hu.MAP. The hypothesis that it organizes the whole shared module is plausible but unproven, because the relationships are co-abundance edges without STRING or hu.MAP confirmation.

#### CTNNA2

- **Related proteins** (co-abundance neighbors): TMEM109 (0.86), MYO1D (0.84); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin alpha 2. Enables actin filament binding activity. Involved in negative regulation of Arp2/3 complex-mediated actin nucleation; regulation of neuron migration; and regulation of neuron projection development. Located in cytoplasm. Implicated in complex cortical dysplasia with other brain malformations. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: complex cortical dysplasia with other brain malformations (0.720); refractive error (0.392); diabetes mellitus (0.356); hereditary breast ovarian cancer syndrome (0.340); lung adenocarcinoma (0.340)
- **Europe PMC papers**: 1454
- **Why important**: CTNNA2 is connected to MYO1D and TMEM109 hu.MAP and has the largest literature volume among the module members. Its established annotations include actin binding, cell adhesion, regulation of cell migration and neuronal projection development. It has a strong disease association with complex cortical dysplasia and other brain malformations, while HPA shows enrichment in brain, retina and epididymis and immune-cell enrichment in basophils.
- **Conclusion**: Established evidence makes CTNNA2 an important cell-adhesion and cytoskeletal candidate with a particularly strong neural and developmental context. Its role in a shared circulatory-system and stem-cell module remains a hypothesis and could reflect cell composition or a more general adhesion program.

#### FKBP7

- **Related proteins** (co-abundance neighbors): MYO1D (0.91), LZIC (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FKBP prolyl isomerase 7. The protein encoded by this gene belongs to the FKBP-type peptidyl-prolyl cis/trans isomerase (PPIase) family. Members of this family exhibit PPIase activity and function as molecular chaperones. A similar protein in mouse is located in the endoplasmic reticulum and binds calcium. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: atrial fibrillation (0.398); neurodegenerative disease (0.377); alcohol drinking (0.232); stroke disorder (0.232); heart failure (0.119)
- **Europe PMC papers**: 246
- **Why important**: FKBP7 occupies a bridge position between MYO1D and LZIC. It is an endoplasmic-reticulum FKBP-family peptidyl-prolyl isomerase and molecular chaperone, with evidence for calcium binding in a related mammalian protein. HPA places it in an ovary-associated tissue context and in several stromal, fibroblast, hepatic-stellate and germ-cell populations. It also has disease associations involving atrial fibrillation, neurodegenerative disease, stroke and heart failure.
- **Conclusion**: Established evidence supports FKBP7 as a membrane-proximal or endoplasmic-reticulum proteostasis candidate. Its bridge position suggests possible coordination between trafficking and cell-state regulation, but a mechanistic role in the conserved module is not established by the available interaction resources.

#### TOR2A

- **Related proteins** (co-abundance neighbors): MYO1D (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: torsin family 2 member A. This gene encodes a member of the AAA family of adenosine triphosphatases with similarity to Clp proteases and heat shock proteins. Alternative splicing at this locus results in the translation of multiple isoforms of the encoded protein, some of which contain salusin peptides in the C-terminal region. These peptides may play roles in hypotension, myocardial growth and the induction of mitogenesis…
- **Diseases (Open Targets)**: prostate carcinoma (0.069); mathematical ability (0.056); preeclampsia (0.041); brucellosis (0.018); neuroblastoma (0.014)
- **Europe PMC papers**: 161
- **Why important**: TOR2A connects to MYO1D in the module hu.MAP and provides the strongest link to a possible extracellular or vascular readout because HPA annotates it as secreted to blood. Its annotations include torsin-family ATPase similarity, endoplasmic-reticulum and plasma-membrane localization, calcium transport, antimicrobial humoral responses and salusin-related biology. It is also associated with hypotension, myocardial growth and atherosclerosis-related mechanisms in the supplied description, and with preeclampsia among Open Targets associations.
- **Conclusion**: Established evidence supports TOR2A as a membrane and secretory candidate that could connect intracellular organelle biology with circulatory physiology. The proposed role as an extracellular mediator of the whole module is only a hypothesis, since no physical network or complex evidence links it to the other members.
