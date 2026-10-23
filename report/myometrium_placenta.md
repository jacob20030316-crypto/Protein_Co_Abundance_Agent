# Conserved co-abundance modules: myometrium and placenta

## Module 0

**Tissue pair**: myometrium and placenta  
**Genes (7)**: ACO2, ANXA6, HSPA5, CANX, PDIA4, SEC23A, VPS35

### Function

The module is most consistent with an endoplasmic-reticulum protein-handling and membrane-trafficking program, with links to cellular energy metabolism and endosomal transport. CANX, HSPA5, and PDIA4 form a coherent ER quality-control axis involving chaperoning, protein folding, disulfide-bond processing, secretion, and ER-stress homeostasis. SEC23A adds ER-to-Golgi COPII export, while VPS35 represents endosomal-to-Golgi retrieval. ANXA6 may connect membrane dynamics with calcium-dependent trafficking, and ACO2 contributes a mitochondrial metabolic component. No GO or KEGG term passed global correction, so the functional interpretation is based on the gene annotations and network structure rather than statistically significant pathway enrichment. The absence of a globally enriched term does not invalidate the module.

**Cell composition.** This is not predominantly a plasma-protein, secreted-protein, or blood-cell module. Only a minority of its genes are secretome-associated, and all genes have low immune-cell specificity in HPA, arguing against a blood-cell explanation. Most genes show low tissue specificity, with broad cellular relevance rather than a sharply restricted tissue program. The module is detected at the protein level in both myometrium and placenta, although VPS35 and SEC23A are not detected in myometrium in the supplied HPA results. Several genes show cell-type-enhanced expression in trophoblast populations, and some also show enhancement in plasma cells or other specialized cell types. Thus, the shared module could partly reflect common placental or stromal cellular states, but the available evidence does not support interpreting it primarily as blood contamination. Its composition instead favors a conserved intracellular proteostasis and trafficking program that may be active in both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a compact, high-confidence ER-centered interaction core: CANX is connected to HSPA5 and PDIA4, and HSPA5 is also connected to PDIA4. These relationships are biologically concordant with ER chaperoning, folding, and quality control, and they strengthen the interpretation that this part of the co-abundance module reflects a real molecular program rather than an arbitrary correlation. The remaining module relationships, including links involving ANXA6, ACO2, VPS35, and SEC23A, are not represented as high-confidence STRING partners in the supplied results. No hu.MAP complex contains multiple module members. Therefore, the module includes a known ER interaction core embedded within a broader co-abundance pattern, but it is not equivalent to a previously established hu.MAP complex.

**STRING interactions (score >= 0.7)**: 3 of 21 gene pairs: CANX–HSPA5 (0.998); CANX–PDIA4 (0.931); HSPA5–PDIA4 (0.99)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The individual genes and the ER interaction relationships are not novel: HSPA5, CANX, and PDIA4 are well studied, and their mutual STRING relationships are already known. The co-abundance observation may nevertheless represent a potentially new tissue-pair-specific association linking ER quality control with COPII export, endosomal retrieval, membrane regulation, and mitochondrial metabolism in myometrium and placenta. This should be described as a candidate novel module-level observation rather than a proven new biological mechanism. The absence of a hu.MAP complex or of STRING links for some module pairs does not by itself establish novelty. Independent replication, tissue-cell deconvolution, and comparison with existing co-expression resources would be needed to determine whether the full configuration is genuinely new.

**Hypothesis.** Hypothesis: in shared cellular populations of myometrium and placenta, increased demand for synthesis and trafficking of membrane or secreted proteins co-regulates ER folding capacity, ER-to-Golgi export, endosomal recycling, and membrane remodeling. HSPA5, CANX, and PDIA4 could form the proteostasis core; SEC23A could support export from the ER; VPS35 could maintain retrieval and recycling; ANXA6 could couple calcium-sensitive membrane dynamics to trafficking; and ACO2 could reflect the mitochondrial energy demand associated with this activity. This is a mechanistic hypothesis inferred from the annotations and network, not an experimentally demonstrated causal pathway.

### Important genes

#### HSPA5

