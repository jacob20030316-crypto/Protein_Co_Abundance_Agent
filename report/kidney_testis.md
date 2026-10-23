# Conserved co-abundance modules: kidney and testis

## Module 0

**Tissue pair**: kidney and testis  
**Genes (12)**: SLC3A2, ATP13A1, ATL3, CANX, CKAP4, GFM1, PTGFRN, GPD2, ITGB1, OPA1, SCARB2, TRAP1

### Function

The module is best interpreted as a conserved organelle-membrane and membrane-protein homeostasis program. The primary evidence is (GO:CC organelle membrane; q_global = 0.0326), in which nearly the entire module overlaps the GO cellular-component term organelle membrane. This interpretation is reinforced by the supplementary STRING terms for transmembrane helices and integral membrane components (STRING Keyword Transmembrane helix; within-query FDR = 0.001) (STRING Component Organelle membrane; within-query FDR = 0.0144) (STRING Component Integral component of membrane; within-query FDR = 0.0153). The genes span several connected cellular systems: endoplasmic-reticulum organization and protein folding through ATL3, CANX and CKAP4; endosomal and lysosomal membrane trafficking through SCARB2 and ATP13A1; cell-surface adhesion and transport through ITGB1, PTGFRN and SLC3A2; and mitochondrial organization, translation and energy handling through OPA1, TRAP1, GFM1 and GPD2. Thus, the most defensible function is coordinated maintenance, trafficking and quality control of intracellular and plasma-membrane systems, rather than a narrowly defined pathway. No GO or KEGG biological-process term passed global correction; (GO:CC organelle membrane; q_global = 0.0326) is a cellular-component result and should not be overinterpreted as proof of one specific biochemical process.

**Cell composition.** The module is not composed of secreted proteins, so a plasma-protein explanation is not supported by the HPA summary. All members have low tissue specificity, and protein detection is broadly concordant in kidney and testis for most genes, which supports a shared cellular program rather than a kidney-only or testis-only tissue marker. The module is also not uniformly blood-cell specific: most genes have low immune-cell specificity, although SCARB2 and GPD2 show notable myeloid or blood-cell enrichment and CKAP4 has immune-cell enhancement. Several genes have cell-type-enhanced or cell-type-enriched patterns in specialized cells, including spermatids, oocytes, epithelial cells and neutrophil-related populations. Therefore, variation in shared cell types or sample composition could contribute to the co-abundance signal, especially in testis or in samples containing myeloid cells, but the membrane and organelle interpretation is not reducible to blood contamination. The module also contains broadly used housekeeping-like machinery, including mitochondrial translation, mitochondrial dynamics, protein folding and membrane quality-control components.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC organelle membrane | 0.0326 | ATL3, ATP13A1, CANX, CKAP4, GPD2, ITGB1, OPA1, PTGFRN, SCARB2, SLC3A2, TRAP1 |

### STRING and hu.MAP

The direct STRING network support is limited: the only high-confidence STRING pair is ITGB1–SCARB2. Nevertheless, STRING functional enrichment independently supports membrane localization through (STRING Keyword Transmembrane helix; within-query FDR = 0.001) (STRING Component Organelle membrane; within-query FDR = 0.0144) (STRING Component Integral component of membrane; within-query FDR = 0.0153), although these are supplementary within-query results and not global enrichment evidence. hu.MAP provides two kinds of prior support. ITGB1 and PTGFRN co-occur in the adhesion and cell-surface-associated complexes (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1), while TRAP1 and GFM1 co-occur in the mitochondrial protein-maintenance complex (hu.MAP huMAP3_13468.1). These complexes contain many additional proteins that are not in the module, so they support membership in known cellular neighborhoods rather than a complete module-specific complex. The combination of one STRING pair, the ITGB1–PTGFRN hu.MAP relationships, and the TRAP1–GFM1 hu.MAP relationship suggests that parts of the module recapitulate established membrane-adhesion and mitochondrial machinery. The remaining cross-compartment links are not directly established by these databases and may reflect co-abundance, shared regulation, indirect functional coupling or sample-composition effects.

