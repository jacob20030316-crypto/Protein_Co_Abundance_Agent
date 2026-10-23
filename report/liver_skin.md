# Conserved co-abundance modules: liver and skin

## Module 0

**Tissue pair**: liver and skin  
**Genes (6)**: ACACA, DCTN1, EPS15L1, ITPR2, SEC24D, VAV2

### Function

This is a weakly annotated intracellular co-abundance module rather than a module with a statistically established pathway function. No GO or KEGG term passed global correction, and there was no supplementary STRING functional enrichment. The network topology places ITPR2 at the center, connected to VAV2, SEC24D, DCTN1, and ACACA, while DCTN1 connects to EPS15L1. The annotations nevertheless suggest a possible convergence of intracellular calcium release and signaling through ITPR2, vesicle formation and ER-to-Golgi transport through SEC24D, endocytosis through EPS15L1, microtubule-based transport through DCTN1, small-GTPase signaling through VAV2, and lipid synthesis through ACACA. These are functional clues from individual genes, not evidence of a globally enriched pathway.

**Cell composition.** The module is composed entirely of intracellular proteins; none is annotated as secreted. Protein was detected for every module gene in both liver and skin. Most genes have low tissue specificity, with only ITPR2 showing liver-enhanced expression, so the module is not strongly liver-specific or skin-specific. HPA single-cell annotations are heterogeneous, including neural, renal epithelial, glial, endocrine, and myeloid-related cell types. Two genes have immune-cell-enhanced annotations, but the module is not predominantly blood-cell enriched. The shared signal could therefore reflect broadly expressed cellular machinery, shared cell states, or cellular-composition effects rather than a specialized liver-skin program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction was detected among the module gene pairs at the supplied confidence threshold, and no STRING functional enrichment was present. Thus, the co-abundance edges should not be interpreted as established physical interactions. hu.MAP provides one partial relationship: SEC24D and EPS15L1 both occur in huMAP complex (hu.MAP huMAP3_12394.1), but they represent only a small subset of a very large complex whose other members include proteins involved in vesicle trafficking, coat assembly, endocytosis, and membrane organization. This supports a possible trafficking-related context for part of the module, while also showing that the module is not a complete canonical complex. ITPR2, DCTN1, VAV2, and ACACA had no listed hu.MAP complex membership in the supplied evidence.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12394.1 (SEC24D, EPS15L1; 2/98)

### Novelty

The exact six-gene co-abundance pattern may be a new observation because it is not represented as a connected high-confidence STRING network and is only sparsely represented in hu.MAP. However, absence from those resources does not establish biological novelty: these databases primarily capture physical interactions or curated complexes, whereas co-abundance can arise from shared regulation, cell composition, tissue handling, or indirect pathway coordination. The individual functions are well established, particularly for ITPR2, DCTN1, VAV2, SEC24D, and ACACA, and the partial hu.MAP overlap means the module should be described as a potentially novel cross-tissue co-abundance association rather than a newly discovered molecular complex or pathway.

**Hypothesis.** Hypothesis: in both liver and skin, a shared cellular state may coordinate ER calcium-release capacity, membrane trafficking, cytoskeletal cargo movement, receptor-linked small-GTPase signaling, and lipid biosynthesis. ITPR2 could provide the calcium-sensitive signaling node; SEC24D and EPS15L1 could represent secretory and endocytic membrane traffic; DCTN1 could couple traffic to microtubule transport; VAV2 could connect receptor signals to cytoskeletal or migratory responses; and ACACA could reflect accompanying lipid-production demand. This hypothesis is based on network topology and gene annotations, not on demonstrated physical interactions or globally significant enrichment, and it requires validation with independent cohorts, cell-resolved data, and perturbation experiments.

### Important genes

#### ITPR2

- **Related proteins** (co-abundance neighbors): VAV2 (0.86), SEC24D (0.85), DCTN1 (0.83), ACACA (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum, Mid piece; IHC detected in liver, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inositol 1,4,5-trisphosphate receptor type 2. The protein encoded by this gene belongs to the inositol 1,4,5-triphosphate receptor family, whose members are second messenger intracellular calcium release channels. These proteins mediate a rise in cytoplasmic calcium in response to receptor activated production of inositol triphosphate. Inositol triphosphate receptor-mediated signaling is involved in many processes including cell migration, ce…
- **Diseases (Open Targets)**: isolated anhidrosis with normal sweat glands (0.547); alcohol drinking (0.428); atrial fibrillation (0.394); open-angle glaucoma (0.365); familial hypercholesterolemia (0.333)
- **Europe PMC papers**: 1988
- **Why important**: ITPR2 is the central network gene, connecting the other functional neighborhoods in the module. It encodes an intracellular calcium-release channel, and its annotations include calcium transport, calcium-mediated signaling, receptor-linked phospholipase signaling, migration, and responses to hypoxia. It is liver-enhanced and detected in both tissues, while also showing cell-type-enhanced expression in several epithelial and immune-related cell types. It has extensive literature and multiple disease associations, making it the strongest candidate for organizing the module biologically.
- **Conclusion**: Established evidence supports ITPR2 as an intracellular calcium-signaling component and as the topological hub of this co-abundance module. It is plausible, but not established, that ITPR2 coordinates the other module genes or explains the cross-tissue conservation.

#### DCTN1

- **Related proteins** (co-abundance neighbors): ITPR2 (0.83), EPS15L1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in liver, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynactin subunit 1. This gene encodes the largest subunit of dynactin, a macromolecular complex consisting of 10 subunits ranging in size from 22 to 150 kD. Dynactin binds to both microtubules and cytoplasmic dynein. Dynactin is involved in a diverse array of cellular functions, including ER-to-Golgi transport, the centripetal movement of lysosomes and endosomes, spindle formation, chromosome movement, nuclear positi…
- **Diseases (Open Targets)**: Perry syndrome (0.798); amyotrophic lateral sclerosis (0.764); neuronopathy, distal hereditary motor, type 7B (0.743); cancer (0.547); neurodegenerative disease (0.530)
- **Europe PMC papers**: 1985
- **Why important**: DCTN1 is the major connector between ITPR2 and EPS15L1 and encodes the largest subunit of dynactin. Its established roles include dynein and microtubule binding, ER-to-Golgi transport, endosome and lysosome movement, spindle organization, nuclear positioning, and axonogenesis. It is broadly expressed and detected in both tissues, with substantial literature and strong disease associations involving Perry syndrome, amyotrophic lateral sclerosis, and hereditary motor neuron disease.
- **Conclusion**: Established evidence supports DCTN1 as a core microtubule-based transport and dynactin component. Its position suggests that intracellular cargo movement could link calcium-related and endocytic signals in the module, but that linkage remains a hypothesis.

#### SEC24D

- **Related proteins** (co-abundance neighbors): ITPR2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in liver, skin
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: SEC24 homolog D, COPII component. The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec24p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. This gene product is implicated in the shaping of the vesicle, and also in cargo selection and concentration. Mut…
- **Diseases (Open Targets)**: Cole-Carpenter syndrome (0.753); hereditary disease (0.380); osteogenesis imperfecta type 1 (0.370); Seizure (0.259); Intellectual disability (0.259)
- **Europe PMC papers**: 780
- **Why important**: SEC24D is connected directly to ITPR2 and is one of the two module genes represented in huMAP complex (hu.MAP huMAP3_12394.1). It is a COPII component involved in ER-to-Golgi transport, cargo selection, and vesicle formation. Its disease associations include Cole-Carpenter syndrome and osteogenesis imperfecta, providing strong evidence that altered SEC24D function has organism-level consequences. Its vesicular localization and detection in both tissues support a role in shared intracellular trafficking rather than secretion of the protein itself.
- **Conclusion**: Established evidence supports SEC24D as an ER export and COPII cargo-selection factor, with partial complex-level support from (hu.MAP huMAP3_12394.1). Its module association may indicate coordinated secretory-pathway activity, but no direct interaction with ITPR2 was established by STRING.

#### VAV2

- **Related proteins** (co-abundance neighbors): ITPR2 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in liver, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vav guanine nucleotide exchange factor 2. VAV2 is the second member of the VAV guanine nucleotide exchange factor family of oncogenes. Unlike VAV1, which is expressed exclusively in hematopoietic cells, VAV2 transcripts were found in most tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2008].
- **Diseases (Open Targets)**: cutaneous leishmaniasis (0.503); open-angle glaucoma (0.448); glaucoma (0.373); type 2 diabetes mellitus (0.306); diabetes mellitus (0.301)
- **Europe PMC papers**: 2236
- **Why important**: VAV2 is directly connected to ITPR2 and encodes a guanine-nucleotide exchange factor involved in small-GTPase signaling, receptor-linked immune signaling, cell migration, and platelet activation. It is broadly expressed, has cell-type-enhanced annotations in renal epithelial cells, and is immune-cell enhanced in memory B cells. Its literature is extensive, and disease associations include cutaneous leishmaniasis, glaucoma, and diabetes-related traits.
- **Conclusion**: Established evidence supports VAV2 as a signaling and cytoskeletal-regulatory factor. The module may capture coordinated receptor signaling and calcium responses, but the immune-cell annotation also means that cell-composition effects must be considered.

#### ACACA

- **Related proteins** (co-abundance neighbors): ITPR2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA carboxylase alpha. Acetyl-CoA carboxylase (ACC) is a complex multifunctional enzyme system. ACC is a biotin-containing enzyme which catalyzes the carboxylation of acetyl-CoA to malonyl-CoA, the rate-limiting step in fatty acid synthesis. There are two ACC forms, alpha and beta, encoded by two different genes. ACC-alpha is highly enriched in lipogenic tissues. The enzyme is under long term control at the transcriptio…
- **Diseases (Open Targets)**: neurodegenerative disease (0.550); Alzheimer disease (0.463); lysosomal storage disease (0.460); Parkinson disease (0.460); autoimmune disorder of central nervous system (0.383)
- **Europe PMC papers**: 6268
- **Why important**: ACACA is connected to ITPR2 and encodes acetyl-CoA carboxylase alpha, the rate-limiting enzyme for fatty-acid synthesis and a regulator of malonyl-CoA production. It is highly relevant to liver biology and lipid metabolism, has broad literature coverage, and is associated with neurodegenerative and lysosomal disease contexts. Its cytosolic localization and detection in both tissues make it a useful marker of metabolic state rather than a secreted or plasma protein.
- **Conclusion**: Established evidence supports ACACA as a central lipid-biosynthetic enzyme. Its co-abundance with the calcium-signaling hub could reflect coordinated metabolic and signaling state, but the module does not establish a direct mechanistic connection between lipid synthesis and ITPR2.

#### EPS15L1

- **Related proteins** (co-abundance neighbors): DCTN1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in liver, skin
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: epidermal growth factor receptor pathway substrate 15 like 1. Enables cadherin binding activity. Predicted to be involved in endocytosis and endosomal transport. Located in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: split hand-foot malformation (0.370); lysosomal storage disease (0.310); neurodegenerative disease (0.310); Alzheimer disease (0.310); Parkinson disease (0.310)
- **Europe PMC papers**: 426
- **Why important**: EPS15L1 is connected to DCTN1 and is the second module member represented in huMAP complex (hu.MAP huMAP3_12394.1). It has cadherin-binding activity and is annotated for endocytosis, endosomal transport, and synaptic vesicle endocytosis. Its vesicular localization and detection in both liver and skin support a membrane-trafficking interpretation. It has a smaller literature base than several other module genes, but its placement next to DCTN1 and its partial complex support make it informative for the trafficking component.
- **Conclusion**: Established evidence supports EPS15L1 as an endocytic and endosomal-trafficking factor with partial complex-level support from (hu.MAP huMAP3_12394.1). Its connection to DCTN1 is consistent with coordinated cargo handling, but the module provides no evidence that EPS15L1 physically interacts with DCTN1.

