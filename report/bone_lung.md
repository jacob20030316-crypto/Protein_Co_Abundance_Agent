# Conserved co-abundance modules: bone and lung

## Module 0

**Tissue pair**: bone and lung  
**Genes (47)**: ACADVL, ACSL3, AGPS, APMAP, ATP2A2, ATL3, CANX, ALCAM, DHCR7, DNAJB12, EMC1, GNG12, GNA13, GPD2, PIGK, HSDL2, ITGA3, ITGB1, MBLAC2, MPDU1, NDUFAF4, NECTIN2, NFU1, NSDHL, NUCB2, DDOST, PCK2, PTPMT1, QSOX2, NRAS, RCN2, DIS3, RTN4, SEC61A1, OXCT1, SEC63, HM13, SUCLG1, TBL2, TFRC, MIA3, TIMMDC1, TIMM50, TMEM214, TMX1, TOMM40, VAMP7

### Function

The strongest interpretation is an endoplasmic-reticulum membrane and membrane-protein biogenesis module. The primary evidence is the concordant set of globally corrected cellular-component terms for the ER membrane, ER subcompartments, the nuclear-outer-membrane–ER network, organelle membranes, membranes, membrane-protein complexes, and ER protein-containing complexes (9 globally significant GO/KEGG terms, q_global 7.95e-08–0.0376; see the table). The module therefore appears to coordinate ER organization, protein insertion and translocation, glycoprotein processing, folding and quality control, membrane trafficking, and associated lipid and sterol metabolism. SEC61A1, SEC63, DDOST, CANX, EMC1, DNAJB12, MPDU1, PIGK, HM13, and TMX1 provide a coherent ER proteostasis and membrane-biogenesis core. Other genes extend the module toward cholesterol and lipid metabolism, mitochondrial function, vesicle traffic, calcium handling, and cell adhesion. The STRING terms independently support a transmembrane and ER-membrane interpretation (15 supplementary STRING terms; within-query FDR 2.24e-11–5.75e-06), but they are supplementary rather than globally corrected enrichment evidence. The absence of a biological-process term among the primary results means that the most defensible conclusion is about cellular location and machinery, not a uniquely defined physiological pathway.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. The HPA summary identifies only a minority of secreted genes, while most genes have low tissue specificity and low immune-cell specificity. Thus, the module does not resemble a conventional blood-plasma signature or a strongly blood-cell-enriched program. A subset of genes has immune-cell-enhanced or hematopoietic associations, including GNA13, GPD2, NECTIN2, TFRC, VAMP7, ALCAM, and genes associated with myeloid cells, monocytes, eosinophils, neutrophils, or platelets. This may contribute to the shared signal, but it is not sufficient to explain the module by blood contamination alone. HPA single-cell annotations are diverse, with repeated enrichment in epithelial, trophoblast, germ-cell, secretory, and other cell types, which is more consistent with broadly used membrane and organelle machinery than with one shared cell type. Lung protein detection is common for many members, whereas the fact sheet provides no matching HPA bone protein assessment; therefore, the bone–lung conservation should not be interpreted as demonstrated protein-level co-expression in both tissues. ALCAM and NUCB2 are secreted to blood according to HPA, and TFRC is also annotated as secreted to blood, but these do not constitute the majority of the module.

**GO/KEGG enrichment**: 9 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC endoplasmic reticulum membrane | 7.95e-08 | ACSL3, ATL3, ATP2A2, CANX, DDOST, DHCR7, DNAJB12, EMC1, HM13, MBLAC2, MIA3, MPDU1, NRAS, NSDHL, PIGK, RTN4, SEC61A1, SEC63, TBL2, TMEM214, TMX1, VAMP7 |
| GO:CC endoplasmic reticulum subcompartment | 7.95e-08 | ACSL3, ATL3, ATP2A2, CANX, DDOST, DHCR7, DNAJB12, EMC1, HM13, MBLAC2, MIA3, MPDU1, NRAS, NSDHL, PIGK, RTN4, SEC61A1, SEC63, TBL2, TMEM214, TMX1, VAMP7 |
| GO:CC nuclear outer membrane-endoplasmic reticulum membrane network | 1.22e-07 | ACSL3, ATL3, ATP2A2, CANX, DDOST, DHCR7, DNAJB12, EMC1, HM13, MBLAC2, MIA3, MPDU1, NRAS, NSDHL, PIGK, RTN4, SEC61A1, SEC63, TBL2, TMEM214, TMX1, VAMP7 |
| GO:CC organelle subcompartment | 4.65e-06 | ACSL3, ATL3, ATP2A2, CANX, DDOST, DHCR7, DNAJB12, EMC1, HM13, MBLAC2, MIA3, MPDU1, NRAS, NSDHL, PIGK, RTN4, SEC61A1, SEC63, TBL2, TMEM214, TMX1, VAMP7 |
| GO:CC endoplasmic reticulum | 6.13e-06 | ACSL3, ATL3, ATP2A2, CANX, DDOST, DHCR7, DNAJB12, EMC1, HM13, MBLAC2, MIA3, MPDU1, NRAS, NSDHL, NUCB2, PIGK, RCN2, RTN4, SEC61A1, SEC63, TBL2, TIMM50, TMEM214, TMX1, VAMP7 |
| GO:CC organelle membrane | 7.28e-06 | ACADVL, ACSL3, AGPS, ATL3, ATP2A2, CANX, DDOST, DHCR7, DNAJB12, EMC1, GPD2, HM13, ITGB1, MBLAC2, MIA3, MPDU1, NDUFAF4, NRAS, NSDHL, PIGK, PTPMT1, QSOX2, RTN4, SEC61A1, SEC63, TBL2, TFRC, TIMM50, TIMMDC1, TMEM214, TMX1, TOMM40, VAMP7 |
| GO:CC membrane | 0.000241 | ACADVL, ACSL3, AGPS, ALCAM, APMAP, ATL3, ATP2A2, CANX, DDOST, DHCR7, DIS3, DNAJB12, EMC1, GNA13, GNG12, GPD2, HM13, HSDL2, ITGA3, ITGB1, MBLAC2, MIA3, MPDU1, NDUFAF4, NECTIN2, NRAS, NSDHL, NUCB2, PIGK, PTPMT1, QSOX2, RTN4, SEC61A1, SEC63, TBL2, TFRC, TIMM50, TIMMDC1, TMEM214, TMX1, TOMM40, VAMP7 |
| GO:CC membrane protein complex | 0.00206 | ALCAM, ATP2A2, DDOST, EMC1, GNA13, GNG12, HM13, ITGA3, ITGB1, PIGK, SEC61A1, SEC63, TFRC, TIMM50, TOMM40, VAMP7 |
| GO:CC endoplasmic reticulum protein-containing complex | 0.0376 | DDOST, EMC1, HM13, PIGK, SEC61A1, SEC63 |

### STRING and hu.MAP

STRING contains a coherent set of established relationships within the module, especially CANX with SEC61A1, DDOST, EMC1, SEC63, TMX1, and ATP2A2; DDOST with SEC61A1 and EMC1; SEC61A1 with SEC63 and TMEM214; ITGA3 with ITGB1; DHCR7 with NSDHL; NDUFAF4 with TIMMDC1; and TIMM50 with TOMM40. Additional links connect ATL3 with RTN4, GNA13 with GNG12, and ITGB1 with TFRC. These relationships indicate that the module contains recognizable ER folding and translocation machinery, sterol-biosynthetic components, adhesion machinery, and mitochondrial import or respiratory-chain components rather than an entirely unconnected gene set. hu.MAP provides convergent complex-level support. The ER and membrane complexes include SEC61A1, ATP2A2, HM13, DHCR7, ACSL3, DNAJB12, QSOX2, and PTPMT1 (hu.MAP huMAP3_09592.1) (hu.MAP huMAP3_06247.1) (hu.MAP huMAP3_08167.1), while several complexes repeatedly contain the ITGA3–ITGB1–ALCAM adhesion group (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1) (hu.MAP huMAP3_06815.1) and GNA13–GNG12 signaling components (hu.MAP huMAP3_10824.1) (hu.MAP huMAP3_12729.1) (hu.MAP huMAP3_11173.1). SEC61A1 also recurs in complexes with QSOX2 or ATP2A2 (hu.MAP huMAP3_08448.1) (hu.MAP huMAP3_07170.1). These known interactions validate portions of the network, but the co-abundance edges that are not represented by STRING or hu.MAP remain associations rather than established physical interactions.