**STRING interactions (score >= 0.7)**: 1 of 66 gene pairs: ITGB1–SCARB2 (0.719)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transmembrane helix (FDR = 0.001, 9 genes); Component Organelle membrane (FDR = 0.0144, 11 genes); Component Integral component of membrane (FDR = 0.0153, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10503.1 (ITGB1, PTGFRN; 2/27); huMAP3_10980.1 (ITGB1, PTGFRN; 2/44); huMAP3_09336.1 (ITGB1, PTGFRN; 2/50); huMAP3_13468.1 (TRAP1, GFM1; 2/99)

### Novelty

This module should not be claimed as a newly discovered physical complex or as a wholly novel pathway. Several members have well-established functions, and subsets are represented in known STRING or hu.MAP relationships, particularly ITGB1 with SCARB2, ITGB1 with PTGFRN, and TRAP1 with GFM1. At the same time, the specific conserved kidney–testis co-abundance grouping is not directly established by the reported STRING and hu.MAP evidence: most module pairs lack a high-confidence STRING interaction, and the hu.MAP complexes contain only subsets of the module. Accordingly, the potentially novel aspect is the cross-tissue co-abundance organization of these membrane, endoplasmic-reticulum, lysosomal and mitochondrial genes, not the individual gene functions or the existence of the component complexes. Because database absence does not prove biological novelty, this should be described as a candidate conserved co-abundance signature requiring validation in independent cohorts, cell-type-aware analyses and perturbation experiments.

**Hypothesis.** Hypothesis: in kidney and testis, a shared population of metabolically active or differentiating cells coordinates organelle-membrane remodeling with membrane-protein quality control. ATL3 and CANX could support endoplasmic-reticulum architecture and folding, ATP13A1 and SCARB2 could support removal or trafficking of damaged and endolysosomal membrane proteins, and ITGB1, PTGFRN and SLC3A2 could couple the membrane system to adhesion, extracellular interactions and nutrient or amino-acid transport. OPA1, TRAP1, GFM1 and GPD2 could provide mitochondrial structural, translational and metabolic support for this high membrane-maintenance demand. The hypothesis predicts that the co-abundance signal will be strongest in the relevant shared cell populations and will track coordinated changes in organelle stress, membrane trafficking and cellular differentiation. This is a mechanistic hypothesis, not an established interaction map; the available evidence directly establishes localization and selected database relationships, but not causal coupling among all module members.

### Important genes

#### ITGB1

- **Related proteins** (co-abundance neighbors): ATL3 (0.89), PTGFRN (0.89), SLC3A2 (0.87), GFM1 (0.86), CANX (0.82), CKAP4 (0.81); STRING partners: SCARB2 (0.719)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in kidney
- **hu.MAP 3.0**: huMAP3_10503.1, huMAP3_10980.1, huMAP3_09336.1
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 has the strongest network position in the module, with connections to ATL3, PTGFRN, SLC3A2, GFM1, CANX and CKAP4. It is the sole module member with a reported high-confidence STRING interaction, with SCARB2, and it occurs with PTGFRN in the hu.MAP complexes (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1). Its established role is as an integrin beta subunit involved in cell adhesion, recognition, angiogenesis, phagocytosis and tissue repair. Its plasma-membrane and focal-adhesion localization connects the organelle-membrane signal to cell-surface organization. It also has extensive literature and disease associations including inflammatory, infectious and autoimmune disease contexts.
- **Conclusion**: Established evidence supports ITGB1 as the principal membrane-adhesion anchor of the module and as an important network hub. It is plausible, but not proven, that ITGB1 links the shared organelle-maintenance program to cell adhesion or cell-state composition in kidney and testis.

#### GFM1

- **Related proteins** (co-abundance neighbors): ITGB1 (0.86), TRAP1 (0.84), GPD2 (0.82), SLC3A2 (0.82), OPA1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: G elongation factor mitochondrial 1. Eukaryotes contain two protein translational systems, one in the cytoplasm and one in the mitochondria. Mitochondrial translation is crucial for maintaining mitochondrial function and mutations in this system lead to a breakdown in the respiratory chain-oxidative phosphorylation system and to impaired maintenance of mitochondrial DNA. This gene encodes one of the mitochondrial translation elongati…
- **Diseases (Open Targets)**: hepatoencephalopathy due to combined oxidative phosphorylation defect type 1 (0.822); neurodegenerative disease (0.463); combined oxidative phosphorylation deficiency (0.451); hereditary disease (0.341); Leigh syndrome (0.313)
- **Europe PMC papers**: 1380
- **Why important**: GFM1 has a high network position and links ITGB1, TRAP1, GPD2, SLC3A2 and OPA1, thereby connecting the membrane-associated portion of the module to mitochondrial genes. It is a member of the mitochondrial translation machinery, and its hu.MAP association with TRAP1 in (hu.MAP huMAP3_13468.1) provides prior complex-level support. Its established function is mitochondrial translation elongation, a process required for respiratory-chain and oxidative-phosphorylation maintenance. GFM1 has recognized disease associations involving combined oxidative-phosphorylation defects and hepatoencephalopathy, with substantial literature support.
- **Conclusion**: Established evidence supports GFM1 as the mitochondrial translation component and a bridge between the mitochondrial and membrane-related portions of the module. A coordinated mitochondrial response may help explain the co-abundance pattern, but the data do not establish that GFM1 mechanistically regulates the membrane genes.

#### CANX

- **Related proteins** (co-abundance neighbors): SCARB2 (0.83), ITGB1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is connected to SCARB2 and ITGB1 and is part of the globally significant organelle-membrane term (GO:CC organelle membrane; q_global = 0.0326) and all supplementary STRING membrane terms (STRING Keyword Transmembrane helix; within-query FDR = 0.001) (STRING Component Organelle membrane; within-query FDR = 0.0144) (STRING Component Integral component of membrane; within-query FDR = 0.0153). It is an endoplasmic-reticulum calcium-binding chaperone that assists folding and assembly of newly synthesized glycoproteins and participates in retention and degradation of incorrectly folded proteins. Its detection in kidney and testis and enrichment in late spermatids make it especially relevant to the shared tissue context. Its substantial literature and disease-related associations also provide strong prior biological support.
- **Conclusion**: Established evidence supports CANX as an endoplasmic-reticulum protein-folding and quality-control component of the module. It is a strong candidate for coordinating membrane-protein maturation with the broader organelle-maintenance program, although that coordination remains a hypothesis.

#### OPA1

- **Related proteins** (co-abundance neighbors): ATP13A1 (0.84), GFM1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OPA1 mitochondrial dynamin like GTPase. The protein encoded by this gene is a nuclear-encoded mitochondrial protein with similarity to dynamin-related GTPases. The encoded protein localizes to the inner mitochondrial membrane and helps regulate mitochondrial stability and energy output. This protein also sequesters cytochrome c. Mutations in this gene have been associated with optic atrophy type 1, which is a dominantly inherited optic …
- **Diseases (Open Targets)**: autosomal dominant optic atrophy, classic form (0.846); Behr syndrome (0.812); optic atrophy with or without deafness, ophthalmoplegia, myopathy, ataxia, and neuropathy (0.766); mitochondrial DNA depletion syndrome 14B (cardioencephalomyopathic type) (0.745); optic atrophy (0.653)
- **Europe PMC papers**: 12169
- **Why important**: OPA1 connects the mitochondrial branch of the module to ATP13A1 and GFM1 and is included in (GO:CC organelle membrane; q_global = 0.0326) and (STRING Keyword Transmembrane helix; within-query FDR = 0.001) (STRING Component Organelle membrane; within-query FDR = 0.0144) (STRING Component Integral component of membrane; within-query FDR = 0.0153). It is an inner-mitochondrial-membrane dynamin-like GTPase involved in mitochondrial fusion, inner-membrane organization, mitochondrial stability and energy output. Its disease associations include dominant optic atrophy and related mitochondrial syndromes, and it has extensive literature support. Its presence alongside GFM1, TRAP1 and GPD2 gives the module a coherent mitochondrial-maintenance component rather than a purely generic membrane signature.
- **Conclusion**: Established evidence supports OPA1 as the mitochondrial architecture component of the module. It may indicate that mitochondrial structural integrity is coupled to membrane and protein-quality demands in the shared cell population, but the co-abundance data alone cannot establish directionality or causation.

#### SLC3A2

- **Related proteins** (co-abundance neighbors): ITGB1 (0.87), GFM1 (0.82), PTGFRN (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 3 member 2. This gene is a member of the solute carrier family and encodes a cell surface, transmembrane protein. The protein exists as the heavy chain of a heterodimer, covalently bound through di-sulfide bonds to one of several possible light chains. The encoded transporter plays a role in regulation of intracellular calcium levels and transports L-type amino acids. Alternatively spliced transcript variants…
- **Diseases (Open Targets)**: sensorineural hearing loss disorder (0.370); neurodegenerative disease (0.324); neoplasm (0.117); breast cancer (0.113); breast carcinoma (0.110)
- **Europe PMC papers**: 6815
- **Why important**: SLC3A2 is connected to ITGB1, GFM1 and PTGFRN and is included in (GO:CC organelle membrane; q_global = 0.0326) and (STRING Keyword Transmembrane helix; within-query FDR = 0.001) (STRING Component Organelle membrane; within-query FDR = 0.0144) (STRING Component Integral component of membrane; within-query FDR = 0.0153). It is a plasma-membrane heavy chain of amino-acid transporter heterodimers and contributes to amino-acid transport and regulation of intracellular calcium. Its detection in both kidney and testis and its cell-type-enhanced patterns in epithelial and specialized cells fit a context in which nutrient transport supports membrane and mitochondrial activity. It has substantial literature and disease associations including hearing, neurodegenerative and cancer-related conditions.
- **Conclusion**: Established evidence supports SLC3A2 as a membrane transport component that could connect extracellular nutrient availability with intracellular organelle maintenance. Its proposed role as a metabolic link within this module is plausible, but direct coupling to the other module members remains untested.

## Module 1

**Tissue pair**: kidney and testis  
**Genes (18)**: A2M, ALDH7A1, SERPINC1, ATP1B1, CAT, C3, GALM, DGLUCY, ALDH6A1, PCCA, PCCB, PEPD, PRXL2A, PC, SELENBP1, TAGLN, ACAA1, TMT1A

### Function

The strongest interpretation is a mitochondrial and peroxisomal metabolic module centered on branched-chain amino-acid and propionyl-CoA handling. The globally corrected evidence is the carbon-carbon bond ligase activity term (GO:MF ligase activity, forming carbon-carbon bonds; q_global = 0.0208), represented by PC, PCCA and PCCB, and the valine, leucine and isoleucine degradation pathway (KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 0.0361), represented by ACAA1, ALDH6A1, ALDH7A1, PCCA and PCCB. These findings are biologically coherent with the annotated roles of PCCA and PCCB in propionyl-CoA carboxylation, ALDH6A1 in valine and related catabolism, ALDH7A1 in lysine and aldehyde metabolism, ACAA1 in peroxisomal beta-oxidation, and PC in mitochondrial anaplerosis. The module is not exclusively metabolic: C3, A2M and SERPINC1 form a separate complement, protease-inhibitor and coagulation-associated component, while CAT, PRXL2A and DGLUCY provide possible oxidative or detoxification context. Thus, the most defensible functional summary is coordinated intermediary metabolism with a linked extracellular protease, complement and coagulation signal.

**Cell composition.** The module is not predominantly a plasma or secreted-protein module, because only C3, A2M, SERPINC1 and PRXL2A are annotated as secreted or secreted in other tissues, whereas most members are intracellular metabolic or structural proteins. It is also not a simple broadly expressed housekeeping module: the HPA summary shows strong tissue and cell-type specificity across the module, with liver and hepatocyte enrichment especially prominent, alongside kidney and proximal-tubule signals and selected spermatid, epididymal and other tissue-specific signals. The presence of C3, A2M and SERPINC1, together with immune-cell enrichment for several genes, means that blood exposure, vascular content, immune cells or shared stromal and epithelial cell types could contribute to the kidney-testis co-abundance pattern. This possibility is particularly important because SERPINC1 is secreted to blood and is not detected by IHC in either listed tissue, while C3 and A2M are secreted to blood and detected in both tissues. At the same time, most module proteins are detected in kidney and testis, and several metabolic genes have kidney, liver, proximal-tubule or spermatid associations, so the module cannot be reduced to contamination without additional sample-level and cell-composition analysis.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF ligase activity, forming carbon-carbon bonds | 0.0208 | PC, PCCA, PCCB |
| KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human) | 0.0361 | ACAA1, ALDH6A1, ALDH7A1, PCCA, PCCB |

### STRING and hu.MAP

STRING supports a coherent metabolic core: PCCA and PCCB have an especially strong relationship, PC connects to both PCC subunits, and ACAA1, ALDH6A1 and ALDH7A1 connect within the valine and related catabolic network. STRING also identifies the A2M-SERPINC1 relationship and the C3-A2M-SERPINC1 complement and coagulation grouping through supplementary enrichment (STRING KEGG Complement and coagulation cascades; within-query FDR = 0.0274). These relationships are established database-supported associations rather than proof that every co-abundance edge is a direct physical interaction. hu.MAP independently supports the PCCA-PCCB complex, with ALDH7A1 present in related complexes (hu.MAP huMAP3_07028.1) (hu.MAP huMAP3_02917.1), and places PCCA and PCCB in broader mitochondrial metabolic assemblies (hu.MAP huMAP3_10458.1) (hu.MAP huMAP3_13468.1). hu.MAP also repeatedly groups A2M and C3, with SERPINC1 included in a related extracellular complex (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1). The agreement between the co-abundance structure, STRING and hu.MAP therefore strengthens the interpretation of a real metabolic core plus an extracellular complement and protease-regulation component. Conversely, several module edges and genes lack STRING or hu.MAP support, so the network should not be interpreted as a single experimentally established complex.

**STRING interactions (score >= 0.7)**: 12 of 153 gene pairs: A2M–SERPINC1 (0.927); ACAA1–ALDH6A1 (0.952); ACAA1–PCCA (0.948); ACAA1–PCCB (0.955); ALDH6A1–ALDH7A1 (0.934); ALDH6A1–PCCA (0.96); ALDH6A1–PCCB (0.967); ALDH7A1–PCCA (0.852); ALDH7A1–PCCB (0.859); PC–PCCA (0.922); PC–PCCB (0.989); PCCA–PCCB (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Valine, leucine and isoleucine degradation (FDR = 0.0071, 5 genes); DISEASES Disease of metabolism (FDR = 0.0087, 11 genes); DISEASES Inherited metabolic disorder (FDR = 0.0229, 10 genes); KEGG Carbon metabolism (FDR = 0.0274, 5 genes); KEGG Complement and coagulation cascades (FDR = 0.0274, 3 genes); WikiPathways Biotin metabolism, including IMDs (FDR = 0.0366, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07028.1 (PCCA, PCCB, ALDH7A1; 3/4); huMAP3_15040.1 (SERPINC1, A2M, C3; 3/64); huMAP3_02917.1 (PCCB, ALDH7A1; 2/3); huMAP3_10458.1 (PCCA, PCCB; 2/16); huMAP3_08395.1 (A2M, C3; 2/43); huMAP3_09531.1 (A2M, C3; 2/47); huMAP3_10101.1 (A2M, C3; 2/49); huMAP3_10678.1 (A2M, C3; 2/71); huMAP3_13468.1 (PCCA, PCCB; 2/99)

### Novelty

This module should not be called a wholly new biological pathway. Its central metabolic relationships are already represented in STRING and hu.MAP, and the PCCA-PCCB, PC-PCCA/PCCB, aldehyde-dehydrogenase and complement or coagulation associations have established biological context. The potentially novel finding is the tissue-pair-specific co-abundance organization: a kidney-testis module that combines a branched-chain and propionyl-CoA metabolic core with extracellular complement and coagulation proteins and selected cell-type markers. That integrated arrangement may be new in this dataset, but the fact sheet does not provide a comparison against prior kidney-testis modules, independent cohorts, or published co-abundance networks. Therefore novelty is plausible at the module-configuration and cross-tissue level, not established at the level of individual genes, pathways or protein complexes. Absence of support for some genes in STRING or hu.MAP is evidence of incomplete prior annotation, not proof that those relationships are novel.

**Hypothesis.** Hypothesis: the conserved kidney-testis module reflects a shared metabolic state of specialized epithelial or germ-cell-associated compartments that require mitochondrial propionyl-CoA disposal, branched-chain amino-acid catabolism, aldehyde detoxification and anaplerotic support. In kidney, proximal-tubule and related epithelial metabolism could generate the signal; in testis, spermatid, epididymal or other supporting-cell metabolism could produce a partially analogous signal. The complement, antithrombin and alpha-two-macroglobulin component may reflect local vascular or extracellular inflammatory regulation, shared tissue fluid exposure, or variable blood and immune-cell content rather than a direct part of the mitochondrial pathway. A testable prediction is that the metabolic genes should co-vary within purified kidney epithelial and testis cellular populations, whereas the C3-A2M-SERPINC1 signal should track extracellular fluid, vascular or immune-cell abundance more strongly.

### Important genes

#### PCCA

- **Related proteins** (co-abundance neighbors): PCCB (0.93), GALM (0.91), ATP1B1 (0.85), ALDH7A1 (0.85), CAT (0.81), PEPD (0.80); STRING partners: ACAA1 (0.948), ALDH6A1 (0.96), ALDH7A1 (0.852), PC (0.922), PCCB (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_07028.1, huMAP3_10458.1, huMAP3_13468.1
- **Function (MyGene.info)**: propionyl-CoA carboxylase subunit alpha. The protein encoded by this gene is the alpha subunit of the heterodimeric mitochondrial enzyme Propionyl-CoA carboxylase. PCCA encodes the biotin-binding region of this enzyme. Mutations in either PCCA or PCCB (encoding the beta subunit) lead to an enzyme deficiency resulting in propionic acidemia. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by…
- **Diseases (Open Targets)**: propionic acidemia (0.853); hereditary disease (0.487); dilated cardiomyopathy (0.370); neurodegenerative disease (0.357); pontocerebellar hypoplasia type 2D (0.340)
- **Europe PMC papers**: 2633
- **Why important**: PCCA is the highest-connectivity member of the module and links the metabolic core to PCCB, PC, ALDH7A1, CAT, GALM and PEPD. It is present in both globally corrected terms (GO:MF ligase activity, forming carbon-carbon bonds; q_global = 0.0208) (KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 0.0361), has strong STRING support with the core metabolic genes, and occurs in multiple hu.MAP complexes (hu.MAP huMAP3_07028.1) (hu.MAP huMAP3_10458.1) (hu.MAP huMAP3_13468.1). Its annotated role as the biotin-binding alpha subunit of propionyl-CoA carboxylase directly connects the network to propionyl-CoA disposal and branched-chain amino-acid metabolism. Propionic acidemia is an established disease association, and the substantial literature volume indicates that this is a well-characterized anchor rather than a speculative marker.
- **Conclusion**: Established evidence supports PCCA as a central biochemical and network component of the module. It is a strong candidate for the conserved metabolic driver, although the co-abundance data alone do not prove that PCCA activity causes the tissue-pair association.

#### PCCB

- **Related proteins** (co-abundance neighbors): PCCA (0.93), SELENBP1 (0.88), GALM (0.87), ALDH6A1 (0.83), DGLUCY (0.81); STRING partners: ACAA1 (0.955), ALDH6A1 (0.967), ALDH7A1 (0.859), PC (0.989), PCCA (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_07028.1, huMAP3_02917.1, huMAP3_10458.1, huMAP3_13468.1
- **Function (MyGene.info)**: propionyl-CoA carboxylase subunit beta. The protein encoded by this gene is a subunit of the propionyl-CoA carboxylase (PCC) enzyme, which is involved in the catabolism of propionyl-CoA. PCC is a mitochondrial enzyme that probably acts as a dodecamer of six alpha subunits and six beta subunits. This gene encodes the beta subunit of PCC. Defects in this gene are a cause of propionic acidemia type II (PA-2). Multiple transcript variants e…
- **Diseases (Open Targets)**: propionic acidemia (0.861); hereditary disease (0.517); hypertensive disorder (0.453); coronary artery disorder (0.438); coronary atherosclerosis (0.428)
- **Europe PMC papers**: 1404
- **Why important**: PCCB is the partner subunit of PCCA and is among the strongest network-connected genes. It occurs in both primary terms (GO:MF ligase activity, forming carbon-carbon bonds; q_global = 0.0208) (KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 0.0361), has very strong STRING relationships with PCCA, PC, ACAA1 and ALDH6A1, and is represented in several hu.MAP complexes (hu.MAP huMAP3_07028.1) (hu.MAP huMAP3_02917.1) (hu.MAP huMAP3_10458.1) (hu.MAP huMAP3_13468.1). Its annotated role as the beta subunit of propionyl-CoA carboxylase provides direct mechanistic support for the module’s propionyl-CoA and branched-chain catabolic interpretation. Propionic acidemia type two is an established disease association, with substantial literature support.
- **Conclusion**: Established evidence identifies PCCB as a core enzymatic partner of PCCA and one of the best-supported functional anchors in the module. Its presence strengthens the interpretation of a genuine mitochondrial metabolic program rather than a generic co-expression signal.

#### ALDH6A1

- **Related proteins** (co-abundance neighbors): PEPD (0.85), SERPINC1 (0.84), PCCB (0.83), PC (0.81), TAGLN (0.81); STRING partners: ACAA1 (0.952), ALDH7A1 (0.934), PCCA (0.96), PCCB (0.967)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 6 family member A1. This gene encodes a member of the aldehyde dehydrogenase protein family. The encoded protein is a mitochondrial methylmalonate semialdehyde dehydrogenase that plays a role in the valine and pyrimidine catabolic pathways. This protein catalyzes the irreversible oxidative decarboxylation of malonate and methylmalonate semialdehydes to acetyl- and propionyl-CoA. Methylmalonate semialdehyde dehydrogen…
- **Diseases (Open Targets)**: methylmalonate semialdehyde dehydrogenase deficiency (0.706); hereditary disease (0.413); alcohol drinking (0.158); atrial fibrillation (0.089); gastric cancer (0.076)
- **Europe PMC papers**: 1031
- **Why important**: ALDH6A1 occupies a central position connecting the propionyl-CoA-related genes to PEPD, SERPINC1 and TAGLN, and it has strong STRING relationships with ACAA1, ALDH7A1, PCCA and PCCB. It is included in the globally corrected valine, leucine and isoleucine degradation term (KEGG Valine, leucine and isoleucine degradation - Homo sapiens (human); q_global = 0.0361) and in several supplementary metabolic terms (4 supplementary STRING terms; within-query FDR 0.0071–0.0274). Its annotated mitochondrial methylmalonate semialdehyde dehydrogenase activity and role in valine and branched-chain catabolism provide a direct biochemical bridge between aldehyde processing and the PCC pathway. Methylmalonate semialdehyde dehydrogenase deficiency is an established disease association, with meaningful literature support.
- **Conclusion**: Established evidence supports ALDH6A1 as a central metabolic connector and a plausible contributor to the shared kidney-testis metabolic phenotype. The link from this metabolic core to SERPINC1 or TAGLN is a network-level observation and remains mechanistically unresolved.

#### C3

- **Related proteins** (co-abundance neighbors): A2M (0.89), SERPINC1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 represents the extracellular and immune-associated branch of the module. It connects to A2M and SERPINC1 in the co-abundance network, is secreted to blood, is liver-enriched, and is associated with a non-classical monocyte cell type. Its annotated role as the central complement component and its established links to complement-mediated inflammation, complement deficiency and complement-related kidney disease make it biologically important for interpreting tissue composition and disease relevance. It is represented in multiple hu.MAP extracellular complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1), although it lacks a listed STRING interaction within this module.
- **Conclusion**: Established evidence supports C3 as a complement and extracellular-fluid marker that may explain part of the shared module. It should not be assumed to be part of the mitochondrial metabolic mechanism; its co-abundance may instead report vascular, immune or extracellular context.

#### SERPINC1

- **Related proteins** (co-abundance neighbors): ALDH6A1 (0.84), C3 (0.81); STRING partners: A2M (0.927)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 is important because it marks the blood and coagulation branch and forms a strong STRING relationship with A2M. It is a liver-enriched protein secreted to blood, is not detected in immune cells, and is not detected by IHC in the listed kidney and testis samples, making it particularly informative for evaluating circulating-protein contribution. Its established function as antithrombin, its participation in blood-coagulation regulation, and its associations with hereditary antithrombin deficiency and venous thromboembolic disease provide strong functional and clinical context. It is also included in a hu.MAP extracellular complex with A2M and C3 (hu.MAP huMAP3_15040.1).
- **Conclusion**: Established evidence supports SERPINC1 as an extracellular coagulation-associated component rather than a core intracellular metabolic enzyme. Its inclusion argues for careful control of blood or extracellular-fluid effects when interpreting the kidney-testis conservation.

## Module 2

**Tissue pair**: kidney and testis  
**Genes (30)**: ABCF1, ATXN10, ATXN2L, CNOT1, COPG2, CPSF1, CPSF3, DCTN1, DDX46, DDX6, DHX36, ADAR, EPB41L2, CAST, EIF4G1, MBOAT7, NSUN2, NUP107, NUP214, PDCD4, PRPF31, GART, PYM1, RBM39, SEPTIN7, SMARCC2, SRRT, STRN, XRN2, ZW10

### Function

The module is best interpreted as a conserved RNA regulation and processing program. The strongest primary evidence is enrichment for mRNA metabolic process (GO:BP mRNA metabolic process; q_global = 2.63e-05), mRNA processing (GO:BP mRNA processing; q_global = 0.000405), RNA processing (GO:BP RNA processing; q_global = 0.00673), RNA binding (GO:MF RNA binding; q_global = 0.00108), nucleic acid binding (GO:MF nucleic acid binding; q_global = 0.000587), and catalytic activity acting on RNA (GO:MF catalytic activity, acting on RNA; q_global = 0.0367). Its components span RNA editing, RNA helicases, spliceosome-associated processing, three-prime end formation, RNA degradation, RNA modification, translation control, and RNA export. The enrichment of ribonucleoprotein granule and cytoplasmic ribonucleoprotein granule terms (GO:CC ribonucleoprotein granule; q_global = 0.011) (GO:CC cytoplasmic ribonucleoprotein granule; q_global = 0.0285) indicates coupling between nuclear RNA processing and cytoplasmic RNA fate. The kinetochore and centromeric-region terms (GO:CC kinetochore; q_global = 0.0303) (GO:CC condensed chromosome, centromeric region; q_global = 0.0303), together with the supramolecular-complex term (GO:CC supramolecular complex; q_global = 0.0346), suggest an additional cell-cycle or structural component rather than a separate dominant function. The STRING results support the same interpretation through RNA metabolism and mRNA-processing categories (4 supplementary STRING terms; within-query FDR 6.02e-06–0.0025), while these remain supplementary rather than global enrichment evidence.

**Cell composition.** This does not resemble a plasma-protein or secreted-protein module: nearly all members are intracellular, only one gene has a secretome annotation, and protein detection is broadly supported in both kidney and testis. Most genes have low tissue specificity, and most have low immune-cell specificity, arguing against a module driven primarily by blood contamination. There is nevertheless substantial cell-type enhancement, especially across spermatid and primary-spermatocyte populations, with additional enhancement in renal epithelial populations for SMARCC2. A small blood-cell-related signal is present for genes such as NUP214 and MBOAT7, but it is not a dominant module-wide pattern. The shared kidney-testis signal therefore most plausibly reflects a broadly used intracellular RNA-processing program that may be particularly active in germ-cell differentiation and in selected kidney cell types, rather than a secreted or blood-derived signature.

**GO/KEGG enrichment**: 13 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP mRNA metabolic process | 2.63e-05 | ADAR, ATXN2L, CNOT1, CPSF1, CPSF3, DDX46, DHX36, NSUN2, PRPF31, PYM1, RBM39, SRRT, XRN2 |
| GO:BP mRNA processing | 0.000405 | ADAR, CPSF1, CPSF3, DDX46, DHX36, NSUN2, PRPF31, RBM39, SRRT, XRN2 |
| GO:MF nucleic acid binding | 0.000587 | ABCF1, ADAR, ATXN2L, CNOT1, CPSF1, CPSF3, DDX46, DDX6, DHX36, EIF4G1, NSUN2, PDCD4, PRPF31, PYM1, RBM39, SMARCC2, SRRT, XRN2, ZW10 |
| GO:MF RNA binding | 0.00108 | ABCF1, ADAR, ATXN2L, CNOT1, CPSF1, CPSF3, DDX46, DDX6, DHX36, EIF4G1, NSUN2, PDCD4, PRPF31, PYM1, RBM39, SRRT, XRN2 |
| GO:BP RNA processing | 0.00673 | ADAR, CPSF1, CPSF3, DDX46, DHX36, NSUN2, PRPF31, RBM39, SRRT, XRN2 |
| GO:CC ribonucleoprotein granule | 0.011 | ATXN2L, CNOT1, DDX46, DDX6, DHX36, EIF4G1, NSUN2, PRPF31, RBM39 |
| GO:BP regulatory ncRNA-mediated gene silencing | 0.0244 | ADAR, CNOT1, DDX6, EIF4G1, SRRT |
| GO:CC cytoplasmic ribonucleoprotein granule | 0.0285 | ATXN2L, CNOT1, DDX6, DHX36, EIF4G1, NSUN2 |
| GO:CC kinetochore | 0.0303 | DCTN1, NUP107, SEPTIN7, SMARCC2, ZW10 |
| GO:CC condensed chromosome, centromeric region | 0.0303 | DCTN1, NUP107, SEPTIN7, SMARCC2, ZW10 |
| GO:CC supramolecular complex | 0.0346 | ATXN2L, CNOT1, DCTN1, DDX46, DDX6, DHX36, EIF4G1, NSUN2, NUP107, PRPF31, RBM39, SEPTIN7, SMARCC2, ZW10 |
| GO:MF catalytic activity, acting on RNA | 0.0367 | ADAR, CNOT1, CPSF3, DDX46, DDX6, DHX36, NSUN2, XRN2 |
| GO:CC nuclear protein-containing complex | 0.0487 | ADAR, CPSF1, CPSF3, DDX46, EPB41L2, NUP107, NUP214, PRPF31, PYM1, SMARCC2 |

### STRING and hu.MAP

STRING provides strong known links within several coherent subunits: CNOT1 connects with DDX6 and EIF4G1; DDX6 connects with ATXN2L and EIF4G1; EIF4G1 connects with PDCD4; CPSF1 connects with CPSF3, and CPSF3 connects with XRN2; NUP107 connects with NUP214; RBM39 connects with SRRT; and DCTN1 connects with ZW10. These relationships show that the module contains established RNA-decay, translation-control, cleavage and polyadenylation, nuclear-pore, and chromosome-segregation relationships, but the STRING network covers only a minority of all possible within-module pairs. hu.MAP independently supports several known complexes: DDX6 with ATXN2L occurs across multiple complexes (hu.MAP huMAP3_13965.1) (hu.MAP huMAP3_02526.1) (hu.MAP huMAP3_08724.1) (hu.MAP huMAP3_08431.1) (hu.MAP huMAP3_08733.1) (hu.MAP huMAP3_10338.1) (hu.MAP huMAP3_14201.1) (hu.MAP huMAP3_10207.1) (hu.MAP huMAP3_13164.1), CPSF1 with CPSF3 occurs in cleavage and polyadenylation complexes (hu.MAP huMAP3_00102.1) (hu.MAP huMAP3_09096.1) (hu.MAP huMAP3_11757.1), ADAR with NSUN2 occurs in a large RNA-related complex (hu.MAP huMAP3_12301.1), NUP107 with NUP214 occurs in a nuclear-pore complex (hu.MAP huMAP3_12581.1), PYM1 with SRRT and EPB41L2 with SRRT occur in RNA-processing complexes (hu.MAP huMAP3_11073.1) (hu.MAP huMAP3_09943.1), and DDX46 with PRPF31 occurs in spliceosomal complexes (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_08980.1). Because many hu.MAP complexes contain only a subset of the module members, the module is not simply one preassembled complex; it appears to combine several interacting RNA-processing assemblies with related cellular regulation.

**STRING interactions (score >= 0.7)**: 10 of 435 gene pairs: ATXN2L–DDX6 (0.952); CNOT1–DDX6 (0.999); CNOT1–EIF4G1 (0.814); CPSF1–CPSF3 (0.999); CPSF3–XRN2 (0.789); DCTN1–ZW10 (0.719); DDX6–EIF4G1 (0.857); EIF4G1–PDCD4 (0.974); NUP107–NUP214 (0.999); RBM39–SRRT (0.936)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Metabolism of RNA (FDR = 6.02e-06, 14 genes); Keyword RNA-binding (FDR = 2.34e-05, 12 genes); Process mRNA metabolic process (FDR = 5.63e-05, 12 genes); Function RNA binding (FDR = 9.08e-05, 18 genes); COMPARTMENTS Nuclear lumen (FDR = 0.00013, 15 genes); Function Nucleic acid binding (FDR = 0.00019, 19 genes); Keyword Ubl conjugation (FDR = 0.00022, 15 genes); Process RNA metabolic process (FDR = 0.00034, 14 genes); Keyword Nucleus (FDR = 0.00049, 20 genes); Keyword Phosphoprotein (FDR = 0.0023, 29 genes); Keyword mRNA processing (FDR = 0.0025, 7 genes); Keyword Isopeptide bond (FDR = 0.0025, 12 genes); COMPARTMENTS Nucleus (FDR = 0.0029, 21 genes); COMPARTMENTS Nucleoplasm (FDR = 0.0037, 10 genes); Keyword Mitosis (FDR = 0.0047, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13965.1 (DDX6, ATXN2L; 2/5); huMAP3_02526.1 (DDX6, ATXN2L; 2/6); huMAP3_08724.1 (DDX6, ATXN2L; 2/7); huMAP3_08431.1 (DDX6, ATXN2L; 2/8); huMAP3_08733.1 (DDX6, ATXN2L; 2/8); huMAP3_10338.1 (DDX6, ATXN2L; 2/8); huMAP3_14201.1 (DDX6, ATXN2L; 2/8); huMAP3_10207.1 (DDX6, ATXN2L; 2/9); huMAP3_13164.1 (DDX6, ATXN2L; 2/10); huMAP3_00102.1 (CPSF1, CPSF3; 2/12); huMAP3_09096.1 (CPSF1, CPSF3; 2/15); huMAP3_11757.1 (CPSF1, CPSF3; 2/16); huMAP3_12301.1 (ADAR, NSUN2; 2/26); huMAP3_12581.1 (NUP214, NUP107; 2/58); huMAP3_11073.1 (PYM1, SRRT; 2/67); huMAP3_09943.1 (EPB41L2, SRRT; 2/78); huMAP3_06511.1 (DDX46, PRPF31; 2/79); huMAP3_08980.1 (DDX46, PRPF31; 2/97)

### Novelty

The co-abundance observation is potentially novel because the module combines several established RNA-processing, RNA-decay, nuclear-transport, translation-control, and cell-division components in a conserved kidney-testis pattern, whereas STRING and hu.MAP document only selected pairwise relationships and partial complexes. However, the biological functions of its component genes and many of their relationships are already established. Therefore, the evidence supports novelty of the tissue-pair co-abundance organization or its coordinated interpretation, not novelty of the genes, complexes, or molecular functions themselves. The absence of some module-wide connections from STRING or hu.MAP cannot by itself establish that the module is a new biological complex. Experimental validation across independent kidney and testis samples, cell types, and perturbation systems would be required to claim a new mechanism.

**Hypothesis.** Hypothesis: the module coordinates transcript maturation with transcript fate during highly active or changing cellular states. In the nucleus, ADAR, DDX46, RBM39, CPSF1, CPSF3, NSUN2, XRN2, and associated factors could regulate RNA editing, splicing, modification, three-prime processing, termination, and export. After export, CNOT1, DDX6, EIF4G1, PDCD4, and ATXN2L could balance translation, storage, silencing, and decay in ribonucleoprotein granules. NUP107 and NUP214 could couple nuclear transport to this RNA workflow, while the kinetochore-associated genes could reflect the proliferative and differentiation demands of germ cells or selected renal cells. The shared kidney-testis co-abundance pattern may therefore represent a common RNA-quality-control and translational-reprogramming state, with stronger manifestation in spermatogenic cells rather than a tissue-specific secreted signal. This is a mechanistic hypothesis, not a demonstrated causal pathway.

### Important genes

#### ADAR

- **Related proteins** (co-abundance neighbors): RBM39 (0.93), XRN2 (0.92), ATXN2L (0.90), PYM1 (0.88), ABCF1 (0.88), EPB41L2 (0.87), SRRT (0.87), PDCD4 (0.85), NSUN2 (0.84), DHX36 (0.84), EIF4G1 (0.83), CAST (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_12301.1
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR is one of the most connected genes in the module and links RBM39, XRN2, ATXN2L, PYM1, ABCF1, EPB41L2, SRRT, and PDCD4 in the co-abundance network. It is the RNA-editing enzyme responsible for adenosine-to-inosine editing and is represented across many primary RNA-processing and RNA-binding terms (8 globally significant GO/KEGG terms, q_global 2.63e-05–0.0487; see the table). It has extensive literature and established associations with dyschromatosis symmetrica hereditaria and Aicardi-Goutieres-related interferonopathy. Its kidney and testis detection and broad tissue profile support a general intracellular role rather than a secreted or blood-derived explanation.
- **Conclusion**: Established evidence identifies ADAR as a central RNA-editing and RNA-processing component of the module. Its network position and broad annotation make it a strong integrator of the module, but the co-abundance data do not prove that ADAR editing causes the shared kidney-testis pattern. A plausible hypothesis is that RNA editing helps coordinate transcript processing or quality control in the shared cellular state.

#### DDX6

- **Related proteins** (co-abundance neighbors): ATXN10 (0.89), GART (0.85); STRING partners: ATXN2L (0.952), CNOT1 (0.999), EIF4G1 (0.857)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytoplasmic bodies; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_13965.1, huMAP3_02526.1, huMAP3_08724.1, huMAP3_08431.1, huMAP3_08733.1, huMAP3_10338.1, huMAP3_14201.1, huMAP3_10207.1, huMAP3_13164.1
- **Function (MyGene.info)**: DEAD-box helicase 6. This gene encodes a member of the DEAD box protein family. The protein is an RNA helicase found in P-bodies and stress granules, and functions in translation suppression and mRNA degradation. It is required for microRNA-induced gene silencing. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: intellectual developmental disorder with impaired language and dysmorphic facies (0.650); Intellectual disability (0.555); neurodegenerative disease (0.459); lung carcinoma (0.371); Global developmental delay (0.371)
- **Europe PMC papers**: 3002
- **Why important**: DDX6 connects the module to cytoplasmic RNA fate through known STRING relationships with ATXN2L, CNOT1, and EIF4G1, and it participates with ATXN2L in multiple hu.MAP complexes (hu.MAP huMAP3_13965.1) (hu.MAP huMAP3_02526.1) (hu.MAP huMAP3_08724.1) (hu.MAP huMAP3_08431.1) (hu.MAP huMAP3_08733.1) (hu.MAP huMAP3_10338.1) (hu.MAP huMAP3_14201.1) (hu.MAP huMAP3_10207.1) (hu.MAP huMAP3_13164.1). It is an RNA helicase associated with P-bodies and stress granules, mRNA degradation, translation suppression, microRNA-mediated silencing, and spermatogenesis. It is represented in the primary RNA-binding, ribonucleoprotein-granule, regulatory-gene-silencing, and RNA-catalytic evidence (7 globally significant GO/KEGG terms, q_global 0.000587–0.0367; see the table). Its literature and disease associations include intellectual disability and neurodevelopmental disorders.
- **Conclusion**: Established evidence places DDX6 at the nuclear-to-cytoplasmic RNA-fate interface and supports its importance for the module’s granule, silencing, and decay interpretation. The kidney-testis co-abundance pattern suggests coordinated activity with ATXN2L and CNOT1, but does not establish a testis-specific DDX6 mechanism. A plausible hypothesis is that DDX6-mediated storage or decay buffers transcripts during germ-cell differentiation and in analogous renal cellular states.

#### CPSF3

- **Related proteins** (co-abundance neighbors): CNOT1 (0.81); STRING partners: CPSF1 (0.999), XRN2 (0.789)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_00102.1, huMAP3_09096.1, huMAP3_11757.1
- **Function (MyGene.info)**: cleavage and polyadenylation specific factor 3. This gene encodes a member of the metallo-beta-lactamase family. The encoded protein is a 73kDa subunit of the cleavage and polyadenylation specificity factor and functions as an endonuclease that recognizes the pre-mRNA 3'-cleavage site AAUAAA prior to polyadenylation. It also cleaves after the pre-mRNA sequence ACCCA during histone 3'-end pre-mRNA processing. [provided by RefSeq, Oct 2012].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, hypotonia, nystagmus, and seizures (0.601); neurodegenerative disease (0.527); neurodevelopmental disorder with hypotonia, microcephaly, and seizures (0.416); complex neurodevelopmental disorder (0.370); dengue disease (0.370)
- **Europe PMC papers**: 548
- **Why important**: CPSF3 is the catalytic endonuclease of the cleavage and polyadenylation specificity factor and is directly paired with CPSF1 in STRING and in several hu.MAP cleavage and polyadenylation complexes (hu.MAP huMAP3_00102.1) (hu.MAP huMAP3_09096.1) (hu.MAP huMAP3_11757.1). It is represented in the primary mRNA metabolic, mRNA-processing, RNA-binding, RNA-catalytic, and nuclear-complex evidence (8 globally significant GO/KEGG terms, q_global 2.63e-05–0.0487; see the table). Its HPA cell-type enhancements include primary spermatocytes and spermatids, making it especially relevant to the shared tissue context. Its disease associations include a neurodevelopmental disorder involving microcephaly, hypotonia, nystagmus, and seizures.
- **Conclusion**: Established evidence identifies CPSF3 as a core catalytic component linking the module to pre-mRNA three-prime processing and polyadenylation. Its germ-cell expression pattern is consistent with an active transcript-maturation program, but the module does not demonstrate that altered CPSF3 activity drives the kidney-testis conservation. A plausible hypothesis is that coordinated three-prime processing is a key regulatory bottleneck in the shared state.

#### RBM39

- **Related proteins** (co-abundance neighbors): ADAR (0.93), EPB41L2 (0.86), EIF4G1 (0.85), PRPF31 (0.85); STRING partners: SRRT (0.936)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 39. This gene encodes a member of the U2AF65 family of proteins. The encoded protein is found in the nucleus, where it co-localizes with core spliceosomal proteins. It has been shown to play a role in both steroid hormone receptor-mediated transcription and alternative splicing, and it is also a transcriptional coregulator of the viral oncoprotein v-Rel. Multiple transcript variants have been observed…
- **Diseases (Open Targets)**: neurodegenerative disease (0.401); endometrial cancer (0.220); skin neoplasm (0.217); skin cancer (0.217); actinic keratosis (0.217)
- **Europe PMC papers**: 1169
- **Why important**: RBM39 has high network connectivity relative to many module members and links ADAR, EPB41L2, EIF4G1, and PRPF31. It is directly supported by the STRING relationship with SRRT and appears in many primary RNA-processing, RNA-binding, ribonucleoprotein-granule, and supramolecular-complex terms (7 globally significant GO/KEGG terms, q_global 2.63e-05–0.0346; see the table). It is a nuclear RNA-binding and splicing-associated protein that also participates in steroid-hormone-receptor transcriptional regulation. It has substantial literature and disease associations involving neurodegenerative disease and cancer.
- **Conclusion**: Established evidence supports RBM39 as a nuclear RNA-processing and transcriptional coregulator that may connect splicing with translational or cytoplasmic components of the module. Its tissue enhancement in bone marrow is not sufficient to make the module blood-derived, especially given its kidney and testis detection and low immune-cell specificity. A plausible hypothesis is that RBM39 helps couple alternative splicing to cell-state-specific gene regulation in the shared module.

#### NUP107

- **Related proteins** (co-abundance neighbors): SRRT (0.87), COPG2 (0.81); STRING partners: NUP214 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 107. This gene encodes a member of the nucleoporin family. The protein is localized to the nuclear rim and is an essential component of the nuclear pore complex (NPC). All molecules entering or leaving the nucleus either diffuse through or are actively transported by the NPC. Alternate transcriptional splice variants of this gene have been observed but have not been thoroughly characterized. [provided …
- **Diseases (Open Targets)**: Galloway-Mowat syndrome (0.665); nephrotic syndrome, type 11 (0.622); 46 XX gonadal dysgenesis (0.577); familial idiopathic steroid-resistant nephrotic syndrome (0.554); HIV infectious disease (0.541)
- **Europe PMC papers**: 1487
- **Why important**: NUP107 links the module to nuclear transport and is strongly connected to NUP214 in STRING and to a nuclear-pore complex in hu.MAP (hu.MAP huMAP3_12581.1). It contributes to mRNA export, protein transport, nuclear-pore assembly, and nuclear organization, and it is represented in the primary kinetochore, centromeric-region, supramolecular-complex, and nuclear-complex terms (4 globally significant GO/KEGG terms, q_global 0.0303–0.0487; see the table). It has established disease associations with Galloway-Mowat syndrome, nephrotic syndrome, and gonadal dysgenesis. Its enhancement in early primary spermatocytes is consistent with a role during germ-cell nuclear remodeling.
- **Conclusion**: Established evidence identifies NUP107 as a nuclear-pore component that can connect transcript processing with nucleocytoplasmic transport and cell-cycle organization. Its presence does not prove that nuclear export is the causal organizing principle of the module, but it broadens the interpretation beyond RNA catalysis alone. A plausible hypothesis is that regulated nuclear export couples transcript maturation to the cytoplasmic RNA-processing and translation machinery in both tissues.

## Module 3

**Tissue pair**: kidney and testis  
**Genes (6)**: ACADM, TSFM, IDH3A, NADK2, SUCLA2, ACAT1

### Function

This module is most consistent with coordinated mitochondrial energy metabolism. The genes form a co-abundance chain spanning fatty-acid and acyl-CoA metabolism, the tricarboxylic acid cycle, mitochondrial NADP production, and mitochondrial protein translation. The strongest functional support is supplementary STRING evidence for the mitochondrial matrix, mitochondrial localization, and transit peptides (STRING Component Mitochondrial matrix; within-query FDR = 0.00082) through (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0254). No GO or KEGG term passed global correction, so there is no globally significant GO or KEGG enrichment to report. The module therefore supports a biologically coherent mitochondrial interpretation, but the enrichment evidence should be treated as supportive rather than globally validated.

**Cell composition.** This is not a plasma-protein, secreted-protein, or blood-cell-dominated module: none of the genes is secreted, and most have low immune-cell specificity. The genes are mitochondrial and are detected at the protein level in both kidney and testis for nearly all members, with one member lacking protein-detection data. HPA patterns show tissue enhancement in liver, skeletal muscle, tongue, and kidney, together with repeated enrichment in early or late spermatids and other specialized cell types. This suggests that the shared kidney-testis signal is more plausibly related to mitochondrial metabolic activity in shared or metabolically active cell populations than to blood contamination. The liver and spermatid patterns also indicate that the module is not kidney- or testis-exclusive.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING contains the recorded high-confidence relationships ACADM–ACAT1, ACADM–SUCLA2, ACAT1–SUCLA2, and IDH3A–SUCLA2. SUCLA2 is the main STRING-connected bridge within the set, while TSFM and NADK2 have no listed STRING partners under the specified threshold. The STRING functional results consistently point to mitochondrial matrix or mitochondrial localization (STRING Component Mitochondrial matrix; within-query FDR = 0.00082), (STRING Keyword Mitochondrion; within-query FDR = 0.0079), (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.0194), (STRING COMPARTMENTS Mitochondrion; within-query FDR = 0.0254) and transit peptides (STRING Keyword Transit peptide; within-query FDR = 0.00085), but these are supplementary within-query results rather than globally corrected module evidence. No hu.MAP complex contains at least two module members. Thus, the network has partial support from known protein relationships, but it is not represented as a shared hu.MAP complex.

**STRING interactions (score >= 0.7)**: 4 of 15 gene pairs: ACADM–ACAT1 (0.717); ACADM–SUCLA2 (0.755); ACAT1–SUCLA2 (0.883); IDH3A–SUCLA2 (0.972)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Mitochondrial matrix (FDR = 0.00082, 6 genes); Keyword Transit peptide (FDR = 0.00085, 6 genes); Keyword Mitochondrion (FDR = 0.0079, 6 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.0194, 5 genes); COMPARTMENTS Mitochondrion (FDR = 0.0254, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be called a definitively new biological pathway. Its genes are individually well characterized mitochondrial enzymes or a mitochondrial translation factor, and several of the recorded STRING relationships are already known. The absence of a hu.MAP complex and the lack of STRING partners for some members do not establish novelty. A potentially novel aspect is the kidney-testis co-abundance organization of these genes as one conserved module, especially the linking of metabolic enzymes with TSFM and NADK2, but that claim requires validation in independent cohorts, protein-level measurements, and comparison with published tissue co-expression studies.

**Hypothesis.** Hypothesis: the module represents a coordinated mitochondrial capacity program that couples substrate oxidation and tricarboxylic-acid-cycle flux with mitochondrial redox support and production of mitochondrially encoded proteins. In testis, this program could support the high energetic demands of spermatid differentiation; in kidney, it could support metabolically active cells. The observed co-abundance may therefore reflect shared regulation of mitochondrial abundance or activity rather than direct physical assembly of all module proteins. This is a hypothesis, not an established causal mechanism from the supplied evidence.

### Important genes

#### SUCLA2

- **Related proteins** (co-abundance neighbors): ACADM (0.84), IDH3A (0.80); STRING partners: ACADM (0.755), ACAT1 (0.883), IDH3A (0.972)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate-CoA ligase ADP-forming subunit beta. Succinyl-CoA synthetase (SCS) is a mitochondrial matrix enzyme that acts as a heterodimer, being composed of an invariant alpha subunit and a substrate-specific beta subunit. The protein encoded by this gene is an ATP-specific SCS beta subunit that dimerizes with the SCS alpha subunit to form SCS-A, an essential component of the tricarboxylic acid cycle. SCS-A hydrolyzes ATP to convert succinate t…
- **Diseases (Open Targets)**: mitochondrial DNA depletion syndrome, encephalomyopathic form with methylmalonic aciduria (0.816); mitochondrial DNA depletion syndrome, encephalomyopathic form (0.581); neurodegenerative disease (0.485); mitochondrial disease (0.374); disease of peritoneum (0.372)
- **Europe PMC papers**: 1440
- **Why important**: SUCLA2 is a central network member linking ACADM, ACAT1, and IDH3A, and it has the strongest STRING support within the module, including a relationship with IDH3A. It encodes the beta subunit of the ATP-specific succinyl-CoA synthetase complex and connects the module to the tricarboxylic acid cycle and succinyl-CoA metabolism. Its association with myopathic mitochondrial DNA depletion syndrome gives the module disease relevance. The gene has substantial literature support.
- **Conclusion**: Established evidence supports SUCLA2 as a mitochondrial matrix enzyme in energy metabolism and as an important network bridge. It is a strong candidate for an organizing metabolic component of this module. It remains a hypothesis that SUCLA2 directly coordinates the co-abundance of the other members.

#### ACADM

- **Related proteins** (co-abundance neighbors): ACAT1 (0.86), SUCLA2 (0.84); STRING partners: ACAT1 (0.717), SUCLA2 (0.755)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA dehydrogenase medium chain. This gene encodes the medium-chain specific (C4 to C12 straight chain) acyl-Coenzyme A dehydrogenase. The homotetramer enzyme catalyzes the initial step of the mitochondrial fatty acid beta-oxidation pathway. Defects in this gene cause medium-chain acyl-CoA dehydrogenase deficiency, a disease characterized by hepatic dysfunction, fasting hypoglycemia, and encephalopathy, which can result in infant…
- **Diseases (Open Targets)**: medium chain acyl-CoA dehydrogenase deficiency (0.854); hereditary disease (0.516); rhabdomyolysis (0.370); short chain acyl-CoA dehydrogenase deficiency (0.349); Epileptic spasm (0.333)
- **Europe PMC papers**: 4795
- **Why important**: ACADM is among the most connected module members and links to ACAT1 and SUCLA2 in both the co-abundance network and STRING. It catalyzes the initial step of medium-chain fatty-acid beta-oxidation. Medium-chain acyl-CoA dehydrogenase deficiency is a well-established disease association involving hepatic dysfunction, fasting hypoglycemia, and encephalopathy. Its broad literature base and protein detection in kidney and testis make it an informative anchor for interpreting the module as an oxidative metabolism program.
- **Conclusion**: Established evidence supports ACADM as a mitochondrial fatty-acid oxidation enzyme and as a plausible metabolic entry point for the module. The data do not establish that fatty-acid oxidation is the sole driver of the kidney-testis co-abundance pattern.

#### ACAT1

- **Related proteins** (co-abundance neighbors): ACADM (0.86); STRING partners: ACADM (0.717), SUCLA2 (0.883)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA acetyltransferase 1. This gene encodes a mitochondrially localized enzyme that catalyzes the reversible formation of acetoacetyl-CoA from two molecules of acetyl-CoA. Defects in this gene are associated with 3-ketothiolase deficiency, an inborn error of isoleucine catabolism characterized by urinary excretion of 2-methyl-3-hydroxybutyric acid, 2-methylacetoacetic acid, tiglylglycine, and butanone. [provided by RefSeq,…
- **Diseases (Open Targets)**: beta-ketothiolase deficiency (0.817); hereditary disease (0.470); Abnormality of the skeletal system (0.239); neoplasm (0.115); nonpapillary renal cell carcinoma (0.105)
- **Europe PMC papers**: 4147
- **Why important**: ACAT1 catalyzes reversible acetoacetyl-CoA formation and participates in acetyl-CoA, coenzyme A, fatty-acid, and isoleucine metabolism. It is connected to ACADM in the module and to both ACADM and SUCLA2 in STRING, providing a bridge between lipid-derived acyl-CoA metabolism and central mitochondrial metabolism. It is tissue-enhanced in kidney and appears in spermatid and metabolically active cell annotations. Its association with beta-ketothiolase deficiency and substantial literature support strengthen its interpretive value.
- **Conclusion**: Established evidence supports ACAT1 as a mitochondrial acyl-CoA metabolic enzyme that reinforces the fatty-acid and ketone-related interpretation. A specific role in the shared kidney-testis module, beyond reflecting mitochondrial metabolic state, remains hypothetical.

#### IDH3A

- **Related proteins** (co-abundance neighbors): TSFM (0.82), SUCLA2 (0.80); STRING partners: SUCLA2 (0.972)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: isocitrate dehydrogenase (NAD(+)) 3 catalytic subunit alpha. Isocitrate dehydrogenases catalyze the oxidative decarboxylation of isocitrate to 2-oxoglutarate. These enzymes belong to two distinct subclasses, one of which utilizes NAD(+) as the electron acceptor and the other NADP(+). Five isocitrate dehydrogenases have been reported: three NAD(+)-dependent isocitrate dehydrogenases, which localize to the mitochondrial matrix, and two NADP(+)-dependent isoci…
- **Diseases (Open Targets)**: retinitis pigmentosa 90 (0.791); retinitis pigmentosa (0.467); neurodegenerative disease (0.437); inherited retinal dystrophy (0.381); colorectal carcinoma (0.182)
- **Europe PMC papers**: 1497
- **Why important**: IDH3A connects TSFM and SUCLA2 in the co-abundance network and has a particularly strong recorded STRING relationship with SUCLA2. It is the catalytic alpha subunit of mitochondrial NAD-dependent isocitrate dehydrogenase and directly supports tricarboxylic-acid-cycle interpretation. It is detected in kidney and testis and has associations with inherited retinal disease and neurodegenerative disease. Its literature support is substantial, although its HPA immune-cell enhancement in plasmacytoid dendritic cells is a contextual feature rather than evidence that this module is blood-cell driven.
- **Conclusion**: Established evidence supports IDH3A as a central tricarboxylic-acid-cycle enzyme and a molecular link between central carbon metabolism and this module. The immune-cell annotation should be considered a possible source of context, but it does not outweigh the overall low immune specificity of the module. Direct regulation of the module by IDH3A is not established.

#### TSFM

- **Related proteins** (co-abundance neighbors): IDH3A (0.82), NADK2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Ts translation elongation factor, mitochondrial. This gene encodes a mitochondrial translation elongation factor. The encoded protein is an enzyme that catalyzes the exchange of guanine nucleotides on the translation elongation factor Tu during the elongation step of mitchondrial protein translation. Mutations in this gene are associated with combined oxidative phosphorylation deficiency-3 syndrome. Alternate splicing results in multiple transcr…
- **Diseases (Open Targets)**: fatal mitochondrial disease due to combined oxidative phosphorylation defect type 3 (0.795); steroid-resistant nephrotic syndrome (0.474); hereditary disease (0.414); mitochondrial disease (0.372); neurodegenerative disease (0.370)
- **Europe PMC papers**: 484
- **Why important**: TSFM provides functional breadth beyond intermediary metabolism: it is a mitochondrial translation elongation factor required for elongation during mitochondrial protein synthesis. It occupies an internal position linking IDH3A and NADK2 in the co-abundance network, while lacking a listed STRING partner at the specified threshold. Its association with combined oxidative phosphorylation deficiency and steroid-resistant nephrotic syndrome connects mitochondrial translation to both systemic mitochondrial disease and kidney biology. Its literature base is smaller than that of the principal metabolic enzymes, making it especially useful for generating a mechanistic interpretation rather than merely confirming a well-known pathway.
- **Conclusion**: Established evidence supports TSFM as a mitochondrial translation factor and a plausible indicator of oxidative-phosphorylation capacity. Its placement alongside metabolic enzymes suggests coordinated mitochondrial function, but the supplied data do not prove a direct physical or regulatory interaction with them.

## Module 4

**Tissue pair**: kidney and testis  
**Genes (8)**: AFG2A, DRG2, EPS15L1, EPS15, NUP88, RBM12, UPF1, SEC23IP

### Function

The module does not have a statistically supported GO or KEGG functional annotation: no GO/KEGG term passed global correction across the module-term tests. Its most coherent biological signal is an endomembrane and RNA–protein homeostasis axis. EPS15 and EPS15L1 are associated with endocytosis, endosomal transport, vesicle organization, receptor recycling and synaptic vesicle endocytosis; this interpretation is supported by the supplementary STRING annotations (STRING SMART Ubiquitin-interacting motif.; within-query FDR = 0.0195) and (STRING SMART Eps15 homology domain; within-query FDR = 0.0452), but those terms are not globally corrected evidence. SEC23IP contributes ER-to-Golgi transport and endomembrane organization, while DRG2 is linked to cytoplasmic translation and signal transduction. UPF1 and NUP88 represent RNA surveillance, RNA export and nucleocytoplasmic transport. AFG2A contributes an AAA ATPase function and has annotations involving mitochondrial integrity and ribosome biogenesis. Thus, the safest interpretation is a mixed cellular logistics module involving vesicle trafficking, secretory-pathway transport, nucleocytoplasmic RNA handling and translational quality control, rather than a narrowly defined pathway. The absence of globally significant enrichment does not invalidate the module.

**Cell composition.** The HPA evidence argues against the module being a plasma-protein or secreted-protein module: none of the genes is annotated as secreted. The genes are broadly distributed across tissues, with low tissue specificity throughout, and protein detection is present in both kidney and testis for the genes with available data. Most genes also show low immune-cell specificity, and no blood-cell type is repeatedly enriched. Two genes have neutrophil-enhanced single-cell patterns, but this is not sufficient to assign the module to blood contamination. Other cell-type annotations are scattered across myonuclei, melanocytes, endometrial glandular cells and late primary spermatocytes. The shared kidney–testis signal is therefore more consistent with broadly expressed intracellular machinery, possibly combined with shared cellular states, than with a secreted or blood-derived program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence direct relationship within the module, EPS15–EPS15L1, and no other listed module pair is supported at the specified stringent interaction threshold. The supplementary SMART annotations (STRING SMART Ubiquitin-interacting motif.; within-query FDR = 0.0195) and (STRING SMART Eps15 homology domain; within-query FDR = 0.0452) independently point to the same EPS15/EPS15L1 pair and are consistent with ubiquitin-interacting and Eps fifteen homology domains. hu.MAP identifies the same pair together in multiple clathrin-mediated endocytosis and adaptor-complex assemblies (hu.MAP huMAP3_05120.1) through (hu.MAP huMAP3_12394.1). These complexes contain many established trafficking partners, including adaptor-complex subunits, FCHO proteins, ITSN proteins, STON proteins, NECAP proteins and other endocytic factors. The repeated recovery of EPS15 and EPS15L1 in these complexes supports a known endocytic submodule. It does not establish physical complexes involving the other module genes, because those genes are not represented as shared members in the reported hu.MAP complexes. The remaining co-abundance edges may therefore reflect coordinated expression, indirect functional coupling or shared cellular context rather than documented physical interaction.

**STRING interactions (score >= 0.7)**: 1 of 28 gene pairs: EPS15–EPS15L1 (0.99)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Ubiquitin-interacting motif. (FDR = 0.0195, 2 genes); SMART Eps15 homology domain (FDR = 0.0452, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05120.1 (EPS15, EPS15L1; 2/14); huMAP3_06283.1 (EPS15, EPS15L1; 2/19); huMAP3_08540.1 (EPS15, EPS15L1; 2/19); huMAP3_05849.1 (EPS15, EPS15L1; 2/21); huMAP3_09107.1 (EPS15, EPS15L1; 2/23); huMAP3_08320.1 (EPS15, EPS15L1; 2/24); huMAP3_09403.1 (EPS15, EPS15L1; 2/26); huMAP3_10876.1 (EPS15, EPS15L1; 2/40); huMAP3_10762.1 (EPS15, EPS15L1; 2/62); huMAP3_12918.1 (EPS15, EPS15L1; 2/62); huMAP3_12394.1 (EPS15, EPS15L1; 2/98)

### Novelty

This module should not be presented as a wholly new molecular complex or as a newly discovered pathway. The EPS15–EPS15L1 relationship and their participation in endocytic assemblies are already established by STRING and hu.MAP. The potentially novel observation is the tissue-pair co-abundance pattern that places this known endocytic pair alongside UPF1, RBM12, DRG2, AFG2A, SEC23IP and NUP88. However, the available evidence does not demonstrate that this complete combination is a previously unreported biological unit. The lack of STRING or hu.MAP support for several edges is evidence of limited prior database support, not proof of novelty. The appropriate conclusion is that this is a candidate conserved co-abundance program requiring experimental or independent cohort validation.

**Hypothesis.** Hypothesis: in cells shared between kidney and testis, coordinated expression of endocytic and secretory-pathway machinery may be coupled to nucleocytoplasmic RNA handling and protein-quality control. EPS15 and EPS15L1 could organize receptor and membrane-trafficking events; SEC23IP could connect this state to ER-to-Golgi export; UPF1, RBM12 and NUP88 could coordinate RNA surveillance, RNA processing and transport; DRG2 and AFG2A could support translational, growth-related or organelle-maintenance demands. This is a mechanistic model rather than an established interaction map. It predicts that the shared module will track intracellular trafficking and RNA or protein homeostasis in relevant kidney and testis cell populations, while the individual cross-pathway connections should be tested directly.

### Important genes

#### EPS15

- **Related proteins** (co-abundance neighbors): AFG2A (0.83), EPS15L1 (0.82), UPF1 (0.81); STRING partners: EPS15L1 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_05120.1, huMAP3_06283.1, huMAP3_08540.1, huMAP3_05849.1, huMAP3_09107.1, huMAP3_08320.1, huMAP3_09403.1, huMAP3_10876.1, huMAP3_10762.1, huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: epidermal growth factor receptor pathway substrate 15. This gene encodes a protein that is part of the EGFR pathway. The protein is present at clatherin-coated pits and is involved in receptor-mediated endocytosis of EGF. Notably, this gene is rearranged with the HRX/ALL/MLL gene in acute myelogeneous leukemias. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, May 2009].
- **Diseases (Open Targets)**: atrial fibrillation (0.399); Abnormality of the skeletal system (0.383); bile duct carcinoma (0.370); esophageal adenocarcinoma (0.370); B-cell acute lymphoblastic leukemia (0.370)
- **Europe PMC papers**: 2810
- **Why important**: EPS15 is a central network gene with the highest connectivity alongside UPF1 and is the principal annotated endocytic component. It participates in receptor-mediated endocytosis, receptor recycling, Golgi-to-endosome transport and vesicle organization. It forms the only STRING-supported direct pair in the module with EPS15L1 and appears with EPS15L1 in every reported hu.MAP complex (hu.MAP huMAP3_05120.1) through (hu.MAP huMAP3_12394.1). Its substantial literature volume and disease associations make it the best-established biological anchor.
- **Conclusion**: Established evidence supports EPS15 as an endocytic and vesicle-trafficking anchor of the module. Its connection to the other module genes beyond EPS15L1 remains a co-abundance-based hypothesis.

#### EPS15L1

- **Related proteins** (co-abundance neighbors): EPS15 (0.82), RBM12 (0.82); STRING partners: EPS15 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_05120.1, huMAP3_06283.1, huMAP3_08540.1, huMAP3_05849.1, huMAP3_09107.1, huMAP3_08320.1, huMAP3_09403.1, huMAP3_10876.1, huMAP3_10762.1, huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: epidermal growth factor receptor pathway substrate 15 like 1. Enables cadherin binding activity. Predicted to be involved in endocytosis and endosomal transport. Located in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: split hand-foot malformation (0.370); lysosomal storage disease (0.310); neurodegenerative disease (0.310); Alzheimer disease (0.310); Parkinson disease (0.310)
- **Europe PMC papers**: 426
- **Why important**: EPS15L1 is the obligate partner of EPS15 in the strongest STRING relationship and is repeatedly present with EPS15 in hu.MAP endocytic assemblies (hu.MAP huMAP3_05120.1) through (hu.MAP huMAP3_12394.1). It is annotated for endocytosis, endosomal transport and synaptic vesicle endocytosis, and it has cadherin-binding activity. Its network position links EPS15 to RBM12, making it important for the module’s most coherent trafficking-centered substructure. Its disease associations and established literature provide additional biological support.
- **Conclusion**: Established evidence supports EPS15L1 as a member of an EPS fifteen-centered endocytic machinery. Its proposed bridge to RNA-related genes through co-abundance is a hypothesis, not a demonstrated molecular interaction.

#### UPF1

- **Related proteins** (co-abundance neighbors): RBM12 (0.90), DRG2 (0.85), EPS15 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UPF1 RNA helicase and ATPase. This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons.…
- **Diseases (Open Targets)**: Intellectual disability (0.437); Global developmental delay (0.426); High anterior hairline (0.425); Frontal bossing (0.425); Hypertelorism (0.425)
- **Europe PMC papers**: 4252
- **Why important**: UPF1 has the strongest network position in the module and connects the EPS15 branch with RBM12 and DRG2. It is a core RNA helicase and ATPase involved in nonsense-mediated decay, mRNA export and translational termination, with additional annotations in DNA replication and repair. Its extensive literature and developmental disease associations make it a strong candidate for interpreting the module beyond membrane trafficking.
- **Conclusion**: Established evidence supports UPF1 as an RNA surveillance and mRNA quality-control factor. The module data support coordinated expression with endocytic genes, but do not establish that UPF1 directly regulates EPS15 or EPS15L1 in these tissues.

#### SEC23IP

- **Related proteins** (co-abundance neighbors): DRG2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC23 interacting protein. This gene encodes a member of the phosphatidic acid preferring-phospholipase A1 family. The encoded protein is localized to endoplasmic reticulum exit sites and plays a critical role in ER-Golgi transport as part of the multimeric coat protein II complex. An orthologous gene in frogs is required for normal neural crest cell development, suggesting that this gene may play a role in Waardenburg synd…
- **Diseases (Open Targets)**: Parkinson disease (0.409); type 2 diabetes mellitus (0.372); cardiomyopathy (0.326); diabetes mellitus (0.294); Genu valgum (0.269)
- **Europe PMC papers**: 265
- **Why important**: SEC23IP provides the module’s clearest link to ER exit sites, COPII-associated ER-to-Golgi transport and Golgi organization. It is connected to DRG2 in the co-abundance graph and is detected in both kidney and testis by HPA. Its annotations also include spermatid development, which is relevant to the testis component, while its disease associations broaden its potential biomedical importance.
- **Conclusion**: Established evidence supports SEC23IP as an ER-to-Golgi and endomembrane trafficking factor. Its connection to the EPS fifteen-centered machinery is currently a module-level hypothesis rather than a documented physical relationship.

#### NUP88

- **Related proteins** (co-abundance neighbors): AFG2A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 88. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins, a family of 50 to 100 proteins, are the main components of the nuclear pore complex in eukaryotic cells. The protein encoded by this gene belongs to the nucleoporin family and is associated with th…
- **Diseases (Open Targets)**: fetal akinesia deformation sequence 1 (0.656); Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.527); fetal akinesia deformation sequence (0.378)
- **Europe PMC papers**: 1030
- **Why important**: NUP88 occupies a terminal position in the module but contributes a distinct and biologically important process: nucleocytoplasmic transport. Its annotations include nuclear export of ribosomal subunits, mRNA export and protein import and export. Its cell-type-enhanced pattern in late primary spermatocytes is relevant to the testis context, and its disease and cancer-related evidence gives it substantial interpretive value despite the absence of STRING or hu.MAP support within this module.
- **Conclusion**: Established evidence supports NUP88 as a nucleoporin involved in macromolecular transport. Its proposed participation in a shared trafficking and RNA-homeostasis program is plausible but not directly demonstrated by the reported interaction resources.

## Module 5

**Tissue pair**: kidney and testis  
**Genes (39)**: PGM3, AP1B1, AP2B1, AP3B1, AP3D1, ATP2A2, ATAD3A, HSPA5, MTHFD1, COPB1, CTNND1, CYFIP1, DNM1L, DYNC1H1, DNM2, EIF3C, GARS1, GNL1, HSP90AA1, HK1, HYOU1, METAP2, NCKAP1, PDCD6IP, PDIA4, PFAS, SACM1L, SF3B3, AARS1, TNPO1, TRIM25, TXNRD1, UBA6, USP5, USO1, WASHC5, XPO1, XPO4, XPNPEP1

### Function

No GO/KEGG term passed global correction, so the module does not support a formally significant pathway label from primary enrichment. Its biological content nevertheless points to intracellular protein and membrane logistics. The module contains components of coatomer and adaptor systems, including AP1B1, AP2B1, AP3B1, AP3D1 and COPB1, together with vesicle transport factors such as USO1 and DNM2. It also contains nuclear transport factors, translational machinery, aminoacyl-tRNA synthetases, protein-folding and endoplasmic-reticulum stress proteins, ubiquitin-system components, cytoskeletal regulators and organelle-dynamics proteins. The supplementary STRING results reinforce a membrane-coat and adaptor organization through (STRING InterPro Armadillo-like helical; within-query FDR = 0.00029), (STRING InterPro Clathrin/coatomer adaptor, adaptin-like, N-terminal; within-query FDR = 0.0012), (STRING InterPro Armadillo-type fold; within-query FDR = 0.0017), (STRING COMPARTMENTS Membrane coat; within-query FDR = 0.0195), (STRING COMPARTMENTS AP-type membrane coat adaptor complex; within-query FDR = 0.0274) and (STRING InterPro Armadillo; within-query FDR = 0.0425), while (STRING Pfam non-SMC mitotic condensation complex subunit 1; within-query FDR = 0.0043) reflects shared annotation of adaptor genes rather than proof of a complete mitotic complex. Overall, this is best interpreted as a mixed intracellular maintenance and trafficking module rather than a narrowly defined pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: HPA identifies only a small secreted or intracellular-and-membrane subset, while most genes are intracellular. Most genes have low tissue specificity, and the proteins are detected in both kidney and testis for nearly all members, supporting a broadly expressed cellular program rather than a kidney-specific or testis-specific secretome. Immune-cell specificity is generally low, so the module is not strongly suggestive of blood-cell contamination, although selected genes show monocyte, myeloid, neutrophil or plasma-cell associations. Cell-type-enhanced annotations are heterogeneous and include late spermatogenic cells, microglia, muscle-related cells, epithelial cells and secretory-cell populations. Thus, shared cell types or ubiquitous cellular machinery may contribute to the conserved signal, but the HPA evidence does not support a simple blood-derived explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING shows a sparse but biologically coherent set of already known relationships. The strongest evidence concerns the AP adaptor group, especially AP3B1 with AP3D1, AP1B1 with AP2B1 and AP3D1, and links from adaptors to DNM2. COPB1 is linked to USO1, CYFIP1 is linked to NCKAP1, and the chaperone cluster connects HSPA5, HYOU1, PDIA4 and HSP90AA1. Nuclear transport relationships include TNPO1 with XPO1 and XPO1 with XPO4, while AARS1 and GARS1 form a known aminoacyl-tRNA synthetase relationship. These observations indicate that portions of the co-abundance module recapitulate established protein interaction systems. hu.MAP independently supports partial membership in adaptor, AP3, coatomer, nuclear-transport, chaperone, aminoacyl-tRNA synthetase and cytoskeletal complexes, including (hu.MAP huMAP3_14442.1), (hu.MAP huMAP3_11232.1), (hu.MAP huMAP3_12394.1), (hu.MAP huMAP3_06230.1), (hu.MAP huMAP3_07455.1), (hu.MAP huMAP3_11534.1), (hu.MAP huMAP3_04405.1), (hu.MAP huMAP3_02474.1) and (hu.MAP huMAP3_08540.1). Many hu.MAP matches contain only a subset of the full complex, so they support modular reuse of known machinery rather than proving that the entire co-abundance module is one physical complex.

**STRING interactions (score >= 0.7)**: 19 of 741 gene pairs: AARS1–GARS1 (0.983); AARS1–HYOU1 (0.709); AP1B1–AP2B1 (0.819); AP1B1–AP3D1 (0.844); AP1B1–DNM2 (0.717); AP2B1–AP3D1 (0.853); AP2B1–DNM2 (0.759); AP3B1–AP3D1 (0.999); COPB1–USO1 (0.869); CYFIP1–NCKAP1 (0.999); DYNC1H1–HSP90AA1 (0.909); HSP90AA1–HSPA5 (0.968); HSP90AA1–HYOU1 (0.842); HSPA5–HYOU1 (0.999); HSPA5–PDIA4 (0.99); HSPA5–TXNRD1 (0.7); HYOU1–PDIA4 (0.997); TNPO1–XPO1 (0.868); XPO1–XPO4 (0.904)
**STRING functional enrichment (supplementary, within-query FDR)**: InterPro Armadillo-like helical (FDR = 0.00029, 10 genes); InterPro Clathrin/coatomer adaptor, adaptin-like, N-terminal (FDR = 0.0012, 5 genes); InterPro Armadillo-type fold (FDR = 0.0017, 10 genes); Pfam non-SMC mitotic condensation complex subunit 1 (FDR = 0.0043, 4 genes); PMID (2022) High content screening and proteomic analysis identify a kinase inhibitor that rescues pathological phenotypes in a patient-derived model of Parkinsons disease. (FDR = 0.0172, 9 genes); COMPARTMENTS Membrane coat (FDR = 0.0195, 6 genes); COMPARTMENTS AP-type membrane coat adaptor complex (FDR = 0.0274, 4 genes); InterPro Armadillo (FDR = 0.0425, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (UBA6, GARS1, AARS1, XPNPEP1; 4/57); huMAP3_11232.1 (DNM2, TNPO1, XPO4; 3/78); huMAP3_09592.1 (XPO1, ATP2A2, TNPO1; 3/95); huMAP3_12394.1 (USO1, AP2B1, AP1B1; 3/98); huMAP3_06230.1 (AP3B1, AP3D1; 2/4); huMAP3_07455.1 (HSPA5, HYOU1; 2/4); huMAP3_03536.1 (AP3B1, AP3D1; 2/5); huMAP3_11534.1 (GARS1, AARS1; 2/5); huMAP3_13727.1 (AP3B1, AP3D1; 2/6); huMAP3_03149.1 (AP3B1, AP3D1; 2/7); huMAP3_14281.1 (AP3B1, AP3D1; 2/7); huMAP3_12325.1 (AP3B1, AP3D1; 2/8); huMAP3_12813.1 (AP3B1, AP3D1; 2/9); huMAP3_15082.1 (AP3B1, AP3D1; 2/9); huMAP3_11493.1 (AP3B1, AP3D1; 2/10); huMAP3_12157.1 (AP3B1, AP3D1; 2/10); huMAP3_04405.1 (COPB1, SACM1L; 2/10); huMAP3_09332.1 (COPB1, SACM1L; 2/11); huMAP3_02474.1 (CYFIP1, NCKAP1; 2/13); huMAP3_07170.1 (XPO1, ATP2A2; 2/14); huMAP3_12869.1 (COPB1, SACM1L; 2/16); huMAP3_08540.1 (AP2B1, AP1B1; 2/19); huMAP3_09107.1 (AP2B1, AP1B1; 2/23); huMAP3_09598.1 (CYFIP1, NCKAP1; 2/23); huMAP3_08320.1 (AP2B1, AP1B1; 2/24); huMAP3_10473.1 (ATP2A2, ATAD3A; 2/24); huMAP3_09053.1 (TNPO1, XPO4; 2/25); huMAP3_09403.1 (AP2B1, AP1B1; 2/26); huMAP3_12376.1 (AP2B1, AP1B1; 2/32); huMAP3_13345.1 (CYFIP1, NCKAP1; 2/35); huMAP3_10876.1 (AP2B1, AP1B1; 2/40); huMAP3_06775.1 (PDIA4, HYOU1; 2/60); huMAP3_10762.1 (AP2B1, AP1B1; 2/62); huMAP3_12918.1 (AP2B1, AP1B1; 2/62); huMAP3_06247.1 (ATP2A2, TNPO1; 2/65); huMAP3_09327.1 (PDIA4, HYOU1; 2/93)

### Novelty

The module-level observation may be a new finding in the specific kidney-testis co-abundance analysis, but it should not be presented as discovery of a new molecular pathway. Several of its central relationships and complexes are already represented in STRING and hu.MAP, and many component genes are broadly expressed housekeeping or cellular-maintenance genes. The absence of a complete module-level match in either resource would not establish novelty, because co-abundance modules can combine proteins from several physical complexes and database coverage is incomplete. A cautious conclusion is that the conserved tissue-pair module is potentially novel as a systems-level association, while its main biological building blocks are established. Demonstrating novelty would require independent replication, tissue-resolved validation, and evidence that the cross-tissue co-abundance pattern exceeds what is expected from ubiquitous expression, shared cell types and known interaction architecture.

**Hypothesis.** Hypothesis: the module represents coordinated demand for intracellular logistics in cells present in both kidney and testis. Coatomer and adaptor proteins may organize Golgi, endosomal and lysosomal cargo flow; USO1 and COPB1 may support ER-to-Golgi and retrograde transport; DNM2 and the CYFIP1-NCKAP1 system may couple membrane remodeling to actin dynamics; and TNPO1, XPO1 and XPO4 may coordinate nuclear-cytoplasmic cargo exchange. In parallel, EIF3C, AARS1, GARS1, HSPA5, HYOU1 and PDIA4 may support translation, folding and ER proteostasis, with ATP2A2, TXNRD1 and DNM1L contributing calcium, redox and organelle-homeostasis context. The shared module could therefore reflect a common cellular state involving cargo trafficking, protein synthesis and stress resilience, rather than a single tissue-specific function. This remains a hypothesis because the primary enrichment analysis yielded no globally significant GO/KEGG term and co-abundance does not establish direct physical or causal interaction.

### Important genes

#### AP3D1

- **Related proteins** (co-abundance neighbors): SF3B3 (0.87), EIF3C (0.86), USP5 (0.85), ATP2A2 (0.85), AARS1 (0.83), METAP2 (0.83), PGM3 (0.82), COPB1 (0.82), DYNC1H1 (0.82), CTNND1 (0.81), MTHFD1 (0.81), PDCD6IP (0.81), TRIM25 (0.81); STRING partners: AP1B1 (0.844), AP2B1 (0.853), AP3B1 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06230.1, huMAP3_03536.1, huMAP3_13727.1, huMAP3_03149.1, huMAP3_14281.1, huMAP3_12325.1, huMAP3_12813.1, huMAP3_15082.1, huMAP3_11493.1, huMAP3_12157.1
- **Function (MyGene.info)**: adaptor related protein complex 3 subunit delta 1. The protein encoded by this gene is a subunit of the AP3 adaptor-like complex, which is not clathrin-associated, but is associated with the golgi region, as well as more peripheral structures. The AP-3 complex facilitates the budding of vesicles from the golgi membrane, and may be directly involved in trafficking to lysosomes. This subunit is implicated in intracellular biogenesis and trafficking …
- **Diseases (Open Targets)**: Hermansky-Pudlak syndrome 10 (0.584); Hermansky-Pudlak syndrome 2 (0.455); Hermansky-Pudlak syndrome (0.432); Alzheimer disease (0.421); lysosomal storage disease (0.417)
- **Europe PMC papers**: 637
- **Why important**: AP3D1 is a central trafficking anchor in the module and has strong connections to AP3B1, AP1B1 and AP2B1 in STRING. It is represented across many hu.MAP AP3 complexes through (hu.MAP huMAP3_06230.1), (hu.MAP huMAP3_03536.1), (hu.MAP huMAP3_13727.1), (hu.MAP huMAP3_14281.1) and related entries. Its established function in AP3-mediated Golgi, lysosomal and specialized-granule trafficking directly supports the module's strongest mechanistic theme. Its association with Hermansky-Pudlak syndromes and lysosomal disease gives the finding disease relevance, while its literature base is substantial.
- **Conclusion**: Established evidence supports AP3D1 as an important vesicle-trafficking component and one of the best mechanistic anchors of the module. The hypothesis that it organizes the kidney-testis co-abundance pattern through shared lysosomal or specialized-vesicle demand is plausible but not demonstrated.

#### AP1B1

- **Related proteins** (co-abundance neighbors): PDCD6IP (0.85), XPO4 (0.84), WASHC5 (0.82), CTNND1 (0.81), NCKAP1 (0.80); STRING partners: AP2B1 (0.819), AP3D1 (0.844), DNM2 (0.717)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_12394.1, huMAP3_08540.1, huMAP3_09107.1, huMAP3_08320.1, huMAP3_09403.1, huMAP3_12376.1, huMAP3_10876.1, huMAP3_10762.1, huMAP3_12918.1
- **Function (MyGene.info)**: adaptor related protein complex 1 subunit beta 1. Adaptor protein complex 1 is found at the cytoplasmic face of coated vesicles located at the Golgi complex, where it mediates both the recruitment of clathrin to the membrane and the recognition of sorting signals within the cytosolic tails of transmembrane receptors. This complex is a heterotetramer composed of two large, one medium, and one small adaptin subunit. The protein encoded by this gene…
- **Diseases (Open Targets)**: ichthyosiform erythroderma, corneal involvement, and hearing loss (0.715); HIV infectious disease (0.503); MEDNIK syndrome (0.371); neurodegenerative disease (0.370); KID syndrome (0.292)
- **Europe PMC papers**: 500
- **Why important**: AP1B1 has a prominent position among the adaptor-related module genes and connects to AP2B1, AP3D1 and DNM2 in STRING. It recurs in many hu.MAP adaptor and endocytic complexes, including (hu.MAP huMAP3_12394.1), (hu.MAP huMAP3_08540.1), (hu.MAP huMAP3_09107.1), (hu.MAP huMAP3_08320.1), (hu.MAP huMAP3_09403.1) and (hu.MAP huMAP3_12376.1). Its established role in clathrin recruitment, cargo recognition, intracellular transport and basolateral secretion makes it a strong link between membrane sorting and tissue-cell polarity. It also has disease associations involving epithelial and systemic trafficking phenotypes.
- **Conclusion**: Established evidence identifies AP1B1 as a core membrane-sorting component whose presence strengthens the trafficking interpretation. Its specific contribution to conservation between kidney and testis remains a hypothesis and could reflect shared epithelial or germ-cell transport requirements.

#### EIF3C

- **Related proteins** (co-abundance neighbors): PFAS (0.91), COPB1 (0.90), TNPO1 (0.90), ATP2A2 (0.90), AARS1 (0.89), USP5 (0.89), XPNPEP1 (0.86), AP3D1 (0.86), SF3B3 (0.86), DNM1L (0.84), NCKAP1 (0.84), GNL1 (0.84), PDCD6IP (0.83), MTHFD1 (0.83), DYNC1H1 (0.83), CTNND1 (0.83), AP2B1 (0.82), GARS1 (0.82), PGM3 (0.81), AP3B1 (0.80), XPO1 (0.80), HSP90AA1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C has the most prominent network position in the supplied module and connects to genes spanning trafficking, translation, nuclear transport, metabolism and proteostasis. Its established role as a subunit of the eukaryotic translation-initiation complex provides a plausible explanation for its broad network reach. HPA indicates low tissue specificity with detection in kidney and testis, and its literature base is extensive, including cancer-related associations.
- **Conclusion**: Established evidence supports EIF3C as a broadly used translation-initiation factor and a likely coordinator of general cellular demand. Its high module connectivity may reflect shared housekeeping biology rather than a tissue-specific regulatory role, so any claim that it drives the module is hypothetical.

#### HSPA5

- **Related proteins** (co-abundance neighbors): PDIA4 (0.83), HYOU1 (0.82); STRING partners: HSP90AA1 (0.968), HYOU1 (0.999), PDIA4 (0.99), TXNRD1 (0.7)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_07455.1
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is a central ER chaperone in the proteostasis portion of the module and has strong STRING relationships with HYOU1, PDIA4, HSP90AA1 and TXNRD1. hu.MAP supports its chaperone context with (hu.MAP huMAP3_07455.1). Its established functions in ER protein folding and the unfolded-protein response connect the module to protein quality control, while its presence in epididymal cell types and plasma-cell annotations indicates relevance to cells with substantial protein-handling demands. It also has a very large literature base.
- **Conclusion**: Established evidence supports HSPA5 as a proteostasis and ER-homeostasis component. The hypothesis that coordinated ER stress handling helps explain the shared kidney-testis signal is credible, but the co-abundance data do not establish active stress or causality.

#### CTNND1

- **Related proteins** (co-abundance neighbors): GNL1 (0.86), DNM1L (0.85), HK1 (0.85), NCKAP1 (0.85), PGM3 (0.85), PDCD6IP (0.84), AARS1 (0.84), ATP2A2 (0.83), EIF3C (0.83), HYOU1 (0.83), SACM1L (0.82), USO1 (0.82), AP1B1 (0.81), AP3D1 (0.81), XPNPEP1 (0.81), PDIA4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin delta 1. This gene encodes a member of the Armadillo protein family, which function in adhesion between cells and signal transduction. Multiple translation initiation codons and alternative splicing result in many different isoforms being translated. Not all of the full-length natures of the described transcript variants have been determined. Read-through transcription also exists between this gene and the…
- **Diseases (Open Targets)**: blepharocheilodontic syndrome (0.724); listeriosis (0.526); cleft lip (0.510); hereditary disease (0.415); exudative vitreoretinopathy (0.376)
- **Europe PMC papers**: 3021
- **Why important**: CTNND1 is one of the higher-connectivity genes and links to membrane, cytoskeletal, metabolic and vesicle-associated members of the module. Its armadillo-family annotation is consistent with the supplementary STRING results (STRING InterPro Armadillo-like helical; within-query FDR = 0.00029), (STRING InterPro Armadillo-type fold; within-query FDR = 0.0017) and (STRING InterPro Armadillo; within-query FDR = 0.0425). Its established roles in cadherin-mediated cell adhesion, signal transduction and cell migration are relevant to epithelial organization in kidney and to specialized cellular architecture in testis. It has strong disease and literature support.
- **Conclusion**: Established evidence supports CTNND1 as a membrane-associated adhesion and signaling regulator that may connect trafficking to cell architecture. Its role as a bridge within this particular conserved module is a hypothesis, not a demonstrated physical mechanism.

#### ATP2A2

- **Related proteins** (co-abundance neighbors): EIF3C (0.90), TNPO1 (0.86), AP3D1 (0.85), PFAS (0.84), USP5 (0.83), CTNND1 (0.83), TRIM25 (0.83), DNM1L (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_09592.1, huMAP3_07170.1, huMAP3_10473.1, huMAP3_06247.1
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darie…
- **Diseases (Open Targets)**: Darier disease (0.823); acrokeratosis verruciformis (0.663); neurodegenerative disease (0.507); hereditary disease (0.416); schizophrenia (0.406)
- **Europe PMC papers**: 9327
- **Why important**: ATP2A2 is well connected to EIF3C, TNPO1, AP3D1, PFAS, USP5, CTNND1, TRIM25 and DNM1L. It is represented in several hu.MAP complexes, including (hu.MAP huMAP3_09592.1), (hu.MAP huMAP3_07170.1), (hu.MAP huMAP3_10473.1) and (hu.MAP huMAP3_06247.1). Its established SERCA function links the module to intracellular calcium storage and homeostasis, while its Darier disease association provides a clear disease connection. HPA shows enrichment in muscle-related tissues and detection in both target tissues, and its literature base is extensive.
- **Conclusion**: Established evidence supports ATP2A2 as a calcium-homeostasis component that may influence membrane trafficking, adhesion and organelle function. A coordinated calcium-trafficking role in the shared module is a reasonable hypothesis, but it is not proven by the co-abundance network.

## Module 6

**Tissue pair**: kidney and testis  
**Genes (14)**: AIMP2, BOLA2, CCDC6, CHORDC1, DAZAP1, LZTFL1, PSMC4, PSMA1, PSMD13, RAE1, SAE1, SEH1L, SPART, SRPK1

### Function

The module is best interpreted as a mixed intracellular proteostasis, RNA-processing, and nuclear-transport module with a possible germ-cell context. PSMA1, PSMC4, and PSMD13 form a proteasome-centered core supported by STRING and hu.MAP complexes (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1), and (hu.MAP huMAP3_05064.1). RAE1 and SEH1L provide a nuclear-pore and nucleocytoplasmic-transport component supported by STRING and hu.MAP complex (hu.MAP huMAP3_12581.1). AIMP2, SRPK1, DAZAP1, and CHORDC1 add links to translation-complex assembly, RNA splicing, spermatogenesis, protein folding, and centrosome biology. No GO or KEGG term passed global correction, so no GO or KEGG enrichment can be claimed as primary evidence. The STRING results (STRING RCTM Disorders of transmembrane transporters; within-query FDR = 0.0234) through (STRING RCTM SCF(Skp2)-mediated degradation of p27/p21; within-query FDR = 0.0483) are supplementary and mainly support proteasomal degradation, immune-related context, and cell-cycle substrate turnover.

**Cell composition.** This is not a plasma-protein or secreted-protein module. The HPA summary reports no secreted genes, and the proteins are predominantly intracellular. Most genes have low tissue specificity, while a smaller component is tissue-enhanced in skeletal muscle or testis. Many genes are cell-type-enhanced in late primary spermatocytes and early or late spermatids, and RAE1 is tissue-enhanced in testis. The generally low immune-cell specificity argues against interpreting the module primarily as blood contamination, although SRPK1 and SPART have basophil-related annotations. Protein detection in both kidney and testis supports presence in both tissues but does not establish that the same cell type drives the co-abundance.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

Known relationships are concentrated in two subnetworks. PSMA1, PSMC4, and PSMD13 form a strongly supported STRING triangle and recur together in hu.MAP proteasome complexes (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1), and (hu.MAP huMAP3_05064.1). RAE1 and SEH1L have a strong STRING relationship and co-occur in the nuclear-pore-related hu.MAP complex (hu.MAP huMAP3_12581.1). Several other module edges have no corresponding high-confidence STRING or hu.MAP relationship in the supplied evidence. Therefore, the module is partly anchored in established complexes but is not a single experimentally consolidated complex. The STRING enrichment terms (STRING RCTM Disorders of transmembrane transporters; within-query FDR = 0.0234) through (STRING RCTM SCF(Skp2)-mediated degradation of p27/p21; within-query FDR = 0.0483) are supplementary and must not be treated as globally corrected enrichment.

**STRING interactions (score >= 0.7)**: 4 of 91 gene pairs: PSMA1–PSMC4 (0.999); PSMA1–PSMD13 (0.999); PSMC4–PSMD13 (0.999); RAE1–SEH1L (0.964)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Disorders of transmembrane transporters (FDR = 0.0234, 5 genes); RCTM Host Interactions of HIV factors (FDR = 0.0241, 5 genes); RCTM Activation of NF-kappaB in B cells (FDR = 0.0483, 3 genes); RCTM Oxygen-dependent proline hydroxylation of Hypoxia-inducible Factor Alpha (FDR = 0.0483, 3 genes); RCTM ER-Phagosome pathway (FDR = 0.0483, 3 genes); RCTM Cross-presentation of soluble exogenous antigens (endosomes) (FDR = 0.0483, 3 genes); RCTM Cytokine Signaling in Immune system (FDR = 0.0483, 5 genes); RCTM Autodegradation of Cdh1 by Cdh1:APC/C (FDR = 0.0483, 3 genes); RCTM SCF-beta-TrCP mediated degradation of Emi1 (FDR = 0.0483, 3 genes); RCTM APC/C:Cdc20 mediated degradation of Securin (FDR = 0.0483, 3 genes); RCTM APC/C:Cdh1 mediated degradation of Cdc20 and other APC/C:Cdh1 targeted proteins in late mitosis/early G1 (FDR = 0.0483, 3 genes); RCTM Cdc20:Phospho-APC/C mediated degradation of Cyclin A (FDR = 0.0483, 3 genes); RCTM Vpu mediated degradation of CD4 (FDR = 0.0483, 3 genes); RCTM Vif-mediated degradation of APOBEC3G (FDR = 0.0483, 3 genes); RCTM SCF(Skp2)-mediated degradation of p27/p21 (FDR = 0.0483, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09656.1 (PSMA1, PSMC4, PSMD13; 3/64); huMAP3_13725.1 (PSMA1, PSMC4, PSMD13; 3/69); huMAP3_05064.1 (PSMC4, PSMD13; 2/31); huMAP3_12581.1 (RAE1, SEH1L; 2/58)

### Novelty

The module is not a wholly new molecular complex because its proteasome and nuclear-pore relationships are already represented in STRING and hu.MAP. Its potentially novel feature is the tissue-pair co-abundance pattern connecting established proteostasis and nuclear-transport components with spermatogenesis, RNA-processing, ciliary, and disease-relevant genes. Absence of some edges from STRING or hu.MAP does not prove novelty, and the absence of globally significant GO or KEGG terms limits claims of a newly defined pathway. The cautious conclusion is a potentially novel tissue-contextual association built from partly well-known components that requires replication and cell-resolved validation.

**Hypothesis.** Hypothesis: in germ-cell-rich or otherwise specialized kidney and testis cellular contexts, coordinated demand for protein quality control, RNA handling, nuclear transport, and cell-structure maintenance produces the observed co-abundance pattern. The proteasome branch may remove damaged or regulated proteins during differentiation, while the RAE1-SEH1L branch may support RNA export, nuclear-pore function, and mitotic organization. AIMP2, SRPK1, and DAZAP1 may connect translation-complex assembly and RNA splicing to spermatogenic programs, while LZTFL1 may connect the pattern to ciliary trafficking and reproductive or kidney disease biology. This is a mechanistic hypothesis rather than an enrichment result.

### Important genes

#### PSMC4

- **Related proteins** (co-abundance neighbors): SPART (0.89), CCDC6 (0.86), PSMD13 (0.85), PSMA1 (0.80); STRING partners: PSMA1 (0.999), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1, huMAP3_05064.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 4. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.603); mantle cell lymphoma (0.542); neoplasm (0.519); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1065
- **Why important**: PSMC4 is a highly connected node linking SPART, CCDC6, PSMD13, and PSMA1. It is a proteasome ATPase component, has strong STRING relationships with PSMA1 and PSMD13, and appears in hu.MAP complexes (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1), and (hu.MAP huMAP3_05064.1). Its annotations include proteolysis, ubiquitin-dependent protein catabolism, oxidative-stress response, and type-I-interferon response. It has disease associations involving plasma-cell myeloma, mantle-cell lymphoma, neoplasm, HIV infectious disease, and amyloidosis, together with substantial literature support.
- **Conclusion**: Established evidence supports PSMC4 as an anchor of the proteasome-centered portion of the module. The module supports a role in shared intracellular proteostasis, but does not establish a kidney-testis-specific proteasome form or a causal role in spermatogenesis.

#### PSMD13

- **Related proteins** (co-abundance neighbors): PSMC4 (0.85), SAE1 (0.83), AIMP2 (0.80), SRPK1 (0.80); STRING partners: PSMA1 (0.999), PSMC4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1, huMAP3_05064.1
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 is a highly connected proteasome-associated node joining PSMC4 to SAE1, AIMP2, and SRPK1. It has strong STRING links to PSMA1 and PSMC4 and occurs in hu.MAP complexes (hu.MAP huMAP3_09656.1), (hu.MAP huMAP3_13725.1), and (hu.MAP huMAP3_05064.1). It is a non-ATPase component of the proteasome with annotations for ubiquitin-dependent catabolism, oxidative-stress response, and type-I-interferon response. Its disease associations include plasma-cell myeloma, mantle-cell lymphoma, neurodegenerative disease, neoplasm, and HIV infectious disease.
- **Conclusion**: Established evidence identifies PSMD13 as a proteasome component and plausible connector between proteasomal degradation and less densely connected module genes. Its specific contribution to the shared kidney-testis pattern remains a hypothesis.

#### RAE1

- **Related proteins** (co-abundance neighbors): AIMP2 (0.81); STRING partners: SEH1L (0.964)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: huMAP3_12581.1
- **Function (MyGene.info)**: ribonucleic acid export 1. Mutations in the Schizosaccharomyces pombe Rae1 and Saccharomyces cerevisiae Gle2 genes have been shown to result in accumulation of poly(A)-containing mRNA in the nucleus, suggesting that the encoded proteins are involved in RNA export. The protein encoded by this gene is a homolog of yeast Rae1. It contains four WD40 motifs, and has been shown to localize to distinct foci in the nucleoplasm, to …
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); COVID-19 (0.370); Histiocytosis (0.370)
- **Europe PMC papers**: 1837
- **Why important**: RAE1 is testis-enhanced and cell-type-enhanced in early spermatids, late primary spermatocytes, and oocytes. It is annotated for RNA export, nucleocytoplasmic transport, and mitotic-spindle organization. It connects to AIMP2 in the module, has a strong STRING relationship with SEH1L, and belongs to hu.MAP complex (hu.MAP huMAP3_12581.1). It also has substantial literature support and associations with viral infectious disease, HIV infectious disease, orthomyxoviridae infectious disease, COVID-19, and histiocytosis.
- **Conclusion**: Established evidence supports RAE1 as an RNA-export and nuclear-transport factor with a relevant testis context. The co-abundance pattern supports participation in a shared transport or germ-cell program, but does not prove causality.

#### AIMP2

- **Related proteins** (co-abundance neighbors): SRPK1 (0.83), CHORDC1 (0.82), RAE1 (0.81), PSMD13 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aminoacyl tRNA synthetase complex interacting multifunctional protein 2. The protein encoded by this gene is part of the aminoacyl-tRNA synthetase complex, which contains nine different aminoacyl-tRNA synthetases and three non-enzymatic factors. The encoded protein is one of the non-enzymatic factors and is required for assembly and stability of the complex. [provided by RefSeq, May 2016].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 17 (0.617); hereditary disease (0.494); Neurodevelopmental abnormality (0.111); Parkinson disease (0.107); neoplasm (0.106)
- **Europe PMC papers**: 605
- **Why important**: AIMP2 is a highly connected bridge between SRPK1, CHORDC1, RAE1, and PSMD13. It is tissue-enhanced in skeletal muscle and cell-type-enhanced in late primary spermatocytes. It is a non-enzymatic aminoacyl-tRNA synthetase-complex factor required for complex assembly and stability, with annotations for tRNA aminoacylation and protein-containing complex assembly. Its disease associations include hypomyelinating leukodystrophy and neurodevelopmental abnormality.
- **Conclusion**: Established evidence supports AIMP2 as a translation-related complex factor and a plausible bridge between protein synthesis, RNA biology, and proteostasis. Its bridge role here is inferred from network position and co-abundance because no listed STRING or hu.MAP partner was supplied.

#### LZTFL1

- **Related proteins** (co-abundance neighbors): SEH1L (0.85), CCDC6 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: leucine zipper transcription factor like 1. This gene encodes a ubiquitously expressed protein that localizes to the cytoplasm. This protein interacts with Bardet-Biedl Syndrome (BBS) proteins and, through its interaction with BBS protein complexes, regulates protein trafficking to the ciliary membrane. Nonsense mutations in this gene cause a form of Bardet-Biedl Syndrome; a ciliopathy characterized in part by polydactyly, obesity, cognitiv…
- **Diseases (Open Targets)**: Bardet-Biedl syndrome (0.791); COVID-19 (0.493); respiratory failure (0.405); polydactyly (0.371); eye disorder (0.370)
- **Europe PMC papers**: 1015
- **Why important**: LZTFL1 connects SEH1L and CCDC6 and is cell-type-enhanced in late primary spermatocytes, ciliated epithelial populations, and thymocytes. It interacts with Bardet-Biedl syndrome proteins and regulates trafficking to the ciliary membrane. Its annotations include flagellated sperm motility and regulation of protein localization to the cilium. Nonsense mutations cause a form of Bardet-Biedl syndrome involving hypogonadism and kidney failure, making it particularly relevant to the tissue pair.
- **Conclusion**: Established evidence supports LZTFL1 as a ciliary-trafficking and reproductive or kidney-disease gene. Its placement in this module suggests a possible structural or trafficking link to the proteostasis and nuclear-transport program, but that link is currently hypothetical.

## Module 7

**Tissue pair**: kidney and testis  
**Genes (40)**: PRMT5, CCAR1, CPSF6, DDX5, DIAPH2, EIF2A, EML4, FKBP4, TUBGCP2, GYG1, HSPH1, KPNA2, IPO4, MSH2, MTA2, NAA15, NSF, NUP93, NUP98, PAK2, PPM1G, PPAT, SF3A1, SRP54, SUGP2, EPRS1, IARS1, KARS1, LARS1, MARS1, SYMPK, QARS1, RARS1, VARS1, YARS1, CCT5, CCT3, CCT7, CCT8, TTLL12

### Function

The module is best interpreted as a conserved intracellular gene-expression and protein-biosynthesis program, with a particularly strong aminoacyl-tRNA synthetase component. The primary evidence is the globally corrected enrichment for nucleic acid metabolism (GO:BP nucleic acid metabolic process; q_global = 5.18e-06), macromolecule biosynthesis (GO:BP macromolecule biosynthetic process; q_global = 4.18e-05), gene expression (GO:BP gene expression; q_global = 4.98e-05), aminoacyl-tRNA ligase activity (GO:MF aminoacyl-tRNA ligase activity; q_global = 6.39e-05), tRNA aminoacylation (GO:BP tRNA aminoacylation for protein translation; q_global = 6.39e-05), and aminoacyl-tRNA biosynthesis (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 6.39e-05). The synthetase genes form a coherent functional core, while DDX5, SF3A1, CPSF6, SYMPK, PRMT5, MTA2, NUP93, NUP98, KPNA2 and related genes support RNA processing, splicing, nuclear transport and gene regulation. The CCT subunits provide an additional chaperone component, supported by the chaperonin-containing T-complex enrichment (GO:CC chaperonin-containing T-complex; q_global = 0.00117) and ATP-dependent protein-folding chaperone enrichment (GO:MF ATP-dependent protein folding chaperone; q_global = 0.0148). The Cajal-body, telomerase, sperm-recognition and telomere-related terms (7 globally significant GO/KEGG terms, q_global 0.00117–0.00117; see the table), (6 globally significant GO/KEGG terms, q_global 0.00418–0.00418; see the table), (4 globally significant GO/KEGG terms, q_global 0.00998–0.00998; see the table) and (GO:BP sperm-egg recognition; q_global = 0.0191) (GO:BP regulation of DNA biosynthetic process; q_global = 0.0191) are driven mainly by the shared CCT subunits and should be treated as specific annotations of that submodule rather than as proof that the entire module is a dedicated telomere or fertilization complex. Overall, the most defensible interpretation is coordinated translational capacity, RNA maturation and nuclear organization, with protein folding and spermatogenic relevance layered onto a broadly expressed cellular program.

**Cell composition.** The module is not predominantly composed of plasma proteins or secreted proteins: HPA identifies only one secreted gene, and the proteins are generally intracellular. It is also not blood-cell dominated. The HPA summary reports low immune-cell specificity for almost all genes and no frequent enriched blood-cell category, although individual genes have cell-type annotations involving neutrophils or erythrocyte progenitors. Most genes have low tissue specificity, consistent with a broadly expressed housekeeping-like program. At the same time, a substantial subset is enhanced in spermatogenic cell types, especially late spermatids and primary spermatocytes, and several genes are tissue enhanced in testis. Protein detection is broadly concordant in kidney and testis, with a single gene not detected in each tissue. Thus, the shared module is unlikely to be explained primarily by plasma contamination or blood-cell admixture. Its conservation between kidney and testis may instead reflect ubiquitous biosynthetic and RNA-processing requirements, with a superimposed contribution from germ-cell composition in testis.

**GO/KEGG enrichment**: 64 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP nucleic acid metabolic process | 5.18e-06 | CCAR1, CCT3, CCT5, CCT7, CCT8, CPSF6, DDX5, EPRS1, FKBP4, IARS1, KARS1, KPNA2, LARS1, MARS1, MSH2, MTA2, NAA15, NUP98, PPM1G, PRMT5, QARS1, RARS1, SF3A1, SUGP2, SYMPK, VARS1, YARS1 |
| GO:CC aminoacyl-tRNA synthetase multienzyme complex | 1.15e-05 | EPRS1, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1 |
| GO:BP macromolecule biosynthetic process | 4.18e-05 | CCAR1, CCT3, CCT5, CCT7, CCT8, CPSF6, DDX5, EIF2A, EPRS1, FKBP4, GYG1, HSPH1, IARS1, KARS1, KPNA2, LARS1, MARS1, MSH2, MTA2, NAA15, NUP93, NUP98, PPM1G, PRMT5, QARS1, RARS1, SF3A1, SUGP2, SYMPK, VARS1, YARS1 |
| GO:BP gene expression | 4.98e-05 | CCAR1, CCT3, CCT5, CCT7, CCT8, CPSF6, DDX5, EIF2A, EPRS1, FKBP4, HSPH1, IARS1, KARS1, KPNA2, LARS1, MARS1, MSH2, MTA2, NAA15, NUP93, NUP98, PPM1G, PRMT5, QARS1, RARS1, SF3A1, SUGP2, SYMPK, VARS1, YARS1 |
| GO:MF aminoacyl-tRNA ligase activity | 6.39e-05 | EPRS1, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1, YARS1 |
| GO:BP tRNA aminoacylation for protein translation | 6.39e-05 | EPRS1, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1, YARS1 |
| GO:MF ligase activity, forming carbon-oxygen bonds | 6.39e-05 | EPRS1, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1, YARS1 |
| GO:BP amino acid activation | 6.39e-05 | EPRS1, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1, YARS1 |
| GO:BP tRNA aminoacylation | 6.39e-05 | EPRS1, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1, YARS1 |
| KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human) | 6.39e-05 | EPRS1, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1, YARS1 |
| GO:MF catalytic activity, acting on a tRNA | 0.000338 | EPRS1, IARS1, KARS1, LARS1, MARS1, QARS1, RARS1, VARS1, YARS1 |
| GO:MF ATP binding | 0.000547 | CCT3, CCT5, CCT7, CCT8, DDX5, EPRS1, FKBP4, HSPH1, IARS1, KARS1, LARS1, MARS1, MSH2, NSF, PAK2, QARS1, RARS1, TTLL12, VARS1, YARS1 |
| GO:MF adenyl ribonucleotide binding | 0.000608 | CCT3, CCT5, CCT7, CCT8, DDX5, EPRS1, FKBP4, HSPH1, IARS1, KARS1, LARS1, MARS1, MSH2, NSF, PAK2, QARS1, RARS1, TTLL12, VARS1, YARS1 |
| GO:BP macromolecule metabolic process | 0.000659 | CCAR1, CCT3, CCT5, CCT7, CCT8, CPSF6, DDX5, EIF2A, EPRS1, FKBP4, GYG1, HSPH1, IARS1, KARS1, KPNA2, LARS1, MARS1, MSH2, MTA2, NAA15, NSF, NUP93, NUP98, PAK2, PPM1G, PRMT5, QARS1, RARS1, SF3A1, SUGP2, SYMPK, TTLL12, VARS1, YARS1 |
| GO:CC membraneless organelle | 0.000831 | CCT3, CCT5, CCT7, CCT8, CPSF6, DDX5, DIAPH2, EIF2A, EML4, FKBP4, HSPH1, IPO4, LARS1, MARS1, MSH2, MTA2, NAA15, NSF, NUP93, NUP98, PAK2, PRMT5, RARS1, SF3A1, SRP54, SUGP2, SYMPK, TTLL12, TUBGCP2, YARS1 |

### STRING and hu.MAP

STRING directly supports two major known assemblies. The aminoacyl-tRNA synthetases show a dense set of high-confidence relationships and are enriched for cytosolic tRNA aminoacylation and the aminoacyl-tRNA synthetase multienzyme complex (6 supplementary STRING terms; within-query FDR 1.51e-05–0.0001). The CCT subunits CCT3, CCT5, CCT7 and CCT8 are mutually strongly connected, consistent with the CCT chaperonin. Additional STRING-supported relationships include CPSF6 with SYMPK, NUP93 with NUP98, and CCAR1 with DDX5. hu.MAP independently supports the aminoacyl-tRNA synthetase assemblies (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), the CCT-containing complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), the VARS1–TTLL12 associations (hu.MAP huMAP3_08052.1) (hu.MAP huMAP3_00469.1) (hu.MAP huMAP3_12041.1), the SF3A1–CCAR1 complexes (hu.MAP huMAP3_10359.1), nuclear pore assemblies containing KPNA2 and NUP98 (hu.MAP huMAP3_10000.1) (hu.MAP huMAP3_12581.1), and spliceosomal complexes containing PRMT5 and SF3A1 (hu.MAP huMAP3_06511.1) (hu.MAP huMAP3_08980.1). These results show that the network is not an unexplained set of isolated correlations: much of its structure recapitulates known molecular assemblies. The co-abundance module nevertheless joins several assemblies and functional processes rather than corresponding to a single established physical complex.

**STRING interactions (score >= 0.7)**: 45 of 780 gene pairs: CCAR1–DDX5 (0.836); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999); CPSF6–SYMPK (0.963); EPRS1–IARS1 (0.999); EPRS1–KARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–MARS1 (0.999); EPRS1–QARS1 (0.999); EPRS1–RARS1 (0.999); EPRS1–VARS1 (0.97); EPRS1–YARS1 (0.999); IARS1–KARS1 (0.999); IARS1–LARS1 (0.999); IARS1–MARS1 (0.999); IARS1–QARS1 (0.999); IARS1–RARS1 (0.999); IARS1–VARS1 (0.9); IARS1–YARS1 (0.966); KARS1–LARS1 (0.999); KARS1–MARS1 (0.999); KARS1–QARS1 (0.999); KARS1–RARS1 (0.999); KARS1–VARS1 (0.978); KARS1–YARS1 (0.988); LARS1–MARS1 (0.999); LARS1–QARS1 (0.999); LARS1–RARS1 (0.999); LARS1–VARS1 (0.968); LARS1–YARS1 (0.98); MARS1–QARS1 (0.999); MARS1–RARS1 (0.999); MARS1–VARS1 (0.902); MARS1–YARS1 (0.999); NUP93–NUP98 (0.999); QARS1–RARS1 (0.999); QARS1–VARS1 (0.91); QARS1–YARS1 (0.959); RARS1–VARS1 (0.905); RARS1–YARS1 (0.942); VARS1–YARS1 (0.956)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Cytosolic tRNA aminoacylation (FDR = 1.51e-05, 9 genes); KEGG Aminoacyl-tRNA biosynthesis (FDR = 2.64e-05, 9 genes); Keyword Aminoacyl-tRNA synthetase (FDR = 3.7e-05, 9 genes); Component aminoacyl-tRNA synthetase multienzyme complex (FDR = 5.19e-05, 7 genes); COMPARTMENTS aminoacyl-tRNA synthetase multienzyme complex (FDR = 8.45e-05, 7 genes); Function aminoacyl-tRNA ligase activity (FDR = 0.0001, 9 genes); Function ATP binding (FDR = 0.0001, 20 genes); Keyword ATP-binding (FDR = 0.00013, 19 genes); Keyword Protein biosynthesis (FDR = 0.00013, 10 genes); InterPro Aminoacyl-tRNA synthetase, class I, conserved site (FDR = 0.00019, 7 genes); InterPro Rossmann-like alpha/beta/alpha sandwich fold (FDR = 0.0002, 8 genes); NetworkNeighborAL tRNA Aminoacylation, and glutamyl-tRNA(Gln) amidotransferase complex (FDR = 0.0002, 9 genes); Function Nucleic acid binding (FDR = 0.00021, 22 genes); NetworkNeighborAL tRNA Aminoacylation (FDR = 0.00037, 8 genes); Function Heterocyclic compound binding (FDR = 0.00039, 31 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, IARS1, QARS1, RARS1, MARS1, KARS1, LARS1; 7/14); huMAP3_13688.1 (EPRS1, IARS1, QARS1, RARS1, MARS1, KARS1, LARS1; 7/14); huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_08052.1 (VARS1, TTLL12; 2/10); huMAP3_00469.1 (VARS1, TTLL12; 2/12); huMAP3_12041.1 (VARS1, TTLL12; 2/16); huMAP3_10359.1 (SF3A1, CCAR1; 2/27); huMAP3_10000.1 (KPNA2, NUP98; 2/44); huMAP3_12581.1 (KPNA2, NUP98; 2/58); huMAP3_06511.1 (PRMT5, SF3A1; 2/79); huMAP3_08980.1 (PRMT5, SF3A1; 2/97)

### Novelty

The exact tissue-pair co-abundance observation may be a useful systems-level finding, but the module should not be described as a newly discovered molecular complex. Its central components are already well established in STRING, hu.MAP, GO and gene-specific literature, particularly the aminoacyl-tRNA synthetase complex and the CCT chaperonin. Conversely, missing STRING or hu.MAP coverage for several peripheral genes does not demonstrate novelty. The strongest cautious claim is that this analysis identifies a conserved kidney–testis co-abundance configuration that combines known translation, RNA-processing, nuclear-transport and chaperone assemblies, with a possible germ-cell-associated context. Establishing genuine novelty would require comparison with previously published kidney–testis co-abundance modules, independent cohorts, preservation statistics, and experiments showing coordinated regulation or physical cooperation beyond the known complexes.

**Hypothesis.** Hypothesis: the module represents a shared cellular proteostasis and gene-expression state that supports high-throughput production of correctly processed proteins. In this model, the aminoacyl-tRNA synthetase core maintains charging of diverse tRNAs and translational fidelity, DDX5, SF3A1, CPSF6, SYMPK and PRMT5 coordinate RNA processing and maturation, KPNA2 and the nucleoporins regulate exchange between nucleus and cytoplasm, and the CCT subunits together with HSPH1 and FKBP4 buffer folding stress. In testis, this general program may be recruited or amplified during spermatogenic differentiation, while in kidney it may reflect the biosynthetic demands of differentiated epithelial cells. The co-abundance pattern does not by itself prove direct regulation among these components; it predicts that perturbing translational charging or RNA processing should alter the abundance or activity of the chaperone and nuclear-trafficking components in relevant kidney and germ-cell models.

### Important genes

#### KARS1

- **Related proteins** (co-abundance neighbors): CCT7 (0.91), DDX5 (0.89), CCT8 (0.88), SF3A1 (0.86), RARS1 (0.85), CCT3 (0.84), VARS1 (0.83), QARS1 (0.82); STRING partners: EPRS1 (0.999), IARS1 (0.999), LARS1 (0.999), MARS1 (0.999), QARS1 (0.999), RARS1 (0.999), VARS1 (0.978), YARS1 (0.988)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: lysyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. Lysyl-tRNA synthetase is a homodimer localized to the cytoplasm which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Alternatively spliced transcript variants encoding different…
- **Diseases (Open Targets)**: leukoencephalopathy, progressive, infantile-onset, with or without deafness (0.753); deafness, congenital, and adult-onset progressive leukoencephalopathy (0.714); autosomal recessive nonsyndromic hearing loss 89 (0.685); Charcot-Marie-Tooth disease recessive intermediate B (0.670); deafness (0.534)
- **Europe PMC papers**: 232
- **Why important**: KARS1 is a central network connector among the CCT subunits and the synthetase cluster. It is part of the aminoacyl-tRNA synthetase multienzyme complex supported by (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 1.15e-05), (GO:MF aminoacyl-tRNA ligase activity; q_global = 6.39e-05), (GO:BP tRNA aminoacylation for protein translation; q_global = 6.39e-05), (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 6.39e-05) and (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), and its established function is lysine charging of tRNA for protein translation. HPA places it in late primary spermatocytes and late spermatids while also detecting it in kidney and testis. Its disease associations include inherited neurological and hearing-related disorders, making translational fidelity biologically consequential. Its literature volume is more limited than that of some broad RNA regulators, but its direct enzymatic role and network position make it an important module anchor.
- **Conclusion**: Established evidence supports KARS1 as a core translational enzyme and a member of a known multisynthetase assembly. Its co-abundance with the other synthetases is therefore readily explained by coordinated translation capacity. A testis-specific regulatory role or a direct functional connection to the CCT submodule remains a hypothesis, not an established conclusion from this module.

#### CCT8

- **Related proteins** (co-abundance neighbors): CCT7 (0.95), KARS1 (0.88), KPNA2 (0.85), RARS1 (0.85), MTA2 (0.85), FKBP4 (0.84), CCT3 (0.83), CCT5 (0.83), PRMT5 (0.81), TTLL12 (0.80); STRING partners: CCT3 (0.999), CCT5 (0.999), CCT7 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is one of the most connected genes in the module and belongs to the tightly connected CCT3–CCT5–CCT7–CCT8 group. STRING and hu.MAP strongly support this chaperonin assembly, while (GO:CC chaperonin-containing T-complex; q_global = 0.00117) and (GO:MF ATP-dependent protein folding chaperone; q_global = 0.0148) support chaperonin and ATP-dependent protein folding functions. Its annotations include protein folding and regulation of Cajal-body and telomerase-related localization, and HPA detects it in kidney and testis with cell-type enhancement in oocytes. The gene therefore links a known protein-folding machine to the nuclear-body and reproductive annotations appearing in the enrichment results.
- **Conclusion**: Established evidence supports CCT8 as a subunit of the CCT chaperonin and as a plausible marker of folding demand. The module does not establish that CCT8 independently drives telomerase regulation, sperm recognition or the shared kidney–testis phenotype; those are annotations associated with the CCT submodule and should remain mechanistic hypotheses.

#### DDX5

- **Related proteins** (co-abundance neighbors): CCT3 (0.89), CCT5 (0.89), KARS1 (0.89), CCAR1 (0.86), YARS1 (0.85), FKBP4 (0.85), PPAT (0.84), RARS1 (0.83), EPRS1 (0.82), SYMPK (0.81), NUP93 (0.80); STRING partners: CCAR1 (0.836)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 has the strongest network position in the supplied ranking and connects the CCT group, synthetase genes, CCAR1, FKBP4 and PPAT. It is a DEAD-box RNA helicase involved in RNA-structure remodeling, transcriptional co-regulation, splicing and small noncoding RNA processing. It is repeatedly represented in the primary enrichment for nucleic acid metabolism, gene expression, RNA metabolism and RNA catalysis, including (GO:BP nucleic acid metabolic process; q_global = 5.18e-06), (GO:BP gene expression; q_global = 4.98e-05), (GO:BP RNA metabolic process; q_global = 0.0024) and (GO:MF catalytic activity, acting on RNA; q_global = 0.00867). STRING supports its relationship with CCAR1, and its extensive literature base makes it a well-studied integrative RNA regulator.
- **Conclusion**: Established evidence supports DDX5 as a plausible bridge between the module's RNA-processing and biosynthetic components. The network suggests coordination between DDX5 and translation or chaperone capacity, but it does not prove that DDX5 is the upstream organizer of the module or that its disease associations explain the kidney–testis conservation.

#### SF3A1

- **Related proteins** (co-abundance neighbors): HSPH1 (0.87), CCT7 (0.86), FKBP4 (0.86), KARS1 (0.86), NUP93 (0.84), IPO4 (0.84), QARS1 (0.83), DIAPH2 (0.81), CCAR1 (0.81), RARS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_10359.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 is highly connected to HSPH1, FKBP4, CCT7, KARS1, NUP93, IPO4 and QARS1. It is a core component of the U2 snRNP and is annotated for spliceosome assembly and pre-mRNA splicing. The primary enrichment includes RNA processing, nuclear bodies, nucleoplasm and RNA binding (GO:BP RNA metabolic process; q_global = 0.0024), (GO:CC nuclear body; q_global = 0.00387), (GO:CC nuclear lumen; q_global = 0.0047) and (GO:MF RNA binding; q_global = 0.00521). hu.MAP supports its participation in complexes with CCAR1 and PRMT5 (hu.MAP huMAP3_10359.1), (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1). HPA shows enhancement in late spermatids and neutrophils, while the gene has substantial disease and literature coverage.
- **Conclusion**: Established evidence supports SF3A1 as a spliceosomal and nuclear RNA-processing component that plausibly explains part of the module's nuclear organization signal. Its co-abundance with translation and chaperone genes may reflect coordinated expression in biosynthetically active cells, but a direct SF3A1-mediated coupling between splicing and tRNA charging remains a hypothesis.

#### RARS1

- **Related proteins** (co-abundance neighbors): CCT7 (0.89), CCT8 (0.85), KARS1 (0.85), FKBP4 (0.84), DDX5 (0.83), CCT3 (0.81), QARS1 (0.80), SF3A1 (0.80); STRING partners: EPRS1 (0.999), IARS1 (0.999), KARS1 (0.999), LARS1 (0.999), MARS1 (0.999), QARS1 (0.999), VARS1 (0.905), YARS1 (0.942)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: arginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Arginyl-tRNA synthetase belongs to the class-I aminoacyl-tRNA synthetase family. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 9 (0.753); POLR-related leukodystrophy (0.554); hereditary disease (0.470); leukodystrophy (0.271); Abnormality of the skeletal system (0.094)
- **Europe PMC papers**: 168
- **Why important**: RARS1 is embedded in the densely connected synthetase cluster and participates in the high-confidence STRING and hu.MAP assemblies (6 supplementary STRING terms; within-query FDR 1.51e-05–0.0001) and (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). It catalyzes arginine-tRNA charging and is represented across the primary aminoacylation and translation terms, including (GO:CC aminoacyl-tRNA synthetase multienzyme complex; q_global = 1.15e-05), (GO:MF aminoacyl-tRNA ligase activity; q_global = 6.39e-05), (GO:BP tRNA aminoacylation for protein translation; q_global = 6.39e-05) and (KEGG Aminoacyl-tRNA biosynthesis - Homo sapiens (human); q_global = 6.39e-05). It connects to CCT subunits, FKBP4, DDX5 and SF3A1 in the co-abundance network. Its established disease associations with leukodystrophy emphasize the importance of accurate translation, and its literature base is substantial for a synthetase gene.
- **Conclusion**: Established evidence supports RARS1 as a core member of the module's aminoacylation machinery and as a strong marker of the translational program. The network does not show that RARS1 has a special kidney–testis-specific function beyond coordinated expression of a broadly required enzyme, although germ-cell enrichment could motivate targeted testing.

#### KPNA2

- **Related proteins** (co-abundance neighbors): CCT8 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_10000.1, huMAP3_12581.1
- **Function (MyGene.info)**: karyopherin subunit alpha 2. The import of proteins into the nucleus is a process that involves at least 2 steps. The first is an energy-independent docking of the protein to the nuclear envelope and the second is an energy-dependent translocation through the nuclear pore complex. Imported proteins require a nuclear localization sequence (NLS) which generally consists of a short region of basic amino acids or 2 such regions s…
- **Diseases (Open Targets)**: severe acute respiratory syndrome (0.462); Orthomyxoviridae infectious disease (0.462); dengue disease (0.462); COVID-19 (0.373); non-alcoholic fatty liver (0.324)
- **Europe PMC papers**: 2442
- **Why important**: KPNA2 provides a nuclear-import axis that complements the RNA-processing and nucleoporin components. It is connected to CCT8 and appears in primary terms for nuclear localization, nucleoplasm and nucleic-acid-related processes, including (GO:CC nuclear lumen; q_global = 0.0047), (GO:CC nucleoplasm; q_global = 0.0224) and (GO:BP protein localization to nucleus; q_global = 0.0356). hu.MAP places KPNA2 with NUP98 in nuclear-pore and transport complexes (hu.MAP huMAP3_10000.1) (hu.MAP huMAP3_12581.1). HPA reports testis tissue enhancement and enrichment across spermatogenic cell types while detecting the protein in kidney and testis. Its disease and infection associations also reflect the importance of nuclear transport.
- **Conclusion**: Established evidence supports KPNA2 as a nuclear import receptor and as part of a known transport context with NUP98. Its testis enhancement makes it a useful candidate for the shared-tissue interpretation, but the module does not establish that KPNA2 specifically links nuclear import to the synthetase or CCT assemblies.

## Module 8

**Tissue pair**: kidney and testis  
**Genes (6)**: ARPC1B, OLA1, SEPTIN2, SERPINH1, SMS, VIM

### Function

The module most plausibly reflects a shared cellular-architecture and remodeling program rather than a narrowly defined pathway. SEPTIN2, ARPC1B, and VIM are established cytoskeletal components: SEPTIN2 is associated with septin complexes, cilium assembly, cell division, and cytoskeletal organization; ARPC1B is a subunit of the Arp2/3 actin-nucleation complex; and VIM is an intermediate-filament protein involved in cell shape, integrity, attachment, migration, and signaling. SERPINH1 adds endoplasmic-reticulum protein folding and collagen-specific chaperone activity, while OLA1 contributes ATPase-related cellular regulation and SMS contributes polyamine biosynthesis. Thus, the most defensible interpretation is coordinated abundance of proteins involved in cytoskeletal organization, structural maintenance, protein handling, and cellular state regulation. No GO or KEGG term passed global correction, so this interpretation is based on the individual gene annotations and network pattern rather than statistically significant pathway enrichment. The absence of a globally enriched term does not invalidate the module.

**Cell composition.** The module is not dominated by plasma or classically secreted proteins. SERPINH1 is annotated as intracellular and membrane-associated rather than as a freely secreted plasma protein, and the remaining genes are non-secreted intracellular proteins. HPA shows low immune-cell specificity for every member and no enriched blood-cell category, arguing against a straightforward blood-cell contamination explanation. Most members have low tissue specificity, while ARPC1B and VIM show tissue enhancement in lymphoid tissue and blood vessel, respectively. Several genes show enhancement in stromal, trophoblast, hepatic, Leydig, epithelial, or oocyte-related cell types, indicating that shared cell populations or broadly used structural programs could contribute to the kidney–testis co-abundance pattern. All members are detected at the protein level in both kidney and testis, supporting technical and biological plausibility of their presence in both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The module has no high-confidence STRING interaction among its member pairs and no hu.MAP complex containing multiple module members. Therefore, the co-abundance edges are not corroborated here as established physical interactions or as membership in a known multiprotein complex. Nevertheless, several individual annotations describe established cellular machinery: ARPC1B belongs to the Arp2/3 complex, SEPTIN2 belongs to a septin complex, VIM forms intermediate filaments, SERPINH1 functions as a collagen-specific endoplasmic-reticulum chaperone, and SMS catalyzes spermine production. The module therefore may combine proteins that participate in related cellular states without forming one physical complex. The absence of STRING or hu.MAP support should be treated as lack of corroboration, not evidence that the co-abundance relationship is biologically false.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The co-abundance configuration appears potentially novel as a cross-tissue network observation because it is not represented by a high-confidence STRING interaction set or a hu.MAP complex shared by module members. However, that absence alone cannot establish a new biological mechanism. The genes have substantial prior annotation and literature, and their known functions are heterogeneous rather than defining an unrecognized canonical complex. A cautious conclusion is that the kidney–testis co-abundance association is a candidate novel systems-level observation, while the underlying biology remains to be validated by independent cohorts, cell-composition adjustment, perturbation, or orthogonal protein measurements.

**Hypothesis.** Hypothesis: the module captures a shared structural-remodeling state present in selected kidney and testis cell populations. Cytoskeletal organization by SEPTIN2, ARPC1B, and VIM could accompany changes in cell shape, adhesion, migration, ciliary or membrane-associated organization, and intracellular trafficking. SERPINH1 could support collagen handling and extracellular-matrix-related stress responses, while OLA1 and SMS could help reflect accompanying metabolic and proteostatic demands. The coordinated signal may therefore arise from a common cellular state or shared stromal, vascular, epithelial, or specialized reproductive cell populations rather than from a single physical complex. This hypothesis is not established by the enrichment results, because no GO or KEGG term passed global correction and neither STRING nor hu.MAP supplied complex-level support.

### Important genes

#### SEPTIN2

- **Related proteins** (co-abundance neighbors): ARPC1B (0.88), OLA1 (0.84), SMS (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Actin filaments; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: septin 2. Enables identical protein binding activity. Predicted to be involved in several processes, including cilium assembly; regulation of exocytosis; and smoothened signaling pathway. Predicted to act upstream of or within regulation of L-glutamate import across plasma membrane and regulation of protein localization. Located in several cellular components, including cytoskeleton; photoreceptor connectin…
- **Diseases (Open Targets)**: hypothyroidism (0.239); squamous cell carcinoma (0.201); ischemic stroke (0.189); coronary artery disorder (0.181); skin cancer (0.181)
- **Europe PMC papers**: 281
- **Why important**: SEPTIN2 has the strongest network connectivity in the module and links the cytoskeletal branch to OLA1 and SMS while also connecting to ARPC1B. Its established association with septin complexes, cytoskeleton organization, cilium assembly, cytokinesis, and sperm-annulus biology makes it a plausible structural anchor. It also has a substantial literature and multiple disease associations, although those associations do not by themselves explain this module.
- **Conclusion**: Established evidence supports SEPTIN2 as a cytoskeletal and cellular-organization component and as a central connector in this module. It is a strong candidate for an organizing role, but a direct mechanistic role in the kidney–testis shared signal remains a hypothesis.

#### ARPC1B

- **Related proteins** (co-abundance neighbors): SEPTIN2 (0.88), VIM (0.82), SERPINH1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: actin related protein 2/3 complex subunit 1B. This gene encodes one of seven subunits of the human Arp2/3 protein complex. This subunit is a member of the SOP2 family of proteins and is most similar to the protein encoded by gene ARPC1A. The similarity between these two proteins suggests that they both may function as p41 subunit of the human Arp2/3 complex that has been implicated in the control of actin polymerization in cells. It is possib…
- **Diseases (Open Targets)**: platelet abnormalities with eosinophilia and immune-mediated inflammatory disease (0.771); combined immunodeficiency (0.429); autoimmune disorder of central nervous system (0.397); cutaneous leishmaniasis (0.370); immunodeficiency disease (0.346)
- **Europe PMC papers**: 1334
- **Why important**: ARPC1B is highly connected and bridges SEPTIN2, VIM, and SERPINH1, linking actin organization with intermediate-filament and protein-folding-related components. Its established role as an Arp2/3-complex subunit gives the module a concrete actin-polymerization mechanism. It also has extensive disease literature involving immune and platelet abnormalities, while HPA shows enhancement in several immune-associated and trophoblast-related cell types.
- **Conclusion**: Established evidence supports ARPC1B as an actin-nucleation component with important cell-structural and disease relevance. Its position makes it a plausible network bridge, but the module does not establish that immune biology is the driver in kidney or testis.

#### VIM

- **Related proteins** (co-abundance neighbors): ARPC1B (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vimentin. This gene encodes a type III intermediate filament protein. Intermediate filaments, along with microtubules and actin microfilaments, make up the cytoskeleton. The encoded protein is responsible for maintaining cell shape and integrity of the cytoplasm, and stabilizing cytoskeletal interactions. This protein is involved in neuritogenesis and cholesterol transport and functions as an organizer of a…
- **Diseases (Open Targets)**: dengue disease (0.516); early-onset non-syndromic cataract (0.462); early-onset partial cataract (0.458); Developmental cataract (0.435); cataract (0.372)
- **Europe PMC papers**: 86568
- **Why important**: VIM connects to ARPC1B and represents the intermediate-filament arm of the module. It is broadly studied and established as a regulator of cell shape, cytoplasmic integrity, attachment, migration, signaling, and interactions among cytoskeletal systems. HPA shows enhancement in blood vessel and in stromal, hepatic, and Leydig-related cell types, making it relevant to possible structural or cellular-composition explanations.
- **Conclusion**: Established evidence supports VIM as a broad structural and remodeling marker. Its presence is compatible with a shared cytoskeletal state, but because VIM is broadly expressed, it cannot alone demonstrate a kidney–testis-specific mechanism.

#### SERPINH1

- **Related proteins** (co-abundance neighbors): ARPC1B (0.82), OLA1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family H member 1. This gene encodes a member of the serpin superfamily of serine proteinase inhibitors. The encoded protein is localized to the endoplasmic reticulum and plays a role in collagen biosynthesis as a collagen-specific molecular chaperone. Autoantibodies to the encoded protein have been found in patients with rheumatoid arthritis. Expression of this gene may be a marker for cancer, and nucleotide polymo…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 10 (0.714); preterm premature rupture of the membranes (0.559); coronary artery disorder (0.554); myocardial infarction (0.510); Abnormality of the skeletal system (0.474)
- **Europe PMC papers**: 2762
- **Why important**: SERPINH1 connects ARPC1B and OLA1 and contributes a distinct endoplasmic-reticulum and extracellular-matrix-related dimension. Its established function as a collagen-specific molecular chaperone links the module to protein folding and collagen fibril organization. It has extensive literature and disease associations involving skeletal, cardiovascular, and pregnancy-related phenotypes, and HPA shows enhancement in stromal, trophoblast, and epididymal cell types.
- **Conclusion**: Established evidence supports SERPINH1 as a collagen-processing and proteostasis component. Its co-abundance with cytoskeletal genes may indicate coordinated matrix-associated remodeling, but that interpretation remains a hypothesis rather than demonstrated pathway membership.

#### SMS

- **Related proteins** (co-abundance neighbors): SEPTIN2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: spermine synthase. This gene encodes a protein belonging to the spermidine/spermin synthase family and catalyzes the production of spermine from spermidine. Pseudogenes of this gene are located on chromosomes 1, 5, 6 and X. Mutations in this gene cause an X-linked intellectual disability called Snyder-Robinson Syndrome (SRS). Multiple transcript variants encoding different isoforms have been found for this gene. [pr…
- **Diseases (Open Targets)**: syndromic X-linked intellectual disability Snyder type (0.814); hereditary disease (0.484); Intellectual disability (0.337); autoimmune disorder of central nervous system (0.336); neurodegenerative disease (0.331)
- **Europe PMC papers**: 14362
- **Why important**: SMS provides the clearest metabolic specialization in the module by catalyzing spermine production from spermidine. It has an extensive literature and an established connection to Snyder-Robinson syndrome. Its network connection to SEPTIN2 and HPA enhancement in reproductive and endometrial-related cell types make it relevant to a possible specialized cellular-state interpretation.
- **Conclusion**: Established evidence supports SMS as a polyamine-metabolism enzyme with important human disease relevance. Its inclusion suggests that polyamine state may accompany the structural program, but the module does not establish that SMS regulates the cytoskeletal or tissue-sharing signal.

## Module 9

**Tissue pair**: kidney and testis  
**Genes (23)**: ASCC3, CIAO1, CPSF2, DBNL, DYNC1I2, EXOC8, GYS1, HNRNPH1, HNRNPF, HNRNPL, LMNB1, LMNB2, METAP1, MATR3, MOV10, NHLRC2, ADSS2, CAD, SNX6, TIPRL, SNRNP200, EFTUD2, UMPS

### Function

The strongest functional interpretation is nuclear pre-mRNA processing, especially catalytic spliceosome activity. The globally corrected GO evidence is (GO:CC catalytic step 2 spliceosome; q_global = 0.0411), supported by EFTUD2, HNRNPF, HNRNPH1, and SNRNP200. Their annotations describe spliceosomal assembly, conformational remodeling, RNA processing, and regulation of alternative splicing. The network also contains a coherent hnRNP and RNA-binding subnetwork involving HNRNPH1, HNRNPF, HNRNPL, MATR3, and MOV10. Additional edges connect this RNA-processing core to nuclear lamins, vesicle trafficking, nucleotide metabolism, and cytoskeletal transport, but these peripheral themes are not globally enriched GO/KEGG findings. No STRING functional-enrichment term was reported. Thus, the module is best interpreted as a conserved RNA-processing module with connected nuclear-structural and cellular-maintenance components, rather than as a single pathway spanning every gene.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are predominantly intracellular or nuclear. Most genes have low tissue specificity, consistent with broadly expressed housekeeping or core-cellular machinery. Protein detection in both kidney and testis is widespread across the module, so the shared signal is unlikely to be explained simply by a kidney-specific or testis-specific secreted product. HPA shows low immune-cell specificity for nearly all genes and no frequent enriched blood-cell category, arguing against a straightforward blood contamination explanation. Some genes show cell-type enhancement in spermatids, progenitors, glial or epithelial populations, and other specialized cells, but these annotations are heterogeneous. The shared module may therefore reflect ubiquitous RNA and nuclear functions that are active in both tissues, with possible contributions from shared proliferative or differentiating cell states.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC catalytic step 2 spliceosome | 0.0411 | EFTUD2, HNRNPF, HNRNPH1, SNRNP200 |

### STRING and hu.MAP

STRING provides several well-supported known relationships. EFTUD2 and SNRNP200 form a particularly strong spliceosomal pair, while HNRNPH1, HNRNPF, HNRNPL, and MATR3 form a connected hnRNP or RNA-processing neighborhood. LMNB1 and LMNB2 form a lamin pair, and ADSS2, CAD, and UMPS form a nucleotide-metabolism neighborhood. MATR3 is also linked to MOV10, connecting nuclear RNA handling to post-transcriptional regulation. hu.MAP independently supports these interpretations: EFTUD2 with SNRNP200 repeatedly occurs in spliceosomal complexes (hu.MAP huMAP3_00960.1), (hu.MAP huMAP3_07622.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), (hu.MAP huMAP3_09945.1), (hu.MAP huMAP3_08980.1); HNRNPH1 with HNRNPF occurs in hnRNP-associated complexes (hu.MAP huMAP3_07055.1), (hu.MAP huMAP3_06054.1), (hu.MAP huMAP3_11034.1), (hu.MAP huMAP3_13511.1), (hu.MAP huMAP3_14523.1); HNRNPL with MATR3 occurs in larger RNA-binding assemblies (hu.MAP huMAP3_05721.1), (hu.MAP huMAP3_07581.1), (hu.MAP huMAP3_10625.1); and LMNB1 with LMNB2 occurs in nuclear-lamina assemblies (hu.MAP huMAP3_03501.1), (hu.MAP huMAP3_00325.1), (hu.MAP huMAP3_13519.1), (hu.MAP huMAP3_10433.1), (hu.MAP huMAP3_09259.1), (hu.MAP huMAP3_10492.1), (hu.MAP huMAP3_10614.1). These databases therefore show that important parts of the module recapitulate established physical or complex-level biology. They do not, by themselves, demonstrate that the entire co-abundance module is one physical complex or one biochemical pathway.

**STRING interactions (score >= 0.7)**: 12 of 253 gene pairs: ADSS2–CAD (0.963); ADSS2–UMPS (0.715); CAD–UMPS (0.946); EFTUD2–SNRNP200 (0.999); HNRNPF–HNRNPH1 (0.994); HNRNPF–HNRNPL (0.95); HNRNPF–MATR3 (0.766); HNRNPH1–HNRNPL (0.982); HNRNPH1–MATR3 (0.911); HNRNPL–MATR3 (0.757); LMNB1–LMNB2 (0.999); MATR3–MOV10 (0.722)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03501.1 (LMNB1, LMNB2; 2/2); huMAP3_07055.1 (HNRNPH1, HNRNPF; 2/3); huMAP3_00325.1 (LMNB1, LMNB2; 2/3); huMAP3_06054.1 (HNRNPH1, HNRNPF; 2/4); huMAP3_13519.1 (LMNB1, LMNB2; 2/4); huMAP3_11034.1 (HNRNPH1, HNRNPF; 2/5); huMAP3_10433.1 (LMNB1, LMNB2; 2/5); huMAP3_05721.1 (HNRNPL, MATR3; 2/6); huMAP3_09259.1 (LMNB1, LMNB2; 2/8); huMAP3_00960.1 (SNRNP200, EFTUD2; 2/8); huMAP3_13511.1 (HNRNPH1, HNRNPF; 2/9); huMAP3_10492.1 (LMNB1, LMNB2; 2/9); huMAP3_10614.1 (LMNB1, LMNB2; 2/9); huMAP3_07622.1 (SNRNP200, EFTUD2; 2/9); huMAP3_07581.1 (HNRNPL, MATR3; 2/21); huMAP3_09042.1 (CIAO1, UMPS; 2/26); huMAP3_06975.1 (MATR3, MOV10; 2/31); huMAP3_14523.1 (HNRNPH1, HNRNPF; 2/33); huMAP3_08501.1 (SNRNP200, EFTUD2; 2/47); huMAP3_09504.1 (SNRNP200, EFTUD2; 2/51); huMAP3_10625.1 (HNRNPL, MATR3; 2/57); huMAP3_09945.1 (SNRNP200, EFTUD2; 2/61); huMAP3_08980.1 (SNRNP200, EFTUD2; 2/97)

### Novelty

The biological ingredients are not individually novel: the spliceosomal, hnRNP, lamin, and nucleotide-metabolism relationships are already represented in STRING and hu.MAP. The potentially new observation is their coordinated co-abundance across kidney and testis, particularly the connection between the spliceosome-centered core and peripheral trafficking, nuclear-envelope, transport, and metabolic genes. However, the fact sheet does not establish that this exact module has been reported previously, and absence from STRING or hu.MAP would not prove novelty. The cautious conclusion is that this is a potentially novel cross-tissue co-abundance organization built largely from established molecular machinery, requiring replication in independent cohorts and testing against cell composition, tissue state, and technical effects before being called a new biological mechanism.

**Hypothesis.** Hypothesis: the module represents a shared demand for coordinated RNA maturation and nuclear organization in kidney and testis cells. A spliceosomal core containing EFTUD2, SNRNP200, HNRNPH1, and HNRNPF may coordinate transcript processing, while HNRNPL and MATR3 help organize RNA-associated nuclear assemblies. LMNB1 and LMNB2 may couple this RNA-processing state to nuclear-envelope structure, and EXOC8, DYNC1I2, SNX6, and DBNL may connect it to intracellular trafficking. CAD, UMPS, and ADSS2 may reflect the nucleotide supply needed for transcription and RNA metabolism. This is a mechanistic hypothesis rather than a demonstrated interaction among all module members; the co-abundance data alone cannot establish directionality or physical coupling.

### Important genes

#### HNRNPH1

- **Related proteins** (co-abundance neighbors): TIPRL (0.84), HNRNPF (0.83), SNX6 (0.83), EXOC8 (0.83), SNRNP200 (0.82), ADSS2 (0.81); STRING partners: HNRNPF (0.994), HNRNPL (0.982), MATR3 (0.911)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_07055.1, huMAP3_06054.1, huMAP3_11034.1, huMAP3_13511.1, huMAP3_14523.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein H1. This gene encodes a member of a subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins that complex with heterogeneous nuclear RNA. These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the n…
- **Diseases (Open Targets)**: neurodevelopmental disorder with craniofacial dysmorphism and skeletal defects (0.668); dengue disease (0.462); hereditary disease (0.411); neurodevelopmental disorder (0.400); syndromic intellectual disability (0.370)
- **Europe PMC papers**: 1509
- **Why important**: HNRNPH1 has high network connectivity within the module and links the spliceosomal genes to the hnRNP neighborhood and to peripheral genes. It is present in the globally significant spliceosome term (GO:CC catalytic step 2 spliceosome; q_global = 0.0411), is annotated for mRNA splicing and RNA processing, and has established STRING relationships with HNRNPF, HNRNPL, and MATR3. It is also represented in multiple hu.MAP RNA-associated complexes (hu.MAP huMAP3_07055.1), (hu.MAP huMAP3_06054.1), (hu.MAP huMAP3_11034.1), (hu.MAP huMAP3_13511.1), (hu.MAP huMAP3_14523.1). Its disease associations and substantial literature support make it a strong biological anchor.
- **Conclusion**: Established evidence supports HNRNPH1 as a central RNA-processing and spliceosome-associated component of the module. It is plausible, but not demonstrated, that its abundance helps couple the spliceosomal core to the broader hnRNP network in both tissues.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): EXOC8 (0.83), MATR3 (0.83), HNRNPH1 (0.82), ASCC3 (0.81), EFTUD2 (0.81); STRING partners: EFTUD2 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is a core U5 small nuclear ribonucleoprotein helicase and has high network connectivity. It belongs to the globally significant catalytic spliceosome term (GO:CC catalytic step 2 spliceosome; q_global = 0.0411), has a very strong STRING relationship with EFTUD2, and appears with EFTUD2 across several hu.MAP spliceosomal complexes (hu.MAP huMAP3_00960.1), (hu.MAP huMAP3_07622.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), (hu.MAP huMAP3_09945.1), (hu.MAP huMAP3_08980.1). Its established role in spliceosome remodeling and its disease associations make it a particularly informative marker of the module’s principal function.
- **Conclusion**: Established evidence identifies SNRNP200 as a core spliceosomal remodeling factor and one of the clearest functional representatives of the module. The data support its use as a module marker, but do not show that altered SNRNP200 abundance drives the cross-tissue co-abundance pattern.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): HNRNPL (0.85), MOV10 (0.82), SNRNP200 (0.81), CAD (0.80); STRING partners: SNRNP200 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_00960.1, huMAP3_07622.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_08980.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 is a spliceosomal GTPase with high network connectivity and is included in (GO:CC catalytic step 2 spliceosome; q_global = 0.0411). Its strongest reported relationship is with SNRNP200, and it repeatedly co-occurs with SNRNP200 in hu.MAP spliceosomal assemblies (hu.MAP huMAP3_00960.1), (hu.MAP huMAP3_07622.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), (hu.MAP huMAP3_09945.1), (hu.MAP huMAP3_08980.1). Its developmental disease associations and substantial literature make it important for interpreting the module as functional RNA-processing machinery rather than nonspecific housekeeping.
- **Conclusion**: Established evidence supports EFTUD2 as a core component of the spliceosomal part of the module. A reasonable hypothesis is that coordinated EFTUD2 and SNRNP200 abundance reflects shared demand for spliceosome assembly or remodeling, but co-abundance does not establish catalytic regulation.

#### HNRNPF

- **Related proteins** (co-abundance neighbors): HNRNPH1 (0.83); STRING partners: HNRNPH1 (0.994), HNRNPL (0.95), MATR3 (0.766)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_07055.1, huMAP3_06054.1, huMAP3_11034.1, huMAP3_13511.1, huMAP3_14523.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein F. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins that complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and regulate alternative splicing, polyadenylation, and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present…
- **Diseases (Open Targets)**: neurodegenerative disease (0.518); dengue disease (0.370); knee fracture (0.322); breast cancer (0.103); posterior cortical atrophy (0.083)
- **Europe PMC papers**: 971
- **Why important**: HNRNPF is one of the genes in (GO:CC catalytic step 2 spliceosome; q_global = 0.0411) and is tightly connected in STRING to HNRNPH1, HNRNPL, and MATR3. It is annotated for alternative splicing, RNA processing, and regulation of RNA splicing, and it occurs with HNRNPH1 in multiple hu.MAP hnRNP-associated complexes (hu.MAP huMAP3_07055.1), (hu.MAP huMAP3_06054.1), (hu.MAP huMAP3_11034.1), (hu.MAP huMAP3_13511.1), (hu.MAP huMAP3_14523.1). Its literature and disease associations provide additional support for selecting it as a representative regulatory RNA-binding factor.
- **Conclusion**: Established evidence supports HNRNPF as part of the module’s spliceosomal and hnRNP regulatory core. Its role in coordinating the module’s peripheral genes remains a hypothesis and requires perturbation or RNA-interaction experiments.

#### MATR3

- **Related proteins** (co-abundance neighbors): DYNC1I2 (0.87), HNRNPL (0.85), SNRNP200 (0.83), EXOC8 (0.81); STRING partners: HNRNPF (0.766), HNRNPH1 (0.911), HNRNPL (0.757), MOV10 (0.722)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_05721.1, huMAP3_07581.1, huMAP3_06975.1, huMAP3_10625.1
- **Function (MyGene.info)**: matrin 3. This gene encodes a nuclear matrix protein, which is proposed to stabilize certain messenger RNA species. Mutations of this gene are associated with distal myopathy 2, which often includes vocal cord and pharyngeal weakness. Alternatively spliced transcript variants, including read-through transcripts composed of the upstream small nucleolar RNA host gene 4 (non-protein coding) and matrin 3 gene s…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.735); distal myopathy with vocal cord weakness (0.569); neurodegenerative disease (0.529); distal myopathy (0.384); hereditary disease (0.193)
- **Europe PMC papers**: 1756
- **Why important**: MATR3 connects the RNA-processing neighborhood to DYNC1I2, SNRNP200, EXOC8, HNRNPL, HNRNPH1, HNRNPF, and MOV10. It is represented in hu.MAP RNA-associated complexes with HNRNPL (hu.MAP huMAP3_05721.1), (hu.MAP huMAP3_07581.1), (hu.MAP huMAP3_10625.1) and with MOV10 (hu.MAP huMAP3_06975.1), while STRING supports relationships with several hnRNP proteins and MOV10. Its annotated roles in post-transcriptional regulation and its strong literature and disease record make it useful for interpreting the module’s broader RNA-organization architecture.
- **Conclusion**: Established evidence supports MATR3 as an RNA-associated nuclear scaffold or regulatory component connected to several module neighborhoods. It may help bridge spliceosomal and post-transcriptional functions, but that bridging role is a hypothesis rather than a conclusion from the co-abundance data.

#### LMNB1

- **Related proteins** (co-abundance neighbors): CPSF2 (0.87), CAD (0.83), LMNB2 (0.81), METAP1 (0.80); STRING partners: LMNB2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_03501.1, huMAP3_00325.1, huMAP3_13519.1, huMAP3_10433.1, huMAP3_09259.1, huMAP3_10492.1, huMAP3_10614.1
- **Function (MyGene.info)**: lamin B1. This gene encodes one of the two B-type lamin proteins and is a component of the nuclear lamina. A duplication of this gene is associated with autosomal dominant adult-onset leukodystrophy (ADLD). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: microcephaly 26, primary, autosomal dominant (0.723); autosomal dominant primary microcephaly (0.675); adult-onset autosomal dominant demyelinating leukodystrophy (0.670); hereditary disease (0.488); Syndrome with microcephaly as major feature (0.487)
- **Europe PMC papers**: 3851
- **Why important**: LMNB1 is the most informative representative of the nuclear-envelope branch. It is connected to LMNB2 in STRING and is present with LMNB2 in several hu.MAP lamin-associated complexes (hu.MAP huMAP3_03501.1), (hu.MAP huMAP3_00325.1), (hu.MAP huMAP3_13519.1), (hu.MAP huMAP3_10433.1), (hu.MAP huMAP3_09259.1), (hu.MAP huMAP3_10492.1), (hu.MAP huMAP3_10614.1). Its HPA tissue enhancement in bone marrow and lymphoid tissue and cell-type enhancement in spermatid and progenitor populations provide context for possible nuclear-state or differentiation effects. Its nuclear-lamina function and extensive disease literature further support its importance.
- **Conclusion**: Established evidence supports LMNB1 as a nuclear-envelope component that forms a coherent structural submodule with LMNB2. Its connection to the spliceosomal core is presently a co-abundance association, so any role in coordinating nuclear structure with RNA processing remains hypothetical.

## Module 10

**Tissue pair**: kidney and testis  
**Genes (7)**: ATP1B3, ERGIC2, SIRAL1, PSMC2, PSME4, RCC1, RUVBL2

### Function

The module does not have a GO or KEGG term passing global correction, and STRING reports no functional enrichment. Its genes nevertheless point to a mixed biological theme involving proteasome-associated protein quality control, genome maintenance, chromosome and cell-cycle regulation, membrane ion homeostasis, and secretory-pathway trafficking. The strongest coherent molecular anchor is the proteasome-related pair PSMC2 and PSME4, supported by their shared membership in hu.MAP complexes (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1) and by their STRING interaction. The remaining genes connect this anchor only indirectly through co-abundance, so a single established pathway should not be assigned to the whole module.

**Cell composition.** The module is not dominated by secreted proteins, plasma proteins, or blood-cell-enriched proteins. Most genes have low tissue specificity, and blood-cell specificity is generally low, arguing against a straightforward blood-contamination explanation. Several genes show enrichment in spermatogenic cell types, especially late primary spermatocytes, early spermatids, and late spermatids, while protein detection is present in both kidney and testis for nearly all genes with available data. This pattern is compatible with a shared cellular or germ-cell-associated expression program, but the broadly expressed genes mean that the module is not exclusively testis-specific. PSME4 and RUVBL2 have tissue-enhanced expression in skeletal muscle and testis, respectively, whereas the other genes are broadly distributed or cell-type enhanced.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

Known molecular support is sparse. STRING identifies only the PSMC2–PSME4 relationship among the tested gene pairs, providing direct support for a proteasome-associated connection. PSMC2 and PSME4 also co-occur in hu.MAP complexes (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1), whose larger membership is dominated by proteasome subunits and associated proteasome regulators. The fact that only two module members occur in each large complex indicates that the module is not itself a complete proteasome complex. ATP1B3, SIRAL1, ERGIC2, RCC1, and RUVBL2 have no listed STRING partners or hu.MAP complexes within the supplied evidence. Thus, the network contains one established proteasome relationship embedded in a predominantly co-abundance-based structure, rather than a densely validated physical interaction complex.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: PSMC2–PSME4 (0.776)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09656.1 (PSMC2, PSME4; 2/64); huMAP3_13725.1 (PSMC2, PSME4; 2/69)

### Novelty

The co-abundance association may represent a potentially new cross-tissue observation, particularly because most between-gene relationships lack listed STRING or hu.MAP support. However, absence from those resources does not establish novelty: it may reflect tissue context, incomplete coverage, indirect regulation, or correlated cell composition. The lack of globally significant GO or KEGG enrichment and the sparse known-interaction support make it inappropriate to claim discovery of a new conserved molecular complex or pathway. The most defensible conclusion is that this is a candidate shared expression module requiring independent validation, with the PSMC2–PSME4 proteasome link already established rather than novel.

**Hypothesis.** Hypothesis: the module reflects a shared proteostasis-and-genome-maintenance state that is especially visible in spermatogenic cells and is also present in kidney. Proteasome-associated activity represented by PSMC2 and PSME4 could co-vary with DNA repair, chromosome organization, and remodeling functions represented by RUVBL2 and RCC1, while ATP1B3 and ERGIC2 may capture coupled membrane-ion and secretory-trafficking demands. SIRAL1 may be a poorly characterized co-regulated component rather than a proven physical interactor. This model predicts coordinated changes in proteasome activity, DNA-repair or chromatin processes, and germ-cell differentiation, but the current evidence does not demonstrate that these proteins form one biochemical complex.

### Important genes

#### PSME4

- **Related proteins** (co-abundance neighbors): SIRAL1 (0.86), ATP1B3 (0.84), RCC1 (0.81); STRING partners: PSMC2 (0.776)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Not detected in immune cells; location Nucleoplasm; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome activator subunit 4. Predicted to enable lysine-acetylated histone binding activity; peptidase activator activity; and proteasome binding activity. Predicted to be involved in DNA repair; proteasomal ubiquitin-independent protein catabolic process; and spermatogenesis, exchange of chromosomal proteins. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Alzheimer disease (0.340); aortic disorder (0.253); intestinal obstruction (0.198); Paralytic ileus (0.198); breast carcinoma (0.197)
- **Europe PMC papers**: 561
- **Why important**: PSME4 is the highest-strength node in the module and connects three module genes. It has the clearest proteasome-related interpretation, with proteasome activator and binding functions, links to DNA damage response and sperm DNA condensation, direct STRING support with PSMC2, and membership in both hu.MAP complexes (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1). Its protein is detected in kidney and testis, and its tissue-enhanced skeletal-muscle pattern suggests that it is not simply a blood-derived signal. Its literature base is substantial.
- **Conclusion**: Established evidence supports PSME4 as the principal proteasome-associated anchor of the module and as a plausible bridge between protein quality control and germ-cell genome protection. It is not established that PSME4 mechanistically coordinates the other module genes; that broader role remains a hypothesis.

#### PSMC2

- **Related proteins** (co-abundance neighbors): SIRAL1 (0.87); STRING partners: PSME4 (0.776)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is a proteasome regulatory ATPase and is the direct STRING partner of PSME4. It also appears with PSME4 in hu.MAP complexes (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1), giving convergent support from interaction and complex resources. Its annotations include ubiquitin-dependent proteolysis and regulation of proteasomal protein catabolism, and it has disease associations involving plasma-cell malignancy and other neoplastic or protein-aggregation-related conditions. Its literature base is substantial.
- **Conclusion**: Established evidence identifies PSMC2 as a bona fide proteasome component that reinforces the module's proteostasis interpretation. Its inclusion in a germ-cell-associated co-abundance module may indicate shared proteasome demand, but a specific role in kidney–testis conservation is not demonstrated.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): ATP1B3 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 is a multifunctional AAA ATPase with annotations for DNA repair, recombination, telomere maintenance, DNA replication regulation, and snoRNP assembly. It is tissue-enhanced in testis and cell-type enhanced across several spermatogenic populations, making it especially informative for the tissue-pair context. It has a large literature base and disease associations including hypogonadotropic hypogonadism and neoplasia. Its network degree is limited, so its importance comes more from biological specificity than from connectivity.
- **Conclusion**: Established evidence supports RUVBL2 as a plausible genome-maintenance and spermatogenesis-related component. A direct functional connection to the proteasome pair or to ATP1B3 is not established by the supplied interaction resources; its module membership may instead reflect shared regulation or cellular state.

#### RCC1

- **Related proteins** (co-abundance neighbors): ERGIC2 (0.83), PSME4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: regulator of chromosome condensation 1. Enables several functions, including guanyl-nucleotide exchange factor activity; nucleosomal DNA binding activity; and protein heterodimerization activity. Involved in several processes, including G1/S transition of mitotic cell cycle; regulation of mitotic nuclear division; and spindle organization. Located in chromatin; cytoplasm; and nucleus. Part of protein-containing complex. [provided by All…
- **Diseases (Open Targets)**: injury (0.338); neurodegenerative disease (0.338); myasthenia gravis (0.329); neoplasm (0.104); cancer (0.091)
- **Europe PMC papers**: 3525
- **Why important**: RCC1 has strong and well-characterized roles in chromosome segregation, mitotic spindle organization, nuclear reassembly, and cell-cycle regulation. It is cell-type enriched in late spermatids, is detected in both kidney and testis, and has an extensive literature base with disease associations spanning injury, neurodegeneration, and neoplasia. Its co-abundance links to ERGIC2 and PSME4 give it a potentially informative position between genome-related and trafficking-associated signals, although no physical interaction is listed.
- **Conclusion**: Established evidence supports RCC1 as a chromosome and cell-cycle regulator that could be relevant to proliferative or differentiating cells. The proposed connection between RCC1 and the proteasome or ERGIC2 in this module is correlative and should be treated as a hypothesis.

#### ATP1B3

- **Related proteins** (co-abundance neighbors): PSME4 (0.84), ERGIC2 (0.83), RUVBL2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase Na+/K+ transporting subunit beta 3. The protein encoded by this gene belongs to the family of Na+/K+ and H+/K+ ATPases beta chain proteins, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a vari…
- **Diseases (Open Targets)**: congestive heart failure (0.600); atrial fibrillation (0.595); heart failure (0.578); cardiovascular disorder (0.551); cardiac arrhythmia (0.503)
- **Europe PMC papers**: 805
- **Why important**: ATP1B3 is a membrane subunit of the sodium–potassium ATPase system and is annotated for sodium and potassium transport and intracellular ion homeostasis. It is one of the more connected nodes, linking PSME4, ERGIC2, and RUVBL2 in the co-abundance graph. Its protein is detected in kidney and testis, and its cell-type-enhanced pattern includes late spermatids as well as several endocrine, vascular, and other specialized cell populations. It has a substantial literature base and cardiovascular disease associations.
- **Conclusion**: Established evidence supports ATP1B3 as an ion-homeostasis and membrane-function marker that may reflect the physiological demands of kidney and germ-cell tissues. A mechanistic connection to proteasome, DNA-repair, or spermatogenic programs is not established and may represent shared cellular composition or coordinated regulation.

## Module 11

**Tissue pair**: kidney and testis  
**Genes (6)**: ATP2B4, LNPEP, RABGGTA, PITRM1, IARS2, UGGT1

### Function

No GO or KEGG term passed global correction, so the module does not support a formally significant pathway assignment. The network nevertheless suggests a broad protein-homeostasis and membrane-cellular-processing theme rather than a single established pathway. LNPEP connects the other module regions and is associated with peptide processing and signaling; IARS2 and PITRM1 point toward mitochondrial translation, mitochondrial protein processing, and proteolysis; UGGT1 supports endoplasmic-reticulum glycoprotein quality control; RABGGTA supports Rab protein geranylgeranylation and vesicle trafficking; and ATP2B4 supports plasma-membrane calcium transport and calcium homeostasis. These annotations are compatible with coordinated control of protein maturation, trafficking, degradation, and ion homeostasis, but that integrated interpretation remains inferential because there is no globally significant GO or KEGG enrichment.

**Cell composition.** The module is not dominated by blood-cell-enriched genes: every member has low immune-cell specificity in HPA and no blood-cell enrichment is reported. Most genes have low tissue specificity, while the tissue-enhanced signals are distributed across smooth muscle and esophagus rather than concentrated in kidney or testis. Cell-type-enhanced signals are heterogeneous, including neutrophil progenitors, erythrocyte progenitors, spermatids, epithelial cells, smooth muscle cells, and spermatogonial cells. Two genes are classified as secreted in the HPA summary, although the individual annotations also include intracellular, membrane, mitochondrial, cytosolic, or plasma-membrane localization. All module proteins are detected in both kidney and testis. Overall, the shared signal is more consistent with broadly expressed cellular machinery and mixed shared cell states than with a blood-contamination signature or a narrowly tissue-specific program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and STRING reported no functional enrichment. This means the co-abundance relationships are not supported by the supplied STRING evidence as established physical or functional interactions. hu.MAP provides the main external complex context: ATP2B4 and LNPEP occur together in C1, C2, C3, and C4. Those complexes are broad and contain many additional membrane, adhesion, transporter, lysosomal, and signaling proteins, so their recurrence supports a possible shared cellular context but does not establish that the complete module is one molecular complex. IARS2, PITRM1, UGGT1, and RABGGTA are not reported as members of these hu.MAP complexes in the supplied evidence.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10980.1 (ATP2B4, LNPEP; 2/44); huMAP3_10848.1 (ATP2B4, LNPEP; 2/46); huMAP3_09336.1 (ATP2B4, LNPEP; 2/50); huMAP3_11349.1 (ATP2B4, LNPEP; 2/78)

### Novelty

This is best described as a potentially novel tissue-shared co-abundance association, not as a proven new molecular complex or pathway. The module has no supporting STRING interactions or STRING enrichment, and only the ATP2B4-LNPEP pair has recurring hu.MAP complex support. The remaining co-abundance links therefore appear less represented in the supplied interaction resources. However, absence from STRING or hu.MAP cannot establish novelty: the signal may reflect co-expression, shared cellular composition, condition-specific biology, or incomplete database coverage. Novelty should therefore be tested with independent cohorts, cell-resolved data, perturbation experiments, and targeted protein or interaction measurements.

**Hypothesis.** Hypothesis: in kidney and testis cells, a shared cellular state couples membrane calcium control and peptide handling through LNPEP and ATP2B4 with mitochondrial proteostasis through IARS2 and PITRM1, endoplasmic-reticulum glycoprotein quality control through UGGT1, and Rab-dependent trafficking through RABGGTA. The recurring ATP2B4-LNPEP hu.MAP association may represent a membrane or trafficking context in which calcium balance and peptide processing are coordinated, while the other co-abundance links may reflect parallel proteostasis demands rather than direct binding. This hypothesis is compatible with the annotations and network topology, but it is not demonstrated by the enrichment or interaction evidence.

### Important genes

#### LNPEP

- **Related proteins** (co-abundance neighbors): IARS2 (0.86), UGGT1 (0.83), ATP2B4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_10980.1, huMAP3_10848.1, huMAP3_09336.1, huMAP3_11349.1
- **Function (MyGene.info)**: leucyl and cystinyl aminopeptidase. This gene encodes a zinc-dependent aminopeptidase that cleaves vasopressin, oxytocin, lys-bradykinin, met-enkephalin, dynorphin A and other peptide hormones. The protein can be secreted in maternal serum, reside in intracellular vesicles with the insulin-responsive glucose transporter GLUT4, or form a type II integral membrane glycoprotein. The protein catalyzes the final step in the conversion of…
- **Diseases (Open Targets)**: Epstein-Barr virus infection (0.273); frozen shoulder (0.269); hypertensive disorder (0.207); response to xenobiotic stimulus (0.205); inflammatory bowel disease (0.168)
- **Europe PMC papers**: 604
- **Why important**: LNPEP is the most connected and strongest network member, linking IARS2, UGGT1, and ATP2B4. It is a zinc-dependent aminopeptidase with roles in peptide-hormone cleavage, proteolysis, cell-cell signaling, and antigen processing, and it can occupy intracellular vesicular, membrane, or secreted contexts. It is also the only member repeatedly present with ATP2B4 across the reported hu.MAP complexes. Its disease associations include hypertensive disorder and inflammatory bowel disease, and it has comparatively extensive literature support.
- **Conclusion**: Established: LNPEP is the network hub, has peptide-processing and signaling functions, and has repeated hu.MAP context with ATP2B4. Hypothesis: LNPEP may organize or mark the shared membrane-trafficking and proteostasis state represented by the module, but direct coordination with the other members is unproven.

#### ATP2B4

- **Related proteins** (co-abundance neighbors): LNPEP (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Primary cilium; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_10980.1, huMAP3_10848.1, huMAP3_09336.1, huMAP3_11349.1
- **Function (MyGene.info)**: ATPase plasma membrane Ca2+ transporting 4. The protein encoded by this gene belongs to the family of P-type primary ion transport ATPases characterized by the formation of an aspartyl phosphate intermediate during the reaction cycle. These enzymes remove bivalent calcium ions from eukaryotic cells against very large concentration gradients and play a critical role in intracellular calcium homeostasis. The mammalian plasma membrane calcium …
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.393); malaria (0.367); chronic venous hypertension (0.222); male infertility (0.208); prostate cancer (0.114)
- **Europe PMC papers**: 1568
- **Why important**: ATP2B4 is a plasma-membrane and primary-cilium calcium pump, and its established functions include calcium transport, intracellular calcium homeostasis, and spermatogenesis. It is tissue-enhanced in smooth muscle and cell-type-enhanced across several epithelial and smooth-muscle populations. It shares hu.MAP complex context with LNPEP across all reported complexes, despite having no supplied STRING partner. It has the largest literature volume among the module genes and disease associations that include male infertility.
- **Conclusion**: Established: ATP2B4 provides a credible calcium-homeostasis and spermatogenesis component and has repeated complex-level association with LNPEP. Hypothesis: calcium handling may be a regulatory link between the membrane-associated portion of the module and proteostasis or trafficking, but this causal role is not established.

#### PITRM1

- **Related proteins** (co-abundance neighbors): IARS2 (0.84), RABGGTA (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pitrilysin metallopeptidase 1. The protein encoded by this gene is an ATP-dependent metalloprotease that degrades post-cleavage mitochondrial transit peptides. The encoded protein binds zinc and can also degrade amyloid beta A4 protein, suggesting a possible role in Alzheimer's disease. [provided by RefSeq, Dec 2016].
- **Diseases (Open Targets)**: spinocerebellar ataxia, autosomal recessive 30 (0.721); mitochondrial DNA depletion syndrome 7 (hepatocerebral type) (0.333); thyroid gland disorder (0.252); skin disorder (0.244); sporadic amyotrophic lateral sclerosis (0.209)
- **Europe PMC papers**: 400
- **Why important**: PITRM1 is a mitochondrial ATP-dependent metalloprotease that degrades mitochondrial transit peptides and participates in proteolysis and mitochondrial protein localization. It connects IARS2 with RABGGTA in the module, creating a bridge between mitochondrial protein processing and a vesicle-related geranylgeranylation function. It is enriched in early and late spermatids at the single-cell level and is associated with recessive spinocerebellar ataxia and mitochondrial DNA depletion disease. Its literature base is substantial enough to support an established mitochondrial-proteostasis interpretation.
- **Conclusion**: Established: PITRM1 is a mitochondrial protease with reproductive-cell and disease relevance. Hypothesis: its co-abundance with IARS2 may reflect coordinated mitochondrial translation quality control, while its link to RABGGTA may reflect a broader cellular proteostasis state rather than direct interaction.

#### IARS2

- **Related proteins** (co-abundance neighbors): LNPEP (0.86), PITRM1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 2, mitochondrial. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Two forms of isoleucine-tRNA synthetase exist, a cytoplasmic form and a mitochondrial form. This gene encodes th…
- **Diseases (Open Targets)**: cataract-growth hormone deficiency-sensory neuropathy-sensorineural hearing loss-skeletal dysplasia syndrome (0.724); Leigh syndrome (0.563); hereditary disease (0.416); neurodegenerative disease (0.411); mitochondrial disease (0.374)
- **Europe PMC papers**: 411
- **Why important**: IARS2 is the mitochondrial isoleucine-tRNA synthetase and is directly connected to LNPEP and PITRM1 in the module. Its established functions include mitochondrial translation, isoleucyl-tRNA aminoacylation, aminoacyl-tRNA metabolism, and translational fidelity. It is broadly expressed in the supplied HPA summary and is associated with mitochondrial, sensory, skeletal, and neurodegenerative disease categories. Its literature support is substantial, making it a useful anchor for interpreting the mitochondrial component.
- **Conclusion**: Established: IARS2 supplies a clear mitochondrial translation function and occupies a bridging position between the network hub and mitochondrial proteolysis. Hypothesis: coordinated abundance with PITRM1 may indicate coupled synthesis and quality control of mitochondrial proteins, but no direct physical association is shown.

#### UGGT1

- **Related proteins** (co-abundance neighbors): LNPEP (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UDP-glucose glycoprotein glucosyltransferase 1. UDP-glucose:glycoprotein glucosyltransferase (UGT) is a soluble protein of the endoplasmic reticulum (ER) that selectively reglucosylates unfolded glycoproteins, thus providing quality control for protein transport out of the ER.[supplied by OMIM, Oct 2009].
- **Diseases (Open Targets)**: congenital disorder of glycosylation (0.416); hypercholesterolemia, familial, 1 (0.333); connective tissue disorder (0.234); ovarian dysfunction (0.216); chronic laryngitis (0.147)
- **Europe PMC papers**: 507
- **Why important**: UGGT1 is the module member most directly associated with endoplasmic-reticulum glycoprotein quality control. It reglucosylates incompletely folded glycoproteins and supports glycoprotein biosynthesis, folding, and ER mannose processing. Although it is a peripheral network member connected to LNPEP, that position can identify a distinct proteostasis arm of the module. Its disease associations include congenital disorder of glycosylation, and its literature support is substantial.
- **Conclusion**: Established: UGGT1 is an ER glycoprotein-folding and quality-control factor linked to the module through LNPEP. Hypothesis: its co-abundance may indicate that the shared kidney-testis state increases demand for coordinated secretory-pathway quality control alongside membrane trafficking and mitochondrial maintenance.

## Module 12

**Tissue pair**: kidney and testis  
**Genes (28)**: BAX, ERO1A, FAM120A, FLNA, FLNB, FLNC, FSCN1, G6PD, HARS1, HDGF, HNRNPK, EIF5, IQGAP1, NIBAN2, ALDH18A1, PCYOX1L, PRKDC, PTBP1, RAN, RAB3GAP2, SEPTIN9, STAT1, TFRC, TKT, TLN1, TMX1, TXNDC5, XRCC6

### Function

The strongest interpretation is a coupled cell-adhesion, actin-cytoskeleton, and RNA-processing module. The primary enrichment evidence supports cadherin binding (GO:MF cadherin binding; q_global = 0.0017), cell adhesion molecule binding (GO:MF cell adhesion molecule binding; q_global = 0.0125), and RNA binding (GO:MF RNA binding; q_global = 0.0368). The adhesion terms are represented by a coordinated set including FLNA, FLNB, FSCN1, IQGAP1, SEPTIN9, STAT1, TLN1, and related genes, while the RNA-binding term includes HNRNPK, PTBP1, FAM120A, RAN, and other nuclear or cytosolic RNA-associated proteins. The co-abundance structure therefore appears to combine membrane–cytoskeleton organization with post-transcriptional regulation, translation, DNA maintenance, and stress-response functions rather than representing a narrowly tissue-specific pathway. The STRING cadherin-binding result (STRING Function Cadherin binding; within-query FDR = 0.0014) independently supports the adhesion interpretation, but the primary claims are based on (GO:MF cadherin binding; q_global = 0.0017) (GO:MF cell adhesion molecule binding; q_global = 0.0125) (GO:MF RNA binding; q_global = 0.0368).

**Cell composition.** This is not predominantly a plasma or secreted-protein module: most genes are intracellular, with only a minority annotated as secreted or intracellular-and-membrane proteins. It is also not primarily blood-cell specific. HPA indicates broadly low tissue specificity for most genes and low immune-cell specificity for most genes, although several genes show enhancement in megakaryocytes, neutrophils, monocytes, dendritic cells, erythrocyte progenitors, or other specialized cell types. The frequent HPA associations with megakaryocytes and myeloid cells, together with the STRING tissue annotations for leukemia and blood-cancer cells (4 supplementary STRING terms; within-query FDR 0.0084–0.0144), raise the possibility that shared blood-associated or stromal cell content contributes to the kidney–testis signal. However, the module is not adequately explained as a blood-contamination signature because it also contains coherent epithelial, cytoskeletal, RNA-processing, DNA-repair, and germ-cell-related observations. Protein detection is broad in both kidney and testis, supporting biological detectability in the paired tissues rather than a module composed mainly of undetected proteins.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF cadherin binding | 0.0017 | EIF5, FLNA, FLNB, FSCN1, HNRNPK, IQGAP1, NIBAN2, RAN, SEPTIN9, STAT1, TLN1 |
| GO:MF cell adhesion molecule binding | 0.0125 | EIF5, FLNA, FLNB, FSCN1, HNRNPK, IQGAP1, NIBAN2, RAN, SEPTIN9, STAT1, TLN1 |
| GO:MF RNA binding | 0.0368 | ALDH18A1, EIF5, FAM120A, FLNA, FLNB, FSCN1, HARS1, HDGF, HNRNPK, PRKDC, PTBP1, RAN, TFRC, XRCC6 |

### STRING and hu.MAP

STRING contains a clear filamin–talin–IQGAP1–fascin cytoskeletal interaction group: FLNA connects strongly with FLNB, FLNC, FSCN1, IQGAP1, SEPTIN9, and TLN1, while FLNB and FLNC connect with TLN1 and the other filamins. This is established network support for an actin-linked adhesion scaffold. A second known group links HNRNPK with PTBP1, and a DNA-repair group links XRCC6 with PRKDC and BAX. ERO1A–TXNDC5 and G6PD–TKT provide additional redox, protein-folding, and metabolic relationships. hu.MAP supplies partial complex support: HDGF, EIF5, and TLN1 occur in one complex (hu.MAP huMAP3_14982.1), while HNRNPK and FAM120A occur together in two RNA-associated complexes (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_10625.1). These complexes include many proteins outside the module, so they support participation in larger assemblies rather than proving that the entire module is one physical complex. Overall, STRING and hu.MAP show that important parts of the module recapitulate known molecular relationships, while the cross-compartment co-abundance of all genes is a higher-level association.

**STRING interactions (score >= 0.7)**: 18 of 378 gene pairs: BAX–XRCC6 (0.972); ERO1A–TXNDC5 (0.976); FLNA–FLNB (0.979); FLNA–FLNC (0.907); FLNA–FSCN1 (0.887); FLNA–IQGAP1 (0.952); FLNA–SEPTIN9 (0.707); FLNA–TLN1 (0.998); FLNB–FLNC (0.921); FLNB–FSCN1 (0.788); FLNB–TLN1 (0.995); FLNC–FSCN1 (0.794); FLNC–TLN1 (0.996); G6PD–TKT (0.91); HNRNPK–PTBP1 (0.997); HNRNPK–XRCC6 (0.738); IQGAP1–TLN1 (0.893); PRKDC–XRCC6 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Cadherin binding (FDR = 0.0014, 11 genes); Keyword Ubl conjugation (FDR = 0.0063, 13 genes); TISSUES Lymphocytic leukemia cell (FDR = 0.0084, 8 genes); TISSUES Cervical carcinoma cell (FDR = 0.0086, 7 genes); TISSUES Digestive gland (FDR = 0.0086, 23 genes); TISSUES Blood cancer cell (FDR = 0.0086, 13 genes); TISSUES Leukemia cell (FDR = 0.0086, 12 genes); TISSUES Respiratory system (FDR = 0.0096, 15 genes); TISSUES Chronic lymphocytic leukemia cell (FDR = 0.0144, 5 genes); Keyword Isopeptide bond (FDR = 0.0161, 11 genes); TISSUES Liver (FDR = 0.017, 20 genes); SMART Filamin-type immunoglobulin domains (FDR = 0.0171, 3 genes); TISSUES Alimentary canal (FDR = 0.0187, 15 genes); TISSUES Endocrine gland (FDR = 0.02, 27 genes); TISSUES Lymphoid tissue (FDR = 0.0202, 12 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14982.1 (HDGF, EIF5, TLN1; 3/28); huMAP3_10659.1 (HNRNPK, FAM120A; 2/28); huMAP3_10625.1 (HNRNPK, FAM120A; 2/57)

### Novelty

The module should not be described as a wholly new molecular interaction network. Much of its internal structure is already recognized through STRING and hu.MAP, especially the filamin–talin–IQGAP1 adhesion scaffold, the HNRNPK–PTBP1 RNA-processing relationship, and the XRCC6–PRKDC DNA-repair relationship. The potentially novel observation is the coordinated abundance of these cytoskeletal, RNA, DNA-repair, translation, redox, and stress-related components across kidney and testis. That tissue-pair association may be a new systems-level finding, but the fact sheet does not establish novelty against all prior co-expression or proteomic studies. Absence of some genes or edges from STRING or hu.MAP is not evidence of novelty. Independent replication, comparison with existing kidney and testis co-abundance datasets, and cell-type-aware analysis would be needed before claiming a new biological mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared state of structurally active, proliferative or differentiating cells in kidney and testis. In this model, the FLNA–FLNB–FLNC–FSCN1–TLN1–IQGAP1 network organizes adhesion and actin remodeling; SEPTIN9 supports cytoskeletal organization and cell division; HNRNPK and PTBP1 coordinate RNA processing; EIF5, RAN, and HARS1 support translation and nucleocytoplasmic or protein-production demands; and XRCC6 with PRKDC buffers DNA damage associated with proliferation or differentiation. STAT1, NIBAN2, BAX, ERO1A, TXNDC5, G6PD, and TKT could represent signaling, survival, redox, and proteostasis components of the same cellular state. This is a mechanistic model, not an established causal pathway. A competing explanation is shared abundance of particular stromal, epithelial, vascular, germ-cell, or blood-associated cell populations in the tissue samples.

### Important genes

#### FLNA

- **Related proteins** (co-abundance neighbors): TLN1 (0.87), FSCN1 (0.86), FLNC (0.82), FLNB (0.81); STRING partners: FLNB (0.979), FLNC (0.907), FSCN1 (0.887), IQGAP1 (0.952), SEPTIN9 (0.707), TLN1 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is a central adhesion-associated scaffold in the module. It has direct STRING relationships with FLNB, FLNC, FSCN1, IQGAP1, SEPTIN9, and TLN1, and it contributes to all primary enrichment terms (GO:MF cadherin binding; q_global = 0.0017) (GO:MF cell adhesion molecule binding; q_global = 0.0125) (GO:MF RNA binding; q_global = 0.0368). Its established function is to crosslink actin and connect the cytoskeleton to membrane glycoproteins, integrins, receptor complexes, and signaling molecules. HPA places it at the plasma membrane, actin filaments, and cytosol, with enhancement in vascular and several structural cell types. Its disease associations include multiple skeletal and neurodevelopmental syndromes, and its literature support is extensive.
- **Conclusion**: Established evidence supports FLNA as a structural hub linking actin organization to cell adhesion and signaling. Its presence is highly consistent with the module function. The hypothesis that FLNA helps coordinate the kidney–testis shared state is plausible, but co-abundance does not demonstrate that FLNA drives the module.

#### TLN1

- **Related proteins** (co-abundance neighbors): FLNA (0.87), FLNB (0.84), IQGAP1 (0.81); STRING partners: FLNA (0.998), FLNB (0.995), FLNC (0.996), IQGAP1 (0.893)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_14982.1
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 is a focal-adhesion and integrin-associated cytoskeletal protein and contributes to the primary adhesion terms (GO:MF cadherin binding; q_global = 0.0017) (GO:MF cell adhesion molecule binding; q_global = 0.0125). It connects in STRING with FLNA, FLNB, FLNC, and IQGAP1, placing it at the core of the known adhesion scaffold. It is also present in the hu.MAP complex (hu.MAP huMAP3_14982.1). HPA localizes it to focal adhesion sites and cytosol and associates it with megakaryocytes and platelets. Its established functions include cell adhesion, integrin activation, cell–cell junction assembly, and actin-cytoskeleton organization, with disease associations spanning cancer and developmental or cardiac syndromes.
- **Conclusion**: Established evidence identifies TLN1 as a plausible physical and functional bridge between membrane adhesion and actin remodeling. The hypothesis that TLN1 helps couple this scaffold to the RNA and stress components is not yet established and requires experimental or perturbational testing.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): PTBP1 (0.90), XRCC6 (0.88), SEPTIN9 (0.87), EIF5 (0.83), NIBAN2 (0.82), PRKDC (0.81), HDGF (0.80), G6PD (0.80); STRING partners: PTBP1 (0.997), XRCC6 (0.738)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK is one of the strongest integrators of the module. It contributes to every primary enrichment term (GO:MF cadherin binding; q_global = 0.0017) (GO:MF cell adhesion molecule binding; q_global = 0.0125) (GO:MF RNA binding; q_global = 0.0368), connects strongly with PTBP1 and XRCC6 in STRING, and participates in both RNA-associated hu.MAP complexes (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_10625.1). Its established functions include RNA processing, mRNA splicing, transcriptional regulation, and nucleocytoplasmic RNA-associated activity. HPA indicates broad tissue distribution and nucleoplasmic localization. It has extensive disease and literature support, including a defined developmental syndrome association.
- **Conclusion**: Established evidence supports HNRNPK as the principal RNA-processing and transcriptional regulator embedded within an adhesion-rich module. The hypothesis that HNRNPK coordinates the transcriptional or splicing response accompanying cytoskeletal remodeling is biologically coherent but remains unproven in this tissue pair.

#### XRCC6

- **Related proteins** (co-abundance neighbors): SEPTIN9 (0.88), HNRNPK (0.88), PRKDC (0.87), EIF5 (0.85), FAM120A (0.85), NIBAN2 (0.84), PTBP1 (0.84), HARS1 (0.82), STAT1 (0.80); STRING partners: BAX (0.972), HNRNPK (0.738), PRKDC (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: X-ray repair cross complementing 6. The p70/p80 autoantigen is a nuclear complex consisting of two subunits with molecular masses of approximately 70 and 80 kDa. The complex functions as a single-stranded DNA-dependent ATP-dependent helicase. The complex may be involved in the repair of nonhomologous DNA ends such as that required for double-strand break repair, transposition, and V(D)J recombination. High levels of autoantibodies t…
- **Diseases (Open Targets)**: HIV infectious disease (0.505); neurodegenerative disease (0.441); intelligence (0.209); breast cancer (0.175); Abnormality of the skeletal system (0.154)
- **Europe PMC papers**: 2742
- **Why important**: XRCC6 is a high-connectivity bridge between the RNA-associated and DNA-repair portions of the module. It connects with PRKDC and HNRNPK in STRING and contributes to RNA binding (GO:MF RNA binding; q_global = 0.0368). Its established function is as a Ku-associated component of DNA-dependent protein kinase activity and nonhomologous end joining, with additional roles in telomere maintenance and immune-related processes. HPA shows broad tissue distribution and association with early and late primary spermatocytes. It has strong disease relevance, including immunodeficiency and neurological or systemic disease associations, and substantial literature support.
- **Conclusion**: Established evidence supports XRCC6 as a DNA-damage maintenance component that may be especially relevant to proliferating or differentiating cells. Its bridging position supports a role in the broader module, but the hypothesis that DNA-repair activity is coordinated with adhesion remodeling in kidney and testis is not demonstrated by co-abundance alone.

#### SEPTIN9

- **Related proteins** (co-abundance neighbors): XRCC6 (0.88), HNRNPK (0.87), FSCN1 (0.86), EIF5 (0.85), FAM120A (0.85), TMX1 (0.84), HARS1 (0.84), PTBP1 (0.83), TXNDC5 (0.82), TKT (0.81), FLNB (0.81); STRING partners: FLNA (0.707)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: septin 9. This gene is a member of the septin family involved in cytokinesis and cell cycle control. This gene is a candidate for the ovarian tumor suppressor gene. Mutations in this gene cause hereditary neuralgic amyotrophy, also known as neuritis with brachial predilection. A chromosomal translocation involving this gene on chromosome 17 and the MLL gene on chromosome 11 results in acute myelomonocytic l…
- **Diseases (Open Targets)**: neuralgic amyotrophy (0.564); hypertensive disorder (0.496); cataract (0.437); essential hypertension (0.426); alcohol drinking (0.420)
- **Europe PMC papers**: 748
- **Why important**: SEPTIN9 has the strongest module connectivity and links to XRCC6, HNRNPK, FSCN1, EIF5, FAM120A, TMX1, HARS1, and PTBP1. It contributes to the primary adhesion terms (GO:MF cadherin binding; q_global = 0.0017) (GO:MF cell adhesion molecule binding; q_global = 0.0125) and is associated with cytoskeleton organization, intracellular protein localization, cytokinesis, and cilium assembly. HPA places it at actin filaments and associates it with urothelial cells, with detection in both tissues. STRING also links it to FLNA. It has disease associations including hereditary neuralgic amyotrophy and leukemia-related rearrangement, with substantial literature support.
- **Conclusion**: Established evidence supports SEPTIN9 as a structural and cell-cycle-related connector that could unify the adhesion and proliferative aspects of the module. The hypothesis that SEPTIN9 is a key organizer of the shared kidney–testis co-abundance state is attractive because of its network position, but causal importance remains to be tested.

## Module 13

**Tissue pair**: kidney and testis  
**Genes (23)**: CAPN2, GPS1, DNAJB1, EHD1, EWSR1, COLGALT1, GMPS, HSPA8, EIF4G3, IMPDH2, KIFBP, PPP3CA, RECQL, SEC23A, SCFD1, SRP68, SRP72, STAMBP, TARS1, THOP1, NAE1, VPS35, VPS4B

### Function

This is a heterogeneous intracellular module rather than a module with a single statistically established pathway. No GO/KEGG term passed global correction, and STRING provided no supplementary functional enrichment. The strongest functional themes inferred from the individual gene annotations and network structure are protein handling and trafficking: SRP-dependent targeting of nascent secretory and membrane proteins through SRP68 and SRP72; ER-to-Golgi and post-Golgi transport through SCFD1 and SEC23A; endosomal, lysosomal, and membrane-trafficking processes through VPS35, VPS4B, STAMBP, and EHD1; and protein folding or proteostasis through HSPA8 and DNAJB1. A second coherent axis is cellular biosynthetic and growth capacity, represented by IMPDH2 and GMPS in guanine nucleotide synthesis, together with TARS1, EIF4G3, RECQL, and NAE1. The network hub SCFD1 connects several of these otherwise weakly connected functional neighborhoods. Thus, the most defensible interpretation is a shared cellular maintenance module involving protein synthesis, quality control, and intracellular trafficking, rather than a narrowly defined pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only one member is annotated as secreted, and most members are intracellular. It is also not strongly blood-cell specific, because nearly all genes have low immune-cell specificity in HPA. Most genes have low tissue specificity, consistent with broadly expressed housekeeping or core cellular functions. There is nevertheless a testis-related signal, including tissue enhancement for GMPS and EHD1 and enrichment among early or late spermatid-associated profiles. Several genes are also enhanced in diverse epithelial, reproductive, neuronal, or myeloid cell types, so the module may partly reflect shared cellular programs or cell-composition effects rather than a kidney-and-testis-specific biochemical pathway. Protein detection is broadly compatible with the module being present in both tissues, although SEC23A was detected in testis but not kidney and a small minority of genes lacked tissue protein data.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports only a small set of high-confidence pairwise relationships within the module: the chaperone pair HSPA8–DNAJB1, the guanine-nucleotide biosynthesis pair GMPS–IMPDH2, and the SRP pair SRP68–SRP72. These links independently reinforce three plausible local units: protein folding, GMP production, and cotranslational ER targeting. hu.MAP provides repeated support for HSPA8 and DNAJB1 occurring together in several chaperone-related complexes (hu.MAP huMAP3_06506.1), (hu.MAP huMAP3_07919.1), (hu.MAP huMAP3_11049.1), and (hu.MAP huMAP3_14723.1). STAMBP and SEC23A co-occur in a large trafficking-associated complex (hu.MAP huMAP3_12394.1). However, each hu.MAP complex contributes only a small subset of its members to this module, so the evidence supports reuse of established molecular components rather than a complete canonical complex. The sparse STRING connectivity and absence of hu.MAP assignments for most genes indicate that the module is not simply a single known physical complex.

**STRING interactions (score >= 0.7)**: 3 of 253 gene pairs: DNAJB1–HSPA8 (0.999); GMPS–IMPDH2 (0.998); SRP68–SRP72 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06506.1 (HSPA8, DNAJB1; 2/23); huMAP3_07919.1 (HSPA8, DNAJB1; 2/27); huMAP3_11049.1 (HSPA8, DNAJB1; 2/30); huMAP3_14723.1 (HSPA8, DNAJB1; 2/52); huMAP3_12394.1 (STAMBP, SEC23A; 2/98)

### Novelty

The integrated kidney–testis co-abundance module may represent a new systems-level association, but the data do not establish a wholly new molecular pathway. Several of its local relationships are already known through STRING or hu.MAP, especially the HSPA8–DNAJB1 chaperone relationship, the GMPS–IMPDH2 biosynthetic relationship, the SRP68–SRP72 relationship, and the STAMBP–SEC23A complex membership. Conversely, most module edges lack corresponding STRING or hu.MAP support, and there is no globally significant GO/KEGG enrichment that would define a familiar pathway. Therefore, the defensible novelty claim is the cross-tissue co-abundance organization and its proposed connection of protein quality control, trafficking, translation-related machinery, and nucleotide synthesis, not discovery of new protein functions or new physical interactions. Absence from interaction databases alone is insufficient to prove novelty.

**Hypothesis.** Hypothesis: in both kidney and testis, this module reflects a shared demand for coordinated proteostasis and intracellular cargo handling in cells with substantial protein synthesis, membrane trafficking, or specialized reproductive and epithelial functions. SCFD1 may provide a central trafficking-related co-abundance anchor linking ER and Golgi transport with cytosolic maintenance processes. SRP68 and SRP72 could couple synthesis of secretory or membrane proteins to ER targeting, while SEC23A, EHD1, VPS35, VPS4B, and STAMBP could route or recycle intracellular cargo. HSPA8 and DNAJB1 could protect newly synthesized or stress-sensitive proteins, and IMPDH2 with GMPS could support the nucleotide demand associated with RNA production, DNA maintenance, and cell differentiation. This model predicts coordinated regulation of these processes in relevant kidney and testis cell populations, but it requires experimental validation because the enrichment analysis did not identify a globally significant pathway.

### Important genes

#### SCFD1

- **Related proteins** (co-abundance neighbors): SRP72 (0.86), IMPDH2 (0.85), EHD1 (0.85), KIFBP (0.85), SEC23A (0.85), NAE1 (0.85), THOP1 (0.84), HSPA8 (0.83), GMPS (0.83), SRP68 (0.83), VPS35 (0.83), GPS1 (0.82), EWSR1 (0.82), TARS1 (0.81), PPP3CA (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sec1 family domain containing 1. Predicted to enable syntaxin binding activity. Involved in negative regulation of autophagosome assembly; regulation of protein transport; and response to toxic substance. Located in cis-Golgi network. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); bronchial disorder (0.270); placental retention (0.240); bladder calculus (0.205); amyotrophic lateral sclerosis (0.195)
- **Europe PMC papers**: 391
- **Why important**: SCFD1 is the principal network hub and connects SRP72, IMPDH2, EHD1, KIFBP, SEC23A, NAE1, THOP1, and HSPA8. Its annotation places it at the cis-Golgi and in ER-to-Golgi, retrograde, and post-Golgi transport, as well as regulation of autophagosome assembly. It has broad tissue expression and was detected in both kidney and testis, making it a strong candidate for the shared structural organizer of the module. Its literature support is substantial, although less extensive than that of the major chaperone and trafficking genes.
- **Conclusion**: Established evidence supports SCFD1 as a vesicle-transport and Golgi-associated protein with the strongest network position in this module. The hypothesis that it organizes the cross-talk between trafficking, proteostasis, and nucleotide-related processes is plausible but not demonstrated by the supplied data.

#### IMPDH2

- **Related proteins** (co-abundance neighbors): SRP68 (0.87), SCFD1 (0.85), GMPS (0.85), GPS1 (0.84), SRP72 (0.83), EIF4G3 (0.82), VPS4B (0.81), EWSR1 (0.81), EHD1 (0.80); STRING partners: GMPS (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inosine monophosphate dehydrogenase 2. This gene encodes the rate-limiting enzyme in the de novo guanine nucleotide biosynthesis. It is thus involved in maintaining cellular guanine deoxy- and ribonucleotide pools needed for DNA and RNA synthesis. The encoded protein catalyzes the NAD-dependent oxidation of inosine-5'-monophosphate into xanthine-5'-monophosphate, which is then converted into guanosine-5'-monophosphate. This gene is up-…
- **Diseases (Open Targets)**: acute lymphoblastic leukemia (0.529); Crohn disease (0.447); acute myeloid leukemia (0.421); lupus nephritis (0.408); myelodysplastic syndrome (0.403)
- **Europe PMC papers**: 1438
- **Why important**: IMPDH2 is a relatively central connector linking GMPS to SCFD1, SRP68, SRP72, GPS1, EIF4G3, VPS4B, and EWSR1. It is the rate-limiting enzyme in de novo guanine nucleotide production and is directly paired with GMPS by STRING. Its disease associations include hematologic, inflammatory, and renal conditions, and it has a substantial literature base. It was detected in both kidney and testis, while its cell-type enhancement in epithelial and epididymal populations is compatible with specialized tissue activity.
- **Conclusion**: Established evidence identifies IMPDH2 as a core guanine-nucleotide biosynthetic enzyme and a supported local partner of GMPS. Its participation may indicate biosynthetic support for active or differentiating cells, but the module does not establish that nucleotide metabolism drives the entire co-abundance pattern.

#### SRP72

- **Related proteins** (co-abundance neighbors): SRP68 (0.96), SCFD1 (0.86), IMPDH2 (0.83), GMPS (0.82); STRING partners: SRP68 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: signal recognition particle 72. This gene encodes the 72 kDa subunit of the signal recognition particle (SRP), a ribonucleoprotein complex that mediates the targeting of secretory proteins to the endoplasmic reticulum (ER). The SRP complex consists of a 7S RNA and 6 protein subunits: SRP9, SRP14, SRP19, SRP54, SRP68, and SRP72, that are bound to the 7S RNA as monomers or heterodimers. SRP has at least 3 distinct functions that c…
- **Diseases (Open Targets)**: autosomal dominant aplasia and myelodysplasia (0.641); neurodegenerative disease (0.416); intracranial subdural hematoma (0.280); type 2 diabetes mellitus (0.044); oropharynx cancer (0.032)
- **Europe PMC papers**: 696
- **Why important**: SRP72 is directly connected to SRP68 by STRING and has a strong module connection to SCFD1 and IMPDH2. Together with SRP68, it forms the annotated SRP heterodimer involved in signal recognition, translational arrest, and cotranslational targeting of proteins to the ER. It was detected in both kidney and testis and has disease associations involving aplasia, myelodysplasia, and neurodegenerative disease. Its literature support is meaningful and its paired relationship provides one of the clearest mechanistic units in the module.
- **Conclusion**: Established evidence supports SRP72 as an SRP component required for ER targeting of secretory and membrane proteins. The hypothesis that SRP68–SRP72 links the module to tissue-specific secretory or membrane-protein production is reasonable, but the module does not prove altered SRP activity.

#### HSPA8

- **Related proteins** (co-abundance neighbors): TARS1 (0.84), CAPN2 (0.84), SCFD1 (0.83); STRING partners: DNAJB1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Flagellar centriole, Annulus; IHC detected in kidney, testis
- **hu.MAP 3.0**: huMAP3_06506.1, huMAP3_07919.1, huMAP3_11049.1, huMAP3_14723.1
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 8. This gene encodes a member of the heat shock protein 70 family, which contains both heat-inducible and constitutively expressed members. This protein belongs to the latter group, which are also referred to as heat-shock cognate proteins. It functions as a chaperone, and binds to nascent polypeptides to facilitate correct folding. It also functions as an ATPase in the disassembly of clathrin-coated…
- **Diseases (Open Targets)**: dengue disease (0.505); systemic lupus erythematosus (0.375); smoking initiation (0.199); Lennox-Gastaut syndrome (0.118); neoplasm (0.105)
- **Europe PMC papers**: 6937
- **Why important**: HSPA8 is a constitutive HSP70 chaperone involved in nascent-protein folding, unfolded-protein responses, and clathrin-coated-vesicle disassembly. It links TARS1, CAPN2, and SCFD1 in the co-abundance graph and forms a high-confidence STRING relationship with DNAJB1. HSPA8 and DNAJB1 also recur together across several hu.MAP complexes (hu.MAP huMAP3_06506.1), (hu.MAP huMAP3_07919.1), (hu.MAP huMAP3_11049.1), and (hu.MAP huMAP3_14723.1). HSPA8 has the largest literature volume among the prioritized genes and was detected in both tissues.
- **Conclusion**: Established evidence supports HSPA8 as a broadly acting chaperone and trafficking-associated ATPase embedded in known chaperone complexes. It is a strong marker of proteostasis within the module, while the claim that it functionally coordinates the other module branches remains a hypothesis.

#### SEC23A

- **Related proteins** (co-abundance neighbors): COLGALT1 (0.86), SCFD1 (0.85), VPS35 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in testis
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A is connected to SCFD1, COLGALT1, and VPS35 and is assigned with STAMBP to the hu.MAP trafficking complex (hu.MAP huMAP3_12394.1). It is a COPII component responsible for ER export, vesicle budding, and cargo loading, providing a direct mechanistic bridge to the SRP and Golgi-trafficking themes. It has substantial literature and disease associations including craniolenticulosutural dysplasia and male reproductive organ cancer. Its protein was detected in testis, whereas kidney detection was absent in the supplied HPA evidence, so its contribution may be cell-selective rather than uniformly tissue-wide.
- **Conclusion**: Established evidence supports SEC23A as a COPII-mediated ER export factor and as a member of a known trafficking-associated complex. Its integration into a shared kidney–testis module is suggestive of coordinated cargo transport, but the tissue asymmetry in protein detection argues for cautious interpretation.

## Module 14

**Tissue pair**: kidney and testis  
**Genes (5)**: GRIPAP1, ITSN1, PPM1B, SHTN1, MIA3

### Function

The module is most consistent with a membrane-trafficking and endosomal-recycling program, with possible links to neuronal or specialized-cell membrane dynamics. The strongest primary evidence is the globally corrected GO term for synaptic vesicle recycling via endosome (GO:BP synaptic vesicle recycling via endosome; q_global = 0.0369), which contains ITSN1 and GRIPAP1. ITSN1 is associated with endosomal transport, clathrin-coated vesicles, synaptic vesicle endocytosis, and actin assembly, while GRIPAP1 regulates receptor transport and recycling-endosome localization at the postsynapse. MIA3 contributes a vesicle cargo-loading and ER-to-Golgi trafficking function, SHTN1 contributes cell extension, axonogenesis, and Cdc42 or Ras-linked signaling, and PPM1B provides a phosphorylation-regulatory component. Thus, the most defensible interpretation is vesicle and membrane trafficking with context-dependent cell-surface remodeling, rather than a module restricted to synaptic biology. The enrichment result is supported by only the (GO:BP synaptic vesicle recycling via endosome; q_global = 0.0369) term; no other GO or KEGG term passed global correction.

**Cell composition.** The module is not composed of plasma or secreted proteins: the secretome annotation is absent for every member. All members have detected protein in kidney and testis. Most genes have low tissue specificity, so the shared signal could reflect broadly present cellular machinery rather than a tissue-exclusive program. At the same time, every member is cell-type enhanced in HPA, with recurring annotations involving neural or glial populations, photoreceptors, and selected myeloid populations. SHTN1 is brain-enriched and has group-enriched blood-cell annotations, while ITSN1 has immune-cell enhancement; the remaining genes have predominantly low immune-cell specificity. Therefore, blood contamination is not the leading explanation, although shared cell types, cellular composition, or a broadly distributed vesicle-trafficking program could contribute to the kidney-testis co-abundance pattern.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP synaptic vesicle recycling via endosome | 0.0369 | GRIPAP1, ITSN1 |

### STRING and hu.MAP

The module has no high-confidence STRING pairwise interactions among its members and no hu.MAP complex containing multiple module members. Consequently, the co-abundance network is not recapitulated by the queried physical-interaction or curated-complex resources. This does not invalidate the module: co-abundance can arise from coordinated regulation, shared cell-type composition, pathway-level coupling, transient interactions, or interactions that are tissue-, isoform-, or condition-dependent. The internal network connects MIA3 to PPM1B, ITSN1, and SHTN1, with PPM1B connected to GRIPAP1; this topology suggests a trafficking-centered bridge involving regulatory and cytoskeletal or membrane-associated functions, but the edges should be treated as co-abundance relationships rather than established physical interactions.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may represent a novel kidney-testis co-abundance association, but the available evidence does not justify calling it a newly discovered molecular complex or a new pathway. Its novel aspect is the joint co-abundance of these genes across the two tissues, especially because the member set is absent from the queried STRING high-confidence interactions and hu.MAP multi-member complexes. However, absence from those resources alone does not prove novelty. Several component functions are already established, including ITSN1 and GRIPAP1 in endosomal or receptor recycling, MIA3 in secretory trafficking, SHTN1 in neuronal migration and extension, and PPM1B in protein dephosphorylation and stress-related regulation. The appropriate conclusion is that the cross-tissue co-abundance organization is potentially novel and requires replication, tissue-cellular deconvolution, and independent interaction or perturbation studies.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of vesicle movement and membrane remodeling in a shared or compositionally similar cell population present in kidney and testis. MIA3 could mark secretory-pathway cargo handling, ITSN1 and GRIPAP1 could coordinate endosomal recycling and receptor trafficking, SHTN1 could connect that trafficking state to actin-dependent extension or migration, and PPM1B could tune the program through dephosphorylation and stress or signaling control. The neural and photoreceptor annotations suggest that specialized membrane trafficking is one possible cellular context, but this remains a hypothesis rather than evidence that the kidney-testis module is neuronal or synaptic in vivo.

### Important genes

#### ITSN1

- **Related proteins** (co-abundance neighbors): MIA3 (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: intersectin 1. The protein encoded by this gene is a cytoplasmic membrane-associated protein that indirectly coordinates endocytic membrane traffic with the actin assembly machinery. In addition, the encoded protein may regulate the formation of clathrin-coated vesicles and could be involved in synaptic vesicle recycling. This protein has been shown to interact with dynamin, CDC42, SNAP23, SNAP25, SPIN90, EPS15,…
- **Diseases (Open Targets)**: hereditary disease (0.531); neurodevelopmental disorder (0.451); Autistic behavior (0.404); Intellectual disability (0.378); autosomal dominant non-syndromic intellectual disability (0.371)
- **Europe PMC papers**: 1094
- **Why important**: ITSN1 is the clearest functional anchor because it is one of the two genes in the primary global enrichment term (GO:BP synaptic vesicle recycling via endosome; q_global = 0.0369) and is directly connected to MIA3 in the module. Its established annotations place it at the intersection of endosomal transport, clathrin-coated vesicles, actin assembly, and synaptic vesicle endocytosis. It also has the largest literature base among the module members in the supplied evidence and has disease associations involving hereditary and neurodevelopmental disorders. Its HPA annotations support cell-type-specific membrane biology, including photoreceptors and selected immune cells.
- **Conclusion**: Established conclusion: ITSN1 is a biologically plausible trafficking hub and a principal driver of the module's endosomal-recycling interpretation. Hypothesis: its co-abundance with MIA3 may indicate coordinated control of membrane cargo internalization and recycling in the shared kidney-testis cellular context.

#### GRIPAP1

- **Related proteins** (co-abundance neighbors): PPM1B (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GRIP1 associated protein 1. This gene encodes a guanine nucleotide exchange factor for the Ras family of small G proteins (RasGEF). The encoded protein interacts in a complex with glutamate receptor interacting protein 1 (GRIP1) and plays a role in the regulation of AMPA receptor function. [provided by RefSeq, Aug 2013].
- **Diseases (Open Targets)**: neurodegenerative disease (0.286); type 2 diabetes mellitus (0.123); neurodevelopmental disorder (0.118); neoplasm (0.021); Alzheimer disease (0.014)
- **Europe PMC papers**: 210
- **Why important**: GRIPAP1 is the second gene in the primary enrichment term (GO:BP synaptic vesicle recycling via endosome; q_global = 0.0369) and is connected to PPM1B. Its established functions include regulation of neurotransmitter-receptor transport, recycling-endosome localization within the postsynapse, and receptor clustering. Its photoreceptor-enriched HPA annotations fit a specialized membrane-recycling role. Although its literature base is smaller than that of ITSN1, its functional specificity makes it important for interpreting the module.
- **Conclusion**: Established conclusion: GRIPAP1 supports an endosomal receptor-trafficking interpretation and independently reinforces (GO:BP synaptic vesicle recycling via endosome; q_global = 0.0369). Hypothesis: GRIPAP1 may connect the module to regulated surface-receptor recycling outside canonical neuronal tissue, including specialized kidney or testis cell populations.

#### MIA3

- **Related proteins** (co-abundance neighbors): PPM1B (0.88), ITSN1 (0.88), SHTN1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MIA SH3 domain ER export factor 3. Enables cargo receptor activity. Involved in several processes, including COPII-coated vesicle cargo loading; cell migration involved in sprouting angiogenesis; and regulation of leukocyte migration. Located in endoplasmic reticulum exit site and endoplasmic reticulum membrane. Is integral component of membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: coronary artery disorder (0.503); myocardial infarction (0.481); odontochondrodysplasia 2 with hearing loss and diabetes (0.471); coronary atherosclerosis (0.464); angina pectoris (0.439)
- **Europe PMC papers**: 604
- **Why important**: MIA3 has the strongest network position in the module, connecting to PPM1B, ITSN1, and SHTN1. Its established role as an ER exit-site cargo receptor involved in COPII-coated vesicle loading and ER-to-Golgi transport provides an upstream secretory-trafficking counterpart to the endosomal functions of ITSN1 and GRIPAP1. It also has substantial literature support and disease associations involving cardiovascular and developmental disorders.
- **Conclusion**: Established conclusion: MIA3 is the principal network bridge and supports a broad intracellular vesicle-trafficking interpretation. Hypothesis: MIA3 may couple secretory cargo export to the downstream endosomal-recycling processes represented by ITSN1 and GRIPAP1.

#### SHTN1

- **Related proteins** (co-abundance neighbors): MIA3 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location Plasma membrane, Cytosol; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: shootin 1. Enables identical protein binding activity. Involved in positive regulation of neuron migration. Located in cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: smoking initiation (0.404); cleft lip (0.399); cannabis dependence (0.363); obesity disorder (0.328); risk-taking behaviour (0.297)
- **Europe PMC papers**: 258
- **Why important**: SHTN1 is connected to MIA3 and is the only tissue-enriched gene in the module according to the supplied HPA summary, with brain enrichment. Its established functions include axonogenesis, positive regulation of axon extension, cell extension, and Cdc42 or Ras-linked signaling. Its cell-type annotations span glial, endocrine, and myeloid populations, and its disease or trait associations include developmental and behavior-related traits. It therefore provides a potential cell-shape and migration component rather than a direct vesicle-recycling marker.
- **Conclusion**: Established conclusion: SHTN1 supplies evidence for cytoskeletal remodeling, extension, and migration-related biology within the module. Hypothesis: SHTN1 may connect trafficking to cell-surface remodeling or polarized extension in the shared tissue-associated cell population.

#### PPM1B

- **Related proteins** (co-abundance neighbors): MIA3 (0.88), GRIPAP1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Cytosol; IHC detected in kidney, testis
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase, Mg2+/Mn2+ dependent 1B. The protein encoded by this gene is a member of the PP2C family of Ser/Thr protein phosphatases. PP2C family members are known to be negative regulators of cell stress response pathways. This phosphatase has been shown to dephosphorylate cyclin-dependent kinases (CDKs), and thus may be involved in cell cycle control. Overexpression of this phosphatase is reported to cause cell-growth arrest or cel…
- **Diseases (Open Targets)**: cancer (0.509); neurodegenerative disease (0.301); ovarian dysfunction (0.201); hypertrophic cardiomyopathy (0.185); refractive error (0.157)
- **Europe PMC papers**: 745
- **Why important**: PPM1B occupies an intermediate network position, linking MIA3 and GRIPAP1. Its established function as a PP2C-family serine or threonine phosphatase, together with roles in protein dephosphorylation, stress responses, cell-cycle regulation, interferon-beta production, and NF-kappaB signaling, makes it a plausible regulatory modifier of the trafficking-associated genes. It has substantial literature support and disease associations spanning cancer, neurodegenerative disease, and other disorders.
- **Conclusion**: Established conclusion: PPM1B is a signaling and phosphorylation-regulatory component that could modulate the state of the module without defining its primary trafficking function. Hypothesis: PPM1B may tune vesicle trafficking or membrane-remodeling activity through context-dependent dephosphorylation of regulatory proteins.