## Module 1

**Tissue pair**: liver and skin  
**Genes (15)**: ACLY, EIF3L, HSPH1, NUP93, PSMC6, PSMC4, PSMC2, PSMD13, RECQL, RUVBL2, CCT5, CCT3, CCT7, XPO1, CSE1L

### Function

The module is best interpreted as a conserved intracellular proteostasis and macromolecular-trafficking program. The strongest primary evidence is coordinated ATP-dependent activity and ATP hydrolysis (GO:MF ATP hydrolysis activity; q_global = 0.000173)(GO:MF ATP-dependent activity; q_global = 0.00024), with a proteasome regulatory-particle and proteasome-accessory-complex component (GO:CC proteasome regulatory particle; q_global = 0.000287)(GO:CC proteasome accessory complex; q_global = 0.000287)(GO:MF proteasome-activating activity; q_global = 0.00343)(GO:CC proteasome regulatory particle, base subcomplex; q_global = 0.0103)(KEGG Proteasome - Homo sapiens (human); q_global = 0.0106)(GO:CC proteasome complex; q_global = 0.0183). The CCT genes, together with HSPH1, support ATP-dependent protein folding and protection from protein misfolding (GO:CC protein folding chaperone complex; q_global = 0.00362)(GO:MF ATP-dependent protein folding chaperone; q_global = 0.00773)(GO:CC chaperonin-containing T-complex; q_global = 0.0103)(GO:MF protein folding chaperone; q_global = 0.0183)(GO:BP protein folding; q_global = 0.0393). RUVBL2 and the CCT genes also provide primary evidence for nuclear-body, Cajal-body, RNA-localization, chromosome-organization, and telomere-maintenance functions (5 globally significant GO/KEGG terms, q_global 0.000287–0.0014; see the table)(GO:BP positive regulation of telomere maintenance; q_global = 0.00362)(GO:BP regulation of telomere maintenance; q_global = 0.0054)(GO:BP positive regulation of chromosome organization; q_global = 0.0054)(7 globally significant GO/KEGG terms, q_global 0.0103–0.0103; see the table)(4 globally significant GO/KEGG terms, q_global 0.0211–0.0232; see the table)(GO:BP regulation of telomere maintenance via telomerase; q_global = 0.0362)(GO:BP regulation of telomere maintenance via telomere lengthening; q_global = 0.0362)(GO:BP telomere maintenance; q_global = 0.0429). XPO1, CSE1L, and NUP93 add a nucleocytoplasmic transport axis (GO:BP RNA localization; q_global = 0.0014)(GO:BP protein localization to nucleus; q_global = 0.00644). Thus, the most coherent interpretation is coordinated protein folding, proteasomal quality control, and regulated movement of macromolecules between the cytoplasm and nucleus. The sperm-related terms (GO:BP binding of sperm to zona pellucida; q_global = 0.0362)(GO:BP sperm-egg recognition; q_global = 0.0362) and the spinocerebellar-ataxia pathway (KEGG Spinocerebellar ataxia - Homo sapiens (human); q_global = 0.0429) should be treated as pleiotropic annotation signals rather than as the central module function.

**Cell composition.** This is an intracellular, broadly expressed module rather than a plasma-protein or secreted-protein module. HPA reports no secreted genes and low immune-cell specificity across the module, arguing against a blood-cell or circulating-protein explanation. Most genes have low tissue specificity, and protein detection is common in both liver and skin. The module therefore plausibly reflects shared cellular machinery present in multiple cell types rather than a liver-specific or skin-specific secretory program. Several genes show cell-type enhancement in reproductive, epithelial, placental, or other specialized populations, while RUVBL2 is tissue-enhanced in testis; these signals may reflect expression differences among cell types, but they do not establish that the liver-skin module is driven by blood contamination. The shared signal is most consistent with ubiquitous proteostasis, nuclear transport, and genome-maintenance machinery.

**GO/KEGG enrichment**: 51 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF ATP hydrolysis activity | 0.000173 | CCT3, CCT5, CCT7, PSMC2, PSMC4, PSMC6, RECQL, RUVBL2 |
| GO:MF ATP-dependent activity | 0.00024 | CCT3, CCT5, CCT7, HSPH1, PSMC2, PSMC4, PSMC6, RECQL, RUVBL2 |
| GO:CC proteasome regulatory particle | 0.000287 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:CC proteasome accessory complex | 0.000287 | PSMC2, PSMC4, PSMC6, PSMD13 |
| GO:BP RNA localization to Cajal body | 0.000287 | CCT3, CCT5, CCT7, RUVBL2 |
| GO:BP telomerase RNA localization to Cajal body | 0.000287 | CCT3, CCT5, CCT7, RUVBL2 |
| GO:BP telomerase RNA localization | 0.000287 | CCT3, CCT5, CCT7, RUVBL2 |
| GO:BP RNA localization to nucleus | 0.000287 | CCT3, CCT5, CCT7, RUVBL2 |
| GO:BP RNA localization | 0.0014 | CCT3, CCT5, CCT7, NUP93, RUVBL2, XPO1 |
| GO:CC intracellular protein-containing complex | 0.00181 | CCT3, CCT5, CCT7, PSMC2, PSMC4, PSMC6, PSMD13, RUVBL2 |
| GO:MF proteasome-activating activity | 0.00343 | PSMC2, PSMC4, PSMC6 |
| GO:BP positive regulation of telomere maintenance | 0.00362 | CCT3, CCT5, CCT7, RUVBL2 |
| GO:CC protein folding chaperone complex | 0.00362 | CCT3, CCT5, CCT7, RUVBL2 |
| GO:BP regulation of telomere maintenance | 0.0054 | CCT3, CCT5, CCT7, RUVBL2 |
| GO:BP positive regulation of chromosome organization | 0.0054 | CCT3, CCT5, CCT7, RUVBL2 |

### STRING and hu.MAP

STRING independently supports the ATPase and ATP-dependent activity interpretation (STRING Function ATP hydrolysis activity; within-query FDR = 1.59e-05)(STRING Function ATP-dependent activity; within-query FDR = 1.59e-05)(STRING Function ATP binding; within-query FDR = 0.0013), the proteasome regulatory-particle cluster (STRING Component Proteasome regulatory particle; within-query FDR = 0.00087)(STRING COMPARTMENTS Proteasome regulatory particle; within-query FDR = 0.00092)(STRING NetworkNeighborAL Proteasome regulatory particle, and Proteasome alpha-type subunit; within-query FDR = 0.00094), and the chaperone/CCT-related cluster (STRING NetworkNeighborAL Unfolded protein binding, and Chaperone complex; within-query FDR = 0.00094)(STRING NetworkNeighborAL Chaperone complex, and Prefoldin; within-query FDR = 0.001). The high-confidence edges form recognizable substructures: CCT3, CCT5, and CCT7 connect with one another and with RUVBL2; PSMC2, PSMC4, PSMC6, and PSMD13 form a proteasome regulatory-particle group; and CSE1L, XPO1, and NUP93 form a nuclear-transport group. hu.MAP confirms that the proteasome genes occur together in multiple proteasome complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1), that the CCT genes recur in several CCT-containing complexes (hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1)(hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1), and that XPO1, CSE1L, and NUP93 recur in nuclear-transport-related complexes (hu.MAP huMAP3_09042.1). The hu.MAP associations are generally partial-complex overlaps, not evidence that every module gene is a physical component of one complex. Collectively, STRING and hu.MAP indicate that the co-abundance structure captures established molecular machines and their coordinated cellular context, with weaker or indirect links between the machines.

**STRING interactions (score >= 0.7)**: 14 of 105 gene pairs: CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–RUVBL2 (0.766); CCT5–CCT7 (0.999); CCT5–RUVBL2 (0.705); CCT7–RUVBL2 (0.802); CSE1L–XPO1 (0.976); NUP93–XPO1 (0.712); PSMC2–PSMC4 (0.999); PSMC2–PSMC6 (0.999); PSMC2–PSMD13 (0.999); PSMC4–PSMC6 (0.999); PSMC4–PSMD13 (0.999); PSMC6–PSMD13 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function ATP hydrolysis activity (FDR = 1.59e-05, 8 genes); Function ATP-dependent activity (FDR = 1.59e-05, 9 genes); TISSUES Lymphoblast (FDR = 9.5e-05, 8 genes); Component Proteasome regulatory particle (FDR = 0.00087, 4 genes); COMPARTMENTS Proteasome regulatory particle (FDR = 0.00092, 4 genes); NetworkNeighborAL Unfolded protein binding, and Chaperone complex (FDR = 0.00094, 5 genes); NetworkNeighborAL Proteasome regulatory particle, and Proteasome alpha-type subunit (FDR = 0.00094, 4 genes); NetworkNeighborAL Chaperone complex, and Prefoldin (FDR = 0.001, 4 genes); RCTM Host Interactions of HIV factors (FDR = 0.0012, 6 genes); RCTM Cell Cycle (FDR = 0.0012, 7 genes); RCTM TCF dependent signaling in response to WNT (FDR = 0.0012, 5 genes); RCTM Regulation of mRNA stability by proteins that bind AU-rich elements (FDR = 0.0012, 5 genes); RCTM MAPK6/MAPK4 signaling (FDR = 0.0012, 5 genes); RCTM Mitotic Anaphase (FDR = 0.0012, 6 genes); Function ATP binding (FDR = 0.0013, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05064.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/31); huMAP3_09656.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/64); huMAP3_13725.1 (PSMC2, PSMC4, PSMC6, PSMD13; 4/69); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_07938.1 (CCT5, CCT3, CCT7; 3/23); huMAP3_06559.1 (CCT5, CCT3, CCT7; 3/25); huMAP3_09042.1 (XPO1, CSE1L, NUP93; 3/26); huMAP3_09191.1 (CCT5, CCT3, CCT7; 3/32); huMAP3_10656.1 (CCT5, CCT3, CCT7; 3/36); huMAP3_14584.1 (CCT5, CCT3, CCT7; 3/61); huMAP3_07170.1 (XPO1, CSE1L; 2/14); huMAP3_06791.1 (XPO1, CSE1L; 2/31); huMAP3_09592.1 (XPO1, CSE1L; 2/95)

### Novelty

The module should not be described as a newly discovered proteasome, CCT chaperonin, or nuclear-export complex: these relationships are already established by STRING and hu.MAP. Its potentially novel aspect is the conservation of a co-abundance program spanning liver and skin and linking proteostasis, nuclear transport, and genome-maintenance components in these tissues. However, the fact sheet alone does not establish that this tissue-pair co-abundance pattern is absent from prior transcriptomic or proteomic studies. Absence of a STRING or hu.MAP record would not prove novelty, and the presence of many known complexes argues for a cautious conclusion: this is a potentially interesting cross-tissue regulatory module, not evidence of a new molecular complex or a new gene function. Direct comparison with published liver-skin co-expression and proteomics studies would be required to claim a new finding.

**Hypothesis.** Hypothesis: in shared liver and skin cell populations, cellular stress or high macromolecular flux co-regulates a proteostasis circuit in which CCT chaperonins and HSPH1 stabilize newly synthesized or stress-sensitive proteins, the proteasome regulatory particle removes damaged or ubiquitinated proteins, and the XPO1-CSE1L-NUP93 transport axis coordinates nuclear-cytoplasmic exchange. RUVBL2 and RECQL may connect this proteostasis state to DNA repair, chromosome organization, and telomere maintenance. ACLY may couple the state to cytosolic acetyl-CoA and lipid-related metabolism. This is a mechanistic model rather than a demonstrated causal pathway; the co-abundance data and enrichment results support coordination, but do not show physical interaction among all module genes, directionality, or tissue-specific causation.