**STRING interactions (score >= 0.7)**: 24 of 1081 gene pairs: ACADVL–HSDL2 (0.787); ALCAM–ITGB1 (0.824); ATL3–RTN4 (0.826); ATP2A2–CANX (0.849); CANX–DDOST (0.886); CANX–EMC1 (0.854); CANX–SEC61A1 (0.914); CANX–SEC63 (0.713); CANX–TMX1 (0.872); DDOST–EMC1 (0.818); DDOST–SEC61A1 (0.998); DHCR7–NSDHL (0.966); GNA13–GNG12 (0.803); GNA13–SUCLG1 (0.718); GNG12–NRAS (0.714); ITGA3–ITGB1 (0.999); ITGB1–TFRC (0.838); NDUFAF4–TIMMDC1 (0.999); NECTIN2–TOMM40 (0.895); OXCT1–SUCLG1 (0.737); SEC61A1–SEC63 (0.999); SEC61A1–TMEM214 (0.778); SEC63–TMEM214 (0.723); TIMM50–TOMM40 (0.971)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Transmembrane (FDR = 2.24e-11, 29 genes); Keyword Transmembrane helix (FDR = 7.38e-11, 28 genes); Keyword Membrane (FDR = 8.84e-10, 37 genes); Component Endoplasmic reticulum membrane (FDR = 4.92e-09, 22 genes); Component Integral component of membrane (FDR = 4.92e-09, 30 genes); COMPARTMENTS Nuclear outer membrane-endoplasmic reticulum membrane network (FDR = 2.03e-08, 18 genes); COMPARTMENTS Endoplasmic reticulum subcompartment (FDR = 2.03e-08, 17 genes); COMPARTMENTS Endoplasmic reticulum membrane (FDR = 2.31e-08, 17 genes); COMPARTMENTS Endoplasmic reticulum (FDR = 5.71e-08, 22 genes); Component Organelle membrane (FDR = 1.03e-07, 33 genes); COMPARTMENTS Organelle subcompartment (FDR = 1.46e-07, 18 genes); Component Endoplasmic reticulum (FDR = 4.78e-07, 24 genes); COMPARTMENTS Organelle membrane (FDR = 4.87e-07, 28 genes); Keyword Endoplasmic reticulum (FDR = 8.78e-07, 19 genes); Component Membrane (FDR = 5.75e-06, 42 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09592.1 (ACSL3, ATP2A2, SEC61A1, QSOX2, HM13, PTPMT1, DNAJB12, DHCR7; 8/95); huMAP3_06247.1 (ATP2A2, SEC61A1, HM13, DHCR7; 4/65); huMAP3_08167.1 (ACSL3, HM13, DHCR7; 3/24); huMAP3_10503.1 (ITGB1, ITGA3, ALCAM; 3/27); huMAP3_10980.1 (ITGB1, ITGA3, ALCAM; 3/44); huMAP3_09336.1 (ITGB1, ITGA3, ALCAM; 3/50); huMAP3_06815.1 (ITGB1, ITGA3; 2/5); huMAP3_08448.1 (SEC61A1, QSOX2; 2/12); huMAP3_07170.1 (ATP2A2, SEC61A1; 2/14); huMAP3_08103.1 (ITGA3, ALCAM; 2/23); huMAP3_09105.1 (ITGA3, ALCAM; 2/24); huMAP3_10824.1 (GNA13, GNG12; 2/26); huMAP3_12729.1 (GNA13, GNG12; 2/30); huMAP3_11173.1 (GNA13, GNG12; 2/34); huMAP3_08689.1 (ITGA3, ALCAM; 2/37)

### Novelty

The module should not be called a wholly new molecular pathway. Much of its content and internal structure recapitulates established ER translocation, glycosylation, chaperone, membrane-shaping, sterol, mitochondrial, and adhesion biology documented by STRING and hu.MAP. At the same time, the specific conserved co-abundance organization across bone and lung may be a potentially novel systems-level observation, particularly because it combines an ER-centered core with adhesion, lipid, and mitochondrial branches. Absence of a relationship from STRING or hu.MAP cannot establish novelty, since those resources emphasize experimentally supported or computationally integrated interactions and may not capture tissue-specific co-abundance. A defensible novelty claim would require replication in independent bone and lung cohorts, preservation after adjustment for cell composition and technical effects, comparison with published tissue co-expression modules, and experimental testing of the proposed cross-branch connections. The present evidence supports a novel module-level association as a possibility, not a proven new mechanism.

**Hypothesis.** Hypothesis: in shared bone and lung cell populations, coordinated ER membrane organization supports the production, folding, glycosylation, quality control, and trafficking of membrane and secretory proteins, while linked sterol and fatty-acid metabolism supplies or remodels the membrane environment. SEC61A1, SEC63, DDOST, CANX, EMC1, DNAJB12, MPDU1, HM13, and TMX1 could form the proteostasis and insertion backbone; ATL3 and RTN4 could help organize ER morphology; DHCR7, NSDHL, and ACSL3 could tune sterol and lipid composition; and ITGA3, ITGB1, ALCAM, and related signaling genes could connect membrane composition to adhesion and tissue architecture. Mitochondrial genes may represent coordinated energetic or organelle-stress demands rather than a single physical complex with the ER. This hypothesis predicts that perturbing ER translocation or lipid composition should alter adhesion-receptor maturation, trafficking, and cellular responses in relevant bone and lung cell types. These causal links are not established by the co-abundance data.

### Important genes

#### SEC61A1

- **Related proteins** (co-abundance neighbors): DDOST (0.82); STRING partners: CANX (0.914), DDOST (0.998), SEC63 (0.999), TMEM214 (0.778)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09592.1, huMAP3_06247.1, huMAP3_08448.1, huMAP3_07170.1
- **Function (MyGene.info)**: SEC61 translocon subunit alpha 1. The protein encoded by this gene belongs to the SECY/SEC61- alpha family. It appears to play a crucial role in the insertion of secretory and membrane polypeptides into the endoplasmic reticulum. This protein found to be tightly associated with membrane-bound ribosomes, either directly or through adaptor proteins. This gene encodes an alpha subunit of the heteromeric SEC61 complex, which also cont…
- **Diseases (Open Targets)**: hyperuricemic nephropathy, familial juvenile type 4 (0.720); immunodeficiency, common variable, 15 (0.529); familial juvenile hyperuricemic nephropathy type 2 (0.515); SEC61A1 deficiency (0.509); severe congenital neutropenia (0.418)
- **Europe PMC papers**: 859
- **Why important**: SEC61A1 is a central network-linked ER translocon component and appears in every primary ER and membrane-complex term listed for it (9 globally significant GO/KEGG terms, q_global 7.95e-08–0.0376; see the table). It has strong STRING relationships with DDOST, SEC63, and CANX and recurs in multiple hu.MAP complexes (hu.MAP huMAP3_09592.1), (hu.MAP huMAP3_06247.1), (hu.MAP huMAP3_08448.1), and (hu.MAP huMAP3_07170.1). Its established role is insertion and translocation of secretory and membrane proteins. It has a substantial literature and disease associations involving SEC61A1 deficiency and immunodeficiency.
- **Conclusion**: Established evidence supports SEC61A1 as a core structural and functional anchor of the ER part of this module. It is a strong candidate for organizing the module's protein-entry machinery. It is not established that SEC61A1 causally drives the conserved bone–lung co-abundance pattern.

#### CANX

- **Related proteins** (co-abundance neighbors): TMX1 (0.87), ATL3 (0.84), ACSL3 (0.81); STRING partners: ATP2A2 (0.849), DDOST (0.886), EMC1 (0.854), SEC61A1 (0.914), SEC63 (0.713), TMX1 (0.872)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is an ER chaperone with a central position among the known interaction evidence, linking ATP2A2, DDOST, EMC1, SEC61A1, SEC63, and TMX1 in STRING. It participates in all primary ER and membrane terms (8 globally significant GO/KEGG terms, q_global 7.95e-08–0.00206; see the table) and has a large literature. Its established function in calnexin-mediated folding and quality control makes it a direct bridge between translocation, glycoprotein maturation, and ER stress handling.
- **Conclusion**: Established evidence supports CANX as a key proteostasis component and a plausible functional connector within the ER core. The module data support coordinated abundance with other ER machinery, but do not demonstrate that altered CANX activity is responsible for the module in either tissue.

#### DDOST

- **Related proteins** (co-abundance neighbors): ATL3 (0.84), PTPMT1 (0.83), MPDU1 (0.82), SEC61A1 (0.82), PIGK (0.81); STRING partners: CANX (0.886), EMC1 (0.818), SEC61A1 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dolichyl-diphosphooligosaccharide--protein glycosyltransferase non-catalytic subunit. This gene encodes a component of the oligosaccharyltransferase complex which catalyzes the transfer of high-mannose oligosaccharides to asparagine residues on nascent polypeptides in the lumen of the rough endoplasmic reticulum. The protein complex co-purifies with ribosomes. The product of this gene is also implicated in the processing of advanced glycation endproducts (AGEs), which form from non…
- **Diseases (Open Targets)**: DDOST-congenital disorder of glycosylation (0.734); young-onset Parkinson disease (0.561); neurodegenerative disease (0.539); dengue disease (0.505); congenital disorder of glycosylation (0.373)
- **Europe PMC papers**: 685
- **Why important**: DDOST is a high-connectivity ER-associated member of the oligosaccharyltransferase machinery. It is present in all primary terms (9 globally significant GO/KEGG terms, q_global 7.95e-08–0.0376; see the table) and has particularly strong known STRING links with SEC61A1, CANX, and EMC1. Its established role in cotranslational N-linked glycosylation directly connects protein translocation to maturation and quality control. It has substantial literature and associations with congenital glycosylation disorders.
- **Conclusion**: Established evidence identifies DDOST as a mechanistically informative bridge between the ER translocon and glycoprotein processing. Its co-abundance with the ER core is consistent with coordinated biosynthetic demand, but the data do not establish a disease-specific glycosylation defect in bone or lung.

#### ATL3

- **Related proteins** (co-abundance neighbors): CANX (0.84), DDOST (0.84), NECTIN2 (0.83), PTPMT1 (0.81), ACADVL (0.81), NSDHL (0.81), DHCR7 (0.80); STRING partners: RTN4 (0.826)
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: atlastin GTPase 3. This gene encodes a member of a family of dynamin-like, integral membrane GTPases. The encoded protein is required for the proper formation of the network of interconnected tubules of the endoplasmic reticulum. Mutations in this gene may be associated with hereditary sensory neuropathy type IF. Alternatively spliced transcript variants that encode distinct isoforms have been described. [provided b…
- **Diseases (Open Targets)**: neuropathy, hereditary sensory, type 1F (0.718); hereditary sensory and autonomic neuropathy type 1 (0.617); hereditary disease (0.193); Familial prostate cancer (0.112); prostate cancer (0.112)
- **Europe PMC papers**: 672
- **Why important**: ATL3 has the strongest network position in the supplied module and is annotated as an ER membrane GTPase required for formation and fusion of the tubular ER network. It participates in the primary ER terms (7 globally significant GO/KEGG terms, q_global 7.95e-08–0.000241; see the table) and has a known STRING relationship with RTN4, another ER-shaping protein. Its disease association with hereditary sensory neuropathy and its substantial literature make it biologically informative beyond simple annotation overlap.
- **Conclusion**: Established evidence supports ATL3 as a candidate ER-architecture regulator within the module. Its position suggests that ER morphology may be an important organizing feature, but whether ATL3 mediates the bone–lung conservation or merely tracks with ER abundance remains a hypothesis.

#### ACSL3

- **Related proteins** (co-abundance neighbors): CANX (0.81), HM13 (0.81), EMC1 (0.81), ALCAM (0.80), SEC63 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_09592.1, huMAP3_08167.1
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 3. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme is highly expressed…
- **Diseases (Open Targets)**: prostate adenocarcinoma (0.370); acute myeloid leukemia (0.313); neurodegenerative disease (0.300); ovarian dysfunction (0.253); Abnormality of the skeletal system (0.215)
- **Europe PMC papers**: 2930
- **Why important**: ACSL3 connects ER membrane localization with long-chain fatty-acid activation and lipid metabolism. It has high network connectivity, participates in the primary ER and membrane terms (7 globally significant GO/KEGG terms, q_global 7.95e-08–0.000241; see the table), and is included in hu.MAP ER and membrane complexes (hu.MAP huMAP3_09592.1) and (hu.MAP huMAP3_08167.1). Its large literature and associations with skeletal-system abnormality and cancer-related traits make it a prominent metabolic and disease-relevant member. It may provide a lipid-metabolic link to ER membrane organization.
- **Conclusion**: Established evidence supports ACSL3 as a lipid-metabolism component embedded in the ER-centered module. The idea that ACSL3-mediated lipid handling tunes ER proteostasis or adhesion-receptor trafficking in bone and lung is plausible but unproven.

#### ITGB1

- **Related proteins** (co-abundance neighbors): NECTIN2 (0.82), RTN4 (0.81), ITGA3 (0.81); STRING partners: ALCAM (0.824), ITGA3 (0.999), TFRC (0.838)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10503.1, huMAP3_10980.1, huMAP3_09336.1, huMAP3_06815.1
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 represents the cell-surface adhesion branch of the module. It is linked to ITGA3, ALCAM, NECTIN2, RTN4, and TFRC in the network or STRING evidence, and it recurs in several hu.MAP adhesion complexes (hu.MAP huMAP3_10503.1) (hu.MAP huMAP3_10980.1) (hu.MAP huMAP3_09336.1) (hu.MAP huMAP3_06815.1). Its established roles include cell adhesion, tissue repair, immune functions, angiogenesis, and phagocytosis. It also has a very substantial literature and broad disease relevance.
- **Conclusion**: Established evidence supports ITGB1 as a functional output or interface of the module connecting membrane protein biogenesis to cell–matrix and cell–cell interactions. The hypothesis that the ER and lipid branches regulate ITGB1 maturation or surface availability in bone and lung is not directly demonstrated.

## Module 1

**Tissue pair**: bone and lung  
**Genes (15)**: AKAP8, BCLAF1, CBX5, GOLIM4, HNRNPR, JPT2, LSM6, NCBP3, NUP214, PNKP, PRPF4, RBM19, SNW1, TRMT1L, USP36

### Function

The strongest interpretation is a nuclear RNA-processing and ribonucleoprotein-granule module. All globally significant GO evidence points to nuclear specks, ribonucleoprotein granules, and nuclear ribonucleoprotein granules (GO:CC nuclear speck; q_global = 0.0271)(GO:CC ribonucleoprotein granule; q_global = 0.0438)(GO:CC nuclear ribonucleoprotein granule; q_global = 0.0476). The shared genes include spliceosome-related factors such as PRPF4 and LSM6, RNA-binding or RNA-export factors such as NCBP3 and HNRNPR, and nucleolar or nuclear regulators such as RBM19 and USP36. The module therefore most plausibly represents coordinated nuclear RNA maturation, splicing, RNA handling, and organization of RNA-protein assemblies. The presence of BCLAF1, CBX5, PNKP, AKAP8, and USP36 also supports connections to transcriptional regulation, chromatin, DNA-damage responses, and nuclear organization, but these are secondary functional interpretations rather than globally significant enrichment results.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity and low immune-cell specificity, and many encode nuclear or nucleolar proteins detected in lung. Thus the shared bone-lung signal is more consistent with broadly used intracellular machinery than with a circulating plasma program. Some genes show cell-type-enhanced patterns, including reproductive, epithelial, neural, and selected myeloid contexts, while NUP214 has blood-cell and spermatid-associated enrichment and GOLIM4 has eosinophil-associated enrichment. These features warrant attention to cell composition, but the overall HPA pattern does not support a primarily blood-cell-driven or secreted module. Bone-specific protein detection cannot be assessed from the supplied HPA tissue data because no matching bone result is available.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC nuclear speck | 0.0271 | BCLAF1, NCBP3, PRPF4, RBM19, SNW1, USP36 |
| GO:CC ribonucleoprotein granule | 0.0438 | BCLAF1, LSM6, NCBP3, PRPF4, RBM19, SNW1, USP36 |
| GO:CC nuclear ribonucleoprotein granule | 0.0476 | BCLAF1, NCBP3, PRPF4, RBM19, SNW1, USP36 |

### STRING and hu.MAP

STRING provides direct high-confidence support for selected parts of the module: BCLAF1 connects with SNW1, while LSM6 connects with PRPF4 and SNW1. STRING functional annotations independently place several members in the nuclear lumen, nucleoplasm, and nuclear speck (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0117)(STRING COMPARTMENTS Nuclear speck; within-query FDR = 0.0161)(STRING Component Nuclear speck; within-query FDR = 0.0195)(STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.024). However, the direct STRING network is sparse relative to all possible gene pairs, so the co-abundance structure is not simply a fully established protein-interaction network. hu.MAP identifies a spliceosome-related complex containing PRPF4 and LSM6 (hu.MAP huMAP3_08980.1), and an RNA-processing or export-related complex containing NCBP3 and BCLAF1 (hu.MAP huMAP3_09943.1). Because each complex contributes only a subset of its members to this module, the data support convergence on RNA-processing machinery rather than a single complete complex. Known STRING and hu.MAP relationships therefore validate important local connections, while the remaining co-abundance links may reflect shared regulation, transient interactions, or common cellular state.

**STRING interactions (score >= 0.7)**: 3 of 105 gene pairs: BCLAF1–SNW1 (0.823); LSM6–PRPF4 (0.999); LSM6–SNW1 (0.826)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Nuclear lumen (FDR = 0.0117, 11 genes); COMPARTMENTS Nuclear speck (FDR = 0.0161, 5 genes); Component Nuclear speck (FDR = 0.0195, 6 genes); COMPARTMENTS Nucleoplasm (FDR = 0.024, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09943.1 (NCBP3, BCLAF1; 2/78); huMAP3_08980.1 (PRPF4, LSM6; 2/97)

### Novelty

The biological components are not novel individually: spliceosome, RNA-export, nuclear-speck, chromatin, and DNA-repair functions are already represented by known annotations and interaction resources. The module may nevertheless be a new observation as a conserved co-abundance pattern across bone and lung, especially because it combines members from several related nuclear processes and is not represented as one complete STRING or hu.MAP complex. That claim should remain provisional. Sparse representation in STRING or partial representation in hu.MAP cannot establish novelty by itself, and the current evidence does not demonstrate a new molecular mechanism. Replication in independent tissue datasets, testing for cell-composition effects, and experimental validation of the module's coordinated regulation would be needed before calling it a novel biological entity.

**Hypothesis.** Hypothesis: a conserved nuclear RNA-processing state is shared by cells present in bone and lung. Coordinated regulation of nuclear-speck and ribonucleoprotein-granule components could couple pre-mRNA splicing, RNA export, RNA surveillance, and transcriptional responses to DNA damage or cellular stress. SNW1, NCBP3, PRPF4, and LSM6 may form the RNA-processing core, while BCLAF1, CBX5, USP36, and PNKP could connect that core to transcription, chromatin, protein stability, or genome-maintenance responses. This is a mechanistic proposal rather than a demonstrated causal pathway; an alternative explanation is that the co-abundance pattern reflects a broadly shared nuclear program or differences in cell composition.

### Important genes

#### SNW1

- **Related proteins** (co-abundance neighbors): NCBP3 (0.90), TRMT1L (0.89), AKAP8 (0.83), LSM6 (0.80); STRING partners: BCLAF1 (0.823), LSM6 (0.826)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SNW domain containing 1. This gene, a member of the SNW gene family, encodes a coactivator that enhances transcription from some Pol II promoters. This coactivator can bind to the ligand-binding domain of the vitamin D receptor and to retinoid receptors to enhance vitamin D-, retinoic acid-, estrogen-, and glucocorticoid-mediated gene expression. It can also function as a splicing factor by interacting with poly(A)-bindin…
- **Diseases (Open Targets)**: cancer (0.580); dengue disease (0.370); neurodegenerative disease (0.261); congenital lactic acidosis, Saguenay-Lac-Saint-Jean type (0.118); chondromalacia (0.052)
- **Europe PMC papers**: 653
- **Why important**: SNW1 has the strongest network position in the module and connects to NCBP3, TRMT1L, AKAP8, and LSM6. It is present in every globally significant GO term (GO:CC nuclear speck; q_global = 0.0271)(GO:CC ribonucleoprotein granule; q_global = 0.0438)(GO:CC nuclear ribonucleoprotein granule; q_global = 0.0476), in all listed STRING compartment terms (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0117)(STRING COMPARTMENTS Nuclear speck; within-query FDR = 0.0161)(STRING Component Nuclear speck; within-query FDR = 0.0195)(STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.024), and has direct STRING links to BCLAF1 and LSM6. Its established functions include transcriptional coactivation, spliceosome-associated RNA processing, and regulation of receptor-mediated transcriptional programs. It also has substantial literature and disease-link coverage relative to several other module members.
- **Conclusion**: Established evidence supports SNW1 as a central connector between the module's nuclear-speck localization and its RNA-splicing or transcriptional functions. It is a strong candidate for a core regulatory component. It remains a hypothesis that SNW1 drives the conserved bone-lung co-abundance pattern or directly coordinates the other module members.

#### PRPF4

- **Related proteins** (co-abundance neighbors): NUP214 (0.86), RBM19 (0.85), USP36 (0.82); STRING partners: LSM6 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: pre-mRNA splicing tri-snRNP complex factor PRPF4. The protein encoded by this gene is part of a heteromeric complex that binds U4, U5, and U6 small nuclear RNAs and is involved in pre-mRNA splicing. The encoded protein also is a mitotic checkpoint protein and a regulator of chemoresistance in human ovarian cancer. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: retinitis pigmentosa (0.634); retinitis pigmentosa 70 (0.578); inherited retinal dystrophy (0.377); neurodegenerative disease (0.203); refractive error (0.083)
- **Europe PMC papers**: 461
- **Why important**: PRPF4 is well connected within the module, links to NUP214, RBM19, and USP36, and has a direct high-confidence STRING relationship with LSM6. It appears in all globally significant GO terms (GO:CC nuclear speck; q_global = 0.0271)(GO:CC ribonucleoprotein granule; q_global = 0.0438)(GO:CC nuclear ribonucleoprotein granule; q_global = 0.0476) and all listed STRING nuclear-compartment terms (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0117)(STRING COMPARTMENTS Nuclear speck; within-query FDR = 0.0161)(STRING Component Nuclear speck; within-query FDR = 0.0195)(STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.024). Its established role in spliceosomal tri-snRNP assembly and pre-mRNA splicing is reinforced by its membership in the hu.MAP spliceosome-related complex (hu.MAP huMAP3_08980.1). It also has a substantial literature base and disease associations involving inherited retinal disorders.
- **Conclusion**: Established evidence makes PRPF4 a strong molecular anchor for the interpretation of the module as RNA-splicing machinery organized in nuclear specks and ribonucleoprotein granules. The hypothesis that altered PRPF4 activity explains the shared tissue pattern is not established by co-abundance alone.

#### NCBP3

- **Related proteins** (co-abundance neighbors): SNW1 (0.90), HNRNPR (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_09943.1
- **Function (MyGene.info)**: nuclear cap binding subunit 3. Enables RNA 7-methylguanosine cap binding activity and mRNA binding activity. Involved in defense response to virus. Located in cytoplasm and nuclear speck. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: mixed connective tissue disease (0.203); retinal degeneration (0.033); infection (0.030); stroke disorder (0.022); alcohol drinking (0.022)
- **Europe PMC papers**: 190
- **Why important**: NCBP3 is connected to SNW1 and HNRNPR, appears in all globally significant GO terms (GO:CC nuclear speck; q_global = 0.0271)(GO:CC ribonucleoprotein granule; q_global = 0.0438)(GO:CC nuclear ribonucleoprotein granule; q_global = 0.0476), and is represented in all listed STRING nuclear-compartment terms (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0117)(STRING COMPARTMENTS Nuclear speck; within-query FDR = 0.0161)(STRING Component Nuclear speck; within-query FDR = 0.0195)(STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.024). It is a member of the hu.MAP RNA-processing or export complex with BCLAF1 (hu.MAP huMAP3_09943.1). Its established functions include mRNA-cap binding, mRNA export, small nuclear RNA export, post-transcriptional regulation, and defense responses to viruses.
- **Conclusion**: Established evidence supports NCБP3 as an interface between nuclear RNA-protein assemblies and RNA export or post-transcriptional control. It is important for explaining why the module may extend beyond splicing into RNA handling. A specific role for NCBP3 in bone-lung coordination remains a hypothesis.

#### BCLAF1

- **Related proteins** (co-abundance neighbors): TRMT1L (0.86), CBX5 (0.83); STRING partners: SNW1 (0.823)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_09943.1
- **Function (MyGene.info)**: BCL2 associated transcription factor 1. This gene encodes a transcriptional repressor that interacts with several members of the BCL2 family of proteins. Overexpression of this protein induces apoptosis, which can be suppressed by co-expression of BCL2 proteins. The protein localizes to dot-like structures throughout the nucleus, and redistributes to a zone near the nuclear envelope in cells undergoing apoptosis. Multiple transcript var…
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); Pulmonary artery atresia (0.416); acute myeloid leukemia (0.357); bronchial disorder (0.288); Vertigo (0.253)
- **Europe PMC papers**: 1702
- **Why important**: BCLAF1 links to TRMT1L and CBX5 in the co-abundance network and has a direct STRING relationship with SNW1. It appears in all globally significant GO terms (GO:CC nuclear speck; q_global = 0.0271)(GO:CC ribonucleoprotein granule; q_global = 0.0438)(GO:CC nuclear ribonucleoprotein granule; q_global = 0.0476) and all listed STRING nuclear-compartment terms (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0117)(STRING COMPARTMENTS Nuclear speck; within-query FDR = 0.0161)(STRING Component Nuclear speck; within-query FDR = 0.0195)(STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.024), and it is paired with NCBP3 in hu.MAP complex (hu.MAP huMAP3_09943.1). Its established functions include transcriptional repression or activation, apoptosis, DNA-damage response, and mRNA stabilization. HPA indicates bone-marrow tissue enhancement but low immune-cell specificity, making it relevant to interpretation without proving a blood-cell origin.
- **Conclusion**: Established evidence places BCLAF1 at the intersection of nuclear RNA regulation, transcription, and stress or apoptosis responses. It may help explain how a shared RNA-processing module is coupled to cellular-state regulation. Whether BCLAF1 is a causal organizer of the conserved module is unresolved.

#### PNKP

- **Related proteins** (co-abundance neighbors): RBM19 (0.85), GOLIM4 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polynucleotide kinase 3'-phosphatase. This locus represents a gene involved in DNA repair. In response to ionizing radiation or oxidative damage, the protein encoded by this locus catalyzes 5' phosphorylation and 3' dephosphorylation of nucleic acids. Mutations at this locus have been associated with microcephaly, seizures, and developmental delay.[provided by RefSeq, Sep 2010].
- **Diseases (Open Targets)**: Ataxia-oculomotor apraxia type 4 (0.802); microcephaly, seizures, and developmental delay (0.800); genetic developmental and epileptic encephalopathy (0.710); spinocerebellar ataxia, autosomal recessive, with axonal neuropathy 2 (0.652); Charcot-Marie-Tooth disease type 2B2 (0.618)
- **Europe PMC papers**: 2922
- **Why important**: PNKP occupies a network bridge between RBM19 and GOLIM4 and is located in the nucleoplasm and nucleoli according to HPA. Its established function is repair of damaged nucleic acids, including single-strand-break and base-excision repair, and it has strong disease associations involving neurological development and DNA-repair deficiency. STRING places it in the nuclear lumen annotation (STRING COMPARTMENTS Nuclear lumen; within-query FDR = 0.0117), although it is not part of a globally significant GO term for this module.
- **Conclusion**: Established evidence supports PNKP as a possible genome-maintenance component adjacent to the RNA-processing core, not as primary evidence for the module's main enriched function. Its inclusion raises the hypothesis that RNA processing and DNA-damage responses are coordinated in the shared tissue state, but the module data do not establish that mechanism.

## Module 2

**Tissue pair**: bone and lung  
**Genes (7)**: ANXA6, ARHGEF2, DNM2, GNL1, KLC4, RPS6KA1, MAP1S

### Function

The module is most consistent with a cytoskeleton-linked intracellular transport and signaling program, centered on KLC4 and connected to microtubule-associated movement, membrane trafficking, calcium-related membrane processes, Rho-family signaling, and kinase-mediated growth or differentiation signaling. The strongest functional convergence is supplementary STRING evidence for a microtubule keyword (STRING Keyword Microtubule; within-query FDR = 0.0087), involving KLC4, MAP1S, ARHGEF2, and DNM2. This interpretation remains provisional: no GO or KEGG term passed global correction, so there is no globally significant GO or KEGG enrichment to support a more specific pathway assignment. The star-like network topology, with KLC4 connected to every other module member, suggests that KLC4 is the network-centered co-abundance marker rather than establishing direct physical binding among the proteins.

**Cell composition.** The module is not composed of secreted proteins and does not show a plasma-protein signature. All members have low tissue specificity, and the HPA summary indicates low immune-cell specificity across the module. The cell-type annotations are heterogeneous, including neutrophils, oligodendrocytes, late spermatids, adipocytes, hepatic stellate cells, and several epithelial or neuronal cell types. Thus, the module does not point cleanly to blood contamination or a single shared cell type. Its broad tissue pattern and diverse cell-type enhancements are compatible with a broadly used intracellular program, although shared cellular state, cellular composition, or technical covariance could still contribute. Protein detection in lung supports that the proteins are present in lung; there is no matching HPA bone tissue result with which to compare them.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The module has no high-confidence STRING interaction among its member pairs, and no hu.MAP complex contains multiple module members. Therefore, the co-abundance edges should not be interpreted as validated physical protein interactions or as membership in a known multiprotein complex. The supplementary STRING microtubule keyword (STRING Keyword Microtubule; within-query FDR = 0.0087) provides functional context for four genes, but it is not global enrichment evidence and does not establish direct interactions. The absence of STRING or hu.MAP links suggests that the module may capture coordinated regulation, shared localization, or common cellular state rather than a pre-existing physical complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Microtubule (FDR = 0.0087, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears to be a potentially novel co-abundance association pattern, because its members do not form a documented high-confidence STRING subnetwork or a shared hu.MAP complex. However, it cannot be called a new biological discovery on that basis alone. The lack of globally significant GO or KEGG enrichment, the absence of independent physical-interaction support, the broad tissue expression pattern, and the possibility of shared cell-state or technical effects all limit the novelty claim. A defensible conclusion is that the bone-lung co-abundance module is a new candidate module requiring replication and orthogonal validation, rather than an established novel mechanism.

**Hypothesis.** Mechanistic hypothesis: coordinated regulation of intracellular transport and cytoskeletal remodeling links KLC4-associated microtubule movement with DNM2-dependent endocytic or vesicular trafficking, ANXA6-dependent calcium and membrane processes, ARHGEF2-mediated Rho signaling, MAP1S-related microtubule organization, and RPS6KA1 signaling. This coordination could produce a shared protein-abundance pattern in bone and lung without requiring stable physical complexes. The hypothesis predicts that the module will track cellular remodeling, trafficking, or differentiation states and should be tested using independent cohorts, cell-resolved data, perturbation experiments, and protein-level measurements.

### Important genes

#### KLC4

- **Related proteins** (co-abundance neighbors): GNL1 (0.92), MAP1S (0.88), ANXA6 (0.85), DNM2 (0.82), RPS6KA1 (0.81), ARHGEF2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kinesin light chain 4. Predicted to be located in cytoplasm and microtubule. Predicted to be part of kinesin complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: early-childhood-onset neurodegeneration with retinitis pigmentosa, sensorineural hearing loss, and demyelinating peripheral neuropathy (0.399); lung carcinoma (0.094); lung cancer (0.094); neoplasm (0.058); hereditary spastic paraplegia (0.033)
- **Europe PMC papers**: 194
- **Why important**: KLC4 is the clear network hub, connecting to every other module member with the strongest weighted relationships in the subgraph. It is annotated as kinesin light chain four, is predicted to participate in a kinesin complex and microtubule-based movement, and is included in the supplementary microtubule signal (STRING Keyword Microtubule; within-query FDR = 0.0087). Its lung protein detection and broad tissue profile support relevance to the sampled tissue, while its disease associations include neurodegeneration with sensory and peripheral nerve features, hereditary spastic paraplegia, and lung malignancy. Its literature volume is comparatively limited within this selected group, making the network centrality particularly important for prioritization.
- **Conclusion**: Established: KLC4 is the structural center of this co-abundance subgraph and has microtubule-related functional annotation. Hypothesis: KLC4 may coordinate the shared intracellular transport state represented by the module, but the network does not establish direct binding or causality.

#### DNM2

- **Related proteins** (co-abundance neighbors): KLC4 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 2. Dynamins represent one of the subfamilies of GTP-binding proteins. These proteins share considerable sequence similarity over the N-terminal portion of the molecule, which contains the GTPase domain. Dynamins are associated with microtubules. They have been implicated in cell processes such as endocytosis and cell motility, and in alterations of the membrane that accompany certain activities such …
- **Diseases (Open Targets)**: autosomal dominant centronuclear myopathy (0.844); Charcot-Marie-Tooth disease dominant intermediate B (0.830); fetal akinesia-cerebral and retinal hemorrhage syndrome (0.739); autosomal dominant Charcot-Marie-Tooth disease type 2M (0.715); centronuclear myopathy (0.692)
- **Europe PMC papers**: 2412
- **Why important**: DNM2 contributes to the microtubule-related supplementary signal (STRING Keyword Microtubule; within-query FDR = 0.0087) and is a GTPase involved in endocytosis, receptor-mediated endocytosis, autophagy, and post-Golgi vesicle transport. Its description also links dynamin activity to microtubules, cell motility, and membrane alterations accompanying osteoclast bone resorption. It has lung protein detection, a neutrophil-enhanced cell-type annotation, extensive disease associations involving centronuclear myopathy and Charcot-Marie-Tooth disease, and a large literature base.
- **Conclusion**: Established: DNM2 is a well-supported membrane-remodeling and vesicle-trafficking protein with relevance to cytoskeletal processes and bone resorption. Hypothesis: its co-abundance with KLC4 may reflect coordinated trafficking or remodeling rather than a direct DNM2-KLC4 complex.

#### ARHGEF2

- **Related proteins** (co-abundance neighbors): KLC4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho/Rac guanine nucleotide exchange factor 2. Rho GTPases play a fundamental role in numerous cellular processes that are initiated by extracellular stimuli that work through G protein coupled receptors. The encoded protein may form complex with G proteins and stimulate rho-dependent signals. Alternatively spliced transcript variants encoding different isoforms have been identified.[provided by RefSeq, Jun 2009].
- **Diseases (Open Targets)**: neurodevelopmental disorder with midbrain and hindbrain malformations (0.525); microcephaly (0.140); Abnormality of the skeletal system (0.127); myoepithelial tumor (0.111); Parkinson disease (0.109)
- **Europe PMC papers**: 1619
- **Why important**: ARHGEF2 is included in the supplementary microtubule keyword signal (STRING Keyword Microtubule; within-query FDR = 0.0087) and is annotated for Rho-family signaling, actin organization, intracellular transport, cell morphogenesis, spindle orientation, and negative regulation of microtubule depolymerization. It has cell-type enhancement in monocytes, neutrophils, and oligodendrocytes, disease associations involving neurodevelopment and skeletal abnormalities, and substantial literature support. Its connection to the KLC4 hub makes it informative for linking microtubules to actin and cell-shape regulation.
- **Conclusion**: Established: ARHGEF2 can connect extracellularly regulated Rho signaling with cytoskeletal organization and transport. Hypothesis: it may help explain how the module couples microtubule movement to remodeling of cell shape in bone and lung.

#### ANXA6

- **Related proteins** (co-abundance neighbors): KLC4 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A6. Annexin VI belongs to a family of calcium-dependent membrane and phospholipid binding proteins. Several members of the annexin family have been implicated in membrane-related events along exocytotic and endocytotic pathways. The annexin VI gene is approximately 60 kbp long and contains 26 exons. It encodes a protein of about 68 kDa that consists of eight 68-amino acid repeats separated by linking …
- **Diseases (Open Targets)**: systemic lupus erythematosus (0.292); asthma (0.194); poisoning (0.193); stricture (0.193); neoplasm (0.115)
- **Europe PMC papers**: 1621
- **Why important**: ANXA6 provides a membrane and calcium dimension to the module. It is a calcium-dependent phospholipid-binding annexin implicated in exocytotic and endocytotic events, and its annotations include calcium transport, mitochondrial calcium homeostasis, and apoptotic signaling. It is detected in lung, has enhancement in adipocytes and hepatic stellate cells among other cell types, is associated with systemic lupus erythematosus and asthma, and has the largest literature volume in the selected set.
- **Conclusion**: Established: ANXA6 is a membrane-associated calcium and trafficking regulator with broad biological relevance. Hypothesis: its co-abundance with the KLC4-centered cytoskeletal group may report coordinated membrane remodeling or calcium-sensitive trafficking, but this is not demonstrated by the available interaction data.

#### RPS6KA1

- **Related proteins** (co-abundance neighbors): KLC4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein S6 kinase A1. This gene encodes a member of the RSK (ribosomal S6 kinase) family of serine/threonine kinases. This kinase contains 2 nonidentical kinase catalytic domains and phosphorylates various substrates, including members of the mitogen-activated kinase (MAPK) signalling pathway. The activity of this protein has been implicated in controlling cell growth and differentiation. Alternate transcriptional spli…
- **Diseases (Open Targets)**: neurodegenerative disease (0.490); hypothyroidism (0.392); bone disorder (0.306); type 2 diabetes mellitus (0.256); response to statin (0.205)
- **Europe PMC papers**: 1449
- **Why important**: RPS6KA1 supplies a signaling component to the module. It is a serine/threonine kinase in the RSK family, acts on substrates including MAPK-pathway components, and is implicated in growth and differentiation. Its annotations include protein phosphorylation, signal transduction, regulation of transcription, and TOR-related regulation. It is detected in lung, has cell-type enhancement in oligodendrocytes and several epithelial or neural cell types, and is associated with bone disorder, neurodegenerative disease, diabetes, and statin response. It also has substantial literature support.
- **Conclusion**: Established: RPS6KA1 is a plausible signaling regulator of growth and differentiation with relevance to bone-related biology. Hypothesis: its coordinated abundance with the cytoskeletal and trafficking genes may reflect signaling control of remodeling or differentiation states rather than membership in a stable protein complex.

## Module 3

**Tissue pair**: bone and lung  
**Genes (5)**: AP3D1, BRIX1, MYG1, UBLCP1, USP15

### Function

The module has no GO or KEGG term that passes global multiple-testing correction, so no pathway-level function can be assigned from primary enrichment evidence. The gene annotations nevertheless suggest a mixed intracellular program involving nucleolar and ribosome-related biology, RNA processing, vesicle and lysosomal trafficking, ubiquitin-dependent regulation, and transforming growth factor beta or bone morphogenetic protein signalling. BRIX1 is the most connected node and links the nucleolar genes MYG1 and UBLCP1 with AP3D1, while AP3D1 connects this nucleolar-associated part of the module to USP15. This supports a co-abundance pattern spanning intracellular maintenance processes rather than a demonstrated single biochemical pathway. The absence of significant enrichment does not invalidate the module.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary identifies no secreted genes, and all genes have intracellular locations or intracellularly annotated functions. Most genes have low tissue specificity, and most have low immune-cell specificity, so the module is not uniformly characteristic of a single tissue or blood-cell population. However, HPA identifies neutrophil-associated expression for UBLCP1 and USP15, with USP15 specifically enhanced in bone marrow, neutrophil progenitors, and neutrophils. Several other genes show cell-type-enhanced expression in specialized cell types, including neural or trophoblast populations. Therefore, shared abundance in bone and lung could partly reflect common cell composition or blood-related material, especially neutrophil-associated material, rather than a bone-lung-specific program. Lung protein detection is available for MYG1, UBLCP1, and USP15, whereas the supplied bone tissue entry has no matching HPA tissue result; this limits direct protein-level comparison between the tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional enrichment is reported. None of the possible within-module gene pairs reaches the supplied high-confidence STRING interaction threshold, and no hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not supported by known high-confidence physical or functional interactions in these resources. The observed structure may reflect coordinated expression, indirect regulation, shared cell composition, or relationships that are not represented in the queried databases. In particular, the BRIX1-centered pattern should not be interpreted as a validated protein complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may represent a previously unrecognized co-abundance association because its member relationships are absent from the supplied high-confidence STRING and hu.MAP results and because no established enriched pathway explains the full set. However, absence from those resources does not prove biological novelty: the genes individually have known functions, and co-abundance can arise from cell composition, tissue sampling, indirect regulation, or incomplete database coverage. The appropriate conclusion is that the module is a novel candidate association requiring replication and orthogonal validation, not a confirmed new molecular complex or pathway.

**Hypothesis.** Hypothesis: the module reflects coordinated intracellular stress or maintenance activity in shared bone and lung cellular material, combining nucleolar and RNA-processing functions with vesicle trafficking and ubiquitin-mediated signalling. BRIX1 may mark the nucleolar and ribosome-biogenesis component; MYG1 and UBLCP1 may accompany RNA-processing and proteostasis activity; AP3D1 may represent intracellular trafficking; and USP15 may connect ubiquitin regulation with transforming growth factor beta or bone morphogenetic protein signalling. An alternative, and possibly coexisting, explanation is that neutrophil-associated material contributes substantially to the shared signal. This hypothesis should be tested by cell-resolved expression, independent cohorts, and perturbation or interaction assays.

### Important genes

#### BRIX1

- **Related proteins** (co-abundance neighbors): MYG1 (0.86), AP3D1 (0.84), UBLCP1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Mitotic chromosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: biogenesis of ribosomes BRX1. Enables RNA binding activity. Predicted to be involved in ribosomal large subunit assembly. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: colorectal cancer (0.077); cancer (0.077); colorectal carcinoma (0.074); deficiency anemia (0.065); sialolithiasis (0.060)
- **Europe PMC papers**: 251
- **Why important**: BRIX1 has the strongest network position in the supplied subgraph and connects the other nucleolar-associated genes with AP3D1. Its established annotations place it in ribosome biogenesis, ribosomal large-subunit assembly, and ribosomal RNA processing. It therefore provides the clearest structural and functional anchor for the module. Its disease-resource associations include cancer-related and deficiency-anemia entries, while its literature record is substantial.
- **Conclusion**: Established evidence supports BRIX1 as a nucleolar ribosome-biogenesis factor and the principal network anchor. It is plausible that BRIX1 helps organize the observed co-abundance pattern, but the data do not establish that it regulates the other module members or that the module is a ribosome-biogenesis pathway.

#### AP3D1

- **Related proteins** (co-abundance neighbors): BRIX1 (0.84), USP15 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor related protein complex 3 subunit delta 1. The protein encoded by this gene is a subunit of the AP3 adaptor-like complex, which is not clathrin-associated, but is associated with the golgi region, as well as more peripheral structures. The AP-3 complex facilitates the budding of vesicles from the golgi membrane, and may be directly involved in trafficking to lysosomes. This subunit is implicated in intracellular biogenesis and trafficking …
- **Diseases (Open Targets)**: Hermansky-Pudlak syndrome 10 (0.584); Hermansky-Pudlak syndrome 2 (0.455); Hermansky-Pudlak syndrome (0.432); Alzheimer disease (0.421); lysosomal storage disease (0.417)
- **Europe PMC papers**: 637
- **Why important**: AP3D1 occupies an intermediate network position between BRIX1 and USP15. Its established function in the AP-three adaptor complex connects the module to Golgi-derived vesicle budding, lysosomal trafficking, and intracellular protein transport, with additional relevance to pigment, platelet dense-granule, and neurotransmitter-vesicle biology. It has the largest literature record among the selected genes and disease associations involving Hermansky-Pudlak and lysosomal-storage disorders.
- **Conclusion**: Established evidence supports AP3D1 as a vesicle-trafficking and lysosome-related adaptor-complex component. Its position suggests a possible bridge between trafficking and the nucleolar or regulatory genes, but the co-abundance data do not demonstrate a direct connection or a shared vesicle complex in this module.

#### USP15

- **Related proteins** (co-abundance neighbors): AP3D1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin specific peptidase 15. This gene encodes a member of the ubiquitin specific protease (USP) family of deubiquitinating enzymes. USP enzymes play critical roles in ubiquitin-dependent processes through polyubiquitin chain disassembly and hydrolysis of ubiquitin-substrate bonds. The encoded protein associates with the COP9 signalosome, and also plays a role in transforming growth factor beta signalling through deubiquitina…
- **Diseases (Open Targets)**: neurodegenerative disease (0.548); alcohol drinking (0.294); post term pregnancy (0.272); smoking initiation (0.217); injury (0.162)
- **Europe PMC papers**: 1872
- **Why important**: USP15 is connected to AP3D1 and is the clearest tissue and blood-cell contextual marker in the module: HPA reports bone-marrow enhancement and enrichment in neutrophil progenitors and neutrophils. Its established molecular role is deubiquitination, including regulation of protein stability and transforming growth factor beta or bone morphogenetic protein signalling. It also has the largest literature record in the module and disease-resource associations spanning neurological disease and other traits.
- **Conclusion**: Established evidence supports USP15 as a deubiquitinating enzyme with relevance to transforming growth factor beta and bone morphogenetic protein signalling, and HPA supports a neutrophil-associated context. It is a strong candidate for explaining either a regulatory component of the module or a contribution from shared neutrophil material. The module does not prove that USP15 controls AP3D1 or the other genes.

#### MYG1

- **Related proteins** (co-abundance neighbors): BRIX1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: MYG1 exonuclease. Predicted to enable nuclease activity. Predicted to be involved in nucleic acid phosphodiester bond hydrolysis. Predicted to act upstream of or within locomotory exploration behavior. Located in mitochondrion and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: triple-A syndrome (0.333); vitiligo (0.090); lung adenocarcinoma (0.074); breast carcinoma (0.037); breast cancer (0.037)
- **Europe PMC papers**: 183
- **Why important**: MYG1 is directly connected to BRIX1 and contributes a second nucleic-acid-processing component. Its supplied annotations describe nuclease activity and roles in mitochondrial RNA metabolism, ribosomal RNA processing, and messenger RNA processing. HPA detects the protein in lung and reports enhancement across several neural cell types, while disease-resource associations include triple-A syndrome and lung adenocarcinoma.
- **Conclusion**: Established evidence supports MYG1 as an RNA-processing or nuclease-related factor with mitochondrial and nucleoplasmic annotations. Its link to BRIX1 is consistent with coordinated RNA and ribosome-related activity, but the data do not establish a direct physical interaction or a lung-specific mechanism.

#### UBLCP1

- **Related proteins** (co-abundance neighbors): BRIX1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli, Nucleoli rim; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin like domain containing CTD phosphatase 1. Enables protein serine/threonine phosphatase activity. Involved in protein dephosphorylation. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); liver disorder (0.226); psoriatic arthritis (0.224); hypothyroidism (0.219); sialolithiasis (0.209)
- **Europe PMC papers**: 215
- **Why important**: UBLCP1 is linked to BRIX1 and adds a nucleolar or nucleoplasmic protein-regulatory component. Its established annotations include protein serine or threonine phosphatase activity, protein dephosphorylation, negative regulation of ATP-dependent activity, and regulation of proteasome assembly. HPA reports enhancement in neutrophils and detects the protein in lung, making it relevant to the possibility of shared immune-cell composition.
- **Conclusion**: Established evidence supports UBLCP1 as a phosphatase-related regulator connected to proteasome assembly and nucleolar biology. Its co-abundance with BRIX1 may indicate coordinated proteostasis or RNA-associated cellular maintenance, but the module does not establish such a mechanism. The neutrophil annotation makes a cell-composition explanation an important competing interpretation.

## Module 4

**Tissue pair**: bone and lung  
**Genes (7)**: AQR, NDUFS7, NUP188, RBM12B, SLX9, SRRT, THOC2

### Function

The module does not have a globally significant GO or KEGG enrichment term, and STRING reports no supplementary functional enrichment. Its gene-level annotations nevertheless converge on nuclear RNA and gene-expression processes: RNA splicing and ribonucleoprotein biology through RBM12B and AQR, mRNA export through THOC2, primary microRNA processing through SRRT, and nucleocytoplasmic transport through NUP188. NDUFS7 contributes a mitochondrial respiratory-chain and energy-production axis. The co-abundance structure is sparse, with RBM12B acting as the main network connector and the remaining relationships forming short links between RNA-processing, nuclear-transport, and mitochondrial genes. Thus, the most defensible interpretation is a broad cellular gene-expression and protein-homeostasis module rather than a narrowly defined pathway.

**Cell composition.** The module is not composed of secreted or plasma proteins, and HPA indicates low immune-cell specificity for every member. Most genes have low tissue specificity, consistent with broadly expressed intracellular biology rather than a tissue-restricted program. Several genes show cell-type-enhanced HPA patterns, including reproductive cell types, epicardial cells, enterocytes, and esophageal epithelial cells, while NDUFS7 is tissue-enhanced in skeletal muscle. These patterns do not support a blood-cell or circulating-protein explanation for the shared bone-lung signal. Because the genes are largely ubiquitous nuclear, mitochondrial, or housekeeping-like factors, the module could reflect shared cellular composition or general cellular state in the sampled tissues rather than a bone-lung-specific mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair reaches the supplied STRING interaction threshold, and STRING provides no functional-enrichment result. Therefore the co-abundance links should not be treated as established direct protein-protein interactions. The only supplied hu.MAP complex evidence is (hu.MAP huMAP3_09943.1), which contains THOC2 and SRRT among a much larger complex. This supports that those two proteins can occur in a shared RNA-associated molecular context, but the limited module representation does not establish that the whole module is a single physical complex. The absence of STRING partners and hu.MAP assignments for the other genes indicates that the network is primarily a co-abundance observation, with only limited support from known molecular-complex membership.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09943.1 (THOC2, SRRT; 2/78)

### Novelty

This appears to be a potentially novel tissue-shared co-abundance pattern, but it cannot be claimed as a newly discovered molecular complex or pathway. The pattern is not already explained by a globally significant GO or KEGG term, a STRING interaction network, or a broadly represented hu.MAP complex. Its novelty lies in the cross-tissue co-abundance relationship among these particular genes, especially the connection of the RBM12B-centered subgraph to NDUFS7, NUP188, and the THOC2-SRRT pair. However, absence from STRING or hu.MAP alone does not prove novelty, and the broad expression of most members means that shared cellular state, cell composition, or technical covariance remain plausible alternative explanations. Validation with independent cohorts, cell-composition adjustment, and targeted molecular assays would be needed before describing it as a new biological mechanism.

**Hypothesis.** Hypothesis: the module may represent coordinated variation in nuclear gene-expression capacity, coupling spliceosome-associated RNA handling and messenger-RNA export with nucleocytoplasmic transport, while also tracking mitochondrial respiratory capacity. RBM12B may mark the central co-abundance axis linking AQR, NUP188, THOC2, and NDUFS7, whereas the SLX9-SRRT link may reflect a related nucleolar or RNA-effector state. In bone and lung, this could arise from shared metabolically active structural or progenitor-like cell populations, or from a common cellular response that coordinates RNA maturation, RNA trafficking, and energy production. This is a mechanistic hypothesis rather than an established interaction model; the sparse network and lack of STRING support argue for testing co-expression reproducibility and cellular localization before inferring direct regulation.

### Important genes

#### RBM12B

- **Related proteins** (co-abundance neighbors): AQR (0.85), NDUFS7 (0.82), THOC2 (0.81), NUP188 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 12B. Enables RNA binding activity. Predicted to be involved in regulation of RNA splicing. Predicted to be part of ribonucleoprotein complex. Predicted to be active in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: placental retention (0.353); connective tissue disorder (0.342); neurodegenerative disease (0.289); alcohol drinking (0.170); myoepithelial tumor (0.111)
- **Europe PMC papers**: 126
- **Why important**: RBM12B is the principal network connector, linking AQR, NDUFS7, THOC2, and NUP188. Its annotation supports RNA binding, regulation of RNA splicing, and ribonucleoprotein-complex biology, placing it at the intersection of the module's RNA-processing and transport signals. It has a comparatively substantial literature presence within this module, although its functional annotation remains partly predictive and its disease associations are not specific to bone or lung.
- **Conclusion**: Established: RBM12B is the strongest network-centered candidate and is annotated for RNA-related nuclear functions. Hypothesis: it may be a regulatory hub through which variation in RNA processing becomes co-abundant with mitochondrial and nuclear-transport genes.

#### AQR

- **Related proteins** (co-abundance neighbors): RBM12B (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aquarius intron-binding spliceosomal factor. Enables 3'-5' RNA helicase activity and single-stranded RNA binding activity. Involved in mRNA splicing, via spliceosome. Located in nucleoplasm. Part of U2-type catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dengue disease (0.370); preeclampsia (0.191); male reproductive organ cancer (0.152); poisoning (0.126); drug allergy (0.126)
- **Europe PMC papers**: 1166
- **Why important**: AQR is a spliceosomal factor with RNA helicase and single-stranded RNA-binding activities and is part of the U two-type catalytic step two spliceosome. Its link to RBM12B provides a coherent RNA-splicing connection within the module. AQR also has the largest literature presence among the selected candidates, making its molecular role relatively well established compared with the less characterized members.
- **Conclusion**: Established: AQR participates in spliceosome-mediated messenger-RNA splicing. Hypothesis: its co-abundance with RBM12B may indicate coordinated regulation of spliceosomal activity in the shared bone-lung cellular context.

#### NUP188

- **Related proteins** (co-abundance neighbors): SLX9 (0.85), RBM12B (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 188. The nuclear pore complex (NPC) is found on the nuclear envelope and forms a gateway that regulates the flow of proteins and RNAs between the cytoplasm and nucleoplasm. The NPC is comprised of approximately 30 distinct proteins collectively known as nucleoporins. Nucleoporins are pore-complex-specific glycoproteins which often have cytoplasmically oriented O-linked N-acetylglucosamine residues and …
- **Diseases (Open Targets)**: sandestig-stefanova syndrome (0.799); HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.527); microcephaly (0.453)
- **Europe PMC papers**: 629
- **Why important**: NUP188 connects SLX9 and RBM12B and is annotated as a nucleoporin involved in RNA export, protein import, and nucleocytoplasmic transport. It provides a mechanistic bridge between nuclear pore function and the module's RNA-processing signals. Its disease associations and comparatively substantial literature make it an important candidate for distinguishing general nuclear transport from a tissue-specific effect.
- **Conclusion**: Established: NUP188 is a component of the nuclear pore system with roles in nucleocytoplasmic transport. Hypothesis: coordinated NUP188 and RNA-processing variation may influence the availability and export of transcripts represented by this module.

#### THOC2

- **Related proteins** (co-abundance neighbors): RBM12B (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_09943.1
- **Function (MyGene.info)**: THO complex subunit 2. The TREX multiprotein complex binds specifically to spliced mRNAs to facilitate mRNA export. The protein encoded by this gene is a member of the THO complex, a subset of the TREX complex. The encoded protein interacts with the THOC1 protein.[provided by RefSeq, Jun 2010].
- **Diseases (Open Targets)**: non-syndromic X-linked intellectual disability (0.753); neurodegenerative disease (0.500); hereditary disease (0.452); X-linked complex neurodevelopmental disorder (0.370); rheumatoid arthritis (0.302)
- **Europe PMC papers**: 680
- **Why important**: THOC2 is linked directly to RBM12B and is a member of the THO subset of the TREX complex, which facilitates export of spliced messenger RNA. It is also one of the two module genes represented in hu.MAP complex (hu.MAP huMAP3_09943.1), providing the module's clearest complex-level support. Its established connection to mRNA processing and export, together with substantial literature and neurodevelopmental disease associations, makes it a strong functional anchor.
- **Conclusion**: Established: THOC2 participates in TREX-associated mRNA processing and nuclear export and appears in hu.MAP complex (hu.MAP huMAP3_09943.1). Hypothesis: THOC2 may connect transcript maturation to the broader nuclear-transport signal in this module, although direct module-wide physical association is unproven.

#### SRRT

- **Related proteins** (co-abundance neighbors): SLX9 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_09943.1
- **Function (MyGene.info)**: serrate, RNA effector molecule. Enables mRNA cap binding complex binding activity and protein-macromolecule adaptor activity. Involved in primary miRNA processing. Located in nucleoplasm. Part of ribonucleoprotein complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dengue disease (0.370); myxedema (0.228); hypothyroidism (0.228); neurodegenerative disease (0.227); hair color (0.175)
- **Europe PMC papers**: 413
- **Why important**: SRRT is linked to SLX9 and is the second module member in hu.MAP complex (hu.MAP huMAP3_09943.1). It is an RNA-effector molecule involved in primary microRNA processing and can bind the mRNA cap-binding complex, giving the module a post-transcriptional regulatory dimension beyond splicing and export. Its literature and disease-association record support biological relevance, while its cell-type-enhanced pattern in spermatogenic cells indicates that its abundance may also reflect cellular composition.
- **Conclusion**: Established: SRRT participates in primary microRNA processing and occurs with THOC2 in hu.MAP complex (hu.MAP huMAP3_09943.1). Hypothesis: the SLX9-SRRT branch may represent a nucleolar or RNA-effector substate that is coordinated with the RBM12B-centered branch.

#### NDUFS7

- **Related proteins** (co-abundance neighbors): RBM12B (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S7. This gene encodes a protein that is a subunit of one of the complexes that forms the mitochondrial respiratory chain. This protein is one of over 40 subunits found in complex I, the nicotinamide adenine dinucleotide (NADH):ubiquinone oxidoreductase. This complex functions in the transfer of electrons from NADH to the respiratory chain, and ubiquinone is believed to be the immediate electron accept…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.765); mitochondrial complex I deficiency, nuclear type 3 (0.699); Leigh syndrome (0.691); mitochondrial disease (0.609); type 2 diabetes mellitus (0.608)
- **Europe PMC papers**: 1206
- **Why important**: NDUFS7 is directly connected to RBM12B and is the module's clearest mitochondrial component. It is a core subunit of respiratory-chain complex I and is annotated for electron transport, aerobic respiration, complex I assembly, and ATP synthesis. Its established mitochondrial disease associations and tissue-enhanced skeletal-muscle pattern make it important for evaluating whether the module couples RNA regulation to cellular energy demand.
- **Conclusion**: Established: NDUFS7 contributes to mitochondrial complex I and respiratory electron transport, with disease associations involving complex I deficiency and Leigh syndrome. Hypothesis: its co-abundance with the nuclear RNA machinery may reflect coordination between transcriptional or post-transcriptional capacity and mitochondrial energy production, or may instead arise from shared metabolically active cell populations.

## Module 5

**Tissue pair**: bone and lung  
**Genes (12)**: ASNS, DBN1, HARS1, IDE, EIF5, LAS1L, MAK16, NUDCD1, PFDN6, RAE1, POLR2D, SNRNP40

### Function

The module is most consistent with a broadly expressed nuclear gene-expression and proteostasis program rather than a tissue-specific bone or lung pathway. Its genes cover RNA polymerase II transcription through POLR2D, pre-mRNA splicing through SNRNP40, RNA export through RAE1, ribosome biogenesis through LAS1L and MAK16, translation initiation through EIF5, aminoacyl-tRNA charging through HARS1, protein folding through PFDN6, and metabolic or peptide processing through ASNS and IDE. The co-abundance structure therefore suggests coordinated regulation of RNA production, RNA maturation, translation, and protein homeostasis. This interpretation is functional coherence inferred from gene annotations and network structure, not from enrichment: no GO or KEGG term passed global correction. The lack of a globally significant term does not invalidate the module.

**Cell composition.** The module does not appear to be driven by plasma proteins, a secreted-protein program, or blood-cell contamination. HPA assigns low immune-cell specificity to every gene, identifies only IDE as secreted in other tissues, and shows low tissue specificity for most genes. A minority are tissue-enhanced, especially in testis or pancreas, while many genes are cell-type enhanced in germ-cell populations and some in podocytes, neurons, glia, fibroblasts, platelets, or cardiomyocytes. This pattern is more compatible with broadly expressed intracellular machinery plus cell-state or cellular-composition effects than with a bone- or lung-specific program. Lung protein detection is mixed across the module, and the bone HPA protein field has no matching tissue data, so these observations do not establish protein-level co-expression in bone.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides limited direct support: the only high-confidence reported interaction is LAS1L–MAK16. This is biologically coherent because both genes are annotated in maturation of ribosomal RNA, but it does not explain the whole module. hu.MAP provides a relevant complex-level connection in (hu.MAP huMAP3_11092.1), where PFDN6 and POLR2D occur among a much larger transcription and RNA-polymerase-associated complex. The module also contains plausible functional links that are not represented as reported STRING or hu.MAP relationships, including the RNA-processing, translation, and chaperone annotations. Thus, the network is a co-abundance pattern with partial support from known molecular relationships, not a fully validated physical complex.

**STRING interactions (score >= 0.7)**: 1 of 66 gene pairs: LAS1L–MAK16 (0.739)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11092.1 (PFDN6, POLR2D; 2/65)

### Novelty

The module may represent a new tissue-pair co-abundance observation, but it cannot be called a newly discovered molecular complex or a definitive new biological pathway. The limited STRING coverage and the partial hu.MAP overlap support only cautious novelty claims: they show that much of the within-module structure is not captured by the referenced interaction resources, while the LAS1L–MAK16 relationship and (hu.MAP huMAP3_11092.1) provide prior biological context. Absence from STRING or hu.MAP alone is not evidence of novelty. The strongest defensible claim is that coordinated abundance of this particular combination across bone and lung appears insufficiently characterized in the supplied resources and requires independent replication and experimental testing.

**Hypothesis.** Hypothesis: the module reflects a shared intracellular capacity program that couples transcription, splicing, RNA export, ribosome biogenesis, translation, protein folding, and peptide or amino-acid metabolism. In bone and lung, variation in the abundance or activity of a common stromal, epithelial, or other non-immune cellular state could coordinately alter these processes, producing the observed co-abundance pattern. The germ-cell and other cell-type enrichments in HPA may indicate generic proliferative or highly biosynthetic cellular machinery rather than a germ-cell process in these tissues. This hypothesis predicts that module abundance should track markers of biosynthetic activity and RNA processing, while not necessarily tracking immune-cell abundance or secretion.

### Important genes

#### POLR2D

- **Related proteins** (co-abundance neighbors): RAE1 (0.87), LAS1L (0.83), MAK16 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase II subunit D. This gene encodes the fourth largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. In yeast, this polymerase subunit is associated with the polymerase under suboptimal growth conditions and may have a stress protective role. A sequence for a ribosomal pseudogene is contained within the 3' untranslated region of the transcript from this gene.…
- **Diseases (Open Targets)**: HIV infectious disease (0.600); acrocephalosyndactyly (0.370); dengue disease (0.370); Orthomyxoviridae infectious disease (0.370); Alzheimer disease (0.235)
- **Europe PMC papers**: 361
- **Why important**: POLR2D has the strongest central network position in the supplied graph and connects directly to RAE1, LAS1L, and MAK16. It is a core RNA polymerase II subunit, is located in the nucleoplasm and nuclear speckles, and is represented in the transcription-associated hu.MAP complex (hu.MAP huMAP3_11092.1). Its substantial literature base and disease-linked Open Targets associations make it a strong anchor for interpreting the module as a nuclear gene-expression program.
- **Conclusion**: Established evidence supports POLR2D as a central transcriptional component and as part of (hu.MAP huMAP3_11092.1). Its co-abundance with RNA-processing and ribosome-biogenesis genes supports a coordinated biosynthetic state. It is not established that POLR2D drives the shared bone-lung module; that causal role remains a hypothesis.

#### RAE1

- **Related proteins** (co-abundance neighbors): POLR2D (0.87), DBN1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribonucleic acid export 1. Mutations in the Schizosaccharomyces pombe Rae1 and Saccharomyces cerevisiae Gle2 genes have been shown to result in accumulation of poly(A)-containing mRNA in the nucleus, suggesting that the encoded proteins are involved in RNA export. The protein encoded by this gene is a homolog of yeast Rae1. It contains four WD40 motifs, and has been shown to localize to distinct foci in the nucleoplasm, to …
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); COVID-19 (0.370); Histiocytosis (0.370)
- **Europe PMC papers**: 1837
- **Why important**: RAE1 occupies a relatively central position and links POLR2D with DBN1. Its annotated functions include nuclear mRNA export, nucleocytoplasmic transport, transcription-dependent tethering of RNA polymerase II gene DNA at the nuclear periphery, and regulation of mitotic spindle organization. It has a large literature base and is tissue-enhanced in testis with germ-cell enrichment, while remaining low in immune-cell specificity.
- **Conclusion**: Established evidence supports RAE1 as an RNA-export and nuclear-organization factor that can connect transcription to post-transcriptional handling of RNA. Its place in this module is consistent with that role, but the supplied data do not establish whether the association reflects RNA export, cell-state composition, or another shared tissue feature.

#### SNRNP40

- **Related proteins** (co-abundance neighbors): LAS1L (0.85), NUDCD1 (0.83), PFDN6 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 40. This gene encodes a component of the U5 small nuclear ribonucleoprotein (snRNP) particle. The U5 snRNP is part of the spliceosome, a multiprotein complex that catalyzes the removal of introns from pre-messenger RNAs. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.530); dengue disease (0.377); X-linked lymphoproliferative syndrome (0.058); autoimmune lymphoproliferative syndrome (0.055); Familial hemophagocytic lymphohistiocytosis (0.053)
- **Europe PMC papers**: 235
- **Why important**: SNRNP40 is among the more connected genes in the module and links LAS1L, NUDCD1, and PFDN6. It is a U5 small nuclear ribonucleoprotein component with established roles in spliceosome assembly, spliceosome conformational change, and mRNA splicing. Its nuclear-speckle localization and germ-cell-associated cell-type pattern fit a regulated RNA-processing interpretation, and its disease associations provide additional biological relevance.
- **Conclusion**: Established evidence identifies SNRNP40 as a spliceosomal factor. Its network position makes RNA splicing an important component of the module-level interpretation, but no globally corrected GO or KEGG result demonstrates pathway enrichment, and no causal disease or tissue mechanism can be assigned from co-abundance alone.

#### LAS1L

- **Related proteins** (co-abundance neighbors): SNRNP40 (0.85), POLR2D (0.83); STRING partners: MAK16 (0.739)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LAS1 like ribosome biogenesis factor. Enables RNA binding activity. Predicted to be involved in maturation of 5.8S rRNA and maturation of LSU-rRNA. Located in membrane. Part of MLL1 complex. Implicated in Wilson-Turner syndrome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Wilson-Turner syndrome (0.658); spinal muscular atrophy with respiratory distress type 2 (0.370); hereditary disease (0.296); Global developmental delay (0.259); neurodevelopmental disorder (0.119)
- **Europe PMC papers**: 286
- **Why important**: LAS1L connects SNRNP40 and POLR2D and forms the sole reported high-confidence STRING interaction in the module with MAK16. Both LAS1L and MAK16 are annotated for maturation of ribosomal RNA, giving this edge direct functional coherence. LAS1L also has disease associations involving Wilson-Turner syndrome and neurodevelopmental conditions, and its nucleoplasmic localization supports a nuclear RNA-processing interpretation.
- **Conclusion**: Established evidence supports LAS1L as a ribosome-biogenesis factor and supports its physical or functional relationship with MAK16 through STRING. Its connection to transcription and splicing genes suggests coordination of nuclear gene-expression machinery, but whether LAS1L is a module driver or simply a correlated component is unknown.

#### PFDN6

- **Related proteins** (co-abundance neighbors): ASNS (0.83), SNRNP40 (0.81), HARS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11092.1
- **Function (MyGene.info)**: prefoldin subunit 6. PFDN6 is a subunit of the heteromeric prefoldin complex that chaperones nascent actin (see MIM 102560) and alpha- and beta-tubulin (see MIM 602529 and MIM 191130, respectively) chains pending their transfer to the cytosolic chaperonin containing TCP1 (MIM 186980) (CCT) complex (Hansen et al., 1999 [PubMed 10209023]).[supplied by OMIM, Jul 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.472); colorectal carcinoma (0.074); neoplasm (0.056); hemoglobin D disease (0.046); dehydrated hereditary stomatocytosis (0.043)
- **Europe PMC papers**: 230
- **Why important**: PFDN6 is highly connected and links ASNS, SNRNP40, and HARS1. It is a prefoldin subunit involved in chaperone-mediated folding and stabilization of nascent proteins, and it appears with POLR2D in the hu.MAP complex (hu.MAP huMAP3_11092.1). This places protein quality control alongside transcription and RNA processing. Its disease associations and broad intracellular localization further support its importance for interpreting cellular proteostasis.
- **Conclusion**: Established evidence supports PFDN6 as a protein-folding and complex-assembly factor with membership in (hu.MAP huMAP3_11092.1). Its position suggests that the module extends beyond RNA metabolism into downstream proteostasis. It is not established that PFDN6 connects the listed processes physically in bone or lung; that integrative role is a hypothesis.

#### IDE

- **Related proteins** (co-abundance neighbors): HARS1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin degrading enzyme. This gene encodes a zinc metallopeptidase that degrades intracellular insulin, and thereby terminates insulins activity, as well as participating in intercellular peptide signalling by degrading diverse peptides such as glucagon, amylin, bradykinin, and kallidin. The preferential affinity of this enzyme for insulin results in insulin-mediated inhibition of the degradation of other peptides such as…
- **Diseases (Open Targets)**: diabetes mellitus (0.307); type 2 diabetes mellitus (0.287); diabetic retinopathy (0.146); diabetic eye disease (0.144); brain cancer (0.142)
- **Europe PMC papers**: 19876
- **Why important**: IDE is the most extensively studied gene in the module according to the supplied literature measure and has a distinct functional position as an insulin- and peptide-degrading zinc metallopeptidase. It connects to HARS1 and is annotated for proteolysis, insulin receptor signaling, peptide catabolism, ubiquitin recycling, and antigen processing. It is the sole gene identified as secreted in other tissues, although the overall module is not a secreted-protein module.
- **Conclusion**: Established evidence supports IDE in intracellular proteolysis and peptide signaling, with disease associations including diabetes and related disorders. Its presence may connect the biosynthetic program to metabolic or peptide-homeostasis demands, but the supplied network does not establish a specific insulin-related mechanism in bone or lung.

## Module 6

**Tissue pair**: bone and lung  
**Genes (36)**: BOP1, CNOT1, DDX54, DDX56, DHX37, CLINT1, ERBIN, GEMIN5, GNL3, GSR, GTPBP4, HEATR1, KRR1, NDUFS2, NKRF, NOL11, NOL6, NOP56, NUP155, NUP205, NUP62, NUP85, NUP93, PES1, ADSS2, PDCD11, RRS1, SMARCA4, SPTBN1, SPTAN1, SURF6, TBL3, UTP15, UTP20, WDR36, WDR3

### Function

The module represents a nucleolar ribosome-biogenesis and RNA-processing program. The strongest primary evidence is the coordinated enrichment for rRNA metabolic process (GO:BP rRNA metabolic process; q_global = 6.74e-12), rRNA processing (GO:BP rRNA processing; q_global = 1.49e-11), preribosome (GO:CC preribosome; q_global = 6.66e-11), ribosome biogenesis (GO:BP ribosome biogenesis; q_global = 1.05e-10), and ribonucleoprotein-complex biogenesis (GO:BP ribonucleoprotein complex biogenesis; q_global = 6.87e-10). Further primary evidence links the module to small-subunit biogenesis and the small-subunit processome (GO:BP ribosomal small subunit biogenesis; q_global = 4.6e-09)(GO:CC small-subunit processome; q_global = 6.62e-09), the nucleolus (GO:CC nucleolus; q_global = 2.01e-08), the eukaryotic ribosome-biogenesis pathway (KEGG Ribosome biogenesis in eukaryotes - Homo sapiens (human); q_global = 2.38e-05), and maturation and cleavage of precursor rRNA (GO:BP maturation of SSU-rRNA; q_global = 0.000226)(GO:BP maturation of SSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA); q_global = 0.0111)(GO:BP endonucleolytic cleavage of tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA); q_global = 0.0155). The nuclear-pore and RNA-binding terms (GO:CC nuclear membrane; q_global = 0.00442)(GO:MF structural constituent of nuclear pore; q_global = 0.00463)(GO:MF snoRNA binding; q_global = 0.00851) indicate that the module also includes nuclear transport and RNA-associated components. Thus, the best-supported interpretation is a conserved nucleolar production, maturation, and trafficking system for ribosomal RNA and ribonucleoprotein particles, with additional links to general RNA processing and gene expression (GO:BP cellular component biogenesis; q_global = 4.48e-06)(GO:BP RNA processing; q_global = 5.77e-06)(GO:BP RNA biosynthetic process; q_global = 3.4e-05)(GO:BP RNA metabolic process; q_global = 0.000183)(GO:BP gene expression; q_global = 0.00139).

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It is also not strongly blood-cell biased, because nearly all genes have low immune-cell specificity and only limited enrichment is associated with basophils or progenitor populations. Most genes have low tissue specificity, which is consistent with a broadly used intracellular housekeeping program rather than a bone- or lung-specific pathway. Many proteins are detected in lung, while the bone comparison has no matching HPA tissue protein result. The HPA pattern therefore supports a shared cellular program, plausibly reflecting nucleated cells present in both tissues, rather than a blood or extracellular contamination signal. Cell-type-enhanced annotations in reproductive, epithelial, muscle, neural, and progenitor populations further argue that the program is broadly deployed across cell types.

**GO/KEGG enrichment**: 39 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP rRNA metabolic process | 6.74e-12 | BOP1, DDX54, DDX56, DHX37, GTPBP4, HEATR1, KRR1, NOL11, NOL6, NOP56, PDCD11, PES1, RRS1, SMARCA4, TBL3, UTP15, UTP20, WDR3, WDR36 |
| GO:BP rRNA processing | 1.49e-11 | BOP1, DDX54, DDX56, DHX37, GTPBP4, HEATR1, KRR1, NOL11, NOL6, NOP56, PDCD11, PES1, RRS1, TBL3, UTP15, UTP20, WDR3, WDR36 |
| GO:CC preribosome | 6.66e-11 | BOP1, DHX37, HEATR1, KRR1, NOL6, NOP56, PDCD11, PES1, RRS1, TBL3, UTP15, UTP20, WDR3, WDR36 |
| GO:BP ribosome biogenesis | 1.05e-10 | BOP1, DDX54, DDX56, DHX37, GTPBP4, HEATR1, KRR1, NOL11, NOL6, NOP56, PDCD11, PES1, RRS1, SURF6, TBL3, UTP15, UTP20, WDR3, WDR36 |
| GO:BP ribonucleoprotein complex biogenesis | 6.87e-10 | BOP1, DDX54, DDX56, DHX37, GEMIN5, GTPBP4, HEATR1, KRR1, NOL11, NOL6, NOP56, PDCD11, PES1, RRS1, SURF6, TBL3, UTP15, UTP20, WDR3, WDR36 |
| GO:BP ribosomal small subunit biogenesis | 4.6e-09 | DHX37, HEATR1, KRR1, NOL11, NOL6, NOP56, RRS1, SURF6, TBL3, UTP15, UTP20, WDR3 |
| GO:CC small-subunit processome | 6.62e-09 | DHX37, HEATR1, KRR1, NOL6, NOP56, PDCD11, TBL3, UTP15, UTP20, WDR3, WDR36 |
| GO:CC nucleolus | 2.01e-08 | BOP1, DDX54, DDX56, DHX37, GNL3, GTPBP4, HEATR1, KRR1, NKRF, NOL11, NOL6, NOP56, PDCD11, PES1, RRS1, SMARCA4, SPTBN1, SURF6, TBL3, UTP15, UTP20, WDR3, WDR36 |
| GO:BP cellular component biogenesis | 4.48e-06 | BOP1, CNOT1, DDX54, DDX56, DHX37, GEMIN5, GTPBP4, HEATR1, KRR1, NDUFS2, NOL11, NOL6, NOP56, NUP205, NUP62, NUP85, NUP93, PDCD11, PES1, RRS1, SMARCA4, SPTAN1, SPTBN1, SURF6, TBL3, UTP15, UTP20, WDR3, WDR36 |
| GO:BP RNA processing | 5.77e-06 | BOP1, DDX54, DDX56, DHX37, GEMIN5, GTPBP4, HEATR1, KRR1, NOL11, NOL6, NOP56, NUP155, PDCD11, PES1, RRS1, TBL3, UTP15, UTP20, WDR3, WDR36 |
| GO:CC nuclear protein-containing complex | 6.43e-06 | BOP1, DHX37, GEMIN5, HEATR1, KRR1, NOL11, NOL6, NOP56, NUP155, NUP205, NUP62, NUP85, NUP93, PDCD11, PES1, SMARCA4, TBL3, UTP15, UTP20, WDR3, WDR36 |
| GO:CC 90S preribosome | 8.28e-06 | BOP1, HEATR1, NOL6, PES1, TBL3, UTP20, WDR3 |
| KEGG Ribosome biogenesis in eukaryotes - Homo sapiens (human) | 2.38e-05 | GNL3, GTPBP4, HEATR1, NOL6, NOP56, TBL3, UTP15, WDR3, WDR36 |
| GO:BP RNA biosynthetic process | 3.4e-05 | BOP1, CNOT1, DDX54, DDX56, DHX37, GEMIN5, GNL3, GTPBP4, HEATR1, KRR1, NKRF, NOL11, NOL6, NOP56, NUP155, NUP62, NUP85, PDCD11, PES1, RRS1, SMARCA4, TBL3, UTP15, UTP20, WDR3, WDR36 |
| GO:BP nucleobase-containing compound biosynthetic process | 5.8e-05 | ADSS2, BOP1, CNOT1, DDX54, DDX56, DHX37, GEMIN5, GNL3, GTPBP4, HEATR1, KRR1, NDUFS2, NKRF, NOL11, NOL6, NOP56, NUP155, NUP62, NUP85, PDCD11, PES1, RRS1, SMARCA4, TBL3, UTP15, UTP20, WDR3, WDR36 |

### STRING and hu.MAP

STRING provides strong supplementary support for a coherent ribosome-biogenesis network: its functional categories repeatedly recover preribosome, rRNA processing, ribosome biogenesis, nucleolus, and ribonucleoprotein-complex biogenesis (STRING NetworkNeighborAL Preribosome, and Ribosome biogenesis; within-query FDR = 6.85e-17)(STRING Process rRNA processing; within-query FDR = 7.09e-12)(STRING Process Ribosome biogenesis; within-query FDR = 9.66e-12)(STRING COMPARTMENTS Nucleolus; within-query FDR = 1.77e-11)(STRING Process Ribonucleoprotein complex biogenesis; within-query FDR = 5.24e-11). The dense STRING relationships among BOP1, GTPBP4, HEATR1, KRR1, NOL6, NOP56, PDCD11, PES1, TBL3, UTP15, UTP20, WDR3, and WDR36 indicate that much of the co-abundance structure corresponds to already recognized functional relationships. A separate, tightly connected group of NUP155, NUP205, NUP62, NUP85, and NUP93 corresponds to nuclear-pore components and is also supported by STRING. hu.MAP independently identifies a nuclear-pore complex containing NUP155, NUP62, and NUP85 (hu.MAP huMAP3_12581.1), complexes containing NUP93 and NUP205 (hu.MAP huMAP3_07789.1)(hu.MAP huMAP3_05673.1)(hu.MAP huMAP3_09042.1), and small-subunit-processome-related complexes containing UTP15 and NOL11 (hu.MAP huMAP3_01743.1)(hu.MAP huMAP3_14264.1). The SPTAN1-SPTBN1 pair is supported by several hu.MAP complexes (hu.MAP huMAP3_07940.1)(hu.MAP huMAP3_05473.1)(hu.MAP huMAP3_09165.1). These results show that the module is not merely a statistical group: it contains established ribosome-biogenesis, nuclear-pore, and cytoskeletal-complex relationships. However, STRING associations are supplementary evidence and do not replace the globally corrected GO and KEGG results.

**STRING interactions (score >= 0.7)**: 164 of 630 gene pairs: BOP1–DDX54 (0.966); BOP1–DDX56 (0.963); BOP1–DHX37 (0.721); BOP1–GNL3 (0.995); BOP1–GTPBP4 (0.996); BOP1–HEATR1 (0.971); BOP1–KRR1 (0.818); BOP1–NOL6 (0.929); BOP1–NOP56 (0.974); BOP1–PDCD11 (0.97); BOP1–PES1 (0.999); BOP1–RRS1 (0.962); BOP1–SURF6 (0.857); BOP1–TBL3 (0.967); BOP1–UTP15 (0.797); BOP1–UTP20 (0.914); BOP1–WDR3 (0.973); BOP1–WDR36 (0.951); DDX54–DDX56 (0.892); DDX54–DHX37 (0.718); DDX54–GNL3 (0.888); DDX54–GTPBP4 (0.804); DDX54–HEATR1 (0.78); DDX54–NOL6 (0.887); DDX54–PDCD11 (0.792); DDX54–PES1 (0.959); DDX54–SURF6 (0.874); DDX54–TBL3 (0.848); DDX54–WDR3 (0.753); DDX54–WDR36 (0.717); DDX56–GNL3 (0.919); DDX56–GTPBP4 (0.978); DDX56–HEATR1 (0.844); DDX56–KRR1 (0.912); DDX56–NOL6 (0.778); DDX56–NOP56 (0.884); DDX56–PDCD11 (0.853); DDX56–PES1 (0.97); DDX56–RRS1 (0.914); DDX56–TBL3 (0.938); DDX56–WDR3 (0.893); DDX56–WDR36 (0.923); DHX37–HEATR1 (0.943); DHX37–KRR1 (0.943); DHX37–NOL11 (0.96); DHX37–NOL6 (0.975); DHX37–NOP56 (0.943); DHX37–PDCD11 (0.96); DHX37–PES1 (0.714); DHX37–TBL3 (0.913); DHX37–UTP15 (0.938); DHX37–UTP20 (0.975); DHX37–WDR3 (0.892); DHX37–WDR36 (0.929); GNL3–GTPBP4 (0.992); GNL3–KRR1 (0.852); GNL3–NOL6 (0.753); GNL3–NOP56 (0.964); GNL3–PDCD11 (0.778); GNL3–PES1 (0.997); GNL3–RRS1 (0.95); GNL3–SMARCA4 (0.878); GNL3–SURF6 (0.794); GNL3–TBL3 (0.773); GNL3–WDR3 (0.857); GNL3–WDR36 (0.854); GTPBP4–HEATR1 (0.933); GTPBP4–KRR1 (0.771); GTPBP4–NOL6 (0.781); GTPBP4–NOP56 (0.941); GTPBP4–PDCD11 (0.928); GTPBP4–PES1 (0.999); GTPBP4–RRS1 (0.99); GTPBP4–SURF6 (0.974); GTPBP4–TBL3 (0.895); GTPBP4–UTP15 (0.832); GTPBP4–UTP20 (0.824); GTPBP4–WDR3 (0.951); GTPBP4–WDR36 (0.947); HEATR1–KRR1 (0.998); HEATR1–NOL11 (0.983); HEATR1–NOL6 (0.999); HEATR1–NOP56 (0.999); HEATR1–PDCD11 (0.999); HEATR1–PES1 (0.877); HEATR1–TBL3 (0.999); HEATR1–UTP15 (0.999); HEATR1–UTP20 (0.999); HEATR1–WDR3 (0.999); HEATR1–WDR36 (0.999); KRR1–NOL11 (0.965); KRR1–NOL6 (0.998); KRR1–NOP56 (0.999); KRR1–PDCD11 (0.999); KRR1–PES1 (0.894); KRR1–RRS1 (0.961); KRR1–SURF6 (0.854); KRR1–TBL3 (0.999); KRR1–UTP15 (0.998); KRR1–UTP20 (0.999); KRR1–WDR3 (0.999); KRR1–WDR36 (0.999); NOL11–NOL6 (0.919); NOL11–NOP56 (0.948); NOL11–PDCD11 (0.87); NOL11–TBL3 (0.913); NOL11–UTP15 (0.986); NOL11–UTP20 (0.979); NOL11–WDR3 (0.951); NOL11–WDR36 (0.936); NOL6–NOP56 (0.998); NOL6–PDCD11 (0.999); NOL6–PES1 (0.86); NOL6–TBL3 (0.999); NOL6–UTP15 (0.998); NOL6–UTP20 (0.999); NOL6–WDR3 (0.999); NOL6–WDR36 (0.999); NOP56–PDCD11 (0.997); NOP56–PES1 (0.956); NOP56–RRS1 (0.848); NOP56–TBL3 (0.999); NOP56–UTP15 (0.999); NOP56–UTP20 (0.997); NOP56–WDR3 (0.999); NOP56–WDR36 (0.999); NUP155–NUP205 (0.999); NUP155–NUP62 (0.997); NUP155–NUP85 (0.998); NUP155–NUP93 (0.999); NUP205–NUP62 (0.998); NUP205–NUP85 (0.998); NUP205–NUP93 (0.999); NUP62–NUP85 (0.995); NUP62–NUP93 (0.999); NUP85–NUP93 (0.999); PDCD11–PES1 (0.969); PDCD11–RRS1 (0.786); PDCD11–TBL3 (0.996); PDCD11–UTP15 (0.987); PDCD11–UTP20 (0.999); PDCD11–WDR3 (0.997); PDCD11–WDR36 (0.998); PES1–RRS1 (0.981); PES1–SURF6 (0.94); PES1–TBL3 (0.935); PES1–UTP20 (0.827); PES1–WDR3 (0.914); PES1–WDR36 (0.928); RRS1–SURF6 (0.949); RRS1–TBL3 (0.757); RRS1–WDR3 (0.789); RRS1–WDR36 (0.7); SPTAN1–SPTBN1 (0.999); TBL3–UTP15 (0.999); TBL3–UTP20 (0.999); TBL3–WDR3 (0.999); TBL3–WDR36 (0.999); UTP15–UTP20 (0.998); UTP15–WDR3 (0.999); UTP15–WDR36 (0.999); UTP20–WDR3 (0.999); UTP20–WDR36 (0.999); WDR3–WDR36 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Preribosome, and Ribosome biogenesis (FDR = 6.85e-17, 20 genes); Process rRNA processing (FDR = 7.09e-12, 18 genes); Process Ribosome biogenesis (FDR = 9.66e-12, 19 genes); COMPARTMENTS Nucleolus (FDR = 1.77e-11, 22 genes); Process Ribonucleoprotein complex biogenesis (FDR = 5.24e-11, 20 genes); Process ncRNA processing (FDR = 5.24e-11, 19 genes); RCTM rRNA modification in the nucleus and cytosol (FDR = 1.11e-10, 12 genes); RCTM Major pathway of rRNA processing in the nucleolus and cytosol (FDR = 1.11e-10, 15 genes); RCTM Metabolism of RNA (FDR = 2.52e-10, 22 genes); Component Nucleolus (FDR = 6.09e-10, 23 genes); NetworkNeighborAL rRNA modification in the nucleus and cytosol (FDR = 1.1e-09, 11 genes); COMPARTMENTS Preribosome (FDR = 1.8e-09, 12 genes); Component Preribosome (FDR = 2.16e-09, 12 genes); COMPARTMENTS Nuclear lumen (FDR = 7.2e-09, 26 genes); Keyword Ribosome biogenesis (FDR = 1.13e-08, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12581.1 (NUP155, NUP62, NUP85; 3/58); huMAP3_07940.1 (SPTBN1, SPTAN1; 2/5); huMAP3_01743.1 (UTP15, NOL11; 2/6); huMAP3_07789.1 (NUP93, NUP205; 2/7); huMAP3_05473.1 (SPTBN1, SPTAN1; 2/7); huMAP3_05673.1 (NUP93, NUP205; 2/11); huMAP3_14264.1 (UTP15, NOL11; 2/20); huMAP3_09042.1 (NUP93, NUP205; 2/26); huMAP3_09165.1 (SPTBN1, SPTAN1; 2/39); huMAP3_11232.1 (UTP20, NUP85; 2/78)

### Novelty

The biological function itself is not a new discovery. Ribosome biogenesis, precursor-rRNA processing, nucleolar localization, nuclear-pore transport, and several component relationships are already well established by the primary annotations, STRING network, hu.MAP complexes, and gene-specific literature. What may be novel is the observation that these genes form one conserved co-abundance module shared by bone and lung, especially the way the dominant nucleolar program is coupled to a nuclear-pore subnetwork in these tissue groups. The available evidence does not establish that this tissue-pair module has never been reported, because absence from a particular interaction or complex database cannot prove novelty. The most defensible conclusion is therefore that this is a potentially novel tissue-level co-abundance organization of a largely known cellular machinery, not a newly discovered molecular pathway.

**Hypothesis.** Hypothesis: the shared bone-lung module reflects coordinated demand for ribosome production and nucleocytoplasmic RNA trafficking in metabolically active or proliferative nucleated cells. In this model, small-subunit-processome and nucleolar factors such as WDR3, UTP15, UTP20, PDCD11, and GNL3 coordinate precursor-rRNA maturation, while the NUP93-NUP205-NUP155-NUP62-NUP85 group supports export of processed ribonucleoprotein particles and import of required nuclear factors. The association with SMARCA4, spectrins, mitochondrial NDUFS2, and redox-related GSR may reflect coupling of ribosome production to chromatin state, cell architecture, energy metabolism, and oxidative protection. This mechanism is plausible from the module composition and annotations, but it remains a hypothesis: co-abundance does not demonstrate physical interaction, causal regulation, or tissue-specific directionality.

### Important genes

#### GNL3

- **Related proteins** (co-abundance neighbors): NUP93 (0.89), SPTBN1 (0.88), SPTAN1 (0.87), RRS1 (0.86), ADSS2 (0.83), PES1 (0.82), GTPBP4 (0.81), NUP85 (0.81); STRING partners: BOP1 (0.995), DDX54 (0.888), DDX56 (0.919), GTPBP4 (0.992), KRR1 (0.852), NOL6 (0.753), NOP56 (0.964), PDCD11 (0.778), PES1 (0.997), RRS1 (0.95), SMARCA4 (0.878), SURF6 (0.794), TBL3 (0.773), WDR3 (0.857), WDR36 (0.854)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein nucleolar 3. The protein encoded by this gene may interact with p53 and may be involved in tumorigenesis. The encoded protein also appears to be important for stem cell proliferation. This protein is found in both the nucleus and nucleolus. Three transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Nov 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.357); Abnormality of the skeletal system (0.264); cataract (0.252); trauma complication (0.245); osteoarthritis (0.155)
- **Europe PMC papers**: 959
- **Why important**: GNL3 is among the more connected module genes and links the nucleolar ribosome-biogenesis cluster to nuclear-pore and spectrin-associated portions of the network. It is annotated to the nucleolus and appears in the primary nucleolus, RNA-processing, and ribosome-biogenesis terms (GO:CC nucleolus; q_global = 2.01e-08)(KEGG Ribosome biogenesis in eukaryotes - Homo sapiens (human); q_global = 2.38e-05)(GO:BP RNA biosynthetic process; q_global = 3.4e-05). Its established descriptions include roles in stem-cell proliferation, telomere maintenance, and interaction with p53, while Open Targets links it to skeletal-system abnormality and osteoarthritis. Its extensive literature makes it a strong integrative marker of the module rather than an isolated peripheral component.
- **Conclusion**: Established evidence supports GNL3 as a nucleolar regulator associated with ribosome production and cell-proliferative state. Its network position supports a bridging role within this module. A specific role for GNL3 in coordinating the bone-lung shared program is a hypothesis, not demonstrated by the fact sheet.

#### WDR3

- **Related proteins** (co-abundance neighbors): TBL3 (0.90), NOP56 (0.85), SURF6 (0.81), CLINT1 (0.80); STRING partners: BOP1 (0.973), DDX54 (0.753), DDX56 (0.893), DHX37 (0.892), GNL3 (0.857), GTPBP4 (0.951), HEATR1 (0.999), KRR1 (0.999), NOL11 (0.951), NOL6 (0.999), NOP56 (0.999), PDCD11 (0.997), PES1 (0.914), RRS1 (0.789), TBL3 (0.999), UTP15 (0.999), UTP20 (0.999), WDR36 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 3. This gene encodes a nuclear protein containing 10 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, which usually include a trp-asp at the C-terminal end. Proteins belonging to the WD repeat family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. [provid…
- **Diseases (Open Targets)**: presbycusis (0.335); respiratory tract infectious disorder (0.184); neurodegenerative disease (0.143); preeclampsia (0.120); alcohol drinking (0.098)
- **Europe PMC papers**: 280
- **Why important**: WDR3 is a highly integrated member of the core ribosome-biogenesis network and is represented across essentially all major primary terms, including rRNA processing, the small-subunit processome, preribosome, nucleolus, and the KEGG ribosome-biogenesis pathway (GO:BP rRNA metabolic process; q_global = 6.74e-12)(GO:BP rRNA processing; q_global = 1.49e-11)(GO:CC preribosome; q_global = 6.66e-11)(GO:BP ribosomal small subunit biogenesis; q_global = 4.6e-09)(GO:CC small-subunit processome; q_global = 6.62e-09)(KEGG Ribosome biogenesis in eukaryotes - Homo sapiens (human); q_global = 2.38e-05). Its annotation directly supports small-subunit rRNA maturation and small-subunit biogenesis. STRING places it in the central nucleolar interaction cluster, and its literature includes links to respiratory tract infectious disorder and neurodegenerative disease.
- **Conclusion**: Established evidence identifies WDR3 as a core small-subunit ribosome-biogenesis factor and a strong functional representative of the module. Its presence does not by itself establish a bone- or lung-specific function, although it is a plausible readout of shared nucleolar activity.

#### UTP20

- **Related proteins** (co-abundance neighbors): HEATR1 (0.81), DDX54 (0.80), PDCD11 (0.80); STRING partners: BOP1 (0.914), DHX37 (0.975), GTPBP4 (0.824), HEATR1 (0.999), KRR1 (0.999), NOL11 (0.979), NOL6 (0.999), NOP56 (0.997), PDCD11 (0.999), PES1 (0.827), TBL3 (0.999), UTP15 (0.998), WDR3 (0.999), WDR36 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11232.1
- **Function (MyGene.info)**: UTP20 small subunit processome component. UTP20 is a component of the U3 small nucleolar RNA (snoRNA) (SNORD3A; MIM 180710) protein complex (U3 snoRNP) and is involved in 18S rRNA processing (Wang et al., 2007 [PubMed 17498821]).[supplied by OMIM, Jun 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.437); bacterial arthritis (0.113); cartilage disease (0.050); corneal ulcer (0.044); breast neoplasm (0.041)
- **Europe PMC papers**: 285
- **Why important**: UTP20 is a nucleolar small-subunit-processome component with strong connections to HEATR1, PDCD11, and the broader rRNA-processing cluster. It participates in primary terms for rRNA processing, small-subunit biogenesis, the small-subunit processome, precursor-rRNA maturation, and cleavage (GO:BP rRNA processing; q_global = 1.49e-11)(GO:BP ribosomal small subunit biogenesis; q_global = 4.6e-09)(GO:CC small-subunit processome; q_global = 6.62e-09)(GO:BP maturation of SSU-rRNA; q_global = 0.000226)(GO:BP maturation of SSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA); q_global = 0.0111)(GO:BP endonucleolytic cleavage of tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA); q_global = 0.0155). Its gene-specific annotation identifies it as part of the U3 snoRNA complex involved in eighteen-S rRNA processing, and its disease associations include neurodegenerative and cartilage-related conditions. It also has supporting hu.MAP membership (hu.MAP huMAP3_11232.1) and broad STRING support.
- **Conclusion**: Established evidence supports UTP20 as a mechanistically direct component of precursor-rRNA processing and small-subunit assembly. Its disease links make it relevant to tissue pathology, but a causal connection to bone or lung phenotypes remains unproven.