- **Related proteins** (co-abundance neighbors): CANX (0.82), SEC23A (0.81); STRING partners: CANX (0.998), PDIA4 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in myometrium, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is a central ER chaperone and regulator of ER homeostasis. It has a direct high-confidence STRING relationship with CANX and another with PDIA4, placing it in the best-supported interaction core of the module. It also has extensive literature and is enhanced in trophoblast-related cell populations in the supplied HPA evidence.
- **Conclusion**: Established evidence supports HSPA5 as a core ER folding and stress-homeostasis component of the module. Its central biological role makes it a strong candidate for the module's functional anchor. It is hypothesized, but not proven here, to coordinate the other module components during increased secretory or membrane-trafficking demand.

#### CANX

- **Related proteins** (co-abundance neighbors): PDIA4 (0.91), ANXA6 (0.84), HSPA5 (0.82); STRING partners: HSPA5 (0.998), PDIA4 (0.931)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in myometrium, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is an ER calcium-binding chaperone that assists folding and assembly of newly synthesized glycoproteins and participates in retention of incorrectly folded proteins. It has strong STRING relationships with HSPA5 and PDIA4 and connects the ER interaction core to ANXA6 in the co-abundance network. Its literature base is substantial.
- **Conclusion**: Established evidence supports CANX as a principal ER quality-control and glycoprotein-folding component. Its network position supports a role in the conserved proteostasis portion of the module. A specific role in coordinating calcium-dependent membrane behavior with ER quality control remains a hypothesis.

#### PDIA4

- **Related proteins** (co-abundance neighbors): ANXA6 (0.95), CANX (0.91), ACO2 (0.91); STRING partners: CANX (0.931), HSPA5 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in myometrium, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 is an ER protein-folding enzyme with catalytically active thioredoxin domains and a role in thiol-disulfide interchange, protein secretion, ER-stress responses, and antibody assembly. It is strongly connected to CANX and HSPA5 in STRING and is also connected to ANXA6 and ACO2 in the module network. It has a substantial literature base and is enhanced in several cell populations relevant to placenta and secretory biology.
- **Conclusion**: Established evidence supports PDIA4 as the disulfide-processing and folding component of the ER core. Its placement alongside CANX and HSPA5 gives the module a coherent protein-quality-control interpretation. Its possible coordination with mitochondrial metabolism or membrane regulation is a hypothesis rather than an established function of this module.

#### SEC23A

- **Related proteins** (co-abundance neighbors): HSPA5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A is a COPII component involved in vesicle budding, cargo loading, and ER-to-Golgi transport. Although it is peripheral in the co-abundance network, it links directly to HSPA5 and provides a mechanistic bridge from ER folding to export. Its disease associations and established role in intracellular transport make it important despite its limited network connectivity.
- **Conclusion**: Established evidence supports SEC23A as the ER export component of the module. Its connection to HSPA5 is compatible with coordinated quality control and forward trafficking. The hypothesis that this module controls export of a particular tissue-specific cargo is not established by the supplied data.

#### VPS35

- **Related proteins** (co-abundance neighbors): ACO2 (0.95), ANXA6 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS35 retromer complex component. This gene belongs to a group of vacuolar protein sorting (VPS) genes. The encoded protein is a component of a large multimeric complex, termed the retromer complex, involved in retrograde transport of proteins from endosomes to the trans-Golgi network. The close structural similarity between the yeast and human proteins that make up this complex suggests a similarity in function. Expression studie…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.743); neurodegenerative disease (0.553); young-onset Parkinson disease (0.503); Parkinson disease (0.482); Parkinson disease, dominant (0.370)
- **Europe PMC papers**: 3611
- **Why important**: VPS35 is a retromer component involved in endosome-to-Golgi retrieval, protein transport, and regulation of organelle organization. It connects in the module to ACO2 and ANXA6, extending the network beyond the ER into endosomal and membrane systems. It also has strong disease relevance in the supplied Open Targets summary and a substantial literature base.
- **Conclusion**: Established evidence supports VPS35 as a membrane-protein recycling and retrograde-transport component. Its presence suggests that the module may encompass post-ER trafficking rather than ER folding alone. A direct functional coupling between VPS35 and the ER chaperone core is a plausible hypothesis but is not demonstrated by the supplied STRING or complex evidence.