### Important genes

#### CCT5

- **Related proteins** (co-abundance neighbors): PSMC2 (0.90), CCT7 (0.85), RUVBL2 (0.84), PSMC4 (0.83), HSPH1 (0.83), CCT3 (0.81), CSE1L (0.80); STRING partners: CCT3 (0.999), CCT7 (0.999), RUVBL2 (0.705)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_01951.1, huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is the strongest network hub in the supplied module and connects the CCT chaperone group with proteasome, HSPH1, RUVBL2, and nuclear-transport-related neighbors. It is repeatedly supported by primary enrichment for ATP-dependent folding, Cajal-body and telomerase-RNA localization, telomere maintenance, and protein stabilization (GO:MF ATP hydrolysis activity; q_global = 0.000173)(GO:MF ATP-dependent activity; q_global = 0.00024)(5 globally significant GO/KEGG terms, q_global 0.000287–0.0014; see the table)(4 globally significant GO/KEGG terms, q_global 0.00362–0.0054; see the table)(GO:MF ATP-dependent protein folding chaperone; q_global = 0.00773)(GO:CC chaperonin-containing T-complex; q_global = 0.0103)(7 globally significant GO/KEGG terms, q_global 0.0103–0.0103; see the table)(GO:MF protein folding chaperone; q_global = 0.0183) (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 0.0211) (GO:BP positive regulation of telomere maintenance via telomere lengthening; q_global = 0.0211)(6 globally significant GO/KEGG terms, q_global 0.0362–0.0429; see the table). STRING and hu.MAP independently place it in the CCT complex (STRING Function ATP hydrolysis activity; within-query FDR = 1.59e-05)(STRING Function ATP-dependent activity; within-query FDR = 1.59e-05)(STRING NetworkNeighborAL Unfolded protein binding, and Chaperone complex; within-query FDR = 0.00094)(STRING NetworkNeighborAL Chaperone complex, and Prefoldin; within-query FDR = 0.001)(hu.MAP huMAP3_01951.1) (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1)(hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1). It also has substantial literature and a disease association with hereditary sensory and autonomic neuropathy with spastic paraplegia.
- **Conclusion**: Established evidence supports CCT5 as a central ATP-dependent folding component and a structural or functional marker of the CCT arm of the module. Its network position supports a coordinating role, but the data do not prove that CCT5 controls the proteasome or telomere-related signals in liver or skin. A role as a cross-tissue proteostasis integrator is a plausible hypothesis.

#### PSMC2

- **Related proteins** (co-abundance neighbors): CCT5 (0.90), PSMC4 (0.83), PSMC6 (0.80), PSMD13 (0.80); STRING partners: PSMC4 (0.999), PSMC6 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in liver, skin
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is a central member of the proteasome subnetwork and connects to the other module proteasome components. It is present in the primary proteasome, ATPase, ubiquitin-dependent catabolism, and proteasome-regulation terms (4 globally significant GO/KEGG terms, q_global 0.000173–0.000287; see the table)(GO:CC intracellular protein-containing complex; q_global = 0.00181)(GO:MF proteasome-activating activity; q_global = 0.00343)(GO:MF ribonucleoside triphosphate phosphatase activity; q_global = 0.00826)(GO:CC proteasome regulatory particle, base subcomplex; q_global = 0.0103)(9 globally significant GO/KEGG terms, q_global 0.0106–0.0183; see the table)(GO:BP regulation of proteasomal protein catabolic process; q_global = 0.029)(GO:CC endopeptidase complex; q_global = 0.0429)(KEGG Spinocerebellar ataxia - Homo sapiens (human); q_global = 0.0429). STRING gives strong support for its relationships with PSMC4, PSMC6, and PSMD13 (5 supplementary STRING terms; within-query FDR 1.59e-05–0.00092)(STRING NetworkNeighborAL Proteasome regulatory particle, and Proteasome alpha-type subunit; within-query FDR = 0.00094)(7 supplementary STRING terms; within-query FDR 0.0012–0.0013), while hu.MAP places it in multiple proteasome complexes (hu.MAP huMAP3_05064.1) (hu.MAP huMAP3_09656.1) (hu.MAP huMAP3_13725.1). It has substantial literature and disease associations involving plasma-cell malignancy, lymphoma, neoplasia, HIV infection, and amyloidosis.
- **Conclusion**: Established evidence identifies PSMC2 as an ATPase subunit of the proteasome regulatory particle and a major marker of the module's protein-degradation arm. Its inclusion does not by itself establish disease activity or increased proteolysis in liver or skin. It is a strong candidate for testing whether module abundance tracks proteasome capacity or stress adaptation.

#### XPO1

- **Related proteins** (co-abundance neighbors): HSPH1 (0.87), EIF3L (0.80), ACLY (0.80); STRING partners: CSE1L (0.976), NUP93 (0.712)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_09042.1, huMAP3_07170.1, huMAP3_06791.1, huMAP3_09592.1
- **Function (MyGene.info)**: exportin 1. This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSe…
- **Diseases (Open Targets)**: plasma cell myeloma (0.642); B-cell chronic lymphocytic leukemia (0.626); diffuse large B-cell lymphoma (0.602); HIV infectious disease (0.561); neurodegenerative disease (0.522)
- **Europe PMC papers**: 5357
- **Why important**: XPO1 is the main nuclear-export component in the module and links HSPH1 with the CSE1L-NUP93 transport group. It contributes to primary RNA and protein localization, nuclear localization, proteasome-regulation, and ubiquitin-dependent catabolism terms (GO:BP RNA localization; q_global = 0.0014)(GO:BP protein localization to nucleus; q_global = 0.00644)(GO:BP proteasome-mediated ubiquitin-dependent protein catabolic process; q_global = 0.0142)(GO:BP regulation of proteasomal protein catabolic process; q_global = 0.029). STRING supports its relationships with CSE1L and NUP93 (6 supplementary STRING terms; within-query FDR 0.0012–0.0012), and hu.MAP places it in several transport-associated complexes (hu.MAP huMAP3_09042.1)(hu.MAP huMAP3_07170.1) (hu.MAP huMAP3_06791.1) (hu.MAP huMAP3_09592.1). XPO1 has substantial literature and prominent disease associations involving plasma-cell myeloma, B-cell chronic lymphocytic leukemia, diffuse large B-cell lymphoma, HIV infection, and neurodegenerative disease.
- **Conclusion**: Established evidence supports XPO1 as a nuclear-export factor and a bridge between nuclear transport and the broader module. Its network position makes it a plausible coordination point, but the module does not demonstrate altered export flux or causal control of proteostasis. The proposed bridge function remains a hypothesis requiring transport and localization measurements.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): CCT5 (0.84); STRING partners: CCT3 (0.766), CCT5 (0.705), CCT7 (0.802)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 is an ATPase and DNA-helicase-associated factor connected to the CCT group and annotated for DNA repair, DNA recombination, replication regulation, telomere maintenance, and nuclear-body processes (GO:MF ATP hydrolysis activity; q_global = 0.000173)(GO:MF ATP-dependent activity; q_global = 0.00024)(5 globally significant GO/KEGG terms, q_global 0.000287–0.0014; see the table)(GO:BP positive regulation of telomere maintenance; q_global = 0.00362)(GO:BP regulation of telomere maintenance; q_global = 0.0054)(GO:BP positive regulation of chromosome organization; q_global = 0.0054)(GO:MF ribonucleoside triphosphate phosphatase activity; q_global = 0.00826)(6 globally significant GO/KEGG terms, q_global 0.015–0.0165; see the table)(GO:CC microtubule cytoskeleton; q_global = 0.0232)(GO:BP regulation of chromosome organization; q_global = 0.0232)(GO:BP protein folding; q_global = 0.0393)(GO:BP telomere maintenance; q_global = 0.0429). STRING supports its links to CCT3, CCT5, and CCT7 (STRING Function ATP hydrolysis activity; within-query FDR = 1.59e-05)(STRING Function ATP-dependent activity; within-query FDR = 1.59e-05)(STRING NetworkNeighborAL Unfolded protein binding, and Chaperone complex; within-query FDR = 0.00094)(STRING NetworkNeighborAL Chaperone complex, and Prefoldin; within-query FDR = 0.001)(STRING Function ATP binding; within-query FDR = 0.0013). Although it lacks a listed hu.MAP complex in this module, it has substantial literature and disease associations including hypogonadotropic hypogonadism, neurodegenerative disease, hepatocellular carcinoma, and neoplasia. Its testis-enhanced HPA profile and reproductive cell-type associations are notable but do not define the liver-skin module.
- **Conclusion**: Established evidence supports RUVBL2 as an ATPase/helicase-related factor associated with genome maintenance and telomere biology, and as a connection to the CCT arm. The module supports coordinated proteostasis and genome-maintenance activity, but does not prove that RUVBL2 mediates the connection or that telomere maintenance is altered in either tissue. Its bridging role is a testable hypothesis.

#### ACLY

- **Related proteins** (co-abundance neighbors): CSE1L (0.83), NUP93 (0.82), HSPH1 (0.82), XPO1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP citrate lyase. ATP citrate lyase is the primary enzyme responsible for the synthesis of cytosolic acetyl-CoA in many tissues. The enzyme is a tetramer (relative molecular weight approximately 440,000) of apparently identical subunits. It catalyzes the formation of acetyl-CoA and oxaloacetate from citrate and CoA with a concomitant hydrolysis of ATP to ADP and phosphate. The product, acetyl-CoA, serves several im…
- **Diseases (Open Targets)**: familial hypercholesterolemia (0.532); Hypercholesterolemia (0.532); atherosclerosis (0.470); inherited lipid metabolism disorder (0.467); cardiovascular disorder (0.449)
- **Europe PMC papers**: 7957
- **Why important**: ACLY is a metabolically distinctive member of an otherwise strongly proteostasis- and transport-oriented module. It connects in the module network to CSE1L, NUP93, HSPH1, and XPO1, and contributes to primary ATP-binding, adenyl-ribonucleotide-binding, and microtubule-cytoskeleton terms (GO:MF ATP binding; q_global = 0.015)(GO:MF adenyl ribonucleotide binding; q_global = 0.0156)(GO:CC microtubule cytoskeleton; q_global = 0.0232). It has no listed STRING partner or hu.MAP complex in the supplied evidence, so its network inclusion is less independently validated than the proteasome and CCT groups. ACLY has extensive literature and disease associations involving familial and general hypercholesterolemia, atherosclerosis, inherited lipid-metabolism disorders, and cardiovascular disease.
- **Conclusion**: Established evidence supports ACLY as the cytosolic ATP-dependent source of acetyl-CoA for lipid and cholesterol biosynthesis. Its presence suggests a possible metabolic coupling to the module, but the enrichment and interaction evidence do not establish that ACLY drives the proteostasis program. A metabolism-proteostasis link is therefore a hypothesis, not an established function of this module.

## Module 2

**Tissue pair**: liver and skin  
**Genes (7)**: ATP1A1, ATP2A2, ICAM1, ALDH18A1, AARS2, IARS2, TECR

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established pathway-level annotation from those analyses. The strongest functional interpretation is a membrane and organelle homeostasis module centered on ion transport, calcium handling, mitochondrial translation, amino-acid metabolism, and lipid biosynthesis. ATP1A1 and ATP2A2 provide the clearest functional anchor: ATP1A1 maintains sodium and potassium electrochemical gradients, while ATP2A2 transports calcium into the sarcoplasmic or endoplasmic reticulum. Their shared P-type cation-transport annotations are independently reflected by the supplementary STRING terms (STRING SMART Cation transporter/ATPase, N-terminus; within-query FDR = 0.0239), (STRING Pfam E1-E2 ATPase; within-query FDR = 0.0325), (STRING Pfam Cation transporting ATPase, C-terminus; within-query FDR = 0.0325), and (STRING Pfam Cation transport ATPase (P-type); within-query FDR = 0.0325). AARS2 and IARS2 support mitochondrial protein synthesis, ALDH18A1 supports mitochondrial amino-acid biosynthesis, and TECR supports endoplasmic-reticulum fatty-acid and sphingolipid metabolism. ICAM1 adds a cell-surface adhesion and immune-interaction component. Thus, the most defensible interpretation is coordinated cellular maintenance involving ion gradients, calcium and membrane physiology, mitochondrial proteostasis, and lipid handling, rather than a single narrowly defined pathway.