#### PDCD11

- **Related proteins** (co-abundance neighbors): NKRF (0.86), NOL6 (0.81), UTP20 (0.80), NUP93 (0.80); STRING partners: BOP1 (0.97), DDX54 (0.792), DDX56 (0.853), DHX37 (0.96), GNL3 (0.778), GTPBP4 (0.928), HEATR1 (0.999), KRR1 (0.999), NOL11 (0.87), NOL6 (0.999), NOP56 (0.997), PES1 (0.969), RRS1 (0.786), TBL3 (0.996), UTP15 (0.987), UTP20 (0.999), WDR3 (0.997), WDR36 (0.998)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 11. PDCD11 is a NF-kappa-B (NFKB1; 164011)-binding protein that colocalizes with U3 RNA (MIM 180710) in the nucleolus and is required for rRNA maturation and generation of 18S rRNA (Sweet et al., 2003 [PubMed 14624448]; Sweet et al., 2008 [PubMed 17654514]).[supplied by OMIM, Oct 2008].
- **Diseases (Open Targets)**: Back pain (0.277); insomnia (0.216); systemic lupus erythematosus (0.170); neoplasm (0.095); colorectal carcinoma (0.093)
- **Europe PMC papers**: 334
- **Why important**: PDCD11 occupies a bridging position between the nucleolar ribosome-biogenesis cluster and the nuclear-pore-associated part of the module. It is present in the primary rRNA-processing, ribonucleoprotein-biogenesis, nucleolar, and RNA-processing terms (GO:BP rRNA metabolic process; q_global = 6.74e-12)(GO:BP rRNA processing; q_global = 1.49e-11)(GO:BP ribonucleoprotein complex biogenesis; q_global = 6.87e-10)(GO:CC nucleolus; q_global = 2.01e-08)(GO:BP RNA processing; q_global = 5.77e-06). The gene-specific evidence describes binding to NF-kappa-B, colocalization with U3 RNA, a requirement for rRNA maturation and eighteen-S rRNA generation, and participation in cleavage of the precursor-rRNA transcript. Its literature is substantial and includes associations with systemic lupus erythematosus, back pain, and neoplasia.
- **Conclusion**: Established evidence supports PDCD11 as a direct nucleolar rRNA-maturation factor and a plausible connector between core processing machinery and broader nuclear organization. Its connection to inflammatory or tissue disease should be treated as association rather than proof that it drives the shared module.