**Cell composition.** The module is not dominated by secreted proteins or blood-cell-enriched genes: the HPA summary reports no secreted genes and low immune-cell specificity for every member. Protein detection is present throughout skin and only partial in liver, which is compatible with tissue-specific regulation or cellular-composition differences between the tissues. Three genes have low tissue specificity, three are tissue enhanced, and one is group enriched; the enriched tissues are heterogeneous and include parathyroid gland, muscle, tongue, salivary gland, lung, and urinary bladder rather than a single liver or skin program. Five genes show cell-type-enhanced expression, including epithelial, muscle, renal, intestinal, and salivary cell types. ICAM1 is associated with endothelial and immune-related cells and has alveolar-cell, Kupffer-cell, macrophage, and monocyte enhancement, but the uniformly low blood-cell specificity argues against interpreting the whole module as a blood-cell contamination signature. The module therefore appears more consistent with shared cellular physiology, with possible contributions from particular epithelial, parenchymal, or stromal cell populations, than with a plasma-protein or circulating-blood program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The network contains two high-confidence STRING relationships. ATP1A1--ATP2A2 is consistent with the shared cation-transport interpretation and is also represented in hu.MAP complex C1. AARS2--IARS2 is a particularly strong known relationship linking two mitochondrial aminoacyl-tRNA synthetases and is represented in hu.MAP complexes C2 and C3. hu.MAP C1 additionally places TECR with ATP1A1 and ATP2A2 in a larger membrane-associated complex context, although the module contains only a subset of that complex. hu.MAP C2 and C3 place ALDH18A1, AARS2, and IARS2 within larger mitochondrial metabolic and translation-associated assemblies. These results show that several module edges or functional groupings are supported by prior interaction and complex evidence, while the remaining co-abundance links are not established physical interactions in STRING or hu.MAP. STRING enrichment (STRING SMART Cation transporter/ATPase, N-terminus; within-query FDR = 0.0239) through (STRING Pfam Cation transport ATPase (P-type); within-query FDR = 0.0325) is supplementary and is driven by the ATP1A1 and ATP2A2 pair; it is not global enrichment evidence.

**STRING interactions (score >= 0.7)**: 2 of 21 gene pairs: AARS2–IARS2 (0.918); ATP1A1–ATP2A2 (0.82)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Cation transporter/ATPase, N-terminus (FDR = 0.0239, 2 genes); Pfam E1-E2 ATPase (FDR = 0.0325, 2 genes); Pfam Cation transporting ATPase, C-terminus (FDR = 0.0325, 2 genes); Pfam Cation transport ATPase (P-type) (FDR = 0.0325, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10473.1 (ATP1A1, ATP2A2, TECR; 3/24); huMAP3_10525.1 (ALDH18A1, AARS2, IARS2; 3/33); huMAP3_13468.1 (ALDH18A1, AARS2, IARS2; 3/99)

### Novelty

This module should not be called entirely new because the ATP1A1--ATP2A2 relationship, the AARS2--IARS2 relationship, and the relevant hu.MAP complex memberships are already known. At the same time, the liver-skin co-abundance organization of these genes may be a novel systems-level observation, particularly because the module combines two established mitochondrial synthetases with ion pumps, a lipid-biosynthesis enzyme, a proline and ornithine biosynthesis enzyme, and ICAM1. Absence of some edges from STRING or hu.MAP does not establish novelty: it may reflect incomplete interaction coverage, context dependence, tissue composition, or co-regulation rather than a previously undiscovered molecular interaction. The appropriate conclusion is therefore partial novelty at the tissue-pair network or co-abundance level, with several components grounded in prior biology.

**Hypothesis.** Hypothesis: in liver and skin, a shared cellular state may coordinate membrane ion gradients and calcium sequestration with mitochondrial translational capacity, amino-acid metabolism, and endoplasmic-reticulum lipid remodeling. ATP1A1 could mark plasma-membrane electrochemical maintenance, ATP2A2 could couple that state to intracellular calcium control, and TECR could support the associated membrane-lipid requirements. AARS2 and IARS2 could indicate a linked mitochondrial protein-synthesis demand, while ALDH18A1 could support mitochondrial amino-acid and nitrogen metabolism. ICAM1 may reflect an accompanying adhesion or local inflammatory-interface state rather than a core biochemical component. This is a mechanistic model generated from co-abundance and prior annotations, not a demonstrated causal pathway; it requires experimental testing of cell type, subcellular localization, and condition-specific regulation.

### Important genes

#### ATP1A1

- **Related proteins** (co-abundance neighbors): ALDH18A1 (0.85), ATP2A2 (0.81), ICAM1 (0.80); STRING partners: ATP2A2 (0.82)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Plasma membrane; IHC detected in liver, skin
- **hu.MAP 3.0**: huMAP3_10473.1
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit alpha 1. The protein encoded by this gene belongs to the family of P-type cation transport ATPases, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organi…
- **Diseases (Open Targets)**: Charcot-Marie-tooth disease, axonal, type 2DD (0.790); hypomagnesemia, seizures, and intellectual disability 2 (0.722); congestive heart failure (0.603); atrial fibrillation (0.596); heart failure (0.580)
- **Europe PMC papers**: 3782
- **Why important**: ATP1A1 is the most connected gene in the module and links ALDH18A1, ATP2A2, and ICAM1. It is detected in both liver and skin, localizes to the plasma membrane and vesicles, and has an established role in maintaining sodium and potassium gradients. Its direct STRING relationship with ATP2A2 and membership in hu.MAP complex C1 make it a central network anchor. It also has extensive literature and disease associations involving neuropathy, electrolyte-related neurological disease, and cardiac disorders.
- **Conclusion**: Established evidence supports ATP1A1 as a central ion-homeostasis component and as one of the strongest anchors of the module. It is plausible, but not proven, that its co-abundance links membrane transport to the mitochondrial and lipid-related genes.

#### ATP2A2

- **Related proteins** (co-abundance neighbors): TECR (0.82), ATP1A1 (0.81), AARS2 (0.81); STRING partners: ATP1A1 (0.82)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_10473.1
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darie…
- **Diseases (Open Targets)**: Darier disease (0.823); acrokeratosis verruciformis (0.663); neurodegenerative disease (0.507); hereditary disease (0.416); schizophrenia (0.406)
- **Europe PMC papers**: 9327
- **Why important**: ATP2A2 has high connectivity and links TECR, ATP1A1, and AARS2. It is the module's clearest calcium-handling gene, is represented with ATP1A1 in STRING and hu.MAP complex C1, and is detected in skin. Its annotations connect calcium transport, intracellular calcium homeostasis, cell adhesion, and epidermis development. Its association with Darier disease gives the gene direct relevance to skin biology, and it has extensive literature.
- **Conclusion**: Established evidence supports ATP2A2 as a major calcium and membrane-homeostasis component with particular relevance to skin. The proposed coordination between calcium handling and the mitochondrial or lipid genes remains a hypothesis rather than a demonstrated mechanism.

#### AARS2

- **Related proteins** (co-abundance neighbors): IARS2 (0.81), ATP2A2 (0.81); STRING partners: IARS2 (0.918)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in liver, skin
- **hu.MAP 3.0**: huMAP3_10525.1, huMAP3_13468.1
- **Function (MyGene.info)**: alanyl-tRNA synthetase 2, mitochondrial. The protein encoded by this gene belongs to the class-II aminoacyl-tRNA synthetase family. Aminoacyl-tRNA synthetases play critical roles in mRNA translation by charging tRNAs with their cognate amino acids. The encoded protein is a mitochondrial enzyme that specifically aminoacylates alanyl-tRNA. Mutations in this gene are a cause of combined oxidative phosphorylation deficiency 8. [provided by R…
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 8 (0.789); leukoencephalopathy, progressive, with ovarian failure (0.767); ovarioleukodystrophy (0.619); neurodegenerative disease (0.536); hereditary disease (0.503)
- **Europe PMC papers**: 789
- **Why important**: AARS2 occupies an internally connected position through IARS2 and ATP2A2 and has a strong STRING relationship with IARS2. It is detected in both tissues and belongs to hu.MAP complexes C2 and C3 with IARS2 and ALDH18A1. Its established function is mitochondrial alanyl-tRNA charging and support of mitochondrial translation, and its disease associations include combined oxidative-phosphorylation deficiency and neurological syndromes.
- **Conclusion**: Established evidence supports AARS2 as a mitochondrial translation component and as part of a known AARS2--IARS2 relationship. Its connection to the ion-pump branch may indicate coordinated cellular demand or shared regulation, but a direct functional coupling is not established by the supplied evidence.

#### IARS2

- **Related proteins** (co-abundance neighbors): AARS2 (0.81); STRING partners: AARS2 (0.918)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in liver, skin
- **hu.MAP 3.0**: huMAP3_10525.1, huMAP3_13468.1
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 2, mitochondrial. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Two forms of isoleucine-tRNA synthetase exist, a cytoplasmic form and a mitochondrial form. This gene encodes th…
- **Diseases (Open Targets)**: cataract-growth hormone deficiency-sensory neuropathy-sensorineural hearing loss-skeletal dysplasia syndrome (0.724); Leigh syndrome (0.563); hereditary disease (0.416); neurodegenerative disease (0.411); mitochondrial disease (0.374)
- **Europe PMC papers**: 411
- **Why important**: IARS2 forms the module's strongest-supported mitochondrial pair with AARS2 and belongs with AARS2 and ALDH18A1 in hu.MAP complexes C2 and C3. It contributes mitochondrial isoleucine-tRNA aminoacylation and mitochondrial translation, is detected in both liver and skin, and has disease associations including Leigh syndrome and other mitochondrial or hereditary disorders. Although its module degree is limited, its relationship with AARS2 is highly informative for interpreting the mitochondrial branch.
- **Conclusion**: Established evidence supports IARS2 as a mitochondrial translation gene that reinforces the AARS2-centered substructure. Its presence does not by itself prove that the full module is a mitochondrial pathway; the broader interpretation remains a hypothesis based on network context.

#### TECR

- **Related proteins** (co-abundance neighbors): ATP2A2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in liver, skin
- **hu.MAP 3.0**: huMAP3_10473.1
- **Function (MyGene.info)**: trans-2,3-enoyl-CoA reductase. This gene encodes a multi-pass membrane protein that resides in the endoplasmic reticulum, and belongs to the steroid 5-alpha reductase family. The elongation of microsomal long and very long chain fatty acid consists of 4 sequential reactions. This protein catalyzes the final step, reducing trans-2,3-enoyl-CoA to saturated acyl-CoA. Alternatively spliced transcript variants have been found for th…
- **Diseases (Open Targets)**: neurodegenerative disease (0.503); autosomal recessive non-syndromic intellectual disability (0.407); systemic lupus erythematosus (0.199); jaw disease (0.198); esophageal squamous cell carcinoma (0.074)
- **Europe PMC papers**: 425
- **Why important**: TECR links directly to ATP2A2 and is included with ATP1A1 and ATP2A2 in hu.MAP complex C1. It is detected in both tissues and resides in the endoplasmic reticulum, where it catalyzes a step in long-chain and very-long-chain fatty-acid elongation and is associated with sphingolipid metabolism. Its tissue and cell-type pattern includes epithelial and reproductive cell types, and its disease associations include neurological and other disorders, although its literature volume is more limited than that of the ion pumps or ICAM1.
- **Conclusion**: Established evidence supports TECR as an endoplasmic-reticulum lipid-metabolism component connected to the ATP2A2 branch. It is a plausible membrane-remodeling partner in the proposed module, but the co-abundance data do not establish a direct biochemical interaction with ATP2A2.

#### ICAM1

- **Related proteins** (co-abundance neighbors): ATP1A1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: intercellular adhesion molecule 1. This gene encodes a cell surface glycoprotein which is typically expressed on endothelial cells and cells of the immune system. It binds to integrins of type CD11a / CD18, or CD11b / CD18 and is also exploited by Rhinovirus as a receptor. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.528); atrial fibrillation (0.407); vascular disorder (0.358); Crohn disease (0.340); lymphatic system disorder (0.285)
- **Europe PMC papers**: 19543
- **Why important**: ICAM1 is connected to ATP1A1 and provides the module with a distinct cell-surface adhesion and immune-interface signal. It is enriched in lung and urinary bladder tissue and in several epithelial or myeloid-associated cell types, while remaining low in blood-cell specificity according to HPA. Its established roles include leukocyte adhesion, extravasation, immune responses, and cell adhesion. It has the largest literature volume among the module genes and broad disease associations, including vascular, inflammatory, cardiac, and neurological conditions.
- **Conclusion**: Established evidence supports ICAM1 as a cell-adhesion and immune-interface marker rather than as a core ion-transport or mitochondrial enzyme. Its association with ATP1A1 may reflect shared cellular state or cell composition; a direct mechanistic link within this module is currently only a hypothesis.

## Module 3

**Tissue pair**: liver and skin  
**Genes (9)**: CENPV, CASK, ELP1, FLOT1, MAN2A1, NUP205, MRPL11, SACM1L, TM9SF2

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent; therefore the module does not support a statistically established pathway-level functional label. Its gene-level annotations instead suggest a heterogeneous set of intracellular processes: Golgi N-glycan maturation through MAN2A1, phosphoinositide metabolism and Golgi organization through SACM1L, membrane organization and vesicle trafficking through FLOT1 and TM9SF2, intracellular scaffolding and adhesion-related functions through CASK, translation-related functions through ELP1 and MRPL11, nuclear transport through NUP205, and cytokinesis or chromosome organization through CENPV. The co-abundance pattern is therefore best described as a putative shared intracellular membrane-trafficking, organelle-maintenance, and cell-state module rather than as an established canonical pathway. These interpretations are gene-level evidence and hypotheses, not globally significant enrichment findings.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. All genes have low tissue specificity, and protein detection is generally present in both liver and skin where data are available, although MAN2A1 was detected in liver but not skin and NUP205 had no immunohistochemistry detection in either tissue. The single-cell annotations are mixed, including enteric, reproductive, glial, adrenal, epithelial, and immune-cell signals. Blood-cell annotations include enhanced or enriched signals for basophils, eosinophils, memory B cells, and neutrophils, but most genes have low immune-cell specificity. This mixture means the shared module could partly reflect broadly expressed cellular programs, variable cell composition, or blood-cell contributions in tissue samples; the data do not establish a liver-skin-specific mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was reported among the module genes, and no hu.MAP complex contained multiple module members. Thus the co-abundance edges are not supported here by known physical or functional interactions in those resources. The absence of database-supported relationships does not show that the genes cannot interact, but it does make a single coherent protein complex or well-established interaction network unlikely on the current evidence. The strongest internal co-abundance bridge is MAN2A1, which connects to CASK, ELP1, MRPL11, SACM1L, and NUP205; the remaining links form smaller associations involving CASK with TM9SF2 and SACM1L with CENPV and FLOT1. These are observed network relationships, not established molecular interactions.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a previously unreported co-abundance association in the liver-skin comparison, because the module has no high-confidence STRING interactions, no multi-member hu.MAP complex, and no globally significant GO/KEGG term. However, those absences alone do not establish novelty: they may reflect incomplete database coverage, tissue-specific regulation, indirect co-regulation, cell-composition effects, or a data-driven association. The defensible conclusion is that the module represents a potentially novel cross-tissue co-abundance pattern whose biological novelty requires replication in independent cohorts, control for cell composition, and experimental or orthogonal molecular validation.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of intracellular membrane and organelle homeostasis across liver and skin cells. In this model, MAN2A1-dependent glycan processing, SACM1L-dependent phosphoinositide control, TM9SF2-related endosomal function, and FLOT1-related membrane trafficking are coupled to CASK-mediated scaffolding, while ELP1, MRPL11, NUP205, and CENPV represent translation, mitochondrial, nuclear-transport, and cell-division state components. The association could arise from a shared cellular stress, differentiation, or proliferative state, or from mixed cell populations including immune cells. This is a mechanistic model generated from gene annotations and network structure, not a demonstrated causal pathway.

### Important genes

#### MAN2A1

- **Related proteins** (co-abundance neighbors): CASK (0.86), ELP1 (0.86), MRPL11 (0.84), SACM1L (0.83), NUP205 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Golgi apparatus; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosidase alpha class 2A member 1. This gene encodes a glycosyl hydrolase that localizes to the Golgi and catalyzes the final hydrolytic step in the asparagine-linked oligosaccharide (N-glycan) maturation pathway. Mutations in the mouse homolog of this gene have been shown to cause a systemic autoimmune disease similar to human systemic lupus erythematosus. [provided by RefSeq, Dec 2013].
- **Diseases (Open Targets)**: alcohol drinking (0.456); schizophrenia (0.455); COVID-19 (0.370); smoking initiation (0.364); dislocation (0.344)
- **Europe PMC papers**: 663
- **Why important**: MAN2A1 is the central network connector in the module and links genes spanning membrane, nuclear, translational, and trafficking annotations. Its established function is a Golgi glycosyl hydrolase involved in the final step of N-glycan maturation. It is detected in liver, has a reported autoimmune phenotype in the mouse homolog, and has substantial literature coverage. These features make it the strongest candidate for anchoring the module in Golgi and glycoprotein-processing biology.
- **Conclusion**: Established: MAN2A1 performs Golgi N-glycan processing and is the most connected module gene. Hypothesis: its co-abundance with the other genes may mark coordinated Golgi function or a broader organelle-state program. The module does not establish that MAN2A1 causally controls the other genes.

#### SACM1L

- **Related proteins** (co-abundance neighbors): CENPV (0.87), MAN2A1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus; IHC detected in liver, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SAC1 like phosphatidylinositide phosphatase. This gene encodes an integral membrane protein, which is localized to the endoplasmic reticulum, and functions as a phosphoinositide phosphatase that hydrolyzes phosphatidylinositol 3-phosphate, phosphatidylinositol 4-phosphate, and phosphatidylinositol 3,5-bisphosphate. Deletion of this gene in mouse results in preimplantation lethality. Other studies suggest that this gene is also involved in th…
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); placenta praevia (0.352); alcohol drinking (0.193); autoimmune disorder of central nervous system (0.175); digestive system disorder (0.077)
- **Europe PMC papers**: 1120
- **Why important**: SACM1L connects MAN2A1 with CENPV and contributes a membrane-lipid regulatory axis to the module. It is an integral membrane phosphoinositide phosphatase associated with the endoplasmic reticulum and Golgi, and it has reported roles in Golgi organization and mitotic-spindle organization. Its function provides a plausible bridge between membrane homeostasis and cell-state changes.
- **Conclusion**: Established: SACM1L regulates phosphoinositide pools and is implicated in Golgi and mitotic organization. Hypothesis: SACM1L may connect membrane remodeling with the proliferative or differentiation state represented by the module. Direct cooperation with MAN2A1 or CENPV is not established by the supplied interaction databases.

#### CASK

- **Related proteins** (co-abundance neighbors): MAN2A1 (0.86), TM9SF2 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm; IHC detected in liver, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium/calmodulin dependent serine protein kinase. This gene encodes a calcium/calmodulin-dependent serine protein kinase. The encoded protein is a MAGUK (membrane-associated guanylate kinase) protein family member. These proteins are scaffold proteins and the encoded protein is located at synapses in the brain. Mutations in this gene are associated with FG syndrome 4, intellectual disability and microcephaly with pontine and cerebellar hypoplasia…
- **Diseases (Open Targets)**: syndromic X-linked intellectual disability Najm type (0.829); FG syndrome 4 (0.800); cask-related x-linked intellectual disability (0.667); FG syndrome (0.567); hereditary disease (0.531)
- **Europe PMC papers**: 3838
- **Why important**: CASK is a network intermediary linking MAN2A1 and TM9SF2. It is a calcium/calmodulin-dependent serine protein kinase and MAGUK-family scaffold with annotations involving cell adhesion, protein localization, transport, and keratinocyte proliferation. It is detected in both liver and skin and has extensive disease and literature associations, including X-linked intellectual-disability syndromes.
- **Conclusion**: Established: CASK is a scaffold and signaling protein with roles in localization, adhesion, and transport. Hypothesis: CASK could couple membrane or endosomal organization to tissue-cell-state regulation in this module. Its neuronal disease associations do not demonstrate a liver-skin mechanism.

#### FLOT1

- **Related proteins** (co-abundance neighbors): CENPV (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Golgi apparatus; IHC detected in liver, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: flotillin 1. This gene encodes an protein that localizes to the caveolae, which are small domains on the inner cell membranes. This protein plays a role in vesicle trafficking and cell morphology. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016].
- **Diseases (Open Targets)**: neurodegenerative disease (0.332); gastric cancer (0.101); hepatocellular carcinoma (0.101); neoplasm (0.097); lung adenocarcinoma (0.093)
- **Europe PMC papers**: 3298
- **Why important**: FLOT1 is linked to CENPV and contributes a membrane-domain and trafficking perspective. It localizes to caveolar membrane domains and is annotated for vesicle trafficking, cell morphology, receptor internalization, cell-cell junction assembly, and extracellular matrix disassembly. It is detected in both tissues and has substantial literature coverage, including studies of neutrophils and cancer-related conditions.
- **Conclusion**: Established: FLOT1 participates in membrane organization, trafficking, and junctional processes. Hypothesis: its association with CENPV may reflect coordinated membrane remodeling during migration, differentiation, or cell-state transitions. The supplied evidence does not prove a direct FLOT1-CENPV interaction.

#### ELP1

- **Related proteins** (co-abundance neighbors): MAN2A1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in liver, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: elongator acetyltransferase complex subunit 1. The protein encoded by this gene is a scaffold protein and a regulator for three different kinases involved in proinflammatory signaling. The encoded protein can bind NF-kappa-B-inducing kinase and I-kappa-B kinases through separate domains and assemble them into an active kinase complex. Mutations in this gene have been associated with familial dysautonomia. Alternative splicing results in multip…
- **Diseases (Open Targets)**: Riley-Day syndrome (0.807); medulloblastoma (0.721); primary dysautonomia (0.407); hereditary sensory and autonomic neuropathy (0.374); mathematical ability (0.361)
- **Europe PMC papers**: 960
- **Why important**: ELP1 is directly connected to the central MAN2A1 node and adds a translation and inflammatory-signaling dimension. It is a scaffold for the elongator acetyltransferase complex and can assemble kinase complexes involved in proinflammatory signaling; it is also associated with familial dysautonomia. Its presence suggests that the module may include regulation of protein synthesis or inflammatory cell state rather than only membrane biology.
- **Conclusion**: Established: ELP1 has roles in tRNA modification, translation regulation, and proinflammatory signaling. Hypothesis: ELP1 may indicate a shared translational or inflammatory state that helps explain the cross-tissue co-abundance pattern. The data do not establish that ELP1 mediates the MAN2A1 association.