#### NUP93

- **Related proteins** (co-abundance neighbors): GNL3 (0.89), NUP155 (0.87), NUP205 (0.83), RRS1 (0.83), PDCD11 (0.80); STRING partners: NUP155 (0.999), NUP205 (0.999), NUP62 (0.999), NUP85 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_07789.1, huMAP3_05673.1, huMAP3_09042.1
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 represents the nuclear-pore arm of the module and connects that arm to GNL3, RRS1, PDCD11, and other module genes. It is included in primary terms for cellular-component biogenesis, nuclear-pore structure, nuclear-pore organization, and nucleocytoplasmic transport (GO:BP cellular component biogenesis; q_global = 4.48e-06)(GO:CC nuclear protein-containing complex; q_global = 6.43e-06)(GO:CC nuclear membrane; q_global = 0.00442)(GO:MF structural constituent of nuclear pore; q_global = 0.00463). STRING shows strong relationships with NUP155, NUP205, NUP62, and NUP85, while hu.MAP places it in several complexes with NUP205 (hu.MAP huMAP3_07789.1)(hu.MAP huMAP3_05673.1)(hu.MAP huMAP3_09042.1). Its established functions include nuclear import, RNA export, and nuclear-pore assembly, and its disease associations include nephrotic syndromes and viral disease.
- **Conclusion**: Established evidence supports NUP93 as a structural and transport component of the nuclear-pore subnetwork. Its co-abundance with nucleolar factors suggests coordinated nuclear organization, but it does not prove that NUP93 directly regulates ribosome biogenesis in these tissues.