## Module 4

**Tissue pair**: liver and skin  
**Genes (17)**: DHX9, MACROH2A1, HNRNPR, IMPDH2, LMNB1, MATR3, NOP56, PPM1G, RPL12, RPL3, RPL6, SF3A1, SF3B3, SUPT16H, EPRS1, IARS1, MARS1

### Function

This is a conserved nuclear gene-expression and RNA-processing module. The strongest primary evidence is the broad enrichment for nucleic-acid binding (GO:MF nucleic acid binding; q_global = 4.48e-06), RNA binding (GO:MF RNA binding; q_global = 0.000122), ribonucleoprotein complexes (GO:CC ribonucleoprotein complex; q_global = 0.000239), gene expression (GO:BP gene expression; q_global = 0.000529), macromolecule biosynthesis (GO:BP macromolecule biosynthetic process; q_global = 0.00119), RNA metabolism (GO:BP RNA metabolic process; q_global = 0.0111), biosynthesis (GO:BP biosynthetic process; q_global = 0.0133), the cytosolic large ribosomal subunit (GO:CC cytosolic large ribosomal subunit; q_global = 0.0141), and nucleic-acid metabolism (GO:BP nucleic acid metabolic process; q_global = 0.0341). The module therefore appears to couple pre-mRNA processing and RNA handling with ribosome biogenesis or function, translation, and chromatin-associated transcriptional control. The near-complete membership of the module in the gene-expression and biosynthetic terms supports a coherent housekeeping-like expression program rather than a narrowly tissue-specific pathway. The cytosolic large-ribosomal-subunit signal is driven by RPL12, RPL3, and RPL6 (GO:CC cytosolic large ribosomal subunit; q_global = 0.0141), while NOP56, SF3A1, SF3B3, HNRNPR, DHX9, and MATR3 connect the module to RNA processing and ribonucleoprotein biology. EPRS1, IARS1, and MARS1 provide a translation and tRNA-aminoacylation arm. SUPT16H, LMNB1, MACROH2A1, and PPM1G add chromatin, nuclear-envelope, and splicing-regulatory context. Overall, the most defensible interpretation is coordinated maintenance of nuclear RNA production and processing together with protein-synthesis capacity.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and the proteins are detected in liver and skin for nearly all or all members. It is also not blood-cell enriched according to HPA, which reports low immune-cell specificity for every gene and no enriched blood-cell category. Most genes have low tissue specificity, consistent with broadly expressed cellular machinery. Some single-cell enrichments occur in specialized populations, including epithelial, germline, erythrocyte-progenitor, neutrophil, stromal, and monocyte-progenitor populations, but these are heterogeneous rather than a single coherent blood signature. The shared liver-skin signal is therefore more plausibly related to common cellular RNA, chromatin, splicing, ribosome, and biosynthetic programs than to plasma contamination or a dominant immune-cell component. HPA protein detection in both tissues supports biological presence, while the lack of tissue specificity cautions against interpreting the module as liver- or skin-specific.

**GO/KEGG enrichment**: 9 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleic acid binding | 4.48e-06 | DHX9, EPRS1, HNRNPR, IARS1, IMPDH2, LMNB1, MACROH2A1, MARS1, MATR3, NOP56, RPL12, RPL3, RPL6, SF3A1, SF3B3, SUPT16H |
| GO:MF RNA binding | 0.000122 | DHX9, EPRS1, HNRNPR, IARS1, IMPDH2, MARS1, MATR3, NOP56, RPL12, RPL3, RPL6, SF3A1, SF3B3, SUPT16H |
| GO:CC ribonucleoprotein complex | 0.000239 | DHX9, EPRS1, HNRNPR, NOP56, RPL12, RPL3, RPL6, SF3A1, SF3B3 |
| GO:BP gene expression | 0.000529 | DHX9, EPRS1, HNRNPR, IARS1, LMNB1, MACROH2A1, MARS1, MATR3, NOP56, PPM1G, RPL12, RPL3, RPL6, SF3A1, SF3B3, SUPT16H |
| GO:BP macromolecule biosynthetic process | 0.00119 | DHX9, EPRS1, HNRNPR, IARS1, LMNB1, MACROH2A1, MARS1, MATR3, NOP56, PPM1G, RPL12, RPL3, RPL6, SF3A1, SF3B3, SUPT16H |
| GO:BP RNA metabolic process | 0.0111 | DHX9, EPRS1, HNRNPR, IARS1, MACROH2A1, MARS1, NOP56, PPM1G, RPL6, SF3A1, SF3B3, SUPT16H |
| GO:BP biosynthetic process | 0.0133 | DHX9, EPRS1, HNRNPR, IARS1, IMPDH2, LMNB1, MACROH2A1, MARS1, MATR3, NOP56, PPM1G, RPL12, RPL3, RPL6, SF3A1, SF3B3, SUPT16H |
| GO:CC cytosolic large ribosomal subunit | 0.0141 | RPL12, RPL3, RPL6 |
| GO:BP nucleic acid metabolic process | 0.0341 | DHX9, EPRS1, HNRNPR, IARS1, MACROH2A1, MARS1, NOP56, PPM1G, RPL6, SF3A1, SF3B3, SUPT16H |

### STRING and hu.MAP

STRING independently recapitulates the central biology through nucleic-acid binding (STRING Function Nucleic acid binding; within-query FDR = 7.48e-07), RNA binding (STRING Function RNA binding; within-query FDR = 1.58e-05), ribonucleoprotein complexes (STRING COMPARTMENTS Ribonucleoprotein complex; within-query FDR = 5.91e-05) and (STRING Component Ribonucleoprotein complex; within-query FDR = 0.00018), RNA metabolism (STRING RCTM Metabolism of RNA; within-query FDR = 0.00082), and gene expression (STRING Process Gene expression; within-query FDR = 0.0031). Several high-confidence pairwise relationships are already known: DHX9 connects with HNRNPR, MATR3, and RPL6; EPRS1 connects strongly with IARS1 and MARS1 and also with ribosomal proteins; RPL12, RPL3, and RPL6 form a strongly supported ribosomal cluster; and SF3A1 connects with SF3B3. hu.MAP provides complex-level support for an aminoacyl-tRNA-synthetase complex containing EPRS1, IARS1, and MARS1 (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1); chromatin-associated complexes containing PPM1G, MACROH2A1, and SUPT16H (hu.MAP huMAP3_10862.1) and (hu.MAP huMAP3_10592.1); heterogeneous nuclear ribonucleoprotein complexes containing HNRNPR and MATR3 (hu.MAP huMAP3_07581.1) and (hu.MAP huMAP3_10625.1); and spliceosomal complexes containing SF3A1 and SF3B3 (hu.MAP huMAP3_04549.1), (hu.MAP huMAP3_06511.1), and (hu.MAP huMAP3_08980.1). Thus, the module is not merely a collection of genes with correlated abundance: many of its edges and subgroups correspond to established molecular interactions or complexes. At the same time, STRING and hu.MAP do not explain every co-abundance edge, so the network may also reflect coordinated regulation across interacting nuclear and translational systems.

**STRING interactions (score >= 0.7)**: 16 of 136 gene pairs: DHX9–HNRNPR (0.909); DHX9–MATR3 (0.786); DHX9–RPL6 (0.958); DHX9–SF3B3 (0.73); EPRS1–IARS1 (0.999); EPRS1–MARS1 (0.999); EPRS1–NOP56 (0.739); EPRS1–RPL12 (0.732); EPRS1–RPL3 (0.855); EPRS1–RPL6 (0.711); HNRNPR–MATR3 (0.714); IARS1–MARS1 (0.999); RPL12–RPL3 (0.999); RPL12–RPL6 (0.999); RPL3–RPL6 (0.999); SF3A1–SF3B3 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Nucleic acid binding (FDR = 7.48e-07, 16 genes); Function RNA binding (FDR = 1.58e-05, 14 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 5.91e-05, 9 genes); Component Ribonucleoprotein complex (FDR = 0.00018, 9 genes); Keyword Isopeptide bond (FDR = 0.00027, 11 genes); TISSUES Lymphocyte (FDR = 0.00034, 10 genes); COMPARTMENTS Nuclear lumen (FDR = 0.00077, 10 genes); Keyword Ubl conjugation (FDR = 0.0008, 11 genes); RCTM Selenoamino acid metabolism (FDR = 0.00082, 6 genes); RCTM Metabolism of RNA (FDR = 0.00082, 9 genes); TISSUES Female reproductive gland (FDR = 0.0015, 14 genes); Component Nuclear lumen (FDR = 0.0019, 14 genes); Process Gene expression (FDR = 0.0031, 12 genes); TISSUES Brain (FDR = 0.0033, 17 genes); RCTM Major pathway of rRNA processing in the nucleolus and cytosol (FDR = 0.0057, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, IARS1, MARS1; 3/14); huMAP3_13688.1 (EPRS1, IARS1, MARS1; 3/14); huMAP3_10862.1 (PPM1G, MACROH2A1, SUPT16H; 3/33); huMAP3_10592.1 (PPM1G, MACROH2A1; 2/5); huMAP3_07581.1 (HNRNPR, MATR3; 2/21); huMAP3_04549.1 (SF3B3, SF3A1; 2/52); huMAP3_10625.1 (HNRNPR, MATR3; 2/57); huMAP3_06511.1 (SF3B3, SF3A1; 2/79); huMAP3_08980.1 (SF3B3, SF3A1; 2/97)

### Novelty

The module is unlikely to represent a wholly new molecular complex, because its main components belong to established ribosomal, spliceosomal, heterogeneous nuclear ribonucleoprotein, aminoacyl-tRNA-synthetase, chromatin, and RNA-helicase systems supported by STRING and hu.MAP. The conserved co-abundance relationship across liver and skin may nevertheless be a useful systems-level observation. Its potentially novel aspect is the tissue-pair-specific organization of these known components into one reproducible abundance module, especially the linkage between RNA helicase and RNA-binding proteins, spliceosomal factors, aminoacyl-tRNA synthetases, ribosomal proteins, and chromatin regulators. Absence of some genes from STRING or hu.MAP, such as DHX9 or LMNB1 in particular hu.MAP entries, should not be interpreted as evidence that their co-abundance relationship is novel. A claim of new biology would require independent replication, comparison with existing co-expression resources, and experimental testing of whether the cross-tissue association reflects regulation within the same cells rather than shared cellular composition.

**Hypothesis.** Hypothesis: liver and skin cells may coordinate a common nuclear-to-cytoplasmic gene-expression state in which chromatin accessibility and transcriptional elongation support RNA production, DHX9 and heterogeneous nuclear ribonucleoproteins support RNA remodeling and handling, SF3A1 and SF3B3 support spliceosome assembly, NOP56 supports nucleolar RNA and ribosome biogenesis, and EPRS1, IARS1, MARS1, together with ribosomal proteins, sustain accurate translation. PPM1G could help couple this state to phosphorylation-dependent regulation of splicing factors, while MACROH2A1 and LMNB1 could connect transcriptional output to chromatin and nuclear architecture. This is a mechanistic model rather than a demonstrated causal pathway. Testing it would require cell-resolved measurements, perturbation of hub genes, and assessment of transcription, splicing, ribosome production, and translation in relevant liver and skin cell populations.

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): LMNB1 (0.83), HNRNPR (0.83), IARS1 (0.83), MARS1 (0.83), MATR3 (0.82), RPL6 (0.81); STRING partners: HNRNPR (0.909), MATR3 (0.786), RPL6 (0.958), SF3B3 (0.73)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 has a central network position and connects to HNRNPR, MATR3, and RPL6. It is an RNA helicase that unwinds RNA and DNA-RNA complexes, localizes to the nucleus and cytoplasm, and is associated with transcriptional regulation and alternative splicing. It appears across nearly all primary enrichment categories (GO:MF nucleic acid binding; q_global = 4.48e-06), (GO:MF RNA binding; q_global = 0.000122), (GO:CC ribonucleoprotein complex; q_global = 0.000239), (GO:BP gene expression; q_global = 0.000529), (GO:BP macromolecule biosynthetic process; q_global = 0.00119), (GO:BP RNA metabolic process; q_global = 0.0111), (GO:BP biosynthetic process; q_global = 0.0133), and (GO:BP nucleic acid metabolic process; q_global = 0.0341), and its established STRING links reinforce the RNA-processing interpretation. Its disease associations include developmental, neurodegenerative, infectious, and lysosomal disorders, and it has substantial literature support.
- **Conclusion**: Established evidence supports DHX9 as a central RNA-remodeling and gene-expression component of the module. Its network position makes it a plausible integrator, but the co-abundance data do not establish that DHX9 causally controls the other module genes.

#### SF3A1

- **Related proteins** (co-abundance neighbors): RPL3 (0.83), MATR3 (0.82), PPM1G (0.81); STRING partners: SF3B3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in liver, skin
- **hu.MAP 3.0**: huMAP3_04549.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 is a component of the U2 snRNP and is directly involved in spliceosome assembly and splice-site recognition. It connects in the module to RPL3, MATR3, and PPM1G, and has a strong STRING relationship with SF3B3. It is represented across the primary RNA-binding, ribonucleoprotein, gene-expression, RNA-metabolism, and nucleic-acid-metabolism terms (GO:MF nucleic acid binding; q_global = 4.48e-06), (GO:MF RNA binding; q_global = 0.000122), (GO:CC ribonucleoprotein complex; q_global = 0.000239), (GO:BP gene expression; q_global = 0.000529), (GO:BP macromolecule biosynthetic process; q_global = 0.00119), (GO:BP RNA metabolic process; q_global = 0.0111), (GO:BP biosynthetic process; q_global = 0.0133), and (GO:BP nucleic acid metabolic process; q_global = 0.0341). hu.MAP places it with SF3B3 in several spliceosomal complexes (hu.MAP huMAP3_04549.1), (hu.MAP huMAP3_06511.1), and (hu.MAP huMAP3_08980.1). Its disease and literature records provide substantial external support for biological importance.
- **Conclusion**: Established evidence identifies SF3A1 as a spliceosomal anchor that explains an important part of the module. It is a strong candidate for maintaining coordinated RNA processing, although the cross-tissue co-abundance pattern alone does not demonstrate altered splicing.

#### EPRS1

- **Related proteins** (co-abundance neighbors): IARS1 (0.80); STRING partners: IARS1 (0.999), MARS1 (0.999), NOP56 (0.739), RPL12 (0.732), RPL3 (0.855), RPL6 (0.711)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is a multifunctional glutamyl-prolyl-tRNA synthetase and one of the most informative links between translation and the rest of the module. It is in the hu.MAP aminoacyl-tRNA-synthetase complexes with IARS1 and MARS1 (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), and STRING connects it to those enzymes, NOP56, and several ribosomal proteins. It appears in the primary nucleic-acid-binding, RNA-binding, ribonucleoprotein, gene-expression, biosynthetic, and RNA-metabolism terms (GO:MF nucleic acid binding; q_global = 4.48e-06), (GO:MF RNA binding; q_global = 0.000122), (GO:CC ribonucleoprotein complex; q_global = 0.000239), (GO:BP gene expression; q_global = 0.000529), (GO:BP macromolecule biosynthetic process; q_global = 0.00119), (GO:BP RNA metabolic process; q_global = 0.0111), (GO:BP biosynthetic process; q_global = 0.0133), and (GO:BP nucleic acid metabolic process; q_global = 0.0341). Its known functions include tRNA charging, translation, and a reported response to insulin.
- **Conclusion**: Established evidence supports EPRS1 as a translation-related bridge between the aminoacylation machinery and RNA or ribosome-associated components. Its role as a regulator of the entire shared module remains a hypothesis requiring perturbation evidence.

#### PPM1G

- **Related proteins** (co-abundance neighbors): RPL6 (0.84), SF3B3 (0.82), MACROH2A1 (0.82), LMNB1 (0.82), MATR3 (0.82), SF3A1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_10862.1, huMAP3_10592.1
- **Function (MyGene.info)**: protein phosphatase, Mg2+/Mn2+ dependent 1G. The protein encoded by this gene is a member of the PP2C family of Ser/Thr protein phosphatases. PP2C family members are known to be negative regulators of cell stress response pathways. This phosphatase is found to be responsible for the dephosphorylation of Pre-mRNA splicing factors, which is important for the formation of functional spliceosome. Studies of a similar gene in mice suggested a rol…
- **Diseases (Open Targets)**: neurodegenerative disease (0.264); hepatocellular carcinoma (0.110); Crohn disease (0.106); lung adenocarcinoma (0.096); gout (0.081)
- **Europe PMC papers**: 799
- **Why important**: PPM1G has a central network position and connects to RPL6, SF3B3, MACROH2A1, LMNB1, MATR3, and SF3A1. It is a PP2C-family serine/threonine phosphatase known to dephosphorylate pre-mRNA splicing factors and to participate in stress-response and cell-cycle regulation. It contributes to the primary gene-expression, macromolecule-biosynthesis, RNA-metabolism, biosynthetic, and nucleic-acid-metabolism terms (GO:BP gene expression; q_global = 0.000529), (GO:BP macromolecule biosynthetic process; q_global = 0.00119), (GO:BP RNA metabolic process; q_global = 0.0111), (GO:BP biosynthetic process; q_global = 0.0133), and (GO:BP nucleic acid metabolic process; q_global = 0.0341). hu.MAP links it with chromatin-associated partners (hu.MAP huMAP3_10862.1) and (hu.MAP huMAP3_10592.1). It has disease associations including neurodegenerative disease and several cancers, with a substantial literature base.
- **Conclusion**: Established evidence supports PPM1G as a plausible regulatory connector between splicing, chromatin-associated machinery, and the broader expression program. Its position suggests a possible control role, but the module does not prove that its phosphatase activity drives the shared abundance pattern.

#### LMNB1

- **Related proteins** (co-abundance neighbors): DHX9 (0.83), PPM1G (0.82), MACROH2A1 (0.81), HNRNPR (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in liver, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lamin B1. This gene encodes one of the two B-type lamin proteins and is a component of the nuclear lamina. A duplication of this gene is associated with autosomal dominant adult-onset leukodystrophy (ADLD). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: microcephaly 26, primary, autosomal dominant (0.723); autosomal dominant primary microcephaly (0.675); adult-onset autosomal dominant demyelinating leukodystrophy (0.670); hereditary disease (0.488); Syndrome with microcephaly as major feature (0.487)
- **Europe PMC papers**: 3851
- **Why important**: LMNB1 connects the module's RNA-associated core to nuclear architecture through DHX9, PPM1G, MACROH2A1, and HNRNPR. As a nuclear-lamina protein, it contributes to nuclear-envelope organization, heterochromatin formation, and nuclear positioning. It is included in the primary nucleic-acid-binding, gene-expression, macromolecule-biosynthesis, and biosynthetic terms (GO:MF nucleic acid binding; q_global = 4.48e-06), (GO:BP gene expression; q_global = 0.000529), (GO:BP macromolecule biosynthetic process; q_global = 0.00119), and (GO:BP biosynthetic process; q_global = 0.0133). HPA shows expression in both liver and skin and tissue enhancement in bone marrow and lymphoid tissue, while still reporting low immune-cell specificity. Its duplication is associated with adult-onset leukodystrophy, and it has extensive literature support.
- **Conclusion**: Established evidence supports LMNB1 as the nuclear-architecture component of the module. Its association suggests coordination between nuclear structure and gene expression, but whether nuclear-envelope organization explains the liver-skin conservation remains untested.

#### MATR3

- **Related proteins** (co-abundance neighbors): DHX9 (0.82), PPM1G (0.82), SF3A1 (0.82); STRING partners: DHX9 (0.786), HNRNPR (0.714)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver, skin
- **hu.MAP 3.0**: huMAP3_07581.1, huMAP3_10625.1
- **Function (MyGene.info)**: matrin 3. This gene encodes a nuclear matrix protein, which is proposed to stabilize certain messenger RNA species. Mutations of this gene are associated with distal myopathy 2, which often includes vocal cord and pharyngeal weakness. Alternatively spliced transcript variants, including read-through transcripts composed of the upstream small nucleolar RNA host gene 4 (non-protein coding) and matrin 3 gene s…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.735); distal myopathy with vocal cord weakness (0.569); neurodegenerative disease (0.529); distal myopathy (0.384); hereditary disease (0.193)
- **Europe PMC papers**: 1756
- **Why important**: MATR3 is a nuclear matrix protein proposed to stabilize selected messenger RNAs and is associated with post-transcriptional gene regulation. It connects to DHX9, PPM1G, and SF3A1, and STRING also links it to HNRNPR and DHX9. It contributes to the primary nucleic-acid-binding, RNA-binding, gene-expression, macromolecule-biosynthesis, and biosynthetic terms (GO:MF nucleic acid binding; q_global = 4.48e-06), (GO:MF RNA binding; q_global = 0.000122), (GO:BP gene expression; q_global = 0.000529), (GO:BP macromolecule biosynthetic process; q_global = 0.00119), and (GO:BP biosynthetic process; q_global = 0.0133). hu.MAP supports its association with heterogeneous nuclear ribonucleoprotein complexes (hu.MAP huMAP3_07581.1) and (hu.MAP huMAP3_10625.1). Its links to amyotrophic lateral sclerosis and distal myopathy, together with extensive literature, make it biologically important.
- **Conclusion**: Established evidence supports MATR3 as a post-transcriptional and nuclear-matrix component that may connect RNA handling with nuclear organization. Its role as a mediator of the conserved module is plausible but remains inferential.

## Module 5

**Tissue pair**: liver and skin  
**Genes (7)**: MYBBP1A, CAD, RSL1D1, AARS1, KARS1, LARS1, TXNDC5

### Function

The strongest functional interpretation is a broadly expressed core of protein-production and cellular biosynthetic machinery. The primary evidence is (GO:MF amino acid binding; q_global = 0.0388), in which AARS1, KARS1, and CAD share the globally significant molecular-function term amino acid binding. AARS1 and KARS1 are aminoacyl-tRNA synthetases that charge tRNAs, while CAD supplies de novo pyrimidine biosynthesis needed for nucleotide production and cell proliferation. The co-abundance structure connects the aminoacyl-tRNA-synthetase genes AARS1, KARS1, and LARS1, with RSL1D1, MYBBP1A, TXNDC5, and CAD forming connected peripheral relationships. RSL1D1 and MYBBP1A point toward nucleolar, ribosome-related, transcriptional, and stress-regulatory biology, whereas TXNDC5 points toward endoplasmic-reticulum protein folding. (STRING COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex; within-query FDR = 0.0297) supports an aminoacyl-tRNA synthetase multienzyme-complex interpretation, but it is supplementary rather than globally corrected primary evidence. Overall, the module is most consistent with coordinated translational capacity, nucleotide supply, nucleolar regulation, and protein-folding or proteostasis activity rather than a narrowly tissue-specific pathway.