#### BOP1

- **Related proteins** (co-abundance neighbors): UTP15 (0.81); STRING partners: DDX54 (0.966), DDX56 (0.963), DHX37 (0.721), GNL3 (0.995), GTPBP4 (0.996), HEATR1 (0.971), KRR1 (0.818), NOL6 (0.929), NOP56 (0.974), PDCD11 (0.97), PES1 (0.999), RRS1 (0.962), SURF6 (0.857), TBL3 (0.967), UTP15 (0.797), UTP20 (0.914), WDR3 (0.973), WDR36 (0.951)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BOP1 ribosomal biogenesis factor. Enables RNA binding activity. Involved in regulation of cell cycle; regulation of signal transduction by p53 class mediator; and ribosomal large subunit biogenesis. Located in chromosome; nucleolus; and nucleoplasm. Part of PeBoW complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.318); cancer (0.090); neoplasm (0.087); polycystic ovary syndrome (0.082); colorectal carcinoma (0.078)
- **Europe PMC papers**: 1064
- **Why important**: BOP1 is a central member of the dense STRING-supported nucleolar cluster and is part of the PeBoW complex with PES1 and WDR12 according to the supplied annotation. It appears in primary terms for rRNA metabolic process, rRNA processing, preribosome, ribosome biogenesis, large- and small-subunit-related maturation, and cleavage (GO:BP rRNA metabolic process; q_global = 6.74e-12)(GO:BP rRNA processing; q_global = 1.49e-11)(GO:CC preribosome; q_global = 6.66e-11)(GO:BP ribosome biogenesis; q_global = 1.05e-10)(GO:CC 90S preribosome; q_global = 8.28e-06)(GO:BP endonucleolytic cleavage of tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA); q_global = 0.0155). Its established functions include large-subunit assembly, precursor-rRNA cleavage, cell-cycle regulation, and regulation of p53-class signaling. It has a substantial literature and disease links involving cancer, neoplasia, and polycystic ovary syndrome.
- **Conclusion**: Established evidence supports BOP1 as a core ribosome-biogenesis factor and a representative of the module's dominant biological signal. Its association with proliferative disease makes it biologically important, but the module does not establish a causal role for BOP1 in either bone or lung.

## Module 7

**Tissue pair**: bone and lung  
**Genes (13)**: CLUH, GMPS, HSPH1, EIF4G1, KPNA2, IMPDH2, IPO4, MSH2, MSH6, NASP, PFAS, CTPS1, SMC4

### Function

The strongest functional interpretation is nucleotide biosynthesis centered on glutamine use. (GO:BP glutamine metabolic process; q_global = 0.0252) is the only GO/KEGG term passing global correction and links CTPS1, GMPS, and PFAS to glutamine metabolic process. This is biologically coherent: PFAS uses glutamine in de novo purine synthesis, GMPS uses glutamine in GMP production, and CTPS1 uses glutamine in CTP production. The STRING evidence supports a connected purine/nucleotide module through the high-confidence relationships among CTPS1, GMPS, IMPDH2, and PFAS (STRING Keyword Glutamine amidotransferase; within-query FDR = 0.0057)(STRING Keyword Purine biosynthesis; within-query FDR = 0.0122)(STRING InterPro Class I glutamine amidotransferase-like; within-query FDR = 0.0127)(STRING Keyword GMP biosynthesis; within-query FDR = 0.0345). A secondary layer involves nuclear transport, chromatin assembly, translation, stress protection, and genome maintenance, represented by IPO4, NASP, KPNA2, EIF4G1, HSPH1, SMC4, MSH2, and MSH6. The MSH2–MSH6 pair specifically supports mismatch-repair activity, but this is supplementary evidence rather than globally significant GO/KEGG enrichment.

**Cell composition.** The module is not dominated by plasma or secreted proteins: HPA reports no secreted genes, and the proteins are predominantly intracellular. Most genes have low tissue specificity, while several show cell-type enhancement in erythrocyte progenitors and germ-cell populations. HPA also identifies tissue enhancement in testis for GMPS, IPO4, and KPNA2, lymphoid-tissue enhancement for SMC4, and immune-cell enhancement for only a limited subset. The repeated erythrocyte-progenitor signal, together with broadly expressed biosynthetic, translation, chromatin, and stress-response genes, means the bone–lung association could partly reflect shared proliferative or blood-related cellular composition rather than a tissue-specific pathway. Lung protein detection is widespread among the module genes, whereas bone has no matching HPA tissue result, so the available protein evidence does not establish bone-specific expression.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP glutamine metabolic process | 0.0252 | CTPS1, GMPS, PFAS |

### STRING and hu.MAP

STRING contains established high-confidence relationships within the module. The strongest connected biochemical core is CTPS1–GMPS–IMPDH2–PFAS, with GMPS linked to IPO4, and the DNA-repair pair MSH2–MSH6 is also strongly supported. IPO4–NASP is supported as a nuclear transport or chromatin-associated relationship. hu.MAP identifies NASP and IPO4 together across several histone, chromatin-assembly, and replication-associated complexes (hu.MAP huMAP3_05517.1)(hu.MAP huMAP3_06020.1)(hu.MAP huMAP3_08143.1)(hu.MAP huMAP3_09859.1)(hu.MAP huMAP3_10747.1)(hu.MAP huMAP3_12711.1), while PFAS and HSPH1 co-occur in a lower-confidence chaperone-associated complex (hu.MAP huMAP3_13774.1). These results show that important parts of the module recapitulate known biochemical and physical interaction neighborhoods. They do not demonstrate that all module genes form one physical complex; instead, the network appears to join a nucleotide-metabolism core with nuclear, chromatin, translation, and stress-response components.

**STRING interactions (score >= 0.7)**: 6 of 78 gene pairs: CTPS1–GMPS (0.96); CTPS1–IMPDH2 (0.927); GMPS–IMPDH2 (0.998); GMPS–IPO4 (0.861); IPO4–NASP (0.775); MSH2–MSH6 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Glutamine amidotransferase (FDR = 0.0057, 3 genes); TISSUES Testis (FDR = 0.0063, 10 genes); TISSUES Female reproductive gland (FDR = 0.0101, 11 genes); Keyword Purine biosynthesis (FDR = 0.0122, 3 genes); InterPro Class I glutamine amidotransferase-like (FDR = 0.0127, 3 genes); TISSUES Blood cancer cell (FDR = 0.0234, 8 genes); TISSUES Right colon (FDR = 0.0234, 2 genes); Keyword Hereditary nonpolyposis colorectal cancer (FDR = 0.0277, 2 genes); Keyword GMP biosynthesis (FDR = 0.0345, 2 genes); Keyword ATP-binding (FDR = 0.0446, 7 genes); SMART DNA-binding domain of DNA mismatch repair MUTS family (FDR = 0.0496, 2 genes); SMART ATPase domain of DNA mismatch repair MUTS family (FDR = 0.0496, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05517.1 (NASP, IPO4; 2/13); huMAP3_06020.1 (NASP, IPO4; 2/13); huMAP3_08143.1 (NASP, IPO4; 2/21); huMAP3_09859.1 (NASP, IPO4; 2/24); huMAP3_10747.1 (NASP, IPO4; 2/25); huMAP3_13774.1 (PFAS, HSPH1; 2/33); huMAP3_12711.1 (NASP, IPO4; 2/35)

### Novelty

The conserved bone–lung co-abundance module may be a new cross-tissue network observation, but the biological relationships within it are not broadly novel. The purine and glutamine-utilization relationships are supported by established STRING links, the MSH2–MSH6 mismatch-repair pair is well established, and NASP–IPO4 recur in multiple hu.MAP chromatin-related complexes. Therefore, absence of a complete matching module in STRING or hu.MAP would not by itself prove novelty. The defensible novelty claim is that these known processes co-vary in this particular bone–lung module and may be conserved across the two tissue groups. That claim requires independent replication, control for cell composition and proliferation, and preferably experimental or longitudinal validation before being considered a new mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared proliferative and biosynthetic state present in cellular populations sampled from bone and lung. In this state, glutamine-supported purine and GMP production through PFAS, IMPDH2, and GMPS is coordinated with CTP production through CTPS1, while IPO4, NASP, and KPNA2 support nuclear import and chromatin handling. SMC4 and the MSH2–MSH6 pair could maintain chromosome organization and mismatch surveillance, whereas HSPH1 and EIF4G1 could buffer proteotoxic and translational demands. The erythrocyte-progenitor and germ-cell enrichment signals suggest that shared cellular composition or a common high-proliferation program may generate the cross-tissue co-abundance pattern. This is a mechanistic hypothesis, not a demonstrated causal pathway.

### Important genes

#### PFAS

- **Related proteins** (co-abundance neighbors): IMPDH2 (0.90), GMPS (0.87), IPO4 (0.86), HSPH1 (0.84), KPNA2 (0.83), CTPS1 (0.83), CLUH (0.83), SMC4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_13774.1
- **Function (MyGene.info)**: phosphoribosylformylglycinamidine synthase. Purines are necessary for many cellular processes, including DNA replication, transcription, and energy metabolism. Ten enzymatic steps are required to synthesize inosine monophosphate (IMP) in the de novo pathway of purine biosynthesis. The enzyme encoded by this gene catalyzes the fourth step of IMP biosynthesis. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: dyskeratosis congenita (0.520); Coats plus syndrome (0.455); neurodegenerative disease (0.187); hereditary disease (0.174); retinal disorder (0.118)
- **Europe PMC papers**: 3393
- **Why important**: PFAS is the most network-connected member in the supplied subgraph and links the nucleotide-metabolism core to HSPH1, KPNA2, CLUH, SMC4, and IPO4. It is part of the globally significant glutamine-metabolism signal (GO:BP glutamine metabolic process; q_global = 0.0252), is annotated as the glutamine-dependent enzyme catalyzing a step in de novo IMP synthesis, and participates in the STRING glutamine-amidotransferase and purine-biosynthesis signals (STRING Keyword Glutamine amidotransferase; within-query FDR = 0.0057)(STRING Keyword Purine biosynthesis; within-query FDR = 0.0122)(STRING InterPro Class I glutamine amidotransferase-like; within-query FDR = 0.0127). Its HPA profile is broadly expressed with erythrocyte-progenitor enhancement and lung protein detection. Its disease associations include dyskeratosis congenita and Coats plus syndrome, and it has substantial literature support.
- **Conclusion**: Established evidence supports PFAS as a central biochemical and network component of the module. Its role as an organizer of the entire cross-tissue module remains a hypothesis because co-abundance and network connectivity do not establish causal control.

#### GMPS

- **Related proteins** (co-abundance neighbors): IPO4 (0.89), PFAS (0.87), IMPDH2 (0.85), KPNA2 (0.80); STRING partners: CTPS1 (0.96), IMPDH2 (0.998), IPO4 (0.861)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: guanosine monophosphate synthase. In the de novo synthesis of purine nucleotides, IMP is the branch point metabolite at which point the pathway diverges to the synthesis of either guanine or adenine nucleotides. In the guanine nucleotide pathway, there are 2 enzymes involved in converting IMP to GMP, namely IMP dehydrogenase (IMPD1), which catalyzes the oxidation of IMP to XMP, and GMP synthetase, which catalyzes the amination of …
- **Diseases (Open Targets)**: rheumatoid arthritis (0.277); nephrotic syndrome (0.259); lupus nephritis (0.259); rhabdomyosarcoma (0.247); hepatocellular carcinoma (0.237)
- **Europe PMC papers**: 5161
- **Why important**: GMPS is embedded in the strongest biochemical interaction core, connecting CTPS1, IMPDH2, PFAS, IPO4, and KPNA2. It is one of the genes in the globally significant glutamine-metabolism term (GO:BP glutamine metabolic process; q_global = 0.0252) and is supported by multiple supplementary purine, GMP, and glutamine-amidotransferase annotations (STRING Keyword Glutamine amidotransferase; within-query FDR = 0.0057)(STRING TISSUES Testis; within-query FDR = 0.0063)(STRING TISSUES Female reproductive gland; within-query FDR = 0.0101)(STRING Keyword Purine biosynthesis; within-query FDR = 0.0122)(STRING InterPro Class I glutamine amidotransferase-like; within-query FDR = 0.0127)(STRING Keyword GMP biosynthesis; within-query FDR = 0.0345). Its established function is conversion of XMP to GMP in the guanine-nucleotide branch of de novo purine synthesis. It is testis-enhanced and enriched in spermatogenic cell types, with disease associations including rheumatoid arthritis, lupus nephritis, and hepatocellular carcinoma, and extensive literature support.
- **Conclusion**: Established evidence identifies GMPS as a key enzymatic bridge between glutamine use and guanine-nucleotide production. Its testis and germ-cell pattern may reflect a proliferative cellular program, but it does not establish that germ-cell biology drives the bone–lung module.

#### CTPS1

- **Related proteins** (co-abundance neighbors): PFAS (0.83); STRING partners: GMPS (0.96), IMPDH2 (0.927)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CTP synthase 1. This gene encodes an enzyme responsible for the catalytic conversion of UTP (uridine triphosphate) to CTP (cytidine triphospate). This reaction is an important step in the biosynthesis of phospholipids and nucleic acids. Activity of this proten is important in the immune system, and loss of function of this gene has been associated with immunodeficiency. Alternative splicing results in multiple tr…
- **Diseases (Open Targets)**: combined immunodeficiency due to CTPS1 deficiency (0.712); androgenetic alopecia (0.204); hyperpituitarism (0.195); urolithiasis (0.097); alcohol drinking (0.097)
- **Europe PMC papers**: 641
- **Why important**: CTPS1 belongs to the globally significant glutamine-metabolism gene set (GO:BP glutamine metabolic process; q_global = 0.0252) and is connected in STRING to GMPS and IMPDH2 (STRING Keyword Glutamine amidotransferase; within-query FDR = 0.0057)(STRING TISSUES Female reproductive gland; within-query FDR = 0.0101)(STRING InterPro Class I glutamine amidotransferase-like; within-query FDR = 0.0127). Its established function is glutamine-dependent CTP production, linking pyrimidine synthesis with the purine-centered biochemical core. CTPS1 is important for immune function, and loss of function is associated with combined immunodeficiency. It is broadly expressed, shows cell-type enhancement in hepatocytes and salivary acinar cells, is detected in lung, and has a substantial disease and literature record.
- **Conclusion**: Established evidence supports CTPS1 as the module component that extends the nucleotide-biosynthesis interpretation beyond purines into pyrimidine metabolism. Its contribution to a shared proliferative state is plausible but remains a hypothesis.

#### MSH2

- **Related proteins** (co-abundance neighbors): MSH6 (0.86); STRING partners: MSH6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutS homolog 2. This locus is frequently mutated in hereditary nonpolyposis colon cancer (HNPCC). When cloned, it was discovered to be a human homolog of the E. coli mismatch repair gene mutS, consistent with the characteristic alterations in microsatellite sequences (RER+ phenotype) found in HNPCC. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: Lynch syndrome (0.891); colorectal cancer (0.776); mismatch repair cancer syndrome (0.775); Muir-Torre syndrome (0.752); mismatch repair cancer syndrome 1 (0.740)
- **Europe PMC papers**: 22581
- **Why important**: MSH2 forms the high-confidence MSH2–MSH6 relationship (STRING TISSUES Blood cancer cell; within-query FDR = 0.0234)(STRING TISSUES Right colon; within-query FDR = 0.0234)(STRING Keyword Hereditary nonpolyposis colorectal cancer; within-query FDR = 0.0277)(STRING SMART DNA-binding domain of DNA mismatch repair MUTS family; within-query FDR = 0.0496)(STRING SMART ATPase domain of DNA mismatch repair MUTS family; within-query FDR = 0.0496), and the pair is annotated for mismatch repair and hereditary nonpolyposis colorectal cancer. MSH2 is a core mismatch-repair protein with extensive disease and literature support, including Lynch syndrome and related mismatch-repair cancer syndromes. Its HPA profile is broadly expressed with enhancement in erythrocyte progenitors and lung protein detection. Its position connects the module to genome surveillance rather than directly to the glutamine-metabolism core.
- **Conclusion**: Established evidence supports MSH2 as a marker of mismatch-repair capacity within the module, especially together with MSH6. The reason mismatch repair co-abundances with nucleotide synthesis in bone and lung is unresolved; a connection through DNA replication or proliferative demand is a hypothesis.

#### NASP

- **Related proteins** (co-abundance neighbors): EIF4G1 (0.82); STRING partners: IPO4 (0.775)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_05517.1, huMAP3_06020.1, huMAP3_08143.1, huMAP3_09859.1, huMAP3_10747.1, huMAP3_12711.1
- **Function (MyGene.info)**: nuclear autoantigenic sperm protein. This gene encodes a H1 histone binding protein that is involved in transporting histones into the nucleus of dividing cells. Multiple isoforms are encoded by transcript variants of this gene. The somatic form is expressed in all mitotic cells, is localized to the nucleus, and is coupled to the cell cycle. The testicular form is expressed in embryonic tissues, tumor cells, and the testis. In male g…
- **Diseases (Open Targets)**: neurodegenerative disease (0.445); Paralytic ileus (0.301); glioma (0.080); central nervous system cancer (0.080); hepatocellular carcinoma (0.076)
- **Europe PMC papers**: 1349
- **Why important**: NASP participates with IPO4 in several hu.MAP chromatin and histone-associated complexes (hu.MAP huMAP3_05517.1)(hu.MAP huMAP3_06020.1)(hu.MAP huMAP3_08143.1)(hu.MAP huMAP3_09859.1)(hu.MAP huMAP3_10747.1)(hu.MAP huMAP3_12711.1), and it is linked to IPO4 in STRING. Its established function is histone transport and DNA replication-dependent chromatin assembly, providing a mechanistic bridge to the module's nuclear and genome-maintenance features. NASP is broadly expressed, shows enhancement in differentiating spermatogonia, primary spermatocytes, and erythrocyte progenitors, and is detected in lung. Its disease associations include neurodegenerative disease and selected cancers, with a substantial literature base.
- **Conclusion**: Established evidence supports NASP as a chromatin-assembly and histone-handling component that helps explain the module's nuclear layer. Its co-abundance with the nucleotide-metabolism core may indicate coordinated support of DNA replication, but this causal interpretation remains a hypothesis.

## Module 8

**Tissue pair**: bone and lung  
**Genes (5)**: ELOC, PNPO, PPM1A, PRRC2C, RBM12

### Function

The module does not support a specific canonical function from enrichment: no GO or KEGG term passed global correction, and STRING supplied neither functional enrichment nor supplementary terms. Its topology instead suggests a mixed intracellular regulatory module centered on PPM1A, with links to stress-granule biology through PRRC2C, RNA-related regulation through RBM12, vitamin B6 biosynthesis through PNPO, and transcriptional elongation and ubiquitin-dependent regulation through ELOC. These annotations are biologically plausible at the gene level but should not be treated as an enriched shared pathway. The module may therefore represent coordinated abundance of broadly distributed regulatory proteins rather than a well-defined biochemical complex.

**Cell composition.** The module is not dominated by secreted or plasma proteins, and all genes have low immune-cell specificity in HPA. Thus, the evidence does not favor a blood-cell or circulating-protein explanation. Most genes show low tissue specificity, while the tissue-enhanced signals point separately toward bone marrow and liver rather than a shared bone-lung lineage. Cell-type-enhanced signals include reproductive and specialized epithelial or neural-associated cell types, but these are heterogeneous and do not establish a common cell population in bone and lung. Protein detection in lung is present for most assessed genes, whereas matching HPA tissue evidence is unavailable for bone. Overall, the composition is more consistent with broadly expressed intracellular proteins, with possible sample or cellular-composition effects, than with a tissue-specific secretory module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair in the module has a high-confidence STRING interaction, and no hu.MAP complex contains multiple module members. Consequently, the co-abundance edges are not supported as already established physical or functional interactions by these resources. PPM1A is the network hub, connecting PRRC2C, RBM12, and PNPO, while RBM12 connects onward to ELOC. This structure may reflect coordinated regulation or shared abundance patterns, but it does not demonstrate a physical complex or a single linear pathway.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is a potentially interesting co-abundance observation because its internal edges are not represented by the supplied high-confidence STRING or hu.MAP evidence and because no canonical enrichment explains the grouping. However, it cannot be called a new biological pathway or a novel physical complex. Database absence can reflect incomplete coverage, context dependence, tissue-specific regulation, or technical limitations. The strongest defensible claim is that this particular bone-lung co-abundance configuration appears insufficiently characterized and requires replication, comparison with independent cohorts, and orthogonal interaction or perturbation experiments.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of intracellular stress and gene-expression regulators rather than one stable multiprotein complex. PPM1A could provide a regulatory connection through stress-responsive phosphatase activity; PRRC2C could relate that state to stress-granule assembly and translational control; RBM12 and ELOC could couple RNA processing or transcriptional elongation with protein turnover; and PNPO could indicate a metabolic or vitamin B6-related component. A shared cellular stress or remodeling state in bone and lung could therefore produce the observed co-abundance pattern. This is a hypothesis only, because the module lacks globally significant enrichment, STRING support, and hu.MAP complex support.

### Important genes

#### PPM1A

- **Related proteins** (co-abundance neighbors): PRRC2C (0.87), RBM12 (0.80), PNPO (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase, Mg2+/Mn2+ dependent 1A. The protein encoded by this gene is a member of the PP2C family of Ser/Thr protein phosphatases. PP2C family members are known to be negative regulators of cell stress response pathways. This phosphatase dephosphorylates, and negatively regulates the activities of, MAP kinases and MAP kinase kinases. It has been shown to inhibit the activation of p38 and JNK kinase cascades induced by environmenta…
- **Diseases (Open Targets)**: neurodegenerative disease (0.446); Hypoxemia (0.241); asphyxia (0.241); hair color (0.225); nephrotic syndrome (0.196)
- **Europe PMC papers**: 1198
- **Why important**: PPM1A is the central network hub, connecting three other module members and having the strongest apparent network position. It is a PP2C-family serine/threonine phosphatase that negatively regulates stress-response pathways, including MAP kinase signaling, and is also linked to regulation of transcription, transforming growth factor beta receptor signaling, and NF-kappaB signaling. Its lung protein detection, bone-marrow tissue enhancement, disease associations, and substantial literature make it the most informative candidate for testing whether the module has a stress-regulatory core.
- **Conclusion**: Established: PPM1A is a stress-responsive regulatory phosphatase with the central position in this module. Hypothesis: its coordinated abundance with the other genes may mark a shared stress-signaling state in bone and lung, but the network does not establish direct molecular binding or causality.

#### PRRC2C

- **Related proteins** (co-abundance neighbors): PPM1A (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proline rich coiled-coil 2C. Enables protein C-terminus binding activity. Involved in stress granule assembly. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.425); neurodegenerative disease (0.387); mathematical ability (0.278); alcohol drinking (0.250); intelligence (0.209)
- **Europe PMC papers**: 327
- **Why important**: PRRC2C is directly connected to the PPM1A hub and has an annotated role in cytoplasmic stress-granule assembly and regulation of cytoplasmic translation. It provides the clearest mechanistic link between the network hub and a cellular stress or translational-control interpretation. Its skeletal-system abnormality association and literature support add relevance to the bone context, although its tissue specificity is low.
- **Conclusion**: Established: PRRC2C participates in stress-granule and translational regulation according to the supplied annotations. Hypothesis: it may connect PPM1A-associated stress signaling to post-transcriptional control in the shared module; this relationship is not validated as a physical interaction.

#### RBM12

- **Related proteins** (co-abundance neighbors): PPM1A (0.80), ELOC (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Not detected; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 12. This gene encodes a protein that contains several RNA-binding motifs, potential transmembrane domains, and proline-rich regions. This gene and the gene for copine I overlap at map location 20q11.21. Alternative splicing in the 5' UTR results in four transcript variants. All variants encode the same protein. [provided by RefSeq, Nov 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.518); schizophrenia (0.462); schizophrenia 19 (0.437); lysosomal storage disease (0.221); Neurodevelopmental delay (0.119)
- **Europe PMC papers**: 272
- **Why important**: RBM12 occupies the intermediate position between PPM1A and ELOC, making it a potential bridge between phosphatase-related regulation and transcriptional machinery. Its annotations include RNA-binding features and regulation of RNA splicing, while its disease associations include neurodevelopmental and psychiatric conditions. Its literature base is meaningful, and its lung detection supports the possibility that it contributes to a broadly expressed intracellular program.
- **Conclusion**: Established: RBM12 is an RNA-associated protein annotated in RNA-splicing regulation and lies on the module's internal bridge. Hypothesis: RBM12 could transmit a stress or signaling state into RNA processing or transcript-selective regulation, but this proposed role in the module remains untested.

#### PNPO

- **Related proteins** (co-abundance neighbors): PPM1A (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyridoxamine 5'-phosphate oxidase. The enzyme encoded by this gene catalyzes the terminal, rate-limiting step in the synthesis of pyridoxal 5'-phosphate, also known as vitamin B6. Vitamin B6 is a required co-factor for enzymes involved in both homocysteine metabolism and synthesis of neurotransmitters such as catecholamine. Mutations in this gene result in pyridoxamine 5'-phosphate oxidase (PNPO) deficiency, a form of neonatal epil…
- **Diseases (Open Targets)**: pyridoxal phosphate-responsive seizures (0.806); hereditary disease (0.485); Seizure (0.401); neuronopathy, distal hereditary motor, type 5A (0.340); fetal growth restriction (0.333)
- **Europe PMC papers**: 20173
- **Why important**: PNPO is directly linked to PPM1A and encodes the terminal enzyme in pyridoxal phosphate biosynthesis, connecting the module to vitamin B6 metabolism. It has a liver-enhanced tissue pattern, specialized-cell expression signals, lung protein detection, and a strong disease association with pyridoxal-phosphate-responsive seizures. Its very substantial literature makes it an important anchor for evaluating whether the module includes a metabolic component rather than being purely regulatory.
- **Conclusion**: Established: PNPO is a vitamin B6 pathway enzyme with a well-defined metabolic function and disease relevance. Hypothesis: its co-abundance with PPM1A may reflect metabolic support for stress-responsive signaling or cellular remodeling, but no enrichment evidence supports a shared vitamin B6 pathway for the module as a whole.

#### ELOC

- **Related proteins** (co-abundance neighbors): RBM12 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: elongin C. This gene encodes the protein elongin C, which is a subunit of the transcription factor B (SIII) complex. The SIII complex is composed of elongins A/A2, B and C. It activates elongation by RNA polymerase II by suppressing transient pausing of the polymerase at many sites within transcription units. Elongin A functions as the transcriptionally active component of the SIII complex, whereas elongins …
- **Diseases (Open Targets)**: HIV infectious disease (0.588); metabolic disease (0.269); Hypercholesterolemia (0.180); renal cell carcinoma (0.104); neoplasm (0.085)
- **Europe PMC papers**: 817
- **Why important**: ELOC is the terminal member of the RBM12 branch and encodes elongin C, a regulatory component of the RNA polymerase II transcription-elongation machinery. It is also annotated in protein ubiquitination and proteasome-mediated protein catabolism. Its position gives the module a possible connection to transcriptional output and protein turnover, while its literature support and specialized-cell expression make it useful for testing whether the signal involves cell-state regulation.
- **Conclusion**: Established: ELOC participates in transcriptional elongation and ubiquitin-dependent regulatory processes. Hypothesis: ELOC may link RNA-associated regulation through RBM12 to transcription and protein-quality control, but the module does not demonstrate a shared elongin complex or direct interaction among these proteins.

## Module 9

**Tissue pair**: bone and lung  
**Genes (6)**: AHCTF1, MYEF2, PHIP, SMARCA1, TOP2A, ZNF638

### Function

This is best interpreted as a nuclear regulatory and genome-maintenance module. Its genes collectively implicate chromatin remodeling, nuclear organization, transcriptional regulation, DNA topology, cytokinesis, and chromosome handling. SMARCA1 is the principal network connector, linking AHCTF1, TOP2A, and MYEF2, while AHCTF1 connects to PHIP and ZNF638. TOP2A provides a strong link to DNA replication, chromosome segregation, and the DNA-damage response. PHIP supports chromatin organization, transcriptional regulation, signal transduction, and growth-related biology. AHCTF1 supports nuclear-pore assembly and cytokinesis, while MYEF2 and ZNF638 support nuclear RNA or transcriptional regulation. No GO or KEGG term passed global correction. Therefore, the proposed function is based on the individual gene annotations and the co-abundance topology, not on significant module-level enrichment.

**Cell composition.** The module consists of intracellular nuclear proteins rather than plasma or secreted proteins; HPA identifies no secreted genes. All module proteins were detected in lung, while no matching HPA bone tissue result is available. Most genes have low tissue specificity, and most have cell-type-enhanced profiles. Several genes show immune-cell enhancement involving neutrophils or T-cell populations, and TOP2A is enhanced in lymphoid tissue and proliferative progenitor or germ-cell populations. Thus, shared abundance may partly reflect nuclear activity in proliferating or immune-associated cells present in the samples, rather than a bone-and-lung-specific program. The HPA evidence does not support a plasma-protein or secreted-protein explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction was detected among the module gene pairs at the stated confidence threshold, and STRING functional enrichment was absent. This weakens the case that the co-abundance pattern represents a well-established physical interaction network, although it does not invalidate coordinated regulation or shared cellular-state effects. The hu.MAP evidence provides one partial complex connection: (hu.MAP huMAP3_07289.1) contains TOP2A and PHIP among its module members, with TOP2B and ZNF451 as other complex members. This supports a possible physical or functional relationship between TOP2A and PHIP, but the partial membership and intermediate complex confidence do not establish that the whole module is a single complex. The remaining module relationships lack support from the reported STRING and hu.MAP resources.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07289.1 (TOP2A, PHIP; 2/4)

### Novelty

The conserved bone-lung co-abundance pattern may represent a previously unreported cross-tissue association, but the available evidence is insufficient to call it a new biological mechanism. Its novelty is suggested by the absence of reported STRING interactions and by the limited hu.MAP overlap, yet absence from those databases alone does not prove novelty. The lack of globally significant GO or KEGG enrichment and the possible contribution of shared proliferative or immune-associated cell states further limit a strong novelty claim. A defensible conclusion is that this is a potentially novel co-abundance module whose biological specificity requires replication and independent validation.

**Hypothesis.** Hypothesis: the module reflects coordinated nuclear activity in a shared proliferative or immune-associated cell state present in bone and lung samples. In this model, SMARCA1 could coordinate chromatin accessibility and transcription, AHCTF1 could couple nuclear pore or cytokinesis functions to that state, TOP2A could manage DNA topology and chromosome dynamics, and PHIP could connect chromatin regulation with signaling and cell growth. MYEF2 and ZNF638 could contribute cell-state-dependent transcriptional or RNA processing regulation. The partial hu.MAP relationship between TOP2A and PHIP is consistent with, but does not prove, this mechanism. Testing should determine whether module abundance tracks proliferation, immune-cell composition, chromatin activity, or direct protein interactions.

### Important genes

#### SMARCA1

- **Related proteins** (co-abundance neighbors): AHCTF1 (0.88), TOP2A (0.88), MYEF2 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SNF2 related chromatin remodeling ATPase 1. This gene encodes a member of the SWI/SNF family of proteins. The encoded protein is an ATPase which is expressed in diverse tissues and contributes to the chromatin remodeling complex that is involved in transcription. The protein may also play a role in DNA damage, growth inhibition and apoptosis of cancer cells. Alternative splicing results in multiple transcript variants. [provided by RefSeq, …
- **Diseases (Open Targets)**: neurodevelopmental disorder (0.423); X-linked intellectual disability (0.401); non-syndromic X-linked intellectual disability (0.333); Abnormal brain morphology (0.266); cancer (0.211)
- **Europe PMC papers**: 924
- **Why important**: SMARCA1 has the strongest connector role in the module and links three other members. It is a SWI/SNF-family chromatin-remodeling ATPase with annotations in chromatin remodeling, transcriptional regulation, heterochromatin formation, development, and apoptosis-related biology. Its substantial literature and disease associations involving neurodevelopment and cancer make it a strong functional anchor.
- **Conclusion**: Established evidence supports SMARCA1 as a chromatin and transcriptional regulator and as the central network connector. It is plausible, but unproven, that SMARCA1 coordinates the module's shared abundance.

#### TOP2A

- **Related proteins** (co-abundance neighbors): SMARCA1 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_07289.1
- **Function (MyGene.info)**: DNA topoisomerase II alpha. This gene encodes a DNA topoisomerase, an enzyme that controls and alters the topologic states of DNA during transcription. This nuclear enzyme is involved in processes such as chromosome condensation, chromatid separation, and the relief of torsional stress that occurs during DNA transcription and replication. It catalyzes the transient breaking and rejoining of two strands of duplex DNA which al…
- **Diseases (Open Targets)**: neoplasm (0.618); breast cancer (0.616); acute myeloid leukemia (0.606); plasma cell myeloma (0.594); small cell lung carcinoma (0.580)
- **Europe PMC papers**: 11752
- **Why important**: TOP2A is a central functional marker despite having a peripheral position in the co-abundance graph. It controls DNA topology and is involved in chromosome condensation, sister-chromatid segregation, DNA metabolism, and DNA-damage response. It has strong disease relevance across neoplastic and hematologic contexts, extensive literature, and HPA enhancement in lymphoid and proliferative cell populations. Its partial hu.MAP association with PHIP is the clearest complex-level support in the module.
- **Conclusion**: Established evidence supports TOP2A as a marker of DNA topology and proliferative chromosome biology. Its presence suggests that cell proliferation or genome maintenance may contribute to the module, but it does not by itself establish a tissue-specific mechanism.

#### AHCTF1

- **Related proteins** (co-abundance neighbors): PHIP (0.90), SMARCA1 (0.88), ZNF638 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Nuclear membrane, Nuclear bodies; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: AT-hook containing transcription factor 1. Predicted to enable DNA binding activity. Involved in nuclear pore complex assembly and regulation of cytokinesis. Located in nuclear membrane. Colocalizes with chromatin; kinetochore; and nuclear pore outer ring. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.519); lysosomal storage disease (0.306); stricture (0.223); premature birth (0.182); Intellectual disability (0.111)
- **Europe PMC papers**: 392
- **Why important**: AHCTF1 is tied for the strongest connector role and bridges SMARCA1, PHIP, and ZNF638. It is associated with nuclear-pore complex assembly, nucleocytoplasmic transport, chromatin or kinetochore localization, and cytokinesis. HPA places it in nuclear compartments and shows neutrophil-associated cell-type enhancement, which makes it relevant both to nuclear organization and to possible immune-cell composition effects.
- **Conclusion**: Established evidence supports AHCTF1 as a nuclear-pore and cell-division regulator. Its network position makes it a plausible coordinator of the module, but the co-abundance data do not demonstrate direct interaction or causality.

#### PHIP

- **Related proteins** (co-abundance neighbors): AHCTF1 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_07289.1
- **Function (MyGene.info)**: PHIP subunit of CUL4-Ring ligase complex. This gene encodes a protein that binds to the insulin receptor substrate 1 protein and regulates glucose transporter translocation in skeletal muscle cells. The encoded protein may also regulate growth and survival of pancreatic beta cells. Elevated copy number of this gene may be associated with melanoma severity and the encoded protein may promote melanoma metastasis in human patients. [provided…
- **Diseases (Open Targets)**: PHIP-related behavioral problems-intellectual disability-obesity-dysmorphic features syndrome (0.805); Intellectual disability (0.544); hereditary disease (0.543); obesity due to melanocortin 4 receptor deficiency (0.383); obesity disorder (0.383)
- **Europe PMC papers**: 2064
- **Why important**: PHIP is the most literature-supported gene in the module and is the module member paired with TOP2A in (hu.MAP huMAP3_07289.1). Its annotations connect it to a CUL4-Ring ligase complex, chromatin organization, transcriptional regulation, insulin-receptor signaling, cell proliferation, and survival. It has a strong disease association with a PHIP-related intellectual-disability and obesity syndrome, as well as cancer-related associations.
- **Conclusion**: Established evidence supports PHIP as a multifunctional regulator linking chromatin, signaling, and growth. Its relationship with TOP2A is supported by (hu.MAP huMAP3_07289.1), but whether PHIP mediates the shared bone-lung co-abundance pattern remains a hypothesis.

#### ZNF638

- **Related proteins** (co-abundance neighbors): AHCTF1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger protein 638. The protein encoded by this gene is a nucleoplasmic protein. It binds cytidine-rich sequences in double-stranded DNA. This protein has three types of domains: MH1, MH2 (repeated three times) and MH3. It is associated with packaging, transferring, or processing transcripts. Multiple alternatively spliced transcript variants have been found for this gene, but the biological validity of some variants…
- **Diseases (Open Targets)**: intelligence (0.363); atrial fibrillation (0.332); post term pregnancy (0.209); breast benign neoplasm (0.209); atrial flutter (0.197)
- **Europe PMC papers**: 392
- **Why important**: ZNF638 provides a regulatory complement to the chromatin and genome-maintenance genes. It is a nucleoplasmic DNA-binding protein associated with transcript packaging, transfer, processing, and RNA-splicing regulation. Its edge to AHCTF1 places it in the module's nuclear-organization branch, while its disease and trait associations provide additional biological context despite a smaller literature base than TOP2A or PHIP.
- **Conclusion**: Established evidence supports ZNF638 as a nuclear transcriptional and RNA-processing regulator. Its participation is consistent with coordinated nuclear gene control, but there is no direct evidence that it drives the module or physically interacts with AHCTF1.

## Module 10

**Tissue pair**: bone and lung  
**Genes (5)**: MCM2, MCM4, MCM5, MCM6, MCM7

### Function

The module is a coherent DNA-replication and genome-maintenance module composed entirely of MCM2, MCM4, MCM5, MCM6, and MCM7. Every module gene contributes to the globally corrected MCM-complex and DNA-replication findings, including the MCM complex (GO:CC MCM complex; q_global = 3.87e-10), regulation of replication initiation (GO:BP regulation of DNA-templated DNA replication initiation; q_global = 1.76e-09), the DNA-replication preinitiation and CMG complexes (GO:CC DNA replication preinitiation complex; q_global = 2.23e-08)(GO:CC CMG complex; q_global = 2.23e-08), DNA replication (GO:BP DNA-templated DNA replication; q_global = 3.2e-05)(GO:BP DNA replication; q_global = 0.00023), and the KEGG DNA-replication pathway (KEGG DNA replication - Homo sapiens (human); q_global = 4.85e-07). The module also supports helicase activity (GO:MF four-way junction helicase activity; q_global = 2.04e-07)(GO:MF forked DNA-dependent helicase activity; q_global = 2.04e-07)(GO:MF double-stranded DNA helicase activity; q_global = 2.82e-07)(GO:MF 3'-5' DNA helicase activity; q_global = 2.82e-07)(GO:MF single-stranded 3'-5' DNA helicase activity; q_global = 2.82e-07)(GO:MF DNA helicase activity; q_global = 2.23e-06), homologous-recombination and double-strand-break repair processes (GO:BP double-strand break repair via break-induced replication; q_global = 4.92e-09)(KEGG Homologous recombination - Homo sapiens (human); q_global = 8.58e-06)(GO:BP double-strand break repair via homologous recombination; q_global = 2.41e-05)(GO:BP recombinational repair; q_global = 2.66e-05), and cell-cycle DNA replication (KEGG Cell cycle - Homo sapiens (human); q_global = 6.59e-06). Thus, the most defensible interpretation is coordinated abundance of the MCM replicative helicase and associated replication-initiation machinery, likely reflecting proliferative or replication-competent cells in both tissues. The enrichment is biologically specific because the same complete set of module genes drives the principal findings, rather than a mixture of unrelated annotations.

**Cell composition.** This is not a module of plasma proteins or secreted proteins: the HPA summary reports no secreted genes, nucleoplasmic localization, and low immune-cell specificity for every member. However, all members are tissue-enhanced and cell-type-enhanced, with frequent enrichment in bone marrow and progenitor populations including erythrocyte, megakaryocyte, and monocyte progenitors. The lack of enriched mature blood-cell categories, together with the progenitor pattern, is more consistent with proliferative progenitor or precursor-cell abundance than with a plasma-protein signal. The shared bone and lung signal could therefore partly reflect shared or infiltrating proliferative cell populations rather than a tissue-exclusive program. Protein detection in lung is present for most members, whereas MCM2 is not detected there by the supplied HPA evidence; there is no matching HPA bone-tissue protein result. These observations support caution in treating the module as a specialized function of mature bone or lung parenchymal cells.

**GO/KEGG enrichment**: 53 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC MCM complex | 3.87e-10 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication initiation | 1.76e-09 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP double-strand break repair via break-induced replication | 4.92e-09 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP regulation of DNA-templated DNA replication | 4.92e-09 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC DNA replication preinitiation complex | 2.23e-08 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:CC CMG complex | 2.23e-08 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:BP DNA replication initiation | 1.43e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF four-way junction helicase activity | 2.04e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF forked DNA-dependent helicase activity | 2.04e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF double-stranded DNA helicase activity | 2.82e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF 3'-5' DNA helicase activity | 2.82e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded 3'-5' DNA helicase activity | 2.82e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| KEGG DNA replication - Homo sapiens (human) | 4.85e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded DNA helicase activity | 7.93e-07 | MCM2, MCM4, MCM5, MCM6, MCM7 |
| GO:MF single-stranded DNA binding | 1.24e-06 | MCM2, MCM4, MCM5, MCM6, MCM7 |

### STRING and hu.MAP

STRING provides strong prior support for the module: every tested gene pair among MCM2, MCM4, MCM5, MCM6, and MCM7 is a high-confidence interaction. STRING also independently assigns all members to the MCM complex and MCM domains (STRING Component MCM complex; within-query FDR = 5.82e-10)(STRING InterPro MCM domain; within-query FDR = 8.53e-10)(STRING InterPro Mini-chromosome maintenance, conserved site; within-query FDR = 8.53e-10)(STRING InterPro MCM N-terminal domain; within-query FDR = 8.53e-10)(STRING InterPro Mini-chromosome maintenance protein; within-query FDR = 8.53e-10)(STRING InterPro MCM OB domain; within-query FDR = 8.53e-10)(STRING InterPro MCM, AAA-lid domain; within-query FDR = 8.53e-10), and connects the set to the CMG complex, replication initiation, break-induced replication, DNA unwinding, and replication-stress responses (STRING Component CMG complex; within-query FDR = 2.31e-09)(STRING Process Double-strand break repair via break-induced replication; within-query FDR = 6.73e-09)(STRING Process Regulation of DNA-templated DNA replication initiation; within-query FDR = 6.73e-09)(STRING RCTM Unwinding of DNA; within-query FDR = 6.93e-09)(STRING RCTM Activation of the pre-replicative complex; within-query FDR = 6.93e-09)(STRING RCTM Activation of ATR in response to replication stress; within-query FDR = 7.14e-09). These STRING results are supplementary rather than globally corrected enrichment evidence. hu.MAP independently places the complete module set in a compact MCM-containing complex (hu.MAP huMAP3_05529.1) and in several larger assemblies containing MCM3, CDC45, GINS proteins, MCMBP, TIMELESS, TIPIN, and CLSPN (hu.MAP huMAP3_14758.1)(hu.MAP huMAP3_08554.1)(hu.MAP huMAP3_11832.1)(hu.MAP huMAP3_12180.1). Additional hu.MAP complexes contain most of the module, particularly MCM2, MCM4, and MCM6 (hu.MAP huMAP3_06061.1)(hu.MAP huMAP3_07113.1)(hu.MAP huMAP3_09860.1)(hu.MAP huMAP3_02602.1). Therefore, the co-abundance edges are strongly consistent with a pre-existing physical replication complex. The module subgraph captures only part of the broader known MCM and CMG interaction architecture, so its co-abundance structure should not be interpreted as a newly discovered physical complex.

**STRING interactions (score >= 0.7)**: 10 of 10 gene pairs: MCM2–MCM4 (0.999); MCM2–MCM5 (0.999); MCM2–MCM6 (0.999); MCM2–MCM7 (0.999); MCM4–MCM5 (0.999); MCM4–MCM6 (0.999); MCM4–MCM7 (0.999); MCM5–MCM6 (0.999); MCM5–MCM7 (0.999); MCM6–MCM7 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Component MCM complex (FDR = 5.82e-10, 5 genes); COMPARTMENTS MCM complex (FDR = 6.25e-10, 5 genes); InterPro MCM domain (FDR = 8.53e-10, 5 genes); InterPro Mini-chromosome maintenance, conserved site (FDR = 8.53e-10, 5 genes); InterPro MCM N-terminal domain (FDR = 8.53e-10, 5 genes); InterPro Mini-chromosome maintenance protein (FDR = 8.53e-10, 5 genes); InterPro MCM OB domain (FDR = 8.53e-10, 5 genes); InterPro MCM, AAA-lid domain (FDR = 8.53e-10, 5 genes); Component CMG complex (FDR = 2.31e-09, 5 genes); COMPARTMENTS CMG complex (FDR = 2.48e-09, 5 genes); Process Double-strand break repair via break-induced replication (FDR = 6.73e-09, 5 genes); Process Regulation of DNA-templated DNA replication initiation (FDR = 6.73e-09, 5 genes); RCTM Unwinding of DNA (FDR = 6.93e-09, 5 genes); RCTM Activation of the pre-replicative complex (FDR = 6.93e-09, 5 genes); RCTM Activation of ATR in response to replication stress (FDR = 7.14e-09, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05529.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/6); huMAP3_14758.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/14); huMAP3_08554.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_11832.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/15); huMAP3_12180.1 (MCM4, MCM5, MCM7, MCM2, MCM6; 5/17); huMAP3_06061.1 (MCM4, MCM7, MCM2, MCM6; 4/5); huMAP3_07113.1 (MCM4, MCM7, MCM2, MCM6; 4/6); huMAP3_11119.1 (MCM4, MCM5, MCM7, MCM6; 4/14); huMAP3_09860.1 (MCM4, MCM2, MCM6; 3/4); huMAP3_00154.1 (MCM4, MCM2, MCM6; 3/5); huMAP3_09466.1 (MCM4, MCM2, MCM6; 3/23); huMAP3_10862.1 (MCM4, MCM2, MCM6; 3/33); huMAP3_14306.1 (MCM4, MCM2, MCM6; 3/55); huMAP3_02602.1 (MCM4, MCM6; 2/2); huMAP3_09238.1 (MCM5, MCM7; 2/11); huMAP3_08848.1 (MCM4, MCM6; 2/15)

### Novelty

The molecular function and core protein assembly are not new: the complete gene set is a canonical MCM complex, has dense high-confidence STRING support, and repeatedly occurs in hu.MAP complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_08848.1). Absence of a relationship from either resource would not by itself establish novelty, and here the opposite pattern is observed. The potentially novel aspect is the observation that these known replication proteins form a conserved co-abundance module across bone and lung in the analyzed dataset. That cross-tissue co-abundance observation may be useful, but it does not establish a new mechanism or tissue-specific role. A claim of a new finding would require independent replication, comparison with prior tissue co-expression studies, and evidence that the signal is not driven by shared progenitor-cell composition or proliferation state.

**Hypothesis.** Mechanistic hypothesis: the module reflects coordinated abundance of the MCM helicase core in replication-competent progenitor or precursor cells shared between bone-associated and lung samples. In this model, MCM2, MCM4, MCM5, MCM6, and MCM7 assemble with the broader pre-replication and CMG machinery, license or support replication-fork progression, and help protect or restart stalled forks through replication-stress and repair pathways, consistent with (GO:BP regulation of DNA-templated DNA replication initiation; q_global = 1.76e-09)(GO:BP double-strand break repair via break-induced replication; q_global = 4.92e-09)(GO:CC CMG complex; q_global = 2.23e-08)(KEGG Homologous recombination - Homo sapiens (human); q_global = 8.58e-06)(GO:BP double-strand break repair via homologous recombination; q_global = 2.41e-05) and (5 supplementary STRING terms; within-query FDR 6.73e-09–7.14e-09). The tissue-level signal may therefore arise from a shared abundance of cycling or progenitor cells rather than from a lung-specific or bone-specific biochemical pathway. This is a hypothesis: the supplied co-abundance data and annotations do not demonstrate physical assembly in these particular samples, cell proliferation, replication stress, or causal activity.

### Important genes

#### MCM6

- **Related proteins** (co-abundance neighbors): MCM4 (0.92), MCM5 (0.84); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 6. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: lactose intolerance (0.246); neurodegenerative disease (0.225); obesity disorder (0.166); nervous system disorder (0.141); systemic lupus erythematosus (0.140)
- **Europe PMC papers**: 3766
- **Why important**: MCM6 occupies the strongest weighted-degree position in the module subgraph and connects directly to MCM4 and MCM5. It participates in every principal globally corrected MCM, replication, helicase, repair, and cell-cycle annotation, including (50 globally significant GO/KEGG terms, q_global 3.87e-10–0.0138; see the table). It is also present across the broadest set of hu.MAP complexes listed for the module, including the compact MCM assembly (hu.MAP huMAP3_05529.1) and multiple larger replication-related assemblies. HPA links it to lymphoid tissue and several hematopoietic progenitor populations, while the supplied literature and disease resources show substantial study and disease associations.
- **Conclusion**: Established: MCM6 is a core MCM-complex component with strong network, GO/KEGG, STRING, hu.MAP, and HPA support. Hypothesis: its prominent co-abundance position may make it a useful marker of the shared replication-competent cell state, but the data do not show that MCM6 independently drives the module.

#### MCM7

- **Related proteins** (co-abundance neighbors): MCM5 (0.87), MCM2 (0.85); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM5 (0.999), MCM6 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 7. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication…
- **Diseases (Open Targets)**: Spastic paraplegia (0.532); Meier-Gorlin syndrome (0.531); AP-4 deficiency syndrome (0.529); microcephaly (0.473); Trichiasis (0.425)
- **Europe PMC papers**: 4587
- **Why important**: MCM7 has a high weighted-degree position and links to MCM5 and MCM2 in the co-abundance subgraph. It is included in the complete MCM-complex and replication findings (34 globally significant GO/KEGG terms, q_global 3.87e-10–0.000728; see the table) and in the STRING and hu.MAP assemblies (15 supplementary STRING terms; within-query FDR 5.82e-10–7.14e-09)(hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1)(hu.MAP huMAP3_09238.1). HPA associates it with bone marrow and progenitor populations, and the supplied disease associations include Meier-Gorlin syndrome, spastic paraplegia, AP-4 deficiency syndrome, and microcephaly. It also has a substantial literature base.
- **Conclusion**: Established: MCM7 is a well-supported replication-initiation and helicase-complex component with relevant developmental disease associations. Hypothesis: its position may help report coordinated replication capacity in the shared bone-lung cell population, but the module cannot establish that the disease associations explain the tissue pattern.

#### MCM5

- **Related proteins** (co-abundance neighbors): MCM7 (0.87), MCM6 (0.84); STRING partners: MCM2 (0.999), MCM4 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_11119.1, huMAP3_09238.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 5. The protein encoded by this gene is structurally very similar to the CDC46 protein from S. cerevisiae, a protein involved in the initiation of DNA replication. The encoded protein is a member of the MCM family of chromatin-binding proteins and can interact with at least two other members of this family. The encoded protein is upregulated in the transition from the G0 to G1/S phase of the cell cycl…
- **Diseases (Open Targets)**: Meier-Gorlin syndrome (0.563); neurodegenerative disease (0.397); lysosomal storage disease (0.362); kidney transplant (0.198); diabetic ketoacidosis (0.129)
- **Europe PMC papers**: 4143
- **Why important**: MCM5 has a strong weighted-degree position and connects to MCM7 and MCM6. It contributes to the complete MCM and DNA-replication enrichment pattern (34 globally significant GO/KEGG terms, q_global 3.87e-10–0.000728; see the table) and to the STRING and hu.MAP evidence (15 supplementary STRING terms; within-query FDR 5.82e-10–7.14e-09)(hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1)(hu.MAP huMAP3_11119.1)(hu.MAP huMAP3_09238.1). MyGene evidence describes a role in replication initiation and transition toward the proliferative cell-cycle state. HPA places it in bone marrow and several progenitor populations, and the supplied resources associate it with Meier-Gorlin syndrome and other disorders. Its literature volume is substantial.
- **Conclusion**: Established: MCM5 is a conserved replication factor associated with cell-cycle entry and the MCM assembly. Hypothesis: its abundance may track proliferative activation in shared progenitor populations, but co-abundance alone cannot distinguish cell number from per-cell regulation.

#### MCM4

- **Related proteins** (co-abundance neighbors): MCM6 (0.92); STRING partners: MCM2 (0.999), MCM5 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_11119.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1, huMAP3_02602.1, huMAP3_08848.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 4. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication rel…
- **Diseases (Open Targets)**: primary immunodeficiency with natural-killer cell deficiency and adrenal insufficiency (0.714); X-linked adrenal hypoplasia congenita (0.185); lung adenocarcinoma (0.112); microcephaly (0.111); neoplasm (0.102)
- **Europe PMC papers**: 4082
- **Why important**: MCM4 is directly connected to MCM6 in the module and is one of the most broadly represented members across the listed hu.MAP complexes, including the compact MCM assembly and larger replication assemblies (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1) (hu.MAP huMAP3_02602.1) (hu.MAP huMAP3_09238.1) (hu.MAP huMAP3_08848.1). It contributes to every principal MCM, replication, helicase, repair, and cell-cycle finding (53 globally significant GO/KEGG terms, q_global 3.87e-10–0.024; see the table). HPA links it to bone marrow and progenitor cell types. The supplied disease associations include primary immunodeficiency with natural-killer-cell deficiency and adrenal insufficiency, as well as lung adenocarcinoma.
- **Conclusion**: Established: MCM4 is a core replication-complex component with extensive complex-level support and disease relevance. Hypothesis: its connection to lung adenocarcinoma may be biologically compatible with proliferative biology, but the supplied module does not establish a cancer-specific process or causal relationship.

#### MCM2

- **Related proteins** (co-abundance neighbors): MCM7 (0.85); STRING partners: MCM4 (0.999), MCM5 (0.999), MCM6 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05529.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_06061.1, huMAP3_07113.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is a canonical member of the MCM helicase and replication-initiation machinery and contributes to all globally corrected module annotations (53 globally significant GO/KEGG terms, q_global 3.87e-10–0.024; see the table). It connects to MCM7 in the module and to every other module member in STRING, while appearing in many hu.MAP complexes (hu.MAP huMAP3_05529.1) (hu.MAP huMAP3_14758.1) (hu.MAP huMAP3_08554.1) (hu.MAP huMAP3_11832.1) (hu.MAP huMAP3_12180.1) (hu.MAP huMAP3_06061.1) (hu.MAP huMAP3_07113.1) (hu.MAP huMAP3_11119.1) (hu.MAP huMAP3_09860.1) (hu.MAP huMAP3_00154.1) (hu.MAP huMAP3_09466.1) (hu.MAP huMAP3_10862.1) (hu.MAP huMAP3_14306.1). HPA identifies bone marrow and lymphoid tissue enhancement and enrichment in several progenitor populations. MCM2 has the largest literature volume among the module genes in the supplied evidence and has multiple disease associations in Open Targets.
- **Conclusion**: Established: MCM2 is a heavily studied, conserved replication-initiation factor and a strong biological anchor for the module. Hypothesis: its absence of lung protein detection in the supplied HPA result may reflect measurement or cell-composition differences, but it cannot by itself refute the lung co-abundance signal.

## Module 11

**Tissue pair**: bone and lung  
**Genes (12)**: MGME1, PTCD3, MRPL11, MRPL48, MRPL55, MRPS11, MRPS15, MRPS18B, MRPS22, MRPS23, MRPS27, LARS2

### Function

The module is strongly and coherently associated with mitochondrial protein synthesis. The primary GO and KEGG evidence includes organellar and mitochondrial ribosome, mitochondrial translation, mitochondrial gene expression, ribosomal subunits, translation, protein biosynthesis, mitochondrial matrix and inner-membrane localization, and structural ribosome activity (24 globally significant GO/KEGG terms, q_global 1.58e-13–0.0175; see the table). The enrichment is not driven by a single annotation: nearly the entire module contributes to the mitochondrial translation signal, while the ribosomal subunit evidence is concentrated across both small- and large-subunit proteins. STRING independently supports mitochondrial ribosome assembly and mitochondrial translation (15 supplementary STRING terms; within-query FDR 3.02e-14–9.83e-10). Thus, the best-supported interpretation is a conserved mitochondrial gene-expression and mitoribosome module, likely reflecting coordinated abundance of mitoribosome components rather than a tissue-specific signaling pathway.

**Cell composition.** The module is composed almost entirely of mitochondrial ribosomal proteins and closely related mitochondrial gene-expression factors. HPA reports low tissue specificity for every module gene and low immune-cell specificity for every module gene, with no enriched blood-cell category. Only one gene is annotated as secreted, while the module is overwhelmingly intracellular and mitochondrial. Protein detection is broad in lung, and the available HPA summary provides no matching bone tissue result. These observations argue against a plasma-protein or blood-cell contamination explanation. They are more consistent with a broadly expressed housekeeping-type mitochondrial program that can be shared across bone and lung, although sample cellular composition and general mitochondrial content could still contribute to the co-abundance pattern. Cell-type-enhanced annotations occur for some genes, including reproductive, neural, epithelial and trophoblast-related cell types, but no single cell type dominates the module.

**GO/KEGG enrichment**: 24 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC organellar ribosome | 1.58e-13 | MRPL11, MRPL48, MRPL55, MRPS11, MRPS15, MRPS18B, MRPS22, MRPS23, MRPS27, PTCD3 |
| GO:CC mitochondrial ribosome | 1.58e-13 | MRPL11, MRPL48, MRPL55, MRPS11, MRPS15, MRPS18B, MRPS22, MRPS23, MRPS27, PTCD3 |
| GO:BP mitochondrial translation | 6.06e-13 | LARS2, MRPL11, MRPL48, MRPL55, MRPS11, MRPS15, MRPS18B, MRPS22, MRPS23, MRPS27, PTCD3 |
| GO:CC ribosomal subunit | 5.04e-12 | MRPL11, MRPL48, MRPL55, MRPS11, MRPS15, MRPS18B, MRPS22, MRPS23, MRPS27, PTCD3 |
| KEGG Ribosome - Homo sapiens (human) | 5.04e-12 | MRPL11, MRPL48, MRPL55, MRPS11, MRPS15, MRPS18B, MRPS22, MRPS23, MRPS27, PTCD3 |
| GO:BP mitochondrial gene expression | 1.34e-11 | LARS2, MRPL11, MRPL48, MRPL55, MRPS11, MRPS15, MRPS18B, MRPS22, MRPS23, MRPS27, PTCD3 |
| GO:CC ribosome | 2.85e-10 | MRPL11, MRPL48, MRPL55, MRPS11, MRPS15, MRPS18B, MRPS22, MRPS23, MRPS27, PTCD3 |
| GO:CC mitochondrial protein-containing complex | 3.46e-10 | MRPL11, MRPL48, MRPL55, MRPS11, MRPS15, MRPS18B, MRPS22, MRPS23, MRPS27, PTCD3 |
| GO:CC organellar small ribosomal subunit | 3.04e-09 | MRPS11, MRPS15, MRPS18B, MRPS22, MRPS23, MRPS27, PTCD3 |
| GO:CC mitochondrial small ribosomal subunit | 3.04e-09 | MRPS11, MRPS15, MRPS18B, MRPS22, MRPS23, MRPS27, PTCD3 |
| GO:CC small ribosomal subunit | 2.26e-08 | MRPS11, MRPS15, MRPS18B, MRPS22, MRPS23, MRPS27, PTCD3 |
| GO:BP translation | 2.16e-07 | LARS2, MRPL11, MRPL48, MRPL55, MRPS11, MRPS15, MRPS18B, MRPS22, MRPS23, MRPS27, PTCD3 |
| GO:BP protein biosynthetic process | 2.16e-07 | LARS2, MRPL11, MRPL48, MRPL55, MRPS11, MRPS15, MRPS18B, MRPS22, MRPS23, MRPS27, PTCD3 |
| GO:CC mitochondrial matrix | 3.24e-07 | LARS2, MRPL11, MRPL48, MRPL55, MRPS11, MRPS15, MRPS18B, MRPS22, MRPS23, MRPS27, PTCD3 |
| GO:CC mitochondrial inner membrane | 5.13e-07 | MRPL11, MRPL48, MRPL55, MRPS11, MRPS15, MRPS18B, MRPS22, MRPS23, MRPS27, PTCD3 |

### STRING and hu.MAP

STRING shows dense, high-confidence relationships among the mitochondrial ribosomal proteins, including extensive links connecting the small-subunit and large-subunit members and PTCD3 [the listed STRING interactions]. The supplementary STRING categories independently recover mitochondrial ribosome, mitochondrial translation, translation initiation, elongation and termination (15 supplementary STRING terms; within-query FDR 3.02e-14–9.83e-10). hu.MAP provides direct complex-level support: the small-subunit genes cluster in complexes C1 and C2, while the large-subunit genes cluster in C3 and C4; additional complexes contain subsets involving MRPS27, MRPS18B, MRPL55 and MRPL11 (hu.MAP huMAP3_05807.1) (hu.MAP huMAP3_05954.1) (hu.MAP huMAP3_06439.1) (hu.MAP huMAP3_06589.1) (hu.MAP huMAP3_08562.1) (hu.MAP huMAP3_04652.1) (hu.MAP huMAP3_06550.1) (hu.MAP huMAP3_07939.1) (hu.MAP huMAP3_08458.1) (hu.MAP huMAP3_09113.1) (hu.MAP huMAP3_09483.1). The module therefore contains relationships already known from physical-complex and functional-association resources. Its co-abundance structure is biologically plausible and likely reflects coordinated abundance of a mitochondrial translation apparatus, not merely coincidental gene co-expression. MGME1 and LARS2 extend the module toward mitochondrial genome maintenance and mitochondrial aminoacyl-tRNA charging, respectively, but neither has a reported STRING interaction or hu.MAP complex in this fact sheet.

**STRING interactions (score >= 0.7)**: 45 of 66 gene pairs: MRPL11–MRPL48 (0.91); MRPL11–MRPL55 (0.885); MRPL11–MRPS11 (0.997); MRPL11–MRPS15 (0.998); MRPL11–MRPS18B (0.952); MRPL11–MRPS22 (0.948); MRPL11–MRPS23 (0.944); MRPL11–MRPS27 (0.931); MRPL11–PTCD3 (0.888); MRPL48–MRPL55 (0.951); MRPL48–MRPS11 (0.9); MRPL48–MRPS15 (0.922); MRPL48–MRPS18B (0.933); MRPL48–MRPS22 (0.932); MRPL48–MRPS23 (0.922); MRPL48–MRPS27 (0.897); MRPL48–PTCD3 (0.917); MRPL55–MRPS11 (0.913); MRPL55–MRPS15 (0.926); MRPL55–MRPS18B (0.885); MRPL55–MRPS22 (0.879); MRPL55–MRPS23 (0.881); MRPL55–MRPS27 (0.876); MRPL55–PTCD3 (0.824); MRPS11–MRPS15 (0.999); MRPS11–MRPS18B (0.997); MRPS11–MRPS22 (0.998); MRPS11–MRPS23 (0.995); MRPS11–MRPS27 (0.996); MRPS11–PTCD3 (0.996); MRPS15–MRPS18B (0.996); MRPS15–MRPS22 (0.998); MRPS15–MRPS23 (0.995); MRPS15–MRPS27 (0.999); MRPS15–PTCD3 (0.994); MRPS18B–MRPS22 (0.999); MRPS18B–MRPS23 (0.983); MRPS18B–MRPS27 (0.999); MRPS18B–PTCD3 (0.993); MRPS22–MRPS23 (0.997); MRPS22–MRPS27 (0.999); MRPS22–PTCD3 (0.999); MRPS23–MRPS27 (0.996); MRPS23–PTCD3 (0.996); MRPS27–PTCD3 (0.996)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Mitochondrial ribosome (FDR = 3.02e-14, 10 genes); Process Mitochondrial translation (FDR = 3.03e-14, 11 genes); COMPARTMENTS Mitochondrial ribosome (FDR = 3.24e-14, 10 genes); NetworkNeighborAL Organellar ribosome (FDR = 3.79e-14, 10 genes); RCTM Mitochondrial translation initiation (FDR = 4.52e-14, 10 genes); RCTM Mitochondrial translation elongation (FDR = 4.52e-14, 10 genes); RCTM Mitochondrial translation termination (FDR = 4.52e-14, 10 genes); Keyword Ribosomal protein (FDR = 9.46e-14, 10 genes); Component Ribosomal subunit (FDR = 1.17e-13, 10 genes); COMPARTMENTS Ribosomal subunit (FDR = 2.74e-12, 9 genes); RCTM Translation (FDR = 4.65e-12, 11 genes); Component Mitochondrial small ribosomal subunit (FDR = 2.36e-10, 7 genes); Component Mitochondrial protein-containing complex (FDR = 2.36e-10, 10 genes); COMPARTMENTS Mitochondrial matrix (FDR = 4.7e-10, 11 genes); Component Mitochondrial matrix (FDR = 9.83e-10, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05807.1 (MRPS11, MRPS15, MRPS27, PTCD3, MRPS23, MRPS18B; 6/81); huMAP3_05954.1 (MRPS22, MRPS11, MRPS15, PTCD3, MRPS23; 5/28); huMAP3_06439.1 (MRPL55, MRPL48, MRPL11; 3/57); huMAP3_06589.1 (MRPL55, MRPL48, MRPL11; 3/79); huMAP3_08562.1 (MRPS27, MRPS18B; 2/6); huMAP3_04652.1 (MRPL55, MRPL11; 2/30); huMAP3_06550.1 (MRPL55, MRPL11; 2/62); huMAP3_07939.1 (MRPL55, MRPL11; 2/68); huMAP3_08458.1 (MRPL55, MRPL11; 2/70); huMAP3_09113.1 (MRPL55, MRPL11; 2/72); huMAP3_09483.1 (MRPL55, MRPL11; 2/74)

### Novelty

This module should not be described as a newly discovered mitochondrial ribosome complex: the component functions and many relationships are already established by GO, KEGG, STRING and hu.MAP (24 globally significant GO/KEGG terms, q_global 1.58e-13–0.0175; see the table), (15 supplementary STRING terms; within-query FDR 3.02e-14–9.83e-10), (hu.MAP huMAP3_05807.1) (hu.MAP huMAP3_05954.1) (hu.MAP huMAP3_06439.1) (hu.MAP huMAP3_06589.1) (hu.MAP huMAP3_08562.1) (hu.MAP huMAP3_04652.1) (hu.MAP huMAP3_06550.1) (hu.MAP huMAP3_07939.1) (hu.MAP huMAP3_08458.1) (hu.MAP huMAP3_09113.1) (hu.MAP huMAP3_09483.1). The potentially novel aspect is the conserved co-abundance pattern across bone and lung, particularly the way canonical mitoribosome components occur together with PTCD3, LARS2 and MGME1. However, the fact sheet does not provide an external replication cohort, perturbation evidence, comparison with previously published tissue modules, or a literature search demonstrating that this exact cross-tissue module is absent. Therefore the defensible conclusion is that the module may represent a useful tissue-pair-specific co-abundance observation, but its novelty as a biological mechanism remains unproven. Absence of a STRING or hu.MAP record by itself would not establish novelty.

**Hypothesis.** Hypothesis: bone and lung samples share a conserved mitochondrial translational-capacity program in which coordinated abundance of mitoribosome small- and large-subunit proteins supports mitochondrial gene expression and production of mitochondrially encoded respiratory-chain components. PTCD3 may help connect ribosomal RNA or small-subunit functions with the broader mitoribosome assembly state, while LARS2 could couple the program to accurate mitochondrial tRNA charging and MGME1 could couple it to maintenance of the mitochondrial genome. This model predicts that module abundance will track mitochondrial translation and respiratory capacity, but the co-abundance data alone do not establish causality, physical assembly of the complete module, or a bone- and lung-specific mechanism.

### Important genes

#### PTCD3

- **Related proteins** (co-abundance neighbors): MGME1 (0.93), LARS2 (0.84), MRPL55 (0.83), MRPS15 (0.81); STRING partners: MRPL11 (0.888), MRPL48 (0.917), MRPL55 (0.824), MRPS11 (0.996), MRPS15 (0.994), MRPS18B (0.993), MRPS22 (0.999), MRPS23 (0.996), MRPS27 (0.996)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_05807.1, huMAP3_05954.1
- **Function (MyGene.info)**: pentatricopeptide repeat domain 3. Enables rRNA binding activity and ribosomal small subunit binding activity. Involved in mitochondrial translation. Located in several cellular components, including cytosol; mitochondrion; and nucleoplasm. Implicated in combined oxidative phosphorylation deficiency 51. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: combined oxidative phosphorylation deficiency 51 (0.678); mixed connective tissue disease (0.230); hereditary disease (0.193); alcohol drinking (0.110); posterior cortical atrophy (0.074)
- **Europe PMC papers**: 308
- **Why important**: PTCD3 is a mitochondrial RNA-associated factor with rRNA-binding and small-subunit-binding activities and a direct role in mitochondrial translation. It is among the more connected module genes, links to both the ribosomal proteins and the peripheral mitochondrial factors, is present in the small-subunit hu.MAP complexes (hu.MAP huMAP3_05807.1) and (hu.MAP huMAP3_05954.1), and participates in the core mitochondrial translation evidence (24 globally significant GO/KEGG terms, q_global 1.58e-13–0.0175; see the table), (15 supplementary STRING terms; within-query FDR 3.02e-14–9.83e-10). Its disease association with combined oxidative phosphorylation deficiency gives the module a clinically relevant anchor, and its literature record is substantial.
- **Conclusion**: Established evidence supports PTCD3 as a functional bridge between mitochondrial RNA handling and mitoribosome activity. It is reasonable to hypothesize that PTCD3 helps organize or stabilize the observed module, but the co-abundance network does not prove that it is the causal organizer.

#### MRPS22

- **Related proteins** (co-abundance neighbors): MRPS27 (0.92), MRPL11 (0.86), MRPS23 (0.86), MRPL48 (0.85), MRPL55 (0.83); STRING partners: MRPL11 (0.948), MRPL48 (0.932), MRPL55 (0.879), MRPS11 (0.998), MRPS15 (0.998), MRPS18B (0.999), MRPS23 (0.997), MRPS27 (0.999), PTCD3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_05954.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein S22. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: hypotonia with lactic acidemia and hyperammonemia (0.787); 46 XX gonadal dysgenesis (0.631); neurodegenerative disease (0.525); androgenetic alopecia (0.507); hereditary disease (0.495)
- **Europe PMC papers**: 448
- **Why important**: MRPS22 is a mitochondrial small-subunit ribosomal protein and one of the most connected genes in the module. It links to both large- and small-subunit members, appears across all primary enrichment categories (24 globally significant GO/KEGG terms, q_global 1.58e-13–0.0175; see the table), is represented in hu.MAP complex C2, and has strong STRING support with the other module components. Its disease associations include mitochondrial and developmental phenotypes, and it has a substantial literature record.
- **Conclusion**: Established evidence identifies MRPS22 as a core small-subunit component of the mitochondrial translation apparatus and a central network node. Its position makes it a strong marker of module activity, but does not demonstrate that changes in MRPS22 initiate the shared bone–lung program.

#### MRPS23

- **Related proteins** (co-abundance neighbors): MRPL55 (0.94), MRPS22 (0.86), MRPS18B (0.81), MRPS11 (0.81); STRING partners: MRPL11 (0.944), MRPL48 (0.922), MRPL55 (0.881), MRPS11 (0.995), MRPS15 (0.995), MRPS18B (0.983), MRPS22 (0.997), MRPS27 (0.996), PTCD3 (0.996)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_05807.1, huMAP3_05954.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein S23. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.495); combined oxidative phosphorylation deficiency 46 (0.399); tendon sheath disorder (0.307); gout (0.204); liver disorder (0.186)
- **Europe PMC papers**: 362
- **Why important**: MRPS23 is a mitochondrial small-subunit ribosomal protein with a relatively central position in the module and strong connections to both small-subunit and large-subunit proteins. It is present in the primary mitochondrial ribosome and translation annotations (24 globally significant GO/KEGG terms, q_global 1.58e-13–0.0175; see the table), in hu.MAP complexes C1 and C2, and throughout the corresponding STRING evidence. Its disease associations include combined oxidative phosphorylation deficiency and other systemic disorders, while its literature support is substantial.
- **Conclusion**: Established evidence supports MRPS23 as a core component of the coordinated mitoribosome signal. Its cross-subunit connectivity suggests a useful module marker, whereas any specific role in coupling bone and lung biology remains hypothetical.

#### MRPL55

- **Related proteins** (co-abundance neighbors): MRPS23 (0.94), MRPS22 (0.83), PTCD3 (0.83), MRPS18B (0.82), MRPL48 (0.80); STRING partners: MRPL11 (0.885), MRPL48 (0.951), MRPS11 (0.913), MRPS15 (0.926), MRPS18B (0.885), MRPS22 (0.879), MRPS23 (0.881), MRPS27 (0.876), PTCD3 (0.824)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in lung
- **hu.MAP 3.0**: huMAP3_06439.1, huMAP3_06589.1, huMAP3_04652.1, huMAP3_06550.1, huMAP3_07939.1, huMAP3_08458.1, huMAP3_09113.1, huMAP3_09483.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein L55. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.486); hypertensive disorder (0.071); essential hypertension (0.057); atrial fibrillation (0.043); cardiovascular disorder (0.038)
- **Europe PMC papers**: 192
- **Why important**: MRPL55 is a mitochondrial large-subunit ribosomal protein and one of the more connected genes in the co-abundance graph. It links to the small-subunit proteins, occurs in several hu.MAP large-subunit complexes (hu.MAP huMAP3_06439.1), (hu.MAP huMAP3_06589.1), (hu.MAP huMAP3_04652.1) (hu.MAP huMAP3_06550.1) (hu.MAP huMAP3_07939.1) (hu.MAP huMAP3_08458.1) (hu.MAP huMAP3_09113.1) (hu.MAP huMAP3_09483.1), and is supported by the primary mitochondrial translation, ribosome and protein-biosynthesis annotations (8 globally significant GO/KEGG terms, q_global 1.58e-13–3.46e-10; see the table), (13 globally significant GO/KEGG terms, q_global 2.16e-07–0.0175; see the table). Its disease associations include neurodegenerative and cardiovascular-related conditions, and it has a substantial literature record.
- **Conclusion**: Established evidence supports MRPL55 as a large-subunit representative of the module's core mitoribosome program. Its network position makes it informative for tracking coordinated mitochondrial translation, but no fact-sheet evidence shows that it has a unique regulatory role.

#### LARS2

- **Related proteins** (co-abundance neighbors): PTCD3 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in lung
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: leucyl-tRNA synthetase 2, mitochondrial. This gene encodes a class 1 aminoacyl-tRNA synthetase, mitochondrial leucyl-tRNA synthetase. Each of the twenty aminoacyl-tRNA synthetases catalyzes the aminoacylation of a specific tRNA or tRNA isoaccepting family with the cognate amino acid. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: Perrault syndrome 4 (0.797); hydrops-lactic acidosis-sideroblastic anemia-multisystemic failure syndrome (0.772); Perrault syndrome (0.738); myopathy, lactic acidosis, and sideroblastic anemia (0.698); neurodegenerative disease (0.550)
- **Europe PMC papers**: 1026
- **Why important**: LARS2 supplies a functionally distinct link to mitochondrial translation by catalyzing mitochondrial leucyl-tRNA aminoacylation and contributing to translational fidelity. It appears in the primary mitochondrial translation and mitochondrial gene-expression terms (GO:BP mitochondrial translation; q_global = 6.06e-13), (GO:BP mitochondrial gene expression; q_global = 1.34e-11), (GO:BP translation; q_global = 2.16e-07) (GO:BP protein biosynthetic process; q_global = 2.16e-07) (GO:CC mitochondrial matrix; q_global = 3.24e-07), (GO:CC mitochondrion; q_global = 6.11e-05), (GO:BP protein metabolic process; q_global = 0.0175), and connects in the module to PTCD3. Its disease associations include Perrault syndrome and multisystem mitochondrial disorders, and it has the largest literature record among the highlighted genes.
- **Conclusion**: Established evidence supports LARS2 as the module's aminoacyl-tRNA charging component rather than a ribosomal structural protein. Its co-abundance with PTCD3 and the mitoribosome genes suggests coordination between tRNA charging and translation, but this coupling is a hypothesis rather than a demonstrated mechanism.