**Cell composition.** This does not look like a module dominated by plasma or classically secreted proteins. The HPA summary reports low tissue specificity for every member, and no tissue was repeatedly enriched. Most genes also have low cell-type specificity and low immune-cell specificity, arguing against a module primarily driven by a particular blood-cell population. The HPA data do identify TXNDC5 as group-enriched in choroid plexus epithelial cells and plasma cells and in selected B-cell and plasmacytoid dendritic-cell groups, while KARS1 is cell-type enhanced in selected nonhepatic cell types; these are individual signals rather than a coherent blood signature. Two genes are classified in the HPA summary as secreted genes, but the individual localization evidence emphasizes intracellular, membrane-associated, cytosolic, or endoplasmic-reticulum compartments rather than a dominant circulating-protein program. Protein detection is widespread in skin and present for most members in liver. The shared liver-skin signal therefore more plausibly reflects broadly expressed housekeeping or biosynthetic activity, shared cellular physiology, or sample-composition effects than a specialized liver-skin secretory program.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF amino acid binding | 0.0388 | AARS1, CAD, KARS1 |

### STRING and hu.MAP

STRING provides strong support for a known aminoacyl-tRNA-synthetase core: AARS1 is connected to KARS1 and LARS1, and KARS1 is connected to LARS1. The STRING evidence is concordant with (STRING COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex; within-query FDR = 0.0297), which places AARS1, KARS1, and LARS1 in an aminoacyl-tRNA synthetase multienzyme-complex context. STRING also links MYBBP1A and RSL1D1, supporting a known relationship between two nucleolar regulatory proteins. The hu.MAP evidence independently places KARS1 and LARS1 together in (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), with each complex containing many additional aminoacyl-tRNA synthetases and associated factors. Thus, the module contains a recognizable known synthetase-complex component and a separate known MYBBP1A-RSL1D1 relationship, while the remaining cross-links and the complete co-abundance arrangement are not fully explained by the listed curated interactions. This supports biological coherence but also indicates that the module is not equivalent to a single experimentally defined complex.

**STRING interactions (score >= 0.7)**: 4 of 21 gene pairs: AARS1–KARS1 (0.992); AARS1–LARS1 (0.968); KARS1–LARS1 (0.999); MYBBP1A–RSL1D1 (0.831)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex (FDR = 0.0297, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (KARS1, LARS1; 2/14); huMAP3_13688.1 (KARS1, LARS1; 2/14)

### Novelty

The module should not be described as a wholly new molecular complex or as a newly discovered function. The AARS1-KARS1-LARS1 relationships, the MYBBP1A-RSL1D1 relationship, and the KARS1-LARS1 hu.MAP associations are already supported by independent interaction and complex resources. The potentially novel aspect is the conserved co-abundance pattern across liver and skin and the way translational, nucleolar, nucleotide-biosynthetic, and endoplasmic-reticulum genes are combined in one tissue-pair module. However, the supplied evidence does not establish that this cross-tissue co-abundance organization is new, and absence of a complete matching entry in STRING or hu.MAP would not prove novelty. The appropriate conclusion is that the module is a potentially interesting tissue-pair co-abundance observation built partly from established biology, requiring comparison with published co-expression modules, replication cohorts, and independent perturbation or interaction data before a novelty claim.

**Hypothesis.** Hypothesis: the liver-skin module reflects a shared demand for biosynthetic and proteostatic capacity in broadly expressed cells. AARS1, KARS1, and LARS1 may coordinate aminoacyl-tRNA charging, CAD may support nucleotide production for RNA and DNA synthesis, and RSL1D1 together with MYBBP1A may connect this demand to nucleolar and translational regulation. TXNDC5 may represent an endoplasmic-reticulum folding response coupled to increased protein-production load. A plausible model is that cellular growth, renewal, stress, or protein-synthesis demand produces the observed coordinated abundance pattern in both tissues. This is a mechanistic hypothesis rather than a demonstrated causal pathway; the available evidence does not show that any one member drives the co-abundance relationship or that the module is specific to liver-skin biology.

### Important genes

#### AARS1

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.83); STRING partners: KARS1 (0.992), LARS1 (0.968)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alanyl-tRNA synthetase 1. The human alanyl-tRNA synthetase (AARS) belongs to a family of tRNA synthases, of the class II enzymes.  Class II tRNA synthases evolved early in evolution and are highly conserved. This is reflected by the fact that 498 of the 968-residue polypeptide human AARS shares 41% identity witht the E.coli protein.  tRNA synthases are the enzymes that interpret the RNA code and attach specific aminoacids …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2N (0.762); developmental and epileptic encephalopathy, 29 (0.747); undetermined early-onset epileptic encephalopathy (0.678); trichothiodystrophy 8, nonphotosensitive (0.568); Charcot-Marie-Tooth disease type 2 (0.566)
- **Europe PMC papers**: 672
- **Why important**: AARS1 is a direct member of the globally significant (GO:MF amino acid binding; q_global = 0.0388) amino acid-binding overlap and belongs to the synthetase-centered part of the module. Its STRING links to KARS1 and LARS1 are strong and biologically concordant with aminoacyl-tRNA charging. It has broad liver and skin protein detection, disease associations involving axonal Charcot-Marie-Tooth disease and developmental epileptic encephalopathy, and a substantial literature base.
- **Conclusion**: Established evidence supports AARS1 as a central functional marker of the module's translational machinery. Its role as a driver of the liver-skin co-abundance pattern remains a hypothesis and is not established by the supplied data.

#### KARS1

- **Related proteins** (co-abundance neighbors): MYBBP1A (0.82); STRING partners: AARS1 (0.992), LARS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver, skin
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: lysyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. Lysyl-tRNA synthetase is a homodimer localized to the cytoplasm which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Alternatively spliced transcript variants encoding different…
- **Diseases (Open Targets)**: leukoencephalopathy, progressive, infantile-onset, with or without deafness (0.753); deafness, congenital, and adult-onset progressive leukoencephalopathy (0.714); autosomal recessive nonsyndromic hearing loss 89 (0.685); Charcot-Marie-Tooth disease recessive intermediate B (0.670); deafness (0.534)
- **Europe PMC papers**: 232
- **Why important**: KARS1 is part of (GO:MF amino acid binding; q_global = 0.0388), has strong STRING links to AARS1 and LARS1, and is present in both hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Its established function in lysyl-tRNA aminoacylation directly supports the module's protein-production interpretation. It is detected in liver and skin and has disease associations involving progressive leukoencephalopathy and hearing-loss phenotypes, as well as an autoimmune connection through polymyositis and dermatomyositis autoantibodies.
- **Conclusion**: Established evidence makes KARS1 one of the best-supported functional anchors of the module. Its cell-type-enhanced HPA pattern may influence abundance in some contexts, but a specific contribution to the shared liver-skin signal is not demonstrated.

#### LARS1

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.85), MYBBP1A (0.81); STRING partners: AARS1 (0.968), KARS1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in liver, skin
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: leucyl-tRNA synthetase 1. This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals w…
- **Diseases (Open Targets)**: infantile liver failure syndrome 1 (0.670); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.510); Global developmental delay (0.119); sensorineural hearing loss disorder (0.119); Generalized-onset seizure (0.118)
- **Europe PMC papers**: 267
- **Why important**: LARS1 is the leucine-tRNA synthetase member of the synthetase-centered network, with strong STRING links to AARS1 and KARS1 and membership in both hu.MAP complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Its known functions include leucyl-tRNA aminoacylation and cellular responses to amino-acid availability, making it a mechanistic bridge between translation and nutrient sensing. It is detected in both tissues and is associated with infantile liver failure syndrome and other developmental or sensory disorders.
- **Conclusion**: Established evidence supports LARS1 as a core translational and amino-acid-response component. The possibility that leucine-responsive signaling helps coordinate the module is plausible, but it remains a hypothesis because the co-abundance data do not establish signaling direction.

#### RSL1D1

- **Related proteins** (co-abundance neighbors): LARS1 (0.85), AARS1 (0.83), TXNDC5 (0.81), CAD (0.81); STRING partners: MYBBP1A (0.831)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in liver, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal L1 domain containing 1. Enables mRNA 3'-UTR binding activity and mRNA 5'-UTR binding activity. Involved in regulation of apoptotic process and regulation of cellular senescence. Acts upstream of or within regulation of protein localization. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: adolescent idiopathic scoliosis (0.219); hepatocellular carcinoma (0.099); neoplasm (0.099); colorectal carcinoma (0.096); insomnia (0.078)
- **Europe PMC papers**: 381
- **Why important**: RSL1D1 has the highest network connectivity in the supplied module and links the synthetase-associated portion to TXNDC5 and CAD. It is localized to the nucleoli and mitotic chromosomes and has annotations involving mRNA binding, apoptosis, cellular senescence, and protein localization. Its STRING relationship with MYBBP1A provides an independently supported nucleolar connection. It is detected in liver and skin and has disease associations including hepatocellular carcinoma and other neoplastic or developmental conditions.
- **Conclusion**: Established evidence supports RSL1D1 as an important network integrator connecting translation-related and stress or growth-related biology. Its position suggests a coordinating role, but causality and any specific role in liver-skin conservation remain unproven.

#### TXNDC5

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Endoplasmic reticulum; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin domain containing 5. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal endoplasmic reticulum (ER)-signal sequence, three catalytically active thioredoxin domains and a C-terminal ER-retention sequence. Its expression is induced by hypoxia and its role ma…
- **Diseases (Open Targets)**: colorectal carcinoma (0.321); spinal stenosis (0.203); neoplasm (0.096); central nervous system cancer (0.092); glioma (0.091)
- **Europe PMC papers**: 1026
- **Why important**: TXNDC5 connects to RSL1D1 in the co-abundance network and represents a distinct endoplasmic-reticulum protein-folding component. Its thioredoxin and protein-disulfide-isomerase functions support proteostasis and its documented induction by hypoxia links it to cellular stress. HPA data show group enrichment in choroid plexus epithelial cells and plasma cells and in selected immune-cell groups, while protein detection is reported in skin but not liver. It has a large literature base and disease associations including colorectal carcinoma and glioma.
- **Conclusion**: Established evidence supports TXNDC5 as a proteostasis and stress-related component that may broaden the module beyond translation. Its inclusion could reflect cell composition or stress-state variation rather than a direct mechanistic partnership with the synthetases; this distinction requires validation.

#### CAD

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carbamoyl-phosphate synthetase 2, aspartate transcarbamylase, and dihydroorotase. The de novo synthesis of pyrimidine nucleotides is required for mammalian cells to proliferate. This gene encodes a trifunctional protein which is associated with the enzymatic activities of the first 3 enzymes in the 6-step pathway of pyrimidine biosynthesis: carbamoylphosphate synthetase (CPS II), aspartate transcarbamoylase, and dihydroorotase. This protein is regulated by the mitogen-activated…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 50 (0.660); congenital disorder of glycosylation type I (0.595); infantile epileptic-dyskinetic encephalopathy (0.499); type 2 diabetes mellitus (0.286); urolithiasis (0.283)
- **Europe PMC papers**: 60667
- **Why important**: CAD is part of the globally significant (GO:MF amino acid binding; q_global = 0.0388) amino acid-binding overlap and connects to RSL1D1 in the module. Its trifunctional enzyme supplies the early steps of de novo pyrimidine biosynthesis, linking nucleotide availability to proliferation and RNA production. It has liver-development and nucleotide-biosynthesis annotations, disease associations spanning neurodevelopmental disorders and metabolic disease, and by far the largest literature base among the module members.
- **Conclusion**: Established evidence supports CAD as the module's nucleotide-biosynthetic anchor and a plausible complement to its translation-related genes. The proposed coupling between CAD activity and the other module members is mechanistically reasonable but not directly demonstrated by the supplied network.
